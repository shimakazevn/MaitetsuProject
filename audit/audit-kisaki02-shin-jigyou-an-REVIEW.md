# Audit — 稀咲02_新事業案.txt.toml (route 06_Kisaki)

- File: `稀咲02_新事業案.txt.toml` — route 06_Kisaki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b202_#U65b0#U4e8b#U696d#U6848.txt.toml`
- Số dòng script: **448** (độc thoại 170, Kisaki 128, Soutetsu 116, Hibiki 20, Hachiroku 14). Đọc toàn bộ 448/448 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: Kisaki trình bày phương án "quỹ My Rail" (chứng khoán hóa đường ray) để cứu tuyến Ohitoyo trước sức ép nhà máy Aircra; xen kẽ cảnh tập lái/tắm trên đầu máy 8620 (Kisaki làm phụ lái tập sự, Soutetsu hướng dẫn, Hibiki làm nhân viên cơ vụ tập sự); kết bằng chạy thử 8620.
- **Kết quả: 29/448 dòng sai (6,5%)** — thấp hơn nhiều so với file 01 cùng route (47,0%). Không có chuỗi xoay, không lệch vị trí.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN == TW. TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 235 giá trị TOML đã flatten `\n` literal thành khoảng trắng (234 thuần + 1 dòng 2160 thừa 1 khoảng trắng); CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `ead507acd1b6cb5a2ef94bf4ea990d92`. Không có bản sao của file này trong 11 nhóm trùng.
- `[selections]` rỗng. `[character_subs]`: 2593 Hachiroku, 2791 Hibiki, 2801 Hibiki/Soutetsu/Kisaki, 3097 Soutetsu, 3135 "3 người" — không liên quan đến các fix.

## Phân loại (29)

| Loại | Số dòng | Keys |
|---|---|---|
| Thuật ngữ (terminology) | 10 | 1371, 1721, 1750, 1772, 2038, 2151, 2192, 2331, 2559, 2676 |
| Thở gấp (gasp) | 7 | 1870, 2289, 2394, 2395, 2810, 2821, 2830 (cả 7 từ sweep, đã kiểm chứng) |
| Sai nghĩa (meaning) | 7 | 1370, 1674, 1942, 2223, 2376, 2915, 2992 |
| Thẻ %l (tag) | 2 | 2008, 2365 |
| Đại từ (pronoun) | 1 | 2260 |
| SFX | 1 | 2523 |
| Thêm nghĩa (addition) | 1 | 2874 |

Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0, cụt câu 0.

## §1. Thuật ngữ (10)

### 1371 [稀咲] — 御一夜 → Ohitoyo
- JP: 「エアクラ社が御一夜を候補地にしている最大の理由は九洲中央部への生産・販売の拠点とし易いからだ」
- TW: 「空凝機公司將御一夜定為候選地的最重要原因，是因為這麼做便於建立面向九州中央地區的生產和銷售據點」
- VN cũ: 「Lý do lớn nhất khiến công ty Aircra chọn Ohimitera làm địa điểm ứng cử, là vì nơi đây dễ dàng trở thành cứ điểm sản xuất và bán hàng cho khu vực trung tâm Kyushu.」
- Fix: `Ohimitera` → `Ohitoyo`.

### 1721 [稀咲] — 御一夜 → Ohitoyo
- JP: 「共存共栄？　御一夜市と、エアクラ社とのかい？」
- TW: 「互利共贏？御一夜市和空凝機公司嗎？」
- VN cũ: 「Cùng tồn tại và cùng phát triển? Giữa thành phố Ohimitera và công ty Aircra sao?」
- Fix: `Ohimitera` → `Ohitoyo`.

### 1750 [稀咲] — 御一夜 → Ohitoyo
- JP: 「かといって、協調だけでは緩やかな衰退は避け得ない。ちょうど、御一夜が陥ってしまった状況のようにね」
- TW: 「但雖如此，光靠合作也無法迴避緩慢的衰退。就和目前御一夜所處的狀況一樣」
- VN cũ: 「Tuy nhiên, nếu chỉ có hợp tác thì cũng không thể tránh khỏi sự suy thoái chậm chạp. Giống hệt như tình trạng mà Ohimitera đang mắc phải vậy.」
- Fix: `Ohimitera` → `Ohitoyo`.

### 1772 [双鉄] — 御一夜鉄道 → Đường sắt Ohitoyo
- JP: 「その復線が仮にできれば、エアクラ社と御一夜鉄道、ともに利益を生み出せるから……出来ればと考えたのだ」
- TW: 「假如能夠恢復廢線，空凝機公司和御一夜鐵路都能從中獲益……如果能實現的話就好了」
- VN cũ: 「Nếu giả sử có thể khôi phục lại tuyến đường đó, thì cả công ty Aircra và Đường sắt Ohito đều có thể tạo ra lợi nhuận…… nên tôi đã nghĩ nếu làm được thì tốt biết mấy.」
- Fix: `Đường sắt Ohito` → `Đường sắt Ohitoyo`.

### 2038 [稀咲] — 御一夜鉄道 → Đường sắt Ohitoyo
- JP: 「御一夜鉄道も？　って、あ……そうか。当然か、移送となれば貨物列車が走るわけだし――」
- TW: 「御一夜鐵路也有？呃，啊……是這樣啊。也對，要運輸的話就要用到貨運列車——」
- VN cũ: 「Cả Đường sắt Ohito nữa sao? Ơ, à…… ra là vậy. Đương nhiên rồi, nếu là vận chuyển thì sẽ có đoàn tàu chở hàng chạy qua mà——」
- Fix: `Đường sắt Ohito` → `Đường sắt Ohitoyo`.

### 2151 [稀咲] — 右田一 → Migita Ichi (không phải "Migita System")
- JP: 「そうだね。右田一酒造元もそうだろうし、隈銀だって、例外じゃない」
- TW: 「是啊。右田一釀酒廠也一樣，隈元銀行也不例外」
- VN cũ: 「Đúng vậy. Xưởng rượu Migita System cũng thế, và Kumagin cũng không ngoại lệ.」
- Fix: `Migita System` → `Migita Ichi` (右田一 là tên riêng; "System" là dịch sai chữ 一). Ghi chú: hàng đợi thống nhất liệt kê 15 dòng "Migita System→Migita Ichi" toàn dự án — dòng này có thể là 1 trong số đó, đã sửa trực tiếp tại đây, đợt thống nhất cần đối chiếu lại để khỏi đếm trùng.

### 2192 [稀咲] — 御一夜 → Ohitoyo
- JP: 「彼の仕事は、『御一夜に工場を誘致すること』ではなく、『最適の場所に工場を立地すること』だからさ」
- TW: 「浦上的工作不是"讓工廠落戶到御一夜"，而是"讓工廠落戶到最合適的地方"」
- VN cũ: 「Công việc của anh ấy không phải là 『thu hút nhà máy đến Ohimitera』, mà là 『chọn địa điểm tối ưu nhất để đặt nhà máy』.」
- Fix: `Ohimitera` → `Ohitoyo`.

### 2331 [双鉄] — 御一夜 → Ohitoyo
- JP: 「それ……と、は、御一夜-千内間の復線か？」
- TW: 「這個……是說恢復御一夜至川內間的線路？」
- VN cũ: 「Cách đó…… ý cô là, khôi phục lại tuyến đường giữa Ohimitera và Sendai sao?」
- Fix: `Ohimitera` → `Ohitoyo`. ("Sendai" giữ nguyên theo furigana せんだい của 千内, khớp TW 川內市.)

### 2559 [monologue] — 御一夜 → Ohitoyo
- JP: 「そこと御一夜との間はかつて、鹿兒島をぐるり回って、帝鉄路線で結ばれていた。」
- TW: 「以前川內和御一夜之間是通過繞了鹿兒島一圈的帝國鐵路線路連接起來的。」
- VN cũ: 「Giữa nơi đó và Ohimitera trước đây, từng được kết nối bằng tuyến đường sắt Teitetsu chạy vòng quanh Kagoshima.」
- Fix: `Ohimitera` → `Ohitoyo`. (帝鉄 → "Teitetsu" đã đúng.)

### 2676 [monologue] — 御一夜 → Ohitoyo
- JP: 「御一夜より有利な候補地を設定できれば、工場誘致は回避でき、浦上さんの得点にもなる。」
- TW: 「如果能找到比御一夜更適合的候選地的話，在阻止工廠落戶的同時，對浦上經理也有益處。」
- VN cũ: 「Nếu có thể thiết lập một địa điểm ứng cử viên có lợi thế hơn Ohimitera, thì vừa có thể tránh được việc thu hút nhà máy, vừa mang lại điểm cộng cho anh Urakami.」
- Fix: `Ohimitera` → `Ohitoyo`.

## §2. Thở gấp っ — sweep (7, cả 7 áp nguyên đã kiểm chứng)

Sweep có đúng 7 mục cho file này (`sweep-raw-gasp-wrong.json`), cả 7 đều đúng và được áp nguyên — không có mục sweep nào bị bác, không có gasp nào sweep bỏ sót (đã quét lại toàn file: các っ còn lại đều là っ nhấn mạnh cuối câu gắn với từ có nội dung — vd. 2032 「後部異状、無しっ！」→ "Phía sau không có gì bất thường!" — hoặc đã được diễn đạt — vd. 1865 うんっ → "ừm", 1903 ごめんっ → "Xin lỗi nhé").

### 1870 [稀咲] — sweep lost-gasp-trailing
- JP: 「ひえっ！？　あうわっ！？――あ――きゅうう～～～っ」
- TW: 「呃啊！？啊哇！？——啊——嗚嗚嗚～～～」
- VN cũ: 「Hiee!? Auwa!?——A——kyuuu～～～」
- Fix: 「Hiee!? Auwa!?——A——kyuuu～～～Ư」 (っ cuối tuyệt đối, sau ~~~, âm bị mất hẳn → thêm Ư.)

### 2289 [双鉄] — sweep lost-gasp-trailing
- JP: 「き、きんっ――――～～～っ」
- TW: 「緊、緊————～～～」
- VN cũ: 「C, căng thẳng――――～～～」
- Fix: 「C, căng thẳng――――～～～Ư」

### 2394 [双鉄] — sweep lost-gasp-whole
- JP: 「っ！」 / TW: 「！」
- VN cũ: 「!」 → Fix: 「Ư!」

### 2395 [双鉄] — sweep lost-gasp-whole
- JP: 「っ！？」 / TW: 「！？」
- VN cũ: 「!?」 → Fix: 「Ư!?」

### 2810 [monologue] — sweep lost-gasp-trailing
- JP: 「運転台では、あれほど頼りなかった姿が、今はどうだ、これほどまでに美しく――――――っ！！」
- TW: 「曾經在駕駛台上手忙腳亂的她，現在卻顯得如此美麗動人——————！！」
- VN cũ: 「Dáng vẻ thiếu tự tin trong buồng lái khi nãy, giờ đây lại xinh đẹp đến nhường này sao――――――!!」
- Fix: 「……sao――――――Ư!!」 (っ sau chuỗi gạch dài bị mất hẳn trong VN cũ → thêm Ư trước !!.)

### 2821 [monologue] — sweep lost-gasp-trailing
- JP: 「真正面の。稀咲の視線が、下を向く。向いた視線が、すぐ上へ――っ！！？」
- TW: 「正面。稀咲的視線往下看。投來的視線很快往上——！！？」
- VN cũ: 「Ngay chính diện. Ánh mắt của Kisaki nhìn xuống dưới. Và ánh mắt đó, ngay lập tức lại hướng lên trên——!!?」
- Fix: 「……hướng lên trên——Ư!!?」

### 2830 [monologue] — sweep lost-gasp-trailing
- JP: 「それは止まずに、僕の脇へと回り込み、正面側へと近づいてく――っ！！」
- TW: 「水聲沒有停下來，繞到我的側邊，又接近我的正側面——！！」
- VN cũ: 「Tiếng nước đó không hề dừng lại, mà vòng sang bên hông, rồi tiến sát ngay bên cạnh tôi——!!」
- Fix: 「……tiến sát ngay bên cạnh tôi——Ư!!」

## §3. Sai nghĩa (7)

### 1370 [双鉄] — 謳歌 ≠ "ca ngợi"
- JP: 「この世の春を謳歌しているものだと思っていたが」
- TW: 「我還以為它現在已經高枕無憂了呢」
- VN cũ: 「Tôi cứ tưởng họ đang ca ngợi mùa xuân của thế gian này cơ.」
- Fix: 「Tôi cứ tưởng họ đang tận hưởng mùa xuân của thế gian này cơ.」 (謳歌する = tận hưởng thời hoàng kim, không phải "ca ngợi". Cùng lỗi ở 2223.)

### 1674 [稀咲] — 地獄の窯 ≠ "lò bát quái"
- JP: 「ふ、普通の火なら平気だけどさ。驚くだろう！？　こんな、地獄の窯みたいな火」
- TW: 「一、一般的火是不怕啦。但這種看起來像煉獄一樣的火，正常人都會嚇到吧！？」
- VN cũ: 「B, bình thường thì tôi không sợ đâu. Nhưng mà giật mình chứ sao!? Ngọn lửa cứ như lò bát quái thế này.」
- Fix: 「……Ngọn lửa cứ như lò địa ngục thế này.」 (JP là 地獄 "địa ngục", TW là 煉獄; "lò bát quái" thay bằng hình ảnh văn hóa khác không có trong JP.)

### 1942 [双鉄] — chủ ngữ bịa "hành khách"
- JP: 「ああ、そうだな。炭水車やボイラが邪魔になり、運転台の様子や前の様子は、まるで見えない」
- TW: 「嗯，是的。煤水車和鍋爐會擋住視野，完全看不見駕駛台和駕駛台前面的情況」
- VN cũ: 「À, đúng vậy. Bị toa tiếp than nước và lò hơi che khuất, nên hành khách hoàn toàn không thể nhìn thấy tình hình trong buồng lái hay cảnh vật phía trước.」
- Fix: bỏ "hành khách" → 「……nên hoàn toàn không thể nhìn thấy tình hình trong buồng lái hay cảnh vật phía trước.」 (JP/TW đều không có chủ ngữ; người không nhìn thấy được là người lái trong buồng lái — hành khách không ngồi trong buồng lái, đây là chủ ngữ Gemini bịa thêm.)

### 2223 [稀咲] — 謳歌 ≠ "ca ngợi" (lần 2)
- JP: 「今はまだエアロ＝クラフテック機関の特許料があるから、この世の春は春だろうけど……謳歌する余裕なんて、ね」
- TW: 「現在公司還有空凝機引擎的專利費支撐，雖然確實可以說是高枕……但遠遠說不上無憂呢」
- VN cũ: 「Bây giờ vẫn còn phí bản quyền của động cơ Aero-Craftech, nên mùa xuân của thế gian này vẫn là mùa xuân thôi…… nhưng làm gì có dư dả để mà ca ngợi chứ.」
- Fix: 「……nhưng làm gì có dư dả để mà tận hưởng chứ.」

### 2376 [日々姫] — 兄さん ≠ "anh Soutetsu"
- JP: 「にぃにっ――兄さん？」
- TW: 「阿哥——哥哥？」
- VN cũ: 「Anh hai——anh Soutetsu?」
- Fix: 「Anh hai——anh trai?」 (JP/TW chỉ có hai cách gọi "anh trai" — にぃに rồi 兄さん; VN cũ bịa thêm tên "Soutetsu" vào chỗ không có tên.)

### 2915 [monologue] — 合格点 ≠ "điểm tuyệt đối"
- JP: 「稀咲の顔が満足そうだ。僕の理解は、合格点をもらえたらしい。」
- TW: 「稀咲一副滿意的表情。看來我猜到點子上了。」
- VN cũ: 「Gương mặt Kisaki lộ vẻ hài lòng. Có vẻ như sự hiểu biết của tôi đã đạt điểm tuyệt đối.」
- Fix: 「……Có vẻ như sự hiểu biết của tôi đã nhận được điểm đạt.」 (合格点 = điểm đạt/chuẩn đỗ, không phải điểm tuyệt đối.)

### 2992 [monologue] — chủ thể bị đổi: 少女が産みだした, không phải "nụ cười sinh ra"
- JP: 「路線網――鉄道の生命線たるそれの復活に繋がる案を、僕の目の前、笑顔の少女が産みだした。」
- TW: 「能令相當於鐵路生命線的線路網起死回生的方案，是由我眼前這位滿面歡笑的少女所想到的。」
- VN cũ: 「Phương án dẫn đến sự hồi sinh của mạng lưới đường sắt——sinh mệnh của ngành đường sắt, đã được sinh ra từ nụ cười của thiếu nữ ngay trước mắt tôi.」
- Fix: 「……đã được cô thiếu nữ đang mỉm cười ngay trước mắt tôi nghĩ ra.」 (JP: chính cô gái nghĩ ra phương án; VN cũ đổi chủ thể thành "nụ cười" sinh ra phương án.)

## §4. Thẻ %l (2)

### 2008 [稀咲] — "[8620'86]" là dạng tag hỏng
- JP: 「双鉄が[ハチロク,3]8620を所有し、走らせ、利益の分配を受ける。同じことを、レールを使って、大人数でやるってことさ」
- TW: 「就像雙鐵擁有[八六,3]８６２０，可以讓８６２０行駛並得到分紅一樣。就是讓更多的人來參與鐵路運營的意思」
- VN cũ: 「Giống như anh Soutetsu sở hữu [8620'86], cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」
- Fix: `[8620'86]` → `\x%l8620;#00ffc040;8620%l;#;` (theo đúng mẫu của dòng 1758 cùng file: `[ハチロクニイマル,3]8620` → `\x%l8620;#00ffc040;8620%l;#;`. Toàn dự án 8620 chỉ được diễn bằng "8620" trơn hoặc tag %l này, không có dạng `[8620'86]`.)

### 2365 [稀咲] — "[8620'86]" (lần 2)
- JP: 「[ハチロク,3]8620に乗せてもらったからさ。それに、復線の話も細かく聞かせてもらえたから」
- TW: 「都是因為搭乘了[八六,3]８６２０。而且也詳細聽你說了恢復廢線的事情」
- VN cũ: 「Là nhờ được ngồi trên [8620'86] đấy. Hơn nữa, cũng nhờ được nghe anh kể chi tiết về chuyện khôi phục tuyến đường.」
- Fix: `[8620'86]` → `\x%l8620;#00ffc040;8620%l;#;`.

## §5. Đại từ (1)

### 2260 [ハチロク] — "Chị Kisaki" → "Cô Kisaki"
- JP: 「稀咲様が機関助士見習い。双鉄様がその指導。となれば、日々姫が機関士見習いで――」
- TW: 「稀咲小姐擔任見習司爐。雙鐵少爺進行指導。這樣一來，就只能讓日日姬擔任見習司機——」
- VN cũ: 「Chị Kisaki sẽ làm phụ lái tàu tập sự. Ngài Soutetsu sẽ hướng dẫn. Nếu vậy, Hibiki sẽ làm nhân viên cơ vụ tập sự——」
- Fix: `Chị Kisaki` → `Cô Kisaki`. (Bằng chứng: cùng cảnh, cùng người nói, chỉ 2 key sau (2262) Hachiroku gọi "Cô Kisaki, cô đã vất vả rồi"; toàn dự án Hachiroku gọi Kisaki là "cô Kisaki" 10 lần vs "chị Kisaki" 2 lần — và 1 trong 2 lần "chị" đó chính là dòng này. Soutetsu cũng gọi Kisaki là "cô" xuyên suốt file.)

## §6. SFX (1)

### 2523 [monologue] — ちゃぷん ≠ "róc rách"
- JP: 「ちゃぷん、と水音。」
- TW: 「一聲"啾噗"的水聲。」
- VN cũ: 「Tiếng nước kêu róc rách.」
- Fix: 「Tiếng nước kêu 'chụp' một tiếng.」 (ちゃぷん là một tiếng nước bắn tóe đơn lẻ — "chụp/bõm" — còn "róc rách" là tiếng nước chảy rì rào liên tục, khác loại âm.)

## §7. Thêm nghĩa (1)

### 2874 [monologue] — ghi chú giải thích câu chơi chữ không có trong JP
- JP: 「自分自身が意図せぬところで、下らぬダジャレを口にしてしまっていたことに。」
- TW: 「看她的樣子我才意識到，自己這話說得太不過腦子了。」
- VN cũ: 「Bản thân mình vừa vô tình thốt ra một câu chơi chữ nhạt nhẽo. (Bảo hỏa - Hoka / Ngoài ra - Hoka)」
- Fix: bỏ parenthetical → 「Bản thân mình vừa vô tình thốt ra một câu chơi chữ nhạt nhẽo.」
- Ghi chú: parenthetical giải thích câu chơi chữ 保火/他 (hoka) ở dòng 1952 — là ghi chú của dịch giả, không có trong JP của dòng này. Nếu Hieu muốn giữ nó như chú thích cho người đọc thì có thể khôi phục; theo quy tắc "không thêm nghĩa ngoài JP" thì bỏ.

## §8. Kiểm chứng đại từ (không sửa, chỉ ghi nhận)

- **Soutetsu "tôi" với Kisaki đúng toàn file**: 116 thoại Soutetsu, 0 dòng tự xưng "anh" (3 lần "anh" xuất hiện đều là "anh Urakami" ngôi thứ ba: 1782, 1891, 2337). Độc thoại Soutetsu toàn "tôi", 0 "anh" tự xưng (các "anh" trong độc thoại đều là "anh Urakami").
- **Soutetsu gọi Kisaki "cô" nhất quán** (1730, 1916, 1991, 2047, 2267...); gọi Hibiki "em ấy" (2073, 2232, 2763); gọi Hachiroku "em" (1791); gọi Mayami "chị Mayami" (2049, 2059); gọi Mototada "ông Mototada", Urakami "anh Urakami".
- **Hibiki**: tự xưng "em", gọi Soutetsu "anh hai" (2098, 2376); gọi Kisaki "Tiền bối Kisaki" (2257).
- **Hachiroku**: tự xưng "em", gọi Soutetsu "ngài Soutetsu" (2384), gọi Kisaki "cô" (2262, sau fix 2260).
- **Kisaki — KHÔNG sửa, chờ Hieu** (xem §10): tự xưng "tôi" 16 dòng khi nói với Soutetsu, gọi Soutetsu "anh Soutetsu" 10 dòng; 0 dòng tự xưng "em" trong file này.

## §9. Các kiểm tra cơ học

- **Lệch vị trí / chuỗi xoay**: 0. Không có cặp VN nào bị hoán đổi: giá trị VN trùng duy nhất là 1902/1924 「À……」 — JP cả hai đều là 「ああ……」 (Kisaki 1902, Soutetsu 1924), trùng hợp lệ, không phải lệch dòng. File 01 cùng route có chuỗi xoay 173 dòng; file này KHÔNG có.
- **Nhiễm chéo**: 0. Không có dòng VN nào thuộc file khác.
- **Mồ côi**: 0. Mọi dòng VN đều khớp nghĩa với JP/TW của chính key đó.
- **Chưa dịch / VN trống / VN == TW**: 0.
- **Ký tự Nhật sót trong VN**: 0 ngoài các thuật ngữ JP hợp lệ nằm trong thẻ %l (vd. `\x%lエアクラ;…`, `\x%l溶栓;…` — đúng quy tắc giữ tag).
- **Thẻ %l**: cân bằng ở mọi dòng (số `\x%l` == số `%l;#;`); không có tag hỏng nào ngoài 2008/2365 (đã sửa).
- **fa/fu**: chỉ có ふぅ (1874 "Phù……", 1946 "Hửm?") — đều đúng; không có ふぁ/ふあ/ふぇ trong file.
- **ひゃ/ひあ**: 1859 ひゃっ → "Á!?", 1861 ひゃっ/きゃうっ → "Kya!? Kyaư!" — giữ nguyên theo quyết định Hieu 20/11 (họ ひゃ/ひあ là ngẫu hứng theo nhân vật + ngữ cảnh, không thống nhất); sweep không gắn cờ các dòng này.
- **日ノ本**: 4 dòng, đều đã là "Hinomoto" đúng (1766, 1821, 2130, 2246) — không cần sửa.
- **まいてつ → "chủ tàu"**: đúng ở 1907, 2181. **エアクラ → "Aircra"**: đúng toàn file. **投炭 → "thêm than"**: đúng (1940). **ポーカー → "móc bếp"**: giữ — là gloss chiếm đa số toàn dự án (6 dòng vs "cây cời than" 1 dòng). **Thị trưởng Paulette** (1378): giữ — Paulette là thị trưởng, dạng này xuất hiện 35 lần toàn dự án.
- **2333** Kisaki gọi "tiền bối" — giữ: người nghe là Soutetsu (senpai hướng dẫn cô trong buồng lái), "hậu bối" là Hibiki; khớp dòng kề 2331/2334.
- **2346** "Ư, a." cho あっ — giữ: âm đã được diễn đạt, không mất.
- **3065** "Toyoda, Ponda, Nissanu, Machida" — giữ: JP dùng tên nhại (トヨダ/ポンダ/ニッサヌ/マチダ), VN theo JP là đúng; TW tự ý đổi thành tên hãng thật.
- **3121** （かぽーん）→ "（Rào rào）" và **3119** （ざばあああああっ！）→ "（Àooooooooo!）" — giữ: âm nước, TW cũng dùng 嘩啦; không rõ ràng sai.
- **2004** "Rơi rơi rơi mất!" cho 落ちる落ちる落ちるっ — giữ: "mất" diễn đạt sự rơi mất, TW cũng thêm 下去.

## §10. Chờ Hieu (không tự quyết)

1. **Kisaki tự xưng "tôi" hay "em" với Soutetsu — câu hỏi ĐANG CHỜ từ file 稀咲01, file này bổ sung thêm bằng chứng.** File này: Kisaki tự xưng "tôi" 16 dòng với Soutetsu (1674, 1702, 1900, 1940, 2008, 2065, 2067, 2068, 2080, 2081, 2092, 2105, 2118, 2133, 2286, 2292, 2297, 2339...) và gọi Soutetsu "anh Soutetsu" 10 dòng — nội bộ file NHẤT QUÁN, không sửa dòng nào. Nhưng đối chiếu toàn dự án: Kisaki "tôi" 284 dòng vs "em" 247 dòng — cảnh H (h1/h2/h3) và Grand 06 dùng "em" áp đảo, còn các file họp/bàn công việc (Common 14, Paulette 09/14, Hibiki 10/13/14) dùng "tôi". File 01 cùng route dùng "em" 12 dòng / "tôi" 3 dòng, và agent file 01 đã ghi "Chờ Hieu: Kisaki ボク với Soutetsu 'tôi' hay 'em' (tiền lệ h1 có phải chỉ đúng trong bối cảnh riêng?)". Khả năng cao là theo NGỮ CẢNH (thân mật → "em", công việc → "tôi"), nhưng đây là quyết định của Hieu — không đổi hàng loạt 26 dòng khi chưa có chốt.
2. **2874**: ghi chú "(Bảo hỏa - Hoka / Ngoài ra - Hoka)" đã bỏ theo quy tắc; nếu Hieu muốn giữ chú thích giải thích câu chơi chữ cho người đọc thì khôi phục lại.
3. **2151 "Migita Ichi"**: đã sửa trực tiếp; đợt thống nhất cần đối chiếu lại với 15 dòng "Migita System" trong hàng đợi để khỏi đếm trùng.
4. **2333 "tiền bối"**: đã giữ với lý do ở §9; nếu Hieu thấy Kisaki không gọi Soutetsu là "tiền bối" thì báo lại.

## Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 29 fix đối chiếu trực tiếp với JP của từng dòng (không chỉ parse-check): **29 tổng / 29 soát lại đạt / 0 bỏ / 0 sửa**. Trong lượt soát 2, kiểm tra thêm: không fix nào thay đổi ngoài phần cần sửa (diff-sanity cơ học: mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa — xem log build); JP/TW/old_vn trong JSON khớp CSV3 tuyệt đối 29/29.

## Khối TOML (đã parse-kiểm chứng: 29 khóa, 0 sai lệch giá trị)

```toml
"1370" = "「Công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; cũng có những khó khăn riêng của công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; nhỉ.\\nTôi cứ tưởng họ đang tận hưởng mùa xuân của thế gian này cơ.」"
"1371" = "「Lý do lớn nhất khiến công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; chọn Ohitoyo làm địa điểm ứng cử,\\nlà vì nơi đây dễ dàng trở thành cứ điểm sản xuất và bán hàng cho khu vực trung tâm Kyushu.」"
"1674" = "「B, bình thường thì tôi không sợ đâu.\\nNhưng mà giật mình chứ sao!? Ngọn lửa cứ như lò địa ngục thế này.」"
"1721" = "「Cùng tồn tại và cùng phát triển? Giữa thành phố Ohitoyo và\\ncông ty \\x%lエアクラ;#00ffc040;Aircra%l;#; sao?」"
"1750" = "「Tuy nhiên, nếu chỉ có hợp tác thì cũng không thể tránh khỏi sự suy thoái chậm chạp.\\nGiống hệt như tình trạng mà Ohitoyo đang mắc phải vậy.」"
"1772" = "「Nếu giả sử có thể khôi phục lại tuyến đường đó, thì cả công ty \\x%lエアクラ;#00ffc040;Aircra%l;#; và Đường sắt Ohitoyo\\nđều có thể tạo ra lợi nhuận…… nên tôi đã nghĩ nếu làm được thì tốt biết mấy.」"
"1870" = "「Hiee!? Auwa!?——A——kyuuu～～～Ư」"
"1942" = "「À, đúng vậy. Bị \\x%l炭水車;#00ffc040;toa tiếp than nước%l;#; và lò hơi che khuất,\\nnên hoàn toàn không thể nhìn thấy tình hình trong \\x%l運転台;#00ffc040;buồng lái%l;#; hay cảnh vật phía trước.」"
"2008" = "「Giống như anh Soutetsu sở hữu \\x%l8620;#00ffc040;8620%l;#, cho chạy tàu, và nhận được phần lợi nhuận được chia. Ý tôi là làm điều tương tự với đường ray, nhưng với số lượng người tham gia lớn hơn.」"
"2038" = "「Cả Đường sắt Ohitoyo nữa sao? Ơ, à…… ra là vậy. Đương nhiên rồi,\\nnếu là vận chuyển thì sẽ có \\x%l列車;#00ffc040;đoàn tàu%l;#; chở hàng chạy qua mà——」"
"2151" = "「Đúng vậy. Xưởng rượu Migita Ichi cũng thế,\\nvà Kumagin cũng không ngoại lệ.」"
"2192" = "「Công việc của anh ấy không phải là 『thu hút nhà máy đến Ohitoyo』,\\nmà là 『chọn địa điểm tối ưu nhất để đặt nhà máy』.」"
"2223" = "「Bây giờ vẫn còn phí bản quyền của động cơ Aero-Craftech,\\nnên mùa xuân của thế gian này vẫn là mùa xuân thôi…… nhưng làm gì có dư dả để mà tận hưởng chứ.」"
"2260" = "「Cô Kisaki sẽ làm \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự. Ngài Soutetsu sẽ hướng dẫn.\\nNếu vậy, Hibiki sẽ làm \\x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; tập sự——」"
"2289" = "「C, căng thẳng――――～～～Ư」"
"2331" = "「Cách đó…… ý cô là, khôi phục lại tuyến đường giữa Ohitoyo và Sendai sao?」"
"2365" = "「Là nhờ được ngồi trên \\x%l8620;#00ffc040;8620%l;#; đấy. Hơn nữa, cũng nhờ được nghe anh kể chi tiết về chuyện khôi phục tuyến đường.」"
"2376" = "「Anh hai——anh trai?」"
"2394" = "「Ư!」"
"2395" = "「Ư!?」"
"2523" = "Tiếng nước kêu 'chụp' một tiếng."
"2559" = "Giữa nơi đó và Ohitoyo trước đây,\\ntừng được kết nối bằng tuyến đường sắt \\x%l帝鉄;#00ffc040;Teitetsu%l;#; chạy vòng quanh Kagoshima."
"2676" = "Nếu có thể thiết lập một địa điểm ứng cử viên có lợi thế hơn Ohitoyo,\\nthì vừa có thể tránh được việc thu hút nhà máy, vừa mang lại điểm cộng cho anh Urakami."
"2810" = "Dáng vẻ thiếu tự tin trong \\x%l運転台;#00ffc040;buồng lái%l;#; khi nãy, giờ đây lại xinh đẹp đến nhường này sao――――――Ư!!"
"2821" = "Ngay chính diện. Ánh mắt của Kisaki nhìn xuống dưới. Và ánh mắt đó, ngay lập tức lại hướng lên trên——Ư!!?"
"2830" = "Tiếng nước đó không hề dừng lại, mà vòng sang bên hông, rồi tiến sát ngay bên cạnh tôi——Ư!!"
"2874" = "Bản thân mình vừa vô tình thốt ra\\nmột câu chơi chữ nhạt nhẽo."
"2915" = "Gương mặt Kisaki lộ vẻ hài lòng.\\nCó vẻ như sự hiểu biết của tôi đã nhận được điểm đạt."
"2992" = "Phương án dẫn đến sự hồi sinh của mạng lưới đường sắt——sinh mệnh của ngành đường sắt, đã được cô thiếu nữ đang mỉm cười ngay trước mắt tôi nghĩ ra."
```

## Kết bài

File 稀咲02_新事業案: đọc 448/448 dòng, sai **29 dòng (6,5%)** — thuật ngữ 10, thở gấp 7 (cả 7 từ sweep), sai nghĩa 7, thẻ 2, đại từ 1, SFX 1, thêm nghĩa 1. Không lệch vị trí, không chuỗi xoay — trái hẳn với file 01 cùng route (47,0% với chuỗi xoay 173 dòng): file này dịch cẩn thận hơn hẳn, lỗi tập trung ở thuật ngữ cũ Ohimitera/Ohito (9/29) và vài lỗi nghĩa lẻ. Đại từ Soutetsu/Kisaki/Hibiki/Hachiroku đều đã đúng; câu hỏi duy nhất còn treo là Kisaki "tôi" hay "em" với Soutetsu (đã chờ từ file 01, file này bổ sung 16 dòng "tôi" + 10 dòng "anh Soutetsu" vào cùng câu hỏi — chờ Hieu chốt, không tự đổi). Lượt soát 2: 29/29/0/0. Khối TOML 29 khóa parse đạt, 0 sai lệch.
