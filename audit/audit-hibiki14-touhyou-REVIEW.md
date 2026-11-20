# Audit — 日々姫14_投開票 (Hibiki 14, ngày bỏ phiếu / kiểm phiếu)

- File: `日々姫14_投開票.txt.toml` — route 02_Hibiki
- Disk: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb14_#U6295#U958b#U7968.txt.toml`
- CSV3: `Matetsu Last Run - Trang tính 3.csv` — 476 dòng script, 1 set duy nhất (không có dual-set), 0 key trùng
- Đã đọc: **476/476 dòng** (đọc tay từng dòng đối chiếu JP + TW)
- Kết quả: **24 dòng sai (5,0%)** — thuật ngữ 11, gasp 10, SFX 1, sai nghĩa 2
- Cơ sở tổng: 138 file / 6.285 dòng sai (đã tự kiểm chứng lại từ ROUTE-AUDIT.md)

## §1. Kiểm tra toàn vẹn

- Lệch vị trí: **0**. Xoay chuỗi (rotation): **0**. Nhiễm chéo file khác: **0**. Mồ côi (orphan): **0**. Chưa dịch: **0** (VN rỗng: 0). Key trùng: **0**.
- VN trùng nhau trong file: chỉ có `「Ưm……」` ở 1704 (JP 「ん……」) và 1730 (JP 「んっ……」) — hai tiếng hít gần giống nhau, đúng JP từng dòng, không phải lệch vị trí.
- TOML md5: `fe0d16d01d8081c02be60d88086da2e8` — **không có file TOML trùng** (duy nhất trong 227 file).
- TOML vs CSV3: 476/476 key khớp; 266 dòng VN TOML khác CSV3 chỉ ở chỗ `\n` bị flatten thành khoảng trắng (đặc tính TOML-2 đã biết) — CSV3 là bản chuẩn để audit, không tính là sai.
- Tag %l: 0 tag thiếu `;` trong VN file này; số tag JP = VN ở mọi dòng đã sửa (kiểm tra cơ học).
- Sweep っ-gasp: file có 11 entry trong `sweep-raw-gasp-wrong.json` — 10 entry lost-gasp đã kiểm chứng đúng JP và áp nguyên (1714, 1729, 1824, 2166, 2193, 2194, 2195, 2196, 2967, 3052); 1 entry already-rendered 1712 (むぅぅ～～っ → 「Ư ư~~」) giữ nguyên, không sửa. Sweep không bỏ sót entry nào cho file này.
- Không có fa/fu, ひあ/ひゃ trong file — quy tắc romaji fallback cho tiếng rên (Hieu duyệt 21/11 ~01:56) không áp dụng.
- Không có 乗務鞄/運転鞄/乗員/日ノ本/宮司/小畑/駿袋/まいてつ/市電 trong file.

## §2. Phân loại 24 dòng sai

| Loại | Số dòng | Keys |
|---|---|---|
| Thuật ngữ đã chốt | 11 | 1276 (×2 gloss), 1597 (×2 gloss), 1744, 1876, 2168, 2174, 2185, 2609, 2637, 2888, 3030 (×2 gloss) |
| Gasp っ (sweep) | 10 | 1714, 1729, 1824, 2166, 2193, 2194, 2195, 2196, 2967, 3052 |
| SFX | 1 | 1689 |
| Sai nghĩa | 2 | 1889, 2721 |

## §3. Chi tiết từng dòng sai

### 1276 — ポーレット (thuật ngữ ×2)

- **JP:** 「\x%l帝鉄;#00ffc040;帝鉄%l;#;[にまんにせんけいかい,6]22000系改、御一夜\x%l22形;#00ffc040;[ニイニイ,1]22系%l;#;1号\x%l客車;#00ffc040;客車%l;#;、\x%lイロ;#00ffc040;ナイロ[ニイニイイチ,2]221%l;#;改修の全工程は、終了しました」
- **TW:** 「\x%l帝鉄;#00ffc040;帝國鐵路%l;#;２２０００型改、御一夜\x%l22形;#00ffc040;２２型%l;#;１號\x%l客車;#00ffc040;客運車廂%l;#;、\x%lナイロ221;#00ffc040;Ｎａｉｒｏ２２１%l;#;的修復工程全部結束了」
- **Cũ:** 「Toa \x%l客車;#00ffc040;hành khách%l;#; số 1 Ohimitera \x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;,\ntoàn bộ quá trình cải tạo \x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」
- **Mới:** 「Toa \x%l客車;#00ffc040;hành khách%l;#; số 1 Ohitoyo \x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;,\ntoàn bộ quá trình cải tạo \x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo' (thuật ngữ đã chốt 19/11); 帝鉄 gloss 'Đường sắt Hoàng gia'→'Đường sắt Đế quốc' — đây là lần đầu 帝鉄 xuất hiện trong file (theo thứ tự script), dùng dạng đầy đủ trong thẻ %l, tiền lệ Common 01/09/10/14 (Common 10: key 63 đầy đủ, các key sau 'Teitetsu').

### 1597 — 双鉄 (thuật ngữ ×2)

- **JP:** 「\x%l運転体;#00ffc040;運転体%l;#;へ、\x%lタブレット;#00ffc040;タブレット%l;#;交換はしないのか？」
- **TW:** 「你不把\x%lタブレット;#00ffc040;操作板%l;#;替換到\x%l運転体;#00ffc040;駕駛體%l;#;上嗎？」
- **Cũ:** 「Không đổi \x%lタブレット;#00ffc040;thẻ bảng%l;#; sang \x%l運転体;#00ffc040;kíp lái%l;#; sao?」
- **Mới:** 「Không đổi \x%lタブレット;#00ffc040;máy tính bảng%l;#; sang \x%l運転体;#00ffc040;thân vận hành%l;#; sao?」
- **Lý do:** 運転体 'kíp lái'→'thân vận hành' — đó là thân thể, không phải kíp người (tiền lệ Common 08: 1456/1486/2517/2529/2692; TW 駕駛體 = thân lái); タブレット 'thẻ bảng'→'máy tính bảng' (tiền lệ Common 08/15, Paulette 11).

### 1689 — れいな (SFX)

- **JP:** 「はぅう～いいですねぇ。\nれいな、すっごくうらやましいですぅ」
- **TW:** 「哈呼～真好啊。玲奈好羨慕」
- **Cũ:** 「Haa~ Thích quá đi.\nReina, vô cùng ghen tị luôn đó ạ~」
- **Mới:** 「Hauu~ Thích quá đi.\nReina, vô cùng ghen tị luôn đó ạ~」
- **Lý do:** はぅう～ 'Haa~'→'Hauu~' — công thức độ dài nguyên âm: 1 + 2 (ぅ/う) = 3 nguyên âm (a,u,u); tiền lệ Grand 04 1833 'Hauu!', lr真闇追加02 1254 'Hauuu~'. Số nguyên âm đã kiểm lại độc lập (xem §6).

### 1714 — ふかみ (gasp, sweep)

- **JP:** 「あっ――あのッ――あうぅうう～っ！」
- **TW:** 「啊——那個——啊嗚嗚嗚嗚～！」
- **Cũ:** 「A――Cái đó――Auuuu~!」
- **Mới:** 「A――Cái đó――Auuuu~Ư!」
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN giữ dấu ~ nhưng mất tiếng hít っ cuối → thêm Ư. Số nguyên âm kiểm lại độc lập: あうぅうう = 1+4 = 5 (Auuuu).

### 1729 — 日々姫 (gasp, sweep)

- **JP:** 「はい――ずっと――っ！！」
- **TW:** 「嗯——永遠——！」
- **Cũ:** 「Vâng――sẽ mãi mãi――!!」
- **Mới:** 「Vâng――sẽ mãi mãi――Ư!!」
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN mất っ cuối → thêm Ư.

### 1744 — ハチロク (thuật ngữ)

- **JP:** 「はい、湯医で」
- **TW:** 「嗯，湯醫見」
- **Cũ:** 「Vâng, hẹn gặp ở ga Yui.」
- **Mới:** 「Vâng, hẹn gặp ở ga Yunoi.」
- **Lý do:** 湯医 'ga Yui'→'ga Yunoi' (thuật ngữ đã chốt 19/11; tiền lệ Hachiroku14_橋 1754 sửa trong audit theo chỉ đạo Hieu 21/11 01:51).

### 1824 — ふかみ (gasp, sweep)

- **JP:** 「き、[きのう,1]昨夜から！？　昨夜からって――はうう～っ！」
- **TW:** 「從、從昨天晚上開始！？從昨天晚上開始也就是——哈嗚～！」
- **Cũ:** 「Từ, từ đêm qua sao!? Từ đêm qua nghĩa là――Hauu~!」
- **Mới:** 「Từ, từ đêm qua sao!? Từ đêm qua nghĩa là――Hauu~Ư!」
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN mất っ cuối → thêm Ư. Số nguyên âm kiểm lại độc lập: はうう = 1+2 = 3 (Hauu).

### 1876 — ハチロク (thuật ngữ)

- **JP:** 「次に会うのは、湯医でとなることを期待します」
- **TW:** 「我期待下一次我們見面的地方是湯醫」
- **Cũ:** 「Kỳ vọng rằng lần tới chúng ta gặp nhau sẽ là ở ga Yui.」
- **Mới:** 「Kỳ vọng rằng lần tới chúng ta gặp nhau sẽ là ở ga Yunoi.」
- **Lý do:** 湯医 'ga Yui'→'ga Yunoi' (thuật ngữ đã chốt).

### 1889 — 日々姫 (sai nghĩa)

- **JP:** 「ボクって……え？　えと！　稀咲先輩っ！？」
- **TW:** 「我自己……哎？哎！稀咲學姐！？」
- **Cũ:** 「Bản thân chị…… Hả? À ừm! Tiền bối Kisaki!?」
- **Mới:** 「Boku…… Hả? À ừm! Tiền bối Kisaki!?」
- **Lý do:** ボクって là Hibiki nhắc lại từ ボク của Kisaki ở 1868 (「ボクを使ってほしい」) — ngạc nhiên trước cách tự xưng của Kisaki. Bản cũ 'Bản thân chị……' sai: Hibiki tự xưng 'em' với Kisaki (không bao giờ 'chị'), và 'bản thân' không có trong JP. Giữ nguyên từ được nhắc lại bằng romaji 'Boku' để giữ hiệu ứng echo; TW 我自己 chỉ là diễn đạt lỏng, JP thắng TW. Đây là lần duy nhất ボクって xuất hiện toàn dự án.

### 2166 — 日々姫 (gasp, sweep)

- **JP:** 「なら、私も。にぃにぃ――っ！」
- **TW:** 「那，我也。阿哥——！」
- **Cũ:** 「Nếu vậy, em cũng thế. Anh hai――!」
- **Mới:** 「Nếu vậy, em cũng thế. Anh hai――Ư!」
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN mất っ cuối → thêm Ư.

### 2168 — 双鉄 (thuật ngữ)

- **JP:** 「ならば、湯医で」
- **TW:** 「那，湯醫見」
- **Cũ:** 「Nếu vậy, hẹn gặp ở ga Yui.」
- **Mới:** 「Nếu vậy, hẹn gặp ở ga Yunoi.」
- **Lý do:** 湯医 'ga Yui'→'ga Yunoi' (thuật ngữ đã chốt).

### 2174 — ポーレット (thuật ngữ)

- **JP:** 「開票結果は、票数が少ないところから集計がくるの。\nつまり、御一夜の中心部以外の場所から」
- **TW:** 「開票結果是先從票數少的地區開始統計的。也就是從御一夜市中心以外的地區」
- **Cũ:** 「Kết quả kiểm phiếu sẽ được tổng hợp từ những nơi có ít phiếu bầu trước.\nNói cách khác, là từ những khu vực ngoài trung tâm Ohimitera.」
- **Mới:** 「Kết quả kiểm phiếu sẽ được tổng hợp từ những nơi có ít phiếu bầu trước.\nNói cách khác, là từ những khu vực ngoài trung tâm Ohitoyo.」
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo' (thuật ngữ đã chốt).

### 2185 — ハチロク (thuật ngữ)

- **JP:** 「双鉄様と日々姫と。ふたりだけの運転で湯医まで、\n\x%l22形;#00ffc040;ナイロ221%l;#;を引いた\x%l8620;#00ffc040;8620%l;#;を持っていく」
- **TW:** 「雙鐵少爺和日日姬，你們兩人要開著\x%l8620;#00ffc040;８６２０%l;#;把\x%lナイロ221;#00ffc040;Ｎａｉｒｏ２２１%l;#;拉到湯醫去」
- **Cũ:** 「Ngài Soutetsu và Hibiki. Hai người sẽ tự mình lái \x%l8620;#00ffc040;8620%l;#;\nkéo theo \x%l22形;#00ffc040;Nairo 221%l;#; đến tận ga Yui.」
- **Mới:** 「Ngài Soutetsu và Hibiki. Hai người sẽ tự mình lái \x%l8620;#00ffc040;8620%l;#;\nkéo theo \x%l22形;#00ffc040;Nairo 221%l;#; đến tận ga Yunoi.」
- **Lý do:** 湯医 'ga Yui'→'ga Yunoi' (thuật ngữ đã chốt).

### 2193 — 双鉄 (gasp, sweep)

- **JP:** 「っ！」
- **TW:** 「！」
- **Cũ:** 「!」
- **Mới:** 「Ư!」
- **Lý do:** Sweep lost-gasp-whole, đã kiểm chứng đúng JP — cả dòng chỉ là tiếng hít, VN chỉ còn dấu ! → 'Ư!'.

### 2194 — 日々姫 (gasp, sweep)

- **JP:** 「っ！！！！」
- **TW:** 「！！！！」
- **Cũ:** 「!!!!」
- **Mới:** 「Ư!!!!」
- **Lý do:** Sweep lost-gasp-whole, đã kiểm chứng đúng JP → 'Ư!!!!'.

### 2195 — 双鉄 (gasp, sweep)

- **JP:** 「っ！！？」
- **TW:** 「！！？」
- **Cũ:** 「!!?」
- **Mới:** 「Ư!!?」
- **Lý do:** Sweep lost-gasp-whole, đã kiểm chứng đúng JP → 'Ư!!?'.

### 2196 — 双鉄 (gasp, sweep)

- **JP:** 「っ！？」
- **TW:** 「！？」
- **Cũ:** 「!?」
- **Mới:** 「Ư!?」
- **Lý do:** Sweep lost-gasp-whole, đã kiểm chứng đúng JP → 'Ư!?'.

### 2609 — monologue (thuật ngữ)

- **JP:** そうして二人で――\n僕と日々姫と二人の力で、御一夜の夜を駆け抜けよう。
- **TW:** 就這樣憑藉兩個人——我和日日姬兩個人的力量，來穿越御一夜的黑夜吧。
- **Cũ:** Và rồi hai chúng tôi――\nbằng sức mạnh của cả hai, tôi và Hibiki sẽ cùng nhau băng qua màn đêm của Ohimitera.
- **Mới:** Và rồi hai chúng tôi――\nbằng sức mạnh của cả hai, tôi và Hibiki sẽ cùng nhau băng qua màn đêm của Ohitoyo.
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo' (thuật ngữ đã chốt).

### 2637 — monologue (thuật ngữ)

- **JP:** 御一夜の、すべての人達で――\nそれが、日々姫の描いた未来だ。
- **TW:** 御一夜所有的人面帶歡笑——這就是日日姬所描繪的未來。
- **Cũ:** Cùng với tất cả mọi người ở Ohimitera――\nĐó chính là tương lai mà Hibiki đã vẽ nên.
- **Mới:** Cùng với tất cả mọi người ở Ohitoyo――\nĐó chính là tương lai mà Hibiki đã vẽ nên.
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo' (thuật ngữ đã chốt).

### 2721 — monologue (sai nghĩa)

- **JP:** 唸りをあげる凪の気持ちは想像できる。\nここで一気に勝負をかけて、圧勝にまで運びたいのだ。
- **TW:** 我能理解凪為何不滿地嘟起了嘴。她是想一口氣賭一把然後順勢取得完勝。
- **Cũ:** Tôi có thể tưởng tượng được cảm xúc của Nagi khi rên rỉ như vậy.\nCon bé muốn dốc toàn lực quyết thắng ở đây, và giành chiến thắng áp đảo.
- **Mới:** Tôi có thể tưởng tượng được cảm xúc của Nagi khi gầm gừ như vậy.\nCon bé muốn dốc toàn lực quyết thắng ở đây, và giành chiến thắng áp đảo.
- **Lý do:** 唸り 'rên rỉ'→'gầm gừ' — 唸る là gầm gừ/càu nhàu vì bực bội, không phải rên rỉ (đau/khoái cảm); TW 不滿 (bất mãn) xác nhận sắc thái; tiền lệ toàn dự án lr_凪h2 1533 'khẽ gầm gừ một tiếng'.

### 2888 — monologue (thuật ngữ)

- **JP:** それから御一夜に入線し、おそらくそのまま、\nあの乗客を乗せて引くことともなるのだろう。
- **TW:** 然後就要駛入御一夜，到時候恐怕還會載上剛才那些乘客們吧。
- **Cũ:** Sau đó tiến vào ga Ohimitera, và có lẽ cứ thế,\nkéo theo những hành khách kia nữa.
- **Mới:** Sau đó tiến vào ga Ohitoyo, và có lẽ cứ thế,\nkéo theo những hành khách kia nữa.
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo' (thuật ngữ đã chốt).

### 2967 — monologue (gasp, sweep)

- **JP:** 天井が見える。\nと、いうことは僕は倒れて――っ！？
- **TW:** 能看見天花板。那也就是說我摔倒了——！？
- **Cũ:** Tôi có thể nhìn thấy trần nhà.\nNói cách khác là tôi đã ngã xuống――!?
- **Mới:** Tôi có thể nhìn thấy trần nhà.\nNói cách khác là tôi đã ngã xuống――Ư!?
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN mất っ cuối → thêm Ư.

### 3030 — monologue (thuật ngữ ×2)

- **JP:** ならば221の方は、旧\x%l帝鉄;#00ffc040;帝鉄%l;#;22000系改め御一夜22系の22に、\n単純に一号客車の1を付け足しただけのものか。
- **TW:** 那２２１，就只是單純在舊\x%l帝鉄;#00ffc040;帝國鐵路%l;#;２２０００型改御一夜２２型的“２２”上加了個表示一號客運車廂的“１”啊。
- **Cũ:** Vậy thì phần 221, chỉ đơn giản là số 22 của Dòng 22 Ohimitera được đổi từ Dòng 22000 của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ,\ncộng thêm số 1 của toa hành khách số 1 thôi sao.
- **Mới:** Vậy thì phần 221, chỉ đơn giản là số 22 của Dòng 22 Ohitoyo được đổi từ Dòng 22000 của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ,\ncộng thêm số 1 của toa hành khách số 1 thôi sao.
- **Lý do:** 御一夜 'Ohimitera'→'Ohitoyo'; 帝鉄 gloss 'Đường sắt Hoàng gia'→'Teitetsu' — lần thứ hai 帝鉄 xuất hiện trong file (lần đầu 1276 đã dùng dạng đầy đủ 'Đường sắt Đế quốc'), tiền lệ Common 10 (key 63 đầy đủ, 2436/1900 'Teitetsu').

### 3052 — monologue (gasp, sweep)

- **JP:** まずは僕から\x%l運転台;#00ffc040;運転台%l;#;へ――っ！？
- **TW:** 首先我走到\x%l運転台;#00ffc040;駕駛台%l;#;前——！？
- **Cũ:** Đầu tiên tôi sẽ lên \x%l運転台;#00ffc040;buồng lái%l;#;――!?
- **Mới:** Đầu tiên tôi sẽ lên \x%l運転台;#00ffc040;buồng lái%l;#;――Ư!?
- **Lý do:** Sweep lost-gasp-trailing, đã kiểm chứng đúng JP — VN mất っ cuối → thêm Ư.

## §4. Đại từ — đã rà, không sửa, 5 dòng không chắc (giữ nguyên, chờ quyết)

Đã rà toàn bộ 18 dòng Soutetsu tự xưng 'anh' + 1 dòng 'tôi' trong file theo dòng kề:

- 'anh' đúng (đối tượng Hibiki/Paulette): 1552, 1562, 1567 (Fukami), 1807, 1844, 1859, 1863, 1885, 1900, 1918 (Paulette), 1945, 2125, 2158, 1668.
- 1829 'anh' (tự nhủ khi chóng mặt, có Hibiki bên cạnh) — giữ.
- Không chắc — giữ nguyên bản cũ, KHÔNG quyết (cần Hieu/parent xem thêm ngữ cảnh cảnh):
  - **1841** 「わからんな」→ 'Anh cũng không biết nữa.' — 1840 Hachiroku hỏi 「と、おっしゃいますと？」 ('Ý ngài là sao ạ?'); nếu 1840 hỏi Soutetsu thì 1841 đáp Hachiroku → phải là 'tôi'; nếu 1840 hỏi Kisaki (chủ đề 次善の策 của Kisaki) thì 1841 là Soutetsu xen vào nói với nhóm → 'anh' đúng.
  - **1854** 「僕と日々姫は、昨日から恋人同士になった」→ 'Anh và Hibiki…' — nếu thông báo cho Kisaki (người mới đến, chưa biết) thì phải là 'Tôi'; nếu nói với Paulette/Hibiki thì 'anh' đúng.
  - **1856** 「あのときのことを思い出し……過去の僕が、今に怯えて震えているのか」→ 'Là tôi của quá khứ…' — cùng cụm cảnh với 1854: nếu đối tượng là Kisaki thì 'tôi' đúng; nếu cùng cảnh với 1857/1859/1863 (đều 'anh') thì phải là 'anh'.
  - **2102** 「協力依頼のときにはきちんと、『乗客を乗せずにやる』と説明したのだが――」→ 'Lúc nhờ giúp đỡ anh đã giải thích…' — đối tượng có thể là Kisaki (→'tôi', nối tiếp 2103 'mong được cô giúp đỡ') hoặc Paulette/Hachiroku (→'anh' nếu Paulette, 'tôi' nếu Hachiroku).
  - **2181** 「報告の必要があるとは思っていなかったが――」→ 'Anh không nghĩ là có cần thiết phải báo cáo đâu, nhưng――' — 2182 Hachiroku đáp lại trực tiếp (「それはそうでしょうが――」) nên đối tượng có thể là Hachiroku (→'tôi'); nhưng cũng có thể Soutetsu đang nói với Hibiki còn Hachiroku xen vào.
- Các cặp khác đã kiểm chứng đúng: Hibiki tự xưng 'em'; Fukami tự xưng 'mình' (1893); Nagi→Fukami 'bé' (1798, 1800); Fukami→Nagi 'bé Nagi' (1576, 1796); Nagi→Hibiki 'chị Hibiki' (1939); Reina tự xưng 'em', gọi Soutetsu 'ngài ấy' (1557); Paulette tự xưng 'chị' (1731); Hachiroku tự xưng 'em' nhất quán trong file (1803, 2154, 2180 'chúng em'); Soutetsu gọi Kisaki 'cô' (2018, 2103).
- 2183 義妹→'em gái nuôi' — GIỮ NGUYÊN (không tính sai): TW dùng 義妹, theo tiền lệ file 14 (TW 義弟/義兄 → 'nuôi' được chấp nhận).

## §5. Đã kiểm tra, giữ nguyên (không tính sai)

- 1712 むぅぅ～～っ → 「Ư ư~~」 (sweep already-rendered, đúng).
- 1717 「ぁっ」→ 'A' và 2084 「はうあっ！？」→ 'Hau á!?' — giữ: tiền lệ các file H (lr_ハチロクh1 1247/1249: ぁっ→'a') cho thấy っ đơn sau nguyên âm ngắn được hấp thụ vào âm đột ngột; sweep cũng không gắn cờ.
- 2104 けどっ → 'Nhưng mà' — っ cuối nhấn mạnh gắn với từ nội dung (けど), không phải gasp, không thêm Ư (tiền lệ ブロワーっ).
- 2176–2179 にぃにぃっ!!! → 'Anh hai!!!' — っ đã được diễn bằng dấu !!!, không thêm Ư.
- 2377 「息が、肚まで。肚の奥底まで落ちてくる」→ 'Hơi thở, nghẹn lại ở bụng. Rơi tuột xuống tận đáy bụng.' — diễn đạt tự do nhẹ ('nghẹn lại') nhưng ý chính (hơi thở rơi xuống đáy bụng) còn đủ, TW đồng thuận; giữ.
- 2698 トッ → 'Bịch' và 2799 ト、っと → 'lạch bạch chạy lon ton' — SFX ngẫu hứng theo ngữ cảnh, giữ.
- 1852 'hai em', 1609 'Chúng ta thắng rồi', 2129 'chúng ta' — dạng số nhiều, không thuộc quy tắc số ít, giữ.

## §6. Lượt soát 2 (second pass) + kiểm chứng cơ học

- Lượt soát 2: **24/24 tái kiểm chứng, 0 bỏ, 3 sửa** — 3 chỗ sửa đều do kiểm tra diff-sanity bắt được trong lúc soát: 1744/1876/2168 ban đầu làm rớt dấu 「」 và đổi dấu '.' thành '。' (đã sửa lại đúng bản cũ, chỉ đổi 'Yui'→'Yunoi').
- Số nguyên âm kiểm lại độc lập (không dựa vào JSON↔block): 1714 'Auuuu' = 5 (JP あうぅうう: 1+4), 1824 'Hauu' = 3 (JP はうう: 1+2), 1689 'Hauu' = 3 (JP はぅう: 1+2) — đều khớp công thức.
- Kiểm chứng cơ học (script): JSON 24 mục dạng chuẩn, khóa chuỗi; khối TOML [script] 24 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 24/24; diff-sanity từng fix chỉ đổi đúng chỗ cần đổi (đã kiểm bằng thay thế có mục tiêu từng cặp, 24/24 đạt).
- TOML block đã kiểm chứng parse — xem §7.

## §7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1276" = "「Toa \\x%l客車;#00ffc040;hành khách%l;#; số 1 Ohitoyo \\x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;,\\ntoàn bộ quá trình cải tạo \\x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」"
"1597" = "「Không đổi \\x%lタブレット;#00ffc040;máy tính bảng%l;#; sang \\x%l運転体;#00ffc040;thân vận hành%l;#; sao?」"
"1689" = "「Hauu~ Thích quá đi.\\nReina, vô cùng ghen tị luôn đó ạ~」"
"1714" = "「A――Cái đó――Auuuu~Ư!」"
"1729" = "「Vâng――sẽ mãi mãi――Ư!!」"
"1744" = "「Vâng, hẹn gặp ở ga Yunoi.」"
"1824" = "「Từ, từ đêm qua sao!? Từ đêm qua nghĩa là――Hauu~Ư!」"
"1876" = "「Kỳ vọng rằng lần tới chúng ta gặp nhau sẽ là ở ga Yunoi.」"
"1889" = "「Boku…… Hả? À ừm! Tiền bối Kisaki!?」"
"2166" = "「Nếu vậy, em cũng thế. Anh hai――Ư!」"
"2168" = "「Nếu vậy, hẹn gặp ở ga Yunoi.」"
"2174" = "「Kết quả kiểm phiếu sẽ được tổng hợp từ những nơi có ít phiếu bầu trước.\\nNói cách khác, là từ những khu vực ngoài trung tâm Ohitoyo.」"
"2185" = "「Ngài Soutetsu và Hibiki. Hai người sẽ tự mình lái \\x%l8620;#00ffc040;8620%l;#;\\nkéo theo \\x%l22形;#00ffc040;Nairo 221%l;#; đến tận ga Yunoi.」"
"2193" = "「Ư!」"
"2194" = "「Ư!!!!」"
"2195" = "「Ư!!?」"
"2196" = "「Ư!?」"
"2609" = "Và rồi hai chúng tôi――\\nbằng sức mạnh của cả hai, tôi và Hibiki sẽ cùng nhau băng qua màn đêm của Ohitoyo."
"2637" = "Cùng với tất cả mọi người ở Ohitoyo――\\nĐó chính là tương lai mà Hibiki đã vẽ nên."
"2721" = "Tôi có thể tưởng tượng được cảm xúc của Nagi khi gầm gừ như vậy.\\nCon bé muốn dốc toàn lực quyết thắng ở đây, và giành chiến thắng áp đảo."
"2888" = "Sau đó tiến vào ga Ohitoyo, và có lẽ cứ thế,\\nkéo theo những hành khách kia nữa."
"2967" = "Tôi có thể nhìn thấy trần nhà.\\nNói cách khác là tôi đã ngã xuống――Ư!?"
"3030" = "Vậy thì phần 221, chỉ đơn giản là số 22 của Dòng 22 Ohitoyo được đổi từ Dòng 22000 của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ,\\ncộng thêm số 1 của toa hành khách số 1 thôi sao."
"3052" = "Đầu tiên tôi sẽ lên \\x%l運転台;#00ffc040;buồng lái%l;#;――Ư!?"
```

## Kết bài

File 日々姫14_投開票: 476 dòng đã đọc hết, **24 dòng sai (5,0%)** — thuật ngữ 11, gasp 10, SFX 1, sai nghĩa 2. Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep っ-gasp: 10/11 entry áp nguyên sau kiểm chứng, 1 entry already-rendered giữ nguyên, 0 bỏ sót. Lượt soát 2: 24/24, 0 bỏ, 3 sửa. 5 dòng đại từ không chắc (1841, 1854, 1856, 2102, 2181) giữ nguyên chờ quyết — xem §4. Danh sách sửa đầy đủ: `audit-hibiki14-touhyou-wrong.json` (24 mục).
