# Audit — グランドリライト02_ナビ (09_Grand) — 2/435 (0,5%)

File: `グランドリライト02_ナビ.txt.toml` — route 09_Grand, 435 dòng script.
Disk: `sources/toml2/translation_toml/09_Grand/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c802_#U30ca#U30d3.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: Soutetsu mơ gặp Michiko trên tàu (chuyến tàu hướng tới tương lai, ga cuối), rồi về Ohito thăm mộ bố mẹ ruột, trò chuyện dài với Navi về "bản thân trong quá khứ" vs "bản thân hiện tại", cuối cùng gặp Hibiki trên đường về.
Nhân vật: monologue 200, 双鉄 145, ナビ 44, 路子 21, 日々姫 15, ハチロク 7, 真闇 3.

Phương pháp: đọc toàn bộ 435 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3).

## §1. Kết quả

Sai: **2/435 (0,5%)** — cả 2 đều là pronoun (đại từ xưng hô của Soutetsu), không có lỗi nào khác.
Không lệch hàng, không chuỗi xoay, 0 orphan / 0 untranslated / 0 duplicate key.
Sweep っ-gasp: 0 mục cho file này (đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`); trong file cũng không có hàng っ đứng riêng nào bị mất âm — mọi っ cuối từ nhấn mạnh đều đã được diễn (xem §3).
Strong candidates 8 → đọc toàn bộ chỉ tìm ra 2 sai: file này dịch khá sạch; 8 candidates là heuristic (đếm thô), không phải tổng số.

Phân loại (2): pronoun 2 (1867, 1493). Mistranslation 0, gasp 0, sfx 0, terminology 0, tag 0.

## §2. Các lỗi và cách sửa

### 1867 — 双鉄 → Michiko: "tôi" → "anh" (pronoun)

- JP: 「……ならば、僕は。仕事を楽しめているのだな」
- TW: 「那我一定是很享受工作了」
- VN cũ: 「……Nếu vậy, tôi. Chắc hẳn đang rất tận hưởng công việc.」
- Sửa: 「……Nếu vậy, anh. Chắc hẳn đang rất tận hưởng công việc.」

Bằng chứng: cảnh mơ nói chuyện với Michiko (ngay sau 1405 Michiko: "Trông Sou-chan cũng rất vui vẻ!"); mọi câu khác của Soutetsu với Michiko trong cùng cảnh đều dùng "anh" (1729 "Có lẽ anh sẽ đảm nhận…", 1095 "Anh sẽ không bao giờ…", 1661 "Anh hứa.", 1651 "Anh nhất định sẽ đưa em đến.", 1687 "anh muốn chuyến tàu lăn bánh"). Quy tắc đã sửa: Soutetsu là "anh" với Michiko (em gái sinh đôi). "Tôi" ở đây là sót duy nhất trong cảnh.

### 1493 — 双鉄 → nhóm Hachiroku + Hibiki: "anh" → "tôi" (pronoun)

- JP: 「そのときには会って欲しい。紹介させて欲しい。僕の家族に――僕の家族を」
- TW: 「到時候，請讓我介紹你們給我的家人認識——請讓我向你們介紹我的家人」
- VN cũ: 「Khi đó anh muốn hai người đến gặp họ. Hãy để anh giới thiệu.\nVới gia đình anh――gia đình của anh.」
- Sửa: 「Khi đó tôi muốn hai người đến gặp họ. Hãy để tôi giới thiệu.\nVới gia đình tôi――gia đình của tôi.」

Bằng chứng: người nghe là cả hai người — chính VN cũ cũng ghi "hai người"; Hachiroku đáp lại ngay sau đó (1752 「この上なく、光栄なことと存じます」), Hibiki nói ngay trước đó (1859 「わたし！わたしも！！」). Soutetsu là "tôi" với Hachiroku, nên xưng "anh" trước nhóm có Hachiroku là sai. Tiền lệ đã chấp nhận: Paulette 14 key 1544 "anh"→"tôi" cho địa chỉ nhóm. Ba chỗ "anh" trong câu (xưng hô + 2 sở hữu "gia đình anh") đều đổi sang "tôi" cho nhất quán.

## §3. Kiểm tra cơ học và các mục đã xác minh là ĐÚNG (giữ nguyên)

- CSV3: bộ duy nhất, 435 dòng, 0 key trùng, 0 VN trống; thư mục CSV `translation_toml\\09_Grand`.
- TOML: md5 `58d5973b73c2dab6a2ef6bf31feb6b30`, 94.496 byte, BOM + CRLF, [selections] rỗng, không có file trùng md5 (1 bản sao duy nhất).
- TOML ↔ CSV3: 435 khóa script khớp tuyệt đối, 0 khóa thừa/thiếu; VN khớp tuyệt đối 435/435 (kể cả trường hợp TOML gộp `\n` thành khoảng trắng); JP comment 435/435 khớp CSV3.
- %l tag: số lượng tag JP vs VN khớp ở mọi hàng; không có tag VN thiếu dấu `;` đóng trong file này.
- っ: không có hàng っ đứng riêng (gasp) nào; các っ cuối từ nhấn mạnh đều đã diễn: 1527 ひゃっ→"Hya!?", 1553 うおっ→"Uo!?", 1732 えへへっ→"Ehehe", 1591 大歓迎っ→"vô cùng hoan nghênh rồi", 2617 （どくんっ）→（Thịch）, 2576 ひゅっ、ひゅっ→"Phù, phù", 2614 （ふっ――）→（Phù――）, 1782 あうっ→"Auu!?". Không thêm Ư cho っ nhấn mạnh cuối từ — đúng quy tắc.
- Trùng VN ở 2 key: 3 cặp, đều là câu ngắn giống nhau hợp lệ, không phải lệch hàng: 1734/1587 「そうか」→「Vậy sao.」; 1098 「――ああ」/1091 「――うん」→「――Ừ.」; 1535/1538 「うむっ！？」/「うむ！？」→「Hả!?」. JP trùng 2 cặp tương ứng.
- 1073 義父さん/義母さん → "bố nuôi và mẹ nuôi": HỢP LỆ vì TW ghi 養父養母 (theo ngoại lệ đã ghi trong skill — luôn kiểm tra TW trước khi gắn cờ 義).
- Soutetsu "tôi" với Navi (31 dòng) và với Hachiroku (1185, 1881, 1575, 1177) đều đúng; "anh" với Hibiki (1796, 1684, 1551, 1713, 1763, 1745, 1656, 1783, 1699, 1669) và với Michiko (1729, 1095, 1661, 1651, 1687) đều đúng; "con" với bố mẹ ở mộ (1604, 1676, 1097, 1631, 1777, 1691, 1849, 1581, 1675, 1104, 1622, 1574, 1667, 1694) đều đúng; lời độc thoại nội tâm dùng "mình" (2618) đúng ngoại lệ. (Tổng Soutetsu: 37 dòng "tôi" — 31 Navi + 4 Hachiroku + 1 chào chung 1828 + 1 sai 1867; 16 dòng "anh" — 10 Hibiki + 5 Michiko + 1 sai 1493.)
- Navi được Soutetsu gọi "cô" khi đối thoại trực tiếp (1454, 1457, 1570, 1561, 1679, 1900) nhưng "nó" trong lời kể monologue (2370...) — nhất quán trong file, giữ nguyên.
- 1733 路子: câu dở じゃなくて → VN "…không phải là chuyến tàu bỏ lại Michi, mà là..." — giữ đúng dạng bỏ lửng của JP.
- 1610 路子: 「みち、ね？」 → "Michi, anh biết không?" — ね？ diễn thành câu hỏi với người nghe, chấp nhận được.
- 1777: "Michiko rất muốn gặp hai người. Bố và mẹ." — mảnh "Bố và mẹ." soi đúng đuôi 「父さんと母さんに。」 của JP, giữ nguyên.
- 2332: câu thứ hai bỏ lửng ("Thế nhưng, tôi luôn cảm nhận được.") theo đúng JP; TW bỏ luôn câu này, JP thắng.
- 1652: 父さんの実家 → "quê nội", 四國 → "Shikoku" — đúng. 2413: [そごう,1]十川 → "Sogou" theo ruby — đúng.
- 1901/2355/2575…: "Đường sắt Ohito" — xem ghi chú thống nhất bên dưới, không tính sai.

## §4. Lượt soát 2 (đọc lại toàn bộ fix)

Tổng 2 / tái kiểm chứng 2 / loại bỏ 0 / sửa lại 0.
Cả 2 fix đã đọc lại từng giá trị so với JP + dòng kề để xác định người nghe; không fix nào bị loại hay sửa lại trong lượt soát 2.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"1867" = "「……Nếu vậy, anh. Chắc hẳn đang rất tận hưởng công việc.」"
"1493" = "「Khi đó tôi muốn hai người đến gặp họ. Hãy để tôi giới thiệu.\\nVới gia đình tôi――gia đình của tôi.」"
```

Kiểm chứng: khối parse được bằng tomllib, 2 khóa, 0 sai lệch giá trị so với JSON.

## §6. Ghi chú cho Hieu (cần quyết, không tính sai)

1. **Thống nhất "Ohito" → "Ohitoyo"**: 10 chỗ dùng "Ohito" ở 8 key (1684, 2575 ×2, 2213, 2319 ×2, 1901, 1017, 2355, 1713) — dạng cũ của 御一夜, chờ đợt thống nhất toàn dự án (đã quyết thuật ngữ là "Ohitoyo"). Không sửa trong audit này, theo tiền lệ file Hibiki 06 (ghi chú, không tính sai).
2. **Hachiroku tự xưng "Tôi" hay "em" với Soutetsu?** 1195 dùng "em" ("không cần em đi cùng ngài sao ạ?") nhưng 1785 và 1589 dùng "Tôi" ("Tôi, đã nói ra một điều thật vô ý." / "xin hãy cho phép tôi được gửi lời chào."). Cả 2 chỗ "Tôi" đều là ngữ cảnh trang trọng (わたくし — xin lỗi / thỉnh cầu trang trọng), có thể là lựa chọn thanh điệu hợp lệ chứ không phải lỗi. Giữ nguyên, chờ Hieu chốt có chuẩn hoá về "em" hay không.
3. **"thể chế toàn Ohito"** (2355, オール御一夜体制): giữ nguyên cùng ghi chú (1) — sẽ thành "thể chế toàn Ohitoyo" khi thống nhất.

## Kết bài

Đã đọc toàn bộ 435 dòng của グランドリライト02_ナビ, sai 2 dòng (0,5%), cả 2 đều là đại từ xưng hô của Soutetsu: 1867 "tôi"→"anh" với Michiko, 1493 "anh"→"tôi" với nhóm Hachiroku + Hibiki. Không lệch hàng, không chuỗi xoay, không orphan, không untranslated, không trùng key; tag %l sạch; sweep っ không có mục nào cho file này và mọi っ nhấn mạnh đều đã được diễn. Hai fix đã qua lượt soát 2 đầy đủ. Còn chờ Hieu: thống nhất "Ohito"→"Ohitoyo" (10 chỗ) và chuẩn hoá tự xưng của Hachiroku ("Tôi" vs "em", 2 dòng).
