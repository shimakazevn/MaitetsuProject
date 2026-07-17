import os
import re
import csv
import codecs

PROJECT_DIR = r"E:\MaitetsuProject"
TOML_DIR = os.path.join(PROJECT_DIR, "translation_toml")
CSV_PATH = os.path.join(PROJECT_DIR, "maitetsu_translation.csv")

def has_cjk(s):
    # Check if string contains Chinese characters
    return any('\u4e00' <= char <= '\u9fff' for char in s)

def clean_value(val):
    # Remove outer quotes and unescape
    if val.startswith('"') and val.endswith('"'):
        val = val[1:-1]
    # Unescape escaped backslashes and quotes
    val = val.replace('\\\\', '\\').replace('\\"', '"')
    return val

def parse_toml(file_path):
    entries = []
    with codecs.open(file_path, 'r', 'utf-8-sig', errors='ignore') as f:
        lines = f.readlines()

    current_section = None
    char_name = ""
    display_name = ""
    jp_text = ""
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Section headers
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            char_name = ""
            display_name = ""
            jp_text = ""
            continue
            
        if current_section not in ('script', 'selections'):
            continue
            
        # Parse comments
        if line.startswith('#'):
            comment = line[1:].strip()
            if comment.startswith('【') and comment.endswith('】'):
                char_name = comment[1:-1]
            elif comment.startswith('display as '):
                display_name = comment[11:].strip()
            elif comment.startswith('JP:'):
                jp_text = comment[3:].strip()
            elif comment == "monologue":
                char_name = "monologue"
            continue
            
        # Parse Key = Value
        m = re.match(r'^(\d+)\s*=\s*(.+)$', line)
        if m:
            key = m.group(1)
            val = clean_value(m.group(2).strip())
            
            # If the current value is already translated (no CJK characters),
            # we default the Vietnamese column to this value.
            # Otherwise, the Vietnamese column is empty.
            if val and not has_cjk(val):
                vi_val = val
            else:
                vi_val = ""
                
            entries.append({
                'Key': key,
                'Section': current_section,
                'Character': char_name,
                'DisplayAs': display_name,
                'JP Original': jp_text,
                'TW Original/Current': val,
                'Vietnamese': vi_val
            })
            
            # Reset temporary fields
            char_name = ""
            display_name = ""
            jp_text = ""
            
    return entries

def main():
    all_entries = []
    
    print("Reading TOML files...")
    for root, dirs, files in os.walk(TOML_DIR):
        for f in files:
            if f.endswith('.toml'):
                full_path = os.path.join(root, f)
                rel_path = os.path.relpath(full_path, PROJECT_DIR)
                
                file_entries = parse_toml(full_path)
                for entry in file_entries:
                    entry['File'] = rel_path
                    all_entries.append(entry)
                    
    print(f"Found {len(all_entries)} lines to translate.")
    
    # Write to CSV
    print(f"Writing to CSV: {CSV_PATH}...")
    fieldnames = ['File', 'Section', 'Key', 'Character', 'DisplayAs', 'JP Original', 'TW Original/Current', 'Vietnamese']
    
    with open(CSV_PATH, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for entry in all_entries:
            writer.writerow(entry)
            
    print("[OK] CSV file generated successfully.")

if __name__ == "__main__":
    main()
