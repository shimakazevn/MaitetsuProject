import csv, json, tomllib, difflib

BS = chr(92)
CSV='sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv'
TARGET='日々姫10_稀咲の未来図、日々姫の未来図.txt.toml'
rows={}
with open(CSV, encoding='utf-8-sig', newline='') as f:
    for row in csv.DictReader(f):
        if row['File'].split(chr(92))[-1]==TARGET:
            rows[row['Key']]=row

# Each fix is built by replacing ONE substring of the CSV3 old_vn (or a whole short
# single-line value) so the row's own line-break convention is preserved byte-for-byte.
# (old_fragment, new_fragment) pairs, hand-decided from the JP read.
REPL=[
 ("2437", "fabrication",   ("Chắc chắn rồi, cảm ơn cô rất nhiều.", "Không, không, cảm ơn cô rất nhiều.")),
 ("2581", "style",         ("tán thành tuyệt đối. Ạ.", "tán thành tuyệt đối ạ.")),
 ("2602", "style",         (". Ạ!", " ạ!")),
 ("2647", "meaning",       ("Chắc…… vậy thôi.", "Ừ…… đúng vậy.")),
 ("2691", "pronoun",       ("tôi mượn điện thoại", "anh mượn điện thoại")),
 ("2720", "omission",      ("còn đây là bộ điều khiển trung tâm.", "còn đây là thiết bị lái tích hợp.")),
 ("2781", "tag",           (None, None)),  # special: move the line break out of the %l tag
 ("2847", "pronoun",       ("chị biết rồi?", "mình biết rồi?")),
 ("2888", "meaning",       ("Reina, lại đây nào.", "Reina, được chứ?")),
 ("2920", "style",         (None, None)),  # special: two spots in one row
 ("2925", "pronoun",       ("Anh thử gọi điện xem sao?", "Ngài thử gọi điện xem sao?")),
 ("2940", "gasp",          ("「!」", "「Ư!」")),
 ("2943", "transliteration",("Sa bàn En-nu?", "Sa bàn N?")),
 ("3390", "gasp",          ("không——!!?", "không——Ư!!?")),
 ("3620", "meaning",       ("phá lên cười.", "nhoẻn miệng cười.")),
 ("3666", "meaning",       ("đã từ bỏ việc dùng kính ngữ \"cô\",", "đã thôi gọi Kisaki bằng kính ngữ,")),
]
out=[]
for key, kind, (old_f, new_f) in REPL:
    r=rows[key]
    old=r['Vietnamese']
    if key=="2781":
        # CSV3 old_vn has %l; + backslash-run + n + #;  (line break INSIDE the tag).
        # Move the break to after #;, keeping the row's exact backslash run.
        idx = old.find('%l;')
        fix = None
        while idx != -1:
            j = idx + 3
            while j < len(old) and old[j] == BS:
                j += 1
            if old[j:j+3] == 'n#;':
                bs_run = old[idx+3:j]
                fix = old[:idx] + '%l;#;' + bs_run + 'n' + old[j+3:]
                break
            idx = old.find('%l;', idx + 3)
        assert fix is not None, old
    elif key=="2920":
        assert "Mô hình đô thị này cũng đẹp. Thật ạ. Nhưng!" in old
        assert "còn đẹp hơn nhiều. Lắm ạ!" in old
        fix=old.replace("Mô hình đô thị này cũng đẹp. Thật ạ. Nhưng!",
                        "Mô hình đô thị này cũng đẹp thật ạ. Nhưng!", 1)
        fix=fix.replace("còn đẹp hơn nhiều. Lắm ạ!", "còn đẹp hơn nhiều ạ!", 1)
    elif key=="2581":
        assert old_f in old, old
        fix=old.replace(old_f, new_f, 1).replace("Ừm……tán thành", "Ừm…… tán thành", 1)
    else:
        assert old_f in old, (key, old)
        fix=old.replace(old_f, new_f, 1)
    out.append({"key": key, "jp": r['JP Original'], "tw": r['TW Original/Current'],
                "old_vn": old, "fix": fix, "kind": kind, "character": r['Character']})
with open('audit-hibiki10-miraizu-wrong.json','w',encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
    f.write('\n')
print("json entries:", len(out))
print("fixes containing real newline:", [e['key'] for e in out if chr(10) in e['fix']])

lines=[]
for e in out:
    v=e['fix'].replace(BS, BS+BS).replace('"', BS+'"')
    lines.append('"%s" = "%s"' % (e['key'], v))
block='[script]\n'+'\n'.join(lines)+'\n'
parsed=tomllib.loads(block)
assert len(parsed['script'])==len(out)
mism=[e['key'] for e in out if parsed['script'][e['key']]!=e['fix']]
print("toml keys:", len(parsed['script']), "value mismatches vs JSON:", mism)
with open('audit-hibiki10-miraizu-tomlblock.txt','w',encoding='utf-8') as f:
    f.write(block)

for e in out:
    sm=difflib.SequenceMatcher(None, e['old_vn'], e['fix'])
    ops=[o for o in sm.get_opcodes() if o[0]!='equal']
    print(e['key'], e['kind'], 'changed-blocks:', len(ops), '|', ' / '.join('%s:%r->%r'%(t, e['old_vn'][i1:i2][:32], e['fix'][j1:j2][:32]) for t,i1,i2,j1,j2 in ops))
