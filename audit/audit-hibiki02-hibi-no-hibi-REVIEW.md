# Audit: 日々姫02_日々姫の日々.txt.toml — route 02_Hibiki

- File: `日々姫02_日々姫の日々.txt.toml` — route 02_Hibiki, 410 dòng script (độc thoại 186, Soutetsu 89, Hibiki 79, Kisaki 22, Saitou 17, chủ tiệm giặt ủi 10, Uragami 5, Hachiroku 1, Mayami 1).
- Nội dung: buổi sáng ở nhà xưởng ủ rượu — Soutetsu đánh bóng bồn chứa, gặp Hibiki đang phác thảo nhà xưởng lần đầu; bà Saitou nhận xét Hachiroku hợp quản lý nhiệt độ nhưng "không phải người trở thành thợ nấu rượu", đuổi Hibiki khỏi nghề vẽ vời vì sợ con bé ỷ lại "lúc nào cũng có thể quay về"; chiều đến văn phòng Kisaki — dự án "biển hiệu thành phố cũng phải đẹp", bản đồ minh họa, ký hiệu tượng hình (pictogram) của Hibiki; kết bằng Hibiki nhờ Soutetsu dạy mình làm 機関助士 (phụ lái tàu), bắt đầu từ 100kg 投炭.
- Nguồn: TOML-2 `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb02_#U65e5#U3005#U59eb#U306e#U65e5#U3005.txt.toml`, md5 `bc2003a84a0c9b38fee9be64a31ee67b` (UTF-8 BOM + CRLF). CSV3: 410 dòng, 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN==TW. VN khớp TOML tuyệt đối ngoại trừ 242 dòng TOML-2 dẹp `\n` thành khoảng trắng (CSV3 là chuẩn cho fix list). `[selections]` rỗng. Không có bản sao file này (md5 duy nhất trong cây toml2).
- Phương pháp: đọc từng dòng 410/410 đối chiếu JP + TW (JP thắng khi khác nhau); kiểm tra sweep, thẻ `%l`, lệch vị trí/chuỗi xoay/nhiễm chéo/mồ côi/chưa dịch/trùng khóa; quét máy đại từ Soutetsu và dấu ngoặc; lượt soát 2 toàn bộ fix.

## Kết quả tổng quan

**24/410 dòng sai (5,9%)** — thuật ngữ 14, bịa thêm 2, dịch sai nghĩa 1, đại từ 1, gasp 4, dấu câu 3 (dòng 2663 gộp 2 lỗi: thuật ngữ + dấu câu).

**Tổng cộng sau file này: 129 file / 5.968 dòng sai** (cơ sở 128/5.944 + 24 file này — cơ sở đã tự kiểm chứng lại với ROUTE-AUDIT.md dòng 2601).


## §1. Thuật ngữ (14 dòng)

### key 2741 — monologue
- JP: 御一夜のシンボルとして描くのならば、最適だろう。\nが――うん、と頷く日々姫の顔は、いささか硬い。
- TW: 把它當成御一夜的標誌畫在畫上，可謂再合適不過了吧。但是——日日姬雖然表示贊同，表情卻略顯生硬。
- VN cũ: Nếu vẽ như một biểu tượng của Ohimitera thì quá hợp lý rồi.\nNhưng——ừm, khuôn mặt gật đầu của Hibiki lại có phần cứng nhắc.
- VN sửa: Nếu vẽ như một biểu tượng của Ohitoyo thì quá hợp lý rồi.\nNhưng——ừm, khuôn mặt gật đầu của Hibiki lại có phần cứng nhắc.
- Lý do: 御一夜→Ohitoyo (quyết định 20/11)

### key 2111 — 双鉄
- JP: 「御一夜をもっと知りたいだけだ。日々姫が言った通り、\n掃除番を務めて初めて、見えてきた景色もある」
- TW: 「我只是想要更了解御一夜。就像你說的，我在負責清掃工作之後發現了一些新的事物」
- VN cũ: 「Anh chỉ muốn hiểu thêm về Ohimitera thôi. Đúng như Hibiki đã nói,\ncó những khung cảnh chỉ khi làm người quét dọn mới nhìn thấy được.」
- VN sửa: 「Anh chỉ muốn hiểu thêm về Ohitoyo thôi. Đúng như Hibiki đã nói,\ncó những khung cảnh chỉ khi làm người quét dọn mới nhìn thấy được.」
- Lý do: 御一夜→Ohitoyo

### key 2524 — monologue
- JP: ならば、宝生稀咲のところできっと、\n御一夜をより知るための何かと出会えるということだろう。
- TW: 也就是說，這會有助於我進一步了解御一夜。
- VN cũ: Nếu vậy, chắc chắn ở chỗ của Houshou Kisaki,\ntôi sẽ gặp được điều gì đó giúp hiểu thêm về Ohimitera.
- VN sửa: Nếu vậy, chắc chắn ở chỗ của Houshou Kisaki,\ntôi sẽ gặp được điều gì đó giúp hiểu thêm về Ohitoyo.
- Lý do: 御一夜→Ohitoyo

### key 3116 — monologue
- JP: （曇りを払い、汚れを落として、\nまっさらな目で、御一夜をゼロから知り直すのだ）
- TW: （我要在抹去濛霧、除去汙漬之後，以全新的視野從零開始重新認識御一夜）
- VN cũ: （Phủi đi vết mờ đục, gột rửa vết bẩn,\nvà dùng đôi mắt trong trẻo để tìm hiểu lại Ohimitera từ con số không.）
- VN sửa: （Phủi đi vết mờ đục, gột rửa vết bẩn,\nvà dùng đôi mắt trong trẻo để tìm hiểu lại Ohitoyo từ con số không.）
- Lý do: 御一夜→Ohitoyo

### key 2316 — 双鉄
- JP: 「御一夜市のイラストマップか」
- TW: 「這是御一夜市的彩繪地圖嗎」
- VN cũ: 「Bản đồ minh họa thành phố Ohimitera sao.」
- VN sửa: 「Bản đồ minh họa thành phố Ohitoyo sao.」
- Lý do: 御一夜市→Ohitoyo

### key 2105 — 稀咲
- JP: 「『御一夜市看板もよしプロジェクト』というのを考えた。\nピクトアイコンを、マップと看板両方に載せるんだ」
- TW: 「我們制定了“御一夜市招牌也要好計劃”，準備在地圖和招牌上統一都畫上象形圖示」
- VN cũ: 「Tôi đã nghĩ ra 『Dự án biển hiệu thành phố Ohimitera cũng phải đẹp』.\nĐưa biểu tượng tượng hình lên cả bản đồ lẫn biển hiệu.」
- VN sửa: 「Tôi đã nghĩ ra 『Dự án biển hiệu thành phố Ohitoyo cũng phải đẹp』.\nĐưa biểu tượng tượng hình lên cả bản đồ lẫn biển hiệu.」
- Lý do: 御一夜市→Ohitoyo

### key 2329 — 双鉄
- JP: 「まさしく――御一夜市、看板も良し、だな」
- TW: 「還真是——“御一夜市，招牌也要好”啊」
- VN cũ: 「Quả đúng là——thành phố Ohimitera, biển hiệu cũng phải đẹp, nhỉ.」
- VN sửa: 「Quả đúng là——thành phố Ohitoyo, biển hiệu cũng phải đẹp, nhỉ.」
- Lý do: 御一夜市→Ohitoyo

### key 3122 — monologue
- JP: （まして……稀咲は本当に、御一夜の発展を考えている）
- TW: （況且……稀咲是真心在考慮如何發展御一夜）
- VN cũ: （Hơn nữa... Kisaki thực sự đang nghĩ đến sự phát triển của Ohimitera.）
- VN sửa: （Hơn nữa... Kisaki thực sự đang nghĩ đến sự phát triển của Ohitoyo.）
- Lý do: 御一夜→Ohitoyo

### key 2165 — 双鉄
- JP: 「うむ。そうだった。その上、勉強にもなった。\nなるほどこれは、“御一夜をより知る”助けになるな」
- TW: 「是啊。而且我也學到了不少。原來如此，確實“有助於了解御一夜”啊」
- VN cũ: 「Ừm. Là vậy đấy. Hơn nữa, anh cũng học hỏi được nhiều điều.\nRa là vậy, chuyện này sẽ giúp ích cho việc "hiểu thêm về Ohimitera" đây.」
- VN sửa: 「Ừm. Là vậy đấy. Hơn nữa, anh cũng học hỏi được nhiều điều.\nRa là vậy, chuyện này sẽ giúp ích cho việc "hiểu thêm về Ohitoyo" đây.」
- Lý do: 御一夜→Ohitoyo

### key 2684 — monologue
- JP: 御一夜は、戦争で焼けた部分も少ない、古い町だ。\n無論改築もあるのだろう。
- TW: 御一夜在戰爭中損毀的部分很少，是一個古老的城市。當然，肯定也有重新修建的部分。
- VN cũ: Ohimitera là một thành phố cổ, ít bị tàn phá bởi chiến tranh.\nTất nhiên cũng có những nơi được xây dựng lại.
- VN sửa: Ohitoyo là một thành phố cổ, ít bị tàn phá bởi chiến tranh.\nTất nhiên cũng có những nơi được xây dựng lại.
- Lý do: 御一夜→Ohitoyo

### key 2364 — 日々姫
- JP: 「にぃに、御一夜の復興は、\nハチロクの復活あってのことばい」
- TW: 「阿哥，要復興御一夜，八六的復活是必不可少的」
- VN cũ: 「Anh hai, để phục hưng Ohimitera,\nsự hồi sinh của Hachiroku là không thể thiếu.」
- VN sửa: 「Anh hai, để phục hưng Ohitoyo,\nsự hồi sinh của Hachiroku là không thể thiếu.」
- Lý do: 御一夜→Ohitoyo

### key 2663 — monologue
- JP: それを活かさず腐らせたのなら、\n御一夜の復興をむしろ、遠ざけてしまうだろう。
- TW: 如果浪費了這些付出，那復興御一夜只會變得更加困難。
- VN cũ: Nếu lãng phí những nỗ lực đó,\nthì việc phục hưng Ohimitera sẽ càng xa vời hơn.」
- VN sửa: Nếu lãng phí những nỗ lực đó,\nthì việc phục hưng Ohitoyo sẽ càng xa vời hơn.
- Lý do: 御一夜→Ohitoyo; Dấu 」 thừa: JP độc thoại không có ngoặc kép — xóa 」 thừa (cùng dòng với sửa Ohitoyo)

### key 2320 — 日々姫
- JP: 「なら、御一夜をよりよく知ることだけじゃ足りません。\n\x%l8620;#00ffc040;8620%l;#;復活のためにも、もっとたくさん、努力しないと」
- TW: 「這樣的話，只是深入了解御一夜是不夠的。為了讓\x%l8620;#00ffc040;８６２０%l;#;復活，必須付出更多努力才行」
- VN cũ: 「Nếu vậy, chỉ hiểu biết sâu sắc về Ohimitera thôi là chưa đủ.\nĐể \x%l8620;#00ffc040;8620%l;#; hồi sinh, chúng ta phải nỗ lực nhiều hơn nữa.」
- VN sửa: 「Nếu vậy, chỉ hiểu biết sâu sắc về Ohitoyo thôi là chưa đủ.\nĐể \x%l8620;#00ffc040;8620%l;#; hồi sinh, chúng ta phải nỗ lực nhiều hơn nữa.」
- Lý do: 御一夜→Ohitoyo

### key 2346 — 双鉄
- JP: 「ならばいくぞ。目指すは御一夜温泉駅だ」
- TW: 「那我們開始吧。目標御一夜溫泉站」
- VN cũ: 「Vậy thì bắt đầu thôi. Mục tiêu là ga Suối nước nóng Ohimitera.」
- VN sửa: 「Vậy thì bắt đầu thôi. Mục tiêu là ga Suối nước nóng Ohitoyo.」
- Lý do: 御一夜温泉駅→Ohitoyo


## §2. Bịa thêm (2 dòng)

### key 1906 — 双鉄
- JP: 「それなら――[あに,1]義兄としてありがたい」
- TW: 「你能這麼說，作為哥哥我也很高興」
- VN cũ: 「Vậy thì——với tư cách là anh trai nuôi, tôi rất biết ơn.」
- VN sửa: 「Vậy thì——với tư cách là anh trai, tôi rất biết ơn.」
- Lý do: 義兄→'nuôi' bịa thêm; TW chỉ nói 哥哥; xem cờ Hieu

### key 2325 — 双鉄
- JP: 「無論だ。大事な[いもうと,1]義妹であるし、\n僕の帰り道も同じだからな」
- TW: 「這還用說。她可是我重要的妹妹，而且我們回去也同路」
- VN cũ: 「Tất nhiên rồi. Là cô em gái nuôi quan trọng của tôi mà,\nvới lại đường về của tôi cũng là đường đó.」
- VN sửa: 「Tất nhiên rồi. Là cô em gái quan trọng của tôi mà,\nvới lại đường về của tôi cũng là đường đó.」
- Lý do: 義妹→'nuôi' bịa thêm; TW chỉ nói 妹妹; xem cờ Hieu


## §3. Dịch sai nghĩa (1 dòng)

### key 2976 — monologue
- JP: 醸造した後の焼酎を木樽でじっくり寝かせると、\nウィスキーのような風味と色とが付け加わるのだ。
- TW: 經過釀造的燒酒置於桶中慢慢發酵，會生出威士忌般的醇香與色澤。
- VN cũ: Rượu shochu sau khi chưng cất nếu được ủ kỹ trong thùng gỗ,\nsẽ có thêm hương vị và màu sắc giống như rượu whisky.
- VN sửa: Rượu shochu sau khi ủ men nếu được ủ kỹ trong thùng gỗ,\nsẽ có thêm hương vị và màu sắc giống như rượu whisky.
- Lý do: JP 醸造 (ủ/nấu) ≠ 蒸留 (chưng cất); TW 釀造


## §4. Đại từ xưng hô (1 dòng)

### key 2062 — 双鉄
- JP: 「らしいな。何度か会っているとのことなのだが、\n僕は完全に失念していた」
- TW: 「好像是的。似乎是見過幾次面，不過我完全沒印象了」
- VN cũ: 「Có vẻ là vậy. Nghe nói đã gặp nhau vài lần, nhưng tôi hoàn toàn không nhớ gì cả.」
- VN sửa: 「Có vẻ là vậy. Nghe nói đã gặp nhau vài lần, nhưng anh hoàn toàn không nhớ gì cả.」
- Lý do: Soutetsu nói với Hibiki → 'anh' (quy tắc đã sửa 20/11); 3 dòng 'tôi' còn lại đều ở cảnh Kisaki — đúng


## §5. Gasp っ bị mất (4 dòng)

### key 1992 — クリーニング屋
- JP: 「あ……あ～～っ」
- TW: 「啊……啊～～」
- VN cũ: 「A... a~~」
- VN sửa: 「A... a~~Ư」
- Lý do: sweep lost-gasp-trailing, đã kiểm chứng JP あ……あ～～っ

### key 2002 — 日々姫
- JP: 「って！　上手かこと描けるかどーかは、\nまるっきり別次元の話やけどねぇ～っ」
- TW: 「啊！不過能不能畫出好作品，又是另一回事了～」
- VN cũ: 「Cơ mà! Việc có vẽ đẹp được hay không,\nlại là một chuyện hoàn toàn khác đấy nhé~」
- VN sửa: 「Cơ mà! Việc có vẽ đẹp được hay không,\nlại là một chuyện hoàn toàn khác đấy nhé~Ư」
- Lý do: sweep lost-gasp-trailing, đã kiểm chứng JP ねぇ～っ

### key 2374 — 日々姫
- JP: 「っ！」
- TW: 「！」
- VN cũ: 「!」
- VN sửa: 「Ư!」
- Lý do: sweep lost-gasp-whole, đã kiểm chứng JP っ！

### key 2376 — 日々姫
- JP: 「～～っ！」
- TW: 「～～！」
- VN cũ: 「~~!」
- VN sửa: 「~~Ư!」
- Lý do: sweep lost-gasp-trailing, đã kiểm chứng JP ～～っ！


## §6. Dấu câu (2 dòng)

### key 3080 — monologue
- JP: 何か……僕は……\nとんでもないことを言ったのだろうか？
- TW: 難道……我……說了什麼驚人的話嗎？
- VN cũ: Lẽ nào... mình...\nđã nói điều gì kinh khủng lắm sao?」
- VN sửa: Lẽ nào... mình...\nđã nói điều gì kinh khủng lắm sao?
- Lý do: Dấu 」 thừa: JP độc thoại không có ngoặc kép, VN thiếu 「 mở — xóa 」 thừa

### key 2905 — monologue
- JP: その全てを潰し切るため、\nたくさんの手が、今も動いてくれている。
- TW: 為了把它們全部解決，許多人正在行動。
- VN cũ: Để giải quyết triệt để tất cả,\nhiều người vẫn đang làm việc không ngừng nghỉ.」
- VN sửa: Để giải quyết triệt để tất cả,\nhiều người vẫn đang làm việc không ngừng nghỉ.
- Lý do: Dấu 」 thừa: JP độc thoại không có ngoặc kép — xóa 」 thừa

## Sweep っ-gasp — kiểm chứng trực tiếp

- Sweep có đúng 4 mục cho file này (1992, 2002, 2374, 2376) — nhận cả 4 fix, đối chiếu JP từng dòng: 1992 あ……あ～～っ, 2002 ねぇ～っ, 2374 っ！ nguyên dòng, 2376 ～～っ！ — đều là っ mất hẳn, thêm Ư theo quy tắc gasp đã khóa 20/11. (Lưu ý: giá trị sweep dùng bản TOML đã dẹp `\n` thành khoảng trắng — đã chuẩn hóa khi đối chiếu; fix trong JSON giữ `\n` gốc từ CSV3.)
- Quét máy bổ sung toàn file cho っ-gasp: các っ còn lại đều đã được diễn (1983 んんっ→"ưm!", 1957 ううんっ→"ưm", 1967 あはっ→"Aha", 2000 あははっ→"Ahaha", 1974 ふえっ→"Hể", 2017 うんっ→"Vâng!", 1936 そうっ→"đúng rồi!", 1875 小娘たいっ→"thôi!" — っ nhấn mạnh gắn từ nội dung, không phải gasp; 2990 ヒュっ→"hức", 3115 きゅっ→"Két——kéét", 3114 きぃ→"Két——") hoặc là っ trong từ (じっくり, しっかり, って...). Không còn gasp nào sweep bỏ sót.
- Hai dòng giữ nguyên theo quy tắc đã khóa, ghi chú ở đây để khỏi sửa lại: 1636 「……ぅ……ぁっ……」 → "……Ư……a……" (っ giữa dòng, sau ぁ đã diễn thành "a", TW cũng bỏ — không thêm Ư); 2130 あのっ、そのっ → "à, ừm" (từ đệm đã diễn, TW cũng chỉ giữ từ đệm).

## Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. VN đọc liền mạch theo đúng trình tự truyện; không dòng nào là bản dịch của dòng khác; không có chữ Hàn/Trung rò rỉ ngoài thẻ `%l` (quét máy: 0 ký tự CJK ngoài thẻ).
- Thẻ `%l`: số thẻ JP == số thẻ VN ở mọi dòng (quét máy, 0 lệch); không có thẻ lỗi định dạng nào trong file. Các gloss giữ nguyên theo quyết định: もろみ→"Cơm rượu", 杜氏→"trưởng hầm rượu", エアクラ→"Aircra", 8620 giữ nguyên, 機関助士→"phụ lái tàu", 機関士→"người lái tàu", 投炭→"xúc than".
- Đại từ Soutetsu (quét máy toàn bộ thoại 双鉄): "anh" với Hibiki đúng toàn file; "tôi" chỉ ở 3 dòng cảnh Kisaki (2023, 1906, 2325 — đúng) và 1 dòng sai đã sửa (2062, cảnh Hibiki); "cháu" với bà Saitou (2122, 2175 — đúng). Độc thoại dùng "tôi" nhất quán (giọng người kể). Hibiki "em" với Soutetsu, "chị" với Kisaki/Hachiroku, "cháu" với chủ tiệm giặt ủi — đúng. Kisaki không có dòng tự xưng số ít nào trong file (chỉ có "chúng ta" cho ボクら ở 2106). Mayami gọi Soutetsu "Sou-chan" (1971), Hachiroku gọi "ngài Soutetsu" (2157) — đúng.

## Không sửa (đã kiểm, giữ nguyên có lý do)

- "Migita System" ×2 (2671, 2516) — thuộc đợt thống nhất (Migita System→Migita Ichi), KHÔNG sửa trong audit.
- 2108 「引き取られたばかりの僕が」 → "được nhận nuôi" — JP + TW (領養) đều xác nhận, giữ nguyên. (Dòng này là bằng chứng Soutetsu được nhận nuôi — xem cờ Hieu về 義兄/義妹.)
- 2990 ヒュっ → "hức" — SFX hít vào, diễn ngẫu hứng theo nhân vật + ngữ cảnh (quy tắc Hieu 22:05), giữ nguyên.
- 2082 あのっ―― → "là——" — từ đệm あの bỏ, dấu gạch ngang giữ nhịp ngập ngừng; TW giữ 那個 nhưng đây là từ đệm, không phải âm thanh — giữ nguyên.
- Chủ tiệm giặt ủi gọi Hibiki "cô" (2078, 2169, 2312) — Hibiki là nữ thiết kế trẻ làm việc chuyên nghiệp, "cô" lịch sự và nhất quán toàn file — giữ nguyên.
- 2976 đã sửa (xem §3); các dòng còn lại về rượu/shochu đã đối chiếu kỹ: ステンタンク→"bồn thép không gỉ", かめ/甕→"chum vại", 杜氏→"trưởng hầm rượu" — đúng.
- 2259 ねぇねぇ → "chị hai" (chị gái Hibiki, TW 阿姐) — đúng. 1960 茶玉クリーニング → "Tiệm giặt ủi Chadama" (theo JP; TW 岡留 khác JP, JP thắng) — đúng.

## Cờ chờ Hieu (không tự quyết)

1. **1906 + 2325 — 義兄/義妹: "anh rể/em dâu" hay "anh trai/em gái"?** Soutetsu dùng 義兄 (1906) và 義妹 (2325) cho chính mình và Hibiki — trong khi hai người là anh em sinh đôi cùng nhà. TW dịch trơn thành 哥哥/妹妹. Audit đã bỏ "nuôi" theo quy tắc 義 (TW không giữ 義/養) → "anh trai"/"em gái". NHƯNG key 2108 cho thấy Soutetsu được nhận nuôi (引き取られた, TW 領養), nên 義 ở đây có thể là cố ý (anh em nuôi / anh rể hàm ý Kisaki×Hibiki như một cặp). Hieu quyết: giữ "anh trai/em gái" như đã sửa, hay đổi sang "anh rể/em dâu"?
2. **2349 + 2713 — gloss 機関助士/機関士:** "phụ lái tàu" / "người lái tàu" (theo dạng ngắn đã quyết cho 機関士 là "lái tàu"); TW dùng 司爐 ("người đốt lò") — vai trò này trong ngữ cảnh 投炭 (xúc than) đúng là người đốt lò. Giữ "phụ lái tàu" hay đổi theo TW? Có thể gộp vào đợt thống nhất.
3. **2512 — 投炭 gloss "xúc than":** đã có trong hàng đợi thống nhất (投炭 gloss split) — ghi nhận, không sửa ở đây.

## Lượt soát 2

**24/24/0/0** — đọc lại toàn bộ 24 giá trị fix đối chiếu JP (kể cả 3 fix dấu câu và fix gộp 2663): 24 xác minh lại, 0 bỏ, 0 sửa. JSON 24 mục, khối TOML 24 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 24/24.

## Khối TOML (đã kiểm parse bằng tomllib)

```toml

[script]
"2741" = "Nếu vẽ như một biểu tượng của Ohitoyo thì quá hợp lý rồi.\\nNhưng——ừm, khuôn mặt gật đầu của Hibiki lại có phần cứng nhắc."
"2111" = "「Anh chỉ muốn hiểu thêm về Ohitoyo thôi. Đúng như Hibiki đã nói,\\ncó những khung cảnh chỉ khi làm người quét dọn mới nhìn thấy được.」"
"2524" = "Nếu vậy, chắc chắn ở chỗ của Houshou Kisaki,\\ntôi sẽ gặp được điều gì đó giúp hiểu thêm về Ohitoyo."
"3116" = "（Phủi đi vết mờ đục, gột rửa vết bẩn,\\nvà dùng đôi mắt trong trẻo để tìm hiểu lại Ohitoyo từ con số không.）"
"2316" = "「Bản đồ minh họa thành phố Ohitoyo sao.」"
"2105" = "「Tôi đã nghĩ ra 『Dự án biển hiệu thành phố Ohitoyo cũng phải đẹp』.\\nĐưa biểu tượng tượng hình lên cả bản đồ lẫn biển hiệu.」"
"2329" = "「Quả đúng là——thành phố Ohitoyo, biển hiệu cũng phải đẹp, nhỉ.」"
"3122" = "（Hơn nữa... Kisaki thực sự đang nghĩ đến sự phát triển của Ohitoyo.）"
"2165" = "「Ừm. Là vậy đấy. Hơn nữa, anh cũng học hỏi được nhiều điều.\\nRa là vậy, chuyện này sẽ giúp ích cho việc \"hiểu thêm về Ohitoyo\" đây.」"
"2684" = "Ohitoyo là một thành phố cổ, ít bị tàn phá bởi chiến tranh.\\nTất nhiên cũng có những nơi được xây dựng lại."
"2364" = "「Anh hai, để phục hưng Ohitoyo,\\nsự hồi sinh của Hachiroku là không thể thiếu.」"
"2663" = "Nếu lãng phí những nỗ lực đó,\\nthì việc phục hưng Ohitoyo sẽ càng xa vời hơn."
"2320" = "「Nếu vậy, chỉ hiểu biết sâu sắc về Ohitoyo thôi là chưa đủ.\\nĐể \\x%l8620;#00ffc040;8620%l;#; hồi sinh, chúng ta phải nỗ lực nhiều hơn nữa.」"
"2346" = "「Vậy thì bắt đầu thôi. Mục tiêu là ga Suối nước nóng Ohitoyo.」"
"1906" = "「Vậy thì——với tư cách là anh trai, tôi rất biết ơn.」"
"2325" = "「Tất nhiên rồi. Là cô em gái quan trọng của tôi mà,\\nvới lại đường về của tôi cũng là đường đó.」"
"2976" = "Rượu shochu sau khi ủ men nếu được ủ kỹ trong thùng gỗ,\\nsẽ có thêm hương vị và màu sắc giống như rượu whisky."
"2062" = "「Có vẻ là vậy. Nghe nói đã gặp nhau vài lần, nhưng anh hoàn toàn không nhớ gì cả.」"
"1992" = "「A... a~~Ư」"
"2002" = "「Cơ mà! Việc có vẽ đẹp được hay không,\\nlại là một chuyện hoàn toàn khác đấy nhé~Ư」"
"2374" = "「Ư!」"
"2376" = "「~~Ư!」"
"3080" = "Lẽ nào... mình...\\nđã nói điều gì kinh khủng lắm sao?"
"2905" = "Để giải quyết triệt để tất cả,\\nhiều người vẫn đang làm việc không ngừng nghỉ."
```

## Kết bài

File 日々姫02_日々姫の日々.txt.toml: 410 dòng đã đọc hết, 24 dòng sai (5,9%) — chủ yếu là thuật ngữ Ohimitera cũ (14 dòng, tức 58% số lỗi) và 4 gasp từ sweep, cộng 2 dòng bịa "nuôi", 1 dòng dịch sai quá trình ủ rượu, 1 đại từ Soutetsu sai đối tượng, 3 dấu 」 thừa. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Đại từ Soutetsu đã quét máy xác minh: chỉ 1 lỗi duy nhất (2062). 3 cờ chờ Hieu (nghĩa 義兄/義妹, gloss 機関助士, gloss 投炭) đã ghi ở trên — không tự quyết.
