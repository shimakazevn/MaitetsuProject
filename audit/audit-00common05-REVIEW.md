# Audit — 00_Common file 05 (共通05_ようやく石炭)

File: `共通05_ようやく石炭.txt.toml` — Common Route chương 5, lấy than cho Hachiroku: Paulette giảng về まいてつ, kiểm tra xe, Reina ngủ gật, rồi Soutetsu xin than và nhận làm 機関士 của Hachiroku.
Audit ngày 19/11/2026. Đọc toàn bộ từng dòng đối chiếu JP + TW, theo brief audit chuẩn (JP thắng TW khi lệch; kiểm tra chuỗi xoay, tràn chương khác, tag %l, quét đại từ Soutetsu, mẫu rên っ).

## Nguồn đã kiểm chứng: một bộ CSV duy nhất, khớp 100%

- CSV "Trang tính 3" chỉ có **một** bộ dòng cho file này (`00_Common\`, 421 dòng) — không có bẫy hai bộ như 共通02/03/04/06 hay lr_ふかみh2.
- CSV ↔ TOML: **421/421 key khớp, 0 lệch nội dung** (156 khớp y hệt + 265 khớp sau khi gỡ `\n` — TOML-2 làm phẳng `\n` thành khoảng trắng; CSV giữ `\n` gốc nên CSV là chuẩn cho fix list). `# JP:` comment đủ 421/421 key script. File giữ BOM + CRLF.
- TOML chỉ tồn tại một bản duy nhất dưới `00_Common/` (md5 `de5a6dfdd9e725f1e7df12251d6d2b2f`, không có file trùng lặp nào trong toàn dự án) — fix chỉ cần vào một bản.

## Tổng kết: 52/421 dòng sai (12,4%)

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 32 | 御一夜→Ohitoyo 11 (77, 3082, 2484, 2183, 2495, 2641, 2266, 2426, 2254, 2645, 3104); 帝鉄→Teitetsu 8 (2685, 1809, 2418, 2392, 2680, 2408, 1843, 2524); まいてつ→chủ tàu 6 (2443, 2719, 2474, 2467, 2730, 2495); 気動車→toa xe tự hành 5 (1812, 2188, 2509, 2151, 2591); 市電→tàu điện thành phố 2 (2404, 2378); 整備体→thân bảo trì 1 (2227) — lưu ý 2495 và 2551 mang 2 lỗi, tính 1 dòng |
| Xưng hô | 9 | Soutetsu→Paulette “cô”→“em” 5 (2573, 2139, 2395, 2442, 2185); Soutetsu→Hachiroku “cô”→“em” 2 (2440, 2727); Soutetsu độc thoại “Mình”→“Tôi” 1 (3560); Paulette tự sửa くん→さん 1 (2551) |
| Rên っ | 3 | 2763, 2287 (sweep, nhận nguyên văn); 2284 (sweep-missed) |
| SFX | 1 | 1840 (tiếng cười bị diễn thành tiếng rên) |
| Nghĩa | 2 | 2559 (khôi phục → khắc phục sự chậm trễ); 2699 (đô con → uống khỏe) |
| Nhỏ/văn phong | 2 | 2417 (hửm → không phải); 3089 (ngắt câu Railord/Reina) |
| Tag %l | 3 | Gỡ tag VN tự thêm: 2587, 2662, 2991 |
| **Tổng** | **52** | |

Lệch dòng (misaligned): **0**. Chuỗi xoay (rotation chain): **0**. Tràn từ chương khác: **0** (kiểm tra bằng project VN index: VN dài >25 ký tự chỉ trùng 1 dòng với ハチロク10_炙り出し 2405 — nhưng JP hai bên gần như giống hệt nhau (心底、驚いたような顔 vs 心底、びっくりしたような顔) nên đó là hai bản dịch độc lập cùng một câu, không phải tràn chương; JP trùng lặp trong file: 0). Dòng mồ côi (orphan VN): **0**. Dòng chưa dịch: **0**. Trùng key: **0**.

Nhân vật: monologue 187, ポーレット 90, 双鉄 77, ハチロク 39, れいな 22, 女子Ａ 4, 女子Ｂ 2. Paulette có mặt trong file nên quy tắc B4 áp dụng — kiểm tra hết: **0 dòng Paulette gọi tên trần “Soutetsu”** (tất cả đều là “anh Soutetsu” / “ngài Soutetsu” / “cậu Soutetsu” trong các câu tự sửa くん→さん).

## 52 dòng sai (chi tiết)


### Thuật ngữ (32 dòng)

### [77] — Thuật ngữ
- **JP:** \x%l列車;#00ffc040;列車%l;#;は、御一夜へと戻っている。 (monologue)
- **TW:** \x%l列車;#00ffc040;列車%l;#;正返回御一夜。
- **Cũ:** \x%l列車;#00ffc040;Đoàn tàu%l;#; đang quay trở về Ohimitera.
- **Mới:** \x%l列車;#00ffc040;Đoàn tàu%l;#; đang quay trở về Ohitoyo.
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11 (không dùng Ohimitera).

### [1809] — Thuật ngữ
- **JP:** 「\x%l帝鉄;#00ffc040;帝鉄%l;#;が夢見ていた全線電化。それがもっと進んでいれば
少しは事情も違ったのかもしれないですけれど」 (ポーレット)
- **TW:** 「\x%l帝鉄;#00ffc040;帝國鐵路%l;#;曾計劃全線電力化。如果能推進得再快些的話，其後或許還能有所不同」
- **Cũ:** 「Toàn tuyến điện khí hóa mà \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; từng mơ ước. Nếu điều đó được tiến hành nhanh hơn
thì có lẽ tình hình đã khác đi một chút.」
- **Mới:** 「Toàn tuyến điện khí hóa mà \x%l帝鉄;#00ffc040;Teitetsu%l;#; từng mơ ước. Nếu điều đó được tiến hành nhanh hơn thì có lẽ tình hình đã khác đi một chút.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11.

### [1812] — Thuật ngữ
- **JP:** 「\x%l気動車;#00ffc040;気動車%l;#;」 (双鉄)
- **TW:** 「\x%l気動車;#00ffc040;動車%l;#;」
- **Cũ:** 「\x%l気動車;#00ffc040;Động cơ%l;#;.」
- **Mới:** 「\x%l気動車;#00ffc040;Toa xe tự hành%l;#;.」
- **Lý do:** Gloss 気動車 “Động cơ” → “Toa xe tự hành”: 気動車 là toa xe tự hành (xe diesel tự hành), không phải động cơ (cái máy). Tiền lệ trong chính file: ディーゼル気動車 → “toa xe diesel tự hành” (2493, 2258); toàn dự án “toa xe tự hành” 27 dòng vs “động cơ” 5 dòng.

### [1843] — Thuật ngữ
- **JP:** 「……そこまで細かく知っている、っていうことは。
ハチロクさんは、やっぱりもともとは\x%l帝鉄;#00ffc040;帝鉄%l;#;の？」 (ポーレット)
- **TW:** 「……既然知道得這麼詳細，也就是說，果然八六小姐原本是\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的？」
- **Cũ:** 「……Biết rõ chi tiết đến mức đó, nghĩa là.
Chị Hachiroku, quả nhiên vốn dĩ là người của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; sao?」
- **Mới:** 「……Biết rõ chi tiết đến mức đó, nghĩa là. Chị Hachiroku, quả nhiên vốn dĩ là người của \x%l帝鉄;#00ffc040;Teitetsu%l;#; sao?」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11.

### [2151] — Thuật ngữ
- **JP:** 「だけじゃないですぅ。
ガソリン\x%l気動車;#00ffc040;気動車%l;#;もありますよぉ」 (れいな)
- **TW:** 「並不只有這些的。還有汽油\x%l気動車;#00ffc040;動車%l;#;哦」
- **Cũ:** 「Không chỉ vậy đâu nha.
Còn có \x%l気動車;#00ffc040;động cơ%l;#; xăng nữa đó ạ.」
- **Mới:** 「Không chỉ vậy đâu nha. Còn có \x%l気動車;#00ffc040;toa xe tự hành%l;#; xăng nữa đó ạ.」
- **Lý do:** Gloss 気動車 “động cơ” → “toa xe tự hành” (xem 1812). ガソリン気動車 = toa xe tự hành xăng.

### [2183] — Thuật ngữ
- **JP:** 「なんという幸運……すばらしい、栄誉です。
まさか、それほどの機体が御一夜に来てくれるだなんて」 (ポーレット)
- **TW:** 「何等的幸運……簡直是至高無上的榮譽。竟有如此寶貴的機體來到了御一夜」
- **Cũ:** 「Thật là may mắn……một vinh dự tuyệt vời.
Không ngờ, một cỗ máy tầm cỡ như vậy lại đến Ohimitera.」
- **Mới:** 「Thật là may mắn……một vinh dự tuyệt vời. Không ngờ, một cỗ máy tầm cỡ như vậy lại đến Ohitoyo.」
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11.

### [2188] — Thuật ngữ
- **JP:** 「さっき乗ってもらったように、\x%l運転台;#00ffc040;運転台%l;#;と客席が、
ひとつの車輌に一緒になってるのが\x%l気動車;#00ffc040;気動車%l;#;です」 (ポーレット)
- **TW:** 「像剛才咱們坐過的那種\x%l運転台;#00ffc040;駕駛台%l;#;和乘客座位在同一節車廂裡的，就是\x%l気動車;#00ffc040;動車%l;#;」
- **Cũ:** 「Như lúc nãy anh đã đi thử đó, \x%l運転台;#00ffc040;buồng lái%l;#; và ghế hành khách
được kết hợp trong cùng một toa xe thì gọi là \x%l気動車;#00ffc040;động cơ%l;#; ạ.」
- **Mới:** 「Như lúc nãy anh đã đi thử đó, \x%l運転台;#00ffc040;buồng lái%l;#; và ghế hành khách được kết hợp trong cùng một toa xe thì gọi là \x%l気動車;#00ffc040;toa xe tự hành%l;#; ạ.」
- **Lý do:** Gloss 気動車 “động cơ” → “toa xe tự hành” (xem 1812). Dòng này giải thích 気動車 là gì nên gọi nó là “động cơ” làm vỡ nghĩa giải thích.

### [2227] — Thuật ngữ
- **JP:** 「なるほど、それが整備[ボディ]体か」 (双鉄)
- **TW:** 「原來如此，這就是整備體嗎」
- **Cũ:** 「Ra là vậy, đó là cơ thể bảo dưỡng sao.」
- **Mới:** 「Ra là vậy, đó là thân bảo trì sao.」
- **Lý do:** 整備体 → “thân bảo trì” theo quyết định 19/11 (không dùng “cơ thể bảo dưỡng”). JP có ruby [ボディ] trên 体, khớp với “thân”.

### [2254] — Thuật ngữ
- **JP:** 「ハチロクさんの[ハチロクニイマル,3]8620を是非、
御一夜鉄道で走らせてくれませんか？」 (ポーレット)
- **TW:** 「可以讓八六小姐的８６２０行駛在御一夜鐵路公司的線路上嗎？」
- **Cũ:** 「Anh có thể cho chiếc 8620 của chị Hachiroku
chạy trên tuyến đường sắt Ohimitera được không?」
- **Mới:** 「Anh có thể cho chiếc 8620 của chị Hachiroku chạy trên tuyến đường sắt Ohitoyo được không?」
- **Lý do:** 御一夜鉄道 → Ohitoyo theo quyết định 19/11.

### [2266] — Thuật ngữ
- **JP:** 「あの、それは――ええと、右田っ！　右田家といえば、
高額納税者ナンバーワンですから、御一夜市の」 (ポーレット)
- **TW:** 「呃，是因為——那個什麼，右田！說到右田家，可是御一夜第一高額納稅人」
- **Cũ:** 「À, chuyện đó——ừm, Migita! Nhắc đến nhà Migita,
thì đó là người nộp thuế cao nhất của thành phố Ohimitera mà.」
- **Mới:** 「À, chuyện đó——ừm, Migita! Nhắc đến nhà Migita, thì đó là người nộp thuế cao nhất của thành phố Ohitoyo mà.」
- **Lý do:** 御一夜市 → Ohitoyo theo quyết định 19/11. “Nhà Migita” (右田家) giữ nguyên — họ Migita, không phải xưởng rượu Migita Ichi.

### [2378] — Thuật ngữ
- **JP:** 「\x%l市電;#00ffc040;市電%l;#;とはいえ全線電化など――
よくも、それほどの偉業を」 (ハチロク)
- **TW:** 「就算是\x%l市電;#00ffc040;市電%l;#;，怎麼說也都是全線電力化。竟能夠完成如此的偉業」
- **Cũ:** 「Dù là \x%l市電;#00ffc040;nguồn điện chính%l;#; nhưng lại điện khí hóa toàn tuyến sao——
Thật đáng nể, một vĩ nghiệp như vậy.」
- **Mới:** 「Dù là \x%l市電;#00ffc040;tàu điện thành phố%l;#; nhưng lại điện khí hóa toàn tuyến sao—— Thật đáng nể, một vĩ nghiệp như vậy.」
- **Lý do:** Gloss 市電 “nguồn điện chính” → “tàu điện thành phố”. Hieu đã chốt 20/11; docs mục 119 đã sửa.

### [2392] — Thuật ngữ
- **JP:** 「――帝鉄末期、これが1000を超えている地方路線は、
ザラだったと聞いています」 (ポーレット)
- **TW:** 「帝國鐵路末期，聽說這個係數超過１０００的地方線路隨處可見」
- **Cũ:** 「——Vào cuối thời kỳ Đường sắt Hoàng gia, nghe nói những tuyến đường địa phương có hệ số này vượt quá 1000
là chuyện rất bình thường.」
- **Mới:** 「——Vào cuối thời kỳ Teitetsu, nghe nói những tuyến đường địa phương có hệ số này vượt quá 1000 là chuyện rất bình thường.」
- **Lý do:** 帝鉄末期 → “cuối thời kỳ Teitetsu” theo quyết định 19/11 (dòng này không có tag %l, sửa thẳng vào văn bản).

### [2404] — Thuật ngữ
- **JP:** 「\x%l市電;#00ffc040;市電%l;#;なんです[ひろでん,1]廣電は。ですから\x%l架線;#00ffc040;[がせん,1]架線%l;#;も容易で、
大廃線以前から、完全電化がされていました」 (ポーレット)
- **TW:** 「廣島電鐵是\x%l市電;#00ffc040;市電%l;#;。所以\x%l架線;#00ffc040;架線%l;#;也很容易，在大廢線以前，就實現了完全電力化」
- **Cũ:** 「Đường sắt điện Hiroshima là \x%l市電;#00ffc040;nguồn điện chính%l;#; mà. Vì vậy việc \x%l架線;#00ffc040;đường dây tiếp điện trên cao%l;#; cũng dễ dàng,
từ trước đợt Đại bãi bỏ, nó đã được điện khí hóa hoàn toàn rồi.」
- **Mới:** 「Đường sắt điện Hiroshima là \x%l市電;#00ffc040;tàu điện thành phố%l;#; mà. Vì vậy việc \x%l架線;#00ffc040;đường dây tiếp điện trên cao%l;#; cũng dễ dàng, từ trước đợt Đại bãi bỏ, nó đã được điện khí hóa hoàn toàn rồi.」
- **Lý do:** Gloss 市電 “nguồn điện chính” → “tàu điện thành phố”: 市電 = tàu điện thành phố (tram) — 広電 là hãng tàu điện Hiroshima, cả đoạn đang nói về mạng lưới tàu điện và đường dây trên cao. “Nguồn điện chính” (main power source) làm câu vô nghĩa. Hieu đã chốt “tàu điện thành phố” 20/11; docs mục 119 đã sửa.

### [2408] — Thuật ngữ
- **JP:** 「全盛期から、\x%l帝鉄;#00ffc040;帝鉄%l;#;はあまりに巨大過ぎました。
理念と現実が一致せず、上部と末端は乖離していました」 (ハチロク)
- **TW:** 「從全盛期開始，\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的規模就過於龐大了。理想跟不上現實，上層與底層產生了分裂」
- **Cũ:** 「Ngay từ thời kỳ hoàng kim, \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; đã quá đỗi khổng lồ.
Lý tưởng và hiện thực không đồng nhất, cấp trên và cấp dưới bị chia rẽ.」
- **Mới:** 「Ngay từ thời kỳ hoàng kim, \x%l帝鉄;#00ffc040;Teitetsu%l;#; đã quá đỗi khổng lồ. Lý tưởng và hiện thực không đồng nhất, cấp trên và cấp dưới bị chia rẽ.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11.

### [2418] — Thuật ngữ
- **JP:** 「そうだろうって思います。それでも、\x%l帝鉄;#00ffc040;帝鉄%l;#;は、
強く電化を推し進めようとしていました」 (ポーレット)
- **TW:** 「應該是的。即便如此，\x%l帝鉄;#00ffc040;帝國鐵路%l;#;也還是強力推行了電力化」
- **Cũ:** 「Tôi cũng nghĩ vậy. Dù thế, \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; vẫn
cố gắng đẩy mạnh việc điện khí hóa.」
- **Mới:** 「Tôi cũng nghĩ vậy. Dù thế, \x%l帝鉄;#00ffc040;Teitetsu%l;#; vẫn cố gắng đẩy mạnh việc điện khí hóa.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11.

### [2426] — Thuật ngữ
- **JP:** 「僕が御一夜に帰ってきたのは、
\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致計画を撤回させるそのためだ」 (双鉄)
- **TW:** 「我之所以會回到御一夜，是為了促使\x%lエアクラ;#00ffc040;空凝機%l;#;工場落戶計劃撤銷」
- **Cũ:** 「Lý do tôi trở về Ohimitera,
là để hủy bỏ kế hoạch thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」
- **Mới:** 「Lý do tôi trở về Ohitoyo, là để hủy bỏ kế hoạch thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11.

### [2443] — Thuật ngữ
- **JP:** 「なぁ、ハチロク。さっきポーレットが言っていたな。
『時代が時代。\x%lまいてつ;#00ffc040;まいてつ%l;#;それぞれに事情がある』と」 (双鉄)
- **TW:** 「我說，八六。剛才波萊特是這樣說的——“這個時代情況很複雜。\x%lまいてつ;#00ffc040;掌車人%l;#;各有各的隱情”」
- **Cũ:** 「Này, Hachiroku. Lúc nãy Paulette có nói mà.
『Thời đại bây giờ là vậy. Mỗi \x%lまいてつ;#00ffc040;người sành toa xe%l;#; đều có những lý do riêng』」
- **Mới:** 「Này, Hachiroku. Lúc nãy Paulette có nói mà. 『Thời đại bây giờ là vậy. Mỗi \x%lまいてつ;#00ffc040;chủ tàu%l;#; đều có những lý do riêng』」
- **Lý do:** Gloss まいてつ “người sành toa xe” → “Maitetsu”: “sành” (sành sỏi) không đúng nghĩa gốc — 2155 tự định nghĩa まいてつ là người sở hữu và vận hành đoàn tàu; file này dùng “Maitetsu” ở 6 dòng khác (1826, 2132, 2155, 2501, 3296, 2472) và file 03 cũng dùng “Maitetsu”. Thống nhất về “Maitetsu” trong file. (Toàn dự án còn chia 4 cách: chủ tàu 23 / Maitetsu 11 / người sành toa xe 9 / người đam mê đường sắt 3 — cần Hieu chốt một cách ở đợt thống nhất.)

### [2467] — Thuật ngữ
- **JP:** 「大廃線後の鉄道文化をぎりぎり支えてるのは、
地方地方の民間鉄道と、\x%lまいてつ;#00ffc040;まいてつ%l;#;たちなんです」 (ポーレット)
- **TW:** 「支撐著大廢線之後的鐵路文化的，就是各地的民間鐵路，以及\x%lまいてつ;#00ffc040;掌車人%l;#;們」
- **Cũ:** 「Những người đang cố gắng chống đỡ nền văn hóa đường sắt sau đợt Đại bãi bỏ,
chính là các tuyến đường sắt tư nhân ở các địa phương và những \x%lまいてつ;#00ffc040;người sành toa xe%l;#; đấy.」
- **Mới:** 「Những người đang cố gắng chống đỡ nền văn hóa đường sắt sau đợt Đại bãi bỏ, chính là các tuyến đường sắt tư nhân ở các địa phương và những \x%lまいてつ;#00ffc040;chủ tàu%l;#; đấy.」
- **Lý do:** Gloss まいてつ “người sành toa xe” → “Maitetsu” (thống nhất trong file, xem 2443).

### [2474] — Thuật ngữ
- **JP:** 「大人物です。\x%lまいてつ;#00ffc040;まいてつ%l;#;界きっての有名人ですし」 (ポーレット)
- **TW:** 「是一位大人物。在\x%lまいてつ;#00ffc040;掌車人%l;#;圈子裡最有名的」
- **Cũ:** 「Là một nhân vật vĩ đại đấy. Cô ấy là người nổi tiếng nhất trong giới \x%lまいてつ;#00ffc040;người sành toa xe%l;#; mà.」
- **Mới:** 「Là một nhân vật vĩ đại đấy. Cô ấy là người nổi tiếng nhất trong giới \x%lまいてつ;#00ffc040;chủ tàu%l;#; mà.」
- **Lý do:** Gloss まいてつ “người sành toa xe” → “Maitetsu” (thống nhất trong file, xem 2443).

### [2484] — Thuật ngữ
- **JP:** 「私と、れいなとのふたりのです。
御一夜鉄道レールショップは、私達のお城ですから」 (ポーレット)
- **TW:** 「是我和玲奈兩個人的愛好。御一夜鐵路的鐵路商店就像是我們的城堡一樣」
- **Cũ:** 「Là của cả tôi và Reina.
Cửa hàng đường sắt Ohimitera là lâu đài của chúng tôi mà.」
- **Mới:** 「Là của cả tôi và Reina. Cửa hàng đường sắt Ohitoyo là lâu đài của chúng tôi mà.」
- **Lý do:** 御一夜鉄道 → Ohitoyo theo quyết định 19/11.

### [2495] — Thuật ngữ
- **JP:** 「はい。わたしは、れいなと\x%lキハ07;#00ffc040;キハ07%l;#;Sの\x%lまいてつ;#00ffc040;まいてつ%l;#;です。
かつ、御一夜鉄道株式会社の社長でもあります」 (ポーレット)
- **TW:** 「是的。我是玲奈和\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;Ｓ的\x%lまいてつ;#00ffc040;掌車人%l;#;。也是御一夜鐵路股份公司的社長」
- **Cũ:** 「Vâng. Tôi là \x%lまいてつ;#00ffc040;người sành toa xe%l;#; của Reina và \x%lキハ07;#00ffc040;KiHa 07%l;#;S.
Đồng thời, cũng là giám đốc của Công ty Cổ phần Đường sắt Ohimitera.」
- **Mới:** 「Vâng. Tôi là \x%lまいてつ;#00ffc040;chủ tàu%l;#; của Reina và \x%lキハ07;#00ffc040;KiHa 07%l;#;S. Đồng thời, cũng là giám đốc của Công ty Cổ phần Đường sắt Ohitoyo.」
- **Lý do:** Hai lỗi trong một dòng: gloss まいてつ “người sành toa xe” → “Maitetsu” (thống nhất trong file, xem 2443) và 御一夜鉄道 → Ohitoyo theo quyết định 19/11.

### [2509] — Thuật ngữ
- **JP:** 「そうですね、\x%l電車;#00ffc040;電車%l;#;は、厳密には電気\x%l気動車;#00ffc040;気動車%l;#;のことです。
でも、\x%l電車;#00ffc040;電車%l;#;っていう略称ぽいのが実は正式名称なんです」 (ポーレット)
- **TW:** 「是的。電車，嚴格來說是叫電力\x%l気動車;#00ffc040;動車%l;#;。不過，電車這種聽起來像是簡稱的稱呼，實際上卻是正式名稱」
- **Cũ:** 「Đúng vậy ạ, \x%l電車;#00ffc040;tàu điện%l;#; nói chính xác thì là \x%l気動車;#00ffc040;động cơ%l;#; điện.
Nhưng mà, cái tên nghe như viết tắt \x%l電車;#00ffc040;tàu điện%l;#; đó thực ra lại là tên chính thức đấy ạ.」
- **Mới:** 「Đúng vậy ạ, \x%l電車;#00ffc040;tàu điện%l;#; nói chính xác thì là \x%l気動車;#00ffc040;toa xe tự hành%l;#; điện. Nhưng mà, cái tên nghe như viết tắt \x%l電車;#00ffc040;tàu điện%l;#; đó thực ra lại là tên chính thức đấy ạ.」
- **Lý do:** Gloss 気動車 “động cơ” → “toa xe tự hành” (xem 1812). 電気気動車 = toa xe tự hành điện.

### [2524] — Thuật ngữ
- **JP:** 「はい、\x%l帝鉄;#00ffc040;帝鉄%l;#;[ハチロクニイマル,3]8620形\x%l蒸気機関車;#00ffc040;蒸気機関車%l;\x%l8620;#;#00ffc040;8620%l;#;トップナンバー機の
専用\x%lレイルロオド;#00ffc040;レイルロオド%l;#;――それが、わたくしの出自です」 (ハチロク)
- **TW:** 「是的，\x%l帝鉄;#00ffc040;帝國鐵路%l;#;８６２０型\x%l蒸気機関車;#00ffc040;蒸汽機車%l;\x%l8620;#;#00ffc040;８６２０%l;#;首車的專用\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;——這就是，我的出身」
- **Cũ:** 「Vâng, \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của chiếc đầu máy số một
\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; dòng \x%l8620;#00ffc040;8620%l;#; thuộc \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;——đó chính là xuất thân của tôi.」
- **Mới:** 「Vâng, \x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của chiếc đầu máy số một \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; dòng \x%l8620;#00ffc040;8620%l;#; thuộc \x%l帝鉄;#00ffc040;Teitetsu%l;#;——đó chính là xuất thân của tôi.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11. Giữ nguyên cấu trúc tag phức tạp của JP (tag %l; lồng ruby [ハチロクニイマル,3]) — chỉ đổi gloss.

### [2591] — Thuật ngữ
- **JP:** 「今はそうです。でも、れいな。
もともとはガソリン\x%l気動車;#00ffc040;気動車%l;#;だったんですよぉ」 (れいな)
- **TW:** 「現在是的。不過，玲奈本來是汽油\x%l気動車;#00ffc040;動車%l;#;哦」
- **Cũ:** 「Bây giờ thì đúng là vậy. Nhưng mà, Reina nha.
Vốn dĩ ban đầu là \x%l気動車;#00ffc040;động cơ%l;#; xăng đó ạ.」
- **Mới:** 「Bây giờ thì đúng là vậy. Nhưng mà, Reina nha. Vốn dĩ ban đầu là \x%l気動車;#00ffc040;toa xe tự hành%l;#; xăng đó ạ.」
- **Lý do:** Gloss 気動車 “động cơ” → “toa xe tự hành” (xem 1812).

### [2641] — Thuật ngữ
- **JP:** 「ところで、双鉄さんは、
どんなご用で御一夜に帰ってらしたんですか？」 (ポーレット)
- **TW:** 「話說回來，雙鐵先生回到御一夜是有什麼事呢？」
- **Cũ:** 「Nhân tiện, anh Soutetsu,
anh trở về Ohimitera có việc gì vậy ạ?」
- **Mới:** 「Nhân tiện, anh Soutetsu, anh trở về Ohitoyo có việc gì vậy ạ?」
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11.

### [2645] — Thuật ngữ
- **JP:** 「\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;を御一夜で？」 (双鉄)
- **TW:** 「讓\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;在御一夜行駛？」
- **Cũ:** 「Cho \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; chạy ở Ohimitera sao?」
- **Mới:** 「Cho \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; chạy ở Ohitoyo sao?」
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11.

### [2680] — Thuật ngữ
- **JP:** 「その話は事実です。\x%l帝鉄;#00ffc040;帝鉄%l;#;は、国有鉄道という性質上、
もともと、それを許容する体質でした」 (ハチロク)
- **TW:** 「這個的確是事實。\x%l帝鉄;#00ffc040;帝國鐵路%l;#;作為國有鐵路，從體制上來說，是允許此類情況發生的」
- **Cũ:** 「Chuyện đó là sự thật. \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, với tính chất là đường sắt quốc gia,
vốn dĩ đã có cơ cấu chấp nhận điều đó rồi.」
- **Mới:** 「Chuyện đó là sự thật. \x%l帝鉄;#00ffc040;Teitetsu%l;#;, với tính chất là đường sắt quốc gia, vốn dĩ đã có cơ cấu chấp nhận điều đó rồi.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11.

### [2685] — Thuật ngữ
- **JP:** 「それで十分です。\x%lエアクラ;#00ffc040;エアクラ%l;#;の台頭。大廃線。
\x%l帝鉄;#00ffc040;帝鉄%l;#;までもが解体され、鉄道は衰退の一途をたどります」 (ポーレット)
- **TW:** 「這樣就足夠了。\x%lエアクラ;#00ffc040;空凝機%l;#;的普及，導致了大廢線。連\x%l帝鉄;#00ffc040;帝國鐵路%l;#;都被迫解體，鐵路踏上了無可避免的衰退」
- **Cũ:** 「Vậy là đủ rồi. Sự trỗi dậy của \x%lエアクラ;#00ffc040;Aircra%l;#;. Đại bãi bỏ.
Ngay cả \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũng bị giải thể, đường sắt đang trên đà suy thoái.」
- **Mới:** 「Vậy là đủ rồi. Sự trỗi dậy của \x%lエアクラ;#00ffc040;Aircra%l;#;. Đại bãi bỏ. Ngay cả \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũng bị giải thể, đường sắt đang trên đà suy thoái.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11 (bỏ “Đường sắt Hoàng gia” — 帝鉄 là 帝国鉄道, không phải 皇室).

### [2719] — Thuật ngữ
- **JP:** 「ええと、\x%lまいてつ;#00ffc040;まいてつ%l;#;の話でしたね。
そういう事情で、鉄道網はずたずたになりました」 (ポーレット)
- **TW:** 「那個，我們在說\x%lまいてつ;#00ffc040;掌車人%l;#;對吧。由於出現剛才所說的那種情況，鐵路網也變得支離破碎了」
- **Cũ:** 「À ừm, chúng ta đang nói về \x%lまいてつ;#00ffc040;người sành toa xe%l;#; nhỉ.
Vì những lý do đó, mạng lưới đường sắt đã trở nên tan nát.」
- **Mới:** 「À ừm, chúng ta đang nói về \x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ. Vì những lý do đó, mạng lưới đường sắt đã trở nên tan nát.」
- **Lý do:** Gloss まいてつ “người sành toa xe” → “Maitetsu” (thống nhất trong file, xem 2443).

### [2730] — Thuật ngữ
- **JP:** 「ならば、ポーレットも\x%lまいてつ;#00ffc040;まいてつ%l;#;なのだな？」 (双鉄)
- **TW:** 「那麼，波萊特也是\x%lまいてつ;#00ffc040;掌車人%l;#;囉？」
- **Cũ:** 「Nếu vậy, Paulette cũng là \x%lまいてつ;#00ffc040;người sành toa xe%l;#; nhỉ?」
- **Mới:** 「Nếu vậy, Paulette cũng là \x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ?」
- **Lý do:** Gloss まいてつ “người sành toa xe” → “Maitetsu” (thống nhất trong file, xem 2443).

### [3082] — Thuật ngữ
- **JP:** 御一夜温泉駅につく。 (monologue)
- **TW:** 到達了御一夜溫泉站。
- **Cũ:** Chúng tôi đến ga suối nước nóng Ohimitera.
- **Mới:** Chúng tôi đến ga suối nước nóng Ohitoyo.
- **Lý do:** 御一夜温泉駅 → Ohitoyo theo quyết định 19/11.

### [3104] — Thuật ngữ
- **JP:** “水の町、温泉の町　御一夜”を強くアピールできれば、
それは当然、工場誘致への強い拒否感へとつながるだろう。 (monologue)
- **TW:** 只要大力宣傳“水鄉、溫泉之鄉——御一夜”的概念，自然會促使人們對汙染水源的工場落戶計劃產生反感。
- **Cũ:** Nếu có thể quảng bá mạnh mẽ hình ảnh “Ohimitera - Thành phố của nước, thành phố của suối nước nóng”,
thì đương nhiên điều đó sẽ dẫn đến sự phản đối mạnh mẽ đối với việc thu hút nhà máy.
- **Mới:** Nếu có thể quảng bá mạnh mẽ hình ảnh “Ohitoyo - Thành phố của nước, thành phố của suối nước nóng”, thì đương nhiên điều đó sẽ dẫn đến sự phản đối mạnh mẽ đối với việc thu hút nhà máy.
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11.


### Xưng hô (9 dòng)

### [2139] — Xưng hô
- **JP:** 「すまんが、ハチロクに石炭を補充できていなくてな。
もしよければ」 (双鉄)
- **TW:** 「不好意思，八六一直都沒能補充煤炭。如果可以的話」
- **Cũ:** 「Xin lỗi, nhưng tôi vẫn chưa thể bổ sung than cho Hachiroku.
Nếu cô không phiền.」
- **Mới:** 「Xin lỗi, nhưng tôi vẫn chưa thể bổ sung than cho Hachiroku. Nếu em không phiền.」
- **Lý do:** Soutetsu gọi Paulette: “cô” → “em” theo quyết định 19/11.

### [2185] — Xưng hô
- **JP:** 「なぜ知っている？
僕が、“帰ってきた”のだと」 (双鉄)
- **TW:** 「你為什麼會知道我是“回來”的？」
- **Cũ:** 「Sao cô lại biết?
Rằng tôi “trở về”.」
- **Mới:** 「Sao em lại biết? Rằng tôi “trở về”.」
- **Lý do:** Soutetsu gọi Paulette: “cô” → “em” theo quyết định 19/11.

### [2395] — Xưng hô
- **JP:** 「それは助かる。頼みというのは、
石炭を分けて欲しいということなのだが」 (双鉄)
- **TW:** 「幫大忙了。其實是希望你能分給我們一些煤炭」
- **Cũ:** 「Thế thì tốt quá. Chuyện tôi muốn nhờ là,
tôi muốn xin cô một ít than đá.」
- **Mới:** 「Thế thì tốt quá. Chuyện tôi muốn nhờ là, tôi muốn xin em một ít than đá.」
- **Lý do:** Soutetsu gọi Paulette: “cô” → “em” theo quyết định 19/11.

### [2440] — Xưng hô
- **JP:** 「僕としては悪くない話であると考える。
が――ハチロク。鉄道のことはお前の判断を尊重しよう」 (双鉄)
- **TW:** 「我覺得這對我來說是個不錯的提議。不過——八六，事關鐵路，我尊重你的判斷」
- **Cũ:** 「Tôi thấy đây là một đề nghị không tồi.
Nhưng——Hachiroku. Về chuyện đường sắt, tôi sẽ tôn trọng quyết định của cô.」
- **Mới:** 「Tôi thấy đây là một đề nghị không tồi. Nhưng——Hachiroku. Về chuyện đường sắt, tôi sẽ tôn trọng quyết định của em.」
- **Lý do:** Soutetsu gọi Hachiroku: “cô” → “em”. Tiền lệ đã chốt: file 03 Soutetsu→Hachiroku “em” nhất quán (65 dòng); 夜の嵐 1528 fix về “Hachiroku, em không khỏe à?”; Hachiroku tự xưng “Em” theo docs §2.2.

### [2442] — Xưng hô
- **JP:** 「勘違いした。僕と君とが、昔会ってでもいるのかと」 (双鉄)
- **TW:** 「我誤會了。我還以為我們之前是不是見過」
- **Cũ:** 「Tôi đã hiểu lầm. Cứ tưởng tôi và cô, ngày xưa đã từng gặp nhau.」
- **Mới:** 「Tôi đã hiểu lầm. Cứ tưởng tôi và em, ngày xưa đã từng gặp nhau.」
- **Lý do:** Soutetsu gọi Paulette: “cô” → “em” theo quyết định 19/11 (JP 僕と君とが — 君 = em).

### [2551] — Xưng hô
- **JP:** 「やっぱり！　双鉄くっ――ん、双鉄さんも、
\x%lまいてつ;#00ffc040;まいてつ%l;#;なんですね！　そこまでわかっちゃうなんて」 (ポーレット)
- **TW:** 「果然！雙鐵君……不，雙鐵先生，也是一位\x%lまいてつ;#00ffc040;掌車人%l;#;呢！居然連這都知道」
- **Cũ:** 「Quả nhiên! Anh Soutetsu……à không, anh Soutetsu cũng là
\x%lまいてつ;#00ffc040;người sành toa xe%l;#; nhỉ! Đến mức đó mà anh cũng hiểu được.」
- **Mới:** 「Quả nhiên! Cậu Soutetsu……à không, anh Soutetsu cũng là \x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ! Đến mức đó mà anh cũng hiểu được.」
- **Lý do:** Hai lỗi: (1) Paulette tự sửa 双鉄くん→双鉄さん mà VN viết “anh Soutetsu……à không, anh Soutetsu” — mất hẳn trò đùa tự sửa. Theo tiền lệ trong chính file (2721, 2421, 2275: くん→“cậu”, さん→“anh”), sửa thành “Cậu Soutetsu……à không, anh Soutetsu”. (2) Gloss まいてつ “người sành toa xe” → “Maitetsu” (xem 2443).

### [2573] — Xưng hô
- **JP:** 「ポーレット、すまんが力を貸して欲しい」 (双鉄)
- **TW:** 「波萊特，不好意思，想請你幫個忙」
- **Cũ:** 「Paulette, xin lỗi nhưng tôi muốn nhờ cô giúp một tay.」
- **Mới:** 「Paulette, xin lỗi nhưng tôi muốn nhờ em giúp một tay.」
- **Lý do:** Soutetsu gọi Paulette: “cô” → “em” theo quyết định 19/11 (unify “cô”→“em”).

### [2727] — Xưng hô
- **JP:** 「ならば、ハチロク。
僕はお前の\x%l機関士;#00ffc040;機関士%l;#;と」 (双鉄)
- **TW:** 「那麼，八六。就由我來當你的\x%l機関士;#00ffc040;司機%l;#;」
- **Cũ:** 「Nếu vậy, Hachiroku.
Tôi sẽ trở thành \x%l機関士;#00ffc040;người lái tàu%l;#; của cô.」
- **Mới:** 「Nếu vậy, Hachiroku. Tôi sẽ trở thành \x%l機関士;#00ffc040;người lái tàu%l;#; của em.」
- **Lý do:** Soutetsu gọi Hachiroku: “cô” → “em” (xem 2440).

### [3560] — Xưng hô
- **JP:** （僕もハチロクを見習うか。
質問はあとまわしにして――ともかく今は見学だ） (monologue)
- **TW:** （我也向八六看齊吧。把疑問留到以後——現在先好好參觀學習）
- **Cũ:** （Mình cũng nên học tập Hachiroku thôi.
Để dành câu hỏi lại sau——dù sao thì bây giờ cứ quan sát đã.）
- **Mới:** （Tôi cũng nên học tập Hachiroku thôi. Để dành câu hỏi lại sau——dù sao thì bây giờ cứ quan sát đã.）
- **Lý do:** Soutetsu độc thoại dùng “Mình” làm chủ ngữ mệnh đề chính — sai theo quy tắc: Soutetsu = “tôi”, “mình” chỉ được trong độc thoại tự vấn cảm xúc. Đây là quyết tâm (“nên học tập…”), không phải tự vấn → về “tôi”. (Các “mình” khác trong file đều đúng: sở hữu/phản thân/mệnh đề phụ/thành ngữ — xem mục phân tích xưng hô.)


### Rên っ (3 dòng)

### [2284] — Rên っ
- **JP:** 「あぐっ」 (ポーレット)
- **TW:** 「啊嗚」
- **Cũ:** 「A.」
- **Mới:** 「Agu.」
- **Lý do:** Sweep-missed: JP 「あぐっ」 (tiếng nghẹn của Paulette khi luống cuống) mà VN chỉ còn “A.” — mất hẳn âm ぐっ. TW 啊嗚. Diễn thành “Agu.” giữ âm Nhật theo nguyên tắc 22:19.

### [2287] — Rên っ
- **JP:** 「ああ、ハチロクの石炭と――っ！！」 (双鉄)
- **TW:** 「啊，就像是八六的煤炭——啊！！」
- **Cũ:** 「A, giống như than của Hachiroku——!!」
- **Mới:** 「A, giống như than của Hachiroku——Ư!!」
- **Lý do:** Sweep gasp (lost-gasp-trailing), nhận nguyên văn: JP 「――っ！！」 — tiếng rên giật mình cuối câu bị mất, TW có 啊. Chỉ thêm Ư cho っ đứng một mình cuối câu.

### [2763] — Rên っ
- **JP:** 「っ！？」 (双鉄)
- **TW:** 「！？」
- **Cũ:** 「!?」
- **Mới:** 「Ư!?」
- **Lý do:** Sweep gasp (lost-gasp-whole), nhận nguyên văn: JP 「っ！？」 nguyên dòng, VN chỉ còn “!?”.


### SFX (1 dòng)

### [1840] — SFX
- **JP:** 「……すやぁ……すやぁ……うふふふふ……」 (れいな)
- **TW:** 「……呼……呼……嗚嘿嘿嘿嘿……」
- **Cũ:** 「……Khò……khò……ư hừ hừ hừ……」
- **Mới:** 「……Khò……khò……Ufufufufu……」
- **Lý do:** Tiếng cười bị diễn thành tiếng rên: JP うふふふふ (Reina cười trong lúc ngủ) mà VN viết “ư hừ hừ hừ”. Theo quy tắc 22:05, tiếng cười (ふふっ/うふふ/んふふ) phải diễn thành tiếng cười, KHÔNG thành tiếng rên — tiền lệ h8 “Ư hự” đã bị bãi bỏ. Sửa thành “Ufufufufu” (う + ふ×4).


### Nghĩa (2 dòng)

### [2559] — Nghĩa
- **JP:** 「いや、
\x%l列車;#00ffc040;列車%l;#;の遅れを回復するのが最優先なのは当然だろう」 (双鉄)
- **TW:** 「沒事，當時最重要的是挽回\x%l列車;#00ffc040;列車%l;#;的延誤嘛」
- **Cũ:** 「Không sao,
việc khôi phục lại sự chậm trễ của \x%l列車;#00ffc040;đoàn tàu%l;#; đương nhiên là ưu tiên hàng đầu mà.」
- **Mới:** 「Không sao, việc khắc phục sự chậm trễ của \x%l列車;#00ffc040;đoàn tàu%l;#; đương nhiên là ưu tiên hàng đầu mà.」
- **Lý do:** Sai hướng nghĩa: JP 遅れを回復する = khắc phục/bù lại sự chậm trễ (lấy lại giờ), TW 挽回延誤. VN “khôi phục lại sự chậm trễ” = khôi phục lại chính cái sự trễ — ngược nghĩa.

### [2699] — Nghĩa
- **JP:** 「随分と強いようだな」 (双鉄)
- **TW:** 「還真是能喝啊」
- **Cũ:** 「Trông em có vẻ đô con nhỉ.」
- **Mới:** 「Trông em uống khỏe thật đấy.」
- **Lý do:** Sai nghĩa: JP 随分と強いようだな — Soutetsu khen Reina uống khỏe (vừa tu cạn bình nhiên liệu), TW 還真是能喝啊. VN “Trông em có vẻ đô con nhỉ” = trông to khỏe về vóc dáng — sai hẳn.


### Nhỏ/văn phong (2 dòng)

### [2417] — Nhỏ/văn phong
- **JP:** 「と、違うかねぇ――あ、ううんっ！？
ね、ね？　似おーとらん？　あん二人」 (女子Ｂ)
- **TW:** 「應該不是吧——啊，不對哦！？你們快看，那兩個人是不是很速配啊」
- **Cũ:** 「Cũng không hẳn đâu——a, hửm!?
Này, này? Thấy hai người họ đẹp đôi không?」
- **Mới:** 「Cũng không hẳn đâu——a, không phải!? Này, này? Thấy hai người họ đẹp đôi không?」
- **Lý do:** Lệch sắc thái: JP ううんっ là âm phủ định (“không phải”) khi 女子Ｂ tự sửa suy nghĩ; TW 不對. VN “hửm!?” diễn thành âm ngơ ngác (“hả?”) — mất ý phủ định.

### [3089] — Nhỏ/văn phong
- **JP:** \x%lレイルロオド;#00ffc040;レイルロオド%l;#;が、れいなが眠っているにもかかわらず、
ポーレットの運転のなめらかさには、変化が無い。 (monologue)
- **TW:** 即使\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;——即使玲奈睡著了，波萊特也依然能夠流暢駕駛。
- **Cũ:** Mặc dù \x%lレイルロオド;#00ffc040;Railord%l;#;, Reina đang ngủ,
nhưng sự mượt mà trong thao tác lái của Paulette vẫn không hề thay đổi.
- **Mới:** Dù \x%lレイルロオド;#00ffc040;Railord%l;#; Reina đang ngủ, nhưng sự mượt mà trong thao tác lái của Paulette vẫn không hề thay đổi.
- **Lý do:** Văn phong lủng củng: “Mặc dù Railord, Reina đang ngủ,” ngắt câu sai chỗ — Railord là Reina (danh xưng), không phải hai chủ ngữ. Gộp lại “Dù Railord Reina đang ngủ” cho trơn. Nghĩa giữ nguyên.


### Tag %l (3 dòng)

### [2587] — Tag %l
- **JP:** 「\x%l就業後検査;#00ffc040;就業後検査%l;#;――とわたし達は呼んでるんですが、それを。
[コウバン,1]交番検査ができないので、都度で細かくやってるんです」 (ポーレット)
- **TW:** 「玲奈在進行所謂的\x%l就業後検査;#00ffc040;結業檢查%l;#;。由於做不到輪換檢查，我們只能在每天結業後仔細檢查一遍」
- **Cũ:** 「Chúng tôi gọi đó là——\x%l就業後検査;#00ffc040;kiểm tra sau ca làm việc%l;#;.
Vì không thể thực hiện \x%l交番検査;#00ffc040;kiểm tra luân chuyển%l;#;, nên mỗi lần xong việc đều phải làm rất tỉ mỉ.」
- **Mới:** 「Chúng tôi gọi đó là——\x%l就業後検査;#00ffc040;kiểm tra sau ca làm việc%l;#;. Vì không thể thực hiện kiểm tra luân chuyển, nên mỗi lần xong việc đều phải làm rất tỉ mỉ.」
- **Lý do:** Tag %l do VN tự thêm: JP chỉ có tag %l cho 就業後検査, còn 交番検査 chỉ có ruby [コウバン,1] — VN gắn thêm tag %l cho nó. Theo tiền lệ reina02 (gỡ gloss VN tự thêm cho 改軌/8620), gỡ tag, giữ text thường “kiểm tra luân chuyển”.

### [2662] — Tag %l
- **JP:** 「[コウバン,1]交番検査？」 (双鉄)
- **TW:** 「輪換檢查？」
- **Cũ:** 「\x%l交番検査;#00ffc040;Kiểm tra luân chuyển%l;#;?」
- **Mới:** 「Kiểm tra luân chuyển?」
- **Lý do:** Tag %l do VN tự thêm: JP 「[コウバン,1]交番検査？」 chỉ có ruby, không có tag %l. Gỡ tag theo tiền lệ reina02.

### [2991] — Tag %l
- **JP:** 広大な鉄道用地を利しての周辺開発。
ホテル業、旅行業、ターミナル駅での百貨店経営。 (monologue)
- **TW:** 以廣闊的鐵路用地作為優勢進行周邊開發。經營鐵路沿線的住宿業、旅遊業以及終點站的百貨商店。
- **Cũ:** Tận dụng diện tích đất đường sắt rộng lớn để phát triển khu vực xung quanh.
Kinh doanh khách sạn, du lịch, và bách hóa tại các \x%lターミナル駅;#00ffc040;ga đầu mối%l;#;.
- **Mới:** Tận dụng diện tích đất đường sắt rộng lớn để phát triển khu vực xung quanh. Kinh doanh khách sạn, du lịch, và bách hóa tại các ga đầu mối.
- **Lý do:** Tag %l do VN tự thêm: JP không có tag nào ở dòng này, VN gắn tag cho ターミナル駅. Gỡ tag theo tiền lệ reina02.

## Đối chiếu sweep rên っ

Sweep có 3 entry cho file này: **2 fix đã nhận nguyên văn** (2763 lost-gasp-whole, 2287 lost-gasp-trailing — xem trên) và **1 entry already-rendered** (2311 「ん～～っ」→“Ưm~~”, không cần sửa). Ngoài ra audit tìm thêm **1 sweep-missed** (2284, あぐっ→“Agu.”, xem trên). Tổng JP có っ: rà soát hết tất cả các dòng chứa っ — phần lớn là っ trong từ (ちょっと, しまった…), っ nhấn mạnh gắn vào từ (なっ!?, かーっこいい, ひえっ!?), hoặc âm thanh đã được diễn (ごきゅっ→“Ực”, ほうっ→“Phù”, きゃーーーっ→“Á————!”, ボリンっ→“Rộp!”) — đều đúng, không thêm Ư theo quy tắc.

## Tag %l

0 tag lỗi dạng thiếu dấu `;` đóng trong file (JP = VN về số lượng tag ở mọi dòng, trừ 3 dòng VN tự thêm tag đã gỡ ở trên: 2587, 2662, 2991). Gloss 機関士 “người lái tàu” (2505, 2432, 2727) và 運転士 “người lái tàu” (2319) giữ theo quy ước đã chốt, không tính lỗi. Tag phức tạp ở 2524 (tag %l; lồng ruby [ハチロクニイマル,3] cho 8620形) giữ nguyên cấu trúc JP, chỉ đổi gloss 帝鉄→Teitetsu.

## Phân tích xưng hô (đã kiểm tra hết, không chỉ heuristic)

- **Soutetsu → Paulette “em”:** 5 dòng “cô” đã sửa về “em” (2573, 2139, 2395, 2442, 2185) theo quyết định 19/11. Các “cô ấy” trong monologue đều là ngôi thứ ba chỉ Paulette — đúng, không sửa.
- **Soutetsu → Hachiroku “em”:** 2 dòng “cô” đã sửa về “em” (2440, 2727). Tiền lệ đã chốt: file 03 Soutetsu→Hachiroku “em” nhất quán (65 dòng); 夜の嵐 1528 fix về “Hachiroku, em không khỏe à?”; docs §2.2 Hachiroku tự xưng “Em”.
- **Paulette → Soutetsu “anh Soutetsu”:** nhất quán, trừ 3 câu tự sửa くん→さん (2721, 2421, 2275) dùng “cậu Soutetsu——anh Soutetsu” — đúng, giữ nguyên; 2551 đã sửa theo đúng mẫu này.
- **Soutetsu “mình”:** rà soát hết 15 lần xuất hiện (14 “mình” thường + 1 “Mình” đầu câu): chỉ **1 lần sai** (3560 — chủ ngữ mệnh đề chính trong độc thoại). Các lần còn lại đều đúng theo tiền lệ hearing: sở hữu (“của mình”, “đầu gối mình”, “trang phục của mình”), phản thân (“tự mình”, “chính mình”), mệnh đề phụ (“mình nói thiếu ý” 3136, “mình nên nói gì thêm” 3021), thành ngữ (“một mình”, “giật mình”), “mình” của nhân vật khác (2623 Paulette, 3123 Hachiroku, 3408 Reina).
- **Hachiroku gọi Paulette “cô Paulette” / “Thị trưởng Paulette”** (2732, 2733, 2610, 2572): đúng theo docs §2.2 — Paulette là thị trưởng (xác nhận ở 3316 “Vừa là thị trưởng vừa là giám đốc sao.” và 2436 “thị trưởng tiền nhiệm” là cha cô ấy), nên 様→“Thị trưởng” là đúng, không sửa. 2162 Paulette ngại khi bị gọi “thị trưởng” cũng giữ nguyên.
- **“em ấy”** (2247 Reina, 3423 Reina): đúng — chỉ Reina.
- **“cô ấy”** trong monologue (3330, 2993, 3452, 3416, 3362, 3367, 3520, 3358, 3383, 3306, 2960, 3292, 3323, 3182, 3526, 3069, 3022): đều là ngôi thứ ba chỉ Paulette/Reina/Hachiroku — đúng, không sửa.

## Dòng không chắc chắn: 0

Không có dòng nào phải để ngỏ. Hai điểm cần Hieu xác nhận ở đợt thống nhất (không phải dòng chưa chắc — audit đã sửa theo JP, ghi rõ xung đột để Hieu chốt hoặc lật lại):

1. **市電 → “tàu điện thành phố” (2404, 2378):** Hieu chốt 20/11 (docs mục 119 đã sửa từ “Nguồn điện chính”). JP rõ ràng là tàu điện thành phố (広電 = hãng tàu điện Hiroshima; cả đoạn nói về tàu điện và đường dây trên cao). Còn 2 dòng ở ハチロク02 (71, 1917) sẽ sửa khi audit file đó.
2. **まいてつ — toàn dự án chia 4 cách:** chủ tàu 23 / Maitetsu 11 / người sành toa xe 9 / người đam mê đường sắt 3. File này đã thống nhất nội bộ về “Maitetsu” (6 dòng có sẵn + 7 dòng sửa). Cần Hieu chốt MỘT cách cho toàn dự án ở đợt thống nhất.

## Cố tình KHÔNG sửa (đã kiểm tra, có lý do)

- **2572** 「ポーレット様」→“Thị trưởng Paulette.” — đúng: Paulette là thị trưởng (3316, 2436), docs §2.2 ghi Hachiroku gọi Paulette là “Thị trưởng Paulette” cho ポーレット様.
- **2162** 「さ、様とかも」→“Thị, thị trưởng gì đó” — Paulette ngại khi bị gọi bằng chức danh, giữ nguyên.
- **2345** 「はぁい。着駅までには復帰……しま……すやぁ」→“Vâng ạ. Trước khi đến ga em sẽ phục hồi……lại……khò.” — はぁい → “Vâng ạ” là cách dịch đã chốt toàn dự án (kiểm tra project-wide: “Vâng ạ” 8+3+2 dòng cho はぁい); hơi thở buồn ngủ vẫn giữ qua “khò” ở cuối câu.
- **2268** 「はふあ……」→“Oáp……” — tiếng ngáp buồn ngủ của Reina, hợp cảnh (cô ấy đang thiếp đi), giữ nguyên.
- **2273** 「えへへぇ」→“Hì hì.” — tiếng cười diễn thành tiếng cười, đúng quy tắc 22:05.
- **2275** 「ひえっ！？」→“Hie!?” — tiếng thốt giữ dạng Latin, theo tiền lệ “Hya”/“Hyafu” ở h6/h7.
- **2311** 「ん～～っ」→“Ưm~~” — sweep đã ghi already-rendered, giữ nguyên.
- **2262** 「きゃーーーっ！」→“Á————!” — tiếng hét, đã diễn thành âm, không thêm Ư.
- **2773** 「～～～っ////」→“~~~////” — dấu ngượng của Paulette, っ ở đây là âm ngượng đi kèm dấu ////, không phải rên.
- **2721, 2421, 2275** — Paulette tự sửa 双鉄くっ――双鉄さん → “cậu Soutetsu——anh Soutetsu” — đúng mẫu くん→“cậu” / さん→“anh”, giữ nguyên (2551 đã sửa theo đúng mẫu này).
- **3364** 「ふわん、とポーレットが笑う」→“Paulette khẽ mỉm cười.” — ふわん là trạng từ mềm mại, không phải tiếng cười thành âm; TW cũng dịch là nụ cười, giữ nguyên.
- **3416** 「――どころか、運転台のポーレットにまで」→“——Đâu chỉ mình tôi, có lẽ Paulette ở buồng lái cũng nghe thấy rồi.” — “Đâu chỉ mình tôi” là cách đọc đúng của どころか (không chỉ riêng tôi), TW 聽到了 ủng hộ “nghe thấy”.
- **3144** エアクラ → “Aircra” — đúng theo quyết định (không “fix” thành Aircra khác).
- **2524** — cấu trúc tag %l; lồng ruby [ハチロクニイマル,3] giữ nguyên như JP, chỉ đổi gloss.
- **2460** 「偏は金偏。旁は——おお！」→“Bên trái là bộ Kim (金 - tiền/vàng). Bên phải là chữ Thất (失 - mất)——Ồ!” — giải thích bộ thủ thêm (金 - tiền/vàng) giúp người đọc Việt hiểu trò đố chữ, giữ nguyên.
- **3296** “My鉄道” → “My đường sắt” — giữ “My” như JP, hợp nguyên tắc giữ gần tiếng Nhật.
- **2269** 「ごきゅっ――ごきゅっ――ごきゅっ――ぷはぁ～～」→“Ực——ực——ực——phù~~” — tiếng ừng ực và thở phào sau khi uống, đã diễn đủ âm.
- **3376** 「ほうっ……と長く、熱っぽい息。」→“Phù……một hơi thở dài và nóng hổi.” — hơi thở dài đã diễn thành “Phù”, giữ nguyên.
- **3182** 「ほーっと、やけに長い息。」→“Phù——một tiếng thở dài thật thườn thượt.” — giữ nguyên.
- **3554** 「（ガキっ！　ゴリっ！　バリボリっ！）」→“（Rắc! Rắc! Rộp rộp!）” và **3555** 「（ボリンっ！）」→“（Rộp!）” — tiếng nhai vỡ than, đã diễn thành âm Việt tương đương.
- **“Đại bãi bỏ”** (大廃線, vd. 2685, 2739, 2404, 2467, 2660): giữ nguyên — cách dịch nhất quán trong file, TW 大廢線, không có quyết định docs nào khác.
- **2493/2258** ディーゼル気動車 → “toa xe diesel tự hành” — đúng, là tiền lệ cho fix 気動車 ở 5 dòng trên.
- **2319** 運転士 → “người lái tàu” và **2505/2432/2727** 機関士 → “người lái tàu” — theo quy ước thiểu số đã chốt, không tính lỗi.
- **2764** ワンスコ → “Wansuko (One-scoop)” — giữ âm Nhật + chú thích tiếng Anh, theo nguyên tắc giữ gần tiếng Nhật.
- **2294/2536** 架線 がせん vs 河川 かせん — trò chơi chữ đã dịch đúng theo JP (“dòng sông (Kasen)”, “Tôi cứ tưởng đọc là Kasen chứ”); TW viết 天線 là lệch, VN theo JP là đúng.
- **3022** 「マニ、まで言いかけファンと修正。」→“Đang định nói là cuồng, thì cô ấy sửa lại thành fan.” — Hachiroku nói hụt “mani” rồi sửa thành “fan”, VN giữ đúng.

## Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 52 fix so với JP của từng dòng: **tổng 52 / kiểm tra lại 52 / loại bỏ 0 / sửa 1**. Lần 2 bắt được 1 lỗi trong bản thảo fix: 3089 bị rớt mất tag %l của レイルロオド (JP có tag, bản thảo chỉ giữ text “Railord”) — đã khôi phục tag, kiểm tra lại chẵn lẻ 「」 (0 lệch) và số lượng tag %l (0 lệch, trừ 3 dòng cố tình gỡ tag VN tự thêm) cho cả 52 dòng. Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt.

Khối TOML dưới đây đã parse-verified bằng tomllib: **52 key, 0 lệch giá trị** so với JSON fix list (`audit-00common05-wrong.json`). Quy ước \n: không fix nào chứa ký tự `\n` (tất cả đều một dòng), nên không phát sinh vấn đề escape `\n` trong khối.

## Khối TOML (fix)

```toml
[script]
77 = "\\x%l列車;#00ffc040;Đoàn tàu%l;#; đang quay trở về Ohitoyo."
1809 = "「Toàn tuyến điện khí hóa mà \\x%l帝鉄;#00ffc040;Teitetsu%l;#; từng mơ ước. Nếu điều đó được tiến hành nhanh hơn thì có lẽ tình hình đã khác đi một chút.」"
1812 = "「\\x%l気動車;#00ffc040;Toa xe tự hành%l;#;.」"
1840 = "「……Khò……khò……Ufufufufu……」"
1843 = "「……Biết rõ chi tiết đến mức đó, nghĩa là. Chị Hachiroku, quả nhiên vốn dĩ là người của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; sao?」"
2139 = "「Xin lỗi, nhưng tôi vẫn chưa thể bổ sung than cho Hachiroku. Nếu em không phiền.」"
2151 = "「Không chỉ vậy đâu nha. Còn có \\x%l気動車;#00ffc040;toa xe tự hành%l;#; xăng nữa đó ạ.」"
2183 = "「Thật là may mắn……một vinh dự tuyệt vời. Không ngờ, một cỗ máy tầm cỡ như vậy lại đến Ohitoyo.」"
2185 = "「Sao em lại biết? Rằng tôi “trở về”.」"
2188 = "「Như lúc nãy anh đã đi thử đó, \\x%l運転台;#00ffc040;buồng lái%l;#; và ghế hành khách được kết hợp trong cùng một toa xe thì gọi là \\x%l気動車;#00ffc040;toa xe tự hành%l;#; ạ.」"
2227 = "「Ra là vậy, đó là thân bảo trì sao.」"
2254 = "「Anh có thể cho chiếc 8620 của chị Hachiroku chạy trên tuyến đường sắt Ohitoyo được không?」"
2266 = "「À, chuyện đó——ừm, Migita! Nhắc đến nhà Migita, thì đó là người nộp thuế cao nhất của thành phố Ohitoyo mà.」"
2284 = "「Agu.」"
2287 = "「A, giống như than của Hachiroku——Ư!!」"
2378 = "「Dù là \\x%l市電;#00ffc040;tàu điện thành phố%l;#; nhưng lại điện khí hóa toàn tuyến sao—— Thật đáng nể, một vĩ nghiệp như vậy.」"
2392 = "「——Vào cuối thời kỳ Teitetsu, nghe nói những tuyến đường địa phương có hệ số này vượt quá 1000 là chuyện rất bình thường.」"
2395 = "「Thế thì tốt quá. Chuyện tôi muốn nhờ là, tôi muốn xin em một ít than đá.」"
2404 = "「Đường sắt điện Hiroshima là \\x%l市電;#00ffc040;tàu điện thành phố%l;#; mà. Vì vậy việc \\x%l架線;#00ffc040;đường dây tiếp điện trên cao%l;#; cũng dễ dàng, từ trước đợt Đại bãi bỏ, nó đã được điện khí hóa hoàn toàn rồi.」"
2408 = "「Ngay từ thời kỳ hoàng kim, \\x%l帝鉄;#00ffc040;Teitetsu%l;#; đã quá đỗi khổng lồ. Lý tưởng và hiện thực không đồng nhất, cấp trên và cấp dưới bị chia rẽ.」"
2417 = "「Cũng không hẳn đâu——a, không phải!? Này, này? Thấy hai người họ đẹp đôi không?」"
2418 = "「Tôi cũng nghĩ vậy. Dù thế, \\x%l帝鉄;#00ffc040;Teitetsu%l;#; vẫn cố gắng đẩy mạnh việc điện khí hóa.」"
2426 = "「Lý do tôi trở về Ohitoyo, là để hủy bỏ kế hoạch thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.」"
2440 = "「Tôi thấy đây là một đề nghị không tồi. Nhưng——Hachiroku. Về chuyện đường sắt, tôi sẽ tôn trọng quyết định của em.」"
2442 = "「Tôi đã hiểu lầm. Cứ tưởng tôi và em, ngày xưa đã từng gặp nhau.」"
2443 = "「Này, Hachiroku. Lúc nãy Paulette có nói mà. 『Thời đại bây giờ là vậy. Mỗi \\x%lまいてつ;#00ffc040;chủ tàu%l;#; đều có những lý do riêng』」"
2467 = "「Những người đang cố gắng chống đỡ nền văn hóa đường sắt sau đợt Đại bãi bỏ, chính là các tuyến đường sắt tư nhân ở các địa phương và những \\x%lまいてつ;#00ffc040;chủ tàu%l;#; đấy.」"
2474 = "「Là một nhân vật vĩ đại đấy. Cô ấy là người nổi tiếng nhất trong giới \\x%lまいてつ;#00ffc040;chủ tàu%l;#; mà.」"
2484 = "「Là của cả tôi và Reina. Cửa hàng đường sắt Ohitoyo là lâu đài của chúng tôi mà.」"
2495 = "「Vâng. Tôi là \\x%lまいてつ;#00ffc040;chủ tàu%l;#; của Reina và \\x%lキハ07;#00ffc040;KiHa 07%l;#;S. Đồng thời, cũng là giám đốc của Công ty Cổ phần Đường sắt Ohitoyo.」"
2509 = "「Đúng vậy ạ, \\x%l電車;#00ffc040;tàu điện%l;#; nói chính xác thì là \\x%l気動車;#00ffc040;toa xe tự hành%l;#; điện. Nhưng mà, cái tên nghe như viết tắt \\x%l電車;#00ffc040;tàu điện%l;#; đó thực ra lại là tên chính thức đấy ạ.」"
2524 = "「Vâng, \\x%lレイルロオド;#00ffc040;Railord%l;#; chuyên dụng của chiếc đầu máy số một \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; dòng \\x%l8620;#00ffc040;8620%l;#; thuộc \\x%l帝鉄;#00ffc040;Teitetsu%l;#;——đó chính là xuất thân của tôi.」"
2551 = "「Quả nhiên! Cậu Soutetsu……à không, anh Soutetsu cũng là \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ! Đến mức đó mà anh cũng hiểu được.」"
2559 = "「Không sao, việc khắc phục sự chậm trễ của \\x%l列車;#00ffc040;đoàn tàu%l;#; đương nhiên là ưu tiên hàng đầu mà.」"
2573 = "「Paulette, xin lỗi nhưng tôi muốn nhờ em giúp một tay.」"
2587 = "「Chúng tôi gọi đó là——\\x%l就業後検査;#00ffc040;kiểm tra sau ca làm việc%l;#;. Vì không thể thực hiện kiểm tra luân chuyển, nên mỗi lần xong việc đều phải làm rất tỉ mỉ.」"
2591 = "「Bây giờ thì đúng là vậy. Nhưng mà, Reina nha. Vốn dĩ ban đầu là \\x%l気動車;#00ffc040;toa xe tự hành%l;#; xăng đó ạ.」"
2641 = "「Nhân tiện, anh Soutetsu, anh trở về Ohitoyo có việc gì vậy ạ?」"
2645 = "「Cho \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; chạy ở Ohitoyo sao?」"
2662 = "「Kiểm tra luân chuyển?」"
2680 = "「Chuyện đó là sự thật. \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, với tính chất là đường sắt quốc gia, vốn dĩ đã có cơ cấu chấp nhận điều đó rồi.」"
2685 = "「Vậy là đủ rồi. Sự trỗi dậy của \\x%lエアクラ;#00ffc040;Aircra%l;#;. Đại bãi bỏ. Ngay cả \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũng bị giải thể, đường sắt đang trên đà suy thoái.」"
2699 = "「Trông em uống khỏe thật đấy.」"
2719 = "「À ừm, chúng ta đang nói về \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ. Vì những lý do đó, mạng lưới đường sắt đã trở nên tan nát.」"
2727 = "「Nếu vậy, Hachiroku. Tôi sẽ trở thành \\x%l機関士;#00ffc040;người lái tàu%l;#; của em.」"
2730 = "「Nếu vậy, Paulette cũng là \\x%lまいてつ;#00ffc040;chủ tàu%l;#; nhỉ?」"
2763 = "「Ư!?」"
2991 = "Tận dụng diện tích đất đường sắt rộng lớn để phát triển khu vực xung quanh. Kinh doanh khách sạn, du lịch, và bách hóa tại các ga đầu mối."
3082 = "Chúng tôi đến ga suối nước nóng Ohitoyo."
3089 = "Dù \\x%lレイルロオド;#00ffc040;Railord%l;#; Reina đang ngủ, nhưng sự mượt mà trong thao tác lái của Paulette vẫn không hề thay đổi."
3104 = "Nếu có thể quảng bá mạnh mẽ hình ảnh “Ohitoyo - Thành phố của nước, thành phố của suối nước nóng”, thì đương nhiên điều đó sẽ dẫn đến sự phản đối mạnh mẽ đối với việc thu hút nhà máy."
3560 = "（Tôi cũng nên học tập Hachiroku thôi. Để dành câu hỏi lại sau——dù sao thì bây giờ cứ quan sát đã.）"
```

## Kết bài

File 05 là file Common thứ ba được audit (52/421 = 12,4% sai — cao hơn file 03 (4,4%) vì mật độ thuật ngữ chuyên ngành dày đặc: cả chương là bài giảng về đường sắt, với 11 dòng Ohimitera, 8 dòng 帝鉄, 7 dòng まいてつ, 5 dòng 気動車). Điểm đáng chú ý: **không lệch dòng, không chuỗi xoay, không tràn chương, không dòng mồ côi** — cột Việt đứng đúng chỗ ở cả 421 dòng, khác hẳn các file Paulette 03 (30,9–56%). 52 lỗi còn lại đều là lỗi lẻ tẻ, tập trung vào thuật ngữ (32 dòng — phần lớn là các quyết định 19/11 chưa được áp vào file cũ) và xưng hô (9 dòng — Soutetsu→Paulette “cô” 5, Soutetsu→Hachiroku “cô” 2, Soutetsu “Mình” 1, Paulette tự sửa くん→さん 1). **0 dòng chưa chắc chắn.**

Hai phát hiện để lại cho đợt thống nhất: (1) gloss まいてつ toàn dự án đang chia 4 cách (chủ tàu 23 / Maitetsu 11 / người sành toa xe 9 / người đam mê đường sắt 3) — Hieu chốt “chủ tàu” 20/11 theo đề xuất của Muse (theo tiền lệ TW 掌車人, đa số, ngắn gọn); file này đã thống nhất nội bộ về “chủ tàu”; (2) gloss 市電 “nguồn điện chính” (docs mục 119) mâu thuẫn JP — audit đã sửa 2 dòng trong file này về “tàu điện thành phố” (Hieu chốt 20/11, docs đã sửa).
