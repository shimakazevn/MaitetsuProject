# Quét toàn dự án: sửa chữ っ (gasp) còn sót trong bản dịch Việt

Ngày: 19/11/2026. Nguồn: TOML-2 (227 file, 93.153 dòng script) + CSV "Trang tính 3" (JP/TW/VN).
Theo yêu cầu trực tiếp của Hieu (19/11): "bản dịch còn sót nguyên chữ っ tiếng Nhật trong câu tiếng Việt có rất nhiều hãy cập nhập" — và mở rộng sau đó: tìm cả từ JP gốc, không chỉ các dòng VN còn っ.

## 1. Tóm tắt

| Phần | Nội dung | Số dòng sửa | Số file |
|---|---|---|---|
| A | VN còn nguyên chữ っ | 318 | 59 |
| B1 | Mất gasp cả dòng (JP chỉ là っ + dấu câu, VN chỉ còn dấu câu) | 386 | 160 |
| B2 | Mất gasp cuối dòng (JP kết thúc bằng ――っ / ～っ / …っ, VN chỉ còn gạch) | 431 | 151 |
| B2 giữa dòng | Mất gasp giữa dòng (gasps nằm giữa đoạn, VN có gạch ở giữa) | 11 | 10 |
| **Tổng sửa** | | **1.146** | **210** |

Không sửa (đã phân loại, chi tiết ở mục 7):

- Audit của file đã sửa gasp rồi — không sửa trùng: **32 dòng**.
- VN đã diễn gasp bằng cách khác (Ư/Ự/Hự/Hức, câu cảm thán, SFX đã dịch) — không phải gasp bị mất: **134 dòng**.
- Cần audit file xử lý (lệch dòng / lệch số đoạn, không đặt được gasp chắc chắn): **82 dòng**.
- Chưa chắc chắn: **4 dòng**.
- Tổng số dòng đã rà soát và phân loại: 1.146 sửa + 253 không sửa = **1.399 dòng** (gồm phụ lục §9: +16 sửa, +2 không sửa; phụ lục §10: +5 sửa; phụ lục §11: −1 sửa, +1 không sửa).

## 2. Quy tắc sửa

っ là tiếng nấc/nghẹn (glottal stop — nhân vật nghẹn giọng, hít vào, nấc lên). Theo tiền lệ đã chốt (Hachiroku 12 再開発 2103/2537, các audit Paulette 09–16), dịch thành **Ư** và giữ nguyên dấu câu đi kèm:

| JP | VN |
|---|---|
| 「っ」 | 「Ư」 |
| 「っ!」 | 「Ư!」 |
| 「っ!?」 | 「Ư!?」 |
| 「っ!!!」 | 「Ư!!!」 |
| ——っ | ——Ư (VD "——っ!」" → "——Ư!」") |
| ～っ | ～Ư (VD "A～～っ」" → "A～～Ư」") |
| っ! ở đầu câu | Ư! (VD "「っ! ——Xin hãy dùng…" → "「Ư! ——Xin hãy dùng…") |

Chỉ sửa đúng chỗ っ/gasp — không dịch lại, không sửa dấu câu hay nội dung khác của dòng.

**KHÔNG sửa:**

- っ nằm trong tag `%l` (thuật ngữ Nhật trong tag là hợp lệ) — chỉ sửa っ ở text hiển thị ngoài tag.
- っ gắn vào từ: nhấn mạnh cuối câu (「冷静になり報告しなさいっ！」 → "Bình tĩnh lại và báo cáo đi!"), っ trong từ (ちょっと, しっかり, まったく, って, よっと). Quy tắc: chữ ngay trước っ là kana/kanji tạo thành từ thì đó KHÔNG phải gasp.
- っ là một phần của từ mimetic SFX mà VN đã dịch (tiếng bụng sôi ぐ～っ → "Rột~", tiếng liếm れろろ～っ → "liếm láp～", tiếng trơn trượt にゅる～っ → "Trơn tuột～", tiếng hút/chụt ちゅうう～っ → "chuuu~"...). Phân biệt: っ gắn qua ～ vào một từ mimetic **không phải tiếng nói** (âm thanh của vật/hành động) mà VN đã dịch → không thêm Ư. Ngược lại, っ tách ra bằng ―― khỏi từ đó, hoặc gắn với tiếng nói thuần túy (cười えへ, thở dài はぁ/ふぅ, khóc ひゃ, rên ん, ngạc nhiên え) → vẫn là gasp, sửa bình thường.
- Dòng VN đã diễn gasp bằng cách khác: Ư, Ự, Hự, Hức, hoặc câu cảm thán ("A!!", "Ưm!", "Hả!?"), hoặc SFX đã dịch ("Rột~~~").

## 3. Phương pháp — và cam kết kiểm tra lần 2 (theo yêu cầu của Hieu)

Hieu đã dặn (19/11): "đừng kiểu dùng script để sửa nhiều nhé vì là 91000 line nên rất dễ bị lỗi sửa xong phải kiểm tra lại". Toàn bộ sweep này làm theo đúng yêu cầu đó:

1. **Script chỉ dùng để liệt kê/đếm và kiểm tra máy** (parse TOML, đối chiếu số key, đếm ký tự). Script KHÔNG tạo nội dung bản sửa. Mọi giá trị sửa đều được viết sau khi đọc trực tiếp dòng JP (+TW làm chứng thứ hai) của chính dòng đó.
2. **Kiểm tra lần 2 đầy đủ:** sau khi dựng xong các khối TOML, đã đọc lại **TỪNG** giá trị sửa đối chiếu với dòng JP của chính nó, xác nhận nghĩa và dấu câu đúng — không chỉ kiểm tra parse. Parse đúng + đủ key là cần thiết nhưng KHÔNG đủ.
3. **Kết quả lần 2:**
   - Tổng số bản sửa (bản nháp): 1.128 dòng.
   - Tổng số bản sửa cuối cùng: **1.126 dòng**.
   - Tổng số đã đọc lại đối chiếu JP: **1.126 dòng (100%)**.
   - Số bản sửa bị **loại** trong lần 2: **13 dòng** — 10 dòng là từ mimetic SFX mà VN đã dịch (không phải gasp, xem mục 4), 3 dòng JP/TW mâu thuẫn nhau nên không rõ gasp thuộc về dòng nào (chuyển sang "chưa chắc chắn", xem mục 7.1).
   - Số bản sửa được **viết lại** trong lần 2: **8 dòng (9 chỗ, vì key 1629 có ở 2 file)** — 4 dòng đặt Ư sai vị trí (Ư nằm ở cuối dòng trong khi gasp nằm ở đoạn đầu của dòng gộp), 4 dòng khôi phục gasp đầu dòng bị mất (JP bắt đầu bằng っ đứng riêng, VN chỉ còn "!").
   - Ngoài ra, khi rà soát chéo với các audit file, phát hiện thêm **11 dòng** mà bản sửa của audit còn để sót gasp (còn nguyên っ, hoặc mất gasp) — đã bổ sung vào danh sách sửa. Ở 11 dòng này, giá trị sửa của sweep sẽ **thay thế** giá trị của audit (cùng nội dung, chỉ thêm gasp).
4. Mọi khối TOML đều đã kiểm tra parse bằng tomllib, số key khớp đúng số dòng sửa của file đó (210/210 khối parse đúng, 0 lỗi).

## 4. Đối chiếu số liệu

### 4.1 Phần A — VN còn nguyên chữ っ

- CSV có **327** dòng VN chứa っ (326 ở text hiển thị + 1 chỉ trong tag); TOML-2 có **321** giá trị VN chứa っ (320 ở text hiển thị + 1 chỉ trong tag).
- Hợp của 2 tập (text hiển thị): **336 dòng / 65 file**.
- 16 dòng chỉ có ở CSV: dữ liệu cũ — TOML đã có giá trị khác/đúng (VD ふかみh2 1013: CSV "「っ――」" nhưng TOML "「A——a——ưm——ưm——ưm!!」") — không sửa, ghi chú ở đây.
- 10 dòng chỉ có ở TOML: nằm trong các file trùng của 09_Grand (グランドリライト03/09/10) — đã sửa ở đây.
- Tập sửa: 320 dòng TOML trừ 2 dòng đã sửa trong audit Grand 01 (2585, 3560 — audit dịch mới cả câu, trong đó có gasp) = **318 dòng / 59 file**.
- 1 dòng chỉ có っ trong tag (Paulette 15 1849, っ nằm trong thuật ngữ Nhật いっとき của tag) — KHÔNG sửa, tag giữ nguyên.
- Kiểm tra thêm: ở cả 318 dòng, số っ trong JP ≥ số っ trong VN (mọi っ trong VN đều có gasp JP tương ứng, 0 dòng JP không có gasp); 42 dòng có >1 っ (nhiều nhất 6), tổng 383 ký tự っ ở text hiển thị. 24 dòng vừa có っ thô vừa mất thêm 1 gasp cuối (gộp A+B2) — đã sửa cả hai trong cùng một giá trị.
- Quirk ghi chú (không cần làm gì): ふかみh2 1442 — CSV gán JP 独占欲 cho key này, nhưng `# JP:` trong chính TOML-2 ở 1442 là 呼吸も、望みも…――っ！ (khớp với dòng CSV của 11_Other); TOML tự nhất quán, bản sửa "là——Ư!" giữ nguyên.

### 4.2 Phần B1 — mất gasp cả dòng

- Liệt kê theo đoạn: **406 ứng viên (401 dòng riêng biệt)** — đoạn JP chỉ là っ + dấu câu, đoạn VN chỉ còn dấu câu.
- Đối chiếu với ước tính ~426 của bản quét trước: ước tính đó đếm theo dòng (row-level) trên CSV, còn lần này đếm theo đoạn (segment-level). Chênh lệch do các dòng nhiều đoạn (một dòng có 2 gasp ở 2 đoạn), các dòng VN đã diễn gasp, và các dòng đã sửa ở phần A.
- 587 dòng liên quan B1 (ứng viên + chưa rõ) đối chiếu đủ: **381 sửa** + 105 đã sửa ở phần A (VN có っ thô) + 101 không sửa (25 audit đã sửa, 48 VN đã diễn bằng câu cảm thán, 27 lệch dòng cần audit file, 1 audit diễn bằng "Á!!!"). 381 + 105 + 101 = 587. ✓

### 4.3 Phần B2 — mất gasp cuối dòng (và giữa dòng)

- Liệt kê theo đoạn: **653 dòng riêng biệt** liên quan (ứng viên cùng-chỉ-số + căn đoạn cuối + chưa rõ).
- Đối chiếu với ước tính ~487 của bản quét trước: ước tính đó là row-level; con số theo đoạn của lần này cao hơn vì nhiều dòng có gasp ở 2 đoạn và vì đếm cả các dòng đã diễn/không sửa. 653 = **427 sửa** (416 cuối dòng + 11 giữa dòng) + 76 sửa ở dạng khác (chủ yếu phần A) + 150 không sửa (đã có audit sửa / đã diễn / lệch dòng / chưa chắc chắn). 427 + 76 + 150 = 653. ✓
- Riêng B2 giữa dòng: 47 ứng viên (VN có gạch ở giữa đoạn đúng vị trí gasp); chỉ sửa khi số gasp JP == số gạch+dấu câu của VN — 12 dòng đạt, 1 dòng trong đó sau đó bị loại ở lần 2 (SFX hút: れいなh1 1271), còn **11 dòng**. Các dòng không đạt kiểm tra đếm được đưa vào "cần audit file".

## 5. Các dòng đã loại trong lần kiểm tra thứ hai (13 dòng — KHÔNG có trong khối sửa)

10 dòng là từ mimetic SFX mà VN đã dịch (không phải gasp), 3 dòng JP/TW mâu thuẫn nhau.

| File | Key | JP (đoạn gasp) | VN | Lý do loại |
|---|---|---|---|---|
| 01_Hachiroku/ハチロク04_煙には煙を.txt.toml | 3088 | （ぐ～っ） | （Rột~） | already-rendered: stomach growl ぐ～っ already rendered as (Rột~) |
| 01_Hachiroku/ハチロクh3_磨き洗い.txt.toml | 1224 | 「ぺろっ――れろっ――ちゅっ――れろろ～っ」 | 「Liếm——liếm——chụt——liếm láp～」 | already-rendered: tongue mimetic れろろ～っ already rendered as liếm láp～ |
| 01_Hachiroku/ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 1718 | （にゅる～っ） | （Trơn tuột～） | already-rendered: slimy mimetic にゅる～っ already rendered as (Trơn tuột～) |
| 01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 837 | 「れるっ――ずぢゅじゅじゅじゅじゅじゅじゅ～～っ！」 | 「Mút——chùn chụt chùn chụt chùn chụt~~!」 | already-rendered: slurping mimetic ずぢゅじゅじゅ～～っ already rendered as chùn chụt~~! |
| 01_Hachiroku/ハチロクh8_桜色のひめごと.txt.toml | 1584 | （もみゅ！　むにゅっ！　にゅるっ！　さすすす～～っ） | （Nắn bóp! Mềm mại! Trơn tuột! Vuốt ve~~） | already-rendered: stroking mimetic さすすす～～っ already rendered as Vuốt ve~~ |
| 02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml | 1663 | （ぐ～～～～～～っ） | （Rột~~~~~~） | already-rendered: stomach growl ぐ～～～～～～っ already rendered as (Rột~~~~~~) |
| 02_Hibiki/日々姫03_客車手配.txt.toml | 2328 | 「新しいのが来て、\x%l気動車;#00ffc040;気動車%l;#;改造\x%l客車;#00ffc040;客車%l;… | 「Có xe mới đến, \x%l客車;#00ffc040;toa hành khách%l;#; được c… | already-rendered: extrusion SFX にゅ～っ already rendered as phụt~ |
| 03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1028 | 「ぐちゅっ！　ちゅぶっ！　ずちゅっ！　じゅぼっ！\nぐりゅっ――リュッ――じゅぶ！　じゅるるる～～っ！」 | 「Gu chu! Chu bu! Zu chu! Ju bo! Gu ryu——ryu——ju bu! Ju ru r… | already-rendered: slurp mimetic じゅるるる～～っ already rendered as Ju ru ru ru～～! |
| 04_Reina/lr_れいなh1_レディ・れいな.txt.toml | 1271 | 「ちゅぶっ！　ちゅぼっ！　ちゅぶっ！　ちゅずず～っ！\nずりゅっ！　ちゅむっ　れろおっ、じゅっ！　ちゅぶっ」 | 「Chu mút! Chu mút! Chu mút! Chu mút t~! Chu mút! Chu mút! L… | already-rendered: sucking mimetic ちゅずず～っ already rendered as Chu mút t~! |
| 04_Reina/れいなh3_おもらし自由化大作戦.txt.toml | 1199 | 「はっ――あっ――ちゅ――ちうっ――\nちゅっ――ちゅうっ――ちゅっ――ちゅうう～っ」 | 「Ha——a——chụt——chiu—— Chụt——chụt——chụt——chuuu~」 | already-rendered: kissing mimetic ちゅうう～っ already rendered as chuuu~ |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1078 | 「蒸留器の加熱も……してくれているのか――っ！」 | 「Kh——a…… Fuka, mi——」 | uncertain: JP/TW disagree (JP asks about the distiller, TW/VN is Fukami gasp "Ah... Fukami..."); VN follows TW and is truncated mid-word |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1588 | （まるで――卵を温める母鳥の羽――っ！！？） | Đột nhiên Fukami ngậm sâu vào—— Thu trọn toàn bộ sự cương c… | uncertain: JP/TW disagree (JP is a mother-bird simile, TW/VN is Fukami deep-throating) |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1566 | 「ん～～～――っ！！！」 | Không thể kìm nén được nữa. Fukami há to miệng, để lọt ra n… | uncertain: JP/TW disagree (JP is a short moan ん～～～――っ, TW/VN is a long narration about Fukami suppressing her voice) |

## 6. Các dòng sửa lại trong lần kiểm tra thứ hai (8 dòng / 9 chỗ)

| File | Key | Giá trị nháp (sai) | Giá trị đã sửa | Lý do |
|---|---|---|---|---|
| 01_Hachiroku/ハチロク02_ハートブレイク・レイルロオド.txt.toml | 2461 | 「Mi——!? A a——Ư」 | 「Mi——Ư!? A a——」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 01_Hachiroku/ハチロク14_橋.txt.toml | 1614 | 「! Ra là vậy, cái này cũng là do áp suất không khí——Ư!!?」 | 「Ư! Ra là vậy, cái này cũng là do áp suất không khí——Ư!!?」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 01_Hachiroku/ハチロク15b_さよなら列車.txt.toml | 1602 | 「! ~~~Ư!」 | 「Ư! ~~~Ư!」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 01_Hachiroku/ハチロクh8_桜色のひめごと.txt.toml | 953 | 「~~~~~~~~~Ư!!!」 | 「ƯƯƯƯƯ~~~~~~~~~Ư!!!」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 02_Hibiki/lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1777 | 「Quy đầu của, anh hai――phần đầu của, chim――! Đang――hôn vào―… | 「Quy đầu của, anh hai――phần đầu của, chim――Ư! Đang――hôn vào… | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 03_Paulette/ポーレット07_うさぎ.txt.toml | 1719 | 「Oa oa oa oa oa~ Mẹ ơi, bé thỏ, bé thỏ, hu hu hu~Ư」 | 「Oa oa oa oa oa~Ư Mẹ ơi, bé thỏ, bé thỏ, hu hu hu~」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 06_Kisaki/稀咲h3_チャイナドレスでおもてなし.txt.toml | 2003 | 「Đầu vú…… được, anh Soutetsu…… vuốt ve――…… Chỉ cần vậy, thô… | 「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư Chỉ cần vậy, th… | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 07_Nagi_Fukami/グランドリライト09_凪.txt.toml | 1629 | 「! ――Ư!」 | 「Ư! ――Ư!」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |
| 09_Grand/グランドリライト09_凪.txt.toml | 1629 | 「! ――Ư!」 | 「Ư! ――Ư!」 | Ư đặt sai vị trí / gasp đầu dòng bị mất — đã viết lại sau khi đọc JP |

Ghi chú: 4 dòng đầu (2461, 1777, 1719, 2003) là dòng gộp 2 đoạn — gasp nằm ở đoạn 0 nhưng bản nháp đặt Ư ở cuối dòng (thuộc về đoạn 1, đoạn này không có gasp). 4 dòng sau (953, 1629 ×2 file, 1614, 1602) khôi phục gasp đầu dòng: JP bắt đầu bằng っ đứng riêng mà VN chỉ còn "!".

## 7. 11 dòng bổ sung từ rà soát chéo audit (giá trị sweep thay thế giá trị audit)

Khi quét toàn bộ 1.945 giá trị sửa trong các audit file, phát hiện 11 dòng mà bản sửa của audit còn để sót gasp. Ở các dòng này, **áp dụng giá trị của sweep, không áp dụng giá trị của audit** (cùng nội dung, chỉ khác ở chỗ gasp).

| File | Key | Giá trị audit | Giá trị sweep |
|---|---|---|---|
| 01_Hachiroku/ハチロク13_夜の嵐.txt.toml | 2068 | 「!!?」 | 「Ư!!?」 |
| 02_Hibiki/日々姫03_湯富院.txt.toml | 1933 | 「っ！！」 | 「Ư！！」 |
| 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml | 2306 | 「っ!」 / 「A.」 | 「Ư!」 / 「A.」 |
| 03_Paulette/ポーレット01_御一夜探し.txt.toml | 1947 | 「Ư!」 「——っ」 | 「Ư!」 / 「——Ư」 |
| 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml | 1519 | 「——っ」 | 「——Ư」 |
| 02_Hibiki/日々姫03_湯富院.txt.toml | 2433 | 「～～っ」 | 「～～Ư」 |
| 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml | 2338 | 「A——!!!」 | 「A——Ư!!!」 |
| 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml | 2326 | Ồ, vào đường hầm rồi sao. / Hơi có mùi khói——! | Ồ, vào đường hầm rồi sao. / Hơi có mùi khói——Ư! |
| 01_Hachiroku/ハチロク13_夜の嵐.txt.toml | 2334 | Tôi vươn tay ra. Hachiroku từ từ nắm lấy tay tôi——! | Tôi vươn tay ra. Hachiroku từ từ nắm lấy tay tôi——Ư! |
| 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml | 1583 | 「Phù…… a~」 | 「Phù…… a~Ư」 |
| 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml | 1590 | 「Phù~」 | 「Phù~Ư」 |

## 8. Khối TOML theo file (210 file — mỗi file MỘT khối, gộp cả A + B1 + B2)

Cách dùng: copy khối của file cần sửa, paste vào phần `[script]` của file TOML tương ứng (giữ nguyên BOM UTF-8 và CRLF của file). Mỗi khối đã kiểm tra parse bằng tomllib, số key khớp đúng số dòng sửa của file đó.

### 00_Common/共通01_右田双鉄の帰還.txt.toml — 5 dòng (raw-tsu: 5)

```toml
[script]
1247 = "「Ư! ——Xin hãy dùng \\x%l制動;#00ffc040;hãm phanh%l;#; tối đa. Tôi sẽ hỗ trợ để không bị \\x%l滑走;#00ffc040;trượt bánh%l;#;.」"
1317 = "「Chắc rắc xuống cái là bị cuốn trôi đi ngay thôi. Nhưng mà, có làm còn hơn không——Ư」"
1375 = "「Tôi sẽ lập tức kết nối \\x%l共感;#00ffc040;cộng cảm%l;#; với \\x%lレイルロオド;#00ffc040;Railord%l;#; phía trước để thông báo việc chậm trễ ——Ư!? Gì cơ!? Hả? Xin hãy nhắc lại!?」"
1382 = "「Tiếp tục \\x%l制動;#00ffc040;hãm phanh%l;#;. ——Thêm chút nữa——áp suất, thêm một chút nữa thôi——Ư!!!」"
1430 = "「Đã rõ tiếp tục giảm tốc. \\x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng cường——Ư!」"
```

### 00_Common/共通02_日々姫と真闇と人形と.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
2194 = "「Tôi tuyệt đối không lên \\x%lエアクラ;#00ffc040;Aircra%l;#; đâu! \\x%lエアクラ;#00ffc040;Aircra%l;#; là, thứ đó là, kẻ thù truyền kiếp của chúng tôiƯ!!」"
2570 = "「Đến cả anh hai cũng nói y như chị hai vậy~Ư」"
```

### 00_Common/共通03_ハチロクとナビ.txt.toml — 3 dòng (lost-gasp-whole: 2, raw-tsu: 1)

```toml
[script]
1273 = "「Ư!!!」"
1274 = "「Ư!?」"
1323 = "「Dù có vậy đi chăng nữa! Em cũng không thèm đi \\x%lエアクラ;#00ffc040;Aircra%l;#;Ư」"
```

### 00_Common/共通04_キハ07。ポーレットとれいな.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
2676 = "「Ư!」"
2677 = "「Ư!」\\n「A」"
```

### 00_Common/共通05_ようやく石炭.txt.toml — 2 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 1)

```toml
[script]
2287 = "「A, giống như than của Hachiroku——Ư!!」"
2763 = "「Ư!?」"
```

### 00_Common/共通07_鍵.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
2144 = "「Ư!」"
```

### 00_Common/共通08_傷跡.txt.toml — 3 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 2)

```toml
[script]
1996 = "「Đó, Hachiroku. Vào rồi đấy——Ư!?」"
2098 = "「Ư!」"
2099 = "「Ư!!」"
```

### 00_Common/共通09_さきだつもの.txt.toml — 8 dòng (lost-gasp-trailing: 7, lost-gasp-whole: 1)

```toml
[script]
109 = "Ngay cả chị \\x%l車販;#00ffc040;nhân viên bán hàng%l;#; cũng không trụ nổi trước cú rung lắc dữ dội, ngã nhào cùng với chiếc xe đẩy——Ư!?"
2581 = "「Không sao chứ, Michi——Ư!?」"
2634 = "「Khoan!? Anh hai! E-Em đi trước đây~~Ư!!」"
2681 = "「Nhà bán shochu tới đây làm gì? Tại sao lại làm con gái nhà người ta khóc chứ ――――Ư!」"
2796 = "「Ư!」"
3270 = "Tôi nói với Michiko, cũng là để tự nhủ với bản thân mình như vậy——Ư!?"
3284 = "Cú lắc quá mạnh khiến cả cơ thể tôi và Michiko đều bị hất văng——Ư!?"
3655 = "（Nếu vậy thì——cơn đau—— như thể phổi bị nghiền nát lúc nãy là——Ư）"
```

### 00_Common/共通10_クマ川くだりで見る景色.txt.toml — 3 dòng (raw-tsu: 2, lost-gasp-whole: 1)

```toml
[script]
2209 = "「Cái gì mà 『Không phải chuyện lợi ích』 chứ, toàn là nói xằng nói bậy. Nếu không có lợi ích, thì ngay cả ngôi đền này cũng chẳng duy trì nổi đâu――Ư!」"
2815 = "「Ư!?」"
2995 = "Để chắc chắn, tôi nhận lấy tấm danh thiếp và nhìn kỹ, quả nhiên trên đó ghi, 『Giám đốc chi nhánh Ohimitera, Ngân hàng Kumamoto』――Ư!?"
```

### 00_Common/共通11_経営資源.txt.toml — 3 dòng (raw-tsu: 1, lost-gasp-whole: 2)

```toml
[script]
1811 = "「…………Ư」"
3067 = "「Ư!!!!」"
3068 = "「Ư!?」"
```

### 00_Common/共通12_のぞみ.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
2632 = "「Ư!」"
2633 = "「Ư!?」"
```

### 00_Common/共通13_勾配図.txt.toml — 7 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 3)

```toml
[script]
1874 = "「Không xong rồi! Bị thân cây chắn ngang hoàn toàn rồi——Ư!!?」"
1927 = "「Hachiroku nói trước đi——Ư!」\\n「Ngài Soutetsu nói trước đi ạ——Ư!」"
2028 = "「Phù~~Ư」"
2533 = "「Ư!」"
2534 = "「Ư!!」"
2535 = "「Ư!!!!!」"
2810 = "Nếu để nhịp tim và nhịp thở rối loạn, tốc độ sẽ giảm đi tương ứng. Sẽ làm tăng nguy cơ xảy ra tai nạn mất——Ư!!?"
```

### 00_Common/共通14_負債.txt.toml — 3 dòng (raw-tsu: 3)

```toml
[script]
1443 = "「Gì chứ! Cả bố lẫn cái ông chú Mototada đó, hoàn toàn coi anh hai như đồ vật vậy～Ư」"
1549 = "「Aー……aー……a～～Ư」"
1550 = "「A～～Ư」"
```

### 00_Common/共通15_回り始める動輪.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1906 = "「Chà.」\\n「Ư!」"
```

### 01_Hachiroku/lr_ハチロクh1_今ひとたびの契り.txt.toml — 16 dòng (lost-gasp-trailing: 10, lost-gasp-whole: 6)

```toml
[script]
1142 = "「Hyauuuuuuuuuuuuuuuu~~~Ư!!!」"
1152 = "「Ư!!?」"
1195 = "「Fua! A! A! ~~~~Ư!!!」"
1219 = "「Ư!!」"
1220 = "「Ư!!!」"
1221 = "「Ư!!!!」"
1222 = "「Ư!!!!!」"
1223 = "「Ư!!!?」"
1234 = "「A……——ưm——chum——chuu——Ư」"
1264 = "「Nnnnnnuuuuu~~~~~Ư!!!」"
1265 = "「Nn~~~~~~Ư!!!!」"
1330 = "「Vì, vậy——Ư!!!!」"
1430 = "「~~~Ư」"
1435 = "「~~~~~~Ư」"
1437 = "「~~~~~~~~~~~~Ư!!!!!!」"
1810 = "Âm đạo đột ngột siết chặt lại——Ư!!??"
```

### 01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml — 17 dòng (raw-tsu: 10, lost-gasp-whole: 2, lost-gasp-trailing: 5)

```toml
[script]
1414 = "「Ư」"
1415 = "「Ư!!!」"
1416 = "「Ư!!!!」"
1417 = "「Ư!?」"
1418 = "「Ư——a——Suzu, Suzu!」"
1456 = "「Ư!!!!」"
1457 = "「Ư!!!!!!」"
1458 = "「Ư!!!!!!!!」"
1459 = "「Ư!!!?」"
1462 = "「A——a——Ư——」"
1474 = "「A~~~~Ư」"
1483 = "「Ư——!!!!」"
1557 = "「Anh cũng vậy, Suzu. Thế nên——Ư!!!?」"
1583 = "「Em! Không——a ư——giới hạn, giới hạn rồi! Ư——nhưng mà——cùng, cùng nhau, nhé, cùng nhau」"
1681 = "「Su, zu. Không được đâu. ——Cứ thế này thì, anh——Ư!?」"
2009 = "Một hành động vô cùng dâm đãng, nhưng lại được tô điểm bằng nụ cười ngây thơ——Ư!!"
2109 = "Chuyển động của Suzu trở nên đơn điệu. Chỉ để thúc giục tôi xuất tinh—— sự thẳng thừng, đơn giản, bạo lực, mang tính động vật và máy móc này——Ư!?"
```

### 01_Hachiroku/lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml — 15 dòng (raw-tsu: 8, lost-gasp-whole: 1, lost-gasp-trailing: 6)

```toml
[script]
1203 = "「Ư!」"
1204 = "「Ư!!!!!」"
1206 = "「ƯƯ!!!? Khoan——au!!」"
1207 = "「Ư!?」"
1248 = "「Ư!!!!!!」"
1249 = "「Ư!!!?」"
1264 = "「A——a——Ư————. Kuha!」"
1273 = "「Ư!!!?」"
1331 = "「Giống như đài phun nước nya! Thú vị quá nya~Ư!!」"
1378 = "「Em——cô bé——a hỏng mất—— mất thôi——hyagu——ngài Soutetsu——của——Ư!」"
1385 = "「Ư~~~~~~~Ư!!!!」"
1494 = "「~~~~Ư!!」"
1497 = "「~~~~~~~~~~~~~~~~Ư!!!!」"
1642 = "Sự cương cứng đang xuất tinh lại tiếp tục bị những ngón tay của Suzu đùa giỡn——Ư!!!!"
1757 = "Đã phản ứng lại. Cả trái tim và cơ thể dốc toàn lực. Sự tấn công bất ngờ, quá đỗi đáng yêu——Ư!?"
```

### 01_Hachiroku/グランドリライト10_ハチロク.txt.toml — 5 dòng (raw-tsu: 5)

```toml
[script]
1188 = "「Ư——」"
1676 = "「Ư!!?」"
1693 = "「Ư!」"
1694 = "「Ư!!!」"
2174 = "「Ư!!!」"
```

### 01_Hachiroku/ハチロク01_こんにちわ赤ちゃん.txt.toml — 6 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 2)

```toml
[script]
1620 = "「——Ư!」"
1621 = "「——————Ư!!!」"
2262 = "「Ư!!」"
2263 = "「Ư!!!」"
2280 = "「Anyu~~Ư.」"
2637 = "「Không thể thay đổi được? ——Rốt cuộc là chuyện gì chứ————Ư!!!」"
```

### 01_Hachiroku/ハチロク01_双鉄の目・ハチロクの目.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1755 = "「Ư!」"
```

### 01_Hachiroku/ハチロク02_8620運転台通信.txt.toml — 4 dòng (lost-gasp-whole: 3, lost-gasp-trailing: 1)

```toml
[script]
1837 = "「Ư!」"
2261 = "「Ư!!」"
2272 = "『「Hả~~Ư!」\\n「Hả~~Ư!」』"
2282 = "『「Ư!!?」\\n「A.」』"
```

### 01_Hachiroku/ハチロク02_ハートブレイク・レイルロオド.txt.toml — 6 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 4)

```toml
[script]
78 = "\\x%l汽笛;#00ffc040;Còi hơi nước%l;#; không kêu. Tôi cứ tưởng đương nhiên là nó sẽ kêu chứ——Ư!?"
2103 = "「Ư!!?」"
2139 = "「Ư!!!」"
2461 = "「Mi——Ư!? A a——」"
2654 = "「Đó! Giờ đâu phải lúc nói chuyện thong thả đâu! Cứ vậy rồi lỡ luống cuống thêm thì lại càng nguy hiểm hơn á~Ư!!」"
3261 = "Paulette chạy chậm lại chỗ tôi. Nhưng, biểu cảm của em ấy lại tối sầm——Ư!?"
```

### 01_Hachiroku/ハチロク03_冥国式レイルロオド.txt.toml — 9 dòng (raw-tsu: 6, lost-gasp-whole: 3)

```toml
[script]
1528 = "\"Olivy đã bị đối xử như thế nào ở Đường sắt Mikan\" ——Ư!"
2124 = "「Ư!!?」"
2125 = "「Ư!?」"
2165 = "「Ư!!」"
2167 = "「Ư!!!!」"
2168 = "「Ư!?」"
2629 = "「Ư!」\\n「Không phải đâu ạ!」"
2684 = "「Ngài Soutetsu!」「Phanh khẩn cấpppp!!!!」\\n「Ư!!!」"
3078 = "Chắc hẳn Olivy cũng đang tập trung cao độ. Ánh mắt cô ấy như xuyên thấu lưng tôi, nhưng nếu cứ giữ vững phong độ này thì——Ư!"
```

### 01_Hachiroku/ハチロク03_客車試験.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
1780 = "「Ư!!?」"
```

### 01_Hachiroku/ハチロク04_煙には煙を.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
2455 = "「Ư!」"
```

### 01_Hachiroku/ハチロク05_レイルロオドたち.txt.toml — 8 dòng (raw-tsu: 4, lost-gasp-whole: 2, lost-gasp-trailing: 2)

```toml
[script]
2267 = "「Ư!!?」"
2382 = "「Ư!」"
2439 = "「Ư!!!?」\\n「Gì vậy!?」"
2443 = "「Ư!?」"
2459 = "「Ư! Anh Soutetsu cũng giống Hachiroku thôi! Làm sao mà hiểu được cảm giác của bọn Olivy chứ.」"
3023 = "「Ư!?」"
3326 = "Không phải ở nhà bếp――vậy thì――Ư!!?"
3611 = "（Tôi cùng Hachiroku vội vàng đỡ lấy cô ấy——Ư!!?）"
```

### 01_Hachiroku/ハチロク05_軋み.txt.toml — 5 dòng (raw-tsu: 5)

```toml
[script]
1538 = "「——Ư! Giới hạn 60——!」"
1900 = "「Ư!」"
1901 = "「Ư!?」"
1910 = "『「Ư!?」\\n「Ư!?」』"
2410 = "Tôi rút một tập hồ sơ xếp ở góc xưởng đầu máy ra, và so sánh với bức ảnh của \\x%l8620;#00ffc040;8620%l;#; ngay sau khi cải tạo――――Ư!"
```

### 01_Hachiroku/ハチロク06_それぞれの傷跡.txt.toml — 5 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 2)

```toml
[script]
1974 = "「Hỏi han gì chứ――sợ tai nạn là chuyện đương nhiên mà――Ư!」"
2025 = "「Ư!!?」"
2026 = "「Ư!?」"
2031 = "『「――Ư!」\\n「A」』"
2629 = "Nếu bám chặt vào đường ray bằng một lực mạnh, và trục bánh xe bị vặn xoắn mạnh, thì đương nhiên sẽ tạo ra sức mạnh lớn, nhưng tải trọng cũng sẽ lớn theo tương ứng――Ư!"
```

### 01_Hachiroku/ハチロク06_のぞみ.txt.toml — 1 dòng (lost-gasp-trailing-mid: 1)

```toml
[script]
2402 = "「Ồ, dùng bồn nước lạnh để hạ nhiệt――Ư! Không lẽ cơ sở suối nước nóng này được xây dựng vì mục đích đó sao?」"
```

### 01_Hachiroku/ハチロク07_ハチロクの目覚め.txt.toml — 8 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 4)

```toml
[script]
1457 = "「Nếu có Michiko ở đây thì có thể bàn bạc…… Không, vốn dĩ nếu có Michiko, thì chuyện gặp gỡ Hachiroku đã――Ư!」"
1487 = "「Sao vậy, Hachiroku――Ư!?」"
1661 = "「Ngài Soutetsu――Ư!?」"
1676 = "「Ư!」"
1677 = "「Ư!!!」"
1678 = "「Ư!!?」"
1679 = "「Ư!?」"
2208 = "Không hiểu sao tôi lại thấy xấu hổ vô cùng, bất giác quay lưng lại――Ư!"
```

### 01_Hachiroku/ハチロク07_延命.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
2548 = "「Ư!!?」\\n「Trời ạ!」"
2828 = "「Ư!!?」"
3528 = "Dù đã nghe nói là \"chắc chắn sẽ hứng thú\", nhưng tôi không ngờ lại đến mức này——Ư!!"
```

### 01_Hachiroku/ハチロク08_台枠問題.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
2501 = "「Ư!」"
2502 = "「Ư!?」"
```

### 01_Hachiroku/ハチロク08_教導.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
3202 = "Nghe thấy giọng nói đau đớn, tôi quay lại. Olivy lảo đảo, loạng choạng——Ư!!?"
```

### 01_Hachiroku/ハチロク09_もくもくオリヴィ.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
1648 = "「Ư!」"
1675 = "「Ư!?」\\n「Á!?」"
```

### 01_Hachiroku/ハチロク09_採決.txt.toml — 4 dòng (lost-gasp-whole: 3, lost-gasp-trailing: 1)

```toml
[script]
2452 = "「Ư!」"
2453 = "「Ư!!?」"
2454 = "「Ư!?」"
2649 = "Các kỹ thuật viên ở Kokura cũng vậy, và cả những kỹ sư của bộ phận hơi nước thuộc Công ty Xe lửa Hinomoto, nơi được cho là đã bị đóng cửa nữa——Ư!"
```

### 01_Hachiroku/ハチロク10_旺宮鉄道歴史館.txt.toml — 8 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 3)

```toml
[script]
2062 = "「Ư!!?」\\n「!!」"
2205 = "「——Ư」"
2206 = "「Ư!!?」"
2241 = "「Ư!!?」\\n「!!!」"
2259 = "「Ư!!!」"
2839 = "「Ư!!!?」"
3447 = "Tổng tài đầu tiên của Teitetsu được phát hiện đã tử vong do bị tàu cán vào một đêm mưa giữa khuya. Đó là một vụ án mạng, hay chỉ là một tai nạn, sự thật đó cho đến nay vẫn——Ư!"
3663 = "Sững sờ——kinh ngạc——không, còn trống rỗng hơn cả những từ ngữ đó—— A, đúng rồi. Một biểu cảm như người mất hồn——Ư!!?"
```

### 01_Hachiroku/ハチロク10_炙り出し.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
2105 = "「Ư!」"
2110 = "『「Ư!?」\\n「Á——em xin lỗi——ơ, a, anh hai.」』"
2513 = "Để có thể khắc sâu hình ảnh Hachiroku, vào tận trong tim mình——Ư!?"
```

### 01_Hachiroku/ハチロク11_幽霊.txt.toml — 6 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 2)

```toml
[script]
1393 = "「——Ư」"
1718 = "「Rốt cuộc là em ấy bị sao vậy nhỉ? ——Ư」"
1873 = "「Chữ U (幽) trong U linh, âm Kun đọc là 'kasuka' (mờ ảo). Chữ Vong (亡) trong Vong linh, âm Kun đọc là 'nai' (không còn). Tức là——Ư!?」"
2092 = "「Em nói ngốc nghếch gì——Ư!」"
2135 = "「Ư!」"
2183 = "「Ư!!?」"
```

### 01_Hachiroku/ハチロク11_御一夜鉄道小畑線.txt.toml — 4 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 2)

```toml
[script]
1736 = "「Nội dung——là sao——Ư!!」"
1739 = "「Ư!!!!?」"
1781 = "「Ư!!?」"
2858 = "Nghe vậy, tôi mới nhận ra. Bóng dáng em ấy không thấy đâu——không thấy đâu——Ư!!?"
```

### 01_Hachiroku/ハチロク12_ムナカタ来訪.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
1667 = "「Ư!!?」"
1681 = "「E he he~Ư」"
```

### 01_Hachiroku/ハチロク12_再開発.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
2538 = "「Ư!!?」"
2550 = "『「Ư!?」\\n「Cái gì!」』"
```

### 01_Hachiroku/ハチロク13_夜の嵐.txt.toml — 5 dòng (lost-gasp-whole: 3, lost-gasp-trailing: 2)

```toml
[script]
2066 = "「Ư!」"
2067 = "「Ư!!!」"
2068 = "「Ư!!?」"
2334 = "Tôi vươn tay ra. Hachiroku từ từ nắm lấy tay tôi——Ư!"
2818 = "Những dị vật nhỏ bám trên đường ray sẽ nổi lên, làm giảm \\x%l粘着力;#00ffc040;lực bám đường%l;#; một cách đáng kể——Ư!?"
```

### 01_Hachiroku/ハチロク13_実りの秋.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
1830 = "「Ư!!?」"
1846 = "「Ư!?」\\n「Hả!?」"
2933 = "Những biểu hiện như vậy, ít nhất là tôi không hề nhận ra——Ư!!"
```

### 01_Hachiroku/ハチロク14_冬.txt.toml — 9 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 5)

```toml
[script]
2385 = "「Có hại cho cơ thể, thế nên Olivy——Ư!」"
2386 = "「Ư!!?」\\n「!!?」"
2515 = "「Ư!?」"
2551 = "「Ư!」"
2552 = "「Ư!」\\n「A」"
3154 = "「Ư!」"
3623 = "Nở nụ cười tươi như hoa, Olivy——Ư!?"
3861 = "Em tuyệt vọng chạy đến, đỡ lấy bé Olivy đang gục ngã——Ư!?"
4104 = "Âm thanh như thể có thứ gì đó phát nổ——Ư!!?"
```

### 01_Hachiroku/ハチロク14_橋.txt.toml — 11 dòng (lost-gasp-trailing: 6, lost-gasp-whole: 5)

```toml
[script]
1463 = "「Không đâu ạ, làm gì có chuyện——Ư!!?」"
1614 = "「Ư! Ra là vậy, cái này cũng là do áp suất không khí——Ư!!?」"
1834 = "「Tiền bối Kisaki——Ư!」"
1910 = "「Ư!」"
1911 = "「Ư!!!」"
1912 = "「Ư!!?」"
1915 = "「Ư!?」"
1924 = "「Ư!」\\n「Ư!」"
2195 = "Nhưng…… chạy tàu trong điều kiện thời tiết khắc nghiệt gần như không có tầm nhìn thế này, thì ngay cả ban ngày tôi cũng chưa từng trải qua bao giờ——Ư!?"
2398 = "Chỉ dựa vào kinh nghiệm. Chỉ những gì đã tìm hiểu và tích lũy từ trước đến nay——Ư!?"
2746 = "Âm thanh không dừng lại. Thậm chí còn ngày càng lớn hơn——Ư!"
```

### 01_Hachiroku/ハチロク15_家族.txt.toml — 8 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 3)

```toml
[script]
1651 = "「Ư!?」"
1660 = "「Haưư～～Ư」"
2075 = "「Ư!」"
2076 = "「Ư!!!」"
2077 = "「Ư!!?」"
2078 = "「~Ư」"
2088 = "『「Ư!!?」\\n「Ư!!?」』"
2368 = "Hachiroku mở to hai mắt――Ư!?"
```

### 01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml — 6 dòng (lost-gasp-trailing: 5, lost-gasp-whole: 1)

```toml
[script]
1838 = "「~~~~Ư!!」"
2242 = "「Ư!!!」"
2251 = "「Là \\x%l共感;#00ffc040;cộng cảm%l;#; từ Navi! Hình ảnh từ camera và dữ liệu tổng hợp, em sẽ truyền cho cả Olivy——Ư!」"
2256 = "「~~~Ư!!!!」"
2530 = "Nhiệm vụ mà bé Olivy được giao phó. Dù thế nào đi nữa, cũng phải hoàn thành cho bằ——Ư!!?"
2585 = "Tiến vào nơi sâu thẳm nhất trong \\x%l共感;#00ffc040;cộng cảm%l;#; của bé Olivy, nơi mà bình thường tuyệt đối không bao giờ bước vào——Ư!!?"
```

### 01_Hachiroku/ハチロク15b_さよなら列車.txt.toml — 13 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 10)

```toml
[script]
1264 = "「——Ư」"
1524 = "「Ư!!?」"
1568 = "「Ư!!!」"
1569 = "「Ư!!?」"
1570 = "「Ư!?」"
1590 = "「Ư!!?」"
1592 = "「Ư!!?」"
1600 = "「Ư!」"
1601 = "「Ư!!!」"
1602 = "「Ư! ~~~Ư!」"
1616 = "「Ư!!!!」"
1668 = "「Dậy đi, Olivy! Chỉ còn một chút nữa là đến Yatsushiro rồi! Cô đâu phải là một \\x%lレイルロオド;#00ffc040;Railord%l;#; vô trách nhiệm như vậy——Ư!!!」"
1863 = "「Ư!」"
```

### 01_Hachiroku/ハチロク16_春.txt.toml — 9 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 4)

```toml
[script]
1721 = "「Ư!!」"
1725 = "「Ư!」"
1744 = "「Ư!!」\\n「A――」"
1746 = "「Ư!!?」\\n「Kya!」"
1808 = "「Nặng quá~! Nặng quá đi mất~Ư!」"
1932 = "「Hibiki, sao thế? Có bị thương không――Ư!!!」"
2052 = "「Ư!!!!」"
2380 = "Có lẽ vì sốt ruột trước bài diễn văn dài dòng của Tiến sĩ Phượng Hoàng, cô bé sốt sắng bước lên phía trước――Ư!!"
2783 = "Dù biết đó là chuyện không tưởng, nhưng tôi vẫn bất giác đưa mắt tìm kiếm hình bóng ấy giữa đám đông――Ư!!!"
```

### 01_Hachiroku/ハチロクh1_契り.txt.toml — 6 dòng (lost-gasp-whole: 2, raw-tsu: 4)

```toml
[script]
1242 = "「Ư!」"
1371 = "「Anh đoán là——ưm——tinh dịch…… là hạt giống, của em bé——anh nghĩ vậyƯ」"
1376 = "「Vì vậy——xin ngài hãyƯ」"
1463 = "「Xin hãy, lấp đầy em——bằng ngài Soutetsu—— bằng niềm vui, nóng bỏng——mà ngài Soutetsu, trao cho emƯ」"
1508 = "「Ngài…… Soutetsu——cô bé, của em, sắp, tan chảy mất rồi——khó chịu, quá——Ư」"
1519 = "「Ư!!」"
```

### 01_Hachiroku/ハチロクh2_お勉強の成果.txt.toml — 9 dòng (raw-tsu: 5, lost-gasp-whole: 2, lost-gasp-trailing: 2)

```toml
[script]
717 = "「——Nói chuyện, thì lưỡi, sẽƯ!」"
721 = "「——Ư」"
976 = "「Phù a——tuyệt quá——ưm——a——a a! Hự——đến đây——thứ gì đó trắng xóa——to lớnƯ」"
987 = "「Ư!」"
1083 = "「Nế, nếu là con người, thì sẽ có——a—— một căn phòng, dành cho em bé, gọi là tử cung——nhưng màƯ」"
1112 = "「Anh đã nói——là ra——rồi màƯ」"
1156 = "「Có——có thể là vậy ạ——ưm, nhưng nỗi đau đó, em lại cảm thấy, rất vui sướngƯ」"
1201 = "「Ư!?」"
1565 = "Tại sao chứ. Em nhìn tôi bằng ánh mắt thiết tha, rồi cứ thế dừng mọi chuyển động——Ư!?"
```

### 01_Hachiroku/ハチロクh3_磨き洗い.txt.toml — 20 dòng (raw-tsu: 17, lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
964 = "「Không ghét đâu——ưm——vuiƯ—— emƯ——vui lắm——ạƯ——phù a!」"
972 = "「Nhưng, nhưng mà, e, emƯ—— bây giờƯ——bây giờ, đãƯ!——ưm!」"
1003 = "「Á——ngón tay——ưm——vào sâu, trong lỗƯ—— hậu môn, mất——áƯ」"
1012 = "「Phù a——a——nơi, chưa từng biếtƯ——ưm—— đang bị cọ xát——cái này——á——sung——sướng quáƯ」"
1019 = "「Hả!? Dạ——sao em có thể cưỡi lên người ngài Soutetsu đượcƯ」"
1021 = "「A——đến rồi! Cộc một cái——a, phần đỉnh——cậu bé——của ngài SoutetsuƯ」"
1026 = "「A——nóng——nóng quá——ưm—— tinh dịch——tinh dịchƯ——của ngài SoutetsuƯ——」"
1036 = "「A……ưm——em——sẽ cố gắng——a—— tìm ra nơi——sung sướng——mà từ trước đến nay, chưa từng biếtƯ」"
1072 = "「Vâng. Ưm——cùng với, ngài SoutetsuƯ, hai chúng ta——a——, cùng, nhauƯ」"
1089 = "「Phần đỉnh, của cậu bé——là——hự, a—— gọi là——quy đầu——người ta thường nói, vậy đấyƯ」"
1106 = "「Quy đầu, em thíchƯ——quy đầu của ngài Soutetsu, em thích lắm! Hãy hôn, chụt một cái, vào tử cung——của em đi——ưm hưm!!」"
1127 = "「Vâ, vângƯ——em muốn, khai pháƯ——ưm, làm tình——cùng với——ngài Soutetsu——phù a」"
1149 = "「Hiếm khi——lắm mới——ưm——dùng đến—— Hi a, ưm——ưm ư——chỉ khi, thế nào, cũng khôngƯ——」"
1168 = "「A——quan hệ……qua đường——hậu mônƯ」"
1170 = "「Nơi……sung sướng—— khác với, mọi khi……ưm——nơi——mới mẻƯ」"
1189 = "「Chỗ nàyƯ——ưm——cảm giác này, em chưa, từng biếtƯ—— cô, bé——vách, âm đạo, thế này——sung——sướng quáƯ」"
1218 = "「Ngài, Soutetsu——!? Ưm kya——chỗ đóƯ—— là lỗƯ——lỗ——hậu môn, đấy ạƯ——ưm」"
1221 = "「Ư!」"
1222 = "「Ư!!?」"
1226 = "「～～～～Ư!」"
```

### 01_Hachiroku/ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml — 30 dòng (raw-tsu: 26, lost-gasp-whole: 1, lost-gasp-trailing: 3)

```toml
[script]
677 = "「Ô——ồ——cái nàyƯ——」"
866 = "「Không được! Vẫn chưa——Ư——chịu đựngƯ——ưm—— Phù!!!」"
867 = "「Đú, đúng——vậy……nhỉƯ——ưm—— Sự sung sướng……mới——mẻƯ——phù a」"
886 = "「Một chút nữa thôi——anh cũng——Suzu, chịu đựng——thêm một chút nữa——thôiƯ——」"
912 = "「Hya——á——không được——chịu đựng——a—— không thể——đượcƯ——ưm——vìƯ——mông emƯ」"
914 = "「Á——xấu hổ——lắm ạƯ——ưm——rõ ràng, là, mông, thế mà, em——á a——a——lại thế, này」"
915 = "「Á——mông——của em——mông emƯ—— đang được ngài SoutetsuƯ——ngoáy——vào——rồi」"
918 = "「Á——bên trong âm đạo——có gelƯ——lạnh——quáƯ Ưm……phù a——a」"
919 = "「Á——ngài SoutetsuƯ——chậm——như vậyƯ, chậm, chạp——như vậyƯ——hi a!」"
926 = "「Kya fư!? Cô bé——hột leƯ—— chạm, vào rồi——ưm ưm～～～～～～～Ư!!」"
931 = "「Kyu fư ư ư! A——trơn tuột—— cái nàyƯ——thích quá!!!」"
933 = "「Hya gư!? A——khoét sâuƯ——ưm—— hyu a!!!」"
935 = "「Hya ư!? Ưm——hi—— trơn tuột——mông em——a——cái nàyƯ——sâu quá——」"
938 = "「Á!? Ngài, SoutetsuƯ——á—— cậu bé——rút ra——không chịu, đâu——ưm」"
958 = "「A——đến rồi——hôn đi——cô bé—— tận cùng, bên trongƯ——tử cung, hãy,——hôn đi」"
962 = "「Ư a――――cái này, là——Ư」"
966 = "「A……vâ, vâng. Nếu dùng cái đóƯ——ưm—— bên trong, hậu mônƯ——có thể tiến sâu, hơn nữa——a」"
983 = "「A, v, vângƯ—— theo ý, ngài SoutetsuƯ!?——ưm hưm!」"
985 = "「A, nóng——quá——mông emƯ——bụng, cũngƯ—— ưm——nóng, quá ạƯ——Ngài, Soutetsu——」"
1013 = "「A——a——em không biết——cảm giác nàyƯ——a—— đang cắm vào——vậy màƯ——sâu, quá——vậy màƯ——ưm」"
1020 = "「E, em sẽ chịu đựng——sẽ chịuƯ——hyu——chịu đựngƯ—— Vì——ngài SoutetsuƯ——cùng nhau——kư fưn!!」"
1041 = "「Vâ, vâng——ngài SoutetsuƯ——a——cứ thế—— nàyƯ——, cùng, nhauƯ——ưm」"
1074 = "「Dạ, dạ——ngài Soutetsu? Cô bé thì——ưm hưm——không cần——gel đâu ạƯ」"
1082 = "「Lần này, thì——em——ưm—— cho đến khi, ngài bắn ra——em sẽ——chịu đựngƯ」"
1096 = "「Thế nàyƯ——a——vẫn đang cắm, bên trongƯ——ưm hưm! A——sâu quá——kư ha a!」"
1121 = "「N, ngài Soutetsu——phu ya——cái nàyƯ—— tuyệt quá——kư hi i i ưm!」"
1129 = "「Ư!?」"
1131 = "「~~~~~~~~Ư!!!」"
1337 = "Rồi em cuộn ngón tay lại thành hình ống, và đâm mạnh ống tiêm vào trong đó——Ư!!?"
1549 = "Suzu dịu dàng ôm lấy tôi, nhẹ nhàng vuốt ve lưng tôi——Ư!!!?"
```

### 01_Hachiroku/ハチロクh5_おだいどこしごと.txt.toml — 6 dòng (lost-gasp-trailing: 6)

```toml
[script]
992 = "「A……mặc dù, cách lớp quần lót——ưm——hà——á——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」"
1031 = "「A——đến rồi——ưm! Á——a—— tinh dịch——nặng, quá——thế này——sướng quá——Ư!!」"
1064 = "「Phù á!? A! Không được——nếu ấn vào—— ưm——nữa——a, phù a——ưm ưm~~~Ư」"
1065 = "「Phù á!? Cái này!——Sướng quá—— ~~~~~~~~~~Ư!!!!」"
1401 = "Gần như sắp khóc nấc lên, Suzu lại một lần nữa run rẩy dữ dội——Ư!"
1416 = "Giọng nói thốt ra những lời đàng hoàng, nhưng lại cao vút lên vì phát tình. Đến mức đó sao, Suzu đang hưng phấn đến thế——Ư!!?"
```

### 01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 9 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 5)

```toml
[script]
775 = "「Nhưng mà, bây giờ chỉ có hai chúng ta thôi mà? Đâu cần thiết phải giấu núm vú ngay cả với tôi chứ——Ư!」"
873 = "「Ư!!」"
1008 = "「Vì——vậy, nhiều hơn nữa——những thứ……bên trong, ngài Soutetsu ——vào sâu hơn nữa——tất cả——em muốn, có——Ư!?」"
1080 = "「Ư!」"
1081 = "「Ư!!」"
1082 = "「Ư!!!!!」"
1083 = "「Ư!!?」"
1557 = "Chà xát núm vú bằng phần hông của cậu bé đang cương cứng, trượt mạnh qua khe hẹp giữa chiếc váy và bầu ngực——Ư!?"
1771 = "Sâu trong cổ họng Suzu khẽ giật, toàn bộ nước bọt và hơi thở trong miệng tôi bị hút mạnh đi——Ư!?"
```

### 01_Hachiroku/ハチロクh7_レトロモダンメイクラヴ.txt.toml — 11 dòng (lost-gasp-trailing: 3, raw-tsu: 7, lost-gasp-whole: 1)

```toml
[script]
477 = "「Ư——」"
804 = "「Ư!」"
807 = "「Ư!!!!!!!!!!」"
814 = "「Ư! （Ực）」"
974 = "「Ư!」"
975 = "「Ư!!」"
976 = "「Ư!!!」"
978 = "「Ư!?」"
1433 = "Tôi muốn cứ thế này mà chìm đắm mãi. Tôi muốn trở thành em bé của Suzu. Cái ham muốn ngu ngốc đó——Ư!?"
1444 = "Tôi không thể đút côn thịt vào tiểu huyệt quen thuộc một cách trơn tru. Suzu đang lên đỉnh thậm chí còn chẳng còn tâm trí để dẫn dắt tôi——Ư!!"
1842 = "（Làm gì có chuyện——đột nhiên chứ——Ư!）"
```

### 01_Hachiroku/ハチロクh8_桜色のひめごと.txt.toml — 8 dòng (lost-gasp-trailing: 6, raw-tsu: 1, lost-gasp-whole: 1)

```toml
[script]
467 = "「——Ư!!!!」"
749 = "「Iiiiiiiiiiiiiii~~~~~Ư!!!!」"
951 = "「Ư!」"
952 = "「Ư!!?」"
953 = "「ƯƯƯƯƯ~~~~~~~~~Ư!!!」"
1225 = "Quá sung sướng, muốn được sung sướng hơn nữa, toàn bộ cơ thể tôi đã khô khốc cả rồi——Ư!!?"
1274 = "Hiểu được những gì em nói, niềm sung sướng trong tôi chợt trào dâng mạnh mẽ——Ư!!?"
1276 = "Tràn ngập cảm giác thỏa mãn và thành tựu, tôi nằm yên bất động cho đến khi đường âm đạo đang co thắt nới lỏng ra——Ư!?"
```

### 01_Hachiroku/ハチロクh9_コノフクハキルコト.txt.toml — 30 dòng (raw-tsu: 25, lost-gasp-whole: 1, lost-gasp-trailing: 4)

```toml
[script]
1354 = "「Ư——」"
1868 = "「Xin ngài——hãy cùng nhau——ban cho em, tinh dịchƯ Em——đã——ưm, đến giới hạn, rồi, sắp!」"
1896 = "「Không cần, nhịn đâu——bắn ra, bắn ra điƯ. Em——cũng——em, sắp, sắp rồi!」"
2017 = "「A——không được, trốn đâuƯ——ưm——a, không được——đâu ạ——dương vật——của ngài SoutetsuƯ」"
2041 = "「Hyuua!! A——vào rồi! Vào rồi, a Ưm, a——không được——cái eo, em, lẳng lơ quáƯ」"
2046 = "「Hahi!? Hi——tuyệt quá——tuyệt, quá! Kyuhu! Em——đang bị, dương vậtƯ」"
2055 = "「Hà, hà——hà——hà—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」"
2082 = "「A——phù a——không được——đâu ạ——sức lực không còn——nữa rồiƯ——cơ thể——cứng đờ, mất rồi」"
2086 = "「A——a a——a a a——của ngài Soutetsu, em hiểu, rồiƯ——đang giật giật, đang nhịnƯ——ưm, a」"
2089 = "「A——vâng, vâng——đúng vậy, nhỉ, Ngài SoutetsuƯ——ưm——phù——phù a——a」"
2097 = "「Hàa——a——sướng, quá——a, ngon, ngon lắmƯ——ưm——dương vật——của ngài Soutetsu」"
2106 = "「A, ư……Đó——là——nơi đang—— vuốt ve, vuốt ve——ưm, dương vật——của ngài SoutetsuƯ」"
2109 = "「Hà! A! Thích quá! Thích quá! Ngài Soutetsu! Ngài SoutetsuƯ——phù, a——phu quânƯ」"
2144 = "「Ưm——phù——a——ưm, ư——ưm ư, Ngài Soutetsu——của ngài Soutetsu——dương vậtƯ」"
2151 = "「Ưm——xong, rồi. Của ngài Soutetsu, to quá—— Phù……a……chỉ lấy ra từ cửa sổ thôi——mà cũngƯ」"
2176 = "「Ưm ư——Ư——」"
2223 = "「Kyuu——ưm——a——a——chỗ này, thích lắm, dương vật, đang liếm, cô bé——của emƯ」"
2251 = "「Cô bé——ưm——đang bị ngài Soutetsu—— đâm thốc lên——đầy ắp, đầy ắp rồiƯ——」"
2319 = "「Cô bé——của em——phù, a, đang chảy——rất nhiều——nước dãi——thế nàyƯ」"
2329 = "「Em, sắp——ra. Rồi——nhé? Ngài SoutetsuƯ—— Ưm——ưm ư ư ư ư ư ư ư!!!」"
2428 = "「Đúng như――tôi mong muốnƯ」"
2588 = "「Suzu——tôi ra đâyƯ」"
2613 = "「Dương vật——ưm. Thật to——phù, a, phần——nhô ra——đã vào trong——cô bé, rồiƯ」"
2614 = "「Dương vật——của ngài SoutetsuƯ—— đến tận——bên trong——sâu nhất, của emƯ」"
2624 = "「Ư!」"
2625 = "「Ư!!!」"
2815 = "Không xong rồi, mất thăng bằng——Ư!!!?"
3131 = "Khi tôi gọi tên, Suzu buông lỏng toàn thân, giao phó tất cả cho tôi——Ư!?"
3250 = "Để làm dịu vẻ mặt bất an của Hachiroku, tôi lại ực thêm một ngụm bia vốn không quen uống——Ư!?"
3256 = "Những điều muốn nói, những điều muốn làm cho em——Ư!"
```

### 01_Hachiroku/仲国06_聖都とパンダとハチロクと.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1523 = "「Ư!!!」"
```

### 02_Hibiki/lr_日々姫h1_鏡の中日々姫.txt.toml — 14 dòng (lost-gasp-trailing: 5, lost-gasp-whole: 9)

```toml
[script]
1005 = "「Nếu ngón tay của Hibiki không đủ——thì sẽ thế nào——Ư!!」"
1049 = "「Fuya! A——chỗ đó——chỗ đó——Ư!!」"
1054 = "「Hể? Gương——a——gương—— Ư!!!!!!!?」"
1092 = "「Ư!」"
1093 = "「Ư!!」"
1094 = "「Ư!!!」"
1095 = "「Ư!!!!」"
1097 = "「Ư!!!!!!」"
1123 = "「Ư!!!?」"
1127 = "「Ư!!!!!!!!!!」"
1237 = "「Hibi, ki——Ư!」"
1291 = "「Ha——ha——ha——ha—— Anh hai——anh hai——Ư!」"
1331 = "「Ư!!」"
1338 = "「~~~~~~~~~~Ư!!!」"
```

### 02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml — 12 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 7)

```toml
[script]
675 = "——Dù vậy em ấy vẫn không làm một mạch. Lại chỉ ngậm mỗi phần đầu——Ư!!?"
691 = "……Dù có hơi tràn ra một chút, nhưng Hibiki vẫn uống cạn toàn bộ, không chừa lại giọt nào——Ư!"
972 = "「Ư!!!」"
1006 = "「Ư!!」"
1009 = "「Ư!!!!!」"
1010 = "「Ư!!!!!!」"
1013 = "「Ư!?」"
1038 = "「Hamu——reru——amu——chuu——hamu, Chu——famu——chuu——ưm——Ư!!!」"
1146 = "「Hibiki——Hibiki——cùng nhau, cùng nhau nhé——Ư!!!」"
1168 = "「Ha——a——gì, thế này——! ——Dù, dừng, lại ——thì——anh hai——chỉ cần, ở bên trong——thôi, là——Ư」"
1572 = "Vừa dứt lời, ánh mắt Hibiki bỗng trở nên dịu dàng——Ư!?"
1594 = "Phần đầu của tôi hôn lên sâu trong cổ họng Hibiki——Ư!!!?"
```

### 02_Hibiki/lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml — 45 dòng (lost-gasp-trailing: 3, raw-tsu: 40, lost-gasp-whole: 2)

```toml
[script]
933 = "「Ư――Ư――~~~Ư! ――A――hà, hà」"
1305 = "「Bây giờ, quy đầu của anh, đang chạm vào nơi sâu nhất trong âm đạo của Fukami―― chạm vào, cổ tử cung――Ư!!!?」"
1332 = "「Ư!!!!!」"
1338 = "「Ư!」"
1339 = "「Ư!! ~~~Ư――. Bắt đầu nhé, Hibiki.」"
1341 = "「Ư!!!!!」"
1342 = "「Ư!!!!?」"
1343 = "「~~~Ư!!!」"
1344 = "「~~~~Ư!!」"
1355 = "「Fua――a――Ư――a――a!!」"
1390 = "「Ư!?」"
1400 = "「Ư!!」"
1401 = "「Ư!!!」"
1402 = "「Ư!!!!」"
1403 = "「Ư!!!!!」"
1404 = "「Ư!!!!!!」"
1405 = "「Ư!!!?」"
1406 = "「Ư!!? ――A, ừm」"
1407 = "「Ư!!?」"
1408 = "「Ư!!? A――ưm――（Ực）―― A――! ――Hít, thở, hít, thở――」"
1409 = "「Ư!?」"
1410 = "「~~~~~~~Ư!!!!」"
1411 = "「~~~~~~~~Ư!!!」"
1412 = "「~~~~~~~~Ư!!!!!」"
1413 = "「~~~~~~~~~~~Ư!!!」"
1423 = "「A――Ư――a――hà――ưm」"
1431 = "「A――. ――――Ư――」"
1449 = "「!――Ư!――Ư!!?」"
1451 = "「Ư!!!」"
1452 = "「Ư!!!!」"
1453 = "「Ư!!!!!」"
1454 = "「Ư!!!!!!!!!!!」"
1455 = "「Ư!!?」"
1465 = "「Ư!!!!!!!!!」"
1481 = "「Vâng. Ừm――xin anh, hãy――Ư!!!!!!」"
1518 = "「Đau――gu~~~~~~~Ư!!!!!!」"
1777 = "「Quy đầu của, anh hai――phần đầu của, chim――Ư! Đang――hôn vào――tử cung, của em――」"
1784 = "「Ư!!!」"
1785 = "「Ư!?」"
1900 = "Thế nhưng, trong nháy mắt nó lại trở nên ngọt ngào. Chỉ vì Hibiki nở một nụ cười rạng rỡ――Ư!!?"
1968 = "Thật xấu hổ. Trước mặt em gái nuôi. Trước mặt Hibiki. Bị ép phải thú nhận rằng mình sắp xuất tinh rồ――Ư!?"
2226 = "Fukami chà đạp. Dùng chân chà đạp lên hạ bộ của tôi. Ngay trước mắt Hibiki――Ư!!?"
2230 = "Ánh mắt và giọng nói của Fukami rất kiên định. Thậm chí có cảm giác như em ấy đang rất quyết tâm. Vậy thì bây giờ, thay vì hỏi lý do, tốt nhất là cứ làm the――Ư!!?"
2316 = "Dứt quy đầu ra khỏi cổ tử cung đang bám chặt lấy rồi lại để nó mút vào. Mỗi lần lặp lại, những làn sóng khoái cảm lại càng lớn hơn――Ư!"
2318 = "Tô kín toàn bộ quy đầu bằng chất bôi trơn không chừa chỗ nào. Từ rãnh quy đầu đến mặt dưới, thực sự không chừa một chỗ nà――Ư!"
```

### 02_Hibiki/lr_日々姫真闇h1_三人家族.txt.toml — 24 dòng (raw-tsu: 21, lost-gasp-trailing: 3)

```toml
[script]
1042 = "「――Ư」"
1044 = "「――――Ư――Hà――ưm!!」"
1061 = "「…………。…………。…………（Ực）――。 ……Chị……cũng………………nhé?…………Ư」"
1439 = "「Hyu!!!? ~~~~~~~~~~Ư!!!!」"
1458 = "「~~~~~~~~Ư!!!」"
1496 = "「Hà…… a…… Sou, chan――Hii, chan――Ư」"
1508 = "「Ư!? Ư!? Ư!? Ư!!?」"
1525 = "「Ư!!!!!!!」"
1530 = "「A――ưm…… e~~~~~~~Ư」"
1551 = "「Ư! ――A――hia! A――ha!!」"
1552 = "「Ư!」"
1553 = "「A!」\\n「Ư!!!!!」"
1555 = "「A! Fua! A!!! Nguuuuu~Ư!!」"
1557 = "「Ư! ~~~~~………………. …………………………………………………Vâng!!!」"
1561 = "「Ư!!」"
1562 = "「Ư!!!」"
1563 = "「Ư!!!!」"
1564 = "「Ư!!!!!」"
1565 = "「Ư!!!!!!!!!」"
1566 = "「Ư!!!!?」"
1571 = "「~~~~~~~~~~~~~~~Ư!!!!!」"
1608 = "「Pua! A――. ƯƯ!!!!」"
1712 = "「Em! Em khao khát điều đó! ……Ư. ――――Ưm!!」"
1736 = "「Hibiki! Hibiki! Một chút nữa thôi――vì vậy! Ư! Anh sẽ――rót toàn bộ――tinh dịch――vào tử cung của Hibiki!」"
```

### 02_Hibiki/lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml — 29 dòng (raw-tsu: 28, lost-gasp-trailing: 1)

```toml
[script]
1114 = "「──Ư! Ư~~~Ư」"
1743 = "「Fua!? A── anh hai── nóng quá── ưm Hơn── mọi khi── nóng── và── to──Ư」"
1767 = "「Ư! Oa」"
1771 = "「Ư!!!!!!!!」"
1774 = "「Hà── a! Ư── ưm── ưm hưuuu」"
1786 = "「Hau! A! A! Aaa! Fua──Ư──ưm! Ưm uuuu!!!」"
1794 = "「Ư……a.」"
1833 = "「Ưm──Ư──ê──liếm──liếmmmmm」"
1871 = "「Vâng ạ! Mikuro, muốn thế ạ! Vì vậy, Mikuro── sẽ làm thế! ──Ư!!」"
1942 = "「Đúng vậy. Vào trong âm đạo đó── hự── thế này── đưa── dương vật cương cứng── vào──ƯƯƯ」"
1961 = "「Sao thế, Hibi──Ư!!!」"
2100 = "「Mi……kuro──Ư」"
2101 = "「Mikuro cũng── sẽ sớm. Cùng nhau, thôi── nhé ──Anh hai, chị, và──Ư──ba người, cùng nhau──」"
2104 = "「Miku, ro──Ư──hự──a──」"
2125 = "「Mikuro cũng, giống như Hibiki── hự── Thích, kiểu kích thích── này, nhỉ──Ư!!!」"
2148 = "「Mikuro đang, nhìn ạ── Mikuro──Ư──a── chị Hibiki, ──anh Soutetsu, cũng── rất, đẹp── ạ, ưm!」"
2180 = "「Nhưng nếu là Hibiki, người vợ của anh thì──Ư!」"
2250 = "「Ư──. Nhanh quá, cái đó, trông có vẻ mạnh bạo nhưng…… Anh Soutetsu, có bị đau, hay gì không ạ?」"
2292 = "「Ư!!」"
2293 = "「Ư!!!」"
2294 = "「Ư!!!!」"
2295 = "「Ư!!!!!」"
2321 = "「Ư!?」"
2322 = "「Ư!? Ưm……phu──phu──a──」"
2323 = "「Ư!? Anh hai.」"
2325 = "「Ư!!!?」"
2328 = "「~~~~~~~Ư」"
2655 = "Tôi đang tăng tốc. Tôi cảm thấy không ổn rồi. Cứ thế này thì tôi sẽ xuất tinh mất──Ư!!?"
2822 = "Chạm rồi. Tận sâu nhất của Mikuro. Dù không thể chứa hết toàn bộ dương vật cương cứng của tôi nhưng──Ư!!?"
```

### 02_Hibiki/グランドリライト03_日々姫.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
2428 = "「Bị kéo đi? ――Ư!?」"
```

### 02_Hibiki/日々姫01_リゾート食堂列車計画.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1603 = "「Ư!」"
```

### 02_Hibiki/日々姫01_双鉄の妹.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
2588 = "「Ư!!」"
2589 = "「Ư!?」"
```

### 02_Hibiki/日々姫02_文庫森.txt.toml — 4 dòng (lost-gasp-trailing: 2, lost-gasp-trailing-mid: 2)

```toml
[script]
1522 = "「Nhưng, khi một khung cảnh tuyệt vời đến thế này, dang phản chiếu trong đôi mắt của Hibiki——Ư!」"
1713 = "「Ê he~Ư! Ê he he~Ư! Anh vẽ \"âm vang\" (Hibiki) cho em đó hả!!」"
2051 = "「Anh hai, từ lúc nào mà anh lại——Ư!! Xin lỗi! Em xin lỗi!!?」"
2065 = "「Toa ăn—— Toa ăn á! Rào cản cao quá đi mất~~Ư!!」"
```

### 02_Hibiki/日々姫02_日々姫の日々.txt.toml — 4 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 1)

```toml
[script]
1992 = "「A... a~~Ư」"
2002 = "「Cơ mà! Việc có vẽ đẹp được hay không, lại là một chuyện hoàn toàn khác đấy nhé~Ư」"
2374 = "「Ư!」"
2376 = "「~~Ư!」"
```

### 02_Hibiki/日々姫03_客車手配.txt.toml — 3 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 1)

```toml
[script]
2322 = "「Anh nói cứ như thể không có việc gì thì không được đến tìm anh vậy á~~Ư」"
2427 = "「Á á!!?」\\n「Ư!!」"
2894 = "「Là điện thoại nhỉ, giờ này mà còn——Ư!?」"
```

### 02_Hibiki/日々姫03_湯富院.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
1933 = "「Ư！！」"
1963 = "「Ư!」"
2433 = "「～～Ư」"
```

### 02_Hibiki/日々姫04_カフェキッチン.txt.toml — 2 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 1)

```toml
[script]
1306 = "……Chị. Chị hai——Ư!?"
1909 = "「Ư!!!?」"
```

### 02_Hibiki/日々姫04_同乗.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
2215 = "「Ư……」"
2868 = "Nếu vậy thì, không cần cô ấy phải gánh vác một mình thêm nữa——Ư!?"
```

### 02_Hibiki/日々姫05_市議会見学.txt.toml — 7 dòng (lost-gasp-trailing: 4, raw-tsu: 2, lost-gasp-whole: 1)

```toml
[script]
1554 = "「……Ư」"
1878 = "「Nhưng mà——Ư!?」"
1945 = "「Ừ. Vì trên này ghi là 'Bài viết liên quan ở trang 3' mà——Ư!?」"
2202 = "「Thưa chủ tọa. Xin hãy lưu ý đến những phát ngôn không đúng quy định————Ư!?」"
2281 = "「Ư!」\\n「Ư!!?」"
2284 = "「~~~~Ư!!!」"
2744 = "Có lẽ tốt nhất là cứ làm theo lời Hachiroku, bình tĩnh đợi cơm——Ư!!?"
```

### 02_Hibiki/日々姫05_御一夜ステーションカフェ.txt.toml — 4 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 1)

```toml
[script]
2040 = "「Ôi chao. Thật không giống mình chút nào, đến nước này rồi còn vương vấn cái gì chứ——Ư!」"
2069 = "「Ư!」"
2967 = "Tròn xoe như quả bóng bay, cứ như thể bụng đang to ra vậy——Ư!!?"
3330 = "Và rồi tôi, sẽ tạo ra một cơn gió. Để một ngày nào đó khi Hibiki vỗ cánh——Ư!"
```

### 02_Hibiki/日々姫06_みくろ、来訪.txt.toml — 3 dòng (lost-gasp-whole: 2, raw-tsu: 1)

```toml
[script]
1986 = "「Ư!!?」"
2015 = "「Ư!」"
2035 = "「Ư!!」"
```

### 02_Hibiki/日々姫06_日々姫の決断.txt.toml — 2 dòng (raw-tsu: 2)

```toml
[script]
2489 = "「Ể!?」\\n「Hibiki? ——Ư!!」"
2942 = "「Ư!」"
```

### 02_Hibiki/日々姫07_たったひとりの宣戦布告.txt.toml — 4 dòng (raw-tsu: 4)

```toml
[script]
1949 = "「Chị ăn đây——Amu——Ư!!!」"
2166 = "「Ư」\\n「Ư!」"
2168 = "「Ư!!」"
2169 = "「Ư!!?」"
```

### 02_Hibiki/日々姫07_姉の想い。妹の想い.txt.toml — 5 dòng (lost-gasp-whole: 5)

```toml
[script]
1832 = "「Ư!」"
1833 = "「Ư!!!」"
1834 = "「Ư!!!!」"
1850 = "「Ư!!?」"
1900 = "「Chờ đã, Nagi!?」\\n「Ư!?」"
```

### 02_Hibiki/日々姫08_とれいん食堂.txt.toml — 6 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 3, lost-gasp-trailing-mid: 1)

```toml
[script]
2181 = "「Uuu~~Ư」"
2196 = "「Ư!」"
2201 = "「Ư!!!」"
2213 = "「Ư!!?」"
2783 = "「~~Ư! Xin cảm ơn quý khách đã sử dụng dịch vụ ạ!」"
2785 = "「~~~~~~~Ư」"
```

### 02_Hibiki/日々姫08_開きかけのつぼみ.txt.toml — 5 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 2)

```toml
[script]
1731 = "「……Ư」"
2052 = "「Hả? A, a ha ha ha ha ha ha! Cái đó, là hiểu lầm! Chắc chắn là em ấy đang hiểu lầm cực kỳ nghiêm trọng luôn~Ư」"
2399 = "「Ư!」"
2400 = "「Ư!!?」"
3073 = "Bên trên bầu ngực, yết hầu trắng ngần cùng xương quai xanh chuyển động lên xuống. Cứ như thể em ấy vừa nuốt nước bọt vậy――Ư!"
```

### 02_Hibiki/日々姫09_run_with_our_dreams.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
1778 = "「Ư!!?」"
2478 = "Tôi gật đầu. Tôi cũng vậy. Cả anh Tochigi, cả anh Kimoto cũng vậy――Ư!!"
```

### 02_Hibiki/日々姫09_静かなる開戦.txt.toml — 7 dòng (lost-gasp-trailing: 2, raw-tsu: 2, lost-gasp-whole: 3)

```toml
[script]
1459 = "「Bảo là di chuyển cùng lúc nhiều toa xe, chứ Đường sắt Ohimitera đâu cần nhiều toa xe đến thế——Ư!」"
1558 = "「HyaƯ」"
1579 = "「Phù~, sống lại rồi~~Ư」"
1604 = "「Báo à? ——Ư」"
1918 = "「Ư!」"
1919 = "「Ư!!!」"
1920 = "「Ư!?」\\n「Ư!!」"
```

### 02_Hibiki/日々姫10_稀咲の未来図、日々姫の未来図.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
2940 = "「Ư!」"
3390 = "Vẫn giữ nguyên tư thế đó——\\ Tôi cố gắng suy nghĩ, tìm kiếm xem có cách nào không——Ư!!?"
```

### 02_Hibiki/日々姫11_御一夜モザイク.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1952 = "「Ừ.\\ ——Ư!!?」"
```

### 02_Hibiki/日々姫13_討論会.txt.toml — 3 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 1)

```toml
[script]
1304 = "「Oa a a a a~Ư」"
1703 = "「Ư!」"
2251 = "Và rồi con bé thoăn thoắt vẽ thứ gì đó――Ư!!"
```

### 02_Hibiki/日々姫14_投開票.txt.toml — 10 dòng (lost-gasp-trailing: 6, lost-gasp-whole: 4)

```toml
[script]
1714 = "「A――Cái đó――Auuuu~Ư!」"
1729 = "「Vâng――sẽ mãi mãi――Ư!!」"
1824 = "「Từ, từ đêm qua sao!? Từ đêm qua nghĩa là――Hauu~Ư!」"
2166 = "「Nếu vậy, em cũng thế. Anh hai――Ư!」"
2193 = "「Ư!」"
2194 = "「Ư!!!!」"
2195 = "「Ư!!?」"
2196 = "「Ư!?」"
2967 = "Tôi có thể nhìn thấy trần nhà. Nói cách khác là tôi đã ngã xuống――Ư!?"
3052 = "Đầu tiên tôi sẽ lên \\x%l運転台;#00ffc040;buồng lái%l;#;――Ư!?"
```

### 02_Hibiki/日々姫16_夢を乗せて.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
2683 = "Lịch trình á. Tại vì, hội nghị vừa mới bế mạc xong mà——Ư!!?"
```

### 02_Hibiki/日々姫h1_マッサージの続き.txt.toml — 6 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 3)

```toml
[script]
1011 = "「Ơ, xin lỗi——Ư!?」"
1230 = "「Ư!」"
1231 = "「Ư!!!」"
1232 = "「Ư!!?」"
1237 = "「~~~~~~Ư!!」"
1670 = "Đôi mắt Hibiki cong lên thành hình vòng cung đầy vẻ vui sướng——Ư!?"
```

### 02_Hibiki/日々姫h2_洗って大丈夫なスーツ.txt.toml — 3 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 1)

```toml
[script]
1085 = "「Ê hê hê, anh hai~Ư」"
1086 = "「Ê hê hê~Ư」"
1283 = "「Ư!?」"
```

### 02_Hibiki/日々姫h3_汚れてしまった制服で.txt.toml — 2 dòng (raw-tsu: 1, lost-gasp-whole: 1)

```toml
[script]
1262 = "「Ư!」"
1264 = "「Ư!?」"
```

### 02_Hibiki/日々姫h4_いもうとタオル.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
1182 = "「Ư!」"
1183 = "「Ư!!?」"
```

### 02_Hibiki/日々姫h5_白濁絵の具の射精会.txt.toml — 11 dòng (lost-gasp-trailing: 8, lost-gasp-whole: 3)

```toml
[script]
1180 = "「Phù――a! Anh hai――anh hai~Ư!!!」"
1351 = "「Anh hai~ Anh hai~~Ư」"
1359 = "「Ư!」"
1360 = "「Ư!!」"
1361 = "「Ư!!!」"
1364 = "「~~~Ư!」 "
1365 = "「~~~~~Ư」"
1368 = "「~~~~~~~~~~Ư!!!」"
1825 = "Giọng nói dễ thương――Tôi không ngờ cổ họng mình lại thốt ra âm thanh cao vút hệt như tiếng rên rỉ của Hibiki――Ư!!?"
1899 = "Vừa xuất tinh tôi vừa ấn sâu vào miệng em ấy――Ư!!?"
1963 = "Đang tăng tốc. Tăng tốc theo một đường thẳng, đẩy mọi thứ đến giới hạn cuối cùng――Ư!?"
```

### 02_Hibiki/日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 7 dòng (lost-gasp-trailing: 5, lost-gasp-whole: 2)

```toml
[script]
1418 = "「――Ư」"
2241 = "「A――ư ư ư~~Ư」"
2759 = "「Ư!」"
2761 = "「Ư!!?」"
2982 = "Trong lúc đó, những người tham gia khác, đã lần lượt lấy phong bì và mở ra――Ư!!?"
3414 = "Hibiki móc ngón tay vào cổ áo, kéo nhẹ xuống một chút. Khe ngực mỏng manh và độ phồng của bầu ngực liền phơi bày ra toàn bộ――Ư!"
3421 = "Hibiki rướn người tới trước――Ư!!?"
```

### 03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml — 16 dòng (lost-gasp-trailing-mid: 1, lost-gasp-trailing: 9, lost-gasp-whole: 6)

```toml
[script]
705 = "「——Ư」"
997 = "「Hya――~~Ư!!!!!」"
998 = "「Kíuphù!!!? ~~~~~~~Ư!!!!」"
1005 = "「Hia! A——ư——～～～～～Ư! Nhưng mà——thế này——cứ đâm lút cán là——em lại không kiềm được tiếng rên.」"
1014 = "「Á～～～～～～～Ư!!!」"
1035 = "「Ế～～Ư」"
1044 = "「Ư! Ư! Ư! ～～～～～Ư!!!」"
1045 = "「Ư!!! ～～～Ư!! Ư——a——ư!!!」"
1046 = "「～～～～～～～～～～～～～～～～～～Ư!!!」"
1061 = "「A——ha——a——ưm——Góc độ—— Nữa đi——sâu hơn nữa——dựng thẳng lên——Ư」"
1077 = "「Ư! ――Paulette」"
1078 = "「Ư!」"
1079 = "「Ư!!」"
1080 = "「Ư!!!」"
1083 = "「Chụt——ưm——chụụt——chụt——rộp—— rộp——rột——rột——chụt——Ư!?」"
1196 = "「Paulette——Ư!」"
```

### 03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml — 8 dòng (lost-gasp-trailing: 6, lost-gasp-whole: 2)

```toml
[script]
1009 = "「Kíuphù!? Ưm! Khoan đã! Bình tĩnh——a——bình tĩnh lại đi——anh Soutetsu——Ư!」"
1044 = "「Ư!!!?」"
1064 = "「Ư!!!」"
1070 = "「～～Ư」"
1124 = "「Ưm kyuu!! Ưm～～～～～～～～～～～Ư!!」"
1236 = "「Trần truồng sao? Không phải——Ư!!!?」"
1558 = "Trong khoảnh khắc, Paulette dừng mọi chuyển động——Ư!!!?"
1597 = "Cuối cùng, cuối cùng cũng được em ấy ngậm lấy rồi! Cảm giác thỏa mãn, thành tựu và an tâm——Ư!!!?"
```

### 03_Paulette/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 13 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 8)

```toml
[script]
1597 = "「Ư!!!」"
1816 = "「Bụ, ng——bụng, dưới——âm, đạo——chật, quá ——chật ních——em, bị nhét đầy, mất——Ư!」"
1894 = "「Ư!!!!」"
1895 = "「Ư!!!!!!!」"
1896 = "「Ư!!!!!!!!!!!」"
1897 = "「Ư!!!?」"
1906 = "「～～～～Ư!!!」"
1908 = "「～～～～～Ư!!」"
2135 = "Cảm giác ngực vừa bị ấn nhẹ——Ư!?"
2178 = "Tôi biết. Tôi cảm nhận được. Cửa tử cung của Paulette cũng đang khao khát tinh dịch của tôi. Mỗi lần đâm vào nơi sâu nhất, nó lại khẽ khàng mút lấy một cách ngọt ngào——Ư!"
2309 = "Cửa tử cung của Kisaki hút lấy quy đầu một cách mãnh liệt. Như muốn nuốt trọn toàn bộ tinh dịch của tôi——Ư!!"
2349 = "Siết chặt. Bàn tay phải của Paulette túm chặt lấy ga giường——Ư!"
2501 = "（Ra là vậy, đây chính là—— làm tình ba người sao——Ư!!?）"
```

### 03_Paulette/れいな02_れいなとポーレット.txt.toml — 3 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 1)

```toml
[script]
1948 = "「Vâng ạ~, tất nhiên là cực kỳ thích——Ư」"
2199 = "「Ư!」"
2388 = "Khi nghe Reina kể về \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp, tôi cũng có cảm nghĩ y hệt như vậy——Ư!"
```

### 03_Paulette/グランドリライト04_ポーレット.txt.toml — 5 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 3)

```toml
[script]
1317 = "「……Ừm. Cài xong rồi. Chắc chắn là rất hợp với Paulette——Ư!?」"
1815 = "「Ư!!!」"
1817 = "「Ư!?」\\n「Hyaa!!?」"
1860 = "「Ư!」"
2949 = "Đôi mắt xanh biếc hơi ngấn lệ. Cô ấy bước một bước lớn lại gần tôi——Ư!?"
```

### 03_Paulette/ポーレット01_ポーレット退任.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1635 = "「Uyuu~Ư」"
```

### 03_Paulette/ポーレット01_御一夜探し.txt.toml — 2 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 1)

```toml
[script]
1606 = "「Mogyuuuu~~~Ư」"
1947 = "「Ư!」\n「——Ư」"
```

### 03_Paulette/ポーレット02_古地図.txt.toml — 3 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 2)

```toml
[script]
1638 = "「Ra là vậy. ——Ư!?」"
2172 = "「Ư!」"
2173 = "「Ư!!!」"
```

### 03_Paulette/ポーレット02_解放b寝台.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1779 = "「Ư!?」"
```

### 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml — 3 dòng (lost-gasp-trailing: 3)

```toml
[script]
1583 = "「Phù…… a~Ư」"
1590 = "「Phù~Ư」"
2326 = "Ồ, vào đường hầm rồi sao.\nHơi có mùi khói——Ư!"
```

### 03_Paulette/ポーレット03_廃炭鉱.txt.toml — 2 dòng (raw-tsu: 1, lost-gasp-whole: 1)

```toml
[script]
1345 = "「Ư///////!」"
2155 = "「Ư!!!」"
```

### 03_Paulette/ポーレット04_ヒヤリング.txt.toml — 4 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 3)

```toml
[script]
1461 = "「Hơiiiiii~Ư」"
1838 = "「Ư!」"
1839 = "「Ư!!!!!」"
1840 = "「Ư!!?」"
```

### 03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1836 = "「A…… ưm…… hơ——. Ừm thì——a… i… a…… to——ưm ưm~Ư」"
```

### 03_Paulette/ポーレット05_whatsentertainment.txt.toml — 4 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 2)

```toml
[script]
1337 = "「Chậc! Anh hai chẳng có gì đáng để trêu chọc cả nha~Ư」"
1632 = "「Ư!!?」"
1633 = "「Ư!?」"
2083 = "Có lẽ do trà quá nóng, mà khuôn mặt của Paulette đỏ bừng——Ư!!!"
```

### 03_Paulette/ポーレット05_鳴呼の町.txt.toml — 2 dòng (lost-gasp-trailing: 2)

```toml
[script]
1252 = "「——Ư」"
2613 = "Với lời giải thích đó, cho đến khi tôi ra khỏi đoạn đường đóng đường, Hikari tuyệt đối sẽ không leo lên——Ư!!!?"
```

### 03_Paulette/ポーレット06_おひとよマイントレジャー.txt.toml — 4 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 3)

```toml
[script]
1800 = "「Ra vậy. Nếu thế thì sẽ phá sản thật sao. Tin đồn sẽ biến thành sự thật mất――Ư!」"
2207 = "「Ư!」"
2208 = "「Ư!!」"
2209 = "「Ư!!!」"
```

### 03_Paulette/ポーレット06_雪の宿.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1841 = "「Ư!?」"
```

### 03_Paulette/ポーレット07_うさぎ.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1719 = "「Oa oa oa oa oa~Ư Mẹ ơi, bé thỏ, bé thỏ, hu hu hu~」"
```

### 03_Paulette/ポーレット07_支線.txt.toml — 3 dòng (lost-gasp-whole: 3)

```toml
[script]
2034 = "「Ư!」"
2035 = "「Ư!」\\n「A」"
2037 = "「Ư!!」"
```

### 03_Paulette/ポーレット08_未来へのレール.txt.toml — 2 dòng (lost-gasp-trailing: 2)

```toml
[script]
1482 = "「——Ư」"
2914 = "Vạt áo khoác bị kéo. Quay lại, là Hikari——Ư!!!"
```

### 03_Paulette/ポーレット08_線から面へ.txt.toml — 5 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 2)

```toml
[script]
1520 = "「Hửm~Ư?」"
1529 = "「Vẻ bề ngoài, ảnh hưởng lớn đến khách hàng lắm đó nha~Ư!」"
1827 = "「Ư!」"
1828 = "「Ư!!」"
2073 = "Tôi đang mải nhìn hành khách, cũng vội vàng hướng mắt về phía trước――Ư!"
```

### 03_Paulette/ポーレット09_ストーブ客車.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1670 = "「Nhưng mà, nói đi cũng phải nói lại, thế này thì sớm quá――Ư!!?」"
```

### 03_Paulette/ポーレット10_見えない傷.txt.toml — 2 dòng (lost-gasp-trailing: 2)

```toml
[script]
1036 = "「……Suuu~……Suyaaa~~Ư」"
1844 = "\"Dừng lại đi, dừng lại đi, dừng lại đi, dừng lại đi. Đừng mang tên con ra, đừng gọi tên con rồi cãi nhau nữa――Ư\""
```

### 03_Paulette/ポーレット11_記憶と記録.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1368 = "「Hauuu~Ư」"
```

### 03_Paulette/ポーレット12_解放.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1337 = "Sự im lặng. Dài――quá dài. Đến mức người nghe ở đầu dây bên này là tôi cũng ngày càng thấy bất an……Ư!?"
```

### 03_Paulette/ポーレット13_再評価.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
1831 = "Như muốn nói 'Chết dở rồi nè!', Nagi lấy hai tay bịt chặt miệng lại——Ư!?"
```

### 03_Paulette/ポーレット15_求人難.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1543 = "「À……tờ rơi tuyển dụng trên báo sao—— Hửm, không lẽ Paulette đã——Ư!?」"
```

### 03_Paulette/ポーレット16_明日へのレール.txt.toml — 2 dòng (lost-gasp-trailing: 1, raw-tsu: 1)

```toml
[script]
2260 = "「Quả thật. Thời kỳ đó có rất nhiều khu nhà ở công cộng thế này mà. A xem kìa, hoài niệm thật. Mặc tạp dề đi mua sắm——Ư!?」"
3330 = "Hiếm lắm mới có người mang đậm phong thái Hinomoto cổ kính và tốt đẹp đến nhường ấy——Ư!"
```

### 03_Paulette/ポーレットh1_ファーストセックス.txt.toml — 6 dòng (lost-gasp-whole: 4, lost-gasp-trailing: 1, raw-tsu: 1)

```toml
[script]
983 = "「Ư!」"
984 = "「~Ư!」"
988 = "「Ư!」"
995 = "「Ư!!!」"
1007 = "「Ư!」"
1015 = "「Liếm——ưm——chụt——chùn chụt——ưm~Ư」"
```

### 03_Paulette/ポーレットh2_制服変更？.txt.toml — 5 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 3)

```toml
[script]
950 = "「Hya un!? B, bẩn lắm——bởi vì, có nước tiểu——ưm——Soutetsu, này——Ư!」"
952 = "「Ư!」"
985 = "「Á——Ư!」"
1004 = "「Ư!!?」"
1135 = "「~~~~~~~~Ư!!!」"
```

### 03_Paulette/ポーレットh3_誘惑アイスコーヒー.txt.toml — 6 dòng (lost-gasp-whole: 2, raw-tsu: 4)

```toml
[script]
907 = "「Ư!」"
908 = "「Ư!」"
934 = "「Ư!」"
935 = "「Ư——」"
954 = "「Ư!」"
1639 = "（Ư!?）"
```

### 03_Paulette/ポーレットh4_クリーム＆クリーム.txt.toml — 3 dòng (lost-gasp-trailing: 2, raw-tsu: 1)

```toml
[script]
941 = "「Ư!」"
1030 = "「～～～～～～～～～Ư!!」"
1632 = "（Cái này……thì——sướng quá—— Đến mức——đầu óc——cũng nổi bọt——mất thôi——Ư）"
```

### 03_Paulette/ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml — 5 dòng (lost-gasp-trailing: 1, raw-tsu: 3, lost-gasp-whole: 1)

```toml
[script]
904 = "「Ư!」"
905 = "「Ư!」"
935 = "「Ư!!!」"
953 = "「Ư!」"
1228 = "Dù bị siết chặt đến nhường này, nhưng phần thịt của Paulette lại quá mềm mại——Ư!"
```

### 03_Paulette/ポーレットh6_あなたとふたりの学園エッチ.txt.toml — 10 dòng (lost-gasp-trailing: 6, lost-gasp-whole: 3, raw-tsu: 1)

```toml
[script]
774 = "「Ư!!?」"
784 = "「Phù——ưm——chụt——chụt——ưm—— Anh Sou, tetsu——ưm——em——cũng——Ư!!!!」"
790 = "「Phù, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」"
814 = "「Ư!」"
816 = "「A! ——Ư!?」"
817 = "「Ư!!」"
819 = "「Ư!?」"
1271 = "Dồn hết sức đẩy hông tới, đúng lúc đó Paulette cũng giật nảy mình run rẩy——Ư!?"
1290 = "Nên tôi hôn ngọt ngào lên tử cung, để nói cho nó biết tôi là ai——Ư!?"
1377 = "Sau đó, cái miệng đáng yêu hé mở. Như muốn khoe khoang rằng em đã nuốt hết rồi, hãy khen em đi——Ư!"
```

### 03_Paulette/ポーレットh7_残業エッチもyシャツで.txt.toml — 5 dòng (lost-gasp-trailing: 5)

```toml
[script]
1233 = "Thêm vào đó, phần thân bị kẹp chặt giữa bầu ngực ướt đẫm, nếu lơ là, tôi có thể xuất tinh ngay lập tức——Ư!?"
1271 = "Khó chịu lắm phải không. Cứ thế mà kích thích——Ư!?"
1285 = "Việc làm cô ấy lên đỉnh khiến tôi rất mãn nguyện, nhưng cảm nhận được sự cựa quậy đó lại càng kích thích khao khát xuất tinh——Ư!?"
1331 = "Bị nhét ngón tay vào lỗ hậu lần nữa, Paulette run lên bần bật——Ư!!"
1380 = "Nên tôi áp sát hết sức, và vò nát bầu ngực của Paulette——Ư!?"
```

### 03_Paulette/ポーレットh8_気動車の国のアリス.txt.toml — 7 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 2)

```toml
[script]
2147 = "「Ư!」"
2148 = "「Ư!!?」"
2183 = "「Ủa ủa? Sao thế? A! Nóng quá hả? Xin lỗi nhé? Em không để ý. Phù~ phù~Ư」"
2252 = "「Ư!!」"
2253 = "「Ư!!?」"
2254 = "「Ư!?」"
3150 = "Ngón cái và ngón trỏ siết chặt lấy dương vật. Vì đau, tôi bất giác định lùi eo lại——Ư!"
```

### 04_Reina/lr_れいなh1_レディ・れいな.txt.toml — 8 dòng (lost-gasp-whole: 6, lost-gasp-trailing: 2)

```toml
[script]
904 = "「——Ư」"
1258 = "「Ư!!!」"
1282 = "「Ư!!!!」"
1431 = "「Ư!!!」"
1432 = "「Ư!!!!」"
1433 = "「Ư!!!!!!」"
1434 = "「Ư!?」"
1440 = "「~~~~~~~~~~~~~~Ư!!!!」"
```

### 04_Reina/lrれいな追加02_花嫁修業の先生たち.txt.toml — 3 dòng (raw-tsu: 2, lost-gasp-trailing: 1)

```toml
[script]
1339 = "「Ừm. ——Ư!」"
1363 = "「Hửm?——Ư!!!!!!」"
1885 = "Làm theo chỉ thị dời chiếc bàn trà hình tam giác và sofa đi, Kisaki liền nhanh nhẹn trong khoảng thời gian đó——Ư!"
```

### 04_Reina/lrれいな追加03_れいなとのレール.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
1079 = "「Ư——」"
```

### 04_Reina/lrれいな追加h_夜の花嫁修業.txt.toml — 10 dòng (raw-tsu: 7, lost-gasp-trailing: 3)

```toml
[script]
727 = "「——Ư!!!!!」"
1233 = "「Khóa học, làm dâu, của——Ư——thành quả——hơn cả mong đợi, tuyệt vời, quá——. Ưm!」"
1321 = "「Nếu vậy thì——nhiều hơn nữa——Ư!」"
1331 = "「Ư!!!」"
1332 = "「Ư!!!! ——A hự!」"
1335 = "「~~~~~ƯƯƯ」"
1337 = "「~~~~~~~~Ư!!!」"
1475 = "Ư!"
1572 = "Tôi không hề nhận ra. Reina đang dùng tay bao lấy quy đầu, và hứng lấy toàn bộ tinh dịch——Ư!?"
1923 = "（Là do lỗ hậu đang bị kích thích sao……Ư—— Một kích thích đơn thuần lên dương vật thôi mà lại mạnh gấp mấy lần bình thường——）"
```

### 04_Reina/れいな01_炭鉱探索.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
2035 = "「Ư!」"
```

### 04_Reina/れいな02_れいなとポーレット.txt.toml — 3 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 1)

```toml
[script]
1948 = "「Vâng ạ~, tất nhiên là cực kỳ thích——Ư」"
2199 = "「Ư!」"
2388 = "Khi nghe Reina kể về \\x%l列車;#00ffc040;đoàn tàu%l;#; hỗn hợp, tôi cũng có cảm nghĩ y hệt như vậy——Ư!"
```

### 04_Reina/れいな03_しゅっぱつしんこう.txt.toml — 5 dòng (lost-gasp-trailing-mid: 1, lost-gasp-trailing: 1, lost-gasp-whole: 3)

```toml
[script]
1395 = "「Ể~Ư... Người khác là sao chứ, tự nhiên lại...」"
1631 = "「Paulette! Thế này là――――Ư!?」"
1766 = "「Ư!!?」"
1767 = "「Ư!?」"
2432 = "（Ư!）"
```

### 04_Reina/れいなh1_おかあさんのレッスン.txt.toml — 5 dòng (lost-gasp-whole: 4, lost-gasp-trailing: 1)

```toml
[script]
1323 = "「Ư!!」"
1346 = "「Ư!」"
1348 = "「Ư!!?」"
1349 = "「Ư!?」"
1574 = "「~~~~Ư!」"
```

### 04_Reina/れいなh2_おもらし防止大作戦.txt.toml — 4 dòng (lost-gasp-whole: 3, lost-gasp-trailing: 1)

```toml
[script]
1031 = "「Ư!」"
1070 = "「Ư!」"
1071 = "「Ư!!」"
1215 = "「~~~Ư!」"
```

### 04_Reina/れいなh3_おもらし自由化大作戦.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
1074 = "「Ư!」"
1080 = "「Ư!!!?」"
1099 = "「Nmu——mu——uuuuuuu~~~~Ư!」"
```

### 04_Reina/れいなh4_ふたりっきりのハロウィン.txt.toml — 5 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 3)

```toml
[script]
1963 = "「Ư!!!」"
1990 = "「Hauuuu~Ư!!」"
2022 = "「Ư!」"
2972 = "Hút sạch cho đến những giọt nước tiểu cuối cùng——Ư!?"
3095 = "Reina xoay người lại và cúi xuống, cái mông đáng yêu lộ ra hoàn toàn——Ư!!?"
```

### 04_Reina/グランドリライト05_れいな.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1881 = "「Ư!?」"
```

### 05_Mayami/lr_真闇h1_僕のおねえちゃん.txt.toml — 16 dòng (lost-gasp-trailing: 9, lost-gasp-whole: 7)

```toml
[script]
1163 = "——Miệng chị ấy há hốc cứng đờ thành hình chữ 'A'. Hít một hơi, rồi nín bặt——Ư!"
1495 = "「Ư!!!」"
1496 = "「Ư!!!!!!!!」"
1497 = "「Ư!!?」"
1519 = "「Ừ. Được mà. Sou-chan——Ư!!」"
1575 = "「Dương vật của Sou-chan ngốc nghếch quá nhỉ~. Vậy thì nhé? Chị sẽ dạy cho em——Ư!」"
1607 = "「Em hiểu rồi. Em sẽ dừng lại——hôm nay——chị Mayami——Ư!!」"
1699 = "「Ư!!」"
1700 = "「Ư!!!!」"
1701 = "「Ư!!!!!」"
1702 = "「Ư!!!?」"
1706 = "「~~~~Ư!!!」"
1709 = "「~~~~~~~~~~Ư!!!」"
1797 = "Ra vậy, nếu cứ tiếp tục nhắc đến chuyện này thì đúng là quá kém tinh tế. Nếu vậy, nơi nên chạm vào tất nhiên là——Ư!?"
1828 = "Bầu ngực trượt mạnh sang một bên, phần đỉnh dương vật bị ném ra ngoài và trở nên lạnh lẽo. Cảm giác hụt hẫng ập đến bất ngờ——Ư!!?"
1915 = "Khoảnh khắc nhìn thấy, toàn bộ công việc đang làm dở đều bay biến sạch. Nghe nói là đồ lót, nhưng mà ngực và cả chỗ đó đều phơi bày hết ra rồi kìa——Ư!"
```

### 05_Mayami/lr真闇追加01_新婚旅行のリクエスト.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
1077 = "「Ư!」"
1657 = "Reina lại hứng thú với một chủ đề không ngờ tới. Chị Mayami như chỉ chờ có thế——Ư!"
```

### 05_Mayami/lr真闇追加02_御一夜新婚旅行.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1835 = "Nâng chiếc cốc lên, đưa thẳng vào miệng——Ư!!"
```

### 05_Mayami/lr真闇追加03_ブルートレインの夜.txt.toml — 2 dòng (lost-gasp-whole: 2)

```toml
[script]
1120 = "「Ư!」"
1121 = "「Ư!!!!」"
```

### 05_Mayami/lr真闇追加h_赤ちゃん、欲しか.txt.toml — 9 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 6)

```toml
[script]
1016 = "\"「Không được, đâu——Sou, chan—— Trêu chọc——hư hỏng——như thế, là——Ư!」\""
1108 = "\"「Ư!!」\""
1125 = "\"「Ư!」\""
1128 = "\"「Ư!!!」\""
1129 = "\"「Ư!!!!!」\""
1130 = "\"「Ư!!!!!!!!!!!!」\""
1141 = "\"「Ư!!!!」\""
1254 = "\"「Của Sou-chan——ưm——phù——em bé, của—— Chị——sẽ——trở thành——mẹ——Ư!!」\""
1542 = "Cô đặc, hình như em vừa nghe thấy từ đó. Em cứ tưởng là sẽ được vắt kiệt chứ——Ư!"
```

### 05_Mayami/グランドリライト07_真闇.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
2579 = "\"「Đúng vậy. Hay là làm cho hoành tráng luôn, \\x%l編成;#00ffc040;ghép%l;#; cả toa phát điện và xe đông lạnh vào——Ư!!」\""
```

### 05_Mayami/真闇01_再蒸留.txt.toml — 2 dòng (raw-tsu: 2)

```toml
[script]
1800 = "「Ư!」"
1801 = "「Ư!!?」"
```

### 05_Mayami/真闇02_精髄.txt.toml — 2 dòng (lost-gasp-whole: 1, raw-tsu: 1)

```toml
[script]
2060 = "「Ư!!」"
2061 = "「Ư!?」"
```

### 05_Mayami/真闇03_ひとしずく.txt.toml — 9 dòng (lost-gasp-trailing: 6, lost-gasp-whole: 3)

```toml
[script]
1484 = "「Không có chi――Ư!」"
1565 = "「Ra là vậy, há miệng chờ sung――Ư!!?」"
1621 = "「Hửm? ――Ư!」"
1995 = "「Ư!」"
1996 = "「Ư!!!」"
1997 = "「Ư!!?」"
2675 = "Vậy thì, cả chị Mayami cũng? Nhưng…… thái độ như vậy, chưa một lần nào――Ư!"
2713 = "Rõ ràng là do tôi bảo anh ấy làm vậy, nhưng sự thật là tôi vẫn――Ư!!?"
2746 = "（Suỵt~Ư）"
```

### 05_Mayami/真闇h1_長期熟成.txt.toml — 4 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 2)

```toml
[script]
1181 = "「Đau――~~~~~Ư!!」"
1218 = "「Chị Mayami, làm gì――Ư!?」"
1272 = "「Ư!」"
1273 = "「Ư!!?」"
```

### 05_Mayami/真闇h2_無濾過.txt.toml — 7 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 4)

```toml
[script]
827 = "「――Ư!?」"
1158 = "「Đã bảo là, với tôi thì――Ư!」"
1208 = "「Ư!」"
1209 = "「Ư!!!」"
1210 = "「Ư!!?」"
1211 = "「Ư!?」"
1213 = "「~~~~~~~~Ư!!!」"
```

### 05_Mayami/真闇h3_補習授業の廃校舎.txt.toml — 8 dòng (raw-tsu: 2, lost-gasp-whole: 3, lost-gasp-trailing: 3)

```toml
[script]
1554 = "「……Ư」"
2694 = "「Nóng quá――Ư――tuyệt, quá――fua, á―― á――dương, vật――trong bụng――toàn bộ!」"
2889 = "「Ư!」"
2890 = "「Ư!!」"
2891 = "「Ư!!?」"
3114 = "Toàn bộ tinh dịch, đều đã được chị Mayami nuốt trọn――Ư!?"
3264 = "Cuối cùng, ngón tay, cũng chịu chạm vào, nhưng lại là tinh hoàn――Ư!?"
3965 = "Toàn bộ quy đầu đã được nuốt trọn, nhưng tốc độ vẫn không tăng lên. Cứ từ từ, chầm chậm, chìm dần vào trong miệng chị Mayami――Ư!?"
```

### 06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml — 13 dòng (lost-gasp-trailing: 8, lost-gasp-whole: 4, raw-tsu: 1)

```toml
[script]
1000 = "「~~~~Ư!」"
1001 = "「Ư!!」"
1003 = "「~~~~~~~~Ư!!!!」"
1020 = "「ƯƯƯƯƯ!? Đau quá――――――――」"
1029 = "「Ư!!」"
1030 = "「Ư!!!」"
1039 = "「Ư!?」"
1291 = "「Cảm ơn nhé, nhưng――Ư!」"
1341 = "Khoái cảm thể xác cưỡng ép mà bản thân không thể kiểm soát nhịp độ!! Cổ họng tự động mở ra, não bộ bị lắc lư chao đảo――Ư!"
1425 = "Âm thanh sung sướng tự động trào ra khỏi cổ họng, tôi vội vàng nuốt lại――Ư!!!!?」"
1429 = "Vừa định chồm tới đè cô ấy xuống thì mất thăng bằng, lúc đó tôi mới nhớ ra là hai tay mình đang bị trói――Ư!!!"
1551 = "Hơi ấm, niêm mạc, nước bọt sền sệt của Kisaki đang làm sụp đổ mọi suy nghĩ trong tôi. Giờ đây tôi chỉ khao khát được xuất tinh một cách sướng nhất――Ư!"
1619 = "Toàn bộ quy đầu bị nuốt chửng. Sự chật chội và nóng rực từ âm đạo của Kisaki truyền đến càng thêm mãnh liệt――Ư!!"
```

### 06_Kisaki/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 13 dòng (lost-gasp-whole: 5, lost-gasp-trailing: 8)

```toml
[script]
1597 = "「Ư!!!」"
1816 = "「Bụ, ng——bụng, dưới——âm, đạo——chật, quá ——chật ních——em, bị nhét đầy, mất——Ư!」"
1894 = "「Ư!!!!」"
1895 = "「Ư!!!!!!!」"
1896 = "「Ư!!!!!!!!!!!」"
1897 = "「Ư!!!?」"
1906 = "「～～～～Ư!!!」"
1908 = "「～～～～～Ư!!」"
2135 = "Cảm giác ngực vừa bị ấn nhẹ——Ư!?"
2178 = "Tôi biết. Tôi cảm nhận được. Cửa tử cung của Paulette cũng đang khao khát tinh dịch của tôi. Mỗi lần đâm vào nơi sâu nhất, nó lại khẽ khàng mút lấy một cách ngọt ngào——Ư!"
2309 = "Cửa tử cung của Kisaki hút lấy quy đầu một cách mãnh liệt. Như muốn nuốt trọn toàn bộ tinh dịch của tôi——Ư!!"
2349 = "Siết chặt. Bàn tay phải của Paulette túm chặt lấy ga giường——Ư!"
2501 = "（Ra là vậy, đây chính là—— làm tình ba người sao——Ư!!?）"
```

### 06_Kisaki/lr稀咲追加01_仲国視察の誘い.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1400 = "「Ư!!!」"
```

### 06_Kisaki/lr稀咲追加02_仲国視察.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1184 = "「Ư!!!」"
```

### 06_Kisaki/lr稀咲追加03_新事業案.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
1274 = "「Đúng vậy. Cái này khiến người ta bất giác muốn cổ vũ cho Dương Nương của Suika——Ư!!?」"
```

### 06_Kisaki/lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 8 dòng (raw-tsu: 5, lost-gasp-whole: 1, lost-gasp-trailing: 2)

```toml
[script]
775 = "「——Ư. ～～～～～——Buhaa」"
800 = "「…………Ư」"
1079 = "「Ư——Kuh!!」"
1124 = "「ƯƯƯƯƯƯ!! R, ra rồiiiii!!」"
1133 = "「Ư!!!」"
1134 = "「Ư!!? Xin lỗi, Kisaki.」"
1135 = "「Ư!?」"
1473 = "Vì có vẻ trơn trượt, nên tôi đã định thử làm thật chậm và dài, nhưng nếu Kisaki đã yêu cầu như vậy thì——Ư!!!"
```

### 06_Kisaki/グランドリライト06_稀咲.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
2106 = "「Ư!?」"
```

### 06_Kisaki/稀咲02_新事業案.txt.toml — 7 dòng (lost-gasp-trailing: 5, lost-gasp-whole: 2)

```toml
[script]
1870 = "「Hiee!? Auwa!?——A——kyuuu～～～Ư」"
2289 = "「C, căng thẳng――――～～～Ư」"
2394 = "「Ư!」"
2395 = "「Ư!?」"
2810 = "Dáng vẻ thiếu tự tin trong \\x%l運転台;#00ffc040;buồng lái%l;#; khi nãy, giờ đây lại xinh đẹp đến nhường này sao――――――Ư!!"
2821 = "Ngay chính diện. Ánh mắt của Kisaki nhìn xuống dưới. Và ánh mắt đó, ngay lập tức lại hướng lên trên——Ư!!?"
2830 = "Tiếng nước đó không hề dừng lại, mà vòng sang bên hông, rồi tiến sát ngay bên cạnh tôi——Ư!!"
```

### 06_Kisaki/稀咲03_純白のレール.txt.toml — 3 dòng (lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
2146 = "「Ư!」"
2147 = "「Ư!!?」"
2461 = "Đúng rồi, hôm nay anh Urakami cũng sẽ lại từ Sendai đến đây. Tôi cũng phải đi chào hỏi mới được——Ư!"
```

### 06_Kisaki/稀咲h1_性生活.txt.toml — 12 dòng (raw-tsu: 9, lost-gasp-whole: 2, lost-gasp-trailing: 1)

```toml
[script]
1254 = "「I hyuuuuuuuƯƯ!!!」"
1306 = "「Ưm kyu――kuha――ưm a――~~~Ư!!!」"
1310 = "「Ưm!? Phụt――ưm~~~~~~Ư」"
1316 = "「Ừm, anh cũng vậy. ――Anh cũng……ƯƯ――ra đây」"
1323 = "「Ưm~~~~~Ư――ưm――ưm――ực!」"
1366 = "「Anh cũng vậy――Kisaki! Một chút, nữa thôi――Ư!」"
1486 = "「Ư!」"
1487 = "「Ư!!」"
1488 = "「Ư!!!」"
1492 = "「~~~~~Ư!!!」"
1494 = "「~~~~~~~~~~Ư!!!」"
1650 = "Nụ cười rạng rỡ. Cơ thể đang căng cứng của Kisaki, chợt mềm ra một chút――Ư!!?"
```

### 06_Kisaki/稀咲h2_プライベートルーム.txt.toml — 9 dòng (raw-tsu: 4, lost-gasp-whole: 3, lost-gasp-trailing: 2)

```toml
[script]
1168 = "「Hyu a――Ư――~~~~~~~Ư!!!」"
1198 = "「A――Ư~~~~~~~Ư!!!」"
1201 = "「Fu――Ư――tsu――ưm~~~~~Ư!!」"
1219 = "「Ưm kyu――Ư――ha――~~~~~Ư!!!」"
1389 = "「Ư!」"
1390 = "「Ư!!!」"
1391 = "「Ư!!?」"
1804 = "Nó đang bám chặt, nhào nặn và vắt kiệt dương vật của tôi. Nếu vậy thì, chỉ cần――cứ thế này tiếp tục đẩy sâu vào thôi――Ư!"
1832 = "Từng chút, từng chút một――tiến sâu vào――Ư!?"
```

### 06_Kisaki/稀咲h3_チャイナドレスでおもてなし.txt.toml — 11 dòng (lost-gasp-trailing: 7, lost-gasp-whole: 4)

```toml
[script]
1552 = "「……Ư」"
2003 = "「Đầu vú…… được, anh Soutetsu…… vuốt ve――……Ư Chỉ cần vậy, thôi――đã nóng ran――và cứng lại, thế này――」"
2161 = "「Kya! Phu――~~~~~~~~Ư!!!」"
2257 = "「Khu phư ưm~~~~Ư!!!」"
2809 = "「Ư!」"
2810 = "「Ư!!」"
2813 = "「Ư!!?」"
2814 = "「Ư!?」"
2824 = "「~~~~~Ư!」"
2826 = "「~~~~~~~~~Ư!!!?」"
3143 = "Bất chợt, Kisaki cố gắng che giấu cơ thể mình――Ư!"
```

### 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml — 5 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 4)

```toml
[script]
1288 = "「Ư!」"
1613 = "Dòng tinh dịch đầu tiên vừa bắn ra, đã bị tử cung nuốt chửng mất rồi. Nhưng, ngay từ bây giờ, để rót lên cơ thể Fukami——Ư!?"
1651 = "Một giọng nói quen thuộc. Giọng của Fukami. Đây là đâu? ……A, không, mình đang ngủ gật mà——Ư!?"
1780 = "Fukami hơi nhấc hông lên, và nhanh chóng cởi bỏ chiếc quần lót dễ thương——Ư!?"
1835 = "Easter, là Lễ Phục Sinh nhỉ. Nhắc đến thỏ Phục Sinh thì——Ư!"
```

### 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 1)

```toml
[script]
1105 = "「Ư!!」"
1558 = "Vừa phả ra hơi thở nóng hổi, Fukami vừa luồn lưỡi vào. Đúng là, ngọt thật——hương rượu cũng cực kỳ nhạt——Ư!!"
```

### 07_Nagi_Fukami/lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 6 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 4)

```toml
[script]
1178 = "「Á――Ư!」"
1208 = "「Ư!!」"
1211 = "「Ư!!!!」"
1212 = "「Ư!!!!!」"
1215 = "「Ư!?」"
1515 = "Giọng nói nũng nịu cất lên khi em đã hoàn toàn kiệt sức. Tôi cũng kiệt sức rồi, nhưng vẫn muốn đáp lại em——Ư!!!?"
```

### 07_Nagi_Fukami/lr_凪h2_虎さんの交尾.txt.toml — 6 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 3)

```toml
[script]
1220 = "「Nhyu! ——~~~~~~~~~~~~Ư!!!」"
1221 = "「Ư!!」"
1222 = "「Ư!!!」"
1247 = "「Ha——a——cái đó——nữa đi——anh Soutetsu, lúc nãy ấy——nữa đi——fua! Nữa đi——Ư!」"
1268 = "「A! A! A! A! A! A! A! A! Anh Soutetsu, em——không chịu nổi nữa——Ư!」"
1296 = "「Ư!」"
```

### 07_Nagi_Fukami/lr_凪ふかみh1_じぇいけい！.txt.toml — 13 dòng (lost-gasp-trailing: 10, lost-gasp-whole: 3)

```toml
[script]
1003 = "「~~~~~~~~Ư!!!!」"
1005 = "「……………………Ư!!!」"
1493 = "「Ku——a——a——Ư!!!」"
1537 = "「Hả!? Đùa sao!!?」\\n「A——kha——~~~~~Ư!!!?」"
1566 = "「~~~~~~~~~~~~~~~~~~~~Ư!!!」"
1607 = "「Ư!!」"
1609 = "「Ư!!!!!!」"
1675 = "「Ư!!?」"
1697 = "「Hapu! A, anh Soutetsu! Tuyệt quá——Ư!!!」"
1968 = "Không hiểu sao Fukami lại lộ vẻ mặt thở phào nhẹ nhõm, rồi sau đó thè lưỡi ra liếm——Ư!?"
2081 = "Khi cơn xuất tinh cuối cùng cũng lắng xuống, nhịp thở trở lại bình thường, theo đó tâm trí cũng trở nên sáng suốt——Ư!!"
2121 = "Tôi bắn ra lượng tinh dịch đặc quánh, dính dớp đến mức khó tin đây là lần thứ ba. Cả tôi và Fukami đều rã rời——Ư!?"
2217 = "Màn mút mát ướt át đầy nũng nịu, cùng với cú sục mạnh bạo ở gần gốc dương vật, càng làm tinh dịch sôi sục điên cuồng——Ư!"
```

### 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml — 3 dòng (raw-tsu: 1, lost-gasp-trailing: 1, lost-gasp-whole: 1)

```toml
[script]
736 = "「Ư…………」"
1442 = "Cả nhịp thở, cả ước muốn, đều đang hòa quyện vào nhau. Vì vậy, cứ thế này, chỉ cần dập hông hết sức là——Ư!"
1735 = "（Phập——phập——phập——trượt sâu u u——Ư）"
```

### 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml — 2 dòng (lost-gasp-trailing: 2)

```toml
[script]
1664 = "「…………Ư」"
2728 = "「Ra vậy, có lý. Nhưng, nói là hạnh phúc thì——Ư!」"
```

### 07_Nagi_Fukami/グランドリライト09_凪.txt.toml — 4 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 1, raw-tsu: 2)

```toml
[script]
1629 = "「Ư! ――Ư!」"
1633 = "「Ư!!」"
2404 = "\"Đột nhiên, Nagi dừng bước. Ở một nơi có vẻ như chẳng có gì đặc biệt――――Ư!\""
2492 = "\"Nếu chưa thể đong đếm được điều đó mà đã vội vàng xin lỗi, thì lời xin lỗi có lẽ cũng chỉ là ngoài mặt——Ư!!\""
```

### 07_Nagi_Fukami/凪h1_ふたりっきりのデート.txt.toml — 6 dòng (raw-tsu: 4, lost-gasp-trailing-mid: 1, lost-gasp-trailing: 1)

```toml
[script]
850 = "「——Ư」"
1069 = "「Ư!」"
1083 = "「Ư!?」"
1116 = "「Ư!」"
1152 = "「Anh hai! Anh hai! Anh hai! Anh hai——Ư!? Hả? A——Phù a!?」"
1214 = "\"「Kỷ niệm? Giữa anh và Nagi——Ư!」\""
```

### 07_Nagi_Fukami/凪h2_おとなの水着.txt.toml — 7 dòng (raw-tsu: 3, lost-gasp-trailing: 4)

```toml
[script]
2487 = "「Ư——A——Sắp……xuất tinh, rồi. Cứ thế này bắn vào miệng, em——có sao, không——」"
2536 = "「Ư!」"
2544 = "「Ư!?」"
3354 = "Nagi ôm chầm lấy thùng các tông, rồi xoay một vòng——Ư!!?"
3433 = "Vậy mà, lại ướt đẫm đến thế này. Từ từ, quy đầu như đang cắm phập vào——Ư!"
3610 = "Có vẻ thích thú khi thấy nó cử động, Nagi cười khúc khích, một nụ cười ngây thơ——Ư!?"
3719 = "Sau đó Nagi lại ngó ngoáy xung quanh——Ư!?"
```

### 07_Nagi_Fukami/凪ふかみ01_凪の成長、ふかみの成長.txt.toml — 2 dòng (raw-tsu: 2)

```toml
[script]
1620 = "「Ư!!!」"
2452 = "Vui quá đi! Cảm giác Nagi-sama tự nhiên thông minh hẳn ra——Ư!!!"
```

### 07_Nagi_Fukami/凪ふかみ01_流れ.txt.toml — 5 dòng (lost-gasp-whole: 4, lost-gasp-trailing: 1)

```toml
[script]
1854 = "「Ư!!?」"
1855 = "「Ư!?」"
2334 = "Ví dụ như lấy than của \\x%l8620;#00ffc040;8620%l;#; dùng luôn làm chất mồi lửa chẳng hạn――――Ư!"
2581 = "（Ư!）"
2582 = "（Ư!?）"
```

### 07_Nagi_Fukami/凪ふかみ02_凪の大会初挑戦！.txt.toml — 5 dòng (lost-gasp-trailing: 4, lost-gasp-whole: 1)

```toml
[script]
1470 = "「——Ư」"
1471 = "「——Ư」"
2082 = "「Ư!!」"
2688 = "Một mạch vung kiếm lên cao, rồi cứ thế lao vào đối thủ——Ư!?"
2771 = "Bán khai, chắc có nghĩa là mở một nửa. Cơ thể của Nagi, đúng như cái tên, xoay nửa người lại——Ư!"
```

### 07_Nagi_Fukami/凪ふかみ02_命の重さ.txt.toml — 5 dòng (lost-gasp-whole: 3, lost-gasp-trailing: 2)

```toml
[script]
1635 = "「Ư!」"
1636 = "「Ư!!」"
1637 = "「Ư!?」"
1644 = "「~~~~Ư!!」"
2308 = "Tất cả đều đồng loạt im lặng, chỉ chờ đợi khoảnh khắc công việc kết thúc——Ư!?"
```

### 07_Nagi_Fukami/凪ふかみ03_みかんの旅.txt.toml — 4 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 3)

```toml
[script]
2229 = "「Hahaha——Ư!!?」"
2273 = "「Ư!」"
2274 = "「Ư!!」\\n「A.」"
2295 = "「Ư!?」"
```

### 07_Nagi_Fukami/凪ふかみ03_三人いっしょ.txt.toml — 3 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 2)

```toml
[script]
1460 = "「Oaaaa! Nagi, vẫn chưa được mở cửa đâ——uuuu~~Ư!?」"
1848 = "「Ư!」"
1849 = "「Ư!!?」"
```

### 07_Nagi_Fukami/凪ふかみ05_凪の開眼！？.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
2058 = "「Phù~~Ư」"
```

### 07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml — 3 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 2)

```toml
[script]
1755 = "「Ê ê ê~Ư!?」"
1820 = "「Ư!!」"
1821 = "「Ư!!!!!」"
```

### 07_Nagi_Fukami/凪ふかみ07_少しずつ、大人に.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
2084 = "「Đến cả chị Hibiki cũng hùa theo á~Ư!?」"
```

### 07_Nagi_Fukami/凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml — 4 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 2)

```toml
[script]
1662 = "「Hả? Đúng cái gì cơ――Ư!?」"
1678 = "「Ư!!」"
1679 = "「Ư!!!」"
1692 = "「Hauuu~~Ư」"
```

### 07_Nagi_Fukami/凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml — 2 dòng (lost-gasp-whole: 1, raw-tsu: 1)

```toml
[script]
2250 = "「Ư!!?」"
2405 = "「Là vậy đó」\\n「Hauuu～～Ư」"
```

### 07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
2140 = "「Nếu anh Soutetsu và bé Fukami muốn kết hôn thì――Ư!」"
```

### 07_Nagi_Fukami/凪ふかみh2_みずあそび.txt.toml — 5 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 4)

```toml
[script]
1015 = "「Ư!」"
1294 = "「Hà... hà... hà——hà——a~Ư」"
1865 = "Tôi vòng ra phía sau hai cô gái đang say sưa với nhau, định tung một đòn vuốt ve bất ngờ để trừng phạt——Ư!?"
1946 = "Giọng nói có vẻ luống cuống của Fukami——Ư!?"
2019 = "Cùng lúc với tiếng reo hò, Nagi thọc cả hai tay xuống mặt sông——Ư!!?"
```

### 08_Niiroku/lr_ニイロクh_誓い。約束.txt.toml — 5 dòng (lost-gasp-whole: 4, lost-gasp-trailing-mid: 1)

```toml
[script]
1318 = "「Ư!」"
1323 = "「Ư!!」"
1324 = "「Ư!!!」"
1325 = "「Ư!!!?」"
1474 = "「Phồng lên rồi──Kiyoharu──nóng, quá──Ư!! Cứng quá──bên trong, âm đạo, tất cả──đang bị, khắc sâu vào!」"
```

### 08_Niiroku/ニイロク01_正和四十一年・粉蔵.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1499 = "「Ư!!?」"
```

### 08_Niiroku/ニイロク02_御一夜旅行.txt.toml — 3 dòng (lost-gasp-trailing: 3)

```toml
[script]
1503 = "「Này nhé! Tôi――Ư!!?」"
1561 = "「~~~~~~Ư!!!!」"
1635 = "「Dai dẳng quá――Ư!」"
```

### 08_Niiroku/ニイロク03_粉蔵の嵐.txt.toml — 5 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 3)

```toml
[script]
1036 = "......Không kết nối được. Mở rộng kênh tần số hơn nữa――Ư!!!?"
1426 = "「Ư!!?」"
1451 = "「Ư!」"
1812 = "「Ư!!!」"
2083 = "Cuộn xoáy, rất nhiều, vô số――cùng một lúc―― Tức giận, khóc lóc, hoang mang――Ư!!?"
```

### 08_Niiroku/ニイロク04_終端.txt.toml — 9 dòng (raw-tsu: 9)

```toml
[script]
1244 = "「——Ư——ư——hít――――hà!」"
1265 = "「Ư」"
1731 = "「Ư!!!」"
1743 = "「Ư!」"
1746 = "「Ư!!!」"
1757 = "「Ư!!!!」"
2114 = "「Ư!!!」"
2115 = "「Ư!!!?」"
2364 = "Có lẽ em ấy đã kết nối \\x%l共感;#00ffc040;cộng cảm%l;#; ngay lập tức. Cơ thể Niiroku bỗng trở nên ấm áp——Ư!!?"
```

### 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml — 6 dòng (raw-tsu: 2, lost-gasp-trailing: 3, lost-gasp-whole: 1)

```toml
[script]
1519 = "「——Ư」"
2306 = "「Ư!」\n「A.」"
2308 = "「Ư!」"
2338 = "「A——Ư!!!」"
2912 = "「Khoan đã! Chị hai~Ư」"
3588 = "Mọi người đều háo hức, như đang chờ đợi lời tôi nói ngước nhìn lên tôi——Ư!!"
```

### 09_Grand/グランドリライト03_日々姫.txt.toml — 1 dòng (raw-tsu: 1)

```toml
[script]
2428 = "「Bị kéo đi? ――Ư!?」"
```

### 09_Grand/グランドリライト04_ポーレット.txt.toml — 5 dòng (lost-gasp-trailing: 2, lost-gasp-whole: 3)

```toml
[script]
1317 = "「……Ừm. Cài xong rồi. Chắc chắn là rất hợp với Paulette——Ư!?」"
1815 = "「Ư!!!」"
1817 = "「Ư!?」\\n「Hyaa!!?」"
1860 = "「Ư!」"
2949 = "Đôi mắt xanh biếc hơi ngấn lệ. Cô ấy bước một bước lớn lại gần tôi——Ư!?"
```

### 09_Grand/グランドリライト05_れいな.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1881 = "「Ư!?」"
```

### 09_Grand/グランドリライト06_稀咲.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
2106 = "「Ư!?」"
```

### 09_Grand/グランドリライト07_真闇.txt.toml — 1 dòng (lost-gasp-trailing: 1)

```toml
[script]
2579 = "\"「Đúng vậy. Hay là làm cho hoành tráng luôn, \\x%l編成;#00ffc040;ghép%l;#; cả toa phát điện và xe đông lạnh vào——Ư!!」\""
```

### 09_Grand/グランドリライト08_ふかみ.txt.toml — 5 dòng (lost-gasp-trailing: 3, lost-gasp-whole: 2)

```toml
[script]
1772 = "「Hyau!? Ây, anh búng trán em~Ư」"
1801 = "「Ư!」"
1822 = "「Ư!!?」"
1845 = "「Hửm? ――Ư!」"
1846 = "「Ồ!」\\n「――Ư!」"
```

### 09_Grand/グランドリライト09_凪.txt.toml — 4 dòng (lost-gasp-trailing: 1, lost-gasp-whole: 1, raw-tsu: 2)

```toml
[script]
1629 = "「Ư! ――Ư!」"
1633 = "「Ư!!」"
2404 = "\"Đột nhiên, Nagi dừng bước. Ở một nơi có vẻ như chẳng có gì đặc biệt――――Ư!\""
2492 = "\"Nếu chưa thể đong đếm được điều đó mà đã vội vàng xin lỗi, thì lời xin lỗi có lẽ cũng chỉ là ngoài mặt——Ư!!\""
```

### 09_Grand/グランドリライト10_ハチロク.txt.toml — 5 dòng (raw-tsu: 5)

```toml
[script]
1188 = "「Ư——」"
1676 = "「Ư!!?」"
1693 = "「Ư!」"
1694 = "「Ư!!!」"
2174 = "「Ư!!!」"
```

### 09_Grand/グランドリライト11_ナインスターズ！.txt.toml — 4 dòng (lost-gasp-whole: 4)

```toml
[script]
2315 = "「Ư!」"
2317 = "「Ư!!」"
2318 = "「Ư!!!」"
2355 = "「Ư!!?」"
```

### 10_Chikuni/仲国03_北琴鉄道歴史館.txt.toml — 3 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 2)

```toml
[script]
1945 = "「Vâng!!」\\n「Ư!!!」"
1963 = "「Haa~Ư」"
2845 = "Ôi chà, có điện thoại. Cô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——Ư!"
```

### 10_Chikuni/仲国04_z49列車.txt.toml — 2 dòng (lost-gasp-whole: 1, lost-gasp-trailing-mid: 1)

```toml
[script]
2143 = "「Ư!!!!」"
2846 = "(Rốt cuộc là đang vẽ cái gì――――Ư!)"
```

### 10_Chikuni/仲国05_真夜中の餐車.txt.toml — 10 dòng (lost-gasp-whole: 6, lost-gasp-trailing-mid: 1, lost-gasp-trailing: 3)

```toml
[script]
1947 = "「Ư!!?」"
1972 = "「Ư!!!」"
1982 = "「Ư!!」"
1983 = "「Ư!!?」\\n「Đúng vậy. Khớp nối toa xe cũng đang bị kéo căng――trước hết là cái đó.」"
2071 = "「Sao vậy? ――Ư! Không lẽ đi lại mệt mỏi quá nên phát sốt rồi.」"
2365 = "「Thầy Soutetsu sao? Suika―― không hề nghe thấy tiếng bước chân nào như vậy――Ư!!?」"
2375 = "「Ư!!!!!」"
2376 = "「Ư!!!?」"
2874 = "Dù không hề ra lệnh, nhưng khí xả tự động lọt ra từ miệng tôi, tạo thành một tiếng động lớn không ngờ――Ư!"
3158 = "Suika khẽ gật đầu. Vì vậy, tôi mở cộng cảm――Ư!!!!!!!!!"
```

### 10_Chikuni/仲国06_聖都とパンダとハチロクと.txt.toml — 1 dòng (lost-gasp-whole: 1)

```toml
[script]
1523 = "「Ư!!!」"
```

### 10_Chikuni/仲国07_芭岩鉄道.txt.toml — 3 dòng (lost-gasp-whole: 1, lost-gasp-trailing: 2)

```toml
[script]
1383 = "「Ư!!!!!」\\n「Đúng rồi!!!」"
1980 = "Là tiếng huýt sáo. Có vẻ rất quen thuộc, một âm thanh khá lớn và hay――Ư!!?"
1985 = "Một lượng hơi nước khổng lồ chứa lượng nước có thể nhìn thấy bằng mắt thường, được xả ra với một thế lực mãnh liệt về phía thung lũng――Ư!!!!"
```

### 11_Other/lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml — 5 dòng (lost-gasp-whole: 4, lost-gasp-trailing-mid: 1)

```toml
[script]
1301 = "「Ư!!」"
1554 = "「Ư!!!?」"
1591 = "「Ư!」"
1925 = "「Ư!!!」"
2099 = "「Tôi biết! Đàn ông đi tiểu——Ư!!!!? please wait!! Đợi một chút!?」"
```

## 9. Các dòng chưa sửa

### 9.1 Chưa chắc chắn (4 dòng — KHÔNG có trong khối sửa, Hieu quyết)

- **07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml — key 1078**
  - JP: 「く――あ……ふか、み――」
  - TW: 「啊……深美……」
  - VN hiện tại: 「Kh——a…… Fuka, mi——」
  - Lý do: JP và TW mâu thuẫn nhau (JP hỏi về máy chưng cất, TW/VN là tiếng gasp "Ah... Fukami..."); VN theo TW và còn bị cụt giữa chừng, không rõ gasp thuộc về dòng nào.

- **07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml — key 1588**
  - JP: ふかみがいきなり深くまで――\n僕の勃起の全部を一気に口いっぱいに収めてくれ――っ！
  - TW: 深美突然用力，把我的肉棒一口氣全部含進嘴裡……唔！
  - VN hiện tại: Đột nhiên Fukami ngậm sâu vào——\nThu trọn toàn bộ sự cương cứng của tôi vào miệng cùng một lúc——!
  - Lý do: JP và TW mâu thuẫn nhau (JP là so sánh cánh chim mẹ ấp trứng, TW/VN là Fukami ngậm sâu); không rõ gasp thuộc về dòng nào.

- **07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml — key 1566**
  - JP: 閉じ込めきれず。ふかみは大きく口を開いて息を漏らして。\nそれでも、声は、どうにかこうにか抑え続け――っ！？
  - TW: 深美沒能徹底控制住自己的聲音，她大張著嘴在呼氣。但是她依然勉強控制著自己的聲音……唔？！
  - VN hiện tại: Không thể kìm nén được nữa. Fukami há to miệng, để lọt ra những tiếng thở hắt.\nDù vậy, em ấy vẫn bằng cách nào đó tiếp tục kìm nén giọng nói của mình——!?
  - Lý do: JP và TW mâu thuẫn nhau (JP chỉ là tiếng rên ngắn ん～～～――っ, TW/VN là đoạn dẫn dài về Fukami kìm giọng); không rõ gasp thuộc về dòng nào.

- **09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml — key 1556**
  - JP: 「っ」
  - TW: 「……」
  - VN hiện tại: 「Ô kìa Thị trưởng. Cô lên tiếng gọi tôi thì đúng là hiếm thấy đấy.」
  - Lý do: JP chỉ là một tiếng gasp trơ trụi 「っ」 không có dấu câu; TW và bản sửa của audit đều dịch thành 「……」 (lửng). Hieu quyết xem giữ 「……」 hay đổi thành 「Ư」.

### 9.2 Cần audit file xử lý (82 dòng — gasp không đặt được chắc chắn vì lệch dòng / lệch số đoạn)

Các dòng này sẽ được xử lý khi audit tới file của chúng (audit đọc từng dòng đối chiếu JP nên sẽ đặt lại gasp đúng chỗ).

| File | Key | JP | VN hiện tại |
|---|---|---|---|
| 00_Common/共通02_日々姫と真闇と人形と.txt.toml | 1942 | 「丁寧なご挨拶いたみいる。僕は双鉄。\n右田双鉄という学生――休学したての学生だ」 | 「Cảm ơn cô đã chào hỏi tử tế. Tôi là Soutetsu.\nMột sinh vi… |
| 00_Common/共通02_日々姫と真闇と人形と.txt.toml | 2592 | 「//////」 | 「//////」 |
| 00_Common/共通02_日々姫と真闇と人形と.txt.toml | 2894 | 日々姫の気持ちはよくわかる。\nだが、坊主と袈裟とは別物だ。 | Tôi rất hiểu cảm giác của Hibiki.\nNhưng ghét sư thì đừng g… |
| 00_Common/共通03_ハチロクとナビ.txt.toml | 1547 | 「左様ですね」 | 「Đúng vậy nhỉ.」 |
| 00_Common/共通03_ハチロクとナビ.txt.toml | 2036 | 雲ひとつ無い。\nなのに、なぜ、ナビともあろうものがそんな――っ！ | Trời không một gợn mây.\nVậy mà, tại sao một hệ thống như N… |
| 00_Common/共通04_キハ07。ポーレットとれいな.txt.toml | 2154 | 「ハチロク。時計とぜんまいカギを」 | 「Hachiroku. Đồng hồ và chìa khóa lên dây cót đâu.」 |
| 00_Common/共通06_8620を探せ.txt.toml | 2016 | 「良さそうですね。こんなにビクビク暴れてしまって。\nうふふ、それなら――これはいかがです？」 | 「Có vẻ hiệu quả tốt đấy ạ. Ngài giật nảy người lên thế này … |
| 00_Common/共通06_8620を探せ.txt.toml | 3153 | しまった。\n思いをそのままぽろりと漏らしてしまった。 | Chết thật.\nTôi lỡ buột miệng nói ra suy nghĩ của mình mất … |
| 00_Common/共通06_8620を探せ.txt.toml | 3173 | 意味がわからん。 | Chẳng hiểu gì cả. |
| 01_Hachiroku/lr_ハチロクh1_今ひとたびの契り.txt.toml | 1314 | 「わかっている、すず。\n僕も――こみあげ――きって――いるっ――っ！」 | 「Anh biết rồi, Suzu.\nAnh cũng——đang trào dâng——đến giới hạ… |
| 01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml | 1720 | 「～～～～～～～～っ」 | 「~~~~~~~~ưm」 |
| 01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml | 2103 | すずの指先が強気に動き、僕の醜い勃起を包む。\n包む――というか、――これは――かな、り、――っ。 | Đầu ngón tay Suzu mạnh bạo di chuyển, bao trọn lấy sự cương… |
| 01_Hachiroku/ハチロク06_それぞれの傷跡.txt.toml | 1979 | 「っ！」 | 「Chuyện đó!」 |
| 01_Hachiroku/ハチロク09_もくもくオリヴィ.txt.toml | 1678 | 「っ！？\nな、なんと、もうか！？　あっという間だな」 | 「!?\nCái, cái gì, đã đến rồi sao!? Mới chớp mắt một cái thô… |
| 01_Hachiroku/ハチロク14_橋.txt.toml | 1914 | 「っ！！？\n双鉄様、代わってください！　わたくしが」 | 「!!?\nNgài Soutetsu, xin hãy đổi chỗ cho em! Em sẽ」 |
| 01_Hachiroku/ハチロクh7_レトロモダンメイクラヴ.txt.toml | 783 | 「あっ――ひっ――しょっ――くっ――んあっ――\nゆっく――りっ――され、りゅっ――と――んぅ～っ！」 | 「A——hi——ức——khục——ưm a——\nchậm——chậm——lại, đi——ưm~ !」 |
| 02_Hibiki/日々姫h3_汚れてしまった制服で.txt.toml | 1855 | （スンっ――スン――っ！） | （Khịt khịt——Khịt khịt!） |
| 03_Paulette/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2236 | ポーレットの手が僕から離れる。離れて―っ！\nぺろりと小さく、赤い舌先で先走り汁の味をみる。 | Tay Paulette rời khỏi người tôi. Rời khỏi——!\nCô ấy thè chi… |
| 03_Paulette/ポーレット03_廃炭鉱.txt.toml | 1791 | 「あ、はい。\n炭鉱の中は少し肌寒かったですけど――っ！！？」 | 「A, vâng.\nBên trong mỏ than hơi se lạnh một chút nhưng——ơ!… |
| 03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml | 1863 | 「うぅ～っ！\nうまれてないと、いっしょじゃないのー？」 | 「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsu… |
| 03_Paulette/ポーレット15_求人難.txt.toml | 1903 | 「証？　\n……っ！！」 | 「Minh chứng?\n……!!」 |
| 03_Paulette/ポーレットh7_残業エッチもyシャツで.txt.toml | 816 | 「ひあっ！　あっ――めくれっ――んっ――ひっぱ――っ\n――あっ――おま、んこっ――ひっ――しゅご――んっ」 | 「Hya! A——bị lộn, ngược——ưm——bị kéo, ra——\n——a——âm, đạo——hi—… |
| 04_Reina/lr_れいなh1_レディ・れいな.txt.toml | 1597 | もごもごしゃべる。短い舌があたってくる。\nただそれだけで精液水位がぐぐとあがっ――っ！！！？ | Em ấy nói chuyện ậm ờ. Chiếc lưỡi ngắn chạm vào.\nChỉ bấy n… |
| 04_Reina/lr_れいなh1_レディ・れいな.txt.toml | 1790 | 腸も、そうして排泄孔にいたるまで。\nれいなの全部を、僕の精液で染め尽くした――っ！？ | Cả ruột, rồi cho đến tận lỗ bài tiết.\nTôi muốn nhuộm đẫm t… |
| 06_Kisaki/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 2236 | ポーレットの手が僕から離れる。離れて―っ！\nぺろりと小さく、赤い舌先で先走り汁の味をみる。 | Tay Paulette rời khỏi người tôi. Rời khỏi——!\nCô ấy thè chi… |
| 06_Kisaki/稀咲01_金と人.txt.toml | 2063 | 「っ！」 | Lại một sự thật phũ phàng nữa khó lòng phản bác. |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1384 | 「貰って、染めてほしいです――んっ――双鉄おにいさん\n専用、の――わたしの――ふかみの――おまんこたまご」 | 「Hãy nhận lấy, và nhuộm màu cho nó đi ạ——ưm——dành riêng\nch… |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1445 | 「奇遇だな。僕もふかみとキスしたかった」 | 「Trùng hợp thật. Tôi cũng muốn hôn Fukami.」 |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1629 | きゅうんと締まる。ぞわぞわざわめく。\n僕の射精のイメージが、ふかみの膣に伝わったらしい。 | Thắt chặt lại. Run rẩy râm ran.\nCó vẻ như hình ảnh tôi bắn… |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1817 | ガチガチに締め付けられた膣内で、貼り付いてくる膣壁が、\n蠕動をして僕の勃起をぎゅうぎゅう幾度も乳搾りする。 | Trong âm đạo bị siết chặt cứng, thành âm đạo bám dính lấy,\… |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1967 | （ぎちゅちゅっ！　きゅうっ！　きゅうんっ！！） | (Gichuchu! Kyu! Kyuun!!) |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1027 | 「ひゃっ！？　あっ！　待っ！　まって！　らめっ、\nほんとっ――いま――わたし――ばかに、なっちゃうっ」 | 「Hya!? A! Đợi! Đợi đã! Không được,\nthật đấy——bây giờ——em——… |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1099 | 「～～～～～～～～～～～～～～～～～～っ！！！！！」 | 「~~~~~~~~~~~~!!!!!」 |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1107 | 「っ！！！！！！」 | 「!!!!!!」 |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1120 | 「じゅぼっ！　ばちゅっ！　ごちゅっ！　ぢゅぶっ！！\nじゅぶっ！　ぢゅうっ！　じゅぼっ！　ぼちゅっ！！」 | 「Chụt! Bạch! Cụp! Chụt!!\nChụt! Chuu! Chụt! Phụt!!」 |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1179 | 「おまんこ、いまっ――双鉄おにいさん、かたち、に――\n双鉄おにいさんの、ため、だけの――ふ……ぁ……嬉し」 | 「Âm đạo, bây giờ——đã biến thành, hình dạng——của anh Soutets… |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1241 | 「僕の種が、ふかみのおまんこで蒸留され――\nその精髄たる一滴が、子宮に達し、熟成される」 | 「Hạt giống của tôi, được chưng cất trong âm đạo của Fukami—… |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1260 | 「ふぁ……あ――双鉄、おにいさんの――おちんちんの、\nさきっぽ――ん――いっつも、よりも――ふくれ、てて」 | 「Ha…… a——phần đầu——dương vật, của anh Soutetsu——\nưm——căng … |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1423 | 双鉄おにいさんに戻ってしまった。それも嬉しく愛おしく、\n体を崩して、べとりとくっつき、キスをする。 | Lại trở về cách gọi anh Soutetsu rồi. Điều đó cũng khiến tô… |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1479 | 僕も感じる。ふかみの膣内に射精す快感はいつもと同じ、\n最高の密着感であるのに――そこより深い何かを確かに。 | Tôi cũng cảm nhận được. Khoái cảm khi xuất tinh vào trong â… |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1717 | （すっ――しにゅっ――グチュッ――チュぶっ――） | (Sột soạt——nhóp nhép——nhóp nhép——chụt——) |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1733 | （ぢゅゅこんっ！！！） | (Sùng sục!!!) |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1760 | （ふにっ――もみゅっ――コリュ――さすっ） | (Mềm mại——xoa nắn——cọ xát——vuốt ve) |
| 07_Nagi_Fukami/lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1223 | 「ずじゅ～～～～～～～～～～～～～～～～～っ！！！」 | 「Zujuuuuuuuuuuuuuuuuuuu!!!」 |
| 07_Nagi_Fukami/lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1272 | 「お望み、どおりの――お乳を――母乳を――\n凪が――たくさん――出せる、ように、なる――っ！」 | 「Như em, mong muốn——để Nagi——có thể, tiết ra——\nthật nhiều—… |
| 07_Nagi_Fukami/lr_凪ふかみh1_じぇいけい！.txt.toml | 1838 | 「気持ちいいは――気持ちよかけど……ん～～っ……\n――あ！　ぺろおおおおっ！」 | 「Sướng thì——sướng thật nhưng……ưm~~……\n——A! Liếmmmmm!」 |
| 07_Nagi_Fukami/ふかみh1_ともはり練習.txt.toml | 1403 | 快感が強烈すぎるのか、\nふかみがイヤイヤと頭を振っ――っ！ | Có lẽ vì khoái cảm quá mãnh liệt,\nFukami lắc đầu nguầy ngu… |
| 07_Nagi_Fukami/ふかみh1_ともはり練習.txt.toml | 1426 | そうしてそれは、とても静かな頷きになる。 | Và rồi em ấy gật đầu một cái thật khẽ. |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1043 | 「ぷあっ」 | 「Phù」 |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1312 | それでもやはり、万が一にも、\n嬌声などは聞かせたくない。 | Nhưng dù vậy, phòng trường hợp vạn nhất,\ntôi cũng không mu… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1382 | 唇で歯をくるんでくれて、舌を沿わせて。僕の勃起を\n傷つけないよう丁寧に準備してくれる――から！ | Dùng môi bọc lấy răng, rồi đưa lưỡi ra liếm dọc theo. Em ấy… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1440 | もう一度、キス。\nその距離のまま、ふかみの瞳が僕をみつめる。 | Một nụ hôn nữa.\nGiữ nguyên khoảng cách đó, đôi mắt Fukami … |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1465 | ふかみの声を、抑え込めてる。\nこれなら、僕にしか聞こえない。 | Tôi đang kìm nén giọng nói của Fukami lại.\nThế này thì, ch… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1482 | ふかみに重なり、崩れ落ちてる。 | Tôi đè lên người Fukami, ngã gục xuống. |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1512 | ならばと逸る体をなだめ、\nゆっくり、ねっとりつながる部分を動かしていく。 | Thấy vậy, tôi xoa dịu cơ thể đang rạo rực của mình,\ntừ từ,… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1553 | 涼やかな夕立ちにあったみたいに、ふかみはうっとり\n目を閉じて、僕の白濁のシャワーを浴びる。 | Giống như gặp phải một cơn mưa rào mát mẻ, Fukami say sưa\n… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1601 | パンツの上から指をあて、パンツに形を浮かせるように、\nふかみは、おまんこを大きく開く。 | Đặt ngón tay lên trên quần lót, như thể muốn in hằn hình dá… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1605 | 僕らのホームへ――\n『おかえりなさい』を、言い合うために。 | Về nhà ga của chúng tôi——\nĐể cùng nói với nhau câu 『Chào m… |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 1723 | （ガララ――ピシャっ） | （Cạch cạch——xoạch） |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2292 | 「やっ、なにこれっ！？　こんなにひどいとかっ」 | 「Á, gì thế này!? Sao lại mưa to thế này chứ」 |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2519 | 「一雨くるな」 | 「Sắp mưa to rồi」 |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2531 | 「お、思いましたです……けどっ――」 | 「C, có nghĩ ạ…… nhưng——」 |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2629 | 「ああ、事故さえを引き起こしかねない。\nゆえに、草むしりが最優先となってしまうのだ」 | 「Ừ, thậm chí có thể gây ra tai nạn.\nVì vậy, nhổ cỏ mới trở… |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2829 | 「だったら、わたし、重ねたいです。\n凪ちゃんとの思い出の上に、もっと新しい思い出を」 | 「Nếu vậy, em, muốn tô điểm thêm.\nLên trên những kỷ niệm vớ… |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2869 | 「雨宿り……つづけなきゃ」 | 「Chúng ta phải…… tiếp tục trú mưa thôi」 |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3127 | 凸と凹。肉襞の、亀頭の突起のレベルですらも、\n噛み合い、魅き合い、貼り付き剥がれあっている。 | Lồi và lõm. Thậm chí ở cấp độ của những nếp gấp thịt, những… |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3390 | 唇を割り、ふかみの舌を自分の舌で軽くつつけば、\nすぐさまふかみは、僕の口内に逆進してくる。 | Tách đôi môi em ra, dùng lưỡi mình khẽ chạm vào lưỡi Fukami… |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3619 | ふかみの足が、絡んで来ている。 | Đôi chân Fukami, đang quấn chặt lấy tôi. |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 3805 | その程度の距離なら、なにほどもない。 | Khoảng cách chừng đó thì chẳng nhằm nhò gì. |
| 07_Nagi_Fukami/グランドリライト08_ふかみ.txt.toml | 1693 | 「いまうとうとしとったでしょー。疲れとるのわかるけど、\nいけんよ？　講義中にいねむりだとか」 | 「Anh vừa mới ngủ gật đúng không. Em biết là anh mệt, nhưng\… |
| 07_Nagi_Fukami/グランドリライト08_ふかみ.txt.toml | 1703 | 「そうか？」 | 「Vậy sao?」 |
| 07_Nagi_Fukami/グランドリライト08_ふかみ.txt.toml | 1790 | 「ああ、すまん。ついというか、思わずというか」 | 「A, xin lỗi. Là anh lỡ tay, hay nói đúng hơn là không kiềm … |
| 07_Nagi_Fukami/グランドリライト08_ふかみ.txt.toml | 2484 | いかん。路子の妙におとなびた声につられてしまい、\n余計な心配をかけてしまった。 | Không ổn rồi. Bị cuốn theo giọng nói có vẻ trưởng thành đến… |
| 07_Nagi_Fukami/グランドリライト08_ふかみ.txt.toml | 2626 | わずかに震える指先で――\nそれでもしっかり、受話器を掴む。 | Với những đầu ngón tay hơi run rẩy――\nNhưng vẫn nắm chặt lấ… |
| 07_Nagi_Fukami/グランドリライト09_凪.txt.toml | 1630 | 「っ！」 | 「Vậy sao!」 |
| 07_Nagi_Fukami/凪ふかみ05_凪の開眼！？.txt.toml | 2160 | 「っ！！？」 | 「Ế!!?」 |
| 07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml | 1988 | 「すまん、ギリギリになってしま――っ\nごほっ！　げほっ！」 | 「Xin lỗi, anh tới sát giờ qu——\nKhụ! Khụ khụ!」 |
| 07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml | 3052 | ふかみと凪はうなずきあって――っ！？ | Fukami và Nagi gật đầu với nhau――hả!? |
| 07_Nagi_Fukami/凪ふかみh1_修学旅行の夜.txt.toml | 1736 | 目と目。\nそれだけでまた会話して――っ！！？ | Bốn mắt nhìn nhau.\nChỉ bấy nhiêu thôi mà hai người lại trò… |
| 09_Grand/グランドリライト09_凪.txt.toml | 1630 | 「っ！」 | 「Vậy sao!」 |
| 10_Chikuni/仲国02_北琴の鉄道.txt.toml | 3294 | （ぐ～～っ） | (Rột~~) |
| 11_Other/lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 2166 | 「なるほど。ならば方法を……っ！\nああ、今日は丁度、[もみじ,1]紅葉が尋ねてくる日でしたか」 | 「Ra vậy. Nếu vậy thì cách tốt nhất là……!\nA, hôm nay vừa ha… |

### 9.3 Audit của file đã sửa gasp rồi — không sửa trùng (32 dòng)

| File | Key | Bản sửa của audit (đã có gasp) |
|---|---|---|
| 01_Hachiroku/ハチロク12_再開発.txt.toml | 2103 | 「Ư!」 |
| 01_Hachiroku/ハチロク12_再開発.txt.toml | 2537 | 「Ư!」 |
| 03_Paulette/ポーレット01_ポーレット退任.txt.toml | 1648 | 「Ư!」 |
| 03_Paulette/ポーレット01_御一夜探し.txt.toml | 2480 | Fukami và Nagi thì——Ư!? |
| 03_Paulette/ポーレット03_廃炭鉱.txt.toml | 2154 | 「Ư!」 |
| 03_Paulette/ポーレット09_ストーブ客車.txt.toml | 2274 | 「Ư!」 |
| 03_Paulette/ポーレット09_ストーブ客車.txt.toml | 2275 | 「Ư!?」 |
| 03_Paulette/ポーレット09_ストーブ客車.txt.toml | 2277 | 「~Ư!」 |
| 03_Paulette/ポーレット10_見えない傷.txt.toml | 1634 | 「Ư!」 |
| 03_Paulette/ポーレット10_見えない傷.txt.toml | 1635 | 「Ư!!!」 |
| 03_Paulette/ポーレット10_見えない傷.txt.toml | 1639 | 「~~~Ư!」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1008 | 「——Ư!!?」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1771 | 「Ư!」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1772 | 「Ư!」 「Ư!」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1774 | 「Ư!!」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1775 | 「Ư!!!」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1776 | 「Ư!!?」 |
| 03_Paulette/ポーレット11_記憶と記録.txt.toml | 1777 | 「Ư!!?」 「Hyawa!!?」 |
| 03_Paulette/ポーレット12_解放.txt.toml | 1161 | 「Ư!」 |
| 03_Paulette/ポーレット12_解放.txt.toml | 822 | 「――Ư」 |
| 03_Paulette/ポーレット13_再評価.txt.toml | 1483 | 「Ư!」 |
| 03_Paulette/ポーレット13_再評価.txt.toml | 1484 | 「Ư!?」 |
| 03_Paulette/ポーレット14_ふたたび走り出すために.txt.toml | 1889 | 「Ư!!?」 |
| 03_Paulette/ポーレット14_ふたたび走り出すために.txt.toml | 1890 | 「Ư!!?」 |
| 03_Paulette/ポーレット15_求人難.txt.toml | 1976 | 「Ư!」 |
| 03_Paulette/ポーレット15_求人難.txt.toml | 1977 | 「Ư!!」 |
| 03_Paulette/ポーレット15_求人難.txt.toml | 1978 | 「Ư!?」 |
| 03_Paulette/ポーレット16_明日へのレール.txt.toml | 2448 | 「Ư!」 |
| 03_Paulette/ポーレット16_明日へのレール.txt.toml | 2449 | 「Ư!!?」 |
| 03_Paulette/ポーレット16_明日へのレール.txt.toml | 2450 | 「Ư!?」 |
| 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml | 2585 | 「Việc tôi hầu hạ bên cạnh ngài Soutetsu là điều đương nhiên… |
| 09_Grand/グランドリライト01_オール御一夜、成立ならず.txt.toml | 3560 | 'Sự tự do của tôi', đang được Kisaki, và Paulette định nghĩ… |

### 9.4 VN đã diễn gasp bằng cách khác — không phải gasp bị mất (132 dòng)

Các dòng này VN đã có Ư/Ự/Hự/Hức, câu cảm thán ("A!!", "Ưm!", "Hả!?"), hoặc SFX đã dịch ("Rột~~~") ở đúng vị trí gasp. Chỉ liệt kê file + key (chi tiết JP/VN trong file JSON đi kèm).

| File | Các key |
|---|---|
| 00_Common/共通05_ようやく石炭.txt.toml | 2311 |
| 00_Common/共通09_さきだつもの.txt.toml | 2359 |
| 00_Common/共通13_勾配図.txt.toml | 2057 |
| 01_Hachiroku/lr_ハチロクh2_新しい服。新しい旅.txt.toml | 1104 |
| 01_Hachiroku/lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml | 1307 |
| 01_Hachiroku/ハチロク04_煙には煙を.txt.toml | 3088 |
| 01_Hachiroku/ハチロク06_それぞれの傷跡.txt.toml | 1638 |
| 01_Hachiroku/ハチロク06_のぞみ.txt.toml | 2257, 2329 |
| 01_Hachiroku/ハチロク07_延命.txt.toml | 2292 |
| 01_Hachiroku/ハチロク08_教導.txt.toml | 2085 |
| 01_Hachiroku/ハチロク10_旺宮鉄道歴史館.txt.toml | 2488 |
| 01_Hachiroku/ハチロク13_夜の嵐.txt.toml | 1660 |
| 01_Hachiroku/ハチロク13_実りの秋.txt.toml | 1839 |
| 01_Hachiroku/ハチロク14_冬.txt.toml | 2690 |
| 01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml | 1875 |
| 01_Hachiroku/ハチロクh3_磨き洗い.txt.toml | 1063, 1066, 1224 |
| 01_Hachiroku/ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 956, 1718 |
| 01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 837, 938, 946 |
| 01_Hachiroku/ハチロクh7_レトロモダンメイクラヴ.txt.toml | 759 |
| 01_Hachiroku/ハチロクh8_桜色のひめごと.txt.toml | 732, 1584 |
| 01_Hachiroku/ハチロクh9_コノフクハキルコト.txt.toml | 2178 |
| 02_Hibiki/lr_日々姫h1_鏡の中日々姫.txt.toml | 1069, 1126, 1146 |
| 02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml | 1079, 1663 |
| 02_Hibiki/lr_日々姫真闇h1_三人家族.txt.toml | 1432, 1723 |
| 02_Hibiki/lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 2092 |
| 02_Hibiki/日々姫02_文庫森.txt.toml | 1664 |
| 02_Hibiki/日々姫03_客車手配.txt.toml | 2328 |
| 02_Hibiki/日々姫05_市議会見学.txt.toml | 2280 |
| 02_Hibiki/日々姫09_静かなる開戦.txt.toml | 1580 |
| 02_Hibiki/日々姫11_御一夜モザイク.txt.toml | 2321 |
| 02_Hibiki/日々姫13_討論会.txt.toml | 1704 |
| 02_Hibiki/日々姫14_投開票.txt.toml | 1712 |
| 02_Hibiki/日々姫16_夢を乗せて.txt.toml | 1703 |
| 02_Hibiki/日々姫h2_洗って大丈夫なスーツ.txt.toml | 1071 |
| 02_Hibiki/日々姫h4_いもうとタオル.txt.toml | 1065 |
| 02_Hibiki/日々姫h5_白濁絵の具の射精会.txt.toml | 1166, 1241 |
| 02_Hibiki/日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2282 |
| 03_Paulette/lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1016 |
| 03_Paulette/lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1028, 1062, 1063, 1065, 1068 |
| 03_Paulette/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1599, 1892, 1893 |
| 03_Paulette/ポーレット01_御一夜探し.txt.toml | 1909 |
| 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml | 1663 |
| 03_Paulette/ポーレット04_ヒヤリング.txt.toml | 1489 |
| 03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml | 1864 |
| 03_Paulette/ポーレット06_雪の宿.txt.toml | 1835 |
| 03_Paulette/ポーレット07_うさぎ.txt.toml | 1713 |
| 03_Paulette/ポーレットh3_誘惑アイスコーヒー.txt.toml | 994 |
| 03_Paulette/ポーレットh4_クリーム＆クリーム.txt.toml | 896 |
| 03_Paulette/ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 833 |
| 03_Paulette/ポーレットh7_残業エッチもyシャツで.txt.toml | 879, 899 |
| 03_Paulette/ポーレットh8_気動車の国のアリス.txt.toml | 2344 |
| 04_Reina/lr_れいなh1_レディ・れいな.txt.toml | 1271, 1280, 1281, 1283, 1761 |
| 04_Reina/れいなh1_おかあさんのレッスン.txt.toml | 1373, 1375 |
| 04_Reina/れいなh3_おもらし自由化大作戦.txt.toml | 1199 |
| 05_Mayami/lr_真闇h1_僕のおねえちゃん.txt.toml | 1428, 1503, 1698, 1803 |
| 05_Mayami/真闇h1_長期熟成.txt.toml | 1092 |
| 06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml | 1065, 1073, 1262 |
| 06_Kisaki/lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1599, 1892, 1893 |
| 06_Kisaki/稀咲01_金と人.txt.toml | 1618 |
| 06_Kisaki/稀咲h1_性生活.txt.toml | 1012 |
| 06_Kisaki/稀咲h3_チャイナドレスでおもてなし.txt.toml | 3373, 3483 |
| 07_Nagi_Fukami/lr_ふかみh1_ふかみうさぎのたまご.txt.toml | 1287, 1304, 1400 |
| 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml | 1029, 1035, 1070, 1763 |
| 07_Nagi_Fukami/lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1135, 1155 |
| 07_Nagi_Fukami/lr_凪ふかみh1_じぇいけい！.txt.toml | 1395, 1495, 1563 |
| 07_Nagi_Fukami/ふかみh1_ともはり練習.txt.toml | 1461 |
| 07_Nagi_Fukami/ふかみh2_homesweethome.txt.toml | 988, 1033 |
| 07_Nagi_Fukami/ふかみh3_夏休みの最後の日の、前の日.txt.toml | 2281, 3645 |
| 07_Nagi_Fukami/凪h2_おとなの水着.txt.toml | 2489 |
| 07_Nagi_Fukami/凪ふかみ05_凪の開眼！？.txt.toml | 2142 |
| 07_Nagi_Fukami/凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml | 1516 |
| 07_Nagi_Fukami/凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml | 2232 |
| 07_Nagi_Fukami/凪ふかみh1_修学旅行の夜.txt.toml | 1235, 1236, 1285, 2022 |
| 07_Nagi_Fukami/凪ふかみh2_みずあそび.txt.toml | 1291, 1319, 1330, 1373, 1382 |
| 08_Niiroku/lr_ニイロクh_誓い。約束.txt.toml | 1365 |
| 08_Niiroku/ニイロク02_御一夜旅行.txt.toml | 1524, 1560, 1563 |
| 10_Chikuni/仲国02_北琴の鉄道.txt.toml | 2171, 2186, 2232 |
| 10_Chikuni/仲国03_北琴鉄道歴史館.txt.toml | 1984 |
| 10_Chikuni/仲国04_z49列車.txt.toml | 1772 |

Ghi chú: 9 dòng vừa có một gasp đã diễn, vừa có một gasp khác được sửa — 9 dòng đó đã tính vào mục "đã sửa" (mục 8), không tính trùng ở đây.

## 10. Katakana khác trong text hiển thị (chỉ đếm, KHÔNG sửa)

- **124 giá trị** VN có katakana ngoài tag `%l` chuẩn (trên tổng 93.153 dòng script) — khớp đúng số đếm của bản quét trước.
- Nguyên nhân chính: **151 tag `%l` thiếu dấu `;` đóng** (đã kiểm chứng độc lập bằng mẫu tag, khớp đúng số đếm 151 của audit Paulette 13; parent đếm lại 19/11 xác nhận 151 là đúng cho dạng này). 151 tag hỏng này nằm trên **118 dòng / 7 file**, tập trung ở: 真闇02_夕凪 (64), Paulette 11_記憶と記録 (54), Paulette 10_見えない傷 (24), Paulette 13_再評価 (5), Chikuni 03 (2), Paulette 12 (1), Paulette 07_支線 (1). Ngoài ra parent đếm thêm **9 tag đóng sai dạng khác** (tag đóng bằng `%l;` rồi mở tag mới ngay — vd 共通12 3129, P10 2032, 日々姫08 1706) trên 6 file nữa, **tổng cộng 160 tag hỏng**. Các thuật ngữ Nhật trong các tag hỏng này — レイルロオド 29, ブレーキ 17, タブレット 9, 客車 7, 8620 7, エアクラ 7, 電車 4, 列車 4... — trông như "katakana sót" khi quét thô, nhưng thực ra là thuật ngữ trong tag bị hỏng, không phải từ chưa dịch.
- Chỉ **13 giá trị / 15 lần xuất hiện** là katakana thực sự đứng ngoài tag, và tất cả đều có chủ ý, không phải từ chưa dịch:
  - 10 chú thích ruby dạng `[JP,n]VN`: ハチロクニイマル 4, ハチロク 2 (đều là `[ハチロクニイマル,3]8620` — tên hiệu + số hiệu), フォースリブート 1, タブレット・レベル 1, メリケン 1 (`[メリケン,2]Mỹ` — đúng quy tắc đã chốt: furigana Meriken thì giữ "Minh Quốc" ở bản dịch chính, đây là chú thích ruby nên giữ nguyên), マイ・マスター 1.
  - 5 lần nhân vật đang bàn về chính chữ Nhật đó: ル 2, キルコト 1, ノ 1 (ハチロクh9 1344/2812 — đang bàn chữ "ru" (ル) với chữ "no" (ノ) trong từ "kirukoto"), ハ 1 (ハチロク08 2944 — "hình chữ V ngược (bát - ハ)").
- 49 lần dùng ー (kéo dài: "Aー", "Hơiiーーーー") và ・ (gạch đầu dòng trong danh sách) là cách viết của người dịch, không phải chữ Nhật sót.
- **Kết luận: KHÔNG có từ katakana nào chưa dịch trong text hiển thị.** Vấn đề thực sự là 151 tag `%l` thiếu dấu `;` — Hieu đang chờ kiểm tra trong game ở Paulette 13 1596 trước khi quyết có quét sửa toàn dự án không (quyết định 12 đang chờ).

## 11. Kết bài

- Đã sửa **1.126 dòng / 210 file**: 318 dòng VN còn nguyên っ, 381 dòng mất gasp cả dòng, 416 dòng mất gasp cuối dòng, 11 dòng mất gasp giữa dòng. Tổng cộng 1.232 ký tự Ư trong các giá trị sửa (383 chữ っ thô được thay bằng Ư + 849 chữ Ư chèn thêm), trong đó có 24 dòng gộp A+B2 (vừa thay っ thô vừa chèn thêm gasp) và 12 dòng có từ 2 gasp trở lên.
- Mọi bản sửa đều đã qua lần kiểm tra thứ hai (đọc lại từng giá trị đối chiếu JP): 13 dòng bị loại, 8 dòng được viết lại, 11 dòng bổ sung từ rà soát audit. Không còn dòng nào trong tập sửa chứa っ ở text hiển thị, không tag nào bị đổi, mọi khối TOML đều parse đúng.
- 254 dòng không sửa đã phân loại rõ: 32 audit đã sửa, 136 VN đã diễn gasp bằng cách khác, 82 cần audit file (chủ yếu lệch dòng — sẽ xử lý khi audit tới file đó), 4 chưa chắc chắn chờ Hieu quyết (trong đó Grand 01 1556: JP là gasp trơ trụi 「っ」, TW và audit đều dịch thành 「……」).
- Việc còn lại: (1) Hieu quyết 4 dòng chưa chắc chắn; (2) khi audit file thì xử lý 82 dòng "cần audit file" trong file đó; (3) quyết định có quét sửa 160 tag `%l` hỏng (151 thiếu dấu `;` + 9 dạng sai khác) sau khi kiểm tra trong game ở Paulette 13 1596; (4) 16 dòng CSV cũ (TOML đã đúng) không cần làm gì — chỉ ghi chú để khỏi nhầm khi đối chiếu CSV/TOML sau này.

---
File dữ liệu đi kèm: `sweep-raw-gasp-wrong.json` — 1.399 mục (1.146 đã sửa + 253 không sửa), mỗi mục có file, key, JP, TW, VN hiện tại, giá trị sửa (nếu có), và lý do.

## 9. Phụ lục 19/11 — 16 dòng đa-っ bị sót (do parent rà soát lại sau khi sweep xong)

**Nguyên nhân:** mẫu liệt kê B1/B2 của sweep chỉ bắt đúng **1** chữ っ (vd `――っ`, `～っ`). Các dòng JP kết thúc bằng **nhiều っ liên tiếp** (っっ, っっっ…) slipped through. Parent đếm lại toàn dự án và tìm thêm 20 dòng: 4 dòng gasp cả dòng (っ×2–4) và 16 dòng gasp cuối dòng (――っっ / ～っっ / …っっ). Trong đó 16 dòng sửa được ngay (mỗi っ → 1 Ư, giữ nguyên mọi thứ khác — đã đọc từng dòng JP + VN gốc trước khi viết, và kiểm tra lại bằng script: giá trị sửa = giá trị TOML cũ chỉ khác ở đúng n chữ Ư chèn trước dấu câu cuối, n = số っ cuối JP). 2 dòng loại (VN đã diễn SFX), 1 dòng "1197" là ảo (xem dưới), 1 dòng đã có trong audit Paulette h1.

**Tổng cập nhật: 1.126 + 16 = 1.142 dòng sửa / 210 file** (cả 12 file phụ lục đều đã nằm trong 210 file của sweep). JSON: 1.380 + 18 = **1.398 mục**.

### 02_Hibiki/日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 2 dòng

```toml
[script]
2201 = "「ƯƯƯ!!!」"
2767 = "「~~~~~~~~~~~~ƯƯ!!!!」"
```

### 07_Nagi_Fukami/lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 3 dòng

```toml
[script]
1124 = "「I——a——~~~~~~~~ƯƯƯƯƯ!!」"
1193 = "「ƯƯ!!!!」"
1209 = "「ƯƯƯƯ!!!!」"
```

### 01_Hachiroku/lr_ハチロクh1_今ひとたびの契り.txt.toml — 1 dòng

```toml
[script]
1216 = "「——ƯƯƯ」"
```

### 01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 2 dòng

```toml
[script]
519 = "「——ƯƯ!!」"
1085 = "「~~~~ƯƯ!!!!!!!!!」"
```

### 01_Hachiroku/ハチロクh7_レトロモダンメイクラヴ.txt.toml — 1 dòng

```toml
[script]
763 = "「Hiu!? Hu——a!? Ng, Ngài Soutetsu! Đợi——đợi——đợi đã——! ~~~~ƯƯ!!!」"
```

### 02_Hibiki/lr_日々姫h2_デザートは食事の前に.txt.toml — 1 dòng

```toml
[script]
971 = "「~~~ƯƯƯ!!!」"
```

### 03_Paulette/ポーレットh7_残業エッチもyシャツで.txt.toml — 1 dòng

```toml
[script]
1270 = "Với vẻ mặt ngây dại thế nào, mà lại khao khát sự xuất tinh, tinh dịch của tôi một cách đơn điệu, đầy tính động vật đến vậy——ƯƯ!!?"
```

### 07_Nagi_Fukami/lr_ふかみh2_セックスの意味.txt.toml — 1 dòng

```toml
[script]
1063 = "「Anh——hau——Soutetsu, anh—— A——fu——a——a——ưm~~~ƯƯƯ!!!」"
```

### 06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml — 1 dòng

```toml
[script]
1062 = "「Khoan! Đợi đã! Kisa――tôi, thở không nổi――tim đập nhanh quá――――ƯƯƯƯƯƯƯ!!!!」"
```

### 07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml — 1 dòng

```toml
[script]
1231 = "「——————ƯƯƯ!!!」"
```

### 08_Niiroku/lr_ニイロクh_誓い。約束.txt.toml — 1 dòng

```toml
[script]
1580 = "「~~~~~~~~~~~~~~~~~~~~~~~~~ƯƯƯƯ!!!!」"
```

### 02_Hibiki/lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml — 1 dòng

```toml
[script]
2330 = "「~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ƯƯƯƯƯƯ!」"
```

### Không sửa trong phụ lục này

- **lr_日々姫h2 973** (already-rendered): JP là tiếng bụng sôi 「ぐうぅ～～～っっっっ！！！！」, VN đã diễn thành "「Guuuuu~~~~!!!!」" — không thêm Ư.
- **ポーレットh7 896** (already-rendered): JP là tiếng mút/chụt 「ぢゅぶるるるるるぅ～～～～～～っっ！！！」, VN đã diễn thành "rột rột rột rột～～～～～～!!!" — không thêm Ư.
- **lr_ふかみh2 1197 — KHÔNG phải dòng sót:** câu rên "おにいひゃっ…ん～～～っっっ！" nằm ở key **1063** trong file TOML (đã sửa ở trên). Key 1197 trong file TOML là câu tỏ tình của Soutetsu ("Anh yêu em!…"), không có gasp — số 1197 chỉ xuất hiện vì CSV có 2 bộ dòng cho cùng tên file (bộ 07_ và bộ 11_Other, xem ghi chú thư mục dưới).
- **ポーレットh1 1008** (already-covered): JP 「っっ！！？」 → audit Paulette h1 đã sửa thành "ƯƯ!!?" — không trùng trong phụ lục này.

### Ghi chú kèm (phát hiện khi rà soát phụ lục)

- **CSV "11_Other" ≠ TOML-2 "11_Other":** CSV Trang tính 3 liệt kê 6 file dưới `11_Other/` (lr_ふかみh1, lr_ふかみh2, ふかみh1, ふかみh2_homesweethome, ふかみh3, lr追加_ひよこ電車姫オリヴィ), nhưng trong TOML-2 chỉ có 1 file ở `11_Other/` (ひよこ電車姫オリヴィ); 5 file còn lại nằm ở `07_Nagi_Fukami/`. Khi audit phải xác minh file theo **tên file + nội dung khớp**, không theo đường dẫn thư mục.
- **lr_ふかみh2 có 2 bộ dòng trong CSV:** bộ `07_` và bộ `11_Other` cùng tên file, cùng 291 key, nhưng nội dung khác nhau ở 286/291 key (cùng câu nhưng khác key — vd câu rên trên ở 1063 trong bộ 11_Other nhưng ở 1197 trong bộ 07_). File TOML khớp bộ **11_Other** ở 286/291 key, nên khi audit file này phải lấy bộ 11_Other làm nguồn JP/TW; bộ 07_ không có file TOML tương ứng (câu dẫn "Âm đạo và dương vật…" ở key 1063 bộ 07_ không tồn tại trong bất kỳ file TOML nào).
- **Đếm lại tag `%l` lỗi (parent, 19/11): 160 tag** (151 thiếu dấu `;` cuối — đúng số sweep đếm — + 9 dạng sai khác, vd tag đóng bằng `%l;` rồi mở tag mới ngay: 共通12 3129, P10 2032, 日々姫08 1706) trên 13 file. Tập trung ở 真闇02 (64), ポーレット11 (54), ポーレット10 (24). Con số chính xác vẫn cần thống nhất trước khi quyết quét toàn dự án; câu hỏi gửi Hieu (kiểm tra trong game ở Paulette 13 1596) không đổi.
- **Audit h6 sửa lại 2 giá trị sweep (parent, 19/11):** h6 1271 — JP có hai っ (震えてっ――っ！？) nhưng sweep chỉ diễn 1 Ư ("run rẩy——Ư!?"); giá trị audit ("run rẩyƯ——Ư!?") đúng theo quy tắc đa-っ (1 Ư/1 っ) nên thay thế giá trị sweep. h6 784 — sweep chỉ thêm gasp Ư; audit sửa thêm わらひ→"ehm" (sweep để "em"); giá trị audit thay thế. 2 dòng h6 audit tìm ra mà sweep bỏ sót (815 gasp đầu dòng, 850 hai gasp cuối) chỉ nằm trong file audit h6, không thêm vào JSON sweep. Tổng số dòng sửa của sweep không đổi (1.142).

## 10. Phụ lục 19/11 — hiệu đính từ audit lr_h1/lr_h2 (audit thay thế sweep)

- 3 giá trị sweep bị audit thay thế (đọc kỹ hơn từ JP): lr_h1 998 "Kyufu" → "Kíuphù" (JP きゅっふっ); lr_h1 1005 "Hya" → "Hia" (JP ひあっ, không phải ひゃ); lr_h1 1083 mảnh La-tinh "ryu/chu ru/chu ro/chu mu" → Việt hóa đầy đủ "rộp/rột/chụt" + ちゅうっ → "chụụt" theo quy tắc độ dài âm (1+う).
- 4 dòng sweep ghi "already-rendered" nhưng audit chứng minh gasp bị mất: lr_h1 1044 (JP ba tiếng っ đứng riêng), 1045 (JP っ đầu/giữa/cuối dòng), lr_h2 1009 (JP っ cuối dòng sau そうてつく――), 1124 (JP っ cuối dòng sau ん～～～). Đã chuyển sang khối sửa với giá trị audit (khối TOML §8 và JSON đã cập nhật; §9.4 đã gỡ 4 dòng khỏi danh sách already-rendered).
- 1 dòng sweep bỏ sót hoàn toàn: lr_h1 1077 (JP っ！ đầu dòng, VN chỉ còn "!") — đã thêm mới vào JSON và khối TOML §8.
- Tổng cập nhật: sửa 1.142 → 1.147; already-rendered 138 → 134 (bảng §9.4 liệt kê 132 dòng fix rỗng + 2 dòng fix == old_vn là lr_日々姫h2 973 và ポーレットh7 896, không đổi giá trị); không sửa 256 → 252 (= 32 + 134 + 82 + 4); tổng mục JSON 1.398 → 1.399. Khối TOML §8: lr_h1 13 → 16 dòng, lr_h2 6 → 8 dòng.
- Đính chính thêm: các dòng B1/B2 trong bảng §1 trước đây chưa gồm +16 dòng của phụ lục §9 (B1 ghi 381, thực tế theo kind là 384; B2 ghi 416, thực tế 429) — nay đã sửa về đúng số liệu JSON theo kind: B1 387, B2 431, B2-giữa-dòng 11, A 318, tổng 1.147. Tương tự, mục "đã diễn gasp" trong §1 ghi 136 nhưng thực tế kind already-rendered là 138 (gồm 2 dòng fix == old_vn nói trên) — nay đã sửa thành 134 sau khi trừ 4 dòng hiệu đính.

## 11. Phụ lục 20/11 — audit file 15 bác bỏ 1 mục sweep (1474 không phải gasp)

- 共通15 key 1474: JP 「ブロワーっ！！」 — っ cuối câu gắn vào danh từ chuyên môn đang hét lên (blower), là っ nhấn mạnh, KHÔNG phải tiếng hít/gasp. Giá trị sweep ("Thiết bị thổi gióƯ!!") sai — vi phạm chính quy tắc loại trừ của sweep (っ nhấn mạnh cuối câu gắn vào từ thì không thêm Ư). 4 mẫu giống hệt trong cùng file (1835/1973/2000/2113) sweep không hề gắn cờ và VN cũng không diễn thành Ư — nhất quán với việc bác bỏ.
- Đã chuyển 1474 sang kind mới "not-a-gasp" (fix rỗng), gỡ khỏi khối TOML §8 của file 15 (2 dòng → 1 dòng, chỉ còn 1906).
- Tổng cập nhật: sửa 1.147 → 1.146 (lost-gasp-whole 387 → 386); không sửa 252 → 253 (= 32 + 134 + 82 + 4 + 1 not-a-gasp); tổng mục JSON 1.399 không đổi.
