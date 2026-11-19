# Audit 00_Common file 07 — 共通07_鍵.txt.toml

**Ngày kiểm toán:** 19/11/2026
**Tệp TOML:** `00_Common/共通07_鍵.txt.toml` — md5 `ee6e26eef127ff6d76a5ddb65e2242f9`, BOM, CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 331 hàng `[script]`.
**Kết quả: 34/331 dòng sai (10,3%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Đại từ xưng hô (pronoun) | 19 |
| Thuật ngữ (terminology) | 7 |
| Lỗi nhỏ (minor) | 5 |
| Thẻ gloss %l (tag) | 1 |
| Sai nghĩa (meaning) | 1 |
| Tiếng thở/gasp (gasp) | 1 |
| **Tổng** | **34** |

**Theo loại dòng:** thoại 30/210 sai (14,3%), độc thoại 4/121 sai (3,3%).
**Theo nhân vật:** 双鉄 (Soutetsu) 17, ポーレット (Paulette) 11, れいな (Reina) 1, ハチロク (Hachiroku) 1, độc thoại 4.

Nhóm đại từ (19) chia nhỏ: Soutetsu gọi Paulette "cô" → "em" (12 dòng); Soutetsu tự xưng "em" (2 dòng: 1777, 1801); B4 — Paulette gọi "Soutetsu-kun" → "anh Soutetsu" (5 dòng: 1674, 1684, 1970, 1972, 2133).

File này sạch hơn mặt bằng chung: **không có dòng nào lệch dòng** (misaligned), không có chuỗi xoay, không có nhiễm chéo — toàn bộ 34 lỗi đều là lỗi tại chỗ (sai đại từ, sai thuật ngữ, dịch lệch nhỏ), sửa được ngay không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục (thư mục CSV và TOML-2 không khớp nhau ở nhiều file khác — file này chỉ có một bộ hàng nên không bị ảnh hưởng).
- **CSV vs TOML:** VN khớp tuyệt đối 140 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 330/331. Hàng duy nhất khác biệt chỉ là **khoảng trắng thừa ở cuối** (không phải lỗi dịch) — bộ dữ liệu sạch, JP comment khớp CSV3.
- **Sweep っ (gasp):** sweep có đúng 1 mục cho file này (2144) — đã xác nhận là gasp mất hẳn, đưa vào fix list. Không có sweep-missed gasp nào khác (xem §5).
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có hàng VN == TW trừ 1433 `「…………」` (dấu lửng, không phải lỗi).

## 3. Các lỗi đã sửa (34 dòng)

### 1417 — れいな — terminology

**JP:** 「重たいんですよぉ、\x%l8620;#00ffc040;8620%l;#;は。 ⏎ れいなのキハ[レイナナエス,3]07-sが全長19.7mで総重量27.2tですからぁ」

**TW:** 「\x%l8620;#00ffc040;８６２０%l;#;可重啦。玲奈的Ｋｉｈａ０７－Ｓ全長１９．７公尺，總重量才２７．２噸呢」

**VN cũ:** 「\x%l8620;#00ffc040;8620%l;#; nặng lắm đó nha~. ⏎ Kiha 07S của Reina tổng chiều dài 19.7m mà tổng trọng lượng cũng chỉ có 27.2 tấn thôi đó~」

**Fix:** 「\x%l8620;#00ffc040;8620%l;#; nặng lắm đó nha~. KiHa 07S của Reina tổng chiều dài 19.7m mà tổng trọng lượng cũng chỉ có 27.2 tấn thôi đó~」

KiHa theo quyết định 19/11 (#14, cách viết chính thức của JR: Ki = 気動車, Ha = 普通車); "Kiha" sai chính tả.

### 1423 — ポーレット — meaning

**JP:** 「――すごい」

**TW:** 「——天啊」

**VN cũ:** 「——Khủng khiếp quá.」

**Fix:** 「——Khủng thật。」

すごい ở đây là thán phục trước quy mô (TW: 天啊 — "trời ơi"); "Khủng khiếp quá" đọc thành "kinh khủng/khiếp sợ", sai sắc thái. (Lượt soát 2: bản cũ có 「」, fix lần 1 gõ tay làm rơi — đã khôi phục.)

### 1431 — れいな — minor

**JP:** 「『中古\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、機関車一式』―― ⏎ はわわ、これ、ハチロクさんたちのことですねぇ」

**TW:** 「“舊\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;、機車一套”——哇，這個應該說的是八六小姐她們吧」

**VN cũ:** 「'Trọn bộ \x%lレイルロオド;#00ffc040;Railord%l;#; và đầu máy cũ'—— ⏎ Oa, cái này, là nói về nhóm chị Hachiroku đó nha~」

**Fix:** 「'Trọn bộ \x%lレイルロオド;#00ffc040;Railord%l;#; cũ và đầu máy'—— Oa, cái này, là nói về nhóm chị Hachiroku đó nha~」

中古 bổ nghĩa cho レイルロオド (Railord cũ), không phải 機関車; bản cũ đặt "cũ" vào đầu máy — sai phạm vi bổ nghĩa. (Lượt soát 2: fix lần 1 dùng chuỗi thay thế sai — thẻ %l chen giữa "Railord" và "và đầu máy cũ" nên replace không khớp, fix thực chất chưa sửa gì; đã sửa lại bằng chuỗi đúng.)

### 1445 — ハチロク — minor

**JP:** 「……昨日のお話、の続きでしょうね」

**TW:** 「……是來繼續昨天那個話題的吧」

**VN cũ:** 「……Chắc là tiếp tục, câu chuyện ngày hôm qua nhỉ.」

**Fix:** 「……Chắc là chuyện tiếp theo của ngày hôm qua nhỉ。」

Trật tự từ tiếng Việt lủng củng ("Chắc là tiếp tục, câu chuyện ngày hôm qua nhỉ"); JP: 「昨日のお話、の続きでしょうね」 = chuyện tiếp theo của hôm qua. (Lượt soát 2: bản cũ có 「」, fix lần 1 gõ tay làm rơi — đã khôi phục.)

### 1665 — 双鉄 — pronoun

**JP:** 「無いというなら、ポーレットにはもっと無い。 ⏎ それより、後処理だ。怪我などないか？」

**TW:** 「不怪我的話，那就更不怪你了。不說這個了，趕緊開始收拾吧。你沒有受傷吧？」

**VN cũ:** 「Nếu tôi không có lỗi, thì Paulette lại càng không. ⏎ Quan trọng hơn là dọn dẹp hậu quả đã. Cô có bị thương không?」

**Fix:** 「Nếu tôi không có lỗi, thì Paulette lại càng không. Quan trọng hơn là dọn dẹp hậu quả đã. Em có bị thương không?」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1674 — ポーレット — pronoun

**JP:** 「いえ、そんなっ！　双鉄くんの責任なんて」

**TW:** 「不，別這麼說！這不怪雙鐵君」

**VN cũ:** 「Không, đâu có! Sao lại là lỗi của Soutetsu-kun được.」

**Fix:** 「Không, đâu có! Sao lại là lỗi của anh Soutetsu được.」

Paulette gọi Soutetsu: 双鉄くん → "anh Soutetsu" theo quyết định B4 (19/11, Hieu ủy quyền Muse chốt; ngoại lệ tên rên đã bãi bỏ — gọi tên trần/"-kun" đều sai).

### 1684 — ポーレット — pronoun

**JP:** 「任せてください。双鉄くん」

**TW:** 「交給我吧，雙鐵君」

**VN cũ:** 「Cứ giao cho tôi. Soutetsu-kun.」

**Fix:** 「Cứ giao cho tôi. Anh Soutetsu.」

Paulette gọi Soutetsu: 双鉄くん → "anh Soutetsu" theo quyết định B4 (19/11, Hieu ủy quyền Muse chốt; ngoại lệ tên rên đã bãi bỏ — gọi tên trần/"-kun" đều sai). (Lượt soát 2: "anh Soutetsu" đứng đầu câu sau dấu chấm phải viết hoa "Anh" — fix lần 1 giữ thường là sai.)

### 1700 — 双鉄 — terminology

**JP:** 「思い出せないか？　自分がいつごろ、 ⏎ 汰斗さんに連れられ、この御一夜にやってきたのか」

**TW:** 「你想不起來了嗎？汰斗老爺帶著你來到御一夜，具體是什麼時候的事？」

**VN cũ:** 「Em không nhớ được sao? Khoảng thời gian nào, ⏎ em được ông Taito đưa đến Ohimitera này.」

**Fix:** 「Em không nhớ được sao? Khoảng thời gian nào, em được ông Taito đưa đến Ohitoyo này.」

御一夜 → Ohitoyo theo quyết định 19/11; "Ohimitera" là dạng cũ.

### 1704 — 双鉄 — pronoun

**JP:** 「心当たりの倉庫があるのか」

**TW:** 「你知道可能在什麼倉庫裡嗎」

**VN cũ:** 「Cô biết nhà kho đó ở đâu sao?」

**Fix:** 「Em biết nhà kho đó ở đâu sao?」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1711 — 双鉄 — pronoun

**JP:** 「それほどに大きく重い物であれば、 ⏎ そう簡単に格納も移動も出来ない、ということになるか」

**TW:** 「像這樣一件龐然大物，無論是存放還是挪動都不簡單，對吧」

**VN cũ:** 「Một thứ to lớn và nặng nề như vậy, ⏎ thì không thể dễ dàng cất giấu hay di chuyển được, ý cô là vậy sao.」

**Fix:** 「Một thứ to lớn và nặng nề như vậy, thì không thể dễ dàng cất giấu hay di chuyển được, ý em là vậy sao.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1723 — ポーレット — terminology

**JP:** 「全長が16.7[メートル]m、全高が3.8m。 ⏎ 機関車だけでも、\x%l運転整備重量;#00ffc040;運転整備重量%l;#;が39.8[トン]tもあるんです」

**TW:** 「全長１６．７公尺，全高３．８公尺。單算機車，都有３９．８噸的\x%l運転整備重量;#00ffc040;行駛整備質量%l;#;」

**VN cũ:** 「Tổng chiều dài là 16.7m, tổng chiều cao là 3.8m. ⏎ Chỉ tính riêng đầu máy thôi, \x%l運転整備重量;#00ffc040;khối lượng chỉnh bị vận hành%l;#; đã lên tới 39.8 tấn rồi.」

**Fix:** 「Tổng chiều dài là 16.7m, tổng chiều cao là 3.8m. Chỉ tính riêng đầu máy thôi, \x%l運転整備重量;#00ffc040;khối lượng vận hành%l;#; đã lên tới 39.8 tấn rồi.」

運転整備重量 = khối lượng vận hành (trọng lượng khi sẵn sàng chạy); "khối lượng chỉnh bị vận hành" — "chỉnh bị" không phải từ tiếng Việt (gõ sai), làm câu tối nghĩa.

### 1753 — 双鉄 — pronoun

**JP:** 「知っている――のだよな。 ⏎ 右田のことは」

**TW:** 「右田家的事情，你——是知道的吧」

**VN cũ:** 「Cô biết——đúng không. ⏎ Chuyện của nhà Migita ấy.」

**Fix:** 「Em biết——đúng không. Chuyện của nhà Migita ấy.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1777 — 双鉄 — pronoun

**JP:** 「ああ、うん。今行く」

**TW:** 「啊——好。這就去」

**VN cũ:** 「À, vâng. Em ra ngay đây.」

**Fix:** 「À, vâng. Tôi ra ngay đây.」

Soutetsu không bao giờ tự xưng "em" (tiền lệ file 02: 8 dòng "em" đều sai). Người gọi là người lớn tuổi hơn (Mayami/Paulette, xưng "vâng"); "tôi" là dạng mặc định đúng — "anh" chỉ dùng khi đối thoại với người nhỏ hơn.

### 1799 — ハチロク — minor

**JP:** 「まぁ。 ⏎ まさしく塞翁が馬ですね、双鉄様」

**TW:** 「嗯。這可真是塞翁失馬焉知非福呀，雙鐵少爺」

**VN cũ:** 「Chà. ⏎ Đúng là tái ông thất mã ngài nhỉ, ngài Soutetsu.」

**Fix:** 「Chà. Đúng là tái ông thất mã nhỉ, ngài Soutetsu.」

Thừa một "ngài": JP chỉ có một 双鉄様 (đã dịch là "ngài Soutetsu" ở cuối câu); "tái ông thất mã ngài nhỉ" gắn "ngài" sai chỗ.

### 1801 — 双鉄 — pronoun

**JP:** 「ふむ。ならばその時には」

**TW:** 「嗯。那有需要的時候就用吧」

**VN cũ:** 「Hừm. Vậy thì khi nào cần em sẽ dùng.」

**Fix:** 「Hừm. Vậy thì khi nào cần anh sẽ dùng.」

Soutetsu tự xưng "em" — sai (nói với Hachiroku, người nhỏ hơn; Soutetsu xưng "anh" với Hachiroku).

### 1830 — 双鉄 — terminology

**JP:** 「だご汁はいいな。 ⏎ 『ああ、御一夜だ』という気がするよ」

**TW:** 「團兒湯真是個好東西。喝著就有一股御一夜的味道」

**VN cũ:** 「Canh Dago ngon thật đấy. ⏎ Cảm giác đúng kiểu 'A, Ohimitera đây rồi'.」

**Fix:** 「Canh Dago ngon thật đấy. Cảm giác đúng kiểu 'A, Ohitoyo đây rồi'.」

御一夜 → Ohitoyo theo quyết định 19/11.

### 1845 — 双鉄 — pronoun

**JP:** 「わかった。いったん下りてくれ」

**TW:** 「好的。你先下來吧」

**VN cũ:** 「Hiểu rồi. Cô xuống trước đi đã.」

**Fix:** 「Hiểu rồi. Em xuống trước đi đã.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1863 — 双鉄 — pronoun

**JP:** 「誰の責任かといえば、僕のだろう。 ⏎ 慌てさせたのもはしごを手放したのも、僕だからな」

**TW:** 「實在要說的話，這也是我的責任。讓你緊張的，鬆開梯子的都是我」

**VN cũ:** 「Nếu nói là lỗi của ai, thì chắc là của tôi rồi. ⏎ Người làm cô hoảng hốt và buông tay khỏi cái thang đều là tôi mà.」

**Fix:** 「Nếu nói là lỗi của ai, thì chắc là của tôi rồi. Người làm em hoảng hốt và buông tay khỏi cái thang đều là tôi mà.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1886 — ポーレット — minor

**JP:** 「覚悟」

**TW:** 「心理」

**VN cũ:** 「Chuẩn bị tinh thần?」

**Fix:** 「Chuẩn bị tinh thần!」

JP 覚悟 là một từ cụt, dạng cảm thán/quyết tâm ("Quyết tâm rồi!"); bản cũ thêm "?" biến thành câu hỏi, đảo ngược thái độ người nói.

### 1895 — ポーレット — terminology

**JP:** 「あの、旧\x%l帝鉄;#00ffc040;帝鉄%l;#;から施設の譲り渡しを受けたとき…… ⏎ 個人に貸与している物だから手を触れるなって言われて」

**TW:** 「怎麼說呢，接受前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;轉讓設施的時候……我被警告過——別去碰那些租借給個人的設施」

**VN cũ:** 「À ừm, lúc nhận bàn giao cơ sở vật chất từ \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ…… ⏎ họ có dặn là những thứ đang cho cá nhân thuê thì đừng có động vào.」

**Fix:** 「À ừm, lúc nhận bàn giao cơ sở vật chất từ \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ…… họ có dặn là những thứ đang cho cá nhân thuê thì đừng có động vào.」

帝鉄 → Teitetsu theo quyết định 19/11 (#6, bỏ "Đường sắt Hoàng gia" — 帝鉄 là 帝国鉄道, không phải 皇室).

### 1926 — 双鉄 — pronoun

**JP:** 「わかる気がする。意識の外へと追いやったんだな？ ⏎ 気にすれば、何もかもが手につかなくなってしまうから」

**TW:** 「我懂。你是故意忘了這件事吧？總是在意這種事情，就沒辦法專心去做別的事情了」

**VN cũ:** 「Tôi hiểu mà. Cô đã cố gạt nó ra khỏi tâm trí đúng không? ⏎ Vì nếu cứ bận tâm, cô sẽ chẳng làm nên trò trống gì cả.」

**Fix:** 「Tôi hiểu mà. Em đã cố gạt nó ra khỏi tâm trí đúng không? Vì nếu cứ bận tâm, em sẽ chẳng làm nên trò trống gì cả.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1930 — 双鉄 — pronoun

**JP:** 「随分と熱心に見ていたようだが――」

**TW:** 「我看你剛才，看得還挺認真——」

**VN cũ:** 「Lúc nãy thấy cô xem chăm chú lắm mà——」

**Fix:** 「Lúc nãy thấy em xem chăm chú lắm mà——」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1949 — 双鉄 — pronoun

**JP:** 「引渡し時の注意をずっと、守り続けてきたわけか」

**TW:** 「接受轉讓之後，一直都遵守了這個要求嗎」

**VN cũ:** 「Nghĩa là cô vẫn luôn tuân thủ lời dặn lúc bàn giao sao.」

**Fix:** 「Nghĩa là em vẫn luôn tuân thủ lời dặn lúc bàn giao sao.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1964 — 双鉄 — pronoun

**JP:** 「そうか。ならば任せる」

**TW:** 「是嗎。那就交給你了」

**VN cũ:** 「Vậy sao. Thế thì giao cho cô đấy.」

**Fix:** 「Vậy sao. Thế thì giao cho em đấy.」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 1970 — ポーレット — pronoun

**JP:** 「はい――これ、見てください双鉄くん。 ⏎ 背表紙……ほら、『会計記録』ってあります」

**TW:** 「是的——看看這個吧，雙鐵君。這書脊……你看，是《會計記錄》」

**VN cũ:** 「Vâng——Soutetsu-kun, anh xem cái này đi. ⏎ Gáy sách này……anh thấy không, có ghi 'Hồ sơ kế toán'.」

**Fix:** 「Vâng——anh Soutetsu, anh xem cái này đi. Gáy sách này……anh thấy không, có ghi 'Hồ sơ kế toán'.」

Paulette gọi Soutetsu: 双鉄くん → "anh Soutetsu" theo quyết định B4 (19/11, Hieu ủy quyền Muse chốt; ngoại lệ tên rên đã bãi bỏ — gọi tên trần/"-kun" đều sai).

### 1972 — ポーレット — pronoun

**JP:** 「そうなんです。 ⏎ 双鉄くんの言うとおりな感じで、だから」

**TW:** 「是的。和雙鐵君說得一樣，所以」

**VN cũ:** 「Đúng vậy ạ. ⏎ Cảm giác đúng như Soutetsu-kun nói, thế nên.」

**Fix:** 「Đúng vậy ạ. Cảm giác đúng như anh Soutetsu nói, thế nên.」

Paulette gọi Soutetsu: 双鉄くん → "anh Soutetsu" theo quyết định B4 (19/11, Hieu ủy quyền Muse chốt; ngoại lệ tên rên đã bãi bỏ — gọi tên trần/"-kun" đều sai).

### 2012 — 双鉄 — pronoun

**JP:** 「ポーレット、大丈夫か怪我はないか？」

**TW:** 「波萊特，你沒事吧，有沒有受傷？」

**VN cũ:** 「Paulette, cô không sao chứ, có bị thương ở đâu không?」

**Fix:** 「Paulette, em không sao chứ, có bị thương ở đâu không?」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 2048 — 双鉄 — pronoun

**JP:** 「本当に平気か？　痛むのではないか？ ⏎ 顔が赤く呼吸が荒いぞ？」

**TW:** 「真的沒事嗎？有沒有哪裡覺得痛？你的臉很紅，呼吸也很急促」

**VN cũ:** 「Cô thực sự không sao chứ? Có đau ở đâu không? ⏎ Mặt cô đỏ bừng, hơi thở cũng gấp gáp lắm đấy?」

**Fix:** 「Em thực sự không sao chứ? Có đau ở đâu không? Mặt em đỏ bừng, hơi thở cũng gấp gáp lắm đấy?」

Soutetsu gọi Paulette: "cô" → "em" theo quyết định 19/11 (#13, cặp xưng hô "anh – em").

### 2133 — ポーレット — pronoun

**JP:** 「双鉄くん！」

**TW:** 「雙鐵君！」

**VN cũ:** 「Soutetsu-kun!」

**Fix:** 「Anh Soutetsu!」

Paulette gọi Soutetsu: 双鉄くん → "anh Soutetsu" theo quyết định B4 (19/11, Hieu ủy quyền Muse chốt; ngoại lệ tên rên đã bãi bỏ — gọi tên trần/"-kun" đều sai). (Lượt soát 2: cả dòng chỉ là một tiếng gọi độc lập, đầu câu phải viết hoa "Anh" — fix lần 1 giữ thường là sai.)

### 2144 — 双鉄 — gasp

**JP:** 「っ！」

**TW:** 「！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

Sweep lost-gasp-whole (JP 「っ！」 nguyên dòng, TW 「！」): VN chỉ còn "!" — mất âm. Fix theo sweep: 「Ư!」.

### 2436 — monologue — minor

**JP:** 口を結んで手と目を動かす。 ⏎ 部屋の散らかり具合からして、汰斗さんは雑な性格だろう。

**TW:** 我閉上了嘴，開始仔細地找起來。房間這麼亂，想必汰斗老爺也是個很隨性的人吧。

**VN cũ:** Tôi mím môi, bắt đầu di chuyển tay và mắt. ⏎ Nhìn căn phòng bừa bộn thế này, chắc hẳn ông Taito là người có tính cách cẩu thả.

**Fix:** Tôi mím môi, bắt tay vào tìm kiếm. Nhìn căn phòng bừa bộn thế này, chắc hẳn ông Taito là người có tính cách cẩu thả.

"Bắt đầu di chuyển tay và mắt" là dịch từng chữ vụng về của 手と目を動かす (bắt tay vào tìm kiếm).

### 2525 — monologue — tag

**JP:** 整備ボディのれいなにじいっと見守られる中、 ⏎ ポーレットがなにやら真剣に説明している。

**TW:** 波萊特在整備體玲奈的注視下，認真地向我們解說著什麼。

**VN cũ:** Dưới ánh mắt chăm chú theo dõi của Reina trong \x%l整備体;#00ffc040;thân chính%l;#;, ⏎ Paulette đang nghiêm túc giải thích điều gì đó.

**Fix:** Dưới ánh mắt chăm chú theo dõi của Reina trong thân bảo trì, Paulette đang nghiêm túc giải thích điều gì đó.

VN tự thêm thẻ gloss %l (JP không có thẻ — 整備ボディ là chữ thường trong JP); theo tiền lệ reina02/file 02 (2693), thẻ gloss VN tự thêm phải gỡ. Gloss "thân chính" cũng sai: 整備体 = "thân bảo trì" theo quyết định #11. Fix: bỏ thẻ, dùng "thân bảo trì" dạng chữ thường.

### 2543 — monologue — terminology

**JP:** 御一夜鉄道社長として、御一夜市長として―― ⏎ \x%l8620;#00ffc040;8620%l;#;を発見し、そこに未来を見出したいのだろう。

**TW:** 畢竟她是御一夜鐵路的社長，是御一夜的市長——因此她也想找出\x%l8620;#00ffc040;８６２０%l;#;，為公司和城市帶來新的希望吧。

**VN cũ:** Với tư cách là giám đốc Đường sắt Ohimitera, với tư cách là thị trưởng Ohimitera—— ⏎ Có lẽ cô ấy muốn tìm thấy \x%l8620;#00ffc040;8620%l;#; và nhìn thấy tương lai ở đó.

**Fix:** Với tư cách là giám đốc Đường sắt Ohitoyo, với tư cách là thị trưởng Ohitoyo—— Có lẽ cô ấy muốn tìm thấy \x%l8620;#00ffc040;8620%l;#; và nhìn thấy tương lai ở đó.

御一夜 → Ohitoyo theo quyết định 19/11 (2 chỗ trong dòng).

### 2636 — monologue — terminology

**JP:** 産まれこそは帝都だが、育ちのいくらかは御一夜だ。 ⏎ 問われればすぐに思い当たる。

**TW:** 雖然我出生於帝都，但多少也算是在御一夜長大的人。聽見這個問題立刻就能給出答案。

**VN cũ:** Dù sinh ra ở Đế đô, nhưng tôi cũng lớn lên ở Ohimitera một thời gian. ⏎ Nên khi được hỏi, tôi liền nhớ ra ngay.

**Fix:** Dù sinh ra ở Đế đô, nhưng tôi cũng lớn lên ở Ohitoyo một thời gian. Nên khi được hỏi, tôi liền nhớ ra ngay.

御一夜 → Ohitoyo theo quyết định 19/11.


## 4. Kiểm tra chéo

### 4.1 Chuỗi xoay (rotation chains)
**Không có.** Không dòng nào cần dịch lại từ JP do lệch dòng — mọi fix đều sửa tại chỗ trên bản VN cũ. Không cần kiểm tra chuỗi xoay trước khi dịch mới vì không có dòng nào dịch mới.

### 4.2 Nhiễm chéo file (cross-file contamination)
**Không có.** Đã đối chiếu các giá trị VN trùng lặp trong file với chỉ mục VN toàn dự án: chỉ có 2 giá trị trùng là các câu chung chung `「Ra là vậy。」` (1737/1965) và `「Vâng。」` (1844/1977) — cả hai đều đúng ngữ cảnh, không phải nhiễm chéo. Không có dòng nào thuộc 3 trường hợp nhiễm đã biết (Hachiroku 12 → 夜の嵐, hearing → stove, obasan ↔ sleeper).

### 4.3 Thẻ gloss %l
- Số lượng thẻ JP == VN trên mọi hàng, **trừ 2 hàng**:
  - **2525 — VN tự thêm thẻ** (đã sửa, xem fix list): JP là chữ thường `整備ボディ`, VN tự thêm thẻ gloss với gloss sai "thân chính". Gỡ thẻ, dùng "thân bảo trì" theo quyết định #11.
  - **2547 — thẻ phía JP bị tách** (xem §7, không phải lỗi VN, không tính vào 34): thẻ gloss JP bị ngắt bởi ký tự xuống dòng trước khi đóng; phía VN đóng thẻ đúng và gloss "trưởng hầm rượu" là đúng.
- **0 thẻ VN lỗi định dạng** (không có thẻ nào thiếu dấu `;` đóng). File này không nằm trong 13 file có thẻ lỗi đã tổng hợp toàn dự án.

### 4.4 Sweep đại từ Soutetsu (kiểm tra bằng máy + đọc tay)
- **"cô" gọi Paulette:** quét được 8 "cô" thường + 4 "Cô" hoa đầu câu (1665, 1704, 1753, 1845) — cả 12 đều sai, đã sửa hết thành "em". Lưu ý: quét phân biệt hoa/thường là bắt buộc — quét chỉ thường sẽ sót 4 dòng.
- **Soutetsu tự xưng "em":** chỉ 1777 và 1801 sai. Hai dòng "em" khác là đúng vì "em" ở đó là người được gọi, không phải Soutetsu tự xưng: 1700 "em" = Hachiroku (người nghe), 1808 "em" = Hibiki (người nghe).
- **Soutetsu tự xưng "mình":** 6 dòng (1935, 2101, 2348, 2430, 2550, 2630) — tất cả đều đúng theo tiền lệ hearing (dạng phụ thuộc/quan hệ/sở hữu/phản thân, không phải tự xưng trong đối thoại trực tiếp).
- **Soutetsu tự xưng "anh":** 6 dòng (1670, 1673, 1709, 1922, 2040, 2132) — tất cả đều nói với người nhỏ hơn, đúng.

### 4.5 Kiểm tra gasp っ
- Chỉ **2144** mất gasp (JP `「っ！」` nguyên dòng, VN chỉ còn "!") — đã sửa thành `「Ư!」`, khớp với sweep.
- Các っ còn lại đều đã được xử lý đúng: っ trong từ (きゃっ → "Á", んっ → "Ưm"), っ nhấn mạnh cuối câu gắn với từ (không phải gasp, không thêm Ư), 1754/1755 và 2279 (ハっと → "nín thở"), 2534 (dấu gạch ngang ngắt câu giữ nguyên), 2425 (ぽんっ — hành động đã được diễn tả bằng lời). Không có gasp nào bị sweep bỏ sót.
- **0 ký tự っ thô còn sót trong VN.**

### 4.6 Thuật ngữ mở (chưa có quyết định của Hieu)
- **まいてつ và 市電 không xuất hiện trong file này** — không cần xử lý.
- **Ohimitera → Ohitoyo:** đã sửa 5 lần xuất hiện trên 4 dòng (1700, 1830, 2543 ×2, 2636). Tính đến hết file 07: tổng ban đầu 134 lần ở 15 file 00_Common, đã sửa ở file 02 (5), 03 (3), 04 (1 — key 2658, đã kiểm chứng), 05 (11), 07 (5) → còn lại 109 lần, tập trung ở file 14 (30), 09 (15), 15 (15), 10 (14), 11 (12), 01 pilot (8, chưa chốt), 12 (6), 06 (4), 13 (3), 08 (2).

## 5. Đã kiểm tra, không sai (ghi lại để khỏi sửa lại lần sau)

- **1910 — KHÔNG SỬA.** Paulette tự sửa "Soutetsu-san" thành "Soutetsu-kun" ngay trong câu (`「双鉄さん……あ、双鉄くん」`) — sự đổi hậu tố -kun chính là điểm nhấn của câu; giữ "Soutetsu-kun" là đúng. (Ngoại lệ nội dung của khóa B4 — xem §6.)
- **2342 — KHÔNG SỬA.** Độc thoại của Soutetsu nhận ra cách gọi đã đổi từ "anh" sang "kun" (`"さん"から"くん"に変わったか`) — chính sự phân biệt san/kun là nội dung của dòng; giữ nguyên.
- **1893 — KHÔNG SỬA.** "anh Soutetsu" cho 兄さん, "anh hai" cho にぃにぃ — hai cách gọi khác nhau, dịch khác nhau là đúng.
- **1898 / 2070 / 2103 — KHÔNG SỬA.** Mayami gọi "Sou-chan" — biệt danh thân mật, nhất quán cả 3 lần.
- **1979 — KHÔNG SỬA.** JP tự có điểm lạ (nhà kho mô tả là 石造 — bằng đá — nhưng lại nói xây bằng れんが — gạch); VN giữ cả hai như JP, không "sửa" JP.
- **2025 — KHÔNG SỬA.** "bố tôi bảo" — bố là nguồn tin đã được xác lập ở 2099 ("パパから").
- **2119 — KHÔNG SỬA.** "Chị, chị hai!!?" — cách diễn tả nói lắp, đúng ngữ cảnh.
- **2121 — KHÔNG SỬA.** Hai tiếng cảm thán trong một key; nội dung VN đúng như đã viết.
- **2279 — KHÔNG SỬA.** "khẽ nín thở" — diễn tả đúng ハっと.
- **2425 — KHÔNG SỬA.** ぽんっ — hành động đã được diễn tả bằng lời.
- **2534 — KHÔNG SỬA.** Dấu gạch ngang ngắt câu giữ nguyên, đúng.

## 6. Ghi chú về khóa B4 (ngoại lệ nội dung)

Khóa B4 (Paulette gọi Soutetsu trần/"-kun" → "anh Soutetsu") được áp dụng cho cả 5 dòng trong file này. Hai dòng **1910 và 2342** là ngoại lệ nội dung đã ghi ở §5: ở đó chính sự phân biệt san → kun là nội dung của câu, nên giữ nguyên cách diễn "Soutetsu-kun"/"kun". Nếu Hieu không đồng ý với cách xử lý hai dòng này, nói lại — còn các dòng gọi tên thông thường vẫn sửa thành "anh Soutetsu" như khóa B4.

## 7. Ghi chú toàn vẹn dữ liệu (không phải lỗi VN, không tính vào 34)

**Thẻ %l phía JP bị tách ở key 2547.** Trong JP, thẻ gloss của 杜氏 mở ở dòng trên (`\x%l杜氏;#00ffc040;杜氏%l;`) rồi bị ngắt bởi ký tự xuống dòng, dấu đóng `#;` nằm ở dòng dưới — thẻ JP mở 1, đóng 0 nếu đếm theo dòng. Phía VN đóng thẻ đúng trước khi xuống dòng và gloss "trưởng hầm rượu" là đúng (杜氏 = bậc thầy ủ rượu; TW: 掌窖). Đây là dị thường ở nguồn JP, không phải lỗi dịch — ghi lại để khi rebuild TOML không ai "sửa" nhầm phía VN theo JP.

## 8. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix so với JP)

**Tổng: 34 / đã kiểm tra lại: 34 / đã loại bỏ: 0 / đã sửa lại: 5.**

Lượt soát 2 bắt được 5 lỗi trong fix lần 1 (đều là lỗi gõ tay/thao tác, không phải lỗi phán đoán dịch):

1. **1423** — fix lần 1 gõ tay làm rơi cặp 「」 mà bản cũ có. Đã khôi phục: `「——Khủng thật。」`
2. **1445** — tương tự, rơi 「」. Đã khôi phục: `「……Chắc là chuyện tiếp theo của ngày hôm qua nhỉ。」`
3. **1431** — fix lần 1 dùng chuỗi thay thế sai: thẻ %l chen giữa "Railord" và "và đầu máy cũ" nên lệnh thay thế không khớp — fix thực chất chưa sửa gì (chỉ gộp dòng). Đã sửa lại bằng chuỗi đúng: `「'Trọn bộ Railord cũ và đầu máy'—— …」`
4. **1684** — "anh Soutetsu" đứng đầu câu sau dấu chấm phải viết hoa. Đã sửa: `「Cứ giao cho tôi. Anh Soutetsu.」`
5. **2133** — cả dòng chỉ là một tiếng gọi độc lập, đầu câu phải viết hoa. Đã sửa: `「Anh Soutetsu!」`

Sau 5 lần sửa trên, toàn bộ 34 fix đã được đọc lại lần 2 so với JP và xác nhận đúng.

## 9. Khối TOML (đã kiểm chứng)

Khối dưới đây parse được bằng tomllib, **34 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"1417" = "「\\x%l8620;#00ffc040;8620%l;#; nặng lắm đó nha~. KiHa 07S của Reina tổng chiều dài 19.7m mà tổng trọng lượng cũng chỉ có 27.2 tấn thôi đó~」"
"1423" = "「——Khủng thật。」"
"1431" = "「'Trọn bộ \\x%lレイルロオド;#00ffc040;Railord%l;#; cũ và đầu máy'—— Oa, cái này, là nói về nhóm chị Hachiroku đó nha~」"
"1445" = "「……Chắc là chuyện tiếp theo của ngày hôm qua nhỉ。」"
"1665" = "「Nếu tôi không có lỗi, thì Paulette lại càng không. Quan trọng hơn là dọn dẹp hậu quả đã. Em có bị thương không?」"
"1674" = "「Không, đâu có! Sao lại là lỗi của anh Soutetsu được.」"
"1684" = "「Cứ giao cho tôi. Anh Soutetsu.」"
"1700" = "「Em không nhớ được sao? Khoảng thời gian nào, em được ông Taito đưa đến Ohitoyo này.」"
"1704" = "「Em biết nhà kho đó ở đâu sao?」"
"1711" = "「Một thứ to lớn và nặng nề như vậy, thì không thể dễ dàng cất giấu hay di chuyển được, ý em là vậy sao.」"
"1723" = "「Tổng chiều dài là 16.7m, tổng chiều cao là 3.8m. Chỉ tính riêng đầu máy thôi, \\x%l運転整備重量;#00ffc040;khối lượng vận hành%l;#; đã lên tới 39.8 tấn rồi.」"
"1753" = "「Em biết——đúng không. Chuyện của nhà Migita ấy.」"
"1777" = "「À, vâng. Tôi ra ngay đây.」"
"1799" = "「Chà. Đúng là tái ông thất mã nhỉ, ngài Soutetsu.」"
"1801" = "「Hừm. Vậy thì khi nào cần anh sẽ dùng.」"
"1830" = "「Canh Dago ngon thật đấy. Cảm giác đúng kiểu 'A, Ohitoyo đây rồi'.」"
"1845" = "「Hiểu rồi. Em xuống trước đi đã.」"
"1863" = "「Nếu nói là lỗi của ai, thì chắc là của tôi rồi. Người làm em hoảng hốt và buông tay khỏi cái thang đều là tôi mà.」"
"1886" = "「Chuẩn bị tinh thần!」"
"1895" = "「À ừm, lúc nhận bàn giao cơ sở vật chất từ \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ…… họ có dặn là những thứ đang cho cá nhân thuê thì đừng có động vào.」"
"1926" = "「Tôi hiểu mà. Em đã cố gạt nó ra khỏi tâm trí đúng không? Vì nếu cứ bận tâm, em sẽ chẳng làm nên trò trống gì cả.」"
"1930" = "「Lúc nãy thấy em xem chăm chú lắm mà——」"
"1949" = "「Nghĩa là em vẫn luôn tuân thủ lời dặn lúc bàn giao sao.」"
"1964" = "「Vậy sao. Thế thì giao cho em đấy.」"
"1970" = "「Vâng——anh Soutetsu, anh xem cái này đi. Gáy sách này……anh thấy không, có ghi 'Hồ sơ kế toán'.」"
"1972" = "「Đúng vậy ạ. Cảm giác đúng như anh Soutetsu nói, thế nên.」"
"2012" = "「Paulette, em không sao chứ, có bị thương ở đâu không?」"
"2048" = "「Em thực sự không sao chứ? Có đau ở đâu không? Mặt em đỏ bừng, hơi thở cũng gấp gáp lắm đấy?」"
"2133" = "「Anh Soutetsu!」"
"2144" = "「Ư!」"
"2436" = "Tôi mím môi, bắt tay vào tìm kiếm. Nhìn căn phòng bừa bộn thế này, chắc hẳn ông Taito là người có tính cách cẩu thả."
"2525" = "Dưới ánh mắt chăm chú theo dõi của Reina trong thân bảo trì, Paulette đang nghiêm túc giải thích điều gì đó."
"2543" = "Với tư cách là giám đốc Đường sắt Ohitoyo, với tư cách là thị trưởng Ohitoyo—— Có lẽ cô ấy muốn tìm thấy \\x%l8620;#00ffc040;8620%l;#; và nhìn thấy tương lai ở đó."
"2636" = "Dù sinh ra ở Đế đô, nhưng tôi cũng lớn lên ở Ohitoyo một thời gian. Nên khi được hỏi, tôi liền nhớ ra ngay."
```

## Kết bài

File 07 là một file sạch theo chuẩn của dự án: **34/331 dòng sai (10,3%)**, không có dòng lệch, không có chuỗi xoay, không có nhiễm chéo — mọi lỗi đều sửa được tại chỗ. Lỗi lớn nhất là nhóm đại từ (19/34): Soutetsu gọi Paulette bằng "cô" tới 12 lần, tự xưng "em" 2 lần, và Paulette gọi "Soutetsu-kun" 5 lần — cả ba đều đã được quyết định thống nhất từ trước (khóa #13, tiền lệ file 02, khóa B4), chỉ việc áp dụng. Thuật ngữ Ohitoyo đã sửa nốt 5 lần xuất hiện trong file này; còn lại 109 lần ở các file 00_Common khác, chờ lượt thống nhất (unification pass). Hai điểm cần Hieu biết: (1) hai dòng 1910/2342 được giữ nguyên có chủ đích vì chính sự phân biệt san/kun là nội dung của câu — nếu Hieu muốn đổi, nói lại; (2) thẻ gloss JP ở 2547 bị tách bởi ký tự xuống dòng là dị thường ở nguồn, phía VN không có lỗi. Lượt soát 2 đã đọc lại toàn bộ 34 fix so với JP: 34/34 xác nhận đúng, 0 loại bỏ, 5 sửa lại (chủ yếu là lỗi gõ tay: rơi 「」, chuỗi thay thế không khớp, viết hoa đầu câu). File tiếp theo trong hàng đợi 00_Common: file 06, 08, 09, 10, 11, 12, 13, 14, 15, 末尾.
