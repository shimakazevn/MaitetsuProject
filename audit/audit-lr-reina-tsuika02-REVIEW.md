# Audit — lrれいな追加02_花嫁修業の先生たち (04_Reina)

- File: `04_Reina/lrれいな追加02_花嫁修業の先生たち.txt.toml` — route Reina, buổi học "làm cô dâu": Mayami dạy nấu ăn (nikujaga, vị nhà Migita), Kisaki dạy trà đạo (ousu, seiza), Hibiki dạy cắm hoa (ikebana, Tự do hoa); Soutetsu + Reina là học viên.
- Đọc: **384/384 dòng script** (key 796–2185), đối chiếu từng dòng với JP + TW (CSV3). Không lấy mẫu. Nhân vật: monologue 110, れいな 92, 双鉄 56, 稀咲 45, 日々姫 43, 真闇 38.
- TOML md5: `d620b749cf8ff3d0db532c2b68a22295`; **1 bản duy nhất, không trùng lặp** (không có file trùng md5 trong toml2; file `lr...h_夜の花嫁修業` là file khác). CSV3 1 bộ duy nhất 384 dòng, key khớp tuyệt đối 384/384, 0 ô VN trống, 0 trùng key. `[selections]` rỗng. Không có thẻ `%l` nào trong file.
- 238 chênh lệch VN giữa TOML và CSV3 đều là kiểu đã biết — TOML-2 làm phẳng `\n` thành khoảng trắng; CSV3 (literal `\n`) là chuẩn. Không có chênh lệch nội dung nào khác.
- Cơ sở tổng cộng (đã kiểm chứng với ROUTE-AUDIT.md dòng cuối): **108 file / 5.009 dòng sai** — khớp đúng số parent giao.

## §1. Kết quả

**16 dòng sai / 384 dòng = 4,2%.** Thoại 14/274 (5,1%), độc thoại 2/110 (1,8%). Không có lệch vị trí, không có chuỗi xoay vòng, không có nhiễm chéo file khác, không có dòng mồ côi, không có dòng chưa dịch, không có trùng khóa.

Phân loại:

| Loại | Số dòng | Key |
|---|---|---|
| Đại từ | 5 | 1187, 1357, 1405, 1456, 1692 |
| SFX tiếng cười (うふふ → "Ư hư hư") | 6 | 1263, 1265, 1266, 1376, 1511, 2017 |
| Gasp っ (sweep) | 3 | 1339, 1363, 1885 |
| fa/fu | 1 | 1274 |
| SFX/discourse (っと) | 1 | 1655 |

## §2. Chi tiết từng dòng sai

### Đại từ — Soutetsu (5 dòng)

- **1187 [双鉄]** — JP 「いや、そのような謙遜は」 / TW 「不用這麼謙虛的」 / Cũ: 「Không, chị đừng khiêm tốn như vậy.」 → **「Không, cô đừng khiêm tốn như vậy.」** (Soutetsu đáp lại sự khiêm tốn của Kisaki ở 1183 ("いやいや、そこは関係しないと思うよ" — cô phủ nhận khiêm tốn) → người nghe là Kisaki; trong file này Soutetsu gọi Kisaki là "cô" nhất quán 5× (1428, 1438, 1518, 1659, 1697), "chị" là sai.)
- **1357 [双鉄]** — JP 「ああ、うむ。もちろん。面白そうだ。僕も大変に興味がある」 / TW 「嗯，當然了。感覺就很有趣，我也很有興趣」 / Cũ: 「À, ừm. Tất nhiên rồi.\nCó vẻ thú vị đấy. Anh cũng rất hứng thú.」 → **「À, ừm. Tất nhiên rồi.\nCó vẻ thú vị đấy. Tôi cũng rất hứng thú.」** (Soutetsu trả lời câu hỏi của Kisaki ở 1351 về thiết kế tài sản cho tương lai → người nghe là Kisaki → "tôi" theo quy tắc đã sửa.)
- **1405 [双鉄]** — JP 「真闇姉もよければなのだが。どんな話を二人でしたのか、僕にも聞かせてはくれないか」 / TW 「如果真闇姐不介意的話，能告訴我你們都說了什麼嗎」 / Cũ: 「Nếu chị Mayami cũng không phiền. Hai người đã nói chuyện gì vậy,\ncó thể cho anh nghe cùng được không.」 → **「Nếu chị Mayami cũng không phiền. Hai người đã nói chuyện gì vậy,\ncó thể cho tôi nghe cùng được không.」** (Người nghe là Mayami (真闇姉 gọi thẳng) → "tôi"; "chị Mayami" giữ nguyên.)
- **1456 [双鉄]** — JP 「知らなかった……塩分を増やす代わりに、味を濃くする、染みさせる……そのための工夫を、こんなにも――」 / TW 「我都不知道……還有不增加鹽分而提味噌香的辦法……原來為了做菜要花這麼多工夫……」 / Cũ: 「Anh không hề biết……Thay vì tăng lượng muối, chị lại làm cho vị đậm đà hơn,\nthấm hơn……Chị đã tốn bao nhiêu công sức để làm điều đó——」 → **「Tôi không hề biết……Thay vì tăng lượng muối, chị lại làm cho vị đậm đà hơn,\nthấm hơn……Chị đã tốn bao nhiêu công sức để làm điều đó——」** (Soutetsu nói với Mayami (cô đang giảng về nêm nếm món ninh) → "tôi"; "chị" = Mayami giữ nguyên.)
- **1692 [双鉄]** — JP 「生け花を通じ、生活そのものをデザインする――選び、整えることの大切さも、教えてもらえた気がする」 / TW 「這就是透過插花來設計自己的生活——我也明白了挑選、整理對於自己而言有多重要」 / Cũ: 「Thông qua nghệ thuật cắm hoa để thiết kế chính cuộc sống của mình——\nEm có cảm giác mình đã học được tầm quan trọng của việc lựa chọn và sắp xếp.」 → **「Thông qua nghệ thuật cắm hoa để thiết kế chính cuộc sống của mình——\nAnh có cảm giác mình đã học được tầm quan trọng của việc lựa chọn và sắp xếp.」** ("Em" không bao giờ là tự xưng của Soutetsu. Câu này nói về ikebana — giáo viên là Hibiki (dòng 1691 Mayami nói trước, 1692 Soutetsu cảm nhận về bài học cắm hoa) → "anh".)

### SFX tiếng cười — うふふ bị dịch thành tiếng rên (6 dòng, vi phạm quy tắc Hieu 22:05)

- **1263 [れいな]** — JP 「うふふぅ」 / TW 「呵呵」 / Cũ: 「Ư hư hư~」 → **「Ufufu~」** (Tiếng cười, không phải tiếng rên.)
- **1265 [れいな]** — JP 「うふふぅ。\n喜んでもらえて、れいなもとーってもうれしいですよぉ」 / TW 「呵呵，你開心玲奈也就開心了」 / Cũ: 「Ư hư hư~.\nThấy chị vui, Reina cũng vui lắ-ắm luôn nha~」 → **「Ufufu~.\nThấy chị vui, Reina cũng vui lắ-ắm luôn nha~」** (Chỉ sửa tiếng cười đầu dòng; nửa sau giữ nguyên — "chị" = Mayami, đúng.)
- **1266 [真闇]** — JP 「うふふっ、そぎゃんならなによりねぇ」 / TW 「呵呵，那可真是太好了」 / Cũ: 「Ư hư hư, vậy thì còn gì bằng nữa.」 → **「Ufufu, vậy thì còn gì bằng nữa.」**
- **1376 [れいな]** — JP 「うふふぅ、ですねぇ。きさきさんもひびきさんも、\nれいなとそうてつさんに色んなこと教えてくれましたぁ」 / TW 「嘿嘿，是啊。稀咲小姐和日日姬小姐都教了玲奈和雙鐵先生好多事情」 / Cũ: 「Ư hư hư, đúng vậy nha~. Cả cô Kisaki và chị Hibiki,\nđều đã dạy cho Reina và anh Soutetsu rất nhiều điều nha~」 → **「Ufufu~, đúng vậy nha~. Cả cô Kisaki và chị Hibiki,\nđều đã dạy cho Reina và anh Soutetsu rất nhiều điều nha~」**
- **1511 [れいな]** — JP 「こうですねぇ。――うふふぅ、\nほんとににゃんこのおててみたいですぅ」 / TW 「是這樣吧。呵呵，的確是跟貓咪的手一樣」 / Cũ: 「Thế này đúng không ạ~. ——Ư hư hư~,\ntrông giống bàn tay mèo thật đó nha~」 → **「Thế này đúng không ạ~. ——Ufufu~,\ntrông giống bàn tay mèo thật đó nha~」**
- **2017 [monologue]** — JP 「真闇姉がなにか囁いた瞬間に、\nれいながうふふうと笑いを零す。」 / TW 「真闇姐輕聲耳語之後，玲奈便禁不住笑了起來。」 / Cũ: 「Khoảnh khắc chị Mayami thì thầm điều gì đó,\nReina bật cười khúc khích ư hư hư.」 → **「Khoảnh khắc chị Mayami thì thầm điều gì đó,\nReina bật cười khúc khích ufufu.」** (Độc thoại: JP nói rõ Reina "cười khúc khích" (笑いを零す) — "ư hư hư" là tiếng rên, sai hẳn; "ufufu" giữ âm cười.)

### Gasp っ — sweep (3 dòng, nhận nguyên văn giá trị sweep)

- **1339 [双鉄]** — JP 「うむ。――っ！」 / TW 「嗯……啊！」 / Cũ: 「Ừm. ——っ!」 → **「Ừm. ——Ư!」** (Sweep raw-tsu: っ thô còn sót trong VN.)
- **1363 [双鉄]** — JP 「うむ？――っ！！！！！！」 / TW 「嗯？……啊！！！！！！」 / Cũ: 「Hửm?——っ!!!!!!」 → **「Hửm?——Ư!!!!!!」** (Sweep raw-tsu.)
- **1885 [monologue]** — JP 「指示通り三角形のローテーブルとソファをズラすと、\n稀咲はその間にテキパキと――っ！」 / TW 「我們依照稀咲的要求把三角矮桌和沙發挪走，而稀咲則趁這段時間一頓安排。」 / Cũ: 「Làm theo chỉ thị dời chiếc bàn trà hình tam giác và sofa đi,\nKisaki liền nhanh nhẹn trong khoảng thời gian đó——!」 → **「Làm theo chỉ thị dời chiếc bàn trà hình tam giác và sofa đi,\nKisaki liền nhanh nhẹn trong khoảng thời gian đó——Ư!」** (Sweep lost-gasp-trailing: VN giữ dấu gạch nhưng làm mất tiếng gasp cuối.)

### fa/fu (1 dòng)

- **1274 [れいな]** — JP 「ふああっ」 / TW 「哇」 / Cũ: 「Phu a a.」 → **「Phùa a.」** (ふあ → "phùa" theo quy tắc fa/fu đã chốt (tiền lệ h3: ふあっ→"phùa"); あ dài thêm một "a"; っ cuối từ cảm thán được xem là kéo dài, không thêm Ư — theo tiền lệ れいな01 1336.)

### SFX/discourse (1 dòng)

- **1655 [真闇]** — JP 「大正解！　――っと」 / TW 「說得太對了！……那麼」 / Cũ: 「Hoàn toàn chính xác! ——Xong」 → **「Hoàn toàn chính xác! ——Rồi」** (っと ở đây là âm chuyển ý ("rồi thì—", Mayami khen xong chuyển sang bước tiếp theo ở 1657), không có nghĩa "xong/hoàn thành". "Rồi" là tiểu từ chuyển tiếp tiếng Việt tương đương.)

## §3. Kiểm chứng & ghi chú

- **Sweep:** 3 mục cho file, nhận cả 3 fix nguyên văn (1339, 1363, 1885). Quét máy bổ sung toàn file: 2 dòng còn っ thô trong VN chính là 1339/1363 (đã sửa); không bắt thêm gasp nào sweep bỏ sót.
- **Đại từ Soutetsu đã rà toàn file (56 dòng):** "anh" đúng với Hibiki/Reina (827, 1318, 1442, 1444, 1487); "tôi" đúng với Kisaki (1449, 1468, 1518, 1635, 1659, 1695); "cô" cho Kisaki nhất quán 5× (1428, 1438, 1518, 1659, 1697); "chị" cho Mayami đúng (1218, 1405, 1456, 1660); "em ấy" = Reina (1392) đúng; "em gái tôi" = Michiko (1195) đúng. Các dòng giữ nguyên có lý do: 1505 + 1637 (mơ hồ người nghe — xem §4); 1442/1444 (nhóm học với Hibiki/Reina → "anh"); 1349 ("Xin lỗi em" — Hibiki hoặc Reina, cả hai đều là "em").
- **Kisaki tự xưng — GIỮ NGUYÊN, không đổi sang "em":** ボク → "tôi" với Soutetsu trong cả file (1351, 1355, 1439, 1446, 1452, 1724, 1725) và "chị" với Reina (1300, 1454, 1503, 1569). Trong file này Kisaki ở vai trò giáo viên/chuyên gia, gọi Soutetsu là "cậu" (1439), nên cặp "tôi"/"cậu" là nhất quán; tiền lệ "em" ở lr_稀咲h1 có thể chỉ đúng trong bối cảnh riêng của file đó. Đã cờ cho Hieu xác nhận ở §4.
- **fa/fu đã rà toàn file:** ふぁ/ふあ chỉ có 1274 (đã sửa). ふは (1290 "Phu ha a a a.") và ふわ (1279, 1292, 1658 — đều dịch "Oa…", khớp TW 哇) không thuộc quy tắc đã chốt → giữ nguyên. 1292 はうっ→"ha ư" (っ trên câu cảm thán) giữ nguyên, ghi chú cùng mục fa/fu ở §4.
- **Thuật ngữ đã chốt kiểm tra:** Railord (1529, 1592) ✓; "chị em dâu" cho 義理の姉妹 (1955, TW 姻親姐妹 xác nhận — không phải "nuôi") ✓; "Long đởm" cho 竜胆 (1730) ✓; "Sư phạm bậc 4" cho ４級師範 (2109) ✓; "tiền bối Kisaki" cho 稀咲センパイ (1521) ✓; "Tự do hoa" cho 自由花 (1537, 1593, 1640, 1696) ✓; "ousu (trà loãng)" (1185) ✓; "cô giáo Kisaki" (1476, 1575, 1697) ✓.
- **SFX khác đã kiểm tra và giữ:** えっへへ→"Ê hê hê" (1365–1380, nhất quán), あはは→"A ha ha" (1298), ふふっ→"Fufu" (1297, 1300), ふふーん→"Hư hừm" (1320, tiếng hừ đắc ý — không phải cười thành rên), ごくっ→"Ực" + ふうっ→"phù" (1735), ん→"Ưm" (1693), パチ→"Lách cách"/"Tách" (1926, 2168–2170), さくっ→"phập" (2168).
- **Không có:** lệch vị trí, chuỗi xoay vòng, nhiễm chéo file khác, dòng mồ côi, dòng chưa dịch, trùng khóa. Không có %l cần sửa (0 thẻ %l trong file). Không có hàng chờ thống nhất nào khác trong file ngoài mục fa/fu ở §4.

## §4. Chờ Hieu (không đưa vào JSON/TOML — không tự quyết)

- **1505:** Soutetsu "Anh cảm thấy rằng, lễ nghi chính là sự tích lũy của những điều như vậy." — người nghe mơ hồ: Kisaki vừa demo seiza (1503) nhưng câu này cũng có thể nói với cả nhóm/Reina. Nếu là Kisaki → "Tôi cảm thấy". Giữ nguyên "Anh", chờ Hieu chốt.
- **1637:** Soutetsu "Bông hoa thay cho khăn cài túi áo ngực của anh, ..." — người nghe mơ hồ: có thể tiếp tục mạch nói với Kisaki (1635 dùng "tôi") hoặc chuyển sang khoe bình hoa với Hibiki/Reina (chủ đề ikebana). Nếu là Kisaki → "của tôi". Giữ nguyên, chờ Hieu chốt.
- **Kisaki ボク với Soutetsu — "tôi" hay "em"?** File này dùng "tôi" (vai trò giáo viên, gọi Soutetsu là "cậu" ở 1439); tiền lệ lr_稀咲h1 dùng "em". Giữ "tôi" trong file này; cần Hieu xác nhận tiền lệ h1 có phải chỉ đúng trong bối cảnh riêng không, trước khi áp dụng rộng.
- **Mâu thuẫn fa/fu toàn dự án ("phùa" vs "phù")** — file này dùng "phùa" theo quy tắc đã chốt cho 1274; các dòng ふは/ふわ giữ nguyên dạng phiên âm (1290, 1292, 1279, 1658) và 1292 はうっ→"ha ư" — chờ đợt thống nhất của Hieu.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1187" = "「Không, cô đừng khiêm tốn như vậy.」"
"1263" = "「Ufufu~」"
"1265" = "「Ufufu~.\\nThấy chị vui, Reina cũng vui lắ-ắm luôn nha~」"
"1266" = "「Ufufu, vậy thì còn gì bằng nữa.」"
"1274" = "「Phùa a.」"
"1339" = "「Ừm. ——Ư!」"
"1357" = "「À, ừm. Tất nhiên rồi.\\nCó vẻ thú vị đấy. Tôi cũng rất hứng thú.」"
"1363" = "「Hửm?——Ư!!!!!!」"
"1376" = "「Ufufu~, đúng vậy nha~. Cả cô Kisaki và chị Hibiki,\\nđều đã dạy cho Reina và anh Soutetsu rất nhiều điều nha~」"
"1405" = "「Nếu chị Mayami cũng không phiền. Hai người đã nói chuyện gì vậy,\\ncó thể cho tôi nghe cùng được không.」"
"1456" = "「Tôi không hề biết……Thay vì tăng lượng muối, chị lại làm cho vị đậm đà hơn,\\nthấm hơn……Chị đã tốn bao nhiêu công sức để làm điều đó——」"
"1511" = "「Thế này đúng không ạ~. ——Ufufu~,\\ntrông giống bàn tay mèo thật đó nha~」"
"1655" = "「Hoàn toàn chính xác! ——Rồi」"
"1692" = "「Thông qua nghệ thuật cắm hoa để thiết kế chính cuộc sống của mình——\\nAnh có cảm giác mình đã học được tầm quan trọng của việc lựa chọn và sắp xếp.」"
"1885" = "Làm theo chỉ thị dời chiếc bàn trà hình tam giác và sofa đi,\\nKisaki liền nhanh nhẹn trong khoảng thời gian đó——Ư!"
"2017" = "Khoảnh khắc chị Mayami thì thầm điều gì đó,\\nReina bật cười khúc khích ufufu."
```

## Kết bài

- JSON `audit-lr-reina-tsuika02-wrong.json`: 16 mục dạng chuẩn list-of-dicts, khóa chuỗi; khối TOML 16 khóa, **0 sai lệch giá trị**; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; diff-sanity: tỉ lệ thấp nhất 1263 (0,33 — thay toàn bộ dòng SFX ngắn うふふぅ "Ư hư hư~"→"Ufufu~"), còn lại ≥0,82; mọi fix chỉ khác old VN ở đúng chỗ sửa mục tiêu.
- **Lượt soát 2: tổng 16 / soát lại 16 / bỏ 0 / sửa 0.** (Soát lại toàn bộ 16 giá trị fix đối chiếu JP + TW lần 2; không phát hiện thêm lỗi; không bỏ, không sửa fix nào.)
- **Tổng cộng sau file này: 109 file / 5.025 dòng sai** (cơ sở 108 file / 5.009 dòng sai + 16 file này).
