# Moan snippet — lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

- File: lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml (02_Hibiki, 485 dòng, audit 68 sai đã merge).
- Đọc toàn bộ 485/485 dòng; xét các dòng rên/SFX theo mẫu quét (họ はぁ/はあ 10, họ hya 9, họ fa/fu 16, cười 10, rên ngắn, hôn/mút 42, SFX （） 66, gasp 48).
- Đổi 15 dòng rên: 11 đếm nguyên âm (10 dòng はぁっ/はあっ thiếu 1 a: 933, 1385, 1389, 1422, 1423, 1505, 1740, 1741, 1742, 1743; 1475 audit đếm thiếu 1 u: "ryuu"→"ryuuu"); 2 mất âm (1334 やっ "Á"→"Ya", 1406 あぁ "ừm"→"aa"); 2 trộn 2 hệ trong một âm (1358 đuôi "ưm"→"nn" trong chuỗi romaji, 1440 "ư fufu"→"ufufu").
- Lỗi nặng nhất: họ はぁ/はあ thiếu 1 a ở 10 dòng (16 token); audit đã sửa gasp nhưng giữ "hà" 1 a.
- Kiểm chứng audit: 1357 (18 a), 1359 (9 a), 1447 (2 a), 1463 (11 a), 1328 (16 u), 1371 (6 a), 1446 (11 a), 1461 ("roooo"/"zuryuuu") đều đúng — giữ nguyên, không sửa lại.
- Gasp Ư của audit (48 dòng) không đụng; không dòng "Kh" nào bị đổi; SFX （） 66 dòng giữ nguyên theo quyết định audit §537.
- 5 giá trị moan xây trên fix audit (933, 1358, 1406, 1423, 1475) — áp thay fix audit ở đợt thống nhất; 10 giá trị còn lại xây trên VN cũ CSV3.
- Cờ: F1 quy ước ふっ ("Hư" file này vs "phù"/"fu" file khác); F2 độ dài SFX （） (2467 ngắn vs 2468 kéo dài); F3 2451 くっ→"Ư" trong （）; F4 1475 audit đếm sai (đã sửa bằng giá trị moan); F5 5 dòng chồng audit.
- Lượt soát 2: 15/15 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 15 mục dạng chuẩn, khóa string, jp/tw/old_vn khớp CSV3 15/15; khối TOML 15 khóa parse đúng, 0 sai lệch.

**Tổng cộng sau file này: 26 file / 576 dòng sai (moan)** (cơ sở 25 file / 561 dòng + 15 file này)
