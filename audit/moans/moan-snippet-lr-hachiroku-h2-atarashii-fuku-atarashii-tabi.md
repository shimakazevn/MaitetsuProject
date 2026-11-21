# Moan-fix snippet — lr_ハチロクh2_新しい服。新しい旅.txt.toml (moan-lr-hachiroku-h2-atarashii-fuku-atarashii-tabi)

- File: `lr_ハチロクh2_新しい服。新しい旅.txt.toml` — route 01_Hachiroku, 327 dòng script, audit trước đó 63 sai.
- TOML md5: `7b0a3c5d1db89046c9b50bee2ff0e6f5` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 327 dòng, 0 key trùng; TOML vs CSV3 khác 173 key (chỉ `\n` flatten thành khoảng trắng).
- Đã đọc 327/327 dòng; xét 133 dòng rên/SFX (họ fa/fu 17, họ ひゃ/ひあ/ひゅ 5, gasp Ư 32, cười 7, chuỗi hơi thở 24, chuỗi SFX miệng 8, SFX độc thoại 29, khác 11).
- Đổi 20 dòng: 18 romaji + 1 sai âm + 1 gasp.
- Romaji fa/fu → Fa/Fua (Hepburn chặt, đúng 14 dòng audit §9.1 đã cờ): 1410 ひあっ→"Hia" + ふあっ→"Fua", 1424/1427/1432/1433/1440 ふぁ→"Fa", 1429/1434/1436/1438 ふあっ→"Fua", 1425 ふぁ→"Fa" + ふぁぁ→"Faa", 1428 ふぁああああん→"Faaaaan" (5 a), 1442 ふぁああっ→"Faaa" (3 a), 1443 ふぁぁああああっ→"Faaaaaa" (6 a).
- Romaji gộp mảnh rời: 1453 うぁあああ→"Uaaaa", 1466 あむっ→"Amu" + れろおおっ→"Rerooo" (3 o) + はむっ→"Hamu" ×2, 1473 ぁうっ→"Au", 1715 れるううううううっ→"Reruuuuuuu" (7 u, chỉ đổi phần trong ngoặc).
- Sai âm: 1484 くっ→"Ku" (tiền lệ Paulette h3 906; audit từng giữ "Ưm" — cờ F1).
- Gasp: 1567 ぁっ cuối tuyệt đối dòng 1→"aƯ" (audit sót, cùng mẫu §2b).
- Giữ 113 dòng rên/SFX: 29 gasp Ư sweep/audit + 3 already-rendered, 7 cười audit đã sửa, 1495/1496 đếm đúng, 24 chuỗi hơi thở mềm, 8 chuỗi SFX miệng, 29 SFX độc thoại 2166–2210 theo quy ước file, ふーっ "Phù" (1905/2056), 1449 ふえっ→"Hả!?", すずっ→"Suzu".
- Quy tắc họ ひゃ (21/11 ~11:55) đã kiểm chứng: không còn dòng "Á" nào cho ひゃ/ひゅ/ひあ/きゃ trong dòng rên (1407/1408/1411 "Hyau", 1410 "Hia", 1429 "Ahyu", 1496 "hyuuuuuuu").
- 6 key trùng audit chỉ khác đúng token rên (1410, 1424, 1429, 1433, 1436, 1440) — áp MỘT giá trị moan mỗi key.
- Sweep: 20 mục đã kiểm chứng trực tiếp — 17 fix Ư của audit giữ nguyên, 3 already-rendered giữ. Không dòng "Kh" nào bị đổi.
- Flag: F1 1484 (くっ→"Ku" vs audit giữ "Ưm"); F2 chuỗi SFX miệng "chụt" vs romaji (1475/1476/1479/1481/1715); F3 gasp っ―― (1582, 1589); F4 SFX độc thoại 2166–2210; F5 Fa/Fua chặt vs h8; F6 1473.
- Lượt soát 2: tổng 20 / tái kiểm chứng 20 / bỏ 0 / sửa 0 (kiểm tra đếm bằng máy bắt 1 lỗi 1428 thừa 1 a, đã sửa trước lượt soát 2).
- TOML block: parse-verified (tomllib), 20 key, 0 value mismatch vs wrong.json.
- Chi tiết đầy đủ: `moan-lr-hachiroku-h2-atarashii-fuku-atarashii-tabi-REVIEW.md`; danh sách sửa: `moan-lr-hachiroku-h2-atarashii-fuku-atarashii-tabi-wrong.json`.

**Tổng cộng sau file này: 14 file / 338 dòng sai (moan)** (cơ sở 13 file / 318 dòng + 20 file này — cơ sở kiểm chứng lại từ ROUTE-MOANS.md trước khi viết snippet: file 凪ふかみh1 26 dòng đã được merge trong lúc làm file này, nên cơ sở đổi từ 12/292 lúc nhận việc thành 13/318)
