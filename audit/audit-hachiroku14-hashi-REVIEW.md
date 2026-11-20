# Audit ハチロク14 — ハチロク14_橋.txt.toml

**Ngày kiểm toán:** 21/11/2026
**Tệp TOML:** `01_Hachiroku/#U30cf#U30c1#U30ed#U30af14_#U6a4b.txt.toml` — md5 `3d12a51d767e4c69da087e7eb161c54f`, BOM + CRLF, `[selections]` rỗng, **không có bản sao trùng** (chỉ 1 copy trong 227 tệp TOML; 11 nhóm trùng của dự án không chứa file này).
**Nguồn CSV:** "Trang tính 3" — **1 set duy nhất** (476 dòng, 0 key trùng, 0 VN rỗng) — không có bẫy dual-set. TOML khớp CSV3 tuyệt đối về key (476/476) và nội dung (203 khớp phẳng + 273 khớp sau khi chuẩn hoá `\n`, 0 khác biệt thực chất — toàn bộ là hiện tượng gộp `\n` trong TOML-2). CSV3 là bản chuẩn cho fix list.
**Cơ sở totals (đã kiểm chứng):** ROUTE-AUDIT.md hiện tại là **136 file / 6.200 dòng sai** — khớp đúng cơ sở 136/6.200 trong lệnh giao; snippet dùng 136/6.200 + 59 = 137/6.259.
**Kết quả: 59/476 dòng sai (12,4%), 0 dòng chưa chắc chắn, 0 dòng lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo file, 0 dòng chưa dịch, 0 key trùng.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Đại từ Soutetsu "anh"/"em"→"tôi" với Hachiroku (thoại 26 + độc thoại 3) | 29 |
| Gasp っ bị mất | 12 |
| Thuật ngữ/gloss %l | 17 |
| Sai nghĩa/bịa thêm | 1 |
| **Tổng** | **59** |

**Theo loại dòng:** thoại 43/228 sai (18,9%), độc thoại 18/248 sai (7,3%). **Theo nhân vật:** 双鉄 (Soutetsu) 34/107, monologue 18/248, ハチロク (Hachiroku) 4/64, ふかみ (Fukami) 1/3, 日々姫 (Hibiki) 1/3, 元忠 (Mototada) 1/18; 凪, 稀咲, 蓑笠, 真闇, 早瀬堰 0 sai.

File này sạch về cấu trúc — 0 lệch vị trí, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng. Lỗi tập trung ở một lỗi hệ thống duy nhất: Soutetsu tự xưng "anh" với Hachiroku ở 29/59 dòng sai (thoại 26 + độc thoại 3) — Gemini dịch nhất quán sai quy tắc đã chốt trong toàn bộ cảnh tình cảm cuối file (từ 1454 đến 1900), trong khi phần còn lại của file Soutetsu đã dùng đúng "tôi" ở độc thoại (245/248 dòng) và gọi Hachiroku là "em" đúng ở mọi chỗ. Các lỗi còn lại: 12 gasp (11 từ sweep + 1 needs-file-audit tự giải quyết), 17 gloss thuật ngữ (機関士/運転体/整備体/KiHa/Jutsu-sen/Seki/御一夜/湯医), 1 bịa thêm. **Thay đổi trong lúc audit:** theo chỉ đạo mới của Hieu 21/11 01:51 ("điều tra để quyết, không park phán đoán cho Hieu"), 7 dòng 御一夜/湯医 đã được quyết và sửa trong audit thay vì để lại đợt thống nhất (xem §3: 1733, 1754, 2372, 2355, 1696, 1200, 1777); chỉ tên công ty "Đường sắt Ohito" ở 2748 là giữ lại vì đó là quyết định đặt tên riêng của Hieu (xem §5).

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `3d12a51d767e4c69da087e7eb161c54f`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** CSV3 1 set duy nhất, 476 dòng, 0 key trùng, 0 VN rỗng. TOML script 476 khóa, khớp CSV3 476/476 về key; giá trị VN: 203 khớp tuyệt đối + 273 khớp sau khi chuẩn hoá `\n`, 0 khác biệt thực chất. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** kiểm tra trực tiếp sweep-raw-gasp-wrong.json — file này CÓ 12 mục (11 fix + 1 needs-file-audit 1914). Áp nguyên 11 fix sweep + tự giải quyết 1914 (xem §3). Quét bổ sung toàn bộ 185 dòng JP chứa っ: **không còn gasp nào sweep bỏ sót** (khác ふかみh2 bắt thêm 7 — file này sweep đã bao đủ).
- **Thẻ %l:** số lượng thẻ JP = VN ở mọi dòng — **0 thẻ thiếu dấu `;` đóng, 0 thẻ VN tự thêm, 0 thẻ thiếu**. Gloss sai chỉ là sai từ gloss (機関士/運転体/整備体/KiHa), đã sửa trong fix list.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng, không có VN trùng nhau trong file (0 cặp trùng — không có bằng chứng lệch vị trí/xoay). Nội dung là một cảnh liên tục duy nhất (lái 8620 vượt bão qua cầu sông Kuma, về ga Ohito) — các key tuy không theo thứ tự câu chuyện nhưng dòng chảy liền mạch, không có dấu hiệu VN của dòng khác lọt vào.
- **Đại từ:** Soutetsu gọi Hachiroku là "em" đúng ở mọi chỗ (1876, 1882, 1636, 1520, 1539, 1517, 1515, 1892; "Em ấy" ngôi thứ ba ở 1545/1790 đúng); Hachiroku tự xưng "em" nhất quán; Soutetsu tự xưng "tôi" đúng ở độc thoại 245/248 dòng (3 dòng sai đã sửa) và ở mọi thoại không nằm trong cảnh tình cảm cuối file. Kisaki tự xưng "Con" với bố Mototada (1682, 1238, 1723, 1726, 1245) và "Tớ" với cả nhóm (1721, giữ — nhóm hỗn hợp, xem §6); Nagi dùng ウチ → "em" nhất quán (1750, 1843); Fukami gọi Seki "ông nội" đã sửa thành "ông ngoại" (1815, xem §3).
- **Thuật ngữ đã chốt:** エアクラ = "Aircra" đúng (2742); レイルロオド = "Railord" đúng (1705, 1717, 2137); 砂撒き gloss "phun cát" (2682, viết thường giữa câu, giữ); 共存 = "Cộng tồn" nhất quán 2 dòng (1225, 2742); 御一夜 = "Ohitoyo" và 湯医 = "Yunoi" đã sửa trong audit ở 7 dòng (1733, 1754, 2372, 2355, 1696, 1200, 1777) theo chỉ đạo mới của Hieu 21/11 01:51 — chỉ còn tên công ty "Đường sắt Ohito" ở 2748 giữ nguyên chờ Hieu quyết (xem §5); file không có 帝鉄/コン/宮司/小畑/冥国/冥軍/駿袋/日ノ本/乗務鞄/運転鞄/乗員/マスコン/回数券/定期券; không có dòng fa/fu hay ひあ/ひゃ nào — quy tắc romaji fallback cho tiếng rên (Hieu duyệt 21/11 ~01:56) không áp dụng cho file này.
- **Chỉ đạo mới trong lúc audit (MEMORY.md cập nhật 21/11 ~01:55):** Hieu khẳng định lại việc ủy quyền quyết định cho Muse ("điều tra để quyết, không park phán đoán cho Hieu") — chỉ các mục thực sự cần kiểm tra trong game (B19) hoặc sở thích cá nhân của Hieu mới được park. Áp dụng: 7 dòng 御一夜/湯医 quyết và sửa trong audit; 2748 (tên công ty) park với lý do nêu ở §5.

## 3. Các lỗi đã sửa (59 dòng)

### 1200 — 双鉄 — thuật ngữ
**JP:** 「――御一夜は、こういう町だと知っていました。 / だから僕は、それを守りたいと思っています」
**TW:** 「——我知道御一夜就是這樣一座城市。所以我才想要守護它」
**Cũ:** 「——Tôi biết Ohito là một thị trấn như vậy. / Thế nên tôi mới muốn bảo vệ nó.」
**Mới:** 「——Tôi biết Ohitoyo là một thị trấn như vậy. / Thế nên tôi mới muốn bảo vệ nó.」
御一夜 (thị trấn) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.

### 1454 — 双鉄 — đại từ
**JP:** 「いや、だめだ。僕が行く」
**TW:** 「不可以。我去」
**Cũ:** 「Không, không được. Anh sẽ đi.」
**Mới:** 「Không, không được. Tôi sẽ đi.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1463 — ハチロク — gasp
**JP:** 「いえ、そのような――っ！！？」
**TW:** 「不，這怎麼——啊！！？」
**Cũ:** 「Không đâu ạ, làm gì có chuyện——!!?」
**Mới:** 「Không đâu ạ, làm gì có chuyện——Ư!!?」
Gasp cuối dòng っ bị mất — JP kết bằng ――っ！！？, TW có 啊, VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).

### 1481 — 双鉄 — đại từ
**JP:** 「越えよう。今日こそ。 / 僕と、お前で――僕らふたりで」
**TW:** 「今天就讓我和你——兩人一起跨過這道障礙吧」
**Cũ:** 「Cùng vượt qua nào. Chính hôm nay. / Anh và em——hai chúng ta.」
**Mới:** 「Cùng vượt qua nào. Chính hôm nay. / Tôi và em——hai chúng ta.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1493 — 双鉄 — đại từ
**JP:** 「だが、お前と出会い。僕はものではなくなった。 / お前を求めることにより――僕は、ひとりの男となった」
**TW:** 「但是，遇見你之後，我就不再是物品了。因為想要你——我變成了一個男人」
**Cũ:** 「Nhưng, kể từ khi gặp em. Anh không còn là đồ vật nữa. / Nhờ khao khát em——anh đã trở thành một người đàn ông thực thụ」
**Mới:** 「Nhưng, kể từ khi gặp em. Tôi không còn là đồ vật nữa. / Nhờ khao khát em——tôi đã trở thành một người đàn ông thực thụ」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 2 lần 'anh' đều là Soutetsu tự xưng.

### 1505 — 双鉄 — đại từ
**JP:** 「お前は、違うか？　まだ、ものなのか？ / お前は、僕を求めては――」
**TW:** 「你不是嗎？你還是物品嗎？你不想要我——」
**Cũ:** 「Còn em thì sao? Vẫn là đồ vật ư? / Em, không khao khát anh sao——」
**Mới:** 「Còn em thì sao? Vẫn là đồ vật ư? / Em, không khao khát tôi sao——」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1508 — 双鉄 — đại từ
**JP:** 「一人じゃない。僕も、お前も」
**TW:** 「你和我都不是孤身一人」
**Cũ:** 「Em không cô đơn đâu. Cả anh, cả em đều vậy.」
**Mới:** 「Em không cô đơn đâu. Cả tôi, cả em đều vậy.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). 'Em' ở đây gọi Hachiroku, đúng.

### 1509 — 双鉄 — đại từ
**JP:** 「もう一人じゃない。一人じゃないんだ。 / 僕がいて、お前がいるから――ここにいるから」
**TW:** 「你已經不是孤身一人了。我們都不是。這裡有我，也有你——我們都在這裡」
**Cũ:** 「Em không còn cô đơn nữa. Không cô đơn đâu. / Vì có anh, có em——vì chúng ta đang ở đây.」
**Mới:** 「Em không còn cô đơn nữa. Không cô đơn đâu. / Vì có tôi, có em——vì chúng ta đang ở đây.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1523 — 双鉄 — đại từ
**JP:** 「お前は、あの橋を越えられなかった。 / 僕は、あの橋を越えられなかった」
**TW:** 「你未能跨過那座橋。我也未能跨過那座橋」
**Cũ:** 「Em, đã không thể vượt qua cây cầu đó. / Anh, cũng đã không thể vượt qua cây cầu đó.」
**Mới:** 「Em, đã không thể vượt qua cây cầu đó. / Tôi, cũng đã không thể vượt qua cây cầu đó.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1541 — 双鉄 — đại từ
**JP:** 「ハチロク……僕は……」
**TW:** 「八六……我……」
**Cũ:** 「Hachiroku…… Anh……」
**Mới:** 「Hachiroku…… Tôi……」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1542 — 双鉄 — đại từ
**JP:** 「ハチロク。僕はお前が欲しい」
**TW:** 「八六。我想要你」
**Cũ:** 「Hachiroku. Anh muốn có em」
**Mới:** 「Hachiroku. Tôi muốn có em」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1547 — 双鉄 — đại từ
**JP:** 「ハチロク！　ブロアをかけるが、良いか！ / \x%lカマ;#00ffc040;カマ%l;#;の具合がすぐれんのだ」
**TW:** 「八六！我要通風，可以嗎！\x%lカマ;#00ffc040;窯%l;#;的狀況不太好」
**Cũ:** 「Hachiroku! Anh bật thiết bị thổi gió nhé, được không! / Tình trạng \x%lカマ;#00ffc040;lò hơi%l;#; không được tốt lắm.」
**Mới:** 「Hachiroku! Tôi bật thiết bị thổi gió nhé, được không! / Tình trạng \x%lカマ;#00ffc040;lò hơi%l;#; không được tốt lắm.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1551 — 双鉄 — đại từ
**JP:** 「ハチロク、ブロアをかけるぞ」
**TW:** 「八六，我要通風了」
**Cũ:** 「Hachiroku, anh bật thiết bị thổi gió nhé.」
**Mới:** 「Hachiroku, tôi bật thiết bị thổi gió nhé.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku; Hachiroku gọi Soutetsu là 'ngài Soutetsu' 双鉄様).

### 1614 — 双鉄 — gasp
**JP:** 「っ！　そうかっ、これも気圧が――っ！！？」
**TW:** 「啊！原來如此，這也是氣壓在作怪——呃！！？」
**Cũ:** 「! Ra là vậy, cái này cũng là do áp suất không khí——!!?」
**Mới:** 「Ư! Ra là vậy, cái này cũng là do áp suất không khí——Ư!!?」
Gasp đầu dòng っ！ và gasp cuối ――っ！！？ đều bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing). そうかっ giữa dòng là っ nhấn mạnh gắn với từ nội dung, giữ nguyên theo sweep.

### 1622 — 双鉄 — đại từ
**JP:** 「うん。そうだった。そうしなければ生きられなかった。 / 今振り返れば……あれは、ものとしての生だったのだな」
**TW:** 「嗯。以前是這樣的。必須這樣我才能活下去。現在回頭想想……那簡直是一段形同物品的生命」
**Cũ:** 「Ừ. Đúng là vậy. Nếu không làm thế thì anh đã không thể sống tiếp. / Bây giờ nhìn lại…… đó đúng là một cuộc sống của đồ vật nhỉ」
**Mới:** 「Ừ. Đúng là vậy. Nếu không làm thế thì tôi đã không thể sống tiếp. / Bây giờ nhìn lại…… đó đúng là một cuộc sống của đồ vật nhỉ」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1684 — 双鉄 — đại từ
**JP:** 「あの橋を、あの過去を。 / 僕も同じだ。越えられなかった」
**TW:** 「我也一樣。我沒能跨過那座橋，跨過那段過去」
**Cũ:** 「Cây cầu đó, quá khứ đó. / Anh cũng giống em. Không thể vượt qua được.」
**Mới:** 「Cây cầu đó, quá khứ đó. / Tôi cũng giống em. Không thể vượt qua được.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1686 — 双鉄 — đại từ
**JP:** 「僕は、ハチロク。お前にも。 / 僕を所有し、独占して欲しいと思っているのだ」
**TW:** 「我也希望八六——你會想擁有我，獨占我」
**Cũ:** 「Anh cũng muốn Hachiroku, cả em nữa. / Cũng khao khát được sở hữu anh, được độc chiếm anh」
**Mới:** 「Tôi cũng muốn Hachiroku, cả em nữa. / Cũng khao khát được sở hữu tôi, được độc chiếm tôi」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 3 lần 'anh' đều là Soutetsu tự xưng.

### 1696 — 双鉄 — thuật ngữ
**JP:** 「当然のことをしたまでです。鉄道に関わる人間として。 / そして、御一夜の一員として」
**TW:** 「我只是做了理所應當的事而已。身為鐵路的從業人員，以及身為御一夜的一員，這都是應該的」
**Cũ:** 「Tôi chỉ làm việc đương nhiên thôi. Với tư cách là một người liên quan đến đường sắt. / Và với tư cách là một thành viên của Ohito.」
**Mới:** 「Tôi chỉ làm việc đương nhiên thôi. Với tư cách là một người liên quan đến đường sắt. / Và với tư cách là một thành viên của Ohitoyo.」
御一夜 (tổ chức/địa danh) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11). Quyết theo chỉ đạo mới của Hieu 21/11 01:51. (Chỉ tên công ty 'Đường sắt Ohito' ở 2748 là giữ lại chờ Hieu quyết — xem §5.)

### 1701 — 双鉄 — đại từ
**JP:** 「僕とハチロクも、一緒に帰る」
**TW:** 「我和八六也一起回去」
**Cũ:** 「Em và Hachiroku cũng sẽ về cùng」
**Mới:** 「Tôi và Hachiroku cũng sẽ về cùng」
Soutetsu tự xưng 'Em' khi nói với cả Hibiki + Mayami (câu trước 1835 gọi cả hai, 1631 Mayami đáp, 2244 cả hai cùng cười) — 'Em' sai cả hai chiều (với Hibiki là 'anh', với Mayami là 'tôi'); dạng xưng hô nhóm dùng 'tôi' theo tiền lệ Paulette 14 key 1544.

### 1712 — 双鉄 — đại từ
**JP:** 「与えられた関係ではなく。僕の、僕だけのお前が欲しい。 / 僕は、お前を独占したいし、家族にしたい」
**TW:** 「我想要只屬於我的你，而不是這種被給予的關係。我想要獨占你，想讓你成為我的家人」
**Cũ:** 「Không phải là một mối quan hệ được ban cho. Anh muốn em là của anh, của riêng anh thôi. / Anh muốn độc chiếm em, muốn em trở thành gia đình của anh」
**Mới:** 「Không phải là một mối quan hệ được ban cho. Tôi muốn em là của tôi, của riêng tôi thôi. / Tôi muốn độc chiếm em, muốn em trở thành gia đình của tôi」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 5 lần 'anh' đều là Soutetsu tự xưng.

### 1714 — 双鉄 — đại từ
**JP:** 「僕はオーナーでマスターだ」
**TW:** 「我是所有者，也是你的主人」
**Cũ:** 「Anh là chủ sở hữu và là Master.」
**Mới:** 「Tôi là chủ sở hữu và là Master.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). 'Master' giữ nguyên (thuật ngữ dự án cho マスター).

### 1719 — 双鉄 — đại từ
**JP:** 「僕も、確かにものだった。 / 誰かのために、機能するだけの存在だった」
**TW:** 「我曾經也是物品。也是為了他人而發揮作用的存在」
**Cũ:** 「Anh cũng từng là đồ vật mà. / Cũng từng là tồn tại chỉ hoạt động vì một ai đó thôi」
**Mới:** 「Tôi cũng từng là đồ vật mà. / Cũng từng là tồn tại chỉ hoạt động vì một ai đó thôi」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1733 — 双鉄 — thuật ngữ
**JP:** 「だから、帰ろう。御一夜に」
**TW:** 「所以，我們回御一夜吧」
**Cũ:** 「Nào, về thôi. Về Ohito.」
**Mới:** 「Nào, về thôi. Về Ohitoyo.」
御一夜 (địa danh) dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51 (điều tra để quyết, không park) thay vì để lại đợt thống nhất.

### 1735 — 双鉄 — đại từ
**JP:** 「だから、越えたい。あの橋を」
**TW:** 「所以，我想跨過那座橋」
**Cũ:** 「Thế nên, anh muốn vượt qua. Cây cầu đó.」
**Mới:** 「Thế nên, tôi muốn vượt qua. Cây cầu đó.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1737 — 双鉄 — đại từ
**JP:** 「すまん。 / 同じ失敗は繰り返さぬようにする」
**TW:** 「抱歉。我會小心不再犯同樣的錯誤」
**Cũ:** 「Xin lỗi. / Anh sẽ không lặp lại sai lầm tương tự nữa.」
**Mới:** 「Xin lỗi. / Tôi sẽ không lặp lại sai lầm tương tự nữa.」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1754 — 双鉄 — thuật ngữ
**JP:** 「そうだな、[ゆのい,1]湯医の\x%l三角線;#00ffc040;[さんかくせん,2]三角線%l;#;まで行ってしまう方が安全だ。 / そこから折り返して、前を向いて御一夜へ帰ろう」
**TW:** 「是啊，去湯醫的\x%l三角線;#00ffc040;三角線%l;#;比較安全。在那邊折返，面向前方，返回御一夜吧」
**Cũ:** 「Đúng vậy, đi đến \x%l三角線;#00ffc040;đường tam giác%l;#; ở Yui thì sẽ an toàn hơn. / Từ đó chúng ta sẽ quay đầu, hướng về phía trước và trở về Ohito.」
**Mới:** 「Đúng vậy, đi đến \x%l三角線;#00ffc040;đường tam giác%l;#; ở Yunoi thì sẽ an toàn hơn. / Từ đó chúng ta sẽ quay đầu, hướng về phía trước và trở về Ohitoyo.」
Hai thuật ngữ sai trong một dòng: 湯医 dùng 'Yui' — JP mang furigana [ゆのい,1] nên đọc là 'Yunoi' theo thuật ngữ đã chốt; 御一夜 dùng 'Ohito' — sửa về 'Ohitoyo'. Quyết theo chỉ đạo mới của Hieu 21/11 01:51 (điều tra để quyết, không park).

### 1777 — 双鉄 — thuật ngữ
**JP:** 「例えば、あなたと僕とでも。 / 御一夜を大事に思う気持ちは、きっと共通してますし」
**TW:** 「比如說，您和我也是一樣。我們重視御一夜的心情，一定也是相通的」
**Cũ:** 「Ví dụ như, giữa ông và tôi cũng vậy. / Tình cảm trân trọng Ohito, chắc chắn là chúng ta giống nhau.」
**Mới:** 「Ví dụ như, giữa ông và tôi cũng vậy. / Tình cảm trân trọng Ohitoyo, chắc chắn là chúng ta giống nhau.」
御一夜 dùng 'Ohito' — sửa về 'Ohitoyo' theo thuật ngữ đã chốt (19/11). Quyết theo chỉ đạo mới của Hieu 21/11 01:51.

### 1815 — ふかみ — thuật ngữ
**JP:** 「おじいちゃん……」
**TW:** 「爺爺……」
**Cũ:** 「Ông nội……」
**Mới:** 「Ông ngoại……」
Fukami gọi Seki (早瀬堰) là 'ông nội' — theo quyết định đã chốt 20/11, Seki là ông ngoại của Fukami (mẹ Fukami là Midori; 08c 2456 Seki gọi Midori là 娘, 2086 gọi Fukami là 孫娘). Đây là dòng Seki thứ 6 tìm được trong audit (sau 4 dòng đã liệt kê + ハチロク07 2679) — sửa trong audit theo đúng tiền lệ 2679. Cảnh này: Seki vừa nói với Fukami (1798), dặn gọi điện cho Midori (1668), và đáp lời xin lỗi của Fukami (1455), nên người được gọi chắc chắn là Seki.

### 1821 — 双鉄 — đại từ
**JP:** 「今、か。 / 今、この瞬間の僕の生は――」
**TW:** 「現在啊。在現在這個瞬間，我的生命應該是——」
**Cũ:** 「Hiện tại, sao. / Cuộc sống của anh trong khoảnh khắc này, lúc này là——」
**Mới:** 「Hiện tại, sao. / Cuộc sống của tôi trong khoảnh khắc này, lúc này là——」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1834 — 日々姫 — gasp
**JP:** 「稀咲先輩っ――っ！」
**TW:** 「稀咲學姐——！」
**Cũ:** 「Tiền bối Kisaki——!」
**Mới:** 「Tiền bối Kisaki——Ư!」
Gasp cuối dòng っ――っ! bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).

### 1836 — 双鉄 — đại từ
**JP:** 「それを与えてくれたのは。 / ハチロク。お前だ」
**TW:** 「而給予我這樣的生命的正是你啊，八六」
**Cũ:** 「Và người đã ban cho anh điều đó. / Chính là em, Hachiroku」
**Mới:** 「Và người đã ban cho tôi điều đó. / Chính là em, Hachiroku」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1856 — 双鉄 — đại từ
**JP:** 「あの日の橋を。 / 僕と、お前で――」
**TW:** 「讓我和你一起，去跨過那一天的橋——」
**Cũ:** 「Cây cầu của ngày hôm đó. / Anh và em——」
**Mới:** 「Cây cầu của ngày hôm đó. / Tôi và em——」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1890 — 双鉄 — đại từ
**JP:** 「あの事故の後、お前と出会うまでの僕は―― / 誰かの目的を果たすため、機能するだけの存在だった」
**TW:** 「那起事故後，在和你相遇前——我不過是為了完成他人的目的而發揮作用的存在」
**Cũ:** 「Sau vụ tai nạn đó, cho đến trước khi gặp em—— / anh cũng chỉ là một tồn tại hoạt động nhằm hoàn thành mục đích của ai đó mà thôi」
**Mới:** 「Sau vụ tai nạn đó, cho đến trước khi gặp em—— / tôi cũng chỉ là một tồn tại hoạt động nhằm hoàn thành mục đích của ai đó mà thôi」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1893 — 双鉄 — đại từ
**JP:** 「ならば。僕も“もの”だったのだな」
**TW:** 「那麼，我曾經也是“物品”啊」
**Cũ:** 「Nếu vậy. Thì anh cũng từng là "đồ vật" nhỉ」
**Mới:** 「Nếu vậy. Thì tôi cũng từng là "đồ vật" nhỉ」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku).

### 1900 — 双鉄 — đại từ
**JP:** 「それはそうだが。もっと欲しい。 / 僕は――僕は――」
**TW:** 「雖然是這樣沒錯。但是我還想要更多。我——我——」
**Cũ:** 「Đúng là vậy. Nhưng anh muốn nhiều hơn thế. / Anh——Anh——」
**Mới:** 「Đúng là vậy. Nhưng tôi muốn nhiều hơn thế. / Tôi——Tôi——」
Soutetsu tự xưng 'anh' với Hachiroku — sai theo quy tắc đã chốt ('tôi' với Hachiroku). Cả 3 lần 'anh' đều là Soutetsu tự xưng.

### 1910 — ハチロク — gasp
**JP:** 「っ！」
**TW:** 「！」
**Cũ:** 「!」
**Mới:** 「Ư!」
Gasp nguyên dòng っ! bị mất — VN chỉ còn '!'. Áp nguyên sweep (lost-gasp-whole).

### 1911 — 双鉄 — gasp
**JP:** 「っ！！！」
**TW:** 「！！！」
**Cũ:** 「!!!」
**Mới:** 「Ư!!!」
Gasp nguyên dòng っ!!! bị mất — VN chỉ còn '!!!'. Áp nguyên sweep (lost-gasp-whole).

### 1912 — 双鉄 — gasp
**JP:** 「っ！！？」
**TW:** 「！！？」
**Cũ:** 「!!?」
**Mới:** 「Ư!!?」
Gasp nguyên dòng っ!!? bị mất — VN chỉ còn '!!?'. Áp nguyên sweep (lost-gasp-whole).

### 1914 — ハチロク — gasp
**JP:** 「っ！！？ / 双鉄様、代わってください！　わたくしが」
**TW:** 「！！？雙鐵少爺，請讓我來！我去」
**Cũ:** 「!!? / Ngài Soutetsu, xin hãy đổi chỗ cho em! Em sẽ」
**Mới:** 「Ư!!? / Ngài Soutetsu, xin hãy đổi chỗ cho em! Em sẽ」
Sweep đánh dấu needs-file-audit — tự giải quyết trong audit: dòng đầu là gasp nguyên dòng っ!!?, VN chỉ còn '!!?' nên thêm Ư; dòng sau JP わたくしが và TW '我去' đều cụt câu, VN 'Em sẽ' giữ đúng dạng cụt — không bịa thêm phần còn lại.

### 1915 — ハチロク — gasp
**JP:** 「っ！？」
**TW:** 「！？」
**Cũ:** 「!?」
**Mới:** 「Ư!?」
Gasp nguyên dòng っ!? bị mất — VN chỉ còn '!?'. Áp nguyên sweep (lost-gasp-whole).

### 1924 — 元忠 — gasp
**JP:** 『「っ！」 / 「っ！」』
**TW:** 『「！」 / 「！」』
**Cũ:** 「!」 / 「!」
**Mới:** 「Ư!」 / 「Ư!」
Gasp nguyên dòng っ! ×2 (hai người cùng thốt lên) bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-whole).

### 2140 — monologue — đại từ
**JP:** 誰かに言われたからでなく、目的を果たすためでもなく。 / ただ僕自身の欲として、これほど強く求めてる。
**TW:** 不是因為他人的話，也不是單純為了達到目的。只是出於我自身的欲望而如此強烈地渴求。
**Cũ:** Không phải vì bị ai đó sai bảo, cũng chẳng phải để hoàn thành mục đích nào cả. / Chỉ đơn thuần là dục vọng của chính bản thân anh, khao khát mãnh liệt đến thế này.
**Mới:** Không phải vì bị ai đó sai bảo, cũng chẳng phải để hoàn thành mục đích nào cả. / Chỉ đơn thuần là dục vọng của chính bản thân tôi, khao khát mãnh liệt đến thế này.
Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi'; toàn file độc thoại dùng 'tôi' ở 245/248 dòng.

### 2195 — monologue — gasp
**JP:** が……これほどの、ほぼ無視界の悪天候下で走らせるなど、 / 日中にさえ、まったく経験の無い―――っ！？
**TW:** 但是……就算在白天，我也沒有過在視野如此之差的惡劣天氣下行車的經驗——！？
**Cũ:** Nhưng…… chạy tàu trong điều kiện thời tiết khắc nghiệt gần như không có tầm nhìn thế này, / thì ngay cả ban ngày tôi cũng chưa từng trải qua bao giờ——!?
**Mới:** Nhưng…… chạy tàu trong điều kiện thời tiết khắc nghiệt gần như không có tầm nhìn thế này, / thì ngay cả ban ngày tôi cũng chưa từng trải qua bao giờ——Ư!?
Gasp cuối dòng ―――っ!? bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).

### 2258 — monologue — thuật ngữ
**JP:** はっきりとしたハチロクの\x%l喚呼;#00ffc040;喚呼%l;#;が気合を新たにしてくれる。 / 術仙炭鉱廃駅までを安全に乗り切るために――
**TW:** 八六吐字清晰的\x%l喚呼;#00ffc040;復誦%l;#;讓我鼓足了幹勁。為了安全到達術仙煤礦廢車站——
**Cũ:** Tiếng \x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới. / Để vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsusen một cách an toàn——
**Mới:** Tiếng \x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới. / Để vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsu-sen một cách an toàn——
術仙炭鉱廃駅 viết 'Jutsusen' — thiếu gạch nối so với dạng đã chốt 'Jutsu-sen'. Đây là dòng 術仙 duy nhất trong file.

### 2355 — monologue — thuật ngữ
**JP:** 御一夜駅に戻ったのなら、どれほど乾かしておいたとて。 / そこからぎゅうぎゅう、更に絞られるのだろうから。
**TW:** 回到御一夜站後，她們應該都烘乾身子了。不過，她們大概還得面臨一頓暴風雨般的臭罵。
**Cũ:** Nhưng khi về đến ga Ohito rồi, thì dù có hong khô đến mức nào đi nữa. / Chắc chắn sẽ bị vắt kiệt sức thêm nữa thôi.
**Mới:** Nhưng khi về đến ga Ohitoyo rồi, thì dù có hong khô đến mức nào đi nữa. / Chắc chắn sẽ bị vắt kiệt sức thêm nữa thôi.
御一夜駅 dùng 'ga Ohito' — sửa về 'ga Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.

### 2368 — monologue — thuật ngữ
**JP:** 事故の、そのあと。\x%l機関士;#00ffc040;機関士%l;#;からも仲間からも。 / 同じ時間を過ごした存在、全てから――
**TW:** 在事故之後，不管是\x%l機関士;#00ffc040;司機%l;#;還是同伴，曾與她共度時光的所有人都將她拋棄——
**Cũ:** Sau vụ tai nạn đó. Từ \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; cho đến những người đồng đội. / Từ tất cả những người đã cùng chung sống trong khoảng thời gian đó——
**Mới:** Sau vụ tai nạn đó. Từ \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; cho đến những người đồng đội. / Từ tất cả những người đã cùng chung sống trong khoảng thời gian đó——
Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09.

### 2372 — monologue — thuật ngữ
**JP:** 御一夜駅に無事に帰り着くまで、 / ゆっくり休んで、温まり乾かしておけばいい。
**TW:** 在平安回到御一夜站之前，就讓她們好好休息，暖暖身子吧。
**Cũ:** Cho đến khi bình an trở về ga Ohito, / cứ thong thả nghỉ ngơi, sưởi ấm và hong khô người là được.
**Mới:** Cho đến khi bình an trở về ga Ohitoyo, / cứ thong thả nghỉ ngơi, sưởi ấm và hong khô người là được.
御一夜駅 dùng 'ga Ohito' — sửa về 'ga Ohitoyo' theo thuật ngữ đã chốt (19/11) + furigana おひとよ. Quyết theo chỉ đạo mới của Hieu 21/11 01:51.

### 2374 — monologue — thuật ngữ
**JP:** 助士が不在で、僕が投げ込みに回る以上、 / \x%l機関士;#00ffc040;機関士%l;#;として\x%l8620;#00ffc040;8620%l;#;を運転するのは、ハチロクだ。
**TW:** 在沒有司爐，必須由我來加煤的情況下，是八六在作為\x%l機関士;#00ffc040;司機%l;#;駕駛\x%l8620;#00ffc040;８６２０%l;#;。
**Cũ:** Vì không có phụ lái tàu, tôi phải quay sang xúc than, / nên người lái \x%l8620;#00ffc040;8620%l;#; với tư cách là \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;, chính là Hachiroku.
**Mới:** Vì không có phụ lái tàu, tôi phải quay sang xúc than, / nên người lái \x%l8620;#00ffc040;8620%l;#; với tư cách là \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;, chính là Hachiroku.
Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09.

### 2398 — monologue — gasp
**JP:** ただ、経験のみ。 / 今まで調べ、積み重ねてきたものだけが――っ！？
**TW:** 她只是在憑經驗、依靠至今為止所學到的知識——嗯！？
**Cũ:** Chỉ dựa vào kinh nghiệm. / Chỉ những gì đã tìm hiểu và tích lũy từ trước đến nay——!?
**Mới:** Chỉ dựa vào kinh nghiệm. / Chỉ những gì đã tìm hiểu và tích lũy từ trước đến nay——Ư!?
Gasp cuối dòng ――っ!? bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).

### 2455 — monologue — thuật ngữ
**JP:** 車体の状態を適宜モニタし、最適の運転指示をくれる。 / \x%l運転体;#00ffc040;運転体%l;#;の能力を、今のハチロクは発揮できない。
**TW:** 往常的她能即時監控車體的狀態，並作出最適合的操作指示。但現在的她卻無法發揮出\x%l運転体;#00ffc040;駕駛體%l;#;那樣的能力。
**Cũ:** Theo dõi trạng thái thân xe một cách thích hợp, và đưa ra chỉ thị lái tối ưu nhất. / Năng lực của \x%l運転体;#00ffc040;kíp lái%l;#;, Hachiroku hiện tại không thể phát huy được.
**Mới:** Theo dõi trạng thái thân xe một cách thích hợp, và đưa ra chỉ thị lái tối ưu nhất. / Năng lực của \x%l運転体;#00ffc040;thân vận hành%l;#;, Hachiroku hiện tại không thể phát huy được.
Gloss 運転体 dùng 'kíp lái' — sửa về 'thân vận hành' theo tiền lệ ハチロク14_凪 3983 / 日々姫09.

### 2514 — monologue — thuật ngữ
**JP:** \x%l整備体;#00ffc040;整備体%l;#;の横顔は凛と張り詰めて、 / 怖いくらいに美しいものと感じもするが――
**TW:** 我在側面看著她的\x%l整備体;#00ffc040;整備體%l;#;端莊而嚴肅的臉，真是美麗得令人感到恐怖，但是——
**Cũ:** Góc nghiêng của \x%l整備体;#00ffc040;thân chính%l;#; vô cùng nghiêm nghị và căng thẳng, / đẹp đến mức khiến tôi cảm thấy đáng sợ——
**Mới:** Góc nghiêng của \x%l整備体;#00ffc040;thân bảo trì%l;#; vô cùng nghiêm nghị và căng thẳng, / đẹp đến mức khiến tôi cảm thấy đáng sợ——
Gloss 整備体 dùng 'thân chính' — sửa về 'thân bảo trì' theo thuật ngữ đã chốt.

### 2582 — monologue — đại từ
**JP:** 乗り越えたいと、だから思えた。 / ハチロクがともにいてくれたから、乗り越えられた。
**TW:** 所以我才想要去跨過那道障礙。因為八六和我在一起，我才能夠做到。
**Cũ:** Nên anh mới muốn vượt qua. / Vì có Hachiroku ở bên, nên anh mới có thể vượt qua được.
**Mới:** Nên tôi mới muốn vượt qua. / Vì có Hachiroku ở bên, nên tôi mới có thể vượt qua được.
Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi' ('mình' chỉ cho tự vấn nội tâm); toàn file độc thoại dùng 'tôi' ở 245/248 dòng.

### 2678 — monologue — thuật ngữ
**JP:** \x%l機関士;#00ffc040;機関士%l;#;の僕と、\x%l運転体;#00ffc040;運転体%l;#;のハチロクとで組んでるときの―― / 背中を完全に預けあえている安心感が、今は無い。
**TW:** 現在我感覺不到由我擔當\x%l機関士;#00ffc040;司機%l;#;與使用\x%l運転体;#00ffc040;駕駛體%l;#;的八六搭檔時那種能將身後完全託付給對方的安全感。
**Cũ:** Cảm giác an tâm khi tôi làm \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#; kết hợp với \x%l運転体;#00ffc040;kíp lái%l;#; của Hachiroku—— / cảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa.
**Mới:** Cảm giác an tâm khi tôi làm \x%l機関士;#00ffc040;thợ lái đầu máy%l;#; kết hợp với \x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku—— / cảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa.
Hai gloss sai trong một dòng: 機関士 'nhân viên cơ vụ' → 'thợ lái đầu máy' (thuật ngữ đã chốt); 運転体 'kíp lái' → 'thân vận hành' (tiền lệ ハチロク14_凪 3983 / 日々姫09).

### 2741 — monologue — đại từ
**JP:** そして今、僕はこれほど強く、強く、 / 終着駅のさらに先へも、ともにいきたいと望んでる。
**TW:** 而現在，我是如此迫切地希望，在駛過終點站之後，八六也能和我在一起。
**Cũ:** Và giờ đây, anh đang khao khát mãnh liệt, vô cùng mãnh liệt, / muốn được cùng em đi xa hơn nữa, vượt qua cả nhà ga cuối cùng.
**Mới:** Và giờ đây, tôi đang khao khát mãnh liệt, vô cùng mãnh liệt, / muốn được cùng em đi xa hơn nữa, vượt qua cả nhà ga cuối cùng.
Độc thoại người kể Soutetsu dùng 'anh' — quy tắc chung độc thoại là 'tôi'; toàn file độc thoại dùng 'tôi' ở 245/248 dòng.

### 2746 — monologue — gasp
**JP:** 音は止まない。 / むしろますます加熱して――っ！
**TW:** 聲音沒有停止。反而變得越來越劇烈——！
**Cũ:** Âm thanh không dừng lại. / Thậm chí còn ngày càng lớn hơn——!
**Mới:** Âm thanh không dừng lại. / Thậm chí còn ngày càng lớn hơn——Ư!
Gasp cuối dòng ――っ! bị mất — VN chỉ còn dấu câu. Áp nguyên sweep (lost-gasp-trailing).

### 2910 — monologue — thuật ngữ
**JP:** （だが、目隠しだ。\x%l整備体;#00ffc040;整備体%l;#;のハチロクでは、 / センサ性能が不十分すぎる）
**TW:** （但這不過是掩飾而已。八六的\x%l整備体;#00ffc040;整備體%l;#;感測器性能太過低下）
**Cũ:** （Nhưng mà, thế này chẳng khác nào bịt mắt. Với \x%l整備体;#00ffc040;thân chính%l;#; của Hachiroku, / thì hiệu suất cảm biến quá kém.）
**Mới:** （Nhưng mà, thế này chẳng khác nào bịt mắt. Với \x%l整備体;#00ffc040;thân bảo trì%l;#; của Hachiroku, / thì hiệu suất cảm biến quá kém.）
Gloss 整備体 dùng 'thân chính' — sửa về 'thân bảo trì' theo thuật ngữ đã chốt.

### 2927 — monologue — thuật ngữ
**JP:** （ハチロクが――\x%l機関士;#00ffc040;機関士%l;#;役など）
**TW:** （居然要由八六來擔任\x%l機関士;#00ffc040;司機%l;#;）
**Cũ:** （Để Hachiroku——đóng vai trò \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;）
**Mới:** （Để Hachiroku——đóng vai trò \x%l機関士;#00ffc040;thợ lái đầu máy%l;#;）
Gloss 機関士 dùng 'nhân viên cơ vụ' — đó là gloss của 運転士, không phải 機関士; sửa về 'thợ lái đầu máy' theo thuật ngữ đã chốt + tiền lệ 日々姫09 (9 dòng).

### 2940 — monologue — thuật ngữ
**JP:** （\x%lキハ07;#00ffc040;キハ07%l;#;が営業運転に復帰できれば、 / 金銭面でも運営面でも、大きな余裕が生まれてくる）
**TW:** （若是\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;能夠恢復營業運行，不管是資金方面還是運營方面都能充裕很多）
**Cũ:** （Nếu \x%lキハ07;#00ffc040;Kiha 07%l;#; có thể hoạt động thương mại trở lại, / thì cả về mặt tài chính lẫn vận hành đều sẽ có khoảng dư dả lớn.）
**Mới:** （Nếu \x%lキハ07;#00ffc040;KiHa 07%l;#; có thể hoạt động thương mại trở lại, / thì cả về mặt tài chính lẫn vận hành đều sẽ có khoảng dư dả lớn.）
Gloss キハ07 viết 'Kiha 07' — sai chính tả, cách viết chính thức của JR là 'KiHa' (tiền lệ 00common07, 日々姫10).

### 2948 — monologue — sai nghĩa
**JP:** （文字通りの手探り、だな。これは）
**TW:** （這簡直是真正意義上的“摸索”了啊）
**Cũ:** （Đúng nghĩa đen là mò mẫm trong đêm tối rồi. Thế này thì）
**Mới:** （Đúng nghĩa đen là mò mẫm rồi đây.）
VN bịa thêm 'trong đêm tối' (JP 手探り và TW 摸索 đều không có) và dịch これは thành mảnh câu dở dang 'Thế này thì' — JP là một ý hoàn chỉnh ('đây đúng nghĩa đen là mò mẫm'). Sửa về đúng JP; 'mò mẫm' tự nó đã hàm ý dò dẫm trong tối.

## 4. Rà soát chéo với sweep gasp

- Sweep có 12 mục cho file này: 11 fix (1463, 1614, 1834, 1910, 1911, 1912, 1915, 1924, 2195, 2398, 2746) — audit xác nhận cùng giá trị 11/11, áp nguyên; 1 needs-file-audit (1914) — audit tự giải quyết (chỉ thêm Ư vào dòng gasp, giữ nguyên dòng cụt sau).
- Quét bổ sung toàn bộ 185 dòng JP chứa っ: **0 gasp sweep bỏ sót**. Các っ còn lại đều đã được diễn hoặc là っ nhấn mạnh gắn với từ nội dung (xem §6).
- Ghi chú sweep: JP của sweep cho file này khớp JP bộ tốt (không có vấn đề stale-set như ふかみh2).

## 5. Thuật ngữ chờ đợt thống nhất (ghi nhận, không tính sai)

- **Tên công ty "Đường sắt Ohito" (1 dòng, giữ nguyên — park có lý do):** 2748 "Công ty Cổ phần Đường sắt Ohito". Đây là câu hỏi đặt tên riêng: "Đường sắt Ohito" xuất hiện 215 lần toàn dự án vs "Đường sắt Ohitoyo" 5 lần — chỉ Hieu mới quyết được có đổi tên công ty đường sắt không (cf. ROUTE-AUDIT). Theo chỉ đạo mới 21/11 01:51, đây thuộc diện "sở thích cá nhân của Hieu" nên được park, với lý do này.
- **Đã quyết và sửa trong audit (không chờ thống nhất):** 御一夜 (địa danh/trạm) → "Ohitoyo" 7 dòng (1733, 1754, 2372, 2355, 1696, 1200, 1777); 湯医 → "Yunoi" 1 dòng (1754, furigana ゆのい là bằng chứng quyết định); "Kiha 07" → "KiHa 07" (2940, sai chính tả theo quyết định 19/11); "Jutsusen" → "Jutsu-sen" (2258, dạng đã chốt); Seki "ông nội" → "ông ngoại" (1815, quyết định đã chốt 20/11).

## 6. Đã kiểm tra và không tính sai

- **Thán từ っ (えっ/なっ/いやっ/うおっ/うむっ):** 1598 "Hả!?", 1475/1476 "Cái gì!?", 2627 "Không!?", 2903 "(Không)", 1592 "Ua!?", 1628 "Ừm!" — sweep phân loại raw-tsu/already-rendered (tiền lệ 共通14 1443 うおっ raw-tsu; lr h3 1307 うむっ already-rendered); VN đã diễn được thán từ, giữ nguyên.
- **あっ―― bị cắt bởi gạch ngang:** 1602 "A——", 1603 "A——A" — gạch ngang đã diễn được sự ngắt tiếng; giữ nguyên theo tiền lệ ハチロク01 2319 (không thêm Ư).
- **っ nhấn mạnh gắn với từ nội dung:** 1851/1585 くそっ, 1645 よしっ, 1490 ですがっ, 1764 油切れかっ, 1878 これはっ, 1881 こそっ/ぞっ, 2656 くるっ, 1905 様っ, 1546 ハチロクっ, 1801 馬鹿者がっ, 1744 なのにっ――, 1679/1867/1676/1688/1852 (lắp bắp, gạch ngang đã diễn), 1639 はいっ, 1529 ましたっ, 1767 はいっ, 1640 痛かっ, 1842 大阿呆がっ, 1813 父さんっ, 1816 じいちゃんっ — đều là っ nhấn mạnh/cắt câu, không phải gasp; giữ nguyên.
- **SFX đã diễn:** 2925 (ざくっ→"Phập"), 2936, 2123 (ボっ→"Phụt!"), 2916, 2922 (パンっ→"Bốp!!!"), 2923/2924, 2917 (ぽかっ→"Bộp!"), 2926 (ズォボーッツ→"Xìiiiiiiiii"), 1196 (ぅはっ→"Ư hự!"), 1620 (くっ→"hự!"), 2272 (ぐ、と→"Ưực."), 1608 (はっ→"ha", んっ→"ưm"), 2846 (ほーーーっと→"Phùuu").
- **2475 視界をっ:** JP cụt câu (thiếu động từ); VN bổ sung động từ duy nhất có thể ("che khuất tầm nhìn") — không bịa thêm nghĩa mới, giữ nguyên.
- **1816 Nagi gọi Minokasa "Ông nội!?":** Minokasa không phải Seki; quyết định 20/11 chỉ đổi các dòng Seki — giữ nguyên.
- **1495 尻を拭う → "dọn dẹp rắc rối":** làm nhẹ cách nói tục nhưng giữ đúng nghĩa ("cha lo hậu quả cho con gái"); giữ nguyên.
- **1225/2742 共存 → "Cộng tồn":** nhất quán 2 dòng, giữ nguyên.
- **1633 おっと → "Ây da!":** cách diễn hợp lệ; "Ối" chỉ là đề xuất (tiền lệ h7 861), chưa phải quyết định chốt — giữ nguyên.
- **1721 Kisaki tự xưng "Tớ":** nói với cả nhóm hỗn hợp (Hibiki, Soutetsu, mọi người), không phải riêng Soutetsu hay Paulette nên không áp quy tắc "em với Soutetsu / tôi với Paulette" — giữ nguyên.
- **"mình" trong độc thoại:** 2247 "giống như mình", 2558 "Tôi nghĩ... mình cũng đã biết", 2797 "chính mình", 2184 "theo ý mình", 2275 "gồng mình", 2552 "lao mình ra", 2489 "cơ thể mình", 2589 "tay mình" — đều là "mình" ở vị trí tân ngữ/so sánh/quán dụng, không phải đại từ chủ ngữ độc lập; giữ nguyên (chỉ sửa "mình" làm chủ ngữ độc lập).
- **1703 "E, m và":** tách lắp bắp của "Em" (わた、くし), diễn đúng JP; giữ nguyên.
- **1175 "ông cháu":** diễn chung cho 祖父・孫 (Seki–Fukami), không nêu nội/ngoại; giữ nguyên.
- **2682 砂撒き gloss "phun cát":** viết thường vì ở giữa câu, đúng thuật ngữ đã chốt; giữ nguyên.

## 7. Lượt soát 2 và khối TOML

**Lượt soát 2: 59/59 tái kiểm chứng, 0 bỏ, 1 sửa + 7 thêm.** Lỗi sửa ở lượt 2: 1900 — lần build đầu chỉ thay "Anh" hoa mà sót "anh" thường trong "Nhưng anh muốn nhiều hơn thế" (do `\n` literal trong CSV3 làm regex quét máy bỏ sót dòng này ở lượt 1); đã sửa thành "tôi" và kiểm tra lại toàn bộ bằng quét chuẩn hoá `\n`. 7 dòng thêm ở lượt 2: 1733, 1754, 2372, 2355, 1696, 1200, 1777 (御一夜/湯医) — quyết và sửa theo chỉ đạo mới của Hieu 21/11 01:51, mỗi dòng đã đọc lại JP/TW trước khi chốt.

**Kiểm chứng cơ học:** JSON 59 mục (khóa dạng chuỗi); jp/tw/old_vn khớp CSV3 59/59; mỗi fix chỉ khác old VN ở đúng chỗ sửa (đã kiểm tra diff từng dòng — các fix nhiều chỗ thay chỉ là "anh"→"tôi" lặp lại hoặc đổi từ gloss dài ngắn khác nhau trong cùng một thẻ %l); khối TOML dưới đây parse OK bằng tomllib, 59 khóa, 0 sai lệch giá trị so với JSON.

```toml
"1200" = "「——Tôi biết Ohitoyo là một thị trấn như vậy.\\nThế nên tôi mới muốn bảo vệ nó.」"
"1454" = "「Không, không được. Tôi sẽ đi.」"
"1463" = "「Không đâu ạ, làm gì có chuyện——Ư!!?」"
"1481" = "「Cùng vượt qua nào. Chính hôm nay.\\nTôi và em——hai chúng ta.」"
"1493" = "「Nhưng, kể từ khi gặp em. Tôi không còn là đồ vật nữa.\\nNhờ khao khát em——tôi đã trở thành một người đàn ông thực thụ」"
"1505" = "「Còn em thì sao? Vẫn là đồ vật ư?\\nEm, không khao khát tôi sao——」"
"1508" = "「Em không cô đơn đâu. Cả tôi, cả em đều vậy.」"
"1509" = "「Em không còn cô đơn nữa. Không cô đơn đâu.\\nVì có tôi, có em——vì chúng ta đang ở đây.」"
"1523" = "「Em, đã không thể vượt qua cây cầu đó.\\nTôi, cũng đã không thể vượt qua cây cầu đó.」"
"1541" = "「Hachiroku…… Tôi……」"
"1542" = "「Hachiroku. Tôi muốn có em」"
"1547" = "「Hachiroku! Tôi bật thiết bị thổi gió nhé, được không!\\nTình trạng \\x%lカマ;#00ffc040;lò hơi%l;#; không được tốt lắm.」"
"1551" = "「Hachiroku, tôi bật thiết bị thổi gió nhé.」"
"1614" = "「Ư! Ra là vậy, cái này cũng là do áp suất không khí——Ư!!?」"
"1622" = "「Ừ. Đúng là vậy. Nếu không làm thế thì tôi đã không thể sống tiếp.\\nBây giờ nhìn lại…… đó đúng là một cuộc sống của đồ vật nhỉ」"
"1684" = "「Cây cầu đó, quá khứ đó.\\nTôi cũng giống em. Không thể vượt qua được.」"
"1686" = "「Tôi cũng muốn Hachiroku, cả em nữa.\\nCũng khao khát được sở hữu tôi, được độc chiếm tôi」"
"1696" = "「Tôi chỉ làm việc đương nhiên thôi. Với tư cách là một người liên quan đến đường sắt.\\nVà với tư cách là một thành viên của Ohitoyo.」"
"1701" = "「Tôi và Hachiroku cũng sẽ về cùng」"
"1712" = "「Không phải là một mối quan hệ được ban cho. Tôi muốn em là của tôi, của riêng tôi thôi.\\nTôi muốn độc chiếm em, muốn em trở thành gia đình của tôi」"
"1714" = "「Tôi là chủ sở hữu và là Master.」"
"1719" = "「Tôi cũng từng là đồ vật mà.\\nCũng từng là tồn tại chỉ hoạt động vì một ai đó thôi」"
"1733" = "「Nào, về thôi. Về Ohitoyo.」"
"1735" = "「Thế nên, tôi muốn vượt qua. Cây cầu đó.」"
"1737" = "「Xin lỗi.\\nTôi sẽ không lặp lại sai lầm tương tự nữa.」"
"1754" = "「Đúng vậy, đi đến \\x%l三角線;#00ffc040;đường tam giác%l;#; ở Yunoi thì sẽ an toàn hơn.\\nTừ đó chúng ta sẽ quay đầu, hướng về phía trước và trở về Ohitoyo.」"
"1777" = "「Ví dụ như, giữa ông và tôi cũng vậy.\\nTình cảm trân trọng Ohitoyo, chắc chắn là chúng ta giống nhau.」"
"1815" = "「Ông ngoại……」"
"1821" = "「Hiện tại, sao.\\nCuộc sống của tôi trong khoảnh khắc này, lúc này là——」"
"1834" = "「Tiền bối Kisaki——Ư!」"
"1836" = "「Và người đã ban cho tôi điều đó.\\nChính là em, Hachiroku」"
"1856" = "「Cây cầu của ngày hôm đó.\\nTôi và em——」"
"1890" = "「Sau vụ tai nạn đó, cho đến trước khi gặp em——\\ntôi cũng chỉ là một tồn tại hoạt động nhằm hoàn thành mục đích của ai đó mà thôi」"
"1893" = "「Nếu vậy. Thì tôi cũng từng là \"đồ vật\" nhỉ」"
"1900" = "「Đúng là vậy. Nhưng tôi muốn nhiều hơn thế.\\nTôi——Tôi——」"
"1910" = "「Ư!」"
"1911" = "「Ư!!!」"
"1912" = "「Ư!!?」"
"1914" = "「Ư!!?\\nNgài Soutetsu, xin hãy đổi chỗ cho em! Em sẽ」"
"1915" = "「Ư!?」"
"1924" = "「Ư!」\\n「Ư!」"
"2140" = "Không phải vì bị ai đó sai bảo, cũng chẳng phải để hoàn thành mục đích nào cả.\\nChỉ đơn thuần là dục vọng của chính bản thân tôi, khao khát mãnh liệt đến thế này."
"2195" = "Nhưng…… chạy tàu trong điều kiện thời tiết khắc nghiệt gần như không có tầm nhìn thế này,\\nthì ngay cả ban ngày tôi cũng chưa từng trải qua bao giờ——Ư!?"
"2258" = "Tiếng \\x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới.\\nĐể vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsu-sen một cách an toàn——"
"2355" = "Nhưng khi về đến ga Ohitoyo rồi, thì dù có hong khô đến mức nào đi nữa.\\nChắc chắn sẽ bị vắt kiệt sức thêm nữa thôi."
"2368" = "Sau vụ tai nạn đó. Từ \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; cho đến những người đồng đội.\\nTừ tất cả những người đã cùng chung sống trong khoảng thời gian đó——"
"2372" = "Cho đến khi bình an trở về ga Ohitoyo,\\ncứ thong thả nghỉ ngơi, sưởi ấm và hong khô người là được."
"2374" = "Vì không có phụ lái tàu, tôi phải quay sang xúc than,\\nnên người lái \\x%l8620;#00ffc040;8620%l;#; với tư cách là \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#;, chính là Hachiroku."
"2398" = "Chỉ dựa vào kinh nghiệm.\\nChỉ những gì đã tìm hiểu và tích lũy từ trước đến nay——Ư!?"
"2455" = "Theo dõi trạng thái thân xe một cách thích hợp, và đưa ra chỉ thị lái tối ưu nhất.\\nNăng lực của \\x%l運転体;#00ffc040;thân vận hành%l;#;, Hachiroku hiện tại không thể phát huy được."
"2514" = "Góc nghiêng của \\x%l整備体;#00ffc040;thân bảo trì%l;#; vô cùng nghiêm nghị và căng thẳng,\\nđẹp đến mức khiến tôi cảm thấy đáng sợ——"
"2582" = "Nên tôi mới muốn vượt qua.\\nVì có Hachiroku ở bên, nên tôi mới có thể vượt qua được."
"2678" = "Cảm giác an tâm khi tôi làm \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#; kết hợp với \\x%l運転体;#00ffc040;thân vận hành%l;#; của Hachiroku——\\ncảm giác có thể hoàn toàn giao phó tấm lưng cho nhau, bây giờ không còn nữa."
"2741" = "Và giờ đây, tôi đang khao khát mãnh liệt, vô cùng mãnh liệt,\\nmuốn được cùng em đi xa hơn nữa, vượt qua cả nhà ga cuối cùng."
"2746" = "Âm thanh không dừng lại.\\nThậm chí còn ngày càng lớn hơn——Ư!"
"2910" = "（Nhưng mà, thế này chẳng khác nào bịt mắt. Với \\x%l整備体;#00ffc040;thân bảo trì%l;#; của Hachiroku,\\nthì hiệu suất cảm biến quá kém.）"
"2927" = "（Để Hachiroku——đóng vai trò \\x%l機関士;#00ffc040;thợ lái đầu máy%l;#;）"
"2940" = "（Nếu \\x%lキハ07;#00ffc040;KiHa 07%l;#; có thể hoạt động thương mại trở lại,\\nthì cả về mặt tài chính lẫn vận hành đều sẽ có khoảng dư dả lớn.）"
"2948" = "（Đúng nghĩa đen là mò mẫm rồi đây.）"
```

Kết bài
