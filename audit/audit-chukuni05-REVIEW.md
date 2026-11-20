# Audit — 仲国05_真夜中の餐車 (10_Chikuni)

- File: `10_Chikuni/仲国05_真夜中の餐車.txt.toml` — route Chikuni, cảnh nửa đêm trên tàu Z49: tiệc trà bí mật của Hachiroku và Suika trong toa ăn, Suika tâm sự chuyện tình cảm với Zhihuan và nỗi sợ mở "phong ấn" (シーリング), rồi phanh khẩn cấp, tàu dừng giữa dốc 14‰, cả đội bàn cách dùng độ rơ khớp nối (圧縮引出方) để khởi hành lại mà không đánh thức hành khách.
- Đọc: **467/467 dòng script** (key 1539–3316), đối chiếu từng dòng với JP + TW (CSV3). Không lấy mẫu.
- TOML md5: `fe04f16828477df45bf95ab529d47673`; **1 bản duy nhất, không trùng lặp**. CSV3 1 bộ 467 dòng, key khớp tuyệt đối 467/467, 0 ô VN trống.
- Lưu ý: 315 chênh lệch VN giữa TOML và CSV3 đều là kiểu đã biết — TOML làm phẳng `\n` thật thành khoảng trắng; CSV3 (literal `\n`) là chuẩn. Không có chênh lệch nội dung nào khác. 2 dòng VN == TW (1579, 1578) chỉ là dòng "…………" / "……………………", không phải chưa dịch.
- Cơ sở tổng cộng (đã kiểm chứng với ROUTE-AUDIT.md): **102 file / 4.846 dòng sai**.

## §1. Kết quả

**14 dòng sai / 467 dòng = 3,0%.** Không có chuỗi xoay vòng, không có dòng mồ côi, không có dòng chưa dịch, không có trùng key, không có tràn file khác.

Phân loại:

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 1 | 1605 |
| Gasp っ bị mất | 13 | 1562, 1946, 1947, 1972, 1982, 1983, 2071, 2365, 2375, 2376, 2378, 2874, 3158 |

Theo người nói: Soutetsu 6 (1562, 1947, 1982, 2071, 2376, 2378), Suika 4 (1946, 1972, 2365, 2375), monologue 2 (2874, 3158), Hachiroku 1 (1605), Zhihuan 1 (1983). Thoại 12, lời dẫn 2.

## §2. Chi tiết từng dòng sai

### Thuật ngữ (1 dòng)

- **1605 [ハチロク]** — JP 「……ですね。[このからだ,2]整備体でもわかりますから、決して小さくはない勾配です」/ TW 「……的確。即便是[這副身體,2]整備體我也能確定，而且這明顯不是個緩坡」/ Cũ: 「……Đúng vậy. Ngay cả với [cơ thể này] thân chính cũng có thể nhận ra,\nchắc chắn độ dốc không hề nhỏ.」 → **「……Đúng vậy. Ngay cả với [cơ thể này] thân bảo trì cũng có thể nhận ra,\nchắc chắn độ dốc không hề nhỏ.」** (整備体 = "thân bảo trì" theo thuật ngữ đã chốt; "thân chính" là lỗi đã gặp ở nhiều file trước — cf. ROUTE-AUDIT.md: file 08 có 6 dòng, file 09 có 1 dòng cùng lỗi này. Chỉ đổi đúng từ đó.)

### Gasp っ bị mất — sweep đã liệt kê, kiểm chứng đúng (10 dòng)

- **1947 [双鉄]** — JP 「っ！！？」/ TW 「哎！！？」/ Cũ: 「!!?」 → **「Ư!!?」**
- **1972 [西瓜]** — JP 「っ！！！」/ TW 「啊！！！」/ Cũ: 「!!!」 → **「Ư!!!」**
- **1982 [双鉄]** — JP 「っ！！」/ TW 「嗯！！」/ Cũ: 「!!」 → **「Ư!!」**
- **1983 [志寰]** — JP 「っ！！？」\n「だな。連結器も伸び切っていた――まずはそれを」/ TW 「嗯！！？」\n「是啊。車鉤也都是繃緊的——先從這裡著手吧」/ Cũ: 「!!?」\n「Đúng vậy. Khớp nối toa xe cũng đang bị kéo căng――trước hết là cái đó.」 → **「Ư!!?」\n「Đúng vậy. Khớp nối toa xe cũng đang bị kéo căng――trước hết là cái đó.」** (chỉ thêm Ư ở dòng đầu, giữ nguyên dòng sau)
- **2071 [双鉄]** — JP 「どうした？　――っ！\nまさか、旅疲れで異常発熱でも」/ TW 「怎麼啦？啊——！難道說是舟車勞頓，出現異常發熱了嗎」/ Cũ: 「Sao vậy? ――!\nKhông lẽ đi lại mệt mỏi quá nên phát sốt rồi.」 → **「Sao vậy? ――Ư!\nKhông lẽ đi lại mệt mỏi quá nên phát sốt rồi.」**
- **2365 [西瓜]** — JP 「双鉄先生が？　西瓜には――\nそのような足音は聞こえていな――っ！！？」/ TW 「雙鐵先生嗎？西瓜怎麼——沒聽到他的腳步——！！？」/ Cũ: 「Thầy Soutetsu sao? Suika――\nkhông hề nghe thấy tiếng bước chân nào như vậy――!!?」 → **「Thầy Soutetsu sao? Suika――\nkhông hề nghe thấy tiếng bước chân nào như vậy――Ư!!?」**
- **2375 [西瓜]** — JP 「っ！！！！！」/ TW 「！！！！！」/ Cũ: 「!!!!!」 → **「Ư!!!!!」**
- **2376 [双鉄]** — JP 「っ！！！？」/ TW 「！！！？」/ Cũ: 「!!!?」 → **「Ư!!!?」**
- **2874 [monologue]** — JP 「命令もだしておりませんのに、口から勝手に排気が漏れて、思いもかけぬ大きな音を響かせ――っ！」/ TW 「我明明沒有發出指令，嘴卻不由自主地長長排了一口氣，而且聲音還格外響亮——！」/ Cũ: 「Dù không hề ra lệnh, nhưng khí xả tự động lọt ra từ miệng tôi,\ntạo thành một tiếng động lớn không ngờ――!」 → **「Dù không hề ra lệnh, nhưng khí xả tự động lọt ra từ miệng tôi,\ntạo thành một tiếng động lớn không ngờ――Ư!」**
- **3158 [monologue]** — JP 「こくん、と西瓜が頷きます。\nですから、共感を開きま――っ！！！！！！」/ TW 「西瓜點了點頭。既然這樣，就開始共鳴——！！！！！！」/ Cũ: 「Suika khẽ gật đầu.\nVì vậy, tôi mở cộng cảm――!!!!!!!!!」 → **「Suika khẽ gật đầu.\nVì vậy, tôi mở cộng cảm――Ư!!!!!!!!!」** (giữ nguyên 9 dấu ! của VN cũ; JP có 7 dấu ! sau っ — số dấu ! là lựa chọn sẵn có của VN, không đổi)

### Gasp っ bị mất — sweep bỏ sót, audit tìm thêm (3 dòng)

- **1946 [西瓜]** — JP 「っ！！！？　なにかありましたか、ハチロク」/ TW 「哎！！！？怎麼啦，八六」/ Cũ: 「!!!? Có chuyện gì vậy, Hachiroku.」 → **「Ư!!!? Có chuyện gì vậy, Hachiroku.」** (っ đầu dòng + dấu câu, rồi mới tới lời thoại — mẫu sweep không liệt kê; cùng dạng với file 08 key 1490 「っ――」→「Ư――」 đã được audit trước đó tìm ra)
- **1562 [双鉄]** — JP 「っ――」/ TW 「——」/ Cũ: 「――」 → **「Ư――」** (cùng mẫu 1490 file 08; TW bỏ hẳn tiếng gasp nên không soi được từ TW)
- **2378 [双鉄]** — JP 「っ！！！？」「ふえっ！？」\n「なにごとですかっ！？」/ TW 「！！！？」「唔唉！？」\n「出什麼事了！？」/ Cũ: 「!!!?」「Uể!?」\n「Có chuyện gì vậy!?」 → **「Ư!!!?」「Phuê!?」\n「Có chuyện gì vậy!?」** (hai chỗ: っ đầu dòng bị mất → thêm Ư; ふえっ bị diễn thành "Uể" — theo quy tắc fa/fu đã chốt, ふぇ → "phuê". Dòng thứ ba なにごとですかっ là っ nhấn cuối câu, VN "Có chuyện gì vậy!?" đã đủ, không thêm Ư.)

## §3. Kiểm tra sweep っ cho file này

- `sweep-raw-gasp-wrong.json` có 10 mục cho file này, cả 10 đều kiểm chứng đúng với JP và được áp dụng: 1947, 1972, 1982, 1983, 2071, 2365, 2375, 2376, 2874, 3158.
- Lưu ý: 4 giá trị sweep (2071, 2365, 2874, 3158) đã làm phẳng dấu ngắt dòng `\n` của CSV3 thành khoảng trắng; audit đã khôi phục lại `\n` từ CSV3 để mỗi fix chỉ khác VN cũ đúng chỗ cần sửa (chèn Ư), theo quy tắc kiểm chứng diff.
- Audit tìm thêm 3 gasp sweep bỏ sót: 1946, 1562, 2378 (xem §2). Không có mục sweep nào khác.

## §4. Kiểm tra cấu trúc

- 0 dòng chưa dịch, 0 trùng key (467 key duy nhất), 0 dòng mồ côi (không có dòng VN nào không tìm được JP/TW tương ứng trong dự án), 0 chuỗi xoay vòng, 0 tràn file khác.
- Tag %l: số lượng `\x` JP = VN trên mọi dòng, 0 mất cân bằng mở/đóng; 0 dấu 「 」 lệch. Các annotation ruby [X,n] được xử lý theo quy ước của file (bỏ — xem §6).
- Không có dòng VN nào trùng nhau do lệch dòng, trừ 2 SFX khác nhau cùng diễn thành "(Phịch)": 3303 （とっ — bước chân đáp nhẹ) và 3280 （どさっ — Suika rơi từ giường xuống) — giữ nguyên, ghi chú nhỏ (xem §6).
- Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai):
  - **Soutetsu gọi Hachiroku là "em"** (1940 「Thấy em……không có trên giường」, 1994 「À, xin lỗi em」, 2723 「thì thầm 『Cảm ơn em』 bên tai」, và độc thoại "em ấy" ở 3056, 3079, 2883, 2638, 3193, 2634): đúng theo tiền lệ đã chốt — file 03 có 2 dòng Soutetsu gọi Hachiroku "cô"→"em" (2440, 2727), tiền lệ file 03 "em" 65 dòng (ROUTE-AUDIT.md). Không sửa.
  - **Ngáp ふぁ → "Oáp"** (1940 「やふぁひ、ほほふぁ。ふぁ――…」→「À, ừm. Oáp――…」, 1952 「ふぁぁあああああああ」→「Oápppppppppp」): đây là tiếng ngáp, diễn thành "Oáp" theo tiếng Việt là đúng; quy tắc ふぁ→"phà" áp cho SFX gasp/cười, không áp cho ngáp.
  - **仲国 → "Trung Quốc"** (2595 「だが仲国では」→「Nhưng ở Trung Quốc」, 2749 仲国語→"tiếng Trung", 2183 仲国国鉄→"Đường sắt Quốc gia Trung Quốc", 1577/2563 日ノ本語→"tiếng Hinomoto"): nhất quán toàn file; 仲国 là nước tương tự Trung Quốc trong truyện.
  - **シーリング → "Phong ấn"** (2019, 2021, 2023, 1573, 1894, 2267…): nhất quán toàn file, khớp TW 封印.
  - **Đông Phú 4 / Lưu Chí Hoàn**: 2140 東富4型→"Dongfu 4", 2370 劉志寰→"Lưu Chí Hoàn" — phiên âm Hán-Việt nhất quán.
  - **2798 よいしょ！ → "Ây da!"**: tiếng rặn khi bước lên bệ — "Ây da" dùng được cho cả gắng sức trong tiếng Việt; TW 欸咻 cũng là tiếng gắng sức. Giữ nguyên.
  - **1837 あっ → "A."**, **1969 あっ！/わっ！？/すごっ！ → "A!"/"Oa!?"/"Tuyệt quá!"**, **2382 （ふうっ）→"(Phù~)"**, **3291 （ぎしっ――ぎっ）→"(Cót――két)"**, **3289 （ばしゅーーっ）→"(Phụt――)"**, **3310 （ぐんっ！）→"(Khục!)"**: các thán từ/onomatopoeia đã được diễn, không mất âm.
  - **1995/3295 うふふっ → "Ufufu"**: tiếng cười được diễn thành tiếng cười, đúng quy tắc 22:05.
  - **2116** [ｗｏ－ｚｈｉ－ｄａｏ－ｌｅ,3]我知道了 → "Wo zhi dao le!" (giữ nguyên romaji tiếng Trung, bỏ ruby) và **2032** [あっしゅくひきだしほう,4]圧縮引出方 → "Phương pháp khởi hành nén": theo quy ước bỏ ruby của file (xem §6).
  - **2024** TW viết 右田先生 trong khi JP viết 双鉄先生 — JP thắng TW, VN "thầy Soutetsu" đúng.

## §5. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 14 fix đối chiếu JP lần 2: **14 tổng / 14 kiểm chứng lại / 0 bỏ / 0 sửa**. Không fix nào bị loại hay sửa lại ở lượt 2.

Kiểm chứng cơ học: JSON 14 mục dạng chuẩn (key dạng string, đủ jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; khối TOML 14 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô, kể cả `\n` literal); mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng: 11 chèn Ư, 1 thay "chính"→"bảo trì", 1 thay "Uể"→"Phuê" kèm chèn Ư, 1 chèn Ư giữ nguyên phần còn lại).

## §6. Chờ Hieu (không tính sai, không tự quyết)

1. **1956 [西瓜] 「あ――あ――あ――ああっ」** → VN hiện tại 「A――A――A――A.」: っ cuối tuyệt đối, không có dấu câu theo sau; sweep không liệt kê. Không rõ đây là gasp (nên thêm Ư → "A――A――A――AƯ.") hay っ nhấn cuối từ cảm thán (giữ nguyên). Cần Hieu chốt cách diễn cho dạng っ cuối tuyệt đối này.
2. **2254 [ハチロク] 「……これほどの――はうっ」** → VN hiện tại 「……mức độ này――ha.」: cùng dạng っ cuối thán từ như 1956 (はうっ là tiếng thở hắt bối rối). Giữ nguyên "ha" chờ quyết chung với 1956.
3. **Ruby [X,n] chưa thống nhất toàn dự án.** File này bỏ annotation ở 1605 [このからだ,2], 2963 [て,1], 2032 [あっしゅくひきだしほう,4], 2116 [ｗｏ－ｚｈｉ－ｄａｏ－ｌｅ,3] — đã ghi chú chờ quyết ở các file trước, giữ nguyên quy ước của file.
4. **1926 [日々姫] 「お尻から二両目」** → VN hiện tại 「toa thứ hai từ dưới đếm lên」: hơi khó hiểu ("từ dưới" có thể đọc thành "từ phía dưới"), cách diễn rõ hơn là "toa thứ hai tính từ cuối đoàn". Chỉ là vụng về nhẹ, không sai nghĩa rõ — giữ nguyên, ghi chú để Hieu quyết có muốn sửa trong đợt rà soát văn phong hay không.
5. **3303 （とっ） vs 3280 （どさっ） cùng là "(Phịch)"**: hai SFX khác trọng lượng (bước đáp nhẹ vs rơi mạnh) đang dùng chung một cách diễn. Giữ nguyên vì "(Phịch)" không sai hẳn cho cả hai, nhưng nếu Hieu muốn phân biệt thì 3303 có thể đổi thành "(Cộp)".

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1562 = "「Ư――」"
1605 = "「……Đúng vậy. Ngay cả với [cơ thể này] thân bảo trì cũng có thể nhận ra,\\nchắc chắn độ dốc không hề nhỏ.」"
1946 = "「Ư!!!? Có chuyện gì vậy, Hachiroku.」"
1947 = "「Ư!!?」"
1972 = "「Ư!!!」"
1982 = "「Ư!!」"
1983 = "「Ư!!?」\\n「Đúng vậy. Khớp nối toa xe cũng đang bị kéo căng――trước hết là cái đó.」"
2071 = "「Sao vậy? ――Ư!\\nKhông lẽ đi lại mệt mỏi quá nên phát sốt rồi.」"
2365 = "「Thầy Soutetsu sao? Suika――\\nkhông hề nghe thấy tiếng bước chân nào như vậy――Ư!!?」"
2375 = "「Ư!!!!!」"
2376 = "「Ư!!!?」"
2378 = "「Ư!!!?」「Phuê!?」\\n「Có chuyện gì vậy!?」"
2874 = "Dù không hề ra lệnh, nhưng khí xả tự động lọt ra từ miệng tôi,\\ntạo thành một tiếng động lớn không ngờ――Ư!"
3158 = "Suika khẽ gật đầu.\\nVì vậy, tôi mở cộng cảm――Ư!!!!!!!!!"
```

## Kết bài

File 仲国05_真夜中の餐車: đọc 467 dòng, sai 14 dòng (3,0%) — nhẹ hơn nhiều so với mức trung bình dự án (~10%), và là file sạch nhất trong nhóm Chikuni đã audit tới nay. Lỗi tập trung gần như toàn bộ ở gasp っ bị mất (13/14), trong đó 10 mục sweep đã liệt kê và 3 mục sweep bỏ sót do っ ở đầu dòng hoặc đi kèm SFX khác. Lỗi duy nhất ngoài gasp là thuật ngữ 整備体→"thân bảo trì" ở 1605, cùng mẫu lỗi đã gặp ở nhiều file trước. Không có lỗi hệ thống (xoay vòng, mồ côi, tràn file). 5 điểm chờ Hieu đã ghi ở §6, trong đó quan trọng nhất là cách diễn っ cuối tuyệt đối không dấu câu (1956, 2254).
