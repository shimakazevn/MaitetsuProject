# Audit — れいなh2_おもらし防止大作戦.txt.toml

- File: `れいなh2_おもらし防止大作戦.txt.toml` — route 04_Reina, 284 dòng script (87 thoại Reina, 49 thoại Soutetsu, 148 độc thoại).
- Nội dung: Reina xin đặc huấn chống tè dầm — (1) nhịn tè khi sướng, (2) đặc huấn miệng để nuốt ực không nhả ra, (3) làm tình đàng hoàng như người lớn. Mặc đồng phục theo gợi ý của Paulette (để Soutetsu vui), ôm thú bông KiHa 07 làm bùa hộ mệnh; Soutetsu đặc huấn cho cô bé suốt đêm, kết bằng việc cả hai khắc sâu "bốn chữ" おもらし vào lòng.
- **Kết quả: 23/284 dòng sai (8,1%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (284 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML tuyệt đối 284/284 (0 lệch thực chất — 165 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng.
- Thẻ `%l`: file này KHÔNG có thẻ `%l` nào trong JP lẫn VN — không có thẻ sai định dạng, không có thẻ VN tự thêm.
- TOML md5 `141739546028af97fdbac1c3ffe9ab6e`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Soutetsu "anh" với Reina đúng toàn file (1098 "anh hiểu rồi", 1195 "cơ thể anh", 999/1162 "anh"…); không có dòng nào Soutetsu tự xưng "tôi" sai đối tượng (quét máy: 0 dòng 双鉄H chứa "tôi"). Reina gọi "anh Soutetsu" nhất quán; Soutetsu gọi Reina "em" đúng (981, 983, 988, 1204). "chị Paulette" ở 1145/1146 khớp cách gọi đã dùng trong toàn route 04_Reina (34 dòng trong CSV3).
- Thuật ngữ: "KiHa 07" đúng chính tả (983); 先走り汁 → "dịch nhờn (trước khi xuất tinh)" nhất quán (1015, 1195, 1389); れいななくん → "bé số 07" nhất quán (1035, 1137, 1141, 1487). Không có dòng nào dùng Ohito/Yui/Migita/Teitetsu nên không có gì chờ đợt thống nhất trong file này.

## §2. Danh sách sửa (23 dòng)

Phân loại: gasp 4 (1031, 1070, 1071, 1215 — cả 4 từ sweep), fa/fu 14 (1001, 1027, 1036, 1052, 1061, 1065, 1081, 1114, 1174, 1180, 1182, 1183, 1184, 1185), SFX cười 2 (1104, 1108), bịa thêm 2 (1118, 1628), sai nghĩa 1 (1465).

### 1001 — Reina — fa/fu
- JP: 「ひゃっ――あっ――んっ――んんっ――ふあっ――\nやっ――したっ――ぬりゅう、って――ふあ――あっ」
- TW: 「呀啊……啊、嗯……啊嗯……蛤啊……啊嗯……下面……變濕了……啊啊啊」
- VN cũ: 「Hya——a——ưm——ưm——ha——\nÁ——bên dưới——nhầy nhụa, rồi——ha——a」
- Sửa: 「Hya——a——ưm——ưm——phùa——\nÁ——bên dưới——nhầy nhụa, rồi——phùa——a」
- Lý do: JP ふあっ / ふあ―― (2 lần): quy tắc fa/fu đã chốt — ふあ→"phùa" (tiền lệ ふかみh3: 2278, 2338, 2346, 2352). VN cũ "ha" làm mất phụ âm f.

### 1027 — Reina — fa/fu
- JP: 「はっ――んっ――ふあッ――んっ――\nもっと――もっと――ね、そうてつ――さぁ、んっ――」
- TW: 「哈嗯……啊嗯……繼續……繼續嘛，雙鐵先生……」
- VN cũ: 「Ha——ưm——ha——ưm——\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」
- Sửa: 「Ha——ưm——phùa——ưm——\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」
- Lý do: JP ふあッ: ふあ→"phùa" theo quy tắc fa/fu đã chốt (tiền lệ ふかみh3). VN cũ "ha" làm mất phụ âm f.

### 1031 — Soutetsu — gasp っ
- JP: 「っ！」
- TW: 「唔！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep (lost-gasp-whole): JP 「っ！」 là gasp nguyên dòng; VN chỉ còn dấu "!" — áp nguyên giá trị sweep "Ư!" (đã kiểm chứng với JP).

### 1036 — Reina — fa/fu
- JP: 「あ――ふあっ――」
- TW: 「啊……蛤啊……」
- VN cũ: 「A——ha——」
- Sửa: 「A——phùa——」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "ha" làm mất phụ âm f.

### 1052 — Reina — fa/fu
- JP: 「ひゃん――んっ――わきばら――くすぐったいで――\nふあっ――んっ！」
- TW: 「啊嗯……嗯……側腹好癢哦……蛤啊……嗯！」
- VN cũ: 「Hyan——ưm——mạn sườn——nhột quá——\nHa——ưm!」
- Sửa: 「Hyan——ưm——mạn sườn——nhột quá——\nPhùa——ưm!」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "Ha" làm mất phụ âm f.

### 1061 — Reina — fa/fu
- JP: 「ひあっ！　あっ！　あうっ――ふあっ――\nそうてつ、さんっ――そうてつ、さぁんっ！」
- TW: 「啊嗯！啊、啊、啊啊啊……雙鐵先生……雙鐵先生！」
- VN cũ: 「Hya! A! Au——ha——\nAnh Soutetsu——anh Soutetsu!」
- Sửa: 「Hya! A! Au——phùa——\nAnh Soutetsu——anh Soutetsu!」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "ha" làm mất phụ âm f.

### 1065 — Reina — fa/fu
- JP: 「ひゃっ！　あっ――おなか――めくれっ――るっ！――\nふあっ――ささる――の――ふかいっ――ふか、くてっ」
- TW: 「啊嗯！在肚子裡……插來插去……蛤啊……插得……好深……好深」
- VN cũ: 「Hya! A——bụng——như bị lộn ngược——ra!——\nHa——đâm vào——sâu——sâu, quá」
- Sửa: 「Hya! A——bụng——như bị lộn ngược——ra!——\nPhùa——đâm vào——sâu——sâu, quá」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "Ha" làm mất phụ âm f.

### 1070 — Soutetsu — gasp っ
- JP: 「っ！」
- TW: 「啊！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep (lost-gasp-whole): JP 「っ！」 là gasp nguyên dòng; VN chỉ còn dấu "!" — áp nguyên giá trị sweep "Ư!" (đã kiểm chứng với JP).

### 1071 — Soutetsu — gasp っ
- JP: 「っ！！」
- TW: 「啊！！」
- VN cũ: 「!!」
- Sửa: 「Ư!!」
- Lý do: Sweep (lost-gasp-whole): JP 「っ！！」 là gasp nguyên dòng; VN chỉ còn "!!" — áp nguyên giá trị sweep "Ư!!" (đã kiểm chứng với JP).

### 1081 — Reina — fa/fu
- JP: 「ふぁっ――あ――ちゅっ！――ちゅうう――ちゅっ――\nれるっ――れりゅ――ちゅっ――ちゅうう――ちゅっ！」
- TW: 「啾、啾、啾……噗啾！啾、啾嚕……啾、啾嚕！」
- VN cũ: 「Ha——a——chụt!——chụt——chụt——\nChụt——chụt——chụt——chụt——chụt!」
- Sửa: 「Phà——a——chụt!——chụt——chụt——\nChụt——chụt——chụt——chụt——chụt!」
- Lý do: JP ふぁっ: ふぁ→"phà" theo quy tắc fa/fu đã chốt (tiền lệ ふかみh3: 2301, 2345, 2358). VN cũ "Ha" làm mất phụ âm f.

### 1104 — Reina — SFX (cười)
- JP: 「ふふ～っ、ふふぅっへひへひはひはへー\nひふへほひーれふよ？　ほーへふふぁん」
- TW: 「嘿嘿……這樣子舒服吧……啾嚕嚕……」
- VN cũ: 「Ư hu hu~, sướng chứ ạ~\nchụt chụt chụt」
- Sửa: 「Fufu~, sướng chứ ạ~\nchụt chụt chụt」
- Lý do: JP ふふ～っ là TIẾNG CƯỜI, không phải tiếng rên — quy tắc Hieu 19/11: cười diễn thành cười (Paulette "Fufu"), không diễn thành tiếng rên/khóc. VN cũ "Ư hu hu~" nghe như khóc/rên; TW 嘿嘿 khớp "Fufu". Phần nói ngọng (miệng đang ngậm) giữ nguyên theo TW.

### 1108 — Reina — SFX (cười)
- JP: 「うふふぅ、ですよねぇ。そうてつさんのズボンの前も、\nそういうふうに言ってますよぉ？」
- TW: 「嘿嘿，是呀。你的下身也是這麼說的哦」
- VN cũ: 「Ư hu hu~, đúng không ạ. Phía trước quần của anh Soutetsu,\ncũng đang nói như vậy đó nha~?」
- Sửa: 「Ufufu~, đúng không ạ. Phía trước quần của anh Soutetsu,\ncũng đang nói như vậy đó nha~?」
- Lý do: JP うふふぉ là TIẾNG CƯỜI — như 1104: VN cũ "Ư hu hu~" diễn cười thành rên/khóc; sửa thành "Ufufu~" theo quy tắc Hieu 19/11.

### 1114 — Reina — fa/fu
- JP: 「ひゃいれふぅ――んッ――れろおおおおおおっ――\nんむっ――ぷあっ！　ぷはっ！　はぁっ……はぁっ」
- TW: 「好的……嗯……啾嚕嚕嚕……嗯……噗哈！蛤啊、蛤啊……」
- VN cũ: 「Vâng ạ——ưm——chụt——\nƯm——phù! Phù! Ha……ha」
- Sửa: 「Vâng ạ——ưm——chụt——\nƯm——phùa! Phù! Ha……ha」
- Lý do: JP ぷあっ: ぷあ→"phùa" (tiền lệ ふかみh3 key 2351: ぷあっ→"phùa"). VN cũ "phù" làm mất nguyên âm a. ぷはっ→"Phù" giữ nguyên (không thuộc quy tắc fa/fu).

### 1118 — Reina — bịa thêm
- JP: 「はいですぅ。れいな、がんばります――よ、ぉ」
- TW: 「好的，玲奈會加油的……嗯」
- VN cũ: 「Vâng ạ~. Reina, sẽ cố gắng——ạ~, ưm」
- Sửa: 「Vâng ạ~. Reina, sẽ cố gắng——đấy ạ~」
- Lý do: JP がんばります――よ、ぉ: よ、ぉ chỉ là tiểu từ nhấn mạnh kéo dài, không có âm rên nào. VN cũ thêm "ưm" không có cơ sở JP — gỡ, giữ "đấy ạ~" diễn ý nhấn mạnh.

### 1174 — Reina — fa/fu
- JP: 「おもいっきり――おもいっきり――ふあっ――\nそうてつ、さんの――おもい、きり――」
- TW: 「盡情……盡情地……蛤啊……雙鐵先生……盡情地……」
- VN cũ: 「Mạnh bạo——mạnh bạo——ha——\ncủa anh, Soutetsu——mạnh, bạo——」
- Sửa: 「Mạnh bạo——mạnh bạo——phùa——\ncủa anh, Soutetsu——mạnh, bạo——」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "ha" làm mất phụ âm f.

### 1180 — Reina — fa/fu
- JP: 「ひゃっ――あっ――ふあっ――あっ――おまた――\nきもち――いい――です、よぉっ――んうっ」
- TW: 「蛤啊……啊……蛤啊啊……下面……好舒服……啊嗯」
- VN cũ: 「Hya——a——ha——a——bên dưới——\nsướng——quá——ạ~——ưm」
- Sửa: 「Hya——a——phùa——a——bên dưới——\nsướng——quá——ạ~——ưm」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "ha" làm mất phụ âm f.

### 1182 — Soutetsu — fa/fu
- JP: 「ぷあっ――あっ――れいな。いいか？」
- TW: 「蛤啊……玲奈，可以嗎？」
- VN cũ: 「Phù——a——Reina. Được chứ?」
- Sửa: 「Phùa——a——Reina. Được chứ?」
- Lý do: JP ぷあっ: ぷあ→"phùa" (tiền lệ ふかみh3 key 2351). VN cũ "Phù" làm mất nguyên âm a.

### 1183 — Reina — fa/fu
- JP: 「ふぇっ――ふあっ――はっ――はぅぅ――」
- TW: 「蛤啊……蛤啊……」
- VN cũ: 「Fe——ha——ha——hau——」
- Sửa: 「Phuê——phùa——ha——hau——」
- Lý do: JP ふぇっ――ふあっ: ふぇ→"phuê" theo quy tắc đã chốt, KHÔNG romanisation (VN cũ "Fe"); ふあ→"phùa". はっ→"ha", はぅぅ→"hau" giữ nguyên.

### 1184 — Reina — fa/fu
- JP: 「ふあっ――あっ――おっぱい――――んっ――ふっ」
- TW: 「蛤啊、啊……胸部……啊嗯」
- VN cũ: 「Ha——a——ngực————ưm——phù」
- Sửa: 「Phùa——a——ngực————ưm——phù」
- Lý do: JP ふあっ: ふあ→"phùa" theo quy tắc fa/fu đã chốt. VN cũ "Ha" làm mất phụ âm f.

### 1185 — Reina — fa/fu
- JP: 「ふぁっ――はあっ――あっ――ふぁぁっ――」
- TW: 「蛤啊、蛤啊、啊啊啊啊」
- VN cũ: 「Ha——ha——a——ha——」
- Sửa: 「Phà——ha——a——phàà——」
- Lý do: JP ふぁっ――ふぁぁっ: ふぁ→"phà"; ふぁぁっ (kéo dài) →"phàà" (tiền lệ ふかみh1 key 1465: ふああっ→"Phùaa"). VN cũ "Ha" làm mất phụ âm f cả hai chỗ.

### 1215 — Soutetsu — gasp っ
- JP: 「～～～っ！」
- TW: 「～～～唔！」
- VN cũ: 「~~~!」
- Sửa: 「~~~Ư!」
- Lý do: Sweep (lost-gasp-trailing): JP 「～～～っ！」 — gasp っ sau dấu kéo dài; VN giữ dấu ~~~ nhưng bỏ mất gasp — áp nguyên giá trị sweep "~~~Ư!" (đã kiểm chứng với JP).

### 1465 — độc thoại — sai nghĩa
- JP: その四文字を心に刻み、僕らは次なる特訓のため、\n今はともかく――尿処理をする。
- TW: 我們把這四個字刻在心中，為了開始下一次特訓……現在要先把尿液打掃乾淨。
- VN cũ: Khắc sâu câu nói đó vào lòng, để chuẩn bị cho lần đặc huấn tiếp theo,\ntrước mắt thì——chúng tôi dọn dẹp bãi chiến trường.
- Sửa: Khắc sâu bốn chữ ấy vào lòng, để chuẩn bị cho lần đặc huấn tiếp theo,\ntrước mắt thì——chúng tôi dọn dẹp bãi chiến trường.
- Lý do: JP その四文字 = "bốn chữ ấy" (từ おもらし, 4 kana) — chi tiết đếm chữ có chủ ý. VN cũ "câu nói đó" làm mất chi tiết này. Nửa sau (尿処理→"dọn dẹp bãi chiến trường") giữ nguyên: diễn đạt uyển chuyển nhưng đúng nghĩa dọn dẹp.

### 1628 — độc thoại — bịa thêm
- JP: 肉芽と、膣穴の間に小さく、\nぴくぴく震える穴が開いてる。
- TW: 肉芽和小穴之間的小洞不斷抽動，我將其輕輕撐開。
- VN cũ: Giữa hạt ngọc và lỗ âm đạo, có một cái lỗ nhỏ,\nđang giật giật run rẩy, tôi mở nó ra.
- Sửa: Giữa hạt ngọc và lỗ âm đạo, có một cái lỗ nhỏ,\nđang giật giật run rẩy.
- Lý do: JP thắng TW: JP 「肉芽と、膣穴の間に小さく…ぴくぴく震える穴が開いてる。」 không có mệnh đề nào về việc "mở ra" — VN cũ "tôi mở nó ra" theo TW 「我將其輕輕撐開」 là thêm vào, không có cơ sở JP — gỡ.

## §3. Sweep っ-gasp kiểm chứng

- Sweep có đúng 4 mục cho file này (1031, 1070, 1071, 1215) — nhận cả 4, đã kiểm chứng từng giá trị với JP (xem §2).
- Quét máy bổ sung toàn file: các っ còn lại đều đã được diễn (はっ→"Ha", んっ→"ưm", ふっ→"phù", ごくっ→"Ực"…) hoặc là っ ngắt trong tiếng rên đã nén (1045 んうっっ→"ưm", 1094 ん～～～～～～っ→"Ưm~~~~~~", 1186 はっっっ→"Ha") — không còn gasp nào sweep bỏ sót. 1072 「！？」 JP không có âm, VN 「!?" đúng (TW thêm 啊, không theo).
- Lưu ý: 1101 よいしょっ → "hây dô" giữ nguyên (よいしょ là tiếng lấy đà, っ cuối chỉ ngắt — đã diễn đủ).

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- Key 786: すき/しゅき/だいしゅきい → "thích……thích……thích nhất……" — giữ nguyên: tiền lệ ふかみh3 key 2394 giữ しゅき→"thích" (tiếng ngọng cute không có tương đương Việt tự nhiên).
- Key 1043/1093: んむっ → "A ưm" — giữ nguyên (diễn rên ngẫu hứng theo quy tắc Hieu 19/11; âm mũi ん được diễn thành "A ưm" nhất quán trong file).
- Key 1120: ごろーーーーん → "Nằm xuống" — giữ nguyên (diễn âm lăn người thành hành động, đúng nghĩa trong cảnh nằm xuống; cùng dạng 1740 くぱあっ→"Tách ra", 1769 じわあっ→"Rỉ ra").
- Key 1167: TW 捨不得 (tiếc nuối chia xa) vs JP さみしくて (buồn/cô đơn) — VN "buồn bã" theo JP, đúng (JP thắng TW).
- Key 1210: あひゅっ → "a" — giữ nguyên: ひゅ trong chuỗi rên được nén nhất quán trong file (1042 んひゅっ→"Ưm!", 1068 うひゅっ→"Ư").
- Key 1732/1757: ぐり/ぐい → "Phập" — giữ nguyên: trong ngữ cảnh các âm ( ) ở 1730–1744 đều là tiếng đâm/thúc, "Phập" diễn đúng hành động; 1735 ぐりっ→"Ngoáy" là hành động khác (xoay/ngoáy tay).
- Key 1730–1771 (chuỗi SFX trong ngoặc đơn): đã đọc hết — "Phập/Rột/Chụt/Phụt/Bạch" nhất quán với từng nhóm âm; không sửa thêm.
- Key 1158: cột JP có ký tự lỗi `���` (この���ま) — lỗi dữ liệu phía JP, VN "cứ thế này" (このまま) đúng, không tính sai.
- Key 1628: cột JP có ký tự lỗi `��` (小さく��) — lỗi dữ liệu phía JP, không ảnh hưởng phần sửa ở §2. Key 1496: cột TW có ký tự lỗi `���`, JP/VN bình thường.
- Key 1077 あ～～んっ→"A~~", 1002 ひゃあああんっ→"Hyaaaaaan", 1064 ふうううう→"fuuuuu", 1089 ひゅふぅぅ…→"Hyuuuu…": các tiếng rên romanisation (Hya/Kyu/fuu) đã dùng nhất quán toàn dự án (tiền lệ ふかみh2 key 1270 giữ "fuu") — giữ nguyên; điều khoản "không romanisation" trong brief chỉ áp dụng cho nhóm fa/fu (ふぁ/ふあ/ふぇ).

## §5. Khối TOML (đã parse-kiểm chứng: 23 khóa, 0 sai lệch)

```toml
[script]
"1001" = "「Hya——a——ưm——ưm——phùa——\\nÁ——bên dưới——nhầy nhụa, rồi——phùa——a」"
"1027" = "「Ha——ưm——phùa——ưm——\\nNữa đi——nữa đi——nha, anh Soutetsu——ưm——」"
"1031" = "「Ư!」"
"1036" = "「A——phùa——」"
"1052" = "「Hyan——ưm——mạn sườn——nhột quá——\\nPhùa——ưm!」"
"1061" = "「Hya! A! Au——phùa——\\nAnh Soutetsu——anh Soutetsu!」"
"1065" = "「Hya! A——bụng——như bị lộn ngược——ra!——\\nPhùa——đâm vào——sâu——sâu, quá」"
"1070" = "「Ư!」"
"1071" = "「Ư!!」"
"1081" = "「Phà——a——chụt!——chụt——chụt——\\nChụt——chụt——chụt——chụt——chụt!」"
"1104" = "「Fufu~, sướng chứ ạ~\\nchụt chụt chụt」"
"1108" = "「Ufufu~, đúng không ạ. Phía trước quần của anh Soutetsu,\\ncũng đang nói như vậy đó nha~?」"
"1114" = "「Vâng ạ——ưm——chụt——\\nƯm——phùa! Phù! Ha……ha」"
"1118" = "「Vâng ạ~. Reina, sẽ cố gắng——đấy ạ~」"
"1174" = "「Mạnh bạo——mạnh bạo——phùa——\\ncủa anh, Soutetsu——mạnh, bạo——」"
"1180" = "「Hya——a——phùa——a——bên dưới——\\nsướng——quá——ạ~——ưm」"
"1182" = "「Phùa——a——Reina. Được chứ?」"
"1183" = "「Phuê——phùa——ha——hau——」"
"1184" = "「Phùa——a——ngực————ưm——phù」"
"1185" = "「Phà——ha——a——phàà——」"
"1215" = "「~~~Ư!」"
"1465" = "Khắc sâu bốn chữ ấy vào lòng, để chuẩn bị cho lần đặc huấn tiếp theo,\\ntrước mắt thì——chúng tôi dọn dẹp bãi chiến trường."
"1628" = "Giữa hạt ngọc và lỗ âm đạo, có một cái lỗ nhỏ,\\nđang giật giật run rẩy."
```

## §6. Chờ Hieu (không tự quyết)

- Không có mục nào chờ Hieu trong file này: không có thuật ngữ chờ đợt thống nhất (Ohito/Yui/Migita/Teitetsu đều vắng mặt), không có đại từ mơ hồ (người nghe Soutetsu↔Reina rõ toàn file), không có dòng JP dở dang cần Hieu hoàn thiện (1158/1628 chỉ lỗi ký tự hiển thị ở cột JP, VN đã đúng).
- Ghi chú: file này là H-scene dài (148 độc thoại + 136 thoại, phần lớn là tiếng rên/SFX) — tỷ lệ sai 8,1% tập trung gần hết ở nhóm SFX/fa-fu, không có lỗi lệch dòng hay bịa nghĩa lớn.

## Kết bài

File れいなh2_おもらし防止大作戦 đã audit xong toàn bộ 284 dòng: 23 dòng sai (8,1%) — 4 gasp từ sweep, 14 fa/fu (ふあ/ふぁ/ぷあ→"phùa"/"phà", ふぇ→"phuê"), 2 tiếng cười bị diễn thành rên (1104, 1108), 2 bịa thêm (1118, 1628), 1 sai nghĩa (1465). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 23 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 23/23, 0 bỏ, 1 sửa (1118: lượt soát phát hiện fix làm mất ngoặc 「」 của VN cũ, đã khôi phục). Không có mục nào chờ Hieu.
