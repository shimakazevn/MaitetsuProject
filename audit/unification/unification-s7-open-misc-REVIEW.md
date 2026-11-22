# Unification §7 OPEN misc — REVIEW (U14c)

**Phạm vi:** §7 OPEN O38–O60 + O63–O65 (26 mục). O61 đã quyết ở U9, O62 đã quyết ở U3 — ngoài phạm vi, không đụng tới.
**Chuỗi cơ sở:** 100 mục / 2.686 dòng (U13b đã merge 22/11 ~13:00).
**Kết quả batch này:** 21 dòng mới, 9 mục có sửa (O38, O44, O47, O49, O50, O53, O56, O57, O64); 17 mục giữ nguyên (0 dòng).

**Phương pháp:** old_vn theo thứ tự ưu tiên: unif đã merge (theo thứ tự merge) > moan > audit > CSV3 (bộ tốt 87.833 dòng, đã bỏ 3.898 dòng stale). jp/tw trong JSON khớp CSV3 tuyệt đối modulo chuẩn hóa duy nhất U+3000 → space. Mọi giá trị fix viết tay từ JP (+TW); JP thắng TW khi mâu thuẫn. Không dùng script để sửa hàng loạt — script chỉ dùng để tra cứu/liệt kê/kiểm chứng. F5 (điều phối viên 22/11 ~12:50): token SFX romaji viết hoa ở mọi vị trí trong fix mới.

---

## O38. 凪ふかみ08a 2426 — SỬA (1 dòng)

**File:** `凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml` — Fukami độc thoại.

- **JP:** `例え、双鉄おにいさんの隣にいるのが、\nわたしじゃなくても――それでも、やっぱり。`
- **TW:** `即使在他身邊的人不是我也無妨。`
- **old_vn (csv3):** `Dù cho người ở bên cạnh anh Soutetsu,\nkhông phải là mình――thì mình vẫn mong như vậy.`
- **fix:** `Dù cho người ở bên cạnh anh Soutetsu,\nkhông phải là mình――thì mình vẫn mong anh ấy được hạnh phúc.`
- **Lý do:** JP bỏ lửng ở `やっぱり。` — câu chưa hoàn thành, đối tượng "mong" không nói ra. TW hoàn thiện bằng "cũng chẳng sao" (không sao cả). VN cũ "vẫn mong như vậy" mơ hồ — "như vậy" là như thế nào không rõ. Dòng kề trước 2665 nói rõ đối tượng: `Mình muốn anh Soutetsu được hạnh phúc.` Chọn hướng (b) của audit review: giữ "vẫn mong" nhưng viết rõ đối tượng từ 2665. Chỉ sửa nửa sau câu; nửa đầu giữ nguyên.

## O44. ニイロク01 1592 / 1593 / 2337 — SỬA (3 dòng)

**File:** `ニイロク01_正和四十一年・粉蔵.txt.toml` — TW dịch sai hệ thống từ 脈 (mạch) thành 希望 (hi vọng); audit đi theo TW nên sai theo. JP thắng TW.

### 1592 (Akai)

- **JP:** `「脈は――確かにありますが」`
- **TW:** `「希望——確實是有的啊」`
- **old_vn (audit):** `「Hi vọng thì——đúng là có thật.」`
- **fix:** `「Mạch thì——đúng là có đập thật.」` (khôi phục đúng VN CSV3)
- **Lý do:** JP nói về mạch (脈). Dòng kề xác nhận: 1593 `脈……ですか`, độc thoại 2165 Soutetsu vô thức nắm cổ tay mình (bắt mạch). Audit đã sửa sai theo TW.

### 1593 (Akai) — mở rộng O44, cùng lỗi, dòng kề ngay sau

- **JP:** `「脈……ですか」`
- **TW:** `「希望……啊」`
- **old_vn (csv3):** `「Hi vọng...... sao.」`
- **fix:** `「Mạch...... sao.」`
- **Lý do:** Cùng từ 脈, cùng lỗi TW, cùng người nói, dòng kề ngay sau 1592. Để lại "Hi vọng" ở dòng ngay sau khi đã sửa 1592 thành "Mạch" thì mạch hội thoại vỡ. Chỉ thay từ sai, giữ nguyên cấu trúc câu.

### 2337 (monologue) — mở rộng O44, cùng lỗi, cùng file

- **JP:** `（脈、ですか）`
- **TW:** `（有希望嗎）`
- **old_vn (csv3):** `（Hi vọng, sao）`
- **fix:** `（Mạch, sao）`
- **Lý do:** Cùng cụm `脈、ですか` vọng lại trong độc thoại, cùng lỗi TW. Chỉ thay từ sai.

## O47. 日々姫03 2266 / 2608 / 2873 — SỬA (3 dòng)

**File:** `日々姫03_客車手配.txt.toml` — Paulette tự xưng "mình" → "em" trong cả 3 dòng. Người nghe là Soutetsu trong cả 3 dòng; P13 + tiền lệ U6/O1 (Soutetsu→Paulette "em" mọi ngữ cảnh, không ngoại lệ công việc) — Paulette xưng "em" với Soutetsu. Lý do giữ của audit ("dạng xưng hô mềm, trung tính") ghi nhận là bằng chứng ngược nhưng không thắng được quy tắc hệ thống + bằng chứng người nghe.

### 2266 (Paulette)

- **JP:** `「けど、今はわたしより、\nもっと双鉄くんの手伝いを必要な人が、きっといるから」`
- **TW:** `「不過比起我來，現在應該有更需要雙鐵君幫忙的人吧」`
- **old_vn (csv3):** `「Nhưng mà, bây giờ chắc chắn có người\ncần sự giúp đỡ của Soutetsu hơn mình đấy.」`
- **fix:** `「Nhưng mà, bây giờ chắc chắn có người\ncần sự giúp đỡ của Soutetsu hơn em đấy.」`
- **Lý do:** Dòng 2371 Soutetsu đáp lại: "Vất vả cho em rồi" — người nghe là Soutetsu. Chỉ đổi "mình" → "em".

### 2608 (Paulette)

- **JP:** `「わかりました」`
- **TW:** `「我知道了」`
- **old_vn (csv3):** `「Mình hiểu rồi.」`
- **fix:** `「Em hiểu rồi.」`
- **Lý do:** Dòng 2755 Soutetsu dặn dò, 2608 đáp lại — người nghe Soutetsu.

### 2873 (Paulette)

- **JP:** `「じゃ、わたしこれから役所に行きます。姉妹都市の話、\n先方に、少しでも報告できること作りたいですし」`
- **TW:** `「那我現在就到市政府去了。關於姐妹城市那方面，我也想至少先做一點能向對方報告的事」`
- **old_vn (csv3):** `「Vậy, bây giờ mình sẽ đến tòa thị chính. Về chuyện thành phố kết nghĩa,\nmình cũng muốn tạo ra một chút gì đó để có thể báo cáo với phía bên kia.」`
- **fix:** `「Vậy, bây giờ em sẽ đến tòa thị chính. Về chuyện thành phố kết nghĩa,\nem cũng muốn tạo ra một chút gì đó để có thể báo cáo với phía bên kia.」`
- **Lý do:** Tiếp tục cùng mạch trao đổi với Soutetsu. Đổi cả 2 "mình" → "em".

---

## O49. Olivy độc thoại "tôi" vs "mình" — SỬA (8 dòng)

**File:** `lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml` — độc thoại Olivy.

**Quyết định: thống nhất về "tôi".** Đếm cơ học trên bộ tốt (đã loại "cửa mình" — từ chỉ bộ phận sinh dục, không phải đại từ): độc thoại có 29 dòng chứa "tôi" (26 dòng chỉ "tôi" + 3 dòng cả hai), 12 dòng chứa "mình", trong đó chỉ 8 dòng "mình" là đại từ tự xưng thật; 4 dòng còn lại là sở hữu phản thân / thành ngữ cố định ("phong cách của mình", "giật nảy mình" ×2, "cơ quan sinh dục của mình" — chủ ngữ là Công chúa Tàu điện, ngôi thứ ba) nên giữ nguyên. Lời thoại của Olivy (char ひよこ) cũng dùng "tôi" 15 lần vs "mình" 3 lần. "Tôi" vừa là đa số tuyệt đối, vừa là dạng trung tính mặc định. (Lưu ý: con số 12/18 trong audit đếm theo cách khác, không tái hiện được bằng đếm cơ học trên bộ tốt — xem cờ O49 ở cuối.)

### 1367

- **JP:** `フシチョーハカセの顔がちょこっと曇っちゃう。\nああ、やっぱりかぁ。しょーがないよね。自覚もあるし。`
- **TW:** `「你通過法定檢查了。不過——」`
- **old_vn (csv3):** `Khuôn mặt của Tiến sĩ Phoenix hơi tối sầm lại.\nAh, quả nhiên là vậy. Hết cách rồi nhỉ. Mình cũng tự nhận thức được mà.`
- **fix:** `Khuôn mặt của Tiến sĩ Phoenix hơi tối sầm lại.\nAh, quả nhiên là vậy. Hết cách rồi nhỉ. Tôi cũng tự nhận thức được mà.`
- **Lý do:** "Mình" là đại từ tự xưng (JP 自覚もあるし — "tôi cũng tự nhận thức được"). Chỉ đổi đại từ.

### 889

- **JP:** `漏れちゃったみたいなタメイキ。ちょっと辛そう。\nフシチョーハカセ、わかってたけどやさしいんだ。`
- **TW:** `「……」`
- **old_vn (csv3):** `Một tiếng thở dài buột ra. Trông cô ấy có vẻ hơi đau khổ.\nTiến sĩ Phoenix, mình biết mà, cô ấy rất tốt bụng.`
- **fix:** `Một tiếng thở dài buột ra. Trông cô ấy có vẻ hơi đau khổ.\nTiến sĩ Phoenix, tôi biết mà, cô ấy rất tốt bụng.`
- **Lý do:** "mình biết mà" = tôi đã biết (về tính cách của Tiến sĩ). Chỉ đổi đại từ.

### 1531

- **JP:** `広げてみたら――うわわ、やっぱり。何回みてもこの写真、\nすっごく不思議で、ぞわぞわってするぅ！`
- **TW:** `「嗯。不想把這個隨隨便便地放在一邊，帶在身上又不好帶，就折起來了」`
- **old_vn (csv3):** `Mở ra xem thử——oái, quả nhiên là vậy. Dù có nhìn bao nhiêu lần đi nữa, bức ảnh này\nvẫn thật kỳ lạ, khiến mình sởn cả gai ốc!`
- **fix:** `Mở ra xem thử——oái, quả nhiên là vậy. Dù có nhìn bao nhiêu lần đi nữa, bức ảnh này\nvẫn thật kỳ lạ, khiến tôi sởn cả gai ốc!`
- **Lý do:** "khiến mình sởn gai ốc" — "mình" là người cảm nhận (Olivy). Chỉ đổi đại từ.

### 1900

- **JP:** `使い方、なんだかオリヴィわかった気がする。`
- **TW:** `「雙頭……假陽具。因為是有兩個頭的陽具……所以這麼叫」`
- **old_vn (csv3):** `Cách sử dụng, không hiểu sao Olivy lại có cảm giác mình đã hiểu ra.`
- **fix:** `Cách sử dụng, không hiểu sao Olivy lại có cảm giác tôi đã hiểu ra.`
- **Lý do:** "mình" trong mệnh đề nhúng chỉ Olivy (chủ ngữ là tên riêng "Olivy" tự xưng ngôi thứ ba). File này Olivy trộn tên riêng + "tôi" thường xuyên (1465, 1905, 2317), nên "tôi" nhất quán với giọng file.

### 1546

- **JP:** `言葉とよだれが一緒になって、もうどろどろで垂れ流しで。\nばっちくて綺麗で――だからオリヴィ、わかった気がする。`
- **TW:** `「嗯唔唔！！啊？！好激烈——好爽！一直這麼激烈下去的話……！」`
- **old_vn (csv3):** `Lời nói và nước bọt quyện vào nhau, chảy ròng ròng.\nDơ bẩn nhưng lại rất đẹp——vì thế Olivy, có cảm giác như mình đã hiểu ra.`
- **fix:** `Lời nói và nước bọt quyện vào nhau, chảy ròng ròng.\nDơ bẩn nhưng lại rất đẹp——vì thế Olivy, có cảm giác như tôi đã hiểu ra.`
- **Lý do:** Cùng mẫu 1900.

### 1617

- **JP:** `だってオリヴィ、いつ壊れるかわからないんだし、\nそれまでにヨノナカのこと、ちょっとでも多くわかりたい。`
- **TW:** `「如果不是不應該知道的事，那奧莉薇想知道」`
- **old_vn (csv3):** `Bởi vì Olivy không biết bao giờ mình sẽ hỏng,\nnên trước lúc đó, tôi muốn hiểu thêm về thế giới này, dù chỉ một chút thôi.`
- **fix:** `Bởi vì Olivy không biết bao giờ tôi sẽ hỏng,\nnên trước lúc đó, tôi muốn hiểu thêm về thế giới này, dù chỉ một chút thôi.`
- **Lý do:** Mâu thuẫn ngay trong dòng: nửa đầu "mình", nửa sau "tôi". Thống nhất về "tôi".

### 1817

- **JP:** `「あ！ それだったら見てみて勉強したい、ネヤゴト！\nオリヴィ、知らないまんまのことあるのヤだから」`
- **TW:** `「說的是詠字報紙上面照片的事。照片上雖然是一男一女，但這次由同性的我倆進行示範」`
- **old_vn (csv3):** `「A! Nếu là chuyện đó thì tôi muốn xem thử để học hỏi, chuyện phòng the ấy!\nVì Olivy không thích có chuyện mình không biết mà.」`
- **fix:** `「A! Nếu là chuyện đó thì tôi muốn xem thử để học hỏi, chuyện phòng the ấy!\nVì Olivy không thích có chuyện tôi không biết mà.」`
- **Lý do:** Mâu thuẫn ngay trong dòng: câu đầu "tôi", câu sau "mình". Thống nhất về "tôi".

### 1821

- **JP:** `けど知りたい。知らない方がよかっただとか、\nあのとき聞いておけばだとか、絶対に思いたくない。`
- **TW:** `「請問，不死鳥博士」`
- **old_vn (csv3):** `Nhưng tôi muốn biết. Tôi tuyệt đối không muốn nghĩ rằng\nthà không biết còn hơn, hay giá như lúc đó mình đã hỏi.`
- **fix:** `Nhưng tôi muốn biết. Tôi tuyệt đối không muốn nghĩ rằng\nthà không biết còn hơn, hay giá như lúc đó tôi đã hỏi.`
- **Lý do:** Dòng đã dùng "tôi" 2 lần; "mình" ở cuối là lệch duy nhất. Thống nhất về "tôi".

**Giữ nguyên trong O49 (4 dòng, không tính sửa):** 1668 "phong cách của mình" (sở hữu phản thân, chủ ngữ Công chúa Tàu điện); 1548 + 1466 "giật nảy mình"/"giật mình" (thành ngữ cố định, chủ ngữ Công chúa Tàu điện); 1524 "cơ quan sinh dục của mình" (sở hữu phản thân, chủ ngữ Công chúa Tàu điện). Không phải đại từ tự xưng của Olivy.

## O50. 凪h2 2515 — SỬA (1 dòng)

**File:** `凪h2_おとなの水着.txt.toml`

- **JP:** `「ああ――あふゅいっ――ひ、へ――へーえきっ――\nおなかっ――あかちゃん――おへや、びゅうびゅう」`
- **TW:** `「啊……危……沒、沒事……肚子裡……造人房間，咻咻的」`
- **old_vn (csv3):** `「A——Nóng quá——T, ti——Tinh dịch——\nBụng——Em bé——Căn phòng, phụt phụt」`
- **fix:** `「A——Afyui——T, ti——Tinh dịch——\nBụng——Em bé——Căn phòng, phụt phụt」`
- **Lý do:** あふゅいっ là tiếng rên thở, không phải từ có nghĩa — JP không có 熱い/暑い (nóng) nên "Nóng quá" là bịa; TW 危 cũng không có căn cứ JP (không có 危ない). Theo romaji fallback (Hieu 21/11): dùng romaji của âm JP. Hepburn a+f+yu+i = "Afyui", viết hoa theo F5. Phần còn lại của dòng giữ nguyên.

## O53. 凪ふかみ02 1544 — SỬA (1 dòng)

**File:** `凪ふかみ02_命の重さ.txt.toml` — Soutetsu.

- **JP:** `「であれば、すまんがよろしく頼む。\nということだ。僕はいつでも――」`
- **TW:** `「真抱歉，那就交給你了。就是這樣，我隨時都可以——」`
- **old_vn (csv3):** `「Nếu vậy, xin lỗi nhưng nhờ cô nhé.\nLà vậy đấy. Anh thì lúc nào cũng——」`
- **fix:** `「Nếu vậy, xin lỗi nhưng nhờ em nhé.\nLà vậy đấy. Anh thì lúc nào cũng——」`
- **Lý do:** Người nghe là **Fukami**, không phải Hachiroku — parent đã kiểm chứng 21/11 ~09:20 (audit review §3): dòng kề thực sự là 1542 (Fukami đề nghị giúp) và 1549 (Fukami khẳng định "Để tớ làm cho"); Hachiroku không có dòng thoại nào gần 1544. Soutetsu gọi Fukami là "em" trong file này (1575 "Cảm ơn em", 1613); "cô" trong file này chỉ dùng với Hachiroku (1226, 1325). Câu sau "Anh thì lúc nào cũng——" giữ nguyên "Anh" — đúng với người nghe Fukami. (Fix sai "Anh"→"Tôi" trước đây của audit đã bị parent loại; không áp lại.)

## O56. ハチロクh8 798 — SỬA (1 dòng)

**File:** `ハチロクh8_桜色のひめごと.txt.toml` — chuỗi SFX.

- **JP:** `「じゅぼっ！ じゅぶっ！ れるっ！ れろおっ！\nじゅるるっ！ じゅ！ じゅぼっ！ ぶぢゅ！！」`
- **TW:** `「啾啵！啾！咻嚕！嗯！啾嚕！啾！啾啵！噗啾！！」`
- **old_vn (audit):** `「Nhóp nhép! Nhóp nhép! Liếm! Mút mát!\nChóp chép! Nhóp! Nhóp nhép! Bụp!!」`
- **fix:** `「Nhóp nhép! Nhóp nhép! Rộp! Mút mát!\nChóp chép! Nhóp! Nhóp nhép! Bụp!!」`
- **Lý do:** Theo T77 (điều phối viên E2): token れる/るっ → "rộp"; れろ LOẠI khỏi T77. U13b đã áp "rộp" cho 809/827 cùng file nhưng bỏ sót 798. れろおっ → "Mút mát" giữ nguyên theo tiền lệ 827. ぶぢゅ → "Bụp" của audit giữ nguyên. Chỉ đổi "Liếm" → "Rộp".

## O57. 凪ふかみh1 1303 — SỬA (1 dòng)

**File:** `凪ふかみh1_修学旅行の夜.txt.toml`

- **JP:** `「ん……ちゅっ――んむっ――ふっ――れるっ――\nひょはひょひょ――んっ――ひーはふっ――んっ」`
- **TW:** `「嗯啾……嗯唔……呼……啾……濕漉漉的……嗯……沒關係……嗯」`
- **old_vn (csv3):** `「Ưm... chụt——ưm——phù——liếm——\nkh-không sao đâu——ưm——cứ ra đi——ưm」`
- **fix:** `「Ưm... chụt——ưm——phù——rộp——\nkh-không sao đâu——ưm——cứ ra đi——ưm」`
- **Lý do:** れるっ → "rộp" theo T77. U13b đã đổi dòng song sinh 1291 cùng cảnh (đã là "Rộp"); 1303 bị bỏ sót. Chỉ đổi "liếm" → "rộp"; cách diễn âm ngọng (ひょはひょひょ → "kh-không sao đâu", ひーはふっ → "cứ ra đi") giữ nguyên cả hai dòng.

## O64. 日々姫03 2368 / 2607 — SỬA (2 dòng)

**File:** `日々姫03_客車手配.txt.toml` — Fukami nói về các ông của mình. **Trích dẫn trong list ("日々姫04 2668", "Grand 08 2010") đều sai** — xem cờ O64 ở cuối. Hai dòng thật là 2368/2607 ở 日々姫03.

- **JP (2368):** `「おじいちゃんたちに、\n\x%l保線;#00ffc040;保線%l;#;のことをお願いすればいいんですか？」`
- **TW (2368):** `「只要我拜託爺爺他們進行\x%l保線;#00ffc040;巡線%l;#;就可以了嗎？」`
- **old_vn (csv3, 2368):** `「Có phải là nhờ ông nội và mọi người,\nlo việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; đúng không ạ?」`
- **fix (2368):** `「Có phải là nhờ ông ngoại và mọi người,\nlo việc \x%l保線;#00ffc040;bảo trì đường ray%l;#; đúng không ạ?」`
- **JP (2607):** `「わかりました。おじいちゃんたちに伝えておきます」`
- **TW (2607):** `「我知道了。我會傳達給爺爺他們的」`
- **old_vn (csv3, 2607):** `「Em hiểu rồi. Em sẽ chuyển lời lại cho ông nội và mọi người ạ.」`
- **fix (2607):** `「Em hiểu rồi. Em sẽ chuyển lời lại cho ông ngoại và mọi người ạ.」`
- **Lý do:** "おじいちゃんたち" ở đây là anh em ông Seki — độc thoại 3579 cùng file: `ふかみの曽祖父、早瀬堰さんとそのご兄弟` ("Ông cố của Fukami, ông Hayase Seki và các anh em của ông"). Tiền lệ đã chốt: 凪ふかみ02 2299 "ông nội Fukami" → "ông ngoại Fukami" (cùng nhóm Seki + anh em) trong audit; T20 Seki = "ông ngoại". Chỉ đổi "nội" → "ngoại", giữ nguyên tag %l và phần còn lại.

---

## Các mục GIỮ NGUYÊN (0 dòng)

### O39. ポーレット13 1357 — GIỮ "Em——em, làm được rồi!"

JP `「わたし――わたし、やりました！」`. Dòng 1356 Paulette nói trang trọng với hội đồng (`ご懸念、ごもっともと存じます`), 1357 bùng ra câu cảm thán cá nhân "Tôi làm được rồi!", rồi 1363–1364 trở lại giọng hội đồng ("chúng tôi đang dự định nộp đơn xin…"). Soutetsu đứng ở cánh gà xem (1884: `舞台袖から、僕は覗いて`), và 1309 anh đáp trực tiếp thành tích của cô: "Em làm rất xuất sắc." Đây là câu reo cá nhân với Soutetsu, không phải xưng hô hội đồng — "em" đúng. Audit review bảo cần kiểm tra trong game, nhưng bằng chứng người nghe (cánh gà + 1309 + mạch trang trọng→cá nhân→trang trọng) đã đủ theo ủy quyền.

### O40. れいなh4 2288 — GIỮ "Em nói là năm nay sẽ tổ chức Halloween đúng không."

JP `「ああ。今年はハロウィンを開催するといっていたな」` — chủ ngữ といっていた bị lược. Reina là người gợi chủ đề Halloween (2182: hóa trang Halloween; 1945 Soutetsu hỏi cô có phiền não chuyện hóa trang không); cả cảnh chỉ có hai người (ふたりっきりのハロウィン); 2295 Reina khẳng định ngay sau: "Đúng vậy ạ~, là Halloween đó ạ~". Đọc "Em nói" (Reina từng nói với Soutetsu) là đọc hợp lý nhất từ mạch hội thoại. Paulette chỉ xuất hiện như chủ đề được nhắc tới (2219, 2335), không phải người thông báo Halloween. Audit ghi "chưa chắc chắn, chờ kiểm tra trong game" — quyết theo ủy quyền: giữ nguyên, kiểm tra trong game vẫn có thể xác nhận sau.

### O41. lr真闇追加02 1545 — GIỮ "Đối với anh"

1542 Reina hỏi thẳng Soutetsu, 1545 anh trả lời cô; P1 Soutetsu "anh" với Reina. Hai dòng chỉ dẫn nhóm 1548–1549 không đổi người nghe của câu trả lời. old_vn là fix đã gộp ở U4 (T7 Yunoi trên nền "anh" của audit; CSV3 là "em" — đã sửa xong từ trước).

### O42. Gasp sweep — GIỮ (0 dòng)

- 1078/1588 (lr_ふかみh2) và 1566 (ふかみh2): JP/TW/VN bộ tốt đồng nhất; comment `# JP:` trong TOML-2 xác nhận JP bộ tốt (1078 `く――あ……ふか、み――`, 1588 độc thoại deep-throating, 1566 tường thuật). Sự "không chắc" của sweep đến từ JP của bộ STALE. 1078 giữ "Kh" theo M6. Dấu っ cuối 1588 không thêm Ư — ngoài phạm vi mục.
- Grand01 1556: giữ fix audit `「……」` (JP trần `っ`, TW `……`; M5 — dấu ba chấm diễn sự ngắt, Ư sẽ thêm âm JP không có).

### O43. ふかみh1 — GIỮ (0 dòng)

Cả 6 dòng đều là lỗi xoay vòng CSV3 đã được audit sửa (1031, 1034, 1081, 781, 1065), SFX 1675 còn được moan U12b kéo dài thêm. Không còn gì để bỏ.

### O45. ハチロク03 1913 / 1826 — GIỮ

- 1913 giữ "Tôi": thảo luận công việc nhóm; 1950 Nagi / 1982 Fukami đáp lại; tiền lệ P13 nhóm trang trọng.
- 1826 giữ "Tớ…… không sao" + "cảm ơn cậu": người nghe là Nagi (2820 Nagi vỗ lưng cô); cặp "Tớ"/"cậu" nhất quán (audit review §5).

### O46. ハチロク15a — GIỮ / CỜ CHO ĐIỀU PHỐI VIÊN (0 dòng)

Mục như trích dẫn **không tái hiện được**: không có mẫu ký hiệu 'N' 20 dòng nào trong CSV3 bộ tốt / TOML-2 / audit của file này (đã quét N/n độc lập, ン, んっ, "ưn", "nn", [characters]/[selections], ' N '). 1893 `うん……` → "Ưm……" là đúng (tiền lệ cùng file 1855 "ừm!"); 2232 ngắt câu bằng dấu phẩy khớp cách diễn nói lắp đã chốt trong file (1937/2171 "Oli, vy"). Nếu điều phối viên muốn nói tới mẫu khác thì cần diễn đạt lại chính xác.
**Phát hiện ngoài phạm vi (không sửa):** ハチロク15a [characters] 2345 = "Olive" — U10 F36 đã sửa 15b 1908/2063, Grand09 2180/2466, ハチロク02 2823/3034 nhưng sót dòng này; ứng viên T46 còn lại cho U15.

### O48. Common 09 — CỜ CHO ĐIỀU PHỐI VIÊN (0 dòng)

Mục như trích dẫn **không tái hiện được**: key 2054 không tồn tại trong TOML-2 lẫn CSV3 của 共通09; ROUTE-AUDIT mục Common 09 không nhắc tới tỉ lệ này; Michiko (路子) trong Common 09 bộ tốt chỉ có 36 dòng, tự xưng "em" 2 dòng (2721, 2138), "con" 1 dòng (2287, với bố mẹ), **không có "chị"** nào. Quét toàn dự án (đầu dòng sau 「 hoặc đầu câu): "em" 9 dòng, "chị" 3 lần trúng đều là ngôi thứ ba / xưng hô người khác ("chị Hibiki", "Chị Hachiroku"), không có "chị" tự xưng thật nào. Nếu tỉ lệ 23/15 lấy từ đâu khác thì mục cần diễn đạt lại kèm danh sách file+key. Không có dòng nào để sửa.

### O51. 日々姫04 2219 / 2125 / 1938 — GIỮ (0 dòng)

- 2219/2125 giữ "vàng cam" cho 柿色 (màu hồng chín): TW 赤褐色 "nâu đỏ" sai với phần pudding vị dâu (2125). 2219 old_vn là giá trị đã gộp ở U4 ("KiHa 07S").
- 1938 giữ fix audit `Vâng! Tại vì là cho chị hai…` — diễn đúng câu cụt JP `うん！ だってねぇねに`, không lấy phần hoàn thiện của TW ("tôi muốn tự tay pha trà chanh cho chị hai"). ROUTE-AUDIT xác nhận: giữ câu cụt theo JP, chờ Hieu.

### O52. れいな01 2415 — GIỮ + CỜ (0 dòng)

Ô JP bị hỏng (chứa chính văn bản VN); TW là một dòng hoàn toàn khác (tin nhà máy điện, cảm ơn Reina); VN "Bước đi xạo xạc." khớp dòng kề (2348 đi qua cỏ mùa hè). Không thể sửa từ JP/TW — cần kiểm tra nguồn. List ghi "không tính vào số sai".

### O54. 日々姫05 1562 / 1566 / 1947 — GIỮ (0 dòng)

- 1562 Soutetsu "tôi": người nghe là Hachiroku (2747 độc thoại: Hachiroku đồng tình với câu "tôi cũng chưa trưởng thành" của anh; 2096 Hachiroku nói); P1 "tôi" với Hachiroku đúng.
- 1566 Kisaki "tôi": ngữ cảnh công việc (tham quan hội đồng thành phố, bàn về thị trưởng Paulette và thu hút nhà máy; 2158 Hibiki hỏi); quy tắc Kisaki 21/11 ~19:45: công việc/quyết đoán → "tôi".
- 1947 Kisaki "tôi" khi gọi điện thoại (2812 cô cúp máy; đối tác không rõ) + "cô" cho đối tác chưa biết — dạng trung tính an toàn.

### O55. ハチロクh1 1238 — GIỮ fix audit "I——a——Nkuu!!!"

JP `「いっ――あっ――んくうっっっっっっっ！！！」`. Âm đầu là いっ (nguyên âm i), không phải あっ — "Á" sẽ là lỗi sai nguyên âm (cùng họ lỗi mà quy tắc ひゃ đã xử: "Á" chỉ đúng khi JP không có phụ âm mora). Romaji fallback (Hieu duyệt 21/11) cho "I"; tiền lệ h9 2101: くああ → "Kuaa" chứ không giữ "Aaa". Audit tự ghi "nếu Hieu thấy 'Á!' tự nhiên hơn thì trả về 'Á'" — quyết theo quy tắc đã chốt: giữ romaji "I".

### O56. ハチロクh8 1162 — GIỮ fix audit "tan ra"

散らされていく; TW 升天 ủng hộ; CSV3 "bị phân tâm" mới là sai.

### O57. 凪ふかみh1 1291 — GIỮ

Đã là "Rộp" qua U13b (dòng song sinh của 1303); chỉ 1303 cần sửa (xem trên).

### O58. 稀咲h3 2217 / 2238 / 2155 + 稀咲02 2874 — GIỮ (0 dòng)

- 2217 giữ "Kua!" (くあっ, nhất quán M7 romaji).
- 2238 giữ cách diễn hỗn hợp hiện tại (しゅき ngọng → giải mã "hích anh"; ほーへふっ không giải mã được → romaji "Houhefu"; ふぁ → "fa" theo U11a M1 — "fa" thường giữa dòng để cho đợt quét viết hoa F5 ở U15, không sửa ở batch này).
- 2155 giữ "Tuyệt quá!" (しゅごっ = すごっ ngọng; TW 我喜歡 bác bỏ; dòng song song 稀咲h1 1244 cùng token → "tuyệt quá").
- 2874 thực ra ở **稀咲02_新事業案** (list ghi nhầm file là 稀咲h3; key không có trong CSV3/TOML của 稀咲h3) — quyết GIỮ BỎ: audit đã gỡ chú thích "(Bảo hỏa - Hoka / Ngoài ra - Hoka)"; cách chơi chữ 保火/他 (cùng đọc ほか) không nhìn thấy được trong VN, và quy tắc không-thêm-chú-thích + quyết định gỡ có chủ đích của audit thắng. Hieu vẫn có thể yêu cầu khôi phục.

### O59. ハチロク07 2916–2918 — GIỮ

Hachiroku nói với nhiệt kế trong miệng (độc thoại 3333); âm JP rối không diễn được thành âm VN; TW phiên âm la-tinh rối. Tiền lệ dự án (O57/O58): giải mã ngọng ra nghĩa — "A, ngài Soutetsu" / "Vâng, nhờ ngài ạ" / "Ngài cứ yên tâm ạ" giữ nguyên.

### O60. ハチロク03 2149 — GIỮ "Haa~" / "Hafaa~"

Ngáp của Hibiki sau báo cáo công việc (2991: cô và Olivy gục xuống mệt lử; 2261/2535 "mệt quá"). Ngáp KHÔNG phải rên — quy tắc rên fa/fu M1/M2 không áp dụng; TW `哈～` ủng hộ cách đọc ngáp thường. Chênh nhỏ "Haa~" vs "Hafaa~" để nguyên; ép thành "Faa~" sẽ đọc thành token rên.

### O63. 日々姫11 2038 — GIỮ "Chị cứ kỳ vọng đi!"

Người nghe là Mayami: 2051 [真闇] đáp trực tiếp; 2307 Hibiki hỏi "chị" về matcha "anh hai" (Soutetsu) làm. Hibiki→Mayami (chị gái) = "chị".

### O65. ハチロク09 2027 — GIỮ "bác Seki"

JP [せき]堰さん là người lái đò họ Seki (堰 = đập nước), KHÔNG phải ông ngoại Seki — T20 "ông ngoại" không áp dụng. Ngữ cảnh xác nhận: 1753 Hachiroku thắc mắc người lái đò là ai; Soutetsu đoán Seki/Nagare/Osamu. "Bác" với người lái đò lớn tuổi là hợp lý.

---

## Khối TOML (để merge)

```toml
[script]
"2426" = "Dù cho người ở bên cạnh anh Soutetsu,\\nkhông phải là mình――thì mình vẫn mong anh ấy được hạnh phúc."
```

```toml
[script]
"1592" = "「Mạch thì——đúng là có đập thật.」"
"1593" = "「Mạch...... sao.」"
"2337" = "（Mạch, sao）"
```

```toml
[script]
"2266" = "「Nhưng mà, bây giờ chắc chắn có người\\ncần sự giúp đỡ của Soutetsu hơn em đấy.」"
"2608" = "「Em hiểu rồi.」"
"2873" = "「Vậy, bây giờ em sẽ đến tòa thị chính. Về chuyện thành phố kết nghĩa,\\nem cũng muốn tạo ra một chút gì đó để có thể báo cáo với phía bên kia.」"
"2368" = "「Có phải là nhờ ông ngoại và mọi người,\\nlo việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#; đúng không ạ?」"
"2607" = "「Em hiểu rồi. Em sẽ chuyển lời lại cho ông ngoại và mọi người ạ.」"
```

```toml
[script]
"1367" = "Khuôn mặt của Tiến sĩ Phoenix hơi tối sầm lại.\\nAh, quả nhiên là vậy. Hết cách rồi nhỉ. Tôi cũng tự nhận thức được mà."
"889" = "Một tiếng thở dài buột ra. Trông cô ấy có vẻ hơi đau khổ.\\nTiến sĩ Phoenix, tôi biết mà, cô ấy rất tốt bụng."
"1531" = "Mở ra xem thử——oái, quả nhiên là vậy. Dù có nhìn bao nhiêu lần đi nữa, bức ảnh này\\nvẫn thật kỳ lạ, khiến tôi sởn cả gai ốc!"
"1900" = "Cách sử dụng, không hiểu sao Olivy lại có cảm giác tôi đã hiểu ra."
"1546" = "Lời nói và nước bọt quyện vào nhau, chảy ròng ròng.\\nDơ bẩn nhưng lại rất đẹp——vì thế Olivy, có cảm giác như tôi đã hiểu ra."
"1617" = "Bởi vì Olivy không biết bao giờ tôi sẽ hỏng,\\nnên trước lúc đó, tôi muốn hiểu thêm về thế giới này, dù chỉ một chút thôi."
"1817" = "「A! Nếu là chuyện đó thì tôi muốn xem thử để học hỏi, chuyện phòng the ấy!\\nVì Olivy không thích có chuyện tôi không biết mà.」"
"1821" = "Nhưng tôi muốn biết. Tôi tuyệt đối không muốn nghĩ rằng\\nthà không biết còn hơn, hay giá như lúc đó tôi đã hỏi."
```

```toml
[script]
"2515" = "「A——Afyui——T, ti——Tinh dịch——\\nBụng——Em bé——Căn phòng, phụt phụt」"
```

```toml
[script]
"1544" = "「Nếu vậy, xin lỗi nhưng nhờ em nhé.\\nLà vậy đấy. Anh thì lúc nào cũng——」"
```

```toml
[script]
"798" = "「Nhóp nhép! Nhóp nhép! Rộp! Mút mát!\\nChóp chép! Nhóp! Nhóp nhép! Bụp!!」"
```

```toml
[script]
"1303" = "「Ưm... chụt——ưm——phù——rộp——\\nkh-không sao đâu——ưm——cứ ra đi——ưm」"
```

> Ghi chú khối TOML: các khối trên gom theo file, theo thứ tự: 凪ふかみ08a (1 khóa), ニイロク01 (3 khóa), 日々姫03_客車手配 (5 khóa), lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」 (8 khóa), 凪h2_おとなの水着 (1 khóa), 凪ふかみ02_命の重さ (1 khóa), ハチロクh8_桜色のひめごと (1 khóa), 凪ふかみh1_修学旅行の夜 (1 khóa). Tổng 21 khóa = đúng số mục JSON.

---

## Lượt soát 2 (second pass)

Đọc lại toàn bộ 21 giá trị fix đối chiếu JP (không đối chiếu TW, trừ khi JP mơ hồ):

- **Tổng: 21 / tái kiểm chứng: 21 / loại bỏ: 0 / sửa lại: 0.**
- Kiểm tra từng dòng: O38 đối tượng "được hạnh phúc" lấy từ 2665 đúng mạch; O44 cả 3 dòng 脈 → "Mạch" đúng, 1592 khôi phục đúng VN CSV3 (đã kiểm chứng bằng byte: dấu `.` ASCII, không phải `。`); O47 cả 3 dòng "mình" → "em" đúng người nghe Soutetsu; O49 cả 8 dòng "mình" → "tôi" đúng vai tự xưng, 4 dòng "mình" phản thân/thành ngữ đã loại khỏi danh sách sửa; O50 "Afyui" đúng Hepburn a+f+yu+i, viết hoa theo F5; O53 "nhờ em nhé" đúng người nghe Fukami (theo kiểm chứng của parent 21/11 ~09:20); O56/O57 れるっ → "rộp" theo T77, れろおっ giữ "Mút mát" theo tiền lệ 827; O64 cả 2 dòng "ông nội" → "ông ngoại" đúng nhóm Seki (độc thoại 3579 cùng file).
- Kiểm chứng cơ học (đã chạy): JSON 21 mục, đủ 8 trường, key dạng chuỗi, jp/tw khớp CSV3 tuyệt đối modulo U+3000, old_vn khớp bản đồ ưu tiên (unif đã merge > moan > audit > csv3), 0 fix == old_vn, 0 newline thực, 0 `\\n` đôi. Khối TOML: 8 khối, 21 khóa, parse bằng tomllib, 0 sai lệch giá trị so với JSON. Hai lỗi phát hiện trong lúc kiểm chứng đã sửa trước khi chốt: old_vn 1592 (`。」` → `.」` theo fix audit) và fix 1592 (`。」` → `.」` theo VN CSV3 — khôi phục đúng từng byte).

## Kết bài

**Đã quyết (26/26 mục trong phạm vi):**

- Có sửa — 9 mục, 21 dòng mới, 0 dòng gộp: O38 (1), O44 (3 — gồm 1593 + 2337 mở rộng cùng lỗi), O47 (3), O49 (8), O50 (1), O53 (1), O56 (1), O57 (1), O64 (2 — dòng thật là 日々姫03 2368/2607).
- Giữ nguyên — 17 mục, 0 dòng: O39, O40, O41, O42, O43, O45, O46, O48, O51, O52, O54, O55, O58, O59, O60, O63, O65 (lý do từng mục ở trên; O56-1162 và O57-1291 là giữ nguyên trong mục có sửa).

**Cờ cho điều phối viên:**

1. **O46 — mục không tái hiện được.** Không có mẫu 'N' nào trong file ハチロク15a (bộ tốt/TOML/audit). Cần diễn đạt lại chính xác nếu muốn nói tới mẫu khác. Phát hiện ngoài phạm vi: ハチロク15a [characters] 2345 = "Olive" — ứng viên T46 còn lại cho U15 (U10 F36 đã sửa các file khác).
2. **O48 — mục không tái hiện được.** Key 2054 không tồn tại; tỉ lệ "em 23 vs chị 15" không khớp Common 09 (36 dòng Michiko: "em" 2, "con" 1, "chị" 0) lẫn quét toàn dự án (không có "chị" tự xưng thật). Cần diễn đạt lại kèm danh sách file+key.
3. **O52 — cần kiểm tra nguồn.** Ô JP của れいな01 2415 bị hỏng (chứa văn bản VN); TW là dòng khác hẳn. Không sửa được từ JP/TW.
4. **O64 — trích dẫn trong list sai cả hai:** "日々姫04 2668" (JP về Kumakuma, không có "ông nội" trong file) và "Grand 08 2010" (key không tồn tại; không có "ông nội" trong Grand 08 bộ tốt). Dòng thật đã sửa ở đây là 日々姫03 2368/2607. List cần sửa trích dẫn.
5. **O58 — list ghi nhầm file:** 2874 ở 稀咲02_新事業案, không phải 稀咲h3.
6. **O49 — con số 12/18 trong audit không tái hiện được** bằng đếm cơ học trên bộ tốt (29 dòng "tôi" / 12 dòng "mình", trong đó 8 "mình" tự xưng thật). Quyết "tôi" dựa trên đếm cơ học này + lời thoại Olivy ("tôi" 15 vs "mình" 3).
7. **O44 mở rộng:** 1593 + 2337 được sửa thêm ngoài key trích dẫn (1592) — cùng từ 脈, cùng lỗi TW, cùng file; ghi rõ để điều phối viên biết.

**File giao:** `unification-s7-open-misc-wrong.json` (21 mục), `unification-s7-open-misc-REVIEW.md` (file này), `unification-snippet-s7-open-misc.md`.
