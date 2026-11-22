# Moan-fix snippet — 真闇h2_無濾過.txt.toml (moan-mayamih2-muroka)

- File: `05_Mayami/真闇h2_無濾過.txt.toml` — H-scene Mayami "rượu không lọc" (nếm thử shochu không lọc, quan hệ bằng mông); 316 dòng, audit sai 17 (7 gasp, 1 đại từ, 1 nghĩa, 4 fa/fu, 3 nguyên âm, 1 romaji).
- Đọc 316/316 dòng, xét 249 dòng có dấu hiệu âm thanh, đổi 28 dòng.
- fa/fu → romaji (4): 1040, 1058, 1088 ふあっ→"Fua"; 1117 ぷあっ→"Pua" — tiền lệ lr_日々姫h2 (tất cả ふあっ→Fua) + 日々姫h3 (ぷあ→Pua); audit đã đổi "phua"→"phùa", moan-fix này chuyển tiếp sang romaji.
- くっ → "Ku" (4): 1056 「くっ！」→"Ku!", 1085/1086 「くっ――」→"Ku――", 1092 「ん――くっ」→"Ưm――ku." — tiền lệ 凪h1 (くっ trong thoại → "Ku"); "Ư" làm mất phụ âm k-.
- Cười んふふ → "Nfufu" (3): 1027, 1029, 1031 — tiền lệ Mayami h3 key 2352 ("Ufufu" mất ん đầu).
- あふ → "Afu" (1): 1010 あふっ "aphu"→"Afu" — tiền lệ ハチロクh2 key 966; "aphu" lai romaji + Việt trong một âm.
- ちゅっ khôi phục っ (1): 1029 ちゅっちゅっちゅっ "chu chu chu"→"chụt chụt chụt" (mất っ cả 3 lần).
- Đếm nguyên âm — ちゅう (3): 1075, 1078, 1450 ちゅう "chu"→"chuu" (2u; tiền lệ Mayami h3 key 2330).
- Đếm nguyên âm — chụt (1): 1844 ちゅっうっ "Chụt"→"Chụụt" (2ụ; tiền lệ ハチロクh3 key 1813).
- Kéo dài phụ âm t (2): 1142 くう…ぅ… (14u) 13t→14t — audit đếm thiếu âm u của く (đúng lỗi lớp h3 1063); 1884 ずろお… (9o) 5t→9t. Giữ kiểu t-stretch, chỉ sửa đếm — cờ F3.
- SFX dài → romaji (8): 1820 ずぶ+7う→"Zubuuuuuuuu!" (9u); 1823 ずる+8う→"Zuruuuuuuuuu" (10u); 1832 くぱ+2あ→"Kupaaa" (3a); 1834 むりゅ+6う→"Muryuuuuuuuu!" (8u); 1837 むに+3い→"Muniiii" (4i); 1846 きゅ+4う→"Kyuuuuu" (5u); 1848 きゅ+5う→"Kyuuuuuu!" (6u); 1872 ぬと+4お→"Nutooooo" (5o).
- Đếm lặp SFX (2): 1822 ぎち×6 → 6 "Siết" (cũ 5); 1882 キチ×6 → 6 "Siết" (cũ 5).
- Giữ nguyên: gasp Ư của audit (827/1158/1208/1209/1210/1211/1213) không đụng; họ ひゃ đã romaji đúng (16 dòng); ふっ "Phư" (1032, 1084) + ふうっ "phuu" (1005) giữ theo Mayami h3 (cờ F1); んふっ "Ưm phư" (1061, 1105) giữ theo Mayami h3; họ ちゅ đã chuẩn (1077/1083/1103/1819/1827/1829/1845); ああ→"A a" (1076, 1836) giữ theo h3; SFX ngắn diễn nghĩa Việt đã đúng (1817/1821/1824/1826/1828/1830/1831/1833/1835/1838/1839/1849/1850/1852/1856–1860/1862/1863/1867–1871/1873–1875/1883); audit fix đếm nguyên âm đã đúng (1017 5i, 1083 3u, 1121 7i, 1198 3u).
- Cờ đợt thống nhất: F1 ふっ "Phư"/"Phù" vs "Fu" (Mayami h3 giữ ph- vs 日々姫h3 F2 Fu); F2 くっ thoại "Ku" (凪h1) vs "hự" (h3 1089) vs "Ngoáy" (h3 1815); F3 kiểu t-stretch (1142/1884 — lr_日々姫h2 F1, 凪h1 cờ); F4 んふふ "Nfufu" vs "Ufufu" + hoa/thường; F5 ngưỡng SFX dài → romaji (1832 くぱああ 3a); F6 họ きゅ ngắn diễn nghĩa vs dài romaji; F7 1861 ぱくっ→"Phập!" giữ theo ngữ cảnh (vs h3 "Ngoạm"); F8 1005 ふうっ→"phuu" giữ.
- Sweep gasp kiểm tra trực tiếp 7/7 mục — tất cả nằm trong audit (gasp), không có mục nào thuộc moan-fix này; không đụng dòng gasp Ư nào; không đổi dòng "Kh" nào.
- Lượt soát 2: 28/28 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `6a7e62c050273bbf93e38135c93f7f15`; CSV3 1 bộ 316 dòng, 0 key trùng; khối TOML 28 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 62 file / 1475 dòng sai (moan)** (cơ sở 61 file / 1447 dòng + 28 file này) [REBASE 22/11 ~10:38 — snippet ghi cơ sở cũ 60/1418 vì 日々姫h4 (29 dòng) đã gộp trước trong cùng đợt; parent đã gộp 日々姫h4, GitHub 3d6eae6c là cơ sở trước]
