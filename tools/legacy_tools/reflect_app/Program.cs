using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Collections;
using GameRes;

class Extractor {
    static void Main(string[] args) {
        string datPath = Path.Combine("GameData", "Formats.dat");
        using (Stream s = File.OpenRead(datPath)) {
            FormatCatalog.Instance.DeserializeScheme(s);
        }

        string arcPath = @"E:\SteamLibrary\steamapps\common\MaitetsuLastRun\others.xp3";
        string outDir = @"E:\MaitetsuProject\steam_version_patch_vn\extracted_assets\others";
        Directory.CreateDirectory(outDir);

        var arcFormats = Assembly.LoadFrom("ArcFormats.dll");
        var xp3OpenerType = arcFormats.GetType("GameRes.Formats.KiriKiri.Xp3Opener");
        var format = FormatCatalog.Instance.ArcFormats.FirstOrDefault(a => a.GetType().Name == "Xp3Opener");

        var schemeProp = xp3OpenerType.GetProperty("Scheme");
        var schemeObj = schemeProp.GetValue(format, null);
        var knownSchemesField = schemeObj.GetType().GetField("KnownSchemes", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
        var knownSchemes = (IDictionary)knownSchemesField.GetValue(schemeObj);

        object maitetsuCrypt = null;
        foreach (DictionaryEntry entry in knownSchemes) {
            string k = entry.Key.ToString();
            if (k == "Maitetsu - Last Run!!") {
                maitetsuCrypt = entry.Value;
                Console.WriteLine("Found scheme: " + k);
                break;
            }
        }

        var forceQueryField = xp3OpenerType.GetField("ForceEncryptionQuery", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
        if (forceQueryField != null) forceQueryField.SetValue(format, false);

        var noCryptField = xp3OpenerType.GetField("NoCryptAlgorithm", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
        if (noCryptField != null && maitetsuCrypt != null) {
            noCryptField.SetValue(format, maitetsuCrypt);
        }

        using (var file = new ArcView(arcPath)) {
            using (var arc = format.TryOpen(file)) {
                if (arc != null) {
                    Console.WriteLine("Archive opened! Total entries: " + arc.Dir.Count);
                    int count = 0;
                    foreach (var entry in arc.Dir) {
                        if (entry.Name.EndsWith(".tjs") || entry.Name.EndsWith(".csv") || entry.Name.EndsWith(".ini")) {
                            string dest = Path.Combine(outDir, entry.Name.Replace('/', Path.DirectorySeparatorChar));
                            var dir = Path.GetDirectoryName(dest);
                            if (dir != null) Directory.CreateDirectory(dir);
                            using (var srcStream = arc.OpenEntry(entry))
                            using (var dstStream = File.Create(dest)) {
                                srcStream.CopyTo(dstStream);
                            }
                            count++;
                            if (count <= 5) {
                                Console.WriteLine("Extracted: " + entry.Name);
                            }
                        }
                    }
                    Console.WriteLine("Total extracted: " + count + " files");
                } else {
                    Console.WriteLine("TryOpen returned null!");
                }
            }
        }
    }
}
