import os
import sys
import subprocess
import argparse
import glob

# Add current folder to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from make_patch3_maitetsu import pack_maitetsu_xp3

# Paths to tools
GAME_DIR = r"E:\まいてつ Last Run!!"
TOOLS_DIR = os.path.join(GAME_DIR, "tools")
KREXTRACT_DIR = os.path.join(GAME_DIR, "KrkrExtract_Output")
SCN_TRANSLATION_DIR = os.path.join(GAME_DIR, "scn_translation")
VN_PATCH_DIR = os.path.join(GAME_DIR, "vn_patch")

INSERTER = r"D:\Games\tools\scn-tool-main\target\release\scn-script-inserter.exe"
EXTRACTOR = r"D:\Games\tools\scn-tool-main\target\release\scn-script-extractor.exe"

# Priority of folders to search for latest original SCN files
SEARCH_PRIORITY = [
    "patch2",
    "patch",
    "patch_data2",
]
# Add patch_append92 down to patch_append72 dynamically
for i in range(92, 71, -1):
    SEARCH_PRIORITY.append(f"patch_append{i}")
SEARCH_PRIORITY.extend(["data", "data2", "data3"])

def find_original_scn(scenario_name):
    """Find the latest original SCN file in KrkrExtract_Output based on priority."""
    # Strip any extension if provided
    base_name = scenario_name.replace(".txt", "").replace(".scn", "")
    target_names = [f"{base_name}.txt.scn", f"{base_name}.scn"]

    for folder in SEARCH_PRIORITY:
        folder_path = os.path.join(KREXTRACT_DIR, folder)
        if not os.path.exists(folder_path):
            continue
            
        for name in target_names:
            full_path = os.path.join(folder_path, name)
            if os.path.exists(full_path):
                print(f"[OK] Found original SCN in priority folder '{folder}': {full_path}")
                return full_path

    # Fallback search if not found in prioritized list
    for name in target_names:
        fallback_pattern = os.path.join(KREXTRACT_DIR, "**", name)
        matches = glob.glob(fallback_pattern, recursive=True)
        if matches:
            print(f"[OK] Found original SCN (fallback search): {matches[0]}")
            return matches[0]

    return None

def extract_scenario(scenario_name):
    """Extract text from the latest SCN into TOML for translation."""
    base_name = scenario_name.replace(".txt", "").replace(".scn", "")
    original_scn = find_original_scn(base_name)
    if not original_scn:
        print(f"[ERROR] Could not find original SCN file for '{base_name}' in KrkrExtract_Output!")
        return False

    os.makedirs(SCN_TRANSLATION_DIR, exist_ok=True)
    toml_path = os.path.join(SCN_TRANSLATION_DIR, f"{base_name}.toml")

    print(f"Extracting kịch bản to TOML: {toml_path}")
    # Run scn-script-extractor.exe --slot 0 <scn> <toml>
    cmd = [EXTRACTOR, "--slot", "0", original_scn, toml_path]
    print(f"Running: {' '.join(cmd)}")
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Extractor failed with code {res.returncode}")
        if res.stdout: print("Stdout:", res.stdout)
        if res.stderr: print("Stderr:", res.stderr)
        return False

    print(f"[OK] Successfully extracted kịch bản to {toml_path}")
    return True

def translate_scenario(scenario_name):
    """Insert translation from TOML into raw SCN and save to vn_patch."""
    base_name = scenario_name.replace(".txt", "").replace(".scn", "")
    original_scn = find_original_scn(base_name)
    if not original_scn:
        print(f"[ERROR] Could not find original SCN file for '{base_name}'!")
        return False

    # Check for TOML
    toml_path = os.path.join(SCN_TRANSLATION_DIR, f"{base_name}.toml")
    if not os.path.exists(toml_path):
        print(f"[ERROR] Translation TOML not found at: {toml_path}")
        return False

    # Setup vn_patch outputs
    os.makedirs(os.path.join(VN_PATCH_DIR, "scn"), exist_ok=True)
    
    # Save SCN to both root and scn/ directories to ensure engine loads it correctly
    out_scn_root = os.path.join(VN_PATCH_DIR, f"{base_name}.txt.scn")
    out_scn_subdir = os.path.join(VN_PATCH_DIR, "scn", f"{base_name}.txt.scn")

    print(f"Translating scenario '{base_name}' using TOML...")
    cmd = [INSERTER, toml_path, original_scn, out_scn_root]
    print(f"Running: {' '.join(cmd)}")
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[ERROR] Inserter failed with code {res.returncode}")
        if res.stdout: print("Stdout:", res.stdout)
        if res.stderr: print("Stderr:", res.stderr)
        return False

    # Copy to scn/ subdirectory too
    import shutil
    shutil.copy2(out_scn_root, out_scn_subdir)

    print(f"[OK] Compiled Vietnamese SCN:")
    print(f"  -> {out_scn_root}")
    print(f"  -> {out_scn_subdir}")
    return True

def pack_patch():
    """Pack vn_patch directory into patch3.xp3."""
    out_xp3 = os.path.join(GAME_DIR, "patch3.xp3")
    pack_maitetsu_xp3(VN_PATCH_DIR, out_xp3)

def main():
    parser = argparse.ArgumentParser(description="Maitetsu - Last Run!! Translation Pipeline")
    parser.add_argument("scenario", nargs="?", help="Name of the scenario file (e.g. れいな01_炭鉱探索)")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract text from SCN into TOML for editing")
    parser.add_argument("-t", "--translate", action="store_true", help="Insert TOML translations into SCN")
    parser.add_argument("-p", "--pack", action="store_true", help="Pack all translated files in vn_patch/ into patch3.xp3")
    
    args = parser.parse_args()

    if not args.scenario and not args.pack:
        parser.print_help()
        sys.exit(1)

    success = True
    if args.scenario:
        if args.extract:
            success = extract_scenario(args.scenario)
        elif args.translate:
            success = translate_scenario(args.scenario)
        else:
            # Default action is to translate (insert TOML -> SCN)
            success = translate_scenario(args.scenario)

    if success and args.pack:
        pack_patch()

if __name__ == "__main__":
    main()
