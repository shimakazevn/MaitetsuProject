import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1600, len(lines)):
    line = lines[i].strip()
    if line.startswith('# JP: '):
        print(f'L{i+1} JP: {line[6:]}')
    elif '=' in line and not line.startswith('#'):
        val = line.split('=', 1)[1].strip().strip('\"')
        print(f'L{i+1} VN: {val}')
