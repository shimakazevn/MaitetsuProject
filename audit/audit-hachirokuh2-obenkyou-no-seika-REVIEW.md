# Audit — ハチロクh2_お勉強の成果 (01_Hachiroku)

**File:** `ハチロクh2_お勉強の成果.txt.toml` — Route 01_Hachiroku, H-scene (Soutetsu × Hachiroku, đêm tân hôn: học từ sách rồi thực hành).
**Đường dẫn TOML:** `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30afh2_#U304a#U52c9#U5f37#U306e#U6210#U679c.txt.toml`
**CSV3:** `sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv`

## 1. Xác minh file

- TOML md5 `76334dd708ac74656eebf9f65c140e97`, UTF-8 BOM + CRLF, **1 bản duy nhất** (không có file trùng md5 trong `sources/toml2/` — không thuộc nhóm 11 file trùng).
- TOML: 312 dòng `[script]`, key 711–1767, `[selections]` rỗng, **0 tag `%l`** trong file, characters 1295/1381, character_subs 1353→Hachiroku, 1634→Suzu, 1672→Soutetsu.
- CSV3: **312 dòng, 1 bộ duy nhất**, section `script` 312/312, **0 key trùng**, **0 VN trống**, **0 VN==TW**.
- TOML↔CSV3: khớp 312/312 key, 0 key thiếu. 150 VN khác nhau chỉ do TOML-2 làm phẳng `\n` literal thành khoảng trắng (149 dòng) hoặc mất hẳn ký tự xuống dòng (key 1024) — không phải lỗi nội dung; CSV3 (literal `\n`) là chuẩn cho fix list.
- Cơ sở tổng đã kiểm chứng trực tiếp từ dòng tổng cuối ROUTE-AUDIT.md: **154 file / 6.891 dòng sai** (khớp cơ sở task giao — không cần rebase).

## 2. Tổng kết — 46/312 dòng sai (14,7%)

Đọc toàn bộ 312 dòng đối chiếu JP + TW (CSV3). Phân loại:

| Loại | Số dòng | Key |
|---|---:|---|
| Đại từ — Soutetsu tự xưng "anh" với Hachiroku (phải là "tôi") | 16 | 716, 923, 925, 1033, 1047, 1084, 1097, 1100, 1102, 1103, 1104, 1112, 1122, 1157, 1172, 1180 |
| Gasp っ (sweep 8 + sweep bỏ sót 3 + tên+っ 2; 1112 gộp vào đại từ) | 13 | 717, 720, 721, 976, 985, 987, 990, 1083, 1156, 1189, 1201, 1202, 1565 |
| Sai nghĩa / bịa thêm | 3 | 1014, 1088, 1145 |
| Thuật ngữ — 膣口/膣 | 6 | 1115, 1185, 1194, 1495, 1596, 1647 |
| Moan / SFX | 8 | 964, 972, 973, 974, 1045, 1053, 1055, 1148 |
| **Tổng** | **46** | |

- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch, 0 key trùng** (xem §6).
- Thoại: 双鉄H 66 dòng (16 sai đại từ), ハチロク 120 dòng, monologue 126 dòng.

## 3. Các lỗi

### 3.1 Đại từ — Soutetsu tự xưng "anh" với Hachiroku (16 dòng)

Quy tắc đã chốt: Soutetsu là **"tôi"** với Hachiroku (Hachiroku gọi Soutetsu là 双鉄様/"ngài Soutetsu" xuyên suốt file — vd. 926, 979, 981, 995, 1028). Toàn bộ 16 dòng thoại 双鉄H dùng "anh" đều sai; độc thoại trong file đã đúng "tôi" 100% (không sửa dòng độc thoại nào). Kiểm chứng addressee từ dòng kề cho từng dòng (người đối thoại duy nhất là Hachiroku/Suzu).

**716** (双鉄H)
- JP: 「――が、何ほどでもない。まだまだいけるさ」 / TW: 「——其實也沒有那麼累，我還可以」
- VN cũ: 「——Nhưng, chẳng thấm vào đâu. Anh vẫn còn làm được nữa」
- VN mới: 「——Nhưng, chẳng thấm vào đâu. Tôi vẫn còn làm được nữa」

**923** (双鉄H)
- JP: 「その本は――確定的に正しい。\n僕は……興奮し、このうえないほど、たかまっている」 / TW: 「你看的書——說得一點沒錯。我現在……就是興奮到無以復加了」
- VN cũ: 「Cuốn sách đó——chắc chắn là đúng rồi.\nAnh đang……hưng phấn, và kích thích đến mức không thể nào hơn được nữa」
- VN mới: 「Cuốn sách đó——chắc chắn là đúng rồi.\nTôi đang……hưng phấn, và kích thích đến mức không thể nào hơn được nữa」

**925** (双鉄H)
- JP: 「口に出し、飲んでもらえて、嬉しかった。\nすずに、包まれているような気がした」 / TW: 「你肯喝下去，我很高興。感覺自己被你包裹了似的」
- VN cũ: 「Anh rất vui vì được xuất vào miệng và được em nuốt lấy.\nCảm giác như được Suzu bao bọc vậy」
- VN mới: 「Tôi rất vui vì được xuất vào miệng và được em nuốt lấy.\nCảm giác như được Suzu bao bọc vậy」

**1033** (双鉄H) — 2 lần "anh"
- JP: 「んっ――だとは思うが……しかし……初めてのとき――\nあっ――あれほど、たくさん――射精、した、のに」 / TW: 「嗯——似的……但是……第一次做愛——啊——已經射了——那麼多了」
- VN cũ: 「Ưm——anh nghĩ là vậy……nhưng mà……lần đầu tiên——\na——anh đã xuất tinh, nhiều đến thế, rồi mà」
- VN mới: 「Ưm——tôi nghĩ là vậy……nhưng mà……lần đầu tiên——\na——tôi đã xuất tinh, nhiều đến thế, rồi mà」

**1047** (双鉄H)
- JP: 「ああ……\nそうしてもらえるのなら、嬉しい」 / TW: 「嗯……那我就太高興了」
- VN cũ: 「Ừm……\nNếu được em làm vậy, anh rất vui」
- VN mới: 「Ừm……\nNếu được em làm vậy, tôi rất vui」

**1084** (双鉄H)
- JP: 「性感のためだけの、か――\nならば初めてのときさすってやれば」 / TW: 「專門提供性刺激啊——那要是第一次的時候就撫摸——」
- VN cũ: 「Chỉ dành riêng cho khoái cảm, sao——\nVậy nếu lần đầu tiên anh vuốt ve nó thì」
- VN mới: 「Chỉ dành riêng cho khoái cảm, sao——\nVậy nếu lần đầu tiên tôi vuốt ve nó thì」

**1097** (双鉄H)
- JP: 「僕も――すずの全部が好きだ」 / TW: 「我——也喜歡鈴的全部」
- VN cũ: 「Anh cũng——thích tất cả mọi thứ của Suzu」
- VN mới: 「Tôi cũng——thích tất cả mọi thứ của Suzu」

**1100** (双鉄H)
- JP: 「恥ずかしがらせるのは本意ではない」 / TW: 「我不是故意想讓你害羞」
- VN cũ: 「Làm em xấu hổ không phải là ý định của anh」
- VN mới: 「Làm em xấu hổ không phải là ý định của tôi」

**1102** (双鉄H)
- JP: 「僕も、だ――」 / TW: 「我也——」
- VN cũ: 「Anh cũng, vậy——」
- VN mới: 「Tôi cũng, vậy——」

**1103** (双鉄H)
- JP: 「僕も、この上なく幸せだ」 / TW: 「我也是不能更幸福了」
- VN cũ: 「Anh cũng vậy, không gì hạnh phúc hơn」
- VN mới: 「Tôi cũng vậy, không gì hạnh phúc hơn」

**1104** (双鉄H) — 2 lần "Anh"
- JP: 「僕もだ。これほどに望んでる」 / TW: 「我也是很想的啊」
- VN cũ: 「Anh cũng vậy. Anh khao khát điều đó đến nhường này」
- VN mới: 「Tôi cũng vậy. Tôi khao khát điều đó đến nhường này」

**1112** (双鉄H) — đại từ + gasp (sweep raw-tsu, xem §4)
- JP: 「出る――と、言っている――のにっ」 / TW: 「我都說要射了——啊」
- VN cũ: 「Anh đã nói——là ra——rồi màっ」
- VN mới: 「Tôi đã nói——là ra——rồi màƯ」

**1122** (双鉄H)
- JP: 「ほう。教えてもらえるか？」 / TW: 「是嗎，能告訴我嗎？」
- VN cũ: 「Ồ. Dạy cho anh được không?」
- VN mới: 「Ồ. Dạy cho tôi được không?」

**1157** (双鉄H)
- JP: 「僕の妻になってくれて、ありがとう」 / TW: 「謝謝你願意做我的妻子」
- VN cũ: 「Cảm ơn em, vì đã trở thành vợ anh」
- VN mới: 「Cảm ơn em, vì đã trở thành vợ tôi」

**1172** (双鉄H) — 2 lần "anh"
- JP: 「ならば、子宮もあるのだな。一番奥まで押し込んだとき、\n肉の扉をノックするような感じがあった」 / TW: 「那你也有子宮啊。我插得最深的時候有敲到肉門一樣的感覺」
- VN cũ: 「Vậy thì, em cũng có tử cung đấy. Khi anh đâm vào sâu nhất,\nanh có cảm giác như đang gõ vào một cánh cửa bằng thịt vậy」
- VN mới: 「Vậy thì, em cũng có tử cung đấy. Khi tôi đâm vào sâu nhất,\ntôi có cảm giác như đang gõ vào một cánh cửa bằng thịt vậy」

**1180** (双鉄H)
- JP: 「だから、するぞ？　僕とすずとのセックスを」 / TW: 「那我要做了，只屬於我和你的性愛」
- VN cũ: 「Vậy nên, bắt đầu nhé? Cuộc làm tình của anh và Suzu」
- VN mới: 「Vậy nên, bắt đầu nhé? Cuộc làm tình của tôi và Suzu」

### 3.2 Gasp っ (13 dòng)

8 mục sweep đã kiểm chứng đúng giá trị (xem §4: 717, 721, 976, 987, 1083, 1156, 1201, 1565) + 3 gasp sweep bỏ sót (720, 985, 1202 — cùng quy tắc gasp trơ trụi như 987/1201) + 2 tên+っ (990, 1189 — tiền lệ sweep ハチロクh9 2109: さまっ → "SoutetsuƯ"). Quy tắc khóa: thêm Ư chỉ khi っ hoàn toàn mất (đầu dòng hoặc cuối tuyệt đối không dấu câu); không diễn trùng っ đã diễn bằng gạch/dấu câu.

**717** (双鉄H) — sweep raw-tsu
- JP: 「――しゃべると、舌、がっ！」 / TW: 「——別說話，舌頭會……！」
- VN cũ: 「——Nói chuyện, thì lưỡi, sẽっ!」
- VN mới: 「——Nói chuyện, thì lưỡi, sẽƯ!」

**720** (双鉄H) — sweep bỏ sót: gasp đầu dòng mất hẳn
- JP: 「――っ――あっ」 / TW: 「——嗯——啊」
- VN cũ: 「——a」 (chỉ diễn あっ; っ đầu dòng mất)
- VN mới: 「——Ư——a」

**721** (双鉄H) — sweep lost-gasp-trailing
- JP: 「――っ」 / TW: 「——嗯」
- VN cũ: 「——」
- VN mới: 「——Ư」

**976** (ハチロク) — sweep raw-tsu (chỉ っ cuối dòng "のっ" còn thô)
- JP: 「ふあっ――すごっ――んっ――あっ――ああっ！\nくっ――来ますっ――まっしろなっ――おっきい、のっ」 / TW: 「呼啊——好厲害——啊——啊啊！嗯——來了——雪白——好大的」
- VN cũ: 「Phù a——tuyệt quá——ưm——a——a a!\nHự——đến đây——thứ gì đó trắng xóa——to lớnっ」
- VN mới: 「Phù a——tuyệt quá——ưm——a——a a!\nHự——đến đây——thứ gì đó trắng xóa——to lớnƯ」

**985** (双鉄H) — sweep bỏ sót: cả dòng chỉ là gasp
- JP: 「っ――！」 / TW: 「唔——！」
- VN cũ: 「!」
- VN mới: 「Ư——!」

**987** (双鉄H) — sweep lost-gasp-whole
- JP: 「っ！」 / TW: 「唔！」
- VN cũ: 「!」
- VN mới: 「Ư!」

**990** (双鉄H) — tên+っ (tiền lệ h9 2109)
- JP: 「あ――あっ、すず、すずっ」 / TW: 「啊——啊，鈴、鈴」
- VN cũ: 「A——a, Suzu, Suzu」
- VN mới: 「A——a, Suzu, SuzuƯ」

**1083** (ハチロク) — sweep raw-tsu
- JP: 「に、人間であれば、子宮、と、いう――あっ――\n赤ちゃんの、お部屋が、ある、そう――なの、ですがっ」 / TW: 「如、如果是人類，就是子宮——啊——小寶寶的房間，那樣——但是」
- VN cũ: 「Nế, nếu là con người, thì sẽ có——a——\nmột căn phòng, dành cho em bé, gọi là tử cung——nhưng màっ」
- VN mới: 「Nế, nếu là con người, thì sẽ có——a——\nmột căn phòng, dành cho em bé, gọi là tử cung——nhưng màƯ」

**1156** (ハチロク) — sweep raw-tsu
- JP: 「か――かもしれませんが――んっ、あの痛み、\nわたくしは、とても嬉しく、感じてっ、おりました」 / TW: 「說不定——嗯，但那個疼痛，我覺得非常高興……」
- VN cũ: 「Có——có thể là vậy ạ——ưm, nhưng nỗi đau đó,\nem lại cảm thấy, rất vui sướngっ」
- VN mới: 「Có——có thể là vậy ạ——ưm, nhưng nỗi đau đó,\nem lại cảm thấy, rất vui sướngƯ」

**1189** (双鉄H) — tên+っ (cùng mẫu 990)
- JP: 「すず、すずっ」 / TW: 「鈴，鈴」
- VN cũ: 「Suzu, Suzu」
- VN mới: 「Suzu, SuzuƯ」

**1201** (双鉄H) — sweep lost-gasp-whole
- JP: 「っ！？」 / TW: 「！？」
- VN cũ: 「!?」
- VN mới: 「Ư!?」

**1202** (双鉄H) — sweep bỏ sót: gasp đầu dòng mất hẳn (cùng mẫu 1201)
- JP: 「っ！？　待っ―うぁっ」 / TW: 「！？等一下……啊」
- VN cũ: 「!? Đợi——u a」 ("Đợi——" đã diễn 待っ; "u a" diễn うぁっ theo tiền lệ bare あっ)
- VN mới: 「Ư!? Đợi——u a」

**1565** (monologue) — sweep lost-gasp-trailing
- JP: 「何故だろう。\n切なげな目で僕を見て、そのまま動きを止め――っ！？」 / TW: 「為什麼呢。她懇切似地看我，停下了動作——！？」
- VN cũ: "Tại sao chứ.\nEm nhìn tôi bằng ánh mắt thiết tha, rồi cứ thế dừng mọi chuyển động——!?"
- VN mới: "Tại sao chứ.\nEm nhìn tôi bằng ánh mắt thiết tha, rồi cứ thế dừng mọi chuyển động——Ư!?"

### 3.3 Sai nghĩa / bịa thêm (3 dòng)

**1014** (ハチロク) — bịa "ngài Soutetsu" + bỏ mất nửa sau JP
- JP: 「はふはむはふはむおはひひははひ、ほーふぇふはま」 / TW: 「啊嗚啊嗚啊嗚」 (chỉ có tiếng ngọng, không có 双鉄)
- VN cũ: 「A fư ha mư a fư ha mư o ha hi hi ha ha hi, ngài Soutetsu」 — "ngài Soutetsu" không có trong JP/TW (bịa kiểu Gemini); đồng thời bỏ mất cả vế "ほーふぇふはま"
- VN mới: 「A fư ha mư a fư ha mư o ha hi hi ha ha hi, hô phuê phư ha ma」 (ほー→"hô", ふぇ→"phuê" theo quy tắc đã chốt, ふ→"phư", は→"ha", ま→"ma")

**1088** (双鉄H) — sai thì/thể: JP là tiếc nuối quá khứ, VN dịch thành tương lai
- JP: 「すずの痛みを、もっと減らしてやれたのかな？」 / TW: 「就能讓你不那麼痛了嗎？」 (やれた = tiềm năng quá khứ: "liệu đã có thể làm bớt đau hơn không")
- VN cũ: 「Sẽ giúp Suzu bớt đau hơn đúng không?」 ("Sẽ giúp" = tương lai — sai hướng thời gian)
- VN mới: 「Liệu tôi đã có thể giúp Suzu bớt đau hơn không nhỉ?」

**1145** (双鉄H) — bịa "mà vui"
- JP: 「痛みをか？」 / TW: 「疼痛嗎？」 (chỉ hỏi "Đau à?")
- VN cũ: 「Đau mà vui sao?」 — "mà vui" không có trong JP/TW
- VN mới: 「Đau sao?」

### 3.4 Thuật ngữ — 膣口 / 膣 (6 dòng)

File dùng lẫn lộn: 膣口 và 膣 đều dịch thành "âm đạo" (1115, 1185, 1194), thậm chí 膣 bị dịch nhầm thành "tử cung" (1115, 1194) — sai cơ quan (tử cung = 子宮, đã dùng đúng ở 1083/1172/1519). Chuẩn thống nhất toàn file: **膣口 → "cửa âm đạo", 膣 → "âm đạo"** (khớp 10+ dòng 膣 đã đúng: 1317, 1320, 1361, 1617, 1646, 1671).

**1115** (ハチロク)
- JP: 「そ、そこ――入り口は、[ちつこう,1]膣口、というそうです。\nその奥の――んっ、おちんちんを、受け入れる筒が、膣」 / TW: 「據說那裡——入口叫陰道口。裡面——就是接受小雞雞的陰道」
- VN cũ: 「Đó, đó——phần cửa vào, gọi là âm đạo ạ.\nSâu bên trong——ưm, cái ống tiếp nhận cậu bé, là tử cung」
- VN mới: 「Đó, đó——phần cửa vào, gọi là cửa âm đạo ạ.\nSâu bên trong——ưm, cái ống tiếp nhận cậu bé, là âm đạo」

**1185** (双鉄H)
- JP: 「改めてこうして見てみると……\nすずは、膣口までもが愛らしいのだな」 / TW: 「重新看來……你還真是從外表到陰道口都可愛」
- VN cũ: 「Nhìn kỹ lại thế này mới thấy……\nSuzu, ngay cả âm đạo cũng đáng yêu thật đấy」
- VN mới: 「Nhìn kỹ lại thế này mới thấy……\nSuzu, ngay cả cửa âm đạo cũng đáng yêu thật đấy」

**1194** (双鉄H)
- JP: 「[ちつこう,1]膣口に、膣か――\n膣の、さらに奥の方はどうなっている？」 / TW: 「陰道口和陰道啊——陰道更深處呢？」
- VN cũ: 「Âm đạo, tử cung sao——\nSâu bên trong tử cung, thì có gì?」
- VN mới: 「Cửa âm đạo, âm đạo sao——\nSâu bên trong âm đạo, thì có gì?」

**1495** (monologue)
- JP: 「すずの可愛い割れ目を開いて、\n膣口を目視で確認しなおす。」 / TW: 「我剝開鈴可愛的肉縫，重新目測陰道口。」
- VN cũ: "Tách khe hở đáng yêu của Suzu ra,\ntôi tận mắt xác nhận lại âm đạo."
- VN mới: "Tách khe hở đáng yêu của Suzu ra,\ntôi tận mắt xác nhận lại cửa âm đạo."

**1596** (monologue)
- JP: 「勃起の一番先端を、膣口に軽く押し付けてみれば、\n柔らかな肉がひくひく動き、僕を甘やかに呑もうとする。」 / TW: 「肉棒的最尖端輕輕頂在陰道口上，柔肉就抽動起來，要軟軟地吞下我。」
- VN cũ: "Thử ấn nhẹ đỉnh phần cương cứng vào âm đạo,\nlớp thịt mềm mại co giật, ngọt ngào chực nuốt lấy tôi."
- VN mới: "Thử ấn nhẹ đỉnh phần cương cứng vào cửa âm đạo,\nlớp thịt mềm mại co giật, ngọt ngào chực nuốt lấy tôi."

**1647** (monologue)
- JP: 「すずの膣口はおつゆにまみれ、\nくぱくぱ、ひくひく物欲しそうに震えてる。」 / TW: 「鈴的陰道口全是愛液，一張一合地抽動著，似乎很想要。」
- VN cũ: "Âm đạo của Suzu đẫm dịch nhờn,\nco bóp, giật giật run rẩy như đang thèm khát."
- VN mới: "Cửa âm đạo của Suzu đẫm dịch nhờn,\nco bóp, giật giật run rẩy như đang thèm khát."

### 3.5 Moan / SFX (8 dòng)

**964** (ハチロク) — きゅ sai nguyên âm + sai số lượng (quy tắc ひゃ-family: romaji; công thức đếm nguyên âm)
- JP: 「ひゅあっ！？\nんっ――んきゅううううううううううっ！！！」 / TW: 「呀啊！？嗯——嗯嗚嗚嗚嗚嗚嗚嗚嗚嗚！！！」
- VN cũ: 「Hyu a!?\nƯm——ưm kyaaaa!!!」 — きゅう×9 bị dịch thành "kyaaaa": sai nguyên âm (kyu→kya) và sai số lượng (9う → 4 a)
- VN mới: 「Hyu a!?\nƯm——Nkyuuuuuuuuuu!!!」 (んきゅ → "Nkyu" dính theo tiền lệ んひゅ→"Nhyu"; きゅ+9う = 10 u)

**973** (ハチロク) — mất âm: thiếu 1あ + mất ん (romaji fallback cho moan fa/fu dài)
- JP: 「ふあああんっ！」 / TW: 「呼、啊嗯！」 (ふ+3あ+ん+っ)
- VN cũ: 「Phù a a!」 (chỉ 2 a, không có n)
- VN mới: 「Fuaaan!」 (fu + 3a + n; "!" diễn っ)

**974** (ハチロク) — mất ん trong あんっ
- JP: 「ふあっ――あっ――あんっ！　んっ――」 / TW: 「呼啊——啊——啊！嗯——」
- VN cũ: 「Phù a——a——a! Ưm——」 ("a!" cho あんっ — mất ん)
- VN mới: 「Phù a——a——an! Ưm——」

**1053** (ハチロク) — ひゅ-family phải romaji (quy tắc 21/11 ~11:55; "Á"/"Ưm hưm" làm mất phụ âm hy-)
- JP: 「んひゅっ！　好き、すきすき、おてても、\n指――もっ」 / TW: 「嗯咻！喜歡，喜歡喜歡，您的手，您的手指——」
- VN cũ: 「Ưm hưm! Thích, thích lắm, cả bàn tay,\ncả ngón tay——nữa」
- VN mới: 「Nhyu! Thích, thích lắm, cả bàn tay,\ncả ngón tay——nữa」 (んひゅ → "Nhyu" đúng quy tắc; もっ cuối dòng là っ nhấn mạnh trên trợ từ — giữ nguyên, xem §5)

**1055** (ハチロク) — きゅ sai nguyên âm (kyu→kya) + tách mora
- JP: 「んきゅっ！！」 / TW: 「嗯嗚！！」
- VN cũ: 「Ưm kya!!」
- VN mới: 「Nkyu!!」 (んきゅ → "Nkyu" dính, đúng nguyên âm u; "!!" diễn っ)

**1045** (ハチロク) — れろっ dịch sai họ âm (file tự dùng "liếm" cho れる/れろ 4 chỗ khác: 1013, 1022, 1038, cùng dòng này)
- JP: 「ん……ちゅっ……ちゅるっ……ん……\nれるっ……じゅっ……じゅる……れろっ」 / TW: 「嗯……啾……啾嚕……嗯……咻嚕……啾……啾嚕……咻嚕」
- VN cũ: 「Ưm……chụt……chu mút……ưm……\nliếm……chụt……chu mút……sột sột」 ("sột sột" là họ âm ướt của じゅぶ/ずにゅ trong file này — 1718/1719/1720 — không phải tiếng liếm)
- VN mới: 「Ưm……chụt……chu mút……ưm……\nliếm……chụt……chu mút……liếm」

**972** (ハチロク) — tiếng cười phải là "Ufufu" (dạng chuẩn đã chốt), không tách "Ư fufu"
- JP: 「うふふ、双鉄様、良かったのですね？\n先走りのおつゆが――ほぉら、こんなにニチニチと」 / TW: 「呵呵，雙鐵少爺，這樣很舒服吧？你的預射液——淌了這麼多出來呢」
- VN cũ: 「Ư fufu, ngài Soutetsu, thấy sướng đúng không ạ?\nDịch nhờn rỉ ra——ngài xem, dính nhớp thế này cơ mà」
- VN mới: 「Ufufu, ngài Soutetsu, thấy sướng đúng không ạ?\nDịch nhờn rỉ ra——ngài xem, dính nhớp thế này cơ mà」

**1148** (ハチロク) — cùng mẫu 972
- JP: 「それほど心地よいのですか。　\n嬉しい、うふふ。では、次のお作法にすすみますね？」 / TW: 「真就這麼舒服嗎？那太好了，嘻嘻。我要開始下一步了啦」
- VN cũ: 「Sung sướng đến thế cơ ạ.\nEm vui quá, ư fufu. Vậy thì, em xin phép chuyển sang bước tiếp theo nhé?」
- VN mới: 「Sung sướng đến thế cơ ạ.\nEm vui quá, Ufufu. Vậy thì, em xin phép chuyển sang bước tiếp theo nhé?」

## 4. Kiểm chứng sweep gasp của file (9/9 mục trong sweep-raw-gasp-wrong.json)

Đã đọc trực tiếp 9 mục của file này trong sweep; cả 9 đều đúng JP và được áp nguyên giá trị sweep:

| Key | Loại sweep | Giá trị sweep |
|---|---|---|
| 717 | raw-tsu | "sẽƯ!" |
| 721 | lost-gasp-trailing | "——Ư" |
| 976 | raw-tsu | "to lớnƯ" |
| 987 | lost-gasp-whole | "Ư!" |
| 1083 | raw-tsu | "nhưng màƯ" |
| 1112 | raw-tsu | "rồi màƯ" (gộp với sửa đại từ) |
| 1156 | raw-tsu | "rất vui sướngƯ" |
| 1201 | lost-gasp-whole | "Ư!?" |
| 1565 | lost-gasp-trailing | "——Ư!?" |

Sweep bỏ sót 3 gasp cùng quy tắc (720, 985, 1202 — đã sửa ở §3.2) và 2 tên+っ (990, 1189 — tiền lệ h9 2109).

## 5. Các dòng giữ nguyên có lý do (đáng chú ý)

- **Bare あっ → "A"/"a"** (1007, 1036, 1043, 986, 719, 1012 ああ→"À", 1183): giữ theo tiền lệ sweep — sweep cố tình không thêm Ư cho あっ trơ trụi (vd. ハチロク02 2282, ハチロク06 2031, 凪ふかみ03 2274: 「あっ」→"A." giữ nguyên; lr_凪h2 1268: 8×「あっ！」→"A!" giữ nguyên).
- **っ cuối dòng sau nguyên âm dài bỏ** (1195 さまぁっ → "Soutetsu", tiền lệ h1 1238; 719 ぅあっ → "ư a").
- **っ nhấn mạnh gắn từ có nội dung — không phải gasp** (1032 出るっ → "ra mất"; 1053 もっ; 966 のっ; 1506 続けっ; 1767 これっ――は; tiền lệ 共通15 1474 ブロワーっ).
- **っ đã diễn bằng gạch/dấu câu — không diễn trùng** (989 あっ――→"A——"; 1028 好きっ――→"thích——"; 1031 んっっ→"Ưm"; 1003 ごくんっ→"ực").
- **"Phù a"/"phù a" cho ふあっ** (974, 996, 1001, 1003, 1004, 1006, 1011, 1036, 1038): giữ nguyên — âm đầy đủ, nhất quán trong file; đợt thống nhất + vòng moan sẽ xem xét lại họ fa/fu (chuyển romaji nếu ngượng) theo quyết định 21/11 ~01:56. Chỉ sửa 973/974 ở chỗ mất âm thật sự.
- **SFX trong ngoặc diễn theo nghĩa hành động** (1717–1767: "Phập", "Sột sột", "Chụt", "Ấn", "Ngoạm" v.v.): giữ theo tiền lệ ROUTE-AUDIT (chỉ sửa khi sai hẳn âm). Riêng "sột sột" đã thống nhất trong file cho họ âm ướt じゅぶ/ずにゅ (1718/1719/1720) — chỉ 1045 là dùng sai chỗ (đã sửa).
- **くふうううううんっ → "Ư hưm"** (1030): giữ — tiền lệ 932 くあっ→"Ư a!" (く đầu moan diễn thành Ư).
- **んくっ/んむっ → "Ưm"** (1039, 1054): giữ theo tiền lệ cũ (947/949 んきゅ→"Ưm"; 868 んきゅっっ→"Ưm") — hai họ này không thuộc nhóm romaji bắt buộc ひゃ/ひゅ/ひあ/きゃ.
- **1627 "(chiếc chuông nhỏ)"**: giữ — gloss nghĩa tên 鈴 = chuông, TW xác nhận cách chơi chữ ("她就跟鈴鐺一樣"), không phải bịa.
- **ポーカー → "que cời than"** (1086): đúng — đây là gậy khều than, không phải bài poker; TW 火鉗 xác nhận.
- **1086, 1185, 1495, 1596, 1647** — xem §3.4 (đã sửa 膣口).

## 6. Kiểm tra lệch vị trí / tràn chương / mồ côi / chưa dịch / key trùng

- **Lệch vị trí 0 cặp, chuỗi xoay vòng 0:** đọc ngữ nghĩa từng dòng theo thứ tự key; cảnh H diễn tiến liền mạch (cởi đồ → oral → học từ sách → thực hành → cao trào → trò chuyện sau). Không có cặp dòng nào bị đảo.
- **Tràn chương 0:** kiểm tra chỉ mục VN toàn dự án (91.731 dòng CSV3): 43 VN trong file này cũng xuất hiện ở file khác với JP khác — tất cả đều là dòng ngắn chung (moan 1 âm "A"/"Ưm!", "Vâng", "Hả?", "Đúng vậy", SFX "Phập!"/"Chụt"/"Nắn nắn") hoặc tên gọi lặp ("Suzu, Suzu" ở h9 2592 cùng là gọi tên) — không có dòng thoại nội dung nào bị tràn. Nhóm trùng VN trong file (6 nhóm: 「!」×3 là 985/987/1200 — 2 trong 3 đã sửa khác nhau; 「Ư……a」×2, 「A, may quá!」×2, 「Ưm!」×2, 「（Nắn nắn）」×2, 「（Siết! Siết chặt!）」×2) đều là SFX/câu ngắn hợp lệ với JP khác nhau nhưng cùng họ âm.
- **Dòng mồ côi 0:** mọi VN đều đối chiếu được với đúng JP của key đó (sai là sai cách dịch, không phải dòng lạ).
- **Chưa dịch 0:** 0 VN trống, 0 VN==TW.
- **Key trùng 0** (CSV3 lẫn TOML).
- **JP-side (không phải lỗi VN, không sửa):** key **1174** — JP gốc thiếu dấu 」 đóng (cả comment `# JP:` trong TOML lẫn CSV3 đều thiếu; VN đã đóng 」 đúng); key **1730** — JP gốc mở （ đóng 」 (lệch ngoặc; VN đã dùng （…） đúng). Hai lỗi này nằm ở phía nguồn, chờ Hieu/quy trình nguồn nếu muốn sửa gốc — VN đã chuẩn hóa đúng nên không tính sai.

## 7. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 46 giá trị sửa đối chiếu từng JP (+TW) sau khi viết fix list, đồng thời kiểm tra cơ học: JSON 46 mục (key dạng string), jp/tw/old_vn khớp CSV3 tuyệt đối 46/46, khối TOML parse đúng 46/46 key, 0 sai lệch giá trị, diff từng fix chỉ khác VN cũ ở đúng chỗ sửa.

- **Tổng: 46 / tái kiểm chứng: 46 / loại bỏ: 0 / sửa lại: 0.**

## 8. Khối TOML (đã parse-verified: 46/46 key, 0 sai lệch giá trị)

```toml
[script]
716 = "「——Nhưng, chẳng thấm vào đâu. Tôi vẫn còn làm được nữa」"
717 = "「——Nói chuyện, thì lưỡi, sẽƯ!」"
720 = "「——Ư——a」"
721 = "「——Ư」"
923 = "「Cuốn sách đó——chắc chắn là đúng rồi.\\nTôi đang……hưng phấn, và kích thích đến mức không thể nào hơn được nữa」"
925 = "「Tôi rất vui vì được xuất vào miệng và được em nuốt lấy.\\nCảm giác như được Suzu bao bọc vậy」"
964 = "「Hyu a!?\\nƯm——Nkyuuuuuuuuuu!!!」"
972 = "「Ufufu, ngài Soutetsu, thấy sướng đúng không ạ?\\nDịch nhờn rỉ ra——ngài xem, dính nhớp thế này cơ mà」"
973 = "「Fuaaan!」"
974 = "「Phù a——a——an! Ưm——」"
976 = "「Phù a——tuyệt quá——ưm——a——a a!\\nHự——đến đây——thứ gì đó trắng xóa——to lớnƯ」"
985 = "「Ư——!」"
987 = "「Ư!」"
990 = "「A——a, Suzu, SuzuƯ」"
1014 = "「A fư ha mư a fư ha mư o ha hi hi ha ha hi, hô phuê phư ha ma」"
1033 = "「Ưm——tôi nghĩ là vậy……nhưng mà……lần đầu tiên——\\na——tôi đã xuất tinh, nhiều đến thế, rồi mà」"
1045 = "「Ưm……chụt……chu mút……ưm……\\nliếm……chụt……chu mút……liếm」"
1047 = "「Ừm……\\nNếu được em làm vậy, tôi rất vui」"
1053 = "「Nhyu! Thích, thích lắm, cả bàn tay,\\ncả ngón tay——nữa」"
1055 = "「Nkyu!!」"
1083 = "「Nế, nếu là con người, thì sẽ có——a——\\nmột căn phòng, dành cho em bé, gọi là tử cung——nhưng màƯ」"
1084 = "「Chỉ dành riêng cho khoái cảm, sao——\\nVậy nếu lần đầu tiên tôi vuốt ve nó thì」"
1088 = "「Liệu tôi đã có thể giúp Suzu bớt đau hơn không nhỉ?」"
1097 = "「Tôi cũng——thích tất cả mọi thứ của Suzu」"
1100 = "「Làm em xấu hổ không phải là ý định của tôi」"
1102 = "「Tôi cũng, vậy——」"
1103 = "「Tôi cũng vậy, không gì hạnh phúc hơn」"
1104 = "「Tôi cũng vậy. Tôi khao khát điều đó đến nhường này」"
1112 = "「Tôi đã nói——là ra——rồi màƯ」"
1115 = "「Đó, đó——phần cửa vào, gọi là cửa âm đạo ạ.\\nSâu bên trong——ưm, cái ống tiếp nhận cậu bé, là âm đạo」"
1122 = "「Ồ. Dạy cho tôi được không?」"
1145 = "「Đau sao?」"
1148 = "「Sung sướng đến thế cơ ạ.\\nEm vui quá, Ufufu. Vậy thì, em xin phép chuyển sang bước tiếp theo nhé?」"
1156 = "「Có——có thể là vậy ạ——ưm, nhưng nỗi đau đó,\\nem lại cảm thấy, rất vui sướngƯ」"
1157 = "「Cảm ơn em, vì đã trở thành vợ tôi」"
1172 = "「Vậy thì, em cũng có tử cung đấy. Khi tôi đâm vào sâu nhất,\\ntôi có cảm giác như đang gõ vào một cánh cửa bằng thịt vậy」"
1180 = "「Vậy nên, bắt đầu nhé? Cuộc làm tình của tôi và Suzu」"
1185 = "「Nhìn kỹ lại thế này mới thấy……\\nSuzu, ngay cả cửa âm đạo cũng đáng yêu thật đấy」"
1189 = "「Suzu, SuzuƯ」"
1194 = "「Cửa âm đạo, âm đạo sao——\\nSâu bên trong âm đạo, thì có gì?」"
1201 = "「Ư!?」"
1202 = "「Ư!? Đợi——u a」"
1495 = "Tách khe hở đáng yêu của Suzu ra,\\ntôi tận mắt xác nhận lại cửa âm đạo."
1565 = "Tại sao chứ.\\nEm nhìn tôi bằng ánh mắt thiết tha, rồi cứ thế dừng mọi chuyển động——Ư!?"
1596 = "Thử ấn nhẹ đỉnh phần cương cứng vào cửa âm đạo,\\nlớp thịt mềm mại co giật, ngọt ngào chực nuốt lấy tôi."
1647 = "Cửa âm đạo của Suzu đẫm dịch nhờn,\\nco bóp, giật giật run rẩy như đang thèm khát."
```

## Kết bài

File ハチロクh2_お勉強の成果: đọc 312/312 dòng, **46 dòng sai (14,7%)** — đại từ 16, gasp 13 (+1112 gộp), sai nghĩa 3, thuật ngữ 膣口/膣 6, moan/SFX 8. Lỗi lớn nhất là hệ thống: Soutetsu tự xưng "anh" trong toàn bộ thoại với Hachiroku (16/16 dòng thoại có đại từ, 0 lần "tôi" đúng) và cụm 膣口/膣 bị dịch lẫn thành "âm đạo"/"tử cung". 0 lệch vị trí, 0 tràn chương, 0 mồ côi, 0 chưa dịch, 0 key trùng. Lượt soát 2: 46/46 tái kiểm chứng, 0 loại, 0 sửa lại. Khối TOML parse đúng 46/46. Hai ghi chú JP-side (1174 thiếu 」, 1730 lệch ngoặc) không tính sai vì VN đã chuẩn hóa đúng. Không có điểm nào cần Hieu quyết ngay; họ fa/fu "Phù a" giữ nguyên chờ đợt thống nhất + vòng moan xem xét romaji theo quyết định 21/11 ~01:56.

