
using System;
using System.IO;
using System.IO.MemoryMappedFiles;
using System.Reflection;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Diagnostics;
using System.Runtime.InteropServices;
using GameRes;
using GameRes.Formats;
using GameRes.Formats.KiriKiri;
using GameRes.Compression;
using GameRes.Utility;

class Program
{
    static void Main(string[] args)
    {
        try
        {
            string inputFolder = args.Length > 0 ? args[0] : @"E:\まいてつ Last Run!!\patch2_extracted";
            string outputFile = args.Length > 1 ? args[1] : @"E:\まいてつ Last Run!!\patch2.xp3";
            
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

            // Find Maitetsu - Last Run!! scheme from original Xp3Opener
            Type origXp3OpenerType = typeof(GameRes.Formats.KiriKiri.Xp3Opener);
            var knownSchemesProp = origXp3OpenerType.GetProperty("KnownSchemes", BindingFlags.Public | BindingFlags.Static);
            var knownSchemes = (System.Collections.IDictionary)knownSchemesProp.GetValue(null);
            
            object scheme = knownSchemes["Maitetsu - Last Run!!"];
            if (scheme == null)
            {
                throw new Exception("Maitetsu - Last Run!! scheme not found!");
            }
            Console.WriteLine("Found Maitetsu - Last Run!! scheme.");

            // Build list of GameRes.Entry
            var entryList = new List<Entry>();

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
                Entry entry = new Entry();
                entry.Name = relPath;
                
                // Detect type by extension
                string ext = Path.GetExtension(relPath).ToLower();
                string type = "binary";
                if (ext == ".tlg" || ext == ".png" || ext == ".jpg" || ext == ".bmp")
                    type = "image";
                else if (ext == ".ogg" || ext == ".wav")
                    type = "audio";
                else if (ext == ".txt" || ext == ".tjs" || ext == ".scn")
                    type = "script";
                
                entry.Type = type;
                entryList.Add(entry);
            }

            // Set up MyXp3.Xp3Options
            var options = new Xp3Options
            {
                Version = 2,
                Scheme = (ICrypt)scheme,
                CompressIndex = true,
                CompressContents = false,
                RetainDirs = true
            };

            // Instantiate MyXp3Opener
            var opener = new MyXp3Opener();

            // Backup original patch2.xp3 if not already backed up
            string backupFile = @"E:\まいてつ Last Run!!\patch2.xp3.bak";
            if (!File.Exists(backupFile) && File.Exists(outputFile))
            {
                File.Copy(outputFile, backupFile);
                Console.WriteLine("Backed up original patch2.xp3 to patch2.xp3.bak");
            }

            Console.WriteLine("Creating output file: " + outputFile);
            using (var outputStream = File.Create(outputFile))
            {
                opener.Create(outputStream, entryList, options, null);
            }
            Console.WriteLine("patch2.xp3 archive created successfully with custom standalone MyXp3Opener!");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex);
        }
    }
}

public class MyXp3Opener : Xp3Opener
{
    static readonly byte[] s_xp3_header = { 0x58, 0x50, 0x33, 0x0d, 0x0a, 0x20, 0x0a, 0x1a, 0x8b, 0x67, 0x01 };

    public override void Create (Stream output, IEnumerable<Entry> list, ResourceOptions options,
                                 EntryCallback callback)
    {
        var xp3_options = GetOptions<Xp3Options> (options);

        ICrypt scheme = xp3_options.Scheme;
        bool compress_index = xp3_options.CompressIndex;
        bool compress_contents = xp3_options.CompressContents;
        bool retain_dirs = xp3_options.RetainDirs;

        bool use_encryption = !(scheme is NoCrypt);

        using (var writer = new BinaryWriter (output, Encoding.ASCII, true))
        {
            writer.Write (s_xp3_header);
            if (2 == xp3_options.Version || 3 == xp3_options.Version)
            {
                writer.Write ((long)0x17);
                writer.Write ((int)1);
                writer.Write ((byte)0x80);
                writer.Write ((long)0);
            }
            long index_pos_offset = writer.BaseStream.Position;
            writer.BaseStream.Seek (8, SeekOrigin.Current);

            int callback_count = 0;
            var used_names = new HashSet<string>();
            var dir = new List<Xp3Entry>();
            long current_offset = writer.BaseStream.Position;
            foreach (var entry in list)
            {
                if (null != callback)
                    callback (callback_count++, entry, "Adding...");

                string name = entry.Name;
                if (!retain_dirs)
                    name = Path.GetFileName (name);
                else
                    name = name.Replace (@"\", "/");
                if (!used_names.Add (name))
                {
                    continue;
                }

                // CUSTOM IS_ENCRYPTED LOGIC: Exclude SCN files from CxEncryption!
                bool isScn = name.EndsWith(".scn", StringComparison.OrdinalIgnoreCase);

                var xp3entry = new Xp3Entry {
                    Name            = name,
                    Cipher          = scheme,
                    IsEncrypted     = use_encryption && !isScn
                                   && !(scheme.StartupTjsNotEncrypted && VFS.IsPathEqualsToFileName (name, "startup.tjs"))
                };
                bool compress = compress_contents && ShouldCompressFile (entry);
                using (var file = File.Open (name, FileMode.Open, FileAccess.Read, FileShare.Read))
                {
                    if (!xp3entry.IsEncrypted || 0 == file.Length)
                        RawFileCopy (file, xp3entry, output, compress);
                    else
                        EncryptedFileCopy (file, xp3entry, output, compress);
                }

                dir.Add (xp3entry);
            }

            long index_pos = writer.BaseStream.Position;
            writer.BaseStream.Position = index_pos_offset;
            writer.Write (index_pos);
            writer.BaseStream.Position = index_pos;

            using (var header = new BinaryWriter (new MemoryStream (dir.Count*0x58), Encoding.Unicode))
            {
                long dir_pos = 0;
                if (3 == xp3_options.Version)
                {
                    foreach (var entry in dir)
                    {
                        header.Write ((uint)0x6e666e68); // "hnfn"
                        header.Write ((long)(4+2+entry.Name.Length*2));
                        header.Write ((uint)entry.Hash);
                        header.Write ((short)entry.Name.Length);
                        foreach (char c in entry.Name)
                            header.Write (c);
                    }
                    dir_pos = header.BaseStream.Position;
                }
                foreach (var entry in dir)
                {
                    var entry_name = entry.Name;
                    if (3 == xp3_options.Version)
                    {
                        using (var md5 = System.Security.Cryptography.MD5.Create())
                        {
                            var text_bytes = Encoding.Unicode.GetBytes(entry.Name.ToLowerInvariant());
                            var hash = md5.ComputeHash(text_bytes);
                            var sb = new StringBuilder(32);
                            for (int i = 0; i < hash.Length; ++i)
                                sb.AppendFormat("{0:x2}", hash[i]);
                            entry_name = sb.ToString();
                        }
                    }
                    header.BaseStream.Position = dir_pos;
                    header.Write ((uint)0x656c6946); // "File"
                    long header_size_pos = header.BaseStream.Position;
                    header.Write ((long)0);
                    header.Write ((uint)0x6f666e69); // "info"
                    header.Write ((long)(4+8+8+2 + entry_name.Length*2));
                    header.Write ((uint)(entry.IsEncrypted ? 0x80000000 : 0));
                    header.Write ((long)entry.UnpackedSize);
                    header.Write ((long)entry.Size);

                    header.Write ((short)entry_name.Length);
                    foreach (char c in entry_name)
                        header.Write (c);

                    header.Write ((uint)0x6d676573); // "segm"
                    header.Write ((long)0x1c);
                    var segment = entry.Segments.First();
                    header.Write ((int)(segment.IsCompressed ? 1 : 0));
                    header.Write ((long)segment.Offset);
                    header.Write ((long)segment.Size);
                    header.Write ((long)segment.PackedSize);

                    header.Write ((uint)0x726c6461); // "adlr"
                    header.Write ((long)4);
                    header.Write ((uint)entry.Hash);

                    dir_pos = header.BaseStream.Position;
                    long header_size = dir_pos - header_size_pos - 8;
                    header.BaseStream.Position = header_size_pos;
                    header.Write (header_size);
                }

                header.BaseStream.Position = 0;
                writer.Write (compress_index);
                long unpacked_dir_size = header.BaseStream.Length;
                if (compress_index)
                {
                    long packed_dir_size_pos = writer.BaseStream.Position;
                    writer.Write ((long)0);
                    writer.Write (unpacked_dir_size);

                    long dir_start = writer.BaseStream.Position;
                    using (var zstream = new ZLibStream (writer.BaseStream, CompressionMode.Compress, CompressionLevel.Level9, true))
                        header.BaseStream.CopyTo (zstream);

                    long packed_dir_size = writer.BaseStream.Position - dir_start;
                    writer.BaseStream.Position = packed_dir_size_pos;
                    writer.Write (packed_dir_size);
                }
                else
                {
                    writer.Write (unpacked_dir_size);
                    header.BaseStream.CopyTo (writer.BaseStream);
                }
            }
        }
        output.Seek (0, SeekOrigin.End);
    }

    void RawFileCopy (FileStream file, Xp3Entry xp3entry, Stream output, bool compress)
    {
        if (file.Length > uint.MaxValue)
            throw new Exception("File too large");

        uint unpacked_size    = (uint)file.Length;
        xp3entry.UnpackedSize = (uint)unpacked_size;
        xp3entry.Size         = (uint)unpacked_size;
        compress = compress && unpacked_size > 0;
        var segment = new Xp3Segment {
            IsCompressed = compress,
            Offset       = output.Position,
            Size         = unpacked_size,
            PackedSize   = unpacked_size
        };
        if (compress)
        {
            var start = output.Position;
            using (var zstream = new ZLibStream (output, CompressionMode.Compress, true))
            {
                xp3entry.Hash = CheckedCopy (file, zstream);
            }
            segment.PackedSize = (uint)(output.Position - start);
            xp3entry.Size = segment.PackedSize;
        }
        else
        {
            xp3entry.Hash = CheckedCopy (file, output);
        }
        xp3entry.Segments.Add (segment);
    }

    void EncryptedFileCopy (FileStream file, Xp3Entry xp3entry, Stream output, bool compress)
    {
        if (file.Length > int.MaxValue)
            throw new Exception("File too large");

        using (var map = MemoryMappedFile.CreateFromFile (file, null, 0,
                MemoryMappedFileAccess.Read, null, HandleInheritability.None, true))
        {
            uint unpacked_size    = (uint)file.Length;
            xp3entry.UnpackedSize = (uint)unpacked_size;
            xp3entry.Size         = (uint)unpacked_size;
            using (var view = map.CreateViewAccessor (0, unpacked_size, MemoryMappedFileAccess.Read))
            {
                var segment = new Xp3Segment {
                    IsCompressed = compress,
                    Offset       = output.Position,
                    Size         = unpacked_size,
                    PackedSize   = unpacked_size,
                };
                if (compress)
                {
                    output = new ZLibStream (output, CompressionMode.Compress, true);
                }
                unsafe
                {
                    byte[] read_buffer = new byte[81920];
                    byte* ptr = null;
                    view.SafeMemoryMappedViewHandle.AcquirePointer (ref ptr);
                    try
                    {
                        var checksum = new Adler32();
                        bool hash_after_crypt = xp3entry.Cipher.HashAfterCrypt;
                        if (!hash_after_crypt)
                            xp3entry.Hash = checksum.Update (ptr, (int)unpacked_size);
                        int offset = 0;
                        int remaining = (int)unpacked_size;
                        while (remaining > 0)
                        {
                            int amount = Math.Min (remaining, read_buffer.Length);
                            remaining -= amount;
                            Marshal.Copy ((IntPtr)(ptr+offset), read_buffer, 0, amount);
                            xp3entry.Cipher.Encrypt (xp3entry, offset, read_buffer, 0, amount);
                            if (hash_after_crypt)
                                checksum.Update (read_buffer, 0, amount);
                            output.Write (read_buffer, 0, amount);
                            offset += amount;
                        }
                        if (hash_after_crypt)
                            xp3entry.Hash = checksum.Value;
                    }
                    finally
                    {
                        view.SafeMemoryMappedViewHandle.ReleasePointer();
                        if (compress)
                        {
                            var dest = (output as ZLibStream).BaseStream;
                            output.Dispose();
                            segment.PackedSize = (uint)(dest.Position - segment.Offset);
                            xp3entry.Size = segment.PackedSize;
                        }
                        xp3entry.Segments.Add (segment);
                    }
                }
            }
        }
    }

    uint CheckedCopy (Stream src, Stream dst)
    {
        var checksum = new Adler32();
        var read_buffer = new byte[81920];
        for (;;)
        {
            int read = src.Read (read_buffer, 0, read_buffer.Length);
            if (0 == read)
                break;
            checksum.Update (read_buffer, 0, read);
            dst.Write (read_buffer, 0, read);
        }
        return checksum.Value;
    }

    bool ShouldCompressFile (Entry entry)
    {
        if ("image" == entry.Type || "archive" == entry.Type)
            return false;
        if (entry.Name.EndsWith (".ogg", StringComparison.OrdinalIgnoreCase))
            return false;
        return true;
    }
}
