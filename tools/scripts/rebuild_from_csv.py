import os
import sys
import csv
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

extractor_exe = r'E:\MaitetsuProject\scn-script-extractor.exe'
scn_file = r'E:\MaitetsuProject\original_scn\共通02_日々姫と真闇と人形と.txt.scn'
csv_file = r'e:\MaitetsuProject\Matetsu Last Run - Trang tính3.csv'
output_toml = r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml'

extracted_toml = r'E:\MaitetsuProject\original_scn\共通02_日々姫と真闇と人形と.txt.toml'
if os.path.exists(extracted_toml):
    os.remove(extracted_toml)

print("Extracting fresh TOML from SCN...")
cmd = [extractor_exe, scn_file, '--slot', '2']
subprocess.run(cmd, check=True)

if not os.path.exists(extracted_toml):
    print(f"Error: {extracted_toml} not found!")
    sys.exit(1)

print("Reading CSV translations...")
translations = {}
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 8 and '共通02_日々姫と真闇と人形と' in row[0]:
            key = row[2].strip()
            vn_text = row[7].strip()
            if vn_text:
                translations[key] = vn_text

print("Patching TOML...")
with open(extracted_toml, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

patched_lines = []
missing_count = 0
for line in lines:
    if '=' in line and not line.strip().startswith('#'):
        key, val = line.split('=', 1)
        k = key.strip()
        if k in translations:
            vn_str = translations[k].replace('"', '\\"')
            patched_lines.append(f'{k} = "{vn_str}"\n')
        else:
            patched_lines.append(line)
            missing_count += 1
            print(f"Missing translation for Key: {k} (Length of value: {len(val)})")
    else:
        patched_lines.append(line)

print(f"Total active keys without translation: {missing_count}")

with open(output_toml, 'w', encoding='utf-8-sig') as f:
    f.writelines(patched_lines)
print(f"Saved patched TOML to {output_toml}")

os.remove(extracted_toml)
print("Done!")
