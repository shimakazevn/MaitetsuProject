# Audit: 凪ふかみ07_分岐選択肢.txt.toml — 1/3 (33,3%)

- File: `07_Nagi_Fukami/凪ふかみ07_分岐選択肢.txt.toml` (route 07_Nagi_Fukami), 3 dòng — tất cả `[selections]`, `[script]` rỗng (không có thoại). File nhánh rẽ cuối cảnh 凪ふかみ07 (tiêu đề `[info]` "回り始める動輪"): Soutetsu ngập ngừng gọi Fukami / cả hai / Nagi.
- TOML md5 `36f17b848eff7c3c92106ec685609025`, không có bản trùng; UTF-8 BOM + CRLF, 237 byte. CSV3 1 bộ 3 dòng, key khớp tuyệt đối, VN khớp TOML 3/3, 0 dòng VN trống. Lưu ý: cột "JP Original" của CSV3 TRỐNG cho cả 3 dòng selections; cột TW giữ nguyên văn JP (「ふかみ……」/「ふたり、とも……」/「凪……」) nên dùng TW làm chứng cứ nguồn.
- Phân loại (1): sai nghĩa 1 (key 86: 「ふたり、とも……」 → VN cũ 「Cả hai, người……」 dịch thừa "người" và làm mất とも; sửa → 「Cả hai người……」).
- Sweep gasp: 0 mục cho file này (kiểm tra trực tiếp sweep-raw-gasp-wrong.json); không có っ trong file. Đại từ: không áp dụng (không có thoại).
- Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. 0 tag %l. Key 85 「Fukami……」 và 87 「Nagi……」 đúng.
- Kiểm chứng: JSON 1 mục dạng chuẩn, khóa chuỗi; khối TOML 1 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 1/1 (jp lấy từ cột TW do cột JP Original trống); fix chỉ khác VN cũ ở đúng chỗ cần sửa.
- Lượt soát 2: 1/1 tái kiểm chứng, 0 bỏ, 0 sửa.
- Chi tiết đầy đủ: `audit-nagifukami07-bunki-sentakushi-REVIEW.md`; danh sách sửa: `audit-nagifukami07-bunki-sentakushi-wrong.json` (1 mục).

**Tổng cộng sau file này: 218 file / 9.925 dòng sai** (cơ sở 217 file / 9.924 dòng sai + 1 file này)
