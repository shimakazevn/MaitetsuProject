# Audit — 凪ふかみ02_命の重さ.txt.toml (route 07_Nagi_Fukami)

- File: `07_Nagi_Fukami/凪ふかみ02_命の重さ.txt.toml`
- Đĩa: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/07_Nagi_Fukami/#U51ea#U3075#U304b#U307f02_#U547d#U306e#U91cd#U3055.txt.toml`
- MD5: `1043cc15a027e5a6edcc11a94ce93a93` — bản duy nhất, không thuộc nhóm trùng (không có file TOML nào khác cùng md5).
- Số dòng script đã đọc: **407/407** (đọc từng dòng đối chiếu JP + TW; CSV3: 1 tập duy nhất, 0 khóa trùng).
- Số dòng sai: **10** — tỉ lệ **2,46%**.
- Phân loại: gasp 7 · thuật ngữ (Seki "ông ngoại") 2 · đại từ 1.
- Danh sách sửa: `audit-nagifukami02-inochi-no-omosa-wrong.json` (9 mục, khóa chuỗi).
- Cơ sở tổng: 144 file / 6.519 dòng sai (đã tự kiểm chứng trong ROUTE-AUDIT.md).

## Phương pháp

Đọc toàn bộ 407 dòng script đối chiếu JP + TW trong CSV3 (Trang tính 3, 91.731 dòng). Kiểm tra: lệch dòng / chuỗi xoay / nhiễm chéo file / dòng mồ côi / chưa dịch / khóa trùng; số lượng tag %l JP vs VN từng dòng; quét toàn bộ đại từ Soutetsu (92 dòng thoại 双鉄) và cặp Nagi↔Fukami; kiểm tra trực tiếp 5 mục sweep của file trong `sweep-raw-gasp-wrong.json`; kiểm tra các hàng "ông nội" trong file.

## Các lỗi đã sửa

### 1. Gasp — 7 dòng

**Key 1635** [双鉄] — sweep `lost-gasp-whole`, áp nguyên:
- JP: 「っ！」 / TW: 「！」
- Cũ: 「!」 → **Mới: 「Ư!」**

**Key 1636** [双鉄] — sweep `lost-gasp-whole`, áp nguyên:
- JP: 「っ！！」 / TW: 「！！」
- Cũ: 「!!」 → **Mới: 「Ư!!」**

**Key 1637** [双鉄] — sweep `lost-gasp-whole`, áp nguyên:
- JP: 「っ！？」 / TW: 「！？」
- Cũ: 「!?」 → **Mới: 「Ư!?」**

**Key 1644** [双鉄] — sweep `lost-gasp-trailing`, áp nguyên:
- JP: 「～～～～っ！！」 / TW: 「～～～～！！」
- Cũ: 「~~~~!!」 → **Mới: 「~~~~Ư!!」**

**Key 2308** [monologue] — sweep `lost-gasp-trailing`, áp nguyên:
- JP: みな一様に黙りこみ、\n作業を終える瞬間だけを待ちわび――っ！？
- TW: 難道是大家都默契地不發聲，埋頭等著作業結束的時刻——！？
- Cũ: Tất cả đều đồng loạt im lặng,\nchỉ chờ đợi khoảnh khắc công việc kết thúc——!?
- **Mới: Tất cả đều đồng loạt im lặng,\nchỉ chờ đợi khoảnh khắc công việc kết thúc——Ư!?**

**Key 961** [凪] — gasp đầu dòng, sweep KHÔNG liệt kê (tìm thêm trong lần đọc toàn file):
- JP: 「っ――ひどか、川たい」 / TW: 「——河流太急了」
- Cũ: 「——Dòng sông, chảy xiết quá á.」
- **Mới: 「Ư——Dòng sông, chảy xiết quá á.」**
- Lý do: っ đứng riêng ở đầu dòng, VN chỉ còn dấu gạch ngang — tiếng gasp mất hoàn toàn. Theo quy tắc gasp đã khóa (thêm Ư khi âm っ hoàn toàn mất: cuối tuyệt đối không dấu câu, hoặc đầu dòng) và tiền lệ sweep §8 (4 dòng khôi phục gasp đầu dòng bị mất khi JP bắt đầu bằng っ đứng riêng). Dấu ―― không diễn được âm nghẹn; đây không phải trường hợp already-rendered (không có nguyên âm hay từ tượng thanh nào đi kèm).

**Key 1309** [凪] — んっ diễn chưa đúng dạng đã khóa:
- JP: 「んっ！　……この辺でっ、良か、と？」 / TW: 「唔！……在這附近行嗎？」
- Cũ: 「Ư! ...Chỗ này, được không, á?」
- **Mới: 「Ưm! ...Chỗ này, được không, á?」**
- Lý do: tiền lệ đã khóa trong AUDIT-BRIEF.md: んっ → "Ưm" (âm mũi ん phải được giữ; "Ư" làm mất ん). Cùng file đã đúng ở 1296 (ん？ → "Ưm?") và 1303 (ん―― → "Ưm——") nên 1309 là không nhất quán. でっ giữa câu là っ nhấn mạnh, giữ nguyên không thêm Ư.

### 2. Thuật ngữ Seki — 2 dòng ("ông nội" → "ông ngoại")

**Key 2299** [monologue] — mục đã quyết cho file này (áp trong audit, không flag lại):
- JP: ふかみの祖父とそのご兄弟、堰さんたちの\x%l保線;#00ffc040;保線%l;#;のおかげで、\n\x%l8620;#00ffc040;8620%l;#;も\x%lキハ07;#00ffc040;キハ07%l;#;も、今日も運行できたのだ。
- TW: 都是多虧了深美的爺爺和他的兄弟，堰先生他們的\x%l保線;#00ffc040;巡線%l;#;工作，\x%l8620;#00ffc040;８６２０%l;#;和\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;才能在今天也順利地開行。
- Cũ: Nhờ công \x%l保線;#00ffc040;bảo trì đường ray%l;#; của ông nội Fukami và những người anh em của ông, ông Seki và mọi người,\nmà \x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#; hôm nay mới có thể vận hành được.
- **Mới: Nhờ công \x%l保線;#00ffc040;bảo trì đường ray%l;#; của ông ngoại Fukami và những người anh em của ông, ông Seki và mọi người,\nmà \x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#; hôm nay mới có thể vận hành được.**
- Lý do: Seki là ông ngoại của Fukami (quyết định 20/11: 08c 2456 Seki gọi Midori là 娘, Midori là mẹ Fukami; 08c 2086 Seki gọi Fukami là 孫娘).

**Key 1338** [ふかみ] — cùng nhóm Seki, tìm thêm trong lần đọc toàn file (không có trong danh sách 4 hàng đã liệt kê, nhưng cùng quy tắc đã quyết):
- JP: 「はい。お爺ちゃんたちがいないから、重機は使えません。\nだから、舟は人力で引き揚げます」
- TW: 「嗯。現在爺爺他們不在，用不了重型機械。所以我們要用人力把船拉上岸」
- Cũ: 「Vâng. Vì không có ông nội và mọi người ở đây nên không dùng được máy móc hạng nặng.\nDo đó, chúng ta sẽ kéo thuyền lên bằng sức người.」
- **Mới: 「Vâng. Vì không có ông ngoại và mọi người ở đây nên không dùng được máy móc hạng nặng.\nDo đó, chúng ta sẽ kéo thuyền lên bằng sức người.」**
- Lý do: お爺ちゃんたち ở đây chính là nhóm Seki — chuỗi chứng cứ trong cùng file: 1595 "堰さんたちが、今日も保線をしてくれた" (nhóm Seki làm bảo trì đường ray hôm nay), 1371 Soutetsu hỏi "堰さんたちは、まだ？" (họ chưa về sao?), 1343 Fukami đáp họ đang ở bến thuyền Yunoi kéo thuyền lên, rồi 1338 giải thích vì "các ông" không có mặt nên không dùng được máy móc hạng nặng. Chỉ đổi đúng từ chỉ nhóm Seki; hàng "ông nội" còn lại trong file (1190, ông của Nagi = Minokasa) giữ nguyên vì không phải Seki.

### 3. Đại từ — 0 dòng (1 fix đã loại khi parent kiểm chứng gộp)

**Key 1544** [双鉄] — ĐÃ LOẠI (parent kiểm chứng 21/11 ~09:20): agent kết luận người nghe là Hachiroku và sửa "Anh"→"Tôi", nhưng bằng chứng không đứng: "dòng trước 1346" cách 1544 gần 200 key, thuộc cảnh khác; dòng kề thực sự là 1542 (Fukami đề nghị giúp — "nếu anh Soutetsu... không thấy phiền... thì mới được ạ") và 1549 (Fukami khẳng định "Để tớ làm cho"); 1544 "であれば、すまんがよろしく頼む" đáp trực tiếp lời đề nghị của Fukami. Hachiroku không có dòng thoại nào gần 1544 trong file (các dòng ハチロク: 1196, 1231, 1320, 1346, 1448, 1630). Chính agent cũng ghi 1546 "Anh hiểu rồi" trong cùng mạch thoại là "anh" đúng với người nghe Fukami — mâu thuẫn với kết luận Hachiroku ở 1544. Kết luận: người nghe là Fukami (hoặc nhóm Nagi+Fukami), "Anh" đúng theo quy tắc đã chốt; fix bị loại, giữ nguyên VN cũ. (Tiền lệ: file 09 key 2525, file 08 keys 1980/2071.)
- CỜ CHO HIEU / đợt unification: VN cũ "nhờ cô nhé" trong cùng dòng 1544 vẫn đáng ngờ — Soutetsu gọi Fukami là "em" ở 1575 ("Cảm ơn em") và 1613, không gọi "cô" ("cô" trong file này chỉ dùng với Hachiroku: 1226, 1325); có thể đúng phải là "nhờ em nhé". Giữ nguyên theo quy tắc "khi nghi ngờ thì giữ và cờ" — chưa sửa, chờ Hieu xác nhận hoặc đợt unification quyết.

## Kiểm tra sweep

- File có đúng 5 mục trong `sweep-raw-gasp-wrong.json` (1635, 1636, 1637, 1644, 2308) — cả 5 đều còn ở trạng thái cũ trong TOML, đã áp nguyên, kiểm chứng từng giá trị với JP.
- Ngoài sweep: 961 (gasp đầu dòng bị sweep bỏ sót) và 1309 (んっ → Ưm) tìm thêm trong lần đọc toàn file — xem mục gasp ở trên.

## Kiểm tra cấu trúc

- Lệch dòng: **0**. Xoay vòng (rotation chain): **0**. Nhiễm chéo file: **0**. Dòng mồ côi: **0**. Chưa dịch / VN trống / VN == TW / VN == JP: **0**.
- Khóa trùng trong CSV3: **0** (407 khóa duy nhất, toàn bộ ở section `script`). CSV3 chỉ có 1 tập cho file này (không có tập trùng / tập "home" cũ).
- Tag %l: số lượng tag JP vs VN khớp **407/407** dòng; không có tag hỏng nào trong file này. `[selections]` trong TOML rỗng — không có gì để kiểm tra.
- VN trùng nhau ở 2 khóa: 1282 「わかっとるばい！」 và 1283 「わかったばい！」 cùng dịch "Em biết rồi á!" — JP khác nhau nhưng cùng nghĩa tự nhiên trong tiếng Việt, không phải lệch dòng.
- TOML-2 flatten `\n` thành khoảng trắng ở 220 dòng — hiện tượng đã biết, CSV3 (literal `\n`) là chuẩn cho danh sách sửa; không phải lỗi.

## Kiểm tra đại từ (quét toàn file)

- Quét cả 92 dòng thoại 双鉄: 0 sai sau khi parent loại fix 1544 (xem §3). Các "anh" còn lại đều đúng người nghe: Nagi (1458, 1529, 1300, 1365, 1508, 1457, 1345...), Fukami (1371, 1453, 1538, 1546, 1610, 1597, 1461, 1350, 1488, 960, 1435, 971...); "tôi" với Hachiroku đúng ở 1226; "anh" ở 1520 là lời Paulette nhờ Soutetsu ("đã nhờ anh soát vé") nên đúng.
- Cặp Nagi↔Fukami: Nagi không gọi Fukami là "chị" ở bất cứ dòng nào ("chị" trong file chỉ dành cho Hachiroku 1593 và Paulette 1385); Fukami→Nagi là "cậu" (1304); Fukami tự xưng "tớ"/"em" đúng ngữ cảnh; Nagi tự xưng "em"/"tớ" đúng.
- Monologue không có "anh" làm đại từ tự xưng (lần duy nhất từ "anh" xuất hiện là "anh em" ở 2299).

## Đã xem xét nhưng giữ nguyên (không sửa)

- 2168, 960: "Ohimitera" — thuộc đợt unification pass (dạng cũ của Ohitoyo), không sửa trong audit.
- 1273, 960: "Migita" là họ nhà (nhà xưởng / nhà Migita), không phải tên người trong đợt unification "Migita Ichi".
- 960: 養子 → "con nuôi" là đúng (chính JP dùng 養子; TW cũng 養子).
- 1355, 2152, 2059: câu JP bị cắt dở, VN hoàn thiện ý — TW xác nhận cùng cách hoàn thiện, không phải bịa.
- 2383 (ごおおおっ！ → "Vùuuuu!"), 2367/31/2366 (ざばあっ/ザバンっ → "Rào"/"Ào"), 2365 (こつんっ → "Cộc"), 2357/2356 (くっ → "Hự"), 2359/2375 (chuỗi SFX chà rửa gộp thành "Xoạt") — SFX đã được diễn, TW cũng gộp tương tự; không thêm Ư.
- 1896: ぷりっとした指 → "ngón tay mềm mại" (sắc thái hơi lệch so với "mũm mĩm/căng tròn" nhưng chấp nhận được trong ngữ cảnh); 1367: 岩 → "đất đá" (hơi rộng nhưng không sai nghĩa). Cả hai đều không đủ rõ để sửa.
- 1595: してくれた (quá khứ) dịch "đang làm nhiệm vụ" — TW cũng dùng thì hiện tại tiếp diễn (進行), giữ nguyên theo TW.

## Lượt soát 2 (bắt buộc — đọc lại toàn bộ giá trị sửa đối chiếu JP)

- Tổng số fix: **9** · đã soát lại: **9** · bỏ đi: **1** (1544 — parent loại khi kiểm chứng gộp, xem §3) · sửa lại: **0**.
- Mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra cơ học bằng diff từng cặp old_vn/fix: 961 chèn "Ư"; 1309 chèn "m"; 1338/2299 "nội"→"ngoại"; 1635/1636/1637/1644/2308 chèn "Ư" (fix 1544 đã loại, xem §3)).
- jp/tw/old_vn trong JSON khớp CSV3 tuyệt đối **9/9**; old_vn khớp giá trị hiện tại trong TOML **9/9** (sau khi chuẩn hoá `\n` → khoảng trắng như TOML-2).

## Khối TOML (đã kiểm chứng parse bằng tomllib — 9 khóa, 0 sai lệch giá trị so với JSON; `\n` literal viết dạng `\\n` trong raw text)

```toml
[script]
961 = "「Ư——Dòng sông, chảy xiết quá á.」"
1309 = "「Ưm! ...Chỗ này, được không, á?」"
1338 = "「Vâng. Vì không có ông ngoại và mọi người ở đây nên không dùng được máy móc hạng nặng.\\nDo đó, chúng ta sẽ kéo thuyền lên bằng sức người.」"
1635 = "「Ư!」"
1636 = "「Ư!!」"
1637 = "「Ư!?」"
1644 = "「~~~~Ư!!」"
2299 = "Nhờ công \\x%l保線;#00ffc040;bảo trì đường ray%l;#; của ông ngoại Fukami và những người anh em của ông, ông Seki và mọi người,\\nmà \\x%l8620;#00ffc040;8620%l;#; và \\x%lキハ07;#00ffc040;KiHa 07%l;#; hôm nay mới có thể vận hành được."
2308 = "Tất cả đều đồng loạt im lặng,\\nchỉ chờ đợi khoảnh khắc công việc kết thúc——Ư!?"
```

## Kết bài

File 凪ふかみ02_命の重さ: 407 dòng đã đọc, **9 dòng sai (2,21%)** — gasp 7, thuật ngữ Seki 2, đại từ 0 (1 fix đại từ 1544 đã bị parent loại khi kiểm chứng gộp — người nghe là Fukami, không phải Hachiroku; xem §3). Không có lệch dòng, xoay vòng, nhiễm chéo, mồ côi, chưa dịch hay khóa trùng. Áp đúng 5 mục sweep của file, cộng 2 lỗi gasp tìm thêm trong lần đọc toàn file (961, 1309) và 1 hàng Seki cùng nhóm (1338) theo đúng quy tắc "ông ngoại" đã quyết. Có 1 hàng cờ cho Hieu: 1544 VN cũ "nhờ cô nhé" (xem §3, có thể đúng là "nhờ em nhé"); các mục unification (Ohimitera ×2) để lại cho đợt unification pass.
