# Moan-fix snippet — lr_日々姫真闇h1_三人家族.txt.toml (moan-lr-hibiki-mayami-h1-sannin-kazoku)

- File: `lr_日々姫真闇h1_三人家族.txt.toml` — route 02_Hibiki, H-scene (Hibiki + Mayami, "gia đình ba người"), 436 dòng script, audit trước đó 60 sai.
- TOML md5: `d8f257e11854179d1a64585836ad9112`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 436 dòng, 0 key trùng; VN khớp TOML 435/436 (1 dòng còn lại chỉ khác TOML-2 làm phẳng `\n` thành khoảng trắng, key 1420).
- Đã đọc 436/436 dòng; xét 248 dòng rên/SFX/gasp (169 thoại rên + 79 SFX độc thoại trong ngoặc đơn).
- Đổi 3 dòng: 1550 ああああああっ "A a a a a a" → "Aaaaaa" (gộp 1 âm rên dài bị tách thành 6 mảnh); 1555 んウゥゥぅ "Nguuuuu" → "Nguuuu" (4 u theo JP + TW 4×唔; giữ Ư của audit); 1619 『あーーーーーーん』 'Aaaaaaaan' (8 a) → 'Aaaaaaan' (7 a; JP あ+6ー).
- Kiểm chứng độc lập 9 fix đếm nguyên âm của audit: 8 đúng (1440 19a, 1441 6a, 1446 20u, 1467 4a, 1477 19a, 1478 18a, 1479 14a, 1611 10o); chỉ 1619 sai (audit áp nhầm 8 a của 1579). Kiểm chứng 1579 đúng (8 a).
- Giữ 245 dòng rên/SFX (họ ひゃ/ひゅ/ひあ/きゃ đã romaji, không có "Á"; họ ふぁ/ふあ→"Fua"; ふ、ぁ tách theo JP 、 thì giữ "Fu, a" — tiền lệ parent-verified; cười "Nfufu"/"Ufufu"; SFX từ Việt theo quy ước file; っ nhấn mạnh cuối câu không thêm Ư).
- Sweep: 26 mục đã kiểm chứng trực tiếp — 24 audit đã áp đúng (fix audit = fix sweep 24/24), 2 already-rendered đúng (1432, 1723); không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào (file không có "Kh").
- Cờ cho đợt thống nhất: 2 (1555 — dùng "Nguuuu~Ư!!" thay fix audit 5 u; 1619 — dùng 'Aaaaaaan' 7 a thay fix audit 8 a).
- Lượt soát 2: tổng 3 / tái kiểm chứng 3 / bỏ 0 / sửa 0. JSON 3 mục, khóa string, jp/tw/old_vn khớp CSV3 3/3. Khối TOML parse bằng tomllib: 3 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hibiki-mayami-h1-sannin-kazoku-REVIEW.md`; danh sách sửa: `moan-lr-hibiki-mayami-h1-sannin-kazoku-wrong.json`.

**Tổng cộng sau file này: 36 file / 846 dòng sai (moan)** (cơ sở 35 file / 843 dòng + 3 file này)
- FLAG (đợt thống nhất): 1555 — dùng giá trị moan 「A! Fua! A!!! Nguuuu~Ư!!」 (4 u) thay fix audit 5 u (JP んウゥゥぅ = 4 u, TW 4×唔). 1619 — dùng giá trị moan 'Aaaaaaan' (7 a) thay fix audit 8 a (JP あ+6ー = 7; audit áp nhầm giá trị của 1579).
