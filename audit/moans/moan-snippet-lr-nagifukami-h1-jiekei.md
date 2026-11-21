# Moan-fix snippet — lr_凪ふかみh1_じぇいけい！.txt.toml (moan-lr-nagifukami-h1-jiekei)

- File: `lr_凪ふかみh1_じぇいけい！.txt.toml` — route 07_Nagi_Fukami, 404 dòng script, TOML md5 `ef960cfc3776057ff0cbcad101eb4875` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 404 dòng, 0 key trùng; VN khớp TOML 404/404 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 404/404 dòng; xét 229 dòng rên/hơi thở/SFX.
- Đổi 34 dòng: 21 romaji + 12 đếm nguyên âm + 1 sai âm.
- Romaji họ fa/fu (21): 1479, 1481, 1505, 1509, 1510, 1512, 1513, 1522, 1523, 1532, 1581, 1583, 1590, 1595, 1597, 1598, 1603, 1619, 1657, 1658, 1714 — ふあ→Fua, ふぁ→Fa; đổi ngược token fa/fu audit đã đổi thành "Phà" (romaji fallback Hieu 21/11 ~01:56, tiền lệ file mẫu 凪ふかみh1). 1502/1505 khôi phục "Fu……a——" (ふ……ぁ là hai âm riêng, audit gộp sai).
- Đếm nguyên âm (12): 1477 Hyuaaa (3 a), 1483 Hyuaaaaaaan (7 a + n), 1491 Hyuaaaaaan (5 a + n), 1507 Haa/fuu, 1552 Nfufuun, 1574 Haa——, 1599 Haa ×4, 1614 Haa ×4, 1677 haa + 8 a + n, 1695 Haa ×2, 1789 Aa, 1485 auu.
- Sai âm (1): 1502 ふ……ぁ audit gộp thành "Phà" → khôi phục "Fu……a——".
- Giữ 195 dòng rên/SFX: gasp Ư (audit, 15), họ ひゃ đã romaji (1475/1476/1484/1488/1490/1521…), くっ→"Hự", んっ→"Ưm", cười Fufu/Ufufu, SFX liếm/mút kiểu động từ Việt, はうっ "Hau" (1587/1841), nói ngọng 1375/1545/1550 (audit).
- Sweep: 17 mục đã kiểm chứng — 13 fix + 1624 đã vào audit, 3 already-rendered đúng, 1838 đã diễn âm; không đụng mục nào.
- Audit: 22 key trùng audit, fix chỉ khác đúng token rên (difflib); 12 key fix == old_vn (CSV3) vì đổi ngược đúng token audit đã đổi. Lượt soát 2: tổng 34 / tái kiểm chứng 34 / bỏ 0 / sửa 1 (1491: 6 a → 5 a). JSON 34 mục, khóa string, jp/tw/old_vn khớp CSV3 34/34. Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-nagifukami-h1-jiekei-REVIEW.md`; danh sách sửa: `moan-lr-nagifukami-h1-jiekei-wrong.json`.

**Tổng cộng sau file này: 16 file / 375 dòng sai (moan)** (cơ sở 15 file / 341 dòng + 34 file này)
