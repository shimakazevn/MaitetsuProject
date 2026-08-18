
using System;
using System.Reflection;
using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Text;

class Program
{
    static void Main()
    {
        try
        {
            // Load Assemblies
            var gameRes = Assembly.LoadFrom("GameRes.dll");
            var arcFormats = Assembly.LoadFrom("ArcFormats.dll");

            // Print fields of CxProgram
            var cxProgramType = gameRes.GetType("GameRes.Formats.KiriKiri.CxProgram") ?? arcFormats.GetType("GameRes.Formats.KiriKiri.CxProgram");
            if (cxProgramType != null)
            {
                Console.WriteLine("=== CxProgram Fields ===");
                foreach (var f in cxProgramType.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance))
                {
                    Console.WriteLine($"  {f.FieldType.Name} {f.Name}");
                }
            }

            // Load scheme catalog from GameData/Formats.dat
            string datPath = Path.Combine("GameData", "Formats.dat");
            if (!File.Exists(datPath))
            {
                datPath = "Formats.dat";
            }

            using (Stream stream = File.OpenRead(datPath))
            {
                GameRes.FormatCatalog.Instance.DeserializeScheme(stream);
            }

            // Get XP3 opener
            var format = GameRes.FormatCatalog.Instance.ArcFormats
                .FirstOrDefault(a => a.GetType().Name == "Xp3Opener");

            if (format != null)
            {
                var schemeProperty = format.GetType().GetProperty("Scheme");
                var scheme = schemeProperty.GetValue(format);
                if (scheme != null)
                {
                    var knownSchemesField = scheme.GetType().GetField("KnownSchemes", BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance);
                    var knownSchemes = knownSchemesField.GetValue(scheme) as System.Collections.IDictionary;
                    if (knownSchemes != null)
                    {
                        foreach (System.Collections.DictionaryEntry entry in knownSchemes)
                        {
                            string key = entry.Key.ToString();
                            if (key == "Maitetsu - Last Run!!")
                            {
                                Console.WriteLine($"=== Found: {key} ===");
                                var val = entry.Value;
                                SerializeSchemeToJson(val, "maitetsu_scheme.json");
                                Console.WriteLine("Serialized scheme parameters to maitetsu_scheme.json");
                            }
                        }
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex);
        }
    }

    static void SerializeSchemeToJson(object obj, string filename)
    {
        var type = obj.GetType();
        var data = new Dictionary<string, object>();

        foreach (var f in type.GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance))
        {
            var val = f.GetValue(obj);
            if (val is uint[] uints)
            {
                data[f.Name] = uints;
            }
            else if (val is byte[] bytes)
            {
                data[f.Name] = bytes;
            }
            else if (f.Name == "m_program_list" && val is Array arr)
            {
                var progList = new List<Dictionary<string, object>>();
                for (int i = 0; i < arr.Length; i++)
                {
                    var elem = arr.GetValue(i);
                    if (elem != null)
                    {
                        var elemDict = new Dictionary<string, object>();
                        foreach (var ef in elem.GetType().GetFields(BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Instance))
                        {
                            var eval = ef.GetValue(elem);
                            if (eval is byte[] ebytes)
                            {
                                elemDict[ef.Name] = Convert.ToBase64String(ebytes);
                            }
                            else if (eval is uint[] euints)
                            {
                                elemDict[ef.Name] = euints;
                            }
                            else
                            {
                                elemDict[ef.Name] = eval;
                            }
                        }
                        progList.Add(elemDict);
                    }
                }
                data[f.Name] = progList;
            }
            else if (val is string || val is int || val is uint || val is bool)
            {
                data[f.Name] = val;
            }
        }

        // Quick JSON serialization
        var json = SimpleJsonSerialize(data);
        File.WriteAllText(filename, json);
    }

    static string SimpleJsonSerialize(object obj, int indentLevel = 0)
    {
        string indent = new string(' ', indentLevel * 2);
        if (obj == null) return "null";
        if (obj is string s) return "\"" + EscapeString(s) + "\"";
        if (obj is bool b) return b ? "true" : "false";
        if (obj is int || obj is uint || obj is long || obj is byte) return obj.ToString();
        if (obj is uint[] uints)
        {
            return "[" + string.Join(", ", uints) + "]";
        }
        if (obj is byte[] bytes)
        {
            return "[" + string.Join(", ", bytes) + "]";
        }
        if (obj is IDictionary<string, object> dict)
        {
            var parts = new List<string>();
            foreach (var kvp in dict)
            {
                parts.Add($"\n{indent}  \"{kvp.Key}\": {SimpleJsonSerialize(kvp.Value, indentLevel + 1)}");
            }
            return "{" + string.Join(",", parts) + $"\n{indent}}}";
        }
        if (obj is System.Collections.IList list)
        {
            var parts = new List<string>();
            foreach (var item in list)
            {
                parts.Add(SimpleJsonSerialize(item, indentLevel + 1));
            }
            return "[\n" + string.Join(",\n", parts.Select(x => indent + "  " + x)) + $"\n{indent}]";
        }
        return "\"" + obj.ToString() + "\"";
    }

    static string EscapeString(string s)
    {
        return s.Replace("\\", "\\\\").Replace("\"", "\\\"").Replace("\n", "\\n").Replace("\r", "\\r");
    }
}




