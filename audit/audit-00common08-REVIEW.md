# Audit 00_Common file 08 — 共通08_傷跡.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通08_傷跡.txt.toml` — md5 `6d338fc2caafd1b4abd75c58e1aa4dcd`, BOM, CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 360 hàng `[script]`.
**Kết quả: 38/360 dòng sai (10,6%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Đại từ xưng hô (pronoun) | 18 |
| Thuật ngữ (terminology) | 13 |
| Thẻ gloss %l (tag) | 3 |
| Tiếng thở/gasp (gasp) | 4 |
| **Tổng** | **38** |

**Theo loại dòng:** thoại 27/180 sai (15,0%), độc thoại 11/180 sai (6,1%).
**Theo nhân vật:** 双鉄 (Soutetsu) 18, ハチロク (Hachiroku) 5, れいな (Reina) 3, ポーレット (Paulette) 1, độc thoại 11.

Nhóm đại từ (18) chia nhỏ: Soutetsu tự xưng "anh"→"tôi" 13 dòng (1688, 1725, 1782, 1858, 1876, 1897, 1901, 1921, 1923, 1937, 1958, 1999, 2076); Soutetsu gọi Paulette "cô"→"em" 1 (1974); Soutetsu gọi Reina "cô"→"em" 1 (1855); Soutetsu độc thoại tự xưng "em"→"tôi" 2 (71, 76); B4 — Paulette gọi "Soutetsu-kun"→"anh Soutetsu" 1 (2084).

Nhóm thuật ngữ (17 dòng chạm đến thuật ngữ, kể cả 3 dòng tag): 整備体→"thân bảo trì" 6 (76, 77, 1747, 1810, 1982, 2453); 運転体→"thân vận hành" 5 (1456, 1486, 2517, 2529, 2692); タブレット→"máy tính bảng" 4 (1480, 1929, 1991, 2836); 御一夜→Ohitoyo 2 (1881, 2547). Dòng 76 tính cả hai nhóm (vừa xưng hô vừa thuật ngữ) nên tổng số dòng sai là 40, không phải 41.

File này không có lỗi lệch dòng — toàn bộ 38 lỗi đều là lỗi tại chỗ (sai đại từ, sai thuật ngữ, mất gasp), sửa được ngay không cần dịch lại. Lỗi tập trung ở đại từ Soutetsu: anh ta xưng "anh" với Hachiroku trong 13/18 dòng thoại có đại từ tự xưng — thói quen của người dịch cũ, ngược với quy ước đã chốt ("anh" với Hibiki/Michiko/Paulette/Reina; "tôi" với Hachiroku/Mayami/Nagi/Minokasa).

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục (thư mục CSV và TOML-2 không khớp nhau ở nhiều file khác — file này chỉ có một bộ hàng nên không bị ảnh hưởng).
- **CSV vs TOML:** VN khớp tuyệt đối 162 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 360/360. Không có khác biệt nào — bộ dữ liệu sạch, JP comment khớp CSV3.
- **Sweep っ (gasp):** sweep có đúng 3 mục cho file này (1996, 2098, 2099) — đã xác nhận và lấy nguyên văn. Thêm 1 sweep-missed (1490, xem §5).
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có hàng VN trùng lặp trong file. 2 hàng VN==TW: 1494 `「…………」` chỉ là dấu lửng (không phải lỗi); 1490 `「——」` là gasp bị mất ở cả hai bản (đã sửa, xem §5).

## 3. Các lỗi đã sửa (38 dòng)

### 71 — Đại từ xưng hô

**JP:** \x%lレイルロオド;#00ffc040;レイルロオド%l;#;の傷も自然に「治る」のか、\nハチロクにも傷跡があるのに気付いちゃう。

**TW:** \x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的傷也會自然“癒合”嗎？我注意到八六身上也有傷痕。

**VN cũ:** Vết thương của \x%lレイルロオド;#00ffc040;Railord%l;#; cũng tự nhiên "lành" lại sao,\nem nhận ra trên người Hachiroku cũng có vết sẹo.

**Fix:** Vết thương của \x%lレイルロオド;#00ffc040;Railord%l;#; cũng tự nhiên "lành" lại sao,\ntôi nhận ra trên người Hachiroku cũng có vết sẹo.

Độc thoại Soutetsu: tự xưng "em" → "tôi". Đây là quan sát thường (nhận ra vết sẹo), không phải tự vấn cảm xúc nội tâm nên không thuộc ngoại lệ "mình"; và "em" càng không phải cách Soutetsu tự xưng.
### 76 — Đại từ xưng hô

**JP:** \x%l整備体;#00ffc040;整備体%l;#;……私より少し小さいハチロクは、\nぱっと見だったら、人間の女の子そのものだ。

**TW:** \x%l整備体;#00ffc040;整備體%l;#;……比我稍顯嬌小的八六，乍看之下和人類女孩一模一樣。

**VN cũ:** \x%l整備体;#00ffc040;Thân chính%l;#;……Hachiroku, người nhỏ bé hơn em một chút,\nnhìn thoáng qua thì giống hệt một bé gái con người.

**Fix:** \x%l整備体;#00ffc040;thân bảo trì%l;#;……Hachiroku, người nhỏ bé hơn tôi một chút,\nnhìn thoáng qua thì giống hệt một bé gái con người.

Hai lỗi một dòng: (a) gloss 整備体 "Thân chính" → "thân bảo trì" theo quyết định #11 (19/11); (b) độc thoại Soutetsu: 私より = "hơn tôi", tự xưng "em" → "tôi".
### 77 — Thuật ngữ

**JP:** \x%l整備体;#00ffc040;整備体%l;#;のハチロクは、\n運転席とおぼしき場所に置いてある、黒い鞄を僕に示す。

**TW:** \x%l整備体;#00ffc040;整備體%l;#;的八六指著放在似乎是駕駛座上的黑色皮包。

**VN cũ:** Hachiroku trong \x%l整備体;#00ffc040;thân chính%l;#;,\nchỉ cho tôi xem một chiếc cặp màu đen đặt ở nơi có vẻ như là ghế lái.

**Fix:** Hachiroku trong \x%l整備体;#00ffc040;thân bảo trì%l;#;,\nchỉ cho tôi xem một chiếc cặp màu đen đặt ở nơi có vẻ như là ghế lái.

Gloss 整備体 "thân chính" → "thân bảo trì" theo quyết định #11.
### 1456 — Thuật ngữ

**JP:** ――音がする。それと同時に\x%l運転体;#00ffc040;運転体%l;#;のハチロクが、\nぜんまい切れを起こしたように崩れてしまう。

**TW:** ——聲音傳來，與此同時\x%l運転体;#00ffc040;駕駛體%l;#;的八六好像是發條鬆了一樣倒在了地上。

**VN cũ:** ——Một âm thanh vang lên. Cùng lúc đó, \x%l運転体;#00ffc040;kíp lái%l;#; của Hachiroku\nđổ gục xuống như một món đồ chơi bị đứt cót.

**Fix:** ――Một âm thanh vang lên. Cùng lúc đó, \x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku\nđổ gục xuống như một món đồ chơi bị đứt cót.

運転体 là thân thể vận hành (TW: 駕駛體), không phải một kíp người ("kíp lái"). Theo cặp gloss đã chốt (運転ボディ = "thân vận hành").
### 1480 — Thuật ngữ

**JP:** 「\x%lタブレット;#00ffc040;タブレット%l;#;は……お前の、魂なのか？」

**TW:** 「\x%lタブレット;#00ffc040;操作板%l;#;……那是你的靈魂嗎？」

**VN cũ:** 「\x%lタブレット;#00ffc040;Thẻ bảng%l;#;……là linh hồn của em sao?」

**Fix:** 「\x%lタブレット;#00ffc040;máy tính bảng%l;#;……là linh hồn của em sao?」

タブレット = "máy tính bảng" theo thuật ngữ đã chốt (操作板/タブレット); "Thẻ bảng" sai nghĩa — lỗi giống file 07 key 2525.
### 1486 — Thẻ gloss %l

**JP:** 「\x%l乗務鞄;#00ffc040;乗務鞄%l;#;の中には、運転[ボディ]体が収まるようになっています」

**TW:** 「\x%l乗務鞄;#00ffc040;乘務包%l;#;裡面，剛好可以放下駕駛體」

**VN cũ:** 「Bên trong \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; được thiết kế để vừa vặn chứa \x%l運転体;#00ffc040;kíp lái%l;#; ạ.」

**Fix:** 「Bên trong \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; được thiết kế để vừa vặn chứa thân vận hành ạ.」

Hai lỗi: (a) VN tự thêm thẻ %l cho 運転体 — JP chỉ có [ボディ] dạng ruby trong ngoặc, không có thẻ %l — gỡ theo tiền lệ reina02; (b) gloss 運転体 "kíp lái" → "thân vận hành" (xem 1456). Gloss 乗務鞄 "túi phi hành đoàn" giữ nguyên, ghi vào mục thống nhất (§10).
### 1490 — Tiếng thở/gasp

**JP:** 「っ――」

**TW:** 「——」

**VN cũ:** 「——」

**Fix:** 「Ư――」

JP là gasp nguyên dòng っ + gạch ngang; VN chỉ giữ gạch ngang, mất hẳn tiếng gasp. Sweep-missed (sweep chỉ có 1996/2098/2099 ở file này) — theo quy tắc gasp nguyên dòng → Ư.
### 1688 — Đại từ xưng hô

**JP:** 「いや？　予想よりもずっと早かった」

**TW:** 「不。比我預想的要快得多了」

**VN cũ:** 「Không đâu? Nhanh hơn anh tưởng nhiều.」

**Fix:** 「Không đâu? Nhanh hơn tôi tưởng nhiều.」

Soutetsu nói với Hachiroku — cả đoạn 1688–1725 chỉ có Soutetsu + Hachiroku, Hibiki mãi 1728 mới lên tiếng — nên tự xưng "anh" sai ("anh" với Hibiki/Michiko/Paulette/Reina; "tôi" với Hachiroku/Mayami/Nagi/Minokasa) → "tôi".
### 1725 — Đại từ xưng hô

**JP:** 「予想よりもずっと早く、はるかに見事な歩みだった」

**TW:** 「你的步伐比我預想的還要邁得更快，更漂亮」

**VN cũ:** 「Nhanh hơn anh tưởng nhiều, và là một bước đi vô cùng tuyệt vời.」

**Fix:** 「Nhanh hơn tôi tưởng nhiều, và là một bước đi vô cùng tuyệt vời.」

Soutetsu khen bước đi của Hachiroku, nói với Hachiroku → tự xưng "anh" sai → "tôi" (xem 1688).
### 1747 — Thẻ gloss %l

**JP:** 「ハチロクさん、整備[ボディ]体ですねぇ。\nすてきですぅ、とっても、とってもきれいですぅ」

**TW:** 「八六小姐，這是整備體吧。太漂亮了，真是美極了」

**VN cũ:** 「Chị Hachiroku, là \x%l整備体;#00ffc040;thân chính%l;#; nhỉ~.\nTuyệt quá đi ạ~, cực kỳ, cực kỳ đẹp luôn đó ạ~」

**Fix:** 「Chị Hachiroku, là thân bảo trì nhỉ~.\nTuyệt quá đi ạ~, cực kỳ, cực kỳ đẹp luôn đó ạ~」

Hai lỗi: (a) VN tự thêm thẻ %l cho 整備体 — JP chỉ có [ボディ] dạng ruby, không có thẻ %l — gỡ theo tiền lệ reina02; (b) gloss "thân chính" → "thân bảo trì" theo quyết định #11.
### 1782 — Đại từ xưng hô

**JP:** 「破損箇所のマークにだったら十分すぎるだろう。\n始めたい。ハチロク。どうか指導を頼む」

**TW:** 「只是標出破損處的話已經足夠了吧。八六，我想先做起來，請你指導我吧」

**VN cũ:** 「Để đánh dấu những chỗ hư hỏng thì thế này là quá đủ rồi.\nAnh muốn bắt đầu. Hachiroku. Nhờ em chỉ dẫn cho anh nhé.」

**Fix:** 「Để đánh dấu những chỗ hư hỏng thì thế này là quá đủ rồi.\nTôi muốn bắt đầu. Hachiroku. Nhờ em chỉ dẫn cho tôi nhé.」

Soutetsu nói với Hachiroku (gọi tên cô ấy trong câu) → tự xưng "anh" ×2 sai → "tôi" ×2. "Nhờ em" (gọi Hachiroku) giữ nguyên, đúng.
### 1810 — Thẻ gloss %l

**JP:** 「ああ……よかった。\nわたくしです――わたくしの整備[ボディ]体です」

**TW:** 「啊……太好了。那就是我——我的整備體」

**VN cũ:** 「A……may quá.\nLà em——là \x%l整備体;#00ffc040;thân chính%l;#; của em ạ.」

**Fix:** 「A……may quá.\nLà em——là thân bảo trì của em ạ.」

Hai lỗi: (a) VN tự thêm thẻ %l cho 整備体 — JP chỉ có [ボディ] dạng ruby — gỡ theo tiền lệ reina02; (b) gloss "thân chính" → "thân bảo trì".
### 1855 — Đại từ xưng hô

**JP:** 「ありがたい。\nその時には、遠慮をしている余裕など無くなろうからな」

**TW:** 「太感謝了。因為到時候，恐怕也沒辦法跟你客氣了啊」

**VN cũ:** 「Cảm ơn cô.\nĐến lúc đó thì chắc tôi cũng chẳng còn tâm trí đâu mà khách sáo nữa.」

**Fix:** 「Cảm ơn em.\nĐến lúc đó thì chắc tôi cũng chẳng còn tâm trí đâu mà khách sáo nữa.」

Soutetsu cảm ơn Reina — cô ấy vừa nói sẽ ở lại cùng anh cho đỡ chán (1846–1847) — nên "Cảm ơn cô" sai → "Cảm ơn em".
### 1858 — Đại từ xưng hô

**JP:** 「さてと、ハチロク。指示してくれ。\n２３：００には終わらせたい」

**TW:** 「好了，八六，給我指示吧。我想在２３：００前做完工作」

**VN cũ:** 「Được rồi, Hachiroku. Ra chỉ thị cho anh đi.\nAnh muốn hoàn thành trước 23:00.」

**Fix:** 「Được rồi, Hachiroku. Ra chỉ thị cho tôi đi.\nTôi muốn hoàn thành trước 23:00.」

Soutetsu nói với Hachiroku (gọi tên trong câu) → tự xưng "anh" ×2 sai → "tôi" ×2.
### 1876 — Đại từ xưng hô

**JP:** 「諦めるなら、反対はせん。\n僕はお前の望みに従い――\x%l8620;#00ffc040;8620%l;#;を殺してしまおう」

**TW:** 「如果你想放棄，我也不反對。我會如你所願——殺死\x%l8620;#00ffc040;８６２０%l;#;」

**VN cũ:** 「Nếu em bỏ cuộc, anh sẽ không phản đối.\nAnh sẽ làm theo ý em——giết chết \x%l8620;#00ffc040;8620%l;#;.」

**Fix:** 「Nếu em bỏ cuộc, tôi sẽ không phản đối.\nTôi sẽ làm theo ý em——giết chết \x%l8620;#00ffc040;8620%l;#;.」

Soutetsu nói với Hachiroku → tự xưng "anh" ×2 sai → "tôi" ×2. "Nếu em bỏ cuộc" / "làm theo ý em" (gọi Hachiroku) giữ nguyên.
### 1881 — Thuật ngữ

**JP:** 「これを……御一夜まで引っ張ってきたのか」

**TW:** 「它……就這麼被一路拖回了御一夜嗎」

**VN cũ:** 「Thứ này……đã bị kéo lê đến tận Ohimitera sao.」

**Fix:** 「Thứ này……đã bị kéo lê đến tận Ohitoyo sao.」

御一夜 = "Ohitoyo" theo quyết định đã chốt; "Ohimitera" là dạng cũ cần thống nhất.
### 1897 — Đại từ xưng hô

**JP:** 「僕とお前だ。\n集中すれば、こなせよう」

**TW:** 「憑你我，集中精力肯定能完成」

**VN cũ:** 「Có anh và em mà.\nChỉ cần tập trung thì sẽ làm được thôi.」

**Fix:** 「Có tôi và em mà.\nChỉ cần tập trung thì sẽ làm được thôi.」

Soutetsu nói với Hachiroku (僕とお前だ) → tự xưng "anh" sai → "tôi".
### 1901 — Đại từ xưng hô

**JP:** 「手は貸さん。\nハチロク、お前は、お前の足だけで立ち上がれ」

**TW:** 「我不會幫你的。八六，你要靠你自己的雙腳站起來」

**VN cũ:** 「Anh sẽ không giúp đâu.\nHachiroku, em phải tự đứng lên bằng chính đôi chân của mình.」

**Fix:** 「Tôi sẽ không giúp đâu.\nHachiroku, em phải tự đứng lên bằng chính đôi chân của mình.」

Soutetsu nói với Hachiroku → tự xưng "Anh" sai → "Tôi". "Đôi chân của mình" giữ nguyên — "mình" ở đây là chân của Hachiroku (phản thân ngôi hai, JP: お前の足), không phải Soutetsu tự xưng.
### 1921 — Đại từ xưng hô

**JP:** 「わかった。そのときにハチロクのやり方を見て学ぼう」

**TW:** 「我知道了。到時候看看八六你是怎麼做的吧」

**VN cũ:** 「Anh hiểu rồi. Lúc đó anh sẽ quan sát cách làm của em rồi học theo.」

**Fix:** 「Tôi hiểu rồi. Lúc đó tôi sẽ quan sát cách làm của em rồi học theo.」

Soutetsu nói với Hachiroku → tự xưng "anh" ×2 sai → "tôi" ×2.
### 1923 — Đại từ xưng hô

**JP:** 「わかった。責任をもって預かろう」

**TW:** 「我知道了。我會負起責任收好它的」

**VN cũ:** 「Anh hiểu rồi. Anh sẽ giữ nó cẩn thận.」

**Fix:** 「Tôi hiểu rồi. Tôi sẽ giữ nó cẩn thận.」

Soutetsu nói với Hachiroku (nhận giữ 乗務鞄) → tự xưng "anh" ×2 sai → "tôi" ×2.
### 1929 — Thuật ngữ

**JP:** 「\x%lタブレット;#00ffc040;タブレット%l;#;を交換します。\n驚かないでくださいましね？」

**TW:** 「我要交換\x%lタブレット;#00ffc040;操作板%l;#;了。您可不要吃驚哦？」

**VN cũ:** 「Em sẽ đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#;.\nNgài đừng ngạc nhiên nhé?」

**Fix:** 「Em sẽ đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#;.\nNgài đừng ngạc nhiên nhé?」

タブレット = "máy tính bảng" theo thuật ngữ đã chốt; "thẻ bảng" sai nghĩa.
### 1937 — Đại từ xưng hô

**JP:** 「ここから先は僕も一緒だ。\nハチロク、まずは何から始める？」

**TW:** 「接下來的路，有我陪你走。八六，首先該做什麼？」

**VN cũ:** 「Từ đây trở đi sẽ có anh đồng hành.\nHachiroku, trước tiên chúng ta bắt đầu từ đâu?」

**Fix:** 「Từ đây trở đi sẽ có tôi đồng hành.\nHachiroku, trước tiên chúng ta bắt đầu từ đâu?」

Soutetsu nói với Hachiroku (gọi tên trong câu) → tự xưng "anh" sai → "tôi".
### 1958 — Đại từ xưng hô

**JP:** 「そうか？　綺麗な図面に見えるが」

**TW:** 「是嗎？圖紙看起來挺漂亮的啊」

**VN cũ:** 「Vậy sao? Anh thấy bản vẽ đẹp mà.」

**Fix:** 「Vậy sao? Tôi thấy bản vẽ đẹp mà.」

Soutetsu nhận xét bản vẽ của Hachiroku, nói với cô ấy → tự xưng "anh" sai → "tôi".
### 1974 — Đại từ xưng hô

**JP:** 「ポーレット、よければ――そしてもしも有ればだが、\n\x%l8620;#00ffc040;8620%l;#;の状態の方を見ておいてもらえるか」

**TW:** 「波萊特，如果可以的話——前提是\x%l8620;#00ffc040;８６２０%l;#;在這裡的話——你能去幫我確認一下它的狀況嗎」

**VN cũ:** 「Paulette, nếu cô muốn——và giả sử nó có ở đó thật,\nthì cô có thể vào xem tình trạng của \x%l8620;#00ffc040;8620%l;#; trước giúp tôi được không?」

**Fix:** 「Paulette, nếu em muốn——và giả sử nó có ở đó thật,\nthì em có thể vào xem tình trạng của \x%l8620;#00ffc040;8620%l;#; trước giúp tôi được không?」

Soutetsu gọi Paulette "cô" ×2 → "em" theo quyết định thống nhất (Soutetsu→Paulette = "em").

### 1982 — Thuật ngữ

**JP:** 「れいなも、\x%l整備体;#00ffc040;整備体%l;#;で来てよかったですぅ。\nがんばってハチロクさんのお手伝いをしちゃいますねぇ」

**TW:** 「玲奈幸好也是用\x%l整備体;#00ffc040;整備體%l;#;過來的。這樣就能幫八六小姐好多忙了」

**VN cũ:** 「May mà Reina cũng đến bằng \x%l整備体;#00ffc040;thân chính%l;#; nha~.\nReina sẽ cố gắng hết sức giúp đỡ chị Hachiroku đó nha~」

**Fix:** 「May mà Reina cũng đến bằng \x%l整備体;#00ffc040;thân bảo trì%l;#; nha~.\nReina sẽ cố gắng hết sức giúp đỡ chị Hachiroku đó nha~」

Gloss 整備体 "thân chính" → "thân bảo trì" theo quyết định #11.
### 1991 — Thuật ngữ

**JP:** 「人間の体に例えるのなら、\n\x%lタブレット;#00ffc040;タブレット%l;#;は、脳に近いかとわたくしは」

**TW:** 「用人類的身體來比喻的話，我覺得\x%lタブレット;#00ffc040;操作板%l;#;應該更接近於大腦吧」

**VN cũ:** 「Nếu so sánh với cơ thể con người,\nthì em nghĩ \x%lタブレット;#00ffc040;thẻ bảng%l;#; giống với bộ não hơn ạ.」

**Fix:** 「Nếu so sánh với cơ thể con người,\nthì em nghĩ \x%lタブレット;#00ffc040;máy tính bảng%l;#; giống với bộ não hơn ạ.」

タブレット = "máy tính bảng" theo thuật ngữ đã chốt; "thẻ bảng" sai nghĩa.
### 1996 — Tiếng thở/gasp

**JP:** 「そら、ハチロク。入ったぞ――っ！？」

**TW:** 「看啊，八六，我們到了——！？」

**VN cũ:** 「Đó, Hachiroku. Vào rồi đấy——!?」

**Fix:** 「Đó, Hachiroku. Vào rồi đấy——Ư!?」

Sweep lost-gasp-trailing: JP kết bằng ――っ！？, VN giữ gạch ngang nhưng mất gasp — chèn Ư sau gạch ngang. Lấy nguyên văn từ sweep.
### 1999 — Đại từ xưng hô

**JP:** 「すまなかったな。だが、助かった」

**TW:** 「真對不起。不過你真的幫了大忙」

**VN cũ:** 「Xin lỗi em nhé. Nhưng nhờ có em mà anh đỡ vất vả hơn nhiều.」

**Fix:** 「Xin lỗi em nhé. Nhưng nhờ có em mà tôi đỡ vất vả hơn nhiều.」

Soutetsu nói với Hachiroku → tự xưng "anh" sai → "tôi".

### 2076 — Đại từ xưng hô

**JP:** 「ならばハチロク。僕は、今一度だけ問おう。\nお前は、\x%l8620;#00ffc040;8620%l;#;を助けるものか？　見捨てるものか？」

**TW:** 「那麼八六，我現在就只問你一次。你是來拯救\x%l8620;#00ffc040;８６２０%l;#;的，還是來拋棄它的？」

**VN cũ:** 「Vậy thì Hachiroku. Anh sẽ hỏi em một lần cuối.\nEm sẽ cứu \x%l8620;#00ffc040;8620%l;#; chứ? Hay là bỏ mặc nó?」

**Fix:** 「Vậy thì Hachiroku. Tôi sẽ hỏi em một lần cuối.\nEm sẽ cứu \x%l8620;#00ffc040;8620%l;#; chứ? Hay là bỏ mặc nó?」

Soutetsu nói với Hachiroku (gọi tên trong câu) → tự xưng "anh" sai → "tôi".
### 2084 — Đại từ xưng hô

**JP:** 「そ、双鉄くんっ！？」

**TW:** 「雙、雙鐵君！？」

**VN cũ:** 「S-Soutetsu-kun!?」

**Fix:** 「A-Anh Soutetsu!?」

B4: JP là 双鉄くん, Paulette gọi Soutetsu. Bản cũ giữ romaji "Soutetsu-kun" — theo khóa B4 thì dạng gọi này luôn là "anh Soutetsu" (không có ngoại lệ rên; đây cũng không phải cảnh đánh vần tên như file 04 key 2214). Giữ lại nét lắp bắp bằng "A-Anh".
### 2098 — Tiếng thở/gasp

**JP:** 「っ！」

**TW:** 「！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

Sweep lost-gasp-whole: JP nguyên dòng 「っ！」, VN chỉ còn dấu chấm than — chèn Ư. Lấy nguyên văn từ sweep.
### 2099 — Tiếng thở/gasp

**JP:** 「っ！！」

**TW:** 「！！」

**VN cũ:** 「!!」

**Fix:** 「Ư!!」

Sweep lost-gasp-whole: JP nguyên dòng 「っ！！」, VN chỉ còn dấu chấm than — chèn Ư. Lấy nguyên văn từ sweep.
### 2453 — Thuật ngữ

**JP:** 倒れている\x%l整備体;#00ffc040;整備体%l;#;の服の胸元を開け、\nそこから何か、ネックレスのようなものを引き出して――

**TW:** 她拉開\x%l整備体;#00ffc040;整備體%l;#;胸口的衣服，從中取出一條像是項鍊一樣的東西——

**VN cũ:** Em ấy mở phần ngực áo của \x%l整備体;#00ffc040;thân chính%l;#; đang nằm gục ra,\nrút từ đó ra một thứ gì đó giống như một chiếc vòng cổ——

**Fix:** Em ấy mở phần ngực áo của \x%l整備体;#00ffc040;thân bảo trì%l;#; đang nằm gục ra,\nrút từ đó ra một thứ gì đó giống như một chiếc vòng cổ——

Gloss 整備体 "thân chính" → "thân bảo trì" theo quyết định #11.
### 2517 — Thuật ngữ

**JP:** 鞄を開けば、ハチロクが僕に\x%l運転体;#00ffc040;運転体%l;#;をそっと手渡す。\n鞄の中へ――ああ、これは見事にきっちり収まるものだ。

**TW:** 我打開皮包，八六輕輕將她的\x%l運転体;#00ffc040;駕駛體%l;#;遞給我。我把它放進皮包中——啊，真的是剛剛好的大小。

**VN cũ:** Khi tôi mở cặp ra, Hachiroku nhẹ nhàng trao \x%l運転体;#00ffc040;kíp lái%l;#; cho tôi.\nCho vào trong cặp——à, quả thực là vừa khít luôn.

**Fix:** Khi tôi mở cặp ra, Hachiroku nhẹ nhàng trao \x%l運転体;#00ffc040;thân vận hành%l;#; cho tôi.\nCho vào trong cặp——à, quả thực là vừa khít luôn.

運転体 "kíp lái" → "thân vận hành" (xem 1456).
### 2529 — Thuật ngữ

**JP:** ハチロクの求めるままに\x%l運転体;#00ffc040;運転体%l;#;を床へと下ろせば、\n小さな体は倒れる体に、静かに静かに歩み寄る。

**TW:** 我按照八六的要求把她的\x%l運転体;#00ffc040;駕駛體%l;#;放到地板上。她小小的身體默默地朝倒在地上的那副身體走去。

**VN cũ:** Làm theo yêu cầu của Hachiroku, tôi đặt \x%l運転体;#00ffc040;kíp lái%l;#; xuống sàn nhà,\ncơ thể nhỏ bé đó lặng lẽ, lặng lẽ tiến lại gần cơ thể đang nằm gục kia.

**Fix:** Làm theo yêu cầu của Hachiroku, tôi đặt \x%l運転体;#00ffc040;thân vận hành%l;#; xuống sàn nhà,\ncơ thể nhỏ bé đó lặng lẽ, lặng lẽ tiến lại gần cơ thể đang nằm gục kia.

運転体 "kíp lái" → "thân vận hành" (xem 1456).
### 2547 — Thuật ngữ

**JP:** ポーレットとれいなに案内されて、\n御一夜駅のホームを通り、敷地の更に奥へと進む。

**TW:** 我被波萊特和玲奈帶著穿過御一夜車站的站台，往更深處走去。

**VN cũ:** Được Paulette và Reina dẫn đường,\nchúng tôi đi qua sân ga Ohimitera, tiến sâu hơn vào bên trong khuôn viên.

**Fix:** Được Paulette và Reina dẫn đường,\nchúng tôi đi qua sân ga Ohitoyo, tiến sâu hơn vào bên trong khuôn viên.

御一夜 = "Ohitoyo"; "Ohimitera" là dạng cũ. Đây là lần Ohimitera cuối cùng trong file này — sau file này (cộng cả file 09 đã sửa 15 lần), 00_Common còn 88 lần (xem §9).
### 2692 — Thuật ngữ

**JP:** \x%l乗務鞄;#00ffc040;乗務鞄%l;#;のずっしりとした重さに比べ、\nあまりに軽かった\x%l運転体;#00ffc040;運転体%l;#;。

**TW:** 與\x%l乗務鞄;#00ffc040;乘務包%l;#;的沉重比起來，\x%l運転体;#00ffc040;駕駛體%l;#;實在是顯得太輕了。

**VN cũ:** So với độ nặng trịch của \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;,\nthì \x%l運転体;#00ffc040;kíp lái%l;#; lại quá đỗi nhẹ nhàng.

**Fix:** So với độ nặng trịch của \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;,\nthì \x%l運転体;#00ffc040;thân vận hành%l;#; lại quá đỗi nhẹ nhàng.

運転体 "kíp lái" → "thân vận hành" (xem 1456). Gloss 乗務鞄 "túi phi hành đoàn" giữ nguyên — ghi vào mục thống nhất (§10).
### 2836 — Thuật ngữ

**JP:** （あれが\x%lタブレット;#00ffc040;タブレット%l;#;とやらか？\n交換、とハチロクは言っていたが……）

**TW:** （那就是\x%lタブレット;#00ffc040;操作板%l;#;嗎？八六說要交換這個……）

**VN cũ:** （Đó là cái gọi là \x%lタブレット;#00ffc040;thẻ bảng%l;#; sao?\nHachiroku có nói là đổi, nhưng mà……）

**Fix:** （Đó là cái gọi là \x%lタブレット;#00ffc040;máy tính bảng%l;#; sao?\nHachiroku có nói là đổi, nhưng mà……）

タブレット = "máy tính bảng" theo thuật ngữ đã chốt; "thẻ bảng" sai nghĩa.

## 4. Lệch dòng / chuỗi xoay / nhiễm chéo: 0

- **0 dòng lệch dòng (misaligned):** đọc toàn bộ 360 dòng đối chiếu JP+TW, mọi VN đều khớp đúng câu JP của nó — không có dòng nào là bản dịch của một dòng khác.
- **0 chuỗi xoay (rotation chains):** không có.
- **0 nhiễm chéo file:** kiểm tra bằng chỉ mục VN toàn dự án (mọi VN dài >25 ký tự trong file này đối chiếu với 93.159 dòng TOML-2). Chỉ 2 ứng viên trùng VN ở file khác, cả hai đều là câu lặp hợp lệ với JP gần như giống hệt (2036 「ありがとうございます。双鉄様」 vs 様さま ở 仲国01 1741; 2340 「固く握手」 vs 「固く、握手」 ở ハチロク06 3221) — không phải nhiễm chéo.
- **0 dòng mồ côi, 0 dòng chưa dịch, 0 khóa trùng lặp.**

## 5. Đối chiếu sweep gasp (っ)

- **Sweep có 3 mục, lấy nguyên văn cả 3:** 1996 (lost-gasp-trailing), 2098 + 2099 (lost-gasp-whole).
- **1 sweep-missed, bổ sung từ audit:** 1490 — JP nguyên dòng 「っ――」, VN chỉ còn 「——」; sửa thành 「Ư――」 theo quy tắc gasp nguyên dòng.
- **Các ứng viên っ khác đã xét và KHÔNG sửa:** っ nhấn mạnh cuối câu gắn vào từ (không bao giờ thêm Ư theo quy tắc sweep): 1692 ダメっ, 1719 けれどっ, 1750 ハチロクっ, 1785 ダメばいっ, 1885 のかっ, 1917 わたくしのせいっ, 1993 ではないっ. SFX đã diễn: 1792 ひゃあうっ→"Á á", 1795 きゃっ→"Á", 1800 みゃっ→"Hả", 1807 んんっ→"Hừm", 1824 うぉぷっ→"Oái", 1826 んっ……くっ→"Ưm……ư", 1755 tiếng hét dài→"Khônggggggggggg", 1814 ごめ――んっ (lắp bắp)→"X-Xin——lỗi", 2039 しまっ――あっ→"này——Á", (32)/(2824) ぱしゃんっ/ばしゃんっ→"Ào!".

## 6. Thẻ %l

- **0 thẻ malformed trong file** (cả JP lẫn VN): mọi thẻ đều đóng đúng dạng `%l;#;`.
- **3 thẻ VN tự thêm, đã gỡ** (tiền lệ reina02 — JP chỉ có [ボディ] dạng ruby trong ngoặc, không có thẻ %l): 1486 (運転体), 1747 + 1810 (整備体). Cả 3 dòng đều kèm sửa gloss sai (xem §3).
- Số lượng thẻ JP = VN ở mọi dòng còn lại.

## 7. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 40 fix so với JP của từng dòng: **tổng 40 / kiểm tra lại 40 / loại bỏ 0 / sửa 0**. Ghi chú của parent (20/11): sau lần 2, parent loại thêm 2 fix sai (1980, 2071 — "anh" với Reina là ĐÚNG vì Reina gọi Soutetsu là "anh Soutetsu", xem §3) nên tổng cuối là **38 fix**. Không phát hiện thêm sai sót nào ở lần 2. Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt.

## 8. Giữ nguyên (đã kiểm tra, không sai)

- **2023** Soutetsu 「水と石炭を持ってくるか？」 → "Anh đi lấy nước và than nhé?" — người nghe mơ hồ: Hibiki là người được giao việc lấy than/nước (2010) và cô ấy lại xung phong ở 2080, nên "anh" có thể đúng (nói với Hibiki). Không sửa; ghi nhận là trường hợp biên.
- **1912** Hachiroku "Chị mới là người phải xin lỗi, đã mất bình tĩnh làm em giật mình." — người nghe là Reina: Hachiroku tự xưng "chị" với Reina là đúng (tiền lệ 1966 "Chị hiểu mà" nói với Reina). Không sai.
- **1901** "đôi chân của mình" giữ nguyên — "mình" ở đây là chân của Hachiroku (phản thân ngôi hai, JP: お前の足), không phải Soutetsu tự xưng; chỉ sửa "Anh"→"Tôi".
- **2519** "ấn tượng mình cảm nhận được" và **2572** "chà lưng cho mình" — "mình" phản thân/tân ngữ, giữ theo tiền lệ file 06.
- **Độc thoại Hibiki tự xưng "em"** (1474, 2267, 2300, 2417, 2467, 2538, 2663…) — giọng nội tâm thân mật của cô ấy, giữ nguyên (quy tắc "tôi" chỉ áp cho Soutetsu).
- **1808** Paulette 「ああっ」 → "A." — tiếng thốt ngắn, giữ nguyên.
- **1865** 「はい！　やりますっ」 → "Vâng! Tôi đi đây!" — theo TW (我去), giữ nguyên.
- **1695** 適宜に → "thỉnh thoảng" — chấp nhận được, giữ nguyên.
- **乗務鞄 "túi phi hành đoàn"** (1485, 1486, 2088, 2692) — giữ nguyên, chờ quyết định thống nhất (§10).

## 9. Ohitoyo còn lại

File này sửa xong 2 lần Ohimitera cuối cùng (1881, 2547) — file 08 giờ còn 0. Toàn 00_Common còn **88 lần**: file 14: 30, 15: 15, 10: 14, 11: 12, 12: 6, 13: 3, 01 pilot: 8 (chưa chốt) — file 09 đã sửa xong 15 lần.

## 10. Điểm để lại cho đợt thống nhất

1. **乗務鞄 gloss — cần Hieu chốt một cách chung.** Toàn dự án: "túi phi hành đoàn" 11 dòng (kể cả 1 dòng viết hoa) vs "cặp lái tàu" 3 dòng. TW dùng 乘務包 (túi công vụ). "Phi hành đoàn" là thuật ngữ hàng không (flight crew) — sai lĩnh vực với túi đồ của nhân viên đường sắt — nhưng nó là đa số toàn dự án và nhất quán nội bộ file này (4/4), nên audit giữ nguyên, không tự ý đổi. Cần chốt: giữ "túi phi hành đoàn", hay đổi hết về "cặp lái tàu", hay một cách khác.
2. **2023** (xem §8) — nếu Hieu xác nhận người nghe là Hachiroku thì sửa "Anh"→"Tôi"; nếu là Hibiki thì giữ nguyên.

## Đính chính của parent (20/11)

Quy tắc xưng hô của Soutetsu đã được sửa lại: **"anh" với Hibiki/Michiko/Paulette/Reina** (các em gái gọi Soutetsu là "anh"/"anh hai" — Hibiki gọi "anh hai", Michiko là em sinh đôi, Paulette gọi "anh Soutetsu" per khóa B4, Reina gọi "anh Soutetsu"); **"tôi" với Hachiroku/Mayami/Nagi/Minokasa** (quan hệ trang trọng/xa cách). Cách diễn đạt cũ "anh chỉ với Hibiki" (từ file 02) là quá hẹp — audit đã áp dụng sai thành 2 fix: **1980** (nói với Reina, "Reina." gọi tên trực tiếp) và **2071** (trả lời Reina ở 2069), cả hai đều giữ "anh" mới đúng. Parent đã loại cả hai khỏi fix list. Các fix "anh"→"tôi" còn lại đều nói với Hachiroku (1688 đã xác nhận: cả đoạn 1688–1725 chỉ có Soutetsu + Hachiroku).

## Kết bài

File 08_傷跡 là file Common có lỗi tập trung rõ rệt: **38/360 dòng sai (10,6%)**, gần một nửa là đại từ Soutetsu (18/38), chủ yếu xưng "anh" với Hachiroku (13 dòng) — thói quen hệ thống của người dịch cũ, không phải lỗi rải rác. Phần còn lại là thuật ngữ gloss sai đã có quyết định (整備体/運転体/タブレット/Ohitoyo) và 4 gasp mất. Không có lệch dòng, không có chuỗi xoay, không có nhiễm chéo — file sạch về cấu trúc, chỉ cần áp fix list là xong. 0 dòng chưa chắc chắn. Hai điểm để lại cho Hieu: gloss 乗務鞄 và trường hợp biên 2023.

## Khối TOML (kiểm chứng parse: 38 key, 0 sai lệch giá trị so với JSON)

```toml
[script]
71 = "Vết thương của \\x%lレイルロオド;#00ffc040;Railord%l;#; cũng tự nhiên \"lành\" lại sao,\\ntôi nhận ra trên người Hachiroku cũng có vết sẹo."
76 = "\\x%l整備体;#00ffc040;thân bảo trì%l;#;……Hachiroku, người nhỏ bé hơn tôi một chút,\\nnhìn thoáng qua thì giống hệt một bé gái con người."
77 = "Hachiroku trong \\x%l整備体;#00ffc040;thân bảo trì%l;#;,\\nchỉ cho tôi xem một chiếc cặp màu đen đặt ở nơi có vẻ như là ghế lái."
1456 = "――Một âm thanh vang lên. Cùng lúc đó, \\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku\\nđổ gục xuống như một món đồ chơi bị đứt cót."
1480 = "「\\x%lタブレット;#00ffc040;máy tính bảng%l;#;……là linh hồn của em sao?」"
1486 = "「Bên trong \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; được thiết kế để vừa vặn chứa thân vận hành ạ.」"
1490 = "「Ư――」"
1688 = "「Không đâu? Nhanh hơn tôi tưởng nhiều.」"
1725 = "「Nhanh hơn tôi tưởng nhiều, và là một bước đi vô cùng tuyệt vời.」"
1747 = "「Chị Hachiroku, là thân bảo trì nhỉ~.\\nTuyệt quá đi ạ~, cực kỳ, cực kỳ đẹp luôn đó ạ~」"
1782 = "「Để đánh dấu những chỗ hư hỏng thì thế này là quá đủ rồi.\\nTôi muốn bắt đầu. Hachiroku. Nhờ em chỉ dẫn cho tôi nhé.」"
1810 = "「A……may quá.\\nLà em——là thân bảo trì của em ạ.」"
1855 = "「Cảm ơn em.\\nĐến lúc đó thì chắc tôi cũng chẳng còn tâm trí đâu mà khách sáo nữa.」"
1858 = "「Được rồi, Hachiroku. Ra chỉ thị cho tôi đi.\\nTôi muốn hoàn thành trước 23:00.」"
1876 = "「Nếu em bỏ cuộc, tôi sẽ không phản đối.\\nTôi sẽ làm theo ý em——giết chết \\x%l8620;#00ffc040;8620%l;#;.」"
1881 = "「Thứ này……đã bị kéo lê đến tận Ohitoyo sao.」"
1897 = "「Có tôi và em mà.\\nChỉ cần tập trung thì sẽ làm được thôi.」"
1901 = "「Tôi sẽ không giúp đâu.\\nHachiroku, em phải tự đứng lên bằng chính đôi chân của mình.」"
1921 = "「Tôi hiểu rồi. Lúc đó tôi sẽ quan sát cách làm của em rồi học theo.」"
1923 = "「Tôi hiểu rồi. Tôi sẽ giữ nó cẩn thận.」"
1929 = "「Em sẽ đổi \\x%lタブレット;#00ffc040;máy tính bảng%l;#;.\\nNgài đừng ngạc nhiên nhé?」"
1937 = "「Từ đây trở đi sẽ có tôi đồng hành.\\nHachiroku, trước tiên chúng ta bắt đầu từ đâu?」"
1958 = "「Vậy sao? Tôi thấy bản vẽ đẹp mà.」"
1974 = "「Paulette, nếu em muốn——và giả sử nó có ở đó thật,\\nthì em có thể vào xem tình trạng của \\x%l8620;#00ffc040;8620%l;#; trước giúp tôi được không?」"
1982 = "「May mà Reina cũng đến bằng \\x%l整備体;#00ffc040;thân bảo trì%l;#; nha~.\\nReina sẽ cố gắng hết sức giúp đỡ chị Hachiroku đó nha~」"
1991 = "「Nếu so sánh với cơ thể con người,\\nthì em nghĩ \\x%lタブレット;#00ffc040;máy tính bảng%l;#; giống với bộ não hơn ạ.」"
1996 = "「Đó, Hachiroku. Vào rồi đấy——Ư!?」"
1999 = "「Xin lỗi em nhé. Nhưng nhờ có em mà tôi đỡ vất vả hơn nhiều.」"
2076 = "「Vậy thì Hachiroku. Tôi sẽ hỏi em một lần cuối.\\nEm sẽ cứu \\x%l8620;#00ffc040;8620%l;#; chứ? Hay là bỏ mặc nó?」"
2084 = "「A-Anh Soutetsu!?」"
2098 = "「Ư!」"
2099 = "「Ư!!」"
2453 = "Em ấy mở phần ngực áo của \\x%l整備体;#00ffc040;thân bảo trì%l;#; đang nằm gục ra,\\nrút từ đó ra một thứ gì đó giống như một chiếc vòng cổ——"
2517 = "Khi tôi mở cặp ra, Hachiroku nhẹ nhàng trao \\x%l運転体;#00ffc040;thân vận hành%l;#; cho tôi.\\nCho vào trong cặp——à, quả thực là vừa khít luôn."
2529 = "Làm theo yêu cầu của Hachiroku, tôi đặt \\x%l運転体;#00ffc040;thân vận hành%l;#; xuống sàn nhà,\\ncơ thể nhỏ bé đó lặng lẽ, lặng lẽ tiến lại gần cơ thể đang nằm gục kia."
2547 = "Được Paulette và Reina dẫn đường,\\nchúng tôi đi qua sân ga Ohitoyo, tiến sâu hơn vào bên trong khuôn viên."
2692 = "So với độ nặng trịch của \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;,\\nthì \\x%l運転体;#00ffc040;thân vận hành%l;#; lại quá đỗi nhẹ nhàng."
2836 = "（Đó là cái gọi là \\x%lタブレット;#00ffc040;máy tính bảng%l;#; sao?\\nHachiroku có nói là đổi, nhưng mà……）"
```
