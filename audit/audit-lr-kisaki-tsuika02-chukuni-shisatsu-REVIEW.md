# Audit: lr稀咲追加02_仲国視察.txt.toml (06_Kisaki)

- File: `lr稀咲追加02_仲国視察.txt.toml` — route 06_Kisaki, 345 dòng script (稀咲 103, độc thoại 82, 双鉄 62, 西瓜 61, 姜 37). Nội dung: Soutetsu và Kisaki đi khảo sát ở Trọng Quốc cùng hướng dẫn viên Khương và Railord Suika — tham quan Bảo tàng Đường sắt Bắc Cầm (đầu máy hơi nước siêu lớn 2101 Quốc Hệ Hào, xe Oiran đo giới hạn kiến trúc), Suika vẽ phác thảo giải thích giới hạn kiến trúc, rồi lên tàu đi Thánh Đô ăn trưa ở toa ăn, bàn về việc đường sắt mất khách trẻ, Suika kể về Master đời trước (Lão Sư), cuối cùng vào buồng lái đầu máy Dongfu loại IV và nắm tay nhau.
- Kết quả: **10/345 dòng sai (2,9%)** — file sạch, lỗi rải rác, không có lỗi hệ thống.
- Phân loại (10): thuật ngữ 4 (1567, 1403, 1833, 1349 — 帝鉄 "Đường sắt Hoàng gia"→"Teitetsu"), sai nghĩa 4 (1191, 724, 1389, 1605), đọc sai 1 (1307 — 志 "Chi"→"Chí"), gasp 1 (1184 — từ sweep).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. CSV3 1 set duy nhất, 345 dòng, key khớp tuyệt đối. `[selections]` rỗng. Không có thẻ `%l` nào trong file (cả JP lẫn VN). Không có bản sao file này (md5 `501cd1d2da54ea70adfc3c529ea233f2` — duy nhất trong toml2; 11 nhóm trùng toàn dự án không chứa file này).

## Chi tiết từng sửa

### 1184 — gasp (sweep) — 双鉄
- JP: 「っ！！！」 / TW: 「啊！！！」
- Cũ: 「!!!」 → Mới: 「Ư!!!」
- Lý do: cả dòng chỉ là tiếng hít っ + dấu cảm thán; VN chỉ còn dấu câu là mất hẳn âm. Nhận nguyên fix của sweep (lost-gasp-whole).

### 1191 — sai nghĩa — 稀咲
- JP: 「ああ、だから列車そのものも幅広だし、足元がしっかりしている分、高さもとれているのか」
- TW: 「啊，所以列車整體都會更寬，底盤更加穩固，因而也可以做得更高」
- Cũ: 「A, thảo nào bản thân đoàn tàu cũng rộng hơn,\nvà nhờ phần chân vững chắc nên chiều cao cũng được tăng lên sao.」
- Mới: 「A, thảo nào bản thân đoàn tàu cũng rộng hơn,\nvà nhờ phần chân vững chắc nên chiều cao cũng được đảm bảo sao.」
- Lý do: 高さもとれている = chiều cao cũng được đảm bảo/đạt được, không phải "được tăng lên" (tăng là thêm nghĩa không có trong JP; JP thắng TW ở đây).

### 724 — sai nghĩa (thu hẹp) — 双鉄
- JP: 「『余所行きの召し物を普段着におろしてしまう』\n『途端に扱いが雑になり、みるみるうちに色褪せる』」
- TW: 「“遠行華服若降做平日穿著”“取用滌置便會諸多隨意，不日便會褪去華美色彩”」
- Cũ: 「'Đem trang phục mặc đi tiệc tùng xuống làm đồ mặc thường ngày'\n'Ngay lập tức sẽ bị đối xử thô bạo, và chẳng mấy chốc sẽ phai màu'.」
- Mới: 「'Đem trang phục diện khi ra ngoài xuống làm đồ mặc thường ngày'\n'Ngay lập tức sẽ bị đối xử thô bạo, và chẳng mấy chốc sẽ phai màu'.」
- Lý do: 余所行き = đồ mặc khi ra ngoài (trang phục diện), không riêng "đi tiệc tùng" — bản cũ thu hẹp nghĩa; TW 遠行華服 (y phục đẹp mặc đi xa) xác nhận.

### 1307 — đọc sai — 西瓜
- JP: 「志か――んんっ、西瓜のよく知る若者でしたら。\nネットのニュースサイトを一番頻繁にみているようです」
- TW: 「志……嗯，就西瓜很熟悉的年輕人來說，應該是以網路上的新聞網站為主要訊息來源」
- Cũ: 「Chi——Ưm, nếu là người trẻ mà Suika biết rõ.\nThì có vẻ họ thường xuyên xem các trang tin tức trên mạng nhất ạ.」
- Mới: 「Chí——Ưm, nếu là người trẻ mà Suika biết rõ.\nThì có vẻ họ thường xuyên xem các trang tin tức trên mạng nhất ạ.」
- Lý do: Suika ngập ngừng định nhắc một cái tên bắt đầu bằng 志 (shi); Hán-Việt của 志 là "Chí", không phải "Chi". "Ưm" cho んんっ đã đúng theo quy tắc (んっ→"Ưm"), giữ nguyên.

### 1389 — sai nghĩa (bịa thêm) — 稀咲
- JP: 「この列車が長距離列車だからそうなのかい？\nそれとも、市内の……通勤列車みたいなのも同じ？」
- TW: 「是因為這輛列車是長途列車的關係嗎？還是說，市內的……通勤列車之類也是這樣？」
- Cũ: 「Là do chuyến tàu này là tàu đường dài sao?\nHay là những chuyến tàu nội thành…… kiểu như tàu điện ngầm đi làm cũng vậy?」
- Mới: 「Là do chuyến tàu này là tàu đường dài sao?\nHay là những chuyến tàu nội thành…… kiểu như tàu đi làm cũng vậy?」
- Lý do: 通勤列車 = tàu đi làm (tàu通勤), không phải "tàu điện ngầm" — "điện ngầm" là bịa thêm, không có trong JP/TW; chính file này ở 1610 cũng dịch 通勤列車 là "tàu đi làm".

### 1605 — sai nghĩa (sai đối tượng câu hỏi) — 稀咲
- JP: 「この食堂車――[さんしゃ,1]餐車っていったっけ？\nここはいいね。ノスタルジーに満ちた清潔感がある」
- TW: 「這節餐車——中文是叫ｃａｎｃｈｅ對吧？這裡就不錯，清淨又有一絲淡淡的思鄉的感覺」
- Cũ: 「Toa ăn này——hình như gọi là toa nhà hàng nhỉ?\nỞ đây tuyệt thật đấy. Có một sự sạch sẽ tràn ngập nét hoài cổ.」
- Mới: 「Toa ăn này——tiếng Trung gọi là 'canche' phải không nhỉ?\nỞ đây tuyệt thật đấy. Có một sự sạch sẽ tràn ngập nét hoài cổ.」
- Lý do: Kisaki đang hỏi lại từ tiếng Trung 餐車 (đọc sansha/canche), không phải hỏi "toa nhà hàng" là gì — bản cũ đổi đối tượng câu hỏi và dùng "toa nhà hàng" trái với cách gọi "toa ăn" đã thống nhất trong file (1575, 1986, 1463). Theo TW (中文是叫canche).

### 1567 — thuật ngữ — 双鉄
- JP: 「ときに、この図の建築限界測定車。\n僕の目には、旧帝鉄のオヤそっくりに見えるのだが」
- Cũ: 「Nhân tiện, chiếc xe đo giới hạn kiến trúc trong bản vẽ này.\nTrong mắt tôi, nó trông giống hệt chiếc Oya của Đường sắt Hoàng gia cũ.」
- Mới: 「Nhân tiện, chiếc xe đo giới hạn kiến trúc trong bản vẽ này.\nTrong mắt tôi, nó trông giống hệt chiếc Oya của Teitetsu cũ.」
- Lý do: 帝鉄 = "Teitetsu" theo quy tắc đã chốt (Hieu 19/11); "Đường sắt Hoàng gia" sai tên riêng đã chốt. Tiền lệ sửa trong audit: Niiroku 03 (20 dòng hiển thị 帝鉄→Teitetsu, parent kiểm chứng 22/11).

### 1403 — thuật ngữ — 西瓜
- JP: 「はい。まさしく旧帝鉄のオヤ31そのものです。西瓜は、\n日ノ本に視察にいかせていただいたことがあるのです」
- Cũ: 「Vâng. Nó chính xác là chiếc Oya 31 của Đường sắt Hoàng gia cũ ạ. Suika\nđã từng có cơ hội đến Hinomoto để khảo sát.」
- Mới: 「Vâng. Nó chính xác là chiếc Oya 31 của Teitetsu cũ ạ. Suika\nđã từng có cơ hội đến Hinomoto để khảo sát.」
- Lý do: như 1567 (旧帝鉄→"Teitetsu cũ").

### 1833 — thuật ngữ — độc thoại
- JP: つい最近、日々姫が食堂車の研究をしたおり、\nハチロクが聞かせてくれた帝鉄の話をふと思い出す。
- Cũ: Gần đây, khi Hibiki đang nghiên cứu về toa ăn,\ntôi chợt nhớ lại câu chuyện về Đường sắt Hoàng gia mà Hachiroku từng kể.
- Mới: Gần đây, khi Hibiki đang nghiên cứu về toa ăn,\ntôi chợt nhớ lại câu chuyện về Teitetsu mà Hachiroku từng kể.
- Lý do: như 1567 (帝鉄→"Teitetsu").

### 1349 — thuật ngữ — 双鉄
- JP: 「帝鉄の衰退期にも同じことが起きたと聞いている。\nつまり、列車利用の日常化と、乗客の食堂車離れだ」
- Cũ: 「Tôi nghe nói điều tương tự cũng đã xảy ra trong thời kỳ suy thoái của Đường sắt Hoàng gia.\nTức là, việc sử dụng tàu hỏa trở nên thường nhật hóa, và hành khách dần quay lưng lại với toa ăn.」
- Mới: 「Tôi nghe nói điều tương tự cũng đã xảy ra trong thời kỳ suy thoái của Teitetsu.\nTức là, việc sử dụng tàu hỏa trở nên thường nhật hóa, và hành khách dần quay lưng lại với toa ăn.」
- Lý do: như 1567 (帝鉄→"Teitetsu"). Sau sửa, file không còn dòng "Đường sắt Hoàng gia" nào.

## Kiểm chứng sweep (っ-gasp)
- Sweep có đúng 1 mục cho file này: 1184 (lost-gasp-whole 「っ！！！」→「Ư!!!」) — đã kiểm chứng đúng JP/TW và nhận nguyên.
- 1180 「ぁっ」→"A." KHÔNG sửa, không đếm sai: âm "a" đã được diễn ("A."), dấu chấm diễn sự ngắt đột ngột; sweep không liệt kê dòng này (chỉ liệt kê 1184 trong cùng file); thực hành toàn dự án giữ các âm ngắn đã diễn (tiền lệ 2287 "Hau!" giữ). Ghi nhận là trường hợp biên, không quyết thêm.

## Kiểm chứng đại từ (đã đọc lân cận)
- Soutetsu tự xưng "tôi" toàn file với Kisaki/Suika/Khương (1089, 1188, 1347, 1312, 1595, 1833...) và trong độc thoại — đúng quy tắc đã sửa (Soutetsu "tôi" với Kisaki).
- Kisaki tự xưng "tôi" trong toàn bộ thoại công việc/chuyến khảo sát (1616, 1678, 1286, 1331...) — đúng chế độ công việc/quyết đoán theo quy tắc ngữ cảnh 21/11; "chị" với Suika (1467, 1343, 1362) đúng vai chị lớn với Railord nhỏ tuổi mà Suika gọi là "chị Kisaki".
- Suika/Khương gọi Soutetsu "anh Soutetsu" (先生) và Kisaki "chị Kisaki" (女士) — đúng, không chạm quy tắc tên trần (quy tắc đó chỉ áp cho cách Kisaki gọi Soutetsu).
- Soutetsu gọi Kisaki "em" (1118, 1089, 1188, 1216; "em ấy" ở độc thoại 1910, 1761) — GIỮ NGUYÊN, cờ cho đợt thống nhất (xem dưới): có mâu thuẫn đã ghi nhận toàn dự án (một file Kisaki đã sửa "em"→"cô", nhưng file 01/h3 giữ "em").

## Kiểm chứng CSV3 ↔ TOML
- 345/345 key khớp; khác biệt duy nhất là 254 dòng TOML-2 làm phẳng literal `\n` thành khoảng trắng (mẫu đã biết — CSV3 là chuẩn cho fix list); 0 khác biệt nội dung khác. Không có ô VN trống, không có VN == TW, không có giá trị VN trùng nhau ở 2 key.
- Không có ký tự CJK hay thẻ `%l` nào lọt vào giá trị VN. Các thẻ ngoặc trong JP ([さんしゃ,1]餐車, [ほてい,1]哺定駅, [いもうとき,1]妹機) là furigana, VN bỏ đúng.
- Thuật ngữ đã đúng sẵn toàn file: 日ノ本 "Hinomoto", エアクラ "Aircra", Railord (1 chữ l), 仲国 "Trọng Quốc", 北琴 "Bắc Cầm", 聖都 "Thánh Đô", 東富 "Dongfu", 国繋号 "Quốc Hệ Hào", 大廃線 "Đại bãi bỏ tuyến", オイラン車 "xe Oiran", 餐車/食堂車 "toa ăn", 寝台車 "toa giường nằm", 通勤列車 "tàu đi làm" (1610).

## Các dòng GIỮ NGUYÊN có ghi chú (không sửa, không quyết)
- 1256 徒花 → "bông hoa sớm nở tối tàn": diễn giải "hoa nở vô ích" bằng thành ngữ Việt, chấp nhận được, giữ.
- 1411/1436 正装 → "âu phục": thu hẹp nhẹ (chính trang ≠ riêng âu phục) nhưng thống nhất trong file, giữ.
- 1229 "bọn chị" (Kisaki + Soutetsu nói với Suika): dạng nhóm, không bị quy tắc số ít chi phối; giữ theo tiền lệ nhóm.
- 1649/1357/1426/1535 老子 → "Lão Sư": cách gọi "thầy cũ" cho Master đời trước, thống nhất trong file, TW 師父; giữ.
- 1180 「ぁっ」→"A." (xem mục sweep).
- 1289/1172: cột JP/TW của CSV3 có ký tự hiển thị lỗi ở 2 ô (JP 1289, TW 1172) nhưng giá trị VN và TOML đều đúng — lỗi hiển thị của CSV, không phải lỗi dịch.

## Cờ cho Hieu / đợt thống nhất (KHÔNG tự quyết)
- Kisaki gọi Soutetsu "anh Soutetsu" 5 dòng (1353, 1084, 1629, 1258, 1233) + đại từ "anh" chỉ Soutetsu (1561 "anh phải khen", 1629 "Anh thấy sao?") — GIỮ NGUYÊN theo quyết định 21/11 ~19:45: Kisaki→Soutetsu = tên trần "Soutetsu", phạm vi "các file Kisaki khác" thuộc đợt thống nhất (sweep), không sửa trong audit này. Tiền lệ: audit Kisaki03 cũng giữ + cờ.
- Kisaki tự xưng ở 1233 ("Vì đã có anh Soutetsu hộ tống tôi rồi mà" — cảnh nắm tay, thân mật): "tôi" hay "em" theo quy tắc ngữ cảnh — cờ cho đợt thống nhất rà lại.
- Soutetsu→Kisaki "em" (1118, 1089, 1188, 1216, 1910, 1761) — mâu thuẫn toàn dự án đã ghi nhận (một file sửa về "cô", file 01/h3 giữ "em") — cờ cho đợt thống nhất rà lại, không tự quyết ở đây.
- B19 vẫn park (không liên quan file này — không có thẻ %l hỏng).

## Lượt soát 2 (đọc lại toàn bộ fix theo JP)
- Tổng / kiểm chứng lại / bỏ / sửa: **10 / 10 / 0 / 0**. Không fix nào bị loại; mỗi fix chỉ đổi đúng chỗ cần đổi (đã kiểm tra diff từng dòng).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
"724" = "「'Đem trang phục diện khi ra ngoài xuống làm đồ mặc thường ngày'\\n'Ngay lập tức sẽ bị đối xử thô bạo, và chẳng mấy chốc sẽ phai màu'.」"
"1184" = "「Ư!!!」"
"1191" = "「A, thảo nào bản thân đoàn tàu cũng rộng hơn,\\nvà nhờ phần chân vững chắc nên chiều cao cũng được đảm bảo sao.」"
"1307" = "「Chí——Ưm, nếu là người trẻ mà Suika biết rõ.\\nThì có vẻ họ thường xuyên xem các trang tin tức trên mạng nhất ạ.」"
"1349" = "「Tôi nghe nói điều tương tự cũng đã xảy ra trong thời kỳ suy thoái của Teitetsu.\\nTức là, việc sử dụng tàu hỏa trở nên thường nhật hóa, và hành khách dần quay lưng lại với toa ăn.」"
"1389" = "「Là do chuyến tàu này là tàu đường dài sao?\\nHay là những chuyến tàu nội thành…… kiểu như tàu đi làm cũng vậy?」"
"1403" = "「Vâng. Nó chính xác là chiếc Oya 31 của Teitetsu cũ ạ. Suika\\nđã từng có cơ hội đến Hinomoto để khảo sát.」"
"1567" = "「Nhân tiện, chiếc xe đo giới hạn kiến trúc trong bản vẽ này.\\nTrong mắt tôi, nó trông giống hệt chiếc Oya của Teitetsu cũ.」"
"1605" = "「Toa ăn này——tiếng Trung gọi là 'canche' phải không nhỉ?\\nỞ đây tuyệt thật đấy. Có một sự sạch sẽ tràn ngập nét hoài cổ.」"
"1833" = "Gần đây, khi Hibiki đang nghiên cứu về toa ăn,\\ntôi chợt nhớ lại câu chuyện về Teitetsu mà Hachiroku từng kể."
```

Khối TOML: 10 khóa, parse được, 0 sai lệch giá trị so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10.

Kết bài
