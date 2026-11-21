# Moan-fix snippet — 真闇h3_補習授業の廃校舎 (moan-mayami-h3-hoshuu-jugyou)

- File: `真闇h3_補習授業の廃校舎.txt.toml` — 710 dòng script, TOML md5 `679f382102d8ec0738d3e2eb97494730`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 710 dòng, 0 key trùng (428 lệch VN↔TOML đều do TOML-2 flatten `\n` thành khoảng trắng — CSV3 là chuẩn).
- Đã đọc 710/710 dòng; xét 277 dòng ứng cử viên (233 quét mẫu rên/SFX + 44 quét bổ sung); xác định 145 dòng rên/SFX.
- Đổi 42 dòng: 23 romaji + 14 đếm nguyên âm + 4 sai âm (mất phụ âm mora) + 1 gasp.
- Romaji: 2182 `Hiau!?`, 2184 `Hyaaaan` (4a+1n), 2198 `reroooo`/`rerooooo`, 2199 `Hihahahihafu`, 2208/2307/2308 `Ua`, 2212 `aaa`, 2215 `fau`, 2227 `Hau` + `ưmm`, 2270 `Aa`, 2271 `Aaa`, 2272 `Aaaaaaaa` (8a), 2273 `Aaaaaa` (6a), 2274 `Aaa!` (trên giá trị audit), 2277 `Hau`, 2278 `Nkyuuuuuuuuuuuun` (12u+2n), 2305 `Ku――uu!`, 2310 `Fuaaaaaaaannn` (8a+3n), 2311 `aaaaaa` + `Nuuu`, 2312 `Aaa` + `Ưmm`, 2334 `ưmm`, 2346 `Nhyuuuuuuuuuuu` (11u), 2355 `Nuuuuuuuuuuu` (11u).
- Đếm nguyên âm: 2211 `Sou-chaaan` (3a), 2218 `Haa` (2a), 2225 `Haa! Haa! Haa!`, 2268/2269 `Aa――`, 2288 `chuuuuuu` (6u), 2295 `Chuuuuuu` (6u), 2300 `Aa.`, 2306 `Sou-chaan` (2a), 2330 `chuu……` (2u), 2472 `Sou-chann!` (2n), 2776 `Haaa` (3a), 4019 `Guuuu!` (4u).
- Sai âm: 2249 `Ka――` (khôi phục k của か――), 2352 `Nfufu` (んふふ, tiền lệ 1457), 2363 `churu` (ちゅるっ, khôi phục mora る), 2686 `Nuu` (ぬ――, khôi phục n).
- Gasp: 3967 `（Ư――Phập――）` — っ đầu dòng trong ngoặc bị mất hẳn, sweep bỏ sót (8 mục sweep cho file này đều đã đúng, audit đã áp dụng).
- Kiểu lỗi chính: tách một âm rên duy nhất thành nhiều mảnh rời + diễn lai romaji–tiếng Việt trong một âm; đã gộp về một cách diễn romaji thuần, đếm nguyên âm kiểm chứng bằng script.
- Giữ 103 dòng rên/SFX (họ ひゃ đã romaji, họ ふぁ/ふあ "Fua/fua" nhất quán toàn file, あっ "Á"/"A", はっ "Há", ふっ "phù"/"phư", んっ "Ưm/ưm", ん+X "Ưmpu/Ưnmu/Ưmbu", cười "Ufufu/Nfufu", SFX chuỗi miệng romaji, SFX ngoặc dạng nghĩa Việt, tách âm theo dấu 、 của JP, っ nhấn mạnh cuối từ nội dung không thêm Ư, grunt diễn ngôn).
- Trùng audit: 2274 + 2308 chỉ thay đúng 1 token rên trong giá trị audit (giữ "đầy ắp" và thứ tự từ audit sửa); các fix audit khác có yếu tố moan (1554, 2194, 2665, 2694, 2889/2890/2891, 3114/3264/3965) đều đúng, không đụng. Không dòng "Kh" nào bị đổi (file không có rendering "Kh").
- Cờ cho đợt thống nhất: F1 んっ "ưm" vs "ưn" (2323/2328); F2 ふっ "phù" vs "phư"; F3 SFX ngoặc chưa áp công thức đếm (4014/4016/4042/4043); F4 んんっ "ưmm" vs "nn"; F5 2898 nói ngọng miệng đầy (không phải rên, để audit); F6 2107 はぁい bị bỏ; F7 2199 cười ngọng (đã sửa, chờ parent xác nhận phân loại); F8 2300 "Aa." vs ああ diễn ngôn giữ "A,".
- Lượt soát 2: tổng 42 / tái kiểm chứng 42 / bỏ 0 / sửa 0. JSON 42 mục, khóa string, jp/tw/old_vn khớp CSV3 42/42. Khối TOML parse bằng tomllib: 42 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-mayami-h3-hoshuu-jugyou-REVIEW.md`; danh sách sửa: `moan-mayami-h3-hoshuu-jugyou-wrong.json`.

**Tổng cộng sau file này: 45 file / 1214 dòng sai (moan)** (cơ sở 44 file / 1172 dòng + 42 file này — REBASE: cơ sở lúc spawn là 43/1114, nhưng một file khác (58 dòng) đã gộp vào ROUTE-MOANS.md trong lúc làm file này, nên tổng hiện tại là 44/1172)
