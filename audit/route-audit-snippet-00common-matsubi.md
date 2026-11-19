## 00_Common file 末尾 — 共通末尾_ルート分岐.txt.toml (20/11/2026)

**0/3 dòng sai (0%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

- File rẽ nhánh route cuối Common: **chỉ 3 dòng, tất cả ở `[selections]`**, không có dòng `[script]` nào. TOML md5 `23c4c00fa9c23dcdf341575bf7864238`, BOM + CRLF, không trùng lặp.
- Cả 3 dòng lựa chọn đều dịch đúng (TW 「Xの意見を参考にする」 → "Tham khảo ý kiến của X": Hachiroku 103, Paulette 107, Hibiki 126). Không có thuật ngữ đã chốt, không đại từ, không tag %l, không っ, không bịa thêm.
- Sweep: 0 mục cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`). Nhiễm chéo: mỗi chuỗi VN chỉ xuất hiện đúng 1 lần trong toàn dự án, ở chính file này. CSV↔TOML khớp 3/3.
- Lượt soát 2: 0 tổng / 0 kiểm tra lại / 0 loại bỏ / 0 sửa lại.
- Ghi chú không tính lỗi: `[info] 122 = "回り始める動輪"` là tiêu đề của file 15 (metadata nhân bản, file 14/15 có `[info]` rỗng) — không ảnh hưởng game. Việc 3 lựa chọn hiện tiếng Trung trong game là vấn đề build đã được Hieu park từ 19/11, không phải lỗi dịch.
- Deliverables: `audit-00common-matsubi-REVIEW.md`, `audit-00common-matsubi-wrong.json` (0 mục). Khối TOML trong review đã kiểm chứng parse: 0 key, 0 sai lệch giá trị.
- Ohitoyo 00_Common: không đổi, còn lại **23** (15: 15, 01 pilot: 8 chưa chốt).
- Còn lại chưa kiểm toán trong 00_Common: 15 (đang chạy song song), 01 pilot (bản nháp 35/155, cần audit đầy đủ).

**Tổng cộng sau file này: 58 file / 3.260 dòng sai** (cơ sở 57 file / 3.260 + 0 file này).
