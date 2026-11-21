# Audit: 凪ふかみ07_少しずつ、大人に.txt.toml

- File: `凪ふかみ07_少しずつ、大人に.txt.toml` (route 07_Nagi_Fukami)
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/07_Nagi_Fukami/#U51ea#U3075#U304b#U307f07_#U5c11#U3057#U305a#U3064#U3001#U5927#U4eba#U306b.txt.toml`
- TOML md5: `7fd385c8787aa4752b730b529eb6848e`
- Kích thước: 471 dòng script. UTF-8 BOM + CRLF (977 CRLF, 0 LF-only). 1 bản sao duy nhất (không trùng file).
- Sections: info ({}), characters (2600 Fukami, 2681 Hachiroku, 2753 Nagi, 2790 Soutetsu, 2946 Hibiki), character_subs, script (471 keys), selections ({} rỗng — không có lựa chọn nào, không mất thẻ JP).
- Nội dung: Fukami thực tập/tour khoang lái, đi dạo bên sông cùng Soutetsu và Nagi, trở thành thành viên chính thức của Đường sắt Ohitoyo; kết bằng độc thoại của Soutetsu về các cô gái đang lớn dần.

## §1. Tổng quan

- Đọc: **471/471 dòng** (đối chiếu JP + TW từng dòng).
- Sai: **43/471 = 9,1%**.
- Phân loại: xưng hô 12 (gồm 2851, dòng này đồng thời bỏ 1 thẻ %l) · thuật ngữ 4 · sai nghĩa 2 · SFX 1 + gasp 2 = 3 · dấu câu 1 · thẻ %l 21.
- Hội thoại 38/303 sai; độc thoại 5/168 sai (2803, 2851, 2937, 2999, 3193).
- Không có lệch hàng / xoay vòng / nhiễm / mồ côi / chưa dịch / trùng key (xem §4).

## §2. Nguồn và cấu trúc

- CSV3: 1 bộ duy nhất, 471 dòng, section `script`, 471 key duy nhất, 0 VN trống. CSV3↔TOML: 302 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng (đã kiểm chứng bằng máy: 302 khác biệt chỉ-do-xuống-dòng, 0 khác biệt khác). CSV3 (literal `\n`) là nguồn chuẩn cho fix list.
- Comment `# JP:` trong TOML: **471/471 khớp CSV3 JP chính xác** (0 lệch). 12 comment `# JP:` còn lại nằm ở [characters] (5) và [character_subs] (7), không thuộc script.
- Thẻ %l: JP có 4 thẻ (2258 信号炎管 ×1, 2306 列車防護 ×1, 2339 車掌車 ×2); VN có 28 thẻ (4 của JP + 24 do Gemini thêm). Sau sửa, VN còn đúng 4 thẻ = JP.
- Sweep っ-gasp (`sweep-raw-gasp-wrong.json`): file này có đúng 1 entry (2084, lost-gasp-trailing) — đã áp dụng nguyên giá trị sweep. Ngoài ra audit phát hiện 1 gasp B1 mà sweep bỏ sót (2086, dòng 2 đoạn). Các dòng っ còn lại đã kiểm tra từng dòng theo ranh giới gasp đã chốt: đều là っ trong từ, っ nhấn mạnh sau từ nội dung, đã được dịch sẵn (Ư/Ưm/Hả/!?) hoặc SFX tượng thanh đã dịch — không sửa. Cụ thể giữ nguyên: 2067 はうっ→"Hauu.", 2099 あぅぅっ→"Auuu.", 2033 えっ！？→"Hả!?", 2049 ええええええっ！？→"Ể ể ể ể ể ể ể!?", 2058 だなんてっ, 2032 くださいっ, 2070 気になるっ, 2078 ああっ/見学っ, 2704 大股にっ――, 3060 伸ばしっ――, 3178 つかんだらっ, 3186–3192 SFX (ばちゃんっ→"Tùm", もにっ→"Nắn nắn", ぐいっ→"Giật mạnh", くっ→"Giật nhẹ", ぴとっ→"Áp sát").
- Quy tắc đã áp dụng: JP thắng TW; Fukami & Nagi cùng tuổi (Nagi→Fukami "bé", Fukami tự xưng "mình" với Nagi, Fukami→Nagi "cậu"); Fukami tự xưng "em" với Soutetsu/Hibiki/Hachiroku; Soutetsu tự xưng "anh" với Fukami/Nagi; 御一夜="Ohitoyo"; fa/fu ふぁ/ふあ→"phà"/"phùa"; cười (ふふっ/うふふ/んふふ) là tiếng cười, không phải tiếng rên; "Kh" cho っ tắc thanh được giữ; Ư chỉ thêm khi âm っ mất hoàn toàn.

## §3. Chi tiết theo từng dòng

### 1. Xưng hô (12 dòng, gồm 2851)

### 1461 — ふかみ (xưng hô)

- JP: 「――なことないよ。凪ちゃ――たし、も――」
- TW: 「——沒這回事。小凪——我也——」
- Cũ: 「――Không phải đâu. Nagi――chị, cũng――」
- Sửa: 「――Không phải đâu. Nagi――mình, cũng――」
- Lý do: Fukami nói với Nagi (đáp lại Nagi tự trách ở 1458). Tự xưng わたし → "mình" — hai người cùng tuổi, Fukami không bao giờ là "chị" với Nagi.

### 1879 — ふかみ (xưng hô)

- JP: 「凪ちゃんだけじゃないよ。わたしのことも支えてくれた。 / いつだって――どんなときでも、必ず支えてくれた」
- TW: 「不只是你，我也一直受雙鐵哥哥的幫助。不管什麼時候……他都一定會來幫助我」
- Cũ: 「Không chỉ riêng Nagi đâu. Anh ấy cũng đã hỗ trợ chị. / Lúc nào cũng vậy――dù trong hoàn cảnh nào, anh ấy cũng nhất định giúp đỡ chị.」
- Sửa: 「Không chỉ riêng Nagi đâu. Anh ấy cũng đã hỗ trợ em. Lúc nào cũng vậy――dù trong hoàn cảnh nào, anh ấy cũng nhất định giúp đỡ em.」
- Lý do: Fukami nói với Hibiki (trao đổi 1877/1881); "Nagi" trong câu là ngôi thứ ba. Tự xưng わたし → "em" (Fukami là "em" với Hibiki).

### 1931 — ふかみ (xưng hô)

- JP: 「知らないの？　凪ちゃん。ハンカチは、 / 人の代わりによごれるためにあるんだよ？」
- TW: 「你不懂嗎？手帕就是用來幫人擦去汙垢的」
- Cũ: 「Em không biết sao? Nagi. Khăn tay, / là để chịu bẩn thay cho con người mà?」
- Sửa: 「Cậu không biết sao? Nagi. Khăn tay, là để chịu bẩn thay cho con người mà?」
- Lý do: Fukami nói với Nagi, gọi tên trực tiếp. わたし→"Cậu" cho Nagi.

### 2058 — ふかみ (xưng hô)

- JP: 「あわわ――わたし、そんな忙しいときに、 / のんきに見学だなんてっ」
- TW: 「啊……大家都這麼忙，我居然還來添亂」
- Cũ: 「Awawa——Tớ, trong lúc bận rộn thế này, / mà lại thong dong đi tham quan.」
- Sửa: 「Awawa——Em, trong lúc bận rộn thế này, mà lại thong dong đi tham quan.」
- Lý do: Fukami nói với Soutetsu (đoạn sông, Nagi vắng mặt trong đoạn này). Tự xưng → "Em".

### 2109 — ふかみ (xưng hô)

- JP: 「うん。わたしもわかってる。だから、冗談！ / いじわる、ちょっとだけおかえししちゃった！」
- TW: 「嗯，我知道，所以我也是在逗逗你。回敬一下你的壞心眼！」
- Cũ: 「Ừm. Chị cũng biết mà. Nên là, chị đùa thôi! / Trả đũa em tội xấu tính một chút xíu thôi!」
- Sửa: 「Ừm. Mình cũng biết mà. Nên là, mình đùa thôi! Trả đũa cậu tội xấu tính một chút xíu thôi!」
- Lý do: Fukami đáp lại trò đùa của Nagi ở 2090. Tự xưng → "mình" ×2; gọi Nagi → "cậu".

### 2168 — ふかみ (xưng hô)

- JP: 「凪ちゃん、お顔にまで油ついちゃってる。 / どんなにがんばってるのか――わたし、見学できた」
- TW: 「小凪，油都沾到臉上了哦。我見識到你有多努力了」
- Cũ: 「Nagi, dầu dính lên cả mặt rồi kìa. / Em đã cố gắng đến nhường nào――chị đều thấy cả rồi.」
- Sửa: 「Nagi, dầu dính lên cả mặt rồi kìa. Cậu đã cố gắng đến nhường nào――mình đều thấy cả rồi.」
- Lý do: Fukami nói với Nagi, gọi tên trực tiếp. "Em... chị" → "Cậu... mình".

### 2189 — ふかみ (xưng hô)

- JP: 「出来たよ？　見学。ばっちりわかった」
- TW: 「很成功啊，我學到了好多」
- Cũ: 「Được rồi mà? Tham quan ấy. Chị hiểu rõ rồi.」
- Sửa: 「Được rồi mà? Tham quan ấy. Em hiểu rõ rồi.」
- Lý do: Fukami báo cáo với Soutetsu (cùng đoạn 2190/2192, đều là Fukami→Soutetsu). Tự xưng → "Em".

### 2231 — ふかみ (xưng hô)

- JP: 「凪ちゃんに気をつかわせたくなかったのに～」
- TW: 「我明明不想讓小凪替我費心的～」
- Cũ: 「Tớ không muốn làm Nagi phải bận tâm đâu mà~」
- Sửa: 「Em không muốn làm Nagi phải bận tâm đâu mà~」
- Lý do: Fukami nói với Soutetsu, Nagi là ngôi thứ ba trong câu. Tự xưng → "Em".

### 2294 — ふかみ (xưng hô)

- JP: 「だよ、ね。わたしも。――だけど、双鉄お兄さんは。 / お仕事をして、お休みの日には、必ずわたしたちのこと」
- TW: 「是啊……我也一樣。可是雙鐵哥哥無論工作還是休息，都一定陪著我們」
- Cũ: 「Đúng vậy, nhỉ. Chị cũng thế. ――Nhưng mà, anh Soutetsu thì. / Vừa phải làm việc, đến ngày nghỉ thì lúc nào cũng dành thời gian cho chúng ta」
- Sửa: 「Đúng vậy, nhỉ. Mình cũng thế. ――Nhưng mà, anh Soutetsu thì. Vừa phải làm việc, đến ngày nghỉ thì lúc nào cũng dành thời gian cho chúng ta」
- Lý do: Tiếp 2292, Fukami nói với Nagi (gọi tên). Tự xưng → "Mình".

### 2407 — 凪 (xưng hô)

- JP: 「そぎゃんとご機嫌だったら、 / よか見学ばできたとね？」
- TW: 「看你這麼開心，參觀肯定很有收穫吧？」
- Cũ: 「Tâm trạng chị vui vẻ thế này, / chắc buổi tham quan tốt đẹp lắm nhỉ?」
- Sửa: 「Tâm trạng bé vui vẻ thế này, chắc buổi tham quan tốt đẹp lắm nhỉ?」
- Lý do: Nagi nói với Fukami. Nagi→Fukami là "bé" (quy tắc đã chốt: cùng tuổi, không dùng "chị").

### 2502 — ふかみ (xưng hô)

- JP: 「それじゃあ、またね？　凪ちゃん。 / お仕事がんばって！」
- TW: 「那就再見啦，小凪。工作加油哦！」
- Cũ: 「Vậy, hẹn gặp lại nhé? Nagi. / Chúc em làm việc tốt!」
- Sửa: 「Vậy, hẹn gặp lại nhé? Nagi. Chúc cậu làm việc tốt!」
- Lý do: Fukami nói với Nagi, gọi tên trực tiếp. "em" → "cậu".

### 2851 — monologue (xưng hô + thẻ %l)

- JP: 臨時・急遽の代理車掌と自身でいっていたとおり、 / 憧れるほどの仕事ぶりとは思えなかったが――
- TW: 就像那位臨時代理列車長對自身的評價一樣，她的工作水平並不足以讓人迷上這份工作。
- Cũ: Đúng như cô ấy tự nhận mình chỉ là \x%l車掌;#00ffc040;trưởng tàu%l;#; đại diện lâm thời, khẩn cấp, / tôi không nghĩ phong cách làm việc của cô ấy lại đáng ngưỡng mộ đến thế――
- Sửa: Đúng như em ấy tự nhận mình chỉ là trưởng tàu đại diện lâm thời, khẩn cấp, tôi không nghĩ phong cách làm việc của em ấy lại đáng ngưỡng mộ đến thế――
- Lý do: (a) Bỏ thẻ %l 車掌 do Gemini thêm (JP không có thẻ này). (b) "cô ấy" → "em ấy" ×2: người được nhắc là Fukami — 凪ふかみ03 key 2058 gọi người này là 代理車掌; độc thoại quanh đây (2849/2853) nói về Fukami; độc thoại file này dùng "em ấy" cho Fukami 26 dòng vs "cô ấy" 1 dòng (chính dòng này). Phán đoán này dựa trên suy luận — cần parent kiểm chứng lại.

### 2. Thuật ngữ (4 dòng)

### 2069 — ふかみ (thuật ngữ)

- JP: 「あ！　でもでも、クマ川下りのためでもあるんです。 / 御一夜鉄道でお仕事したいの、実のところは！」
- TW: 「啊！　不過這對隈河漂流也有好處。這也是我想在御一夜鐵路工作的目的！」
- Cũ: 「A! Nhưng mà, cũng là vì chuyến xuôi dòng sông Kuma nữa ạ. / Thực ra, em muốn làm việc ở Đường sắt Ohito!」
- Sửa: 「A! Nhưng mà, cũng là vì chuyến xuôi dòng sông Kuma nữa ạ. Thực ra, em muốn làm việc ở Đường sắt Ohitoyo!」
- Lý do: 御一夜鉄道 → "Đường sắt Ohitoyo" (thuật ngữ đã chốt 19/11; sửa trong audit theo tiền lệ Grand 10, không để lại hàng chờ thống nhất).

### 2175 — 凪 (thuật ngữ)

- JP: 「ふかみちゃん！　明日から見習いじゃなくなるけん！ / 御一夜鉄道の仲間やけんね！！」
- TW: 「小深！　明天開始你就結束實習了！成為咱們御一夜鐵路的一員咧！！」
- Cũ: 「Fukami! Từ ngày mai cậu sẽ không còn là thực tập sinh nữa! / Mà là thành viên của Đường sắt Ohito rồi nha!!」
- Sửa: 「Fukami! Từ ngày mai cậu sẽ không còn là thực tập sinh nữa! Mà là thành viên của Đường sắt Ohitoyo rồi nha!!」
- Lý do: 御一夜鉄道 → "Đường sắt Ohitoyo".

### 2803 — monologue (thuật ngữ)

- JP: ほどなくバーベキュー列車が走るからだろう、 / 御一夜の町には今は、行き交う人の姿も少ない。
- TW: 可能是因為ＢＢＱ列車馬上要出發了，御一夜內現在行人十分稀少。
- Cũ: Có lẽ vì chuyến tàu BBQ sắp khởi hành, / nên thị trấn Ohimitera lúc này thưa thớt người qua lại.
- Sửa: Có lẽ vì chuyến tàu BBQ sắp khởi hành, nên thị trấn Ohitoyo lúc này thưa thớt người qua lại.
- Lý do: 御一夜の町 → "thị trấn Ohitoyo".

### 2999 — monologue (thuật ngữ)

- JP: ポーレットに頼りにされている。 / 御一夜市の観光行政に、ダイレクトな影響力を持っている。
- TW: 深美很受波萊特的器重，對御一夜市的旅遊行政也擁有直接影響力。
- Cũ: Em ấy được Paulette tin tưởng. / Có sức ảnh hưởng trực tiếp đến ngành du lịch của thành phố Ohimitera.
- Sửa: Em ấy được Paulette tin tưởng. Có sức ảnh hưởng trực tiếp đến ngành du lịch của thành phố Ohitoyo.
- Lý do: 御一夜市 → "thành phố Ohitoyo".

### 3. Sai nghĩa (2 dòng)

### 1910 — ふかみ (sai nghĩa)

- JP: 「なにが、です？」
- TW: 「什麼幸福？」
- Cũ: 「Hạnh phúc chuyện gì ạ?」
- Sửa: 「Gì cơ ạ?」
- Lý do: JP chỉ là 「なにが、です？」 ("Gì cơ ạ?"). TW 「什麼幸福？」 tự thêm 幸福 — JP không có 幸せ; JP thắng TW. VN cũ bịa "Hạnh phúc" không có cơ sở trong JP. Ngữ cảnh: Nagi 1909 nói "âm mưu đen tối bị lộ".

### 2063 — ふかみ (sai nghĩa)

- JP: 「あー、[やつしろ,2]八ツ城か[くまもと,1]隈元までおでかけできたんですねー」
- TW: 「啊……那本來是能去八代或者隈元看看了」
- Cũ: 「A, thế là mình có thể đi Yatsushiro hay Kumamoto rồi ha.」
- Sửa: 「A, thế là mình đã có thể đi Yatsushiro hay Kumamoto rồi ha.」
- Lý do: JP おでかけできた là quá khứ thể khả năng (đã có thể đi); TW 「本來是能去」 xác nhận. VN cũ thiếu "đã".

### 4. SFX / gasp (3 dòng)

### 2042 — ふかみ (SFX)

- JP: 「ふあっ！」
- TW: 「哇！」
- Cũ: 「Oa!」
- Sửa: 「Phà!」
- Lý do: JP 「ふあっ！」 → "Phà" theo quy tắc fa/fu đã chốt 19/11 (ふぁ/ふあ → "phà"/"phùa"); cùng file 2026 ふぁああ → "Phaaaa".

### 2084 — ふかみ (gasp)

- JP: 「って、日々姫さんまで～っ！？」
- TW: 「啊，連日日姬小姐都這樣？！」
- Cũ: 「Đến cả chị Hibiki cũng hùa theo á~!?」
- Sửa: 「Đến cả chị Hibiki cũng hùa theo á~Ư!?」
- Lý do: Sweep (lost-gasp-trailing): JP 「～っ！？」, VN đã dịch ～ thành "~" nhưng っ bị mất → thêm Ư. Giá trị sweep được giữ nguyên.

### 2086 — 凪 (gasp)

- JP: 「っ！！？　にーさん！！？」 / 「双鉄お兄さんっ！！？」
- TW: 「啊？！　大哥哥？！」 / 「雙鐵哥哥？！」
- Cũ: 「!!? Anh hai!!?」 / 「Anh Soutetsu!!?」
- Sửa: 「Ư!!? Anh hai!!?」 「Anh Soutetsu!!?」
- Lý do: Sweep BỎ SÓT (dòng 2 đoạn, sweep bỏ qua dòng đa đoạn để audit xử lý): đoạn 1 JP chỉ có 「っ！！？」 (gasp toàn dòng), VN "!!?" mất hoàn toàn → "Ư!!?". Đoạn 2 お兄さんっ là từ+っ nhấn mạnh, giữ nguyên.

### 5. Dấu câu (1 dòng)

### 2481 — ふかみ (dấu câu)

- JP: 「ちょっ――これ――とにかく、岸に―― / あげない、とっ！！」
- TW: 「這……總之……得先拉到岸上！！」
- Cũ: 「Khoan――chuyện này――dù sao cũng phải―― / kéo lên, bờ đã!!」
- Sửa: 「Khoan――chuyện này――dù sao cũng phải―― kéo lên bờ đã!!」
- Lý do: Dấu phẩy tách cụm động từ "kéo lên bờ"; JP 「岸に――あげない、とっ！！」.

### 6. Thẻ %l (21 dòng)

### 1486 — 双鉄 (thẻ %l)

- JP: 「……凪とハチロクは炭水車を見ている。 / 声が聞こえる距離ではないぞ」
- TW: 「……凪和八六在看煤水車的情況。距離這麼遠，她們聽不到的」
- Cũ: 「……Nagi và Hachiroku đang kiểm tra \x%l炭水車;#00ffc040;toa tiếp than nước%l;#;. / Khoảng cách này không nghe thấy tiếng đâu.」
- Sửa: 「……Nagi và Hachiroku đang kiểm tra toa tiếp than nước. Khoảng cách này không nghe thấy tiếng đâu.」
- Lý do: Bỏ thẻ %l 炭水車 do Gemini thêm; giữ nghĩa "toa tiếp than nước" thành chữ thường. JP không có thẻ này.

### 1898 — 双鉄 (thẻ %l)

- JP: 「レイルロオドのように共感がとれるわけでもないし…… / 恐らくは限られた情報内で、瞬時に判断する他にない」
- TW: 「也不能像鐵路人偶那樣依靠共鳴……恐怕只能憑藉有限的訊息，瞬間作出判斷」
- Cũ: 「Cũng không thể \x%l共感;#00ffc040;cộng cảm%l;#; như Railord được…… / Có lẽ chỉ còn cách đưa ra quyết định tức thời trong giới hạn thông tin ít ỏi.」
- Sửa: 「Cũng không thể cộng cảm như Railord được…… Có lẽ chỉ còn cách đưa ra quyết định tức thời trong giới hạn thông tin ít ỏi.」
- Lý do: Bỏ thẻ %l 共感 do Gemini thêm; giữ "cộng cảm" thành chữ thường (共感 = "cộng cảm" theo quy tắc Railord-link đã chốt).

### 1916 — 双鉄 (thẻ %l)

- JP: 「今日の凪がか？ / 油まみれでナッパ服だったではないか」
- TW: 「今天的打扮？她不是穿著一身沾滿油漬的彩頁服嗎」
- Cũ: 「Nagi của ngày hôm nay á? / Chẳng phải em ấy đang mặc bộ \x%l彩頁服;#00ffc040;đồng phục làm việc%l;#; lấm lem dầu mỡ sao?」
- Sửa: 「Nagi của ngày hôm nay á? Chẳng phải em ấy đang mặc bộ đồng phục làm việc lấm lem dầu mỡ sao?」
- Lý do: Bỏ thẻ %l 彩頁服 do Gemini thêm; giữ "đồng phục làm việc" thành chữ thường. Lưu ý: thuật ngữ thẻ 彩頁服 là do Gemini bịa — JP là ナッパ服 (đồng phục lao động), không xuất hiện ở đâu khác trong dự án; nghĩa chú thích "đồng phục làm việc" là chấp nhận được cho ナッパ服 nên giữ nguyên.

### 1935 — 双鉄 (thẻ %l)

- JP: 「ふかみは何故、車掌になろうと考えたのだ？ / みかん鉄道乗車がきっかけとは知っているが……」
- TW: 「你為什麼想成為列車長呢？我知道契機是那次乘坐橙鐵路的列車……」
- Cũ: 「Tại sao Fukami lại muốn trở thành \x%l車掌;#00ffc040;trưởng tàu%l;#; vậy? / Anh biết cơ duyên là từ lần đi tàu Đường sắt Mikan rồi nhưng mà……」
- Sửa: 「Tại sao Fukami lại muốn trở thành trưởng tàu vậy? Anh biết cơ duyên là từ lần đi tàu Đường sắt Mikan rồi nhưng mà……」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 1944 — 双鉄 (thẻ %l)

- JP: 「『赤を切る勇気』。車掌に何よりも必要なのは、 / まさにそれなのだとも、僕は、ハチロクに教わった」
- TW: 「八六也對我說過，列車長最重要的素養就是要擁有“拉紅閥的勇氣”」
- Cũ: 「『Dũng khí kéo van đỏ』. Điều \x%l車掌;#00ffc040;trưởng tàu%l;#; cần hơn bất cứ thứ gì, / chính là điều đó, anh đã được Hachiroku dạy như vậy.」
- Sửa: 「『Dũng khí kéo van đỏ』. Điều trưởng tàu cần hơn bất cứ thứ gì, chính là điều đó, anh đã được Hachiroku dạy như vậy.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2114 — 双鉄 (thẻ %l)

- JP: 「うむ。それが車掌の、最大の仕事であると」
- TW: 「嗯，那就是列車長最重要的職責」
- Cũ: 「Ừm. Đó chính là công việc quan trọng nhất của \x%l車掌;#00ffc040;trưởng tàu%l;#;.」
- Sửa: 「Ừm. Đó chính là công việc quan trọng nhất của trưởng tàu.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2132 — ふかみ (thẻ %l)

- JP: 「教えてもらったから。車掌さんでも一緒に走れるって。 / 一緒に走って、みんなの力になれるんだって」
- TW: 「因為我明白了，列車長也可以和大家一起前行，為大家貢獻力量」
- Cũ: 「Vì em đã được dạy rằng. Dù là \x%l車掌;#00ffc040;trưởng tàu%l;#; thì vẫn có thể đồng hành cùng nhau. / Đồng hành cùng nhau, và trở thành sức mạnh của mọi người.」
- Sửa: 「Vì em đã được dạy rằng. Dù là trưởng tàu thì vẫn có thể đồng hành cùng nhau. Đồng hành cùng nhau, và trở thành sức mạnh của mọi người.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2152 — 双鉄 (thẻ %l)

- JP: 「できるのであれば最初から、 / ポーレットはふかみを車掌にしているさ」
- TW: 「如果你做得到，波萊特就直接讓你當列車長了」
- Cũ: 「Nếu làm được thì ngay từ đầu, / Paulette đã để Fukami làm \x%l車掌;#00ffc040;trưởng tàu%l;#; rồi.」
- Sửa: 「Nếu làm được thì ngay từ đầu, Paulette đã để Fukami làm trưởng tàu rồi.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2197 — 日々姫 (thẻ %l)

- JP: 「一緒にだったら、機関士目指した方がよくない？ / あー、でも、接客スキルがもったいない？」
- TW: 「想和他們一起的話，選擇當司機不好嗎？啊，不過當司機是不是太浪費你的接待能力了？」
- Cũ: 「Nếu muốn ở cùng nhau thì hướng tới mục tiêu làm \x%l機関士;#00ffc040;lái tàu%l;#; chẳng phải tốt hơn sao? / A, nhưng mà, kỹ năng tiếp khách của em bỏ xó thì uổng quá nhỉ?」
- Sửa: 「Nếu muốn ở cùng nhau thì hướng tới mục tiêu làm lái tàu chẳng phải tốt hơn sao? A, nhưng mà, kỹ năng tiếp khách của em bỏ xó thì uổng quá nhỉ?」
- Lý do: Bỏ thẻ %l 機関士 do Gemini thêm; giữ "lái tàu" thành chữ thường (機関士 = "thợ lái đầu máy", dạng ngắn đối thoại "lái tàu").

### 2228 — 双鉄 (thẻ %l)

- JP: 「車掌の業務については知識でしか知らんが―― / その範囲で教えられることはもちろん、全て教えるさ」
- TW: 「我對列車長的工作也只停留在紙面上的知識——不過我會把知道的全都教給你」
- Cũ: 「Về nghiệp vụ của \x%l車掌;#00ffc040;trưởng tàu%l;#; thì anh chỉ biết qua kiến thức sách vở thôi―― / Nhưng trong phạm vi đó, tất nhiên anh sẽ dạy em tất cả những gì có thể.」
- Sửa: 「Về nghiệp vụ của trưởng tàu thì anh chỉ biết qua kiến thức sách vở thôi―― Nhưng trong phạm vi đó, tất nhiên anh sẽ dạy em tất cả những gì có thể.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2235 — ふかみ (thẻ %l)

- JP: 「きっぷを売ったり改札したり、ご案内するだけじゃなく。 / 駅員も安全を支えてるんだって――わたし、わかって」
- TW: 「我明白了站務員不只是負責賣票、檢票和指路，同時也保障著大家的安全」
- Cũ: 「Không chỉ bán vé, \x%l改札;#00ffc040;bấm vé%l;#;, hay hướng dẫn cho hành khách. / Mà nhân viên nhà ga cũng đang duy trì sự an toàn――em đã hiểu ra điều đó.」
- Sửa: 「Không chỉ bán vé, bấm vé, hay hướng dẫn cho hành khách. Mà nhân viên nhà ga cũng đang duy trì sự an toàn――em đã hiểu ra điều đó.」
- Lý do: Bỏ thẻ %l 改札 do Gemini thêm; giữ "bấm vé" thành chữ thường.

### 2240 — ふかみ (thẻ %l)

- JP: 「車掌さんのお仕事、です。運転台には入らなくても、 / 車掌さん、運転のお手伝いもするって聞いて」
- TW: 「我調查了一下列車長的職責，嗯。我聽說就算不能進駕駛台，列車長還是能給駕駛工作幫忙」
- Cũ: 「Về công việc của \x%l車掌;#00ffc040;trưởng tàu%l;#; ạ. Dù không vào buồng lái, / nhưng em nghe nói \x%l車掌;#00ffc040;trưởng tàu%l;#; cũng có thể hỗ trợ việc lái tàu.」
- Sửa: 「Về công việc của trưởng tàu ạ. Dù không vào buồng lái, nhưng em nghe nói trưởng tàu cũng có thể hỗ trợ việc lái tàu.」
- Lý do: Bỏ 2 thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2245 — 双鉄 (thẻ %l)

- JP: 「ならば焦らず、一歩一歩を積み重ねればいい。いまの / ふかみに車掌が務まらぬのは、単に列車を知らんからだ」
- TW: 「所以你不用著急，腳踏實地慢慢積累就行。你現在當不了列車長，只是因為你還不夠了解列車」
- Cũ: 「Vậy thì đừng vội, cứ từng bước một tích lũy là được. Fukami bây giờ / chưa thể đảm đương vị trí \x%l車掌;#00ffc040;trưởng tàu%l;#;, đơn giản là vì em chưa hiểu rõ về đoàn tàu thôi.」
- Sửa: 「Vậy thì đừng vội, cứ từng bước một tích lũy là được. Fukami bây giờ chưa thể đảm đương vị trí trưởng tàu, đơn giản là vì em chưa hiểu rõ về đoàn tàu thôi.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2288 — ふかみ (thẻ %l)

- JP: 「ですです。だから、わたしは。 / 車掌さんになりたいなって、思ったんです」
- TW: 「是呀是呀。所以我就想成為列車長」
- Cũ: 「Vâng vâng. Vì vậy nên, em. / Mới nghĩ là, mình muốn trở thành \x%l車掌;#00ffc040;trưởng tàu%l;#;.」
- Sửa: 「Vâng vâng. Vì vậy nên, em. Mới nghĩ là, mình muốn trở thành trưởng tàu.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2424 — 双鉄 (thẻ %l)

- JP: 「確かにな。入線のとき、黄色い線を踏み越えている者が / いれば、汽笛を鳴らさざるを得ない」
- TW: 「確實。進站時如果有人越過黃線，那就必須鳴起汽笛了」
- Cũ: 「Đúng vậy. Lúc tàu vào ga, nếu có người giẫm qua vạch vàng, / thì bắt buộc phải kéo \x%l汽笛;#00ffc040;còi hơi nước%l;#;.」
- Sửa: 「Đúng vậy. Lúc tàu vào ga, nếu có người giẫm qua vạch vàng, thì bắt buộc phải kéo còi hơi nước.」
- Lý do: Bỏ thẻ %l 汽笛 do Gemini thêm; giữ "còi hơi nước" thành chữ thường.

### 2438 — 双鉄 (thẻ %l)

- JP: 「それに、気持ちも嬉しかった。車掌を目指しているのが、 / 僕たちを支えるためだと――ともに走るためだと聞けて」
- TW: 「而且聽到你說想當列車長是為了幫助我們——為了和我們一起前行，這也很讓我高興」
- Cũ: 「Hơn nữa, anh cũng rất vui khi biết tấm lòng của em. Rằng em muốn làm \x%l車掌;#00ffc040;trưởng tàu%l;#; / là để hỗ trợ chúng anh――để cùng nhau đồng hành.」
- Sửa: 「Hơn nữa, anh cũng rất vui khi biết tấm lòng của em. Rằng em muốn làm trưởng tàu là để hỗ trợ chúng anh――để cùng nhau đồng hành.」
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 2489 — 双鉄 (thẻ %l)

- JP: 「確かに難しかろうな。機関士・運転士とは違い、 / 車掌は進路前方を見ることも出来ない」
- TW: 「這確實很困難啊。列車長和司機、駕駛員不一樣，看不到列車前方的狀況」
- Cũ: 「Chắc chắn là khó rồi. Khác với \x%l機関士;#00ffc040;lái tàu%l;#;, / \x%l車掌;#00ffc040;trưởng tàu%l;#; không thể nhìn thấy phía trước lộ trình.」
- Sửa: 「Chắc chắn là khó rồi. Khác với lái tàu, trưởng tàu không thể nhìn thấy phía trước lộ trình.」
- Lý do: Bỏ 2 thẻ %l (機関士 + 車掌) do Gemini thêm; giữ "lái tàu" và "trưởng tàu" thành chữ thường.

### 2937 — monologue (thẻ %l)

- JP: 赤を切る――異常事態が生じた時に、 / 車掌が自らの判断で、非常ブレーキをかけること。
- TW: 拉紅閥——發生異常情況時，列車長可以依照自己的判斷進行緊急剎車。
- Cũ: Kéo van đỏ――Khi có tình huống bất thường xảy ra, / \x%l車掌;#00ffc040;trưởng tàu%l;#; sẽ tự mình đưa ra quyết định kéo phanh khẩn cấp.
- Sửa: Kéo van đỏ――Khi có tình huống bất thường xảy ra, trưởng tàu sẽ tự mình đưa ra quyết định kéo phanh khẩn cấp.
- Lý do: Bỏ thẻ %l 車掌 do Gemini thêm; giữ "trưởng tàu" thành chữ thường.

### 3193 — monologue (thẻ %l)

- JP: 8620が通過する振動で、はたして川は揺れるのだろうか？ / 汽笛が響けば、川面はうわん、と波立つだろうか？
- TW: ８６２０透過時的震動會讓河流泛起水波嗎？鳴起汽笛會讓水面起伏嗎？
- Cũ: Liệu dòng sông có rung chuyển theo độ rung khi 8620 đi qua không? / Nếu \x%l汽笛;#00ffc040;còi hơi nước%l;#; vang lên, liệu mặt sông có gợn sóng lăn tăn không?
- Sửa: Liệu dòng sông có rung chuyển theo độ rung khi 8620 đi qua không? Nếu còi hơi nước vang lên, liệu mặt sông có gợn sóng lăn tăn không?
- Lý do: Bỏ thẻ %l 汽笛 do Gemini thêm; giữ "còi hơi nước" thành chữ thường.

### 2258 — ふかみ (thẻ %l)

- JP: 「だから[とうがい,1]当該列車の車掌は、停止位置から600メートルを / \x%l信号炎管;#00ffc040;信号炎管%l;#;を示しつつ、全力で走りきらなければならない」
- TW: 「所以當事列車的列車長要舉著\x%l信号炎管;#00ffc040;信號火炬%l;#;，從停車位置全力奔跑６００公尺」
- Cũ: 「Vì vậy \x%l車掌;#00ffc040;trưởng tàu%l;#; của đoàn tàu đó, phải chạy hết tốc lực 600 mét từ vị trí dừng, / đồng thời giơ cao \x%l信号炎管;#00ffc040;ống pháo hiệu%l;#;.」
- Sửa: 「Vì vậy trưởng tàu của đoàn tàu đó, phải chạy hết tốc lực 600 mét từ vị trí dừng, đồng thời giơ cao \x%l信号炎管;#00ffc040;ống pháo hiệu%l;#;.」
- Lý do: Chỉ bỏ thẻ %l 車掌 do Gemini thêm; GIỮ thẻ 信号炎管 của JP (「\x%l信号炎管;#00ffc040;ống pháo hiệu%l;#;」). Sau sửa, số thẻ VN = số thẻ JP = 1 ở dòng này.

### 2339 — 双鉄 (thẻ %l)

- JP: 「本来は、編成の最後に\x%l車掌車;#00ffc040;車掌車%l;#;という物をつけるそうだな。 / そして、\x%l車掌車;#00ffc040;車掌車%l;#;にはブレーキがついている」
- TW: 「本來車廂末尾還有一節\x%l車掌車;#00ffc040;望車%l;#;。而\x%l車掌車;#00ffc040;望車%l;#;裡有控制整輛列車的剎車」
- Cũ: 「Vốn dĩ, người ta sẽ gắn một toa gọi là \x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; ở cuối \x%l編成;#00ffc040;đoàn tàu%l;#;. / Và \x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; có trang bị phanh hãm.」
- Sửa: 「Vốn dĩ, người ta sẽ gắn một toa gọi là \x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; ở cuối đoàn tàu. Và \x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; có trang bị phanh hãm.」
- Lý do: Chỉ bỏ thẻ %l 編成 do Gemini thêm; GIỮ 2 thẻ 車掌車 của JP. Sau sửa, số thẻ VN = số thẻ JP = 2 ở dòng này.

## §4. Lệch hàng / xoay vòng / nhiễm / mồ côi

- **Lệch hàng (misalignment): 0.** Đọc toàn bộ 471 dòng, VN khớp JP/TW theo từng dòng; không có dòng VN nào thuộc về dòng JP khác.
- **Xoay vòng (rotation): 0.** Không có chuỗi dòng bị dịch chuyển vị trí.
- **Nhiễm (contamination): 0.** VN dài >25 ký tự trong file này không trùng dòng nào ở file khác (kiểm chứng bằng máy trên toàn bộ CSV3). VN trùng duy nhất trong file là 「Ồ.」 ở 2094 (JP おっと) và 2122 (JP お) — hai dòng JP khác nhau, trùng hợp hợp lệ, không phải lỗi.
- **Mồ côi (orphan): 0.** Mọi key đều có đủ JP/TW/VN.
- **Chưa dịch: 0.** 0 VN trống; VN==TW/JP duy nhất ở key 1471 (JP 「――――――」, VN 「――――――」, TW 「……」) — dòng chỉ có dấu gạch, giữ nguyên là đúng, không phải chưa dịch.
- **Trùng key: 0.** 471 key duy nhất trong cả CSV3 và TOML.

## §5. Lượt soát 2 (second pass)

Đã đọc lại **toàn bộ 43 giá trị sửa** đối chiếu với JP của từng dòng, lần thứ hai, độc lập với lượt đọc đầu:

- Tổng số fix soát lại: **43**
- Giữ nguyên sau soát 2: **41**
- Sửa lại trong soát 2: **2** — 1910 và 2042: lượt đầu viết fix thiếu cặp ngoặc 「」 (1910 「Gì cơ ạ?」, 2042 「Phà!」); đã bổ sung lại. Đây là lỗi do lúc thay toàn bộ giá trị, không phải lỗi dịch.
- Loại bỏ trong soát 2: **0**

## §6. Các mục cần Hieu / parent quyết định (không sửa)

- **Cụm 2208/2209/2212/2213/2215 (nhóm cảnh, người nghe mơ hồ — Soutetsu hay Nagi):** Fukami tự xưng không nhất quán trong một lượt nói ("T-tớ" ở 2208, "em" ở 2209/2213/2215, "chị" ở 2212); 2209 nói về Nagi ở ngôi thứ ba VÀ 2212 nói về Soutetsu ở ngôi thứ ba. Không xác định được người nghe chắc chắn nên giữ nguyên toàn bộ cụm, không sửa. Các dòng: 2208 "T-tớ", 2209 "E, em! … Nagi xấu tính quá!", 2212 "Chuyện đó, chị cũng vậy mà!", 2213 "Em cũng vậy, ạ.", 2215 "Em cũng có cùng cảm giác đó."
- **2851 (suy luận người được nhắc):** fix "cô ấy"→"em ấy" dựa trên suy luận người được nhắc là Fukami (bằng chứng: 凪ふかみ03 key 2058 gọi người này là 代理車掌; độc thoại quanh đây nói về Fukami; độc thoại file này dùng "em ấy" cho Fukami 26 dòng vs "cô ấy" 1 dòng). Parent nên kiểm chứng lại trước khi merge.
- **Các dòng giữ nguyên có chủ ý (không phải lỗi):** 2012 "Nhân viên vệ sinh xưởng" cho 庫内手 (TW 洗爐工) — chưa rõ sai nên giữ; 2449 "T, thôi đi!" (nói lắp — khớp phong cách nói lắp của file); 2523 "Anh Soutets!?" (cố tình dịch dạng cắt ngắn của おにいさ); 2157 "bọn anh" (dạng nhóm, không bị quy tắc xưng hô số ít chi phối); 2043 わひゃっ！？→"Oái!?" (tiếng kêu ngạc nhiên, không phải dòng rên, dịch ngẫu hứng).

## §7. Hàng chờ thống nhất

- **Không có mục nào để lại hàng chờ thống nhất từ file này.** 4 dòng Ohitoyo (2069, 2175, 2803, 2999) đã sửa trong audit theo tiền lệ Grand 10, không để lại.
- Ghi chú nhỏ (không phải lỗi, để parent xem có đưa vào unification pass không): 代理車掌 được dịch "trưởng tàu đại diện" ở file này (2851) nhưng "trưởng tàu đại lý" ở 凪ふかみ03 (key 2058) — hai cách dịch khác nhau cho cùng một khái niệm. Nghĩa đều giữ được, chỉ là nhất quán thuật ngữ.

## Kết bài

File 凪ふかみ07_少しずつ、大人に: 471 dòng đã đọc, **43 dòng sai (9,1%)** — chủ yếu là xưng hô (12, do quan hệ Fukami–Nagi cùng tuổi và Fukami–Soutetsu/Hibiki) và thẻ %l do Gemini thêm (21). Không có lệch hàng, xoay vòng, nhiễm, mồ côi, chưa dịch hay trùng key. Một cụm 2208–2215 để lại cho Hieu vì người nghe mơ hồ; một suy luận ở 2851 cần parent kiểm chứng. Khối TOML dưới đây đã được kiểm chứng parse (tomllib, 43 key, giá trị khớp JSON 100%).

```toml
[script]
"1461" = "「――Không phải đâu. Nagi――mình, cũng――」"
"1486" = "「……Nagi và Hachiroku đang kiểm tra toa tiếp than nước. Khoảng cách này không nghe thấy tiếng đâu.」"
"1879" = "「Không chỉ riêng Nagi đâu. Anh ấy cũng đã hỗ trợ em. Lúc nào cũng vậy――dù trong hoàn cảnh nào, anh ấy cũng nhất định giúp đỡ em.」"
"1898" = "「Cũng không thể cộng cảm như Railord được…… Có lẽ chỉ còn cách đưa ra quyết định tức thời trong giới hạn thông tin ít ỏi.」"
"1910" = "「Gì cơ ạ?」"
"1916" = "「Nagi của ngày hôm nay á? Chẳng phải em ấy đang mặc bộ đồng phục làm việc lấm lem dầu mỡ sao?」"
"1931" = "「Cậu không biết sao? Nagi. Khăn tay, là để chịu bẩn thay cho con người mà?」"
"1935" = "「Tại sao Fukami lại muốn trở thành trưởng tàu vậy? Anh biết cơ duyên là từ lần đi tàu Đường sắt Mikan rồi nhưng mà……」"
"1944" = "「『Dũng khí kéo van đỏ』. Điều trưởng tàu cần hơn bất cứ thứ gì, chính là điều đó, anh đã được Hachiroku dạy như vậy.」"
"2042" = "「Phà!」"
"2058" = "「Awawa——Em, trong lúc bận rộn thế này, mà lại thong dong đi tham quan.」"
"2063" = "「A, thế là mình đã có thể đi Yatsushiro hay Kumamoto rồi ha.」"
"2069" = "「A! Nhưng mà, cũng là vì chuyến xuôi dòng sông Kuma nữa ạ. Thực ra, em muốn làm việc ở Đường sắt Ohitoyo!」"
"2084" = "「Đến cả chị Hibiki cũng hùa theo á~Ư!?」"
"2086" = "「Ư!!? Anh hai!!?」 「Anh Soutetsu!!?」"
"2109" = "「Ừm. Mình cũng biết mà. Nên là, mình đùa thôi! Trả đũa cậu tội xấu tính một chút xíu thôi!」"
"2114" = "「Ừm. Đó chính là công việc quan trọng nhất của trưởng tàu.」"
"2132" = "「Vì em đã được dạy rằng. Dù là trưởng tàu thì vẫn có thể đồng hành cùng nhau. Đồng hành cùng nhau, và trở thành sức mạnh của mọi người.」"
"2152" = "「Nếu làm được thì ngay từ đầu, Paulette đã để Fukami làm trưởng tàu rồi.」"
"2168" = "「Nagi, dầu dính lên cả mặt rồi kìa. Cậu đã cố gắng đến nhường nào――mình đều thấy cả rồi.」"
"2175" = "「Fukami! Từ ngày mai cậu sẽ không còn là thực tập sinh nữa! Mà là thành viên của Đường sắt Ohitoyo rồi nha!!」"
"2189" = "「Được rồi mà? Tham quan ấy. Em hiểu rõ rồi.」"
"2197" = "「Nếu muốn ở cùng nhau thì hướng tới mục tiêu làm lái tàu chẳng phải tốt hơn sao? A, nhưng mà, kỹ năng tiếp khách của em bỏ xó thì uổng quá nhỉ?」"
"2228" = "「Về nghiệp vụ của trưởng tàu thì anh chỉ biết qua kiến thức sách vở thôi―― Nhưng trong phạm vi đó, tất nhiên anh sẽ dạy em tất cả những gì có thể.」"
"2231" = "「Em không muốn làm Nagi phải bận tâm đâu mà~」"
"2235" = "「Không chỉ bán vé, bấm vé, hay hướng dẫn cho hành khách. Mà nhân viên nhà ga cũng đang duy trì sự an toàn――em đã hiểu ra điều đó.」"
"2240" = "「Về công việc của trưởng tàu ạ. Dù không vào buồng lái, nhưng em nghe nói trưởng tàu cũng có thể hỗ trợ việc lái tàu.」"
"2245" = "「Vậy thì đừng vội, cứ từng bước một tích lũy là được. Fukami bây giờ chưa thể đảm đương vị trí trưởng tàu, đơn giản là vì em chưa hiểu rõ về đoàn tàu thôi.」"
"2258" = "「Vì vậy trưởng tàu của đoàn tàu đó, phải chạy hết tốc lực 600 mét từ vị trí dừng, đồng thời giơ cao \\x%l信号炎管;#00ffc040;ống pháo hiệu%l;#;.」"
"2288" = "「Vâng vâng. Vì vậy nên, em. Mới nghĩ là, mình muốn trở thành trưởng tàu.」"
"2294" = "「Đúng vậy, nhỉ. Mình cũng thế. ――Nhưng mà, anh Soutetsu thì. Vừa phải làm việc, đến ngày nghỉ thì lúc nào cũng dành thời gian cho chúng ta」"
"2339" = "「Vốn dĩ, người ta sẽ gắn một toa gọi là \\x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; ở cuối đoàn tàu. Và \\x%l車掌車;#00ffc040;toa xe trưởng tàu%l;#; có trang bị phanh hãm.」"
"2407" = "「Tâm trạng bé vui vẻ thế này, chắc buổi tham quan tốt đẹp lắm nhỉ?」"
"2424" = "「Đúng vậy. Lúc tàu vào ga, nếu có người giẫm qua vạch vàng, thì bắt buộc phải kéo còi hơi nước.」"
"2438" = "「Hơn nữa, anh cũng rất vui khi biết tấm lòng của em. Rằng em muốn làm trưởng tàu là để hỗ trợ chúng anh――để cùng nhau đồng hành.」"
"2481" = "「Khoan――chuyện này――dù sao cũng phải―― kéo lên bờ đã!!」"
"2489" = "「Chắc chắn là khó rồi. Khác với lái tàu, trưởng tàu không thể nhìn thấy phía trước lộ trình.」"
"2502" = "「Vậy, hẹn gặp lại nhé? Nagi. Chúc cậu làm việc tốt!」"
"2803" = "Có lẽ vì chuyến tàu BBQ sắp khởi hành, nên thị trấn Ohitoyo lúc này thưa thớt người qua lại."
"2851" = "Đúng như em ấy tự nhận mình chỉ là trưởng tàu đại diện lâm thời, khẩn cấp, tôi không nghĩ phong cách làm việc của em ấy lại đáng ngưỡng mộ đến thế――"
"2937" = "Kéo van đỏ――Khi có tình huống bất thường xảy ra, trưởng tàu sẽ tự mình đưa ra quyết định kéo phanh khẩn cấp."
"2999" = "Em ấy được Paulette tin tưởng. Có sức ảnh hưởng trực tiếp đến ngành du lịch của thành phố Ohitoyo."
"3193" = "Liệu dòng sông có rung chuyển theo độ rung khi 8620 đi qua không? Nếu còi hơi nước vang lên, liệu mặt sông có gợn sóng lăn tăn không?"
```
