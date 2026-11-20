# Build audit-lr-hachirokuh2-wrong.json + TOML block from hand-written fixes.
# Fixes are (old, new, count, mode) replacements applied to the EXACT CSV3 old_vn,
# so jp/tw/old_vn in the JSON are byte-identical to CSV3.
# mode 'lit': literal substring (count must equal occurrences). 'word': regex
# word-boundary (avoids corrupting e.g. "thanh"). 'first': replace first `count`.
import csv, json, tomllib, difflib, sys, re

CSV = 'sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv'
FILE_BASENAME = 'lr_ハチロクh2_新しい服。新しい旅.txt.toml'

FIXES = {
 # --- pronoun: Soutetsu "anh" -> "tôi" with Hachiroku (22 rows) ---
 '1120': ('pronoun', [('anh', 'tôi', 4, 'word')]),
 '1358': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1361': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1402': ('pronoun', [('anh', 'tôi', 2, 'word')]),
 '1507': ('pronoun', [('anh', 'tôi', 1, 'word'), ('Anh', 'Tôi', 1, 'word')]),
 '1513': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1516': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1539': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1557': ('pronoun+gasp', [('Anh', 'Tôi', 1, 'word'), ('——!!!?', '——Ư!!!?', 1, 'lit')]),
 '1560': ('pronoun', [('Anh', 'Tôi', 2, 'word')]),
 '1566': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1574': ('pronoun', [('anh', 'tôi', 2, 'word')]),
 '1578': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1595': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1599': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1619': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1623': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1624': ('pronoun', [('anh', 'tôi', 2, 'word')]),
 '1648': ('pronoun', [('Anh', 'Tôi', 1, 'word')]),
 '1669': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1671': ('pronoun', [('anh', 'tôi', 1, 'word')]),
 '1681': ('pronoun+gasp', [('anh', 'tôi', 1, 'word'), ('——!?', '——Ư!?', 1, 'lit')]),
 # --- gasp: sweep entries (15 pure; 1557/1681 above are the other 2) ---
 '1414': ('gasp', [('「っ」', '「Ư」', 1, 'lit')]),
 '1415': ('gasp', [('っ!!!', 'Ư!!!', 1, 'lit')]),
 '1416': ('gasp', [('っ!!!!', 'Ư!!!!', 1, 'lit')]),
 '1417': ('gasp', [('「!?」', '「Ư!?」', 1, 'lit')]),
 '1418': ('gasp', [('「っ——', '「Ư——', 1, 'lit')]),
 '1456': ('gasp', [('っ!!!!', 'Ư!!!!', 1, 'lit')]),
 '1457': ('gasp', [('っ!!!!!!', 'Ư!!!!!!', 1, 'lit')]),
 '1458': ('gasp', [('っ!!!!!!!!', 'Ư!!!!!!!!', 1, 'lit')]),
 '1459': ('gasp', [('「!!!?」', '「Ư!!!?」', 1, 'lit')]),
 '1462': ('gasp', [('——っ——', '——Ư——', 1, 'lit')]),
 '1474': ('gasp', [('A~~~~', 'A~~~~Ư', 1, 'lit')]),
 '1483': ('gasp', [('っ——!!!!', 'Ư——!!!!', 1, 'lit')]),
 '1583': ('gasp', [('\\nっ——', '\\nƯ——', 1, 'lit')]),
 '2009': ('gasp', [('——!!', '——Ư!!', 1, 'lit')]),
 '2109': ('gasp', [('——!?', '——Ư!?', 1, 'lit')]),
 # --- gasp: new, absolute-final っ on sound-words (12 rows) ---
 '1105': ('gasp', [('——A」', '——AƯ」', 1, 'lit')]),
 '1407': ('gasp', [('Hya!!!!', 'HyauƯ!!!!', 1, 'lit')]),
 '1408': ('gasp', [('Hyauuu!!!?', 'HyauuuƯ!!!?', 1, 'lit')]),
 '1410': ('gasp', [('Yuun!!!', 'YuunƯ!!!', 1, 'lit')]),
 '1411': ('gasp', [('Hya!!!!', 'HyauƯ!!!!', 1, 'lit')]),
 '1429': ('gasp', [('Ahyu!!!', 'AhyuƯ!!!', 1, 'lit')]),
 '1433': ('gasp', [('A!!!', 'AƯ!!!', 1, 'lit')]),
 '1463': ('gasp', [('a」', 'aƯ」', 1, 'lit')]),
 '1470': ('gasp', [('Aaaaaa」', 'AaaaaaƯ」', 1, 'lit')]),
 '1472': ('gasp', [('Hau.」', 'HauƯ.」', 1, 'lit')]),
 '1486': ('gasp', [('——a!」', '——aƯ!」', 1, 'lit')]),
 '1527': ('gasp', [('Aa!」', 'AaƯ!」', 1, 'lit')]),
 # --- laughter: giggles rendered as groans (7 rows) ---
 '1423': ('laughter', [('Ưm hừm', 'Nfufu', 1, 'lit')]),
 '1424': ('laughter', [('Hư——ư hừ——ư hừ hừ hừ', 'Hư——Ufu——Ufufufufu', 1, 'lit')]),
 '1447': ('laughter', [('Hừ hừ」', 'Fufu」', 1, 'lit')]),
 '1508': ('laughter', [('Ưm hừm.', 'Nfufu.', 1, 'lit')]),
 '1511': ('laughter', [('Ư hừ hừ,', 'Ufufu,', 1, 'lit')]),
 '1547': ('laughter', [('ư hừ hừ」', 'Ufufu」', 1, 'lit')]),
 '1606': ('laughter', [('Ư hừ hừ.', 'Ufufu.', 1, 'lit')]),
 # --- meaning (3 rows) ---
 '1436': ('meaning', [('ngài Soutetsu, sâu quá!', 'ngài Soutetsu!', 1, 'lit'),
                      ('Của em, của em,', 'Em, em,', 1, 'lit')]),
 '1593': ('meaning', [('ngài muốn mặc bộ quần áo nào', 'ngài muốn em mặc bộ quần áo nào', 1, 'lit')]),
 '1836': ('meaning', [('（Mặc dù', 'Mặc dù', 1, 'lit'),
                      ('trừng phạt em ấy', 'được em ấy trừng phạt', 1, 'lit'),
                      ('hiểu lầm.）', 'hiểu lầm.', 1, 'lit')]),
 # --- SFX (3 rows) ---
 '1714': ('sfx', [('（Ngậm lấy）', '（Gupoooooooo）', 1, 'lit')]),
 '1716': ('sfx', [('（Liếm——liếm——liếm）', '（Nụtọooo——liếm——Chùn chụt）', 1, 'lit')]),
 '1718': ('sfx', [('Chụt!', 'Chụụụt!', 1, 'first')]),
 # --- terminology (1 row) ---
 '1440': ('terminology', [('Tablet', 'máy tính bảng', 1, 'lit')]),
}

with open(CSV, encoding='utf-8-sig', newline='') as f:
    rows = {x['Key']: x for x in csv.DictReader(f)
            if x['File'].split(chr(92))[-1] == FILE_BASENAME}
assert len(rows) == 327, len(rows)

entries = []
errors = []
for key in sorted(FIXES, key=int):
    kind, reps = FIXES[key]
    row = rows.get(key)
    if row is None:
        errors.append(f'{key}: NOT IN CSV3')
        continue
    old = row['Vietnamese']
    fix = old
    for o, n, cnt, mode in reps:
        if mode == 'word':
            pat = re.compile(r'\b' + re.escape(o) + r'\b')
            found = len(pat.findall(fix))
            if found != cnt:
                errors.append(f'{key}: word {o!r} found {found}x, expected {cnt}x')
            fix = pat.sub(n, fix, count=cnt)
        elif mode == 'first':
            found = fix.count(o)
            if found < cnt:
                errors.append(f'{key}: {o!r} found {found}x, expected >= {cnt}x')
            fix = fix.replace(o, n, cnt)
        else:
            found = fix.count(o)
            if found != cnt:
                errors.append(f'{key}: literal {o!r} found {found}x, expected {cnt}x')
            fix = fix.replace(o, n, cnt)
    if fix == old:
        errors.append(f'{key}: fix identical to old_vn!')
    entries.append({'key': key, 'jp': row['JP Original'], 'tw': row['TW Original/Current'],
                    'old_vn': old, 'fix': fix, 'kind': kind, 'character': row['Character']})

print(f'entries: {len(entries)} (expected 63)')
if errors:
    print('ERRORS:')
    for e in errors:
        print(' ', e)
    sys.exit(1)

print('\n--- diff spans (old -> fix) ---')
for e in entries:
    sm = difflib.SequenceMatcher(None, e['old_vn'], e['fix'])
    spans = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal':
            spans.append(f"{e['old_vn'][max(0,i1-8):i2+8]!r} -> {e['fix'][max(0,j1-8):j2+8]!r}")
    print(e['key'], e['kind'], '|', ' ; '.join(spans))

with open('audit-lr-hachirokuh2-wrong.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)

def toml_esc(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

lines = ['[script]']
for e in entries:
    lines.append(f"{e['key']} = {toml_esc(e['fix'])}")
block = '\n'.join(lines) + '\n'
with open('audit-lr-hachirokuh2-tomlblock.txt', 'w', encoding='utf-8') as f:
    f.write('```toml\n' + block + '```\n')

parsed = tomllib.loads(block)
assert set(parsed.keys()) == {'script'}, parsed.keys()
script = parsed['script']
print(f'\nTOML block parses: {len(script)} keys')
mism = [(k, script[k], next(e['fix'] for e in entries if e['key'] == k))
        for k in script if script[k] != next(e['fix'] for e in entries if e['key'] == k)]
print('value mismatches vs JSON:', len(mism))
for m in mism:
    print(' ', m)
print('kinds:', {k: sum(1 for e in entries if e['kind'] == k) for k in sorted(set(e['kind'] for e in entries))})
print('characters:', {c: sum(1 for e in entries if e['character'] == c) for c in sorted(set(e['character'] for e in entries))})
