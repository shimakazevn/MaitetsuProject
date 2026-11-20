# Audit: ふかみh1_ともはり練習.txt.toml (07_Nagi_Fukami)

- File: `translation_toml/07_Nagi_Fukami/ふかみh1_ともはり練習.txt.toml`
- TOML md5: `be7f335b835a741dab4d414880f9aacd` — không có bản trùng (md5 duy nhất trong 227 file TOML).
- Đọc: **272/272 dòng script** (key 755–1684), đối chiếu từng dòng với JP + TW từ CSV3. Nội dung: cảnh h Fukami — buổi hẹn riêng hai người luyện tập chèo thuyền (ともはり練習) trên thuyền xuôi dòng: Fukami lau người cho Soutetsu, hai người ân ái trên thuyền, xen kẽ đối thoại về số lần hẹn hò riêng (Fukami 2 lần, Nagi 1 lần).
- **Sai: 98/272 (36,0%)**.
- Phân loại: lệch dòng 88 · thở gấp (gasp っ) 5 · SFX 2 · dịch sai nghĩa 2 · nhãn 「」 1.
- Lệch vị trí: **88** · chuỗi xoay: **6 chuỗi** (56 + 21 + 5 + 6 + 1 + 1, xem §1) · dòng mồ côi: **2 xác nhận + 4 chưa rõ** · chưa dịch: **0** · trùng key: **0** · thẻ %l: **0** trong file · `[selections]` rỗng.
- Cơ sở tổng: **116 file / 5.436 dòng sai** (xác minh từ ROUTE-AUDIT.md, dòng tổng cuối cùng). Sau file này: **117 file / 5.534 dòng sai**.

## §1. Lệch dòng — 88 dòng, 6 chuỗi xoay

CSV3 có **2 bộ** cho file này (544 dòng = 2 × 272): bộ thư mục home `translation_toml\07_Nagi_Fukami\` chỉ khớp TOML **1/272** VN, JP khác 188/272 dòng — bộ CŨ, KHÔNG dùng. Bộ `translation_toml\11_Other\` khớp TOML 272/272 (sau khi tính TOML-2 flatten `\n` thành khoảng trắng) — audit bộ này. Đây là file dual-set thứ 11 (brief ghi 10 file đã biết). TOML-2 flatten literal `\n` thành khoảng trắng ở 151/272 dòng — CSV3 (literal `\n`) là chuẩn cho fix list. Chú thích `# JP:` trong TOML khớp CSV3 (bộ 11_Other) 272/272.

Không có dòng Nagi nào trong file — không cần kiểm tra quy tắc Nagi→Fukami "bé". Soutetsu xưng "anh" với Fukami đúng nhất quán trong thoại (782, 944, 948, 1069, 1079, 1112...); độc thoại dùng "tôi" đúng. Fukami tự xưng "em" đúng; không có "chị" nào sai. Không có raw っ trong VN. Không có thuật ngữ quyết định nào xuất hiện trong file (日ノ本, 電車姫, 市電, 御一夜, 宮司, Migita... đều 0).

84/98 bản sửa khôi phục được ngay trong file (VN đúng đang nằm ở key khác); 14 bản sửa viết mới. Trong 88 dòng lệch: 82 khôi phục được, 6 dòng không còn VN đúng trong file nên viết mới: 993, 1059, 1065, 1123, 1309, 1675. 6 chuỗi xoay (mũi tên = VN tại key trước là bản dịch của JP tại key sau):

- Chuỗi 1 (56 key, gồm 969 + 781 là SFX chen vào): 1309 → 1442 → 1659 → 1358 → 1015 → 1535 → 1106 → 1085 → 1378 → 1440 → 1133 → 1476 → 1499 → 1014 → 1045 → 1580 → 1326 → 1003 → 1651 → 1001 → 1681 → 1253 → 1300 → 987 → 1553 → 992 → 1382 → 1263 → 1654 → 969 → 1655 → 1068 → 1305 → 1453 → 1026 → 1083 → 1465 → 1379 → 1019 → 952 → 1319 → 1520 → 1107 → 1121 → 1500 → 1484 → 1018 → 1581 → 1312 → 981 → 1074 → 1053 → 1093 → 762 → 1064 → 781.
- Chuỗi 2 (21 key): 1123 → 1135 → 1561 → 1088 → 1473 → 1431 → 1129 → 1087 → 1588 → 1451 → 1100 → 772 → 1307 → 1533 → 1118 → 1455 → 1385 → 942 → 1387 → 1496 → 1034.
- Chuỗi 3 (5 key): 993 → 1117 → 1546 → 990 → 1031.
- Chuỗi 4 (6 key): 1059 → 995 → 1116 → 1678 → 1039 → 1081.
- Đơn 1065 và đơn 1675 (VN mồ côi, bản sửa viết mới).

2 VN mồ côi **xác nhận** (đã tìm toàn dự án TOML-2, chỉ xuất hiện ở file này, không có JP nguồn): 781 `（Ùm m m m m m m m m m m m!!!）`, 1065 `「Tình yêu! Hoàn toàn có thể làm được mà!!」`. 4 VN không khớp còn lại có thể là bản dịch lỏng của JP khác trong file (1031 "Thích em hơn" ~ JP 1081/1123; 1034 "Chà!" ~ JP 1065 っと; 1081 "Hể!!?" ~ JP 993 ふえっ; 1675 "Ưm!?" ~ JP 1059 んぬっ) — không dùng, đã viết mới cho 4 JP đó; xem §7 Chờ Hieu.

- **762** [monologue] JP: ……懸命に、ふかみが僕を拭ってくれてる。\n拭ってくれているのは実に、ありがたいのだが―― / Cũ: 「Ây da, ây da——chà, chà——chà, chà.」 / Mới: ……Fukami đang ra sức lau người cho tôi.\nĐược em ấy lau cho thì đúng là biết ơn thật đấy, nhưng mà—— (bản dịch đúng đang nằm ở key 1093)
- **772** [双鉄H] JP: 「……“平等でなくとも公平”――か」 / Cũ: Tại sao số lần lại không bằng nhau, cho đến khi được hai người giải thích,\ntôi vẫn cảm thấy thật kỳ lạ, nhưng mà…… / Mới: 「……“Dù không bình đẳng nhưng vẫn công bằng”——sao.」 (bản dịch đúng đang nằm ở key 1100)
- **942** [双鉄H] JP: 「しかし……川下り船でとはな」 / Cũ: Cảm giác vượt qua được thử thách khiến tôi vô tình thốt lên những lời nhẹ nhõm. / Mới: 「Nhưng mà……không ngờ lại làm chuyện này trên thuyền xuôi dòng.」 (bản dịch đúng đang nằm ở key 1385)
- **952** [双鉄H] JP: 「一生懸命拭いてもらえたおかげで僕は――\nすっかり、熱くなってしまった」 / Cũ: Theo từng nhịp lau, nó cứ tiến lại gần rồi lại lùi ra xa,\ntừng giọt, từng giọt nước nhỏ xuống mặt tôi. / Mới: 「Nhờ em lau người cho nhiệt tình quá nên anh——\nĐã hoàn toàn nóng lên mất rồi.」 (bản dịch đúng đang nằm ở key 1019)
- **981** [双鉄H] JP: 「いや……うむ」 / Cũ: 「Em xin lỗi. Em đang đun nước tắm rồi nhưng……\nChắc là vẫn còn phải mất thêm một lúc nữa.」 / Mới: 「Không sao……ưm.」 (bản dịch đúng đang nằm ở key 1312)
- **987** [ふかみ] JP: 「ふぁっ――あっ――わたしの――おまんこっ――\n双鉄、さんの――おくちっ――おくち、でっ――」 / Cũ: （Liếm! Liếm——chụt——ngoạm!」 / Mới: 「Phù——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」 (bản dịch đúng đang nằm ở key 1300)
- **990** [双鉄H] JP: 「うぉっ！？」 / Cũ: 「Hả!? Ơ!? T, tại sao——vậy, ạ?」 / Mới: 「Uoa!?」 (bản dịch đúng đang nằm ở key 1546)
- **992** [ふかみ] JP: 「ふぁ、あっ――べろ……あったか……いっ……んうっ」 / Cũ: Ngay từ đầu đã tung hết sức, tôi hôn lên đường rãnh dọc đang in hằn qua lớp quần lót,\nrồi cứ thế thè lưỡi liếm láp thật mạnh. / Mới: 「Phù, ah——lưỡi……ấm……quá……ưm.」 (bản dịch đúng đang nằm ở key 1553)
- **993** [ふかみ] JP: 「ふえっ！！？」 / Cũ: 「Tại sao á, vì anh đã thích Fukami mất rồi.」 / Mới: 「Phuê!?」 (viết mới — không còn VN đúng trong file)
- **995** [ふかみ] JP: 「えっ！？　あっ！　双鉄さん、今こっちに来ちゃっ――\nきゃっ！？　わあああああっ！？」 / Cũ: 「Fukami!?」 / Mới: 「Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\nÁ!? Oa a a a a a a a!?」 (bản dịch đúng đang nằm ở key 1059)
- **1001** [ふかみ] JP: 「あ……や……しみ、てるっ――ん――わたし、おまんこ――双鉄さんの、ツバが……、しみ、て――あつ、くて」 / Cũ: （Liếm! Liếm! Liếm! Nhóp nhép!） / Mới: 「A……ya……thấm, vào rồi——ưm——em, âm đạo——nước bọt của anh Soutetsu……, thấm, vào——nóng, quá.」 (bản dịch đúng đang nằm ở key 1651)
- **1003** [ふかみ] JP: 「あっ――ふっ――やけ、て――とけ、ちゃうっ――\nわた、しの――おまんこっ――ん――とけちゃう、よぉ」 / Cũ: （Rột——chụt! Nhóp nhép! Ực!） / Mới: 「Ah——phù——cháy, mất——tan chảy, mất——\nCủa, em——âm đạo——ưm——tan chảy, mất thôi.」 (bản dịch đúng đang nằm ở key 1326)
- **1014** [ふかみ] JP: 「あ……は、はい。――そう、ですよね。\nわた……し、こんなに――ぐしょぐしょ……で」 / Cũ: 「Ưm——phù. Em ướt sũng hết cả rồi.\nThế này mà không cởi ra……thì Fukami sẽ bị cảm lạnh mất.」 / Mới: 「A……v, vâng. ——Đúng, vậy nhỉ.\nEm……cũng, ướt nhẹp……thế này, rồi.」 (bản dịch đúng đang nằm ở key 1499)
- **1015** [ふかみ] JP: 「あ……わた、し……わた、し……おま、んこ……\n双鉄さんの……お顔の……こんな……こんな近く、で」 / Cũ: Màng nhĩ tôi rung lên dễ chịu bởi giọng nói đầy vui sướng,\ntôi từ từ lột lớp vải đang dính chặt ra, cởi sạch phần dưới của Fukami. / Mới: 「A……của, em……của, em……âm, đạo……\nKhuôn mặt của……anh Soutetsu……gần……gần thế này.」 (bản dịch đúng đang nằm ở key 1358)
- **1018** [ふかみ] JP: 「あ……まだこの辺、全然拭けて無いですね。\nごめんなさい――ん……よいしょ、よい、っしょ」 / Cũ: Vì thế, bồn tắm ở đây cực kỳ lớn,\nnên việc đun nước cũng mất khá nhiều thời gian——nghe nói là vậy. / Mới: 「A……chỗ này vẫn chưa lau được chút nào cả.\nEm xin lỗi——ưm……ây da, ây, da.」 (bản dịch đúng đang nằm ở key 1484)
- **1019** [ふかみ] JP: 「あ――」 / Cũ: 「Nhờ em lau người cho nhiệt tình quá nên anh——\nĐã hoàn toàn nóng lên mất rồi.」 / Mới: 「A——」 (bản dịch đúng đang nằm ở key 1379)
- **1026** [ふかみ] JP: 「あっ！　はい！　はい！　おねがいしますっ！！」 / Cũ: 「Đúng hơn là, Fukami đang ướt sũng rồi kìa.\nNếu em không phiền——anh rất sẵn lòng giúp em lau người đấy?」 / Mới: 「A! Vâng! Vâng! Trăm sự nhờ anh ạ!!」 (bản dịch đúng đang nằm ở key 1453)
- **1031** [ふかみ] JP: 「え！？　ええっ！？　な、なんで――です、か？」 / Cũ: 「“Thích em hơn” sao? Chuyện đó là không thể nào.」 / Mới: 「Hả!? Ơ!? T, tại sao——vậy, ạ?」 (bản dịch đúng đang nằm ở key 990)
- **1034** [ふかみ] JP: 「あ、上手です。双鉄さん。\n今のだったら、揺らさずに瀬を乗り越えられます」 / Cũ: 「Chà!」 / Mới: 「A, giỏi quá. Anh Soutetsu.\nNếu làm như vừa nãy, anh có thể vượt qua dòng thác mà không bị tròng trành đấy.」 (bản dịch đúng đang nằm ở key 1496)
- **1039** [ふかみ] JP: 「好き……好きって……双鉄さんが、わたしのことを――\nすでに好き、って……ふあ、ぁっ」 / Cũ: 「Chắc chắn là sẽ “thích nhiều hơn”, “thích hơn nữa”……\nNhưng một người đã thích Fukami như anh, thì làm sao có chuyện “bắt đầu thích” được nữa.」 / Mới: 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……phù, ah.」 (bản dịch đúng đang nằm ở key 1678)
- **1045** [双鉄H] JP: 「ん――ぷぁ。随分と濡れてしまっているな。\nこれは脱がんと……ふかみこそ風邪を引きかねん」 / Cũ: Dù độ dày có lẽ chưa đến vài milimet,\nnhưng chiếc quần lót ướt sũng dính chặt này thực sự quá vướng víu. / Mới: 「Ưm——phù. Em ướt sũng hết cả rồi.\nThế này mà không cởi ra……thì Fukami sẽ bị cảm lạnh mất.」 (bản dịch đúng đang nằm ở key 1014)
- **1053** [双鉄H] JP: 「う……うむ」 / Cũ: 「Chà, chà——lau, lau——ưm……sao rồi ạ?\nAnh Soutetsu đã khô bớt chút nào chưa?」 / Mới: 「Ư……ưm.」 (bản dịch đúng đang nằm ở key 1074)
- **1059** [双鉄H] JP: 「んぬっ！？」 / Cũ: 「Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\nÁ!? Oa a a a a a a a!?」 / Mới: 「Ưm nu!?」 (viết mới — không còn VN đúng trong file)
- **1064** [ふかみ] JP: 「よいしょ、よいしょ――ごし、ごし――ごし、ごし」 / Cũ: 「……Ư……ưm…………ưm…………」 / Mới: 「Ây da, ây da——chà, chà——chà, chà.」 (bản dịch đúng đang nằm ở key 762)
- **1065** [双鉄H] JP: 「っと！」 / Cũ: 「Tình yêu! Hoàn toàn có thể làm được mà!!」 / Mới: 「Ối!」 (viết mới — không còn VN đúng trong file)
- **1068** [双鉄H] JP: 「ならば」 / Cũ: Vì tôi mãi không thể xác định được đó có phải là cám dỗ hay không,\nnên có vẻ như tôi đã vô tình khiến Fukami phải nóng lòng chờ đợi. / Mới: 「Nếu vậy thì.」 (bản dịch đúng đang nằm ở key 1655)
- **1074** [ふかみ] JP: 「ごめんなさい。お風呂沸かしてるんですけど……\n時間、まだまだかかっちゃいますから」 / Cũ: 「Ư……ưm.」 / Mới: 「Em xin lỗi. Em đang đun nước tắm rồi nhưng……\nChắc là vẫn còn phải mất thêm một lúc nữa.」 (bản dịch đúng đang nằm ở key 981)
- **1081** [双鉄H] JP: 「“もっと好き”“更に好き”にならなれるだろうが……\n既にふかみを好きな僕が、“好きになる”のは不可能だ」 / Cũ: 「Hể!!?」 / Mới: 「Chắc chắn là sẽ “thích nhiều hơn”, “thích hơn nữa”……\nNhưng một người đã thích Fukami như anh, thì làm sao có chuyện “bắt đầu thích” được nữa.」 (bản dịch đúng đang nằm ở key 1039)
- **1083** [双鉄H] JP: 「むしろ、ふかみがぐしょぐしょに濡れてしまってる。\n僕でよければ――拭くのを、喜んで手伝うが？」 / Cũ: Fukami nhận ra điều đó, nhưng không hề ngoảnh mặt đi.\nNếu vậy thì, quả nhiên——đây chắc chắn là một sự cám dỗ rồi. / Mới: 「Đúng hơn là, Fukami đang ướt sũng rồi kìa.\nNếu em không phiền——anh rất sẵn lòng giúp em lau người đấy?」 (bản dịch đúng đang nằm ở key 1026)
- **1085** [ふかみ] JP: 「だから……下……あの、下、は――できっ、でき――\nでき、たら……そのっ！　双鉄、さん――に……」 / Cũ: Cơ thể ngày càng nóng lên,\nnhững phần da thịt chạm vào nhau ướt đẫm mồ hôi của cả hai. / Mới: 「Vì thế……phần dưới……ừm, phần dưới——nếu, nếu——\nNếu được……ừm! Nhờ anh, Soutetsu——làm, giúp em……」 (bản dịch đúng đang nằm ở key 1106)
- **1087** [ふかみ] JP: 「だから、ふたりきりデートは、わたしが二回で、\n凪ちゃんが一回。これで、ぎりぎり公平かなって」 / Cũ: Chỉ là vậy thôi, nhưng không hiểu sao\ntôi lại cảm nhận được một sức ép khó tả. / Mới: 「Vì vậy, hẹn hò riêng hai người, em sẽ được hai lần,\ncòn bé Nagi một lần. Thế này là vừa đủ công bằng rồi nhỉ.」 (bản dịch đúng đang nằm ở key 1129)
- **1088** [ふかみ] JP: 「それでわたし、一回目は見てもらおうって思ったんです。\n自分のホームで、船頭をしてるわたしの姿――」 / Cũ: Sức ép bí ẩn trong giọng nói của Fukami cũng hoàn toàn biến mất,\nthay vào đó, em ấy bắt đầu trở nên vui vẻ, hào hứng. / Mới: 「Vì vậy, em muốn anh xem lần đầu tiên.\nHình ảnh em đang chèo thuyền trên sân nhà của mình——」 (bản dịch đúng đang nằm ở key 1561)
- **1093** [ふかみ] JP: 「ごし、ごし――ふき、ふき――ん……どうでしょう？\nだいぶ、双鉄さん乾きましたか？」 / Cũ: ……Fukami đang ra sức lau người cho tôi.\nĐược em ấy lau cho thì đúng là biết ơn thật đấy, nhưng mà—— / Mới: 「Chà, chà——lau, lau——ưm……sao rồi ạ?\nAnh Soutetsu đã khô bớt chút nào chưa?」 (bản dịch đúng đang nằm ở key 1053)
- **1100** [ふかみ] JP: 「ですね。[じゅっぷん,1]十分の差も無いことですけど、\n双鉄さんの、初めてのエッチの相手は……凪ちゃん」 / Cũ: 「……“Dù không bình đẳng nhưng vẫn công bằng”——sao.」 / Mới: 「Đúng vậy. Dù chênh lệch chưa đến mười phút,\nnhưng người đầu tiên làm tình với anh Soutetsu là……bé Nagi.」 (bản dịch đúng đang nằm ở key 1451)
- **1106** [双鉄H] JP: 「望むところだ」 / Cũ: 「Vì thế……phần dưới……ừm, phần dưới——nếu, nếu——\nNếu được……ừm! Nhờ anh, Soutetsu——làm, giúp em……」 / Mới: 「Chính là điều anh đang mong đợi đấy.」 (bản dịch đúng đang nằm ở key 1535)
- **1107** [双鉄H] JP: 「いや――風邪をひく心配はなかろうさ」 / Cũ: 「Nếu để anh Soutetsu bị cảm lạnh thì em thấy có lỗi lắm.\nEm sẽ lau cho anh bao nhiêu cũng được.」 / Mới: 「Không sao đâu——chắc là không lo bị cảm lạnh đâu.」 (bản dịch đúng đang nằm ở key 1520)
- **1116** [双鉄H] JP: 「ふかみっ！？」 / Cũ: （Tròng trành!） / Mới: 「Fukami!?」 (bản dịch đúng đang nằm ở key 995)
- **1117** [双鉄H] JP: 「何故って、僕は、すでにふかみを好きだからだ」 / Cũ: Chiếc thuyền rung lắc dữ dội dù không phải ở chỗ nước chảy xiết.\nPhản ứng đó khiến tôi nhận ra lời nói của mình thiếu sót trầm trọng. / Mới: 「Tại sao á, vì anh đã thích Fukami mất rồi.」 (bản dịch đúng đang nằm ở key 993)
- **1118** [ふかみ] JP: 「二回もチャンスがあるんだから、\n一回目は、自分のホームで――って、思ったんです」 / Cũ: Mong muốn của Fukami là,\nđược cùng tôi luyện tập chèo thuyền, chỉ có hai người với nhau. / Mới: 「Vì có tận hai cơ hội mà,\nnên em nghĩ, lần đầu tiên sẽ ở sân nhà của mình——」 (bản dịch đúng đang nằm ở key 1533)
- **1121** [ふかみ] JP: 「双鉄さんに、風邪とかひかせたら申し訳ないですし。\nわたし、いくらでも拭きますから」 / Cũ: Để tránh làm văng những giọt nước thừa thãi, em ấy bảo tôi nằm xuống,\nrồi ngồi lên trên, ra sức lắc lư eo, lau người cho tôi. / Mới: 「Nếu để anh Soutetsu bị cảm lạnh thì em thấy có lỗi lắm.\nEm sẽ lau cho anh bao nhiêu cũng được.」 (bản dịch đúng đang nằm ở key 1107)
- **1123** [双鉄H] JP: 「“好きになる”のか？　それは無理だ」 / Cũ: 「Một em, đã được anh Soutetsu……khen là đ, đẹp.\nEm muốn……anh Soutetsu……sẽ, sẽ thích, em, hơn nữa.」 / Mới: 「“Bắt đầu thích” sao? Chuyện đó là không thể nào.」 (viết mới — không còn VN đúng trong file)
- **1129** [双鉄H] JP: 「そうか」 / Cũ: 「Vì vậy, hẹn hò riêng hai người, em sẽ được hai lần,\ncòn bé Nagi một lần. Thế này là vừa đủ công bằng rồi nhỉ.」 / Mới: 「Vậy sao.」 (bản dịch đúng đang nằm ở key 1431)
- **1133** [ふかみ] JP: 「あ、あの――わたし――上は、自分――自分で、脱ぐっ\nその――脱ぎます、から――」 / Cũ: Từng giọt nước nhỏ xuống từ háng em như kéo thành sợi.\nEo của Fukami lại bắt đầu đung đưa, cọ quậy. / Mới: 「A, ừm——em——phần trên, em sẽ tự——tự cởi,\nừm——em sẽ cởi, nên——」 (bản dịch đúng đang nằm ở key 1440)
- **1135** [ふかみ] JP: 「双鉄さんが、う、美しいって……言ってくれたわたしで。\n双鉄さんに……す、好きに、なって、もらいたく、って」 / Cũ: Nói rồi, Fukami đứng thẳng lưng ở mũi thuyền.\nDù đang vươn thẳng người, đôi gò má em vẫn dần ửng đỏ. / Mới: 「Một em, đã được anh Soutetsu……khen là đ, đẹp.\nEm muốn……anh Soutetsu……sẽ, sẽ thích, em, hơn nữa.」 (bản dịch đúng đang nằm ở key 1123)
- **1253** [monologue] JP: けれどもそこにすぐさまに、\n熱さを帯びた薄い酸味の、ぬらつく蜜が混じり始める。 / Cũ: Không hẳn là tươi mát, mà đúng hơn là hương vị của nước lan tỏa trong miệng. / Mới: Nhưng ngay sau đó,\nvị mật ngòn ngọt, mang theo chút hơi ấm bắt đầu hòa quyện vào. (bản dịch đúng đang nằm ở key 1681)
- **1263** [monologue] JP: 焦らしてしまったことを少しでもお詫びしたくて。 / Cũ: （Chụt——rột——liếm——liếm liếm liếm） / Mới: Chỉ muốn bù đắp một chút cho việc đã khiến em ấy phải chờ đợi. (bản dịch đúng đang nằm ở key 1382)
- **1300** [monologue] JP: 瑞々しい、というよりもむしろ水そのものの味が広がり。 / Cũ: 「Phù——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」 / Mới: Không hẳn là tươi mát, mà đúng hơn là hương vị của nước lan tỏa trong miệng. (bản dịch đúng đang nằm ở key 1253)
- **1305** [monologue] JP: 誘惑かどうかの判断をなかなかつけかねていたせいで、\nふかみを焦らす形になってしまっていたかと思わせられる。 / Cũ: Giọng nói vui vẻ, hào hứng. / Mới: Vì tôi mãi không thể xác định được đó có phải là cám dỗ hay không,\nnên có vẻ như tôi đã vô tình khiến Fukami phải nóng lòng chờ đợi. (bản dịch đúng đang nằm ở key 1068)
- **1307** [monologue] JP: 何故に回数が同じでないのか、ふたりに説明されるまで、\n不思議に思ったものであったが…… / Cũ: Ba người……hay nói đúng hơn là, theo thỏa thuận thực tế giữa Fukami và Nagi,\nsố lần hẹn hò được chốt lại là Fukami hai lần, Nagi một lần. / Mới: Tại sao số lần lại không bằng nhau, cho đến khi được hai người giải thích,\ntôi vẫn cảm thấy thật kỳ lạ, nhưng mà…… (bản dịch đúng đang nằm ở key 772)
- **1309** [monologue] JP: 完全にフラットな腹のラインの先にぷるん、と、\n小ぶりなお椀の形の胸が、ピンクの乳首が見えている。 / Cũ: Phía bên kia âm đạo của Fukami. / Mới: Nơi tận cùng đường nét của vùng bụng hoàn toàn phẳng lì, một cặp ngực nhỏ hình bát úp, căng tròn,\nđang lộ ra với núm vú màu hồng. (viết mới — không còn VN đúng trong file)
- **1312** [monologue] JP: 隆盛を極めていた頃には、冬場の川下りも大繁盛で、\n冷えきった船頭さんたちに仕事後の風呂を提供していた。 / Cũ: 「Không sao……ưm.」 / Mới: Vào thời kỳ hưng thịnh, dịch vụ đi thuyền xuôi dòng vào mùa đông rất đắt khách,\nhọ thường cung cấp nước tắm sau giờ làm việc cho những người lái đò bị lạnh cóng. (bản dịch đúng đang nằm ở key 1581)
- **1319** [monologue] JP: 拭く動きにつれ、それが近づき、遠ざかっては、\nぽたりぽたりと僕の顔面に滴を落とす。 / Cũ: Ngay trước mắt tôi, là phần háng quần lót của Fukami đang banh rộng.\nNó ướt sũng, ngậm đầy nước và dính chặt vào da. / Mới: Theo từng nhịp lau, nó cứ tiến lại gần rồi lại lùi ra xa,\ntừng giọt, từng giọt nước nhỏ xuống mặt tôi. (bản dịch đúng đang nằm ở key 952)
- **1326** [monologue] JP: 溶かしてやりたい。もっと、もっとに舐めしゃぶり。\nだが、そうするにはこの薄衣が―― / Cũ: 「Ah——phù——cháy, mất——tan chảy, mất——\nCủa, em——âm đạo——ưm——tan chảy, mất thôi.」 / Mới: Anh muốn làm em tan chảy. Liếm láp, mút mát nhiều hơn, nhiều hơn nữa.\nNhưng để làm được điều đó, thì lớp vải mỏng này—— (bản dịch đúng đang nằm ở key 1580)
- **1358** [monologue] JP: 剥き出しになったおまんこを、\nあらためてまじ、と見てみれば―― / Cũ: 「A……của, em……của, em……âm, đạo……\nKhuôn mặt của……anh Soutetsu……gần……gần thế này.」 / Mới: Nhìn lại một lần nữa vào âm đạo đã hoàn toàn phơi bày,\ntôi chăm chú quan sát—— (bản dịch đúng đang nằm ở key 1659)
- **1378** [monologue] JP: 体がどんどん熱くなり、\n肌と肌とが触れ合う部分が、お互いの汗にぬらついていく。 / Cũ: Mùi hương trở nên nồng đậm hơn. / Mới: Cơ thể ngày càng nóng lên,\nnhững phần da thịt chạm vào nhau ướt đẫm mồ hôi của cả hai. (bản dịch đúng đang nằm ở key 1085)
- **1379** [monologue] JP: ふかみの鼻先、すぐのところで、\n僕の勃起がズボンを大きく持ち上げている。 / Cũ: 「A——」 / Mới: Ngay sát chóp mũi của Fukami,\ndương vật đang cương cứng của tôi đã nhô cao lên lớp quần. (bản dịch đúng đang nằm ở key 1465)
- **1382** [monologue] JP: 最初からもう全開で、パンツ越しに張り付き浮かぶ縦すじに、\nキスしてそのまま、思いっきりに舌を這わせる。 / Cũ: Chỉ muốn bù đắp một chút cho việc đã khiến em ấy phải chờ đợi. / Mới: Ngay từ đầu đã tung hết sức, tôi hôn lên đường rãnh dọc đang in hằn qua lớp quần lót,\nrồi cứ thế thè lưỡi liếm láp thật mạnh. (bản dịch đúng đang nằm ở key 992)
- **1385** [monologue] JP: ふかみと、凪と。\nそれぞれと僕との、ふたりきりでの一日デート。 / Cũ: 「Nhưng mà……không ngờ lại làm chuyện này trên thuyền xuôi dòng.」 / Mới: Với Fukami, và Nagi.\nMột buổi hẹn hò trọn vẹn một ngày chỉ có hai người với từng người. (bản dịch đúng đang nằm ở key 1455)
- **1387** [monologue] JP: 乗り切ったという感覚に、ついつい口も軽くなる。 / Cũ: Vượt qua dòng thác này, một lúc sau,\nchỉ cần để thuyền trôi lững lờ theo dòng nước là được. / Mới: Cảm giác vượt qua được thử thách khiến tôi vô tình thốt lên những lời nhẹ nhõm. (bản dịch đúng đang nằm ở key 942)
- **1431** [monologue] JP: ふかみと凪との、それが決定事項なら、\n僕があれこれ口をはさむべきことでも無い。 / Cũ: 「Vậy sao.」 / Mới: Nếu đó là quyết định của Fukami và Nagi,\nthì tôi cũng không nên xen mồm vào làm gì. (bản dịch đúng đang nằm ở key 1473)
- **1440** [monologue] JP: 匂いが濃くなる。 / Cũ: 「A, ừm——em——phần trên, em sẽ tự——tự cởi,\nừm——em sẽ cởi, nên——」 / Mới: Mùi hương trở nên nồng đậm hơn. (bản dịch đúng đang nằm ở key 1378)
- **1442** [monologue] JP: ふかみのおまんこの、その向こう。 / Cũ: （Ồ……） / Mới: Phía bên kia âm đạo của Fukami. (bản dịch đúng đang nằm ở key 1309)
- **1451** [monologue] JP: 淡々とした口調で、事実を述べている。 / Cũ: 「Đúng vậy. Dù chênh lệch chưa đến mười phút,\nnhưng người đầu tiên làm tình với anh Soutetsu là……bé Nagi.」 / Mới: Em ấy đang nói ra sự thật với giọng điệu đều đều. (bản dịch đúng đang nằm ở key 1588)
- **1453** [monologue] JP: 弾む声。 / Cũ: 「A! Vâng! Vâng! Trăm sự nhờ anh ạ!!」 / Mới: Giọng nói vui vẻ, hào hứng. (bản dịch đúng đang nằm ở key 1305)
- **1455** [monologue] JP: ふかみの希望は、僕のともはり練習を、\nふたりっきりでたっぷり行うことだった。 / Cũ: Với Fukami, và Nagi.\nMột buổi hẹn hò trọn vẹn một ngày chỉ có hai người với từng người. / Mới: Mong muốn của Fukami là,\nđược cùng tôi luyện tập chèo thuyền, chỉ có hai người với nhau. (bản dịch đúng đang nằm ở key 1118)
- **1465** [monologue] JP: ふかみはそれを認識し、少しも顔をそらしはしない。\nならば、やはり――これは、誘惑に違いなかろう。 / Cũ: Ngay sát chóp mũi của Fukami,\ndương vật đang cương cứng của tôi đã nhô cao lên lớp quần. / Mới: Fukami nhận ra điều đó, nhưng không hề ngoảnh mặt đi.\nNếu vậy thì, quả nhiên——đây chắc chắn là một sự cám dỗ rồi. (bản dịch đúng đang nằm ở key 1083)
- **1473** [monologue] JP: ふかみの声からも謎の迫力が綺麗に失せて、\nむしろ楽しげに弾み始める。 / Cũ: Nếu đó là quyết định của Fukami và Nagi,\nthì tôi cũng không nên xen mồm vào làm gì. / Mới: Sức ép bí ẩn trong giọng nói của Fukami cũng hoàn toàn biến mất,\nthay vào đó, em ấy bắt đầu trở nên vui vẻ, hào hứng. (bản dịch đúng đang nằm ở key 1088)
- **1476** [monologue] JP: 股間から糸をひくように滴が落ちる。\nふかみの腰が、またもじもじと揺れ動く。 / Cũ: Tỏng——tỏng. / Mới: Từng giọt nước nhỏ xuống từ háng em như kéo thành sợi.\nEo của Fukami lại bắt đầu đung đưa, cọ quậy. (bản dịch đúng đang nằm ở key 1133)
- **1484** [monologue] JP: だから、ふかみは僕を拭く。\n濡れてスケスケの服を、下着を、そのまま身につけながら。 / Cũ: 「A……chỗ này vẫn chưa lau được chút nào cả.\nEm xin lỗi——ưm……ây da, ây, da.」 / Mới: Vì thế, Fukami đang lau người cho tôi.\nTrong khi vẫn đang mặc nguyên bộ quần áo, đồ lót ướt sũng, mỏng tang. (bản dịch đúng đang nằm ở key 1500)
- **1496** [monologue] JP: この瀬を抜ければしばらくは、\n流されるままに漂うだけだ。 / Cũ: 「A, giỏi quá. Anh Soutetsu.\nNếu làm như vừa nãy, anh có thể vượt qua dòng thác mà không bị tròng trành đấy.」 / Mới: Vượt qua dòng thác này, một lúc sau,\nchỉ cần để thuyền trôi lững lờ theo dòng nước là được. (bản dịch đúng đang nằm ở key 1387)
- **1499** [monologue] JP: ぽた――り。 / Cũ: 「A……v, vâng. ——Đúng, vậy nhỉ.\nEm……cũng, ướt nhẹp……thế này, rồi.」 / Mới: Tỏng——tỏng. (bản dịch đúng đang nằm ở key 1476)
- **1500** [monologue] JP: 無駄な水滴を飛ばさないよう僕を寝かせて、\nその上で、一生懸命、腰をふりふり、僕を拭く。 / Cũ: Vì thế, Fukami đang lau người cho tôi.\nTrong khi vẫn đang mặc nguyên bộ quần áo, đồ lót ướt sũng, mỏng tang. / Mới: Để tránh làm văng những giọt nước thừa thãi, em ấy bảo tôi nằm xuống,\nrồi ngồi lên trên, ra sức lắc lư eo, lau người cho tôi. (bản dịch đúng đang nằm ở key 1121)
- **1520** [monologue] JP: 目の前に、ふかみのパンツの股間が広がる。\n水をたっぷり含んで張り付き、濡れている。 / Cũ: 「Không sao đâu——chắc là không lo bị cảm lạnh đâu.」 / Mới: Ngay trước mắt tôi, là phần háng quần lót của Fukami đang banh rộng.\nNó ướt sũng, ngậm đầy nước và dính chặt vào da. (bản dịch đúng đang nằm ở key 1319)
- **1533** [monologue] JP: 三者……というか、実質的にはふかみと凪との合議により、\nふかみ二回、凪一回というデート回数でまとまった。 / Cũ: 「Vì có tận hai cơ hội mà,\nnên em nghĩ, lần đầu tiên sẽ ở sân nhà của mình——」 / Mới: Ba người……hay nói đúng hơn là, theo thỏa thuận thực tế giữa Fukami và Nagi,\nsố lần hẹn hò được chốt lại là Fukami hai lần, Nagi một lần. (bản dịch đúng đang nằm ở key 1307)
- **1535** [monologue] JP: 嬉しげな声に心地よく鼓膜を揺すられながら、\n張り付く布をゆっくり剥がし、ふかみの下を全部脱がせる。 / Cũ: 「Chính là điều anh đang mong đợi đấy.」 / Mới: Màng nhĩ tôi rung lên dễ chịu bởi giọng nói đầy vui sướng,\ntôi từ từ lột lớp vải đang dính chặt ra, cởi sạch phần dưới của Fukami. (bản dịch đúng đang nằm ở key 1015)
- **1546** [monologue] JP: 舟が揺れる、瀬でも無いのに激しく。\nその反応に、自分の言葉が著しく不足していたと知る。 / Cũ: 「Uoa!?」 / Mới: Chiếc thuyền rung lắc dữ dội dù không phải ở chỗ nước chảy xiết.\nPhản ứng đó khiến tôi nhận ra lời nói của mình thiếu sót trầm trọng. (bản dịch đúng đang nằm ở key 1117)
- **1553** [monologue] JP: （れるっ！　れろっ――じゅうううっ――はむっ！」 / Cũ: 「Phù, ah——lưỡi……ấm……quá……ưm.」 / Mới: （Liếm! Liếm——chụt——ngoạm!） (bản dịch đúng đang nằm ở key 987)
- **1561** [monologue] JP: 言ってふかみは、舳先でしゃん、と背筋を伸ばす。\n伸ばしながらもその頬が、じわじわ赤に染まってく。 / Cũ: 「Vì vậy, em muốn anh xem lần đầu tiên.\nHình ảnh em đang chèo thuyền trên sân nhà của mình——」 / Mới: Nói rồi, Fukami đứng thẳng lưng ở mũi thuyền.\nDù đang vươn thẳng người, đôi gò má em vẫn dần ửng đỏ. (bản dịch đúng đang nằm ở key 1135)
- **1580** [monologue] JP: 厚さ数ミリにも満たぬであろう、\n濡れて張り付くパンツがどうにも、邪魔すぎる。 / Cũ: Anh muốn làm em tan chảy. Liếm láp, mút mát nhiều hơn, nhiều hơn nữa.\nNhưng để làm được điều đó, thì lớp vải mỏng này—— / Mới: Dù độ dày có lẽ chưa đến vài milimet,\nnhưng chiếc quần lót ướt sũng dính chặt này thực sự quá vướng víu. (bản dịch đúng đang nằm ở key 1045)
- **1581** [monologue] JP: ゆえに、ここの風呂は非常に湯船が大きくて、\n沸かすのにも相当な時間が掛かってしまう――のだそうだ。 / Cũ: Vào thời kỳ hưng thịnh, dịch vụ đi thuyền xuôi dòng vào mùa đông rất đắt khách,\nhọ thường cung cấp nước tắm sau giờ làm việc cho những người lái đò bị lạnh cóng. / Mới: Vì thế, bồn tắm ở đây cực kỳ lớn,\nnên việc đun nước cũng mất khá nhiều thời gian——nghe nói là vậy. (bản dịch đúng đang nằm ở key 1018)
- **1588** [monologue] JP: ただそれだけのことなのに、\n言うに言われぬ迫力を何故か、感じてしまう。 / Cũ: Em ấy đang nói ra sự thật với giọng điệu đều đều. / Mới: Chỉ là vậy thôi, nhưng không hiểu sao\ntôi lại cảm nhận được một sức ép khó tả. (bản dịch đúng đang nằm ở key 1087)
- **1651** [monologue] JP: （じゅるっ――じゅううっ！　じゅぶうっ！　ごくっ！） / Cũ: 「A……ya……thấm, vào rồi——ưm——em, âm đạo——nước bọt của anh Soutetsu……, thấm, vào——nóng, quá.」 / Mới: （Rột——chụt! Nhóp nhép! Ực!） (bản dịch đúng đang nằm ở key 1003)
- **1654** [monologue] JP: （じゅっ――じゅるっ――れろっ――れろおおっ） / Cũ: 「Hya fu!」 / Mới: （Chụt——rột——liếm——liếm liếm liếm） (bản dịch đúng đang nằm ở key 1263)
- **1655** [monologue] JP: （じゅぶるっ！！） / Cũ: 「Nếu vậy thì.」 / Mới: （Nhóp nhép!!） (viết mới — không còn VN đúng trong file)
- **1659** [双鉄H] JP: （おお……） / Cũ: Nhìn lại một lần nữa vào âm đạo đã hoàn toàn phơi bày,\ntôi chăm chú quan sát—— / Mới: （Ồ……） (bản dịch đúng đang nằm ở key 1442)
- **1675** [monologue] JP: （ざっぼーーーーーーーーんっ！！！） / Cũ: 「Ưm!?」 / Mới: （Tõm——!!!） (viết mới — không còn VN đúng trong file)
- **1678** [monologue] JP: （ぐらっ！） / Cũ: 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……phù, ah.」 / Mới: （Tròng trành!） (bản dịch đúng đang nằm ở key 1116)
- **1681** [monologue] JP: （ぺろっ！　れろっ！　れりゅっ！　にゅるうっ！） / Cũ: Nhưng ngay sau đó,\nvị mật ngòn ngọt, mang theo chút hơi ấm bắt đầu hòa quyện vào. / Mới: （Liếm! Liếm! Liếm! Nhóp nhép!） (bản dịch đúng đang nằm ở key 1001)

## §2. Thở gấp (gasp っ) — 5 dòng

Quy tắc ranh giới gasp (khóa 20/11): thêm Ư chỉ khi âm っ hoàn toàn bị mất (cuối tuyệt đối / đầu dòng); không diễn kép っ đã được diễn. 5 dòng dưới đều mất hẳn âm っ.

- **979** [双鉄H] JP: 「っ――」 / Cũ: 「Kh——」 / Mới: 「Ư——」 (っ―― bị diễn thành "Kh——" (thêm phụ âm く không có trong JP))
- **1043** [双鉄H] JP: 「ん……っっ――んっ――ふっ――んっ」 / Cũ: 「Ưm……kh——ưm——phù——ưm」 / Mới: 「Ưm……ƯƯ——ưm——phù——ưm」 (っっ giữa dòng bị diễn thành "kh"; mỗi っ một Ư)
- **1058** [ふかみ] JP: 「っ！！？――あひゅうううううんっ！！！」 / Cũ: 「!!?——A hyu u u u u u ưm!!!」 / Mới: 「Ư!!?——A hyu u u u u u ưm!!!」 (っ đầu dòng bị mất hẳn)
- **1137** [双鉄H] JP: 「っ！！！」 / Cũ: 「!!!」 / Mới: 「Ư!!!」 (っ!!! cả dòng bị mất (sweep bỏ sót))
- **1403** [monologue] JP: 快感が強烈すぎるのか、\nふかみがイヤイヤと頭を振っ――っ！ / Cũ: Có lẽ vì khoái cảm quá mãnh liệt,\nFukami lắc đầu nguầy nguậy——! / Mới: Có lẽ vì khoái cảm quá mãnh liệt,\nFukami lắc đầu nguầy nguậy——Ư! (振っ――っ! cuối dòng bị mất; sweep đã cờ needs-file-audit, xác nhận đúng)

## §3. SFX + dịch sai + nhãn — 5 dòng

- **781** [双鉄H] JP: 「……う……むっ…………ぬっ…………」 / Cũ: （Ùm m m m m m m m m m m m!!!） / Mới: 「……Ư……ưm…………ưm…………」 (SFX rên bị diễn méo thành "(Ùm m m...!!!)" trong ngoặc đơn + 11 chữ m + !!!; khôi phục từ key 1064)
- **969** [ふかみ] JP: 「ひゃふっ！」 / Cũ: （Nhóp nhép!!） / Mới: 「Hya fu!」 (ひゃふっ là tiếng kêu, bị diễn thành tiếng liếm "(Nhóp nhép!!)"; khôi phục từ key 1654)
- **1011** [ふかみ] JP: 「あ……んっ――はっ――おっきい、ですっ――\n双鉄、さん、の――んっ――おなか――ささ、って――」 / Cũ: 「A……ưm——ha——to, quá ạ——\nBụng——của anh Soutetsu——đang đâm, vào——」 / Mới: 「A……ưm——ha——to, quá ạ——\nCủa anh Soutetsu——ưm——đang đâm vào bụng em——」 ("Bụng——của anh Soutetsu" gán bụng cho Soutetsu; JP là bụng của Fukami (TW: 插到了……我的裡面))
- **1474** [monologue] JP: 力んだ声。\nふんふん荒い鼻息は、勃起を揺らしかねない程の勢いだ。 / Cũ: Giọng nói đầy quyết tâm.\nHơi thở gấp gáp, mạnh mẽ đến mức làm rung chuyển cả dương vật. / Mới: Giọng nói căng thẳng.\nHơi thở gấp gáp, mạnh mẽ đến mức làm rung chuyển cả dương vật. (力んだ声 = giọng căng thẳng (TW 緊張), không phải "đầy quyết tâm")
- **766** [monologue] JP: ……確かに、濡れているだろう。\n先走り汁が滲んできたのを、随分前から感じてた。 / Cũ: 「……Chắc chắn là ướt rồi.\nAnh đã cảm nhận được dâm thủy rỉ ra từ nãy đến giờ rồi.」 / Mới: ……Chắc chắn là ướt rồi.\nAnh đã cảm nhận được dâm thủy rỉ ra từ nãy đến giờ rồi. (độc thoại bị bọc 「」 thành thoại; gỡ ngoặc, giữ nguyên câu)

## §4. fa/fu — chờ đợt thống nhất (không tính sai)

7 dòng dạng cũ "phù ah"/"phù" cho ふあ/ふぁ/ぷあ — theo tiền lệ lr_ふかみh2 + ハチロクh6, để đợt thống nhất sửa thành "phà"/"phùa", KHÔNG tính vào 98 dòng sai: **987** (bản sửa chứa "Phù——ah" cho ふぁっ), **989** ("Phù ah!" cho ふあっ), **992** (bản sửa chứa "Phù, ah" cho ふぁ), **1039** (bản sửa chứa "phù, ah" cho ふあ), **1045** (bản sửa chứa "Ưm——phù" cho ぷぁ), **1048** ("phù ah" cho ふあぁ và ぷあっ), **1049** ("Phù ah" cho ふあっ). Trong đó 989, 1048, 1049 là dòng đúng, chỉ sai dạng fa/fu. ふわっ ở 976 ("Phù ah") không thuộc họ fa/fu, giữ nguyên. 1553: JP gốc có ngoặc （...」 lệch; bản sửa chuẩn hóa thành （...）.

## §5. Sweep っ — kiểm chứng

Sweep có 3 mục cho file này: **1403** (needs-file-audit) nhận — đã sửa (§2); **1426** và **1461** là false positive — JP cả hai dòng đều không có っ, VN đã đúng, không sửa. Sweep **bỏ sót 4 dòng gasp**: 979, 1043, 1058, 1137 (trong đó 1137 là 「っ！！！」 nguyên dòng → "!!!", đúng mẫu lost-gasp-whole nhưng không có trong sweep).

## §6. Lượt soát 2 + khối TOML

- Lượt soát 2 (đọc lại toàn bộ 98 bản sửa đối chiếu JP): **tổng 98 / tái kiểm chứng 98 / bỏ 0 / sửa 0**.
- JSON: `audit-fukamih1-tomohari-renshuu-wrong.json` — 98 mục, khóa dạng string, jp/tw/old_vn khớp CSV3 tuyệt đối 98/98, không có fix nào trùng old_vn.
- Khối TOML dưới đây parse bằng tomllib: **98 khóa, 0 sai lệch giá trị** so với JSON.

```toml
[script]
"762" = "……Fukami đang ra sức lau người cho tôi.\\nĐược em ấy lau cho thì đúng là biết ơn thật đấy, nhưng mà——"
"766" = "……Chắc chắn là ướt rồi.\\nAnh đã cảm nhận được dâm thủy rỉ ra từ nãy đến giờ rồi."
"772" = "「……“Dù không bình đẳng nhưng vẫn công bằng”——sao.」"
"781" = "「……Ư……ưm…………ưm…………」"
"942" = "「Nhưng mà……không ngờ lại làm chuyện này trên thuyền xuôi dòng.」"
"952" = "「Nhờ em lau người cho nhiệt tình quá nên anh——\\nĐã hoàn toàn nóng lên mất rồi.」"
"969" = "「Hya fu!」"
"979" = "「Ư——」"
"981" = "「Không sao……ưm.」"
"987" = "「Phù——ah——của em——âm đạo——\\nMiệng của——anh Soutetsu——bằng miệng——」"
"990" = "「Uoa!?」"
"992" = "「Phù, ah——lưỡi……ấm……quá……ưm.」"
"993" = "「Phuê!?」"
"995" = "「Hả!? A! Anh Soutetsu, khoan hẵng qua đây——\\nÁ!? Oa a a a a a a a!?」"
"1001" = "「A……ya……thấm, vào rồi——ưm——em, âm đạo——nước bọt của anh Soutetsu……, thấm, vào——nóng, quá.」"
"1003" = "「Ah——phù——cháy, mất——tan chảy, mất——\\nCủa, em——âm đạo——ưm——tan chảy, mất thôi.」"
"1011" = "「A……ưm——ha——to, quá ạ——\\nCủa anh Soutetsu——ưm——đang đâm vào bụng em——」"
"1014" = "「A……v, vâng. ——Đúng, vậy nhỉ.\\nEm……cũng, ướt nhẹp……thế này, rồi.」"
"1015" = "「A……của, em……của, em……âm, đạo……\\nKhuôn mặt của……anh Soutetsu……gần……gần thế này.」"
"1018" = "「A……chỗ này vẫn chưa lau được chút nào cả.\\nEm xin lỗi——ưm……ây da, ây, da.」"
"1019" = "「A——」"
"1026" = "「A! Vâng! Vâng! Trăm sự nhờ anh ạ!!」"
"1031" = "「Hả!? Ơ!? T, tại sao——vậy, ạ?」"
"1034" = "「A, giỏi quá. Anh Soutetsu.\\nNếu làm như vừa nãy, anh có thể vượt qua dòng thác mà không bị tròng trành đấy.」"
"1039" = "「Thích……thích……Anh Soutetsu, đối với em——\\nĐã thích em rồi, sao……phù, ah.」"
"1043" = "「Ưm……ƯƯ——ưm——phù——ưm」"
"1045" = "「Ưm——phù. Em ướt sũng hết cả rồi.\\nThế này mà không cởi ra……thì Fukami sẽ bị cảm lạnh mất.」"
"1053" = "「Ư……ưm.」"
"1058" = "「Ư!!?——A hyu u u u u u ưm!!!」"
"1059" = "「Ưm nu!?」"
"1064" = "「Ây da, ây da——chà, chà——chà, chà.」"
"1065" = "「Ối!」"
"1068" = "「Nếu vậy thì.」"
"1074" = "「Em xin lỗi. Em đang đun nước tắm rồi nhưng……\\nChắc là vẫn còn phải mất thêm một lúc nữa.」"
"1081" = "「Chắc chắn là sẽ “thích nhiều hơn”, “thích hơn nữa”……\\nNhưng một người đã thích Fukami như anh, thì làm sao có chuyện “bắt đầu thích” được nữa.」"
"1083" = "「Đúng hơn là, Fukami đang ướt sũng rồi kìa.\\nNếu em không phiền——anh rất sẵn lòng giúp em lau người đấy?」"
"1085" = "「Vì thế……phần dưới……ừm, phần dưới——nếu, nếu——\\nNếu được……ừm! Nhờ anh, Soutetsu——làm, giúp em……」"
"1087" = "「Vì vậy, hẹn hò riêng hai người, em sẽ được hai lần,\\ncòn bé Nagi một lần. Thế này là vừa đủ công bằng rồi nhỉ.」"
"1088" = "「Vì vậy, em muốn anh xem lần đầu tiên.\\nHình ảnh em đang chèo thuyền trên sân nhà của mình——」"
"1093" = "「Chà, chà——lau, lau——ưm……sao rồi ạ?\\nAnh Soutetsu đã khô bớt chút nào chưa?」"
"1100" = "「Đúng vậy. Dù chênh lệch chưa đến mười phút,\\nnhưng người đầu tiên làm tình với anh Soutetsu là……bé Nagi.」"
"1106" = "「Chính là điều anh đang mong đợi đấy.」"
"1107" = "「Không sao đâu——chắc là không lo bị cảm lạnh đâu.」"
"1116" = "「Fukami!?」"
"1117" = "「Tại sao á, vì anh đã thích Fukami mất rồi.」"
"1118" = "「Vì có tận hai cơ hội mà,\\nnên em nghĩ, lần đầu tiên sẽ ở sân nhà của mình——」"
"1121" = "「Nếu để anh Soutetsu bị cảm lạnh thì em thấy có lỗi lắm.\\nEm sẽ lau cho anh bao nhiêu cũng được.」"
"1123" = "「“Bắt đầu thích” sao? Chuyện đó là không thể nào.」"
"1129" = "「Vậy sao.」"
"1133" = "「A, ừm——em——phần trên, em sẽ tự——tự cởi,\\nừm——em sẽ cởi, nên——」"
"1135" = "「Một em, đã được anh Soutetsu……khen là đ, đẹp.\\nEm muốn……anh Soutetsu……sẽ, sẽ thích, em, hơn nữa.」"
"1137" = "「Ư!!!」"
"1253" = "Nhưng ngay sau đó,\\nvị mật ngòn ngọt, mang theo chút hơi ấm bắt đầu hòa quyện vào."
"1263" = "Chỉ muốn bù đắp một chút cho việc đã khiến em ấy phải chờ đợi."
"1300" = "Không hẳn là tươi mát, mà đúng hơn là hương vị của nước lan tỏa trong miệng."
"1305" = "Vì tôi mãi không thể xác định được đó có phải là cám dỗ hay không,\\nnên có vẻ như tôi đã vô tình khiến Fukami phải nóng lòng chờ đợi."
"1307" = "Tại sao số lần lại không bằng nhau, cho đến khi được hai người giải thích,\\ntôi vẫn cảm thấy thật kỳ lạ, nhưng mà……"
"1309" = "Nơi tận cùng đường nét của vùng bụng hoàn toàn phẳng lì, một cặp ngực nhỏ hình bát úp, căng tròn,\\nđang lộ ra với núm vú màu hồng."
"1312" = "Vào thời kỳ hưng thịnh, dịch vụ đi thuyền xuôi dòng vào mùa đông rất đắt khách,\\nhọ thường cung cấp nước tắm sau giờ làm việc cho những người lái đò bị lạnh cóng."
"1319" = "Theo từng nhịp lau, nó cứ tiến lại gần rồi lại lùi ra xa,\\ntừng giọt, từng giọt nước nhỏ xuống mặt tôi."
"1326" = "Anh muốn làm em tan chảy. Liếm láp, mút mát nhiều hơn, nhiều hơn nữa.\\nNhưng để làm được điều đó, thì lớp vải mỏng này——"
"1358" = "Nhìn lại một lần nữa vào âm đạo đã hoàn toàn phơi bày,\\ntôi chăm chú quan sát——"
"1378" = "Cơ thể ngày càng nóng lên,\\nnhững phần da thịt chạm vào nhau ướt đẫm mồ hôi của cả hai."
"1379" = "Ngay sát chóp mũi của Fukami,\\ndương vật đang cương cứng của tôi đã nhô cao lên lớp quần."
"1382" = "Ngay từ đầu đã tung hết sức, tôi hôn lên đường rãnh dọc đang in hằn qua lớp quần lót,\\nrồi cứ thế thè lưỡi liếm láp thật mạnh."
"1385" = "Với Fukami, và Nagi.\\nMột buổi hẹn hò trọn vẹn một ngày chỉ có hai người với từng người."
"1387" = "Cảm giác vượt qua được thử thách khiến tôi vô tình thốt lên những lời nhẹ nhõm."
"1403" = "Có lẽ vì khoái cảm quá mãnh liệt,\\nFukami lắc đầu nguầy nguậy——Ư!"
"1431" = "Nếu đó là quyết định của Fukami và Nagi,\\nthì tôi cũng không nên xen mồm vào làm gì."
"1440" = "Mùi hương trở nên nồng đậm hơn."
"1442" = "Phía bên kia âm đạo của Fukami."
"1451" = "Em ấy đang nói ra sự thật với giọng điệu đều đều."
"1453" = "Giọng nói vui vẻ, hào hứng."
"1455" = "Mong muốn của Fukami là,\\nđược cùng tôi luyện tập chèo thuyền, chỉ có hai người với nhau."
"1465" = "Fukami nhận ra điều đó, nhưng không hề ngoảnh mặt đi.\\nNếu vậy thì, quả nhiên——đây chắc chắn là một sự cám dỗ rồi."
"1473" = "Sức ép bí ẩn trong giọng nói của Fukami cũng hoàn toàn biến mất,\\nthay vào đó, em ấy bắt đầu trở nên vui vẻ, hào hứng."
"1474" = "Giọng nói căng thẳng.\\nHơi thở gấp gáp, mạnh mẽ đến mức làm rung chuyển cả dương vật."
"1476" = "Từng giọt nước nhỏ xuống từ háng em như kéo thành sợi.\\nEo của Fukami lại bắt đầu đung đưa, cọ quậy."
"1484" = "Vì thế, Fukami đang lau người cho tôi.\\nTrong khi vẫn đang mặc nguyên bộ quần áo, đồ lót ướt sũng, mỏng tang."
"1496" = "Vượt qua dòng thác này, một lúc sau,\\nchỉ cần để thuyền trôi lững lờ theo dòng nước là được."
"1499" = "Tỏng——tỏng."
"1500" = "Để tránh làm văng những giọt nước thừa thãi, em ấy bảo tôi nằm xuống,\\nrồi ngồi lên trên, ra sức lắc lư eo, lau người cho tôi."
"1520" = "Ngay trước mắt tôi, là phần háng quần lót của Fukami đang banh rộng.\\nNó ướt sũng, ngậm đầy nước và dính chặt vào da."
"1533" = "Ba người……hay nói đúng hơn là, theo thỏa thuận thực tế giữa Fukami và Nagi,\\nsố lần hẹn hò được chốt lại là Fukami hai lần, Nagi một lần."
"1535" = "Màng nhĩ tôi rung lên dễ chịu bởi giọng nói đầy vui sướng,\\ntôi từ từ lột lớp vải đang dính chặt ra, cởi sạch phần dưới của Fukami."
"1546" = "Chiếc thuyền rung lắc dữ dội dù không phải ở chỗ nước chảy xiết.\\nPhản ứng đó khiến tôi nhận ra lời nói của mình thiếu sót trầm trọng."
"1553" = "（Liếm! Liếm——chụt——ngoạm!）"
"1561" = "Nói rồi, Fukami đứng thẳng lưng ở mũi thuyền.\\nDù đang vươn thẳng người, đôi gò má em vẫn dần ửng đỏ."
"1580" = "Dù độ dày có lẽ chưa đến vài milimet,\\nnhưng chiếc quần lót ướt sũng dính chặt này thực sự quá vướng víu."
"1581" = "Vì thế, bồn tắm ở đây cực kỳ lớn,\\nnên việc đun nước cũng mất khá nhiều thời gian——nghe nói là vậy."
"1588" = "Chỉ là vậy thôi, nhưng không hiểu sao\\ntôi lại cảm nhận được một sức ép khó tả."
"1651" = "（Rột——chụt! Nhóp nhép! Ực!）"
"1654" = "（Chụt——rột——liếm——liếm liếm liếm）"
"1655" = "（Nhóp nhép!!）"
"1659" = "（Ồ……）"
"1675" = "（Tõm——!!!）"
"1678" = "（Tròng trành!）"
"1681" = "（Liếm! Liếm! Liếm! Nhóp nhép!）"
```

**Tổng cộng sau file này: 117 file / 5.534 dòng sai** (cơ sở 116 file / 5.436 dòng sai + 98 file này)

- Chờ Hieu: (1) fa/fu 7 dòng (§4) vào đợt thống nhất; (2) 4 VN mồ côi có thể là bản dịch lỏng — có muốn dùng lại thay bản viết mới không: 1031 "Thích em hơn" (JP 1123), 1034 "Chà!" (JP 1065 っと), 1081 "Hể!!?" (JP 993 ふえっ), 1675 "Ưm!?" (JP 1059 んぬっ); (3) 2 VN mồ côi xác nhận không có nguồn: 781, 1065; (4) 990 dùng "Uoa!?" (bản dịch có sẵn trong file cho うぉっ) — nếu muốn "Uo!?" thì báo; (5) sweep bỏ sót 4 dòng gasp (979, 1043, 1058, 1137) — có cần bổ sung sweep không.

## Kết bài

File ふかみh1_ともはり練習 là một trong những file lệch nặng nhất: 98/272 dòng sai (36,0%), trong đó 88 dòng lệch vị trí thành 6 chuỗi xoay, 84 bản sửa khôi phục được ngay trong file (82 lệch dòng + 2 SFX). Hai set CSV3 đã được phân biệt rõ (bộ home là bộ cũ, bộ 11_Other mới là chuẩn) — file này là file dual-set thứ 11. Không có lỗi xưng hô, không có thuật ngữ sai, không có dòng Nagi. Sau file này tổng là 117 file / 5.534 dòng sai; còn 99 file trong hàng đợi.
