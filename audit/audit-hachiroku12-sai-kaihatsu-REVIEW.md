# Audit: Hachiroku 12_再開発 — 19 dòng Việt sai (đã đối chiếu JP + TW)

File: `01_Hachiroku/ハチロク12_再開発.txt.toml` — 427 dòng script, **19 dòng Việt sai = 4,4%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 9 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3% — **file sạch thứ tư từ trước tới nay**, và là file gốc của 32 dòng Việt đã bị copy sang 夜の嵐.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 427/427 dòng script** (key 1612–3316, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 19 dòng sai: **lệch nội dung 8** (3195, 3021, 3285: hai loại thân máy bị gộp thành một; 3054: tên niên hiệu dịch sai; 2225: "Vé chuyên cơ"; 2258, 2381, 1699: 持株会社 dịch sai khái niệm), **chưa dịch (còn nguyên tiếng Trung trong TOML) 0**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 0**. 11 dòng còn lại là lỗi nhỏ: **nhất quán thuật ngữ 7** (2016, 2280, 2098, 3070, 2500, 2515, 2508: "Jutsusen" thiếu gạch nối), **dấu câu 3** (2103, 2537: mất tiếng hít っ; 1660: mất ngoặc ngoài 「」), **xưng hô độc thoại 1** (3290: "mình" trái quy ước "Tôi"). Không có dòng nào mang tiếng Trung (VN==TW = 0 sau khi loại trừ 1662 là 「…………」 — giống hệt nhau ở cả ba thứ tiếng, không phải chưa dịch).
- Thoại sai 13/249 (5,2%); lời dẫn (monologue) sai 6/178 (3,4%). Theo người nói: monologue 6, Soutetsu 5, Hachiroku 4, Kisaki 2, Paulette 2; Hibiki 0/12, Nagi 0/10, Reina 0/3, Fukami 0/5.
- **Heuristic thoại/dẫn bắt được 1/427:** đúng 1 dòng lệch loại là 1660 (thoại mất ngoặc ngoài) — và đó là lỗi thật, đã nằm trong 19 dòng sai. Heuristic không thấy 18 lỗi còn lại. Ngoài ra heuristic báo 1 dòng VN==TW (1662) nhưng đó là dương tính giả (「…………」); 2 giá trị Việt trùng nhau thì một cặp là lỗi thật (「!」 ở 2103/2537 — cả hai đều mất っ), cặp còn lại benign (「Ồ.」 2088/2125 — JP đều là 「ほう」). Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** không có dòng lệch vị trí nào trong file (0 cặp chuyển chỗ), nên không có gì để đo shift — lỗi xác nhận bằng đọc ngữ nghĩa từng dòng.
- **TOML và CSV giống hệt nhau về nội dung:** 237/427 dòng khác nhau chỉ ở `\n`/khoảng trắng, 0 dòng khác nội dung thực. Không có dòng CSV trống nào trong file này.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng (không chèn `\n` thủ công).
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có thẻ nào bị mất, lệch hay hỏng trong file này (kiểm tra bằng máy: mọi thẻ trong bản Việt đều khớp dạng `\x%l<JP>;#00ffc040;<gloss>%l;#;`, không có `[ruby]` sót trong bản Việt). Hai chỗ dùng thẻ đúng cần ghi nhận: 整備体/運転ボディ (xem mục A) và 大詔 (3054).

## Kết luận về cơ chế lỗi
- File này **không bị xáo trộn cột Việt**: không có dòng nào mang câu Việt của dòng khác (0 cặp chuyển chỗ trong file), không có dòng "mồ côi" (mọi câu Việt đều có JP/TW tương ứng), không có dòng trùng lặp sai (2 giá trị Việt trùng nhau: 「!」2103/2537 — cả hai đều là bản dịch thiếu của cùng một câu JP 「っ！」, không phải câu của dòng khác; 「Ồ.」2088/2125 — JP đều là 「ほう」).
- **File này là NGUỒN của lỗi tràn chương ở 夜の嵐, không phải nạn nhân:** kiểm tra toàn dự án cho thấy 45 dòng Việt trong file trùng với file khác, trong đó **32 dòng trùng với 夜の嵐** — đúng 32 cặp mà audit 夜の嵐 đã phát hiện (ví dụ: key 3207 của file này = bản dịch đúng, bị copy sang 夜の嵐 key 91; key 2281 = bản dịch đúng, bị copy sang 夜の嵐 key 1182). Cả 32 câu đều dịch đúng JP của chính chúng ở đây, nên **không có tràn ngược vào file này** — chiều tràn chỉ đi một chiều, từ Hachiroku 12 sang 夜の嵐. 13 dòng trùng còn lại đều là câu ngắn thông dụng (「Vâng, ngài Soutetsu.」, 「Ra là vậy.」, 「Ngài Soutetsu.」…) mà JP ở các file kia cũng tương đương — đều đúng.
- Lỗi còn lại tập trung thành nhóm có thể sửa hàng loạt: 3 dòng 持株会社 cùng một lỗi khái niệm, 7 dòng "Jutsusen" cùng một lỗi gạch nối, 2 dòng mất っ cùng một lỗi — cộng với 3 lỗi phân biệt thân máy (整備体/運転ボディ) và 2 lỗi từ đơn (大詔, 専用乗車券). JP và TW khớp nhau ở mọi dòng sai, nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại/chuẩn hoá từ JP/TW, không cần thêm nguồn nào khác.
- 408 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 19 dòng sai

### A. Sai nghĩa / sai thuật ngữ (8 dòng)
- **3195 + 3021** (monologue): JP 整備体 (thân bảo trì — thân máy dùng để bảo dưỡng) — bản Việt cũ dịch cả hai chỗ thành "thân chính". Vấn đề: "thân chính" cũng được dùng cho 運転ボディ ở 3285, tức hai loại thân máy khác nhau bị gộp thành một tên. Sửa: 整備体 → "thân bảo trì" (giữ nguyên thẻ `%l`).
- **3285** (monologue): JP 運転ボディ (thân vận hành — thân máy dùng để lái tàu) — bản Việt cũ cũng dịch thành "thân chính", đụng với 整備体 ở 3195/3021. Sửa: "thân vận hành" để phân biệt với "thân bảo trì".
- **3054** (monologue): JP 大詔時代 — 大詔 là cách viết hư cấu của 大正 (niên hiệu Taishō); TW xác nhận 大正時期. Bản Việt cũ "thời Đại Chiếu" chỉ phiên âm Hán-Việt của chữ hư cấu, không dịch ra tên niên hiệu. Sửa: "Taisho" (theo chuẩn đã dùng trong audit Hibiki 03: 大詔 = Taisho), giữ nguyên thẻ `%l`.
- **2225** (Hachiroku): JP 専用乗車券 (vé chuyên dụng — vé riêng cho tuyến này) — bản Việt cũ "Vé chuyên cơ" là sai hẳn: "chuyên cơ" nghĩa là máy bay chuyên dụng/máy bay riêng, không liên quan gì tới vé tàu. Sửa: "Vé chuyên dụng".
- **2258 + 2381 + 1699** (Kisaki, Soutetsu, Hachiroku): JP 持株会社 (công ty holding — công ty mẹ nắm cổ phần) — bản Việt cũ dịch cả ba chỗ thành "công ty cổ phần" (công ty cổ phần = joint-stock company, một hình thức công ty khác hẳn); TW 控股公司 xác nhận nghĩa holding. Sửa cả ba: "công ty holding".

### B. Nhất quán thuật ngữ (7 dòng — lỗi nhỏ)
- **2016, 2280, 2098, 3070, 2500, 2515, 2508:** 術仙炭鉱 viết thành "mỏ than Jutsusen" (không gạch nối) trong cả 7 chỗ. Chuẩn đã chốt ở audit 廃炭鉱 là "mỏ than Jutsu-sen"; file ムナカタ来訪 cũng dùng "Jutsu-sen" (1525, 2092, 2191). Sửa cả 7: "Jutsu-sen". (Riêng 2508 còn có 湯医 → "Yui" — quyết định đang chờ, giữ nguyên.)

### C. Dấu câu / xưng hô (4 dòng — lỗi nhỏ)
- **2103 + 2537** (Paulette, Soutetsu): JP đều là 「っ！」 (tiếng hít mạnh) — bản Việt cũ chỉ còn "「!」", mất hẳn tiếng っ. Đây là hai dòng duy nhất trong cả hai file Hachiroku 12 có JP là 「っ！」. Sửa cả hai: "「Ư!」".
- **1660** (Kisaki): JP là 「『そんなことをしたら、市が完全に割れてしまう』」 (thoại chứa một câu trích) — bản Việt cũ bỏ mất ngoặc ngoài 「」, chỉ còn 『…』. Đây là dòng duy nhất trong cả hai file có dạng JP 「『…』」. Sửa: khôi phục ngoặc ngoài.
- **3290** (monologue): JP （……今日は、随分と待たされる日だな） — bản Việt cũ "（……Hôm nay, mình bị bắt chờ hơi nhiều nhỉ.）" dùng "mình" làm chủ ngữ độc lập, trái quy ước của file (độc thoại Soutetsu xưng "Tôi" ở 75 dòng). Sửa: "tôi". (Các trường hợp "mình" khác trong file đều đúng nên KHÔNG sửa: "Tôi cảm thấy mình…" 2950 và "tôi chợt nghĩ có lẽ mình…" 3137 là cấu trúc "Tôi… mình…" chuẩn trong tiếng Việt; "một mình" 2868/3021 và "chính tay mình" 3269 là thành ngữ.)

## Các cặp trùng lặp / lệch vị trí đã xác nhận (0 cặp trong file; 32 cặp tràn sang file khác)
- **Trong file: 0 cặp.** Không dòng sai nào mang câu Việt đúng của một key khác trong file. Mọi bản sửa trong khối TOML đều dịch mới/chuẩn hoá từ JP/TW.
- **Tràn sang 夜の嵐 (32 cặp — file này là nguồn, KHÔNG phải nạn nhân):** 2970↔夜の嵐 2347, 2790↔2514, 2277↔1201, 2789↔2036, 2833↔2807, 2378↔2825, 2982↔2846, 2985↔2402, 2473↔2433, 2276↔1212, 2813↔2580, 2281↔1182, 2156↔1208, 3047↔2348, 3207↔91, 2085↔1214, 2079↔2344, 2236↔2624, 2108↔1551, 2965↔2455, 3040↔2532, 3148↔1527, 2347↔1661, 2428↔2323, 2198↔2690, 1991↔1773, 3117↔2019, 3043↔2266, 2338↔2875, 2863↔2697, 2967↔2252, 2375↔1538. Cả 32 câu đều dịch đúng JP của chúng tại key gốc ở file này; bản sửa cho 32 dòng sai bên 夜の嵐 đã nằm trong audit 夜の嵐, không lặp lại ở đây.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (75/178 dòng monologue có đại từ tôi; chỉ 1 dòng xưng "mình" ở vị trí chủ ngữ là 3290 — đã sửa); Soutetsu thoại xưng "tôi"; Hachiroku gọi Soutetsu là "ngài Soutetsu"; Kisaki xưng "Tôi"; Hibiki gọi Soutetsu là "Anh hai"; Nagi gọi Soutetsu là "Anh hai".
- 御一夜 → "Ohitoyo" nhất quán trong cả 8 lần xuất hiện (2926 "Công ty Đường sắt Ohitoyo", 2488, 2346, 2345, 1672, 2471, 2316, 2508) — **chưa chốt** (file ムナカタ来訪 dùng lẫn Ohito/Ohimitera/Ohitoyo; docs: thành phố "Ohimitera"); file này là bằng chứng mạnh nhất cho "Ohitoyo" vì dùng nhất quán và có furigana おひとよ ủng hộ.
- 湯医 → "Yui" trong cả 3 lần xuất hiện (2508, 2464, 2853) — **chưa chốt** (Grand 01 dùng "Yunoi" theo furigana ゆのい; 廃炭鉱 và file này dùng "Yui"); giữ nguyên trong khối sửa.
- 術仙炭鉱 = "mỏ than Jutsu-sen" (sau khi sửa 7 dòng; khớp chuẩn 廃炭鉱 và ムナカタ来訪). 整備体 = "thân bảo trì", 運転ボディ/運転体 = "thân vận hành" (phân biệt rõ hai loại thân máy — xem mục A). 大詔 = "Taisho". 持株会社 = "công ty holding". 専用乗車券 = "Vé chuyên dụng". コン không xuất hiện trong file này (1650 là コンマ trong "制動、コンマ８っ!" — "Hãm phanh, phẩy 8!" — dịch đúng, không liên quan tới tên コン). 冥軍 / 冥国 không xuất hiện. エアクラ = "Aircra" (2332: "công ty Aero-Craftech" — tên công ty, giữ nguyên).
- Còi tàu ポー không xuất hiện trong file này. Trailing "——っ" giữ nguyên theo sfx §3.

## Dòng không chắc chắn (0 dòng)
- Không có dòng nào JP và TW mâu thuẫn nhau, hay mơ hồ tới mức phải đoán, trong file này.

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **Phân biệt thân máy — 運転体/運転ボディ vs 整備体:** file này (và cả dự án) cần hai tên riêng: 運転体/運転ボディ → "thân vận hành", 整備体 → "thân bảo trì". Khối sửa đã dùng đúng hai tên này cho cả 3 dòng. Nếu Hieu chốt thì áp dụng cho toàn dự án (kiểm tra nhanh: các file khác có dùng "thân chính" cho cả hai loại không).
2. **湯医 — "Yui" hay "Yunoi":** file này dùng "Yui" ở cả 3 chỗ (2508, 2464, 2853), giống 廃炭鉱 và 実りの秋 (2102); Grand 01 và 夜の嵐 dùng "Yunoi" theo furigana ゆのい. Chưa chốt — đề xuất trước đó (chốt "Yunoi" toàn dự án) vẫn đang chờ Hieu.
3. **御一夜 — Ohito / Ohimitera / Ohitoyo:** file này dùng nhất quán "Ohitoyo" (8/8 dòng), trong khi file ムナカタ来訪 dùng lẫn cả ba dạng. Nếu Hieu chốt "Ohitoyo" thì chỉ cần sửa file ムナカタ来訪 (và vài chỗ lẻ khác), còn file này đã đúng sẵn.
4. **術仙炭鉱 — "Jutsu-sen" (có gạch nối):** khối sửa đã chuẩn hoá 7 dòng theo chuẩn 廃炭鉱. Audit 夜の嵐 trước đây ghi "Jutsusen" theo file — nếu Hieu chốt "Jutsu-sen" thì cả 夜の嵐 cũng cần sửa lại cho nhất quán.

## Giới hạn của audit này
- Đã đọc hết 427 dòng script của file này: 19 dòng sai đã xác nhận, 0 dòng chưa chắc chắn, 408 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- File này (4,4% sai) sạch thứ tư toàn dự án, sau 実りの秋 (0,4%), ムナカタ来訪 (2,3%) và 08a (4,3%). Tổng 9 file đã audit xong: 133 + 255 + 299 + 374 + 199 + 2 + 20 + 12 + 19 = **1.313 dòng sai**.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **19/19 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1660 = "「『Làm thế thì thành phố sẽ hoàn toàn bị chia rẽ mất.』」"
1699 = "「……Thúc đẩy việc tham gia công ty holding——Để làm được điều đó, cũng cần phải có những tài liệu mang tính thuyết phục đúng không ạ?」"
2016 = "「Cô muốn chúng tôi đưa đến ga bỏ hoang của mỏ than Jutsu-sen—— Nhưng trước tiên, tôi muốn biết lý do.」"
2098 = "「Hừm, chỉ đến ga bỏ hoang mỏ than Jutsu-sen thôi sao.」"
2103 = "「Ư!」"
2225 = "「Ngài thấy sao ạ? Vé chuyên dụng, đặc biệt dành tặng miễn phí cho ngài đấy nhé?」"
2258 = "「Đó là lý do tôi đề xuất thành lập công ty holding. Tất nhiên, tôi cũng muốn chi nhánh có thể cho vay với lãi suất thấp.」"
2280 = "「Nếu vậy thì——đoạn đường chạy thử trước mắt, sẽ là chặng khứ hồi đến ga bỏ hoang mỏ than Jutsu-sen đúng không ạ?」"
2381 = "「Thành lập công ty holding cùng các công ty đường sắt khác—— Cả về mặt vốn lẫn uy tín, đó là điều bắt buộc phải không.」"
2500 = "「Nếu vậy, sau khi dừng tàu tại ga mỏ than Jutsu-sen và kiểm tra xong các bộ phận, mọi người có thể khảo sát luôn nhà ga được không?」"
2508 = "「Nếu chỉ đến ga bỏ hoang mỏ than Jutsu-sen, thì nên chạy tiếp đến Yui rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」"
2515 = "「Có lẽ đây là minh chứng cho việc—— mỏ than Jutsu-sen từng một thời hưng thịnh.」"
2537 = "「Ư!」"
3021 = "Vừa mới chuyển sang \\x%l整備体;#00ffc040;thân bảo trì%l;#; và bước xuống buồng lái, Hachiroku lại một mình đi vào nhà ga bỏ hoang."
3054 = "Một nhà ga bằng gỗ, thạch cao và sắt. Đúng chuẩn hình ảnh nhà ga đường sắt thời xưa——thời \\x%l大詔;#00ffc040;Taisho%l;#;."
3070 = "Đoạn đường chạy thử nên được kéo dài dần dần, đến ga bỏ hoang mỏ than Jutsu-sen là vừa đẹp."
3195 = "Bước xuống sàn, Hachiroku chuyển \\x%lタブレット;#00ffc040;thẻ bảng%l;#; sang \\x%l整備体;#00ffc040;thân bảo trì%l;#;."
3285 = "Hachiroku trong thân vận hành, vừa làm điệu bộ phủi bụi, cuối cùng cũng bước ra khỏi nhà ga bỏ hoang."
3290 = "（……Hôm nay, tôi bị bắt chờ hơi nhiều nhỉ.）"
```

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Hachiroku 12_再開発 (nhớ quyết 4 đề xuất context ở trên trước, để khỏi sửa đi sửa lại), chơi thử chương rồi báo lại.
2. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).
3. Audit tiếp các file còn lại theo thứ tự nặng trước — mỗi file một bản review như file này. Gợi ý từ audit 夜の嵐 và danh sách heuristic: Paulette 04 (19 điểm heuristic).

## Kết bài
Hachiroku 12_再開発 là file thứ chín được audit toàn bộ, và là file có ý nghĩa đặc biệt: nó là **nguồn gốc của lỗi tràn chương** ở 夜の嵐 — 32 câu Việt của nó đã bị copy sang file chương sau, nhưng bản thân nó thì gần như nguyên vẹn (4,4% sai, 0 dòng lệch vị trí, 0 dòng chưa dịch, 0 dòng không chắc chắn). Cùng với file ムナカタ来訪 (2,3%), cả chương 12 đều sạch — trái hẳn với chương 13, nơi hai file cùng số chương lệch nhau một trời một vực (44,9% vs 0,4%). Bài học lặp lại lần nữa: không thể đoán độ sạch của một file từ tên chương, từ file bên cạnh, hay từ heuristic — chỉ có đọc hết từng dòng mới biết chắc.

Việc còn lại của riêng file này chỉ là áp dụng khối TOML 19 dòng và chơi thử chương để nghiệm thu (không có dòng nào chưa chắc chắn). Còn về tổng thể dự án, chín file đã audit xong đã có 1.313 dòng sai — và việc chương 12 sạch cả hai file cho thấy sau khi xong các file nặng trong danh sách, vẫn nên tiếp tục audit các file còn lại thay vì cho rằng phần còn lại đều ổn.
