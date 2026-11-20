# -*- coding: utf-8 -*-
"""Build audit-grand11-nine-stars-wrong.json + TOML block from hand-written fixes.
Fix values are hand-written from reading each row's JP (+TW). They are built
as full strings (literal backslash-n where CSV3 has line breaks) and verified:
- jp/tw/old_vn == CSV3 exactly for every entry
- TOML block parses (tomllib), key count == JSON count, 0 value mismatches
- difflib: each fix differs from old VN only in the targeted change (printed for 2nd pass)
"""
import csv, json, tomllib, difflib

CSV3 = 'sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv'
T = 'グランドリライト11_ナインスターズ！.txt.toml'

# key -> (fix, kind) ; fix uses literal backslash-n (written \\n in this source)
FIXES = {
 # meaning: sync direction reversed (KiHa 07 must follow 8620, not vice versa)
 "2619": ("「Đúng vậy ạ. Do đó, KiHa 07 phải liên động theo thao tác điều khiển của xe đi trước——lần này là 8620 ạ.」", "meaning"),
 # sweep gasp (whole-line っ), adopted verbatim from sweep-raw-gasp-wrong.json
 "2315": ("「Ư!」", "sweep"),
 "2317": ("「Ư!!」", "sweep"),
 "2318": ("「Ư!!!」", "sweep"),
 "2355": ("「Ư!!?」", "sweep"),
 # pronoun: Soutetsu "anh" -> "tôi" with Hachiroku (2118 confirms addressee)
 "2574": ("「Vậy sao——tốt quá. Vui lắm, sao.\\nTôi, nếu vậy thì……tôi, cuối cùng cũng——」", "pronoun"),
 # pronoun: group address (みんな / 全員) -> "tôi" (Paulette 14:1544 precedent)
 "2428": ("「Nếu được, tôi có chuyện muốn bàn với mọi người.」", "pronoun"),
 "2104": ("「Xin lỗi nhưng chuyện của Kisaki để sau đi.\\nChuyện của tôi là chuyện muốn hỏi ý kiến của tất cả mọi người.」", "pronoun"),
 # pronoun: Kisaki cluster — Soutetsu "tôi" with Kisaki (brief rule; Common 14, Grand 01, lr_稀咲h1)
 "2347": ("「Gì chứ,\\ntôi cứ tưởng hôm nay sẽ được thấy Kisaki mặc đồ du lịch cơ.」", "pronoun"),
 "2173": ("「Chẳng phải cô được mời bởi một người bạn ở Đại lục——\\nTrung Quốc sao?」", "pronoun"),
 # Kisaki self "em" -> "Tôi", Kisaki -> Soutetsu "anh Soutetsu" -> bare "Soutetsu" / "cậu"
 "2459": ("「Với ý nghĩa đó, hôm nay cậu phải lái cho thật tốt đấy nhé? Soutetsu.」", "pronoun"),
 "2617": ("「Vừa hay. Tôi cũng có chuyện muốn bàn bạc.\\nNói vậy chứ, trước tiên tôi muốn nói chuyện với Soutetsu và Paulette.」", "pronoun"),
 "1664": ("「……Tóm lại, ý tưởng của Soutetsu là.」", "pronoun"),
 "2514": ("「Tôi chỉ là người đi cùng thôi mà.\\nHay nói đúng hơn……nói thẳng ra là đối tác làm ăn?」", "pronoun"),
 "2142": ("「Không phải bạn tôi. Là con gái của bạn cũ bố tôi.」", "pronoun"),
 "2531": ("「Tiếc là lần này tôi không có thời gian để tận hưởng chuyến đi.\\nNhưng cô ấy đi vì công việc. Chắc chắn cô ấy sẽ dốc toàn lực để tận hưởng chuyến đi này.」", "pronoun"),
 "2599": ("「Tôi nghĩ là có khả năng đó. Mà với tính cách của cô ấy,\\nít nhất thì tôi——『Chỉ cảm thấy có khả năng đó thôi』.」", "pronoun"),
 "2846": ("「Vậy thì, trong khi đặt niềm tin tối đa vào mọi người,\\ntôi sẽ đi cố gắng hoàn thành công việc của mình đây.」", "pronoun"),
 "2508": ("「Tôi cũng chỉ đi cùng đến Yatsushiro thôi.\\nDù sao thì, mọi người cũng có một chuyến đi vui vẻ nhé!」", "pronoun"),
 "2681": ("「Cái này thì——tôi đã quá nóng vội rồi.」", "pronoun"),
 # term: 運転体 "thân chính" -> "thân vận hành" (Common 15: 1516/2619/2938)
 "3300": ("Tôi bế Hachiroku, người đã nhanh chóng thay sang \\x%l運転体;#00ffc040;thân vận hành%l;#; trong lúc tôi giải thích,\\nlên đùi như mọi khi.", "term"),
 # term: タブレット "thẻ bảng" -> "máy tính bảng" (Common 15: 2619; Paulette 04 stove)
 "3554": ("Và \\x%lタブレット;#00ffc040;máy tính bảng%l;#; mô phỏng đồ của \\x%lレイルロオド;#00ffc040;Railord%l;#;——\\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \\x%l運転士;#00ffc040;lái tàu%l;#; Akai.", "term"),
 # term: ISC expansion — game itself spells "International Spirits Competition" (真闇01 1558)
 "3242": ("Việc nếm thử và bán loại rượu đoạt giải cao nhất tại ISC (International Spirits Competition) ngay trên tàu\\nlà một trong những điểm nhấn lớn của chuyến tàu Nine Stars số 1 khởi hành hôm nay.", "term"),
 # added: VN adds vocative "Ngài Soutetsu." with no JP/TW basis
 "2462": ("「Dù không nhìn thấy, nhưng mồ hôi đổ ra sẽ khô lại trên bề mặt cơ thể.\\nNó sẽ tạo ra mùi cơ thể thoang thoảng, gây khó chịu cho những người xung quanh.」", "added"),
 # added-tag: VN adds a %l gloss tag JP does not have (JP has only ruby [かいさつきょう,2])
 "2416": ("「Chắc là em ấy thấy vui khi bấm vé.\\nMỗi lần cầm kìm soát vé bấm lách cách, trông em ấy cứ như——」", "added-tag"),
 # sfx: （ぽっ！） pop, not a beep — TW 啵
 "3972": ("（Bộp!）", "sfx"),
}

rows = {}
with open(CSV3, encoding='utf-8-sig', newline='') as f:
    for r in csv.DictReader(f):
        if r['File'].split(chr(92))[-1] == T:
            rows[r['Key']] = r
print('csv rows:', len(rows))

# sweep cross-check: our 4 sweep fixes must match sweep file verbatim
sweep = json.load(open('sweep-raw-gasp-wrong.json', encoding='utf-8'))
smap = {e['key']: e for e in sweep if e.get('file','').endswith(T)}
for k in ('2315','2317','2318','2355'):
    assert k in smap, f'sweep entry missing {k}'
    assert FIXES[k][0] == smap[k]['fix'], f'sweep fix mismatch {k}'
    assert smap[k]['old_vn'] == rows[k]['Vietnamese'], f'sweep old_vn mismatch {k}'
print('sweep 4/4 match verbatim')

# GUARD: dialogue brackets must match old_vn exactly
for k, (fix, kind) in FIXES.items():
    old = rows[k]['Vietnamese']
    assert (fix.startswith('「')) == (old.startswith('「')), f'bracket open mismatch {k}'
    assert (fix.endswith('」')) == (old.endswith('」')), f'bracket close mismatch {k}'

items = []
for k in sorted(FIXES, key=int):
    fix, kind = FIXES[k]
    r = rows[k]
    items.append({
        "key": k,
        "jp": r['JP Original'],
        "tw": r['TW Original/Current'],
        "old_vn": r['Vietnamese'],
        "fix": fix,
        "kind": kind,
        "character": r['Character'],
    })

with open('audit-grand11-nine-stars-wrong.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('json entries:', len(items))

# TOML block
def toml_escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')
lines = ['[script]']
for it in items:
    lines.append(f"{it['key']} = \"{toml_escape(it['fix'])}\"")
block = '\n'.join(lines) + '\n'
with open('audit-grand11-nine-stars-tomlblock.txt', 'w', encoding='utf-8') as f:
    f.write('```toml\n' + block + '```\n')

# parse-check
d = tomllib.loads(block)
script = d['script']
assert len(script) == len(items), f'key count {len(script)} != {len(items)}'
mism = 0
for it in items:
    v = script[it['key']]
    if v != it['fix']:
        mism += 1
        print('VALUE MISMATCH', it['key'], repr(v), '!=', repr(it['fix']))
print('toml keys:', len(script), 'value mismatches:', mism)

# diff-sanity print (second-pass reading material)
print('\n=== DIFF old_vn -> fix (2nd pass) ===')
for it in items:
    old, fix = it['old_vn'], it['fix']
    sm = difflib.SequenceMatcher(None, old, fix, autojunk=False)
    ops = [o for o in sm.get_opcodes() if o[0] != 'equal']
    desc = '; '.join(f"{tag} old[{a1}:{a2}]={old[a1:a2]!r} -> fix[{b1}:{b2}]={fix[b1:b2]!r}" for tag,a1,a2,b1,b2 in ops)
    print(f"{it['key']} [{it['kind']}] {desc}")
    print(f"    JP: {it['jp'].replace(chr(92)+'n',' / ')[:150]}")
