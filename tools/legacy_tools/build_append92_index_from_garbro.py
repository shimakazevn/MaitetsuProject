import subprocess
import os
import re
import struct

def build_index_from_garbro():
    exe = r"D:\Games\tools\Translator++\www\addons\aec\bin\GARbro-cli\GARbro.Console.exe"
    archive = r"E:\まいてつ Last Run!!\patch_append92.xp3"
    extracted_dir = r"E:\まいてつ Last Run!!\patch_append92_extracted"
    
    # 1. Run GARbro list
    res = subprocess.run([exe, "l", archive], capture_output=True)
    stdout = res.stdout.decode('cp932', errors='ignore')
    
    # Regex to parse lines: " [00024A29] 346116839  filename"
    # Note: filename can contain spaces, Japanese chars, and backslashes
    pattern = re.compile(r'^\s*\[([0-9a-fA-F]+)\]\s+(\d+)\s+(.+)$')
    
    file_entries = []
    
    for line in stdout.splitlines():
        m = pattern.match(line)
        if m:
            comp_size_hex = m.group(1)
            offset_dec = int(m.group(2))
            rel_path = m.group(3).strip()
            
            # Normalize path slashes to forward slashes for XP3 index
            rel_path_xp3 = rel_path.replace('\\', '/')
            
            comp_size = int(comp_size_hex, 16)
            
            # Find original file size on disk
            # Map backslash path for local disk lookup
            local_rel_path = rel_path.replace('/', '\\')
            local_full_path = os.path.join(extracted_dir, local_rel_path)
            
            # Case insensitive path search if exact match fails
            if not os.path.exists(local_full_path):
                # Search case-insensitively
                found = False
                # Normalize and find
                norm_rel = local_rel_path.lower()
                for root, dirs, files in os.walk(extracted_dir):
                    for f in files:
                        full_f = os.path.join(root, f)
                        rel_f = os.path.relpath(full_f, extracted_dir)
                        if rel_f.lower() == norm_rel:
                            local_full_path = full_f
                            found = True
                            break
                    if found:
                        break
            
            if os.path.exists(local_full_path):
                orig_size = os.path.getsize(local_full_path)
            else:
                # If it's the SCN file, we know its uncompressed size is 1214358
                if rel_path_xp3.endswith('.scn'):
                    orig_size = 1214358
                else:
                    print(f"WARNING: File not found in extracted folder: {local_full_path}, using comp_size")
                    orig_size = comp_size
            
            # Determine compression flag
            if comp_size < orig_size:
                flags = 1 # compressed
            else:
                flags = 0 # uncompressed
                # Ensure they are equal
                comp_size = orig_size
                
            file_entries.append({
                'path': rel_path_xp3,
                'offset': offset_dec,
                'orig_size': orig_size,
                'comp_size': comp_size,
                'flags': flags
            })
            
    print(f"Parsed {len(file_entries)} entries from GARbro list.")
    
    # 2. Build index buffer
    index_buf = bytearray()
    
    for entry in file_entries:
        path_utf16 = entry['path'].encode('utf-16le')
        path_len = len(entry['path'])
        
        # 1. time chunk
        time_payload = struct.pack('<Q', 132570000000000000)
        time_chunk = b'time' + struct.pack('<Q', len(time_payload)) + time_payload
        
        # 2. adlr chunk
        adlr_payload = struct.pack('<I', 0x0d73f131)
        adlr_chunk = b'adlr' + struct.pack('<Q', len(adlr_payload)) + adlr_payload
        
        # 3. segm chunk
        segm_payload = bytearray()
        segm_payload.extend(struct.pack('<I', entry['flags']))
        segm_payload.extend(struct.pack('<Q', entry['offset']))
        segm_payload.extend(struct.pack('<Q', entry['orig_size']))
        segm_payload.extend(struct.pack('<Q', entry['comp_size']))
        segm_chunk = b'segm' + struct.pack('<Q', len(segm_payload)) + segm_payload
        
        # 4. info chunk (flags = 0x80000000)
        info_payload = bytearray()
        info_payload.extend(struct.pack('<I', 0x80000000))
        info_payload.extend(struct.pack('<Q', entry['orig_size']))
        info_payload.extend(struct.pack('<Q', entry['comp_size']))
        info_payload.extend(struct.pack('<H', path_len))
        info_payload.extend(path_utf16)
        info_payload.extend(b'\x00\x00')
        info_chunk = b'info' + struct.pack('<Q', len(info_payload)) + info_payload
        
        file_payload = time_chunk + adlr_chunk + segm_chunk + info_chunk
        file_chunk = b'File' + struct.pack('<Q', len(file_payload)) + file_payload
        index_buf.extend(file_chunk)
        
    index_path = r"E:\まいてつ Last Run!!\patch_append92.xp3.index"
    with open(index_path, 'wb') as f:
        f.write(index_buf)
        
    print(f"Successfully generated {index_path} ({len(index_buf)} bytes)")

if __name__ == '__main__':
    build_index_from_garbro()
