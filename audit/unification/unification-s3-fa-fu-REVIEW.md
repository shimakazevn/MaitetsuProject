# Unification U11a — §3 M1 / M16 / M17 (fa/fu)

## §1. Phạm vi (scope)

- **M1** (DECIDED 19/11 Hieu, reaffirmed 20/11 ~15:00): dạng khoá fa/fu — ふぁ/ふあ → "phà"/"phùa", ふぇ → "phuê", ふやぁ → "phuya", never "phá"/romanisation — WITH the 21/11 romaji fallback exception (H-scene moans → romaji per F1 M11). Batch này: các dòng còn dùng dạng khoá VN trong H-scene moan → romaji; non-H KEEP dạng khoá (kể cả 4 dòng non-H dùng bare "Phù" cho token đơn — sửa VỀ dạng khoá). **37 dòng.**
- **M16** (OPEN → QUYẾT trong đợt này, theo uỷ quyền): Fa/Fua strict-vs-loose — vowel count theo công thức mora: ふぁ → "Fa", ふあ → "Fua", ふぁん → "Fan", ふぇ/ふえ → "Fue" (quy ước dự án, KHÔNG phải Hepburn "Fe"); độ dài = số mora (mỗi あ/ぁ = 1 a; ん = n; っ bỏ). Loose "Fua" cho ふぁ là sai → "Fa"; "Fa" cho ふあ là sai → "Fua". **67 dòng.**
- **M17** (OPEN → QUYẾT trong đợt này, theo uỷ quyền): split-fa "Fu, a" vs "phù——a". Quyết định: H-scene moan rows → romaji split "Fu" + dấu phân cách giữ nguyên theo JP (、→", ", ――→"——", ……→"……"/"...") + "a" (giữ nguyên case của token a, vd. "Fu——A" ở 凪h1 1106); non-H rows KEEP split VN. Loại B (JP nối ふあ/ふぁ nhưng VN tách) → nối lại thành romaji ở H-file, thành dạng khoá VN ở non-H file. **62 dòng.**
- **Tổng: 166 dòng sửa, 47 file.**
- Không đụng: dòng gasp-Ư, dòng "Kh", dòng ふっ (M9, batch U12a), dòng ふや đã thuộc U12a/M11 (chỉ sửa ふや khi nằm trong scope M1 VÀ không thuộc U12a — thực tế 0 dòng như vậy trong batch này).

## §2. Phương pháp (method)

- Nguồn: CSV3 good-set (87,833 dòng sau khi bỏ 3,898 dòng stale dual-set, xem `dual-csv-sets.md`) + map giá trị hiện tại theo thứ tự ưu tiên **unification-đã-gộp > moan > audit > CSV3** (precedence correction 22/11 ~11:35, U2c, coordinator CONFIRMED — chỉ load 8 file unification JSON đã gộp; file của các batch đang chạy KHÔNG được đưa vào map).
- Liệt kê ứng viên bằng script (chỉ enumeration/counting/verification — KHÔNG bulk fix): strict list M1 (76 dòng), M16 alignment (mismatch2 64 dòng + countdiff 227 dòng), M17 split2 (178 dòng) + bare-phù scan (17 dòng) + vtoks-empty scan (197 dòng). Mỗi dòng fix đều đọc JP (+TW) của chính dòng đó; JP thắng TW; không bịa phần hoàn thiện cho JP bị cắt ngang.
- old_vn = giá trị hiện tại theo map trên. Nguồn old_vn trong batch này: CSV3, moan, audit (0 dòng unification-đã-gộp — kiểm chứng 0 trùng với 8 batch đã gộp, 656 (file,key)).
- Kiểm chứng chéo: (a) mọi old_vn khớp map; (b) mọi replacement đúng số lần xuất hiện; (c) 3 lỗi basename phát hiện lúc kiểm chứng đã sửa (凪h1 1128, 凪h2 1239, 日々姫h2 1045 — file đúng có tiền tố lr_ / file khác); (d) lr_れいなh1 1204: cả hai token đều là "Fua" (không phải token thứ 2 đã là "Fa" như phân tích ban đầu) — token đầu ふあっ → "Fua" ĐÚNG, chỉ sửa token cuối ふぁっ → "Fa".
- Chú ý tokenizer: giá trị VN chứa literal backslash-n (2 ký tự) — phải thay bằng khoảng trắng trước khi tách từ, nếu không `\nFua` dính thành `nFua` và bị bỏ sót.

## §3. M1 — dạng khoá fa/fu trong H-scene moan → romaji (37 dòng)

Quy tắc áp dụng: H-scene moan → romaji (Fa/Fua/Fan/Fuaa…); non-H KEEP dạng khoá. 4 dòng non-H dùng bare "Phù" cho token đơn (ポーレット03 1590, 日々姫07 1727, 日々姫09 1579, 凪ふかみ03 2203) sửa VỀ dạng khoá (Phùa/Phà/Phàa — "Phàa" theo tiền lệ 日々姫03 2389 "Phàaa" cho ふぁぁ). ポーレットh5 891: token dài ふぁぁ… (17 a, tách tại っ thành 9+8) render hybrid "Phu"+a — sửa đầu "Phu"→"Fa", giữ nguyên số a hai đoạn.

| File | Key | JP | TW | old_vn | fix | Lý do |
| --- | --- | --- | --- | --- | --- | --- |
| lr_ポーレットh2_デコレーション＆ミルク.txt.toml | 1074 | 「ぁ――ふぁ――双鉄くん――そうてつくぅん」 | 「啊——呼啊——雙鐵君——雙鐵君」 | 「A——phà——anh Soutetsu——anh Soutetsu」 | 「A——Fa——anh Soutetsu——anh Soutetsu」 | JP ふぁ; H-scene moan, locked form -> romaji |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1464 | 「ふぁ―あ……セックス―。\nセックス―わたし……したい…………んっ」 | 「呼啊——啊……做愛——做愛——我……想做…………嗯」 | 「Phà——a……Làm tình—— Làm tình——em……muốn làm…………ưm.」 | 「Fa——a……Làm tình—— Làm tình——em……muốn làm…………ưm.」 | JP ふぁ―あ; H-scene moan |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1467 | 「ふぁ……あ―ぁ……ん―（ごくっ）―いっぱい、\nせい、えき―双鉄、くんの……溢れ、そう……」 | 「呼啊……啊——啊……嗯——（咕嘟）——滿、滿的精液——雙鐵、君的……快溢出、來了……」 | 「Phà……a——a……ưm——（Ực）——đầy ắp, tinh, dịch——của anh Soutetsu……sắp tràn, ra rồi……」 | 「Fa……a——a……ưm——（Ực）——đầy ắp, tinh, dịch——của anh Soutetsu……sắp tràn, ra rồi……」 | JP ふぁ……あ―ぁ; H-scene moan |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1497 | 「わ―わ―こんなに優しく……おててでおちんちん、\nいいこいいこってしてあげてるみたいな感じに……ふぁ」 | 「哇——哇——居然這麼溫柔……感覺就像小手手在跟小雞雞說，乖孩子乖孩子一樣……呼啊」 | 「Oa——oa——dịu dàng quá……như thể đang dùng tay vuốt ve khen ngợi dương vật là bé ngoan vậy……phà.」 | 「Oa——oa——dịu dàng quá……như thể đang dùng tay vuốt ve khen ngợi dương vật là bé ngoan vậy……Fa.」 | trailing JP ふぁ; H-scene moan |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1513 | 「はぁ―んっ―ふぁ―あ―。そう、てつ―\n双鉄―ふふっ―よく頑張ったね。双鉄、おいで？」 | 「哈——嗯——呼啊——啊——雙、鐵——雙鐵——呼呼——你真的很努力。雙鐵，過來吧？」 | 「Ha——ưm——phà——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」 | 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」 | JP ふぁ―あ; H-scene moan |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1584 | 「ちゅううっ―ん……ちゅぱっ。ふぁ……\nえと、稀咲…………。あの、ね？　―ありがとう」 | 「啾——嗯……啾。呼啊……呃，稀咲……。那個……　——謝謝」 | 「Chuu u——ưm……chu pa. Phà……Ưm, Kisaki………… Nè? ——Cảm ơn em.」 | 「Chuu u——ưm……chu pa. Fa……Ưm, Kisaki………… Nè? ——Cảm ơn em.」 | JP ふぁ……; H-scene moan |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1641 | 「すご、いっ―やぁ―はずかしっ―わたし、だって、\n―処女なのに―はじめてなのに―こんな、ふぁ」 | 「好厲、害——呀——好害羞——我、還是——處女——還是第一次——卻這樣、嗚啊」 | 「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng, ——vẫn còn trinh——là lần đầu tiên——vậy mà, phà.」 | 「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng, ——vẫn còn trinh——là lần đầu tiên——vậy mà, Fa.」 | trailing JP ふぁ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1678 | 「ひゃうっ──んっ──ふあっ──あっ──\nあっ──あっ──あっ──ああっ──」 | 「呀啊——嗯——呼啊——啊——　啊——啊——啊——啊啊——」 | 「Hyau── ưm── phùa── a──\nA── a── a── aa──」 | 「Hyau── ưm── Fua── a──\nA── a── a── aa──」 | JP ふあっ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1714 | 「ふあっ──あっ──あっ──なに、これ──\nなに、これぇっっ！！　きもちい、みくろ、気持ちいい」 | 「呼啊——啊——啊——這是什麼感覺，感覺好怪啊！！美玖路變得好舒服啊」 | 「Phùa── a── a── gì thế, này──\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」 | 「Fua── a── a── gì thế, này──\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」 | JP ふあっ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1716 | 「ふあっ──あっ──すごっ──ふえっ！！？\nや、みくろ──ごめんっ、制服──私、汚してっっ」 | 「呼啊——啊——天啊——哎？！！呀，美玖路，對不起，你的制服被我弄髒了」 | 「Phùa── a── tuyệt quá── phuê!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」 | 「Fua── a── tuyệt quá── phuê!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」 | JP ふあっ──あっ; H-scene moan. FLAG: same row has ふえっ->phuê (U12a M10) - leave that token |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1718 | 「ふあっ──あっ──すごっ──こんなにっ──あ──\nこんなに──はやくっ──つよくっ──ふか、くにっ」 | 「呼啊——啊——好厲害——這麼——啊——這麼快——這麼用力——這麼深」 | 「Phùa── a── tuyệt quá── thế này── a──\nNhanh── mạnh── sâu, thế này」 | 「Fua── a── tuyệt quá── thế này── a──\nNhanh── mạnh── sâu, thế này」 | JP ふあっ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1720 | 「ふあっ──あっ──日々姫さんの、指……指が──\nみくろ──みくろの、クリトリス、をっ──」 | 「呼啊——啊——日日姬小姐的手指……手指在撫摸美玖路、美玖路的陰核——」 | 「Phùa── a── ngón tay của chị Hibiki…… ngón tay──\nMikuro── âm vật của Mikuro, đang──」 | 「Fua── a── ngón tay của chị Hibiki…… ngón tay──\nMikuro── âm vật của Mikuro, đang──」 | JP ふあっ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1722 | 「ふあっ──あっ──くぱって──みくろ──\n日々姫さんに──ひらかれて、ますっ」 | 「呼啊——啊——美玖路的下面張開了，被日日姬小姐撐開了」 | 「Phùa── a── mở rộng ra── Mikuro──\nđang được chị Hibiki── vạch ra, ạ」 | 「Fua── a── mở rộng ra── Mikuro──\nđang được chị Hibiki── vạch ra, ạ」 | JP ふあっ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1733 | 「ふああっ！？　あっ──み、みくろ、いま──\nみくろの、おまた──すごく、きもちよくて」 | 「呼啊啊？！啊——美、美玖路剛剛——美玖路的胯部——非常舒服」 | 「Phùaa!? A──Mi, Mikuro, vừa nãy──\nChỗ đó của Mikuro── sướng lắm ạ.」 | 「Fuaa!? A──Mi, Mikuro, vừa nãy──\nChỗ đó của Mikuro── sướng lắm ạ.」 | JP ふああっ (2 a's); H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1735 | 「ふあっ！　あっ！　いっしょ──いっしょにぃっ！」 | 「呼啊！啊！一起，我們一起！」 | 「Phùa! A! Cùng nhau── cùng nhauuu!」 | 「Fua! A! Cùng nhau── cùng nhauuu!」 | JP ふあっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1736 | 「ふあっ　あっ！　あっ！　ああああっ！！！！！！」 | 「呼啊！啊！啊！啊啊啊啊！！！！！！」 | 「Phùa a! A! Aaaa!!!!!!」 | 「Fua a! A! Aaaa!!!!!!」 | JP ふあっ あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1737 | 「ふあっ！　あっ！　にぃにっ！　にぃにっ！！！！\nきょうっ！　すごっ──わたしっ──かんじてっ！」 | 「呼啊！啊！阿哥！阿哥！！！！今天！你特別勇猛，我好舒服啊！」 | 「Phùa! A! Anh hai! Anh hai!!!!\nHôm nay! Tuyệt quá── em── cảm nhận được!」 | 「Fua! A! Anh hai! Anh hai!!!!\nHôm nay! Tuyệt quá── em── cảm nhận được!」 | JP ふあっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1739 | 「ふあっ！　あっ！！　あっ──ああああっ！！！！」 | 「呼啊！啊！！啊——啊啊啊啊！！！！」 | 「Phùa! A!! A── aaaa!!!!」 | 「Fua! A!! A── aaaa!!!!」 | JP ふあっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1773 | 「はっっ──あっ──ふっ──ふあっ──」 | 「哈——啊——呼——呼啊——」 | 「Hà── a── phu── phùa──」 | 「Hà── a── phu── Fua──」 | JP ふあっ──; H-scene moan. KEEP 'phu' for ふっ (M9) |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1820 | 「ふぁんっ！！」 | 「啊啊嗯！！」 | 「Phàn!!」 | 「Fan!!」 | JP ふぁんっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1857 | 「んきゅ！　ふあっ！　あ──ずりゅって──ずる、って──やぁぁあっ──にぃに──ぜんぶ、いっちゃうぅ」 | 「嗯唔！呼啊！啊——滋溜——滋嚕的好大聲——呀啊啊啊——阿哥——全都進來了」 | 「Ưm kyu! Phùa! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」 | 「Ưm kyu! Fua! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」 | JP ふあっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1928 | 「はいっ！　ですっ──んっ──ひび、き──さんっ──\nふあっ──みくろも、セックス──セックス、セックス」 | 「好！好的——嗯——日日姬——小姐——呼啊——美玖路也想要做愛——很想，非常想」 | 「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\nPhùa── Mikuro cũng, làm tình── làm tình, làm tình」 | 「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\nFua── Mikuro cũng, làm tình── làm tình, làm tình」 | JP ふあっ──; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 1967 | 「見たいっ──ですっ──んひゅっ──ふあ──あっ、\nみたい、けど──みくろっ──なんだか、みくろぉっ」 | 「想看——好想看——嗯唔——呼啊——啊真的很想看——但美玖路——感覺怪怪的」 | 「Muốn nhìn── ạ── ưm hưu── phùa── a,\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」 | 「Muốn nhìn── ạ── ưm hưu── Fua── a,\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」 | JP ふあ──あっ; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 2107 | 「みくっ、ろっ──みて──あっ──ふあっ──\nこいっ、ばっ──セックスっ──私、と、にぃに、の」 | 「美玖路——看著吧——啊——呼啊——這就是——做愛——我和阿哥的做愛」 | 「Miku, ro── nhìn đi── a── phùa──\nCái này── làm tình── của chị, và, anh hai」 | 「Miku, ro── nhìn đi── a── Fua──\nCái này── làm tình── của chị, và, anh hai」 | JP ふあっ──; H-scene moan |
| lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml | 2198 | 「いい！　ですっ──すご──くっ──ふあっ！\nみく、ろっ──これっ──しゅきいっ」 | 「舒服！非常舒爽——呼啊！美玖路好喜歡這樣」 | 「Sướng! Lắm ạ── rất── hự── phùa!\nMiku, ro── cái này── thích lắmmm」 | 「Sướng! Lắm ạ── rất── hự── Fua!\nMiku, ro── cái này── thích lắmmm」 | JP ふあっ; H-scene moan |
| れいなh1_おかあさんのレッスン.txt.toml | 1284 | 「ふぁ……あっ……すごい……すごい……ですぅ」 | 「哇……好、好厲害」 | 「Phà……a……tuyệt quá……tuyệt quá……ạ~」 | 「Fa……a……tuyệt quá……tuyệt quá……ạ~」 | JP ふぁ……あっ; H-scene moan |
| れいなh1_おかあさんのレッスン.txt.toml | 1350 | 「あ……ふぁ――あっ」 | 「啊，哇……」 | 「A……phà――a.」 | 「A……Fa――a.」 | JP ふぁ――あっ; H-scene moan |
| れいなh1_おかあさんのレッスン.txt.toml | 1529 | 「ふぁ……あ――のんで……る……ンッ――ふっ」 | 「蛤啊……啊……喝下去了……」 | 「Phà……a――đang……nuốt……ưm――phù.」 | 「Fa……a――đang……nuốt……ưm――phù.」 | JP ふぁ……あ; H-scene moan. KEEP trailing phù (M9, ふっ) |
| れいなh1_おかあさんのレッスン.txt.toml | 1532 | 「ふぁ……あっ――あっ！？」 | 「蛤啊……啊、啊！？」 | 「Phà……a——a!?」 | 「Fa……a——a!?」 | JP ふぁ……あっ; H-scene moan |
| れいなh1_おかあさんのレッスン.txt.toml | 1533 | 「ふあ――あっ！　あっ！　ああっ」 | 「蛤啊……啊！啊！啊啊！」 | 「Phùa——a! A! Aa」 | 「Fua——a! A! Aa」 | JP ふあ――あっ; H-scene moan. MOAN-sourced 'Phùa' - moan pass kept VN here, fix per M1+F1 M11 |
| れいなh1_おかあさんのレッスン.txt.toml | 1535 | 「は……ぃ……っ……たっ……んくっ――ふぁっ……\nれい、な……セック、ス……そうてつ、さん――と」 | 「蛤啊……好痛……啊……啊嗯……玲奈……和雙鐵先生……做愛了……」 | 「Ha……đau……quá……ưm——phà……\nReina……đang làm tình……với anh Soutetsu……rồi」 | 「Ha……đau……quá……ưm——Fa……\nReina……đang làm tình……với anh Soutetsu……rồi」 | JP ふぁっ……; H-scene moan |
| ポーレット03_大きなにもつのおばあさん.txt.toml | 1590 | 「ふあ～っ」 | 「呼～」 | 「Phù~Ư」 | 「Phùa~Ư」 | JP ふあ～っ single token rendered bare 'Phù'; NON-H -> locked form Phùa. KEEP trailing Ư as-is |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 891 | 「ふぁぁぁぁぁぁぁぁぁっぁぁぁぁぁぁぁぁっ！！！」 | 「呼啊啊啊啊啊啊！！！」 | 「Phuaaaaaaaaa—Aaaaaaaa!!!」 | 「Faaaaaaaaa—Aaaaaaaa!!!」 | JP ふぁぁぁぁぁぁぁぁぁっ (9 a's) rendered hybrid 'Phu'+a's; H-scene moan -> romaji Fa + 8 a's. KEEP 2nd segment 'Aaaaaaaa' (8 a's, correct) |
| 凪ふかみ03_みかんの旅.txt.toml | 2203 | 「ふぁあ」 | 「呼」 | 「Phù」 | 「Phàa」 | JP ふぁあ (2 a's) rendered bare 'Phù'; NON-H -> locked form Phàa (cf. 日々姫03 2389 'Phàaa' for ふぁぁ) |
| 日々姫07_たったひとりの宣戦布告.txt.toml | 1727 | 「ふあっ！？」 | 「哇啊！？」 | 「Phù!?」 | 「Phùa!?」 | JP ふあっ！？ single token rendered bare 'Phù'; NON-H -> locked form Phùa |
| 日々姫09_静かなる開戦.txt.toml | 1579 | 「ふぁ～、生き返る～～っ」 | 「啊～活過來了～～」 | 「Phù~, sống lại rồi~~Ư」 | 「Phà~, sống lại rồi~~Ư」 | JP ふぁ～ single token rendered bare 'Phù'; NON-H -> locked form Phà |
| 日々姫h1_マッサージの続き.txt.toml | 1059 | 「んっ――ふあっ――やっ――しゅごっ――んっ――\nにいにっ――おちん、ちんっ――なかで――ぷく、って」 | 「嗯――呼――呀――好厲害――嗯――阿哥的――雞雞――在裡面――漲了起來」 | 「Ưm——Phù——Ya——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」 | 「Ưm——Fua——Ya——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」 | JP ふあっ rendered bare 'Phù' (vowel lost); H-scene moan -> Fua |

## §4. M16 — Fa/Fua strict (67 dòng)

Quy tắc áp dụng: strict theo mora count (xem §1). Các token dài đã kiểm chứng từng mora: 1357 (18 a), 1477 (19 a), 1479 (14 a), 1100 (17 a + n), 962 (8 a + n), 2114 (6 a), 1470/819 (5 a + n), 2458 (5 a) — VN thừa đúng 1 ký tự (u thừa sau F, hoặc a thừa) thì bỏ đúng ký tự đó. Token dán 1358 (ふぁふゅぅ×13っんんっ): a:1, u:14, n:2 cả hai phía — chỉ bỏ "u" thừa trong "Fua", giữ nguyên cách dán của moan pass (không thêm F cho ふゅ).

| File | Key | JP | TW | old_vn | fix | Lý do |
| --- | --- | --- | --- | --- | --- | --- |
| lr_れいなh1_レディ・れいな.txt.toml | 1204 | 「ふあっ――あっっ――あっ――あっ――\nれいな――ンッ――なかに、いっぱいっ――ふぁっ」 | 「呼啊——啊——啊——啊————玲奈——嗯——裡面，滿滿的——呼啊」 | 「Fua——a——a——a——\nReina——ưm——bên trong, lấp đầy rồi——Fua」 | 「Fua——a——a——a——\nReina——ưm——bên trong, lấp đầy rồi——Fa」 | JP ふあっ (1st, -> Fua correct) + ふぁっ (trailing, -> Fa); only the TRAILING Fua is loose - fix that one |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1153 | 「ふっ――ぁ――。\nん……ふぁ……ぅ――ん…………あ！」 | 「呼——啊——嗯……哈……嗯…………啊！」 | 「Fu——a——.\nƯm…… fua…… u——ưm………… a!」 | 「Fu——a——.\nƯm…… fa…… u——ưm………… a!」 | JP ふぁ; loose fua -> fa. KEEP 'Fu——a' for ふっ――ぁ (M9) |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1158 | 「ふやっ！！？　ゆ、指っ――\n双鉄さまのお指が――んっ――ふぁっ」 | 「呼呀！！？手，手指——雙鐵少爺的手指——嗯——呼啊」 | 「Fuya!!? Ng-ngón tay——\nNgón tay của ngài Soutetsu——ưm——fua.」 | 「Fuya!!? Ng-ngón tay——\nNgón tay của ngài Soutetsu——ưm——fa.」 | JP ふぁ; loose fua -> fa |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1159 | 「ふぁっ、あっ、あっ、あっ」 | 「呼啊、啊、啊、啊」 | 「Fua, a, a, a.」 | 「Fa, a, a, a.」 | JP ふぁ; loose Fua -> Fa |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1171 | 「ふぁ――ぁっ――あっ――あっ――」 | 「哈——啊——啊——啊——」 | 「Fua——a——a——a——」 | 「Fa——a——a——a——」 | JP ふぁ; loose Fua -> Fa |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1173 | 「ふぁっ――あっ――あっ――んうっ！！！？」 | 「哈——啊——啊——嗯嗚！！！？」 | 「Fua——a——a——Ưm ư!!!?」 | 「Fa——a——a——Ưm ư!!!?」 | JP ふぁ; loose Fua -> Fa |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1178 | 「ふぁっ――あっ――ンッ――きゅふっ――ぁ――ふ――\nそうてつ、さまっ――そうてつ、さまぁっ」 | 「哈——啊——嗯——呼——呼——雙鐵，少爺——雙鐵，少爺——」 | 「Fua——a——n——kyufu——a——fu——\nSou, tetsu, sama——Sou, tetsu, sama~」 | 「Fa——a——n——kyufu——a——fu——\nSou, tetsu, sama——Sou, tetsu, sama~」 | JP ふぁっ; loose Fua -> Fa. KEEP 'kyufu'/'fu' for ふっ/ふ |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1198 | 「ふぁっ！　んぅっ――」 | 「哈！嗯——」 | 「Fua! Ưm ư——」 | 「Fa! Ưm ư——」 | JP ふぁ; loose Fua -> Fa |
| lr_ポーレットh1_家族旅行の最終日の夜.txt.toml | 1023 | 「ふあっ――あっ！　あっ！　あっ！\nはっ！　あっ――んうっ――くふっ――あっ！」 | 「呼啊——啊！啊！啊！哈！啊——嗯唔——咕呼——啊！」 | 「Fa――a! A! A! Hà! A――ưm――Khự――a!」 | 「Fua――a! A! A! Hà! A――ưm――Khự――a!」 | JP ふあっ; strict is Fua, VN has Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1353 | 「ふぁっ――あっ――あっ――あ――！」 | 「呼啊——啊——啊——啊——！」 | 「Fua――a――a――a――!」 | 「Fa――a――a――a――!」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1354 | 「ふぁっ――あっ――あっ――あっ――」 | 「呼啊——啊——啊——啊」 | 「Fua――a――a――a――」 | 「Fa――a――a――a――」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1355 | 「ふぁっ――あっ――っ――あっ――あっ！！」 | 「呼啊——啊——啊——啊！！」 | 「Fua――a――Ư――a――a!!」 | 「Fa――a――Ư――a――a!!」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1356 | 「ふぁっ――あっ――んきゅっ！　うっ！　にぃに！\nまっ！　って――わらっ――わた、しっ――もうっ！」 | 「呼啊——啊——嗚！嗚！阿哥！等等——我——我——要！」 | 「Fua――a――nkyu! Ư! Anh hai!\nĐợi! Đã――em――em, em――sắp!」 | 「Fa――a――nkyu! Ư! Anh hai!\nĐợi! Đã――em――em, em――sắp!」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1357 | 「ふぁぁぁぁぁぁぁぁぁぁぁぁぁっぁあっぁぁぁんっ！」 | 「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！」 | 「Fuaaaaaaaaaaaaaaaaaan!」 | 「Faaaaaaaaaaaaaaaaaan!」 | JP ふぁぁぁぁぁぁぁぁぁぁぁぁぁっぁあっぁぁぁんっ (18 a's); VN has extra 'u' after F - drop it |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1358 | 「ふぁふゅぅぅぅぅぅぅぅぅぅぅぅぅぅっんんっ！！」 | 「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」 | 「Fuafyuuuuuuuuuuuuuunn!!」 | 「Fafyuuuuuuuuuuuuuunn!!」 | glued token JP ふぁふゅぅx13っんんっ (a:1, u:14, n:2); VN has one extra 'u' (the 'u' in 'Fua') - drop it. KEEP the glue as moan pass wrote it (no F on ふゅ) |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1367 | 「ふぁっ？！　あっ――あっ――あっ」 | 「呼啊？！　啊——啊——啊」 | 「Fua?! A――a――a」 | 「Fa?! A――a――a」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | 1479 | 「ん……ぁ――あっ――ふっ――あっ――ん――\nちゅっ――ちゅむっ――ん……フッ――ふぁっ――あ」 | 「嗯……啊——啊——呼——啊——嗯——啾——啾唔——嗯……呼——呼啊——啊」 | 「Ưm…… a――a――hư――a――ưm――\nChụt――chùn chụt――ưm…… hư――fua――a」 | 「Ưm…… a――a――hư――a――ưm――\nChụt――chùn chụt――ưm…… hư――fa――a」 | JP ふぁ; loose fua -> fa. FLAG: row also in U12a M9 list - this fix touches only the ふぁ token |
| lr_日々姫真闇h1_三人家族.txt.toml | 1476 | 「ふぁっ――ぁ……双ちゃん――そうちゃんの……\n（ごくっ）――こぎゃん、あつ、くて――がちがち、で」 | 「呼啊——啊……小雙——小雙的……（吞口水）——居然這麼，滾燙」 | 「Fua――a…… Sou-chan――của Sou-chan……\n（Ực）――nóng, thế này――cứng ngắc, thế này.」 | 「Fa――a…… Sou-chan――của Sou-chan……\n（Ực）――nóng, thế này――cứng ngắc, thế này.」 | JP ふぁ; loose Fua -> Fa |
| lr_日々姫真闇h1_三人家族.txt.toml | 1477 | 「ふぁぁぁぁぁぁぁぁぁぁぁっぁぁぁあああああっ！！」 | 「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」 | 「Fuaaaaaaaaaaaaaaaaaaa!!!!」 | 「Faaaaaaaaaaaaaaaaaaa!!!!」 | JP ふぁぁぁぁぁぁぁぁぁぁぁっぁぁぁあああああっ (19 a's); VN has extra 'u' after F - drop it |
| lr_日々姫真闇h1_三人家族.txt.toml | 1479 | 「ふぁぁぁぁぁぁぁぁぁっぁぁぁぁあっっ！！！！？」 | 「呼啊啊啊啊啊啊啊啊啊啊！！！！？」 | 「Fuaaaaaaaaaaaaaa!!!!?」 | 「Faaaaaaaaaaaaaa!!!!?」 | JP ふぁぁぁぁぁぁぁぁぁっぁぁぁぁあっっ (14 a's); VN has extra 'u' after F - drop it |
| lr_日々姫真闇h1_三人家族.txt.toml | 1481 | 「ふぁんっ！？　ね、ねぇねっ」 | 「呼啊！？啊、阿姐」 | 「Fuan!? Chị, chị hai.」 | 「Fan!? Chị, chị hai.」 | JP ふぁんっ; loose Fuan -> Fan |
| lr_日々姫真闇h1_三人家族.txt.toml | 1634 | 「ねぇねの――おっぱい――やわらか――んっ――すごっ\n――ぁ――指――沈むのに――はりつい、て――ふぁっ」 | 「姐姐的——胸部——好柔軟——嗯——好驚人——啊——手指——陷進去——肉都纏上來了——呼啊」 | 「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\n――a――ngón tay――lún vào――rồi bám chặt, lấy――fua.」 | 「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\n――a――ngón tay――lún vào――rồi bám chặt, lấy――fa.」 | JP ふぁ; loose fua -> fa |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1428 | 「ふぁ……あっ！　んっ――ん～～～～っ！！」 | 「呼啊……啊！　嗯——嗯~～～～！！」 | 「Fua……a! Ưm——ưm~~~~!!」 | 「Fa……a! Ưm——ưm~~~~!!」 | JP ふぁ; loose Fua -> Fa |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1429 | 「ふぁっ！　あっ――あっ――あ……ああ……」 | 「呼啊！　啊——啊——啊……啊……」 | 「Fua! A——a——a……aa……」 | 「Fa! A——a——a……aa……」 | JP ふぁ; loose Fua -> Fa |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1430 | 「ふぁっ！」 | 「呼啊！」 | 「Fua!」 | 「Fa!」 | JP ふぁ; loose Fua -> Fa |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1431 | 「ふぁっ！！」 | 「呼啊！！」 | 「Fua!!」 | 「Fa!!」 | JP ふぁ; loose Fua -> Fa |
| lr_稀咲h1_おしおきとごほうび.txt.toml | 1008 | 「ふぁ……あ……あ……あ――……」 | 「啊、啊、啊、啊……」 | 「Fua……a……a……a――……」 | 「Fa……a……a……a――……」 | JP ふぁ; loose Fua -> Fa |
| lr_稀咲ポーレットh1_悪い大人の契約.txt.toml | 1470 | 「ふぁああああん！　双鉄、ね？　そうてつぅ―あっ、\nボク、ね？　ボクっ―ボク、もう、もう、もうっ！」 | 「呼啊啊啊啊啊！　雙鐵……　雙鐵——啊、我，啊……　我——我、已經、已經、已經」 | 「Faaaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」 | 「Faaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」 | JP ふぁああああん (5 a's + n); VN has 6 a's - drop one |
| lrれいな追加h_夜の花嫁修業.txt.toml | 736 | 「……んぅ……んっ――\nふぁ……あっ――んっ――んんっ」 | 「……嗯……嗯——呼啊……啊……嗯——嗯嗯」 | 「……Ưm……ưm——\nFua……a——ưm——ưm ưm」 | 「……Ưm……ưm——\nFa……a——ưm——ưm ưm」 | JP ふぁ; loose Fua -> Fa |
| lrれいな追加h_夜の花嫁修業.txt.toml | 1061 | 「ふぁ……あ……\nキス。あまくて――すっごくきもちよかったですぅ」 | 「呼……哈……接吻——好甜蜜好舒服呀」 | 「Fua……a……\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」 | 「Fa……a……\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」 | JP ふぁ; loose Fua -> Fa |
| lrれいな追加h_夜の花嫁修業.txt.toml | 1073 | 「ふぁ――おっぱい――んっ――ふ、ぬる、ぬるっ――\nれいな、ちくびっ――ちくびっ――こん、なにっ――」 | 「呼啊——胸部——嗯——呼，滑溜溜的——玲奈的乳頭——乳頭——好舒爽——」 | 「Fua——ngực——ưm——Fu, trơn, trơn——\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」 | 「Fa——ngực——ưm——Fu, trơn, trơn——\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」 | JP ふぁ; loose Fua -> Fa. KEEP 'Fu,' for standalone ふ |
| lrれいな追加h_夜の花嫁修業.txt.toml | 1074 | 「ふぁ」 | 「呼啊」 | 「Fua」 | 「Fa」 | JP ふぁ; loose Fua -> Fa |
| lrれいな追加h_夜の花嫁修業.txt.toml | 1076 | 「ふぁぁぁあ――おっぱい、\nれいな、おっぱいとろけちゃいますぅ」 | 「呼啊啊——胸部，玲奈的胸部快要融化了」 | 「Fuaaaa——ngực,\nReina, ngực tan chảy mất thôi nha~」 | 「Faaaa——ngực,\nReina, ngực tan chảy mất thôi nha~」 | JP ふぁぁぁあ (4 a's); VN has extra 'u' after F - drop it |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1100 | 「ふぁぁぁぁっぁああああああああああああんっ！！！」 | 「呼啊啊啊啊啊啊啊啊啊！！！」 | "「Fuaaaaaaaaaaaaaaaaan!!!」" | "「Faaaaaaaaaaaaaaaaan!!!」" | JP ふぁぁぁぁっぁああああああああああああんっ (17 a's); VN has extra 'u' after F - drop it |
| lr真闇追加h_赤ちゃん、欲しか.txt.toml | 1106 | 「ふぁ！！――あっ！　あっ――んっ――ふ、あっ――\nそ、ちゃんっ――ン――おね、ちゃんの、くり、とりす」 | 「呼啊！！——啊！啊――嗯――呼、啊――小雙——嗯——姐姐的、陰蒂」 | "「Fua!!——A! A——ưm——Fu, a——\nSou, chan——ưm——âm, vật, của, chị.」" | "「Fa!!——A! A——ưm——Fu, a——\nSou, chan——ưm——âm, vật, của, chị.」" | JP ふぁ; loose Fua -> Fa. KEEP 'Fu, a' split for ふ、あっ (already romaji) |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 2346 | 「ふぁっ――あっ――あっ――あっ」 | 電車公主的身體高高翹起，不死鳥博士則是蜷縮起身子。 | 「Fua——ah——ah——ah」 | 「Fa——ah——ah——ah」 | JP ふぁ; loose Fua -> Fa. KEEP 'ah' for あっ as moan pass wrote it |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 2457 | 「ふぁっ――あっ――いいっ――イイっ！　ふっ――あ、\nおねがいっ――このまま――このまま――このままあっ」 | （進進出出） | 「Fua——ah——sướng——sướng quá! Phù——ah,\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」 | 「Fa——ah——sướng——sướng quá! Phù——ah,\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」 | JP ふぁっ; loose Fua -> Fa (1st token only). FLAG: 2nd split 'Phù——ah' is ふっ-based (U12a M9) - leave |
| lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml | 2458 | 「ふあああああっっ！！！！」 | （長驅直入） | 「Fuaaaaaa!!!!」 | 「Fuaaaaa!!!!」 | JP ふあああああっっ (5 a's); VN has 6 a's - drop one |
| れいなh3_おもらし自由化大作戦.txt.toml | 1115 | 「んふふ～　ほれふぁら、えひふぁ、へひほーれふぅ」 | 「嘿嘿……啾嚕……啾嚕……」 | 「Nfufu~ ho re fua ra, e hi fua, he hi ho re fuu」 | 「Nfufu~ ho re fa ra, e hi fa, he hi ho re fuu」 | gibberish chain: JP ふぁ (x2) -> 'fa'. KEEP 'fuu' for ふぅ |
| グランドリライト05_れいな.txt.toml | 1922 | 「えっへへー。れいな、お役にたてたの……\nふぁ……うれしい……です、よぉ」 | 「嘿嘿嘿，玲奈幫上忙了……呼……好開心呀……」 | 「Ehehe~. Reina, giúp ích được cho anh……\nfua……vui lắm……ạ~」 | 「Ehehe~. Reina, giúp ích được cho anh……\nfa……vui lắm……ạ~」 | JP ふぁ; loose fua -> fa (non-H file, romaji count fix still applies) |
| グランドリライト08_ふかみ.txt.toml | 1823 | 「ふがっ！？　んにゅっ！？　んっ――ふぁっ！\nぷはあっ！！？」 | 「啊？！唔？！嗯……啊！啊？！」 | 「Fuga!? Nnyu!? Ưm――Fua!\nPuhaa!!?」 | 「Fuga!? Nnyu!? Ưm――Fa!\nPuhaa!!?」 | JP ふぁ; loose Fua -> Fa (non-H file, romaji count fix still applies) |
| ハチロクh1_契り.txt.toml | 1271 | 「ふぁっ！　っ……あっ――シーリングが開放され、て、\n使える、ように……なった、穴」 | 「嗚啊！啊……這個封印解開了，可以用了的……小穴」 | 「Fua! Ư……A――Phong ấn đã được giải trừ, và,\ncái lỗ……đã có thể, sử dụng được.」 | 「Fa! Ư……A――Phong ấn đã được giải trừ, và,\ncái lỗ……đã có thể, sử dụng được.」 | JP ふぁ; loose Fua -> Fa |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 819 | 「ん……きゅっ――ふぁああああんっ！！！」 | 「嗯……呀嗚、啊——！！！」 | 「Ưm……kiu——Faaaaaan!!!」 | 「Ưm……kiu——Faaaaan!!!」 | JP ふぁああああんっ (5 a's + n); VN has 6 a's - drop one |
| ハチロクh8_桜色のひめごと.txt.toml | 703 | 「きゃふっ！？　あっ！　おまん、まんっ――んっ！！\nわたく、し――わたくしの――おまん、まんっ――ふぁ」 | 「呀呼！？啊！小妹妹——！！我——我的——小妹妹——嗚啊」 | 「Kyafu!? A! Tiểu huyệt——ưm!!\nEm——tiểu huyệt——của em——Fua」 | 「Kyafu!? A! Tiểu huyệt——ưm!!\nEm——tiểu huyệt——của em——Fa」 | JP ふぁ (trailing); loose Fua -> Fa |
| ハチロクh8_桜色のひめごと.txt.toml | 708 | 「ひゃっ！　あっ！？　吸われ――おまめっ…ふぁっ！\nおまんまん――ぁ……じゅるじゅる――音、やっ――ん」 | 「呀！啊！？吸——小豆豆…嗚啊！小妹妹——啊……啾嚕啾嚕的——聲音，啊——」 | 「Hya! A!? Bị mút rồi——hạt đậu... Fua!\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」 | 「Hya! A!? Bị mút rồi——hạt đậu... Fa!\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」 | JP ふぁ; loose Fua -> Fa |
| ハチロクh8_桜色のひめごと.txt.toml | 724 | 「ほーへふはふぁっ――ん……ほーほ、\nわらふひひ……はふぁふぁぇ、ほ――」 | 「呼—呼呼啊——……呼—呼，我……哈呼哈呼，呼——」 | 「Ho he phu ha fua——ưm……ho ho,\nwa ra phu hi hi……ha fua fua e, ho——」 | 「Ho he phu ha fa——ưm……ho ho,\nwa ra phu hi hi……ha fa fa e, ho——」 | gibberish chain: JP ふぁっ/ふぁ/ふぁぇ; each ふぁ -> 'fa' (one word per mora). KEEP 'e' for ぇ |
| ハチロクh8_桜色のひめごと.txt.toml | 746 | 「いぅん！？　あ――吸、吸って――ひ――きゅ！　ふぁ\n――おもら、し――全部――残りも――吸いだされ、て」 | 「咿嗯！？啊——吸，吸——咿——嗯呀！嗚啊——小便——全部——一點不剩地——被吸掉了」 | 「Iun!? A——Hút, hút mất rồi——hi——kyu! Fua\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」 | 「Iun!? A——Hút, hút mất rồi——hi——kyu! Fa\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」 | JP ふぁ at line end; loose Fua -> Fa |
| ハチロクh8_桜色のひめごと.txt.toml | 751 | 「はっ――あむっ――ちゅっ――ちゅむうっ――ん……\nしゅ、きっ――ほーへふ……はふぁ、しゅき、しゅきぃ」 | 「哈——啊姆——啾——啾嗯嗚——……喜歡——喜歡您……嗚啊，喜歡、喜歡」 | 「Ha——a mu——chụt——chu muu——ưm……\nyêu, ngài——ho he phu……ha fua, yêu, yêu ngài lắm」 | 「Ha——a mu——chụt——chu muu——ưm……\nyêu, ngài——ho he phu……ha fa, yêu, yêu ngài lắm」 | gibberish chain: JP ふぁ -> 'fa' |
| ハチロクh8_桜色のひめごと.txt.toml | 754 | 「はむっ！？　ん――ひゅっ――ん……れるっ――ろっ、\nちゅ――ちゅむっ――ほーへふ……んっ――はふぁぁ」 | 「哈姆！？嗯——咻——……咻嚕——嚕，啾——啾姆——嗯—呼……——嗚啊啊」 | 「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\nchu——chụt——ho he phu……ưm——ha fuaa」 | 「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\nchu——chụt——ho he phu……ưm——ha faa」 | gibberish chain: JP ふぁぁ (2 a's) -> 'faa' |
| ハチロクh8_桜色のひめごと.txt.toml | 759 | 「あ――出てッ――んっ――熱、い――んくっ――ふ――\n双鉄、さまの――精子――あつい、のっ――ふ、ふぁ」 | 「啊——出來了——好熱——嗯——呼——雙鐵少爺的——精子——好熱——呼，嗚啊」 | 「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fua」 | 「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fa」 | JP ふ、ふぁ; loose fua -> fa. KEEP 'phù' for standalone ふ (not in M1/M16/M17 scope) |
| ハチロクh8_桜色のひめごと.txt.toml | 812 | 「ふぁ……あ…………あまざけ、い、っぱい――上の、\nおくちも……した、の……おくち、も――ふぁ」 | 「嗚啊……啊……滿滿都是甜米酒——然後又親了……親過了——嗚啊」 | 「Fua……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——fua」 | 「Fa……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——fa」 | JP ふぁ (x2); loose Fua/fua -> Fa/fa |
| ハチロクh8_桜色のひめごと.txt.toml | 813 | 「ふぁ……ぁァ――――――あっ……全部……ぜん、ぶ\n――わたくし――全部を――旦那様、の――おくち、に」 | 「嗚啊……啊啊——啊……全部……哦嗯，噗——我——全部——向夫君——口腔」 | 「Fua……aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」 | 「Fa……aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」 | JP ふぁ; loose Fua -> Fa |
| ハチロクh8_桜色のひめごと.txt.toml | 857 | 「お、まん、まん――ふぁ――おぼれ――おぼれ、りゅっ\n――んっ！　双鉄、さまの――精子、で、たぷたぷっ」 | 「小妹妹——嗚啊——泡——泡在精液裡——！雙鐵少爺的——精子，滿滿的都是」 | 「Tiểu huyệt——Fua——ngập——ngập, rồi\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」 | 「Tiểu huyệt——Fa——ngập——ngập, rồi\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」 | JP ふぁ; loose Fua -> Fa |
| ハチロクh8_桜色のひめごと.txt.toml | 946 | 「そうてつ――さまっ――ふぁっ――双鉄、さまあっ！」 | 「雙鐵少爺——嗚啊——雙鐵少爺！」 | 「Ngài Soutetsu——Fua——Ngài Soutetsu!」 | 「Ngài Soutetsu——Fa——Ngài Soutetsu!」 | JP ふぁ; loose Fua -> Fa |
| ポーレット02_解放b寝台.txt.toml | 1795 | 「ですね。わたしも、サポートします……ふぁ」 | 「嗯。我也會幫你的……呼」 | 「Vâng. Em cũng sẽ hỗ trợ…… fua.」 | 「Vâng. Em cũng sẽ hỗ trợ…… fa.」 | JP ふぁ; loose fua -> fa (non-H file, romaji count fix still applies) |
| ポーレットh2_制服変更？.txt.toml | 962 | 「ふぁぁぁぁっぁぁぁぁんっ！」 | 「呼啊啊啊！」 | 「Fuaaaaaaaan!」 | 「Faaaaaaaan!」 | JP ふぁぁぁぁっぁぁぁぁんっ (8 a's); VN has extra 'u' after F - drop it |
| ポーレットh3_誘惑アイスコーヒー.txt.toml | 915 | 「ふぁっ――あっ――ハァッ――あっ――」 | 「呼啊——啊——呼——啊——」 | 「Fua——a——hàà——a——」 | 「Fa——a——hàà——a——」 | JP ふぁ; loose Fua -> Fa |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 864 | 「ひゃっ！？　抜けっ――んっ！　あつ、っ！　ふあ！」 | 「呀！？拔出去了——嗯！好燙！啊！」 | 「Hya!? Tuột ra——ưm! Nóng, quá! Fa!」 | 「Hya!? Tuột ra——ưm! Nóng, quá! Fua!」 | JP ふあ; strict is Fua, VN has Fa |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 895 | 「ふあっ！　あっ！　あっ！　あっ！　双鉄、くんっ！\nあっ――子宮！　もっと！　叩いて、もっぉ！」 | 「呼啊！啊！啊！啊！雙鐵君！啊——子宮！再多來！頂一頂！」 | 「Fa! A! A! A! Anh Soutetsu! A——tử cung! Nữa đi! Đâm vào, nữa đi!」 | 「Fua! A! A! A! Anh Soutetsu! A——tử cung! Nữa đi! Đâm vào, nữa đi!」 | JP ふあ; strict is Fua, VN has Fa |
| ポーレットh8_気動車の国のアリス.txt.toml | 2049 | 「やだっ！？　また、先、ひとり――でっ――ん、ふぁ、\nきもち、いいけどっ――いいけど――やぁ、なのっ！！」 | 「不要！我又要——一個人——嗯——雖然是、很舒服——但是我不要！！」 | 「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, Fua,\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」 | 「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, Fa,\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」 | JP ふぁ; loose Fua -> Fa |
| ポーレットh8_気動車の国のアリス.txt.toml | 2167 | 「ふぁ……は――双鉄くん……（すんっ、すんっ）\nあ……双鉄、くん、で――わたし――いっぱい――」 | 「呼啊……啊——雙鐵君……（吸鼻子）啊……雙鐵君——弄得我全身都是」 | 「Fua……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\nA……bằng Anh Soutetsu——em——tràn ngập——」 | 「Fa……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\nA……bằng Anh Soutetsu——em——tràn ngập——」 | JP ふぁ; loose Fua -> Fa |
| ポーレットh8_気動車の国のアリス.txt.toml | 2212 | 「あ――は――んっ――ふううっ、ふぁ――は、あ。\nわたし――おまんこ――だき、ついて――ん、ふぁ」 | 「啊——呼——嗯——呼、啊——啊——我的——小穴——在抱著你——嗯、啊」 | 「A——hà——ưm——phù, Fua——hà, a.\nEm——âm đạo——đang ôm, chặt lấy——ưm, Fua」 | 「A——hà——ưm——phù, Fa——hà, a.\nEm——âm đạo——đang ôm, chặt lấy——ưm, Fa」 | JP ふぁ (x2); loose Fua -> Fa (both tokens) |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2114 | 「ふぁぁぁぁぁあっ――ああっ――そこ、すき、なの\nんっ――もっと、そこ、より――だけどっ、もっとぉ」 | 「呼啊啊啊――啊啊――我喜歡那裡，嗯――比那裡，要更――更――」 | 「Faaaaaaa――aa――Chỗ đó, em thích, lắm\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」 | 「Faaaaaa――aa――Chỗ đó, em thích, lắm\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」 | JP ふぁぁぁぁぁあっ (6 a's); VN has 7 a's - drop one |
| 真闇h3_補習授業の廃校舎.txt.toml | 2308 | 「うあ……どろっ、どろ――んっ――（すんっ、すん）\nふぁ……双ちゃんの……おとこの……ひとの……匂い」 | 「嗚啊……黏黏糊糊的――嗯――（嗅、嗅）哇……小雙……男孩子……的氣味」 | 「Ua……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFua……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」 | 「Ua……nhớt, nhớp nháp――ưm――（khịt, khịt）\nFa……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」 | JP ふぁ; loose Fua -> Fa |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 2170 | 「っっっ～～っ――ふぁっ、あっ――おっぱい――ん、\nふっ――ふあっ――んっ――ふうっ――ふうっ」 | 「呃～～――哇、啊――胸部――嗯、呼――嗚啊――嗯――呼――呼」 | 「Ư~~~――Fua, á――vú――ưm,\nphù――Fua――ưm――phù――phù」 | 「Ư~~~――Fa, á――vú――ưm,\nphù――Fua――ưm――phù――phù」 | JP ふぁ (1st token only); loose Fua -> Fa. KEEP 2nd 'Fua' for ふあっ |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 2188 | 「ふうっ――はぁ――んっ――ふぁっ――んっ――\n～～っ！　はっ――ふぁっ――ん……んふ――」 | 「呼――哈――嗯――哇――嗯――～～！　哈――哇――嗯……嗯唔――」 | 「Phù――hà――ưm――Fua――ưm――\n~~Ư! Hà――Fua――ưm……ưm phu――」 | 「Phù――hà――ưm――Fa――ưm――\n~~Ư! Hà――Fa――ưm……ưm phu――」 | JP ふぁ (x2); loose Fua -> Fa (both tokens) |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 2238 | 「あむっ――んっ――ふぁ……んっ――ちゅむっ\nほーへふっ――ふっ――しゅき――んっ――ちゅっ」 | 「啊嗚――嗯――哇……嗯――啾唔啊嗚――呼――喜歡――嗯――啾」 | 「A mu――ưm――fua…… ưm――chu mu\nAnh Houhefu――fu――hích anh――ưm――chụt」 | 「A mu――ưm――fa…… ưm――chu mu\nAnh Houhefu――fu――hích anh――ưm――chụt」 | JP ふぁ; loose fua -> fa. KEEP 'fu' for ふっ |

## §5. M17 — split-fa "Fu, a" vs "phù——a" (62 dòng)

Quy tắc áp dụng: loại A (JP tách ふ、あ) H-scene → romaji split "Fu"+dấu+"a"; loại B (JP nối nhưng VN tách) H-file → nối romaji (giữ dấu phân cách + token a theo sau), non-H file → nối dạng khoá VN. "ah" cho あっ/ぁっ giữ nguyên như moan pass đã viết (ふかみh1 987/992/1039, ふかみh2 1034). Dấu phân cách giữ nguyên theo JP; case của token a giữ nguyên ("Fu——A").

| File | Key | JP | TW | old_vn | fix | Lý do |
| --- | --- | --- | --- | --- | --- | --- |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1237 | 「あ……や――ふ、ぁ――\nはずかし――はずかしゅうございます」 | 「啊……這——呼啊——害羞——好害羞啊……」 | 「A…… ya——fu, a——\nXấu hổ——em xấu hổ lắm ạ.」 | 「A…… ya——Fu, a——\nXấu hổ——em xấu hổ lắm ạ.」 | type A (JP ふ、ぁ) H-scene: VN split 'fu, a' -> romaji split 'Fu, a' (unify capital Fu) |
| lr_ハチロクh1_今ひとたびの契り.txt.toml | 1252 | 「ん……ちゅっ――ん……ふ……ぁ……\nふっ――ちゅむっ――ちゅうっ――れるっ」 | 「嗯……啾……呼……啊……呼——啾唔——啾……唔」 | 「Ưm…… chụt——ưm…… fu…… a……\nFu——chumu——chuu——reru」 | 「Ưm…… chụt——ưm…… Fu…… a……\nFu——chumu——chuu——reru」 | type A (JP ふ……ぁ) H-scene: 'fu…… a' -> 'Fu…… a'. KEEP 'Fu——' for ふっ (M9) |
| lr_凪h1_痛いの痛いの飛んでけばい.txt.toml | 1128 | 「ひゃうっ！　あっ――ふあっ！　あっ！　おまんこっ！\nしきゅうっ――あちゅいのっ――おっぱいっ――ふ、あ」 | 「呀！啊……啊！啊！下面滋滋地……進來了燙燙的……胸部也……啊」 | 「Hyau! A——fua! A! Cô bé!\nTử cung——nóng quá——ngực cũng——fu, a」 | 「Hyau! A——fua! A! Cô bé!\nTử cung——nóng quá——ngực cũng——Fu, a」 | type A (JP ふ、あ) H-scene: trailing split 'fu, a' -> 'Fu, a'. KEEP 'fua!' for ふあっ |
| lr_凪h2_虎さんの交尾.txt.toml | 1239 | 「あ……ふ、ぁ――にーさん……唇――んっ――鼻息も、\nくすぐったかと――気持ち、よくって、じれったくって」 | 「啊……啊……大哥哥……你的嘴唇……嗯……還有鼻息，都癢癢的……好舒服……好急人」 | 「A……fu, a——anh Soutetsu……môi——ưm——cả hơi thở,\ncũng nhột quá——sướng, lắm, nôn nao quá」 | 「A……Fu, a——anh Soutetsu……môi——ưm——cả hơi thở,\ncũng nhột quá——sướng, lắm, nôn nao quá」 | type A (JP ふ、ぁ) H-scene: 'fu, a' -> 'Fu, a' |
| lr_日々姫h1_鏡の中日々姫.txt.toml | 1160 | 「だって――ふ、ぁっ――ひー、ちゃんっ――ちっちゃか、\nころ、からっ――がんば、て――がんば、った――けん」 | 「因為——呼、啊——小日——從小時候起——就很努力——很努力——」 | 「Tại vì——fu, a——Hi-chan——từ lúc, còn nhỏ——\nđã cố gắng——cố gắng, rất nhiều——mà.」 | 「Tại vì——Fu, a——Hi-chan——từ lúc, còn nhỏ——\nđã cố gắng——cố gắng, rất nhiều——mà.」 | type A (JP ふ、ぁっ) H-scene: 'fu, a' -> 'Fu, a' |
| lr_日々姫h2_デザートは食事の前に.txt.toml | 1045 | 「ちゅううううううっ！　んっ……ごくっ――ふ、あ\n――れるっ――れろおおっ――チュむっ――ちゅううっ」 | 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾……噗啾！」 | 「Chuuuuuuu! Ưm…… ực——fu, a\n——liếm——rerooo——chụt——chuuu」 | 「Chuuuuuuu! Ưm…… ực——Fu, a\n——liếm——rerooo——chụt——chuuu」 | type A (JP ふ、あ) H-scene: 'fu, a' -> 'Fu, a' |
| lr_日々姫真闇h1_三人家族.txt.toml | 1471 | 「ふやっ！？　やっ！　ふっ――あっ――ああっっ！！\nねぇね――私――こんな――ふ、ぁっ――上手、すぎっ」 | 「呼呀！？呀！呼——啊——啊啊！！阿姐——我——這樣弄——呼、啊——太厲害了」 | 「Fuya!? Ya! Fu――a――aa!!\nChị hai――em――thế này――fu, a――giỏi, quá.」 | 「Fuya!? Ya! Fu――a――aa!!\nChị hai――em――thế này――Fu, a――giỏi, quá.」 | type A (JP ふ、ぁっ) H-scene: 2nd split 'fu, a' -> 'Fu, a'. KEEP 1st split 'Fu――a' (already romaji) |
| lr_真闇h1_僕のおねえちゃん.txt.toml | 1436 | 「ごく、ごく――のんで、る――精子――精液っ――\n双ちゃん、の――ふ、ぁ――うれし――うれし、かっ」 | 「咕嘟、咕嘟地——喝、著——精子——精液——小雙、的——呼、啊——好開心——好開心」 | 「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\ncủa, Sou-chan——fu, a——vui——vui, quá」 | 「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\ncủa, Sou-chan——Fu, a——vui——vui, quá」 | type A (JP ふ、ぁ) H-scene: 'fu, a' -> 'Fu, a' |
| ふかみh1_ともはり練習.txt.toml | 987 | 「ふぁっ――あっ――わたしの――おまんこっ――\n双鉄、さんの――おくちっ――おくち、でっ――」 | 「哇……啊……我的……那裡……正在被……雙鐵先生的嘴巴……嘴巴……」 | 「Phù——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」 | 「Fa——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」 | type B (JP ふぁっ――あっ) H-scene: joined ふぁっ rendered split 'Phù——ah' -> 'Fa——ah'. KEEP 'ah' for あっ |
| ふかみh1_ともはり練習.txt.toml | 992 | 「ふぁ、あっ――べろ……あったか……いっ……んうっ」 | 「哇，啊……舌頭……好暖……呀……嗯」 | 「Phù, ah——lưỡi……ấm……quá……ưm.」 | 「Fu, ah——lưỡi……ấm……quá……ưm.」 | type A (JP ふぁ、あっ) H-scene: 'Phù, ah' -> 'Fu, ah'. KEEP 'ah' for あっ |
| ふかみh1_ともはり練習.txt.toml | 1039 | 「好き……好きって……双鉄さんが、わたしのことを――\nすでに好き、って……ふあ、ぁっ」 | 「喜歡……喜歡……雙鐵先生已經……喜歡上我了……哇」 | 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……phù, ah.」 | 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……Fu, ah.」 | type A (JP ふあ、ぁっ) H-scene: 'phù, ah' -> 'Fu, ah'. KEEP 'ah' for ぁっ as moan pass wrote it |
| ふかみh2_homesweethome.txt.toml | 1034 | 「ん……ふ、あっ――んっ――ふぁひ……んうっ――んっ、\nほーへふ……ふぁん……うくっ――んっ！」 | 「嗯……好……嗯……好……嗯，嗯，唔唔……嗯……嗯！」 | 「Ưm……phù, ah——ưm——fahi……ưm ư——ưm,\nHo he fu……fan……ư ku——ưm!」 | 「Ưm……Fu, ah——ưm——fahi……ưm ư——ưm,\nHo he fu……fan……ư ku——ưm!」 | type A (JP ふ、あっ) H-scene: 'phù, ah' -> 'Fu, ah'. KEEP 'ah' for あっ; 'fahi'/'fan' for ふぁひ/ふぁん are correct (M16 false positive) |
| れいなh1_おかあさんのレッスン.txt.toml | 1344 | 「んひゅっ！　ふあぁっ――あっ――ひ、んっ――\nそこ――れいな――ふ、ぁ――ぞりって、される、とぉ」 | 「啊嗯……蛤啊……啊……那裡……玲奈……蛤啊……被摩擦的話……」 | 「Nhyu! Fuaa——a——hi, ưm——\nChỗ đó——Reina——phù, a——bị cọ xát, thế này——」 | 「Nhyu! Fuaa——a——hi, ưm——\nChỗ đó——Reina——Fu, a——bị cọ xát, thế này——」 | type A (JP ふ、ぁ) H-scene: VN split 'phù, a' -> romaji split 'Fu, a' |
| ハチロク12_ムナカタ来訪.txt.toml | 1665 | 「ふあっ！」 | 「呃啊！」 | 「Phu a!」 | 「Phùa!」 | type B (JP ふあっ) NON-H: joined ふあっ rendered split 'Phu a!' -> locked VN 'Phùa!' |
| ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml | 965 | 「あ……ふ……あっ……あつい……です……\n双鉄……さま、の……ふっ――あっ――せい……えき」 | 「啊……呼……好……好熱……雙鐵少爺……的——啊——精液……」 | 「A……phù……a……nóng quá……\ntinh dịch……của……ngài Soutetsu……phù——a——」 | 「A……Fu……a……nóng quá……\ntinh dịch……của……ngài Soutetsu……phù——a——」 | type A (JP ふ……あっ) H-scene: 1st split 'phù……a' -> 'Fu……a'. KEEP 2nd split 'phù——a' (ふっ-based, U12a M9) |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 532 | 「……ん……ちゅっ――ちゅむっ――ちゅう……ふ、ぁ\n……だんな、さま――双鉄、さまぁ」 | 「……嗯……啾——啾咕——啾……呼，啊……夫君——雙鐵少爺」 | 「……Ưm……chụt——chụm——chụt……phù, a\n……phu, quân——ngài Soutetsu.」 | 「……Ưm……chụt——chụm——chụt……Fu, a\n……phu, quân——ngài Soutetsu.」 | type A (JP ふ、ぁ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 816 | 「や……そのようなお声……ふ、ぁ……わたくし……\nちく、び……んっ――恥ずかしい……です」 | 「呀……這種聲音……呼，啊……我的……乳頭……嗯——好害羞……」 | 「Ya……giọng nói đó của ngài……phù, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」 | 「Ya……giọng nói đó của ngài……Fu, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」 | type A (JP ふ、ぁ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 847 | 「はっ――むちゅっ――んっ――ちゅう――ふ、ぁ――\nん、れるっ――ひゅぁっ――えろっ――ん、く――あ！」 | 「哈——咕啾——啾——呼，啊——嗯，咻嚕——呀啊——啊嗚——啊！」 | 「Hà——chụm——ưm——chụt——phù, a——\nưm, mút——Hyua——liếm——ưm, Ku——a!」 | 「Hà——chụm——ưm——chụt——Fu, a——\nưm, mút——Hyua——liếm——ưm, Ku——a!」 | type A (JP ふ、ぁ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 906 | 「ん……ふ……ぁ……双鉄……さま――んっ……\nちく、び……なんだか……じれったい……です」 | 「嗯……呼……啊……雙鐵少爺……嗯……乳頭……感覺……急不可耐了……」 | 「Ưm……phù……a……ngài Soutetsu……ưm……\nnúm, vú……cảm giác……bứt rứt quá……ạ.」 | 「Ưm……Fu……a……ngài Soutetsu……ưm……\nnúm, vú……cảm giác……bứt rứt quá……ạ.」 | type A (JP ふ……ぁ) H-scene: 'phù……a' -> 'Fu……a' |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1045 | 「なんて……んっ――いやらいい……光景……ん、ふ、あ\n……それ、に……乳首、も、……へん、な……感じ、で」 | 「這麼……嗯——色情的……景象……呼，啊……而且……乳頭……也有……很奇怪的……感覺」 | 「Thật là một……ưm——quang cảnh……dâm đãng……ưm, phù, a\n……hơn nữa……núm vú, cũng, có……cảm giác……kỳ, lạ.」 | 「Thật là một……ưm——quang cảnh……dâm đãng……ưm, Fu, a\n……hơn nữa……núm vú, cũng, có……cảm giác……kỳ, lạ.」 | type A (JP ふ、あ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml | 1050 | 「そんな、に……した、ら――あっ――わた、くしっ、\nん……ふ――ぁ――おっぱい……おっぱいっ！」 | 「那樣子……做的話——啊——我、我的，嗯……呼——啊——乳房……乳房！」 | 「Làm, như thế……thì——a——em,\nưm……phù——a——vú……vú!」 | 「Làm, như thế……thì——a——em,\nưm……Fu——a——vú……vú!」 | type A (JP ふ――ぁ) H-scene: 'phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 485 | 「は……ぁ……く……は――ふ……あっ――だんな、さま、\nの、手……ん……お尻……ひら……い、てっ――」 | 「……啊……——呼……啊——夫君，的手……把屁股……掰開……了——」 | 「Hà……a……Ku……hà——phù……a——bàn tay, của……\nphu, quân……ưm……đang banh……mông, ra——」 | 「Hà……a……Ku……hà——Fu……a——bàn tay, của……\nphu, quân……ưm……đang banh……mông, ra——」 | type A (JP ふ……あっ) H-scene: 'phù……a' -> 'Fu……a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 694 | 「いや、ですっ――んっ……ふ、あっ――だんな、さ、ま\n――あ！　お指、で――でも――一人で――イク、など」 | 「不要——……呼，啊——夫君——啊！在手指——但——但我不能——一個人高潮啊」 | 「Không, muốn đâu——ưm……phù, a——phu, quân\n——a! Bằng ngón, tay——nhưng mà——lên đỉnh——một mình, thì.」 | 「Không, muốn đâu——ưm……Fu, a——phu, quân\n——a! Bằng ngón, tay——nhưng mà——lên đỉnh——một mình, thì.」 | type A (JP ふ、あっ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 763 | 「ひうっ！？　ふ――あっ！？　そ、双鉄、さまっ！\n待っ――待っ――まぁっ――っ！　～～～～っっ！！！」 | 「咿！？呼——啊！？雙，雙鐵少爺！等——等——等等——！～～～～！！！」 | 「Hiu!? Phù——a!? Ng, Ngài Soutetsu!\nĐợi——đợi——đợi đã——! ~~~~ƯƯ!!!」 | 「Hiu!? Fu——a!? Ng, Ngài Soutetsu!\nĐợi——đợi——đợi đã——! ~~~~ƯƯ!!!」 | type A (JP ふ――あっ) H-scene: 'Phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 791 | 「あ……ん……ちゅっ――ちゅむっ――ンッ――\nふ――っぁ……れろっ――れるっ――ちゅる――ちゅ」 | 「啊……啾——啾姆——嗯——呼——啊……嗯——咻嚕——啾嚕——啾」 | 「A……ưm……chụt——chụm——ưm——\nphù——a……liếm——mút——chụt——chụt」 | 「A……ưm……chụt——chụm——ưm——\nFu——a……liếm——mút——chụt——chụt」 | type A (JP ふ――っぁ) H-scene: 'phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 802 | 「ぁきゅ！　んっ！　はっ――しゅごっ！　ふ、あっ――\nおっぱい、も――おまん、まん――もぉっ！！！！」 | 「啊嗯呀！嗯！哈——好棒！呼，啊——乳房——小妹妹——已經！！！！」 | 「A kiu! Ưm! Hà——sướng quá! Phù, a——\nvú, cũng——cô, bé——rồi!!!!」 | 「A kiu! Ưm! Hà——sướng quá! Fu, a——\nvú, cũng——cô, bé——rồi!!!!」 | type A (JP ふ、あっ) H-scene: 'Phù, a' -> 'Fu, a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 816 | 「んっ――あ……双鉄……さま……ふ――ぁ――ん、\n大丈夫……です……よ？　いいこ……ね？　いいこ……」 | 「嗯——啊……雙鐵少爺……呼——啊——沒關係的……乖哦……要乖乖的哦……」 | 「Ưm——a……Ngài……Soutetsu……phù——a——ưm,\nKhông sao……đâu……ạ? Ngoan nào……nhé? Ngoan nào……」 | 「Ưm——a……Ngài……Soutetsu……Fu——a——ưm,\nKhông sao……đâu……ạ? Ngoan nào……nhé? Ngoan nào……」 | type A (JP ふ――ぁ) H-scene: 'phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 821 | 「ん……ふ―あっ――だんな、さまの――舌が……ぬる、\nぬる……と……わたくしの、肌――唾液で、濡ら、して」 | 「嗯……呼啊——夫君——舌頭……黏黏的……把我的，皮膚——都給舔濕吧」 | 「Ưm……phù——a——chiếc lưỡi——của phu, quân……trơn,\ntrơn……ướt……làm ướt, làn da của em——bằng, nước bọt.」 | 「Ưm……Fu——a——chiếc lưỡi——của phu, quân……trơn,\ntrơn……ướt……làm ướt, làn da của em——bằng, nước bọt.」 | type A (JP ふ―あっ) H-scene: 'phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 837 | 「んひゅっ！！　ふ――あっ！　あっ！　あっ！！」 | 「嗯咻！！呼——啊！啊！啊！！」 | 「Nhyu!! Phù——a! A! A!!」 | 「Nhyu!! Fu——a! A! A!!」 | type A (JP ふ――あっ) H-scene: 'Phù——a' -> 'Fu——a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 853 | 「だんな……さまっ――ふ、ぁっ――すず――の、\nおむね、が――乳首、が――伸び、て――んっ！」 | 「夫君……——呼，啊——鈴的——胸部——乳頭——給拉長了，嗯——！」 | 「Phu……quân——phù, a——ngực, của——\nSuzu——núm vú, bị——kéo dài, ra——ưm!」 | 「Phu……quân——Fu, a——ngực, của——\nSuzu——núm vú, bị——kéo dài, ra——ưm!」 | type A (JP ふ、ぁっ) H-scene: 'phù, a' -> 'Fu, a' |
| ハチロクh7_レトロモダンメイクラヴ.txt.toml | 968 | 「そうてつ、さまっ！　ふ――あっ！　だんな、さまっ！\nわた――くし――わた、し、の――愛おしい――方っ！」 | 「雙鐵少爺！呼——啊！夫君！我——我——愛的人啊——！」 | 「Ngài, Soutetsu! Phù——a! Phu, quân!\nNgười——mà——em, vô cùng——yêu, thương!」 | 「Ngài, Soutetsu! Fu——a! Phu, quân!\nNgười——mà——em, vô cùng——yêu, thương!」 | type A (JP ふ――あっ) H-scene: 'Phù——a' -> 'Fu——a' |
| ハチロクh8_桜色のひめごと.txt.toml | 743 | 「ひあっ！？　いやですぅ――わざと――ふ、ぁっ――\nんっ――わざと、そのようなっ――下品な、音――く！」 | 「咿啊！？討厭——故意——呼，啊——嗯——故意，那樣——粗俗的，聲音——！ | 「Hia!? Không chịu đâu——cố tình——phu, a——\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」 | 「Hia!? Không chịu đâu——cố tình——Fu, a——\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」 | type A (JP ふ、ぁっ) H-scene: 'phu, a' -> 'Fu, a' |
| ハチロクh8_桜色のひめごと.txt.toml | 762 | 「あ――はっ――ひっ――いいっ！　きもちっ――ふ、あ\nきもちいっ――あ――おっぱい、も――おまんまん、も」 | 「啊——哈——哈——好！舒服——呼，啊舒服——啊——乳房，和——小妹妹，都是」 | 「A——ha——hi——thích quá! Sướng——phù, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」 | 「A——ha——hi——thích quá! Sướng——Fu, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」 | type A (JP ふ、あ) H-scene: 'phù, a' -> 'Fu, a' |
| ポーレット03_大きなにもつのおばあさん.txt.toml | 1583 | 「ふぁ……あ～っ」 | 「呼……啊~」 | 「Phù…… a~Ư」 | 「Phà…… a~Ư」 | type B (JP ふぁ……あ～っ) NON-H: joined ふぁ rendered split 'Phù…… a~Ư' -> locked VN 'Phà…… a~Ư' |
| ポーレット03_大きなにもつのおばあさん.txt.toml | 1588 | 「ふあっ――あ～っ！　う～、ちょっと伸びすぎ！\nあーでも……うん。血行、よくなった感じする～」 | 「呼……啊～！嗚，剛才伸展過頭啦！啊，不過……嗯。感覺血液循環得順暢多了～」 | 「Phù—— a~! Ư~, kéo dãn hơi quá rồi!\nÀ nhưng mà…… ừm. Cảm giác máu lưu thông tốt hơn hẳn~」 | 「Phùa—— a~! Ư~, kéo dãn hơi quá rồi!\nÀ nhưng mà…… ừm. Cảm giác máu lưu thông tốt hơn hẳn~」 | type B (JP ふあっ――あ～っ) NON-H: 'Phù—— a~!' -> locked VN 'Phùa—— a~!' |
| ポーレット10_見えない傷.txt.toml | 1319 | 「ふぁ……あー――満腹です。\nほんっと、おいしかったぁ――御馳走さまでした」 | 「呼……啊——吃飽了。真是太美味了——多謝款待」 | 「Phù……A——No quá đi mất.\nThật sự rất ngon luôn——Cảm ơn vì bữa ăn.」 | 「Phà……A——No quá đi mất.\nThật sự rất ngon luôn——Cảm ơn vì bữa ăn.」 | type B (JP ふぁ……あー) NON-H: 'Phù……A——' -> locked VN 'Phà……A——' |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 852 | 「ひゃうんっ！」　ふあっ――そ、双鉄――くんっ！\nんぅうううっ！！！」 | 「呀！呼啊——雙、雙鐵！嗯啊啊啊！！！」 | 「Hyaun!」 Phù——a, anh Soutetsu——!\nƯm ư ư ư!!!」 | 「Hyaun!」 Fua——anh Soutetsu——!\nƯm ư ư ư!!!」 | type B (JP ふあっ――そ) H-scene: joined ふあっ rendered split 'Phù——a,' -> 'Fua——' (absorb split 'a,') |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 1015 | 「舌っ――んっ！　ふ、あっ――入って――ぬるって！\nわたしの、おまんこ――[なか,1]膣内、[すす]啜られて、んうぅっ！！」 | 「舌頭——嗯！呼、啊――進來了――滑進來了！我的小穴裡面——被舔到了，嗯！！」 | 「Lưỡi——ưm! Phù, a——vào rồi——trơn tuột! Cô bé, của em——bên trong âm đạo, bị húp trọn, ưm ư ư!!」 | 「Lưỡi——ưm! Fu, a——vào rồi——trơn tuột! Cô bé, của em——bên trong âm đạo, bị húp trọn, ưm ư ư!!」 | type A (JP ふ、あっ) H-scene: 'Phù, a' -> 'Fu, a' |
| ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml | 1050 | 「おちん、ちん――ふ、あっ――ね？――落ち着いて――ンッ――いいこ、いいこ――で――入線、しよ――ね？」 | 「雞雞——呼——那個——停一下——嗯——慢慢地——進站吧」 | 「Dương, vật——phù, a——nhé?——Bình tĩnh lại nào——ưm——ngoan, ngoan——rồi——tiến vào ga, nhé——được không?」 | 「Dương, vật——Fu, a——nhé?——Bình tĩnh lại nào——ưm——ngoan, ngoan——rồi——tiến vào ga, nhé——được không?」 | type A (JP ふ、あっ) H-scene: 'phù, a' -> 'Fu, a' |
| ポーレットh6_あなたとふたりの学園エッチ.txt.toml | 790 | 「フ、ァッ！――あっ！　おっぱい――そこ――\nさきっぽ――ちく、び――っ！」 | 「呼、啊！——啊！胸部——那裡——前端——乳頭！」 | 「Phù, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」 | 「Fu, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」 | type A (JP フ、ァッ) H-scene: 'Phù, a' -> 'Fu, a' |
| ポーレットh8_気動車の国のアリス.txt.toml | 2129 | 「やっ――へん、んっ――そこっ――ふ、あっ――\nなん、かっ――っ――あっ、ぶるって、ふ、あっ――」 | 「呀——好奇怪、嗯——那裡——呼、啊——有什麼——啊，抖了一下——啊——」 | 「Á——lạ, lắm——chỗ đó——phù, a——\ncái, gì đó——ư——a, run rẩy, phù, a——」 | 「Á——lạ, lắm——chỗ đó——Fu, a——\ncái, gì đó——ư——a, run rẩy, Fu, a——」 | type A (JP ふ、あっ x2) H-scene: both splits 'phù, a' -> 'Fu, a' |
| ポーレットh8_気動車の国のアリス.txt.toml | 2161 | 「は……ん……ちゅっ――ちゅうっ――チュ――\nふ、あ――しゅき――ほーへふ、ふん――ん、ちゅっ」 | 「呼……嗯……啾——啾——啾——呼啊——我喜歡你——雙鐵——嗯——啾」 | 「Hà……ưm……chụt——chụt——chụt——phù, a——thích quá——Anh Soutetsu, ơi——ưm, ưm, chụt」 | 「Hà……ưm……chụt——chụt——chụt——Fu, a——thích quá——Anh Soutetsu, ơi——ưm, ưm, chụt」 | type A (JP ふ、あ) H-scene: 'phù, a' -> 'Fu, a' |
| ポーレットh8_気動車の国のアリス.txt.toml | 2224 | 「あ――んっ……ちゅっ――ふ――あっ――\nちゅっ――ちゅむっ――ちゅうっ――ちゅっ――」 | 「啊——嗯……啾——呼——啊——啾——啾嚕——啾噗——啾——」 | 「A——ưm……chụt——phù——a——chụt——chụt——chụt——chụt——」 | 「A——ưm……chụt——Fu——a——chụt——chụt——chụt——chụt——」 | type A (JP ふ――あっ) H-scene: 'phù——a' -> 'Fu——a' |
| 凪h1_ふたりっきりのデート.txt.toml | 1102 | 「あ……あっ――いまの――でっ――んっ――ふ、あっ、\nウチ、今……にーさんの声、で……イっちゃった、ばい」 | 「啊……啊……剛才的……嗯……呼，啊，咱剛被……大哥哥的聲音……弄丟了」 | 「A……A——Lúc nãy——á——Ưm——Phù, a,\nEm, vừa nãy……chỉ vì giọng nói của anh hai……mà lên đỉnh mất rồi, á」 | 「A……A——Lúc nãy——á——Ưm——Fu, a,\nEm, vừa nãy……chỉ vì giọng nói của anh hai……mà lên đỉnh mất rồi, á」 | type A (JP ふ、あっ) H-scene: 'Phù, a' -> 'Fu, a' |
| 凪h1_ふたりっきりのデート.txt.toml | 1106 | 「は……うっ……気持ち、よか……んっ――にーさんの、\n手に……おっぱい……とろとろ……されて――ふ――あ」 | 「啊……嗚……好舒服……嗯……大哥哥的手……把我胸部……弄得黏糊糊的……呼……啊」 | 「Hà……Ư……Sướng, quá……Ưm——Bàn tay,\ncủa anh hai……Làm ngực em……Nhũn cả ra……rồi——Phù——A」 | 「Hà……Ư……Sướng, quá……Ưm——Bàn tay,\ncủa anh hai……Làm ngực em……Nhũn cả ra……rồi——Fu——A」 | type A (JP ふ――あ) H-scene: 'Phù——A' -> 'Fu——A' (preserve capital A) |
| 日々姫h1_マッサージの続き.txt.toml | 1013 | 「はっ――ひっ――んっ――ふあっ――あっ――」 | 「呼――呀――嗯――呼――啊――」 | 「Hơ——Hi——Ưm——Phù——A——」 | 「Hơ——Hi——Ưm——Fua——A——」 | type B (JP ふあっ――あっ) H-scene: joined ふあっ rendered split 'Phù——A' -> 'Fua——A' (keep —— separator + A) |
| 日々姫h1_マッサージの続き.txt.toml | 1017 | 「ふあっ――あっ――んっ――にぃに――にぃにぃっ」 | 「呼――啊――嗯――阿哥――阿哥」 | 「Phù——A——Ưm——Anh hai——Anh hai.」 | 「Fua——A——Ưm——Anh hai——Anh hai.」 | type B (JP ふあっ――あっ) H-scene: 'Phù——A' -> 'Fua——A' |
| 日々姫h1_マッサージの続き.txt.toml | 1018 | 「ふぁ……あっ――にぃにぃ」 | 「呼……啊――阿哥」 | 「Phù... a——anh hai.」 | 「Fa... a——anh hai.」 | type B (JP ふぁ……あっ) H-scene: 'Phù... a' -> 'Fa... a' (keep ... separator + a) |
| 日々姫h2_洗って大丈夫なスーツ.txt.toml | 1076 | 「ふあ……ぁ……んっ……うれし……\nぴったり――わたし、おまんこ――にぃにの、と」 | 「呼……啊……嗯……好高興……我的小穴――和阿哥的――正合適」 | 「Phù... a... Ưm... Vui quá... Vừa khít——Cô bé, của em——với của, anh hai.」 | 「Fua... a... Ưm... Vui quá... Vừa khít——Cô bé, của em——với của, anh hai.」 | type B (JP ふあ……ぁ) H-scene: 'Phù... a' -> 'Fua... a' |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 928 | 「……ふ……ぁ――しまっとらん、よ？　にぃに――っ、\nん……今のは――だって――下塗り――やけん……」 | 「……呼……啊――沒有、完啊――阿哥――嗯……剛才――算是――塗底色……」 | 「……Phù……a――Chưa xong, đâu? Anh hai――,\nưm……Vừa rồi――chỉ là――lớp sơn lót――thôi mà……」 | 「……Fu……a――Chưa xong, đâu? Anh hai――,\nưm……Vừa rồi――chỉ là――lớp sơn lót――thôi mà……」 | type A (JP ふ……ぁ) H-scene: 'Phù……a' -> 'Fu……a' |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 1129 | 「我慢……せんで、よかと、よ？　ふ……ぁ――\nにぃにの、お声、んっ――私、もっと聞きたい、けん」 | 「不用……忍著啦。呼……啊――我想多聽聽――阿哥的、嗯――聲音」 | 「Không cần……phải nhịn, đâu? Phù……a――\nGiọng nói, của anh hai, ưm――Em, muốn được nghe nhiều hơn nữa, cơ」 | 「Không cần……phải nhịn, đâu? Fu……a――\nGiọng nói, của anh hai, ưm――Em, muốn được nghe nhiều hơn nữa, cơ」 | type A (JP ふ……ぁ) H-scene: 'Phù……a' -> 'Fu……a' |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 1190 | 「ふあ……ぁ……ア……ん……くっ――あ――\nはぁっ――はあっ――はあっ……ふ、ぁ――あっ」 | 「呼……啊……啊……嗯……唔――啊――呼――呼――呼……呼、啊――啊」 | 「Fua……a……a……ưm……hự――a――\nHà――hà――hà……phù, a――a」 | 「Fua……a……a……ưm……hự――a――\nHà――hà――hà……Fu, a――a」 | type A (JP ふ、ぁ) H-scene: 'phù, a' -> 'Fu, a' |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 1191 | 「ふ……ぁ……んっ――むぃ――ぃ～」 | 「呼……啊……嗯――唔――哥～」 | 「Phù……a……ưm――anh――hai~」 | 「Fu……a……ưm――anh――hai~」 | type A (JP ふ……ぁ) H-scene: 'Phù……a' -> 'Fu……a' |
| 日々姫h5_白濁絵の具の射精会.txt.toml | 1192 | 「ふ……あっ……えぐれる――みたい、で……ぁっ――\nはっ――にぃにの――あつさ――すごく……感じ、て」 | 「呼……啊……好像――頂到了……啊――呼――能感受到――阿哥的――很熱……」 | 「Phù……a……Như bị――khoét sâu, vậy……a――\nHà――Độ nóng――của anh hai――cảm nhận……rất rõ」 | 「Fu……a……Như bị――khoét sâu, vậy……a――\nHà――Độ nóng――của anh hai――cảm nhận……rất rõ」 | type A (JP ふ……あっ) H-scene: 'Phù……a' -> 'Fu……a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 1944 | 「らめっ――しきゅ、しきゅうっ！　ふ、あっ！\nいま、いまっ――らめ、なのっ――ぎゅうって、して」 | 「不行――子宮、子宮！呼、啊！剛才、剛才――明明、不行的――卻好有感覺」 | 「Không được――Tử, tử cung! Phù, a!\nBây giờ, ngay bây giờ――không được, đâu――nó siết chặt, quá」 | 「Không được――Tử, tử cung! Fu, a!\nBây giờ, ngay bây giờ――không được, đâu――nó siết chặt, quá」 | type A (JP ふ、あっ) H-scene: 'Phù, a' -> 'Fu, a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2106 | 「ふ……ぁ――あっ――にぃ、に――きつっ、ん」 | 「呼……啊――啊――阿哥――好難受、嗯」 | 「Phù……a――a――Anh, hai――chật quá, ưm」 | 「Fu……a――a――Anh, hai――chật quá, ưm」 | type A (JP ふ……ぁ) H-scene: 'Phù……a' -> 'Fu……a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2194 | 「あ……ンッ――ふ、あっ」 | 「啊……嗯――呼、啊」 | 「A……ưm――phù, a」 | 「A……ưm――Fu, a」 | type A (JP ふ、あっ) H-scene: 'phù, a' -> 'Fu, a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2255 | 「う、うん。できるよ。やると。う……ふ……あんっ\nきとう……にぃにの、おちんちんの、さきっぽ、を」 | 「嗯、嗯。我能做到，我試試。唔……呼……嗯，龜頭……插入、阿哥的、雞雞的、前端」 | 「V-Vâng. Em làm được. Em sẽ làm. Ư……phù……a\nQuy đầu……phần đầu, chim của anh hai」 | 「V-Vâng. Em làm được. Em sẽ làm. Ư……Fu……a\nQuy đầu……phần đầu, chim của anh hai」 | type A (JP ふ……あんっ) H-scene: 'phù……a' -> 'Fu……a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2297 | 「ぷあっ！　あっ！　あっ――ふ、あっ――ああ――\nは――ああ……ふあ――あっ――」 | 「噗哈！啊！啊――呼、啊――啊啊――呼――啊……呼――啊――」 | 「Pua! A! A――phù, a――a――\nHà――a……Fua――a――」 | 「Pua! A! A――Fu, a――a――\nHà――a……Fua――a――」 | type A (JP ふ、あっ) H-scene: 'phù, a' -> 'Fu, a' |
| 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml | 2713 | 「にぃ、に――んっ――くううう～～ん――ふ、あっ\nすと……レッチ、も――いい、けど――よか、けどっ」 | 「阿哥――嗯――唔唔唔～～嗯――呼、啊，伸……伸展運動――做的差不多了吧」 | 「Anh, hai――ưm――kuuuu~~n――phù, a\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」 | 「Anh, hai――ưm――kuuuu~~n――Fu, a\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」 | type A (JP ふ、あっ) H-scene: 'phù, a' -> 'Fu, a' |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 2203 | 「は……んっ――ふ、ぁ……手……双鉄の、手――\nあったか――ふっ……はぁ……はふっ」 | 「哈……嗯――呼、啊……手……雙鐵的手――熱呼呼的――呼……蛤啊……哈呼」 | 「Ha…… ưm――fu, a…… tay…… tay của, anh Soutetsu――\nấm quá――fu…… ha…… ha fu」 | 「Ha…… ưm――Fu, a…… tay…… tay của, anh Soutetsu――\nấm quá――fu…… ha…… ha fu」 | type A (JP ふ、ぁ) H-scene: 'fu, a' -> 'Fu, a' |
| 稀咲h3_チャイナドレスでおもてなし.txt.toml | 2265 | 「ん……ふっ――んっ――ちゅっ――ちゅむっ――\nちゅるっ――ちゅっ――んちゅっ――ふ……あ――」 | 「嗯……呼――嗯――啾――啾唔――啾――啾――嗯啾――呼……啊――」 | 「Ưm…… fu――ưm――chụt――chu mu――\nchu ru――chụt――ưm chu――fu…… a――」 | 「Ưm…… fu――ưm――chụt――chu mu――\nchu ru――chụt――ưm chu――Fu…… a――」 | type A (JP ふ……あ) H-scene: 'fu…… a' -> 'Fu…… a'. KEEP 'fu――' for ふっ (M9) |

## §6. Giữ nguyên / cờ (kept / flagged — đã xem nhưng KHÔNG sửa)

### 6a. Giữ nguyên — non-H, dạng khoá đúng sẵn (M1)

lrれいな追加01 1097, 1101; lrれいな追加02 1274; lrれいな追加03 659; lr真闇追加03 1470; れいな03 1371; グランドリライト05 1816; ハチロク11 1744, 1772; ハチロク15b 1571, 1614; 共通13 2033; 凪ふかみ01 1589; 凪ふかみ07 2042; 凪ふかみ08b 2174, 2176; 凪ふかみ08c 2073; 日々姫03 2389; 日々姫07 1759. Riêng 1097 ("Phùa~ a") và 1274 ("Phùa a."): dạng khoá đã có, chỉ tách mora kéo dài cuối — giữ (biến thể khoảng trắng trong non-H dialogue).

### 6b. Giữ nguyên — đã đúng sẵn (M16/M17)

- Romaji dài đã đúng (đếm mora khớp): ポーレットh4 911, 日々姫h6 2196, lrれいな追加h 1080, れいなh3 1019, れいなh4 1983, lr_日々姫ふかみh1 1359, lr_日々姫真闇h1 1467 (ふや dài); ハチロクh5 1222, 真闇h3 2310, ふかみh3 2289 (a/n khớp).
- Romaji đúng sẵn: 凪h1 1234 ("Fahaa"), 日々姫h2 1038 ("famu"), ポーレットh4 882 ("Kyafua"), れいなh1 1282 ("Hafefe"), れいなh1 1341 ("rafa"), れいなh3 1119 ("Fuei"), 真闇h1 1491 ("Foo"), 凪ふかみh2 1299 ("Hyafa"), 日々姫h4 1032 ("Fa"), ふかみh2 1034 ("fahi"/"fan" — M16 false positive), ハチロク15b 1657 ("faffafa"), 凪h1 1121 ("afahaha" trong chuỗi gibberish).
- Split đã romaji sẵn (M17, không sửa): lr_ふかみh1 1223/1379/1458, lr_ふかみh2 1179, lr_れいなh1 1424, lr_ニイロクh 1274/1297/1392, lr_日々姫h1 1047, lr_日々姫h2 1108, lr_日々姫真闇h1 1450/1484, lr_真闇h1 1425, lrれいな追加h 1168/1283/724, lr稀咲追加h 1104/1147/1195, lr追加_みくろ 1705, ふかみh3 2371/2384, れいなh4 1976, ハチロクh2 1011, ハチロクh5 1178, ハチロクh9 1356/2109/2151/2289/2378/2613, 凪ふかみh2 1300, 日々姫h3 1112, 稀咲h3 2189, ポーレットh7 901, lrれいな追加h 1202, ふかみh3 2359, 凪ふかみh1 1505 (token "fa" đúng + split M9).
- Split non-H KEEP (M17 loại A): ポーレット03 1584/1586, ポーレット07 1686.
- "Hể?" đã đúng sẵn theo F1 M10 (thuộc U12a, không sửa ở đây): 日々姫h1 1054, 日々姫h2 947, 日々姫06 2486, 日々姫02 1974.

### 6c. Giữ nguyên — gibberish / yawn / nghĩa (không thuộc scope M1/M16/M17)

- Gibberish render thành nghĩa/từ: lr_凪ふかみh1 1550, lr_ハチロクh2 1112, 凪ふかみh1 1545, ハチロクh3 1139, 凪ふかみh2 1372/1455, 凪ふかみ02 2071, ハチロク07 2916/2917, ハチロクh2 1014 (baby-talk), れいなh2 1104/1199, 凪ふかみ01 2079 ("Ngoạm").
- Ngáp / thở render thành nghĩa ("Oa", "Oáp", "hơ", "Phaaaa"): ハチロク01 2348, ハチロク02 2038, ハチロク03 2149, ハチロク06 1619, ハチロク09 1747, ポーレット06 1842, ポーレット07 1652/1656/1659/1718/1719, ポーレット10 1324/1354, ポーレット11 1366, ポーレット13 1290, ポーレット15 1516, 仲国05 1940/1952, 仲国06 1738, 共通05 2268, 凪ふかみ02 2107, 凪ふかみ03 2272, 凪ふかみ04 2177, 凪ふかみ05 2084, ポーレット04 1836, ポーレット06 1829, 凪ふかみ07 2026.
- ふぁ/ふぇ/ふや trong từ thường (không phải moan): 凪ふかみh1 1495 (フェラチオ), 日々姫06 2261 + 日々姫h6 2090 (ふやしたら), ハチロク07 3540 (ふぁさっと), ハチロク14 2413 + グランドリライト09 1988 (ふえる).
- 0 dòng "phá" moan: scan 153 dòng chứa "phá" — toàn từ thường ("phá vỡ"/"phá hỏng"/"khai phá"), không có token moan "phá" nào.

### 6d. Cờ cho điều phối / batch khác

- **U12a M11 (ふや → "Fuya", 16 dòng — để U12a):** lr追加_みくろ 1731; ふかみh3 2366; れいなh1 1263, 1525, 1531; ハチロクh4 1121, 988; ポーレットh2 929, 957; 凪h1 1053, 1057, 1081; 日々姫h2 1081; 日々姫h3 1042; 日々姫h4 964; 真闇h1 1021.
- **U12a M10 (ふぇ/ふえ — để U12a):** lr_れいなh1 1179/1199/1236 (đã loại khỏi M16), 凪h1 1090/1091, ふかみh1 993, 凪ふかみ01 1547, 共通13 2038/2432, ハチロク02 2170, れいなh1 1266/1278/1526/1355, ポーレットh2 956/967, 日々姫07 1720/1742, ポーレット03 1638, ポーレット06 1816, ポーレット15 1529, ポーレットh5 903, 仲国05 2378, 凪ふかみ01 1595/1627, 凪ふかみ02 2056, 凪ふかみh2 1324/1403, 日々姫h1 1015/1025, 真闇h3 2238, れいなh3 1133, lr追加_みくろ 1708/1758, ハチロク01 2304 ("Oe"), 稀咲h1 1282 ("fê" cuối chuỗi cười).
- **U12a M9 (ふっ — để U12a; các split ふっ trong cùng dòng với fix của batch này đã giữ nguyên):** lr_日々姫ふかみh1 1479, lr追加_ひよこ 1433/2338/2457 (split thứ 2), ふかみh3 2767, ハチロクh7 971, ポーレットh7 885, ポーレットh8 2303, ハチロクh4 965 (split thứ 2), ハチロクh6 869, lr真闇追加h 1091, 凪h1 1128/1153/1178 + 稀咲h3 2265 + lr_ハチロクh1 1252 (phần "Fu——a"/"fu——" cho ふっ trong cùng dòng).
- **T79 (split ぷ — để batch T79):** ハチロク13 1841, ふかみh1 1047, ポーレットh5 942.
- **凪ふかみh2 1271 — cần coordinator quyết:** split "phù——a" cho ふうっ――あっ (token ふう, không phải fa cũng không phải ふっ) — nằm giữa M9 và M17; chưa áp dụng quy tắc split-romaji cho ふう, để coordinator quyết có mở rộng M17 sang ふう hay không.
- **Trùng dòng với U12a (11 dòng — fix của batch này chỉ chạm token đã nêu; coordinator gộp nếu U12a cũng sửa cùng dòng):** lr追加_みくろ 1857, 1967, 2198; lr_日々姫ふかみh1 1479; ハチロクh8 708, 759; 稀咲h3 2188; lr_ハチロクh1 1237; lr_日々姫真闇h1 1471; 日々姫h5 1190; ふかみh2 1034. (Riêng lr追加_みくろ 1716: cùng dòng có ふえっ → "phuê" thuộc U12a M10 — fix M1 chỉ chạm token ふあっ.)
- **0 trùng với 8 batch đã gộp** (656 (file,key) đã kiểm chứng).

## §7. Lượt soát 2 (second pass — bắt buộc)

- Tổng số fix: **166**; tái kiểm chứng: **166**; loại bỏ: **0**; sửa lại: **0**.
- Phương pháp soát 2: với mỗi dòng, tách token đã đổi (old_sub → new_sub) và đối chiếu độc lập với JP — hepburn strict của token JP, đếm mora (a/u/e/i/o/n) cho token dài/dán (891, 1358), dạng split JP (kể cả ふ――っぁ có っ xen giữa và katakana フ、ァッ), dạng khoá cho non-H; kiểm tra old_sub biến mất đúng số lần; kiểm tra H-scene không còn dạng khoá/split VN cho token fa (trừ split ふっ/ぷ được giữ theo scope).
- Lỗi checker đã sửa trong lúc soát (không phải lỗi fix): v1 bỏ sót split JP (không nhận っ xen giữa, không nhận katakana ァ) và token dán (đếm mora sai cho ふぁふゅ…); v2 kiểm chứng lại toàn bộ — **166/166 đậu, 0 loại, 0 sửa**.
- Sửa phát hiện ở vòng kiểm chứng đầu (trước soát 2): lr_れいなh1 1204 (cả hai token đều "Fua" — chỉ sửa token cuối) và 3 basename sai (凪h1 1128, 凪h2 1239, 日々姫h2 1045).

## §8. Khối TOML (parse-verified)

Mỗi khối một file; literal backslash-n trong giá trị fix được viết `\\n` trong raw text của khối (parse ra đúng literal backslash-n như trong file TOML); newline thật (2 dòng: ハチロクh6 816, 847 — giá trị nguồn CSV3 chứa newline thật, khác artifact flatten của TOML-2; CSV3 là chuẩn) được viết `\n` (TOML escape cho newline). Tất cả khối đã parse-verified bằng tomllib và khớp JSON tuyệt đối.

#### lr_ポーレットh2_デコレーション＆ミルク.txt.toml

```toml
[script]
"1074" = "「A——Fa——anh Soutetsu——anh Soutetsu」"
```

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml

```toml
[script]
"1464" = "「Fa——a……Làm tình—— Làm tình——em……muốn làm…………ưm.」"
"1467" = "「Fa……a——a……ưm——（Ực）——đầy ắp, tinh, dịch——của anh Soutetsu……sắp tràn, ra rồi……」"
"1470" = "「Faaaaan! Anh Soutetsu, nè? Anh Soutetsu——a, em, nè? Em——em, sắp, sắp, sắp rồi!」"
"1497" = "「Oa——oa——dịu dàng quá……như thể đang dùng tay vuốt ve khen ngợi dương vật là bé ngoan vậy……Fa.」"
"1513" = "「Ha——ưm——Fa——a——. Anh, Soutetsu—— Anh Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, anh Soutetsu?」"
"1584" = "「Chuu u——ưm……chu pa. Fa……Ưm, Kisaki………… Nè? ——Cảm ơn em.」"
"1641" = "「Tuyệt, quá——a——xấu hổ quá——em, rõ ràng, ——vẫn còn trinh——là lần đầu tiên——vậy mà, Fa.」"
```

#### lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml

```toml
[script]
"1678" = "「Hyau── ưm── Fua── a──\\nA── a── a── aa──」"
"1714" = "「Fua── a── a── gì thế, này──\\nGì thế, này!! Sướng quá, Mikuro, sướng quá.」"
"1716" = "「Fua── a── tuyệt quá── phuê!!?\\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」"
"1718" = "「Fua── a── tuyệt quá── thế này── a──\\nNhanh── mạnh── sâu, thế này」"
"1720" = "「Fua── a── ngón tay của chị Hibiki…… ngón tay──\\nMikuro── âm vật của Mikuro, đang──」"
"1722" = "「Fua── a── mở rộng ra── Mikuro──\\nđang được chị Hibiki── vạch ra, ạ」"
"1733" = "「Fuaa!? A──Mi, Mikuro, vừa nãy──\\nChỗ đó của Mikuro── sướng lắm ạ.」"
"1735" = "「Fua! A! Cùng nhau── cùng nhauuu!」"
"1736" = "「Fua a! A! Aaaa!!!!!!」"
"1737" = "「Fua! A! Anh hai! Anh hai!!!!\\nHôm nay! Tuyệt quá── em── cảm nhận được!」"
"1739" = "「Fua! A!! A── aaaa!!!!」"
"1773" = "「Hà── a── phu── Fua──」"
"1820" = "「Fan!!」"
"1857" = "「Ưm kyu! Fua! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」"
"1928" = "「Vâng ạ! Đúng vậy── ưm── chị Hibi, ki──\\nFua── Mikuro cũng, làm tình── làm tình, làm tình」"
"1967" = "「Muốn nhìn── ạ── ưm hưu── Fua── a,\\nMuốn nhìn, nhưng mà── Mikuro── sao thế này, Mikuro」"
"2107" = "「Miku, ro── nhìn đi── a── Fua──\\nCái này── làm tình── của chị, và, anh hai」"
"2198" = "「Sướng! Lắm ạ── rất── hự── Fua!\\nMiku, ro── cái này── thích lắmmm」"
```

#### れいなh1_おかあさんのレッスン.txt.toml

```toml
[script]
"1284" = "「Fa……a……tuyệt quá……tuyệt quá……ạ~」"
"1344" = "「Nhyu! Fuaa——a——hi, ưm——\\nChỗ đó——Reina——Fu, a——bị cọ xát, thế này——」"
"1350" = "「A……Fa――a.」"
"1529" = "「Fa……a――đang……nuốt……ưm――phù.」"
"1532" = "「Fa……a——a!?」"
"1533" = "「Fua——a! A! Aa」"
"1535" = "「Ha……đau……quá……ưm——Fa……\\nReina……đang làm tình……với anh Soutetsu……rồi」"
```

#### ポーレット03_大きなにもつのおばあさん.txt.toml

```toml
[script]
"1583" = "「Phà…… a~Ư」"
"1588" = "「Phùa—— a~! Ư~, kéo dãn hơi quá rồi!\\nÀ nhưng mà…… ừm. Cảm giác máu lưu thông tốt hơn hẳn~」"
"1590" = "「Phùa~Ư」"
```

#### ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml

```toml
[script]
"852" = "「Hyaun!」 Fua——anh Soutetsu——!\\nƯm ư ư ư!!!」"
"864" = "「Hya!? Tuột ra——ưm! Nóng, quá! Fua!」"
"891" = "「Faaaaaaaaa—Aaaaaaaa!!!」"
"895" = "「Fua! A! A! A! Anh Soutetsu! A——tử cung! Nữa đi! Đâm vào, nữa đi!」"
"1015" = "「Lưỡi——ưm! Fu, a——vào rồi——trơn tuột! Cô bé, của em——bên trong âm đạo, bị húp trọn, ưm ư ư!!」"
"1050" = "「Dương, vật——Fu, a——nhé?——Bình tĩnh lại nào——ưm——ngoan, ngoan——rồi——tiến vào ga, nhé——được không?」"
```

#### 凪ふかみ03_みかんの旅.txt.toml

```toml
[script]
"2203" = "「Phàa」"
```

#### 日々姫07_たったひとりの宣戦布告.txt.toml

```toml
[script]
"1727" = "「Phùa!?」"
```

#### 日々姫09_静かなる開戦.txt.toml

```toml
[script]
"1579" = "「Phà~, sống lại rồi~~Ư」"
```

#### 日々姫h1_マッサージの続き.txt.toml

```toml
[script]
"1013" = "「Hơ——Hi——Ưm——Fua——A——」"
"1017" = "「Fua——A——Ưm——Anh hai——Anh hai.」"
"1018" = "「Fa... a——anh hai.」"
"1059" = "「Ưm——Fua——Ya——Sướng quá——Ưm——Anh hai——Cậu, nhỏ——Bên trong——Đang phình, ra.」"
```

#### lr_れいなh1_レディ・れいな.txt.toml

```toml
[script]
"1204" = "「Fua——a——a——a——\\nReina——ưm——bên trong, lấp đầy rồi——Fa」"
```

#### lr_ハチロクh1_今ひとたびの契り.txt.toml

```toml
[script]
"1153" = "「Fu——a——.\\nƯm…… fa…… u——ưm………… a!」"
"1158" = "「Fuya!!? Ng-ngón tay——\\nNgón tay của ngài Soutetsu——ưm——fa.」"
"1159" = "「Fa, a, a, a.」"
"1171" = "「Fa——a——a——a——」"
"1173" = "「Fa——a——a——Ưm ư!!!?」"
"1178" = "「Fa——a——n——kyufu——a——fu——\\nSou, tetsu, sama——Sou, tetsu, sama~」"
"1198" = "「Fa! Ưm ư——」"
"1237" = "「A…… ya——Fu, a——\\nXấu hổ——em xấu hổ lắm ạ.」"
"1252" = "「Ưm…… chụt——ưm…… Fu…… a……\\nFu——chumu——chuu——reru」"
```

#### lr_ポーレットh1_家族旅行の最終日の夜.txt.toml

```toml
[script]
"1023" = "「Fua――a! A! A! Hà! A――ưm――Khự――a!」"
```

#### lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

```toml
[script]
"1353" = "「Fa――a――a――a――!」"
"1354" = "「Fa――a――a――a――」"
"1355" = "「Fa――a――Ư――a――a!!」"
"1356" = "「Fa――a――nkyu! Ư! Anh hai!\\nĐợi! Đã――em――em, em――sắp!」"
"1357" = "「Faaaaaaaaaaaaaaaaaan!」"
"1358" = "「Fafyuuuuuuuuuuuuuunn!!」"
"1367" = "「Fa?! A――a――a」"
"1479" = "「Ưm…… a――a――hư――a――ưm――\\nChụt――chùn chụt――ưm…… hư――fa――a」"
```

#### lr_日々姫真闇h1_三人家族.txt.toml

```toml
[script]
"1471" = "「Fuya!? Ya! Fu――a――aa!!\\nChị hai――em――thế này――Fu, a――giỏi, quá.」"
"1476" = "「Fa――a…… Sou-chan――của Sou-chan……\\n（Ực）――nóng, thế này――cứng ngắc, thế này.」"
"1477" = "「Faaaaaaaaaaaaaaaaaaa!!!!」"
"1479" = "「Faaaaaaaaaaaaaa!!!!?」"
"1481" = "「Fan!? Chị, chị hai.」"
"1634" = "「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\\n――a――ngón tay――lún vào――rồi bám chặt, lấy――fa.」"
```

#### lr_真闇h1_僕のおねえちゃん.txt.toml

```toml
[script]
"1428" = "「Fa……a! Ưm——ưm~~~~!!」"
"1429" = "「Fa! A——a——a……aa……」"
"1430" = "「Fa!」"
"1431" = "「Fa!!」"
"1436" = "「Ực, ực——đang, nuốt——tinh trùng——tinh dịch——\\ncủa, Sou-chan——Fu, a——vui——vui, quá」"
```

#### lr_稀咲h1_おしおきとごほうび.txt.toml

```toml
[script]
"1008" = "「Fa……a……a……a――……」"
```

#### lrれいな追加h_夜の花嫁修業.txt.toml

```toml
[script]
"736" = "「……Ưm……ưm——\\nFa……a——ưm——ưm ưm」"
"1061" = "「Fa……a……\\nNụ hôn. Ngọt ngào quá——thích lắm luôn nha~」"
"1073" = "「Fa——ngực——ưm——Fu, trơn, trơn——\\nReina, nhũ hoa——nhũ hoa——nhiều, thế này——」"
"1074" = "「Fa」"
"1076" = "「Faaaa——ngực,\\nReina, ngực tan chảy mất thôi nha~」"
```

#### lr真闇追加h_赤ちゃん、欲しか.txt.toml

```toml
[script]
"1100" = "\"「Faaaaaaaaaaaaaaaaan!!!」\""
"1106" = "\"「Fa!!——A! A——ưm——Fu, a——\\nSou, chan——ưm——âm, vật, của, chị.」\""
```

#### lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml

```toml
[script]
"2346" = "「Fa——ah——ah——ah」"
"2457" = "「Fa——ah——sướng——sướng quá! Phù——ah,\\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」"
"2458" = "「Fuaaaaa!!!!」"
```

#### れいなh3_おもらし自由化大作戦.txt.toml

```toml
[script]
"1115" = "「Nfufu~ ho re fa ra, e hi fa, he hi ho re fuu」"
```

#### グランドリライト05_れいな.txt.toml

```toml
[script]
"1922" = "「Ehehe~. Reina, giúp ích được cho anh……\\nfa……vui lắm……ạ~」"
```

#### グランドリライト08_ふかみ.txt.toml

```toml
[script]
"1823" = "「Fuga!? Nnyu!? Ưm――Fa!\\nPuhaa!!?」"
```

#### ハチロクh1_契り.txt.toml

```toml
[script]
"1271" = "「Fa! Ư……A――Phong ấn đã được giải trừ, và,\\ncái lỗ……đã có thể, sử dụng được.」"
```

#### ハチロクh7_レトロモダンメイクラヴ.txt.toml

```toml
[script]
"485" = "「Hà……a……Ku……hà——Fu……a——bàn tay, của……\\nphu, quân……ưm……đang banh……mông, ra——」"
"694" = "「Không, muốn đâu——ưm……Fu, a——phu, quân\\n——a! Bằng ngón, tay——nhưng mà——lên đỉnh——một mình, thì.」"
"763" = "「Hiu!? Fu——a!? Ng, Ngài Soutetsu!\\nĐợi——đợi——đợi đã——! ~~~~ƯƯ!!!」"
"791" = "「A……ưm……chụt——chụm——ưm——\\nFu——a……liếm——mút——chụt——chụt」"
"802" = "「A kiu! Ưm! Hà——sướng quá! Fu, a——\\nvú, cũng——cô, bé——rồi!!!!」"
"816" = "「Ưm——a……Ngài……Soutetsu……Fu——a——ưm,\\nKhông sao……đâu……ạ? Ngoan nào……nhé? Ngoan nào……」"
"819" = "「Ưm……kiu——Faaaaan!!!」"
"821" = "「Ưm……Fu——a——chiếc lưỡi——của phu, quân……trơn,\\ntrơn……ướt……làm ướt, làn da của em——bằng, nước bọt.」"
"837" = "「Nhyu!! Fu——a! A! A!!」"
"853" = "「Phu……quân——Fu, a——ngực, của——\\nSuzu——núm vú, bị——kéo dài, ra——ưm!」"
"968" = "「Ngài, Soutetsu! Fu——a! Phu, quân!\\nNgười——mà——em, vô cùng——yêu, thương!」"
```

#### ハチロクh8_桜色のひめごと.txt.toml

```toml
[script]
"703" = "「Kyafu!? A! Tiểu huyệt——ưm!!\\nEm——tiểu huyệt——của em——Fa」"
"708" = "「Hya! A!? Bị mút rồi——hạt đậu... Fa!\\nTiểu huyệt——a……tiếng——chóp chép——xấu hổ, quá——ưm」"
"724" = "「Ho he phu ha fa——ưm……ho ho,\\nwa ra phu hi hi……ha fa fa e, ho——」"
"743" = "「Hia!? Không chịu đâu——cố tình——Fu, a——\\nƯm——cố tình, tạo ra âm thanh——dâm đãng, như vậy——khục!」"
"746" = "「Iun!? A——Hút, hút mất rồi——hi——kyu! Fa\\n——Nước, tiểu——tất cả——cả phần còn lại——cũng bị hút ra, hết」"
"751" = "「Ha——a mu——chụt——chu muu——ưm……\\nyêu, ngài——ho he phu……ha fa, yêu, yêu ngài lắm」"
"754" = "「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\\nchu——chụt——ho he phu……ưm——ha faa」"
"759" = "「A——ra rồi——ưm——nóng, quá——ưn ku——phù——\\nTinh trùng——của Ngài Soutetsu——nóng, quá——phù, fa」"
"762" = "「A——ha——hi——thích quá! Sướng——Fu, a\\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」"
"812" = "「Fa……a…………đầy, ắp, rượu ngọt——Cái miệng,\\nở trên……cái miệng, ở……dưới, cũng——fa」"
"813" = "「Fa……aa——————a……Tất cả……toàn, bộ\\n——Em——tất cả——vào miệng, của——phu quân」"
"857" = "「Tiểu huyệt——Fa——ngập——ngập, rồi\\n——Ưm! Tinh trùng——của Ngài Soutetsu, đầy ăm ắp」"
"946" = "「Ngài Soutetsu——Fa——Ngài Soutetsu!」"
```

#### ポーレット02_解放b寝台.txt.toml

```toml
[script]
"1795" = "「Vâng. Em cũng sẽ hỗ trợ…… fa.」"
```

#### ポーレットh2_制服変更？.txt.toml

```toml
[script]
"962" = "「Faaaaaaaan!」"
```

#### ポーレットh3_誘惑アイスコーヒー.txt.toml

```toml
[script]
"915" = "「Fa——a——hàà——a——」"
```

#### ポーレットh8_気動車の国のアリス.txt.toml

```toml
[script]
"2049" = "「Không chịu đâu!? Lại, lên đỉnh, một mình——nữa——ưm, Fa,\\nsướng, lắm nhưng mà——nhưng mà——không chịu, đâu!!」"
"2129" = "「Á——lạ, lắm——chỗ đó——Fu, a——\\ncái, gì đó——ư——a, run rẩy, Fu, a——」"
"2161" = "「Hà……ưm……chụt——chụt——chụt——Fu, a——thích quá——Anh Soutetsu, ơi——ưm, ưm, chụt」"
"2167" = "「Fa……hà——Anh Soutetsu……（sụt sịt, sụt sịt）\\nA……bằng Anh Soutetsu——em——tràn ngập——」"
"2212" = "「A——hà——ưm——phù, Fa——hà, a.\\nEm——âm đạo——đang ôm, chặt lấy——ưm, Fa」"
"2224" = "「A——ưm……chụt——Fu——a——chụt——chụt——chụt——chụt——」"
```

#### 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml

```toml
[script]
"1944" = "「Không được――Tử, tử cung! Fu, a!\\nBây giờ, ngay bây giờ――không được, đâu――nó siết chặt, quá」"
"2106" = "「Fu……a――a――Anh, hai――chật quá, ưm」"
"2114" = "「Faaaaaa――aa――Chỗ đó, em thích, lắm\\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」"
"2194" = "「A……ưm――Fu, a」"
"2255" = "「V-Vâng. Em làm được. Em sẽ làm. Ư……Fu……a\\nQuy đầu……phần đầu, chim của anh hai」"
"2297" = "「Pua! A! A――Fu, a――a――\\nHà――a……Fua――a――」"
"2713" = "「Anh, hai――ưm――kuuuu~~n――Fu, a\\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」"
```

#### 真闇h3_補習授業の廃校舎.txt.toml

```toml
[script]
"2308" = "「Ua……nhớt, nhớp nháp――ưm――（khịt, khịt）\\nFa……mùi của Sou-chan……mùi đàn ông……mùi của một con người.」"
```

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml

```toml
[script]
"2170" = "「Ư~~~――Fa, á――vú――ưm,\\nphù――Fua――ưm――phù――phù」"
"2188" = "「Phù――hà――ưm――Fa――ưm――\\n~~Ư! Hà――Fa――ưm……ưm phu――」"
"2203" = "「Ha…… ưm――Fu, a…… tay…… tay của, anh Soutetsu――\\nấm quá――fu…… ha…… ha fu」"
"2238" = "「A mu――ưm――fa…… ưm――chu mu\\nAnh Houhefu――fu――hích anh――ưm――chụt」"
"2265" = "「Ưm…… fu――ưm――chụt――chu mu――\\nchu ru――chụt――ưm chu――Fu…… a――」"
```

#### lr_凪h1_痛いの痛いの飛んでけばい.txt.toml

```toml
[script]
"1128" = "「Hyau! A——fua! A! Cô bé!\\nTử cung——nóng quá——ngực cũng——Fu, a」"
```

#### lr_凪h2_虎さんの交尾.txt.toml

```toml
[script]
"1239" = "「A……Fu, a——anh Soutetsu……môi——ưm——cả hơi thở,\\ncũng nhột quá——sướng, lắm, nôn nao quá」"
```

#### lr_日々姫h1_鏡の中日々姫.txt.toml

```toml
[script]
"1160" = "「Tại vì——Fu, a——Hi-chan——từ lúc, còn nhỏ——\\nđã cố gắng——cố gắng, rất nhiều——mà.」"
```

#### lr_日々姫h2_デザートは食事の前に.txt.toml

```toml
[script]
"1045" = "「Chuuuuuuu! Ưm…… ực——Fu, a\\n——liếm——rerooo——chụt——chuuu」"
```

#### ふかみh1_ともはり練習.txt.toml

```toml
[script]
"987" = "「Fa——ah——của em——âm đạo——\\nMiệng của——anh Soutetsu——bằng miệng——」"
"992" = "「Fu, ah——lưỡi……ấm……quá……ưm.」"
"1039" = "「Thích……thích……Anh Soutetsu, đối với em——\\nĐã thích em rồi, sao……Fu, ah.」"
```

#### ふかみh2_homesweethome.txt.toml

```toml
[script]
"1034" = "「Ưm……Fu, ah——ưm——fahi……ưm ư——ưm,\\nHo he fu……fan……ư ku——ưm!」"
```

#### ハチロク12_ムナカタ来訪.txt.toml

```toml
[script]
"1665" = "「Phùa!」"
```

#### ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml

```toml
[script]
"965" = "「A……Fu……a……nóng quá……\\ntinh dịch……của……ngài Soutetsu……phù——a——」"
```

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml

```toml
[script]
"532" = "「……Ưm……chụt——chụm——chụt……Fu, a\\n……phu, quân——ngài Soutetsu.」"
"816" = "「Ya……giọng nói đó của ngài……Fu, a……em……\nnúm, vú……ưm——xấu hổ quá……ạ.」"
"847" = "「Hà——chụm——ưm——chụt——Fu, a——\nưm, mút——Hyua——liếm——ưm, Ku——a!」"
"906" = "「Ưm……Fu……a……ngài Soutetsu……ưm……\\nnúm, vú……cảm giác……bứt rứt quá……ạ.」"
"1045" = "「Thật là một……ưm——quang cảnh……dâm đãng……ưm, Fu, a\\n……hơn nữa……núm vú, cũng, có……cảm giác……kỳ, lạ.」"
"1050" = "「Làm, như thế……thì——a——em,\\nưm……Fu——a——vú……vú!」"
```

#### ポーレット10_見えない傷.txt.toml

```toml
[script]
"1319" = "「Phà……A——No quá đi mất.\\nThật sự rất ngon luôn——Cảm ơn vì bữa ăn.」"
```

#### ポーレットh6_あなたとふたりの学園エッチ.txt.toml

```toml
[script]
"790" = "「Fu, a!——A! Ngực——chỗ đó—— Đầu vú——núm, vú——Ư!」"
```

#### 凪h1_ふたりっきりのデート.txt.toml

```toml
[script]
"1102" = "「A……A——Lúc nãy——á——Ưm——Fu, a,\\nEm, vừa nãy……chỉ vì giọng nói của anh hai……mà lên đỉnh mất rồi, á」"
"1106" = "「Hà……Ư……Sướng, quá……Ưm——Bàn tay,\\ncủa anh hai……Làm ngực em……Nhũn cả ra……rồi——Fu——A」"
```

#### 日々姫h2_洗って大丈夫なスーツ.txt.toml

```toml
[script]
"1076" = "「Fua... a... Ưm... Vui quá... Vừa khít——Cô bé, của em——với của, anh hai.」"
```

#### 日々姫h5_白濁絵の具の射精会.txt.toml

```toml
[script]
"928" = "「……Fu……a――Chưa xong, đâu? Anh hai――,\\nưm……Vừa rồi――chỉ là――lớp sơn lót――thôi mà……」"
"1129" = "「Không cần……phải nhịn, đâu? Fu……a――\\nGiọng nói, của anh hai, ưm――Em, muốn được nghe nhiều hơn nữa, cơ」"
"1190" = "「Fua……a……a……ưm……hự――a――\\nHà――hà――hà……Fu, a――a」"
"1191" = "「Fu……a……ưm――anh――hai~」"
"1192" = "「Fu……a……Như bị――khoét sâu, vậy……a――\\nHà――Độ nóng――của anh hai――cảm nhận……rất rõ」"
```

## Kết bài

Batch U11a xong: **166 dòng (M1 37 · M16 67 · M17 62), 47 file**. M16 và M17 đã QUYẾT trong đợt này theo uỷ quyền (strict Fa/Fua; split romaji "Fu"+dấu+"a" cho H-scene, giữ split VN cho non-H). Lượt soát 2: 166/166 tái kiểm chứng, 0 loại, 0 sửa. 0 trùng batch đã gộp; 11 dòng trùng enumeration U12a đã cờ cho coordinator gộp; 16 dòng ふや (M11), các dòng ふぇ/ふえ (M10) và ふっ (M9) để U12a; 3 split ぷ để T79; 1 split ふう (凪ふかみh2 1271) chờ coordinator quyết.
