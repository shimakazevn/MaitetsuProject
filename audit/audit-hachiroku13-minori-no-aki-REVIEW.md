# Audit: Hachiroku 13_実りの秋 — 2 dòng Việt sai (đã đối chiếu JP + TW)

File: `01_Hachiroku/ハチロク13_実りの秋.txt.toml` — 474 dòng script, **2 dòng Việt sai = 0,4%**.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file sạch nhất trong 6 file đã audit toàn bộ tới nay: 廃炭鉱 31%, Grand 01 45,6%, 夜の嵐 44,9%, obasan 56%, Hibiki 03 86,2% — và 実りの秋 chỉ sai 0,4%. Hai file cùng mang số chương 13 nhưng chất lượng bản dịch trái ngược nhau hoàn toàn: 夜の嵐 199/443 sai, 実りの秋 chỉ 2/474 sai.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 474/474 dòng script** (key 97–3081, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn. Không ngoại suy tổng dự án từ file này.
- Phân loại 2 dòng sai: **lệch nội dung (sai nghĩa) 2**, **chưa dịch (còn nguyên tiếng Trung trong TOML) 0**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 0**. Không có dòng nào mang tiếng Trung (VN==TW = 0 trong cả CSV lẫn TOML).
- Thoại sai 1/274 (0,4%); lời dẫn (monologue) sai 1/200 (0,5%). Theo người nói: monologue 1/201, Soutetsu 1/81, Olivy 0/74, Hachiroku 0/38, Hibiki 0/37, Niiroku 0/31, Nagi 0/12.
- **Không có key-shift sạch (không cần thiết):** độ khớp thoại/dẫn ở shift 0 là 0,998 — gần như tuyệt đối; heuristic thoại/dẫn báo 1/474 (0,2%). File này gần như không bị xáo trộn cột Việt.
- **TOML và CSV giống hệt nhau về nội dung:** 280/474 dòng khác nhau chỉ ở `\n`/khoảng trắng, 0 dòng khác nội dung thực. Không có dòng CSV trống nào trong file này. Không có key trùng (File, Section, Key) trong CSV3 ở file này; chỉ có 3 giá trị Việt lặp lại và đều là câu ngắn lặp lại hợp lệ trong JP gốc ("Vậy sao." ×3, "Đã rõ." ×2, "(Phập) (Phập)" ×3).
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung.

## Hai dòng sai (cùng một lỗi nghĩa)
Cả hai dòng đều dịch 隆起 (mặt đất phình lên / đội lên) thành "sụt lún" (mặt đất sụt xuống) — ngược nghĩa hoàn toàn. Các dòng khác nhắc tới 隆起 trong cùng file đều dịch đúng là "phình lên" (1343, 1754, 1826, 1936, 2115, 3022), nên đây là hai lỗi lẻ, không phải do thuật ngữ sai hệ thống:
- **1721** (Soutetsu): JP 「隆起現場を見ておきたいのか」 — VN cũ "Cô muốn đến xem hiện trường sụt lún sao." → sửa: "Cô muốn đến xem hiện trường phình lên sao."
- **2492** (monologue): JP 「ナビに頼んで隆起現場に急ぎ向かえば」 — VN cũ "Nhờ Navi đưa vội đến hiện trường sụt lún" → sửa: "Nhờ Navi đưa vội đến hiện trường phình lên, thì thấy Olivy đang đứng thẫn thờ ở đó."

## Kết luận về cơ chế lỗi
- Không có cơ chế xáo trộn nào trong file này: không trùng lặp sai, không lệch vị trí, không câu Việt từ chương khác. Hai lỗi trên là lỗi dịch sai nghĩa đơn lẻ của một từ chuyên môn (隆起), có thể do nhầm với từ "sụt lún" trong lúc dịch. File này chứng minh không phải mọi file Hachiroku 13 đều hỏng — lỗi tập trung theo từng file, không theo route.
- 472 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Thuật ngữ đã dùng / ghi nhận trong file (theo docs + các dòng đúng sẵn có)
- 隆起 = "phình lên" (nhất quán trong toàn file: 1343, 1754, 1826, 1936, 2115, 3022 — hai dòng sai là ngoại lệ duy nhất).
- 御一夜鉄道 = "Đường sắt Ohito" (1694, 2535); 御一夜駅 = "ga suối nước nóng Ohitoyo" (2278, 2792); 御一夜 (địa danh) = "Ohitoyo" (2102, 2874) — **lưu ý: furigana trong chính file này ở 2102 ghi 御一夜 là おひとよ ("Ohitoyo"), trong khi docs quy thành phố là "Ohimitera" — xem đề xuất 1 bên dưới**.
- 湯医 = "Yui" (2102, furigana ゆのい) — **trái với bản sửa "Yunoi" ở file 夜の嵐, xem đề xuất 2**.
- 帝鉄 = "Teitetsu" dạng ngắn (1751, 1980) — **trái với docs "Đường sắt Hoàng gia (Teitetsu)", xem đề xuất 3**.
- ビーター = "cuốc chim" (theo TW 道鎬, 2217, 2566, 2581); 絶気 = "cắt hơi" (2212, theo TW "vô hơi"); 喚呼 = "hô xác nhận" (2828); 前進フルギア = "cài hết số tiến" (2078); 保線 = "bảo trì đường ray"; バラスト = "đá ba-lát"; 枕木 = "tà vẹt đường ray".
- Olivy xưng "Olivy" (ngôi thứ ba), gọi Soutetsu là "Soutetsu"; Niiroku nói ngắt quãng, câu ngắn; Soutetsu độc thoại xưng "Tôi".

## Dòng không chắc chắn (0 dòng)
- Không có dòng nào JP/TW mâu thuẫn nhau hay lửng tới mức không dịch được trong file này.

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **御一夜 — "Ohitoyo" hay "Ohimitera" (và "Ohito" cho 御一夜鉄道):** file này dùng "Ohitoyo" cho ga/địa danh và "Ohito" cho đường sắt một cách nhất quán, và furigana trong chính file (2102: 御一夜 = おひとよ) ủng hộ "Ohitoyo". Trong khi đó docs quy thành phố là "Ohimitera". Ba dạng đang cùng tồn tại trong dự án; Hieu chốt một dạng thì mình sẽ chuẩn hoá toàn bộ theo.
2. **湯医 — "Yui" hay "Yunoi":** file này dùng "Yui" (2102, dù furigana là ゆのい), còn bản sửa file 夜の嵐 dùng "Yunoi" theo đề xuất từ Grand 01. Hieu chốt một dạng cho toàn dự án.
3. **帝鉄 — "Teitetsu" dạng ngắn hay "Đường sắt Hoàng gia (Teitetsu)":** file này dùng "Teitetsu" (1751, 1980), giống dòng đúng duy nhất ở Grand 01 (3061). Quyết định cũ vẫn đang chờ Hieu.

## Giới hạn của audit này
- Đã đọc hết 474 dòng script của file này: 2 dòng sai đã xác nhận, 472 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra sai nghĩa tinh tế" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: parse được bằng tomllib, **2/2 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1721 = "「Cô muốn đến xem hiện trường phình lên sao.」"
2492 = "Nhờ Navi đưa vội đến hiện trường phình lên, thì thấy Olivy đang đứng thẫn thờ ở đó."
```

## Kết bài
実りの秋 là file thứ sáu được audit toàn bộ, và là file sạch nhất từ trước tới nay: chỉ 2/474 dòng sai (0,4%), cả hai cùng một lỗi nghĩa duy nhất (隆起 dịch thành "sụt lún" thay vì "phình lên") và đã sửa xong trong khối TOML 2 dòng bên trên, kiểm tra parse 2/2. File này chứng minh lỗi không lan đều theo route hay theo số chương — hai file cùng là Hachiroku 13 mà một file sai 44,9%, một file gần như sạch — nên không thể đoán chất lượng một file chưa audit từ file bên cạnh nó, chỉ có đọc từng dòng mới biết.

Việc còn lại của riêng file này chỉ là áp dụng 2 dòng sửa rồi chơi thử chương để nghiệm thu. Còn về tổng thể dự án, sáu file đã audit xong đã có 133 + 255 + 299 + 374 + 199 + 2 = 1.262 dòng sai, và ba quyết định thuật ngữ (御一夜, 湯医, 帝鉄) vẫn đang chờ Hieu chốt — file này còn bổ sung thêm bằng chứng furigana (御一夜 = おひとよ) cho quyết định đó. Bước tiếp theo hợp lý nhất là audit Nagi_Fukami 08a, và đưa Hachiroku 12 vào danh sách sau đó vì phát hiện tràn chương ở file 夜の嵐.
