# REVIEW — Unification U14b: §7 OPEN O20–O37 (pronoun/addressee, group B)

- Batch: **U14b** — `unification-s7-open-pronouns-b`
- Items: **O20–O37** (18 mục, §7 UNIFICATION-LIST.md)
- Fix list: `unification-s7-open-pronouns-b-wrong.json` — **14 dòng, 8 file**
- Items có dòng sửa: **8** (O21, O22, O24, O25, O26, O31, O34, O35) · Items 0 dòng (giữ nguyên có lý do): **10** (O20, O23, O27, O28, O29, O30, O32, O33, O36, O37)
- Cơ sở rebase: chuỗi hiện tại **100 mục / 2.686 dòng** (queue.json, U13b đã gộp 22/11 ~13:00; U14a song song chưa gộp) → sau đợt này **108 mục / 2.700 dòng** (xem snippet)

## §1. Phạm vi + phương pháp

- Đọc §7 O20–O37 (toàn §7 để lấy ngữ cảnh), UNIFICATION-BRIEF.md, AUDIT-BRIEF.md, MOAN-BRIEF.md, LOGIC-DICH-VA-SUA.md (master của Hieu), MEMORY.md (quyết định 19–22/11), ROUTE-UNIFICATION.md (quyết định coordinator E2/F1/F5, quy tắc ひゃ-family, quy tắc đại từ).
- Nguồn số liệu: CSV3 good-set **87.833 dòng** (đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`); map old_vn = unification (gộp sau thắng, theo thứ tự gộp trong queue) > moan (1.516) > audit (9.139) > CSV3 VN. Map unification: 2.585 (file,key) duy nhất từ 21 file `unification-*-wrong.json` đã gộp (tính đến U13b).
- Mỗi dòng ứng viên đều đọc JP (+TW) và 3–8 dòng kề **theo thứ tự dòng của CSV3 (script order)**. Key số KHÔNG phải thứ tự cảnh — mọi kết luận người nghe trong đợt này đều dựa trên file-order + nội dung đối thoại, không dựa trên key-order (bài học U14a O17/O18).
- Quy tắc áp dụng: đại từ theo **NGƯỜI NGHE**, không theo người được nhắc tới (P1); nhóm hỗn hợp → "tôi" (tiền lệ Paulette 14 key 1544, Grand 02 key 1493); P9 Fukami/Nagi cùng tuổi — Nagi → Fukami "bé", Fukami tự xưng "mình" (ngoại lệ 凪ふかみ07 "tớ"), Fukami → Nagi "cậu" (không "em", không "chị"); JP thắng TW; không bịa phần hoàn thiện cho JP cụt (tiền lệ Hibiki h5 1189); không đụng dòng gasp Ư hay dòng "Kh" (không có dòng nào trong đợt này thuộc hai loại đó, trừ O37-2038 đã xét và giữ theo tiền lệ 1042); không sửa lại dòng đã đúng.
- Hiệu chỉnh trích dẫn trong list (ghi lại để coordinator sửa list): O29 key 1877 thuộc **日々姫06_みくろ、来訪** (không phải ハチロク10 — cả hai file ハチロク10 đều không có key 1877); O35 key 2484 thuộc **真闇03_ひとしずく** (không phải 真闇01); O37 key 1928/2038 thuộc **日々姫05_御一夜ステーションカフェ** (không phải ハチロク14_冬); O25 key 2368/2607 thuộc **日々姫03_客車手配** (không phải lr h1 — cả hai file h1 đều không có hai key này); O32 key 1352/1423 và O36 key 2038 **không tồn tại** trong TOML lẫn CSV3 (void).

## §2. Quyết định từng mục OPEN (theo uỷ quyền của Hieu)

### O20. Hachiroku → Hibiki "chị" (仲国01 1377) vs "cô" (file 06) — GIỮ "chị", 0 dòng
- **1377 GIỮ "chị".** Đếm toàn dự án (dòng Hachiroku nói, dạng xưng hô có tên): "chị Hibiki" **12 dòng** (8 "chị" + 4 "Chị") ở 共通07/08/15, ハチロク06 — trong đó gọi TRỰC TIẾP ít nhất 5 dòng (共通08 1828 "Vâng. Có chuyện gì vậy, chị Hibiki."; 1946 "Chị Hibiki. Để chị đợi lâu rồi. Em gội đầu sạch sẽ rồi ạ."; 共通15 2157 "Tất nhiên rồi ạ, chị Hibiki."; ハチロク06 1920 "Cảm ơn chị, chị Hibiki."; 1776 "Chị Hibiki mới đúng――sao chị lại ở đây?") — tự xưng "em" đi kèm. Dạng "cô" CHỈ xuất hiện trong **một file duy nhất 共通06 (cảnh tắm)**: 1954 "Cô xem, em nhỏ bé thế này mà?", 2225 "Cô cứ gọi trống không là được rồi, tiểu thư Hibiki.", 2393 "Hơn nữa, cô biết không? Hibiki." — cộng 1 dòng ngôi thứ ba 共通03 1661 "cô Hibiki" (nói VỚI Soutetsu VỀ Hibiki). Chuẩn toàn dự án là "chị"; "cô" ở file 06 là register trang trọng riêng của cảnh tắm, đã khóa giữ theo P16 — là ngoại lệ, không phải chuẩn. 1377 ("Em viết xong rồi… Em kiểm tra giúp chị được không?") khớp chuẩn "em/chị" → giữ.
- Đối chứng chiều ngược: Hibiki → Hachiroku là "chị" (共通06 2460 fix audit: "chị cứ gọi em là Hibiki đi").

### O21. Nagi → Hachiroku (凪ふかみ05) — 1 dòng sửa
- **2679 SỬA "cô" → "chị".** Nagi: 「お、お願いするとばい」 — Hachiroku vừa nói 「さ、髪を」 (1973, "Nào, để tôi chải tóc cho"), Nagi đáp "nhờ…" — người nghe chắc chắn là Hachiroku. JP KHÔNG có đại từ nào (TW 麻煩你咧 — "phiền bạn"); "cô" trong VN là thêm vào. Chuẩn xưng hô có tên: "chị Hachiroku" **3 dòng, 0 dòng "cô Hachiroku"** (1981 cùng file; グランドリライト08 1264/1663). Fukami cùng tuổi cũng gọi "chị Hachiroku". 2667 "cô giáo Hachiroku" là danh xưng nghề giáo viên, không phải đại từ xưng hô — không tính. **1981 GIỮ "chị Hachiroku"** ("Em, được chị Hachiroku, chỉnh t-t-tóc cho, ạ——đấy!").
- Lưu ý: Hachiroku → Nagi 2107 VN thêm "cô" ("tóc cô mềm…") dù JP không có đại từ — đó là chiều ngược, không thuộc O21, không sửa.

### O22. 凪ふかみ08c 2030 — 1 dòng sửa
- **2030 SỬA "anh" → "tôi".** Soutetsu: 「うむっ――まぁ、それは確かにだ。いかんな、僕が足を引っ張ってしまったか」 — đáp trực tiếp lời quở của Hachiroku ở 2554 (cô gọi anh 双鉄様, nhắc trách nhiệm chủ nhà/đội). P1: Soutetsu → Hachiroku = "tôi". Key 2029 (cảnh nước/teamwork) là cảnh khác, không phải người nghe ở đây. Ghi chú: list nói parent đã gỡ một fix cũ và giữ "anh" chờ Hieu — đợt này quyết lại SỬA theo uỷ quyền + bằng chứng dòng kề (cờ F-O22-1 để coordinator xác nhận việc đảo quyết cũ).

### O23. 凪ふかみ04 — GIỮ TOÀN BỘ, 0 dòng
- **2294 GIỮ "em"** (Fukami tự xưng; đang cõng trên lưng Soutetsu; độc thoại 3280 "双鉄お兄さんが笑う" xác nhận ngữ cảnh). **2296/2407 GIỮ "em"** (Fukami tự xưng với Hibiki + Paulette: 2075 Hibiki hỏi, 2544 Paulette hỏi). **2309 GIỮ "em"** ("V, vâng! Nhờ em nhé, ạ" — "em" = Reina: Reina gọi Fukami "chị Fukami" 2285; Fukami gọi Reina "em" 2571). **2393 GIỮ "chị"** ("Chị xin phép——ưm..." — Fukami tự xưng "chị" với Reina, JP không có đại từ; Reina gọi cô là chị). **2174 GIỮ "Em đợi anh nhaaaa!"** (Nagi → Soutetsu, đúng P1).

### O24. 凪ふかみ01_凪の成長、ふかみの成長 — 1 dòng sửa
- **1955 SỬA "Anh cảm giác" → "Tôi cảm giác".** Soutetsu nói với Hachiroku: 1772 cô mời ("はい、なんでしょう、双鉄様"), 1670 cô đáp — người nghe là Hachiroku → "tôi" (P1). Chỉ đổi đại từ; giữ nguyên toàn bộ fix audit còn lại ("Minh Quốc", gloss %l 蒸機 → "đầu máy hơi nước"). old_vn nguồn audit.
- **1517 GIỮ "em".** Nagi đáp lời khen của Hachiroku (1796) — người nghe là Hachiroku, KHÔNG phải Fukami như list ghi. **1884 KHÔNG SỬA — cờ cho U14c/O64** (じーちゃん "Ông nội cũng hay nhận làm thầu khoán mà!"; xem §6 F-O24-1).

### O25. lr_凪ふかみh1_じぇいけい！ — 3 dòng sửa
- **1620 SỬA "Chị" → "Tớ"** (Fukami: 「ええ！？ そんなことしてないよぉ――えと」). **1672 SỬA "Chị" → "Tớ", "em" → "cậu"** (Fukami dặn Nagi: 「…凪ちゃん、まずは――うん、双鉄お兄さんの、亀頭だけパクってしてあげて？」). **1744 SỬA "em" → "cậu", "chị" → "tớ"** (Fukami dọa Nagi: 「凪ちゃん？ おねだりできないんなら。わたし、おちんちん横取りしちゃうよ？」). Chuẩn P9 đã khóa: Fukami tự xưng KHÔNG bao giờ "chị", Fukami → Nagi KHÔNG bao giờ "em"; dạng đúng trong chính file này là **1746 "tớ"/"cậu"** (「凪ちゃん、凪ちゃん。逆に、わたしも舐め取ってあげる。」) — ba dòng sửa thống nhất về dạng đó.
- **GIỮ 1708/1825 "anh"** (Soutetsu đối thoại, có 「」; 1857 Nagi đáp) và **1746 "tớ"/"cậu"** (dòng chuẩn). **Cờ F-O25-1:** cùng lỗi P9 ở 1616 (Fukami "Em hiểu rồi"), 1687/1737 (Fukami → Nagi "em": "Ufufu, em nói giỏi lắm" / "Nagi, em muốn sao nào?") — KHÔNG có tên trong O25 nên không sửa ở đây (xem §6). **2368/2607 KHÔNG thuộc file này** (cả hai file h1 đều không có hai key) — thực tế là 日々姫03_客車手配, cờ cho U14c/O64 (xem §6 F-O25-2).

### O26. ハチロク08_台枠問題 — 3 dòng sửa
- **1896 SỬA "Anh muốn" → "Tôi muốn".** Bữa trưa nhóm (Hibiki + Hachiroku + Paulette cùng có mặt): 「すまんが、食事は中断してくれ。すぐ、検討をしたいのだ」 — địa chỉ nhóm có Hachiroku → "tôi" (P17).
- **2398 SỬA "Anh đang nghĩ" → "Tôi đang nghĩ".** Thảo luận nhóm: 「そう出来ればと考えている。条件の合うような機体がもしもあれば、だが」 (2368 Paulette đáp) → "tôi" (P17).
- **2023 SỬA — cắt phần hoàn thiện bịa thêm.** JP trích dẫn cụt ở 「日ノ本の鉄路に8620の――」 nhưng VN hoàn thiện thành "không nơi nào là không thấy" — phần đó thực chất là lời nối của Hachiroku ở 1587 (「――機影、見えざるは無し」, audit đã sửa). Fix giữ đúng điểm cụt: 『Trên đường sắt Hinomoto, 8620——』 (quy tắc không bịa, tiền lệ Hibiki h5 1189).

### O27. ハチロク10_炙り出し 1825 — GIỮ, 0 dòng
- **1825 GIỮ "tôi".** "Nếu loại Giáp đã như vậy, thì loại Ất chắc chắn cũng có giá trị của nó. Đương nhiên, tôi cũng định sẽ chụp lại toàn bộ quá trình vận chuyển và bảo dưỡng." — địa chỉ nhóm, Hachiroku có mặt và tham gia (1769 cô hỏi tiếp, 2324 cô vỗ tay) → "tôi" đúng (P17). Ranh giới: nếu coordinator không đồng ý thì chỉ là lật 1 từ "tôi" → "anh".

### O28. ハチロク07_ハチロクの目覚め 1507 — GIỮ, 0 dòng
- **1507 GIỮ "cô".** Người nghe là **Navi — xác định được từ chữ, KHÔNG cần check in-game**: 1666 Navi "Ngài Soutetsu, xin hãy cẩn thận…", 1523 Navi "Tôi đã hiểu ạ", 2305 độc thoại "Chia tay Navi, tôi bước vào khu vực Aircra không thể hoạt động". Soutetsu: 「帰りは、逆側に出るのでよろしく頼む」 → "Lúc về tôi sẽ ra ở phía bên kia, nhờ cô nhé" — "cô" là chuẩn đã khóa cho Navi: お前 → "cô" (共通01 1425 "Đính chính lại đi. Cô——Navi,…"; 1461 "Navi. Cô cũng là đồng loại của Aircra…"; 1308 "một Navi xuất sắc như cô"; 1181 お前たち → "Các cô").

### O29. Key 1877 — GIỮ, 0 dòng (file đã hiệu chỉnh)
- Key 1877 **không có** trong cả hai file ハチロク10 (TOML lẫn CSV3); dòng thật thuộc **日々姫06_みくろ、来訪 1877**. Soutetsu: 「なんと、みくろか！ 御一夜まで尋ねてきてくれたのか」 — VN (old_vn = unif U1a): "Gì chứ, là Mikuro sao! Cô ấy cất công đến tận Ohitoyo tìm tôi à." — người nghe là **職員Ａ**: toàn cảnh là đối thoại với Staff A (2200/2317/2121/1899/2216/2136/2132/2143/2258); Soutetsu gọi Staff A "cậu", tự xưng "tôi" (1899/2136/2143) → "tìm tôi" đúng. Parent đã xác nhận "1877 uncertain giữ nguyên, không tính sai" (ROUTE-AUDIT 日々姫06).

### O30. ハチロク07_延命 2339 — GIỮ, 0 dòng
- **2339 GIỮ "chị…em".** Fukami: 「あ！ それいい！！ なら、わたしはともはりして、あと、川遊び！ 川遊びの仕方も教えてあげる！" — người nghe là **Olivy**: 2393 Nagi mời Olivy chơi sông Kuma, 2702 Olivy đáp; Nagi đã biết chơi sông từ trước nên người được dạy là Olivy → Fukami "chị", Olivy "em" đúng.

### O31. ハチロク02_8620運転台通信 — 2 dòng sửa
- **1952 SỬA "anh cũng nghĩ" → "tôi cũng nghĩ".** Soutetsu ↔ Hachiroku bàn kế hoạch (1963 Soutetsu, 1893/2022 Hachiroku, 1940 Hachiroku): 「そうだな、そういう感じがいいと僕も考えた。興味を引きそうなエピソードを、説明につなげていく」 → "tôi" (P1). Lưu ý: ハートブレイク 1952 là dòng khác (Hibiki nói, không có đại từ) — không phải dòng đích.
- **2049 SỬA "Chào em." → "Chào hai người."** Fukami: 「こんにちわ。あ、これ、おふたりにお福分け。です" — おふたり = **Reina + Paulette**: 1845 Reina chào Nagi + Fukami, 1859 Reina cảm ơn "hai chị", 2063 Paulette hỏi về món quà. "Chào em" số ít sai (Paulette lớn tuổi hơn); phần còn lại của dòng đã nói "hai người" nên "Chào hai người." nhất quán.

### O32. 日々姫h1_マッサージの続き — GIỮ, 0 dòng (tiền đề list sai + "Kua vs Hự" đã có quyết F1)
- **1352/1423 VOID** — không có trong TOML lẫn CSV3. **1421/1447 GIỮ "tôi"** — cả hai đều là **độc thoại của Soutetsu** (char=monologue, JP 僕): 1421 「さらに奥で、口の全部で、僕を包もうとしてくれているのだろう。」 / 1447 「それがまたどろどろとした塊となり、僕の精巣に流れ込んでは、精液を一気に押し上げる。」 Tiền đề "Paulette 'tôi'" của list là SAI — file này chỉ có 3 loại nhân vật (monologue/日々姫/双鉄H), **không có Paulette**; Soutetsu "anh" với Hibiki đúng toàn file (quét máy 65 dòng 双鉄H: 0 dòng "tôi"), độc thoại dùng "tôi" xuyên suốt (ROUTE-AUDIT 日々姫h1).
- **"Kua vs Hự" đã quyết bởi F1/M7 (U12a áp dụng):** 1010/1052 「くあっ！" → **"Kua!" GIỮ** (くあっ ≠ くっ, M7 không bao phủ; diễn đúng mora); 1062 「ンッ――くっ" → "Ưm——hự." và 1041/1043/1044 (Hibiki) → "Hự" **GIỮ theo F1** — 日々姫h1 là 1 trong 4 file convention giữ "Hự" (cùng lr_ふかみh2, lrれいな追加h, ハチロクh2 — 12 dòng). 0 dòng mới.

### O33. lrれいな追加02_花嫁修業の先生たち — GIỮ cả hai, 0 dòng
- **1505 GIỮ "anh".** Soutetsu: "…Anh cảm thấy rằng, lễ nghi chính là sự tích lũy của những điều như vậy." — người nghe **Reina** (nối tiếp 1422 của cô; cô đáp 1286 "Nghe anh nói vậy thì đúng là thế thật") → "anh" đúng P1.
- **1637 GIỮ "của anh".** Soutetsu: "Bông hoa thay cho khăn cài túi áo ngực của anh,…" — nói với **Hibiki** (1395 "cái này——dành cho anh hai!") → "của anh" đúng.
- Cờ (không sửa): 1635 "Còn tôi là chồng của Reina mà." — nhóm hỗn hợp (Kisaki có mặt với vai giáo viên), "tôi" biện hộ được theo P17; để nguyên (xem §6 F-O33-1).

### O34. れいな03_しゅっぱつしんこう — 2 dòng sửa
- **1386 SỬA "tôi hơi choáng váng" → "em hơi choáng váng".** Paulette đáp Soutetsu 1626 ("Pa, Paulette!? Cô sao vậy!" — audit đã sửa thành "Em sao vậy!"): 「はっ！？ い、いえ、あまりにも衝撃的で、一瞬、クラっと" — Paulette → Soutetsu tự xưng "em" (cf. 1547 audit "Em cũng vui lắm").
- **1644 SỬA "tôi sẽ nhận" → "em sẽ nhận".** Paulette nói với Soutetsu: 「れいなに戸籍だけ必要になりますから――そこは、わたしの養女に入ってもらいます" — 1691 Soutetsu đáp "Cảm ơn em. Anh rất vui." (audit) xác nhận cặp "em/anh".

### O35. Key 2484 — 1 dòng sửa (file đã hiệu chỉnh)
- **2484 SỬA "em ấy" → "chị ấy" — file đúng 真闇03_ひとしずく** (list ghi 真闇01 là sai). Độc thoại: 「だから……聞いてみたくなる。酷かことかも、知れんけど。" **Người nghĩ là Hibiki**: các độc thoại kề đều là góc nhìn Hibiki (2451/2253 disp=日日姬; 2711/2451/2348 nhắc にぃに); ngay sau đó 1548 Hibiki hỏi thẳng Hachiroku: 「ハチロクは――これで、良かったと？" — "người ấy" chính là Hachiroku, và TW "她的想法" (suy nghĩ của CÔ ẤY) xác nhận ngôi thứ ba nữ. Hibiki → Hachiroku = "chị" toàn dự án → "hỏi chị ấy". Ghi chú: parent từng cờ "2484 'hỏi em ấy' GIỮ — người nghĩ chưa xác định" (ROUTE-AUDIT 真闇03) — đợt này xác định được người nghĩ là Hibiki từ disp + dòng kề nên quyết SỬA.

### O36. 真闇03_ひとしずく — GIỮ, 0 dòng
- **2038 VOID** — không có trong CSV3 lẫn TOML. **1999 GIỮ fix audit "anh".** VN hiện tại: "Navi á? A……Ra vậy―― Có lẽ anh thuộc tuýp người dễ đoán quá nhỉ." — người nghe là **Hibiki** (1994–1995 Hibiki đáp; 1686–1689 nói VỀ Mayami ở ngôi thứ ba nên người nghe không phải Mayami); parent đã xác minh trong ROUTE-AUDIT. (Ghi chú nguyên văn của parent: "1999 'ナビ' = Hibiki" — giữ lại như đã ghi; Fukami 1964 nhắc ナビさん, Soutetsu đáp 「ナビが？".)

### O37. ハチロク14_冬 (+ 日々姫05) — GIỮ, 0 dòng
- **3202 GIỮ fix audit.** Paulette: "Vậy, tôi giao phó cho anh...." — người nghe Soutetsu đã xác nhận (3143 Paulette giao việc cho anh với vai trò trưởng vận chuyển/bảo trì; 3024 Soutetsu hỏi; 2613 Paulette đáp; 2906 Soutetsu "Tôi đã tiếp nhận.").
- **2590 GIỮ fix audit.** Olivy ＆ Hachiroku: JP 「っ" + 「っっっ！！！？" (1+3 っ), TW 「嗚" + 「嗚嗚！！！？" (1+2) — fix audit 「Ư" + "Ưưư!!!?" diễn đủ cả 4 っ của JP; JP thắng TW.
- **1928 GIỮ "chú" (file đúng 日々姫05_御一夜ステーションカフェ).** Soutetsu: 「いえ、こちらこそ失礼しました" — người nghe là **đứa trẻ khách hàng** (ちびっこ 2229 "ごめんなさぁい" xin lỗi; độc thoại 1445: bọn trẻ chạy lăng xăng va vào anh, khay nghiêng) — Soutetsu xưng "chú" với trẻ nhỏ là tự nhiên, đúng. Audit cờ "người nghe không xác định chắc chắn" nay đã giải quyết bằng dòng kề.
- **2038 GIỮ (file đúng 日々姫05).** Soutetsu: 「おわっ！？ っ――あ。すみません" → "Oái!? ——A. Xin lỗi." — っ trước gạch ngang đã được gạch diễn tiếng ngắt (tiền lệ 日々姫h1 1042 đã khóa: "っ trước gạch ngang thì gạch đã diễn tiếng ngắt"); あ → "A". Không còn gì để diễn thêm; không thêm "Ư" (quy tắc gasp: Ư CHỈ khi っ hoàn toàn mất hẳn).

## §3. Danh sách sửa (14 dòng / 8 file)

### 凪ふかみ05_凪の開眼！？.txt.toml — O21 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2679 | 「お、お願いするとばい」 | 「麻、麻煩你咧」 | 「N... nhờ cô nha.」 | 「N... nhờ chị nha.」 | Nagi → Hachiroku "chị" (chuẩn "chị Hachiroku" ×3: 1981 cùng file, Grand08 1264/1663; 0× "cô Hachiroku"); JP không có đại từ, "cô" là thêm vào. |

### 凪ふかみ08c_新しい家族.txt.toml — O22 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2030 | 「うむっ――まぁ、それは確かにだ。
いかんな、僕が足を引っ張ってしまったか」 | 「唔……嗯，沒錯。不行啊，我居然拖後腿了」 | 「Ưm――chà, điều đó thì đúng thật.
Không được rồi, là anh đã ngáng chân mọi người sao.」 | 「Ưm――chà, điều đó thì đúng thật.
Không được rồi, là tôi đã ngáng chân mọi người sao.」 | Soutetsu → Hachiroku "tôi" (P1); đáp trực tiếp lời quở của Hachiroku 2554 (gọi 双鉄様, trách nhiệm chủ nhà). |

### 凪ふかみ01_凪の成長、ふかみの成長.txt.toml — O24 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1955 | 「冥国式に作られた車両は、海外には売れん気がする。
が、実際、日ノ本にも冥国出身の輸入\x%l蒸機;#00ffc040;蒸機%l;#;は多いよな？」 | 「這樣的話，感覺美國造的車輛沒辦法出口海外啊。可是日本的確有很多從美國進口的\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;」 | 「Anh cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.
Nhưng thực tế, ở Hinomoto cũng có rất nhiều \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」 | 「Tôi cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.
Nhưng thực tế, ở Hinomoto cũng có rất nhiều \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」 | Soutetsu → Hachiroku "tôi" (P1; 1772 cô mời anh hỏi, 1670 cô đáp); chỉ đổi đại từ, giữ nguyên fix audit (Minh Quốc + gloss %l). |

### lr_凪ふかみh1_じぇいけい！.txt.toml — O25 (3 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1620 | 「ええ！？ そんなことしてないよぉ――えと」 | 「啊？沒有的吧……我看看」 | 「Hả!? Chị có làm thế đâu——ưm」 | 「Hả!? Tớ có làm thế đâu——ưm」 | Fukami tự xưng "tớ" (P9; khớp 1746 cùng file "tớ"/"cậu"). |
| 1672 | 「うん。わかった。それじゃ凪ちゃん、まずは――
うん、双鉄お兄さんの、亀頭だけパクってしてあげて？」 | 「嗯，好的，那麼小凪，首先……嗯，把雙鐵哥哥的龜頭含住吧」 | 「Ừm. Chị hiểu rồi. Vậy thì Nagi, trước tiên——
ừm, em ngậm lấy mỗi quy đầu của anh Soutetsu đi?」 | 「Ừm. Tớ hiểu rồi. Vậy thì Nagi, trước tiên——
ừm, cậu ngậm lấy mỗi quy đầu của anh Soutetsu đi?」 | Fukami tự xưng "tớ", Fukami → Nagi "cậu" (P9; khớp 1746). |
| 1744 | 「凪ちゃん？ おねだりできないんなら。
わたし、おちんちん横取りしちゃうよ？」 | 「小凪，如果你不開口求，那我就要搶走雞雞了哦」 | 「Nagi? Nếu em không nũng nịu được.
Thì chị sẽ cướp mất cậu nhỏ đấy nhé?」 | 「Nagi? Nếu cậu không nũng nịu được.
Thì tớ sẽ cướp mất cậu nhỏ đấy nhé?」 | Fukami → Nagi "cậu", tự xưng "tớ" (P9; khớp 1746). |

### ハチロク08_台枠問題.txt.toml — O26 (3 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1896 | 「すまんが、食事は中断してくれ。
すぐ、検討をしたいのだ」 | 「不好意思，吃飯的事先放一放。現在需要立刻展開討論」 | 「Xin lỗi, nhưng tạm dừng bữa ăn đã.
Anh muốn thảo luận ngay bây giờ.」 | 「Xin lỗi, nhưng tạm dừng bữa ăn đã.
Tôi muốn thảo luận ngay bây giờ.」 | Địa chỉ nhóm (Hibiki + Hachiroku + Paulette) → "tôi" (P17). |
| 2023 | 「うむ。聞いているし、本でも読んだ。
『[ひのもと,2]日ノ本の[てつろ,1]鉄路に[ハチロクニイマル,3]8620の――』」 | 「唔。不僅聽過，我在書上也看過。“但得日本鐵路——”」 | 「Ừm. Tôi có nghe rồi, cũng từng đọc trong sách nữa.
『Trên đường sắt Hinomoto, không nơi nào là không thấy——』」 | 「Ừm. Tôi có nghe rồi, cũng từng đọc trong sách nữa.
『Trên đường sắt Hinomoto, 8620——』」 | JP cụt ở 「8620の――」 — bỏ phần hoàn thiện bịa thêm (phần đó là lời nối của Hachiroku 1587, audit đã sửa); giữ đúng điểm cụt (quy tắc không bịa). |
| 2398 | 「そう出来ればと考えている。
条件の合うような機体がもしもあれば、だが」 | 「若是有符合條件的車體的話，應該可行，但是……」 | 「Anh đang nghĩ nếu làm được như vậy.
Nhưng mà, giả sử có cỗ máy nào phù hợp với điều kiện đó không đã.」 | 「Tôi đang nghĩ nếu làm được như vậy.
Nhưng mà, giả sử có cỗ máy nào phù hợp với điều kiện đó không đã.」 | Địa chỉ nhóm (thảo luận chung; Paulette đáp 2368) → "tôi" (P17). |

### ハチロク02_8620運転台通信.txt.toml — O31 (2 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1952 | 「そうだな、そういう感じがいいと僕も考えた。
興味を引きそうなエピソードを、説明につなげていく」 | 「對啊，我也覺得這樣不錯。還可以往中間加入一些有趣的小插話，用以銜接以後的說明」 | 「Đúng vậy, anh cũng nghĩ làm theo hướng đó sẽ rất hay.
Kết nối những câu chuyện thú vị vào phần giải thích.」 | 「Đúng vậy, tôi cũng nghĩ làm theo hướng đó sẽ rất hay.
Kết nối những câu chuyện thú vị vào phần giải thích.」 | Soutetsu ↔ Hachiroku bàn kế hoạch (1963/1893/2022/1940) → "tôi" (P1). |
| 2049 | 「こんにちわ。
あ、これ、おふたりにお福分け。です」 | 「早安。啊，這個是，分給你們兩個人的禮物。嗯」 | 「Chào em.
A, cái này, là quà lộc cho hai người. ạ.」 | 「Chào hai người.
A, cái này, là quà lộc cho hai người. ạ.」 | おふたり = Reina + Paulette (hai người) — "Chào em" số ít sai; 1845/1859/2063 xác nhận. |

### れいな03_しゅっぱつしんこう.txt.toml — O34 (2 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1386 | 「はっ！？ い、いえ、あまりにも衝撃的で、
一瞬、クラっと」 | 「哈！？不，不，衝擊性實在是太強了，我腦袋裡一片空白了」 | 「Hả!? Kh-Không, vì quá sốc,
nên trong chốc lát, tôi hơi choáng váng.」 | 「Hả!? Kh-Không, vì quá sốc,
nên trong chốc lát, em hơi choáng váng.」 | Paulette → Soutetsu "em" (đáp 1626 "Em sao vậy!" audit; cf. 1547 "Em cũng vui lắm"). |
| 1644 | 「れいなに戸籍だけ必要になりますから――
そこは、わたしの養女に入ってもらいます」 | 「玲奈只需要一個戶籍——她只要登記為我的養女就行了」 | 「Chỉ cần làm hộ khẩu cho Reina thôi――
Việc đó thì, tôi sẽ nhận em ấy làm con nuôi.」 | 「Chỉ cần làm hộ khẩu cho Reina thôi――
Việc đó thì, em sẽ nhận em ấy làm con nuôi.」 | Paulette → Soutetsu "em" (1691 Soutetsu "Cảm ơn em. Anh rất vui." audit). |

### 真闇03_ひとしずく.txt.toml — O35 (1 dòng)
| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2484 | だから……聞いてみたくなる。
酷かことかも、知れんけど。 | 所以……我想要知道她的想法，雖然問出口或許很過分。 | Chính vì thế…… tôi lại muốn hỏi em ấy.
Dù biết đó có thể là một điều tàn nhẫn. | Chính vì thế…… tôi lại muốn hỏi chị ấy.
Dù biết đó có thể là một điều tàn nhẫn. | Người nghĩ là Hibiki (độc thoại kề disp=日日姬; 1548 ngay sau Hibiki hỏi thẳng Hachiroku) → "chị ấy" = Hachiroku. |

## §4. Giữ nguyên có lý do (đã xét, 0 dòng)

| Mục | Dòng | Quyết |
|---|---|---|
| O20 | 仲国01 1377 "chị" (Hachiroku → Hibiki) | Giữ — chuẩn toàn dự án "chị Hibiki" ×12 (gọi trực tiếp ≥5 dòng); "cô" chỉ ở cảnh tắm 共通06 (P16 khóa giữ) |
| O21 | 凪ふかみ05 1981 "chị Hachiroku" | Giữ — chuẩn xưng hô có tên (3×, 0× "cô Hachiroku") |
| O23 | 凪ふかみ04 2294/2296/2407 "em", 2309 "em" (= Reina), 2393 "chị", 2174 "Em đợi anh" | Giữ — người nghe đã xác định từng dòng (xem §2 O23) |
| O24 | 凪ふかみ01 1517 "em" (Nagi) | Giữ — người nghe là Hachiroku (1796), không phải Fukami như list ghi |
| O25 | lr h1 1708/1825 "anh" (Soutetsu), 1746 "tớ"/"cậu" (Fukami) | Giữ — 1708/1825 đối thoại đúng P1; 1746 là dòng chuẩn P9 của file |
| O27 | ハチロク10 1825 "tôi" | Giữ — địa chỉ nhóm có Hachiroku (P17) |
| O28 | ハチロク07 1507 "cô" (Soutetsu → Navi) | Giữ — お前 → "cô" là chuẩn đã khóa cho Navi (共通01 ×4); người nghe Navi xác định từ chữ |
| O29 | 日々姫06 1877 "tìm tôi" | Giữ — người nghe 職員Ａ (cả cảnh là đối thoại với Staff A); parent đã xác nhận giữ nguyên |
| O30 | ハチロク07_延命 2339 "chị…em" (Fukami → Olivy) | Giữ — người nghe Olivy (2393/2702) |
| O32 | 日々姫h1 1421/1447 "tôi" (độc thoại Soutetsu); 1010/1052 "Kua!"; 1062/1041/1043/1044 "Hự" | Giữ — 1421/1447 độc thoại đúng; "Kua" đúng mora くあっ; "Hự" giữ theo F1 (file convention) |
| O32 | 日々姫h1 1352/1423 | VOID — không tồn tại trong TOML lẫn CSV3 |
| O33 | lrれいな追加02 1505 "anh" (→ Reina), 1637 "của anh" (→ Hibiki) | Giữ — người nghe đã xác định, đúng P1 |
| O36 | 真闇03 1999 "anh" (fix audit) | Giữ fix — người nghe Hibiki (1994–1995); parent đã xác minh |
| O36 | 真闇03 2038 | VOID — không tồn tại trong CSV3 lẫn TOML |
| O37 | ハチロク14_冬 3202 (fix audit), 2590 (fix audit) | Giữ fix — 3202 người nghe Soutetsu; 2590 diễn đủ 4 っ của JP |
| O37 | 日々姫05 1928 "chú", 2038 "——A" | Giữ — 1928 người nghe là trẻ nhỏ; 2038 っ―― đã có gạch diễn tiếng ngắt (tiền lệ 1042) |

## §5. Khối TOML (đã kiểm chứng parse — xem §7)

```toml
[script]
2679 = "「N... nhờ chị nha.」"
```
```toml
[script]
2030 = "「Ưm――chà, điều đó thì đúng thật.\\nKhông được rồi, là tôi đã ngáng chân mọi người sao.」"
```
```toml
[script]
1955 = "「Tôi cảm giác những toa xe được chế tạo theo kiểu Minh Quốc sẽ không bán được ra nước ngoài.\\nNhưng thực tế, ở Hinomoto cũng có rất nhiều \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; nhập khẩu từ Minh Quốc đúng không?」"
```
```toml
[script]
1620 = "「Hả!? Tớ có làm thế đâu——ưm」"
1672 = "「Ừm. Tớ hiểu rồi. Vậy thì Nagi, trước tiên——\\nừm, cậu ngậm lấy mỗi quy đầu của anh Soutetsu đi?」"
1744 = "「Nagi? Nếu cậu không nũng nịu được.\\nThì tớ sẽ cướp mất cậu nhỏ đấy nhé?」"
```
```toml
[script]
1896 = "「Xin lỗi, nhưng tạm dừng bữa ăn đã.\\nTôi muốn thảo luận ngay bây giờ.」"
2023 = "「Ừm. Tôi có nghe rồi, cũng từng đọc trong sách nữa.\\n『Trên đường sắt Hinomoto, 8620——』」"
2398 = "「Tôi đang nghĩ nếu làm được như vậy.\\nNhưng mà, giả sử có cỗ máy nào phù hợp với điều kiện đó không đã.」"
```
```toml
[script]
1952 = "「Đúng vậy, tôi cũng nghĩ làm theo hướng đó sẽ rất hay.\\nKết nối những câu chuyện thú vị vào phần giải thích.」"
2049 = "「Chào hai người.\\nA, cái này, là quà lộc cho hai người. ạ.」"
```
```toml
[script]
1386 = "「Hả!? Kh-Không, vì quá sốc,\\nnên trong chốc lát, em hơi choáng váng.」"
1644 = "「Chỉ cần làm hộ khẩu cho Reina thôi――\\nViệc đó thì, em sẽ nhận em ấy làm con nuôi.」"
```
```toml
[script]
2484 = "Chính vì thế…… tôi lại muốn hỏi chị ấy.\\nDù biết đó có thể là một điều tàn nhẫn."
```

## §6. Cờ cho coordinator / U15 (không sửa trong đợt này)

- **F-O22-1:** O22-2030 — list ghi parent đã gỡ một fix cũ và giữ "anh" chờ Hieu; đợt này quyết lại SỬA "tôi" theo uỷ quyền + bằng chứng dòng kề (Hachiroku 2554 quở, gọi 双鉄様). Coordinator xác nhận việc đảo quyết cũ này đứng vững.
- **F-O24-1 (chuyển U14c/O64):** 凪ふかみ01 1884 じーちゃん "Ông nội cũng hay nhận làm thầu khoán mà!" — KHÔNG sửa ở đây (thuộc T20, đã liệt kê trong O64). Đề xuất: **GIỮ "ông nội"** — JP じーちゃん chung chung, TW 爺爺 chung chung, không có định danh Seki; T20 chỉ đổi các dòng Seki sang "ông ngoại".
- **F-O25-1 (mới, cần quyết chung):** lr h1 1616 (Fukami tự xưng "Em hiểu rồi"), 1687 ("Ufufu, em nói giỏi lắm"), 1737 ("Nagi, em muốn sao nào?") — cùng lỗi P9 với 3 dòng đã sửa ở O25 nhưng KHÔNG có tên trong mục O25 nên chưa sửa. Đề xuất: sửa cùng dạng "tớ"/"cậu" trong đợt follow-up (hoặc U15) — coordinator quyết có gộp vào đợt này không.
- **F-O25-2 (chuyển U14c/O64):** 2368/2607 thực tế thuộc **日々姫03_客車手配** (おじいちゃんたち → "ông nội và mọi người") — không thuộc lr h1; đã có trong phạm vi O64.
- **F-O33-1:** lrれいな追加02 1635 "Còn tôi là chồng của Reina mà." — nhóm hỗn hợp (Kisaki có mặt), "tôi" biện hộ được theo P17; để nguyên, chỉ ghi chú.
- **Hiệu chỉnh list (đề nghị sửa trong UNIFICATION-LIST.md):** O29 file đúng 日々姫06_みくろ、来訪; O35 file đúng 真闇03_ひとしずく; O37 1928/2038 file đúng 日々姫05_御一夜ステーションカフェ; O25 2368/2607 file đúng 日々姫03_客車手配; O32 1352/1423 và O36 2038 là key void (không tồn tại); O21 thêm bằng chứng 2667 "cô giáo Hachiroku" là danh xưng nghề, không phải đại từ.

## §7. Lượt soát 2 (second pass) + kiểm chứng cơ học

- **Lượt soát 2: 14/14 tái kiểm chứng, 0 loại bỏ, 0 sửa lại.** Mỗi fix đã đọc lại đối chiếu JP (+TW) sau khi viết: 2679 (JP không đại từ; chuẩn "chị Hachiroku" ×3); 2030 (僕 + lời quở Hachiroku 2554 → "tôi"); 1955 (chỉ đổi "Anh" → "Tôi", giữ fix audit); 1620/1672/1744 (わたし/凪ちゃん → "tớ"/"cậu" theo 1746); 1896/2398 (địa chỉ nhóm → "tôi"); 2023 (cụt đúng điểm 「8620の――"); 1952 (僕も考えた → "tôi cũng nghĩ"); 2049 (おふたり = hai người); 1386/1644 (Paulette わたし → "em"); 2484 (người nghĩ Hibiki, hỏi Hachiroku → "chị ấy").
- Kiểm chứng cơ học (script `_u14b/assemble.py`, chạy lại sau khi ghi JSON): JSON 14 mục, đủ 8 trường, key là chuỗi; jp/tw khớp CSV3 tuyệt đối modulo U+3000→space (14/14); old_vn khớp map precedence (csv3 13/14, audit 1/14 — 1955; không dòng nào trùng merged batch, 0 dòng GHÉP); 0 fix == old_vn; 0 ký tự xuống dòng thật; 0 double backslash-n.
- Khối TOML §5: trích từ REVIEW và parse lại bằng tomllib — mọi block value đều bằng đúng fix trong JSON (14/14, 8 file). Chi tiết parse: xem log của `_u14b/build_review.py` + `_u14b/verify_toml.py`.

## Kết bài

- Đợt U14b quyết xong **18/18 mục O20–O37** (không park mục nào cho Hieu — mọi mục đều quyết được từ JP+TW+ngữ cảnh+dòng kề theo uỷ quyền; chỉ có 4 cờ chuyển coordinator/U14c/U15 ở §6, và 1 quyết đảo quyết cũ được ghi rõ để xác nhận: O22-2030).
- **14 dòng sửa mới / 8 file** (O21: 1; O22: 1; O24: 1; O25: 3; O26: 3; O31: 2; O34: 2; O35: 1). **10 mục giữ nguyên 0 dòng** với lý do ghi ở §4 (chủ yếu là: chuẩn toàn dự án đã đúng, register có chủ ý, người nghe xác định được từ chữ, key void, hoặc đã có quyết F1/M7).
- 5 hiệu chỉnh trích dẫn quan trọng cho các đợt sau: người nghe xác định bằng **file-order + nội dung đối thoại** (không phải key-order) — O21/O29/O35/O37 đều đảo ngược hoặc làm rõ kết luận cũ nhờ đó; và 4 mục list ghi sai file (O29/O35/O37/O25-2368-2607) + 3 key void (O32-1352/1423, O36-2038).
- File: `unification-s7-open-pronouns-b-REVIEW.md` + `unification-s7-open-pronouns-b-wrong.json` (14 mục, kind="unification").

**Tổng cộng sau đợt này: 108 mục / 2.700 dòng sai (unification)** (cơ sở 100 mục / 2.686 dòng + đợt U14b 8 mục / 14 dòng mới — đối chiếu `unification/queue.json` 22/11 ~13:00; U14a song song 5 mục / 10 dòng chưa gộp — nếu U14a gộp trước thì chuỗi thành 105 mục / 2.696 dòng và đợt này đưa lên 113 mục / 2.710 dòng)
