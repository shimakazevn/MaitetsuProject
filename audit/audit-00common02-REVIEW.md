# Audit: 00_Common file 02 — 共通02_日々姫と真闇と人形と — 33 dòng Việt sai (đã đối chiếu JP + TW)

File: `00_Common/共通02_日々姫と真闇と人形と.txt.toml` — Common chương 2, Hibiki + Mayami + Hachiroku (búp bê Railord 8620) dọn phòng ông nội Taito, tìm lỗ khóa lên cót.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa từng dòng: **467 dòng** (độc thoại 171, 双鉄 127, 日々姫 77, ハチロク 53, 真闇 39), toàn bộ thuộc section `script`, đối chiếu JP + TW từ CSV3 và TOML-2. Tên file đã kiểm chứng khớp CSV3 và TOML-2.
- **Nguồn dữ liệu — PHÁT HIỆN QUAN TRỌNG (xem §Ghi nhận về nguồn dữ liệu):** CSV3 liệt kê file này **hai lần** (bộ `00_Common` và bộ `02_Hibiki`, mỗi bộ 467 dòng). Audit này dùng bộ **`02_Hibiki`** — JP khớp comment TOML 467/467, VN khớp TOML 466/467 (1 dòng còn lại 2009 chỉ lệch khoảng trắng cuối). Bộ `00_Common` là **STALE** (chỉ 31/467 VN khớp TOML, JP lệch 214 dòng) — cùng bẫy như lr_ふかみh2 và 共通03.
- **Sai: 33/467 (7,1%).** Phân loại: xưng hô 13, thuật ngữ 7, lỗi nhỏ 4, sai nghĩa 3, SFX 3, gasp 2, thẻ %l 1.
- **Lệch dòng: 0. Chuỗi xoay (rotation chain): 0. Nhiễm chéo file khác: 0. VN trùng lặp: 0. Dòng không chắc chắn (uncertain): 0.**
- Thẻ %l: VN có 20 thẻ, JP có 19 thẻ — 1 thẻ VN tự thêm (2693, đã sửa); 0 thẻ thiếu dấu `;` đóng.
- Gasp っ: JP có っ ở 184 dòng; sweep đã sửa 2 dòng (2194, 2570 — xác nhận đúng, không trùng lặp trong danh sách này); audit này bắt thêm **2 gasp sweep bỏ sót** (1560, 2009); 3 dòng sweep ghi needs-file-audit (1942, 2592, 2894) đều kiểm chứng **đúng, không sửa**.
- File trùng lặp (md5): **không có** bản sao nào khác của file này trong TOML-2 — fix chỉ cần áp vào một file.
- **Đợt kiểm tra thứ hai (second pass): 33/33 bản sửa đọc lại đối chiếu JP, 33 được xác nhận, 0 loại bỏ, 7 sửa lại** (2693, 2695, 2848, 3009, 3184, 3243, 3247 — đợt đầu đã thêm thừa dấu 「」 vào các dòng độc thoại vốn không có ngoặc kép; đã sửa về đúng dạng gốc). Parse-check bằng tomllib **không thay thế** đợt đọc lại này.

## Kết luận về cơ chế lỗi

File này **không có lỗi lệch dòng** — mọi VN đều ứng đúng dòng JP của nó, khác hẳn các file Paulette 03 hay Hibiki 03. Lỗi tập trung ở hai chỗ:

1. **Xưng hô của Soutetsu không nhất quán (13/33):** cùng một người, cùng một đoạn đối thoại, lúc tự xưng "em" (1872, 2064, 2167 nửa đầu, 2209, 2324, 2418, 2433, 2563), lúc "anh" (1976 sai người nghe, 2162/2163 sai chiều), lúc "tôi" đúng chỗ. Đây là thói quen của người dịch cũ, không phải lỗi hệ thống — cứ soi người nghe từng dòng (cột Character + 2–3 dòng xung quanh) là phân biệt được: với Hibiki là "anh", với Mayami/Hachiroku là "tôi", "em" **không bao giờ** đúng cho Soutetsu.
2. **Thuật ngữ theo quyết định 19/11 chưa được áp dụng (7/33):** "Ohimitera" còn 5 chỗ (2135, 2201, 2413, 2495, 3009 — toàn bộ 5 chỗ trong file, sửa hết thì file này sạch Ohimitera), gloss 帝鉄 còn "Đường sắt Hoàng gia" (2182), "Jussendo" bỏ mất chữ "t" của 術仙 (2323).

Các lỗi còn lại rải rác: 2 gasp っ bị mất sau tên riêng có thẻ %l (1560, 2009 — cùng mẫu với 2194 mà sweep đã bắt), đếm nguyên âm SFX sai ±1 (2016, 2017), mất âm う (2018), bịa phần kết cho câu cụt JP (2035), đếm sai "bốn chữ" thành "hai chữ" (2695), 1 thẻ gloss VN tự thêm (2693), lỗi dấu câu nhỏ (2076, 3184, 3243, 3247).

## Chi tiết dòng sai

### Xưng hô (13)

#### [1872] — Soutetsu tự xưng "em" với Hibiki
- **JP:** 「一生。それはたまらんな。\nならば聞くまい。自分で、おいおい考えてみよう」
- **TW:** 「一輩子啊，這可真是受不了。那我也不問了，自己慢慢琢磨吧」
- **Cũ:** 「Cả đời cơ à. Thế thì chịu không nổi đâu. Vậy em không hỏi nữa. Em sẽ tự mình từ từ suy nghĩ vậy.」
- **Mới:** 「Cả đời cơ à. Thế thì chịu không nổi đâu. Vậy anh không hỏi nữa. Anh sẽ tự mình từ từ suy nghĩ vậy.」
- **Lý do:** Người nghe là Hibiki (đáp lại ở 1876; Mayami vắng mặt trong đoạn 1872–1909); docs locations §2.1: Soutetsu xưng "Anh" khi nói với em gái Hibiki. "tự mình" giữ nguyên (đại từ phản thân, không phải tự xưng).

#### [1976] — Soutetsu tự xưng "anh" sai người nghe
- **JP:** 「なに、実際に簡単だ。\n僕の\x%lエアクラ;#00ffc040;エアクラ%l;#;は優秀だからな」
- **TW:** 「別擔心，的確很簡單。我的\x%lエアクラ;#00ffc040;空凝機%l;#;可是很優秀的」
- **Cũ:** 「Có gì đâu, thực sự rất đơn giản mà. \x%lエアクラ;#00ffc040;Aircra%l;#; của anh xuất sắc lắm đấy.」
- **Mới:** 「Có gì đâu, thực sự rất đơn giản mà. \x%lエアクラ;#00ffc040;Aircra%l;#; của tôi xuất sắc lắm đấy.」
- **Lý do:** Người nghe là Mayami/Hachiroku — Hibiki không xuất hiện trong đoạn 1967–1981 (Hachiroku vừa giới thiệu với Mayami ở 1974). "Anh" chỉ được dùng với Hibiki.

#### [2064] — Soutetsu tự xưng "em" với Hibiki
- **JP:** 「うん。大学は休学してきた」
- **TW:** 「嗯。大學那邊我休學了」
- **Cũ:** 「Vâng. Em đã bảo lưu ở đại học rồi.」
- **Mới:** 「Vâng. Anh đã bảo lưu ở đại học rồi.」
- **Lý do:** Người nghe là Hibiki — Mayami đã rời đi ở 2059 ("đang dở việc ở xưởng"), Hibiki là người đối thoại trong đoạn 2060–2061. Với Hibiki là "anh". (Nếu người nghe là Mayami thì phải là "tôi" — đằng nào "em" cũng sai.)

#### [2162] — Soutetsu tự xưng "tôi" với Hibiki
- **JP:** 「そうならよかったのだが、僕は」
- **TW:** 「我也希望是這樣，但我——」
- **Cũ:** 「Nếu được vậy thì tốt quá, nhưng tôi thì...」
- **Mới:** 「Nếu được vậy thì tốt quá, nhưng anh thì...」
- **Lý do:** Cùng cuộc đối thoại với Hibiki, ngay sau 2160 dùng "anh" ("Anh cũng không rõ về bản thân mình lắm") — "tôi" ở đây không nhất quán; TW xác nhận 2160 nói trực tiếp với Hibiki ("你").

#### [2163] — Như 2162
- **JP:** 「僕も相続人のはしくれではある。が、一番の相続人。\n右田家の現当主ということであれば、真闇姉だ」
- **TW:** 「我也是繼承人之一。但要說第一順位的繼承人的話，應該是右田家的現任當家，真闇姐」
- **Cũ:** 「Tôi cũng là một trong những người thừa kế. Nhưng người thừa kế số một, đương kim gia chủ nhà Migita hiện tại, là chị Mayami.」
- **Mới:** 「Anh cũng là một trong những người thừa kế. Nhưng người thừa kế số một, đương kim gia chủ nhà Migita hiện tại, là chị Mayami.」
- **Lý do:** Tiếp nối 2160–2162, cùng người nghe Hibiki.

#### [2167] — Câu hỗn hợp hai người nghe
- **JP:** 「ただいま、真闇姉。ただいま、日々姫」
- **TW:** 「我回來了，真闇姐。我回來了，日日姬」
- **Cũ:** 「Em về rồi đây, chị Mayami. Anh về rồi đây, Hibiki.」
- **Mới:** 「Tôi về rồi đây, chị Mayami. Anh về rồi đây, Hibiki.」
- **Lý do:** Nửa đầu nói với Mayami → "tôi" (quyết định 19/11: Soutetsu→Mayami "tôi", không ngoại lệ); nửa sau với Hibiki giữ "anh".

#### [2209] — Soutetsu tự xưng "em" với Hibiki (×2)
- **JP:** 「僕の部屋など物置でも押入れでも構わない。\nああ、酒の倉庫は……できれば、勘弁して欲しいが」
- **TW:** 「把我安排在倉庫或是隔間都沒有問題。啊，但還是儘量……不要是放酒的倉庫」
- **Cũ:** 「Phòng của em thì nhà kho hay tủ âm tường cũng được. A, nhưng kho rượu thì……nếu được, xin tha cho em.」
- **Mới:** 「Phòng của anh thì nhà kho hay tủ âm tường cũng được. A, nhưng kho rượu thì……nếu được, xin tha cho anh.」
- **Lý do:** Tiếp nối 2207 nói với Hibiki ("nếu em dọn dẹp lại...").

#### [2324] — Soutetsu tự xưng "em" với Hibiki
- **JP:** 「いや。　一人でも夜……\n明日の朝までにはなんとか出来るようには思う」
- **TW:** 「沒事。一個人的話到晚……明天早上的話應該可以整理完」
- **Cũ:** 「Không. Một mình em thì đến đêm…… chắc đến sáng mai là có thể xoay xở xong.」
- **Mới:** 「Không. Một mình anh thì đến đêm…… chắc đến sáng mai là có thể xoay xở xong.」
- **Lý do:** Hibiki vừa nói ở 2323; "Một mình em" là tự xưng sai.

#### [2418] — Soutetsu tự xưng "em" với Mayami
- **JP:** 「汰斗さんの部屋なら光栄だ。\nよければ、案内して欲しい」
- **TW:** 「能住汰斗老爺的房間我倍感榮幸。可以的話，麻煩帶我過去吧」
- **Cũ:** 「Được ở phòng ông Taito thì vinh hạnh quá. Nếu được, mong chị dẫn đường cho em.」
- **Mới:** 「Được ở phòng ông Taito thì vinh hạnh quá. Nếu được, mong chị dẫn đường cho tôi.」
- **Lý do:** "Chị" ở đây là Mayami; Soutetsu→Mayami là "tôi".

#### [2433] — Soutetsu tự xưng "em" với Mayami
- **JP:** 「飲まされはしたが、一向に。\nどうも[きゅうしゅう,1]九洲男児とは、体質からして異なるようだ」
- **TW:** 「被人勸著喝過，但一點也沒變強。感覺九州男子在體質上與別處的人有很大差異」
- **Cũ:** 「Cũng bị ép uống, nhưng chẳng khá khẩm gì. Có vẻ thể chất của em khác hẳn với đàn ông Kyushu rồi.」
- **Mới:** 「Cũng bị ép uống, nhưng chẳng khá khẩm gì. Có vẻ thể chất của tôi khác hẳn với đàn ông Kyushu rồi.」
- **Lý do:** Chủ đề uống rượu với Mayami (Mayami rủ thi uống ở 2368).

#### [2443] — Hachiroku gọi Soutetsu là "cô"
- **JP:** 「左様ですね。ご助言、ありがとうございます。\n――すみませんが、後ろを向いていていただけますか？」
- **TW:** 「說得是。非常感謝您的提醒。不好意思，能麻煩您轉過身去嗎？」
- **Cũ:** 「Đúng vậy nhỉ. Cảm ơn cô đã nhắc nhở. ——Xin lỗi, ngài có thể quay lưng lại được không ạ?」
- **Mới:** 「Đúng vậy nhỉ. Cảm ơn ngài đã nhắc nhở. ——Xin lỗi, ngài có thể quay lưng lại được không ạ?」
- **Lý do:** Cùng một câu, nửa sau đã dùng "ngài" — người nghe là Soutetsu (nam, Hachiroku xin quay lưng vì đang thay đồ); "cô" sai, thống nhất "ngài". (Đối chiếu: 2355 Hachiroku gọi Mayami là "cô" là đúng, giữ nguyên.)

#### [2563] — Soutetsu tự xưng "em" với Hachiroku/Mayami
- **JP:** 「それは――そうかと思います。\n[とう,1]義父さんは、帝都でも僕によくしてくださいまして」
- **TW:** 「都是託父親的福。父親在帝都也很照顧我」
- **Cũ:** 「Chuyện đó——chắc là vậy ạ. Cha nuôi ở Đế đô cũng đối xử rất tốt với em.」
- **Mới:** 「Chuyện đó——chắc là vậy ạ. Cha nuôi ở Đế đô cũng đối xử rất tốt với tôi.」
- **Lý do:** Đoạn đối thoại với Hachiroku (nàng hỏi tiếp ở 2564); với Hachiroku hay Mayami đều là "tôi".

#### [2848] — Độc thoại Soutetsu xưng "mình" (không thuộc ngoại lệ)
- **JP:** その見事さに威圧感さえ感じれば――\n右田家に、戻ってきたと実感できる。
- **TW:** 如此整潔，甚至讓人有一絲壓力，我不由得深感到自己確實回到了右田家。
- **Cũ:** Sự lộng lẫy đến mức tạo ra cảm giác áp đảo ấy―― Giúp tôi cảm nhận được một cách chân thực rằng mình đã trở về nhà Migita.
- **Mới:** Sự lộng lẫy đến mức tạo ra cảm giác áp đảo ấy―― Giúp tôi cảm nhận được một cách chân thực rằng tôi đã trở về nhà Migita.
- **Lý do:** Đây là tường thuật khách quan ("tôi cảm nhận được rằng..."), không phải độc thoại tự vấn cảm xúc nội tâm nên ngoại lệ "mình" không áp dụng. Đối chiếu 3008 "Mình nghe nhầm sao?" là câu tự vấn, được giữ theo ngoại lệ.

### Thuật ngữ (7)

#### [2135] — Ohimitera → Ohitoyo
- **JP:** 「[おひとよ,2]御一夜……右田」
- **TW:** 「御一夜……右田」
- **Cũ:** 「Ohimitera……Migita.」
- **Mới:** 「Ohitoyo……Migita.」

#### [2182] — Gloss 帝鉄: "Đường sắt Hoàng gia" → "Teitetsu"
- **JP:** 「わたくしは\x%l帝鉄;#00ffc040;帝鉄%l;#;[ハチロクニイマル,3]8620形\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;、トップナンバー・\n\x%l8620;#00ffc040;8620%l;#;号専用レイルロオド、ハチロクと申します」
- **TW:** 「我是\x%l帝鉄;#00ffc040;帝國鐵路%l;#;８６２０型\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;首車·\x%l8620;#00ffc040;８６２０%l;#;專用鐵路人偶——八六」
- **Cũ:** 「Tôi là Hachiroku, Railord chuyên dụng cho chiếc đầu tiên mang số hiệu \x%l8620;#00ffc040;8620%l;#; thuộc dòng \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; loại 8620 của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;.」
- **Mới:** 「Tôi là Hachiroku, Railord chuyên dụng cho chiếc đầu tiên mang số hiệu \x%l8620;#00ffc040;8620%l;#; thuộc dòng \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; loại 8620 của \x%l帝鉄;#00ffc040;Teitetsu%l;#;.」
- **Lý do:** Quyết định 19/11 #6: 帝鉄 = "Teitetsu", bỏ "Đường sắt Hoàng gia". Chỉ sửa gloss trong thẻ %l; thứ tự thẻ VN (8620 trước) là do cấu trúc câu Việt đảo lại, các thuật ngữ vẫn khớp JP.

#### [2201] — Ohimitera → Ohitoyo
- **JP:** 「わ、わたしは右田日々姫。\n[おひとよ,2]御一夜の学園の学園生です」
- **TW:** 「我，我是右田日日姬。是御一夜學校的學生」
- **Cũ:** 「T, tôi là Migita Hibiki. Là học sinh của học viện Ohimitera.」
- **Mới:** 「T, tôi là Migita Hibiki. Là học sinh của học viện Ohitoyo.」

#### [2323] — "Jussendo" → "Jutsu-sendo"
- **JP:** 「なか……んっ、無いと思います、兄さん。\nですが、ひょっとすると[じゅつせんどう,2]術仙洞に」
- **TW:** 「沒……嗯，應該是沒有，哥哥。但是，說不定在術仙洞有」
- **Cũ:** 「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jussendo lại có.」
- **Mới:** 「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jutsu-sendo lại có.」
- **Lý do:** 術仙 = "Jutsu-sen" (quyết định ở Grand 04: "Jussen" bỏ mất chữ "t" là sai); 術仙洞 = "Jutsu-sendo".

#### [2413] — Ohimitera → Ohitoyo
- **JP:** 「御一夜の衰退を考えれば、当然の結論だというだけです。\n\x%lエアクラ;#00ffc040;エアクラ%l;#;の工場誘致は、安定的な発展をもたらします」
- **TW:** 「考慮到御一夜的衰退，這是必然的結論罷了。引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶，就能帶來穩定的發展」
- **Cũ:** 「Nếu nghĩ đến sự suy thoái của Ohimitera, thì đó chỉ là kết luận tất nhiên thôi. Việc mời nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; về sẽ mang lại sự phát triển ổn định.」
- **Mới:** 「Nếu nghĩ đến sự suy thoái của Ohitoyo, thì đó chỉ là kết luận tất nhiên thôi. Việc mời nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; về sẽ mang lại sự phát triển ổn định.」

#### [2495] — Ohimitera → Ohitoyo
- **JP:** 「御一夜に\x%lエアクラ;#00ffc040;エアクラ%l;#;工場を誘致するという話。\n今、どの程度のものになってる？」
- **TW:** 「邀請\x%lエアクラ;#00ffc040;空凝機%l;#;工廠在御一夜落戶的事情，進展到哪裡了？」
- **Cũ:** 「Chuyện mời nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; về Ohimitera. Bây giờ tiến triển đến đâu rồi chị?」
- **Mới:** 「Chuyện mời nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; về Ohitoyo. Bây giờ tiến triển đến đâu rồi chị?」

#### [3009] — Ohimitera → Ohitoyo
- **JP:** そう、御一夜に、この家にもらわれて来て、初めて知った。\n水が、氷が、これほどうまいということを。
- **TW:** 是的，自從被領養到御一夜的這個家後，我才意識到原來水和冰也能如此美味。
- **Cũ:** Đúng vậy, kể từ khi được nhận nuôi ở ngôi nhà này tại Ohimitera, tôi mới biết. Rằng nước, rằng đá lại có thể ngon đến thế này.
- **Mới:** Đúng vậy, kể từ khi được nhận nuôi ở ngôi nhà này tại Ohitoyo, tôi mới biết. Rằng nước, rằng đá lại có thể ngon đến thế này.
- **Lý do:** Đây là chỗ "Ohimitera" thứ 5 và cuối cùng trong file — sau đợt sửa này file sạch hoàn toàn dạng cũ.

### Gasp っ bị mất (2 — cả hai đều là sweep-missed)

#### [1560] — Gasp sau tên Railord
- **JP:** 「\x%lレイルロオド;#00ffc040;レイルロオド%l;#;っ！？」
- **TW:** 「\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;！？」
- **Cũ:** 「\x%lレイルロオド;#00ffc040;Railord%l;#;!?」
- **Mới:** 「\x%lレイルロオド;#00ffc040;Railord%l;#;Ư!?」
- **Lý do:** っ sau tên riêng có thẻ %l bị mất; sweep không bắt được (đã tra sweep-raw-gasp-wrong.json: không có dòng nào cho key này). Ư đặt ngay sau thẻ đóng, đúng vị trí âm thanh của nó.

#### [2009] — Gasp sau tên Aircra
- **JP:** 「じゃけん、そん\x%lエアクラ;#00ffc040;エアクラ%l;#;が」\n「\x%lエアクラ;#00ffc040;エアクラ%l;#;っ！！？」
- **TW:** 「可是，\x%lエアクラ;#00ffc040;空凝機%l;#;是不能——」\n「\x%lエアクラ;#00ffc040;空凝機%l;#;！！？」
- **Cũ:** 「Thì thế, cái \x%lエアクラ;#00ffc040;Aircra%l;#; đó...」\n「\x%lエアクラ;#00ffc040;Aircra%l;#;!!?」
- **Mới:** 「Thì thế, cái \x%lエアクラ;#00ffc040;Aircra%l;#; đó...」\n「\x%lエアクラ;#00ffc040;Aircra%l;#;Ư!!?」
- **Lý do:** Cùng JP với 2194 (sweep đã sửa với fix "chúng tôiƯ!!" — giữ nguyên fix sweep, không trùng lặp ở đây) nhưng VN ở đây ngắn, nên Ư đặt ngay sau Aircra thứ hai — vừa đúng vị trí âm thanh, vừa đúng cuối câu. Đây là cặp dòng JP giống hệt nhau nhưng dịch khác nhau (2009 ngắn, 2194 dài theo TW) — không phải lỗi lệch dòng.

### SFX (3)

#### [2016] — Đếm nguyên âm thiếu 1
- **JP:** 「ぴゃああああああっ！！！」
- **TW:** 「呀呀呀呀呀呀！！！」
- **Cũ:** 「Pyaaaaaa!!!」
- **Mới:** 「Pyaaaaaaa!!!」
- **Lý do:** JP ぴゃ + 7 âm a; VN chỉ có 6 âm a — thiếu 1 (quy tắc độ dài SFX: đếm đúng số nguyên âm JP).

#### [2017] — Đếm nguyên âm thừa 1
- **JP:** 「きゃあああっ！？」
- **TW:** 「呀呀呀呀呀！？」
- **Cũ:** 「Kyaaaaa!?」
- **Mới:** 「Kyaaaa!?」
- **Lý do:** JP きゃ + 3 âm a = 4 âm a; VN có 5 âm a — thừa 1. (Đối chiếu: 2056 あああっ → "A a á!" đếm đúng 3 âm, giữ nguyên.)

#### [2018] — Mất âm う
- **JP:** 「ひゃうっ！？　ひゃ、あっ――平気！　平気ったい！\nあ！　その、無事です、怪我はありません」
- **TW:** 「呀！唔，我沒事！沒事啦！啊！那個，我沒事，也沒有受傷」
- **Cũ:** 「Hya!? Hya, á——Không sao! Em không sao! A! À ừm, em không sao, không bị thương gì cả.」
- **Mới:** 「Hyau!? Hya, á——Không sao! Em không sao! A! À ừm, em không sao, không bị thương gì cả.」
- **Lý do:** ひゃうっ — âm う bị mất ("Hya" chỉ giữ ひゃ); quy tắc "không để mất âm". (ひゃ、あっ → "Hya, á" ở nửa sau đã đúng, giữ nguyên.)

### Sai nghĩa (3)

#### [1880] — 転ぶぞ dịch sai sắc thái
- **JP:** 「おっと、転ぶぞ？　動きには気をつけろ」
- **TW:** 「不好，別摔倒了？要當心一點哦」
- **Cũ:** 「Ái chà, ngã bây giờ? Cẩn thận cử động chứ.」
- **Mới:** 「Ái chà, sắp ngã đấy? Cẩn thận cử động chứ.」
- **Lý do:** 転ぶぞ là cảnh báo "sắp ngã đấy", không phải câu hỏi "ngã bây giờ?".

#### [2035] — Bịa phần kết cho câu cụt JP
- **JP:** 「おやまぁ、これは随分と」
- **TW:** 「哎呀，這可真是……」
- **Cũ:** 「Ây da, em khách sáo quá.」
- **Mới:** 「Ây da, cái này thì đúng là——」
- **Lý do:** JP là câu cụt (không có vị ngữ); VN "em khách sáo quá" bịa thêm nội dung không có trong gốc — vi phạm quy tắc không bịa phần kết cho câu cụt (tiền lệ P08 2326, P15 1742/2336/2637). Giữ dạng câu cụt với dấu "——".

#### [2695] — Đếm sai "bốn chữ" thành "hai chữ"
- **JP:** ねぇねぇではなく、あえて姉さん。\n姉妹喧嘩、と。その四文字が頭に浮かぶ。
- **TW:** 不是阿姐，而是姐姐嗎。我的腦子浮現出了“姐妹吵架”四個字。
- **Cũ:** Không gọi là chị hai, mà cố tình gọi là chị gái. Hai chữ "chị em cãi nhau" hiện lên trong đầu tôi.
- **Mới:** Không gọi là chị hai, mà cố tình gọi là chị gái. Bốn chữ "chị em cãi nhau" hiện lên trong đầu tôi.
- **Lý do:** その四文字 = bốn chữ (姉妹喧嘩 có 4 chữ Hán; "chị em cãi nhau" có 4 tiếng Việt); VN ghi "Hai chữ" là sai số lượng.

### Thẻ %l (1)

#### [2693] — VN tự thêm thẻ gloss
- **JP:** さすがは、右田家の現当主――\n“クマの右田の女杜氏”だ。
- **TW:** 不愧是右田家的現任當家，“隈右田女掌窖”。
- **Cũ:** Không hổ danh là đương kim gia chủ nhà Migita—— "\x%l杜氏;#00ffc040;Nữ trưởng hầm rượu%l;#; nhà Migita xứ Kuma".
- **Mới:** Không hổ danh là đương kim gia chủ nhà Migita—— "Nữ trưởng hầm rượu nhà Migita xứ Kuma".
- **Lý do:** JP và TW đều không có thẻ ở đây; VN tự thêm thẻ gloss cho 杜氏. Theo tiền lệ gỡ gloss VN tự thêm (機関士 ở Hachiroku 12, 3 thẻ ở reina02) — gỡ thẻ, giữ chữ. Đây là thẻ VN thừa duy nhất trong file (VN 20 thẻ vs JP 19 thẻ).

### Lỗi nhỏ (4)

#### [2076] — Dấu phẩy kiểu máy dịch
- **JP:** 「“姉さん”も、\n兄さんと同じことを言っていましたから」
- **TW:** 「因為“姐姐”也和哥哥說過同樣的話」
- **Cũ:** 「Vì "chị gái" cũng, nói y hệt như anh trai vậy.」
- **Mới:** 「Vì "chị gái" cũng nói y hệt như anh trai vậy.」
- **Lý do:** Bỏ dấu phẩy thừa sau "cũng".

#### [3184] — Khoảng trắng thừa cuối câu
- **JP:** あれは――果たしてどこでだったか――\nおや？
- **TW:** 那到底是在什麼地方來著？
- **Cũ:** Đó là——rốt cuộc là ở đâu nhỉ—— Ô? (có khoảng trắng cuối)
- **Mới:** Đó là——rốt cuộc là ở đâu nhỉ—— Ô?
- **Lý do:** Cắt khoảng trắng thừa cuối giá trị.

#### [3243] — VN tự thêm "!"
- **JP:** （ぽんっ）
- **TW:** （啪）
- **Cũ:** （Bốp!）
- **Mới:** （Bốp）
- **Lý do:** JP không có dấu "!"; phân biệt với （パンっ！） ở 3242 → "（Bốp!）" (đã có "!" đúng).

#### [3247] — Thừa 1 dấu "!"
- **JP:** （ガシャンっ！！！！！！！）
- **TW:** （嘩啦！！！！！！）
- **Cũ:** （Choang!!!!!!!!）
- **Mới:** （Choang!!!!!!!）
- **Lý do:** JP có 7 dấu "！"; VN có 8 dấu "!" — thừa 1.

## Khối TOML để dán vào file (đã kiểm chứng parse được)

Khối dưới đây đã kiểm chứng parse được bằng tomllib, đúng 33 key, giá trị khớp đúng JSON bản sửa. Dán vào section `[script]` của file `00_Common/共通02_日々姫と真闇と人形と.txt.toml` (ghi đè đúng 33 key này, giữ nguyên mọi key khác).

```toml
[script]
1560 = "「\\x%lレイルロオド;#00ffc040;Railord%l;#;Ư!?」"
1872 = "「Cả đời cơ à. Thế thì chịu không nổi đâu. Vậy anh không hỏi nữa. Anh sẽ tự mình từ từ suy nghĩ vậy.」"
1880 = "「Ái chà, sắp ngã đấy? Cẩn thận cử động chứ.」"
1976 = "「Có gì đâu, thực sự rất đơn giản mà. \\x%lエアクラ;#00ffc040;Aircra%l;#; của tôi xuất sắc lắm đấy.」"
2009 = "「Thì thế, cái \\x%lエアクラ;#00ffc040;Aircra%l;#; đó...」\\n「\\x%lエアクラ;#00ffc040;Aircra%l;#;Ư!!?」"
2016 = "「Pyaaaaaaa!!!」"
2017 = "「Kyaaaa!?」"
2018 = "「Hyau!? Hya, á——Không sao! Em không sao! A! À ừm, em không sao, không bị thương gì cả.」"
2035 = "「Ây da, cái này thì đúng là——」"
2064 = "「Vâng. Anh đã bảo lưu ở đại học rồi.」"
2076 = "「Vì \"chị gái\" cũng nói y hệt như anh trai vậy.」"
2135 = "「Ohitoyo……Migita.」"
2162 = "「Nếu được vậy thì tốt quá, nhưng anh thì...」"
2163 = "「Anh cũng là một trong những người thừa kế. Nhưng người thừa kế số một, đương kim gia chủ nhà Migita hiện tại, là chị Mayami.」"
2167 = "「Tôi về rồi đây, chị Mayami. Anh về rồi đây, Hibiki.」"
2182 = "「Tôi là Hachiroku, Railord chuyên dụng cho chiếc đầu tiên mang số hiệu \\x%l8620;#00ffc040;8620%l;#; thuộc dòng \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; loại 8620 của \\x%l帝鉄;#00ffc040;Teitetsu%l;#;.」"
2201 = "「T, tôi là Migita Hibiki. Là học sinh của học viện Ohitoyo.」"
2209 = "「Phòng của anh thì nhà kho hay tủ âm tường cũng được. A, nhưng kho rượu thì……nếu được, xin tha cho anh.」"
2323 = "「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jutsu-sendo lại có.」"
2324 = "「Không. Một mình anh thì đến đêm…… chắc đến sáng mai là có thể xoay xở xong.」"
2413 = "「Nếu nghĩ đến sự suy thoái của Ohitoyo, thì đó chỉ là kết luận tất nhiên thôi. Việc mời nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; về sẽ mang lại sự phát triển ổn định.」"
2418 = "「Được ở phòng ông Taito thì vinh hạnh quá. Nếu được, mong chị dẫn đường cho tôi.」"
2433 = "「Cũng bị ép uống, nhưng chẳng khá khẩm gì. Có vẻ thể chất của tôi khác hẳn với đàn ông Kyushu rồi.」"
2443 = "「Đúng vậy nhỉ. Cảm ơn ngài đã nhắc nhở. ——Xin lỗi, ngài có thể quay lưng lại được không ạ?」"
2495 = "「Chuyện mời nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; về Ohitoyo. Bây giờ tiến triển đến đâu rồi chị?」"
2563 = "「Chuyện đó——chắc là vậy ạ. Cha nuôi ở Đế đô cũng đối xử rất tốt với tôi.」"
2693 = "Không hổ danh là đương kim gia chủ nhà Migita—— \"Nữ trưởng hầm rượu nhà Migita xứ Kuma\"."
2695 = "Không gọi là chị hai, mà cố tình gọi là chị gái. Bốn chữ \"chị em cãi nhau\" hiện lên trong đầu tôi."
2848 = "Sự lộng lẫy đến mức tạo ra cảm giác áp đảo ấy―― Giúp tôi cảm nhận được một cách chân thực rằng tôi đã trở về nhà Migita."
3009 = "Đúng vậy, kể từ khi được nhận nuôi ở ngôi nhà này tại Ohitoyo, tôi mới biết. Rằng nước, rằng đá lại có thể ngon đến thế này."
3184 = "Đó là——rốt cuộc là ở đâu nhỉ—— Ô?"
3243 = "（Bốp）"
3247 = "（Choang!!!!!!!）"
```

## Gasp cross-check với sweep (đã kiểm chứng)

- Sweep đã sửa, **xác nhận đúng, không trùng lặp trong danh sách này:** 2194 (lost-gasp-whole, fix "chúng tôiƯ!!" — giữ nguyên, vì VN là câu dài theo TW, gasp gắn với dấu "!!" cuối câu) và 2570 (lost-gasp-trailing, "vậy~Ư").
- Sweep bỏ sót, **audit này đã sửa:** 1560, 2009 (cả hai đều là っ sau tên riêng có thẻ %l).
- Sweep ghi needs-file-audit, **kiểm chứng đúng, không sửa:** 1942 (JP không có っ — câu tự giới thiệu "Tôi là Soutetsu", tên trần ở đây là tự giới thiệu, đúng), 2592 (「//////」 giống hệt JP/TW), 2894 (thành ngữ "ghét sư thì đừng ghét lây cả áo cà sa" dịch đúng 坊主と袈裟とは別物だ; TW "她和機車" là TW diễn đạt lạ, JP thắng).
- Quét bổ sung: toàn bộ 184 dòng JP có っ đã rà lại — các っ cuối từ nhấn mạnh (イケンばいっ, なかろーもんっ, たまらんっ, うおっ…), tiếng hét La-tinh (ぴゃあっ, きゃあっ) và gasp đã diễn thành chữ Việt ("á", "a", "ưm", "uây", "Khụ") đều đúng, không cần thêm Ư. Trường hợp 2273 (って) là trợ từ trích dẫn, không phải gasp.

## Đã kiểm tra và KHÔNG tính là sai

- **1884** (Hachiroku giải thích tên Mayami/Soutetsu): "cặp đường sắt (Soutetsu)... tức là đường ray" hơi vụng nhưng ý đúng; tên trần "Soutetsu" ở đây là giải thích từ nguyên tên, không phải xưng hô — B4 không áp dụng.
- **1887/1888** (「無くて？」「いや」): câu ngắn, ngữ cảnh phân mảnh; VN "Không phải ý đó? / Không cần đâu." nhất quán với TW ("不是那個？/不用") và đọc được — giữ nguyên, không đoán sửa.
- **1972/2100/2133/2193/2224/2435/2536/2550** — Soutetsu gọi Hachiroku là "cô": đúng (nữ, trang trọng); Hachiroku tự xưng "Em" theo docs.
- **2133** (câu cụt 「そこからを」): VN hoàn thiện tối thiểu, giữ đúng nghĩa — giữ nguyên.
- **2211** ("Xin lỗi. Tôi đã hiểu lầm rất lớn."): người nghe mơ hồ (Hibiki hay Hachiroku đều có thể) — giữ "tôi" (mặc định docs).
- **2377** ("...nhưng anh đi một lát nhé."): hai người nghe Mayami + Hibiki cùng lúc — "anh" hướng về Hibiki là chấp nhận được.
- **2396** ("Quả thực, rất đẹp."): 見事だ trong ngữ cảnh phòng vừa dọn sạch — "đẹp" hơi lệch nhưng không rõ sai.
- **2514** (Hibiki gọi Soutetsu là "cậu" cho あなた): JP cố tình dùng あなた thay vì 兄さん (ngượng ngùng, giữ khoảng cách) — "cậu" giữ được khoảng cách đó; phán đoán, không tính sai.
- **2026** (おっと → "Ái chà."): biến thể chấp nhận được của tiền lệ おっと→"Ối" (h7 861/h8 2179).
- **2205** (アホーーーーーっ → "ngốốốốốốc!"): đếm đúng (6 âm ố = 1+5; "c" cuối diễn tả っ) — giữ nguyên.
- **2057** (きゃあっ → "Kyaa!"): tiếng hét La-tinh, chấp nhận theo tiền lệ h6 "Hyafu".
- **3008** ("Mình nghe nhầm sao?"): độc thoại tự vấn — "mình" được phép theo ngoại lệ (tiền lệ h3 1683, h8 3087/3726). Đối chiếu 2848 (đã sửa) là tường thuật khách quan, không phải tự vấn.
- **"mình" phản thân:** 1872 ("tự mình"), 1981 ("của mình"), 2160 ("bản thân mình"), 2170 ("của mình"), 3000 ("mình là con nuôi" — mệnh đề phụ), 3186 ("việc mình cần làm") — đều là phản thân/sở hữu, không phải tự xưng — giữ nguyên.
- **"nhà mình / tụi mình":** 2020, 2097, 2313, 2368 — "nhà mình" = nhà chung, đúng.
- **2009 vs CSV:** giá trị TOML chứa `\n` dạng text (raw `\\n`) — khớp CSV; chỉ lệch khoảng trắng cuối so với CSV, không phải lỗi nội dung.
- **"Migita System":** không xuất hiện trong file (2806 dùng "xưởng nấu rượu shochu Kuma" — đúng).
- **B4 (tên trần "Soutetsu"):** 3 chỗ xuất hiện — 1884 (giải thích từ nguyên, đúng), 1942 (tự giới thiệu "Tôi là Soutetsu / Migita Soutetsu", đúng) — không có trường hợp Paulette gọi tên trần trong file này (Paulette không xuất hiện).

## Ghi nhận về nguồn dữ liệu — CSV3 có HAI bộ dòng cho file này

Giống bẫy lr_ふかみh2 và 共通03: CSV3 liệt kê file này hai lần với cùng 467 key nhưng nội dung khác nhau:

- Bộ `translation_toml\00_Common\...` (STALE — bỏ): VN khớp TOML chỉ **31/467**, JP khớp comment TOML chỉ **253/467** (lệch 214 dòng). Ví dụ 2781: bộ này ghi "Bàn trà thấp, dày dặn, làm từ một tấm ván nguyên khối." trong khi TOML ghi "Chiếc bàn ngồi bệt bằng gỗ nguyên khối dày cộp." — đây là một bản dịch khác (hoặc bản nháp cũ), **không được dùng để audit hay rebuild**.
- Bộ `translation_toml\02_Hibiki\...` (DÙNG — đúng): JP khớp comment TOML **467/467**, VN khớp TOML **466/467** (chỉ 2009 lệch khoảng trắng cuối). **Mọi audit/rebuild của file này phải dùng bộ 02_Hibiki.**
- TOML-2 chỉ có MỘT file (dưới `00_Common/`), md5 `170e26e6b14a6decfb7f42fbd1ffe95d`, không có bản sao trùng lặp.
- Số dòng thực của file là **467**, không phải 934 (934 là tổng hai bộ CSV cộng lại).

## Kết bài

00_Common file 02 là file sạch nhất về cấu trúc trong các file đã audit: **0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 VN trùng lặp, 0 dòng không chắc chắn** — mọi lỗi đều là lỗi dịch tại chỗ, không phải lỗi hệ thống. Lỗi lớn nhất là xưng hô Soutetsu (13 dòng): người dịch cũ xưng "em" cho Soutetsu một cách tùy tiện, bất kể người nghe là em gái Hibiki ("anh") hay Mayami/Hachiroku ("tôi"). Sau đợt này, file sạch hoàn toàn "Ohimitera" (5/5 đã sửa) và không còn dòng "em" tự xưng sai nào của Soutetsu. Gasp っ còn sót 2 dòng sau tên riêng có thẻ %l (sweep bỏ sót) — đã bắt đủ. Đợt kiểm tra thứ hai: **33/33 bản sửa đọc lại đối chiếu JP, 33 xác nhận, 0 loại bỏ, 7 sửa lại** (bỏ dấu 「」 thêm thừa ở 7 dòng độc thoại). Khối TOML 33 key đã kiểm chứng parse được bằng tomllib, giá trị khớp JSON.
