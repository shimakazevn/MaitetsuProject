# Audit — ハチロク08_台枠問題.txt.toml (route 01_Hachiroku)

- File: `ハチロク08_台枠問題.txt.toml` — route 01_Hachiroku, 408 dòng script (độc thoại 162, 双鉄 87, ハチロク 63, ポーレット 32, 凪 18, 日々姫 18, ふかみ 14, 蓑笠 5, れいな 5, 赤井宮司 2, 真闇 2). Nội dung: vấn đề 台枠 (khung gầm) của 8620 bị biến dạng — bàn phương án đổi khung gầm với 58623 (cỗ máy số 1 của Nippon Sharyo, đang được lưu tĩnh tại trụ sở chính Nagoya), giữ hai tấm biển hiệu 8620 + đoàn tàu BBQ, video quảng bá cán mốc 12 vạn lượt xem, xen cảnh ăn trưa đổi món (かえっこ: cơm cuộn trứng ↔ mì Ý) và màn mô hình khung gầm bằng điều khiển + pin của ông Minokasa; tựa đề nghĩa là “Vấn đề khung gầm”.
- Phương pháp: đọc từng dòng VN đối chiếu JP + TW từ CSV3 (Trang tính 3), kiểm tra chéo sweep, quét máy các mẫu っ / Ohito / Hinamoto / %l / đại từ / KiHa / まいてつ / 湯医線.
- Kết quả: **21/408 dòng sai (5,1%)**.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 408/408, VN rỗng 0. `[selections]` có nhưng rỗng (0 mục). Không có thẻ `%l` sai định dạng trong VN. Không có bản sao file này (md5 `7f63a5a165771defdda21cce22cbf042`, 1 copy trong `01_Hachiroku/`). 255 dòng CSV/TOML khác nhau chỉ do TOML-2 làm phẳng `\n` literal thành khoảng trắng — không phải lỗi, CSV3 là chuẩn.
- Phân loại (21): thuật ngữ 12 (御一夜→Ohitoyo 7 dòng: 1974, 2026, 2163, 2316, 2422, 3151, 3166; まいてつ→chủ tàu 2: 1988, 2055; KiHa 2: 2211, 3166; 帝鉄→Teitetsu 1: 2268; 湯医線→Yunoi 1: 3087 — 3166 mang hai thuật ngữ trong một dòng; các dạng cũ sửa trong audit theo tiền lệ 仲国02/稀咲02/仲国08 — KHÔNG thêm lại vào hàng đợi thống nhất), ý nghĩa 4 (1587, 2186, 2333, 2507), đại từ 1 (2169), rò ngoại ngữ 1 (2167 — chữ Hàn 차), gasp 2 (2501, 2502 — áp nguyên sweep), SFX 1 (2052).
- Sweep kiểm chứng: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **2 mục** (2501, 2502, lost-gasp-whole), cả hai đối chiếu JP đúng và đã áp nguyên. Quét máy bổ sung toàn bộ 150 dòng JP chứa っ: không còn gasp nào sweep bỏ sót; các dòng còn lại đều là っ trong từ, っ nhấn mạnh dính từ nội dung, hoặc âm đã được render theo quy ước toàn dự án (あっ→“A”, えっ→“Hả”, うむっ→“Ừm”, ふふっ→“Fufu”, うふふっ→“Ufufu”, ああっ→“a a” — tiền lệ hachiroku-h5/fukamih3: っ bỏ trước ！; ちょっと→“Khoan đã”). Không còn っ thô trong VN.
- Đại từ đã kiểm chứng: Soutetsu “tôi” đúng toàn file với Hachiroku (1957, 2101, 2223, 2322, 2459 và các độc thoại) và Minokasa (2402 “Ông Minokasa”); “anh” đúng với Hibiki (1928, 2043 — người nghe là Hibiki) và Paulette (2168, 2169 sau sửa). Paulette gọi “anh Soutetsu” đúng (2097, khóa B4); Nagi gọi “Anh Soutetsu” đúng (2086, にーさん). Không có dòng nào áp dụng sai quy tắc “anh chỉ với Hibiki” đã bãi bỏ.
- Thẻ `%l`: VN thêm thẻ gloss cho 静態保存 ở 10 dòng (1605, 1615, 1973, 2124, 2135, 2160, 2472, 2505, 3178, 3180) trong khi JP không có thẻ — giữ nguyên, đây là quy ước hiển thị nhất quán toàn dự án, không tính là lỗi. Không có thẻ `%l` nào sai định dạng.
- Không có thuật ngữ nào khác chờ đợt thống nhất trong file: 0 Hinamoto (“Hinomoto” đúng 3/3 dòng, 4 dòng còn lại là 日ノ本車輌製造 = “Nippon Sharyo” — tên công ty, đúng); 0 Migita System; 0 túi công tác; 0 Seki; 0 電車姫; 共感→“cộng cảm” đúng ở 3051; エアクラ→“Aircra” đúng ở 3127; 宮司→“đền chủ” đúng ở 2936, 3019, 3137; タブレット→“máy tính bảng” đúng ở 2945, 2991; 市電 không xuất hiện.
- Lượt soát 2: 21/21 đã soát lại, 0 bỏ, 0 sửa (xem “Kết bài”).

## Chi tiết từng dòng sai


### 1587 — ハチロク — ý nghĩa

- JP: 「『――[きえい,1]機影、見えざるは無し』。それこそが、\nわたくしたち姉妹の最大の誇りでございました」
- TW: 「“——便有８６２０”。這是我們姐妹最大的驕傲」
- Cũ: 「『——bóng dáng của 8620』. Đó chính là,\nniềm tự hào lớn nhất của chị em chúng em ạ.」
- Mới: 「『——đâu đâu cũng thấy bóng dáng của 8620』. Đó chính là,\nniềm tự hào lớn nhất của chị em chúng em ạ.」
- Lý do: JP là câu đầy đủ 「機影、見えざるは無し」 — “không nơi nào không thấy bóng dáng 8620”; VN cũ chỉ còn cụm danh từ “bóng dáng của 8620”, mất hẳn vị ngữ. TW 「便有８６２０」 (đâu cũng có 8620) ủng hộ. Đây là câu khẩu hiệu của dòng 8620 — 2023 trích lại nửa đầu câu này.

### 1974 — 凪 — thuật ngữ

- JP: 「なーるほど、\nわざわざ御一夜まで来てバーベキュー\x%l列車;#00ffc040;列車%l;#;ば乗って――」
- TW: 「原來如此，特地跑到御一夜來搭乘ＢＢＱ\x%l列車;#00ffc040;列車%l;#;——」
- Cũ: 「Ra là thế,\ncất công lặn lội đến tận Ohito để đi \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——」
- Mới: 「Ra là thế,\ncất công lặn lội đến tận Ohitoyo để đi \x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——」
- Lý do: 御一夜 = “Ohitoyo” (quyết định 20/11); “Ohito” là dạng cũ.

### 1988 — 双鉄 — thuật ngữ

- JP: 「そうしてもらえればありがたい。\n僕には……\x%lまいてつ;#00ffc040;まいてつ%l;#;の心の機微は恐らくわからん」
- TW: 「可以的話那當然最好了。我……或許無法把\x%lまいてつ;#00ffc040;掌車人%l;#;的心理洞察入微」
- Cũ: 「Được thế thì tốt quá.\nTôi e là…… không hiểu được những tinh tế trong tâm hồn của một \x%lまいてつ;#00ffc040;người sành toa xe%l;#; đâu.」
- Mới: 「Được thế thì tốt quá.\nTôi e là…… không hiểu được những tinh tế trong tâm hồn của một \x%lまいてつ;#00ffc040;chủ tàu%l;#; đâu.」
- Lý do: まいてつ = “chủ tàu” (quyết định); gloss cũ “người sành toa xe” sai thuật ngữ đã chốt.

### 2026 — 双鉄 — thuật ngữ

- JP: 「ううむ、ここからだと……御一夜[じょうし,1]城址の公園か？」
- TW: 「唔，從這裡過去的話……御一夜城遺址公園？」
- Cũ: 「Ưm, từ đây thì…… công viên di tích thành Ohito chăng?」
- Mới: 「Ưm, từ đây thì…… công viên di tích thành Ohitoyo chăng?」
- Lý do: 御一夜 = “Ohitoyo”; “thành Ohito” là dạng cũ.

### 2052 — ふかみ — SFX

- JP: 「う……ん。だよね。です」
- TW: 「嗯……是啊。嗯」
- Cũ: 「Ư... m. Đúng vậy nhỉ. Ạ.」
- Mới: 「Ưm... Đúng vậy nhỉ. Ạ.」
- Lý do: う……ん → “Ưm...” (tiền lệ ん……→“Ưm……”); “Ư... m” rời rạc, thừa khoảng trắng.

### 2055 — 双鉄 — thuật ngữ

- JP: 「うん。“\x%l台枠;#00ffc040;台枠%l;#;だけでももう一度走らせてやりたい”と\n――そう思ってくれる\x%lまいてつ;#00ffc040;まいてつ%l;#;さんを、見つけられれば」
- TW: 「嗯。“還想再讓列車行駛一次，哪怕只有車架也好”——只要能找到有這種想法的\x%lまいてつ;#00ffc040;掌車人%l;#;」
- Cũ: 「Ừ. "Chỉ cần \x%l台枠;#00ffc040;khung gầm%l;#; thôi cũng muốn cho nó chạy lại một lần nữa"\n——Nếu tìm được \x%lまいてつ;#00ffc040;người sành toa xe%l;#; có suy nghĩ như vậy.」
- Mới: 「Ừ. "Chỉ cần \x%l台枠;#00ffc040;khung gầm%l;#; thôi cũng muốn cho nó chạy lại một lần nữa"\n——Nếu tìm được \x%lまいてつ;#00ffc040;chủ tàu%l;#; có suy nghĩ như vậy.」
- Lý do: まいてつ = “chủ tàu”; như 1988.

### 2163 — 双鉄 — thuật ngữ

- JP: 「いかがでしょうか？　\n御一夜で[ハチロクニイマル,3]8620の修復を行える可能性は――」
- TW: 「您覺得呢？在御一夜修復８６２０的可能性——」
- Cũ: 「Ông thấy sao ạ?\nKhả năng tiến hành sửa chữa 8620 tại Ohito là——」
- Mới: 「Ông thấy sao ạ?\nKhả năng tiến hành sửa chữa 8620 tại Ohitoyo là——」
- Lý do: 御一夜 = “Ohitoyo”; “tại Ohito” là dạng cũ.

### 2167 — ポーレット — rò ngoại ngữ

- JP: 「次善っていうか――どうしてもダメなときには……\n[ハチロクニイマル,3]8620、\x%l静態保存;#00ffc040;静態保存%l;#;――するのは、どうかって、思います」
- TW: 「應該說是次善之策——到了無論如何也沒辦法的時候……將８６２０靜態保存起來——怎麼樣呢」
- Cũ: 「Nói là 차 thiện thì đúng hơn—— Khi thực sự không còn cách nào khác……\nTôi nghĩ, hay là chúng ta —— \x%l静態保存;#00ffc040;lưu tĩnh%l;#; 8620?」
- Mới: 「Nói là phương án tốt thứ hai thì đúng hơn—— Khi thực sự không còn cách nào khác……\nTôi nghĩ, hay là chúng ta —— \x%l静態保存;#00ffc040;lưu tĩnh%l;#; 8620?」
- Lý do: “차 thiện” — chữ Hàn 차 (차선 = 次善) rò vào VN; 次善 = “phương án tốt thứ hai” (TW 次善之策). Cùng mẫu rò ngoại ngữ như file 12 key 3241 (chữ Hàn 확).

### 2169 — 双鉄 — đại từ

- JP: 「それは――僕も完全に同感だ」
- TW: 「我也——完全贊同」
- Cũ: 「Điều đó—— tôi cũng hoàn toàn đồng tình.」
- Mới: 「Điều đó—— anh cũng hoàn toàn đồng tình.」
- Lý do: Soutetsu đồng tình với đề xuất 静態保存 của Paulette (2167) — người nghe là Paulette → “anh” (quy tắc đã sửa 20/11); 2168 cùng cảnh đã là “Anh”, 2169 “tôi” mâu thuẫn nội bộ.

### 2186 — 日々姫 — ý nghĩa

- JP: 「半分取って？　で、にぃにの」
- TW: 「我的一半給你。然後，阿哥你也分一半給我」
- Cũ: 「Anh lấy một nửa đi? Rồi phần của anh hai.」
- Mới: 「Em cho anh một nửa nhé? Rồi anh hai cũng cho em một nửa phần của anh.」
- Lý do: TW: 「我的一半給你。然後，阿哥你也分一半給我」 — Hibiki cho Soutetsu một nửa phần của mình, rồi xin lại một nửa phần của anh; VN cũ “Rồi phần của anh hai.” là mảnh câu, mất nghĩa trao đổi.

### 2211 — ポーレット — thuật ngữ

- JP: 「幸い、機関車変更による混乱はほとんど起きてません。\n\x%lキハ07;#00ffc040;キハ07%l;#;牽引のアンケートも、満足度凄く高かったですし」
- TW: 「所幸改變編組沒有導致混亂。關於\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;牽引的問卷調查反映出乘客滿意度也很高」
- Cũ: 「May mắn là sự xáo trộn do việc thay đổi đầu máy xe lửa hầu như không xảy ra.\nKhảo sát về việc dùng \x%lキハ07;#00ffc040;Kiha 07%l;#; kéo tàu cũng cho thấy mức độ hài lòng rất cao.」
- Mới: 「May mắn là sự xáo trộn do việc thay đổi đầu máy xe lửa hầu như không xảy ra.\nKhảo sát về việc dùng \x%lキハ07;#00ffc040;KiHa 07%l;#; kéo tàu cũng cho thấy mức độ hài lòng rất cao.」
- Lý do: KiHa — chính tả chính thức của JR (quyết định); “Kiha” sai.

### 2268 — ポーレット — thuật ngữ

- JP: 「板台枠は、当時から品質の安定が難しかったそうで……\n\x%l帝鉄;#00ffc040;帝鉄%l;#;末期には殆どが[ぼうだいわく,2]棒台枠に取って代わられてたんです」
- TW: 「板車架的質量從當時起就一直難以穩定……在\x%l帝鉄;#00ffc040;帝國鐵路%l;#;末期基本上是用框車架來代替的」
- Cũ: 「Khung gầm dạng tấm nghe nói từ thời đó đã rất khó ổn định chất lượng rồi……\nVào cuối thời kỳ \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, hầu hết đã được thay thế bằng khung gầm dạng thanh đấy.」
- Mới: 「Khung gầm dạng tấm nghe nói từ thời đó đã rất khó ổn định chất lượng rồi……\nVào cuối thời kỳ \x%l帝鉄;#00ffc040;Teitetsu%l;#;, hầu hết đã được thay thế bằng khung gầm dạng thanh đấy.」
- Lý do: 帝鉄 = “Teitetsu” (quyết định); gloss cũ “Đường sắt Hoàng gia” sai. Sửa trong audit theo tiền lệ Ohitoyo (仲国02/稀咲02/仲国08) — KHÔNG thêm lại vào hàng đợi thống nhất.

### 2316 — ハチロク — thuật ngữ

- JP: 「ポーレット様……御一夜鉄道に、\n市の補助金を申請するとおっしゃってましたが」
- TW: 「波萊特小姐說……要為御一夜鐵路申請市政府補助金」
- Cũ: 「Thị trưởng Paulette…… đã nói là sẽ xin\ntiền trợ cấp của thành phố cho Đường sắt Ohito nhưng mà.」
- Mới: 「Thị trưởng Paulette…… đã nói là sẽ xin\ntiền trợ cấp của thành phố cho Đường sắt Ohitoyo nhưng mà.」
- Lý do: 御一夜鉄道 = “Đường sắt Ohitoyo”; “Ohito” là dạng cũ.

### 2333 — れいな — ý nghĩa

- JP: 「れいなもびっくりしたですよぉ！\nちょっと前まで、物忘ればっかり」
- TW: 「玲奈也嚇了一跳！明明不久前還很健忘的」
- Cũ: 「Reina cũng bất ngờ lắm đó nha!\nMới trước đây thôi, chị ấy toàn hay quên.」
- Mới: 「Reina cũng bất ngờ lắm đó nha!\nMới trước đây thôi, em toàn hay quên.」
- Lý do: Reina nói về chính mình — JP 「れいなもびっくりした…物忘ればっかり」, TW 「玲奈…還很健忘的」; VN cũ “chị ấy toàn hay quên” chỉ sang người khác, sai chủ ngữ; “em” mới đúng.

### 2422 — ハチロク — thuật ngữ

- JP: 「辞任なさって――\n御一夜鉄道の社長に、ご専念を？」
- TW: 「辭去市長一職——專注於御一夜鐵路社長的工作上？」
- Cũ: 「Từ chức thị trưởng——\nđể tập trung vào vị trí giám đốc Đường sắt Ohito sao ạ?」
- Mới: 「Từ chức thị trưởng——\nđể tập trung vào vị trí giám đốc Đường sắt Ohitoyo sao ạ?」
- Lý do: 御一夜鉄道 = “Đường sắt Ohitoyo”; như 2316.

### 2501 — 双鉄 — gasp

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Mới: 「Ư!」
- Lý do: Sweep liệt kê (lost-gasp-whole), đối chiếu JP đúng — っ đứng một mình, VN cũ chỉ còn “!”: âm gasp mất hoàn toàn. Áp nguyên giá trị sweep (tiền lệ 共通01 1247: っ！→“Ư!”).

### 2502 — 日々姫 — gasp

- JP: 「っ！？」
- TW: 「！？」
- Cũ: 「!?」
- Mới: 「Ư!?」
- Lý do: Sweep liệt kê (lost-gasp-whole), đối chiếu JP đúng — như 2501; っ！？→“Ư!?”

### 2507 — ハチロク — ý nghĩa

- JP: 「[ハチロクニイマル,3]8620の\x%l台枠;#00ffc040;台枠%l;#;は[いただいわく,2]板台枠――25mmの[あつえんこうはん,3]圧延鋼板の縦幅――\nつまり、高さによって強度を取るという構造です」
- TW: 「８６２０的\x%l台枠;#00ffc040;車架%l;#;是板車架——其主體是２５ｍｍ的縱長軋製鋼板——也就是高度來決定強度的構造」
- Cũ: 「\x%l台枠;#00ffc040;Khung gầm%l;#; của 8620 là khung gầm dạng tấm—— với chiều dọc là thép tấm cán nóng dày 25mm——\nTức là cấu trúc lấy chiều cao để tạo độ cứng cáp ạ.」
- Mới: 「\x%l台枠;#00ffc040;Khung gầm%l;#; của 8620 là khung gầm dạng tấm—— với chiều dọc là thép tấm cán dày 25mm——\nTức là cấu trúc lấy chiều cao để tạo độ cứng cáp ạ.」
- Lý do: 圧延鋼板 = thép tấm cán (TW 軋製鋼板); VN cũ thêm “nóng” không có trong JP — từ bịa thêm.

### 3087 — monologue — thuật ngữ

- JP: 湯医線内での営業のみなら、\n\x%l8620;#00ffc040;8620%l;#;に係る負担は、最小限のもので済む。
- TW: 若只在湯醫線上行駛的話，\x%l8620;#00ffc040;８６２０%l;#;所需承受的負擔可以降至最低限度。
- Cũ: Nếu chỉ kinh doanh trong phạm vi tuyến Yui,\ngánh nặng lên \x%l8620;#00ffc040;8620%l;#; sẽ được giữ ở mức tối thiểu.
- Mới: Nếu chỉ kinh doanh trong phạm vi tuyến Yunoi,\ngánh nặng lên \x%l8620;#00ffc040;8620%l;#; sẽ được giữ ở mức tối thiểu.
- Lý do: 湯医線 = “Yunoi” (quyết định); “tuyến Yui” là dạng cũ. Sửa trong audit — KHÔNG thêm lại vào hàng đợi thống nhất.

### 3151 — monologue — thuật ngữ

- JP: それにまつわる費用のすべては、当然僕ら――\nというか、御一夜鉄道株式会社の負担となる。
- TW: 這一切的費用自然都由我們——更應該說是御一夜鐵路股份公司來承擔。
- Cũ: Toàn bộ chi phí liên quan, tất nhiên sẽ do chúng tôi——\nhay nói đúng hơn là Công ty Cổ phần Đường sắt Ohito gánh vác.
- Mới: Toàn bộ chi phí liên quan, tất nhiên sẽ do chúng tôi——\nhay nói đúng hơn là Công ty Cổ phần Đường sắt Ohitoyo gánh vác.
- Lý do: 御一夜鉄道株式会社 = “Công ty Cổ phần Đường sắt Ohitoyo”; “Ohito” là dạng cũ.

### 3166 — monologue — thuật ngữ

- JP: \x%lキハ07;#00ffc040;キハ07%l;#;も可愛らしく魅力的な車輌に間違いないのだが、\n\x%l8620;#00ffc040;8620%l;#;こそは、御一夜の観光復興の金看板だと――
- TW: 雖然\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;也是又可愛又具備魅力的車輛，但\x%l8620;#00ffc040;８６２０%l;#;才是御一夜的旅遊復興的金字招牌——
- Cũ: \x%lキハ07;#00ffc040;Kiha 07%l;#; chắc chắn cũng là một toa xe đáng yêu và đầy sức hút,\nnhưng \x%l8620;#00ffc040;8620%l;#; mới chính là bảng hiệu vàng cho sự phục hưng du lịch của Ohito——
- Mới: \x%lキハ07;#00ffc040;KiHa 07%l;#; chắc chắn cũng là một toa xe đáng yêu và đầy sức hút,\nnhưng \x%l8620;#00ffc040;8620%l;#; mới chính là bảng hiệu vàng cho sự phục hưng du lịch của Ohitoyo——
- Lý do: Hai thuật ngữ trong một dòng: キハ07 → “KiHa 07” (chính tả JR) và 御一夜 → “Ohitoyo”.


## Không chắc — giữ nguyên, chờ Hieu

- **1896** [双鉄] 「すまんが、食事は中断してくれ。すぐ、検討をしたいのだ」 → VN hiện tại “Xin lỗi, nhưng tạm dừng bữa ăn đã. Anh muốn thảo luận ngay bây giờ.” — Soutetsu nói với cả nhóm đang ăn (Hibiki, Paulette, Reina, Fukami, Nagi, Hachiroku, Minokasa lẫn lộn — có người “anh”, có người “tôi”). “Anh” hay “tôi” đều có cơ sở; giữ nguyên, không sửa.
- **2398** [双鉄] 「そう出来ればと考えている。条件の合うような機体がもしもあれば、だが」 → VN hiện tại “Anh đang nghĩ nếu làm được như vậy.” — tiếp tục cuộc thảo luận nhóm (sau 2390, 2394); người nghe không xác định rõ — cùng câu hỏi “anh” vs “tôi” như 1896. Giữ nguyên, không sửa.
- **2023** [双鉄] JP là trích dẫn bị ngắt giữa chừng: 「『日ノ本の鉄路に8620の――』」; VN hiện tại hoàn thiện câu trích: “『Trên đường sắt Hinomoto, không nơi nào là không thấy——』” — phần hoàn thiện (“không nơi nào là không thấy”) khớp đúng câu đầy đủ đã trích ở 1587 (機影、見えざるは無し), nhưng người nói trong JP cố ý bỏ lửng (――). Giữ hay cắt về đúng chỗ ngắt của JP — cần Hieu chốt. (Dòng này cũng đã nằm trong danh sách chờ đợt thống nhất của brief: “file 08 key 2023”.)
- **2944** [monologue] ハの字 → VN “hình chữ V ngược (bát - ハ)” — chú thích trong ngoặc do dịch giả thêm vào, giữ nguyên (giải thích vô hại, không tính là lỗi).

## Khối TOML (đã kiểm chứng cú pháp: 21 khóa, 0 sai lệch giá trị)

```toml
"1587" = "「『——đâu đâu cũng thấy bóng dáng của 8620』. Đó chính là,\\nniềm tự hào lớn nhất của chị em chúng em ạ.」"
"1974" = "「Ra là thế,\\ncất công lặn lội đến tận Ohitoyo để đi \\x%l列車;#00ffc040;đoàn tàu%l;#; BBQ——」"
"1988" = "「Được thế thì tốt quá.\\nTôi e là…… không hiểu được những tinh tế trong tâm hồn của một \\x%lまいてつ;#00ffc040;chủ tàu%l;#; đâu.」"
"2026" = "「Ưm, từ đây thì…… công viên di tích thành Ohitoyo chăng?」"
"2052" = "「Ưm... Đúng vậy nhỉ. Ạ.」"
"2055" = "「Ừ. \"Chỉ cần \\x%l台枠;#00ffc040;khung gầm%l;#; thôi cũng muốn cho nó chạy lại một lần nữa\"\\n——Nếu tìm được \\x%lまいてつ;#00ffc040;chủ tàu%l;#; có suy nghĩ như vậy.」"
"2163" = "「Ông thấy sao ạ?\\nKhả năng tiến hành sửa chữa 8620 tại Ohitoyo là——」"
"2167" = "「Nói là phương án tốt thứ hai thì đúng hơn—— Khi thực sự không còn cách nào khác……\\nTôi nghĩ, hay là chúng ta —— \\x%l静態保存;#00ffc040;lưu tĩnh%l;#; 8620?」"
"2169" = "「Điều đó—— anh cũng hoàn toàn đồng tình.」"
"2186" = "「Em cho anh một nửa nhé? Rồi anh hai cũng cho em một nửa phần của anh.」"
"2211" = "「May mắn là sự xáo trộn do việc thay đổi đầu máy xe lửa hầu như không xảy ra.\\nKhảo sát về việc dùng \\x%lキハ07;#00ffc040;KiHa 07%l;#; kéo tàu cũng cho thấy mức độ hài lòng rất cao.」"
"2268" = "「Khung gầm dạng tấm nghe nói từ thời đó đã rất khó ổn định chất lượng rồi……\\nVào cuối thời kỳ \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, hầu hết đã được thay thế bằng khung gầm dạng thanh đấy.」"
"2316" = "「Thị trưởng Paulette…… đã nói là sẽ xin\\ntiền trợ cấp của thành phố cho Đường sắt Ohitoyo nhưng mà.」"
"2333" = "「Reina cũng bất ngờ lắm đó nha!\\nMới trước đây thôi, em toàn hay quên.」"
"2422" = "「Từ chức thị trưởng——\\nđể tập trung vào vị trí giám đốc Đường sắt Ohitoyo sao ạ?」"
"2501" = "「Ư!」"
"2502" = "「Ư!?」"
"2507" = "「\\x%l台枠;#00ffc040;Khung gầm%l;#; của 8620 là khung gầm dạng tấm—— với chiều dọc là thép tấm cán dày 25mm——\\nTức là cấu trúc lấy chiều cao để tạo độ cứng cáp ạ.」"
"3087" = "Nếu chỉ kinh doanh trong phạm vi tuyến Yunoi,\\ngánh nặng lên \\x%l8620;#00ffc040;8620%l;#; sẽ được giữ ở mức tối thiểu."
"3151" = "Toàn bộ chi phí liên quan, tất nhiên sẽ do chúng tôi——\\nhay nói đúng hơn là Công ty Cổ phần Đường sắt Ohitoyo gánh vác."
"3166" = "\\x%lキハ07;#00ffc040;KiHa 07%l;#; chắc chắn cũng là một toa xe đáng yêu và đầy sức hút,\\nnhưng \\x%l8620;#00ffc040;8620%l;#; mới chính là bảng hiệu vàng cho sự phục hưng du lịch của Ohitoyo——"
```

## Kết bài

- Đã đọc 408/408 dòng, đối chiếu từng dòng với JP + TW; kiểm tra chéo sweep (2 mục, áp nguyên cả hai) và quét máy toàn bộ 150 dòng JP chứa っ.
- Kết quả: **21 dòng sai (5,1%)** — thuật ngữ 12, ý nghĩa 4, đại từ 1, rò ngoại ngữ 1, gasp 2, SFX 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa.
- Lượt soát 2: **21/21 đã soát lại, 0 bỏ, 0 sửa.** JSON 21 mục, khối TOML 21 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 21/21; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm tra bằng diff máy).
- Cơ sở tổng: 128 file / 5.944 dòng sai (đã tự kiểm chứng với ROUTE-AUDIT.md — khớp với cơ sở được giao). File này +21 → **129 file / 5.965 dòng sai**.
- Chờ Hieu: 1896 + 2398 (đại từ Soutetsu khi nói với nhóm hỗn hợp — “anh” vs “tôi”); 2023 (trích dẫn ngắt giữa chừng — giữ phần hoàn thiện hay cắt về đúng chỗ ngắt).

Kết bài
