# Moan-fix review: lr_凪ふかみh1_じぇいけい！.txt.toml (moan-lr-nagifukami-h1-jiekei)

## 1. Kiểm chứng file

- File: `lr_凪ふかみh1_じぇいけい！.txt.toml` — route 07_Nagi_Fukami, cảnh H ba người: Nagi + Fukami khẩu giao kép cho Soutetsu (đồng phục JK), rồi làm tình ba người.
- TOML md5 `ef960cfc3776057ff0cbcad101eb4875` (khớp md5 audit), không có bản trùng trong 227 file, BOM + CRLF, 404 key `[script]`. Chỉ 3 nhân vật: Soutetsu (双鉄), Nagi (凪), Fukami (ふかみ).
- CSV3: 1 bộ duy nhất, 404 dòng, 0 key trùng; VN khớp TOML 404/404 sau chuẩn hoá `\n`/khoảng trắng (218 lệch chỉ là `\n` literal trong CSV3 thành xuống dòng/khoảng trắng trong TOML).
- Đã đọc 404/404 dòng; xét 229 dòng rên/hơi thở/SFX (thoại rên + SFX trong ngoặc + SFX độc thoại). Audit file này: 62/404 dòng sai (15,3%) — terminology 16, meaning 10, pronoun 1, sfx 20, gasp 15.

## 2. Tổng quan các dòng đổi

- Đổi **34 dòng**: 21 romaji + 12 đếm nguyên âm + 1 sai âm.
- Romaji họ fa/fu (21 dòng): 1479, 1481, 1505, 1509, 1510, 1512, 1513, 1522, 1523, 1532, 1581, 1583, 1590, 1595, 1597, 1598, 1603, 1619, 1657, 1658, 1714 — ふあ→Fua, ふぁ→Fa (giữ hoa/thường theo vị trí như audit). Toàn bộ là đổi ngược token fa/fu mà audit đã đổi Fua/fua→Phà/phà: audit áp luật fa/fu khoá ("phà"/"phùa"), moan xét lại theo romaji fallback Hieu 21/11 ~01:56 — "Phà" nghe ngượng trong chuỗi rên H-scene ("Phà! A! A! A!" lặp đi lặp lại), nên chuyển sang romaji; tiền lệ file mẫu 凪ふかみh1 (9 dòng fa/fu → Fua/Fa, parent duyệt 21/11).
- Sai âm (1 dòng): 1502 — audit gộp ふ……ぁ (hai âm riêng) thành "Phà" (một mora); khôi phục "Fu……a——". 1505 token đầu cùng lỗi, gộp trong fix romaji của nó.
- Đếm nguyên âm (12 dòng): 1477, 1483, 1491, 1507, 1552, 1574, 1599, 1614, 1677, 1695, 1789, 1485 — はぁ/はあ→Haa, ひゅあ/ひゅぁ đếm lại số a (1477 thừa 2, 1483 thiếu 1, 1491 thừa 1), あうぅ→auu, ふぅ→fuu, ふふーん→Nfufuun, やああ→Áaa.
- Lưu ý quan trọng: 12 key có fix == old_vn (CSV3): 1481, 1502, 1509, 1522, 1523, 1532, 1595, 1597, 1598, 1603, 1657, 1714 — vì moan đổi ngược đúng token fa/fu mà audit đã đổi (Fua→Phà), nên giá trị cuối trùng lại CSV3. Kiểm chứng cơ học (difflib): fix vs GIÁ TRỊ AUDIT của 22 key trùng audit chỉ khác đúng token rên (xem §7).

## 3. Từng dòng đổi (JP / TW / cũ / mới / lý do)

### 1. key 1479 [凪] — romaji
- JP: 「ひゅあっ！　あっ！　はっ！　こんなのっ！　すごっ！\nふあっ！　こぎゃん、たくさん、されたら、凪、さまっ」
- TW: 「呀！啊！啊！這太棒了！啊！老是這樣做的話，本小姐……」
- Cũ: 「Hyua! A! Ha! Thế này! Tuyệt quá!\nFua! Bị làm, nhiều thế này, Nagi, mất」
- Mới: 「Hyua! A! Ha! Thế này! Tuyệt quá!\nFua! Bị làm, nhiều thế này, Bổn tiểu thư——」
- Lý do: ふあっ → Fua (audit đổi thành "Phà" nghe ngượng trong chuỗi rên; romaji fallback Hieu 21/11 ~01:56; tiền lệ file mẫu 凪ふかみh1: ふあ→Fua). ひゅあっ "Hyua" của audit giữ nguyên.

### 2. key 1481 [凪] — romaji
- JP: 「はひゅっ！　んっ！　ふあっ！　あっ！　あたまっ！\nからだっ！　おまんこ！　あつい！　あつ、くてっ！」
- TW: 「呀！嗯！啊！啊！腦袋！身體！下面！好燙！燙死了！」
- Cũ: 「Hahyu! Ưm! Fua! A! Đầu em!\nCơ thể em! Cô bé! Nóng quá! Nóng, quá!」
- Mới: 「Hahyu! Ưm! Fua! A! Đầu em!\nCơ thể em! Cô bé! Nóng quá! Nóng, quá!」
- Lý do: ふあっ → Fua (như 1479). はひゅっ "Hahyu" của audit giữ nguyên.

### 3. key 1502 [凪] — wrong-sound
- JP: 「ふ……ぁ――にーさん、凶悪ばい」
- TW: 「呼……啊……大哥哥的好兇悍啊」
- Cũ: 「Fu……a——anh Soutetsu, dữ tợn quá đi」
- Mới: 「Fu……a——anh Soutetsu, dữ tợn quá đi」
- Lý do: JP ふ……ぁ―― là HAI âm riêng (hơi thở "fu" + "a", cách nhau ……), audit gộp thành "Phà" (pha = ふぁ một mora) là sai âm. Khôi phục "Fu……a——" — đúng kiểu hơi thở "fu" của file (1645/1659/1679 đều dùng "fu").

### 4. key 1505 [ふかみ] — romaji
- JP: 「ふっ……あ――（すんっ、すんんっ）――すご、い……\n精液……匂い、いっつもより、濃い……ふぁっ――」
- TW: 「呼……啊……（嗅，嗅）好棒……精液的……味道……比平時更濃郁……哇……」
- Cũ: 「Fu……a——（Khịt, khịt）——Tuyệt, quá……\nTinh dịch……mùi, nồng hơn, mọi khi……fua——」
- Mới: 「Fu……a——（Khịt, khịt）——Tuyệt, quá……\nTinh dịch……mùi, nồng hơn, mọi khi……fa——」
- Lý do: Token đầu ふっ……あ―― như 1502 → khôi phục "Fu……a——" (audit "Phà" gộp sai hai âm). Token cuối ふぁっ―― → "fa——" (romaji fallback).

### 5. key 1509 [ふかみ] — romaji
- JP: 「ふあっ――あっ――しゅごっ――すごっ――ふあっ！\nしきゅう――たたいて――びゅって――せいえきっ」
- TW: 「哇……啊……好棒……好棒……啊！精液……打在子宮裡……咻咻的」
- Cũ: 「Fua——a——tuyệt quá——tuyệt quá——fua!\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」
- Mới: 「Fua——a——tuyệt quá——tuyệt quá——fua!\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」
- Lý do: ふあっ ×2 → Fua / fua (giữ hoa/thường theo vị trí như audit). "Phà" nghe ngượng trong chuỗi rên.

### 6. key 1510 [凪] — romaji
- JP: 「ふぁ……あ――あ――ふかみちゃん、\nちょこっと激しく吸いすぎばい」
- TW: 「哇……啊，啊……小深，你吸得太用力了」
- Cũ: 「Fua……a——a——Fukami,\ncậu mút hơi mạnh quá rồi đấy.」
- Mới: 「Fa……a——a——Fukami,\ncậu mút hơi mạnh quá rồi đấy.」
- Lý do: ふぁ…… → Fa…… (romaji fallback; ふぁ = 1 nguyên âm a).

### 7. key 1512 [凪] — romaji
- JP: 「ふぁっ――ふかみちゃん――ふかみちゃんのお顔も、\nにーさんの精液――乾いて、カピカピになっちゃうばい」
- TW: 「哇……小深……你的臉上也是，大哥哥的精液……已經幹了」
- Cũ: 「Fua——Fukami——trên mặt Fukami cũng,\ntinh dịch của anh Soutetsu——khô lại, cứng đơ rồi kìa」
- Mới: 「Fa——Fukami——trên mặt Fukami cũng,\ntinh dịch của anh Soutetsu——khô lại, cứng đơ rồi kìa」
- Lý do: ふぁっ―― → Fa——.

### 8. key 1513 [凪] — romaji
- JP: 「ふぁ――ふかみちゃん、ふかみちゃん……ん……\nちゅっ――れるっ――れろっ――ん――ちゅう――ちゅ」
- TW: 「哇……小深，小深……嗯……啾，啾，啾，嗯……啾，啾」
- Cũ: 「Fua——Fukami, Fukami……ưm……\nChụt——liếm——liếm——ưm——chụt——chụt」
- Mới: 「Fa——Fukami, Fukami……ưm……\nChụt——liếm——liếm——ưm——chụt——chụt」
- Lý do: ふぁ―― → Fa——.

### 9. key 1522 [双鉄] — romaji
- JP: 「ふあっ！　あっ！　あっ！　あっ！」
- TW: 「哇！啊！啊！啊！」
- Cũ: 「Fua! A! A! A!」
- Mới: 「Fua! A! A! A!」
- Lý do: ふあっ！ → Fua! (romaji fallback).

### 10. key 1523 [凪] — romaji
- JP: 「ふあっ！　あっ！　あっ！　あっ！！！」
- TW: 「哇！啊！啊！啊！！！」
- Cũ: 「Fua! A! A! A!!!」
- Mới: 「Fua! A! A! A!!!」
- Lý do: ふあっ！ → Fua! (romaji fallback).

### 11. key 1532 [ふかみ] — romaji
- JP: 「ふあっ！？　あっ――これっ――やっ――あっ！\nわらひっ――わた、しっ――おかしく――なっちゃうっ」
- TW: 「哇？！啊……這……不要……啊！我……我……會瘋掉的」
- Cũ: 「Fua!? A——cái này——không——a!\nTớ——tớ——sẽ trở nên——kỳ lạ, mất」
- Mới: 「Fua!? A——cái này——không——a!\nTớ——tớ——sẽ trở nên——kỳ lạ, mất」
- Lý do: ふあっ！？ → Fua!? (romaji fallback).

### 12. key 1581 [凪] — romaji
- JP: 「ぁ――ふかみ、ちゃんっ――はぁ――ふぁっ――んっ」
- TW: 「啊……小深……啊，啊……嗯」
- Cũ: 「A——Fukami——ha——fua——ưm」
- Mới: 「A——Fukami——haa——fa——ưm」
- Lý do: はぁ → haa (2 nguyên âm a); ふぁっ → fa (romaji fallback).

### 13. key 1583 [ふかみ] — romaji
- JP: 「あ……（くんくんっ――くん、くんっ――）\nふぁ……双鉄おにいさんの、勃起の匂い」
- TW: 「啊……（嗅嗅，嗅，嗅……）哇……是雙鐵哥哥勃起的味道」
- Cũ: 「A……（Khịt khịt——khịt, khịt——）\nFua……Mùi cương cứng của, anh Soutetsu.」
- Mới: 「A……（Khịt khịt——khịt, khịt——）\nFa……Mùi cương cứng của, anh Soutetsu.」
- Lý do: ふぁ…… → Fa…… (romaji fallback; Fukami thở ra khi ngửi mùi).

### 14. key 1590 [凪] — romaji
- JP: 「ふあっ！　やっ！　ぬいちゃっ！　やああっ！！」
- TW: 「啊！不要！別拔出去！不要！！」
- Cũ: 「Fua! Á! Rút ra mất! Áaaa!!」
- Mới: 「Fua! Á! Đừng rút ra! Áaa!!」
- Lý do: ふあっ → Fua; やああっ = や+あ+あ = 3 mora a → "Áaa" (Á + 2 a; cũ "Áaaa" thừa 1 a). Giữ "Đừng rút ra!" của audit. やっ → "Á" giữ (tiền lệ file mẫu 1227/1440).

### 15. key 1595 [ふかみ] — romaji
- JP: 「あっ！　ふあっ！　それも！　そっちもっ！！\n新しいのもくださいっ！　わたしのっ――ひゃんっ！？」
- TW: 「啊！啊！也要！我也要！新的我也要！給我……呀？！」
- Cũ: 「A! Fua! Cái đó! Cả cái đó nữa!!\nHãy cho em cả đợt mới đi! Cho em——hyan!?」
- Mới: 「A! Fua! Cái đó! Cả cái đó nữa!!\nHãy cho em cả đợt mới đi! Cho em——hyan!?」
- Lý do: ふあっ → Fua. ひゃんっ "hyan" của audit giữ nguyên (đã romaji).

### 16. key 1597 [凪] — romaji
- JP: 「ふあっ！　あっ！　あっ！　あっ！」
- TW: 「啊！啊！啊！啊！」
- Cũ: 「Fua! A! A! A!」
- Mới: 「Fua! A! A! A!」
- Lý do: ふあっ！ → Fua! (romaji fallback).

### 17. key 1598 [凪] — romaji
- JP: 「ふあっ！　あっ！　あっ！　あっ！\nにーさんっ！　にーさんっ！　にーさん！　にーさん！」
- TW: 「啊！啊！啊！啊！大哥哥！大哥哥！大哥哥！大哥哥！」
- Cũ: 「Fua! A! A! A!\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu! Anh Soutetsu!」
- Mới: 「Fua! A! A! A!\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu! Anh Soutetsu!」
- Lý do: ふあっ！ → Fua! (romaji fallback).

### 18. key 1603 [凪] — romaji
- JP: 「ふあっ！　あ！　これ！　こればいっ！　んっ！――\nこれが、にーさん！　うちのにーさんのおちんちんばい」
- TW: 「啊！啊！這個！就是這個！嗯！這，才是大哥哥的！才是咱的大哥哥的雞雞咧」
- Cũ: 「Fua! A! Cái này! Chính là cái này! Ưm!——\nĐây mới là anh Soutetsu! Là cậu nhỏ của anh Soutetsu của em!」
- Mới: 「Fua! A! Cái này! Chính là cái này! Ưm!——\nĐây mới là anh Soutetsu! Là cậu nhỏ của anh Soutetsu của em!」
- Lý do: ふあっ！ → Fua! (romaji fallback).

### 19. key 1619 [凪] — romaji
- JP: 「ふぁ――ふかみちゃん――んっ――ちゅっ――れろっ、\nれるっつ――ちゅむっ――ちゅっ――ちゅうう――ちゅ」
- TW: 「啊，小深……嗯，啾，啾，啾，啾，啾，啾，啾」
- Cũ: 「Fua——Fukami——ưm——chụt——liếm,\nliếm——chụt——chụt——chụt——chụt」
- Mới: 「Fa——Fukami——ưm——chụt——liếm,\nliếm——chụt——chụt——chụt——chụt」
- Lý do: ふぁ―― → Fa—— (romaji fallback).

### 20. key 1657 [ふかみ] — romaji
- JP: 「ちょっ！？　凪ちゃっ！　ふあっ！　だめっ！\nこれ！　わらひっ！　わたし――感じすぎ――ひゃう！」
- TW: 「喂？！小凪！哇！不行！這樣，我，我……會因為太舒服……呀！」
- Cũ: 「Khoan!? Nagi! Fua! Không được!\nThế này! Tớ! Tớ——sẽ sướng quá mất——hyau!」
- Mới: 「Khoan!? Nagi! Fua! Không được!\nThế này! Tớ! Tớ——sẽ sướng quá mất——hyau!」
- Lý do: ふあっ → Fua. ひゃう "hyau" của audit giữ nguyên (đã romaji).

### 21. key 1658 [凪] — romaji
- JP: 「う……ぁ……顔中、べとべとばぁい――ん……\nちゅるっ――（ごくっ）――ふぁ――粘っこかぁ～」
- TW: 「嗚……啊……整張臉都黏糊糊的咧……嗯……啾……（咕咚）……哇，太黏了」
- Cũ: 「U……a……khắp mặt, nhớp nháp quá đi——ưm……\nChụt——（Ực）——fua——đặc dính luôn~」
- Mới: 「U……a……khắp mặt, nhớp nháp quá đi——ưm……\nChụt——（Ực）——fa——đặc dính luôn~」
- Lý do: ふぁ―― → fa—— (giữ thường giữa dòng như audit).

### 22. key 1714 [ふかみ] — romaji
- JP: 「あつい――あついよぉ――ふあっ――しゅきっ――\nすき、すき――双鉄おにいさん、好き、凪ちゃん、好き」
- TW: 「好燙……好燙呀……啊……愛你……愛你，愛你，雙鐵哥哥，愛你，小凪，愛你」
- Cũ: 「Nóng quá——nóng quá đi——fua——thích lắm——\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」
- Mới: 「Nóng quá——nóng quá đi——fua——thích lắm——\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」
- Lý do: ふあっ → fua (giữ thường giữa dòng như audit).

### 23. key 1477 [凪] — vowel-count
- JP: 「ひゅあああっっ！　来た！　奥！　奥！　奥！　奥っ！\nにいさんの、あの凄かとが！　うちの、子宮！　にっ！」
- TW: 「呀！來了！裡面！裡面！裡面！裡面！大哥哥的噴泉！要來咱的子宮了！」
- Cũ: 「Hyuaaaaa! Đến rồi! Tận cùng! Tận cùng! Tận cùng! Tận cùng!\nThứ tuyệt vời đó, của anh Soutetsu! Vào tử cung, của em! Vào!」
- Mới: 「Hyuaaa! Đến rồi! Tận cùng! Tận cùng! Tận cùng! Tận cùng!\nThứ tuyệt vời đó, của anh Soutetsu! Vào tử cung, của em! Vào!」
- Lý do: ひゅあああっっ = ひゅ + あ×3 → "Hyuaaa" (cũ "Hyuaaaaa" 5 a, thừa 2).

### 24. key 1483 [凪] — vowel-count
- JP: 「ひゅぁぁぁぁぁぁぁんっ！！」
- TW: 「呀！！」
- Cũ: 「Hyuaaaaaa!!」
- Mới: 「Hyuaaaaaaan!!」
- Lý do: ひゅぁぁぁぁぁぁぁんっ = ひゅ + ぁ×7 + ん → 7 a + n (cũ 6 a, thiếu 1).

### 25. key 1491 [ふかみ] — vowel-count
- JP: 「ひゅあああああんっ！？　奥っ！　子宮――\n赤ちゃ！　赤ちゃん、できる、お部屋、ごちゅって！」
- TW: 「呀？！裡面！子宮……小寶寶！小寶寶的房間……被捅到了！」
- Cũ: 「Hyuaaaaaan!? Tận cùng! Tử cung——\nEm b! Căn phòng, tạo ra, em bé, bị đâm trúng rồi!」
- Mới: 「Hyuaaaaan!? Tận cùng! Tử cung——\nEm b! Căn phòng, tạo ra, em bé, bị đâm trúng rồi!」
- Lý do: ひゅあああああんっ = ひゅ + あ×5 + ん → 5 a + n (cũ 6 a, thừa 1).

### 26. key 1507 [凪] — vowel-count
- JP: 「はぁっ！　はあっ！　はあっ！　えふっ！　はっ――\nはぁっ！　――はぁ……ふぅ……はぁ……はぁ……はぁ」
- TW: 「呼！呼！呼！嘔！呼……呼！呼……呼……呼……呼……呼」
- Cũ: 「Ha! Ha! Ha! Efu! Ha——\nHa! ——Ha……fu……ha……ha……ha」
- Mới: 「Haa! Haa! Haa! Efu! Ha——\nHaa! ——Haa……fuu……haa……haa……haa」
- Lý do: はぁっ/はあっ ×3 → Haa; はぁっ → Haa; はぁ…… ×4 → Haa……; ふぅ…… → fuu…… (ふぅ = 2 u). はっ―― "Ha——" giữ (1 a). えふっ "Efu" giữ.

### 27. key 1552 [凪] — vowel-count
- JP: 「んっふふーん、どうばい？」
- TW: 「哼哼，怎麼樣？」
- Cũ: 「Nfufun, sao hả?」
- Mới: 「Nfufuun, sao hả?」
- Lý do: んっふふーん: ふふーん kéo dài (ー) → "Nfufuun" (cũ "Nfufun" mất độ dài). Tiếng cười khúc khích, giữ dạng romaji.

### 28. key 1574 [ふかみ] — vowel-count
- JP: 「はぁっ――あっ――あっ――（ごくっ）――んっ――\nおなか――しきゅう――おまんこ――いっぱい――ぁ」
- TW: 「啊……啊，啊……（咕咚）嗯……肚子裡……子宮裡……下面……滿了……啊」
- Cũ: 「Ha——a——a——（Ực）——ưm——\nbụng——tử cung——cô bé——đầy ắp rồi——a」
- Mới: 「Haa——a——a——（Ực）——ưm——\nbụng——tử cung——cô bé——đầy ắp rồi——a」
- Lý do: はぁっ―― → "Haa——" (2 a; cũ "Ha——" thiếu 1 a).

### 29. key 1599 [ふかみ] — vowel-count
- JP: 「はぁ！　はぁ！　はぁ！　はぁ！　凪ちゃん！\n凪ちゃん！　凪ちゃん、凪ちゃん、凪ちゃん、凪ちゃん」
- TW: 「啊！啊！啊！啊！小凪！小凪！小凪，小凪，小凪，小凪」
- Cũ: 「Ha! Ha! Ha! Ha! Nagi!\nNagi! Nagi, Nagi, Nagi, Nagi」
- Mới: 「Haa! Haa! Haa! Haa! Nagi!\nNagi! Nagi, Nagi, Nagi, Nagi」
- Lý do: はぁ！ ×4 → "Haa!" ×4 (mỗi token 2 a).

### 30. key 1614 [双鉄] — vowel-count
- JP: 「はぁっ、はぁっ、はぁっ、はぁっ」
- TW: 「啊，啊，啊，啊」
- Cũ: 「Ha, ha, ha, ha」
- Mới: 「Haa, haa, haa, haa」
- Lý do: はぁっ ×4 → "Haa, haa, haa, haa" (mỗi token 2 a; giữ hoa/thường theo vị trí).

### 31. key 1677 [ふかみ] — vowel-count
- JP: 「んっ！？　ぷぁっ！　あっ！？　ぁ――はあっ！？\nそんな、いき――なりっ――ぁぁぁあああああんっ！」
- TW: 「嗯？！哇！啊？！啊……啊？！怎麼突然……啊！」
- Cũ: 「Ưm!? Pua! A!? A——ha!?\nSao lại, đột ngột——thế——aaaaaan!」
- Mới: 「Ưm!? Pua! A!? A——haa!?\nSao lại, đột ngột——thế——aaaaaaaan!」
- Lý do: はあっ → "haa" (2 a); ぁぁぁあああああんっ = ぁ×3 + あ×5 + ん = 8 a + n → "aaaaaaaa" + "n" (cũ 6 a, thiếu 2). ぷぁっ "Pua" giữ.

### 32. key 1695 [凪] — vowel-count
- JP: 「ぶはっっ！　かはっ！　ごほっ！　げほっ！！\nえうっ！　あっ！　あ～～っ！　はぁっ！　はぁっ！！」
- TW: 「噗！啊！咳咳！咳咳！！嘔！啊！啊！呼！！」
- Cũ: 「Buha! Kaha! Goho! Geho!!\nEu! A! A~~! Ha! Ha!!」
- Mới: 「Buha! Kaha! Goho! Geho!!\nEu! A! A~~! Haa! Haa!!」
- Lý do: はぁっ ×2 → "Haa" ×2 (mỗi token 2 a). あ～～っ "A~~" giữ (dấu ~ đã diễn độ dài).

### 33. key 1789 [双鉄] — vowel-count
- JP: 「ああっ、挿れて――いるっ――」
- TW: 「是啊……插著呢」
- Cũ: 「A, đang cắm vào——đây——」
- Mới: 「Aa, đang cắm vào——đây——」
- Lý do: ああっ → "Aa" (2 a; cũ "A" thiếu 1 a; tiền lệ file mẫu 1314: ああっ "A"→"Aa").

### 34. key 1485 [凪] — vowel-count
- JP: 「や、あっ！？　ふかみ、ちゃんっ――ンッ――じっと、\n見ちゃ、や――うちが――ずぼずぼっ――あうぅっ！？」
- TW: 「呀，啊？！小深……嗯……別盯著……咱看……咱正在被……啊？！」
- Cũ: 「D, á!? Fukami——ưm——đừng,\nnhìn chằm chằm thế——em đang——bị đâm phập phập——au!?」
- Mới: 「D, á!? Fukami——ưm——đừng,\nnhìn chằm chằm thế——em đang——bị đâm phập phập——auu!?」
- Lý do: あうぅっ = あ+う+ぅ = 3 nguyên âm → "auu" (cũ "au" thiếu 1 u; công thức: số nguyên âm = 1 + số う/ぅ = 3).

## 4. Dòng rên giữ nguyên (đáng chú ý)

- Gasp Ư (audit, 15 dòng — 1003, 1005, 1493, 1537, 1563, 1566, 1607, 1609, 1624, 1675, 1697, 1968, 2081, 2121, 2217): KHÔNG đụng lại, theo luật khoá.
- Họ ひゃ/ひゅ/ひあ/きゃ đã romaji đúng: 1475 Kyaaa♪ (3 a), 1476 Hyau!, 1479 Hyua, 1481 Hahyu, 1484 Hyuaaaaaaaaaa (đếm lại: 10 a, đúng), 1488 Hya!?, 1490 Hya!?, 1521 Pua! Kyaaaan♪ (4 a + n), 1595 hyan, 1657 hyau, 1730 kya. やっ → "Á" giữ (tiền lệ file mẫu 1227/1440 — や không nằm trong danh sách romaji của quy tắc 3b).
- くっ → "Hự" giữ (1395, 1446, 1546, 1559; tiền lệ file mẫu 1232). っ đơn → "Hự" giữ (1004, 1592). んっ → "Ưm" giữ (1495, 1555, 1564, 1645, 1659, 1666, 1678, 1746).
- Cười khúc khích = tiếng cười, không phải rên: 1548 Fufufu~n, 1550/1554 Fufu-n (audit), 1611 ufufufufu, 1685/1686/1687/1689/1693/1794 Ufufu, 1007 Ufufu, 1616 ufufu.
- Hơi thở "fu" giữ nguyên kiểu romaji của file: 1645 "fu——", 1659 "fu——", 1679 "fu——" (ふっ); 1608 Fuha!!! (ふはっ), 1567 Fuku!!? (ふくっ), 1520 Kuo! (くおっ), 1526 Kua!! (くあっ), 1561 Kuha!!!!! (くはっ), 1562 Nku! (んくっ), 1525 Pua! (ぷあっ), 1647 Puha (ぷは), 1643/1646 pua (ぷぁ).
- SFX liếm/mút/chụt giữ nguyên kiểu động từ Việt của file (âm vẫn đủ, độ dài diễn bằng lặp chữ): 1630–1646, 1660–1661, 1627, 1633 Liếmmmm…/Chụtttt…, 1635/1638 Mút!/Phập!, 1698 Liếmmmmmm!!, 1776 liếm, 1838 Liếmmmmm!. SFX trong ngoặc độc thoại giữ nguyên: 2302/2300 Phụt!, 2316 Tuộtttttt!!, 2326/2325/2321/2314 Phập!, 2340/2341/2305 Siết!!!, 2336 uuuuuuuuuu!, 2297 Phụt!, 2299 Trượttttt!.
- はうっ → "Hau"/"hau" giữ (1587, 1841): âm はう đã diễn, っ chỉ là cắt cụt — đúng quyết định của audit ở 1624 (うあっ cuối dòng giữ "Ua", không thêm Ư).
- 1384 いきゅぅぅ…んんんっ → "Ra mấtttt…!!" giữ: quy ước dự án イク→"Ra mất"; âm kéo dài diễn bằng lặp chữ t.
- Nói ngọng khi ngậm (garbled speech, KHÔNG phải dòng rên — quy tắc 3b): 1375, 1545, 1550 — audit đã dịch theo TW, moan không đụng.
- Thán từ ngạc nhiên giữ tiếng Việt tự nhiên, không đếm nguyên âm: 1543 ええっ→"Ể", 1622 えっ→"Hả", 1533/1539 ふえっ→"Huể". ああ! trong độc thoại (2009, 1791, 2028, 2219, 2031) là "à, ra là vậy" — không phải rên, giữ nguyên.

## 5. Flags (đợt thống nhất / parent xem lại — không tự quyết)

- F1 (1502/1505): audit gộp ふ……ぁ / ふっ……あ―― thành "Phà"; moan khôi phục "Fu……a——" theo kiểu "fu" của file (1645/1659/1679). Nhưng file mẫu 凪ふかみh1 giữ "phù" cho ふっ (1227). Đợt thống nhất cần chốt một kiểu cho hơi thở ふっ/ふ: "fu" hay "phù".
- F2 (1590): "Áaaa" → "Áaa" (やああ = 3 mora a) — đếm lại độc lập vì khác với audit giữ nguyên; cần parent kiểm chứng số a.
- F3 (1552): "Nfufun" → "Nfufuun" (độ dài ーん). Audit ở 1550 dùng "Fufu-n" cho ふふーん — hai kiểu khác nhau trong cùng file; đợt thống nhất nên chọn một kiểu cho ふふーん.
- F4: chuỗi SFX liếm/mút dài (1630–1661, 1633, 1698, 1776, 1838) giữ kiểu động từ Việt ("liếm/chụt/mút") — đã thống nhất theo file; nếu đợt thống nhất muốn romaji thì rà lại toàn bộ.
- F5 (1695/1507): あ～～っ giữ "A~~" (dấu ~ diễn độ dài) trong khi はぁっ sửa thành "Haa" — hai kiểu diễn độ dài khác nhau trong cùng dòng; ghi chú để đợt thống nhất xem có cần thống nhất không.
- F6: 1587/1841 はうっ giữ "Hau" (không thêm dấu cắt cụt) — theo quyết định audit 1624; nếu đợt thống nhất muốn diễn っ cắt cụt ở cuối tuyệt đối thì rà lại cùng 1624.

## 6. Sweep

- Sweep có 17 mục cho file này — đã kiểm chứng trực tiếp trong sweep-raw-gasp-wrong.json:
  - 13 fix lost-gasp đã áp nguyên trong audit (1003, 1005, 1493, 1537, 1566, 1607, 1609, 1675, 1697, 1968, 2081, 2121, 2217) + 1 bỏ sót audit bắt được (1624): moan KHÔNG đụng.
  - 3 already-rendered: 1395 (くっ→"hự"), 1495 (ん――っ→"ưm"), 1563 (audit đã thêm Ư cho ～～～っ): đúng, không đụng.
  - 1 needs-file-audit (1838): đã kiểm tra — ん～～っ → "ưm~~" và ぺろおおおおっ → "Liếmmmmm" đều đã diễn âm; không đổi.
- Không có mục sweep nào bị moan sửa; không phát hiện gasp mới ngoài sweep (audit đã quét 288 dòng chứa っ).

## 7. Lượt soát 2

- Tổng 34 / tái kiểm chứng 34 / bỏ 0 / sửa 1. Mỗi fix đã đọc lại vs JP + TW lần 2.
- 1 sửa trong lượt soát 2: 1491 đếm a bằng mắt ghi 6 a, kiểm chứng cơ học cho thấy JP ひゅあああああん = 5 a → sửa fix thành 5 a ("Hyuaaaaaan"). Sau đó xây lại 1483/1491/1677 bằng phép đếm trong code ("a"*n) để khỏi đếm nhầm bằng mắt.
- JSON 34 mục, khóa string, jp/tw/old_vn khớp CSV3 34/34. Khối TOML parse bằng tomllib: 34 khóa, 0 sai lệch giá trị.
- Kiểm chứng cơ học (difflib): fix vs GIÁ TRỊ AUDIT của 22 key trùng audit chỉ khác đúng token rên (Phà/phà → Fua/Fa/fua/fa/Fu + 2 chỉnh đếm a ở 1581/1590). 12 key còn lại không trùng audit (fix xây trên CSV3).

## 8. Khối TOML

```toml
[script]
1479 = "「Hyua! A! Ha! Thế này! Tuyệt quá!\\nFua! Bị làm, nhiều thế này, Bổn tiểu thư——」"
1481 = "「Hahyu! Ưm! Fua! A! Đầu em!\\nCơ thể em! Cô bé! Nóng quá! Nóng, quá!」"
1502 = "「Fu……a——anh Soutetsu, dữ tợn quá đi」"
1505 = "「Fu……a——（Khịt, khịt）——Tuyệt, quá……\\nTinh dịch……mùi, nồng hơn, mọi khi……fa——」"
1509 = "「Fua——a——tuyệt quá——tuyệt quá——fua!\\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」"
1510 = "「Fa……a——a——Fukami,\\ncậu mút hơi mạnh quá rồi đấy.」"
1512 = "「Fa——Fukami——trên mặt Fukami cũng,\\ntinh dịch của anh Soutetsu——khô lại, cứng đơ rồi kìa」"
1513 = "「Fa——Fukami, Fukami……ưm……\\nChụt——liếm——liếm——ưm——chụt——chụt」"
1522 = "「Fua! A! A! A!」"
1523 = "「Fua! A! A! A!!!」"
1532 = "「Fua!? A——cái này——không——a!\\nTớ——tớ——sẽ trở nên——kỳ lạ, mất」"
1581 = "「A——Fukami——haa——fa——ưm」"
1583 = "「A……（Khịt khịt——khịt, khịt——）\\nFa……Mùi cương cứng của, anh Soutetsu.」"
1590 = "「Fua! Á! Đừng rút ra! Áaa!!」"
1595 = "「A! Fua! Cái đó! Cả cái đó nữa!!\\nHãy cho em cả đợt mới đi! Cho em——hyan!?」"
1597 = "「Fua! A! A! A!」"
1598 = "「Fua! A! A! A!\\nAnh Soutetsu! Anh Soutetsu! Anh Soutetsu! Anh Soutetsu!」"
1603 = "「Fua! A! Cái này! Chính là cái này! Ưm!——\\nĐây mới là anh Soutetsu! Là cậu nhỏ của anh Soutetsu của em!」"
1619 = "「Fa——Fukami——ưm——chụt——liếm,\\nliếm——chụt——chụt——chụt——chụt」"
1657 = "「Khoan!? Nagi! Fua! Không được!\\nThế này! Tớ! Tớ——sẽ sướng quá mất——hyau!」"
1658 = "「U……a……khắp mặt, nhớp nháp quá đi——ưm……\\nChụt——（Ực）——fa——đặc dính luôn~」"
1714 = "「Nóng quá——nóng quá đi——fua——thích lắm——\\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」"
1477 = "「Hyuaaa! Đến rồi! Tận cùng! Tận cùng! Tận cùng! Tận cùng!\\nThứ tuyệt vời đó, của anh Soutetsu! Vào tử cung, của em! Vào!」"
1483 = "「Hyuaaaaaaan!!」"
1491 = "「Hyuaaaaan!? Tận cùng! Tử cung——\\nEm b! Căn phòng, tạo ra, em bé, bị đâm trúng rồi!」"
1507 = "「Haa! Haa! Haa! Efu! Ha——\\nHaa! ——Haa……fuu……haa……haa……haa」"
1552 = "「Nfufuun, sao hả?」"
1574 = "「Haa——a——a——（Ực）——ưm——\\nbụng——tử cung——cô bé——đầy ắp rồi——a」"
1599 = "「Haa! Haa! Haa! Haa! Nagi!\\nNagi! Nagi, Nagi, Nagi, Nagi」"
1614 = "「Haa, haa, haa, haa」"
1677 = "「Ưm!? Pua! A!? A——haa!?\\nSao lại, đột ngột——thế——aaaaaaaan!」"
1695 = "「Buha! Kaha! Goho! Geho!!\\nEu! A! A~~! Haa! Haa!!」"
1789 = "「Aa, đang cắm vào——đây——」"
1485 = "「D, á!? Fukami——ưm——đừng,\\nnhìn chằm chằm thế——em đang——bị đâm phập phập——auu!?」"
```

Kết bài: file lr_凪ふかみh1_じぇいけい！ — 34 dòng rên đã sửa (21 romaji fa/fu + 12 đếm nguyên âm + 1 sai âm), 195 dòng rên/SFX giữ nguyên, sweep 17 mục không đụng, audit 22 key trùng chỉ khác token rên. Quy tắc fa/fu → romaji trong rên H-scene đã áp nhất quán theo tiền lệ file mẫu.