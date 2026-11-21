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
