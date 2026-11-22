# Moan-fix snippet — lr_日々姫h1_鏡の中日々姫.txt.toml (moan-lr-hibikih1-kagami-no-naka-hibiki)

- File: `lr_日々姫h1_鏡の中日々姫.txt.toml` — route 02_Hibiki, 325 dòng script, audit trước đó 41 sai (19 gasp Ư + 18 rên + 4 nghĩa).
- TOML md5: `8e7924c231fed9512780b5e53fce841e` (khớp md5 audit), không có bản trùng. TOML khớp CSV3 tuyệt đối modulo flatten `\n` (158 khớp đúng + 167 flatten, 0 sai lệch khác).
- CSV3: 1 bộ duy nhất, 325 dòng, 0 key trùng.
- Đã đọc 325/325 dòng; xét 127 dòng rên/SFX (60 thoại + 59 SFX độc thoại （ ） + 8 độc thoại khác).
- Đổi 0 dòng: audit đã sửa đúng và đủ cả 18 lỗi rên — kiểm lại bằng máy: 1064 9a/1n, 1115 13a/3n, 1145 13u, 7 dòng ふあっ→"Fua", 1041→"Kyan", 1139→"Nfu", 1142→"Nkun", 6 dòng はぁ/はあ→"Haa" — và 19 lỗi gasp Ư; phần còn lại đã đúng (Hya/Hia/Nhyun/Nkyun, "Fuuuuuuu" 7u, cười "Ehehe"/"Nfufu", SFX diễn bằng lời theo phong cách file).
- Giữ 127 dòng rên/SFX: không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi (file không có dòng "Kh"); 4 dòng nghĩa của audit (1117, 1321, 1377, 1455) không bị sửa, không có dòng rên nào chồng lên.
- Sweep: 14 fix + 3 already-rendered đã kiểm trực tiếp — đều đúng; 5 mục sweep bỏ sót audit đã sửa; 1096 JP chỉ là dấu câu (TW thêm 唔), giữ nguyên là đúng.
- Flag: F1 độ dài kéo dài SFX （ ） diễn bằng lời cảm tính, không nhất quán (1773 vs 1795 đều "lạiiii"; 1797 14i; 1810/1818 đều 10a); F2 `ふっ` "Fu" (file này) vs "phù" vs "Hư" liên file; F3 dạng tách "Fu, a" vs "phù——a" (đồng ý với moan-fix nagifukamih2).
- Lượt soát 2: tổng 0 / tái kiểm chứng 0 / bỏ 0 / sửa 0 (soát lại toàn bộ kết luận 0 đổi: 18 fix rên + 19 gasp của audit và quét máy lại toàn file). JSON 0 mục, khóa string. Khối TOML parse bằng tomllib: 0 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hibikih1-kagami-no-naka-hibiki-REVIEW.md`; danh sách sửa: `moan-lr-hibikih1-kagami-no-naka-hibiki-wrong.json` (danh sách rỗng — file đã sạch về rên).

**Tổng cộng sau file này: 49 file / 1247 dòng sai (moan)** (cơ sở 49 file / 1247 dòng + 0 file này — file đã sạch, 0 dòng đổi; cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của `moans/ROUTE-MOANS.md`)
