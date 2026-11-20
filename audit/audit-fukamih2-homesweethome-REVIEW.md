# Audit ふかみh2 — ふかみh2_homesweethome.txt.toml

**Ngày kiểm toán:** 21/11/2026
**Tệp TOML:** `07_Nagi_Fukami/#U3075#U304b#U307fh2_homesweethome.txt.toml` — md5 `5dee3edcf2470621aa4f3b78c9c0a43b`, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 copy trong 227 tệp TOML; 11 nhóm trùng của dự án không chứa file này).
**Nguồn CSV:** "Trang tính 3" — **BẪY dual-set (đã tránh):** CSV3 có HAI bộ hàng cho file này, mỗi bộ 301 hàng, cùng dải key 736–1776. Bộ ghi thư mục `07_Nagi_Fukami` là STALE (khớp phẳng với TOML chỉ 12/301; JP khác bộ tốt ở 217/301 hàng); bộ ghi thư mục `11_Other` là bộ tốt (khớp phẳng 301/301) — audit CHỈ dùng bộ `11_Other`. Hàng đợi ghi 602 dòng là tổng hai bộ, không phải số dòng thực của file.
**Cơ sở totals (đã rebase):** ROUTE-AUDIT.md hiện tại là **135/6.178** (file lr_mikuro gộp lúc ~01:10 trong khi audit này đang chạy) — khác cơ sở 134/6.096 trong lệnh giao; snippet dùng số mới 135/6.178 + 22 = 136/6.200.
**Kết quả: 22/301 dòng sai (7,3%), 1 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Gasp っ bị mất | 9 |
| Đại từ độc thoại "anh"→"tôi" (người kể Soutetsu) | 5 |
| Đếm nguyên âm SFX dài | 2 |
| Đại từ thoại Soutetsu "mình"→"anh" | 1 |
| Raw っ còn trong VN | 1 |
| Dịch sai nghĩa (giải phẫu: 膣→tử cung) | 1 |
| SFX sai từ (tiếng lắc đầu dịch thành tiếng đâm) | 1 |
| Thuật ngữ không nhất quán (おまんこ "Cô bé") | 1 |
| Âm bị mất hẳn (はっ) | 1 |
| **Tổng** | **22** |

**Theo loại dòng:** thoại 9/143 sai (6,3%), độc thoại 13/158 sai (8,2%). **Theo nhân vật:** ふかみ (Fukami) 5/86, 双鉄H (Soutetsu) 4/55, monologue 13/158, 日々姫 (Hibiki) 0/2.

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng. Lỗi tập trung ở ba nhóm: (1) độc thoại người kể Soutetsu dùng "anh" thay vì "tôi" ở 5 dòng rải rác (1455, 1461, 1564, 1641, 1660); (2) gasp っ bị mất ở 9 dòng + 1 dòng còn raw っ trong VN (1442); (3) các lỗi rời rạc: đếm nguyên âm SFX dài sai 2 dòng, 1 lỗi giải phẫu (1116), 1 SFX sai từ (1562), 1 thuật ngữ không nhất quán (1579), 1 âm はっ bị mất (1776), 1 đại từ thoại (1759). Không có lỗi hệ thống lớn như file lr_ふかみh2 (52 lỗi, 13 đại từ + 24 fa/fu): file này thoại Soutetsu đã dùng đúng "anh" với Fukami, fa/fu đều giữ âm f (chỉ còn dạng cũ chờ thống nhất).

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `5dee3edcf2470621aa4f3b78c9c0a43b`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** bộ tốt `11_Other` khớp phẳng 301/301 với TOML; bộ stale `07_Nagi_Fukami` chỉ khớp 12/301 — đã loại bỏ, không audit. JP comment trong TOML khớp CSV3 301/301. Giá trị TOML: 135 khớp tuyệt đối + 166 khớp sau khi gộp `\n` thành khoảng trắng, 0 khác biệt thực chất — toàn bộ là hiện tượng gộp `\n` trong TOML-2. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 17 mục (xem §4). Quét bổ sung toàn bộ 194 dòng JP chứa っ: bắt thêm 7 gasp sweep bỏ sót (995, 996, 1007, 1024, 1172, 1520, 1591). Không còn gasp っ trần nào khác bị mất. Lưu ý: sweep dùng JP bộ stale cho 2 mục (736, 1735) — đã đối chiếu lại với JP bộ tốt.
- **Thẻ %l:** JP 4 thẻ (1050 `[とう,1]`, 1073 `[かあ,1]`, 1096 `[みぎたいちしゅぞうもと,5]` + `[とうじ,1]`), VN 0 thẻ — VN bỏ toàn bộ tag glossary (xem §6, không tính sai, chờ quyết).
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng, không có hàng VN == TW, VN == JP duy nhất 736 (「…………」 — JP và VN đều chỉ là dấu ba chấm, đúng). 3 cặp VN trùng trong file: 1024/1167 đều 「!!!」 (sau fix 1024 thành 「Ư!!!」 thì hết trùng; JP khác nhau: 1024 có っ, 1167 không — không phải lệch dòng); 1742/1743 đều "（Phập! Phập! Phập! Phập!）" (hai chuỗi thrust khác nhau cùng dịch gộp thành Phập — không phải lệch dòng); 1746/1750 đều "（Phịch）" (ぽふんっ / くてっ đều là tiếng thịch — không phải lệch dòng). Đối chiếu VN file qua chỉ mục VN toàn dự án (84.385 VN khác nhau): 38 va chạm chéo file, TẤT CẢ đều là cảm thán/SFX ngắn chung chung (「!!」, 「Ừ.」, 「Fukami!」, （Phịch）, （Cạch!）…) — 0 câu thoại đầy đủ nào bị đặt nhầm file, nên 0 nhiễm chéo.
- **Đại từ:** Soutetsu thoại dùng "anh" với Fukami nhất quán — 0 lỗi "tôi" trong thoại (1728 "chúng tôi" là dạng số nhiều, đúng quy tắc nhóm); độc thoại 5/158 dòng dùng "anh" sai (đã sửa — trong file độc thoại dùng "tôi" ở 153/158 dòng); Fukami tự xưng "em" nhất quán, gọi Soutetsu "anh Soutetsu" nhất quán; Hibiki gọi Soutetsu "anh hai", Fukami "bé Fukami" (đúng TW). Nagi không có dòng thoại nào trong file — nhưng key 1118 là bằng chứng then chốt cho quy tắc cùng tuổi (Fukami: Hibiki "tầm tuổi em và bé Nagi") nên không có lỗi "chị"/"em" nào cho cặp Fukami–Nagi.
- **Thuật ngữ đã chốt:** 0 "Ohimitera", 0 "Yui", 0 "Teitetsu" sai dạng, 0 "cô" xưng hô sai. 義母/義父 → "mẹ nuôi"/"bố nuôi" đúng vì TW ghi 養母/養父 (936, 1050, 1073 — theo quy tắc: 義 được dịch "nuôi" khi TW ghi 養). お祖母様 → "bà nội" theo TW 奶奶 (936). 杜氏 → "Toji" nhất quán 2 dòng (1096, 1376) — giữ (xem §5). JP 1448 "凪の部屋" vs TW "深美的房間" — VN theo JP ("Phòng của Nagi"), đúng (JP thắng TW khi mâu thuẫn).

## 3. Các lỗi đã sửa (22 dòng)

### 995 — 双鉄H — gasp
**JP:** 「っ！！」
**TW:** 「唔！！」
**Cũ:** 「!!」
**Mới:** 「Ư!!」
Gasp nguyên dòng — VN chỉ còn dấu câu. Tiền lệ lr_ふかみh2 1068.

### 996 — ふかみ — gasp
**JP:** 「～～～～～～～～っ！！！」
**TW:** 「唔！！！」
**Cũ:** 「~~~~~~~~!!!」
**Mới:** 「~~~~~~~~Ư!!!」
Dấu ~ giữ nguyên, っ bị mất — thêm Ư.

### 1007 — 双鉄H — gasp
**JP:** 「っ！？　ふかみっ――声が大きい」
**TW:** 「唔？！深美，你聲音太大了」
**Cũ:** 「!? Fukami——em nói to quá rồi đấy。」
**Mới:** 「Ư!? Fukami——em nói to quá rồi đấy。」
Gasp đầu dòng っ！？ bị mất hẳn (VN chỉ còn "!?"); TW 唔 xác nhận có tiếng gasp. Bắt được nhờ quét bổ sung (sweep bỏ sót).

### 1024 — 双鉄H — gasp
**JP:** 「っ！！！」
**TW:** 「啊！！！」
**Cũ:** 「!!!」
**Mới:** 「Ư!!!」
Gasp nguyên dòng — VN chỉ còn dấu câu. Sau fix này cặp VN trùng 1024/1167 hết trùng.

### 1044 — ふかみ — vowel-count
**JP:** 「んぷっ！！？　んっ！　ふぉぅぅぅぅぅぅぅんっ！！！」
**TW:** 「噗？！嗯！唔！！！」
**Cũ:** 「Ưm pu!!? Ưm! Phù u u u u u u u u n!!!」
**Mới:** 「Ưm pu!!? Ưm! Phù u u u u u u u n!!!」
Đếm nguyên âm: JP ふぉ + 7ぅ = 8 âm; VN cũ có 9 (Phù + 8 u) — thừa 1 u. Bớt 1 u.

### 1116 — ふかみ — meaning
**JP:** 「それ……でっ――おまんこっ――膣、の……入り口――⏎しつ、こく、いじめられ、て――焦らされたり、してっ」
**TW:** 「然後……下面……入口……仔細地欺負我……讓我焦急」
**Cũ:** 「Sau……đó——âm đạo——cửa, của……tử cung——⏎Bị, bắt nạt, dai dẳng——rồi bị làm cho, khao khát」
**Mới:** 「Sau……đó——âm đạo——cửa, của……âm đạo——⏎Bị, bắt nạt, dai dẳng——rồi bị làm cho, khao khát」
Lỗi giải phẫu: 膣の入り口 = cửa âm đạo, VN cũ viết "cửa tử cung" (tử cung = 子宮). Đối chứng: key 1316 cùng file dịch đúng 膣→âm đạo, 子宮→tử cung.

### 1172 — ふかみ — gasp
**JP:** 『「っ！！？」⏎「ひっ――――んっ！」』
**TW:** 『「唔！！？」⏎「呀……嗯！」』
**Cũ:** 『「!!?」⏎「Hi――――ưm!」』
**Mới:** 『「Ư!!?」⏎「Hi――――ưm!」』
Dòng 1 là gasp nguyên dòng (っ！！？) — VN chỉ còn "!!?". Dòng 2 giữ nguyên (ひっ→"Hi", んっ→"ưm" đúng).

### 1442 — monologue — raw-tsu
**JP:** 呼吸も、望みも、重なりあってる。⏎だからこのまま、腰を思い切り動かすだけで――っ！
**TW:** 我們的呼吸，我們的意願現在合而為一。所以接下來我只需要用力插下！
**Cũ:** Cả nhịp thở, cả ước muốn, đều đang hòa quyện vào nhau.⏎Vì vậy, cứ thế này, chỉ cần dập hông hết sức là——っ!
**Mới:** Cả nhịp thở, cả ước muốn, đều đang hòa quyện vào nhau.⏎Vì vậy, cứ thế này, chỉ cần dập hông hết sức là——Ư!
Raw っ còn nguyên trong VN. Áp nguyên fix của sweep (chỉ thay っ→Ư; giữ `\n` của CSV3, không dùng dạng gộp khoảng trắng của sweep).

### 1455 — monologue — pronoun
**JP:** 今度はパンツを横にずらして、⏎ふかみのスジを直接に見て確かめる。
**TW:** 我將內褲扒開，直接觀察深美的裂縫。
**Cũ:** Lần này anh kéo quần lót sang một bên,⏎để trực tiếp nhìn và kiểm tra rãnh dọc của Fukami.
**Mới:** Lần này tôi kéo quần lót sang một bên,⏎để trực tiếp nhìn và kiểm tra rãnh dọc của Fukami.
Độc thoại, người kể là Soutetsu — tự xưng "tôi", không phải "anh" (file dùng "tôi" ở 153/158 dòng độc thoại).

### 1461 — monologue — pronoun
**JP:** 触れて味わいたいのは当然、⏎中身であるに決まっている――が。
**TW:** 我想觸碰想品味的，當然是裡面的東西了。但是……
**Cũ:** Thứ anh muốn chạm vào và thưởng thức, tất nhiên,⏎chắc chắn là phần bên trong rồi——nhưng mà.
**Mới:** Thứ tôi muốn chạm vào và thưởng thức, tất nhiên,⏎chắc chắn là phần bên trong rồi——nhưng mà.
Độc thoại — "tôi".

### 1520 — monologue — gasp
**JP:** やけにあっさり、⏎日々姫は蔵へと戻ってしま――っ！？
**TW:** 日日姬這麼簡單就回酒窖了……唔？！
**Cũ:** Thật nhẹ nhàng,⏎Hibiki đã quay trở lại nhà kho——!?
**Mới:** Thật nhẹ nhàng,⏎Hibiki đã quay trở lại nhà kho——Ư!?
JP kết "――っ！？" — VN giữ gạch + dấu câu, mất っ. Chỉ sửa gasp; "Thật nhẹ nhàng" cho やけにあっさり giữ nguyên (diễn lỏng chấp nhận được).

### 1562 — monologue — sfx
**JP:** ばたばた、首が左右に振られる。⏎おまんこがきゅうきゅう締め付けてくる。
**TW:** 深美搖了搖頭，下面變得更緊了。
**Cũ:** Phập phập, đầu em ấy lắc lư sang hai bên.⏎Âm đạo siết chặt lại từng cơn.
**Mới:** Đầu em ấy lắc lia lịa sang hai bên.⏎Âm đạo siết chặt lại từng cơn.
ばたばた = đầu lắc sang hai bên lia lịa; "Phập phập" là SFX đâm/đập — sai từ cho hành động này, gây hiểu nhầm. Bỏ SFX sai, giữ động tác.

### 1564 — monologue — pronoun
**JP:** あまりに高度な『正しいパンツの触り方』につい熱中し、⏎食い入るように、食い込みに見入ってしまっていたが――
**TW:** 深美正沉浸在很高級的“正確觸摸內褲法”之中，連我都看得入神了。可是……
**Cũ:** Anh lỡ say sưa vào 『cách chạm quần lót đúng chuẩn』 quá mức điêu luyện này,⏎đến nỗi cứ dán mắt vào chỗ lún sâu đó——
**Mới:** Tôi lỡ say sưa vào 『cách chạm quần lót đúng chuẩn』 quá mức điêu luyện này,⏎đến nỗi cứ dán mắt vào chỗ lún sâu đó——
Độc thoại — "tôi".

### 1566 — monologue — gasp
**JP:** 閉じ込めきれず。ふかみは大きく口を開いて息を漏らして。⏎それでも、声は、どうにかこうにか抑え続け――っ！？
**TW:** 深美沒能徹底控制住自己的聲音，她大張著嘴在呼氣。但是她依然勉強控制著自己的聲音……唔？！
**Cũ:** Không thể kìm nén được nữa. Fukami há to miệng, để lọt ra những tiếng thở hắt.⏎Dù vậy, em ấy vẫn bằng cách nào đó tiếp tục kìm nén giọng nói của mình——!?
**Mới:** Không thể kìm nén được nữa. Fukami há to miệng, để lọt ra những tiếng thở hắt.⏎Dù vậy, em ấy vẫn bằng cách nào đó tiếp tục kìm nén giọng nói của mình——Ư!?
JP kết "――っ！？" — VN mất っ. Sweep ghi "uncertain" nhưng lý do của sweep bị nhầm (mô tả JP là "tiếng rên ngắn ん～～～――っ" trong khi JP thực là dòng dẫn dài; JP/TW/VN đều khớp nhau) — đã giải quyết: sửa như các dòng cùng mẫu (1520, 1591).

### 1579 — monologue — term
**JP:** ふかみのおまんこも熱くぬらめき、⏎ひっきりなしの収縮は、より小刻みなペースになってる。
**TW:** 深美的下體也越來越燙，那持續不斷的收縮，頻率也變得越來越快。
**Cũ:** Cô bé của Fukami cũng ướt át nóng bỏng,⏎những cơn co thắt liên tục, đang trở nên dồn dập hơn.
**Mới:** Âm đạo của Fukami cũng ướt át nóng bỏng,⏎những cơn co thắt liên tục, đang trở nên dồn dập hơn.
おまんこ được dịch "âm đạo" ở mọi dòng khác trong file; "Cô bé" ở đây là ngoại lệ không nhất quán.

### 1591 — monologue — gasp
**JP:** ふかみの舌が、口内が、⏎張り付きながらぶるぶる震え――っ！！？
**TW:** 深美的舌頭和嘴，都一邊緊貼著我一邊顫抖著。
**Cũ:** Lưỡi của Fukami, khoang miệng của em ấy,⏎vừa dính chặt vừa run rẩy bần bật——!!?
**Mới:** Lưỡi của Fukami, khoang miệng của em ấy,⏎vừa dính chặt vừa run rẩy bần bật——Ư!!?
JP kết "――っ！！？" — VN mất っ.

### 1641 — monologue — pronoun
**JP:** 見せてくれるのなら素直に嬉しい。ありがたい。
**TW:** 能給我看，我當然開心。我很感激。
**Cũ:** Nếu em ấy cho anh xem thì anh thực sự rất vui. Cảm ơn em.
**Mới:** Nếu em ấy cho tôi xem thì tôi thực sự rất vui. Cảm ơn em.
Độc thoại — "tôi" (cả hai chỗ). "Cảm ơn em" giữ nguyên (gọi Fukami "em" đúng).

### 1660 — monologue — pronoun
**JP:** その喜びが、許可してもらえたことへの自信が、⏎僕をもう少し貪欲にする。
**TW:** 這份喜悅，這份得到允許的自信，刺激了我的貪婪。
**Cũ:** Niềm vui đó, cùng sự tự tin khi được cho phép,⏎khiến anh trở nên tham lam hơn một chút.
**Mới:** Niềm vui đó, cùng sự tự tin khi được cho phép,⏎khiến tôi trở nên tham lam hơn một chút.
Độc thoại — "tôi".

### 1735 — monologue — gasp
**JP:** （ずっ――ぬっ――ずんっ――ぬるうっ――）
**TW:** （拔，插，拔，插）
**Cũ:** （Phập——phập——phập——trượt sâu u u——）
**Mới:** （Phập——phập——phập——trượt sâu u u ư——）
Âm cuối ぬるうっ mất っ (VN chỉ còn "——"). Áp dụng fix của sweep về thực chất (thêm Ư) nhưng đặt Ư TRƯỚC dấu gạch theo thứ tự JP (ぬるうっ――), tiền lệ lr_ふかみh2 1072 (っ―― → Ư――); vị trí của sweep ("u u——Ư") đặt sau gạch vì JP của sweep là dòng stale-set (dòng dẫn dài 1566), không phải dòng SFX này.

### 1759 — 双鉄H — pronoun
**JP:** （靴……だ。⏎僕のも、ふかみのも玄関先に揃ったままで――）
**TW:** （有鞋子……我的和深美的都在門口……）
**Cũ:** （Giày……kìa.⏎Cả của mình và của Fukami đều đang xếp gọn ở lối vào——）
**Mới:** （Giày……kìa.⏎Cả của anh và của Fukami đều đang xếp gọn ở lối vào——）
Soutetsu nói với Fukami — tự xưng "anh" (quy tắc đã chốt); "mình" chỉ dành cho độc thoại Fukami / độc thoại nội tâm cảm xúc của Soutetsu, không dùng trong thoại. (934 "ánh mắt của mình" là sở hữu cách phản thân "của mình" = của chính anh — giữ nguyên, không phải đại từ xưng.)

### 1767 — monologue — vowel-count
**JP:** （きゅううううううんっ！）
**TW:** （緊！）
**Cũ:** （Kyu u u u u u n!）
**Mới:** （Kyu u u u u u u n!）
Đếm nguyên âm: JP きゅ + 6う = 7 âm; VN cũ có 6 (Kyu + 5 u) — thiếu 1 u. Thêm 1 u.

### 1776 — 双鉄H — lost-sound
**JP:** （これ――はっ――）
**TW:** （這……）
**Cũ:** （Cái——này——）
**Mới:** （Cái——này——ha——）
JP có はっ (tiếng thở "ha") sau "これ" — VN bỏ mất hẳn. Thêm "ha" (TW chỉ ghi "這……" nên không đối chứng được; はっ là âm thở, diễn "ha" theo mẫu あっ→"A"/"Ah").

## 4. Sweep っ — 17 mục (đã đối chiếu từng mục với JP bộ tốt)

| Key | Kind (sweep) | Kết quả |
|---|---|---|
| 736 | lost-gasp-whole | **FALSE POSITIVE — không sửa.** JP của sweep (「っ！！！」) là JP bộ stale; JP bộ tốt là 「…………」, VN 「…………」 khớp — không có gasp nào bị mất. |
| 988 | already-rendered | Đã kiểm chứng — giữ. Chuỗi rên dài, mỗi âm đều có diễn đạt (Ư/ưm/phù/ực); âm cuối ひひゅっ→"ưm" là diễn lỏng trong chuỗi, không phải mất âm. |
| 1033 | already-rendered | Đã kiểm chứng — giữ. ぷっ→"pu", こくっ→"Ực" — gasp đã diễn bằng SFX khác. |
| 1043 | needs-file-audit | **fa/fu dạng cũ, không phải gasp.** ぷあっ→"Phù" — giữ âm f, dạng cũ vào đợt thống nhất (xem §6). Không tính sai. |
| 1312, 1382, 1440, 1465, 1482, 1512, 1553, 1601, 1605, 1723 | needs-file-audit (10 mục) | **FALSE POSITIVE — không sửa.** JP các dòng này đều không có っ; VN khớp JP/TW. Lý do chung của sweep ("VN là câu đầy đủ ở dòng khác / lệch số đoạn") không đúng với file này. |
| 1442 | raw-tsu | **Áp nguyên.** Fix lấy từ CSV3 với `\n` nguyên (xem §3). |
| 1566 | uncertain | **Đã giải quyết — sửa.** Lý do uncertain của sweep bị nhầm (mô tả JP là tiếng rên ngắn, trong khi JP thực là dòng dẫn dài); JP/TW/VN khớp nhau, っ cuối dòng bị mất (xem §3). |
| 1735 | lost-gasp-trailing | **Áp dụng về thực chất, sửa vị trí Ư.** JP của sweep là dòng stale-set; JP bộ tốt là dòng SFX. Thêm Ư nhưng đặt trước gạch theo thứ tự JP (xem §3). |

**Sweep bỏ sót 7 gasp** (bắt được khi quét bổ sung toàn bộ 194 dòng JP có っ): 995, 996, 1007, 1024, 1172, 1520, 1591. Không còn gasp っ trần nào khác bị mất trong file.

## 5. Các dòng giữ nguyên có ghi chú (phán đoán đã chốt, không tính sai)

- **"Kh" cho っ tắc thanh quản (989, 997, 1017, 1731, 1739): GIỮ.** くっ→"Kh" (989), っ đứng một mình→"kh" (997: むぅ、っ→"ưm, kh"), っ trần→"Kh" (1017), っぐっ→"kh"/"Kh" (1731, 1739). Âm không bị mất — chỉ diễn khác (tiếng tắc ở cổ họng, nhất quán 5 lần trong file). Quy tắc "không để mất âm" được thỏa mãn; khác với các dòng gasp đã sửa (ở đó VN chỉ còn dấu câu, không có âm nào). Nếu Hieu muốn thống nhất thành Ư thì đưa vào đợt thống nhất (xem §6).
- **fa/fu dạng cũ (973, 981, 982, 1025, 1034, 1043): GIỮ, vào đợt thống nhất.** Tất cả đều giữ âm f ("phù ah"/"phù a"/"Phù") — khác file lr_ふかみh2 (ở đó ふぁ/ふあ thành "Ha"/"Ah" mất âm f, tính sai). Theo tiền lệ ふかみh1, dạng cũ không tính sai (xem §6).
- **あっ→"A"/"Ah", はうっ→"Ha ư"/"A ư", ひゃっ→"Hya", やんっ→"Yan": GIỮ** (tiền lệ ふかみh1: các dòng あっ/はうっ giữ nguyên; ひあ/ひゃ tự do theo nhân vật + ngữ cảnh, Hieu 20/11).
- **Chuỗi SFX rên lỏng (987, 988, 994, 999, 1000, 1002, 1003, 1004, 1013, 1025, 1027, 1028, 1032, 1033, 1034, 1036, 1730–1755, 1766–1772): GIỮ.** Số lượng âm khớp JP; mỗi âm đều có diễn đạt (phù/pu/gu/chụt/Phập…); っ trên âm tiết mở (ぐっ→"gu", ぷっ→"pu", ふっ→"phù") được diễn bằng chính âm tiết đó — cùng chuẩn với 1033 (sweep already-rendered). Chỉ sửa khi âm mất hẳn (995/996/1007/1024/1172/1442/1520/1566/1591/1735/1776) hoặc sai từ (1562).
- **Động từ diễn SFX (1737 "cọ", 1752/1753 "Kéo", 1755 "Dừng lại", 1734 "Rút"): GIỮ.** っ nhấn mạnh trên động từ — không cần Ư (cùng quy tắc với っ nhấn mạnh cuối câu trên từ có nghĩa).
- **1740 "Phập——————Bịch" cho ずぶうううううううッ: GIỮ.** Độ dài âm (7う) được diễn bằng dấu gạch dài sau "Phập".
- **1739/1744 chuỗi "p" diễn chuỗi っ/い dài: GIỮ.** Độ dài được diễn bằng lặp âm p.
- **1768 "Siết chặt" cho きゅううううううううううっっ: GIỮ.** Diễn theo nghĩa (TW cũng diễn "緊"); cùng kiểu với 1755.
- **970 "sẽ có, cảm giác……mất" (hoàn thiện "感じ……って"): GIỮ** — TW đồng thuận ("會有感覺的").
- **1299 "lăn dài" cho 浮きあがってくる: GIỮ** — diễn lỏng ("nước mắt lăn dài" thay cho "dâng lên"), không sai nghĩa cảnh.
- **1163 "vậy——" cho してっ――: GIỮ** — diễn lỏng "～たりして" (làm mấy chuyện như thế).
- **1102 "Hô?" cho ほう？: GIỮ** — phiên âm cảm thán, cùng kiểu với "Hya"/"Hyan".
- **1753 "Kéo" cho ずっ (×3): GIỮ, ghi chú biên.** ずっ là âm đâm vào, "Kéo" là kéo/trượt — hơi lệch hướng; nhưng trong chuỗi montage trượt/cọ thì đọc được như chuyển động qua lại, TW cũng diễn cả ba là 擦 (cọ). Không tính sai; nếu Hieu muốn phân biệt đâm/kéo thì báo.
- **1314 "——" cho ほどっっ――: GIỮ.** っっ nhấn mạnh trên ほど (độc thoại) — không phải gasp, không cần Ư.
- **1080 "——ạ" cho からっ: GIỮ.** っ nhấn mạnh cuối câu — không phải gasp.
- **1448 "Phòng của Nagi": GIỮ, đúng.** JP "凪の部屋" thắng TW "深美的房間".

## 6. Chờ Hieu / đợt thống nhất (không tự quyết)

1. **1513 — CHƯA CHẮC CHẮN (1 dòng duy nhất).** JP: 「飛びつくようにおまんこへ届いた指先が、⏎さすさすと、縦スジに沿って動き始める。」— JP không nêu chủ thể ngón tay là ai; TW nói Soutetsu ("我立刻將手伸上前去"), VN nói Fukami ("Đầu ngón tay em ấy vội vã chạm vào âm đạo"). Dòng trước (1509) là ngón tay Soutetsu đang cọ qua quần lót — có thể là cùng một ngón tay tiếp tục, nhưng "飛びつくように" (như vồ lấy) cũng hợp với Fukami háo hức tự chạm. KHÔNG sửa, không tính sai — cần Hieu xác nhận hoặc tra ngữ cảnh cảnh.
2. **Thẻ %l bị bỏ toàn bộ (4 thẻ, 3 dòng: 1050, 1073, 1096×2).** JP có tag glossary `[とう,1]`, `[かあ,1]`, `[みぎたいちしゅぞうもと,5]`, `[とうじ,1]` nhưng VN 0 thẻ — bản build sẽ mất popup giải thích thuật ngữ. Không tự thêm (chưa rõ cú pháp %l cần dựng + đợt quét thẻ đang chờ kiểm tra B19 trong game). Cần quyết: có bổ sung tag vào đợt quét thẻ không.
3. **fa/fu đợt thống nhất (6 dòng, không tính sai):** 973 (ふあっ→"phù ah"), 981 (ふあっ→"Phù ah!"), 982 (ぷあっ→"Phù ah!!?"), 1025 (ふぁっ→"Phù a", ふぁ→"phù a", ふぁんっ→"phù an"), 1034 (ふぁひ→"phù a hi", ふぁん→"phù an"), 1043 (ぷあっ→"Phù") — sửa thành "phà"/"phùa" theo JP (ふぁ→"phà", ふあ/ぷあ→"phùa").
4. **"Migitaichi" (1096, nhà máy rượu 右田一酒造元).** Có nên tách thành "Migita Ichi" theo quy tắc Migita="Migita Ichi" không? Hiện giữ nguyên (tên nhà máy). Cần quyết trong đợt thống nhất.
5. **"Toji" (1096, 1376) cho 杜氏.** Giữ nhất quán trong file; TW ghi 掌窖 (bậc thầy ủ rượu). Nếu Hieu muốn dịch nghĩa ("bậc thầy ủ rượu"/"chủ lò") thay vì giữ nguyên thì báo.
6. **"Kh" cho っ (989, 997, 1017, 1731, 1739).** Nếu Hieu muốn thống nhất thành Ư thì đưa vào đợt thống nhất (xem §5 — hiện giữ vì âm không bị mất).

## 7. Lượt soát 2 và khối TOML

**Lượt soát 2: 22/22 tái kiểm chứng, 0 bỏ, 0 sửa.** Đọc lại toàn bộ 22 giá trị fix đối chiếu từng dòng với JP (+TW): 9 gasp (995, 996, 1007, 1024, 1172, 1520, 1566, 1591, 1735), 1 raw-tsu (1442), 6 đại từ (1455, 1461, 1564, 1641, 1660, 1759), 2 đếm nguyên âm (1044, 1767), 1 nghĩa (1116), 1 SFX (1562), 1 thuật ngữ (1579), 1 âm mất (1776) — tất cả đều đúng JP, không dòng nào phải bỏ hay sửa lại ở lượt 2.
**Kiểm chứng cơ học:** JSON 22 mục (khóa dạng chuỗi); jp/tw/old_vn khớp CSV3 (bộ tốt) 22/22; mỗi fix chỉ khác old VN ở đúng chỗ sửa (đã kiểm tra diff từng dòng — xem log kiểm chứng); khối TOML dưới đây parse OK bằng tomllib, 22 khóa, 0 sai lệch giá trị so với JSON.

```toml
"995" = "「Ư!!」"
"996" = "「~~~~~~~~Ư!!!」"
"1007" = "「Ư!? Fukami——em nói to quá rồi đấy.」"
"1024" = "「Ư!!!」"
"1044" = "「Ưm pu!!? Ưm! Phù u u u u u u u n!!!」"
"1116" = "「Sau……đó——âm đạo——cửa, của……âm đạo——\\nBị, bắt nạt, dai dẳng——rồi bị làm cho, khao khát」"
"1172" = "『「Ư!!?」\\n「Hi――――ưm!」』"
"1442" = "Cả nhịp thở, cả ước muốn, đều đang hòa quyện vào nhau.\\nVì vậy, cứ thế này, chỉ cần dập hông hết sức là——Ư!"
"1455" = "Lần này tôi kéo quần lót sang một bên,\\nđể trực tiếp nhìn và kiểm tra rãnh dọc của Fukami."
"1461" = "Thứ tôi muốn chạm vào và thưởng thức, tất nhiên,\\nchắc chắn là phần bên trong rồi——nhưng mà."
"1520" = "Thật nhẹ nhàng,\\nHibiki đã quay trở lại nhà kho——Ư!?"
"1562" = "Đầu em ấy lắc lia lịa sang hai bên.\\nÂm đạo siết chặt lại từng cơn."
"1564" = "Tôi lỡ say sưa vào 『cách chạm quần lót đúng chuẩn』 quá mức điêu luyện này,\\nđến nỗi cứ dán mắt vào chỗ lún sâu đó——"
"1566" = "Không thể kìm nén được nữa. Fukami há to miệng, để lọt ra những tiếng thở hắt.\\nDù vậy, em ấy vẫn bằng cách nào đó tiếp tục kìm nén giọng nói của mình——Ư!?"
"1579" = "Âm đạo của Fukami cũng ướt át nóng bỏng,\\nnhững cơn co thắt liên tục, đang trở nên dồn dập hơn."
"1591" = "Lưỡi của Fukami, khoang miệng của em ấy,\\nvừa dính chặt vừa run rẩy bần bật——Ư!!?"
"1641" = "Nếu em ấy cho tôi xem thì tôi thực sự rất vui. Cảm ơn em."
"1660" = "Niềm vui đó, cùng sự tự tin khi được cho phép,\\nkhiến tôi trở nên tham lam hơn một chút."
"1735" = "（Phập——phập——phập——trượt sâu u u ư——）"
"1759" = "（Giày……kìa.\\nCả của anh và của Fukami đều đang xếp gọn ở lối vào——）"
"1767" = "（Kyu u u u u u u n!）"
"1776" = "（Cái——này——ha——）"
```

Kết bài
