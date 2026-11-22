# Audit: lr_稀咲h1_おしおきとごほうび.txt.toml — 60/297 (20,2%)

- File: `06_Kisaki/lr_稀咲h1_おしおきとごほうび.txt.toml` (route 06_Kisaki, 297 dòng script; monologue 113, 稀咲 103, 双鉄 81). Nội dung: Kisaki trừng phạt Soutetsu vì say rượu kể bí mật vợ chồng cho Paulette; phần lớn file là H-scene (Kisaki chủ động, Soutetsu bị trói tay, vừa thẩm vấn vừa ân ái).
- TOML md5 `439e80f22d9abfcda5843f8d2f2844ca`, không có bản trùng (chỉ 1 file tên này trong 06_Kisaki; không thuộc nhóm trùng nào); CSV3 1 bộ 297 dòng, key khớp tuyệt đối, VN khớp TOML 297/297, 0 dòng VN trống. [selections] rỗng; 0 tag %l; BOM + CRLF.
- Phân loại (60): gasp 20 (sweep 14 + mới 6), nguyên âm 16, đại từ 13, sai nghĩa 5, SFX 5, chính tả 1.
- Sweep gasp: 17 mục cho file này (14 fix + 3 already-rendered). Áp nguyên văn 9 (1000/1001/1003/1020/1029/1030/1039/1062/1291 — riêng 1062 phải sửa lại dạng `\n`, xem dưới); 5 mục áp nội dung nhưng khôi phục `\n` literal (1341/1425/1429/1551/1619 — sweep dùng dạng TOML làm phẳng, space thay cho `\n`); 1 mục already-rendered SAI (1262 — っ! cuối dòng 1 bị mất, đã sửa); 2 mục already-rendered đúng (1065 ん～～～～～っ→"Ưm~~~~~", 1073 けど――っ→"đấy!"). Quét cơ học toàn bộ dòng JP có っ tìm thêm 6 gasp (710/971/972/974/1235/1262). 1081 là false positive của quét (っていうか — っ đầu từ, không phải gasp).
- Đại từ: Soutetsu "tôi" với Kisaki xuyên suốt, 0 dòng "Anh" sai; Soutetsu→Kisaki "em"→"cô" 5 dòng + 1 trích lời Paulette (1033); Kisaki gọi Soutetsu "cậu"/tên trần, 0 dòng "anh Soutetsu"; Kisaki キミ→"cậu" đúng cả 2 dòng (1099/1107). Kisaki tự xưng: 18 dòng ボク/僕 — 7 dòng chuyển "tôi"→"em" theo quy tắc ngữ cảnh 19:45 (rên/lên đỉnh/thú nhận mềm yếu), 11 dòng giữ "tôi" (ra lệnh/giải thích/trách móc/quyết đoán).
- Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Thẻ %l: 0 lệch. Không còn っ thô trong VN sau fix (1020 là っ thô duy nhất trong file).
- Ghi chú dữ liệu: JP trong CSV3 bị hỏng ký tự ở 1560 (���直 — JP trong TOML sạch là 正直, VN "Thành thật mà nói" dịch đúng, không tính vào số sai); 1425 có 」 thừa cuối dòng (độc thoại không có 「, đã bỏ trong fix); 1568 VN chứa dấu `\"` chỉ là escape của CSV/JSON, TOML sạch.

## Danh sách sửa (60)

### gasp (20)
- **710** 稀咲 — JP 「っ……ぁっ――ふっ――あっ！」: 「……á――phù――á!」 → 「Ư……á――phù――á!」 (っ đầu dòng bị mất).
- **971** 双鉄 — JP 「っ――がっ――グッ――」: 「――gá――gư――」 → 「Ư――gá――gư――」 (っ đầu dòng bị mất).
- **972** 双鉄 — JP 「っ！　はっ！　あっ！　くっっ！！！！」: 「! Há! Á! Kư!!!!」 → 「Ư! Há! Á! Kư!!!!」 (っ! đầu dòng bị mất).
- **974** 双鉄 — JP 「――っ！　くはっ！！」: 「――! Kưha!!」 → 「――Ư! Kưha!!」 (――っ! bị mất).
- **1000** 双鉄 — JP 「～～～～っ！」: 「~~~~!」 → 「~~~~Ư!」 (sweep áp nguyên văn).
- **1001** 双鉄 — JP 「っ！！」: 「!!」 → 「Ư!!」 (sweep).
- **1003** 双鉄 — JP 「～～～～～～～～っ！！！！」: 「~~~~~~~~!!!!」 → 「~~~~~~~~Ư!!!!」 (sweep).
- **1020** 双鉄 — JP 「っっっっっ！？　痛った――――――――」: 「っっっっっ!? Đau quá――――――――」 → 「ƯƯƯƯƯ!? Đau quá――――――――」 (sweep; っ thô duy nhất trong file).
- **1029** 双鉄 — JP 「っ！！」: 「!!」 → 「Ư!!」 (sweep).
- **1030** 双鉄 — JP 「っ！！！」: 「!!!」 → 「Ư!!!」 (sweep).
- **1039** 双鉄 — JP 「っ！？」: 「!?」 → 「Ư!?」 (sweep).
- **1062** 双鉄 — JP 「…鼓動がっ――っっっっっっっ！！！！」: 「…thở không nổi――tim đập nhanh quá――――!!!!」 → 「…thở không nổi――tim đập nhanh quá――――ƯƯƯƯƯƯƯ!!!!」 (sweep, 7 Ư cho 7 っ; đã sửa lại: sweep fix làm phẳng `\n` thành khoảng trắng, khôi phục `\n` literal theo CSV3).
- **1235** 双鉄 — JP 「っ！　稀咲っ――っと！！！？」: 「! Kisaki――ái!!!?」 → 「Ư! Kisaki――ái!!!?」 (っ! đầu dòng bị mất).
- **1262** 稀咲 — JP 「…そうてつっ――っ！」: 「…Soutetsu――!」 → 「…Soutetsu――Ư!」 (sweep ghi already-rendered nhưng っ! cuối dòng 1 bị mất — Ưm ở dòng 2 là của んっ).
- **1291** 稀咲 — JP 「ありがとう、けど――っ！」: 「Cảm ơn nhé, nhưng――!」 → 「Cảm ơn nhé, nhưng――Ư!」 (sweep).
- **1341** monologue — JP 「…脳がぐらぐらゆすられ――っ！」: 「…não bộ bị lắc lư chao đảo――!」 → 「…não bộ bị lắc lư chao đảo――Ư!」 (sweep, khôi phục `\n`).
- **1425** monologue — JP 「…あわてて飲み込み――っ！！！！？」: 「…tôi vội vàng nuốt lại――!!!!?」」 → 「…tôi vội vàng nuốt lại――Ư!!!!?」 (sweep + khôi phục `\n` + bỏ 」 thừa).
- **1429** monologue — JP 「…思い出しっ――っ！！！」: 「…hai tay mình đang bị trói――!!!」 → 「…hai tay mình đang bị trói――Ư!!!」 (sweep, khôi phục `\n`).
- **1551** monologue — JP 「…それしか望めな――っ！」: 「…được xuất tinh một cách sướng nhất――!」 → 「…được xuất tinh một cách sướng nhất――Ư!」 (sweep, khôi phục `\n`).
- **1619** monologue — JP 「…一層強く感じられ――っ！！」: 「…càng thêm mãnh liệt――!!」 → 「…càng thêm mãnh liệt――Ư!!」 (sweep, khôi phục `\n`).

### nguyên âm (16) — đếm bằng máy theo công thức VN = 1 + số う/ぅ
- **1011** 双鉄 — JP ぁぁぁぁあぁああああああっ (12 a): 「A a a a a a a a a a a a á!!!!!」 (13 a) → 「A a a a a a a a a a a á!!!!!」 (12 a).
- **1013** 双鉄 — JP ぁぁああああっ (6 a): 「A a a a á!!?」 (5 a) → 「A a a a a á!!?」 (6 a).
- **1043** 稀咲 — ぢゅうっ = 2 u: 「…Jupa! Juuu!!」 → 「…Jupa! Juu!!」.
- **1045** 稀咲 — ずろおおおおぉぉぉぉぉ = 10 o (1 ろ + 9), ぢゅぶうううう = 6 u: 「…Zuro o×10――――jubuuuu!!!」 → 「…Zuro o×9――――jubuuuuu!!!」.
- **1055** 稀咲 — れりゅうぅぅ = 4 u: 「Reryuuu――…」 → 「Reryuuuu――…」.
- **1057** 稀咲 — れりゅうううっ = 4 u: 「…Reryuuu!…」 → 「…Reryuuuu!…」.
- **1058** 稀咲 — ぢゅうううううっ = 6 u: 「…Juuuuu!…」 → 「…Juuuuuu!…」.
- **1063** 稀咲 — ぃきゅぅ×7う×10 = 18 u: 「Ikyuuuuuuuuuuuuuu!!!」 (14 u) → 「Ikyuuuuuuuuuuuuuuuuuu!!!」 (18 u).
- **1064** 稀咲 — きゅふぅぅぅ = 5 u: 「Kyufuuu!!!!」 → 「Kyufuuuu!!!!」.
- **1703** monologue — ぢゅびゅううぅ×6うぅ×4ぼぢゅん = 16 u: 「（Jubyuuuuuuuuuuuuubojun!）」 (15 u) → 「（Jubyuuuuuuuuuuuuuubojun!）」 (16 u).
- **1704** monologue — ずびょぉ×9 = 10 o: 「（Zubyooooooo! Bujun!!!!）」 (7 o) → 「（Zubyoooooooooo! Bujun!!!!）」 (10 o).
- **1705** monologue — ずぶう×10 = 12 u: 「（Zubuuuuuuuuuu!!! Gochu!!）」 (11 u) → 「（Zubuuuuuuuuuuu!!! Gochu!!）」 (12 u).
- **1706** monologue — ずろお×16 = 17 o: 「（Zuro o×17!!!）」 (18 o) → 「（Zuro o×16!!!）」 (17 o).
- **1707** monologue — じゅぶう×17 = 19 u: 「（Jubuuuuuuuuuuuuuuuuu!!）」 (18 u) → 「（Jubuuuuuuuuuuuuuuuuuu!!）」 (19 u).
- **1708** monologue — ずゆりゅ×4ぶびゅぶうぅ×6 = 16 u: 「（Zuyuryuryuryuryububyubuuuuuu~!）」 (15 u) → 「（Zuyuryuryuryuryububyubuuuuuuu~!）」 (16 u).
- **1709** monologue — ずにゅううぅ×4う = 9 u: 「（Gư!!! Zunyuuuu――kotsu!）」 (6 u) → 「（Gư!!! Zunyuuuuuuuu――kotsu!）」 (9 u).

### đại từ (13)
- **955** 稀咲 — JP 「ボクの、おまんこ――…」 (đang rên, sắp lên đỉnh): 「Âm hộ, của tôi――…」 → 「Âm hộ, của em――…」 (19:45 context → "em").
- **1014** 稀咲 — JP 「ボクもっ！　ボクもっ！　もうっ！」 (đang lên đỉnh): 「Tôi cũng! Tôi cũng!」 → 「Em cũng! Em cũng!」.
- **1033** 双鉄 — trích lời Paulette 『双鉄くんと稀咲って、…』: 「『Soutetsu-kun và Kisaki…』」 → 「『anh Soutetsu và Kisaki…』」 (khóa B4; "Soutetsu-kun" là romaji thô).
- **1075** 稀咲 — JP 「…ボクの、ヴァギナを――」 (rên giữa cuộc ân ái): 「…âm đạo, của tôi――」 → 「…âm đạo, của em――」.
- **1109** 稀咲 — JP 「ボクっ――ボクのっ――ヴァギナっ――…」 (rên thất thanh): 「…tôi――…của tôi!」 → 「…em――…của em!」.
- **1119** 双鉄 — JP 「…稀咲の好きに任せよう」: 「…giao phó mọi thứ cho em định đoạt.」 → 「…cho cô định đoạt.」 (03:32 Soutetsu→Kisaki "em"→"cô").
- **1160** 稀咲 — JP 「ボク……ばかみたい、嫉妬なんて……双鉄、僕に、夢中なのに」 (tự thú ghen tuông, giọng mềm yếu): 「…tôi……giống như đồ ngốc… Soutetsu, lại say đắm tôi…」 → 「…em……giống như đồ ngốc… Soutetsu, lại say đắm em…」.
- **1162** 稀咲 — JP 「ボクも！　そうっ！　なのっ！」 (đang lên đỉnh): 「Tôi cũng!」 → 「Em cũng!」.
- **1164** 双鉄 — JP 「僕から愛撫をしたい気持ちも、…」: 「…được tự mình ái ân em đến cháy bỏng――」 → 「…ái ân cô đến cháy bỏng――」 (03:32).
- **1183** 稀咲 — JP 「ボクは――つかれた。ちょっと、がんばりすぎたみたいで」 (thú nhận mệt sau ân ái, giọng mềm): 「Tôi――mệt rồi. Có vẻ, tôi đã cố gắng hơi quá sức.」 → 「Em――mệt rồi. Có vẻ, em đã cố gắng hơi quá sức.」 (độ tin cậy thấp nhất trong nhóm đại từ — xem cờ).
- **1233** 双鉄 — JP 「…お願いだ。頼む。」: 「…xin em đấy. Trăm sự nhờ em.」 → 「…xin cô đấy. Trăm sự nhờ cô.」 (03:32, 2 lần trong 1 dòng).
- **1245** 双鉄 — JP 「稀咲！　どうした、…」: 「…em đang nói cái điều hiển nhiên gì vậy.」 → 「…cô đang nói cái điều hiển nhiên gì vậy.」 (03:32).
- **1451** monologue — JP 「だから名を呼ぶ。」: 「Vì vậy tôi gọi tên em.」 → 「Vì vậy tôi gọi tên cô.」 (03:32, độc thoại).

### sai nghĩa (5)
- **1010** 双鉄 — JP 「ああ！　ああ！　ああ！　ああ！」 (TW 啊啊): 「Đúng vậy! Đúng vậy! Đúng vậy! Đúng vậy!」 → 「Aa! Aa! Aa! Aa!」 (ああ là tiếng rên, không phải "Đúng vậy").
- **1133** 稀咲 — JP 「ここ。だ。（ちゅっ！）」 (TW 就是因為這裡): 「Chỗ này. Đúng không. (Chu!)」 → 「Chỗ này đây. (Chu!)」 (câu khẳng định, VN cũ thêm "Đúng không" thành câu hỏi).
- **1166** 稀咲 — JP 「いくね？　双鉄っ」 (TW 我來了): 「Tới đây? Soutetsu.」 → 「Em ra nhé? Soutetsu.」 (いく = ra/cao trào; "Tới đây" đọc thành "lại đây").
- **1211** 稀咲 — JP 「…で、油断させて酔い潰して聞き出した」: 「…Thế là tôi lơ là cảnh giác, chuốc cho cô ta say mèm…」 → 「…Thế là tôi khiến cô ta mất cảnh giác, chuốc cho cô ta say mèm…」 (油断させて = khiến CÔ TA mất cảnh giác — causative; VN cũ đảo ngược chủ ngữ).
- **1390** monologue — JP 「…稀咲はにとにと、伸ばしては縮め弄び――」 (TW lược): 「…Kisaki nhóp nhép, kéo giãn rồi thu lại…」 → 「…Kisaki cười tủm tỉm, kéo giãn rồi thu lại…」 (にとにと = cười toe toét にたり, không phải "nhóp nhép" tiếng nhai/chóp chép).

### SFX (5)
- **1035** 双鉄 — JP 「あぐっ！！！！！！」 (6 !): 「Á!!!!!!!!!」 (9 !) → 「Agu!!!!!!」 ("Á" làm mất ぐ; sửa cả đếm !).
- **1038** 双鉄 — JP 「んぎっ！！！！？」: 「Á!!!!?」 → 「Ưngi!!!!?」 ("Á" làm mất んぎ).
- **1094** 稀咲 — JP 「うふふっ、双鉄。…」: 「Fufu, Soutetsu.…」 → 「Ufufu, Soutetsu.…」 (うふふっ→"Ufufu" như 1093; "Fufu" làm mất う đầu).
- **1690** monologue — JP 「（くちゅっ）」: 「（Chụt）」 → 「（Kuchu）」 ("Chụt" làm mất く; thống nhất với 1688 "kuchu" cho cùng token).
- **1720** monologue — JP 「（ぎゅりっ――ぃぃぃぃぃぃぃぃぃぃぃぃぃっ！！！）」 (13 ぃ, 3 !): 「（Véo――!!!!!）」 (5 !) → 「（Véo――iiiiiiiiiiiii!!!）」 (ぃ×13 bị mất hẳn — TW cũng lược; sửa cả đếm !).

### chính tả (1)
- **1287** 双鉄 — JP 「ならばよかっ！？――たたたたたっ！！」 (TW 那就好): 「Vậy thì tốt rồ!?――Đau đau đau đau đau!!」 → 「Vậy thì tốt rồi!?――Đau đau đau đau đau!!」 ("tốt rồ" vô nghĩa — lỗi gõ của よかった→"tốt rồi").

## Đại từ Kisaki — áp dụng quy tắc ngữ cảnh 19:45 (giữ nguyên 11 dòng)

18 dòng ボク/僕, tất cả VN cũ đều "tôi". Đổi 7 dòng (955/1014/1075/1109/1160/1162/1183 — rên, lên đỉnh, thú nhận mềm yếu). Giữ "tôi" 11 dòng: 947 (đùa khen hợp tần số), 1087 (thách Soutetsu giải thích lý do cô giận — quyết đoán), 1121 (trêu "cởi trói thì liệu tôi có bị làm tơi tả không" — trêu chọc, chủ động), 1134 (giải thích mục đích mua đồ lót), 1137 (mắng ghen — quyết đoán), 1153 (giải thích không véo dương vật), 1168 (nêu ý kiến), 1171 (vặn lại "Ngốc nghếch? Tôi á?" — quyết đoán), 1213 (chất vấn), 1297 (tuyên bố kế hoạch "tôi sẽ làm tất cả" — quyết đoán), 1298 (giải thích đã nghiên cứu sách/mạng). Soutetsu với Kisaki: "tôi" xuyên suốt, gọi Kisaki "cô" (1202/1222/1258/1265/1279 đúng) — chỉ 5 dòng "em" sai đã sửa; Kisaki gọi Soutetsu "cậu"/tên trần, 0 dòng "anh Soutetsu".

## Giữ nguyên có chủ đích (đã đọc, không sửa)

- **1025** ん～～～っ→"Ưm~~~", はああっ→"Haaa", ふあっ→"Fua" — mọi âm đều đã diễn, không mất gasp (quét máy báo sai do căn token lệch).
- **1065/1073** sweep already-rendered đúng (ん～～～～～っ→"Ưm~~~~~"; けど――っ→"đấy!").
- **1081** っていうか — っ đầu từ, không phải gasp (false positive của quét).
- **1126** おちんぽっ→"Dương vật" (trùng với ペニス→"Dương vật") — giữ: TW cũng dùng 肉棒 cho cả hai, chưa có quy tắc riêng cho おちんぽ; chỉ mất sắc thái thô, không sai nghĩa.
- **1281/1282** nói ngọng vì ngậm miệng (ほへははひょふへ → "Hô hê ha ha hyô fư hê") — giữ dạng âm ngọng như JP (TW dịch nghĩa, JP giữ âm ngọng).
- **1685/1695/1712–1719/1723/1724/1726–1728** SFX dịch thành động từ Việt (くっ→"Vạch", どさっ→"Bịch", ぎゅっ→"Véo", むぎゅっ→"Bóp chặt", ふるっ→"Lắc lư", さすっ→"Vuốt ve") — giữ, TW đồng ý; đếm ! đã kiểm tra khớp (1723: JP 9 = VN 9 — đếm mắt ban đầu nhầm 11).
- **1018** ああああああ (6 a) → "A a a a a a" (6 a) đúng; **1041/1046/1053/1054/1056/1060/1068/1069** họ ちゅう/ぢゅ đếm đúng (chuuu/chuuuu/juuu…).
- **1562** 「酒の途中で焼き鳥を、そんな調子で、感慨なしに」 → "…một cách điệu nghệ, không chút cảm xúc" — "điệu nghệ" thêm màu nhẹ cho そんな調子で, không đổi nghĩa, giữ.
- **1289** それじゃぁあ → "Vậy thì." — mất độ kéo dài, giữ (câu đệm, không phải rên/SFX).
- **997/998** んぷっ→"Ưmpu", あぐっっ→"Agu", きゃっっ→"Kya" — っ gắn từ âm đã diễn (tiền lệ), giữ; **995** んっっ→"ưm", だねっ→"nhỉ" — giữ theo quy tắc gasp đã khóa.

## Quyết định (đã quyết theo ủy quyền — ghi rõ căn cứ)

- **1010**: JP thắng TW? Không — JP và TW đồng ý (ああ/啊啊 đều là tiếng rên); VN cũ "Đúng vậy!" là đọc sai ああ thành khẳng định. Đã sửa trong audit.
- **1211**: 油断させて là causative (khiến Paulette mất cảnh giác); TW "把她灌醉" ngầm đồng ý chủ ngữ là Paulette. Đã sửa trong audit.
- **1166**: いく trong H-scene = ra/cao trào (tiền lệ "ra" toàn dự án); TW 我來了. Đã sửa trong audit.
- **1690**: "Kuchu" theo 1688 (cùng token くちゅっ) + mặc định giữ gần JP nhất; "Chụt" là SFX Việt hợp lệ nhưng mất く và phá nhất quán trong file. Đã sửa trong audit.
- **1183**: "em" theo quy tắc ngữ cảnh (thú nhận mệt, giọng mềm sau ân ái) — nhưng là phán đoán biên (câu trần thuật mệt mỏi), độ tin cậy thấp nhất; ghi cờ để parent/Hieu rà lại.
- **1262**: sweep ghi already-rendered là SAI cho っ! cuối dòng 1 (Ưm dòng 2 thuộc về んっ) — đã sửa trong audit, ghi rõ để vòng sweep rà lại logic already-rendered.
- **1062/1341/1425/1429/1551/1619**: giá trị sweep đúng nội dung nhưng 5/6 mục đa dòng dùng dạng TOML làm phẳng (space thay `\n`); 1062 cũng vậy. Đã khôi phục `\n` literal theo CSV3 trong fix.

## Cờ cho Hieu / parent

1. **1183** — "Tôi"→"Em" là phán đoán biên (thú nhận mệt sau ân ái); nếu Hieu thấy Kisaki lúc này vẫn ở giọng quyết đoán thì giữ "tôi".
2. **1690** — audit chọn "Kuchu" (theo 1688) thay "Chụt"; vòng moan xác nhận hướng SFX Việt vs romaji cho họ くちゅ.
3. **1126** — おちんぽっ và ペニス đều "Dương vật": có cần từ thô riêng cho おちんぽ (vd. "cặc") hay giữ "Dương vật" toàn dự án? Chưa có quy tắc — cần Hieu quyết.
4. **fa/fu** — file này dùng romaji "Fua" (991/1025/1075/1262/1263) nhất quán; "Phùa" vs "Fua" toàn dự án vẫn chưa chốt → đợt thống nhất.
5. **SFX độc thoại dài** (1703–1709, 1720): đã sửa đếm nguyên âm bằng máy; vòng moan rà lại toàn bộ họ SFX dài này.
6. B19 vẫn park (kiểm tra trong game tại Paulette 13 1596 trước khi chạy quét tag %l).

## Lượt soát 2

- Đọc lại toàn bộ 60 giá trị sửa đối chiếu JP (+TW) sau khi viết xong: **tổng 60 / tái kiểm chứng 60 / loại bỏ 0 / sửa lại 1** (1062: khôi phục `\n` literal — phát hiện bởi kiểm chứng diff cơ học khi ráp JSON; nội dung gasp không đổi).
- Kiểm tra cơ học: JSON 60 mục (key chuỗi); khối TOML parse được (tomllib), 60 khóa, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 60/60 (lấy trực tiếp từ CSV3); diff-sanity: mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm chứng bằng diff cơ học); 0 fix còn っ thô; mọi fix giữ nguyên dấu 「」/（） của dòng gốc; ngắt dòng là `\n` literal theo chuẩn CSV3.
- Cơ sở tổng: ROUTE-AUDIT.md lúc viết snippet là **212 file / 9.725 dòng sai** (parent giao 209/9.597 lúc 05:17, nhưng 3 file ハチロクh4 + 真闇h1 + 日々姫h4 đã merge lúc ~05:30 trong lúc audit — dùng cơ sở mới theo brief).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"710" = "「Ư……á――phù――á!」"
"955" = "「Thêm chút nữa――nhé――Soutetsu――ưm――á, a!\\nÂm hộ, của em――sắp được, rồi, mà!」"
"971" = "「Ư――gá――gư――」"
"972" = "「Ư! Há! Á! Kư!!!!」"
"974" = "「――Ư! Kưha!!」"
"1000" = "「~~~~Ư!」"
"1001" = "「Ư!!」"
"1003" = "「~~~~~~~~Ư!!!!」"
"1010" = "「Aa! Aa! Aa! Aa!」"
"1011" = "「A a a a a a a a a a a á!!!!!」"
"1013" = "「A a a a a á!!?」"
"1014" = "「Á! Á! Á! A! Cảm ơn! Soutetsu!\\nÂm hộ! Em cũng! Em cũng! Sắp! Ưm!」"
"1020" = "「ƯƯƯƯƯ!? Đau quá――――――――」"
"1029" = "「Ư!!」"
"1030" = "「Ư!!!」"
"1033" = "「A!!!! Đúng rồi, tôi nhớ ra rồi! Tôi cũng bị nói thế.\\n『anh Soutetsu và Kisaki ấy à, có vẻ làm tình nghiêm túc lắm』.」"
"1035" = "「Agu!!!!!!」"
"1038" = "「Ưngi!!!!?」"
"1039" = "「Ư!?」"
"1043" = "「Jumu! Bo! Jumu! Juru!!\\nChuuu! Juru! Jupa! Juu!!」"
"1045" = "「Dyubo! Juba! Ju! Ju!!!!\\nZuro o o o o o o o o o――――jubuuuuu!!!」"
"1055" = "「Reryuuuu――reryu――nuryu――(koku)\\nchu――chumu――chuuu――chuuuu.」"
"1057" = "「Dyubo! Ju! Reryuuuu! Juzu!\\n(Koku)――jubu! Juba! Jubo!」"
"1058" = "「Jumu! Jubo! Bo! Juuuuuu!\\nZubyu――chu――reru――zubo! Bochu!」"
"1062" = "「Khoan! Đợi đã! Kisa――tôi,\\nthở không nổi――tim đập nhanh quá――――ƯƯƯƯƯƯƯ!!!!」"
"1063" = "「Ikyuuuuuuuuuuuuuuuuuu!!!」"
"1064" = "「Kyufuuuu!!!!」"
"1075" = "「Ưm ưm ưm ưm――fua――a――sướng, quá――\\nDương vật, của Soutetsu, to, quá――đang làm, âm đạo, của em――」"
"1094" = "「Ufufu, Soutetsu. Nào, lăn qua đây nàoooooo.」"
"1109" = "「Tuyệt quá! Hôm nay――ưm――á――em――\\nâm đạo――âm, hộ――của em!」"
"1119" = "「Nếu Kisaki đã mong muốn như vậy, thì tất nhiên\\nđêm nay tôi sẽ giao phó mọi thứ cho cô định đoạt.」"
"1133" = "「Chỗ này đây. (Chu!)」"
"1160" = "「Thế này thì――em……giống như đồ ngốc vậy, lại đi ghen tuông……\\nTrong khi――ufufu――Soutetsu, lại say đắm em đến thế này.」"
"1162" = "「Em cũng! Vậy! Đó! Ưm――thình thịch,\\nthình thịch――từ đầu, dương vật, của Soutetsu――ưn ư!」"
"1164" = "「Tôi cũng rất yêu Kisaki, nên tôi cũng khao khát\\nđược tự mình ái ân cô đến cháy bỏng――」"
"1166" = "「Em ra nhé? Soutetsu.」"
"1183" = "「Em――mệt rồi.\\nCó vẻ, em đã cố gắng hơi quá sức.」"
"1211" = "「Mấy ngày liền Paulette cứ cười tủm tỉm suốt, tôi đã cảm thấy\\ncó chuyện gì đó rồi. Thế là tôi khiến cô ta mất cảnh giác, chuốc cho cô ta say mèm rồi moi thông tin.」"
"1233" = "「Ki, saki――Kisaki――xin cô đấy. Trăm sự nhờ cô.\\nNếu là trừng phạt thì sau này bao nhiêu cũng được――nên, bây giờ thì.」"
"1235" = "「Ư! Kisaki――ái!!!?」"
"1245" = "「Kisaki! Sao thế, cô đang nói cái điều hiển nhiên gì vậy.」"
"1262" = "「Fua! Á! Này! Soutetsu――Ư!\\nƯm! Soutetsu cũng――rất――sướng, đúng không? Nhỉ?」"
"1287" = "「Vậy thì tốt rồi!?――Đau đau đau đau đau!!」"
"1291" = "「Cảm ơn nhé, nhưng――Ư!」"
"1341" = "Khoái cảm thể xác cưỡng ép mà bản thân không thể kiểm soát nhịp độ!!\\nCổ họng tự động mở ra, não bộ bị lắc lư chao đảo――Ư!"
"1390" = "Có lẽ tinh dịch đã thấm đẫm vào đầu ngón tay găng tay, nhưng lượng tinh dịch vẫn còn rất nhiều,\\nKisaki cười tủm tỉm, kéo giãn rồi thu lại đùa giỡn với nó――"
"1425" = "Âm thanh sung sướng tự động trào ra khỏi cổ họng,\\ntôi vội vàng nuốt lại――Ư!!!!?"
"1429" = "Vừa định chồm tới đè cô ấy xuống thì mất thăng bằng, lúc đó tôi mới\\nnhớ ra là hai tay mình đang bị trói――Ư!!!"
"1451" = "Vì vậy tôi gọi tên cô. Tôi cất tiếng nói. Không để bản thân cuốn theo khoái cảm thể xác,\\ntôi muốn xuất tinh trong khi tâm hồn vẫn đang kết nối với Kisaki."
"1551" = "Hơi ấm, niêm mạc, nước bọt sền sệt của Kisaki đang làm sụp đổ mọi suy nghĩ trong tôi.\\nGiờ đây tôi chỉ khao khát được xuất tinh một cách sướng nhất――Ư!"
"1619" = "Toàn bộ quy đầu bị nuốt chửng.\\nSự chật chội và nóng rực từ âm đạo của Kisaki truyền đến càng thêm mãnh liệt――Ư!!"
"1690" = "（Kuchu）"
"1703" = "（Jubyuuuuuuuuuuuuuubojun!）"
"1704" = "（Zubyoooooooooo! Bujun!!!!）"
"1705" = "（Zubuuuuuuuuuuu!!! Gochu!!）"
"1706" = "（Zuro o o o o o o o o o o o o o o o o!!!）"
"1707" = "（Jubuuuuuuuuuuuuuuuuuu!!）"
"1708" = "（Zuyuryuryuryuryububyubuuuuuuu~!）"
"1709" = "（Gư!!! Zunyuuuuuuuu――kotsu!）"
"1720" = "（Véo――iiiiiiiiiiiii!!!）"
```

## Kết bài

File lr_稀咲h1_おしおきとごほうび.txt.toml: 297 dòng đã đọc kỹ từng dòng đối chiếu JP + TW, **60 dòng sai (20,2%)** — gasp 20, nguyên âm 16, đại từ 13, sai nghĩa 5, SFX 5, chính tả 1. Lỗi tập trung ở rên/moans và SFX dài (đếm nguyên âm sai 1–4, gasp っ bị mất, vài dòng sai nghĩa do đọc sai ああ/いく/油断させて) cộng cụm đại từ Kisaki (Soutetsu→Kisaki "em"→"cô" 6 chỗ, Kisaki tự xưng "tôi"→"em" 7 dòng theo ngữ cảnh). Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Sweep gasp kiểm tra trực tiếp 17/17 mục (áp 9 nguyên văn, sửa dạng `\n` 6 mục, sửa 1 mục already-rendered sai, tìm thêm 6 gasp bằng quét cơ học). Khối TOML 60 khóa đã kiểm chứng parse, 0 sai lệch. Lượt soát thứ hai: 60/60 tái kiểm chứng, 0 loại bỏ, 1 sửa (1062 khôi phục `\n`). 6 cờ cho Hieu/parent (1183 biên, 1690 Kuchu vs Chụt, 1126 おちんぽ, fa/fu Phùa vs Fua, SFX dài → vòng moan, B19 park).
