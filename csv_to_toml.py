import os
import re
import csv
import codecs

PROJECT_DIR = r"E:\MaitetsuProject"
CSV_PATH = os.path.join(PROJECT_DIR, "maitetsu_translation.csv")

def escape_value(val):
    # Escape backslashes and double quotes for TOML string
    return val.replace('\\', '\\\\').replace('"', '\\"')

def main():
    if not os.path.exists(CSV_PATH):
        print(f"Error: CSV file {CSV_PATH} not found!")
        return

    # 1. Read CSV updates
    print("Reading translations from CSV...")
    updates = {}
    
    with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rel_file = row['File']
            key = row['Key']
            vi_text = row['Vietnamese'].strip()
            
            # Only update if Vietnamese column is not empty
            if vi_text:
                if rel_file not in updates:
                    updates[rel_file] = {}
                updates[rel_file][key] = vi_text
                
    if not updates:
        print("No Vietnamese translations found in CSV.")
        return

    print(f"Applying updates to {len(updates)} TOML files...")
    
    # 2. Apply to TOML files
    updated_files_count = 0
    updated_lines_count = 0
    
    for rel_file, file_updates in updates.items():
        toml_path = os.path.join(PROJECT_DIR, rel_file)
        if not os.path.exists(toml_path):
            print(f"  [WARN] TOML file not found: {toml_path}")
            continue
            
        # Read TOML lines
        with codecs.open(toml_path, 'r', 'utf-8-sig', errors='ignore') as f:
            lines = f.readlines()
            
        new_lines = []
        file_changed = False
        current_section = None
        
        for line in lines:
            line_stripped = line.strip()
            
            # Check section header
            if line_stripped.startswith('[') and line_stripped.endswith(']'):
                current_section = line_stripped[1:-1]
                new_lines.append(line)
                continue
                
            if current_section not in ('script', 'selections'):
                new_lines.append(line)
                continue
                
            # Match Key = Value
            m = re.match(r'^(\d+)(\s*=\s*)(.+)$', line)
            if m:
                key = m.group(1)
                equals = m.group(2)
                
                if key in file_updates:
                    vi_val = file_updates[key]
                    escaped_vi = escape_value(vi_val)
                    # Check if line ending has newline
                    nl = "\r\n" if line.endswith("\r\n") else "\n"
                    # Write key = "escaped_vi"
                    new_line = f'{key}{equals}"{escaped_vi}"{nl}'
                    new_lines.append(new_line)
                    updated_lines_count += 1
                    file_changed = True
                    continue
                    
            new_lines.append(line)
            
        if file_changed:
            with codecs.open(toml_path, 'w', 'utf-8-sig') as f:
                f.writelines(new_lines)
            updated_files_count += 1
            print(f"  Updated: {rel_file}")
            
    print(f"\n[OK] Successfully updated {updated_lines_count} lines across {updated_files_count} TOML files.")

if __name__ == "__main__":
    main()
