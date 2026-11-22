# Unification T1 — "Ohimitera" → "Ohitoyo" — đợt U1a (00_Common / 01_Hachiroku / 02_Hibiki)

Mục: §1 **T1. 御一夜 → "Ohitoyo"** (DECIDED 19/11, Hieu). Batch U1a: chỉ các folder CSV3 00_Common, 01_Hachiroku, 02_Hibiki.

## 1. Phạm vi

- Tổng số dòng sửa trong đợt này: **221 dòng** (01_Hachiroku: 45 · 02_Hibiki: 176 · 00_Common: **0**).
- Tổng số lần xuất hiện "Ohimitera" được thay: **240** (203 dòng ×1, 17 dòng ×2, 1 dòng ×3 — 日々姫06_日々姫の決断 3628).
- 00_Common có 0 dòng: mọi dòng "Ohimitera" của folder này đã được sửa trong audit (xem §2 — riêng 共通14_負債 30 dòng đã sửa trong audit-00common14-wrong.json).
- 25 file có dòng sửa (01_Hachiroku: 7 file · 02_Hibiki: 18 file). File nhiều nhất: 日々姫10_稀咲の未来図、日々姫の未来図 (24), 日々姫13_討論会 (19), 日々姫09_静かなる開戦 (17).
- 23 dòng chứa "Đường sắt Ohimitera" → "Đường sắt Ohitoyo" (cùng phép thay T1; các dòng này cũng thỏa dạng T2 nhưng KHÔNG đếm trùng sang T2). 28 dòng có JP là 御一夜鉄道 (tên công ty).
- 5 dòng có old_vn = giá trị audit fix (không phải CSV3 VN) — xem §4. Không có dòng nào có old_vn = giá trị moan fix.
- 25 dòng chứa tag %l trong giá trị (tag JP giữ nguyên tuyệt đối, chỉ đổi phần gloss/display chứa Ohimitera — thực tế không có dòng nào có "Ohimitera" nằm trong gloss %l; tất cả đều ở display text).

## 2. Phương pháp liệt kê (enumeration)

1. Đọc CSV3 good-set: 87.833 dòng (91.731 − 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`; các dòng stale của 共通02/共通03/共通06 mang nhãn 00_Common đã bị loại, các set tốt của chúng mang nhãn 02_Hibiki/01_Hachiroku được giữ).
2. Nạp TOÀN BỘ fix list trước đó để tính giá trị hiện tại (current value) của từng dòng: moan fix nếu (file,key) có trong bất kỳ `moans/moan-*-wrong.json` nào (kể cả supplement ハチロクh3), ngược lại audit fix nếu có trong bất kỳ `audit-*-wrong.json` nào, ngược lại CSV3 VN. Map fix→file bằng khớp (key, JP) với CSV3 (chuẩn hoá `\n`/khoảng trắng toàn giác khi cần); 2 file dict-shape không có JP được map riêng: `audit-00common14-wrong.json` → 共通14_負債 (52/52 khớp old_vn với CSV3, đã kiểm chứng), `audit-lr-nagih2-wrong.json` (ngoài phạm vi đợt này). Tổng map được: audit 9.189 + moan 1.516 cặp (file,key).
3. Lọc các dòng folder 00_Common/01_Hachiroku/02_Hibiki mà current value còn chứa "Ohimitera": **221 dòng**. Trong cùng phạm vi, **244 dòng** đã được sửa trong audit (CSV3 có "Ohimitera" nhưng current value đã là "Ohitoyo") nên KHÔNG sửa lại — gồm 共通14_負債 30 dòng và các file Common/Hachiroku/Hibiki khác (xem §5).
4. Mỗi dòng ứng viên đều được đọc JP (+TW) để xác nhận JP chứa 御一夜 (hoặc 御一夜鉄道) trước khi sửa: **221/221 có; 0 dòng JP thiếu 御一夜** → 0 dòng bị flag (không có misalignment nào trong đợt này).
5. Kiểm tra chéo số dư toàn dự án bằng cùng phương pháp: current value toàn CSV3 good-set còn **311 dòng** "Ohimitera" (00_Common 0 · 01_Hachiroku 45 · 02_Hibiki 176 · 03_Paulette 11 · 04_Reina 11 · 05_Mayami 26 · 06_Kisaki 4 · 07_Nagi_Fukami 7 · 09_Grand 31 · 08_Niiroku/10_Chikuni/11_Other 0), so với ước lượng §0 của list là 333 — list đã ghi rõ remainder chỉ là ước lượng; số thực đo được là 311 (đợt U1b song song đếm lại độc lập cũng ra 311 — khớp). Trong 311 dòng: đợt U1a xử lý 221 dòng; 90 dòng còn lại thuộc các batch song song — U1b (03–06, 52 dòng) đã gộp vào ROUTE-UNIFICATION.md ~11:10, U1c (07–11, 38 dòng) đang chạy song song. Sau cả ba đợt, T1-Ohimitera còn 0 dòng. (CSV3 good-set có tổng 824 dòng "Ohimitera".)
6. Giới hạn của phép map: 9 cặp audit fix mơ hồ (cùng (key, JP, old_vn) ở 2 file — đều là dòng gasp っ/！？, không chứa Ohimitera) và file `audit-obasan-wrong.json` (255 mục flag, không có trường fix — không phải fix list) đều không ảnh hưởng đợt này. Không có fix entry nào chứa Ohimitera mà không map được.

## 3. Quy tắc áp dụng

- Chỉ thay chuỗi "Ohimitera" → "Ohitoyo", toàn bộ giá trị (kể cả trong tag %l nếu có), giữ nguyên mọi thứ khác: dấu câu, tag JP, `%l` gloss, literal `\n` (1 gạch chéo) và `\\n` (2 gạch chéo — 22 dòng có dạng này, giữ nguyên số gạch chéo), chữ hoa/thường xung quanh.
- JP thắng TW khi TW lược hoặc viết khác tên địa danh (4 dòng, xem ghi chú từng dòng).
- Các dạng khác trong cùng dòng KHÔNG đổi trong đợt này (thuộc item/batch khác): "Đường sắt Ohito" trần (4 dòng), "tuyến/ga Yui" (湯医 → Yunoi, 9 dòng còn chứa "Yui"), "Jutsu-sen" (1 dòng), "Đường sắt Hoàng gia" (1 dòng).
- Không chạm gasp-Ư, "Kh", đại từ, hay bất kỳ nội dung nào khác của dòng.

## 4. Các dòng theo file (JP / TW / old_vn / fix)

old_vn = giá trị hiện tại (moan fix > audit fix > CSV3 VN). Trong 221 dòng: 216 dòng old_vn = CSV3 VN; 5 dòng old_vn = audit fix (ghi rõ ở từng dòng). Ký hiệu `\n` trong old_vn/fix là literal backslash-n trong giá trị (không phải xuống dòng thật).

### 1. 01_Hachiroku / ハチロク01_こんにちわ赤ちゃん (9 dòng)

**Key 1662** (nhân vật: 元忠; nguồn old_vn: csv3)
- JP: 「……他の晴れ舞台があるのなら、\nわざわざ御一夜までやってきてくれる物好きはいないか」
- TW: 「……有著這麼多能夠大展身手的舞台，就沒人肯屈尊來御一夜就職了嗎」
- old_vn: 「……Nếu đã có những sân khấu tỏa sáng khác,\nthì chẳng ai lại cất công lặn lội đến tận Ohimitera nữa nhỉ.」
- fix: 「……Nếu đã có những sân khấu tỏa sáng khác,\nthì chẳng ai lại cất công lặn lội đến tận Ohitoyo nữa nhỉ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2130** (nhân vật: 元忠; nguồn old_vn: csv3)
- JP: 「[おひとよ,2]御一夜-[はやと,1]早戸間のみかん鉄道への[たいよ,1]貸与。\n先方に有利にすぎる条件だとは思っていたが――ふむ」
- TW: 「你之前將御一夜至隼人段租借給橙鐵路，我還覺得是不是太便宜對方了——嗯」
- old_vn: 「Việc cho Đường sắt Mikan thuê đoạn Ohimitera-Hayato.\nTôi đã nghĩ điều kiện đó quá có lợi cho đối phương rồi——hừm.」
- fix: 「Việc cho Đường sắt Mikan thuê đoạn Ohitoyo-Hayato.\nTôi đã nghĩ điều kiện đó quá có lợi cho đối phương rồi——hừm.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2467** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「御一夜鉄道にとって初の廃線復線――御一夜-[はやと,1]早戸間の\n扱いに関して、最終的に残った案は[ふたあん,1]二案でした」
- TW: 「御一夜鐵路恢復的第一條廢線——御一夜至隼人段的運營方案，在探討後最終留下了兩種選擇」
- old_vn: 「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohito——Về cách xử lý đoạn Ohimitera-Hayato,\ncuối cùng có hai phương án được giữ lại.」
- fix: 「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohito——Về cách xử lý đoạn Ohitoyo-Hayato,\ncuối cùng có hai phương án được giữ lại.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). JP là 御一夜鉄道 (tên công ty). JP có 御一夜鉄道 (→ "Đường sắt Ohimitera"→"Đường sắt Ohitoyo") và 御一夜-Hayato; dạng "Đường sắt Ohito" trần trong cùng dòng KHÔNG đổi đợt này (thuộc T1-bare/T2, batch khác).

**Key 2647** (nhân vật: 浦上; nguồn old_vn: csv3)
- JP: 「もちろん。っていうか、それこそ光栄。\n御一夜を立て直した腕に抱っこしてもらえるなんて」
- TW: 「當然，倒不如說能讓令御一夜復興的雙手抱抱我們茉祐真是她的福分呢」
- old_vn: 「Tất nhiên rồi. Phải nói là, đó mới là vinh hạnh đấy.\nĐược vòng tay đã vực dậy Ohimitera bế cơ mà.」
- fix: 「Tất nhiên rồi. Phải nói là, đó mới là vinh hạnh đấy.\nĐược vòng tay đã vực dậy Ohitoyo bế cơ mà.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2662** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「御一夜にまでテレビシイエムが流れておりますものね。\n東日ノ本や四國でも[じょうき,1]蒸機は高く再評価されている様子で」
- TW: 「相關的電視廣告甚至在御一夜都有播放。在關東和四國對蒸汽機車的評價似乎也大有改觀」
- old_vn: 「Ngay cả ở Ohimitera cũng đang phát quảng cáo trên tivi mà.\nỞ Đông Hinomoto hay Shikoku, có vẻ như đầu máy hơi nước cũng đang được đánh giá cao trở lại.」
- fix: 「Ngay cả ở Ohitoyo cũng đang phát quảng cáo trên tivi mà.\nỞ Đông Hinomoto hay Shikoku, có vẻ như đầu máy hơi nước cũng đang được đánh giá cao trở lại.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2710** (nhân vật: 元忠; nguồn old_vn: csv3)
- JP: 「構想は広く受け入れられている。各地の復線も順調だ。\nにもかかわらず――御一夜だけが取り残されている」
- TW: 「藍圖廣受認可，各地恢復廢線的工作也頗為順利。然而——只有御一夜被遠遠拋開」
- old_vn: 「Dự án đang được đón nhận rộng rãi. Việc khôi phục tuyến đường sắt ở các nơi cũng rất thuận lợi.\nMặc dù vậy——chỉ có Ohimitera là bị bỏ lại phía sau.」
- fix: 「Dự án đang được đón nhận rộng rãi. Việc khôi phục tuyến đường sắt ở các nơi cũng rất thuận lợi.\nMặc dù vậy——chỉ có Ohitoyo là bị bỏ lại phía sau.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2725** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「左様でございます。御一夜-早戸間。特に[おこば,1]小畑駅周辺は、\n[ひのもと,2]日ノ本中に名を[とどろ]轟かせる、天下の[しゅんけん,1]峻険」
- TW: 「誠如所言。御一夜至隼人段，尤其是大畑站周邊，乃是日本馳名的崇山峻岭」
- old_vn: 「Đúng vậy ạ. Đoạn Ohimitera-Hayato. Đặc biệt là khu vực quanh ga Okoba,\nlà nơi có địa hình hiểm trở vang danh khắp Hinomoto.」
- fix: 「Đúng vậy ạ. Đoạn Ohitoyo-Hayato. Đặc biệt là khu vực quanh ga Okoba,\nlà nơi có địa hình hiểm trở vang danh khắp Hinomoto.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2792** (nhân vật: 元忠; nguồn old_vn: csv3)
- JP: 「改めて尋ねよう。その理由は？\n構想が受け入れられると、なぜ御一夜が出遅れるのだ」
- TW: 「那我再問你一次，其原因何在？為什麼藍圖廣受認可反而會讓御一夜落後呢」
- old_vn: 「Tôi hỏi lại lần nữa. Lý do là gì?\nDự án được đón nhận, vậy tại sao Ohimitera lại bị chậm chân.」
- fix: 「Tôi hỏi lại lần nữa. Lý do là gì?\nDự án được đón nhận, vậy tại sao Ohitoyo lại bị chậm chân.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2801** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「それでどんな機関車が」「つまりその余剰機が湯医線を。\n8620が御一夜-早戸間を走ることになるのだな？」
- TW: 「那是怎樣的機車」「也就是說要讓汰換車輛負責湯醫線，由８６２０牽引御一夜至隼人段嗎？」
- old_vn: 「Vậy là đầu máy nào」「Tức là đầu máy dư thừa đó sẽ chạy tuyến Yunoi.\nCòn 8620 sẽ chạy đoạn Ohimitera-Hayato đúng không?」
- fix: 「Vậy là đầu máy nào」「Tức là đầu máy dư thừa đó sẽ chạy tuyến Yunoi.\nCòn 8620 sẽ chạy đoạn Ohitoyo-Hayato đúng không?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 2. 01_Hachiroku / ハチロク01_双鉄の目・ハチロクの目 (10 dòng)

**Key 1345** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ――日々姫が見ている“御一夜”とは、\nきっと別の御一夜を、そこから学べるように思う。
- TW: ——這與日日姬眼中的的“御一夜”必然有著千差萬別，而我正打算由此入手。
- old_vn: ——Tôi nghĩ mình có thể học được một Ohimitera khác,\nso với "Ohimitera" mà Hibiki đang nhìn thấy.
- fix: ——Tôi nghĩ mình có thể học được một Ohitoyo khác,\nso với "Ohitoyo" mà Hibiki đang nhìn thấy.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 1926** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「御一夜の人と暮らしを、もっと良く知るべきと――\n日々姫の意見を、僕は大いに参考にすべきものと感じた」
- TW: 「應該更加深入了解御一夜的人文風俗。日日姬的這個意見，我覺得非常有參考價值」
- old_vn: 「Nên hiểu rõ hơn về con người và cuộc sống ở Ohimitera——\nTôi cảm thấy ý kiến của Hibiki, là điều rất đáng để tham khảo.」
- fix: 「Nên hiểu rõ hơn về con người và cuộc sống ở Ohitoyo——\nTôi cảm thấy ý kiến của Hibiki, là điều rất đáng để tham khảo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1936** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「だと思います。きっと、そうです。\nだって、パパは――御一夜を本当に愛してたから」
- TW: 「我也這樣覺得，一定是這樣。因為爸爸他是真心愛著御一夜的」
- old_vn: 「Tôi nghĩ là vậy. Chắc chắn, là vậy rồi.\nBởi vì, ba tôi——thực sự rất yêu Ohimitera.」
- fix: 「Tôi nghĩ là vậy. Chắc chắn, là vậy rồi.\nBởi vì, ba tôi——thực sự rất yêu Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2049** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「パパ、すごくたくさんの写真撮ってたんです。\n御一夜の、それから、鉄道の」
- TW: 「爸爸拍過許許多多的照片。有御一夜的，也有鐵路的」
- old_vn: 「Ba tôi, đã chụp rất nhiều ảnh.\nCủa Ohimitera, và cả của đường sắt nữa.」
- fix: 「Ba tôi, đã chụp rất nhiều ảnh.\nCủa Ohitoyo, và cả của đường sắt nữa.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2086** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「視点は、多い方が良いと思うのだ。\n御一夜を、より深く知りたいのなら」
- TW: 「若想更深入了解御一夜，角度自然是越多越好」
- old_vn: 「Tôi nghĩ, có nhiều góc nhìn thì tốt hơn.\nNếu muốn hiểu sâu hơn về Ohimitera.」
- fix: 「Tôi nghĩ, có nhiều góc nhìn thì tốt hơn.\nNếu muốn hiểu sâu hơn về Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2827** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: それが悪いとは思わない。\n御一夜に馴染み、信頼を得ている日々姫が見る顔。
- TW: 這其實也沒什麼不好。畢竟是久居御一夜、深得眾人信賴的日日姬眼中的景色。
- old_vn: Tôi không nghĩ điều đó là xấu.\nKhuôn mặt mà một người đã hòa nhập và có được sự tin tưởng ở Ohimitera như Hibiki nhìn thấy.
- fix: Tôi không nghĩ điều đó là xấu.\nKhuôn mặt mà một người đã hòa nhập và có được sự tin tưởng ở Ohitoyo như Hibiki nhìn thấy.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2829** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: それはきっと、御一夜の素晴らしい一面であり、\n観光客に伝えていくべき魅力であろうと思うから。が――
- TW: 這必然是御一夜美麗的一面，自然也是應向遊客們展現的魅力所在。然而……
- old_vn: Đó chắc chắn, là một khía cạnh tuyệt vời của Ohimitera,\nvà là sức hấp dẫn nên truyền tải đến khách du lịch. Nhưng——
- fix: Đó chắc chắn, là một khía cạnh tuyệt vời của Ohitoyo,\nvà là sức hấp dẫn nên truyền tải đến khách du lịch. Nhưng——
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2839** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜の町は、楽しみ、親しみ、暮らす空間ではなくて、\n少しでも罪を贖う機会を探し求めるための場所だった。
- TW: 那時的御一夜於我而言，只是個贖罪的地方，完全不像是個“快樂親切的居所”。
- old_vn: Thị trấn Ohimitera, không phải là không gian để tận hưởng, gần gũi hay sinh sống,\nmà là nơi để tôi tìm kiếm cơ hội chuộc tội dù chỉ là một chút.
- fix: Thị trấn Ohitoyo, không phải là không gian để tận hưởng, gần gũi hay sinh sống,\nmà là nơi để tôi tìm kiếm cơ hội chuộc tội dù chỉ là một chút.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2894** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: （[ハチロク,3]8620を――こいつを、御一夜の顔にするのだ）
- TW: （讓[八六,3]８６２０，成為御一夜美麗的門面）
- old_vn: (Phải biến 8620——biến nó, thành gương mặt đại diện cho Ohimitera)
- fix: (Phải biến 8620——biến nó, thành gương mặt đại diện cho Ohitoyo)
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2908** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: （細かなところまで良く作ってあるな。\n町の模型は……古い御一夜を模してあるのかな？）
- TW: （連細節都做得很精緻，這街道的原型……藍本是以前的御一夜嗎？）
- old_vn: (Làm tỉ mỉ đến từng chi tiết nhỏ nhỉ.\nMô hình thị trấn này……là mô phỏng theo Ohimitera ngày xưa sao?)
- fix: (Làm tỉ mỉ đến từng chi tiết nhỏ nhỉ.\nMô hình thị trấn này……là mô phỏng theo Ohitoyo ngày xưa sao?)
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 3. 01_Hachiroku / ハチロク05_軋み (5 dòng)

**Key 1437** (nhân vật: 真闇; nguồn old_vn: csv3)
- JP: 「違かとよ。御一夜商店会の中からのクレームじゃなか。\nおかげで繁盛しとるけん、こっちはむしろ\x%l8620;#00ffc040;[ハチロク,3]8620%l;#;様様」
- TW: 「不是咧。不是御一夜商店協會裡的人投訴的哦。那邊生意興隆，他們感謝\x%l8620;#00ffc040;[八六,3]８６２０%l;#;還來不及」
- old_vn: 「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohimitera đâu.\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \x%l8620;#00ffc040;[Hachiroku,3]8620%l;#; ấy chứ.」
- fix: 「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohitoyo đâu.\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \x%l8620;#00ffc040;[Hachiroku,3]8620%l;#; ấy chứ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1761** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「あの美しいクマ川を、優しい御一夜の人と暮らしを――\n守り抜くため、どうぞわたくしたちを使ってください」
- TW: 「為了保護那條美麗的隈河，保護御一夜善良的人們以及他們的生活，請您使用我們吧」
- old_vn: 「Để bảo vệ dòng sông Kuma xinh đẹp ấy, bảo vệ cuộc sống của những người dân Ohimitera hiền hòa――\nXin ngài hãy sử dụng chúng em đi ạ.」
- fix: 「Để bảo vệ dòng sông Kuma xinh đẹp ấy, bảo vệ cuộc sống của những người dân Ohitoyo hiền hòa――\nXin ngài hãy sử dụng chúng em đi ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2124** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 煙害と感じさせないレベルまで、状況を改善させてこそ、\n僕らの目指す御一夜復興への道筋もつけられよう。
- TW: 做出改善，讓人們不覺得有煙災，這才是我們該走的御一夜復興之路。
- old_vn: （Chỉ khi cải thiện được tình hình đến mức không còn ai cảm thấy khói than là mối nguy hại nữa,\nthì con đường phục hưng Ohimitera mà chúng tôi đang hướng tới mới có thể mở ra.）
- fix: （Chỉ khi cải thiện được tình hình đến mức không còn ai cảm thấy khói than là mối nguy hại nữa,\nthì con đường phục hưng Ohitoyo mà chúng tôi đang hướng tới mới có thể mở ra.）
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2235** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜駅から数キロは離れた、寂れてしまった踏切近くで、\n未だにずっと生き続けている雑貨屋、“踏切屋”さん。
- TW: 在距御一夜車站數公里外一處冷清的道口附近，有一家至今仍在經營的名叫道口商店的雜貨店。
- old_vn: （Cách ga Ohimitera vài km, gần một đoạn giao cắt đường sắt đã bị bỏ hoang,\ncó một cửa hàng tạp hóa vẫn luôn tồn tại từ trước đến nay, mang tên "Fumikiriya".）
- fix: （Cách ga Ohitoyo vài km, gần một đoạn giao cắt đường sắt đã bị bỏ hoang,\ncó một cửa hàng tạp hóa vẫn luôn tồn tại từ trước đến nay, mang tên "Fumikiriya".）
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2475** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜上空を飛ぶものなどは、\n普段であれば鳥たちとナビくらいがせいぜいだ。
- TW: 正常情況下，御一夜的上空只有鳥和Ｎａｖｉ在活動。
- old_vn: （Những thứ bay trên bầu trời Ohimitera,\nbình thường thì cùng lắm cũng chỉ có lũ chim và Navi mà thôi.）
- fix: （Những thứ bay trên bầu trời Ohitoyo,\nbình thường thì cùng lắm cũng chỉ có lũ chim và Navi mà thôi.）
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 4. 01_Hachiroku / ハチロク06_それぞれの傷跡 (4 dòng)

**Key 1710** (nhân vật: 日々姫; nguồn old_vn: audit)
- JP: 「御一夜の人たちと、観光に来てくれた人たちと――\n[この子,3]8620を好きな人、思ってるよりたくさんいるよ？」
- TW: 「御一夜的人們，以及慕名而來的觀光客們——喜歡著[這孩子,3]８６２０的人，或許比你想像得更多哦」
- old_vn: 「Những người dân Ohimitera, những vị khách đến tham quan――\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」
- fix: 「Những người dân Ohitoyo, những vị khách đến tham quan――\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). old_vn = giá trị audit fix (audit đã bỏ tag %l quanh 8620 so với CSV3); chỉ đổi Ohimitera→Ohitoyo trên giá trị audit.

**Key 1819** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「ああ。\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致を撤回させ、御一夜を守りたい。\n僕の目的を、ハチロクは果たさせたいと願っているのだ」
- TW: 「沒錯。八六她是一心想要實現我“取消\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶計劃，守護御一夜”的這一目標」
- old_vn: 「Ừ. Muốn họ rút lại quyết định mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;, muốn bảo vệ Ohimitera.\nHachiroku đang mong muốn giúp tôi đạt được mục đích đó.」
- fix: 「Ừ. Muốn họ rút lại quyết định mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;, muốn bảo vệ Ohitoyo.\nHachiroku đang mong muốn giúp tôi đạt được mục đích đó.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2706** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: その間に、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致を撤回に追い込めないなら、\n双鉄様は、きっと、御一夜から居なくなる。
- TW: 若是不能在這段時間內阻止\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶的話，雙鐵少爺勢必也將無法繼續留在御一夜。
- old_vn: Trong khoảng thời gian đó, nếu không thể ép họ rút lại quyết định mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\nthì chắc chắn ngài Soutetsu sẽ phải rời khỏi Ohimitera.
- fix: Trong khoảng thời gian đó, nếu không thể ép họ rút lại quyết định mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\nthì chắc chắn ngài Soutetsu sẽ phải rời khỏi Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2710** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 驚かされるが、考えてみれば\n御一夜-湯医は路線長でも二十と数キロ。
- TW: 著實嚇我一跳，不過想來御一夜到湯醫雖不近，但也不過二十幾公里。
- old_vn: Tuy hơi bất ngờ, nhưng nghĩ lại thì\ntuyến Ohimitera - Yui cũng chỉ dài khoảng hai mươi mấy kilomet.
- fix: Tuy hơi bất ngờ, nhưng nghĩ lại thì\ntuyến Ohitoyo - Yui cũng chỉ dài khoảng hai mươi mấy kilomet.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 5. 01_Hachiroku / ハチロク11_御一夜鉄道小畑線 (3 dòng)

**Key 1201** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ……御一夜からこの小畑までとて、十分すぎる登りだった。
- TW: ……從御一夜到這大畑，我們已經爬了不少的坡了。
- old_vn: ...Chỉ từ Ohimitera đến Okoba này thôi, độ dốc đã là quá đủ rồi.
- fix: ...Chỉ từ Ohitoyo đến Okoba này thôi, độ dốc đã là quá đủ rồi.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2011** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「まことですね。御一夜から小畑まで、\nわずかに10.4キロだというのに」
- TW: 「是的呀。由御一夜至大畑，不過短短十點四公里而已」
- old_vn: 「Đúng vậy nhỉ. Từ Ohimitera đến Okoba, \nmới chỉ có 10.4 kilomet thôi mà.」
- fix: 「Đúng vậy nhỉ. Từ Ohitoyo đến Okoba, \nmới chỉ có 10.4 kilomet thôi mà.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2664** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ――僕らの街が、御一夜が、\n小さく、けれども、確かに見える。
- TW: 我們的城鎮御一夜，雖然只有一點點，但確實就在我們目力可及之處。
- old_vn: ——Thành phố của chúng ta, Ohimitera, \nnhỏ bé, nhưng chắc chắn là có thể nhìn thấy.
- fix: ——Thành phố của chúng ta, Ohitoyo, \nnhỏ bé, nhưng chắc chắn là có thể nhìn thấy.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 6. 01_Hachiroku / ハチロク12_ムナカタ来訪 (11 dòng)

**Key 1525** (nhân vật: 宗方; nguồn old_vn: csv3)
- JP: 「術仙車両工場だけにとどまらず、\x%l保線;#00ffc040;保線%l;#;についても、\n御一夜回りに集積させ。言うなら“鉄道の御一夜”と？」
- TW: 「不止術仙車輛工廠，也要將\x%l保線;#00ffc040;巡線%l;#;相關的產業聚集於御一夜周邊，說白了也就是將御一夜打造為“鐵路之都”？」
- old_vn: 「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsu-sen, mà cả về \x%l保線;#00ffc040;bảo trì đường ray%l;#;, \ncũng sẽ tập trung xung quanh Ohimitera. Có thể gọi là 'Ohimitera của đường sắt' sao?」
- fix: 「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsu-sen, mà cả về \x%l保線;#00ffc040;bảo trì đường ray%l;#;, \ncũng sẽ tập trung xung quanh Ohitoyo. Có thể gọi là 'Ohitoyo của đường sắt' sao?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. 2× Ohimitera (câu "Ohimitera của đường sắt" + "xung quanh Ohimitera"); "Jutsu-sen" trong cùng dòng KHÔNG đổi đợt này (T17, batch khác).

**Key 1650** (nhân vật: 宗方; nguồn old_vn: csv3)
- JP: 「右田さんは大廃線前。御社社長が復線させたがっている、\n[かわせん,1]川線――[おひとよ,2]御一夜ー[やつしろ,2]八ツ城間に乗ったことは？」
- TW: 「右田先生，對於貴公司社長渴望恢復的那條河岸線路——御一夜至八代段，你在大廢線之前可有過搭車途經過？」
- old_vn: 「Cậu Migita. Trước khi Đại bãi bỏ các tuyến đường sắt diễn ra. Tuyến sông mà ngài Giám đốc quý công ty đang muốn khôi phục—— \nđoạn Ohimitera - Yatsushiro, cậu đã từng đi qua chưa?」
- fix: 「Cậu Migita. Trước khi Đại bãi bỏ các tuyến đường sắt diễn ra. Tuyến sông mà ngài Giám đốc quý công ty đang muốn khôi phục—— \nđoạn Ohitoyo - Yatsushiro, cậu đã từng đi qua chưa?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1658** (nhân vật: れいな; nguồn old_vn: csv3)
- JP: 「昔の[こくら,1]粉蔵みたいに、九洲の鉄道ぜぇんぶをお手当できる。\nポーレットは御一夜をそういうふうにしたいんですよぉ」
- TW: 「同時，要讓御一夜像曾經的小倉一樣，能夠撐起整個九州的鐵路，這就是波萊特的願望」
- old_vn: 「Giống như Kokura ngày xưa, có thể bảo dưỡng cho toàn bộ đường sắt ở Kyushu. \nPaulette muốn biến Ohimitera thành một nơi như vậy đó ạ~」
- fix: 「Giống như Kokura ngày xưa, có thể bảo dưỡng cho toàn bộ đường sắt ở Kyushu. \nPaulette muốn biến Ohitoyo thành một nơi như vậy đó ạ~」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1705** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「ああ、失礼。自己紹介が遅れてしまいました。\nボクは、隈元銀行御一夜支店長の宝生稀咲です」
- TW: 「啊，不好意思，我還沒做自我介紹。我是隈元銀行御一夜支行行長，名叫寶生稀咲」
- old_vn: 「A, thất lễ quá. Cháu giới thiệu bản thân hơi muộn. \nCháu là Houshou Kisaki, Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto.」
- fix: 「A, thất lễ quá. Cháu giới thiệu bản thân hơi muộn. \nCháu là Houshou Kisaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1847** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「御一夜市がすすめる、“蒸気のふるさと”構想を、\n更に推し進めていこうという発想です」
- TW: 「將目前御一夜市正在開展的“蒸汽之鄉御一夜”計劃，做進一步升級」
- old_vn: 「Ý tưởng là thúc đẩy mạnh mẽ hơn nữa dự án 'Quê hương của hơi nước', \nmà thành phố Ohimitera đang tiến hành.」
- fix: 「Ý tưởng là thúc đẩy mạnh mẽ hơn nữa dự án 'Quê hương của hơi nước', \nmà thành phố Ohitoyo đang tiến hành.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1886** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「かつて御一夜は、鉄道の一大\x%lターミナル駅;#00ffc040;ターミナル駅%l;#;でした。\n復線により、その再現を目指していくと同時に」
- TW: 「御一夜曾經也是鐵路的一大\x%lターミナル駅;#00ffc040;總站%l;#;，我們希望藉恢復廢線這個機會，重現當年風采」
- old_vn: 「Trước đây, Ohimitera từng là một \x%lターミナル駅;#00ffc040;ga đầu mối%l;#; đường sắt lớn. \nThông qua việc khôi phục các tuyến đường, chúng cháu hướng tới việc tái hiện lại điều đó, đồng thời」
- fix: 「Trước đây, Ohitoyo từng là một \x%lターミナル駅;#00ffc040;ga đầu mối%l;#; đường sắt lớn. \nThông qua việc khôi phục các tuyến đường, chúng cháu hướng tới việc tái hiện lại điều đó, đồng thời」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1900** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「確かに。ので御一夜市、御一夜鉄道とヴィジョンを\n共有し、シナジーある展開をと考えている最中です」
- TW: 「您所言不虛，所以此次我行計劃與御一夜市以及御一夜鐵路共同展望前景，通力合作以起到相互促進的作用」
- old_vn: 「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohimitera, \nvà Đường sắt Ohito, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」
- fix: 「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohitoyo, \nvà Đường sắt Ohito, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). JP là 御一夜鉄道 (tên công ty). "Đường sắt Ohito" trần trong cùng dòng KHÔNG đổi đợt này (T1-bare/T2, batch khác).

**Key 1955** (nhân vật: 宗方; nguồn old_vn: csv3)
- JP: 「[こくら,1]粉蔵のイメージか……粉蔵と比べ、御一夜は物流経路で\nかなりのハンディを背負いそうだが」
- TW: 「打造類似小倉的形象……可是相比小倉，御一夜僅屬於運輸要道，其中差距可想而知」
- old_vn: 「Hình ảnh của Kokura sao... So với Kokura, Ohimitera \ncó vẻ sẽ phải gánh chịu khá nhiều bất lợi về tuyến đường logistics đấy.」
- fix: 「Hình ảnh của Kokura sao... So với Kokura, Ohitoyo \ncó vẻ sẽ phải gánh chịu khá nhiều bất lợi về tuyến đường logistics đấy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2027** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「はい。御一夜の桜は見事なものです。\n桜吹雪の中を走るⅨ号も、きっと、ひときわ可憐かと」
- TW: 「正是，御一夜的櫻花盛開之景可謂美輪美奐，若讓九號於飛雪般的落花中奔馳，想必更能凸顯其嫵媚」
- old_vn: 「Vâng. Hoa anh đào ở Ohimitera đẹp tuyệt trần ạ. \nĐầu máy số IX chạy giữa cơn mưa hoa anh đào, chắc chắn, cũng sẽ vô cùng kiều diễm.」
- fix: 「Vâng. Hoa anh đào ở Ohitoyo đẹp tuyệt trần ạ. \nĐầu máy số IX chạy giữa cơn mưa hoa anh đào, chắc chắn, cũng sẽ vô cùng kiều diễm.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2089** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「御一夜鉄道自身も、将来的な延伸を計画してます。\n最優先は、御一夜－八ツ城の川線の復線。それから」
- TW: 「而我們御一夜鐵路也計劃於未來進一步延伸，首先是恢復御一夜至八代的河岸線路，然後再……」
- old_vn: 「Bản thân Đường sắt Ohito cũng đang lên kế hoạch mở rộng trong tương lai. \nƯu tiên hàng đầu là khôi phục Tuyến sông Ohimitera - Yatsushiro. Sau đó」
- fix: 「Bản thân Đường sắt Ohito cũng đang lên kế hoạch mở rộng trong tương lai. \nƯu tiên hàng đầu là khôi phục Tuyến sông Ohitoyo - Yatsushiro. Sau đó」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). JP là 御一夜鉄道 (tên công ty). "Đường sắt Ohito" trần trong cùng dòng KHÔNG đổi đợt này (T1-bare/T2, batch khác).

**Key 2176** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「それは……ありかもしれませんね。[おおみや,1]旺宮ー[ひろしま,1]廣島ー御一夜に、\nまがりなりにも、交流が発生しはじめたのですし」
- TW: 「這些主意……的確是可行的，畢竟大宮、廣島以及御一夜之間，多多少少也已經開始開展合作了」
- old_vn: 「Điều đó... có thể khả thi đấy ạ. Dù sao thì giữa Omiya, Hiroshima và Ohimitera, \ncũng đã bắt đầu có sự giao lưu rồi mà.」
- fix: 「Điều đó... có thể khả thi đấy ạ. Dù sao thì giữa Omiya, Hiroshima và Ohitoyo, \ncũng đã bắt đầu có sự giao lưu rồi mà.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 7. 01_Hachiroku / ハチロク16_春 (3 dòng)

**Key 1803** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「オリヴィちゃんは、きっと、しあわせでしたよね？\n御一夜に来たことを、悔やまず、旅立ちましたよね？」
- TW: 「奧莉薇一定很幸福吧？她離開的時候，沒有因為來到御一夜而感到後悔吧？」
- old_vn: 「Bé Olivy, chắc chắn là đã rất hạnh phúc đúng không ạ?\nEm ấy đã ra đi mà không hề hối hận vì đã đến Ohimitera đúng không ạ?」
- fix: 「Bé Olivy, chắc chắn là đã rất hạnh phúc đúng không ạ?\nEm ấy đã ra đi mà không hề hối hận vì đã đến Ohitoyo đúng không ạ?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1839** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「そそ。私は蒸気\x%l機関士;#00ffc040;機関士%l;#;だし――\n術仙工場のこともあるけん、御一夜ば、離れられんし」
- TW: 「對對。我是蒸汽機車的\x%l機関士;#00ffc040;司機%l;#;嘛——還要照顧術仙工廠呢，哪能離開御一夜呀」
- old_vn: 「Đúng đúng. Em là \x%l機関士;#00ffc040;lái tàu%l;#; hơi nước mà――\nCòn chuyện của nhà máy Jutsusen nữa, em không thể rời khỏi Ohimitera được.」
- fix: 「Đúng đúng. Em là \x%l機関士;#00ffc040;lái tàu%l;#; hơi nước mà――\nCòn chuyện của nhà máy Jutsusen nữa, em không thể rời khỏi Ohitoyo được.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1845** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「『御一夜で一番の温泉に泊まりたい』\nこだまちゃんが望んだことではございませんか」
- TW: 「小玉不是希望“在御一夜最好的溫泉過夜”嗎」
- old_vn: 「『Muốn trọ lại suối nước nóng tốt nhất Ohimitera』\nĐó chẳng phải là mong muốn của bé Kodama sao.」
- fix: 「『Muốn trọ lại suối nước nóng tốt nhất Ohitoyo』\nĐó chẳng phải là mong muốn của bé Kodama sao.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 8. 02_Hibiki / lr_日々姫ふかみh1_凪ちゃんの代わり (1 dòng)

**Key 1689** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「まぁ、急な話だったからな。稀咲仲介での、\n仲国からの要人たちの、団体での御一夜視察」
- TW: 「沒辦法嘛。畢竟在稀咲中介下，來自仲國的重要人物集體來御一夜視察這件事太突然了」
- old_vn: 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\nđến thị sát Ohimitera thông qua sự môi giới của Kisaki.」
- fix: 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\nđến thị sát Ohitoyo thông qua sự môi giới của Kisaki.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 9. 02_Hibiki / 日々姫01_リゾート食堂列車計画 (13 dòng)

**Key 1224** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ……エアクラ工場御一夜誘致議案を廃案に追い込み、\n早五年。
- TW: ……空凝機工廠引進議案被迫廢棄後，轉眼就過了五年。
- old_vn: ……Kể từ khi dự luật mời nhà máy Aircra về Ohimitera bị bác bỏ,\nthoắt cái đã năm năm trôi qua.
- fix: ……Kể từ khi dự luật mời nhà máy Aircra về Ohitoyo bị bác bỏ,\nthoắt cái đã năm năm trôi qua.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). TW lược tên địa danh (không có 御一夜) — JP có 御一夜, JP thắng TW, vẫn sửa.

**Key 1561** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「他の全てが上手く運ぶ一方、御一夜市への直接の\n恩恵を運んでくれるこの列車だけが、滞っている」
- TW: 「其他方面都在順利運作，唯有這列能為御一夜市帶來直接利益的列車遲遲沒有進展」
- old_vn: 「Trong khi mọi thứ khác đều đang tiến triển thuận lợi, thì chỉ có chuyến tàu này\n- thứ mang lại lợi ích trực tiếp cho thành phố Ohimitera - lại đang bị đình trệ.」
- fix: 「Trong khi mọi thứ khác đều đang tiến triển thuận lợi, thì chỉ có chuyến tàu này\n- thứ mang lại lợi ích trực tiếp cho thành phố Ohitoyo - lại đang bị đình trệ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1658** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「でしたら認めましょう――リゾート食堂列車計画は、\n御一夜鉄道と周辺各社の出資のみによるもの」
- TW: 「好吧，那麼我承認——觀光餐車計劃完全依賴御一夜鐵路與周邊各公司的投資」
- old_vn: 「Nếu vậy thì tôi xin thừa nhận——Dự án tàu ăn uống nghỉ dưỡng,\nchỉ dựa vào vốn đầu tư của Đường sắt Ohimitera và các công ty xung quanh.」
- fix: 「Nếu vậy thì tôi xin thừa nhận——Dự án tàu ăn uống nghỉ dưỡng,\nchỉ dựa vào vốn đầu tư của Đường sắt Ohitoyo và các công ty xung quanh.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1680** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「現在は他市が受けている恩恵を、御一夜市へ呼ぶ。\nそれが、『リゾート食堂列車』構想の骨子ですね？」
- TW: 「將其他市獲得的利益引至御一夜市。這就是“觀光餐車”方案的核心吧？」
- old_vn: 「Kéo những lợi ích mà các thành phố khác đang được hưởng về Ohimitera.\nĐó chính là cốt lõi của ý tưởng 『Tàu ăn uống nghỉ dưỡng』 đúng không?」
- fix: 「Kéo những lợi ích mà các thành phố khác đang được hưởng về Ohitoyo.\nĐó chính là cốt lõi của ý tưởng 『Tàu ăn uống nghỉ dưỡng』 đúng không?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1714** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「御一夜市が最も多くの資金を出し汗を流しての\n路線延伸が、御一夜市以外の土地だけを潤している」
- TW: 「御一夜市在線路延長事業上投入了最多資金與人力，受惠的卻都是御一夜市以外的土地」
- old_vn: 「Thành phố Ohimitera đã bỏ ra nhiều tiền bạc và mồ hôi công sức nhất\nđể mở rộng tuyến đường, nhưng lại chỉ làm giàu cho những vùng đất ngoài Ohimitera.」
- fix: 「Thành phố Ohitoyo đã bỏ ra nhiều tiền bạc và mồ hôi công sức nhất\nđể mở rộng tuyến đường, nhưng lại chỉ làm giàu cho những vùng đất ngoài Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 1773** (nhân vật: 議長; nguồn old_vn: csv3)
- JP: 「これにて、新津議員の質問を終わります。\n続きまして、『御一夜市民の会』、[ふせ,1]布施議員――」
- TW: 「新津議員的提問就此結束。接下來是“御一夜市民會”的布施議員――」
- old_vn: 「Đến đây, phần chất vấn của nghị viên Niitsu xin được kết thúc.\nTiếp theo, nghị viên Fuse thuộc 『Hội Công dân Ohimitera』——」
- fix: 「Đến đây, phần chất vấn của nghị viên Niitsu xin được kết thúc.\nTiếp theo, nghị viên Fuse thuộc 『Hội Công dân Ohitoyo』——」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1895** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「よいご視察となることを期待しています。\n御一夜市の未来のために、あなたのデザインが必要だ」
- TW: 「祝願您的考察之旅能有所收穫。為了御一夜市的未來，我們需要您的設計」
- old_vn: 「Tôi rất mong chờ chuyến khảo sát tốt đẹp của ngài.\nVì tương lai của thành phố Ohimitera, chúng tôi cần thiết kế của ngài.」
- fix: 「Tôi rất mong chờ chuyến khảo sát tốt đẹp của ngài.\nVì tương lai của thành phố Ohitoyo, chúng tôi cần thiết kế của ngài.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1973** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「驚かれることではないでしょう。御一夜の新名所。\n[ガマダス,6]gamadus――あれも大変に楽しい施設です」
- TW: 「這沒什麼好驚訝的。御一夜的新名勝ＧＡＭＡＤＵＳ，也是非常出色的娛樂設施」
- old_vn: 「Không có gì đáng ngạc nhiên đâu. Địa danh mới của Ohimitera.\nGamadus——đó cũng là một cơ sở vô cùng thú vị.」
- fix: 「Không có gì đáng ngạc nhiên đâu. Địa danh mới của Ohitoyo.\nGamadus——đó cũng là một cơ sở vô cùng thú vị.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2004** (nhân vật: 新津; nguồn old_vn: csv3)
- JP: 「市長自らが中心となりデザイン・計画を進めている、\n[おひとよ,2]御一夜鉄道の『リゾート食堂列車』」
- TW: 「關於市長親自設計、策劃並主持的御一夜鐵路的“觀光餐車”」
- old_vn: 「Dự án 『Tàu ăn uống nghỉ dưỡng』 của Đường sắt Ohimitera,\ndo đích thân thị trưởng làm trung tâm tiến hành thiết kế và lập kế hoạch.」
- fix: 「Dự án 『Tàu ăn uống nghỉ dưỡng』 của Đường sắt Ohitoyo,\ndo đích thân thị trưởng làm trung tâm tiến hành thiết kế và lập kế hoạch.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2225** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜鉄道が主体となっての\n御一夜-小畑-早戸間の復線。
- TW: 恢復以御一夜鐵路為主體的御一夜—大畑—隼人區段的廢線。
- old_vn: Khôi phục tuyến đường giữa Ohimitera - Obata - Hayato\ndo Đường sắt Ohimitera làm chủ thể.
- fix: Khôi phục tuyến đường giữa Ohitoyo - Obata - Hayato\ndo Đường sắt Ohitoyo làm chủ thể.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2473** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 確かにそれこそ、この計画の大目標のひとつだ。\n御一夜から大板へ。大板から御一夜へ。
- TW: 這確實是計劃的大目標之一。從御一夜到大分，再從大分到御一夜。
- old_vn: Đó quả thực là một trong những mục tiêu lớn của dự án này.\nTừ Ohimitera đến Oita. Từ Oita về Ohimitera.
- fix: Đó quả thực là một trong những mục tiêu lớn của dự án này.\nTừ Ohitoyo đến Oita. Từ Oita về Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 2484** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜銀行に籍を置き続ける稀咲相手に、\n経済畑の新津議員はそう強気には出られない。
- TW: 面對擁有御一夜銀行成員身份的稀咲，專攻經濟領域的新津議員也強勢不起來了。
- old_vn: Đối mặt với Kisaki, người vẫn đang giữ chức vụ tại Ngân hàng Ohimitera,\nnghị viên Niitsu thuộc mảng kinh tế không thể tỏ ra quá mạnh miệng được.
- fix: Đối mặt với Kisaki, người vẫn đang giữ chức vụ tại Ngân hàng Ohitoyo,\nnghị viên Niitsu thuộc mảng kinh tế không thể tỏ ra quá mạnh miệng được.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2506** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 確かにガマダス――児童向けの御一夜鉄道資料館は\n素晴らしく楽しい施設だが……
- TW: ＧＡＭＡＤＵＳ——面向兒童的御一夜鐵路資料館確實是非常優秀的娛樂設施，但是……
- old_vn: Đúng là Gamadus——Bảo tàng tư liệu Đường sắt Ohimitera dành cho trẻ em\nlà một cơ sở tuyệt vời và thú vị, nhưng……
- fix: Đúng là Gamadus——Bảo tàng tư liệu Đường sắt Ohitoyo dành cho trẻ em\nlà một cơ sở tuyệt vời và thú vị, nhưng……
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

### 10. 02_Hibiki / 日々姫03_湯富院 (2 dòng)

**Key 2279** (nhân vật: 湯富院市長; nguồn old_vn: csv3)
- JP: 「御一夜の皆さんが客車[しんぞう,1]新造を事業化してくれたこと。\n一個人としても市長としても、感謝してましてね」
- TW: 「無論是以個人還是市長的身份，我都要感謝御一夜能夠把生產全新客運車廂的業務做起來」
- old_vn: 「Việc mọi người ở Ohimitera biến việc đóng mới \x%l客車;#00ffc040;toa hành khách%l;#; thành một dự án kinh doanh.\nDù là tư cách cá nhân hay Thị trưởng, tôi đều rất biết ơn.」
- fix: 「Việc mọi người ở Ohitoyo biến việc đóng mới \x%l客車;#00ffc040;toa hành khách%l;#; thành một dự án kinh doanh.\nDù là tư cách cá nhân hay Thị trưởng, tôi đều rất biết ơn.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2607** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 並び立ちながら競い合う両温泉地に、実際のところ、\n御一夜は潜在的な顧客を奪われ続けていた感さえある。
- TW: 其實這兩座分庭抗禮，互不相讓的溫泉勝地，可能一直在搶奪御一夜的潛在客戶。
- old_vn: Thực tế, Ohimitera thậm chí còn có cảm giác như đang liên tục bị cướp mất khách hàng tiềm năng\nbởi hai khu suối nước nóng đang cạnh tranh gay gắt này.
- fix: Thực tế, Ohitoyo thậm chí còn có cảm giác như đang liên tục bị cướp mất khách hàng tiềm năng\nbởi hai khu suối nước nóng đang cạnh tranh gay gắt này.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 11. 02_Hibiki / 日々姫04_カフェキッチン (6 dòng)

**Key 1757** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「しかし、御一夜の子供たちが鉱山に馴染んでいる\nとは思えません。ほんの少しだけ見立てを変えて――」
- TW: 「但是，御一夜的孩子們應該並不熟悉礦山。稍微改變一下外形……」
- old_vn: 「Nhưng mà, em không nghĩ trẻ em ở Ohimitera\nlại quen thuộc với khu mỏ đâu ạ. Chỉ cần thay đổi cách mô phỏng một chút——」
- fix: 「Nhưng mà, em không nghĩ trẻ em ở Ohitoyo\nlại quen thuộc với khu mỏ đâu ạ. Chỉ cần thay đổi cách mô phỏng một chút——」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1788** (nhân vật: 凪; nguồn old_vn: csv3)
- JP: 「別に、にーさんらのためだけじゃなかとよ～\n御一夜鉄道の、自分らのためでもあるけん！」
- TW: 「又不單單是為了大哥哥你們啦。這也是為了御一夜鐵路，為了我們自己！」
- old_vn: 「Cũng không hẳn là chỉ vì anh Soutetsu đâu~\nMà còn vì Đường sắt Ohimitera, vì chính bản thân bọn em nữa mà!」
- fix: 「Cũng không hẳn là chỉ vì anh Soutetsu đâu~\nMà còn vì Đường sắt Ohitoyo, vì chính bản thân bọn em nữa mà!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1882** (nhân vật: れいな; nguồn old_vn: csv3)
- JP: 「ああ！　そおですねぇ、ＳＬカレーにしたほうが、\n御一夜のおちびちゃんたち、もっと嬉しいかもですぅ」
- TW: 「啊！　也對，做成蒸汽機車咖哩的話，御一夜的小不點們應該會更喜歡的」
- old_vn: 「A! Đúng vậy nha, làm thành cà ri SL,\nchắc các bé ở Ohimitera sẽ vui hơn đó ạ.」
- fix: 「A! Đúng vậy nha, làm thành cà ri SL,\nchắc các bé ở Ohitoyo sẽ vui hơn đó ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2017** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「凪ちゃんとふかみちゃんが教えてくれた、\n御一夜・クマの、古くからの季節の料理もおいしそうで」
- TW: 「小凪和小深跟我講的御一夜、隈元一帶祖傳的當季料理好像也很好吃」
- old_vn: 「Những món ăn theo mùa từ xa xưa của Ohimitera và Kuma\nmà Nagi và Fukami chỉ cho cũng có vẻ ngon lắm.」
- fix: 「Những món ăn theo mùa từ xa xưa của Ohitoyo và Kuma\nmà Nagi và Fukami chỉ cho cũng có vẻ ngon lắm.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2067** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「右田日々姫です。稀咲先輩の後輩で、御一夜市長で、\nデザイナーで。今も、臨時では機関助士です」
- TW: 「我是右田日日姬。是稀咲學姐的後輩，也是御一夜市長，同時兼任設計師。現在還是臨時的司爐」
- old_vn: 「Tôi là Migita Hibiki. Là hậu bối của tiền bối Kisaki, thị trưởng thành phố Ohimitera,\nlà nhà thiết kế. Và hiện tại, cũng là phụ lái tàu tạm thời.」
- fix: 「Tôi là Migita Hibiki. Là hậu bối của tiền bối Kisaki, thị trưởng thành phố Ohitoyo,\nlà nhà thiết kế. Và hiện tại, cũng là phụ lái tàu tạm thời.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2310** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「双鉄様。どうぞ。\n日々姫のため、御一夜のため。お役立てください」
- TW: 「雙鐵少爺，請收下它，並用它幫助日日姬，幫助御一夜吧」
- old_vn: 「Ngài Soutetsu. Xin mời ạ.\nVì Hibiki, vì Ohimitera. Xin ngài hãy sử dụng nó cho hiệu quả ạ.」
- fix: 「Ngài Soutetsu. Xin mời ạ.\nVì Hibiki, vì Ohitoyo. Xin ngài hãy sử dụng nó cho hiệu quả ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 12. 02_Hibiki / 日々姫05_市議会見学 (8 dòng)

**Key 1570** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「……御一夜鉄道もそうだし、御一夜市もそうだし。\nお金があれば、誰も苦しい思いをしないですむのかなぁ」
- TW: 「……御一夜鐵路也好，御一夜市也好，有錢的話誰都不用為難了吧」
- old_vn: 「……Đường sắt Ohimitera cũng vậy, thành phố Ohimitera cũng vậy.\nNếu có tiền, thì có lẽ sẽ không ai phải chịu đựng sự đau khổ nữa nhỉ.」
- fix: 「……Đường sắt Ohitoyo cũng vậy, thành phố Ohitoyo cũng vậy.\nNếu có tiền, thì có lẽ sẽ không ai phải chịu đựng sự đau khổ nữa nhỉ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1868** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「少等部六年の、仲等部にあがる前の年の書き初めで、\nみんな、必ず書くんです。御一夜市全部の学園で」
- TW: 「升上國中部的前一年——也就是小學部六年級那年的新年，大家都會寫的。所有御一夜市的學校都是這樣」
- old_vn: 「Lớp sáu trường Tiểu học, trong buổi khai bút đầu năm trước khi lên Trung học,\nai cũng bắt buộc phải viết nó. Ở tất cả các trường trong thành phố Ohimitera.」
- fix: 「Lớp sáu trường Tiểu học, trong buổi khai bút đầu năm trước khi lên Trung học,\nai cũng bắt buộc phải viết nó. Ở tất cả các trường trong thành phố Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1992** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「だとしても。駿川市との姉妹都市提携が、\n御一夜市に多くのメリットを与えることは変わりません」
- TW: 「就算是這樣，和駿川市結為姐妹城市，一樣會為御一夜市帶來諸多好處」
- old_vn: 「Cho dù là vậy. Việc kết nghĩa thành phố với thành phố Surukawa,\nsẽ mang lại nhiều lợi ích cho thành phố Ohimitera là điều không thay đổi.」
- fix: 「Cho dù là vậy. Việc kết nghĩa thành phố với thành phố Surukawa,\nsẽ mang lại nhiều lợi ích cho thành phố Ohitoyo là điều không thay đổi.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2050** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「だからかな？　御一夜市の市税徴収率は、県下どころか、\n九洲全域でもずば抜けて高い、一位なんだよ」
- TW: 「所以才會這樣？御一夜市的市稅徵收率別說在縣內，在整個九州也是出類拔萃，高居第一」
- old_vn: 「Có lẽ vì thế chăng? Tỷ lệ thu thuế của thành phố Ohimitera không chỉ trong tỉnh,\nmà còn cao vượt trội trên toàn khu vực Kyushu, đứng vị trí số 1 đấy.」
- fix: 「Có lẽ vì thế chăng? Tỷ lệ thu thuế của thành phố Ohitoyo không chỉ trong tỉnh,\nmà còn cao vượt trội trên toàn khu vực Kyushu, đứng vị trí số 1 đấy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2239** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「まったく話が違います。エアロ＝クラフテック社の活動と、\n御一夜市の発展とでは、win-winの関係を築けないと」
- TW: 「這完全不同。空凝科技公司的活動和御一夜市的發展之間構築不了雙贏的關係」
- old_vn: 「Hai chuyện hoàn toàn khác nhau. Hoạt động của công ty Aero-Craftech\nvà sự phát triển của thành phố Ohimitera không thể xây dựng được mối quan hệ đôi bên cùng có lợi.」
- fix: 「Hai chuyện hoàn toàn khác nhau. Hoạt động của công ty Aero-Craftech\nvà sự phát triển của thành phố Ohitoyo không thể xây dựng được mối quan hệ đôi bên cùng có lợi.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2243** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「それが議員の発言か！\n御一夜市民の代表者として、恥ずかしくないのかっ！」
- TW: 「這是議員該有的發言嗎！身為御一夜市民的代表，你難道不感到羞恥嗎！」
- old_vn: 「Đó là phát ngôn của một nghị viên sao!\nLà đại diện cho người dân Ohimitera, ông không thấy xấu hổ à!」
- fix: 「Đó là phát ngôn của một nghị viên sao!\nLà đại diện cho người dân Ohitoyo, ông không thấy xấu hổ à!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2434** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ずっと隈元とか御一夜だったら、きっと、\nこんなに綺麗に響かない。
- TW: 一直待在隈元是不會有這麼標準的發音的。我也一直以她的普通話為榜樣。
- old_vn: Nếu cứ ở Kumamoto hay Ohimitera mãi, thì chắc chắn,\nsẽ không thể nói hay đến thế.
- fix: Nếu cứ ở Kumamoto hay Ohitoyo mãi, thì chắc chắn,\nsẽ không thể nói hay đến thế.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). TW viết 隈元 (Kumamoto) thay cho 御一夜 — JP có 御一夜, JP thắng TW, vẫn sửa.

**Key 2701** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 標準語とか、帝都とか。それはやっぱり憧れだけど、\n御一夜には御一夜の面白さがある。
- TW: 普通話也好，帝都也好，這些確實很讓人嚮往，不過御一夜也有御一夜的樂趣。
- old_vn: Tiếng phổ thông, hay thủ đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\nnhưng Ohimitera cũng có những điều thú vị riêng của Ohimitera.
- fix: Tiếng phổ thông, hay thủ đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\nnhưng Ohitoyo cũng có những điều thú vị riêng của Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

### 13. 02_Hibiki / 日々姫05_御一夜ステーションカフェ (3 dòng)

**Key 2560** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「ここが、ガマダスカフェ――\nあらため、御一夜ステーションカフェですか」
- TW: 「這裡就是ＧＡＭＡＤＵＳ咖啡廳——改名後該叫御一夜站咖啡廳了啊」
- old_vn: 「Đây là quán cà phê Gamadas——\nà không, là quán cà phê ga Ohimitera sao.」
- fix: 「Đây là quán cà phê Gamadas——\nà không, là quán cà phê ga Ohitoyo sao.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3223** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 『御一夜ステーションカフェ』\n御一夜の、驛たる、茶店。
- TW: 是“御一夜站咖啡廳”，也就是御一夜的驛站茶館。
- old_vn: 『Quán cà phê ga Ohimitera』\nQuán trà, dịch trạm của Ohimitera.
- fix: 『Quán cà phê ga Ohitoyo』\nQuán trà, dịch trạm của Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 3285** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜にはまだ、田舎の匂いも色濃いし。\nその上、真闇姉は常に早起きをしてもいるゆえ。
- TW: 畢竟御一夜的鄉村氣息還很濃厚。而真闇姐早上又習慣早起。
- old_vn: Ở Ohimitera, hương vị đồng quê vẫn còn rất đậm nét.\nHơn nữa, chị Mayami lại luôn dậy sớm.
- fix: Ở Ohitoyo, hương vị đồng quê vẫn còn rất đậm nét.\nHơn nữa, chị Mayami lại luôn dậy sớm.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 14. 02_Hibiki / 日々姫06_みくろ、来訪 (7 dòng)

**Key 1877** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「なんと、みくろか！\n御一夜まで尋ねてきてくれたのか」
- TW: 「什麼，是美玖路啊！都找到御一夜來了嗎」
- old_vn: 「Gì chứ, là Mikuro sao!\nCô ấy cất công đến tận Ohimitera tìm tôi à.」
- fix: 「Gì chứ, là Mikuro sao!\nCô ấy cất công đến tận Ohitoyo tìm tôi à.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1890** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「しかし、御一夜では人員的にも場所的にも厳しい。\n\x%l石造機関庫;#00ffc040;石造機関庫%l;#;はすでに満杯。ガマダス前にも場所はない」
- TW: 「但是御一夜的人手和空間都很有限。\x%l石造機関庫;#00ffc040;石製機車庫%l;#;已經滿了。ＧＡＭＡＤＵＳ前也沒地方了」
- old_vn: 「Nhưng ở Ohimitera thì cả nhân lực lẫn địa điểm đều rất khó khăn.\n\x%l石造機関庫;#00ffc040;Xưởng đầu máy bằng đá%l;#; đã kín chỗ rồi. Trước Gamadasu cũng không còn không gian.」
- fix: 「Nhưng ở Ohitoyo thì cả nhân lực lẫn địa điểm đều rất khó khăn.\n\x%l石造機関庫;#00ffc040;Xưởng đầu máy bằng đá%l;#; đã kín chỗ rồi. Trước Gamadasu cũng không còn không gian.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1922** (nhân vật: みくろ; nguồn old_vn: csv3)
- JP: 「本当は、御一夜鉄道にも乗りたかったんですけど」
- TW: 「其實，美玖路還想坐坐看御一夜鐵路的列車呢」
- old_vn: 「Thật ra, Mikuro cũng muốn đi thử Đường sắt Ohimitera nữa.」
- fix: 「Thật ra, Mikuro cũng muốn đi thử Đường sắt Ohitoyo nữa.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2099** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「御一夜でだったら成立すると！\n御一夜は、だってSLの町やけん」
- TW: 「在御一夜的話可以！因為御一夜是蒸汽機車之城嘛」
- old_vn: 「Nếu ở Ohimitera thì chắc chắn sẽ thành công!\nBởi vì Ohimitera là thành phố của đầu máy hơi nước mà.」
- fix: 「Nếu ở Ohitoyo thì chắc chắn sẽ thành công!\nBởi vì Ohitoyo là thành phố của đầu máy hơi nước mà.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 2374** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「『御一夜鉄道の現役蒸気機関士と御一夜市長も、\n[デゴイチ,2]d51の清掃に参加します』って！　そしたら出来るし」
- TW: 「然後就能到處宣傳“御一夜鐵路的現任蒸汽機車司機與御一夜市長也會來參加Ｄ５１的清掃”了！」
- old_vn: 「Thế là có thể tuyên truyền rằng 'Lái tàu hơi nước đương nhiệm của Đường sắt Ohimitera và Thị trưởng Ohimitera\ncũng tham gia dọn dẹp D51'! Như vậy thì làm được rồi.」
- fix: 「Thế là có thể tuyên truyền rằng 'Lái tàu hơi nước đương nhiệm của Đường sắt Ohitoyo và Thị trưởng Ohitoyo\ncũng tham gia dọn dẹp D51'! Như vậy thì làm được rồi.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2439** (nhân vật: みくろ; nguồn old_vn: csv3)
- JP: 「御一夜の温泉、みくろも入ってみたいですけど、\n帰れなくなったら、園に迷惑かけちゃいますし」
- TW: 「美玖路雖然也想泡御一夜的溫泉，但不回去的話會給動物園添麻煩的」
- old_vn: 「Mikuro cũng muốn thử tắm suối nước nóng ở Ohimitera lắm,\nnhưng nếu không về được thì sẽ làm phiền mọi người trong sở thú mất.」
- fix: 「Mikuro cũng muốn thử tắm suối nước nóng ở Ohitoyo lắm,\nnhưng nếu không về được thì sẽ làm phiền mọi người trong sở thú mất.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2504** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「メニューね？　御一夜鉄道のみんなで考えたの」
- TW: 「這些菜都是御一夜鐵路的大家一起想的哦」
- old_vn: 「Thực đơn này hả? Là do mọi người ở Đường sắt Ohimitera cùng nhau nghĩ ra đấy.」
- fix: 「Thực đơn này hả? Là do mọi người ở Đường sắt Ohitoyo cùng nhau nghĩ ra đấy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

### 15. 02_Hibiki / 日々姫06_日々姫の決断 (13 dòng)

**Key 2416** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「隈元銀行御一夜支店長としての宝生稀咲は、決して、\n一学園生の情報だけで行動を起こしたりはしない」
- TW: 「作為隈元銀行御一夜支行長的寶生稀咲是絕不會僅憑一個學生提供的訊息就採取行動的」
- old_vn: 「Với tư cách là Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto, Houshou Kisaki\ntuyệt đối sẽ không hành động chỉ dựa trên thông tin từ một học sinh đâu.」
- fix: 「Với tư cách là Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto, Houshou Kisaki\ntuyệt đối sẽ không hành động chỉ dựa trên thông tin từ một học sinh đâu.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2582** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「御一夜市と、御一夜鉄道。\nそして、わたし達みんなにとっての、最善です」
- TW: 「對御一夜市和御一夜鐵路，還有對我們大家“最好”」
- old_vn: 「Là tốt nhất cho thành phố Ohimitera và Đường sắt Ohimitera.\nVà cũng là tốt nhất cho tất cả chúng ta.」
- fix: 「Là tốt nhất cho thành phố Ohitoyo và Đường sắt Ohitoyo.\nVà cũng là tốt nhất cho tất cả chúng ta.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2589** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「僕という実質的な[よそもの,2]余所者が候補になって、\n御一夜の選挙で――勝てるのか？」
- TW: 「就算我這個事實上的外鄉人去當候選人，又真的能在御一夜的選舉中取勝嗎？」
- old_vn: 「Một kẻ thực chất là người ngoài như anh mà trở thành ứng cử viên,\nthì liệu có thể chiến thắng trong cuộc bầu cử ở Ohimitera không?」
- fix: 「Một kẻ thực chất là người ngoài như anh mà trở thành ứng cử viên,\nthì liệu có thể chiến thắng trong cuộc bầu cử ở Ohitoyo không?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2669** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「真闇姉さんに聞いてみるのが、一番いいと思います。\n御一夜の選挙のこと……多分、誰よりも詳しいですから」
- TW: 「我覺得去問問真闇姐最好。她大概比任何人都更清楚御一夜選舉的事」
- old_vn: 「Em nghĩ hỏi chị Mayami là tốt nhất.\nChuyện bầu cử ở Ohimitera……có lẽ chị ấy là người rành hơn bất cứ ai.」
- fix: 「Em nghĩ hỏi chị Mayami là tốt nhất.\nChuyện bầu cử ở Ohitoyo……có lẽ chị ấy là người rành hơn bất cứ ai.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2673** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「わたしの能力で、御一夜市長と御一夜鉄道社長とを、\nこれ以上兼務することは、とても困難だと感じています」
- TW: 「我認為以我的能力，要繼續兼任御一夜市長和鐵路公司社長會非常困難」
- old_vn: 「Với năng lực của em, việc tiếp tục kiêm nhiệm cả chức Thị trưởng Ohimitera và Giám đốc Đường sắt Ohimitera,\nem cảm thấy là vô cùng khó khăn.」
- fix: 「Với năng lực của em, việc tiếp tục kiêm nhiệm cả chức Thị trưởng Ohitoyo và Giám đốc Đường sắt Ohitoyo,\nem cảm thấy là vô cùng khó khăn.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng. Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2696** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「左様でしたら、わたくしも賛成です。日々姫であれば、\nよりよい御一夜を描いてくれると、確信できます」
- TW: 「既然如此，那我也贊成。我確信日日姬能把御一夜描繪成一個更好的地方」
- old_vn: 「Nếu vậy thì em cũng tán thành ạ. Nếu là Hibiki,\nem tin chắc rằng cô ấy sẽ vẽ nên một Ohimitera tốt đẹp hơn.」
- fix: 「Nếu vậy thì em cũng tán thành ạ. Nếu là Hibiki,\nem tin chắc rằng cô ấy sẽ vẽ nên một Ohitoyo tốt đẹp hơn.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2749** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「まして、御一夜鉄道において――ああ、いや、\n好意的に見れば、観光振興を見込んで……ではないか」
- TW: 「更何況還是在御一夜鐵路上——啊，不，從樂觀的角度來看，他們是看好觀光振興的發展前途……應該也不是啊」
- old_vn: 「Huống hồ lại là trên Đường sắt Ohimitera——À, không,\nnếu nhìn nhận một cách tích cực thì có lẽ họ đang kỳ vọng vào việc chấn hưng du lịch... chăng?」
- fix: 「Huống hồ lại là trên Đường sắt Ohitoyo——À, không,\nnếu nhìn nhận một cách tích cực thì có lẽ họ đang kỳ vọng vào việc chấn hưng du lịch... chăng?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2817** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「双鉄様を上回る能力の候補など、\n御一夜中をどう探しても見つからないでしょう」
- TW: 「而且能力在雙鐵少爺之上的候選人，哪怕找遍整個御一夜也找不到吧」
- old_vn: 「Một ứng cử viên có năng lực vượt trội hơn ngài Soutetsu,\ndù có tìm khắp Ohimitera cũng không thấy đâu.」
- fix: 「Một ứng cử viên có năng lực vượt trội hơn ngài Soutetsu,\ndù có tìm khắp Ohitoyo cũng không thấy đâu.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2926** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「隈銀が御一夜で？　何の広告をするというんだ？」
- TW: 「隈元銀行要在御一夜打廣告？他們要打什麼廣告？」
- old_vn: 「Ngân hàng Kumamoto mà lại quảng cáo ở Ohimitera sao? Bọn họ định quảng cáo cái gì cơ chứ?」
- fix: 「Ngân hàng Kumamoto mà lại quảng cáo ở Ohitoyo sao? Bọn họ định quảng cáo cái gì cơ chứ?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3167** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 無党派層を、賛成でも反対でもない人々の――\n彼らの判断を促すことが、御一夜の未来に繋がると。
- TW: 促使無黨派階層——那些既不贊成也不反對的人們做出決定，會直接聯繫到御一夜的未來。
- old_vn: Thúc đẩy sự phán đoán của những người không thuộc đảng phái nào, những người không tán thành cũng không phản đối——\nđiều đó sẽ kết nối với tương lai của Ohimitera.
- fix: Thúc đẩy sự phán đoán của những người không thuộc đảng phái nào, những người không tán thành cũng không phản đối——\nđiều đó sẽ kết nối với tương lai của Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3326** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜鉄道株式会社から見れば、\n投資のリスクをゼロにできてしまう、魅力的な額。
- TW: 從御一夜鐵路股份公司的角度來看，是一個零投資風險的極富魅力的金額。
- old_vn: Đứng từ góc độ của Công ty Cổ phần Đường sắt Ohimitera,\nđây là một con số hấp dẫn có thể đưa rủi ro đầu tư về mức 0.
- fix: Đứng từ góc độ của Công ty Cổ phần Đường sắt Ohitoyo,\nđây là một con số hấp dẫn có thể đưa rủi ro đầu tư về mức 0.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 3506** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 隈銀は言うまでもなく御一夜唯一の銀行だ。
- TW: 每個人都知道，隈元銀行是御一夜唯一一家銀行。
- old_vn: Không cần phải nói, Kumagin là ngân hàng duy nhất ở Ohimitera.
- fix: Không cần phải nói, Kumagin là ngân hàng duy nhất ở Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3628** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜に産まれ、御一夜に育ち、\n僕に御一夜を教えてくれた、[いもうと,1]義妹を。
- TW: 而是生在御一夜，長在御一夜，又告訴我何為御一夜的——我的義妹。
- old_vn: Sinh ra ở Ohimitera, lớn lên ở Ohimitera,\nvà là người đã dạy tôi về Ohimitera, em gái nuôi của tôi.
- fix: Sinh ra ở Ohitoyo, lớn lên ở Ohitoyo,\nvà là người đã dạy tôi về Ohitoyo, em gái nuôi của tôi.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 3 lần xuất hiện trong dòng. 3× Ohimitera (JP có 御一夜 3×); "em gái nuôi" (義妹) giữ nguyên — thuộc quyết 義 19/11, không phải đợt này.

### 16. 02_Hibiki / 日々姫07_姉の想い。妹の想い (6 dòng)

**Key 2166** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「象徴になるには、愛されるには――\n御一夜の、湯富院の手だけでは、足りない」
- TW: 「要成為象徵，要受到人們的熱愛——光靠御一夜，還有湯布院是不夠的」
- old_vn: 「Để trở thành biểu tượng, để được yêu mến——\nChỉ với bàn tay của Ohimitera, của Yufuin là chưa đủ」
- fix: 「Để trở thành biểu tượng, để được yêu mến——\nChỉ với bàn tay của Ohitoyo, của Yufuin là chưa đủ」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2247** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「メニューについては、御一夜ステーションカフェでの\nアンケートと、モニター調査もしています」
- TW: 「關於菜單，我在御一夜車站咖啡廳進行了問卷調查以及試吃調查」
- old_vn: 「Về thực đơn, em cũng đã làm khảo sát và điều tra thử nghiệm\ntại quán cà phê ga Ohimitera」
- fix: 「Về thực đơn, em cũng đã làm khảo sát và điều tra thử nghiệm\ntại quán cà phê ga Ohitoyo」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2402** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 地元の味を食べ損なう。\n御一夜に囚われたゆえ、僕らはその愚を犯しかけた。
- TW: 不能吃到本地的口味。因為被局限在御一夜之內，我們差點就要做出傻事了。
- old_vn: Lỡ mất cơ hội nếm thử hương vị địa phương.\nVì bị bó hẹp trong Ohimitera, chúng tôi suýt nữa đã phạm phải sai lầm đó.
- fix: Lỡ mất cơ hội nếm thử hương vị địa phương.\nVì bị bó hẹp trong Ohitoyo, chúng tôi suýt nữa đã phạm phải sai lầm đó.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2512** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜の特産、名産で、\nメニューを固めようとしていたのだから。
- TW: 因為我們本來也打算把菜單限定在御一夜的特色和名產上。
- old_vn: Bởi vì chúng tôi đã định cố định thực đơn\nbằng những đặc sản, danh sản của Ohimitera.
- fix: Bởi vì chúng tôi đã định cố định thực đơn\nbằng những đặc sản, danh sản của Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2604** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜の特産だけを主役としようと考えていた。\nアンケートさえ、御一夜でしか取ってなかった。
- TW: 我們只想著讓御一夜的特產做主角，就連問卷調查都只在御一夜舉行。
- old_vn: Chúng tôi đã nghĩ đến việc chỉ lấy đặc sản của Ohimitera làm nhân vật chính.\nThậm chí khảo sát cũng chỉ được thực hiện ở Ohimitera.
- fix: Chúng tôi đã nghĩ đến việc chỉ lấy đặc sản của Ohitoyo làm nhân vật chính.\nThậm chí khảo sát cũng chỉ được thực hiện ở Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 2605** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 見えてなかった。御一夜だけ。身の回りだけ。\nその上、目立つ部分だけしか。
- TW: 我們只關注御一夜，只關注身邊，甚至只關注其中最顯眼的事物。
- old_vn: Chúng tôi đã không nhìn thấy. Chỉ Ohimitera. Chỉ những thứ xung quanh.\nHơn nữa, chỉ những phần nổi bật.
- fix: Chúng tôi đã không nhìn thấy. Chỉ Ohitoyo. Chỉ những thứ xung quanh.\nHơn nữa, chỉ những phần nổi bật.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 17. 02_Hibiki / 日々姫08_とれいん食堂 (16 dòng)

**Key 1619** (nhân vật: 斎藤; nguồn old_vn: csv3)
- JP: 「……\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;いうんは凄かとですねぇ。\n御一夜では見たこともなかとでしたが」
- TW: 「……這個\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;真厲害啊。在御一夜就從來沒見過」
- old_vn: 「……\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; tuyệt thật đấy nhỉ.\nỞ Ohimitera tôi chưa từng thấy bao giờ.」
- fix: 「……\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; tuyệt thật đấy nhỉ.\nỞ Ohitoyo tôi chưa từng thấy bao giờ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2051** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「普通車としての湯医駅発が0545。御一夜着が0645。\n客扱いののち、食堂列車に変わっての発車が0700」
- TW: 「作為普通車從湯醫站始發的時間是０５４５。０６４５到達御一夜。客人上下車完成後，０７００變為食堂列車發車」
- old_vn: 「Khởi hành từ ga Yui với tư cách là tàu thường lúc 05:45. Đến Ohimitera lúc 06:45.\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」
- fix: 「Khởi hành từ ga Yui với tư cách là tàu thường lúc 05:45. Đến Ohitoyo lúc 06:45.\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2270** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「しあさって、八月二十八日のとれいん食堂指定券。\n食事付き。同日から有効の、湯富院-御一夜の乗車券」
- TW: 「大後天，八月二十八日的列車食堂指定票。附帶餐點。當日起有效的，湯布院至御一夜的車票」
- old_vn: 「Vé chỉ định Tàu nhà hàng ngày mốt, ngày 28 tháng 8.\nCó kèm bữa ăn. Vé lên tàu Yufuin - Ohimitera, có hiệu lực từ cùng ngày.」
- fix: 「Vé chỉ định Tàu nhà hàng ngày mốt, ngày 28 tháng 8.\nCó kèm bữa ăn. Vé lên tàu Yufuin - Ohitoyo, có hiệu lực từ cùng ngày.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2349** (nhân vật: 真闇; nguồn old_vn: csv3)
- JP: 「湯富院から、御一夜温泉まででお願いします」
- TW: 「從湯布院上車，在御一夜溫泉下車」
- old_vn: 「Từ Yufuin đến suối nước nóng Ohimitera nhé.」
- fix: 「Từ Yufuin đến suối nước nóng Ohitoyo nhé.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2535** (nhân vật: 斎藤; nguồn old_vn: csv3)
- JP: 「御一夜じゃあ、\nどう転んでも見れん景色ですけんねぇ」
- TW: 「畢竟在御一夜，無論如何都看不到那種景色啊」
- old_vn: 「Ở Ohimitera thì,\ncó làm thế nào cũng chẳng ngắm được cảnh đó đâu nhỉ」
- fix: 「Ở Ohitoyo thì,\ncó làm thế nào cũng chẳng ngắm được cảnh đó đâu nhỉ」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2633** (nhân vật: ふかみ; nguồn old_vn: csv3)
- JP: 「ありがとうございます。鮎と栗、それからなにより\nクマ焼酎は、御一夜の名物なんですよ」
- TW: 「謝謝誇獎。鯰魚和栗子，特別是隈燒酒，是御一夜的特產哦」
- old_vn: 「Cháu cảm ơn ạ. Cá hương, hạt dẻ, và trên hết là\nrượu Shochu Kuma, đều là đặc sản của Ohimitera đó ạ」
- fix: 「Cháu cảm ơn ạ. Cá hương, hạt dẻ, và trên hết là\nrượu Shochu Kuma, đều là đặc sản của Ohitoyo đó ạ」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2970** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 今日の御一夜駅改札は、新しい旅への送迎門だ。
- TW: 今天御一夜站的檢票口，是通往嶄新旅程的大門。
- old_vn: Cổng soát vé ga Ohimitera hôm nay, là cánh cổng đưa đón đến một hành trình mới.
- fix: Cổng soát vé ga Ohitoyo hôm nay, là cánh cổng đưa đón đến một hành trình mới.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3027** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 凪は民芸品置き場からけん玉をとり、\nふかみは書棚から御一夜史の冊子をとって。
- TW: 凪從民俗工藝品擺放區拿起了劍玉，而深美從書架上拿了講述御一夜歷史的讀物。
- old_vn: Nagi lấy Kendama từ khu vực đồ thủ công mỹ nghệ,\nFukami lấy cuốn sách lịch sử Ohimitera từ giá sách.
- fix: Nagi lấy Kendama từ khu vực đồ thủ công mỹ nghệ,\nFukami lấy cuốn sách lịch sử Ohitoyo từ giá sách.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3106** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: レールが繋がった効果によっての好影響で、\n御一夜の観光収入は右肩あがりを続けている。
- TW: 在鐵路連通帶來的正面影響下，御一夜的觀光收入一直在穩步提升。
- old_vn: Nhờ hiệu ứng tích cực từ việc kết nối đường ray,\ndoanh thu du lịch của Ohimitera vẫn tiếp tục tăng trưởng.
- fix: Nhờ hiệu ứng tích cực từ việc kết nối đường ray,\ndoanh thu du lịch của Ohitoyo vẫn tiếp tục tăng trưởng.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3111** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: しあさって――御一夜いきの一番列車ともならない、\nど平日発車の食堂列車。
- TW: 大後天的那班車已經不是發往御一夜的首班車，僅僅是平常日期的食堂列車。
- old_vn: Ngày mốt――Chuyến tàu nhà hàng khởi hành vào một ngày trong tuần,\nthậm chí còn chẳng phải chuyến tàu đầu tiên đi Ohimitera.
- fix: Ngày mốt――Chuyến tàu nhà hàng khởi hành vào một ngày trong tuần,\nthậm chí còn chẳng phải chuyến tàu đầu tiên đi Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3132** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 『湯医線沿線』だ。御一夜ではなく――8620ではなく。\n機関車保存体験という観光を、湯医線沿線へ持ち込めれば。
- TW: 她說的是“湯醫線沿線”而非御一夜——不是８６２０。她建議把機車保養體驗的觀光活動引入湯醫線沿線。
- old_vn: Là 『Dọc tuyến Yui』. Không phải Ohimitera――Không phải 8620.\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yui.
- fix: Là 『Dọc tuyến Yui』. Không phải Ohitoyo――Không phải 8620.\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yui.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3149** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜の魅力が知られれば、\nすぐにこちらも、満席続きとできるはずだ。
- TW: 得知了御一夜的魅力之後，這邊一定也會很前段班班客滿的。
- old_vn: Nếu sức hấp dẫn của Ohimitera được nhiều người biết đến,\nchắc chắn tuyến đường này cũng sẽ sớm liên tục cháy vé thôi.
- fix: Nếu sức hấp dẫn của Ohitoyo được nhiều người biết đến,\nchắc chắn tuyến đường này cũng sẽ sớm liên tục cháy vé thôi.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3495** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: なるほど確かに――今は普通列車扱いの、\n湯医-御一夜間さえも、観光列車区間とできるかもしれん。
- TW: 確實，現在只開行普通列車的湯醫—御一夜段，說不定也可以打造成觀光列車段。
- old_vn: Ra là vậy, quả thực――Ngay cả đoạn Yui - Ohimitera hiện đang chạy tàu thường,\ncũng có thể trở thành đoạn tàu du lịch.
- fix: Ra là vậy, quả thực――Ngay cả đoạn Yui - Ohitoyo hiện đang chạy tàu thường,\ncũng có thể trở thành đoạn tàu du lịch.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3719** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: （湯医）-御一夜-早戸間が御一夜鉄道。\n早戸-鹿兒島-千内-八ツ城-隈元までがみかん鉄道。
- TW: （湯醫）—御一夜—隼人段是御一夜鐵路。隼人—鹿兒島—川內—八代—隈元段是橙鐵路。
- old_vn: Đoạn (Yui) - Ohimitera - Hayato là của Đường sắt Ohito.\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- fix: Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohito.\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). JP là 御一夜鉄道 (tên công ty). "Đường sắt Ohito" trần trong cùng dòng KHÔNG đổi đợt này (T1-bare/T2, batch khác).

**Key 3736** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ＜39000円、 大人１。とれ食2号1号車4A。\n8/25　とれ食１号。御一夜車掌区乗務員発行＞
- TW: ＜３９０００日元，成人座一位。列車食堂２號１號車４Ａ。８／２５　列車食堂１號。御一夜列車長管區乘務員出票＞
- old_vn: ＜39.000 yên, 1 Người lớn. Tàu nhà hàng số 2, toa 1, 4A.\n25/8 Tàu nhà hàng số 1. Nhân viên phân khu trưởng tàu Ohimitera phát hành＞
- fix: ＜39.000 yên, 1 Người lớn. Tàu nhà hàng số 2, toa 1, 4A.\n25/8 Tàu nhà hàng số 1. Nhân viên phân khu trưởng tàu Ohitoyo phát hành＞
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3739** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ＜8月28日から有効　湯富院から御一夜温泉ゆき。\n経由（とれ食）、当日限り。乗車券のみ５日間有効＞
- TW: ＜８月２８日起生效　湯布院至御一夜溫泉。經由（列車食堂），餐點當日有效。車票５日內有效＞
- old_vn: ＜Có hiệu lực từ ngày 28 tháng 8, từ Yufuin đi suối nước nóng Ohimitera.\nChặng (Tàu nhà hàng), chỉ có giá trị trong ngày. Chỉ vé lên tàu có hiệu lực trong 5 ngày＞
- fix: ＜Có hiệu lực từ ngày 28 tháng 8, từ Yufuin đi suối nước nóng Ohitoyo.\nChặng (Tàu nhà hàng), chỉ có giá trị trong ngày. Chỉ vé lên tàu có hiệu lực trong 5 ngày＞
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 18. 02_Hibiki / 日々姫08_開きかけのつぼみ (4 dòng)

**Key 2172** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「いいと思います。遺恨が残るような選挙戦はのちのち、\n御一夜の発展を損ねる要因になってしまうと思いますし」
- TW: 「我贊成。若是在選舉過程中留下遺憾，也可能對御一夜的發展造成不利」
- old_vn: 「Chị nghĩ như vậy là tốt đấy. Một cuộc bầu cử để lại oán hận về sau,\nsẽ trở thành nguyên nhân gây tổn hại đến sự phát triển của Ohimitera.」
- fix: 「Chị nghĩ như vậy là tốt đấy. Một cuộc bầu cử để lại oán hận về sau,\nsẽ trở thành nguyên nhân gây tổn hại đến sự phát triển của Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2260** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「左様です、双鉄様。今は、御一夜-湯医だけの二駅。\nこのような心遣いは不要かもしれませんが――」
- TW: 「沒錯，雙鐵少爺。現在只有御一夜到湯醫這兩站，也許還不必擔心這種事。可是——」
- old_vn: 「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohimitera và Yui.\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」
- fix: 「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohitoyo và Yui.\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2369** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「わたしには重すぎたバトンを、拾ってくれてありがとう。\nどうか、御一夜市を――よろしくお願いいたします」
- TW: 「這擔子對我來說太重了，謝謝你肯把它挑起來。御一夜市就拜託你了」
- old_vn: 「Cảm ơn em đã nhặt lấy cây gậy tiếp sức quá đỗi nặng nề đối với chị.\nXin hãy chăm lo cho thành phố Ohimitera nhé――Trăm sự nhờ em.」
- fix: 「Cảm ơn em đã nhặt lấy cây gậy tiếp sức quá đỗi nặng nề đối với chị.\nXin hãy chăm lo cho thành phố Ohitoyo nhé――Trăm sự nhờ em.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2778** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 僕と日々姫とハチロクと――\n生まれ変わった御一夜を、\x%l8620;#00ffc040;8620%l;#;で駆け抜ける。
- TW: 我、日日姬和八六，我們一起駕駛著\x%l8620;#00ffc040;８６２０%l;#;駛過重生後的御一夜。
- old_vn: Tôi, Hibiki và Hachiroku――\nCùng nhau lái \x%l8620;#00ffc040;8620%l;#; băng qua Ohimitera đã được tái sinh.
- fix: Tôi, Hibiki và Hachiroku――\nCùng nhau lái \x%l8620;#00ffc040;8620%l;#; băng qua Ohitoyo đã được tái sinh.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 19. 02_Hibiki / 日々姫09_run_with_our_dreams (3 dòng)

**Key 1906** (nhân vật: ハチロク; nguồn old_vn: csv3)
- JP: 「旧帝鉄8620形蒸気機関車トップナンバーレイルロオド。\n現、御一夜鉄道の、ハチロクです」
- TW: 「我是前帝國鐵路８６２０型蒸汽機車首車鐵路人偶。現隸屬於御一夜鐵路，名叫八六」
- old_vn: 「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Hoàng gia cũ.\nHiện tại thuộc Đường sắt Ohimitera, Hachiroku ạ.」
- fix: 「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Hoàng gia cũ.\nHiện tại thuộc Đường sắt Ohitoyo, Hachiroku ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2400** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: その中の多くが、御一夜と離れているにも関わらず、\nトレインホステルを宿泊先に、わざわざ選んで下さった。
- TW: 可其中有很多人，還是特地在離御一夜比較遠的列車旅館訂了房。
- old_vn: Vậy mà trong số đó, dù ở cách xa Ohimitera,\nnhưng nhiều người đã cất công chọn khách sạn tàu hỏa làm nơi lưu trú.
- fix: Vậy mà trong số đó, dù ở cách xa Ohitoyo,\nnhưng nhiều người đã cất công chọn khách sạn tàu hỏa làm nơi lưu trú.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2708** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 湯医か鱈木か――トレインホステルの設置場所では、\n御一夜鉄道を二分しての大激論がかわされた。
- TW: 要把列車旅館放在湯醫還是多良木，這個問題讓御一夜鐵路內部分為兩派，引發了激烈的爭論。
- old_vn: Yui hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohimitera.
- fix: Yui hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

### 20. 02_Hibiki / 日々姫09_静かなる開戦 (17 dòng)

**Key 1459** (nhân vật: 債権者Ａ; nguồn old_vn: audit)
- JP: 「複数輌をまとめてってよ、\n御一夜鉄道にゃそぎゃんと多か車輌の必要――っ！」
- TW: 「一次搬運複數車輛？御一夜鐵路要這麼多車輛——！」
- old_vn: 「Bảo là di chuyển cùng lúc nhiều toa xe,\nchứ Đường sắt Ohimitera đâu cần nhiều toa xe đến thế——Ư!」
- fix: 「Bảo là di chuyển cùng lúc nhiều toa xe,\nchứ Đường sắt Ohitoyo đâu cần nhiều toa xe đến thế——Ư!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty). old_vn = giá trị audit fix (audit đã thêm Ư gasp "——Ư!" so với CSV3 "——!"); chỉ đổi Ohimitera→Ohitoyo trên giá trị audit.

**Key 1499** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「けれどお前には、言葉にはならぬ積み重ねがある。\nお前の瞳は、誰より多く、御一夜の綺麗を見つめてきた」
- TW: 「但是你有著其他日積月累的優勢。你對御一夜美好的一面的了解比任何人都深」
- old_vn: 「Nhưng em lại có những sự tích lũy không thể diễn tả bằng lời.\nĐôi mắt em đã ngắm nhìn vẻ đẹp của Ohimitera nhiều hơn bất kỳ ai.」
- fix: 「Nhưng em lại có những sự tích lũy không thể diễn tả bằng lời.\nĐôi mắt em đã ngắm nhìn vẻ đẹp của Ohitoyo nhiều hơn bất kỳ ai.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1548** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「それで私。宝生稀咲先輩の――隈元銀行御一夜支店長の、\n後輩――親しくしていただいている、後輩でもあります」
- TW: 「另外，我也是寶生稀咲學姐——隈元銀行御一夜支行行長的學妹，我和她關係非常親近」
- old_vn: 「Và cháu. Là hậu bối của đàn chị Houshou Kisaki——Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto——\ncháu cũng là một hậu bối khá thân thiết với chị ấy.」
- fix: 「Và cháu. Là hậu bối của đàn chị Houshou Kisaki——Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto——\ncháu cũng là một hậu bối khá thân thiết với chị ấy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1557** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「それでも、ポーレットさんを助けるために、\n私の好きな御一夜を守るために、私――」
- TW: 「可是，為了幫助波萊特小姐，為了保護我所喜歡的御一夜，我——」
- old_vn: 「Nhưng dù vậy, để giúp đỡ chị Paulette,\nđể bảo vệ Ohimitera mà cháu yêu quý, cháu——」
- fix: 「Nhưng dù vậy, để giúp đỡ chị Paulette,\nđể bảo vệ Ohitoyo mà cháu yêu quý, cháu——」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1662** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「ですが、以降は鉄道業に全力を傾注することにより、\n御一夜鉄道を通じた観光振興を必ずや実現して参ります」
- TW: 「從今以後，我會全心全意投入鐵路事業，力爭透過御一夜鐵路來振興旅遊業」
- old_vn: 「Tuy nhiên, từ nay về sau, bằng cách dốc toàn lực vào ngành đường sắt,\ntôi nhất định sẽ thực hiện được việc chấn hưng du lịch thông qua Đường sắt Ohimitera.」
- fix: 「Tuy nhiên, từ nay về sau, bằng cách dốc toàn lực vào ngành đường sắt,\ntôi nhất định sẽ thực hiện được việc chấn hưng du lịch thông qua Đường sắt Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1672** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「御一夜の衰退を見たくない、発展をしてほしい気持ち、\n私にも、もちろん、すごくあります」
- TW: 「我也不想看到御一夜衰落下去，我也非常希望御一夜變得更好」
- old_vn: 「Cháu không muốn thấy Ohimitera suy tàn, cháu muốn nơi này phát triển,\ntất nhiên, bản thân cháu cũng có mong muốn đó rất mãnh liệt.」
- fix: 「Cháu không muốn thấy Ohitoyo suy tàn, cháu muốn nơi này phát triển,\ntất nhiên, bản thân cháu cũng có mong muốn đó rất mãnh liệt.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1690** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「私、右田日々姫です。右田一酒造元の末娘で、\n御一夜鉄道株式会社の車輌部長で、見習い\x%l機関助士;#00ffc040;機関助士%l;#;で」
- TW: 「我叫右田日日姬，是右田一釀酒廠主人的次女，也是御一夜鐵路股份公司的車輛部長，兼任實習\x%l機関士;#00ffc040;司機%l;#;」
- old_vn: 「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita,\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohimitera, và là \x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」
- fix: 「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita,\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohitoyo, và là \x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1694** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「私、それをみんな――御一夜鉄道がらみのみんな、\n出来るだけ多くに検討して欲しいです」
- TW: 「我希望集合儘可能多的——御一夜鐵路的相關人員共同探討」
- old_vn: 「Em, muốn tất cả mọi người——những người liên quan đến Đường sắt Ohimitera,\ncàng nhiều người cùng xem xét ý tưởng đó càng tốt.」
- fix: 「Em, muốn tất cả mọi người——những người liên quan đến Đường sắt Ohitoyo,\ncàng nhiều người cùng xem xét ý tưởng đó càng tốt.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1721** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「当行は御一夜鉄道債の信用力に不安を感じておりません。\nが、この報道にあるご懸念は解消すべきかと考えます」
- TW: 「我行仍然相信御一夜鐵路債券。但是，我們認為有必要消除這篇文章提出的後顧之憂」
- old_vn: 「Ngân hàng chúng tôi không cảm thấy lo ngại về độ tin cậy của trái phiếu đường sắt Ohimitera.\nTuy nhiên, chúng tôi cho rằng cần phải giải tỏa những lo âu mà bài báo này nêu ra.」
- fix: 「Ngân hàng chúng tôi không cảm thấy lo ngại về độ tin cậy của trái phiếu đường sắt Ohitoyo.\nTuy nhiên, chúng tôi cho rằng cần phải giải tỏa những lo âu mà bài báo này nêu ra.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). JP là 御一夜鉄道 (tên công ty).

**Key 1723** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「わたしが市長と御一夜鉄道社長とを兼務したままでは、\nこれ以上の事業拡大は不可能だと判断しました」
- TW: 「我認為如果我繼續兼任市長和御一夜鐵路的社長的話，事業已經不可能再擴大了」
- old_vn: 「Tôi nhận định rằng, nếu tôi vẫn tiếp tục kiêm nhiệm cả chức thị trưởng và giám đốc Đường sắt Ohimitera,\nthì việc mở rộng kinh doanh hơn nữa là điều không thể.」
- fix: 「Tôi nhận định rằng, nếu tôi vẫn tiếp tục kiêm nhiệm cả chức thị trưởng và giám đốc Đường sắt Ohitoyo,\nthì việc mở rộng kinh doanh hơn nữa là điều không thể.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1749** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「絵を描け、日々姫。\nお前の描く、お前の夢見る御一夜の町の未来図を」
- TW: 「日日姬，把你心中描繪的，你夢想中的御一夜的未來畫出來吧」
- old_vn: 「Vẽ tranh đi, Hibiki.\nHãy vẽ bức tranh tương lai về thị trấn Ohimitera mà em hằng mơ ước.」
- fix: 「Vẽ tranh đi, Hibiki.\nHãy vẽ bức tranh tương lai về thị trấn Ohitoyo mà em hằng mơ ước.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1775** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「だから、環境を守るため。\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致無しでも、\n御一夜の経済に、必ず復活してほしくって」
- TW: 「為了保護環境，我想在不引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠的情況下重振御一夜的經濟」
- old_vn: 「Vì vậy, để bảo vệ môi trường. Dù không thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\ncháu vẫn mong kinh tế Ohimitera nhất định sẽ vực dậy.」
- fix: 「Vì vậy, để bảo vệ môi trường. Dù không thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\ncháu vẫn mong kinh tế Ohitoyo nhất định sẽ vực dậy.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1777** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「このご懸念を解消するため、隈元銀行といたしましては、\n御一夜鉄道様に対する特別金利にての融資の準備を――」
- TW: 「為了消除後顧之憂，隈元銀行準備以優惠利率向御一夜鐵道發放貸款——」
- old_vn: 「Để giải tỏa mối lo ngại này, Ngân hàng Kumamoto chúng tôi,\nđang chuẩn bị cung cấp khoản vay với lãi suất đặc biệt cho Đường sắt Ohimitera——」
- fix: 「Để giải tỏa mối lo ngại này, Ngân hàng Kumamoto chúng tôi,\nđang chuẩn bị cung cấp khoản vay với lãi suất đặc biệt cho Đường sắt Ohitoyo——」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 1892** (nhân vật: 債権者Ａ; nguồn old_vn: csv3)
- JP: 「鉄工と木工のごつ、御一夜で賄える技術ばい」
- TW: 「鐵工和木工在御一夜完全能找齊咧」
- old_vn: 「Sắt với mộc thì Ohimitera dư sức lo được.」
- fix: 「Sắt với mộc thì Ohitoyo dư sức lo được.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2068** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 今の、迷える御一夜の、\n大きな力に、支えへと、きっと育っていく筈だ。
- TW: 一定會成長為強大的力量，支撐起如今失去了方向的御一夜。
- old_vn: Chắc chắn sẽ lớn lên thành một sức mạnh to lớn,\nthành điểm tựa cho một Ohimitera đang lạc lối hiện tại.
- fix: Chắc chắn sẽ lớn lên thành một sức mạnh to lớn,\nthành điểm tựa cho một Ohitoyo đang lạc lối hiện tại.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2333** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 確か、御一夜の職人さんたちのお一人だ。\n協力をして頂いたのに不安を与え、素直に申し訳なく思う。
- TW: 我記得他是御一夜的工匠。他幫助了我們，而我們卻讓他感到了不安，我真的覺得很抱歉。
- old_vn: Nếu tôi nhớ không lầm, ông ấy là một trong những nghệ nhân của Ohimitera.\nĐã nhờ họ hợp tác mà lại khiến họ bất an, tôi thực sự thấy có lỗi.
- fix: Nếu tôi nhớ không lầm, ông ấy là một trong những nghệ nhân của Ohitoyo.\nĐã nhờ họ hợp tác mà lại khiến họ bất an, tôi thực sự thấy có lỗi.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2586** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 語る稀咲を飾るのは、\n『隈元銀行御一夜支店長　宝生稀咲』の文字列だ。
- TW: 稀咲下面打出的字幕是“隈元銀行御一夜支行行長寶生稀咲”。
- old_vn: Dòng chữ tô điểm cho Kisaki đang phát biểu là\n『Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto - Houshou Kisaki』.
- fix: Dòng chữ tô điểm cho Kisaki đang phát biểu là\n『Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto - Houshou Kisaki』.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 21. 02_Hibiki / 日々姫10_稀咲の未来図、日々姫の未来図 (24 dòng)

**Key 2258** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「交通にも、御一夜の発展のためにも、\nどんなことにも、複数経路がある方がいい」
- TW: 「不管是交通還是御一夜的發展，什麼東西都要有複數的道路才好」
- old_vn: 「Dù là giao thông, hay sự phát triển của Ohimitera,\nbất cứ việc gì cũng nên có nhiều con đường.」
- fix: 「Dù là giao thông, hay sự phát triển của Ohitoyo,\nbất cứ việc gì cũng nên có nhiều con đường.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2385** (nhân vật: 真闇; nguồn old_vn: csv3)
- JP: 「任せたいのは、御一夜の未来」
- TW: 「咱想交給你的是，御一夜的未來」
- old_vn: 「Điều chị muốn giao phó cho em, là tương lai của Ohimitera.」
- fix: 「Điều chị muốn giao phó cho em, là tương lai của Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2519** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致とあわせ、御一夜発展のための、\nそれこそ車の両輪になれば良いかと感じています」
- TW: 「如果能和\x%lエアクラ;#00ffc040;空凝機%l;#;工廠引進計劃合起來，共同成為發展御一夜的兩個車輪就好了」
- old_vn: 「Cùng với việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\ntôi cảm thấy nếu nó trở thành hai bánh xe thúc đẩy sự phát triển của Ohimitera thì thật tốt.」
- fix: 「Cùng với việc thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\ntôi cảm thấy nếu nó trở thành hai bánh xe thúc đẩy sự phát triển của Ohitoyo thì thật tốt.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2523** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「この地図にひとつ、お前の大好きな御一夜を\n加えるのなら、なにがいい？」
- TW: 「如果要在這地圖上加一點“你最喜歡的御一夜”，加什麼好呢？」
- old_vn: 「Nếu được thêm một nơi mà em yêu thích nhất ở Ohimitera\\nvào bản đồ này, em sẽ chọn gì?」
- fix: 「Nếu được thêm một nơi mà em yêu thích nhất ở Ohitoyo\\nvào bản đồ này, em sẽ chọn gì?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2585** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「そうした市政が、いずれ御一夜を――\n誰もが笑顔で暮らせる町に育てていくと思います」
- TW: 「我想這樣的市政總有一天會讓御一夜——逐漸變成一個誰都能滿面笑容地生活的城市」
- old_vn: 「Tôi tin rằng một chính quyền như vậy, rồi sẽ đưa Ohimitera――\nphát triển thành một thị trấn nơi mọi người đều có thể sống với nụ cười trên môi.」
- fix: 「Tôi tin rằng một chính quyền như vậy, rồi sẽ đưa Ohitoyo――\nphát triển thành một thị trấn nơi mọi người đều có thể sống với nụ cười trên môi.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2592** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「私、描けんけんっ！　期待して、任せてもらって――\nそれなのに、御一夜の未来図、描けんけんっ！！！」
- TW: 「我畫不出來！大家滿懷期待、交給我這個重任——但我卻畫不出御一夜的未來圖景來！！！」
- old_vn: 「Em, không vẽ được! Mọi người đã kỳ vọng, đã giao phó cho em――\nVậy mà, bức tranh tương lai của Ohimitera, em không vẽ được!!!」
- fix: 「Em, không vẽ được! Mọi người đã kỳ vọng, đã giao phó cho em――\nVậy mà, bức tranh tương lai của Ohitoyo, em không vẽ được!!!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2613** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「このレイアウトに継ぎ足しをして巨大な御一夜市――\nいや、いっそ湯医線沿線の広域モデルを作る」
- TW: 「把這個場景模型繼續改造成巨大的御一夜市——不，索性就做成連湯醫線沿線都包括進去的廣域模型」
- old_vn: 「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohimitera khổng lồ——\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yui đi.」
- fix: 「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohitoyo khổng lồ——\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yui đi.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2623** (nhân vật: 真闇; nguồn old_vn: csv3)
- JP: 「観光を捨てて、工業都市として御一夜ば再生させる。\n技師や職人には、むしろ魅力的なプランよね」
- TW: 「放棄觀光，讓御一夜作為工業都市獲得新生。對技師和工匠來說倒不如這個方案更有魅力呢」
- old_vn: 「Từ bỏ du lịch, tái thiết Ohimitera thành một thành phố công nghiệp.\\nĐối với các kỹ sư và nghệ nhân, đây quả là một kế hoạch hấp dẫn.」
- fix: 「Từ bỏ du lịch, tái thiết Ohitoyo thành một thành phố công nghiệp.\\nĐối với các kỹ sư và nghệ nhân, đây quả là một kế hoạch hấp dẫn.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2641** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「隈元銀行御一夜支店のロビーで明日から公開しますので。\n『\x%lエアクラ;#00ffc040;エアクラ%l;#;シティ御一夜』を、是非見て頂きたいですね」
- TW: 「明天就會在隈元銀行御一夜支行的大廳裡公開。我想您一定要看一看這座“\x%lエアクラ;#00ffc040;空凝機%l;#;之城御一夜”」
- old_vn: 「Từ ngày mai, nó sẽ được trưng bày tại sảnh chi nhánh Ohimitera của Ngân hàng Kumamoto.\nRất mong mọi người sẽ đến xem 『Thành phố \x%lエアクラ;#00ffc040;Aircra%l;#; Ohimitera』.」
- fix: 「Từ ngày mai, nó sẽ được trưng bày tại sảnh chi nhánh Ohitoyo của Ngân hàng Kumamoto.\nRất mong mọi người sẽ đến xem 『Thành phố \x%lエアクラ;#00ffc040;Aircra%l;#; Ohitoyo』.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 2695** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「そこに『自分の好きな御一夜の景色』を加えてもらう。\n誰にでも、気楽にやれる形がいい。具体的には――」
- TW: 「然後請大家在這上面加上“自己喜歡的御一夜的景色”。就用這種不論是誰都能輕鬆參與的模式吧。具體來說——」
- old_vn: 「Rồi để mọi người thêm 『khung cảnh Ohimitera yêu thích của mình』 vào đó.\\nPhải làm sao cho ai cũng có thể dễ dàng tham gia. Cụ thể là——」
- fix: 「Rồi để mọi người thêm 『khung cảnh Ohitoyo yêu thích của mình』 vào đó.\\nPhải làm sao cho ai cũng có thể dễ dàng tham gia. Cụ thể là——」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2703** (nhân vật: れいな; nguồn old_vn: csv3)
- JP: 「れいな、もーっとおっきい御一夜の中で、\nレイナナが走るのを見てみたいですぅ！」
- TW: 「玲奈也想開著０７在更大的御一夜城裡轉轉！」
- old_vn: 「Reina cũng muốn thấy KiHa 07\\nchạy trong một Ohimitera rộng lớn hơn nha!」
- fix: 「Reina cũng muốn thấy KiHa 07\\nchạy trong một Ohitoyo rộng lớn hơn nha!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2704** (nhân vật: れいな; nguồn old_vn: csv3)
- JP: 「れいなもですよぉ。あのミニチュアの御一夜市に、\n\x%lキハ07;#00ffc040;キハ07%l;#;も走らせてあげてほしいですぅ」
- TW: 「玲奈也是。玲奈真想讓\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;在那個迷你模型裡跑跑看」
- old_vn: 「Reina cũng vậy đó ạ~ Reina cũng muốn cho \x%lキハ07;#00ffc040;KiHa 07%l;#;\nchạy trong mô hình thành phố Ohimitera thu nhỏ đó nha~」
- fix: 「Reina cũng vậy đó ạ~ Reina cũng muốn cho \x%lキハ07;#00ffc040;KiHa 07%l;#;\nchạy trong mô hình thành phố Ohitoyo thu nhỏ đó nha~」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). TW lược tên địa danh (không có 御一夜) — JP có 御一夜, JP thắng TW, vẫn sửa.

**Key 2753** (nhân vật: 浦上; nguồn old_vn: csv3)
- JP: 「エアロ＝クラフテック社は旧来の交通機関との共存を\n目指しています。御一夜に限っての話ではありません」
- TW: 「空凝科技公司一直以與舊有的交通工具共存為目標。並不是僅限於御一夜一個地方」
- old_vn: 「Công ty Aero-Craftech luôn hướng tới sự cộng sinh với các phương tiện giao thông truyền thống.\nĐây không phải là câu chuyện chỉ giới hạn ở Ohimitera.」
- fix: 「Công ty Aero-Craftech luôn hướng tới sự cộng sinh với các phương tiện giao thông truyền thống.\nĐây không phải là câu chuyện chỉ giới hạn ở Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2770** (nhân vật: 真闇; nguồn old_vn: csv3)
- JP: 「そこに、『\x%lエアクラ;#00ffc040;エアクラ%l;#;シティ御一夜』\nこの都市モデルが後押しばしてきよるけんねぇ」
- TW: 「而且，那座“\x%lエアクラ;#00ffc040;空凝機%l;#;之城御一夜”的城市模型也在後面做推手呢」
- old_vn: 「Đã vậy, lại còn có mô hình đô thị\\n『Thành phố \\x%lエアクラ;#00ffc040;Aircra%l;#; Ohimitera』 hậu thuẫn nữa chứ.」
- fix: 「Đã vậy, lại còn có mô hình đô thị\\n『Thành phố \\x%lエアクラ;#00ffc040;Aircra%l;#; Ohitoyo』 hậu thuẫn nữa chứ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2852** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「御一夜鉄道株式会社様の\x%l8620;#00ffc040;8620%l;#;をイメージしてます。\n工場誘致で住宅圏が広がれば、鉄道の重要性も増します」
- TW: 「這是以御一夜鐵路股份公司的\x%l8620;#00ffc040;８６２０%l;#;為藍本的。如果引進工廠後住宅圈變大了，鐵路的重要性也會增加的」
- old_vn: 「Đó là hình ảnh mô phỏng \x%l8620;#00ffc040;8620%l;#; của Công ty Cổ phần Đường sắt Ohimitera.\nNếu khu dân cư được mở rộng nhờ việc thu hút nhà máy, tầm quan trọng của đường sắt cũng sẽ tăng lên.」
- fix: 「Đó là hình ảnh mô phỏng \x%l8620;#00ffc040;8620%l;#; của Công ty Cổ phần Đường sắt Ohitoyo.\nNếu khu dân cư được mở rộng nhờ việc thu hút nhà máy, tầm quan trọng của đường sắt cũng sẽ tăng lên.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2854** (nhân vật: 記者Ａ; nguồn old_vn: csv3)
- JP: 「\x%lエアクラ;#00ffc040;エアクラ%l;#;の作動不能地帯を抱える御一夜ならでは、\nの重要性となりますか」
- TW: 「這是有著許多\x%lエアクラ;#00ffc040;空凝機%l;#;無法運行地帶的御一夜特有的重要性吧」
- old_vn: 「Tầm quan trọng đó,\nchỉ có ở một nơi có khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động như Ohimitera thôi sao?」
- fix: 「Tầm quan trọng đó,\nchỉ có ở một nơi có khu vực \x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động như Ohitoyo thôi sao?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2856** (nhân vật: 記者Ａ; nguồn old_vn: csv3)
- JP: 「御一夜鉄道さんの動きも、それでは、\n隈銀さんが関与されてのものなのですかね？」
- TW: 「這次御一夜鐵路的一些動作，是隈元銀行也有參與的嗎？」
- old_vn: 「Vậy thì, những động thái của Đường sắt Ohimitera,\ncũng có sự can thiệp của Ngân hàng Kumamoto sao?」
- fix: 「Vậy thì, những động thái của Đường sắt Ohitoyo,\ncũng có sự can thiệp của Ngân hàng Kumamoto sao?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Dạng "Đường sắt Ohimitera"→"Đường sắt Ohitoyo" (cùng phép thay T1; cũng thỏa dạng T2). JP là 御一夜鉄道 (tên công ty).

**Key 2920** (nhân vật: ふかみ; nguồn old_vn: audit)
- JP: 「この都市モデルも綺麗。です。けど！\n御一夜の自然とクマ川の水の方が、もっと綺麗。です！」
- TW: 「雖然這座城市模型是很漂亮，但是御一夜的自然與隈河的水更漂亮。嗯！」
- old_vn: 「Mô hình đô thị này cũng đẹp thật ạ. Nhưng!\\nThiên nhiên Ohimitera và nước sông Kuma còn đẹp hơn nhiều ạ!」
- fix: 「Mô hình đô thị này cũng đẹp thật ạ. Nhưng!\\nThiên nhiên Ohitoyo và nước sông Kuma còn đẹp hơn nhiều ạ!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). old_vn = giá trị audit fix (audit đã viết lại câu so với CSV3); chỉ đổi Ohimitera→Ohitoyo trên giá trị audit.

**Key 2938** (nhân vật: 記者Ａ; nguồn old_vn: csv3)
- JP: 「まず、立候補会見の際に打ち出してらした都市計画、\n『エアクラシティ御一夜』についてお伺いできればと」
- TW: 「首先，我想問您一下您在宣布參選的時候打出的都市計劃“空凝機之城御一夜”的有關情報」
- old_vn: 「Đầu tiên, tôi muốn hỏi về dự án quy hoạch đô thị\n『Thành phố Aircra Ohimitera』 mà cô đã đưa ra trong buổi họp báo tranh cử.」
- fix: 「Đầu tiên, tôi muốn hỏi về dự án quy hoạch đô thị\n『Thành phố Aircra Ohitoyo』 mà cô đã đưa ra trong buổi họp báo tranh cử.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3112** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 自分の大好きな御一夜の景色とは、\nその人の一番大事な思い出にほぼ等しいのか。
- TW: 一個人最喜歡的御一夜的景色，幾乎就等於是對那個人來說最重要的回憶。
- old_vn: Khung cảnh Ohimitera mà mình yêu thích nhất,\\ngần như đồng nghĩa với kỷ niệm quý giá nhất của người đó sao.
- fix: Khung cảnh Ohitoyo mà mình yêu thích nhất,\\ngần như đồng nghĩa với kỷ niệm quý giá nhất của người đó sao.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3135** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: が、よくよく見れば、このジオラマは\n懐かしい……御一夜の、昔の風景にしか思えなくなる。
- TW: 不過，仔細研究一番後，讓人覺得這座模型真是充滿了懷念感……完全讓人覺得這就是過去的御一夜風景。
- old_vn: Nhưng, nhìn kỹ lại thì, mô hình sa bàn này\\nthật hoài niệm... khiến tôi không thể không nghĩ đến khung cảnh Ohimitera ngày xưa.
- fix: Nhưng, nhìn kỹ lại thì, mô hình sa bàn này\\nthật hoài niệm... khiến tôi không thể không nghĩ đến khung cảnh Ohitoyo ngày xưa.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3287** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 失われた鉄道風景――その一言で確信できた。\nこのレイアウトは、やはりかつての御一夜の光景なのだと。
- TW: 失去的鐵路風景——這一句話讓我確信了。這座場景模型果然就是過去的御一夜的風景。
- old_vn: Khung cảnh đường sắt đã mất——chỉ một câu nói đó thôi đã đủ để tôi tin chắc.\\nSa bàn này, quả nhiên là khung cảnh Ohimitera ngày xưa.
- fix: Khung cảnh đường sắt đã mất——chỉ một câu nói đó thôi đã đủ để tôi tin chắc.\\nSa bàn này, quả nhiên là khung cảnh Ohitoyo ngày xưa.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3496** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 僕らが作ろうとする御一夜を、\n日々姫は絵で、示してくれるはずだった。
- TW: 日日姬本應該用畫來展示出我們打算創造的御一夜的。
- old_vn: Một Ohimitera mà chúng tôi đang nỗ lực tạo ra,\nđáng lẽ Hibiki đã phải thể hiện nó qua bức tranh.
- fix: Một Ohitoyo mà chúng tôi đang nỗ lực tạo ra,\nđáng lẽ Hibiki đã phải thể hiện nó qua bức tranh.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3774** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 1/1000スケールの都市モデル――\n現在の御一夜ではなく、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致後の。
- TW: １/１０００比例的城市模型——不是現在的御一夜，而是引進\x%lエアクラ;#00ffc040;空凝機%l;#;工廠之後的。
- old_vn: Mô hình đô thị tỷ lệ 1/1000――\nKhông phải là Ohimitera hiện tại, mà là sau khi thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.
- fix: Mô hình đô thị tỷ lệ 1/1000――\nKhông phải là Ohitoyo hiện tại, mà là sau khi thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 22. 02_Hibiki / 日々姫11_御一夜モザイク (12 dòng)

**Key 1480** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「――そのモザイクは絶対に、\nすごく素敵な、御一夜の未来図になるから」
- TW: 「——這張鑲嵌畫肯定會成為一張非常精彩的御一夜未來圖景」
- old_vn: 「——Bức khảm đó tuyệt đối,\\nsẽ trở thành một bản đồ tương lai vô cùng tuyệt vời của Ohimitera.」
- fix: 「——Bức khảm đó tuyệt đối,\\nsẽ trở thành một bản đồ tương lai vô cùng tuyệt vời của Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1989** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「御一夜モザイク――\nみんなの希望をつなぎあわせた未来図か」
- TW: 「御一夜鑲嵌畫——由大家的期望拼合而成的未來圖景」
- old_vn: 「Bức khảm Ohimitera——\\nBản đồ tương lai kết nối hy vọng của mọi người sao.」
- fix: 「Bức khảm Ohitoyo——\\nBản đồ tương lai kết nối hy vọng của mọi người sao.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1996** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「『みんなでつくろう御一夜未来レイアウト』が\nどういうものか、もうご存知ですか？」
- TW: 「您是否已經了解“大家一起來設計·御一夜未來場景模型”是個怎樣的活動？」
- old_vn: 「Quý khách đã biết 『Cùng nhau tạo nên sa bàn tương lai Ohimitera』\\nlà như thế nào chưa ạ?」
- fix: 「Quý khách đã biết 『Cùng nhau tạo nên sa bàn tương lai Ohitoyo』\\nlà như thế nào chưa ạ?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2095** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「はい、御一夜の町に重点を置き、そこから湯医線沿線の\n光景を、簡略化してジオラマでつくり上げる計画です」
- TW: 「是的。我們計劃以御一夜城區為重點，把御一夜城區和湯醫線的沿線風景簡化成微縮景觀模型」
- old_vn: 「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohimitera, từ đó\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yui ạ.」
- fix: 「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohitoyo, từ đó\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yui ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2136** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「そうしてみんなで作った御一夜からの立体未来図上に、\n僕らの\x%l列車;#00ffc040;列車%l;#;を、一足早く走らせよう――と考えています」
- TW: 「然後儘可能快地讓我們的\x%l列車;#00ffc040;列車%l;#;跑在大家一起創作出的立體未來圖景上」
- old_vn: 「Và trên bản đồ tương lai 3D của Ohimitera do mọi người cùng nhau tạo ra đó,\\nchúng cháu dự định sẽ cho \\x%l列車;#00ffc040;đoàn tàu%l;#; của chúng ta chạy thử một bước trước——là như vậy ạ.」
- fix: 「Và trên bản đồ tương lai 3D của Ohitoyo do mọi người cùng nhau tạo ra đó,\\nchúng cháu dự định sẽ cho \\x%l列車;#00ffc040;đoàn tàu%l;#; của chúng ta chạy thử một bước trước——là như vậy ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). TW lược tên địa danh (không có 御一夜) — JP có 御一夜, JP thắng TW, vẫn sửa.

**Key 2143** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「はい。御一夜の未来図を、みんなで、\n模型で作りあげよう――ということをしています」
- TW: 「當然沒問題。我們是想讓大家用模型來製作御一夜的未來圖景」
- old_vn: 「Vâng. Chúng cháu đang cùng nhau tạo ra\\nbản đồ tương lai của Ohimitera bằng mô hình——là như vậy ạ.」
- fix: 「Vâng. Chúng cháu đang cùng nhau tạo ra\\nbản đồ tương lai của Ohitoyo bằng mô hình——là như vậy ạ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2260** (nhân vật: ポーレット; nguồn old_vn: csv3)
- JP: 「それはですね、わたしたちの――\n御一夜のみんなの力の結晶なんです」
- TW: 「這是我們的——御一夜眾人的功勞」
- old_vn: 「Đó là vì, đây là kết tinh sức mạnh của chúng ta——\\ncủa tất cả mọi người ở Ohimitera.」
- fix: 「Đó là vì, đây là kết tinh sức mạnh của chúng ta——\\ncủa tất cả mọi người ở Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2464** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 基本的には御一夜の変化を求めない彼らが、\n参入余地も無い\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致に積極的である筈がない。
- TW: 他們傾向於不改變御一夜，根本不會積極支持他們參與不了的\x%lエアクラ;#00ffc040;空凝機%l;#;工廠引進計劃。
- old_vn: Về cơ bản, họ không mong muốn Ohimitera thay đổi,\\nnên chắc chắn họ không thể nào tích cực ủng hộ việc thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà họ chẳng có chút cơ hội nào chen chân vào.
- fix: Về cơ bản, họ không mong muốn Ohitoyo thay đổi,\\nnên chắc chắn họ không thể nào tích cực ủng hộ việc thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà họ chẳng có chút cơ hội nào chen chân vào.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2483** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜市内だけでは、足りない。\n線路は続き、線路は繋ぐものだから。
- TW: 光有御一夜市區是不夠的。鐵路是延續的，是相連的。
- old_vn: Nếu chỉ có khu vực nội thành Ohimitera thì không đủ.\\nBởi vì đường ray là thứ kéo dài và kết nối mọi thứ lại với nhau.
- fix: Nếu chỉ có khu vực nội thành Ohitoyo thì không đủ.\\nBởi vì đường ray là thứ kéo dài và kết nối mọi thứ lại với nhau.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2531** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: じつに、嬉しい。\n見知らぬ誰かの描く“夢の御一夜”のその中に。
- TW: 在素不相識的人們描繪出的“夢想中的御一夜”裡，鐵路和\x%l8620;#00ffc040;８６２０%l;#;有機會大顯身手。
- old_vn: Thực sự rất vui.\\nTrong "Ohimitera mơ ước" do một người xa lạ nào đó vẽ nên.
- fix: Thực sự rất vui.\\nTrong "Ohitoyo mơ ước" do một người xa lạ nào đó vẽ nên.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2804** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: その考えに僕を及ばせてくれたのもまた、\n今の御一夜を愛し、そこに暮らしている人たちだ。
- TW: 是那些生活在如今的御一夜，愛著這裡的人們讓我有了這種想法。
- old_vn: Và những người đã khiến tôi có suy nghĩ đó,\\nchính là những người yêu mến Ohimitera hiện tại, và đang sống ở nơi đây.
- fix: Và những người đã khiến tôi có suy nghĩ đó,\\nchính là những người yêu mến Ohitoyo hiện tại, và đang sống ở nơi đây.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3032** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: （今のここにある御一夜を、クマ川を守るということは、\n歴史を守ると同時に、未来を作ることにもなる）
- TW: （保護當今的這個御一夜和隈河，既是在保護歷史，也是在開創未來）
- old_vn: （Bảo vệ Ohimitera hiện tại, bảo vệ sông Kuma,\\nkhông chỉ là bảo vệ lịch sử, mà còn là kiến tạo tương lai.）
- fix: （Bảo vệ Ohitoyo hiện tại, bảo vệ sông Kuma,\\nkhông chỉ là bảo vệ lịch sử, mà còn là kiến tạo tương lai.）
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 23. 02_Hibiki / 日々姫13_討論会 (19 dòng)

**Key 945** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「――だから、御一夜は大丈夫です。\n工場になんて頼らなくても、もっと素敵な町になります」
- TW: 「——不用擔心御一夜。就算沒有工廠，它也會變成一座更加美好的城市」
- old_vn: 「――Vì vậy, Ohimitera sẽ ổn thôi.\nKhông cần dựa dẫm vào nhà máy, nó sẽ trở thành một thị trấn tuyệt vời hơn nữa.」
- fix: 「――Vì vậy, Ohitoyo sẽ ổn thôi.\nKhông cần dựa dẫm vào nhà máy, nó sẽ trở thành một thị trấn tuyệt vời hơn nữa.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 947** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「――いろんな思いがあって、いろんな建物があって、\nそれで、今の御一夜が出来上がっている――」
- TW: 「——各種回憶，各種建築構成了如今的御一夜——」
- old_vn: 「――Có rất nhiều tâm tư, có rất nhiều tòa nhà,\nvà nhờ đó, mới tạo nên Ohimitera của hiện tại――」
- fix: 「――Có rất nhiều tâm tư, có rất nhiều tòa nhà,\nvà nhờ đó, mới tạo nên Ohitoyo của hiện tại――」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 955** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「――このレイアウトは、みなさんの手によって作られた、\nみなさんが描いてくれた、御一夜の未来図です」
- TW: 「——這個場景模型是由大家創作而成，大家描繪出的御一夜的未來圖景」
- old_vn: 「――Sa bàn này được tạo ra bởi chính bàn tay của mọi người,\nlà bức tranh tương lai của Ohimitera do mọi người vẽ nên.」
- fix: 「――Sa bàn này được tạo ra bởi chính bàn tay của mọi người,\nlà bức tranh tương lai của Ohitoyo do mọi người vẽ nên.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1206** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「そして必ず、御一夜の今と重ねていこう」
- TW: 「一定要將御一夜引向那個未來」
- old_vn: 「Và nhất định, phải kết nối nó với Ohimitera hiện tại.」
- fix: 「Và nhất định, phải kết nối nó với Ohitoyo hiện tại.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1222** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「いいえ、先輩。わたしは、見たものしか描けません。\nこれが、現実の御一夜なんです」
- TW: 「不，學姐。我只會畫我看到的東西。這就是真實的御一夜」
- old_vn: 「Không đâu, tiền bối. Tôi chỉ có thể vẽ những gì mình nhìn thấy.\nĐây chính là Ohimitera của hiện thực.」
- fix: 「Không đâu, tiền bối. Tôi chỉ có thể vẽ những gì mình nhìn thấy.\nĐây chính là Ohitoyo của hiện thực.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1234** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「各地の繁栄を支えるために、\n御一夜が犠牲になるのは、おかしな話だ」
- TW: 「但為了其他地區的繁榮而犧牲御一夜，這講不過去」
- old_vn: 「Để hỗ trợ sự phồn vinh của các địa phương khác,\nmà Ohimitera phải hy sinh thì thật là nực cười.」
- fix: 「Để hỗ trợ sự phồn vinh của các địa phương khác,\nmà Ohitoyo phải hy sinh thì thật là nực cười.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1236** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「けど緩やかな変化だからこそ――そこに描かれる未来は、\n御一夜の今と、歪むことなくつながります」
- TW: 「但這種緩慢的變化會為御一夜帶來我們共同希冀的未來」
- old_vn: 「Nhưng chính vì là sự thay đổi chậm rãi――tương lai được vẽ ra ở đó,\nsẽ kết nối với Ohimitera hiện tại mà không hề bị bóp méo.」
- fix: 「Nhưng chính vì là sự thay đổi chậm rãi――tương lai được vẽ ra ở đó,\nsẽ kết nối với Ohitoyo hiện tại mà không hề bị bóp méo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1239** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「思いませんか？\n現実は――今の御一夜は、綺麗って」
- TW: 「你不覺得現在的御一夜很美嗎？」
- old_vn: 「Cô không nghĩ vậy sao?\nHiện thực――Ohimitera hiện tại, rất đẹp.」
- fix: 「Cô không nghĩ vậy sao?\nHiện thực――Ohitoyo hiện tại, rất đẹp.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1390** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「多くの市民の皆様とは、はじめましてになりますね。\nボクの名前は宝生稀咲。御一夜市長選の立候補者です」
- TW: 「很多市民和我是第一次見面吧。我叫寶生稀咲，是御一夜市長候選人」
- old_vn: 「Với nhiều công dân ở đây, có lẽ đây là lần đầu tiên chúng ta gặp mặt.\nTên tôi là Houshou Kisaki. Là ứng cử viên cho chức thị trưởng Ohimitera.」
- fix: 「Với nhiều công dân ở đây, có lẽ đây là lần đầu tiên chúng ta gặp mặt.\nTên tôi là Houshou Kisaki. Là ứng cử viên cho chức thị trưởng Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1395** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「それは、今の御一夜に生きるみんなが、\nそれぞれに、それぞれの大好きを形にしたから」
- TW: 「御一夜會這麼美麗，是因為生活在這裡的人們把各自的想法化為了現實」
- old_vn: 「Đó là bởi vì, tất cả những người đang sống ở Ohimitera hiện tại,\nmỗi người đều đã biến những điều mình yêu thích nhất thành hiện thực.」
- fix: 「Đó là bởi vì, tất cả những người đang sống ở Ohitoyo hiện tại,\nmỗi người đều đã biến những điều mình yêu thích nhất thành hiện thực.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1396** (nhân vật: 稀咲; nguồn old_vn: csv3)
- JP: 「現状の御一夜の経済は低迷している。\nそれが、つまりは信じた結果――」
- TW: 「御一夜的經濟目前陷入了低迷。這就是相信他們的後果——」
- old_vn: 「Nền kinh tế hiện tại của Ohimitera đang trì trệ.\nĐó, tóm lại chính là kết quả của việc tin tưởng――」
- fix: 「Nền kinh tế hiện tại của Ohitoyo đang trì trệ.\nĐó, tóm lại chính là kết quả của việc tin tưởng――」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1407** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「それでも私は。そうしたいって思います。\n御一夜の人たちを、信じるべきだって思っています」
- TW: 「我也還是想這麼做。我認為應該相信御一夜的人們」
- old_vn: 「Dù vậy, tôi. Vẫn muốn làm như thế.\nTôi nghĩ rằng, chúng ta nên tin tưởng vào người dân Ohimitera.」
- fix: 「Dù vậy, tôi. Vẫn muốn làm như thế.\nTôi nghĩ rằng, chúng ta nên tin tưởng vào người dân Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1596** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「政治について、今まで深くは考えていませんでした。\nけど、御一夜の町を私はずっと、見続けて来ました」
- TW: 「至今為止，我雖然並不怎麼關心政治，但我一直關注著御一夜這個城市」
- old_vn: 「Về chính trị, từ trước đến nay tôi chưa từng suy nghĩ sâu sắc.\nNhưng, tôi vẫn luôn dõi theo thị trấn Ohimitera này.」
- fix: 「Về chính trị, từ trước đến nay tôi chưa từng suy nghĩ sâu sắc.\nNhưng, tôi vẫn luôn dõi theo thị trấn Ohitoyo này.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1642** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「そう……だな。\n最初は、御一夜への、右田への恩返しのためだけだった」
- TW: 「這個嘛……最開始我只是為了向御一夜，向右田家報恩」
- old_vn: 「Đúng…… vậy nhỉ.\nBan đầu, anh chỉ muốn báo đáp công ơn của Ohimitera, của nhà Migita.」
- fix: 「Đúng…… vậy nhỉ.\nBan đầu, anh chỉ muốn báo đáp công ơn của Ohitoyo, của nhà Migita.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1669** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「じゃあ、どうして――えと、もちろん、\n御一夜の水を守るためって……けど、それだけで？」
- TW: 「那為什麼……啊，保護御一夜的水資源不受汙染當然重要……但只是這樣嗎？」
- old_vn: 「Vậy thì tại sao――à ừm, tất nhiên là\nđể bảo vệ nguồn nước của Ohimitera rồi…… nhưng, chỉ vì thế thôi sao?」
- fix: 「Vậy thì tại sao――à ừm, tất nhiên là\nđể bảo vệ nguồn nước của Ohitoyo rồi…… nhưng, chỉ vì thế thôi sao?」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1963** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 都市モデルでは、御一夜の町そのものも、\n未来図として描かれていた。
- TW: 在城市模型中，整個御一夜也被一同規劃了。
- old_vn: Trong mô hình đô thị, bản thân thị trấn Ohimitera cũng\nđược khắc họa như một bức tranh tương lai.
- fix: Trong mô hình đô thị, bản thân thị trấn Ohitoyo cũng\nđược khắc họa như một bức tranh tương lai.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1999** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 今の言葉は、御一夜市民への侮辱とも、\n銀行自体の能力不足への吐露ともとられかねない失言だ。
- TW: 她剛才那句話既可以理解為是對御一夜市民的侮辱，也可以理解為是承認銀行自身能力不足。
- old_vn: Lời nói vừa rồi là một sự lỡ lời, có thể bị coi là sự xúc phạm đối với công dân Ohimitera,\ncũng như là sự thừa nhận về sự yếu kém của chính ngân hàng.
- fix: Lời nói vừa rồi là một sự lỡ lời, có thể bị coi là sự xúc phạm đối với công dân Ohitoyo,\ncũng như là sự thừa nhận về sự yếu kém của chính ngân hàng.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2050** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜の未来を示すあの絵をもっと、\n多くの人に見てもらい――
- TW: 得讓更多的人看到那張指示著御一夜未來方向的畫——
- old_vn: Để bức tranh thể hiện tương lai của Ohimitera đó,\nđược nhiều người nhìn thấy hơn nữa――
- fix: Để bức tranh thể hiện tương lai của Ohitoyo đó,\nđược nhiều người nhìn thấy hơn nữa――
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2269** (nhân vật: monologue; nguồn old_vn: audit)
- JP: 笑顔と、笑顔と、笑顔の中を、笑顔にあふれた御一夜を。\n\x%l8620;#00ffc040;8620%l;#;が\x%lキハ07;#00ffc040;キハ07%l;#;sが新しい\x%l客車;#00ffc040;客車%l;#;が、僕らをのせて走ってる。
- TW: 畫上，\x%l8620;#00ffc040;８６２０%l;#;和\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;Ｓ以及全新的\x%l客車;#00ffc040;客運車廂%l;#;正載著我們，跑在充滿笑容的御一夜中。
- old_vn: Giữa những nụ cười, nụ cười và nụ cười, một Ohimitera tràn ngập nụ cười.\n\x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#;S cùng \x%l客車;#00ffc040;toa hành khách%l;#; mới, đang chở chúng tôi băng băng chạy.
- fix: Giữa những nụ cười, nụ cười và nụ cười, một Ohitoyo tràn ngập nụ cười.\n\x%l8620;#00ffc040;8620%l;#; và \x%lキハ07;#00ffc040;KiHa 07%l;#;S cùng \x%l客車;#00ffc040;toa hành khách%l;#; mới, đang chở chúng tôi băng băng chạy.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). old_vn = giá trị audit fix (audit "tiếng cười"→"nụ cười" so với CSV3); chỉ đổi Ohimitera→Ohitoyo trên giá trị audit.

### 24. 02_Hibiki / 日々姫16_夢を乗せて (16 dòng)

**Key 1372** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: ……御一夜駅前に人形時計を設置して、\n御一夜観光のシンボルにする。
- TW: ……在御一夜車站設置一個人偶時鐘，讓它成為御一夜觀光的象徵物。
- old_vn: ……Lắp đặt đồng hồ búp bê trước ga Ohimitera,\nđể biến nó thành biểu tượng du lịch của Ohimitera.
- fix: ……Lắp đặt đồng hồ búp bê trước ga Ohitoyo,\nđể biến nó thành biểu tượng du lịch của Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 1584** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「いいです。見せつけてあげちゃいますよ。\n御一夜のみんなに、私の素敵な旦那様を」
- TW: 「不要緊的，就讓他們看看嘛。讓御一夜的大家看看我的老公有多麼帥氣」
- old_vn: 「Không sao đâu. Cho họ xem luôn cũng được. Cho mọi người ở Ohimitera thấy, người chồng tuyệt vời của em.」
- fix: 「Không sao đâu. Cho họ xem luôn cũng được. Cho mọi người ở Ohitoyo thấy, người chồng tuyệt vời của em.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1601** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「人形も時計も、御一夜の職人さんに製作依頼して――\n更に御一夜の色を出したシンボルにしていきたいと」
- TW: 「人偶和時鐘屆時都委託御一夜的工匠們來製作——要讓它們成為更能突出御一夜特色的象徵物」
- old_vn: 「Cả búp bê và đồng hồ, chúng tôi sẽ nhờ các nghệ nhân của Ohimitera chế tác――\nvà muốn biến nó thành một biểu tượng mang đậm màu sắc Ohimitera hơn nữa.」
- fix: 「Cả búp bê và đồng hồ, chúng tôi sẽ nhờ các nghệ nhân của Ohitoyo chế tác――\nvà muốn biến nó thành một biểu tượng mang đậm màu sắc Ohitoyo hơn nữa.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 1850** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「私、御一夜をもっともっと素敵な町にしたいです。\nみんなにもっと、笑顔になってほしいから」
- TW: 「我想要讓御一夜變成一個更加更加美好的城市。我想讓大家的笑臉更加燦爛」
- old_vn: 「Em muốn biến Ohimitera thành một thành phố tuyệt vời hơn nữa. Vì em muốn mọi người sẽ nở nụ cười nhiều hơn nữa.」
- fix: 「Em muốn biến Ohitoyo thành một thành phố tuyệt vời hơn nữa. Vì em muốn mọi người sẽ nở nụ cười nhiều hơn nữa.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1929** (nhân vật: 議員; nguồn old_vn: csv3)
- JP: 「最後に、御一夜駅前整備についてお伺いいたします」
- TW: 「最後我想問一下關於御一夜車站周邊建設的問題」
- old_vn: 「Cuối cùng, tôi xin hỏi về việc chỉnh trang khu vực trước ga Ohimitera.」
- fix: 「Cuối cùng, tôi xin hỏi về việc chỉnh trang khu vực trước ga Ohitoyo.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1950** (nhân vật: ハチロク; nguồn old_vn: audit)
- JP: 「湯医往復観光特急、\n『ＳＬ御一夜号』間もなく発車いたします！」
- TW: 「湯醫往復觀光特快列車，“蒸汽機車御一夜號”馬上就要發車了！」
- old_vn: 「Tàu tốc hành du lịch khứ hồi Yunoi, "SL Ohimitera" chuẩn bị khởi hành!」
- fix: 「Tàu tốc hành du lịch khứ hồi Yunoi, "SL Ohitoyo" chuẩn bị khởi hành!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). old_vn = giá trị audit fix (audit "Yui"→"Yunoi" cho 湯医往復 so với CSV3); chỉ đổi Ohimitera→Ohitoyo trên giá trị audit.

**Key 1971** (nhân vật: 議員; nguồn old_vn: csv3)
- JP: 「さすが市長、すばらしい修正案をありがとうございます。\nこれでしたら、より御一夜の魅力が伝わりますね」
- TW: 「真不愧是市長，感謝您提出如此優秀的修正案。如果按這個方案執行的話，一定能更好地彰顯御一夜的魅力」
- old_vn: 「Quả không hổ danh thị trưởng, cảm ơn cô vì một bản sửa đổi tuyệt vời.\nNếu làm thế này, sức hấp dẫn của Ohimitera sẽ được truyền tải tốt hơn nhỉ.」
- fix: 「Quả không hổ danh thị trưởng, cảm ơn cô vì một bản sửa đổi tuyệt vời.\nNếu làm thế này, sức hấp dẫn của Ohitoyo sẽ được truyền tải tốt hơn nhỉ.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 1981** (nhân vật: 議員; nguồn old_vn: csv3)
- JP: 「確かに、\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;は新しい御一夜のシンボルでしょう。\nが、真に御一夜を代表する名物は、伝統あるキジ馬です」
- TW: 「確實，\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;算是新御一夜的象徵吧。不過，真正能代表御一夜的名物可是擁有悠久傳統的雉子馬才對」
- old_vn: 「Đúng là \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; có lẽ là biểu tượng mới của Ohimitera.\nNhưng, đặc sản thực sự đại diện cho Ohimitera, chính là ngựa gỗ Kiji truyền thống.」
- fix: 「Đúng là \x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; có lẽ là biểu tượng mới của Ohitoyo.\nNhưng, đặc sản thực sự đại diện cho Ohitoyo, chính là ngựa gỗ Kiji truyền thống.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu). Đổi cả 2 lần xuất hiện trong dòng.

**Key 1996** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「御一夜駅に折り返したら、少し、時間を貰えるか。\n大事なことを話したいんだ」
- TW: 「等折返回御一夜站後能耽誤你一些時間嗎？我有重要的事想對你說」
- old_vn: 「Khi nào quay lại ga Ohimitera, cho anh xin một chút thời gian được không. Anh có chuyện quan trọng muốn nói.」
- fix: 「Khi nào quay lại ga Ohitoyo, cho anh xin một chút thời gian được không. Anh có chuyện quan trọng muốn nói.」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2277** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: どれも、御一夜の名物だ。\nどれが一番だとかって、比べて順位がつくものじゃない。
- TW: 不論哪個都是御一夜的名物。它們不應該非得決出高下，排出名次。
- old_vn: Tất cả đều là đặc sản của Ohimitera.\nKhông thể nào so sánh xem cái nào là nhất, để mà xếp hạng được.
- fix: Tất cả đều là đặc sản của Ohitoyo.\nKhông thể nào so sánh xem cái nào là nhất, để mà xếp hạng được.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2304** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 事実、御一夜がそうだった。\nデメリットの大きさに目を瞑っても、工場誘致を望んだ。
- TW: 事實上御一夜就是這樣。當時儘管缺點非常明顯，人們也寧願睜一隻眼閉一隻眼地想要引進工廠。
- old_vn: Thực tế, Ohimitera đã từng như vậy. Dù nhắm mắt làm ngơ trước những nhược điểm to lớn, họ vẫn mong muốn thu hút nhà máy.
- fix: Thực tế, Ohitoyo đã từng như vậy. Dù nhắm mắt làm ngơ trước những nhược điểm to lớn, họ vẫn mong muốn thu hút nhà máy.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2374** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: そうするために意見や議論を真剣に交わし合うことが、\n結局は、御一夜の民意を一番正しく示すって。
- TW: 只有為此對議案進行真刀真槍的意見討論，最後的結果才能最正確地反映御一夜的民意。
- old_vn: Để làm được điều đó, việc trao đổi ý kiến và tranh luận một cách nghiêm túc,\nrốt cuộc, mới là cách thể hiện chính xác nhất ý nguyện của người dân Ohimitera.
- fix: Để làm được điều đó, việc trao đổi ý kiến và tranh luận một cách nghiêm túc,\nrốt cuộc, mới là cách thể hiện chính xác nhất ý nguyện của người dân Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2495** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: この御一夜から――\nこの\x%l8620;#00ffc040;8620%l;#;の\x%l運転台;#00ffc040;運転台%l;#;から。どこまでも。
- TW: 從御一夜——從\x%l8620;#00ffc040;８６２０%l;#;的\x%l運転台;#00ffc040;駕駛台%l;#;，直到天涯海角。
- old_vn: Từ Ohimitera này——từ \x%l運転台;#00ffc040;buồng lái%l;#; của chiếc \x%l8620;#00ffc040;8620%l;#; này. Bất kể là đi đến đâu.
- fix: Từ Ohitoyo này——từ \x%l運転台;#00ffc040;buồng lái%l;#; của chiếc \x%l8620;#00ffc040;8620%l;#; này. Bất kể là đi đến đâu.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2499** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 御一夜駅のホームには、\nたくさんの人たちが待っている。
- TW: 御一夜站的站台上已經有一大群人在等著了。
- old_vn: Trên sân ga Ohimitera, có rất nhiều người đang chờ đợi.
- fix: Trên sân ga Ohitoyo, có rất nhiều người đang chờ đợi.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2561** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 観光\x%l列車;#00ffc040;列車%l;#;の売りのひとつの『御一夜ガイド』を、\n地元出身の二人より、見事にこなしてくれていると聞く。
- TW: 我聽說在觀光\x%l列車;#00ffc040;列車%l;#;賣點之一“御一夜導遊解說”方面，她比本地出身的凪和深美做得還好。
- old_vn: Nghe nói trong phần "Hướng dẫn Ohimitera", một trong những điểm nhấn của \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch, cô ấy còn làm xuất sắc hơn cả hai người xuất thân từ địa phương này.
- fix: Nghe nói trong phần "Hướng dẫn Ohitoyo", một trong những điểm nhấn của \x%l列車;#00ffc040;đoàn tàu%l;#; du lịch, cô ấy còn làm xuất sắc hơn cả hai người xuất thân từ địa phương này.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2701** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 日々姫が描いた、御一夜のみんなの笑顔をつないだ。
- TW: 正是日日姬畫的御一夜的人們露出燦爛笑容的那張。
- old_vn: Tấm áp phích do Hibiki vẽ, kết nối những nụ cười của mọi người ở Ohimitera.
- fix: Tấm áp phích do Hibiki vẽ, kết nối những nụ cười của mọi người ở Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

### 25. 02_Hibiki / 日々姫h6_オリエンテーリング借り物競走（ペア） (6 dòng)

**Key 2258** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「うむ。恐らくはそれが、御一夜の商店会主催の\n大運動会に初めて触れた人間の反応と同じものだろう」
- TW: 「嗯。你這個反應，就跟其他人第一次聽說御一夜商店協會辦的大運動會的反應一樣」
- old_vn: 「Ừm. Có lẽ đó cũng chính là phản ứng của những người\nlần đầu tiên biết đến Đại hội thao do khu phố thương mại Ohimitera tổ chức đấy」
- fix: 「Ừm. Có lẽ đó cũng chính là phản ứng của những người\nlần đầu tiên biết đến Đại hội thao do khu phố thương mại Ohitoyo tổ chức đấy」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2309** (nhân vật: 日々姫; nguồn old_vn: csv3)
- JP: 「帝都ではそうかもしれんけど、\n御一夜では普通に地植えで――ほら！」
- TW: 「在帝都可能是吧，不過在御一夜是長在地上的――看！」
- old_vn: 「Ở Đế đô có thể là vậy, nhưng ở Ohimitera\nngười ta toàn trồng dưới đất thôi――Nhìn kìa!」
- fix: 「Ở Đế đô có thể là vậy, nhưng ở Ohitoyo\nngười ta toàn trồng dưới đất thôi――Nhìn kìa!」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2442** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「僕は素晴らしい習慣だと思うぞ？\n御一夜の、商店会主催の大運動会」
- TW: 「我覺得這個習俗不錯啊，御一夜商店協會主辦的大運動會很棒」
- old_vn: 「Anh thấy đó là một tập quán tuyệt vời mà?\nĐại hội thao do khu phố thương mại Ohimitera tổ chức ấy」
- fix: 「Anh thấy đó là một tập quán tuyệt vời mà?\nĐại hội thao do khu phố thương mại Ohitoyo tổ chức ấy」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 2589** (nhân vật: 双鉄; nguồn old_vn: csv3)
- JP: 「まぁな。体を思い切り動かすのは嫌いではないし、\n御一夜が一体となる、歴史あるイベントでもあるしな」
- TW: 「算是吧，我不討厭運動身體。而且這個活動很有歷史，還能讓御一夜團結在一起」
- old_vn: 「Cũng có thể nói vậy. Anh không ghét việc vận động cơ thể hết mình,\nvới lại, đây cũng là một sự kiện mang tính lịch sử, gắn kết toàn bộ Ohimitera lại với nhau mà」
- fix: 「Cũng có thể nói vậy. Anh không ghét việc vận động cơ thể hết mình,\nvới lại, đây cũng là một sự kiện mang tính lịch sử, gắn kết toàn bộ Ohitoyo lại với nhau mà」
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3039** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: 日々姫のホーム。日々姫の味方がいくらだっている、\n僕らの町で――御一夜で。
- TW: 在這日日姬的家鄉，在這個日日姬的伙伴們生活的地方，在我們的小鎮――御一夜。
- old_vn: Sân nhà của Hibiki. Nơi có biết bao nhiêu đồng minh của em ấy,\ntrong thị trấn của chúng tôi――tại Ohimitera.
- fix: Sân nhà của Hibiki. Nơi có biết bao nhiêu đồng minh của em ấy,\ntrong thị trấn của chúng tôi――tại Ohitoyo.
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

**Key 3698** (nhân vật: monologue; nguồn old_vn: csv3)
- JP: （そうか。わざわざ遠回りしなくても、\n看板づくりのころから、ずっと、御一夜の町は――）
- TW: （原來如此，不用繞遠也可以。在設計招牌的時候，日日姬就非常熟悉御一夜了）
- old_vn: （Ra vậy. Không cần phải cất công đi đường vòng,\ntừ lúc làm bảng hiệu đến giờ, thị trấn Ohimitera luôn――）
- fix: （Ra vậy. Không cần phải cất công đi đường vòng,\ntừ lúc làm bảng hiệu đến giờ, thị trấn Ohitoyo luôn――）
- Lý do: JP chứa 御一夜 → "Ohimitera" sai, "Ohitoyo" đúng (T1, quyết 19/11, Hieu).

## 5. Dòng đã xét nhưng KHÔNG đổi

### 5a. Đã sửa trong audit rồi (244 dòng trong phạm vi — không sửa lại)

CSV3 VN chứa "Ohimitera" nhưng current value (audit fix) đã là "Ohitoyo". Phân bổ theo file:
- lr_ハチロクh1_今ひとたびの契り: 2
- lr追加_みくろ＆日々姫h「みくろのマスター」: 2
- ハチロク09_もくもくオリヴィ: 7
- ハチロク09_採決: 24
- ハチロク10_旺宮鉄道歴史館: 5
- ハチロク10_炙り出し: 1
- ハチロク12_ムナカタ来訪: 1
- ハチロク15_家族: 5
- ハチロクh7_レトロモダンメイクラヴ: 1
- ハチロクh9_コノフクハキルコト: 6
- 仲国06_聖都とパンダとハチロクと: 1
- 共通01_右田双鉄の帰還: 8
- 共通02_日々姫と真闇と人形と: 5
- 共通03_ハチロクとナビ: 3
- 共通05_ようやく石炭: 11
- 共通06_8620を探せ: 4
- 共通07_鍵: 4
- 共通08_傷跡: 2
- 共通09_さきだつもの: 15
- 共通10_クマ川くだりで見る景色: 14
- 共通11_経営資源: 12
- 共通12_のぞみ: 6
- 共通13_勾配図: 3
- 共通14_負債: 30
- 共通15_回り始める動輪: 14
- 日々姫01_双鉄の妹: 4
- 日々姫02_文庫森: 2
- 日々姫02_日々姫の日々: 14
- 日々姫03_客車手配: 14
- 日々姫03_湯富院: 8
- 日々姫04_カフェキッチン: 1
- 日々姫04_同乗: 2
- 日々姫12_風: 7
- 日々姫14_投開票: 6

### 5b. Dạng khác trong cùng dòng — giữ nguyên đợt này (thuộc item khác)

- "Đường sắt Ohito" trần (T1-bare / T2): ハチロク01_こんにちわ赤ちゃん 2467 · ハチロク12_ムナカタ来訪 1900, 2089 · 日々姫08_とれいん食堂 3719 (4 dòng — các dòng này vẫn được sửa phần "Ohimitera" của chúng; chỉ phần "Ohito" trần là để lại).
- "Yui" / "tuyến Yui" / "ga Yui" (湯医 → "Yunoi", item Yui): 9 dòng trong fix vẫn chứa "Yui" — ハチロク06_それぞれの傷跡 2710 ("tuyến Ohitoyo - Yui") · 日々姫08_とれいん食堂 2051 ("ga Yui"), 3132 ("Dọc tuyến Yui"), 3495 ("đoạn Yui - Ohitoyo"), 3719 ("Đoạn (Yui) - Ohitoyo - Hayato") · 日々姫08_開きかけのつぼみ 2260 ("hai ga là Ohitoyo và Yui") · 日々姫09_run_with_our_dreams 2708 ("Yui hay Taragi") · 日々姫10_稀咲の未来図、日々姫の未来図 2613 ("dọc tuyến Yui") · 日々姫11_御一夜モザイク 2095 ("dọc tuyến Yui"). Chỉ riêng phần Ohimitera được sửa; "Yui" để cho batch Yui. (Riêng 日々姫16_夢を乗せて 1950: audit đã sửa "Yui"→"Yunoi" cho 湯医往復 trước đó, nên fix ở đây chứa "Yunoi" — không thuộc diện trên.)
- "Jutsu-sen" (T17 → "Jutsusen"): ハチロク12_ムナカタ来訪 1525 (1 dòng).
- "Đường sắt Hoàng gia" (T3 → Teitetsu): 日々姫09_run_with_our_dreams 1906 (1 dòng).

### 5c. Flag (JP không chứa 御一夜 — nghi misalignment)

Không có dòng nào. Tất cả 221 dòng ứng viên đều có 御一夜 trong JP (221/221).

## 6. Second pass (đọc lại toàn bộ fix so với JP)

- Tổng số fix: **221** · Đọc lại và xác nhận đúng: **221** · Loại bỏ: **0** · Sửa lại sau second pass: **0**.
- Kiểm tra máy hỗ trợ second pass: mọi fix đều = old_vn với duy nhất phép thay "Ohimitera"→"Ohitoyo" (đã assert từng dòng: fix.replace("Ohitoyo","Ohimitera") == old_vn); không fix nào còn chứa "Ohimitera"; số lần "Ohitoyo" trong fix = số lần "Ohimitera" trong old_vn (tổng 240); tag %l, literal `\n`/`\\n`, dấu câu và mọi nội dung khác giữ nguyên byte-for-byte; 5 dòng audit-src giữ nguyên mọi thay đổi của audit (chỉ đổi Ohimitera).
- Đọc mắt toàn bộ 221 dòng trong file review này (JP đối chiếu fix): không phát hiện sai lệch nào — mọi JP đều chứa 御一夜/御一夜鉄道 đúng vị trí tương ứng với "Ohitoyo" trong fix; 4 dòng TW lược tên địa danh đã được xử lý theo quy tắc JP thắng TW (ghi chú ở từng dòng).

## 7. Khối TOML (parse-verified, theo file)

Mỗi khối có header `[script]`, key dạng chuỗi, giá trị là fix. Trong khối TOML, backslash được escape (`\` → `\\`, `"` → `\"`), nên literal `\n` trong giá trị viết thành `\\n`. Đã parse-verify bằng tomllib: mọi khối parse được và giá trị parse ra khớp fix từng key (25 khối / 221 key).

#### 01_Hachiroku / ハチロク01_こんにちわ赤ちゃん

```toml
[script]
"1662" = "「……Nếu đã có những sân khấu tỏa sáng khác,\\nthì chẳng ai lại cất công lặn lội đến tận Ohitoyo nữa nhỉ.」"
"2130" = "「Việc cho Đường sắt Mikan thuê đoạn Ohitoyo-Hayato.\\nTôi đã nghĩ điều kiện đó quá có lợi cho đối phương rồi——hừm.」"
"2467" = "「Việc khôi phục tuyến đường sắt bị bãi bỏ đầu tiên của Đường sắt Ohito——Về cách xử lý đoạn Ohitoyo-Hayato,\\ncuối cùng có hai phương án được giữ lại.」"
"2647" = "「Tất nhiên rồi. Phải nói là, đó mới là vinh hạnh đấy.\\nĐược vòng tay đã vực dậy Ohitoyo bế cơ mà.」"
"2662" = "「Ngay cả ở Ohitoyo cũng đang phát quảng cáo trên tivi mà.\\nỞ Đông Hinomoto hay Shikoku, có vẻ như đầu máy hơi nước cũng đang được đánh giá cao trở lại.」"
"2710" = "「Dự án đang được đón nhận rộng rãi. Việc khôi phục tuyến đường sắt ở các nơi cũng rất thuận lợi.\\nMặc dù vậy——chỉ có Ohitoyo là bị bỏ lại phía sau.」"
"2725" = "「Đúng vậy ạ. Đoạn Ohitoyo-Hayato. Đặc biệt là khu vực quanh ga Okoba,\\nlà nơi có địa hình hiểm trở vang danh khắp Hinomoto.」"
"2792" = "「Tôi hỏi lại lần nữa. Lý do là gì?\\nDự án được đón nhận, vậy tại sao Ohitoyo lại bị chậm chân.」"
"2801" = "「Vậy là đầu máy nào」「Tức là đầu máy dư thừa đó sẽ chạy tuyến Yunoi.\\nCòn 8620 sẽ chạy đoạn Ohitoyo-Hayato đúng không?」"
```

#### 01_Hachiroku / ハチロク01_双鉄の目・ハチロクの目

```toml
[script]
"1345" = "——Tôi nghĩ mình có thể học được một Ohitoyo khác,\\nso với \"Ohitoyo\" mà Hibiki đang nhìn thấy."
"1926" = "「Nên hiểu rõ hơn về con người và cuộc sống ở Ohitoyo——\\nTôi cảm thấy ý kiến của Hibiki, là điều rất đáng để tham khảo.」"
"1936" = "「Tôi nghĩ là vậy. Chắc chắn, là vậy rồi.\\nBởi vì, ba tôi——thực sự rất yêu Ohitoyo.」"
"2049" = "「Ba tôi, đã chụp rất nhiều ảnh.\\nCủa Ohitoyo, và cả của đường sắt nữa.」"
"2086" = "「Tôi nghĩ, có nhiều góc nhìn thì tốt hơn.\\nNếu muốn hiểu sâu hơn về Ohitoyo.」"
"2827" = "Tôi không nghĩ điều đó là xấu.\\nKhuôn mặt mà một người đã hòa nhập và có được sự tin tưởng ở Ohitoyo như Hibiki nhìn thấy."
"2829" = "Đó chắc chắn, là một khía cạnh tuyệt vời của Ohitoyo,\\nvà là sức hấp dẫn nên truyền tải đến khách du lịch. Nhưng——"
"2839" = "Thị trấn Ohitoyo, không phải là không gian để tận hưởng, gần gũi hay sinh sống,\\nmà là nơi để tôi tìm kiếm cơ hội chuộc tội dù chỉ là một chút."
"2894" = "(Phải biến 8620——biến nó, thành gương mặt đại diện cho Ohitoyo)"
"2908" = "(Làm tỉ mỉ đến từng chi tiết nhỏ nhỉ.\\nMô hình thị trấn này……là mô phỏng theo Ohitoyo ngày xưa sao?)"
```

#### 01_Hachiroku / ハチロク05_軋み

```toml
[script]
"1437" = "「Không phải đâu. Không phải là khiếu nại từ bên trong Hiệp hội Thương mại Ohitoyo đâu.\\nNhờ có nó mà buôn bán phát đạt, bên này còn đang phải cảm tạ \\x%l8620;#00ffc040;[Hachiroku,3]8620%l;#; ấy chứ.」"
"1761" = "「Để bảo vệ dòng sông Kuma xinh đẹp ấy, bảo vệ cuộc sống của những người dân Ohitoyo hiền hòa――\\nXin ngài hãy sử dụng chúng em đi ạ.」"
"2124" = "（Chỉ khi cải thiện được tình hình đến mức không còn ai cảm thấy khói than là mối nguy hại nữa,\\nthì con đường phục hưng Ohitoyo mà chúng tôi đang hướng tới mới có thể mở ra.）"
"2235" = "（Cách ga Ohitoyo vài km, gần một đoạn giao cắt đường sắt đã bị bỏ hoang,\\ncó một cửa hàng tạp hóa vẫn luôn tồn tại từ trước đến nay, mang tên \"Fumikiriya\".）"
"2475" = "（Những thứ bay trên bầu trời Ohitoyo,\\nbình thường thì cùng lắm cũng chỉ có lũ chim và Navi mà thôi.）"
```

#### 01_Hachiroku / ハチロク06_それぞれの傷跡

```toml
[script]
"1710" = "「Những người dân Ohitoyo, những vị khách đến tham quan――\\nCó nhiều người yêu mến 8620 hơn em nghĩ đấy.」"
"1819" = "「Ừ. Muốn họ rút lại quyết định mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;, muốn bảo vệ Ohitoyo.\\nHachiroku đang mong muốn giúp tôi đạt được mục đích đó.」"
"2706" = "Trong khoảng thời gian đó, nếu không thể ép họ rút lại quyết định mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\nthì chắc chắn ngài Soutetsu sẽ phải rời khỏi Ohitoyo."
"2710" = "Tuy hơi bất ngờ, nhưng nghĩ lại thì\\ntuyến Ohitoyo - Yui cũng chỉ dài khoảng hai mươi mấy kilomet."
```

#### 01_Hachiroku / ハチロク11_御一夜鉄道小畑線

```toml
[script]
"1201" = "...Chỉ từ Ohitoyo đến Okoba này thôi, độ dốc đã là quá đủ rồi."
"2011" = "「Đúng vậy nhỉ. Từ Ohitoyo đến Okoba, \\nmới chỉ có 10.4 kilomet thôi mà.」"
"2664" = "——Thành phố của chúng ta, Ohitoyo, \\nnhỏ bé, nhưng chắc chắn là có thể nhìn thấy."
```

#### 01_Hachiroku / ハチロク12_ムナカタ来訪

```toml
[script]
"1525" = "「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsu-sen, mà cả về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, \\ncũng sẽ tập trung xung quanh Ohitoyo. Có thể gọi là 'Ohitoyo của đường sắt' sao?」"
"1650" = "「Cậu Migita. Trước khi Đại bãi bỏ các tuyến đường sắt diễn ra. Tuyến sông mà ngài Giám đốc quý công ty đang muốn khôi phục—— \\nđoạn Ohitoyo - Yatsushiro, cậu đã từng đi qua chưa?」"
"1658" = "「Giống như Kokura ngày xưa, có thể bảo dưỡng cho toàn bộ đường sắt ở Kyushu. \\nPaulette muốn biến Ohitoyo thành một nơi như vậy đó ạ~」"
"1705" = "「A, thất lễ quá. Cháu giới thiệu bản thân hơi muộn. \\nCháu là Houshou Kisaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」"
"1847" = "「Ý tưởng là thúc đẩy mạnh mẽ hơn nữa dự án 'Quê hương của hơi nước', \\nmà thành phố Ohitoyo đang tiến hành.」"
"1886" = "「Trước đây, Ohitoyo từng là một \\x%lターミナル駅;#00ffc040;ga đầu mối%l;#; đường sắt lớn. \\nThông qua việc khôi phục các tuyến đường, chúng cháu hướng tới việc tái hiện lại điều đó, đồng thời」"
"1900" = "「Đúng là vậy. Vì thế chúng tôi đang trong quá trình chia sẻ tầm nhìn với thành phố Ohitoyo, \\nvà Đường sắt Ohito, để cùng nhau phát triển tạo ra sức mạnh tổng hợp.」"
"1955" = "「Hình ảnh của Kokura sao... So với Kokura, Ohitoyo \\ncó vẻ sẽ phải gánh chịu khá nhiều bất lợi về tuyến đường logistics đấy.」"
"2027" = "「Vâng. Hoa anh đào ở Ohitoyo đẹp tuyệt trần ạ. \\nĐầu máy số IX chạy giữa cơn mưa hoa anh đào, chắc chắn, cũng sẽ vô cùng kiều diễm.」"
"2089" = "「Bản thân Đường sắt Ohito cũng đang lên kế hoạch mở rộng trong tương lai. \\nƯu tiên hàng đầu là khôi phục Tuyến sông Ohitoyo - Yatsushiro. Sau đó」"
"2176" = "「Điều đó... có thể khả thi đấy ạ. Dù sao thì giữa Omiya, Hiroshima và Ohitoyo, \\ncũng đã bắt đầu có sự giao lưu rồi mà.」"
```

#### 01_Hachiroku / ハチロク16_春

```toml
[script]
"1803" = "「Bé Olivy, chắc chắn là đã rất hạnh phúc đúng không ạ?\\nEm ấy đã ra đi mà không hề hối hận vì đã đến Ohitoyo đúng không ạ?」"
"1839" = "「Đúng đúng. Em là \\x%l機関士;#00ffc040;lái tàu%l;#; hơi nước mà――\\nCòn chuyện của nhà máy Jutsusen nữa, em không thể rời khỏi Ohitoyo được.」"
"1845" = "「『Muốn trọ lại suối nước nóng tốt nhất Ohitoyo』\\nĐó chẳng phải là mong muốn của bé Kodama sao.」"
```

#### 02_Hibiki / lr_日々姫ふかみh1_凪ちゃんの代わり

```toml
[script]
"1689" = "「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\\nđến thị sát Ohitoyo thông qua sự môi giới của Kisaki.」"
```

#### 02_Hibiki / 日々姫01_リゾート食堂列車計画

```toml
[script]
"1224" = "……Kể từ khi dự luật mời nhà máy Aircra về Ohitoyo bị bác bỏ,\\nthoắt cái đã năm năm trôi qua."
"1561" = "「Trong khi mọi thứ khác đều đang tiến triển thuận lợi, thì chỉ có chuyến tàu này\\n- thứ mang lại lợi ích trực tiếp cho thành phố Ohitoyo - lại đang bị đình trệ.」"
"1658" = "「Nếu vậy thì tôi xin thừa nhận——Dự án tàu ăn uống nghỉ dưỡng,\\nchỉ dựa vào vốn đầu tư của Đường sắt Ohitoyo và các công ty xung quanh.」"
"1680" = "「Kéo những lợi ích mà các thành phố khác đang được hưởng về Ohitoyo.\\nĐó chính là cốt lõi của ý tưởng 『Tàu ăn uống nghỉ dưỡng』 đúng không?」"
"1714" = "「Thành phố Ohitoyo đã bỏ ra nhiều tiền bạc và mồ hôi công sức nhất\\nđể mở rộng tuyến đường, nhưng lại chỉ làm giàu cho những vùng đất ngoài Ohitoyo.」"
"1773" = "「Đến đây, phần chất vấn của nghị viên Niitsu xin được kết thúc.\\nTiếp theo, nghị viên Fuse thuộc 『Hội Công dân Ohitoyo』——」"
"1895" = "「Tôi rất mong chờ chuyến khảo sát tốt đẹp của ngài.\\nVì tương lai của thành phố Ohitoyo, chúng tôi cần thiết kế của ngài.」"
"1973" = "「Không có gì đáng ngạc nhiên đâu. Địa danh mới của Ohitoyo.\\nGamadus——đó cũng là một cơ sở vô cùng thú vị.」"
"2004" = "「Dự án 『Tàu ăn uống nghỉ dưỡng』 của Đường sắt Ohitoyo,\\ndo đích thân thị trưởng làm trung tâm tiến hành thiết kế và lập kế hoạch.」"
"2225" = "Khôi phục tuyến đường giữa Ohitoyo - Obata - Hayato\\ndo Đường sắt Ohitoyo làm chủ thể."
"2473" = "Đó quả thực là một trong những mục tiêu lớn của dự án này.\\nTừ Ohitoyo đến Oita. Từ Oita về Ohitoyo."
"2484" = "Đối mặt với Kisaki, người vẫn đang giữ chức vụ tại Ngân hàng Ohitoyo,\\nnghị viên Niitsu thuộc mảng kinh tế không thể tỏ ra quá mạnh miệng được."
"2506" = "Đúng là Gamadus——Bảo tàng tư liệu Đường sắt Ohitoyo dành cho trẻ em\\nlà một cơ sở tuyệt vời và thú vị, nhưng……"
```

#### 02_Hibiki / 日々姫03_湯富院

```toml
[script]
"2279" = "「Việc mọi người ở Ohitoyo biến việc đóng mới \\x%l客車;#00ffc040;toa hành khách%l;#; thành một dự án kinh doanh.\\nDù là tư cách cá nhân hay Thị trưởng, tôi đều rất biết ơn.」"
"2607" = "Thực tế, Ohitoyo thậm chí còn có cảm giác như đang liên tục bị cướp mất khách hàng tiềm năng\\nbởi hai khu suối nước nóng đang cạnh tranh gay gắt này."
```

#### 02_Hibiki / 日々姫04_カフェキッチン

```toml
[script]
"1757" = "「Nhưng mà, em không nghĩ trẻ em ở Ohitoyo\\nlại quen thuộc với khu mỏ đâu ạ. Chỉ cần thay đổi cách mô phỏng một chút——」"
"1788" = "「Cũng không hẳn là chỉ vì anh Soutetsu đâu~\\nMà còn vì Đường sắt Ohitoyo, vì chính bản thân bọn em nữa mà!」"
"1882" = "「A! Đúng vậy nha, làm thành cà ri SL,\\nchắc các bé ở Ohitoyo sẽ vui hơn đó ạ.」"
"2017" = "「Những món ăn theo mùa từ xa xưa của Ohitoyo và Kuma\\nmà Nagi và Fukami chỉ cho cũng có vẻ ngon lắm.」"
"2067" = "「Tôi là Migita Hibiki. Là hậu bối của tiền bối Kisaki, thị trưởng thành phố Ohitoyo,\\nlà nhà thiết kế. Và hiện tại, cũng là phụ lái tàu tạm thời.」"
"2310" = "「Ngài Soutetsu. Xin mời ạ.\\nVì Hibiki, vì Ohitoyo. Xin ngài hãy sử dụng nó cho hiệu quả ạ.」"
```

#### 02_Hibiki / 日々姫05_市議会見学

```toml
[script]
"1570" = "「……Đường sắt Ohitoyo cũng vậy, thành phố Ohitoyo cũng vậy.\\nNếu có tiền, thì có lẽ sẽ không ai phải chịu đựng sự đau khổ nữa nhỉ.」"
"1868" = "「Lớp sáu trường Tiểu học, trong buổi khai bút đầu năm trước khi lên Trung học,\\nai cũng bắt buộc phải viết nó. Ở tất cả các trường trong thành phố Ohitoyo.」"
"1992" = "「Cho dù là vậy. Việc kết nghĩa thành phố với thành phố Surukawa,\\nsẽ mang lại nhiều lợi ích cho thành phố Ohitoyo là điều không thay đổi.」"
"2050" = "「Có lẽ vì thế chăng? Tỷ lệ thu thuế của thành phố Ohitoyo không chỉ trong tỉnh,\\nmà còn cao vượt trội trên toàn khu vực Kyushu, đứng vị trí số 1 đấy.」"
"2239" = "「Hai chuyện hoàn toàn khác nhau. Hoạt động của công ty Aero-Craftech\\nvà sự phát triển của thành phố Ohitoyo không thể xây dựng được mối quan hệ đôi bên cùng có lợi.」"
"2243" = "「Đó là phát ngôn của một nghị viên sao!\\nLà đại diện cho người dân Ohitoyo, ông không thấy xấu hổ à!」"
"2434" = "Nếu cứ ở Kumamoto hay Ohitoyo mãi, thì chắc chắn,\\nsẽ không thể nói hay đến thế."
"2701" = "Tiếng phổ thông, hay thủ đô. Những thứ đó quả thực rất đáng ngưỡng mộ,\\nnhưng Ohitoyo cũng có những điều thú vị riêng của Ohitoyo."
```

#### 02_Hibiki / 日々姫05_御一夜ステーションカフェ

```toml
[script]
"2560" = "「Đây là quán cà phê Gamadas——\\nà không, là quán cà phê ga Ohitoyo sao.」"
"3223" = "『Quán cà phê ga Ohitoyo』\\nQuán trà, dịch trạm của Ohitoyo."
"3285" = "Ở Ohitoyo, hương vị đồng quê vẫn còn rất đậm nét.\\nHơn nữa, chị Mayami lại luôn dậy sớm."
```

#### 02_Hibiki / 日々姫06_みくろ、来訪

```toml
[script]
"1877" = "「Gì chứ, là Mikuro sao!\\nCô ấy cất công đến tận Ohitoyo tìm tôi à.」"
"1890" = "「Nhưng ở Ohitoyo thì cả nhân lực lẫn địa điểm đều rất khó khăn.\\n\\x%l石造機関庫;#00ffc040;Xưởng đầu máy bằng đá%l;#; đã kín chỗ rồi. Trước Gamadasu cũng không còn không gian.」"
"1922" = "「Thật ra, Mikuro cũng muốn đi thử Đường sắt Ohitoyo nữa.」"
"2099" = "「Nếu ở Ohitoyo thì chắc chắn sẽ thành công!\\nBởi vì Ohitoyo là thành phố của đầu máy hơi nước mà.」"
"2374" = "「Thế là có thể tuyên truyền rằng 'Lái tàu hơi nước đương nhiệm của Đường sắt Ohitoyo và Thị trưởng Ohitoyo\\ncũng tham gia dọn dẹp D51'! Như vậy thì làm được rồi.」"
"2439" = "「Mikuro cũng muốn thử tắm suối nước nóng ở Ohitoyo lắm,\\nnhưng nếu không về được thì sẽ làm phiền mọi người trong sở thú mất.」"
"2504" = "「Thực đơn này hả? Là do mọi người ở Đường sắt Ohitoyo cùng nhau nghĩ ra đấy.」"
```

#### 02_Hibiki / 日々姫06_日々姫の決断

```toml
[script]
"2416" = "「Với tư cách là Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto, Houshou Kisaki\\ntuyệt đối sẽ không hành động chỉ dựa trên thông tin từ một học sinh đâu.」"
"2582" = "「Là tốt nhất cho thành phố Ohitoyo và Đường sắt Ohitoyo.\\nVà cũng là tốt nhất cho tất cả chúng ta.」"
"2589" = "「Một kẻ thực chất là người ngoài như anh mà trở thành ứng cử viên,\\nthì liệu có thể chiến thắng trong cuộc bầu cử ở Ohitoyo không?」"
"2669" = "「Em nghĩ hỏi chị Mayami là tốt nhất.\\nChuyện bầu cử ở Ohitoyo……có lẽ chị ấy là người rành hơn bất cứ ai.」"
"2673" = "「Với năng lực của em, việc tiếp tục kiêm nhiệm cả chức Thị trưởng Ohitoyo và Giám đốc Đường sắt Ohitoyo,\\nem cảm thấy là vô cùng khó khăn.」"
"2696" = "「Nếu vậy thì em cũng tán thành ạ. Nếu là Hibiki,\\nem tin chắc rằng cô ấy sẽ vẽ nên một Ohitoyo tốt đẹp hơn.」"
"2749" = "「Huống hồ lại là trên Đường sắt Ohitoyo——À, không,\\nnếu nhìn nhận một cách tích cực thì có lẽ họ đang kỳ vọng vào việc chấn hưng du lịch... chăng?」"
"2817" = "「Một ứng cử viên có năng lực vượt trội hơn ngài Soutetsu,\\ndù có tìm khắp Ohitoyo cũng không thấy đâu.」"
"2926" = "「Ngân hàng Kumamoto mà lại quảng cáo ở Ohitoyo sao? Bọn họ định quảng cáo cái gì cơ chứ?」"
"3167" = "Thúc đẩy sự phán đoán của những người không thuộc đảng phái nào, những người không tán thành cũng không phản đối——\\nđiều đó sẽ kết nối với tương lai của Ohitoyo."
"3326" = "Đứng từ góc độ của Công ty Cổ phần Đường sắt Ohitoyo,\\nđây là một con số hấp dẫn có thể đưa rủi ro đầu tư về mức 0."
"3506" = "Không cần phải nói, Kumagin là ngân hàng duy nhất ở Ohitoyo."
"3628" = "Sinh ra ở Ohitoyo, lớn lên ở Ohitoyo,\\nvà là người đã dạy tôi về Ohitoyo, em gái nuôi của tôi."
```

#### 02_Hibiki / 日々姫07_姉の想い。妹の想い

```toml
[script]
"2166" = "「Để trở thành biểu tượng, để được yêu mến——\\nChỉ với bàn tay của Ohitoyo, của Yufuin là chưa đủ」"
"2247" = "「Về thực đơn, em cũng đã làm khảo sát và điều tra thử nghiệm\\ntại quán cà phê ga Ohitoyo」"
"2402" = "Lỡ mất cơ hội nếm thử hương vị địa phương.\\nVì bị bó hẹp trong Ohitoyo, chúng tôi suýt nữa đã phạm phải sai lầm đó."
"2512" = "Bởi vì chúng tôi đã định cố định thực đơn\\nbằng những đặc sản, danh sản của Ohitoyo."
"2604" = "Chúng tôi đã nghĩ đến việc chỉ lấy đặc sản của Ohitoyo làm nhân vật chính.\\nThậm chí khảo sát cũng chỉ được thực hiện ở Ohitoyo."
"2605" = "Chúng tôi đã không nhìn thấy. Chỉ Ohitoyo. Chỉ những thứ xung quanh.\\nHơn nữa, chỉ những phần nổi bật."
```

#### 02_Hibiki / 日々姫08_とれいん食堂

```toml
[script]
"1619" = "「……\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; tuyệt thật đấy nhỉ.\\nỞ Ohitoyo tôi chưa từng thấy bao giờ.」"
"2051" = "「Khởi hành từ ga Yui với tư cách là tàu thường lúc 05:45. Đến Ohitoyo lúc 06:45.\\nSau khi đón khách, chuyển thành toa ăn và xuất phát lúc 07:00」"
"2270" = "「Vé chỉ định Tàu nhà hàng ngày mốt, ngày 28 tháng 8.\\nCó kèm bữa ăn. Vé lên tàu Yufuin - Ohitoyo, có hiệu lực từ cùng ngày.」"
"2349" = "「Từ Yufuin đến suối nước nóng Ohitoyo nhé.」"
"2535" = "「Ở Ohitoyo thì,\\ncó làm thế nào cũng chẳng ngắm được cảnh đó đâu nhỉ」"
"2633" = "「Cháu cảm ơn ạ. Cá hương, hạt dẻ, và trên hết là\\nrượu Shochu Kuma, đều là đặc sản của Ohitoyo đó ạ」"
"2970" = "Cổng soát vé ga Ohitoyo hôm nay, là cánh cổng đưa đón đến một hành trình mới."
"3027" = "Nagi lấy Kendama từ khu vực đồ thủ công mỹ nghệ,\\nFukami lấy cuốn sách lịch sử Ohitoyo từ giá sách."
"3106" = "Nhờ hiệu ứng tích cực từ việc kết nối đường ray,\\ndoanh thu du lịch của Ohitoyo vẫn tiếp tục tăng trưởng."
"3111" = "Ngày mốt――Chuyến tàu nhà hàng khởi hành vào một ngày trong tuần,\\nthậm chí còn chẳng phải chuyến tàu đầu tiên đi Ohitoyo."
"3132" = "Là 『Dọc tuyến Yui』. Không phải Ohitoyo――Không phải 8620.\\nNếu có thể mang hoạt động du lịch trải nghiệm bảo tồn đầu máy xe lửa đến dọc tuyến Yui."
"3149" = "Nếu sức hấp dẫn của Ohitoyo được nhiều người biết đến,\\nchắc chắn tuyến đường này cũng sẽ sớm liên tục cháy vé thôi."
"3495" = "Ra là vậy, quả thực――Ngay cả đoạn Yui - Ohitoyo hiện đang chạy tàu thường,\\ncũng có thể trở thành đoạn tàu du lịch."
"3719" = "Đoạn (Yui) - Ohitoyo - Hayato là của Đường sắt Ohito.\\nTừ Hayato - Kagoshima - Sendai - Yatsushiro - Kumamoto là của Đường sắt Mikan."
"3736" = "＜39.000 yên, 1 Người lớn. Tàu nhà hàng số 2, toa 1, 4A.\\n25/8 Tàu nhà hàng số 1. Nhân viên phân khu trưởng tàu Ohitoyo phát hành＞"
"3739" = "＜Có hiệu lực từ ngày 28 tháng 8, từ Yufuin đi suối nước nóng Ohitoyo.\\nChặng (Tàu nhà hàng), chỉ có giá trị trong ngày. Chỉ vé lên tàu có hiệu lực trong 5 ngày＞"
```

#### 02_Hibiki / 日々姫08_開きかけのつぼみ

```toml
[script]
"2172" = "「Chị nghĩ như vậy là tốt đấy. Một cuộc bầu cử để lại oán hận về sau,\\nsẽ trở thành nguyên nhân gây tổn hại đến sự phát triển của Ohitoyo.」"
"2260" = "「Chính xác là vậy ạ, ngài Soutetsu. Hiện tại, chỉ có hai ga là Ohitoyo và Yui.\\nCó thể sự chu đáo như thế này là không cần thiết, nhưng mà――」"
"2369" = "「Cảm ơn em đã nhặt lấy cây gậy tiếp sức quá đỗi nặng nề đối với chị.\\nXin hãy chăm lo cho thành phố Ohitoyo nhé――Trăm sự nhờ em.」"
"2778" = "Tôi, Hibiki và Hachiroku――\\nCùng nhau lái \\x%l8620;#00ffc040;8620%l;#; băng qua Ohitoyo đã được tái sinh."
```

#### 02_Hibiki / 日々姫09_run_with_our_dreams

```toml
[script]
"1906" = "「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Hoàng gia cũ.\\nHiện tại thuộc Đường sắt Ohitoyo, Hachiroku ạ.」"
"2400" = "Vậy mà trong số đó, dù ở cách xa Ohitoyo,\\nnhưng nhiều người đã cất công chọn khách sạn tàu hỏa làm nơi lưu trú."
"2708" = "Yui hay Taragi――Về địa điểm đặt khách sạn tàu hỏa,\\nđã có một cuộc tranh luận nảy lửa chia rẽ cả Đường sắt Ohitoyo."
```

#### 02_Hibiki / 日々姫09_静かなる開戦

```toml
[script]
"1459" = "「Bảo là di chuyển cùng lúc nhiều toa xe,\\nchứ Đường sắt Ohitoyo đâu cần nhiều toa xe đến thế——Ư!」"
"1499" = "「Nhưng em lại có những sự tích lũy không thể diễn tả bằng lời.\\nĐôi mắt em đã ngắm nhìn vẻ đẹp của Ohitoyo nhiều hơn bất kỳ ai.」"
"1548" = "「Và cháu. Là hậu bối của đàn chị Houshou Kisaki——Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto——\\ncháu cũng là một hậu bối khá thân thiết với chị ấy.」"
"1557" = "「Nhưng dù vậy, để giúp đỡ chị Paulette,\\nđể bảo vệ Ohitoyo mà cháu yêu quý, cháu——」"
"1662" = "「Tuy nhiên, từ nay về sau, bằng cách dốc toàn lực vào ngành đường sắt,\\ntôi nhất định sẽ thực hiện được việc chấn hưng du lịch thông qua Đường sắt Ohitoyo.」"
"1672" = "「Cháu không muốn thấy Ohitoyo suy tàn, cháu muốn nơi này phát triển,\\ntất nhiên, bản thân cháu cũng có mong muốn đó rất mãnh liệt.」"
"1690" = "「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita,\\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohitoyo, và là \\x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」"
"1694" = "「Em, muốn tất cả mọi người——những người liên quan đến Đường sắt Ohitoyo,\\ncàng nhiều người cùng xem xét ý tưởng đó càng tốt.」"
"1721" = "「Ngân hàng chúng tôi không cảm thấy lo ngại về độ tin cậy của trái phiếu đường sắt Ohitoyo.\\nTuy nhiên, chúng tôi cho rằng cần phải giải tỏa những lo âu mà bài báo này nêu ra.」"
"1723" = "「Tôi nhận định rằng, nếu tôi vẫn tiếp tục kiêm nhiệm cả chức thị trưởng và giám đốc Đường sắt Ohitoyo,\\nthì việc mở rộng kinh doanh hơn nữa là điều không thể.」"
"1749" = "「Vẽ tranh đi, Hibiki.\\nHãy vẽ bức tranh tương lai về thị trấn Ohitoyo mà em hằng mơ ước.」"
"1775" = "「Vì vậy, để bảo vệ môi trường. Dù không thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ncháu vẫn mong kinh tế Ohitoyo nhất định sẽ vực dậy.」"
"1777" = "「Để giải tỏa mối lo ngại này, Ngân hàng Kumamoto chúng tôi,\\nđang chuẩn bị cung cấp khoản vay với lãi suất đặc biệt cho Đường sắt Ohitoyo——」"
"1892" = "「Sắt với mộc thì Ohitoyo dư sức lo được.」"
"2068" = "Chắc chắn sẽ lớn lên thành một sức mạnh to lớn,\\nthành điểm tựa cho một Ohitoyo đang lạc lối hiện tại."
"2333" = "Nếu tôi nhớ không lầm, ông ấy là một trong những nghệ nhân của Ohitoyo.\\nĐã nhờ họ hợp tác mà lại khiến họ bất an, tôi thực sự thấy có lỗi."
"2586" = "Dòng chữ tô điểm cho Kisaki đang phát biểu là\\n『Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto - Houshou Kisaki』."
```

#### 02_Hibiki / 日々姫10_稀咲の未来図、日々姫の未来図

```toml
[script]
"2258" = "「Dù là giao thông, hay sự phát triển của Ohitoyo,\\nbất cứ việc gì cũng nên có nhiều con đường.」"
"2385" = "「Điều chị muốn giao phó cho em, là tương lai của Ohitoyo.」"
"2519" = "「Cùng với việc thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ntôi cảm thấy nếu nó trở thành hai bánh xe thúc đẩy sự phát triển của Ohitoyo thì thật tốt.」"
"2523" = "「Nếu được thêm một nơi mà em yêu thích nhất ở Ohitoyo\\\\nvào bản đồ này, em sẽ chọn gì?」"
"2585" = "「Tôi tin rằng một chính quyền như vậy, rồi sẽ đưa Ohitoyo――\\nphát triển thành một thị trấn nơi mọi người đều có thể sống với nụ cười trên môi.」"
"2592" = "「Em, không vẽ được! Mọi người đã kỳ vọng, đã giao phó cho em――\\nVậy mà, bức tranh tương lai của Ohitoyo, em không vẽ được!!!」"
"2613" = "「Thêm thắt vào sa bàn này để tạo thành một thành phố Ohitoyo khổng lồ——\\\\nKhông, thà làm luôn mô hình quy mô lớn dọc tuyến Yui đi.」"
"2623" = "「Từ bỏ du lịch, tái thiết Ohitoyo thành một thành phố công nghiệp.\\\\nĐối với các kỹ sư và nghệ nhân, đây quả là một kế hoạch hấp dẫn.」"
"2641" = "「Từ ngày mai, nó sẽ được trưng bày tại sảnh chi nhánh Ohitoyo của Ngân hàng Kumamoto.\\nRất mong mọi người sẽ đến xem 『Thành phố \\x%lエアクラ;#00ffc040;Aircra%l;#; Ohitoyo』.」"
"2695" = "「Rồi để mọi người thêm 『khung cảnh Ohitoyo yêu thích của mình』 vào đó.\\\\nPhải làm sao cho ai cũng có thể dễ dàng tham gia. Cụ thể là——」"
"2703" = "「Reina cũng muốn thấy KiHa 07\\\\nchạy trong một Ohitoyo rộng lớn hơn nha!」"
"2704" = "「Reina cũng vậy đó ạ~ Reina cũng muốn cho \\x%lキハ07;#00ffc040;KiHa 07%l;#;\\nchạy trong mô hình thành phố Ohitoyo thu nhỏ đó nha~」"
"2753" = "「Công ty Aero-Craftech luôn hướng tới sự cộng sinh với các phương tiện giao thông truyền thống.\\nĐây không phải là câu chuyện chỉ giới hạn ở Ohitoyo.」"
"2770" = "「Đã vậy, lại còn có mô hình đô thị\\\\n『Thành phố \\\\x%lエアクラ;#00ffc040;Aircra%l;#; Ohitoyo』 hậu thuẫn nữa chứ.」"
"2852" = "「Đó là hình ảnh mô phỏng \\x%l8620;#00ffc040;8620%l;#; của Công ty Cổ phần Đường sắt Ohitoyo.\\nNếu khu dân cư được mở rộng nhờ việc thu hút nhà máy, tầm quan trọng của đường sắt cũng sẽ tăng lên.」"
"2854" = "「Tầm quan trọng đó,\\nchỉ có ở một nơi có khu vực \\x%lエアクラ;#00ffc040;Aircra%l;#; không thể hoạt động như Ohitoyo thôi sao?」"
"2856" = "「Vậy thì, những động thái của Đường sắt Ohitoyo,\\ncũng có sự can thiệp của Ngân hàng Kumamoto sao?」"
"2920" = "「Mô hình đô thị này cũng đẹp thật ạ. Nhưng!\\\\nThiên nhiên Ohitoyo và nước sông Kuma còn đẹp hơn nhiều ạ!」"
"2938" = "「Đầu tiên, tôi muốn hỏi về dự án quy hoạch đô thị\\n『Thành phố Aircra Ohitoyo』 mà cô đã đưa ra trong buổi họp báo tranh cử.」"
"3112" = "Khung cảnh Ohitoyo mà mình yêu thích nhất,\\\\ngần như đồng nghĩa với kỷ niệm quý giá nhất của người đó sao."
"3135" = "Nhưng, nhìn kỹ lại thì, mô hình sa bàn này\\\\nthật hoài niệm... khiến tôi không thể không nghĩ đến khung cảnh Ohitoyo ngày xưa."
"3287" = "Khung cảnh đường sắt đã mất——chỉ một câu nói đó thôi đã đủ để tôi tin chắc.\\\\nSa bàn này, quả nhiên là khung cảnh Ohitoyo ngày xưa."
"3496" = "Một Ohitoyo mà chúng tôi đang nỗ lực tạo ra,\\nđáng lẽ Hibiki đã phải thể hiện nó qua bức tranh."
"3774" = "Mô hình đô thị tỷ lệ 1/1000――\\nKhông phải là Ohitoyo hiện tại, mà là sau khi thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;."
```

#### 02_Hibiki / 日々姫11_御一夜モザイク

```toml
[script]
"1480" = "「——Bức khảm đó tuyệt đối,\\\\nsẽ trở thành một bản đồ tương lai vô cùng tuyệt vời của Ohitoyo.」"
"1989" = "「Bức khảm Ohitoyo——\\\\nBản đồ tương lai kết nối hy vọng của mọi người sao.」"
"1996" = "「Quý khách đã biết 『Cùng nhau tạo nên sa bàn tương lai Ohitoyo』\\\\nlà như thế nào chưa ạ?」"
"2095" = "「Vâng, chúng cháu dự định tập trung vào khu vực thị trấn Ohitoyo, từ đó\\\\nsẽ đơn giản hóa và dựng thành sa bàn quang cảnh dọc tuyến Yui ạ.」"
"2136" = "「Và trên bản đồ tương lai 3D của Ohitoyo do mọi người cùng nhau tạo ra đó,\\\\nchúng cháu dự định sẽ cho \\\\x%l列車;#00ffc040;đoàn tàu%l;#; của chúng ta chạy thử một bước trước——là như vậy ạ.」"
"2143" = "「Vâng. Chúng cháu đang cùng nhau tạo ra\\\\nbản đồ tương lai của Ohitoyo bằng mô hình——là như vậy ạ.」"
"2260" = "「Đó là vì, đây là kết tinh sức mạnh của chúng ta——\\\\ncủa tất cả mọi người ở Ohitoyo.」"
"2464" = "Về cơ bản, họ không mong muốn Ohitoyo thay đổi,\\\\nnên chắc chắn họ không thể nào tích cực ủng hộ việc thu hút nhà máy \\\\x%lエアクラ;#00ffc040;Aircra%l;#; mà họ chẳng có chút cơ hội nào chen chân vào."
"2483" = "Nếu chỉ có khu vực nội thành Ohitoyo thì không đủ.\\\\nBởi vì đường ray là thứ kéo dài và kết nối mọi thứ lại với nhau."
"2531" = "Thực sự rất vui.\\\\nTrong \"Ohitoyo mơ ước\" do một người xa lạ nào đó vẽ nên."
"2804" = "Và những người đã khiến tôi có suy nghĩ đó,\\\\nchính là những người yêu mến Ohitoyo hiện tại, và đang sống ở nơi đây."
"3032" = "（Bảo vệ Ohitoyo hiện tại, bảo vệ sông Kuma,\\\\nkhông chỉ là bảo vệ lịch sử, mà còn là kiến tạo tương lai.）"
```

#### 02_Hibiki / 日々姫13_討論会

```toml
[script]
"945" = "「――Vì vậy, Ohitoyo sẽ ổn thôi.\\nKhông cần dựa dẫm vào nhà máy, nó sẽ trở thành một thị trấn tuyệt vời hơn nữa.」"
"947" = "「――Có rất nhiều tâm tư, có rất nhiều tòa nhà,\\nvà nhờ đó, mới tạo nên Ohitoyo của hiện tại――」"
"955" = "「――Sa bàn này được tạo ra bởi chính bàn tay của mọi người,\\nlà bức tranh tương lai của Ohitoyo do mọi người vẽ nên.」"
"1206" = "「Và nhất định, phải kết nối nó với Ohitoyo hiện tại.」"
"1222" = "「Không đâu, tiền bối. Tôi chỉ có thể vẽ những gì mình nhìn thấy.\\nĐây chính là Ohitoyo của hiện thực.」"
"1234" = "「Để hỗ trợ sự phồn vinh của các địa phương khác,\\nmà Ohitoyo phải hy sinh thì thật là nực cười.」"
"1236" = "「Nhưng chính vì là sự thay đổi chậm rãi――tương lai được vẽ ra ở đó,\\nsẽ kết nối với Ohitoyo hiện tại mà không hề bị bóp méo.」"
"1239" = "「Cô không nghĩ vậy sao?\\nHiện thực――Ohitoyo hiện tại, rất đẹp.」"
"1390" = "「Với nhiều công dân ở đây, có lẽ đây là lần đầu tiên chúng ta gặp mặt.\\nTên tôi là Houshou Kisaki. Là ứng cử viên cho chức thị trưởng Ohitoyo.」"
"1395" = "「Đó là bởi vì, tất cả những người đang sống ở Ohitoyo hiện tại,\\nmỗi người đều đã biến những điều mình yêu thích nhất thành hiện thực.」"
"1396" = "「Nền kinh tế hiện tại của Ohitoyo đang trì trệ.\\nĐó, tóm lại chính là kết quả của việc tin tưởng――」"
"1407" = "「Dù vậy, tôi. Vẫn muốn làm như thế.\\nTôi nghĩ rằng, chúng ta nên tin tưởng vào người dân Ohitoyo.」"
"1596" = "「Về chính trị, từ trước đến nay tôi chưa từng suy nghĩ sâu sắc.\\nNhưng, tôi vẫn luôn dõi theo thị trấn Ohitoyo này.」"
"1642" = "「Đúng…… vậy nhỉ.\\nBan đầu, anh chỉ muốn báo đáp công ơn của Ohitoyo, của nhà Migita.」"
"1669" = "「Vậy thì tại sao――à ừm, tất nhiên là\\nđể bảo vệ nguồn nước của Ohitoyo rồi…… nhưng, chỉ vì thế thôi sao?」"
"1963" = "Trong mô hình đô thị, bản thân thị trấn Ohitoyo cũng\\nđược khắc họa như một bức tranh tương lai."
"1999" = "Lời nói vừa rồi là một sự lỡ lời, có thể bị coi là sự xúc phạm đối với công dân Ohitoyo,\\ncũng như là sự thừa nhận về sự yếu kém của chính ngân hàng."
"2050" = "Để bức tranh thể hiện tương lai của Ohitoyo đó,\\nđược nhiều người nhìn thấy hơn nữa――"
"2269" = "Giữa những nụ cười, nụ cười và nụ cười, một Ohitoyo tràn ngập nụ cười.\\n\\x%l8620;#00ffc040;8620%l;#; và \\x%lキハ07;#00ffc040;KiHa 07%l;#;S cùng \\x%l客車;#00ffc040;toa hành khách%l;#; mới, đang chở chúng tôi băng băng chạy."
```

#### 02_Hibiki / 日々姫16_夢を乗せて

```toml
[script]
"1372" = "……Lắp đặt đồng hồ búp bê trước ga Ohitoyo,\\nđể biến nó thành biểu tượng du lịch của Ohitoyo."
"1584" = "「Không sao đâu. Cho họ xem luôn cũng được. Cho mọi người ở Ohitoyo thấy, người chồng tuyệt vời của em.」"
"1601" = "「Cả búp bê và đồng hồ, chúng tôi sẽ nhờ các nghệ nhân của Ohitoyo chế tác――\\nvà muốn biến nó thành một biểu tượng mang đậm màu sắc Ohitoyo hơn nữa.」"
"1850" = "「Em muốn biến Ohitoyo thành một thành phố tuyệt vời hơn nữa. Vì em muốn mọi người sẽ nở nụ cười nhiều hơn nữa.」"
"1929" = "「Cuối cùng, tôi xin hỏi về việc chỉnh trang khu vực trước ga Ohitoyo.」"
"1950" = "「Tàu tốc hành du lịch khứ hồi Yunoi, \"SL Ohitoyo\" chuẩn bị khởi hành!」"
"1971" = "「Quả không hổ danh thị trưởng, cảm ơn cô vì một bản sửa đổi tuyệt vời.\\nNếu làm thế này, sức hấp dẫn của Ohitoyo sẽ được truyền tải tốt hơn nhỉ.」"
"1981" = "「Đúng là \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; có lẽ là biểu tượng mới của Ohitoyo.\\nNhưng, đặc sản thực sự đại diện cho Ohitoyo, chính là ngựa gỗ Kiji truyền thống.」"
"1996" = "「Khi nào quay lại ga Ohitoyo, cho anh xin một chút thời gian được không. Anh có chuyện quan trọng muốn nói.」"
"2277" = "Tất cả đều là đặc sản của Ohitoyo.\\nKhông thể nào so sánh xem cái nào là nhất, để mà xếp hạng được."
"2304" = "Thực tế, Ohitoyo đã từng như vậy. Dù nhắm mắt làm ngơ trước những nhược điểm to lớn, họ vẫn mong muốn thu hút nhà máy."
"2374" = "Để làm được điều đó, việc trao đổi ý kiến và tranh luận một cách nghiêm túc,\\nrốt cuộc, mới là cách thể hiện chính xác nhất ý nguyện của người dân Ohitoyo."
"2495" = "Từ Ohitoyo này——từ \\x%l運転台;#00ffc040;buồng lái%l;#; của chiếc \\x%l8620;#00ffc040;8620%l;#; này. Bất kể là đi đến đâu."
"2499" = "Trên sân ga Ohitoyo, có rất nhiều người đang chờ đợi."
"2561" = "Nghe nói trong phần \"Hướng dẫn Ohitoyo\", một trong những điểm nhấn của \\x%l列車;#00ffc040;đoàn tàu%l;#; du lịch, cô ấy còn làm xuất sắc hơn cả hai người xuất thân từ địa phương này."
"2701" = "Tấm áp phích do Hibiki vẽ, kết nối những nụ cười của mọi người ở Ohitoyo."
```

#### 02_Hibiki / 日々姫h6_オリエンテーリング借り物競走（ペア）

```toml
[script]
"2258" = "「Ừm. Có lẽ đó cũng chính là phản ứng của những người\\nlần đầu tiên biết đến Đại hội thao do khu phố thương mại Ohitoyo tổ chức đấy」"
"2309" = "「Ở Đế đô có thể là vậy, nhưng ở Ohitoyo\\nngười ta toàn trồng dưới đất thôi――Nhìn kìa!」"
"2442" = "「Anh thấy đó là một tập quán tuyệt vời mà?\\nĐại hội thao do khu phố thương mại Ohitoyo tổ chức ấy」"
"2589" = "「Cũng có thể nói vậy. Anh không ghét việc vận động cơ thể hết mình,\\nvới lại, đây cũng là một sự kiện mang tính lịch sử, gắn kết toàn bộ Ohitoyo lại với nhau mà」"
"3039" = "Sân nhà của Hibiki. Nơi có biết bao nhiêu đồng minh của em ấy,\\ntrong thị trấn của chúng tôi――tại Ohitoyo."
"3698" = "（Ra vậy. Không cần phải cất công đi đường vòng,\\ntừ lúc làm bảng hiệu đến giờ, thị trấn Ohitoyo luôn――）"
```

## Kết bài

Đợt U1a hoàn tất: **221/221 dòng** "Ohimitera" còn lại trong 3 folder 00_Common (0), 01_Hachiroku (45), 02_Hibiki (176) đã được sửa thành "Ohitoyo", mỗi dòng đều đối chiếu JP có 御一夜, không dòng nào bị flag, không dòng nào phải sửa lại sau second pass. 90 dòng còn lại của T1-Ohimitera thuộc các batch song song (U1b 03–06: 52 dòng, đã gộp ~11:10; U1c 07–11: 38 dòng, đang chạy); sau cả ba đợt, T1-Ohimitera còn 0 dòng. Các dạng chồng chéo trong cùng dòng ("Đường sắt Ohito" trần, "Yui", "Jutsu-sen", "Đường sắt Hoàng gia") được giữ nguyên đúng phạm vi, để cho đúng item của chúng.
