# Audit: Paulette 07_うさぎ — 13 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 13/463 dòng sai (2,8%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. File sạch về cấu trúc, lỗi tập trung ở xưng hô và vài chỗ sai nghĩa. Đây là file Paulette 07 đầu tiên (cảnh Hikari đi chụp ảnh tàu với ba mẹ, gặp em bé Shou và gia đình).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 463 dòng script** (thoại 292, lời dẫn 171) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo 2 dòng: 2590 là dương tính giả (lời dẫn trích lời nói của Paulette nên có 「」 là đúng); 2776 là lỗi thật nhưng chỉ là lỗi nhỏ (thừa 「」). Heuristic bắt được 1/13 theo dòng, 0/13 theo đúng lý do.
- Không có key-shift sạch (shift −5..+5: shift 0 khớp 461/463 = 0,996; shift +3/+4 đạt 1,000 chỉ vì key thưa và phần lớn dòng là lời dẫn — không có ý nghĩa, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (218 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0.
- `[selections]` có tiêu đề nhưng rỗng (0 mục). Thẻ `%l`: 4 dòng có thẻ, không dòng nào lệch thẻ.
- Phân loại lỗi: xưng hô 6, sai nghĩa 4, thuật ngữ 2, lỗi nhỏ 1. Theo người nói: Soutetsu 6, lời dẫn 4, Hikari 2, bà mẹ trẻ 1; Paulette, Reina, em bé 0. Lỗi rải đều cả file (5 + 4 + 4 theo từng đoạn key).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có trùng lặp nội bộ sai — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục). Toàn bộ 13 lỗi đều là lỗi dịch tại chỗ: người dịch xưng hô không nhất quán (Soutetsu "anh"/"Mình" thay vì "Tôi"; Hikari tự xưng "chị"), hai chỗ dịch sai nghĩa/bịa thêm, hai thuật ngữ cũ "Ohimitera", một dấu ngoặc thừa. Đây là file "sạch" kiểu Paulette 06 — không phải file "rối" kiểu 廃炭鉱 hay 夜の嵐.

## Chi tiết 13 dòng sai

### A. Xưng hô — Soutetsu tự xưng "anh"/"Mình" thay vì "Tôi" (5 dòng) + độc thoại "mình" (1 dòng)

**1548 [双鉄]** — Soutetsu tự xưng "anh" khi nói với Hikari/Paulette; docs locations §2.1: Soutetsu xưng "Tôi", "Anh" chỉ khi nói với Hibiki. Trong file này Soutetsu chỉ có 1 lần xưng "tôi" trong thoại, 4 lần "anh" — "anh" là không nhất quán.

- JP: 「大丈夫だ。いつでも、どんなときだって、\n僕は、ポーレットの側にいる」
- TW: 「不用擔心。無論何時我都會陪在你身邊」
- Cũ: 「Không sao đâu. Dù là lúc nào, ở đâu,\nanh cũng sẽ luôn ở bên cạnh Paulette」
- Sửa: 「Không sao đâu. Dù là lúc nào, ở đâu, tôi cũng sẽ luôn ở bên cạnh Paulette」

**1690 [双鉄]** — Soutetsu nói thành tiếng (thoại, không phải độc thoại) mà tự xưng "Mình"; docs: Soutetsu xưng "Tôi" ("Anh" chỉ với Hibiki).

- JP: 「ああ……うたた寝をしてしまっていたのか」
- TW: 「啊……我不小心睡著了啊」
- Cũ: 「A…… Mình ngủ gật mất rồi à」
- Sửa: 「A…… Tôi ngủ gật mất rồi à」

**1884 [双鉄]** — Soutetsu tự xưng "Anh"; docs: "Tôi" ("Anh" chỉ với Hibiki). Người nghe ở đây là Paulette/Hikari.

- JP: 「わかった」
- TW: 「我明白了」
- Cũ: 「Anh hiểu rồi」
- Sửa: 「Tôi hiểu rồi」

**1887 [双鉄]** — Soutetsu tự xưng "Anh" với vợ mình (Paulette); docs: "Tôi" ("Anh" chỉ với Hibiki). Tiền lệ Paulette 06_雪の宿: 5 lần "anh" với Paulette đều đã tính sai.

- JP: 「かわいいな。僕の奥さんは――（ちゅっ）」
- TW: 「我老婆真是太可愛了（親）」
- Cũ: 「Đáng yêu quá. Vợ của anh——（Chụt）」
- Sửa: 「Đáng yêu quá. Vợ của tôi——（Chụt）」

**2096 [双鉄]** — Soutetsu tự xưng "anh" khi nói với Paulette về Hikari; docs: "Tôi".

- JP: 「重すぎて使えんだろうし、\n僕がひかりに指導できるのは、こいつの使い方だけだ」
- TW: 「那台太重了，小孩子沒辦法用。而且我也只能教光用這台」
- Cũ: 「Nặng quá con bé không dùng được đâu,\nvới lại, anh chỉ có thể hướng dẫn Hikari cách dùng cái máy này thôi」
- Sửa: 「Nặng quá con bé không dùng được đâu, với lại, tôi chỉ có thể hướng dẫn Hikari cách dùng cơ bản thôi」

**2536 [monologue]** — Độc thoại Soutetsu: chủ ngữ "mình" trong "cứ như mình biến thành…" là Soutetsu tự nói về mình; file này độc thoại Soutetsu dùng "Tôi" 57/64 chỗ có đại từ — "mình" ở đây là không nhất quán. (Các "mình" khác trong file là sở hữu cách/tân ngữ/thuộc về người khác — không tính sai.)

- JP: 小股、べた足でぺたぺたと。\nペンギンにでもなったような気持ちがしてくる。
- TW: 我邁著小碎步左右搖晃著身體走了起來。我覺得自己此刻活像一隻企鵝。
- Cũ: Bước nhỏ, bàn chân áp sát lạch bạch lạch bạch.\nCảm giác cứ như mình biến thành chim cánh cụt vậy.
- Sửa: 「Bước nhỏ, bàn chân áp sát lạch bạch lạch bạch. Cảm giác cứ như tôi biến thành chim cánh cụt vậy.」

### B. Sai nghĩa (4 dòng)

**1604 [ひかり]** — Người nói là Hikari (4 tuổi). JP 「あの――ね、みてた、の」: chủ ngữ là chính Hikari; bản cũ gán "chị" cho cô bé — Hikari không bao giờ tự xưng "chị". TW 「那個……有看到」 không có chủ ngữ, không cứu được.

- JP: 「あの――ね、みてた、の」
- TW: 「其實……光看見它了」
- Cũ: 「À thì—— này, chị có thấy, đó」
- Sửa: 「À thì—— này, Hikari có thấy, đó」

**1605 [ひかり]** — Cùng lỗi 1604: JP 「あの、ね？みてたの――ひかり、うさちゃん」 — Hikari nói về chính mình ("Hikari có thấy"), bản cũ "Chị có thấy" gán nhầm chủ ngữ. TW 「那個、那個？有看到喔——小光有看到、小兔兔」 xác nhận chủ ngữ là Hikari.

- JP: 「あの、ね？　みてたの――ひかり、うさちゃん」
- TW: 「其實，光有看到……看到小兔子」
- Cũ: 「À thì, này nhé? Chị có thấy——Hikari có thấy, bé thỏ đó」
- Sửa: 「À thì, này nhé? Hikari có thấy——Hikari có thấy bé thỏ đó」

**1841 [若い母親]** — JP 「しょうくん？おねえちゃんが」 chỉ là "Shou-kun? Chị này…" (câu bỏ lửng, mẹ giới thiệu Paulette với Shou). Bản cũ bịa thêm "đang gọi con kìa" — không có trong JP lẫn TW (TW: 「小翔，快看這位姐姐」).

- JP: 「しょうくん？　おねえちゃんが」
- TW: 「小翔，快看這位姐姐」
- Cũ: 「Shou-kun? Có chị đang gọi con kìa」
- Sửa: 「Shou-kun? Nhìn chị này nè」

**2611 [monologue]** — JP 「（そのままダイブ！)」 không có chủ ngữ/tân ngữ; TW 「然後撲進了媽媽的懷裡！」 — "lao vào lòng MẸ". Bản cũ "lòng họ" sai hẳn: "họ" là ai cũng không rõ, và không khớp TW. Người lao vào là Hikari (đang được Soutetsu đưa tay ra ở 2603), mẹ là Paulette.

- JP: そのままダイブ！
- TW: 然後撲進了媽媽的懷裡！
- Cũ: Rồi con bé lao thẳng vào lòng họ!
- Sửa: 「Rồi con bé lao thẳng vào lòng mẹ!」

### C. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (2 dòng)

**2115 [双鉄]** — 御一夜 = "Ohitoyo" (quyết định 19/11: furigana おひとよ + 8/8 "Ohitoyo" ở Hachiroku 12 再開発). Bản cũ "Ohimitera" là dạng cũ cần thống nhất.

- JP: 「御一夜まではまだまだだ。\n[こごた,2]小言田は……多分すぎていると思うが」
- TW: 「離御一夜還遠得很呢。我想，應該已經過了小牛田了」
- Cũ: 「Vẫn chưa đến Ohimitera đâu.\nChắc là…… vừa qua Kogota rồi」
- Sửa: 「Vẫn chưa đến Ohitoyo đâu. Chắc là…… vừa qua Kogota rồi」

**2380 [monologue]** — 御一夜鉄道 = "Đường sắt Ohitoyo" (quyết định 19/11). Bản cũ "Ohimitera".

- JP: それこそ産まれたときから見慣れまくっているせいか、\n御一夜鉄道の車両たちを、ひかりは撮ろうともしなかった。
- TW: 可能是因為從出生起光就見慣了御一夜鐵路的火車，在家裡的時候她並沒有表露出對拍照的興趣。
- Cũ: Có lẽ do đã quá quen mắt từ lúc mới sinh ra,\nnên Hikari chưa bao giờ có ý định chụp lại những toa xe của Đường sắt Ohimitera.
- Sửa: 「……nên Hikari chưa bao giờ có ý định chụp lại những toa xe của Đường sắt Ohitoyo.」

### D. Lỗi nhỏ (1 dòng)

**2776 [monologue]** — SFX trong ngoặc đơn ở lời dẫn, JP （ごとっ） TW （咚）. Bản cũ thêm 「」 bao ngoài thành 「（Cộc）」 — trong file này mọi SFX ngoặc đơn khác (2781–2787) đều không có 「」, nên đây là thừa dấu, không phải lỗi nghĩa.

- JP: （ごとっ）
- TW: （咚）
- Cũ: 「（Cộc）」
- Sửa: （Cộc）

## Các cặp trùng lặp / lệch vị trí đã xác nhận

**0 cặp.** Không có dòng nào bị lệch vị trí, không có chuỗi xoay vòng, không có dòng nào mang bản dịch của dòng khác (kiểm chứng bằng chỉ mục Việt toàn dự án). Các cặp trùng lặp nội bộ đều là câu cảm thán ngắn hợp lệ, JP gần như giống nhau, không tính lỗi:

- "「（Cộc）」" chỉ xuất hiện 1 lần (2776) — lỗi ở đây là thừa 「」, không phải trùng lặp.
- Các SFX "(Tách!…)" 2781–2787 mỗi dòng một dạng khác nhau, không trùng.

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)

- 御一夜 → "Ohitoyo" trong các bản sửa (quyết định 19/11; sau khi sửa file không còn "Ohimitera" nào; file này không có "Ohito", và đã có sẵn 1 "Ohitoyo" đúng ở 1907).
- 術仙炭鉱 = "mỏ than Jutsu-sen"; 湯医線 không xuất hiện trong file này; 帝鉄, 冥国, 冥軍, 小畑, 大畑, コン không xuất hiện.
- Soutetsu độc thoại = "Tôi" (57/64 chỗ có đại từ trong lời dẫn); Soutetsu thoại = "Tôi" (chỉ 1 lần "tôi" ở 1876, còn lại 4 lần "anh" đều đã sửa).
- Hikari tự xưng "Hikari" (ngôi thứ ba), không xưng "chị"/"em" khi nói về mình; gọi ba là "ba", gọi mẹ là "mẹ".
- Không có bản sao file này ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2).

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)

Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng. Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **13/13 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1548 = "「Không sao đâu. Dù là lúc nào, ở đâu, tôi cũng sẽ luôn ở bên cạnh Paulette」"
1604 = "「À thì—— này, Hikari có thấy, đó」"
1605 = "「À thì, này nhé? Hikari có thấy——Hikari có thấy bé thỏ đó」"
1690 = "「A…… Tôi ngủ gật mất rồi à」"
1841 = "「Shou-kun? Nhìn chị này nè」"
1884 = "「Tôi hiểu rồi」"
1887 = "「Đáng yêu quá. Vợ của tôi——（Chụt）」"
2096 = "「Nặng quá con bé không dùng được đâu, với lại, tôi chỉ có thể hướng dẫn Hikari cách dùng cơ bản thôi」"
2115 = "「Vẫn chưa đến Ohitoyo đâu. Chắc là…… vừa qua Kogota rồi」"
2380 = "「……nên Hikari chưa bao giờ có ý định chụp lại những toa xe của Đường sắt Ohitoyo.」"
2536 = "「Bước nhỏ, bàn chân áp sát lạch bạch lạch bạch. Cảm giác cứ như tôi biến thành chim cánh cụt vậy.」"
2611 = "「Rồi con bé lao thẳng vào lòng mẹ!」"
2776 = "（Cộc）"
```

## Việc tiếp theo

- Không có dòng nào chưa chắc chắn trong file này — mọi lỗi đều đã có bản sửa.
- Không có đề xuất cập nhật context mới từ file này: "Hikari" tự xưng theo ngôi thứ ba đã đúng với docs; "Ohimitera" → "Ohitoyo" là áp dụng quyết định đã có.
- Câu hỏi mở duy nhất còn treo từ các file trước vẫn chưa liên quan tới file này: Soutetsu gọi Paulette "cô" (ngữ cảnh công việc) hay "em" (ngữ cảnh gia đình) — trong file này Soutetsu không gọi Paulette bằng "cô"/"em" lần nào, nên không có thêm bằng chứng.

## Kết bài

File うさぎ là một file sạch về cấu trúc (0 lệch vị trí) với 13 lỗi nhỏ rải rác — nhẹ nhất trong các file Paulette đã audit trừ các file gần như không lỗi. Lỗi đáng chú ý nhất là 1604/1605: Hikari 4 tuổi tự xưng "chị" — người chơi sẽ thấy ngay vì giọng nói và lời thoại không khớp tuổi. Lỗi Soutetsu "anh" (4 dòng thoại + 1 độc thoại "mình") là cùng một kiểu lỗi hệ thống đã thấy ở Paulette 06_雪の宿, chỉ nhẹ hơn. Sau khi áp 13 bản sửa này, file coi như xong — không còn việc gì tồn đọng cho file này. File tiếp theo trong cùng chương là 支線 (đã audit cùng đợt, xem file riêng).
