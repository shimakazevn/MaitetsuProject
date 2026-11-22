# Moan-fix — lr_ニイロクh_誓い。約束.txt.toml (08_Niiroku)

File: `08_Niiroku/lr_ニイロクh_誓い。約束.txt.toml` — Niiroku + Akai (Kiyoharu) thề ước, học làm tình từ sách của "chị Shiro", làm tình lần đầu (mở niêm phong Sealing); phần lớn file là H-scene với độc thoại dài của Akai xen kẽ. Không có Soutetsu.
Phương pháp: đọc từng dòng đối chiếu JP + TW (CSV3), rà lại toàn bộ 53 fix rên của audit + 7 mục gasp sweep, xét lại mọi dòng rên/SFX còn lại theo quy tắc romaji (MOAN-BRIEF.md).

## 1. Tổng kết
- Đọc: **320/320 dòng** (key 945–2072).
- Xét: **126 dòng rên/SFX** (93 thoại rên/thở/gasp/cười + 29 SFX trong ngoặc ở độc thoại + 4 độc thoại nuốt/thở: 965, 1746, 1816, 1946).
- Đổi: **38 dòng** (34 romaji + 4 đếm nguyên âm — 1271 và 1292 vừa romaji vừa đếm nguyên âm, tính 1 lần).
- Giữ: **88 dòng rên/SFX**.
- Không sửa dòng nào ngoài rên (không đại từ/thuật ngữ/nghĩa; 945 sai nghĩa, 1300 sai nghĩa, 1346 sai nghĩa, 1675 sai nghĩa, 1517 bịa thêm, 1545 bịa hoàn thiện câu — đã sửa trong audit, đã gộp; 1300 giữ nguyên phần nghĩa "chỗ đó" của audit trong giá trị moan).
- 31/38 dòng sửa xây trên giá trị audit cùng key (chỉ đổi đúng token rên, giữ nguyên các phần khác của audit — kể cả Ư gasp); 7 dòng audit bỏ sót (1275, 1339, 1342, 1392, 1468, 1516, 1569). Áp MỘT giá trị moan cho mỗi key ở đợt build, không áp cả hai.

## 2. Kiểm tra file
- TOML md5: `baf71db80b8ef4a9e7bfd57bf6313b21` (khớp md5 audit). Không có bản trùng.
- CSV3: 1 bộ duy nhất, 320 dòng, 0 trùng khóa. JP trong comment TOML khớp CSV3 JP 320/320 (kiểm chứng qua flat-match của audit).
- JSON: 38 mục, key dạng chuỗi, list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 38/38. Fix values dùng `\n` literal (không newline thật) theo chuẩn CSV3. Tất cả 38 dòng đều là ニイロク.
- Khối TOML: 38 khóa, parse bằng tomllib OK, 0 sai lệch giá trị so với JSON. Mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff cơ học 38/38 — xem §4; diff với giá trị audit cho 31 dòng chồng chéo cũng chỉ chạm đúng token rên).
- Không còn っ thô trong VN (0 dòng). Không có dòng "Kh" (glottal-stop っ) nào trong file — các "Kh" tìm thấy đều là từ Việt ("Không", "Khẽ", "khát"...), không đụng.

## 3. Kiểm tra lại fix rên của audit (53 dòng)
Audit đã làm rất kỹ họ romaji cho file này — **giữ nguyên toàn bộ giá trị audit, trừ đúng token fa/fu (chuyển sang romaji) và 4 chỗ đếm nguyên âm (xem §4)**:
- **Romaji họ ひゃ/ひゅ/ひあ/きゃ + mở rộng (19 dòng) — giữ nguyên:** 1256 Hyau, 1258 Kyua/Áu/Nkyu, 1260 Hyau/Hiu, 1261 Hia/Ya, 1264 Hia, 1265 Hyan ư ư, 1267 Hyau, 1268 Kyau, 1269 Kua, 1274 Nku, 1282 Fukyu, 1305 Fue, 1334 Kuuuuuun ư ư, 1336 Kyuuunn, 1351 Nkyu×17u, 1358 Nhyu, 1363 Nyu×17u, 1572 Hia. Đếm nguyên âm kiểm chứng lại độc lập bằng máy: 1334 6u (く1 + う1 + ぅ4), 1336 3u+2n, 1351 17u (キュ1 + ゥ16), 1363 17u (ゆ1 + う/ぅ16) — khớp kiểm chứng của audit.
- **Gasp Ư (12 dòng) — KHÔNG đụng (quy tắc khóa):** 1272, 1292, 1318, 1319, 1323, 1324, 1325, 1360, 1365, 1381, 1474, 1580. Trong đó 1272/1292/1381 có token fa kèm theo — giá trị moan giữ nguyên phần Ư của audit, chỉ đổi token fa.
- **Vowel (22 dòng) — giữ đếm của audit, chỉ đổi token fa sang romaji (trừ 1317):** 1278 4a/4a, 1280 2a, 1288 aa/ha ư, 1337 Kiyoharuu, 1438 3a — đếm lại đúng; 1297 ふうっ→"phùu" (2u) đúng; 1317 はうっ→"Ha ư" giữ nguyên (không có token fa).
- **SFX audit (1260, 1385, 2047, 2050, 2069) — giữ nguyên:** ずりゅ→"trượt", あうっ→"áu" (2 vần), 2047 "Trượt"+49t, 2050 "ư ư" (2 tiếng ku), 2069 "Trượt!".

## 4. Danh sách sửa (38 dòng)

### 4A. Họ fa/fu → romaji (34 dòng)
Quy tắc chung: "phà"/"phùa" nghe gượng trong rên → romaji (quy tắc duyệt 21/11 ~01:56; tiền lệ ふかみh1/h2/h3, ポーレットh5, ハチロクh5/h6/h9 — fa/fu chuyển hết sang Fa/Fua/Pua). Audit sửa các dòng này từ "phù" (mất âm a) thành "phà"/"phùa" TRƯỚC quy tắc romaji; bản moan này thay thế bằng romaji. `old_vn` trong JSON là VN gốc CSV3 ("phù"); giá trị fix là giá trị cuối cùng (romaji). Chữ hoa/thường theo vị trí VN cũ (đầu dòng "Phùa"→"Fua", giữa dòng "phùa"→"fua" — tiền lệ ハチロクh5).
- **1271** [ニイロク] — ふあっ→Fua; はあっ×4→"hàà" (xem §4B).
  - JP: 「ふあっ──はっ──あっ──あっ──っっ、んっ── / はあっ──はあっ──はあっ──はあっ──」
  - Cũ (CSV3): 「Phù──hà──a──a──ư, ưm── / nhà──hà──hà──hà──」
  - Giá trị audit đã gộp: 「Phùa──hà──a──a──ư ư, ưm── / hà──hà──hà──hà──」
  - Sửa (moan): 「Fua──hà──a──a──ư ư, ưm── / hàà──hàà──hàà──hàà──」
  - Lý do: ふあっ→"Fua"; はあっ = 2 a mỗi hơi (xem §4B). Giữ "hà" cho はっ đầu dòng (1 a, đúng) và Ư ư của audit.
- **1272** — ふあっ→"Fua".
  - JP: 「ふあっ──あっ──あっっっ──あああっ──」 / Cũ: 「Phù──a──a──aaa──」 / Audit: 「Phùa──a──a ư ư ư──aaa──」 / Sửa: 「Fua──a──a ư ư ư──aaa──」
  - Lý do: ふあっ→"Fua"; giữ "a ư ư ư" và "aaa" của audit.
- **1274** — ふ、ぁ→"Fu, a".
  - JP: 「は……ぁっ──んっ──これ……ふ、ぁ── / きもちい──ん……んくっ──あ……んっ──」 / Cũ: 「Hà... a──ưm──cái này... phù, a── / sướng quá──ưm... ưm──a... ưm──」 / Audit: 「Hà... a──ưm──cái này... phù, a── / sướng quá──ưm... Nku──a... ưm──」 / Sửa: 「Hà... a──ưm──cái này... Fu, a── / sướng quá──ưm... Nku──a... ưm──」
  - Lý do: ふ、ぁ là cặp mora ふあ bị tách bởi dấu phẩy — "phù" sai vần cho ふ (audit file 凪ふかみh2 đã lý luận ふあ là Fua, không phải "phù"; tiền lệ ハチロクh9 đổi 5 dòng ふ、あっ→"Fu, a", lr-ポーレットh1 dùng "Fu, a" cho ふ、あ). Giữ "Nku" của audit và "Hà... a" (は……ぁっ = 2 a tách bởi ……).
- **1276** — ふあっ→"Fua". JP: 「ふあっ」 / Cũ: 「Phù.」 / Audit: 「Phùa.」 / Sửa: 「Fua.」
- **1277** — ふああああああああああああっ (12 あ)→"Fuaaaaaaaaaaaa".
  - JP: 「ふああああああああああああっ！！！！！！！！」 / Cũ: 「Phù aaaaaaaaaaaaaa!!!!!!!!」 (14 a) / Audit: 「Phù aaaaaaaaaaaa!!!!!!!!」 (12 a) / Sửa: 「Fuaaaaaaaaaaaa!!!!!!!!」
  - Lý do: đếm bằng máy: JP 12 あ, "Fu" + 12 a. Giữ số a của audit, chỉ đổi hệ diễn.
- **1278** — ふあっ→"Fua" ×2.
  - JP: 「はあああんっ！ ふあっ！ あっ！ おく、なかっ！ / ふあっ！ あっ！ あっ！ ああああっ！！！！！」 / Audit: 「Hà aaa! Phùa! A! Sâu, bên trong! / Phùa! A! A! Aaaa!!!!!」 / Sửa: 「Hà aaan! Fua! A! Sâu, bên trong! / Fua! A! A! Aaaa!!!!!」
  - Lý do: giữ đếm của audit (はあああん = 4 a, ああああ = 4 a). [Parent sửa khi merge 22/11 ~04:55: khôi phục ん cuối token 1 → "Hà aaan" — JP はあああんっ = 4 a + ん; audit và agent đều chỉ đếm nguyên âm nên bỏ sót ん. Tiền lệ giữ ん: 1336 "Kyuuunn" (2n), hibikih1 1115 (3n).]
- **1280** — ふあっ→"Fua". JP: 「ふあっ！ あっ！ あっ！ あっ！！ / あっ！ あっ！ あっ！ ああっ！！！」 / Audit: 「Phùa! A! A! A!! / A! A! A! Aa!!!」 / Sửa: 「Fua! A! A! A!! / A! A! A! Aa!!!」 (giữ "Aa" cho ああっ = 2 a.)
- **1281** — ふあっ→"Fua". JP: 「ふあっ！ あっ！ あっ！ あっ！ / あっ！ あっ！ あっ！ あっ！！！」 / Audit: 「Phùa! A! A! A! / A! A! A! A!!!」 / Sửa: 「Fua! A! A! A! / A! A! A! A!!!」
- **1282** — ふあっ→"Fua".
  - JP: 「ふきゅっ！ んっ──ふあっ！ ちかっ、って！！ / あああ！ っ！ 回路、ショート、する、みたい、でっ」 / Audit: 「Fukyu! Ưm──phùa! Chớp chớp, chớp chớp!! / Aaa! Ư! Mạch điện, cứ như, sắp chập, mất」 / Sửa: 「Fukyu! Ưm──Fua! Chớp chớp, chớp chớp!! / Aaa! Ư! Mạch điện, cứ như, sắp chập, mất」
  - Lý do: giữ "Fukyu" và "Ư" của audit; chỉ đổi token fa.
- **1285** — ふあっ→"Fua". JP: 「ふあっ！ きもちいっ──とけるっ！ とけちゃうっ、 / おんなのこ──とけ、てっ──どろって、しちゃうっ！」 / Audit: 「Phùa! Sướng quá──tan chảy mất! Tan chảy mất thôi, / bé gái──đang, tan chảy──nhũn ra, mất thôi!」 / Sửa: 「Fua! Sướng quá──tan chảy mất! Tan chảy mất thôi, / bé gái──đang, tan chảy──nhũn ra, mất thôi!」
- **1288** — ふあっ→"Fua". JP: 「ふあっ！？ あっ──ああっ──はうっ──んっ。 / ちょくせつ──すり、すり──凄い、さっきよりっ」 / Audit: 「Phùa!? A──aa──ha ư──ưm. / Trực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」 / Sửa: 「Fua!? A──aa──ha ư──ưm. / Trực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」 (giữ "aa" cho ああっ và "ha ư" cho はうっ.)
- **1290** — ふあっ→"Fua". JP: 「ふあっ！？ あっ──ちつ──ね、おんなのこ── / さっき、まで──痛くてっ──くるし、かったのにっ」 / Audit: 「Phùa!? A──âm đạo──nè, bé gái── / lúc nãy, vẫn còn──đau đớn──khó chịu, thế mà」 / Sửa: 「Fua!? A──âm đạo──nè, bé gái── / lúc nãy, vẫn còn──đau đớn──khó chịu, thế mà」
- **1291** — ふあっ→"Fua". JP: 「ふあっ！？──あっ──！」 / Audit: 「Phùa!?──A──!」 / Sửa: 「Fua!?──A──!」
- **1292** — ふあああああっっっ→"Fuaaaaa ư ư ư"; はあっ→"Hàà" (xem §4B).
  - JP: 「はあっ！？ うっ──あっ──ふあああああっっっ」 / Cũ: 「Hà!? Ư──a──phù aaaaa」 / Audit: 「Hà!? Ư──a──phù aaaaa ư ư ư」 / Sửa: 「Hàà!? Ư──a──Fuaaaaa ư ư ư」
  - Lý do: ふ + あ×5 → "Fuaaaaa" (5 a, đếm bằng máy); giữ ư ư ư của audit cho っっっ.
- **1293** — ふあっ→"Fua". JP: 「ふあっ！？ 指──清春──清春の、指、がっ── / おっぱい──んっ──おっぱい──自分の、おっぱいを」 / Audit: 「Phùa!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu── / ngực──ưm──ngực──đang sờ ngực, của em」 / Sửa: 「Fua!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu── / ngực──ưm──ngực──đang sờ ngực, của em」
- **1294** — ふあっ→"Fua". JP: 「ふあっ！？ そこ──そこっ、うそっ！？ / そんなとこ──くぱって、開く──の？」 / Audit: 「Phùa!? Chỗ đó──chỗ đó, đùa sao!? / Chỗ như thế──mà tách ra, được──sao?」 / Sửa: 「Fua!? Chỗ đó──chỗ đó, đùa sao!? / Chỗ như thế──mà tách ra, được──sao?」
- **1297** — ふ、ぁ→"Fu, a".
  - JP: 「はっ──あっ──ふうっ、ん──ベロっ──ぺろぺろっ、 / ふ、ぁ──ここも──すごく──きもち、いいっ」 / Audit: 「Hà──a──phùu, ưm──lưỡi──liếm liếm, / phù, a──chỗ này cũng──rất──sướng, ạ.」 / Sửa: 「Hà──a──phùu, ưm──lưỡi──liếm liếm, / Fu, a──chỗ này cũng──rất──sướng, ạ.」
  - Lý do: như 1274 (cặp ふあ tách dấu phẩy). Giữ "phùu" của audit cho ふうっ (ふ + う = 2 u, hơi thở đơn — không phải họ fa).
- **1300** — ふあっ→"Fua".
  - JP: 「はっ──んっ──うっ──ふあっ──おちん、ちっ、 / んうっ、ごりって──ごりって──してるとこっ」 / Audit: 「Hà──ưm──ư──phùa──ch-chim, / ưm, chỗ cứng──chỗ cứng──chỗ đó」 / Sửa: 「Hà──ưm──ư──Fua──ch-chim, / ưm, chỗ cứng──chỗ cứng──chỗ đó」
  - Lý do: chỉ đổi token fa; giữ nguyên phần nghĩa "chỗ đó" của audit.
- **1322** — ふあっ→"fua" (giữa dòng, viết thường).
  - JP: 「！ ならっ、これ、愛撫っ──ンっ──こしゅ。こしゅ、 / で──気持ち、よく、して、くれてるの──ふあっ」 / Audit: 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ, / thế này──là đang làm cho em, sướng──phùa.」 / Sửa: 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ, / thế này──là đang làm cho em, sướng──fua.」
- **1336** — ぷあっ→"Pua".
  - JP: 「んっ──きゅううんんっ────んっ──ぷあっ！ / あっ！ あっ！ あっ！ あああっ！！！！！」 / Audit: 「Ưm──Kyuuunn────ưm──phùa! / A! A! A! Aaa!!!!!」 / Sửa: 「Ưm──Kyuuunn────ưm──Pua! / A! A! A! Aaa!!!!!」
  - Lý do: giữ "Kyuuunn" của audit (きゅううんん = 3u + 2n).
- **1337** — ぷあっ→"pua" (giữa dòng, viết thường).
  - JP: 「ん………………ぷあっ──えへへっ── / きよはる──きよはるぅ」 / Audit: 「Ưm.................. phùa──e he he── / Kiyoharu──Kiyoharuu」 / Sửa: 「Ưm.................. pua──e he he── / Kiyoharu──Kiyoharuu」
  - Lý do: giữ "Kiyoharuu" của audit (きよはるぅ = +1 u) và "e he he" cho えへへっ (tiếng cười).
- **1339** — ふっ、あ→"Fu, a" (audit bỏ sót).
  - JP: 「うん……ふっ、あ──できる。そのくらい、もちろん」 / Cũ: 「Vâng... phù, a──em làm được. Cỡ đó thì, tất nhiên rồi.」 / Sửa: 「Vâng... Fu, a──em làm được. Cỡ đó thì, tất nhiên rồi.」
  - Lý do: như 1274 (cặp ふあ tách dấu phẩy).
- **1342** — ふっ──ぁ→"Fu──a" (audit bỏ sót).
  - JP: 「ん……ね？ あいぶ──ん……あいぶの、あいって── / ふっ──ぁ──あいって──字──は──恋愛の、愛？」 / Cũ: 「Ưm... này? Ái ân vuốt ve──ưm... chữ ái, trong ái ân vuốt ve── / phù──a──chữ ái──đó──là──chữ ái trong tình ái, yêu đương sao?」 / Sửa: 「Ưm... này? Ái ân vuốt ve──ưm... chữ ái, trong ái ân vuốt ve── / Fu──a──chữ ái──đó──là──chữ ái trong tình ái, yêu đương sao?」
  - Lý do: như 1274 (cặp ふあ tách bởi ──); giữ dấu ── làm nhịp ngắt.
- **1353** — ぷあっ→"pua" (giữa dòng, viết thường).
  - JP: 「んむっ！？ ん……ちゅっ──ちゅむっ──ぷあっ、 / んっ──ちゅずっ──ちゅっ──れるっ──ちゅるっ」 / Audit: 「Ưm!? Ưm... chụt——chụt——phùa, / ưm——chụt——chụt——liếm——rột」 / Sửa: 「Ưm!? Ưm... chụt——chụt——pua, / ưm——chụt——chụt——liếm——rột」
  - Lý do: giữ họ ちゅ→"chụt" của audit (đúng, xem §5).
- **1356** — ふ、ゅっ→"Fu, yu" (audit giữ "Phù, ư" — xem Cờ F5).
  - JP: 「んきゅっ！ んうっ！ ふ、ゅっ──みゅっ── / んううううううっ──！！」 / Cũ: 「Ưm! Ưm! Phù, ư──ưm── / ưmmmmmm──!!」 / Audit: 「Nkyu! Ưm! Phù, ư──Myu── / ưmmmmmm──!!」 / Sửa: 「Nkyu! Ưm! Fu, yu──Myu── / ưmmmmmm──!!」
  - Lý do: ふ、ゅ là cặp ふ + ゅ tách bởi dấu phẩy — "phù" sai vần cho ふ ngắn (phù = ふぅ), "ư" làm mất hẳn phụ âm y của ゅ (tiền lệ 凪h2: ゅっ→"Yu"). Giữ "Nkyu"/"Myu" và "ưmmmmmm" của audit.
- **1358** — ふあっ→"Fua".
  - JP: 「んひゅ！？ ふあっ──クリトリス── / クリトリスも──ぐりぐり、されて──きもち、いい」 / Audit: 「Nhyu!? Phùa──âm vật── / âm vật cũng──được ngoáy ngoáy──sướng, quá」 / Sửa: 「Nhyu!? Fua──âm vật── / âm vật cũng──được ngoáy ngoáy──sướng, quá」
  - Lý do: giữ "Nhyu" của audit.
- **1377** — ぷぁっ→"Pua" (ぷ + ぁ = 2 âm a).
  - JP: 「ぷぁっ──あの…… / 清春……？ 自分……体が──」 / Cũ: 「Phù──ừm... / Kiyoharu...? Cơ thể... của em──」 / Audit: 「Phà──ừm... / Kiyoharu...? Cơ thể... của em──」 / Sửa: 「Pua──ừm... / Kiyoharu...? Cơ thể... của em──」
  - Lý do: ぷぁ = "Pua" (tiền lệ 凪ふかみh2 1405: ぷぁ→"Pua"; ふかみh3: ぷあぁ→"Puaa"). Audit xếp ぷぁ như ふぁ ("phà") — dạng khóa đó cũng gượng trong rên nên về romaji.
- **1381** — ふあっっ→"Fua ư ư".
  - JP: 「おんなんこっ！ ふあっっ！ きもちっ── / 感じるっ！ 感じてっ！ とろけちゃうっっ！！！！」 / Audit: 「Bé gái! Phùa ư ư! Sướng quá── / Cảm thấy rồi! Cảm thấy rồi! Tan chảy mất thôi!!!!」 / Sửa: 「Bé gái! Fua ư ư! Sướng quá── / Cảm thấy rồi! Cảm thấy rồi! Tan chảy mất thôi!!!!」
  - Lý do: giữ ư ư của audit cho っっ sau nguyên âm rên; とろけちゃうっっ giữ nguyên (っ gắn động từ nội dung).
- **1387** — ふあっ→"fua" (giữa dòng, viết thường).
  - JP: 「しゅごい、のっ！ ぜんぶっ──ふあっ！ あっ！ / なか、ねっ！ おんなのこっ ちつ、が──ちつない！」 / Audit: 「Tuyệt, quá! Tất cả──phùa! A! / Bên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」 / Sửa: 「Tuyệt, quá! Tất cả──fua! A! / Bên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」
- **1392** — ふ、あっ→"Fu, a" (audit bỏ sót).
  - JP: 「きもち、い──きもち、いい──ふ、あっ── / これ？ が、セックス？ こしゅ、こしゅ、セックス？」 / Cũ: 「Sướng, quá──sướng, quá──phù, a── / Cái này? Là, làm tình sao? Cọ, cọ thế này, là làm tình sao?」 / Sửa: 「Sướng, quá──sướng, quá──Fu, a── / Cái này? Là, làm tình sao? Cọ, cọ thế này, là làm tình sao?」
  - Lý do: như 1274.
- **1395** — ふぁっ→"Fa"; ん、くっ→"ưm, ku".
  - JP: 「シー……リン、グ──ふぁっ……ん、くっ──はっ── / それ──なにっ──んうっ」 / Cũ: 「Niêm... phong──phù... ưm, hự──hà── / cái đó──là gì──ưm」 / Audit: 「Niêm... phong──phà... ưm, hự──hà── / cái đó──là gì──ưm」 / Sửa: 「Niêm... phong──Fa... ưm, ku──hà── / cái đó──là gì──ưm」
  - Lý do: ふぁ→"Fa" (họ fa); ん、くっ tách dấu phẩy: ん→"ưm", くっ→"ku" — "hự" làm mất hẳn k (tiền lệ ハチロクh6 §3c: くっ trong thoại → "Ku"; chỉ SFX trong ngoặc mới giữ "hự"). Giữ "hà" cho はっ (1 a, đúng).
- **1438** — ふあっ→"fua"; ふああぁんっっ→"Fuaaan ư ư".
  - JP: 「うれし、うれしい──んっ──あっ── / ふあっ！？ ふああぁんっっ！！」 / Cũ: 「Vui, em vui lắm──ưm──a── / phù!? Phù aaaa!!」 / Audit: 「Vui, em vui lắm──ưm──a── / phùa!? Phù aaan ư ư!!」 / Sửa: 「Vui, em vui lắm──ưm──a── / fua!? Fuaaan ư ư!!」
  - Lý do: ふああぁん = ふ + あ×3 + ん → "Fuaaan" (3 a + n, đếm bằng máy); giữ ư ư của audit cho っっ.
- **1569** — ふっ──あっ→"Fu──a" (audit bỏ sót).
  - JP: 「くり、とりすも──ふっ──あっ──おっぱい、も── / それから、ちつ、も──さっき、までっ──んっ！」 / Cũ: 「Âm, vật cũng──phù──a──ngực, cũng── / rồi cả, âm đạo, nữa──lúc nãy, vẫn còn──ưm!」 / Sửa: 「Âm, vật cũng──Fu──a──ngực, cũng── / rồi cả, âm đạo, nữa──lúc nãy, vẫn còn──ưm!」
  - Lý do: như 1342 (cặp ふあ tách bởi ──).
- **1570** — ふあっ→"Fua".
  - JP: 「クリトリ、スっ──ふあっ──クリトリス、好きっ。 / ぺろぺろ、されるのっ──きもち、いいっ──んうっ」 / Audit: 「Âm, vật──phùa──âm vật, thích lắm. / Được liếm láp──sướng, lắm──ưm.」 / Sửa: 「Âm, vật──Fua──âm vật, thích lắm. / Được liếm láp──sướng, lắm──ưm.」

### 4B. Đếm nguyên âm — はぁっ/はあっ = 2 a (4 dòng)
Quy tắc: はぁっ/はあっ = は + ぁ/あ = 2 mora a → 2 a ("Hàà"/"hàà"). Tiền lệ: ハチロクh9 (はぁっ→"Haa", はあっ→"haa" ×3), lr-ハチロクh1 (audit 1174: はあっ→"Haa"), lr-日々姫真闇h1 (はぁっ/はあっ→"Hàa"/"hàa" nhiều dòng), 凪ふかみh2 moan 1294 (はぁ = 2 mora a). Lưu ý: audit file này ghi 1468 "đúng số lượng" với 1 a — xem Cờ F3.
- **1267** — はああっ = 3 a (audit bỏ sót đếm).
  - JP: 「ひゃうっ！ んっ！ はああっ──しゅごっ──うっ、 / しらな、かった──おっぱい──こん、なにっっ」 / Audit: 「Hyau! Ưm! Hà──tuyệt quá──ư, / không, ngờ──ngực──lại, thế này」 / Sửa: 「Hyau! Ưm! Hàaa──tuyệt quá──ư, / không, ngờ──ngực──lại, thế này」
  - Lý do: はああっ = は + あ + あ = 3 a; VN cũ chỉ 1 a. Giữ "Hyau" của audit. (Đối chiếu: audit tự đếm はあああんっ = 4 a ở 1278.)
- **1275** — はぁっ×3 + はあっ×1 = 2 a mỗi hơi; ん、くっ→"ưm, ku" (audit bỏ sót cả hai).
  - JP: 「はぁっ、はぁっ、はぁっ、はあっ──ん、くっ── / あっ──ごりって──ごりって、しゅる、とこで」 / Cũ: 「Hà, hà, hà, hà──ưm, hự── / a──chỗ cứng──cứ cọ vào, chỗ cứng đó」 / Sửa: 「Hàà, hàà, hàà, hàà──ưm, ku── / a──chỗ cứng──cứ cọ vào, chỗ cứng đó」
  - Lý do: mỗi はぁっ/はあっ = 2 a (thiếu 1 a mỗi hơi); ん、くっ như 1395 ("hự" mất k — tiền lệ ハチロクh6 §3c).
- **1468** — はぁっ×1 + はあっ×2 + はあ×1 = 2 a mỗi hơi.
  - JP: 「きよはる──きよはる…… / はぁっ、はあっ、はあっ──はあ──────んっ」 / Cũ: 「Kiyoharu──Kiyoharu... / Hà, hà, hà──hà──────ưm」 / Sửa: 「Kiyoharu──Kiyoharu... / Hàà, hàà, hàà──hàà──────ưm」
  - Lý do: như trên; giữ dấu ────── và "ưm" cho んっ.
- **1516** — はぁ×4 = 2 a mỗi hơi (không có っ).
  - JP: 「はぁ……はぁ……はぁ……はぁ──」 / TW: 「蛤啊……蛤啊……蛤啊……蛤啊——」 / Cũ: 「Hà... hà... hà... hà──」 / Sửa: 「Hàà... hàà... hàà... hàà──」
  - Lý do: はぁ = 2 mora a; TW mỗi hơi 2 âm tiết (蛤啊) ủng hộ đếm 2 a.

## 5. Giữ nguyên — các dòng rên đã đúng (đáng chú ý)
- **Audit romaji đã đúng (19 dòng, §3):** giữ nguyên toàn bộ giá trị audit (kể cả 1265 "Hyan ư ư" — romaji + Ư cho っっ sau nguyên âm rên, cùng mẫu 1334 "Kuuuuuun ư ư"; và 1258 "Áu" cho あうっ = 2 vần theo công thức).
- **Hơi thở ふっ/ふうっ → "phù"/"phùu":** giữ theo quy ước chung (hơi thở ふ đơn không thuộc họ fa) — 1297 "phùu" (2u, đúng), 1415 あっ、ふ→"a, phù", 1571 ふっ！→"phù!". Chỉ sửa ふあ/ふぁ/ぷあ và dạng tách của chúng, không đụng hơi thở ふ đơn.
- **Gasp đã thể hiện:** 1313 「っ」→"Ư" (VN cũ đã có); 1320 うんっ→"Vâng!!" (っ gắn từ nội dung, dấu !! truyền nhấn mạnh); 1368 っ──チュッ→"Ư──chụt"; 1420 ──っ──→"──ư──"; 1425 っ──→"Ư──"; 1547 ならっ/してっ/射精っ/にっ (っ gắn từ nội dung, không thêm Ư).
- **Âm mũi ん:** 1338 ん……→"Ưm...", 1354 んあっ→"Ưm a", 1357 んむっ→"Ưm", 1361/1366 んっ→"Ưm", 1439 ん……→"ưm...", 1547 んうっ→"ưm" — đúng.
- **Hôn/liếm SFX — chỉ mất độ dài (giữ nguyên theo quy ước SFX của audit: độ dài diễn tự do, chỉ sửa khi mất âm tiết hoặc sai họ âm):** 1316/1329/1331/1353/1368 (ちゅっ→"chụt", れるっ→"liếm", ずじゅうっ→"rột"); 2019–2072 các dòng SFX trong ngoặc (2025, 2027, 2028, 2031, 2034–2045, 2048, 2051–2053, 2058–2066, 2072).
- **SFX trong ngoặc （） ở độc thoại — giữ nguyên dạng động từ/từ láy Việt:** 2019–2072 (trừ 3 dòng audit đã sửa 2047/2050/2069); kể cả （くっ）→（Ưm）/(hự) trong ngoặc — ranh giới romaji-vs-động-từ cho SFX ngoặc vẫn là câu hỏi mở (tiền lệ ハチロクh6 F3).
- **Tiếng cười:** 1337 えへへっ→"e he he"; 1772 ふふっ→"Bật cười khúc khích" (tiếng cười, không phải gasp).
- **Rên đã diễn đủ âm:** 1249 はっ→"hà", あっ→"a", んうっ→"ưm"; 1274 は……ぁっ→"Hà... a" (2 a tách bởi ……); 1296 わ→"Oa."; 1301 はっ→"Hà"; 1309 ぁあ……→"A..."; 1534 は……ぅっ→"hà... ư" (は + ぅ = 2 âm); 1473 あっ→"a"; 1571 あっ→"A".
- **Từ cảm giác (không phải rên):** 1242 きゅんきゅん→"râm ran", 1478 きゅん、きゅん→"rộn ràng, rộn ràng", 1693 きゅん→"run lên" (diễn nghĩa, giữ); 1572 もっとぉっ→"nữa đi" (từ nội dung, giữ).
- **Nuốt/thở trong độc thoại:** 965 （ごくりっ）→"(Nuốt nước bọt)", 1746 こくり→"nuốt nước bọt cái ực", 1816 ほおっと→"thở hắt", 1946 ゴクリ→"nuốt nước bọt cái ực" — giữ.

## 6. Sweep gasp — đã kiểm tra trực tiếp 7/7 mục
- File này có **7 mục** trong `sweep-raw-gasp-wrong.json`: 1318, 1323, 1324, 1325, 1474 (lost-gasp, audit áp nguyên văn), 1580 (lost-gasp-trailing, audit áp có sửa số ~ 25→15), 1365 (already-rendered — audit GHI ĐÈ, xem dưới).
- 1365: sweep xếp "already-rendered" là SAI — các "Ưm" trong VN diễn んむっ/むっ, còn っっ đầu dòng không có diễn nào; audit đã sửa thành "ƯƯ!!? Ưm! Ưm──ưm──!?" — **giữ nguyên, không đụng** (quy tắc khóa gasp Ư).
- Không đụng dòng gasp Ư nào. Không có dòng "Kh" nào bị đổi. 2 gasp sweep bỏ sót (1319, 1360) đã được audit tìm thêm và sửa — giữ nguyên.

## 7. Cờ cho đợt thống nhất (không tự quyết)
- **F1 — Đại từ Niiroku (mang từ audit, quyết định 22/11 ~03:32 đã có):** file này Niiroku tự xưng "em" 15 dòng / "Tôi" 0 dòng (1211, 1215, 1293, 1322, 1339, 1377, 1402, 1438, 1439, 1457, 1508, 1534, 1545, 1547, 1549) — phân bố NGƯỢC với Niiroku 01/02 (cơ sở quyết định thống nhất thành "Tôi"). Các giá trị moan ở đây (1293, 1377, 1547...) GIỮ NGUYÊN "em" — đợt thống nhất đổi "em"→"Tôi" cùng các dòng còn lại nếu quyết định giữ nguyên. "Anh" cho Akai (1258/1333/1508/1519) đi với "Tôi" vẫn là cặp xưng hô chuẩn nên không mâu thuẫn. 1439 "cơ thể, của mình" cũng chờ đợt thống nhất.
- **F2 — Dạng tách fa "Fu, a" vs ハチロクh7:** file này đổi 6 dòng tách (1274, 1297, 1339, 1342, 1392, 1569) sang romaji "Fu, a"/"Fu──a" (theo ハチロクh9, lr-ポーレットh1, 凪ふかみh2 1300), NHƯNG ハチロクh7 giữ "phù——a"/"phù, a" (11 dòng, theo tiền lệ audit trong file đó) — cần quyết MỘT dạng duy nhất toàn dự án ở đợt thống nhất (cờ F3 của 凪ふかみh2).
- **F3 — はぁっ/はあっ = 1 a hay 2 a:** audit file này ghi 1468 "đúng số lượng" với "Hà" (1 a) — bản moan sửa thành 2 a theo tiền lệ h9/lr-h1/lr-hibikifukami-h1/凪ふかみh2 (1271, 1275, 1292, 1468, 1516 + 1267 はああっ→3 a). NHƯNG lr-ふかみh1 và lr-ふかみh2 giữ "Ha" theo quy ước thở riêng của từng file (audit §5/§6 của các file đó). Dự án vẫn có hai quy ước — đợt thống nhất cần chốt MỘT dạng. Parent kiểm chứng lại các dòng §4B khi merge.
- **F4 — ん、くっ → "ưm, ku" vs "ưm, hự":** 1275 và 1395 đổi sang "ưm, ku" (theo ハチロクh6 §3c: くっ trong thoại → "Ku", "hự" mất k). Audit file này giữ "ưm, hự" (không nêu lý do). Ranh giới: SFX trong ngoặc （くっ） vẫn giữ "Ư"/"hự" (2050, 2069) — theo đúng ranh giới F3 của ハチロクh6.
- **F5 — ふ、ゅっ → "Fu, yu" (1356):** audit giữ "Phù, ư" với lý do "tách theo dấu phẩy JP" — bản moan đổi sang romaji theo cùng logic dạng tách fa ("phù" sai vần cho ふ ngắn; "ư" mất y của ゅ; tiền lệ 凪h2: ゅっ→"Yu"). Parent kiểm chứng lại khi merge.
- **F6 — 31 dòng thay thế giá trị audit cùng key:** danh sách chồng chéo: 1267, 1271, 1272, 1274, 1276, 1277, 1278, 1280, 1281, 1282, 1285, 1288, 1290, 1291, 1292, 1293, 1294, 1297, 1300, 1322, 1336, 1337, 1353, 1356, 1358, 1377, 1381, 1387, 1395, 1438, 1570. Áp MỘT giá trị moan cho mỗi key ở đợt build; parent kiểm chứng lại khi merge.

## 8. Lượt soát 2
- Đã đọc lại toàn bộ 38 fix đối chiếu từng JP: **38/38 tái kiểm chứng, 0 bỏ, 0 sửa**.
- Đếm nguyên âm kiểm chứng lại bằng máy: 1277 12a, 1292 5a, 1438 3a (Fuaaan), 1271 4×2a, 1275 4×2a, 1292 2a, 1468 4×2a, 1516 4×2a, 1267 3a; đếm của audit đã giữ: 1278 4a/4a, 1280 2a, 1334 6u, 1336 3u+2n, 1351 17u, 1363 17u.
- Cơ sở tổng: đã tự kiểm chứng ROUTE-MOANS.md — lúc bắt đầu 49 file / 1247 dòng sai (moan) (khớp với cơ sở được giao); trong lúc làm file này, parent đã gộp lr_日々姫h1 (0 dòng, 22/11 ~04:40) nên tổng hiện tại là **50 file / 1247 dòng** — snippet đã REBASE theo tổng hiện tại (50/1247 + 38 = 51/1285).

## 9. Khối TOML (đã parse-kiểm chứng — 38 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
"1267" = "「Hyau! Ưm! Hàaa──tuyệt quá──ư,\\nkhông, ngờ──ngực──lại, thế này」"
"1271" = "「Fua──hà──a──a──ư ư, ưm──\\nhàà──hàà──hàà──hàà──」"
"1272" = "「Fua──a──a ư ư ư──aaa──」"
"1274" = "「Hà... a──ưm──cái này... Fu, a──\\nsướng quá──ưm... Nku──a... ưm──」"
"1275" = "「Hàà, hàà, hàà, hàà──ưm, ku──\\na──chỗ cứng──cứ cọ vào, chỗ cứng đó」"
"1276" = "「Fua.」"
"1277" = "「Fuaaaaaaaaaaaa!!!!!!!!」"
"1278" = "「Hà aaan! Fua! A! Sâu, bên trong!\\nFua! A! A! Aaaa!!!!!」"
"1280" = "「Fua! A! A! A!!\\nA! A! A! Aa!!!」"
"1281" = "「Fua! A! A! A!\\nA! A! A! A!!!」"
"1282" = "「Fukyu! Ưm──Fua! Chớp chớp, chớp chớp!!\\nAaa! Ư! Mạch điện, cứ như, sắp chập, mất」"
"1285" = "「Fua! Sướng quá──tan chảy mất! Tan chảy mất thôi,\\nbé gái──đang, tan chảy──nhũn ra, mất thôi!」"
"1288" = "「Fua!? A──aa──ha ư──ưm.\\nTrực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」"
"1290" = "「Fua!? A──âm đạo──nè, bé gái──\\nlúc nãy, vẫn còn──đau đớn──khó chịu, thế mà」"
"1291" = "「Fua!?──A──!」"
"1292" = "「Hàà!? Ư──a──Fuaaaaa ư ư ư」"
"1293" = "「Fua!? Ngón tay──Kiyoharu──ngón tay, của Kiyoharu──\\nngực──ưm──ngực──đang sờ ngực, của em」"
"1294" = "「Fua!? Chỗ đó──chỗ đó, đùa sao!?\\nChỗ như thế──mà tách ra, được──sao?」"
"1297" = "「Hà──a──phùu, ưm──lưỡi──liếm liếm,\\nFu, a──chỗ này cũng──rất──sướng, ạ.」"
"1300" = "「Hà──ưm──ư──Fua──ch-chim,\\nưm, chỗ cứng──chỗ cứng──chỗ đó」"
"1322" = "「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\\nthế này──là đang làm cho em, sướng──fua.」"
"1336" = "「Ưm──Kyuuunn────ưm──Pua!\\nA! A! A! Aaa!!!!!」"
"1337" = "「Ưm.................. pua──e he he──\\nKiyoharu──Kiyoharuu」"
"1339" = "「Vâng... Fu, a──em làm được. Cỡ đó thì, tất nhiên rồi.」"
"1342" = "「Ưm... này? Ái ân vuốt ve──ưm... chữ ái, trong ái ân vuốt ve──\\nFu──a──chữ ái──đó──là──chữ ái trong tình ái, yêu đương sao?」"
"1353" = "「Ưm!? Ưm... chụt——chụt——pua,\\nưm——chụt——chụt——liếm——rột」"
"1356" = "「Nkyu! Ưm! Fu, yu──Myu──\\nưmmmmmm──!!」"
"1358" = "「Nhyu!? Fua──âm vật──\\nâm vật cũng──được ngoáy ngoáy──sướng, quá」"
"1377" = "「Pua──ừm...\\nKiyoharu...? Cơ thể... của em──」"
"1381" = "「Bé gái! Fua ư ư! Sướng quá──\\nCảm thấy rồi! Cảm thấy rồi! Tan chảy mất thôi!!!!」"
"1387" = "「Tuyệt, quá! Tất cả──fua! A!\\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」"
"1392" = "「Sướng, quá──sướng, quá──Fu, a──\\nCái này? Là, làm tình sao? Cọ, cọ thế này, là làm tình sao?」"
"1395" = "「Niêm... phong──Fa... ưm, ku──hà──\\ncái đó──là gì──ưm」"
"1438" = "「Vui, em vui lắm──ưm──a──\\nfua!? Fuaaan ư ư!!」"
"1468" = "「Kiyoharu──Kiyoharu...\\nHàà, hàà, hàà──hàà──────ưm」"
"1516" = "「Hàà... hàà... hàà... hàà──」"
"1569" = "「Âm, vật cũng──Fu──a──ngực, cũng──\\nrồi cả, âm đạo, nữa──lúc nãy, vẫn còn──ưm!」"
"1570" = "「Âm, vật──Fua──âm vật, thích lắm.\\nĐược liếm láp──sướng, lắm──ưm.」"
```

## Kết bài

File lr_ニイロクh_誓い。約束.txt.toml: 320 dòng đã đọc kỹ từng dòng đối chiếu JP + TW, 126 dòng rên/SFX đã xét, đổi 38 dòng (34 romaji + 4 đếm nguyên âm) — 31 dòng xây trên giá trị audit cùng key (chỉ đổi đúng token rên), 7 dòng audit bỏ sót. Không lệch dòng, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Sweep gasp kiểm tra trực tiếp 7/7 mục (5 áp nguyên văn, 1 áp có sửa số ~, 1 ghi đè) + 2 gasp sweep bỏ sót đã được audit sửa — không đụng dòng gasp Ư nào, không đổi dòng "Kh" nào (file không có). 6 cờ cho đợt thống nhất (đại từ Niiroku "em"×15 → "Tôi"; dạng tách fa "Fu, a" vs ハチロクh7; はぁっ/はあっ 1a hay 2a; ん、くっ "ưm, ku" vs "ưm, hự"; ふ、ゅっ "Fu, yu"; 31 dòng thay thế giá trị audit). Đã soát lại toàn bộ 38 fix lần 2 (38/38/0/0).
