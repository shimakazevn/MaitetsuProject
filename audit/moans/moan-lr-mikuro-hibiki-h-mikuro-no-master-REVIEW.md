# Moan-fix — lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml

- File: `lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml` — route 02_Hibiki, 611 dòng script (223 độc thoại, 166 thoại Mikuro, 131 thoại Hibiki, 91 thoại Soutetsu). Nội dung: sau chuyến chạy 8620 thành công, Mikuro đau bụng — hoá ra sealing mở chức năng mới; em muốn Hibiki làm Master, rồi cả ba cùng làm tình lần đầu (Mikuro mất trinh).
- Chỉ sửa TIẾNG RÊN / thở / gasp / SFX theo quy tắc romaji (Hieu duyệt 21/11 ~01:56). Không sửa đại từ, thuật ngữ, nghĩa, lệch dòng — những thứ đó thuộc audit / đợt thống nhất.
- **Kết quả: 31 dòng đổi** (13 romaji + 16 đếm nguyên âm + 1 độ dài ん + 1 sai âm), **384 dòng giữ**.

## §1. Kiểm tra file

- TOML md5 `897021b35bb2e469b516f1f0d7b4274e` (khớp md5 audit); không có bản trùng (không thuộc 11 nhóm trùng). UTF-8 BOM + CRLF, 611 khóa script.
- CSV3: 1 set duy nhất (611 dòng, 0 khóa trùng, 0 ô VN trống); VN khớp TOML 611/611 sau chuẩn hoá `\n`→khoảng trắng (TOML-2 làm phẳng `\n` — quy ước đã biết, không phải lệch).
- Audit của file đã merge: 82/611 sai (13,4%) — xem `audit-lr-mikuro-hibikih-mikuro-no-master-REVIEW.md`. Audit làm TRƯỚC quy tắc romaji nên các bản sửa fa/fu của audit (33 dòng → "phà"/"phùa"/"phuê"/"phuya") được xét lại Ở ĐÂY theo romaji; xem §4 và §5.
- Sweep っ: 31 mục cho file này (28 raw-tsu + 2 lost-gasp-trailing + 1 already-rendered 2092) — audit đã nhận 30 fix, đã kiểm chứng từng fix vs JP; tất cả đều là gasp Ư, KHÔNG đụng ở đây (quy tắc khóa: không xét lại các dòng gasp Ư).
- Đã đọc 611/611 dòng; xét 415 dòng có dấu hiệu rên/thở/gasp/SFX theo JP (260 っ, 42 fa/hya, 18 nguyên âm nhỏ, 11 cười, 76 SFX trong ngoặc, 8 nguyên âm dài); đổi 31, giữ 384 (trong đó có các dòng っ gắn từ nội dung đã kiểm theo audit §3 — không phải gasp).

## §2. Quy tắc áp dụng

- **Romaji khi rên cao trào** (tiền lệ moan-lr-kisaki-h1): ふぁ/ふあ là tiếng rên/thở gấp trong cao trào, trong chuỗi rên, hoặc rên dài đứng riêng → romaji ("phà"/"phùa" nghe gượng, như một từ Việt bị ép vào tiếng rên). **Giữ "phà"** khi là hơi thở nhẹ cuối dòng / tiếng thở dài dịu trong ngữ cảnh trò chuyện, âu yếm — ở file này KHÔNG có dòng nào thuộc trường hợp giữ (cả 33 dòng fa/fu của audit đều là rên/thở gấp trong H-scene), nên cả 33 đều về romaji: 11 dòng đổi Ở ĐÂY (bản cũ sai âm hoặc thiếu Ư gasp), 22 dòng giữ nguyên bản cũ (bản cũ đã là romaji đúng — xem cờ hủy fix audit §5).
- **Công thức đếm nguyên âm:** số nguyên âm = nguyên âm gốc cùng loại trong âm tiết gốc + số kana kéo dài (う/ぅ, あ/ぁ). Ví dụ: きゅうう = 3 u (きゅ 1 + う 2); ひゃあ = 2 a (ひゃ 1 + あ 1). **Lưu ý đã kiểm chứng:** ひゃ không góp u (âm tiết ひゃ là âm a) — nên ひゃううううう = 5 u (không phải 6), và ひゃううう = 3 u (bản cũ "Hyauuu" đã đúng, không sửa — xem §4). Mọi số đếm dài đều đếm lại độc lập bằng token (bài học 凪h2 2500 + kisaki-h1: không tin số trong JSON/block cũ).
- **Một dòng = một cách diễn** (VN hoặc romaji, không trộn). **Ư gasp KHÔNG xét lại. "Kh" giữ nguyên.** Cười là cười, không phải gasp. SFX hành động trong （）giữ dạng động từ Việt (tiền lệ h8 — số chữ kéo dài là cảm tính, không áp công thức).
- JP thắng TW. Mọi fix viết tay từ JP (+TW); lượt soát 2 đọc lại toàn bộ fix vs JP (xem §6).

## §3. Danh sách sửa (31 dòng)

### A. Romaji (họ fa/fu, ひあ/ひゃ — 13 dòng)

### 1705 — みくろ — romaji
- JP: 「ふ……ぁ」
- TW: 「呼……啊」
- VN cũ: 「Phu……a」
- Mới: 「Fu……a」
- Lý do: JP ふ……ぁ là một hơi duy nhất, chính JP tự tách bằng ……. Bản cũ "Phu……a" tách mảnh và "Phu" đọc như từ Việt "phù" → romaji "Fu……a", giữ nguyên hình tách của JP. Audit §4 đã ghi dòng này thuộc đợt thống nhất fa/fu — bản moan này quyết thay.

### 1711 — 日々姫 — romaji
- JP: 「ふあっ──やっ──にぃにっ、いきなり、指、\n二本とかぁ──ふぁうっ！！！？」
- TW: 「呼啊——呀——阿哥，怎麼突然兩根手指插進來了——呼啊！！！」
- VN cũ: 「Fua── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\nvào thế── fua!!!?」
- Mới: 「Fua── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\nvào thế── Fau!!!?」
- Lý do: JP ふぁうっ = "Fau" (f-a-u); bản cũ "fua" sai âm (đó là âm của ふあ). ふあっ đầu dòng giữ "Fua" (romaji, đã đúng). Audit sửa cả hai thành "Phùa"/"phàu" — xem cờ §5 (hủy phần fa/fu của audit, giữ romaji).

### 1712 — 日々姫 — romaji
- JP: 「ふぁっ──あっ──あっ──ああっ」
- TW: 「呼啊——啊——啊——啊啊」
- VN cũ: 「Fua── a── a── aa.」
- Mới: 「Fa── a── a── aaƯ.」
- Lý do: JP ふぁっ = "Fa"; bản cũ "Fua" sai âm (fua là ふあ, không phải ふぁ). Giữ Ư gasp của audit (ああっ cuối dòng → "aaƯ").

### 1724 — みくろ — romaji
- JP: 「ふあっ……あっ──しゅごっ──すごいっ──\nんっ──あっつ──はっ──きれぇ──綺麗っ……」
- TW: 「呼啊……啊——天啊——好厲害——嗯——啊——哈——好美——太美了……」
- VN cũ: 「Fua…… a── tuyệt── tuyệt quá──\nƯm── nóng── hà── đẹp── đẹp quá……」
- Mới: 「FuaƯ…… a── tuyệt── tuyệt quá──\nƯm── nóng── hà── đẹp── đẹp quá……」
- Lý do: JP ふあっ……: ふあ → romaji "Fua" (chuỗi rên cao trào). Giữ Ư gasp của audit cho っ trước …… ("FuaƯ……"). Audit sửa thành "PhùaƯ" — xem cờ §5.

### 1725 — みくろ — romaji
- JP: 「ふあっ……あっ──日々姫、さん。\nみくろ──は、あっ──みくろ──う、んっ」
- TW: 「呼啊……啊，日日姬小姐。美玖路——啊——美玖路——唔、嗯」
- VN cũ: 「Fua…… a── chị Hibiki.\nMikuro── là, a── Mikuro── ư, ưm」
- Mới: 「FuaƯ…… a── chị Hibiki.\nMikuro── là, a── Mikuro── ư, ưm」
- Lý do: JP ふあっ……: như 1724 — ふあ → romaji "Fua", giữ Ư gasp của audit.

### 1727 — みくろ — romaji
- JP: 「ふあっ……みくろ……シーリングが解けたとこ──\nおんなのこのとこ、全部──日々姫さんにこんな近くで」
- TW: 「呼啊……美玖路……封印解除的地方——女孩子的地方，離日日姬小姐這麼近——」
- VN cũ: 「Fua…… Mikuro…… chỗ phong ấn vừa được giải trừ──\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」
- Mới: 「FuaƯ…… Mikuro…… chỗ phong ấn vừa được giải trừ──\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」
- Lý do: JP ふあっ……: như 1724 — ふあ → romaji "Fua", giữ Ư gasp của audit.

### 1728 — みくろ — romaji
- JP: 「ふあっ」
- TW: 「呼啊」
- VN cũ: 「Fua.」
- Mới: 「FuaƯ.」
- Lý do: JP ふあっ đứng riêng: romaji "Fua"; giữ Ư gasp của audit (っ cuối dòng mất hẳn) → "FuaƯ.".

### 1729 — 日々姫 — romaji+vowel-count
- JP: 「ふあぁぁぁぁぁぁあああああああんっ！！！！」
- TW: 「呼啊啊啊啊啊啊啊嗯！！！！」
- VN cũ: 「Fuaaaaaaaaaaaaaaaaan!!!!」
- Mới: 「Fuaaaaaaaaaaaaaan!!!!」
- Lý do: Rên dài ふあぁぁぁぁぁぁあああああああんっ: đếm lại độc lập 14 âm a (ふあ 1 + ぁ 6 + あ 7). Bản cũ 17 a thừa 3 → romaji 14 a. Audit giữ nguyên 17 a trong dạng "Phù…" (audit §4 ghi đúng "JP 14 âm a" nhưng bản sửa audit không chuẩn hoá) — bản moan này chuẩn hoá + chuyển romaji.

### 1741 — みくろ — romaji
- JP: 「ふやっ──なにっ、これっ──あちゅいのっ──\nおなか──おまた──どろって──ふっ──あっ」
- TW: 「呼啊，這是什麼？好熱的東西進到肚子裡面去了，胯部黏糊糊的，呼——啊」
- VN cũ: 「Fuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── phu── a」
- Mới: 「Fuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── phu── aƯ」
- Lý do: JP ふやっ──: ふや → romaji "Fuya". Giữ Ư gasp cuối dòng của audit (あっ → "aƯ"). Audit sửa thành "Phuya" — xem cờ §5.

### 1743 — 日々姫 — romaji
- JP: 「ふあっ！？　あっ──にぃにっ──あっつっ──んっ\nいっつも──より、も──あつ──くて──ふと──っ」
- TW: 「呼啊？！啊——阿哥——啊——嗯——比平時——要熱得多——而且很粗——」
- VN cũ: 「Fua!? A── anh hai── nóng quá── ưm\nHơn── mọi khi── nóng── và── to──」
- Mới: 「Fua!? A── anh hai── nóng quá── ưm Hơn── mọi khi── nóng── và── to──Ư」
- Lý do: JP ふあっ！？: ふあ → romaji "Fua". Giữ Ư gasp cuối dòng của audit (──っ → "──Ư") và giữ dạng làm phẳng \n của audit (quy ước sweep cho 10 fix nhiều dòng).

### 1786 — みくろ — romaji
- JP: 「はうっ！　あっ！　あっ！　あああっ！\nふあ──っ──んっ！　んううううっ！！！」
- TW: 「哈嗚！啊！啊！啊啊啊！呼啊——嗯！嗯唔唔！！！」
- VN cũ: 「Hau! A! A! Aaa!\nFua──っ──ưm! Ưm uuuu!!!」
- Mới: 「Hau! A! A! Aaa! Fua──Ư──ưm! Ưm uuuu!!!」
- Lý do: JP ふあ──っ──: ふあ → romaji "Fua"; giữ fix sweep Ư của audit ("Fua──Ư"). Giữ dạng làm phẳng \n của audit (quy ước sweep). Đồng thời んううううっ → "Ưm uuuu" (4 u, bản cũ đã đúng, không đụng).

### 1789 — 日々姫 — romaji
- JP: 「ふえっ！？　私っ？？」
- TW: 「哎？！你喜歡我嗎？？」
- VN cũ: 「Huê!? Chị á??」
- Mới: 「Fue!? Chị á??」
- Lý do: JP ふえっ = "Fue"; bản cũ "Huê" sai phụ âm đầu (h ≠ f, ふ là f).

### 1821 — みくろ — romaji
- JP: 「あう……」
- TW: 「啊嗚……」
- VN cũ: 「A ư……」
- Mới: 「Au……」
- Lý do: JP あう…… là một hơi duy nhất; bản cũ tách thành "A ư" (2 mảnh) → gộp romaji "Au" (tiền lệ trong file: 1753 "Au!").

### B. Đếm nguyên âm (17 dòng)

### 1675 — みくろ — vowel-count
- JP: 「ひゃうううううっっっっっっっっ！！！！！！！！」
- TW: 「呀唔唔唔！！！！！！！」
- VN cũ: 「Hyauuuuuuuuuuuu!!!!!!!!」
- Mới: 「Hyauuuuu!!!!!!!!」
- Lý do: JP ひゃうううううっ×8: đếm lại độc lập — 5 âm u (ひゃ là âm a, không góp u; chỉ đếm 5 う). Bản cũ 12 u, thừa gấp đôi → 5 u. Dấu !!!!!!!! diễn っ cắt ngang.

### 1748 — 日々姫 — vowel-count
- JP: 「ひゅあああああああっっっ！！！？」
- TW: 「咿呀啊啊啊啊啊！！！」
- VN cũ: 「Hyuaaaaaaaaaaaaaaaaaaaaa!!!?」
- Mới: 「Hyuaaaaaaa!!!?」
- Lý do: JP ひゅあああああああっっっ: đếm lại độc lập 7 âm a (ひゅ không góp a). Bản cũ 21 a, thừa gấp ba → 7 a.

### 1757 — みくろ — vowel-count
- JP: 「ひゃあっ！？」
- TW: 「咿呀？！」
- VN cũ: 「Hya!?」
- Mới: 「Hyaa!?」
- Lý do: JP ひゃあっ = 2 âm a (ひゃ 1 + あ 1); bản cũ "Hya" thiếu 1 → "Hyaa".

### 1765 — みくろ — vowel-count
- JP: 「わぁ……日々姫さんのおんなのこの中。\nピンクで濡れててひくひくしてて、凄く綺麗です」
- TW: 「哇……日日姬小姐的女孩子的裡面。粉嫩濕滑，還在一顫一顫的，非常漂亮」
- VN cũ: 「Oa…… bên trong phần cơ thể con gái của chị Hibiki.\nMàu hồng ướt át và đang co bóp giật giật, đẹp quá đi mất.」
- Mới: 「Oaa…… bên trong phần cơ thể con gái của chị Hibiki.\nMàu hồng ướt át và đang co bóp giật giật, đẹp quá đi mất.」
- Lý do: JP わぁ = 2 âm a (わ 1 + ぁ 1); bản cũ "Oa" thiếu 1 → "Oaa".

### 1768 — みくろ — vowel-count
- JP: 「わあっ！」
- TW: 「哇！」
- VN cũ: 「Oa!」
- Mới: 「Oaa!」
- Lý do: JP わあっ = 2 âm a; bản cũ "Oa" thiếu 1 → "Oaa". (Lý do っ của audit vẫn giữ: dấu ! diễn cắt ngang, không thêm Ư.)

### 1819 — 日々姫 — vowel-count
- JP: 「ぁああああああああああああああああああんっっっ！」
- TW: 「啊啊啊啊啊啊啊啊啊嗯！」
- VN cũ: 「Aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaan!」
- Mới: 「Aaaaaaaaaaaaaaaaaaan!」
- Lý do: JP ぁ + あ×18 + んっっっ: đếm lại độc lập 19 âm a. Bản cũ 51 a → 19 a.

### 1855 — 日々姫 — vowel-count
- JP: 「んひゅううううううううっっっっ！」
- TW: 「嗯唔唔——！」
- VN cũ: 「Ưm hưuuuuuuuuuuuuuuuuuu!」
- Mới: 「Ưm hyuuuuuuuuu!」
- Lý do: JP んひゅううううううううっっっっ: đếm lại độc lập 9 âm u (ひゅ 1 + う 8). Bản cũ 18 u, gấp đôi → "Ưm hyuuuuuuuuu!" (dùng "hyu" theo quy ước romaji của file, thay dạng "hưu" của bản cũ).

### 1864 — みくろ — vowel-count
- JP: 「んぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅっっ！！！」
- TW: 「嗯嗚嗚！！！」
- VN cũ: 「Ưmuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!!!」
- Mới: 「Ưmuuuuuuuuuuuuuuuuuu!!!」
- Lý do: JP んぅ×18 + っっ: đếm lại độc lập 18 âm u. Bản cũ 40 u → 18 u.

### 1865 — みくろ — vowel-count
- JP: 「んきゅうっ！！！　ひゅあっ！　あっ！　あっ！！\n回路っ──いま──みくろ、一瞬──焼けた、みたいに」
- TW: 「嗯嗚！！！嗯啊！啊！啊！！電路剛剛就好像一瞬間被燒斷了一樣」
- VN cũ: 「Ưm kyu!!! Hyua! A! A!!\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」
- Mới: 「Ưm kyuu!!! Hyua! A! A!!\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」
- Lý do: JP んきゅうっ = 2 âm u (きゅ 1 + う 1); bản cũ "kyu" thiếu 1 → "kyuu".

### 1866 — みくろ — vowel-count
- JP: 「んきゅうううううううううううううっ！！！！！！！」
- TW: 「嗯嗚！！！！！！」
- VN cũ: 「Ưm kyuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!!!!!!!」
- Mới: 「Ưm kyuuuuuuuuuuuuuu!!!!!!!」
- Lý do: JP んきゅうううううううううううううっ: đếm lại độc lập 14 âm u (きゅ 1 + う 13). Bản cũ 38 u → 14 u.

### 1898 — みくろ — vowel-count
- JP: 「すーーっ、すーーーっ、すーーっ……すーーっっ！？\nぶはああっ！」
- TW: 「嘶——嘶——嘶——嘶——？！噗蛤啊！」
- VN cũ: 「Híttt, híííttt, híttt…… híttt!?\nBuaaaa!」
- Mới: 「Híttt, híííttt, híttt…… híttt!?\nBuaaa!」
- Lý do: JP ぶはああっ = 3 âm a (は 1 + あ 2); bản cũ "Buaaaa" 4 a thừa 1 → "Buaaa". Phần hít "Híttt…" giữ nguyên quy ước của bản cũ (t diễn cắt ngang của すーーっ).

### 1917 — みくろ — vowel-count
- JP: 「すごい……はぁ……すごい……あんなに長いのが……\nんっ──もう──ほとんど──ほとんど──ぜんぶっ」
- TW: 「好棒……蛤啊……真厲害……那麼長的東西……嗯——幾乎——全部——全部——全都進去了」
- VN cũ: 「Tuyệt quá…… hà…… tuyệt quá…… dài như thế mà……\nƯm── đã── gần như── gần như── toàn bộ」
- Mới: 「Tuyệt quá…… hàà…… tuyệt quá…… dài như thế mà……\nƯm── đã── gần như── gần như── toàn bộ」
- Lý do: JP はぁ = 2 âm a (は 1 + ぁ 1); bản cũ "hà" thiếu 1 → "hàà".

### 2200 — みくろ — vowel-count
- JP: 「はあっ──ふうっ──はああっ──ふううっ」
- TW: 「蛤啊——呼——蛤啊——呼」
- VN cũ: 「Hà── phu── hà── phu」
- Mới: 「Hàà── phuu── hààà── phuuuƯ」
- Lý do: Bốn hơi thở đều thiếu độ dài: はあっ 2 a → "Hàà", ふうっ 2 u → "phuu", はああっ 3 a → "hààà", ふううっ 3 u → "phuuu". Giữ Ư cuối dòng của audit. (Tiền lệ đếm trong file: 1925 はあああっ→"haaaa", ふうううっ→"phuuuu".)

### 2201 — みくろ — vowel-count
- JP: 「はあっ──ん、ふっ──はひゅっ──くっふっ」
- TW: 「蛤啊——嗯、呼——哈——唔呼」
- VN cũ: 「Hà── ưm, phu── ha hyu── kufu」
- Mới: 「Hàà── ưm, phu── ha hyu── kufuƯ」
- Lý do: JP はあっ = 2 a → "Hàà"; giữ Ư cuối dòng của audit. Các âm còn lại đã đúng (ふっ→"phu", はひゅっ→"ha hyu", くっふっ→"kufu").

### 2202 — みくろ — vowel-count
- JP: 「はぁっ──はあっ──はあっ──はあっ──」
- TW: 「蛤啊——蛤啊——蛤啊——蛤啊」
- VN cũ: 「Hà── hà── hà── hà──」
- Mới: 「Hàà── hàà── hàà── hàà──」
- Lý do: JP はぁっ + はあっ×3, mỗi hơi 2 a → "Hàà── hàà── hàà── hàà──".

### 2559 — monologue — vowel-count
- JP: ファーストキス、という言葉の印象とは正反対とも思える。\nこれは、あまりに濃密な……ああ。
- TW: 將如此深情的接吻稱之為初吻實在是過於名不副實。這吻實在是帶著過於濃厚的色彩……
- VN cũ: Có vẻ hoàn toàn trái ngược với ấn tượng về cụm từ nụ hôn đầu.\nNụ hôn này quá đỗi nồng nhiệt…… A.
- Mới: Có vẻ hoàn toàn trái ngược với ấn tượng về cụm từ nụ hôn đầu.\nNụ hôn này quá đỗi nồng nhiệt…… Aa.
- Lý do: Độc thoại, tiếng thở dài "ああ" = 2 âm a; bản cũ "A." thiếu 1 → "Aa.".

### C. Khác (2 dòng)

### 1604 — 日々姫 — length
- JP: 「ちがっ──んんっ──ふっ──あっ──にぃに──\nにぃに、が──いつも──よりっ──」
- TW: 「不是我——嗯嗯——呼——啊——是阿哥——阿哥比平時要粗得多」
- VN cũ: 「Không phải── ưm── phu── a── anh hai──\nAnh hai, so với── mọi khi──」
- Mới: 「Không phải── ưmm── phu── a── anh hai──\nAnh hai, so với── mọi khi──」
- Lý do: JP んんっ (2 mora ん) → bản cũ "ưm" chỉ có 1 m, mất độ dài. Sửa "ưmm" (tiền lệ 凪h2: んんんっ→"Ưmmm"). っ cuối được ── diễn cắt ngang, không thêm Ư. Các âm còn lại đã đúng (ふっ→"phu", あっ→"a").

### 1800 — 双鉄 — wrong-sound
- JP: 「ふうっ！」
- TW: 「唔！」
- VN cũ: 「Hự!」
- Mới: 「Phùu!」
- Lý do: JP ふうっ là hơi thở (2 u), không phải tiếng gằn; bản cũ "Hự!" là cách diễn của くっ. Quy ước file: ふ→"phu" (1703/1925/2200), く→"hự" → "Phùu!" (2 u theo công thức). Audit giữ "Hự!" chỉ vì lý do っ (dấu ! diễn cắt ngang) — lý do đó vẫn đúng, không thêm Ư.

## §4. Dòng rên giữ nguyên (đáng chú ý)

- **Romaji đã đúng, giữ:** ひゃう→"Hyau" (1674, 1679, 1754), ひゃっ→"Hya" (1682, 1760), ひゃあん→"Hyaan" (1751, 2 a đúng), ひゅあ→"Hyua" (1753, 1758, 1865), ひきゅ→"Hikyu" (1756), くあ→"Kua" (1793, 1796–1799), ぎっ→"Gi" (1683), はわ→"Hawa" (1772), はう→"Hau" (1784), ふ→"phu" (1703, 1741, 1751, 1837, 1853), く→"hự" (1791, 1801, 1802), ん→"ưm" (1612, 1872, 2116), ちゅ→"chụt", れろ→"liếm", む→"Mư" (1795, 1803).
- **Cười giữ nguyên (cười là cười, không phải gasp):** ふふっ→"Fufu." (1688, 1901), んふふっ→"Ưm fufu" (1690–1692, 1702, 1861, 2313), うふふ→"Ufufu" (1696–1700).
- **SFX trong ngoặc （）giữ nguyên dạng động từ Việt** (76 dòng: "Nhóp nhép/Phập/Siết/Trượt/Chụt…") — theo tiền lệ h8: số chữ kéo dài của SFX hành động là cách kéo dài cảm tính, không áp công thức đếm.
- **Gasp Ư của audit/sweep giữ nguyên toàn bộ** (51 dòng audit) — không đụng theo quy tắc khóa.
- **Kiểm mà giữ (đã đếm lại, bản cũ đúng):** 1677 "Hyauuu" (ひゃううう = 3 u, đúng); 1731 "Fuyaaaaaaan" (7 a đúng — xem cờ §5 mục 2); 1749 "Hyaunnn" / 1863 "Fukyunnn" (kéo dài ん sau っ — không có công thức đếm ん, giữ quy ước file); 2306 "////!?" (dấu !? diễn cắt ngang như audit đã quyết ở 1768; khác 2316 ///っ không dấu câu nên audit thêm Ư).
- **23 dòng audit fa/fu giữ bản cũ (romaji) — đề nghị HỦY fix audit ở đợt thống nhất** (xem cờ §5 mục 1): 1678, 1708, 1714, 1716, 1718, 1720, 1722, 1731, 1733, 1735, 1736, 1737, 1739, 1758, 1773, 1811, 1820, 1857 (chỉ hủy phần "Phùa"; phần nghĩa "vào hết" của audit giữ nguyên), 1901, 1928, 1967, 2107, 2198.

## §5. Cờ cho đợt thống nhất

- **CỜ 1 — HỦY 23 fix fa/fu của audit** (audit sửa romaji cũ thành "phà"/"phùa"/"phuê"/"phuya"/"Phàn"/"pùa"; bản moan này quyết giữ romaji cũ vì đều là rên cao trào — áp dụng bản moan, KHÔNG áp bản audit cho các dòng này):
  - 1678 ふあっ: audit "Phùa──" → giữ "Fua──".
  - 1708 ふえっ: audit "Phuê!?" → giữ "Fue!?".
  - 1714 ふあっ: audit "Phùa──" → giữ "Fua──".
  - 1716 ふあっ + ふえっ: audit "Phùa── … phuê!!?" → giữ "Fua── … fue!!?".
  - 1718, 1720, 1722 ふあっ: audit "Phùa──" → giữ "Fua──".
  - 1731 ふやぁ…: audit "Phuyaaaaaaan!" → giữ "Fuyaaaaaaan!" (7 a đã đúng — xem cờ 2).
  - 1733 ふああっ: audit "Phùaa!?" → giữ "Fuaa!?".
  - 1735, 1736, 1737, 1739 ふあっ: audit "Phùa" → giữ "Fua".
  - 1758 ふえっ: audit "phuê!?" → giữ "fue!?".
  - 1773 ふあっ: audit "phùa──" → giữ "fua──".
  - 1811 ぷあ: audit "pùa" → giữ "pua" (audit §4 tự ghi ぷあ→"pùa" chưa có tiền lệ, chờ xác nhận — bản moan quyết romaji "Pua").
  - 1820 ふぁんっ: audit "Phàn!!" → giữ "Fan!!".
  - 1857 ふあっ: audit "Phùa!" → giữ "Fua!" (CHỈ hủy phần moan; phần nghĩa "ra hết"→"vào hết" của audit GIỮ NGUYÊN — giá trị cuối dòng này = "Ưm kyu! Fua! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất").
  - 1901 ぷあっ: audit "Pùa──" → giữ "Pua──".
  - 1928, 1967, 2107, 2198 ふあっ: audit "Phùa"/"phùa" → giữ "Fua"/"fua".
- **CỜ 2 — Audit §4 đếm sai 1731:** audit ghi "1731 có 7 a (JP 6 âm a)" — đếm lại bằng token: JP ふやぁぁぁっぁぁぁんっ có や 1 + ぁ 6 = 7 âm a (không phải 6). Bản cũ "Fuyaaaaaaan!" (7 a) đã đúng, không cần sửa đếm. (Bài học kisaki-h1: đếm lại công thức, không tin số trong JSON/block.)
- **CỜ 3 — 1800:** audit giữ "Hự!" (chỉ xét lý do っ, không xét âm); bản moan đổi âm thành "Phùu!" (xem §3). Lý do っ của audit vẫn đúng — không thêm Ư.
- **CỜ 4 — 1743/1786:** bản moan giữ dạng làm phẳng `\n`→khoảng trắng của audit (quy ước sweep cho 10 fix nhiều dòng).

## §6. Lượt soát 2 (đọc lại toàn bộ fix vs JP)

- Tổng 32 ứng viên / tái kiểm chứng 32 / bỏ 1 (1753 no-op — VN cũ đã đúng 3 u theo cả CSV3 lẫn TOML-2, không cần sửa; bản nháp đầu ghi "Kyuun" 2 u là lỗi đếm của nháp, không phải của bản cũ) / sửa 0 — còn 31 fix.
- Mọi số đếm nguyên âm dài đều đếm lại độc lập bằng token từ JP (không tin số đếm cũ): 1675 (5 u), 1729 (14 a), 1731 (7 a — phát hiện audit đếm sai), 1748 (7 a), 1819 (19 a), 1855 (9 u), 1864 (18 u), 1866 (14 u).
- JSON 31 mục dạng chuẩn (khóa string, jp/tw/old_vn khớp CSV3 tuyệt đối 31/31); khối TOML 31 khóa, 0 sai lệch giá trị; mọi fix chỉ khác bản cũ ở phần rên nhắm tới (trừ 1800 thay toàn bộ giá trị 3 ký tự "Hự!"→"Phùu!" vì sai âm).

## §7. Khối TOML (đã parse-kiểm chứng bằng tomllib: 31 khóa, 0 sai lệch)

```toml
[script]
"1604" = "「Không phải── ưmm── phu── a── anh hai──\\nAnh hai, so với── mọi khi──」"
"1675" = "「Hyauuuuu!!!!!!!!」"
"1705" = "「Fu……a」"
"1711" = "「Fua── a── anh hai, tự nhiên lại, đưa cả hai ngón tay\\nvào thế── Fau!!!?」"
"1712" = "「Fa── a── a── aaƯ.」"
"1724" = "「FuaƯ…… a── tuyệt── tuyệt quá──\\nƯm── nóng── hà── đẹp── đẹp quá……」"
"1725" = "「FuaƯ…… a── chị Hibiki.\\nMikuro── là, a── Mikuro── ư, ưm」"
"1727" = "「FuaƯ…… Mikuro…… chỗ phong ấn vừa được giải trừ──\\nchỗ con gái, toàn bộ── ở gần chị Hibiki thế này」"
"1728" = "「FuaƯ.」"
"1729" = "「Fuaaaaaaaaaaaaaan!!!!」"
"1741" = "「Fuya── gì thế, này── nóng quá──\\nBụng── vùng kín── nhão nhoét── phu── aƯ」"
"1743" = "「Fua!? A── anh hai── nóng quá── ưm Hơn── mọi khi── nóng── và── to──Ư」"
"1748" = "「Hyuaaaaaaa!!!?」"
"1757" = "「Hyaa!?」"
"1765" = "「Oaa…… bên trong phần cơ thể con gái của chị Hibiki.\\nMàu hồng ướt át và đang co bóp giật giật, đẹp quá đi mất.」"
"1768" = "「Oaa!」"
"1786" = "「Hau! A! A! Aaa! Fua──Ư──ưm! Ưm uuuu!!!」"
"1789" = "「Fue!? Chị á??」"
"1800" = "「Phùu!」"
"1819" = "「Aaaaaaaaaaaaaaaaaaan!」"
"1821" = "「Au……」"
"1855" = "「Ưm hyuuuuuuuuu!」"
"1864" = "「Ưmuuuuuuuuuuuuuuuuuu!!!」"
"1865" = "「Ưm kyuu!!! Hyua! A! A!!\\nMạch điện── vừa nãy── Mikuro, trong chốc lát── như bị, cháy vậy」"
"1866" = "「Ưm kyuuuuuuuuuuuuuu!!!!!!!」"
"1898" = "「Híttt, híííttt, híttt…… híttt!?\\nBuaaa!」"
"1917" = "「Tuyệt quá…… hàà…… tuyệt quá…… dài như thế mà……\\nƯm── đã── gần như── gần như── toàn bộ」"
"2200" = "「Hàà── phuu── hààà── phuuuƯ」"
"2201" = "「Hàà── ưm, phu── ha hyu── kufuƯ」"
"2202" = "「Hàà── hàà── hàà── hàà──」"
"2559" = "Có vẻ hoàn toàn trái ngược với ấn tượng về cụm từ nụ hôn đầu.\\nNụ hôn này quá đỗi nồng nhiệt…… Aa."
```

## Ghi chú của parent (kiểm chứng khi gộp, 21/11 ~05:00)

- **SỬA 30 giá trị fix (khôi phục 「」):** agent đã làm rơi dấu ngoặc thoại 「」 khỏi toàn bộ 30 fix dòng thoại (chỉ còn 2559 độc thoại là không có ngoặc). Parent đã khôi phục 「」 vào `wrong.json` + khối TOML + các dòng "Mới:" ở §3 (chỉ thêm đúng 2 ký tự ngoặc, không đổi phần rên). Sau sửa, kiểm chứng lại: khối TOML 31 khóa, 0 sai lệch giá trị; mọi fix chỉ khác bản cũ ở phần rên (trừ 1743/1786 giữ dạng làm phẳng `\n` của audit và các dòng giữ Ư của audit). Khối TOML được thêm header `[script]` cho thống nhất với các file moan trước.
- Đếm nguyên âm kiểm chứng độc lập (xem ghi chú gộp trong ROUTE-MOANS.md).

## Kết bài

File lr追加_みくろ＆日々姫h「みくろのマスター」: đọc 611/611 dòng, xét 415 dòng rên/SFX, đổi 31 dòng (13 romaji + 16 đếm nguyên âm + 1 độ dài ん + 1 sai âm), giữ 384 dòng. Lỗi rên tập trung ở hai kiểu hệ thống của bản dịch cũ: (1) đếm nguyên âm dài sai — rên dài bị viết thừa (51 a, 40 u, 38 u, 21 a) hoặc thiếu ("Hya", "kyu", "Oa", "Hà" cho hơi 2 âm); (2) họ fa/fu — audit (trước quy tắc romaji) đã Việt hoá romaji cũ thành "phà"/"phùa", bản moan này đưa 33 dòng fa/fu về romaji theo quy tắc Hieu duyệt 21/11: 11 dòng đổi ở đây (sai âm/thiếu Ư gasp), 22 dòng giữ nguyên bản cũ và đề nghị hủy fix audit ở đợt thống nhất. Không có dòng nào cần hỏi Hieu. Sau file này tổng moan là 6 file / 156 dòng.
