# ROUTE-MOANS — H-scene moan fixes (romaji fallback)

Merged moan-fix log. Running totals: **55 files / 1346 rows changed**.

Rule (Hieu approved 21/11 ~01:56): when a Vietnamese rendering of a moan/breath sounds ngượng, use romaji of the JP sound instead. Ư gasp rows are NOT revisited. "Kh" for glottal-stop っ KEEPS. One row = one rendering (VN or romaji, never mixed).

Fixes here are amendments — applied with the unification pass (after all 216 audits finish), NOT by editing TOML directly now.

---

---

# Moan-fix snippet — ふかみh1_ともはり練習 (moan-fukamih1-tomohari-renshuu)

- File: `ふかみh1_ともはり練習.txt.toml` — 272 dòng script, TOML md5 `be7f335b835a741dab4d414880f9aacd`, không có bản trùng.
- CSV3: 2 bộ — bộ home `07_Nagi_Fukami` cũ (khớp TOML 1/272), bộ `11_Other` tốt (khớp 272/272, đã dùng bộ này).
- Đã đọc 272/272 dòng; xét 107 dòng rên/SFX (68 thoại rên + 1 độc thoại gasp + 38 SFX).
- Đổi 13 dòng: 12 romaji + 1 đếm nguyên âm (1057 `kyuuu`→`kyuu`).
- Romaji: 967 `Hyaaann`, 973 `Hia!?`, 974 `Hyua!?`, 976 `Hie!?` + `Fuwa`, 977 `Hyuan!?`, 982 `Kuo!`, 983 `Kwa!`, 989 `Fua!`, 1027 `Haan!` + `Chỗ đóoo!`, 1048 `Fuaa……Pua`, 1049 `Fua`, 1058 `Ư!!?——Ahyuuuuuun!!!` (giữ Ư đầu dòng của audit, chỉ đổi rên sang romaji).
- Kiểu lỗi chính: bản cũ tách một âm rên duy nhất thành nhiều mảnh rời ("Hya ah ưm", "Hi ah", "Phù ah") — đã gộp thành một cách diễn romaji.
- 3 dòng fa/fu (989, 1048, 1049) sửa thành romaji ở đây, thay cho ghi chú "phùa" của audit ở đợt thống nhất.
- Giữ 94 dòng rên/SFX (kiểu "ah" cho あっ, "Ưm + X" cho ん+X, SFX "chụt/liếm/Phụt", cười "Ufufu", nói ngọng 1077).
- Sweep: 3 mục đã kiểm chứng — 1461 không sửa (JP không có っ), 1403 audit đã sửa đúng ("——Ư!"), 1426 false positive (JP không có っ).
- Cờ cho đợt thống nhất: 5 ghi chú xét lại romaji trong bản sửa audit (987, 992, 995, 1039, 1045); 2 xung đột Kh — đề nghị hủy fix audit của 979 ("Kh——"→"Ư——") và 1043 ("kh"→"ƯƯ"), giữ "Kh"/"kh" theo quyết định khóa 21/11.
- Lượt soát 2: tổng 13 / tái kiểm chứng 13 / bỏ 0 / sửa 0. JSON 13 mục, khóa string, jp/tw/old_vn khớp CSV3 13/13. Khối TOML parse bằng tomllib: 13 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-fukamih1-tomohari-renshuu-REVIEW.md`; danh sách sửa: `moan-fukamih1-tomohari-renshuu-wrong.json`.

**Tổng cộng sau file này: 1 file / 13 dòng sai (moan)** (cơ sở 0 file / 0 dòng + 13 file này)
- FLAG (đợt thống nhất): 2 xung đột "Kh" — đề nghị HỦY fix audit của ふかみh1 979 ("Kh——"→"Ư——") và 1043 ("kh"→"ƯƯ"), giữ "Kh"/"kh" theo quyết định khóa 21/11 (Kh cho glottal-stop っ KEEP, không unify sang Ư).

---

# Moan-fix snippet — 凪h2_おとなの水着.txt.toml

- File: 凪h2_おとなの水着.txt.toml (07_Nagi_Fukami, 673 dòng, audit trước đó 89 sai)
- TOML md5: a581ef85d1d7aed81fc5303b23f050ea
- CSV3: 1 set duy nhất, 673 dòng, 0 key trùng
- Dòng moan tìm được: 158 (rên/thở/gasp/hừm 88, SFX trong ngoặc 39, SFX miệng 22, cười/giggle 9)
- Dòng moan sửa: 25 (24 sai âm + 1 mất độ dài んんんっ→"Ưmmm")
- Dòng moan giữ: 124
- Dòng sweep đã xử lý, không đụng: 8 (7 gasp Ư + 1 already-rendered 2489)
- Flag: 1 (2515 あふゅいっ → "Nóng quá" — TW 危 vs VN "Nóng quá", câu hỏi nghĩa, thuộc vòng audit)
- Nhóm lỗi chính: họ fa/fu diễn "Phù a"/"Phù" sai (8 dòng: 2462, 2452, 2451, 2445, 2449, 2563, 2405, 2428/2589 ぷあ); ひあ diễn "Hya" thay vì "Hia" (5 dòng: 2397, 2398, 2407, 2418, 2403); gasp lạ bị diễn chung chung (5 dòng: 2409 Kahyu, 2512 Nhyu, 2395 Nkyu, 2401 Kyufu, 2414 Nhi/I)
- Second pass: 25 tổng / 25 re-verified / 0 removed / 0 corrected
- TOML block: parse-verified (tomllib), 25 key, 0 value mismatch vs wrong.json

**Tổng cộng sau file này: 2 file / 38 dòng sai (moan)** (cơ sở 1 file / 13 dòng + 25 file này)
- FLAG: 2515 あふゅいっ → "Nóng quá" — câu hỏi nghĩa (TW 危 vs VN "Nóng quá"), thuộc vòng audit, ghi chú lại cho đợt sửa sau.
- SỬA (parent 21/11 ~02:35, sau merge): key 2500 fix "Nyuuuuuuuuu" → "Nyuuuuuuuuuu" (10 u; JP ゅ+7う+2ぅ = 10 u theo công thức, agent đếm thiếu 1). Đã sửa wrong.json + REVIEW; sẽ push lại cùng đợt push sau (staging vẫn giữ bản cũ đã push).

---

# Moan-fix snippet — ポーレットh8_気動車の国のアリス.txt.toml

- File: ポーレットh8_気動車の国のアリス.txt.toml (03_Paulette, 649 dòng, audit trước đó 156 sai)
- TOML md5: da94288489af95805aa9e8d2617d0a42 (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 649 dòng, 0 key trùng.
- Dòng moan xét: 226 (203 theo mẫu chặt + 23 gasp/SFX rà thêm); sửa 33, giữ 193.
- Dòng moan sửa: 33 (23 romaji + 9 cười + 1 sai âm).
- Romaji La-tinh: 2132 Hyu+15a, 2134 Hyaunn, 2137 Hyau, 2139 Kyafu, 2142 Kyu, 2185 Fue, 2187 Hyau, 2241 Hakyu (+くっ Ư→Hự), 2286 Yoisho, 2365 Yoisho×2, 2304 Nyu, 2413 Nhyu. Giữ 2136 Hia (đã đúng).
- Romaji fa/fu: 2049/2167/2207/2214/2303 Fua, 2165 Fuaa, 2163 Fua + Fuaaaaa, 2212 Fua×2, 2279/2340/2376 Pua. Không còn dòng fa/fu nào diễn "phù a" trong file.
- Cười bị diễn thành rên: 2345/2351/2353/2355/2361/2362/2364/2563 Ufufu, 2349 Ufu (うふふ/うふ → "Ư hự hự"/"Ư hự").
- Sai âm: 2228 ぐ――ぅっ "Ư——hự" → "Guu".
- Dòng sweep đã xử lý, không đụng: 8 (7 gasp Ư + 1 already-rendered 2344). Không dòng "Kh" nào bị đổi.
- Flag: 2 (2155 はぁっ cuối dòng có thể mất っ — câu hỏi gasp-sweep; 2179 おっと → "Ốp" — hướng sửa chưa rõ).
- Ghi chú đợt thống nhất: 14 fix thay thế fix audit cùng key (2132, 2137, 2139, 2142, 2185, 2187, 2241, 2279, 2286, 2304, 2340, 2365, 2376, 2413) — áp giá trị moan, không áp cả hai.
- Second pass: 33 tổng / 33 re-verified / 0 removed / 0 corrected.
- TOML block: parse-verified (tomllib), 33 key, 0 value mismatch vs wrong.json.

**Tổng cộng sau file này: 3 file / 71 dòng sai (moan)** (cơ sở 2 file / 38 dòng + 33 file này)
- FLAG: 2155 (はぁっ cuối dòng — っ có thể đã mất, sweep + audit đều bỏ qua; cần vòng audit quyết thêm Ư hay giữ) và 2179 (おっと → "Ốp" — hướng sửa chưa rõ: "Ôi"/"Ối" hay "Otto").
- Parent kiểm chứng 21/11 ~03:20: JSON 33 mục dạng chuẩn, khối TOML 33 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 33/33; 4 dòng gộp fix lệch vị trí của audit (2185/2279/2340/2376) đã kiểm chứng — moan fix chỉ khác fix audit ở đúng phần rên (2185 Phê→Fue, 2279 phù a→Pua, 2340 phù→Pua, 2376 Phù a→Pua), áp giá trị moan thay audit ở đợt thống nhất; 8 dòng sweep gasp Ư không đụng; không dòng "Kh" nào bị đổi; lượt soát 2: 33/33, 0 bỏ, 0 sửa. Flag 2155/2179 ghi lại cho vòng audit (không quyết).

---

# Moan-fix snippet — lr_稀咲ポーレットh1_悪い大人の契約.txt.toml (moan-paulette-lr-kisaki-h1)

- File: `lr_稀咲ポーレットh1_悪い大人の契約.txt.toml` — route 03_Paulette, 488 dòng script, audit trước đó 85 sai.
- TOML md5: `342110f3930d8dcd96d8eaa574e0404a` — trùng khớp bản sao ở `06_Kisaki/` (nhóm trùng lặp; fix áp dụng cho CẢ HAI bản sao).
- CSV3: 1 bộ duy nhất (`03_Paulette`), 488 dòng, 0 key trùng; TOML vs CSV3 chỉ 3 khác `\n`/khoảng trắng (1484, 1611, 1900).
- Đã đọc 488/488 dòng; xét 256 dòng rên/SFX (fa/fu 19, はぁっ 4, gasp Ư 19 + 3 already-rendered, rên dài/SFX dài 11, ひゃ/ひあ/ひゅ 8, cười ふふ 8, chuỗi ちゅ/ぺ 44, độc thoại （…） 90).
- Đổi 21 dòng: 13 fa/fu → romaji (Fa/Fua: 1468, 1397, 1495, 1472, 1481, 1523, 1480, 1477, 1536, 1475, 1470, 1624, 1478) + 5 romaji khác (1442 Kyafu, 1642 Hafuu, 1443 Hyaun, 1576 Fuwa, 1593 Uu) + 2 gộp âm tách (1566 Au, 1484 Kuu) + 1 sửa đếm audit (2503: 17→18 âm u). (2500 đã loại sau kiểm chứng của parent — audit đã đúng đếm, xem REVIEW.)
- Giữ 234 dòng rên/SFX (19 gasp Ư khóa + 3 already-rendered + 6 fa/fu thở nhẹ giữ "phà" + 4 "Hà" + 8 cười "Fufu" + chuỗi ちゅ/ぺ và SFX độc thoại theo quy ước file).
- Phát hiện đếm (đã sửa trong đợt này): audit đếm sai 1468 (ghi 6 âm a, JP có 5 — fix "Faaaaa"), 2503 (fix 17 âm u, JP có 18) — đếm lại độc lập theo công thức. 2500: agent báo audit thiếu 1 âm u nhưng parent kiểm chứng — fix audit "Kí"+13u đã đủ 14 nguyên âm theo công thức (agent không tính nguyên âm gốc "í"); giá trị moan của agent thừa 1 âm nên đã loại dòng này (22 → 21 mục).
- Sweep: 16 mục đã kiểm chứng trực tiếp (13 fix Ư + 3 already-rendered + 2236 needs-file-audit); không dòng "Kh" nào bị đổi.
- Flag: 6 (1573 かはっ→"A!" mất phụ âm "ka"; 1561 「ぁっ」→"A" không dấu ngắt; 1760 nói ngọng giữ nguyên; họ ちゅ→"chụt" hệ thống vẫn chờ Hieu; 2 lỗi đếm audit đã sửa — xem REVIEW; fix áp dụng cả 2 bản sao).
- Second pass (agent): 22 tổng / 22 re-verified / 0 removed / 0 corrected. Parent kiểm chứng: loại 1 (2500, xem trên) → JSON 21 mục, khóa string, jp/tw/old_vn khớp CSV3 21/21. Khối TOML parse-verified (tomllib), 21 key, 0 value mismatch vs wrong.json.
- Chi tiết đầy đủ: `moan-paulette-lr-kisaki-h1-REVIEW.md`; danh sách sửa: `moan-paulette-lr-kisaki-h1-wrong.json`.

**Tổng cộng sau file này: 4 file / 92 dòng sai (moan)** (cơ sở 3 file / 71 dòng + 21 file này)
- FLAG: 2 lỗi đếm của audit đã sửa trong đợt này (1468: 6→5 âm a; 2503: 17→18 âm u). 2500: parent đã kiểm tra lại khi merge — audit đã đúng, agent đếm sai, dòng đã loại (không sửa).
- Parent kiểm chứng 21/11 ~03:20: JSON 21 mục (sau khi loại 2500), khối TOML 21 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 21/21; 2 sửa đếm audit kiểm chứng độc lập (1468: 6→5 a ✓; 2503: 17→18 u ✓); LOẠI key 2500 — agent đếm sai (chỉ đếm chữ u, không tính nguyên âm gốc "í": fix audit "Kí"+13u đã đủ 14 nguyên âm theo công thức; giá trị moan thừa 1 âm); 19 dòng gasp Ư + 3 already-rendered không đụng; không dòng "Kh" nào bị đổi; lượt soát 2 (agent): 22/22, 0 bỏ, 0 sửa. Flag 1573/1561/1760/ちゅ ghi lại (không quyết). REVIEW có Kết bài nhưng khối TOML đặt sau Kết bài (lệch thứ tự mẫu, không ảnh hưởng nội dung).

---

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
- Parent kiểm chứng 21/11 ~04:35 (handoff merge): JSON 33 mục dạng chuẩn, khóa string; khối TOML 33 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 bộ tốt 11_Other 33/33; 31/33 key trùng audit — 9 áp nguyên giá trị audit (1196, 1224, 1279, 1310, 1920, 1949, 1966, 1967, 1968), 22 chỉ khác audit ở đúng token rên (phà/phù/phuê→romaji; 1432 a→aa, giữ "cho anh" của audit); 2 key mới (1280 Hiu, 1655 kyun kyun); đếm nguyên âm kiểm chứng độc lập 10/10 (1224 17a, 1279 8u, 1310 16u, 1920 14u, 1949 4u+1u, 1966 7u, 1967 2u+2u, 1968 1u, 1655 1u/token, 1465 2a); chỉ 1 dòng đổi số lượng Ư (1268 — Ư của audit được giữ nguyên); không dòng "Kh" nào bị đổi; lượt soát 2: 33/33, 0 bỏ, 0 sửa. Flag: 3 dòng "Fu, a" (1223/1379/1458) + 1460 "Fau" ghi lại cho đợt thống nhất (không quyết).

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
- Parent kiểm chứng 21/11 ~09:15 (hoàn tất run moan 03:44 bị timeout): JSON 31 mục dạng chuẩn, khóa string; khối TOML 31 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 31/31; kinds moan-only (romaji/vowel-count/length/wrong-sound); không fix nào bằng VN cũ; Ư gasp của audit được giữ nguyên ở các key đổi fa/fu (1712/1725/1727/1728/1741/1743/2200/2201); không dòng "Kh" nào bị đổi. SỬA 1 lỗi của run 03:44: worker đã loại 1753 khỏi JSON vì tưởng no-op — kiểm chứng độc lập: VN cũ đã đúng 3 u theo cả CSV3 lẫn TOML-2 (JP きゅううんっ = 3 u), nên 1753 ĐÚNG là no-op và worker loại đúng; parent đã xóa nốt mục 1753 khỏi §3 + khối TOML của REVIEW và sửa các số 32→31 (đổi 31, giữ 384, lượt soát 2: 32 ứng viên / bỏ 1 / còn 31 fix). Flag: HỦY 23 fix fa/fu của audit (giữ romaji cũ) ghi lại cho đợt thống nhất; audit §4 đếm sai 1731 (7 a, không phải 6).

---

# Moan-fix snippet — ハチロクh9_コノフクハキルコト.txt.toml (moan-hachiroku-h9-konofuku-ha-kirukoto)

- File: `ハチロクh9_コノフクハキルコト.txt.toml` — route 01_Hachiroku, 613 dòng script, TOML md5 `bcbf02a0308ddac5d5aca3ac1cd717ce` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 613 dòng, 0 key trùng; VN khớp TOML 613/613 (audit đã kiểm chứng; 26 key sửa kiểm tra lại 0 sai lệch).
- Đã đọc 613/613 dòng; xét 100 dòng rên/SFX (69 Hachiroku + 20 Soutetsu + 11 độc thoại; 83 dòng có っ, 10 dòng họ fa/fu/hya, 31 dòng nguyên âm dài, 6 SFX ngoặc, 4 cười).
- Đổi 26 dòng: 13 romaji + 9 đếm nguyên âm + 4 sai âm.
- Romaji fa/fu: 2082 ふあ→"Fua", 2089 ふっ――ふあっ→"Fu——Fua", 2037 ふあっ→"Fua" ×2 + ふううっ→"Fuuu", 2110 ふあっ→"Fua", 2180 rên dài ふあ… (17 a, bản cũ 20 a tách mảnh)→"Fua"+17 a, 2151 ふ……あ→"Fu……a", 2289 ふ――あっ→"Fu——a", 2109/2378/1356/2613/2319 ふ、あっ→"Fu, a", 2144 ふっ――あっ→"Fu——a".
- Đếm nguyên âm: 2055 はあっ→"haa" ×3, 2097 はぁあっ→"Haaa", 2120 ちゅううう→"chuuuu", 2078 ちゅうっ→"chuu", 2122 れるううううっ→"reruuuuu", 2101 くああ→"Kuaa", 2053 ほう→"hoo", 2134 ほー→"hoo", 2054 はああっ→"haaa" + はぁっ→"haa"; 2110/2289/2109 cũng sửa số âm (はぁっ→"Haa", はああっ→"Haaa", はぁ→"haa").
- Sai âm: 2136 ちろっ→"Chiro", 2156 ちゅむっ→"chumu", 1358 ちゅむ→"chumu" ×2 + ちゅうっ→"chuu" + れるっ→"reru" (bản cũ "liếm lútttt"), 2178 きゅくだぅぅぅ→"Kyukuuuuu" (bản cũ "Ưm ưưưư" mất phụ âm kyu).
- Kiểu lỗi chính: họ fa/fu bị Việt hoá "phù a" trong chuỗi rên cao trào; rên dài đếm nguyên âm sai (thiếu/thừa 1–3 âm, hoặc kéo dài bằng phụ âm t như "chụttttt").
- Giữ 74 dòng rên/SFX (romaji đúng "Hyuua/Hia/Kyaaa/Kyuu", cười "Ufufu", hơi thở "phù" đứng riêng, SFX độc thoại onomatopoeia Việt, gasp Ư của audit/sweep không đụng).
- Sweep: 31 mục đã kiểm chứng qua audit (25 raw-tsu + 5 lost-gasp + 1 already-rendered 2178) — không đụng dòng Ư nào; không dòng "Kh" nào bị đổi (1883 "Kh——ông" giữ nguyên).
- Cờ cho đợt thống nhất: mâu thuẫn audit ở 1883 (JSON ghi "là do anh", REVIEW + ROUTE-AUDIT ghi "là do tôi" — parent kiểm tra giá trị đã merge); 2020 "Ohimitera"→"Ohitoyo"; 7 dòng tách nhịp fa đã về romaji (revert dễ nếu Hieu muốn giữ "phù, a"); 1358 "reru" vs "liếm"; 2178 quyết theo JP (TW diễn thành ưm); SFX độc thoại giữ onomatopoeia Việt, chưa áp công thức đếm nguyên âm.
- Lượt soát 2: tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0. JSON 26 mục, khóa string, jp/tw/old_vn khớp CSV3 26/26. Khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.
- Parent kiểm chứng 21/11 ~10:00: JSON 26, TOML 26 khóa 0 sai lệch, CSV3 26/26; 9 key trùng audit chỉ khác đúng token rên; Ư thêm vào đều là Ư của audit; SỬA 2101 "Aa!"→"Kuaa!" (JP くああ có く, JP thắng TW); 1883 đã giải quyết (xem FLAG).
- Chi tiết đầy đủ: `moan-hachiroku-h9-konofuku-ha-kirukoto-REVIEW.md`; danh sách sửa: `moan-hachiroku-h9-konofuku-ha-kirukoto-wrong.json`.

**Tổng cộng sau file này: 7 file / 182 dòng sai (moan)** (cơ sở 6 file / 156 dòng + 26 file này)
- FLAG (đã giải quyết khi merge): 1883 KHÔNG có mâu thuẫn — agent đọc nhầm old_vn thành fix; audit wrong.json ghi old_vn "là do anh", fix "là do tôi"; REVIEW + ROUTE-AUDIT đều ghi "là do tôi" (đã merge đúng). Phần moan của 1883 không đổi.

---

# Moan-fix snippet — 稀咲h3_チャイナドレスでおもてなし.txt.toml (moan-kisaki-h3-china-dress-omotenashi)

- File: `稀咲h3_チャイナドレスでおもてなし.txt.toml` — route 06_Kisaki, 662 dòng script, TOML md5 `3bccfb4626ff9b0e014a8655d1091f7e`, không có bản trùng.
- CSV3: 1 bộ duy nhất (thư mục `06_Kisaki`), 662/662 dòng, 0 khóa trùng; VN TOML-2 khớp CSV3 sau chuẩn hóa `\n`.
- Đã đọc 662/662 dòng; xét 181 dòng rên/SFX (97 thoại Kisaki + 14 thoại Soutetsu + 70 độc thoại, gồm 58 dòng SFX trong ngoặc).
- Đổi 23 dòng: romaji 19 + độ dài nguyên âm 2 + âm sai 2.
- Romaji fa/fu → "Fua" (13): 1538, 2120, 2152, 2170, 2188, 2195, 2225, 2252, 2253, 2254, 2360, 3808 + 2207 (ぷぁ "Pha"→"Pua"); nhất quán với "Fua!" sẵn có ở 2255.
- Romaji họ hia/hya/hyu (4): 2197 ひあっ "I a"→"Hia" (+ たらぁっ "thì"→"thì a"), 2198 ひウっ "I ư"→"Hiu", 2206 ひゅっ "Hưu"→"Hyu", 2277 んひゅんっ "Ưm hưu"→"Nhyun".
- Romaji gộp mảnh rời của âm dài (2): 2155 んうううっ "ư ư ư"→"Nuuu", 2257 くふぅんんんん "Khu phư ưm"→"Kufuunnnn".
- Độ dài nguyên âm (2): 2162 ひゃうっっ "Hya"→"Hyau", 2269 れるうっ "rero"→"Reroo".
- Âm sai (2): 2228 う……む "Ư…… m"→"Ư…… ừm", 2238 ほーへふっ "Anh Houhehu"→"Anh Houhefu" (chỉ sửa ふ "hu"→"fu"; phần bỏ "Anh" parent đã lùi — là sửa đại từ, không thuộc moan; ghi cờ cho đợt thống nhất).
- Giữ 158 dòng rên/SFX, gồm 11 dòng gasp Ư của sweep đã khóa (audit áp nguyên; 4 dòng 2170/2188/2253/2257 giữ Ư của audit trong fix value — dùng fix moan, không áp thêm fix audit cùng key).
- Giữ theo tiền lệ audit đã khóa: "a a"/"á á" (ああっ), "Phuaaaaưm!" (2240), "rồiiiiii" (2116), "Ưm kyu" (2278), "Ưm ưm" (2279), "khưuuuuu" (2398); JP tự tách ("Fu…… a", "fu, a", "phu, á") giữ theo cấu trúc JP; "phù"/"fu" cho ふっ/ふうっ ngắn giữ.
- Sweep: 13 mục đã kiểm chứng — 11 fix Ư audit áp nguyên, 2 already-rendered (3373, 3483); không sửa lại dòng gasp Ư nào.
- Lượt soát 2: tổng 23 / tái kiểm chứng 23 / bỏ 0 / sửa 0 (bản nháp JSON đầu làm mất dấu 「 」, bắt được khi in kiểm tra lúc build, đã sửa trước lượt soát 2).
- Parent kiểm chứng 21/11 ~10:00: JSON 23, TOML 23 khóa 0 sai lệch, CSV3 23/23; 4 key trùng audit chỉ khác đúng token rên; Ư thêm vào đều là Ư của audit; SỬA 2155 "Nuuuu"→"Nuuu" và 2257 "Kufuuunnnn"→"Kufuunnnn" (đếm thừa 1 u); LÙI 2238 phần bỏ "Anh" (sửa đại từ, ghi cờ đợt thống nhất).
- Chi tiết đầy đủ: `moan-kisaki-h3-china-dress-omotenashi-REVIEW.md`; danh sách sửa: `moan-kisaki-h3-china-dress-omotenashi-wrong.json`.

**Tổng cộng sau file này: 8 file / 205 dòng sai (moan)** (cơ sở 7 file / 182 dòng + 23 file này)
- FLAG (đợt thống nhất): 4 fix value gộp cả Ư của audit (2170, 2188, 2253, 2257) — dùng fix moan, KHÔNG áp thêm fix audit cùng key. 2238: "Anh" giữ lại (parent lùi phần bỏ "Anh" — sửa đại từ, không thuộc moan); cờ: "Anh" là cách xưng Kisaki→Soutetsu hay từ bịa của Gemini (TW 呼 = tiếng thở)? 2197 thêm "a" cho たらぁっ (ぁ là mora nguyên âm, không phải chỉ っ).

---

# Moan-fix snippet: lr_ポーレットh2_デコレーション＆ミルク

- File: `03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml` — 333 dòng, đã đọc 333/333.
- Đổi 10 dòng rên: 9 romaji (8 họ fa/fu → Fa/Fua/Fan: 1022, 1024, 1025, 1032, 1039, 1084, 1095, 1099; 1 きゅふっ → "Kyufu": 1009) + 1 sửa đếm (1007 "Kyaaan"→"Kyaan", thừa 1 âm a).
- Giữ 271 dòng ứng viên: 9 fa/fu thở nhẹ giữ "phà"/"phù" (1043, 1053, 1072, 1074, 1079, 1127, 1167, 1315, 1735), 9 cười giữ nguyên, 13 mục gasp Ư khóa, toàn bộ chuỗi SFX oral + độc thoại theo quy ước file.
- Kiểm tra lần hai: 10/10 xác minh đúng, 0 loại, 0 sửa lại; đếm nguyên âm SFX của audit kiểm chứng lại bằng máy — tất cả đúng.
- Flag: 1093 (ぁあっっ — gasp っっ cuối dòng có thể bị mất, thuộc phạm vi gasp-sweep, không tự sửa).
- Không có dòng "Kh" nào bị đổi sang Ư; không chạm xưng hô/thuật ngữ/nghĩa.

**Tổng cộng sau file này: 9 file / 215 dòng sai (moan)** (cơ sở 8 file / 205 dòng + 10 file này)
- Parent kiểm chứng 21/11 ~10:55: JSON 10 mục dạng chuẩn, khóa string; khối TOML 10 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 10/10 (1 bộ duy nhất, 333 dòng); 1009 Ư cuối dòng là của audit đã merge (giữ nguyên, chỉ đổi "Kyu fu"→"Kyufu"); 1025 "Khíu" là của audit (giữ nguyên, chỉ đổi "pha"→"Fa"); 1024 "Faaa" 3 a khớp đếm audit; 1007 mới (きゃぁん = 2 a, "Kyaan"); mọi fix chỉ khác old_vn đúng ở token rên; không dòng "Kh" nào bị đổi; lượt soát 2: 10/10, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất / vòng audit): 1093 (ぁあっっ — っっ cuối dòng có thể mất gasp, thuộc phạm vi gasp-sweep, không tự quyết); 1017 (くはっ → "Ư ha" mất phụ âm k, TW cũng vậy); 1077 (っ cuối diễn thành "ư" thường, không phải "Ư").

---

# Moan-fix snippet — ポーレットh3_誘惑アイスコーヒー.txt.toml (moan-paulette-h3-yuuwaku-ice-coffee)

- File: `ポーレットh3_誘惑アイスコーヒー.txt.toml` — route 03_Paulette, 279 dòng script, TOML md5 `884568f018ff870371ba906804c8651c` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 279 dòng, 0 key trùng; VN khớp TOML 279/279 sau chuẩn hóa `\n`/khoảng trắng (audit đã kiểm chứng; 37 key sửa kiểm tra lại 0 sai lệch).
- Đã đọc 279/279 dòng; xét 139 dòng rên/SFX (57 Paulette + 16 Soutetsu H + 66 độc thoại, gồm 26 SFX ngoặc).
- Đổi 37 dòng: 13 romaji + 7 đếm nguyên âm + 17 sai âm.
- Romaji fa/fu: 897/915/917/919/937/940/950/1070 ふあっ/ふぁっ→"Fua", 948 ぷあっ→"Pua", 977 ぷぁ→"Pua", 982 ふやっ→"Fuya"; 966 れろおおおっ→"Reroooo" (4 o), 968 れるうううううっ→"Reruuuuuu" (6 u), 974 ずろぉぉぉぉぉぉっ→"Zurooooooo" (7 o).
- Đếm nguyên âm: 899 ひゃ…んっ thêm "n" (7 a đã đúng), 920 ふぃぁ…→"Phi"+11 a, 923 ずりゅう…→"Sụ"+11 ụ+"t", 927 thêm 1 a + "n" (13 a), 931/933/942 ちゅううっ→"chụụụt" (3 u), ちゅうっ→"chụụt" (2 u); 948 はぁっ→"hàà" (2 a), はぁああっ→"Hàààà" (4 a); 915 ハァッ→"hàà"; 974 すうっ→"Suụt".
- Sai âm: 898/902/903 きゃっ→"Kya"/"Kyaa", 904 ひゃっ→"Hya", 890/893/894/897 や→"Ya"/"Yaa", 900 くひゅっ→"Kuhyu", 982 くひゅんっ→"Kuhyun", 906 くっ→"Ku", 938 ぅあっ→"Ua", 955 うぁっ→"Wa", 914/946/966/970 ちゅむっ→"chumu", 914/931 ちゅばっ→"Chuba", 933 ちゅぶっ→"chubu", 969 じゅぼっ→"Jubo", ぢゅぶっ→"Jubu", 970 ぢゅぼっ→"Jubo", じゅろっ "Chụtttt"→"Chụt", 967 ちゅる―― (không っ)→"Churu".
- Kiểu lỗi chính: họ fa/fu bị Việt hoá "phù" mất hẳn âm a; rên dài kéo bằng phụ âm t/m thay vì nguyên âm; phụ âm mora bị mất hẳn ("Á" cho きゃっ/ひゃっ/やっ, "chu" cho ちゅむっ/ちゅばっ).
- Giữ 102 dòng rên/SFX (romaji đúng "Hyan!!" 901, "Í!!"/"Uo!?", "Chụt" cho họ ちゅ, "liếm" cho れるっ/れろっ ngắn, "Phù" đứng riêng cho ふっ ngắn, SFX độc thoại onomatopoeia Việt, gasp Ư của audit/sweep không đụng).
- Sweep: 7 mục đã kiểm chứng — 6 bản sửa gasp Ư của audit (907, 908, 934, 935, 954, 1639) không đụng dòng nào; 1 already-rendered (994) giữ nguyên. File không có dòng "Kh" nào.
- Cờ cho đợt thống nhất: 1013 うれしっ→"Sướng" (lỗi nghĩa, TW 高興); SFX độc thoại （ ） chưa áp công thức đếm nguyên âm (1652/1655/1656/1658/1671/1673/1676 kéo bằng t); 1683 (dòng chưa chắc chắn của audit); 946/1069 くぅん kéo dài của くん sau tên "Soutetsu"; 924 むぷっ→"Ưm" giữ (âm m đã bao hàm ぷ).
- Lượt soát 2: tổng 37 / tái kiểm chứng 37 / bỏ 0 / sửa 0. JSON 37 mục, khóa string, jp/tw/old_vn khớp CSV3 37/37. Khối TOML parse bằng tomllib: 37 khóa, 0 sai lệch giá trị.
- 7 key trùng audit (890, 899, 900, 904, 919, 937, 982) chỉ khác giá trị audit ở đúng token rên; dùng fix moan thay cho giá trị audit khi gộp.
- Chi tiết đầy đủ: `moan-paulette-h3-yuuwaku-ice-coffee-REVIEW.md`; danh sách sửa: `moan-paulette-h3-yuuwaku-ice-coffee-wrong.json`.

**Tổng cộng sau file này: 10 file / 252 dòng sai (moan)** (cơ sở 9 file / 215 dòng + 37 file này) [parent REBASE 21/11 ~11:15 — snippet ghi cơ sở cũ 8/205 vì lr h2 đã gộp trước]
- Parent kiểm chứng 21/11 ~11:15: JSON 37 mục dạng chuẩn, khóa string; khối TOML 37 khóa, 0 sai lệch giá trị (sau sửa 923); jp/tw/old_vn khớp CSV3 37/37 (1 bộ duy nhất, 279 dòng); TOML md5 khớp audit; 7 key trùng audit chỉ khác đúng token rên (890 "Á"→"Ya", 899 thêm "n", 900 "Á"→"Kuhyu", 904 "Á"→"Hya", 919/937 "Phù"→"Fua", 982 "Hí——phù"→"Kuhyun! Fuya"); đếm nguyên âm kiểm chứng độc lập 12/12 (899 7a+n, 920 11a, 923 12u, 927 13a+n, 966 4o, 968 6u, 974 7o+2u, 948 2a/4a, 915 2a, 931/933/942 chụ 3u/2u); sweep 7 mục không đụng; không dòng "Kh"; lượt soát 2 (agent): 37/37, 0 bỏ, 0 sửa.
- SỬA (parent): key 923 "Sụ"+11ụ → "Sụ"+12ụ — agent đếm thiếu 1: JP ずりゅう… có 11 chữ う (không phải 10), công thức 1+11=12. Đã sửa wrong.json + REVIEW (§3b, §6, khối TOML).
- GHI CHÚ: 906 "Ư"→"Ku" (くっ — agent quyết く là phụ âm thật, không phải gasp っ trần; sweep không liệt kê, audit không sửa — giữ theo phán đoán moan, ghi lại để đợt thống nhất rà lại).
- FLAG (đợt thống nhất / vòng audit): 1013 (うれしっ→"Sướng" — lỗi nghĩa? TW 高興 = vui mừng, không phải khoái cảm); SFX độc thoại （ ） chưa áp công thức đếm nguyên âm (1652/1655/1656/1658/1671/1673/1676 kéo bằng t — như cờ h9); 1683 (dòng chưa chắc chắn của audit); 946/1069 (くぅん sau tên "Soutetsu"); 924 (むぷっ→"Ưm"); 1072/1002 (tiếng lắp).

---

# Moan-fix snippet: lr_ポーレットh1_家族旅行の最終日の夜

- File: `03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml` — 303 dòng, đã đọc 303/303.
- TOML md5 `bd55bd0643350b7396121d5161727c21` (khớp audit), không có bản trùng. CSV3: 1 bộ duy nhất, 303 dòng, 0 key trùng.
- Đổi 22 dòng rên: 21 romaji + 1 sai âm (1099 んゅっ "Ưm!"→"Nyu!", mất âm yu).
- Romaji: ひゃう→Hyau 3 dòng (1000, 1002, 1003); ふぁ→Fa 8 dòng (1003, 1019, 1022, 1023, 1025, 1062, 1096, 1100); ふあ→Fua 5 dòng (1000, 1020, 1049, 1058, 1124); ぷぁ→Pa 2 dòng (1043, 1065); ぷあ→Pua 2 dòng (1113, 1201); ふえ→Fue 2 dòng (1018, 1098); きゅっふっ→Kyuffu 1 dòng (998). Quy ước Hepburn chặt (ふぁ 1 mora→Fa, ふあ 2 mora→Fua; tiền lệ 凪h2/lr-h2; h8 dùng "Fua" cho cả ふぁ — ghi flag F4).
- 19 fix xây từ giá trị audit (chỉ đổi phần rên); 3 fix xây từ VN cũ (1018, 1098, 1099 — không có trong audit). Fix 998 giữ đuôi gasp ~~~~~~~Ư của sweep.
- Giữ 121 dòng rên/SFX: ひあ→"Hia" (1005, 1007, 1011), ひゃ→"Hya" (997, 1009, 1013), SFX miệng chụt/rột/rộp + đếm nguyên âm của audit, あんっ→"An", "Ưm kyu" (1097), thở ngắn "phù"/"phu", cười Latin fufu/ufufu/ehehe, toàn bộ 54 dòng SFX độc thoại.
- Sweep: 17 mục đã kiểm, 0 dòng đụng. Không dòng "Kh" nào bị đổi; không chạm xưng hô/thuật ngữ/nghĩa.
- Kiểm tra lần hai: 22/22 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 22 mục, khóa string, jp/tw/old_vn khớp CSV3 22/22. Khối TOML parse bằng tomllib: 22 khóa, 0 sai lệch giá trị.
- Flag: F1 1156 くぅん (âm u kéo dài trong tên gọi, không diễn); F2 1689 ぷちゅっん→"Phụt" (nghĩa SFX chưa chắc); F3 cười Latin 1062/1088/1181 chờ Hieu (đã flag từ audit); F4 quy ước Fa/Fua vs h8; F5 audit json dùng key INT (ghi nhận).
- Chi tiết đầy đủ: `moan-paulette-lr-h1-kazoku-ryokou-REVIEW.md`; danh sách sửa: `moan-paulette-lr-h1-kazoku-ryokou-wrong.json`.

**Tổng cộng sau file này: 11 file / 274 dòng sai (moan)** (cơ sở 10 file / 252 dòng + 22 file này)

- Parent kiểm chứng 21/11 ~11:45: JSON 22 mục dạng chuẩn, khóa string; khối TOML 22 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 22/22 (1 bộ duy nhất, 303 dòng); TOML md5 khớp audit; 19 key trùng audit chỉ khác đúng token rên (phà→Fa/Fua/Pa/Pua, Hiau→Hyau, Kíuphù→Kyuffu); 3 key mới (1018/1098/1099 — 1099 んゅっ "Ưm!"→"Nyu!" sửa mất âm yu, "!" diễn っ cắt, không phải dòng gasp Ư); Ư của 998 và "Khự" của 1023 đều là giá trị audit được giữ nguyên (moan chỉ đổi token rên); lượt soát 2: 22/22, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F4 — file này dùng Hepburn chặt Fa (ふぁ) / Fua (ふあ) / Pa (ぷぁ) / Pua (ぷあ), KHÁC với h8 đã merge (dùng "Fua" cho cả ふぁ: 2049/2167/2212; "Pua" cho cả ぷぁ: 2279) — đã kiểm chứng từ moan-paulette-h8-alice-rail-car-wrong.json. Cần quyết một dạng duy nhất toàn dự án ở đợt thống nhất (tiền lệ đa số: Fa/Fua chặt — 凪h2, lr-h2, lr_ふかみh1). F1 (1156 くぅん), F2 (1689 ぷちゅっん), F3 (cười Latin 1062/1088/1181 chờ Hieu), F5 (audit json key INT) ghi lại, không quyết.

---

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

- Parent kiểm chứng 21/11 ~11:50: JSON 18 mục dạng chuẩn, khóa string; khối TOML 18 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 18/18 (1 bộ duy nhất, 435 dòng); TOML md5 khớp audit; 11 key trùng audit chỉ khác đúng token rên; 7 key mới (485/690/711/750/836/837/839 — mất phụ âm/glide + đếm nguyên âm, đều moan-only); đếm nguyên âm kiểm chứng độc lập: 819 "Faaaaaan" 5 a đúng (ふぁ+4あ), 839 "Hikyuu" 2 u đúng (1+1う); sweep 14 mục đã kiểm chứng trực tiếp — 836/837 KHÔNG có trong sweep (Ư trong "Ưm" là âm ん, không phải gasp Ư; っ cắt diễn bằng "!"); Ư cuối 759 là giá trị audit giữ nguyên; không dòng "Kh"; lượt soát 2: 18/18, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): dạng tách fa 11 dòng GIỮ "phù——a"/"phù, a" theo tiền lệ audit trong file (763 §2.1) — NGƯỢC với h9 đã merge (đổi sang romaji "Fu——a"/"Fu, a", 7 dòng); cần quyết một dạng duy nhất toàn dự án. 745 ぐっ→"Gu" vs "Khục" (tiền lệ 1833); họ ちゅう(っ) giữ "chụt"/"chùn chụt"; SFX độc thoại chưa áp công thức đếm (như cờ h9); 1831 （ふわっ → "Nhẹ nhàng", mất âm "Fuwa"); đề xuất "rộp" vẫn chờ Hieu.


# Moan-fix snippet — 凪ふかみh1_修学旅行の夜.txt.toml (moan-nagifukamih1-shuugaku-ryokou-no-yoru)

- File: `凪ふかみh1_修学旅行の夜.txt.toml` — route 07_Nagi_Fukami, 318 dòng script, TOML md5 `50c203c62f6e830c5e30413e09083b02` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 318 dòng, 0 key trùng; VN khớp TOML 318/318 sau chuẩn hóa `\n`/khoảng trắng.
- Đã đọc 318/318 dòng; xét 116 dòng rên/SFX (88 thoại + 28 SFX trong ngoặc).
- Đổi 26 dòng: 24 romaji + 1 đếm nguyên âm (1314 ああっ "A!"→"Aa!") + 1 sai âm (1232 くっ "Ư"→"Hự", thống nhất với 1229/1230).
- Romaji họ fa/fu (9): 1166, 1218, 1227, 1237, 1246 (×2 token), 1247, 1336, 1440, 1474 — ふあ→Fua, ふぁ→Fa, ふや→Fuya.
- Romaji họ ひゃ/ひゅ/ひあ/きゃ (15): 1214 Hyafu, 1216 Hyua, 1219 Hya, 1221 Hyufu, 1222 Hyau, 1223 Hyan, 1224 Hia, 1226 Hyapu, 1304 Nhyu, 1306 Nhyun, 1347 Hya, 1365 Hia, 1486 Kya + Hyau, 1487 Hyaun + Hyua, 1490 Kyau. Quyết định theo ủy quyền của Hieu: "Á" cho họ này là lỗi mất phụ âm mora (tiền lệ ポーレットh3, 凪h2, h7, 稀咲h3).
- Giữ 90 dòng rên/SFX: gasp Ư (16), hôn/liếm "chụt"/"liếm", hơi thở "phù", SFX ngoặc dạng động từ Việt (28), nói ngọng 1291/1303 (audit đã duyệt).
- Sweep: 5 mục đã kiểm chứng — 4 already-rendered đúng (1235, 1236, 1285, 2022), 1736 っ đã diễn thành "ư" — không đụng.
- Audit: key 1280 (あんっ→"An"), 1238/1252 (độ dài hơi thở), 2026/2027/2043 (SFX ướt) đã sửa trong audit — moan không sửa trùng.
- Lượt soát 2: tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0. JSON 26 mục, khóa string, jp/tw/old_vn khớp CSV3 26/26. Khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-nagifukamih1-shuugaku-ryokou-no-yoru-REVIEW.md`; danh sách sửa: `moan-nagifukamih1-shuugaku-ryokou-no-yoru-wrong.json`.

**Tổng cộng sau file này: 13 file / 318 dòng sai (moan)** (cơ sở 12 file / 292 dòng + 26 file này)


# Moan-fix snippet — ハチロクh8_桜色のひめごと.txt.toml (moan-hachiroku-h8-sakura-iro-no-himegoto)

- File: `ハチロクh8_桜色のひめごと.txt.toml` — route 01_Hachiroku, 332 dòng script, audit trước đó 63 sai.
- TOML md5: `818002990fb400412684b19303c9839c`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 332 dòng, 0 key trùng; flat-match VN–TOML 332/332.
- Đã đọc 332/332 dòng; xét 156 dòng rên/SFX (108 thoại rên + 45 SFX ngoặc đơn độc thoại + 3 độc thoại thở/cười).
- Đổi 3 dòng, đều là đếm nguyên âm: 778 はぁぁあ "Haaa"→"Haaaa" (4 a); 811 くひぃ×10 "Kuhiiiiiiiiii" (audit, 10 i)→"Kuhiiiiiiiiiii" (11 i — audit đếm nhầm ぃ×9); 827 んんんっ "ưm ưm"→"ưm ưm ưm" (gộp fix audit Fua/phù, khác fix audit chỉ ở phần rên).
- Không có dòng romaji mới: audit đã áp romaji cho họ fa/fu rất kỹ — đồng ý 46/48 dòng moan của audit (34 romaji + 9 gasp + đếm nguyên âm 709/734/736/749/782/835/836 đã đếm cơ học lại, đều đúng).
- Giữ 153 dòng rên/SFX (ひゃ/ひあ đã romaji sẵn Hya/Hia/Hyua — khớp quy tắc họ ひゃ quyết 21/11 ~11:55, file này không có dòng "Á" nào cho họ này; ふっ→"phù"; cười "Ufufu"; んっ→"ưm"; SFX từ hành động giữ nguyên độ dài kéo chữ theo tiền lệ audit).
- Sweep: 10 mục đã kiểm chứng — 8 audit đã sửa đúng, 2 already-rendered (732, 1584); không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
- Cờ cho đợt thống nhất: 1 (878 — đề nghị HỦY phần gỡ "ưm" của fix audit, giữ VN cũ "——ưm!"; JP có んっ riêng sau にっ, TW có 嗯, toàn file んっ đều diễn "ưm").
- Lượt soát 2: tổng 3 / tái kiểm chứng 3 / bỏ 0 / sửa 0. JSON 3 mục, khóa string, jp/tw/old_vn khớp CSV3 3/3. Khối TOML parse bằng tomllib: 3 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hachiroku-h8-sakura-iro-no-himegoto-REVIEW.md`; danh sách sửa: `moan-hachiroku-h8-sakura-iro-no-himegoto-wrong.json`.

**Tổng cộng sau file này: 14 file / 321 dòng sai (moan)** (cơ sở 13 file / 318 dòng + 3 file này) [parent REBASE 21/11 ~12:05 — snippet ghi cơ sở cũ 12/292 vì 凪ふかみh1 đã gộp trước]
- FLAG (đợt thống nhất): 878 — đề nghị HỦY phần gỡ "ưm" của fix audit, giữ VN cũ "Suzu muốn, tất cả——Ngài Soutetsu——ưm!" (JP んっ riêng sau にっ; TW 嗯; tiền lệ toàn file んっ→"ưm").
- Parent kiểm chứng 21/11 ~12:05: JSON 3 mục dạng chuẩn, khóa string; khối TOML 3 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 3/3 (1 bộ duy nhất, 332 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 811 JP く+ひ+ぃ×10 = 11 i — audit đếm nhầm ぃ×9 (10 i), fix moan 11 i đúng; 778 はぁぁあ = 4 a, "Haaaa" đúng; 827 んんん = 3 ưm, chỉ khác fix audit ở số ưm; không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi; lượt soát 2: 3/3, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): 878 — đề nghị HỦY phần gỡ "ưm" của fix audit, giữ VN cũ (JP んっ riêng sau にっ, TW 嗯, toàn file んっ→"ưm").

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

**Tổng cộng sau file này: 15 file / 341 dòng sai (moan)** (cơ sở 14 file / 321 dòng + 20 file này) [parent REBASE 21/11 ~12:05 — snippet ghi cơ sở 13/318 vì ハチロクh8 đã gộp trước]
- Parent kiểm chứng 21/11 ~12:05: JSON 20 mục dạng chuẩn, khóa string; khối TOML 20 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 20/20 (1 bộ duy nhất, 327 dòng); TOML md5 khớp audit; 6 key trùng audit chỉ khác đúng token rên (1410 Hya→Hia + Fua, 1424/1429/1433/1436/1440 Haa→Fa/Fua — "YuunƯ"/"AhyuƯ"/"AƯ" và "Em, em"/"máy tính bảng" đều là giá trị audit giữ nguyên); đếm nguyên âm kiểm chứng độc lập: 1428 5 a, 1442 3 a, 1443 6 a, 1425 "Faa" 2 a, 1453 "Uaaaa" 4 a, 1466 "Rerooo" 3 o, 1715 "Reruuuuuuu" 7 u — đều đúng; sweep 20 mục cho file này đã kiểm chứng (9 mục còn lại thuộc ハチロクh2_お勉強の成果, file khác), 1567 KHÔNG có trong sweep (gasp mới, audit sót — ぁっ cuối tuyệt đối dòng 1, thêm Ư theo đúng ranh giới gasp); không dòng "Kh" nào bị đổi (1473 chỉ chứa chữ "không"); lượt soát 2: 20/20, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 1484 (くっ→"Ku" vs audit giữ "Ưm" — tiền lệ Paulette h3 906); F2 chuỗi SFX miệng "chụt" vs romaji (1475/1476/1479/1481/1715); F3 gasp っ―― (1582, 1589); F4 SFX độc thoại 2166–2210; F5 Fa/Fua chặt vs h8 (h8 dùng "Fua" cho cả ふぁ); F6 1473.

---

# Moan-fix snippet — lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml

- File: lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml (01_Hachiroku, 331 dòng script).
- Đã đọc 331/331 dòng; 220 dòng chứa token ứng cử viên rên/SFX.
- Audit đã áp romaji fa/fu + họ ひゃ từ trước (34 dòng rên) — đợt moan này chỉ kiểm chứng lại, sửa 2 dòng.
- Sửa 1232: はひゅっ "hahu" → "hahyu" (mất âm ゅ; cùng token diễn đúng "Hahyu" ở 1240).
- Sửa 1307: gasp っ thứ hai sau ―― bị mất, "Ưm——!" → "Ưm——Ư!" (ghi đè quyết định giữ nguyên của audit §4 + phân loại already-rendered của sweep — parent chốt lúc gộp).
- Xác nhận cờ audit: họ ちゅう bỏ 't' cuối khi JP không có っ (1277/1279/1283/1287) đúng; 1224 ふあっっっっ → "Fua!!!!!" đúng (っ×4 là nhấn mạnh).
- Giữ nguyên: 34 dòng rên audit, 15 gasp sweep, 15 dòng SFX （ ） theo quy ước, rên ngắn La-tinh không thêm Ư, không dòng "Kh" nào bị đổi, không còn "Á" cho họ ひゃ.
- Cờ: F1 1307 cần parent chốt; F2 đếm lặp phụ âm SFX （ ） lệch ±1–2 (1909/1966/1983); F3 しゅこんっ "Ngậm lấy" vs "Nắm chặt" theo ngữ cảnh; F4 1192 りゅっ→"mất" (ngoài phạm vi moan); F5 1370 っ giữa câu giữ không Ư.
- Lượt soát 2: tổng 2 / tái kiểm chứng 2 / loại bỏ 0 / sửa lại 0.
- TOML block: parse-verified (tomllib), 2 khóa, 0 sai lệch giá trị vs wrong.json.

**Tổng cộng sau file này: 16 file / 343 dòng sai (moan)** (cơ sở 15 file / 341 dòng + 2 file này)
- Parent kiểm chứng 21/11 ~12:35: JSON 2 mục dạng chuẩn, khóa string; khối TOML 2 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 2/2 (1 bộ duy nhất, 331 dòng); TOML md5 khớp audit; 1232 chỉ khác giá trị audit đúng token "hahu"→"hahyu" (cùng token diễn đúng "Hahyu" ở 1240); 1307 GIỮ fix của agent ("Ưm——Ư!") — quyết của parent: mẫu っ――っ audit đã thêm Ư ở 1378/1385/1642, phân loại already-rendered của sweep là heuristic sai ("Ưm" chỉ diễn うむっ, tiếng っ thứ hai sau ―― mất hẳn); cờ F1 đã giải quyết, không còn chờ. Lượt soát 2: 2/2, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F2 (đếm lặp phụ âm SFX （ ） lệch ±1–2: 1909/1966/1983); F3 (しゅこんっ "Ngậm lấy" vs "Nắm chặt" theo ngữ cảnh); F4 (1192 りゅっ→"mất", ngoài phạm vi moan); F5 (1370 っ giữa câu giữ không Ư).

---

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

**Tổng cộng sau file này: 17 file / 377 dòng sai (moan)** (cơ sở 16 file / 343 dòng + 34 file này) [parent REBASE 21/11 ~12:35 — snippet ghi cơ sở cũ 15/341 vì lr_ハチロクh3 đã gộp trước]
- Parent kiểm chứng 21/11 ~12:35: JSON 34 mục dạng chuẩn, khóa string; khối TOML 34 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 34/34 (1 bộ duy nhất, 404 dòng); TOML md5 khớp audit; 22 key trùng audit — kiểm chứng bằng diff: mọi fix chỉ khác giá trị audit đúng token rên (Phà/phà→Fa/Fua/fua + đếm nguyên âm 1581/1590; 1479 "Bổn tiểu thư——" là giá trị audit giữ nguyên, moan chỉ đổi "Phà"→"Fua"); 12 key fix==old_vn đều là hoàn lại đúng token fa/fu audit đã đổi (tiền lệ lr追加/h2); 12 key mới đều đếm nguyên âm, kiểm chứng độc lập 12/12 theo công thức (1477 3a, 1483 7a+n, 1491 5a+n, 1507 Haa/fuu, 1552 2u, 1574 2a, 1599 2a×4, 1614 2a×4, 1677 2a+8a+n, 1695 2a×2, 1789 2a, 1485 2u); sweep 17 mục không đụng (0 key trùng); không dòng "Kh" nào bị đổi ("Khịt"/"Khoan" là từ cũ giữ nguyên); không dòng gasp Ư nào bị đụng; lượt soát 2: 34/34, 0 bỏ, 1 sửa (1491 6a→5a).
- FLAG (đợt thống nhất): F1 (kiểu hơi thở "fu" vs "phù" 1502/1505); F3 ("Nfufuun" vs kiểu "Fufu-n" của audit ở 1550); F5 (hai kiểu diễn độ dài A~~ vs Haa trong cùng dòng 1695); các cờ F2/F4/F6 trong REVIEW ghi lại, không quyết.

---

# Moan-fix snippet — lr_れいなh1_レディ・れいな.txt.toml (moan-lr-reinah1-lady-reina)

- File: `lr_れいなh1_レディ・れいな.txt.toml` — route 04_Reina, 311 dòng script, TOML md5 `229a246bcd0ae55d389ed9f3493620b3` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 311 dòng, 0 key trùng; VN khớp TOML 311/311 sau chuẩn hóa `\n`/khoảng trắng.
- Đã đọc 311/311 dòng; xét ~216 dòng rên/SFX; đổi 48, giữ ~168.
- Đổi 48 dòng: 39 romaji + 6 đếm nguyên âm + 2 sai âm + 1 gasp.
- Romaji họ fa/fu → Fa/Fua/Fan/Fe/Fue/Fuya (22 dòng riêng): 1179, 1180, 1183, 1185, 1199, 1201, 1202, 1203, 1204, 1207, 1208, 1210, 1211, 1212, 1214, 1215, 1217, 1218, 1231, 1232, 1236, 1424 (+ 1173/1175 cũng chứa token fa/fu, gộp trong dòng họ hya). Dùng Hepburn chặt Fa (ふぁ) / Fua (ふあ) / Pa (ぷぁ) / Pua (ぷあ) — khớp đa số tiền lệ (凪h2, lr-h2, lr-h1).
- Romaji họ ひゃ/ひゅ/ひあ/きゃ/きゅ (12): 1170 Kyaan, 1171 Hyua, 1173 Kyafuuuuuu (6 u), 1174 Hyauuuun (4 u), 1175/1176 Hyau, 1177 Pyayau, 1303 Nkyuuuuuuuuu (9 u), 1304 Nkyuuuuuuu (7 u) + Yaan, 1306/1307 Nhyu, 1308 Nkyun.
- Cười là tiếng cười (5): 1197 Ufufuu~, 1257 Nfufu~, 1298 Nfufu~ + Horehyaa + Hihihahyuhyo~, 1299 Nfufu~~, 1328 Ufufuu~.
- Đếm nguyên âm (6): 1169 MỚI "Kya a a a♪" (4 a, audit bỏ sót), 1226 "Oa a a", 1244/1284/1584 "Aa——", 1288 "Aa.".
- Sai âm (2): 1285 ぉっ→"Ô——a", 1305 んぉっ→"Ôm!?". Gasp (1): 1279 っっ→"ƯƯ!!!".
- 47/47 fix moan của audit kiểm chứng đúng và áp nguyên; 2 điểm khác audit: 1169 mới (thêm 1 a) + 1218 sửa dấu câu "Pua!?"→"Pua!!?" (khớp JP ！！？ và VN cũ).
- 8 dòng gasp sweep của audit không đụng (904, 1258, 1282, 1431, 1432, 1433, 1434, 1440); 5 dòng đại từ của audit không đụng; không dòng "Kh" nào bị đổi; sweep 15 mục đã kiểm chứng trực tiếp.
- Giữ ~168 dòng rên/SFX (rên ngắn La-tinh 905/1242/1247/1252/1253/1301/1243/1228/1238/1248/1255/1429/1430/1275/1276, tiếng rên kiểu chó 1379/1381/1436 "Ư ử", hơi thở "phù"/"phu", chuỗi SFX miệng ちゅ/ぺ/じゅ + SFX độc thoại （ ） theo quy ước file).
- Flag: F1 1225 くっ→"Ư" (vs "Ku"/"Hự", tiền lệ Paulette h3 906) + 1312; F2 1240 ふか、いっ→"sâu, quá"; F3 おまんこ "lồn" vs "chỗ đó" 2/2; F4 SFX miệng mất phụ âm đầu (1254 かぁぷっ→"A mút!", 1220 くぷっ→"Chụt mút"); F5 dạng tách "Kya a a a" vs gộp "Kyaaaa" toàn dự án; F6 SFX （ ） chưa áp công thức đếm (1860/1864/1898/1899/1906/1913).
- Lượt soát 2: tổng 48 / tái kiểm chứng 48 / bỏ 0 / sửa 1 (1218). JSON 48 mục, khóa string, jp/tw/old_vn khớp CSV3 48/48. Khối TOML parse-verified (tomllib), 48 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-reinah1-lady-reina-REVIEW.md`; danh sách sửa: `moan-lr-reinah1-lady-reina-wrong.json`.

**Tổng cộng sau file này: 18 file / 425 dòng sai (moan)** (cơ sở 17 file / 377 dòng + 48 file này)
- Parent kiểm chứng: JSON 48 mục dạng chuẩn, khóa string; khối TOML 48 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 48/48 (1 bộ duy nhất, 311 dòng); TOML md5 khớp audit; 47/48 key trùng audit — chỉ khác giá trị audit đúng token rên (phà/phùa/phù/phuê/phuya→Fa/Fua/Fu/Fue/Fuya, ひあ Hya→Hia) + 2 điểm: 1169 MỚI (きゃあああ 4 a, audit bỏ sót — đếm độc lập đúng) và 1218 sửa dấu câu "Pua!?"→"Pua!!?" (khớp JP ！！？); đếm nguyên âm kiểm chứng độc lập: 1173 6u, 1303 9u, 1304 7u, 1174 4u, 1979 n/a; 1279 っっ→"ƯƯ" (audit fix, 1 Ư cũ thiếu 1 っ); không key đại từ nào (1153/1234/1339/1353/1423), không key gasp sweep nào (904/1258/1282/1431–1434/1440); không dòng "Kh" nào bị đổi; lượt soát 2: 48/48, 0 bỏ, 1 sửa (1218).
- FLAG (đợt thống nhất): F1 (1225 くっ→"Ư" vs "Ku"/"Hự" — tiền lệ h3 906 dùng "Ku", audit file này giữ "Ư"; chưa quyết, chờ quyết くっ một lần toàn dự án) + F5 (dạng tách "Kya a a a" vs gộp "Kyaaaa"); F2 (1240), F3 (おまんこ "lồn" vs "chỗ đó" — chờ Hieu), F4 (SFX miệng mất phụ âm đầu 1254/1220), F6 (SFX （ ） chưa áp công thức đếm). GHI CHÚ: file này dùng "Ya!" cho やっ (1304) — NGƯỢC với jiekei đã gộp (giữ "Á" cho やっ); cần quyết や một lần toàn dự án ở đợt thống nhất.

---

# Moan-fix snippet — れいなh4_ふたりっきりのハロウィン.txt.toml (moan-reinah4-futarikkiri-halloween)

- File: `れいなh4_ふたりっきりのハロウィン.txt.toml` — route 04_Reina, 584 dòng script, TOML md5 `43ddc25620d65d8d021ab6e6572b5caa` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 584 dòng, 0 key trùng; VN khớp TOML 584/584 sau chuẩn hóa `\n`.
- Đã đọc 584/584 dòng; xét ~200 dòng rên/SFX (fa/fu 34 dòng / 46 token, họ ひゃ 35, gasp Ư 6, cười 15, rên dài 20, SFX miệng 30, SFX độc thoại （ ） 30).
- Đổi 43 dòng: 34 romaji fa/fu + 9 sửa mới.
- Romaji fa/fu → Fa/Fua/Fue/Fuya/Fu (Hepburn chặt): toàn bộ 34 dòng audit (1784–2459) đưa về La-tinh — VN cũ vốn đã là La-tinh, audit đã Việt hoá; 5 dòng hoàn lại đúng VN cũ (2015, 2452, 2453, 2454, 2457). Trong đó 2 dòng sửa cả ひあ "Hya"→"Hia" (1885, 1999); 3 dòng sửa thêm đếm (1967 Fuyaa 2a, 1986 Faaaan 3a, 2458 Fuaaaaaa 6a); 1 dòng thêm gasp (2459-final "aƯ").
- Đếm nguyên âm mới (5): 1979 16a (bớt 2), 1984 7u (thêm 1), 2044 10u (thêm 1), 2155 3u (bớt 1), 2021 "Nhyan" (2n, bớt 2n; っっっ→"!!!").
- SFX miệng ちゅ (3): 1994/2043 ちゅううっ→"chụụụt" (3ụ), 2047 ちゅうっ→"chụụt" (2ụ) + ちゅむっ→"chumu" — tiền lệ Paulette h3 đã gộp.
- Gasp audit bỏ sót (2): 1988 はぅうっ→"HauuƯ", 2459-final あっ→"aƯ" — tiền lệ lr-h2 1567/1433 đã gộp.
- Giữ: 6 gasp Ư sweep/audit (1962, 1963, 1990, 2022, 2972, 3095), 3 cười audit "Ufufu~" (2099/2104/2111), 33 dòng họ ひゃ đã romaji, toàn bộ 30 SFX độc thoại （ ）, hơi thở tập thở 1883/2533/2562.
- Sweep: 5 mục đã kiểm chứng — không đụng. Không dòng "Kh" nào trong file.
- Cờ cho đợt thống nhất: F1 Fa/Fua chặt vs h8 ("Fua" cho cả ふぁ); F2 ふっ→"Fu" vs "phù" (h8); F3 họ ちゅう(っ) (h3 dùng chụụt/chumu, h7 giữ "chụt") + SFX （ ） chưa áp công thức đếm; F4 hơi thở tập thở 1883/2533/2562; F5 2 gasp thêm mới chờ parent chốt lúc gộp; F6 2021 "Nhyan"; F7 đếm audit sửa lại (1967 thiếu 1a); F8 2288 (audit, chờ Hieu kiểm tra trong game).
- Lượt soát 2: tổng 43 / tái kiểm chứng 43 / bỏ 0 / sửa 0. JSON 43 mục, khóa string, jp/tw/old_vn khớp CSV3 43/43. Khối TOML parse-verified (tomllib), 43 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-reinah4-futarikkiri-halloween-REVIEW.md`; danh sách sửa: `moan-reinah4-futarikkiri-halloween-wrong.json`.

**Tổng cộng sau file này: 19 file / 468 dòng sai (moan)** (cơ sở 18 file / 425 dòng + 43 file này) [parent REBASE — snippet ghi cơ sở cũ 17/377 vì lr_れいなh1 đã gộp trước]
- Parent kiểm chứng: JSON 43 mục dạng chuẩn, khóa string; khối TOML 43 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 43/43 (1 bộ duy nhất, 584 dòng); TOML md5 khớp audit; 34/34 key trùng audit chỉ khác đúng token rên (phà/phùa/phù/phuê/phuya→Fa/Fua/Fu/Fue/Fuya, ひあ Hya→Hia) + đếm sửa 1967 ("phuya" 1a→"Fuyaa" 2a, audit thiếu 1a) và gasp mới 2459; 9 key mới đều moan-only; đếm nguyên âm kiểm chứng độc lập: 1979 16a (JP 12あ+4ぁ), 1984 7u, 2044 10u, 2155 3u, 2021 2n + っっっ→"!!!", 1994/2043 "chụụụt" 3ụ, 2047 "chụụt" 2ụ + "chumu" (tiền lệ h3); 5 key fix==old_vn (2015/2452/2453/2454/2457) đều là hoàn lại đúng token fa/fu audit đã đổi; không dòng "Kh" (file không có); lượt soát 2: 43/43, 0 bỏ, 0 sửa.
- 2 GASP MỚI — parent CHỐT lúc gộp (giữ fix của agent): 1988 はぅうっ→"HauuƯ" (っ cuối tuyệt đối mất hẳn trong VN cũ "Hauu", tiền lệ lr-h2 1567) và 2459-final あっ→"aƯ" (っ cuối dòng mất hẳn, VN cũ kết "...Fua——a"); cả hai đều là っ mất hoàn toàn, không phải double-render.
- FLAG (đợt thống nhất): F1 (Fa/Fua chặt vs h8); F2 (ふっ→"Fu" vs "phù"); F3 (họ ちゅう(っ) chụụt/chumu vs h7 giữ "chụt"); F4 (hơi thở tập thở 1883/2533/2562); F6 (2021 "Nhyan"); F7 (đếm audit sửa 1967); F8 (2288 chờ Hieu kiểm tra trong game).

---

# Moan-fix snippet — lr_真闇h1_僕のおねえちゃん.txt.toml (moan-lr-mayamih1-boku-no-oneechan)

- File: `lr_真闇h1_僕のおねえちゃん.txt.toml` — route 05_Mayami, 317 dòng script, audit trước đó 59 sai.
- TOML md5: `4baa00ccc02ca48bed882887b182d798`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 317 dòng, 0 key trùng; VN khớp TOML 314/317 (3 dòng còn lại chỉ khác TOML-2 làm phẳng `\n` thành khoảng trắng).
- Đã đọc 317/317 dòng; xét 175 dòng rên/SFX/gasp (112 thoại rên + 63 SFX ngoặc đơn độc thoại).
- Đổi 7 dòng: 1167 はぁっ×3 "Hà"→"Haa" (audit bỏ sót, cùng lỗi 1659); 1433 ふぅっっっ "Fuuuu"→"Fuu" (fix audit "Foo" sai nguyên âm — THAY THẾ giá trị audit); 1457 んふふっ "ưm fufu"→"Nfufu" (một âm, một cách diễn; tiền lệ toàn file); 1464 ァァァ "Aaaa"→"Aaa" (3 a); 1598 thêm "ha" cho はっ (THAY THẾ giá trị audit — giữ đại từ + gasp của audit); 1816 thêm "ku" cho くっ―― cuối độc thoại (TW 嗚); 2029 ああ cuối độc thoại "a"→"aa".
- Kiểm chứng 17 fix rên/SFX của audit: 16 đúng (đếm cơ học lại 1466 12 a, 1467 8 a, 1492 19 u, 2145 11 t, 1531 6 u, 1484 3 a — đều đúng), chỉ 1433 sai nguyên âm. Không có dòng romaji mới cho họ ひゃ/ひあ/きゃ.
- Giữ ~168 dòng rên/SFX (họ ふぁ→"Fua", はぁ→"Haa", くあ→"Kua", んひゅ→"Nhyu", cười "Nfufu"/"Ufufu", んっ→"Ưm", SFX từ Việt theo quy ước file; っ nhấn mạnh cuối câu không thêm Ư).
- Sweep: 20 mục đã kiểm chứng — 16 audit đã áp đúng, 4 already-rendered (1428, 1503, 1698, 1803); không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
- Cờ cho đợt thống nhất: 2 (1433 — dùng "Fuu!!!!" thay "Foo!!!!" của audit; 1598 — dùng giá trị moan có "ha", thay giá trị audit).
- Lượt soát 2: tổng 7 / tái kiểm chứng 7 / bỏ 0 / sửa 0. JSON 7 mục, khóa string, jp/tw/old_vn khớp CSV3 7/7. Khối TOML parse bằng tomllib: 7 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-mayamih1-boku-no-oneechan-REVIEW.md`; danh sách sửa: `moan-lr-mayamih1-boku-no-oneechan-wrong.json`.

**Tổng cộng sau file này: 20 file / 475 dòng sai (moan)** (cơ sở 19 file / 468 dòng + 7 file này)
- FLAG (đợt thống nhất): 1433 — dùng giá trị moan 「Fuu!!!!」 thay fix audit 「Foo!!!!」 (JP ふぅ = fuu, codepoint U+3045; TW 呼嗚). 1598 — dùng giá trị moan có "ha——" thay giá trị audit (khôi phục hơi thở はっ, tiền lệ 1630).
- Parent kiểm chứng 21/11 ~14:15: JSON 7 mục dạng chuẩn, khóa string; khối TOML 7 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 7/7 (1 bộ duy nhất, 317 dòng); TOML md5 khớp audit; 1433 chỉ khác fix audit đúng nguyên âm "oo"→"uu" (JP ふぅ = 2 u theo công thức); 1598 chỉ thêm "ha——" vào fix audit (đại từ "Tôi" + gasp Ư là của audit, không phải sửa mới); 5 key mới đều moan-only — đếm nguyên âm kiểm chứng độc lập: 1167 2a×3, 1464 3a, 2029 2a; 1457 "Nfufu" (tiền lệ toàn file); 1816 "ku" (tiền lệ Paulette h3 906); không dòng "Kh" nào bị đổi; lượt soát 2: 7/7, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): 1433 — dùng giá trị moan "Fuu!!!!" thay fix audit "Foo!!!!"; 1598 — dùng giá trị moan có "ha——" thay giá trị audit.
---

# Moan-fix snippet — ハチロクh1_契り.txt.toml (moan-hachiroku-h1-chigiri)

- File: `ハチロクh1_契り.txt.toml` — 353 dòng script, TOML md5 `ea6d9621d4124d9a966b6842fe53b602`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 353 dòng, 0 key trùng, 0 VN trống; flat-match TOML 353/353.
- Đã đọc 353/353 dòng; xét 101 dòng rên/SFX (63 thoại rên + 38 SFX trong ngoặc).
- Đổi 1 dòng (1248): んううっ "Ưm ư"→"Ưm ưư" (thiếu 1 ư — audit áp sai tiền lệ h9 2144 chỉ có 1 う) + んひゅっ "ưm hyu"→"Nhyu" (quy tắc 3b; tiền lệ h8 2187 audit viện dẫn KHÔNG tồn tại — h8 không có key 2187).
- Audit file này đã áp romaji rất kỹ: 39/40 dòng moan của audit kiểm chứng lại là đúng (chỉ thay thế 1248); fix moan khác fix audit chỉ ở 2 chỗ rên trên.
- Hệ SFX trong ngoặc diễn theo nghĩa hành động GIỮ NGUYÊN (quyết theo tiền lệ moan-fix h8); 10 chỗ sai âm audit đã sửa đúng.
- Sweep: 6 mục cho đúng file này đã kiểm chứng (1242, 1371, 1376, 1463, 1508, 1519 — audit áp đúng, không đụng lại); không đổi dòng "Kh" nào, không xem lại dòng gasp Ư nào.
- Cờ cho Hieu: 1238 いっ→"I" (audit phán đoán, Hieu có thể trả về "Á").
- Lượt soát 2: tổng 1 / tái kiểm chứng 1 / bỏ 0 / sửa 0. JSON 1 mục, khóa string, jp/tw/old_vn khớp CSV3 1/1. Khối TOML parse bằng tomllib: 1 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hachiroku-h1-chigiri-REVIEW.md`; danh sách sửa: `moan-hachiroku-h1-chigiri-wrong.json`.

**Tổng cộng sau file này: 21 file / 476 dòng sai (moan)** (cơ sở 20 file / 475 dòng + 1 file này) [parent REBASE 21/11 ~14:15 — snippet ghi cơ sở cũ 19/468 vì lr_真闇h1 đã gộp trước]
- FLAG (cho Hieu): 1238 いっ → "I" (audit phán đoán; nếu Hieu thấy "Á!" tự nhiên hơn thì trả về "Á" — một dòng, dễ revert).
- Parent kiểm chứng 21/11 ~14:15: JSON 1 mục dạng chuẩn, khóa string; khối TOML 1 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 1/1 (1 bộ duy nhất, 353 dòng); TOML md5 khớp audit; 1248 chỉ khác fix audit đúng 2 token rên ("ưm ư"→"ưm ưư" — JP んううっ 2う; "ưm hyu"→"Nhyu" theo quy tắc 3b); tiền lệ "h8 2187" mà audit viện dẫn KHÔNG tồn tại (không có trong CSV3 lẫn audit wrong.json của h8); không dòng "Kh" nào bị đổi; lượt soát 2: 1/1, 0 bỏ, 0 sửa.
- FLAG (cho Hieu): 1238 いっ → "I" (audit phán đoán; Hieu có thể trả về "Á" — 1 dòng, dễ revert).

---

# Moan-fix snippet — ポーレットh1_ファーストセックス (moan-paulette-h1-fasuto-sekkusu)

- File: `ポーレットh1_ファーストセックス.txt.toml` — 298 dòng script, TOML md5 `f70333e73074278312745a1870038ea3`, không có bản trùng.
- CSV3: 1 bộ duy nhất, khớp TOML 298/298 (lệch phẳng `\n` ↔ khoảng trắng đã chuẩn hoá).
- Đã đọc 298/298 dòng; xét 92 dòng rên/SFX (56 thoại rên + 31 SFX trong ngoặc + 3 trần thuật tiếng thở + 2 SFX trong thoại).
- Đổi 16 dòng: 13 romaji + 1 đếm nguyên âm + 2 sai âm.
- Romaji: 976 `Fuaa` (thay "phà" của audit), 977 `Kya`, 978 `I——Hyuuuuuuuuuuuuuuu` (15 u), 979 `Kyafuuuuuuuu` (8 u), 981 `Kyau`, 982 `Kya`, 985 `Ka`, 987 `Fa` (thay "Phà" của audit), 989 `Kyafu`, 996 `An`, 1019 `chuzooooo` (5 o), 1065 `Fa` + `ư` (thay "phà"/"ưm" của audit), 1106 `ưm kyu` (thay "ưm!" của audit).
- Đếm nguyên âm: 1006 13 a (JP ぁ×2 + あ×11, VN cũ 12).
- Sai âm: 1042 ああ→`Aa` (VN cũ "Ừm!"), 1758 ぐううっ→`Hựựự` (VN cũ "Phập phập!").
- 4 key trùng audit (976, 987, 1065, 1106): fix moan chỉ khác fix audit ở đúng token rên (đã kiểm chứng diff).
- Giữ 76 dòng rên/SFX (980 `Hyau!`, 993/997/998 chuỗi "a", 1002/1017/1026/1041 "ưm/phù", 1027/994 "hự", 1010–1017 chuỗi liếm, 1022/1186 くぅん theo tiền lệ h3 giữ tên, SFX （ ） trừ 1758).
- Sweep: 6 mục đã kiểm chứng (983, 984, 988, 995, 1007, 1015) — đều đã áp qua audit, không đụng trong đợt này. Không dòng "Kh" nào.
- Cờ cho vòng audit: 3 gasp bị bỏ sót (1005 っ――→"A——", 1184 っ―― giữa bị mất, 985 ぃっ cuối bị mất). Cờ cho đợt thống nhất: くぅん sau tên (1022/1186), phần nghĩa audit ở 976/1065, 1057 をっ.
- Lượt soát 2: tổng 16 / tái kiểm chứng 16 / bỏ 0 / sửa 0. JSON 16 mục, khóa string, jp/tw/old_vn khớp CSV3 16/16. Khối TOML parse bằng tomllib: 16 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h1-fasuto-sekkusu-REVIEW.md`; danh sách sửa: `moan-paulette-h1-fasuto-sekkusu-wrong.json`.

**Tổng cộng sau file này: 22 file / 492 dòng sai (moan)** (cơ sở 21 file / 476 dòng + 16 file này)
- Parent kiểm chứng 21/11 ~14:35: JSON 16 mục dạng chuẩn, khóa string; khối TOML 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 16/16 (1 bộ duy nhất, 298 dòng); TOML md5 khớp audit; 4 key trùng audit chỉ khác đúng token rên — 1065 có thêm phán đoán うっ→"ư" (tiền lệ ふかみh1 1046 ふ……うっ→"phù……ư": うっ trần diễn "ư", "ưm" thừa m) và "anh Soutetsu" ở 1106 là giá trị audit giữ nguyên (moan chỉ thêm " kyu"); đếm nguyên âm kiểm chứng độc lập: 978 15u (JP ひゅ+14う), 979 8u (ふ+7う), 1006 13a (ぁ×2+あ×11), 1019 5o (ぞ+4お); sweep 6 mục không đụng (983/984/988/995/1007/1015); không dòng "Kh" nào bị đổi; lượt soát 2: 16/16, 0 bỏ, 0 sửa.
- FLAG (vòng audit / đợt thống nhất): 1005 + 1184 + 985 (3 gasp っ bị bỏ sót — thuộc vòng audit, không tự sửa); くぅん sau tên 1022/1186 (giữ tên theo tiền lệ h3); 1057 をっ; phần nghĩa audit ở 976/1065.

---

# Moan-fix snippet: lr_ふかみh2_セックスの意味.txt.toml

- File: `07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml` — route 07_Nagi_Fukami, 291 dòng script, TOML md5 `896562ad2c4430d5219eef5d177b99c5`, không có bản trùng.
- CSV3: bẫy dual-set — bộ `07_Nagi_Fukami` STALE (khớp TOML 5/291), bộ tốt `11_Other` (khớp phẳng 291/291); chỉ dùng bộ tốt. 0 key trùng.
- Đã đọc 291/291 dòng; xét 166 dòng rên/SFX (97 thoại + 69 độc thoại).
- Đổi 34 dòng: 31 romaji + 2 sai âm + 1 đếm nguyên âm.
- Romaji họ fa/fu (25): 987, 1016, 1030, 1039, 1087, 1094, 1101, 1104, 1136, 1138, 1139, 1179, 1191, 1260, 1262, 1266, 1267, 1268, 1269, 1270, 1272, 1273, 1275 (×2), 1276, 1277 — ふぁ→Fa, ふあ→Fua, ぷぁ→Pa, ぷあ→Pua, ふや→Fuya, ふ……ぁ→Fu……a (Hepburn chặt; tiền lệ 凪ふかみh1 mẫu, lr_ポーレットh1, lr_凪ふかみh1 1502). Audit bỏ sót 3 dòng họ pu (1136/1138/1139).
- Romaji họ ひゃ/ひゅ (6): 1018 Hyau, 1019 Hyau, 1022 Hya, 1029 Nhyu, 1063 Hya, 1096 Nhyu (quy tắc 3b; んひゅ→Nhyu).
- Sai âm (2): 1060 はうっ "Ah"→"Hau" (1061 đã dùng "Hau"); 1195 くっ "ư"→"hự" (quy ước trong file くっ→"Hự" ×3).
- Đếm nguyên âm (1): 1085 あ×19 "A"×18→"A"×19 (giữ gasp ƯƯ của audit).
- Chồng lấn audit: 24 key chỉ khác fix audit đúng token rên; 10 key mới (1018, 1019, 1022, 1029, 1060, 1096, 1136, 1138, 1139, 1195).
- Giữ 132 dòng rên/SFX: gasp Ư audit (1068, 1069, 1071, 1072, 1099, 1105, 1107, 1125, 1127, 1558, 1588, 1598), already-rendered (1035, 1070, 1763), hơi thở "phù" (1063, 1264), はぁ→"Ha", cười Fufu/Ufufu/Ehehe, SFX chuỗi miệng + SFX ngoặc (1717–1775), っ nhấn mạnh cuối câu (audit §4).
- Sweep: 21 mục đã kiểm chứng trực tiếp (3 áp nguyên + 4 already-rendered + 12 needs-file-audit đã giải quyết + 2 uncertain: 1078 giữ "Kh", 1588 audit sửa Ư) — không đụng dòng gasp Ư nào; không dòng "Kh" nào bị đổi. Đính chính: sweep 1566 KHÔNG thuộc file này (của ふかみh2_homesweethome); các dòng "Kh" 989/997/1017/1731/1739 cũng không thuộc file này.
- Lượt soát 2: tổng 34 / tái kiểm chứng 34 / bỏ 0 / sửa 0. JSON 34 mục, khóa string, jp/tw/old_vn khớp CSV3 (bộ tốt) 34/34. Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- FLAG (đợt thống nhất): F1 1063 "Anh——Hya——hau——" (tách token Hya; phương án gộp "Anhya"); F2 1125 đếm âm mơ hồ (15 a + 2 u vs 18 á — audit giữ); F3 1078 sweep uncertain giữ "Kh"; F4 1085 ghi đè quyết định giữ của audit (19 a vs 18 a); F5 1195 くっ→"hự" (audit không bàn); F6 1770 っ sau 羽 giữ (mẫu gasp 1558/1588?); F7 Fa/Fua chặt vs h8 dùng "Fua" cho cả ふぁ.
- Chi tiết đầy đủ: `moan-lr-fukamih2-sekkusu-no-imi-REVIEW.md`; danh sách sửa: `moan-lr-fukamih2-sekkusu-no-imi-wrong.json`.

**Tổng cộng sau file này: 23 file / 526 dòng sai (moan)** (cơ sở 22 file / 492 dòng + 34 file này) [parent REBASE 21/11 ~14:35 — snippet ghi cơ sở cũ 21/476 vì ポーレットh1 đã gộp trước]
- Parent kiểm chứng 21/11 ~14:35: JSON 34 mục dạng chuẩn, khóa string; khối TOML 34 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 34/34 (bộ tốt 11_Other, 291 dòng; bộ 07_Nagi_Fukami stale 5/291 đã loại); TOML md5 khớp audit; 24 key trùng audit chỉ khác đúng token rên (phà/phù→Fa/Fua, Ah→Hyau, 1087 "Ph"→"F"); 10 key mới đều moan-only; đếm nguyên âm kiểm chứng độc lập: 1085 JP 19 a (あ+ぁ×8+あ×10) — audit giữ 18 a, fix moan 19 a đúng, ƯƯ của 1085 là giá trị audit giữ nguyên; 1063 ƯƯƯ là giá trị audit giữ nguyên (moan chỉ thêm "——Hya"); sweep 21 mục đã kiểm chứng (1029/1063/1179/1260 chỉ khác đúng token rên, không đụng dòng gasp Ư nào); không dòng "Kh" nào bị đổi (1078 giữ "Kh" theo sweep uncertain); lượt soát 2: 34/34, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 (1063 tách token "Anh——Hya——hau" vs gộp "Anhya"); F2 (1125 đếm âm mơ hồ); F3 (1078 giữ "Kh"); F4 (1085 19 a vs 18 a của audit — parent chốt 19 a đúng); F5 (1195 くっ→"hự" — tiền lệ trong file 1066/1070/1273 + 凪ふかみh1 1232); F6 (1770 っ sau 羽); F7 (Fa/Fua chặt vs h8).

---

# Moan-fix snippet — 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml (moan-hibikih6-orienteering-karimono)

- File: `日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml` — route 02_Hibiki, 667 dòng script, TOML md5 `77423bec9e1cb3f3bfbb14002019ad44` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 667/667 key khớp TOML.
- Light check: đã đọc 667/667 dòng; xét 134 dòng ứng viên rên/SFX (fa/fu 24, họ hya 7, SFX hôn/mút 11, SFX hành động 20, cười 5, gasp/thán từ 67).
- Đổi 2 dòng: 2075 sửa giá trị fix audit về đúng 6u (`Kyafuuuuuun`, JSON audit đang sai 5u dù review ghi 6u) + giữ `Fua`; 2082 やっ "a"→"Ya" (mất phụ âm y, tiền lệ 2085/Paulette h3).
- Kiểm chứng audit: 32 dòng moan của audit kiểm chứng lại bằng máy — 31 đúng, 1 sai giá trị (2075). Họ hya 0 dòng dùng "Á" (toàn romaji đúng). 2078 giữ nguyên 14u (parent đã loại khỏi audit, đếm lại đúng). Không đụng gasp Ư hay "Kh".
- Giữ: dạng tách âm "phù, a" (1944, 2106, 2194, 2713), "Hà" cho はぁっ, cười "Ehehe/Ufufufu", SFX "chụt/Phụt/ực/hự", 2087 "a――――", 2656 "A!".
- Lượt soát 2: tổng 2 / tái kiểm chứng 2 / bỏ 0 / sửa 0. JSON 2 mục, khóa string, jp/tw/old_vn khớp CSV3 2/2. Khối TOML parse bằng tomllib: 2 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hibikih6-orienteering-karimono-REVIEW.md`; danh sách sửa: `moan-hibikih6-orienteering-karimono-wrong.json`.

**Tổng cộng sau file này: 24 file / 528 dòng sai (moan)** (cơ sở 23 file / 526 dòng + 2 file này)
- Parent kiểm chứng 21/11 ~15:05: JSON 2 mục dạng chuẩn, khóa string; khối TOML 2 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 2/2 (1 bộ duy nhất, 667 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 2075 JP きゃふうううううん = ふ1u + う×5 = 6u — fix moan 6u đúng; LƯU Ý: giá trị fix của audit cho 2075 là 5u ở CẢ JSON lẫn khối TOML trong REVIEW.md của audit (không phải 6u như ghi chú parent lúc merge audit "sửa 7u→6u" — 7u chỉ có trong file tomlblock.txt cũ; giá trị 6u trong text review của audit không vào JSON/block) — fix moan 6u đè lên giá trị audit 5u ở đợt thống nhất; 2082 "a"→"Ya" (やっ mất phụ âm y, tiền lệ 2085 Yaa + Paulette h3); diff mỗi fix chỉ khác old_vn đúng chỗ mục tiêu; không dòng gasp Ư nào bị đụng (2075 Ư 0→0; 2082 "Ưm" đã có trong old_vn từ んっ); không dòng "Kh"; lượt soát 2: 2/2, 0 bỏ, 0 sửa.

---

# Moan snippet — ポーレットh2_制服変更？.txt.toml

- File: ポーレットh2_制服変更？.txt.toml (03_Paulette, 292 dòng, audit 47 sai đã merge).
- Đọc toàn bộ 292/292 dòng; 99 dòng rên/SFX theo mẫu quét.
- Đổi 33 dòng rên: 8 romaji họ fa/fu + ひゃ/きゃ (932, 942, 944, 956, 991, 992, 1003, 1008); 5 "Á"/từ cho やっ/やあ (927, 935, 946, 980, 1025); 7 trộn "Ưm + romaji" trong một âm (938, 1019, 1021, 1022, 1023, 1025, 1026); 9 đếm nguyên âm (923, 929, 932, 946, 957, 962, 963, 992, 1008); 4 mất phụ âm mora (928, 931, 937, 967); 4 khác (950, 972, 1006, 1660).
- Lỗi nặng nhất: rên ん + phụ âm bị tách "Ưm hyu"/"Ưm yu" (7 dòng, kể cả 1023 sai phụ âm ky→hy); họ fa/fu bị Việt hoá mất âm ("phù" cho ふあ, "phá" cho ふぁ); "Á" cho やっ/きゃっ mất phụ âm y/k.
- Gasp Ư của sweep/audit (952, 985, 1004, 1135, 950-cuối) không đụng; không dòng "Kh" khóa nào bị đổi (1003 "Khà"→"Kua": "Kh" đó là cách diễn sai của くあ).
- Cờ: 963 ĐÃ SỬA (parent): JP 10u (không phải 11u như agent đếm), VN cũ romaji 11u thừa 1u → fix romaji 10u "Afuuuuuuuuuun!!!", không áp fix audit; 5 dòng gasp Ư (952, 985, 1004, 1135, 950-cuối) đã có fix trong audit — áp ở đợt thống nhất, TOML-2 giữ VN cũ là đúng mô hình amendment; 960 nói ngọng để audit.
- Lượt soát 2: 33/33 tái kiểm chứng, 0 bỏ, 1 sửa (32 của agent + 1 parent bổ sung 963; 929 bổ sung んううっ→"Nuu" bị sót lượt 1).
- JSON 33 mục dạng chuẩn, khóa string, jp/tw/old_vn khớp CSV3 33/33; khối TOML 33 khóa parse đúng, 0 sai lệch. Parent SỬA 950: giá trị fix xây trên giá trị audit (giữ "anh Soutetsu" + "Ư!" cuối của audit, chỉ đổi "Hya un"→"Hyaun").

**Tổng cộng sau file này: 25 file / 561 dòng sai (moan)** (cơ sở 24 file / 528 dòng + 33 file này) [REBASE — cơ sở lúc giao là 23/526, Hibiki h6 (2 dòng) đã gộp 21/11 ~15:05]
- Parent kiểm chứng 21/11 ~15:35: JSON 33 mục dạng chuẩn, khóa string (32 của agent + 1 parent bổ sung 963); khối TOML 33 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 33/33 (1 bộ duy nhất, 292 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 923 10a, 957 5a, 962 8a, 980 4a, 1019 5u, 1021 11u, 1022 4u, 1023 6u, 929 2u+2a, 938 3u — đều đúng; 5 key trùng audit chỉ khác đúng token rên (923/932/956/957/991) — TRỪ 950 (xem dưới); 1003 "Khà"→"Kua": "Kh" đó là cách diễn sai của くあ, không phải Kh khóa cho っ; 1660 thống nhất theo 1645 (cùng JP （くちいっ）); lượt soát 2: 33/33, 0 bỏ, 1 sửa.
- SỬA (parent): 950 — giá trị fix của agent xây trên VN cũ, bỏ mất 2 sửa của audit ("anh Soutetsu" + "Ư!" cuối dòng, sweep gasp); đã sửa thành giá trị xây trên fix audit (chỉ đổi "Hya un"→"Hyaun"). THÊM 963 — agent tưởng VN cũ romaji 11u đã đúng số lượng, nhưng JP đếm máy chỉ có 10u (ふ1u + う×9); VN cũ thừa 1u; fix romaji 10u "Afuuuuuuuuuun!!!", không áp fix audit "À phùuuuuuuuuun!!!" (đủ 10u nhưng Việt hoá theo lý do tiền-romaji-rule).
- FLAG (đợt thống nhất): 963 — giữ romaji 10u (không áp fix audit); 960 nói ngọng để audit; 1001 くぅん sau tên giữ theo tiền lệ h1; 1639 "liếm" giữ. 5 dòng gasp Ư (952/985/1004/1135/950-cuối) đã có fix trong audit — áp ở đợt thống nhất; TOML-2 giữ VN cũ là đúng mô hình amendment, không thiếu gì.

---

# Moan-fix snippet — lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

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
- Parent kiểm chứng 21/11 ~15:45: JSON 15 mục dạng chuẩn, khóa string; khối TOML 15 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 15/15 (1 bộ duy nhất, 485 dòng); 5 key trùng audit chỉ khác đúng token rên (933/1358/1406/1423/1475), giữ nguyên phần gasp Ư của audit; đếm nguyên âm kiểm chứng độc lập: 1358 15u (ふぁ1u + ふゅ1u + ぅ×13), 1475 3u, 1406 2a — đều đúng; lượt soát 2: 15/15, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 quy ước ふっ ("Hư" file này vs "phù"/"fu" file khác); F2 độ dài SFX （） 2467 vs 2468; F3 2451 くっ→"Ư" trong （）; F4 1475 audit đếm sai (đã sửa bằng giá trị moan); F5 5 dòng chồng audit.

---

# Moan-fix snippet — ハチロクh2_お勉強の成果.txt.toml

- File: ハチロクh2_お勉強の成果.txt.toml (01_Hachiroku, 312 dòng, audit 46 sai đã merge).
- Đọc toàn bộ 312/312 dòng; 120 dòng rên/SFX theo mẫu quét.
- Đổi 27 dòng rên: 10 dòng họ fa/fu "phù a"→romaji (974, 976, 996, 1001, 1003, 1004, 1006, 1011, 1036, 1038 — ぷあ→"Pua", ふあ→"Fua", ふ，→"Fu, a"); 8 dòng họ ひゃ/ひゅ/ひあ/きゃ + やっ gộp mảnh/mất phụ âm (719 "Ua", 960/961 "Ya", 964 "Hyua", 965 "Hyafu", 966 "Hyan"+"Afu", 977 "Hiu", 995 "Ahi"); 5 dòng ん+X khôi phục âm mora (1036/1051 "Ưm fu", 1039 "ưm ku", 1054 "Ưm mư", 1120 "ưm ư"); 5 chuỗi dài về romaji + đếm đúng (1019 "Jururuuuuuuuuuu" 12u, 1020 "Junyururururururururu" る×8, 1030 "Kufuuuuuun" 7u, 1038 "Reroooo" 4o, 1206 "chuuuuu" 5u); 1 đếm nguyên âm (1056 "Ưm aa" 2a).
- Lỗi nặng nhất: "phù a" tách mảnh hệ thống (10 dòng); 1030 "Ư hưm!!!" sai hoàn toàn (mất く, chuỗi 7u thành 1u); 1019/1020 chuỗi mút dài 12–14 mora bị thu thành một "Chu mút".
- 3 giá trị audit thay thế ở đúng 1 token rên (964 "Hyu a"→"Hyua", 974 "Phù a"→"Fua", 976 "Phù a"→"Fua" giữ Ư cuối dòng); 6/8 fix moan của audit giữ nguyên (973 "Fuaaan", 1053 "Nhyu", 1055 "Nkyu", 1045 "liếm", 972/1148 "Ufufu").
- Gasp Ư của sweep/audit (14 dòng) không đụng; không dòng "Kh" khóa nào bị đổi.
- Cờ: 995 双鉄様っ！/双鉄さまぁっ！ (audit không thêm Ư như 990/1189 — để parent quyết); 1020 romaji nguyên dạng là phán đoán (có thể hoàn lại "Chu mút!!"); 976/1011 giữ "a a"/"A a" (tiền lệ kisaki-h3).
- Lượt soát 2: 27/27 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 27 mục dạng chuẩn, khóa string, jp/tw/old_vn khớp CSV3 27/27; khối TOML 27 khóa parse đúng, 0 sai lệch.
- Chi tiết đầy đủ: `moan-hachiroku-h2-obenkyou-no-seika-REVIEW.md`; danh sách sửa: `moan-hachiroku-h2-obenkyou-no-seika-wrong.json`.

**Tổng cộng sau file này: 27 file / 603 dòng sai (moan)** (cơ sở 26 file / 576 dòng + 27 file này) [REBASE — cơ sở lúc giao là 25/561, lr_日々姫ふかみh1 (15 dòng) đã gộp 21/11 ~15:45]
- Parent kiểm chứng 21/11 ~15:50: JSON 27 mục dạng chuẩn, khóa string; khối TOML 27 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 27/27 (1 bộ duy nhất, 312 dòng); 3 key trùng audit chỉ khác đúng token rên (964/974/976), giữ nguyên phần gasp Ư của audit; đếm nguyên âm kiểm chứng độc lập: 1019 12u, 1020 10u (る×8), 1030 7u, 1038 4o, 1206 5u — đều đúng; lượt soát 2: 27/27, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): 995 双鉄様っ！/双鉄さまぁっ！ — audit không thêm Ư như 990/1189, vòng moan không tự thêm gasp (để parent quyết); 1020 romaji nguyên dạng là phán đoán (có thể hoàn lại "Chu mút!!"); 976/1011 giữ "a a"/"A a" theo tiền lệ kisaki-h3.

---

# Moan-fix snippet — れいなh1_おかあさんのレッスン.txt.toml (moan-reinah1-okaasan-no-lesson)

- File: `れいなh1_おかあさんのレッスン.txt.toml` — 402 dòng script, TOML md5 `09eaed303cc160ad7b01033ad81f8c51` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 402 dòng, 0 key trùng.
- Đã đọc 402/402 dòng; xét 168 dòng rên/SFX (sửa 17, giữ 144, sweep 7 mục không đụng).
- Đổi 17 dòng: 14 romaji + 2 đếm nguyên âm + 1 sai âm.
- Romaji: 1233 `Fua`, 1264 `Hia` + `Fuaaaaaaaaaaaaan` (13 a), 1286 `Fuwaa`, 1290 `Fua`, 1322 `Kua!`, 1336 `Fuaaaaaa` (6 a), 1337 `Hia`, 1344 `Nhyu!` + `Fuaa`, 1354 `Fua` + `ưmmm`, 1527 `Hia`, 1528 `Fua`, 1530 `Fua`, 1537 `Fua`, 1552 `Fua`.
- Đếm nguyên âm: 1274 `Aa!` (ああっ), 1533 `Aa` (ああっ, giữ "Phùa" của audit).
- Sai âm: 1420 `Í!?` (いっ, bản cũ "Á" sai nguyên âm).
- Kiểu lỗi chính: họ ふあ(っ) bị tách mảnh/mất âm ("Phù a"/"Phù"/"Ha" — 11 dòng); họ ひあ/んひゅ diễn sai/mất âm theo quy tắc 3b (4 dòng: 1264, 1337, 1344, 1527).
- 9 dòng sửa xây trên VN sau audit (1233, 1264, 1336, 1337, 1344, 1527, 1530, 1533, 1537) — chỉ đổi phần rên, giữ nguyên phần còn lại của audit. Hai câu hỏi chờ của audit đã giải quyết trong file này: "Kua vs Hự" → "Kua" (1322, theo quy tắc romaji + tiền lệ 1272); mâu thuẫn ひあ/ひゃ → quy tắc 3b (1264/1337/1527 → "Hia", 1344 → "Nhyu").
- Giữ: dạng khóa fa/fu của audit ("Phà" 1284/1350/1529/1532/1535, "Phùa" 1533, "phuê" 1266/1278/1355/1526, "phuya" 1263/1525/1531); romaji đã đúng ("Hyawa"/"Hyan"/"Hya"/"Hyau"/"Pukya"/"Kua" 1272); "Ufufu" 1401/2134 (audit đã sửa); đếm 1374 đã đúng 14 u (audit đã sửa, kiểm chứng lại); gasp Ư sweep 5 + already-rendered 2 không đụng.
- Sweep: 7 mục đã kiểm chứng — 5 gasp Ư (1323, 1346, 1348, 1349, 1574) + 2 already-rendered (1373, 1375) đều không đụng.
- Cờ cho đợt thống nhất: 1534 がっ→"ưm" (âm tiết bị ngắt, chưa quyết); JP 1420 có `"` lạ (い"っ); 1282/1341 (cờ nói ngọng của audit còn nguyên); 1535 (phần nghĩa "đau quá" thuộc audit).
- Lượt soát 2: tổng 17 / tái kiểm chứng 17 / bỏ 0 / sửa 0. JSON 17 mục, khóa string, jp/tw/old_vn khớp CSV3 17/17. Khối TOML parse bằng tomllib: 17 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-reinah1-okaasan-no-lesson-REVIEW.md`; danh sách sửa: `moan-reinah1-okaasan-no-lesson-wrong.json`.

**Tổng cộng sau file này: 28 file / 620 dòng sai (moan)** (cơ sở 27 file / 603 dòng + 17 file này)
- Parent kiểm chứng 21/11 ~16:35: JSON 17 mục dạng chuẩn, khóa string; khối TOML 17 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 17/17 (1 bộ duy nhất, 402 dòng); TOML md5 khớp audit; 9 key trùng audit chỉ khác đúng token rên; đếm nguyên âm kiểm chứng độc lập: 1264 13 a, 1336 6 a, 1274 2 a, 1533 2 a, 1354 3 m — đều đúng; 1344 "Ưm" là âm ん (không phải gasp Ư — sweep không liệt kê key này), đổi sang "Nhyu" theo quy tắc 3b là đúng; sweep 7 mục không đụng; không dòng "Kh"; lượt soát 2: 17/17, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): 1534 (がっ→"ưm" — âm tiết bị ngắt, thuộc audit); 1420 (JP có `"` lạ); 1282/1341 (cờ nói ngọng của audit); 1535 (phần nghĩa thuộc audit).

---

# Moan-fix snippet — lr_凪h2_虎さんの交尾.txt.toml (moan-lr-nagih2-tora-san-no-koubi)

- File: `lr_凪h2_虎さんの交尾.txt.toml` — 293 dòng script, TOML md5 `4f26c5ed7e6e0d076848d8be1add75a7`, không có bản trùng.
- CSV3: bộ duy nhất `07_Nagi_Fukami`, 293 dòng, 0 key trùng.
- Đã đọc 293/293 dòng; xét 150 dòng rên/SFX (141 dòng có tiếng rên — 102 thoại + 39 độc thoại — + 9 dòng SFX hành động trong ngoặc).
- Đổi 26 dòng: 22 romaji (20 họ fa/fu + ひあ 1 + や-moan 1) + 3 đếm nguyên âm thuần + 1 sai âm (1205 mang cả romaji lẫn đếm).
- Romaji họ fa/fu: bản cũ dùng chung "Fua"/"fua" cho cả ふぁ lẫn ふあ — ふぁ phải là "Fa": 1174, 1188, 1190, 1205, 1210, 1229 (×2), 1235, 1236 (×2), 1237, 1241, 1243, 1250, 1254, 1258, 1273 ("Fuaaun"→"Faaun"), 1278 ("Fuaaaaaaa"→"Faaaaaaan", 7 a + n), 1280 (ふぇ "Hể"→"Fue"), 1304. ふあ→"Fua"/"fua" bản cũ đã đúng nên giữ (1199, 1247, 1203).
- Sai âm khác: 1183 ひあ "Hya"→"Hia"; 1245 か "Ha"→"Ka" (chuỗi ka—ha—a).
- Đếm nguyên âm: 1185 ひゅぁ… 6 a→10 a (giữ Ư audit); 1276 あ+11ー 11 a→12 a; 1205 7 hơi はぁ 1 a→2 a ("Haa" ×7); 1203 やぁっ/やあっ "Á"/"á"→"Áa"/"áa" (2 a mỗi tiếng).
- Rên や: 1325 やぁ trong chuỗi hơi thở → "yaa" (giữ phụ âm y-); 1181/1187/1203 や là từ chối nên giữ "Á" (chỉ sửa đếm) — xem cờ.
- Giữ ~124 dòng rên/SFX (romaji đúng "Hyau/Hya/Nhyu/Nhi/Nku/Pua/fuwa", cười "fufu/Ehehe/Nhehe", "gao", SFX ngoặc dạng động từ Việt, gasp Ư của audit).
- Sweep: 6 mục đã kiểm chứng qua audit (1220, 1221, 1222, 1247, 1268, 1296) + 2 gasp audit bắt thêm (1185, 1339) — không đụng gasp Ư nào ngoài việc giữ nguyên Ư của audit ở 1185/1247. Không dòng "Kh" nào bị đổi.
- Cờ cho đợt thống nhất: HỦY 17 fix fa/fu của audit (giữ romaji cũ — 1172, 1181, 1187, 1193, 1202, 1207, 1213, 1232, 1248, 1267, 1269, 1271, 1274, 1357, 1366, 1397, 1420; xem REVIEW §6); や chưa quyết chung (giữ "Á" cho từ chối vs "Yaa" cho rên — mâu thuẫn với lr-hibikifukami-h1 1334); 1164 "Kh," nói lắp (ngoài phạm vi moan); 1313 ふーーっ giữ "Phù" (borderline).
- Lượt soát 2: tổng 26 / tái kiểm chứng 26 / bỏ 0 / sửa 0. JSON 26 mục, khóa string, jp/tw/old_vn khớp CSV3 26/26. Khối TOML parse bằng tomllib: 26 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-nagih2-tora-san-no-koubi-REVIEW.md`; danh sách sửa: `moan-lr-nagih2-tora-san-no-koubi-wrong.json`.

**Tổng cộng sau file này: 29 file / 646 dòng sai (moan)** (cơ sở 28 file / 620 dòng + 26 file này) [REBASE — cơ sở lúc giao là 27/603, れいなh1 (17 dòng) đã gộp trước]
- FLAG (đợt thống nhất): HỦY 17 fix fa/fu của audit — giữ romaji cũ (1172, 1181, 1187, 1193, 1202, 1207, 1213, 1232, 1248, 1267, 1269, 1271, 1274, 1357, 1366, 1397, 1420; chi tiết ở REVIEW §6). や chưa quyết chung: file này giữ "Á" cho や là từ chối (1181/1187/1203) nhưng đổi "Yaa" cho やぁ là rên (1325) — chờ quyết một lần toàn dự án.
- Parent kiểm chứng 21/11 ~16:35: JSON 26 mục dạng chuẩn, khóa string; khối TOML 26 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 26/26 (1 bộ duy nhất, 293 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 1185 10 a, 1276 12 a (chữ A hoa cũng tính là 1 âm a — agent đúng, không sửa), 1278 7 a, 1205 "Haa" 2 a ×7, 1273 2 a, 1203 "Áa"/"Áaaa"/"áa" đúng; 1188 "Hyauuu" 3 u đúng; sweep 8 mục không đụng; không dòng "Kh" nào bị đổi; lượt soát 2: 26/26, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): 1164 "Kh," nói lắp (ngoài phạm vi moan); 1313 ふーーっ giữ "Phù" (borderline).

---

# Moan-fix snippet — 稀咲h1_性生活 (moan-kisaki-h1-seiseikatsu)

- File: `稀咲h1_性生活.txt.toml` — 335 dòng script, TOML md5 `ac459e00d403158a8ecd05162a0194d0`, không có bản trùng.
- CSV3: 1 bộ duy nhất (335/335 khớp, không khóa trùng).
- Đã đọc 335/335 dòng; xét 74 dòng rên/SFX (60 thoại rên/thở + 14 SFX độc thoại).
- Đổi 7 dòng: romaji 6 (1253 `I――Gi!`, 1255 `Ia`, 1260 `hia`, 1265 `Ua`, 1281 `Ua!!`, 1283 `hia`) + đếm nguyên âm 1 (1185 やぁっ `á`→`áa`).
- Kiểu lỗi chính: ひあっ bị diễn sai thành "hya" (1260, 1283); âm đơn bị tách mảnh ("Ư a"→"Ia", "ư a"/"U a"→"Ua"); mất âm いっ/ぎっ ("Á――á!"→"I――Gi!", 1253).
- Giữ 67 dòng rên/SFX (ひゃ/きゃ đã romaji đúng, fa/fu đã "fua"/"fu", cười "Fufu", quy ước あっ→"A", はぅっ→"Hau", んっ→"Ưm", SFX "Phập"/"Phụt" theo quy ước file).
- Sweep: 13 mục đã kiểm chứng — 12 fix audit đã áp đúng (1254 đếm lại = 9 u), 1 already-rendered (1012) giữ. Không sửa lại dòng gasp Ư nào; không có dòng "Kh" nào trong file.
- Cờ cho đợt thống nhất: F1 — 1253 "I――Gi!" có thể revert về "Á――á!" nếu Hieu thấy "Á!" tự nhiên hơn; F2 — 1244 しゅごっ→"tuyệt quá" (cờ từ audit, JP mơ hồ); F3 — や chưa quyết chung (1185 giữ "Á" cho từ chối, chỉ sửa đếm); F4 — SFX độc thoại （きゅっ）→"Siết chặt!" diễn nghĩa, chưa đếm nguyên âm.
- Lượt soát 2: tổng 7 / tái kiểm chứng 7 / bỏ 0 / sửa 0. JSON 7 mục, khóa string, jp/tw/old_vn khớp CSV3 7/7. Khối TOML parse bằng tomllib: 7 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-kisaki-h1-seiseikatsu-REVIEW.md`; danh sách sửa: `moan-kisaki-h1-seiseikatsu-wrong.json`.

**Tổng cộng sau file này: 30 file / 653 dòng sai (moan)** (cơ sở 29 file / 646 dòng + 7 file này)

- Parent kiểm chứng 21/11 ~16:55: JSON 7 mục dạng chuẩn, khóa string; khối TOML 7 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 7/7 (1 bộ duy nhất, 335 dòng); TOML md5 khớp agent; 0 key trùng audit (38 dòng); sweep 13 mục, 0 trùng key moan — không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi; đếm nguyên âm kiểm chứng độc lập: 1185 やぁっ = 2 a (tiền lệ lr-nagih2 1203); 1260/1283 ひあ→"hia" đúng quy tắc 3b; lượt soát 2: 7/7, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 1253 "I――Gi!" có thể revert về "Á――á!" nếu Hieu thấy "Á!" tự nhiên hơn; F2 1244 (しゅごっ→"tuyệt quá", cờ từ audit); F3 や chưa quyết chung (1185 giữ "Á" cho từ chối vs lr-nagih2 1325 "Yaa" cho rên); F4 SFX độc thoại （きゅっ）→"Siết chặt!" (2049, 2055) diễn nghĩa, chưa đếm nguyên âm.

---

# Moan-fix snippet — ポーレットh6_あなたとふたりの学園エッチ.txt.toml (moan-paulette-h6-gakuen-ecchi)

- File: `ポーレットh6_あなたとふたりの学園エッチ.txt.toml` — route 03_Paulette, 304 dòng script, audit trước đó 36 sai.
- TOML md5: `1a184880b82bce1ce58a67cbb3a5f923` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 304 dòng, 0 key trùng; VN khớp TOML 304/304 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 304/304 dòng; xét 193 dòng rên/SFX (44 dòng SFX trong ngoặc); sửa 35, giữ 158.
- Đổi 35 dòng: romaji 28 + đếm nguyên âm 5 + sai âm 2.
- Romaji họ fa/fu → Fa/Fua/Pa/Pua (12): 775 ふぁっ→"Fa", 777 ぷあっ→"Pua" + ふあっっ→"Fua", 788 ふぁ→"Fa", 807/815/833/850 ふあっ→"Fua", 838 ふぁ→"Fa" + ぷぁぁ→"Puaa", 853/859 ぷあっ→"Pua", 854 ふあっ→"Fua" + ぷあっ→"Pua", 944 ふぁんっ→"Fan". Không còn dòng fa/fu nào diễn "phù" mất âm a trong file (trừ fa tách giữ "phù, a" — xem cờ F4).
- Romaji mất phụ âm mora (15): 762 ひゃんっ→"Hyan", 764/766 や→"Ya", 767 あんっ→"An", 769 きゃふっ→"Kyafu", 770 ひゃふっ→"Hyafu", 772 くっ→"Ku", 796 きゃっ→"Kya", 801 くぅ→"Kuu", 805 やふっ→"Yafu" + んきゅんっ→"Nkyun", 806 くあっ→"Kua", 836 んきゅっ→"Nkyu", 868 んきゅっっ→"Nkyu", 1348 かはっ→"Kaha", 792 うぁっ→"Wa".
- Đếm nguyên âm (5): 778 んううっ→"ưm ư ư", 789 ぁあっ→"Aa" (+ gỡ dấu 」 thừa), 840/842/870 んうっ→"ưm ư"; gộp mảnh rời: 854 あああっ→"Aaa", 1561 ああ→"Aa"; 775/788 はぁ→"hàà"/"Hàà", 916 ふぅっ→"Phùu", 836 ふ(16 u)→"F"+16u (VN cũ 11 u).
- Sai âm (2): 916 しょっ→"Sho" ("hự" sai phụ âm), 1600 ぐっ→"hự" ("ưm" mất hẳn âm g).
- 4 fix audit bị HỦY (giữ VN cũ, KHÔNG đưa vào JSON): 768 ("Kíuuuuuuuuun" → giữ "Kyuuuuuuuuun"), 800/818 ("Ư a" → giữ "Kua"), 869 ("Ưm" → giữ "Nkyun!"). 5 fix xây trên giá trị audit (770, 815, 840, 850, 868 — chỉ đổi đúng token rên). 2 fix lật giá trị audit (806, 944). 27 dòng mới so với audit.
- Giữ 158 dòng rên/SFX: gasp Ư khóa (771, 774, 814, 816, 817, 819, 1271, 1290, 1377), hơi ngắn ふっ/ぷっ→"phù", fa tách "phù, a"/"phù——a" (786, 790), họ ちゅ→"chụt", nói ngọng (784, 835, 858), SFX độc thoại （ ） dạng nghĩa Việt, んくっ→"ưm" (859), 871 "Ưm ư ư".
- Sweep: 11 mục đã kiểm chứng — 10 fix gasp Ư không đụng, 1 already-rendered (833) chỉ đổi token fa. Không dòng "Kh" nào bị đổi (file không có token "Kh" độc lập).
- Lượt soát 2: tổng 35 / tái kiểm chứng 35 / bỏ 0 / sửa 0. JSON 35 mục, khóa string, jp/tw/old_vn khớp CSV3 35/35. Khối TOML parse bằng tomllib: 35 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h6-gakuen-ecchi-REVIEW.md`; danh sách sửa: `moan-paulette-h6-gakuen-ecchi-wrong.json`.

**Tổng cộng sau file này: 31 file / 688 dòng sai (moan)** (cơ sở 30 file / 653 dòng + 35 file này) [REBASE — snippet ghi cơ sở cũ 29/646 vì 稀咲h1 (7 dòng) đã gộp trước]
- FLAG (đợt thống nhất): F1 — HỦY 4 fix audit (768, 800, 818, 869 — giữ VN cũ, xem REVIEW §4); F2 — んきゅ "Nkyu" vs audit "Ưm"; F3 — くっ "Ku" (772) vs "Hự" (851) vs doc "Ư"; F4 — fa tách "phù, a" (786, 790) vs h9 "Fu, a"; F5 — họ ちゅう "chụt" vs h3 "chụụụt"; F6 — SFX độc thoại （ ） chưa áp công thức đếm (1541, 1543, 1552/1558/1560, 1597); F7 — んうっ→"ưm ư" (TW 1 âm 嗯 vs 2 âm 嗯啊); F8 — 916 "Sho", 1348 "Kaha" (phán đoán mới); F9 — 789 gỡ dấu 」 thừa; F10 — 793 "Uây!" giữ.

- Parent kiểm chứng 21/11 ~17:10: JSON 35 mục dạng chuẩn, khóa string; khối TOML 35 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 35/35 (1 bộ duy nhất, 304 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 778 んううっ = 3 âm ("ưm ư ư"), 836 ふ = 16 u (1+15), 870 んうっ = 2, 775/788 はぁ = 2 a, 789 ぁあっ = 2 a, 916 ふぅっ = 2 u; sweep 11 mục — chỉ 833 trùng key (already-rendered, chỉ đổi token fa, không đụng gasp Ư); không dòng "Kh" nào bị đổi; lượt soát 2: 35/35, 0 bỏ, 0 sửa. \n làm phẳng thành khoảng trắng ở 16 fix — KHỚP quy ước audit của chính file này (audit 18/18 fix đa dòng đều làm phẳng), không phải lỗi.
- 6 key trùng audit — áp giá trị moan: 770 giống hệt audit ("Hyafu!!?"); 769 audit "Kyaphù"→moan "Kyafu" (chỉ khác token fa; agent không liệt kê trong 2 nhóm, parent ghi thêm); 815 khác audit ở token fa + đếm んうっ; 840 chỉ khác đếm めうっ; 850 khác token fa + "Houhehu"→"Hôu-hê-hu" (đổi chính tả romaji, cờ cho đợt thống nhất); 868 "Ưm"→"Nkyu" (xem F2).
- 806/944 lật giá trị audit — đã kiểm chứng qua REVIEW audit (không có trong audit JSON): 806 audit chốt くあ→"Ư a" trong REVIEW, moan đổi lại "Kua" (khớp F1 800/818 giữ "Kua"); 944 audit chấp nhận bỏ đuôi ん ("phù"), moan khôi phục "Fan" (ふぁんっ giữ ん, tiền lệ 762 "Hyan" cùng file).
- FLAG (đợt thống nhất): F1 — HỦY 4 fix audit đã kiểm chứng là phá romaji đúng của VN cũ: 768 "Kyuuuuuuuuun"→audit "Kíuuuuuuuuun", 800 "Kua"→audit "Ư a", 818 "Kua"→audit "Ư a", 869 "Nkyun!"→audit "Ưm!" (giữ VN cũ, KHÔNG đưa vào JSON); F2 んきゅ "Nkyu" vs audit "Ưm" (836/868/869); F3 くっ "Ku" (772) vs "Hự" (851) vs doc "Ư"; F4 fa tách "phù, a" (786, 790) vs h9 "Fu, a"; F5 họ ちゅう "chụt" vs h3 "chụụụt"; F6 SFX độc thoại （ ） chưa áp công thức đếm; F7 んうっ→"ưm ư" (TW 1 âm 嗯 vs 2 âm 嗯啊); F8 916 "Sho", 1348 "Kaha" (phán đoán mới) + 1600 ぐっ→"hự" (vs tiền lệ h7 745 "Gu" romaji — SFX độc thoại dùng động từ Việt nên "hự" hợp quy ước file, chờ quyết chung); F9 789 gỡ dấu 」 thừa; F10 793 "Uây!" giữ.

---

# Moan-fix snippet — lr_れいな追加h_夜の花嫁修業.txt.toml (moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou)

- File: `lrれいな追加h_夜の花嫁修業.txt.toml` — route 04_Reina, 365 dòng script, audit trước đó 33 sai.
- TOML md5: `b6d6a52b2213d8bc98351a0f14d5ae91` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 365 dòng, 0 key trùng; VN khớp TOML 365/365 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 365/365 dòng; xét 161 dòng rên/SFX; sửa 47, giữ 114.
- Đổi 47 dòng: romaji 42 + mất âm 5.
- Romaji họ fa/fu → Fa/Fua/Pua/Fuya/Fuo/Fukyun (32 dòng): 724 ぷあ→Pua + ふ、あ→Fu, a; 736/1061/1067/1068/1069/1071/1073/1074/1081/1294/1474 ふぁ/ふあ→Fua; 1064 ふお→Fuo; 1065 ふや→Fuya + やぁ→Yaa; 1075 ふあ…ん (7 a) →FuaaaaaaanƯƯƯ; 1076 (4 a) →Fuaaaa; 1077 (6 a) →FuaaaaaanƯƯƯƯ; 1078 (9 a) →Fuaaaaaaaaa; 1080 ふや… (6 a) →Fuyaaaaaa; 1102/1162/1177/1188 ぷあ→Pua/Puaa; 1156 ふきゅん→Fukyun; 1170 ふひゅんんんん→Fuhyunnnn; dạng tách ふ、/ふ――→Fu (724, 1073, 1202, 1211, 1283).
- Romaji họ hya/hyu/hia (11 dòng): 1049 ひゅあ…→Hyuaaaa; 1051/1090/1104 ひゃう→Hyau; 1087 ひあ→Hia + ふあ→Fua ×2; 1092 ひゅあ→Hyua (+Ư audit); 1133 ひゅあ… (18 a) →Hyua…an; 1164/1172 んひゅん→Nhyun; 1168 んひゅ→Nhyu (VN cũ "hyun" thừa 1 n) + ふ、ぁ→Fu, a; 1166 んゆ→Nyu; 1178 �んゆう→Nyuu.
- Mất âm (5): 723 っふ→phù ("ưm" mất f); 1116 ふくっ→Fuku; 1118 うあっ→Ua; 1123 く、→Ku; 1221 んくっ→Ư hự (thống nhất trong file với 1169/1173/1120).
- Lật/xây trên audit (6 key): 1060 audit "ư aƯ"→"Kua" (tiền lệ h6 806); 723/1075/1077/1092/1133 giữ giá trị audit (gasp Ư / số nguyên âm) chỉ đổi token rên.
- Giữ 114 dòng rên/SFX: hơi ngắn ふっ/ぷっ→"phù", cười audit "Ufufu~"/"Nfufu~" (1056/1059/1185/1186/1251), 10 dòng sweep-gasp + fix gasp audit, đếm nguyên âm audit đã đúng (1063 8u, 1157 6u, 1189 18u, 1117 3a), くっ→"Hự"/"Ư hự", SFX （ ） dạng nghĩa Việt, ふわあっ→"Oa", nói ngọng (không phải rên).
- Sweep: 10 mục đã kiểm chứng — 0 trùng key moan. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 47 / tái kiểm chứng 47 / bỏ 0 / sửa 0. JSON 47 mục, khóa string, jp/tw/old_vn khớp CSV3 47/47. Khối TOML parse bằng tomllib: 47 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou-REVIEW.md`; danh sách sửa: `moan-lr-reinah-tsuika-h-yoru-no-hanayome-shugyou-wrong.json`.

**Tổng cộng sau file này: 32 file / 735 dòng sai (moan)** (cơ sở 31 file / 688 dòng + 47 file này)
- FLAG (đợt thống nhất): F1 — くっ/くあっ "Hự" vs "Ku"/"Kua" vs "Ư"; F2 — ふきゅん "Fukyun" vs "Hukyun" (h7 750); F3 — ひあ "Hia" vs "Hya" (共通13) vs "Hí a"; F4 — SFX （ ） chưa áp công thức đếm (1832/1833/1854/1861/1878/1881/1893/1894/1900/1925); F5 — 1048 やぁあ→"Đừng"; F6 — 1189 geminate ひっきゅ ("Hi kyu" vs "Hikkyu"); F7 — 1177 っ sau ~~~~ (audit đã quyết: đã diễn); F8 — 1064 "Fuo" + 1170 "Fuhyunnnn" lần đầu trong dự án; F9 — fa/fu audit đã cờ cho thống nhất, moan chuyển romaji theo quy tắc duyệt 21/11; F10 — 1060/1092 chồng audit.
- Parent kiểm chứng 21/11 ~17:45: JSON 47 mục dạng chuẩn, khóa string; khối TOML 47 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 47/47 (1 bộ duy nhất, 365 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 1075 7a, 1076 4a, 1077 6a, 1078 9a, 1133 18a, 1049 4a; sweep 10 mục, 0 trùng key moan; không dòng "Kh" nào bị đổi; 1060 lật audit "ư aƯ"→"Kua" (tiền lệ h6 806 đã kiểm chứng); 1092 giữ Ư của audit (っ đầu dòng); 1075/1077 ƯƯƯ/ƯƯƯƯ cho っ×3/×4 cuối rên (theo quy tắc gasp — っ mất hẳn nếu không diễn); \n literal giữ nguyên như audit (23 fix có \n, 0 làm phẳng); lượt soát 2: 47/47, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 くっ/くあっ "Hự" vs "Ku"/"Kua" vs "Ư"; F2 ふきゅん "Fukyun" vs "Hukyun" (h7 750); F3 ひあ "Hia" vs "Hya" vs "Hí a"; F4 SFX （ ） chưa áp công thức đếm; F5 1048 やぁあ→"Đừng"; F6 1189 geminate ひっきゅ; F7 1177 っ sau ~~~~ (audit đã quyết: đã diễn); F8 1064 "Fuo" + 1170 "Fuhyunnnn" lần đầu trong dự án; F9 fa/fu audit đã cờ cho thống nhất; F10 1060/1092 chồng audit.

---

# Moan-fix snippet — ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml (moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae)

- CSV3: 1 bộ duy nhất, 305 dòng, 0 key trùng; VN khớp TOML 305/305 sau chuẩn hoá `\n`/khoảng trắng.
- Đã đọc 305/305 dòng; xét 202 dòng rên/SFX (33 dòng SFX trong ngoặc); sửa 36, giữ 166.
- Đổi 36 dòng: romaji 27 + đếm nguyên âm 6 + romaji/đếm nguyên âm 3.
- Romaji họ fa/fu → Fa/Fua/Pua (15 dòng, 17 token): 848 ふあっ→"Fua", 854 ふあっ→"Fua", 855 ふあっ→"Fua", 864 ふぁ→"Fa", 873 ふあっ→"Fua", 883 ふあっ→"Fua", 884 ふぁ→"Fa", 886 ふあっ→"Fua" ×2, 888 ぷあっ→"Pua", 890 ふぁ→"Fa", 893 ぷあっ→"Pua", 895 ふあっ→"Fa", 906 ふあっ→"Fua" ×2, 920 ふぁ→"Fa", 958 ふあっ→"Fua". Không còn dòng fa/fu nào diễn "phù" mất âm a trong file (trừ fa tách "phù, a" — xem cờ F4 h6).
- Romaji mất phụ âm mora (16 dòng): 848/880/913 やっ→"Ya", 854 やっ→"Ya" + くっ→"Ku", 856 や→"Ya" + きゅっ→"Kyu", 860 きゃっ→"Kya", 862 やあっ→"Yaa" + ああっ→"Aa", 870/883/886/940 くっ→"Ku", 921 やぁ→"Yaa", 927 や→"Ya", 949 くぅんっ→"Kuun" (+ giữ "Nkyu"), 980 ひゅいっ→"Hyui" (sửa chính tả audit "Huyi"), 1733 くっ→"Ku".
- Đếm nguyên âm (6): 846/870 んんっ→"ưm ưm", 849 んううっ→"ưm ư ư", 891 ふぁ dài 22 a→17 a (9+8, っ giữa diễn "——"), 915 ふぅんっ→"Phùù ưm", 938 んーむっ→"Ưm ưm", 1015 んうぅっ→"ưm ư ư".
- Romaji khác (3): 892 きゅううう→"Kyuuuuuuuuu" (lật audit "Siết"), 924 えろぉっ→"Eroo", 942 ちゅむっ→"chumu" (tiền lệ h3).
- 2 fix audit bị HỦY (giữ VN cũ, KHÔNG đưa vào JSON): 932 ("Kua!"), 947 ("Nkyun!!!!"). 4 fix audit bị lật/kế thừa có chỉnh trong JSON: 892, 942, 949, 980.
- Giữ 166 dòng rên/SFX: gasp Ư khóa, fa tách "phù, a", họ ちゅ→"chụt", SFX độc thoại （ ） dạng động từ Việt, ひ/ひっ→"hí", くっ grunt→"hự" (1003), 1735 p-count 14 = 14 mora đã kiểm chứng.
- Sweep: 5 mục đã kiểm chứng — cả 5 đã được audit sửa đúng thành Ư, không đụng. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 36 / tái kiểm chứng 36 / bỏ 0 / sửa 1 (942 khôi phục token "liếm"). JSON 36 mục, khóa string, jp/tw/old_vn khớp CSV3 36/36. Khối TOML parse bằng tomllib: 36 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae-REVIEW.md`; danh sách sửa: `moan-paulette-h5-hadaka-epuron-no-remon-doresshingu-ae-wrong.json`.

**Tổng cộng sau file này: 33 file / 771 dòng sai (moan)** (cơ sở 32 file / 735 dòng + 36 file này) [parent REBASE 21/11 ~17:45 — snippet ghi cơ sở cũ 31/688 vì lrれいな追加h đã gộp trước]
- FLAG (đợt thống nhất): F1 — HỦY 2 fix audit (932, 947 — giữ VN cũ); F2 — くっ "Ku" (rên) vs "Hự" (grunt) vs doc "Ư" (như h6 F3); F3 — ひ/ひっ "hí" giữ (không thuộc họ ひゃ); F4 — họ ちゅ dài kéo bằng t/m (942/924/938/1723/1722/1702/1704); F5 — 868 ぐっ→"mất" (nghĩa chưa rõ); F6 — 878 ちゅっ→"hôn" giữ (1399 khung "hôn"); F7 — nói lắp 909/959/1047 (không phải rên, audit loop xem); F8 — 1048 tên gọi kéo dài くぅん bị mất độ dài, 1231 escape `\"` TOML vs `"` CSV3; F9 — 891 っ giữa rên dài diễn "——"; F10 — 915 ふぅんっ→"Phùù ưm" tách 2 mảnh vs gộp romaji.
- Parent kiểm chứng 21/11 ~17:45: JSON 36 mục dạng chuẩn, khóa string; khối TOML 36 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 36/36 (1 bộ duy nhất, 305 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 891 17a (9+8, っ giữa diễn "—"), 892 9u (1+8), 915 2u, 938 2 nhịp, 846/870 2 nhịp; sweep 5 mục — cả 5 audit đã sửa đúng thành Ư, không đụng; không dòng "Kh" nào bị đổi; 892 lật audit "Siết"→"Kyuuuuuuuuu" (9u theo công thức); 949 "Kuun" (くぅんっ = 2u); 942 khôi phục token "liếm" (lượt soát 2 sửa 1); 2 fix audit bị HỦY (932, 947 — giữ VN cũ, không đưa vào JSON); \n làm phẳng thành khoảng trắng ở 25 fix — KHỚP quy ước audit của chính file này (audit 14/14 fix đa dòng đều làm phẳng); lượt soát 2: 36/36, 0 bỏ, 1 sửa.
- FLAG (đợt thống nhất): F1 HỦY 2 fix audit (932, 947 — giữ VN cũ); F2 くっ "Ku" (rên) vs "Hự" (grunt) vs doc "Ư"; F3 ひ/ひっ "hí" giữ; F4 họ ちゅ dài kéo bằng t/m; F5 868 ぐっ→"mất" (nghĩa chưa rõ); F6 878 ちゅっ→"hôn" giữ; F7 nói lắp 909/959/1047 (không phải rên, audit loop xem); F8 1048 tên kéo dài + 1231 escape TOML; F9 891 っ giữa rên dài diễn "——"; F10 915 tách 2 mảnh vs gộp romaji.

---

# Moan-fix snippet — ハチロクh5_おだいどこしごと.txt.toml (moan-hachiroku-h5-odaidoko-shigoto)

- CSV3: 1 bộ duy nhất, 291 dòng, 0 key trùng; VN khớp TOML sau khi gộp `\n` thành khoảng trắng ở 148 dòng (hiện tượng TOML-2 đã biết).
- Đã đọc 291/291 dòng; xét 134 dòng rên/SFX (87 thoại + 47 SFX độc thoại （）); sửa 28, giữ 106.
- Đổi 28 dòng: romaji 25 + SFX 3.
- Romaji họ fa/fu → Fua/Fa/Pua/Fuya (12 dòng): 1006 ふあっ→"Fua", 1008 ふあっ→"Fua", 1010 ふあ+12あ→"Fuaaaaaaaaaaaa" (12a), 1011 ふあっ→"Fua", 1033 ふあっ→"fua", 1064 ふやっ→"Fuya" + ふあっ→"fua", 1065 ふやっっ→"Fuya", 1070 ぷああっ→"Puaa", 1073 ふあっ→"Fua", 1089 ふぁっ→"Fa", 1178 ふ、あっ→"Fu, a" ×2, 1222 ふあ+6あ+ん×3→"Fuaaaaaannn" (6a+3n).
- Romaji họ ひゃ/ひゅ/ひあ (6 dòng): 996 ひゃふう×8んっ→"Hyafuuuuuuuuun" (9u), 1000 んひゅっ→"Nhyu", 1012 ひあっ→"Hia", 1013 ひあっ→"Hia", 1073 んひゅっ→"Nhyu", 1077 んひゅううぅ×5っ→"Nhyuuuuuuuu" (8u).
- Rên dài một hơi gộp từ dạng tách mảnh (8 dòng): 996, 998 んふう×5っ→"Nfuuuuuu" (6u), 1010, 1067 んふうううっっ→"Nfuuuu" (4u), 1073 あ×8んっ→"Aaaaaaaan" (parent sửa: agent viết thừa 1 a), 1075 んあ×6っ→"Naaaaaa", 1077, 1222.
- Mất phụ âm mora (10 dòng): 759/992/998/1031/1010 や→"Ya"/"ya", 995 やあっ→"Yaa" + んふっ→"Nfu", 1020/1070 くっ→"Ku", 1074 んふうっ→"Nfuu", 1181 かはっ→"Kaha", 1227 かふっ→"Kafu".
- SFX phán đoán (3): 1012 あちゅっ→"Achu" (VN cũ "nóng quá" mất âm — audit bỏ sót), 1020 くっ→"Ku", 1181 かはっ→"Kaha".
- 16/28 key trùng fix audit — fix moan thay thế fix audit ở đúng token rên. 6 Ư sweep giữ nguyên (992/1031/1064/1065 giữ Ư, 1401/1416 không đổi); 8 Ư audit tự thêm: bỏ 6 (996, 1070, 1073, 1075, 1077, 1222 — っ cuối có !/? diễn cắt, tiền lệ h7) — parent GIỮ LẠI 2 (998 +Ư, 1067 +ƯƯ: っ cuối dòng tuyệt đối, không dấu câu, gasp mất hẳn nếu bỏ). Không dòng "Kh" nào bị đổi.
- Giữ 106 dòng rên/SFX: gasp Ư khóa, hơi thở ふ/ふっ đứng riêng "phù" (756), ひ/ひっ→"hí" (1015, 1074), あ ngắn, SFX ちゅ dạng Việt của file (753, 1223), SFX độc thoại （） 47 dòng, cười ufufu, nuốt.
- Sweep: 6 mục đã kiểm chứng — cả 6 đã được audit sửa đúng thành Ư, không đụng. Không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 28 / tái kiểm chứng 28 / bỏ 0 / sửa 0. JSON 28 mục, khóa string, jp/tw/old_vn khớp CSV3 28/28. Khối TOML parse bằng tomllib: 28 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-hachiroku-h5-odaidoko-shigoto-REVIEW.md`; danh sách sửa: `moan-hachiroku-h5-odaidoko-shigoto-wrong.json`.

**Tổng cộng sau file này: 34 file / 799 dòng sai (moan)** (cơ sở 33 file / 771 dòng + 28 file này)
- FLAG (đợt thống nhất): F1 — 1012 あちゅっ→"Achu" (phán đoán moan-pass, audit bỏ sót); F2 — くっ→"Ku" (1020, 1070) vs "Hự"/"Ư" (câu hỏi mở); F3 — かはっ→"Kaha" (1181), かふっ→"Kafu" (1227); F4 — họ ちゅ giữ dạng Việt (753, 1223) vs "chumu" (h3/paulette-h5 942); F5 — dạng tách fa 1047 giữ "phù——a" vs 1178 → "Fu, a"; F6 — 998 れふっ nói ngọng giữ nguyên; F7 — 1015 はひっ→"Hahí" giữ (chưa chuyển "Hahi").

- Parent kiểm chứng 21/11 ~18:05: JSON 28 mục dạng chuẩn, khóa string; khối TOML 28 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 28/28 (1 bộ duy nhất, 291 dòng); TOML md5 4f711f40ec474cb1d9de27daee7eda85 khớp audit (đường dẫn spawn ghi thiếu #U3053 — file thật đã xác minh bằng md5); sweep 6 mục — 992/1031/1064/1065 giữ Ư, 1401/1416 không đổi; không dòng "Kh" nào bị đổi; đếm nguyên âm kiểm chứng độc lập: 996 9u, 998 6u, 1010 12a, 1067 4u, 1073 8a, 1075 6a, 1077 8u, 1222 6a+3n; lượt soát 2: 28/28, 0 bỏ, 0 sửa.
- SỬA (parent): 1073 "Aaaaaaaaan" (9a) → "Aaaaaaaan" (8a — JP あ×8, agent đếm thừa 1). 998 "Nfuuuuuu" → "NfuuuuuuƯ" và 1067 "Nfuuuu" → "NfuuuuƯƯ" — KHÔI PHỤC Ư/ƯƯ của audit: 2 dòng này っ cuối dòng tuyệt đối, không dấu câu sau, gasp mất hẳn nếu bỏ (quy tắc gasp đã khóa); 6 dòng còn lại (996/1070/1073/1075/1077/1222) giữ quyết bỏ Ư của agent vì っ cuối có !/?/!!! diễn cắt (tiền lệ h7 836/837). Đã sửa wrong.json + REVIEW (§3, §5, §6b, khối TOML) + snippet.
- FLAG (đợt thống nhất): F1 1012 あちゅっ→"Achu" (phán đoán moan-pass); F2 くっ→"Ku" (1020/1070) vs "Hự"/"Ư"; F3 かはっ→"Kaha" (1181), かふっ→"Kafu" (1227); F4 họ ちゅ giữ dạng Việt (753/1223) vs "chumu"; F5 dạng tách fa 1047 giữ "phù——a" vs 1178 → "Fu, a"; F6 998 れふっ nói ngọng giữ; F7 1015 はひっ→"Hahí" giữ.

---

# Moan-fix snippet — ふかみh3_夏休みの最後の日の、前の日.txt.toml (moan-fukamih3-natsuyasumi-no-saigo-no-hi-no-mae-no-hi)

- CSV3: 2 set × 649 — chỉ dùng set tốt `11_Other`, VN khớp TOML 649/649 sau chuẩn hoá `\n`/khoảng trắng; set home-folder `07_Nagi_Fukami` là STALE (7/649). TOML md5 `468ff9287da913deb380278b68d048f8` (khớp audit), không có bản trùng.
- Đã đọc 649/649 dòng; xét 328 dòng ứng viên (lọc máy + quét bổ sung っ cuối dòng / họ fa-fu / họ ひゃ / họ や / chuỗi nguyên âm dài / 40 dòng （ ）); sửa 44, giữ 284.
- Đổi 44 dòng: romaji 31 + romaji/đếm nguyên âm 3 + đếm nguyên âm 5 + gasp 4 + romaji/gasp 1.
- Romaji họ fa/fu → Fa/Fua/Pua (21 dòng, 24 token): 2278 ふあっ→"Fua" (+ひゅあっ→"Hyua", んううう 3→4 nhịp), 2287 ふあっ→"Fua" (+ふきゅうううんんっ 6u/1n→5u/2n), 2301 ふぁ→"Fa", 2302 ぷあぁ→"Puaa" (2a), 2338 ふあっ→"Fua", 2345 ふぁ→"Fa", 2346 ふあっ→"Fua", 2351 ふあっ→"Fua" + ぷあっ→"Pua", 2352 ふあっ→"Fua" (+gasp Ư cuối dòng), 2358 ふぁ→"Fa" ×2, 2359 ふあっ→"Fua" + ふ、あ→"Fu, a", 2362 ふあっ→"Fua", 2371 ふ……ァ→"Fu……a", 2384 ふ、ぁ→"Fu, a", 2385 ぷあっ→"Pua", 2388 ふあっ→"Fua", 2394 ふあっ→"Fua", 2402 ふあっ→"Fua" (+はぁあああ 4a→5a), 2430 ふあっ→"Fua", 2577 ふあっ→"Fua", 2767 ふあっ→"Fua". 20/21 dòng này là fix fa/fu của audit ("phù"→"phà"/"phùa") nay chuyển sang romaji; 2359/2371 sửa luôn lỗi audit (gán "phà" cho ふ tách riêng).
- Romaji mất phụ âm mora (14 dòng): 2273/2280/2283 ひあっ "Hya"→"Hia", 2275/2276 きゃっ "Á"→"Kya", 2281/2292/2876 やっ "Á"/"không"→"Ya", 2293 ひうっ "Hya"→"Hiu", 2309 ふわっ "Oa"→"Fuwa", 2349 くっ "ư"→"Ku", 2409 あむっ "a ưm"→"Amu", 2422 きゃああっ "ááá"→"Kyaaa", 2784 やぁん "Ưm"→"Yaan".
- Đếm nguyên âm (5 dòng chỉ sửa số lượng): 2289 きゅふあ×14んんっ 15a/1n→14a/2n, 2379 はああああああ 8a→7a, 2427 はぅぅ 2→3 nguyên âm, 2428 んうぅっ 2→3 nhịp, 3911 （ああ――） 1a→2a.
- Gasp っ cuối dòng bị mất (4 dòng, cùng mẫu 2728; sweep + audit bỏ sót): 2202, 2596, 3208, 3435 → thêm "Ư".
- 21/44 dòng kế thừa/lật fix audit (20 fa/fu + 2292 kế thừa fix nghĩa "mưa to"→"to"); 23 dòng mới.
- Giữ 284 dòng ứng viên: gasp Ư của audit (1664, 1677, 2449, 2728), ひぁ→"Hya" (2335 — một mora, khác ひあ), romaji đã đúng (2286 "Kyau", 2295 "Hya", 2332 "Nkyuuu", 2397 "Nyun"), đếm đúng (2380 11a, 2335 7 nhịp, 2429 2 nhịp), ふ/ふっ→"phù", họ ちゅ→"chụt", chuỗi nuốt→"Ực/ực", tiếng cười (2478 "ufufu", 2605 "Hehe"), cảm thán Việt (2290 "Hả!?", 2314 "Oái!?", 2318 "Hảảả!?", 2426 "Hưm"), SFX （ ） dạng động từ Việt (40 dòng), っ gắn từ nội dung.
- Sweep: 14 mục đã kiểm chứng trực tiếp — nhận 1664/2728 (audit sửa đúng), 2281/3645 already-rendered đúng, 10 mục needs-file-audit đã xem lại (chỉ 2292 có việc moan). 0 trùng key moan với sweep ngoài các dòng trên. Không dòng "Kh" nào bị đổi (file không có dòng "Kh").
- Lượt soát 2: tổng 44 / tái kiểm chứng 44 / bỏ 0 / sửa 2 (3208, 3435 gỡ ngoặc 「」 thừa). JSON 44 mục, khóa string, jp/tw/old_vn khớp CSV3 44/44. Khối TOML parse bằng tomllib: 44 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-fukamih3-natsuyasumi-no-saigo-no-hi-no-mae-no-hi-REVIEW.md`; danh sách sửa: `moan-fukamih3-natsuyasumi-no-saigo-no-hi-no-mae-no-hi-wrong.json`.

**Tổng cộng sau file này: 35 file / 843 dòng sai (moan)** (cơ sở 34 file / 799 dòng + 44 file này — cơ sở đã cập nhật sau khi loop gộp ハチロクh5 21/11 ~18:05; lúc spawn cơ sở là 33/771)
- FLAG (đợt thống nhất): F1 — 2234/2546 や/やぁ chìm trong diễn nghĩa ("không chịu"/"chịu" là vị ngữ, không thay token được); F2 — 2431 んふっ→"ưm" (mất f?) chưa chắc; F3 — 2303 んぷっ→"Ưm" (mất p?) chưa chắc; F4 — SFX （ ） chưa áp công thức đếm (3885 "Rào"×10 vs 12a; 3892/3898/3900/3902/3921 chuỗi う dài diễn 1 động từ); F5 — phán đoán mới lần đầu: 2309 ふわっ→"Fuwa", 2293 ひうっ→"Hiu"; F6 — audit sửa sai 2359/2371 ("phà, a" cho ふ tách — moan đã sửa thành "Fu, a"/"Fu……a", dùng bản moan); F7 — 2292 kế thừa fix nghĩa audit (dùng giá trị JSON đã gồm cả hai); F8 — んんっ = "nn" hay "nnn" (bản này "nn" theo lr_ふかみh1/lr_れいな追加h; ふかみh1 967 "Hyaaann" viết 3n mâu thuẫn); F9 — 5 gasp audit + sweep bỏ sót (2202, 2352, 2596, 3208, 3435 — cùng mẫu 2728; khác quyết bỏ Ư ở ハチロクh5 996/1070/1073/1075/1077/1222 vì đó là っ cắt cuối rên dài đã diễn đủ âm, còn đây là っ gasp cuối câu nói/độc thoại); F10 — 2427 "A ư ư" (đếm) vs 2426 "Hưm" (từ cảm thán) — ranh giới diễn âm vs từ cảm thán.

- Parent kiểm chứng 21/11 ~18:20: JSON 44 mục dạng chuẩn, khóa string; khối TOML 44 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 bộ tốt 11_Other 44/44 (bộ home 07_Nagi_Fukami là STALE, chỉ 7/649); TOML md5 468ff9287da913deb380278b68d048f8 khớp audit; sweep 14 mục đã kiểm chứng trực tiếp (1664/2728 audit sửa đúng, 2281/3645 already-rendered, 10 needs-file-audit đã xem lại — chỉ 2292 có việc moan); không dòng "Kh" nào bị đổi; đếm nguyên âm kiểm chứng độc lập: 2287 5u/2n, 2289 14a/2n, 2379 7a, 2402 5a, 2427 3, 2428 3, 3911 2a, 2278 4 nhịp, 2422 3a, 2784 2a, 2302 2a; lượt soát 2: 44/44, 0 bỏ, 2 sửa.
- 5 gasp mới (2202/2352/2596/3208/3435) ĐÃ KIỂM CHỨNG: cùng mẫu 2728 trong chính file (audit đã sửa, parent-verified 20/11) — っ gasp cuối câu nói/độc thoại, mất hẳn → +Ư; khác quyết bỏ Ư ở ハチロクh5 (っ cắt cuối rên dài đã diễn đủ âm bằng romaji + !/?). 2352 audit đã sửa phần fa ("Phù"→"Phùa") nhưng bỏ sót gasp — moan thêm Ư là đúng (chỉ nói "audit bỏ sót" phần gasp, không phải cả dòng).
- 21 key trùng audit kiểm chứng: 2292 kế thừa đúng fix nghĩa audit ("mưa to"→"to", chỉ đổi Á→Ya); 2359/2371 agent ĐÚNG — audit gán sai "phà, a"/"phà…… a" cho ふ tách riêng (phải là "Fu, a"/"Fu……a"); 18 key fa/fu còn lại chỉ khác audit ở token rên. 2385 giữ Ư đầu dòng của audit.
- FLAG (đợt thống nhất): F1 (2234/2546 や chìm trong diễn nghĩa); F2 (2431 んふっ→"ưm" mất f?); F3 (2303 んぷっ→"Ưm" mất p?); F4 (SFX （ ） chưa áp công thức đếm); F5 (2309 ふわっ→"Fuwa", 2293 ひうっ→"Hiu" — phán đoán mới, parent kiểm chứng đúng âm Hepburn); F6 (audit sửa sai 2359/2371 — dùng bản moan); F7 (2292 dùng giá trị JSON đã gồm cả hai); F8 (んんっ "nn" vs "nnn" — bản này "nn", mâu thuẫn ふかみh1 967 "Hyaaann" 3n); F9 (5 gasp bỏ sót — đề nghị audit loop quét bổ sung "――っ/……っ cuối dòng" cho các file còn lại); F10 (2427 đếm vs 2426 "Hưm" cảm thán).

# Moan-fix snippet — lr_日々姫真闇h1_三人家族.txt.toml (moan-lr-hibiki-mayami-h1-sannin-kazoku)

- File: `lr_日々姫真闇h1_三人家族.txt.toml` — route 02_Hibiki, H-scene (Hibiki + Mayami, "gia đình ba người"), 436 dòng script, audit trước đó 60 sai.
- TOML md5: `d8f257e11854179d1a64585836ad9112`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 436 dòng, 0 key trùng; VN khớp TOML 435/436 (1 dòng còn lại chỉ khác TOML-2 làm phẳng `\n` thành khoảng trắng, key 1420).
- Đã đọc 436/436 dòng; xét 248 dòng rên/SFX/gasp (169 thoại rên + 79 SFX độc thoại trong ngoặc đơn).
- Đổi 3 dòng: 1550 ああああああっ "A a a a a a" → "Aaaaaa" (gộp 1 âm rên dài bị tách thành 6 mảnh); 1555 んウゥゥぅ "Nguuuuu" → "Nguuuu" (4 u theo JP + TW 4×唔; giữ Ư của audit); 1619 『あーーーーーーん』 'Aaaaaaaan' (8 a) → 'Aaaaaaan' (7 a; JP あ+6ー).
- Kiểm chứng độc lập 9 fix đếm nguyên âm của audit: 8 đúng (1440 19a, 1441 6a, 1446 20u, 1467 4a, 1477 19a, 1478 18a, 1479 14a, 1611 10o); chỉ 1619 sai (audit áp nhầm 8 a của 1579). Kiểm chứng 1579 đúng (8 a).
- Giữ 245 dòng rên/SFX (họ ひゃ/ひゅ/ひあ/きゃ đã romaji, không có "Á"; họ ふぁ/ふあ→"Fua"; ふ、ぁ tách theo JP 、 thì giữ "Fu, a" — tiền lệ parent-verified; cười "Nfufu"/"Ufufu"; SFX từ Việt theo quy ước file; っ nhấn mạnh cuối câu không thêm Ư).
- Sweep: 26 mục đã kiểm chứng trực tiếp — 24 audit đã áp đúng (fix audit = fix sweep 24/24), 2 already-rendered đúng (1432, 1723); không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào (file không có "Kh").
- Cờ cho đợt thống nhất: 2 (1555 — dùng "Nguuuu~Ư!!" thay fix audit 5 u; 1619 — dùng 'Aaaaaaan' 7 a thay fix audit 8 a).
- Lượt soát 2: tổng 3 / tái kiểm chứng 3 / bỏ 0 / sửa 0. JSON 3 mục, khóa string, jp/tw/old_vn khớp CSV3 3/3. Khối TOML parse bằng tomllib: 3 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hibiki-mayami-h1-sannin-kazoku-REVIEW.md`; danh sách sửa: `moan-lr-hibiki-mayami-h1-sannin-kazoku-wrong.json`.

**Tổng cộng sau file này: 36 file / 846 dòng sai (moan)** (cơ sở 35 file / 843 dòng + 3 file này)
- FLAG (đợt thống nhất): 1555 — dùng giá trị moan 「A! Fua! A!!! Nguuuu~Ư!!」 (4 u) thay fix audit 5 u (JP んウゥゥぅ = 4 u, TW 4×唔). 1619 — dùng giá trị moan 'Aaaaaaan' (7 a) thay fix audit 8 a (JP あ+6ー = 7; audit áp nhầm giá trị của 1579).

# Moan-fix snippet — れいなh3_おもらし自由化大作戦.txt.toml (moan-reinah3-omorashi-jiyuuka-daisakusen)

- CSV3: 1 set duy nhất, 279 dòng, 0 trùng khóa; VN khớp TOML 279/279. TOML md5 `6c1b1c26745216faeebd6d942cc2e2f4` (khớp audit), không có bản trùng.
- Đã đọc 279/279 dòng; xét 193 dòng ứng viên rên/SFX (181 lọc máy + 12 VN-only, 11 là dương tính giả do `ực` trong "thực/rần/rực"); sửa 32, giữ 161.
- Đổi 32 dòng: romaji họ fa/fu 17 (1014, 1019, 1031, 1047, 1048, 1053, 1068, 1073, 1078, 1083, 1119, 1121, 1195, 1196, 1197, 1198, 1200 — ふぁ→Fa, ふあ→Fua, ふや→Fuya, ふぇ→Fue, ぷあ→Pua) + romaji họ ひあ 3 (1014, 1016, 1055 — ひあ→Hia) + romaji sai âm 3 (1018 ふゅあ→Fyua, 1040 やぁん→Yaan, 1193 ふゆ→Fuyu) + romaji mất phụ âm mora 2 (1043, 1045 くっ→Ku) + đếm nguyên âm 7 (1025 4u→3u, 1085 7u→8u, 1092 4u→5u, 1099 7u→4u, 1102 1u→2u, 1116 1u→2u, 1192 3a→2a) + độ dài ん 1 (1061 んんっ→ưmm).
- 18/32 key trùng audit, chỉ khác fix audit ở đúng token rên; 14 key mới. 3 dòng hoàn lại đúng VN cũ (1048 "Fuya", 1119 "Fuei!", 1121 "Pua!" — audit đã Việt hoá romaji gốc).
- Giữ 161 dòng ứng viên: gasp Ư của audit/sweep (1050, 1074, 1080, 1099 — 1099 chỉ sửa số lượng u), họ ん→"ưm" theo quy ước file (1056, 1090, 1130 — audit đã chốt), ふっ→"phù" toàn file, họ ちゅ→"chụt", romaji đã đúng (1013/1195 "Hya", 1064 "hyu", 1071 "ya"), tiếng cười, SFX trong （ ） dạng động từ Việt, っ nhấn mạnh / đã diễn.
- Sweep: 4 mục đã kiểm chứng trực tiếp — nhận 3 fix audit (1074/1080/1099) + 1 already-rendered (1199); quét gasp lại toàn file: không còn gasp nào sót. Không dòng "Kh" nào bị đổi (file không có "Kh").
- Lượt soát 2: tổng 32 / tái kiểm chứng 32 / bỏ 0 / sửa 0. JSON 32 mục, khóa string, jp/tw/old_vn khớp CSV3 32/32. Khối TOML parse bằng tomllib: 32 khóa, 0 sai lệch giá trị. Đếm nguyên âm kiểm chứng độc lập: 1018 11a, 1055 10a, 1193 20u, 1085 8u, 1092 5u, 1099 4u, 1025 3u, 1102 2u, 1116 2u, 1192 2a, 1040 2a, 1019 3a.
- Chi tiết đầy đủ: `moan-reinah3-omorashi-jiyuuka-daisakusen-REVIEW.md`; danh sách sửa: `moan-reinah3-omorashi-jiyuuka-daisakusen-wrong.json`.

**Tổng cộng sau file này: 37 file / 878 dòng sai (moan)** (cơ sở 36 file / 846 dòng + 32 file này — cơ sở đã cập nhật: loop gộp lr_日々姫真闇h1 (+3) trong lúc làm file này; lúc spawn cơ sở là 35/843)
- FLAG (đợt thống nhất): F1 — 775 "Ư, m?" (む thành "m" — nói lắp hay mất âm); F2 — 1115 nói ngọng miệng đầy (audit đang chờ); F3 — 1133 ふえっ？ "hả?" hay "phuê?" (chờ Hieu); F4 — SFX （ ） chưa áp công thức đếm (1738/1740/1741/1747/1752/1753/1754/1721/1725); F5 — 1061 んんっ "ưmm" vs "nn" (mâu thuẫn ふかみh3 F8); F6 — 1091/1089 ちゅう… diễn bằng lặp t / bỏ u; F7 — 1094 っぐ→"gu" (っ đầu token); F8 — 1040 "Yaan~" (vị trí ~); F9 — 1192 "Waai!" (tiếng reo có thuộc phạm vi moan); F10 — 1025 bẫy codepoint ふぅぅ (không phải ふぉぅ); F11 — ふっ "phù" vs "Fu" (câu hỏi mở toàn dự án, reinah4 F2).

---

# Moan-fix snippet — れいなh2_おもらし防止大作戦.txt.toml (moan-reinah2-omorashi-boushi-daisakusen)

- CSV3: 1 set duy nhất, 284 dòng, 0 trùng khóa; VN khớp TOML 284/284 (sau chuẩn hoá `\n`). TOML md5 `141739546028af97fdbac1c3ffe9ab6e`, không có bản trùng.
- Đã đọc 284/284 dòng; xét 196 dòng ứng viên rên/SFX (193 lọc máy + 3 VN-only 1095/1098/1100); sửa 37, giữ 159.
- Đổi 37 dòng: romaji họ fa/fu 13 (1001, 1027, 1036, 1052, 1065, 1081, 1114, 1174, 1180, 1182, 1183, 1184, 1185 — ふぁ→Fa, ふあ→Fua, ふぇ→Fue, ぷあ→Pua, ぷは→Puha) + romaji họ ひゃ/ひゅ/ひあ 11 (1042, 1045, 1046, 1047, 1049, 1056, 1057, 1061, 1062, 1068, 1210 — ひゃう→Hyau, ひあ→Hia, んひゅ→Nhyu, ひゃふ→Hyafu, ひゃぷ→Hyapu, うひゅ→Uhyu, あひゅ→Ahyu) + romaji mất phụ âm mora 8 (1003 くっ→Ku, 1030 んくっ→Nku + くっ→Ku ×2, 1053 んきゅっ→Ưm kyu, 1064 きゅふうっ→Kyufuu, 1077 あ～～んっ→A~~n, 1087 ふっ→Phù + んくっ→Nku, 1088 んぷっ→Npu, 1090 んぶっ→Nbu) + đếm nguyên âm 5 (779 ふだ→phùu 2u, 1002 6a→4a, 1040 "Hyaaaaaa"→"Hyauuuuu" 1a+5u, 1089 17u→16u+n, 1216 4a→3a) + đếm kèm trong các dòng trên (1001 んんっ→ưmm, 1088 んんっ→ưmm, 1046 ふうっ→phùu, 1087 ふぅっ/ふーっ→phùu, 1114 はぁっ→Haa ×2, 1183 はぅぅ→hauu, 1185 はあっ→haa + ふぁぁっ→Faa).
- 14/37 key trùng audit, chỉ khác fix audit ở đúng token rên; 23 key mới. 9 key audit không đụng: gasp Ư 1031/1070/1071/1215, cười 1104/1108 (fix audit đã đúng), phi-moan 1118/1465/1628.
- Giữ 159 dòng ứng viên: gasp Ư của audit/sweep, んむっ→"A ưm"/"a ưm"/"ưm"/"Ưm" theo audit §4 (1043, 1093, 1094, 1114), ふっ→"phù" toàn file, họ ん→"ưm", chuỗi nuốt ごくっ→"Ực", chuỗi hôn/mút ちゅ→"chụt", SFX trong （ ） dạng động từ Việt (1730–1771), romaji đã đúng (1032 "Aaaaaa" 6a, 1064 "fuuuuu" 5u, 1052/1065/1180 "Hya"), tiếng cười, nói ngọng miệng đầy (1114, 1199), 786 しゅき→"thích".
- Sweep: 4 mục đã kiểm chứng trực tiếp — cả 4 là fix gasp Ư của audit, không đụng; quét gasp lại toàn file: không còn gasp nào sót (trừ 1026 やぁっ đã flag). Không dòng "Kh" nào bị đổi (file không có "Kh").
- Lượt soát 2: tổng 37 / tái kiểm chứng 37 / bỏ 0 / sửa 0. JSON 37 mục, khóa string, jp/tw/old_vn khớp CSV3 37/37. Khối TOML parse bằng tomllib: 37 khóa, 0 sai lệch giá trị. Đếm nguyên âm kiểm chứng độc lập: 779 2u, 1002 4a, 1040 1a+5u, 1089 16u+n, 1216 3a, 1114 2a ×2, 1183 2u, 1185 2a+2a.
- Chi tiết đầy đủ: `moan-reinah2-omorashi-boushi-daisakusen-REVIEW.md`; danh sách sửa: `moan-reinah2-omorashi-boushi-daisakusen-wrong.json`.

**Tổng cộng sau file này: 38 file / 915 dòng sai (moan)** (cơ sở 37 file / 878 dòng + 37 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
- FLAG (đợt thống nhất): F1 — 1026 やぁっ "không" hay "Yaa" (TW diễn thành rên; audit chấp nhận "không"); F2 — ふだ "phùu" hay "phù" (mâu thuẫn paulette-h6 vs paulette-h8); F3 — んくっ "Nku" hay "Ưm" (mâu thuẫn reinah3 vs nagih2 2501); F4 — SFX （ ） chưa áp công thức đếm (1730–1771); F5 — 1067 "hya" viết thường; F6 — các quyết giữ audit §4 bị ghi đè theo quy tắc 3b/công thức đếm (1042/1068/1210, 1002/1089/1077); F7 — んむっ giữ theo audit (1043/1093/1094/1114), không sửa thành "Nmu".
- Parent kiểm chứng 21/11 ~20:05: JSON 37 mục dạng chuẩn, khóa string; khối TOML 37 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 37/37 (1 bộ duy nhất, 284 dòng); TOML md5 141739546028af97fdbac1c3ffe9ab6e khớp audit; sweep 4 mục (1031/1070/1071/1215) không đụng; không dòng "Kh" nào bị đổi; đếm nguyên âm kiểm chứng độc lập: 1002 4a, 1040 1a+5u, 1089 16u+n, 1216 3a, 779 2u; lượt soát 2: 37/37, 0 bỏ, 0 sửa.
- SỬA (parent): key 1002 "Hyaaaaan" (5 a) → "Hyaaaan" (4 a — JP ひゃあああんっ = ひゃ + あ×3 = 4 a; agent ghi đúng "6a→4a" nhưng viết thừa 1 a). Đã sửa wrong.json + REVIEW (§3, khối TOML).

---

# Moan-fix snippet — ポーレットh7_残業エッチもyシャツで.txt.toml (moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de)

- File: `ポーレットh7_残業エッチもyシャツで.txt.toml` — route 03_Paulette, 326 dòng script, TOML md5 `6cd9aaebbdca88cdc9df37e560158f60` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 326 dòng; TOML vs CSV3 khớp 326/326.
- Đọc 326/326 dòng, xét 208 dòng rên/SFX, sửa 47 dòng (45 romaji + 2 cười), giữ 161 dòng.
- Romaji họ fa/fu (18 token): 780 Pu, 809 Fuya, 818 Fua, 834 Fua×2, 847 Pu, 850 Fua, 851 Fa, 853 Fua, 854 Fua, 858 Fua, 882 Fa, 885 Fua, 901 Fu, 912 Fa, 920 Fuwa, 921 Fuaa, 930 Fupu.
- Romaji họ ひゃ/ひゅ/ひあ/きゃ (15 token): 808 Hia, 810 Hyu+17a, 811 Hyau+8u, 812 Hyau+8u, 816 Hia, 818 Hia+Nyu, 820 Hia, 821 Kyafu+Kyau, 826 Hia, 830 Hyauu, 856 Yuh+14a, 899 Kyafu, 920 Nhyun.
- Romaji gộp ん+phụ âm (13 token): 808 Nmu, 821 Nku, 834 Nkyun, 839 Nku, 867 Ngu, 872 Anmu, 903 Nryu, 905 Nmu+Amu, 918 Nkyun, 921 Nkyu, 930 Nmu, 965 Aaanmu.
- Mất phụ âm mora (11 token): 786 Ya+Ra, 824 Au+Raa, 828 Ya+Yaaan, 843 Ya, 854 Yaa, 882 Ya, 889 Yan, 898 Au.
- Họ く → Ku (4): 838 Ku, 873 Ku, 882 Kku, 885 ku. ふぇ → Fue (1): 862. Cười → Ufufu (2): 936, 939.
- 10 key trùng fix audit (chỉ khác đúng token rên; giá trị moan thay thế giá trị audit): 816, 818, 821, 826, 834, 860, 899, 912, 918, 921. Không đụng fix Ư nào của sweep/audit; không dòng "Kh" nào bị đổi (file không có).
- Lượt soát 2: 47/47 re-verified, 0 bị loại, 3 được sửa (838, 882, 903 — dấu —— không cộng nguyên âm).
- Cờ cho đợt thống nhất: F1 họ く Ku vs Hự vs Ư; F2 ん+phụ âm romaji gộp vs "Ưm" (んぷっ 859/928 giữ "Ưm"); F3 んうっ/んふっ → "ưm" giữ; F4 899 かっ―― "C-" đủ chưa; F5 họ ちゅ/じゅ "chụt" vs h3 "chụụt/chumu"; F6 854 やぁぁ chìm trong diễn nghĩa; F7 ふっ "phù" vs "Fu"; F8 SFX （ ） dài 1696/1649/1650; F9 912 "hi——a——" giữ; F10 phán đoán mới 903 Nryu, 930 Fupu, 882 Kku.
- Chi tiết đầy đủ: `moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de-REVIEW.md`; danh sách sửa: `moan-paulette-h7-zangyou-ecchi-mo-y-shatsu-de-wrong.json`.

**Tổng cộng sau file này: 39 file / 962 dòng sai (moan)** (cơ sở 38 file / 915 dòng + 47 file này — parent REBASE 21/11 ~20:15: snippet ghi cơ sở cũ 37/878 vì れいなh2 đã gộp trước)
- Parent kiểm chứng 21/11 ~20:15: JSON 47 mục dạng chuẩn, khóa string; khối TOML 47 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 47/47 (1 bộ duy nhất, 326 dòng); TOML md5 6cd9aaeb khớp audit; 10 key trùng audit (816, 818, 821, 826, 834, 860, 899, 912, 918, 921) chỉ khác đúng token rên — 816 giữ nguyên Ư của audit (chỉ đổi Hya→Hia), 860 sửa đếm audit 18u→15u theo công thức, 918/921 khôi phục âm mora audit bỏ sót; sweep 10 mục — 816/899 là key audit đã sửa, 8 mục còn lại không đụng; không dòng "Kh" nào bị đổi (3 hit "Kh" chỉ là từ "Không" trong VN); đếm nguyên âm kiểm chứng độc lập: 810 17a, 811/812 1a+8u, 830 1a+2u, 856 14a, 860 15u, 828 Ya+Yaaan, 965 3a, 921 2a; lượt soát 2: 47/47, 0 bỏ, 3 sửa (838/882/903 — dấu —— không cộng nguyên âm). LƯU Ý: audit JSON file này dùng key INT (như F5 lr-h1) — kiểm chứng overlap phải đổi sang string. REBASE totals 37/878→38/915 (れいなh2 gộp trước).
- FLAG (đợt thống nhất): F1–F10 ghi lại trong snippet (F6 854 やぁぁ chìm trong diễn nghĩa — agent đã flag, không tự sửa).

---

# Moan-fix snippet — ふかみh2_homesweethome.txt.toml (moan-fukamih2-homesweethome)

- File: `ふかみh2_homesweethome.txt.toml` — route 07_Nagi_Fukami, 301 dòng script, TOML md5 `5dee3edcf2470621aa4f3b78c9c0a43b` (khớp md5 audit), không có bản trùng.
- CSV3: 2 bộ, bộ tốt là thư mục `11_Other` (flat-match 301/301; bộ `07_Nagi_Fukami` stale, chỉ khớp 12/301); TOML vs CSV3 khớp 301/301.
- Đọc 301/301 dòng, xét 112 dòng rên/SFX (67 thoại + 45 độc thoại/SFX), sửa 19 dòng (13 romaji + 4 âm sai/mất phụ âm + 2 đếm nguyên âm), giữ 93 dòng.
- Romaji họ fa/fu (6 dòng): 973 Fua, 981 Fua, 982 Pua, 1025 Fa/Fa/Fan, 1034 Fahi/Fan, 1043 Pua — thay thế ghi chú đợt thống nhất "→ phà/phùa" (quyết 21/11 ~01:55) bằng romaji theo fallback Hieu duyệt 21/11 ~01:56.
- Romaji họ ひゃ/ひゅ/ひあ (2 dòng): 975 Hia (cho ひあっ "Hi ah"), 988 hihyu (ひひゅっ bị dịch sai thành "ưm").
- Romaji khác (5 dòng): 983 Paa/Yaa, 990 Ku (く→"Ư" sai âm), 993 Kyun (khôi phục ん cuối), 999 Kyu/Fu (khôi phục きゅ/ふ bị mất), 1032 Puha (ぷはっ mất は).
- Âm sai/mất phụ âm (4 dòng): 1003 ưm mu (んむっ mất む), 1004 Ưm gu (ぐ→"mu" sai), 1013 ha (はっ mất h), 1022 Ha ư (はうっ mất h).
- Đếm nguyên âm (2 dòng): 1011 "A…… aa…… aa~—— aaa~~!" (1+2+2+3=8a), 1555 "Aan~" (あーん = 2a+n).
- Không đụng fix audit nào (0 key trùng audit — gasp Ư 995/996/1007/1024/1172/1442/1520/1566/1591/1735, đếm 1044/1767, SFX 1562, は 1776 giữ nguyên); không dòng "Kh" nào bị đổi (989/997/1017/1731/1739 giữ); không đụng thẻ %l đã bỏ (1050/1073/1096×2).
- Lượt soát 2: 19/19 re-verified, 0 bị loại, 0 được sửa.
- Cờ cho đợt thống nhất: F1 fa/fu 6 dòng đã sửa romaji (cập nhật mục thống nhất); F2 あっ "A"/"Ah"/"Á"/"a" không nhất quán; F3 んぐっ "Ưm gu" vs paulette-h7 "Ngu"; F4 んうっ "ưm" (1003) vs "ưm ư" (1033); F5 SFX （ ） chưa áp công thức đếm (1740, 1768, 1726, 1741); F6 970 って→"mất" (nghi bịa ý, cần kiểm tra nghĩa); F7 1026 "A!?" giữ; F8 1744 số lượng p.
- Chi tiết đầy đủ: `moan-fukamih2-homesweethome-REVIEW.md`; danh sách sửa: `moan-fukamih2-homesweethome-wrong.json`.

**Tổng cộng sau file này: 40 file / 981 dòng sai (moan)** (cơ sở 39 file / 962 dòng + 19 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
- Parent kiểm chứng 21/11 ~22:50: JSON 19 mục dạng chuẩn, khóa string; khối TOML 19 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 bộ tốt 11_Other 19/19 (bộ 07_Nagi_Fukami stale, 12/301); TOML md5 5dee3edcf2470621aa4f3b78c9c0a43b khớp audit; 0 key trùng audit; không dòng "Kh" nào bị đổi (989/997/1017/1731/1739); không đụng thẻ %l đã bỏ (1050/1073/1096×2); đếm nguyên âm kiểm chứng độc lập: 1011 8a, 1555 2a+n, 983 2a/2a, 1025 Fa/Fan, 1034 Fahi/Fan, 1043 Pua (ぷあ), 981 Fua, 982 Pua; lượt soát 2: 19/19, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 — 6 dòng fa/fu (973/981/982/1025/1034/1043) sửa romaji thay cho ghi chú thống nhất "→ phà/phùa" (quyết 21/11 ~01:55) — áp romaji theo fallback Hieu duyệt 01:56 (bản cũ "phù ah"/"Phù a" tách mảnh, ngượng); cập nhật mục thống nhất cho file này. F2–F8 ghi lại trong snippet.

---

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
- Parent kiểm chứng 21/11 ~23:05: JSON 44 mục dạng chuẩn, khóa string; khối TOML 44 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 44/44 (1 bộ duy nhất, 265 dòng); TOML md5 64abe8098966360371870067cd0d2843 khớp audit; đếm nguyên âm kiểm chứng độc lập: 881 11u, 911 11a+n, 1008 12a, 901/970 2a, 908 2a, 912 6u, 961 7u, 960 4i, 887 1a+2u; lượt soát 2: 44/44, 0 bỏ, 0 sửa.
- LƯU Ý: 882/884 fix == VN cũ — HỦY fix romanisation của audit (882 "KyaphùaƯ", 884 "Ưm!!"), giữ VN cũ theo quy tắc romaji (đã đối chiếu audit-paulette-h4-cream-and-cream-wrong.json); 42/44 dòng đổi giá trị so với VN cũ. 906/914/970 giữ phần không-phải-rên của audit, chỉ đổi token rên (đã đối chiếu audit JSON). 1010 thêm "Ư" cho っ đứng riêng (F5, cần xác nhận ở đợt thống nhất — っ sẽ mất hẳn nếu không diễn).
- FLAG (đợt thống nhất): F1–F10 ghi lại trong snippet (F5 1010; F6 897 きちゃう→"chạm vào" là lỗi nghĩa, agent đã flag không sửa; F8 882/884 hủy fix audit).

---

# Moan-fix snippet — lr_凪h1_痛いの痛いの飛んでけばい (moan-lr-nagih1-itaino-itaino-tondekebai)

- File: `lr_凪h1_痛いの痛いの飛んでけばい.txt.toml` — 304 dòng script, TOML md5 `3b4b468a7b4e2fc41327c15a75dd230c`, không có bản trùng.
- CSV3: 1 bộ duy nhất 304 dòng (thư mục home `07_Nagi_Fukami`); khớp TOML 304/304 sau chuẩn hoá `\n`.
- Đã đọc 304/304 dòng; xét 168 dòng rên/SFX (Nagi 83, Soutetsu 19, độc thoại 66 — trong đó 56 dòng SFX （）).
- Đổi 34 dòng: 17 romaji + 5 mất/sai âm + 12 đếm nguyên âm.
- Romaji họ fa/fu (13): 1145 `Phuan`→`Fan` (ふぁん), 1185 `phua`→`fa`, 1143 `Phua`→`Fua`, 1180 `Phua`→`Fua`, 1201 `Phua`→`Fa`, 1233 `phua`→`fua`, 1199 `Phua`→`Fua`, 1187 `Phua`→`Fa`, 1195 `Huê`→`Fue` (ふぇ), 1236 `phua`→`fua`, 1158 `Phua`→`Fua`, 1162 `phua`→`fa`, 1129 `Phuya`→`Fuya` (ふや).
- Gộp một âm bị tách mảnh (4): 1157 `Ưm hyun`→`Nhyun`, 1161 `Ưm hyun`→`Nhyunn`, 1242 `Khu hyun`→`Kuhyun`, 1234 `phu haa`→`Fahaa`.
- Mất/sai âm (5): 1190 ふあっ `a!`→`fua!` (mất f), 1216 ぺろっ `rero`×5→`pero`×5 (mất p), 1219 ぢゅぼっ `Chubo`→`Jubo` (mất hữu thanh), 1214 わっ `Oa`→`Wa` (mất w), 1169 ぁあっ `a á!`→`Aa!`.
- Đếm nguyên âm (12): 1163 はあっ×4 `ha`→`haa`, 1130 `Kya phuu…u` (17u)→`Kyafuuuuuuuuuu` (10u, gộp 1 token), 1131 `Nhyuaaaaaa` (6a)→`Nhyuaaaaaaaaaaa` (11a), 1223 `Zujuu…u` (20u)→19u + giữ Ư audit, 1217 `Zuryuuuuu` (6u)→`Zuryuuuuuu` (7u), 1221 `Juruuuuuu` (7u)→`Juruuuuu` (6u), 1222 `Reryuuuu` (4u)→`Reryuuuuu` (5u), 1213 `Juuuuuu` (6u)→`Juuuuu` (5u) + áp Ư audit, 1220 `Reruuuuu` (5u)→`Reruuuu` (4u), 1298 ふーっ `Phù`→`Phùu` ×2, 1379 ふーーーっ `Phùuu`→`Phùuuu` ×4, 1137 ふー `Phù`→`Phùu` ×2.
- Lỗi hệ thống chính: bản cũ dùng chung "phua"/"Phua" cho cả ふぁ lẫn ふあ (sai âm — ふぁ phải là "Fa") và tách nhiều âm rên đơn thành mảnh rời ("Ưm hyun", "Khu hyun", "phu haa").
- Giữ 134 dòng rên/SFX (ひゃうっ→"Hyau", んひゅっ→"Nhyu", はひゅっ→"Hahyu", くあっ→"Kua", くふっ→"Kufu", cười "Ufufu"/"Ehehe"/"Nihehe", ぷあっ→"Pua", ふあっ đã romaji đúng 1203/1204/1167/1173/1248/1134/1128, hơi thở ふっ→"Phu"/"phu", toàn bộ 19 dòng gasp Ư của audit).
- Sweep: 13 mục đã kiểm chứng — không còn mục nào chưa xử lý (9 áp nguyên trong audit + 2 already-rendered + 2 needs-file-audit). Chỉ gộp với audit ở 1213/1223 (giữ Ư, đổi token rên); không dòng "Kh" nào bị đổi.
- Lượt soát 2: tổng 34 / tái kiểm chứng 34 / bỏ 0 / sửa 0. JSON 34 mục, khóa string, jp/tw/old_vn khớp CSV3 34/34. Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-nagih1-itaino-itaino-tondekebai-REVIEW.md`; danh sách sửa: `moan-lr-nagih1-itaino-itaino-tondekebai-wrong.json`.

**Tổng cộng sau file này: 42 file / 1059 dòng sai (moan)** (cơ sở 41 file / 1025 dòng + 34 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
- FLAG (đợt thống nhất): F1 kiai 1224/1225 thiếu 1 o theo công thức (16 thay vì 17; 10 thay vì 11) — tiếng hô kiếm thuật, không phải rên, để nguyên chờ quyết; F2 1337 つっっっ→"quá" (audit đã flag chờ Hieu); F3 1366 lời ngọng chưa giải mã (audit đã flag chờ Hieu); F4 "Phu"/"phu" cho ふっ (1155, 1227) giữ không dấu — đợt thống nhất quyết có chuẩn hoá thành "phù" không.

---

# Moan-fix snippet — lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml (moan-lr-hiyoko-olivy-sex-no-obenkyou)

- File: `lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml` — route 11_Other, 441 dòng script, TOML md5 `bdb02933933db615a0380eb3839cd6de`, không có bản trùng.
- CSV3: 1 bộ duy nhất, 441 dòng, 0 trùng khóa; TOML vs CSV3 khớp 441/441 (chỉ khác `\\n` literal → khoảng trắng, mẫu đã biết).
- Đọc 441/441 dòng, xét ~160 dòng rên/SFX, sửa 55 dòng, giữ ~105 dòng.
- Đổi 55 dòng: 19 họ fa/fu → romaji (Fua/Fuaa/Fuaaa/Fuaaaaaa/Pua), 9 họ ひゃ/ひゅ/ひあ/きゃ/や → romaji (Hia/Hyai/Hyagu/Nhyu/Ya/Yaa), 9 họ ん+X gộp romaji (Nku/Nchu/Nkyu/Nkyun/Nuu/Nuuuu/Nfuuuuuu/Fuuuuun), 7 họ ちゅ/れる/じゅ/ごちゅ → romaji (Chumu/Chuu/Chubu/Reru/Rero/Jubu/Jururuu/Zuji/Buchu/Gochu/Pechu), 7 dòng くっ → "Ku", 2 dòng か…… → "Ka", 1 dòng いっ → "I", 4 dòng sửa đếm nguyên âm (1409 1→4a, 1424 3→2a, 1773 phù 1→2u + Ahhh 3→2a, 2343 tách mảnh + 3a).
- Kiểu lỗi chính: bản cũ tách MỘT âm rên thành nhiều mảnh ("phù ah", "Ư hiu", "Ưm ư ư ư ư", "chụt ưm"), mất phụ âm mora (くっ→"ư", やっ→"Ư", いっ→"Ư", か→"Kh"), sai đếm nguyên âm ("Ahhh" cho 2a, "Cứuu…" cho 13u).
- Trùng fix audit 2 khóa (2331, 2426): 2331 "Pua" ghi đè "phù ah" của audit (audit sửa "phụt"→"phù ah"); 2426 giữ "Ư" + đếm 13u của audit, chỉ đổi いっ "Ư"→"I". Không hủy toàn bộ fix audit nào. 0 key trùng sweep gasp đã sửa (1301/1554/1591/1925/2099/2166 do audit sửa, không đụng); không dòng "Kh" cho っ nào bị đổi.
- Sweep: 6 mục — 1301/1554/1591/1925/2099/2166 đã sửa (không đụng); 2146 っっ――→"ư——" giữ nguyên (gasp đã diễn bằng Ư).
- Giữ ~105 dòng rên/SFX (kiểu ふむ→"Hừm", んっ→"Ưm", あっ/はっ→"Ah/Ha", ふっ→"Phù", cười ふふっ→"Fufu", SFX ngoặc diễn thành động từ VN "Tách ra/Nắn bóp/Phập/Nhóp nhép/Trượt vào/Ngoạm/Ực"; ふえっ→"Hể!?" giữ; 1369 giữ diễn nghĩa).
- Cờ cho đợt thống nhất: F1 んうっ "Ưm" (ngắn) vs romaji "Nu/Nuu" (dài); F2 ふっ "phù" vs "Fu"; F3 SFX miệng/lưỡi trong thoại → romaji vs động từ VN (ranh giới với SFX ngoặc); F4 べろおおおおっっ → "Berooooo" vs "liếm liếm liếm liếm"; F5 ひっ、ぐっ → "Hi, gu" vs "Hức, hức"; F6 1655 ひよこぉ/もっとぉ mất độ dài ぉ (không sửa); F7 1369 giữ diễn nghĩa SFX hành động trong câu; F8 trùng audit 2331/2426 (xem trên); F9 あっ "Ah" vs "A"/"Á"; F10 2146 っっ――→"ư——" giữ (sweep không bao phủ).
- Lượt soát 2: tổng 55 / tái kiểm chứng 54 / bỏ 0 / sửa 1 (2437: "Fukyuuuuuuu" 8u → "Fukyuuuuuuuu" 9u). JSON 55 mục, khóa string, jp/tw/old_vn khớp CSV3 55/55. Khối TOML parse bằng tomllib: 55 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hiyoko-olivy-sex-no-obenkyou-REVIEW.md`; danh sách sửa: `moan-lr-hiyoko-olivy-sex-no-obenkyou-wrong.json`.

**Tổng cộng sau file này: 43 file / 1114 dòng sai (moan)** (cơ sở 42 file / 1059 dòng + 55 file này — REBASE: cơ sở lúc spawn là 41/1025, nhưng lr_凪h1 (34 dòng) đã gộp trước trong cùng lượt, nên tổng hiện tại của ROUTE-MOANS.md là 42/1059)

---

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

---

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

---

# Moan-fix snippet — 日々姫h1_マッサージの続き.txt.toml (moan-hibikih1-massage-no-tsuzuki)

- File: `日々姫h1_マッサージの続き.txt.toml` — route 02_Hibiki, 329 dòng script, TOML md5 `c8169ed72a3a329d6f677624531c75cf` (khớp md5 audit), không có bản trùng.
- CSV3: 1 bộ duy nhất, 329/329 key khớp TOML, 0 sai lệch VN.
- Đã đọc 329/329 dòng; xét 147 dòng rên/SFX thực sự (106 thoại + 41 SFX độc thoại).
- Đổi 16 dòng: họ hya → romaji 3 (1002 きゃ→Kya, 1007 きゃ→Kya, 1019 ひゃ→Hya); やっ→Ya 5 (996, 1001, 1004, 1009, 1059); んふ→Nfu/Nfuu 4 (1004, 1019, 1065, 1084); mất phụ âm mora khác 6 — 970 あうっ→Au (kế thừa fix nghĩa audit), 1003 ふやっ→Fuya + んくう…→Nkuuuuuuuuu (9 u, đếm bằng máy), 1022 ふえっ→Fue, 1039 ぷはっ→Puha, 1041 くっ→Hự (quy ước file ×3), 1044 かはっ→Kaha; rên dài đếm lại 2 (1003, 1019: Nfuu 2u / Nuuu 3u / Kufuun 3u).
- Giữ: họ hya đã romaji đúng (998 Hyau, 999 Hyaun, 1014 Nhyu, 1022 Hia), 1050 Fuaaaaaaaaaaan đếm đúng 11 a, 39 dòng SFX độc thoại đã diễn đúng, gasp Ư của audit (10 dòng) đầy đủ, fa/fu "Phù" 4 dòng (1013, 1017, 1018, 1059) để đợt unification, dòng nói ngọng 1015 giữ nguyên (không phải dòng rên).
- Cờ: F1 くっ "Hự" vs "Ku" (câu hỏi mở toàn dự án); F2 fa/fu "Phù" → unification; F3 1015 nói ngọng; F4 phán đoán ふえっ→Fue ở 1022; F5 giữ "Ưm—————" ở 1040; F6 key 970 kế thừa fix audit (dùng giá trị JSON này, không áp riêng bản audit).
- Lượt soát 2: tổng 16 / tái kiểm chứng 16 / bỏ 0 / sửa 0. JSON 16 mục, khóa string, jp/tw/old_vn khớp CSV3 16/16. Khối TOML parse bằng tomllib: 16 khóa, 0 sai lệch giá trị. Kiểm tra diff phát hiện 16 giá trị fix nháp thiếu ngoặc 「」 — đã bổ sung trước khi chốt.
- Chi tiết đầy đủ: `moan-hibikih1-massage-no-tsuzuki-REVIEW.md`; danh sách sửa: `moan-hibikih1-massage-no-tsuzuki-wrong.json`.

**Tổng cộng sau file này: 46 file / 1230 dòng sai (moan)** (cơ sở 45 file / 1214 dòng + 16 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của ROUTE-MOANS.md)
- Parent kiểm chứng 22/11 ~01:20: JSON 16 mục dạng chuẩn, khóa string; khối TOML 16 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 16/16 (1 bộ duy nhất, 329 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 1003 9u (く+う×8), 1019 Nfuu 2u / Nuuu 3u / Kufuun 3u — đếm trực tiếp theo mora (ん không mang nguyên âm, nên công thức tắt "1+う" không áp cho token bắt đầu bằng ん: んうううっ = 3u, agent đúng); sweep 6 mục (1011/1230/1231/1232/1237/1670) không trùng key moan nào; không dòng "Kh" nào bị đổi; lượt soát 2: 16/16, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 くっ "Hự" vs "Ku" (câu hỏi mở toàn dự án — file này áp "Hự" theo quy ước nội bộ, 1043/1044/1062 đều dùng "Hự"/"hự" cho くっ; tiền lệ ngược ふかみh3 dùng "Ku"); F2 fa/fu "Phù" 4 dòng (1013/1017/1018/1059) → unification; F3 1015 nói ngọng (không phải rên, để audit); F4 1022 ふえっ→"Fue" (phán đoán: nằm đầu chuỗi rên, khác tiền lệ giữ "Hả"/"Hể" cho thán từ độc lập); F5 1040 giữ "Ưm—————"; F6 key 970 dùng giá trị moan (đã gồm fix nghĩa audit "Vào trong tử cung"), KHÔNG áp riêng bản audit.

---

# Moan-fix snippet — lr_ハチロクh1_今ひとたびの契り.txt.toml (moan-lr-hachiroku-h1-ima-hitotabi-no-chigiri)

- File: `lr_ハチロクh1_今ひとたびの契り.txt.toml` — route 01_Hachiroku, 358 dòng script, audit trước đó 64 sai.
- Đã đọc 358/358 dòng; xét 180 dòng rên/SFX (thoại 123 + SFX （） độc thoại 57; thêm 41 dòng văn xuôi có từ tượng thanh đã kiểm tra, giữ nguyên).
- Đổi 9 dòng (đếm nguyên âm 3, romaji 6), giữ 171 dòng rên/SFX.
- Đếm nguyên âm 3: 1163 はぁっ "ha"→"haa", 1170 はぁ ×3 "Ha"→"Haa", 1245 はあっ "Ha!"→"Haa!" (mỗi âm 2 a, VN cũ thiếu 1).
- Romaji 6: 1149 んうっ "ưm"→"ưm ư" (thiếu nguyên âm う); 1213/1234/1241/1252/2008 ちゅむっ "chum"/"Chum"→"chumu"/"Chumu" (thiếu nguyên âm của む; tiền lệ h1_契り 2147).
- 1234 THAY THẾ fix audit cùng key (khác fix audit chỉ ở "chum"→"chumu"; giữ nguyên "——Ư" của audit).
- Đồng ý 34/34 dòng moan của audit (đếm lại theo mora: 1142 14u, 1263 12u, 1264 4n+4u, 1947 9u, 1998 10u, 1999 12u, 2000 13u — đều đúng).
- Giữ hệ SFX （） diễn theo nghĩa hành động (tiền lệ h8/h1_契り); trả lời cờ audit ở 1965: giữ "Xâm nhậpppp..." (しにゅう → "xâm nhập" nhất quán trong file, chuỗi p kéo dài là phong cách nghệ thuật).
- Sweep: 18 mục đã kiểm chứng trực tiếp (17 fix audit áp đúng + 1314 needs-file-audit); không dòng "Kh" nào bị đổi; không dòng gasp Ư nào bị xem lại.
- Cờ: F1 1314 "rồi——Ư!" chờ Hieu (audit đã cờ); F2 1234 thay thế fix audit; F3 1982 "chụt" cho ちゅむうっ (hệ diễn-nghĩa) vs tiền lệ 2147 "Chumu"; F4 そうてつさま không nhất quán (audit đã cờ).
- Lượt soát 2: 9/9 tái kiểm chứng, 0 bỏ, 0 sửa (đã loại 1 lỗi đếm nháp ở 1992: JP đủ 10 u, VN đúng 10 u, không sửa).
- Chi tiết đầy đủ: `moan-lr-hachiroku-h1-ima-hitotabi-no-chigiri-REVIEW.md`; danh sách sửa: `moan-lr-hachiroku-h1-ima-hitotabi-no-chigiri-wrong.json`.
- **Tổng cộng sau file này: 47 file / 1239 dòng sai (moan)** (cơ sở 46 file / 1230 dòng + 9 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng của ROUTE-MOANS.md)

- Parent kiểm chứng 22/11 ~02:30: JSON 9 mục dạng chuẩn, khóa string; khối TOML 9 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 9/9 (1 bộ duy nhất, 358 dòng, 0 key trùng); TOML md5 khớp audit, 1 bản duy nhất; đếm nguyên âm kiểm chứng độc lập: 1163/1170/1245 = 2 a (1+1う), 1213/1234/1241/1252/2008 ちゅむっ → "chumu" (chu+mu, khôi phục nguyên âm u của む), 1149 んうっ → "ưm ư" (ん+う); 1992 kiểm chứng lại: JP じゅ+ぶ+りゅ+7う = 10 u, VN 10 u đúng — agent giữ đúng, không sửa; chỉ 1 key trùng audit (1234) — fix moan chỉ khác audit ở "chum"→"chumu", giữ nguyên "——Ư" của audit; không dòng gasp Ư nào bị xem lại; không dòng "Kh" nào bị đổi (1163 "Kh-không" là lắp thoại, không đụng); lượt soát 2: 9/9, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 1314 "rồi——Ư!" chờ Hieu (audit đã cờ); F2 1234 thay thế fix audit; F3 1982 "chụt" cho ちゅむうっ (hệ diễn-nghĩa) vs tiền lệ "Chumu" (h1_契り 2147); F4 そうてつさま không nhất quán (audit đã cờ).

# Moan-fix snippet — 日々姫h5_白濁絵の具の射精会.txt.toml (moan-hibikih5-hakudaku-enogu)

- File: `日々姫h5_白濁絵の具の射精会.txt.toml` — route 02_Hibiki, 343 dòng script, audit trước đó 39 sai.
- Đã đọc 343/343 dòng; xét 153 dòng rên/SFX (thoại 105 + monologue 48, gồm 44 dòng SFX （）).
- Đổi 3 dòng (nguyên âm 1, moan 2), giữ 150 dòng rên/SFX.
- Nguyên âm 1: 1153 ひゅっ！あああああああああんっ "Hyu! Aaaaaaaaaaaan" (12 a) → "Hyu! Aaaaaaaaan" (9 a) — áp lại fix audit đã bị parent loại, với giá trị ĐÚNG 9 a (JP 9 a + 1 n, đếm bằng máy).
- Moan 2: 1215 はっ "A!" → "Hà!" (mất phụ âm h — ngoại lệ duy nhất của quy ước はっ→"Hà" trong file); 1255 ふ、ぅ "phù" → "phù, u" (âm ぅ bị mất hẳn; tiền lệ 1190 ふ、ぁ→"phù, a"; TW hai tiếng 呼).
- Đồng ý toàn bộ 37 fix moan/gasp/nguyên âm còn hiệu lực của audit; phán lại và đồng ý cả hai phán đoán của audit: 1264 "Nukyu" (ん-う-きゅ đủ 3 mora) và 1154 "Po" (ぽッ là âm tiết おちんぽ bị cắt; "ưm" cũ là âm mũi không có trong JP).
- Đếm nguyên âm kiểm tra lại bằng máy cho mọi chuỗi moan dài: 1151 8a/2n, 1156 10a, 1157 1a/1u/1n, 1152 1a/1u/2n, 1212 12u/6n, 1213 9u, 1228 18o, 1261 3u, 1265 6u, 1269 3u, 1226 5u — tất cả khớp.
- Không dòng gasp Ư nào bị xem lại; không dòng "Kh" nào bị đổi; không có dòng ふぇ/ふや hay dòng cười nào trong file.
- Cờ: F1 1189 không phải dòng moan — MEMORY 22/11 ~02:47 đã quyết bỏ "đã bao phủ", áp ở đợt thống nhất; F2 1215 "Hà!" là fix mới — parent xem lại ở lúc gộp nếu thấy "A!" là diễn có chủ ý.
- Lượt soát 2: 3/3 tái kiểm chứng, 0 bỏ, 0 sửa (kiểm tra cơ học bắt 1 lỗi mã hoá `\n` trong bản nháp JSON — đã dựng lại từ CSV3, khớp tuyệt đối).
- Chi tiết đầy đủ: `moan-hibikih5-hakudaku-enogu-REVIEW.md`; danh sách sửa: `moan-hibikih5-hakudaku-enogu-wrong.json`.
- **Tổng cộng sau file này: 48 file / 1242 dòng sai (moan)** (cơ sở 47 file / 1239 dòng + 3 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng của ROUTE-MOANS.md)
- Parent kiểm chứng 22/11 ~03:00: JSON 3 mục dạng chuẩn, khóa string; khối TOML 3 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 3/3 (1 bộ duy nhất, 343 dòng); TOML md5 khớp audit; 1153 đếm lại bằng máy: JP 9 a + 1 n, fix 9 a đúng (áp lại fix audit đã loại với giá trị đúng); 1215 "Hà!" GIỮ — quy ước file はっ→"Hà" (8 dòng khác), "A!" cũ mất phụ âm h (sound-loss), TW 啊 không mâu thuẫn (TW vẫn diễn はっ thành 啊); 1255 "phù, u" theo tiền lệ 1190 (ふ、ぁ→"phù, a"); không dòng gasp Ư nào bị xem lại; không dòng "Kh" nào bị đổi; lượt soát 2: 3/3, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 1189 đã quyết 22/11 ~02:47 (bỏ "đã bao phủ", áp ở đợt thống nhất — không thuộc moan). F2 (1215) đã quyết lúc gộp: giữ "Hà!".

# Moan-fix snippet — 凪ふかみh2_みずあそび.txt.toml (moan-nagifukamih2-mizuasobi)

- File: `凪ふかみh2_みずあそび.txt.toml` — route 07_Nagi_Fukami, 350 dòng script, audit trước đó 42 sai.
- TOML md5: `dc5ff6dcb84a35650fb89a8465df9fe0` (khớp md5 audit), không có bản trùng. Lưu ý: disk path trong brief trỏ nhầm sang 凪h2_おとなの水着 (md5 `a581ef85...`); file đúng đã dùng là `#U51ea#U3075#U304b#U307fh2_#U307f#U305a#U3042#U305d#U3073.txt.toml`, md5 đã kiểm chứng.
- CSV3: 1 bộ duy nhất, 350 dòng, 0 key trùng; JP trong comment TOML khớp CSV3 350/350 (kể cả 2 dòng CSV3 bị mojibake 1319/1386 đã kiểm chứng qua TOML).
- Đã đọc 350/350 dòng; xét 135 dòng rên/SFX (86 thoại + 43 SFX độc thoại ngoặc + 3 độc thoại gasp + 2 độc thoại thở + 1 độc thoại （おおお）).
- Đổi 5 dòng: 2 romaji (1300 ふ、あ→"Fu, a"; 1326 やっ→"Ya") + 2 đếm nguyên âm (1294 はぁ×3→"Hàà" + ああ～→"aa~", giữ Ư của audit; 1302 はぁぁぁぁ 5 a→"Hààààà") + 1 sai âm (1397 くおっ→"Kuo!").
- Giữ 130 dòng rên/SFX: 34 fix romaji của audit đều đã đúng (1274 14u, 1277 9u kiểm chứng lại bằng máy); 5 gasp Ư sweep + 5 already-rendered không đụng; hơi thở ふっ/ふうっ→"phù" theo quy ước file; SFX miệng "liếm"/"chụt"; gằn Soutetsu "Hự"; cười "Ư hứ hứ"/"Ni hê hê~"; nói ngọng 1421/1455.
- Sweep: 10 mục đã kiểm chứng trực tiếp (5 fix Ư + 5 already-rendered) — không đụng dòng gasp Ư nào; không dòng "Kh" nào bị đổi (file không có dòng "Kh"; "Kh..." ở 1412 là từ "khủng" bị lắp).
- 1294 thay thế giá trị audit cùng key (giữ Ư của audit, thêm đếm nguyên âm) — áp MỘT giá trị moan mỗi key ở đợt thống nhất.
- Flag: F1 1276 "Fukyu" vs "Phù kiu" (chờ Hieu, giữ "Fukyu" theo tiền lệ 3 file); F2 1299 baby-talk giữ "ưm"; F3 dạng tách fa "Fu, a" vs h7 giữ "phù——a" (cần quyết thống nhất); F4 1350 び bị rơi (TW cũng rơi, cần vòng audit); F5 quy ước độ dài SFX độc thoại （ ） (2132/2141/2149/2150/2154/2155/2160/2174/2182/2165); F6 1294 thay giá trị audit vừa gộp; F7 brief ghi sai disk path.
- Lượt soát 2: tổng 5 / tái kiểm chứng 5 / bỏ 0 / sửa 0 (bắt 1 lỗi trước soát 2: 1300/1326 dùng newline thật thay vì `\n` literal — đã sửa). JSON 5 mục, khóa string, jp/tw/old_vn khớp CSV3 5/5. Khối TOML parse bằng tomllib: 5 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-nagifukamih2-mizuasobi-REVIEW.md`; danh sách sửa: `moan-nagifukamih2-mizuasobi-wrong.json`.

**Tổng cộng sau file này: 49 file / 1247 dòng sai (moan)** (cơ sở 48 file / 1242 dòng + 5 file này — parent REBASE 22/11 ~03:00: snippet ghi cơ sở cũ 47/1239 vì 日々姫h5 đã gộp trước)
- Parent kiểm chứng 22/11 ~03:00: JSON 5 mục dạng chuẩn, khóa string; khối TOML 5 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 5/5 (1 bộ duy nhất, 350 dòng); TOML md5 khớp audit; đếm nguyên âm kiểm chứng độc lập: 1294 9 a (2+2+2+1+2) ✓, 1302 5 a ✓; 1294 giữ Ư của audit, chỉ khác audit ở đếm nguyên âm — áp MỘT giá trị moan; 1300 "Fu, a" theo tiền lệ h9/lr-h1; 1326 "Ya" theo tiền lệ Paulette h3 (やっ→"Ya"); 1397 "Kuo!" (くおっ — "Ư!" cũ mất hẳn phụ âm k); không dòng gasp Ư nào bị đụng (1294 giữ Ư audit); file không có dòng "Kh"; lượt soát 2: 5/5, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 1276 "Fukyu" vs "Phù kiu" (chờ Hieu); F2 1299 baby-talk giữ "ưm"; F3 dạng tách fa "Fu, a" vs h7 giữ "phù——a" (cần quyết một dạng toàn dự án); F4 1350 び rơi (cần vòng audit); F5 quy ước độ dài SFX độc thoại （ ）; F6 1294 thay giá trị audit vừa gộp (áp giá trị moan).
- SỬA (parent): disk path trong queue.json của file này đã SAI (trỏ sang 凪h2_おとなの水着, md5 a581ef85 — file đã moan-merged từ trước); agent đã tự dùng đúng file 凪ふかみh2 (md5 dc5ff6dc, parent kiểm chứng lại bằng md5sum). Queue entry đã xóa khi gộp nên lỗi này không còn nguy cơ tái diễn; parent đã ghi vào log ngày.

---

# Moan-fix snippet — lr_日々姫h1_鏡の中日々姫.txt.toml (moan-lr-hibikih1-kagami-no-naka-hibiki)

- File: `lr_日々姫h1_鏡の中日々姫.txt.toml` — route 02_Hibiki, 325 dòng script, audit trước đó 41 sai (19 gasp Ư + 18 rên + 4 nghĩa).
- TOML md5: `8e7924c231fed9512780b5e53fce841e` (khớp md5 audit), không có bản trùng. TOML khớp CSV3 tuyệt đối modulo flatten `\n` (158 khớp đúng + 167 flatten, 0 sai lệch khác).
- CSV3: 1 bộ duy nhất, 325 dòng, 0 key trùng.
- Đã đọc 325/325 dòng; xét 127 dòng rên/SFX (60 thoại + 59 SFX độc thoại （ ） + 8 độc thoại khác).
- Đổi 0 dòng: audit đã sửa đúng và đủ cả 18 lỗi rên — kiểm lại bằng máy: 1064 9a/1n, 1115 13a/3n, 1145 13u, 7 dòng ふあっ→"Fua", 1041→"Kyan", 1139→"Nfu", 1142→"Nkun", 6 dòng はぁ/はあ→"Haa" — và 19 lỗi gasp Ư; phần còn lại đã đúng (Hya/Hia/Nhyun/Nkyun, "Fuuuuuuu" 7u, cười "Ehehe"/"Nfufu", SFX diễn bằng lời theo phong cách file).
- Giữ 127 dòng rên/SFX: không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi (file không có dòng "Kh"); 4 dòng nghĩa của audit (1117, 1321, 1377, 1455) không bị sửa, không có dòng rên nào chồng lên.
- Sweep: 14 fix + 3 already-rendered đã kiểm trực tiếp — đều đúng; 5 mục sweep bỏ sót audit đã sửa; 1096 JP chỉ là dấu câu (TW thêm 唔), giữ nguyên là đúng.
- Flag: F1 độ dài kéo dài SFX （ ） diễn bằng lời cảm tính, không nhất quán (1773 vs 1795 đều "lạiiii"; 1797 14i; 1810/1818 đều 10a); F2 `ふっ` "Fu" (file này) vs "phù" vs "Hư" liên file; F3 dạng tách "Fu, a" (1047/1160, đồng ý với moan-fix nagifukamih2) vs "phù——a" (h7).
- Lượt soát 2: tổng 0 / tái kiểm chứng 0 / bỏ 0 / sửa 0 (soát lại toàn bộ kết luận 0 đổi: 18 fix rên + 19 gasp của audit và quét máy lại toàn file). JSON 0 mục, khóa string. Khối TOML parse bằng tomllib: 0 khóa, 0 sai lệch giá trị.
- Chi tiết đầy đủ: `moan-lr-hibikih1-kagami-no-naka-hibiki-REVIEW.md`; danh sách sửa: `moan-lr-hibikih1-kagami-no-naka-hibiki-wrong.json` (danh sách rỗng — file đã sạch về rên).

**Tổng cộng sau file này: 50 file / 1247 dòng sai (moan)** (cơ sở 49 file / 1247 dòng + 0 file này) [parent REBASE 22/11 ~04:40 — snippet ghi 49/1247 (agent quên cộng chính file này); file đã moan-fix nên tổng file tăng lên 50, tổng dòng giữ 1247]
- Parent kiểm chứng 22/11 ~04:40: JSON 0 mục (danh sách rỗng), khối TOML 0 khóa parse OK; TOML md5 8e7924c2 khớp audit; CSV3 1 bộ duy nhất 325 dòng, 0 key trùng; 18 key moan của audit kiểm chứng độc lập — đếm nguyên âm bằng máy: 1064 9a/1n ✓, 1115 13a/3n ✓, 1145 13u ✓; quét máy độc lập toàn file (Á cho họ ひゃ, Fa/fa cho ふあ, Ha/ha 1a cho はぁ/はあ) — mọi hit đều đã có fix trong audit, không còn lỗi rên nào sót; sweep 17 mục kiểm chứng (14 fix + 3 already-rendered, khớp danh sách agent); không dòng gasp Ư nào bị đụng; không dòng "Kh" nào bị đổi; lượt soát 2: 0/0/0/0. LƯU Ý NHỎ: số "28 dòng đã có fix" ở REVIEW §1 không khớp phép tính (18+19−2−1=34) — lỗi số học trong văn xuôi, không ảnh hưởng kết luận 0 đổi; không lặp lại số này ở snippet đã gộp.
- FLAG (đợt thống nhất): F1 (độ dài kéo dài SFX （ ） cảm tính); F2 (ふっ "Fu" vs "phù" vs "Hư" liên file); F3 (dạng tách "Fu, a" vs "phù——a").

---

# Moan-fix snippet — lr_ニイロクh_誓い。約束.txt.toml (moan-lr-niirokuh-chikai-yakusoku)

- File: `08_Niiroku/lr_ニイロクh_誓い。約束.txt.toml` — Niiroku + Akai, H-scene thề ước/mở niêm phong; không có Soutetsu.
- Đọc 320/320 dòng, xét 126 dòng rên/SFX, đổi 38 dòng (34 romaji + 4 đếm nguyên âm), giữ 88 dòng.
- Họ fa/fu → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ ふかみh1/h2/h3, ハチロクh5/h6/h9): ふあっ→Fua, ふぁっ→Fa, ぷあっ→Pua, ぷぁっ→Pua; dạng tách ふ、ぁ/ふっ、あ/ふっ──ぁ→"Fu, a"/"Fu──a" (6 dòng).
- Đếm nguyên âm: はぁっ/はあっ = 2 a (1271, 1275, 1292, 1468, 1516); はああっ = 3 a (1267, audit bỏ sót).
- Audit bỏ sót 7 dòng: 1275, 1339, 1342, 1392, 1468, 1516, 1569.
- 31/38 dòng xây trên giá trị audit cùng key (chỉ đổi đúng token rên, giữ Ư gasp và các phần khác); áp MỘT giá trị moan cho mỗi key.
- Sweep gasp kiểm tra trực tiếp 7/7 mục — không đụng dòng Ư nào; không có dòng "Kh" nào trong file; 0 っ thô trong VN.
- Cờ đợt thống nhất: đại từ Niiroku "em"×15 → "Tôi" (quyết định 22/11 ~03:32, chờ xác nhận); dạng tách fa "Fu, a" vs ハチロクh7 giữ "phù, a"; はぁっ/はあっ 1a hay 2a (audit ghi 1468 "đúng số lượng"); ん、くっ "ưm, ku" vs "ưm, hự"; ふ、ゅっ "Fu, yu" (1356).
- Lượt soát 2: 38/38 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `baf71db80b8ef4a9e7bfd57bf6313b21` khớp audit; khối TOML 38 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 51 file / 1285 dòng sai (moan)** (cơ sở 50 file / 1247 dòng + 38 file này — REBASE: cơ sở lúc spawn là 49/1247, nhưng lr_日々姫h1 (0 dòng) đã gộp lúc 22/11 ~04:40 trong khi làm file này, nên tổng hiện tại của ROUTE-MOANS.md là 50/1247)
- Parent kiểm chứng 22/11 ~04:55: JSON 38 mục dạng chuẩn, khóa string; khối TOML 38 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 38/38 (1 bộ duy nhất, 320 dòng); TOML md5 khớp audit; 31 key trùng audit — diff từng key chỉ khác đúng token rên (Phù/phù/phà→Fa/Fua/fua/Pua/pua + đếm nguyên âm 1267/1271/1275/1292/1468/1516 + "hự"→"ku" 1395); 7 key mới (1275, 1339, 1342, 1392, 1468, 1516, 1569) đều moan-only; đếm nguyên âm kiểm chứng độc lập: 1277 12a ✓, 1292 5a ✓ (Hàà 2a + Fuaaaaa 5a), 1438 3a+n ✓, 1267 3a ✓, 1278 4a/4a ✓, 1280 2a ✓, 1336 3u+2n ✓; sweep 7 mục không đụng (1272/1292/1381 giữ nguyên phần Ư của audit, chỉ đổi token fa); không dòng "Kh" nào bị đổi; lượt soát 2: 38/38, 0 bỏ, 0 sửa.
- SỬA (parent): key 1278 "Hà aaa!" → "Hà aaan!" — khôi phục ん cuối token 1 (JP はあああんっ = 4 a + ん; audit và agent đều chỉ đếm nguyên âm nên bỏ sót ん; tiền lệ giữ ん: 1336 "Kyuuunn", hibikih1 1115 "…annn"). Đã sửa wrong.json + REVIEW (§4A, khối TOML); khối TOML kiểm parse lại: 38 khóa, 0 sai lệch.
- GHI CHÚ: REVIEW §4A 1377 viết "(ぷ + ぁ = 2 âm a)" — sai số học (ぷぁ chỉ có 1 nguyên âm a; giá trị fix "Pua" vẫn đúng, không sửa).
- FLAG (đợt thống nhất): F1 (đại từ Niiroku "em"×15 → "Tôi", chờ xác nhận); F2 (dạng tách fa "Fu, a" vs h7 giữ "phù, a"); F3 (はぁっ/はあっ 1a hay 2a — parent CHỐT 2a lúc gộp theo tiền lệ h9/lr-h1/lr-hibikifukami-h1 + TW 呼啊 2 âm tiết, và audit file này tự đếm はあああん = 4a ở 1278; lr-ふかみh1/h2 giữ "Ha" vẫn chờ quyết chung); F4 (ん、くっ "ưm, ku" vs "ưm, hự" — parent giữ "ku" theo tiền lệ ハチロクh6 §3c); F5 (1356 ふ、ゅっ "Fu, yu" vs audit "Phù, ư"); F6 (31 dòng thay thế giá trị audit).

---

# Moan-fix snippet — lr_稀咲h1_おしおきとごほうび.txt.toml (moan-lr-kisakih1-oshioki-to-gohoubi)

- File: `06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml` — Kisaki trừng phạt Soutetsu (say rượu kể bí mật vợ chồng cho Paulette); H-scene Kisaki chủ động, Soutetsu bị trói tay.
- Đọc 297/297 dòng, xét 163 dòng rên/SFX, đổi 6 dòng (romaji 2 + đếm nguyên âm 4), giữ 157 dòng.
- Romaji: 991 ふえっ→"Fue", やあっ→"Yaa"; 992 ふえっ→"Fue", うぁっ→"Ư á" (theo mẫu nội file 1021/1034).
- Đếm nguyên âm: 1023 あーーーん 5a→4a ("Aaaan"); 1173/1263 そうてつぅ "Soutetsuuu"→"Soutetsuu" (3u); 1708 SFX 15u→16u (sửa lỗi chép của audit — audit ghi đúng "16 u" nhưng chuỗi fix chỉ có 15u).
- File vốn đã sạch về rên (audit dùng romaji nhất quán): họ fa/fu 9 dòng đều "Fua", họ hya 1 dòng "Kya", không còn "Á" cho họ hya, không còn "phà"/"phùa"; đếm nguyên âm đã kiểm bằng máy đúng ở 1703–1707/1709/1720/1729/1686–1694/1041–1069.
- Sweep gasp kiểm tra trực tiếp 17/17 mục — đều đã có trong audit; không đụng dòng gasp Ư nào; file không có dòng "Kh".
- Cờ đợt thống nhất: F1 ふえっ→"Fue" (991/992, theo tiền lệ 日々姫h1 1022 — chờ parent quyết); F2 くっ "kư" vs "ku"; F3 SFX ぎゅ… dài "Véo――iiii…" trộn 2 cách diễn; F4 ふっ "phù" vs "Fu"; F5 ん "Ưn/ưn" trước nguyên âm; F6 1708 (audit ghi 16u, chuỗi 15u).
- Lượt soát 2: 6/6 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `439e80f22d9abfcda5843f8d2f2844ca` khớp audit; CSV3 1 bộ duy nhất 297 dòng, 0 key trùng; JSON 6 mục, khóa string; khối TOML 6 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 52 file / 1291 dòng sai (moan)** (cơ sở 51 file / 1285 dòng + 6 file này — cơ sở đã tự kiểm chứng lại từ ROUTE-MOANS.md)
- Parent kiểm chứng 22/11 ~07:55: JSON 6 mục dạng chuẩn, khóa string; khối TOML 6 khóa, 0 sai lệch giá trị; jp/tw khớp CSV3 6/6; old_vn khớp CSV3 hoặc giá trị audit cùng key (1708 old_vn = giá trị audit 15u); đếm nguyên âm kiểm chứng độc lập: 1023 4a ✓, 1173/1263 "Soutetsuu" 3u ✓, 1708 JP 16u, fix mới 16u ✓ (audit ghi 16u nhưng chuỗi chỉ có 15u — sửa lỗi chép của audit); sweep 17 mục, 0 key trùng với 6 key sửa; không dòng gasp Ư nào bị đụng; không dòng "Kh" (file không có dòng Kh); lượt soát 2: 6/6, 0 bỏ, 0 sửa.
- FLAG (đợt thống nhất): F1 (ふえっ→"Fue" 991/992 — theo tiền lệ 日々姫h1 1022, cờ F4 của file đó vẫn chờ quyết; nếu giữ "Hả" cho thán từ ngạc nhiên thì hoàn 2 dòng); F2 (くっ "kư" vs "ku" — file dùng "kư" nhất quán, lr_ニイロクh giữ "ku"); F3 (SFX ぎゅ… dài trộn động từ Việt + kéo dài romaji); F4 (ふっ "phù" vs "Fu"); F5 (ん "Ưn/ưn" trước nguyên âm); F6 (1708 audit ghi 16u, chuỗi 15u — đã sửa).
- GHI CHÚ: 992 "Ư á" diễn うぁ (u+a, 2 mora) theo mẫu nội file 1021/1034 — không phải dòng gasp Ư, không thuộc diện cấm xem lại.

---

# Moan-fix snippet — lr真闇追加h_赤ちゃん、欲しか.txt.toml (moan-lr-mayami-tsuika-h-akachan-hoshika)

- File: `05_Mayami/lr真闇追加h_赤ちゃん、欲しか.txt.toml` — Mayami + Soutetsu, H-scene muốn có em bé (sau tuần trăng mật); 316 dòng.
- Đọc 316/316 dòng, xét 183 dòng rên/SFX, đổi 21 dòng (27 token), giữ 162 dòng.
- Họ fa/fu → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ ふかみh1/h2/h3, ハチロクh5/h6/h9, lr_ニイロクh): ふあっ→Fua (1097, 1098, 1107), ふぁ→Fua (1106), ぷあ→Pua/pua (1112, 1152, 1186); dạng tách ふ、あ→"Fu, a" (1106, 1276).
- Họ く → romaji (h6 §3c: くっ/んくっ trong chuỗi rên → Ku/Ưm ku; "Hự" mất phụ âm k): くっ→Ku (1093, 1127, 1292, 1805×2, 1843), んくっ→"ưm ku" + く→Ku (1097), く……→"Ku……" (1094), んぎゅ→"Ngyu" (1127, tiền lệ ポーレットh2 928), かはっ→"Kaha" (1184, tiền lệ trực tiếp h5 1181), くはっ→"Kuha" (1078, 1185), きうっ→"Kiu" (1087, tương tự — xem cờ F2).
- Họ や → romaji (tiền lệ h6 816): やっ→"Ya" (1067), やあっ→"yaa" (1013).
- Đếm nguyên âm (audit bỏ sót): 1103 はあっ→"Haa" (2a) + んあっ→"Na" (tiền lệ h6 843).
- 7/21 dòng xây trên giá trị audit cùng key (1097, 1098, 1106, 1107, 1112, 1152, 1186 — chỉ đổi đúng token rên); 14 dòng audit bỏ sót.
- Audit §4 đã đúng, giữ nguyên 24 dòng (romaji Hya/Kya/Nkyu/Fua…; đếm 1071 19a / 1072 17u+n / 1100 17a+n / 1163 9u+n kiểm lại bằng máy); giữ ふっ độc lập → "phù", grunt むっ/うっ/ぐっ → "hự", んう → "Ưm", ちゅうっ → "chùn chụt" (2u), cười "Ưm fufu"/"Fufu".
- Sweep gasp kiểm tra trực tiếp 9/9 mục (1016, 1108, 1125, 1128, 1129, 1130, 1141, 1254, 1542) — đều là dòng Ư của audit, không đụng; không có dòng "Kh" nào trong file; 0 dòng gasp Ư nào bị đổi.
- Cờ đợt thống nhất: F1 độ dài lặp SFX （ ） diễn bằng từ (1824/1850/1815/1877/1162/1818); F2 1087 "Kiu" (chỉ có tương tự, chưa có tiền lệ trực tiếp); F3 1078/1185 "Kuha" (tương tự Kaha h5 1181); F4 1276 っふ (có thể là gasp bị mất); F5 1067 ッッ―― (có thể là gasp bị mất); F6 ranh giới grunt-vs-rên họ く; F7 dạng tách "Fu, a" vs h7 "phù, a"; F8 phạm vi họ や + んあっ→"Na"; F9 7 dòng thay thế giá trị audit; F10 1095 giữ theo audit §7.
- Lượt soát 2: 21/21 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `7968856545fdf8d9adb32df40193a073` khớp audit; khối TOML 21 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 53 file / 1312 dòng sai (moan)** (cơ sở 52 file / 1291 dòng + 21 file này) [parent REBASE 22/11 ~08:05 — snippet ghi cơ sở cũ 51/1285 vì lr_稀咲h1 đã gộp trong khi agent chạy]
- Parent kiểm chứng 22/11 ~08:05: JSON 21 mục dạng chuẩn, khóa string; khối TOML 21 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 21/21 (16 dòng) — 7 dòng trùng audit chỉ khác giá trị audit đúng ở token rên (áp MỘT giá trị moan mỗi key); đếm nguyên âm kiểm chứng độc lập: 1103 "Haa" 2a ✓, 1152 "chụụụt" 3u ✓, 1013 "yaa" 2a ✓; sweep 9 mục, 0 trùng 21 key sửa; audit §5 gasp 11 dòng, 0 trùng; không dòng "Kh" (file không có); lượt soát 2: 21/21, 0 bỏ, 0 sửa.
- Tiền lệ đã kiểm chứng: h6 §3c (くっ→"Ku", んくっ→"ưm ku"), h6 843 (んぁ→"Na"), paulette-h2 928 (んぎゅ→"Ngyu"), h5 1181 (かはっ→"Kaha"), や→"Ya" nhiều file.
- GHI CHÚ: 1094 "Ư"→"Ku……" và 1127 "Ưm"→"Ngyu" — 2 chỗ "Ư" cũ diễn mora KHÔNG phải gasp (く…… / んぎゅ, đều không có っ), không thuộc diện cấm xem lại dòng gasp Ư; nhãn "False" trong log kiểm tra của agent đã được giải thích (JP dòng 1094 có っ ở token khác — ふっ/あっ — đã giữ nguyên).
- FLAG (đợt thống nhất): F1 (độ dài lặp SFX （ ） diễn bằng từ); F2 (1087 "Kiu" chỉ có tương tự); F3 (1078/1185 "Kuha" tương tự Kaha); F4 (1276 っふ có thể là gasp bị mất); F5 (1067 ッッ―― có thể là gasp bị mất); F6 (ranh giới grunt-vs-rên họ く — audit §7 giữ "hự"); F7 (dạng tách "Fu, a" vs h7 "phù, a"); F8 (phạm vi họ や + んあっ→"Na"); F9 (7 dòng thay thế giá trị audit); F10 (1095 giữ theo audit §7).

---

# Moan-fix snippet — 真闇h1_長期熟成.txt.toml (moan-mayamih1-chouki-jukusei)

- File: `真闇h1_長期熟成.txt.toml` (route 05_Mayami), 298 dòng script; audit đã gộp 50 dòng sai.
- Đọc toàn bộ 298 dòng; xét 113 dòng rên/thở/gasp/SFX (78 thoại + 35 SFX ngoặc đơn).
- Đổi 8 dòng rên: 1010 やっ→"Ya", 1011 や→"Ya", 1050 あんっ→"An!", 1058 ちゅるるっ→"Chururu" + んちゅうっ→"ưm chuu", 1071 ふあっ→"fua" (Hepburn, audit giữ "phua" sai dạng), 1090 んあっっ→"Na!!?", 1173 "nữaaaa"→"nữaa" (4 a thừa → 2 a), 1792 （みち…っっ）→"Michiiiiiiiiii!!" (romaji, 9 い đếm bằng máy — audit ghi 11 い sai).
- Giữ 105 dòng, gồm các quyết định: 1080 んふっ→"ưm phư" (quy ước file), 1089 ごくんっ→"ực" (mất ん — cờ thống nhất), 1801/1803/1822 "Phụt!" gộp (phong cách file, tiền lệ lr-mayamih1), 1014 "Hya" (cờ Hieu vẫn mở).
- Cờ đợt thống nhất/Hieu: F1 1014 Hya vs Á (Hieu); F2 1089 ごくんっ (gokun?); F3 độ dài SFX びゅ; F4 1011 どろって; F5 1241 よぉ; F6 くっ→"Ư" vs "Ku".
- Lượt soát 2: 8 tổng / 8 tái kiểm chứng / 0 bỏ / 0 sửa.
- Kiểm chứng: JSON 8 mục khóa string, jp/tw/old_vn khớp CSV3 8/8; khối TOML 8 khóa parse OK, 0 sai lệch; 0 key trùng audit; không chạm dòng "Kh" hay Ư gasp.

**Tổng cộng sau file này: 54 file / 1320 dòng sai (moan)** (cơ sở 53 file / 1312 dòng + 8 file này)
- Parent kiểm chứng 22/11 ~09:45: JSON 8 mục dạng chuẩn, khóa string; khối TOML 8 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 8/8 (1 bộ duy nhất, 298 dòng, 0 key trùng); TOML md5 af87cd63e115c1890a4aa1a0a05fec4b khớp agent; 0 key trùng audit (50 key audit); đếm nguyên âm kiểm chứng độc lập: 1792 JP 9 い, fix "Michiiiiiiiiii" = chi-i + 9 い ✓; 1173 よぉ 2a ✓; 1058 ちゅう 2u ✓; sweep 5 mục, 0 trùng 8 key sửa; không dòng gasp Ư nào bị đụng; không dòng "Kh"; lượt soát 2: 8/8, 0 bỏ, 0 sửa. Newline trong fix (1011/1071/1173) là real newline — khớp 43 tiền lệ đã gộp (vd. hachiroku-h5), game auto-wrap, không ảnh hưởng.
- FLAG (đợt thống nhất): F1–F6 như trên; thêm: 1058 "ưm chuu" trộn "ưm" VN + romaji trong một âm — tiền lệ mâu thuẫn (lr-h1 1097 giữ "Ưm kyu" vs ポーレットh2 sửa 7 dòng tương tự về romaji thuần "Nhyu"/"Nkyu"); chờ quyết chung dạng ん+romaji.

---

# Moan-fix snippet — ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml (moan-hachiroku-h4-jelly-syringe-condom)

- File: `01_Hachiroku/ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml` — Hachiroku + Soutetsu, H-scene gel/ống tiêm/bao cao su; 306 dòng.
- Đọc 306/306 dòng, xét 103 dòng rên/SFX (56 thoại + 47 SFX ngoặc), đổi 26 dòng, giữ 77 dòng.
- Họ fa/fu → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ h6 §3a, lr_mayami-tsuika-h): ふあっ→Fua (867, 918, 946, 947), ぷあっ→Pua (991); giữ ふやっ→"Phuya" (988, 1121).
- Họ ひゃ/ひゅ/きゃ → romaji (quy tắc 3b): ひゃうっ→Hyau (932, 935), ひゃうんっ→Hyaun (936), ひゃぐっ→Hyagu (933), ひゃふっ→Hyafu (934), きゃふっ→Kyafu (926), あひゅっ→Ahyu (971).
- Họ く → romaji (h6 §3c): く――→Ku (955), くあっ→Kua (979), くっ→Ku (989, 1003), んくっ→"ưm ku" (1013).
- Đếm nguyên âm (cờ audit F2, đếm lại bằng máy): 928 7a, 1000 9i, 1121 4i, 866 12u→"Fuuuuuuuuuuuu", 1002 6u→"Kufuuuuu", 931 5u→"Kyufuuuu", 987 ちゅうっ 2u→"chụụt" + ちゅううっ 3u→"chụụụt"; 952 ちゅうっ→"chụụt"; 1070 かはっ→"Kaha".
- 13/26 dòng thay thế giá trị audit cùng key (866, 867, 918, 926, 931, 933, 935, 936, 946, 947, 991, 1013, 1121); 13 dòng xây trên VN gốc CSV3.
- SFX trong ngoặc giữ cả 47 dòng (quy ước diễn nghĩa của file: "Phập"/"Bụp"/"Siết chặt"/"Trượt"/"Phụt"/"Kéo"/"Cộc" cho こちゅんっ — tiền lệ lr_日々姫ふかみh1 2452).
- Sweep gasp kiểm tra trực tiếp 32/32 mục — đều đã nằm trong audit; không đụng dòng gasp Ư nào; file không có dòng "Kh".
- Cờ đợt thống nhất: F1 ranh giới rên-vs-grunt họ く (955/979/989/1003/1013); F2 công thức đếm cho SFX ngoặc dài (1666/1685/1669/1662/1714/1713/1691/1716/1651/1708/1699/1697/1695); F3 1684 "rồi!"; F4 やっ "Ya" vs "Á" (mâu thuẫn moan-h8 2187); F5 dạng tách fa 965 "phù——a"; F6 ふうっ "Phù" vs "Phùu" (944); F7 SFX "Kéo" 1682/1693.
- Lượt soát 2: 26/26 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `3ed7f3af6db48bb4a7f02fe4ae6a2eed`; CSV3 1 bộ 306 dòng, 0 key trùng; khối TOML 26 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 55 file / 1346 dòng sai (moan)** (cơ sở 54 file / 1320 dòng + 26 file này) [parent REBASE 22/11 ~09:55 — snippet ghi cơ sở cũ 53/1312 vì 真闇h1 đã gộp trong khi agent chạy]
- Parent kiểm chứng 22/11 ~09:55: JSON 26 mục dạng chuẩn, khóa string; khối TOML 26 khóa, 0 sai lệch giá trị; jp/tw khớp CSV3 26/26; old_vn khớp CSV3 13/13 (13 dòng còn lại old_vn = giá trị audit cùng key — diff moan-fix vs audit-fix chỉ khác đúng token rên, đã kiểm chứng cơ học 13/13); TOML md5 khớp agent; đếm nguyên âm kiểm chứng độc lập: 866 12u ✓, 1002 6u ✓, 931 5u ✓, 928 7a ✓, 1121 4i ✓, 987 2u/3u ✓, 952 2u ✓; sweep 32 mục (30 trong audit + 2 already-rendered 1718/956), 9 key trùng sweep chỉ khác đúng token rên, giữ nguyên mọi Ư của audit; không dòng "Kh"; lượt soát 2: 26/26, 0 bỏ, 0 sửa.
- SỬA (parent): key 1000 "Ư iiiiiiii" (8 i) → "Ư iiiiiiiii" (9 i) — agent đếm thiếu 1: JP んひいいいいいいいいっ có ひ(1) + い×8 = 9 âm i (agent ghi "い×7"); đã sửa wrong.json + REVIEW (§3d, §7, khối TOML) + snippet.
- FLAG (đợt thống nhất): F1–F3, F5–F7 như trên. F4 ĐÃ GIẢI QUYẾT lúc gộp: tiền lệ "moan-h8 2187" KHÔNG tồn tại (parent đã kiểm chứng ở lần gộp hachiroku-h1 21/11 ~14:15: h8 không có key 2187 trong CSV3 lẫn audit wrong.json) — "Ya" cho やっ giữ nguyên, không còn mâu thuẫn.

# Moan-fix snippet — lr_日々姫h2_デザートは食事の前に.txt.toml (moan-lr-hibikih2-dessert-wa-shokuji-no-mae-ni)

- File: `02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml` — H-scene Hibiki "món tráng miệng trước bữa ăn"; 288 dòng.
- Đọc 288/288 dòng, xét 149 dòng rên/SFX (112 thoại + 4 độc thoại gasp + 33 SFX ngoặc), đổi 5 dòng, giữ 144 dòng.
- Lỗi duy nhất: ふあっ (2 mora) bị render thiếu mora "u" thành "Fa"/"fa" — sửa "Fua"/"fua" (1172, 1173 token 2, 1174, 1175, 1176); tiền lệ moan-h4 ふあっ→"Fua", quy tắc romaji fallback 21/11 ~01:56.
- ふぁ (1 mora) đã đúng, giữ: 1106 "fa", 1038 "famu"; ぷぁ/ぷあ giữ: 949/1051/1089 "pua"/"Pua!".
- Họ ひゃ/ひゅ/ひあ → romaji đúng quy tắc 3b, giữ: 937 "Hyua" (14a/2n), 941 "Hyua", 942 "Hyagu", 943 "Hia", 946 "Hya", 1185 "hia".
- Nói ngọng (miệng đầy) không phải dòng rên, giữ: 1033 "Hyababa, bafi", 1057 "meshiagare".
- Grunt Soutetsu họ く/グッ → "Hự" nhất quán toàn file, giữ: 696, 697, 948, 968, 969, 970, 1159.
- Cờ audit (6) đã giải quyết — giữ: 939 "fu"/"a", 984 "ha", 994 中っ (ngắt diễn bằng —— + "a!"), 1169/1170/1171 "ha" (ngắt diễn bằng ——/!).
- Audit đếm nguyên âm/phụ âm kiểm chứng lại bằng máy, tất cả đúng: 937 14a/2n, 973 3u, 1001 10u/2n, 1016 2u/3u/8u, 1043 12o, 1066 10u, 1070 19t, 1088 6a, 1658 4ự, 1660 6i, 1677 13u, 1682 4o/2o, 1686 11i, 1687 10o, 1688 5i.
- SFX ngoặc giữ toàn bộ (quy ước diễn nghĩa của file); không đụng dòng gasp Ư nào; file không có dòng "Kh".
- Cờ đợt thống nhất: F1 công thức đếm t/c cho SFX ngoặc dài (1666 4t vs 1668 5t cùng 3u; 1679, 1681, 1682/1683); F2 1659 "Siết chặt!" không kéo dài; F3 "nfufu" vs "Nfufu"; F4 "Phùa" vs "Fua"; F5 1665 "phụ——t".
- Sweep gasp kiểm tra trực tiếp 16/16 mục — đều đã nằm trong audit; không đụng dòng gasp Ư nào.
- Lượt soát 2: 5/5 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `278bb98599c53cd1d22db62a29101c26`; CSV3 1 bộ 288 dòng, 0 key trùng; khối TOML 5 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 56 file / 1351 dòng sai (moan)** (cơ sở 55 file / 1346 dòng + 5 file này)

# Moan-fix snippet — 日々姫h3_汚れてしまった制服で.txt.toml (moan-hibikih3-yogorete-seifuku)

- File: `02_Hibiki/日々姫h3_汚れてしまった制服で.txt.toml` — Hibiki + Soutetsu, H-scene đồng phục bị bẩn; 322 dòng.
- Đọc 322/322 dòng, xét 116 dòng rên/SFX, đổi 24 dòng, giữ 92 dòng.
- Họ fa/fu → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ h6 §3a, lr_mayami-tsuika-h, h4): ふあっ→Fua (1016, 1041, 1053, 1071, 1077, 1084, 1100, 1121), ふっ/ふ tách riêng→Fu (1013, 1018, 1021, 1039, 1055, 1109, 1112, 1142), ぷあっ→Pua (1056, 1111, 1114); giữ ふやっ→"Phuya" (1042, dạng khóa + tiền lệ h4).
- Họ ひゃ/ひゅ/ひあ/きゃ → romaji (quy tắc 3b): chỉ 1027 sai (ひあっ "Hyaa!"→"Hia!"); 18 dòng còn lại đã đúng (1024 "Hyaan", 1026 "Hyan", 1031 "Kyafu", 1121 "Nhyauuuu"/"Hia", 1041 "Hia", v.v.).
- Mất phụ âm mora: 1050 ぬ―― "Ư"→"Nuu" (tiền lệ ROUTE-MOANS 2686); 1010 �んううっ "ưm ưm!!!"→"Nuu!!!" (một âm dài bị tách mảnh + mất うう).
- Trộn 2 hệ trong một âm: 1124 "Ưm phuuuuuuuuuuu"→"Nfuuuuuuuuuuu" (11u; fix audit đếm SAI 12u — JP có 10 う → 11u; bản moan đè lên giá trị audit).
- 16/24 dòng thay thế giá trị audit cùng key (chỉ khác đúng token rên); 8 dòng mới xây trên VN gốc CSV3 (1027, 1050, 1055, 1056, 1111, 1112, 1114, 1142).
- SFX trong ngoặc giữ toàn bộ 48 dòng (quy ước diễn nghĩa của file); không đụng dòng gasp Ư nào (1262/1264 là giá trị audit); file không có dòng "Kh".
- Cờ đợt thống nhất: F1 1124 đếm audit sai 12u→11u; F2 ふっ→"Fu" không hoàn lại "Phù"; F3 1136 "Hừ hừm." giữ (romaji "Fuffuun" là phương án khác); F4 1010 "Nuu!!!" phán đoán mới; F5 や→"Ya" (quyết toàn dự án vẫn mở).
- Sweep gasp kiểm tra trực tiếp 3/3 mục — 1262/1264 đã nằm trong audit, 1855 giữ nguyên; không đụng dòng gasp Ư nào.
- Lượt soát 2: 24/24 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `fd705de9bad2a12e224c2264772c06d6`; CSV3 1 bộ 322 dòng, 0 key trùng; khối TOML 24 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 57 file / 1375 dòng sai (moan)** (cơ sở 56 file / 1351 dòng + 24 file này) [REBASE 22/11 ~10:15 — snippet ghi cơ sở cũ 55/1346 vì lr_日々姫h2 (5 dòng) đã gộp trong khi agent chạy; parent đã gộp lr_日々姫h2 10:13, GitHub 5ad2d1da]

# Moan-fix snippet — ハチロクh3_磨き洗い.txt.toml (moan-hachirokuh3-migaki-arai)

- File: `01_Hachiroku/ハチロクh3_磨き洗い.txt.toml` — H-scene Hachiroku "cọ rửa" (tắm chung ở Tororyu-yu sau ca trực); 312 dòng, audit sai 44 (27 gasp, 14 đại từ, 3 nghĩa).
- Đọc 312/312 dòng, xét 78 dòng rên/SFX/breath (24 đổi + 54 giữ theo §3), đổi 24 dòng.
- fa/fu → romaji (5): 964, 1012, 1015, 1127 ふあっ→"Fua"; 1084 ぷあっ→"Pua" — nhất quán với h2/h5/h6/h7/h8/h9 + lr_日々姫h2 (vừa merge, 5/5 đều Fua); "Phùa" nghe ngượng. F1 để đợt thống nhất chốt một dạng chung.
- Họ ひゃ/きゅ → romaji (2): 1006 ひゃふっっ "Hya fư"→"Hyafu" (tiền lệ ひゃふっ→"Hyafu"); 1218 んきゅっ "Ưm kya"→"Nkyu" (tiền lệ 3 file).
- Đếm nguyên âm — rên (6): 1029 くあぁっ+あぁぁぁっ→"Kuaa Aaaa!" (6a, khôi phục k-); 1030 ずぞぉ×8→"Zuzooooooooo!!!" (9o, khôi phục z-, sửa a→o); 1034 あ+5ー→"A a a a a a" (6a, giữ phong cách cách khoảng); 1062 んひいいっ→"Nhiii!!?" (3i); 1063 んふ+14う→"Nfuuuuuuuuuuuuuuu～～～!" (15u; F2 của audit đếm thiếu — nói 13う, thực tế 14う); 1064 んう×6→"Nuuuuuu!!!" (6u theo tổng Hepburn — xem cờ F6).
- SFX sai lớp nghĩa (2): 1794 + 1807 じゅぶっ "Sột sột"→"Phập!" (âm chèn ướt, TW 啾; tiền lệ 1811 trong file).
- SFX dài → romaji (6): 1828 ずりゅ+12う→"Zuryuuuuuuuuuuuuuu!!!" (14u); 1829 すりゅ+4う→"Suryuuuuu" (6u; "Sột sột" còn sai lớp — すりゅ là trượt); 1832 ずる+4う→"Zuruuuuu" (6u; audit F2 bỏ sót); 1835 ずぶ+11う→"Zubuuuuuuuuuuuuu!!!" (13u); 1836 きゅ+6う→"Kyuuuuuuu!!!" (7u); 1837 ずぼ+9お→"Zuboooooooooo!!" (10o).
- Đếm nguyên âm — SFX (1): 1813 ちゅろぉぉぉ "Chụụụt" (3ụ)→"Chụụụụt" (4ụ; ろ+3ぉ = 4o).
- Cười → romaji (2): 1009 うふふっ "Ư fufu"→"Ufufu" (cười không gắn gasp Ư); 1677 "ư fufu"→"ufufu" (trích dẫn trong lời dẫn).
- Giữ nguyên: gasp Ư của audit (783/784/785/1221/1222/1226) không đụng; họ ひゃ đã romaji đúng (1007/1017/1023/1149); hơi thở/ngắn đã đúng (1010/1045/1046/1048/1049/1065/1066/1067/1068/1069/1037/1038/1039/1040/1044/1088/1089/1106); SFX ngắn đã đúng (1792/1793/1800/1806/1808/1810/1811/1814/1816/1818/1820/1823/1824/1826/1827/1833/1834/1838/1839/1840/1795/1805/1791/1787); 1224 chuỗi liếm "Liếm——liếm——chụt——liếm láp～" giữ (sweep "already-rendered"); 1139 nói ngọng không phải dòng rên.
- 1801 ぶりゅん→"Phập!" GIỮ (âm đâm/va chạm; "Phụt" sẽ đụng SFX xuất tinh trong file) — cờ F2.
- Cờ đợt thống nhất: F1 fa/fu một dạng chung ("Phùa" vs "Fua"); F2 1801 ぶりゅん; F3 じゅぶっ "Chu mút" (1809) vs "Phập!" (1811/1794/1807); F4 1810 "trượt" viết thường; F5 1815 くっ→"Ngoáy" vs 1089 くっ→"hự"; F6 phương pháp đếm — tổng Hepburn thay vì "1 + số う" đọc đen (1064: 6u không phải 7u); F7 cf. cờ F2 lr_日々姫h2 (1659 "Siết chặt!" không kéo dài) vs 1836 → romaji; F8 đếm F2 của audit (1063: 14う không phải 13う).
- Sweep gasp kiểm tra trực tiếp 23/23 mục — 20 nằm trong audit, 1 trong fix moan này (1063), 2 "already-rendered" không fix (1066, 1224) đều giữ đúng; không đụng dòng gasp Ư nào; không đổi dòng "Kh" nào.
- Lượt soát 2: 24/24 tái kiểm chứng, 0 bỏ, 1 sửa (1832 "Zuruuuuuu" 7u → "Zuruuuuu" 6u — JP thật có 4う, đếm tay ban đầu sai). TOML md5 `beac73e26039824c4868e4f3a22cc212`; CSV3 1 bộ 312 dòng, 0 key trùng; khối TOML 24 khóa parse OK, 0 sai lệch.
- LƯU Ý: hai file scratch cũ `.work-h3-cands.json` / `.work-h3-all.json` có JP BỊ LỆCH (vd. 1021 hiển thị JP chứa ふぁっ, JP thật không có) — mọi fix đã xây lại trực tiếp từ CSV3 + audit JSON; hai file scratch đó cần xóa.

**Tổng cộng sau file này: 58 file / 1399 dòng sai (moan)** (cơ sở 57 file / 1375 dòng + 24 file này) [REBASE 22/11 ~10:27 — snippet ghi cơ sở cũ 56/1351 vì 日々姫h3 (24 dòng) đã gộp trong khi agent chạy; parent đã gộp 日々姫h3 10:16, GitHub bdf55681]

# Moan-fix snippet — 凪h1_ふたりっきりのデート.txt.toml (moan-nagih1-futarikkiri-no-date)

- File: `07_Nagi_Fukami/凪h1_ふたりっきりのデート.txt.toml` — H-scene Nagi "hẹn hò chỉ có hai người"; 291 dòng.
- Đọc 291/291 dòng, xét ~120 dòng rên/SFX, đổi 15 dòng, giữ ~105 dòng.
- Lỗi chính: họ fa/fu bị tách mảnh ("Phù a") hoặc mất âm a ("Phù") — romaji Fua/Fa/Fue/Pua (10 dòng, 11 token: Fua ×6, Fa ×1, Fue ×3, Pua ×1); mất phụ âm mora (Ya 1046, Í 1054, Ku 1067, Kuhyun 1096, Nan 1084); đếm nguyên âm 1060 (23→18).
- Audit đã sửa đúng 12/17 dòng rên — giữ; 4 dòng xây trên fix audit (1046, 1086, 1087, 1096); 1 dòng hoàn lại fix audit (1091 "Phuê?" → "Hể?" — thán từ ngạc nhiên, không phải rên).
- Giữ: "Phuya"/"Phuyau" (1053/1057/1081, dạng khóa), "Fan"/"Fan!!" (1080/1082, Hepburn giữ ん), "Phuê!?" 1090 (chờ Hieu ở reina-h3 1133), "Hia"/"Hya"/"Hyafun"/"Hyaun"/"Fukyun", ふっ→"Phù", ふ、あっ 1102 "Phù, a" (JP tách dấu phẩy, 2 token), ふ――あ 1106 "Phù——A" (2 âm), やっ 1105 "Không" (diễn nghĩa).
- Descriptive SFX giữ: 1768/1794/1797/1808 (kéo phụ âm p/t, chưa có quy tắc chốt), 1773 "Thắt tim! Siết chặt!" (dạng khóa cho きゅん), 1772 "Liếmmmm!" (audit, m×3 = お×3), 1195 "Sụt sụt" (audit).
- Sweep gasp kiểm tra trực tiếp 6/6 mục (850, 1069, 1083, 1116, 1152, 1214) — đều đã nằm trong audit; không đụng dòng gasp Ư nào (1152 giữ Ư của audit); file không có dòng "Kh".
- Cờ đợt thống nhất: F1 ふぇ "Fue" vs "Phuê" (ふかみh1 993, 凪ふかみ01 1547 giữ "Phuê"); F2 ふや "Phuya" vs "Fuya" (lr_凪h1); F3 1090 chờ Hieu (reina-h3 1133); F4 1091 hoàn lại fix audit; F5 SFX kéo phụ âm (1768/1794/1797/1808); F6 くっ "Ku" (đối thoại 1067) vs "Ư" (SFX độc thoại 1766/1770/1780); F7 1060 chuẩn hoá nghiêm (23→18 nguyên âm).
- Lượt soát 2: 15/15 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `80187d06a1deaeb1799ea3eb800e662e`; CSV3 1 bộ 291 dòng, 0 key trùng; khối TOML 15 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 59 file / 1414 dòng sai (moan)** (cơ sở 58 file / 1399 dòng + 15 file này) [REBASE 22/11 ~10:31 — snippet ghi cơ sở cũ 56/1351 vì 日々姫h3 (24) và ハチロクh3 (24) đã gộp trong khi agent chạy; parent đã gộp cả hai, GitHub bdf55681 + 89a698bc]

# Moan-fix snippet — 稀咲h2_プライベートルーム (06_Kisaki)

- File: `稀咲h2_プライベートルーム.txt.toml` (323 dòng, đọc 323/323; CSV3 1 bộ, 0 khóa trùng; TOML md5 `3faad778393314e55d05226b04768417`).
- Audit của file: 24 fix — 12 rên/SFX + 9 gasp Ư + 3 sai nghĩa. Sweep: 9 entry, audit nhận hết.
- Moan-fix: **4 dòng đổi**.
- 1108 [稀咲] moan-vowel: ふうっっっ "fuuu" → "fuu" (ふ1u + う1u = 2u; っっっ không thêm nguyên âm).
- 1253 [稀咲] moan-gasp-lost: はっ bị mất thành "thì" → "ha" (quy ước file: はっ→"ha" ×6 dòng khác).
- 1267 [稀咲] moan-romaji: ふぁ "fua" → "fa" (ふぁ = 1 mora "fa"; tiền lệ ふかみh2 1025, ふかみh3, ハチロクh5/h6).
- 1960 [monologue] moan-vowel: sửa đếm của audit — "（Kyuuuuun!）" 5u → "（Kyuuuuuun!）" 6u (きゅ1u + う×5; review audit ghi đúng 6 nhưng chuỗi fix chỉ có 5). old_vn = giá trị fix của audit; khi áp dụng dùng bản moan này THAY bản audit.
- Giữ nguyên: 11/12 fix rên/SFX của audit (1152 Hyaa, 1154 Hyau, 1161 Fu kyuu + ưƯ, 1168/1198/1201/1219 Ư, 1218 Nhyu, 1941 Chụt, 1961 Gừ, 1972 Giẫm/tuốt/cọ/nắn); 9 dòng gasp Ư không xem lại; 3 dòng sai nghĩa không chạm.
- Cờ đợt thống nhất: F1 độ dài SFX diễn bằng từ Việt (1932–1936, 1942, 1944, 1955, 1963); F2 912 っ đầu dòng giữ; F3 1199 "mu chu"; F4 cụm đại từ Kisaki (audit đã cờ); F5 1961 ぐっ "Gừ"/"Thúc".
- Lượt soát 2: 4/4/0/0. Khối TOML 4 khóa parse đạt, 0 sai lệch.

**Tổng cộng sau file này: 60 file / 1418 dòng sai (moan)** (cơ sở 59 file / 1414 dòng + 4 file này) [REBASE 22/11 — cơ sở giao lúc spawn 58/1399 đã cũ vì 凪h1 (15 dòng) đã gộp 10:31; đã kiểm chứng với ROUTE-MOANS.md]

# Moan-fix snippet — 日々姫h4_いもうとタオル.txt.toml (moan-hibikih4-imouto-taoru)

- File: `02_Hibiki/日々姫h4_いもうとタオル.txt.toml` — Hibiki + Soutetsu, H-scene khăn tắm em gái; 296 dòng.
- Đọc 296/296 dòng, xét toàn bộ 133 dòng thoại + 35 dòng SFX độc thoại trong （ ）, đổi 29 dòng.
- Họ fa/fu → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ 日々姫h3, ハチロクh3, lr_日々姫h2): ふあっ→Fua (972, 988, 995, 1001, 1006), ふっ/ふ tách riêng→Fu (1002, 1014, 1029, 1034, 1040), ふぁ→Fa + ふ、ぁっ→Fu, a (1032), ぷぁ→Pua (1041), ふぇ/ふえっ→Fue (990, 991 — cờ F1); giữ ふやっ→"Phuya" (964, tiền lệ 日々姫h3 1042 — cờ F2).
- Chuỗi dài/đếm nguyên âm: 967 んうううううううっっ (8 mora) "ưm ư…"→"Nuuuuuuu"; 1054 くひゅううううううううんっ (10u) "Ưm hyuuuuuuuuun"→"Kuhyuuuuuuuuun" (khôi phục phụ âm k bị mất).
- Mất phụ âm sau ん (cờ (4) của audit): 1035 んぇっ "ưm"→"Ne"; 1040 んくっ "ưm"→"Nku" (tiền lệ ハチロクh3 1218 んきゅっ→"Nkyu"); 1075 んきゅっっ "ưm kyu"→"Nkyu".
- Cười + liếm dài: 1052 んふふっ→"Nfufu" (tiền lệ ハチロクh3 1009), れろおおおっ→"Reroooo" (cờ F6).
- SFX độc thoại dài/dồn (cờ (3) của audit): 1757 ずぶ+9う→"Zubuuuuuuuuuu", 1765 びゅ+10う→"Byuuuuuuuuuuu", 1783 ずろおおぽおおおおおおおおおおっ (14 o)→"Zurooopooooooooooo", 1758 ちょっおおおおおおおおっ→"Chooooooooo", 1743 ずろおおおっ→"Zuroooo", 1762/1770 dãy びゅ→romaji giữ độ dài + る, 1754 4 SFX じゅ→"Jubu! Ju!! Juba!! Jubo!", 1746 ぷりゅんっ→"Puryun!" (cờ F5), 1759 chỉ sửa ずばっ "Bạch!"→"Phập!" (cờ F4).
- 12/29 dòng thay thế giá trị audit cùng key (chỉ khác đúng token rên); 17 dòng mới xây trên VN gốc CSV3.
- Giữ: 993 っと→"Hự" đã XÁC NHẬN (tiền lệ cùng file 1028 くっ→"hự"); 964 "Phuya"; 971/962 んう ngắn đúng số lượng; 1051/1053 chuỗi ngắn đúng; 987/994/997/1019/976 romaji đã đúng; 1760 4 SFX đều đúng từ; 1794/1782 "Thúc mạnh" (cặp っ×5 — cờ F7); 1756/1796/1747/1788/1768/1787 SFX nhớt/trượt diễn nghĩa.
- Cờ đợt thống nhất: F1 ふぇ Fue/Phuê; F2 ふや Phuya/Fuya; F3 "Nfufu" viết hoa; F4 dãy じゅ/ず dồn romaji hay "Phập!"; F5 ぷりゅん→"Puryun!"; F6 れろ dài romaji hay "liếm láp"; F7 っ×5 "Thúc mạnh" hay romaji; F8 んぇ→"Ne"/んく→"Nku" (dạng mới); F9 く→"Ku" trong thoại.
- Sweep gasp kiểm tra trực tiếp 3/3 mục — 1182/1183 đã nằm trong audit, 1065 giữ nguyên; không đụng dòng gasp Ư nào (1024/1182/1183).
- Lượt soát 2: 29/29 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `5d1c304fe9a442ab317f5087d5e53464`; CSV3 1 bộ 296 dòng, 0 key trùng; khối TOML 29 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 61 file / 1447 dòng sai (moan)** (cơ sở 60 file / 1418 dòng + 29 file này) [REBASE 22/11 ~10:36 — cơ sở lúc spawn là 58/1399; 凪h1 (15 dòng) và 稀咲h2 (4 dòng) đã gộp trong khi agent chạy]

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

# Moan snippet — lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml (06_Kisaki)

- File: `lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml` (06_Kisaki) — TOML md5 `947b7e40987a5d77e8a0f963aed53302`, 320 dòng script, CSV3 1 bộ duy nhất, 0 key trùng.
- Đọc 320/320 dòng; xét 137 dòng rên (92 thoại + 45 SFX độc thoại); đổi 25 dòng.
- fa/fu → romaji (7): 782 ふっ→"Fu", 1074 ふあっ→"Fua", 1085 ふうぅ→"Fuuu", 1100 ふあっ→"Fua", 1112 ふっ→"Fu" + ふあっ→"Fua", 1144 ふ、ふっ→"Fu, fu", 1147 ふ→"Fu, a".
- Romaji (9): 784 ぷあ→"Pua", 1114 んうっ→"Nu", 1162 んあっ→"Na", 1265 ぺちゅううっ→"chụụụt" + ぷあ→"Pua", 1296 んうっ→"Nu", 1819 ずちゅううううっ→"Zuchuuuuu" (6u), 1823 にちゃあああああああっ→"Nichaaaaaaaa" (8a), 1857 にゅるうううううううううっっ→"Nyuruuuuuuuuuu" (11u), 1883 くちいいいっっっっっ→"Kuchiiii" (4i).
- Vowel-count (6): 1110 ああ→"Aa", 1121 ううっ→"Uu", 1180 ああ→"Aa", 1834 c 8→9, 1867 c 13→15, 1880 c 9→10.
- SFX thiếu âm (3): 1828 +じゅくっ→"Nhóp nhép", 1839 +しこっ→"Sột soạt", 1848 +しゅちゅっ→"Nhóp nhép".
- Không đụng dòng Ư gasp đã khóa (sweep 8 mục đã áp bởi audit); old_vn = audit fix với 4 key (1074/1085/1100/1112), còn lại CSV3 VN.
- Cờ unification F1–F9: F1 1861 "Thọc sâub…" (17b/11u), F2 1865 "Siết chặtt…" (21t/13u) — lớp verb-render + kéo dài; F3 1162 んあっ→"Na" (phạm vi còn mở, cf. ROUTE-MOANS F8); F4 1110/1180 ああ→"Aa" (tiếng thở giao tiếp); F5 1820/1845 dưới ngưỡng romaji; F6 1817 dạng động từ lỏng; F7 1071 もっとおおおっ; F8 1860 giữ (5ụ=5, trùng ハチロクh3 1860); F9 1124 "ra rồiiiii".
- Second pass: 25/25 đọc lại, 0 loại bỏ, 2 sửa (1819 đếm lại 5u→6u; 1112 sửa dấu gạch). JSON 25 = TOML block 25, parse 0 mismatch, jp/tw/old_vn 0 lệch, đếm nguyên âm dài bằng máy.

**Tổng cộng sau file này: 63 file / 1500 dòng sai (moan)** (cơ sở 62 file / 1475 dòng + 25 file này) [REBASE 22/11 — cơ sở giao lúc spawn 58/1399 đã cũ vì 凪h1 (15), 稀咲h2 (4), 日々姫h4 (29), 真闇h2 (28) đã gộp trong khi agent chạy; đã kiểm chứng với ROUTE-MOANS.md]

# Moan-fix snippet — 日々姫h2_洗って大丈夫なスーツ.txt.toml (moan-hibikih2-aratte-daijoubu-na-suits)

- File: `02_Hibiki/日々姫h2_洗って大丈夫なスーツ.txt.toml` — H-scene Hibiki (ngủ gật ở phòng thị trưởng → bế về → cởi vest "giặt được" → trước gương); 290 dòng, audit sai 16.
- Đọc 290/290 dòng, xét 98 dòng rên/SFX (35 SFX độc thoại + 24 thoại token rên + 39 thoại gasp), đổi 8 dòng.
- Mất âm (1): 1064 かっ bị mất → thêm "Ka——" (audit §4(2) cờ cho vòng moan; TW cũng bỏ).
- Đuôi moan dài (1): 1071 んううううう～っ → "Nuuuuu!" (ん+5う = 5u; audit §4(1) để vòng moan quyết; tiền lệ ハチロクh3 1064).
- fa/fu → romaji (2): 1079, 1123 ふあっ→"Fua" (audit đổi "Phù"→"Phùa" giữ mora あ; moan pass chuyển romaji theo fallback Hieu duyệt — tiền lệ lr_日々姫h2/日々姫h3/ハチロクh3).
- んきゅ → romaji (3): 1126 んきゅっ→"Nkyu", 1138 んきゅ+7う+4ぅ→"Nkyuuuuuuuuuuuu" (12u; audit đã sửa số lượng 8→12u đúng, chỉ còn tách "Ưm kyu..."), 1139 んきゅんっ→"Nkyun" (tiền lệ ハチロクh3 1218 + quy tắc 3b んひゅ→"Nhyu"/んひゅん→"Nhyun").
- SFX (1): 1770 びゅくっ→"Phụt——" (TW toàn 噗噗 = phun; "Giật" diễn co giật sai lớp; audit §4(3)).
- Giữ nguyên: gasp Ư audit (843/1085/1086/1283); audit sửa đúng 1074 "Kuha", 1077 "Fuuuuuuuuun!" (9u), 1078 "Aaaaaaan" (8a), 1081 "Phuyan"; họ ひゃ/きゃ đã romaji (1058/1062/1064/1069/1070/1061); ふっ→"Phù" giữ (1096/1126/1133/1263); 1076 ふあ……ぁ……→"Phù... a..." giữ theo lý do audit §3 (đủ cả hai mora, ngữ cảnh nhẹ); cười "Nhehe"/"Ê hê hê"; ngủ "Khò"; SFX phun đồng nhất "Phụt!" (1764/1766/1771/1772).
- Cờ đợt thống nhất: F1 họ や ("A"/"Á"/"Yan" vs "Ya" — 1055/1060/1066/1067/1220, quyết định toàn dự án vẫn mở); F2 ふっ "Phù" (file này) vs "Fu" (日々姫h3); F3 ふや "Phuyan" vs "Fuya" (lr_凪h1); F4 độ dài SFX phụ âm t/c (1787/1797/1798); F5 くっ SFX tả 1757 "chụt"; F6 SFX phun dồn đồng nhất "Phụt!"; F7 1076 "Phù... a..." vs "Fua"; F8 fa/fu "Phùa" vs "Fua" đã chốt cho file này (→"Fua"), còn lại cho dòng audit ngoài file H.
- Sweep gasp kiểm tra trực tiếp 4/4 mục — 3 nằm trong audit (gasp), 1 already-rendered (1071, không sửa gasp); không đụng dòng gasp Ư nào; không đổi dòng "Kh" nào.
- Lượt soát 2: 8/8 tái kiểm chứng, 0 bỏ, 0 sửa. TOML md5 `406a1ba5a7f06dc38f49413d0fbe2d47`; CSV3 1 bộ 290 dòng, 0 key trùng; khối TOML 8 khóa parse OK, 0 sai lệch.

**Tổng cộng sau file này: 64 file / 1508 dòng sai (moan)** (cơ sở 63 file / 1500 dòng + 8 file này) [REBASE 22/11 ~10:50 — snippet ghi cơ sở cũ 62/1475 vì lr稀咲追加h (25 dòng) đã gộp trước trong cùng đợt; parent đã gộp lr稀咲追加h]

# Moan-fix snippet (BỔ SUNG) — ハチロクh3_磨き洗い.txt.toml (moan-hachirokuh3-migaki-arai-SUPPLEMENT)

- File: `01_Hachiroku/ハチロクh3_磨き洗い.txt.toml` — 312 dòng, audit sai 44; bản moan chính đã gộp 24 dòng (58/1,399).
- Bản bổ sung này xét 8 dòng sót từ bản nháp mồ côi `moan-hachiroku-h3-migaki-arai-wrong.json` (23 mục, không REVIEW, chưa gộp): 4 FIX + 4 KEEP.
- FIX (4): 963 んくっ "ưm"→"Nku" (mất k); 1007 ひゃうんっ "Hya ưm!"→"Hyaun!" (trộn 2 hệ diễn đạt trong 1 âm, sweep lost-gasp); 1039 うあっ "Ư a!"→"Ua!" (っ trên từ-âm bị mất, sweep lost-gasp, tiền lệ "Í"); 1067 んくっ "Ưm——"→"Nku——" (mất k, cùng lỗi như 963).
- KEEP (4): 1066 んううっ～っ "Ưm ưm～" (đủ 2 nguyên âm u, sweep already-rendered); 1106 raw っ "em thíchっ" đã sửa bởi audit, "ưm hưm!!" đủ âm; 1149 audit đã sửa "Hi a"→"Hye" + bỏ raw っ, "ưm ư" đủ 2 mora (đề xuất "ưm" của bản nháp làm mất う); 1678 ああん "A an" — JP chỉ có 2 あ (đếm bằng máy; brief ghi "3 a" là sai), "Aaan" của bản nháp là sai; 3 cờ sweep cho khóa này đều sai (JP không có っ).
- 2 dòng REVIEW đã gộp liệt "đã đúng" nhưng xét kỹ lại sai (1007, 1039, 1067) — bản bổ sung sửa lại nhận xét đó, có bằng chứng (sweep + quy tắc 仲国05 + tiền lệ).
- Lượt soát 2: 4/4 tái kiểm chứng, 0 bỏ, 0 sửa. JSON 4 mục = khối TOML 4 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 4/4.

**Tổng cộng sau file này: 64 file / 1512 dòng sai (moan)** (cơ sở 64 file / 1508 dòng + 4 file này)
