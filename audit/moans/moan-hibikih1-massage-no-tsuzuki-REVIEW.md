# Moan-fix: 日々姫h1_マッサージの続き.txt.toml — route 02_Hibiki (moan-hibikih1-massage-no-tsuzuki)

- File: `日々姫h1_マッサージの続き.txt.toml` — route 02_Hibiki, 329 dòng script (độc thoại 183, 日々姫 81, 双鉄H 65).
- Nội dung: cảnh H tiếp nối buổi mát xa — đêm sau tiệc mừng chiến thắng, Hibiki sang phòng Soutetsu mát xa cho anh (mát xa đứng, rồi bằng miệng), cả hai thừa nhận muốn làm tình, Soutetsu đề nghị làm tình "đàng hoàng" thay vì thuận đà, Hibiki đồng ý và xin anh lấy đi lần đầu của mình, quan hệ lần đầu, kết bằng những nụ hôn và cả hai chìm vào giấc ngủ.
- Nguồn: TOML-2 `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh1_#U30de#U30c3#U30b5#U30fc#U30b8#U306e#U7d9a#U304d.txt.toml`, md5 `c8169ed72a3a329d6f677624531c75cf` (UTF-8 BOM + CRLF, khớp md5 audit). CSV3: 329 dòng, 1 bộ duy nhất, 0 khóa trùng, VN khớp TOML tuyệt đối 329/329 (0 sai lệch). Không có bản sao file này.
- Phương pháp: đọc từng dòng 329/329 đối chiếu JP + TW (JP thắng khi khác nhau); chỉ sửa tiếng rên/thở/gasp/SFX — không sửa đại từ, thuật ngữ, nghĩa hay lệch vị trí (trừ key 970: kế thừa fix nghĩa của audit, xem §3.1). Kiểm tra trực tiếp 6 mục sweep cho file này trong `sweep-raw-gasp-wrong.json`. Lượt soát 2 toàn bộ fix.

## Kết quả tổng quan

**Đổi 16/329 dòng (moan)** — romaji 14, romaji + đếm nguyên âm 2. **Tổng cộng sau file này: 46 file / 1.230 dòng sai (moan)** (cơ sở 45 file / 1.214 dòng + 16 file này — cơ sở đã kiểm chứng trực tiếp dòng tổng cuối của `moans/ROUTE-MOANS.md`).

## §1. Kiểm kê tiếng rên

Đã đọc 329/329 dòng; quét máy 233 dòng ứng viên, trong đó **147 dòng rên/SFX thực sự**: 106 dòng thoại có âm rên/thở/gasp/SFX + 41 dòng SFX độc thoại trong ngoặc đơn (1862–1915). Đổi 16, giữ 131.

Phân loại 16 dòng đổi (một dòng có thể mang nhiều token, các nhóm chồng nhau):
- Họ ひゃ/ひゅ/ひあ/きゃ → romaji ("Á" mất phụ âm mora): 3 dòng (1002, 1007, 1019).
- やっ → "Ya" ("Á" mất phụ âm y, tiền lệ ポーレットh3 / ハチロクh2 / h5 / ふかみh3 / 日々姫h6 2082): 5 dòng (996, 1001, 1004, 1009, 1059).
- んふ → "Nfu"/"Nfuu" ("Ưm" mất phụ âm f, tiền lệ ハチロクh1 1219/1229, kisaki-h3 2207, ハチロクh2/h5, ふかみh2 999): 4 dòng (1004, 1019, 1065, 1084).
- Mất phụ âm mora khác: 6 dòng — 970 あうっ→"Au", 1003 ふやっ→"Fuya" + んくう…→"Nkuuuuuuuuu", 1022 ふえっ→"Fue", 1039 ぷはっ→"Puha", 1041 くっ→"Hự", 1044 かはっ→"Kaha".
- Rên dài đếm lại đúng số nguyên âm (công thức mora): 2 dòng (1003: 9 u; 1019: Nfuu 2u / Nuuu 3u / Kufuun 3u).

## §2. Sweep — đã kiểm chứng trực tiếp, không đụng

Sweep có 6 mục cho file này (1011, 1230, 1231, 1232, 1237, 1670) — cả 6 đều đúng, audit đã nhận nguyên (Ư gasp). **Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào** (file này không có dòng "Kh"). 4 dòng gasp audit tìm thêm ngoài sweep (792, 1051, 1056, 1222) cũng không đụng. 0 trùng key moan với sweep ngoài các dòng trên.

## §3. Các dòng đổi (16)

### 3.1 key 970 — 日々姫 — あうっ → "Au" (kế thừa fix audit)
- JP: 「来たっ！　きてるっ――あうっ――んっ――\nあつい、の――精液――おなか――子宮、にっ――」
- TW: 「來了！進來了――啊――嗯――熱熱的――精液――進到肚子――子宮的裡面――」
- VN cũ: 「Đến rồi! Đến rồi——A——Ưm——Nóng quá——Tinh dịch——Bụng——Tử cung, đang——」
- VN sửa: 「Đến rồi! Đến rồi——Au——Ưm——Nóng quá——Tinh dịch——Bụng——Vào trong tử cung——」
- Lý do: あうっ = 2 mora (a+u) — "A" chỉ diễn 1, mất u (tiền lệ paulette-h2 937, lr-hachiroku-h2 1432, paulette-h7, lr-nagih1 1249). Giá trị sửa XÂY TRÊN fix nghĩa của audit ("Tử cung, đang——" → "Vào trong tử cung——" đã đúng, giữ nguyên) — khi áp dụng dùng giá trị JSON này (đã gồm cả hai), không áp riêng bản audit (tiền lệ ふかみh3 F7, ハチロクh2 964/974/976). Đây là key audit duy nhất bị đụng trong file này.

### 3.2 key 996 — 日々姫 — やっ → "Ya"
- JP: 「やっ――あっ――にぃにに――ンッ――\nぺろぺろ――ちゅっちゅ――されて――私っ」
- TW: 「呀――啊――阿哥――嗯――這麼舔――我」
- VN cũ: 「Á——A——Bị anh hai——Ưm——Liếm láp——Mút mát——Thế này——Em.」
- VN sửa: 「Ya——A——Bị anh hai——Ưm——Liếm láp——Mút mát——Thế này——Em.」
- Lý do: やっ → "Ya" ("Á" mất phụ âm y — tiền lệ ポーレットh3 "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm). Các token còn lại giữ: あっ→"A", ンッ→"Ưm", SFX liếm/mút đã diễn đúng.

### 3.3 key 1001 — 日々姫 — やっ → "Ya"
- JP: 「やっ！？　にぃに――パンツの上から――\n広げる、とか――それっ」
- TW: 「呀！？　阿哥――隔著內褲――扒開――這個」
- VN cũ: 「Á!? Anh hai——Cách lớp quần lót——Mà vạch ra, thế này——Đó là.」
- VN sửa: 「Ya!? Anh hai——Cách lớp quần lót——Mà vạch ra, thế này——Đó là.」
- Lý do: như 996.

### 3.4 key 1002 — 日々姫 — きゃっ → "Kya"
- JP: 「きゃっ！？」
- TW: 「呀！？」
- VN cũ: 「Á!?」
- VN sửa: 「Kya!?」
- Lý do: きゃ → romaji "Kya" theo quy tắc họ ひゃ/ひゅ/ひあ/きゃ 21/11 ~11:55 — "Á" làm mất hẳn phụ âm ky-.

### 3.5 key 1003 — 日々姫 — ふやっ → "Fuya"; んくううううううううっ → "Nkuuuuuuuuu" (9 u)
- JP: 「ふやっ！？　あっ――んくううううううううっ！！！」
- TW: 「呀！？啊――嗯啊――！！！」
- VN cũ: 「Hya!? A——Ưmmmmmmmm!!!」
- VN sửa: 「Fuya!? A——Nkuuuuuuuuu!!!」
- Lý do: ふやっ → "Fuya" — bản cũ "Hya" SAI HẲN ÂM (ふや = fuya, không phải hya; mất fu-, đổi âm). Tiền lệ ハチロクh5 1064/1065 (ふやっ→"Fuya"). んくううううううううっ: đếm bằng máy う×8 → "Nkuuuuuuuuu" (n + k + 9u: く=1u + う×8), bản cũ "Ưmmmmmmmm" mất hẳn "ku". Tiền lệ ハチロクh1 1238 (んくう→"Nkuu"). あっ→"A" giữ.

### 3.6 key 1004 — 日々姫 — やっ → "Ya"; んふ―― → "Nfu"
- JP: 「やっ！？　んっ――あっ――もっと――おねがいっ！\nにぃにっ――服っ――じゃまっ――んふ――んっ」
- TW: 「呀！？嗯――啊――繼續――拜託了！阿哥――衣服――好礙事――嗯――嗯」
- VN cũ: 「Á!? Ưm——A——Nữa đi——Xin anh! Anh hai——Quần áo——Vướng quá——Ưm——Ưm.」
- VN sửa: 「Ya!? Ưm——A——Nữa đi——Xin anh! Anh hai——Quần áo——Vướng quá——Nfu——Ưm.」
- Lý do: やっ→"Ya" (như 996). んふ――→"Nfu": んふ là một hơi duy nhất (n+fu), "Ưm" mất hẳn f (tiền lệ ハチロクh5 995 んふっ→"Nfu", ハチロクh1 1219/1229, kisaki-h3 2207). Token cuối んっ→"Ưm" giữ — hai âm khác nhau nay diễn khác nhau. (Ghi chú: cờ F2 của ふかみh3 từng để ngỏ một dòng んふっ→"ưm" — nhưng tiền lệ đã gộp ở nhiều file là sửa, nên áp theo đa số.)

### 3.7 key 1007 — 日々姫 — きゃっ → "Kya"
- JP: 「きゃっ！？　ベロっ――んっ――ちょく、だと――\nあっ――ぬらって――これっ――すごく――いいっ」
- TW: 「呀！？舌頭――嗯――直接――啊――軟軟的――這樣――好刺激」
- VN cũ: 「Á!? Lưỡi——Ưm——Chạm trực tiếp, thế này——A——Ướt át quá——Thế này——Sướng——Quá.」
- VN sửa: 「Kya!? Lưỡi——Ưm——Chạm trực tiếp, thế này——A——Ướt át quá——Thế này——Sướng——Quá.」
- Lý do: như 1002.

### 3.8 key 1009 — 日々姫 — やっ → "Ya"
- JP: 「やっ！？　おへそ――までっ――」
- TW: 「呀！？連肚臍――都舔到――」
- VN cũ: 「Á!? Cả rốn——Nữa sao——」
- VN sửa: 「Ya!? Cả rốn——Nữa sao——」
- Lý do: như 996.

### 3.9 key 1019 — 日々姫 — んふうっ → "Nfuu"; ひゃっ → "Hya"; んうううっ → "Nuuu"; くふうんっ → "Kufuun"
- JP: 「んふうっ！？　ひゃっ！？　んうううっ！！？\nにぃにっ――つよ、すぎっ――くふうんっ！」
- TW: 「呼！？　呀！？　嗯！！？阿哥――力道太大了――啊！」
- VN cũ: 「Ưm!? Á!? Ưmmm!!? Anh hai——Mạnh, quá——Ưm!」
- VN sửa: 「Nfuu!? Hya!? Nuuu!!? Anh hai——Mạnh, quá——Kufuun!」
- Lý do: cả 4 tiếng rên trong dòng đều bị nuốt mất phụ âm/nguyên âm: んふうっ = n+f+2u ("Ưm" mất f — tiền lệ ハチロクh5 1074 んふうっ→"Nfuu"); ひゃっ→"Hya" (quy tắc họ hya); んうううっ = n+3u ("Ưmmm" mất hẳn u — đếm bằng máy う×3); くふうんっ = ku+fu+u+n ("Ưm" mất hẳn kufu — tiền lệ ハチロクh1 1241 くふううううん→"Kufuuuuun"). "Mạnh, quá" cho つよ、すぎっ giữ (diễn nghĩa đúng).

### 3.10 key 1022 — 日々姫 — ふえっ → "Fue"
- JP: 「ふえっ！？　あっ――んっ――\nなか――ひあっ――めくれ――てっ――んっ！！」
- TW: 「哎！？啊――嗯――裡面――呀――被蹭到――啊――嗯！！」
- VN cũ: 「Hưa!? A——Ưm——Bên trong——Hia——Bị cọ xát——Rồi——Ưm!!」
- VN sửa: 「Fue!? A——Ưm——Bên trong——Hia——Bị cọ xát——Rồi——Ưm!!」
- Lý do: ふえっ nằm ĐẦU CHUỖI RÊN (tiếp nối あっ――んっ――ひあっ――), không phải thán từ ngạc nhiên độc lập — romaji "Fue" (tiền lệ lr-mikuro-h1 1708/1716/1758, lr-nagih1 1195, lr-reinah1; "Huê"/"Hưa" sai phụ âm đầu h ≠ f, ふ là f). Các tiền lệ giữ "Hả"/"Hể"/"Huể" (lr-nagifukami-h1, lr-hiyoko, lr-hachiroku-h2) đều là thán từ "huh?" độc lập, không áp vào đây. ひあっ→"Hia" đã đúng, giữ. (Xem cờ F4.)

### 3.11 key 1039 — 日々姫 — ぷはっ → "Puha"
- JP: 「むっ――むうう～～っ――んっ――ちゅううっ――\nじゅるるっ――れろっ――ぷはっ――むぅぅ～～～」
- TW: 「唔――唔～～――嗯――啾――啾噗――啾嚕――呼――唔～～～」
- VN cũ: 「Ưm——Ưm~~——Ưm——Chụt——Chụt chụt——Liếm——Phù——Ưm~~~」
- VN sửa: 「Ưm——Ưm~~——Ưm——Chụt——Chụt chụt——Liếm——Puha——Ưm~~~」
- Lý do: ぷはっ = pu+ha+っ — bản cũ "Phù" chỉ giữ ぷ, mất hẳn は (TW 噗哈 xác nhận pu+ha). Romaji "Puha" (tiền lệ ふかみh2 1032, reinah2). Các token còn lại giữ: むっ/むうう/むぅぅ→"Ưm" (âm mũi, quy ước đã chốt), ちゅううっ/じゅるるっ/れろっ đã diễn SFX đúng.

### 3.12 key 1041 — 日々姫 — くっ → "Hự"
- JP: 「はっ――あっ――くっ――」
- TW: 「啊――啊――呃――」
- VN cũ: 「Hơ——A——Ư——」
- VN sửa: 「Hơ——A——Hự——」
- Lý do: くっ → "Hự" theo QUY ƯỚC TRONG FILE (くっ→"Hự"/"hự" ×3: 1043, 1044, 1062) — "Ư" là tiếng gasp, không phải tiếng nghẹn ku (tiền lệ lr-fukamih2 1195, 凪ふかみh1 1232). Câu hỏi mở toàn dự án "Ku" (rên) vs "Hự" (grunt) vẫn còn (ハチロクh2 F2 / h5 F2 / h6 F1) — xem cờ F1; file này áp "Hự" để nhất quán nội bộ.

### 3.13 key 1044 — 日々姫 — かはっ → "Kaha"
- JP: 「かはっ――んっ――ん、くっ――」
- TW: 「啊――嗯――嗯、呃――」
- VN cũ: 「A——Ưm——Ưm, hự——」
- VN sửa: 「Kaha——Ưm——Ưm, hự——」
- Lý do: かはっ = ka+ha — "A" mất hẳn "ka" (tiền lệ ハチロクh5 1181, paulette-h4, paulette-h6 1348). んっ→"Ưm", くっ→"hự" giữ (quy ước file, xem 1041).

### 3.14 key 1059 — 日々姫 — やっ → "Ya" (giữ "Phù" cho ふあっ — chờ unification)
- JP: 「んっ――ふあっ――やっ――しゅごっ――んっ――\nにいにっ――おちん、ちんっ――なかで――ぷく、って」
- TW: 「嗯――呼――呀――好厲害――嗯――阿哥的――雞雞――在裡面――漲了起來」
- VN cũ: 「Ưm——Phù——Á——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」
- VN sửa: 「Ưm——Phù——Ya——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」
- Lý do: chỉ đổi token やっ→"Ya" (như 996). Token ふあっ→"Phù" GIỮ NGUYÊN — audit đã cờ cho đợt unification (→"phùa", xem cờ F2); đợt unification sẽ đổi token đó sau, parent đối chiếu khi gộp.

### 3.15 key 1065 — 日々姫 — んふっ → "Nfu"
- JP: 「んふっ――ちゅっ――ぺろっ――ちゅるっ――ぺろおっ\n――れろれろ――れるーーーっっ――――――ぱくっ！」
- TW: 「嗯――啾――啾嚕――哧溜――吸溜――啾嚕――啾嚕――（咬住）！」
- VN cũ: 「Ưm——Chụt——Liếm——Chụt——Liếm——Liếm liếm——Liếmmm————Ngoạm!」
- VN sửa: 「Nfu——Chụt——Liếm——Chụt——Liếm——Liếm liếm——Liếmmm————Ngoạm!」
- Lý do: như 1004 (んふっ một hơi, "Ưm" mất f). Các SFX hôn/liếm/ngoạm giữ nguyên.

### 3.16 key 1084 — 日々姫 — んふっ → "Nfu"
- JP: 「んふっ！！！」
- TW: 「嗯！！！」
- VN cũ: 「Ưm!!!」
- VN sửa: 「Nfu!!!」
- Lý do: như 1065 — cả dòng chỉ là một tiếng rên んふっ, "Ưm" mất f.

## §4. Giữ nguyên — các tiếng rên đã đúng (ghi chú những dòng đáng chú ý)

- **Họ hya đã romaji đúng, giữ:** 998 ひゃうっ→"Hyau!", 999 ひゃうんっ→"Hyaun!!!", 1014 んひゅっ→"Nhyu!!?", 1022 ひあっ→"Hia".
- **fa/fu đã romaji đúng, giữ:** 1050 ふあああああああああああんっ→"Fuaaaaaaaaaaan!!!" (đếm bằng máy あ×11, đúng 11 a).
- **Rên ngắn đã diễn đúng, giữ:** 1010/1052 くあっ→"Kua!", 1016 くぁ――→"Kua——", 1042 うあっ→"Ua", 1191 うぁっ→"Ua", 1012 ふっ――→"Phù——" (hơi thở), 1067 ん……ふっ――→"Ưm... Phù——" (hai âm riêng), 1013 はっ→"Hơ", ひっ→"Hi", んっ→"Ưm", あっ→"A".
- **んっ/むっ → "Ưm", giữ toàn bộ:** む là âm mũi như ん (quy ước đã chốt) — 1061, 1062, 1039, 1057, 1083, 1084 (trừ token んふ đã sửa).
- **SFX hôn/liếm/mút đã diễn đúng, giữ:** 1055, 1056 (chỉ gasp Ư của audit), 1061, 1065 (trừ token んふ đã sửa), 1072–1075.
- **SFX hành động trong ngoặc đơn (1862–1915, 39 dòng), giữ toàn bộ:** đã diễn thành tiếng Việt (Chụt/Ngoạm/Phụt/Bạch/Phập/Liếm/Nắn/Xoa...); độ dài đã truyền qua lặp chữ (1892 う×9 ↔ "Phậppppppppp" 9 p; 1903 お×6 ↔ "Liếmmmmmm" 6 m; 1873 う×5 ↔ "Liếmmmmmm").
- **Thán từ / đồng ý / nói lắp, giữ:** 967 ううん→"Không", 1020 え……へ、へ→"E... hê, hê." (cười khúc khích), 1025 ふぇ？→"Hả?" (audit cờ F4 — thán từ ngạc nhiên tự nhiên), 1066/1070/1072/1073/1075/1082/1083 うん→"Vâng", 1093 うむ？→"Hửm?", 1182 いーち、にぃ→"Mộttttt, haiiii.", 799 やったぁ→"Tuyệt quá." (reo vui, không phải rên).
- **1040 んーーーーーっ → "Ưm—————", giữ:** độ dài đã truyền qua 5 gạch ngang đối ứng ー×5 của JP; không có tiền lệ đã gộp nào cho romaji "Nnnnnn" — xem cờ F5.
- **1013/1017/1018 ふあっ/ふぁ → "Phù", giữ (chờ unification):** audit đã cờ 4 dòng (1013, 1017, 1018, 1059) cho đợt unification (→"phùa"/"phà" theo dạng khóa) — xem cờ F2. 1018 dạng tách "Phù... a" cũng sẽ được xử lý cùng đợt đó.
- **Gasp Ư của audit, giữ:** 792, 1011, 1051, 1056, 1222, 1230, 1231, 1232, 1237, 1670 — đã sửa đúng, không đụng.
- **1049 「っ」→"A.", giữ** (âm đã diễn — audit §3).
- **Các dòng có やっ/きゃ nhưng KHÔNG phải rên, giữ:** 972 やっていい (động từ やる), 1791 しなきゃいけない (しなきゃ), 799 やったぁ (reo vui).

## §5. Cờ (không tự quyết — ghi để parent / đợt thống nhất xử lý)

- **F1 — くっ "Hự" vs "Ku" (câu hỏi mở toàn dự án):** file này áp "Hự" cho 1041 theo quy ước nội bộ (1043/1044/1062). Tiền lệ ngược: ふかみh3 áp "Ku" cho くっ trong chuỗi rên (tiền lệ paulette-h5). Ranh giới rên-vs-grunt vẫn chờ parent/đợt thống nhất quyết (ハチロクh2 F2 / h5 F2 / h6 F1).
- **F2 — fa/fu "Phù" → unification (1013, 1017, 1018, 1059):** audit đã cờ, dạng khóa ふあ→"phùa", ふぁ→"phà". File này KHÔNG đổi các token đó (chỉ đổi token やっ ở 1059). Đợt unification sẽ quyết romaji-vs-VN cho từng dòng theo quy tắc 21/11 ~01:56.
- **F3 — 1015 nói ngọng khi thè lưỡi, giữ nguyên toàn dòng:** 「ふえっ――ふっ――やっ――ほれッ――ふっ――ろふろふ――ひへっ――ひほひ――いひっ」→"Hưa——Phù——Á——Kìa——Phù——Lêu lêu——Hihe——Hihohi——Ihi." — lời nói ngọng (garbled speech) KHÔNG phải dòng rên theo quy tắc 3b — để audit (audit đã cờ F5). Kể cả token やっ→"Á" trong dòng này cũng không đổi.
- **F4 — 1022 ふえっ→"Fue" (phán đoán của vòng này):** áp romaji vì ふえっ nằm đầu chuỗi rên, khác các tiền lệ giữ "Hả"/"Hể" cho thán từ ngạc nhiên độc lập. Parent xem lại khi gộp.
- **F5 — 1040 んーーーーーっ → "Ưm—————" (giữ):** chưa có tiền lệ romaji cho chuỗi んー dài; nếu parent muốn chuẩn "Nnnnnn" thì đổi ở đợt thống nhất.
- **F6 — 970 kế thừa fix audit:** giá trị JSON này đã gồm cả fix nghĩa audit + token moan. Khi áp dụng: dùng giá trị JSON này, KHÔNG áp riêng bản audit cho key 970 (tránh ghi đè token "Au").

## §6. Lượt soát 2 + kiểm chứng máy

- Lượt soát 2 (đọc lại toàn bộ 16 fix đối chiếu JP, từng token): **16 / 16 / 0 / 0** (tổng / xác minh lại / loại bỏ / sửa đổi).
- Kiểm chứng máy: JSON 16 mục, khóa là chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối **16/16**; khối TOML parse được (tomllib), 16 khóa, **0 sai lệch giá trị** so với JSON; mỗi fix chỉ khác VN cũ ở đúng vùng thay đổi mục tiêu (kiểm tra bằng diff — 15 fix là thay token rên duy nhất; 970 là 2 vùng: token "Au" + vùng nghĩa đã kế thừa từ audit).
- Ghi chú kiểm chứng: lúc ráp JSON, kiểm tra diff phát hiện cả 16 giá trị fix nháp bị thiếu ngoặc 「」 (lỗi chép tay khi ráp, cùng bẫy như audit §5) — đã bổ sung lại cho khớp VN cũ trước khi chốt; các giá trị cuối cùng trong JSON + khối TOML đều đã khớp máy 16/16.
- Đếm nguyên âm bằng máy: 1003 んくう… (う×8) → "Nkuuuuuuuuu" (9 u); 1019 んふうっ (2 u), んうううっ (3 u), くふうんっ (3 u); 1050 あ×11 đã đúng, giữ.

## Khối TOML (đã kiểm chứng parse)

```toml
"970" = "「Đến rồi! Đến rồi——Au——Ưm——Nóng quá——Tinh dịch——Bụng——Vào trong tử cung——」"
"996" = "「Ya——A——Bị anh hai——Ưm——Liếm láp——Mút mát——Thế này——Em.」"
"1001" = "「Ya!? Anh hai——Cách lớp quần lót——Mà vạch ra, thế này——Đó là.」"
"1002" = "「Kya!?」"
"1003" = "「Fuya!? A——Nkuuuuuuuuu!!!」"
"1004" = "「Ya!? Ưm——A——Nữa đi——Xin anh! Anh hai——Quần áo——Vướng quá——Nfu——Ưm.」"
"1007" = "「Kya!? Lưỡi——Ưm——Chạm trực tiếp, thế này——A——Ướt át quá——Thế này——Sướng——Quá.」"
"1009" = "「Ya!? Cả rốn——Nữa sao——」"
"1019" = "「Nfuu!? Hya!? Nuuu!!? Anh hai——Mạnh, quá——Kufuun!」"
"1022" = "「Fue!? A——Ưm——Bên trong——Hia——Bị cọ xát——Rồi——Ưm!!」"
"1039" = "「Ưm——Ưm~~——Ưm——Chụt——Chụt chụt——Liếm——Puha——Ưm~~~」"
"1041" = "「Hơ——A——Hự——」"
"1044" = "「Kaha——Ưm——Ưm, hự——」"
"1059" = "「Ưm——Phù——Ya——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」"
"1065" = "「Nfu——Chụt——Liếm——Chụt——Liếm——Liếm liếm——Liếmmm————Ngoạm!」"
"1084" = "「Nfu!!!」"
```

## Kết bài

File 日々姫h1_マッサージの続き: đọc 329/329 dòng, xét 147 dòng rên/SFX, **đổi 16 dòng (moan)** — họ hya 3, やっ→Ya 5, んふ→Nfu 4, mất phụ âm mora khác 6 (chồng lấn), rên dài đếm lại 2. Giữ 131 dòng rên/SFX (họ hya đã romaji đúng, 1050 đếm đúng 11 a, SFX 39 dòng đã diễn đúng, gasp Ư của audit đầy đủ). Không đụng gasp Ư hay dòng "Kh". Cờ cho parent/đợt thống nhất: F1 くっ "Hự" vs "Ku" (câu hỏi mở toàn dự án); F2 fa/fu "Phù" 4 dòng → unification; F3 dòng nói ngọng 1015; F4 phán đoán ふえっ→"Fue" ở 1022; F5 giữ "Ưm—————" ở 1040; F6 key 970 kế thừa fix audit. Lượt soát 2: 16/16/0/0. Khối TOML 16 khóa parse OK, 0 sai lệch.
