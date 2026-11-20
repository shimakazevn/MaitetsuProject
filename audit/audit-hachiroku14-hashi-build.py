# -*- coding: utf-8 -*-
"""Build audit-hachiroku14-hashi-wrong.json + TOML block from CSV3.
Fixes are hand-written targeted replacements on the FULL old VN value.
Literal \\n in CSV3 VN stays literal \\n in JSON fix values (json.dump writes \\\\n).
"""
import csv, json, tomllib, difflib

CSV = "sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv"
FILE = "ハチロク14_橋.txt.toml"

rows = {}
with open(CSV, newline='', encoding='utf-8-sig') as f:
    for r in csv.DictReader(f):
        if r['File'].split(chr(92))[-1] == FILE:
            rows[r['Key']] = r
assert len(rows) == 476, len(rows)

def rep(key, old_sub, new_sub, count=-1):
    """targeted replacement on the full old VN of key; asserts exactly the expected hits."""
    v = rows[key]['Vietnamese']
    n = v.count(old_sub)
    assert n >= 1, (key, old_sub)
    if count != -1:
        assert n == count, (key, old_sub, n, count)
    return v.replace(old_sub, new_sub)

FIX = {}
# ---- gasp (12) — sweep values adopted verbatim, 1914 resolved in-audit ----
FIX['1463'] = rep('1463', '——!!?', '——Ư!!?')
FIX['1614'] = rep('1614', '「!', '「Ư!').replace('——!!?', '——Ư!!?')
FIX['1834'] = rep('1834', '——!', '——Ư!')
FIX['1910'] = rep('1910', '「!', '「Ư!')
FIX['1911'] = rep('1911', '「!!!', '「Ư!!!')
FIX['1912'] = rep('1912', '「!!?', '「Ư!!?')
FIX['1915'] = rep('1915', '「!?', '「Ư!?')
FIX['1924'] = rep('1924', '「!」', '「Ư!」')
FIX['2195'] = rep('2195', '——!?', '——Ư!?')
FIX['2398'] = rep('2398', '——!?', '——Ư!?')
FIX['2746'] = rep('2746', '——!', '——Ư!')
FIX['1914'] = rep('1914', '「!!?', '「Ư!!?')

# ---- pronoun: Soutetsu "anh"/"em" -> "tôi" with Hachiroku (dialogue 26) ----
FIX['1551'] = rep('1551', 'anh bật', 'tôi bật')
FIX['1547'] = rep('1547', 'Anh bật', 'Tôi bật')
FIX['1737'] = rep('1737', 'Anh sẽ', 'Tôi sẽ')
FIX['1454'] = rep('1454', 'Anh sẽ', 'Tôi sẽ')
FIX['1714'] = rep('1714', 'Anh là', 'Tôi là')
FIX['1541'] = rep('1541', 'Anh……', 'Tôi……')
FIX['1508'] = rep('1508', 'Cả anh,', 'Cả tôi,')
FIX['1509'] = rep('1509', 'Vì có anh,', 'Vì có tôi,')
FIX['1684'] = rep('1684', 'Anh cũng', 'Tôi cũng')
FIX['1523'] = rep('1523', 'Anh, cũng', 'Tôi, cũng')
FIX['1735'] = rep('1735', 'anh muốn', 'tôi muốn')
FIX['1481'] = rep('1481', 'Anh và em', 'Tôi và em')
FIX['1856'] = rep('1856', 'Anh và em', 'Tôi và em')
FIX['1701'] = rep('1701', 'Em và Hachiroku', 'Tôi và Hachiroku')
FIX['1893'] = rep('1893', 'anh cũng', 'tôi cũng')
FIX['1890'] = rep('1890', 'anh cũng', 'tôi cũng')
FIX['1622'] = rep('1622', 'anh đã', 'tôi đã')
FIX['1821'] = rep('1821', 'của anh', 'của tôi')
FIX['1836'] = rep('1836', 'cho anh', 'cho tôi')
FIX['1542'] = rep('1542', 'Anh muốn', 'Tôi muốn')
v = rows['1900']['Vietnamese'].replace('Anh', 'Tôi').replace('anh', 'tôi')
assert v.count('Tôi') == 2 and v.count('tôi') == 1 and 'Anh' not in v and 'anh' not in v
FIX['1900'] = v
v = rows['1712']['Vietnamese'].replace('Anh', 'Tôi').replace('anh', 'tôi')
assert 'Anh' not in v and 'anh' not in v
FIX['1712'] = v
v = rows['1686']['Vietnamese'].replace('Anh', 'Tôi').replace('anh', 'tôi')
assert 'Anh' not in v and 'anh' not in v
FIX['1686'] = v
v = rows['1719']['Vietnamese'].replace('Anh', 'Tôi')
assert 'Anh' not in v
FIX['1719'] = v
v = rows['1493']['Vietnamese'].replace('Anh', 'Tôi').replace('anh', 'tôi')
assert 'Anh' not in v and 'anh' not in v
FIX['1493'] = v
FIX['1505'] = rep('1505', 'khao khát anh', 'khao khát tôi')

# ---- pronoun: monologue "anh" -> "tôi" (3) ----
v = rows['2582']['Vietnamese'].replace('anh', 'tôi')
assert v.count('tôi') == 2 and 'anh' not in v
FIX['2582'] = v
FIX['2741'] = rep('2741', 'anh đang', 'tôi đang')
FIX['2140'] = rep('2140', 'bản thân anh', 'bản thân tôi')

# ---- terminology (10 rows) ----
FIX['2927'] = rep('2927', 'nhân viên cơ vụ', 'thợ lái đầu máy')
FIX['2374'] = rep('2374', 'nhân viên cơ vụ', 'thợ lái đầu máy')
v = rows['2678']['Vietnamese'].replace('nhân viên cơ vụ', 'thợ lái đầu máy').replace('kíp lái', 'thân vận hành')
assert 'nhân viên cơ vụ' not in v and 'kíp lái' not in v
FIX['2678'] = v
FIX['2368'] = rep('2368', 'nhân viên cơ vụ', 'thợ lái đầu máy')
FIX['2455'] = rep('2455', 'kíp lái', 'thân vận hành')
FIX['2514'] = rep('2514', 'thân chính', 'thân bảo trì')
FIX['2910'] = rep('2910', 'thân chính', 'thân bảo trì')
FIX['2940'] = rep('2940', 'Kiha 07', 'KiHa 07')
FIX['2258'] = rep('2258', 'Jutsusen', 'Jutsu-sen')
FIX['1815'] = rep('1815', 'Ông nội', 'Ông ngoại')

# ---- meaning (1) ----
FIX['2948'] = '（Đúng nghĩa đen là mò mẫm rồi đây.）'

# ---- terminology decided per Hieu 21/11 01:51 (decide, don't park) ----
# 御一夜 (place/station) = "Ohitoyo" is a DECIDED term (19/11) + furigana おひとよ;
# 湯医 = "Yunoi" is a DECIDED term + furigana ゆのい at 1754. Fix in-file (7 rows).
# 2748 company name "Đường sắt Ohito" stays PARKED: Hieu must decide whether the
# railway company name itself changes (215 uses project-wide vs 5 "Ohitoyo").
FIX['1733'] = rep('1733', 'Về Ohito.', 'Về Ohitoyo.')
v = rows['1754']['Vietnamese'].replace('ở Yui ', 'ở Yunoi ').replace('trở về Ohito.', 'trở về Ohitoyo.')
assert 'ở Yui ' not in v and 'trở về Ohito.' not in v
FIX['1754'] = v
FIX['2372'] = rep('2372', 'ga Ohito,', 'ga Ohitoyo,')
FIX['2355'] = rep('2355', 'ga Ohito rồi', 'ga Ohitoyo rồi')
FIX['1696'] = rep('1696', 'của Ohito.', 'của Ohitoyo.')
FIX['1200'] = rep('1200', 'Ohito là', 'Ohitoyo là')
FIX['1777'] = rep('1777', 'trân trọng Ohito,', 'trân trọng Ohitoyo,')

print('fix count:', len(FIX))
assert len(FIX) == 59, len(FIX)

KIND = {}
for k in ['1463','1614','1834','1910','1911','1912','1915','1924','2195','2398','2746','1914']:
    KIND[k] = 'gasp'
for k in ['1551','1547','1737','1454','1714','1541','1508','1509','1684','1523','1735','1481','1856','1701','1893','1890','1622','1821','1836','1542','1900','1712','1686','1719','1493','1505','2582','2741','2140']:
    KIND[k] = 'pronoun'
for k in ['2927','2374','2678','2368','2455','2514','2910','2940','2258','1815','1733','1754','2372','2355','1696','1200','1777']:
    KIND[k] = 'terminology'
KIND['2948'] = 'meaning'

entries = []
for k in sorted(FIX, key=lambda x: int(x)):
    r = rows[k]
    entries.append({
        'key': k,
        'jp': r['JP Original'],
        'tw': r['TW Original/Current'],
        'old_vn': r['Vietnamese'],
        'fix': FIX[k],
        'kind': KIND[k],
        'character': r['Character'],
    })

with open('audit-hachiroku14-hashi-wrong.json', 'w', encoding='utf-8') as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)
    f.write('\n')

# ---- TOML block (raw text: literal \n written as \\n) ----
lines = ['```toml']
for e in entries:
    v = e['fix'].replace('\\', '\\\\').replace('"', '\\"')
    # fix holds literal backslash+n (2 chars); in TOML basic string write it as \\n
    # the .replace('\\','\\\\') above already doubles the backslash -> raw text has \\n
    lines.append('"%s" = "%s"' % (e['key'], v))
lines.append('```')
block = '\n'.join(lines)
with open('audit-hachiroku14-hashi-tomlblock.txt', 'w', encoding='utf-8') as f:
    f.write(block + '\n')

# ---- mechanical verification ----
loaded = json.load(open('audit-hachiroku14-hashi-wrong.json', encoding='utf-8'))
assert len(loaded) == 59
assert all(isinstance(e['key'], str) for e in loaded)
# TOML parse of the block
inner = block[len('```toml\n'):-len('\n```')]
parsed = tomllib.loads(inner)
assert len(parsed) == 59, len(parsed)
mism = 0
for e in loaded:
    pv = parsed[e['key']]
    if pv != e['fix']:
        mism += 1
        print('VALUE MISMATCH', e['key'], repr(pv), '||', repr(e['fix']))
print('toml value mismatches:', mism)
# jp/tw/old_vn vs CSV3
bad = 0
for e in loaded:
    r = rows[e['key']]
    if e['jp'] != r['JP Original'] or e['tw'] != r['TW Original/Current'] or e['old_vn'] != r['Vietnamese']:
        bad += 1
        print('CSV3 MISMATCH', e['key'])
print('csv3 mismatches:', bad)
# diff-sanity: each fix differs from old only in targeted change — show unified diffs
for e in loaded:
    if e['fix'] == e['old_vn']:
        print('NO-OP FIX!', e['key'])
print('kinds:', {k: sum(1 for e in loaded if e['kind'] == k) for k in set(KIND.values())})
print('OK')
