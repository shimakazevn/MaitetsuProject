import sys
import os
import zlib
import mmap
import struct

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from maitetsu_crypt import MaitetsuCxEncryption
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))
from krkr_xp3 import parse_xp3, TVP_XP3_SEGM_ENCODE_METHOD_MASK, TVP_XP3_SEGM_ENCODE_ZLIB

def main():
    xp3_path = r"E:\まいてつ Last Run!!\tools\test_patch3.xp3"
    print(f"Loading {xp3_path}...")
    
    dec = MaitetsuCxEncryption(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reflect_app", "maitetsu_scheme.json"))
    
    with open(xp3_path, "rb") as fp:
        with mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as data:
            entries = parse_xp3(data, show_log=False)
            
            for target_entry in entries:
                if target_entry.name:
                    print(f"Found target entry: {target_entry.name}")
                    print(f"  Unpacked size: {target_entry.info.fsize} bytes")
                    print(f"  Flags: 0x{target_entry.info.flags:X}")
                    print(f"  Hash (adlr): 0x{target_entry.adlr.hash:X}")
                    
                    is_encrypted = (target_entry.info.flags & 0x80000000) != 0
                    print(f"  Is encrypted: {is_encrypted}")
                    
                    for idx, segm in enumerate(target_entry.segms):
                        segdata = data[segm.offset : segm.offset + segm.zsize]
                        
                        if (segm.flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) == TVP_XP3_SEGM_ENCODE_ZLIB:
                            segdata = zlib.decompress(segdata)
                        
                        segdata_mutable = bytearray(segdata)
                        
                        if is_encrypted:
                            dec.decrypt_buffer(
                                hash_val=target_entry.adlr.hash,
                                offset=0,
                                buffer=segdata_mutable,
                                pos=0,
                                count=len(segdata_mutable)
                            )
                        
                        print("\n--- Decrypted Content (Raw Bytes hex) ---")
                        print(segdata_mutable.hex("-"))
                        
                        print("\n--- Decrypted Content (UTF-16LE or ASCII safely) ---")
                        try:
                            text_utf16 = segdata_mutable.decode("utf-16le", errors="replace")
                            safe_text = "".join(c if ord(c) < 128 else "?" for c in text_utf16)
                            print(safe_text)
                        except Exception as ex:
                            print("Error decoding:", ex)

if __name__ == "__main__":
    main()
