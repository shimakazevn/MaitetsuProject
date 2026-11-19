# Audit 00_Common file 14 — 共通14_負債.txt.toml

**52/411 dòng sai (12,7%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 32 | Ohimitera→Ohitoyo 30 (1082, 1128, 1137, 1411, 1461, 1467, 1487, 1499, 1520, 1529, 1551, 1569, 1637, 1657, 1662, 1671, 1686, 1731, 1735, 1766, 1797, 1805, 1831, 1834, 1896, 1928, 2404, 2488, 2642, 2674 — đúng con số ~30 đã đếm trước đó); Yui→Yunoi 4 (1435, 1571, 1671, 1805 — 1671 và 1805 trùng với Ohimitera, cùng dòng); 帝鉄→Teitetsu 1 (1717) |
| Đại từ | 15 | Soutetsu tự xưng "em"→"tôi"/"anh" 5 (1471, 1554, 1555, 1832 → "tôi"; 1874 → "anh" với Hibiki); Soutetsu "Anh"→"Tôi" 2 (1407 với Kisaki, 1418 với ngân hàng); Soutetsu "tôi"→"anh" với Paulette 2 (1527, 1599); Paulette tự xưng "mình"→"em" 1 (1529, kèm Ohimitera); Soutetsu gọi Paulette "cô"→"em" 1 (1858); Soutetsu "Cảm ơn cô"→"Cảm ơn chị" 1 (1559, với Mayami — xem §7); độc thoại lời nghĩ thầm "Em"→"Tôi" 2 (2152, 2402) |
| Gasp (っ) | 3 | 1443, 1549, 1550 — cả 3 đều từ sweep, đã kiểm chứng đúng với JP và được nhận nguyên văn (1443 đã khôi phục dạng \n của CSV3) |
| Tag %l | 1 | 1548 (VN tự thêm tag cho 8620; 1571 cũng gỡ tag nhưng tính vào thuật ngữ) |
| Nhỏ | 1 | 2686 (dấu ・ Nhật → " và ") |
| **Tổng** | **52** | |

Thoại 44/236 sai (18,6%), độc thoại 8/175 sai (4,6%). Theo nhân vật: 双鉄 26, monologue 8, ポーレット 8, 日々姫 5, 浦上 3, 稀咲 1, 元忠 1.

File này là file 00_Common "nặng thuật ngữ" nhất từ trước đến nay: 32/52 lỗi là thuật ngữ (61,5%), trong đó riêng Ohimitera chiếm 30 dòng — đúng như con số ưu tiên đã đếm (~30). Sau file này, số Ohimitera còn lại trong 00_Common giảm từ 56 xuống **23** (file 15: 15, file 01 pilot: 8 chưa xác nhận; file 13 đã sửa hết 3 dòng của nó trong audit song song — xem §7).

## 2. Phương pháp

- Nguồn: CSV3 bộ duy nhất 00_Common (411 dòng, toàn `script`, key 1075–2734, 411 key duy nhất); TOML-2 `共通14_負債.txt.toml` (`00_Common/#U5171#U901a14_#U8ca0#U50b5.txt.toml`), md5 `1c10d754dc7442a5347c67bbdec03f99`, 93.437 byte, BOM + CRLF (867 CRLF, 0 LF-only), `[selections]` rỗng, không có bản sao trùng (md5 chỉ xuất hiện 1 lần — không thuộc 11 nhóm trùng).
- So sánh CSV↔TOML: 136 dòng khớp tuyệt đối + 274 dòng khớp sau khi gộp ký tự xuống dòng + **1 khác biệt duy nhất ở 1955** (TOML-2 làm phẳng `\n` thành khoảng trắng — hiện tượng đã biết; CSV3 là bản tin cậy cho fix list; bản thân VN ở 1955 là đúng, không cần sửa).
- Đọc từng dòng theo ngữ nghĩa so với JP + TW, toàn bộ 411 dòng, chia 4 đợt (1075–1631, 1637–1932, 1933–2395, 2397–2734). Xác định người nghe từ cột Character + 3–5 dòng xung quanh + luồng hội thoại, không dựa vào thứ tự key (file này các cảnh xen kẽ theo key: cảnh ngân hàng, cảnh ga, cảnh độc thoại đan nhau).
- Sweep っ: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **3 mục** (1443, 1549, 1550). Cả 3 giá trị đã kiểm chứng đúng với JP và được nhận nguyên văn (1443: giá trị sweep có `\n` bị làm phẳng thành khoảng trắng như TOML-2, đã khôi phục dạng `\n` của CSV3). Quét bổ sung toàn bộ 143 dòng JP chứa っ: các dòng còn lại đều là っ trong từ (だった, って, まったく…), っ nhấn mạnh cuối câu gắn với từ (ばいっ, ねっ, けんっ, にぃにっ…), hoặc âm đã được render (1540 あっ!→"A!", 1984 ええっ!?→"Hả!?", 2532 んんっ?→"Hửm?", 2322 ほっと→"thở phào"). Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra toàn bộ chỉ mục VN của dự án — các VN trùng nhau trong file chỉ là 3 cặp câu ngắn thông dụng, JP tương ứng cũng giống nhau (1116/1117 「…………」, 1535/1561 「うん」, 1501/1748 「なるほど」) — dịch độc lập giống nhau, không phải nhiễm chéo. Không có VN nào trong file khớp với JP của file khác. 0 nhiễm chéo.
- Kiểm tra chuỗi xoay trước khi dịch mới: không có dòng lệch nào, nên không cần dịch mới dòng nào; không có dòng mồ côi, không có dòng chưa dịch (VN trống: 0; VN==JP: chỉ 1116/1117 「…………」 — JP cũng là 「…………」, đúng).
- Quét cơ học toàn bộ giá trị VN đầy đủ (không cắt ngắn — bài học file 12): các thuật ngữ đã chốt chỉ còn đúng các dòng trong fix list (Ohimitera đúng 30 = đúng số JP 御一夜 30; Yui đúng 4 = đúng số JP 湯医 4; 帝鉄 đúng 1); tag %l: 0 tag hỏng (số tag mở = số tag đóng ở mọi dòng, cả phía JP), chỉ 2 tag VN tự thêm (1548, 1571 — đã sửa); ký tự Nhật ngoài tag %l chỉ còn 2686 (dấu ・ — đã sửa) và 3 dòng gasp sweep (1443, 1549, 1550 — đã sửa).
- Quy tắc áp dụng: Ohitoyo / Teitetsu / Yunoi / "chủ tàu" / "tàu điện thành phố" / "thân bảo trì" / "thân vận hành" / KiHa / "đền chủ" / Migita Ichi / "vé lượt" / Railord / Olivy; quy tắc đại từ Soutetsu đã sửa ("anh" với Hibiki/Michiko/Paulette/Reina/Fukami, "tôi" với Hachiroku/Mayami/Nagi/Minokasa/Kisaki — KHÔNG dùng lối tắt cũ "chỉ với Hibiki"); khóa B4 (双鉄くん→"anh Soutetsu", không có ngoại lệ rên; tên trần ソウテツ trong cảnh gọi tên là có chủ đích); Hachiroku với Fukami là "chị" (tiền lệ file 10 key 2616); quy tắc ngẫu hứng 22:05 (SFX theo nhân vật + ngữ cảnh, không dập khuôn; tiếng cười không bao giờ thành tiếng rên); công thức độ dài nguyên âm (số nguyên âm VN = 1 + số う/ぅ trong JP); JP thắng TW khi xung đột; cảnh giác bịa của Gemini (từ bịa không có cơ sở JP, tag %l tự thêm, hoàn thiện câu JP bị cắt cụt — nhưng kiểm tra TW trước khi kết luận 義 là bịa: 義父/義母 có thể là "bố nuôi/mẹ nuôi" khi TW nói 養父/養母; 義理の弟/義理の兄 ở 2206/2317 giữ nguyên "em trai nuôi"/"anh trai nuôi" vì TW nói 義弟/義兄 — xem §4).

## 3. Các lỗi đã sửa (52 dòng)

### 1082 — monologue — thuật ngữ

**JP:** あった、は過去形。⏎御一夜駅には、ターンテーブルは現存している。

**TW:** “曾經有過”……可御一夜站的轉車盤，如今仍然存在著。

**VN cũ:** Đã từng có, là thì quá khứ.⏎Bàn quay đầu máy ở ga Ohimitera hiện tại vẫn còn tồn tại.

**Fix:** Đã từng có, là thì quá khứ.⏎Bàn quay đầu máy ở ga Ohitoyo hiện tại vẫn còn tồn tại.

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1128 — 稀咲 — thuật ngữ

**JP:** 「……ボクも御一夜の生まれだ。キミの主張もわかる。⏎わかるからこそ、ボクも融資の許諾を出した」

**TW:** 「……我也是御一夜出身。也明白你的主張。正因明白，我才同意了融資一事」

**VN cũ:** 「……Tôi cũng sinh ra ở Ohimitera. Tôi hiểu lập trường của cậu.⏎Chính vì hiểu, nên tôi mới chấp thuận khoản vay này.」

**Fix:** 「……Tôi cũng sinh ra ở Ohitoyo. Tôi hiểu lập trường của cậu.⏎Chính vì hiểu, nên tôi mới chấp thuận khoản vay này.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1137 — 日々姫 — thuật ngữ

**JP:** 「……にぃにの好きにすればいいばい。⏎御一夜が栄えることは、みんなの共通の希望やもん」

**TW:** 「……隨便阿哥咧。因為御一夜的繁榮，是大家共同的願望嘛」

**VN cũ:** 「……Anh hai cứ làm theo ý mình đi.⏎Ohimitera phồn vinh, là hy vọng chung của tất cả mọi người mà.」

**Fix:** 「……Anh hai cứ làm theo ý mình đi.⏎Ohitoyo phồn vinh, là hy vọng chung của tất cả mọi người mà.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1407 — 双鉄 — đại từ

**JP:** 「いいや……特には何も。⏎何も、言ってなかったかと思う」

**TW:** 「不……沒說什麼。她應該沒有說過什麼話」

**VN cũ:** 「Không…… Không có gì đặc biệt cả.⏎Anh nghĩ là em ấy không nói gì.」

**Fix:** 「Không…… Không có gì đặc biệt cả.⏎Tôi nghĩ là em ấy không nói gì.」

Soutetsu tự xưng "Anh" → "Tôi": đang trả lời Kisaki (nói ở 1404); Kisaki gọi cậu là "cậu", cậu gọi cô là "cô" — quan hệ trang trọng/thương vụ, tự xưng "tôi" theo tiền lệ lr_稀咲h1.

### 1411 — 双鉄 — thuật ngữ

**JP:** 「ではない。御一夜という、僕の第二の故郷を。⏎その水資源と環境を穢させない――それが、僕の目的だ」

**TW:** 「不是的。是為了不讓我的第二故鄉，御一夜的水資源與環境遭到汙染——這才是我的目的」

**VN cũ:** 「Không phải. Ohimitera là quê hương thứ hai của tôi.⏎Bảo vệ nguồn nước và môi trường nơi đây không bị ô nhiễm——đó mới là mục đích của tôi.」

**Fix:** 「Không phải. Ohitoyo là quê hương thứ hai của tôi.⏎Bảo vệ nguồn nước và môi trường nơi đây không bị ô nhiễm——đó mới là mục đích của tôi.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1418 — 双鉄 — đại từ

**JP:** 「わからん。失敗するつもりは全く無いので、⏎確認しようとも思わなかった」

**TW:** 「不知道。我完全沒有作失敗的打算，所以也沒想到要問」

**VN cũ:** 「Anh không biết. Vì anh hoàn toàn không có ý định thất bại,⏎nên cũng không nghĩ đến việc xác nhận lại.」

**Fix:** 「Tôi không biết. Vì tôi hoàn toàn không có ý định thất bại,⏎nên cũng không nghĩ đến việc xác nhận lại.」

Soutetsu tự xưng "Anh" → "Tôi" (2 chỗ): đang trả lời người của ngân hàng (Urakami/Kisaki). Với Urakami là mẫu "anh–tôi" trong công việc (bằng chứng 1781 tự xưng "tôi" với Urakami); với Kisaki là "tôi". Dù người nghe là ai thì "tôi" cũng đúng.

### 1435 — 双鉄 — thuật ngữ

**JP:** 「つまり、かつては湯医にもターンテーブルがあり、⏎しかし、それは失われてしまったのだな？」

**TW:** 「也就是說，曾經在湯醫也有轉車盤，而現在已經沒有了是嗎？」

**VN cũ:** 「Nghĩa là, trước đây ở Yui cũng từng có bàn quay đầu máy,⏎nhưng mà, nó đã bị mất rồi sao?」

**Fix:** 「Nghĩa là, trước đây ở Yunoi cũng từng có bàn quay đầu máy,⏎nhưng mà, nó đã bị mất rồi sao?」

湯医 = "Yunoi" (quyết định 19/11; "Yui" sai).

### 1443 — 日々姫 — gasp

**JP:** 「なんね！　父さんも、その元忠いうおっさんも、⏎にぃにぃのこと、まるっきりモノ扱いしよって～っ」

**TW:** 「什麼嘛！不管是爸爸，還是那個叫元忠的大叔，都完全把阿哥當東西一樣對待～」

**VN cũ:** 「Gì chứ! Cả bố lẫn cái ông chú Mototada đó,⏎hoàn toàn coi anh hai như đồ vật vậy～っ」

**Fix:** 「Gì chứ! Cả bố lẫn cái ông chú Mototada đó,⏎hoàn toàn coi anh hai như đồ vật vậy～Ư」

Sweep っ: giá trị sweep đã kiểm chứng đúng với JP, áp dụng nguyên văn (1443 đã khôi phục dạng \n của CSV3).

### 1456 — 双鉄 — đại từ

**JP:** 「だがな日々姫。ナビは――⏎あれは、僕がここに戻った目的を忘れてはおらんのだ」

**TW:** 「但是啊，日日姬。Ｎａｖｉ——它沒有忘記我回到這裡的目的」

**VN cũ:** 「Nhưng mà Hibiki này. Navi——⏎nó không hề quên mục đích tôi quay lại đây đâu.」

**Fix:** 「Nhưng mà Hibiki này. Navi——⏎nó không hề quên mục đích anh quay lại đây đâu.」

Soutetsu tự xưng "tôi" → "anh": câu mở đầu "Nhưng mà Hibiki này" — nói trực tiếp với Hibiki, người gọi cậu là "anh hai".

### 1461 — 双鉄 — thuật ngữ

**JP:** 「が、現在の倉庫の所有者――つまり御一夜鉄道が、⏎正当な受取先であると認められたのだな？」

**TW:** 「但是，如今倉庫的所有者——御一夜鐵路已經被認定為正當的收款方了是嗎？」

**VN cũ:** 「Nhưng mà, chủ sở hữu hiện tại của nhà kho——tức là Đường sắt Ohimitera,⏎đã được công nhận là người nhận hợp pháp rồi đúng không?」

**Fix:** 「Nhưng mà, chủ sở hữu hiện tại của nhà kho——tức là Đường sắt Ohitoyo,⏎đã được công nhận là người nhận hợp pháp rồi đúng không?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1467 — ポーレット — thuật ngữ

**JP:** 「でも、あの――話を巻き戻しちゃいますけど、⏎これは日々姫ちゃんも言ったとおりに御一夜鉄道の問題で」

**TW:** 「但是，那個——回到原來的話題，日日姬說得沒錯，這是御一夜鐵路的問題」

**VN cũ:** 「Nhưng mà, ừm——em xin phép quay lại chủ đề chính một chút,⏎đúng như Hibiki đã nói, đây là vấn đề của Đường sắt Ohimitera.」

**Fix:** 「Nhưng mà, ừm——em xin phép quay lại chủ đề chính một chút,⏎đúng như Hibiki đã nói, đây là vấn đề của Đường sắt Ohitoyo.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1471 — 双鉄 — đại từ

**JP:** 「帝大を休学し、酒問屋の方も休ませてもらう条件として、⏎僕は、[とう,1]義父さんといくつか約束をしているんだ」

**TW:** 「作為從帝大休學，同時也不幫酒行做事的條件，我答應了父親的幾個要求」

**VN cũ:** 「Với điều kiện là bảo lưu kết quả học tập ở Đại học Đế quốc, và xin nghỉ việc ở xưởng rượu,⏎em đã hứa với cha nuôi vài điều.」

**Fix:** 「Với điều kiện là bảo lưu kết quả học tập ở Đại học Đế quốc, và xin nghỉ việc ở xưởng rượu,⏎tôi đã hứa với cha nuôi vài điều.」

Soutetsu tự xưng "em" → "tôi": "em" không bao giờ đúng với Soutetsu; đang giải thích điều kiện với nhóm ngân hàng → "tôi".

### 1487 — 双鉄 — thuật ngữ

**JP:** 「個々の取引を、それぞれに行う。⏎ただそれだけで、御一夜鉄道の独立性を維持できる」

**TW:** 「兩筆交易，分開進行。只要這樣，就可以維持御一夜鐵路的獨立性」

**VN cũ:** 「Các giao dịch cá nhân sẽ được thực hiện riêng biệt.⏎Chỉ cần như vậy, Đường sắt Ohimitera có thể duy trì được tính độc lập của mình.」

**Fix:** 「Các giao dịch cá nhân sẽ được thực hiện riêng biệt.⏎Chỉ cần như vậy, Đường sắt Ohitoyo có thể duy trì được tính độc lập của mình.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1499 — 双鉄 — thuật ngữ

**JP:** 「なるほど。⏎それで、御一夜駅には\x%l転車台;#00ffc040;[ターンテーブル,2]転車台%l;#;があるのだな？]

**TW:** 「原來如此。正因為這個，御一夜站才有\x%l転車台;#00ffc040;轉車盤%l;#;對吧？」

**VN cũ:** 「Ra là vậy.⏎Vì thế nên ga Ohimitera mới có \x%l転車台;#00ffc040;bàn quay đầu máy%l;#; nhỉ?」

**Fix:** 「Ra là vậy.⏎Vì thế nên ga Ohitoyo mới có \x%l転車台;#00ffc040;bàn quay đầu máy%l;#; nhỉ?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1520 — ポーレット — thuật ngữ

**JP:** 「でも――御一夜鉄道の資産以外で、⏎そんなに大きな担保になるようなものなんて」

**TW:** 「可是——除了御一夜鐵路的資產以外，還有什麼能做如此巨額的擔保——」

**VN cũ:** 「Nhưng mà——ngoài tài sản của Đường sắt Ohimitera ra,⏎thì làm gì còn thứ gì có thể làm tài sản thế chấp lớn đến vậy chứ.」

**Fix:** 「Nhưng mà——ngoài tài sản của Đường sắt Ohitoyo ra,⏎thì làm gì còn thứ gì có thể làm tài sản thế chấp lớn đến vậy chứ.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1527 — 双鉄 — đại từ

**JP:** 「同時に、僕の問題でもあるのだよ。ポーレット。⏎ゆえに、折衷案を、僕は提案しているつもりだ」

**TW:** 「同時，也是我的問題啊。波萊特。所以，我提出的是一個折中方案」

**VN cũ:** 「Đồng thời, nó cũng là vấn đề của tôi. Paulette.⏎Vì vậy, tôi mới định đề xuất một phương án thỏa hiệp.」

**Fix:** 「Đồng thời, nó cũng là vấn đề của anh. Paulette.⏎Vì vậy, tôi mới định đề xuất một phương án thỏa hiệp.」

Soutetsu tự xưng "tôi" → "anh": câu ghi rõ tên Paulette ("Đồng thời, nó cũng là vấn đề của tôi. Paulette.") — với Paulette là "anh".

### 1529 — ポーレット — đại từ

**JP:** 「え？　あ！　そうか、そうですよね！！　最悪の場合、⏎わたしが、御一夜鉄道を担保に新規にお金を借りれば」

**TW:** 「咦？啊！是這樣啊，也對呢！！最壞的情況下，只要我以御一夜鐵路為擔保再去借一筆錢」

**VN cũ:** 「Hả? A! Ra là vậy, đúng vậy nhỉ!! Trong trường hợp xấu nhất,⏎mình chỉ cần lấy Đường sắt Ohimitera làm tài sản thế chấp để vay một khoản tiền mới.」

**Fix:** 「Hả? A! Ra là vậy, đúng vậy nhỉ!! Trong trường hợp xấu nhất,⏎em chỉ cần lấy Đường sắt Ohitoyo làm tài sản thế chấp để vay một khoản tiền mới.」

Paulette tự xưng "mình" → "em": mẫu trong file là "em" (1467, 1564); "mình" lạc khỏi mẫu. (Kèm Ohimitera → Ohitoyo.)

### 1548 — 双鉄 — tag

**JP:** 「ああ。そうなるな。⏎[ハチロクニイマル,3]8620には前後があり、キハ[レイナナ,1]07は、いわば両面が前方だ」

**TW:** 「啊，的確。８６２０有前後之分，而Ｋｉｈａ０７，可以說兩邊都是前方」

**VN cũ:** 「À. Đúng là vậy nhỉ.⏎\x%l8620;#00ffc040;8620%l;#; có phân biệt trước sau, còn KiHa 07 thì có thể nói là hai mặt đều là phía trước.」

**Fix:** 「À. Đúng là vậy nhỉ.⏎8620 có phân biệt trước sau, còn KiHa 07 thì có thể nói là hai mặt đều là phía trước.」

VN tự thêm tag %l cho 8620 trong khi JP chỉ có ruby [ハチロクニイマル,3] — gỡ tag theo tiền lệ reina02/file 09, giữ nguyên chữ "8620".

### 1549 — 日々姫 — gasp

**JP:** 「あー……あー……あ～～っ」

**TW:** 「啊～啊～啊～～」

**VN cũ:** 「Aー……aー……a～～っ」

**Fix:** 「Aー……aー……a～～Ư」

Sweep っ: giá trị sweep đã kiểm chứng đúng với JP, áp dụng nguyên văn (1443 đã khôi phục dạng \n của CSV3).

### 1550 — 日々姫 — gasp

**JP:** 「あ～～っ」

**TW:** 「啊～～」

**VN cũ:** 「A～～っ」

**Fix:** 「A～～Ư」

Sweep っ: giá trị sweep đã kiểm chứng đúng với JP, áp dụng nguyên văn (1443 đã khôi phục dạng \n của CSV3).

### 1551 — 元忠 — thuật ngữ

**JP:** 「おいおい御一夜支店長。⏎頭取に対し、『やめてくれないかな』は無いだろう」

**TW:** 「喂喂，御一夜支行長。對行長說話怎麼能用這種口氣呢」

**VN cũ:** 「Này này giám đốc chi nhánh Ohimitera.⏎Nói với chủ tịch mà lại dùng từ 'được không' sao.」

**Fix:** 「Này này giám đốc chi nhánh Ohitoyo.⏎Nói với chủ tịch mà lại dùng từ 'được không' sao.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1554 — 双鉄 — đại từ

**JP:** 「うん。いや、これは、⏎もっと早くに伝えておくべきことだったんだが――」

**TW:** 「嗯。其實我應該早點告訴你們的——」

**VN cũ:** 「Vâng. À không, chuyện này,⏎lẽ ra em nên nói cho mọi người biết sớm hơn mới phải——」

**Fix:** 「Vâng. À không, chuyện này,⏎lẽ ra tôi nên nói cho mọi người biết sớm hơn mới phải——」

Soutetsu tự xưng "em" → "tôi": "em" không bao giờ đúng với Soutetsu; đang nói với cả nhóm → "tôi".

### 1555 — 双鉄 — đại từ

**JP:** 「うん。その話はお受け出来んと、断った」

**TW:** 「嗯。我說“這個條件我不能接受”，拒絕了他」

**VN cũ:** 「Vâng. Em đã từ chối, bảo là không thể nhận lời được.」

**Fix:** 「Vâng. Tôi đã từ chối, bảo là không thể nhận lời được.」

Soutetsu tự xưng "Em" → "Tôi": như 1554, đang nói với cả nhóm.

### 1559 — 双鉄 — đại từ

**JP:** 「うん。ありがとう」

**TW:** 「嗯。謝謝你」

**VN cũ:** 「Ừm. Cảm ơn cô.」

**Fix:** 「Ừm. Cảm ơn chị.」

Soutetsu "Cảm ơn cô" → "Cảm ơn chị": người được cảm ơn là Mayami — lời đề nghị "đáng quý đến mức lãng phí" (1558) là khoản vay 200 triệu không lãi của Mayami ở 1515; Soutetsu gọi Mayami là "chị", không bao giờ gọi "cô". (Phán đoán từ ngữ cảnh — xem §7.)

### 1569 — 双鉄 — thuật ngữ

**JP:** 「ふむ？　御一夜鉄道は赤字と聞いた気がしたが。⏎市から、補助金でも引っ張れるのか？」

**TW:** 「嗯？我好像聽說過，御一夜鐵路現在還是赤字的狀態。難道能從市裡弄來補助金嗎？」

**VN cũ:** 「Hửm? Hình như tôi nghe nói Đường sắt Ohimitera đang chịu lỗ mà.⏎Có thể xin được tiền trợ cấp từ thành phố sao?」

**Fix:** 「Hửm? Hình như tôi nghe nói Đường sắt Ohitoyo đang chịu lỗ mà.⏎Có thể xin được tiền trợ cấp từ thành phố sao?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1571 — 双鉄 — thuật ngữ

**JP:** 「む？⏎この、『湯医駅[さんかくせん,2]三角線新造』とはなんだ？」

**TW:** 「嗯？這條“新建湯醫站三角線”是什麼？」

**VN cũ:** 「Hửm?⏎Cái 'Xây mới \x%l三角線;#00ffc040;đường tam giác%l;#; ga Yui' này là sao?」

**Fix:** 「Hửm?⏎Cái 'Xây mới đường tam giác ga Yunoi' này là sao?」

湯医 = "Yunoi" (quyết định 19/11; "Yui" sai). VN tự thêm tag %l cho 三角線 trong khi JP chỉ có ruby — gỡ tag, giữ nguyên "đường tam giác".

### 1599 — 双鉄 — đại từ

**JP:** 「返済を滞らせた場合のことなら、僕は厳しくとりたてる。⏎間に僕がいようとも、ポーレットの責任は変わらんぞ？」

**TW:** 「如果借款逾期未還，我會嚴厲地催款。即使有我夾在中間，你所需要擔負的責任也不會有改變哦？」

**VN cũ:** 「Nếu để chậm trễ việc trả nợ, tôi sẽ đòi gắt gao đấy.⏎Cho dù có tôi ở giữa, thì trách nhiệm của Paulette vẫn không thay đổi đâu nhé?」

**Fix:** 「Nếu để chậm trễ việc trả nợ, anh sẽ đòi gắt gao đấy.⏎Cho dù có anh ở giữa, thì trách nhiệm của Paulette vẫn không thay đổi đâu nhé?」

Soutetsu tự xưng "tôi" → "anh" (2 chỗ): đang nói với Paulette (ghi rõ tên trong câu) — với Paulette là "anh".

### 1637 — 浦上 — thuật ngữ

**JP:** 「御一夜鉄道に\x%l保線;#00ffc040;保線%l;#;部が出来たのですか。⏎それは、先日のアクシデントの影響で？」

**TW:** 「御一夜鐵路成立了\x%l保線;#00ffc040;巡線%l;#;部門嗎？是受前幾天那起事故的影響？」

**VN cũ:** 「Đường sắt Ohimitera đã thành lập bộ phận \x%l保線;#00ffc040;bảo trì đường ray%l;#; rồi sao.⏎Đó là do ảnh hưởng từ sự cố hôm nọ à?」

**Fix:** 「Đường sắt Ohitoyo đã thành lập bộ phận \x%l保線;#00ffc040;bảo trì đường ray%l;#; rồi sao.⏎Đó là do ảnh hưởng từ sự cố hôm nọ à?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1657 — 双鉄 — thuật ngữ

**JP:** 「本日は、酒問屋の従業員としてではなく、⏎御一夜鉄道の\x%l保線;#00ffc040;保線%l;#;部長としてご相談に伺いました」

**TW:** 「我今日並非以酒行員工的身份，而是以御一夜鐵路\x%l保線;#00ffc040;巡線%l;#;部門部長的身份前來與您會談」

**VN cũ:** 「Hôm nay, tôi đến không phải với tư cách là nhân viên xưởng rượu,⏎mà là để bàn bạc với tư cách Trưởng bộ phận \x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohimitera.」

**Fix:** 「Hôm nay, tôi đến không phải với tư cách là nhân viên xưởng rượu,⏎mà là để bàn bạc với tư cách Trưởng bộ phận \x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohitoyo.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1662 — 双鉄 — thuật ngữ

**JP:** 「僕は、ナビを担保に稀咲から四億を借り受けよう。⏎そしてそのままの条件で、僕から御一夜鉄道に貸付ける」

**TW:** 「我以Ｎａｖｉ作為擔保，向稀咲借款四億日元。然後再以原條件借給御一夜鐵路」

**VN cũ:** 「Tôi sẽ dùng Navi làm tài sản thế chấp để vay 400 triệu từ Kisaki.⏎Sau đó, với cùng điều kiện đó, tôi sẽ cho Đường sắt Ohimitera vay lại.」

**Fix:** 「Tôi sẽ dùng Navi làm tài sản thế chấp để vay 400 triệu từ Kisaki.⏎Sau đó, với cùng điều kiện đó, tôi sẽ cho Đường sắt Ohitoyo vay lại.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1671 — ポーレット — thuật ngữ

**JP:** 「逆に……多分、ターンテーブルがあったから、⏎御一夜-湯医間に[ハチロクニイマル,3]8620を引いてきたんだと思います」

**TW:** 「我想……或許正因為曾經有過轉車盤，才會將８６２０帶到御一夜至湯醫之間的鐵路上來」

**VN cũ:** 「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,⏎người ta mới đưa 8620 vào chạy tuyến Ohimitera - Yui đấy ạ.」

**Fix:** 「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,⏎người ta mới đưa 8620 vào chạy tuyến Ohitoyo - Yunoi đấy ạ.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai). 湯医 = "Yunoi" (quyết định 19/11; "Yui" sai).

### 1686 — ポーレット — thuật ngữ

**JP:** 「ですので当然、\x%l保線;#00ffc040;保線%l;#;にかかる費用の全てを、⏎御一夜鉄道株式会社が支払うつもりです。けど――」

**TW:** 「所以，\x%l保線;#00ffc040;巡線%l;#;所產生的一切費用，自然由御一夜股份公司全額承擔。但是——」

**VN cũ:** 「Vì thế nên đương nhiên, toàn bộ chi phí liên quan đến \x%l保線;#00ffc040;bảo trì đường ray%l;#;,⏎Công ty Cổ phần Đường sắt Ohimitera dự định sẽ chi trả toàn bộ. Nhưng mà——」

**Fix:** 「Vì thế nên đương nhiên, toàn bộ chi phí liên quan đến \x%l保線;#00ffc040;bảo trì đường ray%l;#;,⏎Công ty Cổ phần Đường sắt Ohitoyo dự định sẽ chi trả toàn bộ. Nhưng mà——」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1717 — ポーレット — thuật ngữ

**JP:** 「はい、\x%l帝鉄;#00ffc040;帝鉄%l;#;が解体されて以降は、そのお金、⏎支払先不明で市が預かる形になってたみたいです」

**TW:** 「是。自\x%l帝鉄;#00ffc040;帝國鐵路%l;#;解體以來，那筆錢因為收款方已經解體，一直由市裡保管著」

**VN cũ:** 「Vâng, kể từ sau khi \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; giải thể, số tiền đó,⏎thành phố có vẻ đã giữ lại dưới dạng khoản thu không rõ người nhận.」

**Fix:** 「Vâng, kể từ sau khi \x%l帝鉄;#00ffc040;Teitetsu%l;#; giải thể, số tiền đó,⏎thành phố có vẻ đã giữ lại dưới dạng khoản thu không rõ người nhận.」

帝鉄 = "Teitetsu" (quyết định 19/11; "Đường sắt Hoàng gia" là dịch sai: 帝鉄 = Đường sắt Đế quốc, không phải Hoàng gia).

### 1731 — 日々姫 — thuật ngữ

**JP:** 「線路を悪いまま放っておいたのは御一夜鉄道ばいっ！⏎なんでにぃにが、そこまでするとっ！？」

**TW:** 「是御一夜鐵路沒有好好維護鐵路咧！憑什麼讓阿哥做到這個地步！？」

**VN cũ:** 「Việc bỏ mặc đường ray xuống cấp là lỗi của Đường sắt Ohimitera mà!⏎Tại sao anh hai lại phải làm đến mức đó chứ!?」

**Fix:** 「Việc bỏ mặc đường ray xuống cấp là lỗi của Đường sắt Ohitoyo mà!⏎Tại sao anh hai lại phải làm đến mức đó chứ!?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1735 — 双鉄 — thuật ngữ

**JP:** 「はい。現在の御一夜鉄道の\x%l保線;#00ffc040;保線%l;#;体制は、⏎率直にいって十分なものではないと判断してのことです」

**TW:** 「是的。御一夜鐵路目前的\x%l保線;#00ffc040;巡線%l;#;制度，說實話還不夠完善」

**VN cũ:** 「Vâng. Thẳng thắn mà nói thì,⏎là do tôi đánh giá hệ thống \x%l保線;#00ffc040;bảo trì đường ray%l;#; hiện tại của Đường sắt Ohimitera vẫn chưa đủ tốt.」

**Fix:** 「Vâng. Thẳng thắn mà nói thì,⏎là do tôi đánh giá hệ thống \x%l保線;#00ffc040;bảo trì đường ray%l;#; hiện tại của Đường sắt Ohitoyo vẫn chưa đủ tốt.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1766 — 浦上 — thuật ngữ

**JP:** 「\x%lエアクラ;#00ffc040;エアクラ%l;#;の作動不能地帯を抱える御一夜では、⏎鉄道の公共性は高いものと当行も評価しています」

**TW:** 「本行也認為，在局部地帶無法使用\x%lエアクラ;#00ffc040;空凝機%l;#;的御一夜地區，鐵路擁有很高的公共需求」

**VN cũ:** 「Tại Ohimitera, nơi có khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,⏎ngân hàng chúng tôi cũng đánh giá cao tính công cộng của đường sắt.」

**Fix:** 「Tại Ohitoyo, nơi có khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,⏎ngân hàng chúng tôi cũng đánh giá cao tính công cộng của đường sắt.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1797 — 双鉄 — thuật ngữ

**JP:** 「浦上さんは、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場を御一夜に建てるために、⏎ここに出向してきているのですよね？」

**TW:** 「浦上經理，你是為了在御一夜這裡建造\x%lエアクラ;#00ffc040;空凝機%l;#;工廠才被派遣到御一夜的吧？」

**VN cũ:** 「Anh Urakami, anh được phái cử đến đây,⏎là để xây dựng nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; ở Ohimitera đúng không?」

**Fix:** 「Anh Urakami, anh được phái cử đến đây,⏎là để xây dựng nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; ở Ohitoyo đúng không?」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1805 — ポーレット — thuật ngữ

**JP:** 「湯医駅の周辺広くが御一夜鉄道の社有地ですから、⏎ターンテーブルより、グっと安く済みます……けど」

**TW:** 「湯醫站周邊一帶，都是御一夜鐵路公司的所有地，所以相比安裝轉車盤，要實惠太多太多……但是」

**VN cũ:** 「Khu vực rộng lớn quanh ga Yui đều là đất của Đường sắt Ohimitera,⏎nên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」

**Fix:** 「Khu vực rộng lớn quanh ga Yunoi đều là đất của Đường sắt Ohitoyo,⏎nên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai). 湯医 = "Yunoi" (quyết định 19/11; "Yui" sai).

### 1831 — 浦上 — thuật ngữ

**JP:** 「御一夜は、非常に有力な候補地として、⏎現地コーディネーターからの推薦を受けています。が」

**TW:** 「當地協調者報告稱，御一夜是非常有力的候選地區。但是——」

**VN cũ:** 「Ohimitera đã nhận được sự tiến cử từ điều phối viên địa phương,⏎như một ứng cử viên vô cùng tiềm năng. Nhưng mà.」

**Fix:** 「Ohitoyo đã nhận được sự tiến cử từ điều phối viên địa phương,⏎như một ứng cử viên vô cùng tiềm năng. Nhưng mà.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1832 — 双鉄 — đại từ

**JP:** 「無論だ。全力を尽くし助けるとも」

**TW:** 「當然。我會盡全力幫忙」

**VN cũ:** 「Đương nhiên rồi. Em sẽ dốc toàn lực để giúp đỡ.」

**Fix:** 「Đương nhiên rồi. Tôi sẽ dốc toàn lực để giúp đỡ.」

Soutetsu tự xưng "Em" → "Tôi": "em" không bao giờ đúng với Soutetsu; đang đáp lời nhóm/Mayami → "tôi".

### 1834 — 双鉄 — thuật ngữ

**JP:** 「無論、仮に工場誘致が強行され、クマ川が汚染され、⏎御一夜の町が損なわれても、僕が死ぬようなことはない」

**TW:** 「當然，即使工廠落戶計劃被強行落實，隈河受到汙染，御一夜這座城市遭受損害，我也不會死」

**VN cũ:** 「Tất nhiên, giả sử việc thu hút nhà máy bị cưỡng chế tiến hành, sông Kuma bị ô nhiễm,⏎thị trấn Ohimitera bị tàn phá, thì tôi cũng chẳng chết được.」

**Fix:** 「Tất nhiên, giả sử việc thu hút nhà máy bị cưỡng chế tiến hành, sông Kuma bị ô nhiễm,⏎thị trấn Ohitoyo bị tàn phá, thì tôi cũng chẳng chết được.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1858 — 双鉄 — đại từ

**JP:** 「この短期間で、良く出してくれたな」

**TW:** 「竟能在這麼短的時間內整理好啊」

**VN cũ:** 「Trong thời gian ngắn như vậy mà cô đã đưa ra được bản dự toán này, làm tốt lắm.」

**Fix:** 「Trong thời gian ngắn như vậy mà em đã đưa ra được bản dự toán này, làm tốt lắm.」

Soutetsu gọi Paulette "cô" → "em": người làm bản dự toán là Paulette (1134); Soutetsu gọi Paulette là "em", không phải "cô".

### 1874 — 双鉄 — đại từ

**JP:** 「その期限内に工場誘致を撤回できれば、⏎見習い期間を終了し、独立を許すとも約束してもらった」

**TW:** 「若能在期限內阻止工廠落戶，父親就答應我結束實習期，並允許我獨立」

**VN cũ:** 「Nếu trong thời hạn đó có thể hủy bỏ việc thu hút nhà máy,⏎cha hứa sẽ kết thúc thời gian học việc và cho phép em tự lập.」

**Fix:** 「Nếu trong thời hạn đó có thể hủy bỏ việc thu hút nhà máy,⏎cha hứa sẽ kết thúc thời gian học việc và cho phép anh tự lập.」

Soutetsu tự xưng "em" → "anh": tiếp nối câu trả lời cho câu hỏi của Hibiki ở 1862 ("Kết hôn với ai?") — với Hibiki là "anh".

### 1896 — ポーレット — thuật ngữ

**JP:** 「その額になると、もう借り入れるしかありません。⏎ですから、御一夜鉄道の設備の一部を担保にすることを」

**TW:** 「要籌到這麼大一筆金額，就只能去借款了。所以，我想以御一夜鐵路的部分設備作為擔保——」

**VN cũ:** 「Với số tiền đó, thì chỉ còn cách đi vay thôi.⏎Vì vậy, việc dùng một phần cơ sở vật chất của Đường sắt Ohimitera làm tài sản thế chấp thì.」

**Fix:** 「Với số tiền đó, thì chỉ còn cách đi vay thôi.⏎Vì vậy, việc dùng một phần cơ sở vật chất của Đường sắt Ohitoyo làm tài sản thế chấp thì.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 1928 — 双鉄 — thuật ngữ

**JP:** 「それはダメだ。\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致賛成派たる銀行に、⏎反対派の本丸である御一夜鉄道の生命線を握らせるのは」

**TW:** 「這樣不行。不可讓支持\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶的銀行，將反對派大本營的御一夜鐵路的性命捏在手裡」

**VN cũ:** 「Không được.⏎Để cho ngân hàng, thuộc phe ủng hộ nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,⏎nắm giữ huyết mạch của Đường sắt Ohimitera - thành trì của phe phản đối thì.」

**Fix:** 「Không được.⏎Để cho ngân hàng, thuộc phe ủng hộ nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,⏎nắm giữ huyết mạch của Đường sắt Ohitoyo - thành trì của phe phản đối thì.」

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 2152 — monologue — đại từ

**JP:** “必ず、全額を返すから”⏎言いかけて、けれども、口には出さずに呑み込む。

**TW:** 一句“我一定全額奉還”，被我咽回了肚子裡。

**VN cũ:** “Em nhất định sẽ trả lại toàn bộ”⏎Tôi định nói vậy, nhưng lại nuốt vào trong, không thốt ra thành lời.

**Fix:** “Tôi nhất định sẽ trả lại toàn bộ”⏎Tôi định nói vậy, nhưng lại nuốt vào trong, không thốt ra thành lời.

Độc thoại, lời nghĩ thầm trong ngoặc kép: Soutetsu tự xưng "Em" → "Tôi". "Em" không bao giờ đúng với Soutetsu.

### 2402 — monologue — đại từ

**JP:** とても言えない。⏎『そんな迷惑はかけられない』、など。

**TW:** 我實在說不出“不能給你添這麼多麻煩”這樣的話。

**VN cũ:** Tôi không thể nào thốt nên lời.⏎Những câu như 『Em không thể gây rắc rối như vậy được』.

**Fix:** Tôi không thể nào thốt nên lời.⏎Những câu như 『Tôi không thể gây rắc rối như vậy được』.

Độc thoại, lời nghĩ thầm trong ngoặc kép: Soutetsu tự xưng "Em" → "Tôi". Như 2152.

### 2404 — monologue — thuật ngữ

**JP:** 話す。飾らず、なにも構えず。⏎御一夜での沢山の出会いが、僕を成長させてくれたこと。

**TW:** 我將回憶毫無掩飾、毫無顧忌地一一訴說出來，訴說那些在御一夜的一場場邂逅，是如何幫助我成長。

**VN cũ:** Tôi kể lại. Không tô vẽ, không e dè.⏎Rằng những cuộc gặp gỡ ở Ohimitera đã giúp tôi trưởng thành.

**Fix:** Tôi kể lại. Không tô vẽ, không e dè.⏎Rằng những cuộc gặp gỡ ở Ohitoyo đã giúp tôi trưởng thành.

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 2488 — monologue — thuật ngữ

**JP:** まして、御一夜外の人間となると、⏎稀咲より厳しい交渉相手なのかもしれん。

**TW:** 更何況他不是御一夜本地人，恐怕是一個比稀咲更難對付的談判對手。

**VN cũ:** Huống hồ, lại còn là người ngoài Ohimitera,⏎có lẽ đây là một đối tác đàm phán khó nhằn hơn cả Kisaki.

**Fix:** Huống hồ, lại còn là người ngoài Ohitoyo,⏎có lẽ đây là một đối tác đàm phán khó nhằn hơn cả Kisaki.

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 2642 — monologue — thuật ngữ

**JP:** だから、僕は御一夜を――⏎この町の水と人とを、損ねたくないと思っていることを。

**TW:** 訴說出，正因如此，我才不想讓御一夜的水與人受到損害。

**VN cũ:** Chính vì vậy, tôi muốn bảo vệ Ohimitera——⏎Bảo vệ nguồn nước và con người của thị trấn này, không muốn chúng bị tổn hại.

**Fix:** Chính vì vậy, tôi muốn bảo vệ Ohitoyo——⏎Bảo vệ nguồn nước và con người của thị trấn này, không muốn chúng bị tổn hại.

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 2674 — monologue — thuật ngữ

**JP:** 隈元銀行御一夜支店長室――⏎宝生稀咲の仕事部屋は、広々として日当たりがいい。

**TW:** 這裡是隈元銀行御一夜支行行長室——寶生稀咲的辦公室，非常寬敞，採光也好。

**VN cũ:** Phòng giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto——⏎Phòng làm việc của Houshou Kisaki, rất rộng rãi và nhiều ánh sáng.

**Fix:** Phòng giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto——⏎Phòng làm việc của Houshou Kisaki, rất rộng rãi và nhiều ánh sáng.

御一夜 = "Ohitoyo" (quyết định 19/11; "Ohimitera" sai).

### 2686 — monologue — nhỏ

**JP:** それはそうだ。\x%l自弁;#00ffc040;自弁%l;#;・\x%l単弁;#00ffc040;単弁%l;#;――⏎\x%lブレーキ;#00ffc040;ブレーキ%l;#;ハンドルを外して歩けば、それでいい。

**TW:** 那是自然。只要將\x%l自弁;#00ffc040;自剎%l;#;・\x%l単弁;#00ffc040;單剎%l;#;——將\x%lブレーキ;#00ffc040;剎車%l;#;杆卸下，走到車的另一邊就行了。

**VN cũ:** Chuyện đó là đương nhiên. \x%l自弁;#00ffc040;Van hãm tự động%l;#;・\x%l単弁;#00ffc040;van hãm đơn%l;#;——⏎Chỉ cần tháo tay gạt \x%lブレーキ;#00ffc040;phanh%l;#; ra rồi mang sang đầu kia là được.

**Fix:** Chuyện đó là đương nhiên. \x%l自弁;#00ffc040;Van hãm tự động%l;#; và \x%l単弁;#00ffc040;van hãm đơn%l;#;——⏎Chỉ cần tháo tay gạt \x%lブレーキ;#00ffc040;phanh%l;#; ra rồi mang sang đầu kia là được.

Dấu ・ (nakaguro Nhật) giữa hai thuật ngữ van hãm trong VN → " và " cho tự nhiên tiếng Việt; JP giữ nguyên cấu trúc tag.

## 4. Các dòng giữ nguyên có chủ đích

- **2206, 2317 — 義理の弟 / 義理の兄 → "em trai nuôi" / "anh trai nuôi" (giữ nguyên).** Không phải bịa kiểu file 06 (義→"nuôi"). Ở file 06, TW nói rõ 血緣關係 (quan hệ huyết thống) trong khi VN nói "anh em nuôi" — mâu thuẫn trực tiếp. Ở đây TW nói 義弟 (2206) và 義兄 (2317) — trong tiếng Trung 義弟/義兄 có nghĩa là em/anh kết nghĩa (không cùng huyết thống), khớp với "em trai nuôi"/"anh trai nuôi" trong bối cảnh Soutetsu được nhận nuôi (1442, 2335). Giữ nguyên.
- **2611 — 義理だなんだ → "chuyện nghĩa lý này nọ" (giữ nguyên).** 義理 = nghĩa vụ/bổn phận gia đình; "nghĩa lý" diễn đúng nghĩa này. Ủng hộ thêm cho cách đọc 2206/2317 ở trên.
- **1407 — "em ấy" (giữ nguyên, chỉ sửa "Anh nghĩ"→"Tôi nghĩ").** "Em ấy" là đại từ ngôi thứ ba (chỉ một người phụ nữ trẻ khác, không phải người nghe Kisaki — không ai gọi người đối diện là "em ấy"); TW cũng nói 她. Người được chỉ chưa xác định được từ ngữ cảnh (có thể là một người phụ nữ trong các lần gặp hồi nhỏ), nhưng bản thân đại từ "em ấy" là hợp lý nên giữ.
- **1418 — giữ "Anh" ở các dòng gọi Urakami ("Anh Urakami", 1434/1667/1781/1797/1801) và chỉ sửa "Anh" tự xưng trong câu trả lời.** Soutetsu gọi Urakami là "anh" (người nghe), tự xưng "tôi" — mẫu "anh–tôi" trong công việc (bằng chứng 1781). Urakami cũng gọi Soutetsu là "anh Migita" (1414, 1631) — hai bên gọi nhau "anh" nhưng tự xưng "tôi", không phải hai "anh" tự xưng.
- **1465, 1469 — Soutetsu tự xưng "tôi" (giữ nguyên).** Không sửa thành "anh" dù 1456 (cùng mạch) sửa thành "anh": 1461/1465/1469 là câu hỏi/giải thích với người của ngân hàng về quyền sở hữu nhà kho và khoản dự toán — người nghe là Kisaki/Urakami, không phải Hibiki. Chỉ 1456 ghi rõ tên Hibiki ("Nhưng mà Hibiki này") mới sửa.
- **1533 — "Cảm ơn cô" (giữ nguyên).** Người được cảm ơn là Kisaki (lời chào đầu buổi họp ngân hàng: "cảm ơn cô đã dành thời gian dù đang bận rộn") — khác với 1559 (cảm ơn Mayami → "Cảm ơn chị"). Hai dòng "Cảm ơn cô" trong file có người nghe khác nhau.
- **1838 — Soutetsu tự xưng "anh" (giữ nguyên).** "Không ai khác chính là anh mà" — câu trả lời ngay sau lời Reina (1836); Reina gọi cậu là "anh Soutetsu" nên "anh" là đúng nếu người nghe là Reina. Giữ (phán đoán từ luồng hội thoại).
- **1990 — "Cảm ơn anh" (giữ nguyên).** "Anh" = Urakami (người liên hệ của ngân hàng trong cuộc họp; Kisaki là "cô", Mototada là "ông" — chỉ Urakami mới là "anh").
- **2482 — "em ấy" trong độc thoại (giữ nguyên).** "Dù vậy, em ấy vẫn không rời khỏi ghế mà tiếp tục lắng nghe" — người được chỉ có khả năng cao là Paulette (dòng 2479 ngay trước đó nói Paulette gật đầu đồng tình; "sự chân thành đó" là sự chân thành của Paulette khi ở lại lắng nghe dù bị chỉ trích gay gắt). Nếu là Kisaki thì phải là "cô ấy" — nhưng luồng 2479→2482 chỉ về Paulette. Giữ.
- **KiHa 07 ở 1957, 2328 (giữ nguyên).** Cả hai đều viết đúng "KiHa 07", tag %l khớp JP. 1548 cũng có "KiHa 07" đúng nhưng bị lỗi tag VN tự thêm ở 8620 (đã sửa).
- **Migita Ichi ở 1697 (giữ nguyên).** 「右田一酒店」 đã dịch đúng "tửu điếm Migita Ichi" — không có "Migita System" trong file này.
- **Đại học Đế quốc ở 1471 (giữ nguyên).** 帝大 đã dịch đúng "Đại học Đế quốc".
- **1935 — "Đi rồi lại lùi" (giữ nguyên).** JP 行って、戻って — "đi rồi lại lùi" diễn đúng thao tác quay đầu trên đường tam giác (đi tới rồi lùi lại), không phải dịch sai.
- **Các "tôi" còn lại của Soutetsu (giữ nguyên).** Toàn bộ các "tôi" khác trong file đều nói với ngân hàng/nhóm (1655, 1657, 1662, 1673, 1674, 1682, 1735, 1781, 1784, 1806, 1879, 1899, 1924, 1931, 1932, 1969, 1970, 1990, 2003, 2004, 2007) hoặc là sở hữu cách "của tôi" (1539, 1754) — đều đúng.

## 5. Kiểm tra chéo

- **Sweep っ-gasp:** 3 mục (1443, 1549, 1550), cả 3 đã kiểm chứng đúng với JP và nhận nguyên văn. Quét bổ sung 143 dòng JP chứa っ: không có gasp nào bị bỏ sót (xem §2).
- **Tag %l:** 0 tag hỏng trong file (mở = đóng ở mọi dòng). 2 tag VN tự thêm đã sửa (1548, 1571). 0 tag JP bị VN bỏ. File này không có dị bản tag JP nào (khác file 07 key 2547, file 09 key 2482, file 10 key 2508, file 12 key 3129).
- **Ký tự ngoại ngữ trong VN:** chỉ còn 2686 (dấu ・) và 3 dòng gasp — tất cả đã sửa. Ngoài ra chỉ có các thuật ngữ JP hợp lệ nằm trong tag %l (8620, 保線, エアクラ, 転車台, 運転台, 列車, 三角線, 帝鉄, 自弁, 単弁, ブレーキ, キハ07).
- **Chuỗi xoay / lệch dòng:** 0. Mọi VN đều khớp JP của chính key đó; không có dòng nào cần dịch mới; không có dòng mồ côi.
- **Nhiễm chéo:** 0 (xem §2).
- **"Ohito":** 0 dòng — toàn bộ 30 dòng 御一夜 đều là "Ohimitera", đã sửa hết thành "Ohitoyo". Không còn "Ohimitera" hay "Ohito" nào trong file này.
- **"Yui":** 0 dòng còn lại sau fix — cả 4 dòng 湯医 đều đã thành "Yunoi".

## 6. Lần đọc thứ hai

Đọc lại toàn bộ 52 giá trị fix so với JP của từng dòng (không đọc từ bản in rút gọn — bài học file 12: fix luôn được dựng từ giá trị VN cũ đầy đủ, và kiểm tra cơ học xác nhận mỗi fix chỉ khác VN cũ đúng ở chỗ sửa có chủ đích).

- **Tổng số fix đọc lại: 52 / 52.**
- **Tái xác nhận: 52 / 52.**
- **Gỡ bỏ: 0.**
- **Sửa lại sau lần đọc thứ hai: 0.**

Lưu ý về lần đọc thứ hai: trong quá trình đọc chunk 1, người audit đã bỏ sót 7 dòng Ohimitera (1467, 1487, 1520, 1662, 1671, 1731, 1797) — được quét cơ học toàn file bắt lại (grep Ohimitera = 30 dòng, khớp đúng số JP 御一夜 = 30). Đây là lý do quét cơ học là bắt buộc, không chỉ đọc mắt.

## 7. Ghi chú cho Hieu

- **1559 — "Cảm ơn cô" → "Cảm ơn chị" (phán đoán từ ngữ cảnh, Hieu có thể bác bỏ).** JP chỉ nói 「うん。ありがとう」 không ghi người nghe. Căn cứ: lời đề nghị ở 1558 ("một lời đề nghị đáng quý đến mức lãng phí" — もったいないほど有り難い) là khoản vay 200 triệu không lãi, không thế chấp của Mayami ở 1515; khoản vay ngân hàng của Kisaki là giao dịch thương mại, không mang sắc thái "đáng quý đến mức lãng phí". Soutetsu gọi Mayami là "chị", không bao giờ gọi "cô". Nếu Hieu thấy người được cảm ơn thực ra là Kisaki thì hoàn lại "Cảm ơn cô".
- **1529 — Paulette tự xưng "mình" → "em" (phán đoán theo mẫu trong file).** Mẫu trong file là "em" (1467, 1564); chỉ 1529 dùng "mình". Tiền lệ file 11 key 2624 thống nhất "Tôi... mình" thành "tôi" trong ngữ cảnh thương vụ — nhưng ở đây trong câu không có "Tôi" để thống nhất theo, và mẫu trong file là "em", nên chọn "em". Hieu có thể bác bỏ nếu muốn Paulette dùng "tôi" trong cảnh họp ngân hàng.
- **1407 — "em ấy" chưa xác định được người được chỉ.** Xem §4. Không tính là dòng chưa chắc chắn vì bản thân đại từ không sai, nhưng nếu Hieu biết "cô ấy" là ai trong cảnh này thì cho biết để ghi chú.
- **Ohitoyo còn lại trong 00_Common sau file này: 23 dòng** (file 15: 15, file 01 pilot: 8 chưa xác nhận). File 13 (audit song song) đã sửa hết 3 dòng Ohimitera của nó. File 14 là file Ohimitera cuối cùng trong 00_Common đã audit xong (30/30).
- **Không có mục mới cho đợt thống nhất (unification pass)** ngoài các mục đã có: các thuật ngữ đã chốt trong file này đều đã áp dụng hết tại chỗ (Ohimitera 30, Yui 4, Teitetsu 1). Không còn "Yui", "Ohimitera", "Ohito", "Đường sắt Hoàng gia" nào trong file này.

## Khối TOML (đã kiểm chứng)

Khối dưới đây đã được parse bằng tomllib: **52 key, 0 lỗi giá trị** (mọi giá trị parse ra đều khớp đúng fix trong JSON). Quy ước: `\\n` trong khối là ký tự xuống dòng theo nghĩa đen (2 ký tự) trong giá trị fix — đúng như CSV3 lưu.

```toml
[script]
"1082" = "Đã từng có, là thì quá khứ.\\nBàn quay đầu máy ở ga Ohitoyo hiện tại vẫn còn tồn tại."
"1128" = "「……Tôi cũng sinh ra ở Ohitoyo. Tôi hiểu lập trường của cậu.\\nChính vì hiểu, nên tôi mới chấp thuận khoản vay này.」"
"1137" = "「……Anh hai cứ làm theo ý mình đi.\\nOhitoyo phồn vinh, là hy vọng chung của tất cả mọi người mà.」"
"1407" = "「Không…… Không có gì đặc biệt cả.\\nTôi nghĩ là em ấy không nói gì.」"
"1411" = "「Không phải. Ohitoyo là quê hương thứ hai của tôi.\\nBảo vệ nguồn nước và môi trường nơi đây không bị ô nhiễm——đó mới là mục đích của tôi.」"
"1418" = "「Tôi không biết. Vì tôi hoàn toàn không có ý định thất bại,\\nnên cũng không nghĩ đến việc xác nhận lại.」"
"1435" = "「Nghĩa là, trước đây ở Yunoi cũng từng có bàn quay đầu máy,\\nnhưng mà, nó đã bị mất rồi sao?」"
"1443" = "「Gì chứ! Cả bố lẫn cái ông chú Mototada đó,\\nhoàn toàn coi anh hai như đồ vật vậy～Ư」"
"1456" = "「Nhưng mà Hibiki này. Navi——\\nnó không hề quên mục đích anh quay lại đây đâu.」"
"1461" = "「Nhưng mà, chủ sở hữu hiện tại của nhà kho——tức là Đường sắt Ohitoyo,\\nđã được công nhận là người nhận hợp pháp rồi đúng không?」"
"1467" = "「Nhưng mà, ừm——em xin phép quay lại chủ đề chính một chút,\\nđúng như Hibiki đã nói, đây là vấn đề của Đường sắt Ohitoyo.」"
"1471" = "「Với điều kiện là bảo lưu kết quả học tập ở Đại học Đế quốc, và xin nghỉ việc ở xưởng rượu,\\ntôi đã hứa với cha nuôi vài điều.」"
"1487" = "「Các giao dịch cá nhân sẽ được thực hiện riêng biệt.\\nChỉ cần như vậy, Đường sắt Ohitoyo có thể duy trì được tính độc lập của mình.」"
"1499" = "「Ra là vậy.\\nVì thế nên ga Ohitoyo mới có \\x%l転車台;#00ffc040;bàn quay đầu máy%l;#; nhỉ?」"
"1520" = "「Nhưng mà——ngoài tài sản của Đường sắt Ohitoyo ra,\\nthì làm gì còn thứ gì có thể làm tài sản thế chấp lớn đến vậy chứ.」"
"1527" = "「Đồng thời, nó cũng là vấn đề của anh. Paulette.\\nVì vậy, tôi mới định đề xuất một phương án thỏa hiệp.」"
"1529" = "「Hả? A! Ra là vậy, đúng vậy nhỉ!! Trong trường hợp xấu nhất,\\nem chỉ cần lấy Đường sắt Ohitoyo làm tài sản thế chấp để vay một khoản tiền mới.」"
"1548" = "「À. Đúng là vậy nhỉ.\\n8620 có phân biệt trước sau, còn KiHa 07 thì có thể nói là hai mặt đều là phía trước.」"
"1549" = "「Aー……aー……a～～Ư」"
"1550" = "「A～～Ư」"
"1551" = "「Này này giám đốc chi nhánh Ohitoyo.\\nNói với chủ tịch mà lại dùng từ 'được không' sao.」"
"1554" = "「Vâng. À không, chuyện này,\\nlẽ ra tôi nên nói cho mọi người biết sớm hơn mới phải——」"
"1555" = "「Vâng. Tôi đã từ chối, bảo là không thể nhận lời được.」"
"1559" = "「Ừm. Cảm ơn chị.」"
"1569" = "「Hửm? Hình như tôi nghe nói Đường sắt Ohitoyo đang chịu lỗ mà.\\nCó thể xin được tiền trợ cấp từ thành phố sao?」"
"1571" = "「Hửm?\\nCái 'Xây mới đường tam giác ga Yunoi' này là sao?」"
"1599" = "「Nếu để chậm trễ việc trả nợ, anh sẽ đòi gắt gao đấy.\\nCho dù có anh ở giữa, thì trách nhiệm của Paulette vẫn không thay đổi đâu nhé?」"
"1637" = "「Đường sắt Ohitoyo đã thành lập bộ phận \\x%l保線;#00ffc040;bảo trì đường ray%l;#; rồi sao.\\nĐó là do ảnh hưởng từ sự cố hôm nọ à?」"
"1657" = "「Hôm nay, tôi đến không phải với tư cách là nhân viên xưởng rượu,\\nmà là để bàn bạc với tư cách Trưởng bộ phận \\x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohitoyo.」"
"1662" = "「Tôi sẽ dùng Navi làm tài sản thế chấp để vay 400 triệu từ Kisaki.\\nSau đó, với cùng điều kiện đó, tôi sẽ cho Đường sắt Ohitoyo vay lại.」"
"1671" = "「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,\\nngười ta mới đưa 8620 vào chạy tuyến Ohitoyo - Yunoi đấy ạ.」"
"1686" = "「Vì thế nên đương nhiên, toàn bộ chi phí liên quan đến \\x%l保線;#00ffc040;bảo trì đường ray%l;#;,\\nCông ty Cổ phần Đường sắt Ohitoyo dự định sẽ chi trả toàn bộ. Nhưng mà——」"
"1717" = "「Vâng, kể từ sau khi \\x%l帝鉄;#00ffc040;Teitetsu%l;#; giải thể, số tiền đó,\\nthành phố có vẻ đã giữ lại dưới dạng khoản thu không rõ người nhận.」"
"1731" = "「Việc bỏ mặc đường ray xuống cấp là lỗi của Đường sắt Ohitoyo mà!\\nTại sao anh hai lại phải làm đến mức đó chứ!?」"
"1735" = "「Vâng. Thẳng thắn mà nói thì,\\nlà do tôi đánh giá hệ thống \\x%l保線;#00ffc040;bảo trì đường ray%l;#; hiện tại của Đường sắt Ohitoyo vẫn chưa đủ tốt.」"
"1766" = "「Tại Ohitoyo, nơi có khu vực \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,\\nngân hàng chúng tôi cũng đánh giá cao tính công cộng của đường sắt.」"
"1797" = "「Anh Urakami, anh được phái cử đến đây,\\nlà để xây dựng nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; ở Ohitoyo đúng không?」"
"1805" = "「Khu vực rộng lớn quanh ga Yunoi đều là đất của Đường sắt Ohitoyo,\\nnên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」"
"1831" = "「Ohitoyo đã nhận được sự tiến cử từ điều phối viên địa phương,\\nnhư một ứng cử viên vô cùng tiềm năng. Nhưng mà.」"
"1832" = "「Đương nhiên rồi. Tôi sẽ dốc toàn lực để giúp đỡ.」"
"1834" = "「Tất nhiên, giả sử việc thu hút nhà máy bị cưỡng chế tiến hành, sông Kuma bị ô nhiễm,\\nthị trấn Ohitoyo bị tàn phá, thì tôi cũng chẳng chết được.」"
"1858" = "「Trong thời gian ngắn như vậy mà em đã đưa ra được bản dự toán này, làm tốt lắm.」"
"1874" = "「Nếu trong thời hạn đó có thể hủy bỏ việc thu hút nhà máy,\\ncha hứa sẽ kết thúc thời gian học việc và cho phép anh tự lập.」"
"1896" = "「Với số tiền đó, thì chỉ còn cách đi vay thôi.\\nVì vậy, việc dùng một phần cơ sở vật chất của Đường sắt Ohitoyo làm tài sản thế chấp thì.」"
"1928" = "「Không được.\\nĐể cho ngân hàng, thuộc phe ủng hộ nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\nnắm giữ huyết mạch của Đường sắt Ohitoyo - thành trì của phe phản đối thì.」"
"2152" = "“Tôi nhất định sẽ trả lại toàn bộ”\\nTôi định nói vậy, nhưng lại nuốt vào trong, không thốt ra thành lời."
"2402" = "Tôi không thể nào thốt nên lời.\\nNhững câu như 『Tôi không thể gây rắc rối như vậy được』."
"2404" = "Tôi kể lại. Không tô vẽ, không e dè.\\nRằng những cuộc gặp gỡ ở Ohitoyo đã giúp tôi trưởng thành."
"2488" = "Huống hồ, lại còn là người ngoài Ohitoyo,\\ncó lẽ đây là một đối tác đàm phán khó nhằn hơn cả Kisaki."
"2642" = "Chính vì vậy, tôi muốn bảo vệ Ohitoyo——\\nBảo vệ nguồn nước và con người của thị trấn này, không muốn chúng bị tổn hại."
"2674" = "Phòng giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto——\\nPhòng làm việc của Houshou Kisaki, rất rộng rãi và nhiều ánh sáng."
"2686" = "Chuyện đó là đương nhiên. \\x%l自弁;#00ffc040;Van hãm tự động%l;#; và \\x%l単弁;#00ffc040;van hãm đơn%l;#;——\\nChỉ cần tháo tay gạt \\x%lブレーキ;#00ffc040;phanh%l;#; ra rồi mang sang đầu kia là được."```

## Kết bài

File 14 (共通14_負債) audit xong: **52/411 dòng sai (12,7%)** — nặng thuật ngữ (32 dòng, trong đó Ohimitera 30 dòng đúng như dự báo) và đại từ Soutetsu (15 dòng, chủ yếu là "em" tự xưng không bao giờ đúng với cậu và "tôi" với Paulette/Hibiki cần thành "anh"). Không có lỗi cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 mồ côi, 0 chưa dịch, 0 key trùng. Sweep っ có 3 mục, cả 3 đúng và đã nhận. Lần đọc thứ hai: 52/52 tái xác nhận, 0 gỡ, 0 sửa. File này dọn sạch Ohimitera trong 00_Common 14; còn 23 dòng Ohimitera ở file 15 (15) và file 01 pilot (8 chưa xác nhận) — file 13 đã sửa hết 3 dòng của nó.
