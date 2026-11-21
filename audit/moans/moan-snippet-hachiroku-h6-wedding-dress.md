# Moan-fix: ハチロクh6_ウェディングドレスを脱ぎ捨てて (moan-hachiroku-h6-wedding-dress)

- File: `01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml` — 461 dòng script, audit trước đó 16 sai (3,5%), không key nào trùng audit.
- Đã đọc 461/461 dòng; kiểm kê rên/SFX: 254 dòng (131 thoại + 123 độc thoại, chủ yếu SFX ngoặc).
- Đổi 58 dòng: 46 romaji + 12 đếm nguyên âm; giữ 196 dòng.
- Họ fa/fu chưa tách → romaji: 14 dòng (829, 830, 831, 832, 852, 863, 881, 884, 915, 930, 941, 948, 950, 1020) — "phù a"/"phù" → Fua/Fa/Pua; dạng tách (ふ、ぁ / ふ……ぁ) giữ nguyên.
- Họ ひゃ/ひゅ/ひあ/きゃ → romaji: 13 dòng (812, 821, 842, 843, 845, 847, 849, 854, 924, 925, 926, 937, 940) — "Á"/"Hí a"/"Ưm hứ" → Hya/Kya/Hia/Hiu/Hyua/Hyau/Nhyu/Nhyun/Kahyu.
- Họ く/くあ/んくっ → romaji: 12 dòng (513, 514, 872, 874, 882, 887, 897, 904, 909, 935, 939, 1052) — "Hự"/"Ưm"/"ư" → Ku/Kuu/Kua/Ưm ku.
- や/あん/んぁ/ぃあ/ふきゅ/ちゅう/じゅう → romaji: 7 dòng (530, 816, 869, 871, 824, 838, 934) — Ya/Iaaaan/An/Fukyu/Chuuu/Juuu.
- Đếm nguyên âm: 12 dòng (819, 844, 929, 946, 839, 932, 856, 865, 866, 875, 1335, 1963) — chuỗi dài đếm lại bằng máy (819: 10u/2n; 844: 13u/5 ưm; 946: 18u).
- Không đụng dòng gasp Ư nào; file không có dòng "Kh"; 2 lỗi đánh máy "nhà"→"hà" cho はっ/はぁっ (881, 948).
- Lượt soát 2: tổng 58 / tái kiểm chứng 58 / bỏ 0 / sửa 0. JSON 58 mục, khóa string, jp/tw/old_vn khớp CSV3 58/58; khối TOML parse bằng tomllib: 58 khóa, 0 sai lệch.
- Cờ cho đợt thống nhất: F1 くっ "Ku" vs "Hự" (grunt, các dòng 513/882/897/935); F2 839 ひ、ぐっ ("Hi, gu" vs "Hức, hức"); F3 SFX ngoặc （） dạng động từ Việt; F4 2034 (くくっ）→（Kéo） lỗi nghĩa (thuộc audit); F5 ghi chú 1163 ひょっ trong ROUTE-AUDIT.md không thuộc file này (key 1163 không tồn tại); F6 931 "chùn chụt" giữ, ranh giới với 838/934.
- Chi tiết đầy đủ: `moan-hachiroku-h6-wedding-dress-REVIEW.md`; danh sách sửa: `moan-hachiroku-h6-wedding-dress-wrong.json`.

**Tổng cộng sau file này: 44 file / 1172 dòng sai (moan)** (cơ sở 43 file / 1114 dòng + 58 file này — đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
