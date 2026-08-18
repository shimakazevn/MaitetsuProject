#!/usr/bin/env python3
r"""
Maitetsu Last Run!! - Vietnamese Patch Build Pipeline
=====================================================
Automated toolchain to compile translated TOML scenarios, merge patch assets,
and package the final patch3.xp3 archive.

Workflow:
  1. Compiles TOML scenarios (translation_toml/) into patched .scn (compiled_scn/).
  2. Merges compiled SCN files with UI/script assets (patch_assets/) into staging_patch/.
  3. Packages patch3.xp3 using Maitetsu CxEncryption (Adler32/XOR) & XP3 V2 format.
  4. Automatically syncs patch3.xp3 to PC Game directory and MuMu Emulator share folder.
  5. (Optional) Restarts the PC game with --restart.

Usage:
  python build_patch.py                    # Build ALL translated files & pack patch3.xp3
  python build_patch.py <toml_file>        # Build a single TOML file & pack patch3.xp3
  python build_patch.py --restart          # Build all, pack, and launch/restart PC game
  python build_patch.py --pack-only        # Skip SCN compilation and pack patch3.xp3 immediately
"""

import os
import sys
import shutil
import subprocess
import concurrent.futures
from threading import Lock
import time

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# ── Project Directories ────────────────────────────────────────────────
PROJECT_DIR      = os.path.dirname(os.path.abspath(__file__))
TOML_DIR         = os.path.join(PROJECT_DIR, "translation_toml")
ORIGINAL_SCN_DIR = os.path.join(PROJECT_DIR, "original_scn")
COMPILED_SCN_DIR = os.path.join(PROJECT_DIR, "compiled_scn")
PATCH_ASSETS_DIR = os.path.join(PROJECT_DIR, "patch_assets")
STAGING_DIR      = os.path.join(PROJECT_DIR, "staging_patch")
TOOLS_DIR        = os.path.join(PROJECT_DIR, "tools")
BIN_DIR          = os.path.join(TOOLS_DIR, "bin")

INSERTER_EXE     = os.path.join(BIN_DIR, "scn-script-inserter.exe")
LOCAL_PATCH_FILE = os.path.join(PROJECT_DIR, "patch3.xp3")

# Target Output / Sync Locations
GAME_DIR         = r"E:\まいてつ Last Run!!"
GAME_PATCH_FILE  = os.path.join(GAME_DIR, "patch3.xp3")
GAME_EXE         = os.path.join(GAME_DIR, "まいてつ Last Run!!.exe")
MUMU_SHARE_DIR   = r"E:\ShareFolderMumu\Download\Maitetsu"
MUMU_PATCH_FILE  = os.path.join(MUMU_SHARE_DIR, "patch3.xp3")

# Add tools to sys.path for XP3 packaging
sys.path.insert(0, TOOLS_DIR)

# ── Helpers ────────────────────────────────────────────────────────────

def find_all_tomls():
    """Find all .toml files recursively under TOML_DIR."""
    tomls = []
    for root, _, files in os.walk(TOML_DIR):
        for f in sorted(files):
            if f.endswith(".toml"):
                tomls.append(os.path.join(root, f))
    return tomls


def toml_to_scn_name(toml_path):
    """Convert TOML filename back to SCN filename."""
    basename = os.path.basename(toml_path)
    if basename.endswith(".txt.toml"):
        return basename[:-5] + ".scn"
    elif basename.endswith(".toml"):
        return basename[:-5] + ".scn"
    return basename


def count_vietnamese_chars(toml_path):
    import re
    vn_chars = re.compile(r'[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', re.IGNORECASE)
    try:
        with open(toml_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        return len(vn_chars.findall(content))
    except Exception:
        return 0


def deduplicate_tomls(toml_paths):
    groups = {}
    for p in toml_paths:
        scn_name = toml_to_scn_name(p)
        groups.setdefault(scn_name, []).append(p)
        
    deduplicated = []
    for scn_name, paths in groups.items():
        if len(paths) == 1:
            deduplicated.append(paths[0])
        else:
            best_path = max(paths, key=count_vietnamese_chars)
            deduplicated.append(best_path)
    return deduplicated


def compile_toml(toml_path):
    """Compile a single TOML file into a patched .scn using the Rust inserter."""
    scn_name = toml_to_scn_name(toml_path)
    old_scn = os.path.join(ORIGINAL_SCN_DIR, scn_name)
    new_scn = os.path.join(COMPILED_SCN_DIR, scn_name)

    if not os.path.exists(old_scn):
        print(f"  [SKIP] Original SCN not found: {old_scn}")
        return None

    os.makedirs(COMPILED_SCN_DIR, exist_ok=True)

    result = subprocess.run(
        [INSERTER_EXE, toml_path, old_scn, new_scn],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )

    if result.returncode != 0:
        print(f"  [ERROR] Failed to compile {os.path.basename(toml_path)}")
        if result.stderr:
            print(f"    {result.stderr.strip()}")
        return None

    return new_scn


def assemble_patch_staging(staging_dir):
    """Combine patch_assets/ and compiled_scn/ into the staging directory."""
    print(f"Assembling patch assets into staging directory: {staging_dir}")
    if os.path.exists(staging_dir):
        shutil.rmtree(staging_dir)
    os.makedirs(staging_dir, exist_ok=True)

    # 1. Copy static assets (UI, scripts, tips, fonts)
    if os.path.exists(PATCH_ASSETS_DIR):
        for root, dirs, files in os.walk(PATCH_ASSETS_DIR):
            rel = os.path.relpath(root, PATCH_ASSETS_DIR)
            dest_root = staging_dir if rel == "." else os.path.join(staging_dir, rel)
            os.makedirs(dest_root, exist_ok=True)
            for f in files:
                shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))

    # 2. Copy compiled scenario SCN files into staging root
    if os.path.exists(COMPILED_SCN_DIR):
        for f in os.listdir(COMPILED_SCN_DIR):
            if f.endswith(".scn"):
                shutil.copy2(os.path.join(COMPILED_SCN_DIR, f), os.path.join(staging_dir, f))


def pack_xp3(staging_dir, output_xp3):
    """Pack staging directory into patch3.xp3 using make_patch3_maitetsu."""
    from make_patch3_maitetsu import pack_maitetsu_xp3  # type: ignore
    pack_maitetsu_xp3(staging_dir, output_xp3)


def stop_game():
    """Stop game process if currently running."""
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", "Get-Process | Where-Object { $_.Path -like '*まいてつ*' -or $_.Name -like '*まいてつ*' } | Stop-Process -Force -ErrorAction SilentlyContinue"],
        capture_output=True
    )
    time.sleep(0.5)


def start_game():
    """Start PC game."""
    if os.path.exists(GAME_EXE):
        subprocess.Popen(
            [GAME_EXE],
            cwd=GAME_DIR,
            creationflags=subprocess.DETACHED_PROCESS
        )
    else:
        print(f"[WARN] Game executable not found at: {GAME_EXE}")


# ── Main Pipeline ──────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    restart = "--restart" in args
    pack_only = "--pack-only" in args
    args = [a for a in args if a not in ("--restart", "--pack-only")]

    print("=" * 65)
    print("      Maitetsu Last Run!! - Vietnamese Patch Build Pipeline")
    print("=" * 65)

    if not pack_only:
        # Determine which TOML(s) to compile
        if args:
            target = args[0]
            if os.path.isfile(target):
                tomls = [target]
            else:
                matches = []
                for root, _, files in os.walk(TOML_DIR):
                    for f in files:
                        if target in f and f.endswith(".toml"):
                            matches.append(os.path.join(root, f))
                if matches:
                    tomls = matches
                else:
                    print(f"[ERROR] No TOML files found matching: {target}")
                    return 1
        else:
            tomls = find_all_tomls()

        tomls = deduplicate_tomls(tomls)
        print(f"[1/4] Compiling {len(tomls)} scenario TOML files...")

        print_lock = Lock()
        counter = 0
        compiled = []

        def process_file(toml_path):
            nonlocal counter
            scn_path = compile_toml(toml_path)
            rel = os.path.relpath(toml_path, TOML_DIR)
            with print_lock:
                counter += 1
                if scn_path:
                    print(f"  [{counter:3d}/{len(tomls)}] {rel} [OK]")
                    return scn_path
                else:
                    print(f"  [{counter:3d}/{len(tomls)}] {rel} [FAIL]")
                    return None

        max_workers = (os.cpu_count() or 4) * 2
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(process_file, tomls))
            compiled = [r for r in results if r is not None]

        print(f"\n[OK] Successfully compiled {len(compiled)}/{len(tomls)} scenario files.\n")
    else:
        print("[INFO] --pack-only mode enabled. Skipping SCN compilation.\n")

    # Assemble staging directory (isolated inside MaitetsuProject)
    print("[2/4] Assembling patch assets & SCN files...")
    assemble_patch_staging(STAGING_DIR)

    # Stop game to release file locks before packing
    print("\n[3/4] Packaging patch3.xp3...")
    stop_game()

    pack_xp3(STAGING_DIR, LOCAL_PATCH_FILE)
    print(f"[OK] Packed patch archive: {LOCAL_PATCH_FILE} ({os.path.getsize(LOCAL_PATCH_FILE)/(1024*1024):.2f} MB)")

    # Sync to other targets
    print("\n[4/4] Synchronizing patch3.xp3 to target environments...")
    if os.path.exists(GAME_DIR):
        try:
            stop_game()
            shutil.copy2(LOCAL_PATCH_FILE, GAME_PATCH_FILE)
            print(f"  -> Synced to PC Game: {GAME_PATCH_FILE}")
        except Exception as e:
            print(f"  -> [WARN] Could not sync to PC game folder: {e}")

    if os.path.exists(MUMU_SHARE_DIR):
        try:
            shutil.copy2(LOCAL_PATCH_FILE, MUMU_PATCH_FILE)
            print(f"  -> Synced to MuMu Emulator: {MUMU_PATCH_FILE}")
        except Exception as e:
            print(f"  -> [WARN] Could not sync to MuMu: {e}")

    # Launch game if requested
    if restart:
        print("\nLaunching game...")
        start_game()
        print("[OK] Game launched.")

    print("\n" + "=" * 65)
    print("                      BUILD COMPLETE!")
    print("=" * 65)
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
