# Audit — ハチロク05_レイルロオドたち.txt.toml (Hachiroku 05, các Railord)

- File: `translation_toml/01_Hachiroku/ハチロク05_レイルロオドたち.txt.toml` (đường dẫn đĩa: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af05_#U30ec#U30a4#U30eb#U30ed#U30aa#U30c9#U305f#U3061.txt.toml`)
- Route: 01_Hachiroku. 570 dòng script. Nội dung: Olivy đến Ohitoyo, Soutetsu truyền lại lời Munakata (chạy thử tuyến chính, môi trường tốt); Hachiroku khen ngợi công tác kiểm tra bảo dưỡng của "cô giáo Olivy"; chọn lái tàu cho chuyến chạy thử (Hibiki vs Nagi, cuối cùng rút thăm); Fukami lén học làm trưởng tàu; tranh luận "đường tắt vs đường vòng" (Olivy mắng Soutetsu ngạo mạn); báo cáo chạy thử với Paulette và Reina (Olivy 100 điểm, Hibiki chật vật với buồng lái tay phải, gia cố biển báo); Olivy nghe lén chuyện tuổi thọ (kiểm tra toàn diện hàng năm), suy sụp vì mình là Railord kiểu Meriken không có Master; kế hoạch của Soutetsu (lương, mua lại Đầu máy số 9, nghiên cứu kéo dài tuổi thọ); Olivy quá nhiệt, được đưa đi Tororyu-yu.
- Phương pháp: đọc từng dòng (row-by-row) đối chiếu JP + TW (JP thắng khi khác nhau), kiểm tra chuỗi xoay, nhiễm chéo, dòng mồ côi, trùng khóa, thẻ %l, sweep っ-gasp của file, xưng hô theo quy tắc Soutetsu đã sửa 20/11.

## Kết quả tổng

- Đọc: **570 dòng**, sai: **42 dòng (7,4%)**.
- Phân loại (42): gasp っ 8 (2267, 2382, 2439, 2443, 2459, 3023, 3326, 3611 — tất cả từ sweep, nhận cả 8), xưng hô/đại từ 24 (Soutetsu→Hachiroku "anh"→"tôi" 3: 2476, 2667, 2233; Soutetsu→Paulette "tôi"→"anh" 9: 3024, 2475, 2689, 3062, 2944, 2449, 2960, 2710, 2836; Soutetsu→Olivy "tôi"→"anh" 6: 2685, 2819, 2879, 2663, 2679, 2688; Paulette→Soutetsu "cậu"→"anh" trái B4 lock 4: 2929, 3078, 2709, 2715; Hachiroku xin lỗi Soutetsu "xin lỗi anh" 1: 2431; 2949 "Giúp tôi"→"Giúp anh" ở vế cảm ơn Paulette, vế sau "đi theo tôi" với Hachiroku giữ nguyên), sai nghĩa 3 (2713, 2564, 3026), thuật ngữ 7 (冥国式 4: 2866, 2605, 3501, 3740; 冥語 1: 3512; 可変パッド 2: 1728, 3057).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3: 1 set duy nhất (570 dòng, khớp TOML tuyệt đối 570/570; 0 chênh lệch). `[selections]` rỗng. Không có thẻ `%l` sai định dạng (đếm mở/đóng bằng nhau trong TOML; JP/VN bằng nhau về số thẻ mọi dòng).
- TOML md5: `14a9b1b96740ced97469f984b138465f` (127.250 byte, UTF-8 BOM + CRLF). Không có bản sao file này (không trùng md5 với file nào khác trong toml2; 1 bản duy nhất, không thuộc nhóm trùng).
- Sweep: 8 mục cho file, đã kiểm chứng từng mục vs JP và nhận cả 8 (2267, 2382, 2439, 2443, 2459, 3023, 3326, 3611 — VN hiện tại vẫn bằng đúng old_vn của sweep, tức sweep chưa được áp vào file này; riêng 2459 sweep ghi old_vn đã làm phẳng ký tự `\n` thành khoảng trắng, fix lấy theo old_vn của CSV3). Quét máy bổ sung: không còn gasp っ nào sweep bỏ sót (mẫu 2748 「――っていう」 là từ, không phải gasp); không còn ký tự Nhật nào sót lại trong VN ngoài 4 dòng っ thô đã sửa.
- Thuật ngữ chờ đợt thống nhất, KHÔNG tính sai: "Ohito" 17 dòng (2473, 2455, 2834, 2922, 3555, 3461, 3706, 3790, 2640, 2361, 2765, 2941, 3743, 3003, 2960, 2316, 2638 — riêng 2960 chỉ sửa đại từ, "Ohito" trong đó vẫn chờ thống nhất), "Tuyến Yui" (湯医線) 7 dòng (2796, 2839, 2260, 2270, 2484, 2776, 2912), "đèo Kobata" (小畑) 1 dòng (3010).
- Soutetsu sạch thêm (đã kiểm chứng, không sửa): "anh"/"em" với Olivy (2755, 2786, 2294, 2914, 2891, 2676, 3008, 2542), "anh" với Paulette (3055, 2296), "tôi" ở độc thoại/nhóm (2665, 2336). Dạng số nhiều "bọn anh" (2842, 2775) và "Chúng anh" (3075) giữ nguyên theo quy tắc nhóm.

## Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix vs JP)

- Tổng: 42 / kiểm chứng lại: 42 / bỏ: 0 / sửa: 0.
- Khối TOML đã parse-verified (tomllib): 42 khóa, 0 sai lệch giá trị so với JSON. jp/tw/old_vn khớp CSV3 tuyệt đối 42/42. Mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (diff-sanity đã chạy máy: fragment thay thế xuất hiện đúng 1 lần trong VN cũ).

## Danh sách sửa (42)

### 1728 — ハチロク [thuật ngữ]

- JP: 「『まくらぎけい[ざい]材要確認』『微細な[ふりく,1]不陸』\n『可変パッド推奨』……これは\x%l保線;#00ffc040;保線%l;#;の専門用語ですね」
- TW: 「“枕距護板需檢查”、“些許空吊”、“建議使用可調撐墊”……這些都是\x%l保線;#00ffc040;巡線%l;#;的專業術語吧」
- VN cũ: 「'Cần kiểm tra vật liệu nối tà vẹt', 'Có dấu hiệu hụt đất nhỏ',\n'Khuyến nghị dùng tấm đệm lót thay đổi'……Đây là thuật ngữ chuyên ngành của \x%l保線;#00ffc040;bảo trì đường ray%l;#; nhỉ.」
- Sửa: 「'Cần kiểm tra vật liệu nối tà vẹt', 'Có dấu hiệu hụt đất nhỏ',\n'Khuyến nghị dùng tấm đệm lót có thể điều chỉnh'……Đây là thuật ngữ chuyên ngành của \x%l保線;#00ffc040;bảo trì đường ray%l;#; nhỉ.」
- Lý do: 可変 = có thể điều chỉnh (TW 可調撐墊); "tấm đệm lót thay đổi" dịch sát chữ 可変 thành "thay đổi" gây hiểu nhầm. Bằng chứng trong chính file này: 2322 dịch đúng là "Đệm lót có thể điều chỉnh".

### 2233 — 双鉄 [đại từ]

- JP: 「まずは、ハチロクのレビューをもらえるか？\n僕も聞きたい」
- TW: 「不妨先聽聽八六的看法吧？說實話我也很好奇你會怎樣評價」
- VN cũ: 「Trước tiên, cho anh nghe nhận xét của Hachiroku được không?\nAnh cũng muốn nghe.」
- Sửa: 「Trước tiên, cho tôi nghe nhận xét của Hachiroku được không?\nTôi cũng muốn nghe.」
- Lý do: Soutetsu hỏi nhận xét CỦA Hachiroku, người nghe là Hachiroku → "tôi" theo quy tắc đã sửa (Paulette trả lời ở 1711, Hachiroku đáp ở 2571).

### 2267 — オリヴィ [gasp っ]

- JP: 「っ！！？」
- TW: 「什！！？」
- VN cũ: 「っ!!?」
- Sửa: 「Ư!!?」
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư.

### 2382 — 双鉄 [gasp っ]

- JP: 「っ！」
- TW: 「呃！」
- VN cũ: 「っ!」
- Sửa: 「Ư!」
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư.

### 2431 — ハチロク [xưng hô]

- JP: 「あ！」\n「あうっ、それもそうですよね、すみません」
- TW: 「啊！」\n「啊嗚，這倒也是，對不起」
- VN cũ: 「A!」\n「A ư, đúng là vậy nhỉ, xin lỗi anh.」
- Sửa: 「A!」\n「A ư, đúng là vậy nhỉ, xin lỗi ạ.」
- Lý do: Hachiroku xin lỗi Soutetsu; cô gọi Soutetsu là "ngài Soutetsu" (3085, 2581, 3079), không bao giờ gọi "anh". JP không có từ xưng hô, VN cũ tự thêm "anh" là sai. Bỏ "anh", giữ "xin lỗi ạ".

### 2439 — 双鉄 [gasp っ]

- JP: 「っ！！！？」\n「なにっ！？」
- TW: 「啊！！！？」\n「什麼！？」
- VN cũ: 「!!!?」\n「Gì vậy!?」
- Sửa: 「Ư!!!?」\n「Gì vậy!?」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng vs JP: dòng gasp cả dòng, VN chỉ còn dấu câu. Dòng 2 「なにっ！？」 giữ nguyên — っ cuối câu gắn với từ là nhấn mạnh, không phải gasp.

### 2443 — 双鉄 [gasp っ]

- JP: 「っ！？」
- TW: 「啊！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng vs JP: dòng gasp cả dòng, VN chỉ còn dấu câu.

### 2449 — 双鉄 [đại từ]

- JP: 「ああ、微妙な話題と感じていたので、\n言うタイミングを計っていた」
- TW: 「啊，我覺得這話題有點不太合適，就一直在找開口的時機」
- VN cũ: 「Ừ, vì tôi cảm thấy đây là một chủ đề nhạy cảm,\nnên vẫn đang canh thời điểm để nói.」
- Sửa: 「Ừ, vì anh cảm thấy đây là một chủ đề nhạy cảm,\nnên vẫn đang canh thời điểm để nói.」
- Lý do: Soutetsu nói với Paulette (2806 Paulette hỏi, 2449 Soutetsu đáp) → "anh".

### 2459 — オリヴィ [gasp っ]

- JP: 「っ！　ソーテツもハチロクとおんなじでしょ！？\nオリヴィたちのことなんて、わかるわけないっ」
- TW: 「嗚！雙鐵你和八六不也都一樣！根本就不理解像奧莉薇這樣的鐵路人偶的感受」
- VN cũ: 「っ! Anh Soutetsu cũng giống Hachiroku thôi!\nLàm sao mà hiểu được cảm giác của bọn Olivy chứ.」
- Sửa: 「Ư! Anh Soutetsu cũng giống Hachiroku thôi!\nLàm sao mà hiểu được cảm giác của bọn Olivy chứ.」
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ đầu dòng còn sót trong VN, diễn thành Ư. っ cuối dòng 2 (わかるわけないっ) là nhấn mạnh, giữ nguyên. Lưu ý: sweep ghi old_vn đã làm phẳng `\n` thành khoảng trắng; fix lấy theo old_vn của CSV3 (giữ `\n` literal).

### 2475 — 双鉄 [đại từ]

- JP: 「ああ、それは僕も感じる」
- TW: 「嗯，我也這麼覺得」
- VN cũ: 「À, tôi cũng cảm thấy vậy.」
- Sửa: 「À, anh cũng cảm thấy vậy.」
- Lý do: Soutetsu đáp Paulette (2693 Paulette hỏi "Olivy rất giỏi truyền đạt nhỉ?") → "anh".

### 2476 — 双鉄 [đại từ]

- JP: 「いや、何ほどのこともない。\nただ――少しぼんやりしてしまっただけだ」
- TW: 「嗯，我很好，沒事。只是——稍微有點走神了」
- VN cũ: 「Không, không có gì đâu.\nChỉ là――anh hơi thẫn thờ một chút thôi.」
- Sửa: 「Không, không có gì đâu.\nChỉ là――tôi hơi thẫn thờ một chút thôi.」
- Lý do: Soutetsu đáp Hachiroku (3085 Hachiroku: 「双鉄さま？　いかがされました？」) → "tôi".

### 2564 — ハチロク [sai nghĩa]

- JP: 「『どっちとも乗りたくて選べないから、くじ引き』と。\nうふふっ、本当にオリヴィちゃんらしい気の遣い方です」
- TW: 「她說“兩個都想要實在選不出，所以就抽籤吧”。嘻嘻，還真是奧莉薇的處事風格」
- VN cũ: 「'Vì ai cũng muốn đi cùng nên không chọn được, rút thăm thôi'.\nUfufu, đúng là cách quan tâm rất ra dáng bé Olivy.」
- Sửa: 「'Vì muốn đi cùng cả hai nên không chọn được, rút thăm thôi'.\nUfufu, đúng là cách quan tâm rất ra dáng bé Olivy.」
- Lý do: JP chủ ngữ là Olivy (どっちとも乗りたくて = muốn đi cùng cả hai); VN cũ đảo chủ ngữ thành "ai cũng muốn đi cùng" (mọi người muốn đi). TW xác nhận: "兩個都想要" (muốn cả hai).

### 2605 — オリヴィ [thuật ngữ]

- JP: 「オリヴィ、[メリケン,2]冥国式だから――マスターがいないから！\nいらなくなったら、すぐにぽいって捨てられてっ！！」
- TW: 「就因為奧莉薇是美國式！沒有定組的司機！用不到了就馬上說丟就丟！！」
- VN cũ: 「Vì Olivy là kiểu Mỹ——vì không có Master!\nNên hễ không cần nữa là lập tức bị vứt bỏ không thương tiếc!!」
- Sửa: 「Vì Olivy là kiểu Meriken——vì không có Master!\nNên hễ không cần nữa là lập tức bị vứt bỏ không thương tiếc!!」
- Lý do: Thuật ngữ đã chốt: 冥国 = "Minh Quốc", riêng furigana メリケン khi được nói ra thì giữ "Meriken". Dòng này có furigana [メリケン,2] → "Meriken". (TW dịch 美國式 nhưng JP thắng TW; "kiểu Mỹ" cũng trái bảng thuật ngữ.)

### 2663 — 双鉄 [đại từ]

- JP: 「まいてつになるためには金が必要で、\nお前には、その金を稼ぐ手段があるといっているのだ」
- TW: 「成為掌車人需要資金，而你有獲取這些資金的手段」
- VN cũ: 「Để trở thành chủ tàu thì cần tiền,\nvà tôi đang nói là cô có cách để kiếm số tiền đó.」
- Sửa: 「Để trở thành chủ tàu thì cần tiền,\nvà anh đang nói là cô có cách để kiếm số tiền đó.」
- Lý do: Soutetsu nói với Olivy → tự xưng "anh". "Cô" (JP おまえ) giữ nguyên — xem điểm chờ Hieu dưới đây.

### 2667 — 双鉄 [đại từ]

- JP: 「僕もそこを疑問に思った。というか、\n実戦形式で訓練した方が成長もよほど早かろう」
- TW: 「我也對此頗有疑問。而且話說回來，實習訓練的進步速度遠比單純的學習更快吧」
- VN cũ: 「Anh cũng thắc mắc điều đó. Hơn nữa,\nhuấn luyện thực tế thì tiến bộ sẽ nhanh hơn nhiều chứ.」
- Sửa: 「Tôi cũng thắc mắc điều đó. Hơn nữa,\nhuấn luyện thực tế thì tiến bộ sẽ nhanh hơn nhiều chứ.」
- Lý do: "僕も" đáp trực tiếp câu hỏi của Hachiroku (2692: 「なぜ、わたくしたちに内緒で？」), Hachiroku tán thành tiếp ở 3080 → người nghe là Hachiroku → "tôi".

### 2679 — 双鉄 [đại từ]

- JP: 「僕は知らん。\nだが、試しもしないうちから諦めるのは愚かしかろう」
- TW: 「我其實還不知道。但連試都不試就放棄未免太不明智」
- VN cũ: 「Tôi không biết.\nNhưng chưa thử mà đã bỏ cuộc thì thật ngốc nghếch.」
- Sửa: 「Anh không biết.\nNhưng chưa thử mà đã bỏ cuộc thì thật ngốc nghếch.」
- Lý do: Soutetsu nói với Olivy (3012 Reina hỏi, 2679 Soutetsu đáp Olivy đang khóc lóc) → "anh".

### 2685 — 双鉄 [đại từ]

- JP: 「考えてはいる、つもり、だが――」
- TW: 「我是有想考慮的，只是——」
- VN cũ: 「Tôi có định nghĩ đến, nhưng——」
- Sửa: 「Anh có định nghĩ đến, nhưng——」
- Lý do: Soutetsu đáp Olivy (2299 Olivy: 「ソーテツ、ちゃんと考えてるの？」) → "anh".

### 2688 — 双鉄 [đại từ]

- JP: 「と、僕は信じる。もしもまだ、誰も研究していないなら、\nその研究をはじめるように、僕らが提唱すればいい」
- TW: 「我相信可以。如果真的還沒有人著手這方面的研究的話，那就由我們來提出，我們來發起這項研究就好了」
- VN cũ: 「Tôi tin là vậy. Nếu vẫn chưa có ai nghiên cứu,\nthì chúng ta cứ việc đề xướng để bắt đầu nghiên cứu đó là được.」
- Sửa: 「Anh tin là vậy. Nếu vẫn chưa có ai nghiên cứu,\nthì chúng ta cứ việc đề xướng để bắt đầu nghiên cứu đó là được.」
- Lý do: Soutetsu nói với Olivy (2549 Olivy hỏi "thực sự kéo dài được sao?") → "anh".

### 2689 — 双鉄 [đại từ]

- JP: 「僕が走れば――\n走れない者は置き去りになってしまうのではないのか？」
- TW: 「我繼續馳騁的話——那不是就要把跑不快的人丟下了嗎？」
- VN cũ: 「Nếu tôi chạy――\nChẳng phải những người không chạy được sẽ bị bỏ lại phía sau sao?」
- Sửa: 「Nếu anh chạy――\nChẳng phải những người không chạy được sẽ bị bỏ lại phía sau sao?」
- Lý do: Soutetsu hỏi Paulette (2894 Paulette đáp) → "anh".

### 2709 — ポーレット [xưng hô]

- JP: 「だから、わたしは。わたしの立場からいったら、\n双鉄くんには、気にせず走ってほしいです」
- TW: 「所以以我的立場來說的話，我希望你不要被這些干擾，不要停下馳騁的腳步」
- VN cũ: 「Nên tôi. Từ lập trường của tôi mà nói,\ntôi muốn cậu Soutetsu cứ mặc kệ mà tiếp tục chạy.」
- Sửa: 「Nên tôi. Từ lập trường của tôi mà nói,\ntôi muốn anh Soutetsu cứ mặc kệ mà tiếp tục chạy.」
- Lý do: Paulette→Soutetsu: 双鉄くん → "anh Soutetsu" theo B4 lock (không có ngoại lệ).

### 2710 — 双鉄 [đại từ]

- JP: 「だから、聞かせてくれ。\nオリヴィが仮に機能停止をした場合――」
- TW: 「所以可以告訴我嗎，假如奧莉薇停止活動了的話——」
- VN cũ: 「Vì vậy, hãy cho tôi biết.\nGiả sử Olivy ngừng hoạt động――」
- Sửa: 「Vì vậy, hãy cho anh biết.\nGiả sử Olivy ngừng hoạt động――」
- Lý do: Soutetsu hỏi Paulette (quyết định kinh doanh của cô ấy) → "anh".

### 2713 — オリヴィ [sai nghĩa]

- JP: 「だから、たくさんメイワクかけないよーに、\n一番少ないひとたちだけに、きっと相談したんだよ」
- TW: 「所以她為了儘可能少給大家添麻煩，才沒有讓更多的人知道」
- VN cũ: 「Thế nên, để không gây nhiều rắc rối,\nchắc chắn em ấy chỉ bàn bạc với những người ít liên quan nhất thôi.」
- Sửa: 「Thế nên, để không gây nhiều rắc rối,\nchắc chắn em ấy chỉ bàn bạc với vài người thôi.」
- Lý do: 一番少ないひとたち = những người ít nhất (số lượng ít nhất), không phải "ít liên quan nhất". TW xác nhận: "才沒有讓更多的人知道" (không để nhiều người biết). VN cũ bịa thêm nghĩa "ít liên quan".

### 2715 — ポーレット [xưng hô]

- JP: 「だから、そんなことは言わないで。\nけど、双鉄くんには、そのまま走ってほしいんです」
- TW: 「所以我們不去說這樣的話就好了。但與此同時，我也希望雙鐵君不要停下馳騁的腳步」
- VN cũ: 「Vì vậy, đừng nói những lời như thế.\nNhưng tôi muốn cậu Soutetsu cứ tiếp tục chạy như vậy.」
- Sửa: 「Vì vậy, đừng nói những lời như thế.\nNhưng tôi muốn anh Soutetsu cứ tiếp tục chạy như vậy.」
- Lý do: Paulette→Soutetsu: 双鉄くん → "anh Soutetsu" theo B4 lock.

### 2819 — 双鉄 [đại từ]

- JP: 「確かに、わかるなどとは言えない。\nオリヴィのことを、僕はまだ、ほとんど知らない」
- TW: 「沒錯，我的確沒辦法強說自己理解。對奧莉薇，我也還知之甚少」
- VN cũ: 「Đúng là tôi không thể nói là mình hiểu được.\nTôi vẫn chưa biết nhiều về Olivy.」
- Sửa: 「Đúng là anh không thể nói là mình hiểu được.\nAnh vẫn chưa biết nhiều về Olivy.」
- Lý do: Soutetsu đáp Olivy (2459 Olivy: 「ソーテツもハチロクとおんなじでしょ！？」) → "anh".

### 2836 — 双鉄 [đại từ]

- JP: 「ポーレット！　水だ！\nバケツにいっぱいの水を頼む！」
- TW: 「波萊特！水！快去打桶水來」
- VN cũ: 「Paulette! Nước!\nLấy cho tôi một xô nước đầy!」
- Sửa: 「Paulette! Nước!\nLấy cho anh một xô nước đầy!」
- Lý do: Soutetsu gọi Paulette lấy nước (2566 Paulette đáp) → "anh".

### 2866 — れいな [thuật ngữ]

- JP: 「れいな、[めいこくしき,2]冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;のこと、\n勘違いしてたって思いましたですよぉ」
- TW: 「玲奈感覺，自己誤解了美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;了」
- VN cũ: 「Reina nghĩ là, mình đã hiểu lầm\nvề \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ rồi á~」
- Sửa: 「Reina nghĩ là, mình đã hiểu lầm\nvề \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc rồi á~」
- Lý do: Thuật ngữ đã chốt: 冥国 = "Minh Quốc". Furigana ở đây là めいこくしき (không phải メリケン) nên dùng "Minh Quốc". TW dịch 美國式 nhưng JP thắng TW.

### 2879 — 双鉄 [đại từ]

- JP: 「確かに……完全に同じではない。\nしかし、だからといってオリヴィのことを」
- TW: 「的確……不可能完全一樣。但這並不是說我就不重視你……」
- VN cũ: 「Đúng là... không hoàn toàn giống nhau.\nNhưng, không có nghĩa là tôi coi thường Olivy...」
- Sửa: 「Đúng là... không hoàn toàn giống nhau.\nNhưng, không có nghĩa là anh coi thường Olivy...」
- Lý do: Soutetsu nói với Olivy (2615 Olivy vừa nói "đâu có giống nhau") → "anh". Lưu ý: câu JP dở dang, VN hoàn thiện theo TW (但這並不是說我就不重視你) — không phải bịa, xem điểm chờ Hieu.

### 2929 — ポーレット [xưng hô]

- JP: 「そうですか？　それなら、双鉄くんにお任せします。\nでも、できるだけ無理のない範囲で」
- TW: 「至於嗎？不過既然雙鐵君都這麼說了，那就交給你吧。不過也儘量不要勉強自己哦」
- VN cũ: 「Vậy sao? Nếu thế thì nhờ cả vào cậu Soutetsu nhé.\nNhưng hãy cố gắng làm trong khả năng thôi.」
- Sửa: 「Vậy sao? Nếu thế thì nhờ cả vào anh Soutetsu nhé.\nNhưng hãy cố gắng làm trong khả năng thôi.」
- Lý do: Paulette nói TRỰC TIẾP với Soutetsu (双鉄くんにお任せします = giao cho cậu ấy) → "anh Soutetsu" theo B4 lock.

### 2944 — 双鉄 [đại từ]

- JP: 「そういえば、みかん鉄道で聞いてきたのだ」
- TW: 「說起來，我在橙鐵路那邊有所耳聞」
- VN cũ: 「Nhắc mới nhớ, tôi có nghe được chuyện này ở Đường sắt Mikan.」
- Sửa: 「Nhắc mới nhớ, anh có nghe được chuyện này ở Đường sắt Mikan.」
- Lý do: Soutetsu nói với Paulette (2806 Paulette hỏi, 2944 Soutetsu đáp) → "anh".

### 2949 — 双鉄 [đại từ]

- JP: 「助かる。いくぞ、オリヴィ。\nハチロクもついてきてくれ」
- TW: 「謝謝。奧莉薇，我們走。八六你也一起來」
- VN cũ: 「Giúp tôi nhiều lắm. Đi thôi, Olivy.\nHachiroku cũng đi theo tôi nhé.」
- Sửa: 「Giúp anh nhiều lắm. Đi thôi, Olivy.\nHachiroku cũng đi theo tôi nhé.」
- Lý do: Một dòng, hai người nghe khác nhau. 助かる cảm ơn Paulette (3072 Paulette vừa cho hạ cánh trên đường ray) → "Giúp anh". Vế sau gọi Hachiroku đi theo → "đi theo tôi" giữ nguyên "tôi". Chỉ sửa vế đầu.

### 2960 — 双鉄 [đại từ]

- JP: 「御一夜鉄道の一員として、御一夜鉄道のまいてつとして、\nポーレットだけがその決断の責を負うべきとは思わん」
- TW: 「身為御一夜鐵路的一員，同時也是御一夜鐵路的掌車人，我不認為應該讓你一個人為這個決定負責」
- VN cũ: 「Với tư cách là một thành viên của Đường sắt Ohito, là chủ tàu của Đường sắt Ohito,\ntôi không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」
- Sửa: 「Với tư cách là một thành viên của Đường sắt Ohito, là chủ tàu của Đường sắt Ohito,\nanh không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」
- Lý do: Soutetsu nói với Paulette → "anh". "Đường sắt Ohito" trong dòng này KHÔNG sửa — chờ đợt thống nhất.

### 3023 — 双鉄 [gasp っ]

- JP: 「っ！？」
- TW: 「這！？」
- VN cũ: 「っ!?」
- Sửa: 「Ư!?」
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư.

### 3024 — 双鉄 [đại từ]

- JP: 「ポーレットが\x%l保線;#00ffc040;保線%l;#;まで手を出すのはオーバーワークだ。\nそこは、\x%l保線部長;#00ffc040;保線部長%l;#;たる僕に任せてほしい」
- TW: 「連\x%l保線;#00ffc040;巡線%l;#;都要波萊特來做的話這實在太過勞累了。還是交給身為\x%l保線部長;#00ffc040;巡線部長%l;#;的我來處理吧」
- VN cũ: 「Paulette mà nhúng tay vào cả việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; thì quá sức đấy.\nChuyện đó, hãy giao cho tôi, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.」
- Sửa: 「Paulette mà nhúng tay vào cả việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; thì quá sức đấy.\nChuyện đó, hãy giao cho anh, \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.」
- Lý do: Soutetsu nói với Paulette (2929 Paulette đáp) → "anh".

### 3026 — オリヴィ [sai nghĩa]

- JP: 「オリヴィ、壊れそうに――\nもういらないこに、ソーテツの目にも、見えるの？」
- TW: 「連雙鐵都覺得，奧莉薇——已經要壞了，沒有用處了，是嗎？」
- VN cũ: 「Ngay cả anh Soutetsu cũng thấy... Olivy sắp hỏng,\nkhông còn giá trị lợi dụng nữa sao?」
- Sửa: 「Ngay cả anh Soutetsu cũng thấy... Olivy sắp hỏng,\nkhông còn cần đến nữa sao?」
- Lý do: もういらないこ = đứa trẻ không còn cần đến nữa; TW 沒有用處 (không còn tác dụng). "Giá trị lợi dụng" thêm hàm ý bóc lột không có trong JP/TW.

### 3057 — ポーレット [thuật ngữ]

- JP: 「それが、[ふりく,1]不陸の原因なのかもしれませんね。\nで、可変パッドは、それを調整できる資材だそうですよ」
- TW: 「那或許就是造成空吊的原因。然後可調撐墊就是可以對形成空吊的縫隙進行支撐、填補的材料」
- VN cũ: 「Đó có lẽ là nguyên nhân gây ra hụt đất nhỉ.\nVà tấm đệm lót thay đổi là vật liệu có thể điều chỉnh được điều đó đấy.」
- Sửa: 「Đó có lẽ là nguyên nhân gây ra hụt đất nhỉ.\nVà tấm đệm lót có thể điều chỉnh là vật liệu có thể điều chỉnh được điều đó đấy.」
- Lý do: Như 1728 — 可変 = có thể điều chỉnh (TW 可調撐墊); trong chính file này 2322 dịch đúng là "Đệm lót có thể điều chỉnh".

### 3062 — 双鉄 [đại từ]

- JP: 「それは――オリヴィの指摘を無視しろ、\nということか？」
- TW: 「那是說——要我無視奧莉薇的批評的意思嗎？」
- VN cũ: 「Ý cô là――bảo tôi phớt lờ lời phê bình của Olivy sao?」
- Sửa: 「Ý cô là――bảo anh phớt lờ lời phê bình của Olivy sao?」
- Lý do: Soutetsu hỏi Paulette (2709 Paulette vừa nói "cứ mặc kệ mà chạy") → "anh". "Cô" gọi Paulette giữ nguyên (mẫu tôi–cô của file với Paulette là "anh–cô").

### 3078 — ポーレット [xưng hô]

- JP: 「双鉄くんも、ハチロクちゃんも、大きな傷を乗り越えて――だから、今、走れてるわけじゃないですか」
- TW: 「雙鐵君和八六都是跨越了曾經的創傷，如今才能縱情馳騁，不是嗎」
- VN cũ: 「Cậu Soutetsu và Hachiroku đều đã vượt qua vết thương lòng lớn lao――nên bây giờ mới có thể chạy được, không phải sao.」
- Sửa: 「Anh Soutetsu và Hachiroku đều đã vượt qua vết thương lòng lớn lao――nên bây giờ mới có thể chạy được, không phải sao.」
- Lý do: Paulette→Soutetsu: 双鉄くん → "anh Soutetsu" theo B4 lock.

### 3326 — monologue [gasp っ]

- JP: キッチンではない――なら――っ！！？
- TW: 不是廚房那邊——那難道是！！？
- VN cũ: Không phải ở nhà bếp――vậy thì――!!?
- Sửa: Không phải ở nhà bếp――vậy thì――Ư!!?
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ, VN giữ dấu gạch nhưng mất gasp.

### 3501 — monologue [thuật ngữ]

- JP: 冥国式という特性を覆し、ハチロクに賞賛されるに至った\nオリヴィという\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を、その克己心を信じよう。
- TW: 奧莉薇克服了她美國式的特徵，甚至在工作上能令八六都讚不絕口，我選擇相信她的自制力。
- VN cũ: （Hãy tin vào một \x%lレイルロオド;#00ffc040;Railord%l;#; tên Olivy,\nngười đã vượt qua đặc tính kiểu Mỹ và được Hachiroku khen ngợi, tin vào tinh thần kiềm chế của cô ấy.）
- Sửa: （Hãy tin vào một \x%lレイルロオド;#00ffc040;Railord%l;#; tên Olivy,\nngười đã vượt qua đặc tính kiểu Minh Quốc và được Hachiroku khen ngợi, tin vào tinh thần kiềm chế của cô ấy.）
- Lý do: 冥国式 không có furigana → "kiểu Minh Quốc" theo thuật ngữ đã chốt (TW dịch 美國式 nhưng JP thắng TW).

### 3512 — monologue [thuật ngữ]

- JP: 冥語の鋭い叫びとともに、\n差し伸べられたハチロクの手がはねのけられる。
- TW: 奧莉薇邊用英語尖叫著，邊推開了八六伸過來的手。
- VN cũ: （Cùng với tiếng thét chói tai bằng tiếng Mỹ,\ncô ấy hất văng bàn tay đang chìa ra của Hachiroku.）
- Sửa: （Cùng với tiếng thét chói tai bằng tiếng Minh Quốc,\ncô ấy hất văng bàn tay đang chìa ra của Hachiroku.）
- Lý do: 冥語 = ngôn ngữ của 冥国 → "tiếng Minh Quốc" theo bảng thuật ngữ (冥国 = "Minh Quốc"). "Tiếng Mỹ" không phải tên một ngôn ngữ; TW ghi 英語 (tiếng Anh) vì trong truyện đó là tiếng Anh, nhưng bảng thuật ngữ của dự án chốt "Minh Quốc" cho 冥国.

### 3611 — monologue [gasp っ]

- JP: ハチロクとともに抱きとめ――っ！！？
- TW: 我和八六一起抱住了奧莉薇——這！！？
- VN cũ: （Tôi cùng Hachiroku vội vàng đỡ lấy cô ấy——!!?）
- Sửa: （Tôi cùng Hachiroku vội vàng đỡ lấy cô ấy——Ư!!?）
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ, VN giữ dấu gạch nhưng mất gasp.

### 3740 — monologue [thuật ngữ]

- JP: 確かに、冥国式であろうとなんであろうと、マスターが\nⅨ号ごとオリヴィを買い取れるのなら、まいてつだ。
- TW: 的確，不管是不是美國式，如果有司機把九號和奧莉薇一起買下的話，那就是掌車人了。
- VN cũ: （Quả thực, bất kể là kiểu Mỹ hay gì đi nữa, nếu Master\ncó thể mua lại cả đầu máy số 9 lẫn Olivy, thì đó chính là chủ tàu.）
- Sửa: （Quả thực, bất kể là kiểu Minh Quốc hay gì đi nữa, nếu Master\ncó thể mua lại cả đầu máy số 9 lẫn Olivy, thì đó chính là chủ tàu.）
- Lý do: 冥国式 không có furigana → "kiểu Minh Quốc" theo thuật ngữ đã chốt.

## Chờ Hieu (không tự quyết — cờ lại, không tính sai)

- **2262** — Soutetsu: 「あやまるようなことでもないとも思うが」 → VN "Anh nghĩ cũng không đến mức phải xin lỗi đâu." Người nghe lẫn cả Hachiroku VÀ Paulette (cả hai cùng xin lỗi ở 2431, char ハチロク＆波萊特). Với Hachiroku thì Soutetsu là "tôi", với Paulette là "anh" — không xác định được một người nghe duy nhất nên GIỮ NGUYÊN "anh". Cần Hieu xem có muốn đổi không.
- **2539 / 2757 / 2663** — Soutetsu gọi Olivy là "cô" thay vì "em" như thường lệ (JP おまえ, giọng gay gắt khi đang mắng Olivy: 「オリヴィ。おまえは――」「ならば何故、その残り少ないかもしれぬ時間を。泣いて喚いて、無駄に使うのだ」). "Cô" có vẻ là chuyển thanh điệu có chủ ý của người dịch để thể hiện sự lạnh lùng, nên GIỮ NGUYÊN cả 3 dòng. Cần Hieu chốt: giữ "cô" ở đoạn gay gắt này, hay thống nhất "em" cho mọi chỗ Soutetsu→Olivy. (Riêng 2663 đã sửa "tôi"→"anh" vì tự xưng "anh" là đúng với Olivy dù gọi cô ấy là "cô" hay "em".)
- **2879** — Câu JP dở dang 「しかし、だからといってオリヴィのことを」; VN hoàn thiện thành "...không có nghĩa là anh coi thường Olivy" — hoàn thiện này lấy theo TW (但這並不是說我就不重視你), không phải bịa. Chỉ sửa đại từ "tôi"→"anh".
- **2557** — Hachiroku gọi Olivy "cậu" (「オリヴィちゃん――あなたは――あの機関士さん……」) trong khi các chỗ khác trong file cô gọi Olivy là "chị/bé Olivy" (2880, 2668, 2489). JP あなた trung tính; "cậu" là cách xưng ngang hàng có thể chấp nhận được nên GIỮ NGUYÊN, chỉ ghi chú.
- **2842 / 2775 / 3075** — Dạng số nhiều "bọn anh" / "Chúng anh" giữ nguyên theo quy tắc nhóm (không bị quy tắc số ít chi phối).
- **3512** — 冥語 → "tiếng Minh Quốc" theo bảng thuật ngữ; TW dịch là 英語 (tiếng Anh) vì tiếng hét trong truyện là tiếng Anh ("Don't touch!!!!"). Nếu Hieu muốn giữ "tiếng Anh" cho dễ hiểu thì báo lại.

## Khối TOML (đã parse-verified, 42 khóa, 0 sai lệch)

```toml
[script]
"1728" = "「'Cần kiểm tra vật liệu nối tà vẹt', 'Có dấu hiệu hụt đất nhỏ',\\n'Khuyến nghị dùng tấm đệm lót có thể điều chỉnh'……Đây là thuật ngữ chuyên ngành của \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nhỉ.」"
"2233" = "「Trước tiên, cho tôi nghe nhận xét của Hachiroku được không?\\nTôi cũng muốn nghe.」"
"2267" = "「Ư!!?」"
"2382" = "「Ư!」"
"2431" = "「A!」\\n「A ư, đúng là vậy nhỉ, xin lỗi ạ.」"
"2439" = "「Ư!!!?」\\n「Gì vậy!?」"
"2443" = "「Ư!?」"
"2449" = "「Ừ, vì anh cảm thấy đây là một chủ đề nhạy cảm,\\nnên vẫn đang canh thời điểm để nói.」"
"2459" = "「Ư! Anh Soutetsu cũng giống Hachiroku thôi!\\nLàm sao mà hiểu được cảm giác của bọn Olivy chứ.」"
"2475" = "「À, anh cũng cảm thấy vậy.」"
"2476" = "「Không, không có gì đâu.\\nChỉ là――tôi hơi thẫn thờ một chút thôi.」"
"2564" = "「'Vì muốn đi cùng cả hai nên không chọn được, rút thăm thôi'.\\nUfufu, đúng là cách quan tâm rất ra dáng bé Olivy.」"
"2605" = "「Vì Olivy là kiểu Meriken——vì không có Master!\\nNên hễ không cần nữa là lập tức bị vứt bỏ không thương tiếc!!」"
"2663" = "「Để trở thành chủ tàu thì cần tiền,\\nvà anh đang nói là cô có cách để kiếm số tiền đó.」"
"2667" = "「Tôi cũng thắc mắc điều đó. Hơn nữa,\\nhuấn luyện thực tế thì tiến bộ sẽ nhanh hơn nhiều chứ.」"
"2679" = "「Anh không biết.\\nNhưng chưa thử mà đã bỏ cuộc thì thật ngốc nghếch.」"
"2685" = "「Anh có định nghĩ đến, nhưng——」"
"2688" = "「Anh tin là vậy. Nếu vẫn chưa có ai nghiên cứu,\\nthì chúng ta cứ việc đề xướng để bắt đầu nghiên cứu đó là được.」"
"2689" = "「Nếu anh chạy――\\nChẳng phải những người không chạy được sẽ bị bỏ lại phía sau sao?」"
"2709" = "「Nên tôi. Từ lập trường của tôi mà nói,\\ntôi muốn anh Soutetsu cứ mặc kệ mà tiếp tục chạy.」"
"2710" = "「Vì vậy, hãy cho anh biết.\\nGiả sử Olivy ngừng hoạt động――」"
"2713" = "「Thế nên, để không gây nhiều rắc rối,\\nchắc chắn em ấy chỉ bàn bạc với vài người thôi.」"
"2715" = "「Vì vậy, đừng nói những lời như thế.\\nNhưng tôi muốn anh Soutetsu cứ tiếp tục chạy như vậy.」"
"2819" = "「Đúng là anh không thể nói là mình hiểu được.\\nAnh vẫn chưa biết nhiều về Olivy.」"
"2836" = "「Paulette! Nước!\\nLấy cho anh một xô nước đầy!」"
"2866" = "「Reina nghĩ là, mình đã hiểu lầm\\nvề \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc rồi á~」"
"2879" = "「Đúng là... không hoàn toàn giống nhau.\\nNhưng, không có nghĩa là anh coi thường Olivy...」"
"2929" = "「Vậy sao? Nếu thế thì nhờ cả vào anh Soutetsu nhé.\\nNhưng hãy cố gắng làm trong khả năng thôi.」"
"2944" = "「Nhắc mới nhớ, anh có nghe được chuyện này ở Đường sắt Mikan.」"
"2949" = "「Giúp anh nhiều lắm. Đi thôi, Olivy.\\nHachiroku cũng đi theo tôi nhé.」"
"2960" = "「Với tư cách là một thành viên của Đường sắt Ohito, là chủ tàu của Đường sắt Ohito,\\nanh không nghĩ chỉ mình Paulette phải chịu trách nhiệm cho quyết định đó.」"
"3023" = "「Ư!?」"
"3024" = "「Paulette mà nhúng tay vào cả việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#; thì quá sức đấy.\\nChuyện đó, hãy giao cho anh, \\x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;.」"
"3026" = "「Ngay cả anh Soutetsu cũng thấy... Olivy sắp hỏng,\\nkhông còn cần đến nữa sao?」"
"3057" = "「Đó có lẽ là nguyên nhân gây ra hụt đất nhỉ.\\nVà tấm đệm lót có thể điều chỉnh là vật liệu có thể điều chỉnh được điều đó đấy.」"
"3062" = "「Ý cô là――bảo anh phớt lờ lời phê bình của Olivy sao?」"
"3078" = "「Anh Soutetsu và Hachiroku đều đã vượt qua vết thương lòng lớn lao――nên bây giờ mới có thể chạy được, không phải sao.」"
"3326" = "Không phải ở nhà bếp――vậy thì――Ư!!?"
"3501" = "（Hãy tin vào một \\x%lレイルロオド;#00ffc040;Railord%l;#; tên Olivy,\\nngười đã vượt qua đặc tính kiểu Minh Quốc và được Hachiroku khen ngợi, tin vào tinh thần kiềm chế của cô ấy.）"
"3512" = "（Cùng với tiếng thét chói tai bằng tiếng Minh Quốc,\\ncô ấy hất văng bàn tay đang chìa ra của Hachiroku.）"
"3611" = "（Tôi cùng Hachiroku vội vàng đỡ lấy cô ấy——Ư!!?）"
"3740" = "（Quả thực, bất kể là kiểu Minh Quốc hay gì đi nữa, nếu Master\\ncó thể mua lại cả đầu máy số 9 lẫn Olivy, thì đó chính là chủ tàu.）"
```

## Kết bài

File ハチロク05_レイルロオドたち.txt.toml: 570 dòng đã đọc hết, sai 42 dòng (7,4%). Lỗi tập trung ở 2 cụm: xưng hô/đại từ (24 — Soutetsu tự xưng "tôi" lạc sang cả 3 người nghe: với Paulette 9 dòng, với Olivy 6 dòng, với Hachiroku ngược lại "anh" 3 dòng; Paulette gọi Soutetsu "cậu Soutetsu" trái B4 lock 4 dòng) và gasp っ (8, tất cả từ sweep). Còn lại là thuật ngữ 冥国式/冥語 (5) và 2 lỗi sai nghĩa rời rạc (2713, 2564, 3026). Không có lệch dòng, chuỗi xoay hay nhiễm chéo — bản dịch file này nhìn chung trung thực, lỗi là rời rạc chứ không hệ thống. Cần Hieu xem 6 điểm đã nêu trên trước khi gộp.
