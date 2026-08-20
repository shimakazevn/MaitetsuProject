#!/usr/bin/env python3
"""
Maitetsu Steam Version - Vietnamese Patch Build Script
Pack clean assets + translated SCN files specifically for the Steam release into patch3.xp3 (for KrkrPatch / version.dll).
"""

import os
import sys
import shutil
import subprocess
import argparse

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
PATCH_ASSETS_DIR = os.path.join(CURRENT_DIR, "patch_assets")
COMPILED_SCN_DIR = os.path.join(PROJECT_ROOT, "compiled_scn")
STAGING_DIR = os.path.join(CURRENT_DIR, "unencrypted")
OUTPUT_XP3 = os.path.join(CURRENT_DIR, "unencrypted.xp3")
XP3PACK_EXE = os.path.join(PROJECT_ROOT, "tools", "legacy_tools", "Xp3Pack.exe")

# Default Steam Game Directory
DEFAULT_STEAM_DIR = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun"

# Ensure tools are importable
sys.path.insert(0, os.path.join(PROJECT_ROOT, "tools"))
from pack_steam_plain_xp3 import pack_steam_plain_xp3

def assemble_staging():
    print(f"[*] Assembling Steam patch assets into {STAGING_DIR}...")
    if os.path.exists(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)
    os.makedirs(STAGING_DIR, exist_ok=True)
    
    # 1. Copy patch assets (include clean custom.tjs & Config.tjs with VN font/text hooks)
    count_assets = 0
    skip_files = set()
    for f in os.listdir(PATCH_ASSETS_DIR):
        if f in skip_files:
            continue
        src = os.path.join(PATCH_ASSETS_DIR, f)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(STAGING_DIR, f))
            count_assets += 1
            
    # 2. Copy compiled SCN
    count_scn = 0
    if os.path.exists(COMPILED_SCN_DIR):
        for f in os.listdir(COMPILED_SCN_DIR):
            if f.endswith(".scn"):
                shutil.copy2(os.path.join(COMPILED_SCN_DIR, f), os.path.join(STAGING_DIR, f))
                count_scn += 1
                
    print(f"    -> Staged {count_assets} assets + {count_scn} SCN files (Total: {count_assets + count_scn} files)")

def pack_xp3():
    if os.path.exists(XP3PACK_EXE):
        print(f"[*] Packaging compressed unencrypted.xp3 via Xp3Pack.exe...")
        res = subprocess.run([XP3PACK_EXE, STAGING_DIR], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"    [WARN] Xp3Pack.exe failed, falling back to python packer...")
            pack_steam_plain_xp3(STAGING_DIR, OUTPUT_XP3)
    else:
        print(f"[*] Packaging unencrypted XP3 archive via pack_steam_plain_xp3...")
        pack_steam_plain_xp3(STAGING_DIR, OUTPUT_XP3)

def build_steam_patch(target_dir=DEFAULT_STEAM_DIR, patch_name="patch3.xp3"):
    assemble_staging()
    pack_xp3()
    
    if os.path.exists(OUTPUT_XP3):
        sz = os.path.getsize(OUTPUT_XP3) / (1024 * 1024)
        print(f"[OK] Steam patch created: {OUTPUT_XP3} ({sz:.2f} MB)")
        
        if target_dir and os.path.exists(target_dir):
            dst = os.path.join(target_dir, patch_name)
            try:
                shutil.copy2(OUTPUT_XP3, dst)
                print(f"[OK] Synced to Steam game folder: {dst}")
            except PermissionError:
                print(f"[WARN] Could not copy to {dst} (Game is currently running). Close the game and re-run, or copy manually.")
            except Exception as e:
                print(f"[WARN] Could not copy to {dst}: {e}")
            
    # Cleanup staging folder if left behind
    if os.path.exists(STAGING_DIR):
        shutil.rmtree(STAGING_DIR)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Steam Vietnamese Patch (unencrypted.xp3) for Maitetsu")
    parser.add_argument("--target", type=str, default=DEFAULT_STEAM_DIR, help="Steam game directory to copy patch to")
    parser.add_argument("--name", type=str, default="unencrypted.xp3", help="Target patch file name (default: unencrypted.xp3)")
    args = parser.parse_args()
    
    build_steam_patch(args.target, args.name)
