import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

project_dir = r"E:\MaitetsuProject"
context_file = os.path.join(project_dir, "docs", "context_trans.md")
ini_file = os.path.join(project_dir, "extracted_assets", "KrkrExtract_Output", "others", "tipsindex_tw.ini")
tw_tips_dir = os.path.join(project_dir, "extracted_assets", "KrkrExtract_Output", "others", "tips_tw")

target_dirs = [
    os.path.join(project_dir, "patch_assets"),
    os.path.join(project_dir, "steam_version_patch_vn", "patch_assets")
]

# Steam engine cannot handle full-width Unicode filenames (raises
# "Cannot convert given narrow string to wide string" at runtime).
# Only ASCII-safe paths are allowed in the Steam patch assets directory.
STEAM_PATCH_DIR = os.path.join(project_dir, "steam_version_patch_vn", "patch_assets")

def is_fullwidth(s):
    """Return True if string contains any full-width Unicode characters."""
    for ch in s:
        cp = ord(ch)
        # Full-width Latin/digits (Ａ-Ｚ ａ-ｚ ０-９) and full-width symbols (！-～)
        if 0xFF01 <= cp <= 0xFF60:
            return True
        # Halfwidth/Fullwidth Forms block (general)
        if 0xFFA0 <= cp <= 0xFFEF:
            return True
    return False

# 1. Parse CN -> JP mapping
with open(ini_file, 'r', encoding='utf-8-sig') as f:
    ini_text = f.read()

cn_to_jp = {
    '爐鉤': 'ポーカー',
    '黏著力': '粘着力',
    '車鉤': '連結器'
}
for line in ini_text.splitlines():
    l = line.strip()
    if not l or l.startswith('#') or len(l) <= 1:
        continue
    parts = l.split('\t')
    if len(parts) >= 2:
        cn_to_jp[parts[0].strip()] = parts[1].strip()

all_jp_keys = set(f[len('tw_tips_'):-len('.txt')] for f in os.listdir(tw_tips_dir) if f.startswith('tw_tips_') and f.endswith('.txt'))
print(f'Total target JP keys in game: {len(all_jp_keys)}')

# 2. Parse context_trans.md
with open(context_file, "r", encoding="utf-8") as fp:
    content = fp.read()

sections = re.split(r'\n##\s*\d+\.\s*', content)
tips_data = {} # jp_key -> (vi_name, clean_body, cn_name)

for sec in sections[1:]:
    lines = sec.strip().splitlines()
    header = lines[0]
    if "➔" not in header: continue
    
    orig_name, vi_name = header.split("➔", 1)
    orig_name = orig_name.strip()
    vi_name = vi_name.strip()

    clean_name = orig_name
    if clean_name.startswith("[") and "'" in clean_name and clean_name.endswith("]"):
        clean_name = clean_name[1:].split("'")[0]

    # Find Japanese key
    jp_key = None
    if clean_name in all_jp_keys:
        jp_key = clean_name
    elif clean_name in cn_to_jp and cn_to_jp[clean_name] in all_jp_keys:
        jp_key = cn_to_jp[clean_name]
    else:
        for cn, jp in cn_to_jp.items():
            if cn.replace(' ', '') == clean_name.replace(' ', ''):
                jp_key = jp
                break

    if not jp_key:
        print(f"Warning: could not resolve JP key for {clean_name}")
        jp_key = clean_name

    # Extract body after ### Giải thích
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

    cleaned_body = "\n".join(body_lines).strip()
    cleaned_body = re.sub(r'^[;\-=\s]+', '', cleaned_body)

    full_text = f"{vi_name}\n*解説\n;---------------------------------------------------------------\n{cleaned_body}\n"
    tips_data[jp_key] = (full_text, clean_name)

print(f'Successfully prepared {len(tips_data)} TIPS translations.')

# 3. Write clean TIPS files to target directories
for target_dir in target_dirs:
    print(f"\nWriting clean TIPS in: {target_dir}")
    os.makedirs(target_dir, exist_ok=True)
    
    # Remove old tw_tips files
    for f in os.listdir(target_dir):
        if f.startswith("tw_tips_") and f.endswith(".txt"):
            os.remove(os.path.join(target_dir, f))

    written_files = 0
    skipped_fullwidth = 0
    is_steam_target = os.path.normcase(os.path.normpath(target_dir)) == os.path.normcase(os.path.normpath(STEAM_PATCH_DIR))

    for jp_key, (text, cn_name) in tips_data.items():
        # 1. Primary: Write with Japanese key (used by Kirikiri engine)
        # Skip full-width filenames for Steam target (engine cannot handle them)
        if is_steam_target and is_fullwidth(jp_key):
            skipped_fullwidth += 1
        else:
            fname_jp = f"tw_tips_{jp_key}.txt"
            fpath_jp = os.path.join(target_dir, fname_jp)
            with open(fpath_jp, "wb") as fp:
                fp.write(b"\xff\xfe" + text.encode("utf-16le"))
            written_files += 1

        # 2. Secondary: Also write with Chinese key alias if different
        if cn_name and cn_name != jp_key:
            if is_steam_target and is_fullwidth(cn_name):
                skipped_fullwidth += 1
            else:
                fname_cn = f"tw_tips_{cn_name}.txt"
                fpath_cn = os.path.join(target_dir, fname_cn)
                with open(fpath_cn, "wb") as fp:
                    fp.write(b"\xff\xfe" + text.encode("utf-16le"))
                written_files += 1

    msg = f"  -> Generated {written_files} pristine UTF-16LE tw_tips files in {target_dir}"
    if skipped_fullwidth:
        msg += f" (skipped {skipped_fullwidth} full-width filenames: Steam-incompatible)"
    print(msg)

print("\n100% of TIPS files generated with exact engine keys and clean UTF-16LE BOM!")
