# Audit — ハチロク05_軋み.txt.toml (Hachiroku 05, tiếng kêu cót két)

- File: `translation_toml/01_Hachiroku/ハチロク05_軋み.txt.toml` (đường dẫn đĩa: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af05_#U8ecb#U307f.txt.toml`)
- Route: 01_Hachiroku. 380 dòng script. Nội dung: khiếu nại khói than từ cửa hàng Fumikiriya (nghi là phe thúc đẩy nhà máy Aircra chụp ảnh từ trên không để gây sức ép); lắp thiết bị gom khói 集煙装置 để đối phó; lái tàu trong mưa, rung động bất thường lặp lại ba lần; phát hiện khung gầm 台枠 của 8620 đã cong/xoắn từ vụ tai nạn cũ (vết thương vô hình tích tụ dần); Hachiroku muốn cố chạy thương mại thêm 1–2 năm để kịp ép rút quyết định mời gọi nhà máy; Soutetsu ôm lấy cô bé đang run rẩy, cho cô nghỉ ngơi; Reina và Kon đến cuối file.
- Phương pháp: đọc từng dòng (row-by-row) đối chiếu JP + TW (JP thắng khi khác nhau), kiểm tra chuỗi xoay, nhiễm chéo, dòng mồ côi, trùng khóa, thẻ %l, sweep っ-gasp của file, xưng hô theo quy tắc Soutetsu đã sửa 20/11.

## Kết quả tổng

- Đọc: **380 dòng**, sai: **10 dòng (2,6%)**.
- Phân loại (10): gasp っ 5 (1538, 1900, 1901, 1910, 2410 — tất cả từ sweep, nhận cả 5), thuật ngữ 3 (雨三本 2: 101, 1895; 整備ボディ 1: 2154), xưng hô 1 (1893, Paulette gọi Soutetsu trái B4 lock), sai nghĩa 1 (2434, SFX ぽっぽ).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3: 1 set duy nhất (380 dòng, khớp TOML tuyệt đối sau khi chuẩn hóa `\n` — TOML-2 làm phẳng `\n` thành khoảng trắng ở 232 dòng, đúng như brief đã ghi; 0 chênh lệch ngoài `\n`). `[selections]` rỗng (chỉ có tiêu đề). Không có thẻ `%l` sai định dạng (đếm mở/đóng bằng nhau trong VN; JP/VN bằng nhau về số thẻ mọi dòng).
- TOML md5: `8224aacbc368b1d06c7e8dd22851afcc` (83.098 byte, UTF-8 BOM + CRLF). Không có bản sao file này (không trùng md5 với file nào khác trong toml2; 1 bản duy nhất, không thuộc nhóm trùng).
- Sweep: 5 mục cho file, đã kiểm chứng từng mục vs JP và nhận cả 5 (1538, 1900, 1901, 1910, 2410 — VN hiện tại vẫn bằng đúng old_vn của sweep, tức sweep chưa được áp vào file này). Quét máy bổ sung: không còn ký tự っ thô nào trong VN ngoài 5 dòng đã sửa; không còn ký tự Nhật nào sót lại trong VN.
- Thuật ngữ chờ đợt thống nhất, KHÔNG tính sai: "Ohimitera" 5 dòng (1437, 2235, 2475, 2124, 1761), "Yui" 3 dòng (2726 "sắp đến Yui", 2518 "ga Yui", 1755 "Tuyến Yui" — 湯医線, furigana ゆのい), Seki "Ông nội của Fukami" 1 dòng (1178 — đã có trong danh sách 4 dòng Seki của brief).
- Bằng chứng mới cho quyết định đang chờ (Soutetsu gọi Paulette "cô" vs "em"), KHÔNG tính sai: Soutetsu gọi Paulette "cô" 3 lần (1235, 1519, 1870) vs "em" 0 lần — cộng dồn toàn dự án: "cô" 46 vs "em" 65 (trước file này "cô" 43 vs "em" 65). "Cô ấy" ở 1631 là ngôi ba chỉ Hachiroku, không tính.
- Quirk của CSV3 (không phải lỗi VN): cột TW của 2 dòng 79 và 2131 bị hoán đổi cho nhau — TW của 79 ("加減弁操作不得當…") thực chất là bản dịch của JP 2131, và TW của 2131 ("儘管我自己沒有意識到…") là bản dịch của JP 79. VN của cả hai dòng đều bám đúng JP của chính mình, không sai.
- Quy ước file (mỹ thuật, KHÔNG tính sai — cần Hieu chốt có chuẩn hóa hay không): khoảng 60 dòng độc thoại ở nửa sau file KHÔNG có ngoặc （ ） trong khi ~100 dòng độc thoại khác có (ví dụ 2154, 2355, 2093, 2311, 2139, 2418, 2164, 2257, 2381, 2393, 2534, 2279, 2347, 2345, 2113, 2291, 2573, 2117, 2147, 2663, 2273, 2656, 2081, 2578, 83, 2137, 2507, 2660, 2162, 2473, 2130, 2328, 2149, 2359, 2135, 2206, 2657, 2166, 2111, 2228, 2260, 2385, 2397, 2264, 2343, 2399, 2380, 2476, 2374, 2158, 2654, 2157, 2327, 2445, 2250, 2575, 2208, 2142, 2409). JP gốc cũng không có （ ） ở các dòng này; người dịch đã thêm （ ） một cách không nhất quán. Đây là quy ước trình bày hệ thống trong file, không phải lỗi nội dung — không sửa hàng loạt ở đây.
- Soutetsu sạch thêm (đã kiểm chứng, không sửa): "em" với Hachiroku nhất quán (1793, 1241, 1480, 1824, 1716, 1462, 1475, 1792, 1582); "tôi" với Hachiroku/Mayami/Paulette trong độc thoại và thoại (1631, 1593, 1519-vế đầu, 1235-vế "tôi"); "chị" với Mayami (1214); Hibiki gọi "anh hai" (1813, 1886, 1884). っ cuối từ nội dung không phải gasp, giữ nguyên (1584 「良しっ！」, 1670 「開けるっ！」, 2729 （くそっ）); SFX đã diễn đủ âm, giữ nguyên (2732 （くっ）→"Hự", 2737 （パシャっ）→"Tách", 2733 （ガトっ）→"Cạch!", 2738 （ポーーーっ！）→"Tuúúúú!", 2734/2735 シュッ→"Xịch" nhất quán trong file).

## Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix vs JP)

- Tổng: 10 / kiểm chứng lại: 10 / bỏ: 0 / sửa: 0.
- Khối TOML đã parse-verified (tomllib): 10 khóa, 0 sai lệch giá trị so với JSON. jp/tw/old_vn khớp CSV3 tuyệt đối 10/10. Mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (diff-sanity đã chạy máy: mỗi fix chỉ có 1 fragment thay thế duy nhất).

## Danh sách sửa (10)

### 101 — monologue [thuật ngữ]

- JP: `\x%l雨三本;#00ffc040;雨三本%l;#;、雨降りの日のブレーキは、\nレールの繋ぎ目３つ分、早めにかける必要がある。`
- TW: `\x%l雨三本;#00ffc040;雨三節%l;#;——下雨時需要在比平常提前三節鐵軌的位置剎車。`
- VN cũ: `（\x%l雨三本;#00ffc040;Lễ hội mưa%l;#;, vào những ngày trời mưa,\ncần phải hãm phanh sớm hơn bình thường khoảng 3 nhịp nối đường ray.）`
- Sửa: `（\x%l雨三本;#00ffc040;Phanh ba nhịp%l;#;, vào những ngày trời mưa,\ncần phải hãm phanh sớm hơn bình thường khoảng 3 nhịp nối đường ray.）`
- Lý do: 雨三本 là quy tắc hãm phanh — ngày mưa phải phanh sớm hơn 3 nhịp nối ray (chính câu này giải thích ngay sau đó; TW 雨三節); "Lễ hội mưa" là bịa đặt (三本 ở đây là "ba nhịp", không phải lễ hội). Thuật ngữ này chỉ xuất hiện trong file này toàn dự án (2 dòng: 101, 1895).

### 1538 — 双鉄 [gasp っ]

- JP: `「――っ！　制限60――！」`
- TW: `「呃！限速６０！」`
- VN cũ: `「——っ! Giới hạn 60——!」`
- Sửa: `「——Ư! Giới hạn 60——!」`
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư (tiền lệ: Hachiroku 12 再開発 2103/2537).

### 1893 — ポーレット [xưng hô]

- JP: `「双鉄くん、なんか、心配事ですか？\n元気、無いみたいに見えますけど」`
- TW: `「雙鐵君，你好像沒什麼精神，是不是有什麼心事？」`
- VN cũ: `「Soutetsu, anh đang lo lắng chuyện gì sao?\nTrông anh có vẻ không được khỏe.」`
- Sửa: `「Anh Soutetsu đang lo lắng chuyện gì sao?\nTrông anh có vẻ không được khỏe.」`
- Lý do: Paulette gọi 双鉄くん (cách gọi trực tiếp) → "anh Soutetsu" theo B4 lock. VN cũ để tên trần "Soutetsu" ở vị trí gọi tên, chỉ giữ "anh" làm đại từ ở vế sau. Toàn dự án "anh Soutetsu" 361 lần vs tên trần 35 lần; tiền lệ cùng lỗi: Paulette gọi "cậu Soutetsu" trái B4 đã sửa ở ハチロク05_レイルロオドたち (2929, 3078, 2709, 2715).

### 1895 — ハチロク [thuật ngữ]

- JP: `「双鉄様！　\x%l雨三本;#00ffc040;[あめさんぼん,2]雨三本%l;#;ですっ！」`
- TW: `「雙鐵少爺！\x%l雨三本;#00ffc040;雨三節%l;#;！」`
- VN cũ: `「Ngài Soutetsu! \x%l雨三本;#00ffc040;Lễ hội mưa%l;#; ạ!」`
- Sửa: `「Ngài Soutetsu! \x%l雨三本;#00ffc040;Phanh ba nhịp%l;#; ạ!」`
- Lý do: Như 101 — 雨三本 là thuật ngữ quy tắc phanh, không phải "lễ hội". Hachiroku đang hét lên cảnh báo thuật ngữ kỹ thuật; gloss và cả phần hiển thị đều phải sửa (xem 101 để biết định nghĩa đầy đủ).

### 1900 — 日々姫 [gasp っ]

- JP: `「っ！」`
- TW: `「！」`
- VN cũ: `「っ!」`
- Sửa: `「Ư!」`
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư.

### 1901 — 双鉄 [gasp っ]

- JP: `「っ！？」`
- TW: `「！？」`
- VN cũ: `「っ!?」`
- Sửa: `「Ư!?」`
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ thô còn sót trong VN, diễn thành Ư.

### 1910 — 日々姫 [gasp っ]

- JP: `『「っ！？」\n「っ！？」』`
- TW: `『「！？」\n「！？」』`
- VN cũ: `『「っ!?」\n「っ!?」』`
- Sửa: `『「Ư!?」\n「Ư!?」』`
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: cả hai っ thô còn sót trong VN, diễn thành Ư.

### 2154 — monologue [thuật ngữ]

- JP: `整備ボディのハチロクは、\nその中にもぐって、\x%l8620;#00ffc040;8620%l;#;の下腹を見上げている。`
- TW: `八六換上了整備體，鑽入其中。她正在檢查\x%l8620;#00ffc040;８６２０%l;#;的底部。`
- VN cũ: `Hachiroku trong hình dáng thân chính đã chui vào bên trong,\nvà đang ngước nhìn phần gầm của \x%l8620;#00ffc040;8620%l;#;.`
- Sửa: `Hachiroku trong hình dáng thân bảo trì đã chui vào bên trong,\nvà đang ngước nhìn phần gầm của \x%l8620;#00ffc040;8620%l;#;.`
- Lý do: 整備ボディ = thân bảo trì (cặp thuật ngữ đã chốt: 整備体/整備ボディ → "thân bảo trì", 運転ボディ → "thân vận hành"); "thân chính" bỏ mất nghĩa "bảo trì" của 整備. Đây là lần duy nhất 整備ボディ/運転ボディ xuất hiện trong file. (Dòng này cũng thuộc nhóm độc thoại không có （ ） — xem mục "Quy ước file" ở trên, không sửa ngoặc ở đây.)

### 2410 — monologue [gasp っ]

- JP: `機関庫の端につんであるファイルを抜き取って、\n改修直後の\x%l8620;#00ffc040;8620%l;#;の写真と、比較する――――っ！`
- TW: `接著，我從堆放在牆邊的文件夾中抽出一張\x%l8620;#00ffc040;８６２０%l;#;剛完成修復時的照片，把兩者作對比……！`
- VN cũ: `Tôi rút một tập hồ sơ xếp ở góc xưởng đầu máy ra,\nvà so sánh với bức ảnh của \x%l8620;#00ffc040;8620%l;#; ngay sau khi cải tạo――――っ!`
- Sửa: `Tôi rút một tập hồ sơ xếp ở góc xưởng đầu máy ra,\nvà so sánh với bức ảnh của \x%l8620;#00ffc040;8620%l;#; ngay sau khi cải tạo――――Ư!`
- Lý do: Sweep raw-tsu đã kiểm chứng vs JP: っ cuối câu (――――っ！) còn sót trong VN, diễn thành Ư theo quy tắc gasp (âm っ sẽ mất hẳn nếu không diễn).

### 2434 — monologue [sai nghĩa]

- JP: `日々姫がロッドを引き込めば、\x%lドラフト;#00ffc040;ドラフト%l;#;音――\n煙を吐き出すぽっぽという音がいくらかこもる。`
- TW: `日日姬拉動了操縱杆，\x%lドラフト;#00ffc040;鍋爐排汽%l;#;聲——煙噴出的“噗噗”聲變得有些沉悶。`
- VN cũ: `（Khi Hibiki kéo cần gạt, tiếng \x%lドラフト;#00ffc040;hút gió lò hơi%l;#;——\ntiếng "phịch phịch" nhả khói nghe có vẻ nghèn nghẹt đi đôi chút.）`
- Sửa: `（Khi Hibiki kéo cần gạt, tiếng \x%lドラフト;#00ffc040;hút gió lò hơi%l;#;——\ntiếng "phụt phụt" nhả khói nghe có vẻ nghèn nghẹt đi đôi chút.）`
- Lý do: ぽっぽ là tiếng phụt hơi nhẹ của đầu máy (TW 噗噗); "phịch phịch" là tiếng nện nặng, sai âm sắc. "Phụt phụt" diễn đúng tiếng hơi phụt ra.

## Khối TOML (đã parse-verified: 10 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
"101" = "（\\x%l雨三本;#00ffc040;Phanh ba nhịp%l;#;, vào những ngày trời mưa,\\ncần phải hãm phanh sớm hơn bình thường khoảng 3 nhịp nối đường ray.）"
"1538" = "「——Ư! Giới hạn 60——!」"
"1893" = "「Anh Soutetsu đang lo lắng chuyện gì sao?\\nTrông anh có vẻ không được khỏe.」"
"1895" = "「Ngài Soutetsu! \\x%l雨三本;#00ffc040;Phanh ba nhịp%l;#; ạ!」"
"1900" = "「Ư!」"
"1901" = "「Ư!?」"
"1910" = "『「Ư!?」\\n「Ư!?」』"
"2154" = "Hachiroku trong hình dáng thân bảo trì đã chui vào bên trong,\\nvà đang ngước nhìn phần gầm của \\x%l8620;#00ffc040;8620%l;#;."
"2410" = "Tôi rút một tập hồ sơ xếp ở góc xưởng đầu máy ra,\\nvà so sánh với bức ảnh của \\x%l8620;#00ffc040;8620%l;#; ngay sau khi cải tạo――――Ư!"
"2434" = "（Khi Hibiki kéo cần gạt, tiếng \\x%lドラフト;#00ffc040;hút gió lò hơi%l;#;——\\ntiếng \"phụt phụt\" nhả khói nghe có vẻ nghèn nghẹt đi đôi chút.）"
```

## Kết bài

File ハチロク05_軋み.txt.toml: 380 dòng đã đọc hết, sai 10 dòng (2,6%). Lỗi tập trung ở 2 cụm: gasp っ thô còn sót (5, tất cả từ sweep — file này sweep chưa được áp) và thuật ngữ bịa đặt/nhầm (3 — "Lễ hội mưa" cho 雨三本 ở 2 dòng, "thân chính" cho 整備ボディ ở 1 dòng), cộng 1 lỗi xưng hô trái B4 lock (1893) và 1 lỗi SFX (2434). Không có lệch dòng, chuỗi xoay hay nhiễm chéo — bản dịch file này nhìn chung trung thực, lỗi là rời rạc chứ không hệ thống. Cần Hieu xem 3 điểm đã nêu trên trước khi gộp: (1) quy ước （ ） không nhất quán ở ~60 dòng độc thoại — có chuẩn hóa trong đợt thống nhất hay giữ nguyên? (2) quyết định đang chờ "cô" vs "em" cho Soutetsu gọi Paulette — file này thêm 3 "cô" (1235, 1519, 1870), cộng dồn "cô" 46 vs "em" 65; (3) các thuật ngữ chờ thống nhất: "Ohimitera" 5 dòng, "Yui" 3 dòng, Seki "Ông nội" 1 dòng (1178).
