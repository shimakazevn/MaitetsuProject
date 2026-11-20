# Audit — ハチロク11_御一夜鉄道小畑線.txt.toml (route 01_Hachiroku)

- File: `ハチロク11_御一夜鉄道小畑線.txt.toml` — route 01_Hachiroku, 460 dòng script.
- Nội dung: chạy thử nghiệm tuyến Okoba (vượt đèo Yatake, vòng lặp Okoba, dốc 25–30‰); bàn về Tablet / Railord là một chủng loài / sinh sản–nhân bản / niêm phong–Lõi Lord; Olivy từ chối đóng băng bảo quản; Hachiroku–Soutetsu–Paulette–Reina–Niiroku–Akai trên tàu 8620.
- Phương pháp: đọc toàn bộ 460/460 dòng đối chiếu JP + TW (CSV3), kiểm chứng chuỗi xoay vòng trên toàn dự án (91.731 dòng), quét っ toàn file, kiểm sweep, kiểm thẻ %l, kiểm đại từ Soutetsu.
- Kết quả: **29/460 dòng sai (6,3%)** — thoại 22/286, độc thoại 7/174. Phân loại: rotation 16, gasp 5, terminology 3, sfx 2, mistranslation 2, punctuation 1. Theo nhân vật: ポーレット 8, monologue 7, 双鉄 5, ハチロク 3, ニイロク 2, れいな 2, オリヴィ 1, 赤井 1.
- CSV bộ duy nhất 460 dòng, 0 key trùng, 0 VN trống; CSV↔TOML: 205 khớp tuyệt đối + 255 gộp `\n` thành khoảng trắng, 0 khác biệt thực chất; comment `# JP` 460/460 khớp CSV3. TOML md5 `31de0f3ff4f370e1a8520ae6cb2b841a`, BOM + CRLF, `[selections]` rỗng, không bản sao trùng.
- 0 misaligned ngoài chuỗi xoay §1 / 0 rotation khác / 0 contamination liên file (mọi VN lệch chỉ xuất hiện trong file này, đã kiểm toàn dự án) / 0 orphan / 0 untranslated / 0 duplicate key.

## §1. Chuỗi xoay vòng 16 dòng (lệch vị trí) — phát hiện chính của file

VN của 16 dòng bị dán lệch thành một chuỗi dài duy nhất (thoại ↔ độc thoại xen kẽ, vì key số không theo thứ tự truyện). Mỗi VN dưới đây đã được đối chiếu JP của key đích, và kiểm toàn dự án: mỗi VN lệch chỉ tồn tại ở đúng 1 key trong file này, không có ở file khác.

Chuỗi (VN ở key A thực ra là bản dịch của JP ở key B):

| VN đang ở key | Thực ra dịch JP của key | Nội dung |
|---|---|---|
| 2229 | 2668 | “Hãy chuẩn bị trước rồi đợi tôi nhé”——… (độc thoại: lời định nói bị ngón tay chặn lại) |
| 2668 | 1920 | “Hãy để em giúp ngài chuẩn bị nhé.” (Hachiroku: xin giúp Soutetsu chuẩn bị) |
| 1920 | 2237 | “Chuyện Cowcatcher em hiểu rồi. Thế còn Hibiki, anh Soutetsu đã nói chuyện chưa?” |
| 2237 | 2109 | “Tôi đã nói sơ qua rồi. Con bé tỏ ra rất hào hứng.” (Soutetsu: đã nói qua với Hibiki) |
| 2109 | 2214 | “Vậy thì, em sẽ chính thức bàn bạc với Hibiki. Chuyện đó, anh cứ yên tâm kỳ vọng nhé.” (Paulette) |
| 2214 | 1871 | “Vậy sao. Chắc hẳn Olivy cũng sẽ rất vui.” (Soutetsu) |
| 1871 | 2131 | “Và, còn một chuyện nữa——” (Paulette) |
| 2131 | 2748 | “Giọng Paulette trở nên căng thẳng. Nên tôi có thể dễ dàng đoán được những lời tiếp theo.” (độc thoại) |
| 2748 | 1289 | “...Những chuyện từ nãy đến giờ, em cũng chưa được nghe.” (Paulette) |
| 1289 | 2580 | “Nói rồi, Paulette nhẹ nhàng vuốt tóc Reina đang nằm trên đùi.” (độc thoại) |
| 2580 | 2059 | “Reina, em có biết không?” (Paulette hỏi Reina) |
| 2059 | 1748 | “Hơ? Chuyện gì cơ ạ?” (Reina) |
| 1748 | 2777 | “Có lẽ là do nãy giờ em ấy cứ ngủ gật. Trông Reina có vẻ hơi bối rối.” (độc thoại) |
| 2777 | 1915 | “Chuyện Railord có thể được tạo ra như một chủng loài. Chuyện Tablet có thể sinh sản... nhân bản? được ấy.” (Paulette) |
| 1915 | 2065 | “Reina mới nghe lần đầu tiên luôn đó ạ.” (Reina) |
| 2065 | 2779 | “Khuôn mặt Reina tươi cười rạng rỡ. Từ biểu cảm đó, chỉ có thể cảm nhận được niềm vui.” (độc thoại) |

Chuỗi đứt ở 2779: VN của 2779 đã đúng với JP của chính nó (độc thoại mặt Reina cười rạng rỡ) và đã xuất hiện ở cả 2065 lẫn 2779 — tức bản dịch của 2779 bị nhân đôi, còn bản dịch đúng của 2229 (Hachiroku: 「でしたら、ね？ 双鉄さま」) không có ở bất cứ đâu trong dự án (đã tìm toàn bộ 91.731 dòng). Cách sửa:

- 15 dòng nhận lại VN đã dời nguyên văn từ key nguồn trong chuỗi (kiểm cơ học: fix == VN hiện tại của key nguồn, 15/15).
- 2229 dịch mới từ JP (không bịa thêm): 「Nếu vậy thì, đúng không ạ, ngài Soutetsu?」 — Hachiroku hỏi Soutetsu, giữ cách xưng “ngài Soutetsu”.
- 2779 giữ nguyên (đã đúng, không tính sai); 2065 nhận VN từ 1915.

Bằng chứng then chốt cho từng mắt xích (JP đích ↔ VN dời):
- 1289 JP 「……ここまでの話は、わたしも、聞いてませんでした」 ↔ VN ở 2748 “…em cũng chưa được nghe.”; 2748 JP (độc thoại “giọng Paulette cứng lại, dễ đoán lời tiếp theo”) ↔ VN ở 2131; 2131 JP 「それで、もうひとつの話なんですけど――」 ↔ VN ở 1871 “Và, còn một chuyện nữa——”; 1871 JP 「そうか。オリヴィもさぞ喜ぼう」 ↔ VN ở 2214 “Chắc hẳn Olivy cũng sẽ rất vui.”; 2214 JP (Paulette hẹn bàn chính thức với Hibiki) ↔ VN ở 2109; 2109 JP 「軽くは話してある。本人は、大いに意欲を示していたな」 ↔ VN ở 2237 “Tôi đã nói sơ qua rồi. Con bé tỏ ra rất hào hứng.”; 2237 JP (Cowcatcher + hỏi Soutetsu đã nói với Hibiki chưa) ↔ VN ở 1920; 1920 JP 「お支度、お手伝いさせてくださいまし」 ↔ VN ở 2668 “Hãy để em giúp ngài chuẩn bị nhé.”; 2668 JP (độc thoại “lời định nói bị ngón tay mềm chặn lại”) ↔ VN ở 2229; 2580 JP (độc thoại “Paulette vừa nói vừa vuốt tóc Reina trên đùi”) ↔ VN ở 1289; 2059 JP 「れいなは、知ってた？」 ↔ VN ở 2580 “Reina, em có biết không?”; 1748 JP 「ほぇ？ なにをですかぁ？」 ↔ VN ở 2059 “Hơ? Chuyện gì cơ ạ?”; 2777 JP (độc thoại Reina ngủ gật, mặt bối rối) ↔ VN ở 1748; 1915 JP (Paulette: Railord là chủng loài, Tablet sinh sản–nhân bản) ↔ VN ở 2777 (giữ nguyên 4 thẻ %l khớp JP); 2065 JP 「れいな、はじめて聞きましたぁ」 ↔ VN ở 1915 “Reina mới nghe lần đầu tiên luôn đó ạ.”; 2779 JP (độc thoại mặt Reina cười rạng rỡ) ↔ VN ở 2065 và ở chính 2779 (trùng lặp).
- Chu trình khép kín qua 15 mắt xích, chỉ thiếu đúng VN của 2229 (dịch mới) và thừa một bản sao của 2779.

## §2. Các lỗi còn lại (13 dòng)

### 2.1 Gasp っ mất âm (5 dòng)
- 1736 (双鉄): JP 「中味――とは――っ！！」 — VN cũ 「Nội dung——là sao——!!」 → thêm Ư: 「Nội dung——là sao——Ư!!」 (mục sweep, đã kiểm chứng).
- 1739 (ニイロク): JP 「っ！！！！？」 — VN cũ 「!!!!?」 → 「Ư!!!!?」 (mục sweep).
- 1781 (双鉄): JP 「っ！！？」 — VN cũ 「!!?」 → 「Ư!!?」 (mục sweep; lưu ý: mục sweep ghi tên file lỗi font `��一夜`, nhưng key + JP/TW/VN khớp đúng file này).
- 2202 (双鉄): JP 「っ！！？ オリヴィっ！？ オリヴィ！！！」 — VN cũ 「!!? Olivy!? Olivy!!!」 → 「Ư!!? Olivy!? Olivy!!!」 (sweep bỏ sót, audit tự tìm: っ đầu dòng mất hẳn).
- 2858 (monologue): JP 「姿がどこにも――どこにも――っ！！？」 — VN cũ 「...không thấy đâu——!!?」 → 「...không thấy đâu——Ư!!?」 (mục sweep).
- Quét bổ sung toàn bộ 170 dòng JP có っ: các っ còn lại đều là nhấn mạnh cuối câu gắn với từ (うむっ, あっ, なのっ, さまっ, フルギアっ, 20っ, まだーっ, 越えられないっ, 撒きますっ, 砂撒きっ, 非常ーっ) hoặc đã diễn (1741 っ！？→“Hử!?”, 1758 あっ→“á”, 1805 うむっ！？→“Hử!?”) — không thêm Ư, đúng quy tắc.

### 2.2 SFX fa mất âm f (2 dòng)
- 1744 (オリヴィ): JP 「ふぁ」 (sau 「ウンメーテキ！！！」) — VN cũ 「Oa」 → 「Phà」 (quy tắc đã chốt: ふぁ→“phà”; “Oa” mất hẳn âm f).
- 1772 (ハチロク): JP 「ふあ」 — VN cũ 「Oa」 → 「Phùa」 (ふあ→“phùa”).

### 2.3 Thuật ngữ 冥国 (3 dòng)
- 1851 (ポーレット): 冥国 → VN cũ “Meikoku” → “Minh Quốc” (quy tắc đã chốt; TW 美國 không thắng JP).
- 2023 (ポーレット): 冥国式 Railord → “kiểu Meikoku đời cũ” → “kiểu Minh Quốc đời cũ”.
- 2575 (monologue): 冥国式 Railord → “kiểu Meikoku” → “kiểu Minh Quốc”.

### 2.4 Sai nghĩa nhỏ — thêm “vì” (2 dòng)
- 2191 (赤井): JP 「それは――」 — VN cũ 「Đó là vì——」 → 「Đó là——」 (JP không có quan hệ nguyên nhân).
- 2193 (ニイロク): JP 「それは？」 — VN cũ 「Là vì?」 → 「Là gì vậy?」 (Niiroku hỏi “đó là gì?”, không phải “vì sao?”; cặp với 2191).

### 2.5 Dấu câu (1 dòng)
- 2600 (monologue): JP 『日ノ本三大車窓』 — VN cũ “...đẹp nhất Hinomoto' thực sự...” (mất dấu mở ngoặc, còn trơ dấu đóng) → “...đẹp nhất 'Hinomoto' thực sự...”.

## §3. Sweep っ — đối chiếu
- Sweep có 4 mục cho file này: 1736, 1739, 1781, 2858 — cả 4 đã kiểm chứng đúng JP, áp nguyên.
- Audit tự tìm thêm 1 mục sweep bỏ sót: 2202 (っ đầu dòng).
- 6 mục sweep còn lại mang tên ハチロク11_幽霊 là file khác, không thuộc file này.

## §4. Thẻ %l
- JP 71 dòng có thẻ, VN 74 dòng — chênh 3 dòng đều là VN chuyển ruby JP thành thẻ %l nhưng chữ hiển thị đúng, không tính sai (tiền lệ 日々姫03): 1652 (力行 ruby → thẻ), 2055 (力行 ruby → thẻ), 1827 (逆転機締切率 ruby → thẻ 逆転機), 2262 (止弁 ruby → thẻ). Sau khi sửa chuỗi xoay, thẻ %l khớp JP tuyệt đối ở mọi dòng (1915: 4 thẻ khớp JP).
- Không có thẻ %l nào thiếu dấu `;`, không có marker ruby `[ruby]` còn sót trong VN.

## §5. Đại từ và thuật ngữ khác
- Soutetsu: toàn file dùng “tôi” với Hachiroku — đúng quy tắc (“tôi” với Hachiroku/Mayami/Minokasa/Kisaki). Dòng duy nhất có “anh” ở thoại Soutetsu (2109) là VN lệch của Paulette, đã trả về đúng key 2214 theo chuỗi xoay; sau khi sửa không còn lỗi đại từ nào. Paulette→Soutetsu “anh Soutetsu” đúng khóa B4 (2189, 2214 sau sửa, 2237 sau sửa). Hachiroku tự xưng “em”, gọi Soutetsu “ngài Soutetsu” — nhất quán.
- 御一夜 dạng cũ chờ đợt thống nhất, KHÔNG tính sai (tiền lệ các file trước): “Ohimitera” 3 dòng (1201, 2011, 2664), “Đường sắt Ohito” 2 dòng (2121, 2446). “Ohitoyo” đúng dạng đã dùng ở 2002, 2077.
- 日ノ本 → “Hinomoto” 4 dòng (1987, 2078, 2600, 2718) — chờ Hieu chốt “Hinomoto” vs “Hinamoto” (đã cờ ở 日々姫03), giữ nguyên.
- Cười うふふ: 1819 (れいな) “U hu hu~”, 1820 (ポーレット) “U hu hu”, 2751 (monologue) “Cười u hu hu” — đều diễn thành tiếng cười, không phải tiếng rên, giữ nguyên theo quy tắc SFX ngẫu hứng của Hieu.
- 2197: 運転士 và 機関士 cùng gloss VN “người lái tàu” (chữ hiển thị phân biệt bằng “tàu điện” / “hơi nước”) — ghi chú, không tính sai; quy tắc đã chốt cho 機関士 là “thợ lái đầu máy” / ngắn “lái tàu”, nhưng gloss ở đây không sai nghĩa.
- 1756: JP 「！」 → VN 「!」 — khớp JP (TW có 唔 nhưng JP thắng), giữ.
- 2682: JP 「教わっている。」 cụt câu, VN “Tôi đã được dạy.” khớp JP, không bịa thêm, giữ.

## §6. Khối TOML (đã parse-kiểm chứng)
- JSON 29 mục dạng chuẩn (key chuỗi); khối TOML 29 khóa, 0 sai lệch giá trị (tomllib).
- jp/tw/old_vn khớp CSV3 tuyệt đối 29/29.
- Kiểm diff-sanity: 13 fix phi-xoay chỉ khác VN cũ ở đúng chỗ sửa (thêm Ư / đổi Oa→Phà·Phùa / Meikoku→Minh Quốc / bỏ “vì” / thêm dấu '); 15 fix xoay là dời nguyên văn VN từ key nguồn (kiểm cơ học 15/15 verbatim); 2229 dịch mới, không có trong dự án.
- Lượt soát 2: 29/29 tái kiểm chứng, 0 bỏ, 2 sửa (1851, 2023: bản nháp đầu làm rơi cặp 「」 của VN cũ, đã sửa lại).

```toml
[script]
"1289" = "「...Những chuyện từ nãy đến giờ, \\nem cũng chưa được nghe.」"
"1736" = "「Nội dung——là sao——Ư!!」"
"1739" = "「Ư!!!!?」"
"1744" = "「「ĐỊNH MỆNH!!」\\n「Phà」」"
"1748" = "「Hơ? Chuyện gì cơ ạ?」"
"1772" = "「「A」\\n「Phùa」」"
"1781" = "「Ư!!?」"
"1851" = "「Sản xuất hàng loạt, tiêu thụ hàng loạt... \\nĐó là hình thức cơ bản của việc chế tạo ở Minh Quốc mà.」"
"1871" = "「Vậy sao. Chắc hẳn Olivy cũng sẽ rất vui.」"
"1915" = "「Chuyện \\x%lレイルロオド;#00ffc040;Railord%l;#; có thể được tạo ra như một chủng loài. \\nChuyện \\x%lタブレット;#00ffc040;Tablet%l;#; có thể sinh sản... nhân bản? được ấy.」"
"1920" = "「Hãy để em giúp ngài chuẩn bị nhé.」"
"2023" = "「Đối với \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc đời cũ, \\nbản thân chức năng niêm phong không hề tồn tại——cũng có tin đồn như vậy.」"
"2059" = "「Reina, em có biết không?」"
"2065" = "「Reina mới nghe lần đầu tiên luôn đó ạ.」"
"2109" = "「Tôi đã nói sơ qua rồi. \\nCon bé tỏ ra rất hào hứng.」"
"2131" = "「Và, còn một chuyện nữa——」"
"2191" = "「Đó là——」"
"2193" = "「Là gì vậy?」"
"2202" = "「Ư!!? Olivy!? Olivy!!!」"
"2214" = "「Vậy thì, em sẽ chính thức bàn bạc với Hibiki. \\nChuyện đó, anh cứ yên tâm kỳ vọng nhé.」"
"2229" = "「Nếu vậy thì, đúng không ạ, ngài Soutetsu?」"
"2237" = "「Chuyện Cowcatcher em hiểu rồi. \\nThế còn Hibiki, anh Soutetsu đã nói chuyện chưa?」"
"2575" = "Một \\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc không có Master cụ thể, \\nđược vận hành trong hệ thống của Teitetsu."
"2580" = "Nói rồi, \\nPaulette nhẹ nhàng vuốt tóc Reina đang nằm trên đùi."
"2600" = "Một trong ba khung cảnh qua cửa sổ đẹp nhất 'Hinomoto' thực sự, \\nkhông phải là thứ mà chúng tôi đã nhận nhầm, Niiroku đang tận hưởng nó một mình."
"2668" = "\"Hãy chuẩn bị trước rồi đợi tôi nhé\"—— \\nLời vừa định nói ra đã bị những đầu ngón tay mềm mại chặn lại."
"2748" = "Giọng Paulette trở nên căng thẳng. \\nNên tôi có thể dễ dàng đoán được những lời tiếp theo."
"2777" = "Có lẽ là do nãy giờ em ấy cứ ngủ gật. \\nTrông Reina có vẻ hơi bối rối."
"2858" = "Nghe vậy, tôi mới nhận ra. \\nBóng dáng em ấy không thấy đâu——không thấy đâu——Ư!!?"
```

## Kết bài
File ハチロク11_御一夜鉄道小畑線: 29/460 dòng sai (6,3%) — chuỗi xoay vòng 16 dòng là lỗi hệ thống chính (15 dời nguyên văn + 2229 dịch mới, bản dịch đúng của 2229 không có trong dự án; bản dịch của 2779 bị nhân đôi ở 2065), cộng 5 gasp っ mất âm (4 sweep + 2202 tự tìm), 3 thuật ngữ 冥国→Minh Quốc, 2 SFX fa mất âm f, 2 dòng thêm “vì” thừa, 1 dấu ngoặc lẻ. Không có dòng mồ côi, không nhiễm liên file, không dòng chưa dịch. Chờ Hieu (không tính sai): “Ohimitera”/“Đường sắt Ohito” 5 dòng chờ đợt thống nhất; 日ノ本 “Hinomoto” vs “Hinamoto” 4 dòng.
