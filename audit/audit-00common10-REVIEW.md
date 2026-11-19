# Audit 00_Common file 10 — 共通10_クマ川くだりで見る景色.txt.toml

**40/430 dòng sai (9,3%), 0 dòng chưa chắc chắn, 0 dòng lệch, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 23 | Ohimitera→Ohitoyo 13 (3356, 3254, 2708, 3296, 2486, 2276, 2778, 2801, 2813, 3404, 2352, 3129, 2510) + 2995 (mục gasp, cùng dòng sửa Ohitoyo) = 14 dòng Ohitoyo; 帝鉄→Teitetsu 3 (2508, 2767, 3092); 湯医→Yunoi 4 (2396, 2605, 2276, 2778 — 2 dòng sau chung với Ohitoyo); 帝大→"Đại học Đế quốc" 1 (2264); 運転体→"thân vận hành" 2 (3005, 3359); タブレット→"máy tính bảng" 1 (3376); 術仙→"Jutsu-sen" 1 (2771); 宮司→"đền chủ" 1 (3092, chung dòng với Teitetsu) |
| Đại từ | 11 | Soutetsu tự xưng "tôi"→"anh" với Fukami 1 (2779); Soutetsu "anh"→"tôi" với Hachiroku 3 (2475, 2479, 2656); Fukami "Chị nói"→"Anh nói" 1 (2221, đối tượng là Soutetsu); Nagi "bé Fukami"→"chị Fukami" 4 (2218, 2228, 2604, 2430) + Soutetsu trích lời Nagi 1 (2642); độc thoại "Anh"→"Tôi" 1 (3217) |
| Gasp (っ) | 3 | 2209, 2815, 2995 — cả 3 đều từ sweep, đã kiểm chứng đúng |
| Meaning | 2 | 3268 (VN bịa thêm "nghe những điều người ta" — JP không có 聞, không có "người ta"; kiểu bịa của Gemini), 2477 ("Chắc……là vậy rồi." dịch ngược sắc thái không chắc chắn của どう……だろうな) |
| SFX | 1 | 2369 はぅ→"Hau" (tiếng bối rối, không phải đồng ý "Vâng") |
| **Tổng** | **41** | |

Thoại 28/270 sai (10,4%), độc thoại 12/160 sai (7,5%). Theo nhân vật: monologue 12, 双鉄 11, ふかみ 6, ハチロク 5, 凪 4, 稀咲 2.

## 2. Phương pháp và độ tin cậy của nguồn

- Nguồn: CSV3 bộ duy nhất 00_Common (430 dòng); TOML-2 `共通10_クマ川くだりで見る景色.txt.toml`, md5 `a36943d7a08e0c9705401e3b771db961`, 86.402 byte, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng (không thuộc 11 nhóm trùng).
- So sánh CSV↔TOML: 177 dòng khớp tuyệt đối + 253 dòng khớp sau khi gộp ký tự xuống dòng, **0 khác biệt** — nguồn sạch, CSV3 là bản tin cậy cho fix list.
- Sweep っ: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **3 mục** (2209 raw-tsu, 2815 lost-gasp-whole, 2995 raw-tsu). Cả 3 giá trị đã kiểm chứng đúng với JP và được nhận nguyên văn (2209, 2815); 2995 nhận giá trị gasp của sweep + sửa thêm Ohitoyo trong cùng dòng. Không có gasp nào sweep bỏ sót trong file này.
- Nhiễm chéo: tra toàn bộ chỉ mục VN của dự án — 16 lần trùng, tất cả đều là các câu ngắn thông dụng được dịch độc lập giống nhau ("Xin lỗi vì đã để quý khách phải đợi", "Đúng vậy", v.v.); 2 lần lặp hợp lệ có JP giống hệt nhau (2578, 3294). Không có nhiễm chéo.
- Kiểm tra chuỗi xoay trước khi dịch mới: không có dòng lệch nào, nên không cần dịch mới dòng nào.
- Quy tắc áp dụng: Ohitoyo / Teitetsu / Yunoi / "chủ tàu" / "tàu điện thành phố" / "thân bảo trì" / "thân vận hành" / KiHa / "đền chủ" / Migita Ichi / "vé lượt" / Railord / Olivy; quy tắc đại từ Soutetsu đã sửa ("anh" với Hibiki/Michiko/Paulette/Reina, "tôi" với Hachiroku/Mayami/Nagi/Minokasa); khóa B4 (双鉄くん→"anh Soutetsu", không có ngoại lệ rên); quy tắc ngẫu hứng 22:05 (SFX theo nhân vật + ngữ cảnh, không dập khuôn; tiếng cười không bao giờ thành tiếng rên); công thức độ dài nguyên âm (số nguyên âm VN = 1 + số う/ぅ trong JP); JP thắng TW khi xung đột; cảnh giác bịa của Gemini (từ bịa không có cơ sở JP, tag %l tự thêm, hoàn thiện câu JP bị cắt cụt).

## 3. Các lỗi đã sửa (41 dòng)

### 2209 — 稀咲 — gasp

**JP:** 「『損得の話じゃない』なんてまるきり妄言じゃないか。⏎得がなければ、この神社だって維持できまい――っ！」

**TW:** 「什麼“不是利益的問題”，完全就是胡話嘛。若沒有利益，就連這座神社都無法維持下去！」

**VN cũ:** 「Cái gì mà 『Không phải chuyện lợi ích』 chứ, toàn là nói xằng nói bậy. Nếu không có lợi ích, thì ngay cả ngôi đền này cũng chẳng duy trì nổi đâu――っ!」

**Fix:** 「Cái gì mà 『Không phải chuyện lợi ích』 chứ, toàn là nói xằng nói bậy. Nếu không có lợi ích, thì ngay cả ngôi đền này cũng chẳng duy trì nổi đâu――Ư!」

Sweep raw-tsu: JP kết bằng ――っ! (gasp cuối câu), VN cũ để nguyên ký tự っ. Áp nguyên văn giá trị sweep (đã kiểm chứng đúng JP).

### 2218 — 凪 — pronoun

**JP:** 「水くさかとよ、ふかみちゃん。⏎困った時はお互いさまばいっ！」

**TW:** 「你太見外啦，小深。遇到困難就要互相幫助咧！」

**VN cũ:** 「Khách sáo quá nha, bé Fukami.⏎Lúc khó khăn thì phải giúp đỡ lẫn nhau chứ nha!」

**Fix:** 「Khách sáo quá nha, chị Fukami.⏎Lúc khó khăn thì phải giúp đỡ lẫn nhau chứ nha!」

Nagi (nhỏ tuổi hơn, năm thứ hai, vóc nhỏ) gọi Fukami (lớn tuổi hơn, cao lớn, đại diện chủ bến, làm từ nhỏ) — "bé" ngược vai vế. Fukami gọi Nagi là "bé Nagi" + tự xưng "chị" (2415), nên chiều ngược lại Nagi gọi Fukami là "chị". Tiền lệ file 07: Hikari 4 tuổi tự xưng "chị" bị sửa — dự án coi trọng đúng hướng tuổi tác.

### 2221 — ふかみ — pronoun

**JP:** 「凪ちゃんのこと？」

**TW:** 「你是指小凪嗎？」

**VN cũ:** 「Chị nói bé Nagi sao?」

**Fix:** 「Anh nói bé Nagi sao?」

Fukami đang hỏi Soutetsu (người vừa khuyên ở 2217; Nagi chen vào ở 2218; Fukami hỏi lại "凪ちゃんのこと?" — "Anh nói bé Nagi sao?"). Người duy nhất Fukami gọi "chị" là Hachiroku, mà Hachiroku không nói gì liên quan ở đây. "Chị" không có đối tượng đúng.

### 2228 — 凪 — pronoun

**JP:** 「クマ川くだりはお客さんが減りすぎて、船頭さん達が⏎やめてっちゃったって、ふかみちゃん困っとったばい」

**TW:** 「來隈河漂流的客人銳減，好多掌棹人都不做了，小深為此傷透了腦筋咧」

**VN cũ:** 「Khách đi thuyền trên sông Kuma giảm đi nhiều quá, các bác cầm lái⏎nghỉ việc hết trơn, bé Fukami đang gặp khó khăn lắm nha.」

**Fix:** 「Khách đi thuyền trên sông Kuma giảm đi nhiều quá, các bác cầm lái⏎nghỉ việc hết trơn, chị Fukami đang gặp khó khăn lắm nha.」

Như 2218: Nagi gọi Fukami — "chị" mới đúng hướng tuổi tác.

### 2264 — 稀咲 — terminology

**JP:** 「帝大生ということも、家業をお手伝いされてることも⏎――と、そうだ」

**TW:** 「包括您就讀於帝大，以及在幫忙打理家業——哦，對了」

**VN cũ:** 「Chuyện anh là sinh viên Đại học Hoàng gia, chuyện anh đang giúp đỡ công việc gia đình⏎――À, phải rồi.」

**Fix:** 「Chuyện anh là sinh viên Đại học Đế quốc, chuyện anh đang giúp đỡ công việc gia đình⏎――À, phải rồi.」

帝大 = 帝国大学 (Đại học Đế quốc). "Hoàng gia" là cùng kiểu dịch sai như 帝鉄→"Đường sắt Hoàng gia" đã bị bãi bỏ 19/11 (帝 = Đế, không phải Hoàng gia); đối chiếu 2543 帝都→"Đế đô" trong cùng file.

### 2276 — 双鉄 — terminology

**JP:** 「なるほど。湯医-御一夜間なら」

**TW:** 「原來如此。若是要在湯醫至御一夜之間往返的話」

**VN cũ:** 「Ra là vậy. Nếu là đoạn giữa Yui và Ohimitera thì.」

**Fix:** 「Ra là vậy. Nếu là đoạn giữa Yunoi và Ohitoyo thì.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera". (Lần 2 bắt được: bản thảo chỉ sửa Ohimitera, quên Yui→Yunoi trong cùng dòng.)

### 2352 — 双鉄 — terminology

**JP:** 「ああ――それはもちろん。いやそういう点で、⏎御一夜を田舎扱いして驚いたのではなくて」

**TW:** 「啊——那是當然。不過我並沒有把御一夜當成鄉下而驚訝於這裡居然存在學生任職」

**VN cũ:** 「À――chuyện đó thì tất nhiên. Không, không phải tôi ngạc nhiên vì coi Ohimitera là vùng quê ở điểm đó.」

**Fix:** 「À――chuyện đó thì tất nhiên. Không, không phải tôi ngạc nhiên vì coi Ohitoyo là vùng quê ở điểm đó.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2369 — ふかみ — sfx

**JP:** 「う……はぅ……」

**TW:** 「嗚……好……」

**VN cũ:** 「Ư…… Vâng……」

**Fix:** 「Ư…… Hau……」

はぅ là tiếng thốt bối rối, không phải lời đồng ý. VN cũ dịch thành "Vâng" (= đồng ý) là sai nghĩa — câu hỏi 2490 ("Gọi là bé Fukami — được không nhỉ?") chưa được trả lời đồng ý ở đây. Tiền lệ h7/h8: はうっ→"Hau" (giữ âm Nhật, không diễn thành lời). Công thức độ dài nguyên âm: はぅ có 1 ぅ → "Hau" có 2 nguyên âm (a+u), khớp.

### 2396 — ふかみ — terminology

**JP:** 「発船所――[ゆのい,1]湯医にもあるから。⏎もっと上流からの、もっと急流のヤツ」

**TW:** 「在湯醫——也有一個發船點。在更加上游的地方，水流更湍急」

**VN cũ:** 「Bến thuyền――ở Yui cũng có ạ.⏎Ở đoạn thượng nguồn xa hơn, nước chảy xiết hơn.」

**Fix:** 「Bến thuyền――ở Yunoi cũng có ạ.⏎Ở đoạn thượng nguồn xa hơn, nước chảy xiết hơn.」

Quyết định 19/11: 湯医/湯医線 = "Yunoi" (furigana ゆのい ghi ngay trong JP dòng này: [ゆのい,1]湯医).

### 2430 — 凪 — pronoun

**JP:** 「ふかみちゃーーん！」

**TW:** 「小深——！」

**VN cũ:** 「Bé Fukami ơiii!」

**Fix:** 「Chị Fukami ơiii!」

Như 2218: Nagi gọi Fukami — "chị".

### 2475 — 双鉄 — pronoun

**JP:** 「僕は――」

**TW:** 「我——」

**VN cũ:** 「Anh――」

**Fix:** 「Tôi――」

Soutetsu đang nói với Hachiroku (cảnh ma/quỷ: 1863, 2804, 2784, 2626 đều là Hachiroku; 2479 tiếp nối cùng cảnh). Quy tắc: "tôi" với Hachiroku.

### 2477 — 双鉄 — meaning

**JP:** 「どう……だろうな」

**TW:** 「我……不確定」

**VN cũ:** 「Chắc……là vậy rồi.」

**Fix:** 「Sao…… nhỉ.」

JP 「どう……だろうな」 = "Sao nhỉ / Không biết nữa" (do dự, không chắc). VN cũ "Chắc là vậy rồi" khẳng định quá mạnh, mâu thuẫn với độc thoại ngay sau (3226: "Không thể trả lời. Ngay cả bản thân tôi cũng không hiểu."). TW cũng là 不確定 (không chắc).

### 2479 — 双鉄 — pronoun

**JP:** 「幽霊も鬼も恐れはしない。⏎現実は常に、そうしたものを駆逐するから」

**TW:** 「我不害怕鬼怪幽靈。因為現實總會將它們排除在外」

**VN cũ:** 「Anh không sợ ma hay quỷ.⏎Vì thực tế luôn xua đuổi những thứ đó.」

**Fix:** 「Tôi không sợ ma hay quỷ.⏎Vì thực tế luôn xua đuổi những thứ đó.」

Soutetsu trả lời Hachiroku (2626 cô ấy hỏi "Thực tế mới là điều ngài e sợ nhất sao?"). Quy tắc: "tôi" với Hachiroku.

### 2486 — 双鉄 — terminology

**JP:** 「ひとまずは、御一夜の駅まで戻ろうと思うが」

**TW:** 「我們打算先回御一夜的車站」

**VN cũ:** 「Trước mắt, bọn anh định quay lại ga Ohimitera.」

**Fix:** 「Trước mắt, bọn anh định quay lại ga Ohitoyo.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2508 — ハチロク — terminology

**JP:** 「双鉄様からご紹介にあずかりました、旧\x%l帝鉄;#00ffc040;帝鉄%l;\x%l8620;#;#00ffc040;8620%l;#;形⏎\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;、\x%l8620;#00ffc040;8620%l;#;専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、ハチロクです」

**TW:** 「我是剛才承蒙雙鐵少爺介紹的，前\x%l帝鉄;#00ffc040;帝國鐵路%l;\x%l8620;#;#00ffc040;８６２０%l;#;型\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;、\x%l8620;#00ffc040;８６２０%l;#;專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，八六」

**VN cũ:** 「Em là Hachiroku, \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; \x%l8620;#00ffc040;8620%l;#;,⏎thuộc dòng \x%l8620;#00ffc040;8620%l;#; của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ, như ngài Soutetsu vừa giới thiệu ạ.」

**Fix:** 「Em là Hachiroku, \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; \x%l8620;#00ffc040;8620%l;#;,⏎thuộc dòng \x%l8620;#00ffc040;8620%l;#; của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ, như ngài Soutetsu vừa giới thiệu ạ.」

Quyết định 19/11: 帝鉄 = "Teitetsu" (viết tắt của 帝国鉄道 = Đường sắt Đế quốc, không phải "Hoàng gia"). Chỉ sửa gloss trong thẻ %l, giữ nguyên cấu trúc thẻ. Lưu ý: JP ở dòng này có thẻ dị dạng (đóng %l; thiếu dấu ; cuối + thừa \x%l8620;#;) — VN đã chuẩn hóa thành thẻ thường từ trước, không sửa thêm.

### 2510 — 双鉄 — terminology

**JP:** 「工場誘致を撤回させようと御一夜に戻ってきた者だ。⏎せっかくなので、少し話をさせてもらえるかな？」

**TW:** 「我是為了阻止工廠落戶而回到御一夜的。這次機會難得，我們可以談談嗎？」

**VN cũ:** 「Tôi là người trở về Ohimitera để yêu cầu hủy bỏ việc thu hút nhà máy.⏎Nhân cơ hội này, chúng ta có thể nói chuyện một chút được không?」

**Fix:** 「Tôi là người trở về Ohitoyo để yêu cầu hủy bỏ việc thu hút nhà máy.⏎Nhân cơ hội này, chúng ta có thể nói chuyện một chút được không?」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2604 — 凪 — pronoun

**JP:** 「そうばい！　このにーさんらは、うちたちの味方ばい！⏎じゃっけーん、ふかみちゃんとこ、連れてきたばいっ！」

**TW:** 「沒錯咧！大哥哥他們是跟咱們同一個陣營的！所以咱把他們帶來見小深咧！」

**VN cũ:** 「Đúng nha! Mấy anh chị này là đồng minh của chúng ta nha!⏎Thế nên, em mới dẫn đến chỗ bé Fukami nha!」

**Fix:** 「Đúng nha! Mấy anh chị này là đồng minh của chúng ta nha!⏎Thế nên, em mới dẫn đến chỗ chị Fukami nha!」

Như 2218: Nagi nói về Fukami — "chị".

### 2605 — ふかみ — terminology

**JP:** 「そう。だからトラック。です。⏎今は、湯医の発船場、人が足りなくて使ってないけど」

**TW:** 「沒錯，所以要用到卡車。雖然現在湯醫發船點，因人手不夠而不再使用了」

**VN cũ:** 「Đúng vậy. Thế nên mới cần xe tải. Ạ.⏎Bây giờ bến thuyền ở Yui thiếu người nên không dùng nữa.」

**Fix:** 「Đúng vậy. Thế nên mới cần xe tải. Ạ.⏎Bây giờ bến thuyền ở Yunoi thiếu người nên không dùng nữa.」

Quyết định 19/11: 湯医 = "Yunoi".


### 2642 — 双鉄 — pronoun

**JP:** 「見事な手際だったな。⏎凪が、『ふかみちゃんは小さな頃から』と言っていたが」

**TW:** 「真是叫人讚嘆的技術啊。聽凪說，“小深是從小開始做的”」

**VN cũ:** 「Tay nghề điêu luyện thật đấy.⏎Nagi có nói là 『bé Fukami làm từ hồi nhỏ』 nhỉ.」

**Fix:** 「Tay nghề điêu luyện thật đấy.⏎Nagi có nói là 『chị Fukami làm từ hồi nhỏ』 nhỉ.」

Soutetsu trích lời Nagi ("Nagi có nói là…") nên dùng đúng cách gọi của Nagi: "chị Fukami".

### 2656 — 双鉄 — pronoun

**JP:** 「確かにな。澄み切っている感じを受ける。⏎ここは、昔も今も変わらず」

**TW:** 「確實啊。這裡給人一種無比清新的感覺。無論過去還是現在，這裡都沒有改變」

**VN cũ:** 「Đúng vậy. Anh cũng cảm thấy rất trong lành.⏎Nơi này, xưa nay vẫn không hề thay đổi.」

**Fix:** 「Đúng vậy. Tôi cũng cảm thấy rất trong lành.⏎Nơi này, xưa nay vẫn không hề thay đổi.」

Soutetsu đáp lại Hachiroku 2640 ("ngôi đền rất đẹp ạ") — "cũng" nối tiếp lời cô ấy; Fukami không có mặt ở đền. Quy tắc: "tôi" với Hachiroku.

### 2708 — ふかみ — terminology

**JP:** 「おまたせいたしました。御一夜クマ川くだり発船所、⏎受付の早瀬でございます」

**TW:** 「讓您久等了。這裡是御一夜隈河漂流發船點，我是櫃臺接待早瀨」

**VN cũ:** 「Xin lỗi vì đã để quý khách phải đợi. Đây là bến thuyền xuôi dòng Kuma Ohimitera,⏎nhân viên tiếp tân Hayase xin nghe.」

**Fix:** 「Xin lỗi vì đã để quý khách phải đợi. Đây là bến thuyền xuôi dòng Kuma Ohitoyo,⏎nhân viên tiếp tân Hayase xin nghe.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2767 — ふかみ — terminology

**JP:** 「だったら、丁度いい――⏎えっと、\x%l帝鉄;#00ffc040;帝鉄%l;#;？　とかいうので働いてたっていう人が」

**TW:** 「那正好，有一位曾經在那個……\x%l帝鉄;#00ffc040;帝國鐵路%l;#;？曾經在那裡工作的人」

**VN cũ:** 「Vậy thì, vừa hay――⏎Ưm, có một người từng làm việc ở \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;? hay gì đó ạ.」

**Fix:** 「Vậy thì, vừa hay――⏎Ưm, có một người từng làm việc ở \x%l帝鉄;#00ffc040;Teitetsu%l;#;? hay gì đó ạ.」

Quyết định 19/11: 帝鉄 = "Teitetsu".

### 2771 — ハチロク — terminology

**JP:** 「[じゅつせんはいたんこう,4]術仙廃炭鉱でしたか。あの近く――⏎\x%lエアクラ;#00ffc040;エアクラ%l;#;が使えなくなる場所を通るのですね？」

**TW:** 「那裡有術仙廢煤礦呀。是為了通過那一段\x%lエアクラ;#00ffc040;空凝機%l;#;無法使用的道路對吧？」

**VN cũ:** 「Mỏ than bỏ hoang Jussen phải không ạ. Gần đó――⏎là đi qua khu vực không thể sử dụng \x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」

**Fix:** 「Mỏ than bỏ hoang Jutsu-sen phải không ạ. Gần đó――⏎là đi qua khu vực không thể sử dụng \x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」

Quyết định 19/11: 術仙 = "Jutsu-sen" (tiền lệ Grand 04 sửa 4× "Jussen"). Ruby JP [じゅつせんはいたんこう,4] xác nhận đọc "jutsen".

### 2778 — 双鉄 — terminology

**JP:** 「ならば、ともに頑張ろう。⏎御一夜の観光復権で、湯医発船場も復活だ」

**TW:** 「那麼，就讓我們一起努力吧。通過御一夜的旅遊業復興，讓湯醫發船點的生意也興隆起來」

**VN cũ:** 「Nếu vậy, chúng ta cùng cố gắng nhé.⏎Phục hưng du lịch Ohimitera, cũng là hồi sinh bến thuyền Yui.」

**Fix:** 「Nếu vậy, chúng ta cùng cố gắng nhé.⏎Phục hưng du lịch Ohitoyo, cũng là hồi sinh bến thuyền Yunoi.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera". (Lần 2 bắt được: bản thảo chỉ sửa Ohimitera, quên Yui→Yunoi trong cùng dòng.)

### 2779 — 双鉄 — pronoun

**JP:** 「ならば、僕とハチロクにクマ川下りを経験させてくれ。⏎料金は、無論、大人二人分を払う」

**TW:** 「那麼，就讓我和八六體驗一回隈河漂流吧。當然，我們會按兩名成人的價格付款」

**VN cũ:** 「Nếu vậy, hãy cho tôi và Hachiroku trải nghiệm đi thuyền xuôi dòng Kuma đi.⏎Đương nhiên là tôi sẽ trả tiền vé cho hai người lớn.」

**Fix:** 「Nếu vậy, hãy cho anh và Hachiroku trải nghiệm đi thuyền xuôi dòng Kuma đi.⏎Đương nhiên là anh sẽ trả tiền vé cho hai người lớn.」

Soutetsu nói với Fukami: Fukami gọi Soutetsu là "anh Soutetsu" (双鉄おにいさん, key 2706; docs pronouns_detail.md cũng ghi "Anh Soutetsu"). Trong file Soutetsu xưng "anh" với Fukami 12 dòng (1881, 2520, 2573, 2629, 2781, 2375, 2486, 2782, 2656→sửa, 2475/2479→sửa, 1868); dòng 2779 dùng "tôi" là lạc nhịp duy nhất. Sửa cả 2 chỗ "tôi" trong dòng.

### 2801 — ハチロク — terminology

**JP:** 「御一夜は、水の匂いのする町ですが……⏎ここの空気は、ひときわ澄み切っているようです」

**TW:** 「雖然御一夜是一座飄蕩著水香的城市……但這裡的空氣似乎更加的清新無比」

**VN cũ:** 「Ohimitera là một thị trấn thoang thoảng mùi nước……⏎Nhưng không khí ở đây dường như lại trong lành hơn hẳn.」

**Fix:** 「Ohitoyo là một thị trấn thoang thoảng mùi nước……⏎Nhưng không khí ở đây dường như lại trong lành hơn hẳn.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2813 — ハチロク — terminology

**JP:** 「鬼に、幽霊。⏎御一夜は、意外と恐ろしい土地なのですね」

**TW:** 「鬼還有幽靈。沒想到御一夜還有些可怕呀」

**VN cũ:** 「Quỷ, rồi lại ma.⏎Ohimitera là một vùng đất đáng sợ ngoài sức tưởng tượng nhỉ.」

**Fix:** 「Quỷ, rồi lại ma.⏎Ohitoyo là một vùng đất đáng sợ ngoài sức tưởng tượng nhỉ.」

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 2815 — ハチロク — gasp

**JP:** 「っ！？」

**TW:** 「！？」

**VN cũ:** 「!?」

**Fix:** 「Ư!?」

Sweep lost-gasp-whole: JP 「っ！？」 là cả dòng chỉ có gasp, VN cũ chỉ còn "!?". Áp nguyên văn giá trị sweep.

### 2995 — monologue — gasp

**JP:** 念のため、名刺を受け取り仔細に見れば、そこにはやはり、⏎『隈元銀行　御一夜支店長』の文字列――っ！？

**TW:** 以防萬一我仔細查看了收下的名片，在那裡果然寫著“隈元銀行·御一夜支行行長”一行字——！？

**VN cũ:** Để chắc chắn, tôi nhận lấy tấm danh thiếp và nhìn kỹ, quả nhiên trên đó ghi,⏎『Giám đốc chi nhánh Ohimitera, Ngân hàng Kumamoto』――っ!?

**Fix:** Để chắc chắn, tôi nhận lấy tấm danh thiếp và nhìn kỹ, quả nhiên trên đó ghi,⏎『Giám đốc chi nhánh Ohitoyo, Ngân hàng Kumamoto』――Ư!?

Sweep raw-tsu: JP kết bằng ――っ！？, VN cũ để nguyên っ. Áp giá trị sweep + sửa Ohimitera→Ohitoyo trong cùng dòng (tên trên danh thiếp).

### 3005 — monologue — terminology

**JP:** ハチロクの依頼どおり、\x%l乗務鞄;#00ffc040;乗務鞄%l;#;は肌身離さず扱っている。⏎中にはもちろん、\x%l運転体;#00ffc040;運転体%l;#;だ。

**TW:** 依照八六的要求，我隨身攜帶著\x%l乗務鞄;#00ffc040;乘務包%l;#;。裡面裝著的自然是\x%l運転体;#00ffc040;駕駛體%l;#;。

**VN cũ:** Theo lời nhờ vả của Hachiroku, tôi luôn giữ \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; khư khư bên mình.⏎Bên trong tất nhiên là \x%l運転体;#00ffc040;kíp lái%l;#; rồi.

**Fix:** Theo lời nhờ vả của Hachiroku, tôi luôn giữ \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; khư khư bên mình.⏎Bên trong tất nhiên là \x%l運転体;#00ffc040;thân vận hành%l;#; rồi.

Quyết định 19/11: 運転体 = "thân vận hành" (là thân thể/bộ phận, không phải kíp người — tiền lệ file 08 sửa 5 dòng). Gloss 乗務鞄 "túi phi hành đoàn" GIỮ NGUYÊN chờ Hieu chốt ở đợt thống nhất (tiền lệ file 08).

### 3092 — monologue — terminology

**JP:** ふかみが僕に教えてくれた、旧\x%l帝鉄;#00ffc040;帝鉄%l;#;の元職員――⏎赤井神社の宮司に会うため。

**TW:** 去見深美介紹的那位前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;原職員——赤井神社的宮司。

**VN cũ:** Để gặp cựu nhân viên của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ mà Fukami đã cho tôi biết――⏎Cung tư tế của đền Akai.

**Fix:** Để gặp cựu nhân viên của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ mà Fukami đã cho tôi biết――⏎Đền chủ của đền Akai.

Quyết định 19/11: 帝鉄 = "Teitetsu"; 宮司 = "đền chủ" (không dùng "Cung tư tế"). Hai sửa trong một dòng.

### 3129 — monologue — terminology

**JP:** 頷いて――その瞬間にそうかと気付く。⏎『隈元銀行御一夜支店』の、支店長。

**TW:** 在點頭的瞬間，我突然想起來。“隈元銀行御一夜支行”的支行長。

**VN cũ:** Gật đầu――và ngay khoảnh khắc đó tôi chợt nhận ra.⏎Giám đốc chi nhánh của 『Ngân hàng Kumamoto chi nhánh Ohimitera』.

**Fix:** Gật đầu――và ngay khoảnh khắc đó tôi chợt nhận ra.⏎Giám đốc chi nhánh của 『Ngân hàng Kumamoto chi nhánh Ohitoyo』.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 3217 — monologue — pronoun

**JP:** お参りをした。⏎汰斗さんと、日々姫と真闇姉とに連れられて。

**TW:** 我曾經在汰斗老爺、日日姬與真闇姐的帶領下來這裡參拜過。

**VN cũ:** Anh từng đến đây viếng đền rồi.⏎Được ông Taito, Hibiki và chị Mayami dẫn đi.

**Fix:** Tôi từng đến đây viếng đền rồi.⏎Được ông Taito, Hibiki và chị Mayami dẫn đi.

Độc thoại (không có 「」): Soutetsu tự thuật — "anh" trong độc thoại là sai (ngoại lệ h3 1683 chỉ cho phép "mình" trong độc thoại nội tâm tự vấn cảm xúc; "anh" không bao giờ đúng ở độc thoại).

### 3254 — monologue — terminology

**JP:** 蓑笠老人がおっしゃってくださったように、⏎御一夜における観光の実態を学ぶことこそが最優先だ。

**TW:** 正如蓑笠老人所說的那樣，現在最要緊的是了解御一夜旅遊業的實際情況。

**VN cũ:** Như lời ông lão Minokasa đã nói,⏎việc tìm hiểu thực trạng du lịch ở Ohimitera mới là ưu tiên hàng đầu.

**Fix:** Như lời ông lão Minokasa đã nói,⏎việc tìm hiểu thực trạng du lịch ở Ohitoyo mới là ưu tiên hàng đầu.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 3268 — monologue — meaning

**JP:** 川の顔だの表情だのを、まるで考えたこともないが、⏎毎日見ているものには、少し興味が湧いてくる。

**TW:** 河川的面容與表情，我雖然之前從來都沒有想過，此刻卻對這些每天都見到的景色產生了些許興趣。

**VN cũ:** Chưa bao giờ tôi nghĩ về khuôn mặt hay biểu cảm của dòng sông,⏎nhưng nghe những điều người ta thấy hàng ngày, tôi bỗng thấy hơi tò mò.

**Fix:** Chưa bao giờ tôi nghĩ về khuôn mặt hay biểu cảm của dòng sông,⏎nhưng thứ mà tôi nhìn thấy mỗi ngày khiến tôi bỗng thấy hơi tò mò.

Bịa thêm nghĩa (kiểu Gemini): JP 毎日見ているものには、少し興味が湧いてくる = "thứ tôi nhìn thấy mỗi ngày khiến tôi hơi tò mò" — không có "nghe" (聞) và không có "người ta" trong JP. VN cũ tự thêm cả hai. (Lần 2: bỏ "lại" thừa trong bản thảo fix.)

### 3296 — monologue — terminology

**JP:** ふかみは、深みを持っている。⏎引き出せたなら、恐らくは、御一夜を支える力になる。

**TW:** 深美，很有深度。若能將其發掘出來，或許，她能成為支撐御一夜的力量。

**VN cũ:** Fukami có chiều sâu.⏎Nếu có thể khơi gợi nó ra, có lẽ cô bé sẽ trở thành sức mạnh chống đỡ cho Ohimitera.

**Fix:** Fukami có chiều sâu.⏎Nếu có thể khơi gợi nó ra, có lẽ cô bé sẽ trở thành sức mạnh chống đỡ cho Ohitoyo.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 3356 — monologue — terminology

**JP:** そうしてここは、御一夜有数の観光スポット。⏎だというのに……まるで人の気配がない。

**TW:** 而這裡是御一夜為數不多的觀光景點，可是……卻空無一人。

**VN cũ:** Vậy mà nơi đây, một trong những địa điểm du lịch nổi tiếng của Ohimitera.⏎Lại vắng tanh vắng ngắt... chẳng có lấy một bóng người.

**Fix:** Vậy mà nơi đây, một trong những địa điểm du lịch nổi tiếng của Ohitoyo.⏎Lại vắng tanh vắng ngắt... chẳng có lấy một bóng người.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

### 3359 — monologue — terminology

**JP:** \x%l運転体;#00ffc040;運転体%l;#;のときと変わらず僕のヒザに乗るハチロクも、⏎そのまま動きにつられ、揺られる。

**TW:** 與使用\x%l運転体;#00ffc040;駕駛體%l;#;時一樣坐在我膝蓋上的八六，也被我的轉身帶動，搖晃了一下。

**VN cũ:** Hachiroku vẫn ngồi trên đùi tôi y như lúc dùng \x%l運転体;#00ffc040;kíp lái%l;#;,⏎cũng bị chuyển động đó làm cho đung đưa theo.

**Fix:** Hachiroku vẫn ngồi trên đùi tôi y như lúc dùng \x%l運転体;#00ffc040;thân vận hành%l;#;,⏎cũng bị chuyển động đó làm cho đung đưa theo.

Quyết định 19/11: 運転体 = "thân vận hành".

### 3376 — monologue — terminology

**JP:** \x%lタブレット;#00ffc040;タブレット%l;#;を換装すればジュニアサイズも大きくなるが⏎さてその場合、救命胴衣はどう扱われる――おや。

**TW:** 若將\x%lタブレット;#00ffc040;操作板%l;#;更換到駕駛體的話，就連兒童救生衣都會顯得太大。那樣的話，不知該穿什麼尺碼的救生衣——哦？

**VN cũ:** Nếu đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#; thì size trẻ em cũng sẽ thành to thôi,⏎nhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa.

**Fix:** Nếu đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#; thì size trẻ em cũng sẽ thành to thôi,⏎nhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa.

Quyết định: タブレット = "máy tính bảng" (tiền lệ file 04/08).

### 3404 — monologue — terminology

**JP:** 御一夜に銀行といえば、ひとつしかない。

**TW:** 說到御一夜的銀行，就只有一間了。

**VN cũ:** Nói đến ngân hàng ở Ohimitera, thì chỉ có một.

**Fix:** Nói đến ngân hàng ở Ohitoyo, thì chỉ có một.

Quyết định 19/11: 御一夜 = "Ohitoyo", không dùng "Ohimitera".

## 4. Các dòng giữ nguyên có chủ đích / phán đoán

- **2616 — ĐÃ QUYẾT BỞI PARENT (20/11, theo ủy quyền của Hieu):** Hachiroku giữ "Chị nghĩ" với Fukami — KHÔNG sửa. Fukami gọi cô ấy là "Chị Hachiroku" (2706), và theo logic đối ứng đã khóa ở B4 (Paulette gọi "anh Soutetsu" → Soutetsu là "anh" với Paulette) thì Hachiroku là "chị" với Fukami. Tiền đề của audit ("em" 2× với Fukami) là sai một nửa: 2483 nói với Soutetsu ("Em cũng vậy" đồng tình với 2479 của Soutetsu) nên "em" ở đó là đúng; 2597 (nói về/cảm ơn Fukami-sama, người nghe chưa rõ) giữ nguyên "em", ghi lại cho Hieu nếu muốn xem xét. Fix "Chị"→"Em" ở 2616 đã bị parent loại khỏi fix list.
- **2779 (xưng "anh" với Fukami là đúng):** Fukami gọi Soutetsu là 「双鉄おにいさん" (2706), và trong file Soutetsu có 12 dòng xưng "anh" với Fukami — 2779 là dòng lẻ duy nhất xưng "tôi".
- **2475/2479/2656 ("tôi" với Hachiroku):** 2656 trả lời trực tiếp Hachiroku 2640; 2475/2479 nằm trong cảnh ma/quỷ chỉ có Soutetsu + Hachiroku đối thoại (xác minh từ các dòng kề).
- **3005 乗務鞄 "túi phi hành đoàn":** GIỮ NGUYÊN chờ quyết định của Hieu ở lần thống nhất (đa số dự án 11 vs "cặp lái tàu" 3; "phi hành đoàn" là thuật ngữ hàng không, sai lĩnh vực đường sắt — nhưng trong file này nhất quán 4/4; chỉ sửa 運転体 trong cùng dòng).
- **2573 "bố nuôi"/"mẹ nuôi" là ĐÚNG, không phải lỗi bịa:** JP 義父/義母, TW 養父/養母 (cha mẹ nuôi), ngữ cảnh là con nuôi — khác hẳn mẫu bịa 義→"nuôi" ở file 06 (2740 義妹→"em gái nuôi" trong khi JP/TW không có ngữ cảnh nhận nuôi).
- **2388 hai câu hô giống nhau là đúng:** JP hai dòng đều là 「ヨイサノサノ」 (cùng một câu hô), TW khác nhau chỉ là cách dịch thoáng; っ nhấn mạnh ở dòng thứ hai được bỏ đúng quy tắc (っ nhấn mạnh cuối câu gắn vào từ không phải gasp).
- **2682 "cô ta" giữ nguyên:** chỉ một bà lão hư cấu trong lời kể của Soutetsu; không có đối tượng nữ trẻ nào khác trong cảnh.
- **2307 "Pyawa" giữ nguyên:** ひゃっ→"Hya" theo tiền lệ đã chốt (lr_h1 1005 "Hia" cho ひあっ, h4 ひゃ→"Hya"); "Pyawa" là cách Việt hóa hợp âm ぴゃわ, không phải romanisation thô.
- **2493/2707 tự giới thiệu trang trọng giữ nguyên:** cả hai đều là lời giới thiệu chính thức ("Tôi là…"), đúng với ngữ cảnh; Soutetsu xưng "tôi" với người lạ là chuẩn.
- **2633 "Chúng tôi" giữ nguyên:** Soutetsu nói thay cho cả nhóm (số nhiều), không phải tự xưng số ít.
- **2502/2554 っ nhấn mạnh được bỏ đúng:** っ cuối câu gắn vào từ (行くのっ, んだっ) là nhấn mạnh, không phải gasp — đúng quy tắc sweep.
- **3325/3326 hai dòng khác nhau, giữ nguyên:** JP 3325 là ハチロクのポケット (túi của Hachiroku), 3326 là túi áo của Soutetsu — hai dòng riêng biệt, không phải trùng lặp.
- **1873 VN==TW chỉ là dấu ba chấm:** JP 「え？" chỉ có 「え？"; cả TW và VN đều thêm "……" — không phải lỗi dịch, không đếm.

## 5. Dị thường dữ liệu (không phải lỗi VN)

- **JP 2508 có tag dị dạng** (cùng mẫu với file 09 key 2482): tag mở 5 / đóng 4 — tag 帝鉄 đóng bằng `%l;` thiếu dấu `;` cuối và thừa `\x%l8620;#;` sau đó. TW giữ nguyên lỗi đó; VN đã chuẩn hóa thành 3 tag thường đúng. Chỉ sửa gloss Teitetsu trong dòng này, không "sửa" phía VN.
- Không có dòng nào JP/TW xung đột cần ghi nhận thêm; không có dòng nào JP bị cắt cụt cần hoàn thiện.

## 6. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 41 giá trị fix đối chiếu JP (không chỉ kiểm parse): **41 tổng / 41 kiểm tra lại / 0 loại bỏ / 3 sửa lại**. Ghi chú của parent (20/11): sau lần 2, parent loại thêm 1 fix sai (2616) nên tổng cuối là **40 fix**.
- 2276: bản thảo chỉ sửa Ohimitera, quên Yui→Yunoi trong cùng dòng (JP 湯医-御一夜間) — đã sửa thành "đoạn giữa Yunoi và Ohitoyo".
- 2778: cùng lỗi — bản thảo quên Yui→Yunoi (JP 湯医発船場) — đã sửa thành "bến thuyền Yunoi".
- 3268: bỏ từ "lại" thừa trong bản thảo fix.
Kiểm tra cơ học bổ sung: ngoặc 「」『』() cân bằng ở cả 41 fix; số lượng tag %l trong fix bằng đúng trong VN cũ ở mọi dòng (không thêm/bớt tag); không có dấu ngoặc kép ASCII nào trong fix.

## 7. Khối TOML

Khối TOML dưới đây parse được bằng tomllib, **40 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"2209" = "「Cái gì mà 『Không phải chuyện lợi ích』 chứ, toàn là nói xằng nói bậy. Nếu không có lợi ích, thì ngay cả ngôi đền này cũng chẳng duy trì nổi đâu――Ư!」"
"2218" = "「Khách sáo quá nha, chị Fukami.\\nLúc khó khăn thì phải giúp đỡ lẫn nhau chứ nha!」"
"2221" = "「Anh nói bé Nagi sao?」"
"2228" = "「Khách đi thuyền trên sông Kuma giảm đi nhiều quá, các bác cầm lái\\nnghỉ việc hết trơn, chị Fukami đang gặp khó khăn lắm nha.」"
"2264" = "「Chuyện anh là sinh viên Đại học Đế quốc, chuyện anh đang giúp đỡ công việc gia đình\\n――À, phải rồi.」"
"2276" = "「Ra là vậy. Nếu là đoạn giữa Yunoi và Ohitoyo thì.」"
"2352" = "「À――chuyện đó thì tất nhiên. Không, không phải tôi ngạc nhiên vì coi Ohitoyo là vùng quê ở điểm đó.」"
"2369" = "「Ư…… Hau……」"
"2396" = "「Bến thuyền――ở Yunoi cũng có ạ.\\nỞ đoạn thượng nguồn xa hơn, nước chảy xiết hơn.」"
"2430" = "「Chị Fukami ơiii!」"
"2475" = "「Tôi――」"
"2477" = "「Sao…… nhỉ.」"
"2479" = "「Tôi không sợ ma hay quỷ.\\nVì thực tế luôn xua đuổi những thứ đó.」"
"2486" = "「Trước mắt, bọn anh định quay lại ga Ohitoyo.」"
"2508" = "「Em là Hachiroku, \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; \\x%l8620;#00ffc040;8620%l;#;,\\nthuộc dòng \\x%l8620;#00ffc040;8620%l;#; của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ, như ngài Soutetsu vừa giới thiệu ạ.」"
"2510" = "「Tôi là người trở về Ohitoyo để yêu cầu hủy bỏ việc thu hút nhà máy.\\nNhân cơ hội này, chúng ta có thể nói chuyện một chút được không?」"
"2604" = "「Đúng nha! Mấy anh chị này là đồng minh của chúng ta nha!\\nThế nên, em mới dẫn đến chỗ chị Fukami nha!」"
"2605" = "「Đúng vậy. Thế nên mới cần xe tải. Ạ.\\nBây giờ bến thuyền ở Yunoi thiếu người nên không dùng nữa.」"
"2642" = "「Tay nghề điêu luyện thật đấy.\\nNagi có nói là 『chị Fukami làm từ hồi nhỏ』 nhỉ.」"
"2656" = "「Đúng vậy. Tôi cũng cảm thấy rất trong lành.\\nNơi này, xưa nay vẫn không hề thay đổi.」"
"2708" = "「Xin lỗi vì đã để quý khách phải đợi. Đây là bến thuyền xuôi dòng Kuma Ohitoyo,\\nnhân viên tiếp tân Hayase xin nghe.」"
"2767" = "「Vậy thì, vừa hay――\\nƯm, có một người từng làm việc ở \\x%l帝鉄;#00ffc040;Teitetsu%l;#;? hay gì đó ạ.」"
"2771" = "「Mỏ than bỏ hoang Jutsu-sen phải không ạ. Gần đó――\\nlà đi qua khu vực không thể sử dụng \\x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」"
"2778" = "「Nếu vậy, chúng ta cùng cố gắng nhé.\\nPhục hưng du lịch Ohitoyo, cũng là hồi sinh bến thuyền Yunoi.」"
"2779" = "「Nếu vậy, hãy cho anh và Hachiroku trải nghiệm đi thuyền xuôi dòng Kuma đi.\\nĐương nhiên là anh sẽ trả tiền vé cho hai người lớn.」"
"2801" = "「Ohitoyo là một thị trấn thoang thoảng mùi nước……\\nNhưng không khí ở đây dường như lại trong lành hơn hẳn.」"
"2813" = "「Quỷ, rồi lại ma.\\nOhitoyo là một vùng đất đáng sợ ngoài sức tưởng tượng nhỉ.」"
"2815" = "「Ư!?」"
"2995" = "Để chắc chắn, tôi nhận lấy tấm danh thiếp và nhìn kỹ, quả nhiên trên đó ghi,\\n『Giám đốc chi nhánh Ohitoyo, Ngân hàng Kumamoto』――Ư!?"
"3005" = "Theo lời nhờ vả của Hachiroku, tôi luôn giữ \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; khư khư bên mình.\\nBên trong tất nhiên là \\x%l運転体;#00ffc040;thân vận hành%l;#; rồi."
"3092" = "Để gặp cựu nhân viên của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ mà Fukami đã cho tôi biết――\\nĐền chủ của đền Akai."
"3129" = "Gật đầu――và ngay khoảnh khắc đó tôi chợt nhận ra.\\nGiám đốc chi nhánh của 『Ngân hàng Kumamoto chi nhánh Ohitoyo』."
"3217" = "Tôi từng đến đây viếng đền rồi.\\nĐược ông Taito, Hibiki và chị Mayami dẫn đi."
"3254" = "Như lời ông lão Minokasa đã nói,\\nviệc tìm hiểu thực trạng du lịch ở Ohitoyo mới là ưu tiên hàng đầu."
"3268" = "Chưa bao giờ tôi nghĩ về khuôn mặt hay biểu cảm của dòng sông,\\nnhưng thứ mà tôi nhìn thấy mỗi ngày khiến tôi bỗng thấy hơi tò mò."
"3296" = "Fukami có chiều sâu.\\nNếu có thể khơi gợi nó ra, có lẽ cô bé sẽ trở thành sức mạnh chống đỡ cho Ohitoyo."
"3356" = "Vậy mà nơi đây, một trong những địa điểm du lịch nổi tiếng của Ohitoyo.\\nLại vắng tanh vắng ngắt... chẳng có lấy một bóng người."
"3359" = "Hachiroku vẫn ngồi trên đùi tôi y như lúc dùng \\x%l運転体;#00ffc040;thân vận hành%l;#;,\\ncũng bị chuyển động đó làm cho đung đưa theo."
"3376" = "Nếu đổi \\x%lタブレット;#00ffc040;máy tính bảng%l;#; thì size trẻ em cũng sẽ thành to thôi,\\nnhưng trong trường hợp đó thì xử lý áo phao thế nào đây――ủa."
"3404" = "Nói đến ngân hàng ở Ohitoyo, thì chỉ có một."
```

## Kết bài

File 10 là một file tương đối sạch (9,3% sai, thấp hơn mức trung bình ~15% của dự án tới nay): không có dòng lệch, không có chuỗi xoay, không có nhiễm chéo, không có dòng chưa dịch. Lỗi tập trung vào thuật ngữ đã chốt (Ohitoyo 14 dòng — đúng con số 14 đã đếm trước đó, Yunoi 4 dòng, Teitetsu 3 dòng) và đại từ của Soutetsu (7/11 dòng đại từ là tự xưng của Soutetsu, trong đó 3 dòng "anh"→"tôi" với Hachiroku và 1 dòng ngược lại với Fukami). Hai lỗi nghĩa đều là kiểu bịa/dịch ngược của bản Gemini gốc, trong đó 3268 là ví dụ rõ nhất (bịa thêm "nghe những điều người ta" không có trong JP). Sau file này, Ohitoyo còn lại trong 00_Common: **74** (14: 30, 15: 15, 11: 12, 12: 6, 13: 3, 01 pilot: 8 chưa chốt). Còn lại chưa kiểm toán trong 00_Common: 11, 12, 13, 14, 15, 末尾 (6 file; file 01 vẫn là bản nháp pilot). Phán đoán 2616 đã được parent quyết (giữ "Chị nghĩ", xem §4); 2597 giữ nguyên "em" chờ Hieu xem lại nếu muốn (người nghe chưa rõ).