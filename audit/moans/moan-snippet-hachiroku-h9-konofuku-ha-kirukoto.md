# Moan-fix snippet — ハチロクh9_コノフクハキルコト.txt.toml (moan-hachiroku-h9-konofuku-ha-kirukoto)

- File: `ハチロクh9_コノフクハキルコト.txt.toml` — route 01_Hachiroku, 613 dòng script, TOML md5 `bcbf02a0308ddac5d5aca3ac1cd717ce` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 613 dòng, 0 key trùng; VN khớp TOML 613/613 (audit đã kiểm chứng; 26 key sửa kiểm tra lại 0 sai lệch).
- Đã đọc 613/613 dòng; xét 100 dòng rên/SFX (69 Hachiroku + 20 Soutetsu + 11 độc thoại; 83 dòng có っ, 10 dòng họ fa/fu/hya, 31 dòng nguyên âm dài, 6 SFX ngoặc, 4 cười).
- Đổi 26 dòng: 13 romaji + 9 đếm nguyên âm + 4 sai âm.
- Romaji fa/fu: 2082 ふあ→"Fua", 2089 ふっ――ふあっ→"Fu——Fua", 2037 ふあっ→"Fua" ×2 + ふううっ→"Fuuu", 2110 ふあっ→"Fua", 2180 rên dài ふあ… (17 a, bản cũ 20 a tách mảnh)→"Fua"+17 a, 2151 ふ……あ→"Fu……a", 2289 ふ――あっ→"Fu——a", 2109/2378/1356/2613/2319 ふ、あっ→"Fu, a", 2144 ふっ――あっ→"Fu——a".
- Đếm nguyên âm: 2055 はあっ→"haa" ×3, 2097 はぁあっ→"Haaa", 2120 ちゅううう→"chuuuu", 2078 ちゅうっ→"chuu", 2122 れるううううっ→"reruuuuu", 2101 くああ→"Kuaa", 2053 ほう→"hoo", 2134 ほー→"hoo", 2054 はああっ→"haaa" + はぁっ→"haa"; 2110/2289/2109 cũng sửa số âm (はぁっ→"Haa", はああっ→"Haaa", はぁ→"haa").
- Sai âm: 2136 ちろっ→"Chiro", 2156 ちゅむっ→"chumu", 1358 ちゅむ→"chumu" ×2 + ちゅうっ→"chuu" + れるっ→"reru" (bản cũ "liếm lútttt"), 2178 きゅくだぅぅぅ→"Kyukuuuuu" (bản cũ "Ưm ưưưư" mất phụ âm kyu).
- Kiểu lỗi chính: họ fa/fu bị Việt hoá "phù a" trong chuỗi rên cao trào; rên dài đếm nguyên âm sai (thiếu/thừa 1–3 âm, hoặc kéo dài bằng phụ âm t như "chụttttt").
- Giữ 74 dòng rên/SFX (romaji đúng "Hyuua/Hia/Kyaaa/Kyuu", cười "Ufufu", hơi thở "phù" đứng riêng, SFX độc thoại onomatopoeia Việt, gasp Ư của audit/sweep không đụng).
- Sweep: 31 mục đã kiểm chứng qua audit (25 raw-tsu + 5 lost-gasp + 1 already-rendered 2178) — không đụng dòng Ư nào; không dòng "Kh" nào bị đổi (1883 "Kh——ông" giữ nguyên).
- Cờ cho đợt thống nhất: mâu thuẫn audit ở 1883 (JSON ghi "là do anh", REVIEW + ROUTE-AUDIT ghi "là do tôi" — parent kiểm tra giá trị đã merge); 2020 "Ohimitera"→"Ohitoyo"; 7 dòng tách nhịp fa đã về romaji (revert dễ nếu Hieu muốn giữ "phù, a"); 1358 "reru" vs "liếm"; 2178 quyết theo JP (TW diễn thành ưm); SFX độc thoại giữ onomatopoeia Việt, chưa áp công thức đếm nguyên âm.
- Lượt soát 2: tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0. JSON 26 mục, khóa string, jp/tw/old_vn khớp CSV3 26/26. Khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.
- Parent kiểm chứng 21/11 ~10:00: JSON 26, TOML 26 khóa 0 sai lệch, CSV3 26/26; 9 key trùng audit chỉ khác đúng token rên; Ư thêm vào đều là Ư của audit; SỬA 2101 "Aa!"→"Kuaa!" (JP くああ có く, JP thắng TW); 1883 đã giải quyết (xem FLAG).
- Chi tiết đầy đủ: `moan-hachiroku-h9-konofuku-ha-kirukoto-REVIEW.md`; danh sách sửa: `moan-hachiroku-h9-konofuku-ha-kirukoto-wrong.json`.

**Tổng cộng sau file này: 7 file / 182 dòng sai (moan)** (cơ sở 6 file / 156 dòng + 26 file này)
- FLAG (đã giải quyết khi merge): 1883 KHÔNG có mâu thuẫn — agent đọc nhầm old_vn thành fix; audit wrong.json ghi old_vn "là do anh", fix "là do tôi"; REVIEW + ROUTE-AUDIT đều ghi "là do tôi" (đã merge đúng). Phần moan của 1883 không đổi.
