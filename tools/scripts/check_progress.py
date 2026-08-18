#!/usr/bin/env python3
import os
import sys
import glob
import re

if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOML_DIR = os.path.join(PROJECT_DIR, "translation_toml")

VN_REGEX = re.compile(r'[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', re.IGNORECASE)

def is_file_translated(content):
    # Check if there are Vietnamese accents (for normal script files)
    vn_chars = len(VN_REGEX.findall(content))
    if vn_chars >= 1:
        return True
    return False

def main():
    print("=" * 65)
    print("        Maitetsu Last Run!! - Translation Progress Report")
    print("=" * 65)

    subdirs = sorted([d for d in os.listdir(TOML_DIR) if os.path.isdir(os.path.join(TOML_DIR, d))])
    total_files = 0
    total_translated = 0

    print(f" {'Route / Folder':<30} | {'Files':<8} | {'Translated':<12} | {'Progress':<10}")
    print("-" * 65)

    for sub in subdirs:
        subpath = os.path.join(TOML_DIR, sub)
        tomls = [f for f in os.listdir(subpath) if f.endswith(".toml")]
        count = len(tomls)
        translated_in_route = 0

        for t in tomls:
            tp = os.path.join(subpath, t)
            try:
                with open(tp, "r", encoding="utf-8-sig", errors="ignore") as fp:
                    content = fp.read()
                if is_file_translated(content):
                    translated_in_route += 1
            except Exception:
                pass

        total_files += count
        total_translated += translated_in_route
        pct = (translated_in_route / count * 100) if count > 0 else 0
        print(f" {sub:<30} | {count:<8} | {translated_in_route:<12} | {pct:>6.1f}%")

    print("-" * 65)
    total_pct = (total_translated / total_files * 100) if total_files > 0 else 0
    print(f" {'TOTAL':<30} | {total_files:<8} | {total_translated:<12} | {total_pct:>6.1f}%")
    print("=" * 65)

if __name__ == "__main__":
    main()
