# Moan-fix: 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 2 dòng (LIGHT check)

## 0. Xác minh file

- File: `日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml` — route 02_Hibiki.
- TOML-2: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh6_#U30aa#U30ea#U30a8#U30f3#U30c6#U30fc#U30ea#U30f3#U30b0#U501f#U308a#U7269#U7af6#U8d70#Uff08#U30da#U30a2#Uff09.txt.toml`, md5 `77423bec9e1cb3f3bfbb14002019ad44` (khớp md5 audit), UTF-8 BOM + CRLF, 667 key script, 1 bản TOML duy nhất (không có file trùng).
- CSV3: 1 set duy nhất, 667/667 key khớp TOML. Không có set stale.
- Đây là LIGHT check theo task giao: audit (làm sau quy tắc romaji) đã sửa moan trong file; vòng này kiểm chứng lại các fix moan của audit rồi xét các dòng rên còn lại.
- Cơ sở tổng (đọc lại từ `moans/ROUTE-MOANS.md` lúc viết): **23 file / 526 dòng**.

## 1. Kho rên (moan inventory)

- Đã đọc 667/667 dòng qua CSV3 (kế thừa bản audit đã đọc hết; tự liệt kê lại toàn bộ dòng chứa âm rên/thở/gasp/SFX bằng mẫu + quét bổ sung phía VN và dải H-scene 1900–2850).
- 134 dòng ứng viên theo mẫu, phân loại: họ fa/fu 24, họ hya 7, SFX hôn/mút (ちゅ) 11, SFX hành động (ぐっ/びゅっ/ずぶ…) 20, cười 5, gasp/thán từ (あっ/はっ/んっ/うっ/はぁ/ふぅ…) 67.
- Trong 134 ứng viên: 38 dòng audit đã sửa (kiểm chứng lại toàn bộ ở §2), 96 dòng còn lại (giữ 95, sửa mới 1: 2082).
- Kết quả vòng này: **2 dòng đổi** — 1 sửa giá trị fix moan của audit (2075, đếm nguyên âm), 1 dòng rên mới (2082, mất phụ âm).

## 2. Kiểm chứng các fix moan của audit — 38 dòng, 37 đúng, 1 sai giá trị (2075)

Đã kiểm chứng lại từng fix moan của audit (đếm nguyên âm bằng máy từ JP, không đếm bằng mắt):

- §2c họ fa/fu → romaji (22 dòng: 1426, 2075, 2077, 2084, 2102, 2111, 2112, 2114, 2116, 2117, 2122, 2124, 2138, 2182, 2184, 2210, 2297, 2298, 2364, 2709, 2711, 2751): đúng 21/22 — chỉ 2075 sai đếm (xem §3a). 2114 `Faaaaaaa` 7a (ふぁ1 + ぁ×5 + あ1) ✓; 2196 `Fuyaaaaaaaaaaan` 11a (や1 + ぁ×10) ✓; 2117 `Fan` ✓; 2122 `Fa` ✓; 2297 `Pua` ✓; 2298 `Puha` ✓.
- §2d đếm nguyên âm trong dòng moan (8 dòng: 2080, 2109, 2190, 2196, 2199, 2202, 2203, 2713): đúng 8/8 — 2080 `Hya` 1a ✓; 2109 `fuuuuuuu` 7u (ふ1u + う×6) ✓; 2190 `Aa` 2a ✓; 2199 `Aaaa` 4a ✓; 2202 `Aaaaaa` 6a ✓; 2203 `Aaaa` 4a ✓; 2713 `kuuuu` 4u (く1u + う×3) ✓.
- Mất âm (2 dòng: 2266, 2085): đúng 2/2 — 2266 `KuunnnnnƯƯƯƯ` (くぅ 2u, ん×5, っ×4 → Ư×4) ✓; 2085 `Yaa` (やぁっ, tiền lệ mất phụ âm) ✓.
- Gasp Ư của audit (13 dòng §2a–2b): KHÔNG sửa lại — đúng quy tắc gasp khóa, không đụng vào. Sweep 10 mục đã được audit kiểm chứng (9 áp nguyên + 2282 nhãn "already-rendered" sai, audit đã sửa đúng).
- 2078 KHÔNG sửa — đúng theo quyết định của parent: VN cũ 14 u đã đúng (ふ 1u + ぅ×13, đã đếm lại bằng máy từ JP `ふぅぅぅぅぅぅぅぅぅぅぅぅぅんっ`).

## 3. Từng dòng sửa (2)

### 3a. 2075 — SỬA GIÁ TRỊ FIX CỦA AUDIT (đếm nguyên âm sai trong JSON)

- **2075** [日々姫] JP: 「きゃふうううううんっ！　あっ！　おな、かっ―― / ぎゅうんって――おちん、ちん――ひろげっ――ふあ」 / TW: 「呀嗯！啊！肚子裡――有感覺――雞雞――撐開了――呼」 / Cũ (TOML-2): 「Kyafuuuuun! A! Trong, bụng―― / Bị nhồi nhét――chim――mở rộng ra――phù」 / Mới: 「Kyafuuuuuun! A! Trong, bụng―― / Bị nhồi nhét――chim――mở rộng ra――Fua」
- Lý do: JP `きゃふうううううん` = ふ 1u + う×5 = **6u**, nên đúng là `Kyafuuuuuun` (6 u). VN cũ có 5u. Fix của audit trong JSON vẫn là 5u (`Kyafuuuuun`) — bản text review nói "thêm 1 u" nhưng giá trị JSON không hề tăng; chỉ phần ふあ→`Fua` là đã sửa đúng. Bản TOML block lẻ `audit-hibikih6-orienteering-karimono-tomlblock.txt` (51 khóa, bản trước khi parent sửa) thì lại có 7u (`Kyafuuuuuuun`) — cũng sai. Giá trị đúng duy nhất là 6u, khớp ghi chú của parent ("2075 sửa 7u→6u"). Fix ở đây giữ `Fua` của audit và sửa đếm về 6u.
- Lưu ý cho loop parent khi gộp: file `audit-hibikih6-orienteering-karimono-tomlblock.txt` là bản CŨ (51 khóa, còn 2078 đã loại + 2075 7u) — đừng dùng nó; JSON + khối TOML trong REVIEW.md của audit mới là bản đã sửa của parent (50 khóa), và fix 2075 ở đây đè lên cả hai.

### 3b. 2082 — MẤT PHỤ ÂM y (dòng rên mới, audit bỏ sót)

- **2082** [日々姫] JP: 「きゅはっ！　んっ――はんっ！　これ――やっ―― / なんで、こんな、に――すご、く――感じ――てっっ」 / TW: 「呀！嗯――呼！這個――呀―― / 為什麼、這麼――舒服啊――」 / Cũ: 「Kyuha! Ưm――han! Thế này――a―― / Tại sao, lại――cảm thấy――sướng, đến thế――này」 / Mới: 「Kyuha! Ưm――han! Thế này――Ya―― / Tại sao, lại――cảm thấy――sướng, đến thế――này」
- Lý do: やっ trong dòng rên bị diễn thành "a" — mất phụ âm y, cùng lỗi đã sửa ở 2085 (やぁっ → `Yaa`) và tiền lệ ポーレットh3 ("Á" cho きゃっ/ひゃっ/やっ là lỗi mất phụ âm). `Kyuha!` (きゅはっ), `han!` (はんっ) giữ nguyên — đã đúng. てっっ cuối dòng giữ nguyên "này" (っ nhấn mạnh trên từ nội dung, tiền lệ audit 2074/2082).

## 4. Giữ nguyên (ghi chú đáng kể)

- Họ ひゃ/ひゅ/ひあ/きゃ: **0 dòng dùng "Á"** — toàn bộ đã romaji đúng (2080 `Hya`, 2088 `Hyan`, 2074 `Hyaaaaan` 5a, 2090 `Hyaaa` 3a, 2077 `Hyuan`, 2185 `hyu`, 2725 `Kya`, 2087 `Kyafu`). Quy tắc 3b đã thỏa.
- Dạng tách âm "phù, a" / "Phù……a" cho ふ、あっ / ふ……ぁ (1944, 2106, 2194, 2713 + 2297 audit đã giữ): GIỮ — hai âm tách dấu câu, không phải một âm ふあ duy nhất; nhất quán với 2297 audit đã giữ "phù, a". Không chuyển sang romaji.
- "Hà" cho はぁっ (2035, 2098, 2108, 2118): GIỮ — cách diễn hơi thở đã chốt, 1 a đúng.
- Cười (2143 `Ehe……ehehehe`, 2144 `Ehehe!`, 2145 `Ehehe`, 2146 `Ehehe, ehehehe`, 2296 `Ufufufu`): GIỮ — cười là ngẫu hứng theo nhân vật, không đếm số へ.
- SFX hôn/mút diễn bằng tiếng Việt (ちゅっ→"chụt", ちゅむっ→"chùn chụt", ごくっ→"ực", くっ→"hự", びゅっ→"Phụt"): GIỮ — quy ước nhất quán trong file, TW cũng diễn nghĩa. ちゅうううっ (2182, 2243) → "chụt" giữ theo quy ước đã chốt.
- 2087 あっっ―――― → "a――――": GIỮ — dấu ―――― đã diễn sự cắt ngang cuối dòng, âm không mất hoàn toàn; audit đã đọc và giữ.
- 2656 ああっ！ → "A!": GIỮ — đây là thán từ ngạc nhiên của Soutetsu trong cảnh chạy định hướng ("Đúng là vậy nhưng――A!"), không phải dòng rên; "A!" tự nhiên trong tiếng Việt. Không áp công thức đếm vào thán từ ngoài H-scene.
- 2522 はううっ → "hauu": GIỮ — は+う×2 = "hauu" đúng.
- 2300 ぎっ！ → "Hự!": GIỮ — tiếng gằn của Soutetsu, đúng.
- 2070 や…… → "Ya……": GIỮ — đã đúng (không mất y). 2071 やああああっ → "Yaaaaa!" (5a) đúng.
- Gasp Ư (1418, 1427, 2201, 2241, 2282, 2759, 2761, 2764, 2767, 2982, 3414, 3421 + 2185, 2266): KHÔNG đụng vào — quy tắc khóa, không xét lại. Không có dòng "Kh" nào bị đổi sang Ư; không có dòng Ư nào bị sửa.
- Các thán từ đồng ý/phủ định (ああ→"À/Ừ/Chà", ううん→"Không phải", うんっ→"Vâng"): GIỮ — không phải rên.

## 5. Cờ (flags)

- Không có dòng nào cần Hieu quyết. Ghi chú duy nhất cho loop parent: xem §3a về file `audit-hibikih6-orienteering-karimono-tomlblock.txt` cũ (51 khóa) — đừng dùng để gộp; và fix 2075 ở đây (6u) đè lên giá trị 5u trong JSON audit.

## 6. Lượt soát 2

- Tổng 2 / tái kiểm chứng 2 / bỏ 0 / sửa 0 (đọc lại từng fix so với JP lần hai; 2075 đếm lại bằng máy: ふ1u + う×5 = 6u; 2082 đối chiếu tiền lệ 2085 + ポーレットh3).
- Kiểm chứng audit: 32 dòng moan của audit đã kiểm chứng lại bằng máy (22 §2c + 8 §2d + 2266/2085) — 31 đúng, 1 sai giá trị (2075). JSON audit 50 mục so với khối TOML trong REVIEW.md của audit: 0 sai lệch (chỉ tomlblock.txt lẻ là khác — bản cũ, xem §3a).
- Kiểm chứng máy (sau sửa): JSON 2 mục (key string, dạng list-of-dicts chuẩn); khối TOML 2 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 2/2; mỗi fix chỉ khác old_vn ở đúng chỗ thay đổi mục tiêu (2075: +1 u và phù→Fua; 2082: a→Ya).

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
2075 = "「Kyafuuuuuun! A! Trong, bụng――\\nBị nhồi nhét――chim――mở rộng ra――Fua」"
2082 = "「Kyuha! Ưm――han! Thế này――Ya――\\nTại sao, lại――cảm thấy――sướng, đến thế――này」"
```

## Kết bài

File 日々姫h6 (667 dòng) là light check: audit đã làm tốt phần moan (22 fa/fu → romaji, 0 dòng "Á" cho họ hya, gasp Ư đầy đủ) — vòng này chỉ tìm thêm **2 dòng đổi**: 2075 sửa giá trị fix của audit về đúng 6u (JSON audit đang sai 5u dù review ghi 6u) và 2082 sửa mất phụ âm y (やっ "a" → "Ya"). Không có dòng gasp Ư hay "Kh" nào bị đụng vào, không có cờ nào cần Hieu quyết. Chi tiết đầy đủ: `moan-hibikih6-orienteering-karimono-wrong.json` (2 mục, khối TOML 2 khóa, 0 sai lệch, jp/tw/old_vn khớp CSV3 tuyệt đối 2/2; lượt soát 2: 2/2/0/0).
