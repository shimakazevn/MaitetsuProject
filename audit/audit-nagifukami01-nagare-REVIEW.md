# Audit — 凪ふかみ01_流れ.txt.toml (07_Nagi_Fukami)

- **File:** `凪ふかみ01_流れ.txt.toml` — route 07_Nagi_Fukami (Nagi + Fukami, chèo thuyền xuôi dòng sông Kuma / luyện tập + khói 8620). File này KHÁC với file đã audit `凪ふかみ01_凪の成長、ふかみの成長.txt.toml` — không nhầm lẫn.
- **Đọc:** toàn bộ **429 dòng** (monologue 178, 双鉄 94, ふかみ 87, 凪 64, ハチロク 3, ポーレット 3), key 1028–2582. Phương pháp: đọc từng dòng đối chiếu JP + TW (CSV3), kiểm tra đại từ theo người nghe, SFX theo quy tắc âm, sweep gasp theo file.
- **Kết quả: 30 dòng sai (7,0%)** — SFX/âm thanh 12, đại từ xưng hô 6, gasp っ (sweep) 5, dịch sai nghĩa/câu vỡ/chủ ngữ 5, thuật ngữ đã quyết 1, từ đệm 1.
- **TOML:** md5 `32e5aee57b56922bdc567e080eab1020`, 1 bản duy nhất (không có bản trùng — đã kiểm md5 toàn bộ toml2; file cùng tên gốc `凪ふかみ01_凪の成長、ふかみの成長` có md5 khác `e6e70075e3d125fe3c9b1191aebf5104`), UTF-8 BOM + CRLF, 429 key script. `[selections]` rỗng. Nhân vật trong TOML: Fukami, Hachiroku, Paulette, Nagi, Soutetsu.
- **CSV3:** 1 bộ duy nhất, 429 dòng, 429 key duy nhất, 0 VN trống, 0 key thiếu ở cả hai chiều. TOML và CSV3 khớp tuyệt đối sau khi chuẩn hoá `\n` literal → khoảng trắng (220/429 dòng chỉ khác nhau ở điểm này — CSV3 giữ `\n` thật, TOML-2 đã làm phẳng; đã kiểm bằng script: 0 khác biệt ngoài `\n`).

## 1. Kiểm chứng file

- TOML parse OK (utf-8-sig, BOM): sections `[info]`, `[characters]`, `[character_subs]`, `[script]`, `[selections]`; 429 key script, khớp CSV3 429/429.
- 0 key trùng trong TOML và trong CSV3. 0 dòng VN trống. 0 tag `%l` lệch (số tag JP = số tag VN ở mọi dòng).
- 0 ký tự JP thô (っ/ぁ/ぃ/ぅ/ぇ/ぉ) còn sót trong VN.
- File chưa từng xuất hiện trong ROUTE-AUDIT.md (grep 0 kết quả) — chưa audit, không trùng lặp.

## 2. Đối chiếu sweep (sweep-raw-gasp-wrong.json)

Sweep có **5 entry** cho file này — cả 5 đều đúng, đã nhận (4 áp nguyên văn, 1 sửa lại):

| Key | Kind | JP | Fix |
|---|---|---|---|
| 1854 | lost-gasp-whole | 「っ！！？」 | 「Ư!!?」 |
| 1855 | lost-gasp-whole | 「っ！？」 | 「Ư!?」 |
| 2334 | lost-gasp-trailing | とか――――っ！ | …chẳng hạn――――Ư! |
| 2581 | lost-gasp-whole | （っ！） | （Ư!） |
| 2582 | lost-gasp-whole | （っ！？） | （Ư!?） |

- **2334 lưu ý:** fix của sweep bỏ mất `\n` của VN cũ (JP có `\n` sau dấu phẩy, VN cũ có `\n`). Tôi đã giữ nguyên `\n`, chỉ thêm Ư — fix chỉ khác VN cũ ở đúng chỗ gasp. Xem chi tiết ở §6.

## 3. SFX / âm thanh — 12 dòng

Nhóm lỗi lớn nhất file này: dịch giả hệ thống rút gọn các âm JP thành "Phù"/"Oái"/"Ư" làm mất mora, hoặc dịch SFX hành động thành tiếng kêu.

### Key 1386 — [双鉄] — sfx
- JP: 「いや、さすがに遊んでるヒマなどは――わぷっ！」 / TW: 「不，我現在根本就沒有時間玩——咕噗！」
- VN cũ: 「Không, làm gì có thời gian rảnh mà chơi——oáp!」
- Fix: 「Không, làm gì có thời gian rảnh mà chơi——phụt!」
- Lý do: わぷっ là tiếng sặc/phụt nước khi bị dìm giữa câu (TW 咕噗); "oáp" là tiếng ngáp — sai hẳn âm.

### Key 1452 — [双鉄] — sfx
- JP: 「ぷはーーーっ！」 / TW: 「呼哈——！」
- VN cũ: 「Phù hơ——!」
- Fix: 「Phù haaaa——!」
- Lý do: ぷはーーーっ = pu + ha + 3 ー = 4 mora "a" (tiền lệ đếm mora ở lr_hibikimayami 1579: 8 mora → 8 a); "Phù hơ" đổi nguyên âm a→ơ và mất độ dài.

### Key 1456 — [双鉄] — sfx
- JP: 「ぷあっ！？　何をっ」 / TW: 「咕哇！？你幹什麼」
- VN cũ: 「Phù!? Em làm gì vậy hả.」
- Fix: 「Phùa!? Em làm gì vậy hả.」
- Lý do: ぷあっ = pu + a; "Phù" làm mất mora あ (quy tắc fa/fu đã quyết: ふあ→"phùa", ぷあ cùng họ).

### Key 1457 — [ふかみ] — sfx
- JP: 「むぎゅっ」 / TW: 「咕嗚」
- VN cũ: 「Ư ư」
- Fix: 「Mugyu」
- Lý do: むぎゅっ là tiếng siết/ôm chặt (Fukami ôm Soutetsu từ phía sau, 1456 anh hỏi "Em làm gì vậy"), không phải tiếng rên; "Ư ư" sai hẳn tính chất âm. Romaji giữ nguyên âm JP (một rendering duy nhất cho cả dòng).

### Key 1469 — [ふかみ] — sfx
- JP: 「ふわっぷ！」 / TW: 「哇！？」
- VN cũ: 「Oái!」
- Fix: 「Phụp!」
- Lý do: ふわっぷ là tiếng phụt/phun (SFX hành động, như nhổ nước), không phải tiếng kêu giật mình "Oái".

### Key 1541 — [双鉄] — sfx
- JP: 「ちょっ！　待てっ――ぷあっ！？」 / TW: 「喂！等——嗚哇！？」
- VN cũ: 「Khoan! Đợi đã——phù!?」
- Fix: 「Khoan! Đợi đã——phùa!?」
- Lý do: ぷあっ, như 1456 — mất mora あ.

### Key 1544 — [凪] — sfx
- JP: 「うひゃあ」 / TW: 「嗚哇」
- VN cũ: 「Uisss」
- Fix: 「Uhyaa」
- Lý do: うひゃあ = u-hya-a; "Uisss" bịa thêm âm "sss" không có trong JP và làm mất phụ âm hy- (lỗi mất âm, tiền lệ họ ひゃ: "Á" cho きゃ/ひゃ là lỗi mất phụ âm mora — ở đây còn bịa thêm âm). Không phải cảnh H nhưng vẫn phải giữ nguyên âm JP; romaji Uhyaa giữ đúng hình âm.

### Key 1547 — [ふかみ] — sfx
- JP: 「ふぇぇっ」 / TW: 「嗚唉」
- VN cũ: 「Ư ơ.」
- Fix: 「Phuêê.」
- Lý do: ふぇ→"phuê" (quy tắc đã quyết), ぇ thêm = 2 ê; "Ư ơ" làm mất phụ âm ph- và biến thành tiếng rên.

### Key 1572 — [双鉄] — sfx
- JP: 「ぶはっ！」 / TW: 「噗哈！」
- VN cũ: 「Phù!」
- Fix: 「Phù ha!」
- Lý do: ぶはっ = bu-ha (trồi lên mặt nước, thở hắt); "Phù" làm mất mora は.

### Key 1754 — [双鉄] — sfx
- JP: 「なんとも見事な――わぷっ！？」 / TW: 「真是太漂亮了——嗚哇！？」
- VN cũ: 「Thật là đẹp mắt——oáp!?」
- Fix: 「Thật là đẹp mắt——phụt!?」
- Lý do: わぷっ, như 1386 — tiếng sặc nước, không phải ngáp.

### Key 2553 — [monologue] — sfx
- JP: （ぐ～～っ――） / TW: （咕～）
- VN cũ: （Rột rột——）
- Fix: （Ừ——）
- Lý do: ぐ～～っ là tiếng rên/gồng khi chèo (chuỗi SFX chèo thuyền 2547–2558); "Rột rột" là tiếng lạo xạo/rè rè — sai âm.

### Key 2577 — [monologue] — sfx
- JP: （ぬぎっ！） / TW: （脫衣服聲）
- VN cũ: （Cởi!）
- Fix: （Tuột!）
- Lý do: ぬぎっ là SFX tiếng tuột/cởi đồ (TW xác nhận là tiếng cởi đồ), không phải mệnh lệnh "Cởi!".

## 4. Đại từ xưng hô — 6 dòng

### Key 1383 — [凪] — pronoun
- JP: 「ばってん、それならもっと先に頑張るところあるばい」 / TW: 「不過，以後需要你努力的時候還多了去咧」
- VN cũ: 「Nhưng mà, nếu vậy thì còn nhiều chỗ cần cậu phải cố gắng trước đó nữa.」
- Fix: 「Nhưng mà, nếu vậy thì còn nhiều chỗ cần anh phải cố gắng trước đó nữa.」
- Lý do: Nagi nói với Soutetsu (đáp lại 1382 của Soutetsu); cô gọi anh là "anh hai" — "cậu" sai.

### Key 1483 — [ふかみ] — pronoun
- JP: 「え、別に無理なんて」 / TW: 「哎，我沒勉強啊」
- VN cũ: 「Ơ, tớ đâu có quá sức gì đâu.」
- Fix: 「Ơ, em đâu có quá sức gì đâu.」
- Lý do: Fukami nói với Soutetsu (mạch 1476–1490, 1486 "Ý anh là sao?"); tự xưng "em". "Tớ" chỉ dùng khi nói với Nagi (cặp tớ–cậu, quyết định 凪ふかみ07).

### Key 1655 — [ふかみ] — pronoun
- JP: 「だから……その、頑張る理由。ええと……つまり……あ、うちのため、とかもあるし」 / TW: 「所以……那個，我這麼努力的理由。唔……也就是……啊，當然也有為了我自己家的原因啦」
- VN cũ: 「Thì là……lý do tớ cố gắng ấy.\nƯm……tức là……A, cũng vì gia đình tớ nữa.」
- Fix: 「Thì là……lý do em cố gắng ấy.\nƯm……tức là……A, cũng vì gia đình em nữa.」
- Lý do: Fukami giải thích với Soutetsu (sau 1651/1653 anh nói "Anh biết rồi"); tự xưng "em" (2 chỗ trong dòng). Đối chứng: 1659 cùng người nói, cùng người nghe dùng "tụi em" đúng.

### Key 1667 — [凪] — pronoun
- JP: 「やっけーん、疲れとるいうことでしょお。ふかみちゃんがウッカリミスばしよるとか」 / TW: 「才不是呢，是你太累了吧。你才不可能會這麼粗心呢」
- VN cũ: 「Thì đó, chứng tỏ là cậu đang mệt mỏi mà.\nChứ Fukami mà lại mắc lỗi bất cẩn sao.」
- Fix: 「Thì đó, chứng tỏ là anh đang mệt mỏi mà.\nChứ Fukami mà lại mắc lỗi bất cẩn sao.」
- Lý do: Nagi nói với Soutetsu ("cậu đang mệt" — người mệt là Soutetsu; Fukami là ngôi thứ ba trong câu sau); "cậu" sai, phải là "anh".

### Key 1813 — [双鉄] — pronoun
- JP: 「今度は僕が、凪とふかみを手助けするのだ」 / TW: 「這次就換我來幫凪和深美吧」
- VN cũ: 「Lần này, tôi sẽ là người giúp đỡ Nagi và Fukami.」
- Fix: 「Lần này, anh sẽ là người giúp đỡ Nagi và Fukami.」
- Lý do: Soutetsu nói với Fukami/Nagi (cảnh sông, Hachiroku không có mặt) → tự xưng "anh" theo quy tắc đã sửa 20/11; "tôi" sai.

### Key 1824 — [ふかみ] — pronoun
- JP: 「あ、あれは……ちょっとウッカリミスとか」 / TW: 「那、那個是……只是我有點粗心了而已」
- VN cũ: 「A, cái đó là……tớ hơi bất cẩn một chút thôi.」
- Fix: 「A, cái đó là……em hơi bất cẩn một chút thôi.」
- Lý do: Fukami nói với Soutetsu (1822 gọi "anh Soutetsu") → "em".

## 5. Dịch sai nghĩa / câu vỡ / chủ ngữ — 5 dòng

### Key 1619 — [双鉄] — mistranslation
- JP: 「どぎゃんもこぎゃんも……\n逆に、何故ドキドキするのか教えてくれんか？」 / TW: 「就算你這麼問……我反而想問你為什麼我要小鹿亂撞啊？」
- VN cũ: 「Tại sao cái gì chứ……\nNgược lại, em nói cho anh biết tại sao anh phải thấy tim đập thình thịch đi?」
- Fix: 「Dù em có hỏi thế nào đi nữa……\nNgược lại, em nói cho anh biết tại sao anh phải thấy tim đập thình thịch đi?」
- Lý do: どぎゃんもこぎゃんも (phương ngữ Hakata) = "dù có hỏi thế nào đi nữa" (TW 就算你這麼問); "Tại sao cái gì chứ" là dịch garbled, không có nghĩa rõ trong tiếng Việt.

### Key 1641 — [ふかみ] — mistranslation
- JP: 「わたし、双鉄さんに。\n川下り、お手伝いしてほしい。です！」 / TW: 「我想請雙鐵先生你來幫忙！嗯」
- VN cũ: 「Em, rất mong anh Soutetsu.\nĐến phụ giúp công việc chèo thuyền xuôi dòng. Ạ!」
- Fix: 「Em rất mong anh Soutetsu\nđến phụ giúp việc chèo thuyền xuôi dòng ạ!」
- Lý do: câu JP là một câu hoàn chỉnh ("Em muốn nhờ anh Soutetsu đến phụ giúp chèo thuyền"); VN cũ vỡ thành 3 mảnh, "Ạ!" đứng riêng một câu vô nghĩa.

### Key 1786 — [双鉄] — mistranslation
- JP: 「大丈夫か――、か」 / TW: 「要不要緊——嗎」
- VN cũ: 「Vẫn ổn chứ——, à.」
- Fix: 「Vẫn ổn chứ——, chứ?」
- Lý do: JP lặp lại trợ từ か sau dấu ngắt (nói lắp/lặp lại câu hỏi); "à." sau dấu phẩy là garbled; lặp "chứ" giữ đúng cấu trúc JP.

### Key 2057 — [monologue] — subject
- JP: そうであっても、煙を掴まえなければならぬ。 / TW: 但就算這樣，我們還是得抓住這縹緲的煙才行。
- VN cũ: Dù vậy, chúng tôi vẫn phải tóm được làn khói đó.
- Fix: Dù vậy, tôi vẫn phải tóm được làn khói đó.
- Lý do: monologue của Soutetsu, chủ ngữ JP là 僕 (số ít, không có ら); toàn bộ monologue khác trong file đều dùng "tôi" (2036, 2040, 2202, 2246, 2298…); "chúng tôi" chỉ đúng khi JP có 僕ら (2489) hoặc 相談の上 (2163) — ở đây không có cơ sở JP.

### Key 2385 — [monologue] — mistranslation
- JP: ふかみが素直に、気兼ねなく涼めるようにと、シャツをめくって、まずは自分が大げさなほど暑がった。 / TW: 為了讓深美能毫無顧慮地接受自己的好意，凪還先掀起衣服故意誇張地做出覺得很熱的樣子。
- VN cũ: Để Fukami có thể ngoan ngoãn, thoải mái hóng mát,\ncon bé đã vén áo lên, tự mình làm quá lên rằng rất nóng trước.
- Fix: Để Fukami có thể ngoan ngoãn, thoải mái hóng mát,\nNagi đã vén áo lên, tự mình làm quá lên rằng rất nóng trước.
- Lý do: chủ ngữ JP là Nagi (TW nói rõ 凪還先掀起衣服; 2415 xác nhận Nagi vén áo sơ mi lên trước để Fukami thoải mái làm theo); "con bé" trong VN đọc thành Fukami — sai chủ thể, đảo ngược hành động.

## 6. Gasp っ (sweep) — 5 dòng

Cả 5 entry sweep của file này đều đúng, đã nhận. Chi tiết JP/TW/VN cũ/fix xem §2.

### Key 1854 — [双鉄] — gasp
- JP: 「っ！！？」 → Fix: 「Ư!!?」 (VN cũ 「!!?」 mất hẳn âm っ.)

### Key 1855 — [双鉄] — gasp
- JP: 「っ！？」 → Fix: 「Ư!?」 (VN cũ 「!?」 mất hẳn âm っ.)

### Key 2334 — [monologue] — gasp
- JP: 例えば\x%l8620;#00ffc040;8620%l;#;の石炭を、\nそのまま点火剤として流用するとか――――っ！
- VN cũ: Ví dụ như lấy than của \x%l8620;#00ffc040;8620%l;#;\ndùng luôn làm chất mồi lửa chẳng hạn――――!
- Fix: Ví dụ như lấy than của \x%l8620;#00ffc040;8620%l;#;\ndùng luôn làm chất mồi lửa chẳng hạn――――Ư!
- Lý do: gasp cuối dòng sau ――――, âm っ mất hẳn → thêm Ư (quy tắc gasp). **Khác fix sweep ở một điểm:** fix của sweep bỏ mất `\n` của VN cũ; tôi giữ nguyên `\n` để fix chỉ khác VN cũ ở đúng chỗ gasp.

### Key 2581 — [monologue] — gasp
- JP: （っ！） → Fix: （Ư!） (VN cũ （!） mất hẳn âm っ.)

### Key 2582 — [monologue] — gasp
- JP: （っ！？） → Fix: （Ư!?） (VN cũ （!?） mất hẳn âm っ.)

## 7. Thuật ngữ đã quyết — 1 dòng

### Key 2287 — [monologue] — terminology
- JP: ポケットの中にメモ帳が無い。\nならば、恐らく\x%l乗務鞄;#00ffc040;乗務鞄%l;#;に……ああ。
- VN cũ: Sổ tay không có trong túi.\nVậy thì chắc là ở trong \x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;……A.
- Fix: Sổ tay không có trong túi.\nVậy thì chắc là ở trong \x%l乗務鞄;#00ffc040;túi công tác%l;#;……A.
- Lý do: 乗務鞄 = "túi công tác" (đã quyết 20/11); "túi phi hành đoàn" là thuật ngữ hàng không, cấm dùng (tiền lệ ハチロク10_炙り出し 2411 sửa trong audit). Đây là dòng 乗務鞄 duy nhất trong file.

## 8. Từ đệm — 1 dòng

### Key 1482 — [ふかみ] — filler
- JP: 「えっ、えとっ」 / TW: 「哎，唔」
- VN cũ: 「Ơ, dạ.」
- Fix: 「Ơ, ừm.」
- Lý do: えとっ là từ đệm ngập ngừng "um" (TW 唔); "dạ" là lời đáp khẳng định, sai chức năng. Đối chứng trong file: 1490 ええとっ → "Ưm".

## 9. Giữ nguyên có lý do (đã kiểm, không sửa)

- **1442 / 1845 — きゃっ → "Á!?":** tiếng kêu giật mình ngoài cảnh H (Fukami hoảng, không phải moan). Quy tắc romaji họ ひゃ/きゃ chỉ áp cho dòng moan trong cảnh H; ngoài cảnh H, "Á" cho tiếng kêu giật mình là chấp nhận được. Giữ.
- **1738 / 1740 — Nagi→Fukami "cậu":** giữ. Cặp Nagi↔Fukami là tớ–cậu cùng tuổi (quyết định 凪ふかみ07 21/11); "bé" là cách gọi âu yếm, còn "cậu" là đại từ nhân xưng trong cặp này. Không phải "chị".
- **1367 — Fukami tự xưng "tớ" với Nagi:** giữ ("Tớ nghĩ nhiều quá…") — đúng cặp tớ–cậu.
- **1441 / 1669 — "tụi mình":** giữ. 1441 là "chúng ta" bao hàm cả nhóm (Soutetsu + hai cô); 1669 Fukami nói với Nagi, "tụi mình" là số nhiều của "tớ" trong cặp tớ–cậu. Khác với 1659 "tụi em" (nhóm các cô nói với Soutetsu) — phạm vi "chúng ta" khác nhau, không mâu thuẫn.
- **1691 — Soutetsu "mình":** GIỮ + CỜ CHO HIEU (xem §10). 「Đúng vậy.\nTại sao mình lại không nhận ra một điều đơn giản như thế chứ.」 — câu tự vấn nói ra thành lời (trong 「」), Hachiroku có mặt (1692 cô đáp "À."). "Mình" đúng nếu tính là tự thoại nội tâm; "tôi" đúng nếu tính là đối thoại với Hachiroku. Không quyết được từ văn bản — giữ nguyên, cờ cho Hieu.
- **1700 — じいちゃん → "Ông nội":** giữ. Đây là ông của Nagi (cảnh nhà Nagi, ăn mì udon), KHÔNG phải Seki; quy tắc "ông ngoại" chỉ áp cho các dòng Seki. Các dòng "ông nội" khác giữ nguyên.
- **1739 — ////っ:** giữ ("Sao lại——à thì……////"). Dấu //// đã diễn tả sự ngượng/cắt ngang; thêm Ư sau //// sẽ kỳ cục.
- **1505 — ぬっ → "Ư!":** giữ (tiếng gầm/gừ ngắn; quy ước file dùng "Ư" cho cả grunt).
- **1521 — ああん → "A a":** giữ (tiếng nũng nịu; thêm "n" thành "Aan" kỳ cục).
- **1549 — うおおおっ → "U ô ồ!!":** giữ (tiếng hét gắng sức; giữ nguyên âm ô, chỉ thiếu 1 mora so với JP — khác với moan, độ dài tiếng hét là ngẫu hứng).
- **1788 — 雲を掴む → "mò kim đáy biển":** giữ (thay thành ngữ tương đương nghĩa "đuổi theo thứ vô hình/không thể"; TW 虛無縹緲 cùng nghĩa).
- **2057 đã sửa; 2163 / 2384 / 2489 — "chúng tôi":** giữ (2163 có 相談の上; 2384 nhóm làm việc trên tàu; 2489 JP có 僕ら — số nhiều rõ ràng).
- **2357 — ベスト → "áo phao":** giữ. ベスト trong cảnh sông + 1838 "để em mặc đàng hoàng" cho thấy đây là áo phao cứu sinh, không phải áo gi-lê thường.
- **2547 — ちゃぷんッ → "Xoạt":** giữ. TW 划船聲 (tiếng chèo) ủng hộ cách đọc "xoạt nước"; không rõ ràng sai.
- **2575 — （ぐっ） → "（Ưm）":** giữ (tiếng gừ ngắn; 2552 ぐっ → "Hự" là ngữ cảnh chèo khác, cả hai đều là cách diễn grunt hợp lệ).
- **2562 / 2565 — "mình" trong （）:** giữ — độc thoại nội tâm trong ngoặc, đúng ngoại lệ "mình".
- **0 lệch hàng / 0 chuỗi xoay / 0 nhiễm chéo / 0 mồ côi / 0 chưa dịch / 0 trùng key.** Đã kiểm: mọi dòng VN đều khớp JP+TW của đúng key của nó; không có dòng nào là bản dịch của dòng khác; không có dòng VN nào không tìm được JP tương ứng trong project (đã đối chiếu toàn bộ 429 key).

## 10. Cờ cho Hieu (không tự quyết)

1. **1691 — "mình" hay "tôi"?** Soutetsu tự vấn thành lời 「どうしてこんな単純なことに気がつかなかったのだ」 trong khi Hachiroku có mặt và đáp lại (1692). Nếu tính là độc thoại nội tâm thì "mình" đúng (ngoại lệ đã quyết); nếu tính là đối thoại với Hachiroku thì phải là "tôi". Cần Hieu (hoặc kiểm tra ngữ cảnh game) quyết.
2. **1452 "Phù haaaa——!" và 1547 "Phuêê."** — hai fix áp dụng công thức đếm mora cho tiếng thở/phụt (không phải moan). Nếu Hieu muốn tiếng thở giữ dạng ngẫu hứng ngắn ("Phù hơ", "Ư ơ") thì báo lại; hiện tại đã sửa theo quy tắc "không để mất âm".
3. **1544 "Uhyaa"** — romaji cho tiếng kêu của Nagi ngoài cảnh H (không phải moan). Quy tắc romaji họ ひゃ hiện chỉ khóa cho moan cảnh H; dòng này sửa vì "Uisss" bịa âm, nhưng nếu Hieu muốn dạng Việt ("Ui yaa"/"Á") thì báo.
4. B19 vẫn park (kiểm tra trong game tại Paulette 13 key 1596 trước khi chạy sweep tag `%l`).

## 11. Lượt soát 2 (second pass)

- **Tổng số: 30 / tái kiểm chứng đúng: 30 / loại bỏ: 0 / sửa lại: 0.** Đọc lại toàn bộ 30 giá trị fix đối chiếu từng JP (+TW) sau khi build JSON; mọi fix chỉ khác VN cũ ở đúng chỗ cần sửa (đã kiểm bằng diff cơ học: mỗi fix 1–2 thao tác thay thế duy nhất, trừ 1641 gộp câu và 1655 sửa 2 chỗ cùng loại).
- Kiểm chứng cơ học: JSON 30 mục dạng list-of-dicts, key chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 30/30; khối TOML 30 khóa, parse OK bằng tomllib, 0 sai lệch giá trị (so sánh chuỗi thô, kể cả `\n` literal).

## 12. Khối TOML (đã kiểm parse, 30 key)

```toml
"1383" = "「Nhưng mà, nếu vậy thì còn nhiều chỗ cần anh phải cố gắng trước đó nữa.」"
"1386" = "「Không, làm gì có thời gian rảnh mà chơi——phụt!」"
"1452" = "「Phù haaaa——!」"
"1456" = "「Phùa!? Em làm gì vậy hả.」"
"1457" = "「Mugyu」"
"1469" = "「Phụp!」"
"1482" = "「Ơ, ừm.」"
"1483" = "「Ơ, em đâu có quá sức gì đâu.」"
"1541" = "「Khoan! Đợi đã——phùa!?」"
"1544" = "「Uhyaa」"
"1547" = "「Phuêê.」"
"1572" = "「Phù ha!」"
"1619" = "「Dù em có hỏi thế nào đi nữa……\\nNgược lại, em nói cho anh biết tại sao anh phải thấy tim đập thình thịch đi?」"
"1641" = "「Em rất mong anh Soutetsu\\nđến phụ giúp việc chèo thuyền xuôi dòng ạ!」"
"1655" = "「Thì là……lý do em cố gắng ấy.\\nƯm……tức là……A, cũng vì gia đình em nữa.」"
"1667" = "「Thì đó, chứng tỏ là anh đang mệt mỏi mà.\\nChứ Fukami mà lại mắc lỗi bất cẩn sao.」"
"1754" = "「Thật là đẹp mắt——phụt!?」"
"1786" = "「Vẫn ổn chứ——, chứ?」"
"1813" = "「Lần này, anh sẽ là người giúp đỡ Nagi và Fukami.」"
"1824" = "「A, cái đó là……em hơi bất cẩn một chút thôi.」"
"1854" = "「Ư!!?」"
"1855" = "「Ư!?」"
"2057" = "Dù vậy, tôi vẫn phải tóm được làn khói đó."
"2287" = "Sổ tay không có trong túi.\\nVậy thì chắc là ở trong \\x%l乗務鞄;#00ffc040;túi công tác%l;#;……A."
"2334" = "Ví dụ như lấy than của \\x%l8620;#00ffc040;8620%l;#;\\ndùng luôn làm chất mồi lửa chẳng hạn――――Ư!"
"2385" = "Để Fukami có thể ngoan ngoãn, thoải mái hóng mát,\\nNagi đã vén áo lên, tự mình làm quá lên rằng rất nóng trước."
"2553" = "（Ừ——）"
"2577" = "（Tuột!）"
"2581" = "（Ư!）"
"2582" = "（Ư!?）"
```

## Kết bài

File 凪ふかみ01_流れ (07_Nagi_Fukami, chèo thuyền sông Kuma): đọc toàn bộ 429 dòng, **30 dòng sai (7,0%)** — nặng nhất là SFX/âm thanh (12 dòng: dịch giả rút gọn hệ thống các âm ぷあ/ぶは/わぷっ/ふぇ thành "Phù"/"oáp"/"Ư ơ", bịa "Uisss", dịch SFX hành động thành tiếng kêu) và đại từ xưng hô (6 dòng: Nagi gọi Soutetsu "cậu" 2×, Fukami tự xưng "tớ" với Soutetsu 3×, Soutetsu tự xưng "tôi" với hai cô 1×), cộng gasp っ sweep 5 dòng, dịch sai nghĩa/câu vỡ/chủ ngữ 5 dòng, thuật ngữ 乗務鞄 1 dòng, từ đệm 1 dòng. Không có lệch hàng, xoay vòng, nhiễm chéo, mồ côi, chưa dịch hay trùng key. Cần Hieu quyết: 1691 "mình" hay "tôi" (tự vấn thành lời trước mặt Hachiroku).
