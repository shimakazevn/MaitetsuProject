# Audit — グランドリライト11_ナインスターズ！ (09_Grand)

## Tổng quan

- File: `グランドリライト11_ナインスターズ！.txt.toml` (route 09_Grand), 603 dòng script.
- **19 dòng sai (3,1%)** — đại từ 8, nghĩa 1, thuật ngữ 3, sweep っ 4, thêm/bịa 2, SFX 1.
- **0 lệch hàng, 0 chuỗi xoay vòng, 0 tràn file khác, 0 dòng mồ côi, 0 chưa dịch, 0 trùng key.**
- TOML md5: `235c146a22a4d2b84e7006c9470f5aac`; kiểm tra trùng lặp toàn bộ `sources/toml2/` — không có bản sao thứ hai (1 copy).

## Phương pháp

- Đọc ngữ nghĩa từng dòng toàn bộ 603 dòng, đối chiếu JP + TW từ CSV3 (91.731 dòng).
- Trích xuất: 603 dòng script, 603 dòng CSV3, 603 key duy nhất, 0 key trùng, 0 VN trống, 0 chưa dịch (chỉ có VN==TW ở key 1652, toàn dấu `「…………」`). `# JP:` khớp CSV3 JP đúng cả 603 key.
- TOML-2 là UTF-8 BOM + CRLF — phải decode `utf-8-sig` trước `tomllib` (plain `tomllib.load` lỗi dòng 1 cột 1). Cả 351 chênh lệch TOML-vs-CSV3 đều do TOML-2 flatten literal `\n` thành khoảng trắng; CSV3 (literal `\n`) là chuẩn cho giá trị fix.
- Quét っ có hệ thống: chỉ 4 dòng gasp toàn dòng = đúng 4 mục sweep của file này; `――っと` (2251/2374) là discourse marker, っ đầu dòng (2811/2346) là quotative/interjection — đúng là không phải gasp. `%l` chỉ mất cân bằng ở 2416 (thêm tag). VN trùng trong file chỉ có `「!」` ở 2899/2304/2315 (2899 và 2304 đều JP `「！」`, hợp lệ; 2315 là fix sweep).
- Kiểm tra tràn file khác qua project VN index: 0. Kiểm tra chuỗi xoay trước khi dịch mới: không có chuỗi nào.

## Cơ chế lỗi

Không có lệch hàng. Lỗi hệ thống chính là **cụm đại từ Kisaki** — file nhất quán nội bộ theo kiểu anh/em, nhưng trái quy tắc dự án ("tôi" với Kisaki) và trái tiền lệ audit đã merge (Common 14, Grand 01, lr_稀咲h1). Docs `locations_and_characters.md` §2.9 cho Kisaki tự xưng "'Em' hoặc 'Tôi'", gọi Soutetsu "'Anh Soutetsu'" — mâu thuẫn với các tiền lệ audit, nên coi là stale/mơ hồ (docs cho cả hai; audit luôn chọn "Tôi"/"cậu"/tên trần cho ngữ cảnh Grand/Common). Các file chưa audit (lr稀咲追加01/03: 96 dòng Soutetsu "Anh"; ハチロク12 "anh Soutetsu") có cùng mẫu anh/em — nhiều khả năng cùng lỗi hệ thống này.
**Parent sửa lại 20/11:** tiền lệ lr_稀咲h1 đã merge nói rõ Kisaki xưng hô THEO NGƯỜI NGHE — "em" với Soutetsu, "tôi" với Paulette (JP đều là ボク) — nên 7 fix tự xưng "em"→"tôi" của agent là SAI và đã bị loại (2142, 2508, 2514, 2531, 2599, 2681, 2846); 2617 sửa lại (giữ tên trần "Soutetsu", tự xưng về "em" vì người nghe gồm Soutetsu). Cụm Kisaki còn lại 5 fix đúng: 1664, 2173, 2347, 2459, 2617.
- 1 lỗi nghĩa duy nhất: 2619 đảo chiều đồng bộ.
- 2 lỗi gloss thuật ngữ theo quyết định Common 15 ("thân chính", "thẻ bảng" đều đã bị phán sai ở Common 15).
- 4 lỗi sweep っ, 2 lỗi thêm/bịa, 1 SFX.

## Chi tiết từng dòng

### Đại từ (8 dòng)

**1664 [稀咲]** — Kisaki gọi Soutetsu "anh Soutetsu" → tên trần (Common 14: Kisaki gọi "cậu"/tên trần; Grand 01: "Kisaki xưng 'Tôi'").

- JP: 「……つまり、双鉄の構想は」
- TW: 「……也就是說，雙鐵這個設想」
- Cũ: 「……Tóm lại, ý tưởng của anh Soutetsu là.」
- Sửa: 「……Tóm lại, ý tưởng của Soutetsu là.」

**2104 [双鉄]** — Soutetsu nói với cả nhóm (全員) → "tôi" (quy tắc nhóm, Paulette 14 key 1544).

- JP: 「すまんが稀咲の方は後回しにしてくれ。\n僕の方は、全員に聞きたい相談なのだ」
- TW: 「不好意思，稀咲的事情先放一放好嗎。我想說的，是關於我們全體的事情」
- Cũ: 「Xin lỗi nhưng chuyện của Kisaki để sau đi.\nChuyện của anh là chuyện muốn hỏi ý kiến của tất cả mọi người.」
- Sửa: 「Xin lỗi nhưng chuyện của Kisaki để sau đi.\nChuyện của tôi là chuyện muốn hỏi ý kiến của tất cả mọi người.」


**2173 [双鉄]** — Soutetsu gọi Kisaki "em" → "cô" (Common 14: "cậu gọi cô là 'cô'").

- JP: 「大陸の――\n[ちゅうごく,1]仲国のご友人の招待なのだろう？」
- TW: 「你是指接待大陸的——仲國的朋友嗎？」
- Cũ: 「Chẳng phải em được mời bởi một người bạn ở Đại lục——\nTrung Quốc sao?」
- Sửa: 「Chẳng phải cô được mời bởi một người bạn ở Đại lục——\nTrung Quốc sao?」

**2347 [双鉄]** — Soutetsu "anh" → "tôi" (nói với Kisaki).

- JP: 「なんだ、\n今日は[りょそう,1]旅装の稀咲をみられるかと思ったのだが」
- TW: 「喲，還想著今天能見到稀咲出遠門的樣子呢」
- Cũ: 「Gì chứ,\nanh cứ tưởng hôm nay sẽ được thấy Kisaki mặc đồ du lịch cơ.」
- Sửa: 「Gì chứ,\ntôi cứ tưởng hôm nay sẽ được thấy Kisaki mặc đồ du lịch cơ.」

**2428 [双鉄]** — Soutetsu nói với cả nhóm (みんな) → "tôi" (quy tắc nhóm, Paulette 14 key 1544).

- JP: 「もしよければ、みんなに相談したいことがある」
- TW: 「如果大家不介意的話，我有事想和你們商量」
- Cũ: 「Nếu được, anh có chuyện muốn bàn với mọi người.」
- Sửa: 「Nếu được, tôi có chuyện muốn bàn với mọi người.」

**2459 [稀咲]** — Kisaki "anh phải lái… Anh Soutetsu" → "cậu phải lái… Soutetsu".

- JP: 「そういう意味でも、今日は良い運転を頼むよ？　双鉄」
- TW: 「就算是從這個角度，今天也要好好駕駛哦，雙鐵」
- Cũ: 「Với ý nghĩa đó, hôm nay anh phải lái cho thật tốt đấy nhé? Anh Soutetsu.」
- Sửa: 「Với ý nghĩa đó, hôm nay cậu phải lái cho thật tốt đấy nhé? Soutetsu.」




**2574 [双鉄]** — Soutetsu "Anh… anh" → "Tôi… tôi" (nói với Hachiroku; reply 2118 xác nhận addressee).

- JP: 「そうか――よかった。楽しかった、か。\n僕は、ならば……僕は、ようやく――」
- TW: 「是嗎——太好了。他們很開心啊。我，那就……我，終於——」
- Cũ: 「Vậy sao——tốt quá. Vui lắm, sao.\nAnh, nếu vậy thì……anh, cuối cùng cũng——」
- Sửa: 「Vậy sao——tốt quá. Vui lắm, sao.\nTôi, nếu vậy thì……tôi, cuối cùng cũng——」


**2617 [稀咲]** — Kisaki "Em… em… anh Soutetsu" → "Tôi… tôi… Soutetsu".

- JP: 「ちょうどいい。ボクからも相談したいことが発生した。\nといっても、まずは双鉄とポーレットとを希望するけど」
- TW: 「正好，我也有事想要找你們商量。不過我本來是想先和雙鐵還有波萊特單獨商量就是了」
- Cũ: 「Vừa hay. Em cũng có chuyện muốn bàn bạc.\nNói vậy chứ, trước tiên em muốn nói chuyện với anh Soutetsu và Paulette.」
- Sửa: 「Vừa hay. Tôi cũng có chuyện muốn bàn bạc.\nNói vậy chứ, trước tiên tôi muốn nói chuyện với Soutetsu và Paulette.」



### Nghĩa (1 dòng)

**2619 [ハチロク]** — VN cũ đảo chiều đồng bộ: JP nói KiHa 07 phải liên động theo thao tác điều khiển của xe đi trước (8620); VN cũ nói ngược lại — hoạt động của 8620 phải đồng bộ với KiHa 07. TW đồng ý với JP.

- JP: 「その通りです。ですので、前――今回は[ハチロクニイマル,3]8620の\n運転操作に、[レ　イ　ナ　ナ,3]キハ07は連動しなければなりません」
- TW: 「正是如此。所以這次Ｋｉｈａ０７必須時刻與前車——也就是８６２０的駕駛操作同步」
- Cũ: 「Đúng vậy ạ. Do đó, hoạt động của xe đi trước——lần này là 8620\nphải đồng bộ với hoạt động điều khiển của KiHa 07 ạ.」
- Sửa: 「Đúng vậy ạ. Do đó, KiHa 07 phải liên động theo thao tác điều khiển của xe đi trước——lần này là 8620 ạ.」

### Thuật ngữ (3 dòng)

**3242 [monologue]** — ISC = "International Spirits Competition" — game tự viết ở 真闇01 key 1558; VN cũ "Challenge" là bịa.

- JP: [インターナショナルスピリッツコンペティション,6]　Ｉ　Ｓ　Ｃ　最優秀賞受賞酒の車内試飲販売は、今日\n走りだすナインスターズ一号列車の大きな目玉のひとつだ。
- TW: 今日啟程的九星一號列車的重頭戲之一，就是車內提供的這款斬獲ＩＳＣ大獎的酒的試飲與銷售。
- Cũ: Việc nếm thử và bán loại rượu đoạt giải cao nhất tại ISC (International Spirits Challenge) ngay trên tàu\nlà một trong những điểm nhấn lớn của chuyến tàu Nine Stars số 1 khởi hành hôm nay.
- Sửa: Việc nếm thử và bán loại rượu đoạt giải cao nhất tại ISC (International Spirits Competition) ngay trên tàu\nlà một trong những điểm nhấn lớn của chuyến tàu Nine Stars số 1 khởi hành hôm nay.

**3300 [monologue]** — 運転体 gloss "thân chính" → "thân vận hành" (Common 15 đã phán "thân chính" sai, sửa ở 1516/2619/2938).

- JP: 説明の間に手早く\x%l運転体;#00ffc040;運転体%l;#;への換装を終えたハチロクを、\nいつものように、膝の上へと抱き上げる。
- TW: 八六已經迅速換裝為\x%l運転体;#00ffc040;駕駛體%l;#;，我邊說邊像往常一樣把她抱到腿上坐下。
- Cũ: Tôi bế Hachiroku, người đã nhanh chóng thay sang \x%l運転体;#00ffc040;thân chính%l;#; trong lúc tôi giải thích,\nlên đùi như mọi khi.
- Sửa: Tôi bế Hachiroku, người đã nhanh chóng thay sang \x%l運転体;#00ffc040;thân vận hành%l;#; trong lúc tôi giải thích,\nlên đùi như mọi khi.

**3554 [monologue]** — タブレット gloss "thẻ bảng" → "máy tính bảng" (Common 15 đã phán "thẻ bảng" sai, sửa ở 2619).

- JP: そして\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の物を模した\x%lタブレット;#00ffc040;タブレット%l;#;――\nリレートレインの象徴は、僕から赤井\x%l運転士;#00ffc040;運転士%l;#;へと。
- TW: 我將模仿\x%lレイルロオド;#00ffc040;鐵路人偶%l;\x%lタブレット;#;#00ffc040;操作板%l;#;的圓盤——也就是接力列車的象徵交給了赤井\x%l運転士;#00ffc040;駕駛員%l;#;。
- Cũ: Và \x%lタブレット;#00ffc040;thẻ bảng%l;#; mô phỏng đồ của \x%lレイルロオド;#00ffc040;Railord%l;#;——\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \x%l運転士;#00ffc040;lái tàu%l;#; Akai.
- Sửa: Và \x%lタブレット;#00ffc040;máy tính bảng%l;#; mô phỏng đồ của \x%lレイルロオド;#00ffc040;Railord%l;#;——\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \x%l運転士;#00ffc040;lái tàu%l;#; Akai.

### Sweep っ (4 dòng)

**2315 [双鉄]** — Gasp toàn dòng っ → "Ư!" (áp nguyên từ sweep).

- JP: 「っ！」
- TW: 「啊！」
- Cũ: 「!」
- Sửa: 「Ư!」

**2317 [双鉄]** — Gasp toàn dòng っ → "Ư!!" (áp nguyên từ sweep).

- JP: 「っ！！」
- TW: 「啊！！」
- Cũ: 「!!」
- Sửa: 「Ư!!」

**2318 [双鉄]** — Gasp toàn dòng っ → "Ư!!!" (áp nguyên từ sweep).

- JP: 「っ！！！」
- TW: 「啊！！！」
- Cũ: 「!!!」
- Sửa: 「Ư!!!」

**2355 [双鉄]** — Gasp toàn dòng っ → "Ư!!?" (áp nguyên từ sweep).

- JP: 「っ！！？」
- TW: 「嗯！！？」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」

### Thêm/bịa (1 dòng)

**2462 [ナビ]** — VN thêm xưng hô "Ngài Soutetsu. " không có trong JP/TW — bỏ.

- JP: 「目に見えずとも、かいた汗は体表面で乾きます。\nそれはかすかな体臭となり、周りに不快感を与えます」
- TW: 「就算眼睛看不見，那也只是因為體表的汗乾了而已。這樣會產生輕微的體味，讓周圍人感到不悅」
- Cũ: 「Ngài Soutetsu. Dù không nhìn thấy, nhưng mồ hôi đổ ra sẽ khô lại trên bề mặt cơ thể.\nNó sẽ tạo ra mùi cơ thể thoang thoảng, gây khó chịu cho những người xung quanh.」
- Sửa: 「Dù không nhìn thấy, nhưng mồ hôi đổ ra sẽ khô lại trên bề mặt cơ thể.\nNó sẽ tạo ra mùi cơ thể thoang thoảng, gây khó chịu cho những người xung quanh.」

### Thêm tag %l (1 dòng)

**2416 [双鉄]** — VN thêm tag %l quanh 改札鋏 mà JP không có (JP chỉ có ruby [かいさつきょう,2]) — giữ chữ "kìm soát vé", bỏ tag.

- JP: 「きっぷを切るのが楽しいのだろう。\n[かいさつきょう,2]改札鋏をカチカチやっているときは、まるで――」
- TW: 「她只是喜歡檢票鉗剪在車票上時那喀嚓喀嚓的感覺吧——」
- Cũ: 「Chắc là em ấy thấy vui khi bấm vé.\nMỗi lần cầm \x%l改札鋏;#00ffc040;kìm soát vé%l;#; bấm lách cách, trông em ấy cứ như——」
- Sửa: 「Chắc là em ấy thấy vui khi bấm vé.\nMỗi lần cầm kìm soát vé bấm lách cách, trông em ấy cứ như——」

### SFX (1 dòng)

**3972 [monologue]** — （ぽっ！） là tiếng bật/pop (TW 啵), "Bíp!" là tiếng beep — sai âm.

- JP: （ぽっ！）
- TW: （啵！）
- Cũ: （Bíp!）
- Sửa: （Bộp!）

## Lượt soát 2

Đọc lại toàn bộ 26 fix đối chiếu từng JP lần thứ hai: **26 tổng / 26 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Đặc biệt kiểm tra lại: 4 mục sweep khớp JP từng dấu; cụm Kisaki kiểm lại từng addressee từ dòng kề (2574 xác nhận bằng reply 2118; 2617 xác nhận Kisaki nói với Soutetsu + Paulette); 2619 kiểm lại chiều đồng bộ — JP và TW đồng ý với nhau, VN cũ đảo ngược; 3242 kiểm lại trong game (真闇01 key 1558 viết "International Spirits Competition"); 3300/3554 theo quyết định Common 15; 3972 theo TW 啵 (= pop, không phải beep).

**Parent kiểm chứng 20/11 ~06:52:** agent soát 2 ghi 26/26/0/0; parent LOẠI 7 fix (2142, 2508, 2514, 2531, 2599, 2681, 2846) + SỬA 1 fix (2617) → còn 19. Lý do: tiền lệ đã merge ở lr_稀咲h1 (review dòng 637) và ROUTE-AUDIT.md — Kisaki xưng hô THEO NGƯỜI NGHE, "em" với Soutetsu và "tôi" với Paulette, JP đều là ボク, KHÔNG phải lỗi — agent đã đọc ngược tiền lệ này thành quy tắc "Kisaki luôn Tôi". Bài học: quy tắc đại từ của Kisaki là theo người nghe, giống Soutetsu; không áp quy tắc tuyệt đối cho tự xưng của Kisaki.

## Ghi chú / chờ Hieu (không tính sai, không tự quyết)

- **Cụm đại từ Kisaki (12 fix) vs docs §2.9** — cần parent kiểm chứng: docs cho cả "Em"/"Tôi" và "'Anh Soutetsu'", nhưng mọi tiền lệ audit đã merge đều chọn "Tôi"/"cậu"/tên trần. Nếu Hieu muốn giữ anh/em cho Kisaki thì 12 fix này phải bãi bỏ.
- **2477 "Anh có một ý tưởng" giữ nguyên** — trả lời câu hỏi trực tiếp của Paulette ở 2799, dù nhóm đang có mặt — không chắc có áp quy tắc nhóm hay không.
- **2804 "anh" giữ nguyên** — Soutetsu nói một mình, addressee mơ hồ.
- **2767 "bọn anh" giữ nguyên** — addressee Paulette số ít.
- **Ứng viên đợt thống nhất (không tính sai):** Ohimitera 12 dòng (2570, 2485, 3915, 2157, 2700, 3414, 3806, 2578, 3916, 2845, 1598, 3524), Ohito 1 (2385), tuyến Yui 4 (1619, 3374, 3916, 1683), Yui tên địa danh 1 (3212), Đường sắt Hoàng gia 1 (3393), Kobata 1 (3526), 九国 "chín tỉnh" vs "chín vùng" không nhất quán, 運転体 toàn dự án ("kíp lái" chiếm đa số ở file chưa audit vs "thân vận hành" đã chốt).
- **Gloss 機関士 giữ nguyên:** "lái tàu" 128× / "Lái tàu" 62× / "người lái tàu" 55× / "nhân viên cơ vụ" 33× toàn dự án; "thợ lái đầu máy" 0× trong CSV3; Common 15 giữ "nhân viên cơ vụ" làm gloss. 2646 "Người lái tàu" là biến thể thiểu số hợp lệ.
- **っ cuối câu giữ nguyên** (nhấn mạnh, không phải gasp): 2738/2289/2306/2309; `――っと` là discourse marker; っ đầu dòng là quotative/interjection.
- Các phán đoán giữ nguyên khác: 3441 工夫→"công sức", 3761 "xoa cằm", 2448 パンプス→"giày cao gót", 3970 độ dài nguyên âm huýt sáo (11 VN vs 9 mora JP).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1664 = "「……Tóm lại, ý tưởng của Soutetsu là.」"
2104 = "「Xin lỗi nhưng chuyện của Kisaki để sau đi.\\nChuyện của tôi là chuyện muốn hỏi ý kiến của tất cả mọi người.」"
2173 = "「Chẳng phải cô được mời bởi một người bạn ở Đại lục——\\nTrung Quốc sao?」"
2315 = "「Ư!」"
2317 = "「Ư!!」"
2318 = "「Ư!!!」"
2347 = "「Gì chứ,\\ntôi cứ tưởng hôm nay sẽ được thấy Kisaki mặc đồ du lịch cơ.」"
2355 = "「Ư!!?」"
2416 = "「Chắc là em ấy thấy vui khi bấm vé.\\nMỗi lần cầm kìm soát vé bấm lách cách, trông em ấy cứ như——」"
2428 = "「Nếu được, tôi có chuyện muốn bàn với mọi người.」"
2459 = "「Với ý nghĩa đó, hôm nay cậu phải lái cho thật tốt đấy nhé? Soutetsu.」"
2462 = "「Dù không nhìn thấy, nhưng mồ hôi đổ ra sẽ khô lại trên bề mặt cơ thể.\\nNó sẽ tạo ra mùi cơ thể thoang thoảng, gây khó chịu cho những người xung quanh.」"
2574 = "「Vậy sao——tốt quá. Vui lắm, sao.\\nTôi, nếu vậy thì……tôi, cuối cùng cũng——」"
2617 = "「Vừa hay. Em cũng có chuyện muốn bàn bạc.\\nNói vậy chứ, trước tiên em muốn nói chuyện với Soutetsu và Paulette.」"
2619 = "「Đúng vậy ạ. Do đó, KiHa 07 phải liên động theo thao tác điều khiển của xe đi trước——lần này là 8620 ạ.」"
3242 = "Việc nếm thử và bán loại rượu đoạt giải cao nhất tại ISC (International Spirits Competition) ngay trên tàu\\nlà một trong những điểm nhấn lớn của chuyến tàu Nine Stars số 1 khởi hành hôm nay."
3300 = "Tôi bế Hachiroku, người đã nhanh chóng thay sang \\x%l運転体;#00ffc040;thân vận hành%l;#; trong lúc tôi giải thích,\\nlên đùi như mọi khi."
3554 = "Và \\x%lタブレット;#00ffc040;máy tính bảng%l;#; mô phỏng đồ của \\x%lレイルロオド;#00ffc040;Railord%l;#;——\\nbiểu tượng của chuyến tàu chuyển tiếp, được tôi trao lại cho \\x%l運転士;#00ffc040;lái tàu%l;#; Akai."
3972 = "（Bộp!）"
```

## Kết bài

File グランドリライト11_ナインスターズ！ đã đọc xong toàn bộ 603 dòng: **19 dòng sai (3,1%)**, gồm đại từ 8 (cụm Kisaki 5 + nhóm/Hachiroku 3), 1 lỗi nghĩa đảo chiều đồng bộ, 3 lỗi thuật ngữ, 4 lỗi sweep っ, 2 lỗi thêm/bịa và 1 SFX. Lượt soát 2: agent 26/26/0/0; parent loại 7 + sửa 1 → 19. Không lệch hàng, không chuỗi xoay, không tràn file khác, không dòng chưa dịch hay trùng key. Còn chờ Hieu: phán quyết 2477/2804/2767 khi có dịp, và xác nhận quy tắc Kisaki tự xưng theo người nghe.
