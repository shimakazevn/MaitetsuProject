#!/usr/bin/env python3
"""
Maitetsu Steam Version - Complete Native Decryptor & Extractor
Extracts and perfectly decrypts all files from Steam XP3 archives to:
E:\MaitetsuProject\steam_version_patch_vn\extracted_assets\
"""

import os
import sys
import zlib
import mmap
import time
import struct

PROJECT_ROOT = r"E:\MaitetsuProject"
STEAM_DIR = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun"
EXTRACT_DEST = os.path.join(PROJECT_ROOT, "steam_version_patch_vn", "extracted_assets")
TOOLS_DIR = os.path.join(PROJECT_ROOT, "tools")
LEGACY_TOOLS_DIR = os.path.join(TOOLS_DIR, "legacy_tools")

sys.path.append(TOOLS_DIR)
sys.path.append(LEGACY_TOOLS_DIR)
sys.path.append(os.path.join(LEGACY_TOOLS_DIR, "build_patch2_work", "GalgameReverse", "project", "krkr", "src"))

from maitetsu_crypt import MaitetsuCxEncryption
from krkr_xp3 import parse_xp3, TVP_XP3_SEGM_ENCODE_METHOD_MASK, TVP_XP3_SEGM_ENCODE_ZLIB

cx_dec = MaitetsuCxEncryption(os.path.join(TOOLS_DIR, "maitetsu_scheme.json"))

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

def descramble_mode1(data_bytes):
    out = bytearray()
    for i in range(0, len(data_bytes), 2):
        if i + 1 < len(data_bytes):
            d = struct.unpack_from('<H', data_bytes, i)[0]
            d = ((d & 0xAAAA) >> 1) | ((d & 0x5555) << 1)
            out.extend(struct.pack('<H', d))
    return out

def descramble_mode0(data_bytes):
    out = bytearray()
    for i in range(0, len(data_bytes), 2):
        if i + 1 < len(data_bytes):
            d = struct.unpack_from('<H', data_bytes, i)[0]
            if d > 0x20:
                d = d ^ (((d & 0xFE) << 8) ^ 1)
            out.extend(struct.pack('<H', d))
    return out

def descramble_text(data_bytes):
    if len(data_bytes) < 5:
        return data_bytes
    key = data_bytes[0] ^ 0xFE
    if (data_bytes[1] ^ key == 0xFE) and (data_bytes[3] ^ key == 0xFF) and (data_bytes[4] ^ key == 0xFE):
        unxored = bytearray(b ^ key for b in data_bytes)
        mode = unxored[2]
        if mode == 1:
            return bytes(descramble_mode1(unxored[5:]))
        elif mode == 0:
            return bytes(descramble_mode0(unxored[5:]))
        elif mode == 2:
            return bytes(zlib.decompress(unxored[21:]))
        else:
            return bytes(unxored[5:])
    return None

def smart_decrypt(entry_data, hash_val, name):
    if len(entry_data) < 5:
        return entry_data
        
    # 1. Try Maitetsu CX Decryption
    cx_data = bytearray(entry_data)
    cx_dec.decrypt_buffer(hash_val=hash_val, offset=0, buffer=cx_data, pos=0, count=len(cx_data))
    
    # Check if CX produced valid magic or text
    if cx_data.startswith(b'\x89PNG') or cx_data.startswith(b'\xff\xd8') or cx_data.startswith(b'PSB') or cx_data.startswith(b'TLG') or cx_data.startswith(b'OggS'):
        return bytes(cx_data)
        
    text_dec = descramble_text(cx_data)
    if text_dec is not None:
        return text_dec
        
    # 2. Check if raw data (non-CX) has text scrambling
    text_raw = descramble_text(entry_data)
    if text_raw is not None:
        return text_raw
        
    # 3. Check simple XOR signatures for images
    for key in [0, entry_data[0] ^ 0x89, entry_data[0] ^ 0xFF, entry_data[0] ^ ord('P'), entry_data[0] ^ ord('T')]:
        test_buf = bytes(b ^ key for b in entry_data[:16])
        if test_buf.startswith(b'\x89PNG') or test_buf.startswith(b'\xff\xd8') or test_buf.startswith(b'PSB') or test_buf.startswith(b'TLG') or test_buf.startswith(b'OggS'):
            return bytes(b ^ key for b in entry_data)
            
    return bytes(cx_data)

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
                cur_offset = 0
                for segm in e.segms:
                    segdata = data[segm.offset : segm.offset + segm.zsize]
                    if (segm.flags & TVP_XP3_SEGM_ENCODE_METHOD_MASK) == TVP_XP3_SEGM_ENCODE_ZLIB:
                        segdata = zlib.decompress(segdata)
                    entry_data.extend(segdata)
                    
                dec_data = smart_decrypt(entry_data, e.adlr.hash, e.name)
                
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
