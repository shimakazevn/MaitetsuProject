# Moan-fix snippet — lr_ふかみh1_ふかみうさぎのたまご.txt.toml

- File: `lr_ふかみh1_ふかみうさぎのたまご.txt.toml` — 289 dòng script, TOML md5 `978b35d98d620183d1a58aa3aaa8eda0`, không có bản trùng.
- CSV3: 2 bộ — bộ home `07_Nagi_Fukami` cũ (khớp TOML 3/289), bộ `11_Other` tốt (khớp 289/289 về nội dung, đã dùng bộ này).
- Đã đọc 289/289 dòng; xét 111 dòng rên/SFX theo mẫu quét (64 thoại + 47 SFX trong ngoặc) + các dòng rên lẻ đọc tay.
- Đổi 33 dòng: 21 romaji fa/fu + 9 đếm nguyên âm + 1 mất tiếng thở (1196) + 1 sai âm (1280) + 1 mất độ dài (1432).
- Romaji: 1223/1379/1458 `Fu, a`; 1233/1268/1457/1464/1467/1468/1469/1471 `Fa`; 1252/1254 `Fue?`; 1267/1270/1283/1461/1463/1472 `Fua`; 1460 `Fau`; 1465 `Fuaa`. Không còn dòng fa/fu nào diễn "phà"/"phù" trong file.
- Đếm nguyên âm: 1224 `Hyua`+17a, 1279 `Kyafu`+8u, 1310 `Y`+16u, 1920 `Guch`+14u, 1949 `Kyuuuu`, 1966 `Kyuuuuuuu`, 1967 `Kyuu`/`Kyuun`, 1968 `Kyun`, 1655 `kyun kyun` (audit bỏ sót).
- Mới so với audit: 1280 `Hiu` (mất glide u), 1432 `aa!!` (mất 1 âm a), 1655 `kyun kyun` (thừa u).
- Giữ ~82 dòng rên/SFX (kiểu "A"/"Ua"/"Kua" cho あっ/うあっ/くあっ, "Hyau" cho ひゃう, "Ưm" cho んっ, "Ha" cho はっ/はぁっ, cười "Ehehe", SFX ướt "Sùng sục/Phụt/Cụp", tiếng gắng sức "dô, ta").
- Sweep: 13 mục đã kiểm chứng ở audit; 16/17 dòng gasp Ư không đụng (1268 chỉ đổi phần fa, giữ Ư của audit). Không dòng "Kh" nào bị đổi.
- Ghi chú đợt thống nhất: 3 dòng tách nhịp ふ、ぁ/ふ、あ (1223/1379/1458) diễn "Fu, a" theo cách đọc 2 nhịp; 1460 ふぁぅ → "Fau"; 9 dòng đếm nguyên âm + 1196 áp nguyên giá trị audit — áp MỘT giá trị moan mỗi key, không áp cả hai.
- Lượt soát 2: tổng 33 / tái kiểm chứng 33 / bỏ 0 / sửa 0. JSON 33 mục, khóa string, jp/tw/old_vn khớp CSV3 33/33. Khối TOML parse bằng tomllib: 33 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-fukamih1-fukami-usagi-no-tamago-REVIEW.md`; danh sách sửa: `moan-lr-fukamih1-fukami-usagi-no-tamago-wrong.json`.

**Tổng cộng sau file này: 5 file / 125 dòng sai (moan)** (cơ sở 4 file / 92 dòng + 33 file này)
