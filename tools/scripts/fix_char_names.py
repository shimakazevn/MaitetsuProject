import sys

sys.stdout.reconfigure(encoding='utf-8')
p = r'E:\MaitetsuProject\translation_toml\00_Common\共通02_日々姫と真闇と人形と.txt.toml'
with open(p, 'r', encoding='utf-8-sig') as f:
    text = f.read()

replacements = {
    '2946 = "日々姫"': '2946 = "Hibiki"',
    '2784 = "双鉄"': '2784 = "Soutetsu"',
    '3045 = "真闇"': '3045 = "Mayami"',
    '2677 = "ハチロク"': '2677 = "Hachiroku"',
    '2971 = "日日姬"': '2971 = "Hibiki"',
    '3201 = "雙鐵"': '3201 = "Soutetsu"',
    '3249 = "？？？"': '3249 = "???"',
    '2740 = "八六"': '2740 = "Hachiroku"',
    '3002 = "日日姬＆八六"': '3002 = "Hibiki & Hachiroku"'
}

for k, v in replacements.items():
    text = text.replace(k, v)

with open(p, 'w', encoding='utf-8-sig') as f:
    f.write(text)
print("Done replacing character names.")
