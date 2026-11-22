# Moan-fix — lr_日々姫h1_鏡の中日々姫.txt.toml (route 02_Hibiki)

- File: `lr_日々姫h1_鏡の中日々姫.txt.toml` — route 02_Hibiki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/02_Hibiki/lr_#U65e5#U3005#U59ebh1_#U93e1#U306e#U4e2d#U65e5#U3005#U59eb.txt.toml`
- Số dòng script: **325** (日々姫 163, 双鉄 66, độc thoại 96). Đọc toàn bộ 325/325 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: cảnh H của Hibiki và Soutetsu trước gương (鏡の中日々姫 — "Hibiki trong gương").
- Audit đã gộp trước đó: **41/325 dòng sai** — 19 mất Ư (gasp), 18 rên (romaji fa/fu, họ ひゃ, đếm âm), 4 sai nghĩa (1117, 1321, 1377, 1455 — KHÔNG sửa trong đợt moan, chỉ kiểm xem có dòng rên nào chồng lên không: không có).
- **Kết quả đợt moan: đổi 0 dòng — file đã sạch về rên.** Audit của file này (gộp 22/11 ~03:45) đã áp triệt để quy tắc romaji + công thức đếm nguyên âm, nên đợt moan chỉ còn việc kiểm chứng lại, không tìm thêm lỗi nào.
- CSV3: 1 set duy nhất, 0 khóa trùng, 325 dòng. TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 158 giá trị khớp đúng, 167 giá trị TOML đã flatten `\n` literal thành khoảng trắng, 0 sai lệch khác (kiểm bằng máy).
- TOML md5: `8e7924c231fed9512780b5e53fce841e` — khớp md5 trong audit REVIEW. Không có bản sao của file này trong 11 nhóm trùng (chỉ 1 file có md5 này trong toàn bộ `sources/toml2/`). File có BOM + CRLF.
- `[selections]` rỗng. Không có thẻ `%l` nào trong file.

## §1. Kiểm kê rên (127 dòng ứng viên)

Đã đọc tay toàn bộ 325 dòng; quét máy tìm 127 dòng ứng viên rên/SFX, gồm:

| Nhóm | Số dòng | Ghi chú |
|---|---|---|
| Thoại có âm rên/thở/gasp/SFX | 60 | 日々姫 + 双鉄 |
| SFX độc thoại trong ngoặc （ ） | 59 | chuỗi 1749–1833 |
| Độc thoại khác có âm thở/rên | 8 | 1433 (đã audit-fix), 1447 (lời kể nhịp thở), 1616/1617 (きゅん/きゅうきゅう diễn bằng lời), còn lại là dương tính giả đã đọc tay (はっきり, ぶるぶる…) |
| **Tổng** | **127** | **Đổi 0, giữ 127** |

Trong 127 dòng: 28 dòng đã có fix trong audit (18 rên + 19 gasp − trùng 1069/1291 tính 1 lần − 1117 nghĩa = 28 dòng rên/gasp thực sự), 99 dòng giữ nguyên từ VN cũ.

## §2. Kiểm chứng lại 18 fix rên của audit — tất cả ĐÚNG, không đổi

Đã kiểm từng giá trị fix rên của audit đối chiếu JP (đếm nguyên âm bằng máy). Không dòng nào cần sửa:

| Keys | Nội dung kiểm chứng | Kết luận |
|---|---|---|
| 1029, 1033, 1039, 1063, 1067, 1069, 1103 | ふあっ → "Fua"/"fua" (7 dòng) | Đúng — ふあ (あ đầy) = "fua", mất mora u nếu viết "fa" |
| 1041 | きゃんっ → "Kyan!!?" | Đúng — quy tắc họ ひゃ 21/11, "Á" mất phụ âm ky- |
| 1064 | ふぁぁぁああああああんっ → "Faaaaaaaaann" (JSON) | Đúng — đếm máy: JP 9 a + 1 ん; fix 9 a + 1 n. Lưu ý: phần văn xuôi §2 của audit review gõ nhầm "Faaaaaaaaann" (2 n), nhưng JSON và khối TOML đều là 9a/1n — giá trị đã gộp là đúng |
| 1115 | token 2 ぁ×13 + ん×3 → "Aaaaaaaaaaaaannn" | Đúng — đếm máy: 13 a + 3 n |
| 1145 | んきゅう×12 → "Nkyuuuuuuuuuuuuu" | Đúng — đếm máy: 13 u (công thức 1 + 12) |
| 1107, 1108, 1219, 1291, 1292, 1433 | はぁ/はあ → "Haa"/"haa" (mỗi token 2 a) | Đúng — 6 dòng, mỗi token đủ 2 a |
| 1139 | んふっ → "Nfu" | Đúng — 1 n, tiền lệ Nhyun/Nkyun |
| 1142 | んくんっ → "Nkun!!" | Đúng — 3 mora n-ku-n, "Ưn" mất mora く |
| 1291 | はぁ×4 → "Haa——haa——haa——haa——" + giữ Ư của audit | Đúng — đếm âm + gasp đều đủ |
| 1103 | ハァッ → "haa" (2 a) + ふあっ → "fua" | Đúng |

Quét máy bổ sung trên toàn file (không chỉ 18 dòng audit): 0 dòng nào khác có はぁ/はあ mà VN chỉ 1 a; 0 dòng nào khác có ふあ mà VN viết "Fa"; 0 dòng nào khác có "Á" cho họ ひゃ/ひゅ/ひあ/きゃ; 0 dòng "Kh" nào bị đổi (file không có dòng "Kh" — chuỗi "Kh" tìm được chỉ là "Không"/"khác" trong câu thường).

## §3. Kiểm tra sweep っ-gasp cho file này — không đụng dòng gasp Ư nào

Sweep có 14 mục fix + 3 mục "already-rendered" cho file này (đã kiểm trực tiếp trong `sweep-raw-gasp-wrong.json`):
- 14 mục fix của sweep (1005, 1049, 1054, 1092, 1093, 1094, 1095, 1097, 1123, 1127, 1237, 1291, 1331, 1338) — audit đã nhận đủ, giá trị đúng, không đụng.
- "Already-rendered" 1126 (`うぅ～～っ` → "Ưư~~") và 1146 (`んんんん～～～っ` → "Ưmmmm~~~!!!") — xác nhận đúng, không sửa.
- "Already-rendered" 1069 — audit đã ghi đè đúng phần ～～っ (xem audit §2), không đụng thêm.
- 5 lỗi sweep bỏ sót (1022, 1034, 1066, 1266, 1337) — audit đã sửa, không đụng.
- 1096: JP chỉ là dấu câu `「！！！！！」`, TW thêm 唔 — JP thắng, không có âm nào để diễn, VN `「!!!!!」` đúng; sweep không có mục này là đúng, audit không cờ là đúng.
- Không dòng gasp Ư nào bị xem lại, không dòng "Kh" nào bị đổi.

## §4. Các dòng đã kiểm và GIỮ NGUYÊN (quyết định có căn cứ)

- 1032 `ひあっ` → "Hia!" — đúng quy tắc họ ひゃ (ひあ→Hia). 1035 `ひゃうんっっ` → "Hyaun!!" (hya-u-n đủ 3 mora). 1154 `ひゃんっ` → "hyan!" — đúng.
- 1141/1143 `んひゅんっ` → "Nhyun", 1144 `んきゅんっ` → "Nkyun" — đúng quy tắc 3b.
- 1052/1059 `ふやっ` → "Fuya" — romaji, nhất quán toàn file (1049, 1067 cùng dạng). 1069 `ふきゅっ` → "Fukyu!" — đúng.
- 1072 `くはっ` → "Kuha!!!", 1073 `くあっ` → "Kua!!!!" — romaji đúng âm.
- 1082/1083 `はぅ` → "Hau" — đúng. 1085 `ふううううううっ` → "Fuuuuuuu" (7 u = công thức 1 + 6 う) — đúng, đã đếm máy.
- 1044/1045/1118/1197 `ふっ` → "Fu"/"fu" — romaji, nhất quán toàn file (xem cờ F2 về khác biệt liên file).
- 1047/1160 `ふ、ぁ` → "Fu, a" — dạng tách hơi thở, TW cũng tách; đồng ý với dạng "Fu, a" của moan-fix 凪ふかみh2 1300 (xem cờ F3).
- 1057/1062/1077 `ふぁ` → "Fa"/"fa" — đúng (ぁ nhỏ, không phải ふあ).
- 1054 `ふぇ？` → "Hể?" — giữ: đây là câu hỏi ngạc nhiên ("huh?"), không phải tiếng rên; "Phuê?" sẽ sai ngữ cảnh.
- 1126 `うぅ～～っ` → "Ưư~~", 1146 `んんんん～～～っ` → "Ưmmmm~~~!!!" — đã diễn đủ âm, sweep + audit đều xác nhận.
- 1122 `ぁっ！　うっ――んっ――` → "A! Ư——ưm——", 1128 `んっっ――ぐっ` → "Ưm——hự!!!", 1071 `くっ――ぁっ――んっ――（ごくっ）` → "Hự——a——ưm——（Ực）" — っ gắn vào âm đã diễn, không thêm Ư.
- 1137 `んふふっ` → "Nfufu" — cười romaji, đúng (không phải gasp). 1086/1088/1125/1329 `えへへっ` → "Ehehe!" — cười, đúng.
- 1036 `やぁん――` → "Đừng mà——", 1038 `やぁん` → "Aaa.", 1029/1148 `やっ――` → "không——"/"Đừng——" — cách diễn phản đối tự nhiên theo ngữ cảnh, audit §5 đã giữ.
- 1109 `（ごくり）` → "（Nuốt nước bọt）", 1334 `（はむっ）` → "（Cắn）" — diễn bằng lời hợp lệ cho SFX trong ngoặc, audit §5 đã giữ.
- 1032 `ごちゅ、ごちゅっ` → "Bị đâm, thật mạnh, thế này", 1317 `ごちゅごちゅ、ノック` → "hãy gõ——thật mạnh" — SFX trong thoại diễn bằng lời theo phong cách nhất quán của file, audit đã giữ.
- 1447 `すうはぁすうはぁ` → "Từng nhịp thở gấp gáp kéo dài vài giây" — đây là lời kể (độc thoại miêu tả nhịp thở), không phải âm rên cần diễn; giữ.
- 1240/763/1235 `――っ――` gắn vào từ có nội dung (には, だが, 日々姫) — không phải gasp, audit §5 đã giữ.
- 985 `いやっ` → "Không.", 1326 `もうっ` → "Sắp!!", 1215 `くるっ！　きちゃう！` → "Đến mất! Sắp ra rồi!" — っ gắn vào từ có nội dung, đã diễn qua từ, không thêm Ư.
- Chuỗi SFX độc thoại 1749–1833 (59 dòng: `ちぃ`→"Xoè", `ごちゅっ`→"Hự", `ずぶっ`→"Phập", `きゅん`→"Siết"/"Thắt lại", `びゅっ`→"Phụt"…) — diễn bằng từ tiếng Việt theo phong cách nhất quán của file, audit §5 đã giữ toàn bộ. Độ dài kéo dài (lạiiii, vàooooo, Phụtttt) là cảm tính, không áp công thức đếm mora theo quyết định audit §5 — xem cờ F1.
- 1117 `ああああああ` → "Aaaaaa" (6 a) đã đúng — dòng này là lỗi nghĩa của audit, không thuộc đợt moan; không có dòng rên nào chồng lên 4 dòng nghĩa (1117, 1321, 1377, 1455).
- Đại từ: Soutetsu "anh" với Hibiki xuyên suốt — không có lỗi đại từ, không sửa (audit đã kiểm).

## §5. Cờ cho đợt thống nhất (không quyết ở đây)

- **F1 — Độ dài kéo dài trong SFX độc thoại （ ） diễn bằng lời là cảm tính, không nhất quán:** 1773 `きゅうう` (2 u) và 1795 `きゅうううう` (4 u) đều → "lạiiii" (4 i); 1797 `きゅぅ×~15` → 14 i; 1798 `きゅう×12` → 10 i; 1799 `きゅう×11` → 10 i; 1810 `ずりゅう×9` → "raaaaaaaaaa" (10 a) nhưng 1818 `う×13` cũng → 10 a; 1825 `ずりゅう×9` → "vàoooooooooooo" (12 o); 1815 `ずぶう×16` → 18 dấu "!" thay vì nguyên âm. Audit §5 đã quyết không áp công thức đếm mora cho dạng diễn bằng lời. Đợt thống nhất nên chốt một quy ước (có chuẩn hoá độ dài kéo dài hay giữ nguyên cảm tính từng dòng).
- **F2 — `ふっ` diễn khác nhau liên file:** file này dùng romaji "Fu" (1044/1045/1118/1197); 凪ふかみh1 dùng "phù"; lr-hibikifukami-h1 dùng "Hư"/"hư". Đợt thống nhất chốt một dạng toàn dự án. Không đổi trong đợt moan.
- **F3 — Dạng tách hơi thở `ふ、ぁ`:** file này dùng "Fu, a" (1047/1160), đồng ý với moan-fix 凪ふかみh2 1300; h7 giữ "phù——a". Đã cờ ở nagifukamih2 (F3) — đợt thống nhất chốt một dạng toàn dự án.

## §6. Lượt soát 2 (đọc lại toàn bộ giá trị fix đối chiếu JP)

- Tổng số fix moan: **0 / đã đọc lại 0 / loại bỏ 0 / sửa lại 0**.
- Lượt soát 2 không chỉ soát fix (không có fix nào) mà soát lại toàn bộ kết luận "0 đổi": đọc lại 18 giá trị fix rên của audit + 19 giá trị gasp Ư + quét máy lại toàn file (はぁ/はあ, ふあ/ふぁ, họ ひゃ, "Á", "Kh") — xác nhận không còn lỗi rên nào. 0 giá trị bị loại, 0 giá trị bị sửa.
- Kiểm cơ học sau soát 2: JSON 0 mục, khóa string (danh sách rỗng); khối TOML parse được bằng tomllib, 0 khóa, 0 sai lệch giá trị; không có dòng gasp Ư nào bị đụng; không có dòng "Kh" nào bị đổi; 4 dòng nghĩa của audit không bị sửa.

## Khối TOML (đã kiểm parse)

```toml
[script]
```

## Kết bài

File lr_日々姫h1_鏡の中日々姫.txt.toml: đọc toàn bộ 325/325 dòng, xét 127 dòng rên/SFX — đổi **0 dòng (moan)**. Audit của file này đã sửa đúng và đủ cả 18 lỗi rên (romaji fa/fu, họ ひゃ, đếm nguyên âm — đã kiểm lại bằng máy: 1064 9a/1n, 1115 13a/3n, 1145 13u) và 19 lỗi gasp Ư; phần còn lại của file đã đúng (romaji Hya/Hia/Kyan/Nhyun/Nkyun/Nfu/Nkun/Fua/Fuuuuuuu, cười "Ehehe"/"Nfufu", SFX diễn bằng lời theo phong cách file). Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa (CSV3 1 set, 325 dòng). Sweep đã kiểm trực tiếp: 14 fix + 3 already-rendered đều đúng, 5 mục sweep bỏ sót audit đã sửa; không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào. Lượt soát 2: 0/0/0/0 (soát lại toàn bộ kết luận 0 đổi). Cờ đợt thống nhất: F1 độ dài kéo dài SFX （ ） cảm tính, F2 `ふっ` "Fu" vs "phù" vs "Hư" liên file, F3 dạng tách "Fu, a" vs "phù——a". Khối TOML trên đã kiểm parse: 0 khóa, 0 sai lệch giá trị.
