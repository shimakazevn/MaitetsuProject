#!/usr/bin/env python3
r"""
Maitetsu Last Run!! - SCN Translation Pipeline
================================================
Complete toolchain for translating SCN scenario files using the Rust scn-tool.

Workflow:
  1. TOML files (extracted with --slot 2 = TW slot) live in:
       E:\MaitetsuProject\translation_toml\<subfolder>\<name>.txt.toml
  2. Edit TOML values to replace Traditional Chinese with Vietnamese.
  3. Run this script to compile edited TOMLs back into .scn files,
     copy them to vn_patch/, rebuild patch3.xp3, and optionally restart the game.

Usage:
  python build_patch.py                    # Build ALL translated files
  python build_patch.py <toml_file>        # Build a single file
  python build_patch.py --restart          # Build all + restart game
  python build_patch.py <toml_file> --restart  # Build one + restart game
"""

import os
import sys
import shutil
import subprocess
import glob
import time

# ── Paths ──────────────────────────────────────────────────────────────
GAME_DIR       = r"E:\まいてつ Last Run!!"
PROJECT_DIR    = r"E:\MaitetsuProject"
TOML_DIR       = os.path.join(PROJECT_DIR, "translation_toml")
OLD_SCN_DIR    = os.path.join(PROJECT_DIR, "original_scn")
NEW_SCN_DIR    = os.path.join(PROJECT_DIR, "compiled_scn")
VN_PATCH_DIR   = os.path.join(GAME_DIR, "vn_patch")

EXTRACTOR_EXE  = os.path.join(PROJECT_DIR, "scn-script-extractor.exe")
INSERTER_EXE   = os.path.join(PROJECT_DIR, "scn-script-inserter.exe")

GAME_EXE       = os.path.join(GAME_DIR, "まいてつ Last Run!!.exe")
PATCH_FILE     = os.path.join(GAME_DIR, "patch3.xp3")

# ── Helpers ────────────────────────────────────────────────────────────

def find_all_tomls():
    """Find all .toml files recursively under TOML_DIR."""
    tomls = []
    for root, dirs, files in os.walk(TOML_DIR):
        for f in sorted(files):
            if f.endswith(".toml"):
                tomls.append(os.path.join(root, f))
    return tomls


def toml_to_scn_name(toml_path):
    """Convert TOML filename back to SCN filename.
    Example: 共通01_右田双鉄の帰還.txt.toml -> 共通01_右田双鉄の帰還.txt.scn
    """
    basename = os.path.basename(toml_path)
    if basename.endswith(".txt.toml"):
        return basename[:-5] + ".scn"   # .txt.toml -> .txt.scn
    elif basename.endswith(".toml"):
        return basename[:-5] + ".scn"   # .toml -> .scn
    return basename


def compile_toml(toml_path, old_scn_dir=OLD_SCN_DIR, new_scn_dir=NEW_SCN_DIR):
    """Compile a single TOML file into a patched .scn using the Rust inserter."""
    scn_name = toml_to_scn_name(toml_path)
    old_scn = os.path.join(old_scn_dir, scn_name)
    new_scn = os.path.join(new_scn_dir, scn_name)

    if not os.path.exists(old_scn):
        print(f"  [SKIP] Original SCN not found: {old_scn}")
        return None

    os.makedirs(new_scn_dir, exist_ok=True)

    result = subprocess.run(
        [INSERTER_EXE, toml_path, old_scn, new_scn],
        capture_output=True, text=True
    )

    if result.returncode != 0:
        print(f"  [ERROR] Failed to compile {os.path.basename(toml_path)}")
        if result.stderr:
            print(f"    {result.stderr.strip()}")
        return None

    return new_scn


def copy_to_vn_patch(scn_path):
    """Copy compiled .scn to vn_patch directory."""
    # Copy to root
    dest = os.path.join(VN_PATCH_DIR, os.path.basename(scn_path))
    shutil.copy2(scn_path, dest)
    
    # Copy to scn/ subdirectory to ensure the engine loads it correctly
    scn_subdir = os.path.join(VN_PATCH_DIR, "scn")
    os.makedirs(scn_subdir, exist_ok=True)
    shutil.copy2(scn_path, os.path.join(scn_subdir, os.path.basename(scn_path)))
    
    return dest


def pack_xp3():
    """Pack vn_patch/ into patch3.xp3."""
    sys.path.insert(0, os.path.join(GAME_DIR, "tools"))
    from make_patch3_maitetsu import pack_maitetsu_xp3  # type: ignore
    pack_maitetsu_xp3(VN_PATCH_DIR, PATCH_FILE)


def stop_game():
    """Stop game if running."""
    subprocess.run(
        ["powershell", "Stop-Process -Name 'まいてつ*' -Force -ErrorAction SilentlyContinue"],
        capture_output=True
    )


def start_game():
    """Start the game."""
    subprocess.Popen(
        [GAME_EXE],
        cwd=GAME_DIR,
        creationflags=subprocess.DETACHED_PROCESS
    )


def count_vietnamese_chars(toml_path):
    import re
    # Vietnamese diacritic characters regex
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


# ── Main ───────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    restart = "--restart" in args
    args = [a for a in args if a != "--restart"]

    # Determine which TOML(s) to compile
    if args:
        # Single file or glob
        target = args[0]
        if os.path.isfile(target):
            tomls = [target]
        else:
            # Try to find by name in TOML_DIR
            matches = []
            for root, dirs, files in os.walk(TOML_DIR):
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

    # Deduplicate files that compile to the same target SCN name
    original_count = len(tomls)
    tomls = deduplicate_tomls(tomls)
    if len(tomls) < original_count:
        print(f"[INFO] Resolved duplicate TOML targets. Deduplicated from {original_count} to {len(tomls)} files based on Vietnamese translation score.")

    print(f"=== Maitetsu SCN Build Pipeline ===")
    print(f"Files to compile: {len(tomls)}")
    print()

    # Compile in parallel
    import concurrent.futures
    from threading import Lock
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
                dest = copy_to_vn_patch(scn_path)
                print(f"  [{counter}/{len(tomls)}] {rel} [OK]")
                return dest
            else:
                print(f"  [{counter}/{len(tomls)}] {rel} [FAIL]")
                return None

    # Use ThreadPoolExecutor to run inserters in parallel
    max_workers = (os.cpu_count() or 4) * 2
    print(f"Compiling in parallel using {max_workers} workers...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(process_file, tomls))
        compiled = [r for r in results if r is not None]

    print()
    print(f"Compiled: {len(compiled)}/{len(tomls)} files")

    if not compiled:
        print("[WARN] No files were compiled. Skipping patch build.")
        return 0

    # Pack - always stop the game first to release the file lock on patch3.xp3
    print("Packing patch3.xp3...")
    stop_game()
    time.sleep(1)

    pack_xp3()
    print(f"[OK] {PATCH_FILE}")

    # Restart
    if restart:
        print("Starting game...")
        start_game()
        print("[OK] Game launched.")

    print()
    print("=== Done ===")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
