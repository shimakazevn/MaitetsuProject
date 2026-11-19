# Audit 00_Common file 末尾 — 共通末尾_ルート分岐.txt.toml (20/11/2026)

**0/3 dòng sai (0%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

## §1. Thông tin file

- **File:** `00_Common/共通末尾_ルート分岐.txt.toml` — file rẽ nhánh route cuối Common.
- **Nguồn:** CSV3 (`Matetsu Last Run - Trang tính 3`), tập duy nhất dưới `00_Common` — **3 dòng, tất cả đều ở `[selections]`** (không có dòng `[script]` nào).
- **TOML-2:** md5 `23c4c00fa9c23dcdf341575bf7864238`, 281 byte, BOM + CRLF (15 CRLF, 0 LF-only), `[selections]` 3 key, `[script]` rỗng, `[characters]` và `[character_subs]` rỗng, **không trùng lặp** (md5 xuất hiện 1 lần trong 227 file TOML — không thuộc 11 nhóm trùng).
- **CSV↔TOML:** 3/3 khớp chính xác (giá trị VN trong CSV = giá trị trong TOML).
- **Phương pháp:** đọc từng dòng đối chiếu nguồn (TW — cột JP Original trống ở các dòng selections này; xem §3), kiểm tra sweep, tag %l, chỉ số VN toàn dự án, md5 trùng lặp.

## §2. Kết quả

**0/3 sai (0%).** Đây là file sạch nhất trong 00_Common — toàn bộ 3 dòng lựa chọn đều dịch đúng, không có lỗi nào thuộc bất kỳ loại nào: không thuật ngữ đã chốt (Ohitoyo/Teitetsu/Yunoi/まいてつ/市電/整備体/宮司/Migita đều không xuất hiện), không đại từ (không có ngôi thứ nhất/thứ hai trong nhãn lựa chọn), không tag %l, không っ, không bịa thêm.

## §3. Đọc từng dòng (lượt 1)

Cột JP Original trong CSV3 trống ở cả 3 dòng selections — nguồn đối chiếu là cột TW (bản Trung Quốc dịch trực tiếp từ câu Nhật gốc, dạng 「Xの意見を参考にする」). Cả 3 dòng có cùng một khuôn mẫu, chỉ khác tên nhân vật.

| Key | TW (nguồn) | VN cũ | Phán quyết |
|-----|-----------|-------|-----------|
| 103 | ハチロクの意見を参考にする | Tham khảo ý kiến của Hachiroku | **Đúng.** 「Xの意見を参考にする」 = "tham khảo ý kiến của X". Tên Hachiroku đúng chuẩn dự án. |
| 107 | ポーレットの意見を参考にする | Tham khảo ý kiến của Paulette | **Đúng.** Cùng khuôn mẫu; Paulette đúng chuẩn dự án. |
| 126 | 日々姫の意見を参考にする | Tham khảo ý kiến của Hibiki | **Đúng.** Cùng khuôn mẫu; Hibiki đúng chuẩn dự án (日々姫 = Hibiki). |

Không có dòng nào thêm nghĩa so với nguồn, không có tag %l tự thêm, không có từ bịa kiểu Gemini.

## §4. Các kiểm tra hệ thống

- **Sweep っ:** đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` (1.399 mục) — **0 mục cho file này**. Đúng như kỳ vọng: file không có dòng script nào và không chứa っ.
- **Tag %l:** 0 tag ở cả JP/TW/VN — không có tag thiếu, không có tag tự thêm, không có tag lỗi đóng.
- **Nhiễm chéo:** kiểm tra chỉ số VN toàn dự án — mỗi chuỗi VN trong 3 dòng chỉ xuất hiện **đúng 1 lần** trong toàn bộ 91.731 dòng CSV3, và đều ở chính file này (103/107/126). Không có nhiễm chéo.
- **Lệch dòng / chuỗi xoay:** không áp dụng được — file không có dòng script; 3 dòng selections mỗi dòng khớp đúng nguồn TW của nó, không có dòng nào bị hoán đổi.
- **Dòng chưa dịch:** 0 — cả 3 dòng đều có VN, VN ≠ TW.
- **Key trùng:** 0 — 3 key duy nhất (103, 107, 126).
- **Dòng mồ côi:** 0 — cả 3 VN đều có nguồn TW tương ứng.
- **Ohitoyo còn lại trong 00_Common:** không đổi, **23** (15: 15, 01 pilot: 8 chưa chốt) — file này không chứa Ohimitera.

## §5. Lượt soát 2

Đọc lại toàn bộ 3 giá trị fix đối chiếu nguồn: **tổng 0 / kiểm tra lại 0 / loại bỏ 0 / sửa lại 0** — không có fix nào để soát lại, vì lượt 1 không tìm ra lỗi nào. Kiểm tra cơ học kèm theo: JSON rỗng parse được, khối TOML rỗng parse được (0 key), CSV↔TOML khớp 3/3.

## §6. Ghi chú không tính vào lỗi (quan sát, không sửa)

1. **`[info]` mang tiêu đề của file 15.** TOML của file này có `[info] 122 = "回り始める動輪"` — đó là tiêu đề của file 15 (共通15_回り始める動輪), trong khi `[info]` của file 14 và 15 đều rỗng. Có vẻ file này được nhân bản từ mẫu của file 15 và `[info]` chưa được cập nhật. Đây là metadata, không phải dòng dịch, không ảnh hưởng tới text trong game — **không tính là lỗi, không sửa**. Ghi lại để lúc rebuild nhớ kiểm tra.
2. **Vấn đề hiển thị tiếng Trung trong game đã được Hieu PARK (19/11).** 3 dòng lựa chọn này đã dịch đúng trong TOML từ trước, nhưng trong game vẫn hiện tiếng Trung — Hieu đã quyết bỏ qua, tự sửa sau (nghi là build cũ hoặc trình chèn bỏ qua `[selections]`). Đây KHÔNG phải lỗi dịch, nên không tính vào 0/3 này; chỉ nhắc lại để khỏi nhầm là file chưa được kiểm toán.

## §7. Khối TOML (đã kiểm chứng parse)

Không có fix nào nên khối rỗng — đã kiểm chứng parse bằng tomllib: 0 key, 0 sai lệch.

```toml
[selections]
```

## Kết bài

File 末尾 là file nhỏ nhất và sạch nhất trong 00_Common: chỉ 3 dòng lựa chọn ở `[selections]`, không có dòng script nào, và cả 3 dòng đều dịch đúng — **0/3 sai (0%)**. Không có lỗi lệch dòng, không có nhiễm chéo, không có thuật ngữ hay đại từ nào cần sửa. Hai quan sát duy nhất đều nằm ngoài phạm vi dịch: `[info]` mang tiêu đề của file 15 (metadata nhân bản, không ảnh hưởng game), và việc 3 lựa chọn hiện tiếng Trung trong game là vấn đề build đã được Hieu park từ 19/11, không phải lỗi bản dịch.

Với file này, 00_Common chỉ còn file 15 đang kiểm toán và file 01 pilot (bản nháp 35/155) cần audit đầy đủ. Tổng cộng sau file này: **58 file / 3.260 dòng sai** (cơ sở 57 file / 3.260 + 0 file này).
