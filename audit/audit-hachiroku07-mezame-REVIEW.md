# Audit: ハチロク07_ハチロクの目覚め.txt.toml (01_Hachiroku)

- File: `ハチロク07_ハチロクの目覚め.txt.toml` — route 01_Hachiroku, 424 dòng script (monologue 231, 双鉄 122, ハチロク 67, ナビ 2, 登呂流湯主人 2). Nội dung: Soutetsu và Hachiroku ở nhà tắm Tororyu-yu sau vụ tai nạn — đối thoại về tội lỗi, về việc sửa chữa 8620, về quá khứ của Soutetsu với Michiko; xen kẽ độc thoại hồi tưởng (tai nạn, đèn dầu, chuyến đi gia đình) và cảnh đi kiểm tra đường ray dọc tuyến. Chỉ có 5 nhân vật; người nghe của mọi câu thoại Soutetsu đều là Hachiroku, trừ 2 dòng trích lời Paulette (1037, 1288 — "anh" giữ đúng).
- Phương pháp: đọc hết từng dòng đối chiếu JP + TW (CSV3), kiểm tra chéo sweep っ-gasp, kiểm tra cơ học (JSON/TOML/CSV3, md5, trùng lặp, thẻ %l, comment # JP).
- **424 dòng đã đọc hết, 56 dòng sai (13,2%)** — đại từ 29, thuật ngữ 17, gasp 8, SFX 1, typo 1. Thoại 42/193 (21,8%), độc thoại 14/231 (6,1%). Theo nhân vật: 双鉄 35/122 (28,7%), ハチロク 6/67 (9,0%), ナビ 1/2, monologue 14/231 (6,1%).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 424 dòng, 0 key trùng. TOML và CSV3 khớp tuyệt đối 423/424 (chênh duy nhất 2014: TOML làm phẳng `\\n` thành khoảng trắng — CSV3 là chuẩn). TOML md5 `e3ad6757cc9bb746e38e2d4408aeb88f`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng. Comment `# JP:` đủ 433/433 (424 script + 9 characters/subs), 0 lệch. Thẻ `%l`: JP = VN mọi dòng (0 thẻ thiếu dấu `;` đóng, 0 thẻ tự thêm).

## §1. Đại từ — Soutetsu "anh"/"mình" → "tôi" với Hachiroku (29 dòng)

File này là file nhiều lỗi đại từ nhất của route Hachiroku từ trước tới nay: 35/122 dòng thoại Soutetsu sai, gần như toàn bộ là tự xưng "anh" (23 dòng) hoặc "mình" (6 dòng) trong khi người nghe là Hachiroku — áp quy tắc đã chốt ("tôi" với Hachiroku; "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi). Tất cả đều đã kiểm chứng người nghe từ dòng kề: mọi dòng đều nằm trong mạch đối thoại trực tiếp với Hachiroku (không có dòng nào là độc thoại nội tâm hay nói với người khác).

- "anh" → "tôi" (23): 1022, 1026, 1070, 1256, 1267, 1315, 1328, 1333, 1340, 1343 (2 chỗ), 1377, 1398, 1418, 1454 (2 chỗ), 1469, 1484, 1497, 1518, 1522 (2 chỗ), 1524, 1605, 1654 — cộng 1468 (xem dưới).
- "mình" → "tôi" (6): 1024, 1073, 1078, 1258, 1604, 1629 — 6 dòng "mình" ở vị trí chủ ngữ trong thoại với Hachiroku (1024 "mình đã dứt bỏ", 1073 "mình đang đứng", 1078 "Mình chắc cũng sắp sốt", 1258 "hơn mình tưởng", 1604 "để mình bình tĩnh lại", 1629 "như mình làm"). [Đếm: 23 dòng "anh" (26 vị trí — 1343/1454/1522 mỗi dòng 2 vị trí) + 6 dòng "mình" (6 vị trí) = 32 vị trí sửa trên 29 dòng.]
- 1468 "Anh cũng, xem em――" → "Tôi cũng, em――": ngoài đại từ, VN cũ bịa thêm động từ "xem" — JP 「僕も、お前を――」 cụt câu, không có động từ; bản sửa giữ nguyên dạng cụt, không bịa phần tiếp (theo quy tắc "không bịa phần hoàn thiện cho JP cụt").
- Giữ nguyên (đúng): 1037 và 1288 "anh" là lời Paulette nhờ Soutetsu ("Nhờ anh đi kiểm tra tuần tra", "Paulette đã nhờ anh kiểm tra đo đạc") — Paulette gọi Soutetsu là "anh Soutetsu" theo khóa B4. 1260/1448/1510/1513/1578/1609/1656 "tôi" đúng sẵn. 1508 "Mình đúng là đồ ngốc" giữ — Soutetsu lẩm bẩm một mình trên đường ray (tự vấn nội tâm, thuộc ngoại lệ "mình" cho độc thoại nội tâm). 1513/1520/1588/1635/1439 "mình" phản thân/sở hữu/thành ngữ ("mình đã chịu được", "lắc mình", "hết mình", "bản thân mình") giữ đúng. 1561 "Mình, là kẻ gây ra tai nạn duy nhất" là lời Taito trích dẫn trong ngoặc — giữ.

## §2. Thuật ngữ (17 dòng)

- Ohigawa → Ohitoyo (6): 1028, 1562, 1580, 2235, 2584, 2607. Toàn bộ 6 lần 御一夜 trong file đều dịch sai thành "Ohigawa" (đọc sai); 0 lần "Ohitoyo" trong VN cũ. Đây là dạng sai cũ của tên địa danh đã chốt "Ohitoyo" — sửa trong audit (không để đợt thống nhất, vì file đang audit).
- エアクラ → "Aircra", không phải "Aerocraft" (3): 1666 (Navi nói), 2305, 2617. "Aerocraft" là cách dịch sai nghĩa đen ("craft" = tàu/máy bay); tên đã chốt là "Aircra".
- 事故車輌 → "toa xe gặp tai nạn", không phải "phương tiện gây tai nạn" (3): 1052, 1451, 2464. 事故車輌 là toa xe *gặp* tai nạn (8620 là nạn nhân của vụ trật bánh), không phải phương tiện *gây ra* tai nạn — VN cũ đảo nghĩa. (2464: vế sau 「鉄道事故を起こしたレイルロオド」 giữ "đã gây ra tai nạn đường sắt" vì 起こした đúng là "gây ra".)
- 帝鉄 gloss → "Teitetsu" (2): 2156, 2350. VN cũ "Đường sắt Hoàng gia (Teitetsu)" sai cả hai mặt: 帝 = "Đế quốc", không phải "Hoàng gia"; và dạng đầy đủ chỉ dùng ở lần xuất hiện đầu tiên toàn dự án (tiền lệ Paulette れいな02 key 63) — 2 dòng này không phải lần đầu (11 dòng khác đã dùng "Teitetsu" trần, vd. 共通02 2234, 共通03 911/912) nên về đúng dạng ngắn "Teitetsu".
- 機関士 gloss → "thợ lái đầu máy" (2): 2085, 2316. Cả hai đều là độc thoại (lời dẫn), không phải thoại — dạng đầy đủ "thợ lái đầu máy" theo quy tắc đã chốt; "Lái tàu" chỉ là dạng rút gọn dùng trong thoại. Tiền lệ: Hachiroku 14 và 凪ふかみ05 đã sửa gloss 機関士 về "thợ lái đầu máy".
- 乗員 → "nhân viên tàu" (1): 2514. "Phi hành đoàn" là thuật ngữ hàng không, sai hoàn toàn với ngữ cảnh đường sắt; TW 車組成員 (thành viên tổ lái tàu) xác nhận. Đây là 1 trong 2 dòng còn lại toàn dự án (dòng kia: 日々姫03 2834); tiền lệ ハチロク10_炙り出し 2411 đã sửa trong audit.

## §3. Gasp っ (8 dòng — sweep áp nguyên 8/8)

Sweep có 8 mục cho file này (1457, 1487, 1661, 1676, 1677, 1678, 1679, 2208) — audit xác nhận và áp nguyên cả 8 giá trị, 0 sửa lại: 1457 「―――っ!」→ "――Ư!", 1487/1661 「――っ!?」→ "――Ư!?", 1676–1679 cả dòng chỉ có っ+chấm câu → "Ư!"/"Ư!!!"/"Ư!!?"/"Ư!?", 2208 「しま――っ!」→ "――Ư!". Sweep không bỏ sót gasp nào trong file (đã quét cơ học toàn bộ JP có っ+chấm câu — các dòng còn lại đều đã diễn đúng theo quy tắc gasp đã khóa: 1396 くっ→"Hức", あっ――→"A――"; 1406 あっ――→"a――"; 2646/2647/2651/2639 SFX hành động đã diễn; 1386/1387/1261/1337/1664 っ gắn từ nội dung/tên riêng — không thêm Ư).

## §4. SFX và typo (2 dòng)

- 32 (SFX): (ちゃぷん）→ "(Tõm)" (VN cũ "(Bùm)"). ちゃぷん là tiếng nước khẽ (chạm nước nhẹ), TW 撲通; "Bùm" nặng như tiếng nổ/nhảy ùm — "Tõm" đúng âm nhẹ và nhất quán với 2640 ぱちゃり→"(Tõm)" trong cùng file.
- 2016 (typo): "nín thở cái thóp" → "nín thở cái thót" (JP ハっと息を呑む = giật mình nín thở; "thóp" là thóp đầu trẻ sơ sinh, vô nghĩa ở đây — lỗi đánh máy cho "thót").

## §5. Mục đã biết từ trước — kiểm chứng trong file này

- **2514 乗員:** đúng như đã ghi — VN cũ "Phi hành đoàn", đã sửa thành "nhân viên tàu" trong audit (§2). Còn 1 dòng toàn dự án: 日々姫03 2834.
- **2679 Seki ("ông ngoại") và 2596 堰さんたち — KHÔNG TỒN TẠI trong file này:** file hiện tại có 424 key, khoảng key 32–2651 (CSV3 và TOML khớp tuyệt đối). Không có key 2679 và không có key 2596. Ghi chú "ハチロク07 2679 đã sửa trong audit 20/11" không khớp với file hiện tại — có thể ghi chú đó nhầm file hoặc nhầm key. Hai dòng Seki thực có trong file đều đúng sẵn, không cần sửa: 2094 「堰さんはガソリン自動車を有しているが」→ "ông Seki" (xưng hô trung tính, đúng); 2588 「保線ボランティアの堰さんたち――凪のお祖父様たちが」→ "đội tình nguyện bảo trì đường ray của ông Seki ―― tức là các ông của Nagi" ("các ông của Nagi", không dùng "ông nội"/"ông ngoại" — đúng, vì đây là nhóm ông của Nagi nói chung, không phải riêng Seki). **Đề nghị parent kiểm tra lại ghi chú 2679/2596** — có thể thuộc file khác (vd. ハチロク07_延命?); không sửa gì thêm ở đây.
- **1391 「っ」→ "Ư":** VN cũ đã đúng sẵn (không tính lỗi).
- **1398 義父 → "bố nuôi":** giữ đúng — TW 養父 xác nhận (tiền lệ file 10 key 2573: 義 = "nuôi" khi TW có 養).
- **1038 「…………」:** VN == TW (chỉ dấu ba chấm) — không tính lỗi.

## §6. Giữ nguyên có lý do (không tính lỗi)

- 1507 "nhờ cô nhé": người nghe là Navi, không phải Hachiroku. Soutetsu gọi Navi là "cô" đã chốt toàn dự án (17×, vd. グランドリライト02 1679 "Cảm ơn cô vì đã luôn bảo vệ tôi"); Navi là nữ (TW/Common03 2030 "cô ấy", Hachiroku10 2525 "Các cô ấy… các Navi"). Cảnh: Soutetsu đi bộ dọc đường ray vào khu vực Aircra không hoạt động, nhờ Navi (bay được) đón ở phía bên kia — khớp 1666 (Navi nói không theo vào được khu vực đó) và 2305 (chia tay Navi khi vào khu vực). 1500 "cô ấy" cho Navi cũng đúng theo đó.
- 1592/2336/2578 "Ông chủ"/"ông ấy" cho 登呂流湯主人: giữ — VN dùng nam nhất quán trong file, JP ご主人 và TW 老闆 đều trung tính, không có bằng chứng ngược. Tên hiển thị nhân vật trong TOML là "Chủ nhà tắm" (trung tính).
- 1404 「あ……」 và 1408 「ああ……」 cùng VN "A……": ghi nhận (JP khác độ dài) nhưng giữ — quy ước của file (và các file trước) dịch ああ thành "A"/"À" (1020, 1407, 1421); sửa riêng 1408 thành "Aa……" sẽ phá nhất quán. Không tính lỗi.
- 1261 「いいえっ!?」→ "Không đúng!?": giữ — いいえ là từ nội dung (không phải từ âm thanh) nên không thêm Ư; "Không đúng" là cách từ chối khiêm nhường hợp ngữ cảnh (Soutetsu vừa cảm ơn Hachiroku).
- 1020/1421 「ああ」→ "À": giữ — "À" là tiếng đáp/à ơi trong thoại, không phải rên.
- 1058/1252/1375/1451/1538/1580 `[8620'86]` và 2362/2368 `[6200'62]`: giữ — quy ước hiển thị số hiệu tàu có ruby trong toàn dự án (JP `[ハチロクニイマル,3]8620`).
- 1375 "dòng [8620'86]": giữ — "dòng" thêm nhẹ nhưng không sai nghĩa.
- 1281 "người thợ làm đèn dầu" (石油ランプの業者): giữ — TW "石油燈工作者" đồng ý.
- 1627 「お前か、これは?」→ "Của em sao, cái này?": giữ theo JP — TW thêm "血" (máu) là diễn giải của TW, JP không có.
- 2014: chỉ khác TOML/CSV3 ở `\\n` bị làm phẳng — VN đúng, không tính lỗi.

## §7. Kiểm chứng

- JSON 56 mục dạng chuẩn list-of-dicts, khóa chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 56/56 (kiểm chứng cơ học).
- Khối TOML 56 khóa, parse OK bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; fix giữ `\\n` literal của VN cũ — số lượng `\\n` khớp VN cũ 56/56, không thêm `\\n` mới).
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 1468 bỏ "xem" bịa + đổi đại từ, và 5 dòng gasp cả dòng thay toàn bộ dấu câu).
- Lượt soát 2 (đọc lại toàn bộ 56 fix đối chiếu JP + TW): **56/56 tái kiểm chứng, 0 bỏ, 0 sửa**.
- Cơ sở tổng đã rebase: khi audit bắt đầu, ROUTE-AUDIT.md ghi 142 file / 6.450 dòng sai; trong lúc audit, 仲国04_z49列車 đã gộp (+13) thành **143 file / 6.463 dòng sai** — snippet dùng cơ sở mới này (không dùng cơ sở cũ 142/6.450).

## §8. Cờ cho Hieu (không tự quyết)

- Ghi chú 2679/2596 không khớp file (§5) — nhờ Hieu/parent xác minh lại file/key đúng.
- 1507: người nghe suy ra là Navi ("cô") theo mạch cảnh + tiền lệ 17×; nếu Hieu chơi tới đoạn này thấy người nghe là Hachiroku thì đổi "nhờ cô nhé" → "nhờ em nhé".
- B19 in-game check (Paulette 13 key 1596) vẫn park toàn dự án; file này không có thẻ %l hỏng nên không bị ảnh hưởng.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
32 = "(Tõm)"
1022 = "「――Nếu là vì muốn chuộc lỗi với tôi, hay vì cảm giác tội lỗi」"
1024 = "「――Cứ ngỡ là, tôi đã hoàn toàn dứt bỏ được rồi chứ」"
1026 = "「――Tôi, cần em」"
1028 = "「――Ngài Soutetsu, chắc chắn sẽ rời khỏi Ohitoyo đúng không ạ?」"
1052 = "「……Nếu là toa xe gặp tai nạn, thì gần như cho không――\\n――A…… không phải」"
1070 = "「……Tôi, vẫn luôn thắc mắc」"
1073 = "「……Không sao đâu.\\nÍt nhất lúc này, tôi đang đứng trên đôi chân của chính mình」"
1078 = "「……Quá nhiệt sao. Tôi chắc cũng sắp sốt vì suy nghĩ quá nhiều rồi đây」"
1256 = "「Đừng bận tâm. Chính tôi cũng không nhận ra mà」"
1258 = "「Làm thử mới thấy――\\nCông việc này đòi hỏi sự tập trung cao độ hơn tôi tưởng」"
1267 = "「Cũng có thể nói vậy. Dù tôi chưa từng nằm mơ thấy nó\\nlại thành hình một cách trực tiếp đến mức này」"
1315 = "「Vết thương sẽ đau, cảm giác tội lỗi không thể xóa nhòa.\\nDù vậy, tôi――rất hạnh phúc vì được gặp em」"
1328 = "「Hachiroku…… tôi」"
1333 = "「Nghe tôi nói này, Hachiroku」"
1340 = "「Hachiroku. Tôi sẽ công nhận điều đó」"
1343 = "「Tôi thì. Hachiroku. Hơn cả sự vững tâm hay bất cứ điều gì.\\nChỉ cần có em ở bên, tôi thấy rất vui」"
1377 = "「Nếu có em ở bên cạnh, làm gì tôi cũng thấy vững tâm」"
1398 = "「Chà, sao nhỉ. Tuân theo lệnh của bố nuôi――\\nCó thể tôi sẽ bị đưa đi nơi khác, cũng có thể bị giữ lại đây」"
1418 = "「Ừ. Tôi cũng vậy.\\nĐương nhiên, ở đó, quá khứ hay gì đi nữa, hoàn toàn không liên quan」"
1451 = "「Nếu muốn chọn, lẽ ra ông ấy có thể chọn bất cứ phương tiện nào.\\nVậy tại sao, ông Taito lại――chọn [8620'86], một toa xe gặp tai nạn」"
1454 = "「Nếu không gặp nhau, tôi đã không thể biết đến em.\\nTai nạn, và quá khứ――tôi đã không thể đối mặt đến mức này」"
1457 = "「Nếu có Michiko ở đây thì có thể bàn bạc…… Không, vốn dĩ nếu có Michiko,\\nthì chuyện gặp gỡ Hachiroku đã――Ư!」"
1468 = "「Tôi cũng, em――」"
1469 = "「Càng tìm hiểu về lịch sử đường sắt, tôi càng thấy kỳ lạ.\\nTại sao, ông Taito lại nhận nuôi [8620'86] và em」"
1484 = "「Từ lúc gặp nhau――đến tận khoảnh khắc này. Được ở cùng Hachiroku.\\nĐược cùng nhau nỗ lực hết mình, tôi thấy rất hạnh phúc và vui vẻ」"
1487 = "「Sao vậy, Hachiroku――Ư!?」"
1497 = "「Phải làm sao để không ai phải chịu chung vết thương đó nữa.\\nTôi nghĩ đó là――điều tốt nhất mà những người sống sót có thể làm」"
1518 = "「Thế nên, Hachiroku. Từ nay về sau, hãy ở bên cạnh tôi nhé」"
1522 = "「Nhưng, ta có thể lấy quá khứ làm bài học để tiến về phía trước.\\nTôi đã được dạy như thế, và tôi vẫn luôn làm như vậy」"
1524 = "「Và, nhận nuôi cả tôi nữa.\\nNói cách khác là…… những nạn nhân của vụ tai nạn đó」"
1562 = "「Về mặt chi phí, ông Taito đã cố tình phớt lờ.\\nThậm chí phải vay nợ để đưa em, và \\x%l8620;#00ffc040;8620%l;#; về Ohitoyo――」"
1580 = "「Đứa trẻ đó giờ đã không còn là [8620'86] của tôi nữa――\\nmà đã trở thành \\x%l8620;#00ffc040;8620%l;#; của Ohitoyo rồi」"
1604 = "「Dù vậy, quả nhiên……\\nlà để tôi bình tĩnh lại. Chắc cũng có ý nghĩa đó nữa」"
1605 = "「Ngốc nghếch. Tôi sẽ không cho phép chuyện đó xảy ra đâu」"
1629 = "「Nơi này đúng là, chỗ dành cho những người trẻ như tôi làm」"
1654 = "「Nếu vậy, em sẽ được tự do.\\nKhi được tự do rồi, em muốn làm gì, hãy nói cho tôi nghe」"
1661 = "「Ngài Soutetsu――Ư!?」"
1666 = "「Ngài Soutetsu, xin hãy cẩn thận.\\nTôi không thể hỗ trợ ngài trong khu vực \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động đâu ạ」"
1676 = "「Ư!」"
1677 = "「Ư!!!」"
1678 = "「Ư!!?」"
1679 = "「Ư!?」"
2016 = "Hachiroku, nín thở cái thót.\\nEm ấy chịu lắng nghe tôi nói――nghĩ vậy, lời nói cũng thêm phần mạnh mẽ."
2085 = "Khi quyết định cứu Hachiroku.\\nKhi tự mình lựa chọn trở thành \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#;, vào lúc đó."
2156 = "Dù cho cuối thời \\x%l帝鉄;#00ffc040;Teitetsu%l;#; tai nạn đường sắt có xảy ra nhiều đến đâu,\\nthì vụ đó chắc chắn…… cũng là một trường hợp cực kỳ hiếm gặp."
2208 = "Không hiểu sao tôi lại thấy xấu hổ vô cùng,\\nbất giác quay lưng lại――Ư!"
2235 = "Điều đó có thực sự là tốt nhất cho Ohitoyo hay không,\\ntôi không còn biết nữa."
2305 = "Chia tay Navi,\\ntôi bước vào khu vực \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động."
2316 = "Vì vậy,\\ntôi muốn trực tiếp giải quyết khiếu nại và xin lỗi với tư cách là \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#;."
2350 = "Ông Taito từng làm việc cho \\x%l帝鉄;#00ffc040;Teitetsu%l;#;,\\nhẳn phải lường trước được cần bao nhiêu vốn liếng để cải tạo chứ."
2464 = "Biết được \\x%l8620;#00ffc040;8620%l;#; là toa xe gặp tai nạn,\\nbiết được Hachiroku là \\x%lレイルロオド;#00ffc040;Railord%l;#; đã gây ra tai nạn đường sắt."
2514 = "Nếu rơi xuống dòng sông đang cuồn cuộn vì bão――\\nNhân viên tàu, hành khách, tất cả đều sẽ bỏ mạng."
2584 = "Cơn mưa từng răn đe tôi,\\nnhư thể đã được cơn mưa của Ohitoyo gột rửa sạch sẽ."
2607 = "Rượu Kuma Shochu,\\nkhông chỉ đại diện cho Ohitoyo, mà còn là Kumamoto, là Kyushu."
2617 = "Điện là \\x%lエアクラ;#00ffc040;Aircra%l;#;, đèn dầu là đường sắt.\\nChắc có lẽ em ấy đã hiểu được ẩn ý đó."
```

## Kết bài

File ハチロク07_ハチロクの目覚め.txt.toml: 424 dòng đã đọc hết (231 độc thoại, 193 thoại), **56 dòng sai (13,2%)** — đại từ 29 (Soutetsu "anh"/"mình" → "tôi" với Hachiroku), thuật ngữ 17 (Ohigawa→Ohitoyo 6, Aerocraft→Aircra 3, 事故車輌 3, 帝鉄 2, 機関士 2, 乗員 1), gasp 8 (sweep áp nguyên), SFX 1, typo 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. JSON + khối TOML đã kiểm chứng parse, 0 sai lệch; lượt soát 2: 56/56, 0 bỏ, 0 sửa. Cờ cho Hieu: ghi chú 2679/2596 không khớp file (§5); 1507 người nghe suy ra là Navi. Cơ sở tổng đã rebase theo ROUTE-AUDIT.md hiện tại (143 file / 6.463 dòng sai).

## Parent kiểm chứng (21/11 ~08:50)

- Parent kiểm chứng 21/11 ~08:50: JSON 56 mục dạng chuẩn, khóa chuỗi; khối TOML 56 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 56/56; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (trừ 1468 bỏ "xem" bịa + đổi đại từ, và 5 dòng gasp thay toàn bộ dấu câu); \n giữ nguyên 56/56; lượt soát 2: 56/56, 0 bỏ, 0 sửa. Đại từ kiểm chứng theo dòng kề: cả 29 fix đều nằm trong mạch thoại trực tiếp Soutetsu↔Hachiroku (nhiều dòng gọi tên/xưng お前 với Hachiroku: 1026, 1328, 1333, 1340, 1343, 1484, 1518); "anh" còn lại chỉ 1037/1288 (lời Paulette, khóa B4); "mình" còn lại chỉ 1508 (tự lẩm bẩm) + phản thân/thành ngữ. Thuật ngữ spot-check 10/10 khớp JP/TW (Ohigawa, Aerocraft, 事故車輌, 帝鉄, 機関士, 乗員 2514, 1468, SFX 32, typo 2016). Không sửa nào bị loại. GIẢI QUYẾT ghi chú 2679/2596: thuộc file ハチロク07_延命 (đã gộp, 64 fix) — key 2679 đã sửa "ông nội"→"ông ngoại" trong audit đó theo nhóm 2596 堰さんたち cùng file; không có key 2679 nào với 堰 trong toàn CSV3; file 目覚め không có dòng Seki nào cần sửa (2094/2588 đã đúng). Chờ Hieu: 1507 người nghe suy ra là Navi (cần xác nhận khi chơi tới đoạn này); B19 vẫn park.
