# Audit — lr_日々姫真闇h1_三人家族.txt.toml (02_Hibiki)

- **File:** `lr_日々姫真闇h1_三人家族.txt.toml` — route 02_Hibiki, H-scene (Hibiki + Mayami, "gia đình ba người")
- **Tổng số dòng đã đọc:** 436 / 436 (đọc toàn bộ, từng dòng đối chiếu JP + TW, CSV3)
- **Số dòng sai:** **60 / 436 (13,8%)**
- **Phân loại:** đại từ xưng hô 22 · っ thô 21 · số nguyên âm 9 · mất âm 3 · mất gasp cuối dòng 3 · gasp (sweep bỏ sót) 1 · nghĩa 1
- **Lệch hàng / xoay vòng / nhiễm chéo / mồ côi / chưa dịch / trùng key: 0** (chi tiết ở mục Kiểm chứng)

## 1. Kiểm chứng file

- **TOML:** md5 `d8f257e11854179d1a64585836ad9112`, 1 bản duy nhất (không có bản trùng), UTF-8 BOM + CRLF, 900 dòng, 436 key script. `[selections]` rỗng. Nhân vật trong TOML: Soutetsu, Hibiki, Mayami.
- **CSV3:** 1 bộ duy nhất, 436 dòng, 436 key duy nhất, 0 VN trống, 0 key thiếu ở cả hai chiều. VN khớp TOML tuyệt đối sau khi chuẩn hoá `\n` → khoảng trắng (203/436 dòng chỉ khác nhau ở điểm này — CSV3 giữ `\n` thật, TOML-2 đã làm phẳng).
- **Tag `%l`:** không có tag nào trong file (cả JP lẫn VN) — không có gì hỏng.
- **Số dòng theo nhân vật:** độc thoại 184 · 日々姫 (Hibiki) 88 · 真闇 (Mayami) 85 · 双鉄 (Soutetsu) 79. Key từ 36 đến 2484 (thưa).
- **Lệch hàng / xoay vòng:** 0 — đọc toàn bộ 436 dòng, mạch truyện liền mạch, không có chuỗi dịch bị dịch chuyển.
- **Nhiễm chéo:** đối chiếu VN file qua chỉ mục VN toàn dự án — 0 nhiễm thật. Các trùng khớp đều là (a) cùng file tự khớp với chính nó, hoặc (b) cụm SFX ngắn chung (vd. "（Phụt! Phụt! Phụt! Phụtttt!）") lặp lại ở các H-file khác nhau — đó là cách dịch SFX chung, không phải nhiễm.
- **Chưa dịch / mồ côi / trùng key:** 0.

## 2. Đối chiếu sweep (sweep-raw-gasp-wrong.json)

- Sweep có **26 entry** cho file này: **24 entry có fix — đã nhận nguyên văn** sau khi kiểm chứng từng dòng với JP (danh sách ở mục 3).
- **2 entry "already-rendered" (1432, 1723) — đã kiểm chứng, giữ nguyên, không sửa** (xem mục 6).
- **1 gasp sweep bỏ sót, phát hiện khi đọc toàn bộ: key 1579** (っ độc lập giữa dấu gạch, xem mục 5).

## 3. っ thô (raw-tsu) — 21 dòng (sweep, đã nhận nguyên văn)

Tất cả đều là っ bị dịch thành "っ" nguyên xi trong VN. Quy tắc gasp: っ độc lập / cuối dòng / cuối chuỗi ～ → "Ư"; っ gắn với từ âm thanh cũng là gasp; っ gắn với từ nội dung thì KHÔNG phải gasp (vd. 1429 こうっ, 1455 激しっ, 1471 すぎっ, 1518 ちゃんっっ, 1491 ますっ, 2115/2119/2241 động từ+っ — đều đã giữ nguyên, xem mục 6).

### Key 1042 — [日々姫] — raw-tsu

- **JP:** `「――っ」`
- **TW:** `「——」`
- **VN cũ:** `「――っ」`
- **VN mới:** `「――Ư」`
- **Lý do:** っ cuối dòng độc lập, không dấu câu đi kèm → Ư (quy tắc gasp).

### Key 1044 — [双鉄] — raw-tsu

- **JP:** `「――――っ――はぁ――んっ！！」`
- **TW:** `「——呃——蛤啊——嗯！！」`
- **VN cũ:** `「――――っ――Hà――ưm!!」`
- **VN mới:** `「――――Ư――Hà――ưm!!」`
- **Lý do:** っ đầu dòng độc lập → Ư; はぁ→Hà, んっ→ưm giữ nguyên.

### Key 1061 — [真闇] — raw-tsu

- **JP:** `「…………。…………。…………（ごくっ）――。\n……おねぇ……ちゃん、も………………ね？…………っ」`
- **TW:** `「…………（吞口水）。……姐姐……也……好不好？……」`
- **VN cũ:** `「…………。…………。…………（Ực）――。\n……Chị……cũng………………nhé?…………っ」`
- **VN mới:** `「…………。…………。…………（Ực）――。 ……Chị……cũng………………nhé?…………Ư」`
- **Lý do:** っ tuyệt đối cuối dòng → Ư (quy tắc gasp).

### Key 1439 — [日々姫] — raw-tsu

- **JP:** `「ひゅっ！！！？　～～～～～～～～～～っ！！！！」`
- **TW:** `「呀唔！！！？哇～～～～～～！！！！」`
- **VN cũ:** `「Hyu!!!? ~~~~~~~~~~っ!!!!」`
- **VN mới:** `「Hyu!!!? ~~~~~~~~~~Ư!!!!」`
- **Lý do:** ひゅっ → "Hyu" (romaji, quy tắc ひゃ-family); っ cuối chuỗi ～ → Ư.

### Key 1458 — [真闇] — raw-tsu

- **JP:** `「～～～～～～～～っ！！！」`
- **TW:** `「呀～～～～～～～！！！」`
- **VN cũ:** `「~~~~~~~~っ!!!」`
- **VN mới:** `「~~~~~~~~Ư!!!」`
- **Lý do:** っ cuối chuỗi ～ → Ư.

### Key 1508 — [真闇] — raw-tsu

- **JP:** `「っ！？　っ！？　っ！？　っ！！？」`
- **TW:** `「哎！？哎！？哎！？哎！！？」`
- **VN cũ:** `「っ!? っ!? っ!? っ!!?」`
- **VN mới:** `「Ư!? Ư!? Ư!? Ư!!?」`
- **Lý do:** 4× っ độc lập → 4× Ư.

### Key 1525 — [双鉄] — raw-tsu

- **JP:** `「っ！！！！！！！」`
- **TW:** `「唔！！！！！！！」`
- **VN cũ:** `「っ!!!!!!!」`
- **VN mới:** `「Ư!!!!!!!」`
- **Lý do:** っ độc lập → Ư.

### Key 1551 — [日々姫] — raw-tsu

- **JP:** `「っ！　――ぁっ――ひあっ！　あっ――はっ！！」`
- **TW:** `「啊！——啊——呀啊！啊——哈！！」`
- **VN cũ:** `「っ! ――A――hia! A――ha!!」`
- **VN mới:** `「Ư! ――A――hia! A――ha!!」`
- **Lý do:** っ độc lập → Ư; ひあっ → "hia" (romaji, quy tắc ひゃ-family).

### Key 1552 — [真闇] — raw-tsu

- **JP:** `「っ！」`
- **TW:** `「啊！」`
- **VN cũ:** `「っ!」`
- **VN mới:** `「Ư!」`
- **Lý do:** っ độc lập → Ư.

### Key 1553 — [日々姫] — raw-tsu

- **JP:** `「あっ！」\n「っ！！！！！」`
- **TW:** `「啊！」\n「唔！！！！！」`
- **VN cũ:** `「A!」\n「っ!!!!!」`
- **VN mới:** `「A!」\n「Ư!!!!!」`
- **Lý do:** っ độc lập (dòng 2) → Ư.

### Key 1557 — [真闇] — raw-tsu

- **JP:** `「っ！　～～～～～………………。\n…………………………………………………はいっ！！！」`
- **TW:** `「啊！唔～～～～～………我願意！！！」`
- **VN cũ:** `「っ! ~~~~~……………….\n…………………………………………………Vâng!!!」`
- **VN mới:** `「Ư! ~~~~~………………. …………………………………………………Vâng!!!」`
- **Lý do:** っ độc lập → Ư.

### Key 1561 — [双鉄] — raw-tsu

- **JP:** `「っ！！」`
- **TW:** `「啊！！」`
- **VN cũ:** `「っ!!」`
- **VN mới:** `「Ư!!」`
- **Lý do:** っ độc lập → Ư (2 dấu ! giữ nguyên).

### Key 1562 — [双鉄] — raw-tsu

- **JP:** `「っ！！！」`
- **TW:** `「啊！！！」`
- **VN cũ:** `「っ!!!」`
- **VN mới:** `「Ư!!!」`
- **Lý do:** っ độc lập → Ư (3 dấu ! giữ nguyên).

### Key 1563 — [双鉄] — raw-tsu

- **JP:** `「っ！！！！」`
- **TW:** `「啊！！！！」`
- **VN cũ:** `「っ!!!!」`
- **VN mới:** `「Ư!!!!」`
- **Lý do:** っ độc lập → Ư (4 dấu ! giữ nguyên).

### Key 1564 — [双鉄] — raw-tsu

- **JP:** `「っ！！！！！」`
- **TW:** `「啊！！！！！」`
- **VN cũ:** `「っ!!!!!」`
- **VN mới:** `「Ư!!!!!」`
- **Lý do:** っ độc lập → Ư (5 dấu ! giữ nguyên).

### Key 1565 — [双鉄] — raw-tsu

- **JP:** `「っ！！！！！！！！！」`
- **TW:** `「啊！！！！！！！！！」`
- **VN cũ:** `「っ!!!!!!!!!」`
- **VN mới:** `「Ư!!!!!!!!!」`
- **Lý do:** っ độc lập → Ư (9 dấu ! giữ nguyên).

### Key 1566 — [双鉄] — raw-tsu

- **JP:** `「っ！！！！？」`
- **TW:** `「啊！！！！？」`
- **VN cũ:** `「っ!!!!?」`
- **VN mới:** `「Ư!!!!?」`
- **Lý do:** っ độc lập → Ư (4 dấu ! + ? giữ nguyên).

### Key 1571 — [真闇] — raw-tsu

- **JP:** `「～～～～～～～～～～～～～～～っ！！！！！」`
- **TW:** `「啊～～～～～～～～！！！！！」`
- **VN cũ:** `「~~~~~~~~~~~~~~~っ!!!!!」`
- **VN mới:** `「~~~~~~~~~~~~~~~Ư!!!!!」`
- **Lý do:** っ cuối chuỗi ～ → Ư.

### Key 1608 — [双鉄] — raw-tsu

- **JP:** `「ぷあっ！　あっ――。っっ！！！！」`
- **TW:** `「噗啊！啊——哎！！！！」`
- **VN cũ:** `「Pua! A――. っっ!!!!」`
- **VN mới:** `「Pua! A――. ƯƯ!!!!」`
- **Lý do:** っっ → ƯƯ (hai gasp liên tiếp).

### Key 1712 — [日々姫] — raw-tsu

- **JP:** `「私っ！　私は望んどると！　……っ。――――ん！！」`
- **TW:** `「我！我想要那樣做！————嗯！！」`
- **VN cũ:** `「Em! Em khao khát điều đó! ……っ. ――――Ưm!!」`
- **VN mới:** `「Em! Em khao khát điều đó! ……Ư. ――――Ưm!!」`
- **Lý do:** っ độc lập → Ư.

### Key 1736 — [双鉄] — raw-tsu

- **JP:** `「日々姫！　日々姫！　もう少し――だからっ！　っ！\nちゃんと――日々姫の――子宮に――全部っ！　精液を」`
- **TW:** `「日日姬！日日姬！馬上——就好了！呃！我會吧——日日姬的——子宮——全部灌滿精液的！」`
- **VN cũ:** `「Hibiki! Hibiki! Một chút nữa thôi――vì vậy! っ!\nAnh sẽ――rót toàn bộ――tinh dịch――vào tử cung của Hibiki!」`
- **VN mới:** `「Hibiki! Hibiki! Một chút nữa thôi――vì vậy! Ư! Anh sẽ――rót toàn bộ――tinh dịch――vào tử cung của Hibiki!」`
- **Lý do:** っ độc lập → Ư. "Anh sẽ" giữ nguyên — nói với Hibiki.

## 4. Đại từ xưng hô Soutetsu — 22 dòng

Quy tắc đã sửa (20/11): Soutetsu tự xưng "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi; "tôi" với Hachiroku/Mayami/Minokasa/Kisaki. Độc thoại [双鉄] không có 「」 là giọng kể chuyện → "tôi" (tiền lệ ふかみh2, ハチロク14). Xưng hô với CẢ HAI → "tôi" (tiền lệ Paulette 14 key 1544). Mỗi fix dưới đây đều đã xác minh người nghe từ các dòng kề cận.

### Key 1080 — [双鉄] — pronoun

- **JP:** `「……日々姫がこの水着を選んだ意味を。真闇姉が驚き\n戸惑いつつも着替えてくれた理由を、僕は、理解した」`
- **TW:** `「……日日姬故意選這種泳裝的意義，以及真闇姐雖然又驚又疑，但還是穿上它的理由，我都明白了」`
- **VN cũ:** `「……Ý nghĩa của việc Hibiki chọn bộ đồ bơi này. Lý do chị Mayami ngạc nhiên\nvà bối rối nhưng vẫn thay đồ, em đã hiểu rồi.」`
- **VN mới:** `「……Ý nghĩa của việc Hibiki chọn bộ đồ bơi này. Lý do chị Mayami ngạc nhiên\nvà bối rối nhưng vẫn thay đồ, tôi đã hiểu rồi.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "tôi" (tiền lệ ふかみh2, ハチロク14).

### Key 1414 — [双鉄] — pronoun

- **JP:** `「胸だけで。手コキやお口の助けを借りずおっぱいだけで。\n僕は未だ、一度も射精にいたれたことがない。ゆえに」`
- **TW:** `「光靠胸部，不借助手或者口交，只用胸部。我至今還從來沒有那樣射出來過。所以」`
- **VN cũ:** `「Chỉ bằng ngực. Không nhờ đến sự trợ giúp của tay hay miệng, chỉ bằng ngực thôi.\nAnh vẫn chưa, một lần nào có thể xuất tinh được. Vì vậy.」`
- **VN mới:** `「Chỉ bằng ngực. Không nhờ đến sự trợ giúp của tay hay miệng, chỉ bằng ngực thôi.\nTôi vẫn chưa, một lần nào có thể xuất tinh được. Vì vậy.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "Tôi" (tiền lệ ふかみh2, ハチロク14).

### Key 1420 — [双鉄] — pronoun

- **JP:** `「日々姫の指に、僕の言葉に興奮してくれてるのだろう。\n小さく控えめな膣口からは、愛液が溢れ出してきている」`
- **TW:** `「可能是被日日姬的手指和我的話語挑起了情慾。真闇姐小巧的穴口已經開始冒出愛液了」`
- **VN cũ:** `「Chắc là đang hưng phấn vì ngón tay của Hibiki, và lời nói của em. \nTừ cửa mình nhỏ nhắn e ấp, dâm thủy đang tràn ra.」`
- **VN mới:** `「Chắc là đang hưng phấn vì ngón tay của Hibiki, và lời nói của tôi. \nTừ cửa mình nhỏ nhắn e ấp, dâm thủy đang tràn ra.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "tôi".

### Key 1668 — [双鉄] — pronoun

- **JP:** `「引き受けた」`
- **TW:** `「得令」`
- **VN cũ:** `「Em nhận lời.」`
- **VN mới:** `「Tôi nhận lời.」`
- **Lý do:** Đối thoại với Mayami (nhận lời nhờ của Mayami, dòng 1659–1662) → "tôi".

### Key 1679 — [双鉄] — pronoun

- **JP:** `「僕は――僕は――僕は、僕はっ！！！！」`
- **TW:** `「我——我——我，我！！！！」`
- **VN cũ:** `「Em――em――em, em!!!!」`
- **VN mới:** `「Tôi――tôi――tôi, tôi!!!!」`
- **Lý do:** Đối thoại với Mayami (trả lời Mayami 1677) → "tôi".

### Key 1681 — [双鉄] — pronoun

- **JP:** `「僕は……ふたりの――\nふたりのおまんこを、並べて眺めて、見比べたい」`
- **TW:** `「我……想要把兩人的——把兩個小穴排在一起細細評判比對一番」`
- **VN cũ:** `「Em…… muốn ngắm nhìn――\nngắm nhìn hai cái bướm đặt cạnh nhau, và so sánh.」`
- **VN mới:** `「Tôi…… muốn ngắm nhìn――\nngắm nhìn hai cái bướm đặt cạnh nhau, và so sánh.」`
- **Lý do:** Đối thoại với CẢ HAI ("ふたりの") → "tôi" (tiền lệ Paulette 14 key 1544, xưng hô nhóm).

### Key 1683 — [双鉄] — pronoun

- **JP:** `「僕はっずっと、この欲望をっ、絶対の禁忌と考えていた。\n日々姫と結ばれてからはもちろん、その以前からずっと」`
- **TW:** `「我一直都把這份欲望視為絕對的禁忌。不論是在跟日日姬結合之前還是之後」`
- **VN cũ:** `「Em đã luôn, coi dục vọng này, là điều tuyệt đối cấm kỵ.\nTừ sau khi kết đôi với Hibiki thì đương nhiên rồi, nhưng ngay cả trước đó cũng vậy.」`
- **VN mới:** `「Tôi đã luôn, coi dục vọng này, là điều tuyệt đối cấm kỵ.\nTừ sau khi kết đôi với Hibiki thì đương nhiên rồi, nhưng ngay cả trước đó cũng vậy.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "Tôi".

### Key 1694 — [双鉄] — pronoun

- **JP:** `「僕と、日々姫は――いくつものいくつもの昼と夜、\nこころを、時間を、肌を重ねて――絆を、深めて、きた」`
- **TW:** `「我和日日姬——兩人的內心、時間、肉體——在無數個日日夜夜裡不斷加深彼此的牽絆」`
- **VN cũ:** `「Anh và, Hibiki――đã trải qua biết bao ngày đêm,\ncùng nhau chia sẻ tâm hồn, thời gian, thể xác――để thắt chặt, mối quan hệ.」`
- **VN mới:** `「Tôi và, Hibiki――đã trải qua biết bao ngày đêm,\ncùng nhau chia sẻ tâm hồn, thời gian, thể xác――để thắt chặt, mối quan hệ.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "Tôi".

### Key 1700 — [双鉄] — pronoun

- **JP:** `「セックス、したい、日々姫とも、真闇姉とも、物凄く。\n今すぐにでも挿入したい、けれど、けれども。その前に」`
- **TW:** `「我想，做愛，非常想。無論是和日日姬還是真闇姐。我甚至想現在就插入，可是，在此之前」`
- **VN cũ:** `「Anh muốn, làm tình, với cả Hibiki, và cả chị Mayami, vô cùng muốn.\nAnh muốn đưa vào ngay lập tức, nhưng, nhưng mà. Trước đó.」`
- **VN mới:** `「Tôi muốn, làm tình, với cả Hibiki, và cả chị Mayami, vô cùng muốn.\nTôi muốn đưa vào ngay lập tức, nhưng, nhưng mà. Trước đó.」`
- **Lý do:** Đối thoại với CẢ HAI ("日々姫とも、真闇姉とも") → "Tôi" ×2 (xưng hô nhóm).

### Key 1702 — [双鉄] — pronoun

- **JP:** `「日々姫と並んで、僕の妻となってほしい。\n日々姫と僕ともう一度――三人家族に、なってほしい」`
- **TW:** `「我懇請你能跟日日姬一起，成為我的妻子。懇請你能跟日日姬和我——重新組成三人的家庭」`
- **VN cũ:** `「Cùng với Hibiki, em muốn chị trở thành vợ em.\nCùng với Hibiki và em một lần nữa――trở thành một gia đình ba người.」`
- **VN mới:** `「Cùng với Hibiki, tôi muốn chị trở thành vợ tôi.\nCùng với Hibiki và tôi một lần nữa――trở thành một gia đình ba người.」`
- **Lý do:** Đối thoại với Mayami (cầu hôn Mayami) → "tôi" ×3 ("vợ em"→"vợ tôi").

### Key 1703 — [双鉄] — pronoun

- **JP:** `「決して望んではいけないことと、こころに蓋をしていた。\nけれど、もし、三人ともが同じ望みをもっているのなら」`
- **TW:** `「我把它封印在內心深處，認為那是絕對不可貪圖之物。但如果我們三人都有同樣的願望的話」`
- **VN cũ:** `「Anh đã đóng chặt trái tim mình, coi đó là điều tuyệt đối không được khao khát.\nNhưng, nếu như, cả ba chúng ta đều có chung một ước muốn.」`
- **VN mới:** `「Tôi đã đóng chặt trái tim mình, coi đó là điều tuyệt đối không được khao khát.\nNhưng, nếu như, cả ba chúng ta đều có chung một ước muốn.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "Tôi".

### Key 1706 — [双鉄] — pronoun

- **JP:** `「絶対の禁忌とこころを閉ざしていたのは、つまりっ――\n僕が、それだけ、強く望んでしまっていた、から、で」`
- **TW:** `「我把它當成絕對的禁忌封存在內心深處，這也意味著——我對它有多麼強烈的渴望」`
- **VN cũ:** `「Việc em đóng chặt trái tim và coi đó là điều cấm kỵ tuyệt đối, có nghĩa là――\nBởi vì, em đã, khao khát nó, quá mãnh liệt.」`
- **VN mới:** `「Việc tôi đóng chặt trái tim và coi đó là điều cấm kỵ tuyệt đối, có nghĩa là――\nBởi vì, tôi đã, khao khát nó, quá mãnh liệt.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "tôi" ×2.

### Key 1709 — [双鉄] — pronoun

- **JP:** `「わかっている――がっ――止めら――れんっ！！！」`
- **TW:** `「我知道——可是——我——停不下來了！！！」`
- **VN cũ:** `「Em biết――nhưng――không thể――dừng lại được!!!」`
- **VN mới:** `「Anh biết――nhưng――không thể――dừng lại được!!!」`
- **Lý do:** Đối thoại với Hibiki (trả lời Hibiki 1707) → "anh".

### Key 1714 — [双鉄] — pronoun

- **JP:** `「僕は、ふたりをっ、妊娠、させるっ――絶対、必ず、\n日々姫も――真闇――姉にも――僕の、こどもをっ――」`
- **TW:** `「我，會讓你們倆，懷孕——一定會無論是日日姬——還是真闇姐——都會懷上，我的孩子——」`
- **VN cũ:** `「Anh sẽ, làm cho cả hai, mang thai――tuyệt đối, chắc chắn,\ncả Hibiki――cả chị――Mayami――những đứa con, của anh――」`
- **VN mới:** `「Tôi sẽ, làm cho cả hai, mang thai――tuyệt đối, chắc chắn,\ncả Hibiki――cả chị――Mayami――những đứa con, của tôi――」`
- **Lý do:** Đối thoại với CẢ HAI → "Tôi sẽ" + "của tôi" (xưng hô nhóm).

### Key 1738 — [双鉄] — pronoun

- **JP:** `「日々姫っ！　真闇姉っ！\n僕はっ――！　僕は――僕はもうっ！！！」`
- **TW:** `「日日姬！真闇姐！我——！我——我已經！！！」`
- **VN cũ:** `「Hibiki! Chị Mayami!\nEm――! Em――em sắp!!!」`
- **VN mới:** `「Hibiki! Chị Mayami!\nTôi――! Tôi――tôi sắp!!!」`
- **Lý do:** Đối thoại với CẢ HAI ("日々姫っ！　真闇姉っ！") → "Tôi" ×3.

### Key 1743 — [双鉄] — pronoun

- **JP:** `「日々姫、真闇姉！　キス、キスしたい。三人で。\nふたりで舌を――舌を伸ばして、くっつけあってほしい」`
- **TW:** `「日日姬，真闇姐！我想要三個人一起接吻。請你們把舌頭——把舌頭伸出來，然後舌頭貼著舌頭」`
- **VN cũ:** `「Hibiki, chị Mayami! Hôn, em muốn hôn. Cả ba người.\nHai người hãy thò lưỡi ra――chạm lưỡi vào nhau đi.」`
- **VN mới:** `「Hibiki, chị Mayami! Hôn, tôi muốn hôn. Cả ba người.\nHai người hãy thò lưỡi ra――chạm lưỡi vào nhau đi.」`
- **Lý do:** Đối thoại với CẢ HAI ("三人で") → "tôi" ("tôi muốn hôn").

### Key 1758 — [双鉄] — pronoun

- **JP:** `「この先例えば何かがあって、日々姫が僕を嫌うとしても\n憎むとしても――僕は、日々姫を愛し続ける。絶対に」`
- **TW:** `「無論今後發生什麼事，哪怕日日姬討厭我，憎恨我——我也絕對會一直深愛著她」`
- **VN cũ:** `「Ví dụ như sau này có chuyện gì xảy ra, dù Hibiki có ghét anh,\ncó hận anh đi chăng nữa――anh vẫn sẽ tiếp tục yêu Hibiki. Tuyệt đối là vậy.」`
- **VN mới:** `「Ví dụ như sau này có chuyện gì xảy ra, dù Hibiki có ghét tôi,\ncó hận tôi đi chăng nữa――tôi vẫn sẽ tiếp tục yêu Hibiki. Tuyệt đối là vậy.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "tôi" ×3.

### Key 1770 — [双鉄] — pronoun

- **JP:** `「真闇姉。今度は、こっちを手伝ってくれ」`
- **TW:** `「真闇姐。這次來這邊弄」`
- **VN cũ:** `「Chị Mayami. Lần này, hãy giúp em bên này.」`
- **VN mới:** `「Chị Mayami. Lần này, hãy giúp tôi bên này.」`
- **Lý do:** Đối thoại với Mayami ("真闇姉") → "tôi".

### Key 1773 — [双鉄] — pronoun

- **JP:** `「僕は、[めと]娶ろう。真闇姉をも。日々姫の隣に。\nそうして、三人で夫婦になって、家族になろう」`
- **TW:** `「真闇姐也成為我的妻子吧。跟日日姬一起。然後三個人結為夫婦，組建家庭」`
- **VN cũ:** `「Em sẽ, cưới. Cả chị Mayami nữa. Bên cạnh Hibiki.\nRồi, ba chúng ta sẽ trở thành vợ chồng, trở thành gia đình.」`
- **VN mới:** `「Tôi sẽ, cưới. Cả chị Mayami nữa. Bên cạnh Hibiki.\nRồi, ba chúng ta sẽ trở thành vợ chồng, trở thành gia đình.」`
- **Lý do:** Đối thoại với Mayami (cưới Mayami) → "Tôi sẽ, cưới".

### Key 1775 — [双鉄] — pronoun

- **JP:** `「僕の勃起を、僕の精子を、子宮の中に欲しがって。\n導こうとして必死になって、おねだりをしてくれている」`
- **TW:** `「真闇姐的子宮在渴求我的硬物和精子。它正在拚命央求著，想邀請我進入其中」`
- **VN cũ:** `「Đang khao khát phần cương cứng của em, tinh trùng của em vào trong tử cung.\nĐang tuyệt vọng cố gắng dẫn dắt, đang cầu xin em.」`
- **VN mới:** `「Đang khao khát phần cương cứng của tôi, tinh trùng của tôi vào trong tử cung.\nĐang tuyệt vọng cố gắng dẫn dắt, đang cầu xin tôi.」`
- **Lý do:** Độc thoại [双鉄] không có 「」 — giọng kể chuyện, dùng "tôi" ×3.

### Key 1791 — [双鉄] — pronoun

- **JP:** `「隠さないで欲しい！　真闇姉の、日々姫の――\n大切な[あね,1]義姉と[いもうと,1]義妹のおまんこを、僕は並べて見てみたい」`
- **TW:** `「請不要遮掩！我想讓真闇姐和日日姬的——我想讓我心愛的繼姐繼妹的小穴並排呈現在眼前」`
- **VN cũ:** `「Đừng giấu! Của chị Mayami, của Hibiki――\nEm muốn nhìn thấy bướm của chị gái nuôi và em gái nuôi quan trọng của em đặt cạnh nhau.」`
- **VN mới:** `「Đừng giấu! Của chị Mayami, của Hibiki――\nTôi muốn nhìn thấy bướm của chị gái nuôi và em gái quan trọng của tôi đặt cạnh nhau.」`
- **Lý do:** Đối thoại với CẢ HAI → "Tôi" + "của tôi" (xưng hô nhóm). Đồng thời thuật ngữ: 義妹 "em gái nuôi" → "em gái" — file dịch 義妹 là "cô em gái" ở 2003, 2005, 2082; chỉ 1791 dùng "nuôi" (xem Cờ cho Hieu về 義姉/義妹).

### Key 1812 — [双鉄] — pronoun

- **JP:** `「僕ら――三人でのセックスを。日々姫をはじめて\n抱いたときから――セックスを知った時から、僕は」`
- **TW:** `「關於我們——三人一起的做愛，我在第一次跟日日姬上床時——在初嘗禁果時，我就」`
- **VN cũ:** `「Chuyện làm tình――giữa ba chúng ta. Từ lần đầu tiên ôm Hibiki\n――từ khi biết đến tình dục, anh đã」`
- **VN mới:** `「Chuyện làm tình――giữa ba chúng ta. Từ lần đầu tiên ôm Hibiki\n――từ khi biết đến tình dục, tôi đã」`
- **Lý do:** Đối thoại với CẢ HAI ("僕ら――三人で") → "tôi" (xưng hô nhóm; dòng bị cắt, nói về "threesome" của ba người).

## 5. Gasp bị mất / sweep bỏ sót — 4 dòng

### Key 1496 — [真闇] — lost-gasp-trailing

- **JP:** `「は……ぁ……そう、ちゃん――ひー、ちゃんっ――っ」`
- **TW:** `「哈……啊……小雙——小、日——」`
- **VN cũ:** `「Hà…… a…… Sou, chan――Hii, chan――」`
- **VN mới:** `「Hà…… a…… Sou, chan――Hii, chan――Ư」`
- **Lý do:** っ tuyệt đối cuối dòng → Ư (quy tắc gasp; sweep bỏ sót vì っ nằm sau ちゃんっ――).

### Key 1530 — [日々姫] — lost-gasp-trailing

- **JP:** `「あ――ん……ぇ～～～～～～～っ」`
- **TW:** `「啊——嗯……哎～～～～」`
- **VN cũ:** `「A――ưm…… e~~~~~~~」`
- **VN mới:** `「A――ưm…… e~~~~~~~Ư」`
- **Lý do:** っ tuyệt đối cuối dòng → Ư (quy tắc gasp).

### Key 1555 — [日々姫] — lost-gasp-trailing

- **JP:** `「あっ！　ふあっ！　あっ！！！　んウゥゥぅ～っ！！」`
- **TW:** `「啊！呼啊！啊！！！嗯唔唔唔唔～！！」`
- **VN cũ:** `「A! Fua! A!!! Nguuuuu~!!」`
- **VN mới:** `「A! Fua! A!!! Nguuuuu~Ư!!」`
- **Lý do:** っ cuối dòng → Ư. "Nguuuuu" (5 u) giữ theo sweep (đọc ～ kéo dài = 5 u, khớp JP んウゥゥぅ～).

### Key 1579 — [真闇] — gasp

- **JP:** `「ん……『あーーーーーーーん』　あむっ――っ――\nちゅるっ――れるっ――れるっ――ちゅぶっ――れりゅ」`
- **TW:** `「嗯……“啊————嗯”啊嗯——唔——啾嚕——滋溜——滋溜——啾噗——滋溜」`
- **VN cũ:** `「Ưm…… 'Aaaaaan' Amu――ưm――\nChụt――rê ru――rê ru――chùn chụt――rê ryu」`
- **VN mới:** `「Ưm…… 'Aaaaaaaan' Amu――Ư――\nChụt――rê ru――rê ru――chùn chụt――rê ryu」`
- **Lý do:** っ độc lập giữa dấu gạch (あむっ――っ――) bị dịch mất → Ư (sweep bỏ sót; quy tắc như 1044). Đồng thời số nguyên âm: 『あーーーーーーーん』 = 8 a → VN cũ 6 a, fix 'Aaaaaaaan' (8 a).

## 6. Số nguyên âm (vowel-count) — 9 dòng

Chuẩn áp dụng: mora-matching (số nguyên âm VN = số âm tiết nguyên âm JP); chỉ sửa u-run khi cả công thức (1 + số う/ぅ) VÀ mora-matching đều đồng ý. Tất cả số đếm đã kiểm bằng script (đếm bằng mắt đã sai ở vài chỗ — tin số script). Key 1579 cũng có sửa số nguyên âm (8 a), xem mục 5.

### Key 1440 — [真闇] — vowel-count

- **JP:** `「ひゅあああああああああああああああああああんっ！」`
- **TW:** `「呀啊啊啊啊啊啊啊啊！」`
- **VN cũ:** `「Hyuaaaaaaaaaaaaaaaaaaaaaaan!」`
- **VN mới:** `「Hyuaaaaaaaaaaaaaaaaaaan!」`
- **Lý do:** Số nguyên âm: JP có 19 a (ひゅ+あ×18+んっ) → VN cũ 23 a. Fix về 19 a ("Hyu"+a×19+"n!").

### Key 1441 — [日々姫] — vowel-count

- **JP:** `「ひゃあああああっ！？　ふ！　ひゃっ！？　ん――\nふあっ！　あっ！　あああああっ！　らめっ、なのっ」`
- **TW:** `「呀啊啊啊啊啊！？呼！呀！？嗯——呼啊！啊！啊啊啊啊啊！我不行了」`
- **VN cũ:** `「Hyaaaaa!? Fu! Hya!? Ưm――\nFua! A! Aaaaa! Không được, đâu.」`
- **VN mới:** `「Hyaaaaaa!? Fu! Hya!? Ưm――\nFua! A! Aaaaa! Không được, đâu.」`
- **Lý do:** Token đầu ひゃ+あ×5 = 6 a → VN cũ 5 a. Fix "Hyaaaaaa" (6 a).

### Key 1446 — [日々姫] — vowel-count

- **JP:** `「きゅぅぅぅぅぅぅぅぅぅぅぅぅぅぅうううううん！！」`
- **TW:** `「呀嗚嗚嗚嗚嗚嗚嗚嗚！！」`
- **VN cũ:** `「Kyuuuuuuuuuuuuuuuuun!!」`
- **VN mới:** `「Kyuuuuuuuuuuuuuuuuuuuun!!」`
- **Lý do:** Số nguyên âm: JP có 20 u (きゅ+ぅ×14+う×5) → VN cũ 17 u. Fix về 20 u ("Ky"+u×20+"n!!").

### Key 1467 — [真闇] — vowel-count

- **JP:** `「ふやぁぁぁっ！？　ひ、ひーちゃっ――あっ！！！？」`
- **TW:** `「呼呀啊啊啊！？小、小日——啊！！！？」`
- **VN cũ:** `「Fuyaaa!? H-Hii-chan――a!!!?」`
- **VN mới:** `「Fuyaaaa!? H-Hii-chan――a!!!?」`
- **Lý do:** Token ふや+ぁ×3 = 4 a → VN cũ 3 a. Fix "Fuyaaaa" (4 a).

### Key 1477 — [真闇] — vowel-count

- **JP:** `「ふぁぁぁぁぁぁぁぁぁぁぁっぁぁぁあああああっ！！」`
- **TW:** `「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」`
- **VN cũ:** `「Fuaaaaaaaaaaaaaaa!!!!」`
- **VN mới:** `「Fuaaaaaaaaaaaaaaaaaaa!!!!」`
- **Lý do:** Số nguyên âm: JP có 19 a → VN cũ 15 a. Fix về 19 a ("Fu"+a×19+"!!!!").

### Key 1478 — [日々姫] — vowel-count

- **JP:** `「ふあぁぁぁっぁぁぁぁぁぁぁぁぁぁぁぁぁぁん！！！」`
- **TW:** `「呼啊啊啊啊啊啊啊啊啊啊！！！」`
- **VN cũ:** `「Fuaaaaaaaaaaaaaaaaaaaaaaan!!!」`
- **VN mới:** `「Fuaaaaaaaaaaaaaaaaaan!!!」`
- **Lý do:** Số nguyên âm: JP có 18 a → VN cũ 23 a. Fix về 18 a ("Fu"+a×18+"n!!!").

### Key 1479 — [双鉄] — vowel-count

- **JP:** `「ふぁぁぁぁぁぁぁぁぁっぁぁぁぁあっっ！！！！？」`
- **TW:** `「呼啊啊啊啊啊啊啊啊啊啊！！！！？」`
- **VN cũ:** `「Fuaaaaaaaaaaaaaaaaa!!!!?」`
- **VN mới:** `「Fuaaaaaaaaaaaaaa!!!!?」`
- **Lý do:** Số nguyên âm: JP có 14 a → VN cũ 17 a. Fix về 14 a ("Fu"+a×14+"!!!!?").

### Key 1611 — [双鉄] — vowel-count

- **JP:** `「ぉぉぉぉぉぉおぉぉぉっっ！！！」`
- **TW:** `「噢噢噢噢噢噢噢噢！！！」`
- **VN cũ:** `「Ooooooooooooooo!!!」`
- **VN mới:** `「Oooooooooo!!!」`
- **Lý do:** Số nguyên âm: JP có 10 o (ぉ×6+お×4) → VN cũ 15 o. Fix về 10 o ("O"+o×9+"!!!").

### Key 1619 — [日々姫] — vowel-count

- **JP:** `「はぁい。ねぇね。あ、喉、絡むから気をつけてね？\nん……『あーーーーーーん』」`
- **TW:** `「好了，阿姐。啊，會有些黏喉嚨，要注意一點哦？嗯……“啊————嗯”」`
- **VN cũ:** `「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\nƯm…… 'Aaaaaan'」`
- **VN mới:** `「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\nƯm…… 'Aaaaaaaan'」`
- **Lý do:** Số nguyên âm: 『あーーーーーーーん』 = 8 a → VN cũ 6 a, fix 'Aaaaaaaan' (8 a).

## 7. Mất âm / nghĩa — 4 dòng

### Key 1390 — [双鉄] — lost-sound

- **JP:** `「真闇姉、の――力も――必要、だっ――くっ！　僕らは\n――三人で――セックスをして――家族に、なる、ゆえ」`
- **TW:** `「也需要——真闇姐的，幫助——呃！因為我們——要三個人——一起做愛——一起成為，家人」`
- **VN cũ:** `「Sức mạnh――của chị Mayami――cũng cần thiết――ư! Chúng ta\n――sẽ làm tình――cả ba người――và trở thành, một gia đình.」`
- **VN mới:** `「Sức mạnh――của chị Mayami――cũng cần thiết――ku! Chúng ta\n――sẽ làm tình――cả ba người――và trở thành, một gia đình.」`
- **Lý do:** くっ → "ku": phụ âm k bị mất khi dịch thành "ư" (xem 1513/1615).

### Key 1513 — [双鉄] — lost-sound

- **JP:** `「くっ――あっ！　あっ！　あっ！！！」`
- **TW:** `「唔——啊！啊！啊！！！」`
- **VN cũ:** `「Ư――a! A! A!!!」`
- **VN mới:** `「Ku――a! A! A!!!」`
- **Lý do:** くっ → "Ku": phụ âm k bị mất (chuẩn trong file: くっ → "Ku" ở 1464–1466, 2360, 2426).

### Key 1615 — [日々姫] — lost-sound

- **JP:** `「だっ、て――んっ――ばってん、私の、おっぱい、じゃ\n……くっ――やっぱり――ちょこっと――無理、やけん」`
- **TW:** `「因為——嗯——因為靠我的，胸部……咕——還是——有點——勉強」`
- **VN cũ:** `「Bởi, vì――ưm――nhưng mà, ngực của em, thì\n……ư――quả nhiên――vẫn hơi――quá sức.」`
- **VN mới:** `「Bởi, vì――ưm――nhưng mà, ngực của em, thì\n……ku――quả nhiên――vẫn hơi――quá sức.」`
- **Lý do:** くっ → "ku": phụ âm k bị mất (xem 1513).

### Key 1691 — [日々姫] — meaning

- **JP:** `「わたしもっ、わたしもおんなじ――気持ち――\nやけんっ！　んっ！　やけん、ね？」`
- **TW:** `「我也，我也是——一樣的心情——可是！嗯！可是呢」`
- **VN cũ:** `「Em cũng, em cũng có cùng――cảm giác――\nNhưng mà! Ưm! Nhưng mà, này?」`
- **VN mới:** `「Em cũng, em cũng có cùng――cảm giác――\nNên là! Ưm! Nên là, này?」`
- **Lý do:** やけん = だから ("vì thế/nên"), không phải "nhưng mà". TW dịch "可是" là lỗi TW, JP thắng. File dịch やけん là "Nên/Cho nên" ở 1072, 1684, 1715, 1718.

## 8. Các dòng đã đọc kỹ và GIỮ NGUYÊN (có lý do)

### 8.1. Gasp ngắn trần — giữ, không thêm Ư (quy ước dự án)

- **1547** — JP 「あっ」 → VN "A". Gasp ngắn trần, không có dấu gạch dẫn → giữ "A" (tiền lệ ROUTE-AUDIT 3199, 3476 qua audit-chukuni06). Đối chiếu: lr_hachirokuh2 1105 「――あっ」 → "――AƯ" có dấu gạch dẫn nên khác.
- **1494** — JP 「わっ」 → VN "Wa". Cùng quy ước.

### 8.2. Số nguyên âm — giữ (đã đếm bằng script)

- **1432** — JP 6 u, VN 6 u (mora-match đúng; công thức sẽ cho 7 — hai chuẩn mâu thuẫn nhau, VN khớp một chuẩn nên giữ; cũng là entry "already-rendered" của sweep).
- **1555** — "Nguuuuu" (5 u) giữ theo sweep (đọc ～ kéo dài = 5 u, khớp JP んウゥゥぅ～).
- **1583** — JP 8 u, VN 8 u (mora-match đúng).
- **1757** — JP thực tế là ちゅううっ = 3 u, VN "chuuu" = 3 u (đếm bằng mắt lúc đầu tưởng ちゅううううっ — sai; số script đúng).
- **1434** — 4 = 4, khớp. **1443** — ひゃ+あ×3 = 4 a, VN 4 a, khớp. **1550** "A a a a a a" (6 a) ✓; **1559** "Aa" ✓; **1436** "Yaan"/"aaaa" ✓; **1522** kiss-SFX romaji ✓ (れるううっ→"reruuu" 3 u, じゅううっ→"juuu" 3 u).

### 8.3. っ gắn từ nội dung — không phải gasp, giữ

- **1429** こうっ, **1455** 激しっ, **1471** すぎっ, **1518** ちゃんっっ, **1491** ますっ, **2115/2119/2241** động từ+っ — っ gắn với từ có nội dung, không phải gasp.

### 8.4. Khác

- **1493** — Mayami gọi Soutetsu là "em" ("Chị cũng muốn em nhìn…") — GIỮ. Đây là chị gọi em trai (Mayami lớn hơn Soutetsu), không thuộc quy tắc tự xưng của Soutetsu.
- **1491** — TW dịch sai お嫁さん thành 當媽媽 (mẹ); VN dịch đúng theo JP là "cô dâu". Không sửa.
- **1741** — VN thêm "chọn" ("chọn bộ đồ bơi") — đã được 1080 trong file xác lập, không phải bịa.
- **2123** — がっ → "Nhưng!" giữ (đọc が, TW đồng ý).
- **1801** — くっ、てっ → "lắm" giữ (dịch lỏng nhưng trong biên độ dịch).
- **1592/1594/1595/1603** — Hibiki うん → "Vâng" giữ (biến thể đăng ký, không phải lỗi).
- **1447** — に đầu dòng → "A" (nói lắp) giữ.
- **36 + 2344–2484** — SFX onomatopoeia dịch thành từ mô tả tiếng Việt ("Trơn tuột", "Phập", "Cộc", "Co thắt") — lựa chọn ngẫu hứng nhất quán trong file, giữ.
- **1627, 1689, 1736** — "anh" nói với Hibiki, đúng, giữ.
- **1616, 1625, 1633, 1641, 1645, 1647, 1684, 1686, 1692, 1696, 1698, 1715, 1718, 1719, 1723** (sweep already-rendered), **1802, 1804, 1805, 1810, 1811, 1814–1826, 1858+** các dòng độc thoại "tôi" — đã đọc, đúng, giữ.

## 9. Cờ cho Hieu (không tự quyết)

1. **義姉 / 義妹 có nên dịch "nuôi" không?** File dịch 義姉 → "chị gái nuôi" 4× (1791, 2003, 2005, 2082) và 義妹 → "cô em gái" 3× (2003, 2005, 2082), chỉ 1791 dùng "em gái nuôi" (đã sửa thành "em gái" cho nhất quán nội bộ). TW nói 繼姐/繼妹 (chị/em kế), KHÔNG phải 養 (nuôi). Câu hỏi lớn hơn — 義 có nên là "nuôi" không — vẫn đang chờ Hieu (xem câu hỏi 1906/2325 ở file khác, và tiền lệ ハチロク14 3777 "chị chồng/em chồng" cũng đang chờ xác nhận). Không quyết trong unification nếu chưa có ý Hieu.
2. **Chuẩn hoá nghiêm số nguyên âm a-run?** 9 dòng mục 6 sửa theo mora-matching (lệch tới ±5). Câu hỏi mikuro đang chờ Hieu ("có chuẩn hoá nghiêm không") vẫn mở — các fix này giả định là có, theo tiền lệ ふかみh2 (±1).
3. **1493** — Mayami gọi Soutetsu "em": giữ như hiện tại; nếu Hieu muốn Mayami chỉ gọi "Sou-chan" thì báo.
4. **1668** — "Tôi nhận lời": người nghe là Mayami, suy từ mạch 1659–1662; đã ghi chú.

## 10. Second pass (đọc lại toàn bộ fix vs JP)

- **Tổng số fix đọc lại: 60**
- **Đã xác minh lại: 60**
- **Đã gỡ bỏ: 0**
- **Đã sửa lại: 0**
- Ghi chú: đếm bằng mắt ban đầu sai ở 1579/1619 (viết 9 a thay vì 8 a) — đã phát hiện khi kiểm bằng script và sửa trước khi chốt; đếm bằng mắt cũng sai ở 1757 (tưởng ちゅううううっ, thực tế ちゅううっ = 3 u, VN đúng nên giữ). Tất cả số nguyên âm trong fix cuối đã được script đếm lại: 1440 = 19 a, 1446 = 20 u, 1477 = 19 a, 1478 = 18 a, 1479 = 14 a, 1611 = 10 o, 1441 = 6 a, 1467 = 4 a, 1579/1619 = 8 a.

## 11. Khối TOML (đã kiểm parse, 60 key)

```toml
"1042" = "「――Ư」"
"1044" = "「――――Ư――Hà――ưm!!」"
"1061" = "「…………。…………。…………（Ực）――。 ……Chị……cũng………………nhé?…………Ư」"
"1080" = "「……Ý nghĩa của việc Hibiki chọn bộ đồ bơi này. Lý do chị Mayami ngạc nhiên\\nvà bối rối nhưng vẫn thay đồ, tôi đã hiểu rồi.」"
"1390" = "「Sức mạnh――của chị Mayami――cũng cần thiết――ku! Chúng ta\\n――sẽ làm tình――cả ba người――và trở thành, một gia đình.」"
"1414" = "「Chỉ bằng ngực. Không nhờ đến sự trợ giúp của tay hay miệng, chỉ bằng ngực thôi.\\nTôi vẫn chưa, một lần nào có thể xuất tinh được. Vì vậy.」"
"1420" = "「Chắc là đang hưng phấn vì ngón tay của Hibiki, và lời nói của tôi. \\nTừ cửa mình nhỏ nhắn e ấp, dâm thủy đang tràn ra.」"
"1439" = "「Hyu!!!? ~~~~~~~~~~Ư!!!!」"
"1440" = "「Hyuaaaaaaaaaaaaaaaaaaan!」"
"1441" = "「Hyaaaaaa!? Fu! Hya!? Ưm――\\nFua! A! Aaaaa! Không được, đâu.」"
"1446" = "「Kyuuuuuuuuuuuuuuuuuuuun!!」"
"1458" = "「~~~~~~~~Ư!!!」"
"1467" = "「Fuyaaaa!? H-Hii-chan――a!!!?」"
"1477" = "「Fuaaaaaaaaaaaaaaaaaaa!!!!」"
"1478" = "「Fuaaaaaaaaaaaaaaaaaan!!!」"
"1479" = "「Fuaaaaaaaaaaaaaa!!!!?」"
"1496" = "「Hà…… a…… Sou, chan――Hii, chan――Ư」"
"1508" = "「Ư!? Ư!? Ư!? Ư!!?」"
"1513" = "「Ku――a! A! A!!!」"
"1525" = "「Ư!!!!!!!」"
"1530" = "「A――ưm…… e~~~~~~~Ư」"
"1551" = "「Ư! ――A――hia! A――ha!!」"
"1552" = "「Ư!」"
"1553" = "「A!」\\n「Ư!!!!!」"
"1555" = "「A! Fua! A!!! Nguuuuu~Ư!!」"
"1557" = "「Ư! ~~~~~………………. …………………………………………………Vâng!!!」"
"1561" = "「Ư!!」"
"1562" = "「Ư!!!」"
"1563" = "「Ư!!!!」"
"1564" = "「Ư!!!!!」"
"1565" = "「Ư!!!!!!!!!」"
"1566" = "「Ư!!!!?」"
"1571" = "「~~~~~~~~~~~~~~~Ư!!!!!」"
"1579" = "「Ưm…… 'Aaaaaaaan' Amu――Ư――\\nChụt――rê ru――rê ru――chùn chụt――rê ryu」"
"1608" = "「Pua! A――. ƯƯ!!!!」"
"1611" = "「Oooooooooo!!!」"
"1615" = "「Bởi, vì――ưm――nhưng mà, ngực của em, thì\\n……ku――quả nhiên――vẫn hơi――quá sức.」"
"1619" = "「Đây. Chị hai. A, coi chừng vướng ở cổ họng nhé?\\nƯm…… 'Aaaaaaaan'」"
"1668" = "「Tôi nhận lời.」"
"1679" = "「Tôi――tôi――tôi, tôi!!!!」"
"1681" = "「Tôi…… muốn ngắm nhìn――\\nngắm nhìn hai cái bướm đặt cạnh nhau, và so sánh.」"
"1683" = "「Tôi đã luôn, coi dục vọng này, là điều tuyệt đối cấm kỵ.\\nTừ sau khi kết đôi với Hibiki thì đương nhiên rồi, nhưng ngay cả trước đó cũng vậy.」"
"1691" = "「Em cũng, em cũng có cùng――cảm giác――\\nNên là! Ưm! Nên là, này?」"
"1694" = "「Tôi và, Hibiki――đã trải qua biết bao ngày đêm,\\ncùng nhau chia sẻ tâm hồn, thời gian, thể xác――để thắt chặt, mối quan hệ.」"
"1700" = "「Tôi muốn, làm tình, với cả Hibiki, và cả chị Mayami, vô cùng muốn.\\nTôi muốn đưa vào ngay lập tức, nhưng, nhưng mà. Trước đó.」"
"1702" = "「Cùng với Hibiki, tôi muốn chị trở thành vợ tôi.\\nCùng với Hibiki và tôi một lần nữa――trở thành một gia đình ba người.」"
"1703" = "「Tôi đã đóng chặt trái tim mình, coi đó là điều tuyệt đối không được khao khát.\\nNhưng, nếu như, cả ba chúng ta đều có chung một ước muốn.」"
"1706" = "「Việc tôi đóng chặt trái tim và coi đó là điều cấm kỵ tuyệt đối, có nghĩa là――\\nBởi vì, tôi đã, khao khát nó, quá mãnh liệt.」"
"1709" = "「Anh biết――nhưng――không thể――dừng lại được!!!」"
"1712" = "「Em! Em khao khát điều đó! ……Ư. ――――Ưm!!」"
"1714" = "「Tôi sẽ, làm cho cả hai, mang thai――tuyệt đối, chắc chắn,\\ncả Hibiki――cả chị――Mayami――những đứa con, của tôi――」"
"1736" = "「Hibiki! Hibiki! Một chút nữa thôi――vì vậy! Ư! Anh sẽ――rót toàn bộ――tinh dịch――vào tử cung của Hibiki!」"
"1738" = "「Hibiki! Chị Mayami!\\nTôi――! Tôi――tôi sắp!!!」"
"1743" = "「Hibiki, chị Mayami! Hôn, tôi muốn hôn. Cả ba người.\\nHai người hãy thò lưỡi ra――chạm lưỡi vào nhau đi.」"
"1758" = "「Ví dụ như sau này có chuyện gì xảy ra, dù Hibiki có ghét tôi,\\ncó hận tôi đi chăng nữa――tôi vẫn sẽ tiếp tục yêu Hibiki. Tuyệt đối là vậy.」"
"1770" = "「Chị Mayami. Lần này, hãy giúp tôi bên này.」"
"1773" = "「Tôi sẽ, cưới. Cả chị Mayami nữa. Bên cạnh Hibiki.\\nRồi, ba chúng ta sẽ trở thành vợ chồng, trở thành gia đình.」"
"1775" = "「Đang khao khát phần cương cứng của tôi, tinh trùng của tôi vào trong tử cung.\\nĐang tuyệt vọng cố gắng dẫn dắt, đang cầu xin tôi.」"
"1791" = "「Đừng giấu! Của chị Mayami, của Hibiki――\\nTôi muốn nhìn thấy bướm của chị gái nuôi và em gái quan trọng của tôi đặt cạnh nhau.」"
"1812" = "「Chuyện làm tình――giữa ba chúng ta. Từ lần đầu tiên ôm Hibiki\\n――từ khi biết đến tình dục, tôi đã」"
```

## Kết bài

File lr_日々姫真闇h1_三人家族 (02_Hibiki, H-scene): đọc toàn bộ 436 dòng, **60 dòng sai (13,8%)** — nặng nhất là đại từ xưng hô Soutetsu (22 dòng, chủ yếu độc thoại dùng "em/anh" thay vì "tôi" và đối thoại với Mayami/cả hai dùng "em/anh" thay vì "tôi") và っ thô (21 dòng) cùng số nguyên âm moan (9 dòng). Không có lệch hàng, xoay vòng, nhiễm chéo, mồ côi, chưa dịch hay trùng key. Một gasp sweep bỏ sót (1579) đã bắt được khi đọc toàn bộ. Cần Hieu quyết: 義姉/義妹 có dịch "nuôi" không, và có chuẩn hoá nghiêm số nguyên âm a-run không.
