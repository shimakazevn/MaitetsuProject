# Moan-fix REVIEW — ハチロクh8_桜色のひめごと.txt.toml (moan-hachiroku-h8-sakura-iro-no-himegoto)

File H-scene thứ 8 của Hachiroku (lễ hội Hinamatsuri, rượu ngọt/amazake, wakame-zake / wareme-zake). Nhân vật: monologue 176, ハチロク 98, 双鉄 58.

## 1. Xác minh file

- File: `ハチロクh8_桜色のひめごと.txt.toml` — route `01_Hachiroku`.
- Disk: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30afh8_#U685c#U8272#U306e#U3072#U3081#U3054#U3068.txt.toml`
- TOML md5: `818002990fb400412684b19303c9839c` (khớp với md5 lúc audit; không có bản trùng — chỉ 1 file mang tên này trong `sources/toml2/`).
- CSV3: 1 bộ duy nhất, 332 dòng, 0 key trùng; flat-match VN với TOML: 332/332.
- Đã đọc 332/332 dòng (CSV3 + TOML-2, đối chiếu từng dòng).

## 2. Moan inventory — 156 dòng rên/SFX đã xét

- Thoại rên/SFX (ハチロク + 双鉄): 108 dòng — rên dài (あ/は/ふ/ひゃ/ひあ/きゅう…), hơi thở (ふっ/ふ/はぁ), SFX miệng (ちゅ/じゅぼ/れる…), cười (うふふ), tiếng nuốt (ごくん), nói ngọng khi say (ほーへふ/わらふ/はふぁ).
- SFX trong ngoặc （） ở độc thoại: 45 dòng (1524–1594: きゅ/れる/ずぶ/びゅ/にゅぼ/みっちゅう…).
- Độc thoại có tiếng thở/cười: 3 dòng (1137 うふふ, 1167 ん……, 1177 ふうむ).
- Tổng: 156 dòng rên/SFX. Đổi 3 dòng, giữ 153 dòng.

## 3. Các dòng sửa (3 dòng — đều là đếm nguyên âm)

### 778 — đếm nguyên âm (ハチロク)

- JP: 「あ……匂い、濃い……ん――（すん、すん）――\nはぁぁあ――胸、いっぱいに、双鉄様の……匂い、が」
- TW: 「啊……好濃的氣味……——（嗅、嗅）——蛤啊——心裡都是……您的氣味了」
- VN cũ: 「A……mùi, nồng quá……ưm——（Hít, hít）——\nHaaa——Trong lồng ngực, tràn ngập……mùi hương, của Ngài Soutetsu」
- VN mới: 「A……mùi, nồng quá……ưm——（Hít, hít）——\nHaaaa——Trong lồng ngực, tràn ngập……mùi hương, của Ngài Soutetsu」
- Lý do: はぁぁあ = は (1 a) + ぁ + ぁ + あ = 4 âm a; VN cũ "Haaa" chỉ có 3 a — thiếu 1. Audit bỏ sót dòng này. ("A……" đầu dòng ứng với あ…… mở đầu, giữ nguyên.)

### 811 — đếm nguyên âm (ハチロク)

- JP: 「くひぃぃぃぃぃぃぃぃぃぃっ！！！」
- TW: 「嗚咿——！！！」
- VN cũ: 「Kuhiiiiiiiiiiiiiii!!!」 (15 chữ i)
- VN mới: 「Kuhiiiiiiiiiii!!!」 (11 chữ i)
- Lý do: JP = く + ひ (1 i) + ぃ×10 (đếm trực tiếp từng ký tự: ぃ ở vị trí 3–12) = 11 âm i. Fix audit "Kuhiiiiiiiiii" chỉ có 10 i — audit đếm nhầm ぃ×9 trong bản audit (ghi "ひ (1 i) + ぃ×9 → 10 chữ i"). VN cũ thừa 4. Fix moan này thay thế fix audit cùng key (khác fix audit chỉ ở số lượng i). っ cuối dòng bỏ theo tiền lệ (っ sau nguyên âm dài không diễn Ư — như audit 835).

### 827 — đếm nguyên âm, mất độ dài んんんっ (ハチロク)

- JP: 「ん……ちゅっ――んんんっ――ふあっ――ふっ――\nちゅっ――チュムッ――れるっ、れろおっ、ん、ちゅっ」
- TW: 「嗯……啾——嗯嗯——呼啊——呼——啾——啾嗯——咻嚕，嗯，嗯，啾」
- VN cũ: 「Ưm……chụt——ưm ưm——huaa——hu——\nchụt——chụt——liếm, mút mát, ưm, chụt」
- VN mới: 「Ưm……chụt——ưm ưm ưm——Fua——phù——\nchụt——chụt——liếm, mút mát, ưm, chụt」
- Lý do: んんんっ = 3 morae ん; VN cũ "ưm ưm" chỉ diễn 2 — mất 1 âm (tiền lệ moan 凪h2 đã sửa mất độ dài んんんっ). Fix này GỘP cả fix audit cùng key (ふあっ→"Fua", ふっ→"phù") + sửa moan (ưm ưm→ưm ưm ưm); khác fix audit chỉ ở phần rên — áp giá trị moan thay audit ở đợt thống nhất. (TW viết 嗯嗯 = 2, nhưng JP 3 morae là chuẩn — JP thắng TW.)

## 4. Đồng ý với audit — 46 dòng audit đã sửa đúng rên, không đổi thêm

Audit file này đã áp romaji fallback rất kỹ (34 romaji + 5 đếm nguyên âm + 9 gasp = 48 dòng moan). Kiểm chứng lại từng dòng, đồng ý 46/48:

- Romaji fa/fu (đã đúng, giữ nguyên giá trị audit): 703 きゃふっ→"Kyafu" + ふぁ→"Fua"; 705/708/726/728/729/731/732/746/761/771/812/813/821/855/857/946 ふぁ/ふあ→"Fua/Fuaa"; 706/737/743/751/754/759/762/774/780/809/827/829/831/843 ふっ/ふ→"Phù/phù" (tiền lệ h1 giữ "phù" cho ふっ/ふ; file này 767 đã dùng "phù" sẵn); 724/751/754/780/831 nói ngọng ほーへふ/わらふ/はふぁ→"phu/fua".
- Đếm nguyên âm audit đã đúng (đếm cơ học lại): 709 しょこおおおお→"đóoooo" (5 o); 734 ふううううう→"Phuuuuuu" (6 u = 1+5); 736 きゅう×11→12 u; 782 ァぁ→"Aa" (2 a); 835 っきゅう×6→"ƯKyuuuuuuu" (7 u); 836 んきゅう×11→12 u; 749 ぃ×13→13 i (dòng toàn ぃ, không có mora gốc nên không +1).
- Gasp Ư (sweep/audit, KHÔNG đụng lại): 467, 951, 952, 953, 1225, 1274, 1276 + 706 (おっぱい――っ giữa dòng, audit thêm đúng) + 749 (thêm Ư sau ~).
- SFX sai âm audit đã sửa: 798 ぶぢゅ "Bạch"→"Bụp".
- 2 dòng audit sửa moan nhưng moan-fix thay thế (mục 3): 811, 827.

## 5. Ghi chú các dòng rên giữ nguyên (đáng chú ý)

- ひあ/ひゃ đã đúng romaji sẵn, không sửa: 711/713/715 "Hya", 737/738/742/743 "Hia", 705/709/740 "Hyua", 706 "Hyagyu", 816 "hya——a", 927 ひうっ→"hiu", 748 ひぎゅううっ→"Higyuuu" (3 u đúng). (Quy tắc họ ひゃ quyết 21/11 ~11:55 — ひゃ/ひゅ/ひあ/きゃ → romaji, "Á" là lỗi mất âm — file này KHÔNG có dòng "Á" nào cho họ này: tất cả đã là romaji; "Á" duy nhất trong file là từ "Ánh mắt" ở 1137, không phải tiếng rên.)
- ふぁ/ぷぁ đã đúng romaji sẵn: 794/810 ぷぁ→"pua", 847 ぷぁっ→"Pua!".
- んっ→"Ưm" nhất quán toàn file (769, 774, 844, 851, 922, 837 んうっ→"Ưm u", 839 んくっ→"Ưn ku"); ん……→"Ưm……" (1167).
- Cười là cười, không phải rên: 830/846 うふふ→"Ufufu" (830 giữ "Ufufu" kèm ふぅ→"phuu" audit đã sửa đúng 2 u).
- "Kh" cho glottal-stop っ GIỮ NGUYÊN, không đổi sang Ư (quy tắc đã khóa): 743/821/782 くっ→"khục", 1552 ぴたっ→"Khựng lại" (diễn theo sự kiện, audit giữ).
- SFX trong ngoặc （） diễn theo nghĩa hành động — giữ nguyên độ dài kéo chữ của các từ hành động ("mátttt…", "chépppp…", "Siết chặtttt…") theo tiền lệ audit h1: công thức đếm nguyên âm chỉ áp cho tiếng rên dạng romaji/âm thanh, không áp cho từ hành động. Đã đếm cơ học: các độ dài này không theo JP (vd. 722 JP う×15 vs VN t×23; 799 お×17 vs p×26) — đó là phong cách kéo chữ nghệ thuật, audit giữ nguyên, moan-fix cũng giữ.
- Nói ngọng khi say giữ nguyên cách ngắt âm tiết của bản cũ (audit đã chuẩn hóa phụ âm h→f/ph): 724, 751, 754, 780, 831.
- 681 は――ふ、か→"hu, a" giữ nguyên theo quyết định audit (nói ngọng, TW cũng nén thành một âm tiết).
- 783/815/849 ああ→"À" giữ nguyên theo quyết định audit (thán từ "yeah" của Soutetsu, không phải rên cần đếm âm).
- 796/809 VN dùng （） thay 「」 cho dòng thuần SFX — giữ nguyên theo quyết định audit (ghi chú định dạng, không phải lỗi nội dung).
- 756 おっと→"Oops", 757 えいっ→"Ây!", 755 くはっ→"Kuha!", 758 くうっ→"Kuu" (2 u đúng), 784 くあああっ→"Kuaaa" (3 a đúng), 823 はぁ→"haa" (2 a đúng), 830 ふぅ→"phuu" (2 u đúng), 1525 みゅう→"Myuu" (2 u đúng), 1556 きゅん→"Kyun".

## 6. Kiểm chứng sweep gasp

- Sweep có 10 mục cho file này — đã kiểm chứng trực tiếp từng mục:
  - 8 mục audit đã áp (467, 749, 951, 952, 953, 1225, 1274, 1276): đúng, không đụng lại. (953: sweep ghi 9 dấu ~ là sai, audit đã sửa thành 5 Ư + 7 ~ + 1 Ư theo JP.)
  - 2 mục already-rendered (732 んく～～～っ, 1584 もみゅ/むにゅ/にゅる/さすすす～～っ): đúng là đã diễn, không sửa.
- Không có dòng "Kh" nào bị đổi sang Ư. Không có dòng gasp Ư nào bị xem lại.

## 7. Cờ cho đợt thống nhất (1 cờ — đề nghị HỦY một phần fix audit)

### 878 — đề nghị HỦY phần gỡ "ưm" của fix audit, giữ VN cũ

- JP: 「すずは、全部を――双鉄、さま――にっ――んっ！\n染めて――作り変えて――いただき、たい――ですっ！」
- TW: 「我，的全部——都是您的——嗯——！讓我——染上您的色彩——變成您的模樣吧——！」
- VN cũ: 「Suzu muốn, tất cả——Ngài Soutetsu——ưm!\nNhuốm màu——tạo hình lại——cho em——!」
- Fix audit: 「Suzu muốn, tất cả——Ngài Soutetsu——!\nNhuốm màu——tạo hình lại——cho em——!」 (gỡ "ưm", lý do audit: にっ là tiểu từ に + っ nhấn mạnh, không phải tiếng rên — VN cũ bịa thêm âm)
- Ý kiến moan-fix: にっ và んっ là HAI âm riêng biệt — にっ là tiểu từ bị ngắt, còn んっ là một tiếng rên/gasp mũi đứng riêng sau đó. TW có 嗯 tương ứng với んっ, và toàn file này んっ đều diễn thành "ưm" (769, 774, 844, 851, 922). Gỡ "ưm" làm mất hẳn âm んっ — trái quy tắc "không để mất âm". Đề nghị ở đợt thống nhất: HỦY phần gỡ "ưm" của fix audit 878, giữ VN cũ "——ưm!". (Không đưa 878 vào wrong.json vì fix moan sẽ bằng đúng VN cũ — không có gì để đổi so với TOML hiện tại.)

## 8. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 3 giá trị fix so với JP + TW sau lượt đầu, kèm đếm cơ học lại 7 dòng đếm nguyên âm audit đã sửa (709, 734, 736, 749, 782, 835, 836 — đều đúng).
- Tổng: 3 / tái kiểm chứng: 3 / bỏ: 0 / sửa: 0.

## 9. Khối TOML (parse-verified bằng tomllib: 3 khóa, 0 sai lệch giá trị so với wrong.json)

```toml
[script]
"778" = "「A……mùi, nồng quá……ưm——（Hít, hít）——\\nHaaaa——Trong lồng ngực, tràn ngập……mùi hương, của Ngài Soutetsu」"
"811" = "「Kuhiiiiiiiiiii!!!」"
"827" = "「Ưm……chụt——ưm ưm ưm——Fua——phù——\\nchụt——chụt——liếm, mút mát, ưm, chụt」"
```

Lưu ý: trong khối TOML trên, `\\n` là ký tự xuống dòng đã escape (giá trị thực trong JSON/TOML là `\n` literal như CSV3).

## Kết bài

File ハチロクh8_桜色のひめごと: đã đọc 332/332 dòng, xét 156 dòng rên/SFX, đổi 3 dòng (778 thiếu 1 a, 811 audit đếm thiếu 1 i, 827 thiếu 1 ưm) — cả 3 đều là lỗi đếm nguyên âm/độ dài, không có dòng romaji mới vì audit file này đã áp romaji fallback cho họ fa/fu rất kỹ (46/48 dòng moan của audit kiểm chứng lại là đúng). 1 cờ cho đợt thống nhất: hủy phần gỡ "ưm" của fix audit 878. Không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào.
