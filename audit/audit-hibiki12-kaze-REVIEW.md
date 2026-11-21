# Audit — 日々姫12_風.txt.toml

- File: `日々姫12_風.txt.toml` — route 02_Hibiki, 371 dòng script (66 thoại Soutetsu, 58 thoại Hibiki, 160 độc thoại, 15 Paulette, 15 Kisaki, 14 Mayami, 12 幼女, 8 Fukami, 7 Hachiroku, 7 Reina, 7 Nagi, 1 学園生Ａ, 1 学園生Ｂ).
- Nội dung: phương án A (họa tiết đồng hồ quả lắc của Hibiki) thắng phiếu bình chọn màu sơn toa xe; cả nhóm ra ngoài, Soutetsu và Hibiki nắm tay đi dạo đêm tới lò rèn Minokasa; hôm sau ở Rail Shop: Hibiki vẽ sa bàn N-gauge, giúp bé gái sửa mô hình nhà bị hỏng hồ dán; thay giá chuyển hướng (台車) cho toa hành khách mới ở xưởng đầu máy bằng đá; Kisaki xuất hiện, mời Hibiki dự buổi tranh luận về triển vọng phục hồi kinh tế Ohitoyo.
- **Kết quả: 16/371 dòng sai (4,3%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (371 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML: 371/371 khóa trùng khớp, 0 lệch thực chất — 212 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng (đã biết, không phải lỗi); 1 dòng (2186) khớp tuyệt đối. `[selections]` rỗng. Không có thẻ `%l` nào lệch (0 dòng mất cân bằng thẻ); không có thẻ VN tự thêm; không có ký tự JP lạc ngoài thẻ (chỉ 1 dấu ー ở 2013, là dấu kéo dài âm trong VN, giữ nguyên).
- TOML md5 `1fc7a9a1387d671263eb40405ed613db`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Sweep gasp: 0 mục cho file này trong `sweep-raw-gasp-wrong.json` (đã kiểm tra trực tiếp, không phải suy đoán). Quét tay bổ sung toàn file: không có gasp nào bị mất — mọi っ đều đã được diễn ("Phù" 2885, "ơ" 2075/2576, "Ô!?" 2048, "Ưm…ưm" 2076) hoặc đúng quy tắc không thêm Ư (っ nhấn mạnh cuối câu gắn với từ nội dung: 2087, 2111; ばいっ 2186/1994).
- Đại từ đã kiểm chứng toàn file: Soutetsu "anh" với Hibiki đúng (1985, 2398, 2396, 2242 — kể cả "hai anh em mình" 2242); "tôi" với Kisaki đúng (1973, 2227, 2177); "em" trong các dòng Soutetsu đều là Hibiki ở vị trí người nghe, không phải tự xưng (1971, 1978, 1985, 1992, 2242); độc thoại "tôi" xuyên suốt, 0 dòng "mình" làm chủ ngữ (7 lần "mình" đều là sở hữu/phản thân: 2689, 2783, 2664, 2581, 2738, 2660, 2984). Kisaki tự xưng "tôi" toàn file (bối cảnh công việc — lời mời tranh luận, đúng quy tắc theo ngữ cảnh); gọi Soutetsu bằng tên trần "Soutetsu" đúng (2027). Mayami xưng "em" với Soutetsu đúng (2292); Hachiroku gọi Mayami "cô" đúng (2294); Nagi gọi Soutetsu "anh" đúng (1969, 1957, 2419); Reina gọi "anh Soutetsu" đúng (2352); Hibiki xưng "em"/"chị" với bé gái đúng (1990, 2012, 2111, 2129, 2380); Fukami gọi Hibiki "chị Hibiki" theo chuẩn dự án (xem 2161).
- Thuật ngữ đúng sẵn có: エアクラ "Aircra" (2794); 列車 gloss "đoàn tàu" (2779); 石造機関庫 "xưởng đầu máy bằng đá"; 台車 "giá chuyển hướng"; 客車 "toa hành khách"; 知知武鉄道 "Đường sắt Chichibu" (2897, 2376); 宮司 "Đền chủ Akai" (2908); KiHa 07 giữ nguyên.

## §2. Danh sách sửa (16 dòng)

Phân loại: thuật ngữ 8 (2218, 1949, 2396, 1723, 3064, 2301, 2178, 2294), xưng hô 2 (2415, 2161), sai nghĩa 2 (2116, 2333), lỗi nhỏ 4 (2391, 2315, 2256, 2067).

### 2415 — ポーレット — xưng hô
- JP: 「双鉄くんなら、[ハチロク,3]8620ですよね？\n見えるのは、車窓じゃなくて[キャブ,2]運転席からの景色」
- TW: 「雙鐵君你不是要開[八六,3]８６２０嗎？到時候你能看見的可不是車窗外的景色而只是駕駛座外的景色了啊」
- VN cũ: 「Nếu là Sou-chan thì sẽ ở trên 8620 đúng không?
Thứ anh nhìn thấy sẽ không phải là khung cảnh ngoài cửa sổ toa tàu, mà là khung cảnh từ buồng lái cơ.」
- Sửa: 「Nếu là anh Soutetsu thì sẽ ở trên 8620 đúng không?
Thứ anh nhìn thấy sẽ không phải là khung cảnh ngoài cửa sổ toa tàu, mà là khung cảnh từ buồng lái cơ.」
- Lý do: Paulette gọi Soutetsu là 双鉄くん → "anh Soutetsu" theo khóa B4 (không có ngoại lệ moan). "Sou-chan" là cách gọi của Minokasa (双鉄くん của ông lão dịch "Sou-chan"), không phải của Paulette.

### 2116 — 稀咲 — sai nghĩa
- JP: 「しあさって――投票日の三日前。\n午後五時からでどうだろう」
- TW: 「大後天——投票日的三天前。下午五點開始怎麼樣」
- VN cũ: 「Ngày kìa——ba ngày trước ngày bỏ phiếu.
Từ 5 giờ chiều thì sao?」
- Sửa: 「Ngày kia——ba ngày trước ngày bỏ phiếu.
Từ 5 giờ chiều thì sao?」
- Lý do: JP しあさって = ngày kia (ngày mốt); TW 大後天 xác nhận. "Ngày kìa" sai nghĩa (kìa là chỉ định xa, không phải "ngày kia").

### 2161 — ふかみ — xưng hô
- JP: 「お出かけするの。きっと、気分転換とか、\nなるんじゃないかって思う。です」
- TW: 「我想出門去逛逛肯定可以調節一下心情。嗯」
- VN cũ: 「Ra ngoài đi dạo một chút. Chắc chắn sẽ giúp cậu
thay đổi tâm trạng đấy. Nhỉ.」
- Sửa: 「Ra ngoài đi dạo một chút. Chắc chắn sẽ giúp chị
thay đổi tâm trạng đấy. Nhỉ.」
- Lý do: Fukami nói về/với Hibiki (người đi dạo giải tỏa tâm trạng). Toàn dự án Fukami gọi Hibiki là "chị Hibiki" (30 dòng, vd. lr_日々姫ふかみh1 1662/1635/1509, 日々姫08 2446) — "cậu" phá chuẩn xưng hô của cặp này.

### 2333 — ふかみ — sai nghĩa
- JP: 「舟にも、日々姫さんのデザインと合せた中敷きみたいの。\n敷いたら、きっと、お客さん増えそう。かも、です」
- TW: 「船上鋪的墊子似乎也採用了符合日日姬小姐設計的風格。鋪上的話來的客人肯定也會更多吧，說不定」
- VN cũ: 「Trên thuyền cũng nên lót đệm,
theo thiết kế của Hibiki. Nếu làm vậy, chắc chắn lượng khách sẽ tăng lên. Nhỉ.」
- Sửa: 「Trên thuyền cũng nên lót đệm,
theo thiết kế của Hibiki. Nếu làm vậy, có lẽ lượng khách sẽ tăng lên đấy.」
- Lý do: JP きっと…かも = phỏng đoán có dè dặt ("có lẽ"); VN cũ "chắc chắn… Nhỉ." tự mâu thuẫn — khẳng định tuyệt đối rồi lại nghi vấn.

### 2218 — 双鉄 — thuật ngữ
- JP: 「日々姫は御一夜を、どんな町へと育てたいんだ？」
- TW: 「日日姬想把御一夜發展成一個怎樣的城市呢？」
- VN cũ: 「Hibiki muốn phát triển Ohimitera thành một thị trấn như thế nào?」
- Sửa: 「Hibiki muốn phát triển Ohitoyo thành một thị trấn như thế nào?」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11 (không "Ohimitera").

### 1949 — 日々姫 — thuật ngữ
- JP: 「“みんな”だなんて考えちゃうとわからなくなるから、\n私にとって、理想の御一夜を作りたいって思います」
- TW: 「一想到“大家”我就腦袋裡一片空白了，所以我現在只是想把御一夜弄成我理想中的樣子」
- VN cũ: 「Cứ nghĩ đến "tất cả mọi người" là em lại thấy bối rối,
nên em muốn tạo ra một Ohimitera lý tưởng đối với bản thân em.」
- Sửa: 「Cứ nghĩ đến "tất cả mọi người" là em lại thấy bối rối,
nên em muốn tạo ra một Ohitoyo lý tưởng đối với bản thân em.」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11.

### 2396 — 双鉄 — thuật ngữ
- JP: 「では、質問を改めよう。\n日々姫の理想の御一夜は、どんな町なのだ？」
- TW: 「那我就換個問題吧。日日姬理想中的御一夜是一個怎麼樣的城市呢？」
- VN cũ: 「Vậy, anh đổi câu hỏi nhé.
Ohimitera lý tưởng của Hibiki là một thị trấn như thế nào?」
- Sửa: 「Vậy, anh đổi câu hỏi nhé.
Ohitoyo lý tưởng của Hibiki là một thị trấn như thế nào?」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11.

### 1723 — 日々姫 — thuật ngữ
- JP: 「……兄さんが、帝都に帰りたくなくなる町。\nずっと暮らしたくなる御一夜が、私の理想の御一夜です」
- TW: 「……讓哥哥不想再回帝都的城市，讓你想一直住下去的御一夜就是我理想中的御一夜」
- VN cũ: 「……Là thị trấn khiến anh không còn muốn quay về Đế đô nữa.
Một Ohimitera khiến anh muốn sống ở đây mãi mãi, đó là Ohimitera lý tưởng của em.」
- Sửa: 「……Là thị trấn khiến anh không còn muốn quay về Đế đô nữa.
Một Ohitoyo khiến anh muốn sống ở đây mãi mãi, đó là Ohitoyo lý tưởng của em.」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11 (2 chỗ trong dòng này).

### 3064 — monologue — thuật ngữ
- JP: 御一夜市内を遥かに外れ。
- TW: 那裡是離御一夜市中心很遙遠的郊外。
- VN cũ: Nằm cách xa trung tâm thành phố Ohimitera.
- Sửa: Nằm cách xa trung tâm thành phố Ohitoyo.
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11.

### 2301 — 双鉄 — thuật ngữ
- JP: 「さすが、御一夜の職人だな。\n鉄道車体の塗装など、恐らくは初めての経験だろうに」
- TW: 「真不愧是御一夜的工匠們啊。他們明明應該也是第一次給火車的車體塗裝的」
- VN cũ: 「Quả không hổ danh là nghệ nhân của Ohimitera.
Dù có lẽ đây là lần đầu tiên họ sơn thân xe đường sắt.」
- Sửa: 「Quả không hổ danh là nghệ nhân của Ohitoyo.
Dù có lẽ đây là lần đầu tiên họ sơn thân xe đường sắt.」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11.

### 2178 — 稀咲 — thuật ngữ
- JP: 「候補者同士、直接に語り合うのも良いかと思って。\nテーマは『御一夜の経済再生への展望』でどうかな？」
- TW: 「我覺得候選人之間或許可以來一次直接對話。主題就定為“對御一夜經濟再興的展望”，怎麼樣？」
- VN cũ: 「Tôi nghĩ các ứng cử viên nên có một buổi trò chuyện trực tiếp với nhau.
Chủ đề là 『Triển vọng phục hồi kinh tế Ohimitera』 thì sao?」
- Sửa: 「Tôi nghĩ các ứng cử viên nên có một buổi trò chuyện trực tiếp với nhau.
Chủ đề là 『Triển vọng phục hồi kinh tế Ohitoyo』 thì sao?」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11.

### 2294 — ハチロク — thuật ngữ
- JP: 「もちろんです、真闇様。不燃木材、不燃モケットは、\n\x%l帝鉄;#00ffc040;帝鉄%l;#;全盛期の頃に、既に一般化されておりますので」
- TW: 「當然了，真闇小姐。阻燃木材、阻燃絨墊在\x%l帝鉄;#00ffc040;帝國鐵路%l;#;全盛期的時候就已經普及化了」
- VN cũ: 「Tất nhiên rồi ạ, cô Mayami. Gỗ chống cháy và nỉ bọc ghế chống cháy
đã được phổ biến từ thời kỳ hoàng kim của \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; rồi ạ.」
- Sửa: 「Tất nhiên rồi ạ, cô Mayami. Gỗ chống cháy và nỉ bọc ghế chống cháy
đã được phổ biến từ thời kỳ hoàng kim của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; rồi ạ.」
- Lý do: Gloss %l của 帝鉄 → "Teitetsu" dạng ngắn theo quy tắc đã chốt ("Đường sắt Hoàng gia" sai — Hoàng gia ≠ Đế quốc; dạng đầy đủ "Đường sắt Đế quốc" chỉ ở tooltip lần đầu tiên, đã qua từ lâu). Tiền lệ: một file đã merge sửa đúng gloss này (key 2182).

### 2391 — ふかみ — lỗi nhỏ
- JP: 「あの、わたしも。Ａに一票。です」
- TW: 「那我也，給Ａ，投一票。嗯」
- VN cũ: 「Ừm, mình cũng vậy. Bỏ một phiếu cho A. Ạ.」
- Sửa: 「Ừm, mình cũng vậy. Bỏ một phiếu cho A ạ.」
- Lý do: です cuối câu của Fukami đứng một mình thành câu "Ạ." — "ạ" là tiểu từ cuối câu, không đứng thành câu riêng; gộp vào câu trước. Tiền lệ: 3 file đã merge tính đây là lỗi nhỏ (vd. 1346/1534, 2581/2602/2920, 998/1326/1358/1527/1601).

### 2315 — ふかみ — lỗi nhỏ
- JP: 「せ、\x%l石造機関庫;#00ffc040;石造機関庫%l;#;では、今走っている\x%l客車;#00ffc040;客車%l;#;の実物。\n組み立ててるとこ、生で見学できます。です」
- TW: 「石、\x%l石造機関庫;#00ffc040;石製機車庫%l;#;裡可以親眼看到現在實際運營中的\x%l客車;#00ffc040;客運車廂%l;#;實物的組裝場面。嗯」
- VN cũ: 「Ở, \\x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#;, các bạn có thể tận mắt chứng kiến quá trình lắp ráp
\\x%l客車;#00ffc040;toa hành khách%l;#; thật đang hoạt động hiện nay. Ạ.」
- Sửa: 「Ở, \\x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#;, các bạn có thể tận mắt chứng kiến quá trình lắp ráp
\\x%l客車;#00ffc040;toa hành khách%l;#; thật đang hoạt động hiện nay ạ.」
- Lý do: です cuối câu của Fukami đứng một mình thành câu "Ạ." — gộp "ạ" vào câu trước (như 2391).

### 2256 — ふかみ — lỗi nhỏ
- JP: 「そう。です。本物。乗れるようになるのは、\n完成して、テストとか終わってから。ですけど」
- TW: 「是的。真的。雖然要乘上去還得等完成後測試完，才行」
- VN cũ: 「Đúng. Vậy ạ. Đồ thật. Nhưng mà phải đợi lắp ráp xong,
kiểm tra các kiểu xong xuôi thì mới ngồi lên được. Ạ.」
- Sửa: 「Đúng. Vậy ạ. Đồ thật. Nhưng mà phải đợi lắp ráp xong,
kiểm tra các kiểu xong xuôi thì mới ngồi lên được ạ.」
- Lý do: です cuối câu của Fukami đứng một mình thành câu "Ạ." — gộp "ạ" vào câu trước (như 2391).

### 2067 — ふかみ — lỗi nhỏ
- JP: 「あ。こっち――。です」
- TW: 「啊，在這邊。嗯」
- VN cũ: 「A. Bên này——. Ạ.」
- Sửa: 「A. Bên này—— ạ.」
- Lý do: です cuối câu của Fukami đứng một mình thành câu "Ạ." — gộp "ạ" vào câu trước (như 2391).

## §3. Các dòng đã kiểm tra và giữ nguyên (đáng chú ý)

- Key 2418: Soutetsu "anh" trong câu nói với cả nhóm (Hachiroku, Mayami, Paulette, Reina, Fukami, Nagi) — giữ nguyên, cờ mơ hồ (xem §6). Nhóm hỗn hợp, đa số là phía "anh" (4/6), không đủ căn cứ đổi sang "tôi"; tiền lệ parent gần nhất: 5 dòng đại từ mơ hồ trong cảnh nhóm giữ nguyên, không quyết.
- Key 2083: 「ああ」→"Ra vậy." — giữ: cách diễn đạt tự nhiên cho tiếng thừa nhận, không sai nghĩa.
- Key 2100: ふっふーん→"Hư hư." — giữ: diễn được vẻ đắc ý của Nagi; không phải tiếng cười cần sửa thành "Fufu".
- Key 2031: きゃあ！→"Kyaa!" — giữ: romanisation cho tiếng hét ngạc nhiên, đúng quy tắc (không phải dòng rên).
- Key 2047: 幼女 ぅ……ん……→"Ư……vâng……" — giữ: ん diễn thành "vâng" (đồng ý) là hợp lý trong ngữ cảnh bé gái gật đầu làm theo.
- Key 2223/2169/1961/2167/2116: Kisaki tự xưng "tôi" toàn cảnh — giữ: cảnh mời tranh luận là bối cảnh công việc/quyết đoán theo quy tắc theo ngữ cảnh; đổi một dòng sang "em" sẽ phá nhất quán trong cảnh.
- Key 2076: んっ→"ưm"; 2885: ほぉっ→"Phù"; 2036: えへへっ→"Ehehe" — giữ: các tiếng っ đã được diễn hoặc là tiếng cười bị cắt ngắn, không thuộc diện gasp cần thêm Ư.
- Key 2391/2315/2256/2067 đã sửa (xem §2); các "ạ" gắn cuối câu khác trong file đều đúng vị trí (2257, 2294, 2297, 1955, 2006).
- 27 cặp VN trùng trong file với JP khác nhau không phát hiện — các câu ngắn lặp ("Vâng!", "Ừm!", "Ồ.") đều là câu xã giao chung, không phải nhiễm chéo.

## §4. Lượt soát 2

- Lượt soát 2: 16/16 fix đọc lại đối chiếu JP (+TW) — 16 giữ nguyên, 0 bỏ, 0 sửa. (Lượt soát có xét lại 2418: giữ "anh", cờ mơ hồ; 2294: giữ "Teitetsu" theo quy tắc dạng ngắn + tiền lệ key 2182; 2161: giữ "chị" theo 30 dòng tiền lệ toàn dự án.)

## §5. Khối TOML (đã parse-kiểm chứng: 16 khóa, 0 sai lệch)

```toml
[script]
"2415" = "「Nếu là anh Soutetsu thì sẽ ở trên 8620 đúng không?\\\\nThứ anh nhìn thấy sẽ không phải là khung cảnh ngoài cửa sổ toa tàu, mà là khung cảnh từ buồng lái cơ.」"
"2116" = "「Ngày kia——ba ngày trước ngày bỏ phiếu.\\\\nTừ 5 giờ chiều thì sao?」"
"2161" = "「Ra ngoài đi dạo một chút. Chắc chắn sẽ giúp chị\\\\nthay đổi tâm trạng đấy. Nhỉ.」"
"2333" = "「Trên thuyền cũng nên lót đệm,\\\\ntheo thiết kế của Hibiki. Nếu làm vậy, có lẽ lượng khách sẽ tăng lên đấy.」"
"2218" = "「Hibiki muốn phát triển Ohitoyo thành một thị trấn như thế nào?」"
"1949" = "「Cứ nghĩ đến \"tất cả mọi người\" là em lại thấy bối rối,\\\\nnên em muốn tạo ra một Ohitoyo lý tưởng đối với bản thân em.」"
"2396" = "「Vậy, anh đổi câu hỏi nhé.\\\\nOhitoyo lý tưởng của Hibiki là một thị trấn như thế nào?」"
"1723" = "「……Là thị trấn khiến anh không còn muốn quay về Đế đô nữa.\\\\nMột Ohitoyo khiến anh muốn sống ở đây mãi mãi, đó là Ohitoyo lý tưởng của em.」"
"3064" = "Nằm cách xa trung tâm thành phố Ohitoyo."
"2301" = "「Quả không hổ danh là nghệ nhân của Ohitoyo.\\\\nDù có lẽ đây là lần đầu tiên họ sơn thân xe đường sắt.」"
"2178" = "「Tôi nghĩ các ứng cử viên nên có một buổi trò chuyện trực tiếp với nhau.\\\\nChủ đề là 『Triển vọng phục hồi kinh tế Ohitoyo』 thì sao?」"
"2294" = "「Tất nhiên rồi ạ, cô Mayami. Gỗ chống cháy và nỉ bọc ghế chống cháy\\\\nđã được phổ biến từ thời kỳ hoàng kim của \\\\x%l帝鉄;#00ffc040;Teitetsu%l;#; rồi ạ.」"
"2391" = "「Ừm, mình cũng vậy. Bỏ một phiếu cho A ạ.」"
"2315" = "「Ở, \\\\x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#;, các bạn có thể tận mắt chứng kiến quá trình lắp ráp\\\\n\\\\x%l客車;#00ffc040;toa hành khách%l;#; thật đang hoạt động hiện nay ạ.」"
"2256" = "「Đúng. Vậy ạ. Đồ thật. Nhưng mà phải đợi lắp ráp xong,\\\\nkiểm tra các kiểu xong xuôi thì mới ngồi lên được ạ.」"
"2067" = "「A. Bên này—— ạ.」"
```

## §6. Chờ Hieu (không tự quyết)

1. Key 2279 — 湯医線 "Tuyến Yui": giữ nguyên theo thông lệ mới nhất (file merge 22/11 ~01:35 kê "Tuyến Yui" vào cờ đợt thống nhất). Quyết định Yui/Yunoi vẫn chờ Hieu — đổi ở đợt thống nhất, không sửa trong audit này.
2. Key 2908 — 毛利の姫様 → "Denshahime của Mouri": giữ nguyên, cờ đợt thống nhất. Tiền lệ: một file đã merge kê đúng mẫu này (JP 毛利の姫 → "Denshahime") vào cờ thống nhất. Cần Hieu quyết: 毛利の姫様 có phải là 電車姫 không (→ "Công chúa Tàu điện của Mouri") hay là tiểu thư/công chúa nhà Mouri (→ "Tiểu thư Mouri"/"Công chúa Mouri")?
3. Key 2701 — gloss 運転体 "thân chính": giữ nguyên, cờ đợt thống nhất. Đề xuất "thân vận hành" theo quy tắc 運転ボディ đã chốt, nhưng toàn dự án 運転体 đang dùng "kíp lái" 26 dòng — cần quyết thống nhất một chuẩn cho 運転体 trước khi sửa.
4. Key 2418 — Soutetsu "anh" trong câu nói với cả nhóm (Hachiroku + Mayami + Paulette + Reina + Fukami + Nagi): giữ nguyên "anh", cờ mơ hồ. Nhóm hỗn hợp cả hai phía; không đủ căn cứ đổi sang "tôi".
5. B19 vẫn park (không liên quan file này).

## Kết bài

File 日々姫12_風 đã audit xong toàn bộ 371 dòng: 16 dòng sai (4,3%) — 8 thuật ngữ (7 "Ohimitera"→"Ohitoyo" + 1 gloss 帝鉄→"Teitetsu"), 2 xưng hô (2415 "Sou-chan"→"anh Soutetsu" theo khóa B4; 2161 Fukami→Hibiki "cậu"→"chị"), 2 sai nghĩa (2116 "Ngày kìa"→"Ngày kia"; 2333 "chắc chắn… Nhỉ."→"có lẽ… đấy."), 4 lỗi nhỏ ("Ạ." đứng riêng câu của Fukami → gộp "ạ" vào câu trước). Không lệch dòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 16 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 16/16, 0 bỏ, 0 sửa. Chờ Hieu: "Tuyến Yui" (2279), "Denshahime của Mouri" (2908), gloss 運転体 "thân chính" (2701), đại từ nhóm mơ hồ (2418).