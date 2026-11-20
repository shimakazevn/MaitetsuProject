# Audit — ハチロク07_延命.txt.toml

- File: `ハチロク07_延命.txt.toml` — route 01_Hachiroku, 499 dòng script (157 độc thoại, 92 thoại Olivy, 61 thoại Soutetsu, 53 thoại Paulette, 47 thoại Hachiroku, 41 thoại Điện xá Công chúa, 23 thoại Niiroku, 5 thoại Reina, 4 thoại Kisaki, 4 thoại Nagi, 3 thoại Hibiki, 3 thoại Fukami, 3 thoại Mayami, 3 thoại Akai).
- Nội dung: cuộc họp buổi tối về tương lai của Olivy — kiểm tra toàn diện hàng năm, kéo dài tuổi thọ Railord, lương và vai trò mới sau khi nghỉ lái tàu; Niiroku (Railord của Kuha 26, lái tàu Kiyoharu) xuất hiện, nghi ngờ về "cô gái quấn băng gạc" (Railord không có cộng cảm); Densha-hime tài trợ nghiên cứu kéo dài tuổi thọ và gợi ý "bí quyết sống khỏe cho Railord"; Olivy đồng ý chia sẻ kỹ thuật bảo trì đường ray và lái tàu; kết bằng cảnh đo thân nhiệt và tiếng bíp của nhiệt kế.
- **Kết quả: 64/499 dòng sai (12,8%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (499 dòng, 0 khóa trùng, 0 ô VN trống); TOML 499 khóa script, khớp CSV3 tuyệt đối 499/499 (0 lệch thực chất — 2 dòng 2299, 2386 chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng. Không có thẻ `%l` nào sai định dạng trong VN, không có thẻ VN tự thêm (kiểm tra máy: số thẻ mở/đóng VN khớp JP từng dòng).
- TOML md5 `4cd3b14b4f5365d86e1f0459692a8449`; không có bản sao file này (không thuộc 11 nhóm trùng — đã kiểm tra md5 toàn bộ 227 file).
- Nhiễm chéo kiểm tra máy: 0 dòng VN đặc trưng (≥25 ký tự) trong file này trùng với dòng VN ở file khác mà JP khác; trong file chỉ có 1 VN trùng lặp: 「!」 ×5 (2284, 2313, 2317, 2329, 2827 — đều là JP 「!」 thật, hợp lệ).
- Soutetsu: "anh" với Paulette (2367), Hibiki (2508 sửa), Olivy (2418 sửa), Niiroku (2829 sửa; mẫu trong file: 2486 "anh", 2520 "cậu", 2521 "Bọn anh"); "tôi" chỉ còn ở chỗ đúng: với Điện xá Công chúa (2513, 2817 — kèm "ạ"), tự giới thiệu trang trọng 2538, và các dạng nhóm "chúng tôi"/"Bọn anh" (2152, 2245, 2246, 2364, 2520, 2521, 2695). Độc thoại "tôi" toàn file; "mình" duy nhất ở 3580 (suy nghĩ trong ngoặc đơn — giữ theo tiền lệ 1651 "mình đang ngủ gật").
- Hachiroku tự xưng "em" nhất quán toàn file; 3 dòng sai "tôi" đã sửa (2345, 2565, 2905). 2533 "Tôi là Hachiroku" giữ nguyên — tự giới thiệu trang trọng (đối xứng Soutetsu 2538). 2327 "chúng tôi" là dạng nhóm, không phải tự xưng sai.
- Fukami→Nagi: 2453 "em"→"cậu" đã sửa; 2339 "Chị sẽ dạy em" giữ nguyên — người nghe là Olivy (xem §4). Nagi→Fukami không xuất hiện trong file. 2679 Seki "ông ngoại" đã sửa (xem §2, §6).
- Thuật ngữ: file này đã có sẵn 2 dòng 電車姫 đúng ("Công chúa Tàu điện": 3138, 3282) — chứng tỏ "Điện xá Công chúa" là dạng cũ. Không có dạng cũ nào khác ngoài các dòng đã sửa ở §2 (không còn "Hinamoto", "Yui", "Okoba", "Migita System" trong file).

## §2. Danh sách sửa (64 dòng)

Phân loại: thuật ngữ 53 (Điện xá Công chúa→Công chúa Tàu điện 26; Ohito/Ohigawa→Ohitoyo 12; Hoàng gia→Teitetsu 4 — 2490 mang 2 lỗi thuật ngữ; Thẻ bảng→máy tính bảng 4; Mỹ→Minh Quốc 2; Nagi đại nhân→Bổn tiểu thư 1; thân chính/Kíp lái→thân bảo trì/thân vận hành 2; Lõi Lord→Lõi Railord 3), đại từ 7 (2418 kiêm thuật ngữ), thân tộc 1, gasp sweep 3, SFX 1.

### 1588 — monologue — thuật ngữ
- JP: ――6年間。日々姫が描き出してきたデザインたちは、\\n僕らと電車姫様との距離を、確実に大きく縮めてくれた。
- TW: ——在這六年中，日日姬所完成的一個又一個設計方案，的確是大大拉近了我們和電車公主殿下的距離。
- VN cũ: ――6 năm qua. Những thiết kế mà Hibiki tạo ra,\\nđã thực sự kéo gần khoảng cách giữa chúng tôi và Điện xá Công chúa điện hạ một cách đáng kể.
- Sửa: ――6 năm qua. Những thiết kế mà Hibiki tạo ra,\\nđã thực sự kéo gần khoảng cách giữa chúng tôi và Công chúa Tàu điện một cách đáng kể.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 1605 — monologue — thuật ngữ
- JP: ……電車姫様からいただいたご助言を記したメモを見る。
- TW: ……我對照了一下記有電車公主殿下建議的筆記本。
- VN cũ: ……Tôi nhìn vào tờ ghi chú lời khuyên của Điện xá Công chúa điện hạ.
- Sửa: ……Tôi nhìn vào tờ ghi chú lời khuyên của Công chúa Tàu điện.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 1640 — ニイロク — thuật ngữ
- JP: 「――自分は、整備[ボディ]体を失った。\\n運転[ボディ]体。この体しか存在しない」
- TW: 「——我的整備體已經損毀了。只有駕駛體——也就是現在這副身體」
- VN cũ: 「——Tôi, đã mất thân chính rồi.\\nKíp lái. Chỉ còn lại cơ thể này thôi.」
- Sửa: 「——Tôi, đã mất thân bảo trì rồi.\\nthân vận hành. Chỉ còn lại cơ thể này thôi.」
- Lý do: JP 整備[ボディ]体 / 運転[ボディ]体. VN cũ 'thân chính'/'Kíp lái' sai cả hai; thuật ngữ đã chốt: 整備体='thân bảo trì', 運転体='thân vận hành' (tiền lệ ハチロク10, 稀咲01: 整備体→'thân bảo trì'). Phần còn lại của dòng giữ nguyên.

### 1662 — 電車姫 — thuật ngữ
- JP: 「仮称じゃ。正式名称の存在しない――\\n『\\x%lタブレット;#00ffc040;タブレット%l;#;を\\x%lタブレット;#00ffc040;タブレット%l;#;たらしめる何か』のこと」
- TW: 「“實現\\x%lタブレット;#00ffc040;操作板%l;#;功能之物”——並無正式名稱，暫稱如此而已」
- VN cũ: 「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\\nLà 'thứ khiến \\x%lタブレット;#00ffc040;Thẻ bảng%l;#; trở thành \\x%lタブレット;#00ffc040;Thẻ bảng%l;#;'」
- Sửa: 「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\\nLà 'thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;'」
- Lý do: JP タブレット (thẻ %l giữ nguyên). VN cũ gloss 'Thẻ bảng' sai; thuật ngữ đã chốt: タブレット='máy tính bảng' (tiền lệ ハチロク10 sửa 19 dòng trong audit).

### 2173 — ハチロク — thuật ngữ
- JP: 「ロオド――コア？」
- TW: 「人偶——核？」
- VN cũ: 「Lõi――Lord?」
- Sửa: 「Railord――Lõi?」
- Lý do: JP ロオド――コア？ — ロオド là dạng rút gọn của レイルロオド. VN cũ 'Lõi――Lord?' đọc sai ロオド thành 'Lord' và đảo thứ tự; TW 人偶——核？ (= Railord — lõi) xác nhận. Sửa theo thứ tự JP: 'Railord――Lõi?' (xem thêm 2844, 2850).

### 2203 — 電車姫 — thuật ngữ
- JP: 「[おおみや,1]旺宮の旧帝鉄\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;工機部――\\n現・旺宮\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;研究所には、資金を投下しておる」
- TW: 「余有向在大宮的前帝國鐵路\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;工程機械部——現稱大宮\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;研究所提供資金支持」
- VN cũ: 「Bộ phận Cơ khí \\x%lレイルロオド;#00ffc040;Railord%l;#; Đường sắt Hoàng gia cũ ở Omiya――\\nNay là Viện nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; Omiya, ta đang đầu tư vốn vào đó」
- Sửa: 「Bộ phận Cơ khí \\x%lレイルロオド;#00ffc040;Railord%l;#; Teitetsu cũ ở Omiya――\\nNay là Viện nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; Omiya, ta đang đầu tư vốn vào đó」
- Lý do: JP 旧帝鉄. VN cũ 'Đường sắt Hoàng gia' là dạng cũ; thuật ngữ đã chốt: 帝鉄='Teitetsu' ('Đường sắt Đế quốc' đầy đủ chỉ dùng trong tooltip %l ở lần xuất hiện đầu — không có tooltip ở đây; tiền lệ ハチロク10 sửa 3 dòng Teitetsu trong audit).

### 2209 — オリヴィ — thuật ngữ
- JP: 「こんにちわ。オリヴィ[めいこく,1]冥国式の\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;なんだけど、\\nあなた、[ひのもと,2]日ノ本式だよね？　何の専用\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;？」
- TW: 「你好。奧莉薇是美國式的\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，你是日本式的吧？是什麼車輛的專用\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;呀？」
- VN cũ: 「Xin chào. Olivy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ,\\nbạn là kiểu Hinomoto nhỉ? \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của xe nào vậy?」
- Sửa: 「Xin chào. Olivy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nbạn là kiểu Hinomoto nhỉ? \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của xe nào vậy?」
- Lý do: JP 冥国式 (furigana めいこく). VN cũ 'kiểu Mỹ' theo TW 美國式; thuật ngữ đã chốt: 冥国='Minh Quốc' (tiền lệ 凪ふかみ01 sửa 13 dòng 冥国 trong audit). 日ノ本式 đã đúng 'Hinomoto'.

### 2343 — ポーレット — thuật ngữ
- JP: 「あ！？　ありがとうございます――以上に、すみません。\\n内々の話で、電車姫様の貴重なお時間を――」
- TW: 「啊！？殿下過獎——適才我公司內部事務討論卻讓殿下久等，十分抱歉」
- VN cũ: 「A!? Xin cảm ơn ngài――hơn thế nữa, tôi xin lỗi.\\nChuyện nội bộ của chúng tôi đã làm mất thời gian quý báu của Điện xá Công chúa điện hạ――」
- Sửa: 「A!? Xin cảm ơn ngài――hơn thế nữa, tôi xin lỗi.\\nChuyện nội bộ của chúng tôi đã làm mất thời gian quý báu của Công chúa Tàu điện――」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2345 — ハチロク — đại từ
- JP: 「あっ！？　あのっ――いえ、わたくし、その」
- TW: 「啊！？這——不是的，我只是」
- VN cũ: 「A!? Cái đó――không phải, tôi, ừm thì」
- Sửa: 「A!? Cái đó――không phải, em, ừm thì」
- Lý do: Hachiroku tự xưng: 'em' nhất quán toàn file (1644, 1667, 2237, 2271, 2426, 2510, 2761). VN cũ 'tôi' sai.

### 2382 — ポーレット — thuật ngữ
- JP: 「うふふ、どういたしまして。それじゃ、\\n御一夜鉄道社長として――もう一回、聞きますね？」
- TW: 「嘻嘻，不客氣。那我以御一夜鐵路社長的身份再問一次囉？」
- VN cũ: 「Ufufu, không có chi. Vậy thì,\\nvới tư cách là giám đốc Đường sắt Ohigawa――tôi hỏi lại lần nữa nhé?」
- Sửa: 「Ufufu, không có chi. Vậy thì,\\nvới tư cách là giám đốc Đường sắt Ohitoyo――tôi hỏi lại lần nữa nhé?」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2390 — オリヴィ — thuật ngữ
- JP: 「ふーん、あのグージさん、\\n帝鉄の\\x%l運転士;#00ffc040;運転士%l;#;さんだったんだー」
- TW: 「噢，那位宮司，以前是帝國鐵路的\\x%l運転士;#00ffc040;駕駛員%l;#;啊」
- VN cũ: 「Hừm, vị đền chủ đó,\\ntừng là \\x%l運転士;#00ffc040;lái tàu%l;#; của Đường sắt Hoàng gia sao~」
- Sửa: 「Hừm, vị đền chủ đó,\\ntừng là \\x%l運転士;#00ffc040;lái tàu%l;#; của Teitetsu sao~」
- Lý do: JP 帝鉄. VN cũ 'Đường sắt Hoàng gia' là dạng cũ; thuật ngữ đã chốt: 帝鉄='Teitetsu' (tiền lệ ハチロク10 sửa 3 dòng Teitetsu trong audit).

### 2393 — 凪 — thuật ngữ
- JP: 「オリヴィ今度！　クマ川くだりに遊びにくるばい！\\n歓迎のしるしに、凪さま直々に船頭するけん！！」
- TW: 「回頭奧莉薇來咱隈河漂流玩兒唄！本小姐親自給你掌棹！！」
- VN cũ: 「Lần tới Olivy! Hãy đến chơi chuyến đi thuyền trên sông Kuma nha!\\nĐể chào mừng, Nagi đại nhân đây sẽ đích thân chèo thuyền cho cậu!!」
- Sửa: 「Lần tới Olivy! Hãy đến chơi chuyến đi thuyền trên sông Kuma nha!\\nĐể chào mừng, Bổn tiểu thư đây sẽ đích thân chèo thuyền cho cậu!!」
- Lý do: JP 凪さま. VN cũ 'Nagi đại nhân' không khớp quy ước; tiền lệ 凪ふかみ01: 凪さま→'Bổn tiểu thư' (8 dòng), TW 本小姐 xác nhận.

### 2399 — ポーレット — thuật ngữ
- JP: 「オリヴィちゃんの運用にあたって推奨される毎年の全検。\\nこれに応じることは、御一夜鉄道の資産では不可能です」
- TW: 「大宮強烈建議每年對擔任乘務工作的奧莉薇進行全檢，可以目前御一夜鐵路的資產狀況而言是無法負擔的」
- VN cũ: 「Việc kiểm tra toàn diện hàng năm được khuyến nghị cho quá trình vận hành của Olivy.\\nVới tài sản hiện tại của Đường sắt Ohito thì không thể đáp ứng được.」
- Sửa: 「Việc kiểm tra toàn diện hàng năm được khuyến nghị cho quá trình vận hành của Olivy.\\nVới tài sản hiện tại của Đường sắt Ohitoyo thì không thể đáp ứng được.」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2418 — 双鉄 — đại từ + thuật ngữ
- JP: 「オリヴィは最新の保線技術の知識も有している。\\n僕はそれを、御一夜鉄道にも伝えて欲しいと願っている」
- TW: 「奧莉薇掌握著最新的巡線技術和知識，我們希望你能把這些傳授給御一夜鐵路」
- VN cũ: 「Olivy cũng có kiến thức về kỹ thuật bảo trì đường ray mới nhất.\\nTôi cũng mong em có thể truyền đạt điều đó cho Đường sắt Ohito.」
- Sửa: 「Olivy cũng có kiến thức về kỹ thuật bảo trì đường ray mới nhất.\\nAnh cũng mong em có thể truyền đạt điều đó cho Đường sắt Ohitoyo.」
- Lý do: Soutetsu nói với Olivy ('em' = Olivy, người sẽ truyền đạt): Soutetsu xưng 'anh' với Olivy — tiền lệ ハチロク05 kiểm chứng sạch 8 dòng 'anh'/'em' với Olivy. VN cũ 'Tôi' sai. (Cùng dòng sửa Ohito→Ohitoyo.)

### 2444 — 双鉄 — thuật ngữ
- JP: 「\\x%lタブレット;#00ffc040;タブレット%l;#;を――\\x%lタブレット;#00ffc040;タブレット%l;#;たらしめる」
- TW: 「實現\\x%lタブレット;#00ffc040;操作板%l;#;功能——的東西」
- VN cũ: 「Thứ khiến \\x%lタブレット;#00ffc040;Thẻ bảng%l;#;――trở thành \\x%lタブレット;#00ffc040;Thẻ bảng%l;#;」
- Sửa: 「Thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#;――trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;」
- Lý do: JP タブレット (thẻ %l giữ nguyên). VN cũ gloss 'Thẻ bảng' sai; thuật ngữ đã chốt: タブレット='máy tính bảng' (tiền lệ ハチロク10).

### 2451 — ハチロク — thuật ngữ
- JP: 「電車姫様のご照会を受け、もしもポーレット様が、\\nオリヴィちゃんに何も尋ねず、それに応じていたときと」
- TW: 「對電車公主殿下過目的請求，如果波萊特大人不與奧莉薇做任何確認直接應允」
- VN cũ: 「Khi nhận được yêu cầu từ Điện xá Công chúa điện hạ, giả sử cô Paulette,\\nkhông hỏi han gì Olivy mà cứ thế đáp ứng」
- Sửa: 「Khi nhận được yêu cầu từ Công chúa Tàu điện, giả sử cô Paulette,\\nkhông hỏi han gì Olivy mà cứ thế đáp ứng」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2453 — ふかみ — đại từ
- JP: 「ちょ、凪ちゃん！　今そんな話したら」
- TW: 「小、小凪！怎麼能這麼說呢」
- VN cũ: 「Này, Nagi! Sao em lại nói chuyện đó lúc này chứ......」
- Sửa: 「Này, Nagi! Sao cậu lại nói chuyện đó lúc này chứ......」
- Lý do: Fukami nói với Nagi (gọi tên 'Nagi!'): Fukami→Nagi là 'cậu', không bao giờ 'em' (quy tắc đã sửa 20/11 — Fukami và Nagi cùng tuổi, 'friends'). VN cũ 'em' sai.

### 2487 — 双鉄 — thuật ngữ
- JP: 「朝の会議で、電車姫様にいただいたご助言を元に、\\nポーレットはもうひとつ会議を開催せねばと決めたのだ」
- TW: 「後面的會議是波萊特基於電車公主殿下在晨會上的建議，決定加開的」
- VN cũ: 「Dựa trên lời khuyên của Điện xá Công chúa điện hạ trong cuộc họp buổi sáng,\\nPaulette đã quyết định phải tổ chức thêm một cuộc họp nữa」
- Sửa: 「Dựa trên lời khuyên của Công chúa Tàu điện trong cuộc họp buổi sáng,\\nPaulette đã quyết định phải tổ chức thêm một cuộc họp nữa」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2490 — ポーレット — thuật ngữ
- JP: 「御一夜鉄道には、他の鉄道会社にあるような、\\n帝鉄時代からの経験の引き継ぎが存在しません」
- TW: 「御一夜鐵路和其他鐵路公司不同，並沒有沿襲自帝國鐵路時代的經驗」
- VN cũ: 「Đường sắt Ohito không giống như các công ty đường sắt khác,\\nkhông có sự kế thừa kinh nghiệm từ thời Đường sắt Hoàng gia.」
- Sửa: 「Đường sắt Ohitoyo không giống như các công ty đường sắt khác,\\nkhông có sự kế thừa kinh nghiệm từ thời Teitetsu.」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2508 — 双鉄 — đại từ
- JP: 「僕もです」
- TW: 「我也一樣」
- VN cũ: 「Tôi cũng vậy」
- Sửa: 「Anh cũng vậy」
- Lý do: Soutetsu trả lời Hibiki (dòng kề 2506: Hibiki gọi 'anh hai', nói với Soutetsu): Soutetsu xưng 'anh' với Hibiki theo quy tắc đã chốt. VN cũ 'Tôi' sai.

### 2529 — ニイロク — thuật ngữ
- JP: 「自分は。ニイロク。[きゅうていてつしけんがたとっきゅうけいでんしゃ,10]旧帝鉄試験形特急系電車クハ２６の、\\n専用\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;――だったものだ」
- TW: 「我叫二六。是前帝國鐵路測試型特快電車Ｋｕｈａ２６的專用\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;——不過那都是過去的事了」
- VN cũ: 「Tôi là. Niiroku. Từng là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\ntàu điện tốc hành nguyên mẫu Kuha 26 thuộc Đường sắt Hoàng gia cũ.」
- Sửa: 「Tôi là. Niiroku. Từng là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\ntàu điện tốc hành nguyên mẫu Kuha 26 thuộc Teitetsu cũ.」
- Lý do: JP 旧帝鉄. VN cũ 'Đường sắt Hoàng gia cũ' là dạng cũ; thuật ngữ đã chốt: 帝鉄='Teitetsu' → 'Teitetsu cũ' (tiền lệ ハチロク10).

### 2532 — ポーレット — thuật ngữ
- JP: 「オリヴィちゃんが前回[おおみや,1]旺宮で受けた検査の結果を、\\nわたしは、電車姫様に確認してもらいたいと思います」
- TW: 「我想要把奧莉薇之前去大宮接受檢查的結果，交給電車公主殿下過目」
- VN cũ: 「Kết quả kiểm tra lần trước của Olivy ở Omiya,\\ntôi muốn để Điện xá Công chúa điện hạ xác nhận」
- Sửa: 「Kết quả kiểm tra lần trước của Olivy ở Omiya,\\ntôi muốn để Công chúa Tàu điện xác nhận」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2533 — ハチロク — thuật ngữ
- JP: 「わたくしは、ハチロク。\\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;、\\n御一夜鉄道8620の専用\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;でございます」
- TW: 「我是八六。是御一夜鐵路８６２０\\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;的專用\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;」
- VN cũ: 「Tôi là Hachiroku. \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\n\\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; 8620 thuộc Đường sắt Ohito.」
- Sửa: 「Tôi là Hachiroku. \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\n\\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; 8620 thuộc Đường sắt Ohitoyo.」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2548 — ニイロク — gasp (sweep)
- JP: 「っ！！？」\\n「まぁ！」
- TW: 「我！！？」\\n「啊！」
- VN cũ: 「!!?」\\n「Trời ạ!」
- Sửa: 「Ư!!?」\\n「Trời ạ!」
- Lý do: Sweep lost-gasp-whole: JP 「っ！！？」 cả dòng là gasp, VN cũ chỉ còn dấu câu. Thêm Ư theo quy tắc gasp đã chốt. Đã kiểm chứng giá trị sweep với JP.

### 2561 — ポーレット — thuật ngữ
- JP: 「だから。――オリヴィちゃんの検査記録を、\\n電車姫様にみてもらっても、いいですか？」
- TW: 「所以，我可以把奧莉薇的檢查記錄，交給電車公主殿下過目嗎？」
- VN cũ: 「Vậy nên. ――Hồ sơ kiểm tra của Olivy,\\nđể Điện xá Công chúa điện hạ xem qua, có được không?」
- Sửa: 「Vậy nên. ――Hồ sơ kiểm tra của Olivy,\\nđể Công chúa Tàu điện xem qua, có được không?」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2565 — ハチロク — đại từ
- JP: 「すみません。心配をするにしても、伝え方、ですよね。\\nわたくし、何度も同じ過ちを繰り返してしまって」
- TW: 「抱歉。即便是擔心，但是表達方法也仍是確有不妥。我也是，這一樣的錯誤都犯了這麼多次了竟還是這樣」
- VN cũ: 「Xin lỗi ạ. Dù là lo lắng thì cũng phải biết cách truyền đạt nhỉ.\\nTôi cứ lặp đi lặp lại cùng một sai lầm mãi thôi」
- Sửa: 「Xin lỗi ạ. Dù là lo lắng thì cũng phải biết cách truyền đạt nhỉ.\\nEm cứ lặp đi lặp lại cùng một sai lầm mãi thôi」
- Lý do: Hachiroku tự xưng 'em' nhất quán toàn file (đang xin lỗi Olivy/nhóm). VN cũ 'Tôi' sai.

### 2608 — ポーレット — thuật ngữ
- JP: 「そう、オリヴィちゃん。今日、電車姫様にもご相談して、\\nわたしの考え、伝えておいた方がいいって思ったの」
- TW: 「是的，奧莉薇。今天在和電車公主殿下商討過後，我覺得還是應該把我的想法公開出來討論比較好」
- VN cũ: 「Đúng vậy, Olivy. Hôm nay, sau khi bàn bạc với Điện xá Công chúa điện hạ,\\ntôi nghĩ tốt nhất là nên truyền đạt lại suy nghĩ của mình」
- Sửa: 「Đúng vậy, Olivy. Hôm nay, sau khi bàn bạc với Công chúa Tàu điện,\\ntôi nghĩ tốt nhất là nên truyền đạt lại suy nghĩ của mình」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2614 — ポーレット — thuật ngữ
- JP: 「そう……ですか？\\n電車姫様がそうおっしゃるなら、わたしからは何も」
- TW: 「是這樣嗎？不過電車公主殿下既然這樣說，我們也就不再多言了」
- VN cũ: 「Vậy…… sao ạ?\\nNếu Điện xá Công chúa điện hạ đã nói thế, thì tôi không ý kiến gì nữa」
- Sửa: 「Vậy…… sao ạ?\\nNếu Công chúa Tàu điện đã nói thế, thì tôi không ý kiến gì nữa」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2679 — ふかみ — thân tộc
- JP: 「おじいちゃんたち、観光船協会の慰安旅行があって。\\nでも、いつでも電話して大丈夫って、です」
- TW: 「爺爺他們去參加觀光船協會組織的慰勞旅行去了。不過隨時都可以電話聯繫的，嗯」
- VN cũ: 「Ông nội và mọi người đi tham gia chuyến du lịch giải khuây của hiệp hội thuyền du lịch rồi.\\nNhưng mà, gọi điện lúc nào cũng được, ạ......」
- Sửa: 「Ông ngoại và mọi người đi tham gia chuyến du lịch giải khuây của hiệp hội thuyền du lịch rồi.\\nNhưng mà, gọi điện lúc nào cũng được, ạ......」
- Lý do: Fukami nói về 'おじいちゃんたち' (các ông) đi du lịch của hiệp hội thuyền du lịch. Đây là nhóm Seki + anh em (堰さんたち, key 2596 cùng file) — Seki là ông ngoại của Fukami (quyết định 20/11: Seki='ông ngoại'; chỉ các dòng liên quan Seki đổi). Dòng này không nằm trong 4 dòng parent đã liệt kê (vì không nêu tên Seki) nhưng cùng nhóm người — sửa 'ông nội'→'ông ngoại'. Ghi chú rõ để parent kiểm chứng lại (xem §6).

### 2695 — 双鉄 — thuật ngữ
- JP: 「そうだな。ご助言の質も実に高い。僕らも御一夜鉄道も、\\nあの方にはずいぶん助けていただいている」
- TW: 「的確。他給我們的建議也都非常有幫助。我們和御一夜鐵路都從他那裡獲益良多」
- VN cũ: 「Đúng vậy. Lời khuyên của ngài ấy cũng rất chất lượng. Cả chúng tôi và Đường sắt Ohito,\\nđều nhận được sự giúp đỡ rất nhiều từ ngài ấy.」
- Sửa: 「Đúng vậy. Lời khuyên của ngài ấy cũng rất chất lượng. Cả chúng tôi và Đường sắt Ohitoyo,\\nđều nhận được sự giúp đỡ rất nhiều từ ngài ấy.」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2739 — 電車姫 — thuật ngữ
- JP: 「浪費と思わば、[さえぎ]遮っておる。御一夜鉄道という組織の\\nつながりの強さを目の当たりにできたことも、良かった」
- TW: 「若余當真覺得無聊，便早出言打斷了。得親眼目睹御一夜鐵路眾人相處之融洽，實幸事也」
- VN cũ: 「Nếu thấy lãng phí, ta đã ngắt lời rồi. Việc được tận mắt chứng kiến\\nsự gắn kết bền chặt của tổ chức Đường sắt Ohigawa, cũng là một điều tốt」
- Sửa: 「Nếu thấy lãng phí, ta đã ngắt lời rồi. Việc được tận mắt chứng kiến\\nsự gắn kết bền chặt của tổ chức Đường sắt Ohitoyo, cũng là một điều tốt」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2745 — 電車姫 — thuật ngữ
- JP: 「毎年の全検など、御一夜鉄道の資本力では\\nとても果たせることではないと――わかっておろう？」
- TW: 「若言每年之全檢，以御一夜鐵路之資本實力，幾無負擔之可能——汝亦心知肚明否？」
- VN cũ: 「Kiểm tra toàn diện hàng năm, với tiềm lực vốn của Đường sắt Ohigawa\\nthì không thể nào thực hiện được――ngươi biết chứ?」
- Sửa: 「Kiểm tra toàn diện hàng năm, với tiềm lực vốn của Đường sắt Ohitoyo\\nthì không thể nào thực hiện được――ngươi biết chứ?」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2759 — ポーレット — thuật ngữ
- JP: 「そうなっちゃったら……そうね、わたしは電車姫様に、\\n『今すぐにはご容赦ください』って、お願いします」
- TW: 「要真是那樣的話……嗯，我大概會請求電車公主殿下稍作等待」
- VN cũ: 「Nếu vậy thì…… xem nào, tôi sẽ thưa với Điện xá Công chúa điện hạ,\\n'Xin ngài thứ lỗi cho lúc này'」
- Sửa: 「Nếu vậy thì…… xem nào, tôi sẽ thưa với Công chúa Tàu điện,\\n'Xin ngài thứ lỗi cho lúc này'」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2770 — オリヴィ — thuật ngữ
- JP: 「そうだけど――\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;にそんなこと聞くなんて、\\nオヒトヨ鉄道ってほんっとに……」
- TW: 「話是沒錯——但你這麼問\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;……果然御一夜鐵路就是這樣……」
- VN cũ: 「Đúng là vậy nhưng――đi hỏi \\x%lレイルロオド;#00ffc040;Railord%l;#; mấy chuyện đó,\\nĐường sắt Ohigawa đúng là……」
- Sửa: 「Đúng là vậy nhưng――đi hỏi \\x%lレイルロオド;#00ffc040;Railord%l;#; mấy chuyện đó,\\nĐường sắt Ohitoyo đúng là……」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2814 — 双鉄 — thuật ngữ
- JP: 「それだけ、\\n御一夜鉄道を重要視してくれているということだろう」
- TW: 「這也從另一方面說明，那些人是多麼重視御一夜鐵路吧」
- VN cũ: 「Điều đó chứng tỏ,\\nhọ rất coi trọng Đường sắt Ohigawa đấy」
- Sửa: 「Điều đó chứng tỏ,\\nhọ rất coi trọng Đường sắt Ohitoyo đấy」
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 2817 — 双鉄 — thuật ngữ
- JP: 「はい――電車姫さまのお言葉をつなげただけですので。\\nどうぞ、ご随意にお取扱いいただけましたらと」
- TW: 「這名字不過是由電車公主殿下的話語中拼摘而來，大可隨意使用」
- VN cũ: 「Vâng――tôi chỉ ghép lại từ những lời của Điện xá Công chúa điện hạ thôi ạ.\\nXin ngài cứ tùy ý sử dụng」
- Sửa: 「Vâng――tôi chỉ ghép lại từ những lời của Công chúa Tàu điện thôi ạ.\\nXin ngài cứ tùy ý sử dụng」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2824 — ポーレット — thuật ngữ
- JP: 「今回の書類、\\nわたしは、電車姫様に見ていただくべきと思うの」
- TW: 「這次的資料，我覺得應該讓電車公主殿下過目」
- VN cũ: 「Tài liệu lần này,\\ntôi nghĩ nên để Điện xá Công chúa điện hạ xem qua」
- Sửa: 「Tài liệu lần này,\\ntôi nghĩ nên để Công chúa Tàu điện xem qua」
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 2828 — ニイロク — gasp (sweep)
- JP: 「っ！！？」
- TW: 「這！！？」
- VN cũ: 「!!?」
- Sửa: 「Ư!!?」
- Lý do: Sweep lost-gasp-whole: JP 「っ！！？」 cả dòng là gasp, VN cũ chỉ còn dấu câu. Thêm Ư. Đã kiểm chứng với JP.

### 2829 — 双鉄 — đại từ
- JP: 「いや、僕は――」
- TW: 「這，我倒是沒有——」
- VN cũ: 「Không, tôi thì——」
- Sửa: 「Không, anh thì——」
- Lý do: Soutetsu nói với Niiroku (dòng kề 2833 'Em có ý kiến khác sao?' — 'em' = Niiroku): trong file này Soutetsu xưng 'anh' với Niiroku ở 2486 ('anh cũng không biết'), 2520 ('cậu'), 2521 ('Bọn anh'). VN cũ 'Tôi' lệch khỏi mẫu trong file. (2538 'Tôi là Migita Soutetsu' giữ nguyên — tự giới thiệu trang trọng với cả nhóm.)

### 2839 — 双鉄 — thuật ngữ
- JP: 「\\x%lタブレット;#00ffc040;タブレット%l;#;を再現……あるいは新造しようとしても、\\n果たせない――というほどの意味でしょうか？」
- TW: 「那也就是說，復現操作板……或者說製造新的\\x%lタブレット;#00ffc040;操作板%l;#;已經不可能了，對嗎？」
- VN cũ: 「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \\x%lタブレット;#00ffc040;Thẻ bảng%l;#;,\\ncũng không thể thực hiện được――đúng không ạ?」
- Sửa: 「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\ncũng không thể thực hiện được――đúng không ạ?」
- Lý do: JP タブレット (thẻ %l giữ nguyên). VN cũ gloss 'Thẻ bảng' sai; thuật ngữ đã chốt: タブレット='máy tính bảng' (tiền lệ ハチロク10).

### 2844 — 電車姫 — thuật ngữ
- JP: 「それらの問題も無論ある。が、純粋な技術面でもまた、\\nどうにもならぬ。ロオドコアをまるで再現できぬのじゃ」
- TW: 「那些方面雖亦有問題，但純就技術層面而言，亦已無力回天。日本國內早已不再具備復現人偶核之能力」
- VN cũ: 「Đương nhiên cũng có những vấn đề đó. Nhưng về mặt kỹ thuật thuần túy,\\ncũng bó tay. Hoàn toàn không thể tái tạo lại Lõi Lord được」
- Sửa: 「Đương nhiên cũng có những vấn đề đó. Nhưng về mặt kỹ thuật thuần túy,\\ncũng bó tay. Hoàn toàn không thể tái tạo lại Lõi Railord được」
- Lý do: JP ロオドコア. VN cũ 'Lõi Lord' đọc sai ロオド thành 'Lord'; TW 人偶核 (= lõi Railord) xác nhận. Sửa 'Lõi Railord'.

### 2850 — ポーレット — thuật ngữ
- JP: 「ロオドコアって――なんですか？　それ」
- TW: 「那個是叫人偶核嗎？」
- VN cũ: 「Lõi Lord――là gì vậy ạ? Cái đó ấy」
- Sửa: 「Lõi Railord――là gì vậy ạ? Cái đó ấy」
- Lý do: JP ロオドコア. VN cũ 'Lõi Lord' đọc sai ロオド thành 'Lord'; TW 人偶核 xác nhận. Sửa 'Lõi Railord'.

### 2905 — ハチロク — đại từ
- JP: 「いえ。オリヴィちゃんと触れ合ううちに知りました。\\nわたくしの知る“鉄道”は、ごく限られた一部のみです」
- TW: 「非也。和奧莉薇接觸後我才明白，我對“鐵路”的了解，其實不過管中窺豹而已」
- VN cũ: 「Không đâu. Trong quá trình tiếp xúc với Olivy, tôi mới nhận ra.\\n“Đường sắt” mà tôi biết, chỉ là một phần rất nhỏ bé mà thôi.」
- Sửa: 「Không đâu. Trong quá trình tiếp xúc với Olivy, em mới nhận ra.\\n“Đường sắt” mà em biết, chỉ là một phần rất nhỏ bé mà thôi.」
- Lý do: Hachiroku tự xưng 'em' nhất quán toàn file (2 chỗ trong dòng). VN cũ 'tôi' sai cả hai.

### 3121 — monologue — thuật ngữ
- JP: 無意識にだろう。ハチロクが首元の\\x%lタブレット;#00ffc040;タブレット%l;#;に触れる。\\n\\x%lタブレット;#00ffc040;タブレット%l;#;……確かに、極めて定義の難しいものだ。
- TW: 不知是有意還是無意，八六碰了碰頸間的\\x%lタブレット;#00ffc040;操作板%l;#;。\\x%lタブレット;#00ffc040;操作板%l;#;……還確實是個很難簡單定義的東西。
- VN cũ: Chắc là trong vô thức. Hachiroku chạm vào chiếc \\x%lタブレット;#00ffc040;Thẻ bảng%l;#; trên cổ.\\n\\x%lタブレット;#00ffc040;Thẻ bảng%l;#;…… quả thực là một thứ vô cùng khó định nghĩa.
- Sửa: Chắc là trong vô thức. Hachiroku chạm vào chiếc \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trên cổ.\\n\\x%lタブレット;#00ffc040;Máy tính bảng%l;#;…… quả thực là một thứ vô cùng khó định nghĩa.
- Lý do: JP タブレット ×2 (thẻ %l giữ nguyên). VN cũ gloss 'Thẻ bảng' sai; thuật ngữ đã chốt: タブレット='máy tính bảng' (tiền lệ ハチロク10). Gloss thứ hai ở đầu câu nên viết hoa 'Máy tính bảng'.

### 3135 — monologue — thuật ngữ
- JP: いや、ほぼ間違いない。\\n\\x%l運転体;#00ffc040;運転体%l;#;の、\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が。
- TW: 不，應該基本上可以肯定了。那就是一個\\x%l運転体;#00ffc040;駕駛體%l;#;的\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;。
- VN cũ: Không, gần như chắc chắn rồi.\\nLà một \\x%lレイルロオド;#00ffc040;Railord%l;#; trong \\x%l運転体;#00ffc040;kíp lái%l;#;.
- Sửa: Không, gần như chắc chắn rồi.\\nLà một \\x%lレイルロオド;#00ffc040;Railord%l;#; trong \\x%l運転体;#00ffc040;thân vận hành%l;#;.
- Lý do: JP 運転体. VN cũ 'kíp lái' sai; thuật ngữ đã chốt: 運転体='thân vận hành' (tiền lệ ハチロク10, 凪ふかみ01).

### 3161 — monologue — thuật ngữ
- JP: 電車姫様への、あまりにも親しげな口調にだろう。
- TW: 以如此口吻與電車公主殿下對話，未免有失禮數。
- VN cũ: Có lẽ là vì giọng điệu quá đỗi thân mật với Điện xá Công chúa điện hạ.
- Sửa: Có lẽ là vì giọng điệu quá đỗi thân mật với Công chúa Tàu điện.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3174 — monologue — thuật ngữ
- JP: 今のほんの一言だけで、輝くような笑顔だけでも、\\n電車姫様にも、はっきり伝わるものなのだと。
- TW: 僅透過適才的隻言片語，以及開口時的璀璨笑容，想必電車公主殿下已是看在眼裡，瞭然於心了吧。
- VN cũ: Chỉ bằng một câu nói vừa rồi, chỉ bằng nụ cười rạng rỡ ấy,\\ncũng đủ để truyền đạt rõ ràng đến Điện xá Công chúa điện hạ.
- Sửa: Chỉ bằng một câu nói vừa rồi, chỉ bằng nụ cười rạng rỡ ấy,\\ncũng đủ để truyền đạt rõ ràng đến Công chúa Tàu điện.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3294 — monologue — thuật ngữ
- JP: ドアが閉まる音が響いた途端、\\n電車姫様の瞳がスウっと――刃物のように鋭く細まる。
- TW: 就在關門的響聲傳入耳中的時候，電車公主殿下的眼神突然變得犀利了起來。
- VN cũ: Ngay khi tiếng đóng cửa vang lên,\\nánh mắt của Điện xá Công chúa điện hạ vụt――nheo lại sắc lẹm như lưỡi dao.
- Sửa: Ngay khi tiếng đóng cửa vang lên,\\nánh mắt của Công chúa Tàu điện vụt――nheo lại sắc lẹm như lưỡi dao.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3310 — monologue — thuật ngữ
- JP: みかん鉄道から御一夜鉄道に移籍した――\\nあの日の、自らの決断を。
- TW: 從橙鐵路轉屬來到御一夜鐵路那一天，自己做出的決定。
- VN cũ: Chuyển từ Đường sắt Mikan sang Đường sắt Ohigawa――\\nQuyết định của chính mình, vào ngày hôm đó.
- Sửa: Chuyển từ Đường sắt Mikan sang Đường sắt Ohitoyo――\\nQuyết định của chính mình, vào ngày hôm đó.
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 3410 — monologue — thuật ngữ
- JP: 豪速球の、ど真ん中だ。\\nなるほどこれが冥国式かと、ズレた感想を抱いてしまう。
- TW: 直截了當，毫不拐彎抹角。原來如此，這就是美國式啊——首先浮現在腦海裡的卻是這個想法。
- VN cũ: Một cú ném thẳng vào giữa trọng tâm.\\nThì ra đây là phong cách Mỹ sao, tôi bất giác có suy nghĩ lệch lạc như vậy.
- Sửa: Một cú ném thẳng vào giữa trọng tâm.\\nThì ra đây là phong cách Minh Quốc sao, tôi bất giác có suy nghĩ lệch lạc như vậy.
- Lý do: JP 冥国式. VN cũ 'phong cách Mỹ' theo TW 美國式; thuật ngữ đã chốt: 冥国='Minh Quốc' (tiền lệ 凪ふかみ01).

### 3412 — monologue — thuật ngữ
- JP: 誰が御一夜鉄道の金庫番なのか、\\n早くも理解したのだろう。
- TW: 看來，她早已理解了是誰在管著御一夜鐵路的錢袋子。
- VN cũ: Có lẽ cô bé đã sớm hiểu được,\\nai mới là người giữ két sắt của Đường sắt Ohito.
- Sửa: Có lẽ cô bé đã sớm hiểu được,\\nai mới là người giữ két sắt của Đường sắt Ohitoyo.
- Lý do: JP 御一夜鉄道. VN cũ 'Đường sắt Ohito'/'Đường sắt Ohigawa' là dạng cũ; thuật ngữ đã chốt: 御一夜='Ohitoyo' (tiền lệ ハチロク10 sửa 5 dòng Ohitoyo trong audit).

### 3451 — monologue — thuật ngữ
- JP: かなり踏み込んだ質問を、直接電車姫様にぶつける――\\nそれが許される程度にまでも。
- TW: 而究竟拉近到什麼程度呢？從我們可以就如此程度的問題直接向她求助便可見一斑。
- VN cũ: Đặt những câu hỏi khá sâu sát, trực tiếp với Điện xá Công chúa điện hạ――\\nĐến mức độ được phép làm như vậy.
- Sửa: Đặt những câu hỏi khá sâu sát, trực tiếp với Công chúa Tàu điện――\\nĐến mức độ được phép làm như vậy.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3525 — monologue — thuật ngữ
- JP: 扇子がパっ、と開かれて、\\n電車姫様の口元を覆い隠す。
- TW: 隨後，她又“啪”地打開扇子，輕掩朱唇。
- VN cũ: Chiếc quạt xòe ra cái phạch,\\nche đi khóe miệng của Điện xá Công chúa điện hạ.
- Sửa: Chiếc quạt xòe ra cái phạch,\\nche đi khóe miệng của Công chúa Tàu điện.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3528 — monologue — gasp (sweep)
- JP: “興味を持つはず”とは聞かされていたが、\\nこれほどまでとは思ってなか――っ！！
- TW: 雖然赤井宮司確實說了“能令其提起興致”，但我也確實沒料到竟會如此——啊！！
- VN cũ: Dù đã nghe nói là "chắc chắn sẽ hứng thú",\\nnhưng tôi không ngờ lại đến mức này——!!
- Sửa: Dù đã nghe nói là "chắc chắn sẽ hứng thú",\\nnhưng tôi không ngờ lại đến mức này——Ư!!
- Lý do: Sweep lost-gasp-trailing: JP '――っ！！' (gasp sau dấu gạch), VN cũ giữ dấu gạch nhưng làm mất gasp. Thêm Ư sau dấu gạch. Đã kiểm chứng với JP.

### 3531 — monologue — thuật ngữ
- JP: 電車姫様は、オリヴィの運用計画をポーレットに聞き、\\nその上で、早く公開するべきであるとのご助言を下さった。
- TW: 電車公主在向波萊特詢問了奧莉薇的使用計劃後，給了我們應儘早公開這點的建議。
- VN cũ: Điện xá Công chúa điện hạ đã nghe kế hoạch vận hành Olivy từ Paulette,\\nvà dựa trên đó, ngài đã khuyên nên công bố sớm.
- Sửa: Công chúa Tàu điện đã nghe kế hoạch vận hành Olivy từ Paulette,\\nvà dựa trên đó, ngài đã khuyên nên công bố sớm.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3532 — monologue — thuật ngữ
- JP: パチリ、電車姫様は扇子を一瞬強く閉じ、\\n乾いた音を響かせる。
- TW: 電車公主殿下乾脆俐落地合起了扇子，只留清脆的聲音傳入我們耳中。
- VN cũ: Cạch, Điện xá Công chúa điện hạ khép quạt lại thật mạnh trong tích tắc,\\ntạo ra một âm thanh khô khốc.
- Sửa: Cạch, Công chúa Tàu điện khép quạt lại thật mạnh trong tích tắc,\\ntạo ra một âm thanh khô khốc.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3533 — monologue — thuật ngữ
- JP: パチン、パチンと、小刻みに電車姫様の扇子が鳴らされる。
- TW: 電車公主殿下手中的扇子開開合合，發出“啪啪”的聲響。
- VN cũ: Lạch cạch, lạch cạch, chiếc quạt của Điện xá Công chúa điện hạ nhịp nhàng gõ nhẹ.
- Sửa: Lạch cạch, lạch cạch, chiếc quạt của Công chúa Tàu điện nhịp nhàng gõ nhẹ.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3534 — monologue — thuật ngữ
- JP: 画面外から伸びてきた手が渡した書類を、\\nぱらぱらと、電車姫様は驚くべき速度で繰っていく。
- TW: 電車公主殿下接過畫面外伸來的手中的文件，開始以驚人的速度翻閱了起來。
- VN cũ: Nhận lấy tập tài liệu từ bàn tay vươn ra ngoài khung hình,\\nĐiện xá Công chúa điện hạ lật giở với tốc độ đáng kinh ngạc.
- Sửa: Nhận lấy tập tài liệu từ bàn tay vươn ra ngoài khung hình,\\nCông chúa Tàu điện lật giở với tốc độ đáng kinh ngạc.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3535 — monologue — thuật ngữ
- JP: 電車姫様は、いとも楽しげな笑いを零す。\\nその口元はけれどもすぐに、扇によって隠されてしまう。
- TW: 電車公主殿下滿面笑容似乎頗顯樂在其中。不過轉眼便又舉起了扇子半掩住了面孔。
- VN cũ: Điện xá Công chúa điện hạ, bật cười vô cùng thích thú.\\nNhưng ngay sau đó, khóe miệng ngài đã bị chiếc quạt che khuất.
- Sửa: Công chúa Tàu điện, bật cười vô cùng thích thú.\\nNhưng ngay sau đó, khóe miệng ngài đã bị chiếc quạt che khuất.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3536 — monologue — thuật ngữ
- JP: ほんの一瞬――電車姫様が息を呑む。
- TW: 電車公主殿下的氣息甚至也為之短暫地一滯。
- VN cũ: Chỉ một khoảnh khắc――Điện xá Công chúa điện hạ nín thở.
- Sửa: Chỉ một khoảnh khắc――Công chúa Tàu điện nín thở.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3537 — monologue — thuật ngữ
- JP: 瞳に束の間うかんでみえた、淋しげな陰りをかき消して、\\n電車姫様の視線が左に動く。
- TW: 電車公主殿下的眼中閃過一絲落寞的陰影，但她隨即將視線向左移去。
- VN cũ: Xua đi nét u buồn thoáng hiện trong đôi mắt,\\nánh nhìn của Điện xá Công chúa điện hạ chuyển sang trái.
- Sửa: Xua đi nét u buồn thoáng hiện trong đôi mắt,\\nánh nhìn của Công chúa Tàu điện chuyển sang trái.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3538 — monologue — thuật ngữ
- JP: 機嫌よさそうなひとあおぎ。\\n電車姫様の瞳がス――と細まる
- TW: 電車公主殿下眯起了眼睛，心情看起來不錯。
- VN cũ: Một cái quạt có vẻ đầy mãn nguyện.\\nĐôi mắt của Điện xá Công chúa điện hạ khẽ――nheo lại.
- Sửa: Một cái quạt có vẻ đầy mãn nguyện.\\nĐôi mắt của Công chúa Tàu điện khẽ――nheo lại.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3540 — monologue — thuật ngữ
- JP: ふぁさっと小さく扇子が動けば、電車姫様の髪も揺れる。
- TW: 電車公主殿下輕搖手中的扇子，秀髮也隨之飄擺。
- VN cũ: Chiếc quạt nhỏ khẽ phe phẩy, mái tóc của Điện xá Công chúa điện hạ cũng đung đưa theo.
- Sửa: Chiếc quạt nhỏ khẽ phe phẩy, mái tóc của Công chúa Tàu điện cũng đung đưa theo.
- Lý do: JP 電車姫様. VN cũ 'Điện xá Công chúa điện hạ' là dạng cũ; thuật ngữ đã chốt: 電車姫='Công chúa Tàu điện' (không kèm 'điện hạ' — khớp 2 dòng đúng sẵn trong file này: 3138, 3282; tiền lệ ハチロク10 sửa 4 dòng 電車姫 trong audit).

### 3584 — monologue — SFX
- JP: （つぽっ）
- TW: （拔出）
- VN cũ: （Bóp）
- Sửa: （Póc）
- Lý do: JP （つぽっ） là tiếng 'póc' khi rút nhiệt kế khỏi miệng Hachiroku (độc thoại 3333: 'rút chiếc nhiệt kế em ấy đang ngậm trong miệng ra'; TW （拔出） = rút ra). VN cũ '(Bóp)' (bóp/nắn) sai âm — sửa '(Póc)'.

## §3. Sweep っ-gasp kiểm chứng

- Sweep có đúng 4 mục cho file này (2548, 2828, 3528, 2292) — nhận 3 fix (2548, 2828, 3528; xem §2), 2292 là already-rendered (JP 「っ！」 → VN "A!" — gasp đã diễn bằng câu cảm thán, không sửa).
- Quét máy bổ sung toàn file: các っ còn lại đều đã được diễn hoặc thuộc quy ước dự án — あっ→"A" (2328), あっ！？→"A!?" (2340), はうっ→"Hau" (2308), うんっ→"Vâng" (2920), うっ→"ư" (2324), ちがうっ→"khác luôn!" (2700, っ nhấn mạnh dính từ nội dung, không phải gasp). Kiểm chứng quy ước toàn dự án bằng CSV3: あっ→"A." 16×/"A" 8×; あっ！？→"A!?" 14×; はうっ→"Hau" 8×/"Hau!?" 6×/"Hau." 5×; うんっ→"Vâng!" 9× — không còn gasp nào sweep bỏ sót.

## §4. Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai)

- Key 2308 はうっ→"Hau……": giữ nguyên theo quy ước toàn dự án (はうっ→"Hau" là dạng phổ biến nhất; tiền lệ file khác: "はうっ→'Hau' giữ" khi JP không có "!").
- Key 2328 あっ→"A", 2340 あっ！？→"A!?": giữ nguyên theo quy ước toàn dự án (xem §3).
- Key 2920 うんっ→"Vâng!!!": giữ nguyên (うんっ→"Vâng!" là quy ước; んっ cuối → "n" đã chốt).
- Key 2324 あ……うっ――→"A…… ư——", 2325 あ……ぅ→"A……ư.": âm đã diễn, giữ nguyên.
- Key 2339 Fukami "Chị sẽ dạy em cách chơi đùa trên sông nữa!": người nghe là Olivy, không phải Nagi — Nagi là người dân sông Kuma, đã rành chơi sông (chính Nagi mời Olivy ở 2393); Fukami tình nguyện chèo thuyền và dạy người mới là Olivy. "Chị/em" Fukami→Olivy đứng, không sửa.
- Key 2533 "Tôi là Hachiroku" và 2538 "Tôi là Migita Soutetsu": tự giới thiệu trang trọng trong vòng giới thiệu với cả nhóm (gồm Akai, Điện xá Công chúa) — giữ nguyên.
- Key 2513, 2817 Soutetsu "tôi" với Điện xá Công chúa (kèm "ạ"): xưng hô kính trọng với bậc trưởng bối/công chúa — giữ nguyên.
- Key 2874 "きっと上手にバランスを" (JP cụt) → "chắc chắn sẽ cân bằng lại được": VN bổ sung động từ hiển nhiên bị lược — giữ nguyên (không bịa thêm nội dung mới).
- Key 2916–2918 Hachiroku nói ngọng (ふぁ、ほーへふふぁは — nói khi ngậm/miệng đầy): VN diễn rõ nghĩa định sẵn ("A, ngài Soutetsu" / "Vâng, nhờ ngài ạ" / "Ngài cứ yên tâm ạ"); TW diễn bằng pinyin ngọng. Không sửa, nhưng ghi vào §6 để Hieu quyết có muốn giữ nét ngọng hay không.
- Key 2413 Soutetsu "mong em thông cảm cho cô ấy": "cô ấy" = Paulette (người đang lo lắng thái quá) — suy diễn theo cảnh, hợp ngữ cảnh (Olivy vừa phàn nàn bị đối xử như em bé ở 2277) — giữ nguyên.
- Key 3580 độc thoại "(A—— nhắc mới nhớ, … làm mình quên béng mất……)": "mình" trong suy nghĩ ngoặc đơn — giữ theo tiền lệ 1651 "mình đang ngủ gật" (ngoại lệ độc thoại nội tâm).
- Key 2854 Olivy "Để chú ấy học lái…": "chú ấy" = Kiyoharu (người đàn ông lớn tuổi, lái tàu) — đại từ thân tộc cho người được gọi tên, hợp ngữ cảnh — giữ nguyên.
- Key 2596 "堰さんたち" → "ông Seki": số nhiều "tachi" bị lược — giữ nguyên (số nhiều lịch sự, nghĩa mời dự vẫn đủ).
- Key 2379 Densha-hime "Fufu. Em ấy cũng nói vậy mà": chủ ngữ JP bị lược ("と、申してもおるし"); VN chọn "Em ấy" hợp lý — giữ nguyên.
- Key 1697 Niiroku "Tôi, cho Kiyoharu. ——Vì, Kiyoharu.": JP cụt ("自分、が、キヨハルを。――キヨハルの、ために") — VN giữ nguyên dạng cụt, trung thực — giữ nguyên.
- Key 2550 Hachiroku "thà rằng. Tập hợp tất cả mọi người lại cùng một lúc sao ạ?": JP cụt ("いっそのこと、と") — VN giữ dạng gợi ý dở dang — giữ nguyên.
- Key 2299, 2386: TOML-2 làm phẳng \n thành khoảng trắng (đã biết) — không phải lỗi.
- Key 2700 ちがうっ→"khác luôn!": っ nhấn mạnh dính từ nội dung — không thêm Ư theo quy tắc đã chốt.

## §5. Khối TOML (đã parse-kiểm chứng: 64 khóa, 0 sai lệch)

```toml
[script]
1588 = "――6 năm qua. Những thiết kế mà Hibiki tạo ra,\\nđã thực sự kéo gần khoảng cách giữa chúng tôi và Công chúa Tàu điện một cách đáng kể."
1605 = "……Tôi nhìn vào tờ ghi chú lời khuyên của Công chúa Tàu điện."
1640 = "「——Tôi, đã mất thân bảo trì rồi.\\nthân vận hành. Chỉ còn lại cơ thể này thôi.」"
1662 = "「Chỉ là tên gọi tạm thôi. Một thứ không có tên chính thức――\\nLà 'thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;'」"
2173 = "「Railord――Lõi?」"
2203 = "「Bộ phận Cơ khí \\x%lレイルロオド;#00ffc040;Railord%l;#; Teitetsu cũ ở Omiya――\\nNay là Viện nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; Omiya, ta đang đầu tư vốn vào đó」"
2209 = "「Xin chào. Olivy là \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc,\\nbạn là kiểu Hinomoto nhỉ? \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của xe nào vậy?」"
2343 = "「A!? Xin cảm ơn ngài――hơn thế nữa, tôi xin lỗi.\\nChuyện nội bộ của chúng tôi đã làm mất thời gian quý báu của Công chúa Tàu điện――」"
2345 = "「A!? Cái đó――không phải, em, ừm thì」"
2382 = "「Ufufu, không có chi. Vậy thì,\\nvới tư cách là giám đốc Đường sắt Ohitoyo――tôi hỏi lại lần nữa nhé?」"
2390 = "「Hừm, vị đền chủ đó,\\ntừng là \\x%l運転士;#00ffc040;lái tàu%l;#; của Teitetsu sao~」"
2393 = "「Lần tới Olivy! Hãy đến chơi chuyến đi thuyền trên sông Kuma nha!\\nĐể chào mừng, Bổn tiểu thư đây sẽ đích thân chèo thuyền cho cậu!!」"
2399 = "「Việc kiểm tra toàn diện hàng năm được khuyến nghị cho quá trình vận hành của Olivy.\\nVới tài sản hiện tại của Đường sắt Ohitoyo thì không thể đáp ứng được.」"
2418 = "「Olivy cũng có kiến thức về kỹ thuật bảo trì đường ray mới nhất.\\nAnh cũng mong em có thể truyền đạt điều đó cho Đường sắt Ohitoyo.」"
2444 = "「Thứ khiến \\x%lタブレット;#00ffc040;máy tính bảng%l;#;――trở thành \\x%lタブレット;#00ffc040;máy tính bảng%l;#;」"
2451 = "「Khi nhận được yêu cầu từ Công chúa Tàu điện, giả sử cô Paulette,\\nkhông hỏi han gì Olivy mà cứ thế đáp ứng」"
2453 = "「Này, Nagi! Sao cậu lại nói chuyện đó lúc này chứ......」"
2487 = "「Dựa trên lời khuyên của Công chúa Tàu điện trong cuộc họp buổi sáng,\\nPaulette đã quyết định phải tổ chức thêm một cuộc họp nữa」"
2490 = "「Đường sắt Ohitoyo không giống như các công ty đường sắt khác,\\nkhông có sự kế thừa kinh nghiệm từ thời Teitetsu.」"
2508 = "「Anh cũng vậy」"
2529 = "「Tôi là. Niiroku. Từng là \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\ntàu điện tốc hành nguyên mẫu Kuha 26 thuộc Teitetsu cũ.」"
2532 = "「Kết quả kiểm tra lần trước của Olivy ở Omiya,\\ntôi muốn để Công chúa Tàu điện xác nhận」"
2533 = "「Tôi là Hachiroku. \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của\\n\\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; 8620 thuộc Đường sắt Ohitoyo.」"
2548 = "「Ư!!?」\\n「Trời ạ!」"
2561 = "「Vậy nên. ――Hồ sơ kiểm tra của Olivy,\\nđể Công chúa Tàu điện xem qua, có được không?」"
2565 = "「Xin lỗi ạ. Dù là lo lắng thì cũng phải biết cách truyền đạt nhỉ.\\nEm cứ lặp đi lặp lại cùng một sai lầm mãi thôi」"
2608 = "「Đúng vậy, Olivy. Hôm nay, sau khi bàn bạc với Công chúa Tàu điện,\\ntôi nghĩ tốt nhất là nên truyền đạt lại suy nghĩ của mình」"
2614 = "「Vậy…… sao ạ?\\nNếu Công chúa Tàu điện đã nói thế, thì tôi không ý kiến gì nữa」"
2679 = "「Ông ngoại và mọi người đi tham gia chuyến du lịch giải khuây của hiệp hội thuyền du lịch rồi.\\nNhưng mà, gọi điện lúc nào cũng được, ạ......」"
2695 = "「Đúng vậy. Lời khuyên của ngài ấy cũng rất chất lượng. Cả chúng tôi và Đường sắt Ohitoyo,\\nđều nhận được sự giúp đỡ rất nhiều từ ngài ấy.」"
2739 = "「Nếu thấy lãng phí, ta đã ngắt lời rồi. Việc được tận mắt chứng kiến\\nsự gắn kết bền chặt của tổ chức Đường sắt Ohitoyo, cũng là một điều tốt」"
2745 = "「Kiểm tra toàn diện hàng năm, với tiềm lực vốn của Đường sắt Ohitoyo\\nthì không thể nào thực hiện được――ngươi biết chứ?」"
2759 = "「Nếu vậy thì…… xem nào, tôi sẽ thưa với Công chúa Tàu điện,\\n'Xin ngài thứ lỗi cho lúc này'」"
2770 = "「Đúng là vậy nhưng――đi hỏi \\x%lレイルロオド;#00ffc040;Railord%l;#; mấy chuyện đó,\\nĐường sắt Ohitoyo đúng là……」"
2814 = "「Điều đó chứng tỏ,\\nhọ rất coi trọng Đường sắt Ohitoyo đấy」"
2817 = "「Vâng――tôi chỉ ghép lại từ những lời của Công chúa Tàu điện thôi ạ.\\nXin ngài cứ tùy ý sử dụng」"
2824 = "「Tài liệu lần này,\\ntôi nghĩ nên để Công chúa Tàu điện xem qua」"
2828 = "「Ư!!?」"
2829 = "「Không, anh thì——」"
2839 = "「Ý ngài là dù có cố gắng tái tạo…… hay chế tạo mới \\x%lタブレット;#00ffc040;máy tính bảng%l;#;,\\ncũng không thể thực hiện được――đúng không ạ?」"
2844 = "「Đương nhiên cũng có những vấn đề đó. Nhưng về mặt kỹ thuật thuần túy,\\ncũng bó tay. Hoàn toàn không thể tái tạo lại Lõi Railord được」"
2850 = "「Lõi Railord――là gì vậy ạ? Cái đó ấy」"
2905 = "「Không đâu. Trong quá trình tiếp xúc với Olivy, em mới nhận ra.\\n“Đường sắt” mà em biết, chỉ là một phần rất nhỏ bé mà thôi.」"
3121 = "Chắc là trong vô thức. Hachiroku chạm vào chiếc \\x%lタブレット;#00ffc040;máy tính bảng%l;#; trên cổ.\\n\\x%lタブレット;#00ffc040;Máy tính bảng%l;#;…… quả thực là một thứ vô cùng khó định nghĩa."
3135 = "Không, gần như chắc chắn rồi.\\nLà một \\x%lレイルロオド;#00ffc040;Railord%l;#; trong \\x%l運転体;#00ffc040;thân vận hành%l;#;."
3161 = "Có lẽ là vì giọng điệu quá đỗi thân mật với Công chúa Tàu điện."
3174 = "Chỉ bằng một câu nói vừa rồi, chỉ bằng nụ cười rạng rỡ ấy,\\ncũng đủ để truyền đạt rõ ràng đến Công chúa Tàu điện."
3294 = "Ngay khi tiếng đóng cửa vang lên,\\nánh mắt của Công chúa Tàu điện vụt――nheo lại sắc lẹm như lưỡi dao."
3310 = "Chuyển từ Đường sắt Mikan sang Đường sắt Ohitoyo――\\nQuyết định của chính mình, vào ngày hôm đó."
3410 = "Một cú ném thẳng vào giữa trọng tâm.\\nThì ra đây là phong cách Minh Quốc sao, tôi bất giác có suy nghĩ lệch lạc như vậy."
3412 = "Có lẽ cô bé đã sớm hiểu được,\\nai mới là người giữ két sắt của Đường sắt Ohitoyo."
3451 = "Đặt những câu hỏi khá sâu sát, trực tiếp với Công chúa Tàu điện――\\nĐến mức độ được phép làm như vậy."
3525 = "Chiếc quạt xòe ra cái phạch,\\nche đi khóe miệng của Công chúa Tàu điện."
3528 = "Dù đã nghe nói là \"chắc chắn sẽ hứng thú\",\\nnhưng tôi không ngờ lại đến mức này——Ư!!"
3531 = "Công chúa Tàu điện đã nghe kế hoạch vận hành Olivy từ Paulette,\\nvà dựa trên đó, ngài đã khuyên nên công bố sớm."
3532 = "Cạch, Công chúa Tàu điện khép quạt lại thật mạnh trong tích tắc,\\ntạo ra một âm thanh khô khốc."
3533 = "Lạch cạch, lạch cạch, chiếc quạt của Công chúa Tàu điện nhịp nhàng gõ nhẹ."
3534 = "Nhận lấy tập tài liệu từ bàn tay vươn ra ngoài khung hình,\\nCông chúa Tàu điện lật giở với tốc độ đáng kinh ngạc."
3535 = "Công chúa Tàu điện, bật cười vô cùng thích thú.\\nNhưng ngay sau đó, khóe miệng ngài đã bị chiếc quạt che khuất."
3536 = "Chỉ một khoảnh khắc――Công chúa Tàu điện nín thở."
3537 = "Xua đi nét u buồn thoáng hiện trong đôi mắt,\\nánh nhìn của Công chúa Tàu điện chuyển sang trái."
3538 = "Một cái quạt có vẻ đầy mãn nguyện.\\nĐôi mắt của Công chúa Tàu điện khẽ――nheo lại."
3540 = "Chiếc quạt nhỏ khẽ phe phẩy, mái tóc của Công chúa Tàu điện cũng đung đưa theo."
3584 = "（Póc）"
```

## §6. Chờ Hieu (không tự quyết)

- Key 2679 Seki "ông ngoại": dòng này là dòng Seki thứ 5 (parent đã liệt kê 4 dòng: 共通12 2182, ハチロク05 1178, グランド06 2159, 凪ふかみ02 2299). Căn cứ sửa: "おじいちゃんたち" ở đây là nhóm Seki + anh em (堰さんたち, key 2596 cùng file) — Seki là ông ngoại của Fukami theo quyết định 20/11. Parent kiểm chứng lại giúp: nếu nhóm này không phải Seki thì hoàn lại "ông nội".
- Key 2916–2918 giọng ngọng của Hachiroku: VN hiện diễn rõ nghĩa; TW giữ dạng ngọng (pinyin). Hieu có muốn một bản diễn ngọng bằng tiếng Việt (vd. nói líu lưỡi) hay giữ nguyên bản rõ nghĩa?
- Key 2339 Fukami "chị/em": agent phán người nghe là Olivy (lý do ở §4). Nếu Hieu thấy người nghe là Nagi thì phải sửa thành "Mình sẽ dạy cậu".
- Thuật ngữ: 53 dòng đã sửa trực tiếp trong audit lần này (theo tiền lệ ハチロク10 đã gộp). Khi chạy đợt thống nhất, KHÔNG thêm lại các key này vào hàng đợi: Điện xá 26 key (1588, 1605, 2343, 2451, 2487, 2532, 2561, 2608, 2614, 2759, 2817, 2824, 3161, 3174, 3294, 3451, 3525, 3531–3538, 3540); Ohitoyo 12 key (2382, 2399, 2418, 2490, 2533, 2695, 2739, 2745, 2770, 2814, 3310, 3412); Teitetsu 4 key (2203, 2390, 2490, 2529); Thẻ bảng 4 key (1662, 2444, 2839, 3121); Minh Quốc 2 key (2209, 3410); 凪さま 1 key (2393); thân bảo trì/thân vận hành 2 key (1640, 3135); Lõi Railord 3 key (2173, 2844, 2850).
- Không có câu hỏi thuật ngữ mới, không còn đại từ mơ hồ nào chưa quyết, không có dòng JP dở dang nào cần Hieu hoàn thiện.

## Kết bài

File ハチロク07_延命 đã audit xong toàn bộ 499 dòng: 64 dòng sai (12,8%) — thuật ngữ 53 (Điện xá Công chúa 26, Ohitoyo 12, Teitetsu 4, Thẻ bảng 4, Minh Quốc 2, Bổn tiểu thư 1, thân bảo trì/thân vận hành 2, Lõi Railord 3), đại từ 7 (Soutetsu "tôi"→"anh" với Olivy/Hibiki/Niiroku 3; Hachiroku "tôi"→"em" 3; Fukami "em"→"cậu" với Nagi 1), thân tộc 1 (Seki "ông nội"→"ông ngoại"), gasp sweep 3, SFX 1 (つぽっ "Bóp"→"Póc"). Không lệch dòng, không xoay chuỗi, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 64 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 64/64, 0 bỏ, 2 sửa (3121: khôi phục thẻ %l bị rớt khi viết tay; 3528: khôi phục \n bị rớt). Chờ Hieu: 2679 (Seki thứ 5), 2916–2918 (giọng ngọng), 2339 (xác nhận người nghe là Olivy).
