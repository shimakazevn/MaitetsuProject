# Audit — 02_Hibiki 日々姫01_双鉄の妹 (Soutetsu no Imouto / Em gái của Soutetsu)

- File: `02_Hibiki/日々姫01_双鉄の妹.txt.toml` (đường dẫn đĩa: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb01_#U53cc#U9244#U306e#U59b9.txt.toml`)
- Đọc: **424/424 dòng** (193 độc thoại, 112 thoại Soutetsu, 76 thoại Hibiki, 24 thoại Nagayama, 16 thoại Nagi, 1 ông chú, 1 Reina, 1 chủ tế Akai) — đọc逐行 đầy đủ đối chiếu JP + TW (CSV3).
- Sai: **19 dòng / 424 (4,5%)** — tỉ lệ thấp so với mặt bằng dự án; file này dịch khá chắc tay, lỗi tập trung ở thuật ngữ.
- Lệch vị trí 0 / xoay vòng 0 / nhiễm chéo 0 / mồ côi 0 / chưa dịch 0 / trùng key 0 / không chắc chắn 0.
- CSV bộ duy nhất (424 dòng, key không trùng, 0 VN trống, 0 JP trống). CSV↔TOML: 149 khớp tuyệt đối + 274 gộp `\n` thành khoảng trắng + 1 gộp `\n` thành rỗng (key 2102, VN có "không? \n" — TOML-2 lược `\n` vì đã có khoảng trắng trước đó; cùng quirk đã biết, không phải lỗi dịch).
- TOML md5 `1b7df32b0d9d2850a4cc55d76b04ca8d`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng md5 (file duy nhất).
- Thẻ `%l`: 22 dòng có thẻ theo JP; parity khớp 21/22 — chỉ 1 dòng VN tự thêm thẻ (2208, xem dưới). Sau khi sửa, VN còn đúng 22 thẻ = JP. Không có thẻ hỏng trong file.

## Phân loại (19)

- Thuật ngữ 11 (3290, 2294, 2555, 3034, 2097, 2119, 2312, 2500, 2807, 2973, 1778)
- Xưng hô 2 (2229, 2590)
- Sai nghĩa 2 (2534, 2474)
- Mất tiếng hít 2 (2588, 2589)
- Thẻ `%l` tự thêm 1 (2208)
- Lỗi nhỏ 1 (3140)

## Chi tiết từng dòng sai

### Thuật ngữ

**Key 3290** (monologue)
- JP: （……これも、御一夜をより深く知るため、だ）
- TW: （……這也是為了能更進一步加深對御一夜的了解啊）
- VN cũ: （……Đây cũng là để hiểu sâu hơn về Ohimitera mà.）
- Sửa: （……Đây cũng là để hiểu sâu hơn về Ohitoyo mà.）
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11; "Ohimitera" là dạng cũ của Gemini. Tiền lệ sửa trong-audit ở nhiều file đã merge.

**Key 2294** (双鉄 — nói với Nagayama)
- JP: 「社長とは、御一夜鉄道のですか？　雛衣――」
- TW: 「您說的是御一夜鐵道的社長嗎？雛衣——」
- VN cũ: 「Giám đốc là của Đường sắt Ohimitera ạ?\nHinai——」
- Sửa: 「Giám đốc là của Đường sắt Ohitoyo ạ?\nHinai——」
- Lý do: 御一夜鉄道 = "Đường sắt Ohitoyo" (tên công ty chứa cùng 御一夜 đã chốt; quyết định 21/11 ~17:30).

**Key 2555** (双鉄 — nói với Nagayama)
- JP: 「ならば日々姫はどうでしょう？　あれは、御一夜の」
- TW: 「那日日姬怎麼樣？她可是御一夜——」
- VN cũ: 「Vậy thì Hibiki thì sao ạ?\nCon bé là... của Ohimitera.」
- Sửa: 「Vậy thì Hibiki thì sao ạ?\nCon bé là... của Ohitoyo.」
- Lý do: như trên.

**Key 3034** (monologue)
- JP: 知っているなら話が早い。あのイラストマップが伝える御一夜に対する知識と愛。
- TW: 既然她知道就好辦了。從那張彩繪地圖中能看出畫手對御一夜的知識與愛。
- VN cũ: Biết rồi thì dễ nói chuyện thôi.\nKiến thức và tình yêu dành cho Ohimitera được truyền tải qua tấm bản đồ minh họa đó.
- Sửa: Biết rồi thì dễ nói chuyện thôi.\nKiến thức và tình yêu dành cho Ohitoyo được truyền tải qua tấm bản đồ minh họa đó.
- Lý do: như trên. Sau khi sửa, file không còn dòng "Ohimitera" nào.

**Key 2097** (永山)
- JP: 「いい勘ね。大正解。ハチクマライスは、旧\x%l帝鉄;#00ffc040;帝鉄%l;#;の食堂車厨房の[まかな]賄い[めし]飯が元祖なの」
- TW: 「你的第六感不錯。完全正確。蜂熊套餐可是起源自前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;餐車廚房裡的工作餐哦」
- VN cũ: 「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ mà.」
- Sửa: 「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; cũ mà.」
- Lý do: 帝鉄 = "Teitetsu"; dạng đầy đủ "Đường sắt Đế quốc" chỉ dùng trong thẻ %l ở lần xuất hiện đầu tiên (brief). Đây là lần đầu theo thứ tự trong file TOML (vị trí 44/424 — trước 2119, 2312, 2500). "Hoàng gia" (hoàng thất) sai nghĩa gốc 帝鉄 (đường sắt đế quốc); TW 帝國鐵路 xác nhận.

**Key 2119** (双鉄)
- JP: 「旧\x%l帝鉄;#00ffc040;帝鉄%l;#;の食堂車」
- TW: 「前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的餐車？」
- VN cũ: 「Toa ăn của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ ạ.」
- Sửa: 「Toa ăn của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ ạ.」
- Lý do: lần xuất hiện sau → dạng ngắn "Teitetsu" (tiền lệ: gloss 帝鉄 "Đường sắt Hoàng gia"→"Teitetsu" đã sửa trong-audit ở file khác).

**Key 2312** (永山)
- JP: 「\x%l帝鉄;#00ffc040;帝鉄%l;#;仕込みのハチクマライス。駅弁に仕立ててみたんだけどね」
- TW: 「我照著\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的蜂熊套餐做了鐵路便當」
- VN cũ: 「Là suất cơm Hachikuma đặc chế của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;.\nCô đã thử làm thành cơm hộp ga tàu đấy.」
- Sửa: 「Là suất cơm Hachikuma đặc chế của \x%l帝鉄;#00ffc040;Teitetsu%l;#;.\nCô đã thử làm thành cơm hộp ga tàu đấy.」
- Lý do: như trên.

**Key 2500** (双鉄)
- JP: 「永山さんも、それでは元は\x%l帝鉄;#00ffc040;帝鉄%l;#;に、それも、食堂車にいらしたのですか？」
- TW: 「莫非永山女士之前也在前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;工作過嗎？而且還是在餐車上？」
- VN cũ: 「Cô Nagayama, vậy ra trước đây cô cũng làm việc cho \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;,\nmà lại còn ở toa ăn sao?」
- Sửa: 「Cô Nagayama, vậy ra trước đây cô cũng làm việc cho \x%l帝鉄;#00ffc040;Teitetsu%l;#;,\nmà lại còn ở toa ăn sao?」
- Lý do: như trên.
- Ghi chú: key 1789 日ノ本帝有鐵道 → "Đường sắt Hoàng gia Hinomoto" GIỮ NGUYÊN — đây là thuật ngữ khác (帝有鐵道, tên sách), không phải 帝鉄; 日ノ本 đã đúng "Hinomoto".

**Key 2807** (monologue)
- JP: 凪が持つのは、“右田一酒造元”の六文字が白地に紺で染付られた、年季の入った[かよ]通い徳利。
- TW: 凪拿著一個白色瓷底上印著“右田一釀酒廠”六個藍字的酒壺。酒壺看起來有些年頭了。
- VN cũ: Thứ Nagi đang cầm là một chiếc bình đựng rượu lâu năm,\ncó in sáu chữ "Xưởng rượu Migita Ichishuzou" màu xanh đen trên nền trắng.
- Sửa: Thứ Nagi đang cầm là một chiếc bình đựng rượu lâu năm,\ncó in sáu chữ "Xưởng rượu Migita Ichi" màu xanh đen trên nền trắng.
- Lý do: 右田一 = "Migita Ichi" theo quy tắc đã chốt; "Migita Ichishuzou" là dạng lai (Migita Ichi + shuzou phiên âm gộp) chỉ xuất hiện ở đúng 2 dòng này toàn dự án — các file khác đều dùng "Xưởng rượu Migita Ichi" (vd. 1727, 1732). TW 釀酒廠 = xưởng rượu.

**Key 2973** (monologue)
- JP: 何故、右田一酒造元に凪が……と、疑問を感じるより先に、凪の右手が答えを示す。
- TW: 我剛還在好奇為什麼凪會在右田一釀酒廠這裡，她已經用右手回答了我這個問題。
- VN cũ: Tại sao Nagi lại ở Xưởng rượu Migita Ichishuzou……\nCòn chưa kịp thắc mắc, tay phải của Nagi đã đưa ra câu trả lời.
- Sửa: Tại sao Nagi lại ở Xưởng rượu Migita Ichi……\nCòn chưa kịp thắc mắc, tay phải của Nagi đã đưa ra câu trả lời.
- Lý do: như trên.

**Key 1778** (日々姫)
- JP: 「……ゆぅれぇでらの奥さんからのお話ですかぁ～」
- TW: 「……原來是幽靈寺夫人的事啊～」
- VN cũ: 「……Là chuyện của phu nhân chùa Yuurei đúng không ạ~」
- Sửa: 「……Là chuyện của phu nhân chùa Yurei đúng không ạ~」
- Lý do: nhất quán nội bộ — "chùa Yurei" là dạng dùng ở mọi chỗ khác trong file (2398, 2742, 2275) và toàn dự án (vd. 2048, 1788, 2716); "Yuurei" chỉ xuất hiện đúng dòng này. Furigana ゆうれいでら đọc "Yuureidera" nhưng tên chùa đã chốt dạng "Yurei" theo đa số file.

### Xưng hô

**Key 2229** (双鉄 — nói với Hibiki)
- JP: 「ん？　いや――冷静になれば、僕は勝手に日々姫を巻き込んでしまったのか？」
- TW: 「嗯？等等——冷靜下來一想，我這不是擅自把日日姬也牽扯進來了嗎？」
- VN cũ: 「Hửm? Khoan đã——bình tĩnh nghĩ lại thì,\ncó phải mình đã tự ý kéo Hibiki vào chuyện này không?」
- Sửa: 「Hửm? Khoan đã——bình tĩnh nghĩ lại thì,\ncó phải anh đã tự ý kéo Hibiki vào chuyện này không?」
- Lý do: Soutetsu nói thành lời (trong 「」) với Hibiki → tự xưng "anh" theo quy tắc đã sửa. "mình" làm chủ ngữ mệnh đề chính không thuộc ngoại lệ độc thoại nội tâm.

**Key 2590** (双鉄 — trả lời Hibiki, ngay sau câu hỏi 2593 của Hibiki)
- JP: 「判断したのだろう。ハチロクに何か不幸があれば、僕が、ナビの認める僕ではなくなると」
- TW: 「Ｎａｖｉ估計是這麼判斷的。要是八六發生什麼不測，我就不再是Ｎａｖｉ所承認的那個我了」
- VN cũ: 「Chắc cô ấy đã đánh giá tình hình rồi. Nếu Hachiroku gặp chuyện không may,\ntôi sẽ không còn là người mà Navi công nhận nữa.」
- Sửa: 「Chắc cô ấy đã đánh giá tình hình rồi. Nếu Hachiroku gặp chuyện không may,\nanh sẽ không còn là người mà Navi công nhận nữa.」
- Lý do: đang nói với Hibiki → "anh". Phát hiện bằng quét cơ học toàn bộ 112 dòng thoại Soutetsu chứa "tôi"/"mình" (chỉ còn 4 dòng, 2 dòng kia giữ nguyên — xem "Đã kiểm tra và không tính sai").

### Sai nghĩa

**Key 2534** (凪)
- JP: 「そぎゃんこつ、考えてみんとわからんと？　にーさん、頭でっかちすぎたい」
- TW: 「連這種事情都要想一想才知道，大哥哥的腦袋太不好使啦！」
- VN cũ: 「Chuyện đó, không nghĩ thì không biết sao?\nAnh hai, cứng đầu quá đấy.」
- Sửa: 「Chuyện đó, không nghĩ thì không biết sao?\nAnh hai, đầu óc nặng nề quá đấy.」
- Lý do: 頭でっかち = đầu nặng/ôm đồm suy nghĩ bằng đầu, không phải "cứng đầu" (bướng bỉnh). TW "đầu óc không linh hoạt" xác nhận hướng nghĩa.

**Key 2474** (永山)
- JP: 「確かに、一部のお客さんは泣いて喜んでくれたのよ？　けど、肝心の一般のお客さんが……こう……微妙？」
- TW: 「確實有一部分客人吃了都高興得哭了。不過關鍵是，大部分普通客人都覺得……有點微妙？」
- VN cũ: 「Đúng là có một số khách hàng vui đến phát khóc luôn đấy?\nNhưng mà, những vị khách thông thường thì lại……kiểu……hơi tế nhị?」
- Sửa: 「Đúng là có một số khách hàng vui đến phát khóc luôn đấy?\nNhưng mà, những vị khách thông thường thì lại……kiểu……hơi lưng chừng?」
- Lý do: 微妙 = lửng lơ, không rõ tốt hay dở; "tế nhị" (khéo léo, tinh tế trong ứng xử) sai hẳn nghĩa.

### Mất tiếng hít (sweep っ)

**Key 2588** (双鉄)
- JP: 「っ！！」 — TW: 「！！」
- VN cũ: 「!!」
- Sửa: 「Ư!!」
- Lý do: sweep `lost-gasp-whole` — cả dòng chỉ là tiếng hít っ + dấu câu, VN chỉ còn dấu câu nên âm bị mất hoàn toàn → thêm Ư theo quy tắc gasp. Sweep đã liệt kê đúng giá trị này, áp nguyên sau kiểm chứng JP.

**Key 2589** (双鉄)
- JP: 「っ！？」 — TW: 「！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: như trên. Sweep có đúng 2 mục cho file này, cả 2 đều áp nguyên; 0 mục sweep bỏ sót.

### Thẻ %l tự thêm

**Key 2208** (永山)
- JP: 「ん。売れたのは売れたのよ。瞬殺ってやつ、即完売。SL効果、[ハチロク,3]8620さまさま――なんだけどね」 (JP không có thẻ %l nào; 8620 chỉ có chú thích đọc [ハチロク,3])
- TW: 「嗯。賣倒是都賣出去了。可以說是瞬間賣完。這多虧了蒸汽機車效果，是託了[八六,3]８６２０的福呀」
- VN cũ: 「Ừ. Bán thì bán hết đấy. Hết sạch sành sanh trong chớp mắt.\nHiệu ứng SL, nhờ ơn \x%l8620;#00ffc040;8620%l;#; cả đấy——nhưng mà nhé.」
- Sửa: 「Ừ. Bán thì bán hết đấy. Hết sạch sành sanh trong chớp mắt.\nHiệu ứng SL, nhờ ơn 8620 cả đấy——nhưng mà nhé.」
- Lý do: VN tự thêm thẻ %l cho 8620 mà JP không có (mẫu bịa của Gemini); gỡ thẻ theo tiền lệ 機関士. Đây là dòng duy nhất trong file lệch parity thẻ (phát hiện bằng kiểm tra cơ học, không phải đọc mắt). Sau khi sửa VN còn 22 thẻ = JP.

### Lỗi nhỏ

**Key 3140** (monologue)
- JP: 熱く、柔らかく、けれども確かに押し返す。ドっ、ドっ、ドっ、ドと、激しい鼓動が伝わってくる。
- TW: 溫熱，柔軟，卻有著真實的彈性。噗通、噗通、噗通地，激烈的心跳聲傳入我的身體。
- VN cũ: Nóng hổi, mềm mại, nhưng chắc chắn đang đẩy ngược lại.\nThình thịch, thình thịch, thình thịch, nhịp đập dữ dội truyền đến.
- Sửa: Nóng hổi, mềm mại, nhưng chắc chắn đang đẩy ngược lại.\nThình thịch, thình thịch, thình thịch, thình thịch, nhịp đập dữ dội truyền đến.
- Lý do: JP có 4 nhịp tim (ドっ×3 + ド), VN chỉ còn 3 — thiếu 1 nhịp. Đối chiếu: key 3325 （ドっ、ドっ、ドっ、ドっ） VN dịch đủ 4× "Thình thịch".

## Đã kiểm tra và không tính sai

- **2254** Soutetsu tự nhủ 「過ちを改むるに憚ってはならん。ならば、むしろこちらから挨拶するようにしてみよう」 → "thà rằng mình chủ động chào hỏi trước xem sao" — GIỮ. Đây là lời tự nhủ không có người nghe (không phải đối thoại với Hibiki); "mình" ở đây là tự xưng chung, không thuộc quy tắc "anh/tôi" theo người nghe.
- **2386** Soutetsu với Nagayama: "cháu nghĩ mình cũng được thụ hưởng..." — GIỮ. "mình" là tân ngữ/phản thân, không phải chủ ngữ tự xưng; "cháu" với bà Nagayama đã đúng.
- **2995** độc thoại: "Nguy hiểm lắm để anh lấy cho, tôi chưa kịp nói xong..." — GIỮ. Nửa đầu là lời định nói ra với Hibiki ("anh" đúng), nửa sau là tường thuật ("tôi" đúng).
- **2990 / 3091 / 3244** 義兄/義妹 → "anh trai nuôi / em gái nuôi" — GIỮ. Soutetsu đúng là con nuôi trong truyện (1736 "mới được nhận nuôi", 2455 "Cậu là con nuôi mà nhỉ" — JP 養子), TW 義兄/義妹; không phải lỗi bịa "nuôi" kiểu 義≠養. (Vấn đề 義姉/義妹 "nuôi" vs "kế" đang chờ điều tra riêng không liên quan các dòng này.)
- **1766** lời Soutetsu được Hibiki trích lại: "con đường mình đang đi" — GIỮ. "mình" trong mệnh đề phụ, theo tiền lệ.
- **2043** TW ghi 「一百年！」 nhưng JP là 『うーそつーいたら はーりせんぼんのーます』 ("nuốt một nghìn cây kim") — VN theo JP, đúng theo quy tắc JP-trên-TW.
- **2547** 「あのっ――」 → "Chuyện là——": っ gắn với từ nội dung あの, không phải gasp — không thêm Ư, đúng quy tắc.
- **2569** 「えきべんっ！」 → "Cơm hộp nhà ga!": っ nhấn mạnh cuối từ nội dung, dấu ! đã giữ âm — không thêm Ư.
- **2495** 「動いてっ――」 → "đang cử động——": như trên.
- **2064** 「大当たりーーーっ！」 → "Trúng phóc rồi---!": dấu ---! đã giữ âm nhấn.
- **2246** 「は、はひっ！」 → "V, vâng!": っ trong nói lắp đã diễn bằng "V,".
- **2142** 「ふぅっ」 → "Phù.": tiếng thở dài, dấu chấm diễn sự ngắt.
- **2809** 「トっと、軽い足取りで」 → "nhẹ nhàng cất bước": âm bước chân đã diễn thành trạng từ, không mất nghĩa.
- **3108** ふふふ → "Fufufu": tiếng cười diễn thành tiếng cười, đúng quy tắc SFX.
- **2406** 「[きゃたつ,1]脚立脚立」 → "Thang xếp, thang xếp đâu rồi.": TW 梯子呢…… cũng hàm ý tìm thang — giữ.
- **2488** 「僕らには」 → "Chúng ta": dạng nhóm trung tính, đúng quy tắc.
- **3102** ぽぽぽと赤くなる → "mặt đỏ bừng lên": âm ぽぽぽ đã hàm trong "đỏ bừng", giữ.

## Lượt soát 2

- 19 tổng / 19 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.
- Mỗi bản sửa đã đối chiếu lại với JP (+ TW làm chứng thứ hai) trong lượt đọc thứ hai đầy đủ; kiểm chứng cơ học: JSON 19 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 19/19; mỗi bản sửa chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra prefix/suffix chung bằng script); khối TOML parse OK (tomllib), 19 khóa, 0 sai lệch giá trị so với JSON.
- Sweep: 2 mục (2588, 2589) — cả 2 áp nguyên sau kiểm chứng; 0 mục sweep bỏ sót (đã quét toàn file: không còn dòng っ mất tiếng nào ngoài 2 dòng này; các っ còn lại đều đã được diễn hoặc thuộc trường hợp nhấn mạnh không thêm Ư).

## Khối TOML (đã parse-verified)

```toml
[script]
"3290" = "（……Đây cũng là để hiểu sâu hơn về Ohitoyo mà.）"
"2294" = "「Giám đốc là của Đường sắt Ohitoyo ạ?\\nHinai——」"
"2555" = "「Vậy thì Hibiki thì sao ạ?\\nCon bé là... của Ohitoyo.」"
"3034" = "Biết rồi thì dễ nói chuyện thôi.\\nKiến thức và tình yêu dành cho Ohitoyo được truyền tải qua tấm bản đồ minh họa đó."
"2097" = "「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; cũ mà.」"
"2119" = "「Toa ăn của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ ạ.」"
"2312" = "「Là suất cơm Hachikuma đặc chế của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;.\\nCô đã thử làm thành cơm hộp ga tàu đấy.」"
"2500" = "「Cô Nagayama, vậy ra trước đây cô cũng làm việc cho \\x%l帝鉄;#00ffc040;Teitetsu%l;#;,\\nmà lại còn ở toa ăn sao?」"
"2807" = "Thứ Nagi đang cầm là một chiếc bình đựng rượu lâu năm,\\ncó in sáu chữ \"Xưởng rượu Migita Ichi\" màu xanh đen trên nền trắng."
"2973" = "Tại sao Nagi lại ở Xưởng rượu Migita Ichi……\\nCòn chưa kịp thắc mắc, tay phải của Nagi đã đưa ra câu trả lời."
"1778" = "「……Là chuyện của phu nhân chùa Yurei đúng không ạ~」"
"2229" = "「Hửm? Khoan đã——bình tĩnh nghĩ lại thì,\\ncó phải anh đã tự ý kéo Hibiki vào chuyện này không?」"
"2590" = "「Chắc cô ấy đã đánh giá tình hình rồi. Nếu Hachiroku gặp chuyện không may,\\nanh sẽ không còn là người mà Navi công nhận nữa.」"
"2534" = "「Chuyện đó, không nghĩ thì không biết sao?\\nAnh hai, đầu óc nặng nề quá đấy.」"
"2474" = "「Đúng là có một số khách hàng vui đến phát khóc luôn đấy?\\nNhưng mà, những vị khách thông thường thì lại……kiểu……hơi lưng chừng?」"
"2588" = "「Ư!!」"
"2589" = "「Ư!?」"
"2208" = "「Ừ. Bán thì bán hết đấy. Hết sạch sành sanh trong chớp mắt.\\nHiệu ứng SL, nhờ ơn 8620 cả đấy——nhưng mà nhé.」"
"3140" = "Nóng hổi, mềm mại, nhưng chắc chắn đang đẩy ngược lại.\\nThình thịch, thình thịch, thình thịch, thình thịch, nhịp đập dữ dội truyền đến."
```

## Kết bài

File 日々姫01_双鉄の妹: 424 dòng đã đọc, 19 dòng sai (4,5%) — thuật ngữ 11, xưng hô 2, sai nghĩa 2, mất tiếng hít 2, thẻ %l tự thêm 1, lỗi nhỏ 1. Không có lệch vị trí/xoay vòng/nhiễm chéo/mồ côi/chưa dịch/trùng key; không có dòng nào cần hỏi Hieu. File này dịch tốt hơn hẳn mặt bằng chung (chủ yếu sai tên riêng và thuật ngữ đường sắt đã chốt sau này). Khối TOML 19 khóa parse OK, 0 sai lệch.
