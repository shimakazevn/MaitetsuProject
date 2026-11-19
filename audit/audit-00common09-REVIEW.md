# Audit 00_Common file 09 — 共通09_さきだつもの.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通09_さきだつもの.txt.toml` — md5 `c2bc3fe444488de0f3599b65c6d6334f`, BOM, CRLF, `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 497 hàng `[script]`.
**Kết quả: 36/497 dòng sai (7,2%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 18 |
| Đại từ xưng hô (pronoun) | 9 |
| Thẻ gloss %l (tag) | 4 |
| Tiếng thở/gasp (gasp) | 3 |
| Sai nghĩa (meaning) | 2 |
| **Tổng** | **36** |

**Theo loại dòng:** thoại 27/286 sai (9,4%), độc thoại 9/211 sai (4,3%).
**Theo nhân vật:** 双鉄 (Soutetsu) 13, monologue 9, 路子 (Michiko) 4, 蓑笠 (Minokasa) 3, 日々姫 (Hibiki) 2, ハチロク (Hachiroku) 2, ポーレット (Paulette) 2, 凪 (Nagi) 1.

Nhóm thuật ngữ (18) chia nhỏ: Ohimitera→Ohitoyo 15 dòng (2199, 2221, 2452, 2497, 2569, 2710, 2741, 2770, 2782, 3001, 3005, 3027, 3138, 3150, 3303 — file này là file 00_Common "bẩn" nhất về Ohimitera, gấp 3 lần file 05 với 11 dòng); 帝鉄→Teitetsu 3 dòng (2482, 2644, 2724); 湯医→Yunoi 1 dòng (3027, chung dòng với Ohitoyo). Nhóm đại từ (9): Soutetsu gọi Paulette "cô"→"em" 4 dòng (2601, 2737, 2355, 2363); Soutetsu tự xưng "anh" sai đối tượng 1 dòng (2397 với Minokasa); Soutetsu tự xưng "tôi" sai với Nagi 1 dòng (2719 — Nagi gọi Soutetsu là にーさん 421 lần, xem quyết định 20/11); B4 — Paulette gọi "Soutetsu-kun"→"anh Soutetsu" 2 dòng (2461, 2632); Soutetsu gọi ông lão Minokasa là "cô" 1 dòng (2161).

File này sạch về cấu trúc: **không có dòng nào lệch dòng** (misaligned), không có chuỗi xoay, không có nhiễm chéo — toàn bộ 36 lỗi đều là lỗi tại chỗ, sửa được ngay không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `c2bc3fe444488de0f3599b65c6d6334f`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** VN khớp tuyệt đối 227 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 269 hàng; chỉ 1 khác biệt duy nhất là key 3378 (TOML đã làm phẳng ký tự `\n` thành khoảng trắng — hiện tượng đã biết, CSV3 là bản chuẩn cho fix list; không phải lỗi dịch, không tính vào 37).
- **Sweep っ (gasp) — ĐÍNH CHÍNH CỦA PARENT (20/11):** sweep CÓ liệt kê file này — 9 mục trong sweep-raw-gasp-wrong.json (109, 2581, 2634, 2681, 2796, 3270, 3284, 3655, 2359). Parent đã kiểm chứng 8 giá trị fix của sweep đều đúng (2796 trùng khớp với fix của audit: 「Ư!」); 2359 already-rendered đúng, không sửa. 2 gasp mất do audit phát hiện mà sweep bỏ sót: 2326, 2802. Nhận định "sweep chưa bao giờ liệt kê file 09" của audit là sai — agent đã tra nhầm file.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng), không có VN mồ côi (orphan), không có hàng VN == TW, không có key trùng. Các VN trùng nhau trong file chỉ là câu cảm thán ngắn lặp lại hợp lệ (「Á!?」×2, 「Chà.」×2, 「Vâng.」×4...).
- **Kiểm tra nhiễm chéo:** đối chiếu toàn bộ VN của file qua chỉ mục VN toàn dự án — chỉ 2 trùng khớp ngoài file, đều là SFX lặp lại hợp lệ (3675 tiếng còi tàu, trùng 共通01 1668; 3676 だだだだだっ, trùng 凪ふかみ01 2484). JP của 2802 trùng với Grand 01 3088, nhưng đó là dòng đã lệch sẵn trong Grand 01 (file đó đã audit, 45,6% sai) — không phải nhiễm vào file 09: VN của 2802 khớp đúng JP của chính nó.

## 3. Các lỗi đã sửa (36 dòng)

### 102 — monologue — meaning

**JP:** \x%l8620;#00ffc040;8620%l;#;改修は現状、妨害に耐えられるような計画ではない。⏎であるのならば、堅いところから始めるべきだ。

**TW:** \x%l8620;#00ffc040;８６２０%l;#;的修復計劃現狀並非牢不可破。那麼我們就應該從最艱難的部分開始。

**VN cũ:** Kế hoạch sửa chữa \x%l8620;#00ffc040;8620%l;#; hiện tại chưa đủ vững chắc để chống chọi lại những hành động phá hoại.⏎Nếu vậy, chúng ta nên bắt đầu từ những nơi an toàn nhất.

**Fix:** Kế hoạch sửa chữa \x%l8620;#00ffc040;8620%l;#; hiện tại chưa đủ vững chắc để chống chọi lại những hành động phá hoại.⏎Nếu vậy, chúng ta nên bắt đầu từ những chỗ khó khăn nhất.

JP 堅いところ = chỗ khó khăn/cứng rắn; TW 從最艱難的部分開始. Bản cũ dịch ngược nghĩa ("nơi an toàn nhất").

### 2161 — 双鉄 — pronoun

**JP:** 「そういってもらえればありがたい」

**TW:** 「你能這麼說我很開心」

**VN cũ:** 「Cô nói vậy tôi thấy rất biết ơn.」

**Fix:** 「Ông nói vậy tôi thấy rất biết ơn.」

Đối tượng là ông lão Minokasa (蓑笠老人). Gọi ông lão là "cô" sai. (Đối chiếu 2464 cùng file: Soutetsu với Minokasa dùng "Ông".)

### 2182 — 路子 — tag

**JP:** 「れっしゃのゆか、木の板だからいたいよぉ」

**TW:** 「列車的地板是木頭鋪的，掉下來好痛啦～」

**VN cũ:** 「Sàn \x%l列車;#00ffc040;tàu%l;#; làm bằng gỗ nên đau lắm đó.」

**Fix:** 「Sàn tàu làm bằng gỗ nên đau lắm đó.」

JP không có tag %l ở 列車 (「れっしゃのゆか」) — tag do bản Việt tự thêm. Tiền lệ reina02: gỡ tag VN tự thêm, giữ text.

### 2199 — 日々姫 — terminology

**JP:** 「十四万五千って！⏎御一夜の人口よりずっとずううっと多いばいっ！！」

**TW:** 「十四萬五千人！這不是比御一夜的人口還老鼻子多咧！」

**VN cũ:** 「Mười bốn vạn năm ngàn người cơ á!⏎Nhiều hơn dân số của Ohimitera rất rất nhiều luôn đó!!」

**Fix:** 「Mười bốn vạn năm ngàn người cơ á!⏎Nhiều hơn dân số của Ohitoyo rất rất nhiều luôn đó!!」

御一夜 = "Ohitoyo" theo quyết định 19/11 (không dùng Ohimitera/Ohito).

### 2216 — 凪 — meaning

**JP:** 「ゆーちてっかい！」

**TW:** 「反對工廠！」

**VN cũ:** 「Hủy bỏ thu hút!」

**Fix:** 「Phản đối thu hút nhà máy!」

JP ゆーちてっかい = 誘致反対 (phương ngữ của Nagi); TW 反對工廠. 反対 = phản đối, không phải "hủy bỏ".

### 2221 — 双鉄 — terminology

**JP:** 「水汚染が起きれば、御一夜はゆるやかに死んでいく――⏎そうと理解しているものは、決して少なくないはずだ」

**TW:** 「只要水源被汙染，御一夜就會陷入慢性死亡——這麼想的人肯定不在少數」

**VN cũ:** 「Nếu ô nhiễm nguồn nước xảy ra, Ohimitera sẽ chết mòn——⏎Những người hiểu được điều đó chắc chắn không hề ít đâu.」

**Fix:** 「Nếu ô nhiễm nguồn nước xảy ra, Ohitoyo sẽ chết mòn——⏎Những người hiểu được điều đó chắc chắn không hề ít đâu.」

御一夜 = "Ohitoyo".

### 2326 — 双鉄 — gasp

**JP:** 「あぐっ！」

**TW:** 「啊嗚！」

**VN cũ:** 「Á!」

**Fix:** 「Agu!」

JP あぐっ！ — っ bị mất hẳn. Tiền lệ file 05 key 2284: あぐっ → "Agu.".

### 2355 — 双鉄 — pronoun

**JP:** 「うむ。だからやるさ。⏎ついては、知恵を貸して欲しい」

**TW:** 「嗯。所以我們得馬上開展工作。總之，馬上有件事想聽聽你的意見」

**VN cũ:** 「Ừm. Nên mới phải làm chứ.⏎Nhân tiện, tôi muốn nhờ cô cho tôi chút ý kiến.」

**Fix:** 「Ừm. Nên mới phải làm chứ.⏎Nhân tiện, tôi muốn nhờ em cho tôi chút ý kiến.」

Soutetsu xưng hô với người đối thoại trong cảnh này (Michiko/Paulette) — "cô" sai; với cả hai người này Soutetsu đều dùng "em".

### 2363 — 双鉄 — pronoun

**JP:** 「ああ、すまん。⏎朝方の貴重な時間を、ありがとう」

**TW:** 「嗯，抱歉。謝謝你利用清晨的寶貴時間為我出主意」

**VN cũ:** 「À, xin lỗi nhé.⏎Cảm ơn cô đã dành thời gian quý báu buổi sáng cho tôi.」

**Fix:** 「À, xin lỗi nhé.⏎Cảm ơn em đã dành thời gian quý báu buổi sáng cho tôi.」

Đối tượng là Paulette (2362 Paulette vừa nói; cô ấy là người đã dành thời gian buổi sáng). Soutetsu→Paulette = "em".

### 2397 — 双鉄 — pronoun

**JP:** 「十四万四千九百二十八人、と聞いたぞ」

**TW:** 「她說十四萬四千九百二十八人」

**VN cũ:** 「Mười bốn vạn bốn ngàn chín trăm hai mươi tám người, anh nghe vậy đấy.」

**Fix:** 「Mười bốn vạn bốn ngàn chín trăm hai mươi tám người, tôi nghe vậy đấy.」

Soutetsu đang báo con số Reina nói cho Minokasa nghe (2399 Minokasa đáp lại; cảnh thảo luận với Minokasa). Với Minokasa Soutetsu xưng "tôi/cháu" (2760 "cháu"), không dùng "anh".

### 2452 — 日々姫 — terminology

**JP:** 「御一夜から湯医までが大人６９０円でしょう？⏎だったら、ええっと……、一億円だとして――」

**TW:** 「從御一夜到湯醫一張成人票６９０日元對吧？也就是說……嗯，一億日元的話——」

**VN cũ:** 「Từ Ohimitera đến Yunoi, vé người lớn là 690 yên đúng không?⏎Vậy thì, à ừm……, giả sử là một trăm triệu yên thì——」

**Fix:** 「Từ Ohitoyo đến Yunoi, vé người lớn là 690 yên đúng không?⏎Vậy thì, à ừm……, giả sử là một trăm triệu yên thì——」

御一夜 = "Ohitoyo".

### 2461 — ポーレット — pronoun

**JP:** 「どうしたんですか？　双鉄くん」

**TW:** 「怎麼了嗎？雙鐵君」

**VN cũ:** 「Sao vậy? Soutetsu-kun.」

**Fix:** 「Sao vậy? Anh Soutetsu.」

B4: Paulette gọi 双鉄くん trần là sai → "anh Soutetsu" (kể cả khi đang ngạc nhiên, không có ngoại lệ). "Anh" viết hoa vì đứng đầu câu sau dấu "?".

### 2482 — ハチロク — terminology

**JP:** 「旧\x%l帝鉄;#00ffc040;帝鉄%l;\x%l8620;#;#00ffc040;8620%l;#;形トップナンバー\x%l8620;#00ffc040;8620%l;#;専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、⏎ハチロクともうします」

**TW:** 「我是前\x%l帝鉄;#00ffc040;帝國鐵路%l;\x%l8620;#;#00ffc040;８６２０%l;#;型首車\x%l8620;#00ffc040;８６２０%l;#;專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;——八六」

**VN cũ:** 「Em là \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của đầu máy số hiệu đầu tiên thuộc dòng \x%l8620;#00ffc040;8620%l;#; của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ,⏎tên là Hachiroku ạ.」

**Fix:** 「Em là \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của đầu máy số hiệu đầu tiên thuộc dòng \x%l8620;#00ffc040;8620%l;#; của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ,⏎tên là Hachiroku ạ.」

帝鉄 = "Teitetsu" theo quyết định 19/11 (#6); "Đường sắt Hoàng gia" là dịch sai (帝鉄 viết tắt 帝国鉄道, không phải hoàng gia).

### 2497 — 双鉄 — terminology

**JP:** 「だから、御一夜を。⏎クマ川と焼酎と温泉の――この水の町を救いたいんです」

**TW:** 「所以，我想要拯救御一夜、隈河、燒酒廠還有溫泉——拯救這座水鄉」

**VN cũ:** 「Vì thế, cháu muốn cứu lấy Ohimitera.⏎Cứu lấy dòng sông Kuma, shochu và suối nước nóng――cứu lấy thị trấn của nước này.」

**Fix:** 「Vì thế, cháu muốn cứu lấy Ohitoyo.⏎Cứu lấy dòng sông Kuma, shochu và suối nước nóng――cứu lấy thị trấn của nước này.」

御一夜 = "Ohitoyo".


### 2569 — 蓑笠 — terminology

**JP:** 「御一夜の観光の実情がどぎゃんもんか、⏎ほーで少しは、わかってもらえると思いますけん」

**TW:** 「正好也親眼見識一下御一夜旅遊業的實際情況」

**VN cũ:** 「Để cậu có thể hiểu được phần nào,⏎thực trạng du lịch ở Ohimitera là như thế nào.」

**Fix:** 「Để cậu có thể hiểu được phần nào,⏎thực trạng du lịch ở Ohitoyo là như thế nào.」

御一夜 = "Ohitoyo".

### 2580 — 路子 — tag

**JP:** 「だいじょうぶ！？　⏎じょうききかんしゃの火、消えちゃわない？」

**TW:** 「沒事吧！？蒸——汽——機——車的火，不會滅掉吧？」

**VN cũ:** 「Không sao chứ!?⏎Lửa của \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; có bị tắt không?」

**Fix:** 「Không sao chứ!?⏎Lửa của đầu máy hơi nước có bị tắt không?」

JP không có tag %l ở 蒸気機関車 — tag do bản Việt tự thêm. Gỡ tag, giữ text.

### 2601 — 双鉄 — pronoun

**JP:** 「ポーレット、すまんがここで解散だ。⏎日々姫に見つからぬよう、行ってくれ」

**TW:** 「波萊特，不好意思，我們就在這解散吧。你走的時候小心不要讓日日姬發現」

**VN cũ:** 「Paulette, xin lỗi nhưng chúng ta giải tán ở đây nhé.⏎Cô hãy đi đi kẻo Hibiki phát hiện.」

**Fix:** 「Paulette, xin lỗi nhưng chúng ta giải tán ở đây nhé.⏎Em hãy đi đi kẻo Hibiki phát hiện.」

Đối tượng là Paulette. Soutetsu→Paulette = "em".

### 2632 — ポーレット — pronoun

**JP:** 「ほんとだ。双鉄くんの言うとおり。⏎それなら、やらないと損ですね」

**TW:** 「確實，就如雙鐵君所說。既然這樣，不去嘗試才是損失呢」

**VN cũ:** 「Đúng thật. Đúng như Soutetsu-kun nói.⏎Nếu vậy thì không làm mới là thiệt thòi nhỉ.」

**Fix:** 「Đúng thật. Đúng như anh Soutetsu nói.⏎Nếu vậy thì không làm mới là thiệt thòi nhỉ.」

B4: 双鉄くん → "anh Soutetsu".

### 2644 — 蓑笠 — terminology

**JP:** 「[こくら,1]粉蔵の辺りに、\x%l帝鉄;#00ffc040;帝鉄%l;#;の車両工場ばあったそうですたい。⏎そこがのうなって、ま、やむなく言うところでしょうの」

**TW:** 「聽說小倉那一帶以前就是\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的車輛工廠。因為那邊倒了，她們才不得已來找我這糟老頭子吧」

**VN cũ:** 「Nghe nói quanh khu vực Kokura từng có nhà máy chế tạo toa xe của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;.⏎Chỗ đó không còn nữa, nên chắc là bất đắc dĩ mới phải nhờ đến tôi thôi.」

**Fix:** 「Nghe nói quanh khu vực Kokura từng có nhà máy chế tạo toa xe của \x%l帝鉄;#00ffc040;Teitetsu%l;#;.⏎Chỗ đó không còn nữa, nên chắc là bất đắc dĩ mới phải nhờ đến tôi thôi.」

帝鉄 = "Teitetsu".

### 2710 — 蓑笠 — terminology

**JP:** 「右田の――ほれ、御一夜でいっとう古か焼酎蔵さんの、⏎息子さんよ」

**TW:** 「這位是右田家的——就那個御一夜最老的燒酒廠的大兒子」

**VN cũ:** 「Của nhà Migita đấy――cháu biết mà, con trai của xưởng shochu lâu đời nhất Ohimitera đó.」

**Fix:** 「Của nhà Migita đấy――cháu biết mà, con trai của xưởng shochu lâu đời nhất Ohitoyo đó.」

御一夜 = "Ohitoyo".

### 2719 — 双鉄 — pronoun

**JP:** 「そうか。⏎そう言われると、なんとも誇らしい気持ちを感じる」

**TW:** 「這樣啊。聽到你這麼說，我感到很自豪」

**VN cũ:** 「Vậy sao.⏎Nghe em nói vậy, tôi bỗng cảm thấy thật tự hào.」

**Fix:** 「Vậy sao.⏎Nghe em nói vậy, anh bỗng cảm thấy thật tự hào.」

Soutetsu trả lời Nagi (2718 Nagi nói "Thầy của em là giỏi nhất Hinomoto"). Nagi gọi Soutetsu là にーさん ("anh hai") 421 lần toàn dự án, không bao giờ gọi 双鉄さん/双鉄様 — theo nguyên tắc đối ứng (khóa B4), Soutetsu là "anh" với Nagi. "Tôi" sai. (Bổ sung bởi parent 20/11 — audit gốc bỏ sót dòng này và sai tiền đề ở 2123.)

### 2724 — ハチロク — terminology

**JP:** 「ここの刃物は、みな、命を持っているようです。⏎命を持った部品など、\x%l帝鉄;#00ffc040;帝鉄%l;#;でもほとんど見ませんでした」

**TW:** 「這裡的刀具彷彿像活的一樣。這麼具有生命力的部件，就算在\x%l帝鉄;#00ffc040;帝國鐵路%l;#;之中也很罕見」

**VN cũ:** 「Dao kéo ở đây, trông cái nào cũng như có sinh mệnh vậy.⏎Những phụ tùng có sinh mệnh như thế này, ngay cả ở \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; em cũng hiếm khi thấy.」

**Fix:** 「Dao kéo ở đây, trông cái nào cũng như có sinh mệnh vậy.⏎Những phụ tùng có sinh mệnh như thế này, ngay cả ở \x%l帝鉄;#00ffc040;Teitetsu%l;#; em cũng hiếm khi thấy.」

帝鉄 = "Teitetsu".

### 2737 — 双鉄 — pronoun

**JP:** 「では、あげてくれ。⏎うまくいかないと何が困る？」

**TW:** 「那你說說。行不通會有什麼問題？」

**VN cũ:** 「Vậy cô cứ nói đi.⏎Nếu không suôn sẻ thì có gì đáng lo ngại?」

**Fix:** 「Vậy em cứ nói đi.⏎Nếu không suôn sẻ thì có gì đáng lo ngại?」

Đối tượng là Paulette (2739 Paulette đáp). Soutetsu→Paulette = "em".

### 2740 — 路子 — tag

**JP:** 「ねぇ、そーちゃん、いま何時？⏎れっしゃ、どの辺を走ってるの？」

**TW:** 「那個，小雙，現在幾點了？車子現在行駛到哪裡了呢？」

**VN cũ:** 「Này, Sou-chan, bây giờ là mấy giờ rồi?⏎\x%l列車;#00ffc040;Tàu%l;#; đang chạy đến đoạn nào rồi?」

**Fix:** 「Này, Sou-chan, bây giờ là mấy giờ rồi?⏎Tàu đang chạy đến đoạn nào rồi?」

JP không có tag %l ở 列車 (「れっしゃ」) — tag do bản Việt tự thêm. Gỡ tag, giữ text.

### 2741 — 双鉄 — terminology

**JP:** 「隈元銀行御一夜支店。⏎\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致推進派の、いわば総本山だな」

**TW:** 「那可是隈元銀行御一夜支行——\x%lエアクラ;#00ffc040;空凝機%l;#;工廠支持派的大本營呢」

**VN cũ:** 「Chi nhánh Ohimitera của Ngân hàng Kumamoto.⏎Có thể nói đây là tổng hành dinh của phe thúc đẩy thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」

**Fix:** 「Chi nhánh Ohitoyo của Ngân hàng Kumamoto.⏎Có thể nói đây là tổng hành dinh của phe thúc đẩy thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」

御一夜 = "Ohitoyo".

### 2770 — 双鉄 — terminology

**JP:** 「銀行サイド……\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致派もまた、⏎御一夜の復興を真摯に願っていることは確からしいな」

**TW:** 「銀行那邊……支持\x%lエアクラ;#00ffc040;空凝機%l;#;工廠建設的人似乎也真切盼望御一夜的復興」

**VN cũ:** 「Phía ngân hàng……những người ủng hộ việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,⏎có vẻ như cũng đang thực tâm mong muốn sự phục hưng của Ohimitera nhỉ.」

**Fix:** 「Phía ngân hàng……những người ủng hộ việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,⏎có vẻ như cũng đang thực tâm mong muốn sự phục hưng của Ohitoyo nhỉ.」

御一夜 = "Ohitoyo".

### 2782 — 双鉄 — terminology

**JP:** 「クマ川の町、水の町、温泉と焼酎の町――⏎御一夜のイメージが広く定着すれば、誘致も頓挫しよう」

**TW:** 「隈河之畔的城市、水之鄉、有著溫泉和燒酒的城市——只要給御一夜多貼上一些標籤，工廠落戶計劃想必也將受阻」

**VN cũ:** 「Thành phố của sông Kuma, thành phố của nước, thành phố của suối nước nóng và shochu——⏎Nếu hình ảnh của Ohimitera được khẳng định rộng rãi, thì kế hoạch thu hút nhà máy cũng sẽ bị cản trở thôi.」

**Fix:** 「Thành phố của sông Kuma, thành phố của nước, thành phố của suối nước nóng và shochu——⏎Nếu hình ảnh của Ohitoyo được khẳng định rộng rãi, thì kế hoạch thu hút nhà máy cũng sẽ bị cản trở thôi.」

御一夜 = "Ohitoyo". (Monologue; JP 御一夜のイメージ.)

### 2796 — 双鉄 — gasp

**JP:** 「っ！」

**TW:** 「！」

**VN cũ:** 「!」

**Fix:** 「Ư!」

JP bare 「っ！」 — gasp mất hẳn, chỉ còn "!". Tiền lệ sweep file 01 key 1247: っ đầu dòng → "Ư".

### 2802 — 路子 — gasp

**JP:** 「っ！！？　これダメっ！⏎にげてっ！　にげてそーちゃんっ！！」

**TW:** 「！！？這個要出事！快逃！快逃啊，小雙！！」

**VN cũ:** 「!!? Không được rồi!⏎Chạy đi! Chạy đi Sou-chan!!」

**Fix:** 「Ư!!? Không được rồi!⏎Chạy đi! Chạy đi Sou-chan!!」

JP mở đầu bằng っ (「っ！！？」) — gasp đầu dòng bị mất. Tiền lệ sweep lr_h1 1077: っ đầu dòng → "Ư". Phần còn lại (ダメっ, にげてっ) là っ nhấn mạnh cuối từ, không thêm Ư.

### 3001 — monologue — terminology

**JP:** 古き時間をそのまま熟成させている――⏎僕の知る御一夜の町並みを、ハチロクに見せてやりたくて。

**TW:** 保存著過去景象的御一夜街道——我想要快點讓八六看到，我所熟知的街景。

**VN cũ:** Lưu giữ trọn vẹn những tháng năm cổ kính――⏎Tôi muốn cho Hachiroku thấy dãy phố Ohimitera mà tôi từng biết.

**Fix:** Lưu giữ trọn vẹn những tháng năm cổ kính――⏎Tôi muốn cho Hachiroku thấy dãy phố Ohitoyo mà tôi từng biết.

御一夜 = "Ohitoyo".

### 3005 — monologue — terminology

**JP:** 隈元銀行御一夜支店の、目指すところがそこであるなら、⏎やはり僕らの目的地とは、些か異なってくるようだ。

**TW:** 假如這就是隈元銀行御一夜支行的目標的話，那麼果然和我們的目標是有著細微差異的。

**VN cũ:** Nếu mục tiêu của chi nhánh Ohimitera của Ngân hàng Kumamoto là như vậy,⏎thì quả nhiên đích đến của chúng tôi có chút khác biệt.

**Fix:** Nếu mục tiêu của chi nhánh Ohitoyo của Ngân hàng Kumamoto là như vậy,⏎thì quả nhiên đích đến của chúng tôi có chút khác biệt.

御一夜 = "Ohitoyo".

### 3027 — monologue — terminology

**JP:** 二時間ならば、⏎ポーレットたちが湯医まで行き御一夜に戻るほどの時間だ。

**TW:** 兩小時後是波萊特她們從湯醫回到御一夜的時間。

**VN cũ:** Hai tiếng đồng hồ,⏎vừa đủ để nhóm Paulette đi đến Yui rồi quay lại Ohimitera.

**Fix:** Hai tiếng đồng hồ,⏎vừa đủ để nhóm Paulette đi đến Yunoi rồi quay lại Ohitoyo.

Hai thuật ngữ trong một dòng: 湯医 = "Yunoi" (quyết định 19/11 #7; "Yui" sai), 御一夜 = "Ohitoyo".

### 3138 — monologue — terminology

**JP:** 渡されたのは、⏎『御一夜観光イラストマップ』。

**TW:** 她拿給我的是“御一夜觀光彩繪地圖”。

**VN cũ:** Thứ cô ấy đưa cho tôi,⏎là "Bản đồ minh họa du lịch Ohimitera".

**Fix:** Thứ cô ấy đưa cho tôi,⏎là "Bản đồ minh họa du lịch Ohitoyo".

御一夜 = "Ohitoyo" (tên trong 『御一夜観光イラストマップ』).

### 3150 — monologue — terminology

**JP:** 右田に迎えられることがなければ、⏎御一夜でたくさんを学ばなければ、僕は腐って死んでいた。

**TW:** 如果沒有被右田家收養，如果沒有在御一夜長大，我一定已經爛在某個不知名的角落裡了。

**VN cũ:** Nếu không được nhà Migita nhận nuôi,⏎nếu không được học hỏi nhiều điều ở Ohimitera, thì cháu đã mục nát và chết từ lâu rồi.

**Fix:** Nếu không được nhà Migita nhận nuôi,⏎nếu không được học hỏi nhiều điều ở Ohitoyo, thì cháu đã mục nát và chết từ lâu rồi.

御一夜 = "Ohitoyo".

### 3303 — monologue — terminology

**JP:** 日々姫の視線が、レールショップの壁へと走る。⏎そこにあるのは、御一夜鉄道クマ川線の運賃表だ。

**TW:** 日日姬不禁看向鐵路商店的牆上。那裡貼的是御一夜鐵路隈河線的票價表。

**VN cũ:** Ánh mắt Hibiki hướng về phía bức tường của cửa hàng đường sắt.⏎Nơi đó có dán bảng giá vé tuyến Kumagawa của Đường sắt Ohimitera.

**Fix:** Ánh mắt Hibiki hướng về phía bức tường của cửa hàng đường sắt.⏎Nơi đó có dán bảng giá vé tuyến Kumagawa của Đường sắt Ohitoyo.

御一夜 = "Ohitoyo" (御一夜鉄道クマ川線).

### 3519 — monologue — tag

**JP:** 車内販売のお姉さんが、⏎なんとかみんなを落ち着かせようと頑張っている。

**TW:** 負責在列車上售賣商品的姐姐正在努力安撫乘客。

**VN cũ:** Chị \x%l車販;#00ffc040;nhân viên bán hàng%l;#; trên tàu,⏎đang cố gắng hết sức để trấn an mọi người.

**Fix:** Chị nhân viên bán hàng trên tàu,⏎đang cố gắng hết sức để trấn an mọi người.

JP không có tag %l ở 車販 — tag do bản Việt tự thêm. Gỡ tag, giữ text.

## 4. Kiểm tra chéo

- **Chuỗi xoay (rotation):** 0 chuỗi. Không có dòng nào mà VN đúng nằm ở key khác trong file.
- **Nhiễm chéo file:** 0. Xem §2 (2 trùng khớp đều là SFX lặp lại hợp lệ).
- **Thẻ %l:** 4 tag do bản Việt tự thêm đã gỡ (2182, 2580, 2740, 3519 — JP không có tag ở các vị trí đó; tiền lệ reina02). Không có tag nào thiếu dấu `;` đóng trong file này. Lưu ý riêng key 2482: JP gốc có cấu trúc tag dị dạng (`\x%l帝鉄;#00ffc040;帝鉄%l;` đóng bằng `%l;` rồi `\x%l8620;#;` thừa) — TW giữ nguyên cấu trúc đó, VN đã chuẩn hóa thành 3 tag thường; đây là quirk phía JP, không tính lỗi, chỉ sửa gloss 帝鉄→Teitetsu và giữ nguyên dạng tag như VN đang có.
- **Gasp っ:** sweep CÓ liệt kê file này (9 mục; xem §2 đính chính). Audit tự kiểm tra toàn bộ っ trong JP: 3 gasp mất đã sửa (2326 あぐっ→"Agu!" theo tiền lệ file 05 2284; 2796 bare っ!→"Ư!" — trùng với fix của sweep; 2802 っ đầu dòng→"Ư!!?" theo tiền lệ lr_h1 1077). Các っ còn lại đều đã được diễn đúng hoặc là っ nhấn mạnh cuối từ (không thêm Ư): 2321 子っ, 2343 ぐあっ→"Hự", 2344 んっ――ぐっ――→"Ưm――hự――", 2798 んっ――→"Ưm——", 3493 浮くっ (nhấn mạnh), 2802 ダメっ/にげてっ (nhấn mạnh, chỉ sửa っ đầu dòng).
- **まいてつ / 市電:** file này không có dòng nào dùng 2 thuật ngữ này (0 gloss まいてつ, 0 市電) — không áp dụng quyết định mới 20/11 ở đây.
- **Soutetsu "anh" với Michiko:** các dòng 2353, 2356, 2487, 2492, 2494, 2503, 2664 dùng "anh" với Michiko (em gái sinh đôi, anh trai) — ĐÚNG, không sửa. **ĐÍNH CHÍNH QUY TẮC CỦA PARENT (20/11):** quy tắc đúng là "anh" với Hibiki/Michiko/Paulette/Reina (các em gái gọi Soutetsu là "anh"/"anh hai" — Paulette gọi "anh Soutetsu" per khóa B4, Reina gọi "anh Soutetsu", Hibiki gọi "anh hai", Michiko là em sinh đôi); "tôi" với Hachiroku/Mayami/Nagi/Minokasa (quan hệ trang trọng/xa cách). Cách diễn đạt cũ "anh chỉ với Hibiki" là diễn đạt quá hẹp từ file 02 — audit đã áp dụng sai thành fix 2525 ("anh"→"tôi" với Paulette), parent đã loại fix này (xem §3).
- **Soutetsu "cô" đúng:** 2309 ("cô bé" = Nagi, ngôi thứ ba), 2421 ("Cô ấy" = ngôi thứ ba), 2501 ("cô Hinai Paulette" = danh xưng trước tên) — đều không phải lỗi xưng hô.
- **Paulette "anh Soutetsu" đúng:** 2583, 2756, 2792 ("Anh muốn một người như thế nào?") — đã đúng theo B4, không sửa.

## 5. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 37 fix so với JP của từng dòng: **tổng 37 / kiểm tra lại 37 / loại bỏ 0 / sửa 1**. Ghi chú của parent (20/11): sau lần 2, parent loại thêm 2 fix sai (2525, 2123) và bổ sung 1 fix bị sót (2719) nên tổng cuối vẫn là **36 fix**. Lần 2 bắt được 1 lỗi trong bản thảo fix: 2461 viết "anh Soutetsu" thường sau dấu "?" — đã sửa thành "Anh Soutetsu" (viết hoa đầu câu). Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt.

## 6. Các dòng cố tình KHÔNG sửa (ghi chú phán đoán)

- **3238 (monologue):** 「僕は興味ある、僕は興味ある、僕は興味ある――僕のふたごに伝わるように、心で何度も繰り返す。」 VN: "Anh tò mò lắm, anh tò mò lắm, anh tò mò lắm—— Tôi nhẩm đi nhẩm lại trong lòng..." — "Anh" ở đây là nội dung của thông điệp nhẩm trong lòng gửi tới Michiko (truyền tới em sinh đôi), còn "Tôi" là phần tường thuật. Khác với tiền lệ file 06 key 2220 (độc thoại "anh"→"tôi" vì đó là tường thuật về bản thân). Không sửa.
- **3681 (monologue):** 「（泣かせちゃダメだ――僕は、おにいちゃんなんだから）」 VN: "（Không được để em ấy khóc——vì mình, là anh trai mà.）" — "mình" trong độc thoại nội tâm tự vấn cảm xúc — được phép theo ngoại lệ h3 1683. Không sửa.
- **2373:** 「この町に、僕は救われたからです」 VN "thị trấn này đã cứu mạng cháu" — "cứu mạng" hơi mạnh so với 救われた (được cứu) nhưng là cách nói thành ngữ, chấp nhận được. Không sửa.
- **2393:** 蒸気排水 gloss "xả nước ngưng hơi nước" — chính xác về mặt kỹ thuật (van xả nước ngưng ở xi-lanh đầu máy hơi nước); TW 蒸汽排水. Không sửa.
- **102 (phần đầu):** câu đầu "Kế hoạch sửa chữa 8620 hiện tại chưa đủ vững chắc..." khớp JP/TW, chỉ câu sau sai — chỉ sửa câu sau.
- **3378:** chênh lệch `\n` giữa CSV và TOML (TOML làm phẳng thành khoảng trắng) — hiện tượng đã biết, không phải lỗi dịch.

## Kết bài

File 09 là file 00_Common "bẩn" nhất về Ohimitera (15 dòng, gấp 3 lần file 05) nhưng sạch hoàn toàn về cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa chắc chắn. 36 lỗi đều sửa được tại chỗ: 18 thuật ngữ (chủ yếu là các quyết định mới 19/11 chưa được áp dụng), 10 đại từ (tập trung ở Soutetsu với Paulette/Nagi/Minokasa), 4 tag VN tự thêm, 3 gasp mất, 2 sai nghĩa (trong đó 102 dịch ngược nghĩa). Sau file này, 00_Common còn 7 file chưa audit (10, 11, 12, 13, 14, 15, 末尾 — trừ file 01 bản nháp pilot).

Khối TOML dưới đây parse được bằng tomllib, **36 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

```toml
[script]
"102" = "Kế hoạch sửa chữa \\x%l8620;#00ffc040;8620%l;#; hiện tại chưa đủ vững chắc để chống chọi lại những hành động phá hoại.\\nNếu vậy, chúng ta nên bắt đầu từ những chỗ khó khăn nhất."
"2161" = "「Ông nói vậy tôi thấy rất biết ơn.」"
"2182" = "「Sàn tàu làm bằng gỗ nên đau lắm đó.」"
"2199" = "「Mười bốn vạn năm ngàn người cơ á!\\nNhiều hơn dân số của Ohitoyo rất rất nhiều luôn đó!!」"
"2216" = "「Phản đối thu hút nhà máy!」"
"2221" = "「Nếu ô nhiễm nguồn nước xảy ra, Ohitoyo sẽ chết mòn——\\nNhững người hiểu được điều đó chắc chắn không hề ít đâu.」"
"2326" = "「Agu!」"
"2355" = "「Ừm. Nên mới phải làm chứ.\\nNhân tiện, tôi muốn nhờ em cho tôi chút ý kiến.」"
"2363" = "「À, xin lỗi nhé.\\nCảm ơn em đã dành thời gian quý báu buổi sáng cho tôi.」"
"2397" = "「Mười bốn vạn bốn ngàn chín trăm hai mươi tám người, tôi nghe vậy đấy.」"
"2452" = "「Từ Ohitoyo đến Yunoi, vé người lớn là 690 yên đúng không?\\nVậy thì, à ừm……, giả sử là một trăm triệu yên thì——」"
"2461" = "「Sao vậy? Anh Soutetsu.」"
"2482" = "「Em là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của đầu máy số hiệu đầu tiên thuộc dòng \\x%l8620;#00ffc040;8620%l;#; của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ,\\ntên là Hachiroku ạ.」"
"2497" = "「Vì thế, cháu muốn cứu lấy Ohitoyo.\\nCứu lấy dòng sông Kuma, shochu và suối nước nóng――cứu lấy thị trấn của nước này.」"
"2569" = "「Để cậu có thể hiểu được phần nào,\\nthực trạng du lịch ở Ohitoyo là như thế nào.」"
"2580" = "「Không sao chứ!?\\nLửa của đầu máy hơi nước có bị tắt không?」"
"2601" = "「Paulette, xin lỗi nhưng chúng ta giải tán ở đây nhé.\\nEm hãy đi đi kẻo Hibiki phát hiện.」"
"2632" = "「Đúng thật. Đúng như anh Soutetsu nói.\\nNếu vậy thì không làm mới là thiệt thòi nhỉ.」"
"2644" = "「Nghe nói quanh khu vực Kokura từng có nhà máy chế tạo toa xe của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;.\\nChỗ đó không còn nữa, nên chắc là bất đắc dĩ mới phải nhờ đến tôi thôi.」"
"2710" = "「Của nhà Migita đấy――cháu biết mà, con trai của xưởng shochu lâu đời nhất Ohitoyo đó.」"
"2719" = "「Vậy sao.\\nNghe em nói vậy, anh bỗng cảm thấy thật tự hào.」"
"2724" = "「Dao kéo ở đây, trông cái nào cũng như có sinh mệnh vậy.\\nNhững phụ tùng có sinh mệnh như thế này, ngay cả ở \\x%l帝鉄;#00ffc040;Teitetsu%l;#; em cũng hiếm khi thấy.」"
"2737" = "「Vậy em cứ nói đi.\\nNếu không suôn sẻ thì có gì đáng lo ngại?」"
"2740" = "「Này, Sou-chan, bây giờ là mấy giờ rồi?\\nTàu đang chạy đến đoạn nào rồi?」"
"2741" = "「Chi nhánh Ohitoyo của Ngân hàng Kumamoto.\\nCó thể nói đây là tổng hành dinh của phe thúc đẩy thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.」"
"2770" = "「Phía ngân hàng……những người ủng hộ việc thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ncó vẻ như cũng đang thực tâm mong muốn sự phục hưng của Ohitoyo nhỉ.」"
"2782" = "「Thành phố của sông Kuma, thành phố của nước, thành phố của suối nước nóng và shochu——\\nNếu hình ảnh của Ohitoyo được khẳng định rộng rãi, thì kế hoạch thu hút nhà máy cũng sẽ bị cản trở thôi.」"
"2796" = "「Ư!」"
"2802" = "「Ư!!? Không được rồi!\\nChạy đi! Chạy đi Sou-chan!!」"
"3001" = "Lưu giữ trọn vẹn những tháng năm cổ kính――\\nTôi muốn cho Hachiroku thấy dãy phố Ohitoyo mà tôi từng biết."
"3005" = "Nếu mục tiêu của chi nhánh Ohitoyo của Ngân hàng Kumamoto là như vậy,\\nthì quả nhiên đích đến của chúng tôi có chút khác biệt."
"3027" = "Hai tiếng đồng hồ,\\nvừa đủ để nhóm Paulette đi đến Yunoi rồi quay lại Ohitoyo."
"3138" = "Thứ cô ấy đưa cho tôi,\\nlà \"Bản đồ minh họa du lịch Ohitoyo\"."
"3150" = "Nếu không được nhà Migita nhận nuôi,\\nnếu không được học hỏi nhiều điều ở Ohitoyo, thì cháu đã mục nát và chết từ lâu rồi."
"3303" = "Ánh mắt Hibiki hướng về phía bức tường của cửa hàng đường sắt.\\nNơi đó có dán bảng giá vé tuyến Kumagawa của Đường sắt Ohitoyo."
"3519" = "Chị nhân viên bán hàng trên tàu,\\nđang cố gắng hết sức để trấn an mọi người."```
