# Moan-fix: ハチロクh7_レトロモダンメイクラヴ.txt.toml (moan-hachiroku-h7-retro-modern-meikuravu)

- File: `ハチロクh7_レトロモダンメイクラヴ.txt.toml` — route 01_Hachiroku, 435 dòng script (monologue 267, ハチロク 107, 双鉄 61). Cảnh H — Soutetsu và Hachiroku trong trang phục lễ hội hoài cổ Taisho (レトロフェスタ).
- TOML md5 `826355d088615a39f35716717fda637e` (khớp md5 audit), 1 bản duy nhất toàn dự án (không có file trùng md5). UTF-8 BOM + CRLF (889 dòng). `[info]` rỗng, `[selections]` rỗng, không thẻ %l, không [ruby].
- CSV3: 1 bộ duy nhất (`translation_toml\01_Hachiroku`), 435 dòng, 0 khóa trùng, 0 VN trống. TOML `[script]` 435 khóa khớp CSV3 435/435; giá trị VN khớp phẳng 435/435 (sau chuẩn hoá `\n` literal ↔ khoảng trắng — TOML-2 làm phẳng `\n`).
- Audit trước đó: 65 sai (14,9%) — đã gộp vào ROUTE-AUDIT.md. File này KHÔNG có dòng "Kh" nào.

## 1. Kiểm chứng file

- Đã đọc 435/435 dòng (CSV3 + TOML-2).
- Sweep gasp: 14 mục cho file này (kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`): 12 fix Ư đã áp nguyên qua audit (477, 783, 804, 807, 814, 974, 975, 976, 978, 1433, 1444, 1842) + 759 (audit sửa lại: thêm Ư sau ～～) + 763 (audit áp ƯƯ cuối). Không dòng gasp Ư nào bị đụng trong đợt moan này; không dòng "Kh" nào bị đổi.
- Đếm nguyên âm của audit đã kiểm chứng lại độc lập bằng máy (đếm ký tự JP): 736 (きゅぅ×7 → 8 u, "kiuuuuuuuu" ✓), 842 (ぁ×9 + あ×9 = 18 a, nhóm 3+4+6+5 mirror ぁ/あ ✓), 843 (ぅ×10 + う×6 → 17 u ✓), 844 (きゅうう → 3 u ✓), 845 (ゆぅ → 2 u ✓), 759 (んくぅぅぅ → 4 u ✓), 819 (ぁ×1 + あ×4 = 5 a — audit ghi "5 a đã đúng" ✓, chỉ khác cách diễn). Tất cả đều đúng — không sửa đếm nào của audit.

## 2. Kiểm kê rên/SFX

- Đã xét 209 dòng rên/SFX: 104 thoại (ハチロク + 双鉄) + 21 độc thoại có tiếng rên + 84 SFX trong ngoặc （ ）.
- Đổi 18 dòng: 17 romaji + 1 đếm nguyên âm (839).
- Giữ 191 dòng rên/SFX (xem §4).
- Nhóm lỗi chính:
  - Họ fa/fu chưa tách (unsplit) bị Việt hoá "phà"/"phùa"/"phù a" — 10 dòng (692, 731, 743, 759, 796, 812, 813, 819, 823, 971): audit đã sửa thành "phà"/"phùa" theo quy tắc cũ; đợt moan đưa về romaji theo quy tắc fallback 21/11.
  - Âm rên bị mất phụ âm đầu / glide — 7 dòng (485, 690, 711, 745, 750, 836, 837): く→"ư", ひゅぎゅ→"hí hự", ひゃっ→"á", ぐっ→"ư", ふきゅん→"Hukyun", んひゅん→"Ưm hiun", んひゅっ→"Ưm hứ".
  - Đếm nguyên âm — 1 dòng (839: ひきゅうっ thiếu 1 u).

## 3. Chi tiết từng bản sửa (18 dòng)

Quy ước áp dụng: mỗi fix là MỘT giá trị duy nhất cho key đó (áp giá trị moan, không áp thêm fix audit cùng key). Với 11 key trùng audit (692, 731, 743, 745, 759, 796, 812, 813, 819, 823, 971), fix = giá trị audit + chỉ đổi token rên; các phần khác của fix audit (typo, nghĩa, đếm, gasp Ư) được giữ nguyên.

### 3a. Họ fa/fu chưa tách → romaji (10 dòng)

**485** — ハチロク (audit bỏ sót)
- JP: 「は……ぁ……く……は――ふ……あっ――だんな、さま、\nの、手……ん……お尻……ひら……い、てっ――」
- TW: 「……啊……——呼……啊——夫君，的手……把屁股……掰開……了——」
- VN cũ: 「Hà……a……ư……hà——phù……a——bàn tay, của……\nphu, quân……ưm……đang banh……mông, ra——」
- VN mới: 「Hà……a……Ku……hà——phù……a——bàn tay, của……\nphu, quân……ưm……đang banh……mông, ra——」
- Lý do: く…… là tiếng "ku" nghẹn (thở dốc), VN cũ "ư" làm mất phụ âm k. Đổi "ư"→"Ku" (TW gộp vào 啊, JP thắng TW). Giữ "phù……a" cho ふ……あっ (dạng tách — xem ghi chú §4 mục 1).

**692** — ハチロク (trùng audit: giữ typo "Khônh"→"Không" của audit)
- JP: 「らめっ！　だめっ――ですっ――双鉄、様――ふあっ！\nお腰、ぐり、ぐり――おしり――わたくし、広がっ、て」
- TW: 「不行！不行——雙鐵少爺——呼啊！腰，動來動去——屁股——被撐開了」
- VN cũ: 「Khônh! Không được——đâu——Ngài Soutetsu——huaa!\nEo ngài, cứ ngoáy, ngoáy——mông em——em, bị nong rộng ra, mất」
- VN mới: 「Không! Không được——đâu——Ngài Soutetsu——Fua!\nEo ngài, cứ ngoáy, ngoáy——mông em——em, bị nong rộng ra, mất」
- Lý do: ふあっ → "Fua" (romaji; audit "phùa" ngượng).

**731** — ハチロク (trùng audit)
- JP: 「ひあ――あっ――あっ――ふあっ――あっ！！」
- TW: 「呀啊——啊——啊——呼啊——啊！！」
- VN cũ: 「Hí a——a——a——phù a——a!!」
- VN mới: 「Hí a——a——a——Fua——a!!」
- Lý do: ふあっ → "Fua" (audit "phùa"). Giữ "Hí a" cho ひあ―― của audit.

**743** — ハチロク (trùng audit)
- JP: 「ひゃっ！　あっ！　んっ！！　ふあっ――はきゅっ――\nふっ――ふあっ！　あっ！　あっ！　あああっ！！！！」
- TW: 「呀！啊！嗯！！呼啊——哈嗚——呼——呼啊！啊！啊！啊啊！！！！」
- VN cũ: 「Hya! A! Ưm!! Huaa——hakyu——\nphù——huaa! A! A! Aaa!!!!」
- VN mới: 「Hya! A! Ưm!! Fua——hakyu——\nphù——Fua! A! A! Aaa!!!!」
- Lý do: ふあっ ×2 → "Fua" (audit "phùa" ×2). Giữ "phù" cho ふっ (hơi thở riêng, không phải fa).

**759** — ハチロク (trùng audit)
- JP: 「ひあっ！　んっ――お尻――ふあっ――お尻、も……\nです、から――今、は……んっ――んくぅぅぅ～～っ」
- TW: 「咿啊！嗯——屁股——呼啊——屁股，也……——所以現在……嗯嗯——啾嗚～～」
- VN cũ: 「Hí a! Ưm——mông——phù a——mông, cũng……\nmà——bây giờ, thì……ưm——ưm kuuu~~」
- VN mới: 「Hí a! Ưm——mông——Fua——mông, cũng……\nmà——bây giờ, thì……ưm——ưm kuuuu~~Ư」
- Lý do: ふあっ → "Fua" (audit "phùa"). Giữ nguyên giá trị audit ở phần còn lại: んくぅぅぅ → "kuuuu" (4 u = 1+3, đã đếm lại ✓) và Ư cuối dòng của audit (っ tuyệt đối sau ～～ — sweep xếp "already-rendered" là sai ở điểm này, audit đã sửa đúng).

**796** — ハチロク (trùng audit)
- JP: 「ふぁっ」
- TW: 「啊」
- VN cũ: 「A」
- VN mới: 「Fa」
- Lý do: ふぁっ → "Fa" (ふぁ = Fa, khác ふあ = Fua). VN cũ "A" mất hẳn âm ふ; audit "Phà" ngượng → romaji. Không thêm Ư (っ là ngắt của chính âm fa, như 741 ひゃっ→"Hya!", 827 ぷあっ→"Pua").

**812** — ハチロク (trùng audit)
- JP: 「ふぁっ……ふっ……は……あ……お尻、も……いま、は\n……達した……ばか、り……で……敏感……んううっ！」
- TW: 「嗚啊……呼……啊……屁股……現在也……才高潮……還很……敏感……嗚！」
- VN cũ: 「Phù a……phù……hà……a……mông, cũng……bây giờ, thì\n……vừa mới……lên đỉnh……xong……nên rất nhạy cảm……ưm ư!」
- VN mới: 「Fa……phù……hà……a……mông, cũng……bây giờ, thì\n……vừa mới……lên đỉnh……xong……nên rất nhạy cảm……ưm ưư!」
- Lý do: ふぁっ → "Fa" (audit "Phà"). Giữ "phù" cho ふっ và "ưm ưư" cho んううっ (2 ư, audit đã đếm đúng).

**813** — ハチロク (trùng audit)
- JP: 「ふぁ……あっ――それ……ここち……いい……\n双鉄……様の……舌……さっきは――あれ、ほどっ」
- TW: 「嗚啊……啊——那個……好舒服……雙鐵少爺的……舌頭……剛才——那麼的」
- VN cũ: 「Phù……a——như thế……dễ……chịu quá……\nlưỡi……của ngài……Soutetsu……ban nãy——rõ ràng, là.」
- VN mới: 「Fa……a——như thế……dễ……chịu quá……\nlưỡi……của ngài……Soutetsu……ban nãy——đến mức đó……」
- Lý do: ふぁ → "Fa" (audit "Phà"). Giữ phần nghĩa "đến mức đó……" của audit.

**819** — ハチロク (trùng audit)
- JP: 「ん……きゅっ――ふぁああああんっ！！！」
- TW: 「嗯……呀嗚、啊——！！！」
- VN cũ: 「Ưm……kiu——phù a a a a a!!!」
- VN mới: 「Ưm……kiu——Faaaaaan!!!」
- Lý do: ふぁああああん là một âm rên dài liền mạch (ぁ×1 + あ×4 = 5 a, đã đếm lại bằng máy — khớp "5 a" của audit), VN cũ tách thành "phù a a a a a" (dạng tách mảnh, ngượng — tiền lệ h9 2180) → romaji "Faaaaaan" (Fa + 4 a + n). Giữ "Ưm……kiu" của audit.

**823** — ハチロク (trùng audit)
- JP: 「ん……あっ――舌……あったかい……んっ――\nや……くびす、じ……んっ――くすぐった――ふぁ」
- TW: 「嗯……啊——舌頭……暖暖的……——……脖子……——癢癢的——嗚啊」
- VN cũ: 「Ưm……a——lưỡi……ấm quá……ưm——\na……sau, gáy……ưm——nhột quá——phù.」
- VN mới: 「Ưm……a——lưỡi……ấm quá……ưm——\na……sau, gáy……ưm——nhột quá——Fa.」
- Lý do: ふぁ cuối dòng → "Fa" (audit "phà"). Không thêm Ư (không có っ).

**971** — ハチロク (trùng audit)
- JP: 「双鉄様？　――んっ！？　あ……チュッ――んっ――\nふっ――あっ――んむっ――あっ――ふあっ！　あっ！」
- TW: 「雙鐵少爺？嗯——！？啊……啾——呼——啊——姆——啊——呼啊！啊！」
- VN cũ: 「Ngài Soutetsu? ——Ưm!? A……chụt——ưm——\nphù——a——ưm——a——phù a! A!」
- VN mới: 「Ngài Soutetsu? ——Ưm!? A……chụt——ưm——\nphù——a——ưm——a——Fua! A!」
- Lý do: ふあっ cuối dòng → "Fua" (audit "phùa"). Giữ "phù——a" cho ふっ――あっ giữa dòng (dạng tách — xem §4 mục 1).

### 3b. Âm rên bị mất phụ âm / glide — audit bỏ sót (7 dòng)

**690** — ハチロク
- JP: 「らめっ――れす――ん、だめっ！　そう、てつ、さまぁ\n――おまん、まん――の、おつ、ゆ――ひゅぎゅっ！？」
- TW: 「不行——了——不行！雙鐵少爺——小妹妹——的，黏液——呀嗚！？」
- VN cũ: 「Không——được——ưm, không được! Ngài, Soutetsu\n——dịch, nhờn——của, cô bé——hí hự!?」
- VN mới: 「Không——được——ưm, không được! Ngài, Soutetsu\n——dịch, nhờn——của, cô bé——Hyugyu!?」
- Lý do: ひゅぎゅっ = hyu-gyu. VN cũ "hí hự" mất glide y (ひゅ→"hí") và mất phụ âm gy (ぎゅ→"hự" — tiếng hự chung chung). Tiền lệ trong file: audit sửa 736 ひぎゅっ→"Higyu", 738 ひゃぎゅっ→"Hyagyu", 761 いぎゅっ→"Igyu" — đều giữ nguyên âm gy.

**711** — ハチロク
- JP: 「も、申し訳ございません、だんなさま――ひゃっ！？」
- TW: 「十、十分抱歉，夫君——呀！？」
- VN cũ: 「T-Thật có lỗi quá, thưa phu quân——á!?」
- VN mới: 「T-Thật có lỗi quá, thưa phu quân——Hya!?」
- Lý do: ひゃっ → "Hya" (VN cũ "á" mất hẳn phụ âm hy). Tiền lệ: audit sửa 741 ひゃっ→"Hya" cho cùng âm này.

**745** — ハチロク (trùng audit: giữ "Ka" và "ưn kyuuu" của audit)
- JP: 「か……は……あっ――ぐっ――んっ――そ――ん、な、\nいき、なり――いき――なりッ――んきゅうう！！？」
- TW: 「呃……啊——咕——嗯——那樣——的，突然——就——就——嗯啊——！！？」
- VN cũ: 「A……ha……a——ư——ưm——như——vậy,\nđột, nhiên——đột——nhiên——ưn kyuuu!!?」
- VN mới: 「Ka……ha……a——Gu——ưm——như——vậy,\nđột, nhiên——đột——nhiên——ưn kyuuu!!?」
- Lý do: ぐっ → "Gu" (VN cũ/audit "ư" làm mất phụ âm g; TW 咕 = tiếng "gu", JP thắng TW). Tiền lệ song song: audit sửa 777 くおっ "Ư ô"→"Kuo" vì mất k. Giữ "ưn kyuuu" của audit (んきゅうう → 3 u đã đúng; dạng "ưn" khớp 843 "Ưn kyuu…u" của audit).

**750** — ハチロク
- JP: 「ふきゅんっ！！！！！！！」
- TW: 「呼啾！！！！！！！」
- VN cũ: 「Hukyun!!!!!!!」
- VN mới: 「Fukyun!!!!!!!」
- Lý do: ふきゅんっ = fu-kyu-n. VN cũ "Hukyun" viết sai phụ âm đầu (ふ = f, không phải h). Tiền lệ: audit sửa 739 ふぁん→"Fuan" (ふ→F). TW 呼 cũng là h, nhưng JP thắng TW.

**836** — ハチロク
- JP: 「んひゅんっっっ！！」
- TW: 「嗯咻！！」
- VN cũ: 「Ưm hiun!!!」
- VN mới: 「Nhyun!!!」
- Lý do: んひゅん = n-hyu-n. VN cũ "Ưm hiun" viết sai âm ひゅ ("hiun" mất glide y, thừa i). Tiền lệ: Kisaki h3 2277 んひゅんっ → "Nhyun". Không thêm Ư (っっっ sau ん — ngắt đã diễn bằng "n" cuối + !!!, tiền lệ ハチロク01 2319).

**837** — ハチロク
- JP: 「んひゅっ！！　ふ――あっ！　あっ！　あっ！！」
- TW: 「嗯咻！！呼——啊！啊！啊！！」
- VN cũ: 「Ưm hứ!! Phù——a! A! A!!」
- VN mới: 「Nhyu!! Phù——a! A! A!!」
- Lý do: んひゅっ = n-hyu. VN cũ "Ưm hứ" viết sai âm ひゅ ("hứ" mất glide y). Tiền lệ: Kisaki h3 2206 ひゅっ → "Hyu". Giữ "Phù——a" cho ふ――あっ (dạng tách — xem §4 mục 1).

**839** — ハチロク (đếm nguyên âm)
- JP: 「んひっ！　あっ――おくっ――ひきゅうっ――にっ！\nひゅあっ――んくっ――あっ、しきゅう――こつんって」
- TW: 「嗯咿！啊——嗯——咿嗚——！呀啊——嗯——啊，子宮——被頂到了」
- VN cũ: 「Ưm hi! A——bên trong——hikyu——!\nHyua——ưm khục——a, tử cung——bị chạm vào rồi」
- VN mới: 「Ưm hi! A——bên trong——Hikyuu——!\nHyua——ưm khục——a, tử cung——bị chạm vào rồi」
- Lý do: ひきゅうっ = hi-kyu-u → "Hikyuu" (2 u theo công thức 1+1); VN cũ "hikyu" thiếu 1 u. Giữ nguyên phần còn lại (んひっ→"Ưm hi" đủ âm, ひゅあっ→"Hyua" đã đúng, んくっ→"ưm khục" theo quy ước くっ→"khục" trong file).

### 3c. Tổng hợp theo loại

- Romaji (fa/fu chưa tách + mất phụ âm/glide): 17 dòng (485, 690, 692, 711, 731, 743, 745, 750, 759, 796, 812, 813, 819, 823, 836, 837, 971).
- Đếm nguyên âm: 1 dòng (839).
- Trùng audit: 11 dòng (692, 731, 743, 745, 759, 796, 812, 813, 819, 823, 971) — fix moan thay thế fix audit ở đúng token rên; áp MỘT giá trị moan mỗi key.
- Mới so với audit: 7 dòng (485, 690, 711, 750, 836, 837, 839).

## 4. Đã kiểm tra, giữ nguyên (không sai)

1. **Dạng tách fa (ふ―あ / ふ――あ / ふ、あ / ふ、ぁ) giữ "phù——a"/"phù, a"/"phù……a" — KHÔNG đổi sang romaji "Fu——a" trong file này.** Lý do: audit đã chốt tiền lệ trong file ở 763 §2.1 ("Phù——a" theo tiền lệ 837/968) và §2.3 liệt kê 821, 837, 968, 485 là quy ước "phù" cho hơi thở ふ — audit (đã gộp, parent kiểm chứng) phân biệt rõ: fa CHƯA TÁCH → "phà"/"phùa" (nay về romaji), fa ĐÃ TÁCH theo JP (――/、/……) → "phù——a" (hai hơi thở riêng, diễn đúng cấu trúc JP, không ngượng). Các dòng giữ theo tiền lệ này: 485 (phần ふ……あっ), 694 (ふ、あっ), 763 (audit), 787 (audit), 802 (ふ、あっ — audit), 816 (ふ――ぁ――ん — audit "phù——a——ưm"), 821 (ふ―あっ), 837 (phần ふ――あっ), 853 (ふ、ぁっ), 968 (ふ――あっ), 971 (phần ふっ――あっ). Ghi cờ cho đợt thống nhất: nếu Hieu muốn thống nhất dạng tách fa về romaji như h9 (2289 ふ――あっ→"Fu——a"), 11 dòng này đổi theo một lượt.
2. **Gasp Ư khóa — không đụng:** 12 fix gasp Ư của audit/sweep (477, 783, 804, 807, 814, 974, 975, 976, 978, 1433, 1444, 1842) + Ư cuối 759 + ƯƯ cuối 763 — giữ nguyên. Không dòng "Kh" nào bị đổi (file không có dòng "Kh").
3. **783 しょっ→"ức" giữ** — audit §5 đã chốt: cách diễn rên ngắt quãng lỏng lẻo, khớp TW ("慢——慢一點!") — giữ, chỉ sửa gasp cuối (đã sửa ở audit). Không đổi "ức"→"Sho".
4. **Đếm nguyên âm của audit — giữ hết:** 736, 842, 843, 844, 845, 759, 812 (xem §1 — đã đếm lại độc lập bằng máy, tất cả đúng).
5. **Romaji của audit — giữ:** 732 "Kyua", 737 "Kyafuu", 738 "Hyagyu", 739 "Hyan"/"Fuan", 741 "Hya", 753 "Fuaa", 760 "Hian", 761 "Igyu", 777 "Kuo", 787 "Ka", 827 "Pua", 856 "ka" — đều đúng âm và đúng đếm.
6. **"ưn/Ưn" cho ん trước kyu — giữ:** 745 "ưn kyuuu" và 754 "ưn kyu" khớp 843 "Ưn kyuu…u" của audit (dạng này khác 844/845 "Ưm" nhưng cả hai đều đã được audit chấp nhận trong file).
7. **Họ ちゅう(っ) giữ quy ước file "chụt"/"chùn chụt":** 793 (ちゅうっ→"chùn chụt"), 1852, 1858 (ちゅう(っ)→"chụt"), 1867 (×4 →"chùn chụt"), 1880 (ちゅうう→"chùn chụt"). Audit §5 đã giữ 1854/1857 "chùn chụttttt" (5 t cố định) là đúng tỉ lệ file — đổi 793/1852/1858/1867/1880 sang "chuu" sẽ phá vỡ nhất quán nội bộ file. Ghi cờ đợt thống nhất (xem §5).
8. **SFX độc thoại （ ） giữ onomatopoeia Việt / diễn tả:** audit §5 đã giữ các dòng kéo dài theo tỉ lệ file — 1811 (17い→22p), 1826 (10お→11p), 1829 (2お→4p), 1854/1857 (5t), 1866 (2お→5t), 1930 (6う→6t), 1941 (11い→18t) — giữ nguyên. 1820 đã rà lại theo cờ của audit: JP ずぶ + 16う, fix audit 20p (tỉ lệ 1,25×, trong khoảng 1,1–1,5× của cụm ず) — giữ, không đổi sang romaji (xem cờ §5).
9. **Các dòng rên ngắn đã đúng:** "A——" (779), "Haa——haa——haa——haa——" (784, 2 a mỗi hơi ✓), "Hà! A! A! A!!!" (770), "Ưm!!" (847), "Higyu!!!?" (734), "Kuo!!" (777, audit), "Ưm gugu!" (840), "Ưm gu!!?" (841), "Khục!" (778/846 — quy ước く/くっ→"khục" trong file, audit giữ ở 783), "haư" (885 — diễn VN cho はぅ, giữ), "Ưm phu……phù" (835 — đủ âm), "Hya! A! Ưm!!" (743 phần đầu, audit).
10. **SFX hôn/ngắn trong ngoặc đã đúng:** "Chụt" cho ちゅっ/チュッ (810, 873, 1852, 1858, 1862, 1875), "liếm/mút" cho れるっ/れろっ theo quy ước file (audit sửa 1878/1944 → "liếm"; cờ "rộp" của Hieu vẫn chờ — xem §5), "Phụt!" cho びゅっ (1885–1896), "Tuốt!" cho しこ/しゅこ (1920–1926), "Phập!" cho ずっ/ずぶっ ngắn (1815, 1828, 1829 phần đầu).

## 5. Cờ cho đợt thống nhất / vòng audit (không tự quyết)

- **Dạng tách fa (11 dòng):** 485, 694, 763, 787, 802, 816, 821, 837, 853, 968, 971 — hiện giữ "phù——a"/"phù, a"/"phù……a" theo tiền lệ audit file này. Nếu Hieu chốt thống nhất về romaji như h9 ("Fu——a"/"Fu, a"), đổi cả 11 dòng một lượt (revert dễ).
- **Họ ちゅう(っ):** 793, 1852, 1858, 1867, 1880 (diễn "chụt"/"chùn chụt") + 1854/1857 (audit giữ "chùn chụttttt") — có nên áp công thức đếm nguyên âm ("chuu"/"chuuu"/"chuuuu") như h9 và Paulette h3, hay giữ quy ước file? Chờ quyết ở đợt thống nhất.
- **SFX độc thoại （ ） chưa áp công thức đếm nguyên âm:** 1840 （れろおおおおっっ → "Liếm dài"）, 1818 （つううううううううううう → "Trượt dài"）, 1868 （ちゅむううううううううう → "Mút mạnh"）, 1883/1929/1931/1932/1933 （きゅうう… → "Siết chặt"/"Thít chặt"）, 1873 （じゅぶうっ → "Nhóp nhép"）, 1876 （くちいっ → "Nhóp nhép"）, 1919/1928 （むにいい(っ) → "Nắn bóp"）, 1835 （みゅにゅぅっ → "bóp"）, 1850 （くぱああっ → "Mở rộng"）, 1903 （きちぃぃぃぃぃ → "Khít quá!"） — diễn tả bằng động từ Việt, độ dài nguyên âm chưa đếm. Tiền lệ h9/Paulette h3: ghi cờ, không sửa trong vòng moan.
- **1831 （ふわっ） → "（Nhẹ nhàng）":** diễn tả, mất hẳn âm "Fuwa". Không rõ là SFX âm thanh hay mô tả chuyển động (ngữ cảnh: sau đoạn chuẩn bị lễ hội) — không tự quyết, để vòng audit/unification xem lại.
- **Đề xuất "rộp" cho họ れる/るっ/れろ (audit flag):** vẫn chờ Hieu — nếu chốt "rộp" thì 1878, 1944 + các dòng れろっ/れるっ trong file đổi theo (đợt thống nhất).
- **745 ぐっ→"Gu" (mới):** TW 咕 ủng hộ "Gu"; lưu ý tiền lệ 1833 （ぐっ――ググッ → "Khục——khục"） trong độc thoại — nếu đợt thống nhất chốt ぐっ→"Khục" toàn file thì 745 đổi theo.
- **839 "ưm khục" cho んくっ:** giữ theo quy ước くっ→"khục" trong file (783 audit giữ); không đổi sang "Nku".

## 6. Lượt soát 2

- Tổng 18 / tái kiểm chứng 18 / bỏ 0 / sửa 0.
- Lượt soát đọc lại từng fix đối chiếu JP (+TW khi cần): đếm nguyên âm kiểm chứng độc lập bằng máy cho 819 (5 a ✓), 839 (2 u ✓), 759 (4 u ✓); các fix audit trùng key chỉ khác giá trị audit ở đúng token rên (692 giữ typo "Không" của audit; 745 giữ "Ka" của audit; 759 giữ "kuuuu~~Ư" của audit; 812 giữ "ưm ưư" của audit; 813 giữ "đến mức đó……" của audit).
- JSON 18 mục dạng chuẩn (list of dicts, khóa string: key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 18/18. Khối TOML parse bằng tomllib: 18 khóa, 0 sai lệch giá trị so với JSON. Mọi fix đều khác old_vn.
- Không fix nào đụng gasp Ư khóa; không dòng "Kh" nào bị đổi; không sửa đại từ/thuật ngữ/nghĩa (trừ phần nghĩa đã có trong fix audit được giữ nguyên).

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
485 = "「Hà……a……Ku……hà——phù……a——bàn tay, của……\\nphu, quân……ưm……đang banh……mông, ra——」"
690 = "「Không——được——ưm, không được! Ngài, Soutetsu\\n——dịch, nhờn——của, cô bé——Hyugyu!?」"
692 = "「Không! Không được——đâu——Ngài Soutetsu——Fua!\\nEo ngài, cứ ngoáy, ngoáy——mông em——em, bị nong rộng ra, mất」"
711 = "「T-Thật có lỗi quá, thưa phu quân——Hya!?」"
731 = "「Hí a——a——a——Fua——a!!」"
743 = "「Hya! A! Ưm!! Fua——hakyu——\\nphù——Fua! A! A! Aaa!!!!」"
745 = "「Ka……ha……a——Gu——ưm——như——vậy,\\nđột, nhiên——đột——nhiên——ưn kyuuu!!?」"
750 = "「Fukyun!!!!!!!」"
759 = "「Hí a! Ưm——mông——Fua——mông, cũng……\\nmà——bây giờ, thì……ưm——ưm kuuuu~~Ư」"
796 = "「Fa」"
812 = "「Fa……phù……hà……a……mông, cũng……bây giờ, thì\\n……vừa mới……lên đỉnh……xong……nên rất nhạy cảm……ưm ưư!」"
813 = "「Fa……a——như thế……dễ……chịu quá……\\nlưỡi……của ngài……Soutetsu……ban nãy——đến mức đó……」"
819 = "「Ưm……kiu——Faaaaaan!!!」"
823 = "「Ưm……a——lưỡi……ấm quá……ưm——\\na……sau, gáy……ưm——nhột quá——Fa.」"
836 = "「Nhyun!!!」"
837 = "「Nhyu!! Phù——a! A! A!!」"
839 = "「Ưm hi! A——bên trong——Hikyuu——!\\nHyua——ưm khục——a, tử cung——bị chạm vào rồi」"
971 = "「Ngài Soutetsu? ——Ưm!? A……chụt——ưm——\\nphù——a——ưm——a——Fua! A!」"
```

## Kết bài

File ハチロクh7_レトロモダンメイクラヴ.txt.toml: 435 dòng đã đọc hết, xét 209 dòng rên/SFX, **đổi 18 dòng (17 romaji + 1 đếm nguyên âm)** — 10 dòng fa/fu chưa tách về romaji (692, 731, 743, 759, 796, 812, 813, 819, 823, 971; trong đó 819 là rên dài 5 a về "Faaaaaan"), 7 dòng audit bỏ sót bị mất phụ âm/glide (485 く→"Ku", 690 ひゅぎゅ→"Hyugyu", 711 ひゃっ→"Hya", 745 ぐっ→"Gu", 750 ふきゅん→"Fukyun", 836 んひゅん→"Nhyun", 837 んひゅっ→"Nhyu"), 1 dòng đếm nguyên âm (839 ひきゅう→"Hikyuu"). 11/18 key trùng audit — fix moan thay thế fix audit ở đúng token rên. Đếm nguyên âm của audit kiểm chứng lại độc lập bằng máy đều đúng (736, 842, 843, 844, 845, 759, 819). Dạng tách fa giữ "phù——a" theo tiền lệ audit đã chốt trong file (763 §2.1); gasp Ư khóa và SFX độc thoại kéo dài theo tỉ lệ file (audit §5) giữ nguyên, đã rà lại 1820 (16う → 20p, tỉ lệ 1,25×, giữ). Lượt soát 2: 18/18, 0 bỏ, 0 sửa. JSON + khối TOML đã kiểm chứng parse, 0 sai lệch. Cờ cho đợt thống nhất: dạng tách fa 11 dòng, họ ちゅう(っ), SFX độc thoại chưa áp công thức đếm, 1831 （ふわっ）, đề xuất "rộp", 745 ぐっ→"Gu" vs "Khục".
