import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()

pairs = []
for i in range(653, 1184):
    line = lines[i].strip()
    if line.startswith('# JP: '):
        jp = line[6:]
        for j in range(i+1, min(i+10, len(lines))):
            if '=' in lines[j] and not lines[j].strip().startswith('#'):
                k, v = lines[j].split('=', 1)
                pairs.append({'idx': i, 'key': k.strip(), 'jp': jp, 'vn': v.strip().strip('"')})
                break

with open(r'E:\MaitetsuProject\dump_middle.txt', 'w', encoding='utf-8') as f:
    for i, p in enumerate(pairs):
        f.write(f"[{i:03d}] {p['key']} | {p['jp'][:35]} | {p['vn'][:45]}\n")
