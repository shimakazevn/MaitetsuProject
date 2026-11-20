# ROUTE-MOANS — H-scene moan fixes (romaji fallback)

Merged moan-fix log. Running totals: **2 files / 38 rows changed**.

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
