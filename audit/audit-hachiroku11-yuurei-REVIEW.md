# Audit — ハチロク11_幽霊.txt.toml (Hachiroku 11 — "Ghost")

**File:** `01_Hachiroku/ハチロク11_幽霊.txt.toml`  
**Đường dẫn:** `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af11_#U5e7d#U970a.txt.toml`  
**CSV3 master:** `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv`  
**MD5 TOML:** `82befe68e2f2df4ec7f0bf979bea9deb` (UTF-8 BOM + CRLF, 80.655 byte)  
**Ngày audit:** 22/11/2026

## Tổng kết

- **Số dòng đã đọc: 411 / 411** (toàn bộ file, đọc từng dòng đối chiếu JP + TW, không lấy mẫu).
- **Số dòng sai: 21** — tỷ lệ **5,1%** (21/411). Đây là một trong những file sạch nhất của route Hachiroku: không có lỗi misalignment, rotation, contamination, orphan, untranslated hay duplicate keys.
- **Phân loại:** đại từ nhân xưng 11 · hơi thở bị mất (sweep っ) 6 · sai nghĩa 1 · sai giới tính 1 · lỗi đánh máy 1 · SFX 1.
- **Cơ sở tổng:** 180 file / 8.111 dòng sai (đã kiểm chứng với ROUTE-AUDIT.md, dòng cuối). Sau file này: **181 file / 8.132 dòng sai**.
- **Second pass:** tổng 21 / đã kiểm tra lại 21 / loại bỏ 0 / sửa lại 0. Mọi fix đều là một thay thế liên tục duy nhất so với VN cũ (đã kiểm tra bằng diff máy).

## Phương pháp

Đọc toàn bộ 411 dòng theo thứ tự key, đối chiếu từng dòng VN với JP (chính) và TW (chứng thứ hai). Kiểm tra chéo sweep `sweep-raw-gasp-wrong.json` cho file này (6 mục, cả 6 đều đúng và đã nhận). Quét máy các mẫu っ cuối dòng để tìm gasp bị sót (không phát hiện thêm). Kiểm tra %l tag (cân bằng, không có tag hỏng trong file này), kiểm tra VN TOML vs CSV3 (40 khác biệt đều chỉ là flatten `\n`→khoảng trắng của TOML-2, không có khác biệt nội dung; CSV3 là nguồn chính xác cho fix). Xác định người nói / người được nói từ cột Character + 3–5 dòng lân cận (key không theo thứ tự truyện — các cảnh xen kẽ nhau).

## Kiểm tra cấu trúc

- **Misaligned / rotation:** 0. Không có dòng VN nào bị lệch sang key khác; không có chuỗi xoay vòng.
- **Contamination (lẫn file khác):** 0. Không có dòng VN nào thuộc về file khác (đã kiểm tra các dòng khả nghi như 2106/2109 về Michi — đúng ngữ cảnh file này).
- **Orphan (VN không có JP tương ứng):** 0.
- **Untranslated (VN trống / còn tiếng Trung):** 0. Cả 411 dòng đều có VN.
- **Duplicate keys:** 0 trong TOML và 0 trong CSV3. File này KHÔNG thuộc nhóm 11 file trùng lặp (chỉ có 1 bản trên đĩa).
- **%l tags:** tất cả cân bằng; không có tag hỏng, không có tag thừa do Gemini thêm vào trong file này.
- **Sweep っ:** file có 6 mục trong `sweep-raw-gasp-wrong.json`, cả 6 đều đúng (1393, 1718, 1873, 2092, 2135, 2183) và đã nhận hết. Quét bổ sung các dòng JP kết thúc bằng っ: 1773 (あっ――→"A——"), 1789 (はいっ――→"vâng——"), 1917 (双鉄様っ――→"Ngài Soutetsu——") đều đã render đúng theo quy tắc gasp boundary (không thêm Ư) — không có gasp nào bị sót.

## Đại từ nhân xưng (Soutetsu "anh"→"tôi" với Hachiroku; khóa B4 Paulette) (11 dòng)

### Key 1377 — monologue

- **JP:** “逃げ出すように”――と、そんな言葉が、\\n頭をよぎってしまいます。
- **TW:** “就像是逃走一樣”——這樣一句話，不禁浮現在我的腦海裡。
- **VN cũ:** "Như thể đang chạy trốn"——những từ đó,\\nchợt xẹt qua trong tâm trí em.
- **Fix:** "Như thể đang chạy trốn"——những từ đó,\\nchợt xẹt qua trong tâm trí tôi.

### Key 1405 — 双鉄

- **JP:** 「なんだとはご挨拶だな。\\nすまんが、少し場所を借りたい」
- **TW:** 「“什麼嘛”可不算打招呼啊。不好意思，我想借地方坐一下」
- **VN cũ:** 「"Gì vậy" không phải là một câu chào đâu nhé.\\nXin lỗi, nhưng cho anh mượn chỗ một lát.」
- **Fix:** 「"Gì vậy" không phải là một câu chào đâu nhé.\\nXin lỗi, nhưng cho tôi mượn chỗ một lát.」

### Key 1652 — 双鉄

- **JP:** 「……ともかく、茶でも淹れよう。少し待て」
- **TW:** 「不管怎樣，先喝口茶吧。稍等我一下」
- **VN cũ:** 「……Dù sao thì, anh sẽ pha chút trà nhé. Chờ một lát.」
- **Fix:** 「……Dù sao thì, tôi sẽ pha chút trà nhé. Chờ một lát.」

### Key 1810 — 双鉄

- **JP:** 「うん。僕は？」
- **TW:** 「嗯，我怎麼？」
- **VN cũ:** 「Ừm. Anh thì sao?」
- **Fix:** 「Ừm. Tôi thì sao?」

### Key 1926 — 双鉄

- **JP:** 「僕は、お前を嫌ったりしない。\\nむしろ、とても強い好意を変わらず、抱いているよ」
- **TW:** 「我完全沒有討厭你。相反，應該說一直對你有著強烈的好感才對」
- **VN cũ:** 「Anh, không hề ghét em.\\nNgược lại, anh vẫn luôn dành cho em một tình cảm vô cùng mãnh liệt.」
- **Fix:** 「Tôi, không hề ghét em.\\nNgược lại, tôi vẫn luôn dành cho em một tình cảm vô cùng mãnh liệt.」

### Key 1930 — 双鉄

- **JP:** 「僕は、お前と話をしたいよ」
- **TW:** 「我想和你好好聊一聊」
- **VN cũ:** 「Anh, muốn nói chuyện với em.」
- **Fix:** 「Tôi, muốn nói chuyện với em.」

### Key 1932 — 双鉄

- **JP:** 「聞かせて欲しい。お前の、声を」
- **TW:** 「我想要聽聽你的聲音」
- **VN cũ:** 「Anh muốn được nghe. Giọng nói, của em.」
- **Fix:** 「Tôi muốn được nghe. Giọng nói, của em.」

### Key 1980 — 双鉄

- **JP:** 「了解だ。ならばレールショップに戻ろう」
- **TW:** 「明白了。那回鐵路商店裡說吧」
- **VN cũ:** 「Anh hiểu rồi. Vậy thì chúng ta quay lại Rail Shop thôi.」
- **Fix:** 「Tôi hiểu rồi. Vậy thì chúng ta quay lại Rail Shop thôi.」

### Key 1986 — 双鉄

- **JP:** 「ああ。お前といれば楽しいし。\\n笑顔をみれば、もっと喜ばせてやりたくもなる」
- **TW:** 「是啊。和你在一起很開心。看到你的笑容，就不禁想讓你更開心一些」
- **VN cũ:** 「Đúng vậy. Ở bên em rất vui.\\nNhìn thấy nụ cười của em, anh lại càng muốn làm em vui hơn nữa.」
- **Fix:** 「Đúng vậy. Ở bên em rất vui.\\nNhìn thấy nụ cười của em, tôi lại càng muốn làm em vui hơn nữa.」

### Key 2131 — 双鉄

- **JP:** 「そうか。ならば、そうさせてもらうかもしれん」
- **TW:** 「這樣啊。那我們就恭敬不如從命了」
- **VN cũ:** 「Vậy sao. Nếu vậy, có lẽ tôi sẽ làm theo lời cô.」
- **Fix:** 「Vậy sao. Nếu vậy, có lẽ tôi sẽ làm theo lời em.」

### Key 2163 — ポーレット

- **JP:** 「双鉄くん。\\n手が空いたら、少し時間いいですか？」
- **TW:** 「雙鐵君，手頭有空的話，可以借一步說話嗎？」
- **VN cũ:** 「Cậu Soutetsu.\\nNếu rảnh tay, cho tôi xin chút thời gian được không?」
- **Fix:** 「Anh Soutetsu.\\nNếu rảnh tay, cho tôi xin chút thời gian được không?」

## Hơi thở / tiếng nấc bị mất (sweep っ) (6 dòng)

### Key 1393 — 双鉄

- **JP:** 「――っ」
- **TW:** 「——唔」
- **VN cũ:** 「——」
- **Fix:** 「——Ư」

### Key 1718 — 双鉄

- **JP:** 「どうしたっていうんだろうな？　――っ」
- **TW:** 「到底怎麼了呀——啊」
- **VN cũ:** 「Rốt cuộc là em ấy bị sao vậy nhỉ? ——」
- **Fix:** 「Rốt cuộc là em ấy bị sao vậy nhỉ? ——Ư」

### Key 1873 — 双鉄

- **JP:** 「幽霊の幽は、訓読みでは『かすか』。\\n亡霊の亡は、訓読みでは『ない』だ。つまり――っ！？」
- **TW:** 「幽靈的幽字，訓讀通“微”。而亡靈的亡字，訓讀通“無”。也就是說——啊！？」
- **VN cũ:** 「Chữ U (幽) trong U linh, âm Kun đọc là 'kasuka' (mờ ảo). \\nChữ Vong (亡) trong Vong linh, âm Kun đọc là 'nai' (không còn). Tức là——!?」
- **Fix:** 「Chữ U (幽) trong U linh, âm Kun đọc là 'kasuka' (mờ ảo). \\nChữ Vong (亡) trong Vong linh, âm Kun đọc là 'nai' (không còn). Tức là——Ư!?」

### Key 2092 — 双鉄

- **JP:** 「何をバカな――っ！」
- **TW:** 「說什麼傻——呃！」
- **VN cũ:** 「Em nói ngốc nghếch gì——!」
- **Fix:** 「Em nói ngốc nghếch gì——Ư!」

### Key 2135 — ハチロク

- **JP:** 「っ！」
- **TW:** 「這！」
- **VN cũ:** 「!」
- **Fix:** 「Ư!」

### Key 2183 — 双鉄

- **JP:** 「っ！！？」
- **TW:** 「！！？」
- **VN cũ:** 「!!?」
- **Fix:** 「Ư!!?」

## Sai nghĩa (1 dòng)

### Key 1903 — 技工

- **JP:** 「――キミにも、迷惑をかけてしまったかな。\\n右田さん、どうも気を使ってくれてたみたいだし」
- **TW:** 「想必也給你添了麻煩吧。我看右田先生，最近似乎是在顧及我的感受」
- **VN cũ:** 「——Có lẽ tôi cũng đã làm phiền cô rồi.\\nCậu Migita, có vẻ như đã rất để tâm đến chuyện đó.」
- **Fix:** 「——Có lẽ tôi cũng đã làm phiền cô rồi.\\nCậu Migita, hình như cũng đã để ý đến cảm nhận của tôi nhiều lắm.」

## Sai giới tính nhân vật được nhắc tới (1 dòng)

### Key 2006 — ハチロク

- **JP:** 「はい。ご主人はただの一目で、\\nわたくしの不調を心因性とお見抜きになられました」
- **TW:** 「是的。老闆她可是一眼就看出我的問題是由心理原因引起的」
- **VN cũ:** 「Vâng. Ông chủ chỉ cần nhìn thoáng qua,\\nđã nhận ra sự bất ổn của em là do tâm lý.」
- **Fix:** 「Vâng. Bà chủ chỉ cần nhìn thoáng qua,\\nđã nhận ra sự bất ổn của em là do tâm lý.」

## Lỗi đánh máy / cắt từ (1 dòng)

### Key 2015 — れいな

- **JP:** 「いらっしゃいませー、って、なぁんだそうてつさん。\\n忘れ物ですかぁ？」
- **TW:** 「歡迎光臨。咦，什麼嘛，原來是雙鐵先生。是忘了什麼東西嗎?」
- **VN cũ:** 「Kính chào quý khá——ơ, gì vậy, là anh Soutetsu à.\\nAnh để quên đồ sao ạ?」
- **Fix:** 「Kính chào quý kh——ơ, gì vậy, là anh Soutetsu à.\\nAnh để quên đồ sao ạ?」

## SFX — tiếng cười (1 dòng)

### Key 2827 — monologue

- **JP:** うふふと微笑み、軽く手を振り、\\nポーレットが機関庫へとひとり向かっていく。
- **TW:** 輕笑著向我們揮了揮手後，波萊特轉身一個人朝著機車庫走去。
- **VN cũ:** Mỉm cười "ư fufu", khẽ vẫy tay,\\nPaulette một mình đi về phía xưởng đầu máy.
- **Fix:** Mỉm cười "Ufufu", khẽ vẫy tay,\\nPaulette một mình đi về phía xưởng đầu máy.

## Lý do từng fix (tóm tắt)

- **Key 1377:** Độc thoại của Soutetsu (JP 頭をよぎってしまいます; TW 我的腦海裡 = "trong đầu TÔI"). VN cũ viết "trong tâm trí em" — gán suy nghĩ của Soutetsu sang Hachiroku, sai người.
- **Key 1393:** Sweep lost-gasp-trailing: JP 「――っ」, TW 「——唔」. VN cũ chỉ giữ dấu gạch, mất tiếng nấc っ → thêm Ư (quy tắc gasp: âm っ sẽ mất hoàn toàn nếu không render).
- **Key 1405:** Soutetsu nói với Hachiroku (cảnh liền trước 1394 Hachiroku cảm ơn lời khuyên). Theo quy tắc đã sửa: Soutetsu là "tôi" với Hachiroku, không phải "anh".
- **Key 1652:** Soutetsu nói với Hachiroku hoặc với 技工 Koharu — cả hai trường hợp đều không thuộc danh sách "anh" (Hibiki/Michiko/Paulette/Reina/Fukami/Nagi) → "tôi".
- **Key 1718:** Sweep lost-gasp-trailing: JP 「どうしたっていうんだろうな？　――っ」, TW "——啊". VN cũ mất っ → thêm Ư.
- **Key 1810:** Soutetsu hỏi Hachiroku/技工 (không có Paulette/Reina/Fukami/Nagi trong cảnh) → "tôi" (quy tắc đại từ đã sửa).
- **Key 1873:** Sweep lost-gasp-trailing: JP つまり――っ！？, TW "——啊！？" → "Tức là——Ư!?" (giữ nguyên dấu !?).
- **Key 1903:** 技工 Koharu nói với Hachiroku (右田さん được nhắc ở ngôi thứ ba → người nghe là Hachiroku). JP 気を使ってくれてた = Soutetsu đã để ý/quan tâm (đối tượng là Koharu — くれる chỉ hướng về người nói; TW: 顧及我的感受). VN cũ "đã rất để tâm đến chuyện đó" đổi đối tượng thành "chuyện đó", mất hướng người → sửa theo TW.
- **Key 1926:** Soutetsu nói với Hachiroku (お前). Cả hai "anh" trong dòng đều là tự xưng của Soutetsu → "tôi".
- **Key 1930:** Soutetsu nói với Hachiroku (お前と話をしたいよ) → "tôi".
- **Key 1932:** Soutetsu nói với Hachiroku (お前の、声を) → "tôi".
- **Key 1980:** Soutetsu nói với Hachiroku (quay lại Rail Shop cùng nhau) → "tôi".
- **Key 1986:** Soutetsu nói với Hachiroku (お前といれば楽しいし) → "tôi".
- **Key 2006:** ご主人 ở đây là bà chủ nhà tắm (vợ của 雲山 / nữ chủ): TW viết rõ 老闆她 (nữ); cùng file key 2750 VN đã dùng "bà chủ" cho cùng nhân vật này; 2011 雲山 nói "như lời vợ tôi nói". VN cũ "Ông chủ" sai giới tính → "Bà chủ". (Lưu ý: key 2706/2811 登呂流湯のご主人 là ông chủ nam — khác người, giữ nguyên.)
- **Key 2015:** Reina đang chào khách thì ngắt lời (いらっしゃいませー、って). VN cũ "quý khá" là lỗi đánh máy — "quý khách" bị cắt dở phải là "quý kh——".
- **Key 2092:** Sweep lost-gasp-trailing: JP 「何をバカな――っ！」, TW "——呃！" → thêm Ư.
- **Key 2131:** Soutetsu đáp lại lời Hachiroku ở key 2130 ("Vô luận, những thứ tầm đó thì" — cô ấy trấn an). "そうさせてもらう" = để cô ấy làm theo ý cô ấy → người nghe là Hachiroku → "lời em", không phải "lời cô".
- **Key 2135:** Sweep lost-gasp-whole: JP 「っ！", TW 「這！" — cả dòng chỉ là tiếng nấc → "Ư!".
- **Key 2163:** Paulette nói với Soutetsu: JP 双鉄くん. Theo khóa B4, 双鉄くん từ Paulette render "anh Soutetsu" (không phải "Cậu Soutetsu").
- **Key 2183:** Sweep lost-gasp-whole: JP 「っ！！？" → "Ư!!?".
- **Key 2827:** Tiếng cười うふふ của Paulette. Tiền lệ dự án: tiếng cười render "Fufu"/"Ufufu". VN cũ "ư fufu" trộn hai cách render trong một dòng → "Ufufu" (một dòng = một cách render).

## Các mục để vào unification pass (KHÔNG sửa trong audit này)

- **Key 2370:** 日ノ本 → VN đang viết "Hinamoto" — theo quyết định 20/11 phải là "Hinomoto" (đã có trong danh sách unification: ハチロク11 ×1).
- **Key 2184:** gloss %l của 列車 đang là "chuyến tàu" — theo quyết định 21/11 ~18:55, gloss 列車 → "đoàn tàu" (quét trong unification; riêng 真闇02 1113 đã sửa trong audit).
- **Key 1814:** 帝大 → VN đang viết "Đại học Hoàng gia" — thuật ngữ đã chốt là "Đại học Đế quốc" (unification: các biến thể 帝大).
- **Key 2701:** gloss %l của 機関士 đang là "người lái tàu" (key 2184 dùng "lái tàu") — thống nhất gloss trong unification (dạng rút gọn đã chốt là "lái tàu"; dạng đầy đủ "thợ lái đầu máy").

## Các điểm đã xem xét và GIỮ NGUYÊN (judgement calls)

- **Key 2431** (monologue): 恐らくは、そうしかけていたことに気づいて — chủ ngữ của 気づいて không nói rõ. VN "Có lẽ là do em ấy nhận ra mình vừa định làm như vậy" (Hachiroku tự nhận ra → lưng cứng lại) hợp logic cảnh (cô ấy sắp tựa vào lưng Soutetsu trong bồn tắm) và nối nhân quả tốt hơn cách đọc TW (Soutetsu nhận ra). Giữ VN.
- **Key 2559, 2701** (monologue của Hachiroku): "giữa chúng em" / "chúng em vẫn là người lái tàu và Railord" — cặp Hachiroku + Soutetsu. Đây là giọng kể của Hachiroku (cô tự xưng "em"); "chúng em" là dạng nhóm từ góc nhìn của người kể, không vi phạm quy tắc nhóm ("bọn tôi" trung tính chỉ áp dụng cho ngữ cảnh trang trọng/nhóm). Giữ VN.
- **Key 2678** (monologue): "Sâu hơn nữa——dành cho em gái em" — đã xác minh đây là độc thoại của Hachiroku (cô đang trình danh sách linh kiện cho ông Fuchi, key 2608; "em gái" là em gái Railord mà cô nhắc ở key 2625 わたくしの優しい妹). "em gái em" đúng với giọng Hachiroku; không phải Soutetsu nói về Michi.
- **Key 2809** (monologue): 一瞬、唇が結ばれる — VN "tôi mím chặt môi" (Soutetsu). TW gán cho Hachiroku (八六咬了咬嘴唇), nhưng dòng chảy 2797–2798–2810 đều là độc thoại Soutetsu đang giải thích chữ Hán ("tôi đột nhiên hiểu ra" ở 2810). Giữ VN theo JP + dòng chảy; JP không nói rõ chủ ngữ nên đây là điểm TW/JP không hoàn toàn khớp.
- **Key 1774:** Soutetsu nói "xin lỗi bà. Cháu xin nhận ý tốt này ạ" — "bà" là bà chủ nhà tắm (người mời họ tắm; Hachiroku cũng xin lỗi bà ở key 1770). Giữ nguyên.
- **Key 1805, 2136, 2139, 2178:** Soutetsu xưng "cháu" / gọi "ông" với ông chủ nhà tắm, ông Fuchi, vị trụ trì — phù hợp tiền lệ "tôi"/"cháu" với người lớn tuổi (file 09 key 2760, Minokasa). Giữ nguyên.
- **Key 1903/2064/2096:** 技工 Koharu gọi Hachiroku là "cô" — nhất quán trong cả file (3 lần) và phù hợp cách Koharu xưng hô tôn trọng ハチロクさん với Railord số hiệu đầu tiên. Chỉ sửa câu thứ hai của 1903 (sai nghĩa), giữ "cô".
- **Key 2190:** きゃっ → "Á" — đây KHÔNG phải cảnh H (hai người giật mình va vào nhau), quy tắc romaji ひゃ-family chỉ áp dụng cho tiếng rên trong cảnh H. Giữ "Á".
- **Key 1773/1789/1917:** các っ đã được render (あっ――→"A——", はいっ――→"vâng——", 双鉄様っ――→"Ngài Soutetsu——") theo đúng quy tắc gasp boundary — không thêm Ư. Giữ nguyên.
- **Key 1823/1919:** "Bọn cháu" / "Chúng cháu" — Soutetsu + Hachiroku nói với người lớn tuổi (ông chủ, 技工); dạng nhóm kính trọng, giữ nguyên.

## Khối TOML (đã kiểm chứng parse)

Khối dưới đây đã được parse bằng `tomllib`: 21 key, 0 sai lệch giá trị so với JSON. Lưu ý: `\\n` trong khối là ký tự backslash-n thực (giống CSV3), `tomllib` parse lại thành đúng giá trị fix.

```toml
[script]
1377 = "\"Như thể đang chạy trốn\"——những từ đó,\\nchợt xẹt qua trong tâm trí tôi."
1393 = "「——Ư」"
1405 = "「\"Gì vậy\" không phải là một câu chào đâu nhé.\\nXin lỗi, nhưng cho tôi mượn chỗ một lát.」"
1652 = "「……Dù sao thì, tôi sẽ pha chút trà nhé. Chờ một lát.」"
1718 = "「Rốt cuộc là em ấy bị sao vậy nhỉ? ——Ư」"
1810 = "「Ừm. Tôi thì sao?」"
1873 = "「Chữ U (幽) trong U linh, âm Kun đọc là 'kasuka' (mờ ảo). \\nChữ Vong (亡) trong Vong linh, âm Kun đọc là 'nai' (không còn). Tức là——Ư!?」"
1903 = "「——Có lẽ tôi cũng đã làm phiền cô rồi.\\nCậu Migita, hình như cũng đã để ý đến cảm nhận của tôi nhiều lắm.」"
1926 = "「Tôi, không hề ghét em.\\nNgược lại, tôi vẫn luôn dành cho em một tình cảm vô cùng mãnh liệt.」"
1930 = "「Tôi, muốn nói chuyện với em.」"
1932 = "「Tôi muốn được nghe. Giọng nói, của em.」"
1980 = "「Tôi hiểu rồi. Vậy thì chúng ta quay lại Rail Shop thôi.」"
1986 = "「Đúng vậy. Ở bên em rất vui.\\nNhìn thấy nụ cười của em, tôi lại càng muốn làm em vui hơn nữa.」"
2006 = "「Vâng. Bà chủ chỉ cần nhìn thoáng qua,\\nđã nhận ra sự bất ổn của em là do tâm lý.」"
2015 = "「Kính chào quý kh——ơ, gì vậy, là anh Soutetsu à.\\nAnh để quên đồ sao ạ?」"
2092 = "「Em nói ngốc nghếch gì——Ư!」"
2131 = "「Vậy sao. Nếu vậy, có lẽ tôi sẽ làm theo lời em.」"
2135 = "「Ư!」"
2163 = "「Anh Soutetsu.\\nNếu rảnh tay, cho tôi xin chút thời gian được không?」"
2183 = "「Ư!!?」"
2827 = "Mỉm cười \"Ufufu\", khẽ vẫy tay,\\nPaulette một mình đi về phía xưởng đầu máy."
```

## Kết bài

File ハチロク11_幽霊.txt.toml: 411 dòng đã đọc hết, **21 dòng sai (5,1%)** — file sạch, không có lỗi hệ thống (không misalignment, không rotation, không contamination, không orphan, không untranslated, không duplicate keys). Lỗi tập trung ở đại từ của Soutetsu với Hachiroku (9/21 dòng dùng "anh" thay vì "tôi" — lỗi quen thuộc của bản dịch Gemini) và 6 tiếng nấc っ bị mất đã có sẵn trong sweep. 4 mục thuật ngữ (Hinomoto, gloss 列車, 帝大, gloss 機関士) để lại cho unification pass. Tổng cộng sau file này: **181 file / 8.132 dòng sai** (cơ sở 180 file / 8.111 dòng sai + 21 file này).