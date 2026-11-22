# Unification — §6 file-specific DECIDED (batch U10)

**Phạm vi:** §6 F1, F2, F4, F6–F15, F26, F28, F29, F31, F34–F38 của `UNIFICATION-LIST.md`.
**Không đụng:** F17–F24 (Niiroku/tsuika — batch khác), F30 (batch riêng).
**Nguồn:** CSV3 good-set (87.833 dòng; 10 file dual-set đã loại bộ stale theo `dual-csv-sets.md`),
`audit-*-wrong.json` (9.243 mục), `moans/moan-*-wrong.json` (1.535 mục), TOML-2 (kiểm chứng
trực tiếp các dòng ngoài `[script]` và các dòng CSV3 thiếu).

## Phương pháp

- Mỗi key được tra trong CSV3 good-set (JP/TW/VN) + toàn bộ audit/moans fix list.
- `old_vn` theo quy ước bắt buộc: giá trị moan nếu key có trong moan list, nếu không thì giá trị
  audit fix, nếu không thì VN CSV3. Ngoại lệ duy nhất: F29 (hủy fix audit → `fix` = giá trị
  CSV3 trước audit, `old_vn` = giá trị audit bị hủy); F11/F28 (xem từng mục).
- Mọi fix đều viết tay sau khi đọc JP (+TW + 3–5 dòng kề). Không sửa bulk bằng script; script
  chỉ dùng để tra cứu, lắp khối TOML và kiểm chứng cơ học (diff từng fix so với `old_vn`:
  mọi fix chỉ khác ở đúng chỗ cần sửa).
- Các dòng `[characters]` / `[character_subs]` không có trong CSV3 — kiểm chứng trực tiếp
  trong TOML-2 (cả `# JP:` comment phía trên) và quét toàn bộ 216 file TOML để đối chiếu.

## F1. ハチロク06_のぞみ 1660 — 博太 → "Hakata"

- **File:** `ハチロク06_のぞみ.txt.toml`, key `1660`, [script], nhân vật 真闇.
- **JP:** 「……博太によーさん観光にきよる海外のお客さんば、\n九洲全土に、おまねきできるかもしれんねぇ」
- **TW:** 「……說不定就能讓那些專程來參觀博多２３景的國外旅客，對九州全域產生興趣」
- **old_vn (CSV3, không có trong audit/moans):** 「……Những vị khách nước ngoài đến Hakuta du lịch,\ncó khi sẽ được mời đi tham quan toàn bộ Kyushu luôn đó nha」
- **fix:** 「……Những vị khách nước ngoài đến Hakata du lịch,\ncó khi sẽ được mời đi tham quan toàn bộ Kyushu luôn đó nha」
- **Lý do:** JP 博太 là cách viết lệch của 博多; TW đọc 博多 (Hakata) — quyết 20/11 ~17:50.
  Chỉ đổi Hakuta → Hakata, giữ nguyên phần còn lại.

## F2. 日々姫10 2464 — đúng 1 dòng "Vâng!"

- **File:** `日々姫10_稀咲の未来図、日々姫の未来図.txt.toml`, key `2464`, [script], nhân vật 凪.
- **JP:** 「うんっ！」 (đúng 1 dòng)
- **TW:** 「嗯！」\n「嗯！」 (TW nhân đôi — lỗi TW, JP chỉ 1 dòng)
- **old_vn (CSV3, không có trong audit/moans):** 「Vâng!」\n「Vâng!」
- **fix:** 「Vâng!」
- **Lý do:** JP thắng TW; quyết 20/11 ~17:50 — 1 dòng, không nhân đôi.

## F4. 仲国05 — gasp Ư (1956/2254), 1926, 3303

### F4a. 1956 — thêm Ư

- **File:** `仲国05_真夜中の餐車.txt.toml`, key `1956`, [script], nhân vật 西瓜.
- **JP:** 「あ――あ――あ――ああっ」
- **TW:** 「啊——啊——啊——啊啊」
- **old_vn (CSV3, không có trong audit/moans):** 「A――A――A――A.」
- **fix:** 「A――A――A――AƯ.」
- **Lý do:** っ cuối tuyệt đối gắn với từ âm thanh ああ → gasp theo quyết 20/11 ~17:50
  (ranh giới gasp: Ư chỉ khi っ mất hoàn toàn — ở đây VN "A." không còn dấu vết っ).
  Thêm Ư trước dấu chấm, giữ nguyên phần còn lại.

### F4b. 2254 — thêm Ư

- **File:** `仲国05_真夜中の餐車.txt.toml`, key `2254`, [script], nhân vật ハチロク.
- **JP:** 「西瓜は……西瓜はすごいなと。\nよくこれほどの……これほどの――はうっ」
- **TW:** 「西瓜她……西瓜她真厲害。她居然……居然受得了這樣——呼～」
- **old_vn (CSV3, không có trong audit/moans):** 「Suika……Suika thật tuyệt vời.\nVậy mà có thể chịu đựng được mức độ……mức độ này――ha.」
- **fix:** 「Suika……Suika thật tuyệt vời.\nVậy mà có thể chịu đựng được mức độ……mức độ này――haƯ.」
- **Lý do:** như 1956 — はうっ là từ âm thanh + っ cuối, thêm Ư (quyết 20/11 ~17:50).
  Chỉ thêm Ư, không sửa "ha" (quyết chỉ nói thêm Ư).

### F4c. 1926 — "toa thứ hai tính từ cuối đoàn"

- **File:** `仲国05_真夜中の餐車.txt.toml`, key `1926`, [script], nhân vật 日々姫.
- **JP:** 「よね、お尻から二両目やけん、さすがにちょこっと\n衝動出たけど――これ、前の客車は無衝動でしょ」
- **TW:** 「可不是，這可是車尾倒數第二節，還是出現了一丁點縱向衝動——但前面的客運車廂應該是完全沒有的吧」
- **old_vn (CSV3, không có trong audit/moans):** 「Đúng á, vì là toa thứ hai từ dưới đếm lên nên\ncó hơi chấn động một chút――nhưng các toa hành khách phía trước chắc là êm ru luôn ha.」
- **fix:** 「Đúng á, vì là toa thứ hai tính từ cuối đoàn nên\ncó hơi chấn động một chút――nhưng các toa hành khách phía trước chắc là êm ru luôn ha.」
- **Lý do:** お尻から二両目 = toa thứ hai tính từ cuối đoàn (đuôi tàu); "từ dưới đếm lên"
  vừa khó hiểu vừa sai hướng đếm. TW 車尾倒數第二節 đồng ý.

### F4d. 3303 — とっ → "(Cộp)"

- **File:** `仲国05_真夜中の餐車.txt.toml`, key `3303`, [script], monologue.
- **JP:** （とっ）
- **TW:** （然後）
- **old_vn (CSV3, không có trong audit/moans):** (Phịch)
- **fix:** (Cộp)
- **Lý do:** とっ là tiếng gõ/chạm nhẹ, khác どさっ (3280, giữ "(Phịch)" — không đụng).
  Hai dòng trước đây cùng "(Phịch)" nay đã phân biệt.

## F6. ふかみh2 1513 — "Đầu ngón tay tôi"

- **File:** `ふかみh2_homesweethome.txt.toml`, key `1513`, [script], monologue.
- **JP:** 飛びつくようにおまんこへ届いた指先が、\nさすさすと、縦スジに沿って動き始める。
- **TW:** 於是我立刻將手伸上前去，沿著豎線開始活動。 (TW 我 = tay của người kể)
- **old_vn (CSV3; không có trong audit/moans):** Đầu ngón tay em ấy vội vã chạm vào âm đạo,\nbắt đầu xoa xoa dọc theo đường rãnh.
- **fix:** Đầu ngón tay tôi vội vã chạm vào âm đạo,\nbắt đầu xoa xoa dọc theo đường rãnh.
- **Lý do:** monologue của Soutetsu; ngón tay là của Soutetsu (TW 我; quyết 21/11 ~01:55;
  dòng 1509 cùng ngón tay đó). Chỉ đổi "em ấy" → "tôi".

## F7. ふかみh2 1096 — "Migitaichi" → "Migita Ichi"

- **File:** `ふかみh2_homesweethome.txt.toml`, key `1096`, [script], nhân vật ふかみ.
- **JP:** 「[みぎたいちしゅぞうもと,5]右田一酒造元の……真闇さんの前の、[とうじ,1]杜氏さん？」
- **TW:** 「是右田一釀酒廠的……真闇小姐之前的掌窖？」
- **old_vn (CSV3; không có trong audit/moans):** 「Là Toji……trước chị Mayami, của nhà máy rượu Migitaichi sao?」
- **fix:** 「Là Toji……trước chị Mayami, của nhà máy rượu Migita Ichi sao?」
- **Lý do:** ruby みぎたいち = 右田一 = "Migita Ichi" (quyết 21/11 ~01:55; T14).
  Lưu ý: key 1096 trong file `lr_ふかみh2` là dòng khác (moan "Nhyu!!!?") — không nhầm.

## F8. 仲国06 1412 — "Nhân giống"

- **File:** `仲国06_聖都とパンダとハチロクと.txt.toml`, key `1412`, [script], nhân vật 志寰.
- **JP:** 「国内外を問わず、観光客が聖都で一番訪れる場所が、\n聖都の、[ぱんだはんしょくきち,10]大熊猫保存研究中心基地です」
- **TW:** 「不管是來自國內還是國外，大熊貓繁育研究基地是所有來盛都遊客遊覽最多的景點」
- **old_vn (CSV3, không có trong audit/moans):** 「Dù là khách trong hay ngoài nước, địa điểm được ghé thăm nhiều nhất ở Thịnh Đô,\nchính là Cơ sở Nghiên cứu Bảo tồn Gấu trúc lớn Thịnh Đô.」
- **fix:** 「Dù là khách trong hay ngoài nước, địa điểm được ghé thăm nhiều nhất ở Thịnh Đô,\nchính là Cơ sở Nghiên cứu Nhân giống Gấu trúc lớn Thịnh Đô.」
- **Lý do:** ruby はんしょく = 繁殖 (nhân giống) thắng kanji 保存 (bảo tồn); TW 繁育 + địa danh
  thực 成都大熊猫繁育研究基地 đều đồng ý (quyết 21/11 ~18:15). Chỉ đổi "Bảo tồn" → "Nhân giống".

## F9. 真闇02 2793 — SFX "Phụt" → "Kéo"

- **File:** `真闇02_精髄.txt.toml`, key `2793`, [script], monologue.
- **JP:** （くっ――くいっ）
- **TW:** （拉——拉） (= kéo——kéo)
- **old_vn (CSV3; audit giữ nguyên kèm cờ, không có trong audit/moans fix list):** （Phụt——Phụt）
- **fix:** （Kéo——Kéo）
- **Lý do:** くいっ là tiếng kéo/giật (kéo tay gạt van); "Phụt" gợi tiếng phụt chất lỏng, sai
  (quyết 21/11 ~18:55; audit file `audit-mayami02-seisui` đã cờ sẵn dòng này).

## F10. 凪ふかみ01_流れ 1691 — "mình" → "tôi"

- **File:** `凪ふかみ01_流れ.txt.toml`, key `1691`, [script].
- **JP (CSV3, 07_Nagi_Fukami):**
  「そうだ。\nどうしてこんな単純なことに気がつかなかったのだ」
- **TW:** 「是啊。為什麼這麼單純的事情我就沒注意到呢」
- **old_vn (CSV3 VN — giá trị chuẩn; không có trong audit/moans fix list):**
  「Đúng vậy.\nTại sao mình lại không nhận ra một điều đơn giản như thế chứ.」
- **fix:** 「Đúng vậy.\nTại sao tôi lại không nhận ra một điều đơn giản như thế chứ.」
- **Lý do:** Soutetsu tự vấn THÀNH TIẾNG với Hachiroku — dòng trước 1689 là Hachiroku nói
  với Soutetsu ("nếu anh bắt được em…"), dòng sau 1692 「ああ」 là Hachiroku đáp lại.
  Đây là thoại, không phải độc thoại nội tâm, nên ngoại lệ "mình" không áp dụng; quy tắc
  chung "tôi" (quyết 21/11 ~18:55). Chỉ đổi "mình" → "tôi".
- **Ghi chú (sửa bởi coordinator):** bản nháp đầu ghi nhầm "CSV3 thiếu dòng này" — thực tế
  dòng 1691 CÓ trong CSV3 (07_Nagi_Fukami, 1 dòng duy nhất, không dual-set). JSON đã sửa:
  TW lấy từ CSV3; old_vn/fix lấy theo CSV3 (giữ nguyên `\n`, không dùng bản TOML-2 đã
  flatten `\n` thành khoảng trắng).

## F11. 日々姫02_日々姫の日々 1906/2325 — khôi phục "nuôi" (ĐẢO NGƯỢC 2 fix audit)

- **File:** `日々姫02_日々姫の日々.txt.toml` (cả hai key đều ở file này — key 2325 trong
  `日々姫02_文庫森.txt.toml` là dòng monologue khác về bấm máy ảnh, không phải dòng này).

### F11a. 1906 — "anh trai" → "anh trai nuôi"

- **JP:** 「それなら――[あに,1]義兄としてありがたい」
- **TW:** 「你能這麼說，作為哥哥我也很高興」
- **old_vn (= giá trị audit fix đang bị hủy):** 「Vậy thì——với tư cách là anh trai, tôi rất biết ơn.」
- **fix (= giá trị CSV3 trước audit):** 「Vậy thì——với tư cách là anh trai nuôi, tôi rất biết ơn.」
- **Lý do:** JP 義兄 + quyết 義 = "nuôi" đã chốt 21/11 ~19:45 (Soutetsu là con nuôi,
  養子 — 共通10 2573; TW 養父/養母 ~40 dòng). Audit đã gỡ "nuôi" vì cho là bịa (theo
  cảnh báo cũ trong skill — nay đã bị quyết 19:45 thay thế); đợt này khôi phục lại.

### F11b. 2325 — "em gái" → "em gái nuôi"

- **JP:** 「無論だ。大事な[いもうと,1]義妹であるし、\n僕の帰り道も同じだからな」
- **TW:** 「這還用說。她可是我重要的妹妹，而且我們回去也同路」
- **old_vn (= giá trị audit fix đang bị hủy):** 「Tất nhiên rồi. Là cô em gái quan trọng của tôi mà,\nvới lại đường về của tôi cũng là đường đó.」
- **fix (= giá trị CSV3 trước audit):** 「Tất nhiên rồi. Là cô em gái nuôi quan trọng của tôi mà,\nvới lại đường về của tôi cũng là đường đó.」
- **Lý do:** như 1906 — JP 義妹 → "em gái nuôi".

## F12. lr_日々姫真闇h1 2003/2005/2082 — "cô em gái" → "cô em gái nuôi"

- **File:** `lr_日々姫真闇h1_三人家族.txt.toml`, [script], monologue. Cả 3 key đều không có
  trong audit/moans fix list → `old_vn` = VN CSV3. (Cột TW của file này có chỗ bị lệch —
  đã quyết theo JP + dòng kề; ở 3 key này TW 繼姐繼妹 vẫn khớp JP 義姉/義妹.)

### F12a. 2003

- **JP:** 水着を脱ぎ捨て突き立てている。大事な義姉と義妹が、\n裸のおっぱいを合わせつくった、淫猥すぎるその空隙に。
- **TW:** 我重要的繼姐繼妹的兩對乳房貼在一起的景象太過淫猥，我一把脫去泳褲，把高高豎起之物對準夾縫就是一頂。
- **old_vn:** Tôi cởi phăng đồ bơi và đâm mạnh vào. Vào khe hở vô cùng dâm đãng\nđược tạo ra khi cô em gái và người chị nuôi quan trọng của tôi ép chặt hai bộ ngực trần vào nhau.
- **fix:** Tôi cởi phăng đồ bơi và đâm mạnh vào. Vào khe hở vô cùng dâm đãng\nđược tạo ra khi cô em gái nuôi và người chị nuôi quan trọng của tôi ép chặt hai bộ ngực trần vào nhau.
- **Lý do:** JP 義姉と義妹 — cả hai đều là 義; VN cũ chỉ gắn "nuôi" cho chị mà quên em gái.

### F12b. 2005

- **JP:** ゆえに見る。日々姫と真闇姉――僕の大切な義妹と義姉との、\nおんなじ色で、形の違う、おっぱいを。
- **TW:** 所以我要正視她們。好好看看日日姬和真闇姐——我心愛的繼姐繼妹的，那兩對膚色一致，然而形狀各異的胸部。
- **old_vn:** Thế nên tôi nhìn. Nhìn bộ ngực của Hibiki và chị Mayami――của cô em gái và người chị nuôi quan trọng của tôi,\ncùng một màu sắc, nhưng lại có hình dáng khác nhau.
- **fix:** Thế nên tôi nhìn. Nhìn bộ ngực của Hibiki và chị Mayami――của cô em gái nuôi và người chị nuôi quan trọng của tôi,\ncùng một màu sắc, nhưng lại có hình dáng khác nhau.
- **Lý do:** như 2003 — JP 義妹と義姉.

### F12c. 2082

- **JP:** 日々姫と真闇姉が、一緒に暮らす大切な義妹と義姉とが、\n僕の射精を促すために、お互いの胸をもみ合っている。
- **TW:** 日日姬和真闇姐，跟我一起生活，我最心愛的繼妹繼姐，為了讓我射精，互相搓揉著對方的胸脯。
- **old_vn:** Hibiki và chị Mayami, cô em gái và người chị nuôi quan trọng cùng sống chung dưới một mái nhà,\nđang xoa bóp ngực nhau để thúc giục tôi xuất tinh.
- **fix:** Hibiki và chị Mayami, cô em gái nuôi và người chị nuôi quan trọng cùng sống chung dưới một mái nhà,\nđang xoa bóp ngực nhau để thúc giục tôi xuất tinh.
- **Lý do:** như 2003 — JP 義妹と義姉.

## F13. ポーレット14 2402 — "Là em gái nuôi."

- **File:** `ポーレット14_ふたたび走り出すために.txt.toml`, key `2402`, [script], monologue.
- **JP:** なにせ、家族だ。[いもうと,1]義妹だ。\n細かな事情の説明は、最後回しにさせてもらった。
- **TW:** 畢竟日日姬是自家人。我沒有太著急把事情的細節告訴她。
- **old_vn (CSV3, không có trong audit/moans):** Dù sao thì, cũng là người nhà. Là em gái.\nNên tôi để phần giải thích chi tiết hoàn cảnh lại sau cùng.
- **fix:** Dù sao thì, cũng là người nhà. Là em gái nuôi.\nNên tôi để phần giải thích chi tiết hoàn cảnh lại sau cùng.
- **Lý do:** JP 義妹 → "em gái nuôi" (quyết 21/11 ~19:45). Chỉ thêm "nuôi".

## F15. 日々姫h5 1189 — bỏ "đã bao phủ" (diễn cụt theo JP)

- **File:** `日々姫h5_白濁絵の具の射精会.txt.toml`, key `1189`, [script], nhân vật 日々姫.
- **JP:** 「はぁ……ぁっ――うれし――うれし――ぃ――\nにぃにの――えのぐで――わたし――全部、がっ」
- **TW:** 「呼……啊――我好開心――好開心――阿哥的――顏料――全射了出來」
- **old_vn (CSV3; không có trong audit/moans):** 「Hà……a――Vui quá――vui quá――đi――\nMàu vẽ――của anh hai――đã bao phủ――toàn bộ, người em」
- **fix:** 「Hà……a――Vui quá――vui quá――đi――\nMàu vẽ――của anh hai――người em――toàn bộ――」
- **Lý do:** JP kết giữa câu ở がっ (không có động từ hoàn thiện); "đã bao phủ" là phần
  bịa thêm. Dòng kề 1190 là dòng rên mới (ふあ……ぁ……ア……), không phải phần tiếp nối.
  Quyết 22/11 ~02:47: bỏ phần bịa, diễn cụt theo JP (giữ nguyên thứ tự JP:
  にぃにの――えのぐで――わたし――全部 → của anh hai――màu vẽ――người em――toàn bộ――).

## F26. 凪ふかみ07 2208–2215 (+2218) — Fukami tự xưng → "tớ"

- **File:** `凪ふかみ07_少しずつ、大人に.txt.toml`, [script], nhân vật ふかみ (cả 6 dòng).
  Không có key nào trong audit/moans fix list → `old_vn` = VN CSV3.
- **Bối cảnh đã kiểm chứng:** trao đổi với Nagi — 2209 nêu tên 凪ちゃん ("Nagi xấu tính quá!");
  2212 nhắc 双鉄おにいさん ở ngôi thứ ba; các dòng kề 2200/2205/2216 là Soutetsu.
  Cặp cùng tuổi Fukami/Nagi dùng tớ–cậu; "chị"/"em" đều vi phạm quy tắc đã chốt P9
  (quyết 21/11 ~17:30). JP cả 6 dòng đều là わたし (tự xưng ngôi thứ nhất).
- **2208 đã là "tớ" — không sửa** (xem mục Giữ nguyên). **2210/2211/2214 không tồn tại**
  (không có trong CSV3 lẫn TOML-2 — khoảng trống key) — không có dòng nào để sửa.

### F26a. 2209 — "em" → "tớ" (2 chỗ)

- **JP:** 「わ、わたし！　悪だくみなんてしないもんっ！\nもう、凪ちゃんのいじわるっ！」
- **TW:** 「我、我才沒耍奸計！討厭，小凪欺負人！」
- **old_vn:** 「E, em! Em không có âm mưu đen tối gì đâu nhé!\nThật tình, Nagi xấu tính quá!」
- **fix:** 「E, tớ! Tớ không có âm mưu đen tối gì đâu nhé!\nThật tình, Nagi xấu tính quá!」

### F26b. 2212 — "chị" → "tớ"

- **JP:** 「そんなの、わたしだってだよ！　双鉄おにいさんに、\nいつだって甘えて、支えてもらって――」
- **TW:** 「我也一樣啊！　我總是依靠著雙鐵哥哥」
- **old_vn:** 「Chuyện đó, chị cũng vậy mà! Lúc nào cũng\nnũng nịu, và được anh Soutetsu giúp đỡ――」
- **fix:** 「Chuyện đó, tớ cũng vậy mà! Lúc nào cũng\nnũng nịu, và được anh Soutetsu giúp đỡ――」

### F26c. 2213 — "Em" → "Tớ"

- **JP:** 「わたしも、です」
- **TW:** 「我也是」
- **old_vn:** 「Em cũng vậy, ạ.」
- **fix:** 「Tớ cũng vậy, ạ.」

### F26d. 2215 — "Em"/"em" → "Tớ"/"tớ" (2 chỗ)

- **JP:** 「わたしも、おんなじ気持ちです。双鉄おにいさんが\n笑ってくれれば――どこにいたって、楽しい、です」
- **TW:** 「我也是這麼想的。只要雙鐵哥哥能露出笑容，不管去哪裡，我都很開心，嗯」
- **old_vn:** 「Em cũng có cùng cảm giác đó. Chỉ cần anh Soutetsu\nmỉm cười――thì dù ở đâu, em cũng thấy vui, ạ.」
- **fix:** 「Tớ cũng có cùng cảm giác đó. Chỉ cần anh Soutetsu\nmỉm cười――thì dù ở đâu, tớ cũng thấy vui, ạ.」

### F26e. 2218 — "em" → "tớ" (2 chỗ)

- **JP:** 「お客さんのときはあんまり意識してなかったけど――\n黄色い線、踏まれるの怖いって思うようになりました」
- **TW:** 「我以前只是一名普通乘客的時候，都沒有放在心上——但現在變得不敢踩到黃線了」
- **old_vn:** 「Hồi còn là hành khách em không để ý lắm――\nNhưng giờ em đã thấy sợ khi có người giẫm lên vạch vàng rồi.」
- **fix:** 「Hồi còn là hành khách tớ không để ý lắm――\nNhưng giờ tớ đã thấy sợ khi có người giẫm lên vạch vàng rồi.」

## F28. 凪ふかみ03 2058 — "trưởng tàu đại lý" → "trưởng tàu đại diện"

- **File:** `凪ふかみ03_みかんの旅.txt.toml`, key `2058`, [script], nhân vật 双鉄.
- **JP:** 「つまり、君は代理車掌か」
- **TW:** 「也就是說，你是代理列車長？」
- **old_vn (= giá trị audit fix hiện tại):** 「Nói cách khác, em là trưởng tàu thay thế sao.」
- **fix:** 「Nói cách khác, em là trưởng tàu đại diện sao.」
- **Lý do:** 代理 = acting/representative → "trưởng tàu đại diện" (quyết 21/11 ~17:30).
  Lưu ý: audit đã sửa "đại lý" → "thay thế"; đợt này đổi "thay thế" → "đại diện" theo
  đúng thuật ngữ đã chốt (không phải sửa lại từ "đại lý" — `old_vn` trong JSON là giá trị
  audit hiện tại, đúng quy ước).

## F29. ふかみh1 979/1043 — HỦY 2 fix audit, giữ "Kh"/"kh"

- **File:** `ふかみh1_ともはり練習.txt.toml`, [script], nhân vật 双鉄H. Cả hai key đều
  không có trong moan list → `old_vn` = giá trị audit fix bị hủy; `fix` = giá trị CSV3
  trước audit. Lý do chung: quy tắc "Kh" đã khóa (§3 M6) — っ tắc thanh diễn thành "Kh",
  không bao giờ thống nhất thành Ư; hai fix audit xung đột quy tắc này.

### F29a. 979 — "Ư——" → "Kh——"

- **JP:** 「っ――」
- **TW:** 「呃……」
- **old_vn (= audit fix):** 「Ư——」
- **fix (= CSV3):** 「Kh——」

### F29b. 1043 — "ƯƯ" → "kh"

- **JP:** 「ん……っっ――んっ――ふっ――んっ」
- **TW:** 「嗯……呼……嗯……呼……嗯」
- **old_vn (= audit fix):** 「Ưm……ƯƯ——ưm——phù——ưm」
- **fix (= CSV3):** 「Ưm……kh——ưm——phù——ưm」
- **Ghi chú:** chỉ hoàn lại đúng đoạn "ƯƯ" → "kh"; các Ưm/phù còn lại giữ nguyên
  (chúng diễn các âm khác, không phải っ tắc thanh này).

## F36. [characters] / [character_subs] 'Olive' → "Olivy" (6 dòng, 3 file)

- Các dòng này KHÔNG có trong CSV3 (CSV3 chỉ có `[script]`) và không có trong audit/moans
  fix list. Đã kiểm chứng trực tiếp trong TOML-2: giá trị hiện tại là "Olive" ở cả 6 key;
  `# JP:` comment phía trên: オリヴィ ([characters]) / 奥莉薇 ([character_subs]).
  Chính tả đã chốt: **Olivy** (T46). `tw` để trống trong JSON (không có nguồn TW cho
  mapping tên nhân vật).
- **ハチロク15b_さよなら列車.txt.toml:** 1908 [characters] "Olive" → "Olivy";
  2063 [character_subs] "Olive" → "Olivy".
- **グランドリライト09_凪.txt.toml:** 2180 [characters] "Olive" → "Olivy";
  2466 [character_subs] "Olive" → "Olivy".
- **ハチロク02_ハートブレイク・レイルロオド.txt.toml:** 2823 [characters] "Olive" → "Olivy";
  3034 [character_subs] "Olive" → "Olivy".
- **Đính chính cho coordinator:** list ghi "Grand 09 (2823/3034)" nhưng 2823/3034 thực tế
  thuộc về **ハチロク02** (khớp đúng cờ trong ROUTE-AUDIT.md mục ハチロク02:
  "mapping [characters] 2823/3034 = 'Olive'"); các dòng Olive thật của Grand 09 là
  2180/2466 (khớp mục Grand 09 trong ROUTE-AUDIT: "[characters] 2163=Mikuro, 2180=Olive…").
  Batch này sửa cả 6 dòng (2 file theo list + cặp 2823/3034 đúng file của chúng) và ghi rõ
  để coordinator đối chiếu — nếu chỉ muốn đúng 4 dòng theo list thì bỏ cặp ハチロク02.
- **Ngoài phạm vi batch:** quét toàn bộ TOML-2 thấy 'Olive' còn ở ~16 file khác nữa
  (02, 03, 05, 06_のぞみ 2971/3186, 07_延命, 08, 09_もくもくオリヴィ, 10, 11, 12, 13, 14,
  15a, 凪ふかみ03_みかんの旅, グランドリライト11, lr追加_ひよこ電車姫オリヴィ) — để cho
  đợt quét T46, batch này KHÔNG sửa.

## Các mục đã kiểm chứng — GIỮ NGUYÊN, không có dòng JSON

- **F3 — 日々姫10 2595/2715 giữ "chị":** CSV3 "Họa cụ của chị…" / "chị sẽ đơn giản hóa…";
  không có trong audit/moans → giá trị hiện tại đúng, giữ nguyên.
- **F5 — ハチロク06_それぞれの傷跡 1654/1850:** 1654 giá trị hiện tại = audit fix
  "「Anh Soutetsu……」" (JP 「双鉄くんに……」, cụt — giữ); 1850 không có trong audit,
  CSV3 "Từ ngài Soutetsu…… trực tiếp nghe sao." (JP 「双鉄様から……直接に」) — giữ.
- **F14 — ハチロク14_冬 3777: ĐÃ ĐÚNG trong audit fix, không cần dòng unification.**
  Audit fix: "…thì chị chồng và em chồng của em, chắc chắn cũng sẽ lặng lẽ chấp nhận thôi."
  = đúng giá trị đã chốt 21/11 ~19:45 (Hachiroku là vợ Soutetsu; 義姉/義妹 → chị chồng/em chồng).
- **F16 — 日々姫h5 1145/1234:** không có trong audit/moans → CSV3 giữ nguyên:
  1145 "Rút ra, không được, đâu" (JP いったら = "nếu rút ra", TW 不要抽走);
  1234 "anh hai"/"rất thích" (âm ngọng むぃ/らい, TW 哥/最喜歡). Đúng quyết 22/11 ~02:47.
- **F25 — Niiroku01 1563/1907:** không có trong audit → CSV3 giữ nguyên: 1563 "chị Shiro"
  (JP シロおねえちゃん) vs 1907 "chị D60 46" (JP Ｄ６０ ４６おねえちゃん) — JP cố ý đổi, giữ cả hai.
- **F27 — Grand 03 (グランドリライト03_日々姫) 2201:** không có trong audit → CSV3
  "「Của bọn anh sao?」" (JP 「僕らのか？」 — 僕ら gồm Soutetsu nam, đúng) — giữ.
- **F31 — 日々姫h5 1264/1154:** giá trị hiện tại = audit fix, moan pass đồng ý, giữ nguyên:
  1264 "「Nukyu!!!!」" (JP んうきゅっ); 1154 "…Chim――Po――Fua, a――tuyệt, tuyệt quá"
  (JP ぽっ → "Po", ふあっ → "Fua"). Không có mục moan nào khác cho 2 key này.
- **F32 — lr_日々姫真闇h1 1493:** không có trong audit/moans → CSV3 giữ nguyên:
  "――Chị cũng muốn em nhìn…… nhiều như nhìn Hii-chan vậy." (Mayami gọi Soutetsu "em" — giữ).
- **F33 — 凪ふかみ01_流れ 1452/1547/1544:** giá trị hiện tại = audit fix, giữ nguyên:
  1452 "「Phù haaaa——!」", 1547 "「Phuêê.」", 1544 "「Uhyaa」" (đúng công thức mora;
  lưu ý: các key này thuộc file **流れ**, không phải file 成長 cùng tên — file 成長 có các
  key trùng số nhưng JP khác).
- **F34 — 凪h2 2500: giá trị moan đã merge ĐÚNG, không cần sửa.** Đếm bằng máy:
  JP んゅうううううううぅぅっ = ん + ゅ + 7う + 2ぅ → 9 âm う/ぅ; công thức tổng mora
  Hepburn = 1 (んゅ) + 9 = 10u. Giá trị moan trong `moan-nagih2-otona-no-mizugi-wrong.json`:
  "「Nyuuuuuuuuuu!!!」" — đếm máy = đúng 10 chữ u. Ghi nhận là đã kiểm chứng độc lập
  (món nợ kiểm tra trong §6 F34 / §3 M4 đã trả).
- **F35 — Hachiroku 12 (ハチロク12_ムナカタ来訪) 2976: ĐÃ ĐÚNG trong audit fix, không cần dòng.**
  Audit fix: "…Olivy được sản xuất tại Minh Quốc——là một Railord…" (JP 冥国製, TW 美國 —
  JP thắng). CSV3 VN cũ "Meikoku" đã được audit sửa rồi.
- **F37 — ハチロク09_もくもくオリヴィ: 20 dòng thuật ngữ ĐÃ ĐÚNG trong audit fix list,
  đã kiểm chứng từng dòng, không thêm dòng trùng.** Đếm trong
  `audit-hachiroku09-mokumoku-olivy-wrong.json` (34 mục): Ohimitera→Ohitoyo 7
  (1037, 2029, 2835, 1521, 1819, 2116, 2698); Yui→Yunoi 5 (1771, 2831, 2030, 1572, 1006;
  2698 mang cả hai); "Đường sắt Hoàng gia"→Teitetsu 4 (2028, 1645, 1482, 1481);
  Densha Hime→"Công chúa Tàu điện" 2 (2100, 1724); Meriken 1 (1606, furigana メリケン);
  thân bảo trì 1 (1031). Tổng 7+5+4+2+1+1 = 20, khớp list. Các mục còn lại trong file
  (1508 gỡ gloss thừa, 2870/1925/… sai nghĩa, 1648/1675/1678 gasp, 1946/1599 chính tả)
  không thuộc 20 dòng này. Ngoài ra key 2118 (địa danh Yui 由衣) giữ "vùng Yui" theo
  ngoại lệ Yui đã chốt — đã kiểm chứng, không sửa.
- **F38 — ハチロク06_のぞみ 1293: key 1293 KHÔNG TỒN TẠI.** Không có trong CSV3 (file này
  không có key nào trong khoảng 1200–1400), không có trong TOML-2, không có trong
  audit/review của file. Nguồn ghi trong list "ROUTE-AUDIT.md (ハチロク06_のぞみ:1293)"
  thực chất là **số dòng trong ROUTE-AUDIT.md** (mục ハチロク06_のぞみ nằm ở dòng ~1288),
  không phải key script — list đã nhầm số dòng file log thành key. Nội dung gốc thì đúng:
  audit xác nhận "file này dùng 'tôi' nhất quán" cho Soutetsu với Olivy; kiểm chứng mẫu
  key 2459 (JP 「オリヴィ。そのうちわはオリヴィ自身を冷ますものだぞ。\n特に僕などあおがぬでも」,
  VN "…Không cần phải quạt cho tôi đâu") — "tôi" đúng, giữ nguyên. Không có dòng JSON.
- **F26 2208:** đã là "tớ" trong CSV3 ("「T-tớ——à ừm——đâu có……\nFushuuuuuu~~」") — giữ, không sửa.
- **F4 3280:** JP （どさっ） VN "(Phịch)" — giữ theo chỉ đạo, không đụng.

## Ghi chú cho coordinator (các lệch list ↔ nguồn đã phát hiện)

1. **F36:** (2823/3034) thuộc ハチロク02, không phải Grand 09 — xem mục F36. Batch đã sửa
   cả 6 dòng; nếu coordinator chỉ lấy đúng list thì bỏ 2 dòng ハチロク02 (nhưng khi đó cặp
   2823/3034 vẫn còn 'Olive' sai).
2. **F38:** key 1293 không tồn tại (số dòng ROUTE-AUDIT.md bị nhầm thành key) — không có dòng JSON.
3. **F10 1691:** bản nháp ghi nhầm CSV3 thiếu dòng — thực tế có trong CSV3 (07_Nagi_Fukami); coordinator đã sửa JSON theo CSV3 (TW + `\n` trong old_vn/fix).
4. **F14/F35:** đã đúng trong audit fix — batch này ghi nhận kiểm chứng, không tạo dòng trùng.
5. **F28:** `old_vn` là giá trị audit ("thay thế"), không phải "đại lý" như list viết —
   audit đã đổi một lần trước quyết 21/11 ~17:30.

## Lượt soát 2 (second pass)

Đọc lại toàn bộ 32 fix so với JP (lượt riêng, sau khi viết JSON): **tổng 32 / tái kiểm chứng
32 / loại bỏ 0 / sửa lại 0**. Kiểm chứng cơ học kèm theo: mọi fix khác `old_vn` chỉ ở đúng
chỗ cần sửa (diff từng cặp, xem log build); khối TOML parse-verified 17 file / 32 key,
0 sai lệch giá trị (tomllib round-trip).

## Khối TOML (đã parse-verified: 17 file / 32 key, 0 sai lệch)

Literal `\n` trong giá trị được viết `\\n` trong khối; parse lại bằng tomllib cho đúng giá trị gốc.

### lr_日々姫真闇h1_三人家族.txt.toml

```toml
[script]
"2003" = "Tôi cởi phăng đồ bơi và đâm mạnh vào. Vào khe hở vô cùng dâm đãng\\nđược tạo ra khi cô em gái nuôi và người chị nuôi quan trọng của tôi ép chặt hai bộ ngực trần vào nhau."
"2005" = "Thế nên tôi nhìn. Nhìn bộ ngực của Hibiki và chị Mayami――của cô em gái nuôi và người chị nuôi quan trọng của tôi,\\ncùng một màu sắc, nhưng lại có hình dáng khác nhau."
"2082" = "Hibiki và chị Mayami, cô em gái nuôi và người chị nuôi quan trọng cùng sống chung dưới một mái nhà,\\nđang xoa bóp ngực nhau để thúc giục tôi xuất tinh."
```

### ふかみh1_ともはり練習.txt.toml

```toml
[script]
"979" = "「Kh——」"
"1043" = "「Ưm……kh——ưm——phù——ưm」"
```

### ふかみh2_homesweethome.txt.toml

```toml
[script]
"1096" = "「Là Toji……trước chị Mayami, của nhà máy rượu Migita Ichi sao?」"
"1513" = "Đầu ngón tay tôi vội vã chạm vào âm đạo,\\nbắt đầu xoa xoa dọc theo đường rãnh."
```

### グランドリライト09_凪.txt.toml

```toml
[characters]
"2180" = "Olivy"
[character_subs]
"2466" = "Olivy"
```

### ハチロク02_ハートブレイク・レイルロオド.txt.toml

```toml
[characters]
"2823" = "Olivy"
[character_subs]
"3034" = "Olivy"
```

### ハチロク06_のぞみ.txt.toml

```toml
[script]
"1660" = "「……Những vị khách nước ngoài đến Hakata du lịch,\\ncó khi sẽ được mời đi tham quan toàn bộ Kyushu luôn đó nha」"
```

### ハチロク15b_さよなら列車.txt.toml

```toml
[characters]
"1908" = "Olivy"
[character_subs]
"2063" = "Olivy"
```

### ポーレット14_ふたたび走り出すために.txt.toml

```toml
[script]
"2402" = "Dù sao thì, cũng là người nhà. Là em gái nuôi.\\nNên tôi để phần giải thích chi tiết hoàn cảnh lại sau cùng."
```

### 仲国05_真夜中の餐車.txt.toml

```toml
[script]
"1926" = "「Đúng á, vì là toa thứ hai tính từ cuối đoàn nên\\ncó hơi chấn động một chút――nhưng các toa hành khách phía trước chắc là êm ru luôn ha.」"
"1956" = "「A――A――A――AƯ.」"
"2254" = "「Suika……Suika thật tuyệt vời.\\nVậy mà có thể chịu đựng được mức độ……mức độ này――haƯ.」"
"3303" = "(Cộp)"
```

### 仲国06_聖都とパンダとハチロクと.txt.toml

```toml
[script]
"1412" = "「Dù là khách trong hay ngoài nước, địa điểm được ghé thăm nhiều nhất ở Thịnh Đô,\\nchính là Cơ sở Nghiên cứu Nhân giống Gấu trúc lớn Thịnh Đô.」"
```

### 凪ふかみ01_流れ.txt.toml

```toml
[script]
"1691" = "「Đúng vậy.\\nTại sao tôi lại không nhận ra một điều đơn giản như thế chứ.」"
```

### 凪ふかみ03_みかんの旅.txt.toml

```toml
[script]
"2058" = "「Nói cách khác, em là trưởng tàu đại diện sao.」"
```

### 凪ふかみ07_少しずつ、大人に.txt.toml

```toml
[script]
"2209" = "「E, tớ! Tớ không có âm mưu đen tối gì đâu nhé!\\nThật tình, Nagi xấu tính quá!」"
"2212" = "「Chuyện đó, tớ cũng vậy mà! Lúc nào cũng\\nnũng nịu, và được anh Soutetsu giúp đỡ――」"
"2213" = "「Tớ cũng vậy, ạ.」"
"2215" = "「Tớ cũng có cùng cảm giác đó. Chỉ cần anh Soutetsu\\nmỉm cười――thì dù ở đâu, tớ cũng thấy vui, ạ.」"
"2218" = "「Hồi còn là hành khách tớ không để ý lắm――\\nNhưng giờ tớ đã thấy sợ khi có người giẫm lên vạch vàng rồi.」"
```

### 日々姫02_日々姫の日々.txt.toml

```toml
[script]
"1906" = "「Vậy thì——với tư cách là anh trai nuôi, tôi rất biết ơn.」"
"2325" = "「Tất nhiên rồi. Là cô em gái nuôi quan trọng của tôi mà,\\nvới lại đường về của tôi cũng là đường đó.」"
```

### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml

```toml
[script]
"2464" = "「Vâng!」"
```

### 日々姫h5_白濁絵の具の射精会.txt.toml

```toml
[script]
"1189" = "「Hà……a――Vui quá――vui quá――đi――\\nMàu vẽ――của anh hai――người em――toàn bộ――」"
```

### 真闇02_精髄.txt.toml

```toml
[script]
"2793" = "（Kéo——Kéo）"
```

## Kết bài

Batch U10 xong: 16 mục §6 có dòng sửa / **32 dòng** (F1, F2, F4×4, F6, F7, F8, F9, F10, F11×2, F12×3, F13, F15, F26×5, F28, F29×2, F36×6), kèm 13 mục chỉ kiểm chứng-giữ-nguyên (F3, F5, F14, F16, F25, F27, F31, F32, F33, F34, F35, F37, F38). Lượt soát 2: 32/32/0/0; khối TOML 17 file parse-verified. Rebase tổng: cơ sở lúc spawn (0/0) đã cũ — U1b/U1c/U2a
gộp trong lúc batch chạy; đối chiếu ROUTE-UNIFICATION.md 22/11 ~11:15, tổng hiện tại 2 mục /
226 dòng; đợt này +16 mục / +32 dòng = **18 mục / 258 dòng** (0 key trùng với các file U1/U2
đã gộp). Ba điểm cần coordinator để ý: F36 đính chính file của cặp 2823/3034 (ハチロク02,
không phải Grand 09); F38 key 1293 không tồn tại; F10 1691 CÓ trong CSV3 (07_Nagi_Fukami) — ghi chú "CSV3 thiếu" ở bản nháp là sai, coordinator đã sửa.
Không sửa ROUTE-UNIFICATION.md, MEMORY.md hay bất kỳ file audit/moans nào. Không có gì gửi cho Hieu.
