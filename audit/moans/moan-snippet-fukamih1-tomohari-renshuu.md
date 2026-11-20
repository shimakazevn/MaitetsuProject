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
