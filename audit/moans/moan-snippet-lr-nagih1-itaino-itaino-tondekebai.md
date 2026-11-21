# Moan-fix snippet — lr_凪h1_痛いの痛いの飛んでけばい (moan-lr-nagih1-itaino-itaino-tondekebai)

- File: `lr_凪h1_痛いの痛いの飛んでけばい.txt.toml` — 304 dòng script, TOML md5 `3b4b468a7b4e2fc41327c15a75dd230c`, không có bản trùng.
- CSV3: 1 bộ duy nhất 304 dòng (thư mục home `07_Nagi_Fukami`); khớp TOML 304/304 sau chuẩn hoá `\n`.
- Đã đọc 304/304 dòng; xét 168 dòng rên/SFX (Nagi 83, Soutetsu 19, độc thoại 66 — trong đó 56 dòng SFX （）).
- Đổi 34 dòng: 17 romaji + 5 mất/sai âm + 12 đếm nguyên âm.
- Romaji họ fa/fu (13): 1145 `Phuan`→`Fan` (ふぁん), 1185 `phua`→`fa`, 1143 `Phua`→`Fua`, 1180 `Phua`→`Fua`, 1201 `Phua`→`Fa`, 1233 `phua`→`fua`, 1199 `Phua`→`Fua`, 1187 `Phua`→`Fa`, 1195 `Huê`→`Fue` (ふぇ), 1236 `phua`→`fua`, 1158 `Phua`→`Fua`, 1162 `phua`→`fa`, 1129 `Phuya`→`Fuya` (ふや).
- Gộp một âm bị tách mảnh (4): 1157 `Ưm hyun`→`Nhyun`, 1161 `Ưm hyun`→`Nhyunn`, 1242 `Khu hyun`→`Kuhyun`, 1234 `phu haa`→`Fahaa`.
- Mất/sai âm (5): 1190 ふあっ `a!`→`fua!` (mất f), 1216 ぺろっ `rero`×5→`pero`×5 (mất p), 1219 ぢゅぼっ `Chubo`→`Jubo` (mất hữu thanh), 1214 わっ `Oa`→`Wa` (mất w), 1169 ぁあっ `a á!`→`Aa!`.
- Đếm nguyên âm (12): 1163 はあっ×4 `ha`→`haa`, 1130 `Kya phuu…u` (17u)→`Kyafuuuuuuuuuu` (10u, gộp 1 token), 1131 `Nhyuaaaaaa` (6a)→`Nhyuaaaaaaaaaaa` (11a), 1223 `Zujuu…u` (20u)→19u + giữ Ư audit, 1217 `Zuryuuuuu` (6u)→`Zuryuuuuuu` (7u), 1221 `Juruuuuuu` (7u)→`Juruuuuu` (6u), 1222 `Reryuuuu` (4u)→`Reryuuuuu` (5u), 1213 `Juuuuuu` (6u)→`Juuuuu` (5u) + áp Ư audit, 1220 `Reruuuuu` (5u)→`Reruuuu` (4u), 1298 ふーっ `Phù`→`Phùu` ×2, 1379 ふーーーっ `Phùuu`→`Phùuuu` ×4, 1137 ふー `Phù`→`Phùu` ×2.
- Lỗi hệ thống chính: bản cũ dùng chung "phua"/"Phua" cho cả ふぁ lẫn ふあ (sai âm — ふぁ phải là "Fa") và tách nhiều âm rên đơn thành mảnh rời ("Ưm hyun", "Khu hyun", "phu haa").
- Giữ 134 dòng rên/SFX (ひゃうっ→"Hyau", んひゅっ→"Nhyu", はひゅっ→"Hahyu", くあっ→"Kua", くふっ→"Kufu", cười "Ufufu"/"Ehehe"/"Nihehe", ぷあっ→"Pua", ふあっ đã romaji đúng 1203/1204/1167/1173/1248/1134/1128, hơi thở ふっ→"Phu"/"phu", toàn bộ 19 dòng gasp Ư của audit).
- Sweep: 13 mục đã kiểm chứng — không còn mục nào chưa xử lý (9 áp nguyên trong audit + 2 already-rendered + 2 needs-file-audit). Chỉ gộp với audit ở 1213/1223 (giữ Ư, đổi token rên); không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 34 / tái kiểm chứng 34 / bỏ 0 / sửa 0. JSON 34 mục, khóa string, jp/tw/old_vn khớp CSV3 34/34. Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-nagih1-itaino-itaino-tondekebai-REVIEW.md`; danh sách sửa: `moan-lr-nagih1-itaino-itaino-tondekebai-wrong.json`.

**Tổng cộng sau file này: 42 file / 1059 dòng sai (moan)** (cơ sở 41 file / 1025 dòng + 34 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
- FLAG (đợt thống nhất): F1 kiai 1224/1225 thiếu 1 o theo công thức (16 thay vì 17; 10 thay vì 11) — tiếng hô kiếm thuật, không phải rên, để nguyên chờ quyết; F2 1337 つっっっ→"quá" (audit đã flag chờ Hieu); F3 1366 lời ngọng chưa giải mã (audit đã flag chờ Hieu); F4 "Phu"/"phu" cho ふっ (1155, 1227) giữ không dấu — đợt thống nhất quyết có chuẩn hoá thành "phù" không.
