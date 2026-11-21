# Audit — 日々姫13_討論会 (02_Hibiki) — 15/410 sai (3,7%)

File: `02_Hibiki/日々姫13_討論会.txt.toml` — cuộc tranh luận bầu cử thị trưởng: Hibiki diễn thuyết mở màn, Kisaki đáp trả bằng số liệu nhà máy Aircra, Hibiki phản công bằng ảnh chụp + mô hình nhà máy, kết thúc hòa giải bằng sổ phác thảo nụ cười.
Nguồn: CSV3 1 set duy nhất, 410 dòng, 0 key trùng, 0 dòng VN trống. TOML 410 khóa `[script]`, md5 `fbe719d7482b3c65b3d4ac66c7272017`, 1 bản duy nhất (không có file trùng). `[selections]` rỗng, `[characters]`/`[character_subs]` không có "Densha Hime" hay thuật ngữ lạ. Đọc đủ 410/410 dòng đối chiếu JP + TW.

## 1. Tổng quan
- **15/410 sai (3,7%)** — file sạch, lỗi rải rác, không có cụm lỗi hệ thống.
- Phân loại: đại từ 3 (1330, 1530, 2515) + gasp 3 (1304, 1703, 2251 — cả 3 đều là sweep) + "Ạ." đứng một mình 5 (998, 1326, 1358, 1527, 1601) + thêm nghĩa 1 (1334) + SFX 2 (1955, 2344) + dịch sai 1 (2269).
- **0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng mồ côi, 0 dòng chưa dịch, 0 key trùng.** VN trùng lặp: 2 cặp câu ngắn lặp hợp lệ (JP giống hệt nhau: 「Hả!?」 1307/1704 — JP khác nhau えっ！？/っ！？ nhưng cùng một tiếng ngạc nhiên, không phải tràn; 「Đó là――」 1641/1646 — JP đều それは――).
- Tag %l: JP = VN mọi dòng trừ 1512 (VN thêm gloss `Tori-tetsu` cho 撮り鉄 — JP có ruby [と]撮り[テツ]鉄, gloss giải thích thuật ngữ chuyên ngành là hợp lý, GIỮ). 0 thẻ thiếu `;`, 0 thẻ chưa đóng, 0 chữ っ thô còn sót trong VN.

## 2. Các lỗi đã sửa (15)

### Đại từ (3)
- **1330** (日々姫 → Soutetsu): JP 「うん。今なら抜けても気づかれないって思ったし――」 — VN cũ "Chị nghĩ…" → **"Em nghĩ…"**. Hibiki nói với anh trai (1311 "Anh trai. Cảm ơn anh."); mọi dòng khác của Hibiki trong file đều tự xưng "em" (953, 1018, 1431, 1440).
- **1530** (双鉄 → Hachiroku): JP 「無論だ。近くに着水させよう」 — VN cũ "Anh sẽ cho nó hạ cánh…" → **"Tôi sẽ cho nó hạ cánh…"**. Người nghe là Hachiroku (cô ấy hỏi ở 1690); quy tắc đã chốt: Soutetsu "tôi" với Hachiroku.
- **2515** (monologue Soutetsu): JP 「（さて、僕も動かねば）」 — VN cũ "mình cũng phải hành động" → **"tôi cũng phải hành động"**. Đây là câu khẳng định quyết tâm, không phải tự vấn cảm xúc nên quy tắc chung "tôi" áp dụng (ngoại lệ "mình" chỉ cho tự vấn nội tâm cảm xúc); các độc thoại lân cận trong file đều "tôi" (1853, 1967, 2046, 2188).

### Gasp っ (3 — cả 3 đều từ sweep, đã kiểm chứng từng cái với JP)
- **1304** (れいな): JP 「ふわわわわぁ～っ」 — "Oa a a a a~" → **"Oa a a a a~Ư"** (sweep lost-gasp-trailing; 6 mora JP = 6 âm VN).
- **1703** (双鉄): JP 「っ！」 — "!" → **"Ư!"** (sweep lost-gasp-whole).
- **2251** (monologue): JP 「そしてさらさら何かを――っ！！」 — "――!!" → **"――Ư!!"** (sweep lost-gasp-trailing).
- Sweep 1704 (「っ！？」→ "Hả!?") đã ghi "already-rendered" — kiểm chứng đúng, KHÔNG sửa. Quét cơ học toàn file không phát hiện thêm gasp nào bị mất ngoài 3 dòng trên.

### "Ạ." đứng một mình — です cuối câu bị dịch thành câu riêng (5)
Mẫu lỗi hệ thống của Gemini trong file này: です cuối câu được dịch thành một câu "Ạ." độc lập — trong tiếng Việt hạt "ạ" không thể đứng một mình thành câu. Sửa bằng cách gộp vào cuối câu chính:
- **998** (ふかみ): "…đang gật đầu. Ạ." → bỏ "Ạ."
- **1326** (ふかみ): "Mình cũng. Nghĩ là như vậy. Ạ." → **"Mình cũng nghĩ là như vậy ạ."**
- **1358** (ふかみ): "…vậy mà. Ạ." → bỏ "Ạ."
- **1527** (ふかみ): 2× "Ạ." (2× です) → **"Em sẽ gọi điện thoại ạ. … Em sẽ mượn danh sách từ mẹ, rồi nhờ họ thử xem ạ."** (đồng thời bỏ dấu phẩy thừa sau "Em sẽ")
- **1601** (ふかみ): "…biến mất hết. Ạ." → bỏ "Ạ."

### Thêm nghĩa (1)
- **1334** (ポーレット): JP 「うん！」 chỉ là đồng tình — "Tuyệt quá!" → **"Ừ!"**.

### SFX (2)
- **1955** (monologue): JP ゥィン―― là tiếng mô-tơ rít "ween" (TW 嗡——) — "O o――" → **"Uyn――"**.
- **2344** (monologue): JP 「ふっと、稀咲が笑顔を浮かべる」 — ふっと là phó từ "bỗng nhiên" (TW 忽然), không phải hiệu ứng âm thanh — "Phụt, Kisaki nở một nụ cười." → **"Bỗng nhiên, Kisaki nở một nụ cười."**

### Dịch sai (1)
- **2269** (monologue): JP 「笑顔にあふれた御一夜」 = tràn ngập nụ cười — "tràn ngập tiếng cười" → **"tràn ngập nụ cười"** ("tiếng cười" là âm thanh cười, khác 笑顔; cùng dòng đã dịch 笑顔→"nụ cười" 3 lần trước đó). "Ohimitera" GIỮ — đợt thống nhất.

## 3. Giữ nguyên (đã kiểm tra, không sai)
- Kisaki gọi Hibiki là "cô" 3 dòng tranh luận trang trọng (1250, 1366, 1243): JP không có từ xưng hô, "cô" là cách xưng trang trọng trong bối cảnh tranh luận chính thức, nhất quán trong cảnh — GIỮ (ghi chú, không tính lỗi).
- Hibiki gọi Kisaki là "Cô" ở 1508 ("Cô chưa từng hát bài đó sao?") và "Tiền bối Kisaki" ở 1499: "cô" là cách xưng lịch sự với tiền bối nữ, JP không có từ xưng hô — GIỮ.
- 1315 「う、うんっ！」→ "Ư, ừm!": っ cuối đã được diễn bằng "m" chặn + "!" (tiền lệ ハチロク01 2319) — KHÔNG thêm Ư.
- 1320 「ゎうっ！？ すまんばいっ」→ "Oái!? Xin lỗi nha.": っ cuối gắn với từ nội dung (nhấn mạnh), không phải gasp — KHÔNG thêm Ư.
- 2518 （パシャ、パシャ、パシャ、パシャっ！）→ "(Tách, tách, tách, tách!)": âm shutter đã sắc sẵn trong "tách!" — KHÔNG thêm Ư.
- 1208: JP "二年目" thắng TW "一年" (JP beats TW) — VN "vào năm thứ hai" đúng.
- 2088 義父 → "cha nuôi": đúng theo quyết định 義 (TW 義父, gia đình Migita là con nuôi).
- 1488 日ノ本 → "Hinomoto" đã đúng; 0 dòng "Hinamoto".
- Sông theo ruby (không theo kanji): Shimanto (1013/1015), Kitakami (1458), Kiso/Ibi/Chikugo (1506) — đúng.
- 1512 gloss `Tori-tetsu` thêm cho 撮り鉄 — GIỮ (mục §1).
- 2269/1964/60/947/945/1395/1234/1669 "Ohimitera" ×19, "Đường sắt Ohito" ×1 (1347), "tuyến Yui" ×1 (1964), "ga Yui" ×1 (60) — KHÔNG sửa trong audit, vào đợt thống nhất theo quyết định đã chốt (Ohitoyo / Đường sắt Ohitoyo / Yunoi).

## 4. Kiểm chứng
- JSON 15 mục (key chuỗi, list-of-dicts), khối TOML 15 khóa, 0 sai lệch giá trị (tomllib parse).
- jp/tw/old_vn khớp CSV3 tuyệt đối 15/15 (1 set duy nhất, 410 dòng).
- Đại từ ĐÃ KIỂM CHỨNG: người nghe xác định từ dòng kề (1530 ← 1690; 1330 ← 1311; 2515 là độc thoại).
- Second pass (đọc lại toàn bộ 15 giá trị fix đối chiếu JP): tổng 15 / kiểm chứng lại 15 / loại bỏ 0 / sửa lại 0. (Lưu ý: lần ráp khối TOML đầu tiên dùng newline thật thay vì `\n` theo quy ước CSV3 — kiểm tra cơ học bắt được, đã sửa lại trước khi ghi file; không có giá trị fix nào thay đổi nội dung.)
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (tỉ lệ tương đồng 0,86–0,99; 1334 thấp 0,38 vì cả dòng chỉ có 1 từ "Tuyệt quá!" → "Ừ!").

## 5. Khối TOML (đã parse-verified)

```toml
[script]
"998" = "……Có rất nhiều người đang gật đầu.\\nCảm giác như họ đang lắng nghe rất chăm chú."
"1304" = "「Oa a a a a~Ư」"
"1326" = "「Ư, ừm. Mình cũng nghĩ là như vậy ạ.」"
"1330" = "「Ừm.\\nEm nghĩ nếu bây giờ rút lui thì cũng không ai nhận ra đâu――」"
"1334" = "「Ừ!」"
"1358" = "「Sa bàn…… cất công mang đến tận đây vậy mà.」"
"1527" = "「Em sẽ gọi điện thoại ạ. Chia nhau ra gọi cùng với Nagi.\\nEm sẽ mượn danh sách từ mẹ, rồi nhờ họ thử xem ạ.」"
"1530" = "「Tất nhiên rồi. Tôi sẽ cho nó hạ cánh trên mặt nước gần đây.\\nNavi cũng đã nắm bắt được tình hình rồi.」"
"1601" = "「Nếu thứ đó được xây lên thì……\\ncảnh quan hay gì đó cũng sẽ biến mất hết.」"
"1703" = "「Ư!」"
"1955" = "Uyn――\\nTiếng động cơ trầm thấp vang lên trong hội trường."
"2251" = "Và rồi con bé thoăn thoắt vẽ thứ gì đó――Ư!!"
"2269" = "Giữa những nụ cười, nụ cười và nụ cười, một Ohimitera tràn ngập nụ cười.\\n\\x%l8620;#00ffc040;8620%l;#; và \\x%lキハ07;#00ffc040;KiHa 07%l;#;S cùng \\x%l客車;#00ffc040;toa hành khách%l;#; mới, đang chở chúng tôi băng băng chạy."
"2344" = "Bỗng nhiên, Kisaki nở một nụ cười.\\nNhư thể đã cạn lời, lại như thể đã mệt mỏi――"
"2515" = "（Giờ thì, tôi cũng phải hành động thôi）"
```

## 6. Cờ cho Hieu (không tự quyết)
- (1) Kisaki gọi Hibiki là "cô" trong tranh luận (1250, 1366, 1243) — giữ như cách xưng trang trọng hay đổi về gọi tên "Hibiki" như các dòng khác? (Hiện GIỮ nguyên.)
- (2) 2515 Soutetsu độc thoại "mình"→"tôi": audit sửa theo quy tắc chung (không phải tự vấn cảm xúc) — nếu Hieu muốn "mình" cho mọi độc thoại nội tâm của Soutetsu thì hoàn lại.
- Đợt thống nhất: "Ohimitera" ×19, "Đường sắt Ohito" ×1, "tuyến Yui" ×1, "ga Yui" ×1.
- B19 vẫn park (không liên quan file này).

## Kết bài
File 日々姫13_討論会: 410 dòng đã đọc, 15 dòng sai (3,7%) — lỗi rải rác, không có cụm hệ thống ngoài mẫu "Ạ." đứng một mình ×5 (đều của Fukami). Không lệch dòng, không xoay vòng, không tràn chương, không dòng mồ côi, không dòng chưa dịch. JSON + khối TOML đã kiểm chứng xong, sẵn sàng merge.
