# Moan-fix snippet — ハチロクh5_おだいどこしごと.txt.toml (moan-hachiroku-h5-odaidoko-shigoto)

- CSV3: 1 bộ duy nhất, 291 dòng, 0 key trùng; VN khớp TOML sau khi gộp `\n` thành khoảng trắng ở 148 dòng (hiện tượng TOML-2 đã biết).
- Đã đọc 291/291 dòng; xét 134 dòng rên/SFX (87 thoại + 47 SFX độc thoại （）); sửa 28, giữ 106.
- Đổi 28 dòng: romaji 25 + SFX 3.
- Romaji họ fa/fu → Fua/Fa/Pua/Fuya (12 dòng): 1006 ふあっ→"Fua", 1008 ふあっ→"Fua", 1010 ふあ+12あ→"Fuaaaaaaaaaaaa" (12a), 1011 ふあっ→"Fua", 1033 ふあっ→"fua", 1064 ふやっ→"Fuya" + ふあっ→"fua", 1065 ふやっっ→"Fuya", 1070 ぷああっ→"Puaa", 1073 ふあっ→"Fua", 1089 ふぁっ→"Fa", 1178 ふ、あっ→"Fu, a" ×2, 1222 ふあ+6あ+ん×3→"Fuaaaaaannn" (6a+3n).
- Romaji họ ひゃ/ひゅ/ひあ (6 dòng): 996 ひゃふう×8んっ→"Hyafuuuuuuuuun" (9u), 1000 んひゅっ→"Nhyu", 1012 ひあっ→"Hia", 1013 ひあっ→"Hia", 1073 んひゅっ→"Nhyu", 1077 んひゅううぅ×5っ→"Nhyuuuuuuuu" (8u).
- Rên dài một hơi gộp từ dạng tách mảnh (8 dòng): 996, 998 んふう×5っ→"Nfuuuuuu" (6u), 1010, 1067 んふうううっっ→"Nfuuuu" (4u), 1073 あ×8んっ→"Aaaaaaaan" (parent sửa: agent viết thừa 1 a), 1075 んあ×6っ→"Naaaaaa", 1077, 1222.
- Mất phụ âm mora (10 dòng): 759/992/998/1031/1010 や→"Ya"/"ya", 995 やあっ→"Yaa" + んふっ→"Nfu", 1020/1070 くっ→"Ku", 1074 んふうっ→"Nfuu", 1181 かはっ→"Kaha", 1227 かふっ→"Kafu".
- SFX phán đoán (3): 1012 あちゅっ→"Achu" (VN cũ "nóng quá" mất âm — audit bỏ sót), 1020 くっ→"Ku", 1181 かはっ→"Kaha".
- 16/28 key trùng fix audit — fix moan thay thế fix audit ở đúng token rên. 6 Ư sweep giữ nguyên (992/1031/1064/1065 giữ Ư, 1401/1416 không đổi); 8 Ư audit tự thêm: bỏ 6 (996, 1070, 1073, 1075, 1077, 1222 — っ cuối có !/? diễn cắt, tiền lệ h7) — parent GIỮ LẠI 2 (998 +Ư, 1067 +ƯƯ: っ cuối dòng tuyệt đối, không dấu câu, gasp mất hẳn nếu bỏ). Không dòng "Kh" nào bị đổi.
- Giữ 106 dòng rên/SFX: gasp Ư khóa, hơi thở ふ/ふっ đứng riêng "phù" (756), ひ/ひっ→"hí" (1015, 1074), あ ngắn, SFX ちゅ dạng Việt của file (753, 1223), SFX độc thoại （） 47 dòng, cười ufufu, nuốt.
- Sweep: 6 mục đã kiểm chứng — cả 6 đã được audit sửa đúng thành Ư, không đụng. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 28 / tái kiểm chứng 28 / bỏ 0 / sửa 0. JSON 28 mục, khóa string, jp/tw/old_vn khớp CSV3 28/28. Khối TOML parse bằng tomllib: 28 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hachiroku-h5-odaidoko-shigoto-REVIEW.md`; danh sách sửa: `moan-hachiroku-h5-odaidoko-shigoto-wrong.json`.

**Tổng cộng sau file này: 34 file / 799 dòng sai (moan)** (cơ sở 33 file / 771 dòng + 28 file này)
- FLAG (đợt thống nhất): F1 — 1012 あちゅっ→"Achu" (phán đoán moan-pass, audit bỏ sót); F2 — くっ→"Ku" (1020, 1070) vs "Hự"/"Ư" (câu hỏi mở); F3 — かはっ→"Kaha" (1181), かふっ→"Kafu" (1227); F4 — họ ちゅ giữ dạng Việt (753, 1223) vs "chumu" (h3/paulette-h5 942); F5 — dạng tách fa 1047 giữ "phù——a" vs 1178 → "Fu, a"; F6 — 998 れふっ nói ngọng giữ nguyên; F7 — 1015 はひっ→"Hahí" giữ (chưa chuyển "Hahi").
