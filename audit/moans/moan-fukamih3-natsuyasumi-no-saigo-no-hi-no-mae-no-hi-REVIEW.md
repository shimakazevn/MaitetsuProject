# Moan-fix REVIEW — ふかみh3_夏休みの最後の日の、前の日.txt.toml (moan-fukamih3-natsuyasumi-no-saigo-no-hi-no-mae-no-hi)

File H-scene Fukami — buổi hẹn hò Soutetsu–Fukami ngày trước ngày cuối kỳ nghỉ hè (dọc tuyến đường sắt, nhà ga bỏ hoang, mưa rào, cảnh H). Chỉ sửa TIẾNG RÊN / thở / gasp / SFX theo quy tắc romaji (Hieu duyệt 21/11 ~01:56) + quy tắc 3b (ひゃ/ひゅ/ひあ/きゃ → romaji, chốt 21/11 ~11:55). Không sửa đại từ, thuật ngữ, nghĩa, lệch dòng — những thứ đó thuộc audit / đợt thống nhất.

## §1. Xác minh file

- TOML: `sources/toml2/translation_toml/07_Nagi_Fukami/#U3075#U304b#U307fh3_#U590f#U4f11#U307f#U306e#U6700#U5f8c#U306e#U65e5#U306e#U3001#U524d#U306e#U65e5.txt.toml` — BOM + CRLF, md5 `468ff9287da913deb380278b68d048f8` (khớp md5 audit), 649 key script, 0 key trùng, không có bản trùng (md5 không nằm trong 11 nhóm trùng của dự án).
- CSV3: 2 set × 649 — chỉ dùng set tốt `translation_toml\11_Other\...` (khớp TOML 649/649 sau chuẩn hoá `\n`→khoảng trắng; TOML-2 làm phẳng `\n` thành khoảng trắng ở 366/649 dòng, 283 dòng khớp tuyệt đối). Set home-folder `07_Nagi_Fukami` là STALE (chỉ 7/649 khớp, JP xoay) — không dùng.
- Audit của file đã merge: 28/649 sai (ROUTE-AUDIT.md §ふかみh3) — 20 fa/fu + 4 gasp + 3 sai nghĩa + 1 bịa. Bản moan này xây trên audit: 21/44 dòng kế thừa/lật fix audit (20 fa/fu + 2292), 23 dòng mới.
- Đã đọc 649/649 dòng (CSV3 set tốt + TOML). Lọc máy 328 dòng ứng viên (JP chứa âm rên/SFX/gasp hoặc VN chứa cách diễn rên) đã đọc kỹ từng dòng; quét bổ sung: mọi dòng JP kết thúc bằng っ, mọi dòng họ fa/fu, họ ひゃ, họ や, mọi chuỗi nguyên âm dài, mọi dòng （ ） (40 dòng) — không còn dòng rên nào ngoài 328 ứng viên.

## §2. Kiểm kê rên

- 328 dòng ứng viên đã xét; **sửa 44, giữ 284**.
- Phân loại 44 dòng sửa: romaji 31 + romaji + đếm nguyên âm 3 (2278, 2287, 2402) + đếm nguyên âm 5 (2289, 2379, 2427, 2428, 3911) + gasp 4 (2202, 2596, 3208, 3435) + romaji + gasp 1 (2352).
- Romaji họ fa/fu → Fa/Fua/Pua (21 dòng, 24 token — xem §3A): 20 dòng audit đã sửa "phù"→"phà"/"phùa" nay chuyển sang romaji theo quy tắc duyệt 21/11, + 2384 (ふ、ぁ, audit không cờ).
- Romaji mất phụ âm mora (14 dòng — xem §3B): ひあ→"Hia" (2273, 2280, 2283 — bản cũ "Hya" sai âm, tiền lệ 凪h2 sửa "Hya"→"Hia" ×5); きゃ→"Kya" (2275, 2276, 2422); や→"Ya" (2281, 2292, 2876); ひゅあ→"Hyua" (2278); ひう→"Hiu" (2293); ふわ→"Fuwa" (2309); くっ→"Ku" (2349); あむ→"Amu" (2409); やぁん→"Yaan" (2784).
- Đếm nguyên âm (8 dòng có yếu tố đếm — xem §3A/§3C): 2278 んううう 3→4 nhịp; 2287 ふきゅうううんんっ 6u/1n→5u/2n; 2289 きゅふあ×14んんっ 15a/1n→14a/2n; 2379 はああああああ 8a→7a; 2402 はぁあああ 4a→5a; 2427 はぅぅ 2→3 nguyên âm; 2428 んうぅっ 2→3 nhịp; 3911 （ああ――） 1a→2a.
- Gasp っ cuối dòng bị mất (5 dòng — xem §3D): 2202, 2352, 2596, 3208, 3435 — cùng mẫu 2728 mà audit đã sửa (――っ → ——Ư); sweep + audit đều bỏ sót 5 dòng này.

## §3. Các dòng sửa (44)

### §3A. Romaji họ fa/fu (21 dòng)

Quy tắc chung: "phà"/"phùa" nghe gượng trong rên → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ ふかみh1/h2, ポーレットh5 — fa/fu chuyển hết sang Fa/Fua/Pua). Audit sửa 20 dòng này từ "phù" (mất âm a) thành "phà"/"phùa" TRƯỚC quy tắc romaji; bản moan này thay thế bằng romaji. `old_vn` trong JSON là VN gốc CSV3 ("phù"); giá trị fix là giá trị cuối cùng (romaji).

### 2278 — ふかみ — romaji + đếm nguyên âm (3 chỗ)
- JP: 「ひゅあっ！　あっ――ふあっ！　これ――しゅご、\nんううう――おく――ゆっくり――おされ、る、のっ」
- TW: 「呀！啊……啊！這個好棒……嗚……裡面被……慢慢地推……」
- Cũ: 「Hya! A—— phù! Cái này—— tuyệt,\nƯm ư ư—— bên trong—— từ từ—— bị, đẩy, vào」
- Mới: 「Hyua! A—— Fua! Cái này—— tuyệt,\nƯm ư ư ư—— bên trong—— từ từ—— bị, đẩy, vào」
- Lý do: ひゅあっ là một âm duy nhất → "Hyua" (tiền lệ ふかみh1 974; bản cũ "Hya" làm mất âm u); ふあっ → "Fua"; んううう = 4 nhịp (ん + 3 う) nhưng bản cũ chỉ có 3 token "Ưm ư ư" — thêm 1 "ư" (tiền lệ ポーレットh5 849 んううっ→"ưm ư ư", một token một mora).

### 2287 — ふかみ — romaji + đếm nguyên âm (2 chỗ)
- JP: 「ふきゅうううんんっ！！　ふあっ――おく――\nいちば――んっ――子宮――こちゅん、ってっ――」
- TW: 「呀！！哇……裡面……最深處……嗯……子宮……被摩擦了一下」
- Cũ: 「Fukyuuuuun!! Phù—— bên trong——\nSâu, nhất—— tử cung—— bị, chạm vào, rồi——」
- Mới: 「Fukyuuuunn!! Fua—— bên trong——\nSâu, nhất—— tử cung—— bị, chạm vào, rồi——」
- Lý do: ふきゅうううんんっ = ふ(1u) + きゅ(1u) + ううう(3u) = 5u, んん = 2n; bản cũ "Fukyuuuuun" có 6u/1n — thừa 1u, thiếu 1n. Đếm n: một ん = một n (tiền lệ lr_ふかみh1 くふぅんんんん→"Kufuunnnn", lr_れいな追加h 1170 ふひゅんんんんっ→"Fuhyunnnn", đều đếm máy). ふあっ → "Fua".

### 2301 — ふかみ — romaji
- JP: 「ふっ――んっ――じんじん、ってして――ふぁ――\nはっ――ふ、ぅっ――んっ……じれ、たく、って」
- TW: 「呼……嗯……像過電一樣……啊……啊……呼……嗯……好難過……」
- Cũ: 「Phù—— ưm—— tê tê, rần rần—— phù——\nHà—— phù, ư—— ưm…… bứt, rứt, quá」
- Mới: 「Phù—— ưm—— tê tê, rần rần—— Fa——\nHà—— phù, ư—— ưm…… bứt, rứt, quá」
- Lý do: ふぁ → "Fa" (audit "phà"). Giữ "Phù" cho ふっ (hơi thở) và "phù, ư" cho ふ、ぅ (tách đúng, nguyên âm đúng — xem §4).

### 2302 — ふかみ — romaji
- JP: 「んくッ――んくっ――んくっ――ぷあぁ」
- TW: 「咕咚……咕咚……咕咚……哈」
- Cũ: 「Ực—— ực—— ực—— phù」
- Mới: 「Ực—— ực—— ực—— Puaa」
- Lý do: ぷあぁ = ぷ + あ + ぁ = 2 âm a → "Puaa" (audit "phùa" chỉ có 1 a). Giữ "Ực/ực" cho 3 tiếng nuốt んくっ (diễn theo TW 咕咚, đúng).

### 2338 — ふかみ — romaji
- JP: 「ぁっ……ふあっ――んっ――ちゅっ――ちゅむっ、\nちゅっ――ちゅうっ――ちゅるっ――ちゅずっ」
- TW: 「啊……哇……嗯……啾……啾，啾……啾……啾……啾」
- Cũ: 「A…… phù—— ưm—— chụt—— chụt,\nchụt—— chụt—— chụt—— chụt」
- Mới: 「A…… Fua—— ưm—— chụt—— chụt,\nchụt—— chụt—— chụt—— chụt」
- Lý do: ふあっ → "Fua" (audit "phùa"). Giữ họ ちゅ → "chụt" (đúng, xem §4).

### 2345 — ふかみ — romaji
- JP: 「ふぁ……は……ぁっ――」
- TW: 「啊……啊……啊……」
- Cũ: 「Phù…… hà…… a——」
- Mới: 「Fa…… hà…… a——」
- Lý do: ふぁ → "Fa" (audit "phà").

### 2346 — ふかみ — romaji
- JP: 「ふあっ――あっ――はっ――はあっ――いっぱい、\nおな、か――いっぱい――たぷ――たぷっ」
- TW: 「啊……啊……啊……啊……好多，肚子裡……好多，滿滿的」
- Cũ: 「Phù—— a—— hà—— hà—— ngập tràn,\nBụng—— ngập tràn—— óc ách—— óc ách」
- Mới: 「Fua—— a—— hà—— hà—— ngập tràn,\nBụng—— ngập tràn—— óc ách—— óc ách」
- Lý do: ふあっ → "Fua" (audit "phùa").

### 2351 — ふかみ — romaji (2 token)
- JP: 「ふあっ――あっ――んっ――ちゅ――ぷあっ！\nあ――ほしい、です――全部、双鉄、おにいさん」
- TW: 「啊……啊……嗯……啾……哇！啊……想要……我全都想要，雙鐵哥哥」
- Cũ: 「Phù—— a—— ưm—— chụt—— phù!\nA—— em muốn, ạ—— toàn bộ, anh, Soutetsu」
- Mới: 「Fua—— a—— ưm—— chụt—— Pua!\nA—— em muốn, ạ—— toàn bộ, anh, Soutetsu」
- Lý do: ふあっ → "Fua", ぷあっ → "Pua" (phân biệt ぷ/ふ; audit "phùa" cả hai).

### 2352 — ふかみ — romaji + gasp (2 chỗ)
- JP: 「ふあっ――あっ――おっき――おっき、いっ――\nおちん、ちんっ――そこ――ふとい――とこっ――っ」
- TW: 「啊……啊……好大，好大……雞巴……好肥……」
- Cũ: 「Phù—— a—— to—— to, quá——\nChim—— chỗ đó—— chỗ, thô to——」
- Mới: 「Fua—— a—— to—— to, quá——\nChim—— chỗ đó—— chỗ, thô to——Ư」
- Lý do: ふあっ → "Fua" (audit "phùa"); っ trần cuối dòng sau ―― bị mất hẳn → thêm "Ư" (cùng mẫu gasp 1677 「……っ」→「……Ư」 mà audit đã sửa).

### 2358 — ふかみ — romaji (2 token)
- JP: 「ふぁっ――あ――おっぱい、ちく、びっ――んっ、\nもっと――もっと、つよくても、へい、き――ふぁっ」
- TW: 「啊……啊……胸部，乳頭……嗯……可以……可以再強烈一點的……啊」
- Cũ: 「Phù—— a—— ngực, núm, vú—— ưm,\nMạnh—— mạnh hơn, chút nữa, cũng không, sao—— phù」
- Mới: 「Fa—— a—— ngực, núm, vú—— ưm,\nMạnh—— mạnh hơn, chút nữa, cũng không, sao—— Fa」
- Lý do: ふぁっ ×2 → "Fa" (audit "phà" ×2).

### 2359 — ふかみ — romaji (2 token; sửa cả lỗi audit)
- JP: 「はっ――あっ――中ッ――っっ――あっ、ふあっ、\n指っ――ん、っ――うっ――こすって――ふ、あ」
- TW: 「啊……啊……裡面……嗯……啊，啊……手指……嗯……嗚……摩擦著……啊」
- Cũ: 「Hà—— a—— bên trong—— a, phù,\nNgón tay—— ưm, ư—— ư—— cọ xát—— phù, a」
- Mới: 「Hà—— a—— bên trong—— a, Fua,\nNgón tay—— ưm, ư—— ư—— cọ xát—— Fu, a」
- Lý do: ふあっ → "Fua" (audit "phùa"). Token thứ hai ふ、あ: audit sửa "phù, a"→"phà, a" là SAI — ふ tách riêng có nguyên âm u ("phù"/"Fu"), "phà" gán cho ふ nguyên âm a là sai âm; dạng tách phải giữ ngắt: "Fu, a" (tiền lệ lr_ふかみh2 1179 ふ……ぁ……→"Fu……a……"). Bản moan này sửa luôn lỗi audit đó.

### 2362 — ふかみ — romaji
- JP: 「ふあっ――あっ――ひ、ぅっ――おまんこ、の――\nうえっ――んっ――ひっかく――みたい、でっ――」
- TW: 「啊……啊，呀……下面……的裡頭……嗯……就像在撓一樣……」
- Cũ: 「Phù—— a—— hi, ư—— phần trên——\nCủa, cô bé—— ưm—— giống như, đang cào—— vậy——」
- Mới: 「Fua—— a—— hi, ư—— phần trên——\nCủa, cô bé—— ưm—— giống như, đang cào—— vậy——」
- Lý do: ふあっ → "Fua" (audit "phùa"). Giữ "hi, ư" cho ひ、ぅっ (tách đúng, xem §4).

### 2371 — ふかみ — romaji (sửa cả lỗi audit)
- JP: 「あ……ここ、です――ふ……ァッ――\nそうてつ、おにいさん、の――おちん、ちんっ」
- TW: 「啊……就是這個，嗯……呼……啊……雙鐵哥哥的雞巴」
- Cũ: 「A…… chỗ này, ạ—— phù…… a——\nChim, của—— anh, Soutetsu」
- Mới: 「A…… chỗ này, ạ—— Fu……a——\nChim, của—— anh, Soutetsu」
- Lý do: như 2359 — audit sửa "phù…… a"→"phà…… a" là sai nguyên âm của ふ tách riêng; giữ ngắt …… bằng romaji "Fu……a" (tiền lệ lr_ふかみh2 1179).

### 2384 — ふかみ — romaji
- JP: 「あう、んっ――ちく、びっ――んっ――先、から\n――ふ、ぁ――おっぱい――にゅる、って」
- TW: 「啊嗚，嗯……乳頭……嗯……剛才……啊……胸部……就被抹上了」
- Cũ: 「A ư, ưm—— núm, vú—— ưm—— từ, đầu\n——phù, a—— ngực—— trơn, tuột」
- Mới: 「A ư, ưm—— núm, vú—— ưm—— từ, đầu\n——Fu, a—— ngực—— trơn, tuột」
- Lý do: ふ、ぁ là một âm ふぁ tách bởi dấu phẩy — bản cũ "phù, a" gán cho ふ nguyên âm u (sai: ふぁ có nguyên âm a; "phù" là ふぅ). Romaji giữ ngắt: "Fu, a" (tiền lệ ふかみh1 1049 ふあっ→"Fua"; lr_ふかみh1 1502 ふ……ぁ→"Fu……a"). Audit không cờ dòng này.

### 2385 — ふかみ — romaji
- JP: 「っ！　――ぷあっ」
- TW: 「啊！……呼」
- Cũ: 「Ư! ——Phù」
- Mới: 「Ư! ——Pua」
- Lý do: ぷあっ → "Pua" (audit "phùa"). Giữ "Ư!" cho っ đầu dòng (gasp của audit, đúng).

### 2388 — ふかみ — romaji
- JP: 「ふあっ！　あっ――あついの――おくっ――おくっ！\nおまんこのっ――おくっ――びゅって、たたい、て」
- TW: 「啊！啊……燙燙的……進來了裡面……裡面！在裡面……咻咻地……打在上面」
- Cũ: 「Phù! A—— nóng quá—— bên trong—— bên trong!\nBên trong—— cô bé—— phụt ra, đánh vào」
- Mới: 「Fua! A—— nóng quá—— bên trong—— bên trong!\nBên trong—— cô bé—— phụt ra, đánh vào」
- Lý do: ふあっ → "Fua" (audit "phùa").

### 2394 — ふかみ — romaji
- JP: 「はっ！　しゅきっ――うれしっ――いっ――ふあっ、\nこのまま――この、ままっ――わたしっ――このまま」
- TW: 「啊！喜歡……好開心，舒服……啊，就這樣，就這樣，我……就這樣」
- Cũ: 「Hà! Thích—— sướng—— quá—— phù,\nCứ thế này—— cứ, thế này—— em—— cứ thế này」
- Mới: 「Hà! Thích—— sướng—— quá—— Fua,\nCứ thế này—— cứ, thế này—— em—— cứ thế này」
- Lý do: ふあっ → "Fua" (audit "phùa").

### 2402 — ふかみ — romaji + đếm nguyên âm (2 chỗ)
- JP: 「はぁあああっっ、ふっ！　あっ！　しきゅうっ！\nほしっいっ――ふあっ――ごつって――ノックぅっ」
- TW: 「啊，呼！啊！呀！想要……啊……敲打的……」
- Cũ: 「Hà a a a, phù! A! Tử cung!\nMuốn—— phù—— bị cộc—— gõ cửa」
- Mới: 「Hà a a a a, phù! A! Tử cung!\nMuốn—— Fua—— bị cộc—— gõ cửa」
- Lý do: はぁあああ = は(1a) + ぁ(1a) + あああ(3a) = 5 âm a; bản cũ "Hà a a a" chỉ có 4 — thiếu 1 a. ふあっ → "Fua" (audit "phùa"). Giữ "phù!" cho ふっ (hơi thở) và "Tử cung" cho しきゅうっ (từ, diễn nghĩa đúng).

### 2430 — ふかみ — romaji
- JP: 「んっ――ふあっ――」
- TW: 「嗯……啊……」
- Cũ: 「Ưm—— phù——」
- Mới: 「Ưm—— Fua——」
- Lý do: ふあっ → "Fua" (audit "phùa").

### 2577 — ふかみ — romaji
- JP: 「わかる、です。――んっ――双鉄、おにいさん、の\n――かた、ち――ふあっ――おちん、ちん――のっ」
- TW: 「我能感覺到，嗯……嗯……雙鐵哥哥的形狀……啊……雞巴的……」
- Cũ: 「Em biết, ạ. ——Ưm—— hình, dáng——\nCủa, anh, Soutetsu—— phù—— của, chim——」
- Mới: 「Em biết, ạ. ——Ưm—— hình, dáng——\nCủa, anh, Soutetsu—— Fua—— của, chim——」
- Lý do: ふあっ → "Fua" (audit "phùa").

### 2767 — ふかみ — romaji
- JP: 「ふく――とか――そんなの――どうでも、\nいい――ふあっ――んっ――ふっ――はうっ」
- TW: 「衣服……其實……完全無所謂……啊……嗯……呼……啊嗚」
- Cũ: 「Quần áo—— hay gì đó—— sao cũng,\nđược—— phù—— ưm—— phù—— a ư」
- Mới: 「Quần áo—— hay gì đó—— sao cũng,\nđược—— Fua—— ưm—— phù—— a ư」
- Lý do: ふあっ → "Fua" (audit "phùa"). Giữ "phù" cho ふっ và "a ư" cho はうっ (đúng, xem §4).

### §3B. Romaji họ ひゃ/ひゅ/ひあ/きゃ + や/く (14 dòng)

### 2273 — ふかみ — romaji
- JP: 「ひあっ――あっ――おちん、ちん――すごっ――\nそうてつ、おにいさん――あつ、くて――ぶく、って」
- TW: 「呀……啊……雞巴……好棒……雙鐵哥哥……好燙……還膨脹了一下」
- Cũ: 「Hya—— a—— chim—— tuyệt quá——\nAnh, Soutetsu—— nóng, quá—— phình to, ra」
- Mới: 「Hia—— a—— chim—— tuyệt quá——\nAnh, Soutetsu—— nóng, quá—— phình to, ra」
- Lý do: ひあ = hai mora (hi + a) → "Hia", không phải "Hya" (một mora). Tiền lệ: 凪h2 sửa ひあ "Hya"→"Hia" ×5 (quy tắc 3b chốt 21/11).

### 2275 — ふかみ — romaji
- JP: 「きゃっ」
- TW: 「呀」
- Cũ: 「Á」
- Mới: 「Kya」
- Lý do: きゃ → romaji "Kya" (quy tắc 3b); "Á" làm mất phụ âm mora ky- (lỗi mất âm, tiền lệ ポーレットh3).

### 2276 — ふかみ — romaji
- JP: 「きゃっ！」
- TW: 「呀！」
- Cũ: 「Á!」
- Mới: 「Kya!」
- Lý do: như 2275.

### 2280 — ふかみ — romaji
- JP: 「ひあっ！　あっ――はげしっ――はげ、し、いっ、\nばちゅん、ばちゅんって、おまんこ、音、してっ」
- TW: 「呀！啊……好激烈……好激烈，還傳出啾啾的聲音……」
- Cũ: 「Hya! A—— mãnh liệt—— mãnh, liệt, quá,\nBạch, bạch, cô bé, phát ra, tiếng, kêu」
- Mới: 「Hia! A—— mãnh liệt—— mãnh, liệt, quá,\nBạch, bạch, cô bé, phát ra, tiếng, kêu」
- Lý do: ひあっ → "Hia" (như 2273).

### 2281 — ふかみ — romaji
- JP: 「やっ！　あっ！　はげしっ！　はげし、いっ！　ん、\nおな、か――おまん、こ――きゅんきゅん、し、て」
- TW: 「呀！啊！好激烈！好激烈！嗯，肚子裡……下面……都一縮一縮的」
- Cũ: 「Á! A! Mãnh liệt! Mãnh, liệt, quá! Ưm,\nBụng—— cô, bé—— co thắt, liên tục」
- Mới: 「Ya! A! Mãnh liệt! Mãnh, liệt, quá! Ưm,\nBụng—— cô, bé—— co thắt, liên tục」
- Lý do: やっ → "Ya" (tiền lệ ポーレットh5 848/880/913); "Á" làm mất phụ âm y-.

### 2283 — ふかみ — romaji
- JP: 「ひあっ！　あっ！！！！！」
- TW: 「呀！啊！！！！！」
- Cũ: 「Hya! A!!!!!」
- Mới: 「Hia! A!!!!!」
- Lý do: ひあっ → "Hia" (như 2273).

### 2292 — ふかみ — romaji (kế thừa fix audit)
- JP: 「やっ、なにこれっ！？　こんなにひどいとかっ」
- TW: 「呀，怎麼回事？居然這麼大」
- Cũ: 「Á, gì thế này!? Sao lại mưa to thế này chứ」
- Mới: 「Ya, gì thế này!? Sao lại to thế này chứ」
- Lý do: やっ → "Ya" (như 2281). Đồng thời KẾ THỪA fix nghĩa của audit ("mưa to"→"to" — JP không có 雨, TW "居然這麼大"); bản moan này chỉ đổi token rên, không sửa thêm nghĩa.

### 2293 — ふかみ — romaji
- JP: 「ひうっ！！？」
- TW: 「呀？！」
- Cũ: 「Hya!!?」
- Mới: 「Hiu!!?」
- Lý do: ひうっ = hi + u → "Hiu". Bản cũ "Hya" sai hẳn âm (đó là âm của ひゃ, không phải ひう) — lỗi sai âm, không chỉ mất phụ âm.

### 2309 — ふかみ — romaji
- JP: 「ふわっ！！」
- TW: 「哇！！」
- Cũ: 「Oa!!」
- Mới: 「Fuwa!!」
- Lý do: ふわっ = ふ + わ → "Fuwa". Bản cũ "Oa" chỉ diễn わ, làm mất hẳn mora ふ (lỗi mất âm; JP hơn TW — TW 哇 cũng chỉ có わ). Phán đoán mới, lần đầu trong dự án (xem cờ F5).

### 2349 — ふかみ — romaji
- JP: 「はあっ――はあっ――はあっ――ん、くっ――\nあのっ――そこ――でも――なく、てっ――」
- TW: 「啊……啊……啊……嗯，唔……那個……也不是……那裡」
- Cũ: 「Hà—— hà—— hà—— ưm, ư——\nDạ—— chỗ đó—— cũng—— không phải, đâu——」
- Mới: 「Hà—— hà—— hà—— ưm, Ku——\nDạ—— chỗ đó—— cũng—— không phải, đâu——」
- Lý do: くっ trong chuỗi rên → "Ku" (tiền lệ ポーレットh5: くっ→"Ku" ở dòng rên; "Hự" chỉ dùng cho grunt như h5 1003). Bản cũ "ư" làm mất phụ âm k-.

### 2409 — ふかみ — romaji
- JP: 「え？　あ――あむっ――んっ――」
- TW: 「啊？啊……啊唔……嗯」
- Cũ: 「Hả? A—— a ưm—— ưm——」
- Mới: 「Hả? A——Amu——ưm——」
- Lý do: あむっ là MỘT âm duy nhất, bản cũ tách thành 2 mảnh "a ưm" — gộp thành romaji một hơi "Amu" (tiền lệ ふかみh1 973 ひあっ "Hi ah"→"Hia"; quy tắc một dòng = một cách diễn).

### 2422 — ふかみ — romaji
- JP: 「え！？　わ！？　わたしまた口に出て――\nじゃなくてそのっ、なんでもなっ――きゃああっ！？」
- TW: 「啊？！哇？！我又說出口了……不是的，沒什麼……呀？！」
- Cũ: 「Hả!? Oa!? Em lại lỡ nói ra mất rồi——\nKhông phải đâu, cái đó, không có gì đâ—— ááá!?」
- Mới: 「Hả!? Oa!? Em lại lỡ nói ra mất rồi——\nKhông phải đâu, cái đó, không có gì đâ—— Kyaaa!?」
- Lý do: きゃああっ = きゃ(1a) + ああ(2a) = 3 âm a → "Kyaaa" (quy tắc 3b + công thức đếm あ lặp, tiền lệ ふかみh1 967). Bản cũ "ááá" mất phụ âm ky-. Giữ "đâ——" cho なんでもなっ (ngắt câu, đã diễn bằng ――).

### 2784 — ふかみ — romaji
- JP: 「やぁん……こんなに濡れちゃって――んっ」
- TW: 「討厭……都這麼濕了……唔」
- Cũ: 「Ưm…… ướt nhẹp hết cả rồi—— ưm」
- Mới: 「Yaan…… ướt nhẹp hết cả rồi—— ưm」
- Lý do: やぁん = や(1a) + ぁ(1a) + ん = "Yaan". Bản cũ "Ưm" sai hẳn âm (đó là âm của ん, không phải やぁん) — lỗi mất âm (tiền lệ ポーレットh5 921 やぁ→"Yaa").

### 2876 — ふかみ — romaji
- JP: 「そこっ――やっ――らめっ――ふっ、あっ――\nきもち、よす――ぎて――んっ――だめ、ふ、ぅ」
- TW: 「那裡……不要……住手……啊……太舒服了……嗯……不行，呼……」
- Cũ: 「Chỗ đó—— không—— đừng—— phù, a——\nSướng, quá—— mất—— ưm—— không được, phù, ư」
- Mới: 「Chỗ đó—— Ya—— đừng—— phù, a——\nSướng, quá—— mất—— ưm—— không được, phù, ư」
- Lý do: やっ → "Ya" (như 2281). Nghĩa phản đối vẫn giữ bởi "đừng" cho らめっ ngay sau — khác 2234/2546 (xem cờ F1) ở chỗ "không" ở đây chỉ là token độc lập trong chuỗi rên, không phải vị ngữ của câu. Giữ "phù, ư" cho ふ、ぅ (nguyên âm đúng, xem §4).

### §3C. Đếm nguyên âm (5 dòng chỉ sửa số lượng)

### 2289 — ふかみ — đếm nguyên âm
- JP: 「きゅふああああああああああああああんんっ！！！」
- TW: 「呀！！！」
- Cũ: 「Kyufuaaaaaaaaaaaaaaan!!!」
- Mới: 「Kyufuaaaaaaaaaaaaaann!!!」
- Lý do: JP có 14 âm a (きゅふ + あ×14) và んん = 2n; bản cũ 15a/1n — thừa 1a, thiếu 1n. Đếm máy: a = 14, n = 2 (một ん = một n, xem 2287).

### 2379 — ふかみ — đếm nguyên âm
- JP: 「はああああああっっっ」
- TW: 「啊啊啊」
- Cũ: 「Hà a a a a a a a」
- Mới: 「Hà a a a a a a」
- Lý do: JP có 7 âm a (は + あ×6); bản cũ "Hà" + 7 "a" = 8 — thừa 1a. Giữ nguyên っっっ cuối (ngắt đột ngột, đã diễn bằng việc câu kết thúc đột ngột không dấu câu — cùng cách xử lý như 2332 んきゅううっっ→"Nkyuuu!!!" và 2335 っっ không thêm Ư).

### 2427 — ふかみ — đếm nguyên âm
- JP: 「はぅぅ」
- TW: 「嗚」
- Cũ: 「A ư」
- Mới: 「A ư ư」
- Lý do: はぅぅ = は(1a) + ぅ + ぅ = 3 nguyên âm theo công thức (1 + số う/ぅ = 1 + 2); bản cũ "A ư" chỉ có 2 — thiếu 1 "ư". Khác 2426 はぅ→"Hưm" (giữ nguyên — đó là từ cảm thán Việt "hừm", diễn nghĩa tiếng thở dài, không phải diễn âm từng mora; xem §4).

### 2428 — ふかみ — đếm nguyên âm
- JP: 「んうぅっ！」
- TW: 「嗚！」
- Cũ: 「Ưm ư!」
- Mới: 「Ưm ư ư!」
- Lý do: んうぅっ = ん + う + ぅ = 3 nhịp; bản cũ chỉ có 2 token — thiếu 1 "ư" (tiền lệ ポーレットh5 1015 んうぅっ→"ưm ư ư", 3 token).

### 3911 — monologue — đếm nguyên âm
- JP: （ああ――）
- TW: （是啊……）
- Cũ: （A——）
- Mới: （Aa——）
- Lý do: ああ = 2 âm a → "Aa". Đây là tiếng rên trong chuỗi SFX hành động (3907–3915), khác các dòng ああ thừa nhận ("À/Ừ") ở 2321/2450/2451 — những dòng đó là lời đáp, giữ nguyên. (TW diễn "是啊" như lời đáp, nhưng JP + vị trí trong chuỗi SFX hành động cho thấy đây là tiếng rên; JP hơn TW.)

### §3D. Gasp っ cuối dòng bị mất (4 dòng chỉ sửa gasp)

Cùng mẫu với 2728 mà audit đã sửa trong chính file này (「――っ！」→「——Ư!」): っ tuyệt đối cuối dòng sau ――/……, không dấu câu sau, âm bị mất hẳn → thêm Ư. Sweep có 14 mục cho file nhưng không liệt kê 4 dòng này; audit cũng bỏ sót.

### 2202 — 双鉄 — gasp
- JP: 「それほど慌てて飲まずとも――っ」
- TW: 「你沒必要喝得這麼急……」
- Cũ: 「Em không cần phải uống vội vàng thế đâu——」
- Mới: 「Em không cần phải uống vội vàng thế đâu——Ư」
- Lý do: っ tuyệt đối cuối dòng sau ――, mất hẳn → "Ư" (tiền lệ 2728).

### 2596 — ふかみ — gasp
- JP: 「もっとどんどん傾いて、\nそしたらきっと、いつか――っ！」
- TW: 「於是鐵軌越來越傾斜，那樣以後說不定……」
- Cũ: 「Nó sẽ ngày càng nghiêng hơn,\nvà rồi chắc chắn, một lúc nào đó——!」
- Mới: 「Nó sẽ ngày càng nghiêng hơn,\nvà rồi chắc chắn, một lúc nào đó——Ư!」
- Lý do: như 2202 (mẫu 2728, có "!" sau っ cũng vẫn thêm Ư).

### 3208 — monologue — gasp
- JP: けれど一突き。あと一突き。\nふかみの膣の、最奥のその向こうまでをも――っ！
- TW: 再一下，再插一下。我要忍耐到插進深美最裡面！
- Cũ: Nhưng thêm một cú đâm nữa. Thêm một cú đâm nữa thôi.\nĐến tận cùng phía bên kia nơi sâu nhất, trong âm đạo của Fukami——!
- Mới: Nhưng thêm một cú đâm nữa. Thêm một cú đâm nữa thôi.\nĐến tận cùng phía bên kia nơi sâu nhất, trong âm đạo của Fukami——Ư!
- Lý do: như 2202 — độc thoại nội tâm kết bằng ――っ, âm gasp mất hẳn. (Lưu ý: dòng monologue không có ngoặc 「」, fix cũng không thêm ngoặc.)

### 3435 — monologue — gasp
- JP: もう暫くは動けない。動けば精を吐かされるから。\n窮屈で快適な膣内を、もっとじっくり――っ！？
- TW: 我暫時動不了了。一旦亂動肯定會射。我要再仔細點享受這緊緻而舒適的……嗯？！
- Cũ: Tôi không thể nhúc nhích thêm một lúc nữa. Vì nếu cử động, tôi sẽ xuất tinh mất.\nBên trong âm đạo chật chội và thoải mái này, tôi muốn từ từ thưởng thức thêm——!?
- Mới: Tôi không thể nhúc nhích thêm một lúc nữa. Vì nếu cử động, tôi sẽ xuất tinh mất.\nBên trong âm đạo chật chội và thoải mái này, tôi muốn từ từ thưởng thức thêm——Ư!?
- Lý do: như 3208 (――っ！？ cuối độc thoại).

## §4. Các dòng rên GIỮ nguyên (ghi chú đáng kể)

- **Gasp Ư của audit — giữ cả 4:** 1664 「…………っ」→「…………Ư」, 1677 「……っ」→「……Ư」, 2449 「っ！！？」→「Ư!!?」, 2728 「――っ！」→「——Ư!」. Không đụng dòng gasp Ư nào.
- **Sweep 14 mục đã kiểm chứng trực tiếp:** nhận 1664, 2728 (audit đã sửa đúng); 2281, 3645 "already-rendered" đúng — giữ (2281 chỉ đổi やっ→"Ya" ở §3B, gasp đã diễn bằng "Ưm" nên không thêm Ư); 10 mục "needs-file-audit" đã xem lại: 2292 (audit sửa bịa nghĩa; moan đổi やっ→"Ya" ở §3B), còn 2519/2531/2629/2829/2869/3127/3390/3619/3805 không có gasp bị mất (っ gắn từ nội dung hoặc đã diễn) — giữ. 0 trùng key moan với sweep ngoài các dòng trên.
- **Không dòng "Kh" nào bị đổi.** File này không có dòng "Kh" cho っ (kiểm tra toàn file: 0 dòng chứa "Kh"/"kh" diễn っ).
- **ひぁ → "Hya" giữ (2335):** ひぁ là MỘT mora ("hya"), khác ひあ hai mora ("Hia") — "Hya—— a!" đúng. Cùng dòng: んうううううう → "Ưm ư ư ư ư ư ư" (7 token = 7 mora, đúng công thức).
- **Romaji đã đúng — giữ:** 2286 きゃうっ→"Kyau!!", 2295 ひゃっ→"Hya!!?", 2332 んきゅううっっ→"Nkyuuu!!!" (3u đúng), 2397 んゆんっ→"Nyun!!!", 2285 ひぎゅっ→"Higyu!".
- **Đếm đúng — giữ:** 2429 んうっ→"Ưm ư!!" (2 nhịp), 2380 はああああああぁぁぁぁん→"Hà a a a a a a a a a a n!" (11a + n, đếm máy đúng), 2382 あああ→"Aaa" (3a).
- **Hơi thở ふ/ふっ → "phù" giữ:** 2301 ふっ, 2337 ふ、, 2341 ふ、, 2767 ふっ — ふ đơn lẻ là hơi thở, "phù" đúng âm. 2301/2876 ふ、ぅ → "phù, ư" giữ (ふぅ tách đúng: ふ=u + ぅ=u, nguyên âm đúng, ngắt giữ nguyên).
- **はうっ → "a ư" giữ (2383, 2767):** diễn đúng hai mora ha+u (tiền lệ audit giữ nguyên ở 2767).
- **Họ ちゅ → "chụt" giữ:** 2338, 2341, 2424 (ちゅぽっ→"Chụt"), 2425 (8× "chụt"), 2431 (ちゅうっ/ちゅくっ/ちゅっ→"chụt"). 2391 ちゅって/ぐりっ→"Mút đi!/Ngoáy đi!" giữ (mệnh lệnh, diễn nghĩa động từ, không phải rên).
- **Chuỗi nuốt んく/こく/ごく → "Ực/ực" giữ (2302–2304):** diễn theo TW 咕咚 (tiếng nuốt), đúng. 2303 �んぷっ→"Ưm" giữ (xem cờ F3).
- **Tiếng cười giữ:** 2478 うふふっ→"ufufu" (cười, đúng quy tắc Hieu 19/11 — không diễn thành rên), 2605 えへへっ→"Hehe".
- **Cảm thán Việt giữ (không phải rên):** 2290 ひぇっ→"Hả!?", 2314 うわっ→"Oái!?", 2318 えええっ→"Hảảả!?", 2426 はぅ→"Hưm" (từ cảm thán "hừm"), 2321/2322/2325/2434/2450/2451/2476/2615/2625/2640/2875 ああ→"À/Ừ/Được" (lời đáp thừa nhận), 3284/3519 ああ→"A" (thán từ mở đầu độc thoại).
- **っ gắn từ nội dung / ngắt giữa dòng — giữ (không thêm Ư):** 2139 さぬっ――, 2531 けどっ――, 3476 食い込ませっ―― (っ sau ―― giữa câu, đã diễn bằng ――); 2483 なくっ, 2651 ほしっ, 2400 ですっ, 2697/2699 ふかみっ/こいっ, 2819 なっ, 2861 場所っ, 2617 ってっ (っ nhấn mạnh gắn từ, theo quy tắc gasp đã chốt).
- **SFX （ ） dạng động từ Việt — giữ cả 40 dòng (3879–3926):** びゅう/ずぶっ/ぐりっ/ちゅぐっ… → "Phụt/Phập/Ngoáy/Vê/…" (đúng thông lệ dự án cho SFX hành động; xem cờ F4 về việc chưa áp công thức đếm cho nhóm này). 3880 ひゅううっ→"(Vù vù)" giữ (onomatopoeia Việt cho tiếng gió). 3887/3925 là độc thoại trong ngoặc, không phải SFX — giữ.

## §5. Cờ cho đợt thống nhất

- **F1 — やっ chìm trong diễn giải nghĩa (2234, 2546):** 2234 「ぬいちゃ、やっ――」→"Rút ra, không chịu" và 2546 「いっちゃう、の、――やぁ――で、すっ」→"Là, không—— chịu—— đâu, ạ" — âm や/やぁ bị hút vào vị ngữ diễn nghĩa ("không chịu"), không sửa được bằng thay token (thay "không chịu"→"Ya" sẽ làm vỡ câu). Cần cấu trúc lại câu mới diễn được âm — để parent/quyết định đợt thống nhất. (Khác 2876: "không" ở đó chỉ là token độc lập, đã sửa → "Ya".)
- **F2 — 2431 �んふっ → "ưm" (chưa chắc):** chuỗi 「んっ――っ――ふっ――んっ――ちゅうっ――ちゅくっ――ちゅっ――んふっ――ちゅ、んぁ」 — んふっ diễn "ưm" làm mất âm f (so với こくっ/んくっ cùng dòng đều diễn phụ âm "ực"). Có nên romaji "Nfu" không, hay giữ "ưm" như hơi thở mũi bịt? Chưa quyết — giữ nguyên, chờ parent.
- **F3 — 2303 んぷっ → "Ưm" (chưa chắc):** chuỗi nuốt 「んぷっ――んっ――こくっ――んくっ」 diễn "Ưm—— ưm—— ực—— ực" — んぷっ chỉ diễn ん, mất ぷ (trong khi こくっ/んくっ diễn được phụ âm). Giữ nguyên theo chuỗi nuốt Việt, chờ parent quyết có romaji hoá không.
- **F4 — SFX （ ） chưa áp công thức đếm:** 3885 （ざぁぁああああああああああっ）→ 10× "Rào" (JP có 12 âm a); 3892/3898/3900/3902/3921 chuỗi う dài (7–8 u) diễn thành 1 động từ ("Rút ra!", "Phập!", "Nhấn sâu!", "Siết chặt") — độ dài không diễn. Cùng câu hỏi mở như lr_れいな追加h F4 — chờ đợt thống nhất quyết có áp công thức đếm cho SFX （ ） không.
- **F5 — Phán đoán mới, lần đầu trong dự án:** 2309 ふわっ→"Fuwa" (ふ mất trong "Oa"); 2293 ひうっ→"Hiu" (âm mới, "Hya" sai hẳn). Cả hai chưa có tiền lệ chéo file — cần parent kiểm chứng.
- **F6 — Audit sửa sai 2 dòng fa/fu tách (2359, 2371):** audit gán "phà, a"/"phà…… a" cho ふ、あ / ふ……ァ — sai nguyên âm của ふ tách riêng (phải là "phù"/"Fu"). Bản moan này đã sửa thành "Fu, a"/"Fu……a". Khi áp dụng: dùng bản moan này, KHÔNG áp bản audit cho 2 key đó. 18 dòng fa/fu còn lại của audit đều bị thay thế bằng romaji ở đây (dùng bản moan, không áp bản audit). (Song song: parent ghi cờ F5 ở ハチロクh5 — dạng tách fa 1047 giữ "phù——a" vs 1178 → "Fu, a" — chưa thống nhất; bản này theo tiền lệ 1178.)
- **F7 — 2292 kế thừa fix audit:** fix cuối = fix nghĩa audit ("mưa to"→"to") + moan (やっ→"Ya"). Khi áp dụng: dùng giá trị JSON này (đã gồm cả hai), không áp riêng bản audit.
- **F8 — Đếm n cho んんっ ("nn" vs "nnn"):** bản này dùng "nn" cho んん (2287 "Fukyuuuunn", 2289 "…aann") theo tiền lệ đếm máy lr_ふかみh1 "Kufuunnnn" + lr_れいな追加h 1170 "Fuhyunnnn" (một ん = một n, っ không thêm n). Nhưng ふかみh1 967 "Hyaaann" viết 3 n cho �んん (tự mâu thuẫn với lý do "んん=2 n" của chính review đó) — cần đợt thống nhất chốt んんっ = "nn" hay "nnn".
- **F9 — 5 gasp audit + sweep bỏ sót (2202, 2352, 2596, 3208, 3435):** cùng mẫu 2728 đã chốt trong file; audit chỉ bắt 1664/1677/2449/2728. Lưu ý phân biệt với quyết định của parent ở ハチロクh5 (21/11 ~18:05 — BỎ Ư ở 996/1070/1073/1075/1077/1222 vì っ cuối có !/? diễn cắt): 6 dòng đó là っ cắt cuối RÊN DÀI đã diễn đủ âm (moan đã render, っ chỉ là ngắt, !/? đánh dấu ngắt); còn 5 dòng ở đây là っ gasp cuối CÂU NÓI/ĐỘC THOẠI (âm gasp riêng biệt, không thuộc về âm rên nào đã diễn) — tiền lệ trong file là 2728 (câu + ――っ！ → có Ư, parent-verified 20/11) và 2449 (っ！！？ → Ư). Đề nghị audit loop ghi nhận: quét bổ sung "――っ/……っ cuối dòng" cho các file còn lại.
- **F10 — 2427 vs 2426:** はぅぅ → "A ư ư" (đếm 3 nguyên âm) nhưng はぅ → "Hưm" giữ (từ cảm thán Việt). Ranh giới "diễn âm từng mora" vs "từ cảm thán Việt" cho tiếng thở dài — cần nhất quán ở đợt thống nhất.

## §6. Lượt soát 2 + kiểm chứng

- Lượt soát 2: đọc lại toàn bộ 44 giá trị fix đối chiếu từng JP (+TW khi cần), đếm lại độc lập từng rên dài bằng ký tự (2287: 5u/2n; 2289: 14a/2n; 2379: 7a; 2380: 11a — giữ nguyên; 2402: 5a; 2278: 4 nhịp; 2428: 3 nhịp; 2427: 3 nguyên âm; 2335: 7 nhịp — giữ nguyên; 3911: 2a).
- Kết quả lượt soát 2: tổng 44 / tái kiểm chứng 44 / bỏ 0 / sửa 2 (3208, 3435: fix tay ban đầu thêm thừa ngoặc 「」 cho 2 dòng monologue — đã gỡ, kiểm chứng diff chỉ còn chèn "Ư").
- Kiểm chứng diff máy: mỗi fix chỉ khác VN cũ ở đúng token rên đã nêu (xem §3); không fix nào đụng dòng không phải rên, không đổi đại từ/thuật ngữ/nghĩa (trừ 2292 kế thừa fix nghĩa audit đã nêu).
- JSON 44 mục, khóa string, jp/tw/old_vn khớp CSV3 (set tốt 11_Other) 44/44 (kiểm chứng máy: old_vn == giá trị CSV3 từng dòng; jp/tw cũng khớp).
- Khối TOML parse bằng tomllib: 44 khóa, 0 sai lệch giá trị so với wrong.json (xem §7). Quy ước khối TOML theo audit của chính file này: key có ngoặc kép, `\n` literal viết `\\n`.
- TOML gốc: BOM + CRLF, md5 `468ff9287da913deb380278b68d048f8`, 649 key script, 0 key trùng, không có bản trùng.

## §7. Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
[script]
"2202" = "「Em không cần phải uống vội vàng thế đâu——Ư」"
"2273" = "「Hia—— a—— chim—— tuyệt quá——\\nAnh, Soutetsu—— nóng, quá—— phình to, ra」"
"2275" = "「Kya」"
"2276" = "「Kya!」"
"2278" = "「Hyua! A—— Fua! Cái này—— tuyệt,\\nƯm ư ư ư—— bên trong—— từ từ—— bị, đẩy, vào」"
"2280" = "「Hia! A—— mãnh liệt—— mãnh, liệt, quá,\\nBạch, bạch, cô bé, phát ra, tiếng, kêu」"
"2281" = "「Ya! A! Mãnh liệt! Mãnh, liệt, quá! Ưm,\\nBụng—— cô, bé—— co thắt, liên tục」"
"2283" = "「Hia! A!!!!!」"
"2287" = "「Fukyuuuunn!! Fua—— bên trong——\\nSâu, nhất—— tử cung—— bị, chạm vào, rồi——」"
"2289" = "「Kyufuaaaaaaaaaaaaaann!!!」"
"2292" = "「Ya, gì thế này!? Sao lại to thế này chứ」"
"2293" = "「Hiu!!?」"
"2301" = "「Phù—— ưm—— tê tê, rần rần—— Fa——\\nHà—— phù, ư—— ưm…… bứt, rứt, quá」"
"2302" = "「Ực—— ực—— ực—— Puaa」"
"2309" = "「Fuwa!!」"
"2338" = "「A…… Fua—— ưm—— chụt—— chụt,\\nchụt—— chụt—— chụt—— chụt」"
"2345" = "「Fa…… hà…… a——」"
"2346" = "「Fua—— a—— hà—— hà—— ngập tràn,\\nBụng—— ngập tràn—— óc ách—— óc ách」"
"2349" = "「Hà—— hà—— hà—— ưm, Ku——\\nDạ—— chỗ đó—— cũng—— không phải, đâu——」"
"2351" = "「Fua—— a—— ưm—— chụt—— Pua!\\nA—— em muốn, ạ—— toàn bộ, anh, Soutetsu」"
"2352" = "「Fua—— a—— to—— to, quá——\\nChim—— chỗ đó—— chỗ, thô to——Ư」"
"2358" = "「Fa—— a—— ngực, núm, vú—— ưm,\\nMạnh—— mạnh hơn, chút nữa, cũng không, sao—— Fa」"
"2359" = "「Hà—— a—— bên trong—— a, Fua,\\nNgón tay—— ưm, ư—— ư—— cọ xát—— Fu, a」"
"2362" = "「Fua—— a—— hi, ư—— phần trên——\\nCủa, cô bé—— ưm—— giống như, đang cào—— vậy——」"
"2371" = "「A…… chỗ này, ạ—— Fu……a——\\nChim, của—— anh, Soutetsu」"
"2379" = "「Hà a a a a a a」"
"2384" = "「A ư, ưm—— núm, vú—— ưm—— từ, đầu\\n——Fu, a—— ngực—— trơn, tuột」"
"2385" = "「Ư! ——Pua」"
"2388" = "「Fua! A—— nóng quá—— bên trong—— bên trong!\\nBên trong—— cô bé—— phụt ra, đánh vào」"
"2394" = "「Hà! Thích—— sướng—— quá—— Fua,\\nCứ thế này—— cứ, thế này—— em—— cứ thế này」"
"2402" = "「Hà a a a a, phù! A! Tử cung!\\nMuốn—— Fua—— bị cộc—— gõ cửa」"
"2409" = "「Hả? A——Amu——ưm——」"
"2422" = "「Hả!? Oa!? Em lại lỡ nói ra mất rồi——\\nKhông phải đâu, cái đó, không có gì đâ—— Kyaaa!?」"
"2427" = "「A ư ư」"
"2428" = "「Ưm ư ư!」"
"2430" = "「Ưm—— Fua——」"
"2577" = "「Em biết, ạ. ——Ưm—— hình, dáng——\\nCủa, anh, Soutetsu—— Fua—— của, chim——」"
"2596" = "「Nó sẽ ngày càng nghiêng hơn,\\nvà rồi chắc chắn, một lúc nào đó——Ư!」"
"2767" = "「Quần áo—— hay gì đó—— sao cũng,\\nđược—— Fua—— ưm—— phù—— a ư」"
"2784" = "「Yaan…… ướt nhẹp hết cả rồi—— ưm」"
"2876" = "「Chỗ đó—— Ya—— đừng—— phù, a——\\nSướng, quá—— mất—— ưm—— không được, phù, ư」"
"3208" = "Nhưng thêm một cú đâm nữa. Thêm một cú đâm nữa thôi.\\nĐến tận cùng phía bên kia nơi sâu nhất, trong âm đạo của Fukami——Ư!"
"3435" = "Tôi không thể nhúc nhích thêm một lúc nữa. Vì nếu cử động, tôi sẽ xuất tinh mất.\\nBên trong âm đạo chật chội và thoải mái này, tôi muốn từ từ thưởng thức thêm——Ư!?"
"3911" = "（Aa——）"
```

## Kết bài

- ふかみh3 moan: đổi 44/649 dòng (6,8% file; 44/328 dòng ứng viên) — romaji 31, romaji + đếm nguyên âm 3, đếm nguyên âm 5, gasp 4, romaji + gasp 1. Trong đó 21 dòng kế thừa/lật fix audit (20 fa/fu + 2292), 23 dòng mới.
- Lỗi chủ đạo: họ fa/fu bị diễn "phù"/"phà"/"phùa" (21 dòng → romaji Fa/Fua/Pua); mất phụ âm mora trong "Á"/"Ưm" (や/きゃ/ひあ/ひう/ふわ/くっ/あむ/やぁん — 14 dòng); đếm nguyên âm thiếu/thừa (8 dòng); gasp っ cuối dòng bị mất mà sweep + audit bỏ sót (5 dòng).
- Khối TOML 44 key đã parse đúng (tomllib, 0 sai lệch); JSON 44 mục khóa string, jp/tw/old_vn khớp CSV3 44/44.
- Lượt soát 2: 44/44 tái kiểm chứng, 0 bỏ, 2 sửa (3208/3435 gỡ ngoặc thừa). Sweep 14 mục đã kiểm chứng, không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào (file không có dòng "Kh").
- 10 cờ cho đợt thống nhất (F1–F10), trong đó quan trọng nhất: F1 (2234/2546 や chìm trong diễn nghĩa), F6 (audit sửa sai 2 dòng fa/fu tách 2359/2371), F8 (んんっ = "nn" hay "nnn"), F9 (5 gasp audit + sweep bỏ sót).
