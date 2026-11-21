# Kiểm tra bản dịch — グランドリライト09_凪.txt.toml (route 07_Nagi_Fukami)

## Thông tin file

- **File:** `グランドリライト09_凪.txt.toml` — route 07_Nagi_Fukami (Grand Rewrite 09 — Nagi).
- **Đường dẫn TOML:** `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/07_Nagi_Fukami/#U30b0#U30e9#U30f3#U30c9#U30ea#U30e9#U30a4#U30c809_#U51ea.txt.toml`
- **md5 TOML:** `5843270ec2d53178900f0790059b96c7` — bản sao trong `09_Grand/` có cùng md5 (2 bản, giống hệt nhau). UTF-8 BOM + CRLF.
- **CSV3 master:** `~/workspace/maitetsu-pilot/sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv` — 484 dòng cho file này, 1 set duy nhất, khóa duy nhất, 0 VN trống.
- **Kiểm tra phẳng:** VN khớp phẳng TOML 484/484 (0 sai lệch). TOML # JP: khớp CSV3 JP 484/484 (0 sai lệch).
- **Nhân vật (số dòng):** monologue 217, 双鉄 124, 凪 57, 路子 23, ハチロク 18, 中村 15, 日々姫 13, みくろ 12, オリヴィ 5.
- **Nội dung:** Soutetsu kể lại quá trình thử nghiệm tàu khách Nine Stars (toa tắm, bồn tắm, Kuma 1/Kuma 2, D51), xen kẽ các cảnh với Nagi, Michiko, Nakamura; đoạn cuối là giấc mơ/trở lại ga. Không có H-scene.
- **`[characters]`:** 2163=Mikuro, 2180=Olive, 2195=Hachiroku, 2258=Nakamura, 2351=Nagi, 2433=Soutetsu, 2622=Hibiki, 2818=Michiko — đúng. **`[character_subs]`** đúng. **`[selections]`** rỗng.

## Kết quả tổng

- **Đã đọc: 484/484 dòng. Sai: 129 (26,7%).**
- **Phân loại (129):** lệch dòng 118; gasp っ 5 (1629, 1630, 1633, 2404, 2492); dịch sai 5 (1626, 1651, 2025, 2703, 2930); thuật ngữ 1 (2428, "tuyến Yui"→"tuyến Yunoi").
- **Lệch vị trí 0, nhiễm chéo 0, chưa dịch 0, trùng khóa 0. Chuỗi xoay 2 (chu trình 2 phần tử). Mồ côi 0 dòng JP — nhưng có 12 VN mồ côi trong file.**
- **Chi tiết các số 0:** lệch vị trí (không có dòng nào lệch 1 vị trí đơn lẻ — toàn bộ lệch dòng đều nằm trong các chuỗi xoay dài, xem § Chuỗi lệch dòng); chuỗi xoay: 2 chu trình 2 phần tử (1483↔1774, 2044↔2830) — VN của nhau hoán đổi cho nhau; không có chu trình dài hơn; nhiễm chéo (không có VN nào thuộc file khác được xác minh — các VN mồ côi trong file chỉ ghi nhận là mồ côi, chưa xác định được nguồn chéo); mồ côi 0 dòng JP (mọi dòng JP đều có VN, chỉ là sai) — nhưng có 12 VN mồ côi trong file, xem § Chuỗi lệch dòng; chưa dịch 0 (0 VN trống; không có dòng nào còn tiếng Trung/tiếng Nhật nguyên vẹn trừ 2 ký tự っ ở 2404/2492, đã sửa); trùng khóa 0 (484 khóa duy nhất).
- **Nhóm VN trùng lặp (hợp lệ, không tính sai):** 「Vâng!」1636/1695; 「A――」1653/1654/1692 (1692 sai vì lệch dòng, 2 dòng còn lại đúng); 「Đúng vậy.」1827/1865; 「Vậy sao.」1986/1990.
- **Tag `%l`:** 0 lỗi tag độc lập với lệch dòng (mọi sai lệch số lượng tag đều là hệ quả của lệch dòng). Tag ruby `[x,N]` phía JP được VN bỏ đúng (1030, 1535 — xem § Lưu ý).
- **Đại từ:** Soutetsu "anh" với Nagi/Michiko đúng toàn file; "tôi" trong độc thoại và ngữ cảnh trang trọng đúng. Nagi→Fukami: không có lỗi "chị"/"em" trong file này (không có thoại của Fukami).

## Đối chiếu sweep (gasp っ)

Sweep `sweep-raw-gasp-wrong.json` có **5 mục** cho file này — nhận **5/5**:
- 1629 (lost-gasp-trailing): áp nguyên fix 「Ư!" — đúng.
- 1633 (lost-gasp-whole): áp nguyên fix 「Ư!?" — đúng.
- 2404 (raw-tsu): áp nguyên fix — đúng (VN cũ còn ký tự っ).
- 2492 (raw-tsu): áp nguyên fix — đúng (VN cũ còn ký tự っ).
- 1630 (needs-file-audit, sweep không đưa fix): đã sửa trong audit này thành 「Ư!".

Quét máy toàn bộ dòng JP chứa っ: **183 dòng** có っ; chỉ **9 dòng** ở vị trí gasp (1621, 1629, 1630, 1633, 1636, 1637, 2004, 2404, 2492). Trong đó 1636 (うんっ→"Vâng!") và 2004 (にーさんっ→"Anh hai!") giữ nguyên — tiếng cảm thán bị ngắt được thể hiện bằng "!" nên không mất âm. 1621 và 1637 được sửa qua lệch dòng (fix của chúng không phải gasp). **Không còn gasp nào sót.**

## Chuỗi lệch dòng

VN bị xoay trong các chuỗi dài (ký hiệu: VN@Y là bản dịch của JP@X; fix[X] lấy từ VN@Y). 2 chu trình 2 phần tử: **1483↔1774** và **2044↔2830** (VN của nhau hoán đổi cho nhau).

- **A (11):** 1125→2643→1984→1437→1455→1435→2300→1516→1621→2721→2929→(ngoài file — câu hứa "Tôi hứa đấy, tôi sẽ sống…")
- **B (10):** 1650→2481→1737→2831→2306→2017→1724→1780→1116→2045→(ngoài file — "Hơn nữa có lẽ, còn sớm hơn tôi rất nhiều.")
- **C (6):** 1696→1446→2021→2642→2520→1422→(mất — VN hiện tại của 1422 chỉ còn "!")
- **D (15 + chu trình 2):** 2663→2265→2571→2225→2854→1902→2825→1941→1694→1667→2618→1870→2282→1483↔1774
- **D2 (2):** 1812→2558→(ngoài file — "Anh hai! Anh hai!!")
- **E (15 + chu trình 2):** 1927→2251→2564→1789→1637→2800→1943→1920→1523→2267→1708→2598→1432→2044↔2830
- **F (12, kết ở dòng đúng):** 2374→2937→2042→1787→2525→2620→1987→2329→2763→1770→1862→1999→2613 (đúng — VN@1999 là bản sao của VN đúng của 2613)
- **G (15):** 1921→1578→2478→2590→2584→2828→1755→1841→1496→2765→1843→2269→1988→1749→1133→(ngoài file — câu chúc ngủ ngon "Ngủ ngon nhé, Fukami.")
- **H (5):** 2019→1618→2851→2286→2270→(ngoài file — "――Ừ.")
- **I (5):** 1989→1613→1909→2862→1800→(ngoài file — "Ừm!?")
- **J (8):** 1991→1535→2505→2802→2836→1030→1835→2718→(ngoài file — câu chúc ngủ ngon "Ngủ ngon nhé, Soutetsu.")
- **K (4):** 2878→2694→1123→1692 (VN@1123 là bản dịch lệch/garbled một phần của JP 1692)
- **L (9):** 1504→2262→2221→2852→1511→1423→1713→2288→1792→(ngoài file — "Ra là vậy~")

**VN mồ côi trong file (12)** — không có JP tương ứng trong file này, nguồn chéo chưa xác định (đã tìm trong CSV3, không khớp chính xác dòng JP nào): 1133 (câu chúc ngủ ngon Fukami), 1630 ("Vậy sao!"), 1651 ("A, này."), 1745 (câu cảm ơn), 1792 ("Ra là vậy~"), 1800 ("Ừm!?"), 2045 ("Hơn nữa..."), 2270 ("――Ừ."), 2558 ("Anh hai! Anh hai!!"), 2718 (câu chúc ngủ ngon Soutetsu), 2929 (câu hứa), 1422 (chỉ còn "!" — nội dung mất hoàn toàn).

**Gasp (5, không thuộc chuỗi):** 1629, 1630, 1633, 2404, 2492. **Đơn lẻ (7):** 1626, 1651 (cảm thán dịch sai), 2025, 2703, 2930 (dịch sai), 2428 (thuật ngữ), 1745 (fix viết mới, VN mồ côi).

## Lưu ý / điểm tự quyết / cần Hieu

- **1128 — KHÔNG SỬA, chờ Hieu:** Soutetsu xưng "anh" — người nghe chưa rõ (Michiko hay Nakamura; các dòng kề: 1116 Michiko, 1117 Nakamura, 1123 nhắc Nakamura). Giữ nguyên VN cũ, **không tính sai**. Cần Hieu xác định người nghe.
- **2663 — JP bị cắt cụt, chờ Hieu:** JP "今日も今日とて、みくろはD51 1031を――" kết bằng を――, không có động từ. Fix giữ nguyên dạng cụt ("…Mikuro với D51 1031――"), KHÔNG bịa phần hoàn thiện. TW gợi ý 整備 (bảo dưỡng) — nếu Hieu xác nhận thì bổ sung ở đợt thống nhất.
- **1787/1789 — điểm tự quyết (đại từ):** đây là lời thoại với Nagi (trong 「」) nên Soutetsu xưng "anh"; VN lệch dòng ở 2042/2564 dùng "Mình" là sai ngữ cảnh (đó là độc thoại). Đã sửa thành "anh" theo quy tắc Soutetsu "anh" với Nagi.
- **1535 — bỏ tag %l của ドカ停:** JP (CSV3 + TOML # JP:) không có tag này (chỉ TW có). Theo quy tắc không bịa tag %l phía VN nên fix dùng "đỗ tàu lâu" không tag.
- **1030 — bỏ ruby [フランク銀行,1]:** nhất quán với thực hành toàn dự án (bỏ tag ruby `[x,N]` phía JP).
- **2329 — tag %l phía JP bị lỗi:** JP có `\x%l台車;#;#00ffc040;台車%l;#;` (thừa `;#;`) — lỗi phía JP, không phải lỗi VN, nên fix giữ nguyên dạng tag như VN gốc.
- **1985 — 十川 = "Sogou" ĐÚNG, giữ nguyên:** theo ruby そごう; tiền lệ trong audit Grand02 Navi. Không tính sai.
- **1780/2288 — "Ohimitera"→"Ohitoyo":** VN lệch dòng được lấy về chứa "Ohimitera" (dạng cũ); đã sửa thành "Ohitoyo" (thuật ngữ đã quyết) ngay trong fix, không chờ đợt thống nhất.
- **2428 — "tuyến Yui"→"tuyến Yunoi":** thuật ngữ đã quyết (湯医線 = Yunoi); đây là 1 dòng nữa ngoài danh sách thống nhất đã biết.
- **[characters] 2180 = "Olive" vs "Olivy":** `[characters]` và `[character_subs]` trong file dùng "Olive" trong khi chính tả dự án là "Olivy" — **chờ Hieu quyết** (đã nằm trong danh sách chờ từ H15b), không sửa trong audit này.
- **2851/2853 — sửa ở lượt soát 2:** 2851 bị sót ở lượt đọc 1 (VN của nó là bản dịch của JP 2286); 2853 ban đầu bị gắn cờ nhầm nhưng kiểm tra lại thì VN cũ đúng (dịch đúng JP của chính nó) nên đã loại khỏi danh sách sai.
- **1999/2613:** VN@1999 là bản sao y hệt VN đúng của 2613; 2613 tự nó đúng nên không cần sửa. 1999 sửa bằng cách lấy VN từ 1862.
- **Không có H-scene** trong file này nên quy tắc romaji cho họ ひゃ/ひゅ/ひあ/きゃ không áp dụng; tiếng cười ふふっ ở 1601 ("Fufu") giữ nguyên đúng.

## Giữ nguyên có lý do

- **1128:** "anh" — người nghe chưa rõ, giữ nguyên, chờ Hieu (xem § Lưu ý).
- **1985:** 十川 → "Sogou" theo ruby — đúng.
- **1636:** うんっ → "Vâng!" — tiếng cảm thán bị ngắt, "!" thể hiện đủ, không cần "Ư".
- **2004:** にーさんっ → "Anh hai!" — tương tự, giữ nguyên.
- **1590:** "anh" cho bộ ba Nagi/Hibiki/Nakamura — đúng ngữ cảnh.
- **1691:** "em ấy" — đúng.
- **1960:** "Cảm ơn rất nhiều" — đúng.
- **1073:** "Nghe em ấy nói" — đúng.
- **2450:** ボボボボ → "Bô bô bô bô" — đúng.
- **1601:** ふふっ → "Fufu" — tiếng cười, đúng.

## Chi tiết từng dòng sai

### Key 1030 — monologue — lệch dòng

JP: ――本当に、災い転じて福となった。\\nマイアさんの紹介してくれた[フランク銀行,1]佛銀の担当者は、優秀だった。

TW: ——真是轉禍為福了。邁雅阿姨介紹的法國銀行負責人非常優秀。

VN cũ: 「Vậy sao?」

Sửa: ――Đúng là trong cái rủi có cái may.\\nNgười phụ trách của ngân hàng Pháp do bác Maia giới thiệu rất xuất sắc.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1835 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1835.

### Key 1116 — 路子 — lệch dòng

JP: 「わざわい？」

TW: 「“禍”是什麼意思？」

VN cũ: 「Sắp rồi đúng không! Michi, biết mà!\\nBố và mẹ, đang đến gần Michi rồi!」

Sửa: 「Cái rủi?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2045 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2045.

### Key 1123 — 双鉄 — lệch dòng

JP: 「……ああ、中村さんはここであったか」

TW: 「……哦，中村小姐在這裡啊」

VN cũ: 「Sắp được gặp lại bố và mẹ rồi. Sao――」

Sửa: 「……A, cô Nakamura ở đây sao.」

Lý do: Lệch dòng: VN hiện tại ("Sắp được gặp lại bố và mẹ rồi. Sao――") là bản dịch lệch/garbled một phần của JP key 1692 ("父さんと母さんと、もうすぐ会える。か――" — "Sao――" dịch sai か――). Fix viết mới.

### Key 1125 — 双鉄 — lệch dòng

JP: 「――ああ」

TW: 「……噢」

VN cũ: Tương lai――A.\\nĐúng rồi, chắc chắn cũng có một tương lai đang chờ đợi Michiko.

Sửa: 「――À.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2643 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2643.

### Key 1133 — 双鉄 — lệch dòng

JP: 「――そうなのか」

TW: 「……這樣啊」

VN cũ: 「Chúc ngủ ngon. Fukami. Chúc em có những giấc mơ đẹp.」

Sửa: 「――Vậy sao.」

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file); fix viết mới từ JP + TW.

### Key 1422 — 双鉄 — lệch dòng

JP: 「乗れるとも。路子が望む、どんな列車にだって、必ず。\\nそうするために――僕は、ずうっと頑張っているんだ」

TW: 「一定可以。只要是你的願望，不管什麼樣的列車，我都會讓它實現。為了這個目標——我一直在努力」

VN cũ: 「!」

Sửa: 「Chắc chắn sẽ được lên. Bất cứ đoàn tàu nào Michiko muốn, chắc chắn.\\nĐể làm được điều đó――anh, vẫn luôn cố gắng mà.」

Lý do: Lệch dòng: VN hiện tại chỉ còn "!" — nội dung bị mất hoàn toàn. Fix lấy từ VN key 2520 (bản dịch đúng của JP này).

### Key 1423 — 双鉄 — lệch dòng

JP: 「乗れる」

TW: 「一定能」

VN cũ: 「Nếu được như vậy, thì đối với chúng ta cũng là một điều đáng mừng.」

Sửa: 「Sẽ được lên mà.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1713 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1713.

### Key 1432 — 双鉄 — lệch dòng

JP: 「ふかみが、ポーレットが、皆が、それぞれ。\\nできる全てを尽くしてくれたゆえ、越えられたのだ」

TW: 「不僅是深美和波萊特，所有人全都盡了自己最大的努力，所以我們才能跨越難關」

VN cũ: 「Sắp rồi……sao.\\nCũng không thể bắt đầu chạy nhanh đến mức gọi là sắp được đâu, nhưng mà.」

Sửa: 「Fukami, Paulette, và tất cả mọi người.\\nMỗi người đều đã làm tất cả những gì có thể, nên mới vượt qua được.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2044 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2044.

### Key 1435 — 路子 — lệch dòng

JP: 「えー」

TW: 「不是吧……」

VN cũ: Nhưng, cũng có vô số những “sự kết hợp công nghệ đã trưởng thành”\\nmà cho đến nay chưa từng có ai thử nghiệm.

Sửa: 「Ể~」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2300 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2300.

### Key 1437 — 双鉄 — lệch dòng

JP: 「いいや、そうでもない。クマ一・クマ二は、\\n本当に良く、試験に耐えてくれたからな」

TW: 「不，也不是完全取消。多虧隈一、隈二努力把測試堅持下來了啊」

VN cũ: 「Cũng có đề xuất sử dụng nước lò hơi hay nước trong bồn chứa làm "Nước tắm đầu máy hơi nước",\\nnhưng không phải đoạn đường nào cũng do đầu máy hơi nước kéo.」

Sửa: 「Không, cũng không hẳn đâu. Kuma 1 và Kuma 2,\\nthực sự đã chịu đựng các cuộc thử nghiệm rất tốt mà.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1455 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1455.

### Key 1446 — 双鉄 — lệch dòng

JP: 「中村さん。少しいいかな」

TW: 「中村小姐，能跟你聊兩句嗎」

VN cũ: 「Chị Suzuki, nhờ chị trông coi một lúc nhé.」

Sửa: 「Cô Nakamura. Nói chuyện một chút được không.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2021 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2021.

### Key 1455 — 双鉄 — lệch dòng

JP: 「"蒸機の湯"として、ボイラ水や水タンク内の水をという\\n案も出たが、全区間を蒸機牽引というわけでもない」

TW: 「也有人提議改為“蒸汽機車之浴”，使用鍋爐水或者水櫃裡的水，但是也不可能每段都用蒸汽機車牽引」

VN cũ: 「Ể~」

Sửa: 「Cũng có đề xuất sử dụng nước lò hơi hay nước trong bồn chứa làm "Nước tắm đầu máy hơi nước",\\nnhưng không phải đoạn đường nào cũng do đầu máy hơi nước kéo.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1435 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1435.

### Key 1483 — 双鉄 — lệch dòng

JP: 「しかし、大きく厳しかった山を越えたことは確かだ。\\n災いが、転じて福となったゆえ」

TW: 「但是我們確實跨越了難關，轉禍為福了」

VN cũ: 「Sao thế Michiko. Sao lại hốt hoảng vậy.」

Sửa: 「Tuy nhiên, đúng là chúng ta đã vượt qua được một ngọn núi lớn và hiểm trở.\\nBởi vì trong cái rủi, lại có cái may.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1774 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1774.

### Key 1496 — 路子 — lệch dòng

JP: 「だけど、れっ車のおふろ。\\nせっかくしけんしたのに、もったいないねぇ」

TW: 「但是，好不容易做了列車浴室的實驗，取消掉就太可惜了吧」

VN cũ: Ít nhất cũng phải 9 lần. Tức là mỗi ngày cần bổ sung gần 3 tấn nước,\\nvà bắt buộc phải có một bồn chứa để chứa số nước đó.

Sửa: 「Nhưng mà, bồn tắm trên tàu.\\nCất công thử nghiệm rồi mà, tiếc quá nhỉ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2765 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2765.

### Key 1504 — 双鉄 — lệch dòng

JP: 「ふたりとも揃っているなら、話が早い。\\nできれば、みくろにも」

TW: 「你們兩個都在啊，那談起來就方便多了。能不能把美玖路也叫過來」

VN cũ: Cô gái Kendo mạnh nhất Kyushu, thuộc hàng top toàn quốc,\\nngười gần như luôn đánh bại Nagi thời còn đi học――

Sửa: 「Cả hai đều ở đây rồi thì nói chuyện sẽ nhanh thôi. Nếu được thì gọi cả Mikuro đến nữa.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2262 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 1511 — 双鉄 — lệch dòng

JP: 「――楽しみにしていろ。路子。\\n僕が必ず。走らせてやるし、乗せてやる」

TW: 「你就期待著那一天吧，路子。我一定會實現它，讓你坐上那樣的列車」

VN cũ: 「Sẽ được lên mà.」

Sửa: 「――Hãy mong chờ nhé. Michiko.\\nAnh chắc chắn. Sẽ cho nó lăn bánh, và cho em lên tàu.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1423 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1423.

### Key 1516 — 双鉄 — lệch dòng

JP: 「クマ一号試験客車と、クマ二号試験客車か」

TW: 「你說隈元一號、二號測試客車啊」

VN cũ: 「Ể!?」

Sửa: 「Toa hành khách thử nghiệm Kuma số 1, và Toa hành khách thử nghiệm Kuma số 2 sao.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1621 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1621.

### Key 1523 — 路子 — lệch dòng

JP: 「にゅうよくていしゃ！　おもしろそー！！」

TW: 「停車入浴！感覺好好玩！！」

VN cũ: 9 phòng x 6 người, tối đa 54 hành khách.\\nKhông thể bắt tất cả họ dùng chung một bồn nước được.

Sửa: 「Dừng đỗ để tắm rửa! Nghe thú vị quá!!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2267 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2267.

### Key 1535 — 双鉄 — lệch dòng

JP: 「実質、食事・観光の時間も含めてのドカ停だがな。凪の\\n『お風呂停車すればよかと！』の声が、決め手となった」

TW: 「其實把進餐、觀光的時間也包含進去了，也就是說會\\x%lドカ停;#00ffc040;長時間停車%l;#;。這都是多虧凪當時說了句“停車洗澡就行唄！”」

VN cũ: Nếu coi như bồn tắm gia đình, và chỉ cần 9 lượt tắm là xong,\\nthì sẽ cần một bồn tắm lớn hơn để nhiều người có thể ngâm mình cùng lúc.

Sửa: 「Thực chất, đó là đỗ tàu lâu bao gồm cả thời gian ăn uống và tham quan. Câu nói của Nagi\\n『Chỉ cần dừng tàu để tắm là được mà!』 đã trở thành yếu tố quyết định.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2505. Fix lấy từ VN key 1991 nhưng BỎ tag %l của ドカ停: JP (CSV3 + TOML # JP:) không có tag này (chỉ TW có) — theo quy tắc không bịa tag %l phía VN.

### Key 1578 — 中村 — lệch dòng

JP: 「右田\\x%l機関士;#00ffc040;機関士%l;#;。おはようございます」

TW: 「右田\\x%l機関士;#00ffc040;司機%l;#;，早安」

VN cũ: Cô ấy đang lau chùi 8620 bằng dầu.\\nCẩn thận, tỉ mỉ――chỉ một mực cẩn thận và tỉ mỉ.

Sửa: 「\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Chào buổi sáng.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2478 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2478.

### Key 1613 — 路子 — lệch dòng

JP: 「わ！　れっ車で旅をしながらおふろはいれるの！？」

TW: 「哇！一邊坐車旅行，一邊還能泡澡嗎？！」

VN cũ: 「Đúng là dễ thương thật. Hoàn toàn không giống một toa hành khách thử nghiệm\\nđược chế tạo vội vàng từ \\x%l気動車;#00ffc040;toa xe diesel tự hành%l;#; phế liệu chút nào.」

Sửa: 「Oa! Vừa đi du lịch bằng tàu vừa được tắm bồn sao!?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1909 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1909.

### Key 1618 — 凪 — lệch dòng

JP: 「おおっ、にーさん来たと？」

TW: 「哇，大哥哥來啦？」

VN cũ: Dù là một công việc cực kỳ đơn điệu,\\nnhưng cô ấy lại tập trung đến mức đáng kinh ngạc.

Sửa: 「Oa, anh hai tới đó hả?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2851 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2851.

### Key 1621 — 路子 — lệch dòng

JP: 「えええっ！？」

TW: 「哎？！」

VN cũ: Nghe xong, tôi ngạc nhiên khi thấy bản thân mình không mấy bất ngờ.\\nA, nếu vậy thì――

Sửa: 「Ể!?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2721 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2721.

### Key 1626 — 双鉄 — dịch sai

JP: 「あ――」

TW: 「啊……」

VN cũ: 「Ừm?」

Sửa: 「A――」

Lý do: Dịch sai tiếng cảm thán: JP 「あ――」 (ngạc nhiên) bị dịch thành 「Ừm?」 (nghi vấn). Sửa theo JP + TW (啊……).

### Key 1629 — 日々姫 — gasp っ

JP: 「っ！　――っ！」

TW: 「啊！　……唔！」

VN cũ: 「! ――!」

Sửa: 「Ư! ――Ư!」

Lý do: Gasp っ (sweep, lost-gasp-trailing): JP 「あっ！」 — っ bị mất, VN cũ "A!" thiếu độ nghẹn. Sửa 「Ư!」 (áp nguyên fix của sweep).

### Key 1630 — 双鉄 — gasp っ

JP: 「っ！」

TW: 「啊！」

VN cũ: 「Vậy sao!」

Sửa: 「Ư!」

Lý do: Gasp っ (sweep, needs-file-audit): JP chỉ là 「っ！」 (TW 啊！) nhưng VN cũ là câu đầy đủ "Vậy sao!" (lệch dòng, mồ côi trong file). Fix 「Ư!」.

### Key 1633 — 日々姫 — gasp っ

JP: 「っ！！」

TW: 「啊！！」

VN cũ: 「!!」

Sửa: 「Ư!!」

Lý do: Gasp っ (sweep, lost-gasp-whole): JP 「うぇっ！？」 — っ bị mất, VN cũ "Ugh!?" không thể hiện được. Sửa 「Ư!?」. (áp nguyên fix của sweep).

### Key 1637 — 路子 — lệch dòng

JP: 「うんっ！！」

TW: 「嗯！！」

VN cũ: Lời nói, tự động thốt ra.\\nNhư thể thay cho những giọt nước mắt, tuyệt đối không được rơi trước mặt Michiko.

Sửa: 「Vâng!!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2800 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2800.

### Key 1650 — 双鉄 — lệch dòng

JP: 「うむ？」

TW: 「嗯？」

VN cũ: Lấp lánh rạng ngời, mang đậm nét trẻ thơ――\\nA, đúng rồi. Đây chính là ánh mắt của Michiko……của em gái tôi.

Sửa: 「Ừm?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2481 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2481.

### Key 1651 — 双鉄 — dịch sai

JP: 「うむ！？」

TW: 「嗯？！」

VN cũ: 「A, này.」

Sửa: 「Ừm!?」

Lý do: Dịch sai tiếng cảm thán: JP 「うむ！？」 bị dịch thành "A, này.". Sửa 「Ừm!?」 (theo các dòng うむ khác trong file: 1635/1643/1646/1648/1649 đều dùng "Ừm").

### Key 1667 — 双鉄 — lệch dòng

JP: 「つかれるタイプの風呂において、\\n日ノ本人は恐るべき量の水を消費する」

TW: 「在泡澡的時候，日本人會用掉驚人多的水」

VN cũ: Nếu hoàn toàn không có dữ liệu nào,\\nthì không còn cách nào khác ngoài việc cho xe chạy thực tế để thử nghiệm.

Sửa: 「Đối với loại bồn tắm ngâm mình,\\nngười Hinomoto tiêu thụ một lượng nước đáng sợ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2618 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2618.

### Key 1692 — 双鉄 — lệch dòng

JP: 「父さんと母さんと、もうすぐ会える。か――」

TW: 「她馬上就能見到父親母親了啊……」

VN cũ: 「A――」

Sửa: 「Sắp được gặp lại bố và mẹ rồi, phải không――」

Lý do: Lệch dòng: VN hiện tại ("A――") là bản dịch của JP key 1653/1654 (「ああ――"). Fix viết mới từ JP + TW (TW: cô ấy sắp được gặp bố mẹ).

### Key 1694 — 路子 — lệch dòng

JP: 「おもしろーい！」

TW: 「好有意思！」

VN cũ: 「Đối với loại bồn tắm ngâm mình,\\nngười Hinomoto tiêu thụ một lượng nước đáng sợ.」

Sửa: 「Thú vị quá!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1667 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1667.

### Key 1696 — みくろ — lệch dòng

JP: 「はぁい。いまいきまーす」

TW: 「好的，馬上就來」

VN cũ: 「Cô Nakamura. Nói chuyện một chút được không.」

Sửa: 「Dạ. Em đến ngay đây ạ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1446 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 1708 — 双鉄 — lệch dòng

JP: 「試験がうまく行き、かつ諸問題も解決できていればな。\\nそのための実験をする\\x%l客車;#00ffc040;客車%l;#;が、試験客車だ」

TW: 「如果測試順利，並且解決了各種問題就可以。用來做這些實驗的\\x%l客車;#00ffc040;客運車廂%l;#;，就是測試客車」

VN cũ: Do đó, nó đặc biệt được những người nước ngoài thích sự mới lạ ưa chuộng.

Sửa: 「Nếu cuộc thử nghiệm diễn ra suôn sẻ, và giải quyết được các vấn đề liên quan.\\n\\x%l客車;#00ffc040;Toa hành khách%l;#; dùng để thực hiện các thí nghiệm đó, chính là toa hành khách thử nghiệm.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2598 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2598.

### Key 1713 — 双鉄 — lệch dòng

JP: 「そうであるなら、僕らにとっても嬉しいことだな」

TW: 「如果真能成功，我們也會感覺很榮幸」

VN cũ: Tập hợp dữ liệu thu được dù phải trả cái giá đó,\\nchắc chắn sẽ trở thành tài sản của Ohimitera――không, của toàn bộ ngành đường sắt Hinomoto.

Sửa: 「Nếu đúng là như vậy, thì đối với chúng ta cũng là một điều đáng mừng.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2288 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 1724 — 双鉄 — lệch dòng

JP: 「文字通り、様々な試験を行うための\\x%l客車;#00ffc040;客車%l;#;だ。\\n僕らの列車。ナインスターズを走らせるための」

TW: 「字面意思，就是用來進行各種測試的\\x%l客車;#00ffc040;客運車廂%l;#;。有了它才能讓我們的列車——九星成功運行起來」

VN cũ: 「Những nỗ lực huy động vốn đó đã trực tiếp trở thành một chiến dịch quảng bá,\\nvà thu hút được sự chú ý. Kết quả là, khắp các vùng của Kyushu, bao gồm cả Ohimitera.」

Sửa: 「Đúng như tên gọi, là \\x%l客車;#00ffc040;toa hành khách%l;#; dùng để tiến hành nhiều thử nghiệm khác nhau.\\nĐể cho đoàn tàu của chúng ta. Nine Stars, được lăn bánh.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1780 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1780.

### Key 1737 — 双鉄 — lệch dòng

JP: 「車籍を外れ、[あさぎり,1]麻霧駅に留置。レンタルスペースとして\\n地域の皆様や、僕らの役に立ち続けることになる」

TW: 「將它們移除車籍，放置在麻霧站。作為可租賃空間，繼續給當地的居民和我們作貢獻」

VN cũ: Vừa nói vừa cười, nhưng ngay sau đó,\\nkhuôn mặt Michiko lại chuyển sang vẻ hơi bất mãn.

Sửa: 「Chúng sẽ bị rút khỏi danh sách đăng ký xe, và được lưu giữ tại ga Asagiri. Dưới hình thức không gian cho thuê,\\nchúng sẽ tiếp tục giúp ích cho mọi người trong khu vực và cả chúng ta nữa.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2831 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2831.

### Key 1745 — 路子 — lệch dòng

JP: 「そーちゃん！　そーちゃん！！」

TW: 「小雙！小雙！！」

VN cũ: 「Tuyệt quá! Em cảm ơn anh!\\nEm sẽ cố gắng!」

Sửa: 「Sou-chan! Sou-chan!!」

Lý do: Lệch dòng: VN hiện tại là câu cảm ơn (mồ côi trong file). Fix viết mới: Michiko gọi Soutetsu là そーちゃん → "Sou-chan" (theo tiền lệ trong chính file này: 1902 → VN ở 2854 dùng "Sou-chan").

### Key 1749 — 双鉄 — lệch dòng

JP: 「とても大きな困りごとのことだな。\\n線路を繋げるためのお金が、足りなくなりかけたのだ」

TW: 「就是巨大的困難。連接線路需要的資金馬上要不夠用了」

VN cũ: 「――Vậy sao.」

Sửa: 「Là một rắc rối rất lớn đó.\\nSố tiền để kết nối đường ray, suýt chút nữa là không đủ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1133 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1133.

### Key 1755 — 路子 — lệch dòng

JP: 「おふろをつんであるれっ車。\\nすぐにはむりでも、みらいに、みち、のれるかなぁ」

TW: 「就算短時間內不行，小路在未來……能坐上有浴室的列車嗎」

VN cũ: 「Sẽ trở thành nơi mọi người tụ tập sao?」

Sửa: 「Đoàn tàu có chở theo bồn tắm.\\nDù bây giờ chưa được, nhưng trong tương lai, Michi, có được lên không nhỉ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1841 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1841.

### Key 1770 — 双鉄 — lệch dòng

JP: 「試験の結果、今予定されているナインスターズ\\x%l編成;#00ffc040;編成%l;#;では、\\n風呂桶の設置は極めて厳しいとわかってしまったからな」

TW: 「從測試結果來看，以九星目前設計中的\\x%l編成;#00ffc040;編組%l;#;，想設置浴桶非常困難」

VN cũ: 「Ví dụ như, có một kế hoạch biến một phần của Nine Stars thành phòng tắm vòi sen,\\nvà lắp đặt một bồn tắm nhỏ ở đó.」

Sửa: 「Vì kết quả thử nghiệm cho thấy, với \\x%l編成;#00ffc040;đoàn tàu%l;#; Nine Stars dự kiến hiện tại,\\nviệc lắp đặt bồn tắm là cực kỳ khó khăn.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1862 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1862.

### Key 1774 — 双鉄 — lệch dòng

JP: 「どうした路子。そんなにあわてて」

TW: 「怎麼了，路子。你為什麼慌慌張張的」

VN cũ: ――A, đúng rồi. Fukami đã trở thành người lớn mất rồi.

Sửa: 「Sao thế Michiko. Sao lại hốt hoảng vậy.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1483 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1483.

### Key 1780 — 双鉄 — lệch dòng

JP: 「お金を集めるための努力がそのまま、宣伝になり、\\n人気を呼んだ。その結果、御一夜を含む九洲各地へ」

TW: 「我們籌集資金的努力也起到了宣傳效果，成功為包括御一夜在內的九州各地聚集了人氣」

VN cũ: 「Cái rủi?」

Sửa: 「Những nỗ lực huy động vốn đó đã trực tiếp trở thành một chiến dịch quảng bá,\\nvà thu hút được sự chú ý. Kết quả là, khắp các vùng của Kyushu, bao gồm cả Ohitoyo.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1116. Fix lấy từ VN key 1724, sửa "Ohimitera"→"Ohitoyo" (thuật ngữ đã quyết).

### Key 1787 — 双鉄 — lệch dòng

JP: 「僕は、やっぱり――\\n夢で、路子と会っていたんだ」

TW: 「我果然……是在夢裡見到了路子啊」

VN cũ: Giấc mơ mà thời niên thiếu tôi chắc chắn đã từng mơ, và rồi vứt bỏ,\\nnay được cô em gái sinh đôi của tôi, nhẹ nhàng đưa ra, và trả lại cho tôi.

Sửa: 「Anh, quả nhiên―― đã gặp Michiko, trong giấc mơ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2525. Fix viết mới: đây là lời thoại với Nagi (trong 「」) nên Soutetsu xưng "anh" — VN lệch dòng ở 2042 dùng "Mình" là sai ngữ cảnh (đó là độc thoại). Điểm tự quyết, xem § Lưu ý.

### Key 1789 — 双鉄 — lệch dòng

JP: 「路子と会って。話していたんだ」

TW: 「我見到了路子，還跟她說話了啊」

VN cũ: 「Vâng!!」

Sửa: 「Anh đã gặp Michiko. Và nói chuyện với em ấy.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1637. Fix viết mới với "anh" (thoại với Nagi); VN lệch dòng ở 2564 dùng "Mình" không đúng ngữ cảnh thoại.

### Key 1792 — 双鉄 — lệch dòng

JP: 「ゆえ、様々に検討した結果、車内はシャワーだけとした。\\nその代わり、各地方必ず、温泉駅での入浴停車を設けた」

TW: 「所以我們經過探討，決定只在車裡設置淋浴。作為替代，各地區都會在溫泉站停車，供乘客入浴」

VN cũ: 「Ra là vậy~」

Sửa: 「Vì vậy, sau khi xem xét nhiều phương án, chúng ta quyết định chỉ bố trí vòi hoa sen trên tàu.\\nĐổi lại, ở mỗi địa phương, chắc chắn sẽ có điểm dừng đỗ tại ga suối nước nóng để hành khách tắm rửa.」

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file). Fix lấy từ VN key 1713.

### Key 1800 — 路子 — lệch dòng

JP: 「だからね？　きっともうすぐ、\\nそーちゃんのれっ車、走るんだなって」

TW: 「所以，小雙的列車一定馬上就能跑起來了吧」

VN cũ: 「Ừm!?」

Sửa: 「Nên là nhé? Chắc chắn sắp rồi,\\nđoàn tàu của Sou-chan, sắp chạy rồi nhỉ.」

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file). Fix lấy từ VN key 1909.

### Key 1812 — 双鉄 — lệch dòng

JP: 「大丈夫だ。\\nもう、乗り越えてしまえたことだから」

TW: 「放心，我們已經解決了」

VN cũ: Ở một góc nào đó trong thâm tâm, có lẽ tôi cũng đã dự liệu được\\n……hoặc là đã chuẩn bị sẵn tinh thần rồi.

Sửa: 「Không sao đâu.\\nChuyện đó, chúng ta đã vượt qua được rồi.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2558 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2558.

### Key 1835 — 路子 — lệch dòng

JP: 「そーなの？」

TW: 「是嗎？」

VN cũ: Mình đã chìm vào giấc ngủ nhanh đến vậy sao.\\nHoặc cũng có thể là do――Michiko đã gọi mình.

Sửa: 「Vậy sao?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2718 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2718.

### Key 1841 — 路子 — lệch dòng

JP: 「みんながあつまる場所になるの？」

TW: 「會變成很多人聚集的地方嗎？」

VN cũ: 「Nhưng mà, bồn tắm trên tàu.\\nCất công thử nghiệm rồi mà, tiếc quá nhỉ.」

Sửa: 「Sẽ trở thành nơi mọi người tụ tập sao?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1496 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1496.

### Key 1843 — 双鉄 — lệch dòng

JP: 「一時期にはついていた。しかし、もうない。\\n残念ながら、今後つけられることもないだろう」

TW: 「有一段時間有，但是現在已經沒有了。很可惜，以後大概也不會再有了」

VN cũ: Nine Stars về cơ bản được thiết kế và vận hành,\\ndựa trên sự kết hợp giữa thủ công mỹ nghệ truyền thống và những công nghệ đã trưởng thành.

Sửa: 「Đã từng có một thời gian. Nhưng, bây giờ thì không còn nữa.\\nĐáng tiếc là, sau này có lẽ cũng sẽ không được lắp đặt nữa đâu.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2269 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2269.

### Key 1862 — 双鉄 — lệch dòng

JP: 「例えば、ナインスターズの一部をシャワー室とし、\\nそこには小さな風呂桶もつける計画があった」

TW: 「比如我們有個計劃，把九星的一部分劃為浴室，在裡面放上小浴桶」

VN cũ: 「Tên là Kuma (Gấu) sao? Đoàn tàu đó ấy. Dễ thương quá!」

Sửa: 「Ví dụ như, có một kế hoạch biến một phần của Nine Stars thành phòng tắm vòi sen,\\nvà lắp đặt một bồn tắm nhỏ ở đó.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1999 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1999.

### Key 1870 — 路子 — lệch dòng

JP: 「しけんきゃくしゃって？」

TW: 「測試客車是什麼？」

VN cũ: Trái phiếu Đường sắt Quốc tế Hinomoto do anh ta tạo ra. Thường gọi là Trái phiếu Hinomoto,\\nbắt đầu từ Pháp, nay đã được bán ở tận 7 quốc gia.

Sửa: 「Toa hành khách thử nghiệm là gì vậy?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2282 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2282.

### Key 1902 — 路子 — lệch dòng

JP: 「ほんと！？　ならね、そーちゃん――\\nあのね？　お耳かして」

TW: 「真的嗎？！這樣的話……小雙，你湊過來一下」

VN cũ: Nhìn vào đôi mắt Michiko đang ngước lên nhìn tôi,\\nkhông hiểu sao trong khoảnh khắc đó, tôi cảm thấy một nỗi nhớ nhà da diết.

Sửa: 「Thật sao!? Nếu vậy nhé, Sou-chan――\\nNày nhé? Đưa tai đây cho em.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2825 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2825.

### Key 1909 — 双鉄 — lệch dòng

JP: 「確かに可愛いな。廃棄された\\x%l気動車;#00ffc040;気動車%l;#;を改造した、\\n急造の試験客車とはまるで思えない」

TW: 「確實很可愛。完全看不出是用廢棄\\x%l気動車;#00ffc040;動車%l;#;趕製的測試客車」

VN cũ: Tình hình nguy hiểm đến mức ngay cả một đứa trẻ như Michiko cũng có thể cảm nhận được.\\nDo đó tôi vội vàng nói thêm, để nhanh chóng xua tan sự bất an của Michiko.

Sửa: 「Đúng là dễ thương thật. Hoàn toàn không giống một toa hành khách thử nghiệm\\nđược chế tạo vội vàng từ \\x%l気動車;#00ffc040;toa xe diesel tự hành%l;#; phế liệu chút nào.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2862 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2862.

### Key 1920 — 双鉄 — lệch dòng

JP: 「いつか、未来に。必ず風呂桶を乗せた列車が走る。\\n僕らの試験を、決して無駄になど終わらせはしないさ」

TW: 「總有一天，鐵路上一定會馳騁著裝載了浴桶的列車。我們絕對不會浪費這次測試的成果」

VN cũ: 「Dừng đỗ để tắm rửa! Nghe thú vị quá!!」

Sửa: 「Một ngày nào đó, trong tương lai. Chắc chắn sẽ có một đoàn tàu chở theo bồn tắm lăn bánh.\\nCuộc thử nghiệm của chúng ta, tuyệt đối sẽ không kết thúc trong vô ích đâu.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1523 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1523.

### Key 1921 — みくろ — lệch dòng

JP: 「みくろ、来ました。\\n右田\\x%l機関士;#00ffc040;機関士%l;#;、ご用はなんですか？」

TW: 「美玖路來了。右田\\x%l機関士;#00ffc040;司機%l;#;，有什麼事嗎？」

VN cũ: 「\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Chào buổi sáng.」

Sửa: 「Mikuro đến rồi đây. \\x%l機関士;#00ffc040;Lái tàu%l;#; Migita, có việc gì vậy ạ?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1578. Fix viết mới, giữ tag %l của 機関士 (gloss "Lái tàu").

### Key 1927 — 凪 — lệch dòng

JP: 「みくろー！　みくろー！\\nにーさんが呼んどるばい！！」

TW: 「美玖路！美玖路！大哥哥叫你嘞！！」

VN cũ: Không, giờ cô ấy đã là một người đi làm chững chạc rồi,\\ngọi là thiếu nữ thì cũng hơi thất lễ.

Sửa: 「Mikuro ơi! Mikuro ơi! Anh hai gọi em kìa!!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2251 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2251.

### Key 1941 — 双鉄 — lệch dòng

JP: 「それに、\\nクマ一・クマ二の試験終了後の職場も決まっている」

TW: 「而且隈一、隈二在測試結束後的工作地點也已經決定了」

VN cũ: 「Thú vị quá!」

Sửa: 「Hơn nữa,\\nnơi làm việc của Kuma 1 và Kuma 2 sau khi kết thúc thử nghiệm cũng đã được quyết định rồi.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1694 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1694.

### Key 1943 — 路子 — lệch dòng

JP: 「ね！　そーちゃん」

TW: 「聽我說，小雙！」

VN cũ: 「Một ngày nào đó, trong tương lai. Chắc chắn sẽ có một đoàn tàu chở theo bồn tắm lăn bánh.\\nCuộc thử nghiệm của chúng ta, tuyệt đối sẽ không kết thúc trong vô ích đâu.」

Sửa: 「Này! Sou-chan.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1920 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1920.

### Key 1984 — 双鉄 — lệch dòng

JP: 「そうしていきたい。ナインスターズの基礎を固める――\\n鉄道再建の、影の立役者となる車両なのだから」

TW: 「這是我們的願望。因為它們奠定了九星的基礎，是重建鐵路的幕後功臣啊」

VN cũ: 「Không, cũng không hẳn đâu. Kuma 1 và Kuma 2,\\nthực sự đã chịu đựng các cuộc thử nghiệm rất tốt mà.」

Sửa: 「Anh muốn như vậy. Bởi vì chúng là những toa xe đã củng cố nền tảng cho Nine Stars――\\nlà những người hùng thầm lặng trong công cuộc tái thiết đường sắt mà.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1437 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1437.

### Key 1987 — 路子 — lệch dòng

JP: 「そっか！　それならきっとクマさんたちもうれしいね」

TW: 「這樣呀！　那隈元號一定會很開心」

VN cũ: Việc liên tục cải tạo để đáp ứng tiêu chuẩn an toàn,\\nđã tích tụ những hao mòn không thể phục hồi lên toàn bộ \\x%l台枠;#00ffc040;khung gầm%l;\\x%l台車;#;#00ffc040;giá chuyển hướng%l;#; và thân xe.

Sửa: 「Ra vậy! Nếu thế thì chắc chắn các Kuma cũng sẽ vui lắm nhỉ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2329 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2620.

### Key 1988 — 路子 — lệch dòng

JP: 「それでなんだ！　外国のおきゃくさんふえてるの！\\n8620が今ひっぱってる、緑色のれっ車とかすごいよね」

TW: 「這樣呀！所以國外的遊客才會增加呀！８６２０現在拉著的綠色列車就好厲害」

VN cũ: 「Là một rắc rối rất lớn đó.\\nSố tiền để kết nối đường ray, suýt chút nữa là không đủ.」

Sửa: 「Ra là vậy! Khách nước ngoài đang tăng lên kìa!\\nĐoàn tàu màu xanh lá cây mà 8620 đang kéo bây giờ, tuyệt quá nhỉ.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1749 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1749.

### Key 1989 — 路子 — lệch dòng

JP: 「そおなんだー」

TW: 「這樣啊……」

VN cũ: 「Oa! Vừa đi du lịch bằng tàu vừa được tắm bồn sao!?」

Sửa: 「Vậy à~」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1613 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 1991 — 路子 — lệch dòng

JP: 「そーなんだ！」

TW: 「這樣啊！」

VN cũ: 「Thực chất, đó là \\x%lドカ停;#00ffc040;đỗ tàu lâu%l;#; bao gồm cả thời gian ăn uống và tham quan. Câu nói của Nagi\\n『Chỉ cần dừng tàu để tắm là được mà!』 đã trở thành yếu tố quyết định.」

Sửa: 「Vậy à!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1535 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 1999 — 路子 — lệch dòng

JP: 「クマっていうの？　あのれっ車。かわいい！」

TW: 「那叫隈元號呀？長得好可愛！」

VN cũ: 「Không sao đâu.\\nChuyện đó, chúng ta đã vượt qua được rồi.」

Sửa: 「Tên là Kuma (Gấu) sao? Đoàn tàu đó ấy. Dễ thương quá!」

Lý do: Lệch dòng: VN hiện tại là bản sao y hệt VN đúng của key 2613 (D51 Yufuin) — 2613 tự nó đúng, không cần sửa. Fix lấy từ VN key 1862.

### Key 2017 — 路子 — lệch dòng

JP: 「じゃ、クマさんたち、おふろついてるの？」

TW: 「那隈元號上面都有浴室嗎？」

VN cũ: 「Đúng như tên gọi, là \\x%l客車;#00ffc040;toa hành khách%l;#; dùng để tiến hành nhiều thử nghiệm khác nhau.\\nĐể cho đoàn tàu của chúng ta. Nine Stars, được lăn bánh.」

Sửa: 「Vậy, các Kuma, có bồn tắm không?」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1724 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1724.

### Key 2019 — 凪 — lệch dòng

JP: 「この三人を集めたんなら決まっとるばい！\\nあの話ばい！！」

TW: 「都把咱們三人叫到一起了！還不就是那件事唄！！」

VN cũ: 「Oa, anh hai tới đó hả?」

Sửa: 「Đã gọi cả ba người bọn em đến thế này thì chắc chắn là chuyện đó rồi!!」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1618 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1618.

### Key 2021 — 双鉄 — lệch dòng

JP: 「鈴木さん、しばらくお願いします」

TW: 「鈴木小姐，麻煩你看顧一下」

VN cũ: Đã có lúc sau một giấc ngủ, những muộn phiền được gỡ bỏ.\\nDù chỉ chợp mắt một lúc rồi tỉnh dậy, cơ thể lại trở nên nhẹ nhõm.

Sửa: 「Chị Suzuki, nhờ chị trông coi một lúc nhé.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2642 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2642.

### Key 2025 — 日々姫 — dịch sai

JP: 「にぃに、\\x%l投炭;#00ffc040;投炭%l;#;もあげるけん」

TW: 「阿哥，咱開始\\x%l投炭;#00ffc040;加煤%l;#;了」

VN cũ: 「Anh hai, em cũng tăng tốc \\x%l投炭;#00ffc040;thêm than%l;#; đây.」

Sửa: 「Anh hai, em cũng \\x%l投炭;#00ffc040;thêm than%l;#; đây.」

Lý do: Dịch sai: 投炭 (thêm than) bị dịch thêm "tăng tốc" không có trong JP/TW. Bỏ "tăng tốc", giữ nguyên tag %l.

### Key 2042 — 双鉄 — lệch dòng

JP: 「ならばまず、ナインスターズ一号列車を走らせて。\\nその更に先まで、レールを伸ばしていかねばならんな」

TW: 「首先得讓九星一號列車跑起來。還要讓鐵軌延伸向更遠的地方」

VN cũ: 「Mình, quả nhiên――\\nđã gặp Michiko, trong giấc mơ.」

Sửa: 「Nếu vậy thì trước tiên, phải cho đoàn tàu số 1 Nine Stars lăn bánh.\\nRồi phải kéo dài đường ray, vươn xa hơn nữa mới được.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1787 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1787.

### Key 2044 — 双鉄 — lệch dòng

JP: 「もうすぐ……か。\\nすぐ、というほどに早くは走り始められんが」

TW: 「馬上啊……也沒那麼快吧」

VN cũ: Bị đánh thức bởi giọng nói của Michiko.\\nMình vừa mới chui vào chăn thôi mà――a, không phải.

Sửa: 「Sắp rồi……sao.\\nCũng không thể bắt đầu chạy nhanh đến mức gọi là sắp được đâu, nhưng mà.」

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2830 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2830.

### Key 2045 — 路子 — lệch dòng

JP: 「もうすぐなんでしょ！　みちね、わかるの！\\nパパとママ、みちの近くに来てくれてるって！」

TW: 「馬上就要來了！小路能感覺到！爸爸媽媽快要來接小路了！」

VN cũ: Hơn nữa có lẽ, còn sớm hơn tôi rất nhiều.

Sửa: 「Sắp rồi đúng không! Michi, biết mà!\\nBố và mẹ, đang đến gần Michi rồi!」

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file); fix viết mới từ JP + TW.

### Key 2221 — monologue — lệch dòng

JP: ごく単純な理屈が悩みを解いてくれる。

TW: 一個極其簡單的道理解開了我的煩惱。

VN cũ: Nếu đó là sự kết nối, thì trong quá khứ tôi cũng đã cảm nhận được vô số lần.\\nTôi đã nghĩ chắc chắn đó là Michiko, và cũng mong muốn điều đó là sự thật.

Sửa: Một lý lẽ vô cùng đơn giản đã gỡ rối cho những muộn phiền của tôi.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2852 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2852.

### Key 2225 — monologue — lệch dòng

JP: そうしたときには、今と同じく。\\nきっと路子が、僕を励ましてくれてたのだろう。

TW: 一定都是因為路子鼓勵了我吧，就像剛才一樣。

VN cũ: Đó đúng là ga cuối――nhưng đồng thời, cũng là ga khởi hành.\\nĐưa đoàn tàu, hướng tới tương lai. Hướng tới một tương lai xa hơn nữa――

Sửa: Những lúc như vậy, cũng giống hệt như bây giờ.\\nChắc chắn Michiko, đã luôn cổ vũ cho tôi.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2854 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2854.

### Key 2251 — monologue — lệch dòng

JP: いや、立派な社会人となった今となっては、\\n少女よばわりも失礼だろうが。

TW: 不過她現在已經成長為一名出色的員工，再用少女來稱呼就太失禮了。

VN cũ: Sự ủy thác từ Paulette,\\ntôi cũng đã nhận lấy với tư cách là Trưởng phòng Vận hành.

Sửa: Không, giờ cô ấy đã là một người đi làm chững chạc rồi,\\ngọi là thiếu nữ thì cũng hơi thất lễ.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2564 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2564.

### Key 2262 — monologue — lệch dòng

JP: 学園生時代の凪を、ほとんど常に退け続けてきた、\\n九洲最強、全国屈指の剣道少女――

TW: 中村小姐可以說是九州最強、全國首屈一指的劍道少女，學生時代的凪都屢屢敗在她手下。

VN cũ: Một lý lẽ vô cùng đơn giản đã gỡ rối cho những muộn phiền của tôi.

Sửa: Cô gái Kendo mạnh nhất Kyushu, thuộc hàng top toàn quốc,\\nngười gần như luôn đánh bại Nagi thời còn đi học――

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2221 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2221.

### Key 2265 — monologue — lệch dòng

JP: 声をかければ、整備の手が止まる。\\nウェスをまとめ、零さぬように油を床の上に戻して。

TW: 中村小姐聽到我搭話，就停下了忙於整備工作的手。她收拾好擦機布，小心翼翼把油放回地上。

VN cũ: Tạm giao cửa hàng đường sắt cho nhân viên văn phòng Suzuki,\\ntôi đi tìm bóng dáng của những người trẻ tuổi sẽ gánh vác tương lai.

Sửa: Vừa cất tiếng gọi, tay đang bảo dưỡng liền dừng lại.\\nCô ấy gom giẻ lau lại, rồi cẩn thận đặt hộp dầu xuống sàn để không bị đổ.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2571 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2571.

### Key 2267 — monologue — lệch dòng

JP: 9室×6人で、最大54人の乗客。\\nその全員に同じ湯を使いまわさせるわけにもいかない。

TW: 九個六人間，乘客最多可達五十四人，不可能讓所有人都用同一桶水。

VN cũ: 「Nếu cuộc thử nghiệm diễn ra suôn sẻ, và giải quyết được các vấn đề liên quan.\\n\\x%l客車;#00ffc040;Toa hành khách%l;#; dùng để thực hiện các thí nghiệm đó, chính là toa hành khách thử nghiệm.」

Sửa: 9 phòng x 6 người, tối đa 54 hành khách.\\nKhông thể bắt tất cả họ dùng chung một bồn nước được.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1708 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1708.

### Key 2269 — monologue — lệch dòng

JP: ナインスターズは、基本的には伝統工芸や、\\n枯れた技術の組み合わせにより、設計され運用される。

TW: 九星基本上是將早已普及的基礎技術進行組合，再加上傳統工藝設計而成的。

VN cũ: 「Ra là vậy! Khách nước ngoài đang tăng lên kìa!\\nĐoàn tàu màu xanh lá cây mà 8620 đang kéo bây giờ, tuyệt quá nhỉ.」

Sửa: Nine Stars về cơ bản được thiết kế và vận hành,\\ndựa trên sự kết hợp giữa thủ công mỹ nghệ truyền thống và những công nghệ đã trưởng thành.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1988 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1988.

### Key 2270 — monologue — lệch dòng

JP: つまりは、今のは……\\n俗にいう、白昼夢というやつだろう。

TW: 也就是說……剛才的是白日夢啊。

VN cũ: 「――Ừ.」

Sửa: Tóm lại, lúc nãy là……\\nThứ mà người ta thường gọi là, giấc mơ giữa ban ngày.

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file). Fix lấy từ VN key 1792.

### Key 2282 — monologue — lệch dòng

JP: 彼の作成した国際日ノ本鉄路債。通称、ヒノモトボンドは、\\nフランクを皮切りに、実に7カ国で販売されるに至った。

TW: 他擬定的國際日本鐵路債券——通稱日本債券，以法國為起點，最終銷售向了七個國家。

VN cũ: 「Tuy nhiên, đúng là chúng ta đã vượt qua được một ngọn núi lớn và hiểm trở.\\nBởi vì trong cái rủi, lại có cái may.」

Sửa: Trái phiếu Đường sắt Quốc tế Hinomoto do anh ta tạo ra. Thường gọi là Trái phiếu Hinomoto,\\nbắt đầu từ Pháp, nay đã được bán ở tận 7 quốc gia.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1483 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1483.

### Key 2286 — monologue — lệch dòng

JP: 路子がどれほどキラキラと、\\n瞳を輝かせてくれたかを。

TW: 以及她那時的目光有多麼耀眼。

VN cũ: Tóm lại, lúc nãy là……\\nThứ mà người ta thường gọi là, giấc mơ giữa ban ngày.

Sửa: Rằng đôi mắt của Michiko,\\nđã lấp lánh rạng rỡ đến nhường nào.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2270 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2851.

### Key 2288 — monologue — lệch dòng

JP: その代償を払ってまでも得たデータ群は、\\n必ず御一夜――いや、日ノ本の鉄道全ての資産となる。

TW: 以這些代價換來的數據，一定會成為御一夜——不，會成為日本所有鐵路的寶貴資產。

VN cũ: 「Vì vậy, sau khi xem xét nhiều phương án, chúng ta quyết định chỉ bố trí vòi hoa sen trên tàu.\\nĐổi lại, ở mỗi địa phương, chắc chắn sẽ có điểm dừng đỗ tại ga suối nước nóng để hành khách tắm rửa.」

Sửa: Tập hợp dữ liệu thu được dù phải trả cái giá đó,\\nchắc chắn sẽ trở thành tài sản của Ohitoyo――không, của toàn bộ ngành đường sắt Hinomoto.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1792 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1713.

### Key 2300 — monologue — lệch dòng

JP: が、今まで誰一人試していない、\\n“枯れた技術の組み合わせ”も、いくらでもある。

TW: 但是，其中也有幾項從未有人嘗試過的“基礎技術組合”。

VN cũ: 「Toa hành khách thử nghiệm Kuma số 1, và Toa hành khách thử nghiệm Kuma số 2 sao.」

Sửa: Nhưng, cũng có vô số những “sự kết hợp công nghệ đã trưởng thành”\\nmà cho đến nay chưa từng có ai thử nghiệm.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1516 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1516.

### Key 2306 — monologue — lệch dòng

JP: 風呂桶の湯を完全入替えとする場合、\\n一走行、一人の入浴につき、平均300リットル弱の消費。

TW: 假設完全更換浴桶內的水，一趟下來平均每人需要消耗近三百升的水。

VN cũ: 「Vậy, các Kuma, có bồn tắm không?」

Sửa: Trong trường hợp thay toàn bộ nước trong bồn,\\nmỗi chuyến đi, một người tắm sẽ tiêu thụ trung bình gần 300 lít.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2017 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2017.

### Key 2329 — monologue — lệch dòng

JP: 安全基準を満たしながらの改造につぐ改造は、\\n\\x%l台枠;#00ffc040;台枠%l;\\x%l台車;#;#00ffc040;台車%l;#;車体全てに、回復不能な疲労をためた。

TW: 兩輛列車為了達到安全標準而進行了改造，在這基礎上的第二次改造，更是給\\x%l台枠;#00ffc040;車架%l;#;、\\x%l台車;#00ffc040;轉向架%l;#;、車體造成了無法恢復的損耗。

VN cũ: Hơn nữa, việc sử dụng nước giếng hay nước suối để bơm vào bồn chứa\\ncũng không phải là hiếm. Tôi không muốn phải gánh chịu rủi ro bị phàn nàn vì chuyện đó.

Sửa: Việc liên tục cải tạo để đáp ứng tiêu chuẩn an toàn,\\nđã tích tụ những hao mòn không thể phục hồi lên toàn bộ \\x%l台枠;#00ffc040;khung gầm%l;\\x%l台車;#;#00ffc040;giá chuyển hướng%l;#; và thân xe.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2763. Fix giữ nguyên dạng tag %l như VN gốc, kể cả tag 台車 bị lỗi phía JP (\x%l台車;#;#00ffc040;...) — lỗi tag phía JP không phải lỗi VN, không sửa.

### Key 2374 — monologue — lệch dòng

JP: 凪は\\x%lピット;#00ffc040;ピット%l;#;に潜っていたのか。\\n声とほとんど同時に姿が現れる。

TW: 凪似乎在\\x%lピット;#00ffc040;維修區%l;#;，話音未落就探出了身子。

VN cũ: （Quả nhiên là đối thủ của Nagi nhỉ）

Sửa: Nagi đang ở dưới \\x%lピット;#00ffc040;hố kiểm tra%l;#; sao. Vừa nghe thấy giọng nói thì bóng dáng đã xuất hiện.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2937. Fix viết mới, giữ tag %l của ピット (gloss "hố kiểm tra" theo TW 維修區).

### Key 2404 — monologue — gasp っ

JP: ふと、凪の足が止まる。\\nなんでもないような場所でいきなり――――っ！

TW: 凪突然駐足，停在一個看似毫無特殊之處的地方。不對，我想起來了。

VN cũ: "Đột nhiên, Nagi dừng bước.\\nỞ một nơi có vẻ như chẳng có gì đặc biệt――――っ!"

Sửa: "Đột nhiên, Nagi dừng bước. Ở một nơi có vẻ như chẳng có gì đặc biệt――――Ư!"

Lý do: Gasp っ (sweep, raw-tsu): VN cũ còn nguyên ký tự っ ("――――っ!"). Sửa 「――――Ư!」 (áp nguyên fix của sweep).

### Key 2428 — monologue — thuật ngữ

JP: 習熟のためも兼ねている湯医線客車列車の運行ですら、\\nD51の凪\\x%l機関士;#00ffc040;機関士%l;#;での乗務は確かまだ、200時間も無い筈だ。

TW: 即便把為熟悉操作而牽引湯醫線客運列車的時間也算上，凪在Ｄ５１上以\\x%l機関士;#00ffc040;司機%l;#;身份做乘務的經驗也不到２００小時。

VN cũ: Ngay cả với việc vận hành đoàn tàu khách trên tuyến Yui nhằm mục đích làm quen,\\nsố giờ trực của \\x%l機関士;#00ffc040;lái tàu%l;#; Nagi trên D51 chắc chắn vẫn chưa tới 200 giờ.

Sửa: Ngay cả với việc vận hành đoàn tàu khách trên tuyến Yunoi nhằm mục đích làm quen,\\nsố giờ trực của \\x%l機関士;#00ffc040;lái tàu%l;#; Nagi trên D51 chắc chắn vẫn chưa tới 200 giờ.

Lý do: Thuật ngữ: 湯医線 = "tuyến Yui" (sai) → "tuyến Yunoi" (đã quyết). Chỉ sửa đúng chỗ này; các tag %l của 機関士 giữ nguyên.

### Key 2478 — monologue — lệch dòng

JP: 8620をオイルで磨いてくれている。\\n丹念に丹念に――ただひたすらに丹念に。

TW: 她正聚精會神地給８６２０擦油。

VN cũ: Tôi vẫn nhớ. Rất rõ ràng.\\nNhững lời đã trao đổi với Michiko, và cả giọng nói ấy.

Sửa: Cô ấy đang lau chùi 8620 bằng dầu.\\nCẩn thận, tỉ mỉ――chỉ một mực cẩn thận và tỉ mỉ.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2590 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2590.

### Key 2481 — monologue — lệch dòng

JP: キラキラ輝く、こどもらしい――\\nああ、そうだ。これが路子の……僕の妹のまなざしだ。

TW: 她的眼神閃閃發光，稚氣未脫……啊，沒錯。這是屬於路子的——屬於我妹妹的目光。

VN cũ: 「Chúng sẽ bị rút khỏi danh sách đăng ký xe, và được lưu giữ tại ga Asagiri. Dưới hình thức không gian cho thuê,\\nchúng sẽ tiếp tục giúp ích cho mọi người trong khu vực và cả chúng ta nữa.」

Sửa: Lấp lánh rạng ngời, mang đậm nét trẻ thơ――\\nA, đúng rồi. Đây chính là ánh mắt của Michiko……của em gái tôi.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1737 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1737.

### Key 2492 — monologue — gasp っ

JP: それを計ることもできないうちに謝ろうとも、\\n謝罪は恐らく、上辺をなぞるだけしか――っ！！

TW: 如果不明白後果多嚴重，道歉也只是表面工夫而已……噢！

VN cũ: "Nếu chưa thể đong đếm được điều đó mà đã vội vàng xin lỗi,\\nthì lời xin lỗi có lẽ cũng chỉ là ngoài mặt——っ!!"

Sửa: "Nếu chưa thể đong đếm được điều đó mà đã vội vàng xin lỗi, thì lời xin lỗi có lẽ cũng chỉ là ngoài mặt——Ư!!"

Lý do: Gasp っ (sweep, raw-tsu): VN cũ còn nguyên ký tự っ ("――っ！！"). Sửa "——Ư!!" (áp nguyên fix của sweep).

### Key 2505 — monologue — lệch dòng

JP: 家族風呂扱いとし、9回の入浴で済ませるのなら、\\n複数人が一度につかれる、より大型の風呂桶が必要となる。

TW: 如果要設計成家庭浴室，讓入浴次數縮減為九次，就必須設置能夠容納多人的大型浴桶。

VN cũ: Nên đặt bồn tắm theo hướng đường ray, hay hướng \\x%l枕木;#00ffc040;tà vẹt đường ray%l;#;.\\nSẽ có bao nhiêu nước nóng bị tràn ra ngoài, và tiêu thụ bao nhiêu lít.

Sửa: Nếu coi như bồn tắm gia đình, và chỉ cần 9 lượt tắm là xong,\\nthì sẽ cần một bồn tắm lớn hơn để nhiều người có thể ngâm mình cùng lúc.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2802 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2802.

### Key 2520 — monologue — lệch dòng

JP: そうだ、僕は、何を勘違いしてしまっていたんだ。\\nナインスターズを走らせること、路子を送り届けること。

TW: 對，是我誤會了。讓九星行駛起來，以及將路子送達最終的目的地——

VN cũ: 「Chắc chắn sẽ được lên. Bất cứ đoàn tàu nào Michiko muốn, chắc chắn.\\nĐể làm được điều đó――anh, vẫn luôn cố gắng mà.」

Sửa: Đúng rồi, tôi đã hiểu lầm điều gì cơ chứ.\\nViệc cho Nine Stars lăn bánh, việc đưa tiễn Michiko.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1422 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1422.

### Key 2525 — monologue — lệch dòng

JP: 少年時代の僕がきっと夢見て、捨ててしまっていた夢を、\\n僕のふたごの妹が、そうっと差し出し、返してくれる。

TW: 少年時代的我懷揣著夢想，而現在我的雙胞胎妹妹，將我拋棄的夢想交還給我。

VN cũ: Nếu bố và mẹ đến đón.\\nThì từ lúc đó――thời gian mới của Michiko, sẽ lại bắt đầu trôi.

Sửa: Giấc mơ mà thời niên thiếu tôi chắc chắn đã từng mơ, và rồi vứt bỏ,\\nnay được cô em gái sinh đôi của tôi, nhẹ nhàng đưa ra, và trả lại cho tôi.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2620 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2620.

### Key 2558 — monologue — lệch dòng

JP: 僕もこころのどこかでは、予期を\\n……あるいは覚悟を、していたのだろう。

TW: 我其實已經有所預料……或者說是做好心理準備了吧。

VN cũ: 「Anh hai! Anh hai!!」

Sửa: Ở một góc nào đó trong thâm tâm, có lẽ tôi cũng đã dự liệu được\\n……hoặc là đã chuẩn bị sẵn tinh thần rồi.

Lý do: Lệch dòng: VN hiện tại ("Anh hai! Anh hai!!") không có JP tương ứng trong file (mồ côi trong file — có thể là câu にーさん của Nagi ở file khác). Fix lấy từ VN key 1812.

### Key 2564 — monologue — lệch dòng

JP: ポーレットからの一任も、\\n運転部長として既に受けている。

TW: 我已經接受了波萊特任命的運營部長職位。

VN cũ: 「Mình đã gặp Michiko. Và nói chuyện với em ấy.」

Sửa: Sự ủy thác từ Paulette,\\ntôi cũng đã nhận lấy với tư cách là Trưởng phòng Vận hành.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1789 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1789.

### Key 2571 — monologue — lệch dòng

JP: 事務員の鈴木さんへとレールショップをひととき預け、\\n未来を担う若者達の姿を探す。

TW: 我把鐵路商店交給事務員鈴木小姐關照，去尋找肩負未來的年輕人們。

VN cũ: Những lúc như vậy, cũng giống hệt như bây giờ.\\nChắc chắn Michiko, đã luôn cổ vũ cho tôi.

Sửa: Tạm giao cửa hàng đường sắt cho nhân viên văn phòng Suzuki,\\ntôi đi tìm bóng dáng của những người trẻ tuổi sẽ gánh vác tương lai.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2225 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2225.

### Key 2584 — monologue — lệch dòng

JP: 瞬きをして、いま僕は、目を開いているのだと――\\n手を握ってはまた開き、現実感を確かめる。

TW: 我眨了眨眼，發現自己正睜著眼睛。我握緊拳頭，然後再鬆開，確認這份現實感。

VN cũ: Michiko thì thầm vào tai tôi.\\nMột giấc mơ về đoàn tàu ngây thơ, mang đậm nét trẻ con.

Sửa: Chớp mắt một cái, và nhận ra bây giờ mình đang mở mắt――\\nTôi nắm chặt tay rồi lại mở ra, để xác nhận cảm giác thực tại.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2828 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2828.

### Key 2590 — monologue — lệch dòng

JP: 覚えている。はっきりと。\\n路子と交わした言葉を、声を。

TW: 我還清晰記得她的話語與聲音。

VN cũ: Chớp mắt một cái, và nhận ra bây giờ mình đang mở mắt――\\nTôi nắm chặt tay rồi lại mở ra, để xác nhận cảm giác thực tại.

Sửa: Tôi vẫn nhớ. Rất rõ ràng.\\nNhững lời đã trao đổi với Michiko, và cả giọng nói ấy.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2584 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2584.

### Key 2598 — monologue — lệch dòng

JP: ゆえに、特に珍しいもの好きの外国人に好まれている。

TW: 所以喜歡稀奇事物的外國人特別中意。

VN cũ: 「Fukami, Paulette, và tất cả mọi người.\\nMỗi người đều đã làm tất cả những gì có thể, nên mới vượt qua được.」

Sửa: Do đó, nó đặc biệt được những người nước ngoài thích sự mới lạ ưa chuộng.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1432 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1432.

### Key 2618 — monologue — lệch dòng

JP: データがまるでないことならば、\\n実車を走らせ、試していく他に手段は無い。

TW: 既然完全沒有數據可以參考，那就只能讓列車實際跑起來試一試了。

VN cũ: 「Toa hành khách thử nghiệm là gì vậy?」

Sửa: Nếu hoàn toàn không có dữ liệu nào,\\nthì không còn cách nào khác ngoài việc cho xe chạy thực tế để thử nghiệm.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1870 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1870.

### Key 2620 — monologue — lệch dòng

JP: 父さんと母さんが迎えにきたなら。\\nそこから再び――新しい路子の時間は、動き出すのだ。

TW: 既然父母來迎接路子了，那麼她也會再次迎來新生。

VN cũ: 「Ra vậy! Nếu thế thì chắc chắn các Kuma cũng sẽ vui lắm nhỉ.」

Sửa: Nếu bố và mẹ đến đón.\\nThì từ lúc đó――thời gian mới của Michiko, sẽ lại bắt đầu trôi.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1987 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1987.

### Key 2642 — monologue — lệch dòng

JP: 一眠りのあと、悩みが解けていることがあった。\\nうたた寝をして起きたというのに、体が軽くなっていた。

TW: 有時一覺醒來就解開了煩惱，有時只是打個瞌睡，就感覺身體輕鬆不少。

VN cũ: Đúng rồi, tôi đã hiểu lầm điều gì cơ chứ.\\nViệc cho Nine Stars lăn bánh, việc đưa tiễn Michiko.

Sửa: Đã có lúc sau một giấc ngủ, những muộn phiền được gỡ bỏ.\\nDù chỉ chợp mắt một lúc rồi tỉnh dậy, cơ thể lại trở nên nhẹ nhõm.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2520 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2021.

### Key 2643 — monologue — lệch dòng

JP: 未来――ああ。\\nそうだ、路子にも必ず未来が待ってる。

TW: 未來……沒錯，路子也一定擁有未來。

VN cũ: 「Anh muốn như vậy. Bởi vì chúng là những toa xe đã củng cố nền tảng cho Nine Stars――\\nlà những người hùng thầm lặng trong công cuộc tái thiết đường sắt mà.」

Sửa: Tương lai――A.\\nĐúng rồi, chắc chắn cũng có một tương lai đang chờ đợi Michiko.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1984 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1984.

### Key 2663 — monologue — lệch dòng

JP: 研修庫の方から声がする。\\n今日も今日とて、みくろはD51 1031を――

TW: 檢修庫方向傳來了美玖路的聲音。她今天也在細心地給Ｄ５１　１０３１做整備工作吧。

VN cũ: Vừa cất tiếng gọi, tay đang bảo dưỡng liền dừng lại.\\nCô ấy gom giẻ lau lại, rồi cẩn thận đặt hộp dầu xuống sàn để không bị đổ.

Sửa: Từ phía nhà xưởng bảo dưỡng vang lên tiếng nói. Hôm nay cũng như mọi hôm, Mikuro với D51 1031――

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2265. JP bị cắt cụt (kết bằng を――, không có động từ) — fix giữ nguyên dạng cụt, KHÔNG bịa phần hoàn thiện (TW gợi ý 整備/bảo dưỡng — xem § Lưu ý, chờ Hieu).

### Key 2694 — monologue — lệch dòng

JP: それから姿勢を整え直して、僕と向き合う。\\n――小動物めいた容姿ゆえ、その落ち着きが際立ち目立つ。

TW: 然後她端正好姿勢，向我轉過身來。她身材嬌小，所以讓沉穩的氣質變得極為顯眼。

VN cũ: 「……A, cô Nakamura ở đây sao.」

Sửa: Sau đó cô ấy chỉnh lại tư thế, quay mặt về phía tôi.\\n――Vì ngoại hình giống hệt một con thú nhỏ, nên sự điềm tĩnh đó càng trở nên nổi bật.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1123 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1123.

### Key 2703 — monologue — dịch sai

JP: 現在のクマ一・クマ二には、\\x%l死重;#00ffc040;死重%l;#;をたっぷり載せている。\\nナインスターズ客車の設計重量と同じ重さになるように。

TW: 現在的隈一、隈二上裝載了很多\\x%l死重;#00ffc040;呆重%l;#;。這是為了模擬九星客車的設計重量。

VN cũ: Kuma 1 và Kuma 2 hiện tại đang được chở đầy \\x%l死重;#00ffc040;trọng lượng bản thân%l;#;.\\nĐể có cùng trọng lượng với trọng lượng thiết kế của toa hành khách Nine Stars.

Sửa: Kuma 1 và Kuma 2 hiện tại đang được chất đầy \\x%l死重;#00ffc040;tải trọng chết%l;#;.\\nĐể có cùng trọng lượng với trọng lượng thiết kế của toa hành khách Nine Stars.

Lý do: Dịch sai: 死重 (tải trọng chết/ballast, TW 呆重) bị dịch thành "trọng lượng bản thân". Sửa gloss tag thành "tải trọng chết".

### Key 2718 — monologue — lệch dòng

JP: それほど早くに、僕は夢へと落ち込んだ。\\nあるいはきっと――路子が呼んでくれたのだ。

TW: 看來我很快就墜入了夢鄉。或許是因為路子在呼喚著我。

VN cũ: 「Từ đây là em tự về được rồi!\\nChúc ngủ ngon! Anh Soutetsu!!」

Sửa: Mình đã chìm vào giấc ngủ nhanh đến vậy sao.\\nHoặc cũng có thể là do――Michiko đã gọi mình.

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file); fix viết mới từ JP + TW.

### Key 2721 — monologue — lệch dòng

JP: 聞かされて、さほど自分が驚かないでいることに驚く。\\nああ、ならば――

TW: 真沒想到，我聽到這個消息後並不算很吃驚。這樣看來——

VN cũ: （Cọc cạch, cọc cạch,\\nxình xịch, xình xịch——）

Sửa: Nghe xong, tôi ngạc nhiên khi thấy bản thân mình không mấy bất ngờ.\\nA, nếu vậy thì――

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2929 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2929.

### Key 2763 — monologue — lệch dòng

JP: それに、水タンクにいれる水には、井戸水や湧水の利用も\\n珍しくない。クレームリスクを、そこで抱えたくもない。

TW: 而且水櫃內裝的水經常來自井水或者地下水。我不希望因為這個被乘客投訴。

VN cũ: 「Vì kết quả thử nghiệm cho thấy, với \\x%l編成;#00ffc040;đoàn tàu%l;#; Nine Stars dự kiến hiện tại,\\nviệc lắp đặt bồn tắm là cực kỳ khó khăn.」

Sửa: Hơn nữa, việc sử dụng nước giếng hay nước suối để bơm vào bồn chứa\\ncũng không phải là hiếm. Tôi không muốn phải gánh chịu rủi ro bị phàn nàn vì chuyện đó.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1770 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1770.

### Key 2765 — monologue — lệch dòng

JP: これが最低でも9回。一日につき、3t近くの水の追加と、\\nそれをおさめるためのタンクが必用となってしまう。

TW: 而這至少需要九次。每天要追加近三噸的水，就必須要有裝水的水槽。

VN cũ: 「Đã từng có một thời gian. Nhưng, bây giờ thì không còn nữa.\\nĐáng tiếc là, sau này có lẽ cũng sẽ không được lắp đặt nữa đâu.」

Sửa: Ít nhất cũng phải 9 lần. Tức là mỗi ngày cần bổ sung gần 3 tấn nước,\\nvà bắt buộc phải có một bồn chứa để chứa số nước đó.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1843 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1843.

### Key 2800 — monologue — lệch dòng

JP: 言葉が、勝手にこぼれ出ていく。\\n路子の前では決して流せぬ、涙の代わりであるかのように。

TW: 話語彷彿替代了在路子面前絕不會流下的眼淚，情不自禁奔湧而出。

VN cũ: 「Này! Sou-chan.」

Sửa: Lời nói, tự động thốt ra.\\nNhư thể thay cho những giọt nước mắt, tuyệt đối không được rơi trước mặt Michiko.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1943 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1943.

### Key 2802 — monologue — lệch dòng

JP: 風呂桶を線路方向、\\x%l枕木;#00ffc040;枕木%l;#;方向、いずれに設置するべきか。\\nどれほどの湯が零れてしまい、何リットルを消費するのか。

TW: 該把浴桶順線路方向，還是\\x%l枕木;#00ffc040;枕木%l;#;方向設置？路上會灑出多少水？水的消耗量又如何？

VN cũ: Tỷ lệ chọi trong các buổi rút thăm để được lên tàu chạy thử,\\nthậm chí có lúc còn lên tới gần 1/100.

Sửa: Nên đặt bồn tắm theo hướng đường ray, hay hướng \\x%l枕木;#00ffc040;tà vẹt đường ray%l;#;.\\nSẽ có bao nhiêu nước nóng bị tràn ra ngoài, và tiêu thụ bao nhiêu lít.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2836 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2836.

### Key 2825 — monologue — lệch dòng

JP: 僕をみあげる路子の瞳に、\\n何故か瞬間、物凄い郷愁を感じてしまう。

TW: 路子仰視著我，這讓我莫名感受到了濃烈的鄉愁。

VN cũ: 「Hơn nữa,\\nnơi làm việc của Kuma 1 và Kuma 2 sau khi kết thúc thử nghiệm cũng đã được quyết định rồi.」

Sửa: Nhìn vào đôi mắt Michiko đang ngước lên nhìn tôi,\\nkhông hiểu sao trong khoảnh khắc đó, tôi cảm thấy một nỗi nhớ nhà da diết.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1902 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1902.

### Key 2828 — monologue — lệch dòng

JP: ひそひそと、路子が僕に聞かせてくれる。\\nあどけない、とても子供らしい、列車の夢を。

TW: 路子在我耳邊低聲說了幾句。那是她純真而幼稚的、關於列車的夢。

VN cũ: 「Đoàn tàu có chở theo bồn tắm.\\nDù bây giờ chưa được, nhưng trong tương lai, Michi, có được lên không nhỉ.」

Sửa: Michiko thì thầm vào tai tôi.\\nMột giấc mơ về đoàn tàu ngây thơ, mang đậm nét trẻ con.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1755 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2584.

### Key 2830 — monologue — lệch dòng

JP: 路子の声に起こされる。\\nさっき布団に入ったばかりだというのに――ああ、違う。

TW: 路子的聲音叫醒了我。我明明才剛進被窩……不對。

VN cũ: Với bước chân nhẹ tênh, em ấy vui vẻ chạy đi.\\nĐến cả bóng lưng đó, trông cũng như đang mỉm cười.

Sửa: Bị đánh thức bởi giọng nói của Michiko.\\nMình vừa mới chui vào chăn thôi mà――a, không phải.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2044 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2044.

### Key 2831 — monologue — lệch dòng

JP: 言って笑って、けれどもすぐに、\\n路子は少し不満げな顔に変わってしまう。

TW: 路子說著露出了笑容，但馬上又轉為不滿。

VN cũ: Trong trường hợp thay toàn bộ nước trong bồn,\\nmỗi chuyến đi, một người tắm sẽ tiêu thụ trung bình gần 300 lít.

Sửa: Vừa nói vừa cười, nhưng ngay sau đó,\\nkhuôn mặt Michiko lại chuyển sang vẻ hơi bất mãn.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2306 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2306.

### Key 2836 — monologue — lệch dòng

JP: 人を乗せての試験走行のための抽選倍率が、\\n100に近づいてしまうことさえあるほどに。

TW: 載人行駛測試的應徵者人數，甚至達到了乘客容量的近百倍。

VN cũ: ――Đúng là trong cái rủi có cái may.\\nNgười phụ trách của ngân hàng Pháp do bác Maia giới thiệu rất xuất sắc.

Sửa: Tỷ lệ chọi trong các buổi rút thăm để được lên tàu chạy thử,\\nthậm chí có lúc còn lên tới gần 1/100.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1030 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2802.

### Key 2851 — monologue — lệch dòng

JP: 極めて単調な作業というのに、\\n驚くほどに集中している。

TW: 這是件極為單調的工作，她卻做得全神貫注、一絲不苟。

VN cũ: Rằng đôi mắt của Michiko,\\nđã lấp lánh rạng rỡ đến nhường nào.

Sửa: Dù là một công việc cực kỳ đơn điệu,\\nnhưng cô ấy lại tập trung đến mức đáng kinh ngạc.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2286. Fix lấy từ VN key 1618. (Bị sót ở lượt đọc 1, phát hiện ở lượt soát 2.)

### Key 2852 — monologue — lệch dòng

JP: よすがであるなら、過去にも何度も感じてはいた。\\nきっと路子だろうと思い、そうあって欲しいと願っていた。

TW: 這是我們之間的因緣吧，過去也有幾次同樣的感覺。我在心中如此期望著，那些時候我一定也是見到了路子。

VN cũ: 「――Hãy mong chờ nhé. Michiko.\\nAnh chắc chắn. Sẽ cho nó lăn bánh, và cho em lên tàu.」

Sửa: Nếu đó là sự kết nối, thì trong quá khứ tôi cũng đã cảm nhận được vô số lần.\\nTôi đã nghĩ chắc chắn đó là Michiko, và cũng mong muốn điều đó là sự thật.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1511. Fix lấy từ VN key 2221.

### Key 2854 — monologue — lệch dòng

JP: そこは確かに終着駅だが――同時に、始発駅でもある。\\n未来へ、列車を。もっと未来へ――

TW: 這的確是終點站，但同時也是嶄新的始發站。列車將載著她，駛向未來。

VN cũ: 「Thật sao!? Nếu vậy nhé, Sou-chan――\\nNày nhé? Đưa tai đây cho em.」

Sửa: Đó đúng là ga cuối――nhưng đồng thời, cũng là ga khởi hành.\\nĐưa đoàn tàu, hướng tới tương lai. Hướng tới một tương lai xa hơn nữa――

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1902 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1902.

### Key 2862 — monologue — lệch dòng

JP: 幼いままの路子にも、どれほど危険かが伝わる事態。\\nそれゆえ急ぎ言葉を重ね、路子の不安をすぐに解く。

TW: 連依然年幼的路子都能明白事態有多危急。所以我急忙補上一句，解除她的擔憂。

VN cũ: 「Nên là nhé? Chắc chắn sắp rồi,\\nđoàn tàu của Sou-chan, sắp chạy rồi nhỉ.」

Sửa: Tình hình nguy hiểm đến mức ngay cả một đứa trẻ như Michiko cũng có thể cảm nhận được.\\nDo đó tôi vội vàng nói thêm, để nhanh chóng xua tan sự bất an của Michiko.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 1800 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 1909.

### Key 2878 — monologue — lệch dòng

JP: 湯富院で解体を待つのみの窮地から、奇跡の復元を遂げた\\nデゴイチを、大事に整備していたのだろう。

TW: 那輛Ｄ５１在湯布院等待解體的絕境中奇蹟般盼來了修復的機會。

VN cũ: Sau đó cô ấy chỉnh lại tư thế, quay mặt về phía tôi.\\n――Vì ngoại hình giống hệt một con thú nhỏ, nên sự điềm tĩnh đó càng trở nên nổi bật.

Sửa: Chiếc D51 đã kỳ diệu được phục dựng từ tình cảnh ngặt nghèo chỉ còn chờ bị tháo dỡ ở Yufuin――chắc hẳn cô ấy đã cẩn thận bảo dưỡng nó.

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2694 (xem § Chuỗi lệch dòng); bản dịch đúng không còn trong file nên fix viết mới từ JP + TW.

### Key 2929 — monologue — lệch dòng

JP: （カトン、トトン、\\nタタン、タタン――）

TW: （哐啷，哐啷，哐啷，哐啷……）

VN cũ: 「Ừ. Lúc đó, anh sẽ chủ động mời em.」

Sửa: （Cọc cạch, cọc cạch,\\nxình xịch, xình xịch——）

Lý do: Lệch dòng: VN hiện tại không có JP tương ứng trong file này (mồ côi trong file); fix viết mới từ JP + TW.

### Key 2930 — monologue — dịch sai

JP: （ザッ！　ザッ！！！）

TW: （唰啦！唰啦！！！）

VN cũ: （Phập! Phập!!!）

Sửa: （Xoạt! Xoạt!!!）

Lý do: Dịch sai SFX: ザッ (TW 唰啦 — tiếng sột soạt) bị dịch thành "Phập" (tiếng đâm). Sửa "Xoạt".

### Key 2937 — monologue — lệch dòng

JP: （さすがは、凪のライバルか）

TW: （真不愧是凪的勁敵啊）

VN cũ: 「Nếu vậy thì trước tiên, phải cho đoàn tàu số 1 Nine Stars lăn bánh.\\nRồi phải kéo dài đường ray, vươn xa hơn nữa mới được.」

Sửa: （Quả nhiên là đối thủ của Nagi nhỉ）

Lý do: Lệch dòng: VN hiện tại là bản dịch của JP key 2042 (xem § Chuỗi lệch dòng). Fix lấy từ VN key 2042.

## Lượt soát 2

- **Tổng 129 / tái kiểm chứng 129 / bỏ 1 / sửa 7 / thêm 1.**
- Lượt soát 2 gồm 2 bước: (a) đọc lại toàn bộ 484 dòng trong bảng kiểm chứng — phát hiện **2851 bị sót** (thêm vào) và **2853 đọc nhầm** (VN cũ đúng, loại ra); (b) đọc lại toàn bộ **129 giá trị fix** trong bản dump lượt 2 so với JP — **129/129 khớp, 0 bỏ thêm, 0 sửa thêm**.
- Trước lượt soát 2, kiểm tra máy trong lúc build đã sửa: 7 nguồn ADOPT sai (1987, 2286, 2642, 2828, 2831, 2836, 2862), bổ sung dấu 「」 cho 18 fix viết mới (chỉ định dạng, không đổi nghĩa), và thêm tag %l của 機関士 còn thiếu ở 1921.

## Khối TOML (129 khóa — đã kiểm chứng bằng tomllib: 129 khóa, 0 sai lệch giá trị so với JSON)

```toml
[script]
1030 = "――Đúng là trong cái rủi có cái may.\\nNgười phụ trách của ngân hàng Pháp do bác Maia giới thiệu rất xuất sắc."
1116 = "「Cái rủi?」"
1123 = "「……A, cô Nakamura ở đây sao.」"
1125 = "「――À.」"
1133 = "「――Vậy sao.」"
1422 = "「Chắc chắn sẽ được lên. Bất cứ đoàn tàu nào Michiko muốn, chắc chắn.\\nĐể làm được điều đó――anh, vẫn luôn cố gắng mà.」"
1423 = "「Sẽ được lên mà.」"
1432 = "「Fukami, Paulette, và tất cả mọi người.\\nMỗi người đều đã làm tất cả những gì có thể, nên mới vượt qua được.」"
1435 = "「Ể~」"
1437 = "「Không, cũng không hẳn đâu. Kuma 1 và Kuma 2,\\nthực sự đã chịu đựng các cuộc thử nghiệm rất tốt mà.」"
1446 = "「Cô Nakamura. Nói chuyện một chút được không.」"
1455 = "「Cũng có đề xuất sử dụng nước lò hơi hay nước trong bồn chứa làm \"Nước tắm đầu máy hơi nước\",\\nnhưng không phải đoạn đường nào cũng do đầu máy hơi nước kéo.」"
1483 = "「Tuy nhiên, đúng là chúng ta đã vượt qua được một ngọn núi lớn và hiểm trở.\\nBởi vì trong cái rủi, lại có cái may.」"
1496 = "「Nhưng mà, bồn tắm trên tàu.\\nCất công thử nghiệm rồi mà, tiếc quá nhỉ.」"
1504 = "「Cả hai đều ở đây rồi thì nói chuyện sẽ nhanh thôi. Nếu được thì gọi cả Mikuro đến nữa.」"
1511 = "「――Hãy mong chờ nhé. Michiko.\\nAnh chắc chắn. Sẽ cho nó lăn bánh, và cho em lên tàu.」"
1516 = "「Toa hành khách thử nghiệm Kuma số 1, và Toa hành khách thử nghiệm Kuma số 2 sao.」"
1523 = "「Dừng đỗ để tắm rửa! Nghe thú vị quá!!」"
1535 = "「Thực chất, đó là đỗ tàu lâu bao gồm cả thời gian ăn uống và tham quan. Câu nói của Nagi\\n『Chỉ cần dừng tàu để tắm là được mà!』 đã trở thành yếu tố quyết định.」"
1578 = "「\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Chào buổi sáng.」"
1613 = "「Oa! Vừa đi du lịch bằng tàu vừa được tắm bồn sao!?」"
1618 = "「Oa, anh hai tới đó hả?」"
1621 = "「Ể!?」"
1626 = "「A――」"
1629 = "「Ư! ――Ư!」"
1630 = "「Ư!」"
1633 = "「Ư!!」"
1637 = "「Vâng!!」"
1650 = "「Ừm?」"
1651 = "「Ừm!?」"
1667 = "「Đối với loại bồn tắm ngâm mình,\\nngười Hinomoto tiêu thụ một lượng nước đáng sợ.」"
1692 = "「Sắp được gặp lại bố và mẹ rồi, phải không――」"
1694 = "「Thú vị quá!」"
1696 = "「Dạ. Em đến ngay đây ạ.」"
1708 = "「Nếu cuộc thử nghiệm diễn ra suôn sẻ, và giải quyết được các vấn đề liên quan.\\n\\x%l客車;#00ffc040;Toa hành khách%l;#; dùng để thực hiện các thí nghiệm đó, chính là toa hành khách thử nghiệm.」"
1713 = "「Nếu đúng là như vậy, thì đối với chúng ta cũng là một điều đáng mừng.」"
1724 = "「Đúng như tên gọi, là \\x%l客車;#00ffc040;toa hành khách%l;#; dùng để tiến hành nhiều thử nghiệm khác nhau.\\nĐể cho đoàn tàu của chúng ta. Nine Stars, được lăn bánh.」"
1737 = "「Chúng sẽ bị rút khỏi danh sách đăng ký xe, và được lưu giữ tại ga Asagiri. Dưới hình thức không gian cho thuê,\\nchúng sẽ tiếp tục giúp ích cho mọi người trong khu vực và cả chúng ta nữa.」"
1745 = "「Sou-chan! Sou-chan!!」"
1749 = "「Là một rắc rối rất lớn đó.\\nSố tiền để kết nối đường ray, suýt chút nữa là không đủ.」"
1755 = "「Đoàn tàu có chở theo bồn tắm.\\nDù bây giờ chưa được, nhưng trong tương lai, Michi, có được lên không nhỉ.」"
1770 = "「Vì kết quả thử nghiệm cho thấy, với \\x%l編成;#00ffc040;đoàn tàu%l;#; Nine Stars dự kiến hiện tại,\\nviệc lắp đặt bồn tắm là cực kỳ khó khăn.」"
1774 = "「Sao thế Michiko. Sao lại hốt hoảng vậy.」"
1780 = "「Những nỗ lực huy động vốn đó đã trực tiếp trở thành một chiến dịch quảng bá,\\nvà thu hút được sự chú ý. Kết quả là, khắp các vùng của Kyushu, bao gồm cả Ohitoyo.」"
1787 = "「Anh, quả nhiên―― đã gặp Michiko, trong giấc mơ.」"
1789 = "「Anh đã gặp Michiko. Và nói chuyện với em ấy.」"
1792 = "「Vì vậy, sau khi xem xét nhiều phương án, chúng ta quyết định chỉ bố trí vòi hoa sen trên tàu.\\nĐổi lại, ở mỗi địa phương, chắc chắn sẽ có điểm dừng đỗ tại ga suối nước nóng để hành khách tắm rửa.」"
1800 = "「Nên là nhé? Chắc chắn sắp rồi,\\nđoàn tàu của Sou-chan, sắp chạy rồi nhỉ.」"
1812 = "「Không sao đâu.\\nChuyện đó, chúng ta đã vượt qua được rồi.」"
1835 = "「Vậy sao?」"
1841 = "「Sẽ trở thành nơi mọi người tụ tập sao?」"
1843 = "「Đã từng có một thời gian. Nhưng, bây giờ thì không còn nữa.\\nĐáng tiếc là, sau này có lẽ cũng sẽ không được lắp đặt nữa đâu.」"
1862 = "「Ví dụ như, có một kế hoạch biến một phần của Nine Stars thành phòng tắm vòi sen,\\nvà lắp đặt một bồn tắm nhỏ ở đó.」"
1870 = "「Toa hành khách thử nghiệm là gì vậy?」"
1902 = "「Thật sao!? Nếu vậy nhé, Sou-chan――\\nNày nhé? Đưa tai đây cho em.」"
1909 = "「Đúng là dễ thương thật. Hoàn toàn không giống một toa hành khách thử nghiệm\\nđược chế tạo vội vàng từ \\x%l気動車;#00ffc040;toa xe diesel tự hành%l;#; phế liệu chút nào.」"
1920 = "「Một ngày nào đó, trong tương lai. Chắc chắn sẽ có một đoàn tàu chở theo bồn tắm lăn bánh.\\nCuộc thử nghiệm của chúng ta, tuyệt đối sẽ không kết thúc trong vô ích đâu.」"
1921 = "「Mikuro đến rồi đây. \\x%l機関士;#00ffc040;Lái tàu%l;#; Migita, có việc gì vậy ạ?」"
1927 = "「Mikuro ơi! Mikuro ơi! Anh hai gọi em kìa!!」"
1941 = "「Hơn nữa,\\nnơi làm việc của Kuma 1 và Kuma 2 sau khi kết thúc thử nghiệm cũng đã được quyết định rồi.」"
1943 = "「Này! Sou-chan.」"
1984 = "「Anh muốn như vậy. Bởi vì chúng là những toa xe đã củng cố nền tảng cho Nine Stars――\\nlà những người hùng thầm lặng trong công cuộc tái thiết đường sắt mà.」"
1987 = "「Ra vậy! Nếu thế thì chắc chắn các Kuma cũng sẽ vui lắm nhỉ.」"
1988 = "「Ra là vậy! Khách nước ngoài đang tăng lên kìa!\\nĐoàn tàu màu xanh lá cây mà 8620 đang kéo bây giờ, tuyệt quá nhỉ.」"
1989 = "「Vậy à~」"
1991 = "「Vậy à!」"
1999 = "「Tên là Kuma (Gấu) sao? Đoàn tàu đó ấy. Dễ thương quá!」"
2017 = "「Vậy, các Kuma, có bồn tắm không?」"
2019 = "「Đã gọi cả ba người bọn em đến thế này thì chắc chắn là chuyện đó rồi!!」"
2021 = "「Chị Suzuki, nhờ chị trông coi một lúc nhé.」"
2025 = "「Anh hai, em cũng \\x%l投炭;#00ffc040;thêm than%l;#; đây.」"
2042 = "「Nếu vậy thì trước tiên, phải cho đoàn tàu số 1 Nine Stars lăn bánh.\\nRồi phải kéo dài đường ray, vươn xa hơn nữa mới được.」"
2044 = "「Sắp rồi……sao.\\nCũng không thể bắt đầu chạy nhanh đến mức gọi là sắp được đâu, nhưng mà.」"
2045 = "「Sắp rồi đúng không! Michi, biết mà!\\nBố và mẹ, đang đến gần Michi rồi!」"
2221 = "Một lý lẽ vô cùng đơn giản đã gỡ rối cho những muộn phiền của tôi."
2225 = "Những lúc như vậy, cũng giống hệt như bây giờ.\\nChắc chắn Michiko, đã luôn cổ vũ cho tôi."
2251 = "Không, giờ cô ấy đã là một người đi làm chững chạc rồi,\\ngọi là thiếu nữ thì cũng hơi thất lễ."
2262 = "Cô gái Kendo mạnh nhất Kyushu, thuộc hàng top toàn quốc,\\nngười gần như luôn đánh bại Nagi thời còn đi học――"
2265 = "Vừa cất tiếng gọi, tay đang bảo dưỡng liền dừng lại.\\nCô ấy gom giẻ lau lại, rồi cẩn thận đặt hộp dầu xuống sàn để không bị đổ."
2267 = "9 phòng x 6 người, tối đa 54 hành khách.\\nKhông thể bắt tất cả họ dùng chung một bồn nước được."
2269 = "Nine Stars về cơ bản được thiết kế và vận hành,\\ndựa trên sự kết hợp giữa thủ công mỹ nghệ truyền thống và những công nghệ đã trưởng thành."
2270 = "Tóm lại, lúc nãy là……\\nThứ mà người ta thường gọi là, giấc mơ giữa ban ngày."
2282 = "Trái phiếu Đường sắt Quốc tế Hinomoto do anh ta tạo ra. Thường gọi là Trái phiếu Hinomoto,\\nbắt đầu từ Pháp, nay đã được bán ở tận 7 quốc gia."
2286 = "Rằng đôi mắt của Michiko,\\nđã lấp lánh rạng rỡ đến nhường nào."
2288 = "Tập hợp dữ liệu thu được dù phải trả cái giá đó,\\nchắc chắn sẽ trở thành tài sản của Ohitoyo――không, của toàn bộ ngành đường sắt Hinomoto."
2300 = "Nhưng, cũng có vô số những “sự kết hợp công nghệ đã trưởng thành”\\nmà cho đến nay chưa từng có ai thử nghiệm."
2306 = "Trong trường hợp thay toàn bộ nước trong bồn,\\nmỗi chuyến đi, một người tắm sẽ tiêu thụ trung bình gần 300 lít."
2329 = "Việc liên tục cải tạo để đáp ứng tiêu chuẩn an toàn,\\nđã tích tụ những hao mòn không thể phục hồi lên toàn bộ \\x%l台枠;#00ffc040;khung gầm%l;\\x%l台車;#;#00ffc040;giá chuyển hướng%l;#; và thân xe."
2374 = "Nagi đang ở dưới \\x%lピット;#00ffc040;hố kiểm tra%l;#; sao. Vừa nghe thấy giọng nói thì bóng dáng đã xuất hiện."
2404 = "\"Đột nhiên, Nagi dừng bước. Ở một nơi có vẻ như chẳng có gì đặc biệt――――Ư!\""
2428 = "Ngay cả với việc vận hành đoàn tàu khách trên tuyến Yunoi nhằm mục đích làm quen,\\nsố giờ trực của \\x%l機関士;#00ffc040;lái tàu%l;#; Nagi trên D51 chắc chắn vẫn chưa tới 200 giờ."
2478 = "Cô ấy đang lau chùi 8620 bằng dầu.\\nCẩn thận, tỉ mỉ――chỉ một mực cẩn thận và tỉ mỉ."
2481 = "Lấp lánh rạng ngời, mang đậm nét trẻ thơ――\\nA, đúng rồi. Đây chính là ánh mắt của Michiko……của em gái tôi."
2492 = "\"Nếu chưa thể đong đếm được điều đó mà đã vội vàng xin lỗi, thì lời xin lỗi có lẽ cũng chỉ là ngoài mặt——Ư!!\""
2505 = "Nếu coi như bồn tắm gia đình, và chỉ cần 9 lượt tắm là xong,\\nthì sẽ cần một bồn tắm lớn hơn để nhiều người có thể ngâm mình cùng lúc."
2520 = "Đúng rồi, tôi đã hiểu lầm điều gì cơ chứ.\\nViệc cho Nine Stars lăn bánh, việc đưa tiễn Michiko."
2525 = "Giấc mơ mà thời niên thiếu tôi chắc chắn đã từng mơ, và rồi vứt bỏ,\\nnay được cô em gái sinh đôi của tôi, nhẹ nhàng đưa ra, và trả lại cho tôi."
2558 = "Ở một góc nào đó trong thâm tâm, có lẽ tôi cũng đã dự liệu được\\n……hoặc là đã chuẩn bị sẵn tinh thần rồi."
2564 = "Sự ủy thác từ Paulette,\\ntôi cũng đã nhận lấy với tư cách là Trưởng phòng Vận hành."
2571 = "Tạm giao cửa hàng đường sắt cho nhân viên văn phòng Suzuki,\\ntôi đi tìm bóng dáng của những người trẻ tuổi sẽ gánh vác tương lai."
2584 = "Chớp mắt một cái, và nhận ra bây giờ mình đang mở mắt――\\nTôi nắm chặt tay rồi lại mở ra, để xác nhận cảm giác thực tại."
2590 = "Tôi vẫn nhớ. Rất rõ ràng.\\nNhững lời đã trao đổi với Michiko, và cả giọng nói ấy."
2598 = "Do đó, nó đặc biệt được những người nước ngoài thích sự mới lạ ưa chuộng."
2618 = "Nếu hoàn toàn không có dữ liệu nào,\\nthì không còn cách nào khác ngoài việc cho xe chạy thực tế để thử nghiệm."
2620 = "Nếu bố và mẹ đến đón.\\nThì từ lúc đó――thời gian mới của Michiko, sẽ lại bắt đầu trôi."
2642 = "Đã có lúc sau một giấc ngủ, những muộn phiền được gỡ bỏ.\\nDù chỉ chợp mắt một lúc rồi tỉnh dậy, cơ thể lại trở nên nhẹ nhõm."
2643 = "Tương lai――A.\\nĐúng rồi, chắc chắn cũng có một tương lai đang chờ đợi Michiko."
2663 = "Từ phía nhà xưởng bảo dưỡng vang lên tiếng nói. Hôm nay cũng như mọi hôm, Mikuro với D51 1031――"
2694 = "Sau đó cô ấy chỉnh lại tư thế, quay mặt về phía tôi.\\n――Vì ngoại hình giống hệt một con thú nhỏ, nên sự điềm tĩnh đó càng trở nên nổi bật."
2703 = "Kuma 1 và Kuma 2 hiện tại đang được chất đầy \\x%l死重;#00ffc040;tải trọng chết%l;#;.\\nĐể có cùng trọng lượng với trọng lượng thiết kế của toa hành khách Nine Stars."
2718 = "Mình đã chìm vào giấc ngủ nhanh đến vậy sao.\\nHoặc cũng có thể là do――Michiko đã gọi mình."
2721 = "Nghe xong, tôi ngạc nhiên khi thấy bản thân mình không mấy bất ngờ.\\nA, nếu vậy thì――"
2763 = "Hơn nữa, việc sử dụng nước giếng hay nước suối để bơm vào bồn chứa\\ncũng không phải là hiếm. Tôi không muốn phải gánh chịu rủi ro bị phàn nàn vì chuyện đó."
2765 = "Ít nhất cũng phải 9 lần. Tức là mỗi ngày cần bổ sung gần 3 tấn nước,\\nvà bắt buộc phải có một bồn chứa để chứa số nước đó."
2800 = "Lời nói, tự động thốt ra.\\nNhư thể thay cho những giọt nước mắt, tuyệt đối không được rơi trước mặt Michiko."
2802 = "Nên đặt bồn tắm theo hướng đường ray, hay hướng \\x%l枕木;#00ffc040;tà vẹt đường ray%l;#;.\\nSẽ có bao nhiêu nước nóng bị tràn ra ngoài, và tiêu thụ bao nhiêu lít."
2825 = "Nhìn vào đôi mắt Michiko đang ngước lên nhìn tôi,\\nkhông hiểu sao trong khoảnh khắc đó, tôi cảm thấy một nỗi nhớ nhà da diết."
2828 = "Michiko thì thầm vào tai tôi.\\nMột giấc mơ về đoàn tàu ngây thơ, mang đậm nét trẻ con."
2830 = "Bị đánh thức bởi giọng nói của Michiko.\\nMình vừa mới chui vào chăn thôi mà――a, không phải."
2831 = "Vừa nói vừa cười, nhưng ngay sau đó,\\nkhuôn mặt Michiko lại chuyển sang vẻ hơi bất mãn."
2836 = "Tỷ lệ chọi trong các buổi rút thăm để được lên tàu chạy thử,\\nthậm chí có lúc còn lên tới gần 1/100."
2851 = "Dù là một công việc cực kỳ đơn điệu,\\nnhưng cô ấy lại tập trung đến mức đáng kinh ngạc."
2852 = "Nếu đó là sự kết nối, thì trong quá khứ tôi cũng đã cảm nhận được vô số lần.\\nTôi đã nghĩ chắc chắn đó là Michiko, và cũng mong muốn điều đó là sự thật."
2854 = "Đó đúng là ga cuối――nhưng đồng thời, cũng là ga khởi hành.\\nĐưa đoàn tàu, hướng tới tương lai. Hướng tới một tương lai xa hơn nữa――"
2862 = "Tình hình nguy hiểm đến mức ngay cả một đứa trẻ như Michiko cũng có thể cảm nhận được.\\nDo đó tôi vội vàng nói thêm, để nhanh chóng xua tan sự bất an của Michiko."
2878 = "Chiếc D51 đã kỳ diệu được phục dựng từ tình cảnh ngặt nghèo chỉ còn chờ bị tháo dỡ ở Yufuin――chắc hẳn cô ấy đã cẩn thận bảo dưỡng nó."
2929 = "（Cọc cạch, cọc cạch,\\nxình xịch, xình xịch——）"
2930 = "（Xoạt! Xoạt!!!）"
2937 = "（Quả nhiên là đối thủ của Nagi nhỉ）"
```

## Kết bài

File グランドリライト09_凪 có tỷ lệ sai cao (26,7%) vì **lệch dòng là chủ đạo**: 118/129 dòng sai là VN bị xoay trong 12 chuỗi dài, với 2 chu trình 2 phần tử và 12 VN mồ côi trong file (nguồn chéo chưa xác định). Ngoài lệch dòng, chỉ có 5 gasp っ (4 áp nguyên từ sweep + 1630), 5 dịch sai và 1 thuật ngữ — không có lỗi hệ thống nào khác (không bịa quan hệ huyết thống, không sai đếm nguyên âm, không mất âm mora). Hai điểm cần Hieu: **1128** (người nghe chưa rõ) và **2663** (JP bị cắt cụt, TW gợi ý bảo dưỡng) — đã ghi rõ ở § Lưu ý. Khối TOML 129 khóa đã kiểm chứng parse và khớp JSON tuyệt đối.
