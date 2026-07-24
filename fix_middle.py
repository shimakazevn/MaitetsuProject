import sys

sys.stdout.reconfigure(encoding='utf-8')

p = r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml'

with open(p, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

# 1. Collect all active key lines from L653 to L1184 (indices 652 to 1183)
# Plus, grab the next 2 active keys after L1184 to fill in the missing 2!
active_indices = []
for i in range(652, len(lines)):
    line = lines[i]
    if '=' in line and not line.strip().startswith('#'):
        active_indices.append(i)

# We need the first 146 active keys (0 to 145) from the block, plus 2 extra for the shift
# Let's extract exactly the first 148 active keys starting from L653.
subset_indices = active_indices[:148]

old_vns = []
for idx in subset_indices:
    k, v = lines[idx].split('=', 1)
    old_vns.append(v.strip())

new_vns = []
for i in range(146):
    if i < 79:
        # Match perfectly
        new_vns.append(old_vns[i])
    elif i >= 79 and i <= 91:
        # Shift up by 1 due to duplicate at 78/79
        new_vns.append(old_vns[i+1])
    elif i == 92:
        # Missing translation for "…………"
        new_vns.append('"「…………」"')
    elif i >= 93 and i <= 99:
        # Shift up by 1 (we skipped 92, so we just take i+1)
        new_vns.append(old_vns[i+1])
    elif i >= 100:
        # Shift up by 2 due to duplicate at 100/101
        new_vns.append(old_vns[i+2])

# Overwrite the first 146 active keys
for i in range(146):
    idx = subset_indices[i]
    k = lines[idx].split('=', 1)[0]
    lines[idx] = f'{k}= {new_vns[i]}\n'

with open(p, 'w', encoding='utf-8-sig') as f:
    f.writelines(lines)

print("✅ Successfully shifted and restored the translations for the middle of the file!")
