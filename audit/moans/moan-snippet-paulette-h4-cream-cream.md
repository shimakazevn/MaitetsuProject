# Moan-fix snippet — ポーレットh4_クリーム＆クリーム.txt.toml (moan-paulette-h4-cream-cream)

- File: `ポーレットh4_クリーム＆クリーム.txt.toml` — route 03_Paulette, 265 dòng script, TOML md5 `64abe8098966360371870067cd0d2843`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 265 dòng; TOML vs CSV3 khớp 265/265 (146 dòng chỉ khác `\n` literal → khoảng trắng, mẫu đã biết).
- Đọc 265/265 dòng, xét 123 dòng rên/SFX (83 thoại + 40 SFX ngoặc), sửa 44 dòng, giữ 79 dòng.
- Đổi 44 dòng: 18 họ fa/fu → romaji (Fua/Fuya/Funyaa/Fuhya/Pua), 12 họ ひゃ/ひゅ/ひあ/きゃ → romaji (Hya/Hyu/Hia/Kya/Nhyu...), 13 họ ん+phụ âm/nguyên âm dài → romaji gộp (Nkyu/Nmyu/Na/An/Nuu/Nuuuuuu...), 6 họ ちゅ → romaji (Chumu/Churo/Churu/Chuu...), 4 dòng やっ → "Ya", 8 dòng sửa đếm nguyên âm (881: 12→11u; 911: 10→11a + thêm n; 1008: 11→12a; 901/970: 1→2a; 896/932: phù→Phùu; 908: Hà→Haa).
- Kiểu lỗi chính: bản cũ mất phụ âm mora (ひゅ/きゅ/や/か/が/く → "Á"/"a"/"Ưm"/"đang"), tách một âm rên thành nhiều mảnh ("Ưm hya", "Ưm ááá"), và diễn ふあ thành "phù" sai nguyên âm.
- Trùng fix audit 11 khóa (859, 881, 882, 884, 901, 903, 906, 911, 914, 952, 970): 10 fix "romanisation" của audit (chuyển romaji về VN) bị moan sửa/hủy theo quy tắc romaji — trong đó 882/884 giá trị moan = VN cũ (hủy fix audit); 906/914/970 giữ phần không-phải-rên của audit (đại từ, nói ngọng), chỉ đổi token rên.
- Sweep: 4 mục — 1030/1632/941 đã sửa (không đụng); 896 "already-rendered" (chuỗi っ cuối 6 ư vs 7 っ giữ nguyên theo sweep).
- Giữ 79 dòng rên/SFX (kiểu "Hyan!"/"Hyaaa" đã đúng romaji; "hự" cho grunt Soutetsu; "phù" cho ふっ — h7 F7 vẫn mở; SFX ngoặc diễn thành động từ VN "Phập/Phụt/Siết/Nắn bóp"; "chụt" cho ちゅっ thuần).
- Cờ cho đợt thống nhất: F1 họ く Ku vs Hự vs Ư; F2 ん+phụ âm romaji gộp vs "Ưm"; F3 ふっ "phù" vs "Fu"; F4 họ ちゅ "chụt" vs romaji (1594 giữ "chụt" trong SFX ngoặc vs 930 "Churu"); F5 gasp sweep chưa bao phủ — 1010 っ đứng riêng đã thêm "Ư" (cần xác nhận), 932 ～っ đầu dòng giữ "～"; F6 897 きちゃう→"chạm vào" là lỗi nghĩa, KHÔNG sửa (cần vòng audit); F7 896 chuỗi っ 6 ư vs 7 っ; F8 10 fix romanisation của audit bị moan thay thế; F9 họ ふ "F" vs "ph" (file này theo h7 809: Fuya/Fua); F10 1594 vs 930 cùng âm ちゅるっ hai cách diễn.
- Lượt soát 2: tổng 44 / tái kiểm chứng 44 / bỏ 0 / sửa 0. JSON 44 mục, khóa string, jp/tw/old_vn khớp CSV3 44/44. Khối TOML parse bằng tomllib: 44 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h4-cream-cream-REVIEW.md`; danh sách sửa: `moan-paulette-h4-cream-cream-wrong.json`.

**Tổng cộng sau file này: 41 file / 1025 dòng sai (moan)** (cơ sở 40 file / 981 dòng + 44 file này — REBASE: cơ sở lúc spawn là 39/962, nhưng ふかみh2_homesweethome (19 dòng) đã gộp lúc 21/11 ~22:50 trong khi làm file này, nên tổng hiện tại của ROUTE-MOANS.md là 40/981)
- FLAG (đợt thống nhất): F1–F10 ghi lại trong snippet (F6 897 きちゃう→"chạm vào" là lỗi nghĩa — agent đã flag, không tự sửa; F8 882/884 hủy fix audit của audit — giá trị moan = VN cũ).
