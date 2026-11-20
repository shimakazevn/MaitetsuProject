import tomllib, csv, json, re

TOML = 'sources/toml2/translation_toml/09_Grand/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c811_#U30ca#U30a4#U30f3#U30b9#U30bf#U30fc#U30ba#Uff01.txt.toml'
CSV3 = 'sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv'
TARGET = 'グランドリライト11_ナインスターズ！.txt.toml'

raw = open(TOML, encoding='utf-8-sig').read()
d = tomllib.loads(raw)
script = d.get('script', {})
print('script rows:', len(script))
print('info:', d.get('info'))
print('selections:', d.get('selections'))
print('characters keys:', list(d.get('characters', {}).keys()))

# JP comments above each script line
jp_comments = {}
lines = raw.splitlines()
cur_jp = None
for ln in lines:
    m = re.match(r'\s*# JP:\s*(.*)', ln)
    if m:
        cur_jp = m.group(1)
        continue
    m2 = re.match(r'\s*"(\d+)"\s*=', ln)
    if m2 and cur_jp is not None:
        jp_comments[m2.group(1)] = cur_jp
        cur_jp = None
print('jp comments captured:', len(jp_comments))

# CSV3 rows for this file
rows = []
with open(CSV3, encoding='utf-8-sig', newline='') as f:
    r = csv.DictReader(f)
    print('csv cols:', r.fieldnames)
    for row in r:
        fn = row['File'].split(chr(92))[-1]
        if fn == TARGET:
            rows.append(row)
print('csv3 rows for file:', len(rows))
# check duplicate keys in csv3 set
keys = [row['Key'] for row in rows]
print('unique csv keys:', len(set(keys)))
# check sections
from collections import Counter
print('sections:', Counter(row['Section'] for row in rows))
print('characters:', Counter(row['Character'] for row in rows))

# compare TOML VN vs CSV3 VN
mismatch = []
for row in rows:
    k = row['Key']
    tv = script.get(k)
    if tv is None:
        mismatch.append((k, 'MISSING IN TOML'))
    elif tv != row['Vietnamese']:
        mismatch.append((k, 'VN differs TOML vs CSV3'))
print('toml-vs-csv3 mismatches:', len(mismatch))
for m in mismatch[:20]: print(m)
toml_only = [k for k in script if k not in set(keys)]
print('keys in TOML not in CSV3:', toml_only)

# write combined dump for reading
with open('audit-grand11-nine-stars-dump.txt', 'w', encoding='utf-8') as out:
    for row in rows:
        k = row['Key']
        out.write(f"=== KEY {k} | Sec:{row['Section']} | Char:{row['Character']} | Disp:{row['DisplayAs']}\n")
        out.write(f"JP: {row['JP Original']}\n")
        out.write(f"TW: {row['TW Original/Current']}\n")
        out.write(f"VN(csv3): {row['Vietnamese']}\n")
        tv = script.get(k, '<MISSING>')
        if tv != row['Vietnamese']:
            out.write(f"VN(toml): {tv}\n")
        jp_c = jp_comments.get(k)
        if jp_c is not None and jp_c != row['JP Original']:
            out.write(f"JP(comment): {jp_c}\n")
        out.write("\n")
print('dump written')
