# Audit — 日々姫02_文庫森.txt.toml (02_Hibiki)

- File: `日々姫02_文庫森.txt.toml` — route 02_Hibiki, 412 dòng script (độc thoại 166, 双鉄 Soutetsu 105, 日々姫 Hibiki 100, 木本 Kimoto 41). Nội dung: Soutetsu và Hibiki đến thăm gara đầu máy hình quạt ở Bungomori (文庫森機関庫), gặp lão kỹ sư Kimoto; Hibiki phác thảo gara; trò chơi vẽ đoán trên lưng (背中あてっこ, tính điểm đến 10); Kimoto kể lịch sử Đường sắt Kyudai (来大鉄道 — hai tuyến tư nhân hợp nhất, quốc hữu hóa dưới thời 帝鉄, suy tàn vì cơ giới hóa và Aircra), gara hình quạt là biểu tượng của Bungomori; xen cảnh tắm; kết bằng Hibiki tìm thấy "hạt giống" cho bản thiết kế.
- Phương pháp: đọc từng dòng đối chiếu JP + TW từ CSV3 (91.731 dòng), kiểm chứng chéo sweep gasp, kiểm tra đại từ theo quy tắc đã sửa (Soutetsu "anh" với Hibiki), kiểm tra thẻ %l bằng máy.
- Kết quả: **14/412 dòng sai (3,4%)**.

## Phân loại (14)

- Thuật ngữ 7: 扇形機関庫 gloss "hình ngành"→"hình quạt" 5 dòng (1617, 1706, 1831, 1832, 1833); 御一夜→Ohitoyo 2 dòng (1770, 1792 — 1792 hai lần trong một dòng).
- Gasp 4: 1522, 1713, 2051, 2065 — cả 4 đều là mục sweep, đã kiểm chứng đúng (1522 kèm sửa lỗi đánh máy "dang"→"đang").
- Dịch sai nghĩa 2: 1725 (深く "sâu sắc"→"mải mê đến thế"), 2559 (のぼせる "say nắng"→"choáng vì nóng").
- Lỗi đánh máy 1: 2512 ("dang"→"đang").
- Đại từ 0: Soutetsu dùng "anh" đúng toàn bộ thoại với Hibiki; "tôi" chỉ xuất hiện ở độc thoại và 1 dòng liệt kê nhóm (1883, giữ nguyên — xem §4).

## §1. Chi tiết từng dòng sai

### 1522 — 双鉄 — typo + gasp (sweep: lost-gasp-trailing)
- JP: 「けれど、これほどに素晴らしい光景を、日々姫の瞳が映しているとき――っ！」
- TW: 「不過當如此美妙的景象映入你的瞳孔中之時……啊！」
- Cũ: 「Nhưng, khi một khung cảnh tuyệt vời đến thế này,\ndang phản chiếu trong đôi mắt của Hibiki——!」
- Mới: 「Nhưng, khi một khung cảnh tuyệt vời đến thế này,\nđang phản chiếu trong đôi mắt của Hibiki——Ư!」
- Lý do: "dang" là lỗi đánh máy của "đang"; っ cuối dòng bị mất hoàn toàn trong VN cũ (chỉ còn "——!") — thêm Ư theo sweep (TW có 啊). Sweep giữ nguyên "dang", bản này sửa thêm lỗi đánh máy.

### 1617 — 木本 — thuật ngữ
- JP: 「合併した後は、そらあ栄えたもんでした。\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;ば、そん頃に作られた代物ですな」
- TW: 「合併之後的鐵路別提有多繁榮了。\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;就是那時建造出來的偉大建築」
- Cũ: 「Sau khi hợp nhất thì nó phát triển rực rỡ lắm.\n\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; này cũng là thứ được xây dựng vào thời điểm đó.」
- Mới: 「Sau khi hợp nhất thì nó phát triển rực rỡ lắm.\n\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; này cũng là thứ được xây dựng vào thời điểm đó.」
- Lý do: 扇形 = hình quạt (fan-shaped); "hình ngành" không có nghĩa — dịch sai chữ 扇. Thẻ %l giữ nguyên, chỉ sửa gloss.

### 1706 — 双鉄 — thuật ngữ
- JP: 「うむ？　ああ、いや――そうか、日々姫は、\n\x%l扇形機関庫;#00ffc040;扇形機関庫%l;#;に表情を見るのだな――っと」
- TW: 「嗯？啊，感覺，日日姬這是看出了\x%l扇形機関庫;#00ffc040;扇形機車庫%l;#;的表情啊」
- Cũ: 「Hửm? A, không——ra vậy, Hibiki\nđang nhìn biểu cảm của \x%l扇形機関庫;#00ffc040;gara đầu máy hình ngành%l;#; nhỉ——」
- Mới: 「Hửm? A, không——ra vậy, Hibiki\nđang nhìn biểu cảm của \x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; nhỉ——」
- Lý do: như 1617 — 扇形 = hình quạt.

### 1713 — 日々姫 — gasp (sweep: lost-gasp-trailing-mid)
- JP: 「えへ～っ！ えへへ～っ！　\n"ひびき"ば、描いてくれたとねっ！！」
- TW: 「嘿嘿～！嘿嘿嘿～～！阿哥畫的是"響"，是日日姬啊！！」
- Cũ: 「Ê he~! Ê he he~!\nAnh vẽ "âm vang" (Hibiki) cho em đó hả!!」
- Mới: 「Ê he~Ư! Ê he he~Ư!\nAnh vẽ "âm vang" (Hibiki) cho em đó hả!!」
- Lý do: hai っ sau ~ bị mất trong VN cũ — thêm Ư theo sweep, khớp nguyên tắc "không để mất âm". ねっ cuối câu là tiểu từ nhấn mạnh, không phải âm thanh — giữ nguyên (sweep cũng không cờ).

### 1725 — 日々姫 — dịch sai nghĩa
- JP: 「にぃにが守ってくれるってわかっとるけん。\nやけん、わたし、こぎゃんと深く――って、あああ」
- TW: 「因為我知道阿哥在這裡守著我。不然哪能這麼投入……哎呀，哇哇哇」
- Cũ: 「Vì em biết anh hai sẽ bảo vệ em.\nNên em mới có thể sâu sắc——á, a a a.」
- Mới: 「Vì em biết anh hai sẽ bảo vệ em.\nNên em mới có thể mải mê đến thế——á, a a a.」
- Lý do: こぎゃんと深く = "chìm sâu/mải mê đến thế" (TW: 這麼投入); "sâu sắc" (profound) sai nghĩa trong ngữ cảnh này.

### 1770 — 木本 — thuật ngữ
- JP: 「[おひとよ,2]御一夜もですか」
- TW: 「御一夜也一樣嗎？」
- Cũ: 「Ohimitera cũng vậy sao?」
- Mới: 「Ohitoyo cũng vậy sao?」
- Lý do: 御一夜 = "Ohitoyo" theo quyết định 19/11; "Ohimitera" là dạng cũ sai.

### 1792 — 双鉄 — thuật ngữ (2 lần trong 1 dòng)
- JP: 「僕らの全てが、つながっている。\nならばこれは――御一夜――そして、御一夜鉄道だ」
- TW: 「我們全部連接在了一起。那這就是……御一夜，也就是御一夜鐵路」
- Cũ: 「Tất cả chúng ta, đều được kết nối với nhau.\nVậy thì đây là——Ohimitera——và, Đường sắt Ohimitera.」
- Mới: 「Tất cả chúng ta, đều được kết nối với nhau.\nVậy thì đây là——Ohitoyo——và, Đường sắt Ohitoyo.」
- Lý do: như 1770, cả hai lần "Ohimitera" trong dòng đều sửa.

### 1831 — 日々姫 — thuật ngữ
- JP: 「[せんけい,1]扇形機関庫……すごい！　かわいい」
- TW: 「扇形機車庫……好棒啊！太可愛了」
- Cũ: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#;……Tuyệt quá! Dễ thương quá đi.」
- Mới: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;……Tuyệt quá! Dễ thương quá đi.」
- Lý do: như 1617 — 扇形 = hình quạt.

### 1832 — 双鉄 — thuật ngữ
- JP: 「[せんけい,1]扇形機関庫、か――」
- TW: 「扇形機車庫啊」
- Cũ: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#;, sao——」
- Mới: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;, sao——」
- Lý do: như 1617.

### 1833 — 木本 — thuật ngữ
- JP: 「[せんけい,1]扇形機関庫ば、文庫森に初めてできた、\n大きな大きなシンボルでしたけん――失くせんですわ」
- TW: 「扇形機車庫是在豐後森出現的第一個極其重要的標誌——絕不能讓它消失」
- Cũ: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình ngành%l;#; là biểu tượng vô cùng lớn lao\nlần đầu tiên xuất hiện ở Bungomori——không thể để mất được.」
- Mới: 「\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; là biểu tượng vô cùng lớn lao\nlần đầu tiên xuất hiện ở Bungomori——không thể để mất được.」
- Lý do: như 1617. Sau khi sửa, file không còn "hình ngành" nào (đủ 5/5 dòng).

### 2051 — 日々姫 — gasp (sweep: lost-gasp-trailing-mid)
- JP: 「にぃに、いつからそんな――っ！！\nごめんっ！　ごめんなさいっ！！？」
- TW: 「阿哥是什麼時候站在那裡的……啊！！對不起！真的很對不起！！」
- Cũ: 「Anh hai, từ lúc nào mà anh lại——!!\nXin lỗi! Em xin lỗi!!?」
- Mới: 「Anh hai, từ lúc nào mà anh lại——Ư!!\nXin lỗi! Em xin lỗi!!?」
- Lý do: っ sau ―― bị mất hoàn toàn — thêm Ư theo sweep (TW có 啊). Hai っ trong ごめんっ/ごめんなさいっ là nhấn mạnh đã được "!" diễn đạt — giữ nguyên.

### 2065 — 日々姫 — gasp (sweep: lost-gasp-trailing)
- JP: 「食堂車――\n食堂車っ！　ハードル高すぎ～～っ！！」
- TW: 「餐車……餐車！難度太高了～～！！」
- Cũ: 「Toa ăn——\nToa ăn á! Rào cản cao quá đi mất~~!!」
- Mới: 「Toa ăn——\nToa ăn á! Rào cản cao quá đi mất~~Ư!!」
- Lý do: ～～っ cuối dòng bị mất — thêm Ư theo sweep. 食堂車っ đã được "á!" diễn đạt nên không thêm Ư ở đó.

### 2512 — monologue — lỗi đánh máy
- JP: ちらほらと、地元の方らしい人たちが、\n僕らのまわりを遠巻きにして、様子を見ている。
- TW: 看起來像當地人的零星路人們都躲得遠遠的，圍觀著我們。
- Cũ: Lác đác vài người có vẻ là người dân địa phương,\ndang đứng thành vòng tròn quanh chúng tôi để theo dõi.
- Mới: Lác đác vài người có vẻ là người dân địa phương,\nđang đứng thành vòng tròn quanh chúng tôi để theo dõi.
- Lý do: "dang" là lỗi đánh máy của "đang". Quét máy toàn file: chỉ 2 dòng chứa "dang" (1522, 2512), cả hai đều đã sửa.

### 2559 — monologue — dịch sai nghĩa
- JP: 抱き止めた肌は、ぽかぽかだ。\nのぼせる寸前なのかもしれない。
- TW: 被我一把抱住的她身上熱呼呼的，我看她已經快泡暈了。
- Cũ: Làn da tôi ôm lấy đang nóng bừng.\nCó lẽ con bé sắp bị say nắng đến nơi rồi.
- Mới: Làn da tôi ôm lấy đang nóng bừng.\nCó lẽ con bé sắp choáng vì nóng đến nơi rồi.
- Lý do: のぼせる trong cảnh tắm (bồn tắm, key 2438) là choáng vì nước nóng; "say nắng" chỉ say nắng ngoài trời — sai ngữ cảnh. TW 泡暈 (choáng vì ngâm nóng) xác nhận.

## §2. Kiểm tra lệch vị trí / xoay / nhiễm / mồ côi / chưa dịch / trùng khóa

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất, 412/412 khóa khớp TOML tuyệt đối. VN TOML khớp CSV3 modulo flatten `\n`→khoảng trắng đã biết (251 dòng; chỉ 1 dòng chênh lệch khoảng trắng thừa sau khi chuẩn hóa: 1614, không ảnh hưởng nội dung).
- Giá trị VN trùng nhau duy nhất: 「Ây da.」 ở 1635 và 1659 — cả hai JP đều là 「おっと」, lặp hợp lệ, không phải lệch.
- `[selections]` rỗng (0 mục). Không có thẻ `%l` sai định dạng (quét máy: mở/đóng cân bằng toàn file, 58 lần `%l` trong TOML). Không có bản sao file này (md5 `29f4cac3a73d38f175346da6ffa3482c`, không trùng file nào khác trong sources/toml2/).
- `[characters]`/`[character_subs]` đúng: 日々姫→Hibiki, 木本→Kimoto, 老人→Ông lão, 日日姬→Hibiki, 雙鐵→Soutetsu.

## §3. Sweep gasp kiểm chứng

- `sweep-raw-gasp-wrong.json` có 5 mục cho file này: nhận 4 fix (1522, 1713, 2051, 2065 — đã kiểm chứng từng giá trị với JP, áp nguyên; riêng 1522 sửa thêm lỗi đánh máy "dang" mà sweep giữ nguyên); 1 mục already-rendered (1664 むぅ～～っ→"Ưm~~", đúng, không sửa).
- Quét bổ sung bằng tay toàn bộ các dòng JP chứa っ: các dòng còn lại đều đã được diễn đạt (1537 あっ→"A!!", 1592 日々姫っ→"Hibiki!", 1640 えっ→"Hả!?", 1644 わあっ→"oá", 1692 うんっ→"Vâng!", 1694 かなっ→"nhỉ", 1747 わっ→"oá!?", 1967 ええっ→"Hả!?", các SFX 2664/2666/2672/2681/2686/2687/2696/2697 → "Xoẹt"/"Tách"/"Nhoáy"/"loẹt xoẹt"/"Sột soạt" — đều đã có âm). 0 gasp sweep bỏ sót.

## §4. Đại từ — đã kiểm tra, 0 dòng sai

- Soutetsu thoại với Hibiki dùng "anh" nhất quán toàn file (vd. 1558, 1853, 2029 "anh vẽ trước nhé?"); độc thoại dùng "tôi" theo quy tắc chung; với Kimoto (ông lão) dùng "cháu"/"ạ" (2001, 2031) — đúng.
- Kimoto gọi Hibiki "cô" (1570, 1614, 1810, 1898, 2002, 2024) — xưng hô tôn trọng với thị trưởng trẻ, nhất quán, giữ nguyên.
- Hibiki tự xưng "em"/"cháu" đúng; gọi Soutetsu "anh hai" (にぃに) nhất quán.
- 1883 giữ nguyên (không tính sai): 「……Sẽ làm được thôi, chắc chắn.\nNếu là Hibiki, tôi, và mọi người.」 — Soutetsu liệt kê bản thân trong nhóm ("Hibiki, tôi, và mọi người"), theo nguyên tắc nhóm ("bọn tôi" trung tính trong ngữ cảnh nhóm; tiền lệ file 09 key 2637, Paulette 14 key 1544). Nếu Hieu muốn "anh" ở đây vì cảnh thân mật thì báo lại — xem §6.

## §5. Đã kiểm tra và giữ nguyên (không tính sai)

- 60: 鉄道帝有法/日ノ本帝有鉄道 → "Đạo luật Đường sắt Hoàng gia"/"Đường sắt Hoàng gia Hinomoto" — 帝有 là "thuộc về đế quốc" trong bối cảnh giả tưởng này, theo JP (TW 国有 chỉ là cách dịch của bản TW). Dòng này nằm trong nhóm 帝鉄 chờ thống nhất (§6).
- 2498: 従姉妹機 → "xe họ hàng" — diễn đạt thoáng nhưng chấp nhận được (TW 表姐妹車); câu sau "cô em họ Railord" giữ.
- 2214: 美形 → "mỹ nhân" — hơi mạnh nhưng chấp nhận được (TW 輪廓有多美).
- 2312: パターン → "khuôn mẫu" — theo JP (TW 弧線 là cách diễn đạt riêng của TW).
- 2441: 頭を下げる — chủ ngữ là Soutetsu (cúi đầu nghe Hibiki nói nhỏ) theo JP; TW dịch nhầm thành Hibiki cúi đầu — VN theo JP là đúng.
- 2538: giữ nguyên câu mảnh theo JP (không thêm "nhíu mày" như TW tự thêm).
- 日ノ本 đã là "Hinomoto" đúng (1509); エアクラ→"Aircra" đúng (2329); 帝大/冥国/冥軍/小畑/コン/まいてつ/電車姫/宮司/Seki/乗務鞄 không xuất hiện trong file.

## §6. Chờ Hieu (không tự quyết)

1. **1629 — ひえ！？ → "Hí!?"**: JP ひえ là tiếng kêu giật mình (TW 咦); "Hí" trong tiếng Việt dễ đọc thành tiếng cười khúc khích (hí hí). Giữ nguyên vì SFX diễn ngẫu hứng theo nhân vật + ngữ cảnh, nhưng nếu Hieu thấy lệch thì đổi thành "Hử!?". Không tính sai.
2. **1883 — Soutetsu "tôi" trong liệt kê nhóm**: "Nếu là Hibiki, tôi, và mọi người." — giữ theo nguyên tắc nhóm; nếu Hieu muốn "anh" ở đây thì báo lại. Không tính sai.
3. **Thuật ngữ chờ đợt thống nhất (không tính sai, KHÔNG sửa trong audit này)**: 帝鉄 → "Đường sắt Hoàng gia" 6 dòng (1242, 1570 gloss %l, 1655, 1869, 1954, 2544) + 帝有鉄道 key 60 ("Đường sắt Hoàng gia Hinomoto") = 7 dòng — theo hàng đợi thống nhất trong AUDIT-BRIEF.md ("帝鉄→Teitetsu rows"). Ghi nhận để đợt thống nhất xử lý một lần, tránh sửa lẻ tẻ không nhất quán (tiền lệ các review đã gộp để "Đường sắt Hoàng gia" chờ thống nhất: 1118, 1283, 828).

## §7. Lượt soát 2 (bắt buộc)

- Đọc lại toàn bộ 14 giá trị fix đối chiếu JP (+TW): **14 / 14 / 0 / 0** (tổng / đã kiểm chứng lại / bỏ / sửa).
- JSON 14 mục dạng chuẩn (khóa chuỗi, jp/tw/old_vn khớp CSV3 tuyệt đối 14/14); khối TOML 14 khóa, 0 sai lệch giá trị (đã kiểm chứng bằng máy: tomllib parse + so sánh từng giá trị với JSON; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa — xem diff máy).
- Cơ sở tổng: 126 file / 5.913 dòng sai (đã đối chiếu ROUTE-AUDIT.md dòng tổng mới nhất) → sau file này: **127 file / 5.927 dòng sai**.

## §8. Khối TOML (đã kiểm chứng parse)

```toml
"1522" = "「Nhưng, khi một khung cảnh tuyệt vời đến thế này,\\nđang phản chiếu trong đôi mắt của Hibiki——Ư!」"
"1617" = "「Sau khi hợp nhất thì nó phát triển rực rỡ lắm.\\n\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; này cũng là thứ được xây dựng vào thời điểm đó.」"
"1706" = "「Hửm? A, không——ra vậy, Hibiki\\nđang nhìn biểu cảm của \\x%l扇形機関庫;#00ffc040;gara đầu máy hình quạt%l;#; nhỉ——」"
"1713" = "「Ê he~Ư! Ê he he~Ư!\\nAnh vẽ \"âm vang\" (Hibiki) cho em đó hả!!」"
"1725" = "「Vì em biết anh hai sẽ bảo vệ em.\\nNên em mới có thể mải mê đến thế——á, a a a.」"
"1770" = "「Ohitoyo cũng vậy sao?」"
"1792" = "「Tất cả chúng ta, đều được kết nối với nhau.\\nVậy thì đây là——Ohitoyo——và, Đường sắt Ohitoyo.」"
"1831" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;……Tuyệt quá! Dễ thương quá đi.」"
"1832" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#;, sao——」"
"1833" = "「\\x%l扇形機関庫;#00ffc040;Gara đầu máy hình quạt%l;#; là biểu tượng vô cùng lớn lao\\nlần đầu tiên xuất hiện ở Bungomori——không thể để mất được.」"
"2051" = "「Anh hai, từ lúc nào mà anh lại——Ư!!\\nXin lỗi! Em xin lỗi!!?」"
"2065" = "「Toa ăn——\\nToa ăn á! Rào cản cao quá đi mất~~Ư!!」"
"2512" = "Lác đác vài người có vẻ là người dân địa phương,\\nđang đứng thành vòng tròn quanh chúng tôi để theo dõi."
"2559" = "Làn da tôi ôm lấy đang nóng bừng.\\nCó lẽ con bé sắp choáng vì nóng đến nơi rồi."
```

## Kết bài

File 日々姫02_文庫森.txt.toml: 412 dòng đã đọc, 14 dòng sai (3,4%) — lỗi tập trung ở thuật ngữ (gloss 扇形機関庫 "hình ngành" 5 dòng + Ohimitera 2 dòng), gasp (4 dòng, đều từ sweep), 2 dịch sai nghĩa, 2 lỗi đánh máy "dang". Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Đại từ đúng toàn file. 7 dòng "Đường sắt Hoàng gia" để lại cho đợt thống nhất. 2 cờ chờ Hieu: 1629 ("Hí!?") và 1883 ("tôi" nhóm).
