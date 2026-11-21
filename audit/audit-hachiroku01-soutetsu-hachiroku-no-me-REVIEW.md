# Audit — ハチロク01_双鉄の目・ハチロクの目.txt.toml (01_Hachiroku)

- **File:** `01_Hachiroku/ハチロク01_双鉄の目・ハチロクの目.txt.toml`
- **Disk:** `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af01_#U53cc#U9244#U306e#U76ee#U30fb#U30cf#U30c1#U30ed#U30af#U306e#U76ee.txt.toml`
- **TOML md5:** `ffe814ee27a9928f51f6c3525229f577` — bản duy nhất (không có file trùng md5 trong `01_Hachiroku/`, không thuộc nhóm 11 file trùng).
- **CSV3:** 394 dòng, tất cả section `script`, key 1345–2911, **0 key trùng**. TOML `[script]` cũng 394 key, khớp 1–1 với CSV3 (247 "lệch" TOML-vs-CSV3 chỉ là TOML-2 flatten literal `\n` thành khoảng trắng — CSV3 là chuẩn).
- **Phương pháp:** đọc từng dòng (394/394) đối chiếu JP + TW, kiểm tra sweep, kiểm tra tag `%l`, kiểm tra xưng hô/danh xưng toàn file và đối chiếu project-wide khi cần.
- **Kết quả: 394 dòng đọc, 7 dòng sai (1,78%).**
- **Phân loại:** xưng hô 3 (2210, 2232, 1685) · gasp 1 (1755, theo sweep) · thuật ngữ 1 (2718) · diễn đạt 2 (1996, 2423).
- **Cấu trúc:** lệch dòng (misaligned) 0 · rotation 0 · nhiễm chéo file (contamination) 0 · orphan 0 · chưa dịch 0 · key trùng 0.
- **Second pass:** tổng 7 / re-verified 7 / removed 0 / corrected 0. (Đọc lại toàn bộ 7 fix đối chiếu JP; không fix nào bị loại hay phải sửa lại.)

## Các dòng sai

### 1. Key 2210 — ポーレット — xưng hô (B4 lock)
- JP: 「なら、これでみなさん集まったということで――\n双鉄くん。よければ、昨日の話の続きを」
- TW: 「那麼，既然大家都到齊了，雙鐵君，我們就接著昨晚的話題吧」
- Old VN: 「Vậy, vì mọi người đã tập trung đông đủ rồi——\nCậu Soutetsu. Nếu được, xin hãy tiếp tục câu chuyện ngày hôm qua.」
- Fix: 「Vậy, vì mọi người đã tập trung đông đủ rồi——\nAnh Soutetsu. Nếu được, xin hãy tiếp tục câu chuyện ngày hôm qua.」
- Lý do: Paulette gọi Soutetsu là 双鉄くん → theo B4 lock phải là "anh Soutetsu", không phải "cậu Soutetsu".

### 2. Key 2232 — ポーレット — xưng hô (B4 lock)
- JP: 「市政に対する意見とか要望とかも――\n双鉄くん、現場から上げようとしてくれてるんですね？」
- TW: 「雙鐵君，你也會把基層對市政府的意見與期望反映給我們的，對吧？」
- Old VN: 「Những ý kiến hay nguyện vọng đối với chính quyền thành phố——\nCậu Soutetsu, cậu định sẽ thu thập từ hiện trường đúng không?」
- Fix: 「Những ý kiến hay nguyện vọng đối với chính quyền thành phố——\nAnh Soutetsu, anh định sẽ thu thập từ hiện trường đúng không?」
- Lý do: như 2210 — 双鉄くん từ Paulette → "anh Soutetsu" (cả danh xưng lẫn đại từ).

### 3. Key 1685 — ポーレット — xưng hô (B4 lock)
- JP: 「そうですね……それが一番いい形かもって、言われてみれば、感じます」
- TW: 「也是……這麼說來，我也覺得這樣或許真的是最好的方式」
- Old VN: 「Đúng vậy nhỉ……nghe cậu nói thế,\ntôi cảm thấy đó có lẽ là cách tốt nhất.」
- Fix: 「Đúng vậy nhỉ……nghe anh nói thế,\ntôi cảm thấy đó có lẽ là cách tốt nhất.」
- Lý do: JP không có danh xưng, nhưng VN tự thêm "cậu" để chỉ Soutetsu — Paulette xưng hô với Soutetsu là "anh" theo B4 lock, nên "nghe cậu nói" sai quy tắc. (Đây là 1 trong 2 dòng Paulette dùng "cậu" cho Soutetsu trong file; dòng còn lại là 2232.)

### 4. Key 1755 — 双鉄 — gasp (sweep)
- JP: 「っ！」
- TW: 「呃！」
- Old VN: 「!」
- Fix: 「Ư!」
- Lý do: sweep entry duy nhất của file này (`lost-gasp-whole`), đã verify đúng JP — cả dòng chỉ là tiếng gasp っ, VN bỏ mất. Áp dụng đúng giá trị sweep.

### 5. Key 2718 — monologue — thuật ngữ (fabrication)
- JP: 「無論、\x%lナッパ服;#00ffc040;ナッパ服%l;#;も、\x%lスクレイパー;#00ffc040;スクレイパー%l;#;の持ち柄もすでに\n煤と油汚れにまみれ、ドロドロだ。」
- TW: 「當然，\x%lナッパ服;#00ffc040;彩頁服%l;#;和\x%lスクレイパー;#00ffc040;爐鏟%l;#;的握柄早就沾滿煤和油汙，髒得一塌糊塗。」
- Old VN: "Tất nhiên, cả \x%lナッパ服;#00ffc040;dịch vụ trang màu%l;#; lẫn cán của \x%lスクレイパー;#00ffc040;dao cạo xỉ than%l;#; đều đã\nlấm lem bồ hóng và dầu mỡ, bẩn thỉu nhầy nhụa."
- Fix: "Tất nhiên, cả \x%lナッパ服;#00ffc040;quần áo nappa%l;#; lẫn cán của \x%lスクレイパー;#00ffc040;dao cạo xỉ than%l;#; đều đã\nlấm lem bồ hóng và dầu mỡ, bẩn thỉu nhầy nhụa."
- Lý do: ナッパ服 = quần áo lao động bằng da nappa. TW dịch sai thành 彩頁服 ("trang màu"), VN chép theo thành "dịch vụ trang màu" — bịa hoàn toàn, không có cơ sở JP. Chỉ sửa gloss, giữ nguyên phần còn lại.

### 6. Key 1996 — 双鉄 — diễn đạt
- JP: 「そうだ。\n無論、実際に突き落とされてはたまらなかろうが――」
- TW: 「是的。當然，要是真扔下去可就不得了了……」
- Old VN: 「Đúng vậy.\nTất nhiên, nếu thực sự bị đẩy xuống thì gay go to——」
- Fix: 「Đúng vậy.\nTất nhiên, nếu thực sự bị đẩy xuống thì không chịu nổi mất——」
- Lý do: たまらなかろう = "không chịu nổi" (unbearable). "gay go to" vừa lệch nghĩa (chỉ "rắc rối" thay vì "không chịu nổi"), vừa lủng củng (đuôi "to" thừa).

### 7. Key 2423 — monologue — diễn đạt
- JP: 「こっくり、ハチロクはゆっくり頷く。」
- TW: 「八六輕輕地、緩緩地點了一下頭。」
- Old VN: "Gật đầu, Hachiroku chầm chậm gật đầu."
- Fix: "Hachiroku gật đầu chầm chậm."
- Lý do: こっくり + 頷く đều được dịch thành "gật đầu" → lặp từ trong một câu. Gộp thành một lần gật đầu, giữ ý "chầm chậm" (ゆっくり).

## Kiểm tra sweep っ-gasp
- Sweep có đúng **1 entry cho file này**: key 1755 (`lost-gasp-whole`, 「っ！」→「Ư!」) — đã verify và áp dụng (fix #4).
- Các っ khác trong file đã kiểm tra từng cái, đều GIỮ nguyên theo gasp boundary đã khóa:
  - 1759 うぉっ → "Oa." (tiếng cảm thán đã được dịch; sweep không flag; tương tự tiền lệ ハチロク01 2319).
  - 1788 うまいっ → "Ngon quá." (っ gắn từ nội dung, không phải gasp).
  - 2197 ならっ → "Vậy thì." (っ nhấn mạnh gắn từ nội dung).
  - 2890 パシャっ → "Tách" · 2889 むわあっ → "Phừng" · 2887 SFX (ぎゅっ――ごしっ――――バチっ！) → "(Chà——xát————Tách!)" (âm đã được diễn, không double-render).
  - 1813 ――っと → "——" (dấu gạch đã diễn đạt sự ngắt câu).
  - 1764 あははっ → "Ahaha," (tiếng cười, không phải gasp).
  - 1842 ばいっ, 2169 ばいっ (phương ngữ + "!!" đã đủ nhấn mạnh).
  - 1789 く、あ―― → "Kh, a——" (giữ "Kh" theo quy tắc đã khóa, không đổi sang Ư).
  - 2222 こほんっ → "khụ" (tiếng ho đã được dịch).
  - 1792 あっ―― → "A——" (đã diễn theo quy tắc).

## Kiểm tra tag %l và cấu trúc
- Tag `%l` cân bằng toàn file (số mở = số đóng, 0 lệch). Không có tag JP nào bị rơi gloss ở VN.
- Key 2905: VN thêm tag `\x%lNゲージ;#00ffc040;N-gauge%l;#;` trong khi JP không có tag — GIỮ. Gloss "N-gauge" đúng nội dung; gỡ tag sẽ để lại chữ JP thô trên màn hình. Ghi nhận, không tính sai.
- Key 2836: thứ tự 2 tag đảo so với JP do VN đảo trật tự câu — cả 2 tag đều đủ và đúng, không phải lỗi.
- `[selections]` trong TOML rỗng — không có gì để kiểm tra.
- Không có VN trống, không có VN == TW (không có dòng chưa dịch / placeholder tiếng Trung).
- Không có ký tự Trung/Hàn rò rỉ ngoài tag, không có "nuôi" (lỗi bịa 義→nuôi).

## Các điểm JP thắng TW (VN đã đúng — không sửa)
- 1391: JP お召し物 (quần áo) vs TW 食物 (đồ ăn) — VN "trang phục" theo JP, đúng.
- 1361: JP 欲しがるものが限られている (ít người muốn mua hơn) vs TW nói ngược lại (càng hiếm càng hot) — VN theo JP, đúng.

## Đã xác minh là đúng (không sửa, có bằng chứng project-wide)
- 2202 "Thị trưởng Paulette" (Hachiroku, ポーレット様): Paulette LÀ thị trưởng đương nhiệm (共通01 1390: "Thị trưởng hiện tại do Hinai Paulette đảm nhiệm"); "Thị trưởng Paulette" là cách dịch chuẩn project-wide cho ポーレット様.
- 1923 Soutetsu gọi Paulette là "cô" ("Theo lời cô vừa nói"): đã có tiền lệ — 共通05 2573, 共通07 2012 Soutetsu cũng gọi Paulette là "cô".
- 2603 "Michi" cho 路子: đã chuẩn project-wide (382 dòng dùng "Michi").
- 1937 Fukami "Anh Soutetsu" (双鉄さん → "anh Soutetsu"): đúng quy tắc Fukami.
- 2112 Fukami "Gisou, là gì." — romaji cho thuật ngữ đang được hỏi, chấp nhận được.
- 2209 Hibiki "Daiwaku?" — romaji cho cách đọc sai 台枠 của Hibiki, đúng ý đồ JP.
- 1673 すまんな → "Cảm ơn em nhé." — すまん dùng như lời cảm ơn khi nhận khăn, chấp nhận được.

## Xưng hô Soutetsu — đã kiểm tra toàn bộ, GIỮ nguyên
- Soutetsu có **0 dòng "anh"** trong file này; 25 dòng thoại dùng "tôi/Tôi": 1399, 1680, 1758, 1784, 1804, 1808, 1813, 1836, 1846, 1925, 1926, 1933, 1945, 1953, 1955, 1992, 2018, 2056, 2058, 2086, 2092, 2097, 2159, 2162, 2230.
- Tất cả đều là (a) nói với Hachiroku ("tôi" đúng) hoặc (b) phát biểu trước cả nhóm trong cuộc họp (giữ "tôi" theo tiền lệ Paulette 14 key 1544 — group address → "tôi").
- Trường hợp gần nhất: 1808 — Paulette trực tiếp mời Soutetsu nói tiếp, nhưng câu trả lời là tuyên bố quyết định trước toàn bộ cuộc họp → giữ "tôi". Ghi nhận để Hieu biết, không sửa.

## Chờ unification pass (KHÔNG sửa trong audit này — 18 dòng)
- 御一夜 → "Ohitoyo" (dạng cũ "Ohimitera", 10 dòng): 2908, 2839, 1926, 2827, 2829, 1345, 2086, 1936, 2049, 2894.
- 御一夜鉄道 → "Đường sắt Ohitoyo" (dạng cũ "Đường sắt Ohito", 2 dòng): 2109, 1710.
- まいてつ gloss "Maitetsu" → "chủ tàu" (5 dòng): 1361, 1394, 2475, 2224, 2041.
- 運転体 gloss "kíp lái" (1 dòng trong file này: 1719) — cần thống nhất toàn project: hiện có 3 dạng đang dùng lẫn lộn ("kíp lái" phổ biến nhất, "thân chính" ở 共通15, "thân điều khiển" ở ハチロク13). Đề xuất đưa vào unification pass thay vì sửa lẻ 1 dòng.

## TOML block (đã parse-verify: 7 key, 0 value mismatch vs JSON)

```toml
[script]
1685 = "「Đúng vậy nhỉ……nghe anh nói thế,\\ntôi cảm thấy đó có lẽ là cách tốt nhất.」"
1755 = "「Ư!」"
1996 = "「Đúng vậy.\\nTất nhiên, nếu thực sự bị đẩy xuống thì không chịu nổi mất——」"
2210 = "「Vậy, vì mọi người đã tập trung đông đủ rồi——\\nAnh Soutetsu. Nếu được, xin hãy tiếp tục câu chuyện ngày hôm qua.」"
2232 = "「Những ý kiến hay nguyện vọng đối với chính quyền thành phố——\\nAnh Soutetsu, anh định sẽ thu thập từ hiện trường đúng không?」"
2423 = "Hachiroku gật đầu chầm chậm."
2718 = "Tất nhiên, cả \\x%lナッパ服;#00ffc040;quần áo nappa%l;#; lẫn cán của \\x%lスクレイパー;#00ffc040;dao cạo xỉ than%l;#; đều đã\\nlấm lem bồ hóng và dầu mỡ, bẩn thỉu nhầy nhụa."
```

## Kết bài
File ハチロク01_双鉄の目・ハチロクの目: 394 dòng đã đọc hết, 7 dòng sai (1,78%) — 3 xưng hô Paulette→Soutetsu vi phạm B4 lock, 1 gasp theo sweep, 1 thuật ngữ bịa từ TW sai, 2 diễn đạt. Không có lệch dòng, rotation, nhiễm chéo, orphan hay dòng chưa dịch. 18 dòng dạng cũ (Ohimitera/Ohito/Maitetsu/kíp lái) để lại cho unification pass. Second pass: 7/7 re-verified, 0 removed, 0 corrected.
