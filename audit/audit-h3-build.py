# -*- coding: utf-8 -*-
"""Build audit deliverables for lr_ハチロクh3_通販失敗いたしましたにゃん.
Fix values are HAND-WRITTEN below (read against JP+TW row by row).
CSV3 supplies jp/tw/old_vn/character mechanically; script only assembles
and verifies: old_vn match, TOML parse, key count, value match, diff-sanity.
Fix values are SINGLE-LINE (space where old VN had a literal \\n).
"""
import json, tomllib, pathlib

BASE = pathlib.Path('/home/hatch/workspace/maitetsu-pilot')
rows = json.load(open(BASE/'audit-h3-work-csv.json', encoding='utf-8'))
bykey = {r['Key']: r for r in rows}

# (key, fix, kind, reason) — fix hand-written; jp/tw/old_vn/character from CSV3.
F = []
def add(key, fix, kind, reason):
    F.append((str(key), fix, kind, reason))

PR = 'pronoun'
# --- A. Pronoun: Soutetsu "anh" -> "tôi" with Hachiroku (16 rows) ---
add(1112, "「Không! Ý tôi là trạng thái Suzu đang mặc cơ! Thế nên, tôi định mua lại và tặng nó cho Suzu」", PR, "Soutetsu nói với Hachiroku (cả file chỉ có 2 người) — tự xưng phải là 'tôi' theo quy tắc đã sửa; 'anh' chỉ với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi.")
add(1140, "「Em đã để ý đến kích cỡ sao? Bộ đồ lót mà tôi khen lúc mọi người cùng xem tạp chí…」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1155, "「Vậy sao, nó rất giống bộ đồ lót mà tôi đã khen 'Thứ này cũng tuyệt nhỉ'. Chỉ có một điểm——không, hai điểm chăng」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1156, "「Ra vậy. Tôi hiểu lý do em ở trong bộ dạng đó rồi」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1176, "「Chỉ liếm nhũ hoa của tôi, chỉ sóc lọ sự cương cứng của tôi mà đã ướt sũng đến mức này sao?」", PR, "Soutetsu với Hachiroku → 'tôi' (2 lần 'của anh').")
add(1182, "「Tôi không muốn làm em hỏng đâu」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1212, "「Chờ, chờ đã——Suzu! Thế này thì—— Không ổn đâu——tôi, sắp——」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1294, "「Này này, tôi mặc vào thì làm được gì chứ」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1336, "「Nếu trả lại thì tôi sẽ mua lại」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1370, "「Chờ chút, Su, zu——Suzu, Suzu. Thay đổi tư thế nào. Tôi, muốn đạt cực khoái——ở nơi——sâu nhất, của em」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1376, "「Tôi tất nhiên là biết rồi. Vì tôi hiểu rất rõ cơ thể của Suzu mà」", PR, "Soutetsu với Hachiroku → 'tôi' (2 lần).")
add(1390, "「Vậy, rốt cuộc em muốn hỏi tôi chuyện gì?」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1408, "「Không sao đâu. Cho dù là câu hỏi gì đi nữa thì cứ yên tâm. Tôi luôn đứng về phía em. Hãy kể cho tôi nghe mọi chuyện, đừng sợ hãi」", PR, "Soutetsu với Hachiroku → 'tôi' (2 lần).")
add(1420, "「Lý do tôi cương cứng thì đã rõ ràng rồi. Là vì Suzu quá đỗi đáng yêu, quá đỗi yêu kiều và xinh đẹp」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1427, "「Em đã ướt át đến mức này rồi. Đã sẵn sàng rồi. Đã chuẩn bị hoàn tất để tiếp nhận sự cương cứng của tôi rồi」", PR, "Soutetsu với Hachiroku → 'tôi'.")
add(1460, "「Nếu vậy, tôi sẽ làm nhiều hơn nữa」", PR, "Soutetsu với Hachiroku → 'tôi'.")

GA = 'gasp'
# --- B. Gasp: sweep values adopted verbatim after verification vs JP (15 rows) ---
add(1203, "「Ư!」", GA, "Sweep raw-tsu: JP 「っ！」 toàn dòng là gasp; VN còn っ thô → Ư.")
add(1204, "「Ư!!!!!」", GA, "Sweep raw-tsu: JP 「っ！！！！！」 → Ư.")
add(1206, "「ƯƯ!!!? Khoan——au!!」", GA, "Sweep raw-tsu: JP 「っっ！！！？」 → ƯƯ; nửa sau 'Khoan——au!!' giữ (まっ―― đã diễn bằng gạch, あうっ giữ theo quy ước SFX La-tinh).")
add(1207, "「Ư!?」", GA, "Sweep lost-gasp-whole: JP 「っ！？」 toàn dòng gasp, VN chỉ còn dấu câu → thêm Ư.")
add(1248, "「Ư!!!!!!」", GA, "Sweep raw-tsu.")
add(1249, "「Ư!!!?」", GA, "Sweep raw-tsu.")
add(1264, "「A——a——Ư————. Kuha!」", GA, "Sweep raw-tsu: っ sau 'A——a——' bị mất trong VN → Ư; 'Kuha!' giữ (くはっ, quy ước La-tinh).")
add(1273, "「Ư!!!?」", GA, "Sweep raw-tsu.")
add(1331, "「Giống như đài phun nước nya! Thú vị quá nya~Ư!!」", GA, "Sweep lost-gasp-trailing: JP 'にゃ～っ！！' — っ cuối sau ~ bị mất → thêm Ư.")
add(1378, "「Em——cô bé——a hỏng mất—— mất thôi——hyagu——ngài Soutetsu——của——Ư!」", GA, "Sweep lost-gasp-trailing: JP kết 'のっ――っ！' — っ cuối sau ―― bị mất hoàn toàn → thêm Ư.")
add(1385, "「Ư~~~~~~~Ư!!!!」", GA, "Sweep raw-tsu: JP 「っ～～～～～～～っ！！！！」 hai っ thô → Ư…Ư.")
add(1494, "「~~~~Ư!!」", GA, "Sweep lost-gasp-trailing: JP '～～～～っ！！' — っ sau ~ bị mất → thêm Ư.")
add(1497, "「~~~~~~~~~~~~~~~~Ư!!!!」", GA, "Sweep lost-gasp-trailing: như 1494.")
add(1642, "Sự cương cứng đang xuất tinh lại tiếp tục bị những ngón tay của Suzu đùa giỡn——Ư!!!!", GA, "Sweep lost-gasp-trailing: JP '弄びっ――っ！！！！' — っ thứ hai sau ―― là gasp đứng riêng, VN mất hẳn → thêm Ư.")
add(1757, "Đã phản ứng lại. Cả trái tim và cơ thể dốc toàn lực. Sự tấn công bất ngờ, quá đỗi đáng yêu——Ư!?", GA, "Sweep lost-gasp-trailing: JP '可愛らし――っ！？' — っ sau ―― bị mất → thêm Ư.")

SX = 'sfx'
# --- C. Laughter: giggles rendered as gasps (4 rows) ---
add(1236, "「Fufu」", SX, "JP 「ふふっ」 (TW 哈哈) là tiếng cười, VN 'Hừ hừ' lệch sắc thái (nghe như hừ giọng/khinh khỉnh) → 'Fufu' theo tiền lệ 2760 (ふふ→'fufu').")
add(1297, "「Nyafufu~~」", SX, "JP 「にゃふふ～～」 (TW 喵呵呵) là tiếng cười mèo; 'hừ hừ' sai như 1236 → 'Nyafufu~~'.")
add(1318, "「Nfufu. Ngài Soutetsu bé bỏng nũng nịu đáng yêu quá đi. Suzu sẽ yêu thương ngài nhiều thật nhiều nha nya」", SX, "JP 「んふふっ」 là tiếng cười; VN 'Ư hừ hừ' diễn cười thành rên (sai quy tắc 22:05, tiền lệ file 05) → 'Nfufu' (ん=n).")
add(1320, "「Ufufu, đúng vậy nhỉ」", SX, "JP 「うふふっ」 là tiếng cười; VN 'Ư hừ hừ' diễn cười thành rên → 'Ufufu' (tiền lệ 1840, file 05).")

MO = 'moan'
# --- D. fa/fu romaji fallback (Hepburn; ふぁ->Fa, ふあ->Fua, ふにゃ->Funya, ふか->Fuka) (18 rows) ---
add(1201, "「Hyau!? Fua——ngực——nhũ hoa—— của ngài Soutetsu——ưm——ngón tay——ngón tay」", MO, "JP ふあっ――: 'Hua' sai phụ âm (ふ=f, không phải h) → romaji 'Fua' (tiền lệ moan-fix h7: ふあっ→'Fua').")
add(1218, "「Fa——a——a——nhiều quá, nhiều quá—— nhiều quá——em——ngài Soutetsu——ưm!」", MO, "JP ふぁっ―― (ぁ nhỏ = 1 âm 'fa'): 'Hua' sai phụ âm → romaji 'Fa' (tiền lệ moan-fix h7: ふぁっ→'Fa').")
add(1219, "「Fa——ha——a——sướng——quá——ạ—— Ưm——ngực——nhũ hoa cũng——cô bé, cũng」", MO, "JP ふぁっ――: 'Hua' sai phụ âm → 'Fa'; は→'ha' đúng giữ nguyên.")
add(1220, "「Fa——a……a……a……—— Ưm……chụt——ực——pua」", MO, "JP ふぁ――: 'Hua' sai phụ âm → 'Fa'; ぷぁ→'pua' đúng giữ nguyên.")
add(1222, "「Fua——a——a——n a! Ngài Soutetsu——ngài Soutetsu!」", MO, "JP ふあっ――: 'Haa' sai phụ âm (thiếu f, sai nguyên âm) → 'Fua'.")
add(1223, "「Fua! A! A! A! A! A! A! A!!」", MO, "JP ふあっ！: 'Hua' sai phụ âm → 'Fua'.")
add(1224, "「Fua!!!!!」", MO, "JP ふあっっっっ！！！！！: 'Haaaa' sai phụ âm → 'Fua'; っ×4 là nhấn mạnh, dấu !!!!! giữ nhấn (tiền lệ h7: っ cuối rơi, dấu câu giữ nhấn).")
add(1225, "「Funyaaaaaan——」", MO, "JP ふにゃあああああん―― (6 âm a: にゃ+あ×5, VN cũ đủ 6): 'Hunya' sai phụ âm Kunrei (ふ=hu) → Hepburn 'Funyaaaaaan'.")
add(1227, "「Funyaaaaaan. Sâu quá nya! Nóng quá nya!」", MO, "JP ふにゃああああん (5 âm a: にゃ+あ×4): 'Hunyaaaaaan' sai phụ âm + thừa 1 âm a → 'Funyaaaaaan' (5 a).")
add(1228, "「Funya!!!?」", MO, "JP ふにゃっ！！！？: 'Hunya' sai phụ âm Kunrei → Hepburn 'Funya'.")
add(1229, "「Funyaa~」", MO, "JP ふにゃあ～ (2 âm a): 'Hunyaa' sai phụ âm → 'Funyaa'.")
add(1232, "「Ha——hahu——ưm……Fua—— a——a——a——a——Fa」", MO, "JP ふあっ――→'Fua' ('hua' sai phụ âm); ふぁっ→'Fa' ('hua' sai phụ âm); はひゅっ→'hahu' đúng giữ.")
add(1199, "「Hya! Ưm! Ưm kyu! Fua! Em, Suzu, ha! Suzu! Hết——」", MO, "JP ふあっ！: 'Hua' sai phụ âm → 'Fua'; ひあっ→'Hya' đúng giữ.")
add(1261, "「A……a——Fa——a……aa」", MO, "JP ふぁ――: 'hua' sai phụ âm → 'Fa'; あぁ→'aa' đủ 2 âm giữ.")
add(1262, "「A——Fa——」", MO, "JP ふぁ――: 'ha' sai phụ âm (mất f) → 'Fa'.")
add(1271, "「A! Không——Fa!」", MO, "JP ふぁっ！: 'ha!' sai phụ âm → 'Fa!'.")
add(1266, "「A——a——a——a——Fa——Fuka—— sâu——sâu——nóng——nóng quá——」", MO, "JP ふぁ――→'Fa' ('hua' sai); ふかっ――→'Fuka' ('huka' sai phụ âm); あちゅい→'nóng' đúng giữ.")
add(1348, "「Cô bé——sâu bên trong——a! Fua! A! Bụng——đập vào——nóng quá——phụt, một cái」", MO, "JP ふあっ！: 'Hua' sai phụ âm → 'Fua'.")

# --- E. Vowel counts (formula: VN vowel count = JP vowel-sound count) (3 rows) ---
add(1193, "「Hyaf" + "u"*8 + "n!!!」", MO, "JP ひゃふうううううううんっ: 8 âm u (ふ+う×7); VN cũ 'Hyafuuuuuuuuuun' có 10 u → sửa về 8 u.")
add(1269, "「Aaa——」", MO, "JP ぁぁぁっ――: 3 âm a; VN cũ 'Aaaa' có 4 âm a → sửa về 3.")
add(1432, "「Để một Suzu hư hỏng không hiểu sự đời cũng có thể hiểu được. Hãy trừng phạt thật nhiều, thật nghiêm khắc——nkyuuu!?」", MO, "JP んきゅぅう: 3 âm u (きゅ+ぅ+う); VN cũ 'nkyuu' chỉ 2 u → sửa về 3 u ('nkyuuu').")

# --- F. ちゅう family: vowel length per formula (vowel extension, final 't' iff JP ends っ) (13 rows) ---
add(1277, "「Chụt——chụt——ngoạm——a ưm—— chụt——chụụụt——chụt——chụ~~」", MO, "JP ちゅううっ (3 u) → 'chụụụt' ('chụttttt' sai cơ chế đếm); ちゅ～～ (1 u, không っ) → 'chụ~~' ('chụttttt~~' thừa t + thừa u). Tiền lệ moan-fix h9/paulette-h3 (chụụụt/chuuuu).")
add(1278, "「Chụụt——chụụt——liếm——chụụt——chụt——liếm——chụt——liếm!」", MO, "JP ちゅうっ×3 (mỗi 2 u) → 'chụụt' ×3; VN cũ 'chụt' thiếu 1 u mỗi chỗ; ちゅむっ→'chụt' đúng giữ.")
add(1279, "「Chụt——chụụụ~~——chụt!」", MO, "JP ちゅうう～～ (3 u, không っ) → 'chụụụ~~' ('chụttttt~~' sai đếm + thừa t); ちゅ――→'Chụt' đúng giữ.")
add(1281, "「Chụt——chụt——chụt——liếm—— liếm——chụụt——liếm——liếm」", MO, "JP ちゅうっ (2 u) → 'chụụt'; VN cũ 'chụt' thiếu 1 u.")
add(1283, "「Chụt——chụụt——chụt——chụt—— chụt——liếm——liếm——chụụụ~~」", MO, "JP ちゅうっ (2 u) → 'chụụt'; ちゅうう～～ (3 u, không っ) → 'chụụụ~~'.")
add(1285, "「Chụt——chụụụụụt」", MO, "JP ちゅううううっ (5 u) → 'chụụụụụt' ('chụttttt' chỉ 1 u + lặp t).")
add(1287, "「Chụt! Liếm! Liếm! Chụt! Liếm! Liếm! Chụt! Chụụụụ~」", MO, "JP ぢゅううぅ～ (4 u, không っ) → 'chụụụụ~' ('Chụttttt~' sai đếm + thừa t).")
add(1288, "「Chụt! Chụụt! Chụt! Chụt! Chụụt! Chụt! Chụụt! Chụt!」", MO, "JP ちゅうっ / ちゅるうっ / ちゅうっ (mỗi 2 u) → 'chụụt' ×3; VN cũ 'chụttttt' sai cơ chế.")
add(1289, "「Chụt——chụt——chụụụụụụt」", MO, "JP ちゅうううううっ (6 u) → 'chụụụụụụt' ('chụttttt' sai đếm).")
add(1290, "「Chụt……chụt——chụụụt——chụụt—— chụt——chụụt——chụt——（ngậm lấy）」", MO, "JP ちゅううっ (3 u) → 'chụụụt'; ちゅーっ (2 u) → 'chụụt'; ちゅうっ (2 u) → 'chụụt'; VN cũ 'chụttttt' cả ba chỗ (mất phân biệt độ dài).")
add(1292, "「Chụt——chụt——chụt——chụt—— chụụt——chụụt——chụụt——chụụt」", MO, "JP ちゅうっ×4 (mỗi 2 u) → 'chụụt' ×4; VN cũ 'chụt' thiếu 1 u mỗi chỗ.")
add(1304, "「Ưm……liếm——liếm——chụt——（ực） ……liếm——chụụụt——chụt——（ực）」", MO, "JP ちゅううっ (3 u) → 'chụụụt' ('chụttttt' sai đếm).")
add(1411, "「Liếm——liếm——liếm——chụt—— liếm——chụt——chụụt——liếm——」", MO, "JP ちゅうっ (2 u) → 'chụụt'; VN cũ 'chụt' thiếu 1 u.")

ME = 'meaning'
# --- G. Meaning (3 rows) ---
add(1479, "「Ng-ngài Soutetsu?」", ME, "JP 「そ、双鉄さま？」: 'Nga' không phải từ ngập ngừng tiếng Việt (đọc như tên riêng); mẫu nói lắp trong file (1446 'K, không' cho い、いや) → nói lắp trên 'ngài': 'Ng-ngài Soutetsu?'.")
add(1612, "Bị cắn nhẹ quá sướng, tôi bật ra tiếng kêu khá lớn. Suzu rời môi ra chụt một cái, nhìn tôi bằng ánh mắt vui sướng.", ME, "JP 'すずはちゅぱっと唇を話し' (rời môi ra sau nụ hôn; 話し chắc là lỗi đánh máy của 離し) — VN 'chu môi' (mím môi) là hành động ngược lại → 'rời môi ra'.")
add(1801, "Khuôn mặt thật của Suzu ló ra rồi vội vàng trốn sau bóng dáng con mèo. Niềm vui sướng, sự yêu thương. Trong khoảnh khắc đó gấp trăm lần……", ME, "JP cụt câu 'その瞬間に何百倍にも' (dòng kề 1802 đã sang câu mới, không có phần tiếp) — VN cũ bịa thêm phần kết 'tăng lên gấp trăm lần' (tiền lệ file 06 key 2035) → giữ nguyên dạng cụt 'gấp trăm lần……'.")
add(1907, "（Bóp chặt）", SX, "JP （むぎゅっ） là tiếng bóp/nắn chặt (dòng kề 1903/1905/1906/1909 đều là siết/kéo/đâm); VN 'Xoẹt' là tiếng xé/rách — sai hẳn hành động (TW 刺啦 là đọc sai của TW; JP thắng TW) → 'Bóp chặt'.")

# ---- assemble + verify ----
assert len(F) == 73, len(F)
assert len(set(k for k, _, _, _ in F)) == 73, "duplicate keys!"
out = []
for key, fix, kind, reason in F:
    r = bykey[key]
    assert fix != r['Vietnamese'], f"{key}: fix == old"
    out.append({"key": key, "jp": r['JP Original'], "tw": r['TW Original/Current'],
                "old_vn": r['Vietnamese'], "fix": fix, "kind": kind,
                "character": r['Character'], "reason": reason})
json.dump(out, open(BASE/'audit-hachirokuh3-tsuuhan-shippai-wrong.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)

# TOML block (single-line values; no literal \n in fixes)
def toml_escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"')
lines = ["[script]"]
for e in out:
    lines.append(f'{e["key"]} = "{toml_escape(e["fix"])}"')
block = "\n".join(lines) + "\n"
open(BASE/'audit-h3-tomlblock.txt', 'w', encoding='utf-8').write(block)

# verify: parse + counts + values
parsed = tomllib.loads(block)
assert len(parsed['script']) == 73, len(parsed['script'])
mism = [(e['key'], parsed['script'][e['key']], e['fix']) for e in out if parsed['script'][e['key']] != e['fix']]
assert not mism, mism
# diff-sanity: each fix differs from old only in targeted change (similarity ratio)
from difflib import SequenceMatcher
low = []
for e in out:
    ratio = SequenceMatcher(None, e['old_vn'], e['fix']).ratio()
    if ratio < 0.5:
        low.append((e['key'], round(ratio, 2)))
print("JSON entries:", len(out))
print("TOML keys parsed:", len(parsed['script']), "| value mismatches:", len(mism))
print("low-similarity fixes (<0.5):", low)
from collections import Counter
print("by kind:", dict(Counter(e['kind'] for e in out)))
print("by character:", dict(Counter(e['character'] for e in out)))
# check fix strings contain no literal backslash-n and no raw tsu
bad = [e['key'] for e in out if '\\n' in e['fix'] or 'っ' in e['fix']]
print("fixes with literal \\n or raw tsu:", bad)
print("OK")
