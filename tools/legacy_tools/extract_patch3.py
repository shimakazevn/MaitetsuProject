import sys
import os
import zlib
import mmap

# Add paths to sys.path
tools_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(tools_dir)
sys.path.append(os.path.join(tools_dir, "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))

from maitetsu_crypt import MaitetsuCxEncryption
from krkr_xp3 import parse_xp3, TVP_XP3_SEGM_ENCODE_METHOD_MASK, TVP_XP3_SEGM_ENCODE_ZLIB, decrypt_text

def extract_all():
    game_dir = r"E:\まいてつ Last Run!!"
    xp3_path = os.path.join(game_dir, "patch3.xp3")
    out_dir = os.path.join(game_dir, "vn_patch")
    
    if not os.path.exists(xp3_path):
        print(f"[ERROR] {xp3_path} does not exist!")
        return
        
    print(f"Loading {xp3_path}...")
    dec = MaitetsuCxEncryption()
    
    with open(xp3_path, "rb") as fp:
        with mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as data:
            entries = parse_xp3(data, show_log=False)
            print(f"Found {len(entries)} entries in patch3.xp3")
            
            for entry in entries:
                if not entry.name:
                    continue
                
                name = entry.name
                print(f"Extracting {name}...")
                
                is_encrypted = (entry.info.flags & 0x80000000) != 0
                
                entry_data = bytearray()
                for segm in entry.segms:
                    segdata = data[segm.offset : segm.offset + segm.zsize]
                    if (segm.flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) == TVP_XP3_SEGM_ENCODE_ZLIB:
                        segdata = zlib.decompress(segdata)
                    
                    segdata_mutable = bytearray(segdata)
                    if is_encrypted:
                        dec.decrypt_buffer(
                            hash_val=entry.adlr.hash,
                            offset=0,
                            buffer=segdata_mutable,
                            pos=0,
                            count=len(segdata_mutable)
                        )
                    entry_data.extend(segdata_mutable)
                
                # Check for krkr text encryption
                if len(entry_data) > 5 and entry_data[0] == 0xfe and entry_data[1] == 0xfe and entry_data[3] == 0xff and entry_data[4] == 0xfe:
                    entry_data = decrypt_text(entry_data[5:], entry_data[2])
                
                clean_name = entry.name.replace("/", os.sep).strip(os.sep)
                out_path = os.path.join(out_dir, clean_name)
                
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "wb") as out_f:
                    out_f.write(entry_data)
                print(f"  -> Wrote {out_path}")

if __name__ == "__main__":
    extract_all()
