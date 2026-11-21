# Audit REVIEW — 仲国03_北琴鉄道歴史館.txt.toml (10_Chikuni)

- **File:** `10_Chikuni/仲国03_北琴鉄道歴史館.txt.toml` — route 仲国 (Chikuni), bảo tàng lịch sử đường sắt Bắc Cầm (Beiqin). Nhân vật: Soutetsu, Hibiki, Hachiroku, Suika, Zhihuan, cô Jiang.
- **Hàng đã đọc:** 377/377 (toàn bộ `[script]`, đọc từng dòng đối chiếu JP + TW từ CSV3).
- **Sai:** **7 dòng / 377 (1,86%)** — file sạch nhất nhóm 仲国 từ trước tới nay; không có lệch dòng, không có dòng mồ côi, không có dòng chưa dịch.
- **Cơ sở tổng:** 185 file / 8.837 dòng sai (đã kiểm chứng trực tiếp trong ROUTE-AUDIT.md — khớp với cơ sở được giao).
- **TOML:** md5 `fdb400234a3df4f0f55a35451f6eef20`; UTF-8 BOM + CRLF; không trùng lặp với file TOML nào khác (không thuộc 11 nhóm duplicate). `[selections]` rỗng. 377 khóa script = 377 dòng CSV3, khớp 1–1.
- **CSV3:** 1 bộ duy nhất cho file này (không có dual-set), 0 khóa trùng, 0 ô VN trống. TOML khớp CSV3 tuyệt đối sau khi trừ flatten `\n`→khoảng trắng đã biết của TOML-2 (264 dòng chỉ khác ở đó, đã kiểm chứng 0 khác biệt ngoài flatten).

## Phân loại sai (7)

| Loại | Số dòng | Keys |
|---|---|---|
| gasp (っ bị mất, theo sweep) | 3 | 1945, 1963, 2845 |
| tag %l | 3 | 2084 (thiếu `;` đóng), 2132 + 2145 (thêm tag JP không có) |
| content-loss (dịch thiếu) | 1 | 2911 |

## Kiểm tra cấu trúc

- **Lệch dòng / rotation:** 0. JP và VN đi song song suốt file; TW đồng thuận với JP ở mọi dòng đã đọc. Không có cặp lệch (đúng bản dịch nằm sai key).
- **Ô nhiễm chéo (contamination):** 0. Không dòng nào mang nội dung của file khác.
- **Dòng mồ côi (orphan):** 0. Mọi VN đều khớp một JP trong file.
- **Chưa dịch:** 0 ô trống. (Lưu ý: 2911 chỉ còn lại mỗi tên người — tính là content-loss, không phải ô trống.)
- **Khóa trùng:** 0 trong CSV3 và trong TOML.
- **Sweep っ-gasp:** đã tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có 4 mục: 1945, 1963, 2845 (lost-gasp, áp dụng cả 3, đã kiểm chứng từng giá trị với JP) và 1984 (already-rendered, `「っ！！？」`→`「Hả!!?」`, giữ nguyên). Quét bổ sung toàn file cho mọi っ còn lại: các っ giữa từ (びっくり, ふっかふか, すごかった…), っ nhấn mạnh sau từ nội dung (そこっ 1993, うむっ 2003, おおっ 1960) và tiếng cười (うふふっ 2016) đều đã được diễn đúng, không thêm Ư.
- **Tag %l:** quét toàn file — chỉ 2 tag VN sai cú pháp (2084, 2145: thiếu `;` đóng, dạng `%l;#.`) và 2 tag VN thêm mới mà JP không có (2132, 2145). Các tag còn lại khớp JP tuyệt đối (term + gloss).

## Chi tiết từng dòng sai

### 1. Key 1945 — gasp (sweep lost-gasp-whole) — 西瓜
- JP: `「はいっ！！」\n「っ！！！」`
- TW: `「呃！！！」\n「是的！！」`
- Old VN: `「Vâng!!」\n「!!!」`
- Fix: `「Vâng!!」\n「Ư!!!」`
- Lý do: dòng 2 là gasp nguyên dòng (っ + !!!), VN chỉ còn dấu câu. Thêm Ư theo sweep (đã kiểm chứng JP). Thứ tự dòng theo JP (TW đảo 2 dòng, JP thắng).

### 2. Key 1963 — gasp (sweep lost-gasp-trailing) — 日々姫
- JP: `「はぁ～っ」`
- TW: `「唉～」`
- Old VN: `「Haa~」`
- Fix: `「Haa~Ư」`
- Lý do: thở dài kéo dài + っ cắt ngang ở cuối; VN giữ dấu ~ nhưng mất hẳn tiếng gasp. Thêm Ư sau ~ theo sweep.

### 3. Key 2084 — tag %l thiếu `;` đóng — 西瓜
- JP: `「老師ご自身が次期主力として一番に望んだ構想もまた、\n全線電化と\x%l電車;#00ffc040;電車%l;#;形式での高速・大量輸送だったそうです」`
- TW: `「師父本人最看好的下一代主力車型方案，好像也是基於全面電力化的高速大運量\x%l電車;#00ffc040;電車%l;#;」`
- Old VN: `「Ý tưởng mà bản thân Sư phụ mong muốn nhất cho thế hệ chủ lực tiếp theo,\nnghe nói cũng là điện khí hóa toàn tuyến và vận chuyển tốc độ cao, khối lượng lớn bằng hình thức \x%l電車;#00ffc040;tàu điện%l;#.」`
- Fix: `「Ý tưởng mà bản thân Sư phụ mong muốn nhất cho thế hệ chủ lực tiếp theo,\nnghe nói cũng là điện khí hóa toàn tuyến và vận chuyển tốc độ cao, khối lượng lớn bằng hình thức \x%l電車;#00ffc040;tàu điện%l;#;.」`
- Lý do: tag đóng thiếu `;` (`%l;#.`) — chỉ thêm đúng 1 ký tự `;`. Tag này JP có, giữ nguyên tag.

### 4. Key 2132 — tag %l thêm mới, term sai — ハチロク
- JP: `「はじめての、仲国の列車。Z49列車。\n[こうがしゃ,2]硬臥車……三段寝台をお手配いただけたのですね」`
- TW: `「我們即將初次乘坐的仲國的列車，Ｚ４９次列車，硬臥車……應我們的要求安排了三層床鋪車廂的車票啊」`
- Old VN: `「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\n\x%lこうがしゃ;#00ffc040;Toa giường cứng%l;#;…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」`
- Fix: `「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」`
- Lý do: JP chỉ có ruby `[こうがしゃ,2]` trên 硬臥車, KHÔNG có tag %l — VN tự thêm tag (mẫu fabrication của Gemini). Term của tag lại là cách đọc こうがしゃ chứ không phải từ 硬臥車. Bỏ tag, giữ nguyên văn "Toa giường cứng".

### 5. Key 2145 — tag %l thêm mới + thiếu `;` đóng — ハチロク
- JP: `「ですので、狭軌やむなしの日ノ本における鉄道発展の\n最適解は……動力分散方式――電車方式での、発展」`
- TW: `「所以基於無奈選擇了窄軌的日本國鐵路若要進一步發展，那麼選擇動力分散為特點的電車，便是最佳方案了」`
- Old VN: `「Do đó, giải pháp tối ưu cho sự phát triển đường sắt ở Hinomoto, nơi không thể tránh khỏi việc sử dụng khổ hẹp là……\nPhát triển theo phương thức phân tán động lực——phương thức \x%l電車;#00ffc040;tàu điện%l;#.」`
- Fix: `「Do đó, giải pháp tối ưu cho sự phát triển đường sắt ở Hinomoto, nơi không thể tránh khỏi việc sử dụng khổ hẹp là……\nPhát triển theo phương thức phân tán động lực——phương thức tàu điện.」`
- Lý do: JP dùng 電車 trơn, không có tag %l — VN tự thêm tag (lại thêm thiếu `;` đóng). Bỏ tag, giữ nguyên văn "tàu điện." Các dòng 電車 khác trong file giữ tag vì JP có tag ở đó; dòng này theo đúng JP.

### 6. Key 2845 — gasp (sweep lost-gasp-trailing) — monologue
- JP: `おっと、電話か。\n姜さんは早口の仲国語でなにやら――っ！`
- TW: `真不巧，正趕上有電話進來。姜小姐以很快的語速用仲文和對方交流著。`
- Old VN: `Ôi chà, có điện thoại.\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——!`
- Fix: `Ôi chà, có điện thoại.\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——Ư!`
- Lý do: gasp cuối dòng sau ——, VN giữ dấu gạch nhưng mất tiếng gasp. Thêm Ư theo sweep.

### 7. Key 2911 — content-loss (dịch thiếu gần như toàn bộ câu) — monologue
- JP: `ハチロクの、8620形蒸気機関車の――いや、\n日ノ本の近代鉄道の父ともいえる、[しば]芝[こうじろう,2]高次郎技官。`
- TW: `說到八六，８６２０的父親島安次郎技官——不，將其稱作日本國近代鐵路之父也不為過。`
- Old VN: `kỹ sư Shiba Kojiro.`
- Fix: `Kỹ sư Shiba Kojiro — người đứng sau đầu máy hơi nước dòng 8620 của Hachiroku — không, có thể nói ông chính là cha đẻ của đường sắt hiện đại Hinomoto.`
- Lý do: VN cũ chỉ còn mỗi tên người, mất toàn bộ khung câu (người đứng sau đầu máy 8620 của Hachiroku — không, cha đẻ đường sắt hiện đại Hinomoto). Dịch lại đầy đủ từ JP. Tên giữ theo JP là 芝高次郎 (Shiba Kojiro); TW "sửa" thành 島安次郎 (tên thật ngoài đời) — JP thắng TW nên không đổi tên. Dòng này cũng là dòng duy nhất heuristic độ dài bắt được (VN 19 ký tự / JP 60 ký tự).

## Các dòng đã xem xét kỹ nhưng GIỮ NGUYÊN (không tính sai)

- **1952 `はうっ！`→`「Oa!」` và 1976 `ああっ！`→`「A!」`:** っ gắn sau tiếng cảm thán, nhưng dấu `!` đã diễn được cú cắt ngang — cùng tiền lệ `あっ――→"A——"` (không Ư kép). Sweep cũng không gắn cờ 2 dòng này. Giữ nguyên.
- **1984 `「っ！！？」`→`「Hả!!?」`:** sweep xếp already-rendered, giữ nguyên.
- **1993 `そこっ！`→`「Là chỗ đó đấy!」`:** っ nhấn mạnh sau từ nội dung (そこ), theo luật KHÔNG phải gasp, không thêm Ư.
- **2618 `ほうっ、とため息。`→`Phù, một tiếng thở dài.`:** tiếng thở dài đã diễn bằng "Phù", không mất âm.
- **1540 gloss 従輪 `Bánh chịu tải không động lực`:** dài, không đối xứng với 先輪 `Bánh dẫn hướng trước`, nhưng nội dung đúng (bánh không động lực chịu tải) — lựa chọn gloss, không tính sai. Ghi nhận để đợt thống nhất cân nhắc.
- **2709 `『Quốc Hệ Hiệu』` vs các chỗ khác `Quốc Hệ hiệu`:** khác hoa/thường ở chữ "Hiệu" trong tên khắc trên vương miện — khác biệt mỹ thuật, không tính sai.

## Đại từ Soutetsu — đã kiểm tra từng dòng, KHÔNG sửa, gắn cờ mơ hồ

Toàn file Soutetsu xưng "anh" với Hibiki (1602, 1877, 1884, 1886, 1908, 1927, 1989, 2061, 2125, 2134) và "tôi" với Hachiroku/Jiang/Zhihuan (2038, 2045, 2278, 2315) — đều đúng theo luật đã sửa. Các dòng sau ở cảnh nhóm, người nghe trực tiếp không rõ ràng, nên GIỮ NGUYÊN và gắn cờ (không quyết thay Hieu):
- **1958 `tôi`:** "Đến Pashina thì ngay cả tôi cũng từng nghe qua." — phản ứng trước nhận xét của Hibiki (1956) nhưng Hachiroku chen "え？" ngay trước (1957). Có thể "anh".
- **2001 `tôi`:** "thì tôi đoán khổ đường ray này là 1435mm" — đang giải thích cho cả Hibiki + Hachiroku (Hibiki hỏi 1992–1996, đáp 2005). Có thể "anh".
- **1602 `anh`:** "Cảm ơn hai người đã chỉ ra và dạy cho anh biết…" — nói với cả Hachiroku + Hibiki ("hai người"). Có thể "tôi".
- **2310 `anh`:** "anh hoàn toàn không biết mình đã làm hỏng chuyện gì" — cả hai cô đang trách; Hibiki là người trách chính. Có thể "tôi".
- **2379 `anh`:** "anh cảm thấy cô bé có vẻ rất vui" — trả lời trực tiếp câu hỏi của Hachiroku (2378), nhưng Hibiki đang tham gia cùng đoạn hội thoại (2376). Có thể "tôi".
- **2133 `bọn anh`:** "Lúc của bọn anh sao." — GIỮ theo tiền lệ Grand 03 2201 (僕ら số nhiều, đúng mọi cách đọc), không gắn cờ.

## Cờ cho đợt thống nhất (KHÔNG tính vào 7 dòng sai — theo lệ các audit gần nhất, thuật ngữ toàn dự án để đợt thống nhất xử lý một lần)

- **帝鉄 → `Đường sắt Hoàng gia` (13 dòng):** 1585, 1867, 1872, 1992, 2027, 2029, 2081, 2082, 2083, 2190, 2251, 2301, 2860 → `Teitetsu` theo luật đã chốt.
- **冥国 → `Meikoku` (2 dòng):** 2304, 2430 → `Minh Quốc` theo luật đã chốt. Lưu ý: toàn corpus đang lẫn lộn (14 `Minh Quốc` vs 25 `Meikoku` ở 11 file) — đợt thống nhất nên quét toàn dự án, không chỉ 2 dòng này.
- **湯医線 → `Tuyến Yui` (1 dòng):** 2389 → `Yunoi` theo luật đã chốt. Đây là dòng "Yui" thứ 3 ngoài 2 dòng đã có trong danh sách thống nhất (P14 83, P16 2032) — bổ sung vào danh sách.

## Cờ hỏi Hieu (không quyết)

- **2082 + 2248 — `Đường sắt Đế hữu Hinomoto` cho 日ノ本帝有鉄道:** "Đế hữu" là calque từng chữ của 帝有 (đường sắt thuộc Hoàng đế), nghe gượng trong tiếng Việt nhưng dùng nhất quán cả 2 lần và là danh từ riêng trong truyện. Hỏi Hieu có muốn đổi thành "Đường sắt Hoàng gia Hinomoto" / "Đường sắt thuộc Hoàng đế Hinomoto" hay giữ nguyên.
- **1948 + 2347 — Zhihuan gọi người đối thoại là `chị`:** JP không có từ xưng hô; VN thêm "chị" ("Mắt chị tinh quá", "chị muốn hỏi gì cũng được"). Người nghe có lẽ là Hibiki. Giữ nguyên vì không có bằng chứng sai, nhưng nếu Hieu biết rõ tuổi tương đối Zhihuan–Hibiki thì xác nhận giúp.
- **Các dòng đại từ mơ hồ ở mục trên (1958, 2001, 1602, 2310, 2379).**

## Khối TOML (đã kiểm chứng parse)

Khối dưới đã parse bằng tomllib: 7 khóa, 0 sai lệch giá trị so với JSON. Lưu ý: `\\n` trong khối là literal backslash-n (khớp CSV3/TOML-2), KHÔNG phải newline thật.

```toml
[script]
1945 = "「Vâng!!」\\n「Ư!!!」"
1963 = "「Haa~Ư」"
2084 = "「Ý tưởng mà bản thân Sư phụ mong muốn nhất cho thế hệ chủ lực tiếp theo,\\nnghe nói cũng là điện khí hóa toàn tuyến và vận chuyển tốc độ cao, khối lượng lớn bằng hình thức \\x%l電車;#00ffc040;tàu điện%l;#;.」"
2132 = "「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」"
2145 = "「Do đó, giải pháp tối ưu cho sự phát triển đường sắt ở Hinomoto, nơi không thể tránh khỏi việc sử dụng khổ hẹp là……\\nPhát triển theo phương thức phân tán động lực——phương thức tàu điện.」"
2845 = "Ôi chà, có điện thoại.\\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——Ư!"
2911 = "Kỹ sư Shiba Kojiro — người đứng sau đầu máy hơi nước dòng 8620 của Hachiroku — không, có thể nói ông chính là cha đẻ của đường sắt hiện đại Hinomoto."
```

## Second pass (đọc lại toàn bộ 7 fix đối chiếu JP)

- **Tổng / kiểm chứng lại / gỡ bỏ / sửa:** 7 / 7 / 0 / 0.
- Đã đọc lại từng fix với JP gốc: 1945 (gasp nguyên dòng ✓), 1963 (っ cuối sau ~ ✓), 2084 (chỉ thêm `;` ✓), 2132 (bỏ tag, giữ "Toa giường cứng" ✓), 2145 (bỏ tag, giữ "tàu điện." ✓), 2845 (Ư sau —— ✓), 2911 (đủ 4 thành tố: 8620 của Hachiroku / —không— / cha đẻ đường sắt hiện đại / Shiba Kojiro theo JP ✓).
- Diff cơ học fix-vs-old VN: mỗi fix chỉ khác old VN đúng chỗ cần sửa (1 ký tự chèn cho 1945/1963/2084/2845; xóa đúng phần tag cho 2132/2145; viết lại 2911).

## Kết bài

File 仲国03_北琴鉄道歴史館.txt.toml: 377 dòng đã đọc, 7 dòng sai (1,86%) — gasp 3, tag %l 3, dịch thiếu 1 (2911 là lỗi nặng nhất: cả câu chỉ còn lại tên người). Không lệch dòng, không ô nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không khóa trùng. Ba mục sweep đã áp dụng đúng; 2 tag %l sai cú pháp đã sửa; 2 tag thêm mới đã gỡ. Cờ cho đợt thống nhất: 帝鉄 ×13, 冥国 "Meikoku" ×2, "Tuyến Yui" ×1 (dòng thứ 3). Cờ hỏi Hieu: "Đường sắt Đế hữu Hinomoto" (2082/2248), "chị" của Zhihuan (1948/2347), 5 dòng đại từ Soutetsu mơ hồ trong cảnh nhóm. B19 vẫn park.
