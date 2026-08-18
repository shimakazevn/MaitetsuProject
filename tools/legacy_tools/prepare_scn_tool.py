import os
import shutil
import sys
import subprocess

# Add pipeline directory to path to reuse get_prioritized_scns
sys.path.append(r"E:\MaitetsuProject")
from localization_pipeline import get_prioritized_scns

def main():
    game_dir = r"E:\まいてつ Last Run!!"
    scn_tool_dir = r"D:\Games\tools\scn-tool-main"
    old_scn_dir = os.path.join(scn_tool_dir, "old-scn")
    toml_dir = os.path.join(scn_tool_dir, "toml")
    
    os.makedirs(old_scn_dir, exist_ok=True)
    os.makedirs(toml_dir, exist_ok=True)
    
    # 1. Get prioritized scn files
    print("Resolving prioritized SCN files...")
    prioritized = get_prioritized_scns()
    print(f"Found {len(prioritized)} prioritized SCN files.")
    
    # 2. Copy to old-scn/
    print("Copying SCN files to old-scn...")
    copied_count = 0
    for name, info in prioritized.items():
        src_path = info['path']
        # The tool expects filename to end with .txt.scn
        dest_filename = name  # name already ends with .txt.scn
        dest_path = os.path.join(old_scn_dir, dest_filename)
        shutil.copy2(src_path, dest_path)
        copied_count += 1
        
    print(f"[OK] Copied {copied_count} files to {old_scn_dir}.")
    
    # 3. Run extractor.bat
    print("Running extractor.bat...")
    # Change working directory to scn_tool_dir to run extractor.bat correctly
    result = subprocess.run([os.path.join(scn_tool_dir, "extractor.bat")], cwd=scn_tool_dir, capture_output=True, text=True)
    print("Extractor output:")
    print(result.stdout[:500])
    if result.stderr:
        print("Extractor errors:")
        print(result.stderr[:500])
        
    print("[OK] Finished preparing SCN tool workspace.")

if __name__ == "__main__":
    main()
