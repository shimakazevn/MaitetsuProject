# Build audit deliverables for 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml
# Fix values are HAND-WRITTEN from reading each row's JP (+TW). The script only
# applies the hand-written substring replacements to the CSV3 old_vn (authoritative)
# and assembles/verifies the JSON + TOML block. No bulk fixing.
import csv, json, tomllib

FNAME = "日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml"
TOML = ("sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh6_#U30aa#U30ea#U30a8#U30f3"
        "#U30c6#U30fc#U30ea#U30f3#U30b0#U501f#U308a#U7269#U7af6#U8d70#Uff08#U30da#U30a2#Uff09.txt.toml")
CSV3 = "sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv"

# key -> (kind, [(old_sub, new_sub), ...]) — hand-written replacements
FIXES = {
 "1418": ("gasp", [("「――」", "「――Ư」")]),
 "1426": ("moan", [("phù! A!", "Fua! A!"), ("em, mất", "em, hi")]),
 "1427": ("gasp", [("「――!」", "「Ư――!」")]),
 "1985": ("thuật ngữ", [("Cơ thể bảo trì", "Thân bảo trì")]),
 "2015": ("sai nghĩa", [("đỉnh hay không", "buồn cười hay không")]),
 "2028": ("moan", [("không chạm tới được――ấy", "không chạm tới được――anh…")]),
 "2075": ("moan", [("Kyafuuuuun", "Kyaf" + "u"*7 + "n"), ("mở rộng ra――phù", "mở rộng ra――Fua")]),
 "2077": ("moan", [("phù――a! A! Aaaaa", "Fua――a! A! Aaaa")]),
 "2078": ("nguyên âm", [("Fuuuuuuuuuuuuuun", "Fuuuuuuuuuuuuun")]),
 "2080": ("nguyên âm", [("Hyaa!", "Hya!")]),
 "2084": ("moan", [("em――phù!", "em――Fua!")]),
 "2085": ("moan", [("「A! Chim kìa!", "「Yaa! Chim kìa!")]),
 "2102": ("moan", [("phù, a――", "Fua, a――")]),
 "2109": ("nguyên âm", [("fuuuuuu!!!", "fuuuuuuu!!!")]),
 "2111": ("moan", [("Phù――a,", "Fua――a,")]),
 "2112": ("moan", [("「Phù a」", "「Fua」")]),
 "2114": ("moan", [("Fuaaaaaa――", "Faaaaaaa――")]),
 "2116": ("moan", [("Phù!? A!", "Fua!? A!")]),
 "2117": ("moan", [("Fuan!!!", "Fan!!!")]),
 "2122": ("moan", [("Phù! A! Sướng", "Fa! A! Sướng")]),
 "2124": ("moan", [("Phù! A! Bắn", "Fua! A! Bắn")]),
 "2138": ("moan", [("phù a!", "Fua!")]),
 "2182": ("moan", [("A――phù――a――", "A――Fua――a――")]),
 "2184": ("moan", [("phù――\\nTo quá", "Fua――\\nTo quá")]),
 "2185": ("gasp", [("Ưm ưm~~!", "Ưm ưm ưm~~Ư!")]),
 "2190": ("nguyên âm", [("A――ưm――Thế,", "Aa――ưm――Thế,")]),
 "2196": ("nguyên âm", [("Fuyaaaaaaaaaan", "Fuy" + "a"*11 + "n")]),
 "2199": ("nguyên âm", [("Aaaaa――a!", "Aaaa――a!")]),
 "2201": ("gasp", [("「!!!」", "「ƯƯƯ!!!」")]),
 "2202": ("nguyên âm", [("「Aaaaa!」", "「Aaaaaa!」")]),
 "2203": ("nguyên âm", [("「Aaaaa!」", "「Aaaa!」")]),
 "2210": ("moan", [("Thở――khó――thở quá――phù, a!", "Thở――thở――khó thở quá――Fua, a!")]),
 "2241": ("gasp", [("A――ư ư ư~~", "A――ư ư ư~~Ư")]),
 "2266": ("moan", [("Kuuunnnn!", "KuunnnnnƯƯƯƯ!")]),
 "2282": ("gasp", [("Ưm――ư~~", "Ưm――ư~~Ư")]),
 "2297": ("moan", [("Phù! A! A――", "Pua! A! A――"), ("phù――a――", "Fua――a――")]),
 "2298": ("moan", [("Phù! Cảm ơn", "Puha! Cảm ơn")]),
 "2362": ("sai nghĩa", [("『Đỉnh thật!", "『Buồn cười thật!")]),
 "2364": ("moan", [("Ưm――phù! A――", "Ưm――Fua! A――")]),
 "2457": ("sai nghĩa", [("Vận động……thả lỏng", "Thả lỏng……vận động")]),
 "2709": ("moan", [("rồi――phù――a", "rồi――Fua――a")]),
 "2711": ("moan", [("Phù a――a――", "Fua――a――")]),
 "2713": ("nguyên âm", [("kuuu~~n", "kuuuu~~n")]),
 "2751": ("moan", [("Chim――phù――", "Chim――Fua――")]),
 "2759": ("gasp", [("「!」", "「Ư!」")]),
 "2761": ("gasp", [("「!!?」", "「Ư!!?」")]),
 "2764": ("gasp", [("~~~~~!! Kua!", "~~~~~ƯƯ!! Kua!")]),
 "2767": ("gasp", [("~~~~~~~~~~~~!!!!", "~~~~~~~~~~~~ƯƯ!!!!")]),
 "2982": ("gasp", [("mở ra――!!?", "mở ra――Ư!!?")]),
 "3414": ("gasp", [("toàn bộ――!", "toàn bộ――Ư!")]),
 "3421": ("gasp", [("tới trước――!!?", "tới trước――Ư!!?")]),
}

rows = {}
with open(CSV3, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r['File'].split(chr(92))[-1] == FNAME:
            rows[r['Key']] = r

d = tomllib.loads(open(TOML, 'rb').read().decode('utf-8-sig'))
assert len(rows) == 667 and len(d['script']) == 667

out = []
for key in sorted(FIXES, key=int):
    kind, reps = FIXES[key]
    r = rows[key]
    old_vn = r['Vietnamese']
    fix = old_vn
    for old_sub, new_sub in reps:
        assert fix.count(old_sub) == 1, f"key {key}: sub {old_sub!r} count={fix.count(old_sub)}"
        fix = fix.replace(old_sub, new_sub)
    assert fix != old_vn, f"key {key}: fix == old_vn"
    out.append({"key": key, "jp": r['JP Original'], "tw": r['TW Original/Current'],
                "old_vn": old_vn, "fix": fix, "kind": kind, "character": r['Character']})

print("fix count:", len(out))
# sanity: vowel counts for the tricky romaji tokens (from CSV3 data, not re-typed)
def count_u(s): return s.count('u') + s.count('U')
def count_a(s): return s.count('a') + s.count('A')
checks = {
 "2078": ("Fuuuuuuuuuuuuun", 13, 'u'),
 "2109": ("fuuuuuuu", 7, 'u'),
 "2114": ("Faaaaaaa", 7, 'a'),
 "2196": ("Fuy" + "a"*11 + "n", 11, 'a'),
 "2075": ("Kyaf" + "u"*7 + "n", 7, 'u'),
 "2266": ("Kuunnnnn", 2, 'u'),
}
for k, (tok, n, which) in checks.items():
    got = (count_u(tok) if which == 'u' else count_a(tok))
    entry = next(e for e in out if e['key'] == k)
    assert tok in entry['fix'], f"{k}: token {tok!r} not in fix {entry['fix']!r}"
    assert got == n, f"{k}: token has {got} {which}, expected {n}"
print("romaji token counts OK")
with open("audit-hibikih6-orienteering-karimono-wrong.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

# TOML block (json.dumps escaping is valid TOML basic-string escaping here)
lines = ["[script]"]
for e in out:
    lines.append(f"{e['key']} = {json.dumps(e['fix'], ensure_ascii=False)}")
block = "\n".join(lines) + "\n"
with open("audit-hibikih6-orienteering-karimono-tomlblock.txt", "w", encoding="utf-8") as f:
    f.write(block)
# verify block parses and matches JSON exactly
parsed = tomllib.loads(block)
assert set(parsed['script']) == {e['key'] for e in out}, "block key set mismatch"
mism = [(e['key']) for e in out if parsed['script'][e['key']] != e['fix']]
assert not mism, f"value mismatches: {mism}"
print("TOML block OK:", len(parsed['script']), "keys, 0 mismatches")
# verify jp/tw/old_vn match CSV3 exactly
for e in out:
    r = rows[e['key']]
    assert e['jp'] == r['JP Original'] and e['tw'] == r['TW Original/Current'] and e['old_vn'] == r['Vietnamese'], e['key']
print("jp/tw/old_vn match CSV3 exactly:", len(out), "/", len(out))
# verify old_vn matches TOML (modulo \n flattening)
flat_mism = []
for e in out:
    tv = d['script'][e['key']]
    if tv != e['old_vn'] and tv != e['old_vn'].replace('\\n', ' '):
        flat_mism.append(e['key'])
assert not flat_mism, f"TOML VN mismatches: {flat_mism}"
print("old_vn matches TOML-2 (modulo \\n flattening):", len(out), "/", len(out))
# diff-sanity: each fix differs from old_vn only in the targeted substrings
for e in out:
    kind, reps = FIXES[e['key']]
    tmp = e['old_vn']
    for old_sub, new_sub in reps:
        tmp = tmp.replace(old_sub, new_sub, 1)
    assert tmp == e['fix'], f"diff-sanity failed key {e['key']}"
print("diff-sanity OK: every fix differs from old_vn only in the targeted change")
