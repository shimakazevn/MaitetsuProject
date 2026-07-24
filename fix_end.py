import sys

sys.stdout.reconfigure(encoding='utf-8')

p = r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml'

with open(p, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# 1. Collect all active key lines from L1280 onwards
active_indices = []
for i in range(1280, len(lines)):
    line = lines[i]
    if '=' in line and not line.strip().startswith('#'):
        active_indices.append(i)

print(f"Found {len(active_indices)} active keys from L1280 to end.")

# 2. Extract their old VN strings
old_vns = []
for idx in active_indices:
    k, v = lines[idx].split('=', 1)
    old_vns.append(v.strip())

# 3. Create the new VN strings by shifting up by 3
new_vns = []
for i in range(len(old_vns) - 3):
    new_vns.append(old_vns[i+3])

# The last 3 are the ones that got cut off. I'll add them manually based on the master dictionary:
missing_3 = [
    '"Trong vòng tay tôi, đột nhiên cất lên giọng nói rất lớn. Hachiroku bắt đầu cựa quậy giãy giụa."',
    '"「Sao vậy Hachiroku?」"',
    '"「Tôi không bao giờ ngồi lên \\\\x%lエアクラ;#00ffc040;Aircra%l;#; đâu! \\n\\\\x%lエアクラ;#00ffc040;Aircra%l;#; là, đó là kẻ thù không đội trời chung của chúng tôi!!」"'
]
new_vns.extend(missing_3)

# 4. Overwrite the lines
for i, idx in enumerate(active_indices):
    k = lines[idx].split('=', 1)[0]
    lines[idx] = f'{k}= {new_vns[i]}\n'

with open(p, 'w', encoding='utf-8-sig') as f:
    f.writelines(lines)

print("✅ Successfully shifted and restored the translations for the end of the file!")
