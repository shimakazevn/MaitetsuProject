# ROUTE-MOANS — H-scene moan fixes (romaji fallback)

Merged moan-fix log. Running totals: **8 files / 205 rows changed**.

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
