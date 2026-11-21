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

**Tổng cộng sau file này: 3 file / 60 dòng sai (moan)** (cơ sở 2 file / 38 dòng + 22 file này)
- FLAG: 2 lỗi đếm của audit đã sửa trong đợt này (1468: 6→5 âm a; 2503: 17→18 âm u). 2500: parent đã kiểm tra lại khi merge — audit đã đúng, agent đếm sai, dòng đã loại (không sửa).
- LƯU Ý CHO PARENT: file moan h8 (`moan-paulette-h8-alice-rail-car-*`, 33 dòng) đã hoàn thành nhưng CHƯA merge vào ROUTE-MOANS.md — snippet của nó ghi cơ sở 2/38 → 3/71. Snippet này (sau khi parent loại 2500: 21 dòng) rebase thành 4 file / 92 dòng (3/71 + 21) nếu h8 merge trước.
