# Moan-fix snippet — ハチロクh7_レトロモダンメイクラヴ.txt.toml (moan-hachiroku-h7-retro-modern-meikuravu)

- File: `ハチロクh7_レトロモダンメイクラヴ.txt.toml` — route 01_Hachiroku, 435 dòng script, TOML md5 `826355d088615a39f35716717fda637e` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 435 dòng, 0 key trùng; VN khớp TOML 435/435 sau chuẩn hóa `\n`/khoảng trắng.
- Đã đọc 435/435 dòng; xét 209 dòng rên/SFX (104 thoại + 21 độc thoại có tiếng rên + 84 SFX trong ngoặc).
- Đổi 18 dòng: 17 romaji + 1 đếm nguyên âm (839 ひきゅうっ "hikyu"→"Hikyuu", thiếu 1 u).
- Romaji fa/fu chưa tách → Fa/Fua (10): 692, 731, 743 (×2), 759, 796 (ふぁっ→"Fa"), 812, 813, 819 (ふぁああああん 5 a→"Faaaaaan"), 823, 971. Dùng Hepburn chặt Fa (ふぁ) / Fua (ふあ) — khớp đa số tiền lệ (凪h2, lr-h2, lr_ふかみh1, lr-h1 vừa gộp) và cờ F4 của lr-h1.
- Romaji mất phụ âm/glide — audit bỏ sót (7): 485 く→"Ku", 690 ひゅぎゅ→"Hyugyu", 711 ひゃっ→"Hya", 745 ぐっ→"Gu" (TW 咕 ủng hộ; giữ "Ka" + "ưn kyuuu" của audit), 750 ふきゅん→"Fukyun" (ふ=f, không phải h), 836 んひゅん→"Nhyun", 837 んひゅっ→"Nhyu".
- 11 key trùng audit — fix moan thay thế fix audit ở đúng token rên (áp MỘT giá trị mỗi key); 7 key mới so với audit (485, 690, 711, 750, 836, 837, 839).
- Giữ 191 dòng rên/SFX: dạng tách fa "phù——a"/"phù, a" (11 dòng: 485, 694, 763, 787, 802, 816, 821, 837, 853, 968, 971) theo tiền lệ audit đã chốt trong file (763 §2.1); gasp Ư khóa (12 fix sweep/audit) không đụng; SFX độc thoại kéo dài theo tỉ lệ file (audit §5: 1811, 1826, 1829, 1854/1857, 1866, 1930, 1941) giữ nguyên — đã rà lại 1820 (16う → 20p, tỉ lệ 1,25×, giữ); họ ちゅう(っ) giữ "chụt"/"chùn chụt" (793, 1852, 1858, 1867, 1880); đếm nguyên âm của audit kiểm chứng lại độc lập bằng máy đều đúng (736, 842, 843, 844, 845, 759, 819).
- Sweep: 14 mục đã kiểm chứng — 12 fix Ư áp nguyên qua audit + 759/763 sửa lại theo quy tắc gasp; không dòng "Kh" nào (file không có dòng "Kh").
- Cờ cho đợt thống nhất: dạng tách fa 11 dòng (romaji "Fu——a" như h9 hay giữ "phù——a"?); họ ちゅう(っ) ("chuu" theo công thức hay giữ "chùn chụt"?); SFX độc thoại chưa áp công thức đếm (1840, 1818, 1868, 1883, 1929, 1931–1933, 1873, 1876, 1919, 1928, 1835, 1850, 1903); 1831 （ふわっ → "Nhẹ nhàng", mất âm "Fuwa"); đề xuất "rộp" cho họ れる/るっ/れろ (audit flag, vẫn chờ Hieu); 745 ぐっ→"Gu" vs "Khục" (tiền lệ 1833).
- Lượt soát 2: tổng 18 / tái kiểm chứng 18 / bỏ 0 / sửa 0. JSON 18 mục, khóa string, jp/tw/old_vn khớp CSV3 18/18. Khối TOML parse bằng tomllib: 18 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hachiroku-h7-retro-modern-meikuravu-REVIEW.md`; danh sách sửa: `moan-hachiroku-h7-retro-modern-meikuravu-wrong.json`.

**Tổng cộng sau file này: 12 file / 292 dòng sai (moan)** (cơ sở 11 file / 274 dòng + 18 file này)
