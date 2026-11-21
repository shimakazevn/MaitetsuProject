# Moan-fix snippet — 凪ふかみh2_みずあそび.txt.toml (moan-nagifukamih2-mizuasobi)

- File: `凪ふかみh2_みずあそび.txt.toml` — route 07_Nagi_Fukami, 350 dòng script, audit trước đó 42 sai.
- TOML md5: `dc5ff6dcb84a35650fb89a8465df9fe0` (khớp md5 audit), không có bản trùng. Lưu ý: disk path trong brief trỏ nhầm sang 凪h2_おとなの水着 (md5 `a581ef85...`); file đúng đã dùng là `#U51ea#U3075#U304b#U307fh2_#U307f#U305a#U3042#U305d#U3073.txt.toml`, md5 đã kiểm chứng.
- CSV3: 1 bộ duy nhất, 350 dòng, 0 key trùng; JP trong comment TOML khớp CSV3 350/350 (kể cả 2 dòng CSV3 bị mojibake 1319/1386 đã kiểm chứng qua TOML).
- Đã đọc 350/350 dòng; xét 135 dòng rên/SFX (86 thoại + 43 SFX độc thoại ngoặc + 3 độc thoại gasp + 2 độc thoại thở + 1 độc thoại （おおお）).
- Đổi 5 dòng: 2 romaji (1300 ふ、あ→"Fu, a"; 1326 やっ→"Ya") + 2 đếm nguyên âm (1294 はぁ×3→"Hàà" + ああ～→"aa~", giữ Ư của audit; 1302 はぁぁぁぁ 5 a→"Hààààà") + 1 sai âm (1397 くおっ→"Kuo!").
- Giữ 130 dòng rên/SFX: 34 fix romaji của audit đều đã đúng (1274 14u, 1277 9u kiểm chứng lại bằng máy); 5 gasp Ư sweep + 5 already-rendered không đụng; hơi thở ふっ/ふうっ→"phù" theo quy ước file; SFX miệng "liếm"/"chụt"; gằn Soutetsu "Hự"; cười "Ư hứ hứ"/"Ni hê hê~"; nói ngọng 1421/1455.
- Sweep: 10 mục đã kiểm chứng trực tiếp (5 fix Ư + 5 already-rendered) — không đụng dòng gasp Ư nào; không dòng "Kh" nào bị đổi (file không có dòng "Kh"; "Kh..." ở 1412 là từ "khủng" bị lắp).
- 1294 thay thế giá trị audit cùng key (giữ Ư của audit, thêm đếm nguyên âm) — áp MỘT giá trị moan mỗi key ở đợt thống nhất.
- Flag: F1 1276 "Fukyu" vs "Phù kiu" (chờ Hieu, giữ "Fukyu" theo tiền lệ 3 file); F2 1299 baby-talk giữ "ưm"; F3 dạng tách fa "Fu, a" vs h7 giữ "phù——a" (cần quyết thống nhất); F4 1350 び bị rơi (TW cũng rơi, cần vòng audit); F5 quy ước độ dài SFX độc thoại （ ） (2132/2141/2149/2150/2154/2155/2160/2174/2182/2165); F6 1294 thay giá trị audit vừa gộp; F7 brief ghi sai disk path.
- Lượt soát 2: tổng 5 / tái kiểm chứng 5 / bỏ 0 / sửa 0 (bắt 1 lỗi trước soát 2: 1300/1326 dùng newline thật thay vì `\n` literal — đã sửa). JSON 5 mục, khóa string, jp/tw/old_vn khớp CSV3 5/5. Khối TOML parse bằng tomllib: 5 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-nagifukamih2-mizuasobi-REVIEW.md`; danh sách sửa: `moan-nagifukamih2-mizuasobi-wrong.json`.

**Tổng cộng sau file này: 49 file / 1247 dòng sai (moan)** (cơ sở 48 file / 1242 dòng + 5 file này — parent REBASE 22/11 ~03:00: snippet ghi cơ sở cũ 47/1239 vì 日々姫h5 đã gộp trước)
