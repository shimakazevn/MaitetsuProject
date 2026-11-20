# Audit — 仲国02_北琴の鉄道.txt.toml (route 10_Chikuni)

- File: `仲国02_北琴の鉄道.txt.toml` — route 10_Chikuni, 448 dòng script (Soutetsu 104, độc thoại 136, Hibiki 58, Jiang 48, Suika 46, Hachiroku 45, Zhihuan 11). Nội dung: đoàn Soutetsu–Hibiki–Hachiroku đến ga Bắc Cầm (Beiqin) ở Zhongguo để khảo sát — gặp thư ký Jiang Yehuang, Railord Suika (Dongfu 4 2000) và lái tàu Liu Zhihuan; vướng kiểm tra an ninh gắt gao ở ga (mua vé xong phải ra ngoài rồi vào lại, kiểm tra lại), Hibiki suýt bị thu sổ phác thảo vì vẽ đầu máy; giải thích hệ thống vé/điểm dừng/tàu nhanh K – đặc khoái T – trực đạt đặc khoái Z, toa giường mềm/cứng, Lục Bỉ Xa (tàu xanh lá); kết bằng việc quyết định lịch trình (lên tàu sáng ngày mốt, tham quan Bảo tàng Lịch sử Đường sắt Zhongguo).
- Phương pháp: đọc từng dòng VN đối chiếu JP + TW từ CSV3 (Trang tính 3), kiểm tra chéo sweep, quét máy các mẫu っ / Ohito / Hinamoto / %l.
- Kết quả: **14/448 dòng sai (3,1%)**.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, khóa khớp TOML tuyệt đối 448/448, VN rỗng 0. `[selections]` rỗng. Không có thẻ `%l` sai định dạng (7 thẻ, cân bằng mở/đóng). Không có bản sao file này (md5 `84d160b68d227bb3fd574c8a1fbb83f7`, 1 copy trong `10_Chikuni/`). 291 dòng CSV/TOML khác nhau chỉ do TOML-2 làm phẳng `\n` literal thành khoảng trắng — không phải lỗi, CSV3 là chuẩn.
- Phân loại (14): thuật ngữ 8 (1685, 2262, 2388, 2984, 2985, 2996, 3164, 3264 — toàn bộ 御一夜→Ohitoyo: 5× "Ohito" + 3× "Ohimitera", sửa trực tiếp trong audit theo tiền lệ ハチロク03/ハチロク07/ハチロク09_採決 — KHÔNG thêm lại vào hàng đợi thống nhất), đại từ 2 (2026 Soutetsu "cậu"→"cô" với Jiang; 2182 Soutetsu "cậu"→"em" với Hibiki — xem ghi chú mơ hồ bên dưới), dịch sai nghĩa 3 (2255 特急→"đặc cấp"; 2497 + 3192 独り言→"nói mớ"), gasp 1 (2231 っ đầu dòng sweep bỏ sót).
- Sweep kiểm chứng: 4 mục cho file này — nhận 0 fix từ sweep (3 already-rendered: 2171 っ!!!!→"Á!!!!", 2186 っ!?→"Hả!?", 2232 っ!!!?→"Á!!!?"; 1 needs-file-audit 3294 （ぐ～～っ）→"(Rột~~)" đã xử lý: tiếng bụng sôi đã diễn đủ, KHÔNG sửa); quét máy bổ sung bắt thêm 1 gasp sweep bỏ sót (2231). Không còn っ thô trong VN sau fix.
- Soutetsu "tôi" đúng toàn file với Hachiroku/Jiang/Zhihuan/Suika (0 dòng "anh" sai đối tượng); "tôi" với Hibiki ở độc thoại là ngoại lệ độc thoại nội tâm, giữ. Hibiki "chị" với Suika (2590, 2682, 2720) đúng — Suika là Railord nhỏ tuổi hơn; Hibiki "em" với Hachiroku (2103) đúng.
- Không có thuật ngữ nào khác chờ đợt thống nhất trong file (0 Hinamoto, 0 Yui, 0 Migita System, 0 túi công tác, 0 Seki).

## Chi tiết từng dòng sai

### 1685 — 双鉄 — thuật ngữ
- JP: 「……目指さねばならんな。僕らの御一夜鉄道も。\nより深く、より広く、人々の暮らしと共にあることを」
- TW: 「……我們御一夜鐵路也必須要以此為目標才行——要更深入、更廣泛地融入到人們的生活中去」
- Cũ: 「……Chúng ta cũng phải hướng tới điều đó thôi. Cả Đường sắt Ohito của chúng ta nữa.\nPhải đồng hành cùng cuộc sống của mọi người một cách sâu sắc hơn, rộng lớn hơn.」
- Mới: 「……Chúng ta cũng phải hướng tới điều đó thôi. Cả Đường sắt Ohitoyo của chúng ta nữa.\nPhải đồng hành cùng cuộc sống của mọi người một cách sâu sắc hơn, rộng lớn hơn.」
- Lý do: 御一夜 = "Ohitoyo" (quyết định 20/11); "Ohito" là dạng cũ, sửa trong audit.

### 2026 — 双鉄 — đại từ
- JP: 「すみません、ありがとうございます」
- TW: 「不好意思，非常感謝」
- Cũ: 「Xin lỗi, cảm ơn cậu nhiều.」
- Mới: 「Xin lỗi, cảm ơn cô nhiều.」
- Lý do: Soutetsu nói với Jiang — cô ấy là chủ nhà mời ăn (Jiang nói tiếp ở 2028 về món vịt), câu dùng ございます trang trọng; Soutetsu gọi Jiang là "cô" ở mọi dòng khác trong file (2120, 2293, 2398, 2538, 2627, 2732). "Cậu" sai đối tượng.

### 2182 — 双鉄 — đại từ (có mơ hồ — xem "Chờ Hieu")
- JP: 「ははっ。本当に困らせているな。すまない。\nならばかしこまるのはやめよう。いいな？　日々姫」
- TW: 「哈哈。還真是讓你為難了，抱歉。那我們還是不要說太複雜的敬語了吧。好嗎，日日姬」
- Cũ: 「Haha. Đúng là làm cậu bối rối thật rồi. Xin lỗi nhé.\nVậy thì chúng ta đừng khách sáo nữa. Được chứ? Hibiki.」
- Mới: 「Haha. Đúng là làm em bối rối thật rồi. Xin lỗi nhé.\nVậy thì chúng ta đừng khách sáo nữa. Được chứ? Hibiki.」
- Lý do: câu kết thúc bằng cách gọi thẳng Hibiki ("いいな？日々姫"), nên người nghe là Hibiki → Soutetsu gọi "em" (khớp 2083, 2504, 2505 trong file). "Cậu" sai cả hai cách đọc — xem ghi chú mơ hồ.

### 2231 — 西瓜 — gasp (sweep bỏ sót)
- JP: 「っ！！　[ｚｈｉｈｕａｎ,1]志寰！！！」
- TW: 「啊！！志寰！！！」
- Cũ: 「!! \x%lｚｈｉｈｕａｎ;#00ffc040;Zhihuan%l;#;!!!」
- Mới: 「Ư!! \x%lｚｈｉｈｕａｎ;#00ffc040;Zhihuan%l;#;!!!」
- Lý do: っ ở đầu dòng, VN cũ chỉ còn "!!" — âm gasp mất hoàn toàn. Theo ranh giới gasp đã khóa 20/11 (thêm Ư khi âm っ mất hoàn toàn, kể cả đầu dòng). Sweep không có mục cho dòng này. Thẻ %l giữ nguyên.

### 2255 — 双鉄 — dịch sai nghĩa (thuật ngữ)
- JP: 「ほう。同じ漢字圏ならではの面白さだな。\nならば――特急列車もそのまま特急になるのかな」
- TW: 「噢，這真是同在漢字文化圈的醍醐味啊。這麼說，特急列車同樣也是特急二字嗎」
- Cũ: 「Ồ. Đúng là điều thú vị chỉ có ở những nước cùng chung vùng văn hóa chữ Hán nhỉ.\nNếu vậy thì——tàu tốc hành đặc biệt cũng giữ nguyên là đặc cấp sao?」
- Mới: 「Ồ. Đúng là điều thú vị chỉ có ở những nước cùng chung vùng văn hóa chữ Hán nhỉ.\nNếu vậy thì——tàu tốc hành đặc biệt cũng giữ nguyên là tốc hành đặc biệt sao?」
- Lý do: 特急 = tàu tốc hành đặc biệt — chính câu này đã dùng "tàu tốc hành đặc biệt" cho 特急列車, và 2683 cũng vậy; "đặc cấp" (cấp đặc biệt) dịch sai từ, không có trong thuật ngữ đường sắt.

### 2262 — ハチロク — thuật ngữ
- JP: 「御一夜鉄道史で申しますと……\nナインスターズが初走行を果たす、その二年前ですね」
- TW: 「在御一夜鐵路史的年表上看的話……就是九星初次運營成功之前的兩年」
- Cũ: 「Nếu nói theo lịch sử Đường sắt Ohito thì……\nĐó là hai năm trước khi Nine Stars có chuyến chạy đầu tiên nhỉ.」
- Mới: 「Nếu nói theo lịch sử Đường sắt Ohitoyo thì……\nĐó là hai năm trước khi Nine Stars có chuyến chạy đầu tiên nhỉ.」
- Lý do: 御一夜 = "Ohitoyo".

### 2388 — 日々姫 — thuật ngữ
- JP: 「は、はじめまして。右田日々姫です。御一夜鉄道所属の\n車輌デザイナーで、機関士・機関助士も務めています」
- TW: 「您、您好。我叫右田日日姬，在御一夜鐵路擔任車輛設計師，同時兼任司機和司爐」
- Cũ: 「R, rất vui được gặp cô. Tôi là Migita Hibiki. Nhà thiết kế toa xe thuộc Đường sắt Ohimitera,\nđồng thời cũng là lái tàu và phụ lái tàu.」
- Mới: 「R, rất vui được gặp cô. Tôi là Migita Hibiki. Nhà thiết kế toa xe thuộc Đường sắt Ohitoyo,\nđồng thời cũng là lái tàu và phụ lái tàu.」
- Lý do: 御一夜 = "Ohitoyo"; "Ohimitera" là dạng cũ.

### 2497 — ハチロク — dịch sai nghĩa
- JP: 「はい！　そのような心の動きでもれてきた、\nいわゆる、これは、独り言かと」
- TW: 「正是！她心裡現在正是這麼想的，也就是說，這是在自言自語」
- Cũ: 「Vâng! Những chuyển động trong tâm trí như vậy đã vô tình bộc lộ ra ngoài,\ncái này, người ta thường gọi là nói mớ nhỉ.」
- Mới: 「Vâng! Những chuyển động trong tâm trí như vậy đã vô tình bộc lộ ra ngoài,\ncái này, người ta thường gọi là nói một mình nhỉ.」
- Lý do: 独り言 = nói một mình / tự nói với mình (JP và TW 自言自語 đều xác nhận); "nói mớ" là nói trong lúc ngủ (寝言), sai nghĩa.

### 2984 — monologue — thuật ngữ
- JP: 8620を模したボードに描かれているのは、\n『歓迎！　御一夜鉄道御一行』の文字。
- TW: 在做成８６２０形狀的板子上，寫著“歡迎御一夜鐵路貴賓一行！”。
- Cũ: Trên tấm bảng mô phỏng 8620 có viết dòng chữ\n『Hoan nghênh! Phái đoàn Đường sắt Ohimitera』.
- Mới: Trên tấm bảng mô phỏng 8620 có viết dòng chữ\n『Hoan nghênh! Phái đoàn Đường sắt Ohitoyo』.
- Lý do: 御一夜 = "Ohitoyo".

### 2985 — monologue — thuật ngữ
- JP: 御一夜がもっとも賑わう赤井さんの“おくんち”でも、\nこれほどまでの盛況を見ることは難しかろう。
- TW: 在御一夜，即便是頂頂熱鬧的赤井神社“秋大祭”，怕是也難見如此場面吧。
- Cũ: Ngay cả trong lễ hội mùa thu "Okunchi" náo nhiệt nhất của đền Akai ở Ohimitera,\nchắc cũng khó mà thấy được cảnh tượng đông đúc đến mức này.
- Mới: Ngay cả trong lễ hội mùa thu "Okunchi" náo nhiệt nhất của đền Akai ở Ohitoyo,\nchắc cũng khó mà thấy được cảnh tượng đông đúc đến mức này.
- Lý do: 御一夜 = "Ohitoyo". ("Lễ hội mùa thu" theo TW 秋大祭, giữ.)

### 2996 — monologue — thuật ngữ
- JP: 仲国版のナインスターズ計画の草案を立案できたなら、\nその経験は、必ず御一夜鉄道に……も……？
- TW: 如果能成功擬定仲國版九星的設計方案的話，這過程中積累的經驗，想必也能對御一夜鐵路——
- Cũ: Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohito……?
- Mới: Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……?
- Lý do: 御一夜 = "Ohitoyo".

### 3164 — monologue — thuật ngữ
- JP: 御一夜鉄道の特殊な環境それゆえに、\n僕らはついつい、その点を失念しがちだが……
- TW: 畢竟御一夜鐵路環境特殊，而身處其中的我們，也漸漸將這麼重要的事情忘在了腦後……
- Cũ: Vì môi trường đặc thù của Đường sắt Ohito,\nnên chúng tôi thường hay vô tình quên mất điểm đó, nhưng……
- Mới: Vì môi trường đặc thù của Đường sắt Ohitoyo,\nnên chúng tôi thường hay vô tình quên mất điểm đó, nhưng……
- Lý do: 御一夜 = "Ohitoyo".

### 3192 — monologue — dịch sai nghĩa
- JP: 独り言を漏らした背景などは、\n本人もなかなか自覚しづらいことだろう。
- TW: 自言自語背後隱藏的含義，本人怕是也很難意識到吧。
- Cũ: Bản thân người nói mớ chắc cũng khó mà tự nhận thức được\nbối cảnh khiến họ thốt ra những lời đó.
- Mới: Bản thân người nói một mình chắc cũng khó mà tự nhận thức được\nbối cảnh khiến họ thốt ra những lời đó.
- Lý do: 独り言 = nói một mình (TW 自言自語), không phải "nói mớ" (nói trong lúc ngủ). Cùng lỗi với 2497.

### 3264 — monologue — thuật ngữ
- JP: 完全指定制のナインスターズ等観光列車では見られんし、\n御一夜鉄道の全普通列車でお目にかかれることも無い。
- TW: 這種情況不僅不會出現在全指定座的九星上，就是在御一夜鐵路的全普通座列車上也未曾一見。
- Cũ: Cảnh tượng này không thể thấy trên các chuyến tàu du lịch chỉ định chỗ ngồi hoàn toàn như Nine Stars,\nvà cũng chưa từng thấy trên toàn bộ các chuyến tàu thông thường của Đường sắt Ohito.
- Mới: Cảnh tượng này không thể thấy trên các chuyến tàu du lịch chỉ định chỗ ngồi hoàn toàn như Nine Stars,\nvà cũng chưa từng thấy trên toàn bộ các chuyến tàu thông thường của Đường sắt Ohitoyo.
- Lý do: 御一夜 = "Ohitoyo".

## Các dòng đã kiểm tra kỹ và GIỮ NGUYÊN (không sửa)

- 2204 はうっ→"Hau...": giữ theo quy ước toàn dự án (tiền lệ ROUTE-AUDIT.md: はうっ→"Hau" đã kiểm chứng bằng CSV3; "…" diễn đạt ngắt âm). Không thêm Ư.
- 2225 あっ→"A.": giữ theo quy ước toàn dự án (あっ→"A" đã kiểm chứng; tiền lệ ハチロク03).
- 2212 あ…………んっ――→"A…………ưm——": んっ đã diễn thành "ưm", không nhân đôi.
- 2173 あっ――→"A——", 2450/2451 日々姫っ→"Hibiki!", 2743 にぃにっ→"Anh hai!!!", 2745 助けてっ→"cứu em với!": っ dính từ có nội dung / đã diễn bằng dấu câu, không thêm Ư (ranh giới gasp 20/11).
- 2178 うふふっ→"Ufufu": tiếng cười, không phải gasp. (Phần ははっ→"Haha" trong dòng 2182 cũng giữ nguyên — dòng 2182 chỉ sửa đại từ "cậu"→"em".)
- 3294 （ぐ～～っ）→"(Rột~~)": tiếng bụng sôi đã diễn đủ (sweep "needs-file-audit" — đã xử lý, không sửa).
- 2360 「我叫西瓜」→"Ngã khiếu Xigua" và 2489 「歓迎来到北琴」→"Hoan nghênh lai đáo Bắc Cầm": Suika nói tiếng Trung trong JP gốc — VN giữ dạng Hán-Việt là cố ý, không phải rò rỉ tiếng nước ngoài.
- 2632 「かしこままれる――んんっ？　かしこまむらる」→"Khách xáo——hửm? Khách xạo.": Zhihuan nói ngọng, VN diễn lại bằng cặp từ ngọng tương ứng, giữ.
- 2483 北開道/京塗/九洲→"Hokukaido, Kyonuri, Kyushuu": tên địa danh hư cấu (tương tự Hokkaido/Kyoto/Kyushu), phiên âm giữ.
- 2634 danh sách thành phố (Tây An, Tây Ninh, Thánh Đô, Khôn Minh, Hạ Môn, Nam Cầm, Tô Châu, Quảng Châu, Cáp Nhĩ Tân, Thượng Hải, Hồng Cảng): phiên âm nhất quán với tên hư cấu JP, giữ.
- 2210 「なんが、こうがの『が』は『臥』ですか？」→ hỏi về chữ "Giường" trong giường mềm/cứng: diễn đạt gọn, giữ.
- 2025–2026: xem 2026 đã sửa; 2025 ("bụng tôi đã réo lên") đúng.
- 2700/2717/2200 Soutetsu gọi Zhihuan "cậu": đúng (Zhihuan trẻ hơn, Soutetsu xưng "tôi" với cậu ấy).
- 2590/2682/2720 Hibiki tự xưng "chị": đúng — nói với Suika (Railord nhỏ tuổi).
- 2198 Zhihuan "giúp được chị" (với Hibiki), 2294 Zhihuan "Anh Soutetsu, chị Hibiki": đúng — Zhihuan trẻ nhất nhóm.
- 2701/2749 Hachiroku "Anh Zhihuan": đúng.
- 2297 Suika "xin giới thiệu với ngài Migita, quý cô Migita và Hachiroku": JP cũng lược tân ngữ (giới thiệu ai), VN giữ cấu trúc, không sửa.

## Chờ Hieu (cần quyết, không tự quyết)

- **2182 — người nghe là Hibiki hay Hachiroku?** Câu kết bằng "いいな？日々姫" (gọi Hibiki) nên audit sửa "cậu"→"em" (xưng hô với Hibiki). Nhưng nửa đầu ("本当に困らせているな。すまない。ならばかしこまるのはやめよう" — xin lỗi vì làm ai đó bối rối, bảo đừng khách sáo nữa) cũng có thể hướng về Hachiroku — cô ấy mới là người đang nói năng trang trọng (わたくし/でございます) và vừa bối rối ở 2184. Nếu người nghe là Hachiroku thì phải là "cô", không phải "em". "Cậu" thì sai trong cả hai cách đọc. Hieu/parent quyết giữ "em" hay đổi thành "cô".
- **2356 — "Trăm sự nhờ cậu." (Soutetsu, 「決まりだな。よろしく頼む」) — KHÔNG sửa, giữ nguyên.** Người nghe mơ hồ: Jiang (người sắp xếp vé — thì phải là "cô") hay Zhihuan (người đi cùng — "cậu" đúng). Zhihuan nói ngay sau ở 2359, nhưng chưa đủ chắc để đổi. Cần Hieu xác nhận người nghe.
- Không có câu hỏi thuật ngữ mới nào trong file.

## Kiểm chứng

- JSON `audit-chukuni02-kita-koto-no-tetsudo-wrong.json`: 14 mục, khóa là chuỗi, dạng list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 14/14; mỗi fix chỉ khác old VN đúng chỗ cần sửa (kiểm chứng máy).
- Khối TOML: parse được (tomllib), 14 khóa, 0 sai lệch giá trị so với JSON. Lưu ý build: lần build JSON đầu tiên dùng ký tự xuống dòng thật thay vì `\n` literal của CSV3 — kiểm chứng máy bắt được, đã build lại đúng; giá trị fix không đổi.
- Lượt soát 2 (đọc lại toàn bộ 14 fix đối chiếu JP): **14 tổng / 14 xác nhận lại / 0 bỏ / 0 sửa**.
- Sweep: 4 mục cho file (2171, 2186, 2232 already-rendered — nhận; 3294 needs-file-audit — đã xử lý, không sửa) + 1 gasp sweep bỏ sót (2231, đã sửa).

## Khối TOML (đã kiểm chứng parse)

```toml
"1685" = "「……Chúng ta cũng phải hướng tới điều đó thôi. Cả Đường sắt Ohitoyo của chúng ta nữa.\\nPhải đồng hành cùng cuộc sống của mọi người một cách sâu sắc hơn, rộng lớn hơn.」"
"2026" = "「Xin lỗi, cảm ơn cô nhiều.」"
"2182" = "「Haha. Đúng là làm em bối rối thật rồi. Xin lỗi nhé.\\nVậy thì chúng ta đừng khách sáo nữa. Được chứ? Hibiki.」"
"2231" = "「Ư!! \\x%lｚｈｉｈｕａｎ;#00ffc040;Zhihuan%l;#;!!!」"
"2255" = "「Ồ. Đúng là điều thú vị chỉ có ở những nước cùng chung vùng văn hóa chữ Hán nhỉ.\\nNếu vậy thì——tàu tốc hành đặc biệt cũng giữ nguyên là tốc hành đặc biệt sao?」"
"2262" = "「Nếu nói theo lịch sử Đường sắt Ohitoyo thì……\\nĐó là hai năm trước khi Nine Stars có chuyến chạy đầu tiên nhỉ.」"
"2388" = "「R, rất vui được gặp cô. Tôi là Migita Hibiki. Nhà thiết kế toa xe thuộc Đường sắt Ohitoyo,\\nđồng thời cũng là lái tàu và phụ lái tàu.」"
"2497" = "「Vâng! Những chuyển động trong tâm trí như vậy đã vô tình bộc lộ ra ngoài,\\ncái này, người ta thường gọi là nói một mình nhỉ.」"
"2984" = "Trên tấm bảng mô phỏng 8620 có viết dòng chữ\\n『Hoan nghênh! Phái đoàn Đường sắt Ohitoyo』."
"2985" = "Ngay cả trong lễ hội mùa thu \"Okunchi\" náo nhiệt nhất của đền Akai ở Ohitoyo,\\nchắc cũng khó mà thấy được cảnh tượng đông đúc đến mức này."
"2996" = "Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……?"
"3164" = "Vì môi trường đặc thù của Đường sắt Ohitoyo,\\nnên chúng tôi thường hay vô tình quên mất điểm đó, nhưng……"
"3192" = "Bản thân người nói một mình chắc cũng khó mà tự nhận thức được\\nbối cảnh khiến họ thốt ra những lời đó."
"3264" = "Cảnh tượng này không thể thấy trên các chuyến tàu du lịch chỉ định chỗ ngồi hoàn toàn như Nine Stars,\\nvà cũng chưa từng thấy trên toàn bộ các chuyến tàu thông thường của Đường sắt Ohitoyo."
```

Kết bài
