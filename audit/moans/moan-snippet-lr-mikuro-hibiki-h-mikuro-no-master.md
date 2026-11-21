# Moan-fix snippet — lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml (moan-lr-mikuro-hibiki-h-mikuro-no-master)

- File: `lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml` — route 02_Hibiki, 611 dòng script, TOML md5 `897021b35bb2e469b516f1f0d7b4274e` (khớp md5 audit), không có bản trùng.
- CSV3: 1 set duy nhất, 611 dòng, 0 key trùng; VN khớp TOML 611/611 sau chuẩn hoá `\n`→khoảng trắng (TOML-2 làm phẳng `\n`).
- Đã đọc 611/611 dòng; xét 415 dòng rên/SFX (260 っ, 42 fa/hya, 18 nguyên âm nhỏ, 11 cười, 76 SFX ngoặc, 8 nguyên âm dài).
- Đổi 31 dòng: 13 romaji + 16 đếm nguyên âm + 1 độ dài ん + 1 sai âm.
- Romaji fa/fu: 1711 ふぁう→"Fau" (bản cũ "fua" sai âm), 1712 ふぁ→"Fa" (+Ư gasp của audit), 1724/1725/1727/1728 ふあ→"Fua" (+Ư gasp của audit), 1729 ふあぁ…→"Fua" 14 a (bản cũ 17 a), 1741 ふや→"Fuya" (+Ư), 1743 ふあ→"Fua" (+Ư), 1786 ふあ→"Fua──Ư" (giữ dạng làm phẳng `\n` của audit), 1705 ふ……ぁ→"Fu……a", 1789 ふえ→"Fue" (bản cũ "Huê" sai phụ âm), 1821 あう→"Au" (bản cũ tách "A ư").
- Đếm nguyên âm (đếm lại độc lập bằng token): 1675 ひゃう×5→5 u (bản cũ 12 u), 1748 ひゅあ×7→7 a (bản cũ 21 a), 1757 ひゃあ→2 a, 1765 わぁ→2 a, 1768 わあ→2 a, 1819 ぁ+あ×18→19 a (bản cũ 51 a), 1855 んひゅう×8→9 u (bản cũ 18 u), 1864 んぅ×18→18 u (bản cũ 40 u), 1865 んきゅう→2 u, 1866 んきゅう×13→14 u (bản cũ 38 u), 1898 ぶはああ→3 a, 1917 はぁ→2 a, 2200 はあっ/ふうっ/はああっ/ふううっ→2a/2u/3a/3u, 2201 はあっ→2 a, 2202 はぁっ/はあっ×3→2 a mỗi hơi, 2559 (độc thoại) ああ→"Aa".
- Khác: 1604 んんっ→"ưmm" (2 mora ん, tiền lệ 凪h2); 1800 ふうっ→"Phùu!" (hơi thở 2 u, bản cũ "Hự!" là cách diễn của くっ).
- Kiểu lỗi chính: rên dài đếm nguyên âm sai (thừa gấp đôi/gấp ba hoặc thiếu 1 âm); audit (trước quy tắc romaji) đã Việt hoá romaji cũ thành "phà"/"phùa" — bản moan đưa 33 dòng fa/fu về romaji (11 đổi ở đây, 22 giữ bản cũ).
- Giữ 383 dòng rên/SFX (romaji đúng "Hyau/Hya/Hyua/Kua/Hau", cười "Fufu/Ufufu/Ưm fufu", SFX ngoặc dạng động từ Việt, gasp Ư của audit/sweep không đụng).
- Kiểm mà giữ: 1677 "Hyauuu" (3 u đúng), 1731 "Fuyaaaaaaan" (7 a đúng — audit §4 đếm sai "JP 6 âm a"), 1749/1863 "nnn" (không có công thức đếm ん), 2306 "////!?" (!? diễn cắt ngang).
- Sweep: 31 mục đã kiểm chứng qua audit (30 fix đã nhận + 2092 already-rendered) — không đụng.
- Cờ cho đợt thống nhất: HỦY 23 fix fa/fu của audit (giữ romaji cũ — xem REVIEW §5 mục 1, gồm 1857 chỉ hủy phần "Phùa", giữ phần nghĩa "vào hết"); audit §4 đếm sai 1731 (JP 7 âm a, không phải 6); 1800 đổi âm "Hự!"→"Phùu!" (lý do っ của audit vẫn đúng); 1743/1786 giữ dạng làm phẳng `\n` của audit.
- Lượt soát 2: tổng 32 ứng viên / tái kiểm chứng 32 / bỏ 1 (1753 no-op — VN cũ đã đúng 3 u) / sửa 0 — còn 31 fix. JSON 31 mục, khóa string, jp/tw/old_vn khớp CSV3 31/31. Khối TOML parse bằng tomllib: 31 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-mikuro-hibiki-h-mikuro-no-master-REVIEW.md`; danh sách sửa: `moan-lr-mikuro-hibiki-h-mikuro-no-master-wrong.json`.

**Tổng cộng sau file này: 6 file / 156 dòng sai (moan)** (cơ sở 5 file / 125 dòng + 31 file này)
- FLAG (đợt thống nhất): HỦY 23 fix fa/fu của audit — giữ romaji cũ (1678, 1708, 1714, 1716, 1718, 1720, 1722, 1731, 1733, 1735, 1736, 1737, 1739, 1758, 1773, 1811, 1820, 1857-chỉ phần "Phùa", 1901, 1928, 1967, 2107, 2198); chi tiết ở REVIEW §5.
