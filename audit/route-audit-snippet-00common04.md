# ROUTE-AUDIT entry — 00_Common file 04 (共通04_キハ07。ポーレットとれいな)

- **File:** `00_Common/共通04_キハ07。ポーレットとれいな.txt.toml` — md5 `024224f6c52fa78e6dbec6b5f66ba881`, không có bản sao trùng.
- **Nguồn:** CSV3 bộ `03_Paulette` (385 dòng, khớp TOML 384/385; bộ `00_Common` là bộ cũ, chỉ khớp 15/385 — không dùng). Số dòng thật 385, không phải 770.
- **Kết quả: 19/385 dòng sai (4,9%)** — file sạch thứ tư của dự án (sau 実りの秋 0,4%, ヒヤリング 2,0%, 共通03 4,4%).
- **Phân loại:** thuật ngữ 6 (1791 gloss 枕木 'tàu vẹt', 2254 tag bịa 運転体 + 整備体 'thân chính', 2262 帝鉄, 2388 整備ボディ 'thân chính', 2558 tag bịa 整備体 + 'thân chính', 2658 Ohimitera), xưng hô 4 (2138, 2177, 2404, 2624 — Soutetsu gọi Hachiroku/Reina là 'cô' thay vì 'em'), sai nghĩa 4 (2154 câu cụt theo TW, 2393 JP thắng TW, 2534 lời hô 喚呼, 2591 lặp lại cách đọc 'Toumen?'), rên っ 2 (2676, 2677 — sweep lost-gasp-whole), nhỏ 3 (2098 thiếu 1 lần lặp, 2329 thiếu dấu phẩy, 2966 tự thêm ngoặc).
- **Cấu trúc:** 0 lệch dòng, 0 chuỗi xoay, 0 tràn chương, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key, 0 dòng uncertain.
- **Second pass:** 19 tổng / 19 kiểm tra lại / 0 loại bỏ / 0 sửa.
- **Khối TOML:** 19 key, parse-verified, 0 lệch giá trị so với JSON.
- **Ghi chú:** キルクイティウム thống nhất "Quirquitium" 5/5 trong file; "Circuithium" ở 日々姫10 key 2458 là vấn đề thống nhất liên file (docs chưa quyết). CSV==TOML 0 lệch thật (2677 chỉ là lỗi chuẩn hoá `\n` của script so sánh). 'cô' cho Navi (2449) giữ theo quy ước; "Mình" ở 3348 giữ theo ngoại lệ độc thoại nội tâm; 2214 giữ "Soutetsu" trần giữa câu (JP bare ソウテツ đang lắp bắp đọc tên, không phải cách gọi).
- **Tổng mới: 47 files / 2.779 dòng sai** (từ base 46 files / 2.760 + 19). Lưu ý: một audit song song (00_Common file 02) đang chạy — khi merge, cộng thêm số của file 02 vào tổng này.
