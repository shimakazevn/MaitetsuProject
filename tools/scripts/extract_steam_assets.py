#!/usr/bin/env python3
"""
Maitetsu Steam Version - Universal Native Asset Extractor
Extracts and automatically decrypts all files from Steam XP3 archives directly to:
E:\MaitetsuProject\steam_version_patch_vn\extracted_assets\
"""

import os
import sys
import zlib
import mmap
import time

PROJECT_ROOT = r"E:\MaitetsuProject"
STEAM_DIR = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun"
EXTRACT_DEST = os.path.join(PROJECT_ROOT, "steam_version_patch_vn", "extracted_assets")
TOOLS_DIR = os.path.join(PROJECT_ROOT, "tools")
LEGACY_TOOLS_DIR = os.path.join(TOOLS_DIR, "legacy_tools")

sys.path.append(LEGACY_TOOLS_DIR)
sys.path.append(os.path.join(LEGACY_TOOLS_DIR, "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))
from krkr_xp3 import parse_xp3, TVP_XP3_SEGM_ENCODE_METHOD_MASK, TVP_XP3_SEGM_ENCODE_ZLIB, decrypt_text

TARGET_ARCHIVES = [
    "others.xp3",
    "patch_append72.xp3",
    "patch_append82.xp3",
    "patch_append83.xp3",
    "patch_append84.xp3",
    "patch_append85.xp3",
    "patch_append86.xp3",
    "patch_append87.xp3",
    "patch_append88.xp3",
    "patch_append89.xp3",
    "patch_append91.xp3",
    "patch_append92.xp3",
    "data.xp3",
    "data3.xp3",
    "data4.xp3",
    "emote.xp3",
    "emotedx.xp3",
    "thum.xp3",
    "bgimage.xp3",
]

def decrypt_steam_data(entry_data, filename):
    if len(entry_data) < 5:
        return entry_data
        
    # 1. Check Kirikiri text files (TJS, KS, CSV, INI, TXT, SCN)
    key = entry_data[0] ^ 0xFE
    if (entry_data[1] ^ key == 0xFE) and (entry_data[3] ^ key == 0xFF) and (entry_data[4] ^ key == 0xFE):
        unxored = bytearray(b ^ key for b in entry_data)
        mode = unxored[2]
        return bytes(decrypt_text(unxored[5:], mode))
        
    # 2. Check PNG
    if (entry_data[0] ^ entry_data[1] == 0x89 ^ 0x50):
        key = entry_data[0] ^ 0x89
        return bytes(b ^ key for b in entry_data)
        
    # 3. Check JPG
    if (entry_data[0] ^ entry_data[1] == 0xFF ^ 0xD8):
        key = entry_data[0] ^ 0xFF
        return bytes(b ^ key for b in entry_data)
        
    # 4. Check TLG
    if (entry_data[0] ^ entry_data[1] == ord('T') ^ ord('L')):
        key = entry_data[0] ^ ord('T')
        return bytes(b ^ key for b in entry_data)
        
    # 5. Check PSB
    if (entry_data[0] ^ entry_data[1] == ord('P') ^ ord('S')):
        key = entry_data[0] ^ ord('P')
        return bytes(b ^ key for b in entry_data)
        
    # 6. Check OGG
    if (entry_data[0] ^ entry_data[1] == ord('O') ^ ord('g')):
        key = entry_data[0] ^ ord('O')
        return bytes(b ^ key for b in entry_data)
        
    return entry_data

def extract_archive(arc_name):
    arc_path = os.path.join(STEAM_DIR, arc_name)
    if not os.path.exists(arc_path):
        print(f"[SKIP] Archive not found: {arc_name}")
        return 0
        
    arc_dest = os.path.join(EXTRACT_DEST, arc_name.replace(".xp3", ""))
    os.makedirs(arc_dest, exist_ok=True)
    
    extracted = 0
    with open(arc_path, "rb") as fp:
        with mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ) as data:
            entries = parse_xp3(data, show_log=False)
            valid_entries = [e for e in entries if not e.name.startswith("$")]
            print(f"[*] Extracting {arc_name} ({len(valid_entries)} files) -> {arc_dest}...")
            
            for e in valid_entries:
                entry_data = bytearray()
                for segm in e.segms:
                    segdata = data[segm.offset : segm.offset + segm.zsize]
                    if (segm.flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) == TVP_XP3_SEGM_ENCODE_ZLIB:
                        segdata = zlib.decompress(segdata)
                    entry_data.extend(segdata)
                    
                dec_data = decrypt_steam_data(entry_data, e.name)
                
                clean_name = e.name.replace("/", os.sep).strip(os.sep)
                out_path = os.path.join(arc_dest, clean_name)
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                
                with open(out_path, "wb") as out_fp:
                    out_fp.write(dec_data)
                extracted += 1
                
    print(f"    -> [OK] Successfully extracted {extracted} clean files from {arc_name}")
    return extracted

def main():
    print("=" * 65)
    print("  Maitetsu Steam Version - Native Asset Extractor")
    print("=" * 65)
    print(f"Source: {STEAM_DIR}")
    print(f"Destination: {EXTRACT_DEST}\n")
    
    start_time = time.time()
    total_files = 0
    
    for arc in TARGET_ARCHIVES:
        total_files += extract_archive(arc)
        
    elapsed = time.time() - start_time
    print("\n" + "=" * 65)
    print(f"EXTRACTION COMPLETE: {total_files} files extracted in {elapsed:.1f}s")
    print(f"All clean assets ready at: {EXTRACT_DEST}")
    print("=" * 65)

if __name__ == "__main__":
    main()
