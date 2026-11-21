# Moan-fix snippet — lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml (moan-lr-hiyoko-olivy-sex-no-obenkyou)

- File: `lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml` — route 11_Other, 441 dòng script, TOML md5 `bdb02933933db615a0380eb3839cd6de`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 441 dòng, 0 trùng khóa; TOML vs CSV3 khớp 441/441 (chỉ khác `\\n` literal → khoảng trắng, mẫu đã biết).
- Đọc 441/441 dòng, xét ~160 dòng rên/SFX, sửa 55 dòng, giữ ~105 dòng.
- Đổi 55 dòng: 19 họ fa/fu → romaji (Fua/Fuaa/Fuaaa/Fuaaaaaa/Pua), 9 họ ひゃ/ひゅ/ひあ/きゃ/や → romaji (Hia/Hyai/Hyagu/Nhyu/Ya/Yaa), 9 họ ん+X gộp romaji (Nku/Nchu/Nkyu/Nkyun/Nuu/Nuuuu/Nfuuuuuu/Fuuuuun), 7 họ ちゅ/れる/じゅ/ごちゅ → romaji (Chumu/Chuu/Chubu/Reru/Rero/Jubu/Jururuu/Zuji/Buchu/Gochu/Pechu), 7 dòng くっ → "Ku", 2 dòng か…… → "Ka", 1 dòng いっ → "I", 4 dòng sửa đếm nguyên âm (1409 1→4a, 1424 3→2a, 1773 phù 1→2u + Ahhh 3→2a, 2343 tách mảnh + 3a).
- Kiểu lỗi chính: bản cũ tách MỘT âm rên thành nhiều mảnh ("phù ah", "Ư hiu", "Ưm ư ư ư ư", "chụt ưm"), mất phụ âm mora (くっ→"ư", やっ→"Ư", いっ→"Ư", か→"Kh"), sai đếm nguyên âm ("Ahhh" cho 2a, "Cứuu…" cho 13u).
- Trùng fix audit 2 khóa (2331, 2426): 2331 "Pua" ghi đè "phù ah" của audit (audit sửa "phụt"→"phù ah"); 2426 giữ "Ư" + đếm 13u của audit, chỉ đổi いっ "Ư"→"I". Không hủy toàn bộ fix audit nào. 0 key trùng sweep gasp đã sửa (1301/1554/1591/1925/2099/2166 do audit sửa, không đụng); không dòng "Kh" cho っ nào bị đổi.
- Sweep: 6 mục — 1301/1554/1591/1925/2099/2166 đã sửa (không đụng); 2146 っっ――→"ư——" giữ nguyên (gasp đã diễn bằng Ư).
- Giữ ~105 dòng rên/SFX (kiểu ふむ→"Hừm", んっ→"Ưm", あっ/はっ→"Ah/Ha", ふっ→"Phù", cười ふふっ→"Fufu", SFX ngoặc diễn thành động từ VN "Tách ra/Nắn bóp/Phập/Nhóp nhép/Trượt vào/Ngoạm/Ực"; ふえっ→"Hể!?" giữ; 1369 giữ diễn nghĩa).
- Cờ cho đợt thống nhất: F1 んうっ "Ưm" (ngắn) vs romaji "Nu/Nuu" (dài); F2 ふっ "phù" vs "Fu"; F3 SFX miệng/lưỡi trong thoại → romaji vs động từ VN (ranh giới với SFX ngoặc); F4 べろおおおおっっ → "Berooooo" vs "liếm liếm liếm liếm"; F5 ひっ、ぐっ → "Hi, gu" vs "Hức, hức"; F6 1655 ひよこぉ/もっとぉ mất độ dài ぉ (không sửa); F7 1369 giữ diễn nghĩa SFX hành động trong câu; F8 trùng audit 2331/2426 (xem trên); F9 あっ "Ah" vs "A"/"Á"; F10 2146 っっ――→"ư——" giữ (sweep không bao phủ).
- Lượt soát 2: tổng 55 / tái kiểm chứng 54 / bỏ 0 / sửa 1 (2437: "Fukyuuuuuuu" 8u → "Fukyuuuuuuuu" 9u). JSON 55 mục, khóa string, jp/tw/old_vn khớp CSV3 55/55. Khối TOML parse bằng tomllib: 55 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hiyoko-olivy-sex-no-obenkyou-REVIEW.md`; danh sách sửa: `moan-lr-hiyoko-olivy-sex-no-obenkyou-wrong.json`.

**Tổng cộng sau file này: 42 file / 1080 dòng sai (moan)** (cơ sở 41 file / 1025 dòng + 55 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
