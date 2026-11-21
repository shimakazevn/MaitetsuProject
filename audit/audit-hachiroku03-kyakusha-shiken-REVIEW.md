# Audit — ハチロク03_客車試験.txt.toml

- File: `ハチロク03_客車試験.txt.toml` — route 01_Hachiroku, 436 dòng script (174 độc thoại, 65 thoại Fukami, 58 thoại Soutetsu, 42 thoại Paulette, 36 thoại Hachiroku, 33 thoại Nagi, 20 thoại Reina, 8 thoại Hibiki).
- Nội dung: buổi chạy thử toa hành khách — chụp ảnh lưu niệm trước giờ khởi hành, kiểm tra lò hơi/buồng lửa, khởi hành đúng giờ, Fukami làm quen với Paulette/Reina, giải thích quán tính, khói lò sưởi chảy ngược vào toa do đốt không hoàn toàn + gió trên cao, phanh khẩn cấp, Hachiroku giải thích bằng hộp khăn giấy/nam châm, kết bằng phương án chắn khói (deflector) và quạt máy.
- **Kết quả: 68/436 dòng sai (15,6%)** — đọc đủ từng dòng đối chiếu JP + TW. (Hợp nhất hai audit độc lập cùng file: audit này 60 dòng + 8 dòng của agent đồng thời chạy song song; xem §5.)

## §1. Kiểm tra cấu trúc

- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (436 dòng, 0 khóa trùng, 0 ô VN trống, 0 VN==TW); TOML 436 khóa script, khớp CSV3 (434 khớp tuyệt đối + 2 dòng 2297/2293 chỉ khác ở chỗ TOML giữ ký tự `\n` dạng text còn CSV3 có khoảng trắng — cùng hiện tượng làm phẳng đã biết, ngược chiều, nội dung dịch giống hệt, không phải lỗi). `[selections]` rỗng, `[info]` rỗng, `[characters]` 7, `[character_subs]` 7.
- TOML md5 `4e3b8dd9bce01b0a9339b80ba75190b4`; BOM + CRLF; không có bản sao file này (md5 duy nhất trong toàn bộ 227 file — không thuộc 11 nhóm trùng).
- Nhiễm chéo kiểm tra máy: 0 dòng VN đặc trưng (≥25 ký tự) trong file này trùng với dòng VN ở file khác mà JP khác; 1 trùng duy nhất là 2146 「Cuối cùng cũng đến lúc rồi nhỉ.」 = 日々姫04 2186 — JP hai bên đều là 「いよいよ、ですね」, cùng bản dịch đúng, không phải nhiễm. Trong file chỉ có VN trùng lặp hợp lệ: 「Ừm.」 ×3 (1865, 1815, 1385 — đều là JP 「うん」/「うむ」).
- Sweep gasp: sweep có đúng 1 mục cho file này (1780) — đã nhận; 9 mục “ハチロク03” còn lại thuộc file ハチロク03_冥国式レイルロオド (file khác, đã gộp xong), không phải file này.
- **日ノ本: 0 dòng trong file này.** 10 dòng “Hinamoto” thuộc file ハチロク03_冥国式レイルロオド (đã gộp, chờ đợt thống nhất) — không phải file này; ghi chú giao việc nhầm lẫn hai file cùng tiền tố ハチロク03.
- Soutetsu: “tôi” 15 lần trong thoại — 11 sửa thành “anh” (với Paulette/Reina/Fukami/Nagi), 4 dòng giữ “tôi” vì là địa chỉ nhóm (2011, 2090, 1988, 2149 — tiền lệ Paulette 14 key 1544); độc thoại “tôi” toàn file, 0 lần “mình” làm chủ ngữ độc lập (3048 “hơn mình nghĩ” là mệnh đề phụ, 2973/2605/2637 là sở hữu/phản thân — giữ theo tiền lệ).
- Paulette tự xưng theo người nghe (tiền lệ Paulette 13): “em” với Soutetsu (4 dòng sửa: 1695, 1696, 1854, 2182), “tôi” ở ngữ cảnh công việc/hội đồng (1913 giữ — xem §5), “chị” với Fukami/Reina (2029 đúng), “chúng tôi”/“bọn chị” cho nhóm nữ (1966, 2165, 1841 đúng). Paulette gọi Soutetsu “anh Soutetsu” (1978, 1789, 2180 — đúng khóa B4).
- Fukami: độc thoại 31 dòng xưng “em” → chuẩn hoá “mình”; 2 dòng đã đúng “mình” sẵn (2705, 2933); “chúng em” 2793 giữ (nhóm Fukami+Nagi). Thoại: “em” với người lớn, “tớ” với Nagi (2219) — đúng. Nagi: “tớ” với Fukami đúng (1716, 1793); 1919 sửa “tớ”→“em” (nói với Soutetsu).
- Hachiroku tự xưng “em” nhất quán; Reina tự xưng tên mình “Reina” nhất quán; Hibiki tự xưng “em”, gọi Soutetsu “anh hai”.
- CSV3 có vài ký tự hiển thị lỗi (���) ở cột JP/TW của 1938/2837 — chỉ là lỗi hiển thị khi trích xuất; đã đối chiếu TOML, nội dung VN không bị ảnh hưởng (3010 “d���n” trong CSV3, TOML ghi đúng “dồn”; 2646 “thì��—” trong CSV3, TOML ghi đúng “thì——”).

## §2. Danh sách sửa (68 dòng)

Phân loại: xưng hô 49 (độc thoại Fukami “em”→“mình” 31 — gồm 2696 kiêm thuật ngữ; Soutetsu “tôi”→“anh” 11; Paulette “tôi”→“em” với Soutetsu 4; “Bọn chị”→“Bọn tôi” 1934, “chúng em”→“chúng tôi” 2113, Nagi “tớ”→“em” 1919), thuật ngữ 9 (Ohitoyo 4, Yunoi 3, túi công tác 1, thân vận hành 1 — gồm 2696), sai nghĩa 6, gasp 2, SFX 2, thẻ %l 1.

**Key 94 [monologue] — thuật ngữ.** JP: `\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;が、いつもよりずっしり重く感じる。\\nが、それを姿に出してはいかん。` / TW: `\\x%l乗務鞄;#00ffc040;乘務包%l;#;似乎比以往更加沉重。但我斷然不能這樣表現出來。` — Cũ: `Chiếc \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; có vẻ nặng trĩu hơn mọi khi.\\nNhưng tôi không được để lộ điều đó ra ngoài.` → Mới: `Chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;#; có vẻ nặng trĩu hơn mọi khi.\\nNhưng tôi không được để lộ điều đó ra ngoài.`. (乗務鞄 = “túi công tác” (quyết 20/11; tiền lệ hachiroku09 運転鞄→“túi công tác” trong audit).)

**Key 102 [monologue] — xưng hô.** JP: `\\x%l汽笛;#00ffc040;汽笛%l;#;がなって、\\nクって、スピードがあがったような気がします。` / TW: `\\x%l汽笛;#00ffc040;汽笛%l;#;鳴響，感覺列車好像“刷”地一下子加速了。` — Cũ: `Tiếng \\x%l汽笛;#00ffc040;còi hơi nước%l;#; vang lên,\\nvà em cảm giác như tàu vừa tăng tốc một cái "vút".` → Mới: `Tiếng \\x%l汽笛;#00ffc040;còi hơi nước%l;#; vang lên,\\nvà mình cảm giác như tàu vừa tăng tốc một cái "vút".`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 1355 [双鉄] — thẻ %l.** JP: `「[カマ,1]火床の状態は良さそうだな」` / TW: `「[窯,1]火床的狀態好像不錯啊」` — Cũ: `「Tình trạng của \\x%lカマ;#00ffc040;buồng lửa%l;#; có vẻ tốt đấy.」` → Mới: `「Tình trạng của buồng lửa có vẻ tốt đấy.」`. (JP chỉ có ruby [カマ,1] trên 火床, không có thẻ %l; VN tự thêm thẻ gloss — gỡ thẻ, giữ chữ “buồng lửa” (tiền lệ saiketsu 2288).)

**Key 1369 [双鉄] — sai nghĩa.** JP: `「\\x%l客車;#00ffc040;客車%l;#;。\\n……\\x%l列車;#00ffc040;列車%l;#;か」` / TW: `「\\x%l客車;#00ffc040;客運車廂%l;#;……\\x%l列車;#00ffc040;列車%l;#;啊」` — Cũ: `「\\x%l客車;#00ffc040;Toa hành khách%l;#;.\\n……\\x%l列車;#00ffc040;Tàu%l;#; sao.」` → Mới: `「\\x%l客車;#00ffc040;Toa hành khách%l;#;.\\n……\\x%l列車;#00ffc040;Tàu%l;#; à.」`. (か cuối câu là câu hỏi tu từ/ngẫm nghĩ (“một đoàn tàu đấy à”), không phải “sao” (= tại sao); “Tàu sao.” đọc thành câu hỏi nguyên nhân — sai nghĩa.)

**Key 1683 [ポーレット] — thuật ngữ.** JP: `「そうだとしても、試験運転中に倒れさせたのは私の、\\n御一夜鉄道株式会社の責任です」` / TW: `「不管怎麼說，在試乘時出現這種情況，都是我以及御一夜鐵路股份公司的責任」` — Cũ: `「Dù là vậy, việc để em bị ngất trong lúc chạy thử nghiệm là trách nhiệm của chị,\\ncủa Công ty Cổ phần Đường sắt Ohito.」` → Mới: `「Dù là vậy, việc để em bị ngất trong lúc chạy thử nghiệm là trách nhiệm của chị,\\ncủa Công ty Cổ phần Đường sắt Ohitoyo.」`. (御一夜 = “Ohitoyo” (quyết 19/11).)

**Key 1695 [ポーレット] — xưng hô.** JP: `「わかりました。それならわたし、関連資料を」` / TW: `「了解。那我也去查一下相關的資料」` — Cũ: `「Tôi hiểu rồi. Vậy thì tôi sẽ đi tìm tài liệu liên quan.」` → Mới: `「Em hiểu rồi. Vậy thì em sẽ đi tìm tài liệu liên quan.」`. (Paulette tự xưng “em” với Soutetsu (quy tắc theo người nghe; tiền lệ Paulette 13: “tôi” ở hội đồng, “em” với Soutetsu, “chị” với Reina).)

**Key 1696 [ポーレット] — xưng hô.** JP: `「わかりました」` / TW: `「了解」` — Cũ: `「Tôi hiểu rồi.」` → Mới: `「Em hiểu rồi.」`. (Paulette tự xưng “em” với Soutetsu (xem 1695; đáp Soutetsu 1887).)

**Key 1737 [ふかみ] — sai nghĩa.** JP: `「ええと……わたし、お母さんも、ノド、強くないから。\\nそれでちょっと――おおげさになっちゃっただけ。です」` / TW: `「其實，我媽媽的喉嚨也不太好。所以我才——有點反應過度了。嗯」` — Cũ: `「Ừm…… mẹ em, cũng có cổ họng, không được khỏe.\\nNên em mới hơi——làm quá lên một chút thôi. Ạ.」` → Mới: `「Ừm…… mẹ em cũng yếu cổ họng.\\nNên em mới hơi——làm quá lên một chút thôi. Ạ.」`. (ノド、強くない = cổ họng yếu; VN cũ “cũng có cổ họng, không được khỏe” dịch sai cấu trúc JP.)

**Key 1780 [ふかみ] — gasp.** JP: `「っ！！？」` / TW: `「呃！！？」` — Cũ: `「っ!!?」` → Mới: `「Ư!!?」`. (Sweep gasp (raw-tsu): っ thô trong VN → “Ư” (tiền lệ Hachiroku 12 Tái phát triển 2103/2537).)

**Key 1808 [双鉄] — xưng hô.** JP: `「っと、うっかりしていた。\\n送ったほうが――」` / TW: `「哦，差點忘了。我送你回去吧？」` — Cũ: `「À, tôi quên mất.\\nĐể tôi đưa em về——」` → Mới: `「À, anh quên mất.\\nĐể anh đưa em về——」`. (Soutetsu xưng “anh” với Fukami (quy tắc đã sửa 20/11).)

**Key 1809 [ふかみ] — sai nghĩa.** JP: `「そ、そんな。わたしなんて――\\nぜんぜん、まだまだ駆け出しですし……です」` / TW: `「哪、哪裡。我才只是……剛剛上手……而已」` — Cũ: `「Kh, không đâu ạ. Em chỉ là——\\nvẫn còn, còn non nớt lắm…… ạ.」` → Mới: `「Không… không đâu ạ. Em chỉ là——\\nvẫn còn, còn non nớt lắm…… ạ.」`. (“Kh” không có cơ sở JP (không có っ; quy tắc “Kh” khóa chỉ dùng cho っ); そ、そんな chỉ là lắp bắp “không đâu”.)

**Key 1812 [双鉄] — xưng hô.** JP: `「いや、こちらこそ乗ってくれてありがとう」` / TW: `「哪裡，我該謝你肯來試乘才對」` — Cũ: `「Không, tôi mới là người phải cảm ơn em vì đã đi cùng.」` → Mới: `「Không, anh mới là người phải cảm ơn em vì đã đi cùng.」`. (Soutetsu xưng “anh” với Fukami (quy tắc đã sửa 20/11).)

**Key 1825 [ふかみ] — gasp.** JP: `「あ……はっ――はぁあっ」` / TW: `「啊……哈……哈……」` — Cũ: `「A…… ha——haaa」` → Mới: `「A…… ha——haaaƯ」`. (はぁあっ cuối dòng tuyệt đối, không dấu câu sau — っ mất hẳn → thêm “Ư” (quy tắc gasp 20/11; はっ—— trước đó giữ “ha——” vì dấu —— đã diễn tả tiếng ngắt).)

**Key 1854 [ポーレット] — xưng hô.** JP: `「あ――嬉しいですけど、\\n時間、大丈夫なんですか？」` / TW: `「啊，拍照倒是很開心啦，不過時間還來得及嗎？」` — Cũ: `「A——Tôi vui lắm, nhưng mà\\nthời gian có ổn không vậy?」` → Mới: `「A——Em vui lắm, nhưng mà\\nthời gian có ổn không vậy?」`. (Paulette tự xưng “em” với Soutetsu (xem 1695).)

**Key 1862 [れいな] — SFX.** JP: `「すやぁあ……むにゃぁあ」` / TW: `「嗚…呣…」` — Cũ: `「Khòòò…… khòòò」` → Mới: `「Khòòò…… Munyaaa」`. (むにゃぁあ là tiếng lẩm bẩm trong lúc ngủ, không phải ngáy; “Khò” chỉ giữ cho すやぁあ (tiền lệ 00common05 giữ “Khò” cho すやぁ). Hai âm JP khác nhau không được gộp thành một.)

**Key 1879 [双鉄] — xưng hô.** JP: `「うむ……もっともだな。返す言葉も無い」` / TW: `「嗯，有道理，我無言以對」` — Cũ: `「Ừm…… cậu nói đúng. Tôi không còn lời nào để cãi.」` → Mới: `「Ừm…… em nói đúng. Anh không còn lời nào để cãi.」`. (Soutetsu xưng “anh”, gọi Nagi “em” (quy tắc đã sửa 20/11; “cậu” sai người nghe — Nagi là bé gái, tiền lệ hibiki08 2730 “xin lỗi em”).)

**Key 1887 [双鉄] — xưng hô.** JP: `「ああ、ふたりには専門家としてのチェックを頼みたい」` / TW: `「嗯，麻煩兩位以專業的角度來檢查了」` — Cũ: `「Ừ, tôi muốn nhờ hai người kiểm tra với tư cách là chuyên gia.」` → Mới: `「Ừ, anh muốn nhờ hai người kiểm tra với tư cách là chuyên gia.」`. (Soutetsu xưng “anh” với Paulette + Reina (1966) (quy tắc đã sửa 20/11).)

**Key 1919 [凪] — xưng hô.** JP: `「ぜーんぜん気づかんかったばい」` / TW: `「完全沒注意到耶」` — Cũ: `「Tớ hoàn toàn không để ý luôn á.」` → Mới: `「Em hoàn toàn không để ý luôn á.」`. (Nagi xưng “em” với người lớn (tiền lệ hibiki08); “tớ” chỉ dùng với Fukami — đây Nagi đáp Soutetsu (1723).)

**Key 1934 [ハチロク] — xưng hô.** JP: `「ごめんなさい、日々姫。\\nうっかりと話し込んでしまいました」` / TW: `「對不起，日日姬。不小心聊得興起了」` — Cũ: `「Xin lỗi em nhé, Hibiki.\\nBọn chị lỡ mải nói chuyện quá.」` → Mới: `「Xin lỗi em nhé, Hibiki.\\nBọn tôi lỡ mải nói chuyện quá.」`. (“Bọn chị” sai — nhóm gồm Hachiroku + Soutetsu (nam, 1836 Hibiki: “Anh hai với Hachiroku lại đứng nói chuyện”); dạng nhóm trung tính là “Bọn tôi”.)

**Key 1986 [双鉄] — xưng hô.** JP: `「ポーレットとれいなの、専門家としての目だけでなく、\\n一般客に近い目からのレビューも欲しいと考えている」` / TW: `「我們認為，不能只有從波萊特和玲奈她們這樣專業的角度，也要有從貼近普通乘客的角度做出的評價」` — Cũ: `「Ngoài góc nhìn chuyên gia của Paulette và Reina,\\ntôi cũng muốn có những đánh giá từ góc nhìn gần với hành khách thông thường.」` → Mới: `「Ngoài góc nhìn chuyên gia của Paulette và Reina,\\nanh cũng muốn có những đánh giá từ góc nhìn gần với hành khách thông thường.」`. (Soutetsu xưng “anh” với Paulette + Reina (quy tắc đã sửa 20/11).)

**Key 1996 [双鉄] — xưng hô.** JP: `「だから、できれば緊張せず、\\n普通に楽しんで、感想を聞かせてもらえれば嬉しい」` / TW: `「所以儘量不要緊張，放鬆心情去享受，然後告訴我們感想，這樣就最好了」` — Cũ: `「Nên nếu được thì đừng căng thẳng,\\ncứ thoải mái tận hưởng rồi cho tôi biết cảm nhận nhé.」` → Mới: `「Nên nếu được thì đừng căng thẳng,\\ncứ thoải mái tận hưởng rồi cho anh biết cảm nhận nhé.」`. (Soutetsu xưng “anh” với Fukami (1905) (quy tắc đã sửa 20/11).)

**Key 2008 [ポーレット] — thuật ngữ.** JP: `「トンネルの中は絶対開けちゃダメって話だけど、\\n[ゆのい,1]湯医線の区間はほら、トンネルって一個も無いから」` / TW: `「按說隧道裡是絕對不能開窗的啦，不過你看湯醫線這個路段上，一條隧道也沒有」` — Cũ: `「Người ta bảo là tuyệt đối không được mở khi đi qua hầm,\\nnhưng em xem, tuyến Yui đâu có cái hầm nào.」` → Mới: `「Người ta bảo là tuyệt đối không được mở khi đi qua hầm,\\nnhưng em xem, tuyến Yunoi đâu có cái hầm nào.」`. (湯医/湯医線 = “Yunoi” (quyết 20/11; tiền lệ meikoku Yui→Yunoi trong audit).)

**Key 2012 [ハチロク] — thuật ngữ.** JP: `「どうせ撮られるのなら、\\x%l運転体;#00ffc040;運転体%l;#;で……\\n双鉄様と一緒のところが良いのですが」` / TW: `「既然要拍的話，那索性拍\\x%l運転体;#00ffc040;駕駛體%l;#;……和雙鐵少爺一起拍多好」` — Cũ: `「Đằng nào cũng bị chụp, thà chụp \\x%l運転体;#00ffc040;kíp lái%l;#;……\\nchụp chung với ngài Soutetsu thì tốt hơn ạ.」` → Mới: `「Đằng nào cũng bị chụp, thà chụp \\x%l運転体;#00ffc040;thân vận hành%l;#;……\\nchụp chung với ngài Soutetsu thì tốt hơn ạ.」`. (運転体 = “thân vận hành” (tiền lệ meikoku 1984; “kíp lái” sai — đó là thân thể, không phải kíp người).)

**Key 2021 [ふかみ] — sai nghĩa.** JP: `「ハチロクちゃんが。です、か？」` / TW: `「是八六準備的…嗎？」` — Cũ: `「Hachiroku. Chuẩn bị ạ?」` → Mới: `「Là Hachiroku chuẩn bị ạ?」`. (が đánh dấu Hachiroku là chủ ngữ (người chuẩn bị); VN cũ “Hachiroku. Chuẩn bị ạ?” rời rạc, mất nhấn mạnh chủ ngữ.)

**Key 2080 [双鉄] — xưng hô.** JP: `「準備をしすぎてしすぎるということもない。\\n撮ったら、すぐに戻るさ」` / TW: `「準備總歸是不管多充分都不嫌多的。拍完我就馬上回去繼續準備」` — Cũ: `「Chuẩn bị càng kỹ càng tốt mà.\\nChụp xong tôi sẽ quay lại làm việc ngay.」` → Mới: `「Chuẩn bị càng kỹ càng tốt mà.\\nChụp xong anh sẽ quay lại làm việc ngay.」`. (Soutetsu xưng “anh” với Paulette (1854 hỏi về giờ) (quy tắc đã sửa 20/11).)

**Key 2113 [ハチロク] — xưng hô.** JP: `「不完全燃焼が発生し、煙によって視界が大きく遮られ、\\nわたくしたちは、出力を上げ\\x%lカマ;#00ffc040;カマ%l;#;を活性化させました」` / TW: `「發生燃燒不充分的情況後產生的煙，嚴重遮蔽了視線，所以我們拉高了功率，讓\\x%lカマ;#00ffc040;窯%l;#;全力運轉」` — Cũ: `「Tình trạng cháy không hoàn toàn xảy ra, khói làm cản trở tầm nhìn nghiêm trọng,\\nnên chúng em đã tăng công suất để kích hoạt \\x%lカマ;#00ffc040;lò hơi%l;#; ạ.」` → Mới: `「Tình trạng cháy không hoàn toàn xảy ra, khói làm cản trở tầm nhìn nghiêm trọng,\\nnên chúng tôi đã tăng công suất để kích hoạt \\x%lカマ;#00ffc040;lò hơi%l;#; ạ.」`. (“chúng em” sai — nhóm làm máy gồm Hachiroku + Soutetsu (người lái, 3010 chính Soutetsu kéo van); dạng nhóm trung tính “chúng tôi”.)

**Key 2121 [双鉄] — xưng hô.** JP: `「すまなかったな。\\nこんなことになるとは夢にも思っていなかった」` / TW: `「真抱歉。我們無論如何都想不到會出這樣的情況」` — Cũ: `「Xin lỗi em nhé.\\nTôi không bao giờ ngờ tới chuyện này lại xảy ra.」` → Mới: `「Xin lỗi em nhé.\\nAnh không bao giờ ngờ tới chuyện này lại xảy ra.」`. (Soutetsu xưng “anh” với Fukami (quy tắc đã sửa 20/11).)

**Key 2174 [双鉄] — xưng hô.** JP: `「僕のおかげ――では全然無いがな」` / TW: `「託我的福嗎，這話真受之有愧啊」` — Cũ: `「Đâu phải nhờ tôi——chút nào đâu.」` → Mới: `「Đâu phải nhờ anh——chút nào đâu.」`. (Soutetsu xưng “anh” với Reina (2175) (quy tắc đã sửa 20/11).)

**Key 2182 [ポーレット] — xưng hô.** JP: `「そうでした。それじゃあわたしも、\\n今日のところは、無理しないように休みます」` / TW: `「說得沒錯。那我今天也就不勉強自己，好好休息嘍」` — Cũ: `「Đúng rồi nhỉ. Vậy thì tôi cũng,\\nsẽ không cố quá mà nghỉ ngơi cho hôm nay vậy.」` → Mới: `「Đúng rồi nhỉ. Vậy thì em cũng,\\nsẽ không cố quá mà nghỉ ngơi cho hôm nay vậy.」`. (Paulette tự xưng “em” với Soutetsu (xem 1695; đáp Soutetsu 2270).)

**Key 2221 [双鉄] — xưng hô.** JP: `「そこは、ハチロクのフォローもある。\\n二両も三両も、僕のやることに大差はない」` / TW: `「這個嘛，還有八六幫忙處理呢，兩輛三輛其實我要做的事情倒是沒多大區別」` — Cũ: `「Về khoản đó thì đã có Hachiroku hỗ trợ rồi.\\nNên hai toa hay ba toa thì những việc tôi phải làm cũng không khác nhau là mấy.」` → Mới: `「Về khoản đó thì đã có Hachiroku hỗ trợ rồi.\\nNên hai toa hay ba toa thì những việc anh phải làm cũng không khác nhau là mấy.」`. (Soutetsu xưng “anh” với Paulette (1978 hỏi) (quy tắc đã sửa 20/11).)

**Key 2270 [双鉄] — xưng hô.** JP: `「ふかみは“特に”無理の無いよう――といったぞ？\\n他のみんなにも、普通に無理はしてほしくないのだが」` / TW: `「雖然深美是“特別”要避免操勞，但其他人也請“正常地”避免操勞哦」` — Cũ: `「Tôi bảo Fukami là 'đặc biệt' đừng cố quá——rồi mà?\\nTôi cũng không muốn những người khác phải cố sức đâu.」` → Mới: `「Anh bảo Fukami là 'đặc biệt' đừng cố quá——rồi mà?\\nAnh cũng không muốn những người khác phải cố sức đâu.」`. (Soutetsu xưng “anh” với Paulette (tiếp 2225) (quy tắc đã sửa 20/11).)

**Key 2483 [monologue] — xưng hô.** JP: `そうだったんだ、って思います。` / TW: `仔細想想，還真是這樣。` — Cũ: `Ra là vậy, em nghĩ thầm.` → Mới: `Ra là vậy, mình nghĩ thầm.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2514 [monologue] — sai nghĩa.** JP: `ハチロクちゃんはお人形で、日々姫ちゃんは妹さんです。\\nだから……ひょっとして、もしかして――` / TW: `八六小姐是人偶，日日姬小姐是妹妹，那麼……或許，說不定……` — Cũ: `Hachiroku là búp bê, còn chị Hibiki là em gái.\\nVậy nên…… biết đâu, có lẽ nào——` → Mới: `Hachiroku là búp bê, còn Hibiki là em gái.\\nVậy nên…… biết đâu, có lẽ nào——`. (“chị Hibiki là em gái” mâu thuẫn trong một vế (chị... em gái); bỏ “chị”, giữ vai trò “em gái” (của Soutetsu) theo JP 妹さん.)

**Key 2559 [monologue] — xưng hô.** JP: `ダメって、言おうと――\\n窓なんて開けたら――って思って、けど――` / TW: `剛想說“不行”，如果窗開了的話，怕是……` — Cũ: `Không được, em định nói vậy——\\nMở cửa sổ ra thì——em nghĩ vậy, nhưng mà——` → Mới: `Không được, mình định nói vậy——\\nMở cửa sổ ra thì——mình nghĩ vậy, nhưng mà——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2577 [monologue] — xưng hô.** JP: `聞いてるだけで、胸までキイって苦しくて、\\nなんだか、どんどん怖くなります。` / TW: `只是聽著這聲音，胸口就不禁繃得難受，一股莫名的恐懼感漸漸湧上心頭。` — Cũ: `Chỉ nghe thôi mà ngực em cũng thắt lại đau đớn,\\nvà em bắt đầu cảm thấy ngày càng sợ hãi.` → Mới: `Chỉ nghe thôi mà ngực mình cũng thắt lại đau đớn,\\nvà mình bắt đầu cảm thấy ngày càng sợ hãi.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2587 [monologue] — xưng hô.** JP: `でも――わたしにはそれがどうしてかわからなくって、\\n鉄道のこと、あんまり知らない自分がもどかしくなります。` / TW: `可是，我卻陷入茫然，對此一頭霧水。我不禁有點痛恨對鐵路一無所知的自己。` — Cũ: `Nhưng mà——em lại không hiểu lý do vì sao,\\nthật bực bội với bản thân vì chẳng biết gì về đường sắt cả.` → Mới: `Nhưng mà——mình lại không hiểu lý do vì sao,\\nthật bực bội với bản thân vì chẳng biết gì về đường sắt cả.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2592 [monologue] — xưng hô.** JP: `こんなにちゃんとお話しするの初めてで、\\nポーレットさん、すごく、いいひとって思います。` / TW: `和小凪以外的人說這麼多話這還是頭一次。波萊特小姐，真是個相當好的人呢。` — Cũ: `Đây là lần đầu tiên em nói chuyện đàng hoàng thế này,\\nem thấy chị Paulette, thực sự, là một người rất tốt.` → Mới: `Đây là lần đầu tiên mình nói chuyện đàng hoàng thế này,\\nmình thấy chị Paulette, thực sự, là một người rất tốt.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2604 [monologue] — xưng hô.** JP: `偉くて、ちょっとこわい人かと思ってたから、\\n余計に、すごく、かわいいなぁって思います。` / TW: `因為之前我還以為她是那種高高在上又有點可怕的人，所以現在反而覺得她看起來更可愛了。` — Cũ: `Em cứ tưởng chị ấy là người có chức vụ cao nên sẽ hơi đáng sợ,\\nai dè lại thấy dễ thương cực kỳ luôn.` → Mới: `Mình cứ tưởng chị ấy là người có chức vụ cao nên sẽ hơi đáng sợ,\\nai dè lại thấy dễ thương cực kỳ luôn.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2617 [monologue] — sai nghĩa.** JP: `苦しい、です。\\n煙――すごく、イガイガってして――` / TW: `好…難受。煙，不停地強烈刺痛著喉嚨——` — Cũ: `Khó thở, quá.\\nKhói——cực kỳ, ngột ngạt——` → Mới: `Khó thở, quá.\\nKhói——cực kỳ, rát cổ——`. (イガイガ = cổ họng rát/khó chịu, không phải “ngột ngạt” (bí bách); “rát cổ” đúng nghĩa.)

**Key 2618 [monologue] — xưng hô.** JP: `ヘンなこと……まで……は、\\nなら、しゃべっちゃわなかったみたい――かな？` / TW: `好像……沒有把什麼更奇怪的話說出聲來吧……大概？` — Cũ: `Vậy là, những chuyện kỳ quặc……\\nchắc em chưa lỡ nói ra tiếng đâu——nhỉ?` → Mới: `Vậy là, những chuyện kỳ quặc……\\nchắc mình chưa lỡ nói ra tiếng đâu——nhỉ?`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2646 [monologue] — xưng hô.** JP: `凪ちゃんが来て、背中をとんとんしてくれます、けど――\\nこれ、煙……なくならないと――` / TW: `小凪轉過來，不停地拍我的後背。可是，這煙……如果不能散開的話——` — Cũ: `Nagi chạy đến, vỗ lưng cho em, nhưng mà——\\nCái này, khói…… nếu không hết thì——` → Mới: `Nagi chạy đến, vỗ lưng cho mình, nhưng mà——\\nCái này, khói…… nếu không hết thì——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2671 [monologue] — thuật ngữ.** JP: `九洲とはいえ御一夜は、冬には雪も降る土地だ。\\nその頃になら、きっとストーブも活躍しよう。` / TW: `御一夜雖說位於九州，但冬天還是會下雪的。那時這暖爐一定會大展身手的吧。` — Cũ: `Tuy ở Kyushu, nhưng Ohito lại là nơi có tuyết rơi vào mùa đông.\\nĐến lúc đó, chắc chắn cái bếp lò sưởi này sẽ phát huy tác dụng.` → Mới: `Tuy ở Kyushu, nhưng Ohitoyo lại là nơi có tuyết rơi vào mùa đông.\\nĐến lúc đó, chắc chắn cái bếp lò sưởi này sẽ phát huy tác dụng.`. (御一夜 = “Ohitoyo” (quyết 19/11).)

**Key 2696 [monologue] — thuật ngữ + xưng hô.** JP: `わたしも凪ちゃんもいっつもは、\\n湯医まで、この湯医線に乗って学園に通ってます。` / TW: `我和小凪平時都是到湯醫，乘坐列車經這條湯醫線去上學的。` — Cũ: `Cả em và Nagi bình thường,\\nđều đi học bằng cách bắt tuyến Yui này đến Yui.` → Mới: `Cả mình và Nagi bình thường,\\nđều đi học bằng cách bắt tuyến Yunoi này đến Yunoi.`. (湯医/湯医線 = “Yunoi” (quyết 20/11; tiền lệ meikoku Yui→Yunoi trong audit). Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2707 [monologue] — xưng hô.** JP: `双鉄さん――きっと、\\nポーレットさんの秘書になっちゃうって思ってました。` / TW: `我覺得，雙鐵先生一定會去做波萊特小姐的秘書。` — Cũ: `Anh Soutetsu——chắc chắn,\\nsẽ trở thành thư ký của chị Paulette, em đã nghĩ như vậy.` → Mới: `Anh Soutetsu——chắc chắn,\\nsẽ trở thành thư ký của chị Paulette, mình đã nghĩ như vậy.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2712 [monologue] — xưng hô.** JP: `だから……ああ、わかった――かもです。` / TW: `所以……哦，我大概，明白了。` — Cũ: `Cho nên…… à, em hiểu rồi——có lẽ vậy.` → Mới: `Cho nên…… à, mình hiểu rồi——có lẽ vậy.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2713 [monologue] — xưng hô.** JP: `だからスピードをあげてたくさん蒸気を使って、\\n蒸気をどんどん作れるようにしてるんだろうって思います。` / TW: `所以就要提高列車速度消耗大量蒸汽，來促使鍋爐產生更多的蒸汽。` — Cũ: `Nên em đoán họ đang tăng tốc để sử dụng nhiều hơi nước,\\ntừ đó kích thích tạo ra nhiều hơi nước hơn.` → Mới: `Nên mình đoán họ đang tăng tốc để sử dụng nhiều hơi nước,\\ntừ đó kích thích tạo ra nhiều hơi nước hơn.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2715 [monologue] — xưng hô.** JP: `だから、わたし。あのとき。\\n\\x%l8620;#00ffc040;8620%l;#;の修復のあと、みんなでどうするか相談したとき。` / TW: `所以說，在那時，\\x%l8620;#00ffc040;８６２０%l;#;修復完成後，大家討論接下來怎麼辦的時候。` — Cũ: `Cho nên, em. Lúc đó.\\nSau khi phục hồi \\x%l8620;#00ffc040;8620%l;#;, lúc mọi người bàn bạc xem nên làm gì tiếp theo.` → Mới: `Cho nên, mình. Lúc đó.\\nSau khi phục hồi \\x%l8620;#00ffc040;8620%l;#;, lúc mọi người bàn bạc xem nên làm gì tiếp theo.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2720 [monologue] — thuật ngữ.** JP: `ゆえ、\\x%l8620;#00ffc040;8620%l;#;-\\x%l客車;#00ffc040;客車%l;#;-\\x%lキハ07;#00ffc040;キハ07%l;#;と連結し、御一夜駅への戻りには、\\n\\x%lキハ07;#00ffc040;キハ07%l;#;に牽引をお願いすることとなる。` / TW: `所以，就有了\\x%l8620;#00ffc040;８６２０%l;#;－\\x%l客車;#00ffc040;客運車廂%l;#;－\\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;這樣的掛接形式，在返回御一夜站的時候就由\\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;來牽引。` — Cũ: `Do đó, chúng tôi nối thành \\x%l8620;#00ffc040;8620%l;#;-\\x%l客車;#00ffc040;toa hành khách%l;#;-\\x%lキハ07;#00ffc040;KiHa 07%l;#;, và lúc quay về ga Ohito,\\nsẽ nhờ \\x%lキハ07;#00ffc040;KiHa 07%l;#; kéo.` → Mới: `Do đó, chúng tôi nối thành \\x%l8620;#00ffc040;8620%l;#;-\\x%l客車;#00ffc040;toa hành khách%l;#;-\\x%lキハ07;#00ffc040;KiHa 07%l;#;, và lúc quay về ga Ohitoyo,\\nsẽ nhờ \\x%lキハ07;#00ffc040;KiHa 07%l;#; kéo.`. (御一夜 = “Ohitoyo” (quyết 19/11).)

**Key 2741 [monologue] — xưng hô.** JP: `真似して、広げて、ぱた、ぱた、ぱた。\\nわ――ほんとだ。これ、凄く涼しいです！` / TW: `於是我也跟著拉開衣服，啪嗒啪嗒地扇。哇，還真是涼快得很！` — Cũ: `Em cũng bắt chước kéo áo ra, rồi phành, phạch, phành, phạch.\\nOa——đúng thật này. Mát quá đi mất!` → Mới: `Mình cũng bắt chước kéo áo ra, rồi phành, phạch, phành, phạch.\\nOa——đúng thật này. Mát quá đi mất!`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2764 [monologue] — xưng hô.** JP: `声にあわせて両手をつかって説明をしてくれるから、\\nすごく、わかりやすいです。` / TW: `模仿聲音的同時，還以兩手做出連接的樣子說明，真的是非常通俗易懂。` — Cũ: `Nhờ hai chị vừa giải thích vừa dùng tay minh họa,\\nnên em rất dễ hiểu.` → Mới: `Nhờ hai chị vừa giải thích vừa dùng tay minh họa,\\nnên mình rất dễ hiểu.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2767 [monologue] — xưng hô.** JP: `思ってたよりもっと黒くて、まるで、雨雲が近くまで――\\nあ！　わかった。さっきの、“煙が低い”って。` / TW: `比我想像中更黑，簡直就像低垂的雨雲一般——啊，我明白了。剛才說“煙飄得低”就是這個意思啊。` — Cũ: `Đen hơn em tưởng, cứ như mây mưa kéo đến gần vậy——\\nA! Em hiểu rồi. Cái gọi là "khói bay thấp" lúc nãy.` → Mới: `Đen hơn mình tưởng, cứ như mây mưa kéo đến gần vậy——\\nA! Mình hiểu rồi. Cái gọi là "khói bay thấp" lúc nãy.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2792 [monologue] — xưng hô.** JP: `ポーレットさん、すごく優しくて話しやすくて……\\n今の感じなら、がんばって聞いちゃえそうって思います。` / TW: `波萊特小姐感覺很溫柔很好說話，照著現在的樣子，應該可以嘗試著打聽出來。` — Cũ: `Chị Paulette rất dịu dàng và dễ nói chuyện……\\nVới bầu không khí này, chắc em có thể mạnh dạn hỏi thử xem sao.` → Mới: `Chị Paulette rất dịu dàng và dễ nói chuyện……\\nVới bầu không khí này, chắc mình có thể mạnh dạn hỏi thử xem sao.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2810 [monologue] — thuật ngữ.** JP: `湯医駅には、\\x%l転車台;#00ffc040;転車台%l;#;が無い。` / TW: `湯醫站沒有\\x%l転車台;#00ffc040;轉車盤%l;#;。` — Cũ: `Ở ga Yui không có \\x%l転車台;#00ffc040;bàn quay đầu máy%l;#;.` → Mới: `Ở ga Yunoi không có \\x%l転車台;#00ffc040;bàn quay đầu máy%l;#;.`. (湯医/湯医線 = “Yunoi” (quyết 20/11; tiền lệ meikoku Yui→Yunoi trong audit).)

**Key 2813 [monologue] — xưng hô.** JP: `どうして凪ちゃんとお話するときみたいに、\\nすんなり出てきてくれないのか、いやになります。` / TW: `為什麼不能像和小凪說話時那樣，自然隨意地說出口呢，我討厭這樣。` — Cũ: `Sao em không thể nói chuyện trôi chảy như lúc nói chuyện với Nagi chứ,\\nthật đáng ghét.` → Mới: `Sao mình không thể nói chuyện trôi chảy như lúc nói chuyện với Nagi chứ,\\nthật đáng ghét.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2814 [monologue] — xưng hô.** JP: `息がしたくて、もっと楽になりたくて、\\n風の方、涼しい方へ――` / TW: `為能再多喘口氣，讓喉嚨更舒服一些，我向著風和涼爽的方向——` — Cũ: `Em muốn thở, muốn được dễ chịu hơn,\\nnên hướng về phía có gió, phía mát mẻ——` → Mới: `Mình muốn thở, muốn được dễ chịu hơn,\\nnên hướng về phía có gió, phía mát mẻ——`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2820 [monologue] — xưng hô.** JP: `しゃべれなくって、深呼吸して――\\n凪ちゃんの手が、背中、とんとんしてくれてます。` / TW: `無法開口說話，只能不住深呼吸。小凪不停地在用手拍我的後背，想讓我舒服一點。` — Cũ: `Không nói nên lời, em hít thở sâu——\\nBàn tay Nagi vẫn đang vỗ nhè nhẹ vào lưng em.` → Mới: `Không nói nên lời, mình hít thở sâu——\\nBàn tay Nagi vẫn đang vỗ nhè nhẹ vào lưng mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2837 [monologue] — xưng hô.** JP: `煙が低いってどういうことか、少しよくわからなくなって。\\nけどこのお話は、わからなくっても別にいいって思います。` / TW: `煙飄得低是個什麼概念，還是有點不太明白。不過這個話題好像不懂也問題不大的樣子。` — Cũ: `Khói bay thấp là sao nhỉ, em vẫn chưa hiểu lắm.\\nNhưng em nghĩ chuyện này không hiểu cũng chẳng sao.` → Mới: `Khói bay thấp là sao nhỉ, mình vẫn chưa hiểu lắm.\\nNhưng mình nghĩ chuyện này không hiểu cũng chẳng sao.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2842 [monologue] — xưng hô.** JP: `にこにこってして、れいなちゃんが頷いてくれます。` / TW: `玲奈仍然是滿臉笑意地點頭表示同意。` — Cũ: `Bé Reina cười tươi rạng rỡ gật đầu với em.` → Mới: `Bé Reina cười tươi rạng rỡ gật đầu với mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2896 [monologue] — xưng hô.** JP: `れいなちゃん、\\nすごくすっごくにこにこして、わたしに説明してくれます。` / TW: `而玲奈則是掛著掩不住開心的微笑，開始向我說明。` — Cũ: `Bé Reina,\\ncười tươi rạng rỡ, bắt đầu giải thích cho em hiểu.` → Mới: `Bé Reina,\\ncười tươi rạng rỡ, bắt đầu giải thích cho mình hiểu.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2901 [monologue] — xưng hô.** JP: `凪ちゃんがおもしろそうに言うから、\\nちょっと、不思議に思います。` / TW: `聽到小凪說“挺好玩兒的”，我覺得有些不可思議。` — Cũ: `Nghe Nagi nói có vẻ thích thú,\\nem cảm thấy hơi kỳ lạ.` → Mới: `Nghe Nagi nói có vẻ thích thú,\\nmình cảm thấy hơi kỳ lạ.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2903 [monologue] — xưng hô.** JP: `言われて、見てみて、ビックリ……してます。` / TW: `聽她們這麼一說，看了一眼，可嚇了我一大跳。` — Cũ: `Nghe gọi, em nhìn thử, và…… giật mình.` → Mới: `Nghe gọi, mình nhìn thử, và…… giật mình.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2904 [monologue] — xưng hô.** JP: `凪ちゃんのお話で、まとわりついてくる“重い煙”\\nって、不完全燃焼の煙なんだってわかりました。` / TW: `聽小凪這麼說，我明白了這些貼近過來的濃煙是因為燃燒不充分而產生的。` — Cũ: `Qua lời Nagi, em hiểu ra "khói đặc" đeo bám dai dẳng đó\\nchính là khói do cháy không hoàn toàn.` → Mới: `Qua lời Nagi, mình hiểu ra "khói đặc" đeo bám dai dẳng đó\\nchính là khói do cháy không hoàn toàn.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2931 [monologue] — xưng hô.** JP: `ポーレットさんに倒して、押さえてもらえてなかったら、\\nわたし、ぜったい、ころんで――きっと、怪我してました。` / TW: `要不是被波萊特小姐拉倒，按在身下，我肯定會摔倒——也肯定會受傷吧。` — Cũ: `Nếu không được chị Paulette kéo ngã và giữ chặt,\\nem chắc chắn, đã bị ngã——và chắc chắn, đã bị thương.` → Mới: `Nếu không được chị Paulette kéo ngã và giữ chặt,\\nmình chắc chắn, đã bị ngã——và chắc chắn, đã bị thương.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2941 [monologue] — xưng hô.** JP: `トンネルとか、乗ってても……\\n数どころか、あるか無いかも、全然気にしてなかったです。` / TW: `說起隧道，以我乘坐列車的經歷而言，別說有多少，就是有沒有進過，都完全沒有印象。` — Cũ: `Hầm đường sắt gì đó, dù có đi tàu……\\nthì em cũng chẳng để ý đến số lượng, hay thậm chí là có hay không nữa.` → Mới: `Hầm đường sắt gì đó, dù có đi tàu……\\nthì mình cũng chẳng để ý đến số lượng, hay thậm chí là có hay không nữa.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2967 [monologue] — xưng hô.** JP: `どうしてかなって、不思議に思って。すごく思って。\\nわたし、いっぱい考えました。` / TW: `這是為什麼呢，我想不明白，完全不能理解。哪怕想破頭，也還是搞不懂。` — Cũ: `Em cứ tự hỏi tại sao, thấy thật khó hiểu. Rất khó hiểu.\\nEm, đã suy nghĩ rất nhiều.` → Mới: `Mình cứ tự hỏi tại sao, thấy thật khó hiểu. Rất khó hiểu.\\nMình, đã suy nghĩ rất nhiều.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2972 [monologue] — xưng hô.** JP: `褒められるのって、なれなくて、苦手……\\nだけど、やっぱり、嬉しいです。` / TW: `還是不太習慣，被表揚。不過雖然不習慣，但心裡還是高興的。` — Cũ: `Việc được khen ngợi, em vẫn chưa quen, cũng không giỏi ứng phó……\\nNhưng mà, quả nhiên là vẫn thấy vui.` → Mới: `Việc được khen ngợi, mình vẫn chưa quen, cũng không giỏi ứng phó……\\nNhưng mà, quả nhiên là vẫn thấy vui.`. (Độc thoại của Fukami: tự xưng “mình” (quy tắc đã quyết; tiền lệ 凪ふかみ02/04).)

**Key 2979 [monologue] — thuật ngữ.** JP: `扇風機を使える\\x%l客車;#00ffc040;客車%l;#;なら、\\nこれほど夏の御一夜に、似合い、ありがたいものも無い。` / TW: `配有風扇的\\x%l客車;#00ffc040;客運車廂%l;#;，沒有比這個更適合夏天的御一夜、更讓人感激的了。` — Cũ: `Nếu là một \\x%l客車;#00ffc040;toa hành khách%l;#; có thể dùng được quạt máy,\\nthì không gì phù hợp và đáng quý hơn cho mùa hè ở Ohito.` → Mới: `Nếu là một \\x%l客車;#00ffc040;toa hành khách%l;#; có thể dùng được quạt máy,\\nthì không gì phù hợp và đáng quý hơn cho mùa hè ở Ohitoyo.`. (御一夜 = “Ohitoyo” (quyết 19/11).)

**Key 3014 [monologue] — SFX.** JP: `（――ぐんっ）` / TW: `（——轟）` — Cũ: `（——Vù）` → Mới: `（——Vụt）`. (ぐんっ cuối dòng tuyệt đối — âm dừng bị mất; “Vụt” giữ lại tiếng dừng bằng phụ âm cuối “t” (như ちゅっ→“Chụt”).)

## §3. Khối TOML (đã parse-kiểm chứng: 68 khóa, 0 sai lệch giá trị)

```toml
[script]
"94" = "Chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;#; có vẻ nặng trĩu hơn mọi khi.\\nNhưng tôi không được để lộ điều đó ra ngoài."
"102" = "Tiếng \\x%l汽笛;#00ffc040;còi hơi nước%l;#; vang lên,\\nvà mình cảm giác như tàu vừa tăng tốc một cái \"vút\"."
"1355" = "「Tình trạng của buồng lửa có vẻ tốt đấy.」"
"1369" = "「\\x%l客車;#00ffc040;Toa hành khách%l;#;.\\n……\\x%l列車;#00ffc040;Tàu%l;#; à.」"
"1683" = "「Dù là vậy, việc để em bị ngất trong lúc chạy thử nghiệm là trách nhiệm của chị,\\ncủa Công ty Cổ phần Đường sắt Ohitoyo.」"
"1695" = "「Em hiểu rồi. Vậy thì em sẽ đi tìm tài liệu liên quan.」"
"1696" = "「Em hiểu rồi.」"
"1737" = "「Ừm…… mẹ em cũng yếu cổ họng.\\nNên em mới hơi——làm quá lên một chút thôi. Ạ.」"
"1780" = "「Ư!!?」"
"1808" = "「À, anh quên mất.\\nĐể anh đưa em về——」"
"1809" = "「Không… không đâu ạ. Em chỉ là——\\nvẫn còn, còn non nớt lắm…… ạ.」"
"1812" = "「Không, anh mới là người phải cảm ơn em vì đã đi cùng.」"
"1825" = "「A…… ha——haaaƯ」"
"1854" = "「A——Em vui lắm, nhưng mà\\nthời gian có ổn không vậy?」"
"1862" = "「Khòòò…… Munyaaa」"
"1879" = "「Ừm…… em nói đúng. Anh không còn lời nào để cãi.」"
"1887" = "「Ừ, anh muốn nhờ hai người kiểm tra với tư cách là chuyên gia.」"
"1919" = "「Em hoàn toàn không để ý luôn á.」"
"1934" = "「Xin lỗi em nhé, Hibiki.\\nBọn tôi lỡ mải nói chuyện quá.」"
"1986" = "「Ngoài góc nhìn chuyên gia của Paulette và Reina,\\nanh cũng muốn có những đánh giá từ góc nhìn gần với hành khách thông thường.」"
"1996" = "「Nên nếu được thì đừng căng thẳng,\\ncứ thoải mái tận hưởng rồi cho anh biết cảm nhận nhé.」"
"2008" = "「Người ta bảo là tuyệt đối không được mở khi đi qua hầm,\\nnhưng em xem, tuyến Yunoi đâu có cái hầm nào.」"
"2012" = "「Đằng nào cũng bị chụp, thà chụp \\x%l運転体;#00ffc040;thân vận hành%l;#;……\\nchụp chung với ngài Soutetsu thì tốt hơn ạ.」"
"2021" = "「Là Hachiroku chuẩn bị ạ?」"
"2080" = "「Chuẩn bị càng kỹ càng tốt mà.\\nChụp xong anh sẽ quay lại làm việc ngay.」"
"2113" = "「Tình trạng cháy không hoàn toàn xảy ra, khói làm cản trở tầm nhìn nghiêm trọng,\\nnên chúng tôi đã tăng công suất để kích hoạt \\x%lカマ;#00ffc040;lò hơi%l;#; ạ.」"
"2121" = "「Xin lỗi em nhé.\\nAnh không bao giờ ngờ tới chuyện này lại xảy ra.」"
"2174" = "「Đâu phải nhờ anh——chút nào đâu.」"
"2182" = "「Đúng rồi nhỉ. Vậy thì em cũng,\\nsẽ không cố quá mà nghỉ ngơi cho hôm nay vậy.」"
"2221" = "「Về khoản đó thì đã có Hachiroku hỗ trợ rồi.\\nNên hai toa hay ba toa thì những việc anh phải làm cũng không khác nhau là mấy.」"
"2270" = "「Anh bảo Fukami là 'đặc biệt' đừng cố quá——rồi mà?\\nAnh cũng không muốn những người khác phải cố sức đâu.」"
"2483" = "Ra là vậy, mình nghĩ thầm."
"2514" = "Hachiroku là búp bê, còn Hibiki là em gái.\\nVậy nên…… biết đâu, có lẽ nào——"
"2559" = "Không được, mình định nói vậy——\\nMở cửa sổ ra thì——mình nghĩ vậy, nhưng mà——"
"2577" = "Chỉ nghe thôi mà ngực mình cũng thắt lại đau đớn,\\nvà mình bắt đầu cảm thấy ngày càng sợ hãi."
"2587" = "Nhưng mà——mình lại không hiểu lý do vì sao,\\nthật bực bội với bản thân vì chẳng biết gì về đường sắt cả."
"2592" = "Đây là lần đầu tiên mình nói chuyện đàng hoàng thế này,\\nmình thấy chị Paulette, thực sự, là một người rất tốt."
"2604" = "Mình cứ tưởng chị ấy là người có chức vụ cao nên sẽ hơi đáng sợ,\\nai dè lại thấy dễ thương cực kỳ luôn."
"2617" = "Khó thở, quá.\\nKhói——cực kỳ, rát cổ——"
"2618" = "Vậy là, những chuyện kỳ quặc……\\nchắc mình chưa lỡ nói ra tiếng đâu——nhỉ?"
"2646" = "Nagi chạy đến, vỗ lưng cho mình, nhưng mà——\\nCái này, khói…… nếu không hết thì——"
"2671" = "Tuy ở Kyushu, nhưng Ohitoyo lại là nơi có tuyết rơi vào mùa đông.\\nĐến lúc đó, chắc chắn cái bếp lò sưởi này sẽ phát huy tác dụng."
"2696" = "Cả mình và Nagi bình thường,\\nđều đi học bằng cách bắt tuyến Yunoi này đến Yunoi."
"2707" = "Anh Soutetsu——chắc chắn,\\nsẽ trở thành thư ký của chị Paulette, mình đã nghĩ như vậy."
"2712" = "Cho nên…… à, mình hiểu rồi——có lẽ vậy."
"2713" = "Nên mình đoán họ đang tăng tốc để sử dụng nhiều hơi nước,\\ntừ đó kích thích tạo ra nhiều hơi nước hơn."
"2715" = "Cho nên, mình. Lúc đó.\\nSau khi phục hồi \\x%l8620;#00ffc040;8620%l;#;, lúc mọi người bàn bạc xem nên làm gì tiếp theo."
"2720" = "Do đó, chúng tôi nối thành \\x%l8620;#00ffc040;8620%l;#;-\\x%l客車;#00ffc040;toa hành khách%l;#;-\\x%lキハ07;#00ffc040;KiHa 07%l;#;, và lúc quay về ga Ohitoyo,\\nsẽ nhờ \\x%lキハ07;#00ffc040;KiHa 07%l;#; kéo."
"2741" = "Mình cũng bắt chước kéo áo ra, rồi phành, phạch, phành, phạch.\\nOa——đúng thật này. Mát quá đi mất!"
"2764" = "Nhờ hai chị vừa giải thích vừa dùng tay minh họa,\\nnên mình rất dễ hiểu."
"2767" = "Đen hơn mình tưởng, cứ như mây mưa kéo đến gần vậy——\\nA! Mình hiểu rồi. Cái gọi là \"khói bay thấp\" lúc nãy."
"2792" = "Chị Paulette rất dịu dàng và dễ nói chuyện……\\nVới bầu không khí này, chắc mình có thể mạnh dạn hỏi thử xem sao."
"2810" = "Ở ga Yunoi không có \\x%l転車台;#00ffc040;bàn quay đầu máy%l;#;."
"2813" = "Sao mình không thể nói chuyện trôi chảy như lúc nói chuyện với Nagi chứ,\\nthật đáng ghét."
"2814" = "Mình muốn thở, muốn được dễ chịu hơn,\\nnên hướng về phía có gió, phía mát mẻ——"
"2820" = "Không nói nên lời, mình hít thở sâu——\\nBàn tay Nagi vẫn đang vỗ nhè nhẹ vào lưng mình."
"2837" = "Khói bay thấp là sao nhỉ, mình vẫn chưa hiểu lắm.\\nNhưng mình nghĩ chuyện này không hiểu cũng chẳng sao."
"2842" = "Bé Reina cười tươi rạng rỡ gật đầu với mình."
"2896" = "Bé Reina,\\ncười tươi rạng rỡ, bắt đầu giải thích cho mình hiểu."
"2901" = "Nghe Nagi nói có vẻ thích thú,\\nmình cảm thấy hơi kỳ lạ."
"2903" = "Nghe gọi, mình nhìn thử, và…… giật mình."
"2904" = "Qua lời Nagi, mình hiểu ra \"khói đặc\" đeo bám dai dẳng đó\\nchính là khói do cháy không hoàn toàn."
"2931" = "Nếu không được chị Paulette kéo ngã và giữ chặt,\\nmình chắc chắn, đã bị ngã——và chắc chắn, đã bị thương."
"2941" = "Hầm đường sắt gì đó, dù có đi tàu……\\nthì mình cũng chẳng để ý đến số lượng, hay thậm chí là có hay không nữa."
"2967" = "Mình cứ tự hỏi tại sao, thấy thật khó hiểu. Rất khó hiểu.\\nMình, đã suy nghĩ rất nhiều."
"2972" = "Việc được khen ngợi, mình vẫn chưa quen, cũng không giỏi ứng phó……\\nNhưng mà, quả nhiên là vẫn thấy vui."
"2979" = "Nếu là một \\x%l客車;#00ffc040;toa hành khách%l;#; có thể dùng được quạt máy,\\nthì không gì phù hợp và đáng quý hơn cho mùa hè ở Ohitoyo."
"3014" = "（——Vụt）"
```

## §4. Lượt soát 2

- Đã đọc lại toàn bộ 68 giá trị fix đối chiếu JP (+TW khi cần): 68/68 đúng, 0 bỏ, 0 sửa lại (60 fix của audit này đã soát lần 2 đầy đủ; 8 fix nhận từ agent song song đã kiểm chứng lại từng dòng với JP trước khi nhận — xem §5). Kiểm chứng cơ học: JSON 68 mục dạng chuẩn, khóa chuỗi; khối TOML 68 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 68/68; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (đã kiểm tra diff từng dòng).

## §5. Ghi chú hợp nhất + đã kiểm tra và không tính sai / chờ Hieu

- **Trùng lặp audit:** file này bị audit song song bởi hai agent (một của loop, một của chat chính) — agent kia nộp trước với 25 dòng, ghi đè file JSON của audit này; audit này đã hợp nhất: giữ nguyên 60 fix của mình + nhận 8 fix đúng của agent kia (1369, 1695, 1696, 1854, 2021, 2182, 2514, 2617), 17 fix trùng khớp hoàn toàn. Hai chỗ khác nhau đã xử theo bằng chứng: **1737** giữ bản của audit này (“mẹ em cũng yếu cổ họng” — sát cấu trúc JP một vế; bản kia thêm một vế “cổ họng em không khỏe” mà JP không có); **2696** giữ bản của audit này (sửa cả Yui→Yunoi lẫn em→mình theo quy tắc độc thoại Fukami; bản kia chỉ sửa Yui). Một agent thứ ba cùng file vẫn đang chạy lúc hợp nhất — parent cần đối chiếu lại trước khi merge vào ROUTE-AUDIT.md.
- **1913** (Paulette: “Tôi muốn tìm cách nào đó—— mà không làm mất đi khả năng sử dụng bếp lò sưởi cơ.”): giữ “Tôi” — phát biểu ý kiến trong buổi thảo luận công việc trước cả nhóm (theo vế “tôi ở hội đồng” của quy tắc Paulette); nếu Hieu đọc thấy Paulette đang nói riêng với Soutetsu thì đổi thành “Em”.
- **1826** (Fukami: “Tớ…… không sao” + “cảm ơn cậu”): giữ nguyên — người nghe là Nagi (đang vỗ lưng cho Fukami, 2820), nên “Tớ”/“cậu” nhất quán với nhau; nếu Hieu đọc thấy Fukami đang đáp Paulette thì đổi thành “Em”/“cảm ơn chị”.
- **2149** (Soutetsu: “Có chuyện gì thì gọi tôi ngay”): giữ “tôi” — địa chỉ nhóm (nói với cả nhóm, dù nhấn mạnh Fukami); tiền lệ Paulette 14 key 1544.
- **2011 / 2090 / 1988**: giữ “tôi” — đều là địa chỉ nhóm (cả nhóm có mặt, gồm Hachiroku).
- **1777 / 1779 / 1801 / 1817 / 1818** (きゃっ！/わっ！？/おわあっ！？/うわっ！？): giữ nguyên, không thêm Ư — っ đi sau có dấu !/? nên không thuộc trường hợp “mất hẳn” theo quy tắc gasp đã khóa 20/11.
- **3043** （ザアっ）→ “(Soạt)”: giữ — phụ âm cuối “t” đã diễn tả っ (như ちゅっ→“Chụt”). **1935** “Nagi——”: giữ — hậu tố ちゃん vốn không dịch, dấu —— đã diễn tả tiếng ngắt. **1821** “A——a——”: giữ — っ được diễn tả bằng ——.
- **2793** “chúng em”: giữ — nhóm Fukami+Nagi, dạng số nhiều không thuộc quy tắc số ít. **2044/1353** “các em gái của em”: giữ — Hachiroku nói về các em gái dòng 8620.
- **94** (乗務鞄): đã sửa trong audit này theo tiền lệ hachiroku09; dòng này nằm trong 19 dòng chờ đợt thống nhất nên số còn lại cho đợt đó là 18.
- Không có câu hỏi thuật ngữ mới, không có JP cụt cần Hieu hoàn thiện.

## Kết bài

File ハチロク03_客車試験.txt.toml đã audit xong toàn bộ 436 dòng: **68 dòng sai (15,6%)** — 49 xưng hô (31 độc thoại Fukami “em”→“mình”, 11 Soutetsu “tôi”→“anh”, 4 Paulette “tôi”→“em” với Soutetsu, 3 nhóm/người nghe khác), 9 thuật ngữ (Ohitoyo 4, Yunoi 3, túi công tác 1, thân vận hành 1), 6 sai nghĩa, 2 gasp, 2 SFX, 1 thẻ %l. Không lệch dòng, không chuỗi xoay, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 68 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 68/68, 0 bỏ, 0 sửa. Không chắc chắn 0 dòng (2 dòng ghi chú 1826, 1913 — giữ nguyên, không đưa vào khối TOML).
