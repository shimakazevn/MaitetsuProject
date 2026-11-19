# Audit — 00_Common file 06 (共通06_8620を探せ)

File: `共通06_8620を探せ.txt.toml` — Common Route chương 6, đi tìm chiếc 8620: Soutetsu, Hibiki và Hachiroku tới nhà tắm công cộng Tororyu-yu, Hachiroku mất cảm ứng với chiếc 8620 của mình, Soutetsu học cách xoa bóp, bàn chuyện thu hút khách du lịch bằng 8620.
Audit ngày 20/11/2026. Đọc toàn bộ từng dòng đối chiếu JP + TW, theo brief audit chuẩn (JP thắng TW khi lệch; kiểm tra chuỗi xoay, tràn chương khác, tag %l, quét đại từ Soutetsu, mẫu rên っ).

## Nguồn đã kiểm chứng: bẫy hai bộ CSV — dùng bộ 01_Hachiroku

- CSV "Trang tính 3" liệt kê file này **hai lần** (bộ `00_Common` và bộ `01_Hachiroku`, mỗi bộ 444 dòng) — cùng bẫy như lr_ふかみh2 và 共通02/03/04. Audit này dùng bộ **`01_Hachiroku`.
- Bộ `01_Hachiroku` (DÙNG — đúng): JP khớp comment `# JP:` trong TOML **444/444**, VN khớp TOML **444/444** sau khi gỡ `\n` (TOML-2 làm phẳng `\n` thành khoảng trắng ở 268 dòng; CSV giữ `\n` gốc nên CSV là chuẩn cho fix list).
- Bộ `00_Common` (STALE — bỏ): VN khớp TOML chỉ **20/444** — bản dịch khác/cũ, không được dùng.
- TOML chỉ tồn tại một bản duy nhất dưới `00_Common/` (md5 `1d4c8254efe7fe5c556f1a67bed5e439`, không có file trùng lặp nào trong toàn dự án) — fix chỉ cần vào một bản. File giữ BOM + CRLF, `[selections]` rỗng (0 mục).
## Tổng kết: 47/444 dòng sai (10,6%)

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 6 | 御一夜→Ohitoyo 4 (2347, 2395, 3102, 3103); 運転士 gloss→“nhân viên cơ vụ” 2 (2129, 2714) |
| Xưng hô | 25 | Soutetsu tự xưng “tôi”→“anh” với Hibiki 11 (1882, 1940, 1942, 1946, 2080, 2099, 2240, 2244, 2248, 2269, 2270); Soutetsu tự xưng “anh”→“tôi” với Hachiroku 5 (1879, 2206, 2207, 2220, 2334); Soutetsu gọi “cô”→“em” 4 (1587, 2034, 2286, 2410); Hibiki→Hachiroku “cô/cháu”→“chị/em” 3 (2092, 2460, 2461); Hachiroku tự xưng “cháu”→“em” 1 (2231); Hachiroku gọi Soutetsu “cô”→“Ngài” 1 (2150) |
| Rên っ | 2 | 2510, 2511 (sweep-missed) |
| SFX | 2 | 2074 (ふぅむ→“Hừừm” theo công thức nguyên âm); 2760 (ふふ→“fufu”, không phải “ufufu”) |
| Nghĩa | 12 | 1891 (義理の家族→thông gia); 1898 (thiếu 1 lần “Không được”); 1900 (そんなんっ→“Không đời nào!”); 1950 (viển vông→mơ hồ); 1957 (đảo hướng câu hỏi); 2297 + 2513 (nói lắp tên 8620 bị chuẩn hoá); 2385 (bịa “mệt”); 2740 + 2932 (義→“nuôi” bịa thêm); 2857 (それ/これ→“Chuyện nào”); 3092 (あがり症→“sợ đám đông”) |
| **Tổng** | **47** | |
Lệch dòng (misaligned): **0**. Chuỗi xoay (rotation chain): **0**. Tràn từ chương khác: **0** (kiểm tra bằng project VN index: VN dài >25 ký tự chỉ trùng 3 dòng ở file khác, nhưng JP hai bên giống hệt nhau — 「はい、双鉄様」 ở 共通15 2231 và ハチロクh5 1149, và tiếng tàu （カトン、トトン、タタン、タタン――） ở 共通15 3435 / グランドリライト10 2970 / ハチロク10 2855 — đều là câu JP lặp lại được dịch giống hệt, không phải tràn chương; JP trùng lặp trong file: 0). Dòng mồ côi (orphan VN): **0**. Dòng chưa dịch: **0**. Trùng key: **0**.
Nhân vật: monologue 188, 双鉄 115, 日々姫 82, ハチロク 45, 登呂流湯主人 9, 路子 5. Paulette **không xuất hiện** trong file (0 dòng thoại) nên quy tắc B4 không áp dụng — không có dòng nào Paulette gọi tên trần “Soutetsu”.
## 47 dòng sai (chi tiết)

### Thuật ngữ (6 dòng)

### [2129] — Thuật ngữ
- **JP:** 「女性……\x%l機関士;#00ffc040;機関士%l;#;さんって、機関車の\x%l運転士;#00ffc040;運転士%l;#;さんよね。\n昔はそげな人おったと？」
- **TW:** 「女性……\x%l機関士;#00ffc040;司機%l;#;是指機車的\x%l運転士;#00ffc040;駕駛員%l;#;吧。以前有這種人嗎？」
- **Cũ:** 「Phụ nữ…… \x%l機関士;#00ffc040;Người lái tàu%l;#; là \x%l運転士;#00ffc040;nhân viên điều khiển%l;#; đầu máy xe lửa nhỉ.\nNgày xưa cũng có người như vậy sao?」
- **Mới:** 「Phụ nữ…… \x%l機関士;#00ffc040;Người lái tàu%l;#; là \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; đầu máy xe lửa nhỉ.\nNgày xưa cũng có người như vậy sao?」
- **Lý do:** Gloss 運転士 “nhân viên điều khiển” → “nhân viên cơ vụ” (thuật ngữ đã chốt; 2347 trong chính file này đã dùng “nhân viên cơ vụ” cho 運転士). Gloss 機関士 “Người lái tàu” giữ nguyên (đúng theo glossary).

### [2347] — Thuật ngữ
- **JP:** 「ポーレットは市長であるだけでなく、\n御一夜鉄道の社長でもあり、\x%l運転士;#00ffc040;運転士%l;#;まで兼任している」
- **TW:** 「波萊特不僅是市長，還是御一夜鐵路的社長兼\x%l運転士;#00ffc040;駕駛員%l;#;」
- **Cũ:** 「Paulette không chỉ là thị trưởng,\nmà còn là giám đốc của Đường sắt Ohimitera, kiêm luôn cả chức \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;.」
- **Mới:** 「Paulette không chỉ là thị trưởng,\nmà còn là giám đốc của Đường sắt Ohitoyo, kiêm luôn cả chức \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;.」
- **Lý do:** 御一夜鉄道 → “Đường sắt Ohimitera” — sai; theo quyết định 19/11 là “Ohitoyo”.

### [2395] — Thuật ngữ
- **JP:** 「そのうえ天然温泉たい！\n[きゅうしゅう,1]九洲に名高か温泉地、御一夜のお風呂やけんね」
- **TW:** 「而且還是天然溫泉！這裡可是九州著名的溫泉鄉——御一夜的澡堂」
- **Cũ:** 「Hơn nữa còn là suối nước nóng tự nhiên đó nha!\nLà nhà tắm của Ohimitera, khu suối nước nóng nổi tiếng ở Kyushu mà lị.」
- **Mới:** 「Hơn nữa còn là suối nước nóng tự nhiên đó nha!\nLà nhà tắm của Ohitoyo, khu suối nước nóng nổi tiếng ở Kyushu mà lị.」
- **Lý do:** 御一夜 → “Ohimitera” — sai; theo quyết định 19/11 là “Ohitoyo”.

### [2714] — Thuật ngữ
- **JP:** 鉄道会社の社長として、\x%l運転士;#00ffc040;運転士%l;#;としてと同じように、\n市長としてもその強さを保てるものか、正直、疑問だ。
- **TW:** 但在作為市長時，她還能像作為鐵路公司社長、\x%l運転士;#00ffc040;駕駛員%l;#;時那樣，保持那份堅強嗎，說實話令人懷疑。
- **Cũ:** Thành thật mà nói, tôi nghi ngờ liệu cô ấy có thể giữ được sự mạnh mẽ đó với tư cách là Thị trưởng,\ngiống như khi làm Giám đốc công ty đường sắt hay \x%l運転士;#00ffc040;người lái tàu%l;#; hay không.
- **Mới:** Thành thật mà nói, tôi nghi ngờ liệu cô ấy có thể giữ được sự mạnh mẽ đó với tư cách là Thị trưởng,\ngiống như khi làm Giám đốc công ty đường sắt hay \x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; hay không.
- **Lý do:** Gloss 運転士 “người lái tàu” → “nhân viên cơ vụ” (thuật ngữ đã chốt; tránh lẫn với 機関士 vốn đã gloss “người lái tàu” ở 2129).

### [3102] — Thuật ngữ
- **JP:** 湯医は、御一夜鉄道湯医線の終着駅だ。\n学園の他には、温泉医療施設がある。
- **TW:** 湯醫是御一夜鐵路湯醫線的終點站。那裡除了學校還有溫泉醫療設施。
- **Cũ:** Yunoi là ga cuối của tuyến Yunoi thuộc Đường sắt Ohimitera.\nNgoài học viện ra, ở đó còn có cơ sở y tế suối nước nóng.
- **Mới:** Yunoi là ga cuối của tuyến Yunoi thuộc Đường sắt Ohitoyo.\nNgoài học viện ra, ở đó còn có cơ sở y tế suối nước nóng.
- **Lý do:** 御一夜鉄道 → “Đường sắt Ohimitera” — sai; theo quyết định 19/11 là “Ohitoyo”.

### [3103] — Thuật ngữ
- **JP:** \x%lエアクラ;#00ffc040;エアクラ%l;#;可動不能区域である旧術仙炭鉱近辺を抜け、\n御一夜-湯医の往復客を、主に湯医線は運んでいるらしい。
- **TW:** 湯醫線穿越了無法使用\x%lエアクラ;#00ffc040;空凝機%l;#;的區域——前術仙廢煤礦。往返於御一夜和湯醫之間的乘客主要都由這條線路來運送。
- **Cũ:** Tuyến Yunoi đi qua khu vực mỏ than cũ Jutsusen, nơi \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,\nvà chủ yếu vận chuyển hành khách qua lại giữa Ohimitera và Yunoi.
- **Mới:** Tuyến Yunoi đi qua khu vực mỏ than cũ Jutsusen, nơi \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,\nvà chủ yếu vận chuyển hành khách qua lại giữa Ohitoyo và Yunoi.
- **Lý do:** 御一夜 → “Ohimitera” — sai; theo quyết định 19/11 là “Ohitoyo”.

### Xưng hô (25 dòng)

### [1587] — Xưng hô
- **JP:** 「\x%l8620;#00ffc040;8620%l;#;だが。お前――失くしたのか？」
- **TW:** 「\x%l8620;#00ffc040;８６２０%l;#;，你——找不到了嗎？」
- **Cũ:** 「Về chiếc \x%l8620;#00ffc040;8620%l;#; đó. Cô——đã làm mất nó rồi sao?」
- **Mới:** 「Về chiếc \x%l8620;#00ffc040;8620%l;#; đó. Em——đã làm mất nó rồi sao?」
- **Lý do:** Soutetsu gọi Hachiroku: “cô” → “em” (người làm mất 8620 chỉ có thể là Hachiroku, Railord của nó; tiền lệ file 03 Soutetsu→Hachiroku “em” 65 dòng, file 05 2440/2727).

### [1879] — Xưng hô
- **JP:** 「逃げんさ。僕が帰宅し安全になったと見ただけだ。\n着水して、ハチロクを下ろしてくるのだろうよ」
- **TW:** 「不是逃了。它只是在確認我是不是安全到家了。現在應該是準備在水上著陸，放八六下來」
- **Cũ:** 「Không trốn đâu. Chỉ là thấy anh đã về nhà an toàn thôi.\nChắc giờ cô ấy đang hạ cánh trên mặt nước để đưa Hachiroku xuống đấy.」
- **Mới:** 「Không trốn đâu. Chỉ là thấy tôi đã về nhà an toàn thôi.\nChắc giờ nó đang hạ cánh trên mặt nước để đưa Hachiroku xuống đấy.」
- **Lý do:** Hai lỗi một dòng. (1) Soutetsu tự xưng “anh” khi nói với Hachiroku — sai; quy ước đã chốt: “anh” chỉ với Hibiki, với Hachiroku là “tôi” (file 02 §xưng hô; file 05 giữ “Tôi” ở 2440/2727). (2) “cô ấy” chỉ chiếc 8620 (đầu máy, đang hạ cánh để đưa Hachiroku xuống) — sai; TW dùng 它, toàn dự án “nó” 60 lần vs “cô ấy” 8 lần cho 8620.

### [1882] — Xưng hô
- **JP:** 「わからん」
- **TW:** 「不清楚」
- **Cũ:** 「Tôi không biết.」
- **Mới:** 「Anh không biết.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (1881/1883 đều là Hibiki) — sai; với Hibiki là “anh” (file 02 2162/2163).

### [1940] — Xưng hô
- **JP:** 「しかし、よくこんな銭湯を知っていたな。\n僕が帝都に出ていた間に、風呂が壊れでもしたのか？」
- **TW:** 「但是，真虧你知道這種澡堂呢。我去帝都的這段時間裡浴室壞過嗎」
- **Cũ:** 「Nhưng sao em lại biết nhà tắm này hay vậy.\nTrong lúc tôi ở Đế đô, nhà tắm nhà mình bị hỏng hay sao?」
- **Mới:** 「Nhưng sao em lại biết nhà tắm này hay vậy.\nTrong lúc anh ở Đế đô, nhà tắm nhà mình bị hỏng hay sao?」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (“sao em lại biết”) — sai; với Hibiki là “anh”.

### [1942] — Xưng hô
- **JP:** 「しかし、そうなるとどうするか。\nまさか僕が女湯にも入れんし」
- **TW:** 「但這樣的話要怎麼辦？再怎麼說我也不能進女浴室啊」
- **Cũ:** 「Nhưng, nếu vậy thì phải làm sao.\nKhông lẽ tôi lại vào phòng tắm nữ.」
- **Mới:** 「Nhưng, nếu vậy thì phải làm sao.\nKhông lẽ anh lại vào phòng tắm nữ.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (bàn chuyện tắm nam/nữ) — sai; với Hibiki là “anh”.

### [1946] — Xưng hô
- **JP:** 「ハチロクが僕の背中を流すのが、イヤか？」
- **TW:** 「你不喜歡八六幫我擦背嗎？」
- **Cũ:** 「Em ghét việc Hachiroku chà lưng cho tôi sao?」
- **Mới:** 「Em ghét việc Hachiroku chà lưng cho anh sao?」
- **Lý do:** Soutetsu tự xưng “tôi” khi hỏi Hibiki (“Em ghét…”) — sai; với Hibiki là “anh”.

### [2034] — Xưng hô
- **JP:** 「離れすぎたゆえ、一時的に感じられないだけかもしれん。\n探して近くで触れ合えば、また感覚も戻るだろうさ」
- **TW:** 「可能是因為離得太遠，所以暫時感應不到。說不定尋找時在比較近的位置感應又恢復了」
- **Cũ:** 「Có lẽ do khoảng cách quá xa nên tạm thời cô không cảm nhận được thôi.\nNếu tìm thấy và tiếp xúc gần gũi, cảm giác đó sẽ quay lại thôi.」
- **Mới:** 「Có lẽ do khoảng cách quá xa nên tạm thời em không cảm nhận được thôi.\nNếu tìm thấy và tiếp xúc gần gũi, cảm giác đó sẽ quay lại thôi.」
- **Lý do:** Soutetsu gọi Hachiroku: “cô” → “em” (cô ấy không cảm nhận được 8620; tiền lệ file 03/05).

### [2080] — Xưng hô
- **JP:** 「ああ、そうか。それは盲点だったな、すまん」
- **TW:** 「啊。是我疏忽了，抱歉」
- **Cũ:** 「À, ra vậy. Tôi không nghĩ đến chuyện đó, xin lỗi nhé.」
- **Mới:** 「À, ra vậy. Anh không nghĩ đến chuyện đó, xin lỗi nhé.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (2079/2081/2084 đều là Hibiki) — sai; với Hibiki là “anh”.

### [2092] — Xưng hô
- **JP:** 「あ、すみません」
- **TW:** 「啊，對不起」
- **Cũ:** 「A, cháu xin lỗi.」
- **Mới:** 「A, em xin lỗi.」
- **Lý do:** Hibiki tự xưng “cháu” khi xin lỗi Soutetsu/Hachiroku (2088 cô ấy gọi “Anh hai, Hachiroku”; 2095 cũng vậy) — sai; “cháu” chỉ đúng với người lớn tuổi như bà chủ nhà tắm (1982, 2308). Với anh hai và Hachiroku là “em”.

### [2099] — Xưng hô
- **JP:** 「うん。\x%l8620;#00ffc040;8620%l;#;形にその、『誰の目にもわかる魅力』\nがある可能性は、決して低くはないと思う」
- **TW:** 「嗯。我認為\x%l8620;#00ffc040;８６２０%l;#;型很有可能擁有讓“任何人都能感覺到的魅力”」
- **Cũ:** 「Ừ. Khả năng mẫu \x%l8620;#00ffc040;8620%l;#; sở hữu 『sức hấp dẫn mà ai cũng có thể thấy』 đó,\ntôi nghĩ tuyệt đối không hề thấp.」
- **Mới:** 「Ừ. Khả năng mẫu \x%l8620;#00ffc040;8620%l;#; sở hữu 『sức hấp dẫn mà ai cũng có thể thấy』 đó,\nanh nghĩ tuyệt đối không hề thấp.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (tiếp nối 2097 dùng “anh” cùng đoạn, cùng người nghe) — sai; với Hibiki là “anh”.

### [2150] — Xưng hô
- **JP:** 「慎み無いこととお感じになられても仕方ありません。\n嫁入り前の娘が、殿方と一緒にですからね」
- **TW:** 「姑娘在出嫁之前和先生一同入浴，會覺得這不夠慎重也很正常」
- **Cũ:** 「Cô cảm thấy thiếu ý tứ cũng là chuyện đương nhiên thôi.\nVì một thiếu nữ chưa chồng lại đi tắm cùng với đàn ông mà.」
- **Mới:** 「Ngài cảm thấy thiếu ý tứ cũng là chuyện đương nhiên thôi.\nVì một thiếu nữ chưa chồng lại đi tắm cùng với đàn ông mà.」
- **Lý do:** Hachiroku nói với Soutetsu: “Cô cảm thấy thiếu ý tứ” — sai ngôi; người “cảm thấy thiếu ý tứ” là Soutetsu (nam, chủ nhân, 様). “Ngài” mới đúng.

### [2206] — Xưng hô
- **JP:** 「何が正解かはわからない。どれが繋がるかもわからない。\nだったら全部を、正解と信じてやるしかないんだ」
- **TW:** 「我不知道什麼是正確的，也不知道怎麼做能幫到你。那我乾脆就相信這些全都是正確的吧」
- **Cũ:** 「Anh không biết đâu là câu trả lời đúng. Cũng không biết điều gì sẽ kết nối với nhau.\nVậy thì chỉ còn cách tin rằng tất cả đều là câu trả lời đúng và làm thôi.」
- **Mới:** 「Tôi không biết đâu là câu trả lời đúng. Cũng không biết điều gì sẽ kết nối với nhau.\nVậy thì chỉ còn cách tin rằng tất cả đều là câu trả lời đúng và làm thôi.」
- **Lý do:** Soutetsu tự xưng “anh” khi nói với Hachiroku — sai; “anh” chỉ với Hibiki. Đoạn này chỉ có hai người (2199 Hachiroku: “chỉ còn hai chúng ta”). Với Hachiroku là “tôi”.

### [2207] — Xưng hô
- **JP:** 「僕もだ」
- **TW:** 「我也是」
- **Cũ:** 「Anh cũng vậy.」
- **Mới:** 「Tôi cũng vậy.」
- **Lý do:** Như 2206: Soutetsu tự xưng “anh” khi nói với Hachiroku — sai; với Hachiroku là “tôi”.

### [2220] — Xưng hô
- **JP:** 「僕らはふたごだ。僕が誰かを助ければ、\n路子が救われるかもしれないって。そう思うからさ」
- **TW:** 「我們是雙胞胎。如果我幫助了別人，路子也許會得到救贖。正因為這樣想」
- **Cũ:** 「Chúng ta là anh em sinh đôi. Nếu anh cứu giúp một ai đó,\nthì có lẽ Michiko cũng sẽ được cứu rỗi. Anh nghĩ vậy đấy.」
- **Mới:** 「Chúng ta là anh em sinh đôi. Nếu tôi cứu giúp một ai đó,\nthì có lẽ Michiko cũng sẽ được cứu rỗi. Tôi nghĩ vậy đấy.」
- **Lý do:** Soutetsu tự xưng “anh” (2 lần) khi nói với Hachiroku (tiếp nối 2217/2218 cùng đoạn) — sai; với Hachiroku là “tôi”.

### [2231] — Xưng hô
- **JP:** 「わたくしは、双鉄様の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;です。\nどうぞ、ハチロクとお呼びください」
- **TW:** 「我是雙鐵少爺的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;。請叫我八六」
- **Cũ:** 「Cháu là \x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu.\nXin hãy gọi cháu là Hachiroku.」
- **Mới:** 「Em là \x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu.\nXin hãy gọi em là Hachiroku.」
- **Lý do:** Hachiroku tự xưng “cháu” — sai; trong file này cô ấy tự xưng “em” 17 lần, kể cả với Hibiki ở 2225 (chỉ 6 dòng trước, cùng người nghe). “Cháu” là dòng lạc duy nhất.

### [2240] — Xưng hô
- **JP:** 「確かに僕も、\n無関係なことに時間を奪われてはかなわん」
- **TW:** 「我確實也不想被無關的事奪走時間」
- **Cũ:** 「Quả thực tôi cũng,\nkhông muốn bị lãng phí thời gian vào những việc không liên quan.」
- **Mới:** 「Quả thực anh cũng,\nkhông muốn bị lãng phí thời gian vào những việc không liên quan.」
- **Lý do:** Soutetsu tự xưng “tôi” khi đáp lời Hibiki (2238 là câu của Hibiki) — sai; với Hibiki là “anh”.

### [2244] — Xưng hô
- **JP:** 「これから風呂にいく。この汚れでは家にあがれん」
- **TW:** 「我身上太髒沒辦法進屋，現在準備去一趟澡堂」
- **Cũ:** 「Bây giờ tôi sẽ đi tắm. Bẩn thế này thì không vào nhà được.」
- **Mới:** 「Bây giờ anh sẽ đi tắm. Bẩn thế này thì không vào nhà được.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (2241 Hibiki gọi “anh hai”) — sai; với Hibiki là “anh”.

### [2248] — Xưng hô
- **JP:** 「前は隠した。\n日々姫、安心して背中を頼む」
- **TW:** 「我遮好了。放心吧，日日姬，拜託你擦背了」
- **Cũ:** 「Che phía trước rồi đấy.\nHibiki, yên tâm chà lưng cho tôi đi.」
- **Mới:** 「Che phía trước rồi đấy.\nHibiki, yên tâm chà lưng cho anh đi.」
- **Lý do:** Soutetsu tự xưng “tôi” khi nói với Hibiki (gọi tên cô ấy trong câu) — sai; với Hibiki là “anh”.

### [2269] — Xưng hô
- **JP:** 「ああ、すまん。\nそんなつもりはなかったのだが」
- **TW:** 「抱歉。我不是這個意思」
- **Cũ:** 「À, xin lỗi.\nTôi không có ý đó đâu.」
- **Mới:** 「À, xin lỗi.\nAnh không có ý đó đâu.」
- **Lý do:** Soutetsu tự xưng “tôi” khi xin lỗi Hibiki (2262/2273 đều là Hibiki) — sai; với Hibiki là “anh”.

### [2270] — Xưng hô
- **JP:** 「すまんな。すっかり失念していた」
- **TW:** 「抱歉。我都給忘了」
- **Cũ:** 「Xin lỗi nhé. Tôi quên khuấy mất.」
- **Mới:** 「Xin lỗi nhé. Anh quên khuấy mất.」
- **Lý do:** Như 2269: Soutetsu tự xưng “tôi” khi nói với Hibiki — sai; với Hibiki là “anh”.

### [2286] — Xưng hô
- **JP:** 「日々姫に心あたりがあるようだ。\nお前はどうする？　一緒に行くか？」
- **TW:** 「日日姬好像知道有可以洗掉煤灰的地方。怎麼樣？你要一起去嗎？」
- **Cũ:** 「Có vẻ Hibiki biết chỗ nào đó.\nCô thì sao? Có đi cùng không?」
- **Mới:** 「Có vẻ Hibiki biết chỗ nào đó.\nEm thì sao? Có đi cùng không?」
- **Lý do:** Soutetsu gọi Hachiroku: “cô” → “em” (Hibiki được nhắc ở ngôi thứ ba trong cùng câu, nên người nghe là Hachiroku).

### [2334] — Xưng hô
- **JP:** 「だが、僕は汰斗さんに教わったんだ。\n助けられなかった分、助けろと」
- **TW:** 「汰斗老爺教過我，要把自己的不幸和遺憾化為幫助別人的動力」
- **Cũ:** 「Nhưng, anh đã được ông Taito dạy bảo.\nHãy cứu giúp người khác để bù đắp cho những người mình không thể cứu.」
- **Mới:** 「Nhưng, tôi đã được ông Taito dạy bảo.\nHãy cứu giúp người khác để bù đắp cho những người mình không thể cứu.」
- **Lý do:** Soutetsu tự xưng “anh” khi nói với Hachiroku (2328 là câu của Hachiroku) — sai; với Hachiroku là “tôi”. “Mình” trong mệnh đề quan hệ (“những người mình không thể cứu”) giữ nguyên — cách dùng phụ thuộc tự nhiên, không phải đại từ tự xưng.

### [2410] — Xưng hô
- **JP:** 「もしも、ここで眠るのが嫌なら」
- **TW:** 「要是你不喜歡睡在這」
- **Cũ:** 「Nếu cô không thích ngủ ở đây thì」
- **Mới:** 「Nếu em không thích ngủ ở đây thì」
- **Lý do:** Soutetsu gọi người nghe là “cô” — sai; người nghe là Hibiki hoặc Hachiroku, cả hai đều là “em” với Soutetsu.

### [2460] — Xưng hô
- **JP:** 「やったら、私んことも日々姫でよかよ。\n妹やもん、にぃにぃの所有物も同然やけんね」
- **TW:** 「那你也直接叫我日日姬吧。妹妹也相當於是阿哥的人」
- **Cũ:** 「Nếu vậy thì cô cứ gọi tôi là Hibiki đi.\nTôi là em gái, cũng giống như vật sở hữu của anh hai thôi.」
- **Mới:** 「Nếu vậy thì chị cứ gọi em là Hibiki đi.\nEm là em gái, cũng giống như vật sở hữu của anh hai thôi.」
- **Lý do:** Hibiki gọi Hachiroku là “cô” và tự xưng “tôi” — sai; toàn dự án Hibiki gọi Hachiroku là “chị” 18 lần, trong chính file này 3053 cũng là “chị——Hachiroku”. Tự xưng “em” theo đó.

### [2461] — Xưng hô
- **JP:** 「あの……私は」
- **TW:** 「那個……我呢」
- **Cũ:** 「Dạ…… còn cháu thì sao ạ?」
- **Mới:** 「Dạ…… còn em thì sao ạ?」
- **Lý do:** Hibiki tự xưng “cháu” khi nói với Hachiroku — sai; như 2460, với Hachiroku là “em”. Lưu ý: JP 「あの……私は」 là câu bỏ lửng; cách diễn “còn… thì sao” là cách đọc của người dịch cũ, giữ nguyên chỉ sửa xưng hô.

### Rên っ (2 dòng)

### [2510] — Rên っ
- **JP:** 「っ！」
- **TW:** 「！」
- **Cũ:** 「!」
- **Mới:** 「Ư!」
- **Lý do:** JP っ！ — tiếng gasp っ bị mất; sweep không bắt được (sweep-missed). Thêm Ư.

### [2511] — Rên っ
- **JP:** 「っ！！？」
- **TW:** 「！！？」
- **Cũ:** 「!!?」
- **Mới:** 「Ư!!?」
- **Lý do:** JP っ！！？ — tiếng gasp っ bị mất; sweep không bắt được (sweep-missed). Thêm Ư.

### SFX (2 dòng)

### [2074] — SFX
- **JP:** 「ふぅむ」
- **TW:** 「唔」
- **Cũ:** 「Hừm.」
- **Mới:** 「Hừừm.」
- **Lý do:** JP ふぅむ: một ぅ → VN 2 nguyên âm theo công thức đã chốt (VN = 1 + số う/ぅ). “Hừm” chỉ có 1 nguyên âm — thiếu một. 2075 ふむ → “Hừm.” giữ nguyên (hai dòng JP khác nhau không được dịch giống hệt).

### [2760] — SFX
- **JP:** 懐かしそうに目を細め、\nそれからふふ、と、ハチロクは幸せそうに微笑む。
- **TW:** 八六懷念地眯起眼睛，接著幸福地發出了“呵呵”的微笑聲。
- **Cũ:** Cô ấy nheo mắt lại đầy hoài niệm,\nrồi ufufu mỉm cười hạnh phúc.
- **Mới:** Cô ấy nheo mắt lại đầy hoài niệm,\nrồi fufu mỉm cười hạnh phúc.
- **Lý do:** JP ふふ (fufu) — VN “ufufu” diễn thành うふふ, thừa một “u”. Theo quy tắc tiếng cười 22/11: ふふ → “fufu”, うふふ → “ufufu”.

### Nghĩa (12 dòng)

### [1891] — Nghĩa
- **JP:** 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;でも、義理の家族でも。\n見知らぬ他の誰であろうと、おんなじさ」
- **TW:** 「不管是\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;、沒有血緣關係的家人還是素不相識的他人，都一樣」
- **Cũ:** 「Dù là \x%lレイルロオド;#00ffc040;Railord%l;#;, hay gia đình nuôi.\nHay bất kỳ một người xa lạ nào khác, cũng đều giống nhau cả.」
- **Mới:** 「Dù là \x%lレイルロオド;#00ffc040;Railord%l;#;, hay gia đình thông gia.\nHay bất kỳ một người xa lạ nào khác, cũng đều giống nhau cả.」
- **Lý do:** 義理の家族 → “gia đình nuôi” là sai: 義 (nghĩa lý/họ hàng) ≠ 養 (nuôi/dưỡng). TW: “沒有血緣關係的家人” (gia đình không cùng huyết thống). “Gia đình thông gia” là cách gọi chuẩn cho họ hàng nghĩa lý.

### [1898] — Nghĩa
- **JP:** 「無理無理無理無理！　\nわたしもにぃにぃも、こぎゃん格好やけんっ！」
- **TW:** 「不行不行不行不行！我和阿哥都光著身子啊！」
- **Cũ:** 「Không được không được không được! \nCả em và anh hai đều đang trong bộ dạng thế này mà!」
- **Mới:** 「Không được không được không được không được! \nCả em và anh hai đều đang trong bộ dạng thế này mà!」
- **Lý do:** JP 無理×4 nhưng VN chỉ có “Không được”×3 — thiếu một lần. Thêm lần thứ tư.

### [1900] — Nghĩa
- **JP:** 「そんなっ！　そんなんっ！\n私にはまだまだ早かけんっ！」
- **TW:** 「不行！不行！對我來說還太早了！」
- **Cũ:** 「Không đời nào! Chuyện đó!\nVới em thì vẫn còn quá sớm!」
- **Mới:** 「Không đời nào! Không đời nào!\nVới em thì vẫn còn quá sớm!」
- **Lý do:** JP そんなっ！そんなんっ！ là hai lần từ chối giống nhau; TW: 不行！不行！ VN “Chuyện đó!” làm mất nghĩa từ chối của そんなんっ.

### [1950] — Nghĩa
- **JP:** 「わからんて！　んんっ、\n本当に、まだふわふわしたお話なんですね」
- **TW:** 「你不清楚！咳咳，還真的只是模糊的計劃呢」
- **Cũ:** 「Không biết á! Ưm,\nquả thật, vẫn chỉ là một câu chuyện viển vông nhỉ.」
- **Mới:** 「Không biết á! Ưm,\nquả thật, vẫn chỉ là một kế hoạch mơ hồ nhỉ.」
- **Lý do:** ふわふわしたお話 = kế hoạch mơ hồ/không rõ ràng, không phải “viển vông” (viển vông = phi thực tế, không thành được). TW: “模糊的計劃”. Trong chính file này 2364 đã dùng “kế hoạch mơ hồ” cho ぼんやりとした案.

### [1957] — Nghĩa
- **JP:** 「まだこの\x%l列車;#00ffc040;列車%l;#;に乗っているのか」
- **TW:** 「你還在這輛\x%l列車;#00ffc040;列車%l;#;上啊」
- **Cũ:** 「Mình vẫn đang ở trên chuyến \x%l列車;#00ffc040;tàu%l;#; này sao.」
- **Mới:** 「Em vẫn đang ở trên chuyến \x%l列車;#00ffc040;tàu%l;#; này sao.」
- **Lý do:** JP 「まだこの列車に乗っているのか」 là câu hỏi hướng tới người nghe (TW: 你還在這輛列車上啊 — “cậu còn ở trên tàu à”); VN “Mình vẫn đang…” đảo thành tự hỏi bản thân, sai cả ngôi lẫn hướng câu hỏi. Người nghe là Hachiroku (nói ngay sau câu 1954 của cô ấy); “em” đúng cho cả Hibiki lẫn Hachiroku.

### [2297] — Nghĩa
- **JP:** 「それで、市長さんが主張したんですね？　その……\nはちろくにいまる形？　が、すごくいいものだって」
- **TW:** 「是市長說那個……是叫８６２０型嗎？是非常好的東西吧」
- **Cũ:** 「Vậy ra, ngài thị trưởng đã khẳng định sao? Rằng cái……\nloại 8620 đó? Là một thứ vô cùng tuyệt vời.」
- **Mới:** 「Vậy ra, ngài thị trưởng đã khẳng định sao? Rằng cái……\nHachirokunii-maru đó? Là một thứ vô cùng tuyệt vời.」
- **Lý do:** Hibiki nói lắp tên 8620型 thành はちろくにいまる形 (nói sai tên) — VN “loại 8620 đó?” đã chuẩn hoá mất nét nói lắp. Giữ lại theo tiền lệ 1904 (“Hachirokunii…… marukei?”).

### [2385] — Nghĩa
- **JP:** 「まぁ、な。いくらかは」
- **TW:** 「算是吧。多少有些」
- **Cũ:** 「À, ừ. Cũng hơi mệt một chút.」
- **Mới:** 「À, ừ. Ít nhiều gì cũng có.」
- **Lý do:** JP 「まぁ、な。いくらかは」 (“Ừ, ít nhiều gì cũng có”) và TW “算是吧。多少有些” đều mơ hồ, không nói “mệt”. VN “Cũng hơi mệt một chút” bịa thêm “mệt”.

### [2513] — Nghĩa
- **JP:** 「はちろくにいまるけい……ですか？\nそれは、そんなに魅力的な機関車なんですか？」
- **TW:** 「８６２０型……能成為大旗嗎？這輛機車這麼有魅力嗎？」
- **Cũ:** 「Loại 8620……sao ạ?\nĐó là một đầu máy xe lửa hấp dẫn đến thế cơ ạ?」
- **Mới:** 「Hachirokunii-marukei……sao ạ?\nĐó là một đầu máy xe lửa hấp dẫn đến thế cơ ạ?」
- **Lý do:** Hibiki nói lắp tên 8620型 thành はちろくにいまるけい — VN “Loại 8620……sao ạ?” đã chuẩn hoá mất nét nói lắp. Giữ lại theo tiền lệ 1904.

### [2740] — Nghĩa
- **JP:** たとえ賛成・反対両派にわかれていても、\n日々姫は僕の[いもうと,1]義妹だ。
- **TW:** 儘管分屬贊成和反對兩派，日日姬也是我的義妹。
- **Cũ:** Cho dù chúng tôi có thuộc hai phe tán thành và phản đối đi chăng nữa,\nnhưng Hibiki vẫn là em gái nuôi của tôi.
- **Mới:** Cho dù chúng tôi có thuộc hai phe tán thành và phản đối đi chăng nữa,\nnhưng Hibiki vẫn là em gái của tôi.
- **Lý do:** 義妹 → “em gái nuôi” là sai: 義 (nghĩa lý/họ hàng, ở đây là em gái không cùng huyết thống) ≠ 養 (nuôi/dưỡng). Ruby [いもうと,1] chỉ đọc là “em gái”. Không bịa thêm quan hệ nuôi dưỡng.

### [2857] — Nghĩa
- **JP:** それ、で両手をそろえて右に。\nこれ、で両手をそろえて左に。
- **TW:** 她把兩手移到左邊表示“這”，把兩手移到右邊表示“那”。
- **Cũ:** Nói 'Chuyện nào', em ấy chắp hai tay đưa sang phải.\nNói 'ra chuyện đó', em ấy chắp hai tay đưa sang trái.
- **Mới:** Nói 'Cái kia', em ấy chắp hai tay đưa sang phải.\nNói 'Cái này', em ấy chắp hai tay đưa sang trái.
- **Lý do:** JP それ/これ là cặp chỉ định “cái kia/cái này” (Hibiki minh hoạ “đó là đó, này là này” bằng tay: それ→phải, これ→trái). TW: 這/那. VN “Chuyện nào”/“ra chuyện đó” dịch sai từ chỉ định thành chuyện trò.

### [2932] — Nghĩa
- **JP:** 義理だなんだを口にせぬよう、\n言葉を選んでゆっくり話す。
- **TW:** 我小心著不提及血緣關係，斟酌好語言後平靜地開口說。
- **Cũ:** Để tránh nhắc đến chuyện là anh em nuôi,\ntôi chọn lọc từ ngữ và chậm rãi nói.
- **Mới:** Để tránh nhắc đến chuyện huyết thống,\ntôi chọn lọc từ ngữ và chậm rãi nói.
- **Lý do:** 義理だなんだ → “chuyện là anh em nuôi” là sai: 義理 (quan hệ nghĩa lý) ≠ 養 (nuôi). TW dịch thẳng: “不提及血緣關係” (không nhắc đến chuyện huyết thống).

### [3092] — Nghĩa
- **JP:** まだ会って間もない僕にさえ、“あがり症か”と\n思わせるような言動をポーレットはしばしば見せている。
- **TW:** 波萊特三不五時會表現出讓人懷疑她有“對人恐懼症”的言行，就連和她相處時間不長的我都這麼覺得。
- **Cũ:** Ngay cả với một người mới gặp chưa lâu như tôi, Paulette cũng thường xuyên có những hành động\nvà lời nói khiến tôi nghĩ cô ấy "mắc chứng sợ đám đông".
- **Mới:** Ngay cả với một người mới gặp chưa lâu như tôi, Paulette cũng thường xuyên có những hành động\nvà lời nói khiến tôi nghĩ cô ấy "hay hồi hộp trước mặt người khác".
- **Lý do:** あがり症 = hay hồi hộp/lúng túng khi đứng trước người khác (stage fright), không phải “sợ đám đông” (sợ đám đông = sợ nơi đông người, gần với chứng sợ khoảng rộng). TW: “對人恐懼症” (sợ giao tiếp với người). Paulette không sợ đám đông — cô ấy lúng túng khi phải nói trước mặt người khác.

## Kiểm tra chéo và các điểm đã xác minh (không sai)

- **Sweep gasp:** file này có 0 mục fixed trong sweep; 3 key needs-file-audit (2016, 3153, 3173) đều đã giải quyết không cần sửa — JP cả ba đều không có っ (2016 うふふ→“Ufufu” đúng theo quy tắc tiếng cười; 3153 ぽろり và 3173 意味がわからん đều không có gasp). Audit tìm thêm 2 gasp sweep-missed (2510, 2511).
- **Tag %l:** số lượng tag JP = VN ở mọi dòng — **0 thẻ thiếu dấu `;` đóng**, 0 tag lệch. Không có tag VN tự thêm.
- **VN trùng lặp trong file:** 4 cặp, tất cả đều là câu ngắn lặp lại hợp lệ (JP cũng giống hệt nhau): 2104/2109 「Ừ」 (JP 「ああ」), 2146/2184 「Vâng, thưa ngài Soutetsu.」 (JP 「はい、双鉄様」), 2295/2311 「Ừ.」 (JP 「ああ」). Cặp 2074/2075 「Hừm.」 có JP khác nhau (ふぅむ vs ふむ) — đã sửa 2074 về “Hừừm.”.
- **“Mình” trong độc thoại Soutetsu:** 0 dòng sai. Các “mình” còn lại đều đúng vai (sở hữu/phản thân/mệnh đề phụ: “nhà tắm nhà mình” 1940, “ngâm mình” 2004, “mặt mình” 2402, “những người mình không thể cứu” 2334).
- **Xưng hô Hachiroku↔Hibiki (cặp cô/cháu) — GIỮ NGUYÊN, không tính sai:** Hachiroku gọi Hibiki là “cô” 3 lần (1954 “Cô xem”, 2225 “Cô cứ gọi trống không… tiểu thư Hibiki”, 2393 “cô biết không? Hibiki”) — nhất quán trong file, khớp với lối nói trang trọng của cô ấy (わたくし + 日々姫様); dạng “chị Hibiki” toàn dự án (20 lần) là dạng tên+gọi, không mâu thuẫn với đại từ “cô” khi xưng hô trực tiếp. Hibiki gọi Hachiroku “cô”/tự xưng “cháu” ở 2460/2461 thì **đã sửa** (xem trên) vì toàn dự án là “chị” 18 lần và trong chính file này 3053 cũng là “chị”. Cặp này để lại cho đợt thống nhất xác nhận lần cuối.
- **Gloss 投炭 “xúc than” (1596, 2951) — GIỮ NGUYÊN, không tính sai:** gloss “xúc than” là đa số toàn dự án (31/48: “xúc than” 31, “thêm than” 11, “ném than” 5, “tiếp than” 1); TW dùng 加煤 (thêm than). Câu 1596 tự định nghĩa “ném than vào buồng lửa” (cho 投げ込む) trong khi gloss gọi tên nghề là “xúc than” — căng nhẹ nhưng không sai nghĩa. Để lại cho đợt thống nhất chọn một gloss duy nhất.
- **Các điểm khác đã kiểm tra, không sai:** 1975 “Anh em với nhau mà” là thành ngữ anh em, không phải đại từ tự xưng; “chúng cháu” của Soutetsu (2001, 2198, 2458) là số nhiều khiêm nhường với bà chủ nhà tắm lớn tuổi — đúng; Hibiki “cháu/tụi cháu” với bà chủ (1982, 2308) — đúng; “cô ấy” ngôi thứ ba chỉ Paulette (2125) và Hibiki (2338) — đúng; 2115 “cô ấy” = Paulette (JP あの人) — đúng; 2296 はぁ → “Hả” (TW 是嗎 ủng hộ cách đọc nghi vấn); 2095 てえええっ → “Trời ơi” (bản địa hoá, tiền lệ pilot); 2043 tiếng sặc nước viết bằng Latin — nhất quán với 2042; 1904 nói lắp “Hachirokunii…… marukei?” đã giữ — tiền lệ cho 2297/2513; 2060 “Hachiroku——chan” giữ; 2060/2064/2494 “anh hai” vs “anh trai” (にぃに vs 兄さん) — đối lập có chủ ý; 2676 大詔/明智 → Taisho/Meiji (TW đồng ý); 2165/2397/2414 “Thị trưởng Paulette” (thêm tên vào 市長さん) — làm rõ, nhất quán trong file; 1879 (trừ 2 lỗi đã sửa) và 2030/2077 “tôi” khi nói với Hachiroku — đúng theo quy ước.
- **Dòng chưa chắc chắn: 0.** Lưu ý duy nhất: 2461 có JP là câu bỏ lửng (「あの……私は」); cách diễn “còn… thì sao” là cách đọc của người dịch cũ, bản sửa chỉ đổi xưng hô “cháu”→“em” và giữ nguyên cách đọc đó.
## Đợt kiểm tra thứ hai (second pass)

**47/47 bản sửa đọc lại đối chiếu JP, 47 được xác nhận, 0 loại bỏ, 0 sửa lại.** Mỗi bản sửa đã kiểm tra lại từng từ với JP gốc (kèm TW khi cần) sau khi viết xong fix list; không có bản sửa nào bị loại hay phải viết lại ở đợt hai. Parse-check bằng tomllib **không thay thế** đợt đọc lại này — nó chỉ kiểm tra cú pháp và khớp giá trị.
Ngoài ra, mỗi bản sửa còn được kiểm tra cơ học: giá trị mới bằng đúng old_vn sau khi thay đúng (các) đoạn cần sửa — không đụng tới phần còn lại của dòng (47/47 khớp).
## Khối TOML (fix)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 47 key, giá trị khớp đúng JSON bản sửa (0 lệch giá trị). Dán vào section `[script]` của file `00_Common/共通06_8620を探せ.txt.toml` (ghi đè đúng 47 key này, giữ nguyên mọi key khác). Lưu ý: giá trị chứa `\n` dạng text (raw `\\n` trong khối) và `\x%l` (raw `\\x`) để tomllib parse ra đúng `\n`/`\x` như trong JSON.

```toml
[script]
1587 = "「Về chiếc \\x%l8620;#00ffc040;8620%l;#; đó. Em——đã làm mất nó rồi sao?」"
1879 = "「Không trốn đâu. Chỉ là thấy tôi đã về nhà an toàn thôi.\\nChắc giờ nó đang hạ cánh trên mặt nước để đưa Hachiroku xuống đấy.」"
1882 = "「Anh không biết.」"
1891 = "「Dù là \\x%lレイルロオド;#00ffc040;Railord%l;#;, hay gia đình thông gia.\\nHay bất kỳ một người xa lạ nào khác, cũng đều giống nhau cả.」"
1898 = "「Không được không được không được không được! \\nCả em và anh hai đều đang trong bộ dạng thế này mà!」"
1900 = "「Không đời nào! Không đời nào!\\nVới em thì vẫn còn quá sớm!」"
1940 = "「Nhưng sao em lại biết nhà tắm này hay vậy.\\nTrong lúc anh ở Đế đô, nhà tắm nhà mình bị hỏng hay sao?」"
1942 = "「Nhưng, nếu vậy thì phải làm sao.\\nKhông lẽ anh lại vào phòng tắm nữ.」"
1946 = "「Em ghét việc Hachiroku chà lưng cho anh sao?」"
1950 = "「Không biết á! Ưm,\\nquả thật, vẫn chỉ là một kế hoạch mơ hồ nhỉ.」"
1957 = "「Em vẫn đang ở trên chuyến \\x%l列車;#00ffc040;tàu%l;#; này sao.」"
2034 = "「Có lẽ do khoảng cách quá xa nên tạm thời em không cảm nhận được thôi.\\nNếu tìm thấy và tiếp xúc gần gũi, cảm giác đó sẽ quay lại thôi.」"
2074 = "「Hừừm.」"
2080 = "「À, ra vậy. Anh không nghĩ đến chuyện đó, xin lỗi nhé.」"
2092 = "「A, em xin lỗi.」"
2099 = "「Ừ. Khả năng mẫu \\x%l8620;#00ffc040;8620%l;#; sở hữu 『sức hấp dẫn mà ai cũng có thể thấy』 đó,\\nanh nghĩ tuyệt đối không hề thấp.」"
2129 = "「Phụ nữ…… \\x%l機関士;#00ffc040;Người lái tàu%l;#; là \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; đầu máy xe lửa nhỉ.\\nNgày xưa cũng có người như vậy sao?」"
2150 = "「Ngài cảm thấy thiếu ý tứ cũng là chuyện đương nhiên thôi.\\nVì một thiếu nữ chưa chồng lại đi tắm cùng với đàn ông mà.」"
2206 = "「Tôi không biết đâu là câu trả lời đúng. Cũng không biết điều gì sẽ kết nối với nhau.\\nVậy thì chỉ còn cách tin rằng tất cả đều là câu trả lời đúng và làm thôi.」"
2207 = "「Tôi cũng vậy.」"
2220 = "「Chúng ta là anh em sinh đôi. Nếu tôi cứu giúp một ai đó,\\nthì có lẽ Michiko cũng sẽ được cứu rỗi. Tôi nghĩ vậy đấy.」"
2231 = "「Em là \\x%lレイルロオド;#00ffc040;Railord%l;#; của ngài Soutetsu.\\nXin hãy gọi em là Hachiroku.」"
2240 = "「Quả thực anh cũng,\\nkhông muốn bị lãng phí thời gian vào những việc không liên quan.」"
2244 = "「Bây giờ anh sẽ đi tắm. Bẩn thế này thì không vào nhà được.」"
2248 = "「Che phía trước rồi đấy.\\nHibiki, yên tâm chà lưng cho anh đi.」"
2269 = "「À, xin lỗi.\\nAnh không có ý đó đâu.」"
2270 = "「Xin lỗi nhé. Anh quên khuấy mất.」"
2286 = "「Có vẻ Hibiki biết chỗ nào đó.\\nEm thì sao? Có đi cùng không?」"
2297 = "「Vậy ra, ngài thị trưởng đã khẳng định sao? Rằng cái……\\nHachirokunii-maru đó? Là một thứ vô cùng tuyệt vời.」"
2334 = "「Nhưng, tôi đã được ông Taito dạy bảo.\\nHãy cứu giúp người khác để bù đắp cho những người mình không thể cứu.」"
2347 = "「Paulette không chỉ là thị trưởng,\\nmà còn là giám đốc của Đường sắt Ohitoyo, kiêm luôn cả chức \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#;.」"
2385 = "「À, ừ. Ít nhiều gì cũng có.」"
2395 = "「Hơn nữa còn là suối nước nóng tự nhiên đó nha!\\nLà nhà tắm của Ohitoyo, khu suối nước nóng nổi tiếng ở Kyushu mà lị.」"
2410 = "「Nếu em không thích ngủ ở đây thì」"
2460 = "「Nếu vậy thì chị cứ gọi em là Hibiki đi.\\nEm là em gái, cũng giống như vật sở hữu của anh hai thôi.」"
2461 = "「Dạ…… còn em thì sao ạ?」"
2510 = "「Ư!」"
2511 = "「Ư!!?」"
2513 = "「Hachirokunii-marukei……sao ạ?\\nĐó là một đầu máy xe lửa hấp dẫn đến thế cơ ạ?」"
2714 = "Thành thật mà nói, tôi nghi ngờ liệu cô ấy có thể giữ được sự mạnh mẽ đó với tư cách là Thị trưởng,\\ngiống như khi làm Giám đốc công ty đường sắt hay \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; hay không."
2740 = "Cho dù chúng tôi có thuộc hai phe tán thành và phản đối đi chăng nữa,\\nnhưng Hibiki vẫn là em gái của tôi."
2760 = "Cô ấy nheo mắt lại đầy hoài niệm,\\nrồi fufu mỉm cười hạnh phúc."
2857 = "Nói 'Cái kia', em ấy chắp hai tay đưa sang phải.\\nNói 'Cái này', em ấy chắp hai tay đưa sang trái."
2932 = "Để tránh nhắc đến chuyện huyết thống,\\ntôi chọn lọc từ ngữ và chậm rãi nói."
3092 = "Ngay cả với một người mới gặp chưa lâu như tôi, Paulette cũng thường xuyên có những hành động\\nvà lời nói khiến tôi nghĩ cô ấy \"hay hồi hộp trước mặt người khác\"."
3102 = "Yunoi là ga cuối của tuyến Yunoi thuộc Đường sắt Ohitoyo.\\nNgoài học viện ra, ở đó còn có cơ sở y tế suối nước nóng."
3103 = "Tuyến Yunoi đi qua khu vực mỏ than cũ Jutsusen, nơi \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động,\\nvà chủ yếu vận chuyển hành khách qua lại giữa Ohitoyo và Yunoi."
```

## Kết bài

File 06 là file Common thứ tư được audit (47/444 = 10,6% sai — cao hơn file 03 (4,8%) và file 02 (7,1%) nhưng thấp hơn file 05 (12,4%)). Điểm đáng chú ý: **không lệch dòng, không chuỗi xoay, không tràn chương, không dòng mồ côi** — cột Việt đứng đúng chỗ ở cả 444 dòng, giống các file Common khác (khác hẳn các file Paulette 03). 47 lỗi còn lại đều là lỗi lẻ tẻ, tập trung vào xưng hô (25 dòng — Soutetsu tự xưng lộn “tôi”/“anh” theo người nghe, đúng thói quen của người dịch cũ: 11 dòng “tôi” sai với Hibiki, 5 dòng “anh” sai với Hachiroku) và nghĩa (12 dòng — nổi bật là cặp 義妹/義理 bị dịch thành “nuôi” ở 2740/2932/1891, và hai lần Hibiki nói lắp tên 8620 bị chuẩn hoá mất ở 2297/2513). **0 dòng chưa chắc chắn.**
Ba phát hiện để lại cho đợt thống nhất: (1) gloss 投炭 chia 4 cách toàn dự án (“xúc than” 31 / “thêm than” 11 / “ném than” 5 / “tiếp than” 1) — cần chọn một; file này giữ “xúc than” theo đa số; (2) cặp xưng hô Hachiroku→Hibiki “cô” (1954, 2225, 2393) vs “chị Hibiki” toàn dự án — cần chốt đại từ xưng hô trực tiếp của Hachiroku; (3) Soutetsu→Hachiroku “tôi” vs “anh” vẫn chia đôi toàn dự án (87 “tôi” / 65 “anh” theo JP nhắc tên) — file này đã thống nhất nội bộ về “tôi” theo quy ước file 02, nhưng đợt thống nhất nên rà lại toàn dự án.
Fix list (47/47 key verified to parse, 0 lệch giá trị) saved at ~/workspace/maitetsu-pilot/audit-00common06-REVIEW.md and audit-00common06-wrong.json — NOT sent to Hieu (no-files rule).
