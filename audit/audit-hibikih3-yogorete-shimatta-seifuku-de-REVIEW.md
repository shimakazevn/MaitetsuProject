# Audit — 日々姫h3_汚れてしまった制服で.txt.toml (route 02_Hibiki)

- File: `日々姫h3_汚れてしまった制服で.txt.toml` — route 02_Hibiki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh3_#U6c5a#U308c#U3066#U3057#U307e#U3063#U305f#U5236#U670d#U3067.txt.toml`
- Số dòng script: **322** (monologue 165, 日々姫 90, 双鉄H 67). Đọc toàn bộ 322/322 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: Hibiki đi học về, gọi Soutetsu vào phòng để đoán xem em đã thay món đồ nào — hóa ra là chiếc váy đồng phục bị dính màu sơn dầu Terre Verte; em giữ lại chiếc váy này làm 'váy chỉ cho anh hai xem'. Sau đó là H-scene dài: Soutetsu ngửi/liếm qua quần lót, Hibiki tè dầm, liếm hậu môn, quan hệ qua đường hậu môn rồi âm đạo, xuất tinh trong, kết thúc bằng việc cả hai muốn tiếp tục.
- **Kết quả: 36/322 dòng sai (11,2%)** — lỗi tập trung gần như toàn bộ ở các dòng rên trong H-scene (romaji họ ひゃ/や, fa/fu, đếm nguyên âm). Không có lỗi thuật ngữ, không có lỗi đại từ, không có lỗi sai nghĩa nội dung.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống. TOML khớp CSV3 tuyệt đối về khóa (322/322); 147 giá trị VN khác nhau TOML vs CSV3 đều chỉ là hiện tượng đã biết: TOML-2 flatten `\n` literal thành khoảng trắng; CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `fd705de9bad2a12e224c2264772c06d6`. Không có bản sao của file này trong 11 nhóm trùng. File có BOM + CRLF.
- `[selections]` rỗng. `[characters]`: 1372 'Soutetsu H', 1518 'Hibiki'. `[character_subs]`: 1557 'Hibiki', 1712 'Soutetsu' — cả hai đều trỏ tới key KHÔNG có trong `[script]` (script chỉ có key 37–1873, thiếu 1557/1712); dư thừa vô hại, không tính lỗi (cùng mẫu như Kisaki 1961 — xem cờ).
- Thẻ %l: 0 trong file (cả JP lẫn VN). Không có tag lệch.

## Phân loại (36)

| Loại | Số dòng | Keys |
|---|---|---|
| Rên (moan) | 32 | 1007, 1009, 1010, 1013, 1016, 1021, 1023, 1025, 1030, 1033, 1034, 1036, 1037, 1039, 1041, 1042, 1044, 1046, 1048, 1053, 1070, 1071, 1076, 1077, 1084, 1096, 1100, 1109, 1121, 1123, 1124, 1125 |
| Thở gấp (gasp) | 3 | 1018, 1262, 1264 |
| SFX | 1 | 1107 |

Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0, sai nghĩa nội dung 0, thuật ngữ 0, đại từ 0.

Quy tắc đếm nguyên âm áp dụng ở đây: đếm từng chữ nguyên âm JP một cách chặt chẽ (theo quyết định 21/11 'a-run → strict by JP mora count'); công thức 'VN vowel count = 1 + số う/ぅ' là dạng rút gọn cho trường hợp gốc một âm tiết. Romaji họ ひゃ/ひゅ/ひあ/きゃ/きゅ theo quyết định 21/11 ~11:55; や→Ya theo tiền lệ mất phụ âm ポーレットh3; fa/fu theo quy tắc đã chốt (ふあ→'phùa', ふや→'phuya').

## §1. Rên (moan) (32)

### 1007 [日々姫]
- JP: `「やあっ――乳首っ――つねったら――んっ――あっ」`
- TW: `「呀――乳頭――被捏到了――嗯――啊」`
- VN cũ: `「A――Núm vú――bị véo――ưm――a」`
- Fix: `「Yaa――Núm vú――bị véo――ưm――a」`
- やあっ là tiếng rên mở đầu (ya + a dài); VN cũ 'A' làm mất phụ âm y — tiền lệ ポーレットh3: 'Á' cho やっ là lỗi mất phụ âm. Fix 'Yaa' (2 a: や+あ).

### 1009 [日々姫]
- JP: `「ひゃっ――あっ――らめっ――そんな――\nずるって――抜いちゃっ――んっ――おひりっ――」`
- TW: `「呀――啊――不行――這麼――一抽出來――嗯――屁股要――」`
- VN cũ: `「Hyaa――a――Không được――làm vậy――\nTuột ra――rút ra mất――ưm――mông em――」`
- Fix: `「Hya――a――Không được――làm vậy――\nTuột ra――rút ra mất――ưm――mông em――」`
- ひゃっ chỉ có 1 nguyên âm a; VN cũ 'Hyaa' thừa 1 a. Fix 'Hya' theo đếm nguyên âm từng chữ JP.

### 1010 [日々姫]
- JP: `「やっ――あっ――私の――おもらし――パン、つ――\nにぃにが、ベロで――ちゅう、って――んううっ！！！」`
- TW: `「呀――啊――我的尿――內褲――被阿哥的舌頭――被吸到了――嗯啊！！！」`
- VN cũ: `「A――a――Quần lót――tè dầm――của em――\nAnh hai, dùng lưỡi――mút, lấy――ưm ưm!!!」`
- Fix: `「Ya――a――Quần lót――tè dầm――của em――\nAnh hai, dùng lưỡi――mút, lấy――ưm ưm!!!」`
- やっ → 'Ya' (mất y, như 1007).

### 1013 [日々姫]
- JP: `「ひゃっ――あっ――おっぱい――ンッ――\nにぃに――優、しいっ――ふっ――んっ」`
- TW: `「呀――啊――胸部――嗯――阿哥――好溫柔――呼――嗯」`
- VN cũ: `「Hyaa――a――Ngực――ưm――\nAnh hai――dịu, dàng quá――phù――ưm」`
- Fix: `「Hya――a――Ngực――ưm――\nAnh hai――dịu, dàng quá――phù――ưm」`
- ひゃっ 1 a; 'Hyaa' thừa 1 a → 'Hya'.

### 1016 [日々姫]
- JP: `「ゃふっつ――んっ――ふあっ――そこ――らめっ！\nざらざら――ぐりって、しちゃ、ら――んきゅううっ！」`
- TW: `「呀――嗯――呼――那裡――不行！要是頂到――這個地方――嗯啊！」`
- VN cũ: `「Yafu――ưm――phù――Chỗ đó――không được!\nRam ráp――mà cọ xát, như thế, thì――ưm kyuu!」`
- Fix: `「Yafu――ưm――phùa――Chỗ đó――không được!\nRam ráp――mà cọ xát, như thế, thì――Nkyuuu!」`
- ふあっ → 'phùa' theo quy tắc fa/fu đã chốt (ふあ→'phùa'). んきゅううっ: VN cũ 'ưm kyuu' vừa trộn 2 kiểu diễn (ん→VN 'ưm' + きゅうう→romaji) vừa sai số nguyên âm (2 u thay vì 3: きゅ+う+う); fix 'Nkyuuu!' (tiền lệ んひゅ→'Nhyu').

### 1021 [日々姫]
- JP: `「や……あっ――にぃにの、ぺろぺろ――んっ――\n登って……きてる――ふっ――あ――あっ――んっ！！」`
- TW: `「呀……啊――阿哥的舌頭――嗯――舔上來了……呼――啊――啊――嗯！！」`
- VN cũ: `「A……a――Anh hai, đang liếm――ưm――\nLiếm dần lên……trên――phù――a――a――ưm!!」`
- Fix: `「Ya……a――Anh hai, đang liếm――ưm――\nLiếm dần lên……trên――phù――a――a――ưm!!」`
- や…… → 'Ya……' (mất y).

### 1023 [日々姫]
- JP: `「や……私……おとな……なの、に……おもらし……\nにぃにに……見られて……しちゃ、って……んっ！」`
- TW: `「呀……我……明明是大人了……卻還漏尿……阿哥……還看著我……嗯！」`
- VN cũ: `「A……Em……rõ ràng là……người lớn rồi, mà……lại tè dầm……\nBị anh hai……nhìn thấy……đang tè, thế này……ưm!」`
- Fix: `「Ya……Em……rõ ràng là……người lớn rồi, mà……lại tè dầm……\nBị anh hai……nhìn thấy……đang tè, thế này……ưm!」`
- や…… → 'Ya……' (mất y).

### 1025 [日々姫]
- JP: `「ひゃああうっ！！！？」`
- TW: `「呀啊！！！？」`
- VN cũ: `「Hyaaaau!!!?」`
- Fix: `「Hyaaau!!!?」`
- ひゃああうっ = 3 a + 1 u (ひゃ+あ+あ+う); VN cũ 'Hyaaaau' thừa 1 a → 'Hyaaau'.

### 1030 [日々姫]
- JP: `「やっ！　音っ――はずかしっ――んっ――えっち――\nえっちな――音――おしりっ――んひゅっ――」`
- TW: `「呀！聲音――好羞人――嗯――色色的――色色的――聲音――從屁股――嗯呼――」`
- VN cũ: `「A! Âm thanh――xấu hổ quá――ưm――Gợi tình――\nÂm thanh――gợi tình quá――từ mông――ưm hyu――」`
- Fix: `「Ya! Âm thanh――xấu hổ quá――ưm――Gợi tình――\nÂm thanh――gợi tình quá――từ mông――Nhyu――」`
- やっ → 'Ya'. んひゅっ: VN cũ 'ưm hyu' trộn 2 kiểu diễn; fix 'Nhyu' (tiền lệ んひゅ→'Nhyu').

### 1033 [日々姫]
- JP: `「ひゃああんっ！！？」`
- TW: `「呀！！？」`
- VN cũ: `「Hyaaaan!!?」`
- Fix: `「Hyaaan!!?」`
- ひゃああんっ = 3 a + ん; VN cũ 'Hyaaaan' thừa 2 a → 'Hyaaan'.

### 1034 [日々姫]
- JP: `「ひゃっんっ！？」`
- TW: `「呀！？」`
- VN cũ: `「Hyaa!?」`
- Fix: `「Hyan!?」`
- ひゃっんっ = 1 a + ん; VN cũ 'Hyaa' thừa 1 a và làm mất ん → 'Hyan'.

### 1036 [日々姫]
- JP: `「ひゃっ！？　だめっ――ンッ――ぐいって、\nしたら――あっ――匂い、濃くなるっ――」`
- TW: `「呀！？不行――嗯――這樣的話――啊――味道――就會更濃了――」`
- VN cũ: `「Hyaa!? Không được――Ưm――Ấn mạnh vào,\nnhư thế――a――mùi, sẽ đậm hơn mất――」`
- Fix: `「Hya!? Không được――Ưm――Ấn mạnh vào,\nnhư thế――a――mùi, sẽ đậm hơn mất――」`
- ひゃっ 1 a; 'Hyaa' thừa 1 a → 'Hya'.

### 1037 [日々姫]
- JP: `「ひゃはっ！？　あっ――あっ――は――くっ――」`
- TW: `「呀！？啊――啊――呼――呃――」`
- VN cũ: `「Hyaa!? A――a――Hà――hự――」`
- Fix: `「Hyaha!? A――a――Hà――hự――」`
- ひゃはっ = 2 a (ひゃ+は); VN cũ 'Hyaa' làm mất phụ âm h của は → 'Hyaha' (quy tắc 'không để mất âm').

### 1039 [日々姫]
- JP: `「ひゃうっ！？　あっ――なにっ――なんか――\nんっ――おしり――どろっ――って――ふ――あっ」`
- TW: `「呀！？啊――有什麼――什麼東西――嗯――滑進了――屁股裡――呼――啊」`
- VN cũ: `「Hyaa!? A――Cái gì――thứ gì đó――\nƯm――Mông――nhơm nhớp――vậy――phù――a」`
- Fix: `「Hyau!? A――Cái gì――thứ gì đó――\nƯm――Mông――nhơm nhớp――vậy――phù――a」`
- ひゃうっ = a+u; VN cũ 'Hyaa' viết 2 a, sai nguyên âm thứ hai → 'Hyau'.

### 1041 [日々姫]
- JP: `「ひあっ！？　あっ！　べろっ――やっ――にゅうって！\nおしり――中、まで――なめてっ――ふあ、あ、あっ！」`
- TW: `「呀！？啊！舌頭――呀――進來了！屁股――裡面――都被舔到――呼、啊、啊！」`
- VN cũ: `「Hyaa!? A! Lưỡi――a――đang chui vào!\nMông――Bên trong, cũng――bị liếm――phù, a, a!」`
- Fix: `「Hia!? A! Lưỡi――Ya――đang chui vào!\nMông――Bên trong, cũng――bị liếm――phùa, a, a!」`
- ひあっ → 'Hia' (ひあ không có glide y; quy tắc họ ひゃ 21/11). やっ → 'Ya'. ふあ → 'phùa' (fa/fu).

### 1042 [日々姫]
- JP: `「ふやっ！？　にぃに――舐めてっ――んっ――\nふあっ――あっ――ぺろ、ぺろ――おも――らしっ」`
- TW: `「呀！？阿哥――舔了――嗯――呼――啊――舔了――我的尿」`
- VN cũ: `「Hyaa!? Anh hai――đang liếm――ưm――\nPhù――a――liếm, liếm――nước tiểu――của em」`
- Fix: `「Phuya!? Anh hai――đang liếm――ưm――\nPhùa――a――liếm, liếm――nước tiểu――của em」`
- ふやっ → 'Phuya' (quy tắc đã chốt: ふやぁ→'phuya'; VN cũ 'Hyaa' sai hẳn phụ âm). ふあっ → 'Phùa'.

### 1044 [日々姫]
- JP: `「やあっ！？　にぃに！！？　なんばしよっと！？\n私の――おも、おも――おもらしパンツでっ」`
- TW: `「呀！？阿哥！！？這是要幹什麼啊！？用我的――尿濕的內褲」`
- VN cũ: `「A!? Anh hai!!? Anh định làm gì vậy!?\nDùng――quần lót, quần lót――tè dầm của em」`
- Fix: `「Yaa!? Anh hai!!? Anh định làm gì vậy!?\nDùng――quần lót, quần lót――tè dầm của em」`
- やあっ → 'Yaa' (2 a: や+あ).

### 1046 [日々姫]
- JP: `「やっ！？　にぃにっ、へ、変態っぽい――かもっ――\nんっ――お鼻で、おまんこ――すりすり、なん、てっ」`
- TW: `「呀！？阿哥，這樣有、有點變態――嗯――用鼻子在小穴上――擦來擦去」`
- VN cũ: `「A!? Anh hai, c-có vẻ hơi biến thái――đấy――\nƯm――Dùng mũi, cọ cọ――vào âm đạo――như thế」`
- Fix: `「Ya!? Anh hai, c-có vẻ hơi biến thái――đấy――\nƯm――Dùng mũi, cọ cọ――vào âm đạo――như thế」`
- やっ → 'Ya'.

### 1048 [日々姫]
- JP: `「やっ！？　鼻をうずめて――ンッ――おまんこ、でっ\n――すぅはぁっ――しちゃっ――やぁんっ！」`
- TW: `「呀！？鼻子整個埋了進去――在小穴那裡――吸氣――不行――哎呀！」`
- VN cũ: `「A!? Vùi mũi vào――Ưm――âm đạo,\nrồi――hít hà――như thế――không chịu đâu!」`
- Fix: `「Ya!? Vùi mũi vào――Ưm――âm đạo,\nrồi――hít hà――như thế――Yaan!」`
- やっ → 'Ya'. Đuôi やぁんっ: VN cũ 'không chịu đâu!' bịa thêm cả một mệnh đề không có trong JP (JP chỉ là tiếng rên 'yaan'); fix 'Yaan!' theo quy tắc không bịa thêm.

### 1053 [日々姫]
- JP: `「ふあっ――あっ――」`
- TW: `「呼――啊――」`
- VN cũ: `「Phù――a――」`
- Fix: `「Phùa――a――」`
- ふあっ → 'Phùa' (fa/fu).

### 1070 [日々姫]
- JP: `「あっ――やっ――おしり――の穴っ――んっ――\n勝手に――くぱ――くぱっ――して――きちゃ、んっ」`
- TW: `「啊――呀――屁股――屁眼――嗯――自己就――一張一合的――呀、嗯」`
- VN cũ: `「A――a――Lỗ――hậu môn――ưm――\nTự động――đóng――mở――rồi, ưm」`
- Fix: `「A――Ya――Lỗ――hậu môn――ưm――\nTự động――đóng――mở――rồi, ưm」`
- やっ → 'Ya'.

### 1071 [日々姫]
- JP: `「あっ――ふあっ――」`
- TW: `「啊――呼――」`
- VN cũ: `「A――phù――」`
- Fix: `「A――phùa――」`
- ふあっ → 'phùa'.

### 1076 [日々姫]
- JP: `「あっ――んっ――それ――しゅごっ――んっ――\nぐりって――しながらっ――ゆっくり――んひゅっ！？」`
- TW: `「啊――嗯――這樣――好厲害――嗯――一快――然後――一慢――嗯啊！？」`
- VN cũ: `「A――ưm――Chỗ đó――tuyệt quá――ưm――\nVừa――ngoáy――vừa――chậm lại――ưm hyu!?」`
- Fix: `「A――ưm――Chỗ đó――tuyệt quá――ưm――\nVừa――ngoáy――vừa――chậm lại――Nhyu!?」`
- んひゅっ: VN cũ 'ưm hyu' trộn 2 kiểu diễn; fix 'Nhyu'.

### 1077 [日々姫]
- JP: `「あっ――んっ――直、接っ――ふあっ――んっ」`
- TW: `「啊――嗯――這樣直接――呼――嗯」`
- VN cũ: `「A――ưm――Trực, tiếp――phù――ưm」`
- Fix: `「A――ưm――Trực, tiếp――phùa――ưm」`
- ふあっ → 'phùa'.

### 1084 [日々姫]
- JP: `「あ……あっ――どくどく――してっ――ふあっ――\nおしり――にぃにの――精、液――あ、つい――んっ」`
- TW: `「啊……啊――精液――咕嚕咕嚕地――呼――屁股裡面――阿哥的――精液――好燙――嗯」`
- VN cũ: `「A……a――Từng đợt――phù――\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」`
- Fix: `「A……a――Từng đợt――phùa――\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」`
- ふあっ → 'phùa'.

### 1096 [日々姫]
- JP: `「あんっ」`
- TW: `「啊」`
- VN cũ: `「A」`
- Fix: `「An」`
- あんっ: VN cũ 'A' làm mất ん; fix 'An' (tiền lệ ハチロク01 2319: phụ âm cuối n đã truyền tải được sự cụt).

### 1100 [日々姫]
- JP: `「ふあっ！？　アッ――おまんこ――じゅうって！\nパンツの、上、から――ちゅうちゅう――吸われ――ん」`
- TW: `「啊！？啊――小穴――被吸到了！隔著內褲――被吸到了――嗯」`
- VN cũ: `「A!? A――Âm đạo――kêu chụt chụt!\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」`
- Fix: `「Phùa!? A――Âm đạo――kêu chụt chụt!\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」`
- ふあっ: VN cũ 'A!?' làm mất hẳn âm f; fix 'Phùa!?'.

### 1109 [日々姫]
- JP: `「んっ――ふっ――きゅっ――はあっ」`
- TW: `「嗯――呼――啊――呼」`
- VN cũ: `「Ưm――phù――ưm――hà」`
- Fix: `「Ưm――phù――Kyu――hà」`
- きゅっ → 'Kyu' (họ きゃ/きゅ → romaji); VN cũ 'ưm' làm mất phụ âm ky.

### 1121 [日々姫]
- JP: `「んひゃううううっ！？　ひあっ――おひっ――\nそこっ――にぃに――おしりっ――ふあ――あっ！！？」`
- TW: `「嗯呀！？呀――屁――那裡是――阿哥――屁股――呼――啊！！？」`
- VN cũ: `「Ưm hyaa!? Hya――Mô――\nChỗ đó――Anh hai――Mông――phù――a!!?」`
- Fix: `「Nhyauuuu!? Hia――Mô――\nChỗ đó――Anh hai――Mông――phùa――a!!?」`
- んひゃううううっ: VN cũ 'Ưm hyaa' trộn 2 kiểu diễn (ん→'Ưm' + ひゃ→romaji) và sai số nguyên âm (a+2u thay vì a+4u); fix 'Nhyauuuu' (a+4u). ひあっ → 'Hia'. ふあ → 'phùa'.

### 1123 [日々姫]
- JP: `「くふうううううんっっっ」`
- TW: `「嗯啊」`
- VN cũ: `「Ưm a」`
- Fix: `「Kufuuuuuuun!!!」`
- くふうううううんっっっ (8 u + ん + っ×3): VN cũ 'Ưm a' làm mất gần như toàn bộ tiếng rên; fix 'Kufuuuuuuun!!!' (8 u, n cho ん, !!! cho っっっ).

### 1124 [日々姫]
- JP: `「んふううううううううううっっ！！！！」`
- TW: `「嗯啊啊啊！！！！」`
- VN cũ: `「Ưm phuuuuuuuuuuu!!!!」`
- Fix: `「Ưm phuuuuuuuuuuuu!!!!」`
- んふううううううううううっっ: chuỗi ph cần 11 u (ふ+10う); VN cũ chỉ có 10 u → thêm 1 u. 'Ưm' giữ nguyên cho ん đầu dòng.

### 1125 [日々姫]
- JP: `「くひゅうううううんっ！！！」`
- TW: `「嗯啊！！！」`
- VN cũ: `「Ưm a!!!」`
- Fix: `「Kuhyuuuuuun!!!」`
- くひゅうううううんっ (7 u + ん + っ): VN cũ 'Ưm a!!!' làm mất hẳn くひゅ; fix 'Kuhyuuuuuun!!!' (7 u, n cho ん, !!! cho っ).

## §2. Thở gấp (gasp) (3)

### 1018 [日々姫]
- JP: `「きゃんっ――っ――うっ――はげ――しっ――んっ――\nおしりっ――めくれて――おされ、て――ふ――あっ」`
- TW: `「呀――嗯――唔――好激烈――嗯――屁股裡――被捲起來――捅進去――呼」`
- VN cũ: `「Kyan――ưm――hự――Mãnh――liệt quá――ưm――\nMông em――bị lộn ngược――bị đẩy, vào――phù――a」`
- Fix: `「Kyan――ư――hự――Mãnh――liệt quá――ưm――\nMông em――bị lộn ngược――bị đẩy, vào――phù――a」`
- っ đứng một mình giữa dòng là một tiếng nghẹn/gasp → 'Ư' theo quy tắc gasp; VN cũ 'ưm' thêm âm m không có trong JP.

### 1262 [日々姫]
- JP: `「っ！」`
- TW: `「！」`
- VN cũ: `「っ!」`
- Fix: `「Ư!」`
- っ thô còn sót trong VN; áp nguyên văn fix của sweep: 'Ư!'.

### 1264 [双鉄H]
- JP: `「っ！？」`
- TW: `「！？」`
- VN cũ: `「!?」`
- Fix: `「Ư!?」`
- Gasp cả dòng っ bị mất; áp nguyên văn fix của sweep: 'Ư!?'.

## §3. SFX (1)

### 1107 [双鉄H]
- JP: `「ううむ――」`
- TW: `「嗯――」`
- VN cũ: `「Ưm——」`
- Fix: `「Ừm——」`
- ううむ là tiếng trầm ngâm suy nghĩ của Soutetsu, không phải tiếng rên; 'Ưm' trong file này đã dùng cho ん/んっ (rên), gây nhầm; fix 'Ừm'.

## §4. Sweep gasp (kiểm tra trực tiếp trong sweep-raw-gasp-wrong.json)

- File có 3 mục sweep, đã kiểm tra từng mục đối chiếu JP:
- 1262 (raw-tsu): JP 「っ！」 — VN cũ 「っ!」 còn っ thô; áp nguyên văn fix sweep 「Ư!」. ĐÃ SỬA (mục 1262 trong §2).
- 1264 (lost-gasp-whole): JP 「っ！？」 — VN cũ 「!?」 mất hẳn gasp; áp nguyên văn fix sweep 「Ư!?」. ĐÃ SỬA (mục 1264 trong §2).
- 1855 (needs-file-audit): JP （スンっ――スン――っ！） — sweep nghi lệch dòng vì không đặt được gasp chắc chắn. Đã kiểm chứng: dòng KHÔNG lệch, VN ở đúng key 1855, dịch cả hai tiếng khịt mũi ('Khịt khịt——Khịt khịt!'), っ！ cuối được '!' truyền tải. KHÔNG SỬA.
- Ngoài ra đã quét cơ học toàn bộ 205 dòng JP có っ/ッ trong file: các っ còn lại đều đã được diễn đạt (Ưm/Ư/chụt/phụt/dấu gạch ngang) hoặc thuộc các dòng rên đã sửa ở §1; không còn っ thô trong VN sau khi sửa (kiểm chứng cơ học: chỉ còn 1262, đã sửa).

## §5. Đại từ (không sửa dòng nào)

- Soutetsu là 'anh' với Hibiki trong toàn file — đúng quy tắc đã chốt (Hibiki gọi 'anh hai' xuyên suốt; các dòng 1157 'Anh cũng yêu em', 1166, 1172, 1195, 1132 đều đúng). Hibiki tự xưng 'em'. Không có dòng nào dùng 'tôi' sai với Hibiki.
- Không có nhân vật nào khác xuất hiện (chỉ monologue / 日々姫 / 双鉄H). Không có cụm 'bọn tôi'/'bọn anh'.

## §6. Các dòng giữ nguyên có chủ đích (ghi lại để khỏi sửa lại sau này)

- 1111, 1114 — ぷあっ của Soutetsu giữ 'Phù': đây là tiếng thở ra (exhale) khi đang liếm, không phải tiếng rên; quy tắc fa/fu (ふあ→'phùa') áp cho rên của Hibiki (1041/1042/1053/1071/1077/1084/1100/1016/1121). Phân biệt này đã áp nhất quán.
- 1112 (ん……ふ……ぁっ → 'Ưm……phù……a'), 1073 (ぁ――あっ → 'A――a') — あっ/ぁっ cuối dòng được diễn thành 'a' trần; xem cờ §7 (1).
- 1050 (ぬ―― → 'Ư――') — giữ: 'Ư' là tiếng gầm trầm tự nhiên trong VN; 'Nư' không tự nhiên. Xem cờ §7 (2).
- 1082 (あ……う――っ―― → 'A……ư――') — giữ: dấu gạch ngang đã truyền tải sự ngắt quãng; xem cờ §7 (3).
- 1024 (ひゃぁんっ → 'Hyaan'), 1026 (ひゃんっ → 'Hyan!'), 1031 (きゃふっ → 'Kyafu!!'), 1018-きゃんっ (→ 'Kyan'), 1600 (ひゃあ→'Hyaa', いやぁん→'Iyaan'), 1097/1098/1072 (くあっ → 'Kua'), 1105/1106 (はうっ → 'Hau'), 1143 (きゅふう×13んんっっっ → 'Kyufuuuuuuuuuuuuuun!!!' — đếm cơ học: 15 u = きゅ+ふ+13う, đúng), 1124 đã sửa ở §1 — các dòng rên này đã đúng, không sửa.
- SFX dạng động từ giữ nguyên (theo TW, nhất quán trong file): 1837 (ふにっ――もみゅっ―― → 'Nắn bóp——Xoa nắn——'), 1843 (ぺちょっ → 'Nhặt lên'), 1844 (きゅうううっ → 'Thắt chặt!!!'), 1852 (てろおおおおおおおっ → 'Chảy xuống'), 1857 (れろおおおおおっっ → 'Liếm láp'), 1867 (ぐっ → 'Nằm sấp'), 1832 (ぬるうううううううううううううっっっ → 'Trượt ra!'), 1838 (ぬぶっ → 'Xuyên vào'), 1833 (くりっ → 'Vê nhẹ!').
- 1135 Terre Verte: テルベルト dịch đúng 'Terre Verte' (màu sơn dầu xanh đất). 1869 (ひょい → 'Vén lên'), 1835 (つ――つ―― → 'Chỉ chỉ') đúng.

## §7. Cờ cho Hieu (không tự quyết)

1. 1073, 1112 — あっ/ぁっ cuối dòng không dấu câu, VN chỉ còn 'a' trần: tiếng cụt っ có thể coi là mất hẳn (theo biên gasp: Ư chỉ khi っ mất hoàn toàn — trường hợp này đúng là cuối dòng tuyệt đối, không dấu câu). Nhưng dạng 'aƯ' chưa từng xuất hiện trong các file đã merge; để vòng moan-fix phán lại, không sửa trong audit này.
2. 1050 — ぬ―― → 'Ư': âm n đầu bị mất; 'Nư' nghe không tự nhiên. Giữ nguyên, ghi cờ.
3. 1082 — う――っ―― → 'ư――': っ sau う―― không được diễn riêng; dấu gạch ngang truyền tải sự ngắt. Giữ nguyên, ghi cờ.
4. [character_subs] 1557/1712 trỏ key không có trong script — dư thừa vô hại (cùng mẫu Kisaki 1961); không tính lỗi. Nếu Hieu muốn dọn thì dọn ở đợt thống nhất.
5. B19 vẫn park (không có tag %l nào trong file nên không phát sinh thêm).

## §8. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 36 fix đối chiếu trực tiếp với JP của từng dòng (không chỉ parse-check): **36 tổng / 36 soát lại đạt / 0 bỏ / 0 sửa**. Trong lượt soát 2, kiểm tra thêm: không fix nào thay đổi ngoài phần cần sửa (diff-sanity cơ học: mọi khối thay đổi đều ≤12 ký tự phía cũ / ≤14 ký tự phía mới — xem log build); JP/TW/old_vn trong JSON khớp CSV3 tuyệt đối 36/36; đếm nguyên âm các dòng rên dài đã kiểm chứng lại bằng đếm cơ học (1123: 8 u; 1125: 7 u; 1124: chuỗi ph 11 u; 1143 giữ nguyên: 15 u đúng; 1025: 3a+1u; 1033: 3a; 1016-んきゅううっ: 3u; 1121-んひゃううううっ: a+4u). JSON 36 mục (key chuỗi); khối TOML 36 khóa parse OK, 0 sai lệch giá trị; không fix nào làm rơi dấu 「」.

## Khối TOML (đã parse-kiểm chứng: 36 khóa, 0 sai lệch giá trị)

```toml
"1007" = "「Yaa――Núm vú――bị véo――ưm――a」"
"1009" = "「Hya――a――Không được――làm vậy――\\nTuột ra――rút ra mất――ưm――mông em――」"
"1010" = "「Ya――a――Quần lót――tè dầm――của em――\\nAnh hai, dùng lưỡi――mút, lấy――ưm ưm!!!」"
"1013" = "「Hya――a――Ngực――ưm――\\nAnh hai――dịu, dàng quá――phù――ưm」"
"1016" = "「Yafu――ưm――phùa――Chỗ đó――không được!\\nRam ráp――mà cọ xát, như thế, thì――Nkyuuu!」"
"1018" = "「Kyan――ư――hự――Mãnh――liệt quá――ưm――\\nMông em――bị lộn ngược――bị đẩy, vào――phù――a」"
"1021" = "「Ya……a――Anh hai, đang liếm――ưm――\\nLiếm dần lên……trên――phù――a――a――ưm!!」"
"1023" = "「Ya……Em……rõ ràng là……người lớn rồi, mà……lại tè dầm……\\nBị anh hai……nhìn thấy……đang tè, thế này……ưm!」"
"1025" = "「Hyaaau!!!?」"
"1030" = "「Ya! Âm thanh――xấu hổ quá――ưm――Gợi tình――\\nÂm thanh――gợi tình quá――từ mông――Nhyu――」"
"1033" = "「Hyaaan!!?」"
"1034" = "「Hyan!?」"
"1036" = "「Hya!? Không được――Ưm――Ấn mạnh vào,\\nnhư thế――a――mùi, sẽ đậm hơn mất――」"
"1037" = "「Hyaha!? A――a――Hà――hự――」"
"1039" = "「Hyau!? A――Cái gì――thứ gì đó――\\nƯm――Mông――nhơm nhớp――vậy――phù――a」"
"1041" = "「Hia!? A! Lưỡi――Ya――đang chui vào!\\nMông――Bên trong, cũng――bị liếm――phùa, a, a!」"
"1042" = "「Phuya!? Anh hai――đang liếm――ưm――\\nPhùa――a――liếm, liếm――nước tiểu――của em」"
"1044" = "「Yaa!? Anh hai!!? Anh định làm gì vậy!?\\nDùng――quần lót, quần lót――tè dầm của em」"
"1046" = "「Ya!? Anh hai, c-có vẻ hơi biến thái――đấy――\\nƯm――Dùng mũi, cọ cọ――vào âm đạo――như thế」"
"1048" = "「Ya!? Vùi mũi vào――Ưm――âm đạo,\\nrồi――hít hà――như thế――Yaan!」"
"1053" = "「Phùa――a――」"
"1070" = "「A――Ya――Lỗ――hậu môn――ưm――\\nTự động――đóng――mở――rồi, ưm」"
"1071" = "「A――phùa――」"
"1076" = "「A――ưm――Chỗ đó――tuyệt quá――ưm――\\nVừa――ngoáy――vừa――chậm lại――Nhyu!?」"
"1077" = "「A――ưm――Trực, tiếp――phùa――ưm」"
"1084" = "「A……a――Từng đợt――phùa――\\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」"
"1096" = "「An」"
"1100" = "「Phùa!? A――Âm đạo――kêu chụt chụt!\\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」"
"1107" = "「Ừm——」"
"1109" = "「Ưm――phù――Kyu――hà」"
"1121" = "「Nhyauuuu!? Hia――Mô――\\nChỗ đó――Anh hai――Mông――phùa――a!!?」"
"1123" = "「Kufuuuuuuun!!!」"
"1124" = "「Ưm phuuuuuuuuuuuu!!!!」"
"1125" = "「Kuhyuuuuuun!!!」"
"1262" = "「Ư!」"
"1264" = "「Ư!?」"
```

## Kết bài

File 日々姫h3_汚れてしまった制服で: đọc 322/322 dòng, sai **36 dòng (11,2%)** — rên 32, thở gấp 3 (2 từ sweep), SFX 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Lỗi tập trung ở các dòng rên H-scene: romaji họ ひゃ/や bị viết thành 'A'/'Hyaa' sai số nguyên âm hoặc mất phụ âm (y, h, f, ky, n), fa/fu viết 'phù' thay vì 'phùa', 3 dòng rên dài bị viết gọn thành 'Ưm a', và 2 gasp っ từ sweep. Đại từ Soutetsu 'anh' với Hibiki đúng toàn file; không có thuật ngữ cần sửa; không có tag %l lệch. Cờ cho Hieu: 1073/1112 (あっ cuối dòng → 'a' trần), 1050 (ぬ―― → 'Ư'), 1082 (う――っ―― → 'ư――'), [character_subs] 1557/1712 dư thừa. Lượt soát 2: 36/36/0/0. Khối TOML 36 khóa parse đạt, 0 sai lệch.