# -*- coding: utf-8 -*-
"""Build audit deliverables for 稀咲h1_性生活.txt.toml (06_Kisaki).
Hand-written fixes only (from full JP+TW read). Assembles wrong.json +
TOML block from CSV3-exact jp/tw/old_vn, then verifies mechanically.
"""
import csv, json, tomllib, difflib, hashlib

PILOT = "/home/hatch/workspace/maitetsu-pilot"
TOML_PATH = PILOT + "/sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b2h1_#U6027#U751f#U6d3b.txt.toml"
CSV_PATH = PILOT + "/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv"

# key -> (fix, kind, reason)
FIXES = {
 # --- Kisaki self-pronoun "tôi" -> "em" with Soutetsu (11) ---
 # "anh Soutetsu"/"anh" KEPT per pending Hieu question (h3/file-02 precedent); only self-pronoun fixed.
 "1416": ("「Không sao, em quen rồi.\\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\" theo tiền lệ đã merge lr_稀咲h1 + h3 (\"em\" toàn file); \"anh Soutetsu\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu (h3 33 dòng, file 02 10 dòng)."),
 "1217": ("「Dù vậy, em cũng thấy cuộc gọi đó khá kỳ lạ.\\nNửa đêm nửa hôm lại bảo 『hãy đi làm sớm hơn bình thường hai tiếng』.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\" (tiền lệ lr_稀咲h1/h3; file này \"em\" 19 dòng vs \"tôi\" 11 dòng, không chia theo cảnh)."),
 "1464": ("「Chuyện đó em cũng quen rồi.\\nThế? Bố em đã nói gì về em vậy?」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"Bố tôi/về tôi\"→\"Bố em/về em\" theo cùng quy tắc (nói về bản thân với Soutetsu)."),
 "1303": ("「Ừm. Chà, em cũng vậy.\\nMột ngày nào đó…… không xa…… kiểu như trong tương lai gần vậy.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\" (tiền lệ lr_稀咲h1/h3)."),
 "1204": ("「Đối phương là em mà, anh lại bảo không có cảm giác gì sao.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"anh\" (gọi Soutetsu) GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 "1373": ("「Em hiểu mà, anh Soutetsu.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"anh Soutetsu\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 "1357": ("「Tình dục——tình dục không phải là thứ đáng bị ghê tởm.\\nEm sẽ dạy cho anh Soutetsu điều đó.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"anh Soutetsu\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 "1462": ("「Ra là vậy.\\nNếu thế, em sẽ làm cho anh sướng hơn nữa nhé.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"anh\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 "1369": ("「Cảm thấy mãnh liệt như vậy, không biết thực tế có làm thế không——\\nhay đó chỉ là hư cấu nhỉ? Em cũng từng nghĩ thế nhưng……」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\" (tiền lệ lr_稀咲h1/h3)."),
 "1398": ("「Đúng…… vậy. Em cũng, thấy sướng ở núm vú.\\nNhững phần chạm vào cơ thể anh Soutetsu, tất cả, đều sướng đến mức như sắp tan chảy ra vậy.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu: \"tôi\"→\"em\"; \"anh Soutetsu\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 "1376": ("「Giống hệt như tâm trạng của em,\\ncơ thể em cũng đang rất vui sướng vì được gắn kết với anh Soutetsu đấy.」",
           "pronoun", "Kisaki tự xưng ボク với Soutetsu (2 lần): \"tôi\"→\"em\"; \"anh Soutetsu\" GIỮ NGUYÊN theo câu hỏi đang chờ Hieu."),
 # --- Soutetsu "anh" -> "tôi" / "em" -> "cô" with Kisaki (15) ---
 "1288": ("「À——cô đã đánh thức tôi sao.」",
           "pronoun", "Soutetsu với Kisaki là \"tôi\" (JP 僕), gọi Kisaki \"cô\" — quy tắc đã khóa; VN cũ \"em/anh\" sai cả hai chiều (tiền lệ Grand 11 2173/2347)."),
 "1451": ("「Chắc là nhờ Kisaki đánh thức tôi chăng.\\nTôi đã có thể thức dậy với một tâm trạng vô cùng sảng khoái.」",
           "pronoun", "Soutetsu với Kisaki là \"tôi\" (JP 僕, 2 lần) — quy tắc đã khóa; VN cũ \"anh\" cả hai lần."),
 "1394": ("「Đúng vậy…… tôi thích lắm. Cả dương vật lẫn bản thân tôi, đều thích――mái tóc\\n……của Kisaki――cả đôi bàn tay…… hơi thở, và mùi hương…… tôi yêu tất cả mọi thứ thuộc về cô」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (3 lần, JP 僕) và \"em\"→\"cô\" (JP không có đại từ — gọi Kisaki; tiền lệ Grand 11 2173)."),
 "1426": ("「Kisaki――nếu cứ tiếp tục thế này――tôi ra mất!」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (JP 僕, ngầm trong もう — \"tôi sắp ra\")."),
 "1189": ("「Cô không cần phải cố nuốt xuống đâu」",
           "pronoun", "Soutetsu gọi Kisaki \"em\"→\"cô\" (quy tắc đã khóa; tiền lệ Grand 11 2173)."),
 "1432": ("「Kisaki…… cô đẹp lắm」",
           "pronoun", "Soutetsu gọi Kisaki \"em\"→\"cô\" (quy tắc đã khóa; tiền lệ Grand 11 2173)."),
 "1449": ("「Sự tiếp xúc da thịt lại tuyệt vời đến thế này……\\nĐược Kisaki dạy cho điều đó, tôi thực sự rất hạnh phúc」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (JP 僕は)."),
 "1361": ("「Tôi――dạy cho Kisaki sao?」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (JP 僕が)."),
 "1364": ("「Tôi cũng vậy――tình dục của tôi, cũng chỉ có thể học từ Kisaki,\\nvà tôi cũng không muốn học từ ai khác」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (3 lần, JP 僕)."),
 "1433": ("「Kisaki…… cô cởi quần lót ra được không?」",
           "pronoun", "Soutetsu gọi Kisaki \"em\"→\"cô\" (quy tắc đã khóa; tiền lệ Grand 11 2173)."),
 "1400": ("「Vậy sao? Dù đây là lần đầu tiên tôi làm chuyện này đấy」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (JP ngầm — người nói là Soutetsu, lần đầu của cậu)."),
 "1316": ("「Ừm, tôi cũng vậy.\\n――Tôi cũng……ƯƯ――ra đây」",
           "pronoun", "Hai lỗi một dòng: (1) Soutetsu với Kisaki \"anh\"→\"tôi\" (2 lần, JP 僕もだ/僕も); (2) gasp っっ thô trong VN → ƯƯ (sweep raw-tsu, đã kiểm chứng vs JP)."),
 "1366": ("「Tôi cũng vậy――Kisaki! Một chút, nữa thôi――Ư!」",
           "pronoun", "Hai lỗi một dòng: (1) Soutetsu với Kisaki \"anh\"→\"tôi\" (JP 僕もだ); (2) gasp っ thô trong VN → Ư (sweep raw-tsu, đã kiểm chứng vs JP でっ――っ)."),
 "1379": ("「Tôi còn muốn học hỏi nhiều hơn nữa.\\nChỉ cần vết thương ở âm đạo của Kisaki lành lại, tôi sẵn sàng làm ngay lập tức」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (2 lần, JP ngầm — người nói là Soutetsu)."),
 "1450": ("「Nhờ vậy mà, tôi cũng――」",
           "pronoun", "Soutetsu với Kisaki: \"anh\"→\"tôi\" (JP 僕も)."),
 # --- Gasp っ — sweep, verified vs JP (10) ---
 "1254": ("「I hyuuuuuuuuuƯƯ!!!」",
           "gasp", "Sweep raw-tsu: っっ thô trong VN → ƯƯ. Đếm lại độc lập số u: JP いっひゅうぅぅぅぅぅぅぅ = ひゅ(1u) + う(1) + ぅ(7) = 9 u (công thức độ dài nguyên âm; tiền lệ moan lr稀咲追加h 1855: ひゅ1+う8=9u) — bản sweep giữ 7 u của Gemini là SAI, đã sửa thành 9 u."),
 "1306": ("「Ưm kyu――kuha――ưm a――~~~Ư!!!」",
           "gasp", "Sweep raw-tsu: っ thô cuối dòng → Ư (JP ～～～っ; 3 dấu ~ khớp JP)."),
 "1310": ("「Ưm!? Phụt――ưm~~~~~~Ư」",
           "gasp", "Sweep raw-tsu: っ thô cuối dòng → Ư (JP ん～～～～～～っ; 6 dấu ~ khớp JP)."),
 "1323": ("「Ưm~~~~~Ư――ưm――ưm――ực!」",
           "gasp", "Sweep raw-tsu: っ thô sau ~~~~~ → Ư (JP ん～～～～～っ; 5 dấu ~ khớp JP)."),
 "1486": ("「Ư!」",
           "gasp", "Sweep lost-gasp-whole: JP 「っ！」 cả dòng chỉ là gasp, VN cũ chỉ còn \"!\" — thêm Ư."),
 "1487": ("「Ư!!」",
           "gasp", "Sweep lost-gasp-whole: JP 「っ！！」 cả dòng chỉ là gasp, VN cũ chỉ còn \"!!\" — thêm Ư."),
 "1488": ("「Ư!!!」",
           "gasp", "Sweep raw-tsu: JP 「っ！！！」 cả dòng chỉ là gasp, VN còn nguyên っ → Ư."),
 "1492": ("「~~~~~Ư!!!」",
           "gasp", "Sweep raw-tsu: っ thô sau ~~~~~ → Ư (JP ～×5, VN ~×5 khớp)."),
 "1494": ("「~~~~~~~~~~Ư!!!」",
           "gasp", "Sweep raw-tsu: っ thô sau ~~~~~~~~~~ → Ư (JP ～×10, VN ~×10 khớp)."),
 "1650": ("「Nụ cười rạng rỡ.\\nCơ thể đang căng cứng của Kisaki, chợt mềm ra một chút――Ư!!?」",
           "gasp", "Sweep lost-gasp-trailing: JP やわら――っ！！？ — gasp cuối dòng bị mất hẳn trong VN, thêm Ư sau ――."),
 # --- SFX / moan vowels (2) ---
 "1308": ("「Ưm――ực――ưm――ực, ưm――\\nphuê!」",
           "sfx", "JP ぷえっ: ぷ+え+っ → \"phuê\" (tiền lệ ふぇっ→\"Phuê\"); VN cũ \"phù!\" sai nguyên âm (e→u)."),
 "1243": ("「Kyu――ưm――hya――ea――a――」",
           "sfx", "JP ぇあっ: ぇ+あ → \"ea\" (romaji fallback cho rên; \"đừng để mất âm\"); VN cũ \"a\" làm mất âm ぇ."),
}

rows = {}
with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        if row["File"].split(chr(92))[-1] == "稀咲h1_性生活.txt.toml":
            rows[row["Key"]] = row
assert len(rows) == 335, len(rows)

items = []
for k in sorted(FIXES, key=lambda x: int(x)):
    fix, kind, reason = FIXES[k]
    r = rows[k]
    assert fix != r["Vietnamese"], f"no-op {k}"
    items.append({"key": k, "character": r["Character"], "jp": r["JP Original"],
                  "tw": r["TW Original/Current"], "old_vn": r["Vietnamese"],
                  "fix": fix, "kind": kind, "reason": reason})

json.dump(items, open(PILOT + "/audit-kisakih1-seikatsu-wrong.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

# TOML block: literal backslash-n in fix values must be written as \\n
def toml_esc(v):
    return v.replace("\\", "\\\\").replace('"', '\\"')
block_lines = [f'"{it["key"]}" = "{toml_esc(it["fix"])}"' for it in items]
block = "\n".join(block_lines)
open(PILOT + "/audit-kisakih1-seikatsu-tomlblock.txt", "w", encoding="utf-8").write(block + "\n")

# Verify: parse block, key count, 0 value mismatches (raw strings)
parsed = tomllib.loads("[script]\n" + block)["script"]
assert len(parsed) == len(items), (len(parsed), len(items))
mism = [(k, parsed[k], next(i["fix"] for i in items if i["key"] == k))
        for k in parsed if parsed[k] != next(i["fix"] for i in items if i["key"] == k)]
print("JSON items:", len(items))
print("TOML block keys:", len(parsed), "value mismatches:", len(mism))
# diff-sanity
for it in items:
    ratio = difflib.SequenceMatcher(None, it["old_vn"], it["fix"]).ratio()
    if ratio < 0.5:
        print("LOW RATIO", it["key"], round(ratio, 2), repr(it["old_vn"][:60]), "->", repr(it["fix"][:60]))
import collections
print("kinds:", dict(collections.Counter(i["kind"] for i in items)))
print("keys:", [i["key"] for i in items])
print("md5:", hashlib.md5(open(TOML_PATH, "rb").read()).hexdigest())
