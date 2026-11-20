# Audit — れいなh1_おかあさんのレッスン.txt.toml

- File: `れいなh1_おかあさんのレッスン.txt.toml` — route 04_Reina, 402 dòng script (93 thoại Reina, 55 thoại Soutetsu, 51 thoại Paulette, 203 độc thoại).
- Nội dung: H-scene "Bài học của mẹ" — Paulette đóng vai mẹ dạy Reina làm tình với Soutetsu: Reina học oral và giao hợp lần đầu, Paulette làm mẫu rồi tự mình tham gia để đặt dấu chấm hết cho mối tình đầu không thành và trở thành mẹ của Reina cả tâm hồn lẫn thể xác; xen kẽ độc thoại Soutetsu nhận ra "tiếng nói của cơ thể" và sự bồn chồn của cả hai đến từ tâm trí và cơ thể chưa đồng nhất; kết bằng cảnh cả ba trở thành một gia đình.
- **Kết quả: 38/402 dòng sai (9,5%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (402 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 402/402 (0 lệch thực chất — 238 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. Không có thẻ `%l` nào trong JP lẫn VN — không có thẻ sai định dạng, không có thẻ VN tự thêm.
- TOML md5 `09eaed303cc160ad7b01033ad81f8c51`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Cơ sở tổng cộng đã kiểm chứng với ROUTE-AUDIT.md: **106 file / 4.936 dòng sai** (khớp với con số parent giao, không cần rebase).
- Soutetsu "anh" với Reina/Paulette: sau sửa, 0 dòng thoại "tôi" sai đối tượng còn lại (2366 là suy nghĩ trong ngoặc đơn, đúng quy tắc độc thoại; độc thoại dùng "tôi" đúng quy tắc chung). Paulette tự xưng theo người nghe: "em" với Soutetsu (1471, 1518, 1536), "chị" với Reina (1475) — 2 dòng "chị" sai đối tượng (1448, 1453) và 1 dòng "tôi" sai đối tượng (1416) đã sửa; 4 dòng "tôi" còn lại (1352, 1421, 1423, 1447) chờ Hieu vì người nghe mơ hồ — xem §6.
- Thuật ngữ: không có Ohitoyo/Teitetsu/Migita/Yunoi/KiHa/宮司 trong file nên không có gì chờ đợt thống nhất, trừ 日ノ本 "Hinomoto" (1408) đang chờ Hieu chốt "Hinomoto" vs "Hinamoto" — xem §3. Railord viết đúng "Railord" (2243). 義母 ở 2232 dịch "mẹ vợ" đúng (TW 岳母).

## §2. Danh sách sửa (38 dòng)

Phân loại: xưng hô 11 (Soutetsu "tôi"→"anh" với Reina/Paulette 7: 1210, 1248, 1390, 1405, 1451, 1455, 1481 — 1210 và 1451 kèm "cô"→"em"; Paulette "tôi"→"chị" với Reina 1: 1416, "chị"→"em" với Soutetsu 2: 1448, 1453; độc thoại Soutetsu "Chị Paulette"→"Paulette" 1: 2066), gasp 5 (1323, 1346, 1348, 1349, 1574 — cả 5 từ sweep, đã kiểm chứng), tiếng cười 2 (1401, 2134 — うふふ "Ư hự hự"→"Ufufu"), fa/fu 17 (1233, 1266, 1278, 1284, 1336, 1337, 1344, 1350, 1355, 1526, 1527, 1529, 1530, 1532, 1533, 1535, 1537 — ふぁ→"phà", ふあっ→"phù", ふあ→"phùa", ふぇ/ふえ→"phuê", ひあ→"Hya"), đếm nguyên âm 2 (1264 thừa 1 a + mất ん, 1374 thừa 2 u), sai nghĩa 1 (2065 rò chữ "備").

### 1210 — Soutetsu — xưng hô
- JP: 「いや、僕からもお願い」
- TW: 「不，我也想請你……」
- VN cũ: 「Không, chính tôi cũng muốn nhờ cô.」
- Sửa: 「Không, chính anh cũng muốn nhờ em.」
- Lý do: Soutetsu nói với Reina (cô bé vừa từ chối ở 1207, anh đang nhờ cô bé thử cách khác): tự xưng "anh", gọi "em" theo quy tắc đã chốt (Soutetsu "anh" với Reina). VN cũ "tôi"/"cô" sai quy tắc. Dù người nghe có là Paulette thì cũng "anh"/"em" — cả hai đều nhóm "anh".

### 1233 — Reina — fa/fu
- JP: 「せっくす……セックス――んっ――れいな――ちゃんと、\nそうてつ、さんと……んっ――あっ――ふあっ――あっ」
- TW: 「做愛……做愛……玲奈……和雙鐵先生……做到了……蛤啊……蛤啊……」
- VN cũ: 「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\nlàm với anh, Soutetsu……ưm——a——ha——a」
- Sửa: 「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\nlàm với anh, Soutetsu……ưm——a——phù——a」
- Lý do: JP ふあっ: ふあっ→"phù" theo quy tắc fa/fu (tiền lệ ふかみh2: ふあっ→"Phù"). VN cũ "ha" làm mất phụ âm f.

### 1248 — Soutetsu — xưng hô
- JP: 「これ、なのか？　僕が感じてるこのソワソワに、\nれいなも、取りつかれてしまっていたのか？」
- TW: 「原來是這樣嗎？玲奈跟我感受到了同樣的不安？」
- VN cũ: 「Là cái này sao? Sự bồn chồn mà tôi đang cảm thấy,\nReina cũng bị nó ám ảnh sao?」
- Sửa: 「Là cái này sao? Sự bồn chồn mà anh đang cảm thấy,\nReina cũng bị nó ám ảnh sao?」
- Lý do: Soutetsu hỏi Paulette (1244 Paulette vừa giải thích; anh đang hỏi cô ấy về sự bồn chồn của cả hai): tự xưng "anh". Dù người nghe là Reina thì cũng "anh" — cả hai đều nhóm "anh".

### 1264 — Reina — đếm nguyên âm
- JP: 「ひあっ！？　あっ――あっ――あっ――\nふあああああああああああああんっ！！！」
- TW: 「呀啊？！啊啊啊啊……啊啊啊啊啊啊啊！！！」
- VN cũ: 「Hya!? A――a――a――\nPhù aaaaaaaaaaaaaa!!!」
- Sửa: 「Hya!? A――a――a――\nPhù aaaaaaaaaaaaan!!!」
- Lý do: JP ふあああああああああああああんっ: 13 âm a (VN cũ 14 a, thừa 1) + khôi phục âm mũi ん cuối dòng (tiền lệ あんっ→"An" giữ phụ âm mũi ん; quy tắc "không để mất âm"). "Hya" cho ひあっ giữ nguyên theo tiền lệ h3 (romanisation tiếng rên nhất quán toàn dự án) — xem §6 về mâu thuẫn "Hya" vs "Hia".

### 1266 — Reina — fa/fu
- JP: 「ひゃっ！？　あっ――な、なにっ――これっ――\nふぇっ――れいな――れいな――なんだかっ――」
- TW: 「呀啊？！怎、怎麼回事……玲奈……感覺……」
- VN cũ: 「Hya!? A――c-cái gì――thế này――\nfue――Reina――Reina――sao ấy――」
- Sửa: 「Hya!? A――c-cái gì――thế này――\nphuê――Reina――Reina――sao ấy――」
- Lý do: JP ふぇっ: ふぇ→"phuê" theo quy tắc fa/fu đã chốt. VN cũ "fue" là romanisation.

### 1278 — Reina — fa/fu
- JP: 「ふぇっ！？」
- TW: 「咦？」
- VN cũ: 「Fue!?」
- Sửa: 「Phuê!?」
- Lý do: JP ふぇっ: ふぇ→"phuê" theo quy tắc fa/fu đã chốt. VN cũ "Fue" là romanisation.

### 1284 — Reina — fa/fu
- JP: 「ふぁ……あっ……すごい……すごい……ですぅ」
- TW: 「哇……好、好厲害」
- VN cũ: 「Phù……a……tuyệt quá……tuyệt quá……ạ~」
- Sửa: 「Phà……a……tuyệt quá……tuyệt quá……ạ~」
- Lý do: JP ふぁ: ふぁ→"phà" theo quy tắc fa/fu đã chốt. VN cũ "Phù" sai âm (ふぁ nhỏ → "phà", khác ふあ đầy → "phùa"/"phù").

### 1323 — Soutetsu — gasp
- JP: 「っ！！」
- TW: 「唔！！」
- VN cũ: 「!!」
- Sửa: 「Ư!!」
- Lý do: JP 「っ！！」 cả dòng là gasp, VN chỉ còn "!!": gasp bị mất. Mục sweep lost-gasp-whole, kiểm chứng đúng JP/TW, nhận nguyên giá trị sweep 「Ư!!」.

### 1336 — Reina — fa/fu
- JP: 「ふああああああっ！！？」
- TW: 「啊啊啊啊啊！！？」
- VN cũ: 「Haaaaaaaa!!?」
- Sửa: 「Phùaaaaaa!!?」
- Lý do: JP ふああああああっ (ふ + 6 あ): "Phù" + 6 a = "Phùaaaaaa". VN cũ "Haaaaaaaa" làm mất phụ âm f và thừa 2 âm a (8 a cho 6 あ).

### 1337 — Reina — fa/fu
- JP: 「ひあっ――あっ！」
- TW: 「啊啊啊啊！」
- VN cũ: 「Á——a!」
- Sửa: 「Hya——a!」
- Lý do: JP ひあっ: thống nhất trong file về "Hya" (ひゃ→"Hya" ở 1319/1320/1343/1527, ひあっ→"Hya" ở 1264; tiền lệ h3 giữ "Hya" cho ひあ). VN cũ "Á" làm mất âm h và không nhất quán trong file. Xem §6 (mâu thuẫn "Hya" vs "Hia" toàn dự án).

### 1344 — Reina — fa/fu
- JP: 「んひゅっ！　ふあぁっ――あっ――ひ、んっ――\nそこ――れいな――ふ、ぁ――ぞりって、される、とぉ」
- TW: 「啊嗯……蛤啊……啊……那裡……玲奈……蛤啊……被摩擦的話……」
- VN cũ: 「Ưm! Ha——a——hi, ưm——\nChỗ đó——Reina——ha, a——bị cọ xát, thế này——」
- Sửa: 「Ưm! Phùaa——a——hi, ưm——\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」
- Lý do: JP ふあぁっ→"Phùaa" (tiền lệ ふああっ→"Phùaa": ふ→ù, あ→a, ぁ→a, っ cuối rên bỏ theo tiền lệ); ふ、ぁ→"phù, a". VN cũ "Ha"/"ha" làm mất phụ âm f ở cả hai chỗ.

### 1346 — Soutetsu — gasp
- JP: 「っ！」
- TW: 「啊！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: JP 「っ！」 cả dòng là gasp, VN chỉ còn "!". Mục sweep lost-gasp-whole, kiểm chứng đúng, nhận nguyên 「Ư!」.

### 1348 — Soutetsu — gasp
- JP: 「っ！！？」
- TW: 「啊！！？」
- VN cũ: 「!!?」
- Sửa: 「Ư!!?」
- Lý do: JP 「っ！！？」 cả dòng là gasp, VN chỉ còn "!!?". Mục sweep lost-gasp-whole, kiểm chứng đúng, nhận nguyên 「Ư!!?」.

### 1349 — Soutetsu — gasp
- JP: 「っ！？」
- TW: 「啊！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: JP 「っ！？」 cả dòng là gasp, VN chỉ còn "!?". Mục sweep lost-gasp-whole, kiểm chứng đúng, nhận nguyên 「Ư!?」.

### 1350 — Reina — fa/fu
- JP: 「あ……ふぁ――あっ」
- TW: 「啊，哇……」
- VN cũ: 「A……phù a――a.」
- Sửa: 「A……phà――a.」
- Lý do: JP ふぁ: ふぁ→"phà" theo quy tắc fa/fu (tiền lệ h3 1101: ふぁ "Phu a"→"Phà"). Khác ふあっ→"phù a" ở 1354/1528 được giữ theo phán quyết parent ở h2 — xem §3.

### 1355 — Reina — fa/fu
- JP: 「ひゃうっ！？　ふえっ」
- TW: 「啊？！啊嗯……」
- VN cũ: 「Hyau!? Fue.」
- Sửa: 「Hyau!? Phuê.」
- Lý do: JP ふえっ: ふえ→"phuê" theo quy tắc fa/fu (tiền lệ h2 1742: ふえっ→"Phuê!?"). VN cũ "Fue" là romanisation. Đây là tiếng rên, không phải câu hỏi — khác tiền lệ h3 1133 (ふえっ？→"hả?" cho câu hỏi ngạc nhiên).

### 1374 — Reina — đếm nguyên âm
- JP: 「きゅふううううううううううううっ！！！！」
- TW: 「嗚嗚嗚嗚嗚！！！！」
- VN cũ: 「Kyuuuuuuuuuuuuuuuu!!!!」
- Sửa: 「Kyuuuuuuuuuuuuuu!!!!」
- Lý do: JP きゅふううううううううううううっ: 14 âm u (きゅ 1 + ふ 1 + う 12); VN cũ 16 u, thừa 2. Sửa theo công thức độ dài nguyên âm.

### 1390 — Soutetsu — xưng hô
- JP: 「ああ、あるな。僕の好きな言葉だ」
- TW: 「嗯，沒錯。我很喜歡這個詞」
- VN cũ: 「À, có. Một từ mà tôi rất thích.」
- Sửa: 「À, có. Một từ mà anh rất thích.」
- Lý do: Soutetsu trả lời Paulette về từ 心技体 (cô ấy hỏi ở 1408): tự xưng "anh" theo quy tắc đã chốt.

### 1401 — Paulette — tiếng cười
- JP: 「うふふ、今度は、れいなの準備を仕上げる番ね」
- TW: 「嘿嘿，這次輪到讓玲奈準備好了」
- VN cũ: 「Ư hự hự, lần này, đến lượt hoàn thành việc chuẩn bị cho Reina nhỉ.」
- Sửa: 「Ufufu, lần này, đến lượt hoàn thành việc chuẩn bị cho Reina nhỉ.」
- Lý do: JP うふふ là tiếng cười, không phải tiếng rên: diễn thành "Ufufu" theo quy tắc Hieu 19/11 (tiếng cười diễn thành tiếng cười, KHÔNG diễn thành tiếng rên "Ư hự").

### 1405 — Soutetsu — xưng hô
- JP: 「体の声を、僕はきちんと聞けてないのか」
- TW: 「因為我沒有仔細聆聽自己身體的聲音」
- VN cũ: 「Tôi đã không lắng nghe tiếng nói của cơ thể mình một cách đàng hoàng sao.」
- Sửa: 「Anh đã không lắng nghe tiếng nói của cơ thể mình một cách đàng hoàng sao.」
- Lý do: Soutetsu hỏi Paulette (cô ấy vừa cười ở 1401, anh đang tự vấn về "tiếng nói của cơ thể" với cô ấy): tự xưng "anh".

### 1416 — Paulette — xưng hô
- JP: 「わかりました。なら――\nれいな、こっちにきて？」
- TW: 「好吧。那麼……玲奈，過來一下」
- VN cũ: 「Tôi hiểu rồi. Vậy thì――\nReina, qua đây nào?」
- Sửa: 「Chị hiểu rồi. Vậy thì――\nReina, qua đây nào?」
- Lý do: Paulette nói với Reina (gọi thẳng tên trong câu: "Reina, qua đây nào?"): tự xưng "chị" theo quy tắc Paulette tự xưng theo người nghe (tiền lệ P13: "chị" với Reina).

### 1448 — Paulette — xưng hô
- JP: 「お手本。わたし、れいなに見せてあげたいんです。\nたった一度、たった一回だけの、お手本」
- TW: 「我也想給玲奈做示範。唯一一次，也是僅能做一次的示範」
- VN cũ: 「Làm mẫu. Chị, muốn cho Reina xem.\nChỉ một lần, chỉ một lần duy nhất thôi, làm mẫu cho em ấy.」
- Sửa: 「Làm mẫu. Em, muốn cho Reina xem.\nChỉ một lần, chỉ một lần duy nhất thôi, làm mẫu cho em ấy.」
- Lý do: Paulette nói với Soutetsu (Reina ở ngôi ba: "cho Reina xem… em ấy", cần anh đồng ý): tự xưng "em" theo quy tắc Paulette tự xưng theo người nghe.

### 1451 — Soutetsu — xưng hô
- JP: 「僕も同じだ。ポーレットのことは尊敬してるし、\n信頼している」
- TW: 「我也是。我很尊敬你、信賴你」
- VN cũ: 「Tôi cũng vậy. Tôi rất tôn trọng Paulette,\nvà tin tưởng cô.」
- Sửa: 「Anh cũng vậy. Anh rất tôn trọng Paulette,\nvà tin tưởng em.」
- Lý do: Soutetsu nói với Paulette (nói về cô ấy, đáp lại lời đề nghị làm mẫu): tự xưng "anh", gọi "em".

### 1453 — Paulette — xưng hô
- JP: 「わたしは……いいけど――あのっ……\n双鉄、くんが――いやじゃ、なければ」
- TW: 「我倒是……沒關係……只要雙鐵君不討厭的話」
- VN cũ: 「Chị thì…… cũng được thôi――nhưng mà……\nNếu anh Soutetsu――không thấy phiền.」
- Sửa: 「Em thì…… cũng được thôi――nhưng mà……\nNếu anh Soutetsu――không thấy phiền.」
- Lý do: Paulette đáp lại Soutetsu (1451 anh vừa nói tin tưởng cô ấy; trong câu vẫn gọi "anh Soutetsu"): tự xưng "em". Cách gọi "双鉄くん" ở đây là kiểu gọi tên ngượng ngùng khi nói với chính anh, không phải ngôi ba.

### 1455 — Soutetsu — xưng hô
- JP: 「脱いだ――が」
- TW: 「我已經脫了……」
- VN cũ: 「Tôi cởi rồi――nhưng mà.」
- Sửa: 「Anh cởi rồi――nhưng mà.」
- Lý do: Soutetsu nói với Paulette (báo lại việc đã cởi đồ theo lời cô ấy): tự xưng "anh".

### 1481 — Soutetsu — xưng hô
- JP: 「ならばポーレット。どうか僕にも教えて欲しい。\nどうすれば体の声を聞けるかを」
- TW: 「波萊特，也告訴我吧。怎麼樣才能聽見身體的聲音」
- VN cũ: 「Nếu vậy Paulette. Xin hãy chỉ cho tôi với.\nLàm thế nào để nghe được tiếng nói của cơ thể.」
- Sửa: 「Nếu vậy Paulette. Xin hãy chỉ cho anh với.\nLàm thế nào để nghe được tiếng nói của cơ thể.」
- Lý do: Soutetsu nói với Paulette (gọi tên cô ấy, nhờ cô ấy chỉ dạy): tự xưng "anh".

### 1526 — Reina — fa/fu
- JP: 「ふぇっ――らめっ――とまっ――てっ――んっ――\nれいな……おへや……よごしちゃっ――ぅっ――」
- TW: 「蛤啊……不行……快停下來……房間……要被玲奈弄髒了」
- VN cũ: 「Fue――không được――dừng――lại――ưm――\nReina……sẽ làm bẩn……căn phòng mất――ư――」
- Sửa: 「Phuê――không được――dừng――lại――ưm――\nReina……sẽ làm bẩn……căn phòng mất――ư――」
- Lý do: JP ふぇっ: ふぇ→"phuê" theo quy tắc fa/fu đã chốt. VN cũ "Fue" là romanisation.

### 1527 — Reina — fa/fu
- JP: 「ひあッ――んっ――ひゃっ――あっ――\nそうてつ――さんっ――そおてつ――さぁん」
- TW: 「蛤啊……啊……啊……雙鐵先生……雙鐵先生……」
- VN cũ: 「Á——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」
- Sửa: 「Hya——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」
- Lý do: JP ひあッ: thống nhất trong file về "Hya" (như 1337). VN cũ "Á" làm mất âm h.

### 1529 — Reina — fa/fu
- JP: 「ふぁ……あ――のんで……る……ンッ――ふっ」
- TW: 「蛤啊……啊……喝下去了……」
- VN cũ: 「Phù……a――đang……nuốt……ưm――phù.」
- Sửa: 「Phà……a――đang……nuốt……ưm――phù.」
- Lý do: JP ふぁ: ふぁ→"phà" theo quy tắc fa/fu đã chốt. VN cũ "Phù" sai âm.

### 1530 — Reina — fa/fu
- JP: 「ふあっ――あっ――あっ――あ……」
- TW: 「蛤啊……啊、啊、啊……」
- VN cũ: 「Ha——a——a——a……」
- Sửa: 「Phù——a——a——a……」
- Lý do: JP ふあっ: ふあっ→"phù" theo quy tắc fa/fu (tiền lệ ふかみh2). VN cũ "Ha" làm mất phụ âm f.

### 1532 — Reina — fa/fu
- JP: 「ふぁ……あっ――あっ！？」
- TW: 「蛤啊……啊、啊！？」
- VN cũ: 「Ha……a——a!?」
- Sửa: 「Phà……a——a!?」
- Lý do: JP ふぁ: ふぁ→"phà" theo quy tắc fa/fu đã chốt. VN cũ "Ha" làm mất phụ âm f.

### 1533 — Reina — fa/fu
- JP: 「ふあ――あっ！　あっ！　ああっ」
- TW: 「蛤啊……啊！啊！啊啊！」
- VN cũ: 「Ha——a! A! A a」
- Sửa: 「Phùa——a! A! A a」
- Lý do: JP ふあ (không っ): ふあ→"phùa" theo quy tắc fa/fu đã chốt (phán quyết parent ở h2: ふあ→"phùa" giữ nguyên). VN cũ "Ha" làm mất phụ âm f.

### 1535 — Reina — fa/fu
- JP: 「は……ぃ……っ……たっ……んくっ――ふぁっ……\nれい、な……セック、ス……そうてつ、さん――と」
- TW: 「蛤啊……好痛……啊……啊嗯……玲奈……和雙鐵先生……做愛了……」
- VN cũ: 「Ha……đau……quá……ưm——ha……\nReina……đang làm tình……với anh Soutetsu……rồi」
- Sửa: 「Ha……đau……quá……ưm——phà……\nReina……đang làm tình……với anh Soutetsu……rồi」
- Lý do: JP ふぁっ: ふぁ→"phà" theo quy tắc fa/fu (chỉ sửa chỗ thứ hai; "Ha" đầu dòng là は, giữ nguyên).

### 1537 — Reina — fa/fu
- JP: 「ぃっ――ふっ――ふあっ――ふうっ」
- TW: 「蛤啊……蛤啊……唔……」
- VN cũ: 「Ư——phù——phù——phù」
- Sửa: 「Ư——phù——phù——phùù」
- Lý do: JP ふうっ: công thức độ dài nguyên âm (1 + 1 う = 2) → "phùù". VN cũ "phù" thiếu 1 nguyên âm.

### 1574 — Soutetsu — gasp
- JP: 「～～～～っ！」
- TW: 「～～～～唔！」
- VN cũ: 「~~~~!」
- Sửa: 「~~~~Ư!」
- Lý do: JP 「～～～～っ！」: gasp cuối sau dấu ~ bị mất. Mục sweep lost-gasp-trailing, kiểm chứng đúng JP/TW, nhận nguyên giá trị sweep 「~~~~Ư!」.

### 2065 — Độc thoại — sai nghĩa
- JP: それを教えてもらうため、準備が必要とのことで。
- TW: 波萊特說在告訴我之前需要做一些準備。
- VN cũ: Để được chỉ dạy điều đó, cần phải có sự chuẩn備.
- Sửa: Để được chỉ dạy điều đó, cần phải có sự chuẩn bị.
- Lý do: Ký tự "備" (chữ Hán/Nhật) rò rỉ trong VN — lỗi foreign-text leak kiểu Gemini (tiền lệ file 12 key 3241 rò chữ Hàn). JP 準備, TW 準備 → "chuẩn bị".

### 2066 — Độc thoại — xưng hô
- JP: ポーレットはそんなことまで教えてくれているのか。
- TW: 波萊特連這個都告訴她了啊。
- VN cũ: Chị Paulette còn dạy cả những chuyện như thế này sao.
- Sửa: Paulette còn dạy cả những chuyện như thế này sao.
- Lý do: Độc thoại Soutetsu gọi Paulette là "Chị Paulette": sai ngôi — trong độc thoại Soutetsu gọi Paulette bằng tên trần hoặc "cô ấy" (vd. 1871, 1967, 2053, 2060); "chị" là cách gọi của Reina, rò sang độc thoại của Soutetsu.

### 2134 — Độc thoại — tiếng cười
- JP: それを見届け、\nれいなはうふふと幸せそうな笑みを浮かべる。
- TW: 玲奈看著這一幕，露出了幸福的微笑。
- VN cũ: Chứng kiến cảnh đó,\nReina nở một nụ cười hạnh phúc "ư hự hự".
- Sửa: Chứng kiến cảnh đó,\nReina nở một nụ cười hạnh phúc "Ufufu".
- Lý do: JP うふふ là tiếng cười của Reina (độc thoại kể lại): diễn thành "Ufufu" theo quy tắc Hieu 19/11, như 1401.

## §3. Giữ nguyên (không tính sai)

- Key 1290, 1354, 1528, 1552: ふあっ→"phù a" — giữ theo phán quyết của parent ở h2 ("phù a" đủ âm, khác cách ngắt âm tiết với "phùa" — ghi đợt thống nhất).
- Key 1282, 1341: lời nói ngọng do miệng đầy, phiên âm La-tinh cả dòng ("Hafefe? / Hanha, hoohoohihehafuhyoho?", "hoohefuhanho / hanrafa") — giữ nguyên cả dòng theo tiền lệ h3 1115; chờ Hieu (§6).
- Key 1343: んふっ→"nfu" — giữ: cụm Latin ん+phụ âm đã dùng nhất quán (tiền lệ file 07: んきゅんっ→"Ưm kyun").
- Key 1272 "Kua" vs 1322 "Hự" cho くあっ — giữ cả hai: 1272 nằm trong chuỗi rên phiên âm, 1321–1322 là tiếng gằn độc lập ("hự" cho く đơn ở 1321); tiền lệ くあ→"Ư a" ở file khác mâu thuẫn — chờ đợt thống nhất (§6).
- Key 1341: じゅるむっ→"sụt" (mất âm む) — giữ, ghi chú: âm SFX miệng trong file đã làm phẳng nhất quán thành "sụt"/"chụt" (tiền lệ h3 1090); không có quy tắc chốt cho む trong chuỗi hút — chờ Hieu nếu muốn chuẩn hoá (§6).
- Key 1345, 1565: きゅんっ→"Thắt tim"/"thắt lại" — giữ: dịch nghĩa tiếng tim thắt, nhất quán trong file.
- Key 1408: 日ノ本→"Hinomoto" — giữ: "Hinomoto" vs "Hinamoto" đang chờ Hieu chốt (đã ghi trong MEMORY).
- Key 1420: JP 「い"っ！？」 có ký tự `"` lạ — VN "Á!?" đã chuẩn hoá, đúng lệ (JP-side malformed mà VN đã chuẩn hoá thì không tính lỗi).
- Key 2232: 義母→"mẹ vợ" — giữ: TW 岳母 (mẹ vợ) xác nhận, không phải 義→"nuôi" bịa (đúng lệ file 10 key 2573: kiểm TW trước khi gắn cờ 義).
- Key 2320/2343, 2325/2355: cặp VN trùng ("(Nhóp——nhép——)", "(Phập)") cho JP khác nhau — cùng nhóm âm SFX chung (tiếng đẩy/xoáy), không phải nhiễm chéo. Key 2324 みちいいいいいいいいいいいっ→"Phập phập phập phập" — giữ: diễn nhịp tiếng đẩy; khác 2322 みちっ→"Sụt" nhưng là tiếng rên dài kéo, không có quy tắc chốt — ghi chú (§6).
- Key 1412/1469: "Vâng ạ." ×2 cho cùng JP はいですぅ — lặp hợp lệ. Key 1323/1347: "「!!」" ×2 — sau sửa 1323→"Ư!!" thì phân biệt (JP khác nhau ở っ).
- Key 1373: 9 âm ư cho JP 9 う — khớp đúng công thức độ dài. Key 2353/2354: số lượng o khớp (2353: 12 âm o; 2354: 9 âm o). Key 2346: 11 t cho 11 mora — khớp.
- Key 1377, 1338, 1364, 2328, 2329: số lượng t trong "sụt"/"phụt" kéo dài hơi lỏng (±1–2 so với số mora) nhưng không có quy tắc chốt cho phụ âm kéo dài — giữ, ghi chú (§6).
- Key 1358: ぷあっ→"pua" — giữ: tiền lệ file h1 cùng route (ぷあ/ぷぁ giữ "Pua"/"Npua").
- Key 1207, 1213, 1234, 1497, 1525/1526: lời ngọng/câu bỏ lửng giữ theo JP+TW (や→"Đừng……mà"; だか、らっ→"nên, là"; 1497 giữ dạng câu hỏi hàm ý "không thể" theo TW; ら、めぇっ→"kh-không được" diễn nghĩa だめ).
- Key 2366: Soutetsu "tôi" trong suy nghĩ ngoặc đơn — đúng quy tắc độc thoại (suy nghĩ nội tâm dùng "tôi").

## §4. Đối chiếu sweep っ-gasp

- Sweep có 7 mục cho file này: 5 mục fix (1323, 1346, 1348, 1349 lost-gasp-whole; 1574 lost-gasp-trailing) và 2 mục already-rendered (1373, 1375).
- Cả 5 fix của sweep đều CHƯA áp dụng vào VN hiện tại (VN vẫn giữ giá trị cũ sai: "!!", "!", "!!?", "!?", "~~~~!") — audit đã kiểm chứng từng giá trị với JP+TW và nhận nguyên cả 5.
- 2 mục already-rendered kiểm chứng đúng: 1373 (9 ư cho 9 う, khớp công thức) và 1375 (んむっ――ん～～～っ → "Ưm――ưm~~~").
- Quét máy toàn bộ JP của file: không có gasp っ cả dòng/cuối dòng nào khác ngoài 7 mục trên — sweep bỏ sót 0 gasp trong file này.
- Tỉ lệ diff-sanity: fix có tỉ lệ tương đồng thấp nhất là 1278 (0,67 — token SFX ngắn "Fue!?"→"Phuê!?"), 1337 (0,75) và 1336 (0,79) — cả ba đều là dòng SFX ngắn, chỉ đổi đúng phần âm đích, đã kiểm từng dòng; các fix còn lại ≥0,80.

## §5. Khối TOML (đã parse-kiểm chứng: 38 khóa, 0 sai lệch)

```toml
[script]
"1210" = "「Không, chính anh cũng muốn nhờ em.」"
"1233" = "「Làm tình……làm tình——ưm——Reina——đã đàng hoàng,\\nlàm với anh, Soutetsu……ưm——a——phù——a」"
"1248" = "「Là cái này sao? Sự bồn chồn mà anh đang cảm thấy,\\nReina cũng bị nó ám ảnh sao?」"
"1264" = "「Hya!? A――a――a――\\nPhù aaaaaaaaaaaaan!!!」"
"1266" = "「Hya!? A――c-cái gì――thế này――\\nphuê――Reina――Reina――sao ấy――」"
"1278" = "「Phuê!?」"
"1284" = "「Phà……a……tuyệt quá……tuyệt quá……ạ~」"
"1323" = "「Ư!!」"
"1336" = "「Phùaaaaaa!!?」"
"1337" = "「Hya——a!」"
"1344" = "「Ưm! Phùaa——a——hi, ưm——\\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」"
"1346" = "「Ư!」"
"1348" = "「Ư!!?」"
"1349" = "「Ư!?」"
"1350" = "「A……phà――a.」"
"1355" = "「Hyau!? Phuê.」"
"1374" = "「Kyuuuuuuuuuuuuuu!!!!」"
"1390" = "「À, có. Một từ mà anh rất thích.」"
"1401" = "「Ufufu, lần này, đến lượt hoàn thành việc chuẩn bị cho Reina nhỉ.」"
"1405" = "「Anh đã không lắng nghe tiếng nói của cơ thể mình một cách đàng hoàng sao.」"
"1416" = "「Chị hiểu rồi. Vậy thì――\\nReina, qua đây nào?」"
"1448" = "「Làm mẫu. Em, muốn cho Reina xem.\\nChỉ một lần, chỉ một lần duy nhất thôi, làm mẫu cho em ấy.」"
"1451" = "「Anh cũng vậy. Anh rất tôn trọng Paulette,\\nvà tin tưởng em.」"
"1453" = "「Em thì…… cũng được thôi――nhưng mà……\\nNếu anh Soutetsu――không thấy phiền.」"
"1455" = "「Anh cởi rồi――nhưng mà.」"
"1481" = "「Nếu vậy Paulette. Xin hãy chỉ cho anh với.\\nLàm thế nào để nghe được tiếng nói của cơ thể.」"
"1526" = "「Phuê――không được――dừng――lại――ưm――\\nReina……sẽ làm bẩn……căn phòng mất――ư――」"
"1527" = "「Hya——ưm——hya——a——\\nAnh——Soutetsu——anh——Soutetsu~」"
"1529" = "「Phà……a――đang……nuốt……ưm――phù.」"
"1530" = "「Phù——a——a——a……」"
"1532" = "「Phà……a——a!?」"
"1533" = "「Phùa——a! A! A a」"
"1535" = "「Ha……đau……quá……ưm——phà……\\nReina……đang làm tình……với anh Soutetsu……rồi」"
"1537" = "「Ư——phù——phù——phùù」"
"1574" = "「~~~~Ư!」"
"2065" = "Để được chỉ dạy điều đó, cần phải có sự chuẩn bị."
"2066" = "Paulette còn dạy cả những chuyện như thế này sao."
"2134" = "Chứng kiến cảnh đó,\\nReina nở một nụ cười hạnh phúc \"Ufufu\"."
```

## §6. Lượt soát 2 + Chờ Hieu

- Lượt soát 2: 38/38 fix đọc lại đối chiếu JP — 37 giữ nguyên, 0 bỏ, 1 sửa (1264: thêm âm mũi "n" cuối cho ん trong ふあああ…んっ, theo tiền lệ あんっ→"An" giữ phụ âm mũi ん — đã kiểm lại số lượng a: 13 a + n, tổng 17 âm a/A khớp JP).
- Chờ Hieu (không tự quyết):
  1. Key 1352, 1421, 1423, 1447 — Paulette tự xưng "tôi": người nghe mơ hồ. 1352 ("A, tôi hiểu rồi. Vậy thì――ngoạm.") — Paulette làm mẫu, có thể nói với Reina ("chị") hoặc Soutetsu ("em"); 1421/1423 ("nếu tôi được", "Tôi hiểu r(ngoạm!!)") và 1447 ("Tôi nghĩ là vậy") đều nói với cả hai người (ふたり) — "tôi" sai dưới cả hai cách đọc (không phải hội đồng), nhưng giá trị đúng ("em" hay "chị") chưa xác định được từ dòng kề. KHÔNG đưa vào khối TOML — cần Hieu kiểm tra trong game.
  2. Key 1282, 1341 — lời nói ngọng phiên âm La-tinh cả dòng: chuẩn hoá các token ふぁ/ふぇ trong đó theo quy tắc fa/fu (→"phà"/"phuê") hay giữ nguyên cả dòng phiên âm vì đây là lời nói ngọng cố ý? (Tiền lệ h3 1115 cũng đang chờ câu này.)
  3. Mâu thuẫn ひあ/ひゃ toàn dự án: file này thống nhất về "Hya" (1337, 1527 sửa "Á"→"Hya"; 1264 giữ "Hya"), theo tiền lệ h3 (giữ "Hya" cho ひあ) — nhưng có tiền lệ cũ sửa ひあ→"Hia" (file 425: 2136; file 636: 2023, tiền lệ lr_h1 1005) và tiền lệ h2 996 giữ "Á" cho ひゃ. Chưa có quy tắc chốt — cần parent/Hieu thống nhất một hướng.
  4. Key 1272 "Kua" vs 1322 "Hự" cho くあっ — thống nhất về một dạng ("Kua" giữ đủ âm, "Hự" là tiếng gằn Việt, "Ư a" theo tiền lệ cũ) hay giữ theo ngữ cảnh từng dòng?
  5. Key 1341 じゅるむっ→"sụt": có khôi phục âm む (vd. "sụtm") hay giữ cách làm phẳng SFX miệng hiện tại?
  6. Key 2324 みちいい…→"Phập phập phập phập": có chuẩn hoá về "Sụt" kéo dài theo 2322 (みちっ→"Sụt") hay giữ cách diễn nhịp tiếng đẩy?
  7. Số lượng t trong "sụt"/"phụt" kéo dài (1377, 1338, 1364, 2328, 2329 — lệch ±1–2 so với số mora): có chuẩn hoá nghiêm theo số mora như quy tắc nguyên âm hay không?
  8. Key 1408: 日ノ本 "Hinomoto" vs "Hinamoto" (đang chờ từ trước).
  9. Mâu thuẫn fa/fu toàn dự án (đã ghi trong MEMORY): ふあ→"phùa" (áp dụng ở file này) vs "phù" (lr_ふかみh2); "phù a" ở 1290/1354/1528/1552 giữ theo phán quyết parent — chờ đợt thống nhất.

## Kết bài

File れいなh1_おかあさんのレッスン đã audit xong toàn bộ 402 dòng: 38 dòng sai (9,5%) — 11 xưng hô, 5 gasp (cả 5 từ sweep), 2 tiếng cười (うふふ→"Ufufu"), 17 fa/fu, 2 đếm nguyên âm, 1 sai nghĩa (rò chữ "備"). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 38 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 38/38, 0 bỏ, 1 sửa (1264 thêm "n"). Chờ Hieu: 4 dòng Paulette "tôi" mơ hồ người nghe (1352, 1421, 1423, 1447), 2 dòng ngọng phiên âm (1282, 1341), mâu thuẫn ひあ/ひゃ ("Hya" vs "Hia" vs "Á"), "Kua" vs "Hự" (1272/1322), じゅるむっ (1341), みち dài (2324), số lượng t kéo dài, "Hinomoto" vs "Hinamoto", và mâu thuẫn fa/fu toàn dự án.