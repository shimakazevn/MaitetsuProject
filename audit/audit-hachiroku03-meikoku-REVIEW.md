# Audit — ハチロク03_冥国式レイルロオド.txt.toml

- File: `ハチロク03_冥国式レイルロオド.txt.toml` — route 01_Hachiroku, 490 dòng script (178 độc thoại, 99 thoại Soutetsu, 85 thoại Olivy, 66 thoại Hachiroku, 25 thoại Paulette, 23 thoại Hibiki, 7 thoại Nagi, 6 thoại Reina, 1 thoại Fukami).
- Nội dung: ngày đầu tiên của Olivy ở Ohitoyo — chào hỏi buổi sáng (Olivy xin lỗi vì chuyện tối qua, thống nhất cách gọi tên, Hachiroku xin lỗi vì đã đối xử với Olivy như trẻ con), ăn sáng (Soutetsu đập than cho Olivy), đến công ty (Olivy xin lỗi Paulette, được chấp nhận, nhận nhiệm vụ: đi theo chuyến tàu, nộp báo cáo, đi bộ toàn tuyến khi trời nắng, chạy thử Ⅸ号 với Soutetsu/Hibiki/Nagi luân phiên), giải thích "kiểu Meriken" (Minh Quốc) vs "kiểu Hinomoto" (Nhật Bản), phanh khẩn cấp vì hươu suýt đâm, Hachiroku tắt đèn pha theo cộng cảm "Off the light" của Olivy, kết bằng Hachiroku cảm nhận được cảm xúc tuyệt vọng đen tối của Olivy qua cộng cảm.
- **Kết quả: 58/490 dòng sai (11,8%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (490 dòng, 0 khóa trùng, 0 ô VN trống, 0 VN==TW); TOML 490 khóa script, khớp CSV3 tuyệt đối 490/490 (272 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. Không có thẻ `%l` nào sai định dạng trong VN (kiểm tra máy: số thẻ mở/đóng khớp JP từng dòng — chỉ 1 dòng VN tự thêm thẻ: 2127 機関庫, nội dung gloss đúng, chỉ ghi nhận — xem §4).
- TOML md5 `4e718f528c5de0e6aca78a3e53094ec7`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Nhiễm chéo kiểm tra máy: 0 dòng VN đặc trưng (≥25 ký tự) trong file này trùng với dòng VN ở file khác mà JP khác; trong file chỉ có VN trùng lặp hợp lệ: 「Đúng vậy.」 ×2 (2529, 2304 — đều là JP 「だな」), 「Ư!?」 ×2 sau khi sửa (2125, 2168 — đều là JP 「っ！？」).
- Soutetsu: "anh" với Hibiki (2583, 2403 đúng sẵn) và Olivy (10 dòng sửa: 1988, 2023, 2042, 2044, 2112, 2300, 2315, 2345, 2383 + 2037/2214/2238/2522/2327/2107/2470 đúng sẵn); "tôi" chỉ còn ở chỗ đúng: với Hachiroku (2039, 2216, 2386, 2368 — kèm "cô"), độc thoại "tôi" toàn file, dạng nhóm "chúng tôi"/"chúng ta". Không có "mình" làm chủ ngữ chính trong độc thoại (các "mình" còn lại đều trong mệnh đề phụ — "không biết mình có làm gì", "điều mình không thích", "của mình" — giữ theo tiền lệ).
- Hachiroku tự xưng "em" nhất quán toàn file, gọi Olivy "chị" (1 dòng sai "cô" đã sửa: 1993). Hibiki tự xưng "em" (1 dòng sai "chị" đã sửa: 2370). Olivy tự xưng "tôi" 6 dòng (1998, 2131, 2302, 2517, 2570, 2591) + "em" 1 dòng (2663) + gọi tên mình — giữ nguyên theo tiền lệ ハチロク14 (parent kiểm chứng "Olivy tự xưng 'tôi'"); Olivy gọi Soutetsu "cậu" 1 dòng (2680) giữ nguyên theo tiền lệ ハチロク06.
- Fukami chỉ 1 dòng (2152, gọi Nagi "cậu" — đúng). Nagi→Fukami không xuất hiện trong file.
- Thuật ngữ: file này đã có sẵn Teitetsu đúng 2 dòng (1988, 2337); không còn "Ohito"/"Yui"/"Mỹ" sau khi sửa. "Hinamoto" còn 10 dòng — chờ đợt thống nhất (xem §6). 運転体 "kíp lái" đã sửa thành "thân vận hành" ở 1984 (tiền lệ ハチロク07/10) — xem §6.

## §2. Danh sách sửa (58 dòng)

Phân loại: thuật ngữ 32 (Minh Quốc/Meriken 19 — furigana メリケン→"Meriken" 4, còn lại→"Minh Quốc" 15; Ohito→Ohitoyo 7 — 3272 kiêm Yui; Yui→Yunoi 2 dòng riêng; Teitetsu 1; 凪さま→"Bổn tiểu thư" 3), đại từ 10 (Soutetsu "tôi"/"cô"→"anh"/"em" với Olivy 9, Hibiki "chị"→"em" với Olivy 1), đại từ + thuật ngữ 2 (2315, 1993 — đều kiêm Yui), gasp sweep 9, sai nghĩa 2, lỗi nhỏ 1, SFX 2.

### 1528 — monologue — gasp (sweep)
- JP: “オリヴィが、みかん鉄道でどう扱われていたのか”を\n――っ！
- TW: “在橙鐵路時候大家是怎麼差使奧莉薇的”——啊！
- VN cũ: "Olivy đã bị đối xử như thế nào ở Đường sắt Mikan"\n——っ!
- Sửa: "Olivy đã bị đối xử như thế nào ở Đường sắt Mikan"\n——Ư!
- Lý do: Sweep raw-tsu: JP kết ——っ！ (gasp tuyệt đối-cuối, TW ——啊！); VN cũ để nguyên っ. Thêm Ư theo quy tắc gasp (tiền lệ 再開発 2103/2537).

### 1551 — ハチロク — thuật ngữ
- JP: 「[こちら,3]運転台内も問題なかったようですね。\nそれでは速やかに、[ゆのい,1]湯医まで回復運転につとめましょう」
- TW: 「[這邊,3]駕駛台裡也沒有問題吧。那事不宜遲，以縮減延誤模式駛向湯醫吧」
- VN cũ: 「Có vẻ như bên trong buồng lái cũng không có vấn đề gì.\nVậy thì chúng ta hãy nhanh chóng tăng tốc chạy bù giờ đến Yui thôi ạ.」
- Sửa: 「Có vẻ như bên trong buồng lái cũng không có vấn đề gì.\nVậy thì chúng ta hãy nhanh chóng tăng tốc chạy bù giờ đến Yunoi thôi ạ.」
- Lý do: JP 湯医 — thuật ngữ đã chốt: 湯医='Yunoi' (AUDIT-BRIEF). VN cũ 'Yui'.

### 1580 — ハチロク — thuật ngữ
- JP: 「……冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、日ノ本や[えいこく,1]詠国、[どっこく,1]髑国式の\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と大きく異なり、交代乗務を常とします」
- TW: 「……美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;與日本、英國、德國式有著顯著的不同，交替執行乘務任務可以說是家常便飯」
- VN cũ: 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
- Sửa: 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
- Lý do: JP 冥国式 — thuật ngữ đã chốt: 冥国='Minh Quốc' (không có furigana メリケン). VN cũ 'kiểu Mỹ'. 'kiểu Hinamoto' giữ nguyên — chờ đợt thống nhất (brief liệt kê ハチロク03 trong 36 dòng Hinamoto).

### 1984 — 双鉄 — thuật ngữ
- JP: 「\x%l運転体;#00ffc040;運転体%l;#;も\x%l整備体;#00ffc040;整備体%l;#;も無い、ワンボディなのには驚いた。\nあれは、冥国蒸機――いや」
- TW: 「不分\x%l運転体;#00ffc040;駕駛體%l;#;和\x%l整備体;#00ffc040;整備體%l;#;，所有事情都靠這副身體著實讓我意外。那也是美國蒸汽機車——不」
- VN cũ: 「Không có \x%l運転体;#00ffc040;kíp lái%l;#; hay \x%l整備体;#00ffc040;thân chính%l;#;, chỉ có một cơ thể duy nhất khiến tôi rất ngạc nhiên.\nĐó là do đầu máy hơi nước Mỹ——không phải」
- Sửa: 「Không có \x%l運転体;#00ffc040;thân vận hành%l;#; hay \x%l整備体;#00ffc040;thân bảo trì%l;#;, chỉ có một cơ thể duy nhất khiến tôi rất ngạc nhiên.\nĐó là do đầu máy hơi nước Minh Quốc——không phải」
- Lý do: JP 冥国蒸機 → 'Minh Quốc' (không furigana メリケン); JP 整備体 → 'thân bảo trì' (đã chốt); JP 運転体 → 'thân vận hành' (tiền lệ ハチロク07 1640/3135, ハチロク10). VN cũ 'Mỹ'/'thân chính'/'kíp lái'.

### 1988 — 双鉄 — đại từ
- JP: 「機器点検の手際だけでなく、\x%l投炭;#00ffc040;投炭%l;#;指示も的確だったゆえ、\n[ハチロクけい,4]8620形――帝鉄蒸機の乗務経験が豊富なのかと思ったが」
- TW: 「不只是設備清查頗為熟練，連\x%l投炭;#00ffc040;加煤%l;#;指示都精準無誤，還以為你對８６２０型——對帝國鐵路蒸汽機車有豐富的乘務經驗」
- VN cũ: 「Không chỉ thao tác kiểm tra máy móc nhanh nhẹn, mà chỉ thị \x%l投炭;#00ffc040;thêm than%l;#; cũng rất chính xác,\nnên tôi cứ tưởng cô có nhiều kinh nghiệm làm nhiệm vụ trên dòng 8620——đầu máy hơi nước của Teitetsu chứ.」
- Sửa: 「Không chỉ thao tác kiểm tra máy móc nhanh nhẹn, mà chỉ thị \x%l投炭;#00ffc040;thêm than%l;#; cũng rất chính xác,\nnên anh cứ tưởng em có nhiều kinh nghiệm làm nhiệm vụ trên dòng 8620——đầu máy hơi nước của Teitetsu chứ.」
- Lý do: Soutetsu nói với Olivy (dòng sau 2475 Olivy đáp): Soutetsu xưng 'anh', gọi Olivy 'em' — tiền lệ ハチロク05 sửa 6 dòng 'tôi'→'anh' với Olivy, ハチロク07 2418. VN cũ 'tôi'/'cô' sai.

### 1993 — ハチロク — đại từ + thuật ngữ
- JP: 「いいえ。気持ちだけで。\nオリヴィちゃんは、湯医線での初乗務でしたし」
- TW: 「不必勞煩，好意我心領了。畢竟你這才第一次在湯醫線上執行乘務任務」
- VN cũ: 「Không cần đâu ạ. Chỉ cần cô có lòng là được rồi.\nDù sao thì đây cũng là chuyến đi đầu tiên của Olivy trên tuyến Yui mà.」
- Sửa: 「Không cần đâu ạ. Chỉ cần chị có lòng là được rồi.\nDù sao thì đây cũng là chuyến đi đầu tiên của Olivy trên tuyến Yunoi mà.」
- Lý do: Hachiroku nói với Olivy: Hachiroku gọi Olivy 'chị' (Olivy lớn tuổi hơn Hachiroku — bằng chứng chính file 2582 '先輩であるオリヴィさん'; tiền lệ ハチロク06 2378 'cảm ơn cô'→'cảm ơn chị'). VN cũ 'cô' sai. Đồng thời 湯医→'Yunoi' theo thuật ngữ đã chốt.

### 2023 — 双鉄 — đại từ
- JP: 「今日はいろいろ助かった。\n礼というわけでもないが、よければどうだ？」
- TW: 「今天真是幫了我們大忙了。這是真的不成敬意，不如品嚐一下？」
- VN cũ: 「Hôm nay cô đã giúp đỡ rất nhiều.\nCũng không hẳn là quà cảm ơn, nhưng nếu cô thích thì dùng thử xem?」
- Sửa: 「Hôm nay em đã giúp đỡ rất nhiều.\nCũng không hẳn là quà cảm ơn, nhưng nếu em thích thì dùng thử xem?」
- Lý do: Soutetsu nói với Olivy (dòng sau 2591 Olivy đáp): 'anh'/'em' theo tiền lệ ハチロク05/07. VN cũ 'cô' sai.

### 2042 — 双鉄 — đại từ
- JP: 「オリヴィは、[ハチロクニイマルけい,4]8620形の乗務経験があるのか？」
- TW: 「你有８６２０型的乘務經驗嗎？」
- VN cũ: 「Olivy, cô từng làm nhiệm vụ trên dòng 8620 rồi sao?」
- Sửa: 「Olivy, em từng làm nhiệm vụ trên dòng 8620 rồi sao?」
- Lý do: Soutetsu nói với Olivy (dòng sau 2473 Olivy đáp): 'anh'/'em'. VN cũ 'cô' sai.

### 2044 — 双鉄 — đại từ
- JP: 「大丈夫――…………か？」
- TW: 「你還好——嗎？」
- VN cũ: 「Cô không sao——…………chứ?」
- Sửa: 「Em không sao——…………chứ?」
- Lý do: Soutetsu nói với Olivy (ngay sau độc thoại 3280 về tiếng rên của Olivy): 'em'. VN cũ 'Cô' sai.

### 2076 — ポーレット — thuật ngữ
- JP: 「製造は[めいじ,1]明智45年。[めいこく,1]冥国の、\nオールドウィン・ロコモーティブワークス製です」
- TW: 「出廠日期是明治４５年。製造商是美國Ａｌｄｗｉｎ　Ｌｏｃｏｍｏｔｉｖｅ　Ｗｏｒｋｓ」
- VN cũ: 「Được sản xuất vào năm Minh Trị 45. Do hãng Aldwin Locomotive Works\ncủa Mỹ chế tạo.」
- Sửa: 「Được sản xuất vào năm Minh Trị 45. Do hãng Aldwin Locomotive Works\ncủa Minh Quốc chế tạo.」
- Lý do: JP 冥国の (không furigana メリケン) → 'Minh Quốc'. VN cũ 'của Mỹ'.

### 2083 — 双鉄 — thuật ngữ
- JP: 「さっきも話に出てきたが、その[メリケン,2]冥国式というのは――」
- TW: 「剛才也說到過這個，所謂的美國式指的是——」
- VN cũ: 「Lúc nãy cũng có nhắc đến, cái gọi là kiểu Mỹ đó——」
- Sửa: 「Lúc nãy cũng có nhắc đến, cái gọi là kiểu Meriken đó——」
- Lý do: JP [メリケン,2]冥国式 — furigana メリケン là cách đọc nói → giữ 'Meriken' (quyết định 19/11; tiền lệ ハチロク05 2605). VN cũ 'kiểu Mỹ'.

### 2112 — 双鉄 — đại từ
- JP: 「しかし、つい先程、\nなにか苦しげな声を――」
- TW: 「可我剛才聽你聲音好像很痛苦的樣子——」
- VN cũ: 「Nhưng mà, lúc nãy,\ntôi nghe thấy giọng cô có vẻ rất đau đớn——」
- Sửa: 「Nhưng mà, lúc nãy,\nanh nghe thấy giọng em có vẻ rất đau đớn——」
- Lý do: Soutetsu nói với Olivy (dòng sau 2080 Olivy đáp): 'anh'/'em'. VN cũ 'tôi'/'cô' sai.

### 2124 — オリヴィ — gasp (sweep)
- JP: 「っ！！？」
- TW: 「咦！！？」
- VN cũ: 「っ!!?」
- Sửa: 「Ư!!?」
- Lý do: Sweep raw-tsu: JP 「っ！！？」 nguyên dòng là tiếng hít, TW 「咦！！？」; VN cũ để nguyên っ. Sửa 「Ư!!?」 (tiền lệ 再開発 2103/2537).

### 2125 — 双鉄 — gasp (sweep)
- JP: 「っ！？」
- TW: 「咦！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: Sweep lost-gasp-whole: JP 「っ！？」 nguyên dòng là tiếng hít, TW 「咦！？」; VN cũ chỉ còn dấu câu. Thêm Ư.

### 2165 — オリヴィ — gasp (sweep)
- JP: 「っ！！」
- TW: 「唔！！」
- VN cũ: 「!!」
- Sửa: 「Ư!!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！！」 nguyên dòng là tiếng hít, TW 「唔！！」; VN cũ chỉ còn dấu câu. Thêm Ư.

### 2167 — オリヴィ — gasp (sweep)
- JP: 「っ！！！！」
- TW: 「唔！！！！」
- VN cũ: 「!!!!」
- Sửa: 「Ư!!!!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！！！！」 nguyên dòng là tiếng hít, TW 「唔！！！！」; VN cũ chỉ còn dấu câu. Thêm Ư.

### 2168 — 双鉄 — gasp (sweep)
- JP: 「っ！？」
- TW: 「唔！？」
- VN cũ: 「っ!?」
- Sửa: 「Ư!?」
- Lý do: Sweep raw-tsu: JP 「っ！？」 nguyên dòng là tiếng hít, TW 「唔！？」; VN cũ để nguyên っ. Sửa 「Ư!?」.

### 2198 — 凪 — thuật ngữ
- JP: 「あう～、凪さま、めぐりあわせの悪かとばい！」
- TW: 「啊嗚～本小姐怎麼就沒這好命吶！」
- VN cũ: 「Au~, Nagi xui xẻo quá đi mất á!」
- Sửa: 「Au~, Bổn tiểu thư đây xui xẻo quá đi mất á!」
- Lý do: JP 凪さま — Nagi tự xưng; TW 本小姐. Tiền lệ 凪ふかみ01 (8 dòng) + ハチロク07 2393: 凪さま→'Bổn tiểu thư'. VN cũ bỏ hẳn さま.

### 2238 — 双鉄 — thuật ngữ
- JP: 「ああ。改めて自己紹介をさせてもらおう。\n御一夜へようこそ、オリヴィ。僕は右田双鉄だ」
- TW: 「嗯，容我重新做一次自我介紹。奧莉薇，歡迎來到御一夜。我是右田雙鐵」
- VN cũ: 「À. Để anh giới thiệu lại bản thân nhé.\nChào mừng đến Ohito, Olivy. Anh là Migita Soutetsu.」
- Sửa: 「À. Để anh giới thiệu lại bản thân nhé.\nChào mừng đến Ohitoyo, Olivy. Anh là Migita Soutetsu.」
- Lý do: JP 御一夜 — quyết định 19/11: 御一夜='Ohitoyo'. VN cũ 'Ohito'.

### 2283 — オリヴィ — thuật ngữ
- JP: 「オリヴィこそよろしく！　よろしくお願いします！\nオヒトヨのこと、大好きになれるようにがんばるから！」
- TW: 「奧莉薇才要說請多指教呢！奧莉薇會努力喜歡上御一夜的！」
- VN cũ: 「Olivy mới là người cần giúp đỡ! Mong mọi người giúp đỡ nha!\nOlivy sẽ cố gắng để trở nên yêu thích Ohito thật nhiều!」
- Sửa: 「Olivy mới là người cần giúp đỡ! Mong mọi người giúp đỡ nha!\nOlivy sẽ cố gắng để trở nên yêu thích Ohitoyo thật nhiều!」
- Lý do: JP 御一夜 — quyết định 19/11: 御一夜='Ohitoyo'. VN cũ 'Ohito'.

### 2300 — 双鉄 — đại từ
- JP: 「しっかり休んで英気を養ってくれ。\nなにか聞きたいことが出てきたら、明日改めて確認する」
- TW: 「好好休息養精蓄銳吧。如果有什麼要和你問的話就等明天好了」
- VN cũ: 「Cô cứ nghỉ ngơi cho khỏe đi.\nNếu có gì cần hỏi, ngày mai tôi sẽ xác nhận lại sau.」
- Sửa: 「Em cứ nghỉ ngơi cho khỏe đi.\nNếu có gì cần hỏi, ngày mai anh sẽ xác nhận lại sau.」
- Lý do: Soutetsu nói với Olivy (dòng sau 2705 Olivy đáp 'OK!'): 'anh'/'em'. VN cũ 'tôi'/'cô' sai.

### 2315 — 双鉄 — đại từ + thuật ngữ
- JP: 「そこまでが無事に終わったら、まずは僕と組んで、\nⅨ号機関車での湯医線の試運転。それで問題なければ」
- TW: 「如果這一切都順利結束，你就先和我搭檔，駕駛九號機車在湯醫線上進行試運營。若能順利完成……」
- VN cũ: 「Nếu mọi chuyện suôn sẻ đến đó, trước tiên cô sẽ bắt cặp với tôi,\nlái thử đầu máy số 9 trên tuyến Yui. Nếu không có vấn đề gì thì」
- Sửa: 「Nếu mọi chuyện suôn sẻ đến đó, trước tiên em sẽ bắt cặp với anh,\nlái thử đầu máy số 9 trên tuyến Yunoi. Nếu không có vấn đề gì thì」
- Lý do: Soutetsu nói với Olivy: 'anh'/'em' (tiền lệ ハチロク05/07). Đồng thời 湯医線→'tuyến Yunoi' theo thuật ngữ đã chốt.

### 2341 — ハチロク — thuật ngữ
- JP: 「[めいこくしき,2]冥国式。\nこの場合は、冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;のことでございます」
- TW: 「就是美國式。在這個場合，應該是指美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」
- VN cũ: 「Là kiểu Mỹ ạ.\nTrong trường hợp này, ý cô ấy là \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ đó ạ.」
- Sửa: 「Là kiểu Minh Quốc ạ.\nTrong trường hợp này, ý cô ấy là \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc đó ạ.」
- Lý do: JP [めいこくしき,2]冥国式 — đọc thường, không phải メリケン nói → 'Minh Quốc'. VN cũ 'kiểu Mỹ' (cả 2 chỗ).

### 2345 — 双鉄 — đại từ
- JP: 「と、いうわけだ。僕も教導\x%l機関士;#00ffc040;機関士%l;#;として添乗する。\n最終的にどちらと組むかは、総合判断になるな」
- TW: 「就是這樣囉。我作為教練\x%l機関士;#00ffc040;司機%l;#;也會一直陪同。最終會和誰成為搭檔，就要看綜合的評判結果了」
- VN cũ: 「Là vậy đó. Tôi cũng sẽ đi theo với tư cách là \x%l機関士;#00ffc040;lái tàu%l;#; hướng dẫn.\nCuối cùng cô sẽ bắt cặp với ai thì còn phải dựa vào đánh giá tổng hợp nữa.」
- Sửa: 「Là vậy đó. Anh cũng sẽ đi theo với tư cách là \x%l機関士;#00ffc040;lái tàu%l;#; hướng dẫn.\nCuối cùng em sẽ bắt cặp với ai thì còn phải dựa vào đánh giá tổng hợp nữa.」
- Lý do: Soutetsu nói với Olivy (dòng kề 2297 Olivy hỏi, 2697 Olivy đáp): 'anh'/'em'. VN cũ 'tôi'/'cô' sai.

### 2370 — 日々姫 — đại từ
- JP: 「私もそれで大歓迎！\nあらためてよろしくね、オリヴィ！」
- TW: 「我也覺得這樣很好！那就請多指教囉，奧莉薇！」
- VN cũ: 「Chị cũng rất hoan nghênh cách gọi đó!\nMột lần nữa mong được giúp đỡ nhé, Olivy!」
- Sửa: 「Em cũng rất hoan nghênh cách gọi đó!\nMột lần nữa mong được giúp đỡ nhé, Olivy!」
- Lý do: Hibiki nói với Olivy: Hibiki tự xưng 'em' — trong file 'em' 3 dòng (1979, 2442, 2466) vs 'chị' 1 dòng này; toàn dự án Hibiki với Olivy dùng 'em' (ハチロク02 1964, ハチロク13 2263, ハチロク14 2804), 0 dòng 'chị'. VN cũ 'Chị' sai.

### 2373 — ポーレット — thuật ngữ
- JP: 「御一夜鉄道株式会社の社長として。\nオリヴィさんの謝罪、受け入れさせていただきました」
- TW: 「我以御一夜鐵路股份公司社長的身份，接受奧莉薇小姐的道歉」
- VN cũ: 「Với tư cách là Giám đốc của Công ty Cổ phần Đường sắt Ohito.\nTôi xin chấp nhận lời xin lỗi của cô Olivy.」
- Sửa: 「Với tư cách là Giám đốc của Công ty Cổ phần Đường sắt Ohitoyo.\nTôi xin chấp nhận lời xin lỗi của cô Olivy.」
- Lý do: JP 御一夜鉄道 — quyết định 19/11: 御一夜='Ohitoyo'. VN cũ 'Đường sắt Ohito'.

### 2383 — 双鉄 — đại từ
- JP: 「僕も他をよく知らんゆえ、断言はできんが――\n多分、どこでもそのようなものだと思う」
- TW: 「我所了解的範圍實屬有限，所以無法斷言——但我想應該都是大體相當的程度吧」
- VN cũ: 「Tôi cũng không rành những người khác nên không dám khẳng định——\nNhưng có lẽ, ở đâu cũng vậy thôi.」
- Sửa: 「Anh cũng không rành những người khác nên không dám khẳng định——\nNhưng có lẽ, ở đâu cũng vậy thôi.」
- Lý do: Soutetsu nói với Olivy (dòng sau 2516 Olivy đáp): 'anh'. VN cũ 'Tôi' sai.

### 2388 — ハチロク — thuật ngữ
- JP: 「開拓当初の北開道は、広大な土地と低い輸送密度ゆえに、冥国式をお手本として採用したとも聞いておりますが」
- TW: 「我是有聽說在北海道鐵路事業開拓初期，因其土地遼闊與較低的車次密度，借鑑的是美國式」
- VN cũ: 「Em cũng nghe nói rằng ở Hokkaido thời kỳ đầu khai phá, do đất đai rộng lớn và mật độ vận chuyển thấp nên họ đã áp dụng kiểu Mỹ làm hình mẫu ạ.」
- Sửa: 「Em cũng nghe nói rằng ở Hokkaido thời kỳ đầu khai phá, do đất đai rộng lớn và mật độ vận chuyển thấp nên họ đã áp dụng kiểu Minh Quốc làm hình mẫu ạ.」
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'.

### 2389 — ポーレット — thuật ngữ
- JP: 「冥国では、それで十分なんだと思います。\n国土も広大で、輸送密度も相当に薄いはずですし」
- TW: 「我覺得在美國這倒不算是個問題。畢竟疆域遼闊，車次密度相對應該也不高才對」
- VN cũ: 「Ở Mỹ, như vậy chắc là đủ rồi.\nLãnh thổ rộng lớn, mật độ vận chuyển chắc chắn cũng khá thưa thớt.」
- Sửa: 「Ở Minh Quốc, như vậy chắc là đủ rồi.\nLãnh thổ rộng lớn, mật độ vận chuyển chắc chắn cũng khá thưa thớt.」
- Lý do: JP 冥国では (không furigana メリケン) → 'Minh Quốc'. VN cũ 'Ở Mỹ'.

### 2399 — 双鉄 — thuật ngữ
- JP: 「だから、冥国式の蒸機と\x%lレイルロオド;#00ffc040;レイルロオド%l;#;とは、\n日ノ本式のお手本にはなれなかったというわけか」
- TW: 「所以美國式的蒸汽機車和\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，沒有成為日本式所借鑑的對象」
- VN cũ: 「Nên đầu máy hơi nước và \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ,\nđã không thể trở thành hình mẫu cho kiểu Hinamoto sao.」
- Sửa: 「Nên đầu máy hơi nước và \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\nđã không thể trở thành hình mẫu cho kiểu Hinamoto sao.」
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'. 'kiểu Hinamoto' giữ nguyên — chờ đợt thống nhất.

### 2426 — ハチロク — sai nghĩa
- JP: 「か、どうかはまだわかりません。\n双鉄さまはキャブ内を。日々姫は、わたくしを連れて」
- TW: 「是否如此尚難斷言。請雙鐵少爺在駕駛室內稍候。日日姬，帶我去看一下」
- VN cũ: 「Có sao hay không thì vẫn chưa biết được đâu ạ.\nNgài Soutetsu hãy kiểm tra bên trong buồng lái. Hibiki, hãy đưa em đi xem thử.」
- Sửa: 「Có sao hay không thì vẫn chưa biết được đâu ạ.\nNgài Soutetsu cứ ở trong buồng lái ạ. Hibiki, hãy đưa em đi xem thử.」
- Lý do: JP '双鉄さまはキャブ内を' là câu dở dang (thiếu động từ) — TW '請雙鐵少爺在駕駛室內稍候' (mời ngài Soutetsu chờ trong buồng lái). VN cũ bịa thêm động từ 'hãy kiểm tra' — sai nghĩa (Soutetsu ở lại chờ, không phải kiểm tra). Sửa theo TW.

### 2433 — 双鉄 — đại từ
- JP: 「転んで、どこか打ったりしたか？」
- TW: 「是沒站穩撞到哪裡了嗎？」
- VN cũ: 「Cô bị ngã rồi va đập vào đâu à?」
- Sửa: 「Em bị ngã rồi va đập vào đâu à?」
- Lý do: Soutetsu nói với Olivy (ngay sau độc thoại 2916 về Olivy): 'em'. VN cũ 'Cô' sai.

### 2437 — ポーレット — thuật ngữ
- JP: 「はい。国は[えいこく,1]詠国式をお手本にしましたし、大手私鉄も\n[どっこく,1]髑国や詠国が主流。[めいこく,1]冥国式は、そもそも少数派でした」
- TW: 「是的。國家層面上是借鑑的英國，大型的私營鐵路也是以德國和英國為主流。美國式從一開始就是少數派」
- VN cũ: 「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Mỹ vốn dĩ đã là thiểu số rồi.」
- Sửa: 「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Minh Quốc vốn dĩ đã là thiểu số rồi.」
- Lý do: JP [めいこく,1]冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'Kiểu Mỹ'.

### 2449 — 双鉄 — thuật ngữ
- JP: 「いや、湯医線の習熟運転には、ハチロクも同乗する。\nみかん鉄道では、先任\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の同乗は無いのか？」
- TW: 「會的，在你熟悉湯醫線期間，八六也會同行。橙鐵路那邊的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;沒有這樣老帶新的做法嗎？」
- VN cũ: 「Không, trong chuyến chạy làm quen Tuyến Yui, Hachiroku cũng sẽ đi cùng.\nỞ Đường sắt Mikan, không có chuyện \x%lレイルロオド;#00ffc040;Railord%l;#; tiền nhiệm đi cùng sao?」
- Sửa: 「Không, trong chuyến chạy làm quen Tuyến Yunoi, Hachiroku cũng sẽ đi cùng.\nỞ Đường sắt Mikan, không có chuyện \x%lレイルロオド;#00ffc040;Railord%l;#; tiền nhiệm đi cùng sao?」
- Lý do: JP 湯医線 — thuật ngữ đã chốt: 湯医線='tuyến Yunoi'. VN cũ 'Tuyến Yui'.

### 2456 — 凪 — thuật ngữ
- JP: 「凪さまちょこっとムカついたばってん、\n謝るんなら許すばい！　ざばっと水に流すばい！」
- TW: 「本小姐倒是有那麼一點不爽，不過既然你都道歉了，過去的事就過去吧！咱大人有大量，原諒你咧！」
- VN cũ: 「Nagi đại nhân đây có hơi bực mình một tẹo,\nnhưng mà đã xin lỗi rồi thì tha cho á! Cho trôi tuột đi hết luôn á!」
- Sửa: 「Bổn tiểu thư đây có hơi bực mình một tẹo,\nnhưng mà đã xin lỗi rồi thì tha cho á! Cho trôi tuột đi hết luôn á!」
- Lý do: JP 凪さま — Nagi tự xưng; TW 本小姐. Tiền lệ 凪ふかみ01 (8 dòng) + ハチロク07 2393: 凪さま→'Bổn tiểu thư'. VN cũ 'Nagi đại nhân đây' chưa thống nhất.

### 2458 — 凪 — thuật ngữ
- JP: 「凪さま！　凪さまと組んで乗務するばい！」
- TW: 「本小姐！就跟本小姐一塊執行乘務任務！」
- VN cũ: 「Thì Nagi! Sẽ bắt cặp với Nagi để làm nhiệm vụ á!」
- Sửa: 「Thì Bổn tiểu thư đây! Sẽ bắt cặp với Bổn tiểu thư để làm nhiệm vụ á!」
- Lý do: JP 凪さま ×2 — Nagi tự xưng; TW 本小姐. Tiền lệ 凪ふかみ01 + ハチロク07 2393: 凪さま→'Bổn tiểu thư'. VN cũ bỏ hẳn さま ở cả 2 chỗ.

### 2468 — ポーレット — thuật ngữ
- JP: 「ようこそ御一夜へ。そして、ようこそ御一夜鉄道へ！\nこれから、どうぞ、よろしくお願いいたします！」
- TW: 「歡迎來到御一夜，歡迎來到御一夜鐵路！今後還請多多指教！」
- VN cũ: 「Chào mừng đến với Ohito. Và, chào mừng đến với Đường sắt Ohito!\nTừ nay về sau, mong cô giúp đỡ nhiều hơn!」
- Sửa: 「Chào mừng đến với Ohitoyo. Và, chào mừng đến với Đường sắt Ohitoyo!\nTừ nay về sau, mong cô giúp đỡ nhiều hơn!」
- Lý do: JP 御一夜 ×2 — quyết định 19/11: 御一夜='Ohitoyo'. VN cũ 'Ohito' (cả 2 chỗ).

### 2473 — オリヴィ — thuật ngữ
- JP: 「ないよー！　みかん鉄道の現役蒸機は、Ⅸ号……は、\nもうオヒトヨだから、\x%lC56;#00ffc040;Ｃ５６%l;#;　[キューキュー,1]９９と、新しく来るこだけ」
- TW: 「沒有哦！橙鐵路的蒸汽機車有九號……但是已經來御一夜了，還有就是\x%lC56;#00ffc040;Ｃ５６%l;#;　９９和後面新來的那孩子了」
- VN cũ: 「Không có đâu nha! Đầu máy hơi nước đang hoạt động của Đường sắt Mikan, đầu máy số 9…… thì\nđã ở Ohito rồi, nên giờ chỉ còn \x%lC56;#00ffc040;C56%l;#; 99 và chiếc mới đến thôi.」
- Sửa: 「Không có đâu nha! Đầu máy hơi nước đang hoạt động của Đường sắt Mikan, đầu máy số 9…… thì\nđã ở Ohitoyo rồi, nên giờ chỉ còn \x%lC56;#00ffc040;C56%l;#; 99 và chiếc mới đến thôi.」
- Lý do: JP 御一夜 (オヒトヨ) — quyết định 19/11: 御一夜='Ohitoyo'. VN cũ 'Ohito'.

### 2475 — オリヴィ — thuật ngữ
- JP: 「ないない。オリヴィはずっとⅨ号だけ。\nもったいないよね？　せっかく[メリケン,2]冥国式なのに」
- TW: 「沒有沒有。奧莉薇一直都只是搭九號的啦。我明明是少有的美國式，很浪費吧？」
- VN cũ: 「Không có không có nha. Olivy chỉ luôn đi với đầu máy số 9 thôi.\nUổng phí ghê ha? Dù gì cũng cất công mang danh kiểu Mỹ mà.」
- Sửa: 「Không có không có nha. Olivy chỉ luôn đi với đầu máy số 9 thôi.\nUổng phí ghê ha? Dù gì cũng cất công mang danh kiểu Meriken mà.」
- Lý do: JP [メリケン,2]冥国式 — furigana メリケン nói → 'Meriken'. VN cũ 'kiểu Mỹ'.

### 2479 — ハチロク — lỗi nhỏ
- JP: 「はい。正真正銘の天然温泉の大浴場。\n標準的な駅施設の沸かし湯よりも、何百倍も素敵かと」
- TW: 「沒錯，是真真正正的天然溫泉大浴場。比起車站標準的燒水澡堂，可是好了何止千百倍」
- VN cũ: 「Vâng. Là đại lội tắm suối nước nóng thiên nhiên chính hiệu đó ạ.\nTuyệt vời hơn gấp trăm lần so với nước đun sôi ở các cơ sở nhà ga tiêu chuẩn đấy ạ.」
- Sửa: 「Vâng. Là nhà tắm lớn với suối nước nóng thiên nhiên chính hiệu đó ạ.\nTuyệt vời hơn gấp hàng trăm lần so với nước đun sôi ở các cơ sở nhà ga tiêu chuẩn đấy ạ.」
- Lý do: JP 大浴場 (nhà tắm lớn) — VN cũ 'đại lội tắm' là lỗi đánh máy vô nghĩa ('lội' = lội nước). Đồng thời JP 何百倍 (vài trăm lần) — VN cũ 'gấp trăm lần' (100 lần) thiếu chính xác.

### 2540 — ポーレット — thuật ngữ
- JP: 「冥国式のこは、そういう感じの最適化がされないんです。\nそのかわり誰とでも組めるし、どの車両にもすぐ乗れる」
- TW: 「美國式的就沒有這些固定拍檔意識，但相對的，和誰都可以搭檔，不管任何車輛都能很快上手」
- VN cũ: 「Những cô bé kiểu Mỹ không được tối ưu hóa theo kiểu như vậy.\nĐổi lại, họ có thể bắt cặp với bất kỳ ai và lên bất kỳ toa xe nào ngay lập tức.」
- Sửa: 「Những cô bé kiểu Minh Quốc không được tối ưu hóa theo kiểu như vậy.\nĐổi lại, họ có thể bắt cặp với bất kỳ ai và lên bất kỳ toa xe nào ngay lập tức.」
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'.

### 2541 — 双鉄 — thuật ngữ
- JP: 「冥国蒸機」
- TW: 「美國蒸汽機車」
- VN cũ: 「Đầu máy hơi nước Mỹ.」
- Sửa: 「Đầu máy hơi nước Minh Quốc.」
- Lý do: JP 冥国蒸機 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'đầu máy hơi nước Mỹ'.

### 2585 — ポーレット — thuật ngữ
- JP: 「そうですね。冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の、最大の特徴です。\nそもそも、日ノ本式や詠・髑国式とは設計思想が違う」
- TW: 「說得沒錯，那就是美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;最大的特徵。說到底，與日本式、英國式和德國式在設計思想上就有所不同」
- VN cũ: 「Đúng vậy. Đó là đặc điểm lớn nhất của \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ.\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinamoto, kiểu Anh hay kiểu Đức rồi.」
- Sửa: 「Đúng vậy. Đó là đặc điểm lớn nhất của \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinamoto, kiểu Anh hay kiểu Đức rồi.」
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'. 'kiểu Hinamoto' giữ nguyên — chờ đợt thống nhất.

### 2623 — ポーレット — thuật ngữ
- JP: 「そこは、冥国蒸機の強みですよね」
- TW: 「這就是美國蒸汽機車的強悍之處了」
- VN cũ: 「Đó chính là điểm mạnh của đầu máy hơi nước Mỹ đấy.」
- Sửa: 「Đó chính là điểm mạnh của đầu máy hơi nước Minh Quốc đấy.」
- Lý do: JP 冥国蒸機 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'đầu máy hơi nước Mỹ'.

### 2629 — ポーレット — gasp (sweep)
- JP: 「っ！」\n「いえっ！」
- TW: 「這！」\n「不會！」
- VN cũ: 「っ!」\n「Không phải đâu ạ!」
- Sửa: 「Ư!」\n「Không phải đâu ạ!」
- Lý do: Sweep raw-tsu: JP dòng 1 「っ！」 → Ư. Dòng 2 「いえっ！」 giữ nguyên — っ nhấn mạnh trên từ nội dung 'không', không phải gasp (tiền lệ sweep 1474 bị loại).

### 2636 — 双鉄 — thuật ngữ
- JP: 「つまり、オリヴィたち冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、\nマスター、――いや、\x%l機関士;#00ffc040;機関士%l;#;が誰であれ、組めるのか」
- TW: 「那也就是說，奧莉薇她們美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，隨便與哪位\x%l機関士;#00ffc040;司機%l;#;都可以搭檔嗎」
- VN cũ: 「Nói cách khác, những \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ như Olivy,\ncó thể bắt cặp với bất kỳ Master——à không, bất kỳ \x%l機関士;#00ffc040;lái tàu%l;#; nào sao?」
- Sửa: 「Nói cách khác, những \x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc như Olivy,\ncó thể bắt cặp với bất kỳ Master——à không, bất kỳ \x%l機関士;#00ffc040;lái tàu%l;#; nào sao?」
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'.

### 2646 — オリヴィ — sai nghĩa
- JP: 「それで、なんの仕事からすればいいの？\n\x%l罐磨;#00ffc040;罐磨%l;#;き？　[こないせいり,3]庫内整理？」
- TW: 「那奧莉薇要從什麼工作做起呢？\x%l罐磨;#00ffc040;擦車%l;#;？收拾機車庫？」
- VN cũ: 「Vậy, Olivy nên bắt đầu từ công việc gì đây?\n\x%l罐磨;#00ffc040;Cọ rửa lò hơi%l;#;? Dọn dẹp nhà kho?」
- Sửa: 「Vậy, Olivy nên bắt đầu từ công việc gì đây?\n\x%l罐磨;#00ffc040;Cọ rửa lò hơi%l;#;? Dọn dẹp trong kho đầu máy?」
- Lý do: JP 庫内整理 = dọn dẹp trong nhà kho đầu máy (TW 收拾機車庫); 'nhà kho' chung chung làm mất nghĩa 'kho đầu máy' (機関庫, cf. 2127 'kho đầu máy').

### 2684 — ハチロク — gasp (sweep)
- JP: 「双鉄さまっ！」「非常ーーーーーっ！！！！」\n「っ！！！」
- TW: 「雙鐵少爺！」「緊急————！！！！」\n「啊！！！」
- VN cũ: 「Ngài Soutetsu!」「Phanh khẩn cấpppp!!!!」\n「っ!!!」
- Sửa: 「Ngài Soutetsu!」「Phanh khẩn cấpppp!!!!」\n「Ư!!!」
- Lý do: Sweep raw-tsu: JP dòng 3 「っ！！！」 → Ư. 2 dòng đầu đã dịch đúng ('Phanh khẩn cấpppp' giữ nguyên độ dài âm).

### 2694 — 双鉄 — thuật ngữ
- JP: 「メリケン？」
- TW: 「Ａｍｅｒｉｃａｎ？」
- VN cũ: 「Đồ chuẩn Mỹ?」
- Sửa: 「Meriken?」
- Lý do: JP 「メリケン？」 — Soutetsu nhắc lại đúng từ Olivy vừa nói → giữ 'Meriken'. VN cũ 'Đồ chuẩn Mỹ?'.

### 2697 — オリヴィ — thuật ngữ
- JP: 「オッケー了解！　どっちと組んでもだいじょーぶ！\nオリヴィ、[メリケン,2]冥国式だから！」
- TW: 「ＯＫ明白！和誰搭檔都沒問題！奧莉薇可是[Ａｍｅｒｉｃａｎ,2]美國式的！」
- VN cũ: 「OK đã rõ! Bắt cặp với ai cũng được hết á!\nVì Olivy là đồ chuẩn Mỹ mà!」
- Sửa: 「OK đã rõ! Bắt cặp với ai cũng được hết á!\nVì Olivy là kiểu Meriken mà!」
- Lý do: JP [メリケン,2]冥国式 — furigana メリケン nói → 'Meriken'. VN cũ 'đồ chuẩn Mỹ'.

### 3078 — monologue — gasp (sweep)
- JP: オリヴィも集中しきってくれているのだろう。\n視線は背中を刺すようだったが、この調子なら――っ！
- TW: 奧莉薇想必也正全神貫注著吧。雖然我隱約感到身後緊盯著的視線，但以這個狀態的話——！
- VN cũ: Chắc hẳn Olivy cũng đang tập trung cao độ.\nÁnh mắt cô ấy như xuyên thấu lưng tôi, nhưng nếu cứ giữ vững phong độ này thì——っ!
- Sửa: Chắc hẳn Olivy cũng đang tập trung cao độ.\nÁnh mắt cô ấy như xuyên thấu lưng tôi, nhưng nếu cứ giữ vững phong độ này thì——Ư!
- Lý do: Sweep raw-tsu: JP kết ——っ！ (gasp tuyệt đối-cuối, TW ——！); VN cũ để nguyên っ. Thêm Ư.

### 3115 — monologue — thuật ngữ
- JP: 日ノ本式では、そのほとんどが廃用を余儀なくされる。\nけれども冥国式ならば、再活用に困らない。
- TW: 對於日本式，遇到這些情況基本除廢棄別無選擇。但是換成美國式，恢復使用就毫無難度了。
- VN cũ: Ở kiểu Hinamoto, hầu hết đều buộc phải bỏ đi.\nNhưng nếu là kiểu Mỹ, thì không cần lo lắng về việc tái sử dụng.
- Sửa: Ở kiểu Hinamoto, hầu hết đều buộc phải bỏ đi.\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng.
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'. 'kiểu Hinamoto' giữ nguyên — chờ đợt thống nhất.

### 3272 — monologue — thuật ngữ
- JP: そうするためにも、まずは湯医へ。\nそうして、御一夜へ折り返して、だ！
- TW: 為讓這難得的好兆頭不會白費，我們也要順利開到湯醫，而後折返回御一夜！
- VN cũ: Để được như vậy, trước tiên phải đến Yui đã.\nSau đó quay trở lại Ohito!
- Sửa: Để được như vậy, trước tiên phải đến Yunoi đã.\nSau đó quay trở lại Ohitoyo!
- Lý do: JP 湯医→'Yunoi', 御一夜→'Ohitoyo' (quyết định 19/11). VN cũ 'Yui'/'Ohito'.

### 3317 — monologue — thuật ngữ
- JP: 万が一にもしくじって、『御一夜鉄道はこんなものか』と\n思われたのなら、恐らく、オリヴィのためにもならない。
- TW: 若是萬一失了方寸，讓奧莉薇覺得“御一夜鐵路不過如此”的話，恐怕，不管是對奧莉薇，還是對我們，都不是什麼好事。
- VN cũ: Nhỡ may tôi làm hỏng việc, khiến cô ấy nghĩ "Đường sắt Ohito chỉ đến thế này thôi sao"\nthì e rằng cũng chẳng tốt đẹp gì cho Olivy.
- Sửa: Nhỡ may tôi làm hỏng việc, khiến cô ấy nghĩ "Đường sắt Ohitoyo chỉ đến thế này thôi sao"\nthì e rằng cũng chẳng tốt đẹp gì cho Olivy.
- Lý do: JP 御一夜鉄道 — quyết định 19/11: 御一夜='Ohitoyo' → 'Đường sắt Ohitoyo'. VN cũ 'Đường sắt Ohito'.

### 3351 — monologue — thuật ngữ
- JP: そういえば、冥国式がどうのとさっき話に出てきた。
- TW: 說起來，剛才提到過美國式，都還沒來得及問清楚。
- VN cũ: Nhắc mới nhớ, lúc nãy cũng có nhắc đến kiểu Mỹ gì đó.
- Sửa: Nhắc mới nhớ, lúc nãy cũng có nhắc đến kiểu Minh Quốc gì đó.
- Lý do: JP 冥国式 (không furigana メリケン) → 'Minh Quốc'. VN cũ 'kiểu Mỹ'.

### 3359 — monologue — thuật ngữ
- JP: 国産量産第一号機\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;、\n栄えある帝鉄8620形の、トップナンバー・\x%lレイルロオド;#00ffc040;レイルロオド%l;#;。
- TW: 身為第一輛下線的國產量產\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;，無數榮光加身的８６２０型首車的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;。
- VN cũ: \x%lレイルロオド;#00ffc040;Railord%l;#; chiếc đầu tiên, của mẫu 8620 thuộc Đường sắt Hoàng gia đầy vinh quang,\nchiếc \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; sản xuất hàng loạt trong nước đầu tiên.
- Sửa: \x%lレイルロオド;#00ffc040;Railord%l;#; chiếc đầu tiên, của mẫu 8620 thuộc Teitetsu đầy vinh quang,\nchiếc \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; sản xuất hàng loạt trong nước đầu tiên.
- Lý do: JP 帝鉄 — thuật ngữ đã chốt: 帝鉄='Teitetsu' (trong file 1988/2337 đã dùng đúng 'Teitetsu'). VN cũ 'Đường sắt Hoàng gia'.

### 3428 — monologue — SFX
- JP: （パンっ！！）
- TW: （啪！！）
- VN cũ: （Đập tay!!）
- Sửa: （Bốp!!）
- Lý do: JP （パンっ！！） — tiếng vỗ tay high-five; TW （啪！！）. VN cũ diễn thành hành động '(Đập tay!!)' làm mất tiếng; các SFX khác trong file đều giữ dạng tiếng (Bốp, Kịch, Tuuu). Sửa '(Bốp!!)' cho nhất quán.

### 3429 — monologue — SFX
- JP: （パンっ！）
- TW: （啪！）
- VN cũ: （Đập tay!）
- Sửa: （Bốp!）
- Lý do: JP （パンっ！） — tiếng vỗ tay high-five; TW （啪！）. VN cũ diễn thành hành động '(Đập tay!)' làm mất tiếng; các SFX khác trong file đều giữ dạng tiếng. Sửa '(Bốp!)'.
## §3. Sweep っ-gasp kiểm chứng

- Sweep có 9 mục cho file, nhận cả 9 (1528, 2124, 2125, 2165, 2167, 2168, 2629, 2684, 3078) — đã kiểm chứng từng giá trị với JP, xem §2.
- Quét máy bổ sung toàn file (tất cả dòng JP chứa っ): không còn gasp nào sweep bỏ sót. Các っ còn lại đều đã diễn đúng: あっ→"A", あっ！？→"A!?", くっ→"Khục", きゃっ→"Á", むうっ→"Muu", ぁぅっ→"Á", あははっ→"A haha", うふふっ→"ufufu", ふふふ→"Fufufu", いえっ→"Không phải đâu ạ!" (っ nhấn mạnh trên từ nội dung — không phải gasp, tiền lệ sweep 1474 bị loại), そーだねっ/よろしくっ/ソーテツサマっ (っ nhấn mạnh cuối câu — không phải gasp), các phó từ さっと/とっさに/あっさり/ホっと/ギョっと/スっと/ぶわりと đã dịch đúng nghĩa.
- 2 dòng SFX パンっ (3428, 3429) không nằm trong sweep — đã sửa riêng ở §2 (SFX).

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- Olivy tự xưng "tôi" (1998, 2131, 2302, 2517, 2570, 2591): giữ nguyên — tiền lệ ハチロク14 parent kiểm chứng "Olivy tự xưng 'tôi'". Olivy gọi Soutetsu "cậu" (2680): giữ nguyên — tiền lệ ハチロク06 "Olivy xưng 'cậu' với Soutetsu/Hachiroku (giữ nguyên)". Olivy gọi Soutetsu "anh" ở 2589/2663.
- Soutetsu "cô"/"tôi" với Hachiroku (2039, 2216, 2386, 2368): đúng — "tôi" với Hachiroku theo quy tắc đã chốt. Dạng nhóm "chúng tôi"/"chúng ta"/"bọn em" (2500, 2558, 2560, 2530): giữ nguyên theo quy tắc nhóm.
- 2127: VN tự thêm thẻ %l cho 機関庫 ("kho đầu máy") trong khi JP chỉ có ruby [きかんこ,2] — nội dung gloss đúng, chỉ ghi nhận quan sát (tiền lệ ハチロク02 2090).
- 2149: Hibiki 「ふぁあ～」→"Haa~", Olivy 「はふぁ～」→"Hafaa~" — tiếng ngáp; quy tắc fa/fu (ふぁ→"phà") đang chờ đợt thống nhất cho ハチロクh6 + lr_ふかみh2, không áp vào đây (xem §6).
- 2554: 「イェイ！」「いぇいっ！」 đều → "Yeah!" — っ cuối trên từ cảm thán đã diễn bằng dấu "!" (cùng loại っ nhấn mạnh, không phải gasp).
- 2227: ささくれちゃった → "nhạy cảm một chút" — giữ: ささくれる là trở nên cáu kỉnh/gai góc; VN diễn mềm theo giọng Olivy tự nhận lỗi, chấp nhận được.
- 1532/2412/2510/2585/1580/3115/2503/2454/2399/2084 "kiểu Hinamoto": giữ nguyên — chờ đợt thống nhất (xem §6). 2131 投炭 gloss "thêm than": giữ nguyên — "投炭 gloss split" nằm trong hàng đợi thống nhất.
- 2236 Olivy "Cảm ơn chị." (với Paulette): giữ — Paulette là chị cả/chủ tịch, Olivy gọi "chị" hợp lý. 2476 Hibiki gọi Olivy "Olivy" (không -chan): giữ — Hibiki gọi tên trần trong file này nhất quán.

## §5. Khối TOML (đã parse-kiểm chứng: 58 khóa, 0 sai lệch)

```toml
[script]
1528 = "\"Olivy đã bị đối xử như thế nào ở Đường sắt Mikan\"\\n——Ư!"
1551 = "「Có vẻ như bên trong buồng lái cũng không có vấn đề gì.\\nVậy thì chúng ta hãy nhanh chóng tăng tốc chạy bù giờ đến Yunoi thôi ạ.」"
1580 = "「……\\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \\x%lレイルロオド;#00ffc040;Railord%l;#;\\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」"
1984 = "「Không có \\x%l運転体;#00ffc040;thân vận hành%l;#; hay \\x%l整備体;#00ffc040;thân bảo trì%l;#;, chỉ có một cơ thể duy nhất khiến tôi rất ngạc nhiên.\\nĐó là do đầu máy hơi nước Minh Quốc——không phải」"
1988 = "「Không chỉ thao tác kiểm tra máy móc nhanh nhẹn, mà chỉ thị \\x%l投炭;#00ffc040;thêm than%l;#; cũng rất chính xác,\\nnên anh cứ tưởng em có nhiều kinh nghiệm làm nhiệm vụ trên dòng 8620——đầu máy hơi nước của Teitetsu chứ.」"
1993 = "「Không cần đâu ạ. Chỉ cần chị có lòng là được rồi.\\nDù sao thì đây cũng là chuyến đi đầu tiên của Olivy trên tuyến Yunoi mà.」"
2023 = "「Hôm nay em đã giúp đỡ rất nhiều.\\nCũng không hẳn là quà cảm ơn, nhưng nếu em thích thì dùng thử xem?」"
2042 = "「Olivy, em từng làm nhiệm vụ trên dòng 8620 rồi sao?」"
2044 = "「Em không sao——…………chứ?」"
2076 = "「Được sản xuất vào năm Minh Trị 45. Do hãng Aldwin Locomotive Works\\ncủa Minh Quốc chế tạo.」"
2083 = "「Lúc nãy cũng có nhắc đến, cái gọi là kiểu Meriken đó——」"
2112 = "「Nhưng mà, lúc nãy,\\nanh nghe thấy giọng em có vẻ rất đau đớn——」"
2124 = "「Ư!!?」"
2125 = "「Ư!?」"
2165 = "「Ư!!」"
2167 = "「Ư!!!!」"
2168 = "「Ư!?」"
2198 = "「Au~, Bổn tiểu thư đây xui xẻo quá đi mất á!」"
2238 = "「À. Để anh giới thiệu lại bản thân nhé.\\nChào mừng đến Ohitoyo, Olivy. Anh là Migita Soutetsu.」"
2283 = "「Olivy mới là người cần giúp đỡ! Mong mọi người giúp đỡ nha!\\nOlivy sẽ cố gắng để trở nên yêu thích Ohitoyo thật nhiều!」"
2300 = "「Em cứ nghỉ ngơi cho khỏe đi.\\nNếu có gì cần hỏi, ngày mai anh sẽ xác nhận lại sau.」"
2315 = "「Nếu mọi chuyện suôn sẻ đến đó, trước tiên em sẽ bắt cặp với anh,\\nlái thử đầu máy số 9 trên tuyến Yunoi. Nếu không có vấn đề gì thì」"
2341 = "「Là kiểu Minh Quốc ạ.\\nTrong trường hợp này, ý cô ấy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc đó ạ.」"
2345 = "「Là vậy đó. Anh cũng sẽ đi theo với tư cách là \\x%l機関士;#00ffc040;lái tàu%l;#; hướng dẫn.\\nCuối cùng em sẽ bắt cặp với ai thì còn phải dựa vào đánh giá tổng hợp nữa.」"
2370 = "「Em cũng rất hoan nghênh cách gọi đó!\\nMột lần nữa mong được giúp đỡ nhé, Olivy!」"
2373 = "「Với tư cách là Giám đốc của Công ty Cổ phần Đường sắt Ohitoyo.\\nTôi xin chấp nhận lời xin lỗi của cô Olivy.」"
2383 = "「Anh cũng không rành những người khác nên không dám khẳng định——\\nNhưng có lẽ, ở đâu cũng vậy thôi.」"
2388 = "「Em cũng nghe nói rằng ở Hokkaido thời kỳ đầu khai phá, do đất đai rộng lớn và mật độ vận chuyển thấp nên họ đã áp dụng kiểu Minh Quốc làm hình mẫu ạ.」"
2389 = "「Ở Minh Quốc, như vậy chắc là đủ rồi.\\nLãnh thổ rộng lớn, mật độ vận chuyển chắc chắn cũng khá thưa thớt.」"
2399 = "「Nên đầu máy hơi nước và \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nđã không thể trở thành hình mẫu cho kiểu Hinamoto sao.」"
2426 = "「Có sao hay không thì vẫn chưa biết được đâu ạ.\\nNgài Soutetsu cứ ở trong buồng lái ạ. Hibiki, hãy đưa em đi xem thử.」"
2433 = "「Em bị ngã rồi va đập vào đâu à?」"
2437 = "「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Minh Quốc vốn dĩ đã là thiểu số rồi.」"
2449 = "「Không, trong chuyến chạy làm quen Tuyến Yunoi, Hachiroku cũng sẽ đi cùng.\\nỞ Đường sắt Mikan, không có chuyện \\x%lレイルロオド;#00ffc040;Railord%l;#; tiền nhiệm đi cùng sao?」"
2456 = "「Bổn tiểu thư đây có hơi bực mình một tẹo,\\nnhưng mà đã xin lỗi rồi thì tha cho á! Cho trôi tuột đi hết luôn á!」"
2458 = "「Thì Bổn tiểu thư đây! Sẽ bắt cặp với Bổn tiểu thư để làm nhiệm vụ á!」"
2468 = "「Chào mừng đến với Ohitoyo. Và, chào mừng đến với Đường sắt Ohitoyo!\\nTừ nay về sau, mong cô giúp đỡ nhiều hơn!」"
2473 = "「Không có đâu nha! Đầu máy hơi nước đang hoạt động của Đường sắt Mikan, đầu máy số 9…… thì\\nđã ở Ohitoyo rồi, nên giờ chỉ còn \\x%lC56;#00ffc040;C56%l;#; 99 và chiếc mới đến thôi.」"
2475 = "「Không có không có nha. Olivy chỉ luôn đi với đầu máy số 9 thôi.\\nUổng phí ghê ha? Dù gì cũng cất công mang danh kiểu Meriken mà.」"
2479 = "「Vâng. Là nhà tắm lớn với suối nước nóng thiên nhiên chính hiệu đó ạ.\\nTuyệt vời hơn gấp hàng trăm lần so với nước đun sôi ở các cơ sở nhà ga tiêu chuẩn đấy ạ.」"
2540 = "「Những cô bé kiểu Minh Quốc không được tối ưu hóa theo kiểu như vậy.\\nĐổi lại, họ có thể bắt cặp với bất kỳ ai và lên bất kỳ toa xe nào ngay lập tức.」"
2541 = "「Đầu máy hơi nước Minh Quốc.」"
2585 = "「Đúng vậy. Đó là đặc điểm lớn nhất của \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc.\\nVốn dĩ, tư tưởng thiết kế của họ đã khác với kiểu Hinamoto, kiểu Anh hay kiểu Đức rồi.」"
2623 = "「Đó chính là điểm mạnh của đầu máy hơi nước Minh Quốc đấy.」"
2629 = "「Ư!」\\n「Không phải đâu ạ!」"
2636 = "「Nói cách khác, những \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc như Olivy,\\ncó thể bắt cặp với bất kỳ Master——à không, bất kỳ \\x%l機関士;#00ffc040;lái tàu%l;#; nào sao?」"
2646 = "「Vậy, Olivy nên bắt đầu từ công việc gì đây?\\n\\x%l罐磨;#00ffc040;Cọ rửa lò hơi%l;#;? Dọn dẹp trong kho đầu máy?」"
2684 = "「Ngài Soutetsu!」「Phanh khẩn cấpppp!!!!」\\n「Ư!!!」"
2694 = "「Meriken?」"
2697 = "「OK đã rõ! Bắt cặp với ai cũng được hết á!\\nVì Olivy là kiểu Meriken mà!」"
3078 = "Chắc hẳn Olivy cũng đang tập trung cao độ.\\nÁnh mắt cô ấy như xuyên thấu lưng tôi, nhưng nếu cứ giữ vững phong độ này thì——Ư!"
3115 = "Ở kiểu Hinamoto, hầu hết đều buộc phải bỏ đi.\\nNhưng nếu là kiểu Minh Quốc, thì không cần lo lắng về việc tái sử dụng."
3272 = "Để được như vậy, trước tiên phải đến Yunoi đã.\\nSau đó quay trở lại Ohitoyo!"
3317 = "Nhỡ may tôi làm hỏng việc, khiến cô ấy nghĩ \"Đường sắt Ohitoyo chỉ đến thế này thôi sao\"\\nthì e rằng cũng chẳng tốt đẹp gì cho Olivy."
3351 = "Nhắc mới nhớ, lúc nãy cũng có nhắc đến kiểu Minh Quốc gì đó."
3359 = "\\x%lレイルロオド;#00ffc040;Railord%l;#; chiếc đầu tiên, của mẫu 8620 thuộc Teitetsu đầy vinh quang,\\nchiếc \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; sản xuất hàng loạt trong nước đầu tiên."
3428 = "（Bốp!!）"
3429 = "（Bốp!）"
```

## §6. Chờ Hieu (không tự quyết)

- 日ノ本 "Hinamoto" còn 10 dòng (2510, 2412, 2585, 1580, 1532, 2084, 3115, 2503, 2454, 2399) — KHÔNG sửa trong audit này: brief liệt kê ハチロク03 trong 36 dòng Hinamoto→Hinomoto của đợt thống nhất (brief ghi ×9, đếm thực tế trong file là 10 dòng — parent kiểm tra lại con số khi chạy đợt thống nhất).
- Yui→Yunoi đã sửa 5 dòng trong audit này (1551, 2449, 2315, 3272, 1993) theo thuật ngữ đã chốt 湯医/湯医線="Yunoi" — KHÔNG thêm lại các key này vào hàng đợi thống nhất. (Lưu ý: một số audit trước để "Yui" lại chờ thống nhất; các file đã audit vẫn còn "Yui" — đợt thống nhất cần quét toàn dự án, không chỉ P14/P16.)
- Ohito→Ohitoyo đã sửa 7 dòng (2238, 2283, 2373, 2468, 2473, 3272, 3317) — KHÔNG thêm lại vào hàng đợi 67 dòng Ohitoyo cũ (con số 67 là của các file đã audit trước đây; file này chưa từng được tính).
- Minh Quốc/Meriken đã sửa 19 dòng — KHÔNG thêm lại vào hàng đợi thống nhất: Meriken 4 (2694, 2697, 2475, 2083), Minh Quốc 15 (1580, 1984, 2076, 2341, 2388, 2389, 2399, 2437, 2540, 2541, 2585, 2623, 2636, 3115, 3351).
- Teitetsu 3359 + thân vận hành/thân bảo trì 1984 + Bổn tiểu thư 3 dòng (2198, 2456, 2458) đã sửa — KHÔNG thêm lại vào hàng đợi thống nhất. Riêng 運転体 "thân vận hành": tiền lệ ハチロク07/10 dùng "thân vận hành", nhưng 仲国01 vẫn ghi "thân lái" vs "kíp lái" chờ thống nhất — đợt thống nhất chốt một dạng cho toàn dự án.
- 2149 ふぁあ～/はふぁ～ ("Haa~"/"Hafaa~"): tiếng ngáp — có nên áp quy tắc fa/fu (ふぁ→"phà") hay giữ nguyên dạng ngáp tự nhiên? Đưa vào đợt thống nhất fa/fu cùng ハチロクh6 + lr_ふかみh2.
- 2680 Olivy gọi Soutetsu "cậu" (trong khi 2589/2663 gọi "anh"): giữ nguyên theo tiền lệ ハチロク06 — Hieu có muốn thống nhất Olivy→Soutetsu thành "anh" toàn dự án không?
- Không có câu hỏi thuật ngữ mới khác, không còn đại từ mơ hồ nào chưa quyết, không có dòng JP dở dang nào cần Hieu hoàn thiện (2426 đã sửa theo TW).

## Kết bài

File ハチロク03_冥国式レイルロオド đã audit xong toàn bộ 490 dòng: 58 dòng sai (11,8%) — thuật ngữ 32 (Minh Quốc/Meriken 19, Ohito→Ohitoyo 7, Yui→Yunoi 2 riêng + 3 kiêm, Teitetsu 1, Bổn tiểu thư 3), đại từ 10 (Soutetsu với Olivy 9, Hibiki với Olivy 1), đại từ + thuật ngữ 2, gasp sweep 9, sai nghĩa 2, lỗi nhỏ 1, SFX 2. Không lệch dòng, không xoay chuỗi, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 58 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 58/58 giá trị fix đã đọc lại đối chiếu JP, 0 bỏ, 0 sửa giá trị (chỉ chỉnh 2 câu lý do 2456/3317 cho chính xác, không đổi giá trị fix). Chờ Hieu: Hinamoto 10 dòng (đợt thống nhất), 2149 fa/fu ngáp, 2680 Olivy "cậu" với Soutetsu.
