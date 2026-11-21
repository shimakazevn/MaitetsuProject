# Kiểm tra bản dịch — グランドリライト05_れいな.txt.toml (route 04_Reina)

## Thông tin file

- **File:** `グランドリライト05_れいな.txt.toml` — route 04_Reina (Grand Rewrite 05 — Reina).
- **Đường dẫn TOML:** `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/04_Reina/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c805_#U308c#U3044#U306a.txt.toml`
- **md5 TOML:** `45868ca6f866aff3e8752cea7b8bb031` — bản sao trong `09_Grand/` có cùng md5 (2 bản, giống hệt nhau). UTF-8 BOM + CRLF.
- **CSV3 master:** `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv` — 472 dòng cho file này, 1 set duy nhất, khóa duy nhất, 0 VN trống.
- **Kiểm tra phẳng:** VN khớp phẳng TOML 472/472 sau khi chuẩn hoá `\n` của TOML-2 thành khoảng trắng (311 dòng chỉ khác ở chỗ đó, đã biết; 2371 cũng chỉ khác ở đó). TOML # JP khớp CSV3 JP 472/472.
- **Nhân vật (số dòng):** monologue 168, 双鉄 145, れいな 128, 赤井 13, ポーレット 12, 路子 6.
- **Nội dung:** Soutetsu cùng Reina và Paulette về Katakami (đường sắt mỏ, KiHa 07, toa xe trưởng tàu 車掌車), bàn kế hoạch bảo tàng lịch sử manga (đất Đường sắt Ohitoyo, bộ sưu tập manga Yunoi), gặp Akai (đền chủ/trưởng ga) và Gotou; Reina ngủ gật trên lưng Soutetsu, được cõng về. Không có H-scene.
- **`[characters]`:** 2485=Reina, 2551=Paulette, 2630=Soutetsu, 2960=Akai, 2973=Michiko — tên khớp đúng dàn nhân vật trong file (khóa là ID nhân vật, không đối chiếu được với khóa script). **`[character_subs]`:** 2805=Paulette, 2811=Reina, 3023=Soutetsu, 3057="???" — đúng. **`[selections]`** rỗng.

## Kết quả tổng

- **Đã đọc: 472/472 dòng. Sai: 53 (11,2%).**
- **Phân loại (53):** thuật ngữ 45 dòng (58 lượt sửa: Ohitoyo 14, Yunoi 14, Teitetsu 6, đền chủ 9, KiHa 8 — gồm 1 lượt ở dòng xưng hô 2373, Goto 5, chủ tàu 1, túi công tác 1; 10 dòng mang 2–3 lỗi); xưng hô 5 (Paulette→Soutetsu "anh Soutetsu" 4, Paulette tự xưng "em" 1); gasp っ 3 (1816, 1874, 1881).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**
- **Chi tiết các số 0:** lệch vị trí (không có VN nào thuộc dòng khác — mọi VN đều khớp JP/TW của chính khóa đó sau khi đọc từng dòng); chuỗi xoay 0 (không có cặp hoán đổi nào); nhiễm chéo 0 (không có VN nào thuộc file khác — đã kiểm tra các VN dài/khác thường, tất cả đều khớp JP trong file); mồ côi 0 (mọi dòng JP đều có VN, chỉ là sai); chưa dịch 0 (0 VN trống; 0 VN == TW; không còn ký tự っ thô trong VN); trùng khóa 0 (472 khóa duy nhất).
- **Nhóm VN trùng lặp (hợp lệ, không tính sai):** 「À——」1923/1924 (JP cả hai đều 「ああ――」, đúng).
- **Tag `%l`:** 0 lỗi (số lượng tag JP vs VN bằng nhau ở mọi dòng; không có tag VN tự thêm, không có tag thiếu dấu `;`). Tag ruby `[x,N]` phía JP được VN bỏ đúng (1702, 1976, 2070, 2078, 2166, 2193, 2201).
- **Đại từ:** xem § Đại từ dưới đây.

## Đối chiếu sweep (gasp っ)

Sweep `sweep-raw-gasp-wrong.json` có **1 mục** cho file này (cả 2 bản 04_Reina và 09_Grand đều trỏ cùng key 1881) — nhận **1/1**:
- 1881 (lost-gasp-whole): áp nguyên fix 「Ư!?」 — đúng (JP 「っ！？」, TW 「啊？！」).
Quét máy bổ sung toàn bộ dòng JP chứa っ: chỉ còn 4 đoạn ở vị trí gasp — 1814 (そのっ――, từ nội dung + gạch nối, giữ nguyên đúng), 1816 (ふぁっ → "Phà"), 1874 (はうっ → "HauƯ"), 1881 (sweep). Các っ còn lại đều là っ trong từ (っちゃ/って/ちょっと…), っ nhấn mạnh đã có dấu câu truyền tải, hoặc SFX đã diễn đạt (1870 んむっ→"Ưm", 1885 はうう～っ→"Hauu~!", 2379 ちゅっ→"Chụt"). Không còn gasp nào sót, không còn っ thô trong VN.

## Đại từ

- Soutetsu "anh" với Reina đúng toàn file (145 dòng thoại, 0 "tôi" sai); "tôi" chỉ trong độc thoại và khi nói với Akai ("cháu" với ông Akai, 1954/2017/2034/2224/2260 — đúng, Akai là bậc cha chú).
- Paulette→Soutetsu: 4 dòng dùng tên trần/"cậu" đã sửa thành "anh Soutetsu" theo khóa B4 (1730, 2140, 2220, 2373); 2218 "anh đã an tâm rồi đấy" đúng sẵn.
- Paulette tự xưng: "em" với Soutetsu (1899 đã sửa "chị"→"em", tiền lệ đã gộp P-file 1997 + reina01 1614); "tôi" ở 2140/2220/2306/2373 giữ nguyên (xem § Lưu ý).
- Reina gọi Paulette "chị Paulette" đúng (1949, 2314, 2343, 2350); Reina gọi Soutetsu "anh Soutetsu" đúng toàn file; Michiko gọi Soutetsu "Sou-chan"/"anh" đúng (1935, 1971, 2003).
- Akai gọi Soutetsu "cậu Soutetsu" (1957, 2036, 2136) giữ nguyên — cách gọi của bậc cha chú với hậu bối, nhất quán trong file.
- Độc thoại Soutetsu "tôi" đúng toàn file; 3052 "vết thương của mình" giữ nguyên (sở hữu cách, không phải đại từ chủ ngữ — ngoại lệ độc thoại không áp dụng ở đây nhưng "của mình" là cách nói sở hữu tự nhiên trong tiếng Việt).

## Chi tiết từng dòng sai (53 dòng)

- **1251 [monologue]** — JP 「……旧帝鉄製の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の幾体が、
これほどの笑顔で出自を語れるものだろうか。」 / TW 「……前帝國鐵路製造的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，竟然能面帶這樣的笑容道出自己的出身。」 / Cũ: 「……Trong số các \x%lレイルロオド;#00ffc040;Railord%l;#; do Đường sắt Hoàng gia cũ chế tạo,
liệu có mấy người có thể kể về xuất thân của mình với nụ cười tươi tắn như thế này chứ.」 → **「……Trong số các \x%lレイルロオド;#00ffc040;Railord%l;#; do Teitetsu cũ chế tạo,
liệu có mấy người có thể kể về xuất thân của mình với nụ cười tươi tắn như thế này chứ.」** (JP 旧帝鉄製 — thuật ngữ đã chốt 帝鉄="Teitetsu".)
- **1258 [monologue]** — JP 「……大廃線末期。帝鉄解体、まさに真っ最中の動乱。
そうした思い出話はやはり、宮司にとっても傷なのだろう。」 / TW 「……大廢線末期時，他親眼在動亂中見證了帝國鐵路的解體。回憶起這些事情，對他來說肯定無異於揭開過去的傷疤。」 / Cũ: 「……Thời kỳ cuối của cuộc Đại bãi bỏ. Sự giải thể của Đường sắt Hoàng gia, ngay giữa lúc hỗn loạn nhất.
Những câu chuyện hồi ức đó quả nhiên, đối với thầy cúng cũng là một vết thương lòng.」 → **「……Thời kỳ cuối của cuộc Đại bãi bỏ. Sự giải thể của Teitetsu, ngay giữa lúc hỗn loạn nhất.
Những câu chuyện hồi ức đó quả nhiên, đối với đền chủ cũng là một vết thương lòng.」** (JP 帝鉄解体→"Teitetsu"; 宮司→"đền chủ" (dòng này mang cả 2 lỗi).)
- **1693 [ポーレット]** — JP 「「湯医駅周辺の御一夜鉄道の土地を無償貸与して、
上物は湯医町の建築・管理に任せる、マンガの博物館」」 / TW 「「一座通過免費租借湯醫站附近御一夜鐵路的土地，建築物由鎮上來建造管理的有關漫畫的博物館」」 / Cũ: 「「Cho mượn miễn phí khu đất của Đường sắt Ohimitera xung quanh ga Yui,
phần công trình phía trên sẽ giao cho thị trấn Yui xây dựng và quản lý, một bảo tàng manga.」」 → **「「Cho mượn miễn phí khu đất của Đường sắt Ohitoyo xung quanh ga Yunoi,
phần công trình phía trên sẽ giao cho thị trấn Yunoi xây dựng và quản lý, một bảo tàng manga.」」** (御一夜鉄道→"Ohitoyo"; 湯医駅/湯医町→"Yunoi" (đã chốt).)
- **1697 [れいな]** — JP 「「また遊びにきますねぇ！　うふふぅ、もしよかったら、
御一夜鉄道にも、いつでも遊びにきてくださいねぇ！」」 / TW 「「下次玲奈還會來的！嘿嘿嘿，方便的話，你隨時都可以來御一夜鐵路玩哦！」」 / Cũ: 「「Lần sau em lại đến chơi nha~! Ufufu~, nếu được,
hãy đến Đường sắt Ohimitera chơi bất cứ lúc nào nhé~!」」 → **「「Lần sau em lại đến chơi nha~! Ufufu~, nếu được,
hãy đến Đường sắt Ohitoyo chơi bất cứ lúc nào nhé~!」」** (御一夜鉄道→"Ohitoyo".)
- **1699 [双鉄]** — JP 「「のみならず。差別化のため、湯医マンガ歴史館には、
『鉄道マンガ』専門の書架を設けてもらう」」 / TW 「「不僅如此，為了凸顯特色，在湯醫漫畫歷史館還要專設“鐵路漫畫”書架」」 / Cũ: 「「Không chỉ vậy. Để tạo sự khác biệt, Bảo tàng Lịch sử Manga Yui,
sẽ thiết lập một kệ sách chuyên về 『Manga đường sắt』.」」 → **「「Không chỉ vậy. Để tạo sự khác biệt, Bảo tàng Lịch sử Manga Yunoi,
sẽ thiết lập một kệ sách chuyên về 『Manga đường sắt』.」」** (湯医マンガ歴史館→"Yunoi".)
- **1730 [ポーレット]** — JP 「「双鉄くんこそ、『あとは頼む』です！
れいなのこと、よろしくお願いしちゃいますね！」」 / TW 「「你才是呢！剩下的就交給你了！玲奈接下來要跟你走呢！」」 / Cũ: 「「Soutetsu mới là người 『Phần còn lại nhờ cậu』 đấy!
Chuyện của Reina, nhờ cậu chăm sóc nhé!」」 → **「「Anh Soutetsu mới là người 『Phần còn lại nhờ anh』 đấy!
Chuyện của Reina, nhờ anh chăm sóc nhé!」」** (Paulette nói với Soutetsu (JP 双鉄くん) — khóa B4: Paulette→Soutetsu là "anh Soutetsu", không "cậu"/tên trần.)
- **1770 [双鉄]** — JP 「「作り物ではない、正和初期の街。
そこから生まれる蒸気で、熱で、息づき彩られる湯医線」」 / TW 「「創造一個真正的正和早年的小鎮，用那裡面的蒸汽、那裡面的熱量，去點綴湯醫線」」 / Cũ: 「「Không phải là đồ giả tạo, mà là khu phố thời kỳ đầu Showa.
Tuyến Yui được tiếp thêm sức sống và tô điểm bởi hơi nước, bởi nhiệt lượng sinh ra từ đó.」」 → **「「Không phải là đồ giả tạo, mà là khu phố thời kỳ đầu Showa.
Tuyến Yunoi được tiếp thêm sức sống và tô điểm bởi hơi nước, bởi nhiệt lượng sinh ra từ đó.」」** (湯医線→"Yunoi".)
- **1811 [赤井]** — JP 「「しかし、後東は"強盗"との異名を持つような男です。
路線だけでなく、なにもかもを買収し、売り払っていく」」 / TW 「「可是，後東這傢伙人稱“強盜”。不只是線路，他什麼都買，什麼都賣」」 / Cũ: 「「Tuy nhiên, Gotou là kẻ có biệt danh "Cường đạo".
Không chỉ tuyến đường, ông ta mua lại mọi thứ, rồi bán tống bán tháo.」」 → **「「Tuy nhiên, Goto là kẻ có biệt danh "Cường đạo".
Không chỉ tuyến đường, ông ta mua lại mọi thứ, rồi bán tống bán tháo.」」** (Họ 後東: chuẩn toàn dự án "Goto" 62 lần vs "Gotou" 6 lần; 仲国06/グランド06 dùng "Goto Kaita".)
- **1816 [れいな]** — JP 「「ふぁっ」」 / TW 「「呼」」 / Cũ: 「「Fua」」 → **「「Phà」」** (JP ふぁっ — quy tắc fa/fu đã chốt ふぁ→"phà"; tiền lệ 3 file (Fukami epilogue 2174/2176, 日々姫07 1759, 凪ふかみ01 1589) đều "Phà".)
- **1860 [双鉄]** — JP 「「ああ、キハ07自体を\x%l貨車;#00ffc040;貨車%l;#;のように使うのか。
そんな運用があるほどに――栄えていたのだな」」 / TW 「「哦，就是把Ｋｉｈａ０７本身當成\x%l貨車;#00ffc040;貨運車廂%l;#;使用吧。那時候繁榮到要把列車用來做這種事情啊」」 / Cũ: 「「À, dùng chính Kiha 07 như một \x%l貨車;#00ffc040;toa chở hàng%l;#; sao.
Đến mức có cả cách vận hành như vậy——chắc hẳn nơi đó từng rất phồn vinh nhỉ.」」 → **「「À, dùng chính KiHa 07 như một \x%l貨車;#00ffc040;toa chở hàng%l;#; sao.
Đến mức có cả cách vận hành như vậy——chắc hẳn nơi đó từng rất phồn vinh nhỉ.」」** (JP キハ07 — chính tả đã chốt "KiHa" (cách viết chính thức của JR); toàn dự án KiHa 145 vs Kiha 39.)
- **1874 [れいな]** — JP 「「はうっ」」 / TW 「「啊嗚」」 / Cũ: 「「Hau」」 → **「「HauƯ」」** (JP はうっ (từ âm thanh, cuối dòng tuyệt đối, không dấu câu) — っ mất hẳn nên thêm Ư theo quy tắc gasp đã chốt (はうっ là ví dụ nêu tên trong brief); tiền lệ 仲国01 1776/1803 "HaƯ".)
- **1877 [赤井]** — JP 「「ああいやいや、これは失言でした。
戦友――ですからね、後東は。つい口が滑りました」」 / TW 「「啊，抱歉抱歉，我說錯了。後東是我的戰友。一不小心說漏嘴了」」 / Cũ: 「「A, không không, tôi lỡ lời rồi.
Gotou, là chiến hữu——của tôi mà. Tôi lỡ buột miệng thôi.」」 → **「「A, không không, tôi lỡ lời rồi.
Goto, là chiến hữu——của tôi mà. Tôi lỡ buột miệng thôi.」」** (Họ 後東: chuẩn "Goto" (xem 1811).)
- **1881 [双鉄]** — JP 「「っ！？」」 / TW 「「啊？！」」 / Cũ: 「「!?」」 → **「「Ư!?」」** (Sweep lost-gasp-whole: JP 「っ！？」 TW 「啊？！」 — áp nguyên fix 「Ư!?」.)
- **1899 [ポーレット]** — JP 「「うん。最近は読んでる時間もあんまりないし、
読みたくなったら、歴史館で読ませてもらえばいいし」」 / TW 「「嗯，最近我也沒什麼時間讀書，哪天想讀了，去歷史館就行了」」 / Cũ: 「「Ừm. Gần đây chị cũng không có nhiều thời gian để đọc,
nếu muốn đọc, đến bảo tàng đọc ké là được rồi.」」 → **「「Ừm. Gần đây em cũng không có nhiều thời gian để đọc,
nếu muốn đọc, đến bảo tàng đọc ké là được rồi.」」** (Paulette nói với Soutetsu (1901 Soutetsu đáp "rất sẵn lòng") — Paulette tự xưng "em" với Soutetsu; tiền lệ đã gộp: P-file 1997 "chị"→"em", reina01 1614.)
- **1957 [赤井]** — JP 「「もしも、後東と連絡を取りたいと思うのなら――」」 / TW 「「如果你想聯繫後東……」」 / Cũ: 「「Nếu như, cậu muốn liên lạc với Gotou——」」 → **「「Nếu như, cậu muốn liên lạc với Goto——」」** (Họ 後東: chuẩn "Goto" (xem 1811).)
- **1959 [双鉄]** — JP 「「例えば、キハ07の仕様を一番最初の状態に戻して、
改造の過負荷を減少させるなどのことは」」 / TW 「「如果將Ｋｉｈａ０７改回最原本的狀態，是否能減輕改造帶來的負荷？」」 / Cũ: 「「Ví dụ như, khôi phục lại thông số kỹ thuật của Kiha 07 về trạng thái ban đầu,
để giảm thiểu sự quá tải do cải tạo thì sao?」」 → **「「Ví dụ như, khôi phục lại thông số kỹ thuật của KiHa 07 về trạng thái ban đầu,
để giảm thiểu sự quá tải do cải tạo thì sao?」」** (JP キハ07 — "KiHa" (xem 1860).)
- **1972 [双鉄]** — JP 「「御一夜でれいなの笑顔が輝いているのと同じように。
このスキットルが、また輝いたのとおんなじように」」 / TW 「「就好像你來到御一夜之後又綻放出了笑容一樣，就好像這扁酒壺又能反射出耀眼的光芒一樣」」 / Cũ: 「「Cũng giống như nụ cười của Reina đang tỏa sáng ở Ohimitera vậy.
Cũng giống như chiếc bình tông này, lại tỏa sáng một lần nữa.」」 → **「「Cũng giống như nụ cười của Reina đang tỏa sáng ở Ohitoyo vậy.
Cũng giống như chiếc bình tông này, lại tỏa sáng một lần nữa.」」** (御一夜→"Ohitoyo".)
- **1976 [れいな]** — JP 「「キハ[れいなな,1]07のお客さんを乗せるスペースに、小包とか、
お手紙とかを乗せることですよぉ」」 / TW 「「就是在Ｋｉｈａ０７的載客空間裝上郵包或者信件」」 / Cũ: 「「Là dùng không gian chở khách của Kiha 07, để chở bưu kiện,
hay thư từ đó ạ~」」 → **「「Là dùng không gian chở khách của KiHa 07, để chở bưu kiện,
hay thư từ đó ạ~」」** (JP キハ07 — "KiHa" (xem 1860).)
- **1997 [双鉄]** — JP 「「それを学ぶことは、御一夜市の、御一夜鉄道の
滅びを回避する、助けになるかもと思ってな」」 / TW 「「從這些事情裡面，我們可以學到如何規避御一夜市和御一夜鐵路的毀滅」」 / Cũ: 「「Anh nghĩ việc tìm hiểu điều đó, có thể sẽ giúp ích
trong việc tránh cho thành phố Ohimitera, và Đường sắt Ohimitera khỏi sự diệt vong.」」 → **「「Anh nghĩ việc tìm hiểu điều đó, có thể sẽ giúp ích
trong việc tránh cho thành phố Ohitoyo, và Đường sắt Ohitoyo khỏi sự diệt vong.」」** (御一夜市/御一夜鉄道→"Ohitoyo" (cả 2 chỗ).)
- **2017 [双鉄]** — JP 「「ご助言ありがとうございます。後東様へのご連絡を
お願いするかどうか等、稀咲と[あね,1]義姉に相談しようかと」」 / TW 「「感謝您的建議。我準備回去和稀咲還有姐姐談一談是否聯繫後東先生」」 / Cũ: 「「Cảm ơn ông đã khuyên bảo. Về việc có nhờ ông liên lạc với ông Gotou hay không,
cháu định sẽ bàn bạc lại với Kisaki và chị gái.」」 → **「「Cảm ơn ông đã khuyên bảo. Về việc có nhờ ông liên lạc với ông Goto hay không,
cháu định sẽ bàn bạc lại với Kisaki và chị gái.」」** (Họ 後東: chuẩn "Goto" (xem 1811).)
- **2032 [双鉄]** — JP 「「術仙という街をテーマパークにしたいのだがな、
その街自体が、御一夜に昔から暮らす人々の傷なのだ」」 / TW 「「我想把一個叫術仙的小鎮改造成主題公園，但那小鎮對一直住在御一夜的人來說是個傷痕」」 / Cũ: 「「Anh muốn biến khu phố tên Jussen thành công viên chủ đề,
nhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohimitera từ ngày xưa.」」 → **「「Anh muốn biến khu phố tên Jussen thành công viên chủ đề,
nhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohitoyo từ ngày xưa.」」** (御一夜→"Ohitoyo".)
- **2070 [れいな]** — JP 「「そうですねぇ。本当に大事にしてもらいましたぁ。
[れいななえす,4]キハ07sになる前から、内装はずーっと修理なしです」」 / TW 「「是呀。他們待客車真的很好。在成為Ｋｉｈａ０７Ｓ之前，車廂的內部裝飾完全沒有維修過」」 / Cũ: 「「Đúng vậy ạ~. Mọi người thật sự rất trân trọng em.
Từ trước khi trở thành Kiha 07S, nội thất bên trong chưa từng phải sửa chữa lần nào đâu ạ~」」 → **「「Đúng vậy ạ~. Mọi người thật sự rất trân trọng em.
Từ trước khi trở thành KiHa 07S, nội thất bên trong chưa từng phải sửa chữa lần nào đâu ạ~」」** (JP キハ07s — "KiHa 07S" (xem 1860).)
- **2106 [双鉄]** — JP 「「『[たいと,1]汰斗さんのお話を』だ。
帝鉄がいかに衰退し、滅びにいたったかという話――」」 / TW 「「是說跟汰斗老爺，打聽帝國鐵路是如何衰敗、滅亡的——」」 / Cũ: 「「『Câu chuyện của ông Taito』.
Câu chuyện về việc Đường sắt Hoàng gia đã suy tàn và đi đến diệt vong như thế nào——」」 → **「「『Câu chuyện của ông Taito』.
Câu chuyện về việc Teitetsu đã suy tàn và đi đến diệt vong như thế nào——」」** (JP 帝鉄 — thuật ngữ đã chốt "Teitetsu".)
- **2116 [ポーレット]** — JP 「「湯医出身の高名な先生の全盛期が、ちょうどの時期で。
だから湯医にはその頃のマンガの蔵書がとても多いの」」 / TW 「「有個湯醫的知名漫畫家剛好在那段時間特別出名，所以湯醫有許多那個時候的漫畫藏書」」 / Cũ: 「「Thời kỳ hoàng kim của một tác giả nổi tiếng xuất thân từ Yui, đúng vào khoảng thời gian đó.
Vì vậy, ở Yui có rất nhiều bộ sưu tập manga thời kỳ đó.」」 → **「「Thời kỳ hoàng kim của một tác giả nổi tiếng xuất thân từ Yunoi, đúng vào khoảng thời gian đó.
Vì vậy, ở Yunoi có rất nhiều bộ sưu tập manga thời kỳ đó.」」** (湯医→"Yunoi" (cả 2 chỗ).)
- **2136 [赤井]** — JP 「「双鉄君のことは汰斗さんからも頼まれておりますし、
御一夜市に関わることであれば、我がことですから」」 / TW 「「汰斗老先生向我拜託過你的事情，何況事關御一夜市，自然也是我分內之事」」 / Cũ: 「「Chuyện của cậu Soutetsu tôi cũng đã được ông Taito gửi gắm,
hơn nữa, những chuyện liên quan đến thành phố Ohimitera, cũng là chuyện của tôi mà.」」 → **「「Chuyện của cậu Soutetsu tôi cũng đã được ông Taito gửi gắm,
hơn nữa, những chuyện liên quan đến thành phố Ohitoyo, cũng là chuyện của tôi mà.」」** (御一夜市→"Ohitoyo".)
- **2140 [ポーレット]** — JP 「「いえいえ、すまなくなんてないです。
むしろ、双鉄くんにはもう少し長話して欲しいかなって」」 / TW 「「沒事沒事，沒什麼好抱歉的。我甚至還想跟你多聊聊呢」」 / Cũ: 「「Không không, không có gì phải xin lỗi đâu.
Ngược lại, tôi còn muốn Soutetsu nói chuyện lâu hơn một chút cơ.」」 → **「「Không không, không có gì phải xin lỗi đâu.
Ngược lại, tôi còn muốn anh Soutetsu nói chuyện lâu hơn một chút cơ.」」** (Paulette nói với Soutetsu (JP 双鉄くん) — khóa B4 "anh Soutetsu".)
- **2178 [れいな]** — JP 「「れいな、帝鉄さんのことはわからないけど、
[カタカミ,1]硬上鉱山鉄道のことならわかりますよぉ」」 / TW 「「玲奈不了解帝國鐵路，但是知道片上礦山鐵路的事情」」 / Cũ: 「「Reina, không biết về Đường sắt Hoàng gia,
nhưng nếu là Đường sắt mỏ Katakami thì em biết nha~」」 → **「「Reina, không biết về Teitetsu,
nhưng nếu là Đường sắt mỏ Katakami thì em biết nha~」」** (JP 帝鉄さん — "Teitetsu".)
- **2207 [れいな]** — JP 「「れいなの場合は、キハ07の車内をはんぶんこに
わけて、お客さんと荷物、両方はこんじゃったんです」」 / TW 「「玲奈當時是把Ｋｉｈａ０７的車廂分成兩半，同時載客加運貨的」」 / Cũ: 「「Trong trường hợp của Reina, là chia đôi không gian bên trong Kiha 07,
rồi chở cả khách lẫn hành lý luôn đó ạ~」」 → **「「Trong trường hợp của Reina, là chia đôi không gian bên trong KiHa 07,
rồi chở cả khách lẫn hành lý luôn đó ạ~」」** (JP キハ07 — "KiHa" (xem 1860).)
- **2211 [れいな]** — JP 「「れいな、わかりましたぁ！　湯医のマンガ歴史館も、
『レイル・ロマネスク湯医線』の、ひとつなんですねぇ」」 / TW 「「玲奈知道了！湯醫的漫畫歷史館，也是“幻想鐵路·湯醫線”的組成部分吧」」 / Cũ: 「「Reina, hiểu rồi ạ~! Bảo tàng Lịch sử Manga Yui cũng là,
một phần của 『Rail Romanesque tuyến Yui』 nhỉ~」」 → **「「Reina, hiểu rồi ạ~! Bảo tàng Lịch sử Manga Yunoi cũng là,
một phần của 『Rail Romanesque tuyến Yunoi』 nhỉ~」」** (湯医→"Yunoi" (cả 2 chỗ, kể cả trong tên 『レイル・ロマネスク湯医線』).)
- **2220 [ポーレット]** — JP 「「もちろん！　ちょうど、わたしも今双鉄くんとれいなに、
そうしてほしいってお願いしようと思ってたとこなの」」 / TW 「「當然可以！我正準備請你們兩個繼續聊呢」」 / Cũ: 「「Tất nhiên rồi! Vừa hay, tôi cũng đang định nhờ Soutetsu và Reina,
làm như vậy đấy.」」 → **「「Tất nhiên rồi! Vừa hay, tôi cũng đang định nhờ anh Soutetsu và Reina,
làm như vậy đấy.」」** (Paulette nói với Soutetsu (JP 双鉄くん) — khóa B4 "anh Soutetsu".)
- **2253 [双鉄]** — JP 「「なにせ土地は御一夜鉄道のものだ。
駅から歩いて三分せずに入館できることになる」」 / TW 「「而且土地是屬於御一夜鐵路的，只要從車站步行三分鐘不到就能抵達」」 / Cũ: 「「Dù sao thì đất cũng là của Đường sắt Ohimitera.
Đi bộ từ ga chưa tới ba phút là vào được bảo tàng rồi.」」 → **「「Dù sao thì đất cũng là của Đường sắt Ohitoyo.
Đi bộ từ ga chưa tới ba phút là vào được bảo tàng rồi.」」** (御一夜鉄道→"Ohitoyo".)
- **2259 [双鉄]** — JP 「「それも実に楽しそうだな。
だがしかし。同じ同僚なら、御一夜鉄道の方がいい」」 / TW 「「聽起來也挺有意思的。不過，我們還是在御一夜鐵路當同事更好」」 / Cũ: 「「Chuyện đó nghe cũng thú vị thật đấy.
Nhưng mà. Nếu là đồng nghiệp, thì ở Đường sắt Ohimitera vẫn tốt hơn.」」 → **「「Chuyện đó nghe cũng thú vị thật đấy.
Nhưng mà. Nếu là đồng nghiệp, thì ở Đường sắt Ohitoyo vẫn tốt hơn.」」** (御一夜鉄道→"Ohitoyo".)
- **2281 [れいな]** — JP 「「買収と延伸は、なんていっても、
やっぱり帝鉄さんですからぁ」」 / TW 「「負責購買與延長的，基本上都是帝國鐵路」」 / Cũ: 「「Mua lại và mở rộng, dù nói gì đi nữa,
thì vẫn là chuyện của Đường sắt Hoàng gia mà~」」 → **「「Mua lại và mở rộng, dù nói gì đi nữa,
thì vẫn là chuyện của Teitetsu mà~」」** (JP 帝鉄さん — "Teitetsu".)
- **2313 [れいな]** — JP 「「それならそれなら、湯医線にのったひとに、
鉄道のこと、もっと知って好きになってもらえますねぇ」」 / TW 「「這樣的話就可以讓乘坐湯醫線的人更了解、更喜歡鐵路了吧」」 / Cũ: 「「Nếu vậy nếu vậy, những người đi tuyến Yui,
sẽ biết thêm và thích đường sắt hơn nhỉ~」」 → **「「Nếu vậy nếu vậy, những người đi tuyến Yunoi,
sẽ biết thêm và thích đường sắt hơn nhỉ~」」** (湯医線→"Yunoi".)
- **2336 [双鉄]** — JP 「「ならば、御一夜に戻ってからもおしゃべりしよう」」 / TW 「「那我們回御一夜再聊吧」」 / Cũ: 「「Vậy thì, sau khi về Ohimitera chúng ta lại nói chuyện tiếp nhé.」」 → **「「Vậy thì, sau khi về Ohitoyo chúng ta lại nói chuyện tiếp nhé.」」** (御一夜→"Ohitoyo".)
- **2371 [れいな]** — JP 「「そうてつさん、湯医の町長さんと、　
なんのおはなしをしてきたんですかぁ？」」 / TW 「「雙鐵先生，你和湯醫的鎮長說了什麼？」」 / Cũ: 「「Anh Soutetsu, với Trưởng thị trấn Yui, 
đã nói chuyện gì vậy ạ~?」」 → **「「Anh Soutetsu, với Trưởng thị trấn Yunoi, 
đã nói chuyện gì vậy ạ~?」」** (湯医の町長→"Yunoi".)
- **2373 [ポーレット]** — JP 「「双鉄くん。わたし、キハ07sを\x%l検修庫;#00ffc040;検修庫%l;#;に戻しますから」」 / TW 「「雙鐵君，我去把Ｋｉｈａ０７Ｓ開回\x%l検修庫;#00ffc040;檢修庫%l;#;」」 / Cũ: 「「Soutetsu. Tôi, sẽ đưa Kiha 07S về \x%l検修庫;#00ffc040;xưởng bảo dưỡng%l;#; đây.」」 → **「「Anh Soutetsu. Tôi, sẽ đưa KiHa 07S về \x%l検修庫;#00ffc040;xưởng bảo dưỡng%l;#; đây.」」** (Paulette nói với Soutetsu (JP 双鉄くん) — khóa B4 "anh Soutetsu"; JP キハ07s — "KiHa 07S".)
- **2599 [monologue]** — JP 「が、御一夜に古くから住まう人たちにとっては、
僕は所詮は、外来者だ。」 / TW 「但是，對於長久居住在御一夜的人來說，歸根結底，我只是一個外人。」 / Cũ: 「Nhưng, đối với những người đã sống ở Ohimitera từ lâu,
tôi rốt cuộc, cũng chỉ là một kẻ ngoại lai.」 → **「Nhưng, đối với những người đã sống ở Ohitoyo từ lâu,
tôi rốt cuộc, cũng chỉ là một kẻ ngoại lai.」** (御一夜→"Ohitoyo".)
- **2605 [monologue]** — JP 「廃鉱、閉山。大廃線がとどめとなっての、鉄道廃止。
そうして、誇りであった自社発注機、キハ07　2の売却。」 / TW 「停礦，封山。再加上最終因大廢線而起的鐵路廢棄，就這樣，他們賣掉了曾經引以為傲的訂購機車Ｋｉｈａ０７　２。」 / Cũ: 「Mỏ bị bỏ hoang, đóng cửa. Cuộc Đại bãi bỏ các tuyến đường sắt như một đòn kết liễu, dẫn đến việc bãi bỏ tuyến đường sắt.
Và rồi, họ phải bán đi chiếc Kiha 07-2, cỗ máy đặt hàng riêng từng là niềm tự hào của họ.」 → **「Mỏ bị bỏ hoang, đóng cửa. Cuộc Đại bãi bỏ các tuyến đường sắt như một đòn kết liễu, dẫn đến việc bãi bỏ tuyến đường sắt.
Và rồi, họ phải bán đi chiếc KiHa 07-2, cỗ máy đặt hàng riêng từng là niềm tự hào của họ.」** (JP キハ07 2 — "KiHa 07-2" (xem 1860).)
- **2634 [monologue]** — JP 「採炭という技術の継承――それは明確な売りになる。
“レイル・ロマネスク湯医線"には、炭鉱が生きていると。」 / TW 「只要“幻想鐵路·湯醫線”擁有還在運轉的煤礦，那麼繼承採煤技術，就能成為一大賣點。」 / Cũ: 「Sự kế thừa kỹ thuật khai thác than——đó sẽ là một điểm bán hàng rõ ràng.
Rằng mỏ than vẫn đang sống trong "Rail Romanesque tuyến Yui".」 → **「Sự kế thừa kỹ thuật khai thác than——đó sẽ là một điểm bán hàng rõ ràng.
Rằng mỏ than vẫn đang sống trong "Rail Romanesque tuyến Yunoi".」** (湯医線→"Yunoi".)
- **2653 [monologue]** — JP 「今の御一夜鉄道で、れいなにそこまで性能を求める
運用を求めることはありえんだろうし――」 / TW 「在現在的御一夜鐵路，玲奈並不需要那麼強的性能……」 / Cũ: 「Ở Đường sắt Ohimitera hiện tại, việc yêu cầu Reina
phải đạt hiệu suất đến mức đó là điều không thể nào——」 → **「Ở Đường sắt Ohitoyo hiện tại, việc yêu cầu Reina
phải đạt hiệu suất đến mức đó là điều không thể nào——」** (御一夜鉄道→"Ohitoyo".)
- **2676 [monologue]** — JP 「後東槐多。路線用地買収について、
赤井宮司が有しているという、唯一の"心当たり"。」 / TW 「後東慶太，是在購買延伸線路用地方面，赤井宮司能想到的唯一人選。」 / Cũ: 「Gotou Kaita. Về việc mua lại đất đai cho tuyến đường,
là "manh mối" duy nhất mà thầy cúng Akai có được.」 → **「Goto Kaita. Về việc mua lại đất đai cho tuyến đường,
là "manh mối" duy nhất mà đền chủ Akai có được.」** (後東槐多 đọc かいた (furigana ở グランド06 2571; TW 慶太 sai — JP thắng); 宮司→"đền chủ".)
- **2745 [monologue]** — JP 「あれは、僕と赤井宮司とが気兼ねなく話をできるよう、
気を使っての発言だったと思っていたが――」 / TW 「我本以為這是她為了讓我和赤井宮司能敞開了聊……」 / Cũ: 「Tôi cứ tưởng đó là câu nói tinh ý của em ấy,
để tôi và thầy cúng Akai có thể nói chuyện thoải mái mà không phải e dè——」 → **「Tôi cứ tưởng đó là câu nói tinh ý của em ấy,
để tôi và đền chủ Akai có thể nói chuyện thoải mái mà không phải e dè——」** (赤井宮司→"đền chủ Akai".)
- **2754 [monologue]** — JP 「まさしく、そこは盲点だった。
赤井宮司は、元帝鉄。」 / TW 「我竟然漏了這一點。赤井宮司是前帝國鐵路員工。」 / Cũ: 「Quả thực, đó là một điểm mù.
Thầy cúng Akai, là cựu nhân viên Đường sắt Hoàng gia.」 → **「Quả thực, đó là một điểm mù.
Đền chủ Akai, là cựu nhân viên Teitetsu.」** (赤井宮司→"đền chủ Akai"; 元帝鉄→"cựu nhân viên Teitetsu".)
- **2790 [monologue]** — JP 「それと同時に、『レイル・ロマネスク湯医線』
湯医線の統一イメージ構造も、発表するのは最善だろう。」 / TW 「最好在發布這件事的同時，也一併發表“幻想鐵路·湯醫線”的整體構想。」 / Cũ: 「Đồng thời, việc công bố 『Rail Romanesque tuyến Yui』
cấu trúc hình ảnh thống nhất của tuyến Yui, có lẽ là tốt nhất.」 → **「Đồng thời, việc công bố 『Rail Romanesque tuyến Yunoi』
cấu trúc hình ảnh thống nhất của tuyến Yunoi, có lẽ là tốt nhất.」** (湯医線→"Yunoi" (cả 2 chỗ: tên 『レイル・ロマネスク湯医線』 và "cấu trúc hình ảnh thống nhất của tuyến Yui").)
- **2799 [monologue]** — JP 「慎重極まる赤井宮司が、これほど強い言葉を使う。
"無視はされない"と断言する。」 / TW 「極其慎重的赤井宮司使用了非常堅定的措辭。他說那個人不可能不搭理我。」 / Cũ: 「Một người cực kỳ thận trọng như thầy cúng Akai, lại dùng những từ ngữ mạnh mẽ đến vậy.
Khẳng định chắc nịch rằng "sẽ không bị phớt lờ".」 → **「Một người cực kỳ thận trọng như đền chủ Akai, lại dùng những từ ngữ mạnh mẽ đến vậy.
Khẳng định chắc nịch rằng "sẽ không bị phớt lờ".」** (赤井宮司→"đền chủ Akai".)
- **2814 [monologue]** — JP 「れいなは赤井宮司――いや、赤井\x%l運転士;#00ffc040;運転士%l;#;の、
運転鞄に、ずっと話しかけ続けていたのか。」 / TW 「玲奈一直在跟赤井宮司——不，赤井\x%l運転士;#00ffc040;駕駛員%l;#;的駕駛包說話。」 / Cũ: 「Reina đã liên tục nói chuyện với thầy cúng Akai——không, với túi xách của \x%l運転士;#00ffc040;người lái tàu%l;#; Akai sao.」 → **「Reina đã liên tục nói chuyện với đền chủ Akai——không, với túi công tác của \x%l運転士;#00ffc040;người lái tàu%l;#; Akai sao.」** (赤井宮司→"đền chủ Akai"; JP 運転鞄→"túi công tác" (đã chốt 20/11, không phải "túi xách").)
- **2836 [monologue]** — JP 「働くことが大好きで、御一夜鉄道が大好きで、
それでも休みは嬉しいものかと、微笑ましくなる。」 / TW 「玲奈熱愛工作，熱愛御一夜鐵路，但是得到休息時間的她還是由衷地高興了起來。」 / Cũ: 「Rất thích làm việc, rất thích Đường sắt Ohimitera,
thế mà được nghỉ vẫn thấy vui sao, tôi bất giác mỉm cười.」 → **「Rất thích làm việc, rất thích Đường sắt Ohitoyo,
thế mà được nghỉ vẫn thấy vui sao, tôi bất giác mỉm cười.」** (御一夜鉄道→"Ohitoyo".)
- **2964 [monologue]** — JP 「笑う。赤井宮司――いや、赤井さんが。
ごく穏やかに、あたたかに――何故か、父さんを思い出す。」 / TW 「赤井宮司——不，赤井先生笑了。他笑得很溫和，很溫暖。不知為何，這讓我想起了父親。」 / Cũ: 「Cười. Thầy cúng Akai——không, chú Akai.
Một nụ cười vô cùng điềm đạm, ấm áp——Không hiểu sao, lại làm tôi nhớ đến bố.」 → **「Cười. Đền chủ Akai——không, chú Akai.
Một nụ cười vô cùng điềm đạm, ấm áp——Không hiểu sao, lại làm tôi nhớ đến bố.」** (赤井宮司→"đền chủ Akai".)
- **2969 [monologue]** — JP 「赤井宮司は穏やかな笑顔を浮かべようとし――
けれども、上手にできていない。」 / TW 「赤井宮司想露出溫和的笑容，但表現得還是有些僵硬。」 / Cũ: 「Thầy cúng Akai cố nở một nụ cười điềm đạm——
Nhưng mà, ông ấy làm không được tự nhiên cho lắm.」 → **「Đền chủ Akai cố nở một nụ cười điềm đạm——
Nhưng mà, ông ấy làm không được tự nhiên cho lắm.」** (赤井宮司→"đền chủ Akai".)
- **3001 [monologue]** — JP 「赤井宮司らしくない――
けれども極めて、赤井さんらしい言葉だと感じる。」 / TW 「這詞聽起來很不像是赤井宮司會說的話，但卻讓我覺得很有他的風格。」 / Cũ: 「Không giống thầy cúng Akai chút nào——
Nhưng tôi lại cảm thấy, đó là những từ ngữ cực kỳ giống với chú Akai.」 → **「Không giống đền chủ Akai chút nào——
Nhưng tôi lại cảm thấy, đó là những từ ngữ cực kỳ giống với chú Akai.」** (赤井宮司→"đền chủ Akai".)
- **3010 [monologue]** — JP 「『まいてつ』なる人種は、僕のような特殊例を除き、
まず間違いなくポーレットの同類。マニアだろう。」 / TW 「除了我這樣的特殊個例，“掌車人”肯定都是波萊特的同類，也就是鐵路迷。」 / Cũ: 「Những người thuộc nhóm 『Maitetsu』, ngoại trừ trường hợp đặc biệt như tôi,
thì chắc chắn là đồng loại với Paulette. Những người đam mê.」 → **「Những người thuộc nhóm 『chủ tàu』, ngoại trừ trường hợp đặc biệt như tôi,
thì chắc chắn là đồng loại với Paulette. Những người đam mê.」** (JP 『まいてつ』なる人種 — thuật ngữ đã chốt まいてつ="chủ tàu".)
- **3021 [monologue]** — JP 「御一夜鉄道担当者としての湯医町長との会談を終え、
キハ07sに乗車するとき、軽く頷いてみせただけでも。」 / TW 「雖說我只是以御一夜鐵路負責人的身份結束了與湯醫鎮長的會議，在登上Ｋｉｈａ０７Ｓ地時候向她輕輕點了點頭。」 / Cũ: 「Dù chỉ là một cái gật đầu nhẹ khi lên tàu Kiha 07S,
sau khi kết thúc cuộc đàm phán với tư cách là người đại diện Đường sắt Ohimitera với Trưởng thị trấn Yui.」 → **「Dù chỉ là một cái gật đầu nhẹ khi lên tàu KiHa 07S,
sau khi kết thúc cuộc đàm phán với tư cách là người đại diện Đường sắt Ohitoyo với Trưởng thị trấn Yunoi.」** (御一夜鉄道→"Ohitoyo"; 湯医町長→"Yunoi"; JP キハ07s — "KiHa 07S".)

## Lưu ý (giữ nguyên có lý do + chờ Hieu)

- **2156 KHÔNG SỬA, chờ Hieu:** Soutetsu nói với Paulette "phần còn lại nhờ cô nhé" — câu hỏi "cô vs em" cho Paulette vẫn đang chờ Hieu chốt toàn dự án (ROUTE-AUDIT ghi nhận nhiều file nghiêng hai hướng; không tự quyết).
- **Paulette "tôi" giữ nguyên (2140, 2220, 2306, 2373):** Paulette tự xưng "tôi" khi nói với Soutetsu — đây là lối xưng trang trọng của cô (98 lần toàn dự án); tiền lệ đã gộp chỉ sửa "chị"→"em" (mâu thuẫn trực tiếp với "anh Soutetsu"), chưa từng sửa "tôi"→"em". Ghi nhận để parent xem xét, không đưa vào khối sửa.
- **2676 Gotou Kaita:** TW viết 後東慶太 (Keita) nhưng JP là 後東槐多, đọc かいた đã xác nhận bằng furigana ở グランド06 2571 (後東[かいた,1]槐多氏 → "Goto Kaita") — JP thắng TW, giữ "Goto Kaita".
- **"Jussen" giữ nguyên:** file dùng "Jussen" nhất quán 8 lần cho 術仙; toàn dự án có 3 dạng (Jussen 57, Jutsusen 34, Jutsu-sen 13), chưa có quyết định thống nhất — không sửa ở đây, để đợt thống nhất quyết.
- **Giữ nguyên, đã kiểm chứng:** 1814 そのっ―― (っ dính từ nội dung + gạch nối truyền tải, không thêm Ư); 1870 んむっ→"Ưm" (âm "m" đã truyền tải); 1885 はうう～っ→"Hauu~!" (dấu ~ và ! truyền tải); 1922 ふぁ……→"fua……" (hơi thở dài, romaji tự nhiên, tiền lệ lr_ハチロクh1 1153 "fua"); 2345 八ツ城→"Yatsushiro" (TW 八代 xác nhận); 3050 （プォンっ）→"（Bíp）" (âm còi, "p" chặn đã truyền tải っ); 3053 （きゅっ）→"（Nắm lấy）" (diễn tả hành động nắm tay áo, giữ nguyên theo ngữ cảnh).
- **Lượt soát 2: 53 tổng / 53 tái kiểm chứng / 0 bỏ / 2 sửa** — 1258 bổ sung fix Teitetsu bị sót ở lượt 1 (dòng mang 2 lỗi); quét bổ sung "Kiha" toàn file thêm 6 dòng + 2 dòng gộp (2373, 3021). JSON 53 khóa chuỗi; khối TOML parse OK, 53 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 53/53.

## Khối TOML (53 khóa — đã kiểm chứng bằng tomllib: 53 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
1251 = "……Trong số các \\x%lレイルロオド;#00ffc040;Railord%l;#; do Teitetsu cũ chế tạo,\\nliệu có mấy người có thể kể về xuất thân của mình với nụ cười tươi tắn như thế này chứ."
1258 = "……Thời kỳ cuối của cuộc Đại bãi bỏ. Sự giải thể của Teitetsu, ngay giữa lúc hỗn loạn nhất.\\nNhững câu chuyện hồi ức đó quả nhiên, đối với đền chủ cũng là một vết thương lòng."
1693 = "「Cho mượn miễn phí khu đất của Đường sắt Ohitoyo xung quanh ga Yunoi,\\nphần công trình phía trên sẽ giao cho thị trấn Yunoi xây dựng và quản lý, một bảo tàng manga.」"
1697 = "「Lần sau em lại đến chơi nha~! Ufufu~, nếu được,\\nhãy đến Đường sắt Ohitoyo chơi bất cứ lúc nào nhé~!」"
1699 = "「Không chỉ vậy. Để tạo sự khác biệt, Bảo tàng Lịch sử Manga Yunoi,\\nsẽ thiết lập một kệ sách chuyên về 『Manga đường sắt』.」"
1730 = "「Anh Soutetsu mới là người 『Phần còn lại nhờ anh』 đấy!\\nChuyện của Reina, nhờ anh chăm sóc nhé!」"
1770 = "「Không phải là đồ giả tạo, mà là khu phố thời kỳ đầu Showa.\\nTuyến Yunoi được tiếp thêm sức sống và tô điểm bởi hơi nước, bởi nhiệt lượng sinh ra từ đó.」"
1811 = "「Tuy nhiên, Goto là kẻ có biệt danh \"Cường đạo\".\\nKhông chỉ tuyến đường, ông ta mua lại mọi thứ, rồi bán tống bán tháo.」"
1816 = "「Phà」"
1860 = "「À, dùng chính KiHa 07 như một \\x%l貨車;#00ffc040;toa chở hàng%l;#; sao.\\nĐến mức có cả cách vận hành như vậy——chắc hẳn nơi đó từng rất phồn vinh nhỉ.」"
1874 = "「HauƯ」"
1877 = "「A, không không, tôi lỡ lời rồi.\\nGoto, là chiến hữu——của tôi mà. Tôi lỡ buột miệng thôi.」"
1881 = "「Ư!?」"
1899 = "「Ừm. Gần đây em cũng không có nhiều thời gian để đọc,\\nnếu muốn đọc, đến bảo tàng đọc ké là được rồi.」"
1957 = "「Nếu như, cậu muốn liên lạc với Goto——」"
1959 = "「Ví dụ như, khôi phục lại thông số kỹ thuật của KiHa 07 về trạng thái ban đầu,\\nđể giảm thiểu sự quá tải do cải tạo thì sao?」"
1972 = "「Cũng giống như nụ cười của Reina đang tỏa sáng ở Ohitoyo vậy.\\nCũng giống như chiếc bình tông này, lại tỏa sáng một lần nữa.」"
1976 = "「Là dùng không gian chở khách của KiHa 07, để chở bưu kiện,\\nhay thư từ đó ạ~」"
1997 = "「Anh nghĩ việc tìm hiểu điều đó, có thể sẽ giúp ích\\ntrong việc tránh cho thành phố Ohitoyo, và Đường sắt Ohitoyo khỏi sự diệt vong.」"
2017 = "「Cảm ơn ông đã khuyên bảo. Về việc có nhờ ông liên lạc với ông Goto hay không,\\ncháu định sẽ bàn bạc lại với Kisaki và chị gái.」"
2032 = "「Anh muốn biến khu phố tên Jussen thành công viên chủ đề,\\nnhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohitoyo từ ngày xưa.」"
2070 = "「Đúng vậy ạ~. Mọi người thật sự rất trân trọng em.\\nTừ trước khi trở thành KiHa 07S, nội thất bên trong chưa từng phải sửa chữa lần nào đâu ạ~」"
2106 = "「『Câu chuyện của ông Taito』.\\nCâu chuyện về việc Teitetsu đã suy tàn và đi đến diệt vong như thế nào——」"
2116 = "「Thời kỳ hoàng kim của một tác giả nổi tiếng xuất thân từ Yunoi, đúng vào khoảng thời gian đó.\\nVì vậy, ở Yunoi có rất nhiều bộ sưu tập manga thời kỳ đó.」"
2136 = "「Chuyện của cậu Soutetsu tôi cũng đã được ông Taito gửi gắm,\\nhơn nữa, những chuyện liên quan đến thành phố Ohitoyo, cũng là chuyện của tôi mà.」"
2140 = "「Không không, không có gì phải xin lỗi đâu.\\nNgược lại, tôi còn muốn anh Soutetsu nói chuyện lâu hơn một chút cơ.」"
2178 = "「Reina, không biết về Teitetsu,\\nnhưng nếu là Đường sắt mỏ Katakami thì em biết nha~」"
2207 = "「Trong trường hợp của Reina, là chia đôi không gian bên trong KiHa 07,\\nrồi chở cả khách lẫn hành lý luôn đó ạ~」"
2211 = "「Reina, hiểu rồi ạ~! Bảo tàng Lịch sử Manga Yunoi cũng là,\\nmột phần của 『Rail Romanesque tuyến Yunoi』 nhỉ~」"
2220 = "「Tất nhiên rồi! Vừa hay, tôi cũng đang định nhờ anh Soutetsu và Reina,\\nlàm như vậy đấy.」"
2253 = "「Dù sao thì đất cũng là của Đường sắt Ohitoyo.\\nĐi bộ từ ga chưa tới ba phút là vào được bảo tàng rồi.」"
2259 = "「Chuyện đó nghe cũng thú vị thật đấy.\\nNhưng mà. Nếu là đồng nghiệp, thì ở Đường sắt Ohitoyo vẫn tốt hơn.」"
2281 = "「Mua lại và mở rộng, dù nói gì đi nữa,\\nthì vẫn là chuyện của Teitetsu mà~」"
2313 = "「Nếu vậy nếu vậy, những người đi tuyến Yunoi,\\nsẽ biết thêm và thích đường sắt hơn nhỉ~」"
2336 = "「Vậy thì, sau khi về Ohitoyo chúng ta lại nói chuyện tiếp nhé.」"
2371 = "「Anh Soutetsu, với Trưởng thị trấn Yunoi, \\nđã nói chuyện gì vậy ạ~?」"
2373 = "「Anh Soutetsu. Tôi, sẽ đưa KiHa 07S về \\x%l検修庫;#00ffc040;xưởng bảo dưỡng%l;#; đây.」"
2599 = "Nhưng, đối với những người đã sống ở Ohitoyo từ lâu,\\ntôi rốt cuộc, cũng chỉ là một kẻ ngoại lai."
2605 = "Mỏ bị bỏ hoang, đóng cửa. Cuộc Đại bãi bỏ các tuyến đường sắt như một đòn kết liễu, dẫn đến việc bãi bỏ tuyến đường sắt.\\nVà rồi, họ phải bán đi chiếc KiHa 07-2, cỗ máy đặt hàng riêng từng là niềm tự hào của họ."
2634 = "Sự kế thừa kỹ thuật khai thác than——đó sẽ là một điểm bán hàng rõ ràng.\\nRằng mỏ than vẫn đang sống trong \"Rail Romanesque tuyến Yunoi\"."
2653 = "Ở Đường sắt Ohitoyo hiện tại, việc yêu cầu Reina\\nphải đạt hiệu suất đến mức đó là điều không thể nào——"
2676 = "Goto Kaita. Về việc mua lại đất đai cho tuyến đường,\\nlà \"manh mối\" duy nhất mà đền chủ Akai có được."
2745 = "Tôi cứ tưởng đó là câu nói tinh ý của em ấy,\\nđể tôi và đền chủ Akai có thể nói chuyện thoải mái mà không phải e dè——"
2754 = "Quả thực, đó là một điểm mù.\\nĐền chủ Akai, là cựu nhân viên Teitetsu."
2790 = "Đồng thời, việc công bố 『Rail Romanesque tuyến Yunoi』\\ncấu trúc hình ảnh thống nhất của tuyến Yunoi, có lẽ là tốt nhất."
2799 = "Một người cực kỳ thận trọng như đền chủ Akai, lại dùng những từ ngữ mạnh mẽ đến vậy.\\nKhẳng định chắc nịch rằng \"sẽ không bị phớt lờ\"."
2814 = "Reina đã liên tục nói chuyện với đền chủ Akai——không, với túi công tác của \\x%l運転士;#00ffc040;người lái tàu%l;#; Akai sao."
2836 = "Rất thích làm việc, rất thích Đường sắt Ohitoyo,\\nthế mà được nghỉ vẫn thấy vui sao, tôi bất giác mỉm cười."
2964 = "Cười. Đền chủ Akai——không, chú Akai.\\nMột nụ cười vô cùng điềm đạm, ấm áp——Không hiểu sao, lại làm tôi nhớ đến bố."
2969 = "Đền chủ Akai cố nở một nụ cười điềm đạm——\\nNhưng mà, ông ấy làm không được tự nhiên cho lắm."
3001 = "Không giống đền chủ Akai chút nào——\\nNhưng tôi lại cảm thấy, đó là những từ ngữ cực kỳ giống với chú Akai."
3010 = "Những người thuộc nhóm 『chủ tàu』, ngoại trừ trường hợp đặc biệt như tôi,\\nthì chắc chắn là đồng loại với Paulette. Những người đam mê."
3021 = "Dù chỉ là một cái gật đầu nhẹ khi lên tàu KiHa 07S,\\nsau khi kết thúc cuộc đàm phán với tư cách là người đại diện Đường sắt Ohitoyo với Trưởng thị trấn Yunoi."
```

## Kết bài

File グランドリライト05_れいな sạch về cấu trúc (0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 chưa dịch, 0 trùng khóa, 0 lỗi tag) — 53/472 dòng sai (11,2%) đều là lỗi **thuật ngữ cũ chưa thống nhất** (45 dòng, 58 lượt sửa: Ohitoyo 14, Yunoi 14, Teitetsu 6, đền chủ 9, KiHa 8, Goto 5, chủ tàu 1, túi công tác 1) cộng 5 dòng xưng hô Paulette→Soutetsu và 3 gasp っ. Không có lỗi bịa nghĩa kiểu Gemini, không sai đếm nguyên âm, không mất âm mora. Hai điểm cần Hieu: **2156** (Soutetsu gọi Paulette "cô" hay "em" — câu hỏi đang chờ chốt toàn dự án) và dạng chuẩn của **術仙** ("Jussen" 57 vs "Jutsusen" 34 vs "Jutsu-sen" 13). Khối TOML 53 khóa đã kiểm chứng parse và khớp JSON tuyệt đối.

**Tổng cộng sau file này: 165 file / 7.554 dòng sai** (cơ sở 164 file / 7.501 dòng sai + 53 file này)
