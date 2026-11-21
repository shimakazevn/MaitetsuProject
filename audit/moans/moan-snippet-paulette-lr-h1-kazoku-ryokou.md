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
