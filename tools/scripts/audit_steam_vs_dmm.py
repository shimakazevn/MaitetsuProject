import os
import sys
import difflib

DMM_PATCH_DIR = r'E:\MaitetsuProject\steam_version_patch_vn\patch_assets'
STEAM_ORIG_DIR = r'E:\MaitetsuProject\steam_version_patch_vn\extracted_assets\others'

def read_file_clean(path):
    for enc in ['utf-16le', 'utf-8', 'cp932', 'gbk', 'big5']:
        try:
            with open(path, 'r', encoding=enc) as f:
                return f.read(), enc
        except Exception:
            pass
    with open(path, 'rb') as f:
        return f.read().decode('utf-8', errors='ignore'), 'binary'

def main():
    print('=' * 75)
    print('   AUDIT & DIFF ANALYSIS: DMM PATCH ASSETS vs STEAM ORIGINAL ASSETS')
    print('=' * 75)

    dmm_files = {}
    for root, _, files in os.walk(DMM_PATCH_DIR):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), DMM_PATCH_DIR)
            dmm_files[rel] = os.path.join(root, f)

    steam_files = {}
    for root, _, files in os.walk(STEAM_ORIG_DIR):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), STEAM_ORIG_DIR)
            steam_files[rel] = os.path.join(root, f)

    print(f'Total files in DMM Patch:   {len(dmm_files)}')
    print(f'Total files in Steam Clean: {len(steam_files)}\n')

    # 1. Check TJS files specifically
    print('[1] TJS SCRIPT AUDIT:')
    print('-' * 75)
    tjs_dmm = {k: v for k, v in dmm_files.items() if k.endswith('.tjs')}
    
    for rel_name, dmm_path in sorted(tjs_dmm.items()):
        steam_path = steam_files.get(rel_name)
        if not steam_path:
            # Check without tw or with tw
            print(f'  [ONLY IN DMM PATCH] {rel_name}')
            continue

        dmm_content, dmm_enc = read_file_clean(dmm_path)
        steam_content, steam_enc = read_file_clean(steam_path)

        dmm_lines = dmm_content.splitlines()
        steam_lines = steam_content.splitlines()

        if dmm_content.strip() == steam_content.strip():
            print(f'  [IDENTICAL]         {rel_name} ({len(steam_lines)} lines)')
        else:
            diff = list(difflib.unified_diff(steam_lines, dmm_lines, lineterm=''))
            print(f'  [DIFFERENCE FOUND]  {rel_name} -> Steam: {len(steam_lines)} lines | DMM Patch: {len(dmm_lines)} lines (Diff chunks: {len(diff)})')

    # 2. Check Key INI / CSV Configuration Files
    print('\n[2] CONFIG & DATA AUDIT (.ini / .csv):')
    print('-' * 75)
    config_exts = ('.ini', '.csv')
    configs_dmm = {k: v for k, v in dmm_files.items() if any(k.endswith(ext) for ext in config_exts)}

    for rel_name, dmm_path in sorted(configs_dmm.items()):
        steam_path = steam_files.get(rel_name)
        if not steam_path:
            print(f'  [ONLY IN DMM PATCH] {rel_name}')
            continue

        dmm_content, _ = read_file_clean(dmm_path)
        steam_content, _ = read_file_clean(steam_path)

        dmm_lines = dmm_content.splitlines()
        steam_lines = steam_content.splitlines()

        if dmm_content.strip() == steam_content.strip():
            print(f'  [IDENTICAL]         {rel_name} ({len(steam_lines)} lines)')
        else:
            print(f'  [DIFFERENCE FOUND]  {rel_name} -> Steam: {len(steam_lines)} lines | DMM Patch: {len(dmm_lines)} lines')

    # 3. Check Files in Steam Original that are NOT in DMM Patch
    print('\n[3] NEW FILES IN STEAM (Missing in DMM Patch):')
    print('-' * 75)
    new_in_steam = [k for k in steam_files if k not in dmm_files and not k.endswith('.txt')]
    for rel_name in sorted(new_in_steam)[:25]:
        print(f'  [STEAM NEW] {rel_name}')
    if len(new_in_steam) > 25:
        print(f'  ... and {len(new_in_steam) - 25} more files.')

if __name__ == '__main__':
    main()
