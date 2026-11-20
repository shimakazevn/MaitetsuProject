# Audit — ハチロク14_冬.txt.toml (Hachiroku 14, mùa đông)

- File: `translation_toml/01_Hachiroku/ハチロク14_冬.txt.toml` (đường dẫn đĩa: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af14_#U51ac.txt.toml`)
- Route: 01_Hachiroku. 660 dòng script. Nội dung: đêm trực tuyết — Olivy sốt cao vẫn cố trực, giấu nhiệt độ bằng thạch một miếng; nước giếng lẫn cát ở nhiều nhà, nghi núi lửa Shin'endake hoạt động, lập ca trực 24h (3 ca × 8 tiếng); Hachiroku–Soutetsu bàn về "truyền đạt lại" và việc được nhớ đến.
- Phương pháp: đọc từng dòng (row-by-row) đối chiếu JP + TW (JP thắng khi khác nhau), kiểm tra chuỗi xoay, nhiễm chéo, dòng mồ côi, trùng khóa, thẻ %l, sweep っ-gasp của file, xưng hô theo quy tắc Soutetsu đã sửa 20/11.

## Kết quả tổng

- Đọc: **660 dòng**, sai: **39 dòng (5,9%)**.
- Phân loại (39): gasp っ 12 (2385, 2386, 2515, 2551, 2552, 3154, 3623, 3861, 4104 từ sweep + 1760, 2590, 2690 sweep bỏ sót/sai phân loại), xưng hô/đại từ 12 (2573, 3143, 3190, 3202, 3256, 3257 Paulette→Soutetsu trái B4 lock + 2420, 2711, 2833, 2949, 3219 Soutetsu + 2684 Olivy), thuật ngữ/gloss %l 13 (機関士 9, タブレット 3, 氏子 1, 運転体 1 — 3983 gộp 2 gloss trong 1 dòng), sai nghĩa/bịa 1 (3777), SFX 1 (2549).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3: 1 set duy nhất (660 dòng, khớp TOML tuyệt đối; 5 chênh lệch chỉ là ký tự `\n` literal, 0 khác biệt thực chất). `[selections]` rỗng. Không có thẻ `%l` sai định dạng (đếm mở/đóng bằng nhau trong TOML).
- TOML md5: `b1d3343faed4a0f9fb1b27caa54db204` (132.033 byte, UTF-8 BOM). Không có bản sao file này (không trùng md5 với file nào khác).
- Sweep: 9 mục cho file, đã kiểm chứng từng mục vs JP và nhận cả 9 (2385, 2386, 2515, 2551, 2552, 3154, 3623, 3861, 4104 — VN hiện tại vẫn bằng đúng old_vn của sweep, tức sweep chưa được áp vào file này). Ngoài ra bắt thêm 3 gasp sweep bỏ sót/sai phân loại: 1760 (っ――ぁ), 2590 (っ / っっっ), 2690 (sweep ghi 'already-rendered' là sai — xem chi tiết dưới).
- Thuật ngữ chờ đợt thống nhất, KHÔNG tính sai: "Ohito" 8 dòng (1780, 2587, 2774, 2918 ×2, 3680, 3747, 3843, 4147) + "Yui" (湯医) 1 dòng (3680).

## Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix vs JP)

- Tổng: 39 / kiểm chứng lại: 39 / bỏ: 0 / sửa: 0.
- Khối TOML đã parse-verified (tomllib): 39 khóa, 0 sai lệch giá trị so với JSON. jp/tw/old_vn khớp CSV3 tuyệt đối 39/39. Mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (diff-sanity đã chạy máy).

## Danh sách sửa (39)

### 1760 — オリヴィ [gasp っ]

- JP: 「……っ――ぁ――。\nごめん、ね？　おどろかせちゃったよね」
- TW: 「……嗚——啊，抱歉，嚇到你了吧」
- VN cũ: 「……A——.\nXin lỗi, nhé? Làm cậu giật mình rồi nhỉ.」
- Sửa: 「……Ư——A——.\nXin lỗi, nhé? Làm cậu giật mình rồi nhỉ.」
- Lý do: JP っ――ぁ―― có 2 âm (gasp + a dài); TW 嗚——啊 cũng 2 âm; VN chỉ còn 'A——', mất gasp.

### 2342 — 日々姫 [thuật ngữ/gloss %l]

- JP: 「実際にお見舞いしたのはニイロクだけだったけど。\n赤井\x%l機関士;#00ffc040;機関士%l;#;、買い物に付き合わされたって」
- TW: 「不過就二六上去看了看奧莉薇，赤井\x%l機関士;#00ffc040;司機%l;#;是陪她買東西一起來的」
- VN cũ: 「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\n\x%l機関士;#00ffc040;Nhân viên cơ vụ%l;#; Akai bảo là bị kéo đi mua sắm cùng.」
- Sửa: 「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\n\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai bảo là bị kéo đi mua sắm cùng.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 2371 — 日々姫 [thuật ngữ/gloss %l]

- JP: 「ニイロク、すぐおりてきて、『お邪魔した』って。\nあんまり早くて、赤井\x%l機関士;#00ffc040;機関士%l;#;も驚いた顔しとった」
- TW: 「二六隨時就下來準備回去，那這速度快得，把赤井\x%l機関士;#00ffc040;司機%l;#;都給嚇一跳」
- VN cũ: 「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\nNhanh quá mức khiến \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai cũng phải tròn mắt ngạc nhiên.」
- Sửa: 「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\nNhanh quá mức khiến \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cũng phải tròn mắt ngạc nhiên.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 2385 — オリヴィ [gasp っ]

- JP: 「体にドクって、だからオリヴィ――っ！」
- TW: 「什麼好不好，反正奧莉薇已經——！」
- VN cũ: 「Có hại cho cơ thể, thế nên Olivy——!」
- Sửa: 「Có hại cho cơ thể, thế nên Olivy——Ư!」
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ, VN giữ dấu gạch nhưng mất gasp.

### 2386 — 双鉄 [gasp っ]

- JP: 「っ！！？」\n「！！？」
- TW: 「什麼！！？」\n「啊！！？」
- VN cũ: 「!!?」\n「!!?」
- Sửa: 「Ư!!?」\n「!!?」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！！？」 cả dòng là gasp, VN chỉ còn dấu câu.

### 2420 — 双鉄 [xưng hô/đại từ]

- JP: 「あまりよく眠れなかったのか？」
- TW: 「你昨天沒睡好嗎？」
- VN cũ: 「Em ngủ không được ngon giấc sao?」
- Sửa: 「Cô ngủ không được ngon giấc sao?」
- Lý do: Người nói Soutetsu; người nghe là Olivy (2419/2423-2427 đều xoay quanh Olivy) hoặc Hachiroku — cả hai Soutetsu đều gọi 'cô' (2427, 2510). 'Em' sai cả hai cách đọc.

### 2474 — オリヴィ [thuật ngữ/gloss %l]

- JP: 「いっても同じ。\nこれ、\x%lタブレット;#00ffc040;タブレット%l;#;がもうボロボロなせいだから」
- TW: 「去哪都一樣，奧莉薇這是因為\x%lタブレット;#00ffc040;操作板%l;#;已經不堪重負了」
- VN cũ: 「Đến đó cũng vậy thôi.\nCái này, là do \x%lタブレット;#00ffc040;thẻ bảng%l;#; đã tơi tả rồi.」
- Sửa: 「Đến đó cũng vậy thôi.\nCái này, là do \x%lタブレット;#00ffc040;máy tính bảng%l;#; đã tơi tả rồi.」
- Lý do: Gloss %l cho タブレット: thuật ngữ đã chốt 操作板/タブレット='máy tính bảng'; 'thẻ bảng' là dịch sai — TW 操作板.

### 2497 — 日々姫 [thuật ngữ/gloss %l]

- JP: 「短かかったと！　赤井\x%l機関士;#00ffc040;機関士%l;#;を放ってもおけんけん\nわたし、ここでお茶お出ししとったんだけど」
- TW: 「可不是唄！我又不能晾著赤井\x%l機関士;#00ffc040;司機%l;#;，這不還給人泡了茶吶」
- VN cũ: 「Ngắn lắm luôn! Em không thể bỏ mặc \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai được\nnên đã pha trà mời ở đây, nhưng mà.」
- Sửa: 「Ngắn lắm luôn! Em không thể bỏ mặc \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai được\nnên đã pha trà mời ở đây, nhưng mà.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 2515 — 双鉄 [gasp っ]

- JP: 「っ！？」
- TW: 「呃！？」
- VN cũ: 「!?」
- Sửa: 「Ư!?」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！？」 cả dòng là gasp.

### 2549 — 双鉄 [SFX]

- JP: 「うぅ……今日は冷え込むな」
- TW: 「唔……今天氣溫可真低」
- VN cũ: 「Ư……Hôm nay lạnh quá nhỉ.」
- Sửa: 「Ưư……Hôm nay lạnh quá nhỉ.」
- Lý do: JP うぅ…… là tiếng rên dài 2 âm tiết; VN 'Ư' chỉ 1 âm, mất độ dài. Cùng mẫu với 2592 ううっ→'Ưư' trong chính file này.

### 2551 — 双鉄 [gasp っ]

- JP: 「っ！」
- TW: 「唔！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！」 cả dòng là gasp.

### 2552 — 双鉄 [gasp っ]

- JP: 「っ！」\n「あ」
- TW: 「唔！」\n「啊」
- VN cũ: 「!」\n「A」
- Sửa: 「Ư!」\n「A」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！」 dòng 1 là gasp; dòng 2 「あ」→'A' giữ nguyên.

### 2573 — ポーレット [xưng hô/đại từ]

- JP: 「あ！　双鉄くんっ」
- TW: 「啊！雙鐵君」
- VN cũ: 「A! Cậu Soutetsu.」
- Sửa: 「A! Anh Soutetsu.」
- Lý do: B4 lock: Paulette→Soutetsu 双鉄くん = 'anh Soutetsu'. VN 'Cậu Soutetsu' trái quy tắc đã chốt.

### 2590 — オリヴィ [gasp っ]

- JP: 「っ」\n「っっっ！！！？」
- TW: 「嗚」\n「嗚嗚！！！？」
- VN cũ: 「!」\n「!!!?」
- Sửa: 「Ư」\n「Ưưư!!!?」
- Lý do: Sweep BỎ SÓT: JP 「っ」⏎「っっっ！！！？」 — gasp cả 2 dòng, VN chỉ còn dấu câu. Dòng 2 có 3 っ nên 'Ưưư' (theo JP; TW chỉ có 2 嗚 — điểm cần Hieu xem lại).

### 2684 — オリヴィ [xưng hô/đại từ]

- JP: 「って、思うの。だけど、現場は今朝見たときには\n全然変化してなくて、それでオリヴィどうしていいか」
- TW: 「奧莉薇也是這麼認為的，但是今早查看的時候現場還沒有任何變化，所以就不知道該怎麼辦了」
- VN cũ: 「Chị cũng nghĩ vậy. Nhưng mà, hiện trường sáng nay lúc xem\nthì hoàn toàn không có gì thay đổi, nên Olivy không biết phải làm sao.」
- Sửa: 「Tôi cũng nghĩ vậy. Nhưng mà, hiện trường sáng nay lúc xem\nthì hoàn toàn không có gì thay đổi, nên Olivy không biết phải làm sao.」
- Lý do: Người nói Olivy, trả lời Soutetsu (2682/2685): tự xưng 'chị' với Soutetsu là sai; Olivy dùng 'tôi' với Soutetsu trong cả file (2692, 2729).

### 2690 — オリヴィ [gasp っ]

- JP: 「オリヴィ！　ソーテツ起こしてくっ――っ！！！？」
- TW: 「奧莉薇這就去叫雙鐵起來——！！！？」
- VN cũ: 「Olivy! Sẽ đi đánh thức Soutetsu——!!!?」
- Sửa: 「Olivy! Sẽ đi đánh thức Soutetsu——Ư!!!?」
- Lý do: Sweep phân loại 'already-rendered' là SAI: cùng mẫu trailing ――っ như 3861/4104 (sweep đã sửa), VN dòng này không có Ư hay âm tương đương nào; っ đầu (起こしてくっ) là nhấn mạnh, giữ nguyên.

### 2711 — 双鉄 [xưng hô/đại từ]

- JP: 「わかった」
- TW: 「好」
- VN cũ: 「Anh biết rồi.」
- Sửa: 「Tôi biết rồi.」
- Lý do: Người nói Soutetsu, đáp lại Olivy (2710 'わかったー'); Soutetsu gọi Olivy là 'cô' 10× trong file (2427, 2885, 2986...) nên tự xưng 'tôi'. Chỉ khi người nghe là Hibiki mới là 'anh', mà 2713 Hibiki mở chủ đề mới, không liên quan.

### 2740 — 赤井 [thuật ngữ/gloss %l]

- JP: 「必要があれば、氏子さんにも協力をお願いできます」
- TW: 「如果有需要，我會請求信徒協助」
- VN cũ: 「Nếu cần thiết, tôi có thể nhờ các giáo dân giúp đỡ.」
- Sửa: 「Nếu cần thiết, tôi có thể nhờ các tín đồ của đền giúp đỡ.」
- Lý do: 氏子 = dân của đền Shinto (ujiko); 'giáo dân' gợi nhà thờ Công giáo. TW 信徒 (tín đồ). Sửa thành 'tín đồ của đền' theo ngữ cảnh 宮司='đền chủ'.

### 2833 — 双鉄 [xưng hô/đại từ]

- JP: 「僕もわからん。\n小さな菓子でもはいっていそうな容器だが」
- TW: 「我也不清楚，看起來是一個用來裝小零食之類的容器」
- VN cũ: 「Anh cũng không biết.\nTrông giống hộp đựng mấy loại bánh kẹo nhỏ ấy.」
- Sửa: 「Tôi cũng không biết.\nTrông giống hộp đựng mấy loại bánh kẹo nhỏ ấy.」
- Lý do: Người nói Soutetsu, nói với Hachiroku (2831/2835 Hachiroku kẹp hai bên); Soutetsu 'tôi' với Hachiroku.

### 2851 — 双鉄 [thuật ngữ/gloss %l]

- JP: 「赤井\x%l機関士;#00ffc040;機関士%l;#;には、お二方と凪と情報を出し合って、\n常時監視候補者のリスト作成をお願いしたく思います」
- TW: 「我希望赤井\x%l機関士;#00ffc040;司機%l;#;能和凪還有流和治兩位先生交換意見，完成參與全天監視的成員候補名單」
- VN cũ: 「Tôi muốn nhờ \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\nđể lập danh sách các ứng viên giám sát thường trực.」
- Sửa: 「Tôi muốn nhờ \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\nđể lập danh sách các ứng viên giám sát thường trực.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 2920 — 日々姫 [thuật ngữ/gloss %l]

- JP: 「だよ？　昨日、赤井\x%l機関士;#00ffc040;機関士%l;#;といっしょに」
- TW: 「是呀，昨天跟赤井\x%l機関士;#00ffc040;司機%l;#;一起來的」
- VN cũ: 「Đúng vậy? Hôm qua, cùng với \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai đó.」
- Sửa: 「Đúng vậy? Hôm qua, cùng với \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai đó.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 2949 — 双鉄 [xưng hô/đại từ]

- JP: 「なにか気づいたのか？」
- TW: 「有什麼發現了？」
- VN cũ: 「Em nhận ra điều gì sao?」
- Sửa: 「Cô nhận ra điều gì sao?」
- Lý do: Người nói Soutetsu, hỏi Olivy (2947 Olivy 'あのひと'); Soutetsu gọi Olivy là 'cô' 10× trong file, 'em' ở đây là ngoại lệ sai.

### 2997 — 双鉄 [thuật ngữ/gloss %l]

- JP: 「諦めるには早すぎる。例えば明日、\x%lタブレット;#00ffc040;タブレット%l;#;に関する\n新しい知見が発見されるかもしれない」
- TW: 「現在還沒到放棄的時候，說不定明天就會有關於\x%lタブレット;#00ffc040;操作板%l;#;的新發現」
- VN cũ: 「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\nsẽ phát hiện ra kiến thức mới liên quan đến \x%lタブレット;#00ffc040;thẻ bảng%l;#; thì sao.」
- Sửa: 「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\nsẽ phát hiện ra kiến thức mới liên quan đến \x%lタブレット;#00ffc040;máy tính bảng%l;#; thì sao.」
- Lý do: Gloss %l cho タブレット: như 2474 — thuật ngữ đã chốt 'máy tính bảng', TW 操作板.

### 3143 — ポーレット [xưng hô/đại từ]

- JP: 「そっちは、双鉄くん――ううん、\n運輸部長兼\x%l保線部長;#00ffc040;保線部長%l;#;に、全権委任でお願いできますか？」
- TW: 「這些就，雙鐵君——不，我公司的運輸部長兼\x%l保線部長;#00ffc040;巡線部長%l;#;，這些能否全權交由你來規劃？」
- VN cũ: 「Bên đó thì, cậu Soutetsu——à không,\nTrưởng bộ phận Vận tải kiêm \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;, tôi có thể ủy quyền toàn bộ cho cậu được không?」
- Sửa: 「Bên đó thì, anh Soutetsu——à không,\nTrưởng bộ phận Vận tải kiêm \x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;, tôi có thể ủy quyền toàn bộ cho anh được không?」
- Lý do: B4 lock: Paulette→Soutetsu 双鉄くん = 'anh Soutetsu' — sửa cả 2 chỗ 'cậu' trong dòng (xưng hô + 'ủy quyền cho cậu').

### 3154 — ハチロク [gasp っ]

- JP: 「っ！」
- TW: 「這！」
- VN cũ: 「!」
- Sửa: 「Ư!」
- Lý do: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！」 cả dòng là gasp.

### 3155 — 双鉄 [thuật ngữ/gloss %l]

- JP: 「赤井\x%l機関士;#00ffc040;機関士%l;#;もか」
- TW: 「連赤井\x%l機関士;#00ffc040;司機%l;#;都來了嗎」
- VN cũ: 「Cả \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai nữa sao.」
- Sửa: 「Cả \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai nữa sao.」
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 3190 — ポーレット [xưng hô/đại từ]

- JP: 「お願いします。あのね？　オリヴィちゃん。\nいま、双鉄くんとかわるから」
- TW: 「那就交給你了，奧莉薇聽我說，我這就讓雙鐵君聽電話」
- VN cũ: 「Nhờ cậu nhé. Này? Bé Olivy.\nBây giờ chị đổi máy cho cậu Soutetsu nha.」
- Sửa: 「Nhờ cậu nhé. Này? Bé Olivy.\nBây giờ chị đổi máy cho anh Soutetsu nha.」
- Lý do: B4 lock: Paulette→Soutetsu = 'anh Soutetsu'. 'Nhờ cậu nhé' đầu dòng (nói với Olivy) GIỮ NGUYÊN — cần Hieu chốt cách gọi Paulette→Olivy.

### 3202 — ポーレット [xưng hô/đại từ]

- JP: 「では、お任せします。情報共有は三時間おき定時で。\n状況に大きな変化があった場合には、逐次で願います」
- TW: 「那就拜託你了，每隔三小時定期報告彼此的進展，如果情況有變，請一一通知我」
- VN cũ: 「Vậy, tôi giao phó cho cậu. Chia sẻ thông tin định kỳ mỗi ba tiếng một lần.\nNếu tình hình có thay đổi lớn, xin hãy báo cáo ngay lập tức.」
- Sửa: 「Vậy, tôi giao phó cho anh. Chia sẻ thông tin định kỳ mỗi ba tiếng một lần.\nNếu tình hình có thay đổi lớn, xin hãy báo cáo ngay lập tức.」
- Lý do: B4 lock: Paulette ủy quyền + dặn lịch báo cáo 3 tiếng — người nghe là Soutetsu (chỉ huy hiện trường, vừa được toàn quyền ở 3143), nên 'anh'. (Nếu người nghe là Hachiroku/Nagi thì phải là 'em' — điểm cần Hieu xem lại.)

### 3219 — 双鉄 [xưng hô/đại từ]

- JP: 「では、いってくる」
- TW: 「那我們出門了」
- VN cũ: 「Vậy, anh đi đây.」
- Sửa: 「Vậy, tôi đi đây.」
- Lý do: Người nói Soutetsu, chào lúc ra đi; câu ngay sau (3220) 'Nhờ cô nhé' cho thấy người nghe là Hachiroku ('cô') nên tự xưng 'tôi'.

### 3256 — ポーレット [xưng hô/đại từ]

- JP: 「双鉄くん、これ」
- TW: 「雙鐵君，你看這些」
- VN cũ: 「Cậu Soutetsu, xem cái này đi.」
- Sửa: 「Anh Soutetsu, xem cái này đi.」
- Lý do: B4 lock: Paulette→Soutetsu 双鉄くん = 'anh Soutetsu'.

### 3257 — ポーレット [xưng hô/đại từ]

- JP: 「双鉄くん。\nこれ、どの程度の話でしょうか？」
- TW: 「雙鐵君，這個情況嚴重嗎？」
- VN cũ: 「Cậu Soutetsu.\nChuyện này nghiêm trọng đến mức nào vậy?」
- Sửa: 「Anh Soutetsu.\nChuyện này nghiêm trọng đến mức nào vậy?」
- Lý do: B4 lock: Paulette→Soutetsu 双鉄くん = 'anh Soutetsu'.

### 3623 — monologue [gasp っ]

- JP: ぱっと花咲く笑顔を浮かべ、オリヴィは――っ！？
- TW: 只見奧莉薇眉開眼笑，然後——！？
- VN cũ: Nở nụ cười tươi như hoa, Olivy——!?
- Sửa: Nở nụ cười tươi như hoa, Olivy——Ư!?
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ！？, VN mất gasp.

### 3757 — monologue [thuật ngữ/gloss %l]

- JP: \x%lタブレット;#00ffc040;タブレット%l;#;の損傷ならば、直せない。\n登呂流湯さんにも、不死鳥博士にも、他の誰にも。
- TW: 如果是\x%lタブレット;#00ffc040;操作板%l;#;的問題，那我們便無計可施，即使換成登呂流浴場老闆和不死鳥博士，或是什麼其他人，都同樣無能為力。
- VN cũ: Nếu là \x%lタブレット;#00ffc040;thẻ bảng%l;#; bị hỏng, thì không thể sửa được.\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy.
- Sửa: Nếu là \x%lタブレット;#00ffc040;máy tính bảng%l;#; bị hỏng, thì không thể sửa được.\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy.
- Lý do: Gloss %l cho タブレット: như 2474 — thuật ngữ đã chốt 'máy tính bảng', TW 操作板.

### 3777 — monologue [sai nghĩa/bịa]

- JP: 『オリヴィちゃんの望んだこと』と、\nわたくしの[あね,1]義姉と[いもうと,1]義妹も、やはり静かに受け入れましょう。
- TW: 就算她再也回不到那個家了，我家的姐姐和妹妹也都會理解這是她自己的選擇，進而默默接受。
- VN cũ: Nếu là 『điều bé Olivy mong muốn』,\nthì chị gái và em gái nuôi của em, chắc chắn cũng sẽ lặng lẽ chấp nhận thôi.
- Sửa: Nếu là 『điều bé Olivy mong muốn』,\nthì chị chồng và em chồng của em, chắc chắn cũng sẽ lặng lẽ chấp nhận thôi.
- Lý do: 義姉/義妹 bị dịch 'nuôi' là bịa của Gemini: TW chỉ nói 姐姐和妹妹 (không có 養) — 義 ở đây là quan hệ dâu/rể, không phải con nuôi. Người nói là Hachiroku (わたくし); 義姉/義妹 của cô là chị/em gái của Soutetsu = Mayami (chị) và Hibiki (em) → 'chị chồng/em chồng' (hai người đã là vợ chồng, cf. 4073 'vợ mình').

### 3854 — monologue [thuật ngữ/gloss %l]

- JP: 手短に要点だけを確認し、\n電話を切って、赤井\x%l機関士;#00ffc040;機関士%l;#;へと向き直る。
- TW: 我就簡單問了一下他們對主要情況的了解程度，而後掛上電話再次向赤井\x%l機関士;#00ffc040;司機%l;#;開口。
- VN cũ: Tôi xác nhận ngắn gọn những điểm chính,\nrồi cúp máy, quay sang \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai.
- Sửa: Tôi xác nhận ngắn gọn những điểm chính,\nrồi cúp máy, quay sang \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai.
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 3861 — monologue [gasp っ]

- JP: 必死に駆け寄り、\n倒れてしまったオリヴィちゃんを――っ！？
- TW: 我拚命趕了過去，想將她扶起——
- VN cũ: Em tuyệt vọng chạy đến,\nđỡ lấy bé Olivy đang gục ngã——!?
- Sửa: Em tuyệt vọng chạy đến,\nđỡ lấy bé Olivy đang gục ngã——Ư!?
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ！？, VN mất gasp.

### 3983 — monologue [thuật ngữ/gloss %l]

- JP: 確かに、\x%l運転体;#00ffc040;運転体%l;#;では買い物にも不自由しよう。\n赤井\x%l機関士;#00ffc040;機関士%l;#;も、いつもながらとはいえご苦労なことだ。
- TW: 的確，二六隻有\x%l運転体;#00ffc040;駕駛體%l;#;，購物時也多有不便。雖然估計赤井\x%l機関士;#00ffc040;司機%l;#;也是習以為常，但仔細一想著實也是不容易。
- VN cũ: Đúng là, với \x%l運転体;#00ffc040;kíp lái%l;#; thì việc mua sắm cũng bất tiện.\n\x%l機関士;#00ffc040;Nhân viên cơ vụ%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật.
- Sửa: Đúng là, với \x%l運転体;#00ffc040;thân vận hành%l;#; thì việc mua sắm cũng bất tiện.\n\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật.
- Lý do: Dòng này có 2 gloss sai: 運転体 'kíp lái' → 'thân vận hành' (đây là THÂN vận hành, không phải tổ lái; TW 駕駛體) và 機関士 'Nhân viên cơ vụ' → 'Thợ lái đầu máy' (thuật ngữ đã chốt; TW 司機).

### 4065 — monologue [thuật ngữ/gloss %l]

- JP: ポーレット様に、れいなに、ニイロクに、赤井\x%l機関士;#00ffc040;機関士%l;#;に。\n縁ある全ての存在に、今の言葉を、ただ、届けたい。
- TW: 還有波萊特小姐、玲奈、二六、赤井\x%l機関士;#00ffc040;司機%l;#;，以及其他所有與御一夜密不可分的人們，都聽到她方才這句飽含喜悅的話語。
- VN cũ: Cho cô Paulette, cho Reina, cho Niiroku, cho \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; Akai.\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ.
- Sửa: Cho cô Paulette, cho Reina, cho Niiroku, cho \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai.\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ.
- Lý do: Gloss %l cho 機関士: thuật ngữ đã chốt là 'thợ lái đầu máy'; 'nhân viên cơ vụ' (nhân viên tổ) vừa mơ hồ vừa sai nghĩa — TW 司機 (lái tàu).

### 4104 — monologue [gasp っ]

- JP: なにかが爆発したような音――っ！！？
- TW: 驚天動地的響聲傳入耳中，像是哪裡發生了爆炸！！？
- VN cũ: Âm thanh như thể có thứ gì đó phát nổ——!!?
- Sửa: Âm thanh như thể có thứ gì đó phát nổ——Ư!!?
- Lý do: Sweep lost-gasp-trailing đã kiểm chứng vs JP: trailing ――っ！！？, VN mất gasp.

## Các dòng đã kiểm tra nhưng GIỮ NGUYÊN (không tính sai)

- 2532 ふぇ → "Hả!?": ふぇ là tiếng ngạc nhiên, "Hả!?" diễn đúng cảm xúc, nhất quán với えっ→"Hả!?" ở 2533. Quy tắc fa/fu (ふぇ→"phuê") là mặc định, không phải khuôn đóng — cách diễn ngẫu hứng này giữ được.
- 2327: JP bị cắt ngang ("きっと、みんなもオリヴィのこと"), VN hoàn thiện "Chắc chắn, mọi người cũng nghĩ về Olivy" theo hướng TW ("大家肯定也都一樣") — không phải bịa vô căn cứ.
- 2427 "Ông lão có cách nói chuyện giống tôi": có căn cứ — 2577 JP ghi rõ ご老人 ("ông lão"), người đó chính là ông lão nói giọng giống Soutetsu.
- 2536/2559/2561: các tiếng ấp úng (えと、あの、んと) diễn thành "ừm/ờm" — diễn đạt ngẫu hứng, giữ được tính ngập ngừng.
- 2643 んふふっ → "Ưfufu.": tiếng cười, diễn thành tiếng cười đúng quy tắc (không thành tiếng rên).
- 2396/2783/3169/3096/3757 "Tororyu-yu": 3 dạng xưng hô ("ông chủ nhà tắm Tororyu-yu", "ngài Tororyu-yu", "ông Tororyu-yu") cho cùng một nhà tắm được nhân cách hóa (登呂流湯さん/様) — không nhất quán nhưng đều chấp nhận được, ghi chú cho đợt thống nhất, không tính sai.
- 3153/3262 おじーちゃん/おじいちゃん → "ông lão": đây là "nhà ông lão" (ngôi nhà), không phải từ xưng hô họ hàng, nên không dính câu hỏi "ông nội hay ông ngoại" đang chờ Hieu chốt cho 爺ちゃん (Seki).
- 2714 "Cảm ơn ý tốt của em": người nghe là Hibiki (người rủ đi xe đạp, cf. 3071) — "em" đúng.
- 3074 "anh sẽ cõng hoặc bế em": người nghe là Hibiki — "anh/em" đúng.
- 2887 "anh Munakata": Soutetsu gọi Munakata (đàn anh) là "anh" — hợp lý, không có quy tắc khóa trái.
- 2423 Hachiroku gọi Olivy là "Cô ngậm sẵn..." — xưng "cô" trang trọng trong câu hỏi trực tiếp, chấp nhận được (không sửa).
- 1780/2587/2774/2918/3680/3747/3843/4147 "Ohito" + 3680 "Yui": chờ đợt thống nhất (xem trên).

## Điểm cần Hieu xem lại (không tự quyết)

- 2590 "Ưưư!!!?": JP có 3 っ, TW chỉ có 2 嗚. Đã theo JP (3 âm). Nếu muốn theo TW thì đổi thành "Ưư!!!?".
- 3202 "giao phó cho anh": đã chốt người nghe là Soutetsu (ủy quyền + dặn lịch báo cáo 3 tiếng = chỉ huy hiện trường). Nếu người nghe thực ra là Hachiroku/Nagi thì phải sửa thành "em".
- 3190 "Nhờ cậu nhé": Paulette nói với Olivy — "cậu" giữ nguyên. Cách gọi Paulette→Olivy ("cậu" vs "bé/em") chưa có quy tắc khóa, cần Hieu chốt.
- 3777 "chị chồng và em chồng": đã chốt 義姉/義妹 là chị/em gái của Soutetsu (Mayami/Hibiki), không phải "nuôi" (TW không có 養). Hieu xem lại cách gọi này có hợp không.
- 2690: sweep phân loại "already-rendered" nhưng VN dòng này không có Ư nào — audit đã sửa theo cùng mẫu trailing ――っ như 3861/4104. Hieu lưu ý sweep có sai phân loại.
- 2711 "Tôi biết rồi": đã chốt người nghe là Olivy (đáp lại 2710). Nếu người nghe là Hibiki thì phải là "Anh biết rồi".

## Khối TOML (đã parse-verified, 39 khóa, 0 sai lệch)

```toml
[script]
"1760" = "「……Ư——A——.\\nXin lỗi, nhé? Làm cậu giật mình rồi nhỉ.」"
"2342" = "「Nhưng người thực sự đến thăm chỉ có Niiroku thôi.\\n\\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai bảo là bị kéo đi mua sắm cùng.」"
"2371" = "「Niiroku xuống ngay lập tức, rồi bảo 『Xin lỗi vì đã làm phiền』.\\nNhanh quá mức khiến \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cũng phải tròn mắt ngạc nhiên.」"
"2385" = "「Có hại cho cơ thể, thế nên Olivy——Ư!」"
"2386" = "「Ư!!?」\\n「!!?」"
"2420" = "「Cô ngủ không được ngon giấc sao?」"
"2474" = "「Đến đó cũng vậy thôi.\\nCái này, là do \\x%lタブレット;#00ffc040;máy tính bảng%l;#; đã tơi tả rồi.」"
"2497" = "「Ngắn lắm luôn! Em không thể bỏ mặc \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai được\\nnên đã pha trà mời ở đây, nhưng mà.」"
"2515" = "「Ư!?」"
"2549" = "「Ưư……Hôm nay lạnh quá nhỉ.」"
"2551" = "「Ư!」"
"2552" = "「Ư!」\\n「A」"
"2573" = "「A! Anh Soutetsu.」"
"2590" = "「Ư」\\n「Ưưư!!!?」"
"2684" = "「Tôi cũng nghĩ vậy. Nhưng mà, hiện trường sáng nay lúc xem\\nthì hoàn toàn không có gì thay đổi, nên Olivy không biết phải làm sao.」"
"2690" = "「Olivy! Sẽ đi đánh thức Soutetsu——Ư!!!?」"
"2711" = "「Tôi biết rồi.」"
"2740" = "「Nếu cần thiết, tôi có thể nhờ các tín đồ của đền giúp đỡ.」"
"2833" = "「Tôi cũng không biết.\\nTrông giống hộp đựng mấy loại bánh kẹo nhỏ ấy.」"
"2851" = "「Tôi muốn nhờ \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai cùng hai ông ấy và Nagi trao đổi thông tin,\\nđể lập danh sách các ứng viên giám sát thường trực.」"
"2920" = "「Đúng vậy? Hôm qua, cùng với \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai đó.」"
"2949" = "「Cô nhận ra điều gì sao?」"
"2997" = "「Bỏ cuộc bây giờ là quá sớm. Ví dụ như ngày mai, có thể\\nsẽ phát hiện ra kiến thức mới liên quan đến \\x%lタブレット;#00ffc040;máy tính bảng%l;#; thì sao.」"
"3143" = "「Bên đó thì, anh Soutetsu——à không,\\nTrưởng bộ phận Vận tải kiêm \\x%l保線部長;#00ffc040;Trưởng bộ phận bảo trì đường ray%l;#;, tôi có thể ủy quyền toàn bộ cho anh được không?」"
"3154" = "「Ư!」"
"3155" = "「Cả \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai nữa sao.」"
"3190" = "「Nhờ cậu nhé. Này? Bé Olivy.\\nBây giờ chị đổi máy cho anh Soutetsu nha.」"
"3202" = "「Vậy, tôi giao phó cho anh. Chia sẻ thông tin định kỳ mỗi ba tiếng một lần.\\nNếu tình hình có thay đổi lớn, xin hãy báo cáo ngay lập tức.」"
"3219" = "「Vậy, tôi đi đây.」"
"3256" = "「Anh Soutetsu, xem cái này đi.」"
"3257" = "「Anh Soutetsu.\\nChuyện này nghiêm trọng đến mức nào vậy?」"
"3623" = "Nở nụ cười tươi như hoa, Olivy——Ư!?"
"3757" = "Nếu là \\x%lタブレット;#00ffc040;máy tính bảng%l;#; bị hỏng, thì không thể sửa được.\\nCả ông Tororyu-yu, Tiến sĩ Fushicho, hay bất kỳ ai khác cũng vậy."
"3777" = "Nếu là 『điều bé Olivy mong muốn』,\\nthì chị chồng và em chồng của em, chắc chắn cũng sẽ lặng lẽ chấp nhận thôi."
"3854" = "Tôi xác nhận ngắn gọn những điểm chính,\\nrồi cúp máy, quay sang \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai."
"3861" = "Em tuyệt vọng chạy đến,\\nđỡ lấy bé Olivy đang gục ngã——Ư!?"
"3983" = "Đúng là, với \\x%l運転体;#00ffc040;thân vận hành%l;#; thì việc mua sắm cũng bất tiện.\\n\\x%l機関士;#00ffc040;Thợ lái đầu máy%l;#; Akai, dù là chuyện thường ngày nhưng cũng vất vả thật."
"4065" = "Cho cô Paulette, cho Reina, cho Niiroku, cho \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; Akai.\\nEm chỉ muốn truyền đạt lại những lời vừa rồi, cho tất cả những người có duyên gặp gỡ."
"4104" = "Âm thanh như thể có thứ gì đó phát nổ——Ư!!?"
```

## Kết bài

File ハチロク14_冬.txt.toml: 660 dòng đã đọc hết, sai 39 dòng (5,9%). Lỗi tập trung ở 3 cụm: gasp っ bị mất (12, trong đó sweep bỏ sót 3), xưng hô Paulette→Soutetsu trái B4 lock (6) và Soutetsu tự xưng "anh"/gọi "em" lạc khỏi mẫu tôi–cô của file (5 + 1 Olivy tự xưng "chị"), gloss %l sai thuật ngữ đã chốt (13, chủ yếu 機関士→"nhân viên cơ vụ" 9 dòng). Không có lệch dòng, chuỗi xoay hay nhiễm chéo — bản dịch file này nhìn chung trung thực, lỗi là rời rạc chứ không hệ thống. Cần Hieu xem 6 điểm đã nêu trên trước khi gộp.
