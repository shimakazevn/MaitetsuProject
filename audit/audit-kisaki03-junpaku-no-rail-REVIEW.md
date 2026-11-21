# Audit — 稀咲03_純白のレール.txt.toml (route 06_Kisaki)

- File: `稀咲03_純白のレール.txt.toml` — route 06_Kisaki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b203_#U7d14#U767d#U306e#U30ec#U30fc#U30eb.txt.toml`
- Số dòng script: **425** (độc thoại 192, 双鉄 86, 稀咲 47, 日々姫 35, ハチロク 18, 浦上 17, ポーレット 14, 元忠 11, 凪 2, ふかみ 1, 真闇 1, れいな 1). Đọc toàn bộ 425/425 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: họp bàn quỹ My Rail kỳ 1 (bán hết ngay, 10.000+ đơn xin, ~1–5 tỷ yên), phương án kỳ 2 khôi phục tuyến Ohitoyo–Yatsushiro tạo đường vòng với Đường sắt Mikan, ý tưởng mua lại toàn bộ tuyến của Đường sắt Ohitoyo để tập trung bảo trì; Hibiki gọi Soutetsu là "anh trai" và kể chuyện "người bạn" để thúc anh tỏ tình; tàu du lịch đầu tiên chạy, Soutetsu tỏ tình với Kisaki trước mặt mọi người ở ga, Urakami tiết lộ mình là nữ giả nam; kết bằng lời hẹn cùng nhau trải "đường ray thuần khiết".
- **Kết quả: 29/425 dòng sai (6,8%)** — tương đương file 02 cùng route (6,5%). Không có chuỗi xoay, không lệch vị trí.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN == TW (2 dòng 1351/1352 chỉ là dấu "……" nên VN == JP == TW là đúng). TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 221 giá trị TOML đã flatten `\n` literal thành khoảng trắng (220 thuần + 1 dòng 2031 " \n" → 1 khoảng trắng); CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `80f8a824e798ff9ca1e5377a7a6248d4`. Không có bản sao của file này trong 11 nhóm trùng. `[selections]` rỗng.

## Phân loại (29)

| Loại | Số dòng | Keys |
|---|---|---|
| Thuật ngữ (terminology) | 14 | 1690, 2713, 2098, 1908, 1874, 1906, 2704, 2903, 2513, 2891, 1657, 1882 (御一夜 địa danh → Ohitoyo, 12 dòng), 77 (運転体 → thân vận hành), 2869 (機関士代理) |
| Đại từ (pronoun) | 4 | 1818, 1827, 1956, 2029 (Soutetsu với Kisaki = tôi / cô) |
| Sai nghĩa (meaning) | 1 | 1762 |
| SFX | 3 | 1750, 1752, 2721 |
| Thở gấp (gasp) | 3 | 2146, 2147, 2461 (cả 3 từ sweep, đã kiểm chứng) |
| Thẻ %l (tag) | 2 | 2038, 2632 (khôi phục thẻ %l エアクラ bị rớt) |
| Dấu câu (punctuation) | 2 | 1755, 1938 |

Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0, cụt câu 0.

## §1. Thuật ngữ — 御一夜 địa danh → Ohitoyo (12)

Sửa trong audit theo tiền lệ file 02 cùng route (11 dòng, trong đó có cả 1 dòng tên công ty 2038) và nhiều file khác; KHÔNG thêm lại vào hàng đợi thống nhất. Riêng 7 dòng tên công ty "Đường sắt Ohito" (1624, 2565, 1957, 1963, 2894 + phần công ty trong 1906, 1882) GIỮ NGUYÊN theo quyết 21/11 17:30 — chờ đợt thống nhất (xem §8.4). Hai dòng 1906, 1882 mang cả hai: chỉ sửa phần địa danh, phần công ty giữ nguyên.

### 1690 [稀咲] — 御一夜 ×2
- JP: 「鉄道、金融、行政に。古い御一夜と新しい御一夜に。\n\x%lエアクラ;#00ffc040;エアクラ%l;#;社にまで――キミは、強力な人脈を持っている」
- TW: 「你有強大的人脈，從鐵路、金融到行政，從老御一夜到新御一夜，連\x%lエアクラ;#00ffc040;空凝機%l;#;公司裡都有」
- VN cũ: 「Đường sắt, tài chính, hành chính. Ohimitera cũ và Ohimitera mới. Thậm chí cả công ty \x%lエアクラ;#00ffc040;Aircra%l;#;——anh có một mạng lưới nhân mạch vô cùng mạnh mẽ.」
- Fix: 「Đường sắt, tài chính, hành chính. Ohitoyo cũ và Ohitoyo mới. Thậm chí cả công ty \x%lエアクラ;#00ffc040;Aircra%l;#;——anh có một mạng lưới nhân mạch vô cùng mạnh mẽ.」
- Lý do: 御一夜 (địa danh) → "Ohitoyo" theo quy tắc đã chốt.

### 2713 [monologue]
- JP: なにせ稀咲は隈元銀行御一夜支店の、\n誰もが認める優れたリーダーなのだから。
- TW: 畢竟稀咲本人可是人人都認可的隈元銀行御一夜支行的優秀領導。
- VN cũ: Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Kumagin chi nhánh Ohimitera mà.
- Fix: Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Kumagin chi nhánh Ohitoyo mà.

### 2098 [稀咲]
- JP: 「困ったよね、即完売になってしまったから。\n[マイレールファンド,2]ＭＲＦ第一期：御一夜-[かごしま,2]鹿兒島復線ファンドが」
- TW: 「這可就令人頭痛了。因為第一期私有線路基金：御一夜——鹿兒島線剛一發布就被認購一空了」
- VN cũ: 「Đau đầu thật đấy, vì đã bán hết sạch ngay lập tức rồi. Quỹ MRF kỳ 1: Quỹ khôi phục tuyến Ohimitera - Kagoshima ấy.」
- Fix: 「Đau đầu thật đấy, vì đã bán hết sạch ngay lập tức rồi. Quỹ MRF kỳ 1: Quỹ khôi phục tuyến Ohitoyo - Kagoshima ấy.」

### 1908 [ポーレット]
- JP: 「圧倒的に御一夜-[やつしろ,2]八ツ城間です。ここを復線できれば、\nみかん鉄道さんの線路と環状になりますから」
- TW: 「必須是御一夜到八代。如果能讓這裡的廢線恢復，就可以和橙鐵路的線路形成環線」
- VN cũ: 「Áp đảo nhất là đoạn Ohimitera - Yatsushiro. Nếu có thể khôi phục tuyến đường này,\nnó sẽ tạo thành một tuyến đường vòng tròn với tuyến đường của Đường sắt Mikan.」
- Fix: 「Áp đảo nhất là đoạn Ohitoyo - Yatsushiro. Nếu có thể khôi phục tuyến đường này,\nnó sẽ tạo thành một tuyến đường vòng tròn với tuyến đường của Đường sắt Mikan.」

### 1874 [ハチロク]
- JP: 「あの、ポーレット様、悩んでらしたではないですか。\n御一夜-[かごしま,2]鹿兒島間の\x%l保線;#00ffc040;保線%l;#;について」
- TW: 「對了，波萊特小姐，你不是很頭痛從御一夜到鹿兒島之間線路的\x%l保線;#00ffc040;巡線%l;#;問題嗎」
- VN cũ: 「À này, Thị trưởng Paulette, chẳng phải ngài đang đau đầu sao.\nVề việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; đoạn Ohimitera - Kagoshima ấy ạ.」
- Fix: 「À này, Thị trưởng Paulette, chẳng phải ngài đang đau đầu sao.\nVề việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; đoạn Ohitoyo - Kagoshima ấy ạ.」
- Ghi chú: ポーレット様 → "Thị trưởng Paulette" giữ nguyên (tiền lệ Grand 06: "Thịnh trưởng Paulette" → "Thị trưởng Paulette").

### 1906 [双鉄] — chỉ sửa phần địa danh
- JP: 「御一夜鉄道の……御一夜-[ゆのい,1]湯医間をか？」
- TW: 「御一夜鐵路的……是說御一夜到湯醫嗎？」
- VN cũ: 「Của Đường sắt Ohito…… đoạn Ohimitera - Yunoi sao?」
- Fix: 「Của Đường sắt Ohito…… đoạn Ohitoyo - Yunoi sao?」
- Lý do: phần địa danh sửa theo quy tắc; phần tên công ty "Đường sắt Ohito" giữ nguyên chờ đợt thống nhất (quyết 21/11 17:30).

### 2704 [monologue]
- JP: そしてキュウっと赤線で、\n湯医-御一夜-鹿兒島間を大きな丸で囲ってしまう。
- TW: 然後在湯醫——御一夜——鹿兒島之間畫了一個大大的紅圈。
- VN cũ: Sau đó, bằng một đường kẻ đỏ,\ncô ấy khoanh một vòng tròn lớn bao quanh đoạn Yunoi - Ohimitera - Kagoshima.
- Fix: Sau đó, bằng một đường kẻ đỏ,\ncô ấy khoanh một vòng tròn lớn bao quanh đoạn Yunoi - Ohitoyo - Kagoshima.

### 2903 [monologue]
- JP: となると、御一夜-鹿兒島間をどう手当するか――
- TW: 那，應該怎麼處理御一夜到鹿兒島的部分呢——
- VN cũ: Vậy thì, đoạn Ohimitera - Kagoshima sẽ xử lý ra sao đây——
- Fix: Vậy thì, đoạn Ohitoyo - Kagoshima sẽ xử lý ra sao đây——

### 2513 [monologue]
- JP: 復線が成り、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の千内移転が決定し。\n御一夜-鹿兒島間の観光\x%l列車;#00ffc040;列車%l;#;が走りだす。
- TW: 我們成功恢復了廢線，讓\x%lエアクラ;#00ffc040;空凝機%l;#;工廠決定改在川內落戶。從御一夜到鹿兒島的觀光\x%l列車;#00ffc040;列車%l;#;也即將啟動。
- VN cũ: Khôi phục tuyến đường thành công, nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\nChuyến \x%l列車;#00ffc040;tàu%l;#; du lịch đoạn Ohimitera - Kagoshima bắt đầu lăn bánh.
- Fix: Khôi phục tuyến đường thành công, nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\nChuyến \x%l列車;#00ffc040;tàu%l;#; du lịch đoạn Ohitoyo - Kagoshima bắt đầu lăn bánh.
- Ghi chú: gloss 列車 "tàu" giữ nguyên, ghi vào §8.5 (không nhất quán với 1702/1797/2551 dùng "đoàn tàu").

### 2891 [monologue]
- JP: 僕が御一夜に舞い戻ってきたあの日には、\n夢に描くことさえなかった光景だ。
- TW: 這是我回到御一夜那天，做夢也不會想到的場景。
- VN cũ: Vào cái ngày tôi trở về Ohimitera,\nđây là một khung cảnh mà tôi thậm chí còn chưa từng mơ tới.
- Fix: Vào cái ngày tôi trở về Ohitoyo,\nđây là một khung cảnh mà tôi thậm chí còn chưa từng mơ tới.

### 1657 [稀咲]
- JP: 「じゃないでしょ。危なっかしいなぁ。\n御一夜に戻ってきて緩んじゃった？」
- TW: 「什麼叫太熱了。真不讓人省心。一回到御一夜就鬆懈了？」
- VN cũ: 「Nóng nực gì chứ. Nguy hiểm thật đấy.\nVừa quay lại Ohimitera là đã lơi lỏng rồi sao?」
- Fix: 「Nóng nực gì chứ. Nguy hiểm thật đấy.\nVừa quay lại Ohitoyo là đã lơi lỏng rồi sao?」

### 1882 [ハチロク] — chỉ sửa phần địa danh
- JP: 「『第一期追加募集;\n（株）御一夜鉄道稼働中路線・御一夜-湯医間』ですか」
- TW: 「就叫“第一期追加集資：御一夜鐵路股份公司運營中的路線·御一夜至湯醫路段”嗎」
- VN cũ: 「『Đợt huy động bổ sung kỳ 1;\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohito・Đoạn Ohimitera - Yunoi』 sao ạ.」
- Fix: 「『Đợt huy động bổ sung kỳ 1;\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohito・Đoạn Ohitoyo - Yunoi』 sao ạ.」
- Lý do: như 1906 — phần tên công ty giữ nguyên chờ đợt thống nhất.

## §2. Thuật ngữ — 運転体, 機関士代理 (2)

### 77 [monologue] — 運転体 → "thân vận hành"
- JP: キャブの窓から、\x%l運転体;#00ffc040;運転体%l;#;のハチロクの顔。
- TW: \x%l運転体;#00ffc040;駕駛體%l;#;狀態的八六從駕駛室探出腦袋。
- VN cũ: Từ cửa sổ buồng lái, khuôn mặt của Hachiroku trong trạng thái \x%l運転体;#00ffc040;cơ thể vận hành%l;#; ló ra.
- Fix: Từ cửa sổ buồng lái, khuôn mặt của Hachiroku trong trạng thái \x%l運転体;#00ffc040;thân vận hành%l;#; ló ra.
- Lý do: 運転体 là thân thể (vật) của Railord — Hachiroku thò mặt ra khỏi buồng lái trong trạng thái thân vận hành; "cơ thể vận hành" là biến thể lẻ duy nhất toàn dự án (1 lần). Tiền lệ Common 08: 運転体 → "thân vận hành" 5 dòng, ghi rõ "'kíp lái' sai, đó là thân thể không phải kíp người"; khớp quy tắc 運転ボディ = "thân vận hành". Toàn dự án 運転体 đang lộn xộn: "kíp lái" 26×, "thân chính" 5×, "thân điều khiển" 3×, "cơ thể vận hành" 1× — xem §8.6.

### 2869 [monologue] — 機関士代理 → "lái tàu tạm quyền"
- JP: 証券上に記載されている文字列を見れば、\n日々姫が初めて\x%l機関士;#00ffc040;機関士%l;#;代理を任された時の言葉を思い出す。
- TW: 證券上印的字，讓我想起了日日姬第一次被任命為代理\x%l機関士;#00ffc040;司機%l;#;時說的話。
- VN cũ: Nhìn vào dòng chữ được ghi trên chứng khoán, tôi chợt nhớ lại lời nói của Hibiki khi lần đầu tiên được giao làm đại lý \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;.
- Fix: Nhìn vào dòng chữ được ghi trên chứng khoán, tôi chợt nhớ lại lời nói của Hibiki khi lần đầu tiên được giao làm lái tàu tạm quyền \x%l機関士;#00ffc040;lái tàu%l;#;.
- Lý do: hai lỗi trong một dòng. (1) 代理 = tạm quyền/đại diện, không phải "đại lý" — "đại lý" thuộc lĩnh vực thương mại, sai y như quyết 代理車掌 → "trưởng tàu đại diện" (21/11). (2) 機関士 = "lái tàu" (dạng ngắn đã chốt; gloss đa số toàn dự án: "lái tàu" ~197× vs "nhân viên cơ vụ" 37×; TW gloss 司機 = người lái); "nhân viên cơ vụ" mơ hồ, mất nghĩa "lái".

## §3. Đại từ — Soutetsu với Kisaki = "tôi" / "cô" (4)

Quy tắc đã chốt (brief + Grand 11 đã parent-kiểm chứng: 2173 "em"→"cô", 2347 "anh"→"tôi"): Soutetsu với Kisaki xưng "tôi", gọi cô là "cô". File này đã dùng đúng "tôi"/"cô" ở 1627 ("tôi không muốn giao cô cho ai cả"), 1936 ("Cô hãy luôn ở bên cạnh tôi"), 2012, 1928, 2057 — chỉ 4 dòng dưới đây lệch.

### 1818 [双鉄] — câu tỏ tình
- JP: 「好きだ。僕は。君が――宝生稀咲が、好きだ」
- TW: 「喜歡。我喜歡你——喜歡寶生稀咲」
- VN cũ: 「Anh thích em. Anh——thích em, Houshou Kisaki.」
- Fix: 「Tôi thích cô. Tôi——thích cô, Houshou Kisaki.」
- Lý do: cả tự xưng lẫn cách gọi đều sai quy tắc. Trong chính cảnh tỏ tình, 1627 và 1936 đã dùng "tôi"/"cô", nên 1818 là dòng lạc điệu duy nhất — không có ngoại lệ "lãng mạn" cho quy tắc này (tiền lệ h3: sửa 50/50 "anh"→"tôi" với Kisaki, kể cả cảnh H).

### 1827 [双鉄]
- JP: 「ん……稀咲、なんだ？　なにか」
- TW: 「嗯……稀咲，怎麼了？你想說什麼」
- VN cũ: 「Ưm…… Kisaki, sao vậy? Em muốn nói gì à.」
- Fix: 「Ưm…… Kisaki, sao vậy? Cô muốn nói gì à.」
- Lý do: JP không có đại từ; VN cũ tự thêm "em". Soutetsu gọi Kisaki "cô".

### 1956 [双鉄]
- JP: 「だから……我慢か？」
- TW: 「所以……才要忍著？」
- VN cũ: 「Thế nên…… em mới nhẫn nhịn sao?」
- Fix: 「Thế nên…… cô mới nhẫn nhịn sao?」
- Lý do: người nghe là Kisaki (cô trả lời ở 1998). "Em" chỉ đúng với Hibiki/Hachiroku. Toàn file Soutetsu gọi Kisaki "cô" 4 dòng (2012, 1928, 1627, 1936) vs "em" 3 dòng (1818, 1827, 1956) — sửa 3 dòng "em" về "cô" cho nhất quán.
- Ghi chú: file 01/h3 giữ "em" cho Soutetsu→Kisaki — mâu thuẫn này ghi vào §8.2 để đợt thống nhất rà lại toàn tuyến.

### 2029 [双鉄]
- JP: 「説明会を、頑張るよ」
- TW: 「發布會我會加油的」
- VN cũ: 「Anh sẽ cố gắng hết sức cho buổi thuyết trình.」
- Fix: 「Tôi sẽ cố gắng hết sức cho buổi thuyết trình.」
- Lý do: người nghe là Kisaki (2042 Soutetsu gọi "Kisaki——", 1980 Kisaki đáp). Soutetsu với Kisaki = "tôi".

## §4. Sai nghĩa (1)

### 1762 [日々姫] — すごっ ≠ "nhiều quá"
- JP: 「わ――すごっ」
- TW: 「哇，好厲害」
- VN cũ: 「Oa——nhiều quá.」
- Fix: 「Oa——ghê thật.」
- Lý do: すごっ = kinh ngạc/tuyệt vời (TW 好厲害 xác nhận); VN cũ bịa thêm ý số lượng ("nhiều") mà JP không có. Hibiki đang trầm trồ trước núi bưu phẩm — "ghê thật" diễn đúng sự kinh ngạc, không thêm nghĩa.

## §5. SFX (3)

### 1750 [稀咲] — うふふっ → "Ufufu"
- JP: 「うふふっ、双鉄」
- TW: 「呵呵呵，雙鐵」
- VN cũ: 「Fufu, anh Soutetsu.」
- Fix: 「Ufufu, anh Soutetsu.」
- Lý do: tiền lệ h8: ふふっ → "fufu", うふふっ → "ufufu" — VN cũ làm mất âm う đầu ("không để mất âm"). Cách gọi "anh Soutetsu" giữ nguyên, xem §8.1.

### 1752 [真闇] — うふふぅ → "Ufufuu"
- JP: 「うふふぅ、おめでと、ふたりとも」
- TW: 「呵呵，恭喜你們」
- VN cũ: 「Fufu, chúc mừng nhé, hai đứa.」
- Fix: 「Ufufuu, chúc mừng nhé, hai đứa.」
- Lý do: うふふぅ = うふふ + ぅ kéo dài → "Ufufuu"; "Fufu" làm mất cả âm う đầu lẫn độ dài cuối.

### 2721 [monologue] — ふふっと trong lời dẫn
- JP: 頷けば、ふふっと嬉しげな顔。
- TW: 看到我同意她的說法，稀咲開心地笑了。
- VN cũ: Thấy tôi gật đầu, cô ấy nở nụ cười vui vẻ, fufu.
- Fix: Thấy tôi gật đầu, cô ấy cười khúc khích đầy vui vẻ.
- Lý do: "fufu" treo cuối câu lời dẫn tiếng Việt nghe như người kể đang cười; tiếng cười ふふっと phải diễn thành tiếng cười ("cười khúc khích"), không để romaji lẻ.

## §6. Thở gấp — sweep (3, áp nguyên đã kiểm chứng)

Sweep có 3 mục cho file này, cả 3 đều đúng giá trị, áp nguyên:

### 2146 [双鉄] — lost-gasp-whole
- JP: 「っ！」 — TW: 「！」
- VN cũ: 「!」 — Fix: 「Ư!」

### 2147 [双鉄] — lost-gasp-whole
- JP: 「っ！！？」 — TW: 「！！？」
- VN cũ: 「!!?」 — Fix: 「Ư!!?」

### 2461 [monologue] — lost-gasp-trailing
- JP: そうだ、今日は浦上さんもまた千内から来てくれるのだ。\n僕も、挨拶しないわけには――っ！
- TW: 對啊，今天浦上經理也會再次從川內趕來。我也得去打個招呼才行——！
- VN cũ: Đúng rồi, hôm nay anh Urakami cũng sẽ lại từ Sendai đến đây.\nTôi cũng phải đi chào hỏi mới được——!
- Fix: Đúng rồi, hôm nay anh Urakami cũng sẽ lại từ Sendai đến đây.\nTôi cũng phải đi chào hỏi mới được——Ư!
- Ghi chú: không có gasp nào sweep bỏ sót trong file này — đã quét toàn bộ 425 dòng, các っ còn lại đều đã được diễn đạt (Ư/Ưm/Kh/—) hoặc không phải gasp (っ cuối từ nội dung như ブロワーっ không có trong file; 1636 僕はっ―― đã có dấu gạch diễn đạt ngắt câu).

## §7. Thẻ %l + dấu câu (4)

### 2038 [双鉄] — khôi phục thẻ %l エアクラ
- JP: 「マイレールファンド一期はありがとうございました。\n\x%lエアクラ;#00ffc040;エアクラ%l;#;・ヒノモトの社員持株会さんのおかげで――」
- TW: 「私有線路基金第一期的時候真的謝謝您了。都是多虧日本\x%lエアクラ;#00ffc040;空凝機%l;#;公司的員工持股計劃——」
- VN cũ: 「Cảm ơn anh rất nhiều về quỹ My Rail kỳ 1. Nhờ có hội sở hữu cổ phần nhân viên của Aircra Hinomoto mà——」
- Fix: 「Cảm ơn anh rất nhiều về quỹ My Rail kỳ 1. Nhờ có hội sở hữu cổ phần nhân viên của \x%lエアクラ;#00ffc040;Aircra%l;#; Hinomoto mà——」
- Lý do: VN bỏ mất thẻ %l của JP cho エアクラ. Tiền lệ file 01 cùng route đã khôi phục 2 thẻ tương tự (1775, 2325); toàn dự án giữ thẻ 342/351 dòng (chỉ 9 dòng rớt, trong đó 5 dòng ở ハチロク13 chưa audit).

### 2632 [monologue] — khôi phục thẻ %l エアクラ
- JP: \x%lエアクラ;#00ffc040;エアクラ%l;#;・ヒノモトの社員なら誰にでもわかるその事実が、\n持株会のマイレールファンドへの信用を高めたらしい。
- TW: 日本\x%lエアクラ;#00ffc040;空凝機%l;#;公司的職員都明白這件事，這也加深了員工持股計劃對我們的信任。
- VN cũ: Bất kỳ nhân viên nào của Aircra Hinomoto cũng hiểu được sự thật đó,\nvà có vẻ như điều này đã làm tăng thêm sự tin tưởng của hội sở hữu cổ phần đối với quỹ My Rail.
- Fix: Bất kỳ nhân viên nào của \x%lエアクラ;#00ffc040;Aircra%l;#; Hinomoto cũng hiểu được sự thật đó,\nvà có vẻ như điều này đã làm tăng thêm sự tin tưởng của hội sở hữu cổ phần đối với quỹ My Rail.
- Lý do: như 2038. Hai dòng JP có thẻ %l mà VN thêm thẻ (1946 無碍, 1332 運転台) đều là chuyển ruby [むげ,1]/[キャブ,2] của JP thành thẻ %l — đúng mẫu của file, không sửa.

### 1755 [双鉄] — dấu câu
- JP: 「え？　あっ！？　喉っ」
- TW: 「咦？啊！？喉——」
- VN cũ: 「Hả? Á!? Cổ họng.」
- Fix: 「Hả? Á!? Cổ họng!」
- Lý do: 喉っ là câu cảm thán trong ngữ cảnh 「あっ！？」; dấu "." làm mất sắc thái, phải là "!".

### 1938 [双鉄] — dấu câu
- JP: 「僕が、どうかしたか？」
- TW: 「我怎麼了？」
- VN cũ: 「Anh, làm sao?」
- Fix: 「Anh làm sao thế?」
- Lý do: "Anh, làm sao?" gãy ngữ pháp tiếng Việt; JP/TW đều là "có chuyện gì với tôi vậy?" — người nghe là Hibiki, "anh" đúng.

## §8. Chờ Hieu / đợt thống nhất (không tự quyết)

### 8.1. Kisaki gọi Soutetsu "anh Soutetsu" — GIỮ NGUYÊN, chờ Hieu
- Trong file này Kisaki gọi Soutetsu "anh Soutetsu" 9 dòng (2141, 2050, 1760, 2125, 1744, 1750, 1930, 1980, 1979) + 1 dòng gọi "anh" không kèm tên (1793 "anh đến thật này") — nội bộ file NHẤT QUÁN, 0 lần "cậu Soutetsu", 0 lần tên trần.
- Brief ghi Kisaki gọi "cậu"/tên trần (Common 14 + Grand 11: 1664, 2459, 2617 đã parent-kiểm chứng), nhưng hai audit gần nhất cùng tuyến (file 02: 10 dòng, h3: 33 dòng) đều GIỮ NGUYÊN "anh Soutetsu" và cờ cho Hieu; toàn tuyến Kisaki dùng "anh Soutetsu" 135 dòng, "cậu Soutetsu" 0 dòng. Đổi 9 dòng trong file này một mình sẽ phá nhất quán nội tuyến — đây là quyết định toàn tuyến, thuộc đợt thống nhất (như review h3 đã nêu). Không sửa dòng nào.

### 8.2. Soutetsu gọi Kisaki "em" vs "cô" — đã sửa theo brief, nhưng ghi nhận mâu thuẫn
- Audit này sửa 3 dòng "em"→"cô" (1818, 1827, 1956) theo brief + Grand 11 (2173, parent-kiểm chứng) + file 02 ("Soutetsu gọi Kisaki 'cô'") + đa số nội file (4 "cô" vs 3 "em").
- Nhưng file 01 và h3 đã GIỮ "em" cho Soutetsu→Kisaki (01: "nhất quán toàn file, phù hợp hướng thống nhất 'cô'→'em' đang chờ"; h3: 0 fix "em"→"cô"). Nếu đợt thống nhất quyết "em" cho tuyến Kisaki thì 3 fix này + Grand 11: 2173 cần rà lại.

### 8.3. Kisaki tự xưng "tôi" hay "em" với Soutetsu — GIỮ NGUYÊN, chờ Hieu (câu hỏi đang chờ từ file 01)
- File này là bằng chứng sạch cho giả thuyết "theo ngữ cảnh": Kisaki xưng "tôi" 3 dòng khi nói với Soutetsu về công việc (2034 "Tôi hiểu rồi. Tôi sẽ liên lạc ngay.", 1847 "Vì tôi có cảm giác...", 1934 "Tôi và…… Urakami?") vs xưng "em" 7 dòng trong cảnh thân mật sau tỏ tình (1877, 1881, 1930, 1965, 1979, 1998, 2027). Các dòng "tôi" còn lại đều đúng: với Urakami (1842, 2145, 1843) hoặc "tôi" làm tân ngữ (1744 "Anh, thích tôi.").
- Không sửa dòng nào — chờ Hieu chốt (file 01 + 02 đã cờ câu hỏi này; toàn dự án Kisaki "tôi" 284 vs "em" 247).

### 8.4. Tên công ty "Đường sắt Ohito" — chờ đợt thống nhất (7 dòng)
- 1624, 2565, 1957, 1963, 2894 + phần công ty trong 1906, 1882. JP đều là 御一夜鉄道. Giữ nguyên theo quyết 21/11 17:30 ("Đường sắt Ohito" → "Đường sắt Ohitoyo", 236 dòng toàn dự án, chờ đợt thống nhất). Lưu ý: file 02 đã sửa 1 dòng công ty trong audit (2038) trước quyết này; đợt thống nhất đối chiếu lại để khỏi đếm trùng.

### 8.5. Gloss 列車 "tàu" vs "đoàn tàu" — chờ đợt thống nhất (3 dòng)
- 2513, 2923, 1918 dùng gloss "tàu" ("Chuyến tàu du lịch", "chuyến đi bằng tàu"); 1702, 1797, 2551 dùng "đoàn tàu". Nội dung hiển thị "chuyến tàu" vẫn tự nhiên nên không tính sai — chỉ ghi nhận không nhất quán gloss, đợt thống nhất chuẩn hoá (tiền lệ 真闇02: 1113 gloss → "đoàn tàu").

### 8.6. 運転体 toàn dự án — cần quyết một lần (file này chỉ sửa 1 dòng)
- File này: 77 "cơ thể vận hành" → "thân vận hành" (theo tiền lệ Common 08). Toàn dự án 運転体 đang có 5 cách dịch: "kíp lái" 26× (SAI — đó là thân thể, không phải kíp người; Common 08 đã kết luận), "thân chính" 5×, "thân điều khiển" 3×, "thân vận hành" (Common 08/13 + file này), "cơ thể vận hành" 1×. Đề xuất đợt thống nhất: "thân vận hành" (khớp 運転ボディ).

### 8.7. 2912 義理 → "anh em nuôi" — GIỮ NGUYÊN, chờ điều tra 義
- JP: 義理とはいえど兄妹だから、言語感覚もいつの間にやら、似通ってきたのかもしれん。TW: 雖然我們不是親兄妹，但畢竟一起待了那麼久，說話的風格大概也相似起來了。VN: "Dù chỉ là anh em nuôi nhưng vẫn là anh em, có lẽ cảm quan ngôn ngữ cũng đã trở nên giống nhau từ lúc nào không hay."
- 義 → "nuôi" là mẫu bịa đã biết của Gemini, nhưng câu hỏi 義姉/義妹 "nuôi" vs "kế" đang được điều tra toàn dự án (TW 繼姐/繼妹) và chưa chốt — không sửa một mình dòng này. Ghi nhận: TW ở đây chỉ nói 不是親兄妹 (không cùng huyết thống), không nói 養 (nuôi).

### 8.8. Các dòng đã kiểm chứng là ĐÚNG (không sửa, ghi để khỏi rà lại)
- 2892 堰さん → "ông Seki" (Seki ở đây là tình nguyện viên bảo trì, không phải vai ông ngoại — quy tắc "ông ngoại" chỉ áp 5 dòng đã liệt kê: 共通12 2182, ハチロク05 1178, グランド06 2159, 凪ふかみ02_命の重さ 2299, ハチロク07 2679).
- 2094 日ノ本 → "Hinomoto" đúng (không còn "Hinamoto" trong file).
- 1874 ポーレット様 → "Thị trưởng Paulette" đúng (tiền lệ Grand 06).
- 2104 大廃線 → "Đại bãi bỏ tuyến" đúng (dạng chuẩn toàn dự án, hàng chục dòng).
- 1799/1911/2126 Hibiki gọi Soutetsu 兄さん → "anh trai" đúng — cố tình khác にぃにぃ ("anh hai") thường ngày, Soutetsu cũng nhận ra sự khác lạ (2413/2640).
- 1950 "Houshou bên tôi" (うちの宝生) giữ — câu cụt theo JP (――), không sửa.
- 1946 無碍 → "phũ phàng" giữ; 1946/1332 thêm thẻ %l từ ruby của JP giữ.
- 2943 (ポーーーーーっ！) → "(Tuúúúúú!)" giữ — tiếng còi tàu bản địa hoá; 76 ボッ、ボッ → "xình, xịch" giữ.
- 1884 giọng Nagi ("lúc nàaaaao") giữ; 2134 おめでとーーーっ → "Chúc mừng hai người——!" giữ (dấu gạch + ! đã diễn đạt kéo dài + ngắt).
- 浦上 xưng "anh Urakami" suốt file giữ — Soutetsu tưởng Urakami là nam cho đến 2651 mới vỡ lẽ; đó chính là nút thắt của cảnh.
- 1351/1352 chỉ có dấu "……" giữ nguyên (VN == JP == TW là đúng, không phải chưa dịch).

## §9. Kiểm chứng cấu trúc

- 0 lệch vị trí: không dòng VN nào là bản dịch của dòng JP khác (đã đối chiếu từng dòng; không có cặp hoán đổi).
- 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng mồ côi (mọi VN đều khớp một JP trong file; không có VN "lạc" từ file khác).
- 0 dòng chưa dịch: VN trống 0; 2 dòng VN == TW (1351, 1352) chỉ là dấu câu.
- 0 trùng khóa: 425 key duy nhất trong CSV3 và trong TOML.
- TOML khớp CSV3 tuyệt đối modulo flatten `\n`→khoảng trắng đã biết (221 dòng, gồm 2031 " \n"→1 khoảng trắng). CSV3 là authoritative.
- %l: 0 thẻ hỏng trong file (mở = đóng ở mọi dòng); 2 thẻ JP bị VN bỏ (2038, 2632) đã sửa; 2 thẻ VN thêm từ ruby JP (1946, 1332) giữ.
- Sweep: 3/3 mục áp nguyên đã kiểm chứng trực tiếp với JP; 0 mục bị bác; 0 gasp sweep bỏ sót (đã quét toàn bộ 425 dòng).
- Đại từ đã kiểm chứng toàn file: Soutetsu "anh" với Hibiki (1694, 1932, 1938, 2135, 1335, 1974, 1947 — đều đúng), "tôi" với Hachiroku (1995, 2058, 1332, 2099), với nhóm (2118, 2066, 2072); Hibiki "em"/"anh hai"; Hachiroku "em"/"ngài Soutetsu"; Nagi "anh hai" (1855); Reina "anh Soutetsu"/"chị Kisaki" (2137).

## Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 29 fix đối chiếu trực tiếp với JP của từng dòng (không chỉ parse-check): **29 tổng / 29 soát lại đạt / 0 bỏ / 0 sửa**. Trong lượt soát 2, kiểm tra thêm: không fix nào thay đổi ngoài phần cần sửa (diff-sanity cơ học: mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa, chênh lệch ≤30 ký tự); JP/TW/old_vn trong JSON khớp CSV3 tuyệt đối 29/29; khối TOML 29 khóa parse đạt, 0 sai lệch giá trị.

## Khối TOML (đã parse-kiểm chứng: 29 khóa, 0 sai lệch giá trị)

```toml
"1690" = "「Đường sắt, tài chính, hành chính. Ohitoyo cũ và Ohitoyo mới. Thậm chí cả công ty \\x%lエアクラ;#00ffc040;Aircra%l;#;——anh có một mạng lưới nhân mạch vô cùng mạnh mẽ.」"
"2713" = "Dù sao thì Kisaki cũng là một nhà lãnh đạo xuất sắc được mọi người công nhận của Kumagin chi nhánh Ohitoyo mà."
"2098" = "「Đau đầu thật đấy, vì đã bán hết sạch ngay lập tức rồi. Quỹ MRF kỳ 1: Quỹ khôi phục tuyến Ohitoyo - Kagoshima ấy.」"
"1908" = "「Áp đảo nhất là đoạn Ohitoyo - Yatsushiro. Nếu có thể khôi phục tuyến đường này,\\nnó sẽ tạo thành một tuyến đường vòng tròn với tuyến đường của Đường sắt Mikan.」"
"1874" = "「À này, Thị trưởng Paulette, chẳng phải ngài đang đau đầu sao.\\nVề việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#; đoạn Ohitoyo - Kagoshima ấy ạ.」"
"1906" = "「Của Đường sắt Ohito…… đoạn Ohitoyo - Yunoi sao?」"
"2704" = "Sau đó, bằng một đường kẻ đỏ,\\ncô ấy khoanh một vòng tròn lớn bao quanh đoạn Yunoi - Ohitoyo - Kagoshima."
"2903" = "Vậy thì, đoạn Ohitoyo - Kagoshima sẽ xử lý ra sao đây——"
"2513" = "Khôi phục tuyến đường thành công, nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; quyết định chuyển đến Sendai.\\nChuyến \\x%l列車;#00ffc040;tàu%l;#; du lịch đoạn Ohitoyo - Kagoshima bắt đầu lăn bánh."
"2891" = "Vào cái ngày tôi trở về Ohitoyo,\\nđây là một khung cảnh mà tôi thậm chí còn chưa từng mơ tới."
"1657" = "「Nóng nực gì chứ. Nguy hiểm thật đấy.\\nVừa quay lại Ohitoyo là đã lơi lỏng rồi sao?」"
"1882" = "「『Đợt huy động bổ sung kỳ 1;\\nTuyến đường đang hoạt động của Công ty CP Đường sắt Ohito・Đoạn Ohitoyo - Yunoi』 sao ạ.」"
"77" = "Từ cửa sổ buồng lái, khuôn mặt của Hachiroku trong trạng thái \\x%l運転体;#00ffc040;thân vận hành%l;#; ló ra."
"2869" = "Nhìn vào dòng chữ được ghi trên chứng khoán, tôi chợt nhớ lại lời nói của Hibiki khi lần đầu tiên được giao làm lái tàu tạm quyền \\x%l機関士;#00ffc040;lái tàu%l;#;."
"1818" = "「Tôi thích cô. Tôi——thích cô, Houshou Kisaki.」"
"1827" = "「Ưm…… Kisaki, sao vậy? Cô muốn nói gì à.」"
"1956" = "「Thế nên…… cô mới nhẫn nhịn sao?」"
"2029" = "「Tôi sẽ cố gắng hết sức cho buổi thuyết trình.」"
"1762" = "「Oa——ghê thật.」"
"1750" = "「Ufufu, anh Soutetsu.」"
"1752" = "「Ufufuu, chúc mừng nhé, hai đứa.」"
"2721" = "Thấy tôi gật đầu, cô ấy cười khúc khích đầy vui vẻ."
"2146" = "「Ư!」"
"2147" = "「Ư!!?」"
"2461" = "Đúng rồi, hôm nay anh Urakami cũng sẽ lại từ Sendai đến đây.\\nTôi cũng phải đi chào hỏi mới được——Ư!"
"2038" = "「Cảm ơn anh rất nhiều về quỹ My Rail kỳ 1. Nhờ có hội sở hữu cổ phần nhân viên của \\x%lエアクラ;#00ffc040;Aircra%l;#; Hinomoto mà——」"
"2632" = "Bất kỳ nhân viên nào của \\x%lエアクラ;#00ffc040;Aircra%l;#; Hinomoto cũng hiểu được sự thật đó,\\nvà có vẻ như điều này đã làm tăng thêm sự tin tưởng của hội sở hữu cổ phần đối với quỹ My Rail."
"1755" = "「Hả? Á!? Cổ họng!」"
"1938" = "「Anh làm sao thế?」"
```

## Kết bài

File 稀咲03_純白のレール: đọc 425/425 dòng, sai **29 dòng (6,8%)** — thuật ngữ 14, đại từ 4, sai nghĩa 1, SFX 3, thở gấp 3 (cả 3 từ sweep), thẻ %l 2, dấu câu 2. Không lệch vị trí, không chuỗi xoay — trái hẳn với file 01 cùng route (47,0% với chuỗi xoay 173 dòng): file này dịch cẩn thận hơn hẳn, lỗi tập trung ở thuật ngữ cũ Ohimitera (12/29) và cụm đại từ Soutetsu–Kisaki. Lượt soát 2: 29/29/0/0. Khối TOML 29 khóa parse đạt, 0 sai lệch. Chờ Hieu: Kisaki gọi "anh Soutetsu" (9 dòng + 1793), Kisaki tự xưng "tôi" hay "em" với Soutetsu (bằng chứng mới: công việc "tôi" 3 dòng vs thân mật "em" 7 dòng), tên công ty "Đường sắt Ohito" 7 dòng chờ đợt thống nhất, gloss 列車 "tàu" 3 dòng, 運転体 "kíp lái" 26× toàn dự án, 2912 義理 "anh em nuôi".
