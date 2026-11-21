# Audit — ニイロク04_終端.txt.toml (route 08_Niiroku)

- File: `ニイロク04_終端.txt.toml` — route 08_Niiroku, "Niiroku 04 — Kết thúc".
- Disk: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/08_Niiroku/#U30cb#U30a4#U30ed#U30af04_#U7d42#U7aef.txt.toml`
- Đọc: **452/452 dòng** (script keys 51–2884), đọc từng dòng đối chiếu JP + TW (CSV3).
- Sai: **44 dòng (9,7%)** — 59 điểm sửa.
- Cơ sở tổng: 168 file / 7.676 dòng sai (đã tự kiểm chứng ROUTE-AUDIT.md — khớp với cơ sở được giao).

## Nội dung file

Akai Kiyoharu (赤井清春) và Niiroku đối mặt với hồi kết: Kuha 26 bị đưa đi phế thải hồi tống về Moji; Shiro (Hachiroku) hy sinh thân bảo trì để cứu Niiroku; Kiyoharu cùng Trưởng khu tàu điện và Gotou xoay xở chữ ký (338 người) và kế hoạch công ty đường sắt mới; Niiroku dần nhận ra Shiro sẽ kết thúc. Không có H-scene. Nhân vật chính trong file: Akai (độc thoại + thoại, xưng "tôi"), Niiroku ("em", gọi Kiyoharu là "anh"), Gotou, Trưởng khu tàu điện, 先輩 (tiền bối, nói phương ngữ Hakata), 2 kỹ thuật viên. **Soutetsu (双鉄) KHÔNG xuất hiện trong file (0 lần)** — quy tắc đại từ Soutetsu không áp dụng; 先輩 là nhân vật riêng, không phải Soutetsu.

## Phân loại (44 dòng / 59 điểm)

- Thuật ngữ: **34 dòng / 49 điểm** — 整備体 "Thân chính/thân chính"→"thân bảo trì" 8 · 運転体 "kíp lái/Kíp lái"→"thân vận hành" 12 · 操作板 "thẻ bảng/Thẻ bảng"→"máy tính bảng" 11 · 鞄 "túi phi hành đoàn"→"túi công tác" 3 (+ sửa term trong tag %l 3: 乗務鞄→運転鞄 ×2, →運転士鞄 ×1) · 帝鉄 "Đường sắt Hoàng gia"→"Teitetsu" 2 · 冥国 "Meikoku"→"Minh Quốc" 2 · 機関士 "lái tàu/thợ máy"→"thợ lái đầu máy" 2 · 電車区長 "Đoạn trưởng xe điện"→"Trưởng khu tàu điện" 3 · tên 後東/後東塊太 Hán-Việt→"Goto"/"Goto Kaita"/"Cường Đạo Kaita" 3.
- Gasp (っ): **10 dòng** — 9 mục sweep raw-tsu (っ thô trong VN → Ư) + 1 mục sweep bỏ sót (1748, JP 「っ！？」 VN mất hẳn っ → thêm Ư).

## Kiểm tra cấu trúc

- Lệch vị trí 0 · chuỗi xoay 0 · nhiễm chéo 0 · mồ côi 0 · chưa dịch 0 · trùng khóa 0.
- CSV3: 1 set duy nhất, 452/452 key; VN khớp phẳng TOML 452/452 (TOML-2 làm phẳng `\n` literal thành khoảng trắng, CSV3 là chuẩn).
- TOML md5: `a981c54ec743c6e4b045d9549ab234ca` (UTF-8 BOM + CRLF); **1 bản duy nhất, không trùng lặp**.
- `[selections]` rỗng; `[characters]` 2282=Niiroku, 2441=Tiền bối, 2542=Gotou, 2620=Kỹ thuật viên A, 2622=Kỹ thuật viên B, 2755=Akai, 2800=Trưởng ga tàu điện.
- Tag %l: 44 dòng VN có tag mà JP CSV3 không có tag — đây là hiện tượng hệ thống (CSV3 lược tag JP; comment `# JP:` trong TOML có tag), không phải bịa tag. Tag VN tự thêm có nội dung đúng (1287 編成→"đoàn tàu", 1593 列車→"tàu", 1659 架線→"đường dây tiếp điện trên cao", 2056 保線→"bảo trì đường ray", 2823 蒸気機関車→"đầu máy hơi nước") — chỉ ghi nhận, không tính sai (tiền lệ Grand 03).

## Sweep っ-gasp kiểm chứng

- Sweep có 9 mục cho file này (raw-tsu: 1244, 1265, 1731, 1743, 1746, 1757, 2114, 2115, 2364) — nhận 9/9, 0 mục sai.
- Quét toàn bộ っ trong JP (137 dòng chứa っ): phát hiện thêm **1 mục sweep bỏ sót — 1748** (JP 「っ！？」 VN 「!?」 mất hẳn っ → 「Ư!?」). Các っ còn lại đều đã diễn đạt đúng: っ trong từ (そっか, ちょっと, まったく…), っ nhấn mạnh trên từ có nội dung đã được !/——/dấu câu truyền tải (1820 それでもっ, 1847 後東っ, 1853 切るんだっ, 1878 しないでっ, 2357 壊れるっ, 1658 とてもっ…), っ đã diễn đạt (1930 うんっ→"Ưm", 1724 えっ→"Hả", 1635 なっ→"Cái gì").

## Đại từ đã rà toàn file

- Akai "tôi" nhất quán (độc thoại + thoại); Niiroku "em" nhất quán, gọi Kiyoharu "anh" nhất quán (1724, 1777, 1913, 1916); Gotou 俺→"tôi" (2029) giữ nguyên; 先輩 được Akai gọi "tiền bối" (1977, 2460, 2551).
- Niiroku gọi Hachiroku "chị Shiro" nhất quán. Không có dòng nào của Soutetsu để kiểm tra.

## Giữ nguyên, ghi nhận

- 1710 ひあっ→"Hi á": GIỮ — cảnh không phải H-scene (Niiroku hoảng sợ khi Shiro gắng sức), SFX ngẫu hứng; ひ đã diễn thành "Hi", っ được dấu ―― sau đó truyền tải (không double-render theo gasp boundary đã khóa). Cụm SFX cùng cảnh 1717/1721 đã dùng romaji.
- 1717/1721/1722/1755/1756 SFX: GIỮ — diễn ngẫu hứng, âm không mất hẳn (1717/1721 romaji; 1722 ぐっ→"ư" khớp 1755 ぐっ→"Ư" trong cùng file; 1756 ひぐっ→"Hức").
- 1747 JP 「！！？」 VN 「!!?」: GIỮ — JP không có っ, không phải gasp (TW thêm 啊 là TW tự thêm).
- マスター gloss "Master" (7 dòng: 1293, 1790, 1808, 1846, 1966, 2429, 2857): GIỮ — tiền lệ toàn dự án dùng "Master" cho マスター (ROUTE-AUDIT 2308; ハチロク15b "good bye――My Master"); TW 司機/駕駛員 chỉ là cách diễn của TW.
- 2650 運転士 gloss "lái tàu": GIỮ — 運転士 khác 機関士, không có thuật ngữ đã quyết cho 運転士.
- 2152 機関助士 gloss "Phụ lái tàu": GIỮ — đúng (phụ lái).
- 1597/1742 trường âm: đếm JP あ 45/46, VN g 49 / á 47 — khớp, GIỮ.
- 1784 「頼みます」 "Trăm sự nhờ cậu lo cho Niiroku": GIỮ — "cậu" hợp lý (Shiro nhắn Kiyoharu); TW không ghi đại từ.
- 1891/2777 日ノ本 "Hinomoto" đã đúng; 2009/2027 Yunoi đã đúng; 2138/2514 Aircra đã đúng; 共感 "cộng cảm" đã đúng toàn file; 2113 博太 "Hakata" đã đúng; 1178/1628/1829/2861/2883 Teitetsu đã đúng.
- 1244: くっ→"ư", すう→"hít", はぁっ→"hà" đã có sẵn trong VN — sweep chỉ sửa っ đầu dòng, nhận nguyên.

## Cờ cho Hieu

- **Không có câu hỏi mở cần Hieu quyết trong file này.** Hai điểm đã quyết theo quy tắc (ghi chú để parent kiểm chứng khi merge): (1) 2411 機関士 dùng dạng đầy đủ "thợ lái đầu máy" vì là độc thoại (dạng ngắn "lái tàu" chỉ dùng trong thoại — theo quyết định 19/11); (2) 2550/2796 "Kaita" theo ruby JP ごとうかいた, thắng TW 慶太/Keita (quy tắc JP thắng TW).
- Lưu ý unification pass (không sửa ở đây): "Master" (7 dòng) và 運転士 "lái tàu" (2650 + 2592) nếu dự án muốn thống nhất sau này.

## Lượt soát 2

- **44 tổng / 44 tái kiểm chứng / 0 bỏ / 0 sửa.** Đọc lại toàn bộ 44 giá trị fix đối chiếu JP + TW; kiểm chứng cơ học: JSON 44 mục (key chuỗi, list-of-dicts), khối TOML 44 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 44/44; mỗi fix chỉ khác old VN ở đúng điểm sửa (diff-sanity từng dòng).

## Danh sách sửa (44 dòng)


### 1244 — 赤井 (gasp)

- JP: 「――っ――くっ――すう――――はぁっ！」
- TW: 「——吸——呼！」
- Cũ: 「——っ——ư——hít――――hà!」
- Mới: 「——Ư——ư——hít――――hà!」
- Sweep raw-tsu: っ thô trong VN → Ư (gasp đầu dòng; くっ→"ư", すう→"hít", はぁっ→"hà" đã có sẵn trong VN, chỉ sửa っ đầu).

### 1247 — 赤井 (thuật ngữ)

- JP: 「――整備体は、諦めるしかないかと思います」
- TW: 「——我想，只能放棄你的整備體了」
- Cũ: 「——\x%l整備体;#00ffc040;Thân chính%l;#; thì, tôi nghĩ chỉ còn cách từ bỏ thôi.」
- Mới: 「——\x%l整備体;#00ffc040;Thân bảo trì%l;#; thì, tôi nghĩ chỉ còn cách từ bỏ thôi.」
- Thuật ngữ đã quyết: 整備体="thân bảo trì" ("Thân chính" sai; đầu câu nên viết hoa).

### 1261 — 電車区長 (thuật ngữ)

- JP: 「“帝鉄側”の、手の内全部ぞ」
- TW: 「“帝國鐵路方”所有的手段都跟這裡寫著呢」
- Cũ: 「Là toàn bộ con bài trong tay của 'Phía Đường sắt Hoàng gia' đấy.」
- Mới: 「Là toàn bộ con bài trong tay của 'Phía Teitetsu' đấy.」
- Thuật ngữ đã quyết: 帝鉄="Teitetsu" ("Đường sắt Hoàng gia" sai; cùng file 1178/1628 đã dùng "Teitetsu" đúng).

### 1265 — 赤井 (gasp)

- JP: 「っ」
- TW: 「……」
- Cũ: 「っ」
- Mới: 「Ư」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 1285 — 赤井 (thuật ngữ)

- JP: 「……運転体については、\n取引を持ちかけられています」
- TW: 「……對於駕駛體，有人想跟我們做個交易」
- Cũ: 「……Về \x%l運転体;#00ffc040;kíp lái%l;#; thì,\nđang có người đề nghị giao dịch.」
- Mới: 「……Về \x%l運転体;#00ffc040;thân vận hành%l;#; thì,\nđang có người đề nghị giao dịch.」
- Thuật ngữ đã quyết: 運転体="thân vận hành" ("kíp lái" sai nghĩa — "kíp lái" là tổ lái, còn 運転体 là thân thể dùng để lái; TW 駕駛體).

### 1639 — 赤井 (thuật ngữ)

- JP: 「動作確認を省略した。結果、運転鞄の中には、\n運転体の[モックアップ,4]等身大模型が入っています」
- TW: 「他們省略了測試功能那一步。所以，現在他的駕駛包裡，裝著駕駛體的等身大模型」
- Cũ: 「Đã lược bỏ việc xác nhận hoạt động. Kết quả là, bên trong \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;,\nchứa một mô hình kích thước người thật của \x%l運転体;#00ffc040;kíp lái%l;#;.」
- Mới: 「Đã lược bỏ việc xác nhận hoạt động. Kết quả là, bên trong \x%l運転鞄;#00ffc040;túi công tác%l;#;,\nchứa một mô hình kích thước người thật của \x%l運転体;#00ffc040;thân vận hành%l;#;.」
- Thuật ngữ đã quyết: 運転鞄="túi công tác" ("túi phi hành đoàn" là thuật ngữ hàng không, sai — đã quyết 20/11); đồng thời sửa term trong tag %l cho khớp JP: VN ghi 乗務鞄 nhưng JP là 運転鞄 (đã kiểm chứng comment # JP trong TOML). Cùng dòng: 運転体→"thân vận hành".

### 1731 — 赤井 (gasp)

- JP: 「っ！！！」
- TW: 「唔！！！」
- Cũ: 「っ!!!」
- Mới: 「Ư!!!」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 1743 — 赤井 (gasp)

- JP: 「っ！」
- TW: 「啊！」
- Cũ: 「っ!」
- Mới: 「Ư!」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 1746 — 赤井 (gasp)

- JP: 「っ！！！」
- TW: 「啊！！！」
- Cũ: 「っ!!!」
- Mới: 「Ư!!!」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 1748 — 赤井 (gasp)

- JP: 「っ！？　これは？」
- TW: 「啊！？您的意思是？」
- Cũ: 「!? Đây là?」
- Mới: 「Ư!? Đây là?」
- GASP SWEEP BỎ SÓT (phát hiện khi quét toàn bộ っ trong JP): JP 「っ！？」 VN mất hẳn っ → thêm Ư. Sweep chỉ có 9 mục cho file này, không có 1748.

### 1757 — 赤井 (gasp)

- JP: 「っ！！！！」
- TW: 「嗚！！！！」
- Cũ: 「っ!!!!」
- Mới: 「Ư!!!!」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 1768 — ニイロク (thuật ngữ)

- JP: 「うん。それは最初からわかっていた。\n整備体には、[パーソナルマーク,5]個体識別部位が多すぎる」
- TW: 「嗯。打從一開始我就知道了。整備體的個體識別部位太多了」
- Cũ: 「Ừm. Chuyện đó thì ngay từ đầu em đã biết rồi.\n\x%l整備体;#00ffc040;Thân chính%l;#; có quá nhiều bộ phận nhận diện cá thể.」
- Mới: 「Ừm. Chuyện đó thì ngay từ đầu em đã biết rồi.\n\x%l整備体;#00ffc040;Thân bảo trì%l;#; có quá nhiều bộ phận nhận diện cá thể.」
- Thuật ngữ đã quyết: 整備体="thân bảo trì".

### 1819 — 電車区長 (thuật ngữ)

- JP: 「じゃの。そぎゃんば、帝鉄の――いいや、\n国と、[めいこく,1]冥国との意思たい」
- TW: 「對。這是帝國鐵路的——不對，是日本跟美國的意思」
- Cũ: 「Đúng vậy. Đó chính là ý chí của Teitetsu——à không,\ncủa quốc gia, và của nước Meikoku đấy.」
- Mới: 「Đúng vậy. Đó chính là ý chí của Teitetsu——à không,\ncủa quốc gia, và của nước Minh Quốc đấy.」
- Thuật ngữ đã quyết: 冥国="Minh Quốc" (furigana JP là めいこく, không phải メリケン nên không dùng "Meriken"; "Meikoku" là romaji thô. TW 美國 đồng nghĩa Minh Quốc).

### 1828 — 赤井 (thuật ngữ)

- JP: 「帝鉄の――冥国のいう“帝鉄解体”とは、\nつまり、全車輌の解体という意味なのですね？」
- TW: 「帝國鐵路——美國所謂的“解散帝國鐵路”，是指要拆毀所有車輛嗎？」
- Cũ: 「“Giải thể Teitetsu” mà Teitetsu——nước Meikoku nói đến,\nnói cách khác, có nghĩa là giải thể toàn bộ toa xe phải không?」
- Mới: 「“Giải thể Teitetsu” mà Teitetsu——nước Minh Quốc nói đến,\nnói cách khác, có nghĩa là giải thể toàn bộ toa xe phải không?」
- Thuật ngữ đã quyết: 冥国="Minh Quốc" (như 1819; JP không có furigana メリケン).

### 1847 — 電車区長 (thuật ngữ)

- JP: 「やめぇ[ごとう,1]後東っ！！！」
- TW: 「後東，不准亂來！！！」
- Cũ: 「Dừng lại đi Hậu Đông!!!」
- Mới: 「Dừng lại đi Goto!!!」
- Tên riêng nhất quán toàn file: 後東→"Goto" (ruby JP [ごとう,1]; "Hậu Đông" là Hán-Việt, chỉ 2 dòng dùng — 1847 và 2550 — còn lại toàn file dùng "Goto").

### 1902 — ニイロク (thuật ngữ)

- JP: 「この体。整備体。\n明日にはもう、なくなっちゃうでしょ？」
- TW: 「我的這副身體——整備體。明天是不是就要消失了？」
- Cũ: 「Cơ thể này. \x%l整備体;#00ffc040;Thân chính%l;#; này.\nĐến ngày mai là, sẽ biến mất đúng không?」
- Mới: 「Cơ thể này. \x%l整備体;#00ffc040;Thân bảo trì%l;#; này.\nĐến ngày mai là, sẽ biến mất đúng không?」
- Thuật ngữ đã quyết: 整備体="thân bảo trì".

### 1918 — 赤井 (thuật ngữ)

- JP: 「ですので、あとはタブレットです。\nタブレットさえどうにかできれば」
- TW: 「所以，接下來就是操作板了。只要能搞定操作板，接下來就好說了」
- Cũ: 「Vì vậy, còn lại là \x%l操作板;#00ffc040;thẻ bảng%l;#;.\nChỉ cần giải quyết được \x%l操作板;#00ffc040;thẻ bảng%l;#; thì.」
- Mới: 「Vì vậy, còn lại là \x%l操作板;#00ffc040;máy tính bảng%l;#;.\nChỉ cần giải quyết được \x%l操作板;#00ffc040;máy tính bảng%l;#; thì.」
- Thuật ngữ đã quyết: 操作板/タブレット="máy tính bảng" ("thẻ bảng" sai; 2 lần trong cùng dòng).

### 1978 — 赤井 (thuật ngữ)

- JP: 「そこは任意です。運転体・整備体の順であっても、\nその逆であってもかまわない。結果は同じですから」
- TW: 「沒有，可以隨意測試。不管是從駕駛體開始，還是從整備體開始都沒有關係。因為結果是一樣的」
- Cũ: 「Cái đó là tùy ý. Dù là theo thứ tự \x%l運転体;#00ffc040;kíp lái%l;#; - \x%l整備体;#00ffc040;thân chính%l;#;,\nhay ngược lại cũng không sao. Vì kết quả đều giống nhau mà.」
- Mới: 「Cái đó là tùy ý. Dù là theo thứ tự \x%l運転体;#00ffc040;thân vận hành%l;#; - \x%l整備体;#00ffc040;thân bảo trì%l;#;,\nhay ngược lại cũng không sao. Vì kết quả đều giống nhau mà.」
- Thuật ngữ đã quyết: 運転体→"thân vận hành", 整備体→"thân bảo trì".

### 2011 — ニイロク (thuật ngữ)

- JP: 「そこまでするなら――後東さんは、\nどうしてタブレットも助けないの？」
- TW: 「為什麼後東先生做到這種地步，也保不住操作板呢？」
- Cũ: 「Nếu đã làm đến mức đó——thì anh Goto,\ntại sao lại không cứu cả \x%l操作板;#00ffc040;thẻ bảng%l;#;?」
- Mới: 「Nếu đã làm đến mức đó——thì anh Goto,\ntại sao lại không cứu cả \x%l操作板;#00ffc040;máy tính bảng%l;#;?」
- Thuật ngữ đã quyết: 操作板="máy tính bảng".

### 2024 — 赤井 (thuật ngữ)

- JP: 「もちろんですとも。運転鞄、あけますね」
- TW: 「當然可以。我把駕駛包打開」
- Cũ: 「Tất nhiên là được rồi. Tôi mở \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; ra nhé.」
- Mới: 「Tất nhiên là được rồi. Tôi mở \x%l運転鞄;#00ffc040;túi công tác%l;#; ra nhé.」
- Thuật ngữ đã quyết: 運転鞄="túi công tác"; đồng thời sửa term trong tag %l cho khớp JP (VN ghi 乗務鞄, JP là 運転鞄 — đã kiểm chứng comment # JP trong TOML).

### 2041 — 赤井 (thuật ngữ)

- JP: 「車輌、レイルロオド運転体、レイルロオド整備体。\nその全てが揃っていることが、まず確認されます」
- TW: 「第一步，是檢查車輛、鐵路人偶駕駛體、鐵路人偶整備體這三者是不是都齊全」
- Cũ: 「Toa xe, \x%l運転体;#00ffc040;kíp lái%l;#; Railord, \x%l整備体;#00ffc040;thân chính%l;#; Railord.\nTrước tiên, họ sẽ xác nhận xem tất cả những thứ đó có đầy đủ hay không.」
- Mới: 「Toa xe, \x%l運転体;#00ffc040;thân vận hành%l;#; Railord, \x%l整備体;#00ffc040;thân bảo trì%l;#; Railord.\nTrước tiên, họ sẽ xác nhận xem tất cả những thứ đó có đầy đủ hay không.」
- Thuật ngữ đã quyết: 運転体→"thân vận hành", 整備体→"thân bảo trì".

### 2054 — 赤井 (thuật ngữ)

- JP: 「結果として、ブランクの運転体が[のこ]遺りました。\nタブレットも、整備体も車輌も無い運転体が」
- TW: 「結果就是，他保住了一台空白的駕駛體。它既沒有操作板，也沒有整備體、更別提車輛」
- Cũ: 「Kết quả là, một \x%l運転体;#00ffc040;kíp lái%l;#; trống rỗng đã bị bỏ lại.\nMột \x%l運転体;#00ffc040;kíp lái%l;#; không có \x%l操作板;#00ffc040;thẻ bảng%l;#;, không có \x%l整備体;#00ffc040;thân chính%l;#; cũng không có toa xe.」
- Mới: 「Kết quả là, một \x%l運転体;#00ffc040;thân vận hành%l;#; trống rỗng đã bị bỏ lại.\nMột \x%l運転体;#00ffc040;thân vận hành%l;#; không có \x%l操作板;#00ffc040;máy tính bảng%l;#;, không có \x%l整備体;#00ffc040;thân bảo trì%l;#; cũng không có toa xe.」
- Thuật ngữ đã quyết: 運転体→"thân vận hành" (×2), 操作板→"máy tính bảng", 整備体→"thân bảo trì".

### 2061 — 赤井 (thuật ngữ)

- JP: 「運転体とタブレット。最低限それだけ守れば」
- TW: 「至少，我一定要保住你的駕駛體和操作板」
- Cũ: 「\x%l運転体;#00ffc040;Kíp lái%l;#; và \x%l操作板;#00ffc040;thẻ bảng%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」
- Mới: 「\x%l運転体;#00ffc040;Thân vận hành%l;#; và \x%l操作板;#00ffc040;máy tính bảng%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」
- Thuật ngữ đã quyết: 運転体→"Thân vận hành" (đầu câu, viết hoa), 操作板→"máy tính bảng".

### 2110 — 赤井 (thuật ngữ)

- JP: 「こちらが、現帝鉄職員338名分の署名。\nそして、こちらが趣旨提案書となります」
- TW: 「這是現帝國鐵路職員共計３３８人的署名。還有，這是我們主要計劃的提案書」
- Cũ: 「Đây là chữ ký của 338 nhân viên Đường sắt Hoàng gia hiện tại.\nVà, đây là bản đề xuất mục đích.」
- Mới: 「Đây là chữ ký của 338 nhân viên Teitetsu hiện tại.\nVà, đây là bản đề xuất mục đích.」
- Thuật ngữ đã quyết: 帝鉄="Teitetsu" ("Đường sắt Hoàng gia" sai).

### 2114 — 赤井 (gasp)

- JP: 「っ！！！」
- TW: 「這！！！」
- Cũ: 「っ!!!」
- Mới: 「Ư!!!」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 2115 — ニイロク (gasp)

- JP: 「っ！！！？」
- TW: 「這！！！？」
- Cũ: 「っ!!!?」
- Mới: 「Ư!!!?」
- Sweep raw-tsu: っ thô trong VN → Ư.

### 2150 — ニイロク (thuật ngữ)

- JP: 「それなら！　後東さんのレイルロオドは、\n運転体だけは助かるの？」
- TW: 「那麼！後東先生的鐵路人偶就可以保住駕駛體了，是嗎？」
- Cũ: 「Nếu vậy! Railord của anh Goto,\nchỉ cứu được mỗi \x%l運転体;#00ffc040;kíp lái%l;#; thôi sao?」
- Mới: 「Nếu vậy! Railord của anh Goto,\nchỉ cứu được mỗi \x%l運転体;#00ffc040;thân vận hành%l;#; thôi sao?」
- Thuật ngữ đã quyết: 運転体="thân vận hành".

### 2151 — ニイロク (thuật ngữ)

- JP: 「なら、\n動作確認したあとのタブレットは、そのまま？」
- TW: 「那麼，測試完之後的操作板，就放在那不動了？」
- Cũ: 「Nếu vậy,\n\x%l操作板;#00ffc040;thẻ bảng%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」
- Mới: 「Nếu vậy,\n\x%l操作板;#00ffc040;máy tính bảng%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」
- Thuật ngữ đã quyết: 操作板="máy tính bảng".

### 2152 — 赤井 (thuật ngữ)

- JP: 「レイルロオド自らがタブレットを外部に投げ捨てる。\n機関助士、ないし密乗した者が同様の行為をする」
- TW: 「鐵路人偶可能會自己把操作板丟到車外面。司爐，以及偷偷搭上車的人也有可能會這麼做」
- Cũ: 「Railord tự mình ném \x%l操作板;#00ffc040;thẻ bảng%l;#; ra bên ngoài.\n\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」
- Mới: 「Railord tự mình ném \x%l操作板;#00ffc040;máy tính bảng%l;#; ra bên ngoài.\n\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」
- Thuật ngữ đã quyết: 操作板="máy tính bảng" (機関助士 gloss "Phụ lái tàu" giữ nguyên — đúng).

### 2153 — 赤井 (thuật ngữ)

- JP: 「レイルロオドは、\nタブレット換装によっての動作確認がなされます」
- TW: 「鐵路人偶是更換操作板來測試運作是否正常的」
- Cũ: 「Railord thì,\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \x%l操作板;#00ffc040;thẻ bảng%l;#;.」
- Mới: 「Railord thì,\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \x%l操作板;#00ffc040;máy tính bảng%l;#;.」
- Thuật ngữ đã quyết: 操作板="máy tính bảng".

### 2175 — ニイロク (thuật ngữ)

- JP: 「運転体なら、パーソナルマークはとても少ない。\nレイルロオド工機部の人たちに頼めば」
- TW: 「駕駛體的個體識別部位非常少。只要拜託鐵路人偶工程機械部的人動個手腳——」
- Cũ: 「Nếu là \x%l運転体;#00ffc040;kíp lái%l;#; thì, bộ phận nhận diện cá thể rất ít.\nNếu nhờ những người ở bộ phận cơ khí Railord thì.」
- Mới: 「Nếu là \x%l運転体;#00ffc040;thân vận hành%l;#; thì, bộ phận nhận diện cá thể rất ít.\nNếu nhờ những người ở bộ phận cơ khí Railord thì.」
- Thuật ngữ đã quyết: 運転体="thân vận hành".

### 2364 — monologue (gasp)

- JP: 共感を、さっそくつないだのでしょう。\nニイロクの体があたたかに――っ！！？
- TW: 二六一定是很快連上了共鳴。她的身體變熱了——！！？
- Cũ: Có lẽ em ấy đã kết nối \x%l共感;#00ffc040;cộng cảm%l;#; ngay lập tức.\nCơ thể Niiroku bỗng trở nên ấm áp——っ!!?
- Mới: Có lẽ em ấy đã kết nối \x%l共感;#00ffc040;cộng cảm%l;#; ngay lập tức.\nCơ thể Niiroku bỗng trở nên ấm áp——Ư!!?
- Sweep raw-tsu: っ thô trong VN → Ư (độc thoại; 共感 gloss "cộng cảm" đã đúng).

### 2411 — monologue (thuật ngữ)

- JP: これほどの機関士とレイルロオドです。\n機転によって、シロのタブレットも回収されれば――
- TW: 他們是那麼優秀的司機和鐵路人偶。如果隨機應變，能拿回四六的操作板——
- Cũ: Là một \x%l機関士;#00ffc040;lái tàu%l;#; và Railord tuyệt vời đến thế cơ mà.\nNếu tùy cơ ứng biến, và thu hồi được cả \x%l操作板;#00ffc040;thẻ bảng%l;#; của Shiro thì——
- Mới: Là một \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; và Railord tuyệt vời đến thế cơ mà.\nNếu tùy cơ ứng biến, và thu hồi được cả \x%l操作板;#00ffc040;máy tính bảng%l;#; của Shiro thì——
- Thuật ngữ đã quyết: 機関士="thợ lái đầu máy" — dạng đầy đủ, vì đây là độc thoại (dạng ngắn "lái tàu" chỉ dùng trong thoại); cùng dòng 操作板→"máy tính bảng".

### 2550 — monologue (thuật ngữ)

- JP: [ごとうかいた,3]後東塊太――\n同期の中でもこれ程に、食えぬ男は他にいません。
- TW: 後東慶太——在我的同期中，他是令我最不爽的人。
- Cũ: Hậu Đông Khối Thái――\nTrong số những người cùng thời, không ai khó đối phó bằng cậu ta.
- Mới: Goto Kaita――\nTrong số những người cùng thời, không ai khó đối phó bằng cậu ta.
- Tên riêng: JP ruby [ごとうかいた,3]後東塊太 → "Goto Kaita" (JP thắng TW: TW viết 後東慶太/Keita; "Hậu Đông Khối Thái" là Hán-Việt).

### 2592 — monologue (thuật ngữ)

- JP: 見回せば、無数の視線が返ります。\n粉蔵所属の――大げさではなく、全運転士・機関士の。
- TW: 我環顧四周，看到無數視線正看著我。不誇張地說，屬於小倉管轄的所有駕駛員和司機都在這。
- Cũ: Nhìn quanh, vô số ánh mắt đáp lại tôi.\nCủa những người thuộc Kokura――không nói quá đâu, là của toàn bộ lái tàu và thợ máy.
- Mới: Nhìn quanh, vô số ánh mắt đáp lại tôi.\nCủa những người thuộc Kokura――không nói quá đâu, là của toàn bộ lái tàu và thợ lái đầu máy.
- Thuật ngữ đã quyết: 機関士="thợ lái đầu máy" ("thợ máy" sai hẳn — thợ máy là thợ sửa chữa, không phải người lái; 運転士→"lái tàu" giữ nguyên).

### 2594 — monologue (thuật ngữ)

- JP: 真正面から、喉の、奥。そこを強く、親指で押す。\n運転体でも、整備体でも、変わらない。
- TW: 我用大拇指，用力從正面按住二六的喉嚨。駕駛體和整備體的強制關閉方式都一樣。
- Cũ: Từ chính diện, sâu bên trong, cổ họng. Dùng ngón cái ấn mạnh vào đó.\nDù là \x%l運転体;#00ffc040;kíp lái%l;#; hay \x%l整備体;#00ffc040;thân chính%l;#;, cũng không có gì khác biệt.
- Mới: Từ chính diện, sâu bên trong, cổ họng. Dùng ngón cái ấn mạnh vào đó.\nDù là \x%l運転体;#00ffc040;thân vận hành%l;#; hay \x%l整備体;#00ffc040;thân bảo trì%l;#;, cũng không có gì khác biệt.
- Thuật ngữ đã quyết: 運転体→"thân vận hành", 整備体→"thân bảo trì".

### 2603 — monologue (thuật ngữ)

- JP: 運転士鞄を漁ります。
- TW: 我翻找著駕駛包。
- Cũ: Tôi lục lọi trong \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;.
- Mới: Tôi lục lọi trong \x%l運転士鞄;#00ffc040;túi công tác%l;#;.
- Thuật ngữ đã quyết: 運転士鞄="túi công tác"; đồng thời sửa term trong tag %l cho khớp JP (VN ghi 乗務鞄, JP là 運転士鞄 — đã kiểm chứng comment # JP trong TOML).

### 2624 — monologue (thuật ngữ)

- JP: シロのタブレットを、ブランクのダミー運転体に、\nそして、ニイロクの整備体へと。
- TW: 把四六的操作板放到空白的駕駛體上，然後，配以二六的整備體。
- Cũ: \x%l操作板;#00ffc040;Thẻ bảng%l;#; của Shiro, vào \x%l運転体;#00ffc040;kíp lái%l;#; mô hình trống rỗng,\nvà sau đó, là vào \x%l整備体;#00ffc040;thân chính%l;#; của Niiroku.
- Mới: \x%l操作板;#00ffc040;Máy tính bảng%l;#; của Shiro, vào \x%l運転体;#00ffc040;thân vận hành%l;#; mô hình trống rỗng,\nvà sau đó, là vào \x%l整備体;#00ffc040;thân bảo trì%l;#; của Niiroku.
- Thuật ngữ đã quyết: 操作板→"Máy tính bảng" (đầu câu, viết hoa), 運転体→"thân vận hành", 整備体→"thân bảo trì".

### 2673 — monologue (thuật ngữ)

- JP: どう考えても、高負荷すぎです。\nタブレットが瞬時に破損したとて、おかしくない程。
- TW: 無論怎麼想，這對四六那邊的負荷都太重了。哪怕操作板瞬間損壞也不奇怪。
- Cũ: Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\nĐến mức dù \x%l操作板;#00ffc040;thẻ bảng%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ.
- Mới: Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\nĐến mức dù \x%l操作板;#00ffc040;máy tính bảng%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ.
- Thuật ngữ đã quyết: 操作板="máy tính bảng".

### 2728 — monologue (thuật ngữ)

- JP: 電車区長の一喝と、その一言とに鎮まります。
- TW: 而電車段長只用一聲大喝就把他們鎮住了。
- Cũ: Đã bị dập tắt bởi tiếng quát và một lời nói của Đoạn trưởng xe điện.
- Mới: Đã bị dập tắt bởi tiếng quát và một lời nói của Trưởng khu tàu điện.
- Nhất quán nội bộ file: 電車区長="Trưởng khu tàu điện" (10 dòng trong file dùng dạng này; chỉ 3 dòng 2728/2809/2810 dùng "Đoạn trưởng xe điện").

### 2796 — monologue (thuật ngữ)

- JP: 強盗塊太とさえも呼ばれる、アクの強い男ですが……\nあるいは真に相談すべきは、先輩よりもむしろ――
- TW: 雖然他很有個性，甚至被別人取了個外號叫強盜慶太……但是，或許我應該商量的人，不是前輩，而是——
- Cũ: Một gã đàn ông mạnh mẽ, thậm chí còn bị gọi là Cường Đạo Khối Thái......\nNhưng có lẽ người tôi thực sự nên bàn bạc, không phải là tiền bối mà là――
- Mới: Một gã đàn ông mạnh mẽ, thậm chí còn bị gọi là Cường Đạo Kaita......\nNhưng có lẽ người tôi thực sự nên bàn bạc, không phải là tiền bối mà là――
- Tên riêng: biệt danh 強盗塊太 → "Cường Đạo Kaita" (nhất quán với 2550 "Goto Kaita"; TW 強盜慶太 thua JP ruby かいた).

### 2809 — monologue (thuật ngữ)

- JP: 電車区長が見回すと、何人かの職員が目を逸します。\nいい反応ではありません、急ぎ言葉を継ぎ足します。
- TW: 電車段長環視四周，好幾名職員移開視線。這並不算良好的反應，我趕緊補充說道。
- Cũ: Khi Đoạn trưởng xe điện đảo mắt nhìn quanh, một vài nhân viên đã lảng tránh ánh mắt ông.\nĐó không phải là một phản ứng tốt, tôi vội vàng nói tiếp.
- Mới: Khi Trưởng khu tàu điện đảo mắt nhìn quanh, một vài nhân viên đã lảng tránh ánh mắt ông.\nĐó không phải là một phản ứng tốt, tôi vội vàng nói tiếp.
- Nhất quán nội bộ file: 電車区長="Trưởng khu tàu điện" (như 2728).

### 2810 — monologue (thuật ngữ)

- JP: 渡した署名に、電車区長の目が注がれます。\nその口元が、ふ、と緩みます。
- TW: 電車段長看著我遞給他的署名。他的嘴角忽然露出一絲笑容。
- Cũ: Ánh mắt của Đoạn trưởng xe điện đổ dồn vào tờ giấy có chữ ký mà tôi vừa đưa.\nKhóe miệng ông ấy, khẽ nhếch lên.
- Mới: Ánh mắt của Trưởng khu tàu điện đổ dồn vào tờ giấy có chữ ký mà tôi vừa đưa.\nKhóe miệng ông ấy, khẽ nhếch lên.
- Nhất quán nội bộ file: 電車区長="Trưởng khu tàu điện" (như 2728).

### 2815 — monologue (thuật ngữ)

- JP: 運転体の小さな体が、大きく、大きく頷きます。
- TW: 駕駛體小小的身體，用力地點點頭。
- Cũ: Cơ thể nhỏ bé của \x%l運転体;#00ffc040;kíp lái%l;#;, gật đầu thật mạnh, thật mạnh.
- Mới: Cơ thể nhỏ bé của \x%l運転体;#00ffc040;thân vận hành%l;#;, gật đầu thật mạnh, thật mạnh.
- Thuật ngữ đã quyết: 運転体="thân vận hành".


## Khối TOML (đã parse-kiểm chứng: 44 khóa, 0 sai lệch giá trị)

```toml
1244 = "「——Ư——ư——hít――――hà!」"
1247 = "「——\\x%l整備体;#00ffc040;Thân bảo trì%l;#; thì, tôi nghĩ chỉ còn cách từ bỏ thôi.」"
1261 = "「Là toàn bộ con bài trong tay của 'Phía Teitetsu' đấy.」"
1265 = "「Ư」"
1285 = "「……Về \\x%l運転体;#00ffc040;thân vận hành%l;#; thì,\\nđang có người đề nghị giao dịch.」"
1639 = "「Đã lược bỏ việc xác nhận hoạt động. Kết quả là, bên trong \\x%l運転鞄;#00ffc040;túi công tác%l;#;,\\nchứa một mô hình kích thước người thật của \\x%l運転体;#00ffc040;thân vận hành%l;#;.」"
1731 = "「Ư!!!」"
1743 = "「Ư!」"
1746 = "「Ư!!!」"
1748 = "「Ư!? Đây là?」"
1757 = "「Ư!!!!」"
1768 = "「Ừm. Chuyện đó thì ngay từ đầu em đã biết rồi.\\n\\x%l整備体;#00ffc040;Thân bảo trì%l;#; có quá nhiều bộ phận nhận diện cá thể.」"
1819 = "「Đúng vậy. Đó chính là ý chí của Teitetsu——à không,\\ncủa quốc gia, và của nước Minh Quốc đấy.」"
1828 = "「“Giải thể Teitetsu” mà Teitetsu——nước Minh Quốc nói đến,\\nnói cách khác, có nghĩa là giải thể toàn bộ toa xe phải không?」"
1847 = "「Dừng lại đi Goto!!!」"
1902 = "「Cơ thể này. \\x%l整備体;#00ffc040;Thân bảo trì%l;#; này.\\nĐến ngày mai là, sẽ biến mất đúng không?」"
1918 = "「Vì vậy, còn lại là \\x%l操作板;#00ffc040;máy tính bảng%l;#;.\\nChỉ cần giải quyết được \\x%l操作板;#00ffc040;máy tính bảng%l;#; thì.」"
1978 = "「Cái đó là tùy ý. Dù là theo thứ tự \\x%l運転体;#00ffc040;thân vận hành%l;#; - \\x%l整備体;#00ffc040;thân bảo trì%l;#;,\\nhay ngược lại cũng không sao. Vì kết quả đều giống nhau mà.」"
2011 = "「Nếu đã làm đến mức đó——thì anh Goto,\\ntại sao lại không cứu cả \\x%l操作板;#00ffc040;máy tính bảng%l;#;?」"
2024 = "「Tất nhiên là được rồi. Tôi mở \\x%l運転鞄;#00ffc040;túi công tác%l;#; ra nhé.」"
2041 = "「Toa xe, \\x%l運転体;#00ffc040;thân vận hành%l;#; Railord, \\x%l整備体;#00ffc040;thân bảo trì%l;#; Railord.\\nTrước tiên, họ sẽ xác nhận xem tất cả những thứ đó có đầy đủ hay không.」"
2054 = "「Kết quả là, một \\x%l運転体;#00ffc040;thân vận hành%l;#; trống rỗng đã bị bỏ lại.\\nMột \\x%l運転体;#00ffc040;thân vận hành%l;#; không có \\x%l操作板;#00ffc040;máy tính bảng%l;#;, không có \\x%l整備体;#00ffc040;thân bảo trì%l;#; cũng không có toa xe.」"
2061 = "「\\x%l運転体;#00ffc040;Thân vận hành%l;#; và \\x%l操作板;#00ffc040;máy tính bảng%l;#;. Chỉ cần bảo vệ được tối thiểu những thứ đó.」"
2110 = "「Đây là chữ ký của 338 nhân viên Teitetsu hiện tại.\\nVà, đây là bản đề xuất mục đích.」"
2114 = "「Ư!!!」"
2115 = "「Ư!!!?」"
2150 = "「Nếu vậy! Railord của anh Goto,\\nchỉ cứu được mỗi \\x%l運転体;#00ffc040;thân vận hành%l;#; thôi sao?」"
2151 = "「Nếu vậy,\\n\\x%l操作板;#00ffc040;máy tính bảng%l;#; sau khi xác nhận hoạt động xong, sẽ để nguyên như thế à?」"
2152 = "「Railord tự mình ném \\x%l操作板;#00ffc040;máy tính bảng%l;#; ra bên ngoài.\\n\\x%l機関助士;#00ffc040;Phụ lái tàu%l;#;, hoặc kẻ đi lậu vé cũng có thể làm hành động tương tự.」"
2153 = "「Railord thì,\\nsẽ được xác nhận hoạt động thông qua việc hoán đổi \\x%l操作板;#00ffc040;máy tính bảng%l;#;.」"
2175 = "「Nếu là \\x%l運転体;#00ffc040;thân vận hành%l;#; thì, bộ phận nhận diện cá thể rất ít.\\nNếu nhờ những người ở bộ phận cơ khí Railord thì.」"
2364 = "Có lẽ em ấy đã kết nối \\x%l共感;#00ffc040;cộng cảm%l;#; ngay lập tức.\\nCơ thể Niiroku bỗng trở nên ấm áp——Ư!!?"
2411 = "Là một \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; và Railord tuyệt vời đến thế cơ mà.\\nNếu tùy cơ ứng biến, và thu hồi được cả \\x%l操作板;#00ffc040;máy tính bảng%l;#; của Shiro thì——"
2550 = "Goto Kaita――\\nTrong số những người cùng thời, không ai khó đối phó bằng cậu ta."
2592 = "Nhìn quanh, vô số ánh mắt đáp lại tôi.\\nCủa những người thuộc Kokura――không nói quá đâu, là của toàn bộ lái tàu và thợ lái đầu máy."
2594 = "Từ chính diện, sâu bên trong, cổ họng. Dùng ngón cái ấn mạnh vào đó.\\nDù là \\x%l運転体;#00ffc040;thân vận hành%l;#; hay \\x%l整備体;#00ffc040;thân bảo trì%l;#;, cũng không có gì khác biệt."
2603 = "Tôi lục lọi trong \\x%l運転士鞄;#00ffc040;túi công tác%l;#;."
2624 = "\\x%l操作板;#00ffc040;Máy tính bảng%l;#; của Shiro, vào \\x%l運転体;#00ffc040;thân vận hành%l;#; mô hình trống rỗng,\\nvà sau đó, là vào \\x%l整備体;#00ffc040;thân bảo trì%l;#; của Niiroku."
2673 = "Dù nghĩ thế nào, thì cũng quá sức chịu đựng.\\nĐến mức dù \\x%l操作板;#00ffc040;máy tính bảng%l;#; có bị phá hủy ngay tức khắc, thì cũng không có gì lạ."
2728 = "Đã bị dập tắt bởi tiếng quát và một lời nói của Trưởng khu tàu điện."
2796 = "Một gã đàn ông mạnh mẽ, thậm chí còn bị gọi là Cường Đạo Kaita......\\nNhưng có lẽ người tôi thực sự nên bàn bạc, không phải là tiền bối mà là――"
2809 = "Khi Trưởng khu tàu điện đảo mắt nhìn quanh, một vài nhân viên đã lảng tránh ánh mắt ông.\\nĐó không phải là một phản ứng tốt, tôi vội vàng nói tiếp."
2810 = "Ánh mắt của Trưởng khu tàu điện đổ dồn vào tờ giấy có chữ ký mà tôi vừa đưa.\\nKhóe miệng ông ấy, khẽ nhếch lên."
2815 = "Cơ thể nhỏ bé của \\x%l運転体;#00ffc040;thân vận hành%l;#;, gật đầu thật mạnh, thật mạnh."
```

## Kết bài

File ニイロク04_終端: 452 dòng đã đọc hết, 44 dòng sai (9,7%) — toàn bộ là thuật ngữ đã quyết (34 dòng, trong đó 3 dòng sửa cả term trong tag %l cho khớp JP) và gasp っ (10 dòng, gồm 1 mục sweep bỏ sót). Không lệch vị trí, không xoay vòng, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Soutetsu không xuất hiện trong file nên không có sửa đại từ nào. Lượt soát 2: 44/44 tái kiểm chứng, 0 bỏ, 0 sửa. Không có câu hỏi mở cần Hieu quyết.
