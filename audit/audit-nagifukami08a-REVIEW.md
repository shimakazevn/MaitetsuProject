# Audit: Nagi_Fukami 08a — 20 dòng Việt sai (đã đối chiếu JP + TW)

File: `07_Nagi_Fukami/凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml` — 462 dòng script, **20 dòng Việt sai = 4,3%**, 1 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 7 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4% — **08a là file sạch thứ hai từ trước tới nay** (chỉ sau 実りの秋), và là file đầu tiên **không có một dòng lệch vị trí / chưa dịch nào**.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 462/462 dòng script** (key 1183–2893, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn. Không ngoại suy tổng dự án từ file này.
- Phân loại 20 dòng sai: **lệch nội dung 0**, **chưa dịch (còn nguyên tiếng Trung trong TOML) 0**, **dịch thiếu (cụt câu) 0**, **không chắc chắn 1** (2426, xem dưới). 20 dòng sai gồm: **sai nghĩa 5** (1191, 1754, 1811, 1962, 1991), **câu gãy/khó hiểu 1** (1222), **xưng hô độc thoại không nhất quán 14** (xem "Lỗi xưng hô"). Không có dòng nào mang tiếng Trung (VN==TW = 0 trong cả CSV lẫn TOML).
- Thoại sai 5/259 (1,9%); lời dẫn (monologue) sai 15/203 (7,4%). Theo người nói: monologue 15, Fukami 2, Soutetsu 2, Nagi 1; Munakata, Hachiroku, Hibiki, Paulette, Reina, Mayami, Kisaki, Nakamura, Trọng tài, Loa phát thanh: 0 dòng sai.
- **Heuristic thoại/dẫn bắt được 0/462 (0%):** không có dòng nào JP thoại mà VN dẫn hay ngược lại — mọi lỗi trong file này đều cùng loại (thoại→thoại sai, dẫn→dẫn sai) hoặc ở mức đại từ/xưng hô, mà heuristic không thể thấy. Đây là bằng chứng rõ nhất từ trước tới nay rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** thử shift -5..+5 cho kết quả không kết luận được — key trong file thưa (462 dòng trên khoảng key 1183–2893) và thoại/dẫn đi theo cụm dài nên độ khớp loại ở mọi shift đều ~1,0. Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng, không dựa vào shift.
- **TOML và CSV giống hệt nhau về nội dung:** 268/462 dòng khác nhau chỉ ở `\n`/khoảng trắng, 0 dòng khác nội dung thực. Không có dòng CSV trống nào trong file này.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng (không chèn `\n` thủ công) theo đúng quyết định đó.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa. Ghi chú: file này được liệt kê là 1 trong 2 file có `[selections]` (file còn lại là Common 16, đã có 3 mục dịch sẵn), nhưng ở đây section chỉ là tiêu đề trống.
- **Thẻ `%l`:** 5 dòng mang thẻ `%l` cho 機関士 trong bản Việt (1207, 1542, 1750, 1804, 2568) mà JP gốc không có thẻ ở những vị trí đó — bản dịch vẫn đúng nghĩa, chỉ thêm thẻ tra cứu từ điển TIPS cho nhất quán với các chỗ khác. Ghi vào đây như một quan sát, KHÔNG tính là lỗi; nếu Hieu muốn giống hệt bản gốc thì gỡ 5 thẻ này. Không có thẻ `%l` nào bị mất hay lệch (kiểm tra bằng máy: mọi thẻ trong bản sửa đều khớp, không có `[ruby]` sót trong bản Việt).

## Kết luận về cơ chế lỗi
- File này **không bị xáo trộn cột Việt** như 6 file trước: không có dòng nào mang câu Việt của dòng khác (kiểm tra toàn dự án: cả 20 câu Việt sai chỉ xuất hiện ở đúng key của chúng, không trùng với bất kỳ key nào khác), không có dòng "mồ côi" (mọi câu Việt đều có JP/TW tương ứng, chỉ dịch chưa chuẩn), không có dòng trùng lặp sai (5 cặp Việt trùng nhau trong file đều là những câu cảm thán ngắn mà JP cũng giống hệt/na ná nhau: 「Nagi……」1578/1756, 「A――」1671/1864, 「Hả!?」1663/1703, 「Hửm?」1669/1702, （Xoạt! Xoạt! Xoạt!）2878/2883 — đều đúng).
- Không có bằng chứng tràn chương: không dòng Việt sai nào trùng với các file Nagi_Fukami lân cận (08b, 08c, 07, 09) hay bất kỳ file nào khác trong dự án. Kiểm tra tín hiệu tên nhân vật (tên trong bản Việt mà JP+TW không có) cho 0 dòng nghi ngờ; kiểm tra độ dài bất thường cũng sạch (chỉ 1 dòng dài bất thường là 2568, do 4 thẻ `%l`).
- Lỗi còn lại là lỗi dịch thuật lẻ tẻ ở mức câu/chữ, không phải lỗi hệ thống: 5 chỗ sai nghĩa, 1 câu gãy, 14 chỗ xưng hô độc thoại không nhất quán. JP và TW khớp nhau, nên mọi dòng sai đều sửa được chỉ bằng cách dịch lại/chuẩn hoá từ JP/TW, không cần thêm nguồn nào khác.
- 442 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 20 dòng sai

### A. Sai nghĩa (5 dòng)
- **1191** (monologue, Fukami): JP "……Mình không hề nhận ra. Nhưng vì được ví với Hachiroku-chan nên mình mới hiểu." — bản Việt cũ thêm chủ ngữ "anh ấy" không có trong JP/TW ("Nhờ anh ấy ví von với Hachiroku…"), đổi vai chủ động/bị động của câu. Sửa: bỏ "anh ấy", giữ dạng bị động theo JP.
- **1754** (Fukami): JP 「ごめんなさい――ごめんね、凪ちゃん。」/ TW 「對不起……對不起，小凪。」 — cả hai lời xin lỗi đều hướng về Nagi; bản Việt cũ thêm "anh" ("Xin lỗi anh――xin lỗi em nhé, Nagi") khiến câu đầu như đang xin lỗi Soutetsu. Sửa: bỏ "anh".
- **1811** (Soutetsu): JP 『危なっかしい』のひとことだ / TW "看著讓人擔心" — 危なっかしい = "khiến người ta phải lo lắng", không phải "nguy hiểm" theo nghĩa đen. Sửa: 『Đáng lo』.
- **1962** (Nagi): ngay sau lời cầu hôn của Soutetsu ở 1961 (「僕と――結婚してください」), Nagi đáp 「ありがと！　大好き！！！」 — bản Việt cũ "Cảm ơn chị! Em yêu chị nhất!!!" dùng đại từ "chị" sai người nghe (JP/TW không có địa chỉ nào; "chị" ở đây không thể là Soutetsu). Sửa: "Cảm ơn anh! Em yêu anh nhất!!!".
- **1991** (Soutetsu): cùng lỗi 危なっかしい như 1811 — JP "放っておけない、危なっかしい――だから僕は、いつでも凪を助けたい" / TW "看著讓人擔心，不能放著不管". Sửa: "Không thể bỏ mặc, đáng lo――nên lúc nào anh cũng muốn giúp đỡ Nagi."

### B. Câu gãy (1 dòng)
- **1222** (Fukami): JP 「――それ、なら」/ TW 「……這樣的話」 ("Nếu là như vậy thì…"). Bản Việt cũ "――Nếu, vậy." là mảnh câu gãy, đọc không thành câu. Sửa: "――Vậy thì."

### C. Lỗi xưng hô độc thoại không nhất quán (14 dòng)
- Quy ước trong chính file này (đếm bằng máy trên 203 dòng monologue): độc thoại của **Soutetsu (僕) xưng "Tôi"** (15/16 dòng có đại từ rõ ràng; chỉ 1 ngoại lệ là 2879), độc thoại của **Fukami (わたし/私) xưng "mình"** (43/49 dòng; chỉ 6 ngoại lệ). Độc thoại không ghi đại từ trong JP cũng tuân theo quy ước này theo mạch cảnh (xác định POV theo các dòng có đại từ xung quanh). 14 dòng dưới đây đi ngược quy ước của file — nghĩa vẫn đúng, chỉ cần chuẩn hoá xưng hô cho nhất quán giọng nhân vật (cùng cách xử lý như lỗi mình/tôi của Soutetsu ở bản pilot):
- **Fukami xưng "tôi" nhầm thành "mình" (13 dòng):** 1184 (mở đầu, mạch Fukami — 1195 gọi Soutetsu là "おにいさん"), 2284 (JP わたし), 2427 (mạch Fukami 2420–2432), 2586 (JP わたし), 2621 (Fukami đặt ngón tay lên môi hai người — xác nhận ở 2643, "ngón tay nỗ lực này" của Fukami), 2655 (JP わたし), 2782 (mạch Fukami 2781–2786), 2800 (mạch Fukami 2799), 2822 (mạch Fukami 2821–2827), 2826 (cùng mạch), 2848 (JP 私), 2852 (JP わたし), 2856 (JP わたし).
- **Soutetsu xưng "mình" nhầm thành "tôi" (1 dòng):** 2879 — JP （ああ――僕も）, bản Việt cũ "（A――mình cũng vậy）".

## Các cặp trùng lặp / lệch vị trí đã xác nhận (0 cặp)
- Không có cặp nào: không dòng sai nào mang câu Việt đúng của một key khác trong file hay ngoài file. Mọi bản sửa trong khối TOML đều dịch mới/chuẩn hoá từ JP/TW, không lấy lại từ key khác.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại/dẫn chuyện xưng "Tôi"; Fukami độc thoại xưng "mình" (chuẩn hoá theo 43/49 dòng đúng trong file); Nagi gọi Soutetsu là "Anh hai"; Fukami gọi Soutetsu là "Anh Soutetsu"; Hachiroku gọi Soutetsu là "Ngài Soutetsu"; Hibiki gọi Soutetsu là "Anh hai"; Paulette gọi Soutetsu là "Anh Soutetsu"; Mayami gọi Soutetsu là "Sou-chan", xưng "Chị"; Kisaki xưng "Tôi".
- 御一夜鉄道 = "Đường sắt Ohito" trong 3 dòng đúng sẵn có của file (1888, 2695, 2840) — **xem đề xuất bên dưới, chưa chốt**.
- 機関士 = "lái tàu" (giữ thẻ `%l` ở 5 dòng đã có thẻ); 気動車 = tàu diesel; レイルロオド = Railord; 8620 / D51 / 38696 giữ nguyên số hiệu; 千内 = Sendai (theo furigana せんだい, khớp Grand 01 dòng 2764); 御一夜市 = thành phố Ohimitera (theo docs); 熊本 = Kumamoto.
- Kiếm đạo: 面打ち = đánh mặt; 小手打ち = đánh tay; 正眼 = thế chánh nhãn; 右半開 = thế hữu bán khai; 残心 = tàn tâm (giữ nguyên cách gọi đã dùng trong file); 団体戦 = giải đồng đội; 個人戦 = giải cá nhân; 優勝決定戦 = trận chung kết quyết định ngôi vô địch.
- Còi tàu ポー không xuất hiện trong file này. Trailing "——っ" giữ nguyên theo sfx §3.

## Dòng không chắc chắn (1 dòng — cần Hieu xác nhận)
- **2426** (monologue, Fukami): JP 「例え、双鉄おにいさんの隣にいるのが、わたしじゃなくても――それでも、やっぱり。」 — câu JP bỏ lửng có chủ ý. TW hoàn thiện thành "即使在他身邊的人不是我也無妨" (dù không phải là mình cũng chẳng sao), bản Việt cũ hoàn thiện thành "thì mình vẫn mong như vậy" (mơ hồ, đọc không rõ "mong" cái gì). Dòng này KHÔNG nằm trong khối TOML (không đoán). Hieu chọn một trong hai cách hoàn thiện: (a) theo TW — "Dù cho người ở bên cạnh anh Soutetsu, không phải là mình――thì cũng chẳng sao."; (b) giữ ý "vẫn mong" nhưng viết rõ — ví dụ "thì mình vẫn mong được ở bên anh ấy." Ghi chú: các dòng xung quanh (2427–2432) đều là mạch Fukami nên "mình" là đúng.

## Đề xuất cập nhật context (để Hieu quyết, KHÔNG tự đổi toàn dự án)
1. **御一夜鉄道 — "Ohito" hay "Ohimitera" (và 御一夜: Ohitoyo/Ohimitera/Ohito):** file này có 3 dòng đúng dùng "Đường sắt Ohito" (1888, 2695, 2840), trong khi docs quy thành phố là "Ohimitera" và bản sửa Grand 01 dùng "Đường sắt Ohimitera". Không phát sinh bằng chứng mới cho 帝鉄, 湯医 hay コン trong file này (không xuất hiện). Quyết định cũ vẫn đang chờ Hieu, xem audit Grand 01 + Hachiroku 13.
2. **Xưng hô độc thoại Fukami — chốt "mình":** file này dùng "mình" cho độc thoại Fukami ở 43/49 dòng có đại từ rõ ràng; 14 dòng trong khối sửa đã chuẩn hoá theo đó. Nếu Hieu muốn Fukami độc thoại xưng "Tôi" như Soutetsu thì nói một tiếng — lúc đó sẽ phải đổi ngược lại 43 dòng đúng kia, nên cần chốt rõ trước khi áp dụng.

## Giới hạn của audit này
- Đã đọc hết 462 dòng script của file này: 20 dòng sai đã xác nhận, 1 dòng chưa chắc chắn (2426), 441 dòng còn lại khớp JP/TW.
- Vẫn có thể sót vài dòng "trông hợp lý nhưng thực ra là bản dịch của dòng khác" — cách chắc chắn nhất vẫn là chơi qua chương và đối chiếu voice. Nếu Hieu gặp thêm dòng nào nghi ngờ trong file này thì gửi mình, mình kiểm tra nốt.
- File này (4,3% sai) sạch hơn hẳn 5 file trước (31%–86,2%), chỉ kém 実りの秋 (0,4%). Tổng 7 file đã audit xong: 133 + 255 + 299 + 374 + 199 + 2 + 20 = **1.282 dòng sai**.

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **20/20 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa. Dòng 2426 (chưa chắc chắn) KHÔNG nằm trong khối này.

```toml
1184 = "――Mình cảm thấy đó là một điều vô cùng may mắn."
1191 = "……Mình không hề nhận ra. Nhưng nhờ được ví với Hachiroku nên mình mới hiểu."
1222 = "――Vậy thì."
1754 = "Xin lỗi――xin lỗi em nhé, Nagi. Chị――hơi thẫn thờ một chút."
1811 = "Nếu nói về tâm tư đối với Nagi thì―― Chỉ có một từ thôi, 『Đáng lo』."
1962 = "「Cảm ơn anh! Em yêu anh nhất!!!」"
1991 = "Đó là tâm tư của anh dành cho Nagi. Không thể bỏ mặc, đáng lo――nên lúc nào anh cũng muốn giúp đỡ Nagi."
2284 = "Nhưng, mình không thể thốt nên lời nào. Không chỉ mình, cả Nagi cũng vậy."
2427 = "Rằng Nagi sẽ thắng. Dù đã tin chắc như vậy, cơ thể mình vẫn run lên."
2586 = "Đôi mắt thẳng thắn ấy của Nagi, đã xóa tan đi sự do dự trong mình."
2621 = "Mình nhẹ nhàng đặt ngón trỏ lên môi Nagi. Rồi với cùng sự nhẹ nhàng ấy, đặt lên môi anh Soutetsu."
2655 = "Mình nhìn Nagi. Nagi cũng nhìn lại mình."
2782 = "Chỉ nghe vậy thôi là mình đã hiểu ngay. Dù sao thì đối thủ cũng là tuyển thủ Nakamura."
2800 = "Nhìn nụ cười ấy, mình chợt nghĩ."
2822 = "Bao nhiêu năm rồi―― Mình đã hy vọng và chờ đợi ngày này."
2826 = "Mình hoàn toàn bất ngờ. Cơ thể cứng đờ trong giây lát."
2848 = "Anh Soutetsu im lặng. Có lẽ anh ấy đang chờ đợi lời nói của Nagi, của mình."
2852 = "Anh Soutetsu nhìn mình."
2856 = "Cuối cùng anh Soutetsu cũng nhìn mình. Với ánh mắt có phần đờ đẫn."
2879 = "（A――tôi cũng vậy）"
```

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Nagi_Fukami 08a (nhớ quyết dòng 2426 và 2 đề xuất context ở trên trước, để khỏi sửa đi sửa lại), chơi thử chương Nagi_Fukami 08a rồi báo lại.
2. Audit tiếp các file còn lại theo thứ tự nặng trước: Hachiroku 12 (nghi tràn chương từ audit 夜の嵐), rồi các file còn lại trong danh sách heuristic — mỗi file một bản review như file này.
3. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).

## Kết bài
Nagi_Fukami 08a là file thứ bảy được audit toàn bộ, và là file đầu tiên không hề bị xáo trộn cột Việt: không một dòng lệch vị trí, không một dòng chưa dịch, không một dòng mồ côi hay tràn từ chương khác — 20 lỗi còn lại chỉ là những sai sót dịch thuật lẻ tẻ ở mức câu/chữ (5 chỗ sai nghĩa, 1 câu gãy, 14 chỗ xưng hô độc thoại không nhất quán giữa "tôi" và "mình"). Điều này cho thấy mức độ xáo trộn không đồng đều giữa các file: có file gần như nát toàn bộ như Hibiki 03 (86,2%), có file gần như nguyên vẹn như file này (4,3%) và 実りの秋 (0,4%) — nên không thể đoán độ sạch của một file từ tên chương hay heuristic, chỉ có đọc hết từng dòng mới biết chắc.

Việc còn lại của riêng file này chỉ là một dòng chưa chắc chắn (2426) và hai quyết định context đang chờ chung cho cả dự án (御一夜鉄道: Ohito/Ohimitera; xưng hô độc thoại Fukami: mình/Tôi); sau đó là áp dụng khối TOML 20 dòng và chơi thử chương để nghiệm thu. Còn về tổng thể dự án, bảy file đã audit xong đã có 1.282 dòng sai — và việc file này sạch cho thấy sau khi xong các file nặng trong danh sách, vẫn nên tiếp tục audit các file còn lại thay vì cho rằng phần còn lại đều ổn.
