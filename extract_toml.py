import os
import sys
import shutil
import subprocess
from pathlib import Path

GAME_DIR = r"E:\まいてつ Last Run!!"
PROJECT_DIR = r"E:\MaitetsuProject"
EXTRACTED_DIR = os.path.join(GAME_DIR, "KrkrExtract_Output")
ORIGINAL_SCN_DIR = os.path.join(PROJECT_DIR, "original_scn")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "translation_toml")
EXTRACTOR_EXE = os.path.join(PROJECT_DIR, "scn-script-extractor.exe")

def get_priority(folder_name):
    xp3_path = os.path.join(GAME_DIR, folder_name + ".xp3")
    if os.path.exists(xp3_path):
        return os.path.getmtime(xp3_path)
    if folder_name == 'data':
        return 1.0
    return 0.0

def get_prioritized_scns():
    result = {}
    base = Path(EXTRACTED_DIR)
    if not base.exists():
        print(f"Error: Extracted directory {EXTRACTED_DIR} does not exist!")
        return result

    for folder in base.iterdir():
        if not folder.is_dir():
            continue
        prio = get_priority(folder.name)
        if prio <= 0:
            continue
        for root, dirs, files in os.walk(str(folder)):
            for fname in files:
                if not fname.lower().endswith('.scn'):
                    continue
                full_path = os.path.join(root, fname)
                if fname not in result or prio > result[fname]['priority']:
                    result[fname] = {
                        'path': full_path,
                        'priority': prio,
                    }
    return result

def classify_route(filename):
    fn = filename.lower()
    checks = [
        ("00_Common",      ["共通"]),
        ("01_Hachiroku",   ["ハチロク", "86_", "86_"]),
        ("02_Hibiki",      ["日々姫", "スケ"]),
        ("03_Paulette",    ["ポーレット"]),
        ("04_Reina",       ["れいな"]),
        ("05_Mayami",      ["真闇"]),
        ("06_Kisaki",      ["稀咲"]),
        ("07_Nagi_Fukami",  ["ふかみ", "凪"]),
        ("08_Niiroku",     ["ニイロク"]),
        ("09_Grand",       ["グランド"]),
        ("10_Chikuni",     ["仲国"]),
    ]
    for folder, keywords in checks:
        if any(kw in filename for kw in keywords):
            return folder
    return "11_Other"

def main():
    args = sys.argv[1:]
    
    if not os.path.exists(EXTRACTOR_EXE):
        print(f"Error: {EXTRACTOR_EXE} not found!")
        return

    os.makedirs(ORIGINAL_SCN_DIR, exist_ok=True)

    print("Resolving SCN files from game extraction directory...")
    prioritized = get_prioritized_scns()
    if not prioritized:
        print("No SCN files found.")
        return

    scn_names = sorted(prioritized.keys())
    if args:
        pattern = args[0]
        scn_names = [f for f in scn_names if pattern in f]

    if not scn_names:
        print("No SCN files matched pattern.")
        return

    print(f"Processing {len(scn_names)} SCN files...")
    success = 0
    for i, scn_name in enumerate(scn_names, 1):
        info = prioritized[scn_name]
        src_path = info['path']
        
        # 1. Copy SCN to local original_scn/ folder
        local_scn_path = os.path.join(ORIGINAL_SCN_DIR, scn_name)
        shutil.copy2(src_path, local_scn_path)

        # 2. Extract SCN to TOML
        route = classify_route(scn_name)
        toml_name = scn_name.replace(".txt.scn", ".txt.toml").replace(".scn", ".toml")
        output_path = os.path.join(OUTPUT_DIR, route, toml_name)

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        result = subprocess.run(
            [EXTRACTOR_EXE, "--slot", "2", local_scn_path, output_path],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"  [{i}/{len(scn_names)}] {route}/{toml_name} [OK]")
            success += 1
        else:
            print(f"  [{i}/{len(scn_names)}] {route}/{toml_name} [FAIL] -> {result.stderr.strip()}")

    print(f"\nCompleted: {success}/{len(scn_names)} files processed.")

if __name__ == "__main__":
    main()
