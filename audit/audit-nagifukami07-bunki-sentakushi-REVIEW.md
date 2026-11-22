# Audit: 凪ふかみ07_分岐選択肢.txt.toml — 1/3 (33,3%)

- File: `07_Nagi_Fukami/凪ふかみ07_分岐選択肢.txt.toml` (route 07_Nagi_Fukami), 3 dòng — tất cả đều là `[selections]`, không có dòng `[script]` nào.
- Nội dung: file nhánh rẽ cuối cảnh 凪ふかみ07 (tiêu đề cảnh `[info]` 107 = "回り始める動輪" — "Bánh xe chủ động bắt đầu quay"): Soutetsu ngập ngừng gọi tên — chọn Fukami, chọn cả hai, hay chọn Nagi.
- TOML md5 `36f17b848eff7c3c92106ec685609025`, không có bản trùng (duy nhất trong 227 file toml2); UTF-8 BOM + CRLF, 237 byte. Cấu trúc: `[info]` chỉ có tiêu đề JP (không dịch — đúng quy ước, metadata không phải dòng dịch), `[characters]` rỗng, `[character_subs]` rỗng, `[script]` RỖNG (xác nhận: không có dòng thoại nào trong file), `[selections]` 3 khóa 85/86/87.
- CSV3: 1 bộ duy nhất, 3 dòng `[selections]` (85/86/87), key khớp tuyệt đối với TOML, VN khớp TOML 3/3, 0 dòng VN trống. LƯU Ý: cột "JP Original" của CSV3 TRỐNG cho cả 3 dòng selections này (CSV không có JP cho các dòng lựa chọn); cột TW giữ nguyên văn JP (hiragana/kanji, không phải bản dịch tiếng Trung) nên TW được dùng làm chứng cứ nguồn: 「ふかみ……」/「ふたり、とも……」/「凪……」. Đây là thiếu sót của CSV, không phải lỗi dịch.
- Phân loại (1): sai nghĩa 1 (key 86).
- Sweep gasp: 0 mục cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`, 1.399 mục); không có っ trong file nên không có gasp nào bị sót.
- Đại từ: không áp dụng — không có thoại, không có đại từ xưng hô nào.
- Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. 0 tag %l trong file.
- Vấn đề selections hiển thị tiếng Trung trong game (đã park, brief): các lựa chọn đúng trong TOML thì không tính là lỗi dịch — key 86 ở đây SAI CHỮ trong TOML nên vẫn phải sửa; 2 lựa chọn còn lại đúng trong TOML, không flag thêm về hiển thị in-game.

## Chi tiết từng dòng sai

### Key 86 — [selections] — sai nghĩa (dịch thừa + mất nghĩa)
- JP (theo cột TW của CSV3, JP Original trống): 「ふたり、とも……」
- TW: 「ふたり、とも……」
- VN cũ: 「Cả hai, người……」
- VN mới: 「Cả hai người……」
- Lý do: ふたり = hai người; とも = cả hai/cùng nhau. VN cũ "Cả hai" đã dịch trọn ふたりとも, rồi thêm thừa "người" (lượng từ đã hàm chứa trong "cả hai") sau một dấu phẩy — vừa lặp nghĩa, vừa làm mất とも, vừa khiến câu thành mảnh vụn lủng lẳng "Cả hai, người……". Dấu phẩy chỉ là bắt chước dấu 、 trong JP nhưng phá vỡ cụm VN. Trong toàn dự án, ふたりとも luôn được dịch "Cả hai (người/đều…)" (vd. "Cả hai người đều khen Suzu đấy nhé?"). Sửa thành 「Cả hai người……」 — giữ dấu …… ngập ngừng của JP.
- Các dòng đúng (không sửa): key 85 「ふかみ……」 → 「Fukami……」 ✓; key 87 「凪……」 → 「Nagi……」 ✓ (tên đã chuẩn theo dự án).

## Khối TOML (đã parse kiểm chứng)

```toml
[selections]
86 = "「Cả hai người……」"
```

- Kiểm chứng: JSON 1 mục dạng chuẩn (key chuỗi); khối TOML 1 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 1/1 (jp lấy từ cột TW do cột JP Original của CSV3 trống — đã ghi rõ ở trên); fix chỉ khác VN cũ ở đúng chỗ cần sửa (bỏ dấu phẩy thừa + bỏ "người" thừa → "Cả hai người").
- Lượt soát 2: 1/1 tái kiểm chứng, 0 bỏ, 0 sửa. Fix đã đọc lại toàn bộ đối chiếu JP 「ふたり、とも……」: "Cả hai người" = ふたり + とも, "……" = …… — đủ nghĩa, không thêm không bớt.
- Chi tiết đầy đủ: `audit-nagifukami07-bunki-sentakushi-REVIEW.md`; danh sách sửa: `audit-nagifukami07-bunki-sentakushi-wrong.json` (1 mục).
- Cờ cho Hieu: không có. (Lưu ý duy nhất: cột JP Original của CSV3 trống cho các dòng selections — nếu sau này rebuild từ CSV thì các dòng lựa chọn cần lấy JP từ TW hoặc từ file gốc, không phải lỗi dịch.)

## Kết bài

File nhánh rẽ tí hon (3 lựa chọn, 0 thoại): 1/3 dòng sai — key 86 dịch thừa "người" và làm mất とも, sửa thành 「Cả hai người……」. Hai lựa chọn tên riêng đúng. Không có lỗi hệ thống nào khác (không lệch dòng, không nhiễm chéo, không trùng khóa, sweep gasp 0 mục). Cơ sở tổng đã kiểm chứng: 217 file / 9.924 dòng sai.
