# Kiểm tra file ハチロクh1_契り — 57/353 sai (16,1%)

- File: `ハチロクh1_契り.txt.toml` — route 01_Hachiroku, 353 dòng script (monologue 175, ハチロク 107, 双鉄H 71). Nội dung: cảnh H đầu tiên của Hachiroku — phong ấn (シーリング) được giải trừ, hai người kết lời thề nguyện hai kiếp (二世の契り) và làm tình lần đầu; xen kẽ độc thoại Soutetsu giải thích về cơ thể Railord, tablet điều khiển và chức năng mới mở.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 353 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối ngoài 191 dòng chênh ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng (CSV3 là chuẩn, đã kiểm chứng cơ học: 0 lệch ngoài flatten). TOML md5 `ea6d9621d4124d9a966b6842fe53b602`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (md5 xuất hiện 1 lần trong toàn bộ toml2). Comment `# JP:` đủ. Thẻ `%l`: JP 0 dòng, VN 1 dòng (1319 — VN tự thêm thẻ, gỡ theo tiền lệ).
- Phân loại (57): romaji 19, sai âm (wrong-sound) 15, đếm nguyên âm (vowel-count) 6, gasp 6, đại từ 5, thuật ngữ 3, thẻ %l 1, nghĩa 1, lỗi gõ 1. Theo nhân vật: ハチロク 37/107 (34,6%), 双鉄H 8/71 (11,3%), monologue 12/175 (6,9%). Thoại 45/178 (25,3%), độc thoại 12/175 (6,9%). Lỗi tập trung ở tiếng rên/moans (40/57 là romaji + wrong-sound + vowel-count), đúng với bản chất file H-scene.
- Gasp sweep: 6 mục cho file này, áp nguyên 6/6 (1242, 1371, 1376, 1463, 1508, 1519). Đã quét cơ học toàn bộ dòng JP có っ: các っ còn lại đều là っ nhấn mạnh gắn từ có nội dung, っ trong thân từ, hoặc âm đã diễn (kh, ưm, phù) — 0 gasp bị sweep bỏ sót. Riêng 1293 (っ đầu dòng bị rớt) và 1271 (っ…… giữa dòng bị rớt) là 2 gasp sweep không liệt kê — đã sửa theo tiền lệ.
- Thuật ngữ trong file: chỉ có 整備体 (1853 → "thân bảo trì") và タブレット ×2 (1382, 2013 → "máy tính bảng"). Không có 御一夜 / 帝鉄 / 湯医 / まいてつ / 宮司 / 日ノ本 / 乗員 nào — không có mục mới cho đợt unification từ file này.

## Chi tiết từng dòng sai (57)

### 1214 — romaji (ハチロク)
- JP: 「やぁっ――あっ――おまんまんの――すじっ――\nこすられ、てっ――んっ――ふあっ！」
- TW: 「呀——啊——小妹妹——的縫——摩擦來摩擦去的——嗯——嗚啊！」
- VN cũ: 「Nhá——a——khe hở——của cô bé——\nđang bị cọ xát——ưm——ư a!」
- VN mới: 「Nhá——a——khe hở——của cô bé——\nđang bị cọ xát——ưm——Fua!」
- Lý do: ふあっ → "Fua" theo romaji fallback (tiền lệ h9 2037/2082). やぁっ → "Nhá" giữ nguyên theo tiền lệ moan-fix (lr-kisaki-h1 1472 giữ "Nhá"); すじ → "khe hở" đã diễn đủ.

### 1219 — romaji (ハチロク)
- JP: 「や……双鉄……様っ……んっ――\nわたくし、の――胸……など……んふっ」
- TW: 「呀……雙鐵少爺……嗯——我、的胸———有什……嗯唔」
- VN cũ: 「A……Ngài……Soutetsu……ưm――\nNgực――của em……thì có gì……ưm.」
- VN mới: 「A……Ngài……Soutetsu……ưm――\nNgực――của em……thì có gì……Ưm fu.」
- Lý do: んふっ → "Ưm fu" (tiền lệ kisaki-h3 2207: んふっ → "Ưm fu"). や → "A" giữ nguyên theo tiền lệ.

### 1222 — wrong-sound (ハチロク)
- JP: 「ひあっ、あっ――双鉄、さまっ――なにか、きます――\nなにか――やっ――これ――真っ白、にっ――んっっ！」
- TW: 「呀啊、啊——雙鐵少爺——要來了——有什麼——呀——這——腦子一片空白——嗯！」
- VN cũ: 「Kya, a——Ngài Soutetsu——có thứ gì đó, sắp đến——\nthứ gì đó——á——cái này——trắng xóa, rồi——ưm!」
- VN mới: 「Hia, a——Ngài Soutetsu——có thứ gì đó, sắp đến——\nthứ gì đó——á——cái này——trắng xóa, rồi——ưm!」
- Lý do: ひあっ = "Hia", không phải "Kya" (sai phụ âm h→k). やっ → "á" giữ nguyên theo tiền lệ moan-fix (h8 2187 giữ "Á").

### 1225 — romaji (ハチロク)
- JP: 「きゃふうっっっっ！？」
- TW: 「呀嗚——！？」
- VN cũ: 「Kya hưm!?」
- VN mới: 「Kyafuu!?」
- Lý do: きゃふう = "Kyafuu" — một âm, một cách diễn (romaji), không trộn "Kya" + "hưm" (tiền lệ h9 2178: きゅくぅぅぅぅ → "Kyukuuuuu").

### 1226 — romaji (ハチロク)
- JP: 「ひゃうんっ！！？」
- TW: 「呀嗯！！？」
- VN cũ: 「Hyaưn!!?」
- VN mới: 「Hyaun!!?」
- Lý do: ひゃうん = "Hyaun" (tiền lệ h8 2134: ひゃうんんっ → "Hyaunn").

### 1229 — romaji (ハチロク)
- JP: 「ひあっ！？　あ――双鉄様――双鉄さま、がっ――\nんっ！　わたくし、の――おまんまん――を――んふっ」
- TW: 「呀！？啊——雙鐵少爺——雙鐵少爺——嗯！舌頭——伸進——我的妹妹——嗯嗚」
- VN cũ: 「Hia!? A――Ngài Soutetsu――Ngài Soutetsu, đang――\nƯm! Bướm――của, em――ưm.」
- VN mới: 「Hia!? A――Ngài Soutetsu――Ngài Soutetsu――\nƯm! Bướm――của, em――Ưm fu.」
- Lý do: (1) "đang" là từ bịa thêm — JP chỉ có がっ cụt sau 双鉄さま, không có động từ tiếp diễn; bỏ, để dấu gạch ngang giữ sự cụt. (2) んふっ → "Ưm fu" (tiền lệ kisaki-h3 2207).

### 1238 — wrong-sound (ハチロク)
- JP: 「いっ――あっ――んくうっっっっっっっ！！！」
- TW: 「咿——啊——嗯嗚——！！！」
- VN cũ: 「Á——a——ưm kuu!!!」
- VN mới: 「I——a——Nkuu!!!」
- Lý do: いっ = "I" (nguyên âm i, không phải "Á"); んくう = "Nkuu" (tiền lệ h9 2178: âm dài đa nguyên âm → romaji). Xem mục "Cờ cho Hieu": "I" là phán đoán, có thể trả về "Á" nếu Hieu thích.

### 1241 — romaji (ハチロク)
- JP: 「くふううううんっ！」
- TW: 「唔——嗯！」
- VN cũ: 「Ư hưm!」
- VN mới: 「Kufuuuuun!」
- Lý do: くふううううん = ku + fuuuuu + n — "Ư hưm" mất hẳn phụ âm k/f; romaji dài theo công thức (tiền lệ h9 2178: きゅくぅぅぅぅ → "Kyukuuuuu").

### 1242 — gasp (双鉄H) [sweep lost-gasp-whole]
- JP: 「っ！」
- TW: 「唔！」
- VN cũ: 「!」
- VN mới: 「Ư!」
- Lý do: gasp cả dòng bị rớt — áp nguyên mục sweep.

### 1245 — vowel-count (ハチロク)
- JP: 「あひっ――やっ――あうっっ……おまん、まん――\nはっ――あっ――とけ、ちゃうっ――んうっ」
- TW: 「啊——呀——啊嗚……小妹妹——哈——啊——要融化了——嗯嗚」
- VN cũ: 「Ahi――A――Aư……Bướm, bướm――\nHa――A――Tan chảy, mất thôi――Ưm.」
- VN mới: 「Ahi――A――Aư……Bướm, bướm――\nHa――A――Tan chảy, mất thôi――Ưm ư.」
- Lý do: んうっ → "Ưm ư" (tiền lệ h9 2144: んうっ → "ưm ư"); "Ưm" một mình làm mất nguyên âm う. やっ → "A" giữ nguyên theo tiền lệ.

### 1248 — romaji (ハチロク)
- JP: 「あっ――ひっ――んううっ――双鉄、様っ――\nそれ――すごすぎ――って、んひゅっ――ひうううっ！」
- TW: 「啊——咿——嗯嗚——雙鐵少爺——太——太厲害了——嗯呀——嗚嗚嗚！」
- VN cũ: 「A――hi――ưm ư――Ngài, Soutetsu――\nCái đó――sướng quá――ưm hyu――hiưưư!」
- VN mới: 「A――hi――ưm ư――Ngài, Soutetsu――\nCái đó――sướng quá――ưm hyu――Hiuuu!」
- Lý do: ひううう = "Hiuuu" (romaji, nhất quán với "Hia"/"Hyaun" trong file); "hiưưư" là cách viết VN của cùng âm. んひゅっ → "ưm hyu" giữ nguyên (tiền lệ h8 2187).

### 1251 — romaji (ハチロク)
- JP: 「あっ――ふあっ――あっ――あひっ――」
- TW: 「啊——嗚啊——啊——啊咿——」
- VN cũ: 「A——ư a——a——a hi——」
- VN mới: 「A——Fua——a——a hi——」
- Lý do: ふあっ → "Fua" theo romaji fallback.

### 1253 — vowel-count (ハチロク)
- JP: 「あ……ひっ――んっ――あっ――あああっ」
- TW: 「啊……咿——嗯——啊——啊啊啊」
- VN cũ: 「A……Hi――Ưm――A――Aaaa.」
- VN mới: 「A……Hi――Ưm――A――Aaa.」
- Lý do: あああ = 3 nguyên âm a, VN cũ thừa 1 ("Aaaa" = 4). Tiền lệ h9 2110: はああっ → "Haaa".

### 1257 — romaji (ハチロク)
- JP: 「あ……ンッ――ふあっ――あっ――双鉄、ッ様っ――\nじらしちゃ……あっ――いや、ですっ――んっ」
- TW: 「啊……嗯——嗚啊——啊——雙鐵少爺——讓我等得好急……啊——別這樣——嗯」
- VN cũ: 「A……ưm——ư a——a——Ngài Soutetsu——\nĐừng trêu em nữa……a——không chịu, đâu——ưm」
- VN mới: 「A……ưm——Fua——a——Ngài Soutetsu——\nĐừng trêu em nữa……a——không chịu, đâu——ưm」
- Lý do: ふあっ → "Fua" theo romaji fallback.

### 1263 — vowel-count (ハチロク)
- JP: 「ああっ――」
- TW: 「啊啊——」
- VN cũ: 「A a——」
- VN mới: 「Aa——」
- Lý do: ああ = "Aa" liền nhau, không có khoảng trắng giữa hai nguyên âm.

### 1264 — vowel-count (ハチロク)
- JP: 「ああっ」
- TW: 「啊啊」
- VN cũ: 「A.」
- VN mới: 「Aa.」
- Lý do: ああっ = "Aa" — VN cũ làm mất một nguyên âm (đối chiếu 1262 あっ → "A." đúng).

### 1265 — wrong-sound (ハチロク)
- JP: 「あひゅんっ！！！」
- TW: 「啊嗯！！！」
- VN cũ: 「A hưm!!!」
- VN mới: 「Ahyun!!!」
- Lý do: あひゅん = a-hyu-n; "A hưm" mất âm lướt y và đổi n→m. Tiền lệ h8 2134: ひゃうんんっ → "Hyaunn".

### 1266 — romaji (ハチロク)
- JP: 「ふあっ……はっ――はぁっ……あひっ！？」
- TW: 「嗚啊……哈——哈……咿！？」
- VN cũ: 「Phua……ha――ha……ahi!?」
- VN mới: 「Fua……ha――haa……ahi!?」
- Lý do: ふあっ → "Fua"; はぁっ = "haa" (2 a), VN cũ "ha" thiếu 1 nguyên âm (tiền lệ h9 2054: はぁっ → "haa").

### 1267 — romaji (ハチロク)
- JP: 「ふあっ」
- TW: 「嗚啊」
- VN cũ: 「Phua.」
- VN mới: 「Fua.」
- Lý do: ふあっ → "Fua" theo romaji fallback.

### 1268 — romaji (ハチロク)
- JP: 「ふああっ――」
- TW: 「嗚啊啊——」
- VN cũ: 「Phuaa――」
- VN mới: 「Fuaa――」
- Lý do: ふああっ → "Fuaa" (2 a).

### 1269 — romaji (ハチロク)
- JP: 「ふああああああああああっ！！」
- TW: 「嗚啊啊啊啊啊啊啊！！」
- VN cũ: 「Phuaaaaaaaaaa!!」
- VN mới: 「Fuaaaaaaaaaa!!」
- Lý do: ふああああああああああっ → "Fua" + 9 a = 10 a — đã đếm cơ học: JP có 10 chữ あ, VN cũ cũng 10 chữ a, chỉ đổi Phua→Fua, giữ nguyên số lượng (tiền lệ h9 2180).

### 1270 — romaji (ハチロク)
- JP: 「ふああっ！」
- TW: 「嗚啊啊！」
- VN cũ: 「Phuaa!」
- VN mới: 「Fuaa!」
- Lý do: ふああっ → "Fuaa".

### 1271 — romaji (ハチロク)
- JP: 「ふぁっ！　っ……あっ――シーリングが開放され、て、\n使える、ように……なった、穴」
- TW: 「嗚啊！啊……這個封印解開了，可以用了的……小穴」
- VN cũ: 「Phua! ……A――Phong ấn đã được giải trừ, và,\ncái lỗ……đã có thể, sử dụng được.」
- VN mới: 「Fua! Ư……A――Phong ấn đã được giải trừ, và,\ncái lỗ……đã có thể, sử dụng được.」
- Lý do: (1) ふぁっ → "Fua". (2) っ…… giữa dòng bị rớt — gasp độc lập, thêm "Ư" theo tiền lệ sweep 1242 (「っ！」→ "Ư!"); sweep không liệt kê mục này.

### 1272 — wrong-sound (ハチロク)
- JP: 「かはっ！？」
- TW: 「嗚啊！？」
- VN cũ: 「A!?」
- VN mới: 「Kaha!?」
- Lý do: かはっ = "Kaha" — "A!?" làm mất hẳn phụ âm k/h.

### 1274 — pronoun (双鉄H)
- JP: 「ああ――僕の方も、もう限界だ」
- TW: 「嗯——我也要忍不住了」
- VN cũ: 「Ừm——Anh cũng, đến giới hạn rồi.」
- VN mới: 「Ừm——Tôi cũng, đến giới hạn rồi.」
- Lý do: Soutetsu nói với Hachiroku → tự xưng "tôi" (quy tắc đã chốt; Hachiroku gọi "ngài Soutetsu"). ああ đầu câu chỉ là tiếng đáp, không phải đại từ.

### 1278 — wrong-sound (ハチロク)
- JP: 「んっ……んちゅっ――んっ――れるっ――んっ」
- TW: 「嗯……嗯啾——嗯——噗嚕——嗯」
- VN cũ: 「Ưm……chụt――ưm――rột――ưm.」
- VN mới: 「Ưm……Ưm chụt――ưm――Reru――ưm.」
- Lý do: んちゅっ → "Ưm chụt" (tiền lệ h8 2279: んちゅ → "ưm chụt"); れるっ → "Reru" (tiền lệ h9 1358), "rột" là tiếng ực/nuốt, không phải tiếng liếm.

### 1282 — wrong-sound (ハチロク)
- JP: 「んきゅううううっ！！」
- TW: 「嗯呀——！！」
- VN cũ: 「Ưm kyaaa!!」
- VN mới: 「Ưm kyuuuuu!!」
- Lý do: んきゅうううう = "nkyuuuuu" — "kyaaa" sai nguyên âm (a thay vì u). Tiền lệ mikuro 1866: んきゅうううううううううううううっ → "Ưm kyuuuuuuuuuuuuuu".

### 1286 — romaji (ハチロク)
- JP: 「んふうっ――んっ――」
- TW: 「嗯嗚——嗯——」
- VN cũ: 「Ưm hưm——ưm——」
- VN mới: 「Ưm phuu——ưm——」
- Lý do: んふう → "Ưm phuu" (tiền lệ nagih2 2397: んふううっ → "Ưm phuuuu"; h8 2303 tương tự).

### 1287 — romaji (ハチロク)
- JP: 「んふううっっ！」
- TW: 「嗯嗚——！」
- VN cũ: 「Ưm hưm!」
- VN mới: 「Ưm phuuu!」
- Lý do: んふうう → "Ưm phuuu" (3 u, cùng tiền lệ 1286).

### 1290 — vowel-count (ハチロク)
- JP: 「んんうっっ！」
- TW: 「嗯嗯嗚！」
- VN cũ: 「Ưm ưm!」
- VN mới: 「Ưmm ư!」
- Lý do: んんう = n-n-u — "Ưm ưm" diễn う thành mũi thứ hai (thừa m, mất nguyên âm u). Tiền lệ mikuro 1604: んんっ → "ưmm".

### 1291 — vowel-count (ハチロク)
- JP: 「んんっ！」
- TW: 「嗯嗯！」
- VN cũ: 「Ưm!」
- VN mới: 「Ưmm!」
- Lý do: んん = hai nhịp mũi — "Ưm" một nhịp làm mất một nhịp (cùng tiền lệ mikuro 1604: んんっ → "ưmm").

### 1293 — gasp (双鉄H)
- JP: 「っ！？　しかし、お前、痛みが――」
- TW: 「嗯！？但你不是很痛嗎——」
- VN cũ: 「!? Nhưng mà, em, đang đau——」
- VN mới: 「Ư!? Nhưng mà, em, đang đau——」
- Lý do: gasp っ đầu dòng bị rớt — thêm "Ư" theo tiền lệ sweep 1242; sweep không liệt kê mục này.

### 1302 — romaji (ハチロク)
- JP: 「だって、だって――双鉄様の、指に――んっ――\nそのように――優しく、触れられたら――ふあっ」
- TW: 「因、因為——您的手指——嗯——摸得——那麼輕柔的話——嗚啊」
- VN cũ: 「Bởi vì, bởi vì――những ngón tay của Ngài Soutetsu――ưm――\nchạm vào em――dịu dàng đến vậy――phua.」
- VN mới: 「Bởi vì, bởi vì――những ngón tay của Ngài Soutetsu――ưm――\nchạm vào em――dịu dàng đến vậy――Fua.」
- Lý do: ふあっ cuối dòng → "Fua" theo romaji fallback.

### 1319 — tag (ハチロク)
- JP: 「レイルロオドたるこの身に来世があるかは存じませぬ。\nけれどわたくしは双鉄様と、契りを結びとうございます」
- TW: 「小女子不知道鐵路人偶是否有來生。但我也打算與雙鐵少爺，您定下婚約」
- VN cũ: 「Một \x%lレイルロオド;#00ffc040;Railord%l;#; như em không biết liệu mình có kiếp sau hay không.\nNhưng em vẫn muốn được kết lời thề nguyện cùng Ngài Soutetsu.」
- VN mới: 「Một Railord như em không biết liệu mình có kiếp sau hay không.\nNhưng em vẫn muốn được kết lời thề nguyện cùng Ngài Soutetsu.」
- Lý do: JP không có thẻ %l — VN tự thêm (toàn project có 400 dòng VN thêm thẻ kiểu này). Gỡ thẻ theo tiền lệ (file 12: gỡ 3 thẻ tự thêm; Paulette 14: gỡ thẻ gloss 杜氏 2693), thay bằng thuật ngữ đã chốt "Railord" dạng text thường.

### 1351 — typo (ハチロク)
- JP: 「双鉄様のおちんちん、まだまだ動きたいって、\nひくひくおねだり、なさってますね？」
- TW: 「您的雞雞好像還在動呢，它應該是還想要吧？」
- VN cũ: 「Cậu bé của ngài Soutetsu, dường như vẫn muốn vận động tiếp,\ndang giật giật đòi hỏi phải không ạ?」
- VN mới: 「Cậu bé của ngài Soutetsu, dường như vẫn muốn vận động tiếp,\nđang giật giật đòi hỏi phải không ạ?」
- Lý do: lỗi gõ "dang" → "đang".

### 1369 — pronoun (双鉄H)
- JP: 「少しずつ――挿れてみるぞ」
- TW: 「我會慢慢地插進去」
- VN cũ: 「Anh sẽ từ từ——tiến vào nhé」
- VN mới: 「Tôi sẽ từ từ——tiến vào nhé」
- Lý do: Soutetsu nói với Hachiroku → "tôi" (quy tắc đã chốt).

### 1371 — pronoun (双鉄H) [sweep raw-tsu]
- JP: 「多分、だが――んっ――精液……\n赤ちゃんの、種、だと――思うっ」
- TW: 「我猜——嗯——這是精液……是小寶寶的種子」
- VN cũ: 「Anh đoán là——ưm——tinh dịch……\nlà hạt giống, của em bé——anh nghĩ vậyっ」
- VN mới: 「Tôi đoán là——ưm——tinh dịch……\nlà hạt giống, của em bé——tôi nghĩ vậyƯ」
- Lý do: (1) Soutetsu → "tôi" cả hai chỗ ("Anh đoán", "anh nghĩ vậy"). (2) っ thô cuối dòng → "Ư" — áp nguyên mục sweep (tiền lệ Hachiroku 12 再開発 2103/2537).

### 1376 — gasp (ハチロク) [sweep raw-tsu]
- JP: 「ですから――どうぞっ」
- TW: 「所以——來吧」
- VN cũ: 「Vì vậy——xin ngài hãyっ」
- VN mới: 「Vì vậy——xin ngài hãyƯ」
- Lý do: っ thô cuối dòng → "Ư" — áp nguyên mục sweep.

### 1382 — terminology (双鉄H)
- JP: 「タブレット、外してしまって大丈夫なのか？」
- TW: 「操作板也可以卸下來的嗎？」
- VN cũ: 「Thẻ bảng, tháo ra như vậy có sao không?」
- VN mới: 「Máy tính bảng, tháo ra như vậy có sao không?」
- Lý do: タブレット = "máy tính bảng" theo thuật ngữ đã chốt (tiền lệ file khác: タブレット "thẻ bảng" → "máy tính bảng" 2657); "thẻ bảng" là dịch sai.

### 1429 — pronoun (双鉄H)
- JP: 「無論だ――好きにしてくれ。\n僕はすでに、全部まるごと、お前の男なのだから」
- TW: 「當然可以——隨你的便。畢竟我已經徹底屬於你一個人了」
- VN cũ: 「Đương nhiên rồi——tùy ý em đi.\nBởi vì anh, trọn vẹn cả con người này, đã là người đàn ông của em rồi」
- VN mới: 「Đương nhiên rồi——tùy ý em đi.\nBởi vì tôi, trọn vẹn cả con người này, đã là người đàn ông của em rồi」
- Lý do: Soutetsu nói với Hachiroku → "tôi" (quy tắc đã chốt).

### 1463 — gasp (ハチロク) [sweep raw-tsu]
- JP: 「満たして、ください――わたくしを、双鉄様で――\n双鉄様の、くださる――熱い、喜び、でっ」
- TW: 「請把我填滿——用您——滾燙的喜悅——」
- VN cũ: 「Xin hãy, lấp đầy em——bằng ngài Soutetsu——\nbằng niềm vui, nóng bỏng——mà ngài Soutetsu, trao cho emっ」
- VN mới: 「Xin hãy, lấp đầy em——bằng ngài Soutetsu——\nbằng niềm vui, nóng bỏng——mà ngài Soutetsu, trao cho emƯ」
- Lý do: っ thô cuối dòng → "Ư" — áp nguyên mục sweep.

### 1499 — pronoun (双鉄H)
- JP: 「ならば――いくぞっ」
- TW: 「那我要進來了——」
- VN cũ: 「Vậy thì——anh vào đây」
- VN mới: 「Vậy thì——tôi vào đây」
- Lý do: Soutetsu nói với Hachiroku → "tôi" (quy tắc đã chốt). っ nhấn mạnh trên いくぞ không cần thêm Ư (đã diễn bằng dấu câu).

### 1508 — gasp (ハチロク) [sweep raw-tsu]
- JP: 「そう……てつ、さまっ――わたくし――おまん、まん、\nもう、とけそう、で――切なく、てっ」
- TW: 「雙……鐵——我的——小妹妹已經要融化了——好難受」
- VN cũ: 「Ngài…… Soutetsu——cô bé, của em,\nsắp, tan chảy mất rồi——khó chịu, quá——っ」
- VN mới: 「Ngài…… Soutetsu——cô bé, của em,\nsắp, tan chảy mất rồi——khó chịu, quá——Ư」
- Lý do: っ thô cuối dòng → "Ư" — áp nguyên mục sweep.

### 1509 — meaning (ハチロク)
- JP: 「そう、てつ――さまっ――くちづけ、を――\nどうか、わたくしに――」
- TW: 「雙鐵少爺——求您——吻吻我、快吻吻我——」
- VN cũ: 「Ngài Soutetsu——hãy hôn, em đi——\nxin ngài, hãy hôn em——」
- VN mới: 「Ngài Soutetsu——xin ngài, hãy hôn em——」
- Lý do: JP chỉ có MỘT lời xin hôn (くちづけをどうかわたくしに = "xin hãy hôn em"); VN cũ lặp lại hai lần ("hãy hôn em đi" + "xin ngài, hãy hôn em") — Gemini đệm thêm. Gộp thành một.

### 1519 — gasp (ハチロク) [sweep lost-gasp-whole]
- JP: 「っ！！」
- TW: 「！！」
- VN cũ: 「!!」
- VN mới: 「Ư!!」
- Lý do: gasp cả dòng bị rớt — áp nguyên mục sweep.

### 1853 — terminology (monologue)
- JP: 見た目でもそうと思っていたが、整備体のハチロクは、\nこんなに間近で触れてても、人間とまるで変わらない。
- TW: 從外表就能看出，整備體的八六很像真人。但居然這樣撫摸起來都和人類別無二致。
- VN cũ: Nhìn bề ngoài thì tôi cũng đã nghĩ vậy rồi, nhưng Hachiroku trong thân chính,\ndù có chạm vào ở khoảng cách gần thế này, cũng chẳng khác gì con người.
- VN mới: Nhìn bề ngoài thì tôi cũng đã nghĩ vậy rồi, nhưng Hachiroku trong thân bảo trì,\ndù có chạm vào ở khoảng cách gần thế này, cũng chẳng khác gì con người.
- Lý do: 整備体 = "thân bảo trì" theo thuật ngữ đã chốt; "thân chính" là cách gọi khác (dành cho 運転体, đang chờ thống nhất ở đợt unification) — không dùng cho 整備体.

### 2013 — terminology (monologue)
- JP: どころか、タブレットまでを外してしまう。
- TW: 甚至操作板她要卸了下來。
- VN cũ: Thậm chí, em ấy còn tháo cả thẻ bảng ra.
- VN mới: Thậm chí, em ấy còn tháo cả máy tính bảng ra.
- Lý do: タブレット = "máy tính bảng" (như 1382).

### 2128 — wrong-sound (monologue)
- JP: （ぴゅぴゅっ！）
- TW: （咕溜咕溜！）
- VN cũ: （Tũm tũm!）
- VN mới: （Phụt phụt!）
- Lý do: ぴゅぴゅっ là tiếng phun thành tia (xuất tinh), không phải tiếng rơi tõm xuống nước ("Tũm tũm"). "Phụt phụt" là cách diễn tiếng phun trong file (2151 dùng "Phụt" cho びゅ).

### 2132 — wrong-sound (monologue)
- JP: （れるっ――れろっ――じゅちゅっ――じゅるっ）
- TW: （咻嚕——咻嚕——啾——啾嚕）
- VN cũ: （Sượt——sượt——chụt——chu mút）
- VN mới: （Sượt——sượt——Juchu——Juru）
- Lý do: じゅちゅっ = "Juchu" (không phải "chụt" — mất âm ju); じゅるっ = "Juru" (không phải "chu mút" — vừa trộn romaji + động từ VN, vừa sai hành động: じゅる là liếm trượt, không phải mút). れるっ/れろっ → "Sượt" giữ nguyên (cách diễn theo nghĩa hành động, nhất quán trong file).

### 2138 — wrong-sound (monologue)
- JP: （しにゅっ――すっ――するっ――すりゅっ）
- TW: （哧溜——噝——噝嚕——噝溜）
- VN cũ: （Phập——sượt——trượt——sột sột）
- VN mới: （Shinyu——sượt——trượt——Suryu）
- Lý do: しにゅっ = "Shinyu" (tiếng trượt ướt khi đưa vào — "Phập" là tiếng đâm/thúc, sai hành động); すりゅっ = "Suryu" (tiếng trượt — "sột sột" là tiếng sột soạt). すっ → "sượt", するっ → "trượt" giữ nguyên.

### 2139 — wrong-sound (monologue)
- JP: （くりゅっ）
- TW: （哧溜）
- VN cũ: （Chụt）
- VN mới: （Kuryu）
- Lý do: くりゅっ = "Kuryu" — "Chụt" là âm của ちゅっ/じゅっ, sai hẳn âm (đối chiếu 2147: ちゅむっ cũng bị dịch thành "Chụt" — sau khi sửa hai dòng này không còn trùng nhau nữa).

### 2144 — wrong-sound (monologue)
- JP: （ずばっ！　じゅっ！　じゅるっ！　じゅにゅっ！）
- TW: （啪！啾！啾嚕！啾嚕！）
- VN cũ: （Phập! Chụt! Chu mút! Sột sột!）
- VN mới: （Phập! Chụt! Juru! Junyu!）
- Lý do: じゅるっ = "Juru", じゅにゅっ = "Junyu" — "Chu mút" trộn romaji + động từ VN và sai hành động; "Sột sột" là tiếng sột soạt, không phải tiếng mút ướt.

### 2145 — wrong-sound (monologue)
- JP: （ばちゅっ！　じゅ！　じゅりゅ！　ブぼっ！！）
- TW: （啪！啾！啾嚕！噗！！）
- VN cũ: （Phập! Chụt! Chu mút! Bục!!）
- VN mới: （Phập! Chụt! Juryu! Bục!!）
- Lý do: じゅりゅ = "Juryu" — "Chu mút" sai như 2144. ブぼっ → "Bục" giữ nguyên (tiếng bụp VN, diễn đúng).

### 2147 — wrong-sound (monologue)
- JP: （ちゅむっ）
- TW: （啾嚕）
- VN cũ: （Chụt）
- VN mới: （Chumu）
- Lý do: ちゅむっ = "Chumu" (tiền lệ h9 1358: ちゅむ → "chumu"); "Chụt" làm mất âm mu.

### 2149 — wrong-sound (monologue)
- JP: （ツ――れるっ――れろっ――じゅっ――じゅるっ――）
- TW: （嗅——呸嚕——呸囉——啾——啾嚕——）
- VN cũ: （Liếm――liếm láp――liếm láp――chụt――chụt――）
- VN mới: （Liếm――liếm láp――liếm láp――chụt――Juru――）
- Lý do: じゅるっ cuối = "Juru" (không phải "chụt" — "chụt" đã dùng cho じゅっ ngay trước đó). ツ → "Liếm", れるっ/れろっ → "liếm láp" giữ nguyên.

### 2153 — wrong-sound (monologue)
- JP: （びゅるるるっ！　ぼびゅうっ！　びゅるっ！　びゅ！）
- TW: （噗嚕嚕！噗！噗嚕！噗！）
- VN cũ: （Phụt phụt phụt! Phụt! Phụt! Phụt!）
- VN mới: （Phụt phụt phụt! Bobyuu! Phụt! Phụt!）
- Lý do: ぼびゅうっ = "Bobyuu" — "Phụt" làm mất hẳn âm bo-byuu; ba âm びゅ còn lại giữ "Phụt" (nhất quán với 2151).

### 2179 — romaji (monologue)
- JP: （じゅるるうるるるっ）
- TW: （舔舔舔舔）
- VN cũ: （Chùn chụt chùn chụt）
- VN mới: （Jururuurururu）
- Lý do: じゅるるうるるる = ju-ru-ru-u-ru-ru-ru — âm mút dài đa nguyên âm → romaji theo công thức (tiền lệ h9 2503: ずりゅうううううううううううううううううっ → "Zu ryuuuuuuuuuuuuuuuuu").

## Giữ nguyên có lý do

- や/やぁ/やあ → "Nhá"/"A"/"á"/"Aaa" (1214, 1217, 1222, 1224, 1245): giữ theo tiền lệ moan-fix đã chốt (lr-kisaki-h1 1472 giữ "Nhá" cho やぁっ; h8 2187 giữ "Á" cho やっ; lr-kisaki-h1 1523 giữ "A" cho やっ). Không đổi sang "Ya/Yaa".
- ふっ → "phù"/"Phù" (1217, 1276): giữ theo đa số tiền lệ moan-fix (kisaki-h3 2170, nagih2 2395/2449, h8 2137/2163/2303 đều giữ "phù" cho ふっ ngắn); chỉ ふあ/ふぁ mới bắt buộc romaji.
- きゅ → "Siết (chặt)" (2125, 2129, 2170, 2176), れる/れろ → "Sượt"/"liếm (láp)" (2132, 2133, 2149), ちゅ/じゅ ngắn → "Chụt", đâm/thúc → "Phập", nuốt → "Ực", chạm → "Chạm nhẹ": hệ thống SFX trong ngoặc của file — diễn theo nghĩa hành động, nhất quán toàn file; chỉ sửa những chỗ sai hẳn âm (2132/2138/2139/2144/2145/2147/2149/2153/2179). Vòng moan-fix sẽ phán lại hệ này.
- "Kh" cho っ tắc thanh quản: giữ (1144 「いえっ」→ "kh", 1210 「せ、」→ "Ch,", 1315 「は、」→ "kh") theo quy tắc đã khóa — không đổi sang Ư.
- Soutetsu "tôi" đúng: 1298, 1343, 1364, 1393, 1399, 1401, 1490, 1495, 1497 và toàn bộ độc thoại — đã kiểm chứng cơ học: sau khi sửa, file không còn dòng Soutetsu nào tự xưng "anh" (1379 "hoa anh đào" là tên hoa, không phải đại từ).
- "Ưm" cho んっ, "A" cho あっ, "Ha" cho はっ, "Hự" cho くっ (1239), "Ư a" cho うあ (1240), "Aư" cho あう (1245), "Ưm ư" cho んうう (1248), "Ưm ưưưưưư" cho んうううううう (1288, đủ 6 ư): giữ — âm đã diễn đúng, số lượng đúng.
- おつゆ → "nước dâm" (1154, 1373, 1487, 2086) vs "dịch nhờn" (1907): giữ cả hai — "nước dâm" nhất quán trong thoại, "dịch nhờn" ở độc thoại là cách diễn trung tính, không sai nghĩa.
- おまんこ → "lồn" (1393): giữ — JP cố tình đối lập おまんまん ("bướm", từ thời thơ ấu) với おまんこ (từ bạn đại học) và プッシー ("pussy"); VN giữ đúng đối lập thanh điệu.
- 1304: JP có hai dấu 」」 đóng thừa (lỗi phía JP) — VN không lỗi, ghi nhận.
- 1275 「ああ……だな」→ "À……được thôi.": giữ — cách đáp đồng tình tự nhiên trong VN, không sai nghĩa rõ rệt.
- 1300 うむ → "Ưm?" vs 1385/1394 うむ → "Ừm": không nhất quán nhỏ trong file (chính tả "Ưm" vs "Ừm"), chỉ ghi nhận, không tính sai.
- すじっ (1214) → "khe hở của cô bé": giữ — "khe hở" đã diễn đủ "khe" của おまんまんのすじ.
- 1877 ボっ → "bỗng nóng rực lên": giữ — "bỗng" đã diễn sự đột ngột.

## Cờ cho Hieu (không tự quyết)

- 1238: いっ → "I" (thay vì "Á" cũ). Phán đoán theo quy tắc sai-âm (nguyên âm i, không phải a; tiền lệ h9 2101: くああ → "Kuaa" chứ không giữ "Aaa"). Nếu Hieu thấy "Á!" tự nhiên hơn trong tiếng Việt thì trả về "Á" — một dòng, dễ revert.
- Hệ SFX trong ngoặc (きゅ → "Siết chặt", れる/れろ → "Sượt"/"liếm láp", ずぶ/ずる → "Phập"): audit chỉ sửa chỗ sai hẳn âm; việc có nên roman hoá toàn bộ hệ này hay không để vòng moan-fix quyết (đã áp romaji cho 2139/2147/2179 và các じゅる/じゅにゅ).
- 1319: đã gỡ thẻ %l VN tự thêm, thay bằng "Railord" text thường theo tiền lệ (gỡ thẻ tự thêm). Nếu Hieu muốn giữ tooltip cho từ này thì nói lại — một dòng.
- B19 vẫn park (kiểm tra trong game ở Paulette 13 key 1596 trước đợt quét thẻ %l). Không có câu hỏi thuật ngữ mới từ file này.

## Lượt soát 2 (đọc lại toàn bộ 57 giá trị sửa đối chiếu JP)

- Tổng số: 57 / tái kiểm chứng: 57 / bỏ: 0 / sửa: 0.
- Đã kiểm chứng lại từng số lượng nguyên âm bằng đếm cơ học: 1269 (10 a), 1241 (6 u), 1282 (5 u), 1286 (2 u), 1287 (3 u), 1253 (3 a), 1266 (haa = 2 a), 2179 (13 ký tự "Jururuurururu").

## Kiểm chứng

- JSON 57 mục dạng chuẩn (list-of-dicts, khóa chuỗi, đủ jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 tuyệt đối 57/57; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (4 dòng viết lại gần như toàn bộ là tiếng rên ngắn: 1241, 2128, 2139, 2179 — đều là thay đúng âm JP).
- Khối TOML 57 khóa, parse OK (tomllib), 0 sai lệch giá trị so với JSON (so sánh chuỗi thô — lưu ý tomllib parse `\\n` thành backslash-n thật, đã so đúng).
- Sweep: 6/6 mục áp nguyên (1242, 1371, 1376, 1463, 1508, 1519); thêm 2 gasp sweep bỏ sót (1271, 1293).
- Chi tiết đầy đủ: `audit-hachirokuh1-chigiri-REVIEW.md`; danh sách sửa: `audit-hachirokuh1-chigiri-wrong.json` (57 mục).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1214 = "「Nhá——a——khe hở——của cô bé——\\nđang bị cọ xát——ưm——Fua!」"
1219 = "「A……Ngài……Soutetsu……ưm――\\nNgực――của em……thì có gì……Ưm fu.」"
1222 = "「Hia, a——Ngài Soutetsu——có thứ gì đó, sắp đến——\\nthứ gì đó——á——cái này——trắng xóa, rồi——ưm!」"
1225 = "「Kyafuu!?」"
1226 = "「Hyaun!!?」"
1229 = "「Hia!? A――Ngài Soutetsu――Ngài Soutetsu――\\nƯm! Bướm――của, em――Ưm fu.」"
1238 = "「I——a——Nkuu!!!」"
1241 = "「Kufuuuuun!」"
1242 = "「Ư!」"
1245 = "「Ahi――A――Aư……Bướm, bướm――\\nHa――A――Tan chảy, mất thôi――Ưm ư.」"
1248 = "「A――hi――ưm ư――Ngài, Soutetsu――\\nCái đó――sướng quá――ưm hyu――Hiuuu!」"
1251 = "「A——Fua——a——a hi——」"
1253 = "「A……Hi――Ưm――A――Aaa.」"
1257 = "「A……ưm——Fua——a——Ngài Soutetsu——\\nĐừng trêu em nữa……a——không chịu, đâu——ưm」"
1263 = "「Aa——」"
1264 = "「Aa.」"
1265 = "「Ahyun!!!」"
1266 = "「Fua……ha――haa……ahi!?」"
1267 = "「Fua.」"
1268 = "「Fuaa――」"
1269 = "「Fuaaaaaaaaaa!!」"
1270 = "「Fuaa!」"
1271 = "「Fua! Ư……A――Phong ấn đã được giải trừ, và,\\ncái lỗ……đã có thể, sử dụng được.」"
1272 = "「Kaha!?」"
1274 = "「Ừm——Tôi cũng, đến giới hạn rồi.」"
1278 = "「Ưm……Ưm chụt――ưm――Reru――ưm.」"
1282 = "「Ưm kyuuuuu!!」"
1286 = "「Ưm phuu——ưm——」"
1287 = "「Ưm phuuu!」"
1290 = "「Ưmm ư!」"
1291 = "「Ưmm!」"
1293 = "「Ư!? Nhưng mà, em, đang đau——」"
1302 = "「Bởi vì, bởi vì――những ngón tay của Ngài Soutetsu――ưm――\\nchạm vào em――dịu dàng đến vậy――Fua.」"
1319 = "「Một Railord như em không biết liệu mình có kiếp sau hay không.\\nNhưng em vẫn muốn được kết lời thề nguyện cùng Ngài Soutetsu.」"
1351 = "「Cậu bé của ngài Soutetsu, dường như vẫn muốn vận động tiếp,\\nđang giật giật đòi hỏi phải không ạ?」"
1369 = "「Tôi sẽ từ từ——tiến vào nhé」"
1371 = "「Tôi đoán là——ưm——tinh dịch……\\nlà hạt giống, của em bé——tôi nghĩ vậyƯ」"
1376 = "「Vì vậy——xin ngài hãyƯ」"
1382 = "「Máy tính bảng, tháo ra như vậy có sao không?」"
1429 = "「Đương nhiên rồi——tùy ý em đi.\\nBởi vì tôi, trọn vẹn cả con người này, đã là người đàn ông của em rồi」"
1463 = "「Xin hãy, lấp đầy em——bằng ngài Soutetsu——\\nbằng niềm vui, nóng bỏng——mà ngài Soutetsu, trao cho emƯ」"
1499 = "「Vậy thì——tôi vào đây」"
1508 = "「Ngài…… Soutetsu——cô bé, của em,\\nsắp, tan chảy mất rồi——khó chịu, quá——Ư」"
1509 = "「Ngài Soutetsu——xin ngài, hãy hôn em——」"
1519 = "「Ư!!」"
1853 = "Nhìn bề ngoài thì tôi cũng đã nghĩ vậy rồi, nhưng Hachiroku trong thân bảo trì,\\ndù có chạm vào ở khoảng cách gần thế này, cũng chẳng khác gì con người."
2013 = "Thậm chí, em ấy còn tháo cả máy tính bảng ra."
2128 = "（Phụt phụt!）"
2132 = "（Sượt——sượt——Juchu——Juru）"
2138 = "（Shinyu——sượt——trượt——Suryu）"
2139 = "（Kuryu）"
2144 = "（Phập! Chụt! Juru! Junyu!）"
2145 = "（Phập! Chụt! Juryu! Bục!!）"
2147 = "（Chumu）"
2149 = "（Liếm――liếm láp――liếm láp――chụt――Juru――）"
2153 = "（Phụt phụt phụt! Bobyuu! Phụt! Phụt!）"
2179 = "（Jururuurururu）"
```

## Kết bài

File ハチロクh1_契り: 353 dòng đã đọc hết, 57 dòng sai (16,1%) — lỗi tập trung ở tiếng rên (40/57) và 5 dòng đại từ Soutetsu "anh"→"tôi" với Hachiroku, 3 dòng thuật ngữ (タブレット ×2, 整備体), 1 thẻ %l VN tự thêm, 1 dòng lặp ý, 1 lỗi gõ. Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không dòng chưa dịch, không trùng khóa. Cơ sở tổng đã xác minh lại từ ROUTE-AUDIT.md: 148 file / 6.575 dòng sai.

**Tổng cộng sau file này: 149 file / 6.632 dòng sai** (cơ sở 148 file / 6.575 dòng sai + 57 file này)
