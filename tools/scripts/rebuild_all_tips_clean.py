import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

project_dir = r"E:\MaitetsuProject"
context_file = os.path.join(project_dir, "docs", "context_trans.md")
patch_assets = os.path.join(project_dir, "patch_assets")
steam_patch_assets = os.path.join(project_dir, "steam_version_patch_vn", "patch_assets")

def parse_context_trans():
    with open(context_file, "r", encoding="utf-8") as fp:
        content = fp.read()

    # Split by ## <num>.
    sections = re.split(r'\n##\s*\d+\.\s*', content)
    tips_dict = {}

    for sec in sections:
        if not sec.strip(): continue
        lines = sec.strip().splitlines()
        header = lines[0]
        if "➔" not in header: continue
        
        orig_name, vi_name = header.split("➔", 1)
        orig_name = orig_name.strip()
        vi_name = vi_name.strip()

        # Clean title for filename: remove ruby brackets like [６２００'六二] -> ６２００
        clean_filename_name = orig_name
        if clean_filename_name.startswith("[") and "'" in clean_filename_name and clean_filename_name.endswith("]"):
            clean_filename_name = clean_filename_name[1:].split("'")[0]

        # Extract explanation body after ### Giải thích
        body_start = -1
        for i, l in enumerate(lines):
            if "### Giải thích" in l:
                body_start = i + 1
                break

        if body_start == -1:
            body_start = 1

        body_lines = []
        for l in lines[body_start:]:
            if l.startswith("---"): break
            body_lines.append(l)

        # Build clean tw_tips content
        # Line 1: Title (Vietnamese title)
        # Line 2: *解説
        # Line 3: ;---------------------------------------------------------------
        # Line 4+: Content
        
        cleaned_body = "\n".join(body_lines).strip()
        # Remove any leading delimiter if present
        cleaned_body = re.sub(r'^[;\-=\s]+', '', cleaned_body)
        
        full_text = f"{vi_name}\n*解説\n;---------------------------------------------------------------\n{cleaned_body}\n"
        tips_dict[clean_filename_name] = full_text

    return tips_dict

def clean_and_replace_tips(target_dir, tips_dict):
    print(f"\nCleaning and regenerating TIPS in: {target_dir}")
    os.makedirs(target_dir, exist_ok=True)
    
    # 1. Remove all old tw_tips_*.txt files (especially corrupted ones)
    removed_count = 0
    for f in os.listdir(target_dir):
        if f.startswith("tw_tips_") and f.endswith(".txt"):
            os.remove(os.path.join(target_dir, f))
            removed_count += 1
    print(f"  -> Removed {removed_count} old/corrupted tw_tips files.")

    # 2. Write all clean TIPS files with UTF-16LE + BOM
    written_count = 0
    for name, text in tips_dict.items():
        fname = f"tw_tips_{name}.txt"
        fpath = os.path.join(target_dir, fname)
        with open(fpath, "wb") as fp:
            fp.write(b"\xff\xfe" + text.encode("utf-16le"))
        written_count += 1

    print(f"  -> Generated {written_count} pristine UTF-16LE tw_tips files.")

def main():
    tips_dict = parse_context_trans()
    print(f"Successfully parsed {len(tips_dict)} TIPS from {context_file}")
    
    clean_and_replace_tips(patch_assets, tips_dict)
    clean_and_replace_tips(steam_patch_assets, tips_dict)
    print("\nAll TIPS rebuilt cleanly without mojibake or corrupt characters!")

if __name__ == "__main__":
    main()
