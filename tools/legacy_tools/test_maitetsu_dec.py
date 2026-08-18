import sys
import os
import zlib
import mmap
import struct

# Add current folder to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from maitetsu_crypt import MaitetsuCxEncryption
# Also import from the cloned GalgameReverse repo
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))
from krkr_xp3 import parse_xp3, TVP_XP3_SEGM_ENCODE_METHOD_MASK, TVP_XP3_SEGM_ENCODE_ZLIB

def main():
    xp3_path = r"E:\まいてつ Last Run!!\patch_append92.xp3"
    print(f"Loading {xp3_path}...")
    
    # Initialize our decrypter
    dec = MaitetsuCxEncryption()
    
    with open(xp3_path, "rb") as fp:
        with mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as data:
            entries = parse_xp3(data, show_log=False)
            
            # Find a small script file, like append_setup_92.tjs
            target_entry = None
            for e in entries:
                if e.name and e.name.endswith("append_setup_92.tjs"):
                    target_entry = e
                    break
            
            if not target_entry:
                print("Could not find append_setup_92.tjs in the archive!")
                # Let's find any script file
                for e in entries:
                    if e.name and (e.name.endswith(".tjs") or e.name.endswith(".txt")) and not e.name.endswith(".scn"):
                        target_entry = e
                        break
            
            if not target_entry:
                print("No suitable text/tjs entry found!")
                return
                
            print(f"Found target entry: {target_entry.name}")
            print(f"  Unpacked size: {target_entry.info.fsize} bytes")
            print(f"  Flags: 0x{target_entry.info.flags:X}")
            print(f"  Hash (adlr): 0x{target_entry.adlr.hash:X}")
            
            # Check if encrypted (flag 0x80000000)
            is_encrypted = (target_entry.info.flags & 0x80000000) != 0
            print(f"  Is encrypted in archive (index flag): {is_encrypted}")
            
            # Extract segment data
            for idx, segm in enumerate(target_entry.segms):
                print(f"  Segment {idx}: offset=0x{segm.offset:X}, fsize={segm.fsize}, zsize={segm.zsize}")
                segdata = data[segm.offset : segm.offset + segm.zsize]
                
                # If compressed, decompress it
                if (segm.flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) == TVP_XP3_SEGM_ENCODE_ZLIB:
                    print("    Decompressing zlib...")
                    segdata = zlib.decompress(segdata)
                
                # Convert to bytearray so it's mutable for decryption
                segdata_mutable = bytearray(segdata)
                
                # Decrypt if flag is set
                if is_encrypted:
                    print("    Decrypting using MaitetsuCxEncryption...")
                    dec.decrypt_buffer(
                        hash_val=target_entry.adlr.hash,
                        offset=0,
                        buffer=segdata_mutable,
                        pos=0,
                        count=len(segdata_mutable)
                    )
                
                # Check for krkr text encryption (fe fe [type] ff fe)
                final_data = segdata_mutable
                if len(final_data) > 5 and final_data[0] == 0xfe and final_data[1] == 0xfe and final_data[3] == 0xff and final_data[4] == 0xfe:
                    print("    Detected Kirikiri text obfuscation. Decrypting text...")
                    from krkr_xp3 import decrypt_text
                    final_data = decrypt_text(final_data[5:], final_data[2])
                
                # Convert to bytes for decoding/writing
                if isinstance(final_data, memoryview):
                    final_bytes = final_data.tobytes()
                else:
                    final_bytes = bytes(final_data)

                # Save to a file for verification
                out_test_path = "decrypted_test_tjs.txt"
                try:
                    with open(out_test_path, "wb") as test_f:
                        test_f.write(final_bytes)
                    print(f"\nSaved decrypted content to {out_test_path}")
                except Exception as ex:
                    print("Error writing file:", ex)

                # Print first 200 bytes as decoded string safely
                print("\n--- Decrypted Content Preview (Raw Bytes hex) ---")
                print(final_bytes[:64].hex("-"))
                
                print("\n--- Decrypted Content Preview (UTF-16LE) ---")
                try:
                    text_utf16 = final_bytes.decode("utf-16le", errors="replace")
                    # replace the BOM manually to avoid cp932 output error or just print ascii characters
                    safe_text = "".join(c if ord(c) < 128 else "?" for c in text_utf16[:300])
                    print(safe_text)
                except Exception as ex:
                    print("Error printing:", ex)

if __name__ == "__main__":
    main()
