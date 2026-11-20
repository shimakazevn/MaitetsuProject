# Audit — ハチロク06_それぞれの傷跡.txt.toml

- File: `ハチロク06_それぞれの傷跡.txt.toml` — route 01_Hachiroku, 407 dòng script (74 thoại Hachiroku, 62 thoại Soutetsu, 39 thoại Paulette, 33 thoại Hibiki, 16 thoại Reina, 183 độc thoại).
- Nội dung: Hachiroku phát hiện khung gầm (台枠) của 8620 bị biến dạng; Soutetsu thừa nhận mình rất sợ tai nạn đường sắt và định ngừng vận hành 8620 để bảo vệ Hachiroku; hiểu lầm giữa hai người — Hachiroku tưởng Soutetsu đang trách mình, bỏ chạy, rồi được Hibiki làm trung gian hoà giải; song song là kế hoạch tàu BBQ + đổi biểu đồ chạy tàu (khớp giờ tàu du lịch với tàu định kỳ) và nỗi lo về thời hạn 2 năm mà cha của Mayami đã cho.
- **Kết quả: 24/407 dòng sai (5,9%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (407 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 407/407 (0 lệch thực chất — 262 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. Không có bản sao file này (md5 `c27fb7616a7462dcc5232456dbb9e977`; không thuộc 11 nhóm trùng — đã kiểm tra).
- Đại từ: Soutetsu tự xưng "tôi" với Hachiroku đúng toàn file (quét máy: 0 lần "anh" ở các dòng 双鉄); Soutetsu gọi Hachiroku "em" đúng; Hachiroku tự xưng "em" trong thoại; Hibiki tự xưng "chị"; Paulette tự xưng "tôi", gọi Soutetsu "anh Soutetsu" (B4 lock, vd. 1764, 2009); Reina gọi Soutetsu "anh Soutetsu", gọi Hachiroku "chị Hachiroku"; Paulette gọi Hachiroku "Bé Hachiroku" (2037). Độc thoại Hachiroku dùng "tôi" ở ~30 dòng, chỉ 6 dòng lạc sang "em" (đã sửa §2: 2356, 2420, 2455, 2474, 2768, 2797).
- Thuật ngữ chờ đợt thống nhất (không sửa, không tính sai): "Ohimitera" 4 dòng (1710, 1819, 2706, 2710) thay cho "Ohitoyo" đã chốt; "tuyến Yui" 2 dòng (1801, 2710) thay cho "Yunoi" đã chốt. Các thuật ngữ khác đúng: Aircra (1819, 2696, 2706), Railord, KiHa 07 (1737, 2771), 保火→"giữ lửa", 粘着力→"lực bám đường", 台枠→"khung gầm", 8620.
- Thẻ %l: 3 dòng VN tự thêm thẻ gloss cho 8620 (JP chỉ có ruby) — đã sửa §2. Không có thẻ %l sai định dạng nào trong file.

## §2. Danh sách sửa (24 dòng)

Phân loại: gasp 9 (1613, 1638, 1648, 1974, 1979, 2025, 2026, 2031, 2629 — 5 từ sweep + 2 sweep bỏ sót + 2 đính chính sweep), đại từ 8 (1770, 1991, 2356, 2420, 2455, 2474, 2768, 2797), tag 3 (1556, 1710, 1784), nghĩa 3 (1654, 2350, 2800), SFX 1 (2598).

### 1556 — 日々姫 — tag
- JP: 「[この子,3]8620はさ、たくさんの人を喜ばせたでしょ？\n“[ハチロク,3]8620運転台通信”も、もっとたくさんに読まれてる」
- TW: 「其實啊，喜歡著[這孩子,3]８６２０的人不是很多嗎？而“[八六,3]８６２０駕駛台通信”的讀者，那就更多啦」
- VN cũ: 「\x%l8620;#00ffc040;8620%l;#; đã mang lại niềm vui cho rất nhiều người đúng không?\n"Bản tin buồng lái \x%l8620;#00ffc040;8620%l;#;" cũng đang được rất nhiều người đọc nữa.」
- Sửa: 「8620 đã mang lại niềm vui cho rất nhiều người đúng không?\n"Bản tin buồng lái 8620" cũng đang được rất nhiều người đọc nữa.」
- Lý do: JP chỉ có ruby [この子,3]/[ハチロク,3] cho 8620, không có thẻ %l; VN tự thêm 2 thẻ gloss (đã kiểm chứng comment # JP trong TOML). Gỡ theo tiền lệ (file Paulette: 3076 8620 — JP chỉ có ruby, VN tự thêm thẻ thì gỡ).

### 1613 — 双鉄 — gasp
- JP: 「っ」
- TW: 「呃」
- VN cũ: 「Ưm」
- Sửa: 「Ư」
- Lý do: JP 「っ」 cả dòng là gasp; っ→"Ư" theo quy tắc đã chốt. VN "Ưm" thêm đuôi m (âm của む/ん, vd. 1628 む→"Ưm"); sweep bỏ sót vì VN đã có một âm diễn. Tiền lệ: reina-h3 1050 bare っ→「Ư」.

### 1638 — ハチロク — gasp
- JP: 「っ！！」
- TW: 「啊！！」
- VN cũ: 「A!!」
- Sửa: 「Ư!!」
- Lý do: JP 「っ！！」 là gasp; sweep ghi "already-rendered" nhưng "A" diễn âm あ chứ không phải っ — đính chính như tiền lệ sweep review §9.4 (4 dòng already-rendered đã bị audit bác: lr_h1 1044/1045, lr_h2 1009/1124). っ→"Ư" theo quy tắc.

### 1648 — 双鉄 — gasp
- JP: 「っ」
- TW: 「嗯」
- VN cũ: 「Ưm」
- Sửa: 「Ư」
- Lý do: như 1613 — bare っ→「Ư」; "Ưm" là âm của む/ん. TW 「嗯」 cũng diễn thành âm mũi nhưng JP thắng TW.

### 1654 — ポーレット — nghĩa
- JP: 「双鉄くんに……」
- TW: 「在雙鐵君嗎……」
- VN cũ: 「Do anh Soutetsu……」
- Sửa: 「Anh Soutetsu……」
- Lý do: JP là câu cụt chỉ còn tên + に, không có nghĩa nhân quả nào; VN tự thêm "Do" (vì) là bịa phần hoàn thiện câu cụt — vi phạm quy tắc "không tự hoàn thiện JP cụt". Giữ dạng cụt như JP; phần tiếp theo của câu không rõ nên ghi chờ Hieu xác nhận ngữ cảnh (§6).

### 1710 — 日々姫 — tag
- JP: 「御一夜の人たちと、観光に来てくれた人たちと――\n[この子,3]8620を好きな人、思ってるよりたくさんいるよ？」
- TW: 「御一夜的人們，以及慕名而來的觀光客們——喜歡著[這孩子,3]８６２０的人，或許比你想像得更多哦」
- VN cũ: 「Những người dân Ohimitera, những vị khách đến tham quan――\nCó nhiều người yêu mến \x%l8620;#00ffc040;8620%l;#; hơn em nghĩ đấy.」
- Sửa: 「Những người dân Ohimitera, những vị khách đến tham quan――\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」
- Lý do: như 1556 — JP chỉ có ruby, VN tự thêm thẻ gloss. "Ohimitera" giữ nguyên chờ đợt thống nhất (→"Ohitoyo").

### 1770 — ハチロク — đại từ
- JP: 「でしたら……最初からそうとおっしゃってくだされば」
- TW: 「既然這樣，為什麼一開始不直接跟我說啊」
- VN cũ: 「Nếu vậy…… giá như ngài ấy nói cho em biết ngay từ đầu.」
- Sửa: 「Nếu vậy…… giá như ngài nói cho em biết ngay từ đầu.」
- Lý do: Hachiroku nói trực tiếp với Soutetsu — dãy 1770→1771→1772→1773 cùng cảnh (1771 「ご命令されたのですか」 hỏi chính Soutetsu về mệnh lệnh của ngài; thứ tự khóa trong TOML cũng là thứ tự truyện). 「おっしゃってくだされば」 = "giá như ngài nói" (ngôi 2), VN "ngài ấy" (ngôi 3) sai ngôi.

### 1784 — 日々姫 — tag
- JP: 「でしょ？　にぃにだもん。\n[この子,3]8620のことも、見捨てたりとか、絶対しないよ」
- TW: 「是吧？畢竟是阿哥啊。拋棄[這孩子,3]８６２０這種事，他肯定是做不出來的啦」
- VN cũ: 「Đúng không? Vì là anh hai mà.\nAnh ấy tuyệt đối sẽ không bao giờ bỏ rơi \x%l8620;#00ffc040;8620%l;#; đâu.」
- Sửa: 「Đúng không? Vì là anh hai mà.\nAnh ấy tuyệt đối sẽ không bao giờ bỏ rơi 8620 đâu.」
- Lý do: như 1556/1710 — JP chỉ có ruby, VN tự thêm thẻ gloss.

### 1974 — ハチロク — gasp (sweep)
- JP: 「聞くもなにも――事故が怖いなど、当然で――っ！」
- TW: 「這還要問嗎，害怕事故，那還不是理所當然——啊！」
- VN cũ: 「Hỏi han gì chứ――sợ tai nạn là chuyện đương nhiên mà――!」
- Sửa: 「Hỏi han gì chứ――sợ tai nạn là chuyện đương nhiên mà――Ư!」
- Lý do: gasp cuối dòng ――っ！ bị mất; nhận nguyên fix sweep (lost-gasp-trailing), đã kiểm chứng jp/tw/old_vn khớp CSV3.

### 1979 — ハチロク — gasp
- JP: 「っ！」
- TW: 「這！」
- VN cũ: 「Chuyện đó!」
- Sửa: 「Ư!」
- Lý do: JP chỉ là một tiếng gasp; VN 「Chuyện đó!」 bịa hẳn một cụm từ không có trong JP (sweep ghi "needs-file-audit" đúng vì lý do này). Fix 「Ư!」 theo quy tắc っ.

### 1991 — 双鉄 — đại từ
- JP: 「ならば、それでよろしく頼めるか？」
- TW: 「那可以就選定這個方案嗎？」
- VN cũ: 「Nếu vậy thì, nhờ cô tiến hành theo cách đó được không?」
- Sửa: 「Nếu vậy thì, nhờ em tiến hành theo cách đó được không?」
- Lý do: Soutetsu hỏi Paulette (người điều phối phương án BBQ/timetable); Soutetsu gọi Paulette là "em" theo quy tắc đã chốt (Soutetsu→Paulette = "em"), VN "cô" sai. Tiền lệ: file Paulette đã sửa 11 dòng "cô"→"em" tương tự.

### 2025 — ハチロク — gasp (sweep)
- JP: 「っ！！？」
- TW: 「！！？」
- VN cũ: 「!!?」
- Sửa: 「Ư!!?」
- Lý do: gasp cả dòng bị mất; nhận nguyên fix sweep (lost-gasp-whole), đã kiểm chứng jp/tw/old_vn khớp CSV3.

### 2026 — ハチロク — gasp (sweep)
- JP: 「っ！？」
- TW: 「！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: như 2025 — gasp cả dòng bị mất; nhận nguyên fix sweep (lost-gasp-whole).

### 2031 — れいな (Paulette & Reina) — gasp (sweep)
- JP: 『「――っ！」\n「あっ」』
- TW: 『「——呃！」\n「啊」』
- VN cũ: 『「――!」\n「A」』
- Sửa: 『「――Ư!」\n「A」』
- Lý do: gasp ――っ！ ở nửa đầu bị mất; nhận nguyên fix sweep (lost-gasp-trailing). Nửa sau あっ→"A" đã đúng, giữ nguyên.

### 2350 — độc thoại (Hachiroku) — nghĩa
- JP: 「嬉しくて。ほっとして。\nけれど、少し――ほんの少しだけ、口惜しいです。」
- TW: 「喜悅和安心感湧上心頭。不過，還是有點，有那麼一點點委屈。」
- VN cũ: 「Thật vui. Thật nhẹ nhõm.\nNhưng mà, tôi cũng cảm thấy hơi――một chút xíu thôi, hơi hối hận.」
- Sửa: 「Thật vui. Thật nhẹ nhõm.\nNhưng mà, tôi cũng cảm thấy hơi――một chút xíu thôi, hơi không cam lòng.」
- Lý do: 口惜しい = 悔しい (ấm ức/không cam lòng vì sự việc đáng tiếc), không phải "hối hận" (ăn năn về việc mình đã làm) — sai cảm xúc. TW 委屈 cũng lệch. Theo tiền lệ: file trước đã sửa 口惜しい "cam chịu" → "không cam lòng".

### 2356 — độc thoại (Hachiroku) — đại từ
- JP: 「あと二年、無理な運行を続ければ、歪みは回復不能となり、\n\x%l8620;#00ffc040;[あの子,3]8620%l;#;を――わたくしの分身を、必ず壊してしまいますから。」
- TW: 「因為再持續勉強行駛兩年的話，這扭曲會變得無法修復，如同我分身一般的\x%l8620;#00ffc040;[那孩子,3]８６２０%l;#;也必然會徹底損壞。」
- VN cũ: 「Nếu cứ tiếp tục gượng ép chạy thêm hai năm nữa, sự biến dạng sẽ không thể phục hồi,\nvà chắc chắn sẽ phá hủy \x%l8620;#00ffc040;8620%l;#;――phân thân của em mất.」
- Sửa: 「Nếu cứ tiếp tục gượng ép chạy thêm hai năm nữa, sự biến dạng sẽ không thể phục hồi,\nvà chắc chắn sẽ phá hủy \x%l8620;#00ffc040;8620%l;#;――phân thân của tôi mất.」
- Lý do: độc thoại Hachiroku (わたくし) dùng "tôi" — đây là 1 trong 6 dòng độc thoại lạc sang "em" trong khi ~30 dòng độc thoại còn lại trong file đều dùng "tôi" (vd. 2226, 2238, 2426, 2463). "Em" là tự xưng trong thoại, không dùng trong độc thoại.

### 2420 — độc thoại (Hachiroku) — đại từ
- JP: 「わたくし――わたくしは――\nしかし、わたくしは\x%lレイルロオド;#00ffc040;レイルロオド%l;#;なのですし――」
- TW: 「我、我——但是，我只是\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;啊……」
- VN cũ: 「Còn em――em thì――\nNhưng mà, em chỉ là một \x%lレイルロオド;#00ffc040;Railord%l;#; thôi mà――」
- Sửa: 「Còn tôi――tôi thì――\nNhưng mà, tôi chỉ là một \x%lレイルロオド;#00ffc040;Railord%l;#; thôi mà――」
- Lý do: như 2356 (3 lần "em"→"tôi").

### 2455 — độc thoại (Hachiroku) — đại từ
- JP: 「だからわたくしも応えたくって、頑張って。\nなのに、わたくしの\x%l8620;#00ffc040;8620%l;#;が――双鉄様の重荷となって……」
- TW: 「所以我也想回應他的期待，一直在努力著。然而，我的\x%l8620;#00ffc040;８６２０%l;#;，卻成了雙鐵少爺的重擔……」
- VN cũ: 「Nên em cũng muốn đáp lại, em đã cố gắng hết sức.\nThế mà \x%l8620;#00ffc040;8620%l;#; của em――lại trở thành gánh nặng cho ngài Soutetsu……」
- Sửa: 「Nên tôi cũng muốn đáp lại, tôi đã cố gắng hết sức.\nThế mà \x%l8620;#00ffc040;8620%l;#; của tôi――lại trở thành gánh nặng cho ngài Soutetsu……」
- Lý do: như 2356 (3 lần "em"→"tôi").

### 2474 — độc thoại (Hachiroku) — đại từ
- JP: 「でしたら、わたくしは……\nわたくしが行うべきは、ひとつです。」
- TW: 「既然這樣，我……我該做的事自然別無選擇。」
- VN cũ: 「Nếu vậy thì, em……\nViệc em nên làm, chỉ có một thôi.」
- Sửa: 「Nếu vậy thì, tôi……\nViệc tôi nên làm, chỉ có một thôi.」
- Lý do: như 2356 (2 lần "em"→"tôi").

### 2598 — độc thoại (Soutetsu) — SFX
- JP: 「汚れた膝を拭いもせずに、\nぐっ、とハチロクが詰め寄ってくる。」
- TW: 「無暇擦去膝蓋上的汙漬，八六徑直向我衝了過來。」
- VN cũ: 「Không thèm lau đi vết bẩn trên đầu gối,\nHachiroku tiến sát lại gần tôi.」
- Sửa: 「Không thèm lau đi vết bẩn trên đầu gối,\nHachiroku bất chợt tiến sát lại gần tôi.」
- Lý do: ぐっ (âm cử động đột ngột khi sấn tới) bị bỏ mất hoàn toàn; thêm "bất chợt" để giữ âm. Đây là っ-mimetic duy nhất trong file bị bỏ (các っ khác đều đã diễn thành từ Việt hoặc là っ nhấn mạnh — xem §3).

### 2629 — độc thoại — gasp (sweep)
- JP: 「強い力で線路を捕まえ、その車軸が強く拗じられるなら、\n当然強いパワーを生むが、負荷はその分大きく――っ！」
- TW: 「當車輪與線路間摩擦力足夠時，以強力扭動車軸的話，當然就可以輸出相應的大推力，負擔也自然隨之水漲船高。」
- VN cũ: 「Nếu bám chặt vào đường ray bằng một lực mạnh, và trục bánh xe bị vặn xoắn mạnh,\nthì đương nhiên sẽ tạo ra sức mạnh lớn, nhưng tải trọng cũng sẽ lớn theo tương ứng――!」
- Sửa: 「Nếu bám chặt vào đường ray bằng một lực mạnh, và trục bánh xe bị vặn xoắn mạnh,\nthì đương nhiên sẽ tạo ra sức mạnh lớn, nhưng tải trọng cũng sẽ lớn theo tương ứng――Ư!」
- Lý do: gasp cuối dòng ――っ！ bị mất; nhận fix sweep (lost-gasp-trailing) nhưng giữ nguyên dấu \n của CSV3 (sweep dùng bản TOML đã làm phẳng \n thành khoảng trắng — đã chuẩn lại theo CSV3).

### 2768 — độc thoại (Hachiroku) — đại từ
- JP: 「そのような、こと――\nそのようなこと……わたくしは、決して行いません。」
- TW: 「這種事……這種事……我是斷然不會做的。」
- VN cũ: 「Chuyện như vậy――\nChuyện như vậy…… em tuyệt đối sẽ không làm.」
- Sửa: 「Chuyện như vậy――\nChuyện như vậy…… tôi tuyệt đối sẽ không làm.」
- Lý do: như 2356.

### 2797 — độc thoại (Hachiroku) — đại từ
- JP: 「双鉄様は、不具合があると承知の上で、\nわたくしの\x%l機関士;#00ffc040;機関士%l;#;となり、あれほど頑張ってくださった。」
- TW: 「雙鐵少爺明知我有故障，卻還義無反顧地成為了我的\x%l機関士;#00ffc040;司機%l;#;，為此付出了那麼多努力。」
- VN cũ: 「Ngài Soutetsu dù biết rõ em bị lỗi,\nnhưng vẫn trở thành \x%l機関士;#00ffc040;Lái tàu%l;#; của em, và đã cố gắng vì em đến nhường nào.」
- Sửa: 「Ngài Soutetsu dù biết rõ tôi bị lỗi,\nnhưng vẫn trở thành \x%l機関士;#00ffc040;Lái tàu%l;#; của tôi, và đã cố gắng vì tôi đến nhường nào.」
- Lý do: như 2356 (3 lần "em"→"tôi"). "Lái tàu" giữ nguyên — kiểm chứng toàn dự án: 機関士 được dịch "Lái tàu" ở cả 105/105 dòng độc thoại và 204/204 dòng thoại có từ này, dạng đầy đủ "thợ lái đầu máy" không xuất hiện lần nào, nên "Lái tàu" là chuẩn thực tế.

### 2800 — độc thoại — nghĩa
- JP: 「双鉄様のお手がギュウっと握られている。\n握られて、ふるふると小さく震えてる。」
- TW: 「雙鐵少爺的手緊緊地握了起來。不只是握起來，還在輕微地顫抖著。」
- VN cũ: 「Bàn tay ngài Soutetsu đang nắm chặt lại.\nNắm chặt đến mức run lên bần bật.」
- Sửa: 「Bàn tay ngài Soutetsu đang nắm chặt lại.\nNắm chặt đến mức run rẩy nhè nhẹ.」
- Lý do: JP 小さく = run nhẹ; VN "run lên bần bật" (run dữ dội) ngược mức độ. TW 輕微地 cũng xác nhận "nhẹ".

## §3. Sweep っ-gasp kiểm chứng

- Sweep có đúng 7 mục cho file này: 1974, 2025, 2026, 2031, 2629 (fix) + 1638 (already-rendered) + 1979 (needs-file-audit). Nhận nguyên 5 fix sweep sau khi kiểm chứng jp/tw/old_vn khớp CSV3 (2629: chuẩn lại dấu \n theo CSV3, xem §2).
- 1638 already-rendered — ĐÍNH CHÍNH: VN "A!!" diễn âm あ, không phải っ; sửa thành 「Ư!!」 (tiền lệ sweep review §9.4: 4 dòng already-rendered đã bị audit bác).
- 1979 needs-file-audit — đã giải quyết trong audit: VN 「Chuyện đó!」 bịa từ cho một tiếng gasp; sửa thành 「Ư!」.
- Quét máy bổ sung toàn file: bắt thêm 2 gasp sweep bỏ sót — 1613, 1648 (bare っ→"Ưm"; tiền lệ reina-h3 1050: bare っ→「Ư」).
- Các っ còn lại đều đã được diễn (はっ→"Ha", んんっ→"ưm", ふわわっ→"ơ ơ", ん……っと→"Ưm……", ザっ/ピンっ→"Xoạt!"/"Cốc!", ぐいっ→"Lau") hoặc là っ nhấn mạnh cuối câu gắn vào từ (2017 双鉄様っ, 1458 くださいましっ, 1610 ハチロクさんっ, 1773 双鉄様はっ — không thêm Ư theo quy tắc) hoặc っ trong từ/động từ đã dịch thành từ Việt (だだっ子, きゅっと→"mím chặt", きょろっと→"đảo quanh", ぽっと, 気付かなかった…). Không còn gasp nào sót.

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- Key 1474: TW thêm "去找雙鐵少爺" (đi tìm ngài Soutetsu) không có trong JP; VN 「Em――đi đây.」 theo đúng JP — giữ.
- Key 2247: JP 数秒 ("vài giây"), TW ghi 五秒 (năm giây) sai; VN "Vài giây" theo JP — giữ (JP thắng TW).
- Key 2391: TW hiểu sai thành người khác nói với Hachiroku ("幫我回到平常的樣子，對我說…"); JP là Hachiroku tự chọn lời của chính mình; VN theo đúng JP — giữ.
- Key 1850: JP cụt 「双鉄様から……直接に」; VN "trực tiếp nghe" theo ngữ cảnh (1966: にぃにの口から…聞かねば — phải nghe từ chính miệng anh hai); TW "問" (hỏi) khác — giữ VN, ghi chú ở §6.
- Key 1759: JP cụt, VN hoàn thiện "dù cho em có……" khớp TW — giữ.
- Key 2773: JP cụt 「双鉄さまは、きっと、誰のことさえも。」; VN hoàn thiện "sẽ không bỏ rơi bất kỳ ai" theo động từ 見捨てる đã chốt ở 1784 — giữ.
- Key 1619: ふぁ là tiếng ngáp → "Oáp" (diễn ngẫu hứng theo nhân vật/cảnh, không áp quy tắc fa/fu vốn dành cho tiếng thở) — giữ.
- Key 1628/2691/2737: む/ん → "Ưm" — giữ (âm mũi, đúng âm).
- Key 2426: 機関士 → "Lái tàu" trong độc thoại — giữ (kiểm chứng toàn dự án ở §2/2797: dạng đầy đủ không được dùng lần nào).
- Key 1211: VN==TW 「…………」 — chỉ là dấu lặng, đúng — giữ.
- Key 2687: VN thêm "ngáp" (Reina há miệng) — TW 打著哈欠 xác nhận — giữ.
- Key 1547/1455/1484/2496: các lược nhỏ (từ "à" cuối câu cụt; また; "tỏ ra"; 鮮やかに→"gọn gàng") — giữ, không tính sai vì nghĩa cốt lõi còn nguyên và TW cũng lược tương tự.
- Key 2804: 『Hãy tin tôi, bây giờ em cứ nghỉ ngơi đi』 là lời Soutetsu trích dẫn, "em" = Hachiroku (người nghe) — giữ. Key 2662/2675/2371: "em ấy" chỉ Hachiroku ở ngôi 3 trong độc thoại Soutetsu — giữ.
- Key 2037/2043: hai giọng Paulette + Reina cùng lúc — "Bé Hachiroku"/"Chị Hachiroku" và "Anh Soutetsu" ×2 đều đúng — giữ.
- Thuật ngữ chờ đợt thống nhất: "Ohimitera" (1710, 1819, 2706, 2710), "tuyến Yui" (1801, 2710) — không sửa trong audit này, chờ Hieu chốt đợt thống nhất.
- Không có VN trùng bất thường trong file (0 cặp VN trùng dài ≥8 ký tự ở khóa khác nhau); VN trùng trong file đều là câu ngắn/SFX chung — không phải nhiễm chéo.

## §5. Khối TOML (đã parse-kiểm chứng: 24 khóa, 0 sai lệch)
```toml
[script]
"1556" = "「8620 đã mang lại niềm vui cho rất nhiều người đúng không?\\n\"Bản tin buồng lái 8620\" cũng đang được rất nhiều người đọc nữa.」"
"1613" = "「Ư」"
"1638" = "「Ư!!」"
"1648" = "「Ư」"
"1654" = "「Anh Soutetsu……」"
"1710" = "「Những người dân Ohimitera, những vị khách đến tham quan――\\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」"
"1770" = "「Nếu vậy…… giá như ngài nói cho em biết ngay từ đầu.」"
"1784" = "「Đúng không? Vì là anh hai mà.\\nAnh ấy tuyệt đối sẽ không bao giờ bỏ rơi 8620 đâu.」"
"1974" = "「Hỏi han gì chứ――sợ tai nạn là chuyện đương nhiên mà――Ư!」"
"1979" = "「Ư!」"
"1991" = "「Nếu vậy thì, nhờ em tiến hành theo cách đó được không?」"
"2025" = "「Ư!!?」"
"2026" = "「Ư!?」"
"2031" = "『「――Ư!」\\n「A」』"
"2350" = "Thật vui. Thật nhẹ nhõm.\\nNhưng mà, tôi cũng cảm thấy hơi――một chút xíu thôi, hơi không cam lòng."
"2356" = "Nếu cứ tiếp tục gượng ép chạy thêm hai năm nữa, sự biến dạng sẽ không thể phục hồi,\\nvà chắc chắn sẽ phá hủy \\x%l8620;#00ffc040;8620%l;#;――phân thân của tôi mất."
"2420" = "Còn tôi――tôi thì――\\nNhưng mà, tôi chỉ là một \\x%lレイルロオド;#00ffc040;Railord%l;#; thôi mà――"
"2455" = "Nên tôi cũng muốn đáp lại, tôi đã cố gắng hết sức.\\nThế mà \\x%l8620;#00ffc040;8620%l;#; của tôi――lại trở thành gánh nặng cho ngài Soutetsu……"
"2474" = "Nếu vậy thì, tôi……\\nViệc tôi nên làm, chỉ có một thôi."
"2598" = "Không thèm lau đi vết bẩn trên đầu gối,\\nHachiroku bất chợt tiến sát lại gần tôi."
"2629" = "Nếu bám chặt vào đường ray bằng một lực mạnh, và trục bánh xe bị vặn xoắn mạnh,\\nthì đương nhiên sẽ tạo ra sức mạnh lớn, nhưng tải trọng cũng sẽ lớn theo tương ứng――Ư!"
"2768" = "Chuyện như vậy――\\nChuyện như vậy…… tôi tuyệt đối sẽ không làm."
"2797" = "Ngài Soutetsu dù biết rõ tôi bị lỗi,\\nnhưng vẫn trở thành \\x%l機関士;#00ffc040;Lái tàu%l;#; của tôi, và đã cố gắng vì tôi đến nhường nào."
"2800" = "Bàn tay ngài Soutetsu đang nắm chặt lại.\\nNắm chặt đến mức run rẩy nhè nhẹ."
```

## §6. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 24/24 fix đọc lại đối chiếu JP — 24 giữ nguyên, 0 bỏ, 0 sửa. (Lượt soát có xét lại 1638: giữ quyết định đính chính already-rendered của sweep — "A" diễn âm あ, không phải っ; và 1654: giữ dạng cụt 「Anh Soutetsu……」 thay vì hoàn thiện câu.)
- Chờ Hieu (không tự quyết):
  1. Key 1654 — câu cụt 「双鉄くんに……」 của Paulette: phần tiếp theo không rõ (hỏi Soutetsu? nghe từ Soutetsu? nhờ Soutetsu?). Fix hiện tại chỉ gỡ "Do" bịa và giữ dạng cụt; nếu Hieu biết ngữ cảnh cảnh này thì chốt nghĩa đầy đủ.
  2. Đợt thống nhất: "Ohimitera"→"Ohitoyo" (1710, 1819, 2706, 2710) và "tuyến Yui"→"tuyến Yunoi" (1801, 2710) — chờ Hieu chốt phạm vi/thời điểm.
  3. Key 1850 — 「双鉄様から……直接に」: VN hiện "trực tiếp nghe" theo ngữ cảnh 1966; TW dùng "hỏi" (問). Nếu Hieu muốn khớp TW thì đổi thành "trực tiếp hỏi".

## Kết bài

File ハチロク06_それぞれの傷跡 đã audit xong toàn bộ 407 dòng: 24 dòng sai (5,9%) — 9 gasp (5 từ sweep + 2 sweep bỏ sót + 2 đính chính already-rendered/needs-file-audit), 8 đại từ (1 Soutetsu→Paulette "cô"→"em", 1 ngôi "ngài ấy"→"ngài", 6 độc thoại Hachiroku "em"→"tôi"), 3 tag (VN tự thêm thẻ gloss cho 8620), 3 nghĩa (1654, 2350, 2800), 1 SFX (2598). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 24 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 24/24, 0 bỏ, 0 sửa. Chờ Hieu: 1654 (câu cụt Paulette), đợt thống nhất Ohimitera/Yui, 1850 ("nghe" hay "hỏi").
