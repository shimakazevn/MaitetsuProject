# Moan-fix — lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml

- File: `lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml` (route 01_Hachiroku)
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/01_Hachiroku/lr_#U30cf#U30c1#U30ed#U30afh3_#U901a#U8ca9#U5931#U6557#U3044#U305f#U3057#U307e#U3057#U305f#U306b#U3083#U3093.txt.toml`
- Nội dung: Suzu mua nhầm bộ đồ lót mèo qua mạng, hỏi Soutetsu có trả lại được không; hai người ân ái trong khi Suzu vẫn đóng vai mèo.
- Đã đọc: **331/331 dòng script** (đối chiếu từng dòng với JP + TW theo CSV3), phương pháp đọc ngữ nghĩa toàn bộ.
- Kết quả: **2 dòng sửa (moan)** — đúng như dự kiến: audit của file này làm SAU khi quy tắc romaji có hiệu lực nên đã áp romaji cho fa/fu + họ ひゃ (34 dòng rên trong audit) — đợt moan này chỉ kiểm chứng lại và sửa 2 chỗ audit còn sót/sai.

## §1. Kiểm chứng file

- **TOML md5: `58fde88a83504132e89f5d1d2a0d5159`** (khớp md5 audit), UTF-8 BOM + CRLF, sections `[info] [characters] [character_subs] [script] [selections]` (selections rỗng). Không có bản sao trùng.
- **CSV3: 1 bộ duy nhất**, 331 dòng, 0 key trùng; File column: `translation_toml\01_Hachiroku\lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml`. TOML vs CSV3 khác 173 key — TẤT CẢ chỉ là TOML-2 làm phẳng `\n` literal thành khoảng trắng (theo audit §3).
- **1287 "mojibake" KHÔNG phải lỗi dữ liệu**: CSV3 JP là 「れりゅん！」 (dump hiển thị lỗi do encoding lúc in, không phải dữ liệu hỏng); TW 「溜啾」 khớp. VN "Liếm" giữ nguyên.
- **Cơ sở tổng đã xác minh lại từ `moans/ROUTE-MOANS.md`: 15 file / 341 dòng** (khớp với cơ sở được giao).

## §2. Kiểm kê rên/SFX

Đã đọc hết 331 dòng; 220 dòng chứa token ứng cử viên rên/SFX (っ / （ / họ fa-fu / họ ひゃ / họ ちゅう / cười — kể cả っ trong từ thường như まったく/ちょっと nên con số này là chặn trên, không phải tổng dòng rên). Phân loại theo đếm máy trên JP:

| Loại | Số dòng có token | Keys chính |
|---|---|---|
| Họ fa/fu (ふぁ/ふあ/ふぇ/ふや) | 15 | 1199, 1201, 1218, 1219, 1220, 1222, 1223, 1224, 1232, 1261, 1262, 1266, 1271, 1348, 1192 |
| ふにゃ | 4 | 1225, 1227, 1228, 1229 |
| Họ ひゃ/ひゅ/ひあ/きゃ | 16 | 1184, 1188, 1190, 1191, 1192, 1193, 1195, 1196, 1197, 1199, 1201, 1202, 1240, 1275, 1311, 1378 |
| Họ ちゅう/ぢゅう | 36 | 13 dòng thoại (1277–1411) + chuỗi SFX （ ） |
| Cười (ふふっ/うふふ/んふふ) | 4 | 1236, 1297, 1318, 1320 |
| Gasp っ (sweep/audit) | 15 + 1 | 1203, 1204, 1206, 1207, 1248, 1249, 1264, 1273, 1331, 1378, 1385, 1494, 1497, 1642, 1757 (+ 1307 sửa ở đây) |
| SFX trong （ ） (độc thoại) | 53 | 1897–1983 |
| Rên ngắn/thở (はうっ/あっ/んっ/くぁっ…) | ~45 | 860, 1190, 1195, 1202, 1238–1245, 1250–1272, 1301, 1302, 1306, 1312, 1424, 1431, 1448, 1449, 1451, 1481, 1486, 1492, 1956, 1982 |

## §3. Chi tiết từng dòng sửa (2 dòng)

### 3a. 1232 — mất âm ゅ trong はひゅっ (âm sai — wrong-sound)

- Nhân vật: ハチロク (Suzu).
- JP: 「はっ――はひゅっ――ん……ふあっ――あ――あ――あ――あ――ふぁっ」
- TW: 「哈、哈呼、嗯……呼啊、啊、啊、啊、啊……呼啊」
- VN cũ (CSV3): 「Ha——hahu——ưm……hua——a——a——a——a——hua」
- VN audit: 「Ha——hahu——ưm……Fua—— a——a——a——a——Fa」 (audit chỉ sửa 2 token fa/fu, giữ nguyên "hahu")
- **VN mới: 「Ha——hahyu——ưm……Fua—— a——a——a——a——Fa」**
- Lý do: はひゅっ = ha + hyu + っ. "hahu" (ha-hu) làm mất phụ âm lướt ゅ — lỗi mất âm. Cùng một token JP はひゅっ được diễn đúng là "Hahyu" ở key 1240 trong chính file này («はひゅっ！！！» → "Hahyu!!!"). Sửa cho nhất quán nội bộ file + đúng quy tắc "không để mất âm". Chỉ đổi đúng token này so với giá trị audit (parent kiểm chứng trùng audit: mọi token khác giữ nguyên giá trị audit).

### 3b. 1307 — gasp っ thứ hai sau ―― bị mất (gasp)

- Nhân vật: 双鉄 (Soutetsu).
- JP: 「うむっ――っ！　すずっ！　イク、ぞっ！！」
- TW: 「嗯……！鈴！我要，射了！！」
- VN cũ (CSV3): 「Ưm——!　Suzu! Ra, đây!!」
- **VN mới: 「Ưm——Ư! Suzu! Ra, đây!!」**
- Lý do: JP có HAI tiếng っ: うむっ (đã diễn bằng "Ưm") và っ đứng riêng sau ―― (gasp sắc, cuối đoạn 1, chỉ còn dấu "!" theo sau). VN cũ chỉ diễn tiếng đầu — tiếng thứ hai mất hẳn. Đây là mẫu っ――っ mà chính audit của file này đã thêm Ư ở 1642 (弄びっ――っ → "đùa giỡn——Ư!!!!") và 1378 (のっ――っ → "của——Ư!"), và 1385 diễn cả hai っ ("Ư~~~~~~~Ư!!!!") — 1307 là ngoại lệ duy nhất còn thiếu Ư trong file.
- **GHI CHÚ QUAN TRỌNG — sửa này GHI ĐÈ một quyết định giữ nguyên có chủ ý của audit (§4) + phân loại "already-rendered" của sweep** (mục 1307: "VN đã diễn gasp bằng cách khác… không sửa"). Kiểm chứng trực tiếp mục sweep cho thấy phân loại đó là heuristic sai ở đây: "Ưm" chỉ diễn tiếng っ ĐẦU (うむっ), không diễn tiếng っ THỨ HAI sau ――. Quy tắc biên gasp đã khóa (chỉ thêm Ư khi っ mất hẳn) vẫn thỏa: tiếng thứ hai mất hẳn. Parent xác nhận lại lúc gộp — nếu giữ theo audit thì bỏ dòng này.
- Quy ước giá trị sửa: một dòng, khoảng trắng thay chỗ ngắt dòng của CSV3 (chuẩn TOML-2 flatten, như audit key 1112); fix chỉ khác VN cũ ở đúng token Ư thêm vào (+ chỗ `\n`→khoảng trắng chuẩn).

## §4. Xác nhận cờ của audit (đã kiểm chứng, giữ nguyên)

1. **Họ ちゅう — phán đoán bỏ 't' cuối khi JP không có っ (1277/1279/1283/1287): XÁC NHẬN.** Đếm nguyên âm kiểm chứng bằng máy: 1277 ちゅううっ 3u→"chụụụt" + ちゅ～～ 1u→"chụ~~"; 1279 ちゅうう～～ 3u→"chụụụ~~"; 1283 ちゅうう～～ 3u→"chụụụ~~"; 1287 ぢゅううぅ～ 4u→"chụụụụ~". Khớp tiền lệ moan-fix h9 (ちゅううう→"chuuuu", không t) và paulette-h3/lr-h1 (có っ → giữ t).
2. **1224 ふあっっっっ → "Fua!!!!!": XÁC NHẬN.** っ×4 là nhấn mạnh, không phải kéo dài nguyên âm — không thể thành "Fuaaaaa"; dấu !!!!! giữ nhấn. Tiền lệ h7 (っ cuối rơi).
3. **1287 mojibake: KHÔNG PHẢI LỖI** (xem §1 — JP thực là 「れりゅん」).

## §5. Ghi chú giữ nguyên (các diễn rên đã xét là đúng)

- **Audit 34 dòng rên đã kiểm chứng đúng, giữ nguyên**: fa/fu romaji 18 dòng — đếm nguyên âm kiểm chứng bằng máy: 1193 ひゃふうううううううんっ = 1 (ふ) + 7 う = 8u → "Hyafuuuuuuuun" ✓; 1225 ふにゃあああああん = 1 (にゃ) + 5 あ = 6a → "Funyaaaaaan" ✓; 1227 = 1 + 4 あ = 5a → "Funyaaaaaan" ✓; 1229 ふにゃあ = 2a → "Funyaa" ✓; 1269 ぁぁぁっ = 3a → "Aaa" ✓; 1432 んきゅぅう = きゅ+ぅ+う = 3u → "nkyuuu" ✓. Họ ちゅう 13 dòng (đếm đã kiểm ở §4). Cười 4 dòng (1236 "Fufu", 1297 "Nyafufu~~", 1318 "Nfufu", 1320 "Ufufu").
- **Họ ひゃ/ひゅ/ひあ/きゃ đã ở dạng romaji toàn bộ** (Hya/Hyau/Hyafu/Nhyu/Hahyu/Kya) — không còn dòng "Á" nào cho họ này trong dòng rên. Quy tắc 21/11 ~11:55 đã đúng.
- **15 gasp っ của sweep/audit giữ nguyên** (đã kiểm chứng trực tiếp 16 mục sweep: 15 fix áp đúng, 1 already-rendered là 1307 — xem §3b). Không dòng "Kh" nào bị đổi (quy tắc "Kh" khóa giữ nguyên).
- **Rên ngắn La-tinh giữ theo thực hành hiện tại, không thêm Ư**: はうっ→"Hau" (1238/1239), ひゃっ→"Hya", ふあっ→"Fua", ひゃうっ→"Hyau", くぁっ→"Kua", うぁっ→"Ua", あぅっ→"Au", ぅぉっっ→"Uo", んひゅっ→"Nhyu" — khớp quyết parent ở ふかみh2 (はうっ→"Hau" giữ; あっ→"A" giữ) và audit §6.1.
- **Chuỗi SFX miệng "chụt"/"liếm" giữ theo quy ước nội bộ file**: ちゅるっ/ちゅるうっ/じゅるるっ → "chụt"/"chụụt" (1277, 1283, 1288, 1306, 1411, 1220) — る rơi nhưng nhất quán toàn file, audit đã chốt.
- **SFX trong （ ） độc thoại (1897–1983) giữ nguyên**: diễn bằng động từ tiếng Việt ("Phập"/"Siết chặt"/"Ngoáy"/"Xoa nắn"/"Ngậm lấy") + lặp phụ âm đánh dấu độ dài — quy ước audit §2f/§6 đã chốt, moan-fix chưa từng chạm tới dạng này.
- **1370 giữ nguyên (không thêm Ư)**: っ đứng riêng giữa câu (おまえのっ――っ――一番、奥、で) — không phải tuyệt đối-cuối/dòng-đầu theo ranh giới gasp đã khóa; sweep cũng không liệt kê; dấu —— trong VN đã diễn quãng ngắt. Khác với 1307 (っ cuối đoạn).
- **1192 ふやっ→"Fuya" giữ** (đã đúng F); 1225/1227 chỉ sửa phụ âm H→F, đủ số a.

## §6. Cờ cho parent / đợt thống nhất (không tự quyết)

- **F1 — 1307 (xem §3b)**: sửa này ghi đè quyết định giữ nguyên có chủ ý của audit §4 + phân loại already-rendered của sweep. Cần parent chốt lúc gộp (giữ "Ưm——Ư!" hay quay về "Ưm——!").
- **F2 — đếm lặp phụ âm trong SFX （ ）**: các chuỗi độc thoại lặp phụ âm theo cảm tính, lệch ±1–2 so với số う trong JP (1909: 11う→12p "Phậpppppppppppp"; 1966: 5う→7p "Phậppppppp"; 1983: 13う→12p "Phậpppppppppppp"; ngược lại 1905 8う→8t, 1965 10う→10p, 1968 10う→10t đúng). Chưa có quy tắc chốt cho dạng này (công thức đếm nguyên âm không áp cho động từ + lặp phụ âm) — giữ nguyên theo audit, cờ để quyết chung sau.
- **F3 — しゅこんっ hai cách diễn**: "Ngậm lấyyyyy" (1906/1941, ngữ cảnh miệng, TW 再次含住) vs "Nắm chặt" (1945, ngữ cảnh tay, TW 握緊). Cùng một SFX, diễn khác nhau theo ngữ cảnh/TW — audit giữ; không phải lỗi mất âm rên.
- **F4 — ngoài phạm vi moan, KHÔNG sửa**: 1192 lời nói lắp/ngọng của Suzu — りゅっ → "mất" trong "Mãnh liệt quá, hỏng, mất——em——em" (JP 「はげしっ、こわれ、りゅっ――わらくひ――わたくしっ」). Audit giữ; đây là lời ngọng, không phải dòng rên — cờ lại để audit/unification xem.
- **F5 — 1370** (xem §5): っ giữa câu giữ không Ư theo ranh giới gasp đã khóa.

## §7. Lượt soát thứ hai (bắt buộc)

Đọc lại toàn bộ 2 giá trị sửa đối chiếu JP (+TW) sau khi viết xong: **tổng 2 / tái kiểm chứng 2 / loại bỏ 0 / sửa lại 0**.

- 1232: はっ→"Ha" ✓; はひゅっ→"hahyu" ✓ (ha-hyu, đủ ゅ); ん→"ưm" ✓; ふあっ→"Fua" ✓; あ×4→"a"×4 ✓; ふぁっ→"Fa" ✓. Chỉ khác giá trị audit ở đúng token "hahu"→"hahyu".
- 1307: うむっ→"Ưm" ✓; っ (sau ――) →"Ư" ✓ (mới thêm); すずっ→"Suzu" ✓; イク、ぞっ→"Ra, đây" ✓ (giữ nguyên cách diễn bằng từ của VN cũ).
- Kiểm chứng máy: JSON 2 mục dạng chuẩn, khóa string; khối TOML parse được bằng tomllib, **2 khóa, 0 sai lệch giá trị** so với JSON; jp/tw/old_vn khớp CSV3 2/2; diff-sanity: fix 1232 chỉ khác VN cũ ở token "hahu"→"hahyu" + 2 token fa/fu theo giá trị audit ("hua"→"Fua"/"Fa") + `\n`→khoảng trắng chuẩn; fix 1307 chỉ khác VN cũ ở Ư thêm vào + `\n`→khoảng trắng chuẩn.

## §8. Khối TOML (đã kiểm chứng parse — 2 khóa, 0 sai lệch)

```toml
[script]
1232 = "「Ha——hahyu——ưm……Fua—— a——a——a——a——Fa」"
1307 = "「Ưm——Ư! Suzu! Ra, đây!!」"
```

## Kết bài

File lr_ハチロクh3_通販失敗いたしましたにゃん đã đọc hết 331 dòng, **2 dòng sửa moan** — đúng như dự kiến là đợt soát nhẹ (audit đã áp romaji fa/fu + họ ひゃ từ trước): 1232 mất âm ゅ ("hahu"→"hahyu", cùng token diễn đúng "Hahyu" ở 1240) và 1307 gasp っ thứ hai sau ―― bị mất ("Ưm——!"→"Ưm——Ư!", ghi đè quyết định giữ nguyên của audit §4 + phân loại already-rendered của sweep — cần parent chốt lúc gộp). 34 dòng rên của audit, 15 gasp sweep, họ ちゅう (kể cả phán đoán bỏ 't' cuối) và 1224 (っ×4) đều đã kiểm chứng đúng. Không dòng "Kh" nào bị đổi, không còn "Á" cho họ ひゃ. Khối TOML 2 khóa đã kiểm chứng parse, 0 sai lệch. Lượt soát thứ hai: 2/2 tái kiểm chứng, 0 loại bỏ, 0 sửa lại. Tổng cộng sau file này: **16 file / 343 dòng sai (moan)** (cơ sở 15 file / 341 dòng + 2 file này).
