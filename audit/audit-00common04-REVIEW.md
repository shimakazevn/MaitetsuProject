# Audit — 00_Common file 04 (共通04_キハ07。ポーレットとれいな)

File TOML: `00_Common/共通04_キハ07。ポーレットとれいな.txt.toml` — md5 `024224f6c52fa78e6dbec6b5f66ba881`, không có bản sao trùng (duy nhất trong 227 file).
Nguồn CSV: bộ `03_Paulette` của CSV3 (385 dòng, khớp TOML 384/385 flat-match). Bộ `00_Common` là bộ CŨ (chỉ khớp 15/385) — không dùng. Xem `dual-csv-sets.md`.
Phương pháp: đọc toàn bộ 385/385 dòng script, đối chiếu từng dòng với JP (+TW làm chứng thứ hai), kiểm tra chuỗi xoay, tràn chương, tag %l, rên っ, xưng hô, thuật ngữ đã quyết.

## Kết quả: 19/385 dòng sai (4,9%)

| Loại | Số dòng | Chi tiết |
|---|---|---|
| Thuật ngữ (terminology) | 6 | 1791 (gloss 枕木 sai chính tả), 2254 (tag bịa + 'thân chính'), 2262 (帝鉄), 2388 ('thân chính'), 2558 (tag bịa + 'thân chính'), 2658 (Ohimitera) |
| Xưng hô (pronoun) | 4 | 2138, 2177, 2404, 2624 — Soutetsu gọi Hachiroku/Reina là 'cô' thay vì 'em' |
| Sai nghĩa (meaning) | 4 | 2154 (câu cụt, theo TW), 2393 (JP thắng TW), 2534 (lời hô 喚呼), 2591 (lặp lại cách đọc) |
| Rên っ (gasp) | 2 | 2676, 2677 — mất rên cả dòng (sweep đã xác nhận) |
| Nhỏ (minor) | 3 | 2098 (thiếu 1 lần lặp), 2329 (thiếu dấu phẩy), 2966 (tự thêm ngoặc) |
| **Tổng** | **19** | |

## Cấu trúc: 0 lệch dòng, 0 chuỗi xoay, 0 tràn chương, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key

File sạch thứ tư của dự án tính đến nay (4,9% sai, sau 実りの秋 0,4%, ヒヤリング 2,0%, 共通03 4,4%): cột Việt đứng đúng chỗ ở cả 385 dòng. 19 lỗi còn lại đều là lỗi lẻ tẻ, không có lỗi hệ thống nào. Không có dòng nào chưa chắc chắn (uncertain: 0).

## Nguồn dữ liệu — bộ CSV đôi (đã kiểm chứng)

CSV3 có hai bộ dòng cho file này (cùng 385 key): bộ `03_Paulette` khớp TOML 384/385 (1 dòng lệch là 2677, xem dưới), bộ `00_Common` chỉ khớp 15/385 — bộ cũ. Audit dùng bộ `03_Paulette`.

- **2677 không phải lệch CSV/TOML:** script so sánh báo 1 diff ở 2677, nhưng kiểm tra trực tiếp cho thấy VN ở CSV và TOML giống hệt nhau (`「!」\n「A」`, literal `\n` cả hai) — đó là lỗi chuẩn hoá `\n` của script so sánh, không phải lệch thật. CSV==TOML: 0 lệch nội dung thật.
- **Số dòng thật là 385, không phải 770** (385 dòng thật + 385 dòng bộ cũ). Bộ cũ phải bỏ trước khi rebuild.

## Kiểm tra chéo (cross-checks)

- **Chuỗi xoay:** không có. Hai giá trị VN trùng lặp duy nhất là `「Ra là vậy.」`×3 (2180, 2182, 2611 — JP đều là なるほどな) và `「Hừm.」`×3 (2217 ふむ, 2227 ふうむ, 2242 ふむ) — lặp hợp lệ, JP gốc giống nhau, không phải lệch dòng.
- **Tràn chương:** 0. Kiểm tra chỉ mục VN toàn dự án: không giá trị VN nào dài >20 ký tự của file này ứng với JP khác ở file khác.
- **Tag %l:** sạch lỗi cú pháp (0 tag thiếu `;`). Chỉ có 2 chỗ VN tự thêm tag gloss không có trong JP: 2254 (tag 運転体) và 2558 (tag 整備体) — cả hai đã gỡ trong fix. Các tag còn lại: số lượng JP = VN ở mọi dòng.
- **Rên っ:** sweep có 3 entry cho file này — 2676, 2677 (đã áp nguyên fix của sweep) và 2154 (needs-file-audit — đã xử lý: không phải gasp, mà là câu cụt, fix theo hướng nghĩa). Không phát hiện thêm gasp mất nào ngoài 2 dòng trên: các っ còn lại đều đã được diễn (2218 んんっ→"E hèm", 2334 きゃっ→"kya!?", 2647 そっ/んっ→"Ng-"/"Ưm", 3177 こっっっく→"Gật——đầu", 3343 ぐ～～っ→"Rột~~") hoặc là っ nhấn mạnh cuối câu gắn vào từ (2221/2223/2655 双鉄様っ, 2535 まさかっ) theo đúng quy tắc sweep.
- **Xưng hô Soutetsu — đã kiểm tra toàn bộ:** 'tôi' 71 dòng; 'mình' 12 hit — tất cả đều đúng, gồm: sở hữu ("tính cách của mình" 1802, "phương tiện của mình" 2531, "cơ thể mình" 3103, "tóc mái của mình" 3256), phản thân ("tự mình" 3128, "tự trói buộc mình" 2871), thành ngữ ("Thân mình còn lo chưa xong" 2857, "hết mình" 3236, "giật bắn mình" 3323), mệnh đề phụ ("mình đã khinh suất" 3083, theo tiền lệ hearing), và ngoại lệ độc thoại nội tâm cảm xúc ("Mình đúng là một gã thảm hại" 3348 — giữ theo tiền lệ h3 1683 / h8 3087). 4 lỗi 'cô' của Soutetsu đã sửa (2138, 2177, 2404, 2624); 'cô' cho Navi (2449) giữ theo quy ước đã lập ở file 03; 'cô ấy' ngôi thứ ba giữ nguyên.
- **B4 (Paulette gọi Soutetsu):** không vi phạm. Paulette gọi "anh Soutetsu" (2285), "xin lỗi anh" (2235); 2214 có "Soutetsu" trần ở giữa ("Migita…… Soutetsu…… Anh Soutetsu——") nhưng đó là cô ấy đang lắp bắp đọc tên (JP ミギタ……ソウテツ…… — bare trong JP), chỉ lần thứ ba mới là cách gọi (双鉄さん → "anh Soutetsu") — giữ nguyên có lý do, xem mục dưới.
- **キルクイティウム:** trong file thống nhất "Quirquitium" 5/5 dòng (2105, 2240, 2304, 2520, 2629). Docs chưa quyết dạng chuẩn; các dạng "Kirukuitium" chỉ xuất hiện ở bộ CSV cũ của chính file này (sẽ bỏ), còn "Circuithium" ở 日々姫10 key 2458 là vấn đề thống nhất liên file, không sửa trong audit này.
- **Nhân vật / thuật ngữ khác đã kiểm tra:** KiHa 07S đúng (2477); 帝鉄 chỉ còn 1 chỗ sai (2262, đã sửa); 冥福 → "Minh Phúc" (2437, tên ga, giữ); "taihisen" giữ dạng Latin + gloss ở 2321 (trích dẫn từ), dùng "đường tránh tàu" ở 3148 (tham chiếu, không trích dẫn) — cả hai đều hợp lý; "Master" cho 運転士/機関士 có ruby マスター (2648, 2651) giữ nguyên.

## Cố tình KHÔNG sửa (đã kiểm tra, có lý do)

- **2214** 「ミギタ……ソウテツ……双鉄――――さん」→"Migita…… Soutetsu…… Anh Soutetsu——" — "Soutetsu" trần ở giữa là cô ấy lắp bắp đọc tên (JP bare ソウテツ), không phải cách gọi; chỉ 双鉄さん mới là cách gọi → "anh Soutetsu". Không vi phạm B4.
- **2449** 「お前の場合は、エアクラ社の設定より……」→"Trong trường hợp của cô, …" — Soutetsu nói với Navi; 'cô' cho Navi là quy ước đã lập (file 03: 1680/2030/2050), giữ nguyên.
- **3348** （情けない男だな、僕は。……）→"（Mình đúng là một gã thảm hại. …" — độc thoại nội tâm tự vấn cảm xúc của Soutetsu, "mình" được phép theo ngoại lệ h3 1683.
- **3130** 自嘲の色を交えず → "không hề có vẻ tự trào" — JP nói KHÔNG có tự trào; TW nói ngược lại ("伴著些許自嘲") — JP thắng TW, bản Việt đã đúng.
- **1802, 2857, 3083, 3103, 3128, 3236, 3256, 3323** — các 'mình' sở hữu/phản thân/thành ngữ/mệnh đề phụ, giữ theo tiền lệ hearing.
- **2179–2182, 2611** なるほどな → "Ra là vậy." — lặp hợp lệ, JP giống nhau.
- **2217/2227/2242** ふむ/ふうむ → "Hừm." — cùng một tiếng ngẫm, giữ như chuẩn các file trước.
- **2321** タイヒセン → "taihisen (đường tránh tàu)" — giữ cách đọc Nhật + gloss theo nguyên tắc giữ gần tiếng Nhật.
- **2345** よっと → "dô." — diễn ngẫu hứng theo quy tắc 22:05, TW 喲呵 tương tự.
- **2966** ガタン/ゴトン → "Cọc cạch" ×4 — âm tàu Việt hoá, giữ; chỉ gỡ ngoặc thừa (xem fix).
- **3014** ざっくり行く → "cứ gọi một cách thân mật đi" — diễn theo ngữ cảnh (đang nói về cách xưng hô), TW cũng hiểu theo hướng này.
- **2910** せがむ → "đòi hỏi" — せがむ là nài nỉ/dòi hỏi dai dẳng, "đòi hỏi" giữ được ý dai dẳng; không sửa.

## Dòng chưa chắc chắn (uncertain)

Không có. 0 dòng uncertain.

## Danh sách fix (19 dòng)

### [1791] — terminology (monologue)
- **JP:** ……ハチロクが簡潔に説明してくれる。\n\x%lバラスト;#00ffc040;バラスト%l;#;とはすなわち線路と\x%l枕木;#00ffc040;枕木%l;#;とを支える敷石だと。
- **TW:** ……八六作了簡要的說明。\x%lバラスト;#00ffc040;道砟%l;#;即墊在線路下，用作承托鐵軌和\x%l枕木;#00ffc040;枕木%l;#;的碎石。
- **Cũ:** ……Hachiroku giải thích ngắn gọn cho tôi. \x%lバラスト;#00ffc040;Đá ba-lát%l;#; chính là lớp đá dăm lót dưới để nâng đỡ đường ray và \x%l枕木;#00ffc040;tàu vẹt%l;#;.
- **Mới:** ……Hachiroku giải thích ngắn gọn cho tôi. \x%lバラスト;#00ffc040;Đá ba-lát%l;#; chính là lớp đá dăm lót dưới để nâng đỡ đường ray và \x%l枕木;#00ffc040;tà vẹt%l;#;.
- **Lý do:** Gloss 枕木 viết sai chính tả 'tàu vẹt' — từ đúng là 'tà vẹt' (xem 2098 dùng 'tà vẹt đường ray').

### [2098] — minor (ハチロク)
- **JP:** 「だめだめだめだめやめてやめてやめてやめて！\n\x%l踏面;#00ffc040;踏面%l;#;削れて\x%l枕木;#00ffc040;枕木%l;#;傷み\x%lバラスト;#00ffc040;バラスト%l;#;くだけてしまいます！」
- **TW:** 「不行不行不行不行別別別別！會削掉\x%l踏面;#00ffc040;踏面%l;#;的，會傷到\x%l枕木;#00ffc040;枕木%l;#;的，會碾碎\x%lバラスト;#00ffc040;道砟%l;#;的！」
- **Cũ:** 「Không được không được không được không được, dừng lại dừng lại dừng lại đi! Sẽ làm mòn \x%l踏面;#00ffc040;mặt lăn bánh xe%l;#;, hỏng \x%l枕木;#00ffc040;tà vẹt đường ray%l;#; và nghiền nát \x%lバラスト;#00ffc040;đá ba-lát%l;#; mất!」
- **Mới:** 「Không được không được không được không được, dừng lại dừng lại dừng lại dừng lại đi! Sẽ làm mòn \x%l踏面;#00ffc040;mặt lăn bánh xe%l;#;, hỏng \x%l枕木;#00ffc040;tà vẹt đường ray%l;#; và nghiền nát \x%lバラスト;#00ffc040;đá ba-lát%l;#; mất!」
- **Lý do:** JP やめて×4, bản cũ chỉ dịch 3 lần 'dừng lại' — thêm lần thứ 4 cho đủ (quy tắc không để mất âm/lặp).

### [2138] — pronoun (双鉄)
- **JP:** 「お前も凛としているぞ、ハチロク。\nこれなら失礼には当たるまい――む」
- **TW:** 「你也很有精神，八六。絕不會失禮——嗯？」
- **Cũ:** 「Cô cũng rất rạng rỡ đấy, Hachiroku. Theo này thì chắc chắn không thất lễ đâu——hửm.」
- **Mới:** 「Em cũng rất rạng rỡ đấy, Hachiroku. Thế này thì chắc chắn không thất lễ đâu——hửm.」
- **Lý do:** Soutetsu gọi Hachiroku là 'Cô' — sai quy ước (Soutetsu→Hachiroku là 'em', 65 dòng ở file 03, 0 lần 'cô'). 'Theo này thì' → 'Thế này thì' cho đúng JP これなら.

### [2154] — meaning (双鉄)
- **JP:** 「ハチロク。時計とぜんまいカギを」
- **TW:** 「八六，給我時鐘和發條鑰匙」
- **Cũ:** 「Hachiroku. Đồng hồ và chìa khóa lên dây cót đâu.」
- **Mới:** 「Hachiroku. Đưa tôi đồng hồ và chìa khóa lên dây cót.」
- **Lý do:** JP cụt (時計とぜんまいカギを, không động từ); TW '給我時鐘和發條鑰匙' (đưa tôi) + mạch truyện (2157 gọi Hachiroku lại gần) → yêu cầu đưa đồ, không phải câu hỏi 'đâu'.

### [2177] — pronoun (双鉄)
- **JP:** 「なるほど。おかげで納得できた。\n会いたいものだな。その\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と、\x%l運転士;#00ffc040;運転士%l;#;とに」
- **TW:** 「原來如此。你這麼一講我明白了。真想見一見那位\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;和\x%l運転士;#00ffc040;駕駛員%l;#;」
- **Cũ:** 「Ra là vậy. Nhờ cô giải thích mà tôi hiểu rồi. Thật muốn gặp mặt quá. Cả \x%lレイルロオド;#00ffc040;Railord%l;#; và \x%l運転士;#00ffc040;người lái tàu%l;#; đó.」
- **Mới:** 「Ra là vậy. Nhờ em giải thích mà tôi hiểu rồi. Thật muốn gặp mặt quá. Cả \x%lレイルロオド;#00ffc040;Railord%l;#; và \x%l運転士;#00ffc040;người lái tàu%l;#; đó.」
- **Lý do:** Soutetsu gọi người giải thích là 'cô' — dù người đó là Reina, Paulette hay Hachiroku thì Soutetsu đều xưng 'em' với cả ba; 'cô' sai quy ước.

### [2254] — terminology (ハチロク)
- **JP:** 「ですので、わたくしたち\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、\n運行管理[ボディ]体と\x%l整備体;#00ffc040;整備体%l;#;の二種の体を使い分けるのです」
- **TW:** 「因此，我們\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;會切換使用駕駛體和\x%l整備体;#00ffc040;整備體%l;#;」
- **Cũ:** 「Vì vậy, \x%lレイルロオド;#00ffc040;Railord%l;#; chúng tôi, sử dụng hai loại cơ thể là \x%l運転体;#00ffc040;kíp lái%l;#; và \x%l整備体;#00ffc040;thân chính%l;#; tùy theo mục đích ạ.」
- **Mới:** 「Vì vậy, \x%lレイルロオド;#00ffc040;Railord%l;#; chúng tôi, sử dụng hai loại cơ thể là thân vận hành và \x%l整備体;#00ffc040;thân bảo trì%l;#; tùy theo mục đích ạ.」
- **Lý do:** JP là 運行管理[ボディ]体 (không có tag %l) + 整備体; bản cũ bịa tag 運転体 gloss 'kíp lái' (sai nghĩa) và dịch 整備体 thành 'thân chính' — quyết định #11: 整備体='thân bảo trì'; gỡ tag bịa, giữ tag 整備体 của JP.

### [2262] — terminology (ハチロク)
- **JP:** 「わたくしの現役最後の時代……\n旧\x%l帝鉄;#00ffc040;帝鉄%l;#;では、それが守られなくなっていたからです」
- **TW:** 「在我一線生涯的最後那段時間……在那個年代，前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;已經開始有人不遵守了」
- **Cũ:** 「Trong thời kỳ cuối cùng em còn hoạt động ở tiền tuyến…… Tại \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ, điều đó đã không còn được tuân thủ nữa ạ.」
- **Mới:** 「Trong thời kỳ cuối cùng em còn hoạt động ở tiền tuyến…… Tại \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ, điều đó đã không còn được tuân thủ nữa ạ.」
- **Lý do:** 帝鉄 → 'Teitetsu' theo quyết định #6 (bỏ 'Đường sắt Hoàng gia').

### [2329] — minor (れいな)
- **JP:** 「あえてうれしいです、ハチロクさん」
- **TW:** 「很高興見到你，八六小姐」
- **Cũ:** 「Được gặp chị Reina vui lắm nha, chị Hachiroku~」
- **Mới:** 「Được gặp chị, Reina vui lắm nha, chị Hachiroku~」
- **Lý do:** Thiếu dấu phẩy khiến 'Được gặp chị Reina' đọc như gặp chính Reina; thêm phẩy theo đúng mạch (Reina nói kiểu ngôi thứ ba, xem 2284).

### [2388] — terminology (双鉄)
- **JP:** 「整備ボディ？」
- **TW:** 「整備體？」
- **Cũ:** 「Thân chính?」
- **Mới:** 「Thân bảo trì?」
- **Lý do:** 整備ボディ → 'thân bảo trì' theo quyết định #11; 'thân chính' sai.

### [2393] — meaning (れいな)
- **JP:** 「はぁい。れいな。\nじじょおは、れいなから聞いちゃだめって覚えましたぁ」
- **TW:** 「明白了。不可以去打聽別人的隱情，玲奈記住啦」
- **Cũ:** 「Vâng ạ~. Reina, Reina nhớ là không được hỏi về ẩn tình của người khác rồi nha~」
- **Mới:** 「Vâng ạ~. Reina nhớ rồi, không được hỏi Reina về ẩn tình đâu nha~」
- **Lý do:** JP: じじょおは、れいなから聞いちゃだめ — 'không được hỏi Reina về ẩn tình'; bản cũ 'ẩn tình của người khác' theo TW (TW khái quát hoá), JP thắng TW.

### [2404] — pronoun (双鉄)
- **JP:** 「ほう？　なぜわかる」
- **TW:** 「是嗎？你怎麼知道的」
- **Cũ:** 「Hô? Sao cô biết?」
- **Mới:** 「Hô? Sao em biết?」
- **Lý do:** Soutetsu hỏi Hachiroku (người vừa giải thích) — 'cô' sai quy ước, phải 'em'.

### [2534] — meaning (ポーレット)
- **JP:** 「非常停止よし。要救助者を確認」
- **TW:** 「緊急停車正常完成。確認救助對象」
- **Cũ:** 「Dừng khẩn cấp thành công. Đã xác nhận người cần cứu hộ.」
- **Mới:** 「Dừng khẩn cấp, xác nhận! Xác nhận người cần cứu hộ.」
- **Lý do:** 非常停止よし là lời hô xác nhận trong nghi thức 喚呼, không phải báo cáo 'thành công'; 要救助者を確認 là mệnh lệnh hô, không phải quá khứ 'đã xác nhận'.

### [2558] — terminology (ハチロク)
- **JP:** 「わたくしが整備[ボディ]体なら、\n\x%lバラスト;#00ffc040;バラスト%l;#;敷きのお手伝いくらいは出来るのですが――」
- **TW:** 「要是用的是整備體的話，我就能幫忙鋪設\x%lバラスト;#00ffc040;道砟%l;#;了」
- **Cũ:** 「Nếu tôi là \x%l整備体;#00ffc040;thân chính%l;#;, thì ít nhất cũng có thể giúp rải \x%lバラスト;#00ffc040;đá ba-lát%l;#;——」
- **Mới:** 「Nếu tôi là thân bảo trì, thì ít nhất cũng có thể giúp rải \x%lバラスト;#00ffc040;đá ba-lát%l;#;——」
- **Lý do:** JP 整備[ボディ]体 không có tag %l (chỉ có ruby [ボディ]); bản cũ bịa tag gloss 'thân chính' — gỡ tag, dịch 'thân bảo trì' theo quyết định #11.

### [2591] — meaning (双鉄)
- **JP:** 「トウメン？」
- **TW:** 「踏面？」
- **Cũ:** 「Mặt lăn bánh xe?」
- **Mới:** 「Toumen?」
- **Lý do:** JP トウメン？ là Soutetsu lặp lại cách đọc vừa nghe ở 2586 ('đọc là toumen'); bản cũ 'Mặt lăn bánh xe?' làm mất mạch lặp lại cách đọc.

### [2624] — pronoun (双鉄)
- **JP:** 「ならば、何故そのように表情が冴えぬのだ？」
- **TW:** 「那你為什麼還看起來不太高興？」
- **Cũ:** 「Vậy thì, tại sao trông sắc mặt cô lại ủ rũ thế kia?」
- **Mới:** 「Vậy thì, tại sao trông sắc mặt em lại ủ rũ thế kia?」
- **Lý do:** Soutetsu hỏi Reina (2625 Reina trả lời ngay sau) — 'cô' sai quy ước, Reina là 'em' (Hachiroku cũng gọi Reina là 'em', 2167).

### [2658] — terminology (双鉄)
- **JP:** 「雛衣ポーレット……というと、御一夜市長？」
- **TW:** 「雛衣波萊特……莫非是御一夜市長？」
- **Cũ:** 「Hinai Paulette…… là Thị trưởng thành phố Ohimitera sao?」
- **Mới:** 「Hinai Paulette…… là Thị trưởng thành phố Ohitoyo sao?」
- **Lý do:** 御一夜 → 'Ohitoyo', không phải 'Ohimitera'.

### [2676] — gasp (ハチロク)
- **JP:** 「っ！」
- **TW:** 「！」
- **Cũ:** 「!」
- **Mới:** 「Ư!」
- **Lý do:** JP っ！ cả dòng là rên, bản cũ chỉ còn '!' — thêm Ư (sweep lost-gasp-whole, đã xác nhận).

### [2677] — gasp (双鉄)
- **JP:** 「っ！」\n「あ」
- **TW:** 「！」\n「啊」
- **Cũ:** 「!」\n「A」
- **Mới:** 「Ư!」\n「A」
- **Lý do:** JP っ！ ở đầu dòng bị mất rên, bản cũ chỉ còn '!' — thêm Ư (sweep lost-gasp-whole, đã xác nhận).

### [2966] — minor (monologue)
- **JP:** ガタン、ゴトン、\nガタン、ゴトン――
- **TW:** 哐璫哐璫哐璫哐璫——
- **Cũ:** （Cọc cạch, cọc cạch, cọc cạch, cọc cạch——）
- **Mới:** Cọc cạch, cọc cạch, cọc cạch, cọc cạch——
- **Lý do:** JP ガタン、ゴトン、ガタン、ゴトン―― không có ngoặc; bản cũ tự thêm （） — gỡ ngoặc cho đúng định dạng gốc.
## Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 19 fix so với JP của từng dòng: **tổng 19 / kiểm tra lại 19 / loại bỏ 0 / sửa 0**. Không phát hiện thêm sai sót nào ở lần 2. Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt.

Khối TOML dưới đây đã parse-verified bằng tomllib: **19 key, 0 lệch giá trị** so với JSON fix list (`audit-00common04-wrong.json`). Lưu ý: giá trị 2677 chứa literal `\n` (2 ký tự) trong JSON; trong khối TOML nó được viết là `\\n` để tomllib parse lại thành literal `\n` — đã kiểm chứng bằng so sánh giá trị đã parse với JSON.

## Khối TOML (fix)

```toml
[script]
1791 = "……Hachiroku giải thích ngắn gọn cho tôi. \\x%lバラスト;#00ffc040;Đá ba-lát%l;#; chính là lớp đá dăm lót dưới để nâng đỡ đường ray và \\x%l枕木;#00ffc040;tà vẹt%l;#;."
2098 = "「Không được không được không được không được, dừng lại dừng lại dừng lại dừng lại đi! Sẽ làm mòn \\x%l踏面;#00ffc040;mặt lăn bánh xe%l;#;, hỏng \\x%l枕木;#00ffc040;tà vẹt đường ray%l;#; và nghiền nát \\x%lバラスト;#00ffc040;đá ba-lát%l;#; mất!」"
2138 = "「Em cũng rất rạng rỡ đấy, Hachiroku. Thế này thì chắc chắn không thất lễ đâu——hửm.」"
2154 = "「Hachiroku. Đưa tôi đồng hồ và chìa khóa lên dây cót.」"
2177 = "「Ra là vậy. Nhờ em giải thích mà tôi hiểu rồi. Thật muốn gặp mặt quá. Cả \\x%lレイルロオド;#00ffc040;Railord%l;#; và \\x%l運転士;#00ffc040;người lái tàu%l;#; đó.」"
2254 = "「Vì vậy, \\x%lレイルロオド;#00ffc040;Railord%l;#; chúng tôi, sử dụng hai loại cơ thể là thân vận hành và \\x%l整備体;#00ffc040;thân bảo trì%l;#; tùy theo mục đích ạ.」"
2262 = "「Trong thời kỳ cuối cùng em còn hoạt động ở tiền tuyến…… Tại \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ, điều đó đã không còn được tuân thủ nữa ạ.」"
2329 = "「Được gặp chị, Reina vui lắm nha, chị Hachiroku~」"
2388 = "「Thân bảo trì?」"
2393 = "「Vâng ạ~. Reina nhớ rồi, không được hỏi Reina về ẩn tình đâu nha~」"
2404 = "「Hô? Sao em biết?」"
2534 = "「Dừng khẩn cấp, xác nhận! Xác nhận người cần cứu hộ.」"
2558 = "「Nếu tôi là thân bảo trì, thì ít nhất cũng có thể giúp rải \\x%lバラスト;#00ffc040;đá ba-lát%l;#;——」"
2591 = "「Toumen?」"
2624 = "「Vậy thì, tại sao trông sắc mặt em lại ủ rũ thế kia?」"
2658 = "「Hinai Paulette…… là Thị trưởng thành phố Ohitoyo sao?」"
2676 = "「Ư!」"
2677 = "「Ư!」\\n「A」"
2966 = "Cọc cạch, cọc cạch, cọc cạch, cọc cạch——"```

## Kết bài

File 04 là file sạch thứ tư của dự án (19/385 = 4,9% sai): không lệch dòng, không chuỗi xoay, không tràn chương, không dòng mồ côi, không dòng chưa dịch, không trùng key, không dòng uncertain. 19 lỗi còn lại toàn là lỗi lẻ tẻ: 6 thuật ngữ (chủ yếu là 'thân chính' sai cho 整備体/整備ボディ ở 3 chỗ + 2 tag gloss bịa + Ohimitera ×1 + 帝鉄 ×1), 4 xưng hô (Soutetsu gọi Hachiroku/Reina là 'cô' thay vì 'em'), 4 sai nghĩa (trong đó 2154 và 2393 là hai chỗ JP/TW mâu thuẫn hoặc cụt, đã xử lý theo JP + mạch truyện), 2 rên っ mất cả dòng (sweep đã xác nhận), 3 lỗi nhỏ (lặp, dấu phẩy, ngoặc).

Điểm đáng ghi: file này cho thấy 00_Common không đồng đều — file 03 chỉ 4,4% sai, file 04 4,9%, trong khi heuristic từng đoán 00_Common là tuyến nặng (392 điểm). Độ sạch thật chỉ lộ ra khi đọc hết từng dòng.

Việc còn lại cho file này: không có. Dòng uncertain: 0. Thuật ngữ キルクイティウム ("Quirquitium" ở đây vs "Circuithium" ở 日々姫10) cần quyết ở đợt thống nhất, không sửa trong audit.
