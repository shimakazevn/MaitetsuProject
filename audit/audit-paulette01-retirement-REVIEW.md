# Audit: Paulette 01_ポーレット退任 — 35 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット01_ポーレット退任.txt.toml` — lễ bàn giao của Paulette: ngày cuối cùng cô làm thị trưởng, Soutetsu nhìn lại 8 năm nhiệm kỳ của cô, hai người nói về việc làm cha, về Hikari và Reina. 419 dòng script đã đọc hết, đối chiếu từng dòng với JP gốc và TW (nhân chứng thứ hai).

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa toàn bộ 419 dòng (thoại 269: Paulette 101, Soutetsu 76, Hikari 33, Reina 27, Miyamoto 11, nhân viên B 10, Kisaki 6, nhân viên A 4, phóng viên A 1; lời dẫn 150) đối chiếu JP + TW từ CSV "Trang tính 3" và TOML-2.
- **35 dòng sai (8,4%), 0 dòng chưa chắc chắn.** Thoại sai 31/269 (11,5%), lời dẫn sai 4/150 (2,7%). Theo người nói: Soutetsu 19, Paulette 7, Kisaki 3, lời dẫn 4, nhân viên B 1, Reina 1.
- Phân loại: thuật ngữ 12, xưng hô 19, lỗi nhỏ 4; lệch vị trí 0, chưa dịch 0, cắt cụt 0, chưa chắc chắn 0.
- Heuristic (dấu phẩy kiểu MT + "mình" độc lập) báo 2 dòng (2557, 2555) — cả 2 đều đúng là sai thật, nhưng chỉ bắt được 2/35.
- Không key-shift sạch (shift 0: 417/419 — 2 dòng lệch dạng là 2557/2555, độc thoại bọc trong 「」). TOML và CSV giống hệt nhau về nội dung (0 khác biệt thực chất; các khác biệt thô chỉ ở `\n`/khoảng trắng).
- 0 dòng CSV trống; VN==TW 0. `[selections]` rỗng (0 mục). Thẻ `%l`: JP có 0 thẻ, VN có 1 thẻ gloss thêm vào ở 2443 (đúng, còn nguyên) — **0 thẻ thiếu dấu `;` đóng**.
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi:** đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục); 34/35 dòng sai chỉ xuất hiện 1 lần. Ngoại lệ: 1648 "「!」" xuất hiện 206 lần (mẫu lỗi hệ thống mất tiếng hít っ). Cặp trùng trong file "「A——」" 1641/1697 đều đúng (JP khác nhau: 「あ――」 vs 「ああ――」).
- Không có file trùng lặp ở thư mục khác (đã kiểm tra md5 toàn bộ 227 file TOML-2; Grand 04 vẫn là file trùng duy nhất trong dự án).
- Quét xưng hô bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`): Soutetsu trong thoại tự xưng "tôi/Tôi" 2 dòng (1923, 1999 — đúng), "anh/Anh" tự xưng 19 dòng (tất cả sai); "em" ngôi hai với Reina 4 dòng (1932, 2019, 1207, 1508 — đúng); "cháu" 1 dòng (2005, với bà Miyamoto — đúng). "mình" trong độc thoại 10 dòng — tất cả đều đúng (sở hữu/phản thân/mẫu "Tôi… mình…").

## Kết luận về cơ chế lỗi

File sạch về cấu trúc: không có dòng nào bị dán nhầm chỗ, không có chuỗi xoay vòng, không có tràn chương. Lỗi tập trung ở hai lựa chọn hệ thống của người dịch: (1) Soutetsu tự xưng "anh" trong thoại với Paulette/Reina — 19/21 lần tự xưng trong thoại (chỉ 2 lần dùng "tôi"), trái docs locations §2.1 ("Tôi"; "Anh" chỉ dùng với Hibiki); (2) thuật ngữ 御一夜 — file này có 0 lần "Ohitoyo" đúng, toàn bộ 13 lần xuất hiện đều là dạng cũ (Ohimitera 10, Ohito 3). 4 lỗi nhỏ còn lại: 1 mất tiếng hít っ, 2 độc thoại bọc trong 「」, 1 xưng hô "bà Takasaki" lạc với quy ước trong file. File này là chương đầu tiên của tuyến Paulette (chương 01) nhưng tỷ lệ sai 8,4% cao hơn hẳn các chương 04–12 (2,0–7,0%) — chủ yếu vì lỗi xưng hô hệ thống.

## Chi tiết dòng sai

### Thuật ngữ (12 dòng)

**1543 [Kisaki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「そういっていただけると、安心です。
これからも、ともに御一夜市のために」
- TW: 「你這麼說我就放心了。為了御一夜市今後的發展，讓我們繼續攜手並進吧」
- Cũ: 「Nghe cô nói vậy, tôi thấy rất an tâm.
Từ nay về sau, hãy cùng nhau cố gắng vì thành phố Ohimitera nhé.」
- Sửa: 「Nghe cô nói vậy, tôi thấy rất an tâm. Từ nay về sau, hãy cùng nhau cố gắng vì thành phố Ohitoyo nhé.」

**1567 [職員Ｂ]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「前市長。御一夜を笑顔の町に戻してくださり――
本当にありがとうございました！」
- TW: 「前市長，謝謝你讓御一夜又變回了那個充滿笑容的城市！」
- Cũ: 「Cựu Thị trưởng. Cảm ơn cô vì đã mang nụ cười
trở lại với Ohimitera——thực sự cảm ơn cô rất nhiều!」
- Sửa: 「Cựu Thị trưởng. Cảm ơn cô vì đã mang nụ cười trở lại với Ohitoyo——thực sự cảm ơn cô rất nhiều!」

**1727 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「そうですね。
御一夜の――わたしたちの町と、くらしのために」
- TW: 「好的。這都是為了御一夜——為了我們的生活，我們的城市」
- Cũ: 「Vâng ạ.
Vì Ohimitera——vì thị trấn và cuộc sống của chúng ta.」
- Sửa: 「Vâng ạ. Vì Ohitoyo——vì thị trấn và cuộc sống của chúng ta.」

**1789 [Kisaki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「御一夜市の復興はマイントレジャー。
そして、御一夜鉄道様あってのことですから」
- TW: 「御一夜市的復興都是多虧了煤探樂園，還有御一夜鐵路」
- Cũ: 「Sự phục hưng của thành phố Ohimitera là nhờ Mine Treasure.
Và nhờ có Đường sắt Ohito.」
- Sửa: 「Sự phục hưng của thành phố Ohitoyo là nhờ Mine Treasure. Và nhờ có Đường sắt Ohitoyo.」

**1796 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「定年退職までの長きにわたり。御一夜市を支え続けて
くださって、本当にありがとうございました」
- TW: 「您長年為御一夜市奉獻，直到退休，真的十分感謝」
- Cũ: 「Cảm ơn cô rất nhiều vì đã luôn cống hiến cho thành phố Ohimitera
trong suốt một thời gian dài cho đến lúc nghỉ hưu.」
- Sửa: 「Cảm ơn cô rất nhiều vì đã luôn cống hiến cho thành phố Ohitoyo trong suốt một thời gian dài cho đến lúc nghỉ hưu.」

**1813 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「宝生新市長にお任せできること、心強く感じています。
[おひとよ,2]御一夜市の未来を、どうぞよろしくお願いします」
- TW: 「我從心底相信，寶生新市長是值得託付這個城市未來的人。御一夜市的未來就交給你了」
- Cũ: 「Em cảm thấy rất yên tâm khi có thể giao phó cho Tân Thị trưởng Houshou.
Tương lai của thành phố Ohimitera, xin nhờ cả vào chị.」
- Sửa: 「Em cảm thấy rất yên tâm khi có thể giao phó cho Tân Thị trưởng Houshou. Tương lai của thành phố Ohitoyo, xin nhờ cả vào chị.」

**1865 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「です、よね。できちゃうんだ、旅。
今のわたしたちなら――御一夜鉄道の体制なら」
- TW: 「是啊。我們可以出去旅行了。而且御一夜鐵路現在的體制也允許我們這麼做」
- Cũ: 「Đúng, nhỉ. Chúng ta có thể đi du lịch rồi.
Chúng ta của hiện tại——với hệ thống của Đường sắt Ohito hiện tại.」
- Sửa: 「Đúng, nhỉ. Chúng ta có thể đi du lịch rồi. Chúng ta của hiện tại——với hệ thống của Đường sắt Ohitoyo hiện tại.」

**1977 [Kisaki]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「もちろん、全力でお引き受けします。
その上で今後とも――どうぞその手を、御一夜のために」
- TW: 「謝謝你的囑託，我定當全力以赴。希望波萊特小姐今後也能為御一夜的發展盡一份力」
- Cũ: 「Tất nhiên, tôi sẽ dốc toàn lực để đảm đương.
Nhưng đồng thời, từ nay về sau——mong cô hãy tiếp tục góp sức vì Ohimitera.」
- Sửa: 「Tất nhiên, tôi sẽ dốc toàn lực để đảm đương. Nhưng đồng thời, từ nay về sau——mong cô hãy tiếp tục góp sức vì Ohitoyo.」

**2004 [Reina]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「これ、御一夜鉄道と商店会の町のみんなからと、
それからだれより、ひかりちゃんからですよぉ」
- TW: 「這是御一夜鐵路和商店協會的各位送來的。當然，最重要的是，還有小光送給你的花」
- Cũ: 「Đây là hoa từ mọi người ở Đường sắt Ohito và Hiệp hội Thương gia trong thị trấn,
và hơn ai hết, là từ bé Hikari đó nha~.」
- Sửa: 「Đây là hoa từ mọi người ở Đường sắt Ohitoyo và Hiệp hội Thương gia trong thị trấn, và hơn ai hết, là từ bé Hikari đó nha~.」

**2008 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「みんなの力です。
市職員だけでなく、御一夜市のみんなの」
- TW: 「這都是大家的功勞。不光是靠市政府職員，還要多虧了市民的努力」
- Cũ: 「Đó là sức mạnh của tất cả mọi người.
Không chỉ của các nhân viên thành phố, mà là của toàn thể người dân Ohimitera.」
- Sửa: 「Đó là sức mạnh của tất cả mọi người. Không chỉ của các nhân viên thành phố, mà là của toàn thể người dân Ohitoyo.」

**2012 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: 「過分なお褒めに恐縮しますが、光栄です。
御一夜の更なる発展のためにも、努力を重ねて参ります」
- TW: 「過獎了，我深感惶恐，但這是我的光榮。為了御一夜的進一步發展，我們還不能停下努力的腳步」
- Cũ: 「Thật vinh hạnh khi được chị khen ngợi quá lời.
Để Ohimitera ngày càng phát triển hơn nữa, chúng tôi sẽ tiếp tục nỗ lực không ngừng.」
- Sửa: 「Thật vinh hạnh khi được chị khen ngợi quá lời. Để Ohitoyo ngày càng phát triển hơn nữa, chúng tôi sẽ tiếp tục nỗ lực không ngừng.」

**2342 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera"/"Ohito".

- JP: ポーレットの父、雛衣幸三前々市長の時代から、
御一夜市制を実務で支えた、総務部長だ。
- TW: 她是從波萊特的父親——上上屆市長雛衣幸三在任時，就負責御一夜市實際業務的總務部部長。
- Cũ: Trưởng phòng Tổng vụ, người đã gánh vác các công việc thực tế của thành phố Ohimitera
từ thời cha của Paulette, cựu Thị trưởng tiền nhiệm Hinai Kouzou.
- Sửa: Trưởng phòng Tổng vụ, người đã gánh vác các công việc thực tế của thành phố Ohitoyo từ thời cha của Paulette, cựu Thị trưởng tiền nhiệm Hinai Kouzou.

### Xưng hô (19 dòng)

**1194 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「――父親になって、幸せだ。これ以上を望めぬくらいに。
それだけは、間違いなく答えられるよ」
- TW: 「——但是我成為了父親，真的十分幸福，稱之為無上幸福亦不為過。這點我十分肯定」
- Cũ: 「——Trở thành một người cha, anh thấy rất hạnh phúc. Hạnh phúc đến mức không còn mong ước gì hơn.
Đó là điều duy nhất anh có thể khẳng định chắc chắn.」
- Sửa: 「——Trở thành một người cha, tôi thấy rất hạnh phúc. Hạnh phúc đến mức không còn mong ước gì hơn. Đó là điều duy nhất tôi có thể khẳng định chắc chắn.」

**1207 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「……れいな。花束をもってくれるか？」
- TW: 「……玲奈，能幫我拿著花束嗎？」
- Cũ: 「...Reina. Em cầm giúp anh bó hoa được không?」
- Sửa: 「...Reina. Em cầm giúp tôi bó hoa được không?」

**1511 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「いや――僕の判断が悪かった」
- TW: 「不，都怪我反應慢了」
- Cũ: 「Không——Là do phản xạ của anh quá chậm.」
- Sửa: 「Không——Là do phản xạ của tôi quá chậm.」

**1558 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「実際、父親になったいまでも。
怖いことはたくさんだし、わからないことも無数にある」
- TW: 「其實，就算現在已經成為父親了，我還是有很多不懂的、很多害怕的」
- Cũ: 「Thực tế thì, ngay cả bây giờ khi đã làm cha.
Anh vẫn thấy có rất nhiều điều đáng sợ, và vô số điều anh chưa hiểu rõ.」
- Sửa: 「Thực tế thì, ngay cả bây giờ khi đã làm cha. Tôi vẫn thấy có rất nhiều điều đáng sợ, và vô số điều tôi chưa hiểu rõ.」

**1582 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「だからといって後悔もないし、時間を戻したくもない。
問いに対して、ずれた答えになってしまうが――」
- TW: 「可我已經是父親了，既不想後悔也不想回到過去。雖然這個答案可能牛頭不對馬嘴」
- Cũ: 「Dù vậy, anh không hề hối hận, cũng không muốn quay ngược thời gian.
Tuy câu trả lời có hơi lạc đề so với câu hỏi——」
- Sửa: 「Dù vậy, tôi không hề hối hận, cũng không muốn quay ngược thời gian. Tuy câu trả lời có hơi lạc đề so với câu hỏi——」

**1741 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ベビーソープだ。確か、一本三千円くらいすると」
- TW: 「嬰兒沐浴露啊。我記得一瓶要３０００日元左右」
- Cũ: 「Sữa tắm trẻ em ấy. Anh nhớ không lầm thì một chai khoảng 3.000 yên.」
- Sửa: 「Sữa tắm trẻ em ấy. Tôi nhớ không lầm thì một chai khoảng 3.000 yên.」

**1820 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「僕の方こそだ、ポーレット。
僕をおとうさんにしてくれて、ありがとう」
- TW: 「我才要謝你讓我成為一個父親」
- Cũ: 「Anh mới là người phải cảm ơn, Paulette.
Cảm ơn em vì đã cho anh được làm cha.」
- Sửa: 「Tôi mới là người phải cảm ơn, Paulette. Cảm ơn em vì đã cho tôi được làm cha.」

**1827 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「確かにいったが――
しかし、そこまで細かな、心の機微のような問題を」
- TW: 「我是這麼說過……可是，這麼小的孩子能明白這麼細微敏感的感情問題嗎」
- Cũ: 「Đúng là anh có nói——
Nhưng, những vấn đề tinh tế, phức tạp trong tâm hồn như vậy...」
- Sửa: 「Đúng là tôi có nói—— Nhưng, những vấn đề tinh tế, phức tạp trong tâm hồn như vậy...」

**1830 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「幼いこころに、どれほど深い傷がつくのか――
僕には、想像することもできん」
- TW: 「我無法想像這會對她幼小的心靈造成多麼嚴重的傷害」
- Cũ: 「Tâm hồn non nớt ấy sẽ bị tổn thương sâu sắc đến nhường nào——
Anh không dám tưởng tượng nữa.」
- Sửa: 「Tâm hồn non nớt ấy sẽ bị tổn thương sâu sắc đến nhường nào—— Tôi không dám tưởng tượng nữa.」

**1841 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「すまん、れいな、またやってしまったな」
- TW: 「抱歉，玲奈，我又嚇到你了」
- Cũ: 「Xin lỗi, Reina, anh lại làm thế nữa rồi.」
- Sửa: 「Xin lỗi, Reina, tôi lại làm thế nữa rồi.」

**1858 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「だな。うむ、今は違う――と自分では思っているが、
昔は確かに、人からの好意に、価値を覚えていなかった」
- TW: 「是吧。雖然我感覺自己現在應該已經改善了，但以前的確沒怎麼意識到別人對我的好意有多大價值」
- Cũ: 「Đúng vậy. Ừm, bây giờ thì khác rồi——anh tự thấy thế,
nhưng ngày xưa quả thật anh không biết trân trọng thiện ý của người khác.」
- Sửa: 「Đúng vậy. Ừm, bây giờ thì khác rồi——tôi tự thấy thế, nhưng ngày xưa quả thật tôi không biết trân trọng thiện ý của người khác.」

**1932 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「れいなも、とてもいいこだったな。
花束も祝辞も、うれしかった。ありがとう」
- TW: 「玲奈也表現得很好。謝謝你的花束和祝詞」
- Cũ: 「Reina cũng đã rất ngoan mà.
Bó hoa và lời chúc của em, anh rất vui. Cảm ơn em.」
- Sửa: 「Reina cũng đã rất ngoan mà. Bó hoa và lời chúc của em, tôi rất vui. Cảm ơn em.」

**1940 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「あの時、れいなの、いったとおりになった。
僕がお父さんで」
- TW: 「現在正如玲奈當時所說的一樣，我成了父親」
- Cũ: 「Lúc đó, mọi chuyện đã diễn ra đúng như Reina nói.
Anh trở thành một người cha.」
- Sửa: 「Lúc đó, mọi chuyện đã diễn ra đúng như Reina nói. Tôi trở thành một người cha.」

**1941 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「今のポーレットは大人だし、僕と初めて会ったときにも、
ポーレットは、充分すぎるほど大人だった気がするから」
- TW: 「現在的你很成熟，但其實第一次見面的時候，我就覺得你已經很成熟了」
- Cũ: 「Paulette bây giờ đã là người lớn, và ngay cả lần đầu tiên chúng ta gặp nhau,
anh cảm thấy Paulette cũng đã trưởng thành quá mức cần thiết rồi.」
- Sửa: 「Paulette bây giờ đã là người lớn, và ngay cả lần đầu tiên chúng ta gặp nhau, tôi cảm thấy Paulette cũng đã trưởng thành quá mức cần thiết rồi.」

**1942 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「あのときの質問の答えだが……
今もやはり、はっきりとしたものにはならない」
- TW: 「當時你問我的那個問題……就算到現在，我還是無法給出一個明確的答案」
- Cũ: 「Về câu trả lời cho câu hỏi lúc đó...
Đến bây giờ, anh vẫn không thể đưa ra một đáp án rõ ràng.」
- Sửa: 「Về câu trả lời cho câu hỏi lúc đó... Đến bây giờ, tôi vẫn không thể đưa ra một đáp án rõ ràng.」

**1998 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「決して悪いことではないだろう。
むしろ、とても良いことのように思うが――」
- TW: 「這並不是什麼壞事吧。甚至可以說是好事」
- Cũ: 「Đó chắc chắn không phải là chuyện xấu.
Ngược lại, anh thấy đó là một điều rất tốt——」
- Sửa: 「Đó chắc chắn không phải là chuyện xấu. Ngược lại, tôi thấy đó là một điều rất tốt——」

**2009 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「それはそうだな。みな、ひかりに良くしてくれている。
しかし……それのどこが僕に似ているのだ？」
- TW: 「這麼一說好像是這樣。大家都對她很好。可是……這又哪裡像我了？」
- Cũ: 「Đúng là vậy thật. Mọi người đều đối xử rất tốt với Hikari.
Nhưng... điểm đó giống anh ở chỗ nào chứ?」
- Sửa: 「Đúng là vậy thật. Mọi người đều đối xử rất tốt với Hikari. Nhưng... điểm đó giống tôi ở chỗ nào chứ?」

**2019 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「なら良かったが――
すまん、驚かせてしまったな」
- TW: 「那就好。抱歉，嚇到你了」
- Cũ: 「Vậy thì tốt rồi——
Xin lỗi, anh làm em giật mình nhỉ.」
- Sửa: 「Vậy thì tốt rồi—— Xin lỗi, tôi làm em giật mình nhỉ.」

**2020 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi"; "Anh" chỉ dùng với Hibiki).

- JP: 「ならば、ひかりと僕も似ているわけか？」
- TW: 「那就是說，光也很像我嘍」
- Cũ: 「Vậy, Hikari và anh cũng giống nhau sao?」
- Sửa: 「Vậy, Hikari và tôi cũng giống nhau sao?」

### Lỗi nhỏ (4 dòng)

**1648 [Paulette]** — JP 「っ！」 là tiếng hít gasp — bản Việt chỉ còn "「!」" (mẫu mất っ toàn dự án).

- JP: 「っ！」
- TW: 「啊！」
- Cũ: 「!」
- Sửa: 「Ư!」

**2247 [lời dẫn]** — Bản Việt "bà Takasaki" — trong file này Soutetsu gọi bà là "chị Takasaki" trong thoại (2060), độc thoại dùng "vợ anh Takasaki" (2389, 2280, 2267, 2664); "bà" là ngoại lệ duy nhất.

- JP: れいなの手から抜け出して、
高崎さんの陰に隠れてしまった。
- TW: 今天光從玲奈那裡掙脫，藏到了高崎太太身後。
- Cũ: Hikari giật tay khỏi Reina,
và nấp sau lưng bà Takasaki.
- Sửa: Hikari giật tay khỏi Reina, và nấp sau lưng chị Takasaki.

**2555 [lời dẫn]** — Dòng độc thoại nhưng bản Việt bọc trong 「」 — JP là lời dẫn, không phải thoại.

- JP: 無論、れいなはひかりにとてもなつかれている。
れいなおねーちゃんは、いつでも優しくにこにこしてる。
- TW: 當然光也很親玲奈。作為她的姐姐，玲奈也一直對她很溫柔。
- Cũ: 「Tất nhiên, Reina rất được Hikari quý mến.
Chị Reina lúc nào cũng hiền lành và cười tủm tỉm.」
- Sửa: Tất nhiên, Reina rất được Hikari quý mến. Chị Reina lúc nào cũng hiền lành và cười tủm tỉm.

**2557 [lời dẫn]** — Dòng độc thoại nhưng bản Việt bọc trong 「」 — JP là lời dẫn, không phải thoại.

- JP: ひかりが産まれてくるまでは、
こうした景色は、ポーレットとれいなとのものだった。
- TW: 直到光出生之前，波萊特還都是跟玲奈進行這種交流的。
- Cũ: 「Cho đến khi Hikari ra đời,
những cảnh tượng thế này vẫn luôn là của Paulette và Reina.」
- Sửa: Cho đến khi Hikari ra đời, những cảnh tượng thế này vẫn luôn là của Paulette và Reina.

## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1194 = "「——Trở thành một người cha, tôi thấy rất hạnh phúc. Hạnh phúc đến mức không còn mong ước gì hơn. Đó là điều duy nhất tôi có thể khẳng định chắc chắn.」"
1207 = "「...Reina. Em cầm giúp tôi bó hoa được không?」"
1511 = "「Không——Là do phản xạ của tôi quá chậm.」"
1543 = "「Nghe cô nói vậy, tôi thấy rất an tâm. Từ nay về sau, hãy cùng nhau cố gắng vì thành phố Ohitoyo nhé.」"
1558 = "「Thực tế thì, ngay cả bây giờ khi đã làm cha. Tôi vẫn thấy có rất nhiều điều đáng sợ, và vô số điều tôi chưa hiểu rõ.」"
1567 = "「Cựu Thị trưởng. Cảm ơn cô vì đã mang nụ cười trở lại với Ohitoyo——thực sự cảm ơn cô rất nhiều!」"
1582 = "「Dù vậy, tôi không hề hối hận, cũng không muốn quay ngược thời gian. Tuy câu trả lời có hơi lạc đề so với câu hỏi——」"
1648 = "「Ư!」"
1727 = "「Vâng ạ. Vì Ohitoyo——vì thị trấn và cuộc sống của chúng ta.」"
1741 = "「Sữa tắm trẻ em ấy. Tôi nhớ không lầm thì một chai khoảng 3.000 yên.」"
1789 = "「Sự phục hưng của thành phố Ohitoyo là nhờ Mine Treasure. Và nhờ có Đường sắt Ohitoyo.」"
1796 = "「Cảm ơn cô rất nhiều vì đã luôn cống hiến cho thành phố Ohitoyo trong suốt một thời gian dài cho đến lúc nghỉ hưu.」"
1813 = "「Em cảm thấy rất yên tâm khi có thể giao phó cho Tân Thị trưởng Houshou. Tương lai của thành phố Ohitoyo, xin nhờ cả vào chị.」"
1820 = "「Tôi mới là người phải cảm ơn, Paulette. Cảm ơn em vì đã cho tôi được làm cha.」"
1827 = "「Đúng là tôi có nói—— Nhưng, những vấn đề tinh tế, phức tạp trong tâm hồn như vậy...」"
1830 = "「Tâm hồn non nớt ấy sẽ bị tổn thương sâu sắc đến nhường nào—— Tôi không dám tưởng tượng nữa.」"
1841 = "「Xin lỗi, Reina, tôi lại làm thế nữa rồi.」"
1858 = "「Đúng vậy. Ừm, bây giờ thì khác rồi——tôi tự thấy thế, nhưng ngày xưa quả thật tôi không biết trân trọng thiện ý của người khác.」"
1865 = "「Đúng, nhỉ. Chúng ta có thể đi du lịch rồi. Chúng ta của hiện tại——với hệ thống của Đường sắt Ohitoyo hiện tại.」"
1932 = "「Reina cũng đã rất ngoan mà. Bó hoa và lời chúc của em, tôi rất vui. Cảm ơn em.」"
1940 = "「Lúc đó, mọi chuyện đã diễn ra đúng như Reina nói. Tôi trở thành một người cha.」"
1941 = "「Paulette bây giờ đã là người lớn, và ngay cả lần đầu tiên chúng ta gặp nhau, tôi cảm thấy Paulette cũng đã trưởng thành quá mức cần thiết rồi.」"
1942 = "「Về câu trả lời cho câu hỏi lúc đó... Đến bây giờ, tôi vẫn không thể đưa ra một đáp án rõ ràng.」"
1977 = "「Tất nhiên, tôi sẽ dốc toàn lực để đảm đương. Nhưng đồng thời, từ nay về sau——mong cô hãy tiếp tục góp sức vì Ohitoyo.」"
1998 = "「Đó chắc chắn không phải là chuyện xấu. Ngược lại, tôi thấy đó là một điều rất tốt——」"
2004 = "「Đây là hoa từ mọi người ở Đường sắt Ohitoyo và Hiệp hội Thương gia trong thị trấn, và hơn ai hết, là từ bé Hikari đó nha~.」"
2008 = "「Đó là sức mạnh của tất cả mọi người. Không chỉ của các nhân viên thành phố, mà là của toàn thể người dân Ohitoyo.」"
2009 = "「Đúng là vậy thật. Mọi người đều đối xử rất tốt với Hikari. Nhưng... điểm đó giống tôi ở chỗ nào chứ?」"
2012 = "「Thật vinh hạnh khi được chị khen ngợi quá lời. Để Ohitoyo ngày càng phát triển hơn nữa, chúng tôi sẽ tiếp tục nỗ lực không ngừng.」"
2019 = "「Vậy thì tốt rồi—— Xin lỗi, tôi làm em giật mình nhỉ.」"
2020 = "「Vậy, Hikari và tôi cũng giống nhau sao?」"
2247 = "Hikari giật tay khỏi Reina, và nấp sau lưng chị Takasaki."
2342 = "Trưởng phòng Tổng vụ, người đã gánh vác các công việc thực tế của thành phố Ohitoyo từ thời cha của Paulette, cựu Thị trưởng tiền nhiệm Hinai Kouzou."
2555 = "Tất nhiên, Reina rất được Hikari quý mến. Chị Reina lúc nào cũng hiền lành và cười tủm tỉm."
2557 = "Cho đến khi Hikari ra đời, những cảnh tượng thế này vẫn luôn là của Paulette và Reina."
```

Khối trên đã kiểm chứng: parse được bằng tomllib, đúng 35/35 key, giá trị khớp với JSON. Các giá trị đã viết một dòng (không `\n` thủ công, theo quyết định 19/11 của Hieu: game tự xuống dòng). Dấu —— không có khoảng trắng hai bên.

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em":** trong file này "em" 6 lần (1820, 1922, 1531, 1765, 2007, 1541) vs "cô" 2 lần (1539, 2005 — 2005 là ngôi ba "cô ấy"). Cộng dồn P09–16 + file này: "cô" 43 vs "em" 20 (file còn lại của chương 01, 御一夜探し, có thêm "em" 10 lần, "cô" 0 lần — tổng chương 01 là "em" 16 vs "cô" 2).
- **宮司:** JP có 1 lần (2236, đền chủ Akai) — bản Việt "thầy tế Akai", biến thể thứ 4 trong dự án (đền chủ 46×, "Cung tư tế" 11×, "Guuji" 9×, "thầy tế" 1×). Ghi nhận, không tính sai (đề xuất thống nhất về "đền chủ" đang chờ).
- **"KiHa" vs "Kiha":** 1 gloss trong file (2548 "KiHa 07S") — dùng "KiHa". Đề xuất thống nhất đang chờ.
- **コン / 湯医 / 帝鉄 / タブレット / 操作板 / 整備体 / 運転ボディ / マスコン / マスターコントローラー / 駿袋 / 端的:** 0 lần trong JP của file này.

## Đề xuất cập nhật context (chưa chốt)

Không có đề xuất mới từ file này.

## Đã kiểm tra và KHÔNG tính là sai

- **Paulette gọi Kisaki là "chị"** (1624, 1795, 2012): đã kiểm tra toàn dự án — Paulette gọi Kisaki "chị" ở nhiều file (共通11 2696, 2826 dùng "cô Kisaki" ở ngôi ba; Grand 04 2029 "Cả chị Kisaki, chị Mayami và Navi nữa") — đây là quy ước có sẵn trong dự án, không phải lỗi của file này. Không tính sai, không thống nhất nếu chưa có quyết định chung.
- **Paulette tự xưng theo đối tượng:** "em" với Soutetsu, "cháu" với bà Miyamoto, "tôi" ở bối cảnh chính thức — đúng mẫu đã ghi nhận, không tính sai.
- **"mình" trong độc thoại** 10 dòng (2276, 2515, 2316, 2656, 2323, 2317, 2606, 2621, 2549, 2521): tất cả đúng (sở hữu/phản thân/thành ngữ/mẫu "Tôi… mình…").
- **1893 "vợ anh Takasaki":** "anh" ở đây là Takasaki (ngôi ba), không phải Soutetsu tự xưng — đúng.
- **Cặp trùng "「A——」" 1641/1697:** JP khác nhau (「あ――」 vs 「ああ――」) — đều đúng.

## Kết bài

File 退任 sai 35/419 (8,4%) — sạch về cấu trúc, lỗi tập trung ở hai lựa chọn hệ thống: Soutetsu tự xưng "anh" (19 dòng) và thuật ngữ 御一夜 dạng cũ (12 dòng). Không còn dòng chưa chắc chắn nào trong file này; cặp lệch vị trí duy nhất của chương 01 nằm ở file 御一夜探し (1151↔2196), không phải file này. Sau khi dán khối TOML trên, file này coi như xong — không còn việc gì tồn đọng, trừ các quyết định đang chờ Hieu ("cô"/"em", 宮司, "KiHa") vốn là quyết định toàn dự án, không phải của riêng file. Bước tiếp theo: audit Paulette 02 (2 file: 古地図, 解放b寝台).
