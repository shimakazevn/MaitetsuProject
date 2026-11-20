# Audit — 凪ふかみ06_凪の欲しいもの.txt.toml (07_Nagi_Fukami)

- File: `07_Nagi_Fukami/凪ふかみ06_凪の欲しいもの.txt.toml` — 445 dòng script (monologue 153, 双鉄 149, 凪 106, 真闇 37). TOML md5 `11f7a6a2ef37148c3336561fce88dc9f`, không có bản trùng trong `sources/toml2/` (chỉ 1 file trùng tên/md5; queue ghi 1 copy — khớp).
- CSV3: 1 bộ duy nhất 445 dòng, key không trùng, 0 VN trống, 0 JP trống, 0 TW trống. Đối chiếu phẳng TOML↔CSV3: chỉ 1 "lệch" — key 1844 TOML gộp 2 khoảng trắng thành 1 (CSV có 2 khoảng trắng sau dấu `?`) — là artefact làm phẳng của TOML-2, không phải lỗi dịch, không tính sai.
- Phương pháp: đọc toàn bộ 445 dòng theo từng dòng, đối chiếu JP + TW, xác nhận người nghe từ các dòng kề trong file (thứ tự key trong file tăng dần, đúng thứ tự trong TOML).
- Kết quả: **36 dòng sai / 445 (8,1%)**.

## Phân loại sai (36)

- Đại từ (pronoun): 14 — 13 Soutetsu tự xưng sai (11 với Mayami → "tôi": 1796, 1853, 1859, 1897, 1959, 2018, 2074, 2076, 2170, 2182 là "em"→"tôi" + 2030 "anh"→"tôi"; 2 với Nagi → "anh": 1601, 1626 là "em"→"anh") + 1 Nagi gọi Soutetsu "nó" → "anh" (2131).
- SFX — đếm nguyên âm (sfx-vowel): 8 — 1757, 1816, 1817, 1835, 1836, 1839, 2079, 2180.
- Thuật ngữ (terminology): 7 — Ohitoyo 5 (1878, 2016, 2021, 2598, 2735), Yunoi 2 (1890, 2021 — 2021 gộp cả 2 thuật ngữ trong 1 dòng), thân bảo trì 1 (1259).
- Gasp っ bị mất (lost-gasp): 5 — 1231, 1755, 1820, 1821, 1988 (cả 5 đều có trong sweep, đã kiểm chứng lại từng dòng).
- Từ bịa thêm (invented-word): 1 — 2336 ("Nhưng mà." không có trong JP/TW).
- Đọc sai (misread): 1 — 2649 ("chị em sinh đôi" — Soutetsu là nam).

## Chi tiết từng dòng sai

### §1. Đại từ Soutetsu — tự xưng "em"/"anh" sai người nghe (13)

Quy tắc đã chốt: Soutetsu tự xưng "anh" với Nagi (Nagi gọi にーさん 421×), "tôi" với Mayami (chị, gọi 双ちゃん). Các dòng dưới đều đã xác nhận người nghe từ dòng kề trong file.

### 1. Key 1601 — 双鉄 — pronoun ("em"→"anh", với Nagi)

- JP: 「いいや――っと、少しだけ待ってくれ」
- TW: 「不是……啊，稍微等我一下」
- VN cũ: 「Không——à, đợi em một chút。」
- Bản sửa: 「Không——à, đợi anh một chút。」
- Lý do: Soutetsu nói với Nagi (dòng kề 1600, 1603 đều là Nagi thử đồ); 待ってくれ = "đợi anh" — tự xưng "em" sai.

### 2. Key 1626 — 双鉄 — pronoun ("em"→"anh", với Nagi)

- JP: 「遊びを楽しむことは、自分を大事にすることだろう。\n凪とふかみとの修学旅行を、僕は、大いに楽しんでいる」
- TW: 「享受玩樂就是愛惜自己的體現吧。我現在就非常享受和凪、深美她們的修學旅行」
- VN cũ: 「Tận hưởng niềm vui khi đi chơi cũng là trân trọng bản thân mà.\nEm đang rất tận hưởng chuyến tu học cùng Nagi và Fukami đấy。」
- Bản sửa: 「Tận hưởng niềm vui khi đi chơi cũng là trân trọng bản thân mà.\nAnh đang rất tận hưởng chuyến tu học cùng Nagi và Fukami đấy。」
- Lý do: Soutetsu nói với Nagi về chuyến tu học (dòng kề 1621, 1628); 僕は楽しんでいる = "anh đang tận hưởng" — "Em" sai.

### 3. Key 1796 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「っと、いささかのんびりしすぎたな」
- TW: 「哎呀，聊得有點久了啊」
- VN cũ: 「Ái chà, có vẻ em đã hơi thong thả quá đà rồi。」
- Bản sửa: 「Ái chà, có vẻ tôi đã hơi thong thả quá đà rồi。」
- Lý do: Cảnh sáng với Mayami (1793 Soutetsu cảm ơn Mayami vì bữa ăn ngay trước đó); しすぎたな = chính Soutetsu "đã thong thả quá" — tự xưng "em" sai, với Mayami phải là "tôi".

### 4. Key 1853 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「うむ。いただきます！」
- TW: 「嗯，我開動了！」
- VN cũ: 「Ừm. Em xin phép!」
- Bản sửa: 「Ừm. Tôi xin phép!」
- Lý do: Soutetsu chuẩn bị ăn món Mayami nấu (1854 ngay sau đó nói với "chị Mayami"); いただきます là lời tự nói trước khi ăn — "Em xin phép" sai, với Mayami phải là "tôi".

### 5. Key 1859 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「うむ。修学旅行の一環でな。\n今日は、凪とふたりで遊びにいくことになっている」
- TW: 「嗯，這是修學旅行的一環。今天要和凪單獨出去玩」
- VN cũ: 「Ừm. Nằm trong khuôn khổ chuyến tu học.\nHôm nay, em và Nagi sẽ đi chơi cùng nhau。」
- Bản sửa: 「Ừm. Nằm trong khuôn khổ chuyến tu học.\nHôm nay, tôi và Nagi sẽ đi chơi cùng nhau。」
- Lý do: Soutetsu nói với Mayami về kế hoạch đi chơi với Nagi (1860 Mayami đáp "Chú ý an toàn, ca trực tốt lành" tiễn anh đi) — "em và Nagi" sai, phải là "tôi và Nagi".

### 6. Key 1897 — 双鉄 — pronoun + từ bịa thêm ("em"→"tôi"; gỡ "chị ở nhà nhé")

- JP: 「ご馳走様。おいしかったしほっとした。\nそれでは、気をつけていってくる」
- TW: 「多謝款待。茶泡飯很好吃，我也放鬆下來了。那我先走了」
- VN cũ: 「Cảm ơn chị vì bữa ăn. Rất ngon và ấm bụng.\nVậy em đi đây, chị ở nhà nhé。」
- Bản sửa: 「Cảm ơn chị vì bữa ăn. Rất ngon và ấm bụng.\nVậy tôi đi đây, tôi sẽ cẩn thận。」
- Lý do: (a) Soutetsu cảm ơn Mayami rồi ra khỏi nhà — tự xưng phải là "tôi", không phải "em". (b) "chị ở nhà nhé" không có trong JP (気をつけていってくる = "tôi đi đây, tôi sẽ cẩn thận") — bịa thêm, gỡ.

### 7. Key 1959 — 双鉄 — pronoun ("em"→"tôi" ×2, với Mayami)

- JP: 「なのだろうな。自覚は無いが。\n真闇姉の目から見て、どうかな？　僕は、変わったか？」
- TW: 「應該是吧，雖然我自己沒有意識到。真闇姐你覺得呢？　我變了嗎？」
- VN cũ: 「Chắc là vậy rồi. Dù em không tự nhận thức được.\nNhưng dưới góc nhìn của chị Mayami thì sao? Em, có thay đổi không?」
- Bản sửa: 「Chắc là vậy rồi. Dù tôi không tự nhận thức được.\nNhưng dưới góc nhìn của chị Mayami thì sao? Tôi, có thay đổi không?」
- Lý do: Câu hỏi "真闇姉の目から見て" = hỏi thẳng Mayami ("dưới góc nhìn của chị Mayami thì sao") — người nghe là Mayami, cả 2 chỗ "em" đều phải là "tôi".

### 8. Key 2018 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「確かに。[ハチロクニイマル,3]8620で始発を代走するのでもなければ、\nこの時間には起き出さんよなぁ」
- TW: 「是啊。除非是要給８６２０的首班車代班，確實不會在這個時間起床」
- VN cũ: 「Đúng vậy. Nếu không phải chạy thay chuyến tàu đầu tiên bằng 8620,\nthì em cũng chẳng dậy vào giờ này đâu。」
- Bản sửa: 「Đúng vậy. Nếu không phải chạy thay chuyến tàu đầu tiên bằng 8620,\nthì tôi cũng chẳng dậy vào giờ này đâu。」
- Lý do: Cảnh sáng với Mayami (2026 Mayami hỏi "Thật sao?"); 起き出さん = chính Soutetsu "chẳng dậy" — "em" sai, phải là "tôi".

### 9. Key 2030 — 双鉄 — pronoun ("anh"→"tôi", với Mayami)

- JP: 「真っ先に思いつくのは、喫茶店などの類だな。\nかわいい凪を眺めつつ、のんびり過ごすのは幸福そうだ」
- TW: 「最先想到的就是去咖啡店坐坐之類的吧。一邊欣賞可愛的你，一邊悠閒度日，這樣應該會很幸福」
- VN cũ: 「Điều anh nghĩ đến đầu tiên là những nơi như quán cà phê.\nVừa ngắm Nagi dễ thương, vừa thong thả tận hưởng thời gian, có vẻ sẽ hạnh phúc lắm。」
- Bản sửa: 「Điều tôi nghĩ đến đầu tiên là những nơi như quán cà phê.\nVừa ngắm Nagi dễ thương, vừa thong thả tận hưởng thời gian, có vẻ sẽ hạnh phúc lắm。」
- Lý do: Soutetsu nói về Nagi ở ngôi thứ ba ("ngắm Nagi dễ thương") nên người nghe KHÔNG phải Nagi — là Mayami (dòng kề 2026 Mayami, 2035 Mayami nấu ăn) — tự xưng phải là "tôi", không phải "anh".

### 10. Key 2074 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「今は、違うさ。\n僕は、僕を大事にしている」
- TW: 「現在不一樣了。我很愛惜自己」
- VN cũ: 「Bây giờ, khác rồi.\nEm đang rất trân trọng bản thân mình。」
- Bản sửa: 「Bây giờ, khác rồi.\nTôi đang rất trân trọng bản thân mình。」
- Lý do: Soutetsu trả lời Mayami 2066 ("Cái tính cố gắng quá sức vì người khác. Và không biết trân trọng bản thân mình ấy") — Mayami nói tiếp 2077 "Thay đổi rồi chứ" — người nghe là Mayami, "Em" sai.

### 11. Key 2076 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「門限があるからな。そう遅くはならんが――\n[にじゅういちじ,3]2100ギリギリに駆け足で送ることも少なくはない」
- TW: 「畢竟有門禁時間啊，也不能玩得太晚。不過也沒少踩著晚上九點的時限，急急忙忙送她到家」
- VN cũ: 「Có giờ giới nghiêm mà. Nên cũng không đến nỗi quá muộn——\nnhưng cũng không ít lần em phải hớt hải đưa con bé về nhà sát nút 21:00。」
- Bản sửa: 「Có giờ giới nghiêm mà. Nên cũng không đến nỗi quá muộn——\nnhưng cũng không ít lần tôi phải hớt hải đưa con bé về nhà sát nút 21:00。」
- Lý do: Soutetsu kể với Mayami về giờ giới nghiêm khi đưa Nagi ("con bé") về (dòng kề 2075, 2077 đều là Mayami) — "em" sai, phải là "tôi".

### 12. Key 2170 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「それは悪い。手をかけるなら僕が」
- TW: 「那不好，要是很費事就我來做吧」
- VN cũ: 「Vậy thì ngại quá. Nếu mất công thì để em làm cho。」
- Bản sửa: 「Vậy thì ngại quá. Nếu mất công thì để tôi làm cho。」
- Lý do: Soutetsu đề nghị phụ Mayami nấu ăn ("mất công" = công nấu nướng của chị) — người nghe là Mayami, "em" sai.

### 13. Key 2182 — 双鉄 — pronoun ("em"→"tôi", với Mayami)

- JP: 「ならば、一緒にでどうだろう。\n僕も少しは手伝えるだろうし、眠気も晴らしたい」
- TW: 「那就一起做吧。我應該能幫上點忙，順便也想讓腦子清醒一些」
- VN cũ: 「Vậy thì, chúng ta cùng làm được không.\nEm cũng có thể giúp được chút ít, sẵn tiện muốn xua đi cơn buồn ngủ nữa。」
- Bản sửa: 「Vậy thì, chúng ta cùng làm được không.\nTôi cũng có thể giúp được chút ít, sẵn tiện muốn xua đi cơn buồn ngủ nữa。」
- Lý do: Soutetsu đề nghị "cùng làm" (cùng nấu ăn) với Mayami (2178 Mayami: "trong lúc đó chị sẽ~") — "Em" sai, phải là "tôi".

### 14. Key 2131 — 凪 — pronoun (Nagi gọi Soutetsu "nó"→"anh")

- JP: 「なんてゆーたと！？」
- TW: 「說什麼咧？！」
- VN cũ: 「Nó bảo sao!?」
- Bản sửa: 「Anh bảo sao!?」
- Lý do: Nagi phản ứng lại câu "Ngốc nghếch!" của Soutetsu ngay trước đó (2130) — なんて言った = "anh vừa nói gì?" (ngôi thứ hai, nói thẳng với Soutetsu). Nagi luôn gọi Soutetsu là "anh hai", không bao giờ gọi "nó" — "Nó bảo sao" đổi ngôi thứ hai thành ngôi thứ ba, sai.

### §2. Thuật ngữ đã quyết (7)

### 15. Key 1259 — 双鉄 — terminology (整備体→"thân bảo trì")

- JP: 「……鳴らしてしまえば起き出してくる。\n整備体のセンサーでも、人間以上ではあるのだろうな」
- TW: 「……鬧鐘一響，八六肯定就會起床。哪怕是整備體的感測器，也還是比人類更加靈敏吧」
- VN cũ: 「……Nếu để chuông reo thì cô ấy sẽ thức dậy mất.\nDù là cảm biến của cơ thể bảo trì, chắc chắn vẫn nhạy bén hơn con người。」
- Bản sửa: 「……Nếu để chuông reo thì cô ấy sẽ thức dậy mất.\nDù là cảm biến của thân bảo trì, chắc chắn vẫn nhạy bén hơn con người。」
- Lý do: Thuật ngữ đã quyết: 整備体 = "thân bảo trì" (không phải "cơ thể bảo trì").

### 16–20. 御一夜→"Ohitoyo" (5 dòng) + 湯医→"Yunoi" (2 dòng, 2021 gộp cả hai)

- 1878 — 凪 — JP: 「おおお！　飛行機から御一夜の町を見下ろすとばい！？」 / TW: 「噢噢噢！　坐在飛機上俯視御一夜？！」 / Cũ: 「Oa oa oa! Ngắm nhìn thị trấn Ohimitera từ trên máy bay hả!?」 / Sửa: 「Oa oa oa! Ngắm nhìn thị trấn Ohitoyo từ trên máy bay hả!?」
- 1890 — 凪 — JP: 「キハ07ば乗って、[ゆのい,1]湯医にいくと？」 / TW: 「坐Ｋｉｈａ０７去湯醫？」 / Cũ: 「Lên KiHa 07, đi đến Yui hả anh?」 / Sửa: 「Lên KiHa 07, đi đến Yunoi hả anh?」
- 2016 — 双鉄 — JP: 「だな。この時間、\n御一夜で飲食を扱う店は、コンビニだけしか無い」 / TW: 「是啊。這個時間段能吃東西的店鋪，就只有便利商店了」 / Cũ: 「Đúng vậy. Giờ này,\nở Ohimitera chỉ có cửa hàng tiện lợi là có bán đồ ăn thức uống thôi。」 / Sửa: 「Đúng vậy. Giờ này,\nở Ohitoyo chỉ có cửa hàng tiện lợi là có bán đồ ăn thức uống thôi。」
- 2021 — 双鉄 — JP: 「だな。[ごじさんじゅうきゅうふん,3]0539発の[いちでーれっしゃ,1]1dが0622湯医着。\n折り返しの[にーでーれっしゃ,1]2dが0629発の御一夜温泉駅0716着だ」 / TW: 「是啊。０５:３９出發的１Ｄ列車０６:２２到達湯醫。返程的２Ｄ列車０６:２９出發，０７:１６到御一夜溫泉站」 / Cũ: 「Đúng vậy. Chuyến 1D khởi hành lúc 05:39 sẽ đến Yui lúc 06:22.\nChuyến khứ hồi 2D khởi hành lúc 06:29 sẽ đến ga suối nước nóng Ohimitera lúc 07:16。」 / Sửa: 「Đúng vậy. Chuyến 1D khởi hành lúc 05:39 sẽ đến Yunoi lúc 06:22.\nChuyến khứ hồi 2D khởi hành lúc 06:29 sẽ đến ga suối nước nóng Ohitoyo lúc 07:16。」
- 2598 — monologue — JP: 「みなまで聞かずとも頷いている。\nこの時間、御一夜で営業しているのはコンビニだけだ。」 / TW: 「我明白她想說什麼。這個時間段，御一夜裡只有便利商店在營業。」 / Cũ: 「Không cần nghe hết câu tôi cũng gật đầu đồng ý.\nGiờ này, ở Ohimitera chỉ có cửa hàng tiện lợi là mở cửa thôi。」 / Sửa: 「Không cần nghe hết câu tôi cũng gật đầu đồng ý.\nGiờ này, ở Ohitoyo chỉ có cửa hàng tiện lợi là mở cửa thôi。」
- 2735 — monologue — JP: 「少なくとも御一夜の観光に対する現場の見地においては、\nいまやふかみの母さえも、ふかみに届いていないだろう。」 / TW: 「至少從給御一夜觀光建言的能力來說，大概連深美的母親也比不上她。」 / Cũ: 「Ít nhất là về góc nhìn thực tế đối với du lịch Ohimitera,\nhiện tại có lẽ đến cả mẹ của Fukami cũng không thể sánh bằng con bé。」 / Sửa: 「Ít nhất là về góc nhìn thực tế đối với du lịch Ohitoyo,\nhiện tại có lẽ đến cả mẹ của Fukami cũng không thể sánh bằng con bé。」
- Lý do: Thuật ngữ đã quyết: 御一夜 = "Ohitoyo" (không bao giờ "Ohimitera"); 湯医/湯医線 = "Yunoi" (không phải "Yui"). Đã rà toàn file: chỉ còn đúng 5 chỗ "Ohimitera" và 2 chỗ "Yui" — đều đã sửa hết.

### §3. SFX / gasp っ (13 = 5 lost-gasp theo sweep + 8 đếm nguyên âm sweep bỏ sót)

### 21. Key 1231 — 双鉄 — lost-gasp (sweep)

- JP: 「――――――っっっ！！！」 / TW: 「——啊！！！」 / Cũ: 「——————!!!」 / Sửa: 「——————ƯƯƯ!!!」
- Lý do: Sweep đã kiểm chứng: JP kết thúc bằng 3 っ liên tiếp, mỗi っ → 1 Ư, giữ nguyên mọi thứ khác.

### 22. Key 1755 — 凪 — lost-gasp (sweep)

- JP: 「えええ～っ！？」 / TW: 「咦咦咦～？！」 / Cũ: 「Ê ê ê~!?」 / Sửa: 「Ê ê ê~Ư!?」
- Lý do: Sweep đã kiểm chứng: gasp っ sau dấu ~, VN giữ dấu ~ nhưng mất gasp — chèn Ư sau dấu ~.

### 23–24. Key 1820 / 1821 — lost-gasp (sweep, cả dòng là gasp)

- 1820 — 凪 — JP: 「っ！！」 / TW: 「啊！！」 / Cũ: 「!!」 / Sửa: 「Ư!!」
- 1821 — 双鉄 — JP: 「っ！！！！！」 / TW: 「啊！！！！！」 / Cũ: 「!!!!!」 / Sửa: 「Ư!!!!!」
- Lý do: Sweep đã kiểm chứng: cả dòng JP chỉ là gasp っ + dấu câu, VN chỉ còn dấu câu — chèn Ư.

### 25. Key 1988 — 双鉄 — lost-gasp (sweep ghi "needs-file-audit" — đã xử lý xong)

- JP: 「すまん、ギリギリになってしま――っ\nごほっ！　げほっ！」 / TW: 「抱歉，差點遲到了……咳咳！　咳咳！」
- VN cũ: 「Xin lỗi, anh tới sát giờ qu——\nKhụ! Khụ khụ!」
- Bản sửa: 「Xin lỗi, anh tới sát giờ qu——Ư\nKhụ! Khụ khụ!」
- Lý do: Sweep không đặt được gasp vì nghi JP/VN lệch số đoạn — kiểm tra tay: VN có đủ 2 đoạn khớp JP (đoạn 1: lời xin lỗi tới muộn, từ "qu" bị ngắt giữa chừng mirror đúng kiểu ngắt しま――っ của JP; đoạn 2: 2 tiếng ho ごほっ/げほっ → "Khụ! Khụ khụ!"). Vậy gasp っ sau dấu —— là thật, chèn Ư. Không sửa gì khác (giữ nguyên từ ngắt "qu——" theo đúng kiểu ngắt của JP, không bịa từ hoàn chỉnh).

### 26. Key 1816 — 凪 — sfx-vowel (はうっ thừa 1 nguyên âm)

- JP: 「はうっ///」 / TW: 「啊嗚……（臉紅）」 / Cũ: 「Hauu///」 / Sửa: 「Hau///」
- Lý do: Công thức độ dài nguyên âm: はうっ có 1 う → VN cần 2 nguyên âm ("Hau"); VN cũ "Hauu" có 3 nguyên âm (dài ra, ngược với っ ngắt). Tiền lệ: file 凪ふかみ05 key 2068 はうっ→"hau" (đã chốt); đối chiếu はうう (2 う) → "Hauu" mới đúng 3 nguyên âm.

### 27. Key 1817 — 凪 — sfx-vowel (はぅっ thừa 1 nguyên âm)

- JP: 「はぅっ」 / TW: 「啊嗚」 / Cũ: 「Hauu.」 / Sửa: 「Hau.」
- Lý do: Như 1816: はぅっ có 1 ぅ → VN cần 2 nguyên âm; "Hauu" thừa 1.

### 28. Key 1835 — 凪 — sfx-vowel (thiếu 3 âm E + 1 âm O)

- JP: 「チエエエエエエエエエストーーーーーーー！！」 / TW: 「喝啊啊啊啊啊啊啊！！」
- VN cũ: 「CHEEEEEESUTOOOOOOO!!!」 / Bản sửa: 「CHEEEEEEEEEESUTOOOOOOOO!!!」
- Lý do: Đếm cơ học: JP チ + 9 エ → VN cần 9 chữ E (cũ chỉ có 6); ト + 7 ー = 8 mora → VN cần 8 chữ O (cũ chỉ có 7). Đây là tiếng hét "CHEST" kéo dài — độ dài phải khớp JP (tiền lệ hibiki07 key 1785 đã đếm đủ 7 âm a).

### 29. Key 1836 — 凪 — sfx-vowel + lost-gasp (bản sao của 1835, mất っっっ)

- JP: 「チェーーーーーストーーーーっっっ！！」 / TW: 「喝啊！！！！！！」
- VN cũ: 「CHEEEEEESUTOOOOOOO!!!」 / Bản sửa: 「CHEEEEEESUTOOOOOƯƯƯ!!!」
- Lý do: VN cũ là bản sao y hệt của 1835 trong khi JP khác hẳn: チェ+5 ー = 6 âm E (cũ đúng 6, giữ nguyên); ト+4 ー = 5 mora → chỉ cần 5 chữ O (cũ có 7, thừa 2); cuối JP có っっっ → 3 Ư (tiền lệ sweep 1231: ――っっっ → ƯƯƯ).

### 30. Key 1839 — 双鉄 — sfx-vowel (うぅ thiếu 1 nguyên âm)

- JP: 「んっ……うぅ」 / TW: 「嗯……唔……」 / Cũ: 「Ưm…… ư.」 / Sửa: 「Ưm…… ưư.」
- Lý do: んっ → "Ưm" đã đủ; うぅ = う+ぅ (2 âm) → VN cần 2 nguyên âm "ưư" theo công thức (1 + số う/ぅ); cũ chỉ có 1 "ư".

### 31. Key 1757 — 凪 — sfx-vowel (ぎゅう… thiếu 1 âm u)

- JP: 「あれ？　にーさんにはあんま効かんとばい？\nぎゅうううううっ！！！」 / TW: 「咦？　對大哥哥好像沒什麼用咧？看招！！！」
- VN cũ: 「Ủa? Không có tác dụng mấy với anh hai hả?\nGyuuuuu!!!」 / Bản sửa: 「Ủa? Không có tác dụng mấy với anh hai hả?\nGyuuuuuu!!!」
- Lý do: ぎゅ + 5 う = 6 âm u → VN cần 6 chữ u ("Gyuuuuuu"); cũ chỉ có 5. っ cuối là tiếng ngắt (không thêm Ư — theo tiền lệ 凪ふかみ05: っ ngắt làm ngắn tiếng, không phải gasp sau dấu gạch).

### 32. Key 2180 — 凪 — sfx-vowel (ぎゅーーーっ thiếu 1 âm u)

- JP: 「なら押すとばい！　ぎゅーーーっ！」 / TW: 「那咱要按咧！　嘿！」
- VN cũ: 「Vậy em ấn nha! Gyuuu!」 / Bản sửa: 「Vậy em ấn nha! Gyuuuu!」
- Lý do: ぎゅ + 3 ー = 4 âm u → VN cần 4 chữ u ("Gyuuuu"); cũ chỉ có 3. っ cuối là tiếng ngắt, không thêm Ư (như 1757).

### 33. Key 2079 — 凪 — sfx-vowel (いた… thiếu 2 âm "da")

- JP: 「いたたたたたたたたっ！？」 / TW: 「痛痛痛痛痛？！」
- VN cũ: 「Ui da da da da da da!?」 / Bản sửa: 「Ui da da da da da da da da!?」
- Lý do: Đếm cơ học: JP có 8 âm た (いた + 7 た) → VN cần 8 lần "da"; cũ chỉ có 6.

### §4. Sai nghĩa / bịa thêm (2)

### 34. Key 2336 — monologue — invented-word ("Nhưng mà." bịa thêm)

- JP: 「いつの間に、修学旅行という日常が、\nすっかり僕の一部になって、失念していた。」
- TW: 「不知道從什麼時候開始，修學旅行已經完全成為了我生活的一部分，以至於忘記了當初的想法。」
- VN cũ: 「Từ lúc nào, những chuyến tu học thường nhật này,\nđã hoàn toàn trở thành một phần của tôi, khiến tôi quên béng mất. Nhưng mà.」
- Bản sửa: 「Từ lúc nào, những chuyến tu học thường nhật này,\nđã hoàn toàn trở thành một phần của tôi, khiến tôi quên béng mất.」
- Lý do: JP và TW đều không có "nhưng" (không có が cuối câu) — "Nhưng mà." là bịa thêm, lại bỏ lửng không có vế sau. Gỡ. (Đối chiếu: 2751 JP có が cuối câu thật thì VN "Nhưng." là đúng — giữ nguyên.)

### 35. Key 2649 — monologue — misread ("chị em sinh đôi" sai giới tính)

- JP: 「双子で、対等。\nだからこそ、小さな差異にもムキになった。」
- TW: 「正因為是平等的雙胞胎，所以些微的差異也會感到心有不甘。」
- VN cũ: 「Là chị em sinh đôi, ngang hàng với nhau.\nChính vì vậy, dù chỉ là một khác biệt nhỏ cũng khiến tôi phải hơn thua。」
- Bản sửa: 「Là anh em sinh đôi, ngang hàng với nhau.\nChính vì vậy, dù chỉ là một khác biệt nhỏ cũng khiến tôi phải hơn thua。」
- Lý do: 双子 = Soutetsu (nam) + Michiko (nữ) là cặp sinh đôi — "chị em sinh đôi" ám chỉ cả hai đều là nữ, sai; đúng phải là "anh em sinh đôi".

## Kiểm chứng sweep っ cho file này

- Sweep có 5 mục cho file này trong `sweep-raw-gasp-wrong.json` — đã kiểm chứng trực tiếp từng mục với JP:
  - 1231 (lost-gasp-trailing, đa-っ): đúng — đã áp nguyên.
  - 1755 (lost-gasp-trailing): đúng — đã áp nguyên.
  - 1820, 1821 (lost-gasp-whole): đúng — đã áp nguyên.
  - 1988 (needs-file-audit): sweep không dám đặt gasp — kiểm tra tay thấy 2 đoạn JP/VN khớp nhau, gasp っ sau —— là thật — đã thêm Ư (xem §3 mục 25).
- Sweep bỏ sót 8 SFX trong file này (đều là っ đứng ngay sau nguyên âm, không có dấu gạch/ngã nên mẫu của sweep không bắt được): 1757, 1816, 1817, 1835, 1836, 1839, 2079, 2180 — đã bắt hết ở §3 bằng công thức đếm nguyên âm.
- Các っ cuối từ nhấn mạnh KHÔNG phải gasp, giữ nguyên (không thêm Ư): 1741 くっ→"Hự!", 1762 えっ→"Hả!?", 1786 ひゃっ→"Hya!", 1805 うむっ→"Ưm.", 1830 あっ→"Á!?", 1911 けんっ/のにっ→"!", 1921 よしっ→"Tốt!", 1951 とっ→"hả!?", 2041 けんっ→"!!!", 2079 đã sửa số lượng (không thêm Ư), 2511 ニカっ (tường thuật), 2812 ばきっ→"Chát!", 2813 ぱっ→"Bốp!". Tiền lệ: っ cuối tuyệt đối gắn với từ là nhấn mạnh, không phải gasp.

## Các kiểm tra khác — đều sạch

- 0 lệch dòng / luân chuyển / dòng mồ côi / chưa dịch / trùng key: 445 key duy nhất, JP/TW/VN đủ cả; không có dòng VN nào không tìm được JP tương ứng, không có dòng đúng nằm sai key.
- 0 lỗi %l: file không có thẻ %l nào.
- Đại từ khác đều đúng: Soutetsu "anh" với Nagi đúng suốt (30 dòng "anh" đã rà — 1247, 1597, 1605, 1654, 1663, 1670, 1674, 1691, 1714, 1717, 1800, 1846, 1868, 1936, 1942, 1961, 1963, 1965, 1967, 1970, 1988, 1991, 2013, 2054, 2055, 2062, 2103, 2142, 2160, 2222 — riêng 2024/2169/2222 xem mục Chờ Hieu); Soutetsu gọi Mayami "chị" đúng (1665, 1686, 1787, 1793, 1854, 1897, 1959, 2195, 2208); Mayami gọi Soutetsu "em"/"Sou-chan" đúng (2118, 2172); Nagi tự xưng "em" đúng suốt, không có dòng nào Nagi tự xưng "tôi"; monologue toàn "tôi" (không có "anh" nào trong monologue); Nagi→Fukami "cậu ấy" đúng (1653 "Bằng tuổi nhau, vậy mà cậu ấy…" — cùng tuổi, không dùng "chị/em"); Fukami không có dòng thoại nào trong file này.
- Thuật ngữ khác đều đúng: エアクラ→"Aircra" (1224); 機関士→"lái tàu", 機関助士→"phụ lái tàu" nhất quán (1738, 2470, 2747); 投炭→"xúc than" (1670); 義父→"cha nuôi" hợp lệ vì TW ghi 養父 (2505 — đúng quy tắc "check TW trước khi flag 義"); Navi gọi "Cô ấy" (2223) — phù hợp vai nhũ mẫu nữ trong dự án.
- SFX giữ nguyên có lý do: あうっ→"a u" (1603, 1607 — đúng 2 nguyên âm theo công thức); はうううっ→"Hauuu." (1837 — đúng 4 nguyên âm); はあうっ→"hauu" (1759 — tổng 3 nguyên âm khớp JP a,a,u, chỉ khác phân bố — xem Chờ Hieu); cười うふふ→"Ufufu" đúng là tiếng cười, không phải tiếng rên (1743, 1744, 1747, 1749); ちぇーっ→"Xùy" (1870), にへへ→"Nihehe" (1872), ふっふーん→"Hứ hừm" (1801) — diễn xuôi theo quy tắc SFX ngẫu hứng của Hieu.
- Ruby [x,n]: 15 chỗ trong file (1691, 1890, 1940, 1978, 2018, 2021, 2062, 2505, 2785…) — VN đều bỏ ruby, thống nhất với các file trước; vấn đề ruby chưa thống nhất toàn dự án — xem Chờ Hieu.

## Chờ Hieu (không tính sai — ghi lại, không tự quyết)

- Key 2024 — "Anh cũng nghĩ thực sự là như vậy." — người nghe mơ hồ: câu này đồng tình với một câu nói trước đó, mà người nói câu đó có thể là Nagi (đang bàn giờ tàu 2021 cho chuyến đi của hai người) hoặc Mayami (cảnh sáng với Mayami, 2026 Mayami hỏi "Thật sao?"). Giữ nguyên "anh", cần Hieu chốt.
- Key 2169 — "À thì, sáng nay anh cũng ăn no rồi mà." — nhiều khả năng trả lời câu hỏi về đồ ăn của Nagi (2165 "Ăn thế thôi có đủ không?") nên "anh" đúng, nhưng cũng có thể là nói với Mayami (người nấu bữa sáng). Giữ nguyên, ghi lại để Hieu kiểm chứng.
- Key 2222 — "A... a——xin lỗi nhé. Anh vội quá. Cứu mạng rồi." — người đưa trà mơ hồ (Mayami mời trà ở 2172, Nagi đưa trà lúa mạch ở 1783); nếu là Mayami thì "anh" phải sửa thành "tôi". Giữ nguyên, cần Hieu chốt. (Cùng dòng: ぷあっ→"Phù!" — biến thể fa/fu, để unification pass theo tiền lệ lr_ふかみh2, không tính sai.)
- Key 1759 — はあうっ→"hauu" — giữ nguyên: tổng số nguyên âm khớp JP (3 = 3), chỉ khác phân bố (JP a,a,u vs VN a,u,u). Nếu Hieu muốn khớp từng âm thì sửa thành "haau".
- Key 2819 — （ぐっ）→ "(Ấn)" — VN diễn thành hành động ("ấn") thay vì tiếng ("Gừ"), mất âm nhưng giữ nghĩa. Gợi ý "(Gừ)" — để Hieu quyết.
- Ruby [x,n] 15 chỗ — VN bỏ hết ruby (nhất quán với các file trước); cách xử lý ruby chưa thống nhất toàn dự án (ghi chú ở file 仲国05) — để Hieu chốt chung, không sửa riêng file này.
- Key 1600 — "Là không lười biếng cái gì cơ?" — JP chỉ có 「なにを、ばい？」 ("cái gì?") nhưng TW ghi 放鬆 (lười biếng/chểnh mảng) và cả mạch truyện đang nói về 怠る — VN làm rõ chủ đề theo TW, giữ nguyên.
- Key 1909 — "Anh hai ăn gì thế?" — TW ghi "mua gì" (買) nhưng cảnh đang ăn uống, "ăn gì" hợp ngữ cảnh — giữ nguyên.
- Key 2812 — （ばきっ！）→"（Chát!）" — tiếng nứt/gãy, "Chát!" diễn được; giữ nguyên.

## Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 36 fix đối chiếu từng JP (+TW) lần thứ hai: **36 tổng / 36 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Kiểm tra lại đặc biệt: 13 fix đại từ đã xác nhận người nghe từ dòng kề trong file (không sửa đại từ nào khi người nghe mơ hồ — 2024, 2169, 2222 giữ nguyên, ghi ở mục Chờ Hieu); 5 fix sweep áp nguyên khớp JP từng dấu; 8 fix đếm nguyên âm đã đếm lại bằng script (1757: 6 âm u; 2180: 4 âm u; 1816/1817: 2 nguyên âm; 1835: 9 E + 8 O; 1836: 6 E + 5 O + 3 Ư; 1839: 2 âm ư; 2079: 8 lần "da"); 7 fix thuật ngữ khớp đúng thuật ngữ đã quyết; 2 fix sai nghĩa khớp JP/TW (2336 JP/TW đều không có "nhưng"; 2649 双子 là cặp nam+nữ). Kiểm tra cơ học (difflib): mọi fix chỉ khác VN cũ ở chỗ sửa có chủ đích (tỉ lệ tương đồng 0,82–0,99; 3 tỉ lệ thấp nhất là 1897, 2131, 1853 — đều là dòng ngắn đổi đại từ, đúng thiết kế). JSON 36 khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 36/36; khối TOML parse OK, 36 khóa, 0 sai lệch giá trị.

## Khối TOML (đã parse-kiểm chứng)

```toml
[script]
"1231" = "「——————ƯƯƯ!!!」"
"1259" = "「……Nếu để chuông reo thì cô ấy sẽ thức dậy mất.\\nDù là cảm biến của thân bảo trì, chắc chắn vẫn nhạy bén hơn con người.」"
"1601" = "「Không——à, đợi anh một chút.」"
"1626" = "「Tận hưởng niềm vui khi đi chơi cũng là trân trọng bản thân mà.\\nAnh đang rất tận hưởng chuyến tu học cùng Nagi và Fukami đấy.」"
"1755" = "「Ê ê ê~Ư!?」"
"1757" = "「Ủa? Không có tác dụng mấy với anh hai hả?\\nGyuuuuuu!!!」"
"1796" = "「Ái chà, có vẻ tôi đã hơi thong thả quá đà rồi.」"
"1816" = "「Hau///」"
"1817" = "「Hau.」"
"1820" = "「Ư!!」"
"1821" = "「Ư!!!!!」"
"1835" = "CHEEEEEEEEESUTOOOOOOOO!!!"
"1836" = "CHEEEEEESUTOOOOOƯƯƯ!!!"
"1839" = "「Ưm…… ưư.」"
"1853" = "「Ừm. Tôi xin phép!」"
"1859" = "「Ừm. Nằm trong khuôn khổ chuyến tu học.\\nHôm nay, tôi và Nagi sẽ đi chơi cùng nhau.」"
"1878" = "「Oa oa oa! Ngắm nhìn thị trấn Ohitoyo từ trên máy bay hả!?\\nNghe cũng vui lắm nha!!」"
"1890" = "「Lên KiHa 07, đi đến Yunoi hả anh?」"
"1897" = "「Cảm ơn chị vì bữa ăn. Rất ngon và ấm bụng.\\nVậy tôi đi đây, tôi sẽ cẩn thận.」"
"1959" = "「Chắc là vậy rồi. Dù tôi không tự nhận thức được.\\nNhưng dưới góc nhìn của chị Mayami thì sao? Tôi, có thay đổi không?」"
"1988" = "「Xin lỗi, anh tới sát giờ qu——Ư\\nKhụ! Khụ khụ!」"
"2016" = "「Đúng vậy. Giờ này,\\nở Ohitoyo chỉ có cửa hàng tiện lợi là có bán đồ ăn thức uống thôi.」"
"2018" = "「Đúng vậy. Nếu không phải chạy thay chuyến tàu đầu tiên bằng 8620,\\nthì tôi cũng chẳng dậy vào giờ này đâu.」"
"2021" = "「Đúng vậy. Chuyến 1D khởi hành lúc 05:39 sẽ đến Yunoi lúc 06:22.\\nChuyến khứ hồi 2D khởi hành lúc 06:29 sẽ đến ga suối nước nóng Ohitoyo lúc 07:16.」"
"2030" = "「Điều tôi nghĩ đến đầu tiên là những nơi như quán cà phê.\\nVừa ngắm Nagi dễ thương, vừa thong thả tận hưởng thời gian, có vẻ sẽ hạnh phúc lắm.」"
"2074" = "「Bây giờ, khác rồi.\\nTôi đang rất trân trọng bản thân mình.」"
"2076" = "「Có giờ giới nghiêm mà. Nên cũng không đến nỗi quá muộn——\\nnhưng cũng không ít lần tôi phải hớt hải đưa con bé về nhà sát nút 21:00.」"
"2079" = "「Ui da da da da da da da da!?」"
"2131" = "「Anh bảo sao!?」"
"2170" = "「Vậy thì ngại quá. Nếu mất công thì để tôi làm cho.」"
"2180" = "「Vậy em ấn nha! Gyuuuu!」"
"2182" = "「Vậy thì, chúng ta cùng làm được không.\\nTôi cũng có thể giúp được chút ít, sẵn tiện muốn xua đi cơn buồn ngủ nữa.」"
"2336" = "Từ lúc nào, những chuyến tu học thường nhật này,\\nđã hoàn toàn trở thành một phần của tôi, khiến tôi quên béng mất."
"2598" = "Không cần nghe hết câu tôi cũng gật đầu đồng ý.\\nGiờ này, ở Ohitoyo chỉ có cửa hàng tiện lợi là mở cửa thôi."
"2649" = "Là anh em sinh đôi, ngang hàng với nhau.\\nChính vì vậy, dù chỉ là một khác biệt nhỏ cũng khiến tôi phải hơn thua."
"2735" = "Ít nhất là về góc nhìn thực tế đối với du lịch Ohitoyo,\\nhiện tại có lẽ đến cả mẹ của Fukami cũng không thể sánh bằng con bé."
```

## Kết bài

File 凪ふかみ06_凪の欲しいもの (445 dòng) đã đọc hết từng dòng theo JP + TW: **36 dòng sai (8,1%)** — nặng nhất là đại từ Soutetsu tự xưng sai người nghe (14 dòng, trong đó 11 dòng với Mayami phải là "tôi" mà VN ghi "em"/"anh"), rồi SFX/gasp (13 dòng, gồm 5 theo sweep và 8 sweep bỏ sót), thuật ngữ đã quyết (7 dòng: Ohitoyo 5, Yunoi 2, thân bảo trì 1), và 2 dòng sai nghĩa/bịa thêm (2336 "Nhưng mà." bịa, 2649 "chị em sinh đôi" sai giới tính).

Điểm đáng chú ý của file này: đây là file Nagi–Mayami đan xen (cảnh sáng với Mayami nấu ăn xen với cảnh đi chơi với Nagi), nên đại từ của Soutetsu nhảy qua nhảy lại giữa "anh" (với Nagi) và "tôi" (với Mayami) — bản dịch cũ gần như mặc định dùng "em" cho mọi cảnh với Mayami, sai 11 dòng. Ngược lại, các đại từ khác trong file đều sạch: Nagi "em" đúng suốt, Mayami "chị" đúng, Nagi→Fukami "cậu ấy" đúng, monologue toàn "tôi". 3 dòng còn mơ hồ người nghe (2024, 2169, 2222) đã giữ nguyên và ghi lại chờ Hieu chốt, không đoán mò.

**Tổng cộng sau file này: 105 file / 4.912 dòng sai** (cơ sở 104 file / 4.876 dòng sai + 36 file này — cơ sở đã tự kiểm chứng với ROUTE-AUDIT.md).
