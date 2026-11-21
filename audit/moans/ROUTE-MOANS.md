# ROUTE-MOANS — H-scene moan fixes (romaji fallback)

Merged moan-fix log. Running totals: **25 files / 561 rows changed**.

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
