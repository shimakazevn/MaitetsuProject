import os
import sys
import glob
import codecs
import time
import re
import subprocess
from deep_translator import GoogleTranslator

# Character name replacements (to make translation cleaner)
CHAR_MAP = {
    "【ハチロク】": "【Hachiroku】",
    "【双鉄】": "【Soutetsu】",
    "【日々姫】": "【Hibiki】",
    "【ポーレット】": "【Paulette】",
    "【真闇】": "【Mayami】",
    "【稀咲】": "【Kisaki】",
    "【凪】": "【Nagi】",
    "【深美】": "【Fukami】",
    "【れいな】": "【Reina】",
    "【ニイロク】": "【Niiroku】",
    "【ナビ】": "【Navi】",
    "【みのり】": "【Minori】",
    "【ひよこ】": "【Hiyoko】",
    "【りいれ】": "【Riire】",
    "【キハ07】": "【Kiha 07】",
    "【路線】": "【Tuyến】",
}

def read_file(path):
    for enc in ["utf-8-sig", "utf-8", "utf-16", "cp950"]:
        try:
            with codecs.open(path, "r", enc) as f:
                return f.read()
        except Exception:
            continue
    # Fallback with ignore
    with codecs.open(path, "r", "utf-8", errors="ignore") as f:
        return f.read()

def clean_text_for_trans(text):
    # Temporarily replace character brackets so Google Translator doesn't mess them up
    for jp, vn in CHAR_MAP.items():
        text = text.replace(jp, vn)
    return text

def translate_text(translator, text):
    if not text.strip():
        return text
    # Clean brackets
    text = clean_text_for_trans(text)
    
    # Try translation
    for retry in range(5):
        try:
            val = translator.translate(text)
            if val:
                return val
        except Exception as e:
            print(f"  [WARN] Translation failed, retrying in 2s... Error: {e}")
            time.sleep(2)
    return text

def main():
    game_dir = r"E:\まいてつ Last Run!!"
    
    # Scan files in patch2 and patch
    files2 = {os.path.basename(p): p for p in glob.glob(os.path.join(game_dir, "KrkrExtract_Output", "patch2", "tw_tips_*.txt"))}
    files1 = {os.path.basename(p): p for p in glob.glob(os.path.join(game_dir, "KrkrExtract_Output", "patch", "tw_tips_*.txt"))}
    
    # Merge (patch2 has priority)
    all_files = {}
    all_files.update(files1)
    all_files.update(files2)
    
    sorted_filenames = sorted(all_files.keys())
    total = len(sorted_filenames)
    print(f"Found {total} unique TIPS files to translate.")
    
    translator = GoogleTranslator(source='zh-TW', target='vi')
    
    glossary = []
    
    for i, fname in enumerate(sorted_filenames):
        path = all_files[fname]
        content = read_file(path)
        
        # Split into lines
        lines = content.splitlines()
        if len(lines) < 2:
            continue
            
        orig_title = lines[0].strip()
        
        # Translate title
        vi_title = translate_text(translator, orig_title)
        
        # Reconstruct body
        body_lines = []
        for line in lines[1:]:
            if line.strip() == "*解説":
                body_lines.append("*解説")
            else:
                body_lines.append(line)
        body = "\r\n".join(body_lines)
        
        # Translate body
        vi_body = translate_text(translator, body)
        
        # Construct final file content
        vi_content = f"{vi_title}\r\n{vi_body}\r\n"
        
        # Save to vn_patch
        out_path = os.path.join(game_dir, "vn_patch", fname)
        with codecs.open(out_path, "w", "utf-8-sig") as f:
            f.write(vi_content)
            
        try:
            sys.stdout.reconfigure(encoding='utf-8')
            print(f"[{i+1}/{total}] Translated {fname}: {orig_title} -> {vi_title}")
        except Exception:
            pass
        
        # Append to glossary
        glossary.append({
            "orig_title": orig_title,
            "vi_title": vi_title,
            "body": vi_body.replace("*解説\r\n", "").replace("*解説\n", "").strip()
        })
        
        # Brief sleep to avoid spamming the API
        time.sleep(0.3)
        
    # Write context_trans.md
    md_path = os.path.join(game_dir, "context_trans.md")
    print(f"Writing {md_path}...")
    with codecs.open(md_path, "w", "utf-8") as f:
        f.write("# TỔNG HỢP VIỆT HÓA TIPS - MAITETSU LAST RUN!!\n\n")
        for idx, item in enumerate(glossary):
            f.write(f"## {idx+1}. {item['orig_title']} ➔ {item['vi_title']}\n")
            f.write("### Giải thích:\n")
            f.write(f"{item['body']}\n\n")
            f.write("---\n\n")
            
    # Stop the game
    print("Stopping game...")
    subprocess.run(["powershell", "Stop-Process -Name 'まいてつ*' -Force -ErrorAction SilentlyContinue"])
    
    # Rebuild patch3.xp3
    print("Packing patch3.xp3...")
    sys.path.append(os.path.join(game_dir, "tools"))
    from make_patch3_maitetsu import pack_maitetsu_xp3
    pack_maitetsu_xp3(os.path.join(game_dir, "vn_patch"), os.path.join(game_dir, "patch3.xp3"))
    
    # Start the game
    print("Starting game...")
    subprocess.run(["powershell", f"Start-Process -FilePath '{os.path.join(game_dir, 'まいてつ Last Run!!.exe')}'"])
    print("[OK] Finished all TIPS translation.")

if __name__ == "__main__":
    main()
