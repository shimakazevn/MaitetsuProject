import os
import sys
import json
import mmap
import glob

# Add path to import from GalgameReverse
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))
from krkr_xp3 import parse_xp3

def main():
    game_dir = r"E:\まいてつ Last Run!!"
    output_json = os.path.join(game_dir, "tools", "original_hashes.json")
    
    hash_map = {}
    
    # We will scan patch2.xp3.bak, patch.xp3, patch_data2.xp3, and any patch_append*.xp3 files
    xp3_files = [
        os.path.join(game_dir, "patch2.xp3.bak"),
        os.path.join(game_dir, "patch.xp3"),
        os.path.join(game_dir, "patch_data2.xp3"),
    ]
    # Add all patch_append*.xp3 files
    xp3_files.extend(glob.glob(os.path.join(game_dir, "patch_append*.xp3")))
    
    # Also scan data.xp3 if it exists in the game dir
    data_xp3 = os.path.join(game_dir, "data.xp3")
    if os.path.exists(data_xp3):
        xp3_files.append(data_xp3)
        
    print(f"Scanning {len(xp3_files)} archives for original file hashes...")
    
    for xp3_path in xp3_files:
        if not os.path.exists(xp3_path):
            continue
            
        print(f"Parsing {os.path.basename(xp3_path)}...")
        try:
            with open(xp3_path, "rb") as fp:
                # Use mmap for speed
                with mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as data:
                    entries = parse_xp3(data, show_log=False)
                    for entry in entries:
                        if entry.name and entry.adlr:
                            name_lower = entry.name.lower().replace("\\", "/")
                            # Keep the first hash we find (highest priority usually in load order, or just keep it)
                            # But actually we can overwrite to get the latest patch hash
                            hash_map[name_lower] = entry.adlr.hash
        except Exception as ex:
            print(f"  Error parsing {os.path.basename(xp3_path)}: {ex}")
            
    print(f"Extracted {len(hash_map)} original file hashes.")
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(hash_map, f, indent=2)
        
    print(f"Saved database to {output_json}")

if __name__ == "__main__":
    main()
