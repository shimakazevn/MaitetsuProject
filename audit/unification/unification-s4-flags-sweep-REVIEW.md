# Unification U15b — §4 flags sweep: các cờ tồn đọng chưa quyết — REVIEW

## 1. Phạm vi

Batch U15b quét TẤT CẢ các cờ tồn đọng của coordinator/worker chưa được quyết (task 22/11 ~13:47). §7 đã HOÀN TẤT (U14a/b/c gộp, chuỗi **160 mục / 2.731 dòng**). Hai batch song song: U15a (§4 gloss + moan leftovers) và U16 (P1/P5) — trùng (file,key) nào nghi ngờ được ghi ở §2/Kết bài; coordinator ghép khi gộp.

**Kết quả: 436 dòng sửa mới** (E2-Teio 8, F2 11, F3 7, F5 310, O7 37, O25 3, O46 1, M7 1, M10 1, Munakata 48, F-P4-1 9). **0 dòng GHÉP** với batch đã gộp (mọi old_vn đều lấy từ map hiện tại; không dòng nào trong đợt này trùng (file,key) với batch đang chạy — kiểm chứng ở §3). **Sau 07:28: 21 dòng trùng U15a — xem Phụ lục cuối REVIEW.** Chuỗi tổng sau đợt này: **xem snippet** (cơ sở 160 mục / 2.731 dòng + đợt U15b — xem `unification-snippet-s4-flags-sweep.md`).

Nguồn old_vn của 436 dòng sửa: audit 7, csv3 91, moan 178, toml2-characters 1, unif 159.

## 2. Quyết định theo mục (bằng chứng + lý do)

### Mục 1 — 帝央 → “Teio” (8 dòng)

Census JP chứa 帝央: 19 dòng — “Teio” 12, “Teiou” 5, “Trung tâm Hoàng gia” 2. Furigana ていおう → Teiō → “Teio” (ō→o, cùng quy ước T69 “Khách sạn Teio” đã chốt và T68 “Showa”). Một dòng VN-side nữa: ハチロク06 2166, JP katakana 「サッポロ、センダイ、テイオー、ナゴヤ、オーサカ、キョート、ヒロシマ、カゴシマ！」 → “Teio” (cùng tên địa danh, romaji Teiō→Teio, khớp các tên thành phố khác dạng romaji giản lược). ハチロク04 1802: 帝央 nằm NGOÀI tag %l機関区 gloss “kho đầu máy” nên chỉ đổi phần ngoài tag. “Ousaka” ở ハチロク06 2485 giữ nguyên (không thuộc mục này). Kiểm tra lần 2 (22/11): 1570 từng ghi “khởi hành từ Teiou” → “từ Teio” (làm mất “khởi hành”); JP 帝央を出て = “rời khỏi Teio” nên GIỮ “khởi hành” — fix đúng là “khởi hành từ Teio”.

### Mục 2 — U13b F1: T75 KHÔNG mở rộng (0 dòng)

5 dòng ちゅず/ちゅく/ちゅりゅ (ハチロクh9 2031, lr_日々姫h2 1037/1652, lr_稀咲ポーレットh1 2534, 真闇h3 2357) GIỮ romaji. Census 51 dòng JP chứa các token này (54 token, trừ 3 dòng narration): họ “chụt” 33, romaji 16, VN khác 5 — khẳng định của worker U13b “đa số là romaji” là SAI, nhưng đa số “chụt” (61%) yếu so với đa số áp đảo của T75; và (a) phân biệt âm vị: coda T75 đã liệt là môi (む/る/ろ/ぷ/ぱ/ぶ, tiếng “chụt” bật môi) vs ず xát / く vòm / りゅ lướt — cùng logic phân biệt âm vị khi coordinator tách れろ ra khỏi T77; (b) 1652/2534 nằm trong dòng （ ） toàn romaji, 2031 trong dòng toàn romaji — đổi một token sẽ trộn hai hệ (M14 hệ theo file); (c) mở rộng toàn project ≈ 21 dòng, vượt phạm vi 5 dòng đã nêu, trong khi chỉ lật 5 dòng sẽ tạo mâu thuẫn mới với 7 dòng romaji U13b đã giữ (1213/1053/1573/1585/1688/2537/2547: “chuzu”/“churyu”/“chuku”/“chu ku”). 5 dòng này cũng NGOÀI phạm vi F5 (nguồn csv3/audit, không phải giá trị unif/moan đã gộp) nên romaji thường giữ nguyên.

### Mục 3 — U13b F2: T75-miss (9 dòng + 2 extra)

Công thức T75 (kiểm chứng với tiền lệ U13b): ちゅ + nう → “chụ” + ụ×(1+n) (ちゅうっ→“chụụt”, ちゅううっ→“chụụụt”, ちゅううううっ→“chụụụụụt”, ちゅううううううっ→“chụụụụụụụt” 7 ụ); ちゅむっ/ちゅぱっ/ちゅぶっ/ちゅぼっ/ちゅばっ→“chụt” (tiền lệ: 稀咲h1 1053/1069 ちゅばっ→“chụt”; ハチロクh9 2145/2182 ちゅぼっ→“chụt”). Cả 9 dòng đều là miss thật. Extra tìm được trong lúc làm F5 (cùng quy tắc T75/T77, không mơ hồ): lr_れいなh1 1251 (ちゅるっ→“chụt”, ちゅむ→“chụt”), lr_ハチロクh1 1252 (ちゅむっ→“chụt”, ちゅうっ→“chụụt”, れるっ→“rộp”). lr_れいなh1 1266: “Chụt mút!” → “Chụt!” (một token = một cách diễn; “mút” thừa — độ tin cậy trung bình, ghi rõ lý do). lr_稀咲ポーレットh1 1589: giữ はむっ→“Ha mu”, くぷっ→“ku pu”, れろっ→“rê ro”, れりゅうっ→“rê ryu u” (lãnh thổ M68 — U12a có thể đã bỏ sót; CẮM CỜ cho coordinator/U15a, không sửa ở đây). lr_れいなh1 1271: CẮM CỜ (không sửa): ちゅずず～っ (“Chu mút t~”, phụ thuộc F1) và ずりゅっ (“Chu mút”, không phải token ちゅ); れろおっ “Liếm m” là lãnh thổ M68.

### Mục 4 — U13b F3: T77-miss (4 dòng + 3 extra; 1 KEEP)

Công thức T77 (kiểm chứng với tiền lệ U13b, vd. れるうっ→“rộộp”, れるうううっ→“rộộộộp”, れるーーーっっ→“rộộộộp”): r + ộ×(1 + số う/ぅ/ー) + p; れるっ→“rộp”. 4/5 dòng là miss thật. **真闇h3 2336 KEEP “ru”**: るっ ở cuối chuỗi trượt 「ちゅる、るう、るっ」 (TW 啾嚕、嚕、嚕) — là mora cuối của MỘT âm trượt kéo dài qua các mora (ちゅる→“chụt” U13b đã đổi); đổi mora cuối thành “rộp” sẽ chẻ một âm thành hai cách diễn. (Đối chiếu 2043, nơi るっ→“rộp” trong chuỗi miệng romaji れるっ――るっ――るうううっ.) Extra tìm được trong lúc làm F5: lr_凪h1 1213, ハチロクh9 1358, ハチロクh9 2136 — れるっ trong dòng moan-src vẫn “reru”/“rero” → “rộp”.

### Mục 5 — U13b F4: るっ ở lr_日々姫h2 1033 — XÁC NHẬN LIẾM (0 dòng)

JP 「れるっ――じゅぶっ――じゅむっ――るっ――ぶっ――\n『ひゃばば、ばふぃっ』、ぷぁっ――ぷっ――じゅるっ」; chuỗi mở bằng れるっ (liếm) rồi じゅぶっ/じゅむっ (miệng); TW toàn âm miệng (啾嚕/啾噗); ぶっ kế sau mơ hồ, TW không cho nghĩa thrust; audit/moan cũ đã là “liếm” cho るっ. Giữ “rộp” của U13b.

### Mục 6 — U13b F5: viết hoa token romaji SFX (310 dòng, gồm 2 dòng F5b)

Quyết coordinator 22/11 ~12:50: token romaji SFX viết hoa ở MỌI vị trí (đầu dòng và giữa dòng) trong fix MỚI. Phạm vi GIỚI HẠN: (a) token romaji còn giữ trong dòng U13b đã đổi, (b) lr_ニイロクh 1322/1387 “fua”→“Fua”, (c) token romaji thường trong giá trị fix unif/moan ĐÃ GỘP (liệt kê bằng script chỉ từ các wrong.json đã gộp — KHÔNG quét CSV3/TOML thô). Liệt kê: 4.083 dòng có giá trị hiện tại nguồn unif/moan; token toàn-chữ-thường-ASCII: 486 loại, 6.516 lần xuất hiện; dòng có ≥1 token ỨNG CỬ: **390 dòng** (106 dòng U13b đã đổi). Mỗi token quyết tay theo từng dòng: token độc lập → viết hoa; nửa của cách diễn TÁCH (M15: “Ưm kyu”, “ưm fu”, “E mu”, “Chu mút”, “rê ryu”, “Zu ryuu…”, tên tách “Hibi, ki”/“Miku, ro”, từ lóng “Hôu-hê-hu”, chant âm tiết “ho he fu”/“Hyo ha hyo ho”, từ VN “phu quân”/“chu đáo”/“rủi ro”/“êm ru”, tên riêng “San’yo”/“Tororyu-yu”, từ mượn “fan”) → giữ thường. **Token một chữ cái “a” KHÔNG quyết** (745 lần, chủ yếu nửa tách M17 “Fu, a”, “Ha, na, o” — M17 giữ “a” thường có chủ ý; cần phân loại từng lần xuất hiện — xem cờ ở Kết bài). Ngoài 390 dòng dump, rà soát chéo danh sách token còn sót 9 token romaji do danh sách CAND cứng bỏ sót: “huu” (ハチロクh9 2053), “aaaaaaaan” (lr_凪ふかみh1 1677), “fuuuuu” (れいなh2 1064), “ihi” (真闇h2 1058), “iiiiiiiii” (ハチロクh4 1000), “nhehe” (lr_凪h2 1229), “amu” (lr_日々姫h2 1041 ×2, 991, 真闇h3 2288/2363 — các lần còn lại là mảnh tách, giữ thường). “chaaan”/“chaan”/“chann” (真闇h3 2211/2306/2472) là đuôi kéo dài của tên “Sou-chan” — KHÔNG viết hoa. “am” (ポーレット09 1837, lr稀咲追加02 1153) = “am hiểu”, “lu” (真闇01 1335) = “lu mờ” — từ VN, không viết hoa. **Kiểm tra lần 2 (22/11) phát hiện sót do “ha”/“hu”/“gao” nằm trong tập loại trừ VN của enum5d:** 36 dòng “ha”→“Ha” (は/はっ độc lập, đọc tay từng dòng JP; 24 dòng mới + 12 dòng sửa thêm — gồm cả 3 dòng thán từ đối thoại 1598/1887/2449, theo tiền lệ “ah”→“Ah” cho あっ trong cùng dòng 1887; KHÔNG đổi “ha” là từ VN (“đúng ha”, “êm ru luôn ha”), mảnh tách (“ha ư” = はうっ ở 1288, “ha hyu” = はひゅっ ở 2201), chant (“ho he phu ha fa”, “Hyo ha hyo ho”), hay “Anh ha” ở lr_凪h1 1195 (JP không có は)); “hu”→“Hu” ở ハチロクh9 2053 (lần đầu, ふっ độc lập; lần 2 trong chant “hoo he hu” và lần 3 trong tách “re hu” giữ thường; “U hu hu” ở ハチロク12 1746 là một token cười うふふぅ tách làm ba — giữ thường; “Hôu-hê-hu” lisp giữ nguyên); “gao”→“Gao” ở lr_凪h2 1190/1245 (がお độc lập; “gắt gao” ở ハチロク14 3747 là từ VN — giữ); “amu”→“Amu” ở lr_日々姫h2 1038 (あむっ độc lập, sót trong lần rà đầu); “hi-hamu” ở lr_凪h2 1290 KHÔNG viết hoa “hamu” (ひーはむ là MỘT token JP, “hamu” là mảnh tách — giống quy tắc M15). Tổng F5 sau kiểm tra lần 2: **310 dòng** (285 + 25 dòng mới).

### Mục 7 — U14a F-O7-1: Soutetsu→Olivy + →Hachiroku “cô” → “em” (37 dòng)

Tiền lệ O1 (Paulette): “cô” thống nhất thành “em” trong MỌI ngữ cảnh vì “cô” xuất hiện cả trong cảnh thân mật (register theo giai đoạn chương, không theo công việc/thân mật). Tiền lệ O9 (Kisaki→Hibiki “cô” GIỮ): register tranh luận công khai có chủ ý, 4/4 dòng trong một file. Tiền lệ O10 (Hachiroku “Tôi” GIỮ): chuyển register trong một cảnh, JP わたくし. **Olivy:** nhóm chỉ-Olivy toàn project: “em” 28 vs “cô” 8; trong ハチロク05 cả hai dạng cùng một file (9 “em” vs 2 “cô”); ハチロク13 1833 có “cô” trong cảnh THƯỜNG/nghịch (Olivy cười, đùa “マッタクモッテ”) — phá thuyết “cô = register công việc”. → thống nhất “em”. 24 dòng ứng cử đọc tay từng dòng: 16 sửa, 6 giữ (danh từ “cô giáo Olivy”, ngôi ba “cô ấy”/“cô ta”), 1 chuyển sang Hachiroku (2039), 1 chuyển sang Nagi (2510 — người nghe là NAGI, prev speaker 凪 2458 than làm thêm giờ; Soutetsu là “anh” với Nagi nên Nagi là “em”). **Hachiroku:** 30 dòng ứng cử đọc tay: 20 sửa, 9 giữ (danh từ/ngôi ba: “cô dâu”, “cô mèo Xiêm”, “quý cô”, “cô phục vụ”, “hai cô em gái”, “cô ta”), 1 Navi (共通02 2550 — CẮM CỜ, xem dưới). Số đếm U6 nói 25+2039+1623=27; đếm lại được 29 dòng nhóm + 2039 = 30; sau khi đọc: 20 dòng Soutetsu→Hachiroku “cô” thật — ghi rõ chênh lệch. Hỗ trợ: Soutetsu→Hachiroku “em” ~408 dòng (nhóm chỉ-Hachiroku) vs “cô” 29; audit Common 05 đã đổi 2 “cô”→“em” (2440/2727). CẢNH BÁO phương pháp: prev-speaker và nhóm-kề đều KHÔNG đáng tin để xác định người nghe (vd. 1775 là Soutetsu→Hachiroku “em” nhưng phân loại nhầm thành Olivy; 2986 prev speaker là Hachiroku nhưng người nghe là Olivy) — chỉ đọc tay từng dòng mới quyết được.

### Mục 8 — U14a F-O10-1: GHI CHÚ, không lật (0 dòng)

Nếu Hieu muốn Hachiroku “em” với Soutetsu trong MỌI ngữ cảnh, Grand 02 1785/1589 sẽ lật thành “em”. Quyết O10 (U14a): GIỮ “Tôi” — 1195 “em” (nài nỉ, không わたくし) vs 1785/1589 “Tôi” (xin lỗi trang trọng + từ biệt, JP mở bằng わたくし) — chuyển register có chủ ý trong một cảnh. Chỉ ghi lại lựa chọn + bằng chứng, 0 dòng.

### Mục 9 — U14a F-O13-1: GHI CHÚ điều kiện đảo (0 dòng)

O13-2006 đảo lại thành “anh” NẾU bàn tay trong mơ được xác nhận là của Michiko. O13: 1158 “Anh”→“Tôi” (nhóm lẫn Hachiroku+Hibiki, P17) và 2006 “anh”→“tôi” (cảnh mơ, bàn tay chưa xác định — “anh” chỉ đúng nếu tay là Michiko; phần còn lại của đoạn mơ dùng “tôi”/“mình”; độ tin cậy trung bình-cao).

### Mục 10 — U14b F-O25-1: lr h1 1616/1687/1737 → “tớ”/“cậu” (3 dòng)

Cùng vi phạm P9 như các dòng O25 đã sửa (Fukami tự xưng “Em” / Fukami→Nagi “em”). O25 (U14b): 1620 “Chị”→“Tớ”, 1672 “Chị”→“Tớ” + “em”→“cậu”, 1744 “em”→“cậu” + “chị”→“tớ” (chuẩn trong file là 1746 “tớ”/“cậu”). 1616 ghép thêm F5 “ufufu”→“Ufufu” trong cùng fix.

### Mục 11 — U14b F-O33-1: GHI CHÚ, giữ nguyên (0 dòng)

lrれいな追加02 1635 “Còn tôi là chồng của Reina mà.” — nhóm lẫn (Kisaki có mặt với vai trò giáo viên), “tôi” biện hộ được theo P17; giữ nguyên.

### Mục 12 — U14c O52: れいな01 2415 — PARK, JP không khôi phục được (0 dòng)

Ô JP hỏng trong CSV3 (chứa text VN “Bước đi xạo xạc.”), TW là một dòng khác (tin nhà máy điện, cảm ơn Reina). KIỂM TRA NGUỒN đã làm: comment `# JP:` trong TOML-2 cho 2415 CŨNG là “Bước đi xạo xạc.” (hỏng từ lúc dịch). TW tương ứng tìm được: TW đó thuộc về れいな01 1917 (JP 「発電所が再稼働可能かもしれんというのは、朗報だな。れいなは、よく気づいてくれた」) — ô TW bị copy từ 1917 (lệch hàng). Section=monologue; dòng kề 2414 (độc thoại Soutetsu) và 2431 (mặt Paulette). Không có bản .scn gốc trong `~/workspace/maitetsu-pilot/sources/` (chỉ có csv3, tips, toml2). JP thật không khôi phục được từ nguồn nào hiện có — cần .scn gốc hoặc kiểm tra trong game (kiểu B19). Bản thân list đã ghi “không tính vào số sai”.

### Mục 13 — U14c O46: KHÔNG tái hiện được, park cho Hieu (0 dòng) + 1 dòng “Olive”

List §7 O46: “ハチロク15a: ký hiệu ‘N’ 20 dòng + ‘n’ (1893/2232 ‘n’)”, nguồn trích ROUTE-AUDIT.md (ハチロク15a:874) — nhưng đoạn ROUTE-AUDIT ハチロク15a (dòng 868–874) KHÔNG hề nhắc ‘N’; bản thân trích nguồn đã sai/ghi nhầm. Thử tái hiện đều thất bại: ‘N’ độc lập = 0 dòng trong ハチロク15a; ‘n’ độc lập = 6 dòng (không phải 20); 1893 hiện là 「Ưm……」 và 2232 là 「Ngài, Soutetsu——cũng——đang đợi—— Oli, vy——đó——」 — KHÔNG dòng nào chứa ‘n’ độc lập; token kiểu M15 có N = 0 (5 dòng “N…” tìm được đều là từ VN “Ngay” ×4 và “Nghe” ×1); dòng JP-ん mà VN có từ N = 30 (gồm tên Navi/Nagi/Niiroku); token n thường = 32 (từ VN). Park cho Hieu với đầy đủ bản ghi tái hiện. **Tìm ngoài phạm vi trong cùng file: ハチロク15a 2345 = “Olive” — sửa thành “Olivy” (1 dòng).** TOML-2 [characters]: `# JP: オリヴィ / 2345 = “Olive”`. T46: [characters] ‘Olive’ → “Olivy” (U10 F36 đã sửa 15b 1908/2063, Grand09 2180/2466, ハチロク02 2823/3034). Dòng [characters] KHÔNG có trong CSV3 — theo đúng định dạng JSON F36 của U10: jp=“オリヴィ”, tw=“” (rỗng). **CỜ cho coordinator: T46 chưa đầy đủ toàn project.** Grep TOML-2: 37 dòng đúng “Olive” + 47 dòng chứa “Olive” (gồm dạng ghép “Olive & Hibiki”, “Hibiki & Olive”, “Hachiroku & Olive”, “Olive & Nagi”); F36 mới sửa 6. ~41 lần “Olive” còn lại rải nhiều file — cần đợt quét hoàn thiện T46 (NGOÀI phạm vi đợt này, trừ 2345).

### Mục 14 — U14c O48: KHÔNG tái hiện được, park cho Hieu (0 dòng)

List §7 O48: “Common 09: Michiko tự xưng ‘em’ 23 vs ‘chị’ 15 (2054)”. Tái hiện: key 2054 KHÔNG tồn tại trong 共通09 (nó tồn tại trong 共通15_回り始める動輪: Michiko 「ここだよ。そーちゃん」 → “Em ở đây nè. Sou-chan.” — nhãn file của list sai); dòng Michiko ở Common 09 = 36, tự xưng “em” = 2 (2138, 2721), “con” = 1 (2287, với bố mẹ), KHÔNG có “chị” (khớp U14c); 共通15 dòng Michiko = 11, “em” 1, “chị” 0; toàn project Michiko = 237 dòng, tự xưng “em” 27, “chị” 8. Số 23/15 không khớp phạm vi nào đã thử. Park với bản ghi tái hiện. Lưu ý: toàn project Michiko tự xưng “em” 27 vs “chị” 8 có thể hỗ trợ một mục đại từ-Michiko trong tương lai, nhưng O48 như đã nêu thì không tái hiện được.

### Mục 15 — U10b F2/F3 (phạm vi M7/M10): 2 dòng

**M7** (U12a REVIEW §3.1): “token đối thoại H-scene → ‘Ku’. Giữ ‘Hự’ trong 4 file quy ước (lr_ふかみh2, 日々姫h1, lrれいな追加h, ハチロクh2). 5 dòng ‘Hự’ lẻ → ‘Ku’ (凪ふかみh1 1232, lr_ふかみh1 1469, lr_凪h1 1190, ポーレットh6 851, 日々姫h4 1028). Giữ ‘kư’ (lr_稀咲h1) và cụm động từ ‘Ngoáy’/‘Thúc’ (kể cả ハチロクh3 1815). Đối thoại non-H giữ ‘Ư’. （ ） くっ → ‘Ư’.” Cờ F1 của U12a: **59 dòng đối thoại nữa** có くっ độc lập diễn “Hự”/“hự” ngoài 4 file quy ước và 5 dòng đã nêu — “Quy tắc M7 như được viết sẽ đổi hết 59 dòng này, nhưng chỉ 5 dòng được nêu tên. KHÔNG tự đổi — chờ quyết follow-up của coordinator.” **ポーレットh8 2241: CÓ, M7 bao phủ — sửa thành “Ku”.** JP 「はきゅっ！？ くっ――ふうううううっ」 (đối thoại H-scene Paulette, ngữ cảnh thrust, dòng kề là độc thoại thrust); ポーレットh8 không phải file quy ước; tiền lệ M7 gồm くっ theo sau token thở (真闇h1 1059 「くっ――ふっ――」→“Ku——phư——”; ハチロクh9 2289 くっ――はぁ――→“Ku——haa”). Ghép thêm F5 “phuuuuuu”→“Phuuuuuu”. ~58 dòng “Hự” còn lại trong cờ F1 của U12a vẫn chờ quyết coordinator — CẮM CỜ, không tự mở rộng. **M10** (U12a REVIEW): “ふぇ/ふえ: token trong chuỗi rên → ‘Fue’; thán từ ngạc nhiên độc lập (TW 哎/咦, theo sau là câu nhận ra/phủ nhận/hỏi) → ‘Hể?’ (5 dòng: 凪h1 1090, ふかみh1 993, れいなh3 1026, れいなh4 1897, lr_稀咲h1 992 — 992 ĐẢO NGƯỢC fix moan ‘Fue!?’); kéo dài (ふぇぇ/ふえぇ) → giữ ‘Phuê…’ (1547, 2038, 2170); reina-h3 1133 giữ ‘Hả?’.” 5 tiền lệ đều là cả dòng ふえ độc lập hoặc ふえ + câu nhận ra/phủ nhận/hỏi. **ポーレットh8 2185: CÓ, M10 bao phủ — sửa thành “Hể!?”.** Cả dòng 「ふえっ！？」, TW 「哎！？」, dòng kề 2183/2184/2187 đều là Paulette ngạc nhiên — giống hệt 1090/993. Lưu ý: CSV3-VN của 2185 là VN của một dòng KHÁC (độc thoại 3183) — lệch hàng; moan CUR là “Fue!?”. **Mikuro 1708: GIỮ “Fue!?”.** ふえっ mở đầu chuỗi rên (またっ──みくろっ！ またっ！ だって！ ぼっきっ！ — lặp lại hưng phấn về việc ra nữa, TW xác nhận “又要洩了”), không phải ngạc nhiên độc lập. Quy tắc M10-1 (token trong chuỗi rên → “Fue”). **Mikuro 1758: GIỮ “Fue!?”.** ふえっ là token CUỐI của chuỗi rên (ひゅあっ！？ あ──あ……ふえっ！？), trong dòng rên H-scene, không phải ngạc nhiên độc lập. CUR đã là “Fue” hoa (U10b F5 follow-up khôi phục giá trị CSV3).

### Mục 16 — 55 dòng Munakata “tôi” (không 俺 rõ): 48 sửa, 1 giữ

**Đếm lại: 49 dòng, KHÔNG phải 55** (U9 đếm thừa 6; đếm lại có chuẩn hoá NFC, biến thể Character — chỉ ‘宗方’ và ‘車椅子の方’ — và tập stale đều không thêm dòng nào). Phân bố: ハチロク12: 20, ハチロク04: 12, ハチロク15b: 7, ハチロク15a: 5, 凪ふかみ08a: 3, ハチロク02: 2. Cả 13 key ví dụ của U9 đều nằm trong 49. Bằng chứng cho “tao”: 24 dòng “tao” đã gộp (P15: 18 dòng 俺/オレ/おれ trên 5 file; O61: 6 dòng ở ハチロク16 với dòng kề có 俺 rõ xen kẽ; TW xác nhận ngôi nhất 我 cả 6 dòng); lập luận hình thức của O61: “Munakata dùng 俺 cả trong câu trang trọng (ハチロク12 1708) nên tính trang trọng không đổi được đại từ”; **tiền lệ quyết định ハチロク12 2143 (fix unif đã gộp):** JP 「俺――私には、どうにも、夢物語にしか聞こえなくなる」 — Munakata mở đầu bằng 俺 rồi tự sửa thành 私 giữa câu, và fix đã gộp diễn CẢ HAI thành “tao” (“với tao—— với tao”). Vậy 私 rõ → “tao” luôn. Dòng 俺 theo file: ハチロク12: 6, ハチロク16: 4, ハチロク04: 3, ハチロク15a: 3, ハチロク15b: 2 (tổng 18 = 18 dòng P15; 17 đã “tao”, 1 “OTHER” là ハチロク16 2025 thực ra mở đầu “Tao không phải…” — artifact regex, đã “tao”, không phải ứng cử). Dòng 私: chỉ 2, đều ở ハチロク12: 2143 (đã “tao”) và 1147 (私 rõ → “tao” theo tiền lệ 2143). Không có “chúng tôi” trong 49 dòng. **Quyết: sửa TẤT CẢ 48 dòng tự xưng ngôi nhất của Munakata thành “tao”/“Tao” (giữ hoa/thường, mọi lần xuất hiện trong dòng), KỂ CẢ 5 dòng ở file không có bằng chứng 俺 trong file (凪ふかみ08a 1792/1814/1820 — register thường, TW 我; ハチロク02 2352/2406 — trang trọng, nhưng lập luận hình thức của O61 bao phủ). Lý do: chuẩn đại từ theo NHÂN VẬT (cùng người, cùng truyện; file chỉ là đơn vị tuỳ ý); để lại “tôi” ở 2 file sẽ giữ đúng sự không nhất quán mà đợt thống nhất này loại bỏ. Ghi rõ lập luận phạm vi-file vs cấp-nhân-vật. **GIỮ 1 dòng: ハチロク04 2094** — “tôi” là lời TRÍCH của Olivy (JP 『それなら、一日でも早く御一夜で仕事をしたい』と――, TW “它便提出…”), không phải của Munakata. (2223 cũng chứa trích dẫn nhưng “Tôi” của nó là của chính Munakata — sửa.)

### Mục 17 — F-P4-1: tên tách “Anh, Soutetsu” → “Sou, tetsu” (9 dòng)

Từ U7b REVIEW §6: dạng tên tách “Anh, Soutetsu” / “Anh Sou, tetsu” (JP そう、てつ / そうてつ tách). U7b đề xuất bỏ “Anh” cho nhất quán với P4 (“không bao giờ ‘anh Soutetsu’”), nhưng KHÔNG áp vì task chỉ định chuỗi chính xác. Tiền lệ ủng hộ bỏ: U7a D1 đã sửa h2 1166/1205 rên tách (“anh Sou――tetsu” → “Sou――tetsu”, chỉ bỏ “anh ”). 9 dòng đều sửa. CẮM CỜ (không sửa ở đây): SK 1355 “Xin anh đấy” và SP 1513 “anh đã cố gắng” — đại từ “anh” trần của Kisaki→Soutetsu (JP không có đại từ ở đó, chỉ おねがい + tên) — cho coordinator/U16.

### Mục 18 — T74: GHI CHÚ, 0 dòng

Nhãn list ghi 日々姫h2, file thật là 凪h2_おとなの水着 1766 (đã sửa trong U13b; “hợp đồng Maitetsu” → “hợp đồng chủ tàu” theo T8; không dòng nào).

## 3. Phương pháp

- Map giá trị hiện tại chỉ load từ các wrong.json unif **đã gộp** trong `~/workspace/maitetsu-pilot/unification/` (kiểm tra `queue.json` status=merged — chuỗi 160 mục / 2.731 dòng gồm U14a/b/c; KHÔNG dùng file worker đang chạy). Thứ tự ưu tiên old_vn (đã hiệu chỉnh 22/11 ~11:35, coordinator XÁC NHẬN): unif đã gộp (theo thứ tự gộp) > moan > audit > CSV3 VN (good set 87.833 dòng sau khi bỏ 3.898 dòng stale). Bỏ audit fix: null. Hai batch song song cùng đổi một (file,key) ở token khác nhau thì GHÉP, không ghi đè (tiền lệ U4-3719, U3∩U4 4 dòng, U6 Grand01 2181). Đợt này: **0 dòng GHÉP** — không (file,key) nào trùng với batch đang chạy (U15a/U16) trong số 436 dòng; mọi old_vn đều lấy từ map hiện tại, kiểm chứng lại ở §7. *(Sau 07:28 U15a ghi file → 21 dòng trùng, xem Phụ lục.)*
- Mọi fix đọc tay từng dòng JP (+TW); JP thắng TW khi khác nhau. Không bulk script fixing: script CHỈ dùng liệt kê/đếm/kiểm chứng. Không đụng dòng gasp-Ư hay “Kh” (trừ khi mục nói rõ — không mục nào trong đợt này nói rõ). Không sửa lại dòng đã đúng.
- Chuẩn hoá newline: giá trị moan/audit/unif nguồn có 8 giá trị chứa newline THẬT (5 old_vn moan + 3 fix nội dung F2/F3-extra ghi tay trước đợt này); giá trị parse từ TOML trên disk là literal backslash-n (2 ký tự) — đã chuẩn hoá về literal backslash-n trong JSON + khối TOML (khớp tiền lệ U10b; TOML basic string không chứa được newline thật). jp/tw từ CSV3: 0 giá trị cần chuẩn hoá.
- F5: xem §2 mục 6. Quy tắc token độc lập vs mảnh tách được áp thống nhất cả 390 dòng dump + 9 token sót ngoài dump. Hai lỗi applier đã sửa trong đợt: (1) literal backslash-n gộp với token sau (“nfua”, “nreryu”) — che trước khi tách token; (2) lệch chỉ số khi nhiều lần xuất hiện — tính mọi vị trí một lần rồi áp từ cuối lên đầu; (3) tên file `lr真闇追加h` (không gạch dưới sau “lr”) bị gõ sai thành `lr_真闇追加h` ở 2 quyết — đã sửa, applier chạy lại 0 bad; (4) 2 quyết trùng (file,key) (lr_凪h2 1229, lr_凪ふかみh1 1677) — đã gộp thành một mục mỗi dòng.
- Bẫy tự-phản-hồi: loader liệt kê unif đã gộp bằng glob `unification-*-wrong.json` — file output của chính đợt này (`unification-s4-flags-sweep-wrong.json`) từng lọt vào map và làm old_vn của ニイロク03 1404 biến thành fix của chính nó ở lần chạy assemble thứ hai. Đã sửa loader `_u15b/loader.py` loại trừ file output của đợt này; chạy lại assemble từ đầu cho cùng 436 mục, kiểm chứng lại toàn bộ ở §7. Kiểm tra lần 2 sửa thêm 3 giá trị (1570 khôi phục “khởi hành”, 1290 bỏ hoa “hamu”, 1038 thêm hoa “amu”) và bổ sung 25 dòng F5 (“ha”/“hu”/“gao” sót) — xem §2 mục 1/6.

## 4. Các dòng SỬA (436 dòng, kind="unification")

### 4.1. E2-Teio — 8 dòng (6 file). 帝央 → “Teio” (mục mới từ E2)

#### ニイロク03_粉蔵の嵐.txt.toml — 2 dòng

**1404** — JP 「各所での試験を終えれば、営業路線も延伸される。\n[ていおう,1]帝央-[なごや,2]名児耶-[おおさか,1]逢坂。[はかた,1]博太からも、逆に伸びていく」; TW 「只要各地的編組試驗結束，可營業的線路就會增加。從帝都中央車站延至名古屋、大阪。博多那邊也會連接過去」; old_vn (CSV3) 「Sau khi hoàn thành thử nghiệm ở các nơi, tuyến đường thương mại cũng sẽ được mở rộng.\nTeiou - Nagoya - Osaka. Và từ Hakata, cũng sẽ mở rộng ngược lại.」; **fix = 「Sau khi hoàn thành thử nghiệm ở các nơi, tuyến đường thương mại cũng sẽ được mở rộng.\nTeio - Nagoya - Osaka. Và từ Hakata, cũng sẽ mở rộng ngược lại.」**. Đổi: 'rộng.\\nTeiou' → 'rộng.\\nTeio'.

**1570** — JP 「ゆったりと仕事をしながら――快適に、\n帝央を出て……最終的には、博太まで」; TW 「我們的目標就是給從帝都中央車站到博多的商務旅客提供快速舒適的服務」; old_vn (CSV3) 「Vừa làm việc thong thả――vừa thoải mái,\nkhởi hành từ Teiou...... và cuối cùng là đến Hakata.」; **fix = 「Vừa làm việc thong thả――vừa thoải mái,\nkhởi hành từ Teio...... và cuối cùng là đến Hakata.」**. Đổi: 'Teiou......' → 'Teio......'.

#### ハチロク04_小畑越え.txt.toml — 1 dòng

**1802** — JP 「旧帝鉄、[ていおう,1]帝央\x%l機関区;#00ffc040;機関区%l;#;では、8620[けい]形\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、\nトップナンバー以外、ハロ１、ハロ２の連番だったと」; TW 「不是說在前帝國鐵路，帝國中央車站\x%l機関区;#00ffc040;機務段%l;#;，８６２０型\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;除首車人偶都依次稱為Haro1號、Haro2號的嘛」; old_vn (audit) 「Ở Teitetsu cũ, tại \x%l機関区;#00ffc040;kho đầu máy%l;#; Trung tâm Hoàng gia, các \x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」; **fix = 「Ở Teitetsu cũ, tại \x%l機関区;#00ffc040;kho đầu máy%l;#; Teio, các \x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」**. Đổi: 'Trung tâm Hoàng gia,' → 'Teio,'.

#### ハチロク06_のぞみ.txt.toml — 2 dòng

**2166** — JP 「サッポロ、センダイ、テイオー、ナゴヤ、オーサカ、\nキョート、ヒロシマ、カゴシマ！ めぐってみたい！」; TW 「什麼札幌、仙台、帝都中央車站、名古屋、大阪、京都、廣島、鹿兒島！這些奧莉薇都想去轉轉！」; old_vn (CSV3) 「Sapporo, Sendai, Teiou, Nagoya, Ousaka,\nKyoto, Hiroshima, Kagoshima! Olivy muốn đi vòng quanh thử xem sao!」; **fix = 「Sapporo, Sendai, Teio, Nagoya, Ousaka,\nKyoto, Hiroshima, Kagoshima! Olivy muốn đi vòng quanh thử xem sao!」**. Đổi: 'Teiou,' → 'Teio,'.

**2485** — JP 「エアクラ自動車に遥かに勝る――例えば時速200キロで、\n[ていおう,1]帝央と[おおさか,1]逢坂とを結ぶ超高速電車がもしもあるなら」; TW 「如果能出現速度上遠超空凝機汽車的列車——比如能以時速２００公里往返於帝都中央車站和大阪的超高速列車」; old_vn (audit) 「Vượt xa xe ô tô Aircra――ví dụ như nếu có một tuyến tàu điện siêu tốc\nnối liền Teiou và Ousaka với tốc độ 200km/h thì sao」; **fix = 「Vượt xa xe ô tô Aircra――ví dụ như nếu có một tuyến tàu điện siêu tốc\nnối liền Teio và Ousaka với tốc độ 200km/h thì sao」**. Đổi: 'Teiou' → 'Teio'.

#### 仲国05_真夜中の餐車.txt.toml — 1 dòng

**2032** — JP 「で。ございます。このやり方を、帝央機関区では、\n『[あっしゅくひきだしほう,4]圧縮引出方』などと呼称しておりました」; TW 「就是這樣。這種方法，在帝都中央車站機務段，被稱作“壓縮起步法”」; old_vn (CSV3) 「Đúng vậy ạ. Ở Khu đầu máy Trung tâm Hoàng gia, cách làm này\nđược gọi là 『Phương pháp khởi hành nén』 ạ.」; **fix = 「Đúng vậy ạ. Ở Khu đầu máy Teio, cách làm này\nđược gọi là 『Phương pháp khởi hành nén』 ạ.」**. Đổi: 'Trung tâm Hoàng gia,' → 'Teio,'.

#### 共通06_8620を探せ.txt.toml — 1 dòng

**2112** — JP 「[ていおう,1]帝央\x%l機関区;#00ffc040;機関区%l;#;では、長いこと清美機関士お一人だけでした。\nもっとも、戦中には女性\x%l機関士;#00ffc040;機関士%l;#;の方が多くなりましたが」; TW 「在帝都中央\x%l機関区;#00ffc040;機務段%l;#;，很長一段時間裡女性司機只有清美司機一人。不過在戰爭中女性\x%l機関士;#00ffc040;司機%l;#;倒是變得更多了」; old_vn (unif đã gộp) 「Ở \x%l機関区;#00ffc040;kho đầu máy%l;#; Teiou, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\nTuy nhiên, trong thời chiến thì số lượng nữ \x%l機関士;#00ffc040;lái tàu%l;#; đã tăng lên rất nhiều.」; **fix = 「Ở \x%l機関区;#00ffc040;kho đầu máy%l;#; Teio, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\nTuy nhiên, trong thời chiến thì số lượng nữ \x%l機関士;#00ffc040;lái tàu%l;#; đã tăng lên rất nhiều.」**. Đổi: 'Teiou,' → 'Teio,'.

#### 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml — 1 dòng

**2156** — JP 「ふふっ、お褒めに預かり光栄です。\n実のところわたくしの出身は、帝都・[ていおう,1]帝央でございます」; TW 「呵呵，蒙您誇獎，我很榮幸。其實我就來自帝都中央車站」; old_vn (audit) 「Fufu, được khen ngợi là vinh hạnh của tôi.\nThực ra xuất thân của tôi là ở Teiou, Đế đô đấy ạ.」; **fix = 「Fufu, được khen ngợi là vinh hạnh của tôi.\nThực ra xuất thân của tôi là ở Teio, Đế đô đấy ạ.」**. Đổi: 'Teiou,' → 'Teio,'.

### 4.2. F2 — 11 dòng (6 file). U13b F2 — T75-miss trong phụ lục T77/T78

#### lr_れいなh1_レディ・れいな.txt.toml — 3 dòng

**1251** — JP 「あむっ――れるっ――ちゅるっ――ちゅっ――ちゅっ\n――ちゅむ。ん……今日はちょっとしょっぱいですねぇ」; TW 「啊唔——舔——啾——啾——啾——啾。嗯……今天有點鹹呢」; old_vn (unif đã gộp) 「A mút——rộp——chu~——chụt——chụt\n——chu mút. Ưm…… hôm nay có hơi mặn một chút nha~」; **fix = 「A mút——rộp——chụt——chụt——chụt\n——chụt. Ưm…… hôm nay có hơi mặn một chút nha~」**. Đổi: 'chu~' → 'chụt'; 'chu mút.' → 'chụt.'.

**1266** — JP 「じゅぼっ！ ぼちゅっ！ じゅっ！ じゅろぉっ！\nれるっ――れりゅうっ！ ずっ！ ちゅばっ！ じゅぼ」; TW 「啾嗚噗啾！啾！刺溜！舔——舔舔！！ 呲溜！！ 啾啪！！ 啾嗚」; old_vn (unif đã gộp) 「Chu mút! Chụt mút! Chụt! Chu mút t!\nRộp——liếm m! Sụt! Chụt mút! Chu mút」; **fix = 「Chu mút! Chụt mút! Chụt! Chu mút t!\nRộp——liếm m! Sụt! Chụt! Chu mút」**. Đổi: 'Chụt mút!' → 'Chụt!'.

**1271** — JP 「ちゅぶっ！ ちゅぼっ！ ちゅぶっ！ ちゅずず～っ！\nずりゅっ！ ちゅむっ れろおっ、じゅっ！ ちゅぶっ」; TW 「啾噗！啾啪！啾噗！啾啾～吸！！呲溜！！ 啾啾、舔舔、啾！ 啾噗！」; old_vn (CSV3) 「Chu mút! Chu mút! Chu mút! Chu mút t~!\nChu mút! Chu mút! Liếm m, chụt! Chu mút!」; **fix = 「Chụt! Chụt! Chụt! Chu mút t~!\nChu mút! Chụt! Liếm m, chụt! Chụt!」**. Đổi: '「Chu' → '「Chụt!'; 'mút!' → 'Chụt!'; 'Chu mút! Chu mút!' → 'Chụt!'; 'Chu mút!' → 'Chụt!'; 'Chu mút!」' → 'Chụt!」'.

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 1 dòng

**1252** — JP 「ん……ちゅっ――ん……ふ……ぁ……\nふっ――ちゅむっ――ちゅうっ――れるっ」; TW 「嗯……啾……呼……啊……呼——啾唔——啾……唔」; old_vn (unif đã gộp) 「Ưm…… chụt——ưm…… Fu…… a……\nFu——chumu——chuu——reru」; **fix = 「Ưm…… chụt——ưm…… Fu…… a……\nFu——chụt——chụụt——rộp」**. Đổi: 'chumu' → 'chụt'; 'chuu' → 'chụụt'; 'reru」' → 'rộp」'.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 2 dòng

**1039** — JP 「ぺろっ――れるっ――んちゅっ――れるっ――ぺろっ、\nれりゅ――ちゅむっ――ちゅっ――ちゅううううっ！」; TW 「啾嚕、啾嚕、啾嚕……咕啾、啾……啾噗……啾嚕嚕嚕！」; old_vn (unif đã gộp) 「Liếm——rộp——nchu——rộp——liếm nhẹ,\nreryu——chụt——chụt——chuuuuu!」; **fix = 「Liếm——rộp——Nchu——rộp——liếm nhẹ,\nReryu——chụt——chụt——chụụụụụt!」**. Đổi: 'nchu' → 'Nchu'; 'nhẹ,\\nreryu' → 'nhẹ,\\nReryu'; 'chuuuuu!」' → 'chụụụụụt!」'.

**1045** — JP 「ちゅううううううっ！ んっ……ごくっ――ふ、あ\n――れるっ――れろおおっ――チュむっ――ちゅううっ」; TW 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾……噗啾！」; old_vn (unif đã gộp) 「Chuuuuuuu! Ưm…… ực——Fu, a\n——rộp——rerooo——chụt——chuuu」; **fix = 「Chụụụụụụụt! Ưm…… ực——Fu, a\n——rộp——Rerooo——chụt——chụụụt」**. Đổi: '「Chuuuuuuu!' → '「Chụụụụụụụt!'; 'rerooo' → 'Rerooo'; 'chuuu」' → 'chụụụt」'.

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 3 dòng

**1585** — JP 「ちゅっ―れるっ―ちゅうっ―ちゅむっ―\nちゅぱっ―ちゅうっ！ ちゅぶっ！ ちゅううっ！」; TW 「啾——舔——啾——啾——啾啪——啾！ 啾噗！ 啾啾！」; old_vn (unif đã gộp) 「Chụt——rộp——chuu u——chu mu——\nchu pa——chuu u! Chu bu! Chuu u!」; **fix = 「Chụt——rộp——chụụt——chụt——\nchụt——chụụt! Chụt! Chụụụt!」**. Đổi: 'chuu' → 'chụụt——chụt——\\nchụt——chụụt!'; 'u——chu' → 'Chụt!'; 'mu——\\nchu pa——chuu u! Chu bu! Chuu u!」' → 'Chụụụt!」'.

**1589** — JP 「ちゅ！ ちゅぶっ！ ちゅぱっ！―はむっ、くぷっ、\nちゅむっ―れろっ―れりゅうっ―ちゅむっっ」; TW 「啾！ 啾噗！ 啾啪！——啊嗚、唔嗯、啾啾——舔舔——舔舔——啾嗯」; old_vn (CSV3) 「Chụt! Chu bu! Chu pa! ——Ha mu, ku pu,\nchu mu——rê ro——rê ryu u——chu mu」; **fix = 「Chụt! Chụt! Chụt! ——Ha mu, ku pu,\nchụt——rê ro——rê ryu u——chụt」**. Đổi: 'Chu' → 'Chụt!'; 'bu! Chu pa!' → 'Chụt!'; 'pu,\\nchu mu' → 'pu,\\nchụt'; 'chu mu」' → 'chụt」'.

**1821** — JP 「れるっ―れろっ―れりゅっ―りゅっ―\nちゅうっ―ちゅっ―ぺろっっ―ぺちゅっ―」; TW 「舔——舔——啾——啾——啾——啾——舔——舔——」; old_vn (unif đã gộp) 「Rộp——rê ro——rê ryu——ryu——\nchuu u——chụt——pê ro——pê chu——」; **fix = 「Rộp——rê ro——rê ryu——ryu——\nchụụt——chụt——pê ro——pê chu——」**. Đổi: '\\nchuu u' → '\\nchụụt'.

#### ハチロクh2_お勉強の成果.txt.toml — 1 dòng

**1206** — JP 「れるっ――るっ――れろっ――じゅるるっ――\nんっ――んちゅっ――ちゅっ――ちゅううううっ」; TW 「（舔）——（舔）——（舔）——啾——嗯——嗯啾——啾——啾」; old_vn (unif đã gộp) 「Rộp——rộp——liếm——chu mút——\nưm——ưm chụt——chụt——chuuuuu」; **fix = 「Rộp——rộp——liếm——chu mút——\nưm——ưm chụt——chụt——chụụụụụt」**. Đổi: 'chuuuuu」' → 'chụụụụụt」'.

#### ハチロクh8_桜色のひめごと.txt.toml — 1 dòng

**825** — JP 「ん……ちゅっ――れろっ――れるっ――ちゅっ――\nちゅむ……ん……ぺろっ――れろっ――ちゅううっ！」; TW 「嗯……啾——嗯——咻嚕——啾——啾嗯……（舔）——嗯——啾嗚！」; old_vn (unif đã gộp) 「Ưm……chụt——liếm——rộp——chụt——\nchụt……ưm……liếm láp——mút mát——chụttttt!」; **fix = 「Ưm……chụt——liếm——rộp——chụt——\nchụt……ưm……liếm láp——mút mát——chụụụt!」**. Đổi: 'chụttttt!」' → 'chụụụt!」'.

### 4.3. F3 — 7 dòng (5 file). U13b F3 — T77-miss trong phụ lục T75

#### lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 2 dòng

**1213** — JP 「っ！！！！ （はぷっ！！！！）――れるっ！\nじゅううううっ！ ずちゅっ！ じゅぶっ！！！！」; TW 「啊！！！！（含！！！！）啾!啾！啾！啾！！！！」; old_vn (moan) 「Ư!!!! （Hapu!!!!）――reru!\nJuuuuu! Zuchu! Jubu!!!!」; **fix = 「Ư!!!! （Hapu!!!!）――rộp!\nJuuuuu! Zuchu! Jubu!!!!」**. Đổi: '（Hapu!!!!）――reru!\\nJuuuuu!' → '（Hapu!!!!）――rộp!\\nJuuuuu!'.

**1220** — JP 「じゅるっ！ れるうううっ！ れろっ！ ちゅぱっ！\nんっ！ じゅぶっ！ じゅぼっ！ じゅっ！ じゅぶ！」; TW 「啾！啾！啾！啾！嗯！啾！啾！啾！啾！」; old_vn (unif đã gộp) 「Juru! Reruuuu! Rero! Chụt!\nƯm! Jubu! Jubo! Ju! Jubu!」; **fix = 「Juru! Rộộộộp! Rero! Chụt!\nƯm! Jubu! Jubo! Ju! Jubu!」**. Đổi: 'Reruuuu!' → 'Rộộộộp!'.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 1 dòng

**1056** — JP 「ぐぽっ！ ぐぱっ！ ちゅぶっ！ じゅずっ！ ずっ！\nじゅるるるっ！ ぢゅぼっ！ れるっ！ ぶちゅう！」; TW 「嗯……啾、啾……啾嚕……啾嚕……啾嚕……啾……啾噗！」; old_vn (unif đã gộp) 「Gupo! Gupa! Chụt! Juzu! Zu!\nJurururu! Jyubo! Reru! Buchuu!」; **fix = 「Gupo! Gupa! Chụt! Juzu! Zu!\nJurururu! Jyubo! Rộp! Buchuu!」**. Đổi: 'Reru!' → 'Rộp!'.

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 1 dòng

**1058** — JP 「ぢゅむっ！ ぢゅぼっ！ ぼっ！ ぢゅうううううっ！\nずびゅっ――ちゅ――れるっ――ずぼっ！ ぼちゅっ！」; TW 「啾嚕！啾噗！啾嚕嚕嚕！啾、啾、啾……噗啾！」; old_vn (unif đã gộp) 「Jumu! Jubo! Bo! Juuuuuu!\nZubyu――chụt――reru――zubo! Bochu!」; **fix = 「Jumu! Jubo! Bo! Juuuuuu!\nZubyu――chụt――rộp――Zubo! Bochu!」**. Đổi: 'Juuuuuu!\\nZubyu――chụt――reru――zubo!' → 'Juuuuuu!\\nZubyu――chụt――rộp――Zubo!'.

#### ハチロクh9_コノフクハキルコト.txt.toml — 2 dòng

**1358** — JP 「――ちゅっ――ちゅっ、ちゅっ――ちゅむ、ちゅっ、\nちゅっ、ちゅうっ――ちゅっ――ちゅむ――れるっ」; TW 「——啾——啾，啾——啾嗯，啾，啾，啾嗚——啾——啾嗯——咻嚕」; old_vn (moan) 「——Chụt——chụt, chụt——chumu, chụt,\nchụt, chuu——chụt——chumu——reru」; **fix = 「——Chụt——chụt, chụt——Chumu, chụt,\nchụt, Chuu——chụt——Chumu——rộp」**. Đổi: 'chumu,' → 'Chumu,'; 'chuu' → 'Chuu'; 'chumu' → 'Chumu'; 'reru」' → 'rộp」'.

**2136** — JP 「ちろっ、ぺろっ、ぺろっ、ぺろっ、れるっ――\nんっ――ぺるっ、ぺろっ――ぺろ、ぺろ、ぺろ、ぺろ」; TW 「啾嚕，呸嚕，呸嚕，呸嚕，咻嚕——嗯——呸嚕，呸嚕——呸嚕、呸嚕」; old_vn (moan) 「Chiro, pero, pero, pero, rero——\nƯm——pero, pero——pero, pero, pero, pero」; **fix = 「Chiro, Pero, Pero, Pero, rộp——\nƯm——Pero, Pero——Pero, Pero, Pero, Pero」**. Đổi: 'pero,' → 'Pero,'; 'pero,' → 'Pero,'; 'pero,' → 'Pero,'; 'rero' → 'rộp'; 'pero,' → 'Pero,'; 'pero' → 'Pero'; 'pero,' → 'Pero,'; 'pero,' → 'Pero,'; 'pero,' → 'Pero,'; 'pero」' → 'Pero」'.

#### 真闇h3_補習授業の廃校舎.txt.toml — 1 dòng

**2332** — JP 「ん……ちゅっ――んちゅ――ちゅっ――ちゅうっ、\nちゅっ――ちゅ、むっ――んっ――れる――ぷあっ」; TW 「嗯……啾――嗯啾――啾――啾、啾――啾、唔――嗯――嚕溜――噗啊」; old_vn (unif đã gộp) 「Ưm……chụt――ưm chụt――chụt――chụụt,\nchụt――chụt, mu――ưm――reru――pua.」; **fix = 「Ưm……chụt――ưm chụt――chụt――chụụt,\nchụt――chụt, Mu――ưm――rộộộp――Pua.」**. Đổi: 'mu――ưm――reru――pua.」' → 'Mu――ưm――rộộộp――Pua.」'.

### 4.4. F5 — 310 dòng (53 file). U13b F5 — viết hoa token romaji SFX (quyết coordinator 22/11 ~12:50)

#### lr_ふかみh1_ふかみうさぎのたまご.txt.toml — 4 dòng

**1196** — JP 「だが――ぁっ――このまま、で、はっ――」; TW 「但是……啊……這樣下去……」; old_vn (moan) 「Nhưng——a——cứ thế này, thì——ha——」; **fix = 「Nhưng——a——cứ thế này, thì——Ha——」**. Đổi: 'ha' → 'Ha'.

**1432** — JP 「ふ――かみ――緩めて、くれないとっ――ぁあっ！！」; TW 「深美……快放開我……呃！！」; old_vn (moan) 「Fu——kami——nới lỏng ra, cho anh——aa!!」; **fix = 「Fu——kami——nới lỏng ra, cho anh——Aa!!」**. Đổi: 'aa!!」' → 'Aa!!」'.

**1460** — JP 「は……ぁっ――ふぁぅ……んっ――えへへっ――\nそうてつおにいさん――わたしの、双鉄おにいさぁん」; TW 「蛤啊……啊嗯……嘿嘿……雙鐵哥哥……只屬於我的，雙鐵哥哥」; old_vn (moan) 「Ha…… a——Fau…… ưm——ehehe——\nanh Soutetsu——của em, anh Soutetsu của em.」; **fix = 「Ha…… a——Fau…… ưm——Ehehe——\nanh Soutetsu——của em, anh Soutetsu của em.」**. Đổi: 'ehehe' → 'Ehehe'.

**1655** — JP というか、ふかみがいっそう狭い。\n精液を更に欲しがって、きゅんきゅんぐいぐい締めてくる。; TW 應該說是深美的小穴縮得更緊了。她越來越渴求精液，肉壁不停地收緊。; old_vn (moan) Nói đúng hơn là, Fukami càng khít hơn.\nKhao khát tinh dịch hơn nữa, em ấy siết chặt lấy tôi, kyun kyun.; **fix = Nói đúng hơn là, Fukami càng khít hơn.\nKhao khát tinh dịch hơn nữa, em ấy siết chặt lấy tôi, Kyun Kyun.**. Đổi: 'kyun' → 'Kyun'; 'kyun.' → 'Kyun.'.

#### lr_ふかみh2_セックスの意味.txt.toml — 4 dòng

**1029** — JP 「んひゅっ！！？ ちょっ――ちょっ待っ――あうっ――\nらめっ――いま、クリトリスは――強すぎっ――あ！」; TW 「呀啊？！等、等一下……不要啦……現在碰陰蒂……太刺激了……啊！」; old_vn (moan) 「Nhyu!!? Khoan——khoan đã——au——\nkhông được——bây giờ, âm vật thì——kích thích quá——a!」; **fix = 「Nhyu!!? Khoan——khoan đã——Au——\nkhông được——bây giờ, âm vật thì——kích thích quá——a!」**. Đổi: 'au' → 'Au'.

**1060** — JP 「はうっ――ァ――あっ――あっ――おまんこ――これ、\nわたし――わたしの――おまんこ――おまんこ――」; TW 「哈嗚……啊……啊啊……小穴……我、我的小穴……小穴」; old_vn (moan) 「Hau——ah——ah——ah——âm đạo——đây là,\ncủa em——của em——âm đạo——âm đạo——」; **fix = 「Hau——Ah——Ah——Ah——âm đạo——đây là,\ncủa em——của em——âm đạo——âm đạo——」**. Đổi: 'ah' → 'Ah'; 'ah' → 'Ah'; 'ah' → 'Ah'.

**1063** — JP 「おにいひゃっ――はうっ――そうてつ、おにいさ――\nあっ――ふっ――あっ――あっ――ん～～～っっっ！」; TW 「哥哥……啊嗚……雙鐵哥哥。啊……唔……啊嗯！」; old_vn (moan) 「Anh——Hya——hau——Soutetsu, anh——\nA——phù——a——a——ưm~~~ƯƯƯ!!!」; **fix = 「Anh——Hya——Hau——Soutetsu, anh——\nA——phù——a——a——ưm~~~ƯƯƯ!!!」**. Đổi: 'hau' → 'Hau'.

**1270** — JP 「ふあっ！ あっ！ あっ！ あっ！ あっ！！\nひっ！ あっ！ しょこっ！ んっ――ぁ――ふうっ」; TW 「蛤啊！啊啊啊啊！！呀啊！啊！啊啊啊！啊嗯！」; old_vn (moan) 「Fua! A! A! A! A!!\nHí! A! Chỗ đó! Ưm——a——fuu.」; **fix = 「Fua! A! A! A! A!!\nHí! A! Chỗ đó! Ưm——a——Fuu.」**. Đổi: 'fuu.」' → 'Fuu.」'.

#### lr_れいなh1_レディ・れいな.txt.toml — 1 dòng

**1202** — JP 「ふぁっ――はっ――はっ――はっ――\nふぁぁっ――はぁっ――はぁ――はぁ――」; TW 「呼啊——哈——哈——哈——呼啊——哈——哈——哈——」; old_vn (moan) 「Fa——ha——ha——ha——\nFaa——haa——haa——haa——」; **fix = 「Fa——Ha——Ha——Ha——\nFaa——Haa——Haa——Haa——」**. Đổi: 'ha' → 'Ha'; 'ha' → 'Ha'; 'ha' → 'Ha'; 'haa' → 'Haa'; 'haa' → 'Haa'; 'haa' → 'Haa'.

#### lr_ニイロクh_誓い。約束.txt.toml — 11 dòng

**1272** — JP 「ふあっ──あっ──あっっっ──あああっ──」; TW 「呼啊——啊——啊啊啊——啊啊啊——」; old_vn (moan) 「Fua──a──a ư ư ư──aaa──」; **fix = 「Fua──a──a ư ư ư──Aaa──」**. Đổi: 'ư──aaa──」' → 'ư──Aaa──」'.

**1275** — JP 「はぁっ、はぁっ、はぁっ、はあっ──ん、くっ──\nあっ──ごりって──ごりって、しゅる、とこで」; TW 「呼啊、呼啊、呼啊、呼啊——嗯、唔——啊——硬硬的——硬硬的地方」; old_vn (moan) 「Hàà, hàà, hàà, hàà──ưm, ku──\na──chỗ cứng──cứ cọ vào, chỗ cứng đó」; **fix = 「Hàà, hàà, hàà, hàà──ưm, Ku──\na──chỗ cứng──cứ cọ vào, chỗ cứng đó」**. Đổi: 'ku──\\na──chỗ' → 'Ku──\\na──chỗ'.

**1278** — JP 「はあああんっ！ ふあっ！ あっ！ おく、なかっ！\nふあっ！ あっ！ あっ！ ああああっ！！！！！」; TW 「呼啊啊啊啊啊！呼啊！啊！裡面，最深處！呼啊！啊！啊！啊啊啊啊！！！！！」; old_vn (moan) 「Hà aaan! Fua! A! Sâu, bên trong!\nFua! A! A! Aaaa!!!!!」; **fix = 「Hà Aaan! Fua! A! Sâu, bên trong!\nFua! A! A! Aaaa!!!!!」**. Đổi: 'aaan!' → 'Aaan!'.

**1288** — JP 「ふあっ！？ あっ──ああっ──はうっ──んっ。\nちょくせつ──すり、すり──凄い、さっきよりっ」; TW 「呼啊！？啊——啊——啊嗚——嗯。直接——摸來摸去——比剛才、還舒服」; old_vn (moan) 「Fua!? A──aa──ha ư──ưm.\nTrực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」; **fix = 「Fua!? A──Aa──ha ư──ưm.\nTrực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」**. Đổi: 'A──aa──ha' → 'A──Aa──ha'.

**1322** — JP 「！ ならっ、これ、愛撫っ──ンっ──こしゅ。こしゅ、\nで──気持ち、よく、して、くれてるの──ふあっ」; TW 「啊！那這個、愛撫——嗯——摸來摸去——讓我這麼、舒服——呼啊」; old_vn (unif đã gộp) 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho tôi, sướng──fua.」; **fix = 「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\nthế này──là đang làm cho tôi, sướng──Fua.」**. Đổi: 'sướng──fua.」' → 'sướng──Fua.」'.

**1337** — JP 「ん………………ぷあっ──えへへっ──\nきよはる──きよはるぅ」; TW 「嗯………………噗啊——哎嘿嘿——清春——清春」; old_vn (moan) 「Ưm.................. pua──e he he──\nKiyoharu──Kiyoharuu」; **fix = 「Ưm.................. Pua──e he he──\nKiyoharu──Kiyoharuu」**. Đổi: 'pua──e' → 'Pua──e'.

**1353** — JP 「んむっ！？ ん……ちゅっ──ちゅむっ──ぷあっ、\nんっ──ちゅずっ──ちゅっ──れるっ──ちゅるっ」; TW 「嗯唔！？嗯……啾——啾嚕──呼啊、嗯——啾噗——啾——啾嚕——啾叭」; old_vn (moan) 「Ưm!? Ưm... chụt——chụt——pua,\nưm——chụt——chụt——liếm——rột」; **fix = 「Ưm!? Ưm... chụt——chụt——Pua,\nưm——chụt——chụt——liếm——rột」**. Đổi: 'pua,\\nưm' → 'Pua,\\nưm'.

**1356** — JP 「んきゅっ！ んうっ！ ふ、ゅっ──みゅっ──\nんううううううっ──！！」; TW 「嗯啾！嗯！呼、嗯——嗚——嗯嗚嗚嗚！！」; old_vn (moan) 「Nkyu! Ưm! Fu, yu──Myu──\nưmmmmmm──!!」; **fix = 「Nkyu! Ưm! Fu, Yu──Myu──\nưmmmmmm──!!」**. Đổi: 'yu──Myu──\\nưmmmmmm──!!」' → 'Yu──Myu──\\nưmmmmmm──!!」'.

**1387** — JP 「しゅごい、のっ！ ぜんぶっ──ふあっ！ あっ！\nなか、ねっ！ おんなのこっ ちつ、が──ちつない！」; TW 「好厲害！全部都——呼啊！啊！進來了！女孩子的、陰道的——裡面！」; old_vn (moan) 「Tuyệt, quá! Tất cả──fua! A!\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」; **fix = 「Tuyệt, quá! Tất cả──Fua! A!\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」**. Đổi: 'cả──fua!' → 'cả──Fua!'.

**1395** — JP 「シー……リン、グ──ふぁっ……ん、くっ──はっ──\nそれ──なにっ──んうっ」; TW 「封印……呼啊——嗯、唔——哈——那是——什麼——嗯唔」; old_vn (moan) 「Niêm... phong──Fa... ưm, ku──hà──\ncái đó──là gì──ưm」; **fix = 「Niêm... phong──Fa... ưm, Ku──hà──\ncái đó──là gì──ưm」**. Đổi: 'ku──hà──\\ncái' → 'Ku──hà──\\ncái'.

**1438** — JP 「うれし、うれしい──んっ──あっ──\nふあっ！？ ふああぁんっっ！！」; TW 「我好開心、好開心——嗯——啊——呼啊！？呼啊啊啊！！」; old_vn (unif đã gộp) 「Vui, tôi vui lắm──ưm──a──\nfua!? Fuaaan ư ư!!」; **fix = 「Vui, tôi vui lắm──ưm──a──\nFua!? Fuaaan ư ư!!」**. Đổi: 'lắm──ưm──a──\\nfua!?' → 'lắm──ưm──a──\\nFua!?'.

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 8 dòng

**1153** — JP 「ふっ――ぁ――。\nん……ふぁ……ぅ――ん…………あ！」; TW 「呼——啊——嗯……哈……嗯…………啊！」; old_vn (unif đã gộp) 「Fu——a——.\nƯm…… fa…… u——ưm………… a!」; **fix = 「Fu——a——.\nƯm…… Fa…… u——ưm………… a!」**. Đổi: 'fa……' → 'Fa……'.

**1158** — JP 「ふやっ！！？ ゆ、指っ――\n双鉄さまのお指が――んっ――ふぁっ」; TW 「呼呀！！？手，手指——雙鐵少爺的手指——嗯——呼啊」; old_vn (unif đã gộp) 「Fuya!!? Ng-ngón tay——\nNgón tay của ngài Soutetsu——ưm——fa.」; **fix = 「Fuya!!? Ng-ngón tay——\nNgón tay của ngài Soutetsu——ưm——Fa.」**. Đổi: 'fa.」' → 'Fa.」'.

**1163** — JP 「ふえっ！？ がまっ――がまんっ――ん、ふっ、\nはぁっ――はっ――ふっ、あんっ！ も、もうっ我慢っ」; TW 「咦！？忍耐——忍耐——嗯，呼，哈——哈——呼，嗯！忍、不住了」; old_vn (moan) 「Fue!? Nhịn——nhịn——ưm, fu,\nhaa——ha——fu, an! Kh-không nhịn được nữa đâu.」; **fix = 「Fue!? Nhịn——nhịn——ưm, Fu,\nHaa——Ha——fu, an! Kh-không nhịn được nữa đâu.」**. Đổi: 'fu,\\nhaa' → 'Fu,\\nHaa'; 'ha' → 'Ha'.

**1178** — JP 「ふぁっ――あっ――ンッ――きゅふっ――ぁ――ふ――\nそうてつ、さまっ――そうてつ、さまぁっ」; TW 「哈——啊——嗯——呼——呼——雙鐵，少爺——雙鐵，少爺——」; old_vn (unif đã gộp) 「Fa——a——n——kyufu——a——fu——\nSou, tetsu, sama——Sou, tetsu, sama~」; **fix = 「Fa——a——n——Kyufu——a——Fu——\nSou, tetsu, sama——Sou, tetsu, sama~」**. Đổi: 'kyufu' → 'Kyufu'; 'fu' → 'Fu'.

**1213** — JP 「ん……ちゅむっ――ちゅずっ――じゅっ――（こくっ）\n――ちゅむっ――れるっ――れろっ――ちゅりゅっ」; TW 「唔……啾唔——啾嘶——啾——（咽）啾唔——唔——唔——啾嚕」; old_vn (unif đã gộp) 「Ưm…… chụt——chuzu——ju——(ực)\n——chụt——rộp——rero——churyu」; **fix = 「Ưm…… chụt——Chuzu——Ju——(ực)\n——chụt——rộp——Rero——Churyu」**. Đổi: 'chuzu' → 'Chuzu'; 'ju' → 'Ju'; 'rero' → 'Rero'; 'churyu」' → 'Churyu」'.

**1237** — JP 「あ……や――ふ、ぁ――\nはずかし――はずかしゅうございます」; TW 「啊……這——呼啊——害羞——好害羞啊……」; old_vn (unif đã gộp) 「A…… ya——Fu, a——\nXấu hổ——em xấu hổ lắm ạ.」; **fix = 「A…… Ya——Fu, a——\nXấu hổ——em xấu hổ lắm ạ.」**. Đổi: 'ya' → 'Ya'.

**1241** — JP 「あむっ――ふっ――んっ――れうっ――りゅっ――\nちゅむっ――ちゅうっ――じゅりゅっ――」; TW 「啊嗚……呼……唔……啾……啾唔——啾——啾嚕——」; old_vn (unif đã gộp) 「Amu——fu——ưm——reu——ryu——\nChụt——chụụt——juryu——」; **fix = 「Amu——Fu——ưm——Reu——Ryu——\nChụt——chụụt——Juryu——」**. Đổi: 'fu' → 'Fu'; 'reu' → 'Reu'; 'ryu' → 'Ryu'; 'juryu' → 'Juryu'.

**2008** — JP （ちゅむっ――ぷりゅっ）; TW （輕搖柔擺）; old_vn (unif đã gộp) （Chụt——puryu）; **fix = （Chụt——Puryu）**. Đổi: 'puryu）' → 'Puryu）'.

#### lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml — 1 dòng

**1232** — JP 「はっ――はひゅっ――ん……ふあっ――\nあ――あ――あ――あ――ふぁっ」; TW 「哈、哈呼、嗯……呼啊、啊、啊、啊、啊……呼啊」; old_vn (moan) 「Ha——hahyu——ưm……Fua—— a——a——a——a——Fa」; **fix = 「Ha——Hahyu——ưm……Fua—— a——a——a——a——Fa」**. Đổi: 'hahyu' → 'Hahyu'.

#### lr_ポーレットh1_家族旅行の最終日の夜.txt.toml — 4 dòng

**1026** — JP 「はっ――んっ――ふうっ、ふうっ――んっ！ あっ、\n腰っ、もっと――くっ、ふ――双鉄、くんっ――あっ！」; TW 「哈——嗯——呼唔，呼唔——嗯！啊，腰、繼續、呼——雙鐵君——啊！」; old_vn (unif đã gộp) 「Ha——ưm——phù, phù——ưm! A,\nEo, tiếp tục đi——Ku, phu——anh Soutetsu——a!」; **fix = 「Ha——ưm——phù, phù——ưm! A,\nEo, tiếp tục đi——Ku, Phu——anh Soutetsu——a!」**. Đổi: 'phu' → 'Phu'.

**1062** — JP 「ぁ……チュッ――ちゅっ――んっ――ふぁっ。\nん……えへへっ――わたしも、愛しています。双鉄くん」; TW 「啊……啾——啾——嗯——呼啊。嗯……哎嘿嘿——我也愛你。雙鐵君」; old_vn (moan) 「A……chụt——chụt——ưm——Fa. Ưm……ehehe——em cũng yêu anh. Anh Soutetsu」; **fix = 「A……chụt——chụt——ưm——Fa. Ưm……Ehehe——em cũng yêu anh. Anh Soutetsu」**. Đổi: 'Ưm……ehehe' → 'Ưm……Ehehe'.

**1096** — JP 「んきゅっ――ふぁっ――あっ、これ――しゅきっ――\nっっ――ふっ――ねっ――このまま――もっと」; TW 「嗯呀——呼啊——啊，這個——好棒——唔——呼——來——就這樣——繼續」; old_vn (moan) 「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——phu——nè——cứ thế này——nữa đi」; **fix = 「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」**. Đổi: 'phu' → 'Phu'.

**1113** — JP 「ぷあっ！ あっ――はっ――あっ――しゅごっ――\nおまんこ――しきゅう――すごい――こい、のっ」; TW 「噗啊！啊——哈——啊——好厲害——小穴——子宮——好多——濃濃的」; old_vn (moan) 「Pua! A——ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」; **fix = 「Pua! A——Ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」**. Đổi: 'ha' → 'Ha'.

#### lr_ポーレットh2_デコレーション＆ミルク.txt.toml — 3 dòng

**1022** — JP 「ふあっ――は――ァ――あっ――ゆっくり、も――\nすき――んっ――きもち、いいとこ――じっくり――ぁ」; TW 「呼啊——哈——啊——啊——慢慢來——也好喜歡——嗯——舒服的，地方——仔細按摩——啊」; old_vn (moan) 「Fua——ha——a——a——chậm rãi, thế này——\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」; **fix = 「Fua——Ha——a——a——chậm rãi, thế này——\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」**. Đổi: 'ha' → 'Ha'.

**1041** — JP 「はっ！ あっ！ ぁっ――あ――ぁあっ！！\nそう、てつ、くっ――あっ！ わた、しっ――だんだん」; TW 「哈！啊！啊——啊——啊啊！！雙鐵、君——啊！我——快要」; old_vn (unif đã gộp) 「Ha! A! A——a——aa!!\nAnh, Soutetsu——Ku——a! Em——sắp」; **fix = 「Ha! A! A——a——Aa!!\nAnh, Soutetsu——Ku——a! Em——sắp」**. Đổi: 'aa!!\\nAnh,' → 'Aa!!\\nAnh,'.

**1084** — JP 「はっ――あうっ――ふぁんっ――んっ――くぅんっ――\nん。これ――ゆっくり――はっ――ゆっくぃ、らのにぃ」; TW 「啊——啊唔——呼啊——嗯——咕嗯——嗯。這樣——慢慢擺動——哈——明明動作那麼慢」; old_vn (moan) 「Ha——au——Fan——ưm——kuuun——\nƯm. Thế này——chậm rãi——ha——chậm rãi, thế mà」; **fix = 「Ha——Au——Fan——ưm——Kuuun——\nƯm. Thế này——chậm rãi——Ha——chậm rãi, thế mà」**. Đổi: 'au' → 'Au'; 'kuuun' → 'Kuuun'; 'ha' → 'Ha'.

#### lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 11 dòng

**1128** — JP 「ひゃうっ！ あっ――ふあっ！ あっ！ おまんこっ！\nしきゅうっ――あちゅいのっ――おっぱいっ――ふ、あ」; TW 「呀！啊……啊！啊！下面滋滋地……進來了燙燙的……胸部也……啊」; old_vn (unif đã gộp) 「Hyau! A——fua! A! Cô bé!\nTử cung——nóng quá——ngực cũng——Fu, a」; **fix = 「Hyau! A——Fua! A! Cô bé!\nTử cung——nóng quá——ngực cũng——Fu, a」**. Đổi: 'fua!' → 'Fua!'.

**1162** — JP 「んくっ！？ ぷっ――ふぁっ――ンッ――じゅる！\nじゅぼっ！ じゅぶっ！ じゅばっ！ ちゅううっ」; TW 「唔？！噗……啊……嗯……啾！啾！啾！啾！啾」; old_vn (unif đã gộp) 「Ưm ku!? Pu――fa――ưm――juru!\nJubo! Jubu! Juba! Chụụụt」; **fix = 「Ưm ku!? Pu――Fa――ưm――Juru!\nJubo! Jubu! Juba! Chụụụt」**. Đổi: 'Pu――fa――ưm――juru!\\nJubo!' → 'Pu――Fa――ưm――Juru!\\nJubo!'.

**1163** — JP 「くあっ――はあっ――はあっ――はあっ――はあっ」; TW 「啊……呼……呼……呼……呼」; old_vn (moan) 「Kua——haa——haa——haa——haa」; **fix = 「Kua——Haa——Haa——Haa——Haa」**. Đổi: 'haa' → 'Haa'; 'haa' → 'Haa'; 'haa' → 'Haa'; 'haa」' → 'Haa」'.

**1185** — JP 「あ……ん……ふぁっ――あっ――にーさん……\nもっと――もっと、強く――んっ――強く、して」; TW 「啊……嗯……啊……啊……大哥哥……用力……用力點……嗯……再用力點」; old_vn (moan) 「A……ưm……fa――á――anh hai……\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」; **fix = 「A……ưm……Fa――á――anh hai……\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」**. Đổi: '「A……ưm……fa――á――anh' → '「A……ưm……Fa――á――anh'.

**1190** — JP 「あ……もう、ちょっと――んっ――くっ――ふあっ！\nも、ちょっとで――おまんこの、おく――おちん、ちん」; TW 「啊……還差一點……嗯……唔……啊！還差一點……雞雞……就能進到……最深處了」; old_vn (unif đã gộp) 「A……Sắp, được rồi——ưm——Ku——fua!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」; **fix = 「A……Sắp, được rồi——ưm——Ku——Fua!\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」**. Đổi: 'fua!\\nMột,' → 'Fua!\\nMột,'.

**1214** — JP 「え？ わっ――わわわわわわわっ！？」; TW 「啊？哇……哇哇哇哇哇？！」; old_vn (moan) 「Hả? Wa――wawawawawawa!?」; **fix = 「Hả? Wa――Wawawawawawa!?」**. Đổi: 'Wa――wawawawawawa!?」' → 'Wa――Wawawawawawa!?」'.

**1216** — JP 「ぴちゃっ――ぺろっ――ぺろっ――ぺろっ――\nれりゅっ――ぺちょっ――ぺろっ――ぺろっ――」; TW 「啾……啾……啾……啾……啾……啾……啾……啾……」; old_vn (moan) 「Picha――pero――pero――pero――\nreryu――pecho――pero――pero――」; **fix = 「Picha――Pero――Pero――Pero――\nReryu――Pecho――Pero――Pero――」**. Đổi: '「Picha――pero――pero――pero――\\nreryu――pecho――pero――pero――」' → '「Picha――Pero――Pero――Pero――\\nReryu――Pecho――Pero――Pero――」'.

**1221** — JP 「じゅうううううっ！ ずぼっ――ごっ！！！！\nじゅるううううっっっ！ ずびょっ！――ぎゅっ！！」; TW 「啾！滋……咕！啾！滋！啾！」; old_vn (moan) 「Juuuuuu! Zubo――go!!!!\nJuruuuuu! Zubyo!――Gyu!!」; **fix = 「Juuuuuu! Zubo――Go!!!!\nJuruuuuu! Zubyo!――Gyu!!」**. Đổi: 'Zubo――go!!!!\\nJuruuuuu!' → 'Zubo――Go!!!!\\nJuruuuuu!'.

**1233** — JP 「ん……はっ――おっぱい――じわじわ――ンッ――\nまわり、から――もみもみ、される、の――ふあっ！」; TW 「嗯……啊……胸部，都是汗……嗯……被這樣從四周揉著……啊！」; old_vn (moan) 「Ưm……hà――vú――từ từ――ưm――\ntừ, xung quanh――bị, xoa nắn――fua!」; **fix = 「Ưm……hà――vú――từ từ――ưm――\ntừ, xung quanh――bị, xoa nắn――Fua!」**. Đổi: 'nắn――fua!」' → 'nắn――Fua!」'.

**1236** — JP 「ん――ぷあっ！ あ……にーさん、ん……そぎゃん、\nされ、たら――ふあっ――凪、さま――しゅう、ちゅう」; TW 「嗯……啊！啊……大哥哥，嗯……你這樣，啊……本小姐的……注意力」; old_vn (moan) 「Ưm――pua! A……anh hai, ưm……bị, làm,\nnhư vậy――fua――Nagi, sama――tập, trung」; **fix = 「Ưm――Pua! A……anh hai, ưm……bị, làm,\nnhư vậy――Fua――Nagi, sama――tập, trung」**. Đổi: '「Ưm――pua!' → '「Ưm――Pua!'; 'vậy――fua――Nagi,' → 'vậy――Fua――Nagi,'.

**1298** — JP 「修行に夢中になってにーさんの気配ばとれなかった\nうちが未熟――ああっ――（ふーっ、ふーっ）」; TW 「是我沉浸於練刀，沒注意到大哥哥……啊（呼——呼——）」; old_vn (moan) 「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\nLà do em còn non kém――aa――（Phùu, phùu）」; **fix = 「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\nLà do em còn non kém――Aa――（Phùu, phùu）」**. Đổi: 'kém――aa――（Phùu,' → 'kém――Aa――（Phùu,'.

#### lr_凪h2_虎さんの交尾.txt.toml — 16 dòng

**1174** — JP 「ひゃっ――ンッ――どうして、脇、と？ 凪、さま\n――ふぁっ――こぎゃんと――くすぐったか、と――」; TW 「呀……嗯……為什麼是腋下？本小姐……啊……怕癢……」; old_vn (moan) 「Hya——ưm——sao lại, là nách, chứ? Nagi\n——fa——chỗ đó——nhột lắm——」; **fix = 「Hya——ưm——sao lại, là nách, chứ? Nagi\n——Fa——chỗ đó——nhột lắm——」**. Đổi: 'fa' → 'Fa'.

**1190** — JP 「ひゃうっ！？ ふぁっ――あっ――きもち、よか、けど、\nん――いま見てほしいのは――もっと下――がお」; TW 「呀？！哇……啊，好舒服，可是，唔……現在咱想讓你看更下面嗷」; old_vn (moan) 「Hyau!? Fa——a——sướng, lắm, nhưng mà,\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——gao」; **fix = 「Hyau!? Fa——a——sướng, lắm, nhưng mà,\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——Gao」**. Đổi: 'gao」' → 'Gao」'.

**1199** — JP 「ふあっ――あっ！ あ！ あ！ あっ――\nんっ――ふやっ――きもち、よか――んっ――ふっ」; TW 「哇……啊！啊！啊！啊……嗯……呀……好舒服……嗯……呼」; old_vn (moan) 「Fua——a! A! A! A——\nƯm——fuya——sướng, quá——ưm——phù」; **fix = 「Fua——a! A! A! A——\nƯm——Fuya——sướng, quá——ưm——phù」**. Đổi: 'fuya' → 'Fuya'.

**1229** — JP 「ふぁ――ひゃうっ――あっ……ん……んへへっ――\n凪、さま――凪さま――んっ――うれしかと……ふぁっ」; TW 「啊……呀……啊……嗯……嘿嘿，本小姐……本小姐……嗯……好開心……啊」; old_vn (moan) 「Fa——hyau——a……ưm……nhehe——\nNagi——Nagi——ưm——vui lắm……fa」; **fix = 「Fa——Hyau——a……ưm……Nhehe——\nNagi——Nagi——ưm——vui lắm……Fa」**. Đổi: 'hyau' → 'Hyau'; 'a……ưm……nhehe' → 'a……ưm……Nhehe'; 'lắm……fa」' → 'lắm……Fa」'.

**1235** — JP 「あっ――ふぁ――あっ――」; TW 「啊……啊……啊……」; old_vn (moan) 「A——fa——a——」; **fix = 「A——Fa——a——」**. Đổi: 'fa' → 'Fa'.

**1236** — JP 「ふぁ――ふぁ――アッっ――あっ――\nにぃさん――ね――にぃさん――にぃさぁああん」; TW 「啊……啊……啊……啊……大哥哥，大哥哥……大哥哥」; old_vn (moan) 「Fa——fa——A——a——\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」; **fix = 「Fa——Fa——A——a——\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」**. Đổi: 'fa' → 'Fa'.

**1241** — JP 「ぁっ――っ――にーさん……エッチ、ばい……ふぁ……\n凪さまの、ちっちゃか、おっぱい――そぎゃん、夢中に」; TW 「啊……啊……大哥哥……好色情……啊……竟然對本小姐的……小小胸部……這麼沉醉」; old_vn (moan) 「A——a——anh Soutetsu……dâm đãng, quá……fa……\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」; **fix = 「A——a——anh Soutetsu……dâm đãng, quá……Fa……\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」**. Đổi: 'quá……fa……\\nSay' → 'quá……Fa……\\nSay'.

**1245** — JP 「か――はっ――あ――あっとる、ばい――がお。\nそれで、腰を、最初は、ゆっくり、動かし、て――」; TW 「啊……啊……對，沒錯咧……嗷。然後，一開始的時候，要慢慢動腰」; old_vn (moan) 「Ka——ha——a——đúng rồi, đó——gao.\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」; **fix = 「Ka——Ha——a——đúng rồi, đó——Gao.\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」**. Đổi: 'ha' → 'Ha'; 'gao.\\nRồi' → 'Gao.\\nRồi'.

**1247** — JP 「はっ――あっ――それっ――もっと――にーさん、\nいまの――もっと――ふあっ！ もっとぉっ――っ！」; TW 「啊……啊……這個，再來……大哥哥，剛才這個，再來……啊！再來！」; old_vn (moan) 「Ha——a——cái đó——nữa đi——anh Soutetsu,\nlúc nãy ấy——nữa đi——fua! Nữa đi——Ư!」; **fix = 「Ha——a——cái đó——nữa đi——anh Soutetsu,\nlúc nãy ấy——nữa đi——Fua! Nữa đi——Ư!」**. Đổi: 'fua!' → 'Fua!'.

**1254** — JP 「ふぁ――そう、おちんちん、で――おまんこ、もっと\n――じゅぶじゅぶって――して――んっ――は、あっ」; TW 「啊……對，用雞雞……更猛烈一點……啊，啊」; old_vn (moan) 「Fa——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\n——phập phập——đi——ưm——ha, a」; **fix = 「Fa——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\n——phập phập——đi——ưm——Ha, a」**. Đổi: 'ha,' → 'Ha,'.

**1258** — JP 「ふぁ……（ごくっ）――あ！ ふ、ふふふーん！！\nにーさん、凪さまに興奮――発情しちゃったと？」; TW 「啊……（咕咚）……啊！哼哼！！大哥哥看本小姐看得興奮，看得發情了吧？」; old_vn (moan) 「Fa……（Ực）——A! Fu, fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」; **fix = 「Fa……（Ực）——A! Fu, Fufufu-n!!\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」**. Đổi: 'fufufu-n!!\\nAnh' → 'Fufufu-n!!\\nAnh'.

**1280** — JP 「ふぇ――ふあ！！？」; TW 「啊？啊！」; old_vn (moan) 「Fue——fua!!?」; **fix = 「Fue——Fua!!?」**. Đổi: 'fua!!?」' → 'Fua!!?」'.

**1285** — JP 「ちゅうっ――ちゅむっ――れるっ――れろおっ――\nじゅ――ずじゅうううっ――（こくっ）――ぷあっ」; TW 「啾……啾，啾，啾……啾，啾……（咕咚）啊……」; old_vn (unif đã gộp) 「Chụt——chụt——rộp——liếm——\nju——zujuuu——（Ực）——pua」; **fix = 「Chụt——chụt——rộp——liếm——\nJu——Zujuuu——（Ực）——Pua」**. Đổi: '\\nju' → '\\nJu'; 'zujuuu' → 'Zujuuu'; 'pua」' → 'Pua」'.

**1290** — JP 「ん……ひーはむ……ンっ――ひゅき――ちゅっ――\nれるっ――ちゅうう――れるうううっ――ちゅむっ」; TW 「嗯……啊唔……嗯……嘶……啾……啾，啾……啾……啾」; old_vn (unif đã gộp) 「Ưm……hi-hamu……ưm——hyuki——chụt——\nrộp——chụt——rộộộộp——chụt」; **fix = 「Ưm……hi-hamu……ưm——Hyuki——chụt——\nrộp——chụt——rộộộộp——chụt」**. Đổi: 'hyuki' → 'Hyuki'.

**1304** — JP 「んっ、ひゅっ！ ふぁっ――べろぉんって、されると、\nされ、ると――うち、ふあっ――おまんこ、あつ、くて」; TW 「嗯，唔！啊……被你這樣舔著，咱……啊……咱的下面好熱」; old_vn (moan) 「Ưm, hyu! Fa——khi bị, liếm như vậy,\nbị liếm, như vậy——em, fua——cô bé, nóng, quá」; **fix = 「Ưm, Hyu! Fa——khi bị, liếm như vậy,\nbị liếm, như vậy——em, Fua——cô bé, nóng, quá」**. Đổi: 'hyu!' → 'Hyu!'; 'fua' → 'Fua'.

**1325** — JP 「にぃ――さぁん――んっ――やぁ――ん――はっ――\nいじある――しな、いでっ――ンッ――もっと、してぇ」; TW 「大哥哥……嗯……呀……嗯……啊……不要欺負人……嗯……再來刺激點的」; old_vn (moan) 「Anh——Soutetsu——ưm——yaa——ưm——ha——\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」; **fix = 「Anh——Soutetsu——ưm——Yaa——ưm——Ha——\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」**. Đổi: 'yaa' → 'Yaa'; 'ha' → 'Ha'.

#### lr_凪ふかみh1_じぇいけい！.txt.toml — 14 dòng

**1485** — JP 「や、あっ！？ ふかみ、ちゃんっ――ンッ――じっと、\n見ちゃ、や――うちが――ずぼずぼっ――あうぅっ！？」; TW 「呀，啊？！小深……嗯……別盯著……咱看……咱正在被……啊？！」; old_vn (moan) 「D, á!? Fukami——ưm——đừng,\nnhìn chằm chằm thế——em đang——bị đâm phập phập——auu!?」; **fix = 「D, á!? Fukami——ưm——đừng,\nnhìn chằm chằm thế——em đang——bị đâm phập phập——Auu!?」**. Đổi: 'auu!?」' → 'Auu!?」'.

**1505** — JP 「ふっ……あ――（すんっ、すんんっ）――すご、い……\n精液……匂い、いっつもより、濃い……ふぁっ――」; TW 「呼……啊……（嗅，嗅）好棒……精液的……味道……比平時更濃郁……哇……」; old_vn (moan) 「Fu……a——（Khịt, khịt）——Tuyệt, quá……\nTinh dịch……mùi, nồng hơn, mọi khi……fa——」; **fix = 「Fu……a——（Khịt, khịt）——Tuyệt, quá……\nTinh dịch……mùi, nồng hơn, mọi khi……Fa——」**. Đổi: 'khi……fa' → 'khi……Fa'.

**1507** — JP 「はぁっ！ はあっ！ はあっ！ えふっ！ はっ――\nはぁっ！ ――はぁ……ふぅ……はぁ……はぁ……はぁ」; TW 「呼！呼！呼！嘔！呼……呼！呼……呼……呼……呼……呼」; old_vn (moan) 「Haa! Haa! Haa! Efu! Ha——\nHaa! ——Haa……fuu……haa……haa……haa」; **fix = 「Haa! Haa! Haa! Efu! Ha——\nHaa! ——Haa……Fuu……Haa……Haa……Haa」**. Đổi: 'Haa……fuu……haa……haa……haa」' → 'Haa……Fuu……Haa……Haa……Haa」'.

**1509** — JP 「ふあっ――あっ――しゅごっ――すごっ――ふあっ！\nしきゅう――たたいて――びゅって――せいえきっ」; TW 「哇……啊……好棒……好棒……啊！精液……打在子宮裡……咻咻的」; old_vn (moan) 「Fua——a——tuyệt quá——tuyệt quá——fua!\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」; **fix = 「Fua——a——tuyệt quá——tuyệt quá——Fua!\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」**. Đổi: 'fua!\\nTử' → 'Fua!\\nTử'.

**1581** — JP 「ぁ――ふかみ、ちゃんっ――はぁ――ふぁっ――んっ」; TW 「啊……小深……啊，啊……嗯」; old_vn (moan) 「A——Fukami——haa——fa——ưm」; **fix = 「A——Fukami——Haa——Fa——ưm」**. Đổi: 'haa' → 'Haa'; 'fa' → 'Fa'.

**1595** — JP 「あっ！ ふあっ！ それも！ そっちもっ！！\n新しいのもくださいっ！ わたしのっ――ひゃんっ！？」; TW 「啊！啊！也要！我也要！新的我也要！給我……呀？！」; old_vn (moan) 「A! Fua! Cái đó! Cả cái đó nữa!!\nHãy cho em cả đợt mới đi! Cho em——hyan!?」; **fix = 「A! Fua! Cái đó! Cả cái đó nữa!!\nHãy cho em cả đợt mới đi! Cho em——Hyan!?」**. Đổi: 'hyan!?」' → 'Hyan!?」'.

**1614** — JP 「はぁっ、はぁっ、はぁっ、はぁっ」; TW 「啊，啊，啊，啊」; old_vn (moan) 「Haa, haa, haa, haa」; **fix = 「Haa, Haa, Haa, Haa」**. Đổi: 'haa,' → 'Haa,'; 'haa,' → 'Haa,'; 'haa」' → 'Haa」'.

**1643** — JP 「れろっ――じゅりゅっ――ぺろっ――れるっ――\nじゅっ――じゅりゅううううう――（こくっ）――ぷぁ」; TW 「啾，啾，啾，啾，啾，啾……（咕咚）哇」; old_vn (unif đã gộp) 「Liếm——mút——liếm——rộp——\nmút——mútttttt——（Ực）——pua」; **fix = 「Liếm——mút——liếm——rộp——\nmút——mútttttt——（Ực）——Pua」**. Đổi: 'pua」' → 'Pua」'.

**1646** — JP 「ちゅむっ――ちゅっ――れるっ――れろっ――んっ――\nじゅ――ずっ――ずじゅううううっ――こくっ――ぷぁ」; TW 「啾，啾，啾，啾，嗯，啾，滋，滋，咕咚……哇」; old_vn (unif đã gộp) 「Chụt——chụt——rộp——liếm——ưm——\nju——zu——zujuuuuu——（Ực）——pua」; **fix = 「Chụt——chụt——rộp——liếm——ưm——\nJu——Zu——zujuuuuu——（Ực）——Pua」**. Đổi: '\\nju' → '\\nJu'; 'zu' → 'Zu'; 'pua」' → 'Pua」'.

**1657** — JP 「ちょっ！？ 凪ちゃっ！ ふあっ！ だめっ！\nこれ！ わらひっ！ わたし――感じすぎ――ひゃう！」; TW 「喂？！小凪！哇！不行！這樣，我，我……會因為太舒服……呀！」; old_vn (moan) 「Khoan!? Nagi! Fua! Không được!\nThế này! Tớ! Tớ——sẽ sướng quá mất——hyau!」; **fix = 「Khoan!? Nagi! Fua! Không được!\nThế này! Tớ! Tớ——sẽ sướng quá mất——Hyau!」**. Đổi: 'hyau!」' → 'Hyau!」'.

**1658** — JP 「う……ぁ……顔中、べとべとばぁい――ん……\nちゅるっ――（ごくっ）――ふぁ――粘っこかぁ～」; TW 「嗚……啊……整張臉都黏糊糊的咧……嗯……啾……（咕咚）……哇，太黏了」; old_vn (moan) 「U……a……khắp mặt, nhớp nháp quá đi——ưm……\nChụt——（Ực）——fa——đặc dính luôn~」; **fix = 「U……a……khắp mặt, nhớp nháp quá đi——ưm……\nChụt——（Ực）——Fa——đặc dính luôn~」**. Đổi: 'fa' → 'Fa'.

**1660** — JP 「ん……れろおっ――れりゅうっ――レロおっ――\nふっ――んっ――れろおっ――れるううっ――れろおお」; TW 「嗯……啾，啾，啾……呼……嗯……啾，啾，啾」; old_vn (unif đã gộp) 「Ưm……liếm——liếm——liếm——\nfu——ưm——liếm——rộộộp——liếm」; **fix = 「Ưm……liếm——liếm——liếm——\nFu——ưm——liếm——rộộộp——liếm」**. Đổi: '\\nfu' → '\\nFu'.

**1677** — JP 「んっ！？ ぷぁっ！ あっ！？ ぁ――はあっ！？\nそんな、いき――なりっ――ぁぁぁあああああんっ！」; TW 「嗯？！哇！啊？！啊……啊？！怎麼突然……啊！」; old_vn (moan) 「Ưm!? Pua! A!? A——haa!?\nSao lại, đột ngột——thế——aaaaaaaan!」; **fix = 「Ưm!? Pua! A!? A——Haa!?\nSao lại, đột ngột——thế——Aaaaaaaan!」**. Đổi: 'haa!?\\nSao' → 'Haa!?\\nSao'; 'aaaaaaaan!」' → 'Aaaaaaaan!」'.

**1714** — JP 「あつい――あついよぉ――ふあっ――しゅきっ――\nすき、すき――双鉄おにいさん、好き、凪ちゃん、好き」; TW 「好燙……好燙呀……啊……愛你……愛你，愛你，雙鐵哥哥，愛你，小凪，愛你」; old_vn (moan) 「Nóng quá——nóng quá đi——fua——thích lắm——\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」; **fix = 「Nóng quá——nóng quá đi——Fua——thích lắm——\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」**. Đổi: 'fua' → 'Fua'.

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 11 dòng

**991** — JP 「あむっ――ちゅるっ――はむっ――ちゅっ――むっ――\nかぷっ――れるっ――あむっ――ぢゅるっ――はむっ！」; TW 「啊嗚……啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……哈嗚！」; old_vn (unif đã gộp) 「Amu——chụt——hamu——chụt——mu——\nKapu——rộp——amu——juru——hamu!」; **fix = 「Amu——chụt——Hamu——chụt——Mu——\nKapu——rộp——Amu——Juru——Hamu!」**. Đổi: 'hamu' → 'Hamu'; 'mu' → 'Mu'; 'amu' → 'Amu'; 'juru' → 'Juru'; 'hamu!」' → 'Hamu!」'.

**998** — JP 「でゅぼっ！ じゅ！！ ぢゅるるっ！ ちゅ、ばっ！\nんっ――ぢゅぼっ！ ちゅうっ！ じゅるっ！ じゅぶ」; TW 「啊嗯……啾，啾嚕……啊嗯……啾……啾嚕……啾嚕嚕」; old_vn (unif đã gộp) 「Dyubo! Ju!! Jyururu! Chụt, ba!\nƯm——jyubo! Chụụt! Juru! Jubu」; **fix = 「Dyubo! Ju!! Jyururu! Chụt, ba!\nƯm——Jyubo! Chụụt! Juru! Jubu」**. Đổi: 'jyubo!' → 'Jyubo!'.

**1016** — JP 「ちゅむっ――れるうっ――ちゅっ――ちゅっ、ちゅっ、\nれりゅううっ――れろっ――ちゅうううううううっ！！」; TW 「啾……啾……啾嚕嚕嚕……啾嚕……啾嚕……咕嘟……啾！！！」; old_vn (unif đã gộp) 「Chụt——rộộp——chụt——chụt, chụt,\nreryuuu——rero——chuuuuuuuu!!」; **fix = 「Chụt——rộộp——chụt——chụt, chụt,\nReryuuu——Rero——Chuuuuuuuu!!」**. Đổi: 'chụt,\\nreryuuu' → 'chụt,\\nReryuuu'; 'rero' → 'Rero'; 'chuuuuuuuu!!」' → 'Chuuuuuuuu!!」'.

**1033** — JP 「れるっ――じゅぶっ――じゅむっ――るっ――ぶっ――\n『ひゃばば、ばふぃっ』、ぷぁっ――ぷっ――じゅるっ」; TW 「啾嚕……啾噗……啾嚕……對不起了……啾……啾嚕」; old_vn (unif đã gộp) 「Rộp——nhóp nhép——mút——rộp——phập——\n『Hyababa, bafi』, pua——pu——nhóp nhép.」; **fix = 「Rộp——nhóp nhép——mút——rộp——phập——\n『Hyababa, Bafi』, Pua——Pu——nhóp nhép.」**. Đổi: 'bafi』,' → 'Bafi』,'; 'pua' → 'Pua'; 'pu' → 'Pu'.

**1036** — JP 「あ～～――ん～――れるっ――ぺりゅっ――ん……\nれりゅうううっ――れるっ――ぺろっ――れちゅんっ」; TW 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾」; old_vn (unif đã gộp) 「A~~——ưm~——rộp——nhóp nhép——ưm……\nReryuuuu——rộp——liếm nhẹ——rechun」; **fix = 「A~~——ưm~——rộp——nhóp nhép——ưm……\nReryuuuu——rộp——liếm nhẹ——Rechun」**. Đổi: 'rechun」' → 'Rechun」'.

**1038** — JP 「はむっ――れるっ――あむっ――ちゅうっ――はむっ、\nちゅっ――ふぁむっ――ちゅうっ――んっ――っ！！！」; TW 「啾嚕、啾啾……啾嚕嚕嚕！啾嚕嚕……啾嚕……咕啾！！！！」; old_vn (unif đã gộp) 「Hamu——rộp——amu——chụụt——hamu,\nChụt——famu——chụụt——ưm——Ư!!!」; **fix = 「Hamu——rộp——Amu——chụụt——Hamu,\nChụt——Famu——chụụt——ưm——Ư!!!」**. Đổi: 'amu' → 'Amu'; 'hamu,\\nChụt' → 'Hamu,\\nChụt'; 'famu' → 'Famu'.

**1041** — JP 「ちゅるっ――もむっ！ はむっ――あむっ――\nん……はむっ――かぷっ――もぷっ――あむっ――」; TW 「啾嚕、啾嚕嚕嚕……咕啾！嗯……啾……啾嚕……咕啾！」; old_vn (unif đã gộp) 「Chụt——momu! Hamu——amu——\nƯm…… hamu——kapu——mopu——amu——」; **fix = 「Chụt——Momu! Hamu——Amu——\nƯm…… Hamu——Kapu——Mopu——Amu——」**. Đổi: 'momu!' → 'Momu!'; 'amu' → 'Amu'; 'hamu' → 'Hamu'; 'kapu' → 'Kapu'; 'mopu' → 'Mopu'; 'amu' → 'Amu'.

**1042** — JP 「ん……はぁ――んっ――ちゅむっ――れろっ――ちゅっ、\nれりゅううっ――れろっ――しゃぶっ――れるううっ」; TW 「啾嚕嚕嚕……啾嚕……啾嚕……咕嘟。啾、啾嚕、啾嚕嚕……啾嚕嚕嚕」; old_vn (unif đã gộp) 「Ưm…… ha——ưm——chụt——rero——chụt,\nreryuuu——rero——mút——rộộộp」; **fix = 「Ưm…… Ha——ưm——chụt——Rero——chụt,\nReryuuu——Rero——mút——rộộộp」**. Đổi: 'ha' → 'Ha'; 'rero' → 'Rero'; 'chụt,\\nreryuuu' → 'chụt,\\nReryuuu'; 'rero' → 'Rero'.

**1046** — JP 「れっるっ――ぺろっ――ちゅっ――ちゅううっ――\nん……ぺろっ――れりゅっ――ぺろっ――じゅずうっ！」; TW 「啾嚕！啾噗！啾嚕嚕嚕！咕嘟……啾、啾、啾、啾嚕嚕嚕！！」; old_vn (unif đã gộp) 「Rộp——liếm nhẹ——chụt——chuuu——\nƯm…… liếm nhẹ——reryu——liếm nhẹ——juzuu!」; **fix = 「Rộp——liếm nhẹ——chụt——Chuuu——\nƯm…… liếm nhẹ——Reryu——liếm nhẹ——Juzuu!」**. Đổi: 'chuuu' → 'Chuuu'; 'reryu' → 'Reryu'; 'juzuu!」' → 'Juzuu!」'.

**1053** — JP 「ちゅろおおおおっ――れるっ――ちゅっ、チュッ――\nちゅむっ――れるっ――ちゅずっ――ず、ずうううっ」; TW 「嗯……啾……啾嚕……啾……啾嚕嚕……啾嚕……」; old_vn (unif đã gộp) 「Churooooo——rộp——chụt, chụt——\nChụt——rộp——chuzu——zu, zuuuu」; **fix = 「Churooooo——rộp——chụt, chụt——\nChụt——rộp——Chuzu——Zu, Zuuuu」**. Đổi: 'chuzu' → 'Chuzu'; 'zu,' → 'Zu,'; 'zuuuu」' → 'Zuuuu」'.

**1173** — JP 「ふぁっ！ あっ――にぃにっ――んっ――ふあっ、\nあっ――べろっ――あったかい――しゅきぃっ」; TW 「蛤啊！啊……阿哥……嗯……蛤啊……啊……舌頭好暖……好舒服」; old_vn (moan) 「Fa! A——anh hai——ưm——fua,\nA——lưỡi——ấm quá——thích lắm.」; **fix = 「Fa! A——anh hai——ưm——Fua,\nA——lưỡi——ấm quá——thích lắm.」**. Đổi: 'fua,\\nA' → 'Fua,\\nA'.

#### lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml — 8 dòng

**1334** — JP 「やっ！？ 激しっ――ですっ――ふあっ！ あっ！」; TW 「呀！？ 太激——烈了——呼啊！啊！」; old_vn (moan) 「Ya!? Mãnh liệt――quá――fua! A!」; **fix = 「Ya!? Mãnh liệt――quá――Fua! A!」**. Đổi: 'liệt――quá――fua!' → 'liệt――quá――Fua!'.

**1356** — JP 「ふぁっ――あっ――んきゅっ！ うっ！ にぃに！\nまっ！ って――わらっ――わた、しっ――もうっ！」; TW 「呼啊——啊——嗚！嗚！阿哥！等等——我——我——要！」; old_vn (unif đã gộp) 「Fa――a――nkyu! Ư! Anh hai!\nĐợi! Đã――em――em, em――sắp!」; **fix = 「Fa――a――Nkyu! Ư! Anh hai!\nĐợi! Đã――em――em, em――sắp!」**. Đổi: '「Fa――a――nkyu!' → '「Fa――a――Nkyu!'.

**1406** — JP 「っ！！？ ――あ、あぁ」; TW 「唔！！？ ——啊，嗯」; old_vn (moan) 「Ư!!? ――A, aa」; **fix = 「Ư!!? ――A, Aa」**. Đổi: 'aa」' → 'Aa」'.

**1440** — JP 「あっ……うふふっ！\n双鉄おにいさん、おっきくなってきちゃいましたねぇ」; TW 「啊……唔呵呵！雙鐵哥哥，你變大了呀」; old_vn (moan) 「A…… ufufu!\nAnh Soutetsu, nó to lên rồi kìa.」; **fix = 「A…… Ufufu!\nAnh Soutetsu, nó to lên rồi kìa.」**. Đổi: 'ufufu!\\nAnh' → 'Ufufu!\\nAnh'.

**1461** — JP 「ちゅむ――れりゅっ――れろおおおっ――ずりゅっ――\nちゅむっ――ちゅっ――ずりゅうううっ――（こくっ）」; TW 「啾唔——滋溜——滋溜溜——滋溜——啾唔——啾——滋溜溜——（嚥下）」; old_vn (unif đã gộp) 「Chùn chụt――rê ryu――Reroooo――zuryu――\nChùn chụt――chụt――zuryuuu――（Ực）」; **fix = 「Chùn chụt――rê ryu――Reroooo――Zuryu――\nChùn chụt――chụt――Zuryuuu――（Ực）」**. Đổi: 'ryu――Reroooo――zuryu――\\nChùn' → 'ryu――Reroooo――Zuryu――\\nChùn'; 'chụt――chụt――zuryuuu――（Ực）」' → 'chụt――chụt――Zuryuuu――（Ực）」'.

**1475** — JP 「ん――ちゅっ――ちゅむっ――ちゅう――れるっ――\nれりゅううっ――じゅるっ――じゅ――ずりゅ――るっ」; TW 「嗯——啾——啾唔——啾嗚——滋溜——滋溜——啾嚕——啾——滋溜——滋溜」; old_vn (unif đã gộp) 「Ưm――chụt――chùn chụt――chụt――rộp――\nrê ryuuu――chùn chụt――chu――zuryu――ru」; **fix = 「Ưm――chụt――chùn chụt――chụt――rộp――\nrê ryuuu――chùn chụt――Chu――Zuryu――Ru」**. Đổi: 'chụt――chu――zuryu――ru」' → 'chụt――Chu――Zuryu――Ru」'.

**1477** — JP 「ん――れるっ――れろっ――ちゅむっ――ちゅっ――\nん……ちゅうっ――じゅるっ――（こくっ）――ぷ、あ」; TW 「嗯——滋溜——滋溜——啾唔——啾——嗯……啾唔——啾嚕——（嚥下）——噗、啊」; old_vn (unif đã gộp) 「Ưm――rộp――rê rô――chùn chụt――chụt――\nƯm…… chụt――chùn chụt――（Ực）――pu, a」; **fix = 「Ưm――rộp――rê rô――chùn chụt――chụt――\nƯm…… chụt――chùn chụt――（Ực）――Pu, a」**. Đổi: 'chụt――（Ực）――pu,' → 'chụt――（Ực）――Pu,'.

**1479** — JP 「ん……ぁ――あっ――ふっ――あっ――ん――\nちゅっ――ちゅむっ――ん……フッ――ふぁっ――あ」; TW 「嗯……啊——啊——呼——啊——嗯——啾——啾唔——嗯……呼——呼啊——啊」; old_vn (unif đã gộp) 「Ưm…… a――a――hư――a――ưm――\nChụt――chùn chụt――ưm…… hư――fa――a」; **fix = 「Ưm…… a――a――hư――a――ưm――\nChụt――chùn chụt――ưm…… hư――Fa――a」**. Đổi: 'hư――fa――a」' → 'hư――Fa――a」'.

#### lr_日々姫真闇h1_三人家族.txt.toml — 5 dòng

**1471** — JP 「ふやっ！？ やっ！ ふっ――あっ――ああっっ！！\nねぇね――私――こんな――ふ、ぁっ――上手、すぎっ」; TW 「呼呀！？呀！呼——啊——啊啊！！阿姐——我——這樣弄——呼、啊——太厲害了」; old_vn (unif đã gộp) 「Fuya!? Ya! Fu――a――aa!!\nChị hai――em――thế này――Fu, a――giỏi, quá.」; **fix = 「Fuya!? Ya! Fu――a――Aa!!\nChị hai――em――thế này――Fu, a――giỏi, quá.」**. Đổi: 'Fu――a――aa!!\\nChị' → 'Fu――a――Aa!!\\nChị'.

**1522** — JP 「むちゅっ――ちゅうっ――ぺろっ――れりゅっ――ちゅ\n――れるううっ――ぬろっ――じゅううっ――む、ちゅ」; TW 「唔啾——啾唔——滋溜——滋嚕——啾——滋嚕嚕——嚕唔——滋嚕嚕——唔、啾」; old_vn (unif đã gộp) 「Muchu――chụụt――pero――reryu――chụt\n――rộộộp――nuro――juuu――mu, chụt」; **fix = 「Muchu――chụụt――Pero――Reryu――chụt\n――rộộộp――Nuro――Juuu――Mu, chụt」**. Đổi: '「Muchu――chụụt――pero――reryu――chụt\\n――rộộộp――nuro――juuu――mu,' → '「Muchu――chụụt――Pero――Reryu――chụt\\n――rộộộp――Nuro――Juuu――Mu,'.

**1573** — JP 「ちゅっ――んっ――れるっ――れりゅっ――ちゅりゅっ、\nちゅ――むちゅうっ――れりゅうっ――ちゅ、ちゅずっ」; TW 「啾——嗯——滋溜——滋咧——啾溜，啾——唔啾——滋溜——啾，啾茲」; old_vn (unif đã gộp) 「Chụt――ưm――rộp――rê ryu――churyu,\nchu――muchuu――reryuu――chu, chuzu」; **fix = 「Chụt――ưm――rộp――rê ryu――Churyu,\nChu――Muchuu――Reryuu――Chu, Chuzu」**. Đổi: 'ryu――churyu,\\nchu――muchuu――reryuu――chu,' → 'ryu――Churyu,\\nChu――Muchuu――Reryuu――Chu,'; 'chuzu」' → 'Chuzu」'.

**1585** — JP 「ん……ちゅっ――れりゅっ――ちゅるっ――じゅゆうっ\n――れるうっ――れろっ――ちゅっ――ちゅずっ、ずっ」; TW 「嗯……啾——滋溜——啾嚕——啾唔唔——滋溜——滋溜——啾——啾滋、滋」; old_vn (unif đã gộp) 「Ưm…… chụt――reryu――chụt――juyuu\n――rộộp――rero――chụt――chuzu, zu」; **fix = 「Ưm…… chụt――Reryu――chụt――Juyuu\n――rộộp――Rero――chụt――Chuzu, Zu」**. Đổi: 'chụt――reryu――chụt――juyuu\\n――rộộp――rero――chụt――chuzu,' → 'chụt――Reryu――chụt――Juyuu\\n――rộộp――Rero――chụt――Chuzu,'; 'zu」' → 'Zu」'.

**1634** — JP 「ねぇねの――おっぱい――やわらか――んっ――すごっ\n――ぁ――指――沈むのに――はりつい、て――ふぁっ」; TW 「姐姐的——胸部——好柔軟——嗯——好驚人——啊——手指——陷進去——肉都纏上來了——呼啊」; old_vn (unif đã gộp) 「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\n――a――ngón tay――lún vào――rồi bám chặt, lấy――fa.」; **fix = 「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\n――a――ngón tay――lún vào――rồi bám chặt, lấy――Fa.」**. Đổi: 'lấy――fa.」' → 'lấy――Fa.」'.

#### lr_真闇h1_僕のおねえちゃん.txt.toml — 7 dòng

**1429** — JP 「ふぁっ！ あっ――あっ――あ……ああ……」; TW 「呼啊！ 啊——啊——啊……啊……」; old_vn (unif đã gộp) 「Fa! A——a——a……aa……」; **fix = 「Fa! A——a——a……Aa……」**. Đổi: 'a……aa……」' → 'a……Aa……」'.

**1477** — JP 「ちゅっ――ちゅむっ――ちゅうっ――れるっ――\nれろおっ、れりゅっ――ちゅう――ずっ――ぷあっ」; TW 「啾——啾嗯——啾——舔舔——舔舔，啾啾——啾啾，啾——呼啊」; old_vn (unif đã gộp) 「Chụt——chụt——chụt——rộp——\nrột, rột——chụt——chụt——phuha」; **fix = 「Chụt——chụt——chụt——rộp——\nrột, rột——chụt——chụt——Phuha」**. Đổi: 'phuha」' → 'Phuha」'.

**1507** — JP 「んっ――れるっ――んちゅっ――れりゅんっ！」; TW 「嗯——舔——嗯——啾！」; old_vn (unif đã gộp) 「Ưm——rộp——nchu——liếm!」; **fix = 「Ưm——rộp——Nchu——liếm!」**. Đổi: 'nchu' → 'Nchu'.

**1598** — JP 「わかった！ わかりましたっ！ っ――今日は――\n僕、はっ――全部！ まかせる――おねえちゃんにっ！」; TW 「我懂了！ 我完全懂了！ ——今天的——我——全部！ 都交給你了——姐姐！」; old_vn (moan) 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\ntôi, ha——sẽ——giao phó! Tất cả——cho chị!」; **fix = 「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\ntôi, Ha——sẽ——giao phó! Tất cả——cho chị!」**. Đổi: 'ha' → 'Ha'.

**1655** — JP 「れるうううっ――ちゅっ――く、りゅ――ずりゅっ！\nむちょっ――ぺろっ――くりゅっ、く――ずりゅん！！」; TW 「舔舔舔舔……啾——……轉動——滋溜……！啾啾——舔舔——轉動——滋溜！！」; old_vn (unif đã gộp) 「Rộộộộp——chụt——ku, ryu——trơn tuột!\nChụt——liếm——xoay, ku——trơn tuột!!」; **fix = 「Rộộộộp——chụt——Ku, Ryu——trơn tuột!\nChụt——liếm——xoay, Ku——trơn tuột!!」**. Đổi: 'ku,' → 'Ku,'; 'ryu' → 'Ryu'; 'ku' → 'Ku'.

**1816** — JP このタイミング舌がくっ――！！！！！！！; TW 在這種時候的舌頭，嗚——！！！！！！！！！; old_vn (moan) Lưỡi lại liếm vào lúc này——ku!!!!!!!; **fix = Lưỡi lại liếm vào lúc này——Ku!!!!!!!**. Đổi: 'ku!!!!!!!' → 'Ku!!!!!!!'.

**2029** — JP 部屋に入ってきたその瞬間から勃起していた乳首を押せば、\n真闇姉は発情しきったメス猫のような声を――ああ。; TW 進入房間的那一瞬間，我按下她勃起的乳頭，真闇姐就發出像發情的母貓一樣的聲音——啊。; old_vn (moan) Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,\nchị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——aa.; **fix = Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,\nchị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——Aa.**. Đổi: 'aa.' → 'Aa.'.

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 8 dòng

**1023** — JP 「あーーーん……（はぷっ）――ちゅっ――ちゅううっ、\nちゅるっ――ずっ――――――（こくっ）――ぷぁっ」; TW 「啊嗯……啊嗚……啾、啾嚕……啾嚕……嗚……咕嘟……噗」; old_vn (unif đã gộp) 「Aaaan……(hapu)――chụt――chụụụt,\nchụt――zu――――――(koku)――pua.」; **fix = 「Aaaan……(Hapu)――chụt――chụụụt,\nchụt――Zu――――――(Koku)――Pua.」**. Đổi: '「Aaaan……(hapu)――chụt――chụụụt,\\nchụt――zu――――――(koku)――pua.」' → '「Aaaan……(Hapu)――chụt――chụụụt,\\nchụt――Zu――――――(Koku)――Pua.」'.

**1041** — JP 「れりゅっ――ぺろっ――ちゅっ――ちゅむっ――\n（ぷあっ）、ん――ちゅうっ――ずちゅうっ――れるっ」; TW 「啾……啾嚕……啾……咕啾……噗哈……嗯……啾嚕、啾……」; old_vn (unif đã gộp) 「Reryu――pero――chụt――chụt――\n(pua), ưm――chụụt――zuchuu――rộp.」; **fix = 「Reryu――Pero――chụt――chụt――\n(Pua), ưm――chụụt――Zuchuu――rộp.」**. Đổi: '「Reryu――pero――chụt――chụt――\\n(pua),' → '「Reryu――Pero――chụt――chụt――\\n(Pua),'; 'ưm――chụụt――zuchuu――rộp.」' → 'ưm――chụụt――Zuchuu――rộp.」'.

**1053** — JP 「ちゅぶっ――ちゅばっ――ちゅむっ――ちゅううっ。\nふっ――はっ――ちゅむっ――ちゅぶっ――ぢゅるっ」; TW 「啾嚕……啾噗噗……啾啪……啾、啾、啾噗……啾嚕」; old_vn (unif đã gộp) 「Chụt――chụt――chụt――chụụụt.\nPhù――há――chụt――chụt――juru.」; **fix = 「Chụt――chụt――chụt――chụụụt.\nPhù――há――chụt――chụt――Juru.」**. Đổi: '「Chụt――chụt――chụt――chụụụt.\\nPhù――há――chụt――chụt――juru.」' → '「Chụt――chụt――chụt――chụụụt.\\nPhù――há――chụt――chụt――Juru.」'.

**1054** — JP 「れる――れりゅっ――んっ――ぢゅずっ――（こくっ）\nぷぁ――好き――好き、好き――ん――ちゅ――ちゅう」; TW 「啾嚕……啾嚕……咕嘟……蛤啊……好喜歡你……喜歡……喜歡……啾」; old_vn (unif đã gộp) 「Rộp――reryu――ưm――juzu――(koku)\npua――thích――thích lắm, thích――ưm――chụt――chụụt.」; **fix = 「Rộp――Reryu――ưm――Juzu――(Koku)\nPua――thích――thích lắm, thích――ưm――chụt――chụụt.」**. Đổi: '「Rộp――reryu――ưm――juzu――(koku)\\npua――thích――thích' → '「Rộp――Reryu――ưm――Juzu――(Koku)\\nPua――thích――thích'.

**1055** — JP 「れりゅうぅぅ――れりゅっ――ぬりゅっ――（こくっ）\nちゅっ――ちゅむっ――ちゅううっ――ちゅうううっ」; TW 「啾嚕嚕嚕……啾嚕……啾嚕……咕嘟。啾、啾嚕、啾嚕嚕……啾嚕嚕嚕」; old_vn (unif đã gộp) 「Reryuuuu――reryu――nuryu――(koku)\nchụt――chụt――chụụụt――chụụụụt.」; **fix = 「Reryuuuu――Reryu――Nuryu――(Koku)\nchụt――chụt――chụụụt――chụụụụt.」**. Đổi: '「Reryuuuu――reryu――nuryu――(koku)\\nchụt――chụt――chụụụt――chụụụụt.」' → '「Reryuuuu――Reryu――Nuryu――(Koku)\\nchụt――chụt――chụụụt――chụụụụt.」'.

**1068** — JP 「ん……ちゅっ――ちゅむっ――ちゅ……れ――りゅっ、\nれりゅっ――ちゅうっ――ちゅるるっ――れりゅうう」; TW 「嗯……啾、啾……啾嚕……啾嚕……啾嚕……啾……啾噗」; old_vn (unif đã gộp) 「Ưm……chụt――chụt――chụt……re――ryu,\nreryu――chụụt――chụt――reryuuu.」; **fix = 「Ưm……chụt――chụt――chụt……Re――Ryu,\nReryu――chụụt――chụt――Reryuuu.」**. Đổi: '「Ưm……chụt――chụt――chụt……re――ryu,\\nreryu――chụụt――chụt――reryuuu.」' → '「Ưm……chụt――chụt――chụt……Re――Ryu,\\nReryu――chụụt――chụt――Reryuuu.」'.

**1069** — JP 「ん……ふっ――ちゅぷっ――ちゅぱっ――\nちゅっ――ぢゅっ――ぢゅぷっ――ぢゅばっ――」; TW 「嗯……啾噗噗……啾啪……啾、啾、啾噗……」; old_vn (unif đã gộp) 「Ưm……phù――chụt――chụt――\nchụt――ju――jupu――juba――」; **fix = 「Ưm……phù――chụt――chụt――\nchụt――Ju――Jupu――Juba――」**. Đổi: '「Ưm……phù――chụt――chụt――\\nchụt――ju――jupu――juba――」' → '「Ưm……phù――chụt――chụt――\\nchụt――Ju――Jupu――Juba――」'.

**1688** — JP （すにゅっ――くちゅっ――ちゅくっ――ちゅっ）; TW （咕啾、咕啾、咕啾、咕啾）; old_vn (unif đã gộp) （Sunyu――kuchu――chuku――chụt）; **fix = （Sunyu――Kuchu――Chuku――chụt）**. Đổi: '（Sunyu――kuchu――chuku――chụt）' → '（Sunyu――Kuchu――Chuku――chụt）'.

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 6 dòng

**1495** — JP 「ひゃっ！？ あ、双鉄くんの、指の、おなか―ふぁっ、\nわたしの、おまんこ―入り口の、とこ―アウッ―」; TW 「咿呀！？啊，雙鐵君的，手指的，肚子——呼啊、正在、我的——小穴的，入口——啊嗚——」; old_vn (moan) 「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——Fa, đang ở, cửa mình——âm đạo, của em——au——」; **fix = 「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——Fa, đang ở, cửa mình——âm đạo, của em——Au——」**. Đổi: 'au' → 'Au'.

**1542** — JP 「ぁっ―んふ、ふっ―ありがと、双鉄。ボクとも\nちゃんと―ちゃんと―セックス、してくれて」; TW 「啊——嗯呼、呼——謝謝、雙鐵。謝謝你能和我——好好——做愛」; old_vn (unif đã gộp) 「A——ưm fu, fu——cảm ơn anh, Soutetsu. Vì đã\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」; **fix = 「A——ưm fu, Fu——cảm ơn anh, Soutetsu. Vì đã\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」**. Đổi: 'fu' → 'Fu'.

**1593** — JP 「ぅうっ―くっ―あっ―はっ―」; TW 「嗚嗚——嗯——啊——哈——」; old_vn (moan) 「Uu——ku——a——ha——」; **fix = 「Uu——Ku——a——Ha——」**. Đổi: 'ku' → 'Ku'; 'ha' → 'Ha'.

**1601** — JP 「んっ―はっ！ あっ！ 双鉄、双鉄―ボクは―\n次で―二番目で、今日は、いいから―ポーレットを」; TW 「嗯——哈！ 啊！ 雙鐵，雙鐵——我是——下一個，今天，就不用了——波萊特才」; old_vn (unif đã gộp) 「Ưm——ha! A! Soutetsu, Soutetsu——em thì——\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」; **fix = 「Ưm——Ha! A! Soutetsu, Soutetsu——em thì——\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」**. Đổi: 'ha!' → 'Ha!'.

**1604** — JP 「ん……ふふっ―どおお、双鉄？ おまんこの感触―\nんっ―ボクと、ポーレットで、結構違う？」; TW 「嗯……呼呼——怎麼樣，雙鐵？？ 小穴的觸感——嗯——我和波萊特的小穴，很不一樣嗎？」; old_vn (unif đã gộp) 「Ưm……fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」; **fix = 「Ưm……Fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\nưm——của em, và của Paulette, có khác nhau nhiều không?」**. Đổi: '「Ưm……fufu' → '「Ưm……Fufu'.

**1673** — JP 「ボク……も、だ―双鉄……んっ―はっ―あっ―\n今日は―なん、だかっ―いっつも、より、もっ―」; TW 「我……也、是——雙鐵……嗯——哈——啊——今天——總、覺得——比平時、更——」; old_vn (unif đã gộp) 「Em……cũng, vậy——Soutetsu……ưm——ha——a——\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」; **fix = 「Em……cũng, vậy——Soutetsu……ưm——Ha——a——\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」**. Đổi: 'ha' → 'Ha'.

#### lrれいな追加h_夜の花嫁修業.txt.toml — 2 dòng

**1087** — JP 「ひあっ――はっ！ はっ！ ふあっ！ んっ！\nくゅっ！ ふあっ！はっ！ は！ は！ はっ！ は！」; TW 「咿呀——哈！哈！呼啊！嗯！唔！呼啊！哈！哈！哈！哈！哈！」; old_vn (moan) 「Hia——ha! Ha! Fua! Ưm!\nKyu! Fua! Ha! Ha! Ha! Ha! Ha!」; **fix = 「Hia——Ha! Ha! Fua! Ưm!\nKyu! Fua! Ha! Ha! Ha! Ha! Ha!」**. Đổi: 'ha!' → 'Ha!'.

**1123** — JP 「あっ――く、はっ――しゃべられ、る、とっ」; TW 「啊——唔、哈——你一說話……」; old_vn (moan) 「A——Ku, ha——em mà, nói, chuyện, thì」; **fix = 「A——Ku, Ha——em mà, nói, chuyện, thì」**. Đổi: 'ha' → 'Ha'.

#### lr真闇追加h_赤ちゃん、欲しか.txt.toml — 5 dòng

**1013** — JP 「だめっ――やっ、めっ――イっちゃうの――やあっ！\nおねえ、ちゃん――双ちゃんっ――双ちゃんとぉぉ！」; TW 「不行——停——要丟了——不要！姐姐——想跟小雙——想跟你一起！」; old_vn (moan) "「Không được——dừng, lại——ra mất——yaa!\nChị——Sou-chan——cùng với Sou-chan cơ!」"; **fix = "「Không được——dừng, lại——ra mất——Yaa!\nChị——Sou-chan——cùng với Sou-chan cơ!」"**. Đổi: 'yaa!\\nChị' → 'Yaa!\\nChị'.

**1097** — JP 「ふあっ――んっっ――んくっ――く――はっ」; TW 「呼啊——嗯——嗯——呼——啊」; old_vn (unif đã gộp) "「Fua——ưm——Nku——Ku——ha.」"; **fix = "「Fua——ưm——Nku——Ku——Ha.」"**. Đổi: 'ha.」"' → 'Ha.」"'.

**1127** — JP 「はっ！ んぎゅ！ くっ――は――杭打ち、され、て、\nおね、ちゃんっ――刻印っ――双ちゃん――にっっ」; TW 「啊！嗯啊！像打樁一樣——姐姐——被小雙——刻上記號了」; old_vn (moan) "「Ha! Ngyu! Ku——ha——bị đóng cọc, rồi,\nchị——được khắc dấu ấn——của Sou-chan——rồi.」"; **fix = "「Ha! Ngyu! Ku——Ha——bị đóng cọc, rồi,\nchị——được khắc dấu ấn——của Sou-chan——rồi.」"**. Đổi: 'ha' → 'Ha'.

**1152** — JP 「ん……ぷあっ――チュッ――ちゅううっ――チュッ――\nちゅうっ――チュッ――ちゅっ――ちゅっ」; TW 「嗯……噗哈——啾——啾——啾——啾——啾——啾——啾」; old_vn (moan) "「Ưm……pua——chụt——chụụụt——chụt——\nChùn chụt——chụt——chụt——chụt.」"; **fix = "「Ưm……Pua——chụt——chụụụt——chụt——\nChùn chụt——chụt——chụt——chụt.」"**. Đổi: '"「Ưm……pua' → '"「Ưm……Pua'.

**1292** — JP 「真闇姉も、だっ――くっ――はっ――\nじゅくじゅくで、どろ、どろ、で――」; TW 「真闇姐——你也一樣——唔——哈——濕濕的——滑滑的——」; old_vn (moan) "「Chị Mayami cũng, vậy——Ku——ha——\nƯớt sũng, nhầy, nhụa, rồi——」"; **fix = "「Chị Mayami cũng, vậy——Ku——Ha——\nƯớt sũng, nhầy, nhụa, rồi——」"**. Đổi: 'ha' → 'Ha'.

#### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 1 dòng

**1144** — JP 「う……ん。ふ、ふっ――ありがと、双鉄」; TW 「嗯……呼、呼——謝謝你，雙鐵」; old_vn (moan) 「Ư……m. Fu, fu——cảm ơn anh, Soutetsu.」; **fix = 「Ư……m. Fu, Fu——cảm ơn anh, Soutetsu.」**. Đổi: 'fu' → 'Fu'.

#### lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml — 19 dòng

**1368** — JP 「ひゃぐっ！ んっ――あっ！ がまんっ！ がまんっ！\nふあっ！？ むりっ――これっ、むりっ――げんかいっ」; TW 「來了！馬上來了！真的要來了！求你了！我們一起！一起高潮！！」; old_vn (moan) 「Hyagu! Ưm——ah! Nhịn! Cố nhịn!\nFua!? Không được——cái này, không được——đến giới hạn rồi」; **fix = 「Hyagu! Ưm——Ah! Nhịn! Cố nhịn!\nFua!? Không được——cái này, không được——đến giới hạn rồi」**. Đổi: 'ah!' → 'Ah!'.

**1433** — JP 「んきゅっ！！？ ふっ――あっ――もみじっ！！\nうごくっ――っっと――あっ――ふうううんっ！！！」; TW 「呼啊啊！啊！啊啊？！！這太棒了！嗯，唔——太酸爽了——插得好深！！」; old_vn (moan) 「Nkyu!!? Phù——ah——Momiji!!\nĐang chuyển động——kìa——ah——Fuuuuun!!!」; **fix = 「Nkyu!!? Phù——Ah——Momiji!!\nĐang chuyển động——kìa——Ah——Fuuuuun!!!」**. Đổi: 'ah' → 'Ah'; 'ah' → 'Ah'.

**1519** — JP 「はあっ――はあっ――んくっ――ンッ――（ごくっ）\nふふっ――ひよこ――お主はいつも――かわいい、の！」; TW 「嗯——哈——蛤啊——這東西——真的是，唔，太粗了」; old_vn (moan) 「Haa——haa——Nku——Ưm——(ực)\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」; **fix = 「Haa——Haa——Nku——Ưm——(ực)\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」**. Đổi: 'haa' → 'Haa'.

**1556** — JP 「ふっ――んっ――はっ――あ……ふあっ――（ごくっ）、\n紅葉も――余裕、あるよう、には――見えません、が！」; TW 「嗯，呼呼？剛才那副從容的表情哪裡去了？剛剛是不是丟了？」; old_vn (moan) 「Phù——ưm——ha——a……Fua——(ực),\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」; **fix = 「Phù——ưm——Ha——a……Fua——(ực),\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」**. Đổi: 'ha' → 'Ha'.

**1710** — JP 「ん……くっ――はぁっ――はあ――（ごくっ）――\nわらわの、[ほと,1]女陰、から、溢れ出しておる――液体、は」; TW 「比平時箍得還要緊……真是未免讓人有些嫉妒。被奧莉薇女士盯著看竟然會讓你如此亢奮」; old_vn (moan) 「Ưm……Ku——haa——haa——(ực)——\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」; **fix = 「Ưm……Ku——Haa——Haa——(ực)——\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」**. Đổi: 'haa' → 'Haa'; 'haa' → 'Haa'.

**1773** — JP 「はっ、あっ――んっ――ふうっ――\nンッ――フッ――ああっ」; TW 「紅葉？奧莉薇女士又發問了」; old_vn (moan) 「Ha, ah——ưm——Phùù——\nƯm——Phù——Aah」; **fix = 「Ha, Ah——ưm——Phùù——\nƯm——Phù——Aah」**. Đổi: 'ah' → 'Ah'.

**1804** — JP 「んうっっ――くっ――んっ――ああっ――あっ」; TW 「蛤啊，蛤啊，蛤啊，蛤啊」; old_vn (moan) 「Ưm——Ku——ưm——aah——ah」; **fix = 「Ưm——Ku——ưm——Aah——Ah」**. Đổi: 'aah' → 'Aah'; 'ah」' → 'Ah」'.

**1887** — JP 「か……はっ――あっ！ 待てと、申すに……んうっ！\nなにも――そこ、まで――男の、ように――ひぎっ！？」; TW 「那麼粗的東西……Ａｍａｚｉｎｇ……真的插進去了……陰道口整個被撐大了，好厲害」; old_vn (moan) 「Ka……ha——ah! Ta bảo đợi đã, mà……Ưm!\nĐâu cần——đến, mức đó——như đàn ông, vậy——Higi!?」; **fix = 「Ka……Ha——Ah! Ta bảo đợi đã, mà……Ưm!\nĐâu cần——đến, mức đó——như đàn ông, vậy——Higi!?」**. Đổi: '「Ka……ha' → '「Ka……Ha'; 'ah!' → 'Ah!'.

**2098** — JP 「はあっ――はあっ――はあっ――はあっ――んっ―――\nわらわっっ――こんなっ――あさましい――ひっ、ぐっ」; TW 不死鳥博士撐開陰道口，內部一覽無餘。陰道口就好像痙攣一般不斷地在顫抖。; old_vn (moan) 「Haa——Haa——Haa——Haa——Ưm——\nTa——Bộ dạng——đáng xấu hổ, này——Hi, gu」; **fix = 「Haa——Haa——Haa——Haa——Ưm——\nTa——Bộ dạng——đáng xấu hổ, này——Hi, Gu」**. Đổi: 'gu」' → 'Gu」'.

**2146** — JP 「はあっ――っっ――ふっ――ふあっ――きもち、いっ！\nん――おくっ、にっ――ごちゅ、ごちゅ――あた、って」; TW 兩人的動作漸漸開始同化為一體。就好像彼此合二為一了一般——; old_vn (moan) 「Haa——ư——phù——Fua——sướng, quá!\nƯm——ở sâu, bên trong——Gochu, gochu——chạm, vào rồi」; **fix = 「Haa——ư——phù——Fua——sướng, quá!\nƯm——ở sâu, bên trong——Gochu, Gochu——chạm, vào rồi」**. Đổi: 'gochu' → 'Gochu'.

**2168** — JP 「ん――はっ――はあっ――これっ――はっ――やはり、\nくっ――ふと、すぎ――るっ――かもっ――」; TW 太壯觀了，愛液和汗水弄得身體都黏糊糊的。兩個人的臉還紅通通的，連乳頭都立起來了——; old_vn (moan) 「Ưm——ha——haa——cái này——ha——quả nhiên,\nKu——to, quá——mất, rồi——」; **fix = 「Ưm——Ha——Haa——cái này——Ha——quả nhiên,\nKu——to, quá——mất, rồi——」**. Đổi: 'ha' → 'Ha'; 'haa' → 'Haa'; 'ha' → 'Ha'.

**2220** — JP 「はぁっ――んっ――感じる――いつも、より――くっ\nこのような――異常な――状況――んっ……は、あっ」; TW 手指的每一次輕撫，電車公主的皮膚都會隨之慢慢染上紅暈。看起來就和真的“紅葉”一樣，非常漂亮。; old_vn (moan) 「Haa——ưm——cảm nhận được——hơn, mọi khi——Ku\nTình trạng——bất thường——thế này——ưm……ha, ah」; **fix = 「Haa——ưm——cảm nhận được——hơn, mọi khi——Ku\nTình trạng——bất thường——thế này——ưm……Ha, Ah」**. Đổi: 'ưm……ha,' → 'ưm……Ha,'; 'ah」' → 'Ah」'.

**2279** — JP 「あ……ふっ――んっ――ふあっ、あっ」; TW 眼看著假陽具就要插進電車公主的陰道口，不會斷掉嗎？！剛想到這，沒想到它一點點進去——; old_vn (moan) 「A……phù——ưm——Fua, ah」; **fix = 「A……phù——ưm——Fua, Ah」**. Đổi: 'ah」' → 'Ah」'.

**2334** — JP 「んっ――いきなり、挿入――ディルド、使うのか、と、\nあっ――思うて、おった、が――くっ――ふ、あっ」; TW 電車公主和不死鳥博士的胯部……呃，是大陰唇！大陰唇和大陰唇親在了一起。; old_vn (moan) 「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\nah——cứ nghĩ, là vậy, nhưng——Ku——Fua」; **fix = 「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\nAh——cứ nghĩ, là vậy, nhưng——Ku——Fua」**. Đổi: 'dildo,\\nah' → 'dildo,\\nAh'.

**2346** — JP 「ふぁっ――あっ――あっ――あっ」; TW 電車公主的身體高高翹起，不死鳥博士則是蜷縮起身子。; old_vn (unif đã gộp) 「Fa——ah——ah——ah」; **fix = 「Fa——Ah——Ah——Ah」**. Đổi: 'ah' → 'Ah'; 'ah' → 'Ah'; 'ah」' → 'Ah」'.

**2352** — JP 「はふっ――んっ――きゅっ！ ふあっ！ ああっ！\nなかっ！ [なか,1]膣内っっ！ ずりゅって！ みちみちっ！」; TW 電車公主開始轉動腰肢。不死鳥博士也跟著節奏扭腰。; old_vn (moan) 「Hafu——ưm——kyu! Fua! Aah!\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」; **fix = 「Hafu——ưm——Kyu! Fua! Aah!\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」**. Đổi: 'kyu!' → 'Kyu!'.

**2435** — JP 「ひあっ！？ あっ、やっ――みられてっ！ わらわっ！\nイッってる――性器っ――ひらかれ、てっ――んうっ！」; TW （抽出）; old_vn (moan) 「Hia!? Ah, ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ưm!」; **fix = 「Hia!? Ah, Ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ưm!」**. Đổi: 'ya' → 'Ya'.

**2449** — JP 「か……はっ――！！！！？」; TW （直搗黃龍）; old_vn (moan) 「Ka……ha——!!!!?」; **fix = 「Ka……Ha——!!!!?」**. Đổi: '「Ka……ha' → '「Ka……Ha'.

**2457** — JP 「ふぁっ――あっ――いいっ――イイっ！ ふっ――あ、\nおねがいっ――このまま――このまま――このままあっ」; TW （進進出出）; old_vn (unif đã gộp) 「Fa——ah——sướng——sướng quá! Phù——ah,\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」; **fix = 「Fa——Ah——sướng——sướng quá! Phù——Ah,\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」**. Đổi: 'ah' → 'Ah'; 'ah,\\nXin' → 'Ah,\\nXin'.

#### lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml — 11 dòng

**1604** — JP 「ちがっ──んんっ──ふっ──あっ──にぃに──\nにぃに、が──いつも──よりっ──」; TW 「不是我——嗯嗯——呼——啊——是阿哥——阿哥比平時要粗得多」; old_vn (moan) 「Không phải── ưmm── phu── a── anh hai──\nAnh hai, so với── mọi khi──」; **fix = 「Không phải── ưmm── Phu── a── anh hai──\nAnh hai, so với── mọi khi──」**. Đổi: 'phu──' → 'Phu──'.

**1678** — JP 「ひゃうっ──んっ──ふあっ──あっ──\nあっ──あっ──あっ──ああっ──」; TW 「呀啊——嗯——呼啊——啊—— 啊——啊——啊——啊啊——」; old_vn (unif đã gộp) 「Hyau── ưm── Fua── a──\nA── a── a── aa──」; **fix = 「Hyau── ưm── Fua── a──\nA── a── a── Aa──」**. Đổi: 'aa──」' → 'Aa──」'.

**1739** — JP 「ふあっ！ あっ！！ あっ──ああああっ！！！！」; TW 「呼啊！啊！！啊——啊啊啊啊！！！！」; old_vn (unif đã gộp) 「Fua! A!! A── aaaa!!!!」; **fix = 「Fua! A!! A── Aaaa!!!!」**. Đổi: 'aaaa!!!!」' → 'Aaaa!!!!」'.

**1741** — JP 「ふやっ──なにっ、これっ──あちゅいのっ──\nおなか──おまた──どろって──ふっ──あっ」; TW 「呼啊，這是什麼？好熱的東西進到肚子裡面去了，胯部黏糊糊的，呼——啊」; old_vn (moan) 「Fuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── phu── aƯ」; **fix = 「Fuya── gì thế, này── nóng quá──\nBụng── vùng kín── nhão nhoét── Phu── aƯ」**. Đổi: 'phu──' → 'Phu──'.

**1773** — JP 「はっっ──あっ──ふっ──ふあっ──」; TW 「哈——啊——呼——呼啊——」; old_vn (unif đã gộp) 「Hà── a── phu── Fua──」; **fix = 「Hà── a── Phu── Fua──」**. Đổi: 'phu──' → 'Phu──'.

**1811** — JP 「あ……ん──ちゅっ──ちゅむっ──ちゅっ──ふ\n……ん……れるっ──れりゅっ──れろおおっ──ぷあ」; TW 「啊……嗯——啾——啾唔——啾——呼……嗯……咧溜——滋溜溜——噗啊」; old_vn (unif đã gộp) 「A……ưm──chụt──chụt──chụt──fu\n……ưm……liếm──liếm──liếmmm──Pua」; **fix = 「A……ưm──chụt──chụt──chụt──Fu\n……ưm……liếm──liếm──liếmmm──Pua」**. Đổi: '「A……ưm──chụt──chụt──chụt──fu\\n……ưm……liếm──liếm──liếmmm──Pua」' → '「A……ưm──chụt──chụt──chụt──Fu\\n……ưm……liếm──liếm──liếmmm──Pua」'.

**1855** — JP 「んひゅううううううううっっっっ！」; TW 「嗯唔唔——！」; old_vn (moan) 「Ưm hyuuuuuuuuu!」; **fix = 「Ưm Hyuuuuuuuuu!」**. Đổi: 'hyuuuuuuuuu!」' → 'Hyuuuuuuuuu!」'.

**1857** — JP 「んきゅ！ ふあっ！ あ──ずりゅって──ずる、って──やぁぁあっ──にぃに──ぜんぶ、いっちゃうぅ」; TW 「嗯唔！呼啊！啊——滋溜——滋嚕的好大聲——呀啊啊啊——阿哥——全都進來了」; old_vn (unif đã gộp) 「Ưm kyu! Fua! A── trượt── tuột, ra── aaaa── anh hai── vào hết, mất」; **fix = 「Ưm kyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」**. Đổi: 'aaaa──' → 'Aaaa──'.

**1901** — JP 「ぷあっ──ふふっ、だって。みくろ」; TW 「噗啊——呵呵，阿哥是這麼說的哦。美玖路」; old_vn (unif đã gộp) 「Pua──fufu, anh ấy bảo thế kìa. Mikuro.」; **fix = 「Pua──Fufu, anh ấy bảo thế kìa. Mikuro.」**. Đổi: '「Pua──fufu,' → '「Pua──Fufu,'.

**2200** — JP 「はあっ──ふうっ──はああっ──ふううっ」; TW 「蛤啊——呼——蛤啊——呼」; old_vn (moan) 「Hàà── phuu── hààà── phuuuƯ」; **fix = 「Hàà── Phuu── hààà── phuuuƯ」**. Đổi: 'phuu──' → 'Phuu──'.

**2201** — JP 「はあっ──ん、ふっ──はひゅっ──くっふっ」; TW 「蛤啊——嗯、呼——哈——唔呼」; old_vn (moan) 「Hàà── ưm, phu── ha hyu── kufuƯ」; **fix = 「Hàà── ưm, Phu── ha Hyu── kufuƯ」**. Đổi: 'phu──' → 'Phu──'; 'hyu──' → 'Hyu──'.

#### ふかみh1_ともはり練習.txt.toml — 5 dòng

**987** — JP 「ふぁっ――あっ――わたしの――おまんこっ――\n双鉄、さんの――おくちっ――おくち、でっ――」; TW 「哇……啊……我的……那裡……正在被……雙鐵先生的嘴巴……嘴巴……」; old_vn (unif đã gộp) 「Fa——ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」; **fix = 「Fa——Ah——của em——âm đạo——\nMiệng của——anh Soutetsu——bằng miệng——」**. Đổi: 'ah' → 'Ah'.

**992** — JP 「ふぁ、あっ――べろ……あったか……いっ……んうっ」; TW 「哇，啊……舌頭……好暖……呀……嗯」; old_vn (unif đã gộp) 「Fu, ah——lưỡi……ấm……quá……ưm.」; **fix = 「Fu, Ah——lưỡi……ấm……quá……ưm.」**. Đổi: 'ah' → 'Ah'.

**1039** — JP 「好き……好きって……双鉄さんが、わたしのことを――\nすでに好き、って……ふあ、ぁっ」; TW 「喜歡……喜歡……雙鐵先生已經……喜歡上我了……哇」; old_vn (unif đã gộp) 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……Fu, ah.」; **fix = 「Thích……thích……Anh Soutetsu, đối với em——\nĐã thích em rồi, sao……Fu, Ah.」**. Đổi: 'ah.」' → 'Ah.」'.

**1048** — JP 「ん……はっ――ふあぁ……ぷあっ」; TW 「嗯……啊……哇……呼」; old_vn (moan) 「Ưm……ha——Fuaa……Pua」; **fix = 「Ưm……Ha——Fuaa……Pua」**. Đổi: '「Ưm……ha' → '「Ưm……Ha'.

**1049** — JP 「ん……あっ――なか……が――おされ――て――\nふあっ――ひっ――めく、れる……みたい――でっ」; TW 「嗯……啊……裡面……被……推著……哇……呀……像是……在轉……」; old_vn (moan) 「Ưm……ah——bên trong……bị đẩy——vào——\nFua——hi——như bị, lộn ngược……vậy——」; **fix = 「Ưm……Ah——bên trong……bị đẩy——vào——\nFua——hi——như bị, lộn ngược……vậy——」**. Đổi: '「Ưm……ah' → '「Ưm……Ah'.

#### ふかみh2_homesweethome.txt.toml — 9 dòng

**973** — JP 「ひゃっ！？ やっ――双鉄さんっ！？\nパンツ、わたしの、パンツ――食い……込ん――ふあっ」; TW 「呀！討厭……雙鐵先生！內褲，我的內褲……你按進來了……啊」; old_vn (moan) 「Hya!? Ya——anh Soutetsu!?\nQuần lót, quần lót của em——lún……vào——fua」; **fix = 「Hya!? Ya——anh Soutetsu!?\nQuần lót, quần lót của em——lún……vào——Fua」**. Đổi: 'fua」' → 'Fua」'.

**975** — JP 「ひあっ――あっ――んっ――ん――ふうっ――」; TW 「呀，啊，嗯，嗯，呼」; old_vn (moan) 「Hia——ah——ưm——ưm——phù ư——」; **fix = 「Hia——Ah——ưm——ưm——phù ư——」**. Đổi: 'ah' → 'Ah'.

**983** — JP 「ぱあっ！？ ま、またグイって――んっ！ あ――\nパンツでっ……感じちゃう、とかっ――あっ――やぁっ」; TW 「哇？！又、又按……嗯！啊……被內褲……弄出感覺了……啊……不要……」; old_vn (moan) 「Paa!? L, lại ấn mạnh nữa——ưm! A——\nBằng quần lót……mà cũng cảm thấy sướng, sao——ah——yaa」; **fix = 「Paa!? L, lại ấn mạnh nữa——ưm! A——\nBằng quần lót……mà cũng cảm thấy sướng, sao——Ah——Yaa」**. Đổi: 'ah' → 'Ah'; 'yaa」' → 'Yaa」'.

**988** — JP 「ぃ――っ――～～～っ！？ んっ――ふっ――\nふぅっ――ふ――んっ！ んっ――ふっ――ひひゅっ」; TW 「唔……唔，唔？！嗯，呼，呼，呼，嗯！嗯，呼，唔」; old_vn (moan) 「Ư——ư——~~~ư!? Ưm——phù——\nphù——phù——ưm! Ưm——phù——hihyu」; **fix = 「Ư——ư——~~~ư!? Ưm——phù——\nphù——phù——ưm! Ưm——phù——Hihyu」**. Đổi: 'hihyu」' → 'Hihyu」'.

**1011** — JP 「あ……あー……あ～っ――あ～～っ！」; TW 「啊……哦……噢……噢！」; old_vn (moan) 「A…… aa…… aa~—— aaa~~!」; **fix = 「A…… Aa…… Aa~—— Aaa~~!」**. Đổi: 'aa……' → 'Aa……'; 'aa~' → 'Aa~'; 'aaa~~!」' → 'Aaa~~!」'.

**1013** — JP 「ぁっ――はっ――んっ――んっ――んっ！！」; TW 「啊……啊，嗯，嗯，嗯！！」; old_vn (moan) 「A——ha——ưm——ưm——ưm!!」; **fix = 「A——Ha——ưm——ưm——ưm!!」**. Đổi: 'ha' → 'Ha'.

**1025** — JP 「ふぁっ――んっ――ぢゅっ――ぢゅちゅるっ――ぐ――\nあっ――ほーへふ、ふぁ――ほーへふ、ふぁんっ！！」; TW 「啊，嗯，啾，啾，唔，啊，唔唔唔，唔唔唔！！」; old_vn (moan) 「Fa——ưm——chụt——chụt rột——gu——\nAh——ho he fu, fa——ho he fu, fan!!」; **fix = 「Fa——ưm——chụt——chụt rột——Gu——\nAh——ho he fu, Fa——ho he fu, Fan!!」**. Đổi: 'gu' → 'Gu'; 'fa' → 'Fa'; 'fan!!」' → 'Fan!!」'.

**1032** — JP 「ん……ん、ちゅ――ちゅるっ――んっ――――――\nごくんっ……ん～～～――ぷはっ」; TW 「嗯……嗯，啾，啾，嗯……咕咚……嗯……噗哈」; old_vn (moan) 「Ưm……ưm, chụt——chụt——ưm——————\nỰc……ưm~~~——puha」; **fix = 「Ưm……ưm, chụt——chụt——ưm——————\nỰc……ưm~~~——Puha」**. Đổi: 'puha」' → 'Puha」'.

**1034** — JP 「ん……ふ、あっ――んっ――ふぁひ……んうっ――んっ、\nほーへふ……ふぁん……うくっ――んっ！」; TW 「嗯……好……嗯……好……嗯，嗯，唔唔……嗯……嗯！」; old_vn (unif đã gộp) 「Ưm……Fu, ah——ưm——fahi……ưm ư——ưm,\nHo he fu……fan……ư ku——ưm!」; **fix = 「Ưm……Fu, Ah——ưm——Fahi……ưm ư——ưm,\nHo he fu……Fan……ư ku——ưm!」**. Đổi: 'ah' → 'Ah'; 'fahi……ưm' → 'Fahi……ưm'; 'fu……fan……ư' → 'fu……Fan……ư'.

#### れいなh1_おかあさんのレッスン.txt.toml — 1 dòng

**1527** — JP 「ひあッ――んっ――ひゃっ――あっ――\nそうてつ――さんっ――そおてつ――さぁん」; TW 「蛤啊……啊……啊……雙鐵先生……雙鐵先生……」; old_vn (moan) 「Hia——ưm——hya——a——\nAnh——Soutetsu——anh——Soutetsu~」; **fix = 「Hia——ưm——Hya——a——\nAnh——Soutetsu——anh——Soutetsu~」**. Đổi: 'hya' → 'Hya'.

#### れいなh2_おもらし防止大作戦.txt.toml — 3 dòng

**1064** — JP 「きゅふうっ！ んっ――ふううううっ――んっ！\nそこ――ざらざら、の――はっ――きもち――い、いっ」; TW 「啊嗯！嗚嗚嗚嗚……啊嗯！那裡……澀澀的……好舒服……」; old_vn (moan) 「Kyufuu! Ưm——fuuuuu——ưm!\nChỗ đó——nham nhám——ha——sướng——quá」; **fix = 「Kyufuu! Ưm——Fuuuuu——ưm!\nChỗ đó——nham nhám——Ha——sướng——quá」**. Đổi: 'fuuuuu' → 'Fuuuuu'; 'ha' → 'Ha'.

**1183** — JP 「ふぇっ――ふあっ――はっ――はぅぅ――」; TW 「蛤啊……蛤啊……」; old_vn (moan) 「Fue——Fua——ha——hauu——」; **fix = 「Fue——Fua——Ha——Hauu——」**. Đổi: 'ha' → 'Ha'; 'hauu' → 'Hauu'.

**1185** — JP 「ふぁっ――はあっ――あっ――ふぁぁっ――」; TW 「蛤啊、蛤啊、啊啊啊啊」; old_vn (moan) 「Fa——haa——a——Faa——」; **fix = 「Fa——Haa——a——Faa——」**. Đổi: 'haa' → 'Haa'.

#### れいなh3_おもらし自由化大作戦.txt.toml — 8 dòng

**1061** — JP 「んぶっ――むっ――んっ――んんっ――むっ――\nぐっ――ぐうっ――んっうっ――」; TW 「啊嗯……嗚嗚……啾嚕……嗯……嗚嗚嗚……啊嗯……」; old_vn (moan) 「Nbu——mu——ưm——ưmm——mu——\nGu——guu——ưm u——」; **fix = 「Nbu——Mu——ưm——ưmm——Mu——\nGu——Guu——ưm u——」**. Đổi: 'mu' → 'Mu'; 'mu' → 'Mu'; 'guu' → 'Guu'.

**1085** — JP 「ずっ――ずうううううううっ――ずじゅっ！\n――じゅるるるる～～――――ん～ッ――ごくっ」; TW 「啾、啾嚕嚕嚕！啾嚕嚕嚕……嗯……咕嘟……」; old_vn (moan) 「Zu——zuuuuuuuu——zuju!\n——Jururururu~~————n~——goku」; **fix = 「Zu——Zuuuuuuuu——Zuju!\n——Jururururu~~————n~——Goku」**. Đổi: 'zuuuuuuuu' → 'Zuuuuuuuu'; 'zuju!\\n' → 'Zuju!\\n'; 'goku」' → 'Goku」'.

**1089** — JP 「れるっ――ぺろっ――ちゅっ――ちゅううっ――\nんっ……あむ～～～～んっ――」; TW 「啾嚕……啾嚕……嗯……啊嗯……」; old_vn (unif đã gộp) 「Rộp——liếm——chụt——chụt——\nƯm……ammmmm——」; **fix = 「Rộp——liếm——chụt——chụt——\nƯm……Ammmmm——」**. Đổi: '\\nƯm……ammmmm' → '\\nƯm……Ammmmm'.

**1091** — JP 「んむっ――んふっ――れるっ――るっ――\nちゅっ――ちゅむ――ちゅるっ――ちゅううううっ」; TW 「啾嚕嚕……啾嚕……咕啾，啾嚕、啾啾……啾嚕嚕嚕」; old_vn (unif đã gộp) 「Ưm——nfu——rộp——rộp——\nChụt——chụt——chụt——chụtttttt」; **fix = 「Ưm——Nfu——rộp——rộp——\nChụt——chụt——chụt——chụtttttt」**. Đổi: 'nfu' → 'Nfu'.

**1092** — JP 「ンぶっ――むううっ――んっ――ふっ――んっ――\n（スヒっ）――（スヒっ）――んふふぅぅぅ～」; TW 「嗚……嗯……啊嗯……啊……呼……呼……」; old_vn (moan) 「Nbu——muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——nfufuuuu~」; **fix = 「Nbu——Muuu——ưm——phù——ưm——\n（Suhi）——（Suhi）——Nfufuuuu~」**. Đổi: 'muuu' → 'Muuu'; 'nfufuuuu~」' → 'Nfufuuuu~」'.

**1099** — JP 「ンムッ――むっ――んううううっ～～～～っ！」; TW 「嗯……嗚嗚！」; old_vn (moan) 「Nmu——mu——uuuu~~~~Ư!」; **fix = 「Nmu——Mu——uuuu~~~~Ư!」**. Đổi: 'mu' → 'Mu'.

**1195** — JP 「ふあっ――あちゅ――んっ！ ひゃっ――\nあっ――ああっっ――あっ――」; TW 「蛤啊……啊……啊嗯……啊、啊啊……啊啊啊」; old_vn (moan) 「Fua——achu——ưm! Hya——\nA——aa——a——」; **fix = 「Fua——Achu——ưm! Hya——\nA——Aa——a——」**. Đổi: 'achu' → 'Achu'; 'aa' → 'Aa'.

**1196** — JP 「ふぁっ――あっ――んっ――んっ――んむっ――\nんくっ――ごくっ――ごくっ――――――ごくんっ」; TW 「蛤啊……啊……嗯、嗯啊……咕嘟、咕嘟、咕嘟……」; old_vn (moan) 「Fa——a——ưm——ưm——nmu——\nNku——goku——goku——————gokun」; **fix = 「Fa——a——ưm——ưm——Nmu——\nNku——Goku——Goku——————Gokun」**. Đổi: 'nmu' → 'Nmu'; 'goku' → 'Goku'; 'goku' → 'Goku'; 'gokun」' → 'Gokun」'.

#### れいなh4_ふたりっきりのハロウィン.txt.toml — 7 dòng

**2000** — JP 「ふゆっ――んっ――ふあっ――あ――ひゅっ、\nんっ――あ――そうてつさん――そうてつ、さぁん」; TW 「啊嗯……嗯……蛤啊……啊，啊嗯……雙鐵先生——雙鐵先生」; old_vn (moan) 「Fuyu——ưm——Fua——a——hyu,\nưm——a——anh Soutetsu——anh Soutetsu」; **fix = 「Fuyu——ưm——Fua——a——Hyu,\nưm——a——anh Soutetsu——anh Soutetsu」**. Đổi: 'hyu,\\nưm' → 'Hyu,\\nưm'.

**2015** — JP 「きゅふっ――んっ！ ～～～っ！ ふっ――く――\nんっ――だめ――ま、だっ――おまんこ、だめえっ」; TW 「啊嗯！啊啊啊……嗚嗚……啊啊啊……小穴……還不能高潮……」; old_vn (moan) 「Kyufu——ưm! ~~~! Fu——ku——\nưm——không được——vẫn, chưa——chỗ đó, chưa được」; **fix = 「Kyufu——ưm! ~~~! Fu——Ku——\nưm——không được——vẫn, chưa——chỗ đó, chưa được」**. Đổi: 'ku' → 'Ku'.

**2047** — JP 「ん……ちゅっ――ちゅうっ――ちゅむっ――ん……\nしゅき……んっ――ちゅっ――ほうへふ……はぁん」; TW 「嗯……啾……啾嚕……愛你……嗯……啾……哈嗯」; old_vn (moan) 「Ưm……chụt——chụụt——chumu——ưm……\nyêu……ưm——chụt——Soutetsu……haan」; **fix = 「Ưm……chụt——chụụt——Chumu——ưm……\nyêu……ưm——chụt——Soutetsu……Haan」**. Đổi: 'chumu' → 'Chumu'; 'Soutetsu……haan」' → 'Soutetsu……Haan」'.

**2088** — JP 「えへ、へぇ――れいな――ほめ、られ、て――ふっ\n――ふあっ――あ――うれしい、です――よぉ――ん」; TW 「嘿嘿……玲奈被誇獎啦……啊嗯……蛤啊、啊……好開心」; old_vn (moan) 「Ehe, he~——Reina——được, khen——Fu\n——Fua——a——vui, lắm——ạ~——ưm」; **fix = 「Ehe, He~——Reina——được, khen——Fu\n——Fua——a——vui, lắm——ạ~——ưm」**. Đổi: 'he~' → 'He~'.

**2457** — JP 「ふあ……ぁ……ぁ……やぁ――んっ――\nおまんこ――せいえき――あふれ――ちゃって、る」; TW 「蛤啊啊啊、啊啊啊……小穴裡的……精液流出來了……」; old_vn (moan) 「Fua……a……a……ya——ưm——\nchỗ đó——tinh dịch——đang tràn——ra ngoài」; **fix = 「Fua……a……a……Ya——ưm——\nchỗ đó——tinh dịch——đang tràn——ra ngoài」**. Đổi: '「Fua……a……a……ya' → '「Fua……a……a……Ya'.

**2458** — JP 「ふあああぁぁぁ――れいな、そうてつ、さんの――\nおくち、に――んきゅっ！？ ふああ――あんっ！！」; TW 「蛤啊啊啊啊……玲奈……往雙鐵先生的嘴裡……啊啊啊啊！！」; old_vn (moan) 「Fuaaaaaa——Reina, vào miệng——\nanh Soutetsu——nkyu!? Fuaa——an!!」; **fix = 「Fuaaaaaa——Reina, vào miệng——\nanh Soutetsu——Nkyu!? Fuaa——an!!」**. Đổi: 'nkyu!?' → 'Nkyu!?'.

**2459** — JP 「ふあっ！ あっ！ きもち、いっ――きもち、いい。\nんっ――あっ――はっ――あっ――ふあっ――あっ」; TW 「蛤啊！啊！好舒服……好舒服。啊啊啊、啊啊……蛤啊啊」; old_vn (moan) 「Fua! A! Sướng, quá——sướng, quá.\nƯm——a——ha——a——Fua——aƯ」; **fix = 「Fua! A! Sướng, quá——sướng, quá.\nƯm——a——Ha——a——Fua——aƯ」**. Đổi: 'ha' → 'Ha'.

#### グランドリライト05_れいな.txt.toml — 1 dòng

**1922** — JP 「えっへへー。れいな、お役にたてたの……\nふぁ……うれしい……です、よぉ」; TW 「嘿嘿嘿，玲奈幫上忙了……呼……好開心呀……」; old_vn (unif đã gộp) 「Ehehe~. Reina, giúp ích được cho anh……\nfa……vui lắm……ạ~」; **fix = 「Ehehe~. Reina, giúp ích được cho anh……\nFa……vui lắm……ạ~」**. Đổi: 'anh……\\nfa……vui' → 'anh……\\nFa……vui'.

#### ハチロクh3_磨き洗い.txt.toml — 2 dòng

**1084** — JP 「ぷあっ――あっ――はっ――\nはい、双鉄、さまっ……ですが」; TW 「噗啊——啊——哈——是的，雙鐵少爺……不過」; old_vn (moan) 「Pua——a——ha——\nVâng, ngài Soutetsu……nhưng mà」; **fix = 「Pua——a——Ha——\nVâng, ngài Soutetsu……nhưng mà」**. Đổi: 'ha' → 'Ha'.

**1677** — JP 僕の手の中、すずはほうっと幸せそうな息を吐き、\nやがて、うふふと小さく微笑む。; TW 鈴在我的懷抱中幸福地呼氣，不久，又輕輕地微笑起來。; old_vn (moan) Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "ufufu" nhỏ nhẹ.; **fix = Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\nrồi mỉm cười "Ufufu" nhỏ nhẹ.**. Đổi: '"ufufu"' → '"Ufufu"'.

#### ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml — 2 dòng

**1000** — JP 「んひいいいいいいいいっ！！？」; TW 「嗯咿——！！？」; old_vn (moan) 「Ư iiiiiiiii!!?」; **fix = 「Ư Iiiiiiiii!!?」**. Đổi: 'iiiiiiiii!!?」' → 'Iiiiiiiii!!?」'.

**1121** — JP 「そ、双鉄さまぁっ――ふやっ――これっ――\nしゅごっ――くひいいいっんっ！」; TW 「雙、雙鐵少爺——嗚呀——這下——好——好厲害嗯！」; old_vn (unif đã gộp) 「N, ngài Soutetsu——fuya——cái này——\ntuyệt quá——kư hi i i i ưm!」; **fix = 「N, ngài Soutetsu——Fuya——cái này——\ntuyệt quá——kư hi i i i ưm!」**. Đổi: 'fuya' → 'Fuya'.

#### ハチロクh5_おだいどこしごと.txt.toml — 5 dòng

**992** — JP 「や……パンツの、上から、なのに――んっ――はっ――やっ――そんなに優しく――クリトリ、ス――っ！」」; TW 「呀……明明隔著內褲——哈——哎——那麼溫柔地——摸陰蒂——！」」; old_vn (moan) 「Ya……mặc dù, cách lớp quần lót——ưm——hà——ya——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」; **fix = 「Ya……mặc dù, cách lớp quần lót——ưm——hà——Ya——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」**. Đổi: 'ya' → 'Ya'.

**1006** — JP 「ふあっ――あっ―あ……ああっ――\nわたくし――お小水――双鉄、様――にっ――んっ！」; TW 「呼啊——啊——啊……啊啊——我的——尿——射在了雙鐵少爺——不——！」; old_vn (moan) 「Fua——a——a……aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」; **fix = 「Fua——a——a……Aa——\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」**. Đổi: 'a……aa' → 'a……Aa'.

**1010** — JP 「ふああああああああああああっ！！！\nあっ！？――ダメっ――やっ――――あ、ああっ……」; TW 「呼啊——！！！啊！？——不行啊——哎——啊，那樣……」; old_vn (moan) 「Fuaaaaaaaaaaaa!!!\nA!?——Không được——ya————a, aa……」; **fix = 「Fuaaaaaaaaaaaa!!!\nA!?——Không được——Ya————a, Aa……」**. Đổi: 'ya' → 'Ya'; 'aa……」' → 'Aa……」'.

**1033** — JP 「あっ――ああっ――んっ！ 双鉄さまっ――\nふあっ――双鉄、さまぁっ」; TW 「啊——啊啊——嗯！雙鐵少爺——呼啊——雙鐵少爺」; old_vn (moan) 「A——aa——ưm! Ngài Soutetsu——\nfua——Ngài Soutetsu.」; **fix = 「A——Aa——ưm! Ngài Soutetsu——\nFua——Ngài Soutetsu.」**. Đổi: 'aa' → 'Aa'; '\\nfua' → '\\nFua'.

**1064** — JP 「ふやっ！？ あっ！ だめっ――押したら――\nんっ――もっと――あっ、ふあっ――んんん～～～っ」; TW 「嗚呀！？啊！不行——再擠壓的話——嗯——更——啊，呼啊——嗯嗯～～～」; old_vn (moan) 「Fuya!? A! Không được——nếu ấn vào——\nưm——nữa——a, fua——ưm ưm~~~Ư」; **fix = 「Fuya!? A! Không được——nếu ấn vào——\nưm——nữa——a, Fua——ưm ưm~~~Ư」**. Đổi: 'fua' → 'Fua'.

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 1 dòng

**1335** — JP 極大にまで膨れ上がった僕の勃起に貫かれ――ああ。; TW 入口被我膨脹到極限的肉棒給捅開了——啊。; old_vn (moan) Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——aa.; **fix = Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——Aa.**. Đổi: 'aa.' → 'Aa.'.

#### ハチロクh7_レトロモダンメイクラヴ.txt.toml — 3 dòng

**743** — JP 「ひゃっ！ あっ！ んっ！！ ふあっ――はきゅっ――\nふっ――ふあっ！ あっ！ あっ！ あああっ！！！！」; TW 「呀！啊！嗯！！呼啊——哈嗚——呼——呼啊！啊！啊！啊啊！！！！」; old_vn (moan) 「Hya! A! Ưm!! Fua——hakyu——\nphù——Fua! A! A! Aaa!!!!」; **fix = 「Hya! A! Ưm!! Fua——Hakyu——\nphù——Fua! A! A! Aaa!!!!」**. Đổi: 'hakyu' → 'Hakyu'.

**745** — JP 「か……は……あっ――ぐっ――んっ――そ――ん、な、\nいき、なり――いき――なりッ――んきゅうう！！？」; TW 「呃……啊——咕——嗯——那樣——的，突然——就——就——嗯啊——！！？」; old_vn (unif đã gộp) 「Ka……ha……a——Gu——ưm——như——vậy,\nđột, nhiên——đột——nhiên——Nkyuuu!!?」; **fix = 「Ka……Ha……a——Gu——ưm——như——vậy,\nđột, nhiên——đột——nhiên——Nkyuuu!!?」**. Đổi: '「Ka……ha……a' → '「Ka……Ha……a'.

**819** — JP 「ん……きゅっ――ふぁああああんっ！！！」; TW 「嗯……呀嗚、啊——！！！」; old_vn (unif đã gộp) 「Ưm……kiu——Faaaaan!!!」; **fix = 「Ưm……Kiu——Faaaaan!!!」**. Đổi: '「Ưm……kiu' → '「Ưm……Kiu'.

#### ハチロクh8_桜色のひめごと.txt.toml — 6 dòng

**754** — JP 「はむっ！？ ん――ひゅっ――ん……れるっ――ろっ、\nちゅ――ちゅむっ――ほーへふ……んっ――はふぁぁ」; TW 「哈姆！？嗯——咻——……咻嚕——嚕，啾——啾姆——嗯—呼……——嗚啊啊」; old_vn (unif đã gộp) 「Ha mu!? Ưm——hyu——ưm……liếm——liếm,\nchu——chụt——ho he phu……ưm——ha faa」; **fix = 「Ha mu!? Ưm——Hyu——ưm……liếm——liếm,\nChu——chụt——ho he phu……ưm——ha faa」**. Đổi: 'hyu' → 'Hyu'; 'liếm,\\nchu' → 'liếm,\\nChu'.

**762** — JP 「あ――はっ――ひっ――いいっ！ きもちっ――ふ、あ\nきもちいっ――あ――おっぱい、も――おまんまん、も」; TW 「啊——哈——哈——好！舒服——呼，啊舒服——啊——乳房，和——小妹妹，都是」; old_vn (unif đã gộp) 「A——ha——hi——thích quá! Sướng——Fu, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」; **fix = 「A——Ha——hi——thích quá! Sướng——Fu, a\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」**. Đổi: 'ha' → 'Ha'.

**794** — JP 「ちゅ……むっ――ん――ぷぁ――あっ！ 双鉄、様……\nさっき――あれほど、お出しに、なったの……に――ん」; TW 「啾……姆——噗啊——啊！雙鐵少爺……剛才——還出來那麼多的……——嗯」; old_vn (unif đã gộp) 「Chụt……——ưm——pua——a! Ngài Soutetsu……\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」; **fix = 「Chụt……——ưm——Pua——a! Ngài Soutetsu……\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」**. Đổi: 'pua' → 'Pua'.

**812** — JP 「ふぁ……あ…………あまざけ、い、っぱい――上の、\nおくちも……した、の……おくち、も――ふぁ」; TW 「嗚啊……啊……滿滿都是甜米酒——然後又親了……親過了——嗚啊」; old_vn (unif đã gộp) 「Fa……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——fa」; **fix = 「Fa……a…………đầy, ắp, rượu ngọt——Cái miệng,\nở trên……cái miệng, ở……dưới, cũng——Fa」**. Đổi: 'fa」' → 'Fa」'.

**813** — JP 「ふぁ……ぁァ――――――あっ……全部……ぜん、ぶ\n――わたくし――全部を――旦那様、の――おくち、に」; TW 「嗚啊……啊啊——啊……全部……哦嗯，噗——我——全部——向夫君——口腔」; old_vn (unif đã gộp) 「Fa……aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」; **fix = 「Fa……Aa——————a……Tất cả……toàn, bộ\n——Em——tất cả——vào miệng, của——phu quân」**. Đổi: '「Fa……aa' → '「Fa……Aa'.

**841** — JP 「んむっ！ ん――むっ！！ じゅろろっ！ ちゅむ！ \n（すっ――ひっ）ちゅるっ！ れろおおおおおおっ！」; TW 「嗯姆！嗯——姆！！呲啾——！啾嗯！（做——哈）啾嚕！咻嚕——！」; old_vn (unif đã gộp) 「Ưm mu! Ưm——mu!! Chóp chép! Chụt!\n（Su——hi）Chụt! Rerooooooo!!」; **fix = 「Ưm mu! Ưm——Mu!! Chóp chép! Chụt!\n（Su——hi）Chụt! Rerooooooo!!」**. Đổi: 'mu!!' → 'Mu!!'.

#### ハチロクh9_コノフクハキルコト.txt.toml — 18 dòng

**2033** — JP 「ふっ……んっ――――（ごくんっ）\nずっ――ちゅるっ――じゅううっ――（ごくっ）」; TW 「呼……——（嗯）呲——啾嚕——吱嗚——（嗯）」; old_vn (unif đã gộp) 「Fu……ưm————（Ực）\nZu——chụt——juuu——（Ực）」; **fix = 「Fu……ưm————（Ực）\nZu——chụt——Juuu——（Ực）」**. Đổi: 'juuu' → 'Juuu'.

**2043** — JP 「れるっ――るっ――るうううっ――じゅ、ずっ――\nずっ――れろ――れるううっ――ずずっ――ずうっ」; TW 「咻嚕——嚕——嚕嗚——呲啾，呲——呲——嗯——咻嚕嗚——慢慢——嗚」; old_vn (unif đã gộp) 「Rộp——rộp——rộộộộp——ju, zu——\nzu——rero——rộộộp——zuzu——zuu」; **fix = 「Rộp——rộp——rộộộộp——Ju, Zu——\nZu——Rero——rộộộp——Zuzu——Zuu」**. Đổi: 'ju,' → 'Ju,'; 'zu' → 'Zu'; '\\nzu' → '\\nZu'; 'rero' → 'Rero'; 'zuzu' → 'Zuzu'; 'zuu」' → 'Zuu」'.

**2053** — JP 「はっ――んっ――ちゅっ――ふっ、ほうへふ、はぁ\n――ちゅくっ、ん――らいふき――れふっ――ふぅっ」; TW 「哈——啾——呼，哈呼，啊——啾嗯，嗯——墜喜歡——嗚——嗚」; old_vn (moan) 「Ha——ưm——chụt——hu, hoo he hu, haa\n——chu ku, ưm——dai suki——re hu——huu」; **fix = 「Ha——ưm——chụt——Hu, hoo he hu, Haa\n——chu ku, ưm——dai suki——re hu——Huu」**. Đổi: 'hu,' → 'Hu,'; 'haa\\n' → 'Haa\\n'; 'huu」' → 'Huu」'.

**2054** — JP 「はっ、はっ――はああっ――は、あ――はぁっ」; TW 「哈，哈——啊啊——啊——啊」; old_vn (moan) 「Hà, hà——haaa——hà, a——haa」; **fix = 「Hà, hà——Haaa——hà, a——Haa」**. Đổi: 'haaa' → 'Haaa'; 'haa」' → 'Haa」'.

**2055** — JP 「はっ、はあっ――はあっ――はあっ――\nおまん、まんの、奥っ――あと、もう、少し、で」; TW 「哈，啊——啊——啊——小妹妹的，裡頭——還差一點點了」; old_vn (moan) 「Hà, haa——haa——haa—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」; **fix = 「Hà, Haa——Haa——Haa—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」**. Đổi: 'haa' → 'Haa'; 'haa' → 'Haa'; 'haa' → 'Haa'.

**2078** — JP 「あっ――んっ……ちゅうっ」; TW 「啊——……啾嗚」; old_vn (moan) 「A——ưm……chuu」; **fix = 「A——ưm……Chuu」**. Đổi: 'ưm……chuu」' → 'ưm……Chuu」'.

**2120** — JP 「ちゅっ――れるっ――れろっ――ちゅううう――\nちゅるっ――（こくっ）――んっ――ちゅっ、ちゅむ」; TW 「啾——咻嚕——嗯——啾——啾嚕——（咕嚕）——啾，啾嗯」; old_vn (unif đã gộp) 「Chụt——rộp——mút——chuuuu——\nchóp chép——（Ực）——ưm——chụt, chụt」; **fix = 「Chụt——rộp——mút——Chuuuu——\nchóp chép——（Ực）——ưm——chụt, chụt」**. Đổi: 'chuuuu' → 'Chuuuu'.

**2122** — JP 「ちゅっ――じゅっ――じゅるっ――じゅううっ――\nんっ――れろおおっ――れるっ――れるううううっ」; TW 「啾——啾——啾嚕——吱吱嗚——嗯——嗯哦——咻嚕——咻嚕嗚嗚嗚」; old_vn (unif đã gộp) 「Chụt——ju——juru——juuu——\nƯm——rerooo——rộp——rộộộộộp」; **fix = 「Chụt——Ju——Juru——Juuu——\nƯm——Rerooo——rộp——rộộộộộp」**. Đổi: 'ju' → 'Ju'; 'juru' → 'Juru'; 'juuu' → 'Juuu'; 'rerooo' → 'Rerooo'.

**2127** — JP 「ぢゅうううううっ！ ぢゅぼ！ ちゅっ！ じゅぶ、\nじゅぼっ！ ちゅうっ！ ぢゅるっ！ ぢゅ！ ぼ！」; TW 「啾嗚嗚嗚！啾啵！啾！啾，啾啵！啾嗚！啾嚕！呲啾！啵！」; old_vn (unif đã gộp) 「Juuuuu! Jubo! Chụt! Jubu,\njubo! Chụụt! Juru! Ju! Bo!」; **fix = 「Juuuuu! Jubo! Chụt! Jubu,\nJubo! Chụụt! Juru! Ju! Bo!」**. Đổi: 'Jubu,\\njubo!' → 'Jubu,\\nJubo!'.

**2133** — JP 「ちゅるうっ――ちゅ、ずっ――ぺろ、ぺろ、ぺろっ、\nちゅるうっ、ちゅっ――れろっ――ぺろ、ぺろおっっ」; TW 「啾嚕——啾，呲——呸嚕，呸嚕，呸嚕，啾嚕，啾——咻嚕——呸嚕，呸嚕」; old_vn (unif đã gộp) 「Chụụt——chụt, zu——pero, pero, pero,\nchụụt, chụt——rero——pero, perooo」; **fix = 「Chụụt——chụt, Zu——Pero, Pero, Pero,\nchụụt, chụt——Rero——Pero, Perooo」**. Đổi: 'zu' → 'Zu'; 'pero,' → 'Pero,'; 'pero,' → 'Pero,'; 'pero,\\nchụụt,' → 'Pero,\\nchụụt,'; 'rero' → 'Rero'; 'pero,' → 'Pero,'; 'perooo」' → 'Perooo」'.

**2138** — JP 「ちゅむっ！ じゅっ！ じゅぼっ――んっ、ふっ、\nれるっ――ぢゅっ！ ぢゅぼっ！ じゅるううっ！」; TW 「啾姆！啾！呲啾——呼，咻嚕——呲啾！啾啵！啾嚕！」; old_vn (unif đã gộp) 「Chụt! Ju! Jubo——ưm, Fu,\nrộp——ju! Jubo! Juruuu!」; **fix = 「Chụt! Ju! Jubo——ưm, Fu,\nrộp——Ju! Jubo! Juruuu!」**. Đổi: 'ju!' → 'Ju!'.

**2140** — JP 「ちゅむっ、れるっ――ちゅううっ、ちゅるるっ――\nズズッ――んっ――ちゅっ――れろっ、れるうっ」; TW 「啾姆，咻嚕——啾嗚，啾嚕嚕——吹吹——啾——嗯，咻嚕」; old_vn (unif đã gộp) 「Chụt, rộp——chụụụt, chụt——\nZuzu——ưm——chụt——rero, rộộp」; **fix = 「Chụt, rộp——chụụụt, chụt——\nZuzu——ưm——chụt——Rero, rộộp」**. Đổi: 'rero,' → 'Rero,'.

**2145** — JP 「んっ――ちゅっ――ちゅぼっ！ じゅぼっ！\nじゅ！ じゅぼっ！ じゅりゅうう！ じゅ、ぼっ！」; TW 「嗯——啾——啾啵！啾啵！呲啾！啾啵！呲啾！啾，啵！」; old_vn (unif đã gộp) 「Ưm——chụt——chụt! Jubo!\nJu! Jubo! Juryuuu! Ju, bo!」; **fix = 「Ưm——chụt——chụt! Jubo!\nJu! Jubo! Juryuuu! Ju, Bo!」**. Đổi: 'bo!」' → 'Bo!」'.

**2147** — JP 「んっ――ちゅむっ！ じゅっ！ じゅぼっ！ じゅ、\nぢゅちゅっ！ ちゅむっ！ ぢゅるっ！ じゅぶ！」; TW 「嗯——啾姆！啾！啾啵！呲啾，呲啾！啾姆！啾嚕！啾！」; old_vn (unif đã gộp) 「Ưm——chụt! Ju! Jubo! Ju,\njuchu! Chụt! Juru! Jubu!」; **fix = 「Ưm——chụt! Ju! Jubo! Ju,\nJuchu! Chụt! Juru! Jubu!」**. Đổi: 'Ju,\\njuchu!' → 'Ju,\\nJuchu!'.

**2153** — JP 「んっ――はむっ――ちゅっ――ちゅううっ、ちゅ」; TW 「嗯——姆——啾——啾嗚，啾」; old_vn (unif đã gộp) 「Ưm——hamu——chụt——chụụụt, chụt」; **fix = 「Ưm——Hamu——chụt——chụụụt, chụt」**. Đổi: 'hamu' → 'Hamu'.

**2156** — JP 「ん……ちゅっ――ちゅむっ――ちゅっ――んっ――\nれるっ――れろっ――じゅるる――れるっ――ちゅぷ」; TW 「嗯……啾——啾姆——啾——咻嚕——嗯——啾嚕嚕——咻嚕——啾噗」; old_vn (unif đã gộp) 「Ưm……chụt——chumu——chụt——ưm——\nrộp——liếm láp——chóp chép——rộp——chu pu」; **fix = 「Ưm……chụt——Chumu——chụt——ưm——\nrộp——liếm láp——chóp chép——rộp——chu pu」**. Đổi: 'chumu' → 'Chumu'.

**2182** — JP 「んむっ！？ んっ――ちゅぼっ――じゅっ！\nぢゅぶっ！ ぢゅむっ！ ふっ――ちゅむ、じゅっ！」; TW 「嗯姆！？嗯——啾啵——啾！啾噗！呲啾姆！呼——啾嗯，啾！」; old_vn (unif đã gộp) 「Ưm mu!? Ưm——chụt——ju!\nJubu! Jumu! Fu——chụt, ju!」; **fix = 「Ưm mu!? Ưm——chụt——Ju!\nJubu! Jumu! Fu——chụt, Ju!」**. Đổi: 'ju!\\nJubu!' → 'Ju!\\nJubu!'; 'ju!」' → 'Ju!」'.

**2289** — JP 「わたくし――の、おまたの――われ、めっ――んっ、\nふ――あっ――くっ――はぁ――おまん、まん、です」; TW 「我——股間的——裂縫——嗯——呼——啊——嗯——啊——小妹妹」; old_vn (unif đã gộp) 「Là khe hở——giữa hai chân——của em——ưm,\nFu——a——Ku——haa——là cô bé, ạ」; **fix = 「Là khe hở——giữa hai chân——của em——ưm,\nFu——a——Ku——Haa——là cô bé, ạ」**. Đổi: 'haa' → 'Haa'.

#### ポーレット02_解放b寝台.txt.toml — 1 dòng

**1795** — JP 「ですね。わたしも、サポートします……ふぁ」; TW 「嗯。我也會幫你的……呼」; old_vn (unif đã gộp) 「Vâng. Em cũng sẽ hỗ trợ…… fa.」; **fix = 「Vâng. Em cũng sẽ hỗ trợ…… Fa.」**. Đổi: 'fa.」' → 'Fa.」'.

#### ポーレットh1_ファーストセックス.txt.toml — 2 dòng

**989** — JP 「きゃふっ――ひゃっ――押され、てっ――んうっっ」; TW 「哇——呀——被頂到了——嗯」; old_vn (moan) 「Kyafu——hya——bị ấn, vào——ưm.」; **fix = 「Kyafu——Hya——bị ấn, vào——ưm.」**. Đổi: 'hya' → 'Hya'.

**1019** — JP 「んっ――ふっ――んっ――れろっ――れるっ――\nんっ――ちゅっ――ちゅるるっ――ちゅぞおおおおっ」; TW 「嗯——呼——嗯——啾嚕——啾嚕——嗯——啾——啾嚕嚕——啾嚕嚕」; old_vn (unif đã gộp) 「Ưm——phù——ưm——liếm——rộp——\nưm——chụt——chùn chụt——chuzooooo.」; **fix = 「Ưm——phù——ưm——liếm——rộp——\nưm——chụt——chùn chụt——Chuzooooo.」**. Đổi: 'chuzooooo.」' → 'Chuzooooo.」'.

#### ポーレットh2_制服変更？.txt.toml — 3 dòng

**923** — JP 「けどっ――けどぉっ――わたしっ――わらひぃっ――\nあっ――ふああああああああああんっっっっ！」; TW 「可是——可是——我已經——我已經——啊——呼啊啊啊！」; old_vn (moan) 「Nhưng mà——nhưng mà——em——em——\ná——fuaaaaaaaaaan!」; **fix = 「Nhưng mà——nhưng mà——em——em——\ná——Fuaaaaaaaaaan!」**. Đổi: 'fuaaaaaaaaaan!」' → 'Fuaaaaaaaaaan!」'.

**928** — JP 「きあっ――あっ――ひおっ――んぎゅっ――」; TW 「呀——啊——咿——嗯——」; old_vn (moan) 「Kia——á——hio——Ngyu——」; **fix = 「Kia——á——Hio——Ngyu——」**. Đổi: 'hio' → 'Hio'.

**991** — JP 「あ……ひあ……あっ――ふぁ――あっ――あっ――あ」; TW 「啊……呀……啊——呼——啊——啊——啊」; old_vn (moan) 「A... hia... á——Fa——á——á——a.」; **fix = 「A... Hia... á——Fa——á——á——a.」**. Đổi: 'hia...' → 'Hia...'.

#### ポーレットh3_誘惑アイスコーヒー.txt.toml — 5 dòng

**914** — JP 「ふっ――んっ――ちゅっ――ずちゅっ――\nちゅむっ――むっ――ちゅばっ――ちゅむっ」; TW 「呼——嗯——啾——啾嚕——啾嚕——嗯——啾噗——啾噗」; old_vn (moan) 「Phù——ưm——chụt——chụt——\nchumu——ưm——chuba——chumu」; **fix = 「Phù——ưm——chụt——chụt——\nChumu——ưm——Chuba——Chumu」**. Đổi: '\\nchumu' → '\\nChumu'; 'chuba' → 'Chuba'; 'chumu」' → 'Chumu」'.

**933** — JP 「あむっ――ん――ちゅぶっ――ちゅるっ――\nぺろっ――れるっ――れろろっ――ちゅううっ」; TW 「唔——嗯——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕——啾嚕」; old_vn (unif đã gộp) 「Ngoạm——ưm——chubu——chụt——\nliếm——rộp——liếm——chụụụt」; **fix = 「Ngoạm——ưm——Chubu——chụt——\nliếm——rộp——liếm——chụụụt」**. Đổi: 'chubu' → 'Chubu'.

**942** — JP 「はむっ――んっ――ん～～っ――\nれるっ、れろっ――ちゅむつ――ちゅうっ」; TW 「啊——嗯——嗯～～啾嚕、啾嚕——嗯——啾嚕」; old_vn (unif đã gộp) 「Ngoạm——ưm——ưm～～\nrộp, liếm——chumu——chụụt」; **fix = 「Ngoạm——ưm——ưm～～\nrộp, liếm——Chumu——chụụt」**. Đổi: 'chumu' → 'Chumu'.

**946** — JP 「あ……んっ――ちゅっ――ちゅむっ――\nちゅきっ――好きっ――ンッ――双鉄、くぅん」; TW 「啊……嗯——啾——啾嚕——我喜歡——好喜歡你——雙鐵——」; old_vn (moan) 「A……ưm——chụt——chumu——\nThích——thích anh lắm——ưm——anh Soutetsu」; **fix = 「A……ưm——chụt——Chumu——\nThích——thích anh lắm——ưm——anh Soutetsu」**. Đổi: 'chumu' → 'Chumu'.

**966** — JP 「ちゅっ――ちゅむっ――ぺろっ――れろおおおっ」; TW 「啾嚕——啾嚕——啾嚕——啾嚕嚕」; old_vn (moan) 「Chụt——chumu——liếm——Reroooo」; **fix = 「Chụt——Chumu——liếm——Reroooo」**. Đổi: 'chumu' → 'Chumu'.

#### ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml — 1 dòng

**942** — JP 「んっ……ちゅっ――ちゅむっ――ちゅうう――ちゅっ\n――ぷ、あっ――ん――れろっ――れるっ――れろおっ」; TW 「嗯……啾——啾嚕——啾啾——啾嚕——呼、啊——嗯——啾嚕——啾嚕——啾噗」; old_vn (unif đã gộp) 「Ưm……chụt——chumu——chụtttt——chụt ——Phù, a——ưm——liếm——rộp——liếmmmm」; **fix = 「Ưm……chụt——Chumu——chụtttt——chụt ——Phù, a——ưm——liếm——rộp——liếmmmm」**. Đổi: 'chumu' → 'Chumu'.

#### ポーレットh7_残業エッチもyシャツで.txt.toml — 4 dòng

**818** — JP 「ひあっ！ あっ！ はっ！ あっ！ ふあっ！\nあっ――んゆっ――ひゃふっ！！」; TW 「呀！啊！啊！啊！呼啊！啊——嗯——呀啊！！」; old_vn (moan) 「Hia! A! Hà! A! Fua! A——Nyu——hyafu!!」; **fix = 「Hia! A! Hà! A! Fua! A——Nyu——Hyafu!!」**. Đổi: 'hyafu!!」' → 'Hyafu!!」'.

**826** — JP 「ひあっ！？ きゅ――きゅふうううんっ！！！」; TW 「呀！？呀——呀啊啊啊！！！」; old_vn (moan) 「Hia!? Kyu——kyufuuuun!!!」; **fix = 「Hia!? Kyu——Kyufuuuun!!!」**. Đổi: 'kyufuuuun!!!」' → 'Kyufuuuun!!!」'.

**858** — JP 「ふあっ！ あっ――ひっ――あっ――しきゅう――\nばちゅって――あついの――あたっ、って――はきゅ！」; TW 「呼啊！啊——呀——啊——子宮——射到了——燙燙的——打到了——啊！」; old_vn (moan) 「Fua! A——hi——a——tử cung—— bị bắn, trúng——nóng, quá——đập, vào——hakyu!」; **fix = 「Fua! A——hi——a——tử cung—— bị bắn, trúng——nóng, quá——đập, vào——Hakyu!」**. Đổi: 'hakyu!」' → 'Hakyu!」'.

**885** — JP 「はっ！ あっ！ あっ！ あっ！ ひっ――ふあっ！\nそうてつ――く――ふっ――あ――そうてつ、くぅん」; TW 「啊！啊！啊！啊！呀——呼啊！雙鐵——呼啊——雙鐵」; old_vn (moan) 「Hà! A! A! A! Hi——Fua! Anh Soutetsu——ku——phù——a——Anh Soutetsu」; **fix = 「Hà! A! A! A! Hi——Fua! Anh Soutetsu——Ku——phù——a——Anh Soutetsu」**. Đổi: 'ku' → 'Ku'.

#### 凪ふかみh1_修学旅行の夜.txt.toml — 2 dòng

**1226** — JP 「ひゃぷっ！？ わっ――んっ――にゃ、うっ――\nこ、これっ――んっ――熱か――ばいっ――臭か、ばい」; TW 「呀！？哇……嗯……喵……這、這個……嗯……好燙……味道好大」; old_vn (moan) 「Hyapu!? Oa——ưm——nya, ư——\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」; **fix = 「Hyapu!? Oa——ưm——Nya, ư——\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」**. Đổi: 'nya,' → 'Nya,'.

**1290** — JP 「れるっ――ちゅむっ――ぺろ――ぺろおっ――ちゅっ、\nちゅむっ、ちゅうっ――ぺろっ――ぺろっ――れろん！」; TW 「啾……啾……啾……啾……啾，啾，啾……啾……啾……啾！」; old_vn (unif đã gộp) 「Rộp——chụt——liếm——liếm——chụt,\nchụt, chu——liếm——liếm——liếm!」; **fix = 「Rộp——chụt——liếm——liếm——chụt,\nchụt, Chu——liếm——liếm——liếm!」**. Đổi: 'chu' → 'Chu'.

#### 凪ふかみh2_みずあそび.txt.toml — 3 dòng

**1294** — JP 「はぁ……はぁ……はぁっ――は――ああ～っ」; TW 「呼……呼……呼……呼……啊」; old_vn (moan) 「Hàà... hàà... hàà——hà——aa~Ư」; **fix = 「Hàà... hàà... hàà——hà——Aa~Ư」**. Đổi: 'aa~Ư」' → 'Aa~Ư」'.

**1374** — JP 「えうっ――んっ――ちゅ……ちゅずっ――じゅるっ――\nんう……れろ――れるっ――ちゅうっ――ずじゅっ」; TW 「嗯……嗯……啾……啾……啾……嗯……啾……啾……啾……啾」; old_vn (unif đã gộp) 「Eu——ưm——chụt... chụt——rột——\nưm... liếm——rộp——chu——chụt」; **fix = 「Eu——ưm——chụt... chụt——rột——\nưm... liếm——rộp——Chu——chụt」**. Đổi: 'chu' → 'Chu'.

**1428** — JP 「凪ちゃんの指――んっ――おいひい――ひょぉ……ん、\nちゅっ――ちゅう――れろっ――れるうっ」; TW 「小凪的手指……嗯……真好吃……嗯，啾……啾……啾……啾」; old_vn (unif đã gộp) 「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\nchụt——chu——liếm——rộộộp」; **fix = 「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\nchụt——Chu——liếm——rộộộp」**. Đổi: 'chu' → 'Chu'.

#### 日々姫h4_いもうとタオル.txt.toml — 1 dòng

**991** — JP 「ふぇ……ぁ……わた……私、おしっこ――おもらし――\n全部……全部して……イっちゃっ――きゅふっ！！？」; TW 「呼……啊……我……尿出來了――全部……尿出來了……要去了――呀！！？」; old_vn (moan) 「Fue……a……em……Em, đi tè――tè dầm――\nHết……hết sạch rồi……Lên đỉnh mất――kyufu!!?」; **fix = 「Fue……a……em……Em, đi tè――tè dầm――\nHết……hết sạch rồi……Lên đỉnh mất――Kyufu!!?」**. Đổi: 'mất――kyufu!!?」' → 'mất――Kyufu!!?」'.

#### 日々姫h5_白濁絵の具の射精会.txt.toml — 1 dòng

**1253** — JP 「ん……ぷっ――んっ！ ちゅうっ――ずぢゅ！ ごくっ\n――ふっ――あむっ――れろっ――れるっ――こしゅん」; TW 「嗯……噗――嗯！啾――啾嚕！咕嚕――呼――唔――啾嚕――啾嚕――咕啾」; old_vn (unif đã gộp) 「Ưm……phụt――ưm! Chụt――zuju! Ực\n――phù――ngoạm――liếm――rộp――koshun」; **fix = 「Ưm……phụt――ưm! Chụt――Zuju! Ực\n――phù――ngoạm――liếm――rộp――Koshun」**. Đổi: 'Chụt――zuju!' → 'Chụt――Zuju!'; 'Ực\\n――phù――ngoạm――liếm――rộp――koshun」' → 'Ực\\n――phù――ngoạm――liếm――rộp――Koshun」'.

#### 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 2 dòng

**2114** — JP 「ふぁぁぁぁぁあっ――ああっ――そこ、すき、なの\nんっ――もっと、そこ、より――だけどっ、もっとぉ」; TW 「呼啊啊啊――啊啊――我喜歡那裡，嗯――比那裡，要更――更――」; old_vn (unif đã gộp) 「Faaaaaa――aa――Chỗ đó, em thích, lắm\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」; **fix = 「Faaaaaa――Aa――Chỗ đó, em thích, lắm\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」**. Đổi: '「Faaaaaa――aa――Chỗ' → '「Faaaaaa――Aa――Chỗ'.

**2713** — JP 「にぃ、に――んっ――くううう～～ん――ふ、あっ\nすと……レッチ、も――いい、けど――よか、けどっ」; TW 「阿哥――嗯――唔唔唔～～嗯――呼、啊，伸……伸展運動――做的差不多了吧」; old_vn (unif đã gộp) 「Anh, hai――ưm――kuuuu~~n――Fu, a\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」; **fix = 「Anh, hai――ưm――Kuuuu~~n――Fu, a\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」**. Đổi: 'hai――ưm――kuuuu~~n――Fu,' → 'hai――ưm――Kuuuu~~n――Fu,'.

#### 真闇h1_長期熟成.txt.toml — 2 dòng

**1056** — JP 「ちゅっ――んっ……んちゅっ――れるっ――れろっ\n――ん……んふっ……ふっ」; TW 「啾――嗯……嗯啾――舔――舔――嗯……嗯唔……呼」; old_vn (unif đã gộp) 「Chụt――ưm……ưm chụt――rộp――liếm\n――ưm……ưm fu……fu」; **fix = 「Chụt――ưm……ưm chụt――rộp――liếm\n――ưm……ưm fu……Fu」**. Đổi: 'fu……fu」' → 'fu……Fu」'.

**1071** — JP 「ん……あっ――入って、くるっ――んんっ――\n双、ちゃんの――おちん、ちん――ふあっ」; TW 「嗯……啊――進來了――嗯嗯――小雙的――雞雞――嗚啊」; old_vn (moan) 「Ưm……a――đang vào, này――ưm ưm――\nchim, của――Sou, chan――fua.」; **fix = 「Ưm……a――đang vào, này――ưm ưm――\nchim, của――Sou, chan――Fua.」**. Đổi: 'chan――fua.」' → 'chan――Fua.」'.

#### 真闇h2_無濾過.txt.toml — 9 dòng

**1010** — JP 「やんっ――んんっ――やあっ――おしり、ばっ――\nあつく――って――んっ――ヘン――これっ――あふっ」; TW 「呀嗯――嗯嗯――呀啊――屁股真的――好熱――啊――嗯――要――不對了――啊呼」; old_vn (moan) 「Yan――ưm ưm――yaa――mông, thì――\nnóng――lắm――ưm――kỳ lạ――quá――Afu.」; **fix = 「Yan――ưm ưm――Yaa――mông, thì――\nnóng――lắm――ưm――kỳ lạ――quá――Afu.」**. Đổi: 'ưm――yaa――mông,' → 'ưm――Yaa――mông,'.

**1058** — JP 「あ――来た――双ちゃんの、おちんちん――\nんっ――いっぱい――ふあっっ――嬉し――いひっ！？」; TW 「啊――來了――小雙的雞雞――嗯――好撐――嗚啊――好高興！？」; old_vn (moan) 「A――vào rồi――chim của, Sou-chan――\nưm――đầy quá――Fua――vui quá――ihi!?」; **fix = 「A――vào rồi――chim của, Sou-chan――\nưm――đầy quá――Fua――vui quá――Ihi!?」**. Đổi: 'quá――ihi!?」' → 'quá――Ihi!?」'.

**1075** — JP 「あは……双ちゃん。\nちゅうちゅうするたび、ビクン、ビクンて」; TW 「啊哈……小雙。啾啾的時候就在跳個不停呢」; old_vn (moan) 「Aha……Sou-chan.\nMỗi lần em chuu chuu là nó lại giật nảy lên kìa.」; **fix = 「Aha……Sou-chan.\nMỗi lần em Chuu Chuu là nó lại giật nảy lên kìa.」**. Đổi: 'chuu' → 'Chuu'; 'chuu' → 'Chuu'.

**1083** — JP 「ちゅっ――れるっ――ちゅるっ――ちゅううっっ」; TW 「啾――舔――啾――啾」; old_vn (unif đã gộp) 「Chụt――rộp――rột――chuuu.」; **fix = 「Chụt――rộp――rột――Chuuu.」**. Đổi: '「Chụt――rộp――rột――chuuu.」' → '「Chụt――rộp――rột――Chuuu.」'.

**1088** — JP 「ふあっ――んひゅゅっ！！？ ――やああっ、\n双ちゃんっ――そこ、違っ――んっ――んきゅんっ！」; TW 「嗚啊――嗯呀！！？ ――呀啊啊、小雙――不是那裡――嗯――嗯呀嗯！」; old_vn (moan) 「Fua――nhyuu!!? ――Yaaa,\nSou-chan――chỗ đó, không phải――ưm――nkyun!」; **fix = 「Fua――Nhyuu!!? ――Yaaa,\nSou-chan――chỗ đó, không phải――ưm――Nkyun!」**. Đổi: '「Fua――nhyuu!!?' → '「Fua――Nhyuu!!?'; 'phải――ưm――nkyun!」' → 'phải――ưm――Nkyun!」'.

**1092** — JP 「ん――くっ」; TW 「嗯――唔」; old_vn (moan) 「Ưm――ku.」; **fix = 「Ưm――Ku.」**. Đổi: '「Ưm――ku.」' → '「Ưm――Ku.」'.

**1450** — JP 答えるかわりに、ひたすらに吸う。\nちゅくちゅく、ちゅうちゅう、一心に吸う。; TW 我一個勁地吮吸著，這也是我的回答。啾啾、啾啾，專心致志地吮吸。; old_vn (moan) Thay cho câu trả lời, tôi chỉ mải miết mút mát.\nChụt chụt, chuu chuu, mút một cách say sưa.; **fix = Thay cho câu trả lời, tôi chỉ mải miết mút mát.\nChụt chụt, Chuu Chuu, mút một cách say sưa.**. Đổi: 'chuu' → 'Chuu'; 'chuu,' → 'Chuu,'.

**1842** — JP （きゅっ――くぽっっ――きゅぷっ――きゅうっ）; TW （啾――啪――啾唔――壓）; old_vn (unif đã gộp) （Thắt lại――phập――kypu――Thắt lại）; **fix = （Thắt lại――phập――Kypu――Thắt lại）**. Đổi: 'lại――phập――kypu――Thắt' → 'lại――phập――Kypu――Thắt'.

**1845** — JP （ちゅるっ――ちゅっ――れるっ――ちゅむうっ）; TW （啾――啾――舔――啾）; old_vn (unif đã gộp) （Rột――chụt――rộp――chumuu）; **fix = （Rột――chụt――rộp――Chumuu）**. Đổi: '（Rột――chụt――rộp――chumuu）' → '（Rột――chụt――rộp――Chumuu）'.

#### 真闇h3_補習授業の廃校舎.txt.toml — 22 dòng

**2198** — JP 「ぺろっ――れろおおおっ――ぺろっ、ぺちゅっ。\nチュルッ――ちゅっ――れろおおおおっ――れるっ」; TW 「呸嘍――呸嘍――呸囉、呸啾。啾嚕――啾――呸嘍――舔」; old_vn (unif đã gộp) 「Pero――reroooo――pero, pechu.\nChụt――chụt――rerooooo――rộp.」; **fix = 「Pero――Reroooo――Pero, Pechu.\nChụt――chụt――Rerooooo――rộp.」**. Đổi: '「Pero――reroooo――pero,' → '「Pero――Reroooo――Pero,'; 'pechu.\\nChụt――chụt――rerooooo――rộp.」' → 'Pechu.\\nChụt――chụt――Rerooooo――rộp.」'.

**2212** — JP 「はっ――あ、あっ、あああ――んっ――そこ、\nば、され、たら――ふっ――あ――ぞわ、って」; TW 「哈――啊、啊、啊啊啊――嗯――那裡，插那裡的話――呼――啊――好棒」; old_vn (unif đã gộp) 「Há――a, á, aaa――ưm――chỗ đó,\nbị, chạm, vào――Phư――a――rùng mình, mất.」; **fix = 「Há――a, á, Aaa――ưm――chỗ đó,\nbị, chạm, vào――Phư――a――rùng mình, mất.」**. Đổi: 'aaa――ưm――chỗ' → 'Aaa――ưm――chỗ'.

**2215** — JP 「はっ――ん――ふっ――あっ――おねえ、ちゃんっ、\nふぁうっ――ふあっ――そこ、ば――押されたらっ」; TW 「哈――嗯――呼――啊――姐姐，哇――嗚啊――那裡――不能壓啊」; old_vn (unif đã gộp) 「Há――ưm――Phư――á――chị, á,\nfau――fua――chỗ đó――bị ép vào thì.」; **fix = 「Há――ưm――Phư――á――chị, á,\nFau――Fua――chỗ đó――bị ép vào thì.」**. Đổi: 'á,\\nfau――fua――chỗ' → 'á,\\nFau――Fua――chỗ'.

**2218** — JP 「はぁっ――きて、来てる――双ちゃんの――\nあつい、の――おちん、ちん――ふ、あっ――」; TW 「哈――快來、來了――小雙――熱乎的――雞雞――呼、啊――」; old_vn (moan) 「Haa――vào, vào rồi――của Sou-chan――\nnóng, quá――dương, vật――fua, á――」; **fix = 「Haa――vào, vào rồi――của Sou-chan――\nnóng, quá――dương, vật――Fua, á――」**. Đổi: 'vật――fua,' → 'vật――Fua,'.

**2249** — JP 「か――はっ――あっ――ふあっ！ おくっ、ん、\nおくっ――きてる――子宮、に――子宮にぃっ！！」; TW 「啊――哈――啊――嗚啊！ 深處、深處――來了――子宮――子宮！！」; old_vn (moan) 「Ka――há――á――fua! Sâu quá, ưm,\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」; **fix = 「Ka――há――á――Fua! Sâu quá, ưm,\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」**. Đổi: '「Ka――há――á――fua!' → '「Ka――há――á――Fua!'.

**2276** — JP 「はむっ――ちゅっ――ちゅるっ――ころっ――\nん……ちゅるっ――れろっ、ころっっ――こりゅ」; TW 「啊嗚――啾――啾――咕溜――嗯……啾――舔、咕嘍――咕溜」; old_vn (unif đã gộp) 「Hamu――chụt――chụt――koro――\nưm……chụt――rero, koro――koryu.」; **fix = 「Hamu――chụt――chụt――Koro――\nưm……chụt――Rero, Koro――Koryu.」**. Đổi: '「Hamu――chụt――chụt――koro――\\nưm……chụt――rero,' → '「Hamu――chụt――chụt――Koro――\\nưm……chụt――Rero,'; 'koro――koryu.」' → 'Koro――Koryu.」'.

**2288** — JP 「ちゅうっ――ちゅっ――はむっ、あむっ――んっ\nちゅろおっ、ちゅろ、ころっ――ちゅうううううっ」; TW 「啾――啾――啊嗚、啊嗚――嗯啾囉、啾囉、咕溜――啾」; old_vn (unif đã gộp) 「Chụụt――chụt――hamu, amu――ưm\nchụt, chụt, koro――chụụụụụụt.」; **fix = 「Chụụt――chụt――Hamu, Amu――ưm\nchụt, chụt, Koro――chụụụụụụt.」**. Đổi: '「Chụụt――chụt――hamu,' → '「Chụụt――chụt――Hamu,'; 'amu――ưm\\nchụt,' → 'Amu――ưm\\nchụt,'; 'koro――chụụụụụụt.」' → 'Koro――chụụụụụụt.」'.

**2290** — JP 「ちゅっ――れ、るっ――ちゅうっ――ちゅっ、ちゅむ\nちゅるうっ――ちゅるっ――れろっ――れるううっ」; TW 「啾――嚕、溜――啾――啾、啾啾嚕――啾――舔――嚕唔唔」; old_vn (unif đã gộp) 「Chụt――re, rộp――chụụt――chụt, chụt\nchụụt――chụt――rero――rộộộp.」; **fix = 「Chụt――re, rộp――chụụt――chụt, chụt\nchụụt――chụt――Rero――rộộộp.」**. Đổi: 'chụt\\nchụụt――chụt――rero――rộộộp.」' → 'chụt\\nchụụt――chụt――Rero――rộộộp.」'.

**2292** — JP 「ちゅっっ――れるっ――れろ――ちゅる、る――\nん……すごか……ずっしり……ずっしり重かと」; TW 「啾――舔――嚕溜――啾嚕、溜――嗯……好厲害……好重……居然變得這麼重了」; old_vn (unif đã gộp) 「Chụt――rộp――rero――chụt, ru――\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」; **fix = 「Chụt――rộp――Rero――chụt, ru――\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」**. Đổi: '「Chụt――rộp――rero――chụt,' → '「Chụt――rộp――Rero――chụt,'.

**2299** — JP 「じゅううっ！ じゅぼっ！ じゅるる～～にゅぼっ！\nじゅるううっ――れるううっ――じゅぼ！ がぼっ！」; TW 「啾！ 啾啵！ 啾嚕～～呶啵！啾唔唔――嚕唔唔――啾啵！ 咳！」; old_vn (unif đã gộp) 「Juuu! Jubo! Jururu~~nyubo!\nJuruuu――rộộộp――jubo! Gabo!」; **fix = 「Juuu! Jubo! Jururu~~Nyubo!\nJuruuu――rộộộp――Jubo! Gabo!」**. Đổi: 'Jururu~~nyubo!\\nJuruuu――rộộộp――jubo!' → 'Jururu~~Nyubo!\\nJuruuu――rộộộp――Jubo!'.

**2307** — JP 「うぁ――あっ――あああ――あっ――」; TW 「嗚啊――啊――啊啊啊――啊――」; old_vn (moan) 「Ua――á――aaa――á――」; **fix = 「Ua――á――Aaa――á――」**. Đổi: '「Ua――á――aaa――á――」' → '「Ua――á――Aaa――á――」'.

**2311** — JP 「ふあっ！ あっ――ああああああっ！ んうううっ」; TW 「嗚啊！ 啊――啊啊啊啊啊啊！ 嗯嗚」; old_vn (moan) 「Fua! Á――aaaaaa! Nuuu」; **fix = 「Fua! Á――Aaaaaa! Nuuu」**. Đổi: 'Á――aaaaaa!' → 'Á――Aaaaaa!'.

**2316** — JP 「んっ――ちゅっ――チュむっ――ちゅうっ――んっ\nれるっ――ちゅうっ――ちゅぱっ――ちゅ、むっ――」; TW 「嗯――啾――啾――啾――嗯舔――啾――啾啪――啾、唔――」; old_vn (unif đã gộp) 「Ưm――chụt――chụt――chụụt――ưm\nrộp――chụụt――chụt――chụt, mu――」; **fix = 「Ưm――chụt――chụt――chụụt――ưm\nrộp――chụụt――chụt――chụt, Mu――」**. Đổi: 'mu――」' → 'Mu――」'.

**2330** — JP 「ん……は、ぁ……いけん、よ？ 双ちゃん。ね？\nあっ！？ ちゅっ――ちゅむっ――ちゅう……れるっ」; TW 「嗯……哈、啊……不行喔？ 小雙。好嗎？啊！？ 啾――啾唔――啾……舔」; old_vn (moan) 「Ưm……ha, a……không được, đâu? Sou-chan. Nè?\nA!? Chụt――chumu――chuu……rột.」; **fix = 「Ưm……Ha, a……không được, đâu? Sou-chan. Nè?\nA!? Chụt――Chumu――Chuu……rột.」**. Đổi: '「Ưm……ha,' → '「Ưm……Ha,'; 'Chụt――chumu――chuu……rột.」' → 'Chụt――Chumu――Chuu……rột.」'.

**2334** — JP 「ん……ちゅっ――んんっ――ぷあっ――\nおいしくは、なかけど――ん――ちゅるっ（ごくっ）」; TW 「嗯……啾――嗯嗯――噗啊――雖然不太好喝啦――嗯――啾（咕嘟）」; old_vn (unif đã gộp) 「Ưm……chụt――ưmm――pua――\nDù không, ngon lắm――ưm――chụt（ực）」; **fix = 「Ưm……chụt――ưmm――Pua――\nDù không, ngon lắm――ưm――chụt（ực）」**. Đổi: '「Ưm……chụt――ưmm――pua――\\nDù' → '「Ưm……chụt――ưmm――Pua――\\nDù'.

**2336** — JP 「ん……チュッ――ずろっ――ちゅる、るう、るっ」; TW 「嗯……啾――蹭――啾嚕、嚕、嚕」; old_vn (unif đã gộp) 「Ưm……chụt――zuro――chụt, ruu, ru.」; **fix = 「Ưm……chụt――Zuro――chụt, ruu, ru.」**. Đổi: '「Ưm……chụt――zuro――chụt,' → '「Ưm……chụt――Zuro――chụt,'.

**2348** — JP 「んふっ――んっ――はぁっ――ん――ちゅうっ――\nれるっ、れろおっ――ちゅ、ちゅむ――（かりっ！）」; TW 「嗯唔――嗯――哈――嗯――啾――舔、舔――啾、啾――（咬！）」; old_vn (unif đã gộp) 「Ưm phư――ưm――haa――ưm――chụụt――\nrộp, rero――chụt, chụt――(Cắn!)」; **fix = 「Ưm phư――ưm――Haa――ưm――chụụt――\nrộp, Rero――chụt, chụt――(Cắn!)」**. Đổi: 'phư――ưm――haa――ưm――chụụt――\\nrộp,' → 'phư――ưm――Haa――ưm――chụụt――\\nrộp,'; 'rero――chụt,' → 'Rero――chụt,'.

**2350** — JP 「んぷっ――んっ――れろっ――れろ、ずっ――じゅ、\nちゅっ――ちゅるう――ちゅ、れろっ――れるうっ」; TW 「嗯唔――嗯――舔――嚕囉、吱――啾、啾――啾嚕――啾、舔――舔」; old_vn (unif đã gộp) 「Ưmpu――ưm――rero――rero, zu――ju,\nchụt――chụụt――chụt, rero――rộộp.」; **fix = 「Ưmpu――ưm――Rero――Rero, Zu――Ju,\nchụt――chụụt――chụt, Rero――rộộp.」**. Đổi: '「Ưmpu――ưm――rero――rero,' → '「Ưmpu――ưm――Rero――Rero,'; 'zu――ju,\\nchụt――chụụt――chụt,' → 'Zu――Ju,\\nchụt――chụụt――chụt,'; 'rero――rộộp.」' → 'Rero――rộộp.」'.

**2363** — JP 「んっ！？ ふっ――あむっ――れろっ――ちゅるっ、\nちゅっ――れるっ――じゅむっ――ちゅ、ちゅううっ」; TW 「嗯！？ 呼――啊嗚――舔――啾、啾――舔――啾――啾、啾」; old_vn (unif đã gộp) 「Ưm!? Phư――amu――rột――churu,\nchụt――rộp――jumu――chu, chuuu.」; **fix = 「Ưm!? Phư――Amu――rột――Churu,\nchụt――rộp――Jumu――Chu, Chuuu.」**. Đổi: 'Phư――amu――rột――churu,\\nchụt――rộp――jumu――chu,' → 'Phư――Amu――rột――Churu,\\nchụt――rộp――Jumu――Chu,'; 'chuuu.」' → 'Chuuu.」'.

**2424** — JP 「ぴちょ、ぺちょ――ちゅうっ――ぺろろろっ！」; TW 「噗啾、呸啾――啾――呸囉！」; old_vn (unif đã gộp) 「Picho, pecho――chụụt――perororo!」; **fix = 「Picho, Pecho――chụụt――Perororo!」**. Đổi: 'pecho――chụụt――perororo!」' → 'Pecho――chụụt――Perororo!」'.

**2472** — JP 「来てっ！ 双ちゃんんっ！ おね、ちゃんっ、\nもう―イク――イっちゃう――けんっ――ふあっ！！」; TW 「射吧！ 小雙！ 姐姐，要高潮――高潮了――嗯――嗚啊！！」; old_vn (moan) 「Đến đi! Sou-chann! Chị, chị,\nsắp―ra――ra mất――rồi――fua!!」; **fix = 「Đến đi! Sou-chann! Chị, chị,\nsắp―ra――ra mất――rồi――Fua!!」**. Đổi: 'mất――rồi――fua!!」' → 'mất――rồi――Fua!!」'.

**2776** — JP 「はぁぁ――すきっ――好き、双ちゃんっ――\nおねえちゃん、おねえちゃん――最初から――ふあっ！」; TW 「蛤啊――喜歡――喜歡你，小雙――姐姐、姐姐――一開始就喜歡你――嗚啊！」; old_vn (moan) 「Haaa――thích――thích lắm, Sou-chan――\nchị, chị――ngay từ đầu đã――fua!」; **fix = 「Haaa――thích――thích lắm, Sou-chan――\nchị, chị――ngay từ đầu đã――Fua!」**. Đổi: 'đã――fua!」' → 'đã――Fua!」'.

#### 稀咲h1_性生活.txt.toml — 6 dòng

**1260** — JP 「ぁっ――ひあっ――あっ――イッて――いま――\nいって――るっ――か――あっ――待っ――んっ！？」; TW 「啊――咿啊――啊――射吧――快點――射吧――要射了――嗎――啊――等一下――嗯！？」; old_vn (moan) 「A――hia――a――ra đi――bây giờ――\nra――đi――a――đợi đã――ưm!?」; **fix = 「A――Hia――a――ra đi――bây giờ――\nra――đi――a――đợi đã――ưm!?」**. Đổi: '「A――hia――a――ra' → '「A――Hia――a――ra'.

**1283** — JP 「んっ――ふっ――ひあっ――あっ――」; TW 「嗯――呼――咿啊――啊――」; old_vn (moan) 「Ưm――fu――hia――a――」; **fix = 「Ưm――Fu――Hia――a――」**. Đổi: '「Ưm――fu――hia――a――」' → '「Ưm――Fu――Hia――a――」'.

**1349** — JP 「なんだ……双鉄――ンッ――はっ――おっぱい――\nもみもみ――した、かった――んっ――の？」; TW 「怎麼……雙鐵――嗯――哈――你早就想――揉一揉――胸部了――嗯――嗎？」; old_vn (unif đã gộp) 「Gì vậy…… Soutetsu――ưm――ha――ngực em――\nanh muốn――nắn bóp――lắm――ưm――sao?」; **fix = 「Gì vậy…… Soutetsu――ưm――Ha――ngực em――\nanh muốn――nắn bóp――lắm――ưm――sao?」**. Đổi: 'Soutetsu――ưm――ha――ngực' → 'Soutetsu――ưm――Ha――ngực'.

**1409** — JP 「最悪の……想像、よりは――ずうっと――楽――んっ\n……だから、双鉄――動い、て――ひゃんっ！？」; TW 「比我……最壞的想像――要好――得多――嗯……所以雙鐵――動起來吧――呀嗯！？」; old_vn (unif đã gộp) 「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\n……Vậy nên, Soutetsu――cử động, đi――hyan!?」; **fix = 「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\n……Vậy nên, Soutetsu――cử động, đi――Hyan!?」**. Đổi: 'đi――hyan!?」' → 'đi――Hyan!?」'.

**1473** — JP 「気持よく……そうか、ふふふ。\n双鉄は、気持ちよく、目覚めたんだね」; TW 「醒來的感覺嗎……這樣啊，呵呵。你這麼想就好了」; old_vn (unif đã gộp) 「Tâm trạng sảng khoái…… vậy sao, fufu.\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」; **fix = 「Tâm trạng sảng khoái…… vậy sao, Fufu.\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」**. Đổi: 'fufu.\\nSoutetsu,' → 'Fufu.\\nSoutetsu,'.

**1482** — JP 「先走り……の……汁……んっ――ふふっ、\n双鉄のペニスは、ボクの髪のこと――好き、みたいだね」; TW 「預射……液……嗯――呵呵、雙鐵的陰莖好像很喜歡――我的頭髮啊」; old_vn (unif đã gộp) 「Dịch…… nhờn rỉ ra…… ưm――fufu,\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」; **fix = 「Dịch…… nhờn rỉ ra…… ưm――Fufu,\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」**. Đổi: 'ưm――fufu,\\nDương' → 'ưm――Fufu,\\nDương'.

#### 稀咲h2_プライベートルーム.txt.toml — 7 dòng

**1108** — JP 「だめっ――こ、れっ――んっ――感じ――すぎっ――\nふうっっっ――」; TW 「不行――這個――嗯――太有――感覺了――呼――」; old_vn (moan) 「Không được――cái, này――ưm――cảm giác――quá――\nfuu――」; **fix = 「Không được――cái, này――ưm――cảm giác――quá――\nFuu――」**. Đổi: 'giác――quá――\\nfuu――」' → 'giác――quá――\\nFuu――」'.

**1120** — JP 「顔……双鉄……溶けちゃってる……よ？\n……あっ――ふっ――んっ……」; TW 「你的……表情……已經亂了……喔……啊――呼――嗯……」; old_vn (unif đã gộp) 「Khuôn mặt…… của Soutetsu…… tan chảy ra rồi…… kìa?\n……A――fu――ưm……」; **fix = 「Khuôn mặt…… của Soutetsu…… tan chảy ra rồi…… kìa?\n……A――Fu――ưm……」**. Đổi: 'kìa?\\n……A――fu――ưm……」' → 'kìa?\\n……A――Fu――ưm……」'.

**1166** — JP 「ひっ――あっ――っ――ふっ――双――て、つっ――\nんっ――ゆる――してっ――ボクっ――ボク――もうっ」; TW 「咿――啊――嗚――雙――鐵――嗯――放過――我吧――我――我――不行了」; old_vn (unif đã gộp) 「Hi――a――ưm――fu――Sou――tetsu――\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」; **fix = 「Hi――a――ưm――Fu――Sou――tetsu――\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」**. Đổi: '「Hi――a――ưm――fu――Sou――tetsu――\\nƯm――tha――cho' → '「Hi――a――ưm――Fu――Sou――tetsu――\\nƯm――tha――cho'.

**1205** — JP 「んっ――はっ――あっ――双っ――鉄っ――」; TW 「嗯――哈――啊――雙――鐵――」; old_vn (unif đã gộp) 「Ưm――ha――a――Sou――tetsu――」; **fix = 「Ưm――Ha――a――Sou――tetsu――」**. Đổi: '「Ưm――ha――a――Sou――tetsu――」' → '「Ưm――Ha――a――Sou――tetsu――」'.

**1250** — JP 「そう、なんだ――だか、ら……んっ――ふあっ――\n特に……先っぽ――は――ねっ？ ――ん――ちゅぷっ」; TW 「就是這樣――所以呢……嗯――嗚啊――尤其是……頂端――知――道嗎？ ――嗯――啾噗」; old_vn (unif đã gộp) 「Đúng, là vậy đó――Cho, nên…… ưm――fua――\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chụt」; **fix = 「Đúng, là vậy đó――Cho, nên…… ưm――Fua――\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chụt」**. Đổi: 'ưm――fua――\\nĐặc' → 'ưm――Fua――\\nĐặc'.

**1253** — JP 「おしり……はっ――まだっ――準備――んっ――\nちゃんと――出来て――ない、からっ――」; TW 「屁眼……還――還沒有――準備――嗯――好――呢――」; old_vn (moan) 「Mông…… ha――vẫn chưa――chuẩn bị――ưm――\nsẵn sàng――đâu, nên là――」; **fix = 「Mông…… Ha――vẫn chưa――chuẩn bị――ưm――\nsẵn sàng――đâu, nên là――」**. Đổi: 'ha――vẫn' → 'Ha――vẫn'.

**1267** — JP 「ボク、ね？ ここは――んっ――感じる、とこ――んっ\n……ふぁ……こうやっ、って……すり、すり――し、て」; TW 「我啊，我的這裡――嗯――就是敏感帶――嗯……哇……只要這樣……輕輕地摩擦――」; old_vn (moan) 「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\n……fa…… chỉ cần làm thế, này…… xoa, xoa――thôi」; **fix = 「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\n……Fa…… chỉ cần làm thế, này…… xoa, xoa――thôi」**. Đổi: 'được――ưm\\n……fa……' → 'được――ưm\\n……Fa……'.

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml — 8 dòng

**2152** — JP 「ひゃっ――はっ――かふっ――ふあっ――それ――\nゆっくり――ゆっくり――されたらっ――――」; TW 「呀――哈――哈呼――嗚啊――那是――慢慢地――慢慢地――來的話――」; old_vn (moan) 「Hya――hà――khaphu――Fua――cái đó――\nNếu bị――làm――chậm rãi――chậm rãi――――」; **fix = 「Hya――hà――Khaphu――Fua――cái đó――\nNếu bị――làm――chậm rãi――chậm rãi――――」**. Đổi: '「Hya――hà――khaphu――Fua――cái' → '「Hya――hà――Khaphu――Fua――cái'.

**2203** — JP 「は……んっ――ふ、ぁ……手……双鉄の、手――\nあったか――ふっ……はぁ……はふっ」; TW 「哈……嗯――呼、啊……手……雙鐵的手――熱呼呼的――呼……蛤啊……哈呼」; old_vn (unif đã gộp) 「Ha…… ưm――Fu, a…… tay…… tay của, Soutetsu――\nấm quá――fu…… ha…… ha fu」; **fix = 「Ha…… ưm――Fu, a…… tay…… tay của, Soutetsu――\nấm quá――Fu…… Ha…… Ha fu」**. Đổi: 'quá――fu……' → 'quá――Fu……'; 'ha……' → 'Ha……'; 'ha' → 'Ha'.

**2206** — JP 「はっ！？ ひゅっ――ひあ――それっ――なにっ」; TW 「哈！？ 咿――咿啊――那是――什麼」; old_vn (moan) 「Hả!? Hyu――hia――cái đó――là gì vậy」; **fix = 「Hả!? Hyu――Hia――cái đó――là gì vậy」**. Đổi: 'Hyu――hia――cái' → 'Hyu――Hia――cái'.

**2238** — JP 「あむっ――んっ――ふぁ……んっ――ちゅむっ\nほーへふっ――ふっ――しゅき――んっ――ちゅっ」; TW 「啊嗚――嗯――哇……嗯――啾唔啊嗚――呼――喜歡――嗯――啾」; old_vn (unif đã gộp) 「A mu――ưm――fa…… ưm――chu mu\nAnh Houhefu――fu――hích anh――ưm――chụt」; **fix = 「A mu――ưm――Fa…… ưm――chu mu\nAnh Houhefu――Fu――hích anh――ưm――chụt」**. Đổi: 'mu――ưm――fa……' → 'mu――ưm――Fa……'; 'Houhefu――fu――hích' → 'Houhefu――Fu――hích'.

**2254** — JP 「ふあっ！ ペニスっ――すごい――双鉄っ――\nこんなに、硬くっ――て――ふ、あっ――熱いっ」; TW 「嗚啊！ 陰莖――好棒――雙鐵――已經這麼硬了――呼、啊――好熱」; old_vn (unif đã gộp) 「Fua! Dương vật――tuyệt quá――Soutetsu――\nCứng――như thế này――phu, á――nóng quá」; **fix = 「Fua! Dương vật――tuyệt quá――Soutetsu――\nCứng――như thế này――Phu, á――nóng quá」**. Đổi: 'này――phu,' → 'này――Phu,'.

**2265** — JP 「ん……ふっ――んっ――ちゅっ――ちゅむっ――\nちゅるっ――ちゅっ――んちゅっ――ふ……あ――」; TW 「嗯……呼――嗯――啾――啾唔――啾――啾――嗯啾――呼……啊――」; old_vn (unif đã gộp) 「Ưm…… fu――ưm――chụt――chu mu――\nchu ru――chụt――ưm chu――Fu…… a――」; **fix = 「Ưm…… Fu――ưm――chụt――chu mu――\nchu ru――chụt――ưm chu――Fu…… a――」**. Đổi: 'fu――ưm――chụt――chu' → 'Fu――ưm――chụt――chu'.

**2269** — JP 「ん……ちゅっ――ふっ――ちゅむっ――ちゅっ、\nちゅるっ――れろっ――れるうっ――ちゅむっ」; TW 「嗯……啾――呼――啾唔――啾、啾――舔――舔――啾唔」; old_vn (unif đã gộp) 「Ưm……chụt――phu――chụt――chụt,\nchụt――rero――Rộộp――chụt」; **fix = 「Ưm……chụt――Phu――chụt――chụt,\nchụt――Rero――Rộộp――chụt」**. Đổi: '「Ưm……chụt――phu――chụt――chụt,\\nchụt――rero――Rộộp――chụt」' → '「Ưm……chụt――Phu――chụt――chụt,\\nchụt――Rero――Rộộp――chụt」'.

**2465** — JP 「普通は、体を見ると思う。男でも、女でさえも。\nでも、双鉄は真っ先にボクの顔を見て――うふふっ」; TW 「我覺得一般人都會瞅著身體看，無論男女。但是你就只盯著我的臉看――呵呵」; old_vn (unif đã gộp) 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――ufufu」; **fix = 「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――Ufufu」**. Đổi: 'tiên――ufufu」' → 'tiên――Ufufu」'.

### 4.5. O7 — 37 dòng (13 file). U14a F-O7-1 — Soutetsu→Olivy / →Hachiroku “cô” → “em”

#### グランドリライト01_オール御一夜、成立ならず.txt.toml — 1 dòng

**2161** — JP 「ハチロクもどうだ？ イヤでなければ」; TW 「八六如果不嫌棄，也來跟我約好吧」; old_vn (CSV3) 「Hachiroku cũng tham gia chứ? Nếu cô không phiền.」; **fix = 「Hachiroku cũng tham gia chứ? Nếu em không phiền.」**. Đổi: 'cô' → 'em'.

#### グランドリライト02_ナビ.txt.toml — 1 dòng

**1881** — JP 「お前の気持ちは嬉しいが、[ハチロク,3]8620のことが無くとも――\n今回だけは、僕は、一人旅をしたいのだ」; TW 「雖然你有這份心我很高興，但是就算沒有[八六,3]８６２０的事——至少這次，我也想獨自一個人去」; old_vn (CSV3) 「Tôi rất vui vì tấm lòng của cô, nhưng dù không có chuyện của 8620――\nChỉ lần này thôi, tôi muốn đi một mình.」; **fix = 「Tôi rất vui vì tấm lòng của em, nhưng dù không có chuyện của 8620――\nChỉ lần này thôi, tôi muốn đi một mình.」**. Đổi: 'cô,' → 'em,'.

#### グランドリライト06_稀咲.txt.toml — 2 dòng

**1945** — JP 「お前が言ったことだろう。餅は餅屋。汽車は汽車屋。\n――それぞれが、それぞれの役割を最善に果たせばいい」; TW 「你不是說過嗎，術業有專攻。每個人盡力做好自己分內的事就夠了」; old_vn (audit) 「Chính cô đã nói mà. Việc của thợ làm bánh thì để thợ làm bánh lo. Việc của thợ làm tàu thì để thợ làm tàu lo.\n——Mỗi người chỉ cần hoàn thành tốt nhất vai trò của mình là được.」; **fix = 「Chính em đã nói mà. Việc của thợ làm bánh thì để thợ làm bánh lo. Việc của thợ làm tàu thì để thợ làm tàu lo.\n——Mỗi người chỉ cần hoàn thành tốt nhất vai trò của mình là được.」**. Đổi: 'cô' → 'em'.

**2116** — JP 「うむ。今日のところはよろしく頼む」; TW 「嗯，今天就靠你了」; old_vn (audit) 「Ừm. Hôm nay trông cậy vào cô đấy.」; **fix = 「Ừm. Hôm nay trông cậy vào em đấy.」**. Đổi: 'cô' → 'em'.

#### ハチロク03_冥国式レイルロオド.txt.toml — 3 dòng

**2039** — JP 「オリヴィから、なにか――\n例えば、過去に関する\x%l共感;#00ffc040;共感%l;#;などを受け取ったのか？」; TW 「你從奧莉薇那裡——是不是通過\x%l共感;#00ffc040;共鳴%l;#;接收到關於她過去的什麼訊息了？」; old_vn (CSV3) 「Cô đã nhận được gì đó từ Olivy——\nví dụ như \x%l共感;#00ffc040;cộng cảm%l;#; về quá khứ chẳng hạn?」; **fix = 「Em đã nhận được gì đó từ Olivy——\nví dụ như \x%l共感;#00ffc040;cộng cảm%l;#; về quá khứ chẳng hạn?」**. Đổi: '「Cô' → '「Em'.

**2216** — JP 「ああ、だから前照灯をとっさに消灯してくれたのか」; TW 「啊，所以你才能迅速關掉了頭燈啊」; old_vn (CSV3) 「À, ra đó là lý do cô tắt đèn pha ngay lập tức sao.」; **fix = 「À, ra đó là lý do em tắt đèn pha ngay lập tức sao.」**. Đổi: 'cô' → 'em'.

**2386** — JP 「わかっている。お前が最高の性能を発揮できるのは\n僕と組んでいるときだ。そして、その逆もまた真実だ」; TW 「我明白。要發揮出你的最高性能，還得是在和我搭檔的時候。而反過來也是不爭的事實」; old_vn (CSV3) 「Tôi hiểu. Lúc cô có thể phát huy tối đa hiệu suất\nlà khi bắt cặp với tôi. Và ngược lại cũng đúng như vậy.」; **fix = 「Tôi hiểu. Lúc em có thể phát huy tối đa hiệu suất\nlà khi bắt cặp với tôi. Và ngược lại cũng đúng như vậy.」**. Đổi: 'cô' → 'em'.

#### ハチロク05_レイルロオドたち.txt.toml — 2 dòng

**2539** — JP 「オリヴィ。おまえは――自分が毎年、\n全検を受けることを推奨される状態なのだと」; TW 「奧莉薇。以你目前的狀態，現在每年最好接受全檢，這件事你是否知情——」; old_vn (CSV3) 「Olivy. Cô——có biết rằng tình trạng của mình hiện tại,\nđược khuyến cáo là năm nào cũng phải kiểm tra toàn diện không?」; **fix = 「Olivy. Em——có biết rằng tình trạng của mình hiện tại,\nđược khuyến cáo là năm nào cũng phải kiểm tra toàn diện không?」**. Đổi: 'Cô' → 'Em'.

**2663** — JP 「まいてつになるためには金が必要で、\nお前には、その金を稼ぐ手段があるといっているのだ」; TW 「成為掌車人需要資金，而你有獲取這些資金的手段」; old_vn (audit) 「Để trở thành chủ tàu thì cần tiền,\nvà anh đang nói là cô có cách để kiếm số tiền đó.」; **fix = 「Để trở thành chủ tàu thì cần tiền,\nvà anh đang nói là em có cách để kiếm số tiền đó.」**. Đổi: 'cô' → 'em'.

#### ハチロク13_実りの秋.txt.toml — 2 dòng

**1833** — JP 「ああ、そうだな。\n言われてみればまったくもって指摘の通りだ」; TW 「啊，可不是。你這麼一說還真真兒就是這麼個感覺」; old_vn (CSV3) 「À, đúng vậy.\nNghe cô nói thì quả thật là hoàn toàn đúng như vậy.」; **fix = 「À, đúng vậy.\nNghe em nói thì quả thật là hoàn toàn đúng như vậy.」**. Đổi: 'cô' → 'em'.

**1970** — JP 「了解だ。そのときの体温が40.9度以下なら、\n大歓迎で仕事をしてもらおう」; TW 「我明白了。如果到時體溫在四十點九度以下的話，我自然樂意讓你以新身份開始工作」; old_vn (CSV3) 「Rõ rồi. Nếu lúc đó nhiệt độ dưới 40.9 độ,\nthì rất hoan nghênh cô làm việc.」; **fix = 「Rõ rồi. Nếu lúc đó nhiệt độ dưới 40.9 độ,\nthì rất hoan nghênh em làm việc.」**. Đổi: 'cô' → 'em'.

#### ハチロク14_冬.txt.toml — 13 dòng

**2427** — JP 「オリヴィは、そのまま聞き取りを続けてくれるか？\nその、僕と似た口調の方のお名前は？」; TW 「你能繼續打聽情況嗎？那位跟我說話很像的先生怎麼稱呼？」; old_vn (CSV3) 「Olivy, cô có thể tiếp tục nghe ngóng thêm được không?\nÔng lão có cách nói chuyện giống tôi tên là gì?」; **fix = 「Olivy, em có thể tiếp tục nghe ngóng thêm được không?\nÔng lão có cách nói chuyện giống tôi tên là gì?」**. Đổi: 'cô' → 'em'.

**2510** — JP 「すまんが、本格的な時間外労働を頼むかもしれん」; TW 「可能最近這段時間，是真需要拜託你加班了」; old_vn (CSV3) 「Xin lỗi nhé, nhưng có lẽ sẽ phải nhờ cô làm ngoài giờ thực sự đấy.」; **fix = 「Xin lỗi nhé, nhưng có lẽ sẽ phải nhờ em làm ngoài giờ thực sự đấy.」**. Đổi: 'cô' → 'em'.

**2743** — JP 「そうと……自覚できるような何かがあるのか」; TW 「如此說來……是有什麼根據讓你這麼覺得嗎」; old_vn (CSV3) 「Cô có thể…… tự nhận thức được điều đó sao.」; **fix = 「Em có thể…… tự nhận thức được điều đó sao.」**. Đổi: '「Cô' → '「Em'.

**2772** — JP 「ああ。並行して、その他の異変がないかどうかも、\n無理ない範囲で聞き取り調査をしてくれるか？」; TW 「對，另外希望你與此同時，儘可能打聽一下有沒有發現其他異常狀況？」; old_vn (CSV3) 「Ừ. Song song đó, cô có thể nghe ngóng xem\ncó dấu hiệu bất thường nào khác trong phạm vi có thể không?」; **fix = 「Ừ. Song song đó, em có thể nghe ngóng xem\ncó dấu hiệu bất thường nào khác trong phạm vi có thể không?」**. Đổi: 'cô' → 'em'.

**2885** — JP 「で？\n体温は、どうやってごまかしたんだ？」; TW 「所以，你能說說你是怎麼騙過我們的嗎？」; old_vn (CSV3) 「Thế?\nNhiệt độ cơ thể, cô đã lấp liếm bằng cách nào?」; **fix = 「Thế?\nNhiệt độ cơ thể, em đã lấp liếm bằng cách nào?」**. Đổi: 'cô' → 'em'.

**2908** — JP 「了解した。現場までもナビに送らせよう」; TW 「明白，我也直接派Ｎａｖｉ把你送過去吧」; old_vn (CSV3) 「Đã rõ. Tôi sẽ bảo Navi đưa cô đến tận hiện trường.」; **fix = 「Đã rõ. Tôi sẽ bảo Navi đưa em đến tận hiện trường.」**. Đổi: 'cô' → 'em'.

**2979** — JP 「流さんも言っていたが、長丁場になるかもしれん。\nできるだけ早く、ともかく専門家に診てもらおう」; TW 「流先生也說了，這可能會是一場持久戰，要儘早讓專家看看你的情況」; old_vn (CSV3) 「Ông Nagare cũng đã nói, có thể sẽ là một cuộc chiến trường kỳ.\nCàng sớm càng tốt, dù sao cũng phải nhờ chuyên gia khám cho cô.」; **fix = 「Ông Nagare cũng đã nói, có thể sẽ là một cuộc chiến trường kỳ.\nCàng sớm càng tốt, dù sao cũng phải nhờ chuyên gia khám cho em.」**. Đổi: 'cô.」' → 'em.」'.

**2986** — JP 「そうするためにも、どうか延命の可能性にかけてくれ。\n僕ら全員が、ここで、オリヴィの代わりに監視するから」; TW 「為此，你要儘可能對延壽寄予希望，我們所有人都會代替你觀察這裡的情況」; old_vn (CSV3) 「Để làm được điều đó, xin cô hãy đánh cược vào khả năng kéo dài tuổi thọ.\nTất cả chúng tôi, sẽ ở đây, giám sát thay cho Olivy.」; **fix = 「Để làm được điều đó, xin em hãy đánh cược vào khả năng kéo dài tuổi thọ.\nTất cả chúng tôi, sẽ ở đây, giám sát thay cho Olivy.」**. Đổi: 'cô' → 'em'.

**3152** — JP 「そうか、ならば――今すぐにでもナビにおくらせ」; TW 「這樣啊，那我現在就讓Ｎａｖｉ送你回去」; old_vn (CSV3) 「Vậy sao, nếu thế thì——để Navi đưa cô về ngay bây giờ.」; **fix = 「Vậy sao, nếu thế thì——để Navi đưa em về ngay bây giờ.」**. Đổi: 'cô' → 'em'.

**3165** — JP 「では、その石田さんに、\n近辺で井戸水を使っている世帯がないかを確かめてくれ」; TW 「那你再問問石田先生，他家附近有沒有其他用井水的人家」; old_vn (CSV3) 「Vậy thì, nhờ cô hỏi ông Ishida xem,\nquanh đó có hộ nào dùng nước giếng nữa không nhé.」; **fix = 「Vậy thì, nhờ em hỏi ông Ishida xem,\nquanh đó có hộ nào dùng nước giếng nữa không nhé.」**. Đổi: 'cô' → 'em'.

**3169** — JP 「そのことは、登呂流湯さんには？」; TW 「那你有向登呂流浴場老闆反映這一情況嗎？」; old_vn (CSV3) 「Chuyện đó, cô đã nói với ông Tororyu-yu chưa?」; **fix = 「Chuyện đó, em đã nói với ông Tororyu-yu chưa?」**. Đổi: 'cô' → 'em'.

**3186** — JP 「では、くれぐれも無理のないよう行動してくれ。\n辛くなったらすぐ連絡を、ナビを迎えにいかせるゆえ」; TW 「那好吧，切記不要勉強，如果覺得難受就立刻聯絡我們，我會派Ｎａｖｉ來接你」; old_vn (CSV3) 「Vậy thì, xin cô tuyệt đối đừng cố quá sức.\nNếu thấy mệt thì liên lạc ngay, tôi sẽ bảo Navi đến đón.」; **fix = 「Vậy thì, xin em tuyệt đối đừng cố quá sức.\nNếu thấy mệt thì liên lạc ngay, tôi sẽ bảo Navi đến đón.」**. Đổi: 'cô' → 'em'.

**3220** — JP 「ではまた後ほど。よろしく頼む」; TW 「那我們稍後再見，麻煩你了」; old_vn (CSV3) 「Vậy hẹn gặp lại sau. Nhờ cô nhé.」; **fix = 「Vậy hẹn gặp lại sau. Nhờ em nhé.」**. Đổi: 'cô' → 'em'.

#### ポーレット08_線から面へ.txt.toml — 1 dòng

**1623** — JP 「無理をさせることは申し訳ない」; TW 「抱歉，難為你了」; old_vn (CSV3) 「Xin lỗi vì đã bắt ép cô.」; **fix = 「Xin lỗi vì đã bắt ép em.」**. Đổi: 'cô.」' → 'em.」'.

#### 共通02_日々姫と真闇と人形と.txt.toml — 4 dòng

**2133** — JP 「最初から……そうだな、お前……君の怒りを、\n僕が躱してしまった過ち、そこからを」; TW 「從最開始的地方……重來吧，從我躲過了你憤怒的一掌那裡」; old_vn (CSV3) 「Từ lúc bắt đầu……phải rồi, cô……Từ sai lầm của tôi,\nkhi đã né tránh cơn giận của cô.」; **fix = 「Từ lúc bắt đầu……phải rồi, em……Từ sai lầm của tôi,\nkhi đã né tránh cơn giận của em.」**. Đổi: 'cô……Từ' → 'em……Từ'; 'cô.」' → 'em.」'.

**2224** — JP 「身の処し方と言っていたが――\nハチロクに、なにか希望はあるのか？」; TW 「既然已經決定留在這裡，那你有什麼想要做的事嗎？」; old_vn (CSV3) 「Cô vừa nói đến chuyện nơi ăn chốn ở——\nHachiroku có nguyện vọng gì không?」; **fix = 「Em vừa nói đến chuyện nơi ăn chốn ở——\nHachiroku có nguyện vọng gì không?」**. Đổi: '「Cô' → '「Em'.

**2435** — JP 「行くさ。僕は君のオーナーとなったのだからな。\n君を大切に扱う義務がある」; TW 「要去的。既然我成為了你的主人，那我就有認真對待你的義務」; old_vn (CSV3) 「Phải đi chứ. Tôi đã trở thành chủ sở hữu của cô rồi mà.\nTôi có nghĩa vụ phải trân trọng cô.」; **fix = 「Phải đi chứ. Tôi đã trở thành chủ sở hữu của em rồi mà.\nTôi có nghĩa vụ phải trân trọng em.」**. Đổi: 'cô' → 'em'; 'cô.」' → 'em.」'.

**2536** — JP 「そこへ案内したいのだが。\nハチロク、僕はどのように君をエスコートすれば良いか」; TW 「那我帶你過去吧。八六，我該如何護送你才好呢？」; old_vn (CSV3) 「Tôi muốn dẫn cô đến đó.\nHachiroku, tôi nên hộ tống cô như thế nào đây?」; **fix = 「Tôi muốn dẫn em đến đó.\nHachiroku, tôi nên hộ tống em như thế nào đây?」**. Đổi: 'cô' → 'em'; 'cô' → 'em'.

#### 凪ふかみ02_命の重さ.txt.toml — 2 dòng

**1226** — JP 「大丈夫か？ というか、すまん。\n傘のひとつも差し掛けてやればよかったか」; TW 「你沒事吧？說起來真不好意思，要是剛才給你一把傘就好了」; old_vn (CSV3) 「Cô không sao chứ? Mà, xin lỗi.\nĐáng lẽ tôi nên đưa cho cô một chiếc ô.」; **fix = 「Em không sao chứ? Mà, xin lỗi.\nĐáng lẽ tôi nên đưa cho em một chiếc ô.」**. Đổi: '「Cô' → '「Em'; 'cô' → 'em'.

**1325** — JP 「ああ、言われれば、だな」; TW 「啊，你這麼一說，倒也是」; old_vn (CSV3) 「À, nghe cô nói mới thấy đúng thật.」; **fix = 「À, nghe em nói mới thấy đúng thật.」**. Đổi: 'cô' → 'em'.

#### 凪ふかみ03_みかんの旅.txt.toml — 3 dòng

**2099** — JP 「感じていたか。さすがだな」; TW 「你感覺到了啊，厲害」; old_vn (CSV3) 「Cô cũng cảm nhận được sao. Giỏi thật đấy.」; **fix = 「Em cũng cảm nhận được sao. Giỏi thật đấy.」**. Đổi: '「Cô' → '「Em'.

**2317** — JP 「ああ――そうか。\nまさしく、言われてみればそのとおりだ」; TW 「噢……原來是這樣。聽你這麼說我就明白了」; old_vn (CSV3) 「A——ra là vậy.\nNghe cô nói mới thấy, quả đúng là thế thật.」; **fix = 「A——ra là vậy.\nNghe em nói mới thấy, quả đúng là thế thật.」**. Đổi: 'cô' → 'em'.

**2581** — JP 「いや――むしろ助かる。\n僕ひとりでは、行き詰まりそうになっていたところだ」; TW 「沒有，你來得正好。這個問題我一個人想不通」; old_vn (CSV3) 「Không——ngược lại cô đã giúp tôi đấy.\nNếu chỉ có một mình, tôi e là sẽ bế tắc mất.」; **fix = 「Không——ngược lại em đã giúp tôi đấy.\nNếu chỉ có một mình, tôi e là sẽ bế tắc mất.」**. Đổi: 'cô' → 'em'.

#### 日々姫05_市議会見学.txt.toml — 1 dòng

**1854** — JP 「気が利くな、ハチロク。ありがたい」; TW 「八六，還好你反應快」; old_vn (CSV3) 「Cô chu đáo thật đấy, Hachiroku. Cảm ơn nhé.」; **fix = 「Em chu đáo thật đấy, Hachiroku. Cảm ơn nhé.」**. Đổi: '「Cô' → '「Em'.

#### 日々姫05_御一夜ステーションカフェ.txt.toml — 2 dòng

**2313** — JP 「すまん。待たせてしまったな」; TW 「抱歉。讓你久等了」; old_vn (CSV3) 「Xin lỗi. Đã để cô phải đợi rồi.」; **fix = 「Xin lỗi. Đã để em phải đợi rồi.」**. Đổi: 'cô' → 'em'.

**2338** — JP 「レイルロオドだからこそ、朝の時間は貴重だろう。\n待たせてまで聞きたかったのも小さなことで申し訳ない」; TW 「早上的時光對鐵路人偶來說更是珍貴吧。就為了問一件小事而讓你久等，我真的很過意不去」; old_vn (CSV3) 「Chính vì là Railord nên thời gian buổi sáng mới quý giá chứ.\nBắt cô phải đợi chỉ để hỏi một chuyện nhỏ nhặt, thật ngại quá.」; **fix = 「Chính vì là Railord nên thời gian buổi sáng mới quý giá chứ.\nBắt em phải đợi chỉ để hỏi một chuyện nhỏ nhặt, thật ngại quá.」**. Đổi: 'cô' → 'em'.

### 4.6. O25 — 3 dòng (1 file). U14b F-O25-1 — lr h1 1616/1687/1737 → “tớ”/“cậu”

#### lr_凪ふかみh1_じぇいけい！.txt.toml — 3 dòng

**1616** — JP 「あ、うふふ。そういうことですねぇ。わかりました。\nえっとね？ 凪ちゃん、多分――――――こうっ！？」; TW 「啊，嘻嘻嘻……是這樣呀。好的。聽我說，小凪，大概……是這樣的！」; old_vn (CSV3) 「A, ufufu. Ra là vậy nhỉ. Em hiểu rồi.\nƯm nè? Nagi, chắc là——————thế này!?」; **fix = 「A, Ufufu. Ra là vậy nhỉ. Tớ hiểu rồi.\nƯm nè? Nagi, chắc là——————thế này!?」**. Đổi: 'ufufu.' → 'Ufufu.'; 'Em' → 'Tớ'.

**1687** — JP 「うふふっ、よく言えました」; TW 「嘻嘻嘻，說得好」; old_vn (CSV3) 「Ufufu, em nói giỏi lắm.」; **fix = 「Ufufu, cậu nói giỏi lắm.」**. Đổi: 'em' → 'cậu'.

**1737** — JP 「凪ちゃん、どうしてほしいの？ ちゃあんとおくちで、\n双鉄おにいさんにおねだりしないと」; TW 「小凪，你想雙鐵哥哥怎麼做？你要親口求他哦」; old_vn (CSV3) 「Nagi, em muốn sao nào? Phải dùng miệng,\nnũng nịu anh Soutetsu đàng hoàng chứ.」; **fix = 「Nagi, cậu muốn sao nào? Phải dùng miệng,\nnũng nịu anh Soutetsu đàng hoàng chứ.」**. Đổi: 'em' → 'cậu'.

### 4.7. O46 — 1 dòng (1 file). U14c O46 — ハチロク15a 2345 “Olive” → “Olivy”

#### ハチロク15a_痛みとの決別.txt.toml — 1 dòng

**2345** — JP オリヴィ; TW ; old_vn (TOML-2 [characters]) Olive; **fix = Olivy**. Đổi: 'Olive' → 'Olivy'.

### 4.8. M7 — 1 dòng (1 file). U10b F2 — M7: ポーレットh8 2241 くっ → “Ku”

#### ポーレットh8_気動車の国のアリス.txt.toml — 1 dòng

**2241** — JP 「はきゅっ！？ くっ――ふうううううっ」」; TW 「啊呀！？啊——呼啊」; old_vn (moan) 「Hakyu!? Hự——phuuuuuu」; **fix = 「Hakyu!? Ku——Phuuuuuu」**. Đổi: 'Hự' → 'Ku'; 'phuuuuuu」' → 'Phuuuuuu」'.

### 4.9. M10 — 1 dòng (1 file). U10b F3 — M10: ポーレットh8 2185 ふえ → “Hể!?”

#### ポーレットh8_気動車の国のアリス.txt.toml — 1 dòng

**2185** — JP 「ふえっ！？」; TW 「哎！？」; old_vn (moan) 「Fue!?」; **fix = Hể!?**. Đổi: '「Fue!?」' → 'Hể!?'.

### 4.10. Munakata — 48 dòng (6 file). Munakata “tôi” → “tao” (55 dòng, không 俺 rõ)

#### ハチロク02_ハートブレイク・レイルロオド.txt.toml — 2 dòng

**2352** — JP 「今日は助士無しで来ました。オリヴィはお任せします。\nできれば、速やかに調印の方を済ませたいのですが」; TW 「我們今天沒有帶司爐，奧莉薇就交給貴公司了。可以的話我希望能夠儘快完成手續」; old_vn (CSV3) 「Hôm nay tôi đến mà không có phụ lái. Olivy xin nhờ mọi người chăm sóc.\nNếu được, tôi muốn nhanh chóng hoàn tất việc ký kết.」; **fix = 「Hôm nay tao đến mà không có phụ lái. Olivy xin nhờ mọi người chăm sóc.\nNếu được, tao muốn nhanh chóng hoàn tất việc ký kết.」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**2406** — JP 「すまない――すみませんが、[ひない,1]雛衣社長は」; TW 「抱歉——不好意思，請問雛衣社長在哪」; old_vn (CSV3) 「Xin lỗi——cho tôi hỏi, Giám đốc Hinai có ở đây không.」; **fix = 「Xin lỗi——cho tao hỏi, Giám đốc Hinai có ở đây không.」**. Đổi: 'tôi' → 'tao'.

#### ハチロク04_小畑越え.txt.toml — 11 dòng

**1845** — JP 「問題があることは理解した。\n……理解はしたが」; TW 「你們要提出的問題我明白了……可是」; old_vn (CSV3) 「Tôi hiểu vấn đề rồi.\n……Hiểu thì hiểu, nhưng」; **fix = 「Tao hiểu vấn đề rồi.\n……Hiểu thì hiểu, nhưng」**. Đổi: '「Tôi' → '「Tao'.

**2113** — JP 「そんな業務の経験はなかった。\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は命令を守るものだからな」; TW 「對此我沒有任何經驗。畢竟\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;本就應該服從命令」; old_vn (CSV3) 「Tôi chưa từng có kinh nghiệm làm việc đó.\nVì \x%lレイルロオド;#00ffc040;Railord%l;#; vốn là thứ phải tuân theo mệnh lệnh mà.」; **fix = 「Tao chưa từng có kinh nghiệm làm việc đó.\nVì \x%lレイルロオド;#00ffc040;Railord%l;#; vốn là thứ phải tuân theo mệnh lệnh mà.」**. Đổi: '「Tôi' → '「Tao'.

**2116** — JP 「ああ。全て合意の上、確認をとっての行動だ。\n今更クレームを持ち込まれても――正直困る」; TW 「對，一切都建立在符合彼此意向，並得到許可的前提之上。然而貴公司如今又對此心存不滿。說實話，我很為難」; old_vn (CSV3) 「Đúng vậy. Tất cả đều là hành động sau khi đã xác nhận và được sự đồng ý.\nGiờ mới mang khiếu nại đến――thú thật là tôi rất khó xử.」; **fix = 「Đúng vậy. Tất cả đều là hành động sau khi đã xác nhận và được sự đồng ý.\nGiờ mới mang khiếu nại đến――thú thật là tao rất khó xử.」**. Đổi: 'tôi' → 'tao'.

**2223** — JP 「上と相談し、そのことを御社にも報告した。すると、\n御社社長も『そういうことなら是非に』と乗り気で」; TW 「我在與上司商討之後，也將這一情況告知了貴公司，於是貴公司社長也非常樂意，很快就答應了」; old_vn (CSV3) 「Tôi đã thảo luận với cấp trên, và báo cáo việc đó cho công ty cậu. Sau đó,\ngiám đốc công ty cậu cũng rất hào hứng 'Nếu vậy thì nhất định phải làm'.」; **fix = 「Tao đã thảo luận với cấp trên, và báo cáo việc đó cho công ty cậu. Sau đó,\ngiám đốc công ty cậu cũng rất hào hứng 'Nếu vậy thì nhất định phải làm'.」**. Đổi: '「Tôi' → '「Tao'.

**2234** — JP 「[おひとよ,2]御一夜鉄道への譲渡の準備だと答えた。\nすると、アレは――」; TW 「我於是回答這是為了將它移交給御一夜鐵路而做的準備。然後——」; old_vn (unif đã gộp) 「Tôi trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohitoyo.\nThế là, nó――」; **fix = 「Tao trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohitoyo.\nThế là, nó――」**. Đổi: '「Tôi' → '「Tao'.

**2268** — JP 「ので、まずは現状を確認しようと考え、\n一番最初に、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;技師のところに点検に出した」; TW 「於是，我認為應當先明確現狀，最開始我將它送去接受\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;技工的清查」; old_vn (CSV3) 「Vì thế, tôi nghĩ trước tiên phải xác nhận tình trạng hiện tại,\nnên việc đầu tiên là đưa nó đến chỗ kỹ sư \x%lレイルロオド;#00ffc040;Railord%l;#; để kiểm tra.」; **fix = 「Vì thế, tao nghĩ trước tiên phải xác nhận tình trạng hiện tại,\nnên việc đầu tiên là đưa nó đến chỗ kỹ sư \x%lレイルロオド;#00ffc040;Railord%l;#; để kiểm tra.」**. Đổi: 'tôi' → 'tao'.

**2271** — JP 「先方と当事者が乗り気なら、こちらは従うだけだ。\nだから、そのようにオリヴィに命令をした」; TW 「既然接收方和當事者都有相同的意向，我們也只需要尊重便是。所以我便照此向奧莉薇下達命令」; old_vn (CSV3) 「Nếu bên nhận và đương sự đều hào hứng, thì bên này chỉ việc làm theo thôi.\nVì vậy, tôi đã ra lệnh cho Olivy như thế.」; **fix = 「Nếu bên nhận và đương sự đều hào hứng, thì bên này chỉ việc làm theo thôi.\nVì vậy, tao đã ra lệnh cho Olivy như thế.」**. Đổi: 'tôi' → 'tao'.

**2316** — JP 「ああ。その話は聞いたし、業務命令も受けた。\n引き渡しにはこっちも、万全の準備をするつもりだった」; TW 「是，我聽說了你們的用意，也得到了上面的指示。原本我們也是打算做好萬全的準備，再移交給你們的」; old_vn (CSV3) 「À. Chuyện đó tôi có nghe, cũng nhận được lệnh rồi.\nBên này cũng định chuẩn bị kỹ lưỡng cho việc bàn giao.」; **fix = 「À. Chuyện đó tao có nghe, cũng nhận được lệnh rồi.\nBên này cũng định chuẩn bị kỹ lưỡng cho việc bàn giao.」**. Đổi: 'tôi' → 'tao'.

**2369** — JP 「いや、ちゃんと[おおみや,1]旺宮送りにした。\n検査は、まぁいつもどおりの結果だった」; TW 「沒有，是送到大宮那邊去做的。得到的結果與以往沒什麼不同」; old_vn (CSV3) 「Không, tôi đã gửi nó đến Omiya đàng hoàng.\nKết quả kiểm tra thì, chà, vẫn như mọi khi.」; **fix = 「Không, tao đã gửi nó đến Omiya đàng hoàng.\nKết quả kiểm tra thì, chà, vẫn như mọi khi.」**. Đổi: 'tôi' → 'tao'.

**2439** — JP 「一番長くⅨ号を使っていた自分が担当にあてられた。\nつまり、オリヴィに命令を遵守させるためのだ」; TW 「而此事交由駕駛九號時間最長的我來負責，也是為了使奧莉薇服從命令」; old_vn (CSV3) 「Người sử dụng Đầu máy số 9 lâu nhất là tôi được giao phụ trách.\nTức là, để bắt Olivy tuân thủ mệnh lệnh.」; **fix = 「Người sử dụng Đầu máy số 9 lâu nhất là tao được giao phụ trách.\nTức là, để bắt Olivy tuân thủ mệnh lệnh.」**. Đổi: 'tôi' → 'tao'.

**2500** — JP 「なら、ざっくばらんに行くが――」; TW 「那我就打開天窗說亮話了——」; old_vn (CSV3) 「Vậy thì, tôi cứ thẳng thắn mà nói nhé――」; **fix = 「Vậy thì, tao cứ thẳng thắn mà nói nhé――」**. Đổi: 'tôi' → 'tao'.

#### ハチロク12_ムナカタ来訪.txt.toml — 20 dòng

**1147** — JP 「……定年退職した後でも、私が蓄積した経験が、\n御社や鉄道の役に立つなら、嬉しいことです」; TW 「……即使在退休以後，若是我長年累積的知識經驗尚能為貴公司，以及鐵路事業發揮餘熱，自是何樂而不為」; old_vn (CSV3) 「...Sau khi nghỉ hưu, nếu những kinh nghiệm tôi tích lũy được, \ncó thể giúp ích cho quý công ty và ngành đường sắt, thì tôi rất sẵn lòng.」; **fix = 「...Sau khi nghỉ hưu, nếu những kinh nghiệm tao tích lũy được, \ncó thể giúp ích cho quý công ty và ngành đường sắt, thì tao rất sẵn lòng.」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**1159** — JP 「……\x%lレイルロオド;#00ffc040;レイルロオド%l;#;の車歴など気にもしなかったが――\nそうか。言われてみれば、百年以上の蓄積か」; TW 「……我倒是從未關注\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的車齡，不過如此說來，它確實積攢了百年以上的經驗」; old_vn (CSV3) 「...Tôi chưa bao giờ để tâm đến lịch sử hoạt động của \x%lレイルロオド;#00ffc040;Railord%l;#; nhưng—— \nRa là vậy. Nói mới nhớ, là sự tích lũy của hơn một trăm năm sao.」; **fix = 「...Tao chưa bao giờ để tâm đến lịch sử hoạt động của \x%lレイルロオド;#00ffc040;Railord%l;#; nhưng—— \nRa là vậy. Nói mới nhớ, là sự tích lũy của hơn một trăm năm sao.」**. Đổi: '「...Tôi' → '「...Tao'.

**1541** — JP 「いや、掘る方には手は出さないでくれ。\nさっきも言ったが、ガスの可能性もある」; TW 「不，挖土你就別來了。剛才我也說過，有可能是地下聚集了瓦斯」; old_vn (CSV3) 「Không, xin đừng nhúng tay vào việc đào bới. \nNhư tôi đã nói lúc nãy, cũng có khả năng là khí gas.」; **fix = 「Không, xin đừng nhúng tay vào việc đào bới. \nNhư tao đã nói lúc nãy, cũng có khả năng là khí gas.」**. Đổi: 'tôi' → 'tao'.

**1568** — JP 「いいも何も、雇われる身だ。\n雇い主の人事案に、意見が出せるはずもない」; TW 「何須徵得我的同意，我也會在將來受僱於此，怎可能對僱主的人事安排指手畫腳」; old_vn (CSV3) 「Được hay không cái gì, tôi là người làm thuê mà. \nLàm sao có thể có ý kiến với kế hoạch nhân sự của chủ lao động được.」; **fix = 「Được hay không cái gì, tao là người làm thuê mà. \nLàm sao có thể có ý kiến với kế hoạch nhân sự của chủ lao động được.」**. Đổi: 'tôi' → 'tao'.

**1642** — JP 「右田\x%l機関士;#00ffc040;機関士%l;#;。早速で悪いが、\n連絡をもらった支障個所に連れていってくれ」; TW 「右田\x%l機関士;#00ffc040;司機%l;#;，事不宜遲，還勞你帶我到出問題的地點一探究竟」; old_vn (CSV3) 「\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Ngại quá vì phải đi ngay, \nnhưng phiền cậu dẫn tôi đến chỗ xảy ra sự cố mà cậu đã liên lạc.」; **fix = 「\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Ngại quá vì phải đi ngay, \nnhưng phiền cậu dẫn tao đến chỗ xảy ra sự cố mà cậu đã liên lạc.」**. Đổi: 'tôi' → 'tao'.

**1661** — JP 「ああ――その――恐縮です。\nその、コーヒーの方を」; TW 「呃——這個，實屬惶恐，我喝咖啡」; old_vn (CSV3) 「A——à——ngại quá. \nVậy, cho tôi xin một tách cà phê.」; **fix = 「A——à——ngại quá. \nVậy, cho tao xin một tách cà phê.」**. Đổi: 'tôi' → 'tao'.

**1694** — JP 「ああ……その……こういう空気は慣れんですし、\n保線現場も早く確かめたいので――その、本題を」; TW 「啊……這個……我一來不太適應這種氛圍，二來希望能儘早動身查看巡線地點，不知能否儘快進入正題」; old_vn (CSV3) 「A... ừm... tôi không quen với bầu không khí thế này cho lắm, \nvới lại tôi cũng muốn nhanh chóng kiểm tra hiện trường \x%l保線;#00ffc040;bảo trì đường ray%l;#; nên——ừm, vào vấn đề chính đi.」; **fix = 「A... ừm... tao không quen với bầu không khí thế này cho lắm, \nvới lại tao cũng muốn nhanh chóng kiểm tra hiện trường \x%l保線;#00ffc040;bảo trì đường ray%l;#; nên——ừm, vào vấn đề chính đi.」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**1765** — JP 「[きりしま,1]霧縞なら温泉地、火山帯だ。\n今あげた可能性の、どれも十分にありえるな」; TW 「地處霧島，也就是火山帶，多有溫泉。那麼我剛才提到的幾個因素都是完全有可能的」; old_vn (CSV3) 「Nếu là Kirishima thì là vùng suối nước nóng, vành đai núi lửa. \nNhững khả năng tôi vừa nêu, khả năng nào cũng hoàn toàn có thể xảy ra.」; **fix = 「Nếu là Kirishima thì là vùng suối nước nóng, vành đai núi lửa. \nNhững khả năng tao vừa nêu, khả năng nào cũng hoàn toàn có thể xảy ra.」**. Đổi: 'tôi' → 'tao'.

**1840** — JP 「率直にいって、興味深く思っている。\n詳しく話を聞きたいと」; TW 「實話講來，我也頗感興趣，於是也想進一步了解其內容」; old_vn (CSV3) 「Thành thật mà nói, tôi thấy rất hứng thú. \nTôi muốn nghe chi tiết hơn.」; **fix = 「Thành thật mà nói, tao thấy rất hứng thú. \nTao muốn nghe chi tiết hơn.」**. Đổi: 'tôi' → 'tao'; '\\nTôi' → '\\nTao'.

**1864** — JP 「地盤が流れて動き、その影響が地表にでることだ。\nたしか、このあたりは――」; TW 「就是地基發生像流體一樣的運動，進而導致地表出現隆起，我記得這附近應該——」; old_vn (CSV3) 「Là hiện tượng nền đất trôi đi và dịch chuyển, ảnh hưởng của nó bộc lộ lên bề mặt. \nNếu tôi nhớ không lầm, khu vực này là——」; **fix = 「Là hiện tượng nền đất trôi đi và dịch chuyển, ảnh hưởng của nó bộc lộ lên bề mặt. \nNếu tao nhớ không lầm, khu vực này là——」**. Đổi: 'tôi' → 'tao'.

**1936** — JP 「そこは理解できた――かと思います」; TW 「我自認算是理解了你們的想法」; old_vn (CSV3) 「Điểm đó thì tôi đã hiểu——tôi nghĩ vậy.」; **fix = 「Điểm đó thì tao đã hiểu——tao nghĩ vậy.」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**1972** — JP 「リスクを理解してなら、止めん。\nオリヴィ、見てやれ」; TW 「既然你對危險心中有數，那我自不會阻攔。奧莉薇，你就去盯著他吧」; old_vn (CSV3) 「Nếu cậu đã hiểu rõ rủi ro thì tôi không cản. \nOlivy, giám sát cậu ấy nhé.」; **fix = 「Nếu cậu đã hiểu rõ rủi ro thì tao không cản. \nOlivy, giám sát cậu ấy nhé.」**. Đổi: 'tôi' → 'tao'.

**1988** — JP 「承知した。\nいや、余計なことで時間を取らせてすまなかった」; TW 「明白，這個，抱歉耽誤了時間」; old_vn (CSV3) 「Tôi hiểu rồi. \nKhông, xin lỗi vì đã làm mất thời gian của cậu bằng những chuyện bao đồng.」; **fix = 「Tao hiểu rồi. \nKhông, xin lỗi vì đã làm mất thời gian của cậu bằng những chuyện bao đồng.」**. Đổi: '「Tôi' → '「Tao'.

**1996** — JP 「そうか？ なら、鹿兒島まわりで一泊して」; TW 「是這樣嗎？那我就在鹿兒島附近投宿好了」; old_vn (CSV3) 「Vậy sao? Nếu thế thì tôi sẽ vòng qua Kagoshima trọ lại một đêm rồi」; **fix = 「Vậy sao? Nếu thế thì tao sẽ vòng qua Kagoshima trọ lại một đêm rồi」**. Đổi: 'tôi' → 'tao'.

**2010** — JP 「――み鉄には世話になりました。\n定年までは勤めきり、恩を返したいと思っています」; TW 「橙鐵對我有恩，我會一直堅守崗位直至退休」; old_vn (CSV3) 「——Tôi đã chịu nhiều ân huệ của Đường sắt Mikan. \nTôi muốn làm việc đến lúc nghỉ hưu để báo đáp ân tình đó.」; **fix = 「——Tao đã chịu nhiều ân huệ của Đường sắt Mikan. \nTao muốn làm việc đến lúc nghỉ hưu để báo đáp ân tình đó.」**. Đổi: 'Tôi' → 'Tao'; '\\nTôi' → '\\nTao'.

**2040** — JP 「いや、問題の地点を[せんけん,1]線見したくもあったし、\n話をもらった……別件というか、関連というか」; TW 「無需勞煩，我也想親自對有問題的地方踏查一番。另外你們找我商談的另一件事……或者該說與此事不無關係」; old_vn (CSV3) 「Không, tôi cũng muốn đi khảo sát trước địa điểm xảy ra vấn đề, \nvà cũng vì chuyện mà cậu đã nói... gọi là chuyện khác, hay chuyện liên quan nhỉ.」; **fix = 「Không, tao cũng muốn đi khảo sát trước địa điểm xảy ra vấn đề, \nvà cũng vì chuyện mà cậu đã nói... gọi là chuyện khác, hay chuyện liên quan nhỉ.」**. Đổi: 'tôi' → 'tao'.

**2103** — JP 「ポストや報酬については、今日の仕事振りを見てもらい、\n提示を貰うような形でどうでしょうか？」; TW 「至於職位和報酬，不妨請貴公司根據我今天的表現，再行判斷如何？」; old_vn (CSV3) 「Về vị trí và thù lao, xin hãy xem xét cách làm việc của tôi ngày hôm nay, \nrồi đưa ra đề xuất, như vậy được không?」; **fix = 「Về vị trí và thù lao, xin hãy xem xét cách làm việc của tao ngày hôm nay, \nrồi đưa ra đề xuất, như vậy được không?」**. Đổi: 'tôi' → 'tao'.

**2109** — JP 「それなら小一時間か――だが、お言葉に甘えていいなら、\nこのまま送ってもらった方が助かります」; TW 「若是如此，返程則需要將近一個小時，那我可否承蒙好意，請您現在安排將我送回呢」; old_vn (CSV3) 「Nếu vậy thì mất khoảng một tiếng nhỉ——Nhưng, nếu cậu không phiền, \nthì đưa tôi về ngay bây giờ luôn sẽ giúp tôi rất nhiều.」; **fix = 「Nếu vậy thì mất khoảng một tiếng nhỉ——Nhưng, nếu cậu không phiền, \nthì đưa tao về ngay bây giờ luôn sẽ giúp tao rất nhiều.」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**2219** — JP 「さて、それじゃ失礼します。\n明日も乗務があるもので」; TW 「那我就先行告退，明天還有乘務任務需要執行」; old_vn (CSV3) 「Thôi, tôi xin phép cáo từ. \nNgày mai tôi vẫn còn ca trực」; **fix = 「Thôi, tao xin phép cáo từ. \nNgày mai tao vẫn còn ca trực」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**2221** — JP 「それだけでも食っていけるだけの仕事量と報酬は、\nいただけますか？」; TW 「那我能否憑藉該職，獲得足以維持生活的工作量與報酬呢？」; old_vn (CSV3) 「Chỉ với công việc đó, liệu khối lượng công việc và thù lao \ncó đủ để tôi trang trải cuộc sống không?」; **fix = 「Chỉ với công việc đó, liệu khối lượng công việc và thù lao \ncó đủ để tao trang trải cuộc sống không?」**. Đổi: 'tôi' → 'tao'.

#### ハチロク15a_痛みとの決別.txt.toml — 5 dòng

**1750** — JP 「しかし――驚かされたぞ」; TW 「不過——這可真讓我驚訝」; old_vn (CSV3) 「Nhưng mà——Tôi thật sự bất ngờ đấy」; **fix = 「Nhưng mà——Tao thật sự bất ngờ đấy」**. Đổi: 'Tôi' → 'Tao'.

**1780** — JP 「見事な復旧だった。監督指導の必要などまるで無く、\n安全性に一点の曇りも見られなかった。だから、驚いた」; TW 「修復工程很完美。完全不需要我監督指導，也沒有發現安全方面的問題。所以我才驚訝」; old_vn (CSV3) 「Công tác khắc phục vô cùng xuất sắc. Hoàn toàn không cần tôi phải giám sát hay chỉ đạo,\nvề mặt an toàn cũng không có một chút tì vết nào. Vì thế, tôi mới bất ngờ」; **fix = 「Công tác khắc phục vô cùng xuất sắc. Hoàn toàn không cần tao phải giám sát hay chỉ đạo,\nvề mặt an toàn cũng không có một chút tì vết nào. Vì thế, tao mới bất ngờ」**. Đổi: 'tôi' → 'tao'; 'tôi' → 'tao'.

**2003** — JP 「お前の調査が、人的被害を防いだということも聞いた。\n井戸水の濁りの情報の早期共有が、自主避難を促したと」; TW 「我也聽說你的調查結果成功防止了人員傷亡。多虧你在早期就把井水變渾濁的訊息告訴大家，才讓居民主動去避難了」; old_vn (CSV3) 「Tôi cũng nghe nói cuộc khảo sát của cô đã ngăn chặn được thiệt hại về người.\nNhờ việc chia sẻ sớm thông tin nước giếng bị đục, đã thúc đẩy người dân chủ động sơ tán」; **fix = 「Tao cũng nghe nói cuộc khảo sát của cô đã ngăn chặn được thiệt hại về người.\nNhờ việc chia sẻ sớm thông tin nước giếng bị đục, đã thúc đẩy người dân chủ động sơ tán」**. Đổi: '「Tôi' → '「Tao'.

**2038** — JP 「お前がどれほど\x%l保線;#00ffc040;保線%l;#;を真剣に学んでいたか。\nそれを的確に御鉄の皆さんに伝えてくれたかに、驚いた」; TW 「我驚訝於你竟然這麼認真地學習了\x%l保線;#00ffc040;巡線%l;#;知識，還準確地教給了御鐵的人」; old_vn (unif đã gộp) 「Tôi bất ngờ vì cô đã học hỏi về \x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohitoyo nữa chứ」; **fix = 「Tao bất ngờ vì cô đã học hỏi về \x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohitoyo nữa chứ」**. Đổi: '「Tôi' → '「Tao'.

**2116** — JP 「ああ、そのとおりだ。御鉄さんから依頼を受けた。\n陥没の措置の監督と評価とをしてほしいと」; TW 「沒錯。我是御鐵請來的。他們希望我對塌陷應對措施進行監督和評估」; old_vn (unif đã gộp) 「Ừ, đúng thế. Tôi nhận được yêu cầu từ Đường sắt Ohitoyo.\nHọ muốn tôi giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」; **fix = 「Ừ, đúng thế. Tao nhận được yêu cầu từ Đường sắt Ohitoyo.\nHọ muốn tao giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」**. Đổi: 'Tôi' → 'Tao'; 'tôi' → 'tao'.

#### ハチロク15b_さよなら列車.txt.toml — 7 dòng

**1520** — JP 「まぁしかし、おかげでこいつと、\n八ツ城にまで走れるわけだ――っと」; TW 「不過，也多虧這樣，才能和它一起往八代那邊跑了」; old_vn (CSV3) 「Chà, nhưng nhờ vậy mà tôi,\nmới có thể chạy đến tận Yatsushiro cùng với cô đấy——」; **fix = 「Chà, nhưng nhờ vậy mà tao,\nmới có thể chạy đến tận Yatsushiro cùng với cô đấy——」**. Đổi: 'tôi,\\nmới' → 'tao,\\nmới'.

**1686** — JP 「構いませんが――」; TW 「我倒是不介意——」; old_vn (CSV3) 「Tôi thì không sao nhưng——」; **fix = 「Tao thì không sao nhưng——」**. Đổi: '「Tôi' → '「Tao'.

**1696** — JP 「もちろんもらう――（ごくっ、ごくっ）」; TW 「我當然也會喝——（喝水）」; old_vn (CSV3) 「Tất nhiên là tôi cũng uống rồi——(Ực, ực)」; **fix = 「Tất nhiên là tao cũng uống rồi——(Ực, ực)」**. Đổi: 'tôi' → 'tao'.

**1706** — JP 「すまん。右田君、代わってくれるか」; TW 「抱歉，右田，能代替我一會嗎」; old_vn (CSV3) 「Xin lỗi. Cậu Migita, thay tôi một chút được không」; **fix = 「Xin lỗi. Cậu Migita, thay tao một chút được không」**. Đổi: 'tôi' → 'tao'.

**1727** — JP 「なんだ――なんでも聞いてやるぞ」; TW 「是什麼——你儘管開口」; old_vn (CSV3) 「Chuyện gì——Cô nói gì tôi cũng nghe」; **fix = 「Chuyện gì——Cô nói gì tao cũng nghe」**. Đổi: 'tôi' → 'tao'.

**1734** — JP 「だな。しかし……夢にも思っていなかったな。\nお前の、引退セレモニーとは」; TW 「是啊。不過……我做夢都沒想到，你的引退典禮竟然來了這麼多人」; old_vn (CSV3) 「Ừ. Nhưng mà……Tôi nằm mơ cũng không nghĩ tới.\nLễ giải nghệ của cô, lại như thế này」; **fix = 「Ừ. Nhưng mà……Tao nằm mơ cũng không nghĩ tới.\nLễ giải nghệ của cô, lại như thế này」**. Đổi: 'mà……Tôi' → 'mà……Tao'.

**1787** — JP 「代わってくれ、非常事態だ」; TW 「緊急情況，快來替我」; old_vn (CSV3) 「Thay tôi đi, tình trạng khẩn cấp rồi」; **fix = 「Thay tao đi, tình trạng khẩn cấp rồi」**. Đổi: 'tôi' → 'tao'.

#### 凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml — 3 dòng

**1792** — JP 「長かったな。……いいレイルロオドだった。\n失くしてしまうまで、そうとは少しも思わなかったが」; TW 「很長啊……它是個很好的鐵路人偶。雖然在失去它之前，我完全沒有這樣想過」; old_vn (CSV3) 「Rất lâu. ……Là một Railord tốt.\nDù cho đến khi mất đi cô ấy, tôi chưa từng nghĩ như vậy.」; **fix = 「Rất lâu. ……Là một Railord tốt.\nDù cho đến khi mất đi cô ấy, tao chưa từng nghĩ như vậy.」**. Đổi: 'tôi' → 'tao'.

**1814** — JP 「うちのふたりは初段と二段。このクラスの大会では、\n引き分けを拾うのも難しいメンバーだというのに」; TW 「我帶來的兩個是初段和二段。這種規模的大賽，她們這種水平要和對手打個平手都困難啊」; old_vn (CSV3) 「Hai người bên tôi mới chỉ sơ đẳng và nhị đẳng. Ở giải đấu tầm cỡ này,\nđây là những thành viên khó lòng giành được cả một trận hòa.」; **fix = 「Hai người bên tao mới chỉ sơ đẳng và nhị đẳng. Ở giải đấu tầm cỡ này,\nđây là những thành viên khó lòng giành được cả một trận hòa.」**. Đổi: 'tôi' → 'tao'.

**1820** — JP 「わかるよ。ここまでのオーダーからも」; TW 「我明白，從至今為止的排兵布陣當中就能看出來」; old_vn (CSV3) 「Tôi hiểu mà. Nhìn vào thứ tự thi đấu từ đầu đến giờ là biết.」; **fix = 「Tao hiểu mà. Nhìn vào thứ tự thi đấu từ đầu đến giờ là biết.」**. Đổi: '「Tôi' → '「Tao'.

### 4.11. F-P4-1 — 9 dòng (2 file). F-P4-1 — tên tách “Anh, Soutetsu” → “Sou, tetsu”

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 4 dòng

**1364** — JP 「や、らぁ―そう、てつ―んっ！ は！ イク、の、\n一緒？ ね？ 一番、おく、で―一緒、いい、のぉ」; TW 「不、要——雙、鐵——嗯！ 哈！ 要、一起、高潮嗎？ 對吧？ 我要、在、最、裡面——一起」; old_vn (CSV3) 「Đừ, ng——anh, Soutetsu——ưm! Ha! Lên đỉnh,\ncùng nhau nhé? Nè? Ở nơi, sâu nhất——cùng nhau, được, không」; **fix = 「Đừ, ng——Sou, tetsu——ưm! Ha! Lên đỉnh,\ncùng nhau nhé? Nè? Ở nơi, sâu nhất——cùng nhau, được, không」**. Đổi: 'anh,' → 'Sou,'; 'Soutetsu' → 'tetsu'.

**1475** — JP 「ふぁっ！ あっ！ あっ！ あっ！ あっ！ あっ！\nあっ！ あっ！ そう、てつ―双鉄ぅ―んっ！」; TW 「呼啊！ 啊！ 啊！ 啊！ 啊！ 啊！啊！ 啊！ 雙、鐵——雙鐵——嗯！」; old_vn (unif đã gộp) 「Fa! A! A! A! A! A! A! A! Anh, Soutetsu——Soutetsu——ưm!」; **fix = 「Fa! A! A! A! A! A! A! A! Sou, tetsu——Soutetsu——ưm!」**. Đổi: 'Anh,' → 'Sou,'; 'Soutetsu' → 'tetsu'.

**1513** — JP 「はぁ―んっ―ふぁ―あ―。そう、てつ―\n双鉄―ふふっ―よく頑張ったね。双鉄、おいで？」; TW 「哈——嗯——呼啊——啊——雙、鐵——雙鐵——呼呼——你真的很努力。雙鐵，過來吧？」; old_vn (unif đã gộp) 「Ha——ưm——Fa——a——. Anh, Soutetsu—— Soutetsu——fufu——anh đã cố gắng lắm rồi. Lại đây nào, Soutetsu?」; **fix = 「Ha——ưm——Fa——a——. Sou, tetsu—— Soutetsu——Fufu——anh đã cố gắng lắm rồi. Lại đây nào, Soutetsu?」**. Đổi: 'Anh,' → 'Sou,'; 'Soutetsu' → 'tetsu'; 'fufu' → 'Fufu'.

**1534** — JP 「あ―らめっ！ これっ！ くるっ！ きちゃうっ！\nすごいのっ！ そう、てつっ―そうてつぅ！！！」; TW 「啊——不行了！ 我！ 要來了！ 要來了！好厲害！ 雙、鐵——雙鐵！！！」; old_vn (unif đã gộp) 「A——không được! Thế này! Đến mất! Đến mất thôi!\nTuyệt quá! Anh, Soutetsu——Soutetsu!!!」; **fix = 「A——không được! Thế này! Đến mất! Đến mất thôi!\nTuyệt quá! Sou, tetsu——Soutetsu!!!」**. Đổi: 'Anh,' → 'Sou,'; 'Soutetsu' → 'tetsu'.

#### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 5 dòng

**1025** — JP 「ダメ、だよ――双、鉄――んっ――あっ――\n今は――まだ、ダメ」; TW 「不行啦——雙鐵——嗯——啊——現在——還不行」; old_vn (CSV3) 「Không được, đâu——Anh Sou, tetsu——Ưm——A——\nBây giờ——vẫn chưa, được đâu.」; **fix = 「Không được, đâu——Sou, tetsu——Ưm——A——\nBây giờ——vẫn chưa, được đâu.」**. Đổi: −'Anh'.

**1074** — JP 「やっ――あっ――ふあっ――そう、てつぅっ」; TW 「呀——啊——呼——雙鐵」; old_vn (moan) 「Ya——A——Fua——Anh Sou, tetsu.」; **fix = 「Ya——A——Fua——Sou, tetsu.」**. Đổi: −'Anh'.

**1137** — JP 「んっ――はっ――あっ――\nそう、てつ――太っ――んっ――うぅっっ」; TW 「嗯——呼——啊——雙鐵——好粗——嗯——嗚」; old_vn (audit) 「Ưm——Ha——A——\nAnh Sou, tetsu——To quá——Ưm——Ư ư.」; **fix = 「Ưm——Ha——A——\nSou, tetsu——To quá——Ưm——Ư ư.」**. Đổi: '\\nAnh Sou,' → '\\nSou,'.

**1355** — JP 「まだっ――なのっ――そう、てっっ――ボクっ、もう\n――むり――むりっ――んっ――おねがい、そう、てつ」; TW 「還不行嗎——雙鐵——我已經——不行——不行了——嗯——求你了，雙鐵」; old_vn (CSV3) 「Vẫn chưa——được sao——Anh Sou, tetsu——Tôi, không\n——chịu nổi nữa——không chịu nổi nữa——ưm——Xin anh đấy, anh Sou, tetsu.」; **fix = 「Vẫn chưa——được sao——Sou, tetsu——Tôi, không\n——chịu nổi nữa——không chịu nổi nữa——ưm——Xin anh đấy, Sou, tetsu.」**. Đổi: −'Anh'; −'anh'.

**1361** — JP 「双鉄――そう、てつ――ね、ボク――ボク――もうっ、\nもう――ねっ――イキ――そうっ――んっ――ぁあっ」; TW 「雙鐵——雙鐵——我——我已經——嗯——要洩了——啊」; old_vn (unif đã gộp) 「Soutetsu——Anh Sou, tetsu——Này, tôi——tôi——sắp,\nsắp——này——lên đỉnh——rồi——ưm——aa.」; **fix = 「Soutetsu——Sou, tetsu——Này, tôi——tôi——sắp,\nsắp——này——lên đỉnh——rồi——ưm——Aa.」**. Đổi: −'Anh'; 'aa.」' → 'Aa.」'.

## 5. Các dòng GIỮ (không sửa, có lý do)

### F1 — 5 dòng ちゅず/ちゅく/ちゅりゅ GIỮ romaji (T75 không mở rộng)

- ハチロクh9 2031 (ちゅずううっ → “chuzuuu!”); lr_日々姫h2 1037 (ちゅりゅっ → “Churyu!”); lr_日々姫h2 1652 (（ちゅくっ！…) — cả dòng romaji); lr_稀咲ポーレットh1 2534 (（ちゅくうううっっ） → “Chu ku uu u”); 真闇h3 2357 (ちゅずっ → “Chuzu!”). Lý do §2 mục 2: phân biệt âm vị (ず xát / く vòm / りゅ lướt ≠ coda môi T75), trộn hệ nếu đổi lẻ, mở rộng toàn project ≈ 21 dòng vượt phạm vi.

### F3 — 真闇h3 2336 GIỮ “ru”/“ruu”

- JP 「ちゅる、るう、るっ」 là MỘT âm trượt kéo dài qua 3 mora (TW 啾嚕、嚕、嚕); “chụt” đã đổi cho ちゅる, hai mora đuôi “ruu”/“ru” giữ thường — đổi mora cuối thành “rộp” sẽ tách một âm thành hai cách diễn. (F5 vẫn viết hoa “zuro”→“Zuro” trong dòng này vì ずろっ là token độc lập.) Cùng quy tắc: 真闇h3 2292 “ru” (ちゅる、る) giữ thường — xem §7.

### F4 — lr_日々姫h2 1033 XÁC NHẬN “rộp” (0 dòng đổi)

- Chuỗi mở bằng れるっ (liếm) rồi じゅぶっ/じゅむっ (miệng); TW toàn âm miệng; ぶっ kế sau mơ hồ, TW không cho nghĩa thrust; audit/moan cũ đã là “liếm” cho るっ. Giữ “rộp” của U13b.

### M10 — mikuro 1708/1758 GIỮ “Fue!?”

- 1708: ふえっ mở đầu chuỗi rên (またっ──みくろっ！ またっ！ だって！ ぼっきっ！ — TW “又要洩了”), không phải ngạc nhiên độc lập. 1758: ふえっ là token CUỐI chuỗi rên (ひゅあっ！？ あ──あ……ふえっ！？), trong dòng rên H-scene. Quy tắc M10-1 (token trong chuỗi rên → “Fue”).

### O7 — 15 dòng “cô” GIỮ (danh từ / ngôi ba, không phải đại từ xưng hô Soutetsu→Olivy/Hachiroku)

- Olivy (6): ハチロク14_冬 2482 (“cô giáo Olivy” — danh từ, đại từ đã là “em”), 2789/2413/2466/1979/2444 (“cô ấy”/“cô ta” — ngôi ba).
- Hachiroku (9): 共通10 2682, 共通12 2104 (“cô ta”); lr_ハチロクh1 845, ハチロク01 2517 (“cô dâu”); lr_ハチロクh3 1421 (“cô mèo Xiêm”); ハチロク08 2402 (“quý cô”); ハチロクh9 2398, ポーレット08 2059 (“cô phục vụ”); 凪ふかみ03 2462 (“hai cô em gái”).

### Munakata — ハチロク04 2094 GIỮ “tôi”

- “tôi” trong dòng này là lời TRÍCH của Olivy (JP 『それなら、一日でも早く御一夜で仕事をしたい』と――, TW “它便提出…”), không phải tự xưng của Munakata. (2223 cũng chứa trích dẫn nhưng “Tôi” của nó là của chính Munakata — đã sửa.)

### F5 — các token romaji KHÔNG viết hoa (tóm tắt theo quy tắc, không liệt kê từng dòng)

- **Chữ cái đơn “a” — KHÔNG quyết** (745 lần xuất hiện, chủ yếu nửa tách M17 “Fu, a”, “Ha, na, o” — M17 giữ “a” thường có chủ ý; cần phân loại từng lần — xem cờ ở Kết bài).
- **Nửa của cách diễn TÁCH (M15):** “Ưm kyu”, “ưm fu”, “E mu”, “Chu mút”, “rê ryu”, “Zu ryuu…”, tên tách “Hibi, ki”/“Miku, ro”, “hi-hamu” (lr_凪h2 1290 — ひーはむ là một token JP), “ha ư” (lr_ニイロクh 1288 — はうっ), “ha hyu” (lr追加_みくろ 2201 — はひゅっ), “re hu” (ハチロクh9 2053 — れふっ), “Awa wa” (ハチロク08 2091 — あわわっ), “ju ru” (lr_稀咲ポーレットh1 2547 — ぢゅるっ), “chu ru” (稀咲h3 2265 — ちゅるっ), “re” (真闇h3 2290 — れ、るっ), “U hu hu” (ハチロク12 1746 — うふふぅ tách làm ba).
- **Mora đuôi của âm trượt (comma-slide):** “ruu”/“ru” (真闇h3 2336), “ru” (真闇h3 2292).
- **Chant âm tiết:** “ho he fu”, “Hyo ha hyo ho”, “hoo he hu” (ハチロクh9 2053), “ha fa” (ハチロクh8 724/751/754), “ha ha” (ハチロクh9 2134).
- **Từ lóng:** “Hôu-hê-hu” (ポーレットh4 914, ポーレットh6 850).
- **Từ VN / từ mượn / tên riêng:** “phu quân”, “chu đáo”, “rủi ro”, “êm ru”, “am hiểu”, “lu mờ”, “đúng ha” (ハチロク04 2182), “êm ru luôn ha” (仲国05 1926), “vậy ha!” (凪ふかみ05 3222), “gắt gao” (ハチロク14 3747), “San’yo”, “Tororyu-yu”, đuôi kéo dài tên “Sou-chaaan/chaan/chann” (真闇h3 2211/2306/2472).
- **Không có は trong JP:** “Anh ha” (lr_凪h1 1195 — JP にーさっ).
- **M15 “Kh” / “nn” / “mm”:** không đụng (ngoài phạm vi F5).

## 6. Khối TOML theo file (áp vào TOML — escape mọi backslash)

Mỗi file một khối ```toml, header `[script]` (trừ 2345 là `[characters]`), key số trần, giá trị double-quoted với mọi backslash đã escape (`\n` trong JSON → `\\n` trong khối; `\x` trong gloss %l → `\\x`). Kiểm chứng §7: trích khối, parse lại bằng tomllib, mọi giá trị phải bằng fix trong JSON.

#### lr_ふかみh1_ふかみうさぎのたまご.txt.toml — 4 dòng

```toml
[script]
1196 = "「Nhưng——a——cứ thế này, thì——Ha——」"
1432 = "「Fu——kami——nới lỏng ra, cho anh——Aa!!」"
1460 = "「Ha…… a——Fau…… ưm——Ehehe——\\nanh Soutetsu——của em, anh Soutetsu của em.」"
1655 = "Nói đúng hơn là, Fukami càng khít hơn.\\nKhao khát tinh dịch hơn nữa, em ấy siết chặt lấy tôi, Kyun Kyun."
```

#### lr_ふかみh2_セックスの意味.txt.toml — 4 dòng

```toml
[script]
1029 = "「Nhyu!!? Khoan——khoan đã——Au——\\nkhông được——bây giờ, âm vật thì——kích thích quá——a!」"
1060 = "「Hau——Ah——Ah——Ah——âm đạo——đây là,\\ncủa em——của em——âm đạo——âm đạo——」"
1063 = "「Anh——Hya——Hau——Soutetsu, anh——\\nA——phù——a——a——ưm~~~ƯƯƯ!!!」"
1270 = "「Fua! A! A! A! A!!\\nHí! A! Chỗ đó! Ưm——a——Fuu.」"
```

#### lr_れいなh1_レディ・れいな.txt.toml — 4 dòng

```toml
[script]
1202 = "「Fa——Ha——Ha——Ha——\\nFaa——Haa——Haa——Haa——」"
1251 = "「A mút——rộp——chụt——chụt——chụt\\n——chụt. Ưm…… hôm nay có hơi mặn một chút nha~」"
1266 = "「Chu mút! Chụt mút! Chụt! Chu mút t!\\nRộp——liếm m! Sụt! Chụt! Chu mút」"
1271 = "「Chụt! Chụt! Chụt! Chu mút t~!\\nChu mút! Chụt! Liếm m, chụt! Chụt!」"
```

#### lr_ニイロクh_誓い。約束.txt.toml — 11 dòng

```toml
[script]
1272 = "「Fua──a──a ư ư ư──Aaa──」"
1275 = "「Hàà, hàà, hàà, hàà──ưm, Ku──\\na──chỗ cứng──cứ cọ vào, chỗ cứng đó」"
1278 = "「Hà Aaan! Fua! A! Sâu, bên trong!\\nFua! A! A! Aaaa!!!!!」"
1288 = "「Fua!? A──Aa──ha ư──ưm.\\nTrực tiếp──cọ, cọ──tuyệt quá, hơn cả lúc nãy.」"
1322 = "「! Vậy, cái này, ái ân vuốt ve──ưm──cọ. Cọ,\\nthế này──là đang làm cho tôi, sướng──Fua.」"
1337 = "「Ưm.................. Pua──e he he──\\nKiyoharu──Kiyoharuu」"
1353 = "「Ưm!? Ưm... chụt——chụt——Pua,\\nưm——chụt——chụt——liếm——rột」"
1356 = "「Nkyu! Ưm! Fu, Yu──Myu──\\nưmmmmmm──!!」"
1387 = "「Tuyệt, quá! Tất cả──Fua! A!\\nBên trong, nè! Bé gái, âm đạo──bên trong âm đạo!」"
1395 = "「Niêm... phong──Fa... ưm, Ku──hà──\\ncái đó──là gì──ưm」"
1438 = "「Vui, tôi vui lắm──ưm──a──\\nFua!? Fuaaan ư ư!!」"
```

#### lr_ハチロクh1_今ひとたびの契り.txt.toml — 9 dòng

```toml
[script]
1153 = "「Fu——a——.\\nƯm…… Fa…… u——ưm………… a!」"
1158 = "「Fuya!!? Ng-ngón tay——\\nNgón tay của ngài Soutetsu——ưm——Fa.」"
1163 = "「Fue!? Nhịn——nhịn——ưm, Fu,\\nHaa——Ha——fu, an! Kh-không nhịn được nữa đâu.」"
1178 = "「Fa——a——n——Kyufu——a——Fu——\\nSou, tetsu, sama——Sou, tetsu, sama~」"
1213 = "「Ưm…… chụt——Chuzu——Ju——(ực)\\n——chụt——rộp——Rero——Churyu」"
1237 = "「A…… Ya——Fu, a——\\nXấu hổ——em xấu hổ lắm ạ.」"
1241 = "「Amu——Fu——ưm——Reu——Ryu——\\nChụt——chụụt——Juryu——」"
1252 = "「Ưm…… chụt——ưm…… Fu…… a……\\nFu——chụt——chụụt——rộp」"
2008 = "（Chụt——Puryu）"
```

#### lr_ハチロクh3_通販失敗いたしましたにゃん.txt.toml — 1 dòng

```toml
[script]
1232 = "「Ha——Hahyu——ưm……Fua—— a——a——a——a——Fa」"
```

#### lr_ポーレットh1_家族旅行の最終日の夜.txt.toml — 4 dòng

```toml
[script]
1026 = "「Ha——ưm——phù, phù——ưm! A,\\nEo, tiếp tục đi——Ku, Phu——anh Soutetsu——a!」"
1062 = "「A……chụt——chụt——ưm——Fa. Ưm……Ehehe——em cũng yêu anh. Anh Soutetsu」"
1096 = "「Ưm kyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi」"
1113 = "「Pua! A——Ha——a——tuyệt quá—— âm đạo——tử cung——nhiều quá——đặc quá」"
```

#### lr_ポーレットh2_デコレーション＆ミルク.txt.toml — 3 dòng

```toml
[script]
1022 = "「Fua——Ha——a——a——chậm rãi, thế này——\\nem cũng thích——ưm——chỗ, sướng ấy——cứ từ từ——a」"
1041 = "「Ha! A! A——a——Aa!!\\nAnh, Soutetsu——Ku——a! Em——sắp」"
1084 = "「Ha——Au——Fan——ưm——Kuuun——\\nƯm. Thế này——chậm rãi——Ha——chậm rãi, thế mà」"
```

#### lr_凪h1_痛いの痛いの飛んでけばい.txt.toml — 13 dòng

```toml
[script]
1128 = "「Hyau! A——Fua! A! Cô bé!\\nTử cung——nóng quá——ngực cũng——Fu, a」"
1162 = "「Ưm ku!? Pu――Fa――ưm――Juru!\\nJubo! Jubu! Juba! Chụụụt」"
1163 = "「Kua——Haa——Haa——Haa——Haa」"
1185 = "「A……ưm……Fa――á――anh hai……\\nMạnh hơn――mạnh hơn, nữa――ưm――mạnh lên, đi」"
1190 = "「A……Sắp, được rồi——ưm——Ku——Fua!\\nMột, chút nữa thôi——là vào đến, tận cùng——bên trong, rồi」"
1213 = "「Ư!!!! （Hapu!!!!）――rộp!\\nJuuuuu! Zuchu! Jubu!!!!」"
1214 = "「Hả? Wa――Wawawawawawa!?」"
1216 = "「Picha――Pero――Pero――Pero――\\nReryu――Pecho――Pero――Pero――」"
1220 = "「Juru! Rộộộộp! Rero! Chụt!\\nƯm! Jubu! Jubo! Ju! Jubu!」"
1221 = "「Juuuuuu! Zubo――Go!!!!\\nJuruuuuu! Zubyo!――Gyu!!」"
1233 = "「Ưm……hà――vú――từ từ――ưm――\\ntừ, xung quanh――bị, xoa nắn――Fua!」"
1236 = "「Ưm――Pua! A……anh hai, ưm……bị, làm,\\nnhư vậy――Fua――Nagi, sama――tập, trung」"
1298 = "「Do em mải mê tu hành nên không nhận ra sự hiện diện của anh hai\\nLà do em còn non kém――Aa――（Phùu, phùu）」"
```

#### lr_凪h2_虎さんの交尾.txt.toml — 16 dòng

```toml
[script]
1174 = "「Hya——ưm——sao lại, là nách, chứ? Nagi\\n——Fa——chỗ đó——nhột lắm——」"
1190 = "「Hyau!? Fa——a——sướng, lắm, nhưng mà,\\nưm——bây giờ em muốn anh nhìn——xuống dưới cơ——Gao」"
1199 = "「Fua——a! A! A! A——\\nƯm——Fuya——sướng, quá——ưm——phù」"
1229 = "「Fa——Hyau——a……ưm……Nhehe——\\nNagi——Nagi——ưm——vui lắm……Fa」"
1235 = "「A——Fa——a——」"
1236 = "「Fa——Fa——A——a——\\nAnh Soutetsu——nè——anh Soutetsu——anh Soutetsuuuuu」"
1241 = "「A——a——anh Soutetsu……dâm đãng, quá……Fa……\\nSay mê, ngực nhỏ, của Nagi——đến vậy sao」"
1245 = "「Ka——Ha——a——đúng rồi, đó——Gao.\\nRồi sau đó, ban đầu, hãy từ từ, chuyển động, hông——」"
1247 = "「Ha——a——cái đó——nữa đi——anh Soutetsu,\\nlúc nãy ấy——nữa đi——Fua! Nữa đi——Ư!」"
1254 = "「Fa——đúng rồi, dùng cậu nhỏ——làm cô bé, mạnh hơn nữa\\n——phập phập——đi——ưm——Ha, a」"
1258 = "「Fa……（Ực）——A! Fu, Fufufu-n!!\\nAnh Soutetsu, hưng phấn với Nagi——đến phát tình rồi sao?」"
1280 = "「Fue——Fua!!?」"
1285 = "「Chụt——chụt——rộp——liếm——\\nJu——Zujuuu——（Ực）——Pua」"
1290 = "「Ưm……hi-hamu……ưm——Hyuki——chụt——\\nrộp——chụt——rộộộộp——chụt」"
1304 = "「Ưm, Hyu! Fa——khi bị, liếm như vậy,\\nbị liếm, như vậy——em, Fua——cô bé, nóng, quá」"
1325 = "「Anh——Soutetsu——ưm——Yaa——ưm——Ha——\\nđừng——trêu em, nữa——ưm——làm mạnh, hơn đi」"
```

#### lr_凪ふかみh1_じぇいけい！.txt.toml — 17 dòng

```toml
[script]
1485 = "「D, á!? Fukami——ưm——đừng,\\nnhìn chằm chằm thế——em đang——bị đâm phập phập——Auu!?」"
1505 = "「Fu……a——（Khịt, khịt）——Tuyệt, quá……\\nTinh dịch……mùi, nồng hơn, mọi khi……Fa——」"
1507 = "「Haa! Haa! Haa! Efu! Ha——\\nHaa! ——Haa……Fuu……Haa……Haa……Haa」"
1509 = "「Fua——a——tuyệt quá——tuyệt quá——Fua!\\nTử cung——bị đập vào——bắn phụt phụt——tinh dịch」"
1581 = "「A——Fukami——Haa——Fa——ưm」"
1595 = "「A! Fua! Cái đó! Cả cái đó nữa!!\\nHãy cho em cả đợt mới đi! Cho em——Hyan!?」"
1614 = "「Haa, Haa, Haa, Haa」"
1616 = "「A, Ufufu. Ra là vậy nhỉ. Tớ hiểu rồi.\\nƯm nè? Nagi, chắc là——————thế này!?」"
1643 = "「Liếm——mút——liếm——rộp——\\nmút——mútttttt——（Ực）——Pua」"
1646 = "「Chụt——chụt——rộp——liếm——ưm——\\nJu——Zu——zujuuuuu——（Ực）——Pua」"
1657 = "「Khoan!? Nagi! Fua! Không được!\\nThế này! Tớ! Tớ——sẽ sướng quá mất——Hyau!」"
1658 = "「U……a……khắp mặt, nhớp nháp quá đi——ưm……\\nChụt——（Ực）——Fa——đặc dính luôn~」"
1660 = "「Ưm……liếm——liếm——liếm——\\nFu——ưm——liếm——rộộộp——liếm」"
1677 = "「Ưm!? Pua! A!? A——Haa!?\\nSao lại, đột ngột——thế——Aaaaaaaan!」"
1687 = "「Ufufu, cậu nói giỏi lắm.」"
1714 = "「Nóng quá——nóng quá đi——Fua——thích lắm——\\nyêu, yêu——yêu anh Soutetsu, yêu Nagi」"
1737 = "「Nagi, cậu muốn sao nào? Phải dùng miệng,\\nnũng nịu anh Soutetsu đàng hoàng chứ.」"
```

#### lr_日々姫h2_デザートは食事の前に.txt.toml — 14 dòng

```toml
[script]
991 = "「Amu——chụt——Hamu——chụt——Mu——\\nKapu——rộp——Amu——Juru——Hamu!」"
998 = "「Dyubo! Ju!! Jyururu! Chụt, ba!\\nƯm——Jyubo! Chụụt! Juru! Jubu」"
1016 = "「Chụt——rộộp——chụt——chụt, chụt,\\nReryuuu——Rero——Chuuuuuuuu!!」"
1033 = "「Rộp——nhóp nhép——mút——rộp——phập——\\n『Hyababa, Bafi』, Pua——Pu——nhóp nhép.」"
1036 = "「A~~——ưm~——rộp——nhóp nhép——ưm……\\nReryuuuu——rộp——liếm nhẹ——Rechun」"
1038 = "「Hamu——rộp——Amu——chụụt——Hamu,\\nChụt——Famu——chụụt——ưm——Ư!!!」"
1039 = "「Liếm——rộp——Nchu——rộp——liếm nhẹ,\\nReryu——chụt——chụt——chụụụụụt!」"
1041 = "「Chụt——Momu! Hamu——Amu——\\nƯm…… Hamu——Kapu——Mopu——Amu——」"
1042 = "「Ưm…… Ha——ưm——chụt——Rero——chụt,\\nReryuuu——Rero——mút——rộộộp」"
1045 = "「Chụụụụụụụt! Ưm…… ực——Fu, a\\n——rộp——Rerooo——chụt——chụụụt」"
1046 = "「Rộp——liếm nhẹ——chụt——Chuuu——\\nƯm…… liếm nhẹ——Reryu——liếm nhẹ——Juzuu!」"
1053 = "「Churooooo——rộp——chụt, chụt——\\nChụt——rộp——Chuzu——Zu, Zuuuu」"
1056 = "「Gupo! Gupa! Chụt! Juzu! Zu!\\nJurururu! Jyubo! Rộp! Buchuu!」"
1173 = "「Fa! A——anh hai——ưm——Fua,\\nA——lưỡi——ấm quá——thích lắm.」"
```

#### lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml — 8 dòng

```toml
[script]
1334 = "「Ya!? Mãnh liệt――quá――Fua! A!」"
1356 = "「Fa――a――Nkyu! Ư! Anh hai!\\nĐợi! Đã――em――em, em――sắp!」"
1406 = "「Ư!!? ――A, Aa」"
1440 = "「A…… Ufufu!\\nAnh Soutetsu, nó to lên rồi kìa.」"
1461 = "「Chùn chụt――rê ryu――Reroooo――Zuryu――\\nChùn chụt――chụt――Zuryuuu――（Ực）」"
1475 = "「Ưm――chụt――chùn chụt――chụt――rộp――\\nrê ryuuu――chùn chụt――Chu――Zuryu――Ru」"
1477 = "「Ưm――rộp――rê rô――chùn chụt――chụt――\\nƯm…… chụt――chùn chụt――（Ực）――Pu, a」"
1479 = "「Ưm…… a――a――hư――a――ưm――\\nChụt――chùn chụt――ưm…… hư――Fa――a」"
```

#### lr_日々姫真闇h1_三人家族.txt.toml — 5 dòng

```toml
[script]
1471 = "「Fuya!? Ya! Fu――a――Aa!!\\nChị hai――em――thế này――Fu, a――giỏi, quá.」"
1522 = "「Muchu――chụụt――Pero――Reryu――chụt\\n――rộộộp――Nuro――Juuu――Mu, chụt」"
1573 = "「Chụt――ưm――rộp――rê ryu――Churyu,\\nChu――Muchuu――Reryuu――Chu, Chuzu」"
1585 = "「Ưm…… chụt――Reryu――chụt――Juyuu\\n――rộộp――Rero――chụt――Chuzu, Zu」"
1634 = "「Ngực của――chị hai――mềm quá――ưm――tuyệt quá\\n――a――ngón tay――lún vào――rồi bám chặt, lấy――Fa.」"
```

#### lr_真闇h1_僕のおねえちゃん.txt.toml — 7 dòng

```toml
[script]
1429 = "「Fa! A——a——a……Aa……」"
1477 = "「Chụt——chụt——chụt——rộp——\\nrột, rột——chụt——chụt——Phuha」"
1507 = "「Ưm——rộp——Nchu——liếm!」"
1598 = "「Tôi hiểu rồi! Tôi hiểu rồi! Ư——Hôm nay——\\ntôi, Ha——sẽ——giao phó! Tất cả——cho chị!」"
1655 = "「Rộộộộp——chụt——Ku, Ryu——trơn tuột!\\nChụt——liếm——xoay, Ku——trơn tuột!!」"
1816 = "Lưỡi lại liếm vào lúc này——Ku!!!!!!!"
2029 = "Khi tôi ấn vào núm vú đã cương cứng từ khoảnh khắc bước vào phòng,\\nchị Mayami phát ra tiếng kêu như một con mèo cái đang động dục——Aa."
```

#### lr_稀咲h1_おしおきとごほうび.txt.toml — 9 dòng

```toml
[script]
1023 = "「Aaaan……(Hapu)――chụt――chụụụt,\\nchụt――Zu――――――(Koku)――Pua.」"
1041 = "「Reryu――Pero――chụt――chụt――\\n(Pua), ưm――chụụt――Zuchuu――rộp.」"
1053 = "「Chụt――chụt――chụt――chụụụt.\\nPhù――há――chụt――chụt――Juru.」"
1054 = "「Rộp――Reryu――ưm――Juzu――(Koku)\\nPua――thích――thích lắm, thích――ưm――chụt――chụụt.」"
1055 = "「Reryuuuu――Reryu――Nuryu――(Koku)\\nchụt――chụt――chụụụt――chụụụụt.」"
1058 = "「Jumu! Jubo! Bo! Juuuuuu!\\nZubyu――chụt――rộp――Zubo! Bochu!」"
1068 = "「Ưm……chụt――chụt――chụt……Re――Ryu,\\nReryu――chụụt――chụt――Reryuuu.」"
1069 = "「Ưm……phù――chụt――chụt――\\nchụt――Ju――Jupu――Juba――」"
1688 = "（Sunyu――Kuchu――Chuku――chụt）"
```

#### lr_稀咲ポーレットh1_悪い大人の契約.txt.toml — 13 dòng

```toml
[script]
1364 = "「Đừ, ng——Sou, tetsu——ưm! Ha! Lên đỉnh,\\ncùng nhau nhé? Nè? Ở nơi, sâu nhất——cùng nhau, được, không」"
1475 = "「Fa! A! A! A! A! A! A! A! Sou, tetsu——Soutetsu——ưm!」"
1495 = "「Hya!? A, phần bụng, ngón tay, của anh Soutetsu——Fa, đang ở, cửa mình——âm đạo, của em——Au——」"
1513 = "「Ha——ưm——Fa——a——. Sou, tetsu—— Soutetsu——Fufu——anh đã cố gắng lắm rồi. Lại đây nào, Soutetsu?」"
1534 = "「A——không được! Thế này! Đến mất! Đến mất thôi!\\nTuyệt quá! Sou, tetsu——Soutetsu!!!」"
1542 = "「A——ưm fu, Fu——cảm ơn anh, Soutetsu. Vì đã\\nđàng hoàng——đàng hoàng——làm tình, với em nữa.」"
1585 = "「Chụt——rộp——chụụt——chụt——\\nchụt——chụụt! Chụt! Chụụụt!」"
1589 = "「Chụt! Chụt! Chụt! ——Ha mu, ku pu,\\nchụt——rê ro——rê ryu u——chụt」"
1593 = "「Uu——Ku——a——Ha——」"
1601 = "「Ưm——Ha! A! Soutetsu, Soutetsu——em thì——\\nlần sau——hôm nay, em là người thứ hai, cũng được——hãy làm với Paulette đi.」"
1604 = "「Ưm……Fufu——sao nào, Soutetsu? Cảm giác của âm đạo——\\nưm——của em, và của Paulette, có khác nhau nhiều không?」"
1673 = "「Em……cũng, vậy——Soutetsu……ưm——Ha——a——\\nHôm nay——sao, nhỉ——cảm giác, hơn hẳn, mọi khi——」"
1821 = "「Rộp——rê ro——rê ryu——ryu——\\nchụụt——chụt——pê ro——pê chu——」"
```

#### lrれいな追加h_夜の花嫁修業.txt.toml — 2 dòng

```toml
[script]
1087 = "「Hia——Ha! Ha! Fua! Ưm!\\nKyu! Fua! Ha! Ha! Ha! Ha! Ha!」"
1123 = "「A——Ku, Ha——em mà, nói, chuyện, thì」"
```

#### lr真闇追加h_赤ちゃん、欲しか.txt.toml — 5 dòng

```toml
[script]
1013 = "\"「Không được——dừng, lại——ra mất——Yaa!\\nChị——Sou-chan——cùng với Sou-chan cơ!」\""
1097 = "\"「Fua——ưm——Nku——Ku——Ha.」\""
1127 = "\"「Ha! Ngyu! Ku——Ha——bị đóng cọc, rồi,\\nchị——được khắc dấu ấn——của Sou-chan——rồi.」\""
1152 = "\"「Ưm……Pua——chụt——chụụụt——chụt——\\nChùn chụt——chụt——chụt——chụt.」\""
1292 = "\"「Chị Mayami cũng, vậy——Ku——Ha——\\nƯớt sũng, nhầy, nhụa, rồi——」\""
```

#### lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml — 6 dòng

```toml
[script]
1025 = "「Không được, đâu——Sou, tetsu——Ưm——A——\\nBây giờ——vẫn chưa, được đâu.」"
1074 = "「Ya——A——Fua——Sou, tetsu.」"
1137 = "「Ưm——Ha——A——\\nSou, tetsu——To quá——Ưm——Ư ư.」"
1144 = "「Ư……m. Fu, Fu——cảm ơn anh, Soutetsu.」"
1355 = "「Vẫn chưa——được sao——Sou, tetsu——Tôi, không\\n——chịu nổi nữa——không chịu nổi nữa——ưm——Xin anh đấy, Sou, tetsu.」"
1361 = "「Soutetsu——Sou, tetsu——Này, tôi——tôi——sắp,\\nsắp——này——lên đỉnh——rồi——ưm——Aa.」"
```

#### lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml — 19 dòng

```toml
[script]
1368 = "「Hyagu! Ưm——Ah! Nhịn! Cố nhịn!\\nFua!? Không được——cái này, không được——đến giới hạn rồi」"
1433 = "「Nkyu!!? Phù——Ah——Momiji!!\\nĐang chuyển động——kìa——Ah——Fuuuuun!!!」"
1519 = "「Haa——Haa——Nku——Ưm——(ực)\\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」"
1556 = "「Phù——ưm——Ha——a……Fua——(ực),\\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」"
1710 = "「Ưm……Ku——Haa——Haa——(ực)——\\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」"
1773 = "「Ha, Ah——ưm——Phùù——\\nƯm——Phù——Aah」"
1804 = "「Ưm——Ku——ưm——Aah——Ah」"
1887 = "「Ka……Ha——Ah! Ta bảo đợi đã, mà……Ưm!\\nĐâu cần——đến, mức đó——như đàn ông, vậy——Higi!?」"
2098 = "「Haa——Haa——Haa——Haa——Ưm——\\nTa——Bộ dạng——đáng xấu hổ, này——Hi, Gu」"
2146 = "「Haa——ư——phù——Fua——sướng, quá!\\nƯm——ở sâu, bên trong——Gochu, Gochu——chạm, vào rồi」"
2168 = "「Ưm——Ha——Haa——cái này——Ha——quả nhiên,\\nKu——to, quá——mất, rồi——」"
2220 = "「Haa——ưm——cảm nhận được——hơn, mọi khi——Ku\\nTình trạng——bất thường——thế này——ưm……Ha, Ah」"
2279 = "「A……phù——ưm——Fua, Ah」"
2334 = "「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\\nAh——cứ nghĩ, là vậy, nhưng——Ku——Fua」"
2346 = "「Fa——Ah——Ah——Ah」"
2352 = "「Hafu——ưm——Kyu! Fua! Aah!\\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」"
2435 = "「Hia!? Ah, Ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ưm!」"
2449 = "「Ka……Ha——!!!!?」"
2457 = "「Fa——Ah——sướng——sướng quá! Phù——Ah,\\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」"
```

#### lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml — 11 dòng

```toml
[script]
1604 = "「Không phải── ưmm── Phu── a── anh hai──\\nAnh hai, so với── mọi khi──」"
1678 = "「Hyau── ưm── Fua── a──\\nA── a── a── Aa──」"
1739 = "「Fua! A!! A── Aaaa!!!!」"
1741 = "「Fuya── gì thế, này── nóng quá──\\nBụng── vùng kín── nhão nhoét── Phu── aƯ」"
1773 = "「Hà── a── Phu── Fua──」"
1811 = "「A……ưm──chụt──chụt──chụt──Fu\\n……ưm……liếm──liếm──liếmmm──Pua」"
1855 = "「Ưm Hyuuuuuuuuu!」"
1857 = "「Ưm kyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất」"
1901 = "「Pua──Fufu, anh ấy bảo thế kìa. Mikuro.」"
2200 = "「Hàà── Phuu── hààà── phuuuƯ」"
2201 = "「Hàà── ưm, Phu── ha Hyu── kufuƯ」"
```

#### ふかみh1_ともはり練習.txt.toml — 5 dòng

```toml
[script]
987 = "「Fa——Ah——của em——âm đạo——\\nMiệng của——anh Soutetsu——bằng miệng——」"
992 = "「Fu, Ah——lưỡi……ấm……quá……ưm.」"
1039 = "「Thích……thích……Anh Soutetsu, đối với em——\\nĐã thích em rồi, sao……Fu, Ah.」"
1048 = "「Ưm……Ha——Fuaa……Pua」"
1049 = "「Ưm……Ah——bên trong……bị đẩy——vào——\\nFua——hi——như bị, lộn ngược……vậy——」"
```

#### ふかみh2_homesweethome.txt.toml — 9 dòng

```toml
[script]
973 = "「Hya!? Ya——anh Soutetsu!?\\nQuần lót, quần lót của em——lún……vào——Fua」"
975 = "「Hia——Ah——ưm——ưm——phù ư——」"
983 = "「Paa!? L, lại ấn mạnh nữa——ưm! A——\\nBằng quần lót……mà cũng cảm thấy sướng, sao——Ah——Yaa」"
988 = "「Ư——ư——~~~ư!? Ưm——phù——\\nphù——phù——ưm! Ưm——phù——Hihyu」"
1011 = "「A…… Aa…… Aa~—— Aaa~~!」"
1013 = "「A——Ha——ưm——ưm——ưm!!」"
1025 = "「Fa——ưm——chụt——chụt rột——Gu——\\nAh——ho he fu, Fa——ho he fu, Fan!!」"
1032 = "「Ưm……ưm, chụt——chụt——ưm——————\\nỰc……ưm~~~——Puha」"
1034 = "「Ưm……Fu, Ah——ưm——Fahi……ưm ư——ưm,\\nHo he fu……Fan……ư ku——ưm!」"
```

#### れいなh1_おかあさんのレッスン.txt.toml — 1 dòng

```toml
[script]
1527 = "「Hia——ưm——Hya——a——\\nAnh——Soutetsu——anh——Soutetsu~」"
```

#### れいなh2_おもらし防止大作戦.txt.toml — 3 dòng

```toml
[script]
1064 = "「Kyufuu! Ưm——Fuuuuu——ưm!\\nChỗ đó——nham nhám——Ha——sướng——quá」"
1183 = "「Fue——Fua——Ha——Hauu——」"
1185 = "「Fa——Haa——a——Faa——」"
```

#### れいなh3_おもらし自由化大作戦.txt.toml — 8 dòng

```toml
[script]
1061 = "「Nbu——Mu——ưm——ưmm——Mu——\\nGu——Guu——ưm u——」"
1085 = "「Zu——Zuuuuuuuu——Zuju!\\n——Jururururu~~————n~——Goku」"
1089 = "「Rộp——liếm——chụt——chụt——\\nƯm……Ammmmm——」"
1091 = "「Ưm——Nfu——rộp——rộp——\\nChụt——chụt——chụt——chụtttttt」"
1092 = "「Nbu——Muuu——ưm——phù——ưm——\\n（Suhi）——（Suhi）——Nfufuuuu~」"
1099 = "「Nmu——Mu——uuuu~~~~Ư!」"
1195 = "「Fua——Achu——ưm! Hya——\\nA——Aa——a——」"
1196 = "「Fa——a——ưm——ưm——Nmu——\\nNku——Goku——Goku——————Gokun」"
```

#### れいなh4_ふたりっきりのハロウィン.txt.toml — 7 dòng

```toml
[script]
2000 = "「Fuyu——ưm——Fua——a——Hyu,\\nưm——a——anh Soutetsu——anh Soutetsu」"
2015 = "「Kyufu——ưm! ~~~! Fu——Ku——\\nưm——không được——vẫn, chưa——chỗ đó, chưa được」"
2047 = "「Ưm……chụt——chụụt——Chumu——ưm……\\nyêu……ưm——chụt——Soutetsu……Haan」"
2088 = "「Ehe, He~——Reina——được, khen——Fu\\n——Fua——a——vui, lắm——ạ~——ưm」"
2457 = "「Fua……a……a……Ya——ưm——\\nchỗ đó——tinh dịch——đang tràn——ra ngoài」"
2458 = "「Fuaaaaaa——Reina, vào miệng——\\nanh Soutetsu——Nkyu!? Fuaa——an!!」"
2459 = "「Fua! A! Sướng, quá——sướng, quá.\\nƯm——a——Ha——a——Fua——aƯ」"
```

#### グランドリライト01_オール御一夜、成立ならず.txt.toml — 1 dòng

```toml
[script]
2161 = "「Hachiroku cũng tham gia chứ? Nếu em không phiền.」"
```

#### グランドリライト02_ナビ.txt.toml — 1 dòng

```toml
[script]
1881 = "「Tôi rất vui vì tấm lòng của em, nhưng dù không có chuyện của 8620――\\nChỉ lần này thôi, tôi muốn đi một mình.」"
```

#### グランドリライト05_れいな.txt.toml — 1 dòng

```toml
[script]
1922 = "「Ehehe~. Reina, giúp ích được cho anh……\\nFa……vui lắm……ạ~」"
```

#### グランドリライト06_稀咲.txt.toml — 2 dòng

```toml
[script]
1945 = "「Chính em đã nói mà. Việc của thợ làm bánh thì để thợ làm bánh lo. Việc của thợ làm tàu thì để thợ làm tàu lo.\\n——Mỗi người chỉ cần hoàn thành tốt nhất vai trò của mình là được.」"
2116 = "「Ừm. Hôm nay trông cậy vào em đấy.」"
```

#### ニイロク03_粉蔵の嵐.txt.toml — 2 dòng

```toml
[script]
1404 = "「Sau khi hoàn thành thử nghiệm ở các nơi, tuyến đường thương mại cũng sẽ được mở rộng.\\nTeio - Nagoya - Osaka. Và từ Hakata, cũng sẽ mở rộng ngược lại.」"
1570 = "「Vừa làm việc thong thả――vừa thoải mái,\\nkhởi hành từ Teio...... và cuối cùng là đến Hakata.」"
```

#### ハチロク02_ハートブレイク・レイルロオド.txt.toml — 2 dòng

```toml
[script]
2352 = "「Hôm nay tao đến mà không có phụ lái. Olivy xin nhờ mọi người chăm sóc.\\nNếu được, tao muốn nhanh chóng hoàn tất việc ký kết.」"
2406 = "「Xin lỗi——cho tao hỏi, Giám đốc Hinai có ở đây không.」"
```

#### ハチロク03_冥国式レイルロオド.txt.toml — 3 dòng

```toml
[script]
2039 = "「Em đã nhận được gì đó từ Olivy——\\nví dụ như \\x%l共感;#00ffc040;cộng cảm%l;#; về quá khứ chẳng hạn?」"
2216 = "「À, ra đó là lý do em tắt đèn pha ngay lập tức sao.」"
2386 = "「Tôi hiểu. Lúc em có thể phát huy tối đa hiệu suất\\nlà khi bắt cặp với tôi. Và ngược lại cũng đúng như vậy.」"
```

#### ハチロク04_小畑越え.txt.toml — 12 dòng

```toml
[script]
1802 = "「Ở Teitetsu cũ, tại \\x%l機関区;#00ffc040;kho đầu máy%l;#; Teio, các \\x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」"
1845 = "「Tao hiểu vấn đề rồi.\\n……Hiểu thì hiểu, nhưng」"
2113 = "「Tao chưa từng có kinh nghiệm làm việc đó.\\nVì \\x%lレイルロオド;#00ffc040;Railord%l;#; vốn là thứ phải tuân theo mệnh lệnh mà.」"
2116 = "「Đúng vậy. Tất cả đều là hành động sau khi đã xác nhận và được sự đồng ý.\\nGiờ mới mang khiếu nại đến――thú thật là tao rất khó xử.」"
2223 = "「Tao đã thảo luận với cấp trên, và báo cáo việc đó cho công ty cậu. Sau đó,\\ngiám đốc công ty cậu cũng rất hào hứng 'Nếu vậy thì nhất định phải làm'.」"
2234 = "「Tao trả lời là để chuẩn bị chuyển nhượng cho Đường sắt Ohitoyo.\\nThế là, nó――」"
2268 = "「Vì thế, tao nghĩ trước tiên phải xác nhận tình trạng hiện tại,\\nnên việc đầu tiên là đưa nó đến chỗ kỹ sư \\x%lレイルロオド;#00ffc040;Railord%l;#; để kiểm tra.」"
2271 = "「Nếu bên nhận và đương sự đều hào hứng, thì bên này chỉ việc làm theo thôi.\\nVì vậy, tao đã ra lệnh cho Olivy như thế.」"
2316 = "「À. Chuyện đó tao có nghe, cũng nhận được lệnh rồi.\\nBên này cũng định chuẩn bị kỹ lưỡng cho việc bàn giao.」"
2369 = "「Không, tao đã gửi nó đến Omiya đàng hoàng.\\nKết quả kiểm tra thì, chà, vẫn như mọi khi.」"
2439 = "「Người sử dụng Đầu máy số 9 lâu nhất là tao được giao phụ trách.\\nTức là, để bắt Olivy tuân thủ mệnh lệnh.」"
2500 = "「Vậy thì, tao cứ thẳng thắn mà nói nhé――」"
```

#### ハチロク05_レイルロオドたち.txt.toml — 2 dòng

```toml
[script]
2539 = "「Olivy. Em——có biết rằng tình trạng của mình hiện tại,\\nđược khuyến cáo là năm nào cũng phải kiểm tra toàn diện không?」"
2663 = "「Để trở thành chủ tàu thì cần tiền,\\nvà anh đang nói là em có cách để kiếm số tiền đó.」"
```

#### ハチロク06_のぞみ.txt.toml — 2 dòng

```toml
[script]
2166 = "「Sapporo, Sendai, Teio, Nagoya, Ousaka,\\nKyoto, Hiroshima, Kagoshima! Olivy muốn đi vòng quanh thử xem sao!」"
2485 = "「Vượt xa xe ô tô Aircra――ví dụ như nếu có một tuyến tàu điện siêu tốc\\nnối liền Teio và Ousaka với tốc độ 200km/h thì sao」"
```

#### ハチロク12_ムナカタ来訪.txt.toml — 20 dòng

```toml
[script]
1147 = "「...Sau khi nghỉ hưu, nếu những kinh nghiệm tao tích lũy được, \\ncó thể giúp ích cho quý công ty và ngành đường sắt, thì tao rất sẵn lòng.」"
1159 = "「...Tao chưa bao giờ để tâm đến lịch sử hoạt động của \\x%lレイルロオド;#00ffc040;Railord%l;#; nhưng—— \\nRa là vậy. Nói mới nhớ, là sự tích lũy của hơn một trăm năm sao.」"
1541 = "「Không, xin đừng nhúng tay vào việc đào bới. \\nNhư tao đã nói lúc nãy, cũng có khả năng là khí gas.」"
1568 = "「Được hay không cái gì, tao là người làm thuê mà. \\nLàm sao có thể có ý kiến với kế hoạch nhân sự của chủ lao động được.」"
1642 = "「\\x%l機関士;#00ffc040;Lái tàu%l;#; Migita. Ngại quá vì phải đi ngay, \\nnhưng phiền cậu dẫn tao đến chỗ xảy ra sự cố mà cậu đã liên lạc.」"
1661 = "「A——à——ngại quá. \\nVậy, cho tao xin một tách cà phê.」"
1694 = "「A... ừm... tao không quen với bầu không khí thế này cho lắm, \\nvới lại tao cũng muốn nhanh chóng kiểm tra hiện trường \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nên——ừm, vào vấn đề chính đi.」"
1765 = "「Nếu là Kirishima thì là vùng suối nước nóng, vành đai núi lửa. \\nNhững khả năng tao vừa nêu, khả năng nào cũng hoàn toàn có thể xảy ra.」"
1840 = "「Thành thật mà nói, tao thấy rất hứng thú. \\nTao muốn nghe chi tiết hơn.」"
1864 = "「Là hiện tượng nền đất trôi đi và dịch chuyển, ảnh hưởng của nó bộc lộ lên bề mặt. \\nNếu tao nhớ không lầm, khu vực này là——」"
1936 = "「Điểm đó thì tao đã hiểu——tao nghĩ vậy.」"
1972 = "「Nếu cậu đã hiểu rõ rủi ro thì tao không cản. \\nOlivy, giám sát cậu ấy nhé.」"
1988 = "「Tao hiểu rồi. \\nKhông, xin lỗi vì đã làm mất thời gian của cậu bằng những chuyện bao đồng.」"
1996 = "「Vậy sao? Nếu thế thì tao sẽ vòng qua Kagoshima trọ lại một đêm rồi」"
2010 = "「——Tao đã chịu nhiều ân huệ của Đường sắt Mikan. \\nTao muốn làm việc đến lúc nghỉ hưu để báo đáp ân tình đó.」"
2040 = "「Không, tao cũng muốn đi khảo sát trước địa điểm xảy ra vấn đề, \\nvà cũng vì chuyện mà cậu đã nói... gọi là chuyện khác, hay chuyện liên quan nhỉ.」"
2103 = "「Về vị trí và thù lao, xin hãy xem xét cách làm việc của tao ngày hôm nay, \\nrồi đưa ra đề xuất, như vậy được không?」"
2109 = "「Nếu vậy thì mất khoảng một tiếng nhỉ——Nhưng, nếu cậu không phiền, \\nthì đưa tao về ngay bây giờ luôn sẽ giúp tao rất nhiều.」"
2219 = "「Thôi, tao xin phép cáo từ. \\nNgày mai tao vẫn còn ca trực」"
2221 = "「Chỉ với công việc đó, liệu khối lượng công việc và thù lao \\ncó đủ để tao trang trải cuộc sống không?」"
```

#### ハチロク13_実りの秋.txt.toml — 2 dòng

```toml
[script]
1833 = "「À, đúng vậy.\\nNghe em nói thì quả thật là hoàn toàn đúng như vậy.」"
1970 = "「Rõ rồi. Nếu lúc đó nhiệt độ dưới 40.9 độ,\\nthì rất hoan nghênh em làm việc.」"
```

#### ハチロク14_冬.txt.toml — 13 dòng

```toml
[script]
2427 = "「Olivy, em có thể tiếp tục nghe ngóng thêm được không?\\nÔng lão có cách nói chuyện giống tôi tên là gì?」"
2510 = "「Xin lỗi nhé, nhưng có lẽ sẽ phải nhờ em làm ngoài giờ thực sự đấy.」"
2743 = "「Em có thể…… tự nhận thức được điều đó sao.」"
2772 = "「Ừ. Song song đó, em có thể nghe ngóng xem\\ncó dấu hiệu bất thường nào khác trong phạm vi có thể không?」"
2885 = "「Thế?\\nNhiệt độ cơ thể, em đã lấp liếm bằng cách nào?」"
2908 = "「Đã rõ. Tôi sẽ bảo Navi đưa em đến tận hiện trường.」"
2979 = "「Ông Nagare cũng đã nói, có thể sẽ là một cuộc chiến trường kỳ.\\nCàng sớm càng tốt, dù sao cũng phải nhờ chuyên gia khám cho em.」"
2986 = "「Để làm được điều đó, xin em hãy đánh cược vào khả năng kéo dài tuổi thọ.\\nTất cả chúng tôi, sẽ ở đây, giám sát thay cho Olivy.」"
3152 = "「Vậy sao, nếu thế thì——để Navi đưa em về ngay bây giờ.」"
3165 = "「Vậy thì, nhờ em hỏi ông Ishida xem,\\nquanh đó có hộ nào dùng nước giếng nữa không nhé.」"
3169 = "「Chuyện đó, em đã nói với ông Tororyu-yu chưa?」"
3186 = "「Vậy thì, xin em tuyệt đối đừng cố quá sức.\\nNếu thấy mệt thì liên lạc ngay, tôi sẽ bảo Navi đến đón.」"
3220 = "「Vậy hẹn gặp lại sau. Nhờ em nhé.」"
```

#### ハチロク15a_痛みとの決別.txt.toml — 6 dòng

```toml
[characters]
1750 = "「Nhưng mà——Tao thật sự bất ngờ đấy」"
1780 = "「Công tác khắc phục vô cùng xuất sắc. Hoàn toàn không cần tao phải giám sát hay chỉ đạo,\\nvề mặt an toàn cũng không có một chút tì vết nào. Vì thế, tao mới bất ngờ」"
2003 = "「Tao cũng nghe nói cuộc khảo sát của cô đã ngăn chặn được thiệt hại về người.\\nNhờ việc chia sẻ sớm thông tin nước giếng bị đục, đã thúc đẩy người dân chủ động sơ tán」"
2038 = "「Tao bất ngờ vì cô đã học hỏi về \\x%l保線;#00ffc040;bảo trì đường ray%l;#; nghiêm túc đến mức nào.\\nVà còn truyền đạt lại một cách chính xác cho mọi người ở Đường sắt Ohitoyo nữa chứ」"
2116 = "「Ừ, đúng thế. Tao nhận được yêu cầu từ Đường sắt Ohitoyo.\\nHọ muốn tao giám sát và đánh giá các biện pháp khắc phục sự cố sụt lún」"
2345 = "Olivy"
```

#### ハチロク15b_さよなら列車.txt.toml — 7 dòng

```toml
[script]
1520 = "「Chà, nhưng nhờ vậy mà tao,\\nmới có thể chạy đến tận Yatsushiro cùng với cô đấy——」"
1686 = "「Tao thì không sao nhưng——」"
1696 = "「Tất nhiên là tao cũng uống rồi——(Ực, ực)」"
1706 = "「Xin lỗi. Cậu Migita, thay tao một chút được không」"
1727 = "「Chuyện gì——Cô nói gì tao cũng nghe」"
1734 = "「Ừ. Nhưng mà……Tao nằm mơ cũng không nghĩ tới.\\nLễ giải nghệ của cô, lại như thế này」"
1787 = "「Thay tao đi, tình trạng khẩn cấp rồi」"
```

#### ハチロクh2_お勉強の成果.txt.toml — 1 dòng

```toml
[script]
1206 = "「Rộp——rộp——liếm——chu mút——\\nưm——ưm chụt——chụt——chụụụụụt」"
```

#### ハチロクh3_磨き洗い.txt.toml — 2 dòng

```toml
[script]
1084 = "「Pua——a——Ha——\\nVâng, ngài Soutetsu……nhưng mà」"
1677 = "Trong vòng tay tôi, Suzu khẽ thở hắt ra một hơi hạnh phúc,\\nrồi mỉm cười \"Ufufu\" nhỏ nhẹ."
```

#### ハチロクh4_ゼリー・シリンジ・コンドーム.txt.toml — 2 dòng

```toml
[script]
1000 = "「Ư Iiiiiiiii!!?」"
1121 = "「N, ngài Soutetsu——Fuya——cái này——\\ntuyệt quá——kư hi i i i ưm!」"
```

#### ハチロクh5_おだいどこしごと.txt.toml — 5 dòng

```toml
[script]
992 = "「Ya……mặc dù, cách lớp quần lót——ưm——hà——Ya——mà ngài lại nhẹ nhàng như vậy——âm, vật——Ư!」」"
1006 = "「Fua——a——a……Aa——\\nem——đã tiểu——vào ngài, Soutetsu——mất rồi——ưm!」"
1010 = "「Fuaaaaaaaaaaaa!!!\\nA!?——Không được——Ya————a, Aa……」"
1033 = "「A——Aa——ưm! Ngài Soutetsu——\\nFua——Ngài Soutetsu.」"
1064 = "「Fuya!? A! Không được——nếu ấn vào——\\nưm——nữa——a, Fua——ưm ưm~~~Ư」"
```

#### ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml — 1 dòng

```toml
[script]
1335 = "Bị cậu bé cương cứng đến cực đại của tôi đâm xuyên qua——Aa."
```

#### ハチロクh7_レトロモダンメイクラヴ.txt.toml — 3 dòng

```toml
[script]
743 = "「Hya! A! Ưm!! Fua——Hakyu——\\nphù——Fua! A! A! Aaa!!!!」"
745 = "「Ka……Ha……a——Gu——ưm——như——vậy,\\nđột, nhiên——đột——nhiên——Nkyuuu!!?」"
819 = "「Ưm……Kiu——Faaaaan!!!」"
```

#### ハチロクh8_桜色のひめごと.txt.toml — 7 dòng

```toml
[script]
754 = "「Ha mu!? Ưm——Hyu——ưm……liếm——liếm,\\nChu——chụt——ho he phu……ưm——ha faa」"
762 = "「A——Ha——hi——thích quá! Sướng——Fu, a\\nsướng quá——a——nhũ hoa, cũng——tiểu huyệt, cũng」"
794 = "「Chụt……——ưm——Pua——a! Ngài Soutetsu……\\nLúc nãy——ngài vừa mới xuất, nhiều đến thế……mà——ưm」"
812 = "「Fa……a…………đầy, ắp, rượu ngọt——Cái miệng,\\nở trên……cái miệng, ở……dưới, cũng——Fa」"
813 = "「Fa……Aa——————a……Tất cả……toàn, bộ\\n——Em——tất cả——vào miệng, của——phu quân」"
825 = "「Ưm……chụt——liếm——rộp——chụt——\\nchụt……ưm……liếm láp——mút mát——chụụụt!」"
841 = "「Ưm mu! Ưm——Mu!! Chóp chép! Chụt!\\n（Su——hi）Chụt! Rerooooooo!!」"
```

#### ハチロクh9_コノフクハキルコト.txt.toml — 20 dòng

```toml
[script]
1358 = "「——Chụt——chụt, chụt——Chumu, chụt,\\nchụt, Chuu——chụt——Chumu——rộp」"
2033 = "「Fu……ưm————（Ực）\\nZu——chụt——Juuu——（Ực）」"
2043 = "「Rộp——rộp——rộộộộp——Ju, Zu——\\nZu——Rero——rộộộp——Zuzu——Zuu」"
2053 = "「Ha——ưm——chụt——Hu, hoo he hu, Haa\\n——chu ku, ưm——dai suki——re hu——Huu」"
2054 = "「Hà, hà——Haaa——hà, a——Haa」"
2055 = "「Hà, Haa——Haa——Haa—— Sâu bên trong, cô béƯ——chỉ còn, một chút, nữa thôi」"
2078 = "「A——ưm……Chuu」"
2120 = "「Chụt——rộp——mút——Chuuuu——\\nchóp chép——（Ực）——ưm——chụt, chụt」"
2122 = "「Chụt——Ju——Juru——Juuu——\\nƯm——Rerooo——rộp——rộộộộộp」"
2127 = "「Juuuuu! Jubo! Chụt! Jubu,\\nJubo! Chụụt! Juru! Ju! Bo!」"
2133 = "「Chụụt——chụt, Zu——Pero, Pero, Pero,\\nchụụt, chụt——Rero——Pero, Perooo」"
2136 = "「Chiro, Pero, Pero, Pero, rộp——\\nƯm——Pero, Pero——Pero, Pero, Pero, Pero」"
2138 = "「Chụt! Ju! Jubo——ưm, Fu,\\nrộp——Ju! Jubo! Juruuu!」"
2140 = "「Chụt, rộp——chụụụt, chụt——\\nZuzu——ưm——chụt——Rero, rộộp」"
2145 = "「Ưm——chụt——chụt! Jubo!\\nJu! Jubo! Juryuuu! Ju, Bo!」"
2147 = "「Ưm——chụt! Ju! Jubo! Ju,\\nJuchu! Chụt! Juru! Jubu!」"
2153 = "「Ưm——Hamu——chụt——chụụụt, chụt」"
2156 = "「Ưm……chụt——Chumu——chụt——ưm——\\nrộp——liếm láp——chóp chép——rộp——chu pu」"
2182 = "「Ưm mu!? Ưm——chụt——Ju!\\nJubu! Jumu! Fu——chụt, Ju!」"
2289 = "「Là khe hở——giữa hai chân——của em——ưm,\\nFu——a——Ku——Haa——là cô bé, ạ」"
```

#### ポーレット02_解放b寝台.txt.toml — 1 dòng

```toml
[script]
1795 = "「Vâng. Em cũng sẽ hỗ trợ…… Fa.」"
```

#### ポーレット08_線から面へ.txt.toml — 1 dòng

```toml
[script]
1623 = "「Xin lỗi vì đã bắt ép em.」"
```

#### ポーレットh1_ファーストセックス.txt.toml — 2 dòng

```toml
[script]
989 = "「Kyafu——Hya——bị ấn, vào——ưm.」"
1019 = "「Ưm——phù——ưm——liếm——rộp——\\nưm——chụt——chùn chụt——Chuzooooo.」"
```

#### ポーレットh2_制服変更？.txt.toml — 3 dòng

```toml
[script]
923 = "「Nhưng mà——nhưng mà——em——em——\\ná——Fuaaaaaaaaaan!」"
928 = "「Kia——á——Hio——Ngyu——」"
991 = "「A... Hia... á——Fa——á——á——a.」"
```

#### ポーレットh3_誘惑アイスコーヒー.txt.toml — 5 dòng

```toml
[script]
914 = "「Phù——ưm——chụt——chụt——\\nChumu——ưm——Chuba——Chumu」"
933 = "「Ngoạm——ưm——Chubu——chụt——\\nliếm——rộp——liếm——chụụụt」"
942 = "「Ngoạm——ưm——ưm～～\\nrộp, liếm——Chumu——chụụt」"
946 = "「A……ưm——chụt——Chumu——\\nThích——thích anh lắm——ưm——anh Soutetsu」"
966 = "「Chụt——Chumu——liếm——Reroooo」"
```

#### ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml — 1 dòng

```toml
[script]
942 = "「Ưm……chụt——Chumu——chụtttt——chụt ——Phù, a——ưm——liếm——rộp——liếmmmm」"
```

#### ポーレットh7_残業エッチもyシャツで.txt.toml — 4 dòng

```toml
[script]
818 = "「Hia! A! Hà! A! Fua! A——Nyu——Hyafu!!」"
826 = "「Hia!? Kyu——Kyufuuuun!!!」"
858 = "「Fua! A——hi——a——tử cung—— bị bắn, trúng——nóng, quá——đập, vào——Hakyu!」"
885 = "「Hà! A! A! A! Hi——Fua! Anh Soutetsu——Ku——phù——a——Anh Soutetsu」"
```

#### ポーレットh8_気動車の国のアリス.txt.toml — 2 dòng

```toml
[script]
2185 = "Hể!?"
2241 = "「Hakyu!? Ku——Phuuuuuu」"
```

#### 仲国05_真夜中の餐車.txt.toml — 1 dòng

```toml
[script]
2032 = "「Đúng vậy ạ. Ở Khu đầu máy Teio, cách làm này\\nđược gọi là 『Phương pháp khởi hành nén』 ạ.」"
```

#### 共通02_日々姫と真闇と人形と.txt.toml — 4 dòng

```toml
[script]
2133 = "「Từ lúc bắt đầu……phải rồi, em……Từ sai lầm của tôi,\\nkhi đã né tránh cơn giận của em.」"
2224 = "「Em vừa nói đến chuyện nơi ăn chốn ở——\\nHachiroku có nguyện vọng gì không?」"
2435 = "「Phải đi chứ. Tôi đã trở thành chủ sở hữu của em rồi mà.\\nTôi có nghĩa vụ phải trân trọng em.」"
2536 = "「Tôi muốn dẫn em đến đó.\\nHachiroku, tôi nên hộ tống em như thế nào đây?」"
```

#### 共通06_8620を探せ.txt.toml — 1 dòng

```toml
[script]
2112 = "「Ở \\x%l機関区;#00ffc040;kho đầu máy%l;#; Teio, trong một thời gian dài chỉ có một mình cô Kiyomi là người lái tàu thôi ạ.\\nTuy nhiên, trong thời chiến thì số lượng nữ \\x%l機関士;#00ffc040;lái tàu%l;#; đã tăng lên rất nhiều.」"
```

#### 凪ふかみ02_命の重さ.txt.toml — 2 dòng

```toml
[script]
1226 = "「Em không sao chứ? Mà, xin lỗi.\\nĐáng lẽ tôi nên đưa cho em một chiếc ô.」"
1325 = "「À, nghe em nói mới thấy đúng thật.」"
```

#### 凪ふかみ03_みかんの旅.txt.toml — 3 dòng

```toml
[script]
2099 = "「Em cũng cảm nhận được sao. Giỏi thật đấy.」"
2317 = "「A——ra là vậy.\\nNghe em nói mới thấy, quả đúng là thế thật.」"
2581 = "「Không——ngược lại em đã giúp tôi đấy.\\nNếu chỉ có một mình, tôi e là sẽ bế tắc mất.」"
```

#### 凪ふかみ08a_凪エピローグ_一番ほしい、一番.txt.toml — 3 dòng

```toml
[script]
1792 = "「Rất lâu. ……Là một Railord tốt.\\nDù cho đến khi mất đi cô ấy, tao chưa từng nghĩ như vậy.」"
1814 = "「Hai người bên tao mới chỉ sơ đẳng và nhị đẳng. Ở giải đấu tầm cỡ này,\\nđây là những thành viên khó lòng giành được cả một trận hòa.」"
1820 = "「Tao hiểu mà. Nhìn vào thứ tự thi đấu từ đầu đến giờ là biết.」"
```

#### 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml — 1 dòng

```toml
[script]
2156 = "「Fufu, được khen ngợi là vinh hạnh của tôi.\\nThực ra xuất thân của tôi là ở Teio, Đế đô đấy ạ.」"
```

#### 凪ふかみh1_修学旅行の夜.txt.toml — 2 dòng

```toml
[script]
1226 = "「Hyapu!? Oa——ưm——Nya, ư——\\nc-cái này——ưm——nóng quá——nha——nặng mùi, nha」"
1290 = "「Rộp——chụt——liếm——liếm——chụt,\\nchụt, Chu——liếm——liếm——liếm!」"
```

#### 凪ふかみh2_みずあそび.txt.toml — 3 dòng

```toml
[script]
1294 = "「Hàà... hàà... hàà——hà——Aa~Ư」"
1374 = "「Eu——ưm——chụt... chụt——rột——\\nưm... liếm——rộp——Chu——chụt」"
1428 = "「Ngón tay của bé Nagi——ưm——ngon quá——Hyo... ưm,\\nchụt——Chu——liếm——rộộộp」"
```

#### 日々姫05_市議会見学.txt.toml — 1 dòng

```toml
[script]
1854 = "「Em chu đáo thật đấy, Hachiroku. Cảm ơn nhé.」"
```

#### 日々姫05_御一夜ステーションカフェ.txt.toml — 2 dòng

```toml
[script]
2313 = "「Xin lỗi. Đã để em phải đợi rồi.」"
2338 = "「Chính vì là Railord nên thời gian buổi sáng mới quý giá chứ.\\nBắt em phải đợi chỉ để hỏi một chuyện nhỏ nhặt, thật ngại quá.」"
```

#### 日々姫h4_いもうとタオル.txt.toml — 1 dòng

```toml
[script]
991 = "「Fue……a……em……Em, đi tè――tè dầm――\\nHết……hết sạch rồi……Lên đỉnh mất――Kyufu!!?」"
```

#### 日々姫h5_白濁絵の具の射精会.txt.toml — 1 dòng

```toml
[script]
1253 = "「Ưm……phụt――ưm! Chụt――Zuju! Ực\\n――phù――ngoạm――liếm――rộp――Koshun」"
```

#### 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 2 dòng

```toml
[script]
2114 = "「Faaaaaa――Aa――Chỗ đó, em thích, lắm\\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」"
2713 = "「Anh, hai――ưm――Kuuuu~~n――Fu, a\\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」"
```

#### 真闇h1_長期熟成.txt.toml — 2 dòng

```toml
[script]
1056 = "「Chụt――ưm……ưm chụt――rộp――liếm\\n――ưm……ưm fu……Fu」"
1071 = "「Ưm……a――đang vào, này――ưm ưm――\\nchim, của――Sou, chan――Fua.」"
```

#### 真闇h2_無濾過.txt.toml — 9 dòng

```toml
[script]
1010 = "「Yan――ưm ưm――Yaa――mông, thì――\\nnóng――lắm――ưm――kỳ lạ――quá――Afu.」"
1058 = "「A――vào rồi――chim của, Sou-chan――\\nưm――đầy quá――Fua――vui quá――Ihi!?」"
1075 = "「Aha……Sou-chan.\\nMỗi lần em Chuu Chuu là nó lại giật nảy lên kìa.」"
1083 = "「Chụt――rộp――rột――Chuuu.」"
1088 = "「Fua――Nhyuu!!? ――Yaaa,\\nSou-chan――chỗ đó, không phải――ưm――Nkyun!」"
1092 = "「Ưm――Ku.」"
1450 = "Thay cho câu trả lời, tôi chỉ mải miết mút mát.\\nChụt chụt, Chuu Chuu, mút một cách say sưa."
1842 = "（Thắt lại――phập――Kypu――Thắt lại）"
1845 = "（Rột――chụt――rộp――Chumuu）"
```

#### 真闇h3_補習授業の廃校舎.txt.toml — 23 dòng

```toml
[script]
2198 = "「Pero――Reroooo――Pero, Pechu.\\nChụt――chụt――Rerooooo――rộp.」"
2212 = "「Há――a, á, Aaa――ưm――chỗ đó,\\nbị, chạm, vào――Phư――a――rùng mình, mất.」"
2215 = "「Há――ưm――Phư――á――chị, á,\\nFau――Fua――chỗ đó――bị ép vào thì.」"
2218 = "「Haa――vào, vào rồi――của Sou-chan――\\nnóng, quá――dương, vật――Fua, á――」"
2249 = "「Ka――há――á――Fua! Sâu quá, ưm,\\nsâu quá――đến rồi――tử cung, vào――tử cung rồi!!」"
2276 = "「Hamu――chụt――chụt――Koro――\\nưm……chụt――Rero, Koro――Koryu.」"
2288 = "「Chụụt――chụt――Hamu, Amu――ưm\\nchụt, chụt, Koro――chụụụụụụt.」"
2290 = "「Chụt――re, rộp――chụụt――chụt, chụt\\nchụụt――chụt――Rero――rộộộp.」"
2292 = "「Chụt――rộp――Rero――chụt, ru――\\nưm……kinh quá……nặng trĩu……nặng trịch luôn.」"
2299 = "「Juuu! Jubo! Jururu~~Nyubo!\\nJuruuu――rộộộp――Jubo! Gabo!」"
2307 = "「Ua――á――Aaa――á――」"
2311 = "「Fua! Á――Aaaaaa! Nuuu」"
2316 = "「Ưm――chụt――chụt――chụụt――ưm\\nrộp――chụụt――chụt――chụt, Mu――」"
2330 = "「Ưm……Ha, a……không được, đâu? Sou-chan. Nè?\\nA!? Chụt――Chumu――Chuu……rột.」"
2332 = "「Ưm……chụt――ưm chụt――chụt――chụụt,\\nchụt――chụt, Mu――ưm――rộộộp――Pua.」"
2334 = "「Ưm……chụt――ưmm――Pua――\\nDù không, ngon lắm――ưm――chụt（ực）」"
2336 = "「Ưm……chụt――Zuro――chụt, ruu, ru.」"
2348 = "「Ưm phư――ưm――Haa――ưm――chụụt――\\nrộp, Rero――chụt, chụt――(Cắn!)」"
2350 = "「Ưmpu――ưm――Rero――Rero, Zu――Ju,\\nchụt――chụụt――chụt, Rero――rộộp.」"
2363 = "「Ưm!? Phư――Amu――rột――Churu,\\nchụt――rộp――Jumu――Chu, Chuuu.」"
2424 = "「Picho, Pecho――chụụt――Perororo!」"
2472 = "「Đến đi! Sou-chann! Chị, chị,\\nsắp―ra――ra mất――rồi――Fua!!」"
2776 = "「Haaa――thích――thích lắm, Sou-chan――\\nchị, chị――ngay từ đầu đã――Fua!」"
```

#### 稀咲h1_性生活.txt.toml — 6 dòng

```toml
[script]
1260 = "「A――Hia――a――ra đi――bây giờ――\\nra――đi――a――đợi đã――ưm!?」"
1283 = "「Ưm――Fu――Hia――a――」"
1349 = "「Gì vậy…… Soutetsu――ưm――Ha――ngực em――\\nanh muốn――nắn bóp――lắm――ưm――sao?」"
1409 = "「So với…… tưởng tượng tồi tệ nhất, thì――nhẹ nhàng――hơn nhiều――ưm\\n……Vậy nên, Soutetsu――cử động, đi――Hyan!?」"
1473 = "「Tâm trạng sảng khoái…… vậy sao, Fufu.\\nSoutetsu, thức dậy với tâm trạng sảng khoái nhỉ.」"
1482 = "「Dịch…… nhờn rỉ ra…… ưm――Fufu,\\nDương vật của Soutetsu có vẻ――rất thích mái tóc của em nhỉ」"
```

#### 稀咲h2_プライベートルーム.txt.toml — 7 dòng

```toml
[script]
1108 = "「Không được――cái, này――ưm――cảm giác――quá――\\nFuu――」"
1120 = "「Khuôn mặt…… của Soutetsu…… tan chảy ra rồi…… kìa?\\n……A――Fu――ưm……」"
1166 = "「Hi――a――ưm――Fu――Sou――tetsu――\\nƯm――tha――cho em――em――em――không chịu nổi nữa rồi」"
1205 = "「Ưm――Ha――a――Sou――tetsu――」"
1250 = "「Đúng, là vậy đó――Cho, nên…… ưm――Fua――\\nĐặc biệt là…… phần đỉnh――đó――nha? ――Ưm――chụt」"
1253 = "「Mông…… Ha――vẫn chưa――chuẩn bị――ưm――\\nsẵn sàng――đâu, nên là――」"
1267 = "「Em, ấy hả? Chỗ này――ưm――là nơi, cảm nhận được――ưm\\n……Fa…… chỉ cần làm thế, này…… xoa, xoa――thôi」"
```

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml — 8 dòng

```toml
[script]
2152 = "「Hya――hà――Khaphu――Fua――cái đó――\\nNếu bị――làm――chậm rãi――chậm rãi――――」"
2203 = "「Ha…… ưm――Fu, a…… tay…… tay của, Soutetsu――\\nấm quá――Fu…… Ha…… Ha fu」"
2206 = "「Hả!? Hyu――Hia――cái đó――là gì vậy」"
2238 = "「A mu――ưm――Fa…… ưm――chu mu\\nAnh Houhefu――Fu――hích anh――ưm――chụt」"
2254 = "「Fua! Dương vật――tuyệt quá――Soutetsu――\\nCứng――như thế này――Phu, á――nóng quá」"
2265 = "「Ưm…… Fu――ưm――chụt――chu mu――\\nchu ru――chụt――ưm chu――Fu…… a――」"
2269 = "「Ưm……chụt――Phu――chụt――chụt,\\nchụt――Rero――Rộộp――chụt」"
2465 = "「Bình thường thì, người ta sẽ nhìn vào cơ thể. Dù là đàn ông, hay thậm chí là phụ nữ.\\nNhưng mà, Soutetsu lại nhìn vào mặt em đầu tiên――Ufufu」"
```

## 7. Kiểm tra lần 2 (second pass — đọc lại toàn bộ 436 fix đối chiếu JP)

**Số liệu: tổng 436 dòng / đã kiểm lại 436 / loại bỏ 0 / sửa 4 giá trị / bổ sung 25 dòng mới / sửa thêm 13 dòng.**

Đọc toàn bộ §4 (dòng 93–1177 của REVIEW): §4.1 Teio 8, §4.2 F2 11, §4.3 F3 7, §4.4 F5 310, §4.5 O7 37, §4.6 O25 3, §4.7 O46 1, §4.8 M7 1, §4.9 M10 1, §4.10 Munakata 48, §4.11 F-P4-1 9 — mọi fix đã đối chiếu JP (+TW).

**4 giá trị sửa trong kiểm tra lần 2:**

1. ニイロク03_粉蔵の嵐 1570 (Teio): fix cũ “từ Teio” làm mất “khởi hành” — JP 帝央を出て = “rời khỏi Teio”, khôi phục thành “khởi hành từ Teio” (chỉ đổi tên địa danh).
2. lr_凪h2 1290 (F5): bỏ hoa “hamu” — “hi-hamu” diễn MỘT token JP ひーはむ (TW một âm 啊唔), “hamu” là mảnh tách, giữ thường như quy tắc M15; chỉ “hyuki”→“Hyuki”.
3. lr_日々姫h2 1038 (F5): thêm hoa “amu”→“Amu” — あむっ độc lập, sót trong lần rà đầu (6 lần “amu”: 1041 ×2, 991, 2288, 2363, 1038).
4. 真闇h3 2292 (F5): bỏ hoa “ru” — JP ちゅる、る là một âm trượt nối bằng 、 (giống 2336 ちゅる、るう、るっ giữ “ruu”/“ru” thường); “ru” là mora đuôi, không phải token độc lập. Chỉ “rero”→“Rero”.

**25 dòng F5 bổ sung trong kiểm tra lần 2 (token “ha”/“hu”/“gao” bị loại vì nằm trong tập VN của enum5d — đọc tay từng dòng JP):**

- 24 dòng “ha”→“Ha” mới + 1 dòng “gao”→“Gao” mới (lr_凪h2 1190; lr_凪h2 1245 vừa “ha” vừa “gao” trong cùng một quyết).
- 13 dòng sửa thêm: 12 dòng thêm “ha” (1163, 1084 lr_ポーレットh2, 1325, 1042, 1593, 1887, 2168 ×2, 2220, 1064, 1183, 2330, 2203 ×2) + 1 dòng thêm “hu” (ハチロクh9 2053, lần đầu — ふっ độc lập).
- Kiểm chứng chéo toàn bộ 48 dòng chứa “ha” + 4 dòng chứa “hu” + 3 dòng chứa “gao” trong giá trị unif/moan: mọi lần còn lại đều là từ VN / mảnh tách / chant / lisp — đã ghi ở §5.

**0 dòng loại bỏ.** Không dòng nào không kiểm chứng được.

**Kiểm chứng TOML (§6):** trích mọi khối ```toml trong REVIEW, parse lại bằng tomllib — mọi giá trị khối đều bằng fix trong `unification-s4-flags-sweep-wrong.json` (xem kết quả chạy script dưới đây).

**Kiểm chứng JSON:** reload wrong.json — 436 mục, đủ 8 trường, key dạng chuỗi, jp/tw khớp CSV3 good set (chuẩn hoá U+3000→space), old_vn khớp map ưu tiên (unif đã gộp > moan > audit > CSV3), 0 fix==old_vn, 0 newline thật. VERIFICATION PASSED.

## Kết bài

**Đã quyết 18/18 mục, 436 dòng sửa mới** (E2-Teio 8, F2 11, F3 7, F5 310, O7 37, O25 3, O46 1, M7 1, M10 1, Munakata 48, F-P4-1 9) + 8 mục 0 dòng (F1, F4, O10, O13, O33, O52, O48, T74 — đã quyết/ghi chú, tính vào tổng mục). **0 dòng GHÉP** với U15a/U16 trong 436 dòng *(ở thời điểm assemble; sau 07:28: 21 dòng trùng U15a — xem Phụ lục)*.

**Giữ (có lý do):** F1 5 dòng romaji; 2336 “ru”/“ruu”; 1033 “rộp”; mikuro 1708/1758 “Fue!?”; O7 15 dòng “cô” (danh từ/ngôi ba); Munakata 2094 (trích lời Olivy); F5 giữ thường theo quy tắc mảnh tách/chant/từ VN/tên (xem §5).

**Cờ cho coordinator:**

- F1: census sửa sai của U13b (“đa số là romaji” là SAI — họ “chụt” 33 vs romaji 16); 1589 còn token れろ (M68 — U12a có thể đã sót); 1271 còn ちゅずず～っ (“Chu mút t~”) và ずりゅっ (“Chu mút”) phụ thuộc F1.
- F5: token một chữ “a” CHƯA quyết (745 lần — cần phân loại từng lần, ranh giới M17); 1213 lr_ハチロクh1: れろっ→“rero” hay “liếm” (câu hỏi M68 cho U15a); 3 dòng thán từ đối thoại “ha” (1598/1887/2449) đã viết hoa theo tiền lệ “ah”→“Ah” — coordinator xem lại vì đây là đối thoại, không phải rên.
- M7: ~58 dòng “Hự” còn lại trong cờ F1 của U12a — chưa tự mở rộng.
- T46: sweep “Olive” toàn project (~41 lần còn lại, grep TOML-2: 37 dòng đúng “Olive” + 47 dòng chứa “Olive”).
- O46/O48/O52: park cho Hieu, kèm hồ sơ tái hiện thất bại đầy đủ ở §2 mục 12/13/14.
- O7: 共通02 2550 — người nghe là NAVI (không phải Hachiroku), đại từ Soutetsu→Navi chưa quyết.
- F-P4-1: 1355/1513 còn “anh” trần Kisaki→Soutetsu (“Xin anh đấy”, “anh đã cố gắng lắm rồi” — JP không có đại từ) — cho U16/coordinator.
- Munakata→Hachiroku “cô” (5 dòng: ハチロク15a 2003/2038, ハチロク15b 1520/1727/1734) — KHÔNG thuộc mục Munakata (chỉ tự xưng “tôi”→“tao”); có thống nhất thành “em” như Soutetsu→Hachiroku hay giữ “cô” (Munakata lớn tuổi/hàm cao hơn)? Cho coordinator.
- Quy tắc slide ghi lại từ kiểm tra lần 2: mora đuôi của âm trượt nối bằng 、 giữ thường (“ru” 2292/2336) — khác token tách bằng ―― (“Ru” 1475).

— Hết batch U15b.

## Phụ lục — trùng (file,key) với U15a (phát hiện 22/11 ~07:30, sau khi U15a ghi file)

§1 ghi “0 dòng trùng với batch đang chạy” — đúng ở thời điểm assemble (file U15a chưa tồn tại). U15a ghi `unification-s4-gloss-open-leftover-wrong.json` lúc 07:28; đối chiếu cho thấy **21 dòng trùng (file,key)**. 0 dòng trùng với U16 (đã gộp, 0 trùng). Coordinator ghép khi gộp theo quy tắc GHÉP (coordinator 22/11 ~11:50): hai batch đổi token khác nhau thì ghép, không ghi đè; chỉ cộng dòng mới một lần.

**10 dòng fix GIỐNG HỆT nhau (không xung đột):** lr_ニイロクh 1322/1387 (F5), lr_凪h2 1258 (F5/M24), lr_日々姫ふかみh1 1440 (F5/M24), lr_稀咲ポーレットh1 1604 (F5/M24), lr追加_みくろ 1901 (F5/M24), ハチロクh3 1677 (F5/M24), 稀咲h1 1473/1482 (F5/M24), 稀咲h3 2465 (F5/M24).

**10 dòng GHÉP (token khác nhau — giá trị ghép đề xuất):**

- lr_ポーレットh1 1096 (F5/M15): “Nkyu——Fa——a, thế này——thích quá—— ư ư——Phu——nè——cứ thế này——nữa đi” (U15a đổi “Ưm kyu”→“Nkyu”; đợt này hoa “phu”→“Phu”).
- lr_ポーレットh2 1084 (F5/M18): = fix đợt này (“Ha——Au——Fan——ưm——Kuuun——…——Ha——…”) — đã chứa “Kuuun” của U15a.
- lr_凪h1 1162 (F5/M15): “Nku!? Pu――Fa――ưm――Juru!\nJubo! Jubu! Juba! Chụụụt” (U15a “Ưm ku”→“Nku”; đợt này hoa “Fa”/“Juru”).
- lr_凪ふかみh1 1616 (O25/M24): = fix đợt này (“A, Ufufu. Ra là vậy nhỉ. Tớ hiểu rồi…”) — đã chứa “Ufufu” của U15a.
- lr_稀咲ポーレットh1 1513 (F-P4-1/M24): = fix đợt này (“Sou, tetsu—— Soutetsu——Fufu…”) — đã chứa “Fufu” của U15a. **Lưu ý: old_vn của U15a cho dòng này CŨ (trước fix U7b):** U15a old có “Anh Soutetsu——…——anh Soutetsu?” trong khi map đã gộp (U7b P4+M1, sau U11a M1) là “Anh, Soutetsu—— Soutetsu——…——Soutetsu?” — old_vn đợt này đúng theo thứ tự gộp.
- lr追加_みくろ 1857 (F5/M15): “Nkyu! Fua! A── trượt── tuột, ra── Aaaa── anh hai── vào hết, mất” (U15a “Ưm kyu”→“Nkyu”; đợt này hoa “aaaa”→“Aaaa”).
- れいなh3 1092 (F5/M24): = fix đợt này (“Nbu——Muuu——…——Nfufuuuu~”) — đã chứa “Nfufuuuu” của U15a.
- ポーレットh8 2241 (M7/M7): = fix đợt này (“Hakyu!? Ku——Phuuuuuu”) — đã chứa “Ku” của U15a.
- 真闇h1 1056 (F5/M15): “Chụt――ưm……Nchu――rộp――liếm\n――ưm……Nfu……Fu” (U15a đổi “ưm chụt”→“Nchu”, “ưm fu”→“Nfu”; đợt này hoa “fu” cuối→“Fu”).
- 稀咲h3 2265 (F5/M15): “Ưm…… Fu――ưm――chụt――chu mu――\nchu ru――chụt――Nchu――Fu…… a――” (U15a đổi “ưm chu”→“Nchu”; đợt này hoa “fu”→“Fu” ×2).

**1 dòng XUNG ĐỘT (coordinator quyết):**

- lr追加_みくろ 1855 (F5/M15): đợt này “Ưm Hyuuuuuuuuu!” (giữ tách “Ưm hyu”, hoa “Hyu” theo F5) vs U15a “Nhyuuuuuuuuu!” (M15 gộp tách “Ưm hyu”→“Nhyu”). JP 「んひゅううううううううっっっっ！」. Lưu ý: F5 đợt này đã chủ ý hoãn dạng tách cho sweep M15 (U15a) — nên khả năng cao M15 thắng → “Nhyuuuuuuuuu!”; coordinator xác nhận.

**Bẫy loader (đã sửa trong đợt, ghi lại cho batch sau):** `loader.load_unif_multi()` từng chỉ loại trừ file output của chính đợt này; file batch đang chạy (U15a, rank −1) vẫn lọt vào map vì `current_unif()` khởi `bestrank = -1` nên `r >= bestrank` đúng ngay cả với rank −1. Đã sửa: chỉ load file có tên trong ORDER (đã gộp) — đồng thời thêm file U16 (`unification-s2-kisaki-leftover-p1-p5-wrong.json`, gộp 22/11) vào cuối ORDER. Verify lại sau sửa: PASSED 436/436; nội dung deliverable không đổi (diff skeleton §1–§4 = 0 dòng).
