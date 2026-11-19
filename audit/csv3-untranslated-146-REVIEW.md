# CSV thứ 2 ("Trang tính 3") — đính chính: 146 dòng "chỉ có trong TOML" KHÔNG phải bản dịch

Ngày kiểm tra: 19/11/2026. Nguồn: `Matetsu Last Run - Trang tính3.csv` (91.731 dòng)
đối chiếu với `translation_toml-2.zip` (227 file, đã parse TOML sau khi bỏ BOM).

## Phát hiện — sửa lại kết luận trước đó

Kết luận cũ (08:42 ngày 19/11) nói: "chép 146 dòng đó từ TOML vào CSV trước,
kẻo mất bản dịch". **Kết luận đó sai.** Kiểm tra từng dòng trong 146 dòng:

- Cả **146/146** dòng, cột Việt trong TOML **giống hệt 100% cột Trung (TW)** —
  không phải bản dịch tiếng Việt.
- **0/146** dòng chứa bất kỳ chữ tiếng Việt có dấu nào (à, á, đ, ê, ơ, ư…).
- 138/146 là câu tiếng Trung đầy đủ (vd. Grand 01 key 2096:
  「他們以前就是那種脾氣…」); 8/146 còn lại là thán từ tiếng Trung ngắn
  (「是嗎」「嗯？」「啊……」「有道理」「效仿？」「為什麼」「拆走零件」「啊——」).

Tức là 146 dòng này trong TOML **chưa được dịch** — người dịch để nguyên câu
tiếng Trung vào ô Việt làm placeholder. "TOML dịch đầy đủ 0 dòng trống" chỉ
đúng về mặt ô có chữ, không đúng về mặt đã dịch.

## Phân bổ 146 dòng chưa dịch

| File | Số dòng |
|---|---|
| 09_Grand / グランドリライト01_オール御一夜、成立ならず.txt.toml | 100 |
| 02_Hibiki / 日々姫03_湯富院.txt.toml | 44 |
| lr真闇追加01_新婚旅行のリクエスト.txt.toml | 1 |
| lr真闇追加02_御一夜新婚旅行.txt.toml | 1 |
| **Tổng** | **146** |

## Hệ quả — đừng làm theo hướng cũ

1. **ĐỪNG chép 146 dòng này từ TOML vào CSV** với tư cách "bản dịch" — làm vậy
   chỉ là chép tiếng Trung vào cột Việt. Build patch từ đó sẽ hiện tiếng Trung
   trong game ở đúng 146 dòng này.
2. Việc đúng cần làm với 146 dòng này là **dịch mới từ Nhật/Trung sang Việt**
   (cột JP + TW trong CSV3 đã đủ để dịch, không cần thêm nguồn).
3. Cảnh báo cũ "build lại từ CSV sẽ xóa mất bản dịch" **không áp dụng cho 146
   dòng này** — vì chẳng có bản dịch nào để mất. (Cảnh báo đó đúng với file CSV
   CŨ và route Mayami; với CSV3 "Trang tính 3" thì Mayami đã đầy đủ.)

## Kiểm tra chéo — không phải lỗi đếm

- Trong CSV3, có 112 dòng mà VN == TW, nhưng 99/112 chỉ là dấu câu
  ("……", "——") và 13 dòng còn lại cũng toàn dấu câu/ký hiệu — tức là
  **không có dòng Việt nào khác trong CSV3 là tiếng Trung nguyên câu**.
  146 dòng trên là nhóm duy nhất mang câu Trung nguyên vẹn, và chúng chỉ tồn
  tại trong TOML, không có trong CSV3 (CSV3 để trống).
- Không có dòng Việt nào trùng lặp trong 146 dòng này (0 duplicate).

## File worklist đã chuẩn bị (CHƯA gửi cho Hieu, theo quy tắc không gửi file)

- `~/workspace/maitetsu-pilot/csv3-untranslated-146.csv` — 146 dòng, cùng 8 cột
  như CSV3, cột Vietnamese **để trống cố ý** để làm danh sách dịch, không phải
  để paste đè. Đã kiểm tra: 146/146 dòng khớp File/Section/Key với CSV3 và
  cột JP/TW giữ nguyên.

## Hibiki 03 (湯富院) — tín hiệu lệch rất nặng, nên audit tiếp theo

File này vừa có 44 dòng chưa dịch, vừa có tín hiệu lệch mạnh nhất trong các
file còn lại (đo bằng cùng phép check thoại/dẫn đã dùng cho Paulette 03):

| File | Dòng script | Thoại/dẫn lệch (heuristic) | VN trùng lặp |
|---|---|---|---|
| Paulette 03_廃炭鉱 (đã audit: 31% sai thật) | 430 | 63 | — |
| Paulette 03_obasan (đã audit: 56% sai thật) | 455 | 126 | — |
| **Hibiki 03_湯富院 (chưa audit)** | **434** | **183** (trong đó **159** dòng có VN mà vẫn lệch; 24 dòng trống VN có JP là thoại) | 12 giá trị trùng, 20 bản thừa — gồm 「Đã rõ。」 lặp **10 lần** |
| Grand 01 (chưa audit) | 655 | 176 (96 dòng có VN mà vẫn lệch; 80 dòng trống VN có JP là thoại) | 3 giá trị trùng |

Lưu ý: phép check này từng **đánh giá thấp** cả 2 file Paulette (63→133 dòng
sai thật; 126→255 dòng sai thật), nên 159 dòng lệch có VN của Hibiki 03 chỉ là
mức sàn — con số sai thật sau khi đọc hết file nhiều khả năng còn cao hơn.
Hibiki 03 cũng nằm trong route Hibiki, route có mật độ lỗi cao thứ hai toàn
dự án (71,0/1000 dòng, sau Nagi_Fukami 88,7/1000 — xem ROUTE-AUDIT.md).

## Đề xuất thứ tự tiếp theo (chờ Hieu chọn)

1. **Audit full Hibiki 03_湯富院** (434 dòng) — vừa là file lệch nặng nhất theo
   tín hiệu, vừa chứa 44/146 dòng chưa dịch, audit xong là dịch luôn được.
2. Sau đó dịch mới 146 dòng chưa dịch (Grand 01: 100, Hibiki 03: 44, +2 dòng lẻ),
   hoặc dịch 44 dòng của Hibiki 03 ngay trong lúc audit file đó.
3. Audit Grand 01 (655 dòng, 100 dòng chưa dịch + 176 dòng lệch heuristic).
4. Nagi_Fukami 08a vẫn còn trong danh sách — route Nagi_Fukami tệ nhất theo
   mật độ lỗi, nên vẫn là ứng viên sau Hibiki 03/Grand 01.
