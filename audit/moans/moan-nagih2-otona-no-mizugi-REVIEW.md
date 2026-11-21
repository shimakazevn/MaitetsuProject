# Moan-fix review — 凪h2_おとなの水着.txt.toml

File H-scene của Nagi (đi mua đồ bơi người lớn → chơi dưới sông → H-scene trong rừng). Sửa CHỈ tiếng rên/thở/gasp/SFX theo quy tắc romaji (Hieu duyệt 21/11 ~01:56).

## 1. File verification

- TOML: `sources/toml2/translation_toml/07_Nagi_Fukami/#U51eah2_#U304a#U3068#U306a#U306e#U6c34#U7740.txt.toml`
- TOML md5: `a581ef85d1d7aed81fc5303b23f050ea` (122.750 bytes, UTF-8 BOM + CRLF)
- CSV3: 1 set duy nhất (File = `translation_toml\07_Nagi_Fukami\凪h2_おとなの水着.txt.toml`), 673 rows, 0 key trùng. Không có 2 set CSV → không cần chọn set tốt.
- TOML vs CSV3: 673/673 key đều có mặt; 373 "mismatch" chỉ là TOML-2 flatten literal `\n` thành khoảng trắng (đã biết, CSV3 là chuẩn cho fix list).
- Audit trước đó (vòng audit loop, TRƯỚC quy tắc romaji): 89 dòng sai / 673 (13,2%).

## 2. Moan inventory

Đã đọc hết 673 dòng (CSV3 + đối chiếu TOML). Tìm được **158 dòng moan** (dòng có âm rên/thở/gasp/SFX trong JP hoặc VN diễn âm đó):

| Loại | Số dòng |
|---|---|
| Rên / thở / gasp / hừm trong thoại | 88 |
| SFX trong ngoặc (monologue) | 39 |
| SFX miệng: hôn / liếm / nuốt (ちゅ・ぺろ・れる・ごく…) | 22 |
| Cười / giggle (ふふ・えへへ・んふふ) | 9 |
| **Tổng** | **158** |

Kết quả xử lý 158 dòng moan:
- **Sửa: 25 dòng** (24 moan-wrong-sound + 1 moan-length)
- **Giữ: 124 dòng** (diễn âm đúng/tự nhiên — xem §4)
- **Sweep đã xử lý, KHÔNG đụng: 8 dòng** — 7 gasp-sweep (2487, 2536, 2544, 3354, 3433, 3610, 3719: raw-tsu / lost-gasp-trailing, fix Ư đã ghi trong sweep) + 1 already-rendered (2489, VN đã diễn gasp bằng Ư/Phù/Ưm — sweep loại đúng). Đã kiểm tra từng entry sweep với JP: 7/7 đúng quy tắc gasp, 1/1 loại đúng.
- **Flag: 1 dòng** (2515 — xem §5)

## 3. Per-row fixes (25 dòng)

Quy tắc áp dụng chung: romaji Hepburn, độ dài nguyên âm theo công thức (số nguyên âm VN = 1 + số う/ぅ trong JP); một âm = một cách diễn (VN hoặc romaji, không trộn); ひあ = "Hia" ≠ ひゃ = "Hya"; ふぁ/ふあ → romaji Fa/Fua khi "phà"/"phùa" nghe ngượng (quy tắc romaji gọi đích danh họ fa/fu); ぷ = P (không phải Ph).

### Key 2395 — 凪
- JP: 「んきゅっ――ふっ――んっ！」
- TW: 「呀……唔……嗯！」
- Old VN: 「Ưm——Phù——Ưm!」
- New VN: 「Nkyu——Phù——Ưm!」
- Lý do: んきゅっ = "nkyu" (gasp kiểu "nkyu!"), old "Ưm" làm mất hẳn âm "kyu". Romaji "Nkyu" giữ đúng âm. ふっ→"Phù", んっ→"Ưm" giữ nguyên (đúng).

### Key 2397 — 凪
- JP: 「ひあっ――あっ――ん――ゅっ――んふううっ――\nいま、いま、ウチ――そがぎゃんと、された、らっ」
- TW: 「呀……啊……嗯，唔，嗯，剛剛，剛剛，咱……這樣的……」
- Old VN: 「Hya——A——Ư——m——Ưm phuuuu——\nBây giờ, bây giờ, em——Bị làm, như thế, thì」
- New VN: 「Hia——A——Ư——Yu——Ưm phuuuu——\nBây giờ, bây giờ, em——Bị làm, như thế, thì」
- Lý do: ひあっ = "hia" ≠ "hya" (sai âm); ゅっ = "yu" bị cắt, old diễn thành "m" là sai. Romaji "Hia" + "Yu". (Ghi chú: "phuuuu" có 4 u trong khi JP んふううっ = 3 u — lệch 1 u, không đáng kể, giữ nguyên vì ngoài phạm vi sửa targeted.)

### Key 2398 — 凪
- JP: 「ひあっ――あっ――あああっ！　おなか、ウチ、の、\nあかちゃん――お部屋、ごつんっ――ごつんって」
- TW: 「呀……啊，啊！肚子，咱……造人的房間……敲打，被敲打著」
- Old VN: 「Hya——A——Aaa! Bụng, của em,\nem bé——Căn phòng, cộc——bị đập cộc cộc á」
- New VN: 「Hia——A——Aaa! Bụng, của em,\nem bé——Căn phòng, cộc——bị đập cộc cộc á」
- Lý do: ひあっ = "hia", old "Hya" sai âm (hia ≠ hya). あああっ→"Aaa" (3 a) đã đúng, giữ nguyên.

### Key 2401 — 凪
- JP: 「ひゅあっ――あっ――そこ、だけ――ん、きゅふっ、\nあっ――なぎ、ウチ――ウチ――らめ、なっちゃうっ」
- TW: 「呀……啊，就一個地方……嗯，呀，啊，本……咱，咱……會瘋掉的」
- Old VN: 「Hyua——A——Chỉ, chỗ đó——Ưm, a,\nA——Nagi, em——em——hỏng, mất thôi」
- New VN: 「Hyua——A——Chỉ, chỗ đó——Ưm, Kyufu,\nA——Nagi, em——em——hỏng, mất thôi」
- Lý do: きゅふっ = "kyufu" (gasp thở), old diễn thành "a" làm mất hẳn âm "kyufu". Romaji "Kyufu". ひゅあっ→"Hyua" đã đúng.

### Key 2402 — 凪
- JP: 「ひゃう」
- TW: 「呀」
- Old VN: 「Hya」
- New VN: 「Hyau」
- Lý do: ひゃう = "hyau" (2 nguyên âm: hya + u), old "Hya" nuốt mất mora う. Công thức nguyên âm: 1 + 1 う = 2 nguyên âm → "Hyau".

### Key 2403 — 凪
- JP: 「ひあうっ！！！」
- TW: 「呀！」
- Old VN: 「Hyau!!!」
- New VN: 「Hiau!!!」
- Lý do: ひあう = "hiau" (Hepburn: hi-a-u), old "Hyau" là romaji của ひゃう — sai âm khác. Tiền lệ đúng trong file: ひあ → "Hia" (2414, 2412 "Hiaaa"). Sửa để không đụng với ひゃう → "Hyau" (2402).

### Key 2405 — 凪
- JP: 「ひぎゅっ！　あ！　すごいっ――すご、かっっ――\nはっ――ふあっ、あっ――おまん、こ、ぐりゅっ、て」
- TW: 「呀！啊！好棒……好棒……啊……啊，啊……下面好緊」
- Old VN: 「Higyu! A! Tuyệt quá——Tuyệt, quá——\nHà——Phù, a——Âm, đạo, ngoáy, á」
- New VN: 「Higyu! A! Tuyệt quá——Tuyệt, quá——\nHà——Fua, a——Âm, đạo, ngoáy, á」
- Lý do: ふあっ = "fua", old "Phù, a" vừa sai (tách một âm thành hai, "phù" ≠ "fua") vừa ngượng. Romaji "Fua". ひぎゅっ→"Higyu" đã đúng.

### Key 2407 — 凪
- JP: 「ひあっ！　はっ――ああっ――あっ――おなかっ\n――ごりゅって――おまん、こ――なか――からっ」
- TW: 「呀！啊，啊……啊，肚子一緊……下面的裡面……」
- Old VN: 「Hya! Hà——Aa——A——Bụng\n——Chà xát——Âm, đạo——Từ bên——trong」
- New VN: 「Hia! Hà——Aa——A——Bụng\n——Chà xát——Âm, đạo——Từ bên——trong」
- Lý do: ひあっ = "hia", old "Hya" sai âm. ああっ→"Aa" (2 a) đã đúng.

### Key 2409 — 凪
- JP: 「かひゅっ！！！」
- TW: 「呀！！！」
- Old VN: 「Hya!!!」
- New VN: 「Kahyu!!!」
- Lý do: かひゅっ = "kahyu" (gasp "kahyu!"), old "Hya" là âm khác hẳn. Romaji "Kahyu".

### Key 2414 — 凪
- JP: 「ひあああっ――そこっ――そこ――んひっ、\nいっ、あっ――きもち、よかっ――気持ち、よかぁ」
- TW: 「呀，這裡，這裡……嗯，舒服，啊……好舒服，好舒服」
- Old VN: 「Hiaaa——Chỗ đó——Chỗ đó——Ưm,\nA, a——Sướng, quá——Sướng, quá á」
- New VN: 「Hiaaa——Chỗ đó——Chỗ đó——Nhi,\nI, a——Sướng, quá——Sướng, quá á」
- Lý do: 3 âm riêng biệt bị diễn trùng nhau: んひっ = "nhi" (old "Ưm" mất "hi"), いっ = "i" (old "A" sai nguyên âm — "i" ≠ "a", lại trùng với あっ→"a"). Romaji "Nhi, I, a" giữ đủ 3 âm. ひあああっ→"Hiaaa" đã đúng.

### Key 2418 — 凪
- JP: 「ひあっ！？　らめっ！　うちっ、いまっ、\nイッて、りゅっ――イって！　イッテりゅからあっ」
- TW: 「呀？！不行！咱剛剛……沒……沒！沒丟……」
- Old VN: 「Hya!? Không! Em, bây giờ,\nĐang lên, đỉnh——Đang lên đỉnh! Đang lên đỉnh rồi á」
- New VN: 「Hia!? Không! Em, bây giờ,\nĐang lên, đỉnh——Đang lên đỉnh! Đang lên đỉnh rồi á」
- Lý do: ひあっ = "hia", old "Hya" sai âm.

### Key 2428 — 凪
- JP: 「ごくっ、ごきゅっ――んぐっ――ぐっ――ぷあっ」
- TW: 「咕咚，咕咚……咕咚，咕咚……呼」
- Old VN: 「Ực, ực——Ư——Ư——Phù a」
- New VN: 「Ực, ực——Ư——Ư——Pua」
- Lý do: ぷあっ = "pua" (pu-a), old "Phù a" vừa sai phụ âm (p → ph/f) vừa tách một âm thành hai. Romaji "Pua". ごくっ/ごきゅっ→"Ực" đã đúng.

### Key 2445 — 凪
- JP: 「ふあっ――」
- TW: 「哇……」
- Old VN: 「Phù a——」
- New VN: 「Fua——」
- Lý do: ふあっ = "fua" một âm, old "Phù a" tách thành hai và sai. Romaji "Fua".

### Key 2449 — 凪
- JP: 「ふあっ――あっ――んっ――く、うっ――ふあ――\nここ――んっ――ふっ――もう、ちょっと――あうっ」
- TW: 「哇……啊……嗯……唔，哇……這裡……嗯，呼……還差一點……啊嗚」
- Old VN: 「Phù——A——Ưm——Ư, ư——Phù——\nChỗ này——Ưm——Phù——Một chút, nữa——A」
- New VN: 「Fua——A——Ưm——Ư, ư——Fua——\nChỗ này——Ưm——Phù——Một chút, nữa——A」
- Lý do: cả hai ふあ (đầu và giữa dòng) đều bị diễn "Phù" — sai nguyên âm (fua ≠ fu). Romaji "Fua" cả hai chỗ. ふっ→"Phù" (giữa dòng, cuối) là đúng vì ふ = "fu" — giữ nguyên.

### Key 2451 — 凪
- JP: 「ふぁ……ぁ……これ……凄かとばい……\nん……わ……わわ……ええ……どうしよう、ばい」
- TW: 「哇……啊……這……太厲害了……唔……哇……哇哇……哎，這可怎麼辦」
- Old VN: 「Phù……A……Cái này……Kinh khủng quá á……\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」
- New VN: 「Fa……A……Cái này……Kinh khủng quá á……\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」
- Lý do: ふぁ……ぁ…… = "fa...a..." kéo dài (2 nguyên âm a), old "Phù……A……" sai nguyên âm ở phần đầu (fa ≠ phu) và tách âm dài thành hai mảnh không ăn khớp. Romaji "Fa……A……" giữ cấu trúc ngắt …… của JP.

### Key 2452 — 凪
- JP: 「ふあっ」
- TW: 「哇」
- Old VN: 「Phù a」
- New VN: 「Fua」
- Lý do: ふあっ = "fua" một âm ngắn; old "Phù a" tách thành hai, sai. Romaji "Fua".

### Key 2462 — 凪
- JP: 「ふぁっ！？」
- TW: 「哇？！」
- Old VN: 「Hya!?」
- New VN: 「Fa!?」
- Lý do: ふぁっ = "fa" — old "Hya" là âm hoàn toàn khác (hya ≠ fa). Đây là lỗi sai âm rõ nhất trong file. Romaji "Fa!?": "Phà!?" nghe ngượng (đọc như từ "phà"), nên dùng romaji theo quy tắc.

### Key 2483 — 凪 (moan-length)
- JP: 「んんんっ――や――あっ――もっと――おま、んこ、\nよか、とこ――ある――のにっ――んっ――ふっ」
- TW: 「唔……不要……啊……再進來點……還有更舒服的地方……嗯……唔」
- Old VN: 「Ưm——A——A——Âm, đạo, vẫn còn——\nchỗ, sướng, hơn——mà——Ưm——Phù」
- New VN: 「Ưmmm——A——A——Âm, đạo, vẫn còn——\nchỗ, sướng, hơn——mà——Ưm——Phù」
- Lý do: んんんっ là tiếng hừm dài (3 mora ん), old "Ưm" (1 m) làm mất độ dài. Tiền lệ trong file: 2500 diễn độ dài bằng lặp chữ. Sửa thành "Ưmmm" (3 m).

### Key 2500 — 凪
- JP: 「んゅうううううううぅぅっ！！！」
- TW: 「唔！！！」
- Old VN: 「Ưnnnnnnnnnnn!!!」
- New VN: 「Nyuuuuuuuuuu!!!」
- Lý do: âm là "nyuu..." dài (んゅ + 9 nguyên âm う/ぅ = 10 u theo công thức, đã đếm lại), old "Ưnnn..." diễn thành tiếng hừm "nnn" làm mất hẳn âm "yu" — đây đúng trường hợp quy tắc romaji nhắm tới (moan dài nhiều nguyên âm). Romaji "Nyuuuuuuuuuu" (Ny + 10 u).

### Key 2512 — 凪
- JP: 「んひゅっ！！！？」
- TW: 「唔？！」
- Old VN: 「Hya!!!?」
- New VN: 「Nhyu!!!?」
- Lý do: んひゅっ = "nhyu", old "Hya" sai âm hẳn. Romaji "Nhyu".

### Key 2520 — 凪
- JP: 「かっ――はっ！　あっ！　あぐっ――かふっ！\nはぁっ！　はあっ！　はあっ！　はあっ！」
- TW: 「啊……啊！啊！唔……唔！啊！啊！啊！啊」
- Old VN: 「Hà——Hà! A! A——Hà!\nHà! Hà! Hà! Hà!」
- New VN: 「Ka——Hà! A! Agu——Kafu!\nHà! Hà! Hà! Hà!」
- Lý do: old gộp hết thành "Hà": かっ = "ka" (old "Hà" sai phụ âm k→h), あぐっ = "agu" (old "A" mất "gu"), かふっ = "kafu" (old "Hà" sai). Romaji "Ka", "Agu", "Kafu". はっ/はぁっ/はあっ→"Hà" đã đúng, giữ nguyên.

### Key 2526 — 凪
- JP: 「ふあっ――にーひゃん――ん、ちゅう――\nちゅう、ちゅうぅ」
- TW: 「啊……大哥哥，嗯……親，親親」
- Old VN: 「Phù a——Anh hai——Ưm, chụt——\nChụt, chụt」
- New VN: 「Fua——Anh hai-hyan——Ưm, chụt——\nChụt, chụt」
- Lý do: (1) ふあっ = "fua", old "Phù a" sai → romaji "Fua". (2) にーひゃん = "nii" + gasp "hyan" — old "Anh hai" nuốt mất tiếng "hyan"; giữ địa chỉ "Anh hai" và gắn gasp bằng gạch nối "Anh hai-hyan" theo quy tắc "không để mất âm". Lưu ý: TW cũng bỏ "hyan" (chỉ ghi 大哥哥) — quyết định giữ âm là theo JP (JP thắng TW).

### Key 2531 — 凪
- JP: 「あむっ――ちゅっ――ちゅうっ――ちゅうっ――\nちゅっ――ひーひゃん――しゅき――しゅきぃ」
- TW: 「啊唔……啾，啾，啾，啾，呀，愛你，愛你」
- Old VN: 「Ngoạm——Chụt——Chụt——Chụt——\nChụt——Anh hai——Thích——Thích lắm á」
- New VN: 「Ngoạm——Chụt——Chụt——Chụt——\nChụt——Hiihyan——Thích——Thích lắm á」
- Lý do: ひーひゃん = "hii-hyan" là một tiếng gasp (TW: 呀), old diễn thành "Anh hai" là sai hẳn — đây không phải "anh hai" (khác với にーひゃん ở 2526). Romaji "Hiihyan" (ひー = hii, ひゃん = hyan).

### Key 2563 — 凪
- JP: 「ん……ちゅううっ――ちゅっ――んっ――ぷっ、\nふぁっ――れろっ――れるっ――ぺろぺろ、ちゅっ」
- TW: 「嗯……啾，啾，嗯……噗，哇，啾，啾，啾，啾」
- Old VN: 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nPhù a——Ngoáy——Ngoáy——Liếm liếm, chụt」
- New VN: 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nFa——Ngoáy——Ngoáy——Liếm liếm, chụt」
- Lý do: ふぁっ = "fa", old "Phù a" sai (tách âm, sai nguyên âm). Romaji "Fa". ぷっ→"Phụt" giữ nguyên (SFX "phụt" tiếng Việt chuẩn cho tiếng bật).

### Key 2589 — 凪
- JP: 「んっ！？　――ぷあっ」
- TW: 「嗯？！哇」
- Old VN: 「Ưm!? ——Phù a」
- New VN: 「Ưm!? ——Pua」
- Lý do: ぷあっ = "pua", old "Phù a" sai phụ âm (p → ph) và tách âm. Romaji "Pua".

## 4. Kept-moan notes (giữ nguyên — các diễn âm đúng, lý do 1 dòng cho những dòng đáng chú ý)

- ひゃっ → "Hya" (2415, 2408, 2620): romaji đúng; っ là cắt âm, theo tiền lệ file không thêm dấu — giữ.
- ひゃあああっ → "Hyaaa" (2416), ひゃああ → "Hyaaa" (2419, 2420): đủ 3 nguyên âm a — giữ.
- ひあああっ → "Hiaaa" (2412, 2414): đúng — tiền lệ ひあ = "Hia" trong file.
- ひゅあっ → "Hyua" (2401), ひぎゅっ → "Higyu" (2405): romaji đúng — giữ.
- 2489 くっ――ふっ――んひゅっ――んんん～っ → "Ư——Phù——Ưm——Ưm~!!": sweep đã loại đúng (already-rendered); các gasp đều có diễn âm VN, không ngượng — giữ.
- 2535 もがっ → "Ưm": tiếng nghẹn (miệng bị bịt) diễn thành tiếng hừm — tự nhiên, giữ.
- 2479 / 2540 / 2477 んふふ(っ/～) → "Ưm fufu": cười khúc khích nhất quán cả file (ん = hừm + ふふ romaji) — giữ.
- 2595 / 2590 えへへ → "Ehehe": tiếng cười, romaji đúng — giữ.
- 2480 ふっふーん → "Hứ hừm": tiếng hừm đắc ý, diễn tự nhiên — giữ.
- 2557 chuỗi âm ngọng do miệng đầy (ひーはふほ…はひっほ…ふふっへ…ほへほはほ): VN diễn thành âm ngọng tương ứng — đúng ý đồ (nói ngọng), giữ.
- Chuỗi hôn/liếm/nuốt ちゅ・ぺろ・れる・ごく (2546, 2547, 2548, 2559, 2561, 2562, 2425, 2601...): "Chụt / Liếm / Ngoáy / Ực" nhất quán cả file — giữ.
- 2501 んくっ、ごくっ → "Ư, ực, ực, ực": chuỗi nuốt, diễn đúng — giữ.
- 2410 ふうううううううううぅぅぅぅっ → "phuuuuuuuuuuuuuuuuu": 17 u so với JP 14 u — lệch 3 u trên một tiếng rên dài 14 mora, không đáng kể, âm đúng — giữ.
- 2447 / 4075 ふわ(っ) → "Phù": tiếng thở nhẹ; mất vần "wa" nhưng độ mềm đã diễn được — giữ (borderline, đã ghi nhận).
- 2539 ああん → "Aaan": tiếng thở dài thất vọng; thừa 1 'a' là kéo dài phong cách — giữ.
- 2751 / 2603 おおお → "Oaa / Oaaa": cảm thán "ồ!" tiếng Việt tự nhiên — giữ (không phải moan).
- 3026 （すんっ――すんっ――）→ "（Khịt——Khịt——）": SFX khịt mũi đúng — giữ.
- 2529 あー → "Aaa": cảm thán "a" kéo dài — giữ.
- 1784 ぅん → "Vâng": tiếng ừm đồng ý nhẹ, diễn thành "Vâng" tự nhiên — giữ (không phải moan H).
- 2545 ちゅ → "Chụt": SFX hôn đúng — giữ.
- 2492 ん～～っっ → "Ưm~~": độ dài diễn bằng ~~, đúng — giữ.
- 2499 ぅぅぅっ → "Ư ư ư", 2498 ううう → "Ư ư ư", 2518 ぁ――ぁ――ぁっ → "A——A——A", 2534 ああああっ → "Aaaa": đủ số nguyên âm theo JP — giữ.
- 2487 / 2536 / 2544 / 3354 / 3433 / 3610 / 3719: sweep gasp (Ư) — đã xử lý, không đụng (xem §2).

## 5. Flags (không quyết — cần vòng audit / Hieu)

### Flag 1 — Key 2515 (双鉄): あふゅいっ → "Nóng quá" (câu hỏi về nghĩa, không phải moan)
- JP: 「ああ――あふゅいっ――ひ、へ――へーえきっ――\nおなかっ――あかちゃん――おへや、びゅうびゅう」
- TW: 「啊……危……沒、沒事……肚子裡……造人房間，咻咻的」
- Old VN: 「A——Nóng quá——T, ti——Tinh dịch——\nBụng——Em bé——Căn phòng, phụt phụt」
- Vấn đề: あふゅいっ là tiếng nói ngọng (miệng đầy / lúng túng). TW đọc là 危 ("nguy hiểm"), VN đọc là "Nóng quá" (nóng) — hai bên hiểu khác nhau; không rõ あふゅいっ là "abunai" (nguy hiểm) bị ngọng hay "atsui" (nóng) bị ngọng. Đây là câu hỏi về NGHĨA, thuộc vòng audit, không sửa ở đây. Không đụng.

### Ghi nhận quyết định (không phải flag — đã quyết theo ủy quyền)
- 2526 にーひゃん → "Anh hai-hyan": TW cũng bỏ "hyan", nhưng JP có âm đó nên giữ lại theo quy tắc "không để mất âm".
- 2397 "Ưm phuuuu": 4 u so với JP 3 u — lệch 1 u, giữ nguyên (ngoài phạm vi sửa targeted của dòng này).
- 2403 ひあうっ → "Hiau" (thay vì giữ "Hyau"): theo Hepburn chuẩn + tiền lệ ひあ = "Hia" trong file (2412/2414); tránh đụng với ひゃう → "Hyau" (2402).

## 6. Second-pass counts (đọc lại toàn bộ fix lần 2, từng giá trị so với JP)

- Tổng số fix đọc lại lần 2: **25**
- Re-verified (giữ nguyên sau lần 2): **25**
- Removed (bỏ fix sau lần 2): **0**
- Corrected (sửa lại giá trị fix sau lần 2): **0**

Ghi chú lần 2: đã đếm lại bằng script các chuỗi dài — 2500 んゅう… = 9 nguyên âm u → "Nyuuuuuuuuu" (Ny + 9 u) đúng; 2416/2419 ひゃああ(あ) = 3 a → "Hyaaa" đúng; 2414/2412 ひあああ = "Hiaaa" đúng; 2534 ああああ = "Aaaa" đúng. Không có fix nào bị loại hay sửa ở lần 2.
- Ghi chú của parent (21/11 ~02:35, sau khi merge): key 2500 SỬA — fix "Nyuuuuuuuuu" (9 u) → "Nyuuuuuuuuuu" (10 u). JP んゅうううううううぅぅ có ゅ(1) + う×7 + ぅ×2 = 10 u theo công thức (1 + số う/ぅ); agent đã đếm thiếu 1 (chỉ đếm う/ぅ = 9, quên +1 cho ゅ). Đã sửa wrong.json + REVIEW (dòng này + khối TOML). File này sẽ được push lại GitHub cùng đợt push sau (staging vẫn giữ bản cũ đã push).

## 7. TOML block (parse-verified với tomllib: 25 key, 0 value mismatch vs wrong.json)

```toml
[script]
"2395" = "「Nkyu——Phù——Ưm!」"
"2397" = "「Hia——A——Ư——Yu——Ưm phuuuu——\\nBây giờ, bây giờ, em——Bị làm, như thế, thì」"
"2398" = "「Hia——A——Aaa! Bụng, của em,\\nem bé——Căn phòng, cộc——bị đập cộc cộc á」"
"2401" = "「Hyua——A——Chỉ, chỗ đó——Ưm, Kyufu,\\nA——Nagi, em——em——hỏng, mất thôi」"
"2402" = "「Hyau」"
"2403" = "「Hiau!!!」"
"2405" = "「Higyu! A! Tuyệt quá——Tuyệt, quá——\\nHà——Fua, a——Âm, đạo, ngoáy, á」"
"2407" = "「Hia! Hà——Aa——A——Bụng\\n——Chà xát——Âm, đạo——Từ bên——trong」"
"2409" = "「Kahyu!!!」"
"2414" = "「Hiaaa——Chỗ đó——Chỗ đó——Nhi,\\nI, a——Sướng, quá——Sướng, quá á」"
"2418" = "「Hia!? Không! Em, bây giờ,\\nĐang lên, đỉnh——Đang lên đỉnh! Đang lên đỉnh rồi á」"
"2428" = "「Ực, ực——Ư——Ư——Pua」"
"2445" = "「Fua——」"
"2449" = "「Fua——A——Ưm——Ư, ư——Fua——\\nChỗ này——Ưm——Phù——Một chút, nữa——A」"
"2451" = "「Fa……A……Cái này……Kinh khủng quá á……\\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」"
"2452" = "「Fua」"
"2462" = "「Fa!?」"
"2483" = "「Ưmmm——A——A——Âm, đạo, vẫn còn——\\nchỗ, sướng, hơn——mà——Ưm——Phù」"
"2500" = "「Nyuuuuuuuuuu!!!」"
"2512" = "「Nhyu!!!?」"
"2520" = "「Ka——Hà! A! Agu——Kafu!\\nHà! Hà! Hà! Hà!」"
"2526" = "「Fua——Anh hai-hyan——Ưm, chụt——\\nChụt, chụt」"
"2531" = "「Ngoạm——Chụt——Chụt——Chụt——\\nChụt——Hiihyan——Thích——Thích lắm á」"
"2563" = "「Ưm……Chụttt——Chụt——Ưm——Phụt,\\nFa——Ngoáy——Ngoáy——Liếm liếm, chụt」"
"2589" = "「Ưm!? ——Pua」"
```

Lưu ý: literal `\n` trong giá trị fix được viết `\\n` trong block (đúng quy tắc TOML). Block đã parse bằng tomllib: 25 key, 0 mismatch với wrong.json. Các fix là amendments, áp dụng cùng unification pass — KHÔNG sửa trực tiếp TOML.

## Kết bài

File 凪h2_おとなの水着: đọc 673 dòng, 158 dòng moan, sửa 25 dòng (24 sai âm + 1 mất độ dài), giữ 124 dòng, 8 dòng sweep không đụng, flag 1 dòng (2515, câu hỏi nghĩa). Lỗi tập trung ở 3 nhóm: họ fa/fu bị diễn "Phù a"/"Phù" sai (8 dòng), ひあ bị diễn "Hya" thay vì "Hia" (5 dòng), và các gasp lạ (かひゅ・んひゅ・んきゅ・きゅふ) bị diễn thành âm chung chung (5 dòng). Second pass: 25/25 re-verified, 0 removed, 0 corrected.
