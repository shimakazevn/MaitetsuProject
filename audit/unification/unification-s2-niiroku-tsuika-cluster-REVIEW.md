# Unification U8 — §2 P3/P5/P6/P8 + §6 F17–F24 + §7 O2/O3 (Niiroku + tsuika Kisaki pronoun cluster)

- Batch: U8. Mục: P3, P5, P6, P8, F17, F18, F19, F20, F21, F22, F23, F24, O2, O3 (14 mục).
- File sửa: 5 file — `ニイロク02_御一夜旅行.txt.toml` (5 dòng), `lr稀咲追加01_仲国視察の誘い.txt.toml` (19 dòng), `lr稀咲追加02_仲国視察.txt.toml` (8 dòng), `稀咲h2_プライベートルーム.txt.toml` (3 dòng), `lr_ニイロクh_誓い。約束.txt.toml` (15 dòng). **Tổng 50 dòng sửa.**
- File JSON: `unification-s2-niiroku-tsuika-cluster-wrong.json` (50 mục, kind="pronoun").

## §1. Phạm vi

- **P3 / F21** — Soutetsu → Kisaki: "em" → "cô" (NGƯỢC hướng Paulette "cô"→"em"). Áp cho tsuika01 (9 dòng), tsuika02 (8 dòng — xem §6 về hiệu chỉnh số liệu), 稀咲h2 (3 dòng).
- **P5 / F24** — Kisaki tự xưng theo NGỮ CẢNH (công việc/quyết đoán → "tôi"; thân mật/dễ tổn thương → "em"; JP luôn ボク). Áp cho tsuika01 (6 dòng → "em", 1516 giữ "tôi"); rà lại toàn bộ dòng "Tôi" của Kisaki ở tsuika02 (0 dòng đổi — xem §5).
- **P6 / F22** — Kisaki キミ: "anh" → "cậu" (tsuika01, 4 dòng).
- **P8 / F19** — Niiroku tự xưng với Akai → "Tôi" (Niiroku02, 3 dòng).
- **F17** — Niiroku02 1547; **F18** — Niiroku02 1166; **F20** — tsuika01 Soutetsu "Anh" → "Tôi" (3 dòng); **F23** — tsuika01 "anh Soutetsu" → bare "Soutetsu" (0 dòng mới — U7b đã sửa xong token này ở cả 3 key, xem §4).
- **O2** — Kisaki tự xưng: các dòng ranh giới (quyết theo uỷ quyền — xem §5). **O3** — lr_ニイロクh: phân bố em/Tôi đảo ngược (quyết theo uỷ quyền — xem §5).
- Không động: dòng gasp-Ư, dòng "Kh", dòng đã đúng. Không sửa lại các fix đã gộp của U7a/U7b trừ khi GHÉP token khác (xem §2).

## §2. Phương pháp

- Nguồn: CSV3 good-set (87.833 dòng; 10 file dual-set đã bỏ stale theo `dual-csv-sets.md` — không file nào trong batch này thuộc dual-set). TW của lr稀咲追加01 bị SHIFT (TW 684 ≈ JP 1145) — mọi bằng chứng TW từ file này đều VOID, chỉ dùng JP + dòng kề + tiền lệ.
- old_vn theo thứ tự đã hiệu chỉnh: **merged unification > moan > audit > CSV3 VN**. Chỉ load các `unification-*-wrong.json` đã gộp trên đĩa (18 file; không tồn tại file U10b/U11b — batch đang chạy song song không bị load nhầm). Map gồm 2.305 fix unification + 1.516 moan + 9.239 audit.
- Liệt kê ứng viên bằng máy (chỉ đếm/quét): (a) toàn bộ dòng "em"/"Em" của người nói 双鉄/monologue ở tsuika01/tsuika02, lọc người nghe bằng JP + dòng kề; (b) toàn bộ dòng Kisaki "Tôi"/"tôi"/"em" ở tsuika02; (c) toàn bộ dòng "Tôi"/"em" của Niiroku ở lr_ニイロクh; (d) đối chiếu key-list của audit (ROUTE-AUDIT.md) từng dòng. Mỗi fix là thay token viết tay trên old_vn (script chỉ thay đúng chuỗi đã ghi, assert số lần xuất hiện đúng như dự kiến, và assert fix ≠ old_vn).
- GHÉP (compose) với batch đã gộp — 2 dòng: tsuika01 1783 (old_vn = fix U7b P4; thêm F22 "anh"→"cậu" + F24 "tôi"→"em") và tsuika02 1077 (old_vn = fix U-t56-t66 "Trung Quốc"; thêm F21 "em"→"cô"). Cả hai đều ghi rõ trong §3 và §6.
- Nguồn old_vn: CSV3 40 / audit 3 (tsuika01 1025, 1564; lr_ニイロクh 1545) / moan 5 (lr_ニイロクh 1293, 1322, 1339, 1377, 1438) / unification đã gộp 2 (tsuika01 1783 U7b; tsuika02 1077 U-t56-t66).

## §3. Các dòng sửa (JP / TW / old_vn / fix)

Lý do theo nhóm (áp cho mọi dòng trong nhóm; chi tiết từng dòng ở bảng dưới):

- **F17 (1547)** — Người nói là シロ (Shiro), JP 「あらニイロクちゃん。大丈夫よ？」 hỏi Niiroku-chan có sao không; VN cũ "Chị nghe đây?" bịa thêm (TW "四六沒有在工作" cũng sai theo JP). Câu 2 "Chị đang chuẩn bị bữa tối" giữ nguyên — Shiro tự xưng "chị" là đúng.
- **F18 (1166)** — JP kết bằng quotative と (“と”？); romaji "To" theo quyết định 22/11 ~03:32.
- **F19 / P8 (1570/1788/1878)** — Niiroku với Akai → "Tôi" (31 "Tôi" vs 3 "Em" ở 01/02; trang trọng — cô gọi Akai là 赤井運転士). 1878 có 自分 tường minh trong JP.
- **F20 (720/1116/1322)** — Soutetsu với Kisaki → "Tôi" (quy tắc 19:45). 1116 GHÉP cả F21: "Anh nghĩ em đánh giá anh" → "Tôi nghĩ cô đánh giá tôi" (cả "Anh" chủ ngữ lẫn "anh" tân ngữ đều là Soutetsu → "tôi").
- **F21 / P3 (tsuika01 9 dòng; tsuika02 8 dòng; h2 3 dòng)** — Soutetsu gọi Kisaki "em" → "cô" mọi vị trí ngữ pháp (trực tiếp, kể lại, độc thoại "em ấy"→"cô ấy"). tsuika02 1077/1568 xác định người nghe là Kisaki bằng loại trừ: Khương không bao giờ là "em" với Soutetsu (luôn "cô Khương"), Suika vắng mặt trong đoạn trao đổi đó / không đưa "lời khuyên" nào (xem §5).
- **F22 (1327/1564/1587/1783)** — Kisaki キミ "anh" → "cậu". 1327 GHÉP cả F24 (cả 2 キミ + cả 3 ボク). 1564/1587 JP không có キミ tường minh nhưng VN dùng "anh" để gọi Soutetsu — vẫn đổi theo quyết định (đã ghi key). 1783 GHÉP trên fix U7b.
- **F24 (1132/1024/984/1711 + 1327/1783 đã GHÉP)** — Kisaki tự xưng → "em": 1132 bị trêu (thân mật), 1024 được Soutetsu khen (vui, thân mật), 984 bàn tuần trăng mật, "xin nghỉ 2–3 ngày" (thân mật; độ tin cậy thấp nhất như quyết định đã ghi — TW "新婚旅行" ủng hộ), 1711 hồi tưởng thời non nớt ở ngân hàng (dễ tổn thương), 1327 chuẩn bị để Soutetsu yêu mình (thân mật), 1783 "thành quả lớn nhất là cậu" (thân mật).
- **O3 (15 dòng lr_ニイロクh)** — Áp "Tôi" cho toàn bộ 15 dòng "em" (quyết định xem §5; JP 自分 đồng nhất cả 3 file). 1439 đổi cả hai token ("của mình"→"của tôi" + "em không hiểu nổi"→"Tôi không hiểu nổi"). 1293/1322/1339/1377/1438 old_vn là giá trị moan — chỉ đổi token đại từ, giữ nguyên token rên.

### lr_ニイロクh_誓い。約束.txt.toml — key 1211 [O3]

- JP: 「次の機会にも、絶対。愛撫のことも、そのほかのことも。\nもっとくわしく、もっとたくさん。絶対絶対、教えてね」
- TW: 「下次有機會，一定要教我。不管是愛撫，還是其他事情。一定一定要多教教我」
- old_vn: 「Dịp khác, nhất định nhé. Cả chuyện ái ân vuốt ve, và những chuyện khác nữa.\nChi tiết hơn, nhiều hơn nữa. Nhất định, nhất định phải dạy cho em đấy.」
- fix: 「Dịp khác, nhất định nhé. Cả chuyện ái ân vuốt ve, và những chuyện khác nữa.\nChi tiết hơn, nhiều hơn nữa. Nhất định, nhất định phải dạy cho tôi đấy.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1215 [O3]

- JP: 「そうじゃないの。無理なんて感じてない。\nセックスが愛の行為なら、自分は清春とセックスしたい」
- TW: 「不是的，我不是覺得勉強。如果做愛是愛的行為，我想和你做」
- old_vn: 「Không phải thế. Em không hề thấy khiên cưỡng.\nNếu làm tình là hành vi yêu đương, thì em muốn làm tình với Kiyoharu.」
- fix: 「Không phải thế. Tôi không hề thấy khiên cưỡng.\nNếu làm tình là hành vi yêu đương, thì tôi muốn làm tình với Kiyoharu.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1293 [O3]

- JP: 「ふあっ！？　指──清春──清春の、指、がっ──\nおっぱい──んっ──おっぱい──自分の、おっぱいを」
- TW: 「呼啊！？手指——清春——清春的手指——我的胸——嗯——在摸我的胸」
- old_vn: 「Fua!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu──\nngực──ưm──ngực──đang sờ ngực, của em」
- fix: 「Fua!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu──\nngực──ưm──ngực──đang sờ ngực, của tôi」

### lr_ニイロクh_誓い。約束.txt.toml — key 1322 [O3]

- JP: 「！　ならっ、これ、愛撫っ──ンっ──こしゅ。こしゅ、\nで──気持ち、よく、して、くれてるの──ふあっ」
- TW: 「啊！那這個、愛撫——嗯——摸來摸去——讓我這麼、舒服——呼啊」
- old_vn: 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho em, sướng──fua.」
- fix: 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho tôi, sướng──fua.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1339 [O3]

- JP: 「うん……ふっ、あ──できる。そのくらい、もちろん」
- TW: 「嗯……呼、啊——我能脫。這點事當然能做到」
- old_vn: 「Vâng... Fu, a──em làm được. Cỡ đó thì, tất nhiên rồi.」
- fix: 「Vâng... Fu, a──tôi làm được. Cỡ đó thì, tất nhiên rồi.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1377 [O3]

- JP: 「ぷぁっ──あの……\n清春……？　自分……体が──」
- TW: 「噗哈——那個……清春……？我的身體……」
- old_vn: 「Pua──ừm...\nKiyoharu...? Cơ thể... của em──」
- fix: 「Pua──ừm...\nKiyoharu...? Cơ thể... của tôi──」

### lr_ニイロクh_誓い。約束.txt.toml — key 1402 [O3]

- JP: 「にょうどうこう……ちっちゃな穴って思ってた。\nまわりがこんな……ぱかってするって、思ってなかった」
- TW: 「尿道口……我一直覺得它是個小洞而已。沒想到……周圍還能這樣張開」
- old_vn: 「Lỗ niệu đạo... em cứ nghĩ nó chỉ là một cái lỗ nhỏ.\nKhông ngờ... xung quanh lại mở toác ra thế này.」
- fix: 「Lỗ niệu đạo... tôi cứ nghĩ nó chỉ là một cái lỗ nhỏ.\nKhông ngờ... xung quanh lại mở toác ra thế này.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1438 [O3]

- JP: 「うれし、うれしい──んっ──あっ──\nふあっ！？　ふああぁんっっ！！」
- TW: 「我好開心、好開心——嗯——啊——呼啊！？呼啊啊啊！！」
- old_vn: 「Vui, em vui lắm──ưm──a──\nfua!? Fuaaan ư ư!!」
- fix: 「Vui, tôi vui lắm──ưm──a──\nfua!? Fuaaan ư ư!!」

### lr_ニイロクh_誓い。約束.txt.toml — key 1439 [O3]

- JP: 「こんなの、なかった──ん……自分、体──知らない。\nなの、に──どう、して──安、心……きもち、いい」
- TW: 「我從沒有過、這種感覺——嗯……自己的、身體——不知道還能這樣。可是——為什麼——這麼安心……這麼舒服」
- old_vn: 「Chưa từng, có cảm giác này──ưm... cơ thể, của mình──em không hiểu nổi.\nThế, mà──tại, sao──lại an, tâm... sướng, quá.」
- fix: 「Chưa từng, có cảm giác này──ưm... cơ thể, của tôi──Tôi không hiểu nổi.\nThế, mà──tại, sao──lại an, tâm... sướng, quá.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1457 [O3]

- JP: 「そうなの？　それなら、凄く、嬉しい」
- TW: 「是嗎？那我更開心了」
- old_vn: 「Vậy sao? Nếu thế thì, em rất, vui.」
- fix: 「Vậy sao? Nếu thế thì, tôi rất, vui.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1508 [O3]

- JP: 「あの、ね？　清春。愛の意味も、セックスの意味も。\nだって自分は、清春と一緒に知りたいって思うから」
- TW: 「聽我說，清春。不管是愛的意義，還是做愛的意義，我都想和你一起了解」
- old_vn: 「Anh biết không? Kiyoharu. Cả ý nghĩa của tình yêu, lẫn ý nghĩa của tình dục.\nBởi vì, em muốn được cùng Kiyoharu tìm hiểu chúng.」
- fix: 「Anh biết không? Kiyoharu. Cả ý nghĩa của tình yêu, lẫn ý nghĩa của tình dục.\nBởi vì, tôi muốn được cùng Kiyoharu tìm hiểu chúng.」

### lr_ニイロクh_誓い。約束.txt.toml — key 1534 [O3]

- JP: 「なに、これ……知らない。いままで、なかった。\nこんなの、一度も……は……ぅっ──んっ」
- TW: 「這是什麼感覺……我以前都不知道。我從來沒體驗過……呼啊……嗚——嗯」
- old_vn: 「Cái gì, thế này... em không biết. Từ trước đến giờ, chưa từng có.\nCảm giác này, chưa một lần nào... hà... ư──ưm」
- fix: 「Cái gì, thế này... tôi không biết. Từ trước đến giờ, chưa từng có.\nCảm giác này, chưa một lần nào... hà... ư──ưm」

### lr_ニイロクh_誓い。約束.txt.toml — key 1545 [O3]

- JP: 「その……えと……ゆ、び……動き……清春が──\n指……こしゅこしゅ──くちくち──とめて、くれたら」
- TW: 「那個……呃……手指的……動作……你的手指……摸來摸去的動作——能停下來的話」
- old_vn: 「Chuyện đó... ừm... ngón, tay... chuyển động... Kiyoharu──\nngón tay... cọ cọ──nhóp nhép──nếu anh dừng lại giúp em thì...」
- fix: 「Chuyện đó... ừm... ngón, tay... chuyển động... Kiyoharu──\nngón tay... cọ cọ──nhóp nhép──nếu anh dừng lại giúp tôi thì...」

### lr_ニイロクh_誓い。約束.txt.toml — key 1547 [O3]

- JP: 「ならっ、してっ、射精っ、おんなのこ、にっ──んうっ、\n精子、自分の、中──ちつに──たくさん、射精してっ」
- TW: 「那就、射精吧。在女孩子裡——嗯，把精液——射在我的裡面——陰道裡——都射出來吧」
- old_vn: 「Vậy thì, xuất tinh, đi, vào bé gái, đi──ưm,\ntinh trùng, vào bên trong, em──vào âm đạo──xuất thật nhiều, vào」
- fix: 「Vậy thì, xuất tinh, đi, vào bé gái, đi──ưm,\ntinh trùng, vào bên trong, tôi──vào âm đạo──xuất thật nhiều, vào」

### lr_ニイロクh_誓い。約束.txt.toml — key 1549 [O3]

- JP: 「なら、して？　セックス。\n愛の行為を、自分に、教えて」
- TW: 「那就來吧，我們來做愛。來告訴我什麼叫愛的行為」
- old_vn: 「Vậy thì, làm đi? Làm tình ấy.\nHãy dạy cho em biết, hành vi yêu đương là như thế nào.」
- fix: 「Vậy thì, làm đi? Làm tình ấy.\nHãy dạy cho tôi biết, hành vi yêu đương là như thế nào.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 720 [F20]

- JP: 「そうするといい。僕が言うと重すぎるかもしれんが、\n親孝行したいときには親は無し、だ」
- TW: 「……這樣啊，真有可能。要真是這樣的話，那我真要好好謝謝家父才行」
- old_vn: 「Nên làm vậy đi. Anh nói ra thì có thể hơi nặng nề, nhưng\ncây muốn lặng mà gió chẳng ngừng, tử dục dưỡng mà thân bất đãi đâu.」
- fix: 「Nên làm vậy đi. Tôi nói ra thì có thể hơi nặng nề, nhưng\ncây muốn lặng mà gió chẳng ngừng, tử dục dưỡng mà thân bất đãi đâu.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 984 [F24]

- JP: 「うん。ボクもそのほうがもちろん嬉しい。\n今回も、取れて２～３日程度にはなっちゃうだろうし」
- TW: 「不。新婚旅行我一定會再另行安排的。等私有線路基金移交都結束之後就馬上著手」
- old_vn: 「Ừm. Đương nhiên là tôi cũng muốn như vậy hơn.\nLần này chắc cũng chỉ xin nghỉ được tầm 2~3 ngày thôi.」
- fix: 「Ừm. Đương nhiên là em cũng muốn như vậy hơn.\nLần này chắc cũng chỉ xin nghỉ được tầm 2~3 ngày thôi.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1024 [F24]

- JP: 「ふふっ、ありがとう。双鉄に褒めて貰えると嬉しい。\nけど――そうだね。だからボクらは相性がいいのかも」
- TW: 「你這要是算普通的話，日本恐怕早就建立世界第一經濟大國的霸權了」
- old_vn: 「Fufu, cảm ơn nhé. Được Soutetsu khen tôi vui lắm.\nNhưng――đúng vậy nhỉ. Có lẽ vì thế mà chúng ta mới hợp nhau.」
- fix: 「Fufu, cảm ơn nhé. Được Soutetsu khen em vui lắm.\nNhưng――đúng vậy nhỉ. Có lẽ vì thế mà chúng ta mới hợp nhau.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1025 [F21]

- JP: 「かもしれんな。『そう導ける』と思ったがゆえ、\n元忠さんは姜さんを家庭教師に選んだのかもしれん」
- TW: 「你這麼一說的話，感覺就像是再我原本道行基礎上，給姜小姐打通了任督二脈的感覺」
- old_vn: 「Có thể lắm. Chắc vì nghĩ rằng 'có thể dẫn dắt như vậy',\nnên ông Mototada mới chọn cô Khương làm gia sư cho em.」
- fix: 「Có thể lắm. Chắc vì nghĩ rằng 'có thể dẫn dắt như vậy',\nnên ông Mototada mới chọn cô Khương làm gia sư cho cô.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1116 [F20]

- JP: 「買いかぶりすぎかとは思うが……\n稀咲が評価してくれるのであれば、そうかもしれんな」
- TW: 「只是準備的一小部分。因為你時常會靈光一現不是，所以預料之外的情況可能反而會成為發展的機會」
- old_vn: 「Anh nghĩ em đánh giá anh hơi cao rồi đấy……\nNhưng nếu Kisaki đã nhận xét vậy thì, chắc là thế thật.」
- fix: 「Tôi nghĩ cô đánh giá tôi hơi cao rồi đấy……\nNhưng nếu Kisaki đã nhận xét vậy thì, chắc là thế thật.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1132 [F24]

- JP: 「からかわないでよ。意地悪だなぁ。とにかくええと――\nああ、うん、そうだ、お茶菓子の用意もあるんだ」
- TW: 「哪裡哪裡，兩位如此恩愛。讓人看在眼裡又是歡喜又是羨慕」
- old_vn: 「Đừng trêu tôi nữa mà. Xấu tính ghê. Tóm lại là ừm――\nA, đúng rồi, đúng rồi, tôi có chuẩn bị cả bánh kẹo dùng kèm với trà nữa.」
- fix: 「Đừng trêu em nữa mà. Xấu tính ghê. Tóm lại là ừm――\nA, đúng rồi, đúng rồi, em có chuẩn bị cả bánh kẹo dùng kèm với trà nữa.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1187 [F21]

- JP: 「銀行が男社会で、舐められたくなくて気を張っていた\n――というような話だった」
- TW: 「嘻嘻，稱讚的話我就先收下了。那——我想想，剛才說到哪來著？」
- old_vn: 「Đang nói đến đoạn ngân hàng trọng nam khinh nữ, nên em luôn căng thẳng vì không muốn bị coi thường\n——đại loại thế.」
- fix: 「Đang nói đến đoạn ngân hàng trọng nam khinh nữ, nên cô luôn căng thẳng vì không muốn bị coi thường\n——đại loại thế.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1246 [F21]

- JP: 「ではいく方向で返事をしよう。具体的にどこを、\nあるいは何を視察してみたい、などの希望があるか？」
- TW: 「安排成徹底的商務考察我當然也贊成。這樣也有這樣的好，也會是段充實而快樂的時光」
- old_vn: 「Vậy tôi sẽ trả lời là chúng ta sẽ đi. Cụ thể thì em có nguyện vọng\nmuốn khảo sát ở đâu, hay muốn xem những gì không?」
- fix: 「Vậy tôi sẽ trả lời là chúng ta sẽ đi. Cụ thể thì cô có nguyện vọng\nmuốn khảo sát ở đâu, hay muốn xem những gì không?」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1249 [F21]

- JP: 「なるほど。いいな。実にいい。\nではその方向で姜さんに明日にでも返事をして欲しい」
- TW: 「完全交給姜小姐安排怎麼樣？我想看一看姜小姐究竟是打算讓我看些什麼」
- old_vn: 「Ra là vậy. Hay đấy. Rất hay.\nVậy em hãy trả lời cô Khương theo hướng đó vào ngày mai nhé.」
- fix: 「Ra là vậy. Hay đấy. Rất hay.\nVậy cô hãy trả lời cô Khương theo hướng đó vào ngày mai nhé.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1290 [F21]

- JP: 「恐ろしく似合っているので問題なかろう。\n社交の場での”[わたくし]私”も、実に可憐で素敵だが」
- TW: 「從小開始就以[ｂｏｋｕ]我自稱，也是源自於此吧。不過回頭想來，或許倒是起了反效果」
- old_vn: 「Thấy hợp đến đáng sợ nên chắc không sao đâu.\n Dù em xưng là "[watakushi]Tôi" trong các buổi giao tế cũng rất đáng yêu và tuyệt vời.」
- fix: 「Thấy hợp đến đáng sợ nên chắc không sao đâu.\n Dù cô xưng là "[watakushi]Tôi" trong các buổi giao tế cũng rất đáng yêu và tuyệt vời.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1322 [F20]

- JP: 「その選択は大正解だったのだなと感じるよ。\n僕の知る稀咲の、稀咲らしさの根源であるようにさえ」
- TW: 「我覺得這是一套非常可靠的方法論。所以我選擇學習掌握了它」
- old_vn: 「Anh cảm thấy lựa chọn đó là hoàn toàn chính xác.\nThậm chí nó giống như cội nguồn tạo nên một Kisaki mang đậm chất Kisaki mà anh biết vậy.」
- fix: 「Tôi cảm thấy lựa chọn đó là hoàn toàn chính xác.\nThậm chí nó giống như cội nguồn tạo nên một Kisaki mang đậm chất Kisaki mà tôi biết vậy.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1327 [F22]

- JP: 「キミに関する情報は、日々姫がいくらでもくれたから。\nキミに恋してもらえるよう、ボクは出来るだけ準備した」
- TW: 「我？」
- old_vn: 「Thông tin về anh, Hibiki đã cung cấp cho tôi rất nhiều.\nĐể khiến anh yêu tôi, tôi đã chuẩn bị kỹ càng nhất có thể.」
- fix: 「Thông tin về cậu, Hibiki đã cung cấp cho em rất nhiều.\nĐể khiến cậu yêu em, em đã chuẩn bị kỹ càng nhất có thể.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1371 [F21]

- JP: 「真闇姉たちにも予め話を通してあったようだったしな」
- TW: 「既然是親手做的話，考慮到姜小姐的性格，我就覺得在右田家這樣像聚會的感覺她會更喜歡」
- old_vn: 「Có vẻ như em cũng đã báo trước với chị Mayami rồi nhỉ.」
- fix: 「Có vẻ như cô cũng đã báo trước với chị Mayami rồi nhỉ.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1534 [F21]

- JP: 「僕の目に映る稀咲は、完全に理想的な[バンカー,2]銀行家だ。\n未熟なころがあったなど、まったく想像もつかんほどに」
- TW: 「說起來，我這是在銀行一路幹到現在啊。組建基金說到底也還是銀行的工作」
- old_vn: 「Trong mắt tôi, Kisaki hoàn toàn là một chủ ngân hàng lý tưởng.\nĐến mức không thể tưởng tượng nổi em từng có thời non nớt đấy.」
- fix: 「Trong mắt tôi, Kisaki hoàn toàn là một chủ ngân hàng lý tưởng.\nĐến mức không thể tưởng tượng nổi cô từng có thời non nớt đấy.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1538 [F21]

- JP: ふっと、稀咲が身を寄せてくる。\n腕を伸ばせば、それを枕にしてくれる。
- TW: 「謝謝。即便真如你所言，那也完全是拜姜小姐和——把姜小姐介紹給我的家父所賜」
- old_vn: Bất chợt, Kisaki nép sát vào người tôi.\nKhi tôi dang tay ra, em liền dùng nó làm gối đầu.
- fix: Bất chợt, Kisaki nép sát vào người tôi.\nKhi tôi dang tay ra, cô liền dùng nó làm gối đầu.

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1564 [F22]

- JP: 「でもね？　ボクや姜さんはそうじゃない。\nポーレットとかもお仲間だよね。閃かないタイプ」
- TW: 「這太抬舉我了，受之有愧啊……不過若是稀咲這麼評價的話，也說不定真就是這樣」
- old_vn: 「Nhưng anh biết không? Em và cô Khương lại không như thế.\nCả chị Paulette cũng giống tụi em. Đều là tuýp người không có ý tưởng bất chợt.」
- fix: 「Nhưng cậu biết không? Em và cô Khương lại không như thế.\nCả chị Paulette cũng giống tụi em. Đều là tuýp người không có ý tưởng bất chợt.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1587 [F22]

- JP: 「うん。ありがと。\n……今度、三人で食事にでもいこう」
- TW: 「那是自然。這話我說可能不太合適，但千萬別等到子欲養而親不待，是吧」
- old_vn: 「Vâng. Cảm ơn anh.\n……Hôm nào đó, ba chúng ta cùng đi ăn nhé.」
- fix: 「Vâng. Cảm ơn cậu.\n……Hôm nào đó, ba chúng ta cùng đi ăn nhé.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1711 [F24]

- JP: 「あの頃ボクは、年齢的にも精神的にも小娘だった。\n銀行で働き始めることになって、完全に空回りしていた」
- TW: 她溫暖的語調中洋溢著懷念。而這也瞬間激起了我對接下來內容的興趣。
- old_vn: 「Hồi đó tôi, cả về tuổi tác lẫn tinh thần đều chỉ là một con nhóc.\nBắt đầu làm việc ở ngân hàng, tôi hoàn toàn luống cuống.」
- fix: 「Hồi đó em, cả về tuổi tác lẫn tinh thần đều chỉ là một con nhóc.\nBắt đầu làm việc ở ngân hàng, em hoàn toàn luống cuống.」

### lr稀咲追加01_仲国視察の誘い.txt.toml — key 1783 [F22]

- JP: 「けど、姜さんが“ボクにあうやり方”を教えてくれた。\nその一番の成果物なら、キミだよ？　双鉄」
- TW: 我清晰地感受到了稀咲的心跳。不得不承認，稀咲的雙峰又有所成長。
- old_vn: 「Nhưng, cô Khương đã dạy tôi 'cách làm phù hợp với bản thân'.\nThành quả lớn nhất của điều đó, chính là anh đấy? Soutetsu.」
- fix: 「Nhưng, cô Khương đã dạy em 'cách làm phù hợp với bản thân'.\nThành quả lớn nhất của điều đó, chính là cậu đấy? Soutetsu.」

### lr稀咲追加02_仲国視察.txt.toml — key 1077 [F21]

- JP: 「かなり強い同意を受けたように思ったが――\n仲国国鉄の餐車や寝台車も、同じような感じなのか？」
- TW: 「似乎你們也深有同感的樣子——莫非仲國的餐車和臥鋪車也都經歷了類似的過程嗎？
- old_vn: 「Tôi có cảm giác em rất đồng tình với điều này——\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trung Quốc cũng giống như vậy sao?」
- fix: 「Tôi có cảm giác cô rất đồng tình với điều này——\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trung Quốc cũng giống như vậy sao?」

### lr稀咲追加02_仲国視察.txt.toml — key 1089 [F21]

- JP: 「図をみただけでそこまで理解できるのか、\n説明の必要もなかったな。素晴らしい読解力だ」
- TW: 「光是看看圖就能理解到這個程度了，應該就不需要我解釋了吧。真是出眾的理解能力」
- old_vn: 「Chỉ nhìn hình vẽ mà em đã hiểu được đến mức đó sao,\nchẳng cần tôi phải giải thích nữa. Khả năng đọc hiểu tuyệt vời thật.」
- fix: 「Chỉ nhìn hình vẽ mà cô đã hiểu được đến mức đó sao,\nchẳng cần tôi phải giải thích nữa. Khả năng đọc hiểu tuyệt vời thật.」

### lr稀咲追加02_仲国視察.txt.toml — key 1118 [F21]

- JP: 「すごい、よく覚えていたな」
- TW: 「厲害，記得這麼清楚」
- old_vn: 「Tuyệt thật, em nhớ rõ thế.」
- fix: 「Tuyệt thật, cô nhớ rõ thế.」

### lr稀咲追加02_仲国視察.txt.toml — key 1188 [F21]

- JP: 「ああ、そうだった。オイラン車の実物を見せるのが、\n建築限界の説明にもっとも早いかと考えたのだが……」
- TW: 「啊，對哦。我本來想的是直接看看花魁車的實物，比解釋建築限界來得會更快更直接的……」
- old_vn: 「A, đúng rồi. Tôi cứ nghĩ cho em xem tận mắt chiếc xe Oiran\nsẽ là cách nhanh nhất để giải thích về giới hạn kiến trúc……」
- fix: 「A, đúng rồi. Tôi cứ nghĩ cho cô xem tận mắt chiếc xe Oiran\nsẽ là cách nhanh nhất để giải thích về giới hạn kiến trúc……」

### lr稀咲追加02_仲国視察.txt.toml — key 1216 [F21]

- JP: 「うむ。その解釈で間違いない」
- TW: 「嗯，這麼解釋沒錯」
- old_vn: 「Ừm. Em hiểu như vậy là hoàn toàn chính xác.」
- fix: 「Ừm. Cô hiểu như vậy là hoàn toàn chính xác.」

### lr稀咲追加02_仲国視察.txt.toml — key 1568 [F21]

- JP: 「アドバイスをありがとう。けど、大丈夫だ」
- TW: 「謝謝你的提醒，不過我們是不用擔心這個問題的」
- old_vn: 「Cảm ơn lời khuyên của em. Nhưng mà, không sao đâu.」
- fix: 「Cảm ơn lời khuyên của cô. Nhưng mà, không sao đâu.」

### lr稀咲追加02_仲国視察.txt.toml — key 1761 [F21]

- JP: ああ、そこまでは知識の中になかったか。\nここが鉄道博物館なら……っと。
- TW: 啊，她看來還沒有接觸到這部分的知識。既然這裡是鐵路博物館……哦。
- old_vn: A, ra là kiến thức của em ấy chưa đến mức đó.\nNếu đây đã là bảo tàng đường sắt thì…… à.
- fix: A, ra là kiến thức của cô ấy chưa đến mức đó.\nNếu đây đã là bảo tàng đường sắt thì…… à.

### lr稀咲追加02_仲国視察.txt.toml — key 1910 [F21]

- JP: 稀咲が親指を唇に当てる。\n爪を噛むかと思いきや、気づいたように手を戻す。
- TW: 稀咲用拇指抵住了嘴唇。我剛在想她是不是想要咬指甲，她彷彿意識到一般把手又放下了。
- old_vn: Kisaki đưa ngón cái lên chạm vào môi.\nTôi cứ tưởng em ấy định cắn móng tay, nhưng như chợt nhận ra, em ấy lại bỏ tay xuống.
- fix: Kisaki đưa ngón cái lên chạm vào môi.\nTôi cứ tưởng cô ấy định cắn móng tay, nhưng như chợt nhận ra, cô ấy lại bỏ tay xuống.

### ニイロク02_御一夜旅行.txt.toml — key 1166 [F18]

- JP: 「『だ、大丈夫ですっ』――って？　え？　\n――“と”？」
- TW: 「“我、我沒事”——等一下，咦，“唄”？」
- old_vn: 「『Tôi, tôi không sao』――hả? Hả?\n――'Chứ'?」
- fix: 「『Tôi, tôi không sao』――hả? Hả?\n――'To'?」

### ニイロク02_御一夜旅行.txt.toml — key 1547 [F17]

- JP: 「あらニイロクちゃん。大丈夫よ？\nいまは、お夕飯の支度中」
- TW: 「哎呀，是二六？四六沒有在工作。現在在準備晚餐」
- old_vn: 「Ôi bé Niiroku. Chị nghe đây?\nChị đang chuẩn bị bữa tối.」
- fix: 「Ôi bé Niiroku. Em có sao không?\nChị đang chuẩn bị bữa tối.」

### ニイロク02_御一夜旅行.txt.toml — key 1570 [F19]

- JP: 「は！\nわかった。と思う。このマンガには、きっと」
- TW: 「啊！我懂了。這本漫畫裡一定有——」
- old_vn: 「A!\nEm hiểu rồi. Chắc vậy. Trong cuốn manga này, chắc chắn có...」
- fix: 「A!\nTôi hiểu rồi. Chắc vậy. Trong cuốn manga này, chắc chắn có...」

### ニイロク02_御一夜旅行.txt.toml — key 1788 [F19]

- JP: 「それに……わかった。\nわかった、気が、する」
- TW: 「而且……我好像明白了。大概是明白了」
- old_vn: 「Hơn nữa...... em hiểu rồi.\nCó cảm giác, là đã hiểu rồi.」
- fix: 「Hơn nữa...... tôi hiểu rồi.\nCó cảm giác, là đã hiểu rồi.」

### ニイロク02_御一夜旅行.txt.toml — key 1878 [F19]

- JP: 「決まってる。赤井運転士のこと。\n自分はもっと、赤井運転士とお話ししたい」
- TW: 「那當然是赤井駕駛員了。我想和赤井駕駛員多說說話」
- old_vn: 「Rõ ràng quá rồi. Chuyện của lái tàu Akai.\nEm muốn được nói chuyện nhiều hơn với lái tàu Akai.」
- fix: 「Rõ ràng quá rồi. Chuyện của lái tàu Akai.\nTôi muốn được nói chuyện nhiều hơn với lái tàu Akai.」

### 稀咲h2_プライベートルーム.txt.toml — key 933 [P3]

- JP: 「……言われてみれば――\n確かに、そうした傾向はあるかもしれんな」
- TW: 「……這麼說來――的確是有這方面的傾向吧」
- old_vn: 「……Nghe em nói vậy thì――\nCó lẽ anh đúng là có khuynh hướng như thế thật」
- fix: 「……Nghe cô nói vậy thì――\nCó lẽ anh đúng là có khuynh hướng như thế thật」

### 稀咲h2_プライベートルーム.txt.toml — key 1334 [P3]

- JP: 「稀咲――イクなら、一緒にイキたい」
- TW: 「稀咲――要高潮的話，我想跟你一起」
- old_vn: 「Kisaki――Nếu ra, anh muốn ra cùng em」
- fix: 「Kisaki――Nếu ra, anh muốn ra cùng cô」

### 稀咲h2_プライベートルーム.txt.toml — key 1338 [P3]

- JP: 「稀咲……体の力を抜けるか？」
- TW: 「稀咲……可以放鬆一點嗎？」
- old_vn: 「Kisaki…… em thả lỏng cơ thể ra được không?」
- fix: 「Kisaki…… cô thả lỏng cơ thể ra được không?」
## §4. Giữ nguyên / đã đúng (đã kiểm chứng, không sửa)

- **Niiroku01 1563/1907 — GIỮ cả hai (F25).** JP cố ý viết khác nhau: 1563 「シロおねえちゃん」→ "chị Shiro"; 1907 「Ｄ６０ ４６おねえちゃん」→ "Chị D60 46". Không đổi.
- **tsuika01 1516 — GIỮ "tôi" (F24).** JP 「ボクがもしもいなくても、キミなら」— Kisaki trấn an Soutetsu một cách quyết đoán ("Không đâu, Soutetsu. Không có chuyện đó đâu. | Ngay cả khi không có tôi, nếu là cậu thì"); ranh giới như 1744 (tỏ tình giữ "tôi" — giọng quả quyết). VN đã có "cậu" cho キミ — đúng sẵn.
- **tsuika01 1488/1687 — F23 đã xong bởi U7b, không dòng mới.** 1488 old_vn = fix U7b ("Soutetsu thuộc tuýp người hay nảy ra ý tưởng bất chợt mà"); 1687 old_vn = fix U7b ("Sao vậy? Soutetsu."). Không còn token "anh Soutetsu". Lưu ý: 1488 câu 2 "Anh có thể biến những tình huống ngoài dự kiến thành cơ hội phát triển." — "Anh" trần chỉ Soutetsu, U7b để lại; xem cờ F-P3-1 ở §6 (cùng mẫu tsuika02 1084).
- **tsuika01 1564 — "Em"/"tụi em" GIỮ.** F22 chỉ đổi "anh"→"cậu" ở dòng này. "Em và cô Khương" / "tụi em" là Kisaki tự xưng — không nằm trong danh sách F24 (1327/1132/1024/984/1711/1783), ngữ cảnh là tán gẫu ở bữa tối (không quyết đoán kiểu công việc, cũng không thân mật/dễ tổn thương rõ rệt). Không tự mở rộng F24.
- **tsuika02 — "em" = Suika, GIỮ:** 1051 "Suika, cảm ơn em vì bản vẽ tuyệt vời này", 1153 "em am hiểu cả đường sắt của Trung Quốc và Hinomoto" (người am hiểu hai nền đường sắt là Suika — 1155 Kisaki hỏi cô về Master đời trước), 1190 "em là Railord của nguyên mẫu thử nghiệm" (Suika), 1595 "em có thể làm người hướng dẫn" (Suika). 718 "Em gái sao?" = 妹機 (đầu máy em gái Dongfu 4), không phải Kisaki.
- **tsuika02 1233 — GIỮ "tôi" (O2, xem §5).**
- **tsuika03 — toàn bộ cụm đại từ đã sửa xong trong audit (17 dòng), không còn việc cho pass:** Soutetsu "anh"→"tôi" (941/1054/1171/1432), Soutetsu→Kisaki "em"→"cô" (963/990/1573), Kisaki "anh Soutetsu"→tên trần (938/1294/1433/1434), "anh"→"cậu" (940/1026/1189), Kisaki "tôi"→"em" thân mật (896/906/1007/1026). Hai dòng "em ấy" còn lại không phải Kisaki: 1435 (Soutetsu nói về Nagi), 1711 (độc thoại nói về Dương Nương).

## §5. Quyết định các mục OPEN (theo uỷ quyền của Hieu)

### O3 — lr_ニイロクh: ÁP "Tôi" cho cả 15 dòng "em" (1211/1215/1293/1322/1339/1377/1402/1438/1439/1457/1508/1534/1545/1547/1549)

- **Bằng chứng JP:** Niiroku tự xưng bằng 自分 ở cả 3 file, không có sự khác biệt nào về đại từ JP giữa file h và 01/02 — đếm máy trên dòng thoại ニイロク: lr_ニイロクh 自分 ×8 (わたし/あたし/わたくし ×0); ニイロク01 自分 ×14 (+わたし ×1); ニイロク02 自分 ×20. Phân bố 15 "em"/0 "Tôi" ở file h là lệch của bản dịch, không phải chuyển register trong JP.
- **Bằng chứng VN:** quyết định 22/11 ~03:32 đã chốt phẳng "Niiroku tự xưng với Akai → Tôi" (31 "Tôi" vs 3 "Em" ở 01/02; trang trọng vì cô gọi Akai là 赤井運転士) — không có ngoại lệ H-scene nào được chốt. File h toàn là Niiroku với Akai, nên quy tắc áp nguyên vẹn. Các dòng có 自分 tường minh trong JP: 1215, 1293 (自分の、おっぱい), 1377 (自分……体), 1508, 1547 (自分の中), 1549 (自分に).
- **1439:** đổi cả "của mình"→"của tôi" (JP 自分 sở hữu) lẫn "em không hiểu nổi"→"Tôi không hiểu nổi" (chủ ngữ ngầm của 知らない).
- **Không đổi:** Niiroku gọi Akai "anh" (1508 "Anh biết không? Kiyoharu"; P22 đã chốt) và Akai gọi Niiroku "cô" — nhất quán, không sửa.

### O2 — Kisaki tự xưng: các dòng ranh giới (XÁC NHẬN các phán đoán biên của audit — 0 dòng đổi)

- **Hiệu chỉnh nhãn file trong list:** các key 896/906/940/1007/1026 KHÔNG nằm ở 稀咲h2 (file đó không có các key này) mà ở **`lr稀咲追加03_新事業案.txt.toml`** (tsuika03) — audit file đó đã ghi đúng. Key 1233 ("lúc nắm tay") KHÔNG nằm ở 稀咲h1 (file đó không có key 1233) mà ở **tsuika02 1233**. List ghi sai tên file; key thì đúng.
- **tsuika03 896/906/1007/1026 — XÁC NHẬN audit đã đổi "tôi"→"em" là đúng, giữ nguyên giá trị audit (không đưa vào JSON):**
  - 896: Kisaki tự giễu "Đúng là em――à không, chúng ta cuồng công việc quá nhỉ" — vợ chồng nhận ra mình nói chuyện công việc mọi lúc (cả trên máy bay lẫn trong phòng); thân mật, tự trào → "em" đúng.
  - 906: "Em ấy nhé, cũng rất thích việc tình tứ về mặt logic nữa" — nói về イチャイチャ (tình tứ) với chồng → "em" đúng.
  - 1007: "Thực sự thì lần này em có tài giỏi không ta. | Qua một đêm, em cảm thấy cũng có khá nhiều vấn đề đấy" — lo lắng về năng lực của mình, hỏi ý Soutetsu; TW "這一次我的表現能算讓你滿意嗎？" (lần này表現 của em có làm anh hài lòng không?) ủng hộ → "em" đúng, kể cả khi đây là dòng tin cậy thấp nhất.
  - 1026: "Fufu, nếu cậu nghĩ vậy thì em rất vui" — vui vì được chồng khen → "em" đúng. (Audit cũng đã đổi "anh"→"cậu" ở dòng này — đúng hướng F22.)
- **tsuika03 940 — XÁC NHẬN GIỮ "tôi":** "Cậu không hiểu sao? Vậy, tôi sẽ nói cho cậu biết một điều hay ho nhé" — giọng quyết đoán/trêu chọc trong bàn luận công việc (game/business plan) → "tôi" đúng, ranh giới như 1744.
- **tsuika02 1233 — GIỮ "tôi":** JP 「双鉄が、ボクをエスコートしてくれるから」— Kisaki nói với Suika trong bàn luận khảo sát (người nghe là Suika: 1225/1229 Kisaki đều nói với Suika; 1231 Soutetsu chỉ "Ồ"), về việc Soutetsu hộ tống mình — ngữ cảnh công việc, không thân mật/dễ tổn thương → "tôi" đúng. Token "anh Soutetsu" giữ theo quyết định U7b (ngôi ba — nói về Soutetsu với Suika). Nhãn "cảnh nắm tay" trong list là nhầm: dòng này nói về hộ tống (エスコート), cảnh nắm tay thật ở tsuika02 là độc thoại 1900, không có thoại Kisaki.

### P5 / tsuika02 — Rà lại 22 dòng "Tôi" của Kisaki: GIỮ HẾT, 0 dòng đổi

- **Phạm vi rà:** quét máy toàn bộ dòng Kisaki nói ở tsuika02 có "Tôi"/"tôi" tự xưng số ít (loại "chúng tôi" số nhiều — trung tính — và "em" gọi Suika — đúng): 1035, 1072, 1084, 1176, 1179, 1210, 1233, 1239, 1258, 1286, 1325, 1331, 1332, 1334, 1373, 1383, 1466, 1501, 1599, 1616, 1644, 1678 = **22 dòng**.
- **Kết luận:** toàn file là chuyến khảo sát công việc ở Trọng Quốc, có Khương và Suika cùng tham gia — Kisaki ở chế độ công việc xuyên suốt (thảo luận, lập kế hoạch, phân tích, trao đổi lịch sự). Không dòng nào thân mật/dễ tổn thương theo quy tắc 19:45. Đoạn kết thân mật (nắm tay trong buồng lái Dongfu, 1900) hoàn toàn là độc thoại — không có dòng thoại Kisaki nào mang "Tôi" ở đó để đổi.
- **Hai ghi chú trong list không đứng vững:** (a) "15 dòng → em" — đếm lại là 22 dòng, và không dòng nào đủ điều kiện đổi; con số 15 không tái tạo được. (b) "1184 là ranh giới như 1744" — key 1184 ở tsuika02 là dòng gasp của Soutetsu (「っ！！！」→"Ư!!!"), không phải dòng đại từ; ở tsuika01 key 1184 không tồn tại. Tham chiếu này VOID. Ranh giới 1744 thật (tỏ tình giữ "tôi") vẫn được áp đúng ở tsuika01 1516.
- **Ngoài phạm vi U8:** hai nhánh còn lại của P5 — Kisaki03 ("tôi" công việc vs "em" thân mật theo file) và 稀咲02 (16 dòng "tôi") — không thuộc cụm Niiroku + tsuika; để lại cho coordinator phân batch.

## §6. Cờ cho coordinator / hiệu chỉnh số liệu

- **F-P3-1 — P1 chưa có batch nào nhận (lớn nhất):** quy tắc P1 (Soutetsu "Tôi" với Kisaki) chưa từng được áp cho 稀咲h2. Quét máy: 18 dòng 双鉄H còn "Anh"/"anh" tự xưng với Kisaki (915 "cho anh xem sao?", 932, 933*, 1207, 1226, 1230, 1233, 1236, 1265, 1271, 1273, 1275, 1278, 1295, 1302, 1313, 1321, 1334* — * = đã sửa token "em"→"cô" ở đợt này nhưng "Anh" vẫn giữ). Cần một batch P1 riêng (hoặc gộp vào batch P1 tương lai) — U8 không tự mở rộng vì P1 không nằm trong mục được giao. Cùng mẫu: tsuika01 1488 câu 2 "Anh có thể biến..." và tsuika02 1084 "Anh đang định giải thích cho tôi" — "Anh" trần chỉ Soutetsu, U7b để lại, cần quyết chung có đổi thành "Soutetsu" không.
- **F-P3-2 — Hiệu chỉnh số liệu F21 (§8 C20 sai):** tsuika02 thực tế là **8 dòng**, không phải 9. Ba key "đếm thiếu" trong C20 đều VOID: 1180 là gasp của Suika (「ぁっ」→"A."), 1168 là "A——" của Soutetsu (không có "em"), 1043 không tồn tại ở cả hai file tsuika. F21 tổng thực tế = **17 dòng (9 tsuika01 + 8 tsuika02)**, không phải 18. P3 tổng cộng (kèm h2 3 dòng) = 20 dòng.
- **F-P3-3 — tsuika02 1077/1568 (người nghe xác định bằng loại trừ, độ tin cậy trung-cao):** 1077 "em rất đồng tình" — trong đoạn trao đổi chỉ có Kisaki + Khương nói; Khương không bao giờ là "em" với Soutetsu; Suika vắng mặt → Kisaki. 1568 "Cảm ơn lời khuyên của em" — nội dung "lời khuyên" duy nhất kề trước là phân tích marketing của Kisaki (1564–1565); Suika không đưa lời khuyên nào; Khương không phải "em" → Kisaki. Nếu coordinator thấy cần, có thể đảo ngược hai dòng này — nhưng bằng chứng hiện tại nghiêng về Kisaki.
- **F-P3-4 — tsuika01 1564 "Em" giữ lại:** không nằm trong danh sách F24; nếu batch P5 tương lai rà lại Kisaki tự xưng ở tsuika01, đây là dòng duy nhất còn "Em" chưa được quyết (ngữ cảnh tán gẫu bữa tối, trung tính).
- **F-P3-5 — P5 nhánh Kisaki03 + 稀咲02 chưa có batch:** xem §5 (để lại cho coordinator).
- **F-P3-6 — O2 nhãn file sai trong list (đã hiệu chỉnh ở §5):** 896/906/940/1007/1026 thuộc lr稀咲追加03, 1233 thuộc lr稀咲追加02 — không phải 稀咲h2 / 稀咲h1. Đề nghị coordinator sửa nhãn trong UNIFICATION-LIST.md §7 O2 khi gộp (U8 không sửa list).

## §7. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix đối chiếu JP)

- **Tổng: 50 dòng xét / 50 tái kiểm chứng / 0 loại / 0 sửa.**
- Đọc lại từng fix trong bảng §7a (đối chiếu JP, không chỉ parse-check): F17/F18 đúng quyết định; F19/F20/O3 mọi token "em"/"Anh" đã đổi đúng vị trí ngữ pháp (chủ ngữ, tân ngữ, sở hữu); F21/P3 mọi "em"→"cô" đúng người nghe (đã loại Suika/Khương/Nagi/Dương Nương); F22 mọi "anh"→"cậu" đúng người nghe Soutetsu; F24 mọi "tôi"→"em" đúng ngữ cảnh thân mật; 1327/1783/1116 GHÉP đúng cả hai token.
- Kiểm chứng máy bổ sung (quét token sót trong fix): F21/P3 0 token "em" còn sót (16/16 dòng kiểm tra — 1116 tính ở F20); F22 0 token "anh" còn sót; F24 0 token "tôi" còn sót; F20 0 token "anh" còn sót; F19/O3 0 token "em" còn sót. (1564 giữ "Em" có chủ ý — xem §4 — nên không nằm trong quét F22.)
- old_vn kiểm chứng cơ học 50/50 khớp đúng lớp nguồn (CSV3 40 / audit 3 / moan 5 / unification đã gộp 2). Không dòng nào re-fix giá trị đã đúng; không dòng gasp-Ư hay "Kh" nào bị động.

## §8. Khối TOML (parse-verified)

5 file / 50 key. Giá trị `\\n` trong khối là literal backslash-n (theo quy ước brief); parse bằng tomllib cho đúng giá trị fix trong JSON.

### lr_ニイロクh_誓い。約束.txt.toml

```toml
[script]
"1211" = "「Dịp khác, nhất định nhé. Cả chuyện ái ân vuốt ve, và những chuyện khác nữa.\\nChi tiết hơn, nhiều hơn nữa. Nhất định, nhất định phải dạy cho tôi đấy.」"
"1215" = "「Không phải thế. Tôi không hề thấy khiên cưỡng.\\nNếu làm tình là hành vi yêu đương, thì tôi muốn làm tình với Kiyoharu.」"
"1293" = "「Fua!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu──\\nngực──ưm──ngực──đang sờ ngực, của tôi」"
"1322" = "「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\\nthế này──là đang làm cho tôi, sướng──fua.」"
"1339" = "「Vâng... Fu, a──tôi làm được. Cỡ đó thì, tất nhiên rồi.」"
"1377" = "「Pua──ừm...\\nKiyoharu...? Cơ thể... của tôi──」"
"1402" = "「Lỗ niệu đạo... tôi cứ nghĩ nó chỉ là một cái lỗ nhỏ.\\nKhông ngờ... xung quanh lại mở toác ra thế này.」"
"1438" = "「Vui, tôi vui lắm──ưm──a──\\nfua!? Fuaaan ư ư!!」"
"1439" = "「Chưa từng, có cảm giác này──ưm... cơ thể, của tôi──Tôi không hiểu nổi.\\nThế, mà──tại, sao──lại an, tâm... sướng, quá.」"
"1457" = "「Vậy sao? Nếu thế thì, tôi rất, vui.」"
"1508" = "「Anh biết không? Kiyoharu. Cả ý nghĩa của tình yêu, lẫn ý nghĩa của tình dục.\\nBởi vì, tôi muốn được cùng Kiyoharu tìm hiểu chúng.」"
"1534" = "「Cái gì, thế này... tôi không biết. Từ trước đến giờ, chưa từng có.\\nCảm giác này, chưa một lần nào... hà... ư──ưm」"
"1545" = "「Chuyện đó... ừm... ngón, tay... chuyển động... Kiyoharu──\\nngón tay... cọ cọ──nhóp nhép──nếu anh dừng lại giúp tôi thì...」"
"1547" = "「Vậy thì, xuất tinh, đi, vào bé gái, đi──ưm,\\ntinh trùng, vào bên trong, tôi──vào âm đạo──xuất thật nhiều, vào」"
"1549" = "「Vậy thì, làm đi? Làm tình ấy.\\nHãy dạy cho tôi biết, hành vi yêu đương là như thế nào.」"
```

### lr稀咲追加01_仲国視察の誘い.txt.toml

```toml
[script]
"720" = "「Nên làm vậy đi. Tôi nói ra thì có thể hơi nặng nề, nhưng\\ncây muốn lặng mà gió chẳng ngừng, tử dục dưỡng mà thân bất đãi đâu.」"
"984" = "「Ừm. Đương nhiên là em cũng muốn như vậy hơn.\\nLần này chắc cũng chỉ xin nghỉ được tầm 2~3 ngày thôi.」"
"1024" = "「Fufu, cảm ơn nhé. Được Soutetsu khen em vui lắm.\\nNhưng――đúng vậy nhỉ. Có lẽ vì thế mà chúng ta mới hợp nhau.」"
"1025" = "「Có thể lắm. Chắc vì nghĩ rằng 'có thể dẫn dắt như vậy',\\nnên ông Mototada mới chọn cô Khương làm gia sư cho cô.」"
"1116" = "「Tôi nghĩ cô đánh giá tôi hơi cao rồi đấy……\\nNhưng nếu Kisaki đã nhận xét vậy thì, chắc là thế thật.」"
"1132" = "「Đừng trêu em nữa mà. Xấu tính ghê. Tóm lại là ừm――\\nA, đúng rồi, đúng rồi, em có chuẩn bị cả bánh kẹo dùng kèm với trà nữa.」"
"1187" = "「Đang nói đến đoạn ngân hàng trọng nam khinh nữ, nên cô luôn căng thẳng vì không muốn bị coi thường\\n——đại loại thế.」"
"1246" = "「Vậy tôi sẽ trả lời là chúng ta sẽ đi. Cụ thể thì cô có nguyện vọng\\nmuốn khảo sát ở đâu, hay muốn xem những gì không?」"
"1249" = "「Ra là vậy. Hay đấy. Rất hay.\\nVậy cô hãy trả lời cô Khương theo hướng đó vào ngày mai nhé.」"
"1290" = "「Thấy hợp đến đáng sợ nên chắc không sao đâu.\\n Dù cô xưng là \"[watakushi]Tôi\" trong các buổi giao tế cũng rất đáng yêu và tuyệt vời.」"
"1322" = "「Tôi cảm thấy lựa chọn đó là hoàn toàn chính xác.\\nThậm chí nó giống như cội nguồn tạo nên một Kisaki mang đậm chất Kisaki mà tôi biết vậy.」"
"1327" = "「Thông tin về cậu, Hibiki đã cung cấp cho em rất nhiều.\\nĐể khiến cậu yêu em, em đã chuẩn bị kỹ càng nhất có thể.」"
"1371" = "「Có vẻ như cô cũng đã báo trước với chị Mayami rồi nhỉ.」"
"1534" = "「Trong mắt tôi, Kisaki hoàn toàn là một chủ ngân hàng lý tưởng.\\nĐến mức không thể tưởng tượng nổi cô từng có thời non nớt đấy.」"
"1538" = "Bất chợt, Kisaki nép sát vào người tôi.\\nKhi tôi dang tay ra, cô liền dùng nó làm gối đầu."
"1564" = "「Nhưng cậu biết không? Em và cô Khương lại không như thế.\\nCả chị Paulette cũng giống tụi em. Đều là tuýp người không có ý tưởng bất chợt.」"
"1587" = "「Vâng. Cảm ơn cậu.\\n……Hôm nào đó, ba chúng ta cùng đi ăn nhé.」"
"1711" = "「Hồi đó em, cả về tuổi tác lẫn tinh thần đều chỉ là một con nhóc.\\nBắt đầu làm việc ở ngân hàng, em hoàn toàn luống cuống.」"
"1783" = "「Nhưng, cô Khương đã dạy em 'cách làm phù hợp với bản thân'.\\nThành quả lớn nhất của điều đó, chính là cậu đấy? Soutetsu.」"
```

### lr稀咲追加02_仲国視察.txt.toml

```toml
[script]
"1077" = "「Tôi có cảm giác cô rất đồng tình với điều này——\\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trung Quốc cũng giống như vậy sao?」"
"1089" = "「Chỉ nhìn hình vẽ mà cô đã hiểu được đến mức đó sao,\\nchẳng cần tôi phải giải thích nữa. Khả năng đọc hiểu tuyệt vời thật.」"
"1118" = "「Tuyệt thật, cô nhớ rõ thế.」"
"1188" = "「A, đúng rồi. Tôi cứ nghĩ cho cô xem tận mắt chiếc xe Oiran\\nsẽ là cách nhanh nhất để giải thích về giới hạn kiến trúc……」"
"1216" = "「Ừm. Cô hiểu như vậy là hoàn toàn chính xác.」"
"1568" = "「Cảm ơn lời khuyên của cô. Nhưng mà, không sao đâu.」"
"1761" = "A, ra là kiến thức của cô ấy chưa đến mức đó.\\nNếu đây đã là bảo tàng đường sắt thì…… à."
"1910" = "Kisaki đưa ngón cái lên chạm vào môi.\\nTôi cứ tưởng cô ấy định cắn móng tay, nhưng như chợt nhận ra, cô ấy lại bỏ tay xuống."
```

### ニイロク02_御一夜旅行.txt.toml

```toml
[script]
"1166" = "「『Tôi, tôi không sao』――hả? Hả?\\n――'To'?」"
"1547" = "「Ôi bé Niiroku. Em có sao không?\\nChị đang chuẩn bị bữa tối.」"
"1570" = "「A!\\nTôi hiểu rồi. Chắc vậy. Trong cuốn manga này, chắc chắn có...」"
"1788" = "「Hơn nữa...... tôi hiểu rồi.\\nCó cảm giác, là đã hiểu rồi.」"
"1878" = "「Rõ ràng quá rồi. Chuyện của lái tàu Akai.\\nTôi muốn được nói chuyện nhiều hơn với lái tàu Akai.」"
```

### 稀咲h2_プライベートルーム.txt.toml

```toml
[script]
"933" = "「……Nghe cô nói vậy thì――\\nCó lẽ anh đúng là có khuynh hướng như thế thật」"
"1334" = "「Kisaki――Nếu ra, anh muốn ra cùng cô」"
"1338" = "「Kisaki…… cô thả lỏng cơ thể ra được không?」"
```

## Kết bài

U8 xong 14/14 mục được giao (P3, P5, P6, P8, F17–F24, O2, O3) với **50 dòng sửa / 5 file**. Hai mục OPEN đã quyết theo uỷ quyền, có bằng chứng ghi lại: **O2 — xác nhận toàn bộ phán đoán biên của audit** (tsuika03 896/906/1007/1026 giữ "em", 940 giữ "tôi"; tsuika02 1233 giữ "tôi"); **O3 — áp "Tôi" cho cả 15 dòng "em" ở lr_ニイロクh** (JP 自分 đồng nhất cả 3 file — phân bố đảo ngược là lệch của bản dịch). P5 ở tsuika02 rà xong 22 dòng, giữ hết. Hai hiệu chỉnh số liệu quan trọng đã ghi ở §6: F21 thực tế 17 dòng (không phải 18 — C20 sai), và P1 còn ~18 dòng Soutetsu "Anh" ở 稀咲h2 chưa có batch nào nhận. File nộp: `unification-s2-niiroku-tsuika-cluster-wrong.json` (50 mục) + snippet `unification-snippet-s2-niiroku-tsuika-cluster.md`. Không sửa ROUTE-UNIFICATION.md, queue hay MEMORY.md — chờ coordinator gộp.
