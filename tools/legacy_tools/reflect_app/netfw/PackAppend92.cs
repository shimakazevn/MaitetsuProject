
using System;
using System.IO;
using System.Reflection;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            string inputFolder = @"E:\まいてつ Last Run!!\patch_append92_extracted";
            string outputFile = @"E:\まいてつ Last Run!!\patch_append92.xp3";
            
            Console.WriteLine("Initializing GameRes catalog...");
            var gameRes = Assembly.LoadFrom("GameRes.dll");
            var arcFormats = Assembly.LoadFrom("ArcFormats.dll");
            
            Type catalogType = gameRes.GetType("GameRes.FormatCatalog");
            var catalog = catalogType.GetProperty("Instance").GetValue(null);
            
            // Deserialize schemes
            var deserializeMethod = catalogType.GetMethod("DeserializeScheme", new[] { typeof(Stream) });
            string formatsPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "GameData", "Formats.dat");
            using (var stream = File.OpenRead(formatsPath))
            {
                deserializeMethod.Invoke(catalog, new object[] { stream });
            }
            Console.WriteLine("Deserialized scheme database.");

            // Find Maitetsu - Last Run!! scheme
            Type xp3OpenerType = arcFormats.GetType("GameRes.Formats.KiriKiri.Xp3Opener");
            var knownSchemesProp = xp3OpenerType.GetProperty("KnownSchemes", BindingFlags.Public | BindingFlags.Static);
            var knownSchemes = (System.Collections.IDictionary)knownSchemesProp.GetValue(null);
            
            object scheme = knownSchemes["Maitetsu - Last Run!!"];
            if (scheme == null)
            {
                throw new Exception("Maitetsu - Last Run!! scheme not found!");
            }
            Console.WriteLine("Found Maitetsu - Last Run!! scheme.");

            // Find Xp3Opener instance in catalog
            var arcFormatsProp = catalogType.GetProperty("ArcFormats");
            var formats = (IEnumerable<object>)arcFormatsProp.GetValue(catalog);
            object xp3Opener = null;
            foreach (var f in formats)
            {
                if (f.GetType().Name == "Xp3Opener")
                {
                    xp3Opener = f;
                    break;
                }
            }
            if (xp3Opener == null)
            {
                throw new Exception("Xp3Opener format not found in catalog!");
            }

            // Build list of Entry
            Type entryType = gameRes.GetType("GameRes.Entry");
            var entryList = new System.Collections.ArrayList();

            // Set current directory to inputFolder so relative paths work
            string originalCwd = Directory.GetCurrentDirectory();
            Directory.SetCurrentDirectory(inputFolder);

            // Get all files in inputFolder recursively
            var allFiles = Directory.GetFiles(".", "*", SearchOption.AllDirectories);
            Console.WriteLine("Found " + allFiles.Length + " files to pack.");

            foreach (var file in allFiles)
            {
                // Normalize path to relative path with forward slashes
                string relPath = file.Replace(".\\", "").Replace(".\\", "").Replace("\\", "/");
                if (relPath.StartsWith("./"))
                    relPath = relPath.Substring(2);
                
                // Instantiate Entry
                object entry = Activator.CreateInstance(entryType);
                entryType.GetProperty("Name").SetValue(entry, relPath, null);
                
                // Detect type by extension
                string ext = Path.GetExtension(relPath).ToLower();
                string type = "binary";
                if (ext == ".tlg" || ext == ".png" || ext == ".jpg" || ext == ".bmp")
                    type = "image";
                else if (ext == ".ogg" || ext == ".wav")
                    type = "audio";
                else if (ext == ".txt" || ext == ".tjs" || ext == ".scn")
                    type = "script";
                
                entryType.GetProperty("Type").SetValue(entry, type, null);
                entryList.Add(entry);
                Console.WriteLine("  Added entry: " + relPath + " (Type: " + type + ")");
            }

            // Convert entryList to Entry[]
            Array entryArray = Array.CreateInstance(entryType, entryList.Count);
            entryList.CopyTo(entryArray);

            // Set up Xp3Options
            Type xp3OptionsType = arcFormats.GetType("GameRes.Formats.KiriKiri.Xp3Options");
            object options = Activator.CreateInstance(xp3OptionsType);
            xp3OptionsType.GetProperty("Version").SetValue(options, 2, null);
            xp3OptionsType.GetProperty("Scheme").SetValue(options, scheme, null);
            xp3OptionsType.GetProperty("CompressIndex").SetValue(options, true, null);
            xp3OptionsType.GetProperty("CompressContents").SetValue(options, false, null);
            xp3OptionsType.GetProperty("RetainDirs").SetValue(options, true, null);

            // Call opener.Create(outputStream, entries, options, callback)
            var createMethod = xp3Opener.GetType().GetMethod("Create", new[] { typeof(Stream), typeof(IEnumerable<>).MakeGenericType(entryType), gameRes.GetType("GameRes.ResourceOptions"), gameRes.GetType("GameRes.EntryCallback") });
            
            Console.WriteLine("Creating output file: " + outputFile);
            using (var outputStream = File.Create(outputFile))
            {
                createMethod.Invoke(xp3Opener, new object[] { outputStream, entryArray, options, null });
            }
            Console.WriteLine("XP3 archive created successfully!");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex);
        }
    }
}
