# Audit: 仲国06_聖都とパンダとハチロクと.txt.toml (01_Hachiroku / 10_Chikuni — 2 bản sao)

- File: `仲国06_聖都とパンダとハチロクと.txt.toml` — route 01_Hachiroku (bản sao thứ 2 ở 10_Chikuni), 431 dòng script (monologue 139, 双鉄 110, 西瓜 59, ハチロク 55, 日々姫 44, 姜 17, 志寰 7). Nội dung: đoàn đến Thịnh Đô (Thánh Đô), tham quan cơ sở gấu trúc; Hachiroku mê gấu trúc; Suika sợ Chí Hoàn đã thay lòng sau 1 năm 7 tháng xa cách (cô từng bỏ chạy sau khi tỏ tình "Tớ thích cậu"), còn Soutetsu dần hiểu ra cả hai vẫn còn tình cảm — cô chỉ cần loại bỏ "tạp âm" (nỗi sợ, suy đoán) để nghe được giọng nói thật của Chí Hoàn; tàu trễ ~90 phút, kíp lái Chí Hoàn/Tây Qua nỗ lực chạy bù; Hibiki phác thảo, Jiang sắp xếp lịch trình, kết bằng cảnh mọi người đi ngủ trên tàu.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 431 dòng, 0 key trùng, 0 VN trống. TOML và CSV3 khớp tuyệt đối (320 dòng chênh chỉ ở `\n` literal bị TOML-2 làm phẳng thành khoảng trắng — CSV3 là chuẩn, 0 chênh ngoài flatten). TOML md5 `5e756cadc9f3ee1b288883e2d22136d6` cho CẢ HAI bản sao (01_Hachiroku và 10_Chikuni giống hệt nhau — fix áp cho cả hai). BOM + CRLF, `[selections]` rỗng ({}), comment `# JP:` đủ 443 dòng. Thẻ `%l`: JP = VN mọi dòng, 0 thẻ hỏng.
- Phân loại (39): SFX 31, thuật ngữ 3, nghĩa 2, đại từ 1, dấu câu 1, gasp 1. Thoại 30/292 (10,3%), độc thoại 9/139 (6,5%). Theo nhân vật: 双鉄 20/110 (18,2%), monologue 9/139 (6,5%), ハチロク 6/55 (10,9%), 姜 2/17 (11,8%), 西瓜 1/59 (1,7%), 日々姫 1/44 (2,3%), 志寰 0/7.

## 1. Gasp 1 (từ sweep, áp nguyên)

- Sweep có 1 mục duy nhất cho file này (ghi 2 lần, 1 cho mỗi bản sao — cùng 1 dòng): 1523 西瓜 「っ！！！」 → VN cũ 「!!!」 → "「Ư!!!」". Kiểm chứng theo JP: gasp toàn dòng, VN cũ chỉ giữ dấu câu. Áp nguyên giá trị sweep.
- Sweep không bỏ sót gasp nào khác: đã quét cơ học toàn bộ dòng JP chứa っ (xem §8 — các っ còn lại đều là っ trong từ, っ nhấn mạnh gắn từ có nội dung, hoặc âm đã diễn).

## 2. SFX 31 (ああ 23 + tiếng ậm ừ 6 + tiếng cười 2)

- ああ → "Aa" 23 dòng (thiếu 1 nguyên âm a): 1433 (ああああ 4a → "Aaaaa" 5a thừa 1a → "Aaaa"), 1472, 1525, 1541, 1543, 1545, 1546, 1554, 1559 (ああっ！ "A!" → "Aa!"), 1568, 1573, 1580, 1584, 1726, 1733 (giữa câu "a" → "aa"), 1923, 1971, 2214, 2278, 2351, 2353, 2486, 2660. Tiền lệ đã merge: ああ―― "A――"→"Aa――" (ROUTE-AUDIT 174: 1846), 「ああ」→"Aa" (603: 3536), ああっ "A."→"Aa." (1166: 2081/2364; 1245; 1447).
- Tiếng ậm ừ 6 dòng — sai cả phụ âm lẫn số nguyên âm, theo công thức nguyên âm (VN vowel count = 1 + số う/ぅ): 1072 ううむ → "Ưm." → "Hừừm."; 1537/1539/2428 ふぅむ → "Ưm" → "Hừừm"; 1589 うむ (suy ngẫm trước câu suy đoán) → "Ừm." → "Hừm."; 2460 うむ (suy ngẫm) → "ưm." → "hừm." (giữa câu, thường). Tiền lệ đã merge: ふぅむ→"Hừừm" (file 06 2074; 603: 2419). Trong chính file này ふむ đã là "Hừm" (1531, 1540, 1600) và うむ？/うむっ đã là "Hửm?"/"Hửm!?" (1602, 1595) — "Ưm"/"ưm" là không nhất quán.
- Tiếng cười 2 dòng — sai số mora: 1508 うふふふふっ (u + 4 fu) → "Ufufufu" (thiếu 1 "fu") → "Ufufufufu."; 1611 うふふっ (u + 2 fu) → "Fufu" (mất "U" đầu) → "Ufufu.". Đối chứng trong file: 1606 うふふふっ → "Ufufufu." đúng, 1609 うふふっ → "Ufufu" đúng, 1605 ふふっ → "Fufu." đúng. Tiền lệ: うふふ→"Ufufu" (ROUTE-AUDIT 1564).

## 3. Thuật ngữ 3

- 1105 ハチロク: ポーレット様 → "Thịnh trưởng Paulette" → "Thị trưởng Paulette". "Thịnh trưởng" không phải từ Việt; trong chính file này 1435 đã dùng "Thị trưởng Paulette", toàn dự án dùng "Thị trưởng Paulette" 100+ lần.
- 1442 双鉄: 整備体 → "thân chính" → "thân bảo trì". Quy tắc đã chốt: 整備体 = "thân bảo trì" (brief). JP: 「赤ちゃんクマの一体くらい、整備体でもあるのだし」— Soutetsu nói với Tây Qua (Railord dùng thân bảo trì bế gấu con).
- 1873 双鉄: 御一夜 → "Ohimitera" → "Ohitoyo". Quy tắc đã chốt: 御一夜 = "Ohitoyo", never Ohimitera. Sửa trong audit theo tiền lệ đã merge (稀咲h3: 2648/2740/3099 và hàng chục file khác sửa Ohimitera trong audit); ghi chú: review reina03 đã hoãn 7 dòng Ohimitera sang đợt thống nhất — nhưng tiền lệ đa số là sửa trong audit, và brief chỉ liệt kê Ohimitera→Ohitoyo cho riêng ハチロク06_それぞれの傷跡 (1710, 1819, 2706, 2710), không gồm file này.

## 4. Đại từ 1

- 1761 姜: 双鉄先生 → "anh Soutetsu" → "thầy Soutetsu". Chứng cứ: cùng route 仲国, Jiang gọi Soutetsu là "thầy Soutetsu" ở 仲国02 (2028, 2378), 仲国03 (1921), 仲国04 (1984), 仲国07 (947, 1755), 仲国08 (2011, 2055, 2088, 2091); trong chính file này Tây Qua cũng gọi 双鉄先生 là "thầy Soutetsu" 4 lần (1732, 1941, 2057, 2065). "Anh Soutetsu" trong file này là cách dịch của 双鉄さん (Chí Hoàn 1566, 2066) — lẫn さん với 先生. Ghi chú tiền lệ ngược: lr稀咲追加02 Jiang cũng dùng "anh Soutetsu" (1224, 1291, 1342, 1424, 1655) — bối cảnh khác (lần đầu gặp, tuyến Kisaki); quy ước route 仲国 thắng cho file này.

## 5. Nghĩa 2

- 1575 日々姫: 国慶節は仲国の建国記念日 → "còn Quốc khánh là ngày kỷ niệm quốc khánh của Trung Quốc" (lặp từ, vô nghĩa) → "còn Quốc khánh là ngày kỷ niệm thành lập nước Trung Quốc." JP 建国記念日 = ngày kỷ niệm thành lập nước; TW 建國紀念日 xác nhận.
- 1852 双鉄: 西瓜の中や周辺にある雑音を、ひとつひとつ消していく (trần thuật, thì tương lai) → "Hãy loại bỏ từng chút một..." (mệnh lệnh, đổi thể câu) → "Chúng ta sẽ loại bỏ từng chút một những tạp âm bên trong và xung quanh Tây Qua." TW 就要…消除掉 xác nhận thể trần thuật.

## 6. Dấu câu 1

- 1016 monologue: VN cũ thừa dấu 」 cuối dòng — JP không có 「」 (「……関臥原の古戦場は観光地化を目指し、そこそこ以上の整備が行われているらしい。」) → gỡ 」 thừa.

## 7. Mục thuộc đợt unification (không sửa trong audit)

- 帝鉄 → "Đường sắt Hoàng gia" 2 dòng: 1821 (帝鉄全盛期), 2347 (帝鉄時代) → "Teitetsu" chờ đợt thống nhất (brief liệt kê 帝鉄→Teitetsu trong đợt thống nhất; tiền lệ reina03 §6: gloss 帝鉄 "Đường sắt Hoàng gia" không tính sai).

## 8. Giữ nguyên có lý do (không tính sai)

- Gasp ngắn giữ theo quy ước toàn dự án (tiền lệ gộp ROUTE-AUDIT 3199, 3476: あっ/ああっ bare → "A"/"Aa", không thêm Ư): 1506 わあっ → "Oa."; 1587 あうっ → "Aư."; 1522 あ痛っ → "A đau!!?"; 1556 あはっ → "Aha."; 1511 え"っ → "Hả?" (dấu " là vỡ giọng); 1595 うむっ！？ → "Hửm!?" (âm cắt đã diễn bằng phụ âm cuối "m", tiền lệ ハチロク01 2319); 2361/2636 っと cuối độc thoại (2361 bỏ hẳn theo TW; 2636 → "Chắc vậy.").
- ああ/うむ dạng khẳng định giữ nguyên (không phải cảm thán thiếu âm): 1555 ああ → "Ừ."; 1590 うむ → "Ừ."; 1573 うむ！ → "ừ!" (cả ba đều là "vâng/ừ" đáp lại, khác với 1589/2460 là tiếng suy ngẫm đã sửa thành "Hừm"/"hừm").
- 1986 ああ → "Ôi" (cảm thán "ôi, tuyệt vời làm sao" — diễn theo nghĩa, không phải thiếu âm); 1738 ふぁあ → "oáp" (ngáp — diễn ngẫu hứng theo cảnh Hachiroku buồn ngủ, TW 蛤啊 đồng ý); 1519 へぇええ～ → "Hểêê~" (đủ 3 e); 1548/1552/1571 あー → "A" (quy ước file, 3 lần nhất quán).
- Đại từ kiểm chứng đúng toàn file: Soutetsu "tôi" với Hachiroku (nói với Hachiroku/Tây Qua/nhóm trang trọng — 1532, 1837, 1916, 1971, 2006…); Soutetsu "anh" với Hibiki (1580, 1753, 1888); "bọn anh" 1726 giữ (nhóm có Soutetsu là nam, tiền lệ Grand 03 2201); "bọn tôi"/"chúng tôi" dạng nhóm giữ (1971); Hachiroku "em" 22+ lần, "ngài Soutetsu" giữ; Chí Hoàn gọi 双鉄さん → "Anh Soutetsu" đúng (1566, 2066 — さん, khác 先生 ở 1761).
- Ruby thắng TW: 1625 津っ鐵 [つってつ] → "Đường sắt Tsutetsu"; 1690 岳楠鉄道 [がくなん] → "Đường sắt Gakunan"; 1705 後東塊多 [ごとうかいた] → "Goto Kaita" (tiền lệ file 11: 2550/2796 "Kaita" đúng, ruby JP thắng TW 慶太).
- 2067 中慶北駅 → "ga Bắc Trung Khánh" (theo JP 中慶, không phải 重慶/Trùng Khánh; TW 崇慶北站 cũng không phải 重慶); 1851 健為 giải chữ → "Kiện Vi" vs 2084 ケンイー nghe tên → "Jianwei" (giải chữ Hán vs tên nghe được — giữ cả hai); 2441 "Kisaki" theo TW (TW giải nghĩa chủ ngữ mơ hồ trong JP — TW được dùng để gỡ mơ hồ); 2047 thêm "Nghe nói" giữ (làm mềm câu, không sai nghĩa); 2357 "Nghe em ấy nói vậy" giữ (chủ ngữ suy ra từ mạch); 2031 "cảm ơn cô" giữ (người nghe là cô Khương, trang trọng); 1832 Hachiroku hỏi Tây Qua "đối với cô" giữ (xưng hô trang trọng của Hachiroku với đồng nghiệp Railord); 1670–1674 姜秘書 → "thư ký Khương" nhất quán.
- っ trong từ / nhấn mạnh / đã diễn (không phải gasp): きっと, まったく, しっかり…; ざーんねんっ không có trong file; ころんって → "lăn quay", ぴょこっと → "khẽ giật giật", ふわっ → "thở hắt" (TW 嘆息 đồng ý), ぶんぶん → "lia lịa".

## 9. Cờ cho Hieu

- 1412 (志寰, KHÔNG đưa vào fix — đã loại ở lượt soát 2): JP mâu thuẫn nội bộ — chữ Hán 大熊猫保存研究中心基地 (保存 = bảo tồn) nhưng ruby [ぱんだはんしょくきち] đọc はんしょく (繁殖 = nhân giống), TW cũng là 繁育 (nhân giống). VN cũ "Cơ sở Nghiên cứu Bảo tồn Gấu trúc lớn" theo chữ Hán; theo ruby + TW + tên thật (Thành Đô) thì phải là "Nhân giống". JP thắng TW nhưng ở đây chính JP tự mâu thuẫn (chữ vs ruby) — cần Hieu chốt: giữ "Bảo tồn" theo chữ Hán, hay sửa "Nhân giống" theo ruby/TW. Chỉ 1 dòng này trong toàn dự án nhắc đến cơ sở này.
- B19 vẫn park (kiểm tra trong game ở Paulette 13 key 1596 trước đợt quét thẻ %l).

## 10. Lượt soát 2

- 40/40 ứng viên đọc lại toàn bộ giá trị fix đối chiếu JP; 39 tái kiểm chứng đúng, 1 bỏ (1412 — mâu thuẫn chữ Hán/rubi, cờ cho Hieu, xem §9), 0 sửa. Mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng: mỗi fix = đúng 1 thay đổi liên tục — xem §11).

## 11. Kiểm chứng

- JSON 39 mục dạng chuẩn (list of dicts, khóa chuỗi, đủ trường key/jp/tw/old_vn/fix/kind/character); khối TOML 39 khóa, parse OK bằng tomllib, 0 sai lệch giá trị (so sánh chuỗi thô; `\\n` giữ nguyên); jp/tw/old_vn khớp CSV3 tuyệt đối 39/39; mỗi fix chỉ khác VN cũ ở đúng 1 chỗ cần sửa.
- Cơ sở tổng đã kiểm chứng trực tiếp dòng tổng cuối ROUTE-AUDIT.md: 170 file / 7.747 dòng sai.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1016" = "……Chiến trường cổ Quan Ngọa Nguyên dường như đang hướng tới việc trở thành một địa điểm du lịch,\\nvà đã được quy hoạch ở mức độ tương đối."
"1072" = "「……Hừừm.」"
"1105" = "「……Nếu là Thị trưởng Paulette,\\nchắc chắn cô ấy sẽ rất tận hưởng đấy.」"
"1433" = "「Bản thân gấu trúc mới thực sự là một viên ngọc quý!! Aaaa, thật là!\\nGấu trúc thật là! Một sinh vật đáng yêu làm sao!」"
"1442" = "「Chỉ là một bé gấu con thôi mà,\\nem đang dùng thân bảo trì, bế chắc chắn không thành vấn đề đâu.」"
"1472" = "「Dù không có cuộc Đại bãi bỏ tuyến đường sắt, thì việc mọi người quay lưng với đường sắt vẫn là điều khó tránh khỏi sao.\\nAa——nhắc mới nhớ, cô tiếp viên hàng không trên máy bay cũng……」"
"1508" = "「Ôi! Ufufufufu.\\nNếu vậy chắc chắn phải dùng vé bằng lá trúc rồi nhỉ.」"
"1523" = "「Ư!!!」"
"1525" = "「Aa——」"
"1537" = "「Hừừm……nhưng mà, việc bỏ sót cả thao tác lái tàu thì……\\nĐúng là đáng xấu hổ với tư cách một người lái tàu.」"
"1539" = "「Hừừm……Sự quan tâm của mình, hay ánh mắt của mình rốt cuộc đang hướng về đâu,\\ntrước giờ tôi chưa từng bận tâm đến.」"
"1541" = "「Hửm? Aa, không……Nếu xét theo khía cạnh đó,\\nthì việc chỉ có Hibiki ở lại thêm vài ngày——」"
"1543" = "「Aa——」"
"1545" = "「Aa——Hachiroku cũng từng nói, thông qua cộng cảm,\\ncô ấy đã nhận được 'những âm thanh mà bản thân không thể nghe thấy' từ Tây Qua nhỉ.」"
"1546" = "「Aa——ra vậy.\\nĐôi tai của Tây Qua cũng được mài giũa qua những sở thích như thế sao.」"
"1554" = "「Aa……」"
"1559" = "「Aa!」"
"1568" = "「Aa, cũng đúng nhỉ.」"
"1573" = "「Aa, ừ! Tôi ở đây! Tới ngay đây!!\\nĐợi một chút nhé.」"
"1575" = "「À, đó là những kỳ nghỉ lễ lớn ở Trung Quốc. Lễ hội Mùa xuân giống như Tết Nguyên đán của Hinomoto,\\ncòn Quốc khánh là ngày kỷ niệm thành lập nước Trung Quốc. Mỗi dịp đều được nghỉ một tuần.」"
"1580" = "「Aa, anh nhớ rồi. Hình như còn có dòng chữ Đỗ Phủ kèm theo nữa nhỉ.\\nLà một nhà thơ tiêu biểu của Trung Quốc đúng không?」"
"1584" = "「Aa, có vẻ họ đang chuẩn bị đến ga rồi.\\nXin hãy trả lại thẻ mà tôi đã đưa cho mọi người lúc lên tàu.」"
"1589" = "「Hừm. Đây chỉ là suy đoán của tôi thôi——\\nnhưng chắc chắn Chí Hoàn cũng có chung cảm xúc đó.」"
"1611" = "「Ufufu. Những nhận thức như vậy,\\ncó lẽ nếu không đến Trung Quốc thì ngài đã chẳng thể có được nhỉ.」"
"1726" = "「Aa, Hibiki. Em đến tìm bọn anh sao.」"
"1733" = "「Em cảm thấy tất cả những gì mình nhìn thấy đều là những thiết kế tuyệt mỹ.\\nNhưng mà——aa, ngài Soutetsu, nhưng mà, nhưng mà!」"
"1761" = "「Tôi muốn thầy Soutetsu, cô Hibiki,\\nvà Railord Hachiroku quyết định xem nội dung khảo sát nào nên được ưu tiên.」"
"1852" = "「Để có thể lắng nghe trọn vẹn và chân thực nhất giọng nói của Chí Hoàn.\\nChúng ta sẽ loại bỏ từng chút một những tạp âm bên trong và xung quanh Tây Qua.」"
"1873" = "「Đó là cuộc họp của Bộ Đất đai, Hạ tầng, Giao thông và Du lịch, Paulette không thể không tham gia.\\nDo đó, tôi bắt buộc phải có mặt ở Ohitoyo.」"
"1923" = "「Lá trúc? Đó là thức ăn của chúng mà? Aa không——\\nnếu nghĩ theo kiểu con người thì cũng có những chiếc giường làm từ rơm rạ nhỉ.」"
"1971" = "「Tôi cứ nghĩ Tây Qua sẽ đi tham quan cùng Chí Hoàn chứ——\\nAa! Không, ra là vậy. Xin lỗi nhé, vì chúng tôi sao.」"
"2214" = "Aa, vừa ngả lưng xuống là cơn buồn ngủ ập đến nặng trĩu.\\nSự mệt mỏi hóa thành những lớp bông ngái ngủ, nhẹ nhàng ôm lấy toàn bộ cơ thể."
"2278" = "Có vẻ Hachiroku cũng nghĩ giống tôi.\\nNhưng, tại sao lại đột ngột nhắc đến Quan Ngọa Nguyên——Aa!"
"2351" = "Aa, không, nhưng mà, lòng người thì không thể nào đoán trước được.\\nViệc Chí Hoàn hiện tại có còn thích Tây Qua hay không……"
"2353" = "Aa, chuyện này——mình lại lỡ lời rồi sao.\\nChưa kịp nghĩ xong, một giọng nói sắc lẹm đã bay tới."
"2428" = "Tôi cứ tưởng Hachiroku thích phối màu đen-đỏ-vàng cơ chứ……\\nHừừm, hóa ra trắng-đen cũng hợp gu em ấy sao."
"2460" = "Nếu vậy thì——hừm.\\nHãy thử thay đổi góc độ một lần nữa xem sao."
"2486" = "Hibiki mỉm cười. Không hiểu sao trông em ấy vô cùng hạnh phúc——\\nAa, không phải."
"2660" = "（Aa không, có lẽ,\\nem ấy thích động vật, nhưng chỉ là không biết cách tiếp xúc với chúng chăng?）"
```
## Kết bài

File 仲国06_聖都とパンダとハチロクと.txt.toml: 431 dòng đã đọc đủ, 39 dòng sai (9,05%) — lỗi tập trung ở SFX đếm nguyên âm (ああ thiếu 1 a: 23 dòng; tiếng ậm ừ ふぅむ/ううむ/うむ sai cả phụ âm lẫn số âm: 6 dòng; tiếng cười sai số mora: 2 dòng), cộng 3 thuật ngữ ("Thịnh trưởng", 整備体 "thân chính", "Ohimitera"), 2 sai nghĩa (Quốc khánh lặp từ, thể mệnh lệnh 1852), 1 xưng hô (姜 gọi 双鉄先生 là "anh"), 1 dấu 」 thừa và 1 gasp っ từ sweep (1523). Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. 2 dòng 帝鉄 "Đường sắt Hoàng gia" chờ đợt thống nhất. 1 cờ cho Hieu (1412: chữ Hán 保存 vs ruby はんしょく + TW 繁育); B19 vẫn park.
