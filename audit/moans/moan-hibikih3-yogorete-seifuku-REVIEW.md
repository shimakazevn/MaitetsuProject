# Moan-fix: 日々姫h3_汚れてしまった制服で.txt.toml (moan-hibikih3-yogorete-seifuku)

- File: `02_Hibiki/日々姫h3_汚れてしまった制服で.txt.toml` — route 02_Hibiki, 322 dòng script. Cảnh H — Soutetsu và Hibiki (đồng phục bị bẩn, Hibiki tè dầm).
- TOML md5 `fd705de9bad2a12e224c2264772c06d6` (khớp md5 audit), 56,082 bytes, UTF-8 BOM + CRLF (663 CRLF). 1 bản duy nhất toàn dự án (không có file trùng).
- CSV3: 1 bộ duy nhất, 322 dòng, 0 khóa trùng, 0 VN trống. TOML `[script]` 322 khóa khớp CSV3 322/322; giá trị VN khớp phẳng (TOML-2 làm phẳng `\n` literal thành khoảng trắng ở một số dòng — CSV3 là chuẩn).
- Audit trước đó: 36 sai — đã gộp vào ROUTE-AUDIT.md. File không có dòng "Kh" nào. Sweep gasp: 3 mục kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — 1262/1264 đã nằm trong audit (Ư khóa, không đụng); 1855 （スンっ――スン――っ！）sweep không đặt được gasp chắc chắn, VN "Khịt khịt——Khịt khịt!" diễn đủ hai tiếng sniff, giữ nguyên.

## 1. Moan inventory — xét 116 dòng rên/SFX, đổi 24, giữ 92

- Đã đọc 322/322 dòng (CSV3 + TOML-2).
- Đổi 24 dòng: 16 trùng key audit (chỉ khác giá trị audit đúng token rên) + 8 key mới (1027, 1050, 1055, 1056, 1111, 1112, 1114, 1142).
- Lỗi chính: họ fa/fu bị Việt hoá "phà"/"phùa"/"phù" (19 dòng → romaji Fa/Fua/Fu/Pua); ひあ → "Hyaa" (1027 → "Hia"); mất phụ âm mora (1050 ぬ→"Ư", 1056/1111/1114 ぷあ→"phù"/"Phù", 1010 んうう→"ưm ưm"); trộn 2 hệ trong một âm (1124).
- 0 dòng gasp Ư bị đụng, 0 dòng "Kh" (file không có), 0 dòng đại từ/thuật ngữ/nghĩa.

## 2. Chi tiết từng dòng sửa

### 1010 [日々姫]

- JP: `「やっ――あっ――私の――おもらし――パン、つ――\nにぃにが、ベロで――ちゅう、って――んううっ！！！」`
- TW: `「呀――啊――我的尿――內褲――被阿哥的舌頭――被吸到了――嗯啊！！！」`
- Cũ: `「Ya――a――Quần lót――tè dầm――của em――\nAnh hai, dùng lưỡi――mút, lấy――ưm ưm!!!」`
- Mới: `「Ya――a――Quần lót――tè dầm――của em――\nAnh hai, dùng lưỡi――mút, lấy――Nuu!!!」`
- Lý do: Một âm rên duy nhất んううっ bị tách thành hai tiếng "ưm ưm" + mất hẳn nguyên âm うう — gộp về một rendering romaji "Nuu" (ん1n + う×2 = 2u); tiền lệ tách mảnh ở moan-真闇h3.

### 1013 [日々姫]

- JP: `「ひゃっ――あっ――おっぱい――ンッ――\nにぃに――優、しいっ――ふっ――んっ」`
- TW: `「呀――啊――胸部――嗯――阿哥――好溫柔――呼――嗯」`
- Cũ: `「Hya――a――Ngực――ưm――\nAnh hai――dịu, dàng quá――phù――ưm」`
- Mới: `「Hya――a――Ngực――ưm――\nAnh hai――dịu, dàng quá――Fu――ưm」`
- Lý do: ふっ trong chuỗi rên → romaji "Fu" (fallback Hieu duyệt 21/11 ~01:56; tiền lệ moan h6 §3a, lr_mayami-tsuika-h, h4).

### 1016 [日々姫]

- JP: `「ゃふっつ――んっ――ふあっ――そこ――らめっ！\nざらざら――ぐりって、しちゃ、ら――んきゅううっ！」`
- TW: `「呀――嗯――呼――那裡――不行！要是頂到――這個地方――嗯啊！」`
- Cũ: `「Yafu――ưm――phùa――Chỗ đó――không được!\nRam ráp――mà cọ xát, như thế, thì――Nkyuuu!」`
- Mới: `「Yafu――ưm――Fua――Chỗ đó――không được!\nRam ráp――mà cọ xát, như thế, thì――Nkyuuu!」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56; tiền lệ h6 §3a). Audit đổi "phù"→"phùa", moan đổi tiếp → "Fua".

### 1018 [日々姫]

- JP: `「きゃんっ――っ――うっ――はげ――しっ――んっ――\nおしりっ――めくれて――おされ、て――ふ――あっ」`
- TW: `「呀――嗯――唔――好激烈――嗯――屁股裡――被捲起來――捅進去――呼」`
- Cũ: `「Kyan――ư――hự――Mãnh――liệt quá――ưm――\nMông em――bị lộn ngược――bị đẩy, vào――phù――a」`
- Mới: `「Kyan――ư――hự――Mãnh――liệt quá――ưm――\nMông em――bị lộn ngược――bị đẩy, vào――Fu――a」`
- Lý do: ふ――あっ là hai mora tách riêng (ふ + あ), không phải một âm ふあ — "Fu――a" (tiền lệ moan 2359/2371: ふ tách riêng → "Fu, a"/"Fu……a").

### 1021 [日々姫]

- JP: `「や……あっ――にぃにの、ぺろぺろ――んっ――\n登って……きてる――ふっ――あ――あっ――んっ！！」`
- TW: `「呀……啊――阿哥的舌頭――嗯――舔上來了……呼――啊――啊――嗯！！」`
- Cũ: `「Ya……a――Anh hai, đang liếm――ưm――\nLiếm dần lên……trên――phù――a――a――ưm!!」`
- Mới: `「Ya……a――Anh hai, đang liếm――ưm――\nLiếm dần lên……trên――Fu――a――a――ưm!!」`
- Lý do: ふっ trong chuỗi rên → romaji "Fu" (fallback 21/11 ~01:56).

### 1027 [日々姫]

- JP: `「ひあっ！　は――あっ――これっ――おしりっ――\nんっ――あっ――れろって――される、とぉ――んっ」`
- TW: `「呀！呼――啊――那裡――屁股――嗯――啊――被舔到的話――嗯――」`
- Cũ: `「Hyaa! Hà――a――Thế này――mông――\nƯm――a――Bị liếm――thế này, thì――ưm」`
- Mới: `「Hia! Hà――a――Thế này――mông――\nƯm――a――Bị liếm――thế này, thì――ưm」`
- Lý do: ひあっ → "Hia", KHÔNG phải "Hyaa" — quy tắc 3b (ひゃ/ひゅ/ひあ/きゃ → romaji; "Á"/"Hyaa" cho ひあ là mất âm). Tiền lệ moan-凪h2 (5 dòng ひあ→Hia).

### 1039 [日々姫]

- JP: `「ひゃうっ！？　あっ――なにっ――なんか――\nんっ――おしり――どろっ――って――ふ――あっ」`
- TW: `「呀！？啊――有什麼――什麼東西――嗯――滑進了――屁股裡――呼――啊」`
- Cũ: `「Hyau!? A――Cái gì――thứ gì đó――\nƯm――Mông――nhơm nhớp――vậy――phù――a」`
- Mới: `「Hyau!? A――Cái gì――thứ gì đó――\nƯm――Mông――nhơm nhớp――vậy――Fu――a」`
- Lý do: ふ――あっ là hai mora tách riêng — "Fu――a" (tiền lệ moan 2359/2371).

### 1041 [日々姫]

- JP: `「ひあっ！？　あっ！　べろっ――やっ――にゅうって！\nおしり――中、まで――なめてっ――ふあ、あ、あっ！」`
- TW: `「呀！？啊！舌頭――呀――進來了！屁股――裡面――都被舔到――呼、啊、啊！」`
- Cũ: `「Hia!? A! Lưỡi――Ya――đang chui vào!\nMông――Bên trong, cũng――bị liếm――phùa, a, a!」`
- Mới: `「Hia!? A! Lưỡi――Ya――đang chui vào!\nMông――Bên trong, cũng――bị liếm――Fua, a, a!」`
- Lý do: ふあ → romaji "Fua" (fallback 21/11 ~01:56).

### 1042 [日々姫]

- JP: `「ふやっ！？　にぃに――舐めてっ――んっ――\nふあっ――あっ――ぺろ、ぺろ――おも――らしっ」`
- TW: `「呀！？阿哥――舔了――嗯――呼――啊――舔了――我的尿」`
- Cũ: `「Phuya!? Anh hai――đang liếm――ưm――\nPhùa――a――liếm, liếm――nước tiểu――của em」`
- Mới: `「Phuya!? Anh hai――đang liếm――ưm――\nFua――a――liếm, liếm――nước tiểu――của em」`
- Lý do: ふあっ → "Fua" (fallback 21/11 ~01:56). ふやっ GIỮ "Phuya" — dạng khóa (AUDIT-BRIEF.md quy tắc 5), tiền lệ moan-h4 giữ "Phuya" (988, 1121).

### 1050 [双鉄H]

- JP: `「ぬ――あっ――」`
- TW: `「呃――啊――」`
- Cũ: `「Ư――a――」`
- Mới: `「Nuu――a――」`
- Lý do: ぬ―― bị mất phụ âm n ("Ư") — khôi phục "Nuu" (tiền lệ ROUTE-MOANS 2686: ぬ――→"Nuu").

### 1053 [日々姫]

- JP: `「ふあっ――あっ――」`
- TW: `「呼――啊――」`
- Cũ: `「Phùa――a――」`
- Mới: `「Fua――a――」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56).

### 1055 [日々姫]

- JP: `「はっ――あっ――なに――これっ――ふ――んっ――\n吸って――吸ってる――私の、子宮――っ――んっ」`
- TW: `「呼――啊――這是――怎麼回事――呼――嗯――我的子宮――在吸――在吸呢――嗯」`
- Cũ: `「Hà――a――Cái gì――thế này――phù――ưm――\nĐang hút――Tử cung của em――đang hút lấy――ưm」`
- Mới: `「Hà――a――Cái gì――thế này――Fu――ưm――\nĐang hút――Tử cung của em――đang hút lấy――ưm」`
- Lý do: ふ――んっ: ふ tách riêng → "Fu", んっ giữ "ưm" — "Fu――ưm" (tiền lệ moan 2359/2371).

### 1056 [双鉄H]

- JP: `「ぷあっ――ん、む――日々姫。\nお前……ひょっとしておしっこをしたいのか？」`
- TW: `「呼――嗯――日日姬。你……是不是想尿尿？」`
- Cũ: `「Phù――ưm, này――Hibiki.\nEm……không lẽ là đang buồn tè sao?」`
- Mới: `「Pua――ưm, này――Hibiki.\nEm……không lẽ là đang buồn tè sao?」`
- Lý do: ぷあっ bị mất mora あ ("Phù") — khôi phục romaji "Pua" (tiền lệ h1: ぷあ→"Pua"; moan-h6 §3a).

### 1071 [日々姫]

- JP: `「あっ――ふあっ――」`
- TW: `「啊――呼――」`
- Cũ: `「A――phùa――」`
- Mới: `「A――Fua――」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56).

### 1077 [日々姫]

- JP: `「あっ――んっ――直、接っ――ふあっ――んっ」`
- TW: `「啊――嗯――這樣直接――呼――嗯」`
- Cũ: `「A――ưm――Trực, tiếp――phùa――ưm」`
- Mới: `「A――ưm――Trực, tiếp――Fua――ưm」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56).

### 1084 [日々姫]

- JP: `「あ……あっ――どくどく――してっ――ふあっ――\nおしり――にぃにの――精、液――あ、つい――んっ」`
- TW: `「啊……啊――精液――咕嚕咕嚕地――呼――屁股裡面――阿哥的――精液――好燙――嗯」`
- Cũ: `「A……a――Từng đợt――phùa――\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」`
- Mới: `「A……a――Từng đợt――Fua――\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56).

### 1100 [日々姫]

- JP: `「ふあっ！？　アッ――おまんこ――じゅうって！\nパンツの、上、から――ちゅうちゅう――吸われ――ん」`
- TW: `「啊！？啊――小穴――被吸到了！隔著內褲――被吸到了――嗯」`
- Cũ: `「Phùa!? A――Âm đạo――kêu chụt chụt!\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」`
- Mới: `「Fua!? A――Âm đạo――kêu chụt chụt!\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」`
- Lý do: ふあっ → romaji "Fua" (fallback 21/11 ~01:56).

### 1109 [日々姫]

- JP: `「んっ――ふっ――きゅっ――はあっ」`
- TW: `「嗯――呼――啊――呼」`
- Cũ: `「Ưm――phù――Kyu――hà」`
- Mới: `「Ưm――Fu――Kyu――hà」`
- Lý do: ふっ trong chuỗi rên → romaji "Fu" (fallback 21/11 ~01:56). Audit chỉ sửa きゅっ→"Kyu", giữ ふっ→"phù".

### 1111 [双鉄H]

- JP: `「ん――ぷあっ――それから、僕の唾液や、汗や、\n体液の匂いが、全部、混じって」`
- TW: `「嗯――呼――這樣的話，我的唾液、汗水，還有體液的味道，也全部混進去了」`
- Cũ: `「Ưm――Phù――Sau đó, mùi nước bọt, mồ hôi,\nvà cả thể dịch của anh, tất cả, hòa quyện lại với nhau」`
- Mới: `「Ưm――Pua――Sau đó, mùi nước bọt, mồ hôi,\nvà cả thể dịch của anh, tất cả, hòa quyện lại với nhau」`
- Lý do: ぷあっ bị mất mora あ ("Phù") — khôi phục romaji "Pua" (tiền lệ h1).

### 1112 [日々姫]

- JP: `「ん……ふ……ぁっ」`
- TW: `「嗯……呼……啊」`
- Cũ: `「Ưm……phù……a」`
- Mới: `「Ưm……Fu……a」`
- Lý do: ふ……ぁっ là hai mora tách riêng (ふ + ぁ) — "Fu……a" (tiền lệ moan 2359/2371).

### 1114 [双鉄H]

- JP: `「ん……ん……ぷあっ――ソックスに――んっ――\n染み、ては――れるっ――いかん――だろう」`
- TW: `「嗯……嗯……噗哈――因為――嗯――不能――把襪子――弄濕啊」`
- Cũ: `「Ưm……ưm……phù――Để thấm――ưm――\nvào tất――thì――không――được――mà」`
- Mới: `「Ưm……ưm……Pua――Để thấm――ưm――\nvào tất――thì――không――được――mà」`
- Lý do: ぷあっ bị mất mora あ ("phù") — khôi phục romaji "Pua" (tiền lệ h1: ぷあ→"Pua").

### 1121 [日々姫]

- JP: `「んひゃううううっ！？　ひあっ――おひっ――\nそこっ――にぃに――おしりっ――ふあ――あっ！！？」`
- TW: `「嗯呀！？呀――屁――那裡是――阿哥――屁股――呼――啊！！？」`
- Cũ: `「Nhyauuuu!? Hia――Mô――\nChỗ đó――Anh hai――Mông――phùa――a!!?」`
- Mới: `「Nhyauuuu!? Hia――Mô――\nChỗ đó――Anh hai――Mông――Fua――a!!?」`
- Lý do: ふあ――あっ → "Fua――a" (fallback 21/11 ~01:56).

### 1124 [日々姫]

- JP: `「んふううううううううううっっ！！！！」`
- TW: `「嗯啊啊啊！！！！」`
- Cũ: `「Ưm phuuuuuuuuuuuu!!!!」`
- Mới: `「Nfuuuuuuuuuuu!!!!」`
- Lý do: Trộn 2 hệ trong MỘT âm (Ưm + phuu…) — gộp về một rendering romaji thuần "Nfuuuuuuuuuuu" (ん gộp vào romaji; tiền lệ "Nfufu"/"Nfufuun", moan-真闇h3). QUAN TRỌNG: fix audit đếm SAI 12u — JP có 10 う → công thức 1+10 = 11u; bản moan 11u đè lên giá trị audit ở đợt thống nhất (xem F1).

### 1142 [日々姫]

- JP: `「深……か――ぁッ――はっ――熱……いっ――ふっ」`
- TW: `「好深……好――呼――好熱……呼――」`
- Cũ: `「Sâu……quá――a――hà――Nóng……quá――phù」`
- Mới: `「Sâu……quá――a――hà――Nóng……quá――Fu」`
- Lý do: ふっ cuối dòng rên → romaji "Fu" (fallback 21/11 ~01:56).

## 3. Kept-moan notes — các dòng rên đã xét, giữ nguyên (lý do 1 dòng mỗi nhóm)

- Audit đã đúng, romaji + đếm nguyên âm kiểm chứng lại bằng máy: 1007 "Yaa", 1009 "Hya", 1025 "Hyaaau" (3a+1u), 1033 "Hyaaan" (3a), 1034 "Hyan", 1036 "Hya", 1037 "Hyaha", 1044 "Yaa", 1046 "Ya", 1048 "Ya"/"Yaan", 1076 "Nhyu", 1096 "An", 1123 "Kufuuuuuuun" (7u), 1125 "Kuhyuuuuuun" (7u), 1030 "Nhyu", 1023 "Ya", 1070 "Ya", 1018 "Kyan", 1031 "Kyafu", 1143 "Kyufuuuuuuuuuuuuuun" (16u), 1024 "Hyaan", 1026 "Hyan", 1016 "Nkyuuu" (3u), 1121 "Nhyauuuu" (1a+4u), 1041 "Hia", 1109 "Kyu".
- ひゃ/ひゅ/ひあ/きゃ toàn file đã đúng quy tắc 3b (19 dòng kiểm tra: chỉ 1027 sai).
- 1136 ふっふーん → "Hừ hừm." — cười đắc ý (smug hum), tiếng Việt tự nhiên, không phải rên; giữ (xem F3).
- 1088 っと → "a" — TW 啊 đồng ý; giữ.
- 1107 ううむ―― → "Ừm——" — hừm suy nghĩ, không phải rên; giữ.
- 1048 すぅはぁっ → "hít hà" — diễn nghĩa rõ (hít vào); giữ.
- 1070 くぱ――くぱっ → "đóng――mở" — diễn nghĩa rõ; giữ.
- SFX trong ngoặc （ ） giữ toàn bộ 48 dòng (quy ước diễn nghĩa của file: "Phập"/"Chụt"/"Bốp"/"Trượt ra"/"Thắt chặt"/"Vén lên"/"Áp sát"/"Nằm sấp"/"Chảy xuống" — tiền lệ các file đã gộp).
- ふ trong từ thường không phải âm rên, giữ: 1713 含まれよう, 1711 フェロモン, 1473 ふともも.
- はっ → "hà"/"Hà", あっ → "a", んっ → "ưm", くっ → "hự" giữ nguyên toàn file (quy ước đã ổn định; "hự" chỉ đổi sang "Ku" ở đúng 1 tiền lệ đơn lẻ, không áp hàng loạt).
- Gasp Ư khóa (1262 "Ư!", 1264 "Ư!?") là giá trị audit, KHÔNG đụng. File không có dòng "Kh".
- ふやっ 1042 giữ "Phuya" — dạng khóa (quy tắc 5), tiền lệ moan-h4 giữ "Phuya" (988, 1121).

## 4. Flags — đợt thống nhất (không tự quyết)

- F1 — 1124: fix audit đếm SAI 12u (JP んふううううううううううっっ có 10 う → công thức 1+10 = 11u; VN gốc CSV3 đã đúng 11u, audit thêm thừa 1u). Bản moan "Nfuuuuuuuuuuu" (11u) đè lên giá trị audit ở đợt thống nhất — parent kiểm chứng lúc gộp.
- F2 — ふっ trong chuỗi rên → "Fu" ở đây (1013, 1109, 1142); đợt thống nhất KHÔNG hoàn lại thành "Phù" (tiền lệ moan h6 §3a, lr_mayami-tsuika-h, h4 — "phù" cho ふ/ふっ trong rên đều đã chuyển romaji).
- F3 — 1136 ふっふーん "Hừ hừm." giữ nguyên ở đây; nếu đợt thống nhất muốn romaji "Fuffuun" thì đổi (không quyết ở đây).
- F4 — 1010 �んううっ "Nuu!!!" là phán đoán mới (một âm dài bị tách thành "ưm ưm" + mất nguyên âm うう); cần parent kiểm chứng lúc gộp.
- F5 — や→"Ya": audit đã dùng "Ya"/"Yaa" toàn file (1007, 1010, 1021, 1023, 1030, 1044, 1046, 1048, 1070); quyết や toàn dự án vẫn mở (ghi chú ROUTE-MOANS 384) — không đổi ở đây.

## 5. Lượt soát 2

- Tổng 24 / tái kiểm chứng 24 / bỏ 0 / sửa 0.
- Lượt soát đọc lại JSON đã ghi + CSV3 + audit JSON, độc lập với lượt xây: mỗi fix đối chiếu lại JP (âm rên + đếm nguyên âm kiểm chứng bằng máy), diff fix-vs-old_vn chỉ khác đúng token rên, không dòng gasp Ư/"Kh" nào bị đụng.
- Cờ 1111 trong lượt soát là lỗi của script kiểm tra (danh sách token ứng viên thiếu "Phù" đứng một mình) — đã xác minh bằng diff trực tiếp: chỉ đổi Phù→Pua, không sửa gì thêm.
- Đếm nguyên âm kiểm chứng độc lập: 1124 11u (ふ1u + う×10 — audit sai 12u), 1010 2u (んうう), 1050 2u (ぬ――, tiền lệ 2686 "Nuu"), 1123 7u, 1125 7u, 1143 16u, 1025 3a+1u, 1033 3a, 1016 3u ("Nkyuuu"), 1121 1a+4u ("Nhyauuuu").

## 6. Khối TOML (đã parse-kiểm chứng: 24 khóa, 0 sai lệch)

```toml
[script]
"1010" = "「Ya――a――Quần lót――tè dầm――của em――\\nAnh hai, dùng lưỡi――mút, lấy――Nuu!!!」"
"1013" = "「Hya――a――Ngực――ưm――\\nAnh hai――dịu, dàng quá――Fu――ưm」"
"1016" = "「Yafu――ưm――Fua――Chỗ đó――không được!\\nRam ráp――mà cọ xát, như thế, thì――Nkyuuu!」"
"1018" = "「Kyan――ư――hự――Mãnh――liệt quá――ưm――\\nMông em――bị lộn ngược――bị đẩy, vào――Fu――a」"
"1021" = "「Ya……a――Anh hai, đang liếm――ưm――\\nLiếm dần lên……trên――Fu――a――a――ưm!!」"
"1027" = "「Hia! Hà――a――Thế này――mông――\\nƯm――a――Bị liếm――thế này, thì――ưm」"
"1039" = "「Hyau!? A――Cái gì――thứ gì đó――\\nƯm――Mông――nhơm nhớp――vậy――Fu――a」"
"1041" = "「Hia!? A! Lưỡi――Ya――đang chui vào!\\nMông――Bên trong, cũng――bị liếm――Fua, a, a!」"
"1042" = "「Phuya!? Anh hai――đang liếm――ưm――\\nFua――a――liếm, liếm――nước tiểu――của em」"
"1050" = "「Nuu――a――」"
"1053" = "「Fua――a――」"
"1055" = "「Hà――a――Cái gì――thế này――Fu――ưm――\\nĐang hút――Tử cung của em――đang hút lấy――ưm」"
"1056" = "「Pua――ưm, này――Hibiki.\\nEm……không lẽ là đang buồn tè sao?」"
"1071" = "「A――Fua――」"
"1077" = "「A――ưm――Trực, tiếp――Fua――ưm」"
"1084" = "「A……a――Từng đợt――Fua――\\nMông em――Tinh, dịch――của anh hai――nóng, quá――ưm」"
"1100" = "「Fua!? A――Âm đạo――kêu chụt chụt!\\nTừ, bên trên, quần lót――bị hút――chùn chụt――ưm」"
"1109" = "「Ưm――Fu――Kyu――hà」"
"1111" = "「Ưm――Pua――Sau đó, mùi nước bọt, mồ hôi,\\nvà cả thể dịch của anh, tất cả, hòa quyện lại với nhau」"
"1112" = "「Ưm……Fu……a」"
"1114" = "「Ưm……ưm……Pua――Để thấm――ưm――\\nvào tất――thì――không――được――mà」"
"1121" = "「Nhyauuuu!? Hia――Mô――\\nChỗ đó――Anh hai――Mông――Fua――a!!?」"
"1124" = "「Nfuuuuuuuuuuu!!!!」"
"1142" = "「Sâu……quá――a――hà――Nóng……quá――Fu」"
```

## Kết bài

File 日々姫h3_汚れてしまった制服で (322 dòng) đã sửa moan xong: 24 dòng đổi (24 romaji, 0 đếm nguyên âm riêng), 92 dòng rên/SFX giữ nguyên, 0 dòng gasp Ư bị đụng, 0 dòng "Kh" (file không có). 16/24 dòng thay thế giá trị audit cùng key (chỉ khác đúng token rên); 8 dòng mới xây trên VN gốc CSV3. Khối TOML 24 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 24/24, 0 bỏ, 0 sửa.
