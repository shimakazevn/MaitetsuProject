# Audit — ハチロク15b_さよなら列車.txt.toml (01_Hachiroku)

- File: `ハチロク15b_さよなら列車.txt.toml` — Route 01_Hachiroku, cảnh tàu tạm biệt (Olivy giải nghệ, chuyến cuối về Yatsushiro).
- Disk: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af15b_#U3055#U3088#U306a#U3089#U5217#U8eca.txt.toml`
- CSV3: `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv` — 291 dòng, 1 set duy nhất, 0 key trùng.
- Phương pháp: đọc từng dòng JP + TW đối chiếu VN (full row-by-row semantic read). Không lấy mẫu.
- **Đọc: 291 dòng / Sai: 20 dòng / Tỉ lệ: 6,9%.**
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- TOML md5: `404ce649831d5bba51a449dd4bd86755` (291 key `[script]`, 0 key trùng; key set TOML == CSV3). 1 bản duy nhất (không có file trùng lặp). `[selections]` rỗng. BOM + CRLF giữ nguyên.
- CSV3 vs TOML: VN khớp 100% sau chuẩn hóa (155 khác biệt chỉ là TOML-2 làm phẳng `\n` literal thành khoảng trắng — CSV3 là chuẩn cho fix list; riêng key 1763 là `\n` + khoảng trắng).
- `%l` tag: 0 lệch — mọi tag cân bằng `\x%l…;#00ffc040;…%l;#;`, số lượng JP == VN ở mọi dòng; không có tag dị dạng.

## 1. Phân loại (20)

- Gasp っ mất: 14 (1264, 1524, 1568, 1569, 1570, 1590, 1591, 1592, 1600, 1601, 1602, 1616, 1668, 1863) — 13 từ sweep (áp nguyên giá trị, riêng 1668 khôi phục `\n` từ CSV3 vì sweep làm phẳng thành khoảng trắng) + 1 mới do sweep bỏ sót (1591, っ đầu dòng).
- SFX fa/fu: 2 (1571, 1614) — ふぁ/ふあ → "Phu" (mất nguyên âm 'a'), sửa theo quy tắc đã chốt ふぁ → "phà".
- Sai nghĩa: 1 (1574) — đảo nghĩa: イタくない ("không đau") dịch thành "Không, đau."
- Thuật ngữ: 2 (1637 メリケン → "Meriken"; 1680 gloss 運転体 "thân chính" → "thân vận hành").
- Phiên âm gibberish: 1 (1657) — mất âm tiết ほ ("Munafafa" thiếu "ho") + thiếu —— ở ほんほー.

## 2. Chi tiết từng dòng sai (20)

### 1264 — オリヴィ — lost-gasp-trailing (sweep)
- JP: 「――っ」 / TW: 「——唔」
- Cũ: 「——」 → **Mới: 「——Ư」**

### 1524 — オリヴィ — lost-gasp-whole (sweep)
- JP: 「っ！！？」 / TW: 「什！！？」
- Cũ: 「!!?」 → **Mới: 「Ư!!?」**

### 1568 — オリヴィ — lost-gasp-whole (sweep)
- JP: 「っ！！！」 / TW: 「呀！！！」
- Cũ: 「!!!」 → **Mới: 「Ư!!!」**

### 1569 — 双鉄 — lost-gasp-whole (sweep)
- JP: 「っ！！？」 / TW: 「呃！！？」
- Cũ: 「!!?」 → **Mới: 「Ư!!?」**

### 1570 — 宗方 — lost-gasp-whole (sweep)
- JP: 「っ！？」 / TW: 「呃！？」
- Cũ: 「!?」 → **Mới: 「Ư!?」**

### 1571 — オリヴィ — sfx-fa
- JP: 「ふぁ……うふふっ――えへへ～。\nね？　おいしー、でしょ？」
- Cũ: 「Phu……ufufu——ehehe~.\nThấy chưa? Ngon, đúng không?」 → **Mới: 「Phà……ufufu——ehehe~.\nThấy chưa? Ngon, đúng không?」**
- Lý do: ふぁ = "fa"; "Phu" chỉ diễn ふ (fu), mất nguyên âm 'a'. Quy tắc đã chốt: ふぁ → "phà". Tiếng cười "ufufu"/"ehehe" giữ nguyên (diễn sát JP).

### 1574 — オリヴィ — meaning-inversion (lỗi nghĩa nặng nhất file)
- JP: 「あ、れ？　イタく、ない\nなら、これ――オリヴィの夢、なの？」 / TW: 「咦？一點也不痛。難道說，奧莉薇還在夢裡嗎？」
- Cũ: 「Ủa? Không, đau.\nNếu vậy, đây——là giấc mơ, của Olivy, sao?」 → **Mới: 「Ủa? Không đau.\nNếu vậy, đây——là giấc mơ, của Olivy, sao?」**
- Lý do: イタくない = "không đau". Dấu phẩy sau "Không" đảo nghĩa thành "không, [nó] đau" — phá luôn logic câu (không đau → mới nghi là mơ). Chỉ bỏ dấu phẩy.

### 1590 — 双鉄 — lost-gasp-whole (sweep)
- JP: 「っ！！？」 / TW: 「哦！！？」
- Cũ: 「!!?」 → **Mới: 「Ư!!?」**

### 1591 — オリヴィ — lost-gasp-initial (MỚI, sweep bỏ sót)
- JP: 「っ――あっ――」 / TW: 「唔——啊——」
- Cũ: 「——A——」 → **Mới: 「Ư——A——」**
- Lý do: っ đầu dòng bị mất hoàn toàn — theo ranh giới gasp đã khóa, っ đầu dòng thì thêm Ư. TW diễn cả hai âm (唔——啊——). Vế sau あっ―― → "A——" giữ nguyên theo đúng tiền lệ (あっ――→"A——", không diễn đúp).

### 1592 — ハチロク — lost-gasp-whole (sweep)
- JP: 「っ！！？」 / TW: 「唔！！？」
- Cũ: 「!!?」 → **Mới: 「Ư!!?」**

### 1600 — 双鉄 — lost-gasp-whole (sweep)
- JP: 「っ！」 / TW: 「啊！」
- Cũ: 「!」 → **Mới: 「Ư!」**

### 1601 — 日々姫 — lost-gasp-whole (sweep)
- JP: 「っ！！！」 / TW: 「啊！！！」
- Cũ: 「!!!」 → **Mới: 「Ư!!!」**

### 1602 — 日々姫 — lost-gasp-trailing (sweep)
- JP: 「っ！　～～～っ！」 / TW: 「啊～～～！」
- Cũ: 「! ~~~!」 → **Mới: 「Ư! ~~~Ư!」**

### 1614 — オリヴィ — sfx-fa
- JP: 「ふあっ」 / TW: 「噗哈」
- Cũ: 「Phu」 → **Mới: 「Phà」**
- Lý do: như 1571 — ふぁ = "fa", "Phu" mất 'a'. Quy tắc đã chốt ふぁ → "phà".

### 1616 — オリヴィ — lost-gasp-whole (sweep)
- JP: 「っ！！！！」 / TW: 「噫！！！！」
- Cũ: 「!!!!」 → **Mới: 「Ư!!!!」**

### 1637 — オリヴィ — terminology (Meriken)
- JP: 「オリヴィ、メリケンで――オヒトヨの、こ、だけど。\nだけど、ね？　ずっと、オリヴィ――ムナカタのこと」 / TW: 「奧莉薇——雖然，又是美國式——又是，御一夜的，鐵路人偶。可奧莉薇，一直認為，宗方就是——」
- Cũ: 「Olivy, ở Mỹ——là con của, Ohito, nhưng.\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」 → **Mới: 「Olivy, Meriken——là con của, Ohito, nhưng.\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」**
- Lý do: メリケン nói trong thoại → giữ "Meriken" theo quy tắc đã chốt (tiền lệ ハチロク09/10 sửa furigana メリケン → "Meriken" trong audit). "ở Mỹ" sai nghĩa (chỉ vị trí "ở Mỹ", trong khi メリケン = gốc Mỹ/American-made). "Ohito" trong cùng dòng KHÔNG sửa ở đây — để đợt thống nhất (xem §6).

### 1657 — オリヴィ — sfx-transliteration (nói mớ)
- JP: 「むなふぁふぁほ、ふゅひ、ほへはふへ、ひほひ、ひー\nひゅへへ、ふぁっふぁふぁ、ほへ、ほんほー、はんは」
- Cũ: 「Munafafa, fyuhi, hohefafuhe, hihohi, hi——\nhyuhehe, faffafa, hohe, honho, hanha」 → **Mới: 「Munafafaho, fyuhi, hohefafuhe, hihohi, hi——\nhyuhehe, faffafa, hohe, honho——, hanha」**
- Lý do: むなふぁふぁほ = mu-na-fa-fa-ho (5 mora) — bản cũ "Munafafa" mất âm tiết cuối ほ. ほんほー có trường âm ー → "honho——" cho nhất quán với "hi——" cùng dòng. Các âm tiết còn lại đã đối chiếu từng mora, đúng.

### 1668 — 宗方 — lost-gasp-trailing (sweep, `\n` khôi phục từ CSV3)
- JP: 「起きろ、オリヴィ！　八ツ城までもう少しだ！\nお前、そんな無責任な\x%lレイルロオド;#00ffc040;レイルロオド%l;#;じゃ――っ！！！」
- Cũ: 「Dậy đi, Olivy! Chỉ còn một chút nữa là đến Yatsushiro rồi!\nCô đâu phải là một \x%lレイルロオド;#00ffc040;Railord%l;#; vô trách nhiệm như vậy——!!!」 → **Mới: 「Dậy đi, Olivy! Chỉ còn một chút nữa là đến Yatsushiro rồi!\nCô đâu phải là một \x%lレイルロオド;#00ffc040;Railord%l;#; vô trách nhiệm như vậy——Ư!!!」**
- Lưu ý: giá trị sweep bị làm phẳng `\n` thành khoảng trắng — fix này lấy lại `\n` từ CSV3 (tiền lệ: 3 mục sweep ở file trước cũng khôi phục như vậy).

### 1680 — ハチロク — terminology-gloss (運転体)
- JP: 「さぁ、いかがでしょう？　わたくし、\n\x%l運転体;#00ffc040;運転体%l;#;に換装してしまいましたし、力が弱く――ああ！」 / TW: 「我不太清楚。也可能是因為我換了\x%l運転体;#00ffc040;駕駛體%l;#;，沒什麼力氣——啊！」
- Cũ: 「Chà, sao nhỉ? Em,\nđã đổi sang \x%l運転体;#00ffc040;thân chính%l;#; rồi, nên lực tay hơi yếu——A!」 → **Mới: 「Chà, sao nhỉ? Em,\nđã đổi sang \x%l運転体;#00ffc040;thân vận hành%l;#; rồi, nên lực tay hơi yếu——A!」**
- Lý do: 運転体 = thân lái/vận hành (TW 駕駛體); gloss "thân chính" (thân chính) bịa thêm "chính", không có trong JP. Quy tắc đã chốt: 運転ボディ/運転体 → "thân vận hành" (tiền lệ ハチロク07 sửa gloss 運転体 trong audit).

### 1863 — 双鉄 — lost-gasp-whole (sweep)
- JP: 「っ！」 / TW: 「！」
- Cũ: 「!」 → **Mới: 「Ư!」**

## 3. Sweep っ kiểm chứng

- Sweep có 13 mục cho file này — kiểm chứng từng mục với CSV3: JP khớp 13/13, old_vn khớp 12/13 (riêng 1668 lệch do sweep làm phẳng `\n` — đã khôi phục từ CSV3). Áp nguyên 13/13.
- Quét máy bổ sung toàn bộ dòng JP chứa っ: tìm thêm 1 gasp sweep bỏ sót (1591, っ đầu dòng — xem §2).
- Không sửa (đã kiểm, đúng quy tắc ranh giới gasp): 1520 わけだ――っと (っ cuối câu nhấn mạnh sau だ, VN "——" đã diễn); 1636 オリヴィ――――っ―― (っ giữa cơn lắp, dấu —— đã diễn); 1268 いくらでもっ (っ cuối câu sau も); 1515 いわれたもんっ (dấu ! đã diễn); 1260 よしっ ("Rõ!"); 1604 んく/こくっ/んっ/ごくっ/ぷあっ ("Nku——ực——ưm——ực. ——Pua." — っ đã diễn bằng phụ âm cuối/câu); 1696 ごくっ ("Ực"); 2324 ガっ ("Cộc"); 2329 むぎゅっ ("Véo"); 1803 げんっ/解除っ ("Giới, hạn——Hủy bỏ!"); 1860 さまっ ("Ngài Soutetsu!?"). っ giữa từ (ふっと, すっごい, せっかく, はじめて…) không chạm.

## 4. Đại từ — đã kiểm chứng theo dòng kề

- Soutetsu "anh" với Hibiki: đúng (1721 "Anh sẽ làm phụ lái" — nói với Hibiki).
- Soutetsu "anh" với Olivy: đúng (1685 "Anh, đã làm được gì đâu chứ" — tiền lệ ハチロク09/10 sửa Soutetsu→Olivy "tôi"→"anh", đã parent-verified). Độc thoại Soutetsu gọi Olivy "em ấy" (2036, 2100, 2103, 2130, 2166, 2211, 2219, 2280) — nhất quán "em".
- Olivy tự xưng "chị" với Hachiroku/Hibiki: ĐÚNG, giữ nguyên — Olivy lớn tuổi hơn Hachiroku (bằng chứng ハチロク06 3455 「オリヴィは…ハチロクよりも古いのだ」, Hachiroku gọi Olivy 先輩; tiền lệ parent-verified): 1576 "vào lưng, chị" (nói với Hibiki), 1613 "cảm ơn em" (Hachiroku), 1784 "Véo má chị" (Hachiroku), 1809/1810 "ở bên chị"/"kể cho chị nghe" (nhiều khả năng Hachiroku).
- Paulette → Soutetsu "anh Soutetsu": đúng khóa B4 (1807 "anh Soutetsu cứ tự mình quyết định").
- Hachiroku tự xưng "em": nhất quán toàn file (1510, 1608, 1651, 1693, 1833, 1850, 1860, 1861).
- Hibiki tự xưng "em": đúng (1695 "Em á?").
- Mayami tự xưng "chị": đúng (1564, 1786).

## 5. Giữ nguyên (đã đọc kỹ, không phải lỗi)

- 1266 "muốn gọi, như vậy": JP よびたかった không nêu tân ngữ (Olivy muốn gọi Soutetsu bằng gì không nói rõ) — VN giữ độ mơ hồ như JP; TW đoán "Olivy's driver" là diễn giải thêm, không sửa theo.
- 1268 "dù là bao nhiêu đi chăng nữa": JP いくらでもっ là mảnh câu, VN giữ mảnh câu như JP.
- 1315 Munakata "Em đánh giá anh quá cao rồi": người nghe là Olivy hoặc Hibiki (cả hai đều "em") — không mơ hồ đến mức sai.
- 1546 "Không có gì, đáng ngạc nhiên, sao ạ?": JP なにが不思議ではないのですか là câu hỏi tu từ ("có gì mà không lạ?") — VN diễn tương đương.
- 1606 うん → "Ưm": tiếng ừm đồng ý của Olivy, chấp nhận được.
- 1608: JP cụt ("決してオリヴィちゃんのことを…") — VN hoàn thiện bằng động từ 忘れません ở ngay vế trước cùng dòng; TW cũng hoàn thiện tương tự. Không phải bịa.
- 1636: xem §3.
- 1567 ひゃうっ → "Hya!!": tiếng kêu ngạc nhiên (không phải rên H-scene) — "Hya" là dạng romaji chuẩn cho ひゃ; giữ.
- 1723 "Cảm ơn cậu nha, Hibiki": JP không có đại từ; "cậu" là cách gọi thân mật trung tính (tiền lệ giữ "cậu" ở JP あなた trung tính) — giữ, không thống nhất "em".
- 1753 "Còiiii…!!!", 2322/2323 "Tuuu…!": còi tàu — độ dài âm là phong cách SFX, công thức nguyên âm chỉ áp cho う/ぅ, không áp cho ー. Giữ.
- 2319 (がっ――ざしゅっ！×2) → "(Xoạt! Xoạt!)": mỗi cặp thud+swish là một nhát xẻng — TW cũng gộp thành 2 đơn vị. Giữ.
- 1577/1721/2333 gloss 機関士 "người lái tàu": ĐÚNG nghĩa, là dạng gloss phổ biến nhất toàn project (100 dòng) — quy tắc đã chốt "thợ lái đầu máy" chỉ dùng để sửa các gloss sai hẳn ("nhân viên cơ vụ"). Giữ, không đổi.
- 1999 屋岳 → "Yadake": JP viết 屋岳, TW 矢岳; VN theo TW. Không rõ là lỗi chính tả gốc hay biến thể kanji — giữ, không đụng.
- 1279 「…………」: chỉ dấu câu, VN == JP là đúng.
- VN trùng nhau ở các dòng gasp (「!!?」×4, 「!」×2, 「!!!」×2, "(Cộc! Cộc! Cộc! Cộc!)"×2): JP gốc cũng giống hệt nhau — không phải xoay/misalignment.

## 6. Ghi nhận đợt thống nhất (KHÔNG tính sai — theo tiền lệ Grand 08 vừa gộp: Ohito 5 dòng để thống nhất)

- 御一夜/御鉄 → "Ohitoyo" (6 dòng): 1299 (御鉄), 1512 (御一夜), 1637 (オヒトヨ — chỉ sửa Meriken trong audit này, "Ohito" còn lại để thống nhất), 1689 (御一夜鉄道), 1999 (御一夜), 2143 (御一夜鉄道).
- 小畑線 → "Okoba" (1 dòng): 1999 "tuyến Obata" (cùng dòng có cả "Ohito" — 2 mục thống nhất trong 1 dòng).
- 右田一 → "Migita Ichi" (1 dòng): 2228 "nước của Migita System" (TW: 右田一釀酒廠 — tên người/hãng, không phải "System").
- Tổng: 8 dòng ứng viên thống nhất (1999 tính 2 mục).

## 7. Chờ Hieu (không tính sai — cần quyết, không tự quyết)

1. **Cụm đại từ Olivy ↔ Soutetsu (toàn file dùng "chị"/"anh", nhưng mâu thuẫn nội bộ + mâu thuẫn liên file):**
   - Trong file này: độc thoại Soutetsu gọi Olivy "em ấy" 8 lần (2036, 2100, 2103, 2130, 2166, 2211, 2219, 2280) + Olivy gọi Soutetsu "anh" (1542, 1699, 1840) — theo nguyên tắc đối ứng thì Olivy phải tự xưng "em" (hoặc "tôi") với Soutetsu, không phải "chị".
   - Nhưng liên file: ハチロク06/10/14 giữ Olivy tự xưng "tôi" + gọi Soutetsu "cậu" (parent-verified, ROUTE-AUDIT.md); ハチロク06 đã ghi "Chờ Hieu: Olivy xưng 'cậu'; Soutetsu xưng với Olivy 'tôi' hay 'anh'" — vẫn chưa chốt.
   - Các dòng liên quan trong file này: 1699 "giúp đỡ, chị" (nói với Soutetsu), 1839 "đưa chị đến Omiya" (Soutetsu), 1640 "Hình như chị đã hiểu" (đang được Soutetsu bế), 1515/1522/1583/1589 ("chị" — người nghe không rõ, có thể Soutetsu), 1858 "Được em, trân trọng" (người nghe không rõ: nếu là Soutetsu thì "em" sai, phải "anh"; nếu là Hachiroku thì đúng), 1703 "Cảm ơn em… cho chị" (người nghe không rõ: Hachiroku thì đúng, Soutetsu thì sai), 1808 "Cảm ơn cậu… giúp chị" (người nghe không rõ: Paulette hay Hibiki?).
   - Đề xuất: giữ nguyên toàn bộ cụm này chờ Hieu chốt một chuẩn chung cho cả project (đợt thống nhất), vì sửa lẻ từng file sẽ làm các file vênh nhau.
2. **1654 Olivy tự xưng "chị" với Munakata** ("Chị, quên——vậy, thôi——", nói với "Muna……kata"): Munakata là đàn ông lớn tuổi; "chị" với ông là đáng ngờ — nhưng Olivy dùng "chị" nhất quán cả file nên không tự sửa.
3. **1566 Soutetsu tự xưng "anh" với Munakata** ("cánh tay của anh cũng mỏng manh lắm… Nhờ ngài có được không?"): cặp "anh" + "ngài" vênh nhau trong tiếng Việt. Tiền lệ: ハチロク12 1826 Soutetsu → Munakata dùng "cháu/chú" ("Cảm ơn chú… Cháu định…"); file này gọi Munakata là "ngài" chứ không phải "chú". Ứng viên sửa: "tôi" (trung tính, hợp "ngài") hoặc "cháu" (theo ハチロク12) — cần quyết.
4. **[characters] ghi 'Olive' thay vì "Olivy"** (key 1908, character_subs 2063) — không phải dòng script; chính tả đã chốt là "Olivy" (tiền lệ parent đã cờ ở file khác).

## 8. Khối TOML (đã parse-verified: 20 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
1264 = "「——Ư」"
1524 = "「Ư!!?」"
1568 = "「Ư!!!」"
1569 = "「Ư!!?」"
1570 = "「Ư!?」"
1571 = "「Phà……ufufu——ehehe~.\\nThấy chưa? Ngon, đúng không?」"
1574 = "「Ủa? Không đau.\\nNếu vậy, đây——là giấc mơ, của Olivy, sao?」"
1590 = "「Ư!!?」"
1591 = "「Ư——A——」"
1592 = "「Ư!!?」"
1600 = "「Ư!」"
1601 = "「Ư!!!」"
1602 = "「Ư! ~~~Ư!」"
1614 = "「Phà」"
1616 = "「Ư!!!!」"
1637 = "「Olivy, Meriken——là con của, Ohito, nhưng.\\nNhưng, nhé? Từ lâu, Olivy——đối với Munakata」"
1657 = "「Munafafaho, fyuhi, hohefafuhe, hihohi, hi——\\nhyuhehe, faffafa, hohe, honho——, hanha」"
1668 = "「Dậy đi, Olivy! Chỉ còn một chút nữa là đến Yatsushiro rồi!\\nCô đâu phải là một \\x%lレイルロオド;#00ffc040;Railord%l;#; vô trách nhiệm như vậy——Ư!!!」"
1680 = "「Chà, sao nhỉ? Em,\\nđã đổi sang \\x%l運転体;#00ffc040;thân vận hành%l;#; rồi, nên lực tay hơi yếu——A!」"
1863 = "「Ư!」"
```

## 9. Kiểm chứng (verification)

- JSON: 20 mục, key dạng string, dạng list-of-dicts chuẩn; jp/tw/old_vn/character khớp CSV3 tuyệt đối 20/20.
- Khối TOML: parse bằng tomllib OK; 20 khóa; 0 sai lệch giá trị so với JSON (so sánh raw string — lưu ý tomllib parse `\\n` thành literal backslash-n).
- Diff-sanity (cơ học, từng fix vs old VN): mọi fix chỉ đổi đúng chỗ cần sửa — gasp chỉ thêm Ư; 1571/1614 chỉ đổi 'u'→'à'; 1574 chỉ bỏ dấu phẩy; 1637 chỉ đổi "ở Mỹ"→"Meriken"; 1657 chỉ thêm "ho" + "——"; 1680 chỉ đổi gloss; 1668 chỉ thêm Ư (giữ nguyên `\n` + tag %l).
- Lượt soát 2 (đọc lại toàn bộ 20 giá trị fix đối chiếu JP): **20/20 re-verified, 0 bỏ, 5 sửa** — 5 sửa đều là khôi phục dấu 「」 bị sót khi viết fix lần đầu (1571, 1574, 1614, 1637, 1657), phát hiện nhờ diff-sanity cơ học.
- Lưu ý cơ sở tổng: task giao cơ sở 156 file / 6.997 dòng sai, nhưng trong lúc audit, loop đã gộp グランドリライト08_ふかみ (+16) — ROUTE-AUDIT.md hiện tại là **157 file / 7.013 dòng sai**. Snippet dùng cơ sở mới này (xem file snippet).

## Kết bài

File ハチロク15b_さよなら列車: 291 dòng đã đọc hết, **20 dòng sai (6,9%)** — tỉ lệ thấp so với mặt bằng chung, không có lệch vị trí/xoay/nhiễm chéo. Lỗi nặng nhất là 1574 đảo nghĩa ("Không, đau" thay vì "Không đau"); còn lại chủ yếu là gasp っ mất (14, trong đó 13 từ sweep + 1 sweep bỏ sót) và vài lỗi SFX/thuật ngữ nhỏ. Cụm đại từ Olivy ↔ Soutetsu và 2 dòng đại từ với Munakata (1566, 1654) để Hieu quyết — không tự sửa. 8 dòng thuật ngữ (Ohito/Obata/Migita System) ghi vào đợt thống nhất.
