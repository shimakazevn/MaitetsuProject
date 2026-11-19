# Kiểm tra bản dịch — 00_Common 01: 共通01_右田双鉄の帰還

File: `共通01_右田双鉄の帰還.txt.toml` — file mở đầu game (Soutetsu trở về Ohitoyo trên máy bay Navi, tai nạn đường sắt Fujikawa).
Đây là kiểm tra ĐẦY ĐỦ (full audit) thay thế bản pilot 19/11 (35/155, chỉ là bản nháp).

## §1. Tổng quan

- Tổng số dòng script: **155** (monologue 44, hội thoại 111).
- Số dòng sai: **48/155 (31,0%)** — hội thoại 34/111 (30,6%), độc thoại 14/44 (31,8%).
- Phân loại: terminology 10 (Ohitoyo 8, Migita 2), meaning 23, pronoun 4, minor 7, gasp 4.
- TOML md5: `6fbb8ed9aba7b7998742a738c2a223d7` (35.461 byte, BOM + CRLF, `[selections]` 0, `[info]` trống, bản duy nhất — không có file trùng md5).
- CSV↔TOML: 58 dòng khớp tuyệt đối + 97 dòng chỉ khác ở chỗ TOML-2 làm phẳng ký tự `\n` thành khoảng trắng — **0 khác biệt thực chất**. JP comment trong TOML: 171 dòng trích được, **0 lệch so với CSV3**.
- Thẻ `%l`: JP = VN trên mọi dòng, 0 thẻ hỏng.
- **0 misaligned / 0 rotation / 0 contamination** (kiểm tra chỉ mục VN toàn dự án: 0/47 giá trị cũ xuất hiện ở file khác) / **0 orphan / 0 untranslated** (0 dòng VN==TW) / **0 duplicate key**.
- **0 dòng uncertain.**
- Ohitoyo trong file: 8/8 dòng JP 御一夜 đã sửa xong — file này còn **0 Ohimitera**. (Sau file này, Ohitoyo còn lại trong 00_Common: 15 — chỉ còn file 15.)

## §2. Bảng fix (48 dòng)

### 996 — monologue — pronoun
- JP: …………なんで、こんなに眠いんだ――\nさっきまで、僕……寝てた、の、に…………
- TW: …………為什麼，這麼睏呢——明明，直到剛才……我都還……在……睡…………
- Cũ: …………Tại sao, lại buồn ngủ thế này——\nRõ ràng, lúc nãy mình……vẫn còn đang……ngủ, cơ, mà…………
- Mới: …………Sao mà buồn ngủ thế này——\nRõ ràng lúc nãy tôi……vẫn còn đang……ngủ cơ mà…………
- Lý do: Pilot giữ: mình→tôi (mặc định; độc thoại nhận ra mình buồn ngủ, không phải tự vấn cảm xúc kiểu h3 1683 nên ngoại lệ mình không bắt buộc); Tại sao, lại→Sao mà; bỏ dấu phẩy kiểu máy dịch.

### 1000 — monologue — meaning
- JP: ……ダメ、だ。\n聞いてること、意味、わからない。
- TW: ……不行……了。聽到的話……已經……理解不了了。
- Cũ: ……Không, được rồi.\nNhững gì mình nghe thấy, chẳng, hiểu gì cả.
- Mới: ……Không ổn rồi.\nNhững gì tôi nghe thấy, chẳng hiểu gì cả.
- Lý do: Pilot giữ: ダメ、だ=Không ổn rồi (không phải Không, được rồi); mình→tôi; bỏ dấu phẩy thừa.

### 1004 — monologue — pronoun
- JP: ……出血、僕の、頭……から。\nなら、このまま――けど……………………
- TW: ……出血，我的，頭……上。那索性，就這樣——可是……………………
- Cũ: ……Chảy máu, từ……đầu, của mình.\nVậy thì, cứ thế này——nhưng mà……………………
- Mới: ……Máu chảy từ……đầu tôi.\nVậy thì, cứ thế này——nhưng mà……………………
- Lý do: Pilot giữ: mình→tôi; bỏ dấu phẩy kiểu máy dịch.

### 1009 — monologue — minor
- JP: ……物との会話。\nあるいは、ただの独り言。
- TW: ……我對著東西說話。或者說，只是自言自語。
- Cũ: ……Trò chuyện với đồ vật.\nHay có lẽ, chỉ là độc thoại.
- Mới: ……Trò chuyện với đồ vật.\nHay có lẽ chỉ là độc thoại.
- Lý do: Pilot giữ: bỏ dấu phẩy thừa sau có lẽ.

### 1012 — monologue — minor
- JP: ……声、誰かの声が聞こえる。\n……感じる……手……誰かが、僕を……ゆすってる。
- TW: ……聲音，好像聽到了誰的聲音。……感覺到……手……有誰，在……搖晃我。
- Cũ: ……Tiếng nói, tôi nghe thấy tiếng ai đó.\n……Cảm nhận được……bàn tay……ai đó, đang……lay tôi.
- Mới: ……Tôi nghe thấy tiếng ai đó.\n……Cảm nhận được……bàn tay……ai đó đang……lay tôi.
- Lý do: Pilot giữ: gọn câu trùng lặp; bỏ dấu phẩy thừa.

### 1023 — 清美勝子 — meaning
- JP: 「\x%l制動;#00ffc040;制動%l;#;了解。この速度から\x%l非常;#00ffc040;非常%l;#;は無理――よね」
- TW: 「\x%l制動;#00ffc040;減速%l;#;了解。現在這速度\x%l非常;#00ffc040;緊急%l;#;是沒辦法用了」
- Cũ: 「Đã rõ \x%l制動;#00ffc040;hãm phanh%l;#;. Với tốc độ này thì \x%l非常;#00ffc040;phanh khẩn cấp%l;#; là không thể——rồi.」
- Mới: 「Đã rõ, \x%l制動;#00ffc040;hãm phanh%l;#;. Với tốc độ này thì \x%l非常;#00ffc040;phanh khẩn cấp%l;#; là không thể——nhỉ.」
- Lý do: Pilot giữ: よね=nhỉ (không phải rồi); thêm dấu phẩy sau Đã rõ.

### 1027 — ハチロク — meaning

**JP:** 「\x%l粘着力;#00ffc040;粘着力%l;#;が著しく低下しています。⏎[すなま,1]砂撒きを進言します」

**TW:** 「\x%l粘着力;#00ffc040;黏著力%l;#;大幅下降。建議放沙」

**VN cũ:** 「\x%l粘着力;#00ffc040;Lực bám đường%l;#; đang sụt giảm nghiêm trọng.⏎Kiến nghị phun cát dồn toa.」

**Fix:** 「\x%l粘着力;#00ffc040;Lực bám đường%l;#; đang sụt giảm nghiêm trọng.⏎Kiến nghị phun cát.」

"dồn toa" không có trong JP (砂撒きを進言します) lẫn TW (建議放沙) — chỉ có trong ví dụ mẫu ai_translation_prompt.md của Hieu. Hieu chốt 20/11 02:03: dịch sao thuần Việt, dễ hiểu nhất là được → bỏ "dồn toa". (Fix do parent bổ sung sau audit.)

### 1041 — ハチロク — meaning
- JP: 「……これ以上は\x%l滑走;#00ffc040;滑走%l;#;します。\n限界です。制動力は足りません」
- TW: 「……力度再大就要\x%l滑走;#00ffc040;打滑%l;#;了。已經到極限了。減速度不足」
- Cũ: 「……Hơn nữa sẽ bị \x%l滑走;#00ffc040;trượt bánh%l;#; mất.\nĐến giới hạn rồi. Lực hãm phanh không đủ.」
- Mới: 「……Cứ thế này nữa sẽ bị \x%l滑走;#00ffc040;trượt bánh%l;#; mất.\nĐến giới hạn rồi. Lực hãm phanh không đủ.」
- Lý do: Pilot giữ: これ以上=cứ thế này nữa (không phải hơn nữa).

### 1047 — 清美勝子 — meaning
- JP: 「……やむなしね。\n[しずおか,1]靜岡での\x%l接続;#00ffc040;接続%l;#;は遅らせたくなかったんだけど」
- TW: 「……沒辦法啦。還要在靜岡進行\x%l接続;#00ffc040;會車%l;#;呢，真不想晚點啊」
- Cũ: 「……Hết cách rồi.\nTôi không muốn làm chậm trễ việc \x%l接続;#00ffc040;kết nối chuyển tàu%l;#; ở Shizuoka đâu.」
- Mới: 「……Hết cách rồi.\nTôi đã không muốn làm chậm việc \x%l接続;#00ffc040;kết nối chuyển tàu%l;#; ở Shizuoka đâu.」
- Lý do: Pilot giữ: 遅らせたくなかった là ý muốn trong quá khứ → đã không muốn làm chậm.

### 1160 — 帝鉄職員Ａ — meaning
- JP: 「いや、転覆だ！　\x%l脱線転覆;#00ffc040;脱線転覆%l;#;！！\nだが、全滅よりはよほどマシだっ！！」
- TW: 「不，傾覆了！\x%l脱線転覆;#00ffc040;脫軌傾覆%l;#;！！不過總比全滅好多了！！」
- Cũ: 「Không, lật rồi! \x%l脱線転覆;#00ffc040;Trật bánh lật tàu%l;#;!!\nNhưng thế này vẫn còn tốt chán so với bị diệt vong toàn bộ!!」
- Mới: 「Không, là lật tàu! \x%l脱線転覆;#00ffc040;Trật bánh lật tàu%l;#;!!\nNhưng thế này vẫn còn tốt hơn nhiều so với tất cả cùng chết!!」
- Lý do: Pilot giữ: 転覆だ=là lật tàu; 全滅=tất cả cùng chết (không phải bị diệt vong toàn bộ).

### 1166 — ハチロク — minor
- JP: 「お客様、ご着席大丈夫でしょうか」
- TW: 「乘客們不知有沒有好好落座呢」
- Cũ: 「Hành khách, không biết đã ngồi vững hết chưa.」
- Mới: 「Quý khách đã ngồi vào chỗ ổn cả chưa ạ.」
- Lý do: Pilot giữ: お客様→Quý khách (kính ngữ); câu cũ lủng củng.

### 1168 — 双鉄 — meaning
- JP: 「そうだな、着水前に一度上から見ておこう」
- TW: 「也是，在水上降落前先從空中俯瞰一下吧」
- Cũ: 「Cũng được, trước khi hạ cánh xuống nước thì nhìn từ trên cao một chút vậy.」
- Mới: 「Ừ, trước khi hạ cánh xuống nước thì nhìn từ trên cao một lượt vậy.」
- Lý do: Pilot giữ: そうだな=Ừ (không phải Cũng được).

### 1170 — ナビ — terminology
- JP: 「承知しています。まもなく、目的地の[みぎたいちしゅぞうもと,5]右田一酒造元です。\n上空を一度通過しますか？」
- TW: 「了解。即將抵達目的地，右田一釀酒廠。要從上空先飛過一次嗎？」
- Cũ: 「Tôi hiểu rồi. Sắp tới điểm đến là xưởng rượu Migita System.\nNgài có muốn bay qua không phận một lần không?」
- Mới: 「Tôi hiểu rồi. Sắp tới điểm đến là xưởng rượu Migita Ichi.\nNgài có muốn bay qua không phận một lần không?」
- Lý do: Migita System→Migita Ichi (quyết định 19/11 #17; JP 右田一酒造元, TW 右田一釀酒廠; không tồn tại thực thể Migita System). Pilot giữ theo docs cũ — quyết định mới thay thế.

### 1173 — 清美勝子 — meaning
- JP: 「\x%l車掌;#00ffc040;車掌%l;#;・[せき]関、\x%l車販;#00ffc040;車販%l;#;・[まゆずみ]黛のコンビでしょ？\nやってるわ。きちんと、彼女たちの仕事を」
- TW: 「今天是關擔當\x%l車掌;#00ffc040;列車長%l;#;、黛負責\x%l車販;#00ffc040;車售%l;#;吧？她們一定會做好自己的工作的」
- Cũ: 「Hôm nay là bộ đôi \x%l車掌;#00ffc040;trưởng tàu%l;#; Seki và \x%l車販;#00ffc040;nhân viên bán hàng%l;#; Mayuzumi mà nhỉ?\nHọ đang làm đấy. Chắc chắn họ sẽ hoàn thành tốt công việc của mình.」
- Mới: 「Là bộ đôi \x%l車掌;#00ffc040;trưởng tàu%l;#; Seki và \x%l車販;#00ffc040;nhân viên bán hàng%l;#; Mayuzumi mà nhỉ?\nHọ đang làm đấy. Chắc chắn họ sẽ hoàn thành tốt công việc của mình.」
- Lý do: SỬA LẠI pilot: bỏ Hôm nay (JP không có; TW thêm 今天 nhưng JP hơn TW). Câu 2 giữ nguyên bản cũ theo TW (TW: 她們一定會做好自己的工作的) — pilot đổi thành mệnh lệnh Cứ để họ làm... là lệch giọng (JP やってるわ là khẳng định). JP cụt nhưng TW cho đủ căn cứ hoàn thiện.

### 1185 — 清美勝子 — meaning
- JP: 「やってやるわよ。一世一代の仕事をね！」
- TW: 「來吧。這輩子就押在這一次了！」
- Cũ: 「Làm thôi. Đánh cược cả đời vào lần này!」
- Mới: 「Làm thôi! Đây là công việc cả đời mới có một lần đấy!」
- Lý do: Pilot giữ: 一世一代=cả đời mới có một lần (không phải đánh cược cả đời).

### 1217 — ハチロク — meaning
- JP: 「停止、以外――。\nでしたら、逆に！」
- TW: 「剎停以外嗎。那就反其道行之！」
- Cũ: 「Ngoài việc, dừng lại——.\nNếu vậy thì, làm ngược lại!」
- Mới: 「Ngoài việc dừng lại ra——.\nVậy thì, làm ngược lại!」
- Lý do: Pilot giữ: 停止以外=ngoài việc dừng lại ra; bỏ dấu phẩy thừa.

### 1224 — 双鉄 — terminology
- JP: 「なるほど。それゆえ、御一夜は衰退し、\n\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の誘致話が持ち上がったわけか？」
- TW: 「原來如此。所以御一夜才會衰退成這樣，甚至提出讓\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶嗎？」
- Cũ: 「Ra là vậy. Vì thế nên Ohimitera mới suy thoái,\nvà câu chuyện thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; mới được đưa ra bàn tán sao?」
- Mới: 「Ra là vậy. Vì thế nên Ohitoyo mới suy thoái,\nvà câu chuyện thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#; mới được đưa ra bàn tán sao?」
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1247 — ハチロク — gasp
- JP: 「っ！　――最大限の\x%l制動;#00ffc040;制動%l;#;をください。\n\x%l滑走;#00ffc040;滑走%l;#;せぬよう補助します」
- TW: 「啊！請進行全力\x%l制動;#00ffc040;減速%l;#;。我來輔助避免\x%l滑走;#00ffc040;打滑%l;#;」
- Cũ: 「っ! ——Xin hãy dùng \x%l制動;#00ffc040;hãm phanh%l;#; tối đa.\nTôi sẽ hỗ trợ để không bị \x%l滑走;#00ffc040;trượt bánh%l;#;.」
- Mới: 「Ư! ——Xin hãy dùng \x%l制動;#00ffc040;hãm phanh%l;#; tối đa.\nTôi sẽ hỗ trợ để không bị \x%l滑走;#00ffc040;trượt bánh%l;#;.」
- Lý do: Sweep raw-tsu (đã kiểm chứng JP 「っ！――...」): っ đầu câu →Ư. Áp nguyên giá trị sweep, chuyển sang dạng ngắt dòng của CSV3.

### 1260 — ナビ — meaning
- JP: 「矛盾の判断には大きな演算能力を必要とし、\nその負荷が双鉄様の安全を脅かすという……双鉄様？」
- TW: 「在矛盾中做出判斷需要大量的計算能力，而這個負荷又會威脅到雙鐵少爺的安全……雙鐵少爺？」
- Cũ: 「Việc đưa ra quyết định trong sự mâu thuẫn đòi hỏi năng lực tính toán lớn,\nvà khối lượng công việc đó sẽ đe dọa đến sự an toàn của ngài Soutetsu…… Ngài Soutetsu?」
- Mới: 「Việc phán đoán trong mâu thuẫn đòi hỏi năng lực tính toán rất lớn,\nvà gánh nặng đó sẽ đe dọa sự an toàn của ngài Soutetsu…… Ngài Soutetsu?」
- Lý do: Pilot giữ: 判断=phán đoán; 負荷=gánh nặng (không phải khối lượng công việc).

### 1262 — 帝鉄職員Ａ — meaning
- JP: 「ここだ！　落ちてない！　落ちてないぞっ！」
- TW: 「在這裡！沒有墜河！沒有墜河！」
- Cũ: 「Ở đây! Không bị rơi! Không bị rơi xuống sông!」
- Mới: 「Ở đây! Không rơi! Không rơi đâu!」
- Lý do: Pilot giữ: bỏ xuống sông bịa thêm (JP 落ちてない không có sông; JP hơn TW — TW ghi 墜河 nhưng JP mới là gốc).

### 1278 — ナビ — terminology
- JP: 「ご命令を了解しました。\n同期間における御一夜市の変化をご報告します」
- TW: 「已收到您的命令。立即向您報告該期間御一夜市發生的變化」
- Cũ: 「Đã rõ mệnh lệnh.\nXin báo cáo những thay đổi của thành phố Ohimitera trong cùng khoảng thời gian.」
- Mới: 「Đã rõ mệnh lệnh.\nXin báo cáo những thay đổi của thành phố Ohitoyo trong cùng khoảng thời gian.」
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1308 — 双鉄 — meaning
- JP: 「お前のように優秀なナビを、\n敵に回したくはないからな」
- TW: 「我可不想與你這麼優秀的導航系統為敵」
- Cũ: 「Bởi vì tôi không muốn đối đầu\nvới một hệ thống dẫn đường xuất sắc như cô đâu.」
- Mới: 「Vì tôi chẳng muốn biến một Navi xuất sắc như cô\nthành kẻ địch đâu.」
- Lý do: Pilot giữ: 敵に回したくない=không muốn biến thành kẻ địch. Giữ nguyên vị trí ngắt dòng theo JP (2 dòng).

### 1317 — 清美勝子 — gasp
- JP: 「[ま]撒いた瞬間流されるのがオチでしょうけど。\nま、やらないよりはね――っと」
- TW: 「放下的沙子恐怕轉瞬就會被沖走吧。算了，總比什麼也不做強——吧」
- Cũ: 「Chắc rắc xuống cái là bị cuốn trôi đi ngay thôi.\nNhưng mà, có làm còn hơn không——っ」
- Mới: 「Chắc rắc xuống cái là bị cuốn trôi đi ngay thôi.\nNhưng mà, có làm còn hơn không——Ư」
- Lý do: Sweep raw-tsu (đã kiểm chứng JP ――っと): ――っと cuối câu →――Ư. Áp nguyên giá trị sweep.

### 1329 — ナビ — minor
- JP: 「はい。ご息女です。\nしかし、行政手腕は遺伝しなかったとの評判です」
- TW: 「是的，是前任市長千金。不過依風評看來，她並沒有遺傳前任市長的執政能力」
- Cũ: 「Vâng. Là con gái của ngài ấy.\nTuy nhiên, có nhiều đánh giá cho rằng năng lực hành chính không được di truyền.」
- Mới: 「Vâng. Là con gái của ngài ấy.\nNhưng nghe nói năng lực hành chính thì không được di truyền.」
- Lý do: Pilot giữ: 評判=nghe nói; gọn câu.

### 1335 — ハチロク — meaning
- JP: 「状況未確定の事故報告。\x%l発報;#00ffc040;発報%l;#;は[キュウロクヨンニイ,3]9642\x%lレイルロオド;#00ffc040;レイルロオド%l;#;。\n\x%l帝鉄貨物;#00ffc040;帝鉄貨物%l;#;。十五両\x%l編成;#00ffc040;編成%l;#;。全車両喪失の可能性あり」
- TW: 「有狀況尚未確認的事故報告。\x%l発報;#00ffc040;發報%l;#;的是９６４２\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;。\x%l帝鉄貨物;#00ffc040;帝國鐵路貨運%l;#;。十五輛\x%l編成;#00ffc040;編組%l;#;。可能已全部損失」
- Cũ: 「Báo cáo sự cố tình trạng chưa xác định. \x%l発報;#00ffc040;Phát tín hiệu báo động%l;#; từ \x%lレイルロオド;#00ffc040;Railord%l;#; 9642.\n\x%l帝鉄貨物;#00ffc040;Vận tải hàng hóa Đường sắt Hoàng gia%l;#;. \x%l編成;#00ffc040;Đoàn tàu%l;#; mười lăm toa. Có khả năng toàn bộ toa xe đã bị tổn thất.」
- Mới: 「Báo cáo sự cố tình trạng chưa xác định. \x%l発報;#00ffc040;Phát tín hiệu báo động%l;#; từ \x%lレイルロオド;#00ffc040;Railord%l;#; 9642.\n\x%l帝鉄貨物;#00ffc040;Vận tải hàng hóa Đường sắt Đế quốc%l;#;. \x%l編成;#00ffc040;Đoàn tàu%l;#; mười lăm toa. Có khả năng mất toàn bộ toa xe.」
- Lý do: Pilot giữ câu cuối (mất toàn bộ toa xe). Thêm: gloss 帝鉄貨物 Đường sắt Hoàng gia→Đường sắt Đế quốc — quyết định 19/11 #6; file 01 là file mở đầu game và đây là lần xuất hiện 帝鉄 duy nhất trong file → tooltip %l lần đầu dùng dạng đầy đủ Đường sắt Đế quốc.

### 1337 — ハチロク — meaning
- JP: 「当機に停止の手段無し。\x%l制動;#00ffc040;制動%l;#;力を最大限適正にとっても……七五秒後、止まりきれずに――」
- TW: 「本次列車已無法停車。即便進行極限\x%l制動;#00ffc040;減速%l;#;也無法剎停，在七十五秒後……」
- Cũ: 「Chuyến tàu này đã không còn cách dừng lại. Dù có dùng lực \x%l制動;#00ffc040;hãm phanh%l;#; tối đa đi chăng nữa…… thì 75 giây sau, cũng không thể dừng hẳn lại mà——」
- Mới: 「Chuyến tàu này đã không còn cách dừng lại. Dù có dùng lực \x%l制動;#00ffc040;hãm phanh%l;#; tối đa một cách hợp lý nhất…… 75 giây sau, cũng không dừng hẳn được mà——」
- Lý do: Pilot giữ: bổ sung 適正に=một cách hợp lý nhất (bản cũ sót); 止まりきれず=không dừng hẳn được.

### 1352 — ナビ — terminology
- JP: 「その便利な物品を作る工場を、双鉄様は、\n御一夜に誘致してほしくはないとおっしゃっています」
- TW: 「然而雙鐵少爺卻說，不想讓生產這些方便物品的工廠在御一夜落戶」
- Cũ: 「Thế mà ngài Soutetsu lại nói,\nkhông muốn thu hút nhà máy sản xuất những vật phẩm tiện lợi đó về Ohimitera.」
- Mới: 「Thế mà ngài Soutetsu lại nói,\nkhông muốn thu hút nhà máy sản xuất những vật phẩm tiện lợi đó về Ohitoyo.」
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1359 — 双鉄 — terminology
- JP: 「御一夜以外に作って欲しいと思わずにはいられんのだ。\nここは、僕のもうひとつの故郷なのだから」
- TW: 「看到這景色自然會希望不要在御一夜進行生產。這裡可是我的第二故鄉啊」
- Cũ: 「Không thể không mong muốn họ xây dựng nó ở nơi khác ngoài Ohimitera.\nBởi vì nơi này, là quê hương thứ hai của tôi.」
- Mới: 「Không thể không mong muốn họ xây dựng nó ở nơi khác ngoài Ohitoyo.\nBởi vì nơi này, là quê hương thứ hai của tôi.」
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1375 — ハチロク — gasp
- JP: 「すぐに先方の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;へ\x%l共感;#00ffc040;共感%l;#;をつなぎ遅延連絡\n――っ！？　なっ！？　え？　もう一度っ！？」
- TW: 「立即與前方最近的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;進行\x%l共感;#00ffc040;共鳴%l;#;連結告知晚點——！？什…！？哎？請重複！？」
- Cũ: 「Tôi sẽ lập tức kết nối \x%l共感;#00ffc040;cộng cảm%l;#; với \x%lレイルロオド;#00ffc040;Railord%l;#; phía trước để thông báo việc chậm trễ\n——っ!? Gì cơ!? Hả? Xin hãy nhắc lại!?」
- Mới: 「Tôi sẽ lập tức kết nối \x%l共感;#00ffc040;cộng cảm%l;#; với \x%lレイルロオド;#00ffc040;Railord%l;#; phía trước để thông báo việc chậm trễ\n——Ư!? Gì cơ!? Hả? Xin hãy nhắc lại!?」
- Lý do: Sweep raw-tsu (đã kiểm chứng JP ――っ!?): →――Ư!? Áp nguyên giá trị sweep.

### 1382 — ハチロク — gasp
- JP: 「\x%l制動;#00ffc040;制動%l;#;続行。\n――もう少し――圧、もう少しだけ――っ！！！」
- TW: 「繼續\x%l制動;#00ffc040;減速%l;#;。壓力還差一點，加把勁！！！」
- Cũ: 「Tiếp tục \x%l制動;#00ffc040;hãm phanh%l;#;.\n——Thêm chút nữa——áp suất, thêm một chút nữa thôi——っ!!!」
- Mới: 「Tiếp tục \x%l制動;#00ffc040;hãm phanh%l;#;.\n——Thêm chút nữa——áp suất, thêm một chút nữa thôi——Ư!!!」
- Lý do: Sweep raw-tsu (đã kiểm chứng JP ――っ!!!): →――Ư!!! Áp nguyên giá trị sweep.

### 1397 — ハチロク — minor
- JP: 「そうですね。\nわたくしたちも、わたくしたちの」
- TW: 「說得也是呢。我們也要，做好我們的…」
- Cũ: 「Nói cũng phải.\nChúng ta cũng phải, làm tốt công việc của chúng ta.」
- Mới: 「Nói cũng phải.\nChúng ta cũng phải làm tốt công việc của mình.」
- Lý do: Pilot giữ: bỏ dấu phẩy thừa; câu gốc cụt — phần hoàn thiện theo đúng bản cũ, không bịa thêm.

### 1398 — 清美勝子 — meaning
- JP: 「報告なさい。何の方法？　報告が一秒遅れるだけで、\n危険が何メートル近づくかわかってるでしょうに」
- TW: 「請報告，什麼辦法？你應該清楚，晚一秒報告危險就會接近多少公尺的吧」
- Cũ: 「Báo cáo đi. Hết cách gì? Báo cáo chậm một giây thôi là\nnguy hiểm sẽ tiến gần thêm bao nhiêu mét, cô biết rõ mà.」
- Mới: 「Báo cáo đi. Phương pháp gì cơ? Báo cáo chậm một giây thôi là\nnguy hiểm tiến gần thêm bao nhiêu mét, cô biết rõ mà.」
- Lý do: Pilot giữ: 何の方法？=Phương pháp gì cơ? (không phải Hết cách gì?).

### 1404 — 清美勝子 — meaning
- JP: 「お客様乗せてんのよ、無理でも止めるっ！！\n再減速！　そっち主導で！！」
- TW: 「車上還有乘客，無論如何都要停下！！進一步減速，以你為主！！」
- Cũ: 「Trên tàu vẫn còn hành khách, không thể cũng phải dừng lại!!\nTiếp tục giảm tốc! Cô làm chủ đạo đi!!」
- Mới: 「Trên tàu còn có hành khách đấy, dù không thể cũng phải dừng lại!!\nGiảm tốc lại! Cô chủ đạo đi!!」
- Lý do: Pilot giữ: 再減速=giảm tốc lại (không phải tiếp tục giảm tốc).

### 1430 — ハチロク — meaning
- JP: 「再減速了解。\x%l圧;#00ffc040;[あつ,4]ブレーキ力%l;#;、強めます――っ！」
- TW: 「進一步減速了解。加大\x%l圧;#00ffc040;壓力%l;#;！」
- Cũ: 「Đã rõ tiếp tục giảm tốc. \x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng cường——っ!」
- Mới: 「Đã rõ, giảm tốc lại. \x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng thêm——Ư!」
- Lý do: Gộp pilot + sweep: 再減速=giảm tốc lại, 強めます=tăng thêm (pilot); っ cuối câu →Ư (sweep 1430, đã kiểm chứng JP).

### 1434 — 帝鉄職員Ａ — meaning
- JP: 「ならどうしろとっ！！」
- TW: 「那你說怎麼辦！！」
- Cũ: 「Vậy cậu bảo phải làm sao!!」
- Mới: 「Vậy thì phải làm sao đây!!」
- Lý do: Pilot giữ: bỏ cậu bảo bịa thêm (JP どうしろと=phải làm sao đây).

### 1438 — 清美勝子 — meaning
- JP: 「だったら他っ！　停止以外の方策をっ！\n手段は問わない！　目標は転落回避っ！！！」
- TW: 「那就想想別的辦法！剎停以外的方法！什麼辦法都行！能不墜河就行！！！」
- Cũ: 「Thế thì cách khác! Tìm cách khác ngoài việc dừng tàu đi!\nCách gì cũng được! Mục tiêu là tránh rơi xuống sông!!!」
- Mới: 「Thế thì cách khác! Tìm cách khác ngoài việc dừng tàu đi!\nCách gì cũng được! Mục tiêu là tránh bị rơi xuống!!!」
- Lý do: Pilot giữ: 転落回避=tránh bị rơi xuống, bỏ xuống sông bịa thêm (JP hơn TW — TW ghi 墜河 nhưng JP không có sông).

### 1440 — 帝鉄職員Ｃ — minor
- JP: 「もちろんです！　\nですが――、一刻も早く病院につれていかないとっ」
- TW: 「那是自然！可是，得儘快送他去醫院」
- Cũ: 「Tất nhiên rồi!\nNhưng mà——, phải đưa đến bệnh viện càng sớm càng tốt.」
- Mới: 「Tất nhiên rồi!\nNhưng mà——phải đưa đến bệnh viện càng sớm càng tốt.」
- Lý do: Pilot giữ: bỏ dấu phẩy thừa sau ——.

### 1450 — 双鉄 — meaning
- JP: 「[ひない,1]雛衣というと、前の市長の？」
- TW: 「雛衣啊，是前任市長的？」
- Cũ: 「Hinai à, là của thị trưởng tiền nhiệm sao?」
- Mới: 「Hinai à, là con gái thị trưởng tiền nhiệm sao?」
- Lý do: Pilot giữ: 前の市長の雛衣=con gái thị trưởng tiền nhiệm (câu cũ gây khó hiểu).

### 1457 — ハチロク — minor
- JP: 「9642\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は『鉄橋崩落』と――断末魔の\x%l共感;#00ffc040;共感%l;#;で。\n……[ふじがわ,2]冨士川[きょうりょう,1]橋梁が崩落したと」
- TW: 「９６４２\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;在最後關頭通過\x%l共感;#00ffc040;共鳴%l;#;發出了“鐵橋坍塌”的消息。……內容是“富士川橋樑坍塌”」
- Cũ: 「\x%lレイルロオド;#00ffc040;Railord%l;#; 9642 truyền đạt qua \x%l共感;#00ffc040;cộng cảm%l;#; lúc hấp hối rằng 『Cầu sắt sập』.\n……Nội dung là cầu sắt Fujikawa đã sập.」
- Mới: 「\x%lレイルロオド;#00ffc040;Railord%l;#; 9642 truyền đạt qua \x%l共感;#00ffc040;cộng cảm%l;#; lúc hấp hối rằng 『Cầu sắt sập』.\n……Cầu sắt Fujikawa đã sập.」
- Lý do: Pilot giữ: bỏ Nội dung là thừa (đã có truyền đạt rằng).

### 1551 — monologue — terminology
- JP: だから視線はすぐに捉える――眼下を流れる光の帯を。\n太陽の煌きを豊かに返す、御一夜の象徴、クマ川を。
- TW: 因此，我的視線立即捕捉到了，眼前流淌著的光帶——那將太陽的光芒反射得五彩繽紛的，正是御一夜的象徵，隈河。
- Cũ: Nên ánh mắt tôi lập tức bắt lấy——dải sáng lấp lánh chảy dưới tầm mắt.\nCon sông Kuma, biểu tượng của Ohimitera, phản chiếu rực rỡ ánh mặt trời.
- Mới: Nên ánh mắt tôi lập tức bắt lấy——dải sáng lấp lánh chảy dưới tầm mắt.\nCon sông Kuma, biểu tượng của Ohitoyo, phản chiếu rực rỡ ánh mặt trời.
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1592 — monologue — terminology
- JP: 上空から見下ろす御一夜の町並みは、\n出て行ったときと、何も変わっていないように見える。
- TW: 我從上空俯瞰御一夜的街道。與當初離開時相比，這裡似乎一點都沒改變。
- Cũ: Nhìn từ trên cao, quang cảnh thành phố Ohimitera\ncó vẻ như chẳng hề thay đổi so với lúc tôi rời đi.
- Mới: Nhìn từ trên cao, quang cảnh thành phố Ohitoyo\ncó vẻ như chẳng hề thay đổi so với lúc tôi rời đi.
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

### 1601 — monologue — meaning
- JP: 機体姿勢を即座に戻し、けれど航路は変更しない。
- TW: 機身迅速回正，然而航線卻未有絲毫變化。
- Cũ: Ngay lập tức điều chỉnh lại tư thế máy bay, nhưng không thay đổi đường bay.
- Mới: Ngay lập tức lấy lại tư thế thân máy, nhưng không thay đổi đường bay.
- Lý do: Pilot giữ: 機体姿勢を戻し=lấy lại tư thế thân máy (không phải điều chỉnh lại tư thế máy bay).

### 1628 — monologue — terminology
- JP: そうして、[おひとよ,2]御一夜――\n眼下に広がるこの町も、僕を間違いなく救ってくれた。
- TW: 而此時，御一夜——下方映入眼簾的城鎮，也同樣拯救過我。
- Cũ: Và lúc này, Ohimitera——\nthành phố trải dài dưới tầm mắt kia, cũng đã từng cứu rỗi tôi.
- Mới: Và lúc này, Ohitoyo——\nthành phố trải dài dưới tầm mắt kia, cũng đã từng cứu rỗi tôi.
- Lý do: Mở rộng pilot (pilot chỉ sửa khoảng trắng sau ——): Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜). Trong CSV3 vị trí đó là ký tự ngắt dòng nên không còn khoảng trắng để sửa.

### 1634 — monologue — terminology
- JP: 生家という言葉に習うのならば、僕の育家である\n――右田一酒造元の、その姿を。
- TW: 若是類比誕生之家這個詞彙的話，這就是我的養育之家——右田一釀酒廠。
- Cũ: Nếu dùng từ nhà đẻ, thì đây chính là nhà nuôi của tôi\n——hình dáng của xưởng rượu Migita System.
- Mới: Nếu dùng từ nhà đẻ, thì đây chính là nhà nuôi của tôi\n——hình dáng của xưởng rượu Migita Ichi.
- Lý do: Migita System→Migita Ichi (quyết định 19/11 #17; JP 右田一酒造元, TW 右田一釀酒廠). Pilot giữ theo docs cũ — quyết định mới thay thế.

### 1637 — monologue — meaning
- JP: ナビという物品。\x%lエアクラ;#00ffc040;エアクラ%l;#;・ナビ。\n\x%lエアクラ;#00ffc040;エアクラ%l;#;とともに急発展し、一般にまで普及した擬似知能。
- TW: 被我稱作Ｎａｖｉ的物品，全稱\x%lエアクラ;#00ffc040;空凝機%l;#;導航系統，是隨著\x%lエアクラ;#00ffc040;空凝機%l;#;的高速發展而廣為普及的人工智慧。
- Cũ: Vật phẩm mang tên Navi. \x%lエアクラ;#00ffc040;Aircra%l;#; Navi.\nTrí tuệ nhân tạo phát triển nhanh chóng cùng với \x%lエアクラ;#00ffc040;Aircra%l;#;, và đã trở nên phổ biến trong đại chúng.
- Mới: Vật phẩm mang tên Navi. \x%lエアクラ;#00ffc040;Aircra%l;#; Navi.\nTrí tuệ giả lập phát triển nhanh chóng cùng với \x%lエアクラ;#00ffc040;Aircra%l;#;, và đã trở nên phổ biến trong đại chúng.
- Lý do: Pilot giữ: 擬似知能=trí tuệ giả lập (không phải trí tuệ nhân tạo).

### 1647 — monologue — pronoun
- JP: なら、僕……生きてる……\n僕だけ……僕の、はんぶんは――
- TW: 這麼說，我……還活著……只有我……我的，另一半——
- Cũ: Vậy ra, mình……vẫn còn sống……\nChỉ có mình……còn, một nửa của mình——
- Mới: Vậy ra, tôi……vẫn còn sống……\nChỉ có tôi……một nửa của tôi——
- Lý do: Pilot giữ: mình→tôi (mặc định; độc thoại nhận ra mình còn sống — không phải tự vấn nên ngoại lệ mình không bắt buộc).

### 1652 — monologue — pronoun
- JP: それじゃあ、みちが――\n僕を、突き飛ばしてくれた[いもうと,1]路子が――
- TW: 那樣的話，路子——推開了我的[妹妹,1]路子不就——
- Cũ: Như thế thì, Michi——\nMichiko, đứa em gái đã đẩy mình ra sẽ——
- Mới: Thế thì, Michi——\nMichiko, đứa em gái đã đẩy tôi ra, sẽ——
- Lý do: Pilot giữ: mình→tôi; gọn dấu câu.

### 1659 — monologue — terminology
- JP: 着水し、ナビの\x%l翼端;#00ffc040;翼端%l;#;を歩いて渡り岸に下りれば――\n御一夜だ。
- TW: 降落後，只要從Ｎａｖｉ的\x%l翼端;#00ffc040;翼梢%l;#;走上岸，就算到御一夜了。
- Cũ: Hạ cánh xuống nước, đi bộ qua \x%l翼端;#00ffc040;đầu cánh%l;#; của Navi rồi bước lên bờ——\nlà Ohimitera.
- Mới: Hạ cánh xuống nước, đi bộ qua \x%l翼端;#00ffc040;đầu cánh%l;#; của Navi rồi bước lên bờ——\nlà Ohitoyo.
- Lý do: Ohimitera→Ohitoyo (quyết định 19/11; JP 御一夜).

## §3. Đối chiếu với bản pilot 19/11 (35 fix)

Pilot là bản nháp làm từ TOML-2 (giá trị đã bị làm phẳng `\n`). Kết quả đối chiếu sau khi đọc lại toàn bộ 155 dòng từ CSV3:

- **30 fix giữ nguyên** (996, 1000, 1004, 1009, 1012, 1023, 1041, 1047, 1160, 1166, 1168, 1185, 1217, 1260, 1262, 1308, 1329, 1337, 1397, 1398, 1404, 1434, 1438, 1440, 1450, 1457, 1601, 1637, 1647, 1652) — đã dựng lại từ giá trị CSV3 đầy đủ (giữ nguyên vị trí ngắt dòng), không sao chép nguyên văn bản pilot.
- **4 fix sửa lại / mở rộng:**
  - **1173 — sửa lại:** pilot đổi câu 2 thành mệnh lệnh ("Cứ để họ làm...") là lệch giọng. Bản audit bỏ "Hôm nay" (JP không có; TW thêm 今天 nhưng JP hơn TW) và giữ nguyên câu 2 của bản cũ theo TW ("Chắc chắn họ sẽ hoàn thành tốt công việc của mình" — TW: 她們一定會做好自己的工作的; JP やってるわ là khẳng định). JP cụt (không động từ) nhưng TW cho đủ căn cứ hoàn thiện — vẫn nên kiểm tra trong game nếu có dịp.
  - **1335 — mở rộng:** pilot chỉ sửa câu cuối ("mất toàn bộ toa xe"); audit thêm gloss 帝鉄貨物 "Đường sắt Hoàng gia"→"Đường sắt Đế quốc" (quyết định 19/11 #6). File 01 là file mở đầu game và đây là lần xuất hiện 帝鉄 duy nhất trong file → tooltip %l lần đầu dùng dạng đầy đủ.
  - **1430 — mở rộng (gộp pilot + sweep):** pilot sửa nghĩa (giảm tốc lại / tăng thêm); sweep thêm っ→Ư. Giá trị sweep gốc dùng bản cũ sai nghĩa nên bắt buộc phải gộp.
  - **1628 — mở rộng:** pilot chỉ sửa khoảng trắng sau "——"; audit thêm Ohimitera→Ohitoyo. Trong CSV3 vị trí đó là ký tự ngắt dòng nên không còn khoảng trắng để sửa.
- **1 fix bỏ — 992:** pilot sửa dấu chấm (54→55). Kiểm chứng lại: CSV3 đã có 55 dấu chấm, JP == VN — pilot chỉ sửa lỗi làm phẳng của TOML-2, không phải lỗi dịch. Đã bỏ khỏi danh sách.
- **13 fix mới** (pilot chưa phát hiện): 4 gasp từ sweep (1247, 1317, 1375, 1382 — 1430 đã gộp ở trên), 7 Ohitoyo (1278, 1224, 1352, 1551, 1359, 1659 + 1628 đã gộp), 2 Migita (1170, 1634 — pilot giữ theo docs cũ, quyết định #17 ngày 19/11 thay thế).

## §4. Giữ nguyên có chủ đích / phán đoán (không sửa, không tính uncertain)

- **1027 "phun cát dồn toa" — ĐÃ CHỐT (Hieu 20/11 02:03: "dịch sao thuần việt dễ hiểu nhất là ok"):** bỏ "dồn toa" → "Kiến nghị phun cát." — "dồn toa" không có trong JP (砂撒きを進言します) lẫn TW (建議放沙), chỉ có trong ví dụ mẫu của Hieu. Fix do parent bổ sung sau audit.
- **1326 "tôi" với Navi — đã xác minh:** "Tôi còn tưởng con bé..." — "con bé" ở ngôi thứ ba chứng minh người nghe là Navi, không phải Hibiki. Không sửa thành "anh". (Bẫy xác định người nghe — xem file 13 key 1898.)
- **Soutetsu "tôi" với Navi (1184, 1252, 1426) — đúng:** Navi gọi Soutetsu là 双鉄様 (kính ngữ), quan hệ trang trọng → "tôi".
- **1151/1152 "thằng bé" — giữ:** chỉ người lái tàu trẻ trong ngữ cảnh, không phải lỗi xưng hô.
- **1397 — giữ phần hoàn thiện theo bản cũ:** JP cụt (わたくしたちも、わたくしたちの), TW cũng cụt — phần hoàn thiện theo đúng bản cũ, không bịa thêm.
- **1421 — giữ:** JP cụt, bản cũ hoàn thiện theo TW (đã kiểm chứng).
- **996 / 1000 / 1004 / 1647 / 1652 "mình"→"tôi" — giữ theo pilot:** ngoại lệ "mình" chỉ CHO PHÉP trong độc thoại tự vấn cảm xúc, không bắt buộc; "tôi" là mặc định an toàn, không phải lỗi. (Câu hỏi mở số 3 của pilot — đã giải quyết.)
- **1335 gloss "Đường sắt Đế quốc" — phán đoán có ghi chú:** theo đúng quyết định #6 (dạng đầy đủ chỉ trong tooltip %l lần xuất hiện đầu tiên). File 02 (2182) và file 05 (8 dòng) dùng "Teitetsu" vì đó là các lần xuất hiện sau. Nếu đợt thống nhất quyết định chuẩn hóa toàn bộ gloss thành "Teitetsu" thì dòng này sẽ đổi theo.
- **Quy tắc xưng hô Soutetsu với Nagi (sửa đổi 20/11) — KHÔNG ẢNH HƯỞNG file này:** Nagi (凪) không xuất hiện trong file (0 dòng Character 凪, 0 lần nhắc trong JP/TW/VN); không có dòng Soutetsu nào nói với Nagi; không có fix nháp nào cần gỡ. Quy tắc đã cập nhật: "anh" với Hibiki, Michiko, Paulette, Reina, Fukami, Nagi; "tôi" với Hachiroku, Mayami, Minokasa, Navi.
- **1443 "A Di Đà Phật!!!" — giữ:** bản địa hóa 南無三, đúng quy tắc; っ ở đây nhấn mạnh gắn vào từ, không phải gasp.

## §5. Đối chiếu sweep っ-gasp

- Sweep có **5 mục** cho file này (1247, 1317, 1375, 1382, 1430 — đều raw-tsu). **4 mục áp nguyên giá trị sweep** (đã kiểm chứng từng giá trị với JP; chỉ chuyển sang dạng ngắt dòng của CSV3 — sweep lưu dạng làm phẳng). **1430 gộp** với fix nghĩa của pilot (xem §3).
- Quét toàn bộ **59 dòng JP có っ**: **không còn gasp nào bị sót**. Các trường hợp không phải gasp: 1238 おっと ("Ối chà." — một tiếng cảm thán, đã dịch đúng; tiền lệ file 12); 1443 っ nhấn mạnh gắn vào từ; 1308/1404/1434 っ cuối câu đã có trong fix nghĩa.
- Không có dòng っ đầu câu nào khác ngoài 1247; không có dòng bare-っ; không có っ sau ~/….

## §6. Lượt soát 2 + kiểm tra cơ học

- Lượt soát 2 (đọc lại toàn bộ 47 giá trị fix đối chiếu JP): **47/47 tái kiểm chứng, 0 bỏ, 0 sửa.** + 1 fix do parent bổ sung sau audit (1027, Hieu chốt 20/11) — kiểm chứng 1/1, tổng 48.
- Tương đồng thấp nhất: 0,59 (1166), 0,62 (1185), 0,60 (1308) — đều là viết lại toàn câu, đã kiểm từng từ theo JP (xem §2), không phải lỗi.
- Kiểm tra cơ học: mọi fix chỉ khác bản cũ ở chỗ cần sửa (đã kiểm bằng thay thế chuỗi có xác nhận từng vị trí); số lượng thẻ `%l` không đổi trên mọi dòng; cân bằng 「」 trên mọi dòng; không có ký tự xuống dòng thật trong giá trị fix.
- JSON: 47 mục, khóa là chuỗi, `old_vn`/`jp`/`tw` khớp CSV3 tuyệt đối.
- Khối TOML dưới đây: parse OK, 47 khóa, **0 sai lệch** giá trị so với JSON (so sánh chuỗi thô sau khi tomllib parse; khóa chuyển `int(k)` trước khi so).

## Kết bài

File 01 — file mở đầu của game — có **48/155 dòng sai (31,0%)**, nặng hơn mức trung bình 00_Common (~10%) vì đây là file pilot cũ: 30 lỗi pilot đã bắt đúng, nhưng 13 lỗi mới (chủ yếu thuật ngữ đã quyết định sau pilot: Ohitoyo 8, Migita 2, gasp 5) chỉ lộ ra khi đọc lại đầy đủ với bộ quy tắc hiện tại, + 1 fix 1027 do Hieu chốt sau audit. Không có lỗi cấu trúc (misaligned/rotation/contamination) — toàn bộ là lỗi nghĩa, xưng hô, thuật ngữ và gasp rải rác, đúng kiểu "lỗi dán rải rác" của dự án. Sau file này 00_Common đã kiểm tra xong toàn bộ; Ohitoyo trong 00_Common còn 0 (134/134 đã sửa — parent sửa: agent đếm ngược, file 15 đã sửa hết 15 dòng của nó). 1027 "phun cát dồn toa" đã chốt (Hieu 20/11 02:03): bỏ "dồn toa" → "Kiến nghị phun cát."

### Khối TOML (đã kiểm chứng parse)

```toml
[script]
"996" = "…………Sao mà buồn ngủ thế này——\\nRõ ràng lúc nãy tôi……vẫn còn đang……ngủ cơ mà…………"
"1000" = "……Không ổn rồi.\\nNhững gì tôi nghe thấy, chẳng hiểu gì cả."
"1004" = "……Máu chảy từ……đầu tôi.\\nVậy thì, cứ thế này——nhưng mà……………………"
"1009" = "……Trò chuyện với đồ vật.\\nHay có lẽ chỉ là độc thoại."
"1012" = "……Tôi nghe thấy tiếng ai đó.\\n……Cảm nhận được……bàn tay……ai đó đang……lay tôi."
"1023" = "「Đã rõ, \\x%l制動;#00ffc040;hãm phanh%l;#;. Với tốc độ này thì \\x%l非常;#00ffc040;phanh khẩn cấp%l;#; là không thể——nhỉ.」"
"1027" = "「\\x%l粘着力;#00ffc040;Lực bám đường%l;#; đang sụt giảm nghiêm trọng.\\nKiến nghị phun cát.」"
"1041" = "「……Cứ thế này nữa sẽ bị \\x%l滑走;#00ffc040;trượt bánh%l;#; mất.\\nĐến giới hạn rồi. Lực hãm phanh không đủ.」"
"1047" = "「……Hết cách rồi.\\nTôi đã không muốn làm chậm việc \\x%l接続;#00ffc040;kết nối chuyển tàu%l;#; ở Shizuoka đâu.」"
"1160" = "「Không, là lật tàu! \\x%l脱線転覆;#00ffc040;Trật bánh lật tàu%l;#;!!\\nNhưng thế này vẫn còn tốt hơn nhiều so với tất cả cùng chết!!」"
"1166" = "「Quý khách đã ngồi vào chỗ ổn cả chưa ạ.」"
"1168" = "「Ừ, trước khi hạ cánh xuống nước thì nhìn từ trên cao một lượt vậy.」"
"1170" = "「Tôi hiểu rồi. Sắp tới điểm đến là xưởng rượu Migita Ichi.\\nNgài có muốn bay qua không phận một lần không?」"
"1173" = "「Là bộ đôi \\x%l車掌;#00ffc040;trưởng tàu%l;#; Seki và \\x%l車販;#00ffc040;nhân viên bán hàng%l;#; Mayuzumi mà nhỉ?\\nHọ đang làm đấy. Chắc chắn họ sẽ hoàn thành tốt công việc của mình.」"
"1185" = "「Làm thôi! Đây là công việc cả đời mới có một lần đấy!」"
"1217" = "「Ngoài việc dừng lại ra——.\\nVậy thì, làm ngược lại!」"
"1224" = "「Ra là vậy. Vì thế nên Ohitoyo mới suy thoái,\\nvà câu chuyện thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mới được đưa ra bàn tán sao?」"
"1247" = "「Ư! ——Xin hãy dùng \\x%l制動;#00ffc040;hãm phanh%l;#; tối đa.\\nTôi sẽ hỗ trợ để không bị \\x%l滑走;#00ffc040;trượt bánh%l;#;.」"
"1260" = "「Việc phán đoán trong mâu thuẫn đòi hỏi năng lực tính toán rất lớn,\\nvà gánh nặng đó sẽ đe dọa sự an toàn của ngài Soutetsu…… Ngài Soutetsu?」"
"1262" = "「Ở đây! Không rơi! Không rơi đâu!」"
"1278" = "「Đã rõ mệnh lệnh.\\nXin báo cáo những thay đổi của thành phố Ohitoyo trong cùng khoảng thời gian.」"
"1308" = "「Vì tôi chẳng muốn biến một Navi xuất sắc như cô\\nthành kẻ địch đâu.」"
"1317" = "「Chắc rắc xuống cái là bị cuốn trôi đi ngay thôi.\\nNhưng mà, có làm còn hơn không——Ư」"
"1329" = "「Vâng. Là con gái của ngài ấy.\\nNhưng nghe nói năng lực hành chính thì không được di truyền.」"
"1335" = "「Báo cáo sự cố tình trạng chưa xác định. \\x%l発報;#00ffc040;Phát tín hiệu báo động%l;#; từ \\x%lレイルロオド;#00ffc040;Railord%l;#; 9642.\\n\\x%l帝鉄貨物;#00ffc040;Vận tải hàng hóa Đường sắt Đế quốc%l;#;. \\x%l編成;#00ffc040;Đoàn tàu%l;#; mười lăm toa. Có khả năng mất toàn bộ toa xe.」"
"1337" = "「Chuyến tàu này đã không còn cách dừng lại. Dù có dùng lực \\x%l制動;#00ffc040;hãm phanh%l;#; tối đa một cách hợp lý nhất…… 75 giây sau, cũng không dừng hẳn được mà——」"
"1352" = "「Thế mà ngài Soutetsu lại nói,\\nkhông muốn thu hút nhà máy sản xuất những vật phẩm tiện lợi đó về Ohitoyo.」"
"1359" = "「Không thể không mong muốn họ xây dựng nó ở nơi khác ngoài Ohitoyo.\\nBởi vì nơi này, là quê hương thứ hai của tôi.」"
"1375" = "「Tôi sẽ lập tức kết nối \\x%l共感;#00ffc040;cộng cảm%l;#; với \\x%lレイルロオド;#00ffc040;Railord%l;#; phía trước để thông báo việc chậm trễ\\n——Ư!? Gì cơ!? Hả? Xin hãy nhắc lại!?」"
"1382" = "「Tiếp tục \\x%l制動;#00ffc040;hãm phanh%l;#;.\\n——Thêm chút nữa——áp suất, thêm một chút nữa thôi——Ư!!!」"
"1397" = "「Nói cũng phải.\\nChúng ta cũng phải làm tốt công việc của mình.」"
"1398" = "「Báo cáo đi. Phương pháp gì cơ? Báo cáo chậm một giây thôi là\\nnguy hiểm tiến gần thêm bao nhiêu mét, cô biết rõ mà.」"
"1404" = "「Trên tàu còn có hành khách đấy, dù không thể cũng phải dừng lại!!\\nGiảm tốc lại! Cô chủ đạo đi!!」"
"1430" = "「Đã rõ, giảm tốc lại. \\x%l圧;#00ffc040;Áp suất%l;#; hãm phanh, tăng thêm——Ư!」"
"1434" = "「Vậy thì phải làm sao đây!!」"
"1438" = "「Thế thì cách khác! Tìm cách khác ngoài việc dừng tàu đi!\\nCách gì cũng được! Mục tiêu là tránh bị rơi xuống!!!」"
"1440" = "「Tất nhiên rồi!\\nNhưng mà——phải đưa đến bệnh viện càng sớm càng tốt.」"
"1450" = "「Hinai à, là con gái thị trưởng tiền nhiệm sao?」"
"1457" = "「\\x%lレイルロオド;#00ffc040;Railord%l;#; 9642 truyền đạt qua \\x%l共感;#00ffc040;cộng cảm%l;#; lúc hấp hối rằng 『Cầu sắt sập』.\\n……Cầu sắt Fujikawa đã sập.」"
"1551" = "Nên ánh mắt tôi lập tức bắt lấy——dải sáng lấp lánh chảy dưới tầm mắt.\\nCon sông Kuma, biểu tượng của Ohitoyo, phản chiếu rực rỡ ánh mặt trời."
"1592" = "Nhìn từ trên cao, quang cảnh thành phố Ohitoyo\\ncó vẻ như chẳng hề thay đổi so với lúc tôi rời đi."
"1601" = "Ngay lập tức lấy lại tư thế thân máy, nhưng không thay đổi đường bay."
"1628" = "Và lúc này, Ohitoyo——\\nthành phố trải dài dưới tầm mắt kia, cũng đã từng cứu rỗi tôi."
"1634" = "Nếu dùng từ nhà đẻ, thì đây chính là nhà nuôi của tôi\\n——hình dáng của xưởng rượu Migita Ichi."
"1637" = "Vật phẩm mang tên Navi. \\x%lエアクラ;#00ffc040;Aircra%l;#; Navi.\\nTrí tuệ giả lập phát triển nhanh chóng cùng với \\x%lエアクラ;#00ffc040;Aircra%l;#;, và đã trở nên phổ biến trong đại chúng."
"1647" = "Vậy ra, tôi……vẫn còn sống……\\nChỉ có tôi……một nửa của tôi——"
"1652" = "Thế thì, Michi——\\nMichiko, đứa em gái đã đẩy tôi ra, sẽ——"
"1659" = "Hạ cánh xuống nước, đi bộ qua \\x%l翼端;#00ffc040;đầu cánh%l;#; của Navi rồi bước lên bờ——\\nlà Ohitoyo."```
