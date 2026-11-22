# Unification batch U4 — §1 set-3 terminology (T6, T7, T15, T16, T41, T45, T47, T54, T55, T11, T12, T19, T20)

## §0. Phạm vi

- Mục: **T6** 日ノ本 → "Hinomoto" · **T7** 湯医 / 湯医線 → "Yunoi" · **T15** 小畑 → "Okoba" · **T16** 駿袋鉄道 → "Suntai" · **T41** "KiHa" (chính tả JR) · **T45** 冥国 → "Minh Quốc" / 冥軍 → "Minh Quân" · **T47** マスコン / マスターコントローラー → "điều khiển trung tâm" · **T54** 回数券 → "vé lượt" / 定期券 → "vé định kỳ" · **T55** 仲国06 1412 → "Nhân giống" · **T11** 運転体 → "thân vận hành" · **T12** 整備体 → "thân bảo trì" · **T19** 乗員 → "nhân viên tàu" · **T20** Seki → "ông ngoại". Tất cả DECIDED — áp trực tiếp, không có mục OPEN nào trong batch này.
- Kết quả: **193 dòng sửa, 56 file** — T6: 34 · T7: 107 (105 dòng đơn + 2 dòng hai mục) · T15: 6 (5 + 1 hai mục) · T16: 1 · T41: 18 (17 + 1 hai mục) · T45: 6 · T47: 5 · T11: 11 · T12: 3 · T19: 1 · T20: 3. **T54: 0 dòng** và **T55: 0 dòng** — cả hai đã sửa xong trước batch này (xem §3).
- Số lần xuất hiện dạng cũ đã thay: "Hinamoto" ×34 · "Yui" ×111 (trong 107 dòng; 4 dòng ×2) · "Obata"/"Kobata" ×6 · "Suntetsu" ×1 · "Kiha" ×18 · "Meikoku" ×6 · "Master Controller"/"bộ điều khiển trung tâm" ×5 · các dạng thân/kíp ×14 · "phi hành đoàn" (乗員) ×1 · "ông nội" (Seki) ×3.
- So với ước lượng trong UNIFICATION-LIST.md §0: T6 thực tế 34 (ước 28) · T7 thực tế 107 (ước 89) · T15 đúng 6 · T16 đúng 1 · T41 thực tế 18 (ước 14) · T45 thực tế 6 (ước 5) · T47 thực tế 5 (ước 1 — thêm 2 dòng "bộ điều khiển trung tâm" ở P15 và 2 dòng 主幹制御器 ở ハチロク06, xem D1) · T11+T12 thực tế 14 (ước ~6 — kiểm kê toàn bộ 86 dòng JP 運転体/整備体/ボディ tìm thêm các biến thể "thân điều khiển", "cơ thể lái tàu", "thân hình lái tàu", "cơ thể bảo dưỡng", xem D2) · T19 thực tế 1 (ước 2 — ハチロク07 2514 đã sửa trong audit) · T20 thực tế 3 (ước 4 — 凪ふかみ02 2299 và ハチロク07 2679 đã sửa trong audit). Các số "còn lại" trong §0 đã ghi rõ là ước lượng, không phải số cuối cùng.

## §1. Phương pháp liệt kê (chỉ đếm, không sửa hàng loạt)

1. Đọc CSV3 good-set 87.833 dòng (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`).
2. Tính giá trị hiện tại (current value) cho mọi dòng theo thứ tự ĐÃ SỬA (coordinator xác nhận 22/11 ~11:35, phát hiện từ U2c): **unification đã gộp (theo thứ tự gộp) > moan > audit > CSV3 VN** — KHÔNG phải moan > audit > unification như brief gốc viết. Bằng chứng: dùng thứ tự cũ cho ra 14 ứng viên thừa ở U2c (9 dòng đã sửa xong trong U2a). Map unification chỉ nạp các file ĐÃ GỘP (8 file, 656 mục); các file worker đang chạy (U4 set2, T56–T66) KHÔNG được nạp. Giá trị fix moan nếu (file,key) có trong bất kỳ `moans/moan-*-wrong.json` nào (66 file, 1.535 mục, gồm supplement ハチロクh3), nếu không thì giá trị fix audit nếu có trong bất kỳ `audit-*-wrong.json` nào (217 file, 9.500 mục), nếu không thì VN CSV3. Ghép fix-list với CSV3 bằng cặp (file,key) trước, rồi (key,JP). Nguồn old_vn của 193 dòng trong batch này: csv3 143, audit 30, unification đã gộp 20, moan 0. Kiểm chứng chéo hai thứ tự: chỉ 1/193 dòng có old_vn khác nhau giữa thứ tự cũ và thứ tự đã sửa — 日々姫08 3719 (U2c gộp sau khi liệt kê; đã rebase về giá trị gộp, xem §4); 192 dòng còn lại giống hệt.
3. Ứng viên = current value chứa dạng cũ của từng mục. Đã liệt kê: "Hinamoto" 34 · "Yui" (word-boundary) 109 · "Obata"/"Kobata" 6 · "Suntetsu" 1 · "Kiha" (word-boundary) 18 · "Meikoku" 6 · "Master Controller"/"[Bb]ộ điều khiển trung tâm" 5 (tìm thêm bằng case-insensitive mới bắt được ハチロク06 2139/2763) · "kíp lái"/"thân chính"/"thân lái"/"Kíp chuẩn bị" 7 · "phi hành đoàn" 13 · "ông nội" 25.
4. Kiểm chứng chéo bằng phía JP (không chỉ phía VN): JP 日ノ本 367 dòng = 34 "Hinamoto" + 326 "Hinomoto" + 7 dạng khác (Nippon Sharyo / Yamato Nadeshiko) · JP 湯医 221 dòng = 98 "Yui" + 123 "Yunoi", 0 dòng thiếu cả hai · JP 小畑 41 dòng = 35 "Okoba" + 6 dạng cũ · JP キハ 172 dòng (chỉ 18 dòng còn "Kiha") · JP 冥国 84 dòng (chỉ 6 dòng còn "Meikoku"; 冥軍 1 dòng đã "Minh Quân"; メリケン 9 dòng đã "Meriken") · JP 乗員 7 dòng (1 đã "nhân viên tàu", 1 "phi hành đoàn" sửa ở đây, 5 dòng còn lại dùng dạng đúng khác) · kiểm kê toàn bộ 86 dòng JP chứa 運転体/整備体/運転ボディ/整備ボディ cho T11/T12 · kiểm kê toàn bộ 25 dòng "ông nội" cho T20.
5. Đọc từng dòng ứng viên: JP (+TW) của cả 193 dòng đã sửa + các dòng giữ lại ở §3 đã được đọc hết (xem §2–§3). Fix = chỉ thay thế đúng chuỗi mục tiêu, giữ nguyên toàn bộ phần còn lại (kể cả "Ohimitera" còn sót ở 2 dòng 共通14 1671/1805 — thuộc batch leftovers, xem §3; kể cả "túi phi hành đoàn" ở Grand06 3472 — thuộc T18; kể cả "Akai-guji" ở cùng dòng — thuộc T13). Không đụng dòng gasp Ư hay dòng "Kh" nào — ngoại trừ ハチロク10 2488 (T6) vốn đã chứa Ư do audit thêm: chỉ đổi "Hinamoto", Ư giữ nguyên.

## §2. Quyết định trong batch (theo uỷ quyền của Hieu — điều tra JP+TW rồi quyết, không park)

- **D1 — T47: bỏ "bộ" trong "bộ điều khiển trung tâm" (4 dòng: P15 1073/1981, ハチロク06 2139/2763).** Bằng chứng: dạng đã khóa là "điều khiển trung tâm" (không "bộ"); cùng file ハチロク06, key 2145 gloss マスコン/マスターコントローラー đã là "điều khiển trung tâm" trần, và các dòng マスコン khác trong dự án (日々姫10 3219/2346, ハチロク06 2274/1630) đều dùng dạng trần. 2139/2763 có JP là 主幹制御器 — dạng đầy đủ của マスコン (master controller), cùng khái niệm; 2139 JP chỉ còn ruby しゅかんせいぎょき, TW 主控 xác nhận. Cả 4 dòng đều đổi về dạng trần (1073 giữ viết hoa đầu câu: "Điều khiển trung tâm?"). Cộng P15 1664 "Master Controller" → T47 tổng 5 dòng.
- **D2 — T11/T12: thống nhất cả các biến thể chưa liệt kê trong list.** "thân điều khiển" (運転体, ハチロク13 2328/2742/2326/2555/2427 — 5 dòng) → "thân vận hành": audit tự nó đã dùng cả hai dạng cho cùng thuật ngữ ("thân điều khiển" ở ハチロク13 vs "thân vận hành" ở ニイロク04 2061), nên phải thống nhất về dạng đã khóa. "cơ thể lái tàu" (運転ボディ, P07 2512) và "thân hình lái tàu" (運転ボディ, P14 2286) → "thân vận hành": tiền lệ trực tiếp là れいな01 2218 — cùng câu JP 「確かに、いつも抱っこするハチロクは運転ボディ――人形サイズの方の体だ。」 đã được audit sửa thành "thân vận hành". "cơ thể bảo dưỡng" (整備ボディ, P11 1304) → "thân bảo trì" theo cùng logic. "thân chính bảo dưỡng" (整備ボディ, P14 2530) → "thân bảo trì" (bỏ "chính", "bảo dưỡng" đã nằm trong "bảo trì").
- **D3 — T41 ハチロク01 2828:** JP không viết キハ mà dùng レイナナ (Reina-07) — referent vẫn là đầu máy KiHa 07 (chính Reina); chỉ sửa chính tả "Kiha" → "KiHa", không phải misalignment, không đổi gì khác.
- **D4 — T47 ハチロク06 2139:** JP dòng này chỉ còn ruby しゅかんせいぎょき, không có kanji 主幹制御器 trong text; TW 主控 xác nhận thuật ngữ là "chủ khống" = master controller — áp T47 như các dòng マスコン khác (xem D1).
- **Không có quyết định OPEN nào khác trong batch.** T6/T7/T15/T16/T41/T45/T19/T20 đều DECIDED và mọi dòng sửa đều có JP xác nhận trực tiếp (trừ 2 trường hợp D3/D4 đã ghi rõ).

## 00_Common — `共通12_のぞみ.txt.toml` (1 dòng)

### key 2182 — item T20 (JP: 堰)

- JP: 「ふたごの方たちなのですね？\nふかみちゃんのおじいさんたち堰さんと流さんとは」
- TW: 「小深的爺爺堰先生和流先生是雙胞胎吧？」
- old_vn (csv3): 「Hai người là anh em sinh đôi nhỉ?\nÔng nội của Fukami, ông Seki và ông Nagare ấy.」
- fix: 「Hai người là anh em sinh đôi nhỉ?\nÔng ngoại của Fukami, ông Seki và ông Nagare ấy.」
- Lý do: JP chứa 堰 / 祖父 — dòng Seki; VN cũ dùng "ông nội" → đổi thành "ông ngoại" theo T20 (DECIDED 20/11 ~19:15, Hieu; CHỈ các dòng Seki).

## 00_Common — `共通14_負債.txt.toml` (4 dòng)

### key 1435 — item T7 (JP: 湯医)

- JP: 「つまり、かつては湯医にもターンテーブルがあり、\nしかし、それは失われてしまったのだな？」
- TW: 「也就是說，曾經在湯醫也有轉車盤，而現在已經沒有了是嗎？」
- old_vn (csv3): 「Nghĩa là, trước đây ở Yui cũng từng có bàn quay đầu máy,\nnhưng mà, nó đã bị mất rồi sao?」
- fix: 「Nghĩa là, trước đây ở Yunoi cũng từng có bàn quay đầu máy,\nnhưng mà, nó đã bị mất rồi sao?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1571 — item T7 (JP: 湯医)

- JP: 「む？\nこの、『湯医駅[さんかくせん,2]三角線新造』とはなんだ？」
- TW: 「嗯？這條“新建湯醫站三角線”是什麼？」
- old_vn (csv3): 「Hửm?\nCái 'Xây mới \x%l三角線;#00ffc040;đường tam giác%l;#; ga Yui' này là sao?」
- fix: 「Hửm?\nCái 'Xây mới \x%l三角線;#00ffc040;đường tam giác%l;#; ga Yunoi' này là sao?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1671 — item T7 (JP: 湯医)

- JP: 「逆に……多分、ターンテーブルがあったから、\n御一夜-湯医間に[ハチロクニイマル,3]8620を引いてきたんだと思います」
- TW: 「我想……或許正因為曾經有過轉車盤，才會將８６２０帶到御一夜至湯醫之間的鐵路上來」
- old_vn (csv3): 「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,\nngười ta mới đưa 8620 vào chạy tuyến Ohimitera - Yui đấy ạ.」
- fix: 「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,\nngười ta mới đưa 8620 vào chạy tuyến Ohimitera - Yunoi đấy ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: giữ nguyên "Ohimitera" trong fix — đó là dòng T1 còn sót, thuộc batch leftovers (T1), không thuộc batch này.

### key 1805 — item T7 (JP: 湯医)

- JP: 「湯医駅の周辺広くが御一夜鉄道の社有地ですから、\nターンテーブルより、グっと安く済みます……けど」
- TW: 「湯醫站周邊一帶，都是御一夜鐵路公司的所有地，所以相比安裝轉車盤，要實惠太多太多……但是」
- old_vn (csv3): 「Khu vực rộng lớn quanh ga Yui đều là đất của Đường sắt Ohimitera,\nnên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」
- fix: 「Khu vực rộng lớn quanh ga Yunoi đều là đất của Đường sắt Ohimitera,\nnên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: giữ nguyên "Đường sắt Ohimitera" trong fix — dòng T1 còn sót, thuộc batch leftovers (T1), không thuộc batch này.

## 01_Hachiroku — `ハチロク01_双鉄の目・ハチロクの目.txt.toml` (4 dòng)

### key 1719 — item T11 (JP: 運転体)

- JP: 「なるほど、\x%l運転体;#00ffc040;運転体%l;#;のれいなであれば、\n同乗をしてもらっても、大した窮屈さは感じんな」
- TW: 「原來如此，即便加上玲奈的\x%l運転体;#00ffc040;駕駛體%l;#;，應該也不會覺得太擠」
- old_vn (csv3): 「Ra là vậy, nếu là Reina trong hình dáng \x%l運転体;#00ffc040;kíp lái%l;#;,\nthì dù có đi cùng, cũng không thấy quá chật chội.」
- fix: 「Ra là vậy, nếu là Reina trong hình dáng \x%l運転体;#00ffc040;thân vận hành%l;#;,\nthì dù có đi cùng, cũng không thấy quá chật chội.」
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 1778 — item T41 (JP: キハ)

- JP: 「まぁ、キハ[レイナナ,1]07ですね」
- TW: 「哦，這是Ｋｉｈａ０７啊」
- old_vn (csv3): 「Ôi, là Kiha 07 nhỉ.」
- fix: 「Ôi, là KiHa 07 nhỉ.」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 2078 — item T41 (JP: キハ)

- JP: 「それに加え、[ハチロクニイマル,3]8620が営業運転できるようになれば、\nキハ[レイナナ,1]07とれいなの負担も、分散されよう」
- TW: 「而且，８６２０能夠進行商業運營的話，也能分擔Ｋｉｈａ０７和玲奈的負擔吧」
- old_vn (csv3): 「Thêm vào đó, nếu 8620 có thể đi vào vận hành thương mại,\nthì gánh nặng của Kiha 07 và Reina, cũng sẽ được san sẻ.」
- fix: 「Thêm vào đó, nếu 8620 có thể đi vào vận hành thương mại,\nthì gánh nặng của KiHa 07 và Reina, cũng sẽ được san sẻ.」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 2828 — item T41 (JP: キハ)

- JP: 少し低くに構えて撮ったらしい写真には、\nレイナナらしい可愛らしさに、動感と迫力が同居している。
- TW: 這張照片似乎是以稍低的機位拍出的，０７的可愛與令人感動的魄力融合得恰到好處。
- old_vn (csv3): Bức ảnh có vẻ được chụp từ góc thấp,\nvừa mang nét đáng yêu đặc trưng của Kiha 07, vừa toát lên sự sống động và uy lực.
- fix: Bức ảnh có vẻ được chụp từ góc thấp,\nvừa mang nét đáng yêu đặc trưng của KiHa 07, vừa toát lên sự sống động và uy lực.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.
- Lưu ý: JP không viết キハ mà dùng レイナナ (Reina-07) — referent vẫn là đầu máy KiHa 07 (Reina); chỉ sửa chính tả "Kiha" → "KiHa", không đổi gì khác.

## 01_Hachiroku — `ハチロク03_冥国式レイルロオド.txt.toml` (10 dòng)

### key 1532 — item T6 (JP: 日ノ本)

- JP: “日ノ本式――マスターシステム\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、\nこれほど連携にすぐれるものか”と。
- TW: “日本式的——司乘定組體系\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;們，竟然配合得如此默契”云云。
- old_vn (csv3): Cô ấy hỏi "\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinamoto,\nlại có thể phối hợp ăn ý đến thế sao?".
- fix: Cô ấy hỏi "\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinomoto,\nlại có thể phối hợp ăn ý đến thế sao?".
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 1580 — item T6 (JP: 日ノ本)

- JP: 「……冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、日ノ本や[えいこく,1]詠国、[どっこく,1]髑国式の\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と大きく異なり、交代乗務を常とします」
- TW: 「……美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;與日本、英國、德國式有著顯著的不同，交替執行乘務任務可以說是家常便飯」
- old_vn (audit): 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
- fix: 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinomoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2084 — item T6 (JP: 日ノ本)

- JP: 「なるほどな。合理的……といえば極めて合理的だ。\nその視点に立てば逆に、日ノ本式の欠点も見えてくる」
- TW: 「原來如此。很合理……應該說是非常合理。兩相對照，反過來也可以發現日本式的缺點所在」
- old_vn (csv3): 「Ra vậy. Hợp lý…… có thể nói là cực kỳ hợp lý.\nĐứng từ góc độ đó, ngược lại cũng thấy được nhược điểm của kiểu Hinamoto.」
- fix: 「Ra vậy. Hợp lý…… có thể nói là cực kỳ hợp lý.\nĐứng từ góc độ đó, ngược lại cũng thấy được nhược điểm của kiểu Hinomoto.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2399 — item T6 (JP: 日ノ本)

- JP: 「だから、冥国式の蒸機と\x%lレイルロオド;#00ffc040;レイルロオド%l;#;とは、\n日ノ本式のお手本にはなれなかったというわけか」
- TW: 「所以美國式的蒸汽機車和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，沒有成為日本式所借鑑的對象」
- old_vn (audit): 「Nên đầu máy hơi nước và \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\nđã không thể trở thành hình mẫu cho kiểu Hinamoto sao.」
- fix: 「Nên đầu máy hơi nước và \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\nđã không thể trở thành hình mẫu cho kiểu Hinomoto sao.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2412 — item T6 (JP: 日ノ本)

- JP: 「ああいうの――あのれんけーって、どこでもそう？\n[ヒノモト,2]日ノ本式の――マスターシステムの\x%lレイルロオド;#00ffc040;レイルロオド%l;#;って」
- TW: 「日本式的——司乘定組體系的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;們，都能像那樣——做到那樣程度的配合嗎？」
- old_vn (csv3): 「Cái kiểu——phối hợp ăn ý như vậy, ở đâu cũng thế hả?\n\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinamoto ấy.」
- fix: 「Cái kiểu——phối hợp ăn ý như vậy, ở đâu cũng thế hả?\n\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinomoto ấy.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2454 — item T6 (JP: 日ノ本)

- JP: 「確かにだ。それが、日ノ本人の一般的な感覚にも[がっち,1]合致\n――ああ、いや」
- TW: 「有道理，這也符合日本人一般的認識。啊，莫非……」
- old_vn (csv3): 「Đúng vậy. Điều đó cũng phù hợp với cảm nhận chung của người Hinamoto\n——à, không.」
- fix: 「Đúng vậy. Điều đó cũng phù hợp với cảm nhận chung của người Hinomoto\n——à, không.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2503 — item T6 (JP: 日ノ本)

- JP: 「ですが、鉄道輸送で最優先されるべきは常に安全です。\n長期的にみれば、日ノ本式の長所は際立つものかと」
- TW: 「然而鐵路運輸最優先的永遠是安全。從長遠的角度而言，日本式的優勢就體現出來了」
- old_vn (csv3): 「Nhưng mà, ưu tiên hàng đầu trong vận tải đường sắt luôn là an toàn.\nNhìn về lâu dài, ưu điểm của kiểu Hinamoto sẽ nổi bật hơn ạ.」
- fix: 「Nhưng mà, ưu tiên hàng đầu trong vận tải đường sắt luôn là an toàn.\nNhìn về lâu dài, ưu điểm của kiểu Hinomoto sẽ nổi bật hơn ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2510 — item T6 (JP: 日ノ本)

- JP: 「と。聞いております。わたくしは[ひのもとしき,3]日ノ本式との\n交流ばかりが多く、詳しくはないのですが」
- TW: 「的確聽說過是這樣的。但我接觸到的主要都是日本式，所以並不是十分清楚」
- old_vn (csv3): 「Em cũng nghe nói vậy. Do em chỉ chủ yếu giao lưu với\nRailord kiểu Hinamoto nên cũng không rành lắm ạ.」
- fix: 「Em cũng nghe nói vậy. Do em chỉ chủ yếu giao lưu với\nRailord kiểu Hinomoto nên cũng không rành lắm ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2585 — item T6 (JP: 日ノ本)

- JP: 「そうですね。冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の、最大の特徴です。\nそもそも、日ノ本式や詠・髑国式とは設計思想が違う」
- TW: 「說得沒錯，那就是美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;最大的特徵。說到底，與日本式、英國式和德國式在設計思想上就有所不同」
- old_vn (audit): 「Đúng vậy. Đó là đặc điểm lớn nhất của \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinamoto, kiểu Anh hay kiểu Đức rồi.」
- fix: 「Đúng vậy. Đó là đặc điểm lớn nhất của \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinomoto, kiểu Anh hay kiểu Đức rồi.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 3115 — item T6 (JP: 日ノ本)

- JP: 日ノ本式では、そのほとんどが廃用を余儀なくされる。\nけれども冥国式ならば、再活用に困らない。
- TW: 對於日本式，遇到這些情況基本除廢棄別無選擇。但是換成美國式，恢復使用就毫無難度了。
- old_vn (audit): Ở kiểu Hinamoto, hầu hết đều buộc phải bỏ đi.\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng.
- fix: Ở kiểu Hinomoto, hầu hết đều buộc phải bỏ đi.\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 01_Hachiroku — `ハチロク04_煙には煙を.txt.toml` (2 dòng)

### key 2464 — item T7 (JP: 湯医)

- JP: 「バーベキュー\x%l列車;#00ffc040;列車%l;#;の折り返し、[ゆのい,1]湯医の発船場から\n御一夜まで、川下り使う人も右肩上がりじゃないですか」
- TW: 「ＢＢＱ\x%l列車;#00ffc040;列車%l;#;折返的時候，選擇利用漂流從湯醫的發船場去御一夜的人不也越來越多了嗎」
- old_vn (unif): 「Lúc \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yui\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」
- fix: 「Lúc \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2947 — item T7 (JP: 湯医)

- JP: 湯医線の短さであれば、\x%lキハ07;#00ffc040;キハ07%l;#;の救援も機能しようし、\n\x%lエアクラ;#00ffc040;エアクラ%l;#;が飛べる場所ならば、ナビも使える。
- TW: 湯醫線很短，所以也可以利用\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;救援，如果\x%lエアクラ;#00ffc040;空凝機%l;#;能飛到，還可以讓Ｎａｖｉ來運送。
- old_vn (csv3): Với chiều dài ngắn ngủi của Tuyến Yui, việc cứu hộ bằng \x%lキハ07;#00ffc040;KiHa 07%l;#; cũng sẽ phát huy tác dụng,\nvà nếu là nơi \x%lエアクラ;#00ffc040;Aircra%l;#; có thể bay tới, thì cũng có thể dùng Navi.
- fix: Với chiều dài ngắn ngủi của Tuyến Yunoi, việc cứu hộ bằng \x%lキハ07;#00ffc040;KiHa 07%l;#; cũng sẽ phát huy tác dụng,\nvà nếu là nơi \x%lエアクラ;#00ffc040;Aircra%l;#; có thể bay tới, thì cũng có thể dùng Navi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク05_レイルロオドたち.txt.toml` (8 dòng)

### key 2260 — item T7 (JP: 湯医)

- JP: 「ハチロクちゃんと[ハチロクニイマル,3]8620での[ゆのい,1]湯医線の走行を、\nオリヴィちゃんはⅨ号機関車で、そのまま再現した？」
- TW: 「也就是說奧莉薇用九號機車，把八六和８６２０在湯醫線上的行駛狀態完整重現了嗎？」
- old_vn (csv3): 「Việc Hachiroku và 8620 chạy trên Tuyến Yui,\nđã được Olivy tái hiện lại y nguyên bằng Đầu máy số 9 sao?」
- fix: 「Việc Hachiroku và 8620 chạy trên Tuyến Yunoi,\nđã được Olivy tái hiện lại y nguyên bằng Đầu máy số 9 sao?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2270 — item T7 (JP: 湯医)

- JP: 「本日の湯医線Ⅸ号機関車試走。\n\x%l機関士;#00ffc040;機関士%l;#;は右田日々姫、\x%l機関助士;#00ffc040;機関助士%l;#;は蓑笠凪の体制でした」
- TW: 「今天九號機車在湯醫線上的行駛測試，是以\x%l機関士;#00ffc040;司機%l;#;右田日日姬，\x%l機関助士;#00ffc040;司爐%l;#;蓑笠凪的配置進行的」
- old_vn (csv3): 「Chuyến chạy thử Đầu máy số 9 trên Tuyến Yui hôm nay.\nĐược thực hiện với đội hình \x%l機関士;#00ffc040;lái tàu%l;#; Migita Hibiki, \x%l機関助士;#00ffc040;phụ lái tàu%l;#; Minokasa Nagi ạ.」
- fix: 「Chuyến chạy thử Đầu máy số 9 trên Tuyến Yunoi hôm nay.\nĐược thực hiện với đội hình \x%l機関士;#00ffc040;lái tàu%l;#; Migita Hibiki, \x%l機関助士;#00ffc040;phụ lái tàu%l;#; Minokasa Nagi ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2484 — item T7 (JP: 湯医)

- JP: 「うむ。目視の視界の問題だ。湯医線の標識・表示類は、\n全て左側運転台を想定して設置されているので――」
- TW: 「嗯，那就是視野的問題。湯醫線上的標誌、指示全都是以駕駛台位於左側為前提設置的——」
- old_vn (csv3): 「Ừm. Là vấn đề về tầm nhìn quan sát. Các loại biển báo, biển chỉ dẫn trên Tuyến Yui,\nđều được lắp đặt dựa trên giả định buồng lái nằm bên trái――」
- fix: 「Ừm. Là vấn đề về tầm nhìn quan sát. Các loại biển báo, biển chỉ dẫn trên Tuyến Yunoi,\nđều được lắp đặt dựa trên giả định buồng lái nằm bên trái――」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2776 — item T7 (JP: 湯医)

- JP: 「はい。必須のことだと思ったので、手配しました。\n湯医線全線、二週間と少しで改善できる予定です」
- TW: 「是的。我覺得這是必要的，就先準備起來了。給我兩個星期多一點的時間，應該就能完成了」
- old_vn (csv3): 「Vâng. Vì tôi nghĩ đó là việc bắt buộc nên đã sắp xếp rồi.\nDự kiến toàn Tuyến Yui sẽ được cải thiện trong vòng hơn hai tuần nữa.」
- fix: 「Vâng. Vì tôi nghĩ đó là việc bắt buộc nên đã sắp xếp rồi.\nDự kiến toàn Tuyến Yunoi sẽ được cải thiện trong vòng hơn hai tuần nữa.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2796 — item T7 (JP: 湯医)

- JP: 「湯医線での試験走行にも期待しています。\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;・オリヴィ」
- TW: 「期待你在湯醫線行駛測試的成果。\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;奧莉薇」
- old_vn (csv3): 「Em cũng rất mong chờ chuyến chạy thử trên Tuyến Yui.\n\x%lレイルロオド;#00ffc040;Railord%l;#; Olivy.」
- fix: 「Em cũng rất mong chờ chuyến chạy thử trên Tuyến Yunoi.\n\x%lレイルロオド;#00ffc040;Railord%l;#; Olivy.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2839 — item T7 (JP: 湯医)

- JP: 「ふかみ様がどのような理由で、\n湯医線の線見にご同行されたのでしょうか？」
- TW: 「深美小姐她，為什麼會和你們一起去進行湯醫線踏查呢？」
- old_vn (csv3): 「Fukami đã đi cùng chuyến khảo sát Tuyến Yui\nvì lý do gì vậy ạ?」
- fix: 「Fukami đã đi cùng chuyến khảo sát Tuyến Yunoi\nvì lý do gì vậy ạ?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2912 — item T7 (JP: 湯医)

- JP: 「湯医線の営業運転の目処が完全についてから。改めて、\nオリヴィちゃんにも習熟運転に立ちあってもらって。で」
- TW: 「等到湯醫線的商業運營都穩定下來，到時再讓奧莉薇帶著你們去熟悉好了」
- old_vn (csv3): 「Đợi đến khi hoạt động thương mại trên Tuyến Yui hoàn toàn ổn định đã. Rồi sau đó,\nsẽ nhờ bé Olivy hỗ trợ trong quá trình chạy làm quen. Vậy nhé.」
- fix: 「Đợi đến khi hoạt động thương mại trên Tuyến Yunoi hoàn toàn ổn định đã. Rồi sau đó,\nsẽ nhờ bé Olivy hỗ trợ trong quá trình chạy làm quen. Vậy nhé.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3010 — item T15 (JP: 小畑)

- JP: 「確かにその方がより安全だな。オリヴィは直近でも、\n補機有りでとはいえ、小畑を越えているのだし」
- TW: 「這樣的確更安全一些。雖說當時掛了補機，但奧莉薇也是能夠親自翻越過大畑的」
- old_vn (csv3): 「Quả thực làm vậy sẽ an toàn hơn. Dù sao thì gần đây Olivy\ncũng đã vượt qua đèo Kobata, dù là có đầu máy phụ hỗ trợ.」
- fix: 「Quả thực làm vậy sẽ an toàn hơn. Dù sao thì gần đây Olivy\ncũng đã vượt qua đèo Okoba, dù là có đầu máy phụ hỗ trợ.」
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク05_軋み.txt.toml` (4 dòng)

### key 1178 — item T20 (JP: 堰)

- JP: ……ふかみの祖父たち、堰さんとそのご兄弟とは、\n水と土との専門家だ。
- TW: ……深美的祖父——堰先生和他的兄弟是水文與地質方面的專家。
- old_vn (csv3): （……Ông nội của Fukami, ông Seki và anh em của ông ấy,\nlà những chuyên gia về nước và đất.）
- fix: （……Ông ngoại của Fukami, ông Seki và anh em của ông ấy,\nlà những chuyên gia về nước và đất.）
- Lý do: JP chứa 堰 / 祖父 — dòng Seki; VN cũ dùng "ông nội" → đổi thành "ông ngoại" theo T20 (DECIDED 20/11 ~19:15, Hieu; CHỈ các dòng Seki).

### key 1755 — item T7 (JP: 湯医)

- JP: 「[ゆのい,1]湯医線は負荷の少ない路線です。\n振動は機関車側にしか出ずに済みます」
- TW: 「湯醫線是一條負荷比較輕的線路。我有辦法讓震動不傳到車廂」
- old_vn (csv3): 「Tuyến Yui là tuyến đường có tải trọng thấp.\nĐộ rung lắc sẽ chỉ xuất hiện ở phía đầu máy hơi nước thôi ạ.」
- fix: 「Tuyến Yunoi là tuyến đường có tải trọng thấp.\nĐộ rung lắc sẽ chỉ xuất hiện ở phía đầu máy hơi nước thôi ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2518 — item T7 (JP: 湯医)

- JP: 今はともかく、何事もなく湯医駅まで持っていくこと。\nそれだけに、気持ちの全てを集中させる。
- TW: 現在還是先集中所有精力把列車平安地開到湯醫站吧。
- old_vn (csv3): （Bây giờ cứ gác lại đã, phải đưa tàu đến ga Yui an toàn.\nTôi dồn toàn bộ tâm trí vào việc đó.）
- fix: （Bây giờ cứ gác lại đã, phải đưa tàu đến ga Yunoi an toàn.\nTôi dồn toàn bộ tâm trí vào việc đó.）
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2726 — item T7 (JP: 湯医)

- JP: （まぁ、もうすぐ湯医――携帯ももう通じる範囲だ。\nもしも何かあったのなら、永山夫人が知らせてくれよう）
- TW: （反正馬上就到湯醫了——手機也已經有信號了。要是出了什麼事，永山夫人會打電話過來的）
- old_vn (csv3): （Mà, sắp đến Yui rồi——cũng sắp vào vùng có sóng điện thoại rồi.\nNếu có chuyện gì, chắc phu nhân Nagayama sẽ báo cho mình biết thôi.）
- fix: （Mà, sắp đến Yunoi rồi——cũng sắp vào vùng có sóng điện thoại rồi.\nNếu có chuyện gì, chắc phu nhân Nagayama sẽ báo cho mình biết thôi.）
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク06_それぞれの傷跡.txt.toml` (2 dòng)

### key 1801 — item T7 (JP: 湯医)

- JP: 「はい、鉱山鉄道時代と違って、この湯医線ですから……\nどっちをとっても安全だって計算は出来てます」
- TW: 「是的，畢竟和在礦山鐵路時期不同，現在是在湯醫線上行駛的……經過計算，兩種方式都是安全的」
- old_vn (csv3): 「Vâng, khác với thời ở đường sắt khai thác mỏ, vì đây là tuyến Yui……\nNên dù chọn cách nào thì chúng tôi cũng đã tính toán được là sẽ an toàn.」
- fix: 「Vâng, khác với thời ở đường sắt khai thác mỏ, vì đây là tuyến Yunoi……\nNên dù chọn cách nào thì chúng tôi cũng đã tính toán được là sẽ an toàn.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2710 — item T7 (JP: 湯医)

- JP: 驚かされるが、考えてみれば\n御一夜-湯医は路線長でも二十と数キロ。
- TW: 著實嚇我一跳，不過想來御一夜到湯醫雖不近，但也不過二十幾公里。
- old_vn (unif): Tuy hơi bất ngờ, nhưng nghĩ lại thì\ntuyến Ohitoyo - Yui cũng chỉ dài khoảng hai mươi mấy kilomet.
- fix: Tuy hơi bất ngờ, nhưng nghĩ lại thì\ntuyến Ohitoyo - Yunoi cũng chỉ dài khoảng hai mươi mấy kilomet.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク06_のぞみ.txt.toml` (2 dòng)

### key 2139 — item T47 (JP: 主幹制御器)

- JP: 「しゅかんせいぎょき――」
- TW: 「主控——」
- old_vn (csv3): 「Bộ điều khiển trung tâm――」
- fix: 「Điều khiển trung tâm――」
- Lý do: JP chứa マスコン / マスターコントローラー / 主幹制御器; VN cũ dùng dạng cũ → đổi thành "điều khiển trung tâm" theo T47 (DECIDED, khóa B15).
- Lưu ý: JP dòng này chỉ có ruby しゅかんせいぎょき (không có kanji 主幹制御器 trong dòng), TW 主控 xác nhận thuật ngữ — xem quyết định D1.

### key 2763 — item T47 (JP: 主幹制御器)

- JP: 「制御系は、機械的・非感覚的な方が高効率。\nそん発想をもう一歩推し進めたのが――[しゅかんせいぎょき,4]主幹制御器」
- TW: 「論操控來說，控制起來更機械、更死板的產品操控起來效率更高。而將這個方針延續下去的產物——就是主控」
- old_vn (csv3): 「Hệ thống điều khiển càng mang tính máy móc, phi cảm giác thì hiệu suất càng cao.\nVà thứ đẩy mạnh ý tưởng đó lên một bước nữa chính là――Bộ điều khiển trung tâm.」
- fix: 「Hệ thống điều khiển càng mang tính máy móc, phi cảm giác thì hiệu suất càng cao.\nVà thứ đẩy mạnh ý tưởng đó lên một bước nữa chính là――Điều khiển trung tâm.」
- Lý do: JP chứa マスコン / マスターコントローラー / 主幹制御器; VN cũ dùng dạng cũ → đổi thành "điều khiển trung tâm" theo T47 (DECIDED, khóa B15).

## 01_Hachiroku — `ハチロク08_教導.txt.toml` (13 dòng)

### key 1351 — item T7 (JP: ユノイ)

- JP: 「『トンネルがなくて、橋梁がおおいユノイ線。\n\x%l保線;#00ffc040;保線%l;#;する上で、一番』」
- TW: 「“湯醫線上橋樑眾多，沒有一處隧道，於是\x%l保線;#00ffc040;巡線%l;#;上最應當注意的是？”」
- old_vn (audit): 「『Tuyến Yui không có hầm chui, nhưng lại có rất nhiều cầu đường sắt.\nTrong việc \x%l保線;#00ffc040;bảo trì đường ray%l;#;, quan trọng nhất』」
- fix: 「『Tuyến Yunoi không có hầm chui, nhưng lại có rất nhiều cầu đường sắt.\nTrong việc \x%l保線;#00ffc040;bảo trì đường ray%l;#;, quan trọng nhất』」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1379 — item T7 (JP: ユノイ)

- JP: 「……ユノイ線ができてからずっととかだとムツカシそう。\nけど、急に起こるようになったとかなら」
- TW: 「……如果是從湯醫線建成開始就一直存在的問題，那可能很難解決。不過要是突然出現的情況，或許有辦法」
- old_vn (csv3): 「……Nếu chuyện này xảy ra từ hồi tuyến Yui mới xây thì chắc khó giải quyết lắm.\nNhưng nếu dạo gần đây mới bị thì có thể có cách.」
- fix: 「……Nếu chuyện này xảy ra từ hồi tuyến Yunoi mới xây thì chắc khó giải quyết lắm.\nNhưng nếu dạo gần đây mới bị thì có thể có cách.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1966 — item T7 (JP: ユノイ)

- JP: 「みごとセーカイしたソーテツにはボーナスクイズ！\n『ユノイ線にある\x%lポイント;#00ffc040;ポイント%l;#;のソウスウは？』」
- TW: 「作為獎勵，再給雙鐵加一問！“湯醫線上共有多少\x%lポイント;#00ffc040;轉轍器%l;#;？”」
- old_vn (csv3): 「Câu hỏi thưởng cho Soutetsu vì đã trả lời đúng!\n『Tổng số \x%lポイント;#00ffc040;ghi bẻ đường ray%l;#; trên tuyến Yui là bao nhiêu?』」
- fix: 「Câu hỏi thưởng cho Soutetsu vì đã trả lời đúng!\n『Tổng số \x%lポイント;#00ffc040;ghi bẻ đường ray%l;#; trên tuyến Yunoi là bao nhiêu?』」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2302 — item T7 (JP: ユノイ)

- JP: 「わかったー！　じゃ、早いうちに、オリヴィ、\nユノイ線のゴジマン！　舟の上からもみせてもらうねー」
- TW: 「好好！那奧莉薇就趕緊坐一次船，一睹湯醫線的美景」
- old_vn (csv3): 「Biết rồi~! Vậy, Olivy sẽ đi sớm thôi,\nniềm tự hào của tuyến Yui! Cậu cho tớ xem từ trên thuyền luôn nha~」
- fix: 「Biết rồi~! Vậy, Olivy sẽ đi sớm thôi,\nniềm tự hào của tuyến Yunoi! Cậu cho tớ xem từ trên thuyền luôn nha~」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2382 — item T7 (JP: 湯医)

- JP: 「間もなく迎える、Ⅸ号機関車の湯医線営業運転に向け、\n一度でも多く――どうか、添乗に来て欲しい」
- TW: 「希望二位能在百忙之中，儘可能抽出時間，陪同指導九號機車即將開展的湯醫線商業運營」
- old_vn (csv3): 「Hướng tới việc Đầu máy số 9 sắp đi vào hoạt động thương mại trên Tuyến Yui,\ndù chỉ thêm một lần thôi——cũng xin cô hãy đến đi cùng chuyến tàu.」
- fix: 「Hướng tới việc Đầu máy số 9 sắp đi vào hoạt động thương mại trên Tuyến Yunoi,\ndù chỉ thêm một lần thôi——cũng xin cô hãy đến đi cùng chuyến tàu.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2635 — item T7 (JP: ユノイ)

- JP: 「すごくきれー！\nここはきっと、ユノイ線のゴジマンだね～！」
- TW: 「真美！這裡一定是湯醫線的著名景點～！」
- old_vn (csv3): 「Đẹp quá đi~!\nĐây chắc chắn là niềm tự hào của tuyến Yui rồi~!」
- fix: 「Đẹp quá đi~!\nĐây chắc chắn là niềm tự hào của tuyến Yunoi rồi~!」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2794 — item T7 (JP: ユノイ)

- JP: 「それでもすごいよ！　ユノイせんってだって、\n帝鉄時代からでしょお！？」
- TW: 「那也夠厲害的了！湯醫線可是從帝國鐵路時代開始就一直存在的吧！？」
- old_vn (audit): 「Thế cũng siêu lắm rồi! Tuyến Yui á,\ncó từ thời Teitetsu cơ mà!?」
- fix: 「Thế cũng siêu lắm rồi! Tuyến Yunoi á,\ncó từ thời Teitetsu cơ mà!?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2828 — item T7 (JP: ユノイ)

- JP: 「このグループは、オヒトヨ鉄道ユノイ線の\n保線知識があるグループでしょ？　だから、Bグループ」
- TW: 「那麼這一組就是對御一夜鐵路湯醫線的巡線有經驗心得的人沒錯吧？就叫Ｂ組」
- old_vn (unif): 「Nhóm này, là nhóm có kiến thức bảo trì đường ray\ncủa tuyến Yui thuộc Đường sắt Ohitoyo đúng không? Vậy nên, là nhóm B.」
- fix: 「Nhóm này, là nhóm có kiến thức bảo trì đường ray\ncủa tuyến Yunoi thuộc Đường sắt Ohitoyo đúng không? Vậy nên, là nhóm B.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2840 — item T41+T7 (JP: キハ + ユノイ)

- JP: 「8620とキハ07sだけしか列車がなかったいままでと、\nユノイ線以外だって見るこれからはちがうからねー」
- TW: 「雖然以前是只有８６２０和Ｋｉｈａ０７Ｓ兩列，但是以後還得放眼湯醫線以外的路段啦」
- old_vn (csv3): 「Bởi vì từ trước đến nay chỉ có mỗi tàu 8620 và Kiha 07S,\nnhưng từ giờ trở đi sẽ khác, chúng ta còn phải xem xét cả những tuyến khác ngoài tuyến Yui nữa mà~」
- fix: 「Bởi vì từ trước đến nay chỉ có mỗi tàu 8620 và KiHa 07S,\nnhưng từ giờ trở đi sẽ khác, chúng ta còn phải xem xét cả những tuyến khác ngoài tuyến Yunoi nữa mà~」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41. JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Dòng hai mục: đổi cả "Kiha 07S" → "KiHa 07S" (T41) và "tuyến Yui" → "tuyến Yunoi" (T7) trong cùng một fix.

### key 2849 — item T41 (JP: キハ)

- JP: 「双鉄！\nあと十五分で[レイナナ,4]キハ07sば来よるぞー！」
- TW: 「雙鐵！再過１５分鐘Ｋｉｈａ０７Ｓ就要開過來了！」
- old_vn (csv3): 「Soutetsu!\n15 phút nữa là Kiha 07S đến đó!」
- fix: 「Soutetsu!\n15 phút nữa là KiHa 07S đến đó!」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 2850 — item T7 (JP: 湯医)

- JP: 「あとみっつあるじゃろ、双鉄。\n湯医の\x%l三角線;#00ffc040;三角線%l;#;まわりに」
- TW: 「雙鐵，還有三處咧。就是湯醫\x%l三角線;#00ffc040;三角線%l;#;那裡」
- old_vn (csv3): 「Còn 3 cái nữa mà Soutetsu.\nỞ khu vực \x%l三角線;#00ffc040;đường tam giác%l;#; Yui ấy.」
- fix: 「Còn 3 cái nữa mà Soutetsu.\nỞ khu vực \x%l三角線;#00ffc040;đường tam giác%l;#; Yunoi ấy.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2868 — item T7 (JP: ユノイ)

- JP: 「オケー！　そしたらいくよ～！　保線クイズ、第一問！『オヒトヨ鉄道ユノイ線にあるトンネルの数は』」
- TW: 「ＯＫ！那麼就開始提問～！巡線競猜第一題！“御一夜鐵路湯醫線一共有多少隧道？”」
- old_vn (unif): 「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yui của Đường sắt Ohitoyo là bao nhiêu?』」
- fix: 「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yunoi của Đường sắt Ohitoyo là bao nhiêu?』」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3335 — item T7 (JP: 湯医)

- JP: 僕は湯医線でしか乗務をしたことが無いゆえ、\n当然の景色と感じていたが――
- TW: 由於我只在湯醫線負責乘務，早把這麼多橋樑當成是理所當然的景象——
- old_vn (csv3): Vì tôi chỉ làm nhiệm vụ trên tuyến Yui,\nnên cứ ngỡ đó là cảnh sắc đương nhiên——
- fix: Vì tôi chỉ làm nhiệm vụ trên tuyến Yunoi,\nnên cứ ngỡ đó là cảnh sắc đương nhiên——
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク10_旺宮鉄道歴史館.txt.toml` (3 dòng)

### key 1529 — item T6 (JP: 日ノ本)

- JP: 「……日ノ本の鉄道営業法は、\n詠国を見本に作られているのですよね？　恐らく」
- TW: 「……想必日本的鐵路運營法，也是仿照英國的法規制定的吧？」
- old_vn (csv3): 「……Luật kinh doanh đường sắt của Hinamoto,\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」
- fix: 「……Luật kinh doanh đường sắt của Hinomoto,\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 1994 — item T6 (JP: 日ノ本)

- JP: 「全て、とは――\n日ノ本\x%l蒸機;#00ffc040;蒸機%l;#;のものも――ですか？」
- TW: 「一切是指——包括日本\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;的鐵路人偶，是嗎？」
- old_vn (csv3): 「Tất cả, là——\nbao gồm cả của \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; Hinamoto——sao ạ?」
- fix: 「Tất cả, là——\nbao gồm cả của \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; Hinomoto——sao ạ?」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2488 — item T6 (JP: 日ノ本)

- JP: 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は優れたものだ。実際、今の日ノ本では、\nあらゆる場所で、引退した\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が活躍――っ！」
- TW: 「按說\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;著實是性能優異，即使在當今日本，也有不少離開崗位的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;在各行各業——！」
- old_vn (audit): 「\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinamoto hiện tại,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」
- fix: 「\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinomoto hiện tại,\ncác \x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).
- Lưu ý: dòng có gasp Ư (audit thêm "——Ư!") — chỉ đổi "Hinamoto", Ư giữ nguyên, không đụng.

## 01_Hachiroku — `ハチロク10_炙り出し.txt.toml` (4 dòng)

### key 1793 — item T6 (JP: 日ノ本)

- JP: 「はい。大傑作の貨物機です。日ノ本のあらゆる場所で、\nあらゆる貨物を。恐らくは今も、輸送している子達です」
- TW: 「嗯，它是非常優秀的貨運機車。她們過去一直將各種貨物運送到日本各地，恐怕現在仍是如此」
- old_vn (csv3): 「Vâng. Một kiệt tác đầu máy hàng hóa ạ. Các em ấy đã vận chuyển đủ loại hàng hóa,\nđến khắp mọi nơi trên đất nước Hinamoto. Có lẽ ngay cả bây giờ, các em ấy vẫn đang tiếp tục công việc đó.」
- fix: 「Vâng. Một kiệt tác đầu máy hàng hóa ạ. Các em ấy đã vận chuyển đủ loại hàng hóa,\nđến khắp mọi nơi trên đất nước Hinomoto. Có lẽ ngay cả bây giờ, các em ấy vẫn đang tiếp tục công việc đó.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 1868 — item T6 (JP: 日ノ本)

- JP: 「日ノ本車輌から来てくださった技術者さんでしたか」
- TW: 「您是從日本車輛製造來的技術人員吧」
- old_vn (csv3): 「Ông là kỹ sư đến từ công ty Toa xe Hinamoto phải không ạ.」
- fix: 「Ông là kỹ sư đến từ công ty Toa xe Hinomoto phải không ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 1930 — item T6 (JP: 日ノ本)

- JP: 「おはようございます！\n日ノ本車輌さんから返信、来てます」
- TW: 「早安！日本車輛製造那邊給我們回復了」
- old_vn (csv3): 「Chào buổi sáng!\nCó thư phản hồi từ công ty Toa xe Hinamoto rồi ạ.」
- fix: 「Chào buổi sáng!\nCó thư phản hồi từ công ty Toa xe Hinomoto rồi ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2801 — item T6 (JP: 日ノ本)

- JP: 日ノ本車輌に送られていくのを待つだけの、\n歪み、傷つきまくった\x%l台枠;#00ffc040;台枠%l;#;。
- TW: 那個將要送去日本車輛製造的傷痕累累、已經變形了的\x%l台枠;#00ffc040;車架%l;#;。
- old_vn (csv3): Một chiếc \x%l台枠;#00ffc040;khung gầm%l;#; méo mó, đầy vết xước,\nchỉ đang chờ được gửi đến công ty Toa xe Hinamoto.
- fix: Một chiếc \x%l台枠;#00ffc040;khung gầm%l;#; méo mó, đầy vết xước,\nchỉ đang chờ được gửi đến công ty Toa xe Hinomoto.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 01_Hachiroku — `ハチロク11_幽霊.txt.toml` (1 dòng)

### key 2370 — item T6 (JP: 日ノ本)

- JP: 聴診器のような部品の根元のモニタの表示を、\n技工さん――日ノ本車輌の淵様に見せてらっしゃいます。
- TW: 他們正在把連在形似聽診器的工具末端的顯示器拿給技工——也就是日本車輛製造的淵先生看。
- old_vn (csv3): Họ đang cho thợ cơ khí——ông Fuchi của công ty Toa xe Hinamoto xem\nmàn hình hiển thị gắn ở gốc của bộ phận giống như ống nghe.
- fix: Họ đang cho thợ cơ khí——ông Fuchi của công ty Toa xe Hinomoto xem\nmàn hình hiển thị gắn ở gốc của bộ phận giống như ống nghe.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 01_Hachiroku — `ハチロク12_再開発.txt.toml` (3 dòng)

### key 2464 — item T7 (JP: 湯医)

- JP: 「ああ……試験初期の段階で、\n一気に[ゆのい,1]湯医まで走らせるのは避けたいな」
- TW: 「這個啊……在測試初期，最好還是別一口氣開到湯醫那麼遠」
- old_vn (csv3): 「À…… Ở giai đoạn đầu chạy thử,\ntôi muốn tránh việc chạy một mạch đến Yui.」
- fix: 「À…… Ở giai đoạn đầu chạy thử,\ntôi muốn tránh việc chạy một mạch đến Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2508 — item T7 (JP: 湯医)

- JP: 「術仙炭鉱廃駅どまりだと、[ゆのい,1]湯医まで行っての折り返しと、\n後進で御一夜まで戻るのと……いずれがよろしいかと」
- TW: 「開到術仙煤礦廢車站之後，是索性開到湯醫後折返，還是倒車返回御一夜……哪種方法更合適」
- old_vn (audit): 「Nếu chỉ đến ga bỏ hoang mỏ than Jutsu-sen, thì nên chạy tiếp đến Yui rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」
- fix: 「Nếu chỉ đến ga bỏ hoang mỏ than Jutsu-sen, thì nên chạy tiếp đến Yunoi rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2853 — item T7 (JP: 湯医)

- JP: 湯医線の、他のほとんどの廃駅と違い、\n駅舎は、かなりしっかりしている。
- TW: 和湯醫線上其他大多數廢車站不同，這座車站建得還是很有模有樣的。
- old_vn (csv3): Khác với hầu hết các ga bỏ hoang trên tuyến Yui,\nnhà ga này được xây dựng khá kiên cố.
- fix: Khác với hầu hết các ga bỏ hoang trên tuyến Yunoi,\nnhà ga này được xây dựng khá kiên cố.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク13_夜の嵐.txt.toml` (6 dòng)

### key 2326 — item T11 (JP: 運転体)

- JP: それを見届けハチロクは、\x%lタブレット;#00ffc040;タブレット%l;#;を換え、\n\x%l運転体;#00ffc040;運転体%l;#;に戻って声を引き締める。
- TW: 八六見狀，又將\x%lタブレット;#00ffc040;操作板%l;#;換到了\x%l運転体;#00ffc040;駕駛體%l;#;上，嚴肅地說。
- old_vn (csv3): Thấy vậy, Hachiroku đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#;,\ntrở lại \x%l運転体;#00ffc040;thân điều khiển%l;#; và cất giọng nghiêm túc.
- fix: Thấy vậy, Hachiroku đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#;,\ntrở lại \x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 2328 — item T11 (JP: 運転体)

- JP: それを見届けハチロクは、\n\x%lタブレット;#00ffc040;タブレット%l;#;を外し\x%l運転体;#00ffc040;運転体%l;#;へと。
- TW: 八六見狀，自己取出了\x%lタブレット;#00ffc040;操作板%l;#;換到\x%l運転体;#00ffc040;駕駛體%l;#;上。
- old_vn (csv3): Thấy vậy, Hachiroku\ntháo \x%lタブレット;#00ffc040;thẻ bảng%l;#; ra và chuyển sang \x%l運転体;#00ffc040;thân điều khiển%l;#;.
- fix: Thấy vậy, Hachiroku\ntháo \x%lタブレット;#00ffc040;thẻ bảng%l;#; ra và chuyển sang \x%l運転体;#00ffc040;thân vận hành%l;#;.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 2336 — item T12 (JP: 整備体)

- JP: ハチロクはすぐ\x%l整備体;#00ffc040;整備体%l;#;へとまた\x%lタブレット;#00ffc040;タブレット%l;#;を入れ替える。\nだったら僕は、またワンスコを握るしか無い。
- TW: 八六馬上又將\x%lタブレット;#00ffc040;操作板%l;#;換到\x%l整備体;#00ffc040;整備體%l;#;身上。看來我又得拿起公斤鍬了。
- old_vn (csv3): Hachiroku lập tức chuyển \x%lタブレット;#00ffc040;thẻ bảng%l;#; về lại \x%l整備体;#00ffc040;thân chính%l;#;.\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi.
- fix: Hachiroku lập tức chuyển \x%lタブレット;#00ffc040;thẻ bảng%l;#; về lại \x%l整備体;#00ffc040;thân bảo trì%l;#;.\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi.
- Lý do: JP chứa 整備体 / 整備ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân bảo trì" theo T12 (DECIDED 22/11 ~04:03, Hieu).

### key 2427 — item T11 (JP: 運転体)

- JP: \x%l運転体;#00ffc040;運転体%l;#;のときには気づかなかったが――
- TW: 她使用\x%l運転体;#00ffc040;駕駛體%l;#;的時候我還沒有注意到——
- old_vn (audit): Khi ở \x%l運転体;#00ffc040;thân điều khiển%l;#; thì tôi không nhận ra——
- fix: Khi ở \x%l運転体;#00ffc040;thân vận hành%l;#; thì tôi không nhận ra——
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 2555 — item T11 (JP: 運転体)

- JP: \x%l運転体;#00ffc040;運転体%l;#;を\x%l乗務鞄;#00ffc040;乗務鞄%l;#;に大事にしまい、\nさて――と立っても、まだハチロクは立ち上がらない。
- TW: 我把\x%l運転体;#00ffc040;駕駛體%l;#;小心翼翼地收入\x%l乗務鞄;#00ffc040;乘務包%l;#;中。站了起來——但是八六並沒有隨我起身。
- old_vn (audit): Tôi cất cẩn thận \x%l運転体;#00ffc040;thân điều khiển%l;#; vào \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên.
- fix: Tôi cất cẩn thận \x%l運転体;#00ffc040;thân vận hành%l;#; vào \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 2742 — item T11 (JP: 運転体)

- JP: その一言で、\nセンサーの良い\x%l運転体;#00ffc040;運転体%l;#;へと換装をした理由を悟る。
- TW: 聽她這麼說，我就明白了她為什麼要換上感官靈敏的\x%l運転体;#00ffc040;駕駛體%l;#;。
- old_vn (csv3): Chỉ một câu đó,\ntôi đã hiểu lý do em ấy đổi sang \x%l運転体;#00ffc040;thân điều khiển%l;#; có cảm biến tốt hơn.
- fix: Chỉ một câu đó,\ntôi đã hiểu lý do em ấy đổi sang \x%l運転体;#00ffc040;thân vận hành%l;#; có cảm biến tốt hơn.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

## 01_Hachiroku — `ハチロク13_実りの秋.txt.toml` (1 dòng)

### key 2102 — item T7 (JP: 湯医)

- JP: 「[ゆのい,1]湯医発[おひとよ,2]御一夜いきは乗車率65％。いつもより少し軽い。\n天気は晴れ、線路のコンディションは良好」
- TW: 「由湯醫發往御一夜的列車上座率６５％，比平常稍低一些。天氣晴朗，線路狀況良好」
- old_vn (csv3): 「Chuyến từ Yui đi Ohitoyo có tỷ lệ lấp đầy là 65%. Nhẹ hơn mọi khi một chút.\nThời tiết nắng ráo, tình trạng đường ray tốt.」
- fix: 「Chuyến từ Yunoi đi Ohitoyo có tỷ lệ lấp đầy là 65%. Nhẹ hơn mọi khi một chút.\nThời tiết nắng ráo, tình trạng đường ray tốt.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク14_冬.txt.toml` (1 dòng)

### key 3680 — item T7 (JP: 湯医)

- JP: 本当に皆、驚くほどに積極的に協力を申し出てくれた。\n御一夜の人たちだけでなく、湯医や術仙の人たちまでも。
- TW: 大家積極配合的態度完全超乎了我的想像，不止是御一夜，就連湯醫和術仙的民眾也都參與其中。
- old_vn (unif): Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\nKhông chỉ người dân Ohitoyo, mà cả người dân Yui và Jutsusen nữa.
- fix: Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\nKhông chỉ người dân Ohitoyo, mà cả người dân Yunoi và Jutsusen nữa.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク15a_痛みとの決別.txt.toml` (3 dòng)

### key 1455 — item T15 (JP: 小畑)

- JP: 「『総合的に、噴火や水蒸気爆発等が小畑線の安全を\nただちに脅かす可能性は、極めて低いと推測できる』」
- TW: 「“總體來看，大畑線馬上受到火山噴發和蒸汽噴發等安全威脅的可能性很低”」
- old_vn (csv3): 「『Đánh giá tổng thể, có thể suy đoán khả năng các vụ phun trào hay nổ hơi nước\nđe dọa trực tiếp đến sự an toàn của tuyến Obata là cực kỳ thấp』」
- fix: 「『Đánh giá tổng thể, có thể suy đoán khả năng các vụ phun trào hay nổ hơi nước\nđe dọa trực tiếp đến sự an toàn của tuyến Okoba là cực kỳ thấp』」
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu).

### key 1842 — item T15+T7 (JP: 小畑 + 湯医)

- JP: 「湯医線と比し、小畑線の保線費用は極めて高い。\n観光集客が望めなくなれば、赤字の垂れ流しの始まりだ」
- TW: 「和湯醫線比起來，大畑線的巡線費用非常高。一旦遊客變少，赤字雪球就會越滾越大」
- old_vn (csv3): 「So với tuyến Yui, chi phí bảo trì đường ray của tuyến Obata cực kỳ cao.\nNếu không thu hút được khách du lịch, thì đó sẽ là sự khởi đầu cho việc thâm hụt kéo dài」
- fix: 「So với tuyến Yunoi, chi phí bảo trì đường ray của tuyến Okoba cực kỳ cao.\nNếu không thu hút được khách du lịch, thì đó sẽ là sự khởi đầu cho việc thâm hụt kéo dài」
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu). JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Dòng hai mục: đổi cả "tuyến Yui" → "tuyến Yunoi" (T7) và "tuyến Obata" → "tuyến Okoba" (T15) trong cùng một fix.

### key 2129 — item T7 (JP: 湯医)

- JP: 「湯医線はまかせてくださぁい。\nれいな、いくらでも代走しちゃいますよぉ」
- TW: 「湯醫線就交給玲奈吧。隨時接班都沒有問題的」
- old_vn (csv3): 「Tuyến Yui cứ giao cho em.\nReina có thể chạy thay bao nhiêu chuyến cũng được ạ」
- fix: 「Tuyến Yunoi cứ giao cho em.\nReina có thể chạy thay bao nhiêu chuyến cũng được ạ」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク15b_さよなら列車.txt.toml` (1 dòng)

### key 1999 — item T15 (JP: 小畑)

- JP: それでも少しも緩むことなく、みかん鉄道の\x%lC12;#00ffc040;C12%l;#;は、\n小畑線へと進入し、御一夜へ向け、屋岳の坂に挑んでいく。
- TW: 但橙鐵路的\x%lC12;#00ffc040;Ｃ１２%l;#;還是按時發車，進入了大畑線，朝著御一夜方向行駛，去挑戰矢岳的坡道。
- old_vn (unif): Dù vậy, không hề chùn bước, chiếc \x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\ntiến vào tuyến Obata, hướng về Ohitoyo, thách thức con dốc Yadake.
- fix: Dù vậy, không hề chùn bước, chiếc \x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\ntiến vào tuyến Okoba, hướng về Ohitoyo, thách thức con dốc Yadake.
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu).

## 01_Hachiroku — `ハチロク16_春.txt.toml` (4 dòng)

### key 1622 — item T7 (JP: 湯医)

- JP: 「しかし、湯医線でなら望みがあろう。\n沿線人口が順調に増え、[おおいた,1]大板方面に延伸し――」
- TW: 「但是，湯醫線的話還有希望。如果沿線人口順利增加，能延伸到大分方向——」
- old_vn (csv3): 「Nhưng nếu là tuyến Yui thì vẫn còn hy vọng.\nDân số dọc tuyến đường đang tăng đều đặn, nếu kéo dài về phía Oita――」
- fix: 「Nhưng nếu là tuyến Yunoi thì vẫn còn hy vọng.\nDân số dọc tuyến đường đang tăng đều đặn, nếu kéo dài về phía Oita――」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1987 — item T7 (JP: 湯医)

- JP: 「電化なんて、湯医線でも[おこば,1]小畑線でもできんでしょう。\nどーやったって採算とれなくなるけん」
- TW: 「湯醫線和大畑線的電力化又沒辦法完成。反正是回不了本的」
- old_vn (csv3): 「Việc điện khí hóa, cả tuyến Yui lẫn tuyến Okoba đều không thể làm được đâu.\nDù làm cách nào thì cũng không thể thu hồi vốn được.」
- fix: 「Việc điện khí hóa, cả tuyến Yunoi lẫn tuyến Okoba đều không thể làm được đâu.\nDù làm cách nào thì cũng không thể thu hồi vốn được.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2403 — item T7 (JP: 湯医)

- JP: 湯医側から入線してくる『バーベキューオリヴィ』――\nⅨ号機関車の小さな機影を、一番近くで出迎えようと。
- TW: 在那邊，“ＢＢＱ奧莉薇”正從湯醫駛來準備進站——而她則是站在了小小的九號進站時會最先駛過的位置邊上。
- old_vn (csv3): Chuyến tàu 『BBQ Olivy』 đang tiến vào ga từ phía Yui――\nCô bé định đón bóng dáng nhỏ bé của đầu máy số 9 ở khoảng cách gần nhất.
- fix: Chuyến tàu 『BBQ Olivy』 đang tiến vào ga từ phía Yunoi――\nCô bé định đón bóng dáng nhỏ bé của đầu máy số 9 ở khoảng cách gần nhất.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2587 — item T7 (JP: 湯医)

- JP: 湯医線ではもういっぱしの\x%l機関士;#00ffc040;機関士%l;#;となった日々姫でも、\n小畑線には、やはり苦戦を強いられる。
- TW: 日日姬的\x%l機関士;#00ffc040;司機%l;#;技術在湯醫線已經夠用，但她在大畑線果然還是陷入了苦戰。
- old_vn (csv3): Dù đã trở thành một \x%l機関士;#00ffc040;lái tàu%l;#; thực thụ trên tuyến Yui, nhưng Hibiki\nvẫn phải chật vật khi đối mặt với tuyến Okoba.
- fix: Dù đã trở thành một \x%l機関士;#00ffc040;lái tàu%l;#; thực thụ trên tuyến Yunoi, nhưng Hibiki\nvẫn phải chật vật khi đối mặt với tuyến Okoba.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 02_Hibiki — `日々姫01_リゾート食堂列車計画.txt.toml` (1 dòng)

### key 2225 — item T15 (JP: 小畑)

- JP: 御一夜鉄道が主体となっての\n御一夜-小畑-早戸間の復線。
- TW: 恢復以御一夜鐵路為主體的御一夜—大畑—隼人區段的廢線。
- old_vn (unif): Khôi phục tuyến đường giữa Ohitoyo - Obata - Hayato\ndo Đường sắt Ohitoyo làm chủ thể.
- fix: Khôi phục tuyến đường giữa Ohitoyo - Okoba - Hayato\ndo Đường sắt Ohitoyo làm chủ thể.
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu).

## 02_Hibiki — `日々姫03_客車手配.txt.toml` (1 dòng)

### key 2834 — item T19 (JP: 乗員)

- JP: 「フィッティングもしていない、しかも改造\x%l客車;#00ffc040;客車%l;#;で、\n乗員の練度も全く足りていないのですから」
- TW: 「這節改造而成的\x%l客車;#00ffc040;客運車廂%l;#;既沒有進行磨合運行，其乘務組的熟練度也還完全不夠」
- old_vn (csv3): 「Bởi vì chúng ta chưa hề chạy thử, hơn nữa đây lại là \x%l客車;#00ffc040;toa hành khách%l;#; cải tạo,\nvà trình độ của phi hành đoàn cũng hoàn toàn chưa đủ ạ.」
- fix: 「Bởi vì chúng ta chưa hề chạy thử, hơn nữa đây lại là \x%l客車;#00ffc040;toa hành khách%l;#; cải tạo,\nvà trình độ của nhân viên tàu cũng hoàn toàn chưa đủ ạ.」
- Lý do: JP chứa 乗員; VN cũ dùng "phi hành đoàn" → đổi thành "nhân viên tàu" theo T19 (DECIDED 20/11 ~19:15, Hieu; không bao giờ "phi hành đoàn").

## 02_Hibiki — `日々姫04_カフェキッチン.txt.toml` (2 dòng)

### key 1918 — item T41 (JP: キハ)

- JP: 「うん。写真とか絵。[ハチロク,3]8620とか、[レイナナ,4]キハ07sとか、\nみかん鉄道から乗り入れてきてくれるこたちとかの」
- TW: 「嗯。像[八六,3]８６２０啊，[０７,6]Ｋｉｈａ０７Ｓ啊，還有從橙鐵路開進來的火車，店要貼上這些孩子的照片和畫」
- old_vn (csv3): 「Vâng. Ảnh chụp hay tranh vẽ. Như 8620, Kiha 07S,\nhay những toa xe chạy từ Đường sắt Mikan sang chẳng hạn.」
- fix: 「Vâng. Ảnh chụp hay tranh vẽ. Như 8620, KiHa 07S,\nhay những toa xe chạy từ Đường sắt Mikan sang chẳng hạn.」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 2219 — item T41 (JP: キハ)

- JP: 「ひょっとして――ベージュと柿色。\n\x%lキハ07s;#00ffc040;キハ07s%l;#;の二色の塗り分けに、ですか？」
- TW: 「該不會……是代表\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;的米黃色和赤褐色吧？」
- old_vn (audit): Có khi nào là——màu be và màu vàng cam. Được sơn thành hai màu của \x%lキハ07s;#00ffc040;Kiha 07S%l;#; sao ạ?
- fix: Có khi nào là——màu be và màu vàng cam. Được sơn thành hai màu của \x%lキハ07s;#00ffc040;KiHa 07S%l;#; sao ạ?
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 02_Hibiki — `日々姫06_日々姫の決断.txt.toml` (2 dòng)

### key 2628 — item T6 (JP: 日ノ本)

- JP: 「他の国がどうであるかは存じませんが、日ノ本における\n学問は、確かにそうしたものと認識しております」
- TW: 「我不清楚別的國家怎麼樣，不過我知道日本的學校確實就是那樣」
- old_vn (csv3): 「Em không rõ ở các quốc gia khác thì thế nào, nhưng nền giáo dục ở Hinamoto\nquả thực được nhận thức như vậy ạ.」
- fix: 「Em không rõ ở các quốc gia khác thì thế nào, nhưng nền giáo dục ở Hinomoto\nquả thực được nhận thức như vậy ạ.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2709 — item T6 (JP: 日ノ本)

- JP: 「日ノ本の学園は、もともと、職業適性を見出すことと、\nそれを見出すための学習と訓練に特化してますよね？」
- TW: 「日本的學校本來就會集中精力探求學生的職業傾向，並且重視能夠找出這種傾向的學習和訓練吧？」
- old_vn (csv3): 「Trường học ở Hinamoto vốn dĩ chuyên về việc tìm ra năng lực nghề nghiệp,\nvà những bài học, huấn luyện để tìm ra điều đó đúng không?」
- fix: 「Trường học ở Hinomoto vốn dĩ chuyên về việc tìm ra năng lực nghề nghiệp,\nvà những bài học, huấn luyện để tìm ra điều đó đúng không?」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 02_Hibiki — `日々姫08_とれいん食堂.txt.toml` (6 dòng)

### key 2051 — item T7 (JP: 湯医)

- JP: 「普通車としての湯医駅発が0545。御一夜着が0645。\n客扱いののち、食堂列車に変わっての発車が0700」
- TW: 「作為普通車從湯醫站始發的時間是０５４５。０６４５到達御一夜。客人上下車完成後，０７００變為食堂列車發車」
- old_vn (unif): 「Khởi hành từ ga Yui với tư cách là tàu thường lúc 05:45. Đến Ohitoyo lúc 06:45.\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」
- fix: 「Khởi hành từ ga Yunoi với tư cách là tàu thường lúc 05:45. Đến Ohitoyo lúc 06:45.\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2327 — item T7 (JP: 湯医)

- JP: 「そいでね？　双ちゃん。機関車磨きも、楽しかったと。\nあぎゃんこと、湯医線の沿線でもできたらよかとよね」
- TW: 「小雙，還有件事。保養機車的活動也很有趣。如果湯醫線沿線也有這種活動就好了」
- old_vn (csv3): 「Với lại nhé? Sou-chan. Việc lau chùi đầu máy cũng vui lắm đó.\nNếu có thể làm mấy việc như vậy ở dọc tuyến Yui thì tốt biết mấy nhỉ.」
- fix: 「Với lại nhé? Sou-chan. Việc lau chùi đầu máy cũng vui lắm đó.\nNếu có thể làm mấy việc như vậy ở dọc tuyến Yunoi thì tốt biết mấy nhỉ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2585 — item T6 (JP: 日ノ本)

- JP: 「[めいこく,1]冥国式は、汎用性を持つ反面、日ノ本・[えい]詠式より\n車両理解の深さでは及ばないとも聞いている」
- TW: 「美國式的鐵路人偶雖然以通用性見長，但聽說對車輛的理解不如日本式、英國式那麼深」
- old_vn (audit): 「Kiểu Minh Quốc tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinamoto hay Anh」
- fix: 「Kiểu Minh Quốc tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinomoto hay Anh」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 3132 — item T7 (JP: 湯医)

- JP: 『湯医線沿線』だ。御一夜ではなく――8620ではなく。\n機関車保存体験という観光を、湯医線沿線へ持ち込めれば。
- TW: 她說的是“湯醫線沿線”而非御一夜——不是８６２０。她建議把機車保養體驗的觀光活動引入湯醫線沿線。
- old_vn (unif): Là 『Dọc tuyến Yui』. Không phải Ohitoyo――Không phải 8620.\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yui.
- fix: Là 『Dọc tuyến Yunoi』. Không phải Ohitoyo――Không phải 8620.\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yunoi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3495 — item T7 (JP: 湯医)

- JP: なるほど確かに――今は普通列車扱いの、\n湯医-御一夜間さえも、観光列車区間とできるかもしれん。
- TW: 確實，現在只開行普通列車的湯醫—御一夜段，說不定也可以打造成觀光列車段。
- old_vn (unif): Ra là vậy, quả thực――Ngay cả đoạn Yui - Ohitoyo hiện đang chạy tàu thường,\ncũng có thể trở thành đoạn tàu du lịch.
- fix: Ra là vậy, quả thực――Ngay cả đoạn Yunoi - Ohitoyo hiện đang chạy tàu thường,\ncũng có thể trở thành đoạn tàu du lịch.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3719 — item T7 (JP: 湯医)

- JP: （湯医）-御一夜-早戸間が御一夜鉄道。\n早戸-鹿兒島-千内-八ツ城-隈元までがみかん鉄道。
- TW: （湯醫）—御一夜—隼人段是御一夜鐵路。隼人—鹿兒島—川內—八代—隈元段是橙鐵路。
- old_vn (unif): Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- fix: Đoạn (Yunoi) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: old_vn là fix U2c đã gộp ("Đường sắt Ohito" → "Đường sắt Ohitoyo", gộp 22/11 ~11:35) — fix của batch này cộng dồn trên giá trị U2c, chỉ đổi "(Yui)" → "(Yunoi)", giữ nguyên "Đường sắt Ohitoyo" của U2c. Đây là dòng chồng lấn duy nhất với batch đã gộp (cảnh báo của coordinator 22/11 ~11:35); đã sửa lại thành giá trị gộp trước khi nộp, xem §4.

## 02_Hibiki — `日々姫08_開きかけのつぼみ.txt.toml` (2 dòng)

### key 2260 — item T7 (JP: 湯医)

- JP: 「左様です、双鉄様。今は、御一夜-湯医だけの二駅。\nこのような心遣いは不要かもしれませんが――」
- TW: 「沒錯，雙鐵少爺。現在只有御一夜到湯醫這兩站，也許還不必擔心這種事。可是——」
- old_vn (unif): 「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohitoyo và Yui.\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」
- fix: 「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohitoyo và Yunoi.\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2302 — item T7 (JP: 湯医)

- JP: 「湯医線に関しての、現時点での知識と運転経験は、\nポーレット様が双鉄様に勝る――というだけの話です」
- TW: 「目前來說，在湯醫線上，波萊特小姐的駕駛經驗和知識比雙鐵少爺更勝一籌」
- old_vn (csv3): 「Nói về tuyến Yui, kiến thức và kinh nghiệm lái tàu ở thời điểm hiện tại,\ncô Paulette vượt trội hơn ngài Soutetsu――Chỉ đơn giản là vậy thôi ạ.」
- fix: 「Nói về tuyến Yunoi, kiến thức và kinh nghiệm lái tàu ở thời điểm hiện tại,\ncô Paulette vượt trội hơn ngài Soutetsu――Chỉ đơn giản là vậy thôi ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 02_Hibiki — `日々姫09_run_with_our_dreams.txt.toml` (2 dòng)

### key 1640 — item T7 (JP: 湯医)

- JP: 「でもにぃに、どうしてナビで遠回りしてまで\n[ゆのい,1]湯医に行くと？　どうせ、一泊してからの乗車なのに」
- TW: 「不過阿哥，為什麼要乘Ｎａｖｉ繞遠路去湯醫呢？反正都要過一晚才能上車啊」
- old_vn (csv3): 「Nhưng mà anh hai, sao phải đi Navi vòng vèo thế để\nđến Yui làm gì? Đằng nào cũng phải nghỉ lại một đêm rồi mới lên tàu mà.」
- fix: 「Nhưng mà anh hai, sao phải đi Navi vòng vèo thế để\nđến Yunoi làm gì? Đằng nào cũng phải nghỉ lại một đêm rồi mới lên tàu mà.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2708 — item T7 (JP: 湯医)

- JP: 湯医か鱈木か――トレインホステルの設置場所では、\n御一夜鉄道を二分しての大激論がかわされた。
- TW: 要把列車旅館放在湯醫還是多良木，這個問題讓御一夜鐵路內部分為兩派，引發了激烈的爭論。
- old_vn (unif): Yui hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohitoyo.
- fix: Yunoi hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohitoyo.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 02_Hibiki — `日々姫10_稀咲の未来図、日々姫の未来図.txt.toml` (1 dòng)

### key 2613 — item T7 (JP: 湯医)

- JP: 「このレイアウトに継ぎ足しをして巨大な御一夜市――\nいや、いっそ湯医線沿線の広域モデルを作る」
- TW: 「把這個場景模型繼續改造成巨大的御一夜市——不，索性就做成連湯醫線沿線都包括進去的廣域模型」
- old_vn (unif): 「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohitoyo khổng lồ——\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yui đi.」
- fix: 「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohitoyo khổng lồ——\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yunoi đi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: fix chứa ký tự \n thật trong chuỗi (như JSON) — trong khối TOML viết \\n theo quy ước dự án.

## 02_Hibiki — `日々姫11_御一夜モザイク.txt.toml` (2 dòng)

### key 2095 — item T7 (JP: 湯医)

- JP: 「はい、御一夜の町に重点を置き、そこから湯医線沿線の\n光景を、簡略化してジオラマでつくり上げる計画です」
- TW: 「是的。我們計劃以御一夜城區為重點，把御一夜城區和湯醫線的沿線風景簡化成微縮景觀模型」
- old_vn (unif): 「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohitoyo, từ đó\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yui ạ.」
- fix: 「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohitoyo, từ đó\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yunoi ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: fix chứa ký tự \n thật trong chuỗi (như JSON) — trong khối TOML viết \\n theo quy ước dự án.

### key 2498 — item T6 (JP: 日ノ本)

- JP: その他に書かれているのは単なる数字――\n日ノ本円で八桁にのぼる金額だけだ。
- TW: 剩下的都是數字——高達八位數日元的金額。
- old_vn (csv3): Những thứ khác được viết chỉ là những con số đơn thuần——\\nMột số tiền lên đến tám chữ số bằng đồng Yên Hinamoto.
- fix: Những thứ khác được viết chỉ là những con số đơn thuần——\\nMột số tiền lên đến tám chữ số bằng đồng Yên Hinomoto.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 02_Hibiki — `日々姫12_風.txt.toml` (2 dòng)

### key 2279 — item T7 (JP: 湯医)

- JP: 「[ゆのい,1]湯医線は、緑の中と川の上とを走ってますから、\n木のイメージ、すっごーく合うです！　素敵ですぅ」
- TW: 「湯醫線主要是在綠色樹林中和河川上行駛的，木質的風格和它好搭配呀！太棒了」
- old_vn (csv3): 「Tuyến Yui chạy giữa không gian xanh mướt và trên mặt sông,\\nnên hình ảnh gỗ cực kỳ hợp luôn! Tuyệt vời quá nha.」
- fix: 「Tuyến Yunoi chạy giữa không gian xanh mướt và trên mặt sông,\\nnên hình ảnh gỗ cực kỳ hợp luôn! Tuyệt vời quá nha.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2701 — item T11 (JP: 運転体)

- JP: 筆に絵の具を軽く乗せ、日々姫は幼女にそれを持たせて、\n\x%l運転体;#00ffc040;運転体%l;#;のハチロクほどに小さなその手をすっぽりつつむ。
- TW: 她輕輕在筆上打上顏料，然後讓小女孩拿著，又溫柔地扶住那隻就像\x%l運転体;#00ffc040;駕駛體%l;#;八六般大小的手。
- old_vn (csv3): Lấy một chút màu nước lên cọ, Hibiki cho cô bé cầm lấy,\\nrồi bao bọc trọn vẹn bàn tay nhỏ xíu cỡ như \\x%l運転体;#00ffc040;thân chính%l;#; của Hachiroku.
- fix: Lấy một chút màu nước lên cọ, Hibiki cho cô bé cầm lấy,\\nrồi bao bọc trọn vẹn bàn tay nhỏ xíu cỡ như \\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

## 02_Hibiki — `日々姫13_討論会.txt.toml` (2 dòng)

### key 60 — item T7 (JP: 湯医)

- JP: 終点、湯医駅間近。\nよどむところなく日々姫の言葉も終わりに向かう。
- TW: \x%l列車;#00ffc040;列車%l;#;即將到達終點湯醫站，而日日姬流暢的演講也臨近尾聲。
- old_vn (csv3): Điểm cuối, ga Yui đang đến gần.\nLời nói của Hibiki cũng trôi chảy đi đến hồi kết.
- fix: Điểm cuối, ga Yunoi đang đến gần.\nLời nói của Hibiki cũng trôi chảy đi đến hồi kết.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1964 — item T7 (JP: 湯医)

- JP: レイアウト内では、環状線となった湯医線上を、\n\x%l8620;#00ffc040;8620%l;#;と\x%lキハ07;#00ffc040;キハ07%l;#;sとが、それぞれに新\x%l客車;#00ffc040;客車%l;#;を引いている。
- TW: 在場景模型中，\x%l8620;#00ffc040;８６２０%l;#;和\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;Ｓ各自拉著全新的\x%l客車;#00ffc040;客運車廂%l;#;，跑在環形的湯醫線上。
- old_vn (csv3): Bên trong sa bàn, trên tuyến Yui đã trở thành tuyến vòng,\n\x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#;S đang lần lượt kéo theo \x%l客車;#00ffc040;toa hành khách%l;#; mới.
- fix: Bên trong sa bàn, trên tuyến Yunoi đã trở thành tuyến vòng,\n\x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#;S đang lần lượt kéo theo \x%l客車;#00ffc040;toa hành khách%l;#; mới.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 02_Hibiki — `日々姫14_投開票.txt.toml` (1 dòng)

### key 1680 — item T41 (JP: キハ)

- JP: 「\x%lキハ07;#00ffc040;キハ07%l;#;sの“キハ”と同じく、\x%l客車;#00ffc040;客車%l;#;にも称号――\n車輌の特徴を表す略称があるんですよ」
- TW: 「和\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;Ｓ的“Ｋｉｈａ”一樣，\x%l客車;#00ffc040;客運車廂%l;#;也有\x%l形式称号;#00ffc040;代號%l;#;。也就是表現車輛特徵的簡稱」
- old_vn (csv3): 「Giống như chữ "Kiha" trong \x%lキハ07;#00ffc040;KiHa 07%l;#;S, \x%l客車;#00ffc040;toa hành khách%l;#; cũng có danh xưng――\nchính là tên viết tắt thể hiện đặc điểm của phương tiện đó.」
- fix: 「Giống như chữ "KiHa" trong \x%lキハ07;#00ffc040;KiHa 07%l;#;S, \x%l客車;#00ffc040;toa hành khách%l;#; cũng có danh xưng――\nchính là tên viết tắt thể hiện đặc điểm của phương tiện đó.」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.
- Lưu ý: chỉ đổi chữ "Kiha" trong ngoặc kép ở display; gloss \x%lキハ07%l;#; đã là "KiHa 07" đúng sẵn — không đụng.

## 03_Paulette — `グランドリライト04_ポーレット.txt.toml` (12 dòng)

### key 1845 — item T7 (JP: 湯医)

- JP: 「地域をつなげる、そうした列車にせねばならない。\n湯医線の往復だけしか出来ぬ、今の段階からでもやはり」
- TW: 「哪怕現階段只能做到往返湯醫線，還是要想方設法讓列車把整個地區串聯起來」
- old_vn (csv3): 「Phải biến nó thành một chuyến tàu kết nối khu vực.\nNgay cả ở giai đoạn hiện tại, khi chỉ mới chạy khứ hồi trên tuyến Yui.」
- fix: 「Phải biến nó thành một chuyến tàu kết nối khu vực.\nNgay cả ở giai đoạn hiện tại, khi chỉ mới chạy khứ hồi trên tuyến Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1919 — item T7 (JP: 湯医)

- JP: 「ふむ。であれば――温泉と\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;の町――\n御一夜のイメージで、湯医線全線を統一すれば」
- TW: 「嗯，那麼……用御一夜的“溫泉與\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;之城”的形象，來統一整條湯醫線就行了」
- old_vn (audit): 「Ừm. Nếu vậy——thành phố của suối nước nóng và \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;——chỉ cần dùng hình ảnh của Ohitoyo để thống nhất toàn tuyến Yui thì...」
- fix: 「Ừm. Nếu vậy——thành phố của suối nước nóng và \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;——chỉ cần dùng hình ảnh của Ohitoyo để thống nhất toàn tuyến Yunoi thì...」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1962 — item T7 (JP: 湯医)

- JP: 「八ツ城－御一夜間より先に、まず湯医線だな。\n……夢を見すぎて、自分の足元をおろそかにするとは」
- TW: 「在解決八代到御一夜的問題之前，先要解決湯醫線的問題啊。……沒想到我太著迷於夢想，居然疏忽了腳下」
- old_vn (audit): 「Trước đoạn Yatsushiro - Ohitoyo, thì phải lo cho tuyến Yui đã. ……Mải mê mơ mộng mà lại bỏ bê nền tảng của chính mình.」
- fix: 「Trước đoạn Yatsushiro - Ohitoyo, thì phải lo cho tuyến Yunoi đã. ……Mải mê mơ mộng mà lại bỏ bê nền tảng của chính mình.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2006 — item T7 (JP: 湯医)

- JP: 「レイル・ロマネスク――\n湯医線沿線を、そのイメージで育てていこう」
- TW: 「幻想鐵路——將湯醫線沿線打造成這個形象吧」
- old_vn (csv3): 「Đường sắt kỳ ảo——\nHãy phát triển dọc tuyến Yui theo hình ảnh đó.」
- fix: 「Đường sắt kỳ ảo——\nHãy phát triển dọc tuyến Yunoi theo hình ảnh đó.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2067 — item T7 (JP: 湯医)

- JP: 「わたし的に、次に一番必要になってくるのは、\n『湯医方面の観光資源』じゃないかって思います」
- TW: 「我認為，第二重要的應該是“湯醫方面的旅遊資源”」
- old_vn (csv3): 「Theo em, điều cần thiết nhất tiếp theo\nchính là 『tài nguyên du lịch khu vực Yui』.」
- fix: 「Theo em, điều cần thiết nhất tiếp theo\nchính là 『tài nguyên du lịch khu vực Yunoi』.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2127 — item T7 (JP: 湯医)

- JP: 「だな。8620での湯医線観光列車の成功は、必ずや、\n復線買収の推進にもつながる、大きな刺激となろうから」
- TW: 「是啊。８６２０的湯醫線觀光列車的成功一定會極大地刺激到廢線土地收購的進程」
- old_vn (csv3): 「Đúng vậy. Sự thành công của đoàn tàu du lịch 8620 trên tuyến Yui chắc chắn sẽ\ntrở thành động lực lớn, thúc đẩy việc mua lại đất để khôi phục tuyến đường sắt.」
- fix: 「Đúng vậy. Sự thành công của đoàn tàu du lịch 8620 trên tuyến Yunoi chắc chắn sẽ\ntrở thành động lực lớn, thúc đẩy việc mua lại đất để khôi phục tuyến đường sắt.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2145 — item T7 (JP: 湯医)

- JP: 「です。湯医線全線もそのイメージにして、双鉄くんの、\n『路線の観光カタログ化』の成功例にしていきます」
- TW: 「是的。讓這個形象覆蓋湯醫線全線，作為你的“鐵路觀光商品目錄化”的成功案例」
- old_vn (csv3): 「Vâng. Áp dụng hình ảnh đó cho toàn tuyến Yui,\nđể làm ví dụ thành công cho 『danh mục hóa du lịch tuyến đường sắt』 của anh.」
- fix: 「Vâng. Áp dụng hình ảnh đó cho toàn tuyến Yunoi,\nđể làm ví dụ thành công cho 『danh mục hóa du lịch tuyến đường sắt』 của anh.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2156 — item T7 (JP: 湯医)

- JP: 「時を止めた幻想の路線――あの日にもう一度帰れる路線。\nそのように、湯医線を育てていくことができるなら――」
- TW: 「時間靜止、充滿幻想的線路——能夠夢回往昔的線路。如果能將湯醫線打造成這種線路的話——」
- old_vn (csv3): 「Một tuyến đường kỳ ảo nơi thời gian ngừng trôi——nơi ta có thể trở về ngày hôm ấy một lần nữa.\nNếu có thể phát triển tuyến Yui theo hướng như vậy——」
- fix: 「Một tuyến đường kỳ ảo nơi thời gian ngừng trôi——nơi ta có thể trở về ngày hôm ấy một lần nữa.\nNếu có thể phát triển tuyến Yunoi theo hướng như vậy——」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2172 — item T7 (JP: 湯医)

- JP: 「です。そうなったら、湯医線は環状の外――\n『わざわざ乗り換えて行く場所』になっちゃうんです」
- TW: 「沒錯。這樣一來，湯醫線就會被排除在環形線路之外——變成“需要特地換乘才能去的地方”了」
- old_vn (csv3): 「Đúng vậy. Khi đó, tuyến Yui sẽ nằm ngoài vòng tròn——\ntrở thành 『nơi phải cất công chuyển tàu mới đến được』.」
- fix: 「Đúng vậy. Khi đó, tuyến Yunoi sẽ nằm ngoài vòng tròn——\ntrở thành 『nơi phải cất công chuyển tàu mới đến được』.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2205 — item T7 (JP: 湯医)

- JP: 「確かにだ。ゆえ、湯医線沿線の湯医側に――\n『乗り換えてもわざわざ行く価値』が必要なのか」
- TW: 「確實。因此需要讓湯醫線沿線的湯醫擁有“特地換乘去觀光的價值”是嗎？」
- old_vn (csv3): 「Đúng là vậy. Do đó, ở khu vực Yui dọc theo tuyến Yui——\ncần phải có 『giá trị đáng để cất công chuyển tàu』 sao.」
- fix: 「Đúng là vậy. Do đó, ở khu vực Yunoi dọc theo tuyến Yunoi——\ncần phải có 『giá trị đáng để cất công chuyển tàu』 sao.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2264 — item T7 (JP: 湯医)

- JP: 「それじゃダメです、双鉄くん。\nそれだと、湯医線は栄えない」
- TW: 「這可不行，雙鐵君。這樣是不可能讓湯醫線繁榮起來的」
- old_vn (csv3): 「Như thế không được đâu anh Soutetsu.\nLàm vậy thì tuyến Yui không thể phát triển được.」
- fix: 「Như thế không được đâu anh Soutetsu.\nLàm vậy thì tuyến Yunoi không thể phát triển được.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2268 — item T7 (JP: 湯医)

- JP: 「それなら、御一夜の町並みだとか、\n湯医の古い駅舎も生きます！！」
- TW: 「這樣一來，御一夜的街道，還有湯醫的舊車站也能活過來了！！」
- old_vn (audit): 「Nếu vậy, cảnh quan của Ohitoyo, hay nhà ga cũ của Yui cũng sẽ được hồi sinh!!」
- fix: 「Nếu vậy, cảnh quan của Ohitoyo, hay nhà ga cũ của Yunoi cũng sẽ được hồi sinh!!」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 03_Paulette — `ポーレット02_古地図.txt.toml` (1 dòng)

### key 2104 — item T7 (JP: 湯医)

- JP: 「\x%l大詔;#00ffc040;大詔%l;#;の頃のものでしょうかね？\n[ていてつゆのいせん,4]帝鉄湯医線って、ほら、ここ」
- TW: 「這是大正時期的地圖吧？你看這裡，還寫著帝鐵湯醫線呢」
- old_vn (audit): 「Có lẽ là từ thời \x%l大詔;#00ffc040;Taisho%l;#; nhỉ?
Tuyến Teitetsu Yui này, anh xem, ở đây.」
- fix: 「Có lẽ là từ thời \x%l大詔;#00ffc040;Taisho%l;#; nhỉ?
Tuyến Teitetsu Yunoi này, anh xem, ở đây.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).
- Lưu ý: VN gốc chứa newline thật (không phải ký tự \n) — fix giữ nguyên newline thật đó; trong khối TOML (§5) viết thành \n để parse được, giá trị parse ra khớp JSON.

## 03_Paulette — `ポーレット02_解放b寝台.txt.toml` (1 dòng)

### key 1966 — item T16 (JP: 駿袋鉄道)

- JP: 「いえ。マイントレジャーのためには、\n今の、[すんたい,1]駿袋鉄道さんに譲ってもらったこの方が適任です」
- TW: 「沒關係。若是為煤探樂園考慮的話，如今駿遠鐵路轉讓給我們的那台更合適」
- old_vn (csv3): 「Không đâu ạ. Vì lợi ích của Mine Treasure,\ncô bé được nhượng lại từ Đường sắt Suntetsu hiện tại mới là người phù hợp nhất.」
- fix: 「Không đâu ạ. Vì lợi ích của Mine Treasure,\ncô bé được nhượng lại từ Đường sắt Suntai hiện tại mới là người phù hợp nhất.」
- Lý do: JP chứa [すんたい,1]駿袋鉄道, ruby すんたい (TW 駿遠 sai theo JP); VN cũ dùng "Suntetsu" → đổi thành "Suntai" theo T16 (DECIDED 19/11, Hieu).

## 03_Paulette — `ポーレット03_廃炭鉱.txt.toml` (8 dòng)

### key 75 — item T41 (JP: キハ)

- JP: \x%lタイフォン;#00ffc040;タイフォン%l;#;を軽快に響かせて、\n僕らをおろした\x%lキハ07;#00ffc040;キハ07%l;#;が走り去っていく。
- TW: \x%lタイフォン;#00ffc040;風笛%l;#;發出了輕快的響聲，我們下車後，\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;逐漸離我們遠去。
- old_vn (audit): \x%lタイフォン;#00ffc040;còi Typhon%l;#; vang lên nhẹ nhàng, \x%lキハ07;#00ffc040;Kiha 07%l;#; thả chúng tôi xuống rồi chạy vụt đi.
- fix: \x%lタイフォン;#00ffc040;còi Typhon%l;#; vang lên nhẹ nhàng, \x%lキハ07;#00ffc040;KiHa 07%l;#; thả chúng tôi xuống rồi chạy vụt đi.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 1723 — item T7 (JP: 湯医)

- JP: 「よほどの悪天候でも無い限り、湯医線沿線で\n電波が通じないのは、術仙炭鉱廃駅付近だけです」
- TW: 「只要不是氣象條件特別惡劣，整條湯醫線沒有信號的地方就只有術仙煤礦廢車站附近了」
- old_vn (audit): 「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yui, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsu-sen thôi.」
- fix: 「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yunoi, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsu-sen thôi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1728 — item T41 (JP: キハ)

- JP: 「わたくしたちが乗っている以上、\x%l8620;#00ffc040;8620%l;#;は走行しない。\nこの全線が、\x%lキハ07;#00ffc040;キハ07%l;#;の\x%l閉塞;#00ffc040;[へいそく,1]閉塞%l;#;・専有区間となるのですから」
- TW: 「只要我們都在這裡，\x%l8620;#00ffc040;８６２０%l;#;就不會開動。整個路段就是只屬於\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的\x%l閉塞;#00ffc040;閉塞%l;#;專有路段」
- old_vn (audit): 「Chừng nào chúng tôi còn ở trên này, \x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\nToàn bộ tuyến này sẽ trở thành khu vực \x%l閉塞;#00ffc040;phong tỏa%l;#; độc quyền của \x%lキハ07;#00ffc040;Kiha 07%l;#;.」
- fix: 「Chừng nào chúng tôi còn ở trên này, \x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\nToàn bộ tuyến này sẽ trở thành khu vực \x%l閉塞;#00ffc040;phong tỏa%l;#; độc quyền của \x%lキハ07;#00ffc040;KiHa 07%l;#;.」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 1909 — item T7 (JP: 湯医)

- JP: 「古地図だと、湯医線と連絡……直接、乗り入れしてた\n可能性、結構高そうに見えたんですけど」
- TW: 「按照古地圖來看，這裡過去和湯醫線相互連接著的可能性應該挺高的」
- old_vn (audit): 「Theo bản đồ cũ, tuyến Yui với bên này từng liên thông……\nkhả năng từng chạy thẳng qua nhau khá cao đấy ạ.」
- fix: 「Theo bản đồ cũ, tuyến Yunoi với bên này từng liên thông……\nkhả năng từng chạy thẳng qua nhau khá cao đấy ạ.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2087 — item T7 (JP: 湯医)

- JP: 「そうあれば、定時の湯医、御一夜への停車も、\n僕らを拾う夕方の臨時停車も、安全度はより高まろう」
- TW: 「這樣一來無論是定點在湯醫和御一夜站停車時，還是在傍晚載我們回去臨時停車時都能提高不少安全度」
- old_vn (audit): 「Nếu được như vậy, dù là chuyến dừng đúng giờ ở Yui và Ohitoyo, hay chuyến dừng tạm buổi chiều để đón bọn anh, độ an toàn cũng sẽ cao hơn.」
- fix: 「Nếu được như vậy, dù là chuyến dừng đúng giờ ở Yunoi và Ohitoyo, hay chuyến dừng tạm buổi chiều để đón bọn anh, độ an toàn cũng sẽ cao hơn.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2367 — item T7 (JP: 湯医)

- JP: 湯医線の線路を見、\nそれから周囲の地べたを見ていた青い瞳が持ち上がる。
- TW: 一直在低頭觀察湯醫線鐵路和周圍地面的波萊特抬起頭來。
- old_vn (audit): Đôi mắt xanh nãy giờ vẫn đang quan sát đường ray tuyến Yui rồi mặt đất xung quanh, ngẩng lên.
- fix: Đôi mắt xanh nãy giờ vẫn đang quan sát đường ray tuyến Yunoi rồi mặt đất xung quanh, ngẩng lên.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2743 — item T7 (JP: 湯医)

- JP: 言いながら、ポーレットは湯医線の本線を指す。
- TW: 波萊特指著湯醫線幹線說道。
- old_vn (audit): Vừa nói, Paulette vừa chỉ vào tuyến chính của tuyến Yui.
- fix: Vừa nói, Paulette vừa chỉ vào tuyến chính của tuyến Yunoi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2814 — item T41 (JP: キハ)

- JP: 慣れぬ\x%lキハ07;#00ffc040;キハ07%l;#;の\x%l運転台;#00ffc040;運転台%l;#;で、\n\x%l機関助士;#00ffc040;機関助士%l;#;でも\x%l機関士;#00ffc040;機関士%l;#;でもない、\x%l運転士;#00ffc040;運転士%l;#;役。
- TW: 站在還不熟悉的\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的\x%l運転台;#00ffc040;駕駛台%l;#;上，此刻的日日姬既不是\x%l機関助士;#00ffc040;司爐%l;#;也不是\x%l機関士;#00ffc040;司機%l;#;，而是\x%l運転士;#00ffc040;駕駛員%l;#;。
- old_vn (audit): Trong \x%l運転台;#00ffc040;buồng lái%l;#; của \x%lキハ07;#00ffc040;Kiha 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \x%l機関士;#00ffc040;Người lái tàu%l;#;, mà đang đóng vai trò \x%l運転士;#00ffc040;người lái%l;#;.
- fix: Trong \x%l運転台;#00ffc040;buồng lái%l;#; của \x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \x%l機関士;#00ffc040;Người lái tàu%l;#;, mà đang đóng vai trò \x%l運転士;#00ffc040;người lái%l;#;.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 03_Paulette — `ポーレット04_ヒヤリング.txt.toml` (2 dòng)

### key 2023 — item T7 (JP: 湯医)

- JP: 湯医線の復活のその日を写真に収めたく、\nしかし仕事の都合がつかず、娘に代わりを頼むレベルの。
- TW: 他想用照片記錄下湯醫線復活的這一天。哪怕因為工作來不了，也要拜託自己的女兒替他來。
- old_vn (csv3): Đam mê đến mức muốn lưu lại hình ảnh ngày tuyến Yui được khôi phục,\nnhưng vì bận công việc nên đành phải nhờ con gái đi thay.
- fix: Đam mê đến mức muốn lưu lại hình ảnh ngày tuyến Yunoi được khôi phục,\nnhưng vì bận công việc nên đành phải nhờ con gái đi thay.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2532 — item T7 (JP: 湯医)

- JP: 市長候補の一人が、湯医線を市営鉄道として復活させると\n……そんな公約、誰も相手にしないと信じきっていた。
- TW: 雖然有一位市長候選人承諾要將湯醫線改為市營鐵路，使其恢復運作……但我本以為不會有人理會。
- old_vn (csv3): Một trong những ứng cử viên thị trưởng, muốn khôi phục tuyến Yui thành đường sắt của thành phố\n……Tôi đã tin chắc rằng sẽ chẳng có ai quan tâm đến một lời hứa hẹn tranh cử như vậy.
- fix: Một trong những ứng cử viên thị trưởng, muốn khôi phục tuyến Yunoi thành đường sắt của thành phố\n……Tôi đã tin chắc rằng sẽ chẳng có ai quan tâm đến một lời hứa hẹn tranh cử như vậy.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 03_Paulette — `ポーレット07_支線.txt.toml` (1 dòng)

### key 2512 — item T11 (JP: 運転ボディ)

- JP: 確かに、いつも抱っこするハチロクは\n運転ボディ――人形サイズの方の体だ。
- TW: 現在仔細想想，的確我平時只抱過八六的駕駛體——只有人偶大小的身體。
- old_vn (csv3): Quả thực, Hachiroku mà tôi vẫn luôn bế\nlà cơ thể lái tàu——cơ thể có kích thước bằng con búp bê.
- fix: Quả thực, Hachiroku mà tôi vẫn luôn bế\nlà thân vận hành——cơ thể có kích thước bằng con búp bê.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

## 03_Paulette — `ポーレット08_未来へのレール.txt.toml` (9 dòng)

### key 1888 — item T7 (JP: 湯医)

- JP: 「以上をもって、結びと代えさせていただきます。\n今後の、湯医学園のますますのご発展と――」
- TW: 「以上就是我的發言。希望今後湯醫學園能百尺竿頭，更進一步」
- old_vn (csv3): 「Xin được kết thúc bài phát biểu tại đây.\nChúc cho sự phát triển ngày càng lớn mạnh của Học viện Yui trong tương lai——」
- fix: 「Xin được kết thúc bài phát biểu tại đây.\nChúc cho sự phát triển ngày càng lớn mạnh của Học viện Yunoi trong tương lai——」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1910 — item T7 (JP: 湯医)

- JP: 「あのおじさん。――湯医学園の学園長に、この花束を、\nひかりからプレゼントしてあげて欲しいのだ」
- TW: 「光。把這捧花送給那位叔叔——湯醫學園的校長吧」
- old_vn (csv3): 「Chú kia.——Ba muốn Hikari thay mặt ba,\ntặng bó hoa này cho thầy hiệu trưởng của Học viện Yui」
- fix: 「Chú kia.——Ba muốn Hikari thay mặt ba,\ntặng bó hoa này cho thầy hiệu trưởng của Học viện Yunoi」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2301 — item T7 (JP: 湯医)

- JP: 「ポーレット――は湯医学園卒園生ではないし、\nれいなはレイルロオドだし――」
- TW: 「波萊特不是湯醫學園的畢業生，玲奈又是鐵路人偶」
- old_vn (csv3): 「Paulette——thì không phải cựu học sinh Học viện Yui,\nReina lại là Railord——」
- fix: 「Paulette——thì không phải cựu học sinh Học viện Yunoi,\nReina lại là Railord——」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2306 — item T7 (JP: 湯医)

- JP: 「[ゆのい,1]湯医学園の――創立80周年の記念列車か」
- TW: 「湯醫學園建校８０周年的紀念列車啊」
- old_vn (csv3): 「Học viện Yui——Chuyến tàu kỷ niệm 80 năm thành lập à」
- fix: 「Học viện Yunoi——Chuyến tàu kỷ niệm 80 năm thành lập à」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2363 — item T7 (JP: 湯医)

- JP: 「湯医学園は、一年生になったらひかりが通う学園だ。\n湯医学園があったから、御一夜鉄道は存続できた」
- TW: 「等光升上一年級，就要到湯醫學園上學了。有湯醫學園維持，御一夜鐵路才能存續下去」
- old_vn (audit): 「Học viện Yui là ngôi trường mà Hikari sẽ theo học khi lên lớp một. Nhờ có Học viện Yui mà Đường sắt Ohitoyo mới có thể tồn tại được」
- fix: 「Học viện Yunoi là ngôi trường mà Hikari sẽ theo học khi lên lớp một. Nhờ có Học viện Yunoi mà Đường sắt Ohitoyo mới có thể tồn tại được」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2447 — item T7 (JP: 湯医)

- JP: 「では、いくか。\n湯医へ、そして、その先へ」
- TW: 「那我們走吧。去湯醫，去未來」
- old_vn (csv3): 「Vậy, đi thôi nào.\nĐến Yui, và xa hơn thế nữa.」
- fix: 「Vậy, đi thôi nào.\nĐến Yunoi, và xa hơn thế nữa.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2672 — item T7 (JP: 湯医)

- JP: 御一夜鉄道の存続を支え続けてくれたのは、\n間違いなく湯医学園の通学生だ。
- TW: 不用說，支持御一夜鐵路存續的乘客，便是湯醫學園的學生。
- old_vn (audit): Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohitoyo, chắc chắn là các học sinh đi lại của Học viện Yui.
- fix: Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohitoyo, chắc chắn là các học sinh đi lại của Học viện Yunoi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3042 — item T7 (JP: 湯医)

- JP: 学園長はじめ、湯医側の方々をお送りするため、\nもう一往復、このまま乗務を続けることになっている。
- TW: 為了接送湯醫方面的校長等人，我們還需要再往返運行一次列車。
- old_vn (csv3): Để đưa tiễn hiệu trưởng và những người bên Yui,\nchúng tôi sẽ tiếp tục thực hiện nhiệm vụ chạy thêm một vòng nữa.
- fix: Để đưa tiễn hiệu trưởng và những người bên Yunoi,\nchúng tôi sẽ tiếp tục thực hiện nhiệm vụ chạy thêm một vòng nữa.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3043 — item T7 (JP: 湯医)

- JP: 湯医との共存のため、商業・工業系に特化した学園となり、\n凪もふかみも、そちらへの進学を選択したのだ。
- TW: 為了與湯醫共存，它轉為了強調工商業學科的學園，凪和深美都選擇升入了術仙。
- old_vn (csv3): Để cùng tồn tại với Yui, trường đã trở thành một học viện chuyên về khối thương mại và công nghiệp,\ncả Nagi và Fukami đều chọn theo học ở đó.
- fix: Để cùng tồn tại với Yunoi, trường đã trở thành một học viện chuyên về khối thương mại và công nghiệp,\ncả Nagi và Fukami đều chọn theo học ở đó.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 03_Paulette — `ポーレット08_線から面へ.txt.toml` (3 dòng)

### key 1363 — item T7 (JP: 湯医)

- JP: 「暴れて線路にまで溢れだして――\n\x%lキハ07;#00ffc040;キハ07%l;#;は湯医に退避するしかなくなるのか？」
- TW: 「亡靈們發狂，都湧到鐵路上來了——所以\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;只能撤至湯醫站嗎？」
- old_vn (csv3): 「Họ nổi điên và tràn cả ra đường ray――\nNên \x%lキハ07;#00ffc040;KiHa 07%l;#; không còn cách nào khác đành phải sơ tán đến Yui sao?」
- fix: 「Họ nổi điên và tràn cả ra đường ray――\nNên \x%lキハ07;#00ffc040;KiHa 07%l;#; không còn cách nào khác đành phải sơ tán đến Yunoi sao?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1628 — item T7 (JP: 湯医)

- JP: 「掘り返した石炭は宝箱につめ、\x%lキハ07;#00ffc040;キハ07%l;#;には\nそのまま、湯医駅へ向かってもらう」
- TW: 「採到的煤礦裝入寶箱，讓\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;載著遊客前往湯醫站」
- old_vn (csv3): 「Than đá đào được sẽ nhét vào rương báu, và để \x%lキハ07;#00ffc040;KiHa 07%l;#;\ncứ thế hướng thẳng đến ga Yui.」
- fix: 「Than đá đào được sẽ nhét vào rương báu, và để \x%lキハ07;#00ffc040;KiHa 07%l;#;\ncứ thế hướng thẳng đến ga Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1742 — item T7 (JP: 湯医)

- JP: 「\x%l8620;#00ffc040;8620%l;#;を走らせて、御一夜――湯医を往復するのか？」
- TW: 「讓\x%l8620;#00ffc040;８６２０%l;#;在御一夜與湯醫之間往返嗎？」
- old_vn (audit): 「Cho \x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohitoyo――và Yui sao?」
- fix: 「Cho \x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohitoyo――và Yunoi sao?」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 03_Paulette — `ポーレット11_記憶と記録.txt.toml` (1 dòng)

### key 1304 — item T12 (JP: 整備ボディ)

- JP: 「けれど、鉄屑に成り果てた。\n自分の、整備ボディとともに」
- TW: 「但是，它最終還是與我的整備體一同變成了廢鐵」
- old_vn (csv3): 「Nhưng, nó đã trở thành đống sắt vụn.\nCùng với cơ thể bảo dưỡng của tôi.」
- fix: 「Nhưng, nó đã trở thành đống sắt vụn.\nCùng với thân bảo trì của tôi.」
- Lý do: JP chứa 整備体 / 整備ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân bảo trì" theo T12 (DECIDED 22/11 ~04:03, Hieu).

## 03_Paulette — `ポーレット14_ふたたび走り出すために.txt.toml` (3 dòng)

### key 83 — item T7 (JP: 湯医)

- JP: 極めてスムーズな段階緩め――\n滑るようにして\x%l8620;#00ffc040;8620%l;#;は、湯医駅へと到着する。
- TW: \x%l8620;#00ffc040;８６２０%l;#;緩緩減速，極其順暢地駛入湯醫站。
- old_vn (csv3): Quá trình nhả phanh từng nấc cực kỳ mượt mà——\n\x%l8620;#00ffc040;8620%l;#; như lướt đi, tiến vào ga Yui.
- fix: Quá trình nhả phanh từng nấc cực kỳ mượt mà——\n\x%l8620;#00ffc040;8620%l;#; như lướt đi, tiến vào ga Yunoi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2286 — item T11 (JP: 運転ボディ)

- JP: その後姿を見送る小さな小さな運転ボディのハチロクが、\nなんとも大きく、頼もしいものと僕には見える。
- TW: 我突然覺得，以駕駛體目送她們離開的小小八六，看起來是如此高大可靠。
- old_vn (csv3): Nhìn theo bóng lưng họ, Hachiroku với thân hình lái tàu nhỏ bé,\ntrong mắt tôi lại trông thật to lớn và đáng tin cậy.
- fix: Nhìn theo bóng lưng họ, Hachiroku với thân vận hành nhỏ bé,\ntrong mắt tôi lại trông thật to lớn và đáng tin cậy.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

### key 2530 — item T12 (JP: 整備ボディ)

- JP: 止める間もなく、ハチロクは整備ボディに換装し、\nキャブをすたすた下りていってしまう。
- TW: 還沒等我阻止，八六就換上了整備體，快步走下了駕駛室。
- old_vn (csv3): Chưa kịp ngăn lại, Hachiroku đã thay sang thân chính bảo dưỡng,\nvà thoăn thoắt bước xuống khỏi buồng lái.
- fix: Chưa kịp ngăn lại, Hachiroku đã thay sang thân bảo trì,\nvà thoăn thoắt bước xuống khỏi buồng lái.
- Lý do: JP chứa 整備体 / 整備ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân bảo trì" theo T12 (DECIDED 22/11 ~04:03, Hieu).

## 03_Paulette — `ポーレット15_求人難.txt.toml` (3 dòng)

### key 1073 — item T47 (JP: マスコン)

- JP: 「\x%lマスコン;#00ffc040;マスコン%l;#;？」
- TW: 「\x%lマスコン;#00ffc040;中控%l;#;？」
- old_vn (csv3): 「\x%lマスコン;#00ffc040;Bộ điều khiển trung tâm%l;#;?」
- fix: 「\x%lマスコン;#00ffc040;Điều khiển trung tâm%l;#;?」
- Lý do: JP chứa マスコン / マスターコントローラー / 主幹制御器; VN cũ dùng dạng cũ → đổi thành "điều khiển trung tâm" theo T47 (DECIDED, khóa B15).

### key 1664 — item T47 (JP: マスターコントローラー)

- JP: 「マスターコントローラーです。電気制御で……\n四輪自動車のオートマチックみたいな運転装置です」
- TW: 「就是中央控制器。通過電力控制……與四輪驅動車的自動變速箱相似的駕駛裝置」
- old_vn (csv3): 「Là Master Controller. Điều khiển bằng điện……\nlà một thiết bị lái giống như hộp số tự động của xe bốn bánh vậy.」
- fix: 「Là điều khiển trung tâm. Điều khiển bằng điện……\nlà một thiết bị lái giống như hộp số tự động của xe bốn bánh vậy.」
- Lý do: JP chứa マスコン / マスターコントローラー / 主幹制御器; VN cũ dùng dạng cũ → đổi thành "điều khiển trung tâm" theo T47 (DECIDED, khóa B15).
- JP là マスターコントローラー (dạng đầy đủ của マスコン); câu "Là Master Controller" → "Là điều khiển trung tâm" theo dạng đã khóa.

### key 1981 — item T47 (JP: マスコン)

- JP: 「クハ２６は、\x%lマスコン;#00ffc040;マスコン%l;#;搭載車輌だったんで。だから」
- TW: 「Ｋｕｈａ２６是搭載了\x%lマスコン;#00ffc040;中控%l;#;的車輛。所以——」
- old_vn (csv3): 「Kuha 26 là toa xe được trang bị \x%lマスコン;#00ffc040;bộ điều khiển trung tâm%l;#;. Nên là.」
- fix: 「Kuha 26 là toa xe được trang bị \x%lマスコン;#00ffc040;điều khiển trung tâm%l;#;. Nên là.」
- Lý do: JP chứa マスコン / マスターコントローラー / 主幹制御器; VN cũ dùng dạng cũ → đổi thành "điều khiển trung tâm" theo T47 (DECIDED, khóa B15).

## 03_Paulette — `ポーレット16_明日へのレール.txt.toml` (4 dòng)

### key 1971 — item T41 (JP: キハ)

- JP: 「待ってる――って、\x%lキハ07;#00ffc040;キハ07%l;#;でか！？」
- TW: 「在等我們——在\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;上等我們！？」
- old_vn (csv3): 「Đang đợi——ở chỗ \x%lキハ07;#00ffc040;Kiha 07%l;#; sao!?」
- fix: 「Đang đợi——ở chỗ \x%lキハ07;#00ffc040;KiHa 07%l;#; sao!?」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 2032 — item T7 (JP: 湯医)

- JP: 「走っても、すぐに止まります。\n御一夜-湯医の24.8キロだけで」
- TW: 「就算跑起來，也很快會停下。它只會跑御一夜到湯醫之間的這短短２４．８公里」
- old_vn (audit): 「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ. Chỉ trong phạm vi 24,8 km từ Ohitoyo đến Yui.」
- fix: 「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ. Chỉ trong phạm vi 24,8 km từ Ohitoyo đến Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2835 — item T41 (JP: キハ)

- JP: 視察のために、せっかく改修した\x%lキハ07;#00ffc040;キハ07%l;#;に、\nれいなは乗れずに我慢していた。
- TW: 好不容易完成了\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的改造，卻因為大臣視察一事，使得玲奈一直沒機會乘上去。
- old_vn (csv3): Cất công cải tạo lại \x%lキハ07;#00ffc040;Kiha 07%l;#; để phục vụ cho chuyến thị sát,\nvậy mà Reina vẫn phải cố nhịn không được lên tàu.
- fix: Cất công cải tạo lại \x%lキハ07;#00ffc040;KiHa 07%l;#; để phục vụ cho chuyến thị sát,\nvậy mà Reina vẫn phải cố nhịn không được lên tàu.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 3251 — item T41 (JP: キハ)

- JP: ブレーキ解除、ギアをつないで、\nハンドルの上に重ねた手から、\x%lキハ07;#00ffc040;キハ07%l;#;へと力を伝える。
- TW: 解除剎車，連接排檔，握住手把，向\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;傳送出力量。
- old_vn (csv3): Nhả phanh, gài số,\ntừ bàn tay đặt lên cần gạt, truyền lực đến \x%lキハ07;#00ffc040;Kiha 07%l;#;.
- fix: Nhả phanh, gài số,\ntừ bàn tay đặt lên cần gạt, truyền lực đến \x%lキハ07;#00ffc040;KiHa 07%l;#;.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 04_Reina — `れいなh4_ふたりっきりのハロウィン.txt.toml` (1 dòng)

### key 2241 — item T7 (JP: 湯医)

- JP: 「折り返しの列車も、結局は[ゆのい,1]湯医までいった同じ\n列車になってしまう」
- TW: 「折返的列車也一樣，到湯醫為止都是同一輛列車」
- old_vn (csv3): 「Tàu quay đầu, rốt cuộc cũng là chuyến tàu\nđã đi đến tận Yui.」
- fix: 「Tàu quay đầu, rốt cuộc cũng là chuyến tàu\nđã đi đến tận Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 05_Mayami — `lr真闇追加01_新婚旅行のリクエスト.txt.toml` (2 dòng)

### key 1239 — item T41 (JP: キハ)

- JP: 「れーちゃんのキハ07sもたいへんでしょお。\nぽーちゃんひとりで」
- TW: 「小玲的Ｋｉｈａ０７Ｓ也會很辛苦啊，全靠小波一個人」
- old_vn (csv3): 「Kiha 07S của bé Reina cũng vất vả mà nhỉ.\nChỉ có một mình Pau-chan」
- fix: 「KiHa 07S của bé Reina cũng vất vả mà nhỉ.\nChỉ có một mình Pau-chan」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

### key 1512 — item T41 (JP: キハ)

- JP: 「キハ07sはディーゼルエンジン気動車だから、\n大変は大変でも、蒸気機関車ほどじゃないですぅ」
- TW: 「Ｋｉｈａ０７Ｓ是柴油動車，就算辛苦也比不上蒸汽機車」
- old_vn (csv3): 「Kiha 07S là toa xe diesel tự hành mà,\nnên có vất vả thì cũng không bằng đầu máy hơi nước đâu ạ」
- fix: 「KiHa 07S là toa xe diesel tự hành mà,\nnên có vất vả thì cũng không bằng đầu máy hơi nước đâu ạ」
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 05_Mayami — `lr真闇追加02_御一夜新婚旅行.txt.toml` (2 dòng)

### key 1545 — item T7 (JP: 湯医)

- JP: 「湯医線は約25キロと短い上に平坦だからな。\n僕の場合、片道であれば550杯程度ですむ事が多い」
- TW: 「湯醫線大約25公里，里程很短，而且很平坦。在我執行任務的時候，單程通常只需要５５０鏟」
- old_vn (audit): 「Tuyến Yui dài khoảng 25km, vừa ngắn lại vừa bằng phẳng mà.\nĐối với anh, một chiều đi thường chỉ tốn khoảng 550 xẻng là cùng.」
- fix: 「Tuyến Yunoi dài khoảng 25km, vừa ngắn lại vừa bằng phẳng mà.\nĐối với anh, một chiều đi thường chỉ tốn khoảng 550 xẻng là cùng.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1884 — item T41 (JP: キハ)

- JP: 風呂とご飯とキハ07ｓへの乗車と。\nそれらを残すだけとなった、御一夜観光の締めくくり。
- TW: 洗澡，吃飯，乘坐Ｋｉｈａ０７ｓ。做完這些後，這次御一夜旅行就結束了。
- old_vn (unif): "Tắm rửa, ăn uống và lên chuyến tàu Kiha 07S.\nChuyến tham quan Ohitoyo chỉ còn lại những việc đó để khép lại."
- fix: "Tắm rửa, ăn uống và lên chuyến tàu KiHa 07S.\nChuyến tham quan Ohitoyo chỉ còn lại những việc đó để khép lại."
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 05_Mayami — `真闇01_再蒸留.txt.toml` (6 dòng)

### key 1425 — item T45 (JP: 冥国)

- JP: 「あー、なんか、聞いたこと……ある？\nんと……[めいこく,1]冥国で……やるやつと？」
- TW: 「啊，我好像……聽過？唔，讓我想想……在美國辦的？」
- old_vn (csv3): 「A, hình như chị có……nghe nói rồi? \nỪm……Cái tổ chức ở……Meikoku (Mỹ) ấy hả?」
- fix: 「A, hình như chị có……nghe nói rồi? \nỪm……Cái tổ chức ở……Minh Quốc (Mỹ) ấy hả?」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

### key 1511 — item T45 (JP: 冥国)

- JP: 「もし０点ばとっても、うちのお客さんやったら、\n『冥国の田舎もんは酒の味ば知らん』て笑うだけとよ」
- TW: 「就算得了０分，咱家的客人也只會笑著說“美國那種地方的鄉巴佬兒根本不懂酒”而已啊」
- old_vn (csv3): 「Dù có bị điểm 0 đi nữa, thì khách hàng nhà mình cũng chỉ cười và nói rằng \n『Mấy tên nhà quê ở Meikoku thì biết gì về mùi vị của rượu chứ』 thôi.」
- fix: 「Dù có bị điểm 0 đi nữa, thì khách hàng nhà mình cũng chỉ cười và nói rằng \n『Mấy tên nhà quê ở Minh Quốc thì biết gì về mùi vị của rượu chứ』 thôi.」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

### key 1562 — item T45 (JP: 冥国)

- JP: 「わかった。ならば、教えてやろう、\n[めいこく,1]冥国の田舎者どもに、クマ焼酎という酒の旨さを」
- TW: 「我知道了，那麼我們就去教一教美國的那些鄉巴佬們，隈燒酒是何等甘醇吧」
- old_vn (audit): 「Tôi hiểu rồi. Nếu vậy, hãy cho \nnhững kẻ nhà quê ở Meikoku biết, sự thơm ngon của rượu Kuma shochu là như thế nào.」
- fix: 「Tôi hiểu rồi. Nếu vậy, hãy cho \nnhững kẻ nhà quê ở Minh Quốc biết, sự thơm ngon của rượu Kuma shochu là như thế nào.」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

### key 1604 — item T45 (JP: 冥国)

- JP: 「そう。そして審査員のほとんどは[めいこく,1]冥国人。\n[ひのもと,2]日ノ本人は、いても２～３人がせいぜいだろう」
- TW: 「是的。而且評委基本都是美國人。日本人最多也就兩三位吧」
- old_vn (csv3): 「Đúng vậy. Và hầu hết giám khảo là người Meikoku. \nNgười Hinomoto, nếu có thì cũng chỉ khoảng 2-3 người là cùng.」
- fix: 「Đúng vậy. Và hầu hết giám khảo là người Minh Quốc. \nNgười Hinomoto, nếu có thì cũng chỉ khoảng 2-3 người là cùng.」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

### key 1641 — item T7 (JP: 湯医)

- JP: 「御一夜まわりだけでもこれほど栄えていたものが……\n四十六年には、湯医線だけしか残らんとは」
- TW: 「當年光是御一夜周圍都這麼興盛……但四十六年卻只剩下湯醫線」
- old_vn (unif): 「Chỉ riêng khu vực quanh Ohitoyo đã từng sầm uất đến thế này mà…… \nĐến năm 46, lại chỉ còn mỗi Tuyến Yui thôi sao.」
- fix: 「Chỉ riêng khu vực quanh Ohitoyo đã từng sầm uất đến thế này mà…… \nĐến năm 46, lại chỉ còn mỗi Tuyến Yunoi thôi sao.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2415 — item T7 (JP: 湯医)

- JP: 湯医線を存続させた\x%lエアクラ;#00ffc040;エアクラ%l;#;作動不能地帯が、\n観光地としての価値から見た場合には足枷となる。
- TW: 這裡讓湯醫線得以存續的\x%lエアクラ;#00ffc040;空凝機%l;#;無法使用的地帶，從觀光地價值的角度來看更是腳鐐。
- old_vn (csv3): Khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động đã giúp Tuyến Yui tồn tại, \nnhưng nếu nhìn từ giá trị của một địa điểm du lịch thì nó lại trở thành xiềng xích.
- fix: Khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động đã giúp Tuyến Yunoi tồn tại, \nnhưng nếu nhìn từ giá trị của một địa điểm du lịch thì nó lại trở thành xiềng xích.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 05_Mayami — `真闇h3_補習授業の廃校舎.txt.toml` (1 dòng)

### key 3917 — item T41 (JP: キハ)

- JP: 臨時停車のキハ07sを見送り、駅舎を出る。\n途端、真闇姉は大きく大きく伸びをする。
- TW: 送走臨時停靠的Ｋｉｈａ０７Ｓ，我離開車站。就看見真闇姐伸了個大大的懶腰。
- old_vn (csv3): Tiễn chiếc Kiha 07S dừng đỗ tạm thời đi, chúng tôi rời khỏi nhà ga.\nNgay lúc đó, chị Mayami vươn vai thật dài.
- fix: Tiễn chiếc KiHa 07S dừng đỗ tạm thời đi, chúng tôi rời khỏi nhà ga.\nNgay lúc đó, chị Mayami vươn vai thật dài.
- Lý do: JP chứa キハ; VN cũ dùng "Kiha" → đổi thành "KiHa" (chính tả chính thức của JR) theo T41.

## 06_Kisaki — `グランドリライト06_稀咲.txt.toml` (5 dòng)

### key 2146 — item T7 (JP: 湯医)

- JP: 「四人がかり！　それを――いちいちやるのかい？\n線路って、だって、御一夜－[ゆのい,1]湯医の間だけでも」
- TW: 「四人合力！就這麼一路敲過去？可是線路那麼長，就算只是御一夜到湯醫之間就夠遠了」
- old_vn (unif): 「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohitoyo và Yui thôi cũng đã...」
- fix: 「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohitoyo và Yunoi thôi cũng đã...」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2159 — item T20 (JP: 堰)

- JP: 「[せき]堰さん――ふかみの祖父たち、\x%l保線;#00ffc040;保線%l;#;ボランティアの\n方々や、僕ら、御一夜鉄道に関わる者が、だ」
- TW: 「堰先生——深美的祖父他們兄弟幾人，還有\x%l保線;#00ffc040;巡線%l;#;志願者們，以及我們御一夜鐵路的工作人員」
- old_vn (unif): 「Ông Seki――ông nội của Fukami, các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nvà cả chúng ta, những người liên quan đến Đường sắt Ohitoyo.」
- fix: 「Ông Seki――ông ngoại của Fukami, các tình nguyện viên \x%l保線;#00ffc040;bảo trì đường ray%l;#;,\nvà cả chúng ta, những người liên quan đến Đường sắt Ohitoyo.」
- Lý do: JP chứa 堰 / 祖父 — dòng Seki; VN cũ dùng "ông nội" → đổi thành "ông ngoại" theo T20 (DECIDED 20/11 ~19:15, Hieu; CHỈ các dòng Seki).
- Lưu ý: old_vn là giá trị unification đã gộp (U2b) — fix giữ nguyên phần "Đường sắt Ohitoyo" của batch trước, chỉ đổi "ông nội" → "ông ngoại".

### key 2202 — item T7 (JP: 湯医)

- JP: 「湯医線で使っているような、短く軽いレールでも、\nメートルあたり30キログラム、一本で300キロになる」
- TW: 「就算是湯醫線那種又短又輕的鐵軌，每米還是有３０公斤，一根就是３００公斤了」
- old_vn (csv3): 「Ngay cả loại đường ray ngắn và nhẹ như đang dùng ở tuyến Yui,\nmỗi mét cũng nặng 30kg, một thanh dài 10 mét là 300kg rồi.」
- fix: 「Ngay cả loại đường ray ngắn và nhẹ như đang dùng ở tuyến Yunoi,\nmỗi mét cũng nặng 30kg, một thanh dài 10 mét là 300kg rồi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2608 — item T7 (JP: 湯医)

- JP: 「湯医線を郷愁の象徴とし、未来への観光列車を走らせる。\n列車詳細は未定のようだが、コンセプトは評価に値する」
- TW: 「讓湯醫線成為鄉愁的象徵，讓觀光列車駛向未來。就算具體內容還沒決定，概念也值得一個很高的評價」
- old_vn (csv3): 「Biến tuyến Yui thành biểu tượng của sự hoài niệm, và cho chạy chuyến tàu du lịch hướng tới tương lai.\nDù chi tiết về chuyến tàu vẫn chưa được quyết định, nhưng ý tưởng này rất đáng được đánh giá cao.」
- fix: 「Biến tuyến Yunoi thành biểu tượng của sự hoài niệm, và cho chạy chuyến tàu du lịch hướng tới tương lai.\nDù chi tiết về chuyến tàu vẫn chưa được quyết định, nhưng ý tưởng này rất đáng được đánh giá cao.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3472 — item T11 (JP: 運転体)

- JP: 包帯で顔をぐるぐるにした運転体の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を、\n赤井宮司が運転鞄からそっと取り出す。
- TW: 赤井宮司從駕駛包裡小心翼翼地拿出一個駕駛體\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，她的臉上還纏著一圈圈的繃帶。
- old_vn (csv3): Akai-guji nhẹ nhàng lấy từ trong chiếc túi phi hành đoàn ra\nmột \x%lレイルロオド;#00ffc040;Railord%l;#; kíp lái với khuôn mặt bị quấn băng kín mít.
- fix: Akai-guji nhẹ nhàng lấy từ trong chiếc túi phi hành đoàn ra\nmột \x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít.
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

## 07_Nagi_Fukami — `凪ふかみ05_凪の開眼！？.txt.toml` (2 dòng)

### key 1979 — item T7 (JP: 湯医)

- JP: 「４～５歳くらいと、２～３歳くらいに見える姉妹さん。\nおねえちゃんの方が、[ゆのい,1]湯医の温泉病院に通ってるの」
- TW: 「兩姐妹一個四五歲，一個兩三歲吧。年長的姐姐時常要去湯醫的溫泉醫院」
- old_vn (csv3): 「Hai chị em, một bé tầm 4-5 tuổi, bé kia tầm 2-3 tuổi.\nBé lớn hơn thì đang khám ở bệnh viện suối nước nóng Yui.」
- fix: 「Hai chị em, một bé tầm 4-5 tuổi, bé kia tầm 2-3 tuổi.\nBé lớn hơn thì đang khám ở bệnh viện suối nước nóng Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2972 — item T7 (JP: 湯医)

- JP: ああ、気持ちよか！\nあとは湯医で、ぴたっと停車するだけばい！
- TW: 哎呀，太爽咧！剩下只要在湯醫把車停穩當就行！
- old_vn (csv3): A, sảng khoái quá đi!\nSau đó chỉ cần đỗ tàu thật chuẩn xác ở Yui là xong!
- fix: A, sảng khoái quá đi!\nSau đó chỉ cần đỗ tàu thật chuẩn xác ở Yunoi là xong!
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 07_Nagi_Fukami — `凪ふかみ08c_新しい家族.txt.toml` (2 dòng)

### key 2068 — item T7 (JP: 湯医)

- JP: 「ああ、湯医で」
- TW: 「嗯，湯醫站再見」
- old_vn (csv3): 「Ừ, hẹn gặp ở Yui.」
- fix: 「Ừ, hẹn gặp ở Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2541 — item T7 (JP: 湯医)

- JP: 「それじゃ、わたしは客車にいきます。\n湯医でまた！」
- TW: 「那我去客車車廂了。我們湯醫站再見！」
- old_vn (csv3): 「Vậy, em qua \x%l客車;#00ffc040;toa hành khách%l;#; đây.\nHẹn gặp lại ở Yui nhé!」
- fix: 「Vậy, em qua \x%l客車;#00ffc040;toa hành khách%l;#; đây.\nHẹn gặp lại ở Yunoi nhé!」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 09_Grand — `グランドリライト08_ふかみ.txt.toml` (13 dòng)

### key 1648 — item T6 (JP: 日ノ本)

- JP: 「そのとおりだ。稀咲の――日ノ本鉄路の躍進は、\nナインスターズ計画の、大きな希望となっている」
- TW: 「不錯。九星計劃所仰仗的，正是稀咲的……日本鐵路的飛躍式發展」
- old_vn (csv3): 「Đúng vậy. Bước tiến vọt của Kisaki――của Đường sắt Hinamoto,\nđang là niềm hy vọng to lớn của Kế hoạch Nine Stars.」
- fix: 「Đúng vậy. Bước tiến vọt của Kisaki――của Đường sắt Hinomoto,\nđang là niềm hy vọng to lớn của Kế hoạch Nine Stars.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 1948 — item T6 (JP: 日ノ本)

- JP: 「だろうね。ここぞとばかりに、絶対確実に、\n日ノ本鉄路が買い叩かれる」
- TW: 「很可能會。這種危急時刻，他肯定會大殺一筆價錢把日本鐵路納入囊中」
- old_vn (csv3): 「Chắc là vậy rồi. Nhân cơ hội này, tuyệt đối chắc chắn,\nĐường sắt Hinamoto sẽ bị ép giá thê thảm.」
- fix: 「Chắc là vậy rồi. Nhân cơ hội này, tuyệt đối chắc chắn,\nĐường sắt Hinomoto sẽ bị ép giá thê thảm.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2008 — item T6 (JP: 日ノ本)

- JP: 「インバウンドっていうのは、この場合、日ノ本から見た\n海外――外国から来てくださる観光客さんのこと」
- TW: 「所謂境外遊客呢，在這種情況下，指的是來自日本之外的遊客，也就是外國遊客」
- old_vn (csv3): 「Khách du lịch quốc tế, trong trường hợp này, là từ góc nhìn của Hinamoto\nđối với nước ngoài――chỉ những du khách đến từ các nước khác.」
- fix: 「Khách du lịch quốc tế, trong trường hợp này, là từ góc nhìn của Hinomoto\nđối với nước ngoài――chỉ những du khách đến từ các nước khác.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2017 — item T6 (JP: 日ノ本)

- JP: 「日ノ本だけが！　九洲だけが！！　\nこぎゃんと長くつながってる線路を持つとこになるばい」
- TW: 「擁有這麼長的連在一起的線路的，只有日本、只有九州！」
- old_vn (csv3): 「Chỉ có Hinamoto! Chỉ có Kyushu!!\nMới có được tuyến đường sắt kết nối dài đến như vậy đó!」
- fix: 「Chỉ có Hinomoto! Chỉ có Kyushu!!\nMới có được tuyến đường sắt kết nối dài đến như vậy đó!」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2032 — item T6 (JP: 日ノ本)

- JP: 「日ノ本鉄路が線路を負担したことにより、鉄道事業者は、\nナインスターズ計画を押し進めるだけの余裕をもてた」
- TW: 「日本鐵路承擔了線路的相關工作之後，鐵路公司就可以專注於推進九星計劃了」
- old_vn (csv3): 「Nhờ Đường sắt Hinamoto gánh vác phần đường ray, các công ty đường sắt\nmới có đủ khả năng để thúc đẩy Kế hoạch Nine Stars.」
- fix: 「Nhờ Đường sắt Hinomoto gánh vác phần đường ray, các công ty đường sắt\nmới có đủ khả năng để thúc đẩy Kế hoạch Nine Stars.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2044 — item T6 (JP: 日ノ本)

- JP: 「だな。ナインスターズプロジェクトのことどころか、\n日ノ本鉄路のことまで、既に知ってくださっていたとは」
- TW: 「是啊。不僅是九星計劃，就連日本鐵路的事情，她都已經知道了」
- old_vn (csv3): 「Đúng vậy. Không chỉ Dự án Nine Stars,\nmà cô ấy thậm chí đã biết cả chuyện của Đường sắt Hinamoto nữa.」
- fix: 「Đúng vậy. Không chỉ Dự án Nine Stars,\nmà cô ấy thậm chí đã biết cả chuyện của Đường sắt Hinomoto nữa.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2260 — item T7 (JP: 湯医)

- JP: 「レイルロマネスク湯医線の。そしてナインスターズの。\n起点駅であることを示す、いわば、駅併設の迎賓館だ」
- TW: 「那裡相當於和車站配套的迎賓館，代表著那個站就是夢幻鐵路湯醫線和九星的起點站」
- old_vn (csv3): 「Nó thể hiện đây là ga khởi điểm của Tuyến Rail Romanesque Yui. Và của Nine Stars.\nCó thể nói, đó là một nhà khách gắn liền với nhà ga.」
- fix: 「Nó thể hiện đây là ga khởi điểm của Tuyến Rail Romanesque Yunoi. Và của Nine Stars.\nCó thể nói, đó là một nhà khách gắn liền với nhà ga.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2271 — item T6 (JP: 日ノ本)

- JP: 「ならなら、日ノ本がいちばぁん最初に、\nそこをぬけられるかもしれないんですねぇ」
- TW: 「那麼，日本就有可能是第一個走出這種困境的國家」
- old_vn (csv3): 「Nếu vậy thì, Hinamoto có thể là quốc gia đầu tiên,\nthoát khỏi tình trạng đó nhỉ~」
- fix: 「Nếu vậy thì, Hinomoto có thể là quốc gia đầu tiên,\nthoát khỏi tình trạng đó nhỉ~」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2289 — item T6 (JP: 日ノ本)

- JP: 「双鉄様。わたくし、日ノ本以外の国の鉄道事情には、\nまったくくわしくないのですけれど」
- TW: 「雙鐵少爺，我完全不了解國外的鐵路」
- old_vn (csv3): 「Ngài Soutetsu. Tôi hoàn toàn không nắm rõ\ntình hình đường sắt ở các quốc gia khác ngoài Hinamoto, nhưng mà.」
- fix: 「Ngài Soutetsu. Tôi hoàn toàn không nắm rõ\ntình hình đường sắt ở các quốc gia khác ngoài Hinomoto, nhưng mà.」
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2553 — item T6 (JP: 日ノ本)

- JP: ファンドによって集まった資金で、日ノ本鉄路は、\n理想以上の素晴らしい成果をあげつづけている。
- TW: 募集到的資金正在讓日本鐵路收穫超乎理想的成果。
- old_vn (csv3): Nhờ nguồn vốn huy động được từ quỹ, Đường sắt Hinamoto\nvẫn đang tiếp tục gặt hái những thành quả tuyệt vời ngoài mong đợi.
- fix: Nhờ nguồn vốn huy động được từ quỹ, Đường sắt Hinomoto\nvẫn đang tiếp tục gặt hái những thành quả tuyệt vời ngoài mong đợi.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2634 — item T6 (JP: 日ノ本)

- JP: 扱い方を間違えれば、\nナインスターズが、日ノ本鉄路ごと吹き飛ぶ話だ。
- TW: 如果處理失當，這可能會給九星乃至日本鐵路帶來毀滅性打擊。
- old_vn (csv3): Nếu xử lý sai lầm,\nNine Stars và cả Đường sắt Hinamoto sẽ tan thành mây khói.
- fix: Nếu xử lý sai lầm,\nNine Stars và cả Đường sắt Hinomoto sẽ tan thành mây khói.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2746 — item T6 (JP: 日ノ本)

- JP: 投資対象としての日ノ本鉄路は、\n配当を出せるようになるまで、まだ何年もかかってしまう。
- TW: 日本鐵路作為投資對象，恐怕還需要等個幾年才能盈利。
- old_vn (csv3): Đường sắt Hinamoto với tư cách là một đối tượng đầu tư,\nsẽ còn mất nhiều năm nữa mới có thể trả cổ tức.
- fix: Đường sắt Hinomoto với tư cách là một đối tượng đầu tư,\nsẽ còn mất nhiều năm nữa mới có thể trả cổ tức.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

### key 2966 — item T6 (JP: 日ノ本)

- JP: 稀咲は確かに創設者だが、\n現在の立場的には、日ノ本鉄路の取締役にすぎない。
- TW: 雖說稀咲是創辦者，但現在她只不過是日本鐵路的董事。
- old_vn (csv3): Kisaki quả thực là người sáng lập,\nnhưng xét về vị trí hiện tại, cô ấy chỉ là Giám đốc của Đường sắt Hinamoto.
- fix: Kisaki quả thực là người sáng lập,\nnhưng xét về vị trí hiện tại, cô ấy chỉ là Giám đốc của Đường sắt Hinomoto.
- Lý do: JP chứa 日ノ本; VN cũ dùng dạng cũ "Hinamoto" → đổi thành "Hinomoto" theo T6 (DECIDED 20/11 ~19:15, Hieu).

## 09_Grand — `グランドリライト11_ナインスターズ！.txt.toml` (6 dòng)

### key 1619 — item T7 (JP: 湯医)

- JP: 『湯医線に残るべきは、自分たちとⅨ号』\n『キハ07sを、8620と並べて走らせてやって欲しい』と。
- TW: “我們的九號應該留在湯醫線上”，還有“希望能讓Ｋｉｈａ０７Ｓ和８６２０一同馳騁”。
- old_vn (csv3): 『Những người nên ở lại tuyến Yui là chúng tôi và đầu máy số 9』\n『Mong cậu hãy để KiHa 07S chạy song hành cùng 8620』.
- fix: 『Những người nên ở lại tuyến Yunoi là chúng tôi và đầu máy số 9』\n『Mong cậu hãy để KiHa 07S chạy song hành cùng 8620』.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 1683 — item T7 (JP: 湯医)

- JP: 「……日常の足としては、エアクラに勝てないよね。\n湯医線のような特殊事情でもないのなら」
- TW: 「……要說承載日常生活的載體，若不是有像湯醫線這樣的特殊情況，怕是很難勝過空凝機吧」
- old_vn (csv3): 「……Là phương tiện đi lại thường ngày thì không thể thắng nổi Aircra đâu.\nTrừ phi có hoàn cảnh đặc biệt như tuyến Yui.」
- fix: 「……Là phương tiện đi lại thường ngày thì không thể thắng nổi Aircra đâu.\nTrừ phi có hoàn cảnh đặc biệt như tuyến Yunoi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3212 — item T7 (JP: 湯医)

- JP: 宗方さんの代理で、マッチ箱客車に学園生さんたちを乗せ、\nⅨ号でことこと、湯医行きの列車を引っ張るときも。
- TW: 不管是在代替宗方先生駕駛九號，牽引著火柴盒客車滿載著學生去湯醫上學時。
- old_vn (csv3): Kể cả khi tôi thay mặt anh Munakata, chở các học sinh trên toa hành khách hộp diêm,\nvà kéo chuyến tàu hướng đến Yui bằng đầu máy số 9.
- fix: Kể cả khi tôi thay mặt anh Munakata, chở các học sinh trên toa hành khách hộp diêm,\nvà kéo chuyến tàu hướng đến Yunoi bằng đầu máy số 9.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3374 — item T7 (JP: 湯医)

- JP: １番線。湯医線側のホームにはⅨ号機関車が停車している。\nその傍らには、宗方\x%l機関士;#00ffc040;機関士%l;#;とオリヴィと。
- TW: 在一號線上，九號機車正停在湯醫線的站台邊。而宗方\x%l機関士;#00ffc040;司機%l;#;和奧莉薇，正站在九號旁。
- old_vn (csv3): Đường số 1. Đầu máy số 9 đang đỗ ở sân ga phía tuyến Yui.\nBên cạnh là \x%l機関士;#00ffc040;lái tàu%l;#; Munakata và Olivy.
- fix: Đường số 1. Đầu máy số 9 đang đỗ ở sân ga phía tuyến Yunoi.\nBên cạnh là \x%l機関士;#00ffc040;lái tàu%l;#; Munakata và Olivy.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 3526 — item T15 (JP: 小畑)

- JP: 僕らの走る肥颯線は、\n小畑へと、屋岳越えへと向かっていくから。
- TW: 我們正在行駛的這條肥薩線，是通往大畑、翻山前往矢岳方向的。
- old_vn (csv3): Bởi vì tuyến Hisatsu mà chúng tôi đang chạy,\nsẽ hướng đến Kobata, vượt qua núi Yadake.
- fix: Bởi vì tuyến Hisatsu mà chúng tôi đang chạy,\nsẽ hướng đến Okoba, vượt qua núi Yadake.
- Lý do: JP chứa 小畑 (TW 大畑 sai theo JP); VN cũ dùng "Obata"/"Kobata" → đổi thành "Okoba" theo T15 (DECIDED 19/11, Hieu).

### key 3916 — item T7 (JP: 湯医)

- JP: 御一夜を出てしばらくは、\n湯医線、湯医に向かうⅨ号機関車と併走だ。
- TW: 這使得我們在剛剛駛出御一夜站的一小段路上，可以和在湯醫線上駛向湯醫的九號齊頭並進。
- old_vn (unif): Sau khi rời Ohitoyo một đoạn,\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yui trên tuyến Yui.
- fix: Sau khi rời Ohitoyo một đoạn,\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yunoi trên tuyến Yunoi.
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

## 10_Chikuni — `仲国01_副丘→北琴.txt.toml` (1 dòng)

### key 2011 — item T11 (JP: 運転体)

- JP: 「ああ。どうやっても運転体を国外に持ち出す方法はない、\nとのことだったものな」
- TW: 「是啊……這也沒辦法，駕駛體是無論如何都不允許帶出國外的」
- old_vn (csv3): 「Ừ. Nghe nói dù có làm cách nào cũng không thể\nmang thân lái ra nước ngoài được mà.」
- fix: 「Ừ. Nghe nói dù có làm cách nào cũng không thể\nmang thân vận hành ra nước ngoài được mà.」
- Lý do: JP chứa 運転体 / 運転ボディ; VN cũ dùng dạng chưa khóa → đổi thành "thân vận hành" theo T11 (DECIDED 22/11 ~04:03, Hieu, CHỐT).

## 10_Chikuni — `仲国03_北琴鉄道歴史館.txt.toml` (3 dòng)

### key 2304 — item T45 (JP: 冥国)

- JP: 「そして9700は、冥国でも初めて製造された\n1D1の\x%l蒸機;#00ffc040;蒸機%l;#;だった――ゆえに、発注元への敬意を表し」
- TW: 「而９７００甚至在美國，也是第一輛１Ｄ１輪式\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;，所以為致敬其進口方」
- old_vn (csv3): 「Và 9700 cũng là \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; 1D1 đầu tiên được sản xuất tại Meikoku——\nVì vậy, để thể hiện sự tôn trọng đối với bên đặt hàng」
- fix: 「Và 9700 cũng là \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; 1D1 đầu tiên được sản xuất tại Minh Quốc——\nVì vậy, để thể hiện sự tôn trọng đối với bên đặt hàng」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

### key 2389 — item T7 (JP: 湯医)

- JP: 「湯医線も、平坦地の平坦路線やもんね。\nハチロクが軟弱路線のことば知らんの、無理もなかとよ」
- TW: 「連湯醫線都是在平原鋪設的線路吶，也難怪八六對地基不穩固的線路不清楚咯」
- old_vn (csv3): 「Tuyến Yui cũng là tuyến đường bằng phẳng trên vùng đất bằng phẳng mà.\nHachiroku không biết về những tuyến đường nền đất yếu cũng là điều dễ hiểu thôi.」
- fix: 「Tuyến Yunoi cũng là tuyến đường bằng phẳng trên vùng đất bằng phẳng mà.\nHachiroku không biết về những tuyến đường nền đất yếu cũng là điều dễ hiểu thôi.」
- Lý do: JP chứa 湯医 / 湯医線 (hoặc kana ユノイ線, cùng thuật ngữ); VN cũ dùng "Yui" → đổi thành "Yunoi" theo T7 (DECIDED 19/11, Hieu).

### key 2430 — item T45 (JP: 冥国)

- JP: 「[きゅうなな,3]9700、9700形蒸気機関車が1D1形式なのですが――\n彼女たちは、冥国に発注された、輸入\x%l蒸機;#00ffc040;蒸機%l;#;なのです」
- TW: 「９７００型蒸汽機車就是１Ｄ１輪式——她們都是從美國進口的\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;」
- old_vn (csv3): 「9700, đầu máy hơi nước dòng 9700 có hình thức 1D1——\nNhưng các cô ấy là những \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu, được đặt hàng từ Meikoku (Mỹ).」
- fix: 「9700, đầu máy hơi nước dòng 9700 có hình thức 1D1——\nNhưng các cô ấy là những \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu, được đặt hàng từ Minh Quốc (Mỹ).」
- Lý do: JP chứa [めいこく,1]冥国; VN cũ dùng "Meikoku" → đổi thành "Minh Quốc" theo T45 (DECIDED 19/11, Hieu).

## §3. Ghi chú giữ lại / cờ (đã xem xét nhưng KHÔNG đổi)

### T6 — giữ lại (7 dòng JP 日ノ本 không có "Hinamoto")
- 5 dòng "Nippon Sharyo" (日ノ本車輌製造): ハチロク05 3712, ハチロク08 2094/2505/2091/3180 — tên công ty đã dịch đúng dạng tên riêng, không phải "Hinamoto", giữ nguyên.
- 2 dòng "Yamato Nadeshiko" (日ノ本撫子): ハチロク09 1879, ハチロクh6 993 — thuộc mục T73 OPEN ("Yamato Nadeshiko" vs "Hinomoto Nadeshiko"), không đụng trong batch này.
- §0 ước "còn 28" nhưng thực tế 34: kiểm đếm lại bằng current-value map cho thấy CSV3 có 36 dòng "Hinamoto" và chỉ 2 dòng đã được audit sửa thành "Hinomoto" (グランドリライト10 1134/2621) — 34 dòng còn lại nằm trong batch này. Per-file trong list (ハチロク03 10, ハチロク10 3, 日々姫11 1, Grand 08 12, 日々姫05 1, ハチロク14 2, 凪ふかみ01 9) không khớp thực tế: 日々姫05/ハチロク14/凪ふかみ01 không còn dòng "Hinamoto" nào (đã sửa trong audit), bù lại có ハチロク10_炙り出し 4, ハチロク11 1, 日々姫06 2, 日々姫08 1 — list per-file đã lỗi thời, số tổng 36 của §0 thì đúng.

### T7 — giữ lại (2 dòng địa danh 由衣)
- ハチロク09_もくもくオリヴィ 2118 — JP [ゆい,1]由衣, TW 由比: địa danh Yui (Shizuoka), đúng ngoại lệ đã ghi trong list và brief — GIỮ "Yui".
- ハチロク04_小畑越え 1925 — JP [ゆい,1]由衣, TW 由比: cùng địa danh Yui — GIỮ "Yui". (List chỉ nêu 2118, nhưng 1925 là cùng một địa danh, cùng ruby/TW — áp cùng ngoại lệ.)
- Các dạng "Yui" khác đã đổi hết theo ngữ cảnh JP 湯医: "tuyến Yui" → "tuyến Yunoi", "ga Yui" → "ga Yunoi", "Học viện Yui" (湯医学園, 6 dòng: P08 2306/2672/2301/1888/1910/2363) → "Học viện Yunoi", "Tuyến Teitetsu Yui" (P02 2104, JP 帝鉄湯医線) → "Tuyến Teitetsu Yunoi", "Tuyến Rail Romanesque Yui" (Grand08 2260) → "Tuyến Rail Romanesque Yunoi", "bệnh viện suối nước nóng Yui" (凪ふかみ05 1979, JP 湯医の温泉病院) → "... Yunoi".
- 2 dòng trong batch này vẫn còn dạng cũ T1 (đã cờ, không đụng): 共通14 1671/1805 còn "Ohimitera" — thuộc batch leftovers (T1 còn sót), không thuộc batch này. Dòng 日々姫08 3719 từng còn "Đường sắt Ohito" đã được U2c sửa thành "Đường sắt Ohitoyo" (gộp 22/11 ~11:35); fix của batch này đã cộng dồn trên giá trị U2c (xem §4).

### T15 — không có dòng giữ lại
- Cả 6 dòng "Obata"/"Kobata" đều có JP 小畑 và đã sửa. JP-miss: 0 dòng (41 dòng JP 小畑 = 35 "Okoba" đúng sẵn + 6 dòng sửa ở đây). Lưu ý: ハチロク12 2811/2528 (JP 小畑 vs TW 大畑, VN "Okoba" theo JP) đã đúng sẵn — không đụng, đúng như list ghi.

### T16 — không có dòng giữ lại
- 1 dòng duy nhất (P02 sleeper 1966), JP [すんたい,1]駿袋鉄道, TW 駿遠 sai theo JP — đã sửa thành "Suntai".

### T41 — giữ lại / ghi chú
- 7/18 dòng sửa nằm trong gloss %l (P16 1971/2835/3251, P03 2814/1728/75, 日々姫04 2219) — gloss cũng áp chính tả "KiHa" như display, đúng tiền lệ list nêu cho P16.
- "Sekihara" (関原, P09 6 dòng) chứa chuỗi "kihara" thường — không phải "Kiha", không đụng.
- JP キハ 172 dòng: chỉ 18 dòng còn "Kiha"; còn lại đã "KiHa" đúng sẵn.

### T45 — giữ lại
- 2 dòng JP 冥国製 đã dịch "sản xuất tại Mỹ" (ハチロク06 3455, ハチロク07 2214) — không chứa dạng cũ "Meikoku", giữ nguyên (dịch nghĩa "Mỹ" đã đúng, không cần ép thành "Minh Quốc").
- 冥軍 1 dòng (日々姫03 2158) đã "Minh Quân" đúng sẵn; メリケン (nói) 9 dòng đã "Meriken" đúng sẵn theo quy tắc "nói メリケン → Meriken".
- JP 冥国 84 dòng: 6 dòng sửa ở đây, còn lại đã "Minh Quốc" (69 dòng), "Meriken" (7 dòng — JP đọc メリケン trên 冥国), hoặc dịch nghĩa "Mỹ" (9 dòng, có trùng lặp vì một số dòng chứa cả "Meikoku (Mỹ)" / "Minh Quốc (Mỹ)").

### T47 — ghi chú
- Ngoài 5 dòng sửa: các dòng マスコン khác trong dự án đã dùng "điều khiển trung tâm" trần (ハチロク06 2145/2274/1630, 日々姫10 3219/2346) — không đụng. ハチロク06 2139/2763 (主幹制御器) sửa theo D1.

### T54 — 0 dòng (đã sửa hết trong audit)
- Cả 3 dòng sleeper P02 (1819/1832/2560) đã là "vé lượt" trong audit (1819/2560 JP 回数券; 1832 JP kana かいすうけん — tìm bằng kanji sẽ sót, đã kiểm bằng key). Cả 7 dòng 定期券 còn lại (P02 2038, 凪ふかみ04 2572/2499/1526, 仲国01 2091/1790/2035) đã là "vé định kỳ" trong audit. Tổng 9 dòng JP 回数券/定期券 + 1 dòng kana: 0 dòng còn "vé tháng" trong current value (CSV3 còn 7 dòng "vé tháng", audit đã sửa hết).

### T55 — 0 dòng (đã sửa trong unification đã gộp)
- 仲国06 1412 đã là "Cơ sở Nghiên cứu Nhân giống Gấu trúc lớn Thịnh Đô" trong fix unification đã gộp (U10/s6, F8) — current value đã đúng, không sửa lại. CSV3 VN gốc là "Bảo tồn".

### T11/T12 — giữ lại
- 仲国06 2327 "kíp lái" GIỮ NGUYÊN: JP là 機関車・乗務員交代 (đổi đầu máy và đổi tổ lái) — "kíp lái" ở đây là tổ lái/crew, không phải 運転体. Dương tính giả duy nhất trong 7 ứng viên chuỗi cũ.
- 日々姫09 1942 "trải nghiệm bảo dưỡng" GIỮ NGUYÊN: JP là 整備体験 (trải nghiệm bảo dưỡng), không phải 整備体 (thân bảo trì).
- Các dòng JP 運転体/整備体 còn lại (86 dòng kiểm kê) đã dùng "thân vận hành"/"thân bảo trì" đúng sẵn (chủ yếu audit đã sửa) — không đụng. Riêng ニイロク04 2061 audit đã dùng "Thân vận hành" — tiền lệ cho D2.

### T19 — giữ lại (12 dòng "phi hành đoàn" thuộc T18)
- 12 dòng còn "phi hành đoàn" là JP 乗務鞄/運転鞄 (túi) — thuộc T18 (→ "túi công tác"), KHÔNG thuộc T19: 共通08 2088/1486/1485/2692, 共通10 3005, ハチロク13 2555/2559, Grand06 2937/3242/2935/3540/3472 (3472 đã sửa phần "kíp lái" → "thân vận hành" theo T11, phần "túi phi hành đoàn" giữ nguyên chờ T18).
- ハチロク07 2514 (JP 乗員) đã là "Nhân viên tàu" trong audit — 0 dòng cần sửa thêm. Các dòng JP 乗員 còn lại đã đúng: ハチロク10 2411 "nhân viên tàu", 日々姫01 3128 "nhân viên toa ăn", 日々姫03 3785 "nhân viên", 日々姫08 3618 "nhân viên dự bị", lr真闇追加02 1187 "nhân viên" — hai dòng "nhân viên" trần (3785/1187) là dạng rút gọn trong liệt kê (機関車、乗員、線路 / 乗員乗客), nhất quán với nhau, giữ nguyên.

### T20 — giữ lại (22/25 dòng "ông nội" không phải Seki + các mục OPEN)
- Kiểm kê toàn bộ 25 dòng current value chứa "ông nội": chỉ 3 dòng là Seki (sửa ở đây); 2 dòng đã "ông ngoại" trong audit (凪ふかみ02 2299, ハチロク07 2679). Các dòng còn lại giữ nguyên, gồm ハチロク02 1960 (list đã chốt: KHÔNG phải Seki).
- Mục con OPEN (không đụng, chờ batch sau/Hieu): ハチロク09 2027 "bác Seki" (O65 — Seki có áp cho cách xưng hô không?) · 日々姫03 2368/2607 "ông nội" (Fukami nhờ các ông lo 保線 — plausibly Seki nhưng list để OPEN) · ハチロク07 2588 "các ông của Nagi" (JP 凪のお祖父様たち = anh em nhà Seki; VN dùng dạng trung tính "các ông", không có "ông nội" để thay — cờ cho batch leftovers: có đổi thành "các ông ngoại của Nagi" không?) · 凪ふかみ01 1884 / 凪ふかみh1 2368/2607 / Grand 08 2010 / 日々姫04 2668 (các dòng ông khác, list để OPEN).
- 日々姫03 3579 "Ông cố của Fukami" GIỮ: JP là ふかみの曽祖父 (cụ ông, không phải ông ngoại).

## §4. Lượt soát 2 (second pass — đọc lại toàn bộ 193 fix với JP)

- **Tổng: 193 dòng · tái kiểm chứng: 193 · loại bỏ: 0 · sửa lại: 0.** Lượt 2 đọc lại từng fix trong §2 (bảng trên) đối chiếu JP (+TW) của dòng đó: mọi fix chỉ thay đúng chuỗi mục tiêu, không đổi thêm/không sót lần xuất hiện nào trong dòng (kể cả 4 dòng T7 ×2 "Yui" — 日々姫08 3132, グランドリライト04 2205, ポーレット08 2363, グランドリライト11 3916 — cả hai lần đều đổi).
- **Kiểm chứng máy (hỗ trợ lượt 2, không thay thế):** 193/193 fix khác old_vn và chỉ khác ở (các) chuỗi mục tiêu của mục mình (kiểm bằng chuẩn hoá placeholder theo từng mục); 0 fix còn chứa dạng cũ của mục mình; 182/193 fix có JP chứa trực tiếp thuật ngữ kanji, 9 dòng T7 có JP kana ユノイ (cùng thuật ngữ), 2 trường hợp còn lại đã giải thích (D3: ハチロク01 2828 レイナナ; D4: ハチロク06 2139 ruby-only). 193/193 old_vn khớp current-value map theo thứ tự đã sửa (unification-đã-gộp > moan > audit > CSV3 good-set); 0 dòng moan-src, 30 audit-src, 20 unif-src, 143 csv3-src.
- **Rebase chồng lấn 3719 (sau lượt 2, trước khi nộp):** đọc ROUTE-UNIFICATION.md trực tiếp lúc cuối đợt thấy cảnh báo chồng lấn của coordinator (22/11 ~11:35): 日々姫08 3719 nằm cả ở U2c (đã gộp: "Đường sắt Ohito" → "Đường sắt Ohitoyo") và batch này. Kiểm lại toàn bộ 193 dòng với map thứ tự đã sửa (8 file đã gộp, gồm U2c + U2b): chỉ 3719 có old_vn lệch (giá trị U1a cũ); đã sửa old_vn → giá trị U2c và fix → giá trị gộp "(Yunoi) … Đường sắt Ohitoyo", kiểm lại diff (chỉ đổi "(Yui)" → "(Yunoi)") và TOML parse lại 193/193. Hai dòng chồng với U2b (Grand06 2146/2159) đã khớp giá trị gộp từ đầu, không cần sửa. 5 dòng chồng với file worker ĐANG CHẠY (chưa gộp — set2: Grand06 3472, P03 1723, ハチロク13 2555, ハチロク12 2508; T56–T66: ハチロク10 1529) không đụng ở đây; coordinator xử lý thứ tự gộp khi các batch đó nộp.
- **Kiểm chứng TOML:** 56 khối TOML (một khối mỗi file), 193 khóa, parse OK bằng tomllib, giá trị parse được khớp JSON 193/193 (chạy lại sau rebase 3719, vẫn 193/193). Trong khối, `\\n` = ký tự `\n` thật trong giá trị (quy ước TOML block của dự án); `\\x` = ký tự `\x` thật; dấu `"` trong giá trị được escape thành `\"` (3 dòng có `"` trong fix). Dòng P02 2104 có newline thật trong giá trị — trong khối viết `\n`, parse ra newline thật, khớp JSON.
- **Kiểm chứng JSON:** 193 mục, `file` là basename đầy đủ có `.txt.toml`, `key` là string, `kind` = "terminology", `item` = mã mục (2 dòng hai mục ghi "T7+T15" / "T7+T41"). 20 dòng có (file,key) trùng với file unification đã gộp — đó đúng là các dòng old_vn lấy từ fix đã gộp; fix của batch này xây trên giá trị đó, không sửa trùng, đúng quy tắc rebuild theo thứ tự gộp.

## §5. Khối TOML (56 file, 193 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị)

### 00_Common/共通12_のぞみ.txt.toml

```toml
2182 = "「Hai người là anh em sinh đôi nhỉ?\\nÔng ngoại của Fukami, ông Seki và ông Nagare ấy.」"
```

### 00_Common/共通14_負債.txt.toml

```toml
1435 = "「Nghĩa là, trước đây ở Yunoi cũng từng có bàn quay đầu máy,\\nnhưng mà, nó đã bị mất rồi sao?」"
1571 = "「Hửm?\\nCái 'Xây mới \\x%l三角線;#00ffc040;đường tam giác%l;#; ga Yunoi' này là sao?」"
1671 = "「Ngược lại…… có lẽ chính vì có bàn quay đầu máy,\\nngười ta mới đưa 8620 vào chạy tuyến Ohimitera - Yunoi đấy ạ.」"
1805 = "「Khu vực rộng lớn quanh ga Yunoi đều là đất của Đường sắt Ohimitera,\\nnên so với bàn quay đầu máy thì sẽ rẻ hơn rất nhiều…… nhưng mà.」"
```

### 01_Hachiroku/ハチロク01_双鉄の目・ハチロクの目.txt.toml

```toml
1719 = "「Ra là vậy, nếu là Reina trong hình dáng \\x%l運転体;#00ffc040;thân vận hành%l;#;,\\nthì dù có đi cùng, cũng không thấy quá chật chội.」"
1778 = "「Ôi, là KiHa 07 nhỉ.」"
2078 = "「Thêm vào đó, nếu 8620 có thể đi vào vận hành thương mại,\\nthì gánh nặng của KiHa 07 và Reina, cũng sẽ được san sẻ.」"
2828 = "Bức ảnh có vẻ được chụp từ góc thấp,\\nvừa mang nét đáng yêu đặc trưng của KiHa 07, vừa toát lên sự sống động và uy lực."
```

### 01_Hachiroku/ハチロク03_冥国式レイルロオド.txt.toml

```toml
1532 = "Cô ấy hỏi \"\\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinomoto,\\nlại có thể phối hợp ăn ý đến thế sao?\"."
1580 = "「……\\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \\x%lレイルロオド;#00ffc040;Railord%l;#;\\nkiểu Hinomoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」"
2084 = "「Ra vậy. Hợp lý…… có thể nói là cực kỳ hợp lý.\\nĐứng từ góc độ đó, ngược lại cũng thấy được nhược điểm của kiểu Hinomoto.」"
2399 = "「Nên đầu máy hơi nước và \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nđã không thể trở thành hình mẫu cho kiểu Hinomoto sao.」"
2412 = "「Cái kiểu——phối hợp ăn ý như vậy, ở đâu cũng thế hả?\\n\\x%lレイルロオド;#00ffc040;Railord%l;#; của hệ thống Master——kiểu Hinomoto ấy.」"
2454 = "「Đúng vậy. Điều đó cũng phù hợp với cảm nhận chung của người Hinomoto\\n——à, không.」"
2503 = "「Nhưng mà, ưu tiên hàng đầu trong vận tải đường sắt luôn là an toàn.\\nNhìn về lâu dài, ưu điểm của kiểu Hinomoto sẽ nổi bật hơn ạ.」"
2510 = "「Em cũng nghe nói vậy. Do em chỉ chủ yếu giao lưu với\\nRailord kiểu Hinomoto nên cũng không rành lắm ạ.」"
2585 = "「Đúng vậy. Đó là đặc điểm lớn nhất của \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinomoto, kiểu Anh hay kiểu Đức rồi.」"
3115 = "Ở kiểu Hinomoto, hầu hết đều buộc phải bỏ đi.\\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng."
```

### 01_Hachiroku/ハチロク04_煙には煙を.txt.toml

```toml
2464 = "「Lúc \\x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yunoi\\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」"
2947 = "Với chiều dài ngắn ngủi của Tuyến Yunoi, việc cứu hộ bằng \\x%lキハ07;#00ffc040;KiHa 07%l;#; cũng sẽ phát huy tác dụng,\\nvà nếu là nơi \\x%lエアクラ;#00ffc040;Aircra%l;#; có thể bay tới, thì cũng có thể dùng Navi."
```

### 01_Hachiroku/ハチロク05_レイルロオドたち.txt.toml

```toml
2260 = "「Việc Hachiroku và 8620 chạy trên Tuyến Yunoi,\\nđã được Olivy tái hiện lại y nguyên bằng Đầu máy số 9 sao?」"
2270 = "「Chuyến chạy thử Đầu máy số 9 trên Tuyến Yunoi hôm nay.\\nĐược thực hiện với đội hình \\x%l機関士;#00ffc040;lái tàu%l;#; Migita Hibiki, \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; Minokasa Nagi ạ.」"
2484 = "「Ừm. Là vấn đề về tầm nhìn quan sát. Các loại biển báo, biển chỉ dẫn trên Tuyến Yunoi,\\nđều được lắp đặt dựa trên giả định buồng lái nằm bên trái――」"
2776 = "「Vâng. Vì tôi nghĩ đó là việc bắt buộc nên đã sắp xếp rồi.\\nDự kiến toàn Tuyến Yunoi sẽ được cải thiện trong vòng hơn hai tuần nữa.」"
2796 = "「Em cũng rất mong chờ chuyến chạy thử trên Tuyến Yunoi.\\n\\x%lレイルロオド;#00ffc040;Railord%l;#; Olivy.」"
2839 = "「Fukami đã đi cùng chuyến khảo sát Tuyến Yunoi\\nvì lý do gì vậy ạ?」"
2912 = "「Đợi đến khi hoạt động thương mại trên Tuyến Yunoi hoàn toàn ổn định đã. Rồi sau đó,\\nsẽ nhờ bé Olivy hỗ trợ trong quá trình chạy làm quen. Vậy nhé.」"
3010 = "「Quả thực làm vậy sẽ an toàn hơn. Dù sao thì gần đây Olivy\\ncũng đã vượt qua đèo Okoba, dù là có đầu máy phụ hỗ trợ.」"
```

### 01_Hachiroku/ハチロク05_軋み.txt.toml

```toml
1178 = "（……Ông ngoại của Fukami, ông Seki và anh em của ông ấy,\\nlà những chuyên gia về nước và đất.）"
1755 = "「Tuyến Yunoi là tuyến đường có tải trọng thấp.\\nĐộ rung lắc sẽ chỉ xuất hiện ở phía đầu máy hơi nước thôi ạ.」"
2518 = "（Bây giờ cứ gác lại đã, phải đưa tàu đến ga Yunoi an toàn.\\nTôi dồn toàn bộ tâm trí vào việc đó.）"
2726 = "（Mà, sắp đến Yunoi rồi——cũng sắp vào vùng có sóng điện thoại rồi.\\nNếu có chuyện gì, chắc phu nhân Nagayama sẽ báo cho mình biết thôi.）"
```

### 01_Hachiroku/ハチロク06_それぞれの傷跡.txt.toml

```toml
1801 = "「Vâng, khác với thời ở đường sắt khai thác mỏ, vì đây là tuyến Yunoi……\\nNên dù chọn cách nào thì chúng tôi cũng đã tính toán được là sẽ an toàn.」"
2710 = "Tuy hơi bất ngờ, nhưng nghĩ lại thì\\ntuyến Ohitoyo - Yunoi cũng chỉ dài khoảng hai mươi mấy kilomet."
```

### 01_Hachiroku/ハチロク06_のぞみ.txt.toml

```toml
2139 = "「Điều khiển trung tâm――」"
2763 = "「Hệ thống điều khiển càng mang tính máy móc, phi cảm giác thì hiệu suất càng cao.\\nVà thứ đẩy mạnh ý tưởng đó lên một bước nữa chính là――Điều khiển trung tâm.」"
```

### 01_Hachiroku/ハチロク08_教導.txt.toml

```toml
1351 = "「『Tuyến Yunoi không có hầm chui, nhưng lại có rất nhiều cầu đường sắt.\\nTrong việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, quan trọng nhất』」"
1379 = "「……Nếu chuyện này xảy ra từ hồi tuyến Yunoi mới xây thì chắc khó giải quyết lắm.\\nNhưng nếu dạo gần đây mới bị thì có thể có cách.」"
1966 = "「Câu hỏi thưởng cho Soutetsu vì đã trả lời đúng!\\n『Tổng số \\x%lポイント;#00ffc040;ghi bẻ đường ray%l;#; trên tuyến Yunoi là bao nhiêu?』」"
2302 = "「Biết rồi~! Vậy, Olivy sẽ đi sớm thôi,\\nniềm tự hào của tuyến Yunoi! Cậu cho tớ xem từ trên thuyền luôn nha~」"
2382 = "「Hướng tới việc Đầu máy số 9 sắp đi vào hoạt động thương mại trên Tuyến Yunoi,\\ndù chỉ thêm một lần thôi——cũng xin cô hãy đến đi cùng chuyến tàu.」"
2635 = "「Đẹp quá đi~!\\nĐây chắc chắn là niềm tự hào của tuyến Yunoi rồi~!」"
2794 = "「Thế cũng siêu lắm rồi! Tuyến Yunoi á,\\ncó từ thời Teitetsu cơ mà!?」"
2828 = "「Nhóm này, là nhóm có kiến thức bảo trì đường ray\\ncủa tuyến Yunoi thuộc Đường sắt Ohitoyo đúng không? Vậy nên, là nhóm B.」"
2840 = "「Bởi vì từ trước đến nay chỉ có mỗi tàu 8620 và KiHa 07S,\\nnhưng từ giờ trở đi sẽ khác, chúng ta còn phải xem xét cả những tuyến khác ngoài tuyến Yunoi nữa mà~」"
2849 = "「Soutetsu!\\n15 phút nữa là KiHa 07S đến đó!」"
2850 = "「Còn 3 cái nữa mà Soutetsu.\\nỞ khu vực \\x%l三角線;#00ffc040;đường tam giác%l;#; Yunoi ấy.」"
2868 = "「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yunoi của Đường sắt Ohitoyo là bao nhiêu?』」"
3335 = "Vì tôi chỉ làm nhiệm vụ trên tuyến Yunoi,\\nnên cứ ngỡ đó là cảnh sắc đương nhiên——"
```

### 01_Hachiroku/ハチロク10_旺宮鉄道歴史館.txt.toml

```toml
1529 = "「……Luật kinh doanh đường sắt của Hinomoto,\\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」"
1994 = "「Tất cả, là——\\nbao gồm cả của \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; Hinomoto——sao ạ?」"
2488 = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; là một sự tồn tại ưu việt. Thực tế là ở Hinomoto hiện tại,\\ncác \\x%lレイルロオド;#00ffc040;Railord%l;#; đã nghỉ hưu đang hoạt động sôi nổi ở khắp mọi nơi——Ư!」"
```

### 01_Hachiroku/ハチロク10_炙り出し.txt.toml

```toml
1793 = "「Vâng. Một kiệt tác đầu máy hàng hóa ạ. Các em ấy đã vận chuyển đủ loại hàng hóa,\\nđến khắp mọi nơi trên đất nước Hinomoto. Có lẽ ngay cả bây giờ, các em ấy vẫn đang tiếp tục công việc đó.」"
1868 = "「Ông là kỹ sư đến từ công ty Toa xe Hinomoto phải không ạ.」"
1930 = "「Chào buổi sáng!\\nCó thư phản hồi từ công ty Toa xe Hinomoto rồi ạ.」"
2801 = "Một chiếc \\x%l台枠;#00ffc040;khung gầm%l;#; méo mó, đầy vết xước,\\nchỉ đang chờ được gửi đến công ty Toa xe Hinomoto."
```

### 01_Hachiroku/ハチロク11_幽霊.txt.toml

```toml
2370 = "Họ đang cho thợ cơ khí——ông Fuchi của công ty Toa xe Hinomoto xem\\nmàn hình hiển thị gắn ở gốc của bộ phận giống như ống nghe."
```

### 01_Hachiroku/ハチロク12_再開発.txt.toml

```toml
2464 = "「À…… Ở giai đoạn đầu chạy thử,\\ntôi muốn tránh việc chạy một mạch đến Yunoi.」"
2508 = "「Nếu chỉ đến ga bỏ hoang mỏ than Jutsu-sen, thì nên chạy tiếp đến Yunoi rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」"
2853 = "Khác với hầu hết các ga bỏ hoang trên tuyến Yunoi,\\nnhà ga này được xây dựng khá kiên cố."
```

### 01_Hachiroku/ハチロク13_夜の嵐.txt.toml

```toml
2326 = "Thấy vậy, Hachiroku đổi \\x%lタブレット;#00ffc040;thẻ bảng%l;#;,\\ntrở lại \\x%l運転体;#00ffc040;thân vận hành%l;#; và cất giọng nghiêm túc."
2328 = "Thấy vậy, Hachiroku\\ntháo \\x%lタブレット;#00ffc040;thẻ bảng%l;#; ra và chuyển sang \\x%l運転体;#00ffc040;thân vận hành%l;#;."
2336 = "Hachiroku lập tức chuyển \\x%lタブレット;#00ffc040;thẻ bảng%l;#; về lại \\x%l整備体;#00ffc040;thân bảo trì%l;#;.\\nVậy thì tôi chỉ còn cách cầm xẻng lên lại thôi."
2427 = "Khi ở \\x%l運転体;#00ffc040;thân vận hành%l;#; thì tôi không nhận ra——"
2555 = "Tôi cất cẩn thận \\x%l運転体;#00ffc040;thân vận hành%l;#; vào \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên."
2742 = "Chỉ một câu đó,\\ntôi đã hiểu lý do em ấy đổi sang \\x%l運転体;#00ffc040;thân vận hành%l;#; có cảm biến tốt hơn."
```

### 01_Hachiroku/ハチロク13_実りの秋.txt.toml

```toml
2102 = "「Chuyến từ Yunoi đi Ohitoyo có tỷ lệ lấp đầy là 65%. Nhẹ hơn mọi khi một chút.\\nThời tiết nắng ráo, tình trạng đường ray tốt.」"
```

### 01_Hachiroku/ハチロク14_冬.txt.toml

```toml
3680 = "Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\\nKhông chỉ người dân Ohitoyo, mà cả người dân Yunoi và Jutsusen nữa."
```

### 01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml

```toml
1455 = "「『Đánh giá tổng thể, có thể suy đoán khả năng các vụ phun trào hay nổ hơi nước\\nđe dọa trực tiếp đến sự an toàn của tuyến Okoba là cực kỳ thấp』」"
1842 = "「So với tuyến Yunoi, chi phí bảo trì đường ray của tuyến Okoba cực kỳ cao.\\nNếu không thu hút được khách du lịch, thì đó sẽ là sự khởi đầu cho việc thâm hụt kéo dài」"
2129 = "「Tuyến Yunoi cứ giao cho em.\\nReina có thể chạy thay bao nhiêu chuyến cũng được ạ」"
```

### 01_Hachiroku/ハチロク15b_さよなら列車.txt.toml

```toml
1999 = "Dù vậy, không hề chùn bước, chiếc \\x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\\ntiến vào tuyến Okoba, hướng về Ohitoyo, thách thức con dốc Yadake."
```

### 01_Hachiroku/ハチロク16_春.txt.toml

```toml
1622 = "「Nhưng nếu là tuyến Yunoi thì vẫn còn hy vọng.\\nDân số dọc tuyến đường đang tăng đều đặn, nếu kéo dài về phía Oita――」"
1987 = "「Việc điện khí hóa, cả tuyến Yunoi lẫn tuyến Okoba đều không thể làm được đâu.\\nDù làm cách nào thì cũng không thể thu hồi vốn được.」"
2403 = "Chuyến tàu 『BBQ Olivy』 đang tiến vào ga từ phía Yunoi――\\nCô bé định đón bóng dáng nhỏ bé của đầu máy số 9 ở khoảng cách gần nhất."
2587 = "Dù đã trở thành một \\x%l機関士;#00ffc040;lái tàu%l;#; thực thụ trên tuyến Yunoi, nhưng Hibiki\\nvẫn phải chật vật khi đối mặt với tuyến Okoba."
```

### 02_Hibiki/日々姫01_リゾート食堂列車計画.txt.toml

```toml
2225 = "Khôi phục tuyến đường giữa Ohitoyo - Okoba - Hayato\\ndo Đường sắt Ohitoyo làm chủ thể."
```

### 02_Hibiki/日々姫03_客車手配.txt.toml

```toml
2834 = "「Bởi vì chúng ta chưa hề chạy thử, hơn nữa đây lại là \\x%l客車;#00ffc040;toa hành khách%l;#; cải tạo,\\nvà trình độ của nhân viên tàu cũng hoàn toàn chưa đủ ạ.」"
```

### 02_Hibiki/日々姫04_カフェキッチン.txt.toml

```toml
1918 = "「Vâng. Ảnh chụp hay tranh vẽ. Như 8620, KiHa 07S,\\nhay những toa xe chạy từ Đường sắt Mikan sang chẳng hạn.」"
2219 = "Có khi nào là——màu be và màu vàng cam. Được sơn thành hai màu của \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; sao ạ?"
```

### 02_Hibiki/日々姫06_日々姫の決断.txt.toml

```toml
2628 = "「Em không rõ ở các quốc gia khác thì thế nào, nhưng nền giáo dục ở Hinomoto\\nquả thực được nhận thức như vậy ạ.」"
2709 = "「Trường học ở Hinomoto vốn dĩ chuyên về việc tìm ra năng lực nghề nghiệp,\\nvà những bài học, huấn luyện để tìm ra điều đó đúng không?」"
```

### 02_Hibiki/日々姫08_とれいん食堂.txt.toml

```toml
2051 = "「Khởi hành từ ga Yunoi với tư cách là tàu thường lúc 05:45. Đến Ohitoyo lúc 06:45.\\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」"
2327 = "「Với lại nhé? Sou-chan. Việc lau chùi đầu máy cũng vui lắm đó.\\nNếu có thể làm mấy việc như vậy ở dọc tuyến Yunoi thì tốt biết mấy nhỉ.」"
2585 = "「Kiểu Minh Quốc tuy có tính đa dụng cao, nhưng nghe nói về độ hiểu biết toa xe thì không bằng hàng của Hinomoto hay Anh」"
3132 = "Là 『Dọc tuyến Yunoi』. Không phải Ohitoyo――Không phải 8620.\\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yunoi."
3495 = "Ra là vậy, quả thực――Ngay cả đoạn Yunoi - Ohitoyo hiện đang chạy tàu thường,\\ncũng có thể trở thành đoạn tàu du lịch."
3719 = "Đoạn (Yunoi) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan."
```

### 02_Hibiki/日々姫08_開きかけのつぼみ.txt.toml

```toml
2260 = "「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohitoyo và Yunoi.\\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」"
2302 = "「Nói về tuyến Yunoi, kiến thức và kinh nghiệm lái tàu ở thời điểm hiện tại,\\ncô Paulette vượt trội hơn ngài Soutetsu――Chỉ đơn giản là vậy thôi ạ.」"
```

### 02_Hibiki/日々姫09_run_with_our_dreams.txt.toml

```toml
1640 = "「Nhưng mà anh hai, sao phải đi Navi vòng vèo thế để\\nđến Yunoi làm gì? Đằng nào cũng phải nghỉ lại một đêm rồi mới lên tàu mà.」"
2708 = "Yunoi hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohitoyo."
```

### 02_Hibiki/日々姫10_稀咲の未来図、日々姫の未来図.txt.toml

```toml
2613 = "「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohitoyo khổng lồ——\\\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yunoi đi.」"
```

### 02_Hibiki/日々姫11_御一夜モザイク.txt.toml

```toml
2095 = "「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohitoyo, từ đó\\\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yunoi ạ.」"
2498 = "Những thứ khác được viết chỉ là những con số đơn thuần——\\\\nMột số tiền lên đến tám chữ số bằng đồng Yên Hinomoto."
```

### 02_Hibiki/日々姫12_風.txt.toml

```toml
2279 = "「Tuyến Yunoi chạy giữa không gian xanh mướt và trên mặt sông,\\\\nnên hình ảnh gỗ cực kỳ hợp luôn! Tuyệt vời quá nha.」"
2701 = "Lấy một chút màu nước lên cọ, Hibiki cho cô bé cầm lấy,\\\\nrồi bao bọc trọn vẹn bàn tay nhỏ xíu cỡ như \\\\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku."
```

### 02_Hibiki/日々姫13_討論会.txt.toml

```toml
60 = "Điểm cuối, ga Yunoi đang đến gần.\\nLời nói của Hibiki cũng trôi chảy đi đến hồi kết."
1964 = "Bên trong sa bàn, trên tuyến Yunoi đã trở thành tuyến vòng,\\n\\x%l8620;#00ffc040;8620%l;#; và \\x%lキハ07;#00ffc040;KiHa 07%l;#;S đang lần lượt kéo theo \\x%l客車;#00ffc040;toa hành khách%l;#; mới."
```

### 02_Hibiki/日々姫14_投開票.txt.toml

```toml
1680 = "「Giống như chữ \"KiHa\" trong \\x%lキハ07;#00ffc040;KiHa 07%l;#;S, \\x%l客車;#00ffc040;toa hành khách%l;#; cũng có danh xưng――\\nchính là tên viết tắt thể hiện đặc điểm của phương tiện đó.」"
```

### 03_Paulette/グランドリライト04_ポーレット.txt.toml

```toml
1845 = "「Phải biến nó thành một chuyến tàu kết nối khu vực.\\nNgay cả ở giai đoạn hiện tại, khi chỉ mới chạy khứ hồi trên tuyến Yunoi.」"
1919 = "「Ừm. Nếu vậy——thành phố của suối nước nóng và \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;——chỉ cần dùng hình ảnh của Ohitoyo để thống nhất toàn tuyến Yunoi thì...」"
1962 = "「Trước đoạn Yatsushiro - Ohitoyo, thì phải lo cho tuyến Yunoi đã. ……Mải mê mơ mộng mà lại bỏ bê nền tảng của chính mình.」"
2006 = "「Đường sắt kỳ ảo——\\nHãy phát triển dọc tuyến Yunoi theo hình ảnh đó.」"
2067 = "「Theo em, điều cần thiết nhất tiếp theo\\nchính là 『tài nguyên du lịch khu vực Yunoi』.」"
2127 = "「Đúng vậy. Sự thành công của đoàn tàu du lịch 8620 trên tuyến Yunoi chắc chắn sẽ\\ntrở thành động lực lớn, thúc đẩy việc mua lại đất để khôi phục tuyến đường sắt.」"
2145 = "「Vâng. Áp dụng hình ảnh đó cho toàn tuyến Yunoi,\\nđể làm ví dụ thành công cho 『danh mục hóa du lịch tuyến đường sắt』 của anh.」"
2156 = "「Một tuyến đường kỳ ảo nơi thời gian ngừng trôi——nơi ta có thể trở về ngày hôm ấy một lần nữa.\\nNếu có thể phát triển tuyến Yunoi theo hướng như vậy——」"
2172 = "「Đúng vậy. Khi đó, tuyến Yunoi sẽ nằm ngoài vòng tròn——\\ntrở thành 『nơi phải cất công chuyển tàu mới đến được』.」"
2205 = "「Đúng là vậy. Do đó, ở khu vực Yunoi dọc theo tuyến Yunoi——\\ncần phải có 『giá trị đáng để cất công chuyển tàu』 sao.」"
2264 = "「Như thế không được đâu anh Soutetsu.\\nLàm vậy thì tuyến Yunoi không thể phát triển được.」"
2268 = "「Nếu vậy, cảnh quan của Ohitoyo, hay nhà ga cũ của Yunoi cũng sẽ được hồi sinh!!」"
```

### 03_Paulette/ポーレット02_古地図.txt.toml

```toml
2104 = "「Có lẽ là từ thời \\x%l大詔;#00ffc040;Taisho%l;#; nhỉ?\nTuyến Teitetsu Yunoi này, anh xem, ở đây.」"
```

### 03_Paulette/ポーレット02_解放b寝台.txt.toml

```toml
1966 = "「Không đâu ạ. Vì lợi ích của Mine Treasure,\\ncô bé được nhượng lại từ Đường sắt Suntai hiện tại mới là người phù hợp nhất.」"
```

### 03_Paulette/ポーレット03_廃炭鉱.txt.toml

```toml
75 = "\\x%lタイフォン;#00ffc040;còi Typhon%l;#; vang lên nhẹ nhàng, \\x%lキハ07;#00ffc040;KiHa 07%l;#; thả chúng tôi xuống rồi chạy vụt đi."
1723 = "「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yunoi, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsu-sen thôi.」"
1728 = "「Chừng nào chúng tôi còn ở trên này, \\x%l8620;#00ffc040;8620%l;#; sẽ không chạy.\\nToàn bộ tuyến này sẽ trở thành khu vực \\x%l閉塞;#00ffc040;phong tỏa%l;#; độc quyền của \\x%lキハ07;#00ffc040;KiHa 07%l;#;.」"
1909 = "「Theo bản đồ cũ, tuyến Yunoi với bên này từng liên thông……\\nkhả năng từng chạy thẳng qua nhau khá cao đấy ạ.」"
2087 = "「Nếu được như vậy, dù là chuyến dừng đúng giờ ở Yunoi và Ohitoyo, hay chuyến dừng tạm buổi chiều để đón bọn anh, độ an toàn cũng sẽ cao hơn.」"
2367 = "Đôi mắt xanh nãy giờ vẫn đang quan sát đường ray tuyến Yunoi rồi mặt đất xung quanh, ngẩng lên."
2743 = "Vừa nói, Paulette vừa chỉ vào tuyến chính của tuyến Yunoi."
2814 = "Trong \\x%l運転台;#00ffc040;buồng lái%l;#; của \\x%lキハ07;#00ffc040;KiHa 07%l;#; mà em còn chưa quen, Hibiki lúc này không phải \\x%l機関助士;#00ffc040;phụ lái%l;#; cũng không phải \\x%l機関士;#00ffc040;Người lái tàu%l;#;, mà đang đóng vai trò \\x%l運転士;#00ffc040;người lái%l;#;."
```

### 03_Paulette/ポーレット04_ヒヤリング.txt.toml

```toml
2023 = "Đam mê đến mức muốn lưu lại hình ảnh ngày tuyến Yunoi được khôi phục,\\nnhưng vì bận công việc nên đành phải nhờ con gái đi thay."
2532 = "Một trong những ứng cử viên thị trưởng, muốn khôi phục tuyến Yunoi thành đường sắt của thành phố\\n……Tôi đã tin chắc rằng sẽ chẳng có ai quan tâm đến một lời hứa hẹn tranh cử như vậy."
```

### 03_Paulette/ポーレット07_支線.txt.toml

```toml
2512 = "Quả thực, Hachiroku mà tôi vẫn luôn bế\\nlà thân vận hành——cơ thể có kích thước bằng con búp bê."
```

### 03_Paulette/ポーレット08_未来へのレール.txt.toml

```toml
1888 = "「Xin được kết thúc bài phát biểu tại đây.\\nChúc cho sự phát triển ngày càng lớn mạnh của Học viện Yunoi trong tương lai——」"
1910 = "「Chú kia.——Ba muốn Hikari thay mặt ba,\\ntặng bó hoa này cho thầy hiệu trưởng của Học viện Yunoi」"
2301 = "「Paulette——thì không phải cựu học sinh Học viện Yunoi,\\nReina lại là Railord——」"
2306 = "「Học viện Yunoi——Chuyến tàu kỷ niệm 80 năm thành lập à」"
2363 = "「Học viện Yunoi là ngôi trường mà Hikari sẽ theo học khi lên lớp một. Nhờ có Học viện Yunoi mà Đường sắt Ohitoyo mới có thể tồn tại được」"
2447 = "「Vậy, đi thôi nào.\\nĐến Yunoi, và xa hơn thế nữa.」"
2672 = "Những người đã liên tục hỗ trợ sự tồn tại của Đường sắt Ohitoyo, chắc chắn là các học sinh đi lại của Học viện Yunoi."
3042 = "Để đưa tiễn hiệu trưởng và những người bên Yunoi,\\nchúng tôi sẽ tiếp tục thực hiện nhiệm vụ chạy thêm một vòng nữa."
3043 = "Để cùng tồn tại với Yunoi, trường đã trở thành một học viện chuyên về khối thương mại và công nghiệp,\\ncả Nagi và Fukami đều chọn theo học ở đó."
```

### 03_Paulette/ポーレット08_線から面へ.txt.toml

```toml
1363 = "「Họ nổi điên và tràn cả ra đường ray――\\nNên \\x%lキハ07;#00ffc040;KiHa 07%l;#; không còn cách nào khác đành phải sơ tán đến Yunoi sao?」"
1628 = "「Than đá đào được sẽ nhét vào rương báu, và để \\x%lキハ07;#00ffc040;KiHa 07%l;#;\\ncứ thế hướng thẳng đến ga Yunoi.」"
1742 = "「Cho \\x%l8620;#00ffc040;8620%l;#; chạy khứ hồi giữa Ohitoyo――và Yunoi sao?」"
```

### 03_Paulette/ポーレット11_記憶と記録.txt.toml

```toml
1304 = "「Nhưng, nó đã trở thành đống sắt vụn.\\nCùng với thân bảo trì của tôi.」"
```

### 03_Paulette/ポーレット14_ふたたび走り出すために.txt.toml

```toml
83 = "Quá trình nhả phanh từng nấc cực kỳ mượt mà——\\n\\x%l8620;#00ffc040;8620%l;#; như lướt đi, tiến vào ga Yunoi."
2286 = "Nhìn theo bóng lưng họ, Hachiroku với thân vận hành nhỏ bé,\\ntrong mắt tôi lại trông thật to lớn và đáng tin cậy."
2530 = "Chưa kịp ngăn lại, Hachiroku đã thay sang thân bảo trì,\\nvà thoăn thoắt bước xuống khỏi buồng lái."
```

### 03_Paulette/ポーレット15_求人難.txt.toml

```toml
1073 = "「\\x%lマスコン;#00ffc040;Điều khiển trung tâm%l;#;?」"
1664 = "「Là điều khiển trung tâm. Điều khiển bằng điện……\\nlà một thiết bị lái giống như hộp số tự động của xe bốn bánh vậy.」"
1981 = "「Kuha 26 là toa xe được trang bị \\x%lマスコン;#00ffc040;điều khiển trung tâm%l;#;. Nên là.」"
```

### 03_Paulette/ポーレット16_明日へのレール.txt.toml

```toml
1971 = "「Đang đợi——ở chỗ \\x%lキハ07;#00ffc040;KiHa 07%l;#; sao!?」"
2032 = "「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ. Chỉ trong phạm vi 24,8 km từ Ohitoyo đến Yunoi.」"
2835 = "Cất công cải tạo lại \\x%lキハ07;#00ffc040;KiHa 07%l;#; để phục vụ cho chuyến thị sát,\\nvậy mà Reina vẫn phải cố nhịn không được lên tàu."
3251 = "Nhả phanh, gài số,\\ntừ bàn tay đặt lên cần gạt, truyền lực đến \\x%lキハ07;#00ffc040;KiHa 07%l;#;."
```

### 04_Reina/れいなh4_ふたりっきりのハロウィン.txt.toml

```toml
2241 = "「Tàu quay đầu, rốt cuộc cũng là chuyến tàu\\nđã đi đến tận Yunoi.」"
```

### 05_Mayami/lr真闇追加01_新婚旅行のリクエスト.txt.toml

```toml
1239 = "「KiHa 07S của bé Reina cũng vất vả mà nhỉ.\\nChỉ có một mình Pau-chan」"
1512 = "「KiHa 07S là toa xe diesel tự hành mà,\\nnên có vất vả thì cũng không bằng đầu máy hơi nước đâu ạ」"
```

### 05_Mayami/lr真闇追加02_御一夜新婚旅行.txt.toml

```toml
1545 = "「Tuyến Yunoi dài khoảng 25km, vừa ngắn lại vừa bằng phẳng mà.\\nĐối với anh, một chiều đi thường chỉ tốn khoảng 550 xẻng là cùng.」"
1884 = "\"Tắm rửa, ăn uống và lên chuyến tàu KiHa 07S.\\nChuyến tham quan Ohitoyo chỉ còn lại những việc đó để khép lại.\""
```

### 05_Mayami/真闇01_再蒸留.txt.toml

```toml
1425 = "「A, hình như chị có……nghe nói rồi? \\nỪm……Cái tổ chức ở……Minh Quốc (Mỹ) ấy hả?」"
1511 = "「Dù có bị điểm 0 đi nữa, thì khách hàng nhà mình cũng chỉ cười và nói rằng \\n『Mấy tên nhà quê ở Minh Quốc thì biết gì về mùi vị của rượu chứ』 thôi.」"
1562 = "「Tôi hiểu rồi. Nếu vậy, hãy cho \\nnhững kẻ nhà quê ở Minh Quốc biết, sự thơm ngon của rượu Kuma shochu là như thế nào.」"
1604 = "「Đúng vậy. Và hầu hết giám khảo là người Minh Quốc. \\nNgười Hinomoto, nếu có thì cũng chỉ khoảng 2-3 người là cùng.」"
1641 = "「Chỉ riêng khu vực quanh Ohitoyo đã từng sầm uất đến thế này mà…… \\nĐến năm 46, lại chỉ còn mỗi Tuyến Yunoi thôi sao.」"
2415 = "Khu vực \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động đã giúp Tuyến Yunoi tồn tại, \\nnhưng nếu nhìn từ giá trị của một địa điểm du lịch thì nó lại trở thành xiềng xích."
```

### 05_Mayami/真闇h3_補習授業の廃校舎.txt.toml

```toml
3917 = "Tiễn chiếc KiHa 07S dừng đỗ tạm thời đi, chúng tôi rời khỏi nhà ga.\\nNgay lúc đó, chị Mayami vươn vai thật dài."
```

### 06_Kisaki/グランドリライト06_稀咲.txt.toml

```toml
2146 = "「Cần tới bốn người cơ á! Phải làm thế――từng chỗ một sao?\\nĐường ray dài lắm mà, chỉ tính riêng đoạn giữa Ohitoyo và Yunoi thôi cũng đã...」"
2159 = "「Ông Seki――ông ngoại của Fukami, các tình nguyện viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#;,\\nvà cả chúng ta, những người liên quan đến Đường sắt Ohitoyo.」"
2202 = "「Ngay cả loại đường ray ngắn và nhẹ như đang dùng ở tuyến Yunoi,\\nmỗi mét cũng nặng 30kg, một thanh dài 10 mét là 300kg rồi.」"
2608 = "「Biến tuyến Yunoi thành biểu tượng của sự hoài niệm, và cho chạy chuyến tàu du lịch hướng tới tương lai.\\nDù chi tiết về chuyến tàu vẫn chưa được quyết định, nhưng ý tưởng này rất đáng được đánh giá cao.」"
3472 = "Akai-guji nhẹ nhàng lấy từ trong chiếc túi phi hành đoàn ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít."
```

### 07_Nagi_Fukami/凪ふかみ05_凪の開眼！？.txt.toml

```toml
1979 = "「Hai chị em, một bé tầm 4-5 tuổi, bé kia tầm 2-3 tuổi.\\nBé lớn hơn thì đang khám ở bệnh viện suối nước nóng Yunoi.」"
2972 = "A, sảng khoái quá đi!\\nSau đó chỉ cần đỗ tàu thật chuẩn xác ở Yunoi là xong!"
```

### 07_Nagi_Fukami/凪ふかみ08c_新しい家族.txt.toml

```toml
2068 = "「Ừ, hẹn gặp ở Yunoi.」"
2541 = "「Vậy, em qua \\x%l客車;#00ffc040;toa hành khách%l;#; đây.\\nHẹn gặp lại ở Yunoi nhé!」"
```

### 09_Grand/グランドリライト08_ふかみ.txt.toml

```toml
1648 = "「Đúng vậy. Bước tiến vọt của Kisaki――của Đường sắt Hinomoto,\\nđang là niềm hy vọng to lớn của Kế hoạch Nine Stars.」"
1948 = "「Chắc là vậy rồi. Nhân cơ hội này, tuyệt đối chắc chắn,\\nĐường sắt Hinomoto sẽ bị ép giá thê thảm.」"
2008 = "「Khách du lịch quốc tế, trong trường hợp này, là từ góc nhìn của Hinomoto\\nđối với nước ngoài――chỉ những du khách đến từ các nước khác.」"
2017 = "「Chỉ có Hinomoto! Chỉ có Kyushu!!\\nMới có được tuyến đường sắt kết nối dài đến như vậy đó!」"
2032 = "「Nhờ Đường sắt Hinomoto gánh vác phần đường ray, các công ty đường sắt\\nmới có đủ khả năng để thúc đẩy Kế hoạch Nine Stars.」"
2044 = "「Đúng vậy. Không chỉ Dự án Nine Stars,\\nmà cô ấy thậm chí đã biết cả chuyện của Đường sắt Hinomoto nữa.」"
2260 = "「Nó thể hiện đây là ga khởi điểm của Tuyến Rail Romanesque Yunoi. Và của Nine Stars.\\nCó thể nói, đó là một nhà khách gắn liền với nhà ga.」"
2271 = "「Nếu vậy thì, Hinomoto có thể là quốc gia đầu tiên,\\nthoát khỏi tình trạng đó nhỉ~」"
2289 = "「Ngài Soutetsu. Tôi hoàn toàn không nắm rõ\\ntình hình đường sắt ở các quốc gia khác ngoài Hinomoto, nhưng mà.」"
2553 = "Nhờ nguồn vốn huy động được từ quỹ, Đường sắt Hinomoto\\nvẫn đang tiếp tục gặt hái những thành quả tuyệt vời ngoài mong đợi."
2634 = "Nếu xử lý sai lầm,\\nNine Stars và cả Đường sắt Hinomoto sẽ tan thành mây khói."
2746 = "Đường sắt Hinomoto với tư cách là một đối tượng đầu tư,\\nsẽ còn mất nhiều năm nữa mới có thể trả cổ tức."
2966 = "Kisaki quả thực là người sáng lập,\\nnhưng xét về vị trí hiện tại, cô ấy chỉ là Giám đốc của Đường sắt Hinomoto."
```

### 09_Grand/グランドリライト11_ナインスターズ！.txt.toml

```toml
1619 = "『Những người nên ở lại tuyến Yunoi là chúng tôi và đầu máy số 9』\\n『Mong cậu hãy để KiHa 07S chạy song hành cùng 8620』."
1683 = "「……Là phương tiện đi lại thường ngày thì không thể thắng nổi Aircra đâu.\\nTrừ phi có hoàn cảnh đặc biệt như tuyến Yunoi.」"
3212 = "Kể cả khi tôi thay mặt anh Munakata, chở các học sinh trên toa hành khách hộp diêm,\\nvà kéo chuyến tàu hướng đến Yunoi bằng đầu máy số 9."
3374 = "Đường số 1. Đầu máy số 9 đang đỗ ở sân ga phía tuyến Yunoi.\\nBên cạnh là \\x%l機関士;#00ffc040;lái tàu%l;#; Munakata và Olivy."
3526 = "Bởi vì tuyến Hisatsu mà chúng tôi đang chạy,\\nsẽ hướng đến Okoba, vượt qua núi Yadake."
3916 = "Sau khi rời Ohitoyo một đoạn,\\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yunoi trên tuyến Yunoi."
```

### 10_Chikuni/仲国01_副丘→北琴.txt.toml

```toml
2011 = "「Ừ. Nghe nói dù có làm cách nào cũng không thể\\nmang thân vận hành ra nước ngoài được mà.」"
```

### 10_Chikuni/仲国03_北琴鉄道歴史館.txt.toml

```toml
2304 = "「Và 9700 cũng là \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; 1D1 đầu tiên được sản xuất tại Minh Quốc——\\nVì vậy, để thể hiện sự tôn trọng đối với bên đặt hàng」"
2389 = "「Tuyến Yunoi cũng là tuyến đường bằng phẳng trên vùng đất bằng phẳng mà.\\nHachiroku không biết về những tuyến đường nền đất yếu cũng là điều dễ hiểu thôi.」"
2430 = "「9700, đầu máy hơi nước dòng 9700 có hình thức 1D1——\\nNhưng các cô ấy là những \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu, được đặt hàng từ Minh Quốc (Mỹ).」"
```

Kết bài
Đợt U4 hoàn tất: 193 dòng thuộc 11 mục thuật ngữ §1 set-3 (T6, T7, T15, T16, T41, T45, T47, T11, T12, T19, T20) đã đọc JP (+TW) từng dòng, sửa đúng dạng đích đã khóa, soát lại 193/193, khối TOML parse-verified 193/193 (chạy lại sau rebase 3719). Hai mục trong batch đã xong từ trước (T54: 0 dòng — audit đã sửa "vé lượt"/"vé định kỳ"; T55: 0 dòng — unification đã gộp đã sửa "Nhân giống"). Dòng 日々姫08 3719 đã rebase về giá trị gộp của U2c (cộng dồn "(Yunoi)" + "Đường sắt Ohitoyo") theo cảnh báo chồng lấn của coordinator. Còn chờ batch khác: 2 dòng "Ohimitera" còn sót (共通14 1671/1805) đã cờ cho batch leftovers; các mục con OPEN của T20 (gồm "bác Seki" 2027 và "các ông của Nagi" 2588) đã cờ cho batch leftovers; 12 dòng "phi hành đoàn" của túi (T18) không thuộc batch này.
