# Unification batch U2a — T1 (御一夜 → "Ohitoyo") + T2 (御一夜鉄道 → "Đường sắt Ohitoyo"), folders 00–05

## §0. Phạm vi

- Mục: **T1** (DECIDED 19/11, Hieu — 御一夜 → "Ohitoyo") và **T2** (DECIDED 21/11 ~17:30, Muse theo uỷ quyền — 御一夜鉄道 → "Đường sắt Ohitoyo"). T2 là tập con của T1: áp dạng dài "Đường sắt Ohitoyo" trước, rồi dạng trần "Ohito" → "Ohitoyo"; một dòng chứa cả hai dạng = một mục, item "T1+T2".
- Thư mục: **00_Common / 01_Hachiroku / 02_Hibiki / 03_Paulette / 04_Reina / 05_Mayami**. Các dòng chứa "Ohimitera" KHÔNG thuộc batch này (batch U1).
- Kết quả: **136 dòng sửa** — T2: 95, T1: 39, T1+T2: 2. Phân bố theo thư mục: 01_Hachiroku 119, 03_Paulette 9, 02_Hibiki 5, 05_Mayami 2, 04_Reina 1, **00_Common 0** (mọi dòng "Ohito" ở Common đã được sửa thành "Ohitoyo" trong audit — kiểm chứng bằng quét toàn bộ good-set, xem §1).
- So với ước lượng trong UNIFICATION-LIST.md §0 (T1 còn 219, T2 còn 132 toàn dự án): batch này xử lý 97/132 dòng T2 còn lại và 41 dòng có dạng trần (39 T1 + 2 T1+T2) trong 6 thư mục đầu. Phần còn lại thuộc các thư mục 06–11, do các batch sau xử lý.

## §1. Phương pháp liệt kê (chỉ đếm, không sửa hàng loạt)

1. Đọc CSV3 good-set 87.833 dòng (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`; riêng trong phạm vi 00–05, 4 file 共通02/03/04/06 có bộ stale ở 00_Common đã bị loại — nếu không loại, các dòng stale đó sẽ lọt vào danh sách ứng viên sai).
2. Tính giá trị hiện tại (current value) cho mọi dòng trong 00–05: giá trị fix moan nếu (file,key) có trong bất kỳ `moans/moan-*-wrong.json` nào (gồm cả supplement ハチロクh3), nếu không thì giá trị fix audit nếu có trong bất kỳ `audit-*-wrong.json` nào, nếu không thì VN CSV3. Đã nạp toàn bộ 217 file audit (9.500 mục) + 66 file moan (1.535 mục). Ghép fix-list với CSV3 bằng cặp (key, JP) — 46 nhóm (key,JP) trùng trong good-set, nhưng **không ứng viên nào** nằm trong nhóm trùng, nên việc ghép là không mơ hồ đối với batch này.
3. Ứng viên = current value chứa `Ohito` KHÔNG theo sau bởi `yo` (regex `Ohito(?!yo)` — bắt buộc, vì "Ohitoyo" đã đúng tự nó đã chứa chuỗi "Ohito"; lần quét đầu bằng substring thô đã trả 698 dòng, hầu hết là "Ohitoyo" đúng sẵn) và KHÔNG chứa "Ohimitera". Được **136 ứng viên**, 142 lần xuất hiện dạng trần.
4. Kiểm chứng chéo current value với TOML-2 (227 file): 136/136 dòng đều có mặt; 20 dòng "mismatch" khi so sánh thô đều giải thích được — 11 dòng chỉ khác khoảng trắng do TOML-2 dẹp literal `\n` thành khoảng trắng, 8 dòng audit-src khác ở phần KHÔNG liên quan tới Ohito (audit đã sửa đại từ/gloss khác), và 1 dòng ポーレット03 1750 là fix misaligned của audit (VN cũ trong CSV3 "Ây da, chào cô bé đáng yêu nhé." — audit đã sửa thành đúng; old_vn trong JSON này = giá trị audit, đúng quy ước). Không dòng nào bị tính sai current value vì fix-list ghép trượt: trong 354 mục audit không ghép được bằng (key,JP), chỉ có 30 mục nhắc tới Ohito — tất cả đều là file 00_Common 14 dạng "Ohimitera"→"Ohitoyo" (đã sửa trong audit, thuộc batch U1, ngoài phạm vi).
5. Đọc từng dòng ứng viên: JP (+TW) của cả 136 dòng đã được đọc hết (xem §2). Dạng JP: 御一夜鉄道 80, 御一夜 35, オヒトヨ 11, 御鉄 9, おひとよ 1. TW đồng ý 135/136; dòng duy nhất TW không nhắc tên công ty (ハチロク04_小畑越え 1902, TW lược bỏ) thì JP thắng TW — vẫn sửa (ghi chú ở §3). Không có dòng nào "Ohito" nằm trong gloss %l (đã kiểm tra bằng máy: 0 lần xuất hiện trong thẻ %l) — mọi lần xuất hiện đều là display text.
6. Fix = chỉ thay thế đúng chuỗi mục tiêu, giữ nguyên toàn bộ phần còn lại (kể cả "tuyến Yui" ở ハチロク08 2828/2868 — thuộc mục T7, không đụng; kể cả các phần audit đã sửa khác trong 9 dòng audit-src). Thứ tự: "Đường sắt Ohito" → "Đường sắt Ohitoyo" trước, rồi "Ohito" trần còn lại → "Ohitoyo".

## §2. Quyết định trong batch (theo uỷ quyền của Hieu — điều tra JP+TW rồi quyết, không park)

- **御鉄 (9 dòng) = 御一夜鉄道 → "Đường sắt Ohitoyo" (T2).** Bằng chứng: 御鉄 là dạng viết tắt quen thuộc của 御一夜鉄道 (ruby [おんてつ,1] trong JP của 5/9 dòng); TW của cả 9 dòng đều viết 御鐵, tức công ty đường sắt, không phải địa danh; VN cũ của cả 9 dòng đều đã dịch là "Đường sắt Ohito". Các dòng: ハチロク02 2327/2647, ハチロク12 2058/2233, ハチロク15a 2038/2116, ハチロク15b 1299, ハチロク16 2070, lr真闇追加02 1350.
- **オヒトヨ katakana (11 dòng) và おひとよ hiragana (1 dòng) = 御一夜/御一夜鉄道, sửa như kanji.** Bằng chứng: TW của cả 12 dòng đều viết 御一夜/御一夜鐵路; ngữ cảnh (nhân vật Olivy nói giọng trẻ con, hoặc lời thoại thường) giải thích cách viết kana. Các dòng: ハチロク05 2640/2922, ハチロク08 2327/2328/2828/2868, ハチロク13 1694/1955, ハチロク14 1780/2918, ハチロク15b 1637, ポーレット03 2015.
- **Không có quyết định OPEN nào khác trong batch.** T1/T2 đều DECIDED; mọi ứng viên đều có JP xác nhận trực tiếp hoặc qua dạng viết tắt/kana đã quyết ở trên.

## 01_Hachiroku — `ハチロク01_こんにちわ赤ちゃん.txt.toml` (7 dòng)

### key 1670 — item T2 (JP: 御一夜鉄道)

- JP: 「……そのような、いわば回帰があることは、\n御一夜鉄道で働けば、誰にでも容易にわかることです」
- TW: 「……這在某種程度上說也算是回歸鐵路的原點。但凡是在御一夜鐵路工作過的人，都會很快意識到這點」
- old_vn (csv3): 「……Một sự trở về như vậy,\nchỉ cần làm việc ở Đường sắt Ohito, thì ai cũng có thể dễ dàng nhận ra thôi.」
- fix: 「……Một sự trở về như vậy,\nchỉ cần làm việc ở Đường sắt Ohitoyo, thì ai cũng có thể dễ dàng nhận ra thôi.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2096 — item T2 (JP: 御一夜鉄道)

- JP: 「そこを埋め合わせる何物をも、\n六年、御一夜鉄道は出してこなかったわけか」
- TW: 「也就是說，御一夜鐵路用了六年時間，也沒能找到彌補這一鴻溝的方法嗎」
- old_vn (csv3): 「Tức là, trong suốt 6 năm qua, Đường sắt Ohito đã không thể\nđưa ra bất cứ thứ gì để bù đắp cho điều đó sao.」
- fix: 「Tức là, trong suốt 6 năm qua, Đường sắt Ohitoyo đã không thể\nđưa ra bất cứ thứ gì để bù đắp cho điều đó sao.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2135 — item T2 (JP: 御一夜鉄道)

- JP: 「みかん鉄道が新車両を導入し、\n[よじょうき,2]余剰機を御一夜鉄道に回せるように――だな？」
- TW: 「你是想讓橙鐵路購入新車輛，從而將汰換車輛調度給御一夜鐵路——對嗎？」
- old_vn (csv3): 「Để Đường sắt Mikan đưa vào sử dụng phương tiện mới,\nvà chuyển các đầu máy dư thừa cho Đường sắt Ohito——đúng không?」
- fix: 「Để Đường sắt Mikan đưa vào sử dụng phương tiện mới,\nvà chuyển các đầu máy dư thừa cho Đường sắt Ohitoyo——đúng không?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2161 — item T2 (JP: 御一夜鉄道)

- JP: 「原因が何かを御一夜鉄道がきちんと分析できているのか。\n双鉄君、君の口から聞かせてもらおう」
- TW: 「其中緣由御一夜鐵路可有進行過徹底分析嗎？雙鐵，我要你親口給我個解釋」
- old_vn (csv3): 「Đường sắt Ohito đã phân tích kỹ càng nguyên nhân là gì chưa.\nCậu Soutetsu, hãy để tôi nghe từ chính miệng cậu xem nào.」
- fix: 「Đường sắt Ohitoyo đã phân tích kỹ càng nguyên nhân là gì chưa.\nCậu Soutetsu, hãy để tôi nghe từ chính miệng cậu xem nào.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2412 — item T2 (JP: 御一夜鉄道)

- JP: 「実際、御一夜鉄道はこの六年、常に前年比５％以上、\n極めて順調に営業利益を伸ばし続けている」
- TW: 「實際上，御一夜鐵路的利潤在這六年間一直維持著５％以上的年增長率，可謂是極其順利的增長節奏了」
- old_vn (csv3): 「Thực tế, Đường sắt Ohito trong 6 năm qua, luôn đạt mức tăng trưởng trên 5% so với năm trước,\nlợi nhuận kinh doanh tiếp tục tăng trưởng cực kỳ thuận lợi.」
- fix: 「Thực tế, Đường sắt Ohitoyo trong 6 năm qua, luôn đạt mức tăng trưởng trên 5% so với năm trước,\nlợi nhuận kinh doanh tiếp tục tăng trưởng cực kỳ thuận lợi.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2468 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道[ゆのい,1]湯医線には、他の路線と比較した時、\n\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;[しょうち,1]招致に圧倒的に有利な点があります」
- TW: 「御一夜鐵路湯醫線在招攬\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;方面，相比其他線路擁有壓倒性的優勢」
- old_vn (csv3): 「Tuyến Yunoi của Đường sắt Ohito, khi so sánh với các tuyến khác,\ncó một lợi thế áp đảo trong việc thu hút \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;.」
- fix: 「Tuyến Yunoi của Đường sắt Ohitoyo, khi so sánh với các tuyến khác,\ncó một lợi thế áp đảo trong việc thu hút \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2494 — item T2 (JP: 御一夜鉄道)

- JP: 「ご指摘の通りです。御一夜鉄道は本構想の発信源であり、\n中心であるにも関わらず、出遅れてしまっています」
- TW: 「您批評的是。雖然御一夜鐵路是這一藍圖的發源地，同時又是其核心所在，卻反而在行動上落後了」
- old_vn (csv3): 「Đúng như ông đã chỉ ra. Đường sắt Ohito là nơi khởi nguồn của dự án này,\nmặc dù là trung tâm, nhưng lại bị chậm chân.」
- fix: 「Đúng như ông đã chỉ ra. Đường sắt Ohitoyo là nơi khởi nguồn của dự án này,\nmặc dù là trung tâm, nhưng lại bị chậm chân.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク01_双鉄の目・ハチロクの目.txt.toml` (2 dòng)

### key 1710 — item T2 (JP: 御一夜鉄道)

- JP: 「実は、私も見るの初めて。ポーレットさんに聞くまで、\n御一夜鉄道の公式サイトがあるって、知らんかったし」
- TW: 「其實我也是第一次。要不是波萊特小姐告訴我，我都不知道御一夜鐵路還有官方網站」
- old_vn (csv3): 「Thực ra, em cũng mới xem lần đầu. Trước khi nghe chị Paulette nói,\nem còn chẳng biết Đường sắt Ohito có trang web chính thức cơ.」
- fix: 「Thực ra, em cũng mới xem lần đầu. Trước khi nghe chị Paulette nói,\nem còn chẳng biết Đường sắt Ohitoyo có trang web chính thức cơ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2109 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道の公式サイトで紹介するってゆっとった。\nちょっとまって、検索ですぐ出せるけん」
- TW: 「說是要放到御一夜鐵路的官方網站上。等我一下，搜搜就有咧」
- old_vn (csv3): 「Chị ấy bảo sẽ giới thiệu trên trang web chính thức của Đường sắt Ohito.\nĐợi chút, tìm kiếm cái là ra ngay ấy mà.」
- fix: 「Chị ấy bảo sẽ giới thiệu trên trang web chính thức của Đường sắt Ohitoyo.\nĐợi chút, tìm kiếm cái là ra ngay ấy mà.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク02_ハートブレイク・レイルロオド.txt.toml` (29 dòng)

### key 1974 — item T2 (JP: 御一夜鉄道)

- JP: 「みかん鉄道さんと御一夜鉄道を本当の意味で繋ぐために、\n[きゅう]Ⅸ号がどうしても必要って、粘り強くお話したんです」
- TW: 「九號是讓橙鐵路和御一夜鐵路真正緊密相連的關鍵紐帶，所以我始終沒有放棄」
- old_vn (csv3): 「Em đã kiên trì thuyết phục họ rằng, để thực sự kết nối Đường sắt Mikan và Đường sắt Ohito,\nthì Đầu máy số 9 là vô cùng cần thiết.」
- fix: 「Em đã kiên trì thuyết phục họ rằng, để thực sự kết nối Đường sắt Mikan và Đường sắt Ohitoyo,\nthì Đầu máy số 9 là vô cùng cần thiết.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2023 — item T2 (JP: 御一夜鉄道)

- JP: 「あなたがオリヴィさんですね？　はじめまして。\nようこそ、御一夜鉄道へ」
- TW: 「你就是奧莉薇小姐吧？晚安，歡迎來到御一夜鐵路」
- old_vn (csv3): 「Cô là cô Olivy đúng không ạ? Lần đầu gặp mặt.\nChào mừng cô đến với Đường sắt Ohito.」
- fix: 「Cô là cô Olivy đúng không ạ? Lần đầu gặp mặt.\nChào mừng cô đến với Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2191 — item T1 (JP: 御一夜)

- JP: 「うん。御一夜温泉駅イラストマップもつくったけん！\n調印が終わるまで、駅の案内ばしてあげるつもり」
- TW: 「嗯，我還畫了御一夜溫泉站的彩繪地圖！打算在簽約儀式完成前帶她參觀車站」
- old_vn (csv3): 「Vâng. Em cũng đã vẽ xong bản đồ minh họa Ga Suối nước nóng Ohito rồi á!\nTrong lúc chờ ký kết xong, em định sẽ hướng dẫn bé ấy tham quan ga.」
- fix: 「Vâng. Em cũng đã vẽ xong bản đồ minh họa Ga Suối nước nóng Ohitoyo rồi á!\nTrong lúc chờ ký kết xong, em định sẽ hướng dẫn bé ấy tham quan ga.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2327 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「御鉄のみなさんは歓迎してくれているんだぞ。\nそれを……オリヴィ。みかん鉄道の名前を[けが]汚す気か」
- TW: 「御鐵的人們可正在歡迎我們。奧莉薇……你打算辜負人家的好意，給我們橙鐵路抹黑嗎」
- old_vn (csv3): 「Mọi người ở Đường sắt Ohito đang chào đón chúng ta đấy.\nVậy mà……Olivy. Cô định làm ô uế danh tiếng của Đường sắt Mikan sao.」
- fix: 「Mọi người ở Đường sắt Ohitoyo đang chào đón chúng ta đấy.\nVậy mà……Olivy. Cô định làm ô uế danh tiếng của Đường sắt Mikan sao.」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2376 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道運輸部長、\x%l保線部長;#00ffc040;保線部長%l;#;。\n兼、8620号のまいてつ蒸気\x%l機関士;#00ffc040;機関士%l;#;、右田双鉄だ」
- TW: 「我是御一夜鐵路運輸部長及\x%l保線部長;#00ffc040;巡線部長%l;#;，兼８６２０號掌車人\x%l機関士;#00ffc040;司機%l;#;，右田雙鐵」
- old_vn (csv3): 「Trưởng phòng Vận tải Đường sắt Ohito, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\nKiêm chủ tàu 8620, \x%l機関士;#00ffc040;người lái tàu%l;#; hơi nước, Migita Soutetsu.」
- fix: 「Trưởng phòng Vận tải Đường sắt Ohitoyo, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\nKiêm chủ tàu 8620, \x%l機関士;#00ffc040;người lái tàu%l;#; hơi nước, Migita Soutetsu.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2378 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道8620専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;、ハチロクです。\nオリヴィちゃん。これからよろしくお願いしますね？」
- TW: 「我是御一夜鐵路８６２０專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;八六。今後請多關照，奧莉薇」
- old_vn (csv3): 「\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 Đường sắt Ohito, Hachiroku.\nBé Olivy. Từ nay mong được em giúp đỡ nhé?」
- fix: 「\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 Đường sắt Ohitoyo, Hachiroku.\nBé Olivy. Từ nay mong được em giúp đỡ nhé?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2409 — item T1 (JP: 御一夜)

- JP: 「そしたら、それを聞きつけてくれたオリヴィちゃんが、\n多分自分から、御一夜移籍を志願してくれたんですよ！」
- TW: 「於是奧莉薇在聽說之後，就說願意到御一夜來工作！嗯，應該是她主動提出的」
- old_vn (csv3): 「Thế rồi, bé Olivy nghe được chuyện đó,\ncó lẽ đã tự mình tình nguyện chuyển đến Ohito đấy!」
- fix: 「Thế rồi, bé Olivy nghe được chuyện đó,\ncó lẽ đã tự mình tình nguyện chuyển đến Ohitoyo đấy!」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2431 — item T1 (JP: 御一夜)

- JP: 「オリヴィちゃんからです！\n凄いテンションで『いますぐ御一夜にいくー！』って」
- TW: 「是奧莉薇打來的！她激動地和我們說“馬上出發去御一夜！”」
- old_vn (csv3): 「Là bé Olivy gọi ạ!\nBé ấy phấn khích lắm, bảo là 『Em sẽ đến Ohito ngay bây giờ~!』」
- fix: 「Là bé Olivy gọi ạ!\nBé ấy phấn khích lắm, bảo là 『Em sẽ đến Ohitoyo ngay bây giờ~!』」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2473 — item T2 (JP: 御一夜鉄道)

- JP: 「いらっしゃーい！　ようこそ御一夜鉄道へ！！！」
- TW: 「歡迎來到御一夜鐵路！！！」
- old_vn (csv3): 「Chào mừng~! Chào mừng đến với Đường sắt Ohito!!!」
- fix: 「Chào mừng~! Chào mừng đến với Đường sắt Ohitoyo!!!」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2501 — item T2 (JP: 御一夜鉄道)

- JP: 「オリヴィちゃんとⅨ号機関車が、\n御一夜鉄道に来てくれたことを祝して――」
- TW: 「為慶祝奧莉薇和九號機車來到御一夜鐵路——」
- old_vn (csv3): 「Chúc mừng bé Olivy và Đầu máy số 9,\nđã đến với Đường sắt Ohito——」
- fix: 「Chúc mừng bé Olivy và Đầu máy số 9,\nđã đến với Đường sắt Ohitoyo——」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2505 — item T1 (JP: 御一夜)

- JP: 「それで、御一夜温泉駅に戻ってきたら、\nついさっき、また電話がかかってきたんですよぉ」
- TW: 「然後等我們回到御一夜溫泉站，剛才就又有電話打了過來」
- old_vn (csv3): 「Rồi sau đó, lúc tụi em quay lại ga Suối nước nóng Ohito,\nthì vừa nãy lại có điện thoại gọi tới đó ạ~」
- fix: 「Rồi sau đó, lúc tụi em quay lại ga Suối nước nóng Ohitoyo,\nthì vừa nãy lại có điện thoại gọi tới đó ạ~」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2544 — item T2 (JP: 御一夜鉄道)

- JP: 「やっと来たばい！\nいらっしゃーい！　ようこそ御一夜鉄道へ！！」
- TW: 「終於下來嘞！歡迎來到御一夜鐵路！！」
- old_vn (csv3): 「Cuối cùng cũng đến rồi á!\nChào mừng~! Chào mừng đến với Đường sắt Ohito!!」
- fix: 「Cuối cùng cũng đến rồi á!\nChào mừng~! Chào mừng đến với Đường sắt Ohitoyo!!」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2556 — item T2 (JP: 御一夜鉄道)

- JP: 「まぁ、頼もしいこと。一分一秒も無駄にせず、\n早く御一夜鉄道で働きたいと思ってくれているのですね」
- TW: 「著實值得欽佩。看來對方是不願浪費一分一秒，想儘快來我們御一夜鐵路工作呀」
- old_vn (csv3): 「Chà, đáng tin cậy thật. Chắc hẳn họ không muốn lãng phí một phút một giây nào,\nvà muốn làm việc ở Đường sắt Ohito càng sớm càng tốt đây mà.」
- fix: 「Chà, đáng tin cậy thật. Chắc hẳn họ không muốn lãng phí một phút một giây nào,\nvà muốn làm việc ở Đường sắt Ohitoyo càng sớm càng tốt đây mà.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2563 — item T1 (JP: 御一夜)

- JP: 「蒸気のふるさと御一夜は、\nⅨ号機関車とオリヴィさんをお待ちしてました！」
- TW: 「蒸汽之鄉御一夜，恭候九號機車和奧莉薇小姐多時了！」
- old_vn (csv3): 「Quê hương hơi nước Ohito,\nđã chờ đợi Đầu máy số 9 và cô Olivy từ lâu rồi ạ!」
- fix: 「Quê hương hơi nước Ohitoyo,\nđã chờ đợi Đầu máy số 9 và cô Olivy từ lâu rồi ạ!」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2564 — item T1 (JP: 御一夜)

- JP: 「蒸気のふるさと御一夜は、Ⅸ号機関車とオリヴィさんを、\n大歓迎でお迎えします！　です！！」
- TW: 「蒸汽之鄉御一夜，熱烈歡迎九號機車和奧莉薇小姐！嗯！！」
- old_vn (csv3): 「Quê hương hơi nước Ohito, nhiệt liệt chào mừng Đầu máy số 9 và cô Olivy!\nạ!!」
- fix: 「Quê hương hơi nước Ohitoyo, nhiệt liệt chào mừng Đầu máy số 9 và cô Olivy!\nạ!!」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2580 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道への移籍話をききつけたらもう、\n『オリヴィを捨てるんだ！』ってなっちゃったらしくて」
- TW: 「說是聽說自己要到御一夜鐵路工作，她就鬧脾氣說“你們要拋棄奧莉薇！”」
- old_vn (csv3): 「Vừa nghe tin chuyển nhượng đến Đường sắt Ohito là bé ấy đã,\n『Mọi người định vứt bỏ Olivy!』 rồi phản ứng gay gắt luôn ạ.」
- fix: 「Vừa nghe tin chuyển nhượng đến Đường sắt Ohitoyo là bé ấy đã,\n『Mọi người định vứt bỏ Olivy!』 rồi phản ứng gay gắt luôn ạ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2629 — item T1 (JP: 御一夜)

- JP: 「なんと、それも異例だな。[おこば,1]小畑を越えたなら、\n御一夜まで一緒に来て休めばいいのに」
- TW: 「這也不太對勁啊。既然都過了大畑，何不連補機一起開到御一夜休整」
- old_vn (csv3): 「Chà, thế cũng khác thường nhỉ. Đã qua Okoba rồi,\nthì cứ đến thẳng Ohito nghỉ ngơi luôn cũng được mà.」
- fix: 「Chà, thế cũng khác thường nhỉ. Đã qua Okoba rồi,\nthì cứ đến thẳng Ohitoyo nghỉ ngơi luôn cũng được mà.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2640 — item T2 (JP: 御一夜鉄道)

- JP: 「なーんか、気分のよくなか話ばいねー。\n御一夜鉄道、ゴミ箱扱いされとるみたいばい」
- TW: 「這話怎麼那麼難聽呢。整得咱御一夜鐵路就像垃圾箱一樣」
- old_vn (csv3): 「Cứ thấy, câu chuyện này không vui vẻ gì á.\nCứ như Đường sắt Ohito bị coi là thùng rác vậy á.」
- fix: 「Cứ thấy, câu chuyện này không vui vẻ gì á.\nCứ như Đường sắt Ohitoyo bị coi là thùng rác vậy á.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2647 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「いい加減にしろ。今朝からなんだ。\nお前のわがままに[おんてつ,1]御鉄さんまで巻き込んでいるんだぞ」
- TW: 「適可而止一點，你今天從一早開始就在鬧。你的任性要求甚至都影響到人家御鐵了」
- old_vn (csv3): 「Vừa phải thôi. Từ sáng đến giờ rồi.\nSự ích kỷ của cô đang kéo cả Đường sắt Ohito vào đấy.」
- fix: 「Vừa phải thôi. Từ sáng đến giờ rồi.\nSự ích kỷ của cô đang kéo cả Đường sắt Ohitoyo vào đấy.」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3027 — item T2 (JP: 御一夜鉄道)

- JP: みんなが笑顔で歓迎のための準備をしている。\nこれが御一夜鉄道なのだと、じわり、感じる。
- TW: 大家都面帶笑容地為歡迎做準備，讓我深深感受到這就是御一夜鐵路的作風。
- old_vn (csv3): Mọi người đều mỉm cười chuẩn bị cho buổi chào mừng.\nTôi dần cảm nhận được, đây chính là Đường sắt Ohito.
- fix: Mọi người đều mỉm cười chuẩn bị cho buổi chào mừng.\nTôi dần cảm nhận được, đây chính là Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3053 — item T2 (JP: 御一夜鉄道)

- JP: １００年稼働した\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の経験ならば、\nきっと御一夜鉄道にも、素晴らしいものを伝えてくれよう。
- TW: 她作為\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;工作了上百年，一定能用她豐富的經驗為御一夜鐵路帶來諸多裨益。
- old_vn (csv3): Kinh nghiệm của một \x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động 100 năm,\nchắc chắn sẽ mang lại những điều tuyệt vời cho Đường sắt Ohito.
- fix: Kinh nghiệm của một \x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động 100 năm,\nchắc chắn sẽ mang lại những điều tuyệt vời cho Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3069 — item T2 (JP: 御一夜鉄道)

- JP: 異論や疑問があるのなら、率直にぶつけてかまわない。\nそれが許されるのが、御一夜鉄道の長所なのだから。
- TW: 如果有異議或者疑問，大可直言不諱。這正是御一夜鐵路的優點之一。
- old_vn (csv3): Nếu có ý kiến phản đối hay thắc mắc gì, cứ thẳng thắn bày tỏ.\nBởi vì được phép làm vậy chính là điểm mạnh của Đường sắt Ohito mà.
- fix: Nếu có ý kiến phản đối hay thắc mắc gì, cứ thẳng thắn bày tỏ.\nBởi vì được phép làm vậy chính là điểm mạnh của Đường sắt Ohitoyo mà.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3129 — item T1+T2 (JP: 御一夜鉄道)

- JP: 夜は1927御一夜温泉着で運転終了となる御一夜鉄道だが、\n朝練へ向う学園生を運ぶため、始発は早く0527だ。
- TW: 御一夜鐵路在晚上１９２７抵達溫泉站後就會結業，但因參加社團晨練的學生要搭車，所以首班車較早，在０５２７發車。
- old_vn (csv3): Đường sắt Ohito kết thúc chuyến chạy lúc 19:27 khi đến Suối nước nóng Ohito vào buổi tối,\nnhưng để chở học sinh đi tập luyện buổi sáng, chuyến đầu tiên xuất phát rất sớm lúc 05:27.
- fix: Đường sắt Ohitoyo kết thúc chuyến chạy lúc 19:27 khi đến Suối nước nóng Ohitoyo vào buổi tối,\nnhưng để chở học sinh đi tập luyện buổi sáng, chuyến đầu tiên xuất phát rất sớm lúc 05:27.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3166 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道の“らしさ”をできるかぎりに展開し、\nⅨ号機関車と\x%lレイルロオド;#00ffc040;レイルロオド%l;#;とを、暖かに楽しく迎えたい。
- TW: 我想儘可能以完整的御一夜鐵路“風格”，迎接九號機車及其\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，給對方帶來一些溫暖與喜悅。
- old_vn (csv3): Phát huy hết mức có thể "chất" riêng của Đường sắt Ohito,\nđể chào đón Đầu máy số 9 và \x%lレイルロオド;#00ffc040;Railord%l;#; một cách ấm áp và vui vẻ.
- fix: Phát huy hết mức có thể "chất" riêng của Đường sắt Ohitoyo,\nđể chào đón Đầu máy số 9 và \x%lレイルロオド;#00ffc040;Railord%l;#; một cách ấm áp và vui vẻ.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3179 — item T2 (JP: 御一夜鉄道)

- JP: みかん鉄道という鉄道会社がいかに信頼を、\n御一夜鉄道との繋がりを大事にしているかも伝わってくる。
- TW: 我深感橙鐵路公司對我們御一夜鐵路寄予了何等的信任，以及他們有多珍惜彼此之間這份情誼。
- old_vn (csv3): Điều đó cũng cho thấy công ty Đường sắt Mikan coi trọng sự tin tưởng,\nvà mối liên kết với Đường sắt Ohito đến mức nào.
- fix: Điều đó cũng cho thấy công ty Đường sắt Mikan coi trọng sự tin tưởng,\nvà mối liên kết với Đường sắt Ohitoyo đến mức nào.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3378 — item T1 (JP: 御一夜)

- JP: Ⅸ号機関車の、御一夜温泉駅への初入線の瞬間の写真。\nプレゼントにも、広報素材としても使えよう。
- TW: 記錄九號機車初次在御一夜溫泉站進站瞬間的照片，不管作為禮物還是宣傳材料都非常合適。
- old_vn (csv3): Bức ảnh chụp khoảnh khắc Đầu máy số 9 lần đầu tiên tiến vào Ga Suối nước nóng Ohito.\nCó thể dùng làm quà tặng, hoặc làm tư liệu quảng bá cũng được.
- fix: Bức ảnh chụp khoảnh khắc Đầu máy số 9 lần đầu tiên tiến vào Ga Suối nước nóng Ohitoyo.\nCó thể dùng làm quà tặng, hoặc làm tư liệu quảng bá cũng được.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3405 — item T2 (JP: 御一夜鉄道)

- JP: となれば、御一夜鉄道側のリスクはかなり小さくできる。
- TW: 這樣一來，御一夜鐵路要承擔的風險就很小了。
- old_vn (csv3): Nếu vậy, rủi ro phía Đường sắt Ohito sẽ được giảm thiểu đáng kể.
- fix: Nếu vậy, rủi ro phía Đường sắt Ohitoyo sẽ được giảm thiểu đáng kể.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3426 — item T1 (JP: 御一夜)

- JP: れいなの笑顔がムードを作る。\nあたたかく、にぎやかで、御一夜らしい優しい空気を。
- TW: 隨著玲奈的笑容，溫暖、熱鬧、充滿御一夜特色的溫馨氛圍洋溢在這鐵路商店裡。
- old_vn (csv3): Nụ cười của Reina tạo nên bầu không khí.\nMột bầu không khí ấm áp, náo nhiệt, dịu dàng đậm chất Ohito.
- fix: Nụ cười của Reina tạo nên bầu không khí.\nMột bầu không khí ấm áp, náo nhiệt, dịu dàng đậm chất Ohitoyo.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3439 — item T1 (JP: 御一夜)

- JP: まずは凪、ふかみたちによる歓迎パネル\n『ようこそ！　蒸気のふるさと御一夜へ』――間違いない。
- TW: 首先是凪和深美製作的歡迎板“歡迎來到蒸汽之鄉御一夜”——沒有問題。
- old_vn (csv3): Đầu tiên là tấm bảng chào mừng của Nagi và Fukami\n『Chào mừng! Đến với quê hương hơi nước Ohito』——Không có vấn đề gì.
- fix: Đầu tiên là tấm bảng chào mừng của Nagi và Fukami\n『Chào mừng! Đến với quê hương hơi nước Ohitoyo』——Không có vấn đề gì.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク04_小畑越え.txt.toml` (11 dòng)

### key 1477 — item T2 (JP: 御一夜鉄道)

- JP: 「……御一夜鉄道職員としての、出張扱いでもある。\n時間は、極力有意義に使い倒さねばならんな」
- TW: 「……這次也算是作為御一夜鐵路員工的一次出差。難得的機會當然要儘可能善加利用」
- old_vn (csv3): 「……Đây cũng được coi là một chuyến công tác với tư cách là nhân viên của Đường sắt Ohito.\nChúng ta phải tận dụng thời gian một cách có ý nghĩa nhất có thể.」
- fix: 「……Đây cũng được coi là một chuyến công tác với tư cách là nhân viên của Đường sắt Ohitoyo.\nChúng ta phải tận dụng thời gian một cách có ý nghĩa nhất có thể.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1823 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜では、お世話になりました。\n御一夜鉄道[ハチロクニイマル,3]8620号\x%l機関士;#00ffc040;機関士%l;#;。右田双鉄です」
- TW: 「之前在御一夜勞煩您了，我是御一夜鐵路８６２０號\x%l機関士;#00ffc040;司機%l;#;，名叫右田雙鐵」
- old_vn (audit): 「Ở Ohitoyo đã làm phiền anh rồi.\nTôi là \x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohito. Migita Soutetsu.」
- fix: 「Ở Ohitoyo đã làm phiền anh rồi.\nTôi là \x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohitoyo. Migita Soutetsu.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1902 — item T2 (JP: 御一夜鉄道)

- JP: 「お会いできて光栄です。しかし、僕らが\n御一夜鉄道の者だと、よくおわかりになられましたね」
- TW: 「勞您接待不勝榮幸，但是沒想到您竟能一眼認出我們」
- old_vn (csv3): 「Rất hân hạnh được gặp ông. Nhưng mà, sao ông biết\nchúng tôi là người của Đường sắt Ohito hay vậy?」
- fix: 「Rất hân hạnh được gặp ông. Nhưng mà, sao ông biết\nchúng tôi là người của Đường sắt Ohitoyo hay vậy?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1973 — item T2 (JP: 御一夜鉄道)

- JP: 「ああ、あなた方が御一夜鉄道の」
- TW: 「哦，二位便是御一夜鐵路的——」
- old_vn (csv3): 「À, các vị là người của Đường sắt Ohito đúng không.」
- fix: 「À, các vị là người của Đường sắt Ohitoyo đúng không.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2112 — item T2 (JP: 御一夜鉄道)

- JP: 「そうか。ポーレットには帝鉄勤務の経験が無い。\nゆえ、御一夜鉄道はその文化圏の外にあるのか」
- TW: 「對啊，波萊特沒有在帝國鐵路工作的經驗，所以御一夜鐵路就沒有受到其文化的薰陶」
- old_vn (audit): 「Ra vậy. Paulette không có kinh nghiệm làm việc ở Teitetsu.\nDo đó, Đường sắt Ohito nằm ngoài vòng văn hóa đó sao.」
- fix: 「Ra vậy. Paulette không có kinh nghiệm làm việc ở Teitetsu.\nDo đó, Đường sắt Ohitoyo nằm ngoài vòng văn hóa đó sao.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2121 — item T2 (JP: 御一夜鉄道)

- JP: 「みかん鉄道と御一夜鉄道がつながったように、\nレールは必ず、再び広くつながっていきますよ」
- TW: 「就如橙鐵路和御一夜鐵路能夠建立聯繫一樣，鐵路一定會再次遍布我們日本的大地」
- old_vn (csv3): 「Giống như Đường sắt Mikan và Đường sắt Ohito đã kết nối với nhau,\nđường ray nhất định sẽ lại được kết nối rộng khắp một lần nữa.」
- fix: 「Giống như Đường sắt Mikan và Đường sắt Ohitoyo đã kết nối với nhau,\nđường ray nhất định sẽ lại được kết nối rộng khắp một lần nữa.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2181 — item T2 (JP: 御一夜鉄道)

- JP: 「率直に申しますと、そのとおりです。ですので今日は、\n御一夜鉄道への譲渡前の状況などをお伺いできればと」
- TW: 「恕我直言，您的判斷一語中的。所以今天我們就是前來了解她在來到御一夜鐵路之前的各種情況」
- old_vn (csv3): 「Nói thẳng ra thì đúng là vậy. Do đó hôm nay,\nchúng tôi muốn hỏi thăm về tình hình của cô ấy trước khi chuyển nhượng cho Đường sắt Ohito.」
- fix: 「Nói thẳng ra thì đúng là vậy. Do đó hôm nay,\nchúng tôi muốn hỏi thăm về tình hình của cô ấy trước khi chuyển nhượng cho Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2182 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道で働くように――ですか」
- TW: 「您就讓她立刻前往御一夜鐵路工作——是嗎」
- old_vn (csv3): 「Là đi làm việc ở Đường sắt Ohito――sao?」
- fix: 「Là đi làm việc ở Đường sắt Ohitoyo――sao?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2217 — item T2 (JP: 御一夜鉄道)

- JP: 「双鉄さまの\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の、ハチロク、と申します。\n御一夜鉄道[ハチロクニイマル,3]8620の、専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;でございます」
- TW: 「我叫八六，是雙鐵少爺的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，也是御一夜鐵路８６２０專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」
- old_vn (csv3): 「Em là Hachiroku, \x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu ạ.\nLà \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohito ạ.」
- fix: 「Em là Hachiroku, \x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu ạ.\nLà \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohitoyo ạ.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2234 — item T2 (JP: 御一夜鉄道)

- JP: 「[おひとよ,2]御一夜鉄道への譲渡の準備だと答えた。\nすると、アレは――」
- TW: 「我於是回答這是為了將它移交給御一夜鐵路而做的準備。然後——」
- old_vn (csv3): 「Tôi trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohito.\nThế là, nó――」
- fix: 「Tôi trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohitoyo.\nThế là, nó――」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2298 — item T2 (JP: 御一夜鉄道)

- JP: 「はい、そうです。御一夜鉄道運輸部長兼\x%l保線部長;#00ffc040;保線部長%l;#;兼\n[ハチロクニイマル,3]8620\x%l機関士;#00ffc040;機関士%l;#;の、右田双鉄ともうします」
- TW: 「是的，我叫右田雙鐵，是御一夜鐵路運輸部長兼\x%l保線部長;#00ffc040;巡線部長%l;#;，同時擔任８６２０的\x%l機関士;#00ffc040;司機%l;#;」
- old_vn (csv3): 「Vâng, đúng vậy. Tôi là Migita Soutetsu, Trưởng phòng Vận tải kiêm \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;,\nkiêm \x%l機関士;#00ffc040;lái tàu%l;#; của 8620 thuộc Đường sắt Ohito.」
- fix: 「Vâng, đúng vậy. Tôi là Migita Soutetsu, Trưởng phòng Vận tải kiêm \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;,\nkiêm \x%l機関士;#00ffc040;lái tàu%l;#; của 8620 thuộc Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク04_煙には煙を.txt.toml` (6 dòng)

### key 1855 — item T1 (JP: 御一夜)

- JP: 「煙で煙って――にぃに――兄さん、正気ですか？\n夏の御一夜の、しかもこの広さの室内ですよ？」
- TW: 「以煙——阿哥——哥哥，你是認真的嗎？現在御一夜可是夏天，而且車廂很狹窄啊」
- old_vn (audit): 「Khói trị khói á――anh hai――anh Soutetsu, anh tỉnh táo không đấy?\nMùa hè ở Ohito, mà lại trong căn phòng chật hẹp thế này cơ mà?」
- fix: 「Khói trị khói á――anh hai――anh Soutetsu, anh tỉnh táo không đấy?\nMùa hè ở Ohitoyo, mà lại trong căn phòng chật hẹp thế này cơ mà?」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1920 — item T1 (JP: 御一夜)

- JP: 「頑張らねばと――僕も思っていただけだ。\nまずは、観光振興のため、そして御一夜を守るため」
- TW: 「只是我也覺得自己要努力了。為了振興旅遊業，為了守護御一夜」
- old_vn (audit): 「Tôi cũng chỉ đang nghĩ――mình phải cố gắng thôi.\nTrước hết là vì chấn hưng du lịch, và vì bảo vệ Ohito.」
- fix: 「Tôi cũng chỉ đang nghĩ――mình phải cố gắng thôi.\nTrước hết là vì chấn hưng du lịch, và vì bảo vệ Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2073 — item T1 (JP: 御一夜)

- JP: 「そうばい！　御一夜の職人だけで、\n改装一式引き受けてお店ば綺麗にしたとよ」
- TW: 「對！御一夜的工匠承接了裝修工作，把店弄得漂漂亮亮的」
- old_vn (csv3): 「Đúng vậy nha! Chỉ toàn thợ mộc ở Ohito,\nnhận trọn gói sửa chữa làm cho quán đẹp lên đó.」
- fix: 「Đúng vậy nha! Chỉ toàn thợ mộc ở Ohitoyo,\nnhận trọn gói sửa chữa làm cho quán đẹp lên đó.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2105 — item T1 (JP: 御一夜)

- JP: 「御一夜の町ばにぎやかにして、\n川下りにもたくさんお客さん呼ぼーばい！」
- TW: 「御一夜變得熱鬧起來，漂流那邊也會有好多好多的客人來了！」
- old_vn (csv3): 「Làm cho thị trấn Ohito nhộn nhịp lên,\nrồi kéo thêm nhiều khách đi thuyền xuôi dòng nữa nha!」
- fix: 「Làm cho thị trấn Ohitoyo nhộn nhịp lên,\nrồi kéo thêm nhiều khách đi thuyền xuôi dòng nữa nha!」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2393 — item T1 (JP: 御一夜)

- JP: 「絶対、評判になるよね、この\x%l列車;#00ffc040;列車%l;#;。\nそれで、御一夜――またにぎやかな町になるよね」
- TW: 「這輛\x%l列車;#00ffc040;列車%l;#;絕對會大受好評的。而御一夜——也會變回以前一樣熱鬧的鎮子」
- old_vn (csv3): 「Chắc chắn \x%l列車;#00ffc040;chuyến tàu%l;#; này sẽ nổi tiếng lắm đây.\nRồi Ohito――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」
- fix: 「Chắc chắn \x%l列車;#00ffc040;chuyến tàu%l;#; này sẽ nổi tiếng lắm đây.\nRồi Ohitoyo――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2464 — item T1 (JP: 御一夜)

- JP: 「バーベキュー\x%l列車;#00ffc040;列車%l;#;の折り返し、[ゆのい,1]湯医の発船場から\n御一夜まで、川下り使う人も右肩上がりじゃないですか」
- TW: 「ＢＢＱ\x%l列車;#00ffc040;列車%l;#;折返的時候，選擇利用漂流從湯醫的發船場去御一夜的人不也越來越多了嗎」
- old_vn (csv3): 「Lúc \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yui\nđến Ohito cũng đang tăng lên đều đặn mà.」
- fix: 「Lúc \x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yui\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク05_レイルロオドたち.txt.toml` (16 dòng)

### key 2361 — item T1 (JP: 御一夜)

- JP: 「ただ、Ⅸ号が引いてきた\x%l客車;#00ffc040;客車%l;#;をそのまま\n御一夜－[はやと,1]早戸間に流用するのは、難しいそうです」
- TW: 「只不過，問題在於九號帶來的\x%l客車;#00ffc040;客運車廂%l;#;，如果保持原樣用在御一夜至隼人段的話怕是頗有困難」
- old_vn (csv3): 「Chỉ là, có vẻ khó mà sử dụng nguyên xi \x%l客車;#00ffc040;toa hành khách%l;#;\nmà Đầu máy số 9 kéo về cho tuyến Ohito - Hayato được.」
- fix: 「Chỉ là, có vẻ khó mà sử dụng nguyên xi \x%l客車;#00ffc040;toa hành khách%l;#;\nmà Đầu máy số 9 kéo về cho tuyến Ohitoyo - Hayato được.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2455 — item T2 (JP: 御一夜鉄道)

- JP: 「あー、それね。\nそれなんだけど、御一夜鉄道ってかわってるよねー」
- TW: 「啊，這個呀。要說這件事啊，你們御一夜鐵路好奇怪哦」
- old_vn (csv3): 「A, chuyện đó hả.\nVề chuyện đó ấy, Đường sắt Ohito lạ thật đấy~」
- fix: 「A, chuyện đó hả.\nVề chuyện đó ấy, Đường sắt Ohitoyo lạ thật đấy~」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2473 — item T1 (JP: 御一夜)

- JP: 「うむ。御一夜にはレイルロオド技師もいるし、\n術仙には車両工場もあるゆえ――」
- TW: 「嗯，因為御一夜這裡有鐵路人偶技工，術仙那邊還有車輛工廠——」
- old_vn (csv3): 「Ừm. Ở Ohito có cả kỹ sư Railord,\nvà ở Jutsusen cũng có nhà máy chế tạo toa xe nữa nên――」
- fix: 「Ừm. Ở Ohitoyo có cả kỹ sư Railord,\nvà ở Jutsusen cũng có nhà máy chế tạo toa xe nữa nên――」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2638 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道では\x%lレイルロオド;#00ffc040;レイルロオド%l;#;にも給与が支給される。\n[くまぎん,1]隈銀では、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の口座開設も受け付けてくれる」
- TW: 「御一夜鐵路會向\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;支付工資。隈元銀行也接受\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的開戶申請」
- old_vn (csv3): 「Ở Đường sắt Ohito, \x%lレイルロオド;#00ffc040;Railord%l;#; cũng được trả lương.\nNgân hàng Kumagin cũng chấp nhận mở tài khoản cho \x%lレイルロオド;#00ffc040;Railord%l;#; nữa.」
- fix: 「Ở Đường sắt Ohitoyo, \x%lレイルロオド;#00ffc040;Railord%l;#; cũng được trả lương.\nNgân hàng Kumagin cũng chấp nhận mở tài khoản cho \x%lレイルロオド;#00ffc040;Railord%l;#; nữa.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2640 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「オヒトヨ鉄道やっぱりヘン！\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;がお説教しちゃって、怒られないとか！」
- TW: 「御一夜鐵路果然奇怪！\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;教訓人竟然都不會生氣的！」
- old_vn (csv3): 「Đường sắt Ohito đúng là kỳ lạ mà!\n\x%lレイルロオド;#00ffc040;Railord%l;#; thuyết giáo mà không bị mắng gì cả!」
- fix: 「Đường sắt Ohitoyo đúng là kỳ lạ mà!\n\x%lレイルロオド;#00ffc040;Railord%l;#; thuyết giáo mà không bị mắng gì cả!」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2765 — item T1 (JP: 御一夜)

- JP: 「心得た。では、三週間後には僕達も、\n御一夜－早戸間の乗務につけるように習熟せねばな」
- TW: 「明白。那我們也得在三個星期內，把御一夜至隼人段熟悉到可以執行乘務任務才行」
- old_vn (csv3): 「Đã rõ. Vậy thì, 3 tuần nữa chúng ta cũng phải\nthành thạo để có thể đảm nhận tuyến Ohito - Hayato thôi.」
- fix: 「Đã rõ. Vậy thì, 3 tuần nữa chúng ta cũng phải\nthành thạo để có thể đảm nhận tuyến Ohitoyo - Hayato thôi.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2834 — item T2 (JP: 御一夜鉄道)

- JP: 「ポーレット様も、確かにそうおっしゃいましょうね。\n御一夜鉄道の社風の源は、ポーレット様ですから」
- TW: 「波萊特大人確實是會這樣說的。畢竟御一夜鐵路的社風都是受波萊特大人的薰陶而來」
- old_vn (csv3): 「Cô Paulette chắc chắn cũng sẽ nói vậy nhỉ.\nVì cội nguồn văn hóa của Đường sắt Ohito là từ cô Paulette mà.」
- fix: 「Cô Paulette chắc chắn cũng sẽ nói vậy nhỉ.\nVì cội nguồn văn hóa của Đường sắt Ohitoyo là từ cô Paulette mà.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2922 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「それに、線路歩けたのもよかったし！　楽しかったし！\nオヒトヨ鉄道に\x%l保線;#00ffc040;保線%l;#;の専門家いないのもわかったし」
- TW: 「而且沿線路走過一次很有收穫！當然也很開心！也了解到御一夜鐵路這裡沒有\x%l保線;#00ffc040;巡線%l;#;方面的專家」
- old_vn (csv3): 「Với lại, được đi bộ trên đường ray cũng thích lắm! Vui lắm luôn!\nCũng biết được là Đường sắt Ohito không có chuyên gia \x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa.」
- fix: 「Với lại, được đi bộ trên đường ray cũng thích lắm! Vui lắm luôn!\nCũng biết được là Đường sắt Ohitoyo không có chuyên gia \x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa.」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2941 — item T1 (JP: 御一夜)

- JP: 「そういえば、オリヴィは言っていたな。\n『御一夜には\x%l保線;#00ffc040;保線%l;#;の専門家がいない』と」
- TW: 「話說回來，奧莉薇倒是的確說過，“御一夜鐵路這裡沒有\x%l保線;#00ffc040;巡線%l;#;方面的專家”」
- old_vn (csv3): 「Nhắc mới nhớ, Olivy từng nói.\n'Ở Ohito không có chuyên gia \x%l保線;#00ffc040;bảo trì đường ray%l;#;'.」
- fix: 「Nhắc mới nhớ, Olivy từng nói.\n'Ở Ohitoyo không có chuyên gia \x%l保線;#00ffc040;bảo trì đường ray%l;#;'.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2960 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道の一員として、御一夜鉄道のまいてつとして、\nポーレットだけがその決断の責を負うべきとは思わん」
- TW: 「身為御一夜鐵路的一員，同時也是御一夜鐵路的掌車人，我不認為應該讓你一個人為這個決定負責」
- old_vn (audit): 「Với tư cách là một thành viên của Đường sắt Ohito, là chủ tàu của Đường sắt Ohito,\nanh không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」
- fix: 「Với tư cách là một thành viên của Đường sắt Ohitoyo, là chủ tàu của Đường sắt Ohitoyo,\nanh không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3003 — item T1 (JP: 御一夜)

- JP: 「それってわたし、凄いことだと思います。\nその強さが、御一夜を守ってくれたって、思ってます」
- TW: 「這一點真的是讓我很欽佩。我想就是多虧了你們的堅強，才能將御一夜守護至今」
- old_vn (csv3): 「Tôi nghĩ điều đó thật sự rất tuyệt vời.\nTôi tin chính sức mạnh đó đã bảo vệ Ohito.」
- fix: 「Tôi nghĩ điều đó thật sự rất tuyệt vời.\nTôi tin chính sức mạnh đó đã bảo vệ Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3461 — item T2 (JP: 御一夜鉄道)

- JP: オリヴィが来るまでの時間に、\n御一夜鉄道でも求人をかける計画はあった。
- TW: 在奧莉薇來之前，御一夜鐵路其實也在規劃著進行招聘。
- old_vn (csv3): Trong khoảng thời gian chờ Olivy đến,\nĐường sắt Ohito cũng đã có kế hoạch tuyển dụng.
- fix: Trong khoảng thời gian chờ Olivy đến,\nĐường sắt Ohitoyo cũng đã có kế hoạch tuyển dụng.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3555 — item T1 (JP: 御一夜)

- JP: ……御一夜の観光復権は、確かに周辺と比してしまえば\n遅れ気味。とはいえ、実際は極めて堅調だ。
- TW: 御一夜旅遊業的復興與周邊地區相比確實是稍顯落後。但與以往相比，其實還是有了長足的進步。
- old_vn (csv3): ……Sự phục hưng du lịch của Ohito, quả thực nếu so với các khu vực xung quanh\nthì có vẻ hơi chậm. Tuy nhiên, thực tế lại vô cùng vững chắc.
- fix: ……Sự phục hưng du lịch của Ohitoyo, quả thực nếu so với các khu vực xung quanh\nthì có vẻ hơi chậm. Tuy nhiên, thực tế lại vô cùng vững chắc.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3706 — item T1 (JP: 御一夜)

- JP: ふかみはまだまだ若い上、完全に御一夜密着だ。\n無論、クマ川下りとの兼務にはなろうが……
- TW: 深美不光年紀尚輕，還對御一夜了如指掌。當然，隈河漂流那邊也需要她兼顧。不過……
- old_vn (csv3): Fukami vẫn còn rất trẻ, lại hoàn toàn gắn bó với Ohito.\nTất nhiên là sẽ phải kiêm nhiệm cả việc chèo thuyền xuôi dòng sông Kuma……
- fix: Fukami vẫn còn rất trẻ, lại hoàn toàn gắn bó với Ohitoyo.\nTất nhiên là sẽ phải kiêm nhiệm cả việc chèo thuyền xuôi dòng sông Kuma……
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3743 — item T2 (JP: 御一夜鉄道)

- JP: そうするだけで、御一夜鉄道の\x%l保線;#00ffc040;保線%l;#;レベルは、\n格段に跳ね上がっていたことだろう。
- TW: 相信有了這些新知識的補充，御一夜鐵路的\x%l保線;#00ffc040;巡線%l;#;水準就能上一個大台階。
- old_vn (csv3): Chỉ cần làm vậy, trình độ \x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohito\nchắc chắn sẽ tăng vọt lên một tầm cao mới.
- fix: Chỉ cần làm vậy, trình độ \x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohitoyo\nchắc chắn sẽ tăng vọt lên một tầm cao mới.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3790 — item T1+T2 (JP: 御一夜鉄道)

- JP: そこを踏まえても、将来的な御一夜鉄道――というか、\n御一夜を支える柱のひとつに、育っていってくれそうだ。
- TW: 若能處理好這個問題，將來的發展大有可期。說不定會成為御一夜鐵路——或者說整個御一夜的頂樑柱之一。
- old_vn (csv3): Dù vậy, em ấy có vẻ sẽ trưởng thành và trở thành một trong những trụ cột\ncủa Đường sắt Ohito trong tương lai――hay nói đúng hơn là của Ohito.
- fix: Dù vậy, em ấy có vẻ sẽ trưởng thành và trở thành một trong những trụ cột\ncủa Đường sắt Ohitoyo trong tương lai――hay nói đúng hơn là của Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク08_教導.txt.toml` (10 dòng)

### key 1384 — item T1 (JP: 御一夜)

- JP: 「……御一夜を助けたいという願いは、\n御一夜を愛する全員に、間違いなく共通したものだった」
- TW: 「……想要拯救御一夜，這毫無疑問是所有深愛御一夜的人們共同的願望」
- old_vn (csv3): 「……Mong muốn giúp đỡ Ohito,\nchắc chắn là điểm chung của tất cả những ai yêu mến Ohito.」
- fix: 「……Mong muốn giúp đỡ Ohitoyo,\nchắc chắn là điểm chung của tất cả những ai yêu mến Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2031 — item T1 (JP: 御一夜)

- JP: 「\x%l石造機関庫;#00ffc040;石造機関庫%l;#;まわりを含めて御一夜に七つ。\n旧麻霧駅――麻霧信号所に三つで、合計十だ」
- TW: 「包含\x%l石造機関庫;#00ffc040;石製機車庫%l;#;周邊的話，御一夜共有七個，再加上前麻霧站——麻霧信號站那裡有三個，合計十個轉轍器」
- old_vn (csv3): 「Bao gồm cả khu vực quanh \x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; thì ở Ohito có 7 cái.\nỞ ga cũ Makiri—— trạm tín hiệu Makiri có 3 cái, tổng cộng là 10.」
- fix: 「Bao gồm cả khu vực quanh \x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; thì ở Ohitoyo có 7 cái.\nỞ ga cũ Makiri—— trạm tín hiệu Makiri có 3 cái, tổng cộng là 10.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2091 — item T1 (JP: 御一夜)

- JP: 「あれ？　あわわっ――\n一番最初が御一夜ば出て、踏切こえてすぐにあって」
- TW: 「咦？啊哇哇——記得從御一夜站出發，剛過道口就有一座」
- old_vn (csv3): 「Ủa? Awa wa——\nCái đầu tiên là ngay sau khi ra khỏi Ohito, qua khỏi đoạn giao cắt đường sắt là có liền.」
- fix: 「Ủa? Awa wa——\nCái đầu tiên là ngay sau khi ra khỏi Ohitoyo, qua khỏi đoạn giao cắt đường sắt là có liền.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2327 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「だよー！　それに、\nオヒトヨ鉄道、もっと線路伸ばすんでしょ？」
- TW: 「對呀！再說了，御一夜鐵路也準備延長線路對吧？」
- old_vn (csv3): 「Đúng đó! Hơn nữa,\nĐường sắt Ohito còn định kéo dài đường ray thêm nữa mà đúng không?」
- fix: 「Đúng đó! Hơn nữa,\nĐường sắt Ohitoyo còn định kéo dài đường ray thêm nữa mà đúng không?」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2328 — item T1 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「だよ！　だって、　オリヴィが話をきいたハンイでは、\nみんなすっごくよろこんでた！　オヒトヨのおかげって」
- TW: 「對呀！畢竟以奧莉薇所知，大家可都非常高興的！都說是御一夜的功勞！」
- old_vn (csv3): 「Đúng vậy! Bởi vì, theo những gì Olivy nghe được,\nmọi người đều rất vui mừng! Họ bảo là nhờ có Ohito đó.」
- fix: 「Đúng vậy! Bởi vì, theo những gì Olivy nghe được,\nmọi người đều rất vui mừng! Họ bảo là nhờ có Ohitoyo đó.」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2651 — item T1 (JP: 御一夜)

- JP: 「エアクラ工場そのものが悪物ってわけじゃなかけんね、\n御一夜とあわんかったってだけで」
- TW: 「空凝機工廠自身沒有過錯，只是不適合咱們御一夜」
- old_vn (csv3): 「Bản thân nhà máy Aircra đâu phải là thứ xấu xa gì,\nchỉ là không hợp với Ohito thôi.」
- fix: 「Bản thân nhà máy Aircra đâu phải là thứ xấu xa gì,\nchỉ là không hợp với Ohitoyo thôi.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2826 — item T2 (JP: 御一夜鉄道)

- JP: 「したら、御一夜鉄道はこーじゅんかん！\nできとるばいね！　やけん、線路ものびたとばい！！」
- TW: 「那麼御一夜鐵路已經算是個良性循環嘞！所以才能延長線路！！」
- old_vn (csv3): 「Thế thì, Đường sắt Ohito đang có vòng tuần hoàn tốt!\nĐúng không! Vì vậy nên đường ray mới được kéo dài ra!!」
- fix: 「Thế thì, Đường sắt Ohitoyo đang có vòng tuần hoàn tốt!\nĐúng không! Vì vậy nên đường ray mới được kéo dài ra!!」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2828 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「このグループは、オヒトヨ鉄道ユノイ線の\n保線知識があるグループでしょ？　だから、Bグループ」
- TW: 「那麼這一組就是對御一夜鐵路湯醫線的巡線有經驗心得的人沒錯吧？就叫Ｂ組」
- old_vn (csv3): 「Nhóm này, là nhóm có kiến thức bảo trì đường ray\ncủa tuyến Yui thuộc Đường sắt Ohito đúng không? Vậy nên, là nhóm B.」
- fix: 「Nhóm này, là nhóm có kiến thức bảo trì đường ray\ncủa tuyến Yui thuộc Đường sắt Ohitoyo đúng không? Vậy nên, là nhóm B.」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2868 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「オケー！　そしたらいくよ～！　保線クイズ、第一問！『オヒトヨ鉄道ユノイ線にあるトンネルの数は』」
- TW: 「ＯＫ！那麼就開始提問～！巡線競猜第一題！“御一夜鐵路湯醫線一共有多少隧道？”」
- old_vn (csv3): 「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yui của Đường sắt Ohito là bao nhiêu?』」
- fix: 「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yui của Đường sắt Ohitoyo là bao nhiêu?』」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3358 — item T1 (JP: 御一夜)

- JP: 御一夜にはマッチしなかった一つの要素が、\nけれども千内においては、機能し、地域に貢献している。
- TW: 空凝機這個並不適合御一夜的技術，卻能在川內大顯身手，為當地做出貢獻。
- old_vn (csv3): Một yếu tố không phù hợp với Ohito,\nnhưng ở Sendai, nó lại phát huy tác dụng và cống hiến cho khu vực.
- fix: Một yếu tố không phù hợp với Ohitoyo,\nnhưng ở Sendai, nó lại phát huy tác dụng và cống hiến cho khu vực.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク11_御一夜鉄道小畑線.txt.toml` (2 dòng)

### key 2121 — item T2 (JP: 御一夜鉄道)

- JP: 「凍結からの復活時、仮に僕らが寿命を迎えていたとて。\n右田の家や御一夜鉄道が、必ずオリヴィを歓迎しように」
- TW: 「而等奧莉薇從封存中醒來時，即便我們已不在此世，右田家和御一夜鐵路也仍舊會歡迎她的」
- old_vn (csv3): 「Giả sử khi tỉnh dậy từ trạng thái đóng băng, chúng ta đã đi đến cuối cuộc đời. \nThì nhà Migita và Đường sắt Ohito chắc chắn vẫn sẽ dang rộng vòng tay chào đón Olivy.」
- fix: 「Giả sử khi tỉnh dậy từ trạng thái đóng băng, chúng ta đã đi đến cuối cuộc đời. \nThì nhà Migita và Đường sắt Ohitoyo chắc chắn vẫn sẽ dang rộng vòng tay chào đón Olivy.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2446 — item T2 (JP: 御一夜鉄道)

- JP: そうしなければ、御一夜鉄道が存続の危機に陥る――\nこれは恐らく、そういう事態と思うから。
- TW: 以如今的事態看來，我恐怕——御一夜鐵路或會陷入一場生死存亡的危機。
- old_vn (csv3): Nếu không làm vậy, Đường sắt Ohito sẽ rơi vào nguy cơ sống còn—— \nBởi vì tôi nghĩ, có lẽ đây chính là một tình huống như vậy.
- fix: Nếu không làm vậy, Đường sắt Ohitoyo sẽ rơi vào nguy cơ sống còn—— \nBởi vì tôi nghĩ, có lẽ đây chính là một tình huống như vậy.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク12_ムナカタ来訪.txt.toml` (12 dòng)

### key 1590 — item T2 (JP: 御一夜鉄道)

- JP: 「保線専門会社の計画が頓挫した場合は、御一夜鉄道嘱託\nで\x%l保線;#00ffc040;保線%l;#;も見て頂きたいので、ほぼフル勤務となりまして」
- TW: 「假如成立專業巡線公司的企劃夭折，我們還需要委託您負責御一夜鐵路的\x%l保線;#00ffc040;巡線%l;#;事務，待遇與全職員工基本相同」
- old_vn (csv3): 「Trong trường hợp kế hoạch thành lập công ty chuyên bảo trì đường ray bị đổ bể, chúng cháu cũng muốn nhờ chú \nquản lý cả phần \x%l保線;#00ffc040;bảo trì đường ray%l;#; với tư cách là nhân viên hợp đồng của Đường sắt Ohito, nên gần như sẽ là làm việc toàn thời gian ạ」
- fix: 「Trong trường hợp kế hoạch thành lập công ty chuyên bảo trì đường ray bị đổ bể, chúng cháu cũng muốn nhờ chú \nquản lý cả phần \x%l保線;#00ffc040;bảo trì đường ray%l;#; với tư cách là nhân viên hợp đồng của Đường sắt Ohitoyo, nên gần như sẽ là làm việc toàn thời gian ạ」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1626 — item T2 (JP: 御一夜鉄道)

- JP: 「他方、指導を主体とした嘱託としての御一夜鉄道への\n勤務については、ぜひお願いできれば、と考えています」
- TW: 「另外，我們還是希望聘請您為我們御一夜鐵路的合同工，主要負責指導等工作」
- old_vn (csv3): 「Mặt khác, về việc làm nhân viên hợp đồng tại Đường sắt Ohito với nhiệm vụ chính là hướng dẫn, \nchúng cháu rất mong chú có thể nhận lời.」
- fix: 「Mặt khác, về việc làm nhân viên hợp đồng tại Đường sắt Ohitoyo với nhiệm vụ chính là hướng dẫn, \nchúng cháu rất mong chú có thể nhận lời.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1746 — item T2 (JP: 御一夜鉄道)

- JP: 「うふふぅ、御一夜鉄道へようこそですよぉ」
- TW: 「嘻嘻，歡迎來到御一夜鐵路」
- old_vn (csv3): 「U hu hu, chào mừng chú đến với Đường sắt Ohito nha~」
- fix: 「U hu hu, chào mừng chú đến với Đường sắt Ohitoyo nha~」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1760 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道は、オリヴィの蓄積してきた知識を\n積極的に活用したいと考えていますので」
- TW: 「因為我們御一夜鐵路，打算積極運用奧莉薇積攢至今的豐富知識」
- old_vn (csv3): 「Đường sắt Ohito muốn tích cực tận dụng \nnhững kiến thức mà Olivy đã tích lũy được.」
- fix: 「Đường sắt Ohitoyo muốn tích cực tận dụng \nnhững kiến thức mà Olivy đã tích lũy được.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2058 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「[おんてつ,1]御鉄さんで、よくしてもらっているようだな」
- TW: 「看來你在御鐵這邊過得很好」
- old_vn (csv3): 「Ở Đường sắt Ohito, có vẻ cháu được đối xử rất tốt nhỉ.」
- fix: 「Ở Đường sắt Ohitoyo, có vẻ cháu được đối xử rất tốt nhỉ.」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2104 — item T2 (JP: 御一夜鉄道)

- JP: 「同時に\x%l機関士;#00ffc040;機関士%l;#;・\x%l機関助士;#00ffc040;機関助士%l;#;の指導を主務とした御一夜鉄道\n[しょくたく,1]嘱託職員としても勤務して貰えればと思っています」
- TW: 「與之同時，我們也希望能夠委託您成為我們御一夜鐵路的合同工，主要負責指導\x%l機関士;#00ffc040;司機%l;#;以及\x%l機関助士;#00ffc040;司爐%l;#;」
- old_vn (csv3): 「Đồng thời, chúng cháu cũng hy vọng chú có thể làm việc như một nhân viên \x%l嘱託;#00ffc040;hợp đồng%l;#; của Đường sắt Ohito, \nvới nhiệm vụ chính là hướng dẫn \x%l機関士;#00ffc040;lái tàu%l;#; và \x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」
- fix: 「Đồng thời, chúng cháu cũng hy vọng chú có thể làm việc như một nhân viên \x%l嘱託;#00ffc040;hợp đồng%l;#; của Đường sắt Ohitoyo, \nvới nhiệm vụ chính là hướng dẫn \x%l機関士;#00ffc040;lái tàu%l;#; và \x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2224 — item T2 (JP: 御一夜鉄道)

- JP: 「でしたら当面、御一夜鉄道としては、\nどのように対処すればいいんでしょうか？」
- TW: 「那目前來說，我們御一夜鐵路又該作何措施？」
- old_vn (csv3): 「Nếu vậy thì trước mắt, Đường sắt Ohito, \nnên đối phó như thế nào ạ?」
- fix: 「Nếu vậy thì trước mắt, Đường sắt Ohitoyo, \nnên đối phó như thế nào ạ?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2233 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「なら一つだけ。あの隆起地点、お前も細かく見てほしい。\n何かあれば、[おんてつ,1]御鉄さんに報告すると同時に――」
- TW: 「那麼我就只拜託你一件事，那個發生隆起的地點，希望你也要仔細觀察，一旦出現情況，在向御鐵匯報的同時——」
- old_vn (csv3): 「Vậy thì nhờ nhóc một việc. Địa điểm phồng rộp đó, nhóc cũng hãy theo dõi sát sao nhé. \nNếu có gì bất thường, hãy báo cáo cho Đường sắt Ohito, đồng thời——」
- fix: 「Vậy thì nhờ nhóc một việc. Địa điểm phồng rộp đó, nhóc cũng hãy theo dõi sát sao nhé. \nNếu có gì bất thường, hãy báo cáo cho Đường sắt Ohitoyo, đồng thời——」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2477 — item T2 (JP: 御一夜鉄道)

- JP: 実際、御一夜鉄道では旺宮を使っていなかった。\n同様の小規模鉄道事業者も決して少なくはなかろう。
- TW: 之前我們御一夜鐵路也沒有和大宮建立合作關係，肯定也有很多小規模的鐵路運營商亦是如此。
- old_vn (csv3): Thực tế, Đường sắt Ohito đã không sử dụng Omiya. \nChắc chắn cũng có không ít các doanh nghiệp đường sắt quy mô nhỏ tương tự như vậy.
- fix: Thực tế, Đường sắt Ohitoyo đã không sử dụng Omiya. \nChắc chắn cũng có không ít các doanh nghiệp đường sắt quy mô nhỏ tương tự như vậy.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2554 — item T2 (JP: 御一夜鉄道)

- JP: ポーレットが軽々に報酬を弾み過ぎぬよう、ここだけは、\n銀行家でなく、御一夜鉄道経営顧問になってくれている。
- TW: 只有在商討這些問題時，她不會再保持銀行家的態度，而是作為御一夜鐵路的經營顧問為我們出謀劃策。
- old_vn (csv3): Để tránh việc Paulette đưa ra mức thù lao quá hời một cách dễ dãi, chỉ riêng điểm này, \ncô ấy không phải là nhân viên ngân hàng, mà đang đóng vai trò cố vấn quản lý của Đường sắt Ohito.
- fix: Để tránh việc Paulette đưa ra mức thù lao quá hời một cách dễ dãi, chỉ riêng điểm này, \ncô ấy không phải là nhân viên ngân hàng, mà đang đóng vai trò cố vấn quản lý của Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2565 — item T2 (JP: 御一夜鉄道)

- JP: が、宗方さんはれいなの言葉を――御一夜鉄道の文化を、\n少なくとも表面上は、気にせず受け入れてくれている。
- TW: 可是宗方先生對玲奈的發言——對我們御一夜鐵路的文化並沒有表現出排斥，至少表面上他是示以理解的。
- old_vn (audit): Nhưng, Munakata đã đón nhận lời nói của Reina——văn hóa của Đường sắt Ohito, ít nhất là ngoài mặt, mà không hề bận tâm.
- fix: Nhưng, Munakata đã đón nhận lời nói của Reina——văn hóa của Đường sắt Ohitoyo, ít nhất là ngoài mặt, mà không hề bận tâm.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2753 — item T2 (JP: 御一夜鉄道)

- JP: 新人を増員、育成していかねばならぬ\nこれからの御一夜鉄道に、これほど好適な人材も無かろう。
- TW: 對於今後必須不斷發展培養新人的御一夜鐵路而言，當然是不可或缺的人才。
- old_vn (csv3): Đối với Đường sắt Ohito trong tương lai, khi cần phải tuyển thêm và đào tạo nhân viên mới, \nkhông có nhân tài nào phù hợp hơn chú ấy.
- fix: Đối với Đường sắt Ohitoyo trong tương lai, khi cần phải tuyển thêm và đào tạo nhân viên mới, \nkhông có nhân tài nào phù hợp hơn chú ấy.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク13_実りの秋.txt.toml` (3 dòng)

### key 1694 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「そこまではしないよー！　オリヴィ、\nオヒトヨ鉄道を困らせたりしたくないし」
- TW: 「也不會到那個程度的啦！奧莉薇不想讓御一夜鐵路為難」
- old_vn (csv3): 「Không đến mức đó đâu~! Olivy,\nkhông muốn làm khó Đường sắt Ohito đâu.」
- fix: 「Không đến mức đó đâu~! Olivy,\nkhông muốn làm khó Đường sắt Ohitoyo đâu.」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1955 — item T1 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「オヒトヨとかハヤトで、\n『マッタクモッテ』、リューコーしてるの？」
- TW: 「御一夜和隼人那邊，最近很流行說“真真兒”嗎？」
- old_vn (csv3): 「Ở Ohito với Hayato,\ntừ 『hoàn toàn』 đang thịnh hành hả?」
- fix: 「Ở Ohitoyo với Hayato,\ntừ 『hoàn toàn』 đang thịnh hành hả?」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2535 — item T2 (JP: 御一夜鉄道)

- JP: とはいえ残念ながら、現在の御一夜鉄道には、\nこの地点を常時監視できるだけの、人的資金的余裕は無い。
- TW: 但是遺憾的是，對這裡進行二十四小時不間斷的監視，不管是人力還是資金，御一夜鐵路都是心有餘而力不足。
- old_vn (csv3): Tuy nhiên đáng tiếc là, Đường sắt Ohito hiện tại,\nkhông có đủ nhân lực và tài chính để giám sát liên tục địa điểm này.
- fix: Tuy nhiên đáng tiếc là, Đường sắt Ohitoyo hiện tại,\nkhông có đủ nhân lực và tài chính để giám sát liên tục địa điểm này.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク14_冬.txt.toml` (8 dòng)

### key 1780 — item T2 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「……最初ね？　オヒトヨ鉄道いけっていわれたとき。\nオリヴィ、捨てられたって思ったの」
- TW: 「……要說一開始，剛要奧莉薇去御一夜鐵路的時候，奧莉薇還以為自己是被拋棄了」
- old_vn (csv3): 「……Lúc đầu ấy? Khi bị bảo là đến Đường sắt Ohito.\nOlivy, đã nghĩ là mình bị vứt bỏ rồi.」
- fix: 「……Lúc đầu ấy? Khi bị bảo là đến Đường sắt Ohitoyo.\nOlivy, đã nghĩ là mình bị vứt bỏ rồi.」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2587 — item T2 (JP: 御一夜鉄道)

- JP: 「はい、御一夜鉄道です――\nえ？　あ、はい。繋いでください」
- TW: 「喂，這裡是御一夜鐵路——哎？啊，好的，請接過來」
- old_vn (csv3): 「Vâng, Đường sắt Ohito xin nghe——\nHả? À, vâng. Xin hãy nối máy.」
- fix: 「Vâng, Đường sắt Ohitoyo xin nghe——\nHả? À, vâng. Xin hãy nối máy.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2774 — item T1 (JP: 御一夜)

- JP: 「はい。情報はできるだけ密に共有できるようにと――\nその体制づくりも、御一夜市を入れてで進めます」
- TW: 「對，為了讓我們儘可能與對方互通情報，我會建議讓御一夜市也參與其中，共同探討如何建立防災體制」
- old_vn (csv3): 「Vâng. Để có thể chia sẻ thông tin một cách chặt chẽ nhất——\nviệc xây dựng hệ thống đó, tôi sẽ tiến hành cùng với thành phố Ohito.」
- fix: 「Vâng. Để có thể chia sẻ thông tin một cách chặt chẽ nhất——\nviệc xây dựng hệ thống đó, tôi sẽ tiến hành cùng với thành phố Ohitoyo.」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2918 — item T1 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「だよ？　だから。だからオリヴィ、オヒトヨに来て！\nオヒトヨに来れて、すごくよかったって思ってる！」
- TW: 「是呀，所以現在，奧莉薇真的好慶幸！慶幸自己能來到御一夜這裡！」
- old_vn (csv3): 「Đúng vậy đó? Thế nên. Thế nên Olivy, đến Ohito!\nTôi nghĩ thật tốt vì đã có thể đến Ohito!」
- fix: 「Đúng vậy đó? Thế nên. Thế nên Olivy, đến Ohitoyo!\nTôi nghĩ thật tốt vì đã có thể đến Ohitoyo!」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3680 — item T1 (JP: 御一夜)

- JP: 本当に皆、驚くほどに積極的に協力を申し出てくれた。\n御一夜の人たちだけでなく、湯医や術仙の人たちまでも。
- TW: 大家積極配合的態度完全超乎了我的想像，不止是御一夜，就連湯醫和術仙的民眾也都參與其中。
- old_vn (csv3): Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\nKhông chỉ người dân Ohito, mà cả người dân Yui và Jutsusen nữa.
- fix: Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\nKhông chỉ người dân Ohitoyo, mà cả người dân Yui và Jutsusen nữa.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3747 — item T2 (JP: 御一夜鉄道)

- JP: 丸山香織――ポーレットの厳しい選抜にようやく耐えて\n御一夜鉄道に加わった、新人の\x%l庫内手;#00ffc040;庫内手%l;#;・\x%l機関助士;#00ffc040;機関助士%l;#;見習いだ。
- TW: 她提到的丸山香織，是歷經波萊特嚴格挑選，進入御一夜鐵路的\x%l庫内手;#00ffc040;洗爐工%l;#;新人兼見習\x%l機関助士;#00ffc040;司爐%l;#;。
- old_vn (csv3): Maruyama Kaori——Người cuối cùng cũng vượt qua được cuộc tuyển chọn gắt gao của Paulette\nđể gia nhập Đường sắt Ohito, là một nhân viên \x%l庫内手;#00ffc040;rửa lò%l;#; kiêm \x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự mới.
- fix: Maruyama Kaori——Người cuối cùng cũng vượt qua được cuộc tuyển chọn gắt gao của Paulette\nđể gia nhập Đường sắt Ohitoyo, là một nhân viên \x%l庫内手;#00ffc040;rửa lò%l;#; kiêm \x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự mới.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 3843 — item T1 (JP: 御一夜)

- JP: ――シフトや何やの細部をみっちり打ち合わせ、\n流さんが御一夜へと帰っていく。
- TW: 我們具體討論了一下值班的安排及各種細節問題，然後流先生就出發返回御一夜了。
- old_vn (csv3): ——Sau khi bàn bạc kỹ lưỡng chi tiết về ca trực và các thứ khác,\nông Nagare lên đường trở về Ohito.
- fix: ——Sau khi bàn bạc kỹ lưỡng chi tiết về ca trực và các thứ khác,\nông Nagare lên đường trở về Ohitoyo.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 4147 — item T1 (JP: 御一夜)

- JP: （活動自体は出来ているのだし、休むべきを休ませて――\n不死鳥博士に、なんとか御一夜に運んでもらおう）
- TW: （畢竟她還有能力自由行動，只要注意休息——再讓不死鳥博士想辦法來御一夜一趟）
- old_vn (csv3): （Vẫn có thể tự hoạt động được, cứ để cô ấy nghỉ ngơi những lúc cần thiết——\nrồi nhờ Tiến sĩ Fushicho tìm cách đến Ohito.）
- fix: （Vẫn có thể tự hoạt động được, cứ để cô ấy nghỉ ngơi những lúc cần thiết——\nrồi nhờ Tiến sĩ Fushicho tìm cách đến Ohitoyo.）
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク14_橋.txt.toml` (1 dòng)

### key 2748 — item T2 (JP: 御一夜鉄道)

- JP: 稀咲の助力を得られるようになり、実際、\n御一夜鉄道株式会社の財務体質は大きく改善されている。
- TW: 自從得到稀咲的協助後，御一夜鐵路股份公司的財務體系到了極大的改善。
- old_vn (csv3): Nhờ có sự giúp đỡ của Kisaki, thực tế là,\ntình hình tài chính của Công ty Cổ phần Đường sắt Ohito đã được cải thiện đáng kể.
- fix: Nhờ có sự giúp đỡ của Kisaki, thực tế là,\ntình hình tài chính của Công ty Cổ phần Đường sắt Ohitoyo đã được cải thiện đáng kể.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク15a_痛みとの決別.txt.toml` (3 dòng)

### key 1997 — item T2 (JP: 御一夜鉄道)

- JP: 「はい。御一夜鉄道――あっ！　オリヴィちゃん！？\n双鉄くんね？　すぐかわり」
- TW: 「您好，這裡是御一夜鐵路——啊！奧莉薇！？讓雙鐵君接電話是吧？我馬上給他」
- old_vn (csv3): 「Vâng. Đường sắt Ohito xin nghe——Á! Olivy!?\nGặp anh Soutetsu hả? Chị chuyển máy ngay đây」
- fix: 「Vâng. Đường sắt Ohitoyo xin nghe——Á! Olivy!?\nGặp anh Soutetsu hả? Chị chuyển máy ngay đây」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2038 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「お前がどれほど\x%l保線;#00ffc040;保線%l;#;を真剣に学んでいたか。\nそれを的確に御鉄の皆さんに伝えてくれたかに、驚いた」
- TW: 「我驚訝於你竟然這麼認真地學習了\x%l保線;#00ffc040;巡線%l;#;知識，還準確地教給了御鐵的人」
- old_vn (csv3): 「Tôi bất ngờ vì cô đã học hỏi về \x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohito nữa chứ」
- fix: 「Tôi bất ngờ vì cô đã học hỏi về \x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohitoyo nữa chứ」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2116 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「ああ、そのとおりだ。御鉄さんから依頼を受けた。\n陥没の措置の監督と評価とをしてほしいと」
- TW: 「沒錯。我是御鐵請來的。他們希望我對塌陷應對措施進行監督和評估」
- old_vn (csv3): 「Ừ, đúng thế. Tôi nhận được yêu cầu từ Đường sắt Ohito.\nHọ muốn tôi giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」
- fix: 「Ừ, đúng thế. Tôi nhận được yêu cầu từ Đường sắt Ohitoyo.\nHọ muốn tôi giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク15b_さよなら列車.txt.toml` (6 dòng)

### key 1299 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「……御鉄さんの雛衣社長に聞いたんだが、\nテレビで流れたそうだ」
- TW: 「……御鐵的雛衣社長告訴我，你似乎上電視了啊」
- old_vn (csv3): 「……Nghe Giám đốc Hinai của Đường sắt Ohito nói,\nchuyện đó đã được phát trên tivi rồi đấy」
- fix: 「……Nghe Giám đốc Hinai của Đường sắt Ohitoyo nói,\nchuyện đó đã được phát trên tivi rồi đấy」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1512 — item T1 (JP: 御一夜)

- JP: 「それだけじゃなく、御一夜からも早戸からも、\nこれだけの人達が八ツ城にむかってくれるとはなぁ」
- TW: 「不光如此。從御一夜、隼人竟然有這麼多人要前往八代」
- old_vn (csv3): 「Không chỉ vậy, từ Ohito hay từ Hayato,\nlại có ngần này người hướng về Yatsushiro cơ đấy」
- fix: 「Không chỉ vậy, từ Ohitoyo hay từ Hayato,\nlại có ngần này người hướng về Yatsushiro cơ đấy」
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1637 — item T1 (JP: オヒトヨ (katakana của 御一夜))

- JP: 「オリヴィ、メリケンで――オヒトヨの、こ、だけど。\nだけど、ね？　ずっと、オリヴィ――ムナカタのこと」
- TW: 「奧莉薇——雖然，又是美國式——又是，御一夜的，鐵路人偶。可奧莉薇，一直認為，宗方就是——」
- old_vn (audit): 「Olivy, Meriken——là con của, Ohito, nhưng.\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」
- fix: 「Olivy, Meriken——là con của, Ohitoyo, nhưng.\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」
- Lý do: JP chứa オヒトヨ (katakana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1689 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道、\x%l車掌;#00ffc040;車掌%l;#;の早瀬です。あの――増結、\n[けいきゃくしゃ,2]軽客車を二両増結できるかって、駅長さんから」
- TW: 「我叫早瀨，是御一夜鐵路\x%l車掌;#00ffc040;列車長%l;#;。請問——站長問能不能加掛兩節輕型客車」
- old_vn (csv3): 「Tôi là Hayase, \x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohito. Dạ——Trưởng ga hỏi là,\ncó thể ghép thêm hai [けいきゃくしゃ,2]toa hành khách nhẹ nữa không ạ」
- fix: 「Tôi là Hayase, \x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohitoyo. Dạ——Trưởng ga hỏi là,\ncó thể ghép thêm hai [けいきゃくしゃ,2]toa hành khách nhẹ nữa không ạ」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1999 — item T1 (JP: 御一夜)

- JP: それでも少しも緩むことなく、みかん鉄道の\x%lC12;#00ffc040;C12%l;#;は、\n小畑線へと進入し、御一夜へ向け、屋岳の坂に挑んでいく。
- TW: 但橙鐵路的\x%lC12;#00ffc040;Ｃ１２%l;#;還是按時發車，進入了大畑線，朝著御一夜方向行駛，去挑戰矢岳的坡道。
- old_vn (csv3): Dù vậy, không hề chùn bước, chiếc \x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\ntiến vào tuyến Obata, hướng về Ohito, thách thức con dốc Yadake.
- fix: Dù vậy, không hề chùn bước, chiếc \x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\ntiến vào tuyến Obata, hướng về Ohitoyo, thách thức con dốc Yadake.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2143 — item T2 (JP: 御一夜鉄道)

- JP: 実際、僕とハチロクが、そうして御一夜鉄道が、\nどれほどオリヴィに助けられたか――
- TW: 實際上，我和八六還有御一夜鐵路也受了奧莉薇很多幫助——
- old_vn (csv3): Thực tế thì, tôi và Hachiroku, cũng như Đường sắt Ohito,\nđã được Olivy giúp đỡ biết bao nhiêu——
- fix: Thực tế thì, tôi và Hachiroku, cũng như Đường sắt Ohitoyo,\nđã được Olivy giúp đỡ biết bao nhiêu——
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 01_Hachiroku — `ハチロク16_春.txt.toml` (3 dòng)

### key 1221 — item T2 (JP: 御一夜鉄道)

- JP: ……僕ら、御一夜鉄道は、オリヴィから既に受け取った。\n宗方さんが教えてくれた大事なことを、幾つも幾つも。
- TW: ……我們御一夜鐵路已經從奧莉薇那裡學到了很多很多。那些都是宗方先生教給她，她再教給我們的。
- old_vn (csv3): ……Đường sắt Ohito chúng tôi, đã nhận được từ Olivy.\nRất nhiều, rất nhiều những điều quan trọng mà anh Munakata đã truyền dạy.
- fix: ……Đường sắt Ohitoyo chúng tôi, đã nhận được từ Olivy.\nRất nhiều, rất nhiều những điều quan trọng mà anh Munakata đã truyền dạy.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1884 — item T2 (JP: 御一夜鉄道)

- JP: 「おれはマスターではない。\nで、この人たちは、御一夜鉄道のみなさんだ」
- TW: 「我不是你的主人。他們是御一夜鐵路的人」
- old_vn (csv3): 「Tôi không phải là Master.\nVà, những người này là người của Đường sắt Ohito.」
- fix: 「Tôi không phải là Master.\nVà, những người này là người của Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2070 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「\x%l機関士;#00ffc040;機関士%l;#;の方は、教導を任されることになりました。\n御鉄さんから話をいただいていたおかげです」
- TW: 「那邊的\x%l機関士;#00ffc040;司機%l;#;也交給我來帶了。這都是多虧了御鐵這邊向我提出的邀請」
- old_vn (csv3): 「Về phần \x%l機関士;#00ffc040;lái tàu%l;#;, tôi đã được giao nhiệm vụ chỉ dạy.\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohito các cô cậu đấy.」
- fix: 「Về phần \x%l機関士;#00ffc040;lái tàu%l;#;, tôi đã được giao nhiệm vụ chỉ dạy.\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohitoyo các cô cậu đấy.」
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 02_Hibiki — `日々姫07_姉の想い。妹の想い.txt.toml` (2 dòng)

### key 1962 — item T2 (JP: 御一夜鉄道)

- JP: 「その条件で、御一夜鉄道として、引受先を探します。\n第一候補は、もちろん[くるだい,1]来大鉄道――文庫森機関庫で」
- TW: 「我會帶著這個條件，代表御一夜鐵路去尋找接收地。第一候選地自然是久大鐵路的豐後森機車庫」
- old_vn (csv3): 「Với điều kiện đó, Đường sắt Ohito sẽ tìm kiếm nơi tiếp nhận.\nỨng cử viên số một, dĩ nhiên là Đường sắt Kurudai——tại xưởng đầu máy Bungomori」
- fix: 「Với điều kiện đó, Đường sắt Ohitoyo sẽ tìm kiếm nơi tiếp nhận.\nỨng cử viên số một, dĩ nhiên là Đường sắt Kurudai——tại xưởng đầu máy Bungomori」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2840 — item T2 (JP: 御一夜鉄道)

- JP: 『御一夜鉄道の案件』に、御一夜鉄道の部外者の、\n意見を求め、判断基準にしようとするなら。
- TW: 畢竟她的意思是想向某個局外人徵求關於“御一夜鐵路的議案”的意見，並將這個意見視為判斷基準。
- old_vn (csv3): Bởi vì em ấy muốn lấy ý kiến của một người ngoài Đường sắt Ohito\nlàm tiêu chuẩn phán đoán cho 'dự án của Đường sắt Ohito'.
- fix: Bởi vì em ấy muốn lấy ý kiến của một người ngoài Đường sắt Ohitoyo\nlàm tiêu chuẩn phán đoán cho 'dự án của Đường sắt Ohitoyo'.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 02_Hibiki — `日々姫13_討論会.txt.toml` (1 dòng)

### key 1347 — item T2 (JP: 御一夜鉄道)

- JP: 「同じ、鉄道を愛する仲間ですから。\n御一夜鉄道のためにも、きっと力を貸してくれます」
- TW: 「大家都是愛著鐵路的同好，為了御一夜鐵路，他們一定會幫忙的」
- old_vn (csv3): 「Vì chúng tôi đều là những người bạn cùng yêu đường sắt mà.\nVì Đường sắt Ohito, chắc chắn họ sẽ cho chúng ta mượn sức mạnh.」
- fix: 「Vì chúng tôi đều là những người bạn cùng yêu đường sắt mà.\nVì Đường sắt Ohitoyo, chắc chắn họ sẽ cho chúng ta mượn sức mạnh.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 02_Hibiki — `日々姫16_夢を乗せて.txt.toml` (2 dòng)

### key 1994 — item T2 (JP: 御一夜鉄道)

- JP: 「稀咲が僕らの中に加わり、\n御一夜鉄道はさらなる飛躍を遂げつつある」
- TW: 「稀咲加入到我們之中，御一夜鐵路也正在完成更高的飛躍」
- old_vn (csv3): 「Kisaki gia nhập vào nhóm chúng ta, và Đường sắt Ohito đang dần đạt được những bước tiến xa hơn nữa.」
- fix: 「Kisaki gia nhập vào nhóm chúng ta, và Đường sắt Ohitoyo đang dần đạt được những bước tiến xa hơn nữa.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2107 — item T2 (JP: 御一夜鉄道)

- JP: 「御一夜鉄道に参加したいという\x%lまいてつ;#00ffc040;まいてつ%l;#;さんも\nいらっしゃるのに、今は受け入れ余地も無い」
- TW: 「雖然現在也有\x%lまいてつ;#00ffc040;掌車人%l;#;想要參加御一夜鐵路，可我們現在沒有接納他們的餘地」
- old_vn (audit): 「Dù có những \x%lまいてつ;#00ffc040;chủ tàu%l;#; muốn tham gia vào Đường sắt Ohito, nhưng hiện tại chúng ta cũng không còn chỗ để tiếp nhận nữa.」
- fix: 「Dù có những \x%lまいてつ;#00ffc040;chủ tàu%l;#; muốn tham gia vào Đường sắt Ohitoyo, nhưng hiện tại chúng ta cũng không còn chỗ để tiếp nhận nữa.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 03_Paulette — `ポーレット02_古地図.txt.toml` (1 dòng)

### key 2398 — item T1 (JP: 御一夜)

- JP: その上で、例えば掛け紙の裏にでも、\n“キジ馬と御一夜”的な説明文をつければ、なおよかろう。
- TW: 在封紙的背面印上“雉子馬和御一夜”的介紹，效果一定更好。
- old_vn (csv3): Hơn nữa, nếu in thêm một đoạn giải thích về 'Ngựa Kiji và Ohito'\nlên mặt sau của giấy gói cơm hộp thì càng tuyệt vời.
- fix: Hơn nữa, nếu in thêm một đoạn giải thích về 'Ngựa Kiji và Ohitoyo'\nlên mặt sau của giấy gói cơm hộp thì càng tuyệt vời.
- Lý do: JP chứa 御一夜; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 03_Paulette — `ポーレット03_大きなにもつのおばあさん.txt.toml` (5 dòng)

### key 1518 — item T2 (JP: 御一夜鉄道)

- JP: 「知らなくて当然ですよ。\n御一夜鉄道、特急ってまだ一本も走ってませんし」
- TW: 「你當然不知道了。畢竟御一夜鐵路連一個特前段班次都還沒有開行過呢」
- old_vn (csv3): 「Anh không biết là chuyện đương nhiên thôi.\nĐường sắt Ohito đã có chuyến tàu tốc hành nào chạy đâu.」
- fix: 「Anh không biết là chuyện đương nhiên thôi.\nĐường sắt Ohitoyo đã có chuyến tàu tốc hành nào chạy đâu.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 1750 — item T2 (JP: 御一夜鉄道)

- JP: 「すごいホワイト！　御一夜鉄道も見習わなくちゃ」
- TW: 「好棒的企業福利！我們御一夜鐵路也要向他們學習」
- old_vn (audit): 「Phúc lợi tốt quá đi! Đường sắt Ohito cũng phải học theo mới được.」
- fix: 「Phúc lợi tốt quá đi! Đường sắt Ohitoyo cũng phải học theo mới được.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2010 — item T2 (JP: 御一夜鉄道)

- JP: 「あの……ひかりが、『きっぷのルールおしえて』って。\nそれでちょっと、御一夜鉄道株式会社[りょかく,1]旅客営業規則とか」
- TW: 「這……都是她纏著我，要我告訴她車票上印著的制度。所以我就稍微給她念了念御一夜鐵路股份公司的乘客須知」
- old_vn (csv3): 「À thì…… Hikari cứ đòi 『Mẹ dạy cho con luật đi tàu đi』.\nNên em mới đọc một chút về Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohito.」
- fix: 「À thì…… Hikari cứ đòi 『Mẹ dạy cho con luật đi tàu đi』.\nNên em mới đọc một chút về Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2015 — item T2 (JP: おひとよ (hiragana của 御一夜))

- JP: 「てーてつじだいからのでんとーなのー！\nおひとよてつどーにも、きていあるのー！」
- TW: 「這是帝國鐵路時代的傳統！御一夜鐵路也有這個規定！」
- old_vn (csv3): 「Đây là truyền thống từ thời Đế Thiết đó!\nĐường sắt Ohito cũng có quy định này!」
- fix: 「Đây là truyền thống từ thời Đế Thiết đó!\nĐường sắt Ohitoyo cũng có quy định này!」
- Lý do: JP chứa おひとよ (hiragana của 御一夜); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

### key 2393 — item T2 (JP: 御一夜鉄道)

- JP: 御一夜鉄道株式会社旅客営業規則。
- TW: 御一夜鐵路股份公司乘客須知。
- old_vn (csv3): Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohito.
- fix: Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 03_Paulette — `ポーレット03_廃炭鉱.txt.toml` (1 dòng)

### key 1939 — item T2 (JP: 御一夜鉄道)

- JP: 「そうですよね、けど……炭鉱まで本格的に\n調査復興するんなら、御一夜鉄道だけじゃ、ちょっと」
- TW: 「是啊，不過……如果要連煤礦也一起重新調查然後復活，只憑御一夜鐵路的話恐怕……」
- old_vn (csv3): 「Đúng vậy anh nhỉ, nhưng mà…… nếu phải tiến hành điều tra và khôi phục mỏ than\nmột cách bài bản, thì chỉ với Đường sắt Ohito e là hơi khó.」
- fix: 「Đúng vậy anh nhỉ, nhưng mà…… nếu phải tiến hành điều tra và khôi phục mỏ than\nmột cách bài bản, thì chỉ với Đường sắt Ohitoyo e là hơi khó.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 03_Paulette — `ポーレット04_ヒヤリング.txt.toml` (1 dòng)

### key 1685 — item T2 (JP: 御一夜鉄道)

- JP: 「レールショップにいるわたしは、市長ではなく、\n御一夜鉄道株式会社の社長、ですよね？」
- TW: 「當我走進鐵路商店的時候，我的身份就不是市長，而是御一夜鐵路股份公司的社長對吧？」
- old_vn (csv3): 「Khi ở cửa hàng đường sắt, em không phải là thị trưởng,\nmà là giám đốc của Công ty Cổ phần Đường sắt Ohito, đúng không ạ?」
- fix: 「Khi ở cửa hàng đường sắt, em không phải là thị trưởng,\nmà là giám đốc của Công ty Cổ phần Đường sắt Ohitoyo, đúng không ạ?」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 03_Paulette — `ポーレット04_鳴呼いきストーブ列車.txt.toml` (1 dòng)

### key 2604 — item T2 (JP: 御一夜鉄道)

- JP: 理解する。ひかりが読めていたものは、旧帝鉄の――\nつまり、御一夜鉄道でも同じく使われている表記部分で。
- TW: 我懂了。光剛才讀的部分，是從前帝國鐵路時代沿用下來的。也就是說，那部分注意事項與御一夜鐵路使用的相同。
- old_vn (csv3): Tôi đã hiểu ra. Những gì Hikari đọc được, là của Teitetsu cũ——\nNói cách khác, đó là phần biểu đạt cũng được sử dụng ở Đường sắt Ohito.
- fix: Tôi đã hiểu ra. Những gì Hikari đọc được, là của Teitetsu cũ——\nNói cách khác, đó là phần biểu đạt cũng được sử dụng ở Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 04_Reina — `lrれいな追加03_れいなとのレール.txt.toml` (1 dòng)

### key 1319 — item T2 (JP: 御一夜鉄道)

- JP: 「消す方がきっとむつかしいですよぉ。\n御一夜鉄道のみんなだって、れいなたちの家族ですから」
- TW: 「要想消失才更加困難。御一夜鐵路相關的所有人都是我們的家人啊」
- old_vn (csv3): 「Muốn xóa bỏ chắc chắn còn khó hơn đó nha~.\nBởi vì mọi người ở Đường sắt Ohito cũng là gia đình của Reina mà.」
- fix: 「Muốn xóa bỏ chắc chắn còn khó hơn đó nha~.\nBởi vì mọi người ở Đường sắt Ohitoyo cũng là gia đình của Reina mà.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 05_Mayami — `lr真闇追加02_御一夜新婚旅行.txt.toml` (1 dòng)

### key 1350 — item T2 (JP: 御鉄 (viết tắt của 御一夜鉄道))

- JP: 「あ、見たことあるかも。\n[おんてつ,1]御鉄さんのカレンダーとかに載ってなかと？　そん写真」
- TW: 「嗯，你應該見過。御一夜鐵路的日曆上應該有照片吧？」
- old_vn (csv3): "「A, hình như chị cũng từng thấy rồi.\nBức ảnh đó có in trên lịch của Đường sắt Ohito đúng không?」"
- fix: "「A, hình như chị cũng từng thấy rồi.\nBức ảnh đó có in trên lịch của Đường sắt Ohitoyo đúng không?」"
- Lý do: JP chứa 御鉄 (viết tắt của 御一夜鉄道); VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## 05_Mayami — `真闇h3_補習授業の廃校舎.txt.toml` (1 dòng)

### key 2608 — item T2 (JP: 御一夜鉄道)

- JP: 「文化祭やら、体育祭やら……例えば、御一夜鉄道の\nメンツでそれを行えるのなら、楽しそうだ」
- TW: 「文化節啊、體育節啊……要是能帶上御一夜鐵道的人一起辦這些活動，會很有趣的」
- old_vn (csv3): 「Nào là lễ hội văn hóa, đại hội thể thao……Ví dụ như, nếu có thể tổ chức cùng\nnhững thành viên của Đường sắt Ohito, thì chắc sẽ vui lắm.」
- fix: 「Nào là lễ hội văn hóa, đại hội thể thao……Ví dụ như, nếu có thể tổ chức cùng\nnhững thành viên của Đường sắt Ohitoyo, thì chắc sẽ vui lắm.」
- Lý do: JP chứa 御一夜鉄道; VN cũ dùng dạng cũ "Ohito" → đổi thành "Ohitoyo" theo T1/T2 (áp dạng dài trước).

## §3. Ghi chú giữ lại / cờ (đã xem xét nhưng KHÔNG đổi thêm gì ngoài Ohito)

- **0 dòng bị loại vì JP không chứa thuật ngữ.** Cả 136 ứng viên đều có JP xác nhận (kanji, kana hoặc viết tắt 御鉄). Không có flag misalignment nào trong batch này.
- **ハチロク04_小畑越え 1823 (audit-src):** audit đã sửa lần xuất hiện đầu "Ở Ohito" → "Ở Ohitoyo" nhưng bỏ sót "Đường sắt Ohito" ở cùng dòng; batch này chỉ sửa phần còn sót. old_vn = giá trị audit.
- **ハチロク04_小畑越え 1902:** TW lược bỏ tên công ty ("勞您接待不勝榮幸…") nhưng JP có 御一夜鉄道 rõ ràng — JP thắng TW, vẫn sửa thành "Đường sắt Ohitoyo".
- **ハチロク08_教導 2828/2868:** "tuyến Yui thuộc Đường sắt Ohito" → chỉ đổi "Đường sắt Ohito" → "Đường sắt Ohitoyo"; "tuyến Yui" GIỮ NGUYÊN (thuộc mục T7, batch khác).
- **ハチロク05_レイルロオドたち 2361/2765:** "tuyến Ohito - Hayato" (JP 御一夜－早戸間) → "tuyến Ohitoyo - Hayato" (T1, dạng trần trong tên tuyến).
- **9 dòng audit-src** (ハチロク04_小畑越え 1823/2112, ハチロク04_煙には煙を 1855/1920, ハチロク05 2960, ハチロク12 2565, ハチロク15b 1637, 日々姫16 2107, ポーレット03 1750): old_vn = giá trị fix audit (moan không đụng dòng nào trong batch — 0 dòng moan-src). Các phần audit đã sửa khác (đại từ, gloss, "Meriken", Teitetsu…) được giữ nguyên, chỉ đổi Ohito.
- **00_Common: 0 ứng viên.** Đã quét toàn bộ good-set thư mục 00: mọi dòng "Ohito" ở Common đã thành "Ohitoyo" trong audit. Các dòng "Ohimitera" ở Common 14 (vd. keys 1082/1128/1461/1805) đã được audit sửa thành "Ohitoyo" — thuộc batch U1, không đụng ở đây.
- **Không đụng dòng gasp Ư hay dòng "Kh" nào.** Không dòng ứng viên nào là dòng gasp/moans.

## §4. Lượt soát 2 (second pass — đọc lại toàn bộ 136 fix với JP)

- **Tổng số fix:** 136. **Tái kiểm chứng:** 136/136. **Bỏ:** 0. **Sửa:** 0.
- **Kiểm chứng cơ học độc lập (đọc lại từ CSV3 + fix-list audit/moans, bằng code path riêng, không dùng lại code lúc liệt kê):** 136/136 mục có key dạng string, jp/tw khớp CSV3 tuyệt đối, old_vn = current value đúng quy ước (moan > audit > CSV3), fix khác old_vn ĐÚNG ở chuỗi mục tiêu duy nhất (kiểm tra: fix với "Ohitoyo" hoàn lại "Ohito" bằng đúng old_vn với cùng phép hoàn lại; 0 lần xuất hiện "Ohito" trần còn sót trong fix), item T1/T2/T1+T2 khớp dạng trong old_vn 136/136, JP chứa thuật ngữ 136/136, 0 dòng lẫn "Ohimitera".
- **Kiểm chứng TOML:** 26 khối TOML (một khối mỗi file), 136 khóa, parse OK bằng tomllib, giá trị parse được khớp JSON 136/136. Trong khối, `\\n` = ký tự `\n` thật trong giá trị (quy ước TOML block của dự án).
- **Đọc lại bằng mắt:** toàn bộ 136 dòng JP/TW/old_vn đã đọc ở lượt 1 (§2 từng dòng); lượt 2 kiểm tra lại fix value của từng dòng theo quy tắc dài-trước-trần-sau và đếm lại số lần "Ohitoyo" trong fix = số "Ohitoyo" cũ + số "Ohito" trần cũ (136/136 khớp).

## §5. Khối TOML (26 file, 136 khóa — áp vào file TOML khi rebuild; `\\n` trong khối = ký tự \n thật trong giá trị)

### 01_Hachiroku/ハチロク01_こんにちわ赤ちゃん.txt.toml

```toml
1670 = "「……Một sự trở về như vậy,\\nchỉ cần làm việc ở Đường sắt Ohitoyo, thì ai cũng có thể dễ dàng nhận ra thôi.」"
2096 = "「Tức là, trong suốt 6 năm qua, Đường sắt Ohitoyo đã không thể\\nđưa ra bất cứ thứ gì để bù đắp cho điều đó sao.」"
2135 = "「Để Đường sắt Mikan đưa vào sử dụng phương tiện mới,\\nvà chuyển các đầu máy dư thừa cho Đường sắt Ohitoyo——đúng không?」"
2161 = "「Đường sắt Ohitoyo đã phân tích kỹ càng nguyên nhân là gì chưa.\\nCậu Soutetsu, hãy để tôi nghe từ chính miệng cậu xem nào.」"
2412 = "「Thực tế, Đường sắt Ohitoyo trong 6 năm qua, luôn đạt mức tăng trưởng trên 5% so với năm trước,\\nlợi nhuận kinh doanh tiếp tục tăng trưởng cực kỳ thuận lợi.」"
2468 = "「Tuyến Yunoi của Đường sắt Ohitoyo, khi so sánh với các tuyến khác,\\ncó một lợi thế áp đảo trong việc thu hút \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;.」"
2494 = "「Đúng như ông đã chỉ ra. Đường sắt Ohitoyo là nơi khởi nguồn của dự án này,\\nmặc dù là trung tâm, nhưng lại bị chậm chân.」"
```

### 01_Hachiroku/ハチロク01_双鉄の目・ハチロクの目.txt.toml

```toml
1710 = "「Thực ra, em cũng mới xem lần đầu. Trước khi nghe chị Paulette nói,\\nem còn chẳng biết Đường sắt Ohitoyo có trang web chính thức cơ.」"
2109 = "「Chị ấy bảo sẽ giới thiệu trên trang web chính thức của Đường sắt Ohitoyo.\\nĐợi chút, tìm kiếm cái là ra ngay ấy mà.」"
```

### 01_Hachiroku/ハチロク02_ハートブレイク・レイルロオド.txt.toml

```toml
1974 = "「Em đã kiên trì thuyết phục họ rằng, để thực sự kết nối Đường sắt Mikan và Đường sắt Ohitoyo,\\nthì Đầu máy số 9 là vô cùng cần thiết.」"
2023 = "「Cô là cô Olivy đúng không ạ? Lần đầu gặp mặt.\\nChào mừng cô đến với Đường sắt Ohitoyo.」"
2191 = "「Vâng. Em cũng đã vẽ xong bản đồ minh họa Ga Suối nước nóng Ohitoyo rồi á!\\nTrong lúc chờ ký kết xong, em định sẽ hướng dẫn bé ấy tham quan ga.」"
2327 = "「Mọi người ở Đường sắt Ohitoyo đang chào đón chúng ta đấy.\\nVậy mà……Olivy. Cô định làm ô uế danh tiếng của Đường sắt Mikan sao.」"
2376 = "「Trưởng phòng Vận tải Đường sắt Ohitoyo, \\x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.\\nKiêm chủ tàu 8620, \\x%l機関士;#00ffc040;người lái tàu%l;#; hơi nước, Migita Soutetsu.」"
2378 = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 Đường sắt Ohitoyo, Hachiroku.\\nBé Olivy. Từ nay mong được em giúp đỡ nhé?」"
2409 = "「Thế rồi, bé Olivy nghe được chuyện đó,\\ncó lẽ đã tự mình tình nguyện chuyển đến Ohitoyo đấy!」"
2431 = "「Là bé Olivy gọi ạ!\\nBé ấy phấn khích lắm, bảo là 『Em sẽ đến Ohitoyo ngay bây giờ~!』」"
2473 = "「Chào mừng~! Chào mừng đến với Đường sắt Ohitoyo!!!」"
2501 = "「Chúc mừng bé Olivy và Đầu máy số 9,\\nđã đến với Đường sắt Ohitoyo——」"
2505 = "「Rồi sau đó, lúc tụi em quay lại ga Suối nước nóng Ohitoyo,\\nthì vừa nãy lại có điện thoại gọi tới đó ạ~」"
2544 = "「Cuối cùng cũng đến rồi á!\\nChào mừng~! Chào mừng đến với Đường sắt Ohitoyo!!」"
2556 = "「Chà, đáng tin cậy thật. Chắc hẳn họ không muốn lãng phí một phút một giây nào,\\nvà muốn làm việc ở Đường sắt Ohitoyo càng sớm càng tốt đây mà.」"
2563 = "「Quê hương hơi nước Ohitoyo,\\nđã chờ đợi Đầu máy số 9 và cô Olivy từ lâu rồi ạ!」"
2564 = "「Quê hương hơi nước Ohitoyo, nhiệt liệt chào mừng Đầu máy số 9 và cô Olivy!\\nạ!!」"
2580 = "「Vừa nghe tin chuyển nhượng đến Đường sắt Ohitoyo là bé ấy đã,\\n『Mọi người định vứt bỏ Olivy!』 rồi phản ứng gay gắt luôn ạ.」"
2629 = "「Chà, thế cũng khác thường nhỉ. Đã qua Okoba rồi,\\nthì cứ đến thẳng Ohitoyo nghỉ ngơi luôn cũng được mà.」"
2640 = "「Cứ thấy, câu chuyện này không vui vẻ gì á.\\nCứ như Đường sắt Ohitoyo bị coi là thùng rác vậy á.」"
2647 = "「Vừa phải thôi. Từ sáng đến giờ rồi.\\nSự ích kỷ của cô đang kéo cả Đường sắt Ohitoyo vào đấy.」"
3027 = "Mọi người đều mỉm cười chuẩn bị cho buổi chào mừng.\\nTôi dần cảm nhận được, đây chính là Đường sắt Ohitoyo."
3053 = "Kinh nghiệm của một \\x%lレイルロオド;#00ffc040;Railord%l;#; đã hoạt động 100 năm,\\nchắc chắn sẽ mang lại những điều tuyệt vời cho Đường sắt Ohitoyo."
3069 = "Nếu có ý kiến phản đối hay thắc mắc gì, cứ thẳng thắn bày tỏ.\\nBởi vì được phép làm vậy chính là điểm mạnh của Đường sắt Ohitoyo mà."
3129 = "Đường sắt Ohitoyo kết thúc chuyến chạy lúc 19:27 khi đến Suối nước nóng Ohitoyo vào buổi tối,\\nnhưng để chở học sinh đi tập luyện buổi sáng, chuyến đầu tiên xuất phát rất sớm lúc 05:27."
3166 = "Phát huy hết mức có thể \"chất\" riêng của Đường sắt Ohitoyo,\\nđể chào đón Đầu máy số 9 và \\x%lレイルロオド;#00ffc040;Railord%l;#; một cách ấm áp và vui vẻ."
3179 = "Điều đó cũng cho thấy công ty Đường sắt Mikan coi trọng sự tin tưởng,\\nvà mối liên kết với Đường sắt Ohitoyo đến mức nào."
3378 = "Bức ảnh chụp khoảnh khắc Đầu máy số 9 lần đầu tiên tiến vào Ga Suối nước nóng Ohitoyo.\\nCó thể dùng làm quà tặng, hoặc làm tư liệu quảng bá cũng được."
3405 = "Nếu vậy, rủi ro phía Đường sắt Ohitoyo sẽ được giảm thiểu đáng kể."
3426 = "Nụ cười của Reina tạo nên bầu không khí.\\nMột bầu không khí ấm áp, náo nhiệt, dịu dàng đậm chất Ohitoyo."
3439 = "Đầu tiên là tấm bảng chào mừng của Nagi và Fukami\\n『Chào mừng! Đến với quê hương hơi nước Ohitoyo』——Không có vấn đề gì."
```

### 01_Hachiroku/ハチロク04_小畑越え.txt.toml

```toml
1477 = "「……Đây cũng được coi là một chuyến công tác với tư cách là nhân viên của Đường sắt Ohitoyo.\\nChúng ta phải tận dụng thời gian một cách có ý nghĩa nhất có thể.」"
1823 = "「Ở Ohitoyo đã làm phiền anh rồi.\\nTôi là \\x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohitoyo. Migita Soutetsu.」"
1902 = "「Rất hân hạnh được gặp ông. Nhưng mà, sao ông biết\\nchúng tôi là người của Đường sắt Ohitoyo hay vậy?」"
1973 = "「À, các vị là người của Đường sắt Ohitoyo đúng không.」"
2112 = "「Ra vậy. Paulette không có kinh nghiệm làm việc ở Teitetsu.\\nDo đó, Đường sắt Ohitoyo nằm ngoài vòng văn hóa đó sao.」"
2121 = "「Giống như Đường sắt Mikan và Đường sắt Ohitoyo đã kết nối với nhau,\\nđường ray nhất định sẽ lại được kết nối rộng khắp một lần nữa.」"
2181 = "「Nói thẳng ra thì đúng là vậy. Do đó hôm nay,\\nchúng tôi muốn hỏi thăm về tình hình của cô ấy trước khi chuyển nhượng cho Đường sắt Ohitoyo.」"
2182 = "「Là đi làm việc ở Đường sắt Ohitoyo――sao?」"
2217 = "「Em là Hachiroku, \\x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu ạ.\\nLà \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của 8620 thuộc Đường sắt Ohitoyo ạ.」"
2234 = "「Tôi trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohitoyo.\\nThế là, nó――」"
2298 = "「Vâng, đúng vậy. Tôi là Migita Soutetsu, Trưởng phòng Vận tải kiêm \\x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;,\\nkiêm \\x%l機関士;#00ffc040;lái tàu%l;#; của 8620 thuộc Đường sắt Ohitoyo.」"
```

### 01_Hachiroku/ハチロク04_煙には煙を.txt.toml

```toml
1855 = "「Khói trị khói á――anh hai――anh Soutetsu, anh tỉnh táo không đấy?\\nMùa hè ở Ohitoyo, mà lại trong căn phòng chật hẹp thế này cơ mà?」"
1920 = "「Tôi cũng chỉ đang nghĩ――mình phải cố gắng thôi.\\nTrước hết là vì chấn hưng du lịch, và vì bảo vệ Ohitoyo.」"
2073 = "「Đúng vậy nha! Chỉ toàn thợ mộc ở Ohitoyo,\\nnhận trọn gói sửa chữa làm cho quán đẹp lên đó.」"
2105 = "「Làm cho thị trấn Ohitoyo nhộn nhịp lên,\\nrồi kéo thêm nhiều khách đi thuyền xuôi dòng nữa nha!」"
2393 = "「Chắc chắn \\x%l列車;#00ffc040;chuyến tàu%l;#; này sẽ nổi tiếng lắm đây.\\nRồi Ohitoyo――sẽ lại trở thành một thị trấn nhộn nhịp nhỉ.」"
2464 = "「Lúc \\x%l列車;#00ffc040;chuyến tàu%l;#; BBQ quay về, số người sử dụng thuyền xuôi dòng từ bến tàu Yui\\nđến Ohitoyo cũng đang tăng lên đều đặn mà.」"
```

### 01_Hachiroku/ハチロク05_レイルロオドたち.txt.toml

```toml
2361 = "「Chỉ là, có vẻ khó mà sử dụng nguyên xi \\x%l客車;#00ffc040;toa hành khách%l;#;\\nmà Đầu máy số 9 kéo về cho tuyến Ohitoyo - Hayato được.」"
2455 = "「A, chuyện đó hả.\\nVề chuyện đó ấy, Đường sắt Ohitoyo lạ thật đấy~」"
2473 = "「Ừm. Ở Ohitoyo có cả kỹ sư Railord,\\nvà ở Jutsusen cũng có nhà máy chế tạo toa xe nữa nên――」"
2638 = "「Ở Đường sắt Ohitoyo, \\x%lレイルロオド;#00ffc040;Railord%l;#; cũng được trả lương.\\nNgân hàng Kumagin cũng chấp nhận mở tài khoản cho \\x%lレイルロオド;#00ffc040;Railord%l;#; nữa.」"
2640 = "「Đường sắt Ohitoyo đúng là kỳ lạ mà!\\n\\x%lレイルロオド;#00ffc040;Railord%l;#; thuyết giáo mà không bị mắng gì cả!」"
2765 = "「Đã rõ. Vậy thì, 3 tuần nữa chúng ta cũng phải\\nthành thạo để có thể đảm nhận tuyến Ohitoyo - Hayato thôi.」"
2834 = "「Cô Paulette chắc chắn cũng sẽ nói vậy nhỉ.\\nVì cội nguồn văn hóa của Đường sắt Ohitoyo là từ cô Paulette mà.」"
2922 = "「Với lại, được đi bộ trên đường ray cũng thích lắm! Vui lắm luôn!\\nCũng biết được là Đường sắt Ohitoyo không có chuyên gia \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nữa.」"
2941 = "「Nhắc mới nhớ, Olivy từng nói.\\n'Ở Ohitoyo không có chuyên gia \\x%l保線;#00ffc040;bảo trì đường ray%l;#;'.」"
2960 = "「Với tư cách là một thành viên của Đường sắt Ohitoyo, là chủ tàu của Đường sắt Ohitoyo,\\nanh không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」"
3003 = "「Tôi nghĩ điều đó thật sự rất tuyệt vời.\\nTôi tin chính sức mạnh đó đã bảo vệ Ohitoyo.」"
3461 = "Trong khoảng thời gian chờ Olivy đến,\\nĐường sắt Ohitoyo cũng đã có kế hoạch tuyển dụng."
3555 = "……Sự phục hưng du lịch của Ohitoyo, quả thực nếu so với các khu vực xung quanh\\nthì có vẻ hơi chậm. Tuy nhiên, thực tế lại vô cùng vững chắc."
3706 = "Fukami vẫn còn rất trẻ, lại hoàn toàn gắn bó với Ohitoyo.\\nTất nhiên là sẽ phải kiêm nhiệm cả việc chèo thuyền xuôi dòng sông Kuma……"
3743 = "Chỉ cần làm vậy, trình độ \\x%l保線;#00ffc040;bảo trì đường ray%l;#; của Đường sắt Ohitoyo\\nchắc chắn sẽ tăng vọt lên một tầm cao mới."
3790 = "Dù vậy, em ấy có vẻ sẽ trưởng thành và trở thành một trong những trụ cột\\ncủa Đường sắt Ohitoyo trong tương lai――hay nói đúng hơn là của Ohitoyo."
```

### 01_Hachiroku/ハチロク08_教導.txt.toml

```toml
1384 = "「……Mong muốn giúp đỡ Ohitoyo,\\nchắc chắn là điểm chung của tất cả những ai yêu mến Ohitoyo.」"
2031 = "「Bao gồm cả khu vực quanh \\x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; thì ở Ohitoyo có 7 cái.\\nỞ ga cũ Makiri—— trạm tín hiệu Makiri có 3 cái, tổng cộng là 10.」"
2091 = "「Ủa? Awa wa——\\nCái đầu tiên là ngay sau khi ra khỏi Ohitoyo, qua khỏi đoạn giao cắt đường sắt là có liền.」"
2327 = "「Đúng đó! Hơn nữa,\\nĐường sắt Ohitoyo còn định kéo dài đường ray thêm nữa mà đúng không?」"
2328 = "「Đúng vậy! Bởi vì, theo những gì Olivy nghe được,\\nmọi người đều rất vui mừng! Họ bảo là nhờ có Ohitoyo đó.」"
2651 = "「Bản thân nhà máy Aircra đâu phải là thứ xấu xa gì,\\nchỉ là không hợp với Ohitoyo thôi.」"
2826 = "「Thế thì, Đường sắt Ohitoyo đang có vòng tuần hoàn tốt!\\nĐúng không! Vì vậy nên đường ray mới được kéo dài ra!!」"
2828 = "「Nhóm này, là nhóm có kiến thức bảo trì đường ray\\ncủa tuyến Yui thuộc Đường sắt Ohitoyo đúng không? Vậy nên, là nhóm B.」"
2868 = "「OK! Vậy thì bắt đầu nha~! Câu đố bảo trì đường ray, câu hỏi thứ nhất! 『Số lượng hầm chui trên tuyến Yui của Đường sắt Ohitoyo là bao nhiêu?』」"
3358 = "Một yếu tố không phù hợp với Ohitoyo,\\nnhưng ở Sendai, nó lại phát huy tác dụng và cống hiến cho khu vực."
```

### 01_Hachiroku/ハチロク11_御一夜鉄道小畑線.txt.toml

```toml
2121 = "「Giả sử khi tỉnh dậy từ trạng thái đóng băng, chúng ta đã đi đến cuối cuộc đời. \\nThì nhà Migita và Đường sắt Ohitoyo chắc chắn vẫn sẽ dang rộng vòng tay chào đón Olivy.」"
2446 = "Nếu không làm vậy, Đường sắt Ohitoyo sẽ rơi vào nguy cơ sống còn—— \\nBởi vì tôi nghĩ, có lẽ đây chính là một tình huống như vậy."
```

### 01_Hachiroku/ハチロク12_ムナカタ来訪.txt.toml

```toml
1590 = "「Trong trường hợp kế hoạch thành lập công ty chuyên bảo trì đường ray bị đổ bể, chúng cháu cũng muốn nhờ chú \\nquản lý cả phần \\x%l保線;#00ffc040;bảo trì đường ray%l;#; với tư cách là nhân viên hợp đồng của Đường sắt Ohitoyo, nên gần như sẽ là làm việc toàn thời gian ạ」"
1626 = "「Mặt khác, về việc làm nhân viên hợp đồng tại Đường sắt Ohitoyo với nhiệm vụ chính là hướng dẫn, \\nchúng cháu rất mong chú có thể nhận lời.」"
1746 = "「U hu hu, chào mừng chú đến với Đường sắt Ohitoyo nha~」"
1760 = "「Đường sắt Ohitoyo muốn tích cực tận dụng \\nnhững kiến thức mà Olivy đã tích lũy được.」"
2058 = "「Ở Đường sắt Ohitoyo, có vẻ cháu được đối xử rất tốt nhỉ.」"
2104 = "「Đồng thời, chúng cháu cũng hy vọng chú có thể làm việc như một nhân viên \\x%l嘱託;#00ffc040;hợp đồng%l;#; của Đường sắt Ohitoyo, \\nvới nhiệm vụ chính là hướng dẫn \\x%l機関士;#00ffc040;lái tàu%l;#; và \\x%l機関助士;#00ffc040;phụ lái tàu%l;#;.」"
2224 = "「Nếu vậy thì trước mắt, Đường sắt Ohitoyo, \\nnên đối phó như thế nào ạ?」"
2233 = "「Vậy thì nhờ nhóc một việc. Địa điểm phồng rộp đó, nhóc cũng hãy theo dõi sát sao nhé. \\nNếu có gì bất thường, hãy báo cáo cho Đường sắt Ohitoyo, đồng thời——」"
2477 = "Thực tế, Đường sắt Ohitoyo đã không sử dụng Omiya. \\nChắc chắn cũng có không ít các doanh nghiệp đường sắt quy mô nhỏ tương tự như vậy."
2554 = "Để tránh việc Paulette đưa ra mức thù lao quá hời một cách dễ dãi, chỉ riêng điểm này, \\ncô ấy không phải là nhân viên ngân hàng, mà đang đóng vai trò cố vấn quản lý của Đường sắt Ohitoyo."
2565 = "Nhưng, Munakata đã đón nhận lời nói của Reina——văn hóa của Đường sắt Ohitoyo, ít nhất là ngoài mặt, mà không hề bận tâm."
2753 = "Đối với Đường sắt Ohitoyo trong tương lai, khi cần phải tuyển thêm và đào tạo nhân viên mới, \\nkhông có nhân tài nào phù hợp hơn chú ấy."
```

### 01_Hachiroku/ハチロク13_実りの秋.txt.toml

```toml
1694 = "「Không đến mức đó đâu~! Olivy,\\nkhông muốn làm khó Đường sắt Ohitoyo đâu.」"
1955 = "「Ở Ohitoyo với Hayato,\\ntừ 『hoàn toàn』 đang thịnh hành hả?」"
2535 = "Tuy nhiên đáng tiếc là, Đường sắt Ohitoyo hiện tại,\\nkhông có đủ nhân lực và tài chính để giám sát liên tục địa điểm này."
```

### 01_Hachiroku/ハチロク14_冬.txt.toml

```toml
1780 = "「……Lúc đầu ấy? Khi bị bảo là đến Đường sắt Ohitoyo.\\nOlivy, đã nghĩ là mình bị vứt bỏ rồi.」"
2587 = "「Vâng, Đường sắt Ohitoyo xin nghe——\\nHả? À, vâng. Xin hãy nối máy.」"
2774 = "「Vâng. Để có thể chia sẻ thông tin một cách chặt chẽ nhất——\\nviệc xây dựng hệ thống đó, tôi sẽ tiến hành cùng với thành phố Ohitoyo.」"
2918 = "「Đúng vậy đó? Thế nên. Thế nên Olivy, đến Ohitoyo!\\nTôi nghĩ thật tốt vì đã có thể đến Ohitoyo!」"
3680 = "Thật sự mọi người đã chủ động đề nghị hợp tác một cách tích cực đến kinh ngạc.\\nKhông chỉ người dân Ohitoyo, mà cả người dân Yui và Jutsusen nữa."
3747 = "Maruyama Kaori——Người cuối cùng cũng vượt qua được cuộc tuyển chọn gắt gao của Paulette\\nđể gia nhập Đường sắt Ohitoyo, là một nhân viên \\x%l庫内手;#00ffc040;rửa lò%l;#; kiêm \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; tập sự mới."
3843 = "——Sau khi bàn bạc kỹ lưỡng chi tiết về ca trực và các thứ khác,\\nông Nagare lên đường trở về Ohitoyo."
4147 = "（Vẫn có thể tự hoạt động được, cứ để cô ấy nghỉ ngơi những lúc cần thiết——\\nrồi nhờ Tiến sĩ Fushicho tìm cách đến Ohitoyo.）"
```

### 01_Hachiroku/ハチロク14_橋.txt.toml

```toml
2748 = "Nhờ có sự giúp đỡ của Kisaki, thực tế là,\\ntình hình tài chính của Công ty Cổ phần Đường sắt Ohitoyo đã được cải thiện đáng kể."
```

### 01_Hachiroku/ハチロク15a_痛みとの決別.txt.toml

```toml
1997 = "「Vâng. Đường sắt Ohitoyo xin nghe——Á! Olivy!?\\nGặp anh Soutetsu hả? Chị chuyển máy ngay đây」"
2038 = "「Tôi bất ngờ vì cô đã học hỏi về \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohitoyo nữa chứ」"
2116 = "「Ừ, đúng thế. Tôi nhận được yêu cầu từ Đường sắt Ohitoyo.\\nHọ muốn tôi giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」"
```

### 01_Hachiroku/ハチロク15b_さよなら列車.txt.toml

```toml
1299 = "「……Nghe Giám đốc Hinai của Đường sắt Ohitoyo nói,\\nchuyện đó đã được phát trên tivi rồi đấy」"
1512 = "「Không chỉ vậy, từ Ohitoyo hay từ Hayato,\\nlại có ngần này người hướng về Yatsushiro cơ đấy」"
1637 = "「Olivy, Meriken——là con của, Ohitoyo, nhưng.\\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」"
1689 = "「Tôi là Hayase, \\x%l車掌;#00ffc040;trưởng tàu%l;#; của Đường sắt Ohitoyo. Dạ——Trưởng ga hỏi là,\\ncó thể ghép thêm hai [けいきゃくしゃ,2]toa hành khách nhẹ nữa không ạ」"
1999 = "Dù vậy, không hề chùn bước, chiếc \\x%lC12;#00ffc040;C12%l;#; của Đường sắt Mikan,\\ntiến vào tuyến Obata, hướng về Ohitoyo, thách thức con dốc Yadake."
2143 = "Thực tế thì, tôi và Hachiroku, cũng như Đường sắt Ohitoyo,\\nđã được Olivy giúp đỡ biết bao nhiêu——"
```

### 01_Hachiroku/ハチロク16_春.txt.toml

```toml
1221 = "……Đường sắt Ohitoyo chúng tôi, đã nhận được từ Olivy.\\nRất nhiều, rất nhiều những điều quan trọng mà anh Munakata đã truyền dạy."
1884 = "「Tôi không phải là Master.\\nVà, những người này là người của Đường sắt Ohitoyo.」"
2070 = "「Về phần \\x%l機関士;#00ffc040;lái tàu%l;#;, tôi đã được giao nhiệm vụ chỉ dạy.\\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohitoyo các cô cậu đấy.」"
```

### 02_Hibiki/日々姫07_姉の想い。妹の想い.txt.toml

```toml
1962 = "「Với điều kiện đó, Đường sắt Ohitoyo sẽ tìm kiếm nơi tiếp nhận.\\nỨng cử viên số một, dĩ nhiên là Đường sắt Kurudai——tại xưởng đầu máy Bungomori」"
2840 = "Bởi vì em ấy muốn lấy ý kiến của một người ngoài Đường sắt Ohitoyo\\nlàm tiêu chuẩn phán đoán cho 'dự án của Đường sắt Ohitoyo'."
```

### 02_Hibiki/日々姫13_討論会.txt.toml

```toml
1347 = "「Vì chúng tôi đều là những người bạn cùng yêu đường sắt mà.\\nVì Đường sắt Ohitoyo, chắc chắn họ sẽ cho chúng ta mượn sức mạnh.」"
```

### 02_Hibiki/日々姫16_夢を乗せて.txt.toml

```toml
1994 = "「Kisaki gia nhập vào nhóm chúng ta, và Đường sắt Ohitoyo đang dần đạt được những bước tiến xa hơn nữa.」"
2107 = "「Dù có những \\x%lまいてつ;#00ffc040;chủ tàu%l;#; muốn tham gia vào Đường sắt Ohitoyo, nhưng hiện tại chúng ta cũng không còn chỗ để tiếp nhận nữa.」"
```

### 03_Paulette/ポーレット02_古地図.txt.toml

```toml
2398 = "Hơn nữa, nếu in thêm một đoạn giải thích về 'Ngựa Kiji và Ohitoyo'\\nlên mặt sau của giấy gói cơm hộp thì càng tuyệt vời."
```

### 03_Paulette/ポーレット03_大きなにもつのおばあさん.txt.toml

```toml
1518 = "「Anh không biết là chuyện đương nhiên thôi.\\nĐường sắt Ohitoyo đã có chuyến tàu tốc hành nào chạy đâu.」"
1750 = "「Phúc lợi tốt quá đi! Đường sắt Ohitoyo cũng phải học theo mới được.」"
2010 = "「À thì…… Hikari cứ đòi 『Mẹ dạy cho con luật đi tàu đi』.\\nNên em mới đọc một chút về Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohitoyo.」"
2015 = "「Đây là truyền thống từ thời Đế Thiết đó!\\nĐường sắt Ohitoyo cũng có quy định này!」"
2393 = "Quy định kinh doanh hành khách của Công ty cổ phần Đường sắt Ohitoyo."
```

### 03_Paulette/ポーレット03_廃炭鉱.txt.toml

```toml
1939 = "「Đúng vậy anh nhỉ, nhưng mà…… nếu phải tiến hành điều tra và khôi phục mỏ than\\nmột cách bài bản, thì chỉ với Đường sắt Ohitoyo e là hơi khó.」"
```

### 03_Paulette/ポーレット04_ヒヤリング.txt.toml

```toml
1685 = "「Khi ở cửa hàng đường sắt, em không phải là thị trưởng,\\nmà là giám đốc của Công ty Cổ phần Đường sắt Ohitoyo, đúng không ạ?」"
```

### 03_Paulette/ポーレット04_鳴呼いきストーブ列車.txt.toml

```toml
2604 = "Tôi đã hiểu ra. Những gì Hikari đọc được, là của Teitetsu cũ——\\nNói cách khác, đó là phần biểu đạt cũng được sử dụng ở Đường sắt Ohitoyo."
```

### 04_Reina/lrれいな追加03_れいなとのレール.txt.toml

```toml
1319 = "「Muốn xóa bỏ chắc chắn còn khó hơn đó nha~.\\nBởi vì mọi người ở Đường sắt Ohitoyo cũng là gia đình của Reina mà.」"
```

### 05_Mayami/lr真闇追加02_御一夜新婚旅行.txt.toml

```toml
1350 = "\"「A, hình như chị cũng từng thấy rồi.\\nBức ảnh đó có in trên lịch của Đường sắt Ohitoyo đúng không?」\""
```

### 05_Mayami/真闇h3_補習授業の廃校舎.txt.toml

```toml
2608 = "「Nào là lễ hội văn hóa, đại hội thể thao……Ví dụ như, nếu có thể tổ chức cùng\\nnhững thành viên của Đường sắt Ohitoyo, thì chắc sẽ vui lắm.」"
```

Kết bài