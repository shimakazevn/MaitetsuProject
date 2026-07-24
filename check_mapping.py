import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

active_keys = []
for i in range(1280, len(lines)):
    line = lines[i].strip()
    if line.startswith('# JP: '):
        jp = line[6:]
        # find the next active key
        for j in range(i+1, min(i+10, len(lines))):
            if '=' in lines[j] and not lines[j].strip().startswith('#'):
                k, v = lines[j].split('=', 1)
                active_keys.append((k.strip(), jp, v.strip().strip('"')))
                break

for idx, (k, jp, v) in enumerate(active_keys):
    print(f'[{idx:03d}] {jp[:30]}... -> {v[:40]}...')
