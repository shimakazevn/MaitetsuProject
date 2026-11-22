# Moan-fix REVIEW — 稀咲h2_プライベートルーム (06_Kisaki)

File: `稀咲h2_プライベートルーム.txt.toml` — Kisaki h2, phòng riêng của Soutetsu (dạy thủ dâm → làm tình lần 2).
Cơ sở tổng: **59 file / 1.414 dòng sai (moan)** (đọc từ `moans/ROUTE-MOANS.md` lúc làm — cơ sở giao lúc spawn 58/1.399 đã cũ vì 凪h1 gộp 10:31; đã REBASE).

## Xác minh file

- TOML: `sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b2h2_#U30d7#U30e9#U30a4#U30d9#U30fc#U30c8#U30eb#U30fc#U30e0.txt.toml` — md5 `3faad778393314e55d05226b04768417`, UTF-8 BOM + CRLF, sections `[info] [characters] [character_subs] [script] [selections]`, 323 khóa `[script]`.
- CSV3: 1 bộ duy nhất, 323 dòng, 0 khóa trùng, keys 51–1991. CSV3 ↔ TOML: 165 lệch VN, TẤT CẢ chỉ là TOML-2 làm phẳng `\n` (literal) thành khoảng trắng — CSV3 là chuẩn (đã kiểm chứng, kể cả 1172: CSV3 có literal `\n`, TOML có khoảng trắng).
- Audit của file: `audit-kisakih2-private-room-REVIEW.md`, 24 fix (sweep 9, tự tìm 8, sai nghĩa 3, SFX 4). Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. File KHÔNG có thẻ %l nào — không có gì chờ B19.
- Sweep: 9 entry cho file này trong `sweep-raw-gasp-wrong.json` (raw-tsu 1168/1198/1201/1219; lost-gasp-whole 1389/1390/1391; lost-gasp-trailing 1804/1832) — TẤT CẢ đã được audit nhận nguyên văn. Không có entry sweep nào bị audit bỏ sót.
- Đã đọc: **323/323 dòng** (JP + TW + VN cũ, đối chiếu TOML).

## Kho rên (moan inventory)

- 99 dòng thoại có token rên/thở/gasp (稀咲 + 双鉄H).
- 49 dòng có SFX trong （ ） (monologue).
- 71 dòng có VN diễn rên/SFX.
- Audit đã sửa 12 dòng rên/SFX (moan-vowel 1152/1161, moan-romaji 1154/1218, sfx 1941/1961/1972, sfx-vowel 1960, sweep-raw-tsu 1168/1198/1201/1219) + 9 dòng gasp Ư (lost-gasp 1134/1151/1189/1221, sweep-lost-gasp 1389/1390/1391/1804/1832) + 3 dòng sai nghĩa (không thuộc phạm vi moan).
- **Kết quả moan-fix: 4 dòng đổi** (3 dòng audit bỏ sót + 1 dòng sửa lại đếm nguyên âm của audit).

## §1. 1108 [稀咲] — đếm nguyên âm: ふうっっっ → "fuu" (cũ "fuuu")

- JP: `「だめっ――こ、れっ――んっ――感じ――すぎっ――\nふうっっっ――」`
- TW: `「不行――這個――嗯――太有――感覺了――呼――」`
- VN cũ: `「Không được――cái, này――ưm――cảm giác――quá――\nfuuu――」`
- Fix: `「Không được――cái, này――ưm――cảm giác――quá――\nfuu――」`
- Lý do: công thức độ dài nguyên âm (đếm theo từng mora): ふ = 1u + う ×1 = **2u** → "fuu". Bản cũ viết 3u ("fuuu") — thừa 1u. っっっ KHÔNG thêm nguyên âm (tiền lệ: きゅぅ → "kyuu" không phải "kyuuu"; んきゅううっっ → "Nkyuuu!!!" — っっ không diễn). Các token còn lại giữ: んっ→"ưm", すぎっ→"quá" (っ nhấn mạnh trên từ có nghĩa, không phải gasp).

## §2. 1253 [稀咲] — gasp はっ bị mất: "thì" → "ha"

- JP: `「おしり……はっ――まだっ――準備――んっ――\nちゃんと――出来て――ない、からっ――」`
- TW: `「屁眼……還――還沒有――準備――嗯――好――呢――」`
- VN cũ: `「Mông…… thì――vẫn chưa――chuẩn bị――ưm――\nsẵn sàng――đâu, nên là――」`
- Fix: `「Mông…… ha――vẫn chưa――chuẩn bị――ưm――\nsẵn sàng――đâu, nên là――」`
- Lý do: はっ là một hơi thở/gasp độc lập giữa câu (Kisaki đang thở hổn hển) — VN cũ diễn thành "thì" (tiểu từ chủ đề, không có căn cứ JP), gasp mất hẳn. Quy tắc "không để mất âm" + quy ước của CHÍNH file này: はっ → "ha" ở 6 dòng khác (1130, 1149, 1161, 1205, 1219, 1134 "haƯ"). Tiền lệ: ハチロクh6 — はっ diễn thành "nhà" (từ Việt vô căn cứ) đã bị sửa thành "hà" vì cùng lỗi. Chỉ đổi đúng token này; "vẫn chưa / chuẩn bị / ưm / sẵn sàng / đâu / nên là" giữ nguyên.

## §3. 1267 [稀咲] — hình âm sai: ふぁ → "fua" → "fa"

- JP: `「ボク、ね？　ここは――んっ――感じる、とこ――んっ\n……ふぁ……こうやっ、って……すり、すり――し、て」`
- TW: `「我啊，我的這裡――嗯――就是敏感帶――嗯……哇……只要這樣……輕輕地摩擦――」`
- VN cũ: `「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\n……fua…… chỉ cần làm thế, này…… xoa, xoa――thôi」`
- Fix: `「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\n……fa…… chỉ cần làm thế, này…… xoa, xoa――thôi」`
- Lý do: ふぁ là MỘT mora, phát âm "fa" (ふ + ぁ nhỏ); ふあ mới là hai mora "fua". Bản cũ viết "fua" là thêm một âm tiết ma. Tiền lệ đã chốt: ふかみh2 1025 (ふぁっ→"Fa", ふぁ→"fa", ふぁんっ→"fan"), ふかみh3 (ふぁ→"Fa" ×3), ハチロクh5 1089 (ふぁっ→"Fa"), ハチロクh6 (ふぁっ→"Fa"). File này nhất quán sau fix: ふあっ → "fua" (1167, 1186, 1250 — đúng) vs ふぁ → "fa" (1267).

## §4. 1960 [monologue] — SỬA LẠI đếm nguyên âm của audit: 5u → 6u

- JP: `（きゅうううううんっ！）`
- TW: `（噗！）`
- VN cũ (audit fix): `（Kyuuuuun!）` — 5 chữ u
- Fix: `（Kyuuuuuun!）` — 6 chữ u
- Lý do: JP có **5 chữ う** (đếm máy): きゅ (1u) + う×5 = **6u** theo công thức. Bản audit viết 5u — đếm sai, DÙ review của audit ghi đúng "6 mora-u → 6 chữ u" (§1960 + §8 "1960 (きゅううううう = 6 u)"). Lỗi ở chính chuỗi fix, không phải ở lý luận. VN gốc có 7u, audit sửa thành 5u (sai), moan-fix sửa thành 6u (đúng). ん→"n", っ cuối bỏ trước "!" (đúng quy ước file: 1152 うっ→"u" trước "!").
- old_vn trong JSON là giá trị FIX CỦA AUDIT (không phải VN gốc CSV3 `（Kyuuuuuuun!）` 7u) — khi áp dụng ở đợt thống nhất, dùng bản moan này THAY bản audit cho key 1960 (không áp cả hai).

## Giữ nguyên — các dòng rên đã xét (không đổi)

**Fix rên/SFX của audit — giữ 11/12 (chỉ sửa 1960):**
- 1152 ひゃあうっ → "Hyaa u!" (ひゃあ = 2 a đúng; うっ→"u", っ ngầm trước "!").
- 1154 ひゃうっ → "Hyau!?" (ひゃ→Hya, う→u); あっ→"A" giữ (quy ước file: あっ→"A"/"a", audit giữ ở 1154 + 1189).
- 1161 ふきゅうっ → "Fu kyuu" (きゅう = 2u đúng) + うっ → "ưƯ" (っ cuối dòng tuyệt đối, không dấu câu — đúng ranh giới gasp).
- 1168/1198/1201/1219 sweep raw-tsu → Ư (đúng sweep, đã kiểm chứng từng entry).
- 1218 んひゅっ → "Nhyu" (đúng quy tắc 3b).
- 1941 （くちゅっ） → "（Chụt）" (TW 咕啾).
- 1961 （ぐっ） → "（Gừ）" (xem cờ F5).
- 1972 （ふみゅ――しこっ――こしゅっ――もみゅっ） → "（Giẫm――tuốt――cọ――nắn）".

**9 dòng gasp Ư của audit — KHÔNG xem lại (quy tắc khóa):** 1134, 1151, 1189, 1221 (lost-gasp), 1389, 1390, 1391, 1804, 1832 (sweep-lost-gasp).

**Các dòng khác đã xét, giữ nguyên:**
- ひゃ/ひゅ/きゃ → romaji đúng hết: 1153 "Kya!? Hya――", 1149 "Hya――ha――a――", 1168 "Hyu a――" (quy tắc 3b); không còn dòng ひあ/ぷぁ nào trong file (kiểm cơ học: 0 dòng).
- ふあっ → "fua" đúng ở 1167, 1186, 1250 (ふあ = 2 mora).
- 1158 "Fufu", 1160 "Fufu" — cười là cười, không phải rên.
- 1199 むちゅっ → "mu chu" giữ (tiền lệ: "mu chu" cho むちゅっ đã giữ ở file khác — tách 2 nhịp theo từng mora, nhất quán trong file, không ngượng; khác trường hợp むちゅっ→"chụt" mất む ở file kia).
- 1250 ちゅぷっ → "chu pu" giữ (ぷ là âm bật hơi, đã diễn trọn tiếng "pop"; khác ちゅっ→"chụt" vì ちゅ kết thúc bằng nguyên âm nên っ cần "t").
- 1948 （ちぷっ――ちゅっ――ちゅくっ――ちぷっ） → "（Chụt――chụt――chụt――chụt）" giữ (quy ước hôn của file: mọi tiếng hôn → "chụt").
- 1950 （ちゅるんっ！） → "（Chu run!）" giữ (ちゅ→Chu, るん→run).
- 905/910/911/1177 っ đứng riêng → "Ưm"/"ưm" giữ (quy ước file: っ độc lập = tiếng nghẹn "Ưm"; TW 唔/呼 ủng hộ).
- 1181 「っ」 → "Ưm" giữ (TW 唔).
- 1207/1227/1233 ああ → "Ừm" giữ (thán từ đồng ý, TW 嗯 đồng ý).
- 1210 ふぉん/ふぅん → "Hừm", 1172 ふーん → "Hừm", 1236/1237 ふむ → "Hừm" — tiếng nghĩ ngợi, giữ.
- 1130 いっ (くらいっ) → bỏ っ giữ (っ nhấn mạnh trên từ có nghĩa くらい, không phải gasp); 1214 そっかっ, 1223 双鉄っ, 1238/1344 tên gọi + っ → bỏ っ giữ (nhấn mạnh, không phải gasp).
- 912 「っ――あ――…………うむ。」 → "A――ờ――………… ừm." GIỮ (xem cờ F2).
- SFX diễn bằng từ Việt giữ nguyên (xem cờ F1 về độ dài): 1931/1932/1933/1934/1935/1936 "Phập", 1944/1955/1957/1959 "Phụt", 1962 "Ép/Tuốt", 1963 "Siết chặt!", 1965 "Kẹp chặt!", 1971 "Tuốt", 1973 "Bóp/cọ/bịch/xoáy", 1975 "Bóp chặt!!", 1976 "Giẫm!", 1978 "Tách", 1979 "Bật ra!", 1980 "Bóp chặt!", 1982 "Vuốt/chạm", 1983 "Cọ cọ/trượt", 1984 "Cọ", 1985 "Tuốt mạnh!", 1987 "Thắt lại", 1989 "Đạp/tuốt/miết/nắn", 1990 "Đạp nhẹ", 1991 "Xoáy/Thúc/Bịch/Bịch", 1926 "Lột nhẹ", 1928 "Tuột", 1937 "Phập!", 1938 "Phập――!", 1939 "Phập! Phập! Bịch! Phập", 1940 "Phập!!!", 1942 "Gừ! / Kyun!", 1945 "Trơn tuột", 1947/1969 "Bịch".
- 3 dòng sai nghĩa của audit (1259, 1616, 1853) — KHÔNG thuộc phạm vi moan, không chạm.

## Cờ cho đợt thống nhất

- **F1 — Độ dài SFX diễn bằng từ Việt (câu hỏi mở toàn dự án, giống lr_日々姫h2 F1–F2, 凪h1):** các SFX dài trong JP bị diễn thành từ Việt ngắn, độ dài mất hẳn: 1932 （ずるうううううううっ）→"phập", 1933 （ずぶううううっ）→"Phập!", 1934 （ずぶううううううううううっ）→"Phập!!", 1935 （ずるうううううっっっ）→"Phập――", 1936 （ずるうううううううっ）→"Phập!!!", 1955 （びゅるるるるうぅぅっ）→"Phụt!!!", 1963 （きゅううううっ）→"Siết chặt!", 1942 （ぐううっ）→"Gừ!", 1944 （びゅうっ）→"Phụt!". Đợt thống nhất quyết: giữ từ Việt + dấu câu (!/――) hay chuyển sang romaji có độ dài (vd. "Zubuuuu…"). KHÔNG đổi trong bản này.
- **F2 — 912 っ đầu dòng (glottal attack trên あ):** JP 「っ――あ――…………うむ。」, VN "A――ờ――………… ừm." — っ đầu dòng mất hẳn trong VN. GIỮ NGUYÊN vì: (a) audit đã tự tìm 8 gasp mà cố tình bỏ qua dòng này; (b) TW cũng bỏ (――啊); (c) っ ở đây là đòn tấn công thanh môn vào nguyên âm あ tiếp sau, không phải gasp độc lập (khác 905/910/911/1177 là っ đứng riêng → "Ưm"). Nếu ranh giới gasp được mở rộng cho っ đầu dòng trước nguyên âm thì xem lại.
- **F3 — 1199 "mu chu" vs "mu chut":** giữ "mu chu" theo tiền lệ; đợt thống nhất có thể chuẩn hóa đuôi họ ちゅ ("chụt" vs "chu").
- **F4 — Cụm đại từ vợ chồng Soutetsu↔Kisaki:** audit đã cờ (§5/§7, 58 dòng) — theo quyết định 19:45 + 03:32, quét ở đợt thống nhất. Không phải vấn đề moan.
- **F5 — 1961 ぐっ → "Gừ" vs "Thúc":** ghi chú của chính audit — "Gừ" vì ぐっ đứng giữa các tiếng siết (1960/1962/1963); "Thúc" là dạng cho ngữ cảnh đâm/thúc (1991). Đợt thống nhất quyết nếu Hieu muốn đổi.

## §5. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 4 giá trị fix đối chiếu từng JP (lượt soát 2 đầy đủ, không chỉ parse-check):

- **Tổng: 4 / soát lại: 4 / bỏ: 0 / sửa: 0.**
- Đếm nguyên âm đã kiểm tra lại bằng script: 1108 (ふう = ふ1u + う1u = 2u → "fuu"), 1267 (ふぁ = 1 mora → "fa"), 1960 (きゅ1u + う×5 = 6u → "Kyuuuuuun").
- 1253: đối chiếu vị trí token — "ha" thay đúng chỗ はっ, không chạm token nào khác (diff cơ học: old vs fix chỉ khác "thì"→"ha").
- Cơ sở tổng đã tự kiểm chứng với `moans/ROUTE-MOANS.md`: **59 file / 1.414 dòng** — khớp với cơ sở dùng trong snippet (không phải cơ sở 58/1.399 lúc spawn).

## Khối TOML (đã parse-kiểm chứng: 4 khóa, 0 sai lệch giá trị)

```toml
"1108" = "「Không được――cái, này――ưm――cảm giác――quá――\\nfuu――」"
"1253" = "「Mông…… ha――vẫn chưa――chuẩn bị――ưm――\\nsẵn sàng――đâu, nên là――」"
"1267" = "「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\\n……fa…… chỉ cần làm thế, này…… xoa, xoa――thôi」"
"1960" = "（Kyuuuuuun!）"
```

## Kết bài

File 稀咲h2_プライベートルーム: đọc 323/323 dòng, sửa rên **4 dòng** — 1108 (fuuu→fuu, thừa 1u), 1253 (はっ bị mất → "ha"), 1267 (ふぁ "fua"→"fa", sai hình âm), 1960 (sửa đếm của audit 5u→6u). Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. 9 dòng gasp Ư của audit không xem lại; 3 dòng sai nghĩa không chạm. 5 cờ cho đợt thống nhất (F1 độ dài SFX, F2 912, F3 "mu chu", F4 cụm đại từ Kisaki, F5 ぐっ "Gừ"/"Thúc"). Lượt soát 2: 4/4/0/0. Khối TOML 4 khóa parse đạt, 0 sai lệch.
