# Audit — lr真闇追加02_御一夜新婚旅行 (05_Mayami) — 81/355 (22,8%)

File: `lr真闇追加02_御一夜新婚旅行.txt.toml` — route 05_Mayami, 355 dòng script.
Disk: `sources/toml2/translation_toml/05_Mayami/lr#U771f#U95c7#U8ffd#U52a002_#U5fa1#U4e00#U591c#U65b0#U5a5a#U65c5#U884c.txt.toml` (tên file #U-escaped, đúng như trên đĩa).
Nội dung: chuyến "tuần trăng mật" của Mayami (真闇) — Reina làm hướng dẫn viên đưa Mayami đi tham quan Ohitoyo: tập xúc than (投炭) trên máy tập, thi xúc đúng 1kg/xẻng (ワンスコ), tham quan xưởng rượu Migita Ichi, chụp ảnh đường sắt (cầu sông Kuma, tàu 8620 do Hibiki lái), thử rượu shochu, bàn chuyện cải trang/hóa trang thành ma sơ, cậu bé đánh giày…
Nhân vật: 真闇 108, monologue 87, 双鉄 79, れいな 61, 日々姫 20.

Phương pháp: đọc toàn bộ 355 dòng theo từng hàng, đối chiếu JP + TW (CSV3), kiểm tra cơ học thêm (xem §3). TOML order == key order == story order trong file này (đã kiểm tra), nên người nghe xác định theo dòng kề trong key order.

## §1. Kết quả

Sai: **81/355 (22,8%)**.

Phân loại (81):
- **misaligned (chuỗi xoay VN)**: 24 — VN của 24 hàng bị lệch sang hàng khác (xem §2.1).
- **untranslated**: 1 (1370 — VN trống trong CSV3, TOML giữ nguyên câu tiếng Trung).
- **pronoun**: 48 — tự xưng của Soutetsu sai hệ thống: độc thoại 30 (dùng "em" thay vì "tôi"), đối thoại 18 ("em"/"anh" sai người nghe).
- **terminology**: 5 (1252, 1562, 1829 右田一→"Migitakazu"; 1749, 1952 一升瓶→"chai rượu Issho").
- **meaning**: 2 (1414 バトンタッチ→"trao cờ"; 1681 してみたか→"Em muốn đi!!").
- **gasp**: 1 (1835, mục sweep — thiếu Ư).

Theo nhân vật: monologue 39/87 (44,8%), 双鉄 25/79 (31,6%), 真闇 8/108 (7,4%), れいな 7/61 (11,5%), 日々姫 2/20 (10,0%). Đối thoại 42/268 (15,7%), độc thoại 39/87 (44,8%).

**Chuỗi xoay là lỗi hệ thống lớn nhất của file này** (25 hàng gồm cả 1370): 25 hàng ĐẦU TIÊN theo thứ tự file của CSV3 (vị trí 0–24) bị lệch VN xuống 1 hàng — VN ở hàng i là bản dịch đúng của JP ở hàng i−1. Hàng đầu chuỗi (1370) mất luôn VN (trống), và bản dịch đúng của hàng cuối chuỗi (1346 「うむ」) cũng bị mất — không còn ở đâu trong file (đã tìm, không có VN "Ừm" lẻ nào). 24/25 hàng trong chuỗi được sửa bằng cách đưa VN bị lệch về đúng hàng của nó (đã kiểm chứng từng cặp VN↔JP); 1346 dịch mới "Ừm"; 1370 dịch mới từ JP. Ngoài chuỗi này, file KHÔNG còn hàng lệch nào khác (đã kiểm tra trùng VN ở 2 key: 0 cặp; xem §3).

Không orphan (mọi VN lệch đều tìm được JP gốc trong file), không contamination chéo file, 0 duplicate key.

Sweep っ-gasp: 1 mục cho file này (1835) — đã kiểm chứng và áp dụng (xem §2.4). Không còn gasp sót: đã quét toàn bộ dòng JP có っ (xem §3).
Strong candidates 8 → đọc toàn bộ tìm ra 81 sai: heuristic chỉ đếm được một phần nhỏ (nó không thấy được chuỗi xoay và lỗi đại từ hệ thống).

## §2. Các lỗi và cách sửa

### §2.1. Chuỗi xoay VN — 25 hàng (24 misaligned + 1370 untranslated)

Cơ chế: 25 hàng đầu theo thứ tự file của CSV3 (1370, 1217, 1942, 1564, 1163, 1376, 1816, 1475, 1133, 1498, 1982, 1205, 1271, 1120, 1220, 1896, 1428, 1632, 1503, 1228, 1355, 1831, 1625, 1183, 1346) — vị trí 0–24, liên tục tuyệt đối. VN ở mỗi hàng là bản dịch đúng của JP ở hàng liền trước. Hàng 1370 (đầu chuỗi) VN trống; bản dịch của 1346 (cuối chuỗi) bị mất hẳn.

Bảng đối chiếu (mũi tên: VN hiện tại ở hàng X ← bản dịch đúng của JP ở hàng Y; fix = đưa VN về đúng hàng, chỉ chỉnh thêm chỗ ghi chú):

| Hàng sai | Nhân vật | JP (tóm tắt) | VN hiện tại là bản dịch của | Fix (ghi chú) |
|---|---|---|---|---|
| 1120 | 双鉄 | "Không, tôi vẫn vừa nghĩ vừa làm, nên chắc giải thích tốt được" | 1271 (Mayami: "Sou-chan không chừng cũng giải thích kém?") | VN của 1220, đổi "em"→"tôi" (người nghe Mayami) |
| 1133 | 双鉄 | "Minokasa cũng rất quan tâm, bảo 'cách truyền đạt vậy dễ hiểu'" | 1475 (Mayami: "chị tự làm rồi bị vướng nên mới nói được") | VN của 1498, giữ nguyên |
| 1163 | 真闇 | "Tay chị khéo quá, chẳng giống làm lần đầu" | 1564 (Reina: "Kuma + làm dao, lần đầu nên hồi hộp") | VN của 1376, giữ nguyên |
| 1183 | 真闇 | "Vừa đúng á, dù chị xúc đại thôi sao?" | 1625 ("Lượng này, vừa đúng 1kg") | VN của 1346, đổi "em"→"chị" (Mayami tự xưng) |
| 1205 | 双鉄 | "Càng thành thạo càng khó diễn đạt bằng lời" | 1982 (monologue: "Minokasa dạy bằng làm mẫu, Reina không hợp") | VN của 1271, giữ nguyên |
| 1217 | 真闇 | "Ưm fufu, bé Reina vui, chị cũng vui lắm" | 1370 (Reina: "làm hướng dẫn viên thú vị quá") | VN của 1942, giữ nguyên |
| 1220 | れいな | "Ufufuu, Reina cũng cực kỳ mong chờ" | 1120 (Soutetsu: "tôi vẫn vừa nghĩ vừa làm…") | VN của 1896, giữ nguyên |
| 1228 | 真闇 | "Hêê—— A, dùng cái xẻng này để tập sao?" | 1503 (Soutetsu: "thân bảo trì Hachiroku cũng tập xúc than") | VN của 1355, giữ nguyên |
| 1271 | 真闇 | "Ây da, Sou-chan không chừng cũng giải thích kém?" | 1205 (Soutetsu: "càng thành thạo càng khó diễn đạt") | VN của 1120, giữ nguyên |
| 1346 | 双鉄 | 「うむ」 | 1183 (Mayami: "Vừa đúng á, dù xúc đại?") | Dịch mới: 「Ừm」 (bản dịch gốc bị mất) |
| 1355 | 双鉄 | "À, nó gọi là wansuko, xẻng xúc đúng 1kg" | 1228 (Mayami: "dùng cái xẻng này?") | VN của 1831, giữ nguyên |
| 1370 | れいな | "Ưfufu~, làm hướng dẫn viên thú vị quá nhỉ~" | — (VN trống; TOML giữ câu tiếng Trung) | Dịch mới từ JP (+TW) |
| 1376 | れいな | "Ehehe, nhờ ông Minokasa và chị Mayami, lời khuyên dễ hiểu" | 1163 (Mayami: "tay chị khéo quá…") | VN của 1816, giữ nguyên |
| 1428 | れいな | "Vâng ạ. Đây là bãi tập xúc than tự hào của Đường sắt Ohitoyo…" | 1896 (monologue: "Reina vừa nói như vứt bỏ việc hướng dẫn…") | VN của 1632, đổi "Ohito"→"Ohitoyo" |
| 1475 | 真闇 | "Chị tự làm rồi bị vướng nên mới nói được; Reina cũng gặp khó…" | 1816 (monologue: "Tôi gật đầu đồng tình với lời Reina…") | VN của 1133, giữ nguyên |
| 1498 | れいな | "Được chị chỉ dạy bằng lời, Reina mới hiểu ra 'À, là như thế…'" | 1133 (Soutetsu: "Minokasa cũng rất ấn tượng…") | VN của 1982, giữ nguyên |
| 1503 | 双鉄 | "Thân bảo trì Hachiroku cũng tập xúc than; không tập thường xuyên tay nghề mai một" | 1632 (Mayami: "Sou-chan, Hi-chan, Na-chan cũng tập ở đây?") | VN của 1228, đổi "thân chính"→"thân bảo trì" |
| 1564 | れいな | "Kuma + làm dao, lần đầu nên hồi hộp lắm ạ" | 1942 (monologue: "chị Mayami chiều quá, Reina vào chế độ tận hưởng") | VN của 1163, giữ nguyên |
| 1625 | 双鉄 | "Lượng này, vừa đúng 1 kilogram" | 1831 (monologue: "Tôi cắm xẻng wansuko vào đống than…") | VN của 1183, giữ nguyên |
| 1632 | 真闇 | "Vậy thì, Sou-chan, Hi-chan và Na-chan cũng tập ở đây sao?" | 1428 (Reina: "Đây là bãi tập xúc than tự hào của Đường sắt Ohito…") | VN của 1503, đổi "Hii-chan"→"Hi-chan" (dạng dùng 17 chỗ khác trong file) |
| 1816 | monologue | "Tôi gật đầu đồng tình với lời Reina. Ai là hướng dẫn viên đây…" | 1376 (Reina: "nhờ ông Minokasa và chị Mayami…") | VN của 1475, giữ nguyên |
| 1831 | monologue | "Tôi cắm xẻng wansuko vào đống than tập, xúc thử cho xem" | 1355 (Soutetsu: "nó gọi là wansuko, xẻng xúc đúng 1kg") | VN của 1625, giữ nguyên |
| 1896 | monologue | "Reina vừa nói như vứt bỏ việc hướng dẫn, vừa dẫn chúng tôi đến bãi tập…" | 1220 (Reina: "Ufufuu, Reina cũng mong chờ…") | VN của 1428, giữ nguyên |
| 1942 | monologue | "Vì chị Mayami chiều quá, Reina đã vào chế độ tận hưởng" | 1564 (Reina: "Kuma + làm dao, lần đầu nên hồi hộp") | VN của 1564, giữ nguyên |
| 1982 | monologue | "Minokasa là thợ thủ công, dạy bằng làm mẫu; với Reina cách đó không hiệu quả" | 1205 (Soutetsu: "càng thành thạo càng khó diễn đạt") | VN của 1205, giữ nguyên |

Chi tiết 2 hàng dịch mới:
- **1346** — 双鉄: JP 「うむ」; TW 「嗯」; VN cũ (lệch từ 1183) 「Vừa đúng á, dù em chỉ xúc đại thôi sao?」; Sửa: 「Ừm」.
- **1370** — れいな: JP 「うっふふー、ガイドさんって、とーってもたのしいお仕事ですねぇ」; TW 「嘿嘿嘿，導遊真是個特別有趣的工作」; VN cũ: (trống trong CSV3; TOML giữ câu TW 「嘿嘿嘿，導遊真是個特別有趣的工作」); Sửa: 「Ưfufu~, làm hướng dẫn viên, đúng là một công việc cực kỳ thú vị nhỉ~」 — "Ưfufu" theo đúng tiền lệ trong file cho cùng âm うっふふー (1215 "Ưfufu").

### §2.2. Đại từ xưng hô của Soutetsu — 48 hàng (độc thoại 30 + đối thoại 18)

Quy tắc đã sửa (AUDIT-BRIEF): Soutetsu là "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi; "tôi" với Hachiroku/Mayami/Minokasa/Kisaki; độc thoại = "tôi" (trừ độc thoại nội tâm cảm xúc mới dùng "mình"). Trong file này Soutetsu KHÔNG có dòng đối thoại nào dùng đúng "tôi" (0 dòng), và toàn bộ 30 dòng độc thoại có đại từ đều dùng "em" — lỗi hệ thống của bản dịch, không phải vài chỗ sót.

Bằng chứng độc thoại là của Soutetsu (không phải Mayami): 1955 「新婦の僕がとるべきだろう」 ("người bắt nhịp nên là chú rể như tôi"); 1763 「僕なぞと」; 743 nhắc "真闇姉" ở ngôi thứ ba. Chỉ duy nhất 1888 dùng đúng "tôi" — chứng tỏ "tôi" mới là dạng chuẩn trong file, "em" là lỗi.

**Độc thoại 30** (đều "em"→"tôi"; chỉ liệt kê key + chỗ đổi): 731 (2 chỗ + bỏ "rồi" thừa trong "Chưa đổ được than vào rồi"), 737, 743 (2 chỗ), 1743, 1763, 1777, 1785 (2 chỗ), 1791, 1794, 1810, 1813, 1819, 1823, 1827, 1833, 1861, 1881 (kèm "Ohito"→"Ohitoyo"), 1882, 1886, 1901, 1936, 1939, 1949 (2 chỗ), 1955, 1960, 1971, 1976 (3 chỗ), 2002, 2014, 2016.

**Đối thoại 18** (người nghe xác định theo dòng kề, key order = story order):
| Key | Người nghe | Đổi |
|---|---|---|
| 747 | Reina (đáp lại 746 Reina) | "em thấy"→"anh thấy" |
| 1130 | Mayami (đang dạy chị xúc than; "em" ở đây là ngôi 2) | "Em có thể"→"Chị có thể" |
| 1189 | Mayami (1191 Mayami đáp "なるほどね") | "chính em"→"chính tôi" |
| 1190 | Mayami (nói về xưởng rượu; 1191 Mayami đáp) | "anh cảm nhận"→"tôi cảm nhận" |
| 1200 | Nhóm Mayami + Reina ("Nếu chị Mayami và Reina muốn chụp…") | "em có thể"→"tôi có thể" |
| 1202 | Nhóm (nâng ly vì Mayami, Hibiki, Reina) | "Chỉ có em"→"Chỉ có tôi" |
| 1286 | Mayami ("Nếu là yêu cầu của chị Mayami…") | "thì em sẽ"→"thì tôi sẽ" |
| 1291 | Mayami (1294 Mayami tiếp lời về vụ việc; xem §6) | "em nhớ"→"tôi nhớ" |
| 1309 | Mayami (đáp lại 1307 Mayami) | "anh hiểu"→"tôi hiểu" |
| 1416 | Mayami/nhóm (chuẩn bị trước khi tàu đến) | "Em muốn"→"Tôi muốn" |
| 1446 | Mayami (xin lỗi chị về từ "thẳng" trong lúc dạy chị) | "lỗi của em… của em"→"của tôi… của tôi" |
| 1545 | Reina (đáp lại câu hỏi của Reina 1542; xem §6) | "Đối với em"→"Đối với anh" |
| 1568 | Mayami (trang phục tu sĩ cho chị) | "Em hoàn toàn"→"Tôi hoàn toàn" |
| 1599 | Mayami ("nếu chị không phiền thì cho… hỏi") | "cho em hỏi"→"cho tôi hỏi" |
| 1610 | Mayami ("em" ngôi 2, đang dạy chị) | "em nhớ chú ý"→"chị nhớ chú ý" |
| 1631 | Mayami (1632 Mayami đáp lại) | "em vẫn thường thấy"→"tôi vẫn thường thấy" |
| 1633 | Mayami ("chị thông cảm cho em") | "cho em đi"→"cho tôi đi" |
| 1646 | Mayami (uống cùng chị) | "em cũng xin… Cho em"→"tôi cũng xin… Cho tôi" |

Giữ nguyên, không tính sai: 1336 "anh đã nói vậy" (người nghe Reina — đúng); "em ấy" chỉ Hibiki ở ngôi 3: 1342, 1161, 1573 ("em đang điều chỉnh lò hơi"), 1612 ("Vất vả cho em rồi" — em = Hibiki, người nghe); "Bọn anh" ở 1612 — xem §6.

### §2.3. Thuật ngữ — 5 hàng

- **1252** — 日々姫: JP 「うわ、これ――――こいば、今までにない味とよね。右田一とも、ひとしずくとも全然違う……」; TW 「哇，這是————這是從來都沒嚐過的味道。和右田一的酒，根本截然不同……」; VN cũ: 「…Khác hoàn toàn với Migitakazu, cũng chẳng giống Hitoshizuku chút nào...」; Sửa: "Migitakazu"→"Migita Ichi" (右田一 đọc là "Migita Ichi" — thuật ngữ đã chốt; "Migitakazu" là đọc sai 一 thành "kazu". "Migitakazu" còn xuất hiện ở 2 hàng khác trong file này: 1562, 1829; và 6 hàng ở file khác — xem §6).
- **1562** — れいな: JP 『右田一酒造元』; VN cũ "xưởng rượu Migitakazu"; Sửa: "xưởng rượu Migita Ichi".
- **1829** — monologue: JP 「れいながレールショップを観光するのは、実に和もう。が、真闇姉が右田一酒造元を見学するのは……」; VN cũ "…thú vị. …xưởng rượu Migitakazu thì……"; Sửa: "…quả thực rất êm đềm. …xưởng rượu Migita Ichi thì……" — hai lỗi trong một hàng: "Migitakazu"→"Migita Ichi", và 和もう (êm đềm/thanh thản, hợp lẽ) bị dịch thành "thú vị" (thú vị ≠ hòa hợp).
- **1749** — monologue: JP 「一升瓶から、試飲用の小さなプラカップへと、真水のように美しいクマ焼酎が注がれていく。」; VN cũ "Từ chai rượu Issho, …"; Sửa: "Từ chai rượu 1,8 lít, …" — 一升瓶 là danh từ thông thường (chai 1,8 lít), không phải tên riêng; "Issho" là phiên âm làm mất nghĩa. Chỉ 2 hàng trong toàn dự án dùng "Issho", cả 2 đều ở file này (1749, 1952).
- **1952** — monologue: JP 「…ラベルの貼られていない酒瓶を持ち上げる。」(câu đầy đủ: 「真闇姉がふんわり日々姫の言葉を止める。そうしてその手は、ラベルの貼られぬ一升瓶を持ち上げる。」); VN cũ "…nhấc lên một chai rượu Issho chưa dán nhãn."; Sửa: "…một chai rượu 1,8 lít chưa dán nhãn."

### §2.4. Nghĩa sai — 2 hàng; gasp — 1 hàng

- **1414** — 真闇: JP 「だって。ほんなら、はぁい、れーちゃん、バトンタッチ」; TW 「好吧。那好。姐姐和小玲接力」; VN cũ: 「Nghe chưa kìa. Vậy thì, được rồi, Rei-chan, trao cờ cho em đấy.」; Sửa: 「Nhưng mà. Vậy thì, được rồi, Rei-chan, đến lượt em đấy.」 — だって ≠ "Nghe chưa kìa"; バトンタッチ (trao gậy tiếp sức / đến lượt) ≠ "trao cờ".
- **1681** — 日々姫: JP 「！　してみたか！！」; TW 「！能成功嗎！」; VN cũ: 「! Em muốn đi!!」; Sửa: 「! Thử rồi à!!」 — VN cũ không liên quan gì đến JP (đọc nhầm してみたか thành してみたい rồi diễn thành "muốn đi"); không có hàng nào khác trong file có JP tương ứng với "Em muốn đi!!" (không phải lệch hàng mà là bịa). Cảnh: ngay sau 1680 Mayami "！あらまぁ、ふふふっ、まっことねぇ" — Hibiki ngạc nhiên vì Mayami vừa thử (làm) được.
- **1835** — monologue (gasp, mục sweep duy nhất của file): JP 「捧げたカップを、そのまま口へと――っ！！」; TW 「我舉杯直接喝了一口——啊！！」; VN cũ: "Nâng chiếc cốc lên, đưa thẳng vào miệng——!!"; Sửa: "Nâng chiếc cốc lên, đưa thẳng vào miệng——Ư!!" — áp nguyên fix của sweep (đã kiểm chứng từng dấu vs JP; xem §3).

## §3. Kiểm tra cơ học và các mục đã xác minh là ĐÚNG (giữ nguyên)

- CSV3: bộ duy nhất, 355 dòng, 0 key trùng, 0 VN trống ngoài 1370; thư mục CSV `translation_toml\\05_Mayami`.
- TOML: md5 `7ca65c08188951eea0f7655cacce4999`, BOM + CRLF, [selections] rỗng, không có file trùng md5 (1 bản sao duy nhất — kiểm tra toàn bộ `sources/toml2/`).
- TOML ↔ CSV3: 355 khóa script khớp tuyệt đối, 0 khóa thừa/thiếu; VN khớp tuyệt đối 354/355 (chỉ khác 1370: TOML giữ câu tiếng Trung, CSV3 trống); comment # JP trong [script] 355/355.
- Trùng VN ở 2 key: 0 cặp (đã kiểm tra toàn file) — ngoài chuỗi xoay §2.1, không còn lệch hàng nào.
- %l tag: số lượng tag JP vs VN khớp ở mọi hàng; không có tag VN thiếu dấu `;` đóng trong file này; không có tag %l nào do Gemini tự thêm.
- っ: đã quét toàn bộ dòng JP có っ. Mọi っ khác đều đã được diễn đúng: tiếng cười (1215 うっふふー→"Ưfufu", 1368 うふふぅ→"Ufufu~", 1372 えっへへー→"Ehehe", 1680 ふふふっ→"fufu", んふふっ→"Ưm fufu" ở 1218/1222/1223/1224/1280/1283/1285/1382); っ nhấn mạnh cuối từ không thêm Ư (1431 よしっ→"Tốt lắm.", 1481 おおおっ→"Ô ồ!?", 1314 ひゃっ→"Á!", 1300 あうっ→"Á."); っ trong từ (まっすぐ, ゆっくり, ぎゅっと, すっっごく→"cực kỳ", つっかかって, ぴたっと, ガチん→"keng", ぱっと, ふっと); SFX đã diễn (2037 ぱしゃっ→"Tách", 2038 ぽーっ→"Tuúú…", 2039 ぽっ→"Tu", 2041 がちんっ→"Keng", 2045 ざくっ→"Phập"). Chỉ 1835 là gasp bị mất (đã sửa §2.4).
- **1291 義父さん → "bố nuôi": ĐÚNG, giữ nguyên** (chỉ sửa đại từ "em"→"tôi"). Đây là bẫy ngược của quy tắc 義: Soutetsu là con nuôi nhà Migita — 共通10 key 2573: 「右田の家の養子になって…汰斗さんと、義父と、義母と」 với TW 「成為右田家養子…養父、養母」; 真闇03 key 2478: 義父 là người được nhà Migita mời về làm rể (婿入り), TW cũng ghi 養父. Toàn dự án đều dịch 義父/義母 là "bố nuôi/mẹ nuôi" khi TW ghi 養父/養母. Ở 1291 TW chỉ ghi 父親, nhưng sự thật truyện đã chốt (Soutetsu là con nuôi) nên "bố nuôi" đúng; "bố vợ" mới là sai.
- **1545 湯医線 → "Tuyến Yui": GIỮ NGUYÊN** (chỉ sửa đại từ). Quyết định Yui/Yunoi vẫn chờ Hieu (tiền lệ Reina h4 key 2241 giữ "Yui"). Chỉ 1 hàng "Yui" trong file này.
- **1331/1485/1664 琵国 → "Bikoku": giữ nguyên.** JP có furigana [びこく,1] ("Bikoku"); TW dịch là 緬甸 (Myanmar) nhưng JP thắng TW, và "Bikoku" nhất quán cả 3 chỗ. Ghi chú cho Hieu ở §6.
- **1612 "Bọn anh": giữ nguyên, xem §6.** Nhóm "bọn" gồm Soutetsu + Mayami + Reina xem Hibiki lái tàu; "bọn anh" lấy Soutetsu (anh hai của Hibiki) làm trung tâm — dạng nhóm không theo quy tắc số ít, giữ nguyên theo skill.
- **1888 độc thoại dùng "tôi": đúng duy nhất trong file** — bằng chứng "tôi" mới là dạng chuẩn cho độc thoại Soutetsu.
- Độc thoại dùng "mình" ở 1894 ("điện thoại của mình" — của Reina), 1955 ("cốc nhựa cho mình" — của Mayami), 2004 ("cốc rượu của mình" — của Mayami): đều là sở hữu phản thân, đúng, không phải tự xưng của Soutetsu.
- "em ấy" chỉ Hibiki ở ngôi 3: 1342, 1161, 1871, 1868, 1797, 1866 — đúng, giữ nguyên.
- 1372 「はい、けーゆ」 → "Nào, dầu diesel." — ĐÚNG: けーゆ = 軽油 (dầu diesel), nói thay "cheese" khi chụp ảnh — TW cũng ghi 說柴油.
- 1218 「はい、チーズ」 → "Nào, cười lên." — giữ nguyên (diễn ý "cheese" khi chụp ảnh).
- 1409 「ひーちゃんがあぎゃん立派な汽車ば！」 → "Hi-chan mà lại lái được một chuyến tàu hoành tráng đến thế!" — giữ nguyên: JP bỏ lửng không có động từ; cảnh đang xem tàu 8620 do Hibiki lái (1452), nên "lái" hợp cảnh hơn TW "thiết kế".
- 1353 「ふゎああ」 (ngửi mùi rượu) → "Oaaa" — giữ nguyên: đây là tiếng trầm trồ, không thuộc họ fa/fu (tiếng rên), diễn thành tiếng reo là hợp lý.
- 1431 「よしっ」 → "Tốt lắm."; 1342 「ああ」 → "Vâng."; 1643 「そうであるならばなによりだ」 → "Chị thấy vui là tốt rồi."; 1665 「イメエジ」 → "Tưởng tượng." — đều là diễn lỏng nhưng chấp nhận được, không tính sai.
- 1871 「なっぱ服」 → "đồng phục"; 「半切り缶」 → "hộp thiếc nửa vầng trăng" — diễn chung chung chấp nhận được, giữ nguyên.
- 1203 淡麗辛口 → "thanh mát cay nồng (Tanrei Karakuchi)" — giữ nguyên (giải thích thuật ngữ rượu, có ghi phiên âm).
- "wansuko" (ワンスコ) giữ nguyên phiên âm ở 1355/1625/1831 — tên dụng cụ tự đặt trong truyện, nhất quán cả file.

## §4. Lượt soát 2 (đọc lại toàn bộ fix)

Tổng 81 / tái kiểm chứng 81 / loại bỏ 0 / sửa lại 0.
Cả 81 fix đã đọc lại từng giá trị so với JP (+TW, dòng kề): chuỗi xoay kiểm chứng từng cặp VN↔JP (24 cặp + 2 dịch mới); đại từ kiểm chứng người nghe theo dòng kề (key order = story order); thuật ngữ kiểm tra toàn dự án (義父, Issho, Migitakazu). Không fix nào bị loại hay sửa lại trong lượt soát 2.

## §5. Khối TOML (đã kiểm chứng parse)

```toml
"731" = "「Chưa đổ được than vào. 22 điểm, thưa chị Mayami」\\nGiọng nói tự dưng hiện lên trong đầu tôi lúc này đã bị tôi cố tình gạt đi."
"737" = "……Nếu công việc của một hướng dẫn viên là làm cho khách hàng vui vẻ,\\nthì tôi phải công nhận Reina hôm nay chính là hướng dẫn viên tuyệt vời nhất."
"743" = "……Hibiki chắc chắn sẽ không bao giờ nghĩ là bị làm phiền đâu.\\nTôi dám chắc chắn như vậy, nhưng tôi cũng không muốn phủ nhận ý kiến của chị Mayami."
"747" = "「『Một tính cách tuyệt vời, luôn hết mình và say sưa với mọi việc』\\n——Đó là những gì anh thấy được.」"
"1120" = "「Không không, tôi thì vẫn vừa làm vừa suy nghĩ.\\nNên có lẽ tôi có thể giải thích tốt đấy——tôi nghĩ vậy」"
"1130" = "「Tốt lắm. Chị có thể làm chậm lại một chút,\\nnhưng hãy chú ý đừng làm rơi vãi than nhé.」"
"1133" = "「Không đâu, thực tế ông Minokasa cũng rất ấn tượng mà.\\n『Cách truyền đạt như vậy thì dễ hiểu quá nhỉ』 ông ấy bảo thế」"
"1163" = "「Thao tác của em rất điêu luyện mà.\\nKhông hề giống làm lần đầu chút nào」"
"1183" = "「Vừa đúng á, dù chị chỉ xúc đại thôi sao?」"
"1189" = "「Chuyện nhỏ thôi mà. Hơn nữa, chính tôi cũng muốn xem thử.\\nCơ hội được ngắm nhìn từ góc này hiếm lắm.」"
"1190" = "「Cũng giống như men koji đang sống, bản thân xưởng rượu này cũng đang sống.\\nLần đầu tiên tôi cảm nhận được... trải nghiệm được điều đó.」"
"1200" = "「Cũng chỉ là một chút thôi——ừm. Nếu chị Mayami và Reina\\nmuốn chụp thì tôi có thể hướng dẫn vài mẹo cơ bản.」"
"1202" = "「Chỉ có tôi là chẳng làm gì nên cũng hơi ngại, nhưng mà——\\nNâng ly vì công việc tuyệt vời hôm nay của chị Mayami, Hibiki và Reina nào.」"
"1205" = "「Càng thành thạo thì việc diễn đạt bằng lời càng khó chăng.\\nĐặc biệt là khi đã làm một cách vô thức」"
"1217" = "「Ưm fufu. Thấy bé Reina vui vẻ,\\nchị cũng vui lắm」"
"1220" = "「Ufufuu, sao đây ta,\\nReina cũng cực kỳ mong chờ luôn nha」"
"1228" = "「Hêê——\\nA, dùng cái xẻng này để tập sao?」"
"1252" = "「Oa, cái này――――Hương vị chưa từng có từ trước đến nay.\\nKhác hoàn toàn với Migita Ichi, cũng chẳng giống Hitoshizuku chút nào...」"
"1271" = "「Ây da, vậy thì Sou-chan\\nkhông chừng cũng giải thích kém lắm nhỉ?」"
"1286" = "「Ư……ừm. Nếu là yêu cầu của chị Mayami,\\nthì tôi sẽ xem xét giải quyết theo hướng tích cực vậy.」"
"1291" = "「À……tôi nhớ là có nghe nói rồi.\\nVụ đó có liên quan đến bố nuôi đúng không?」"
"1309" = "「À, điều đó thì tôi hiểu.」"
"1346" = "「Ừm」"
"1355" = "「À, nó gọi là wansuko.\\nMột cái xẻng xúc được đúng 1kg mỗi lần」"
"1370" = "「Ưfufu~, làm hướng dẫn viên,\\nđúng là một công việc cực kỳ thú vị nhỉ~」"
"1376" = "「Ehehe, là nhờ ông Minokasa và chị Mayami đó ạ.\\nLời khuyên của chị Mayami, rất dễ hiểu luôn」"
"1414" = "「Nhưng mà. Vậy thì, được rồi,\\nRei-chan, đến lượt em đấy.」"
"1416" = "「Tuyệt quá. Nhưng cứ từ từ đã.\\nTôi muốn chuẩn bị xong xuôi trước khi tàu đến.」"
"1428" = "「Vâng ạ. Đây là bãi tập xúc than dồn toa tự hào của Đường sắt Ohitoyo nha.\\nCác bác lái tàu, cũng thực sự tập luyện ở đây đó ạ」"
"1446" = "「Vừa rồi là lỗi của tôi, xin lỗi chị.\\nTừ 'thẳng' của tôi dùng chưa chuẩn.」"
"1475" = "「Cái đó, là lúc chị tự làm rồi bị vướng nên được dạy cho.\\nTình cờ bé Reina cũng gặp khó khăn ở chỗ đó nên chị mới nói được thôi」"
"1498" = "「Đúng vậy ạ. Được chị chỉ dạy bằng lời, Reina mới\\nhiểu ra 『À, là như thế này sao』 đó ạ」"
"1503" = "「Đúng vậy. Có lúc thân bảo trì của Hachiroku cũng tập xúc than dồn toa ở đây.\\nNếu không làm thường xuyên, tay nghề sẽ bị mai một」"
"1545" = "「Tuyến Yui dài khoảng 25km, vừa ngắn lại vừa bằng phẳng mà.\\nĐối với anh, một chiều đi thường chỉ tốn khoảng 550 xẻng là cùng.」"
"1562" = "「Địa điểm Reina muốn giới thiệu là ở đây ạ~!\\nChính là xưởng rượu Migita Ichi đó nha~」"
"1564" = "「Cả xuôi dòng sông Kuma, và trải nghiệm rèn dao,\\nReina, đều là lần đầu tiên nên hồi hộp lắm ạ」"
"1568" = "「Chắc chắn là hợp rồi. Khá là——không, thực sự rất tuyệt đấy.\\nThú vị thật. Tôi hoàn toàn chưa nghĩ đến trang phục tu sĩ luôn.」"
"1599" = "「Mà này, nếu chị không phiền thì cho tôi hỏi——\\nLoại rượu này có gì khác so với bình thường vậy? Do nước hay do gạo?」"
"1610" = "「Lắc lư sang hai bên là nguyên nhân làm rơi than đấy.\\nKhi vặn người, chị nhớ chú ý đừng để xẻng than bị nghiêng nhé.」"
"1625" = "「Lượng này, vừa đúng 1 kilogram」"
"1631" = "「Vì đây là một 'địa điểm quen thuộc' mà.\\nTrong lúc làm nhiệm vụ, tôi vẫn thường thấy bóng dáng của mấy tay thích chụp ảnh tàu ở đây.」"
"1632" = "「Vậy thì,\\nSou-chan, Hi-chan và Na-chan cũng tập ở đây sao?」"
"1633" = "「Sai số ngần ấy thì chị thông cảm cho tôi đi.\\nTrong lúc làm nhiệm vụ, việc xúc 1kg than này phải lặp đi lặp lại hàng trăm lần đấy.」"
"1646" = "「Nếu vậy thì tôi cũng xin một ngụm. Cho tôi uống cùng với nhé.」"
"1681" = "「! Thử rồi à!!」"
"1743" = "Nhìn sang, tôi thấy Reina đã cất điện thoại đi rồi."
"1749" = "Từ chai rượu 1,8 lít, loại rượu shochu Kuma trong vắt như nước suối\\nđược rót ra những chiếc cốc nhựa nhỏ dùng để uống thử."
"1763" = "Ra là vậy, quả không hổ danh chị Mayami.\\nĐẳng cấp hoàn toàn khác biệt với đứa đang đứng hình không biết phản ứng sao như tôi."
"1777" = "Ừm. Tuyệt thật. Dù không biết Reina đã xem phim gì,\\nnhưng một hình ảnh khá rõ ràng đang tự nhiên hiện lên trong tâm trí tôi."
"1785" = "Bộ ngực căng đầy càng thêm nổi bật, khiến tôi thoáng chốc mất tập trung.\\nNhưng đây là một bức ảnh quan trọng. Tôi lập tức xốc lại tinh thần."
"1791" = "Giọng nói dịu dàng, nhưng vô cùng dứt khoát.\\nĐương nhiên, tôi cũng gật đầu đồng ý nhiệt liệt."
"1794" = "Đầu và ánh mắt của chị hướng về phía chiếc 8620 vừa chạy khuất.\\nChẳng hiểu sao, điều đó lại khiến tôi cảm thấy vô cùng hạnh phúc."
"1810" = "Chưa kịp uống mà tôi đã thấy say men hạnh phúc rồi."
"1813" = "Vừa nói, tôi vừa chậm rãi làm mẫu.\\nBị nhìn chằm chằm như muốn ăn tươi nuốt sống thế này, quả thực cũng có chút ngại ngùng."
"1816" = "Tôi gật đầu đồng tình sâu sắc với lời của Reina.\\nAi là hướng dẫn viên đây. Người ngoài nhìn vào chắc chắn sẽ hiểu lầm hoàn toàn."
"1819" = "Vừa giục chị Mayami, tôi vừa nhìn sang Reina,\\nđúng lúc cô bé đang đội lại chiếc mũ."
"1823" = "Tôi ngạc nhiên thật sự. Trong lúc tập xúc than mà có thể hình dung thực tế đến mức đó——\\nKhả năng này chắc chắn là một tố chất không thể bàn cãi."
"1827" = "Tôi đã bấm máy vào đúng khoảnh khắc hoàn hảo nhất.\\nNhìn sang chị Mayami, thấy chị ấy vẫn giữ khư khư chiếc điện thoại——"
"1829" = "Việc Reina đi tham quan cửa hàng đường sắt thì quả thực rất êm đềm.\\nNhưng việc chị Mayami đi tham quan xưởng rượu Migita Ichi thì……"
"1831" = "Tôi cắm xẻng wansuko vào đống than đá dùng để tập luyện, rồi xúc thử cho xem."
"1833" = "Tôi nhìn vào đống than phía sau cỗ máy tập luyện. Vì không có ai hướng dẫn nên đương nhiên là,\\nthan vương vãi khắp nơi trông khá là hoành tráng."
"1835" = "Nâng chiếc cốc lên, đưa thẳng vào miệng——Ư!!"
"1861" = "Nghe Reina nói vậy, cả tôi và Hibiki đều gật gù đồng tình."
"1881" = "Năm nào cũng có——đúng là vậy thật.\\nÍt nhất là từ khi tôi bắt đầu làm việc cho Đường sắt Ohitoyo, năm nào cũng vậy."
"1882" = "Chính xác là vậy.\\nCảm xúc mà tôi đang trải qua lúc này, có lẽ ông Minokasa cũng đã từng cảm nhận được."
"1886" = "Tôi nghĩ thời điểm hoàn hảo nhất là khi đầu máy vừa chạm đến\\ntrụ cầu sát bờ đối diện theo hướng di chuyển……nhưng mà……"
"1896" = "Vừa nói những lời như thể đã hoàn toàn vứt bỏ công việc hướng dẫn viên,\\nReina vừa lạch bạch dẫn chúng tôi đến bãi tập xúc than dồn toa."
"1901" = "Suốt quãng đường được dẫn đi, tôi đã cứ nghĩ là không thể nào đâu, không thể nào đâu,\\nnhưng không ngờ lại đúng chóc thế này——"
"1936" = "Chị Mayami bước đến trước cỗ máy tập luyện.\\nChị chậm rãi bắt chước động tác của tôi——rồi gật đầu thật sâu."
"1939" = "Kết quả xúc than của chị Mayami đã bị chôn vùi dưới đống than của Reina.\\nNhưng tôi vẫn có thể trả lời mà không chút do dự."
"1942" = "Vì chị Mayami quá đỗi chiều chuộng,\\nnên Reina đã hoàn toàn bước vào chế độ tận hưởng."
"1949" = "Chuyển động cơ thể của chị Mayami hoàn toàn đúng như những gì tôi chỉ dẫn.\\nVăn võ song toàn một cách rất tự nhiên——Tôi cảm nhận rõ ràng dòng máu giống hệt Hibiki đang chảy trong chị."
"1952" = "Chị Mayami nhẹ nhàng ngắt lời Hibiki.\\nRồi tay chị nhấc lên một chai rượu 1,8 lít chưa dán nhãn."
"1955" = "Chị Mayami cũng đã chuẩn bị sẵn một cốc nhựa cho mình.\\nVậy thì, người bắt nhịp nâng ly nên là chú rể như tôi mới phải."
"1960" = "Đôi mắt chị Mayami thoáng chốc tròn xoe,\\nrồi lại chăm chú nhìn tôi."
"1971" = "Lượng than trong khoang chứa của cỗ máy tập luyện đã giảm đi trông thấy.\\nTôi chỉ mới rời mắt đi một chút thôi mà——"
"1976" = "Bị lặp lại y hệt, tôi mới chợt nhận ra.\\nNhững lời tôi vừa nói cũng chỉ là lặp lại y chang những gì Hachiroku đã nhồi nhét vào đầu tôi mà thôi."
"1982" = "Vì ông Minokasa là thợ thủ công, nên ông dạy bằng cách làm mẫu cho xem.\\nNhưng với Reina, cách đó không mấy hiệu quả."
"2002" = "Vừa dứt lời, tôi chợt nhận ra điều gì đó và vội nói thêm."
"2014" = "Cái gọi là \"Trẻ con trước cổng chùa không học cũng thuộc kinh\"——kiến thức ở mức độ đó,\\ntôi cũng có, mà Hibiki thì lại càng rành hơn. Nhưng mà——"
"2016" = "Chủ đề này mà kéo dài thêm thì nguy hiểm lắm.\\nLinh tính mách bảo thế, nên tôi phải nửa ép buộc cắt ngang."
```

Kiểm chứng: khối parse được bằng tomllib, 81 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` trong khối parse về đúng literal backslash-n của CSV3).

## §6. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

Theo tiền lệ file Hibiki 06 / Grand02 (ghi chú, không tính sai), các dạng cũ hệ thống dưới đây KHÔNG tính vào 81 sai — liệt kê kèm giá trị sửa để đợt thống nhất toàn dự án áp dụng luôn:

1. **Thống nhất "Ohito"/"Ohimitera" → "Ohitoyo"** (4 hàng chỉ sai mỗi chỗ này): 1268 "danh lam thắng cảnh của Ohimitera" → "của Ohitoyo"; 1350 "lịch của Đường sắt Ohito" → "Đường sắt Ohitoyo" (JP 御鉄, TW 御一夜鐵路); 1368 "đi tham quan Ohimitera" → "đi tham quan Ohitoyo"; 1884 "lên chuyến tàu Kiha 07S. Chuyến tham quan Ohimitera…" → "lên chuyến tàu KiHa 07S. Chuyến tham quan Ohitoyo…" (kèm "Kiha"→"KiHa" theo chính tả JR đã chốt). Hai hàng 1428 và 1881 cũng chứa "Ohito" nhưng đã được sửa thành "Ohitoyo" trong fix của chúng (vì hai hàng đó sai vì lý do khác).
2. **Thống nhất 宮司 → "đền chủ"** (2 hàng): 1456 "Cả Po-chan và thầy cúng nữa cơ á!" → "Cả Po-chan và đền chủ nữa cơ á!"; 1500 "Cả Paulette và thầy cúng Akai thỉnh thoảng cũng đến đây chụp ảnh" → "Cả Paulette và đền chủ Akai thỉnh thoảng cũng đến đây chụp ảnh".
3. **"Migitakazu" còn ở file khác**: "Migitakazu" xuất hiện 9 hàng toàn dự án — 3 hàng trong file này đã sửa (1252, 1562, 1829); 6 hàng còn lại ở グランドリライト07_真闇 (1605, 2728, 1506) và 真闇01_再蒸留 (2444, 2164) — sẽ được sửa khi audit 2 file đó (hoặc gộp vào đợt thống nhất "Migita Ichi").
4. **琵国 = "Bikoku" hay Myanmar?** 1331/1485/1664 giữ "Bikoku" theo furigana びこく; TW dịch cả 3 chỗ là 緬甸 (Myanmar). Nếu trong truyện 琵国 chính là Myanmar thì cần đổi cả 3 thành "Myanmar" — chờ Hieu chốt.
5. **1545 "Đối với anh" — phán đoán ít chắc nhất trong audit.** 1542 Reina hỏi thẳng Soutetsu ("anh Soutetsu cũng từng được học một chút rồi đúng không ạ?"), nên 1545 Soutetsu đáp lại Reina → "anh". Nhưng 1548–1549 ngay sau đó Soutetsu hướng dẫn cả "hai người" (Mayami + Reina) chụp ảnh, nên cũng có thể 1545 là nói với nhóm → "tôi". Đã chọn "anh" theo mạch hỏi–đáp trực tiếp; nếu Hieu kiểm tra trong game thấy Soutetsu đang nói với Mayami thì đổi thành "tôi".
6. **1291 "bố nuôi" đã xác minh là ĐÚNG** (xem §3) — chỉ sửa đại từ. Không cần Hieu xác nhận thêm, ghi chú để khỏi sửa nhầm về sau.
7. **1612 "Bọn anh có xem đấy."** — giữ nguyên. Nhóm người xem gồm Soutetsu + Mayami + Reina; "bọn anh" lấy Soutetsu làm trung tâm (anh hai của Hibiki). Dạng nhóm không theo quy tắc số ít; nếu Hieu muốn trung tính tuyệt đối thì đổi thành "Bọn tôi có xem đấy."
8. **1829 "rất êm đềm"** cho 実に和もう — phán đoán dịch nghĩa (JP 和もう = êm đềm/thanh thản/hòa hợp, khác hẳn "thú vị" của VN cũ). Nếu Hieu thấy "êm đềm" chưa hợp tai thì có thể đổi thành "rất hợp tình hợp cảnh".
9. **1681 "Thử rồi à!!"** cho してみたか — TW đọc là "làm được không?" (能成功嗎). Đã chọn nghĩa sát chữ "thử rồi à"; nếu trong game ngữ cảnh là hỏi "làm được không" thì đổi thành "Làm được rồi à!!".

## Kết bài

Đã đọc toàn bộ 355 dòng của lr真闇追加02_御一夜新婚旅行, sai 81 dòng (22,8%): chuỗi xoay VN 25 hàng (24 lệch + 1370 chưa dịch — hàng đầu chuỗi mất VN, bản dịch của 1346 「うむ」 cũng bị mất), đại từ Soutetsu sai hệ thống 48 hàng (độc thoại 30 dòng dùng "em" thay "tôi"; đối thoại 18 dòng sai người nghe), thuật ngữ 5, nghĩa sai 2, gasp 1 (sweep 1835). Không orphan, không contamination chéo file, 0 duplicate key; tag %l sạch; mọi っ khác đều đã được diễn đúng. 81 fix đã qua lượt soát 2 đầy đủ (81/81 tái kiểm chứng, 0 bỏ, 0 sửa). Còn chờ Hieu: thống nhất "Ohito"/"Ohimitera"→"Ohitoyo" (4 hàng), 宮司→"đền chủ" (2 hàng), chốt 琵国 "Bikoku" hay Myanmar, và xem lại 2 phán đoán đã ghi ở §6 (1545 "anh" vs "tôi", 1612 "Bọn anh").
