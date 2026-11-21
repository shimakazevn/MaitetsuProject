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

**Tổng cộng sau file này: 20 file / 469 dòng sai (moan)** (cơ sở 19 file / 468 dòng + 1 file này)
- FLAG (cho Hieu): 1238 いっ → "I" (audit phán đoán; nếu Hieu thấy "Á!" tự nhiên hơn thì trả về "Á" — một dòng, dễ revert).
