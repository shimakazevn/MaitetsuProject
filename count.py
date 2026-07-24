import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

vn_strings = []
for line in lines:
    if '=' in line and not line.strip().startswith('#'):
        k, v = line.split('=', 1)
        vn_strings.append(v.strip().strip('"'))

jp_lines = []
for line in lines:
    if line.strip().startswith('# JP:'):
        jp_lines.append(line.strip()[5:].strip())

print(f'Total VN strings: {len(vn_strings)}')
print(f'Total JP lines: {len(jp_lines)}')
