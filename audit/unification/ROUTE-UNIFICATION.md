# ROUTE-UNIFICATION — Maitetsu: Last Run!! unification pass

Single pass approved 20/11 ~19:15, ordered 22/11 ~10:31 ("Gộp danh sách ngay, chạy khi rên xong") + 22/11 ~11:00 ("Chạy đợt thống nhất luôn đi").
List: `~/workspace/maitetsu-pilot/UNIFICATION-LIST.md` (304 items: DECIDED 142 incl. 8 keep / OPEN 154 / PARKED 8).
Brief: `~/workspace/maitetsu-pilot/unification/UNIFICATION-BRIEF.md`.
Base state at pass start (22/11 ~11:00): audit COMPLETE 216/216, 9,927 wrong; moans COMPLETE 64/64, 1,512 rows; GitHub head 8eae66a5; sync record 93 entries.

## Totals chain

**Tổng cộng sau đợt này: 71 mục / 2.338 dòng sai (unification)** (cơ sở 57 mục / 1.604 dòng + đợt U11a §3 fa/fu: 3 mục / 166 dòng + đợt U7a §2 P4: 1 mục / 124 dòng mới + đợt U7b §2 P4: 0 mục / 48 dòng mới + đợt U12a §3 moan dialogue: 8 mục / 98 dòng mới + đợt U12b §3 M14/M19: 2 mục / 298 dòng — gộp 22/11 ~12:05–12:15, coordinator kiểm chứng từ disk: U11a JSON 166 = TOML 166, U7a JSON 126 = TOML 126 (2 dòng GHÉP: 1416 P4+T60, 2203 P4+M17), U7b JSON 51 = TOML 51 (2 dòng GHÉP: 1470 P4+M16, 1513 P4+M1; 1629 đã đúng = fix U13a), U12a JSON 99 = tomlblock 99 (1 dòng GHÉP: 759 M15+M16), U12b JSON 298 = bảng REVIEW 298 (M14 counting, diff chỉ trong （ ）); old_vn khớp map hiện tại ở mọi batch (U11a 0 trùng; U7a csv3 114/audit 8/moan 2/unif 2; U7b csv3 42/audit 1/moan 5/unif 3; U12a csv3 51/audit 23/moan 24/unif 1; U12b csv3 294/audit 4/moan 0/unif 0); second pass U11a 166/166/0/0 + U7a 126/126/0/0 + U7b 51/51/0/0 + U12a 99/99/0/0 + U12b 303 xét/298/5 loại/43 sửa; **§2 P4 HOÀN TẤT; §3 M1/M7/M8/M9/M10/M11/M14/M15/M16/M17/M19/M68/M70 HOÀN TẤT — chỉ còn §3 M3 (U11b), §7 OPEN (U14a/b/c), §4/§6 còn lại (U10b/U15) và E2 (U13b)**)

## Decisions log (coordinator decisions on OPEN items — evidence in batch reviews)

### U1b — T1 Ohimitera (folders 03–06): 52 dòng / 12 file (Paulette 11, Reina 11, Mayami 26, Kisaki 4). GitHub: xem sync record.

### U9 — O61 DECIDED 22/11 ~11:45 (worker per delegation, parent verified): Munakata "tao" cho cả 6 dòng không có 俺 tường minh trong ハチロク16_春 (1297/1306/1637/1903/2050/2070). Bằng chứng: cùng file/cảnh với 4 dòng 俺 tường minh (1301/1884/1910/2025) xen kẽ — 1297/1306 kẹp sát 1301, 1903 cách 1910 7 key, 2050/2070 cùng mạch trả nợ Olivy với 2025; TW xác nhận ngôi thứ nhất (我) ở cả 6 dòng; Munakata dùng 俺 cả trong câu trang trọng (ハチロク12 1708) nên tính trang trọng không đổi được đại từ.
### U9 — P15 count correction: thực tế 18 dòng (không phải 17 như list) — bắt thêm おれ hiragana (ハチロク16 1884 「おれはマスターではない」). List correction: P15 ×4 + O61 thuộc ハチロク16_春, KHÔNG phải ハチロク10_炙り出し (file đó không có các key này).
### U9 — P7 verified 0 rows: chỉ 2 dòng toàn dự án có JP 日々姫さんのお兄さん (共通10 2449/2472), cả hai đã đúng "anh trai của Hibiki" trong CSV3 + TOML-2; không tồn tại dòng nào dịch thành "chị Hibiki".

### U4 — D1 DECIDED 22/11 ~11:50 (worker per delegation, parent verified): T47 bỏ "bộ" trong "bộ điều khiển trung tâm" (4 dòng: P15 1073/1981, ハチロク06 2139/2763) — dạng khóa là "điều khiển trung tâm" trần (tiền lệ ハチロク06 2145).
### U4 — D2 DECIDED 22/11 ~11:50 (worker per delegation, parent verified): T11/T12 thống nhất cả biến thể chưa liệt kê trong list ("thân điều khiển" ×5, "cơ thể lái tàu", "thân hình lái tàu", "thân lái", "cơ thể bảo dưỡng", "thân chính bảo dưỡng" → "thân vận hành"/"thân bảo trì"; tiền lệ audit れいな01 2218 / ニイロク04 2061).
### U3 — O62 DECIDED 22/11 ~11:50 (worker per delegation, parent verified vs JP+TW): "Migitai" ở 凪ふかみ03 (1071/1429/2525) là đọc sai của 右田一 → "Migita Ichi" (JP 右田一酒造元 cả 3 dòng; TW 右田一釀酒廠). O62 KHÔNG còn trong scope U14c nữa.
### U3 — T3b (worker per delegation, parent verified): 5 gloss %l "Đường sắt Đế quốc" → "Đường sắt Teitetsu" (れいな02 63, ハチロク09 2792, 日々姫01 2097, 日々姫14 1276, 真闇01 1621) — gloss trong thoại, KHÔNG phải lần xuất hiện đầu nên không giữ dạng đầy đủ; dạng đầy đủ chỉ giữ ở tooltip lần đầu 共通01 1335 (T4).
### U3 — T17 scale: bẫy T17 lớn hơn list ghi rất nhiều — 61 fix audit đã dùng "Jutsu-sen" trước quyết định 21/11 (không phải chỉ 3 dòng đã biết); tổng T17 = 85 dòng (71 "Jutsu-sen" + 13 "Jussen" + 1 khôi phục 2311).
### U3 — 2311 restoration (worker, parent verified fix == CSV3 VN + T1 + T17): ポーレット07_支線 2311 — fix audit đã cắt cụt dòng chỉ còn nửa đầu + mất tag %l; fix = toàn bộ giá trị CSV3 (JP+TW đều có đủ 2 vế). Gloss 列車 "chuyến tàu" trong fix này lấy từ CSV3 (có sẵn, không phải worker đặt) — U5-G1 phải soát lại theo quyết "đoàn tàu"; nếu file U5 không có dòng này thì đưa vào U15.
### U11a — 凪ふかみh2 1271 DECIDED 22/11 ~12:20 (coordinator per delegation, on the U11a worker's flag): KEEP "phù——a" for ふうっ――あっ — NO change. Evidence: JP 「いっ――んっ――ふうっ――あっ――こ、これ――」 (凪ふかみh2_みずあそび, Fukami speaking, H-scene); ふう is a breath/sigh token, NOT a fa/fu moan token (M1/M16/M17 cover ふぁ/ふあ/ふぇ/ふえ only); TW 呼 confirms a breath reading; the row's system is VN breaths ("Á——ưm——phù——a——c-cái này——…nóng——lắm") — converting one token to romaji would mix systems within the row; "phù" is the established VN rendering for ふう sighs project-wide. M17's rule is NOT extended to ふう. Flag closed, not carried to U15.
### U11a — 11-row candidate overlap with U12a (worker flag): checked by coordinator — only ハチロクh8 759 was a real shared (file,key) (composed M15+M16 at U12a merge); the other 10 rows (lr追加_みくろ 1857/1967/2198, lr_日々姫ふかみh1 1479, ハチロクh8 708, 稀咲h3 2188, lr_ハチロクh1 1237, lr_日々姫真闇h1 1471, 日々姫h5 1190, ふかみh2 1034) were candidates U12a enumerated but did NOT change — U12a's final JSON has 0 overlaps vs the merged map incl. U11a. No action.
### COMPOSITION RULE (coordinator, 22/11 ~11:50 — tiền lệ U4-3719): hai batch song song sửa CÙNG (file,key) ở token khác nhau thì batch gộp sau PHẢI ghép fix (combined) trước khi gộp, không ghi đè. Áp dụng U3∩U4: Grand06 3472 (T13+T18+T11), ハチロク12_再開発 2508 (T17+T7), ハチロク13 2555 (T18+T11), ポーレット03 1723 (T17+T7) — old_vn U3 đổi thành fix U4, fix = giá trị ghép, đã kiểm chứng lại từng giá trị ghép với JP. Rebuild áp dụng fix list theo THỨ TỰ GỘP; 4 dòng này tính 1 lần (U4), U3 chỉ cộng 236 dòng mới.
### E2 DECIDED by coordinator 22/11 ~12:25 (per Hieu's delegation; evidence read from investigation-open-terminology-t67-t81-REPORT.md, 6,021 lines):
- T67 KEEP "buổi bình chọn" — 0 dòng (JP thực là ひんぴょー会, không có dòng nào JP 評議会).
- T68 "Showa" cho niên hiệu (5 dòng: ハチロク03 2176/2550, ハチロクh9 1410, 仲国02 2617/2492) + lrれいな追加01 1397 → "Dầu mỏ Showa Shell" (JP 正和貝石油, chơi chữ trên 昭和シェル石油) — 6 dòng. Bằng chứng: đa số 19/25 "Showa"; tiền lệ niên hiệu romaji (大詔 → "Taisho" 9 dòng); tips §34 thân bài tự viết "Showa".
- T69 KEEP "Khách sạn Teio" — 0 dòng.
- T70 KEEP "Niigata" — 0 dòng.
- T71 "Tàu nhà hàng" cho mọi dòng とれいん食堂 / とれ食 — 11 dòng (10 "Toa ăn Train" + 1 "nhà ăn trên tàu" 日々姫09 1753). Bằng chứng: đa số 13/24; "Toa ăn Train" lai Việt+Anh, không phải tên riêng nguyên bản cũng không phải tiếng Việt trọn vẹn. Độ tin cậy Trung bình (13 vs 10 hẹp).
- T72 "hình quạt" (chỉ tính từ; danh từ Gara/nhà chứa ngoài phạm vi) — 18 dòng. Bằng chứng: TW tips §132 thân bài tự viết "gara hình quạt" hai lần; 扇 = quạt; 6 dòng "hình quạt" đã là audit-fix.
- T73 "Hinomoto Nadeshiko" — 3 dòng (ハチロク09 1879, ハチロクh6 993, ハチロク09 1508 katakana). Bằng chứng: T6 đã chốt 日ノ本 = "Hinomoto" — "Yamato" phá quy tắc; JP katakana đọc thẳng Hinomoto; TW localize sang Nhật thật, JP thắng TW.
- T74 "hợp đồng chủ tàu" — 1 dòng (凪h2_おとなの水着 1766; list trích sai file 日々姫h2). Bằng chứng: まいてつ = "chủ tàu" đã chốt (T8); TW 掌車人契約 đồng thuận nghĩa.
- T75 "chụt"-family cho MỌI âm hôn trần, theo từng token, theo công thức độ dài nguyên âm — 78 dòng. Bằng chứng: đa số áp đảo 483 dòng đã là "chụt"-family; ちゅっ→"chụt", ちゅうっ→"chụụt", ちゅむっ/ちゅるっ/ちゅろっ/ちゅぷっ/ちゅぱっ/ちゅぶっ→"chụt" (một token = một rendering). LƯU Ý: quyết định này lật một phần lựa chọn romaji có chủ ý của moan pass (27 ứng viên moan-src) — đa số thực hành 483 dòng đi ngược lựa chọn đó. 2 dòng biên worker xác nhận lại khi áp dụng: 日々姫h6 3707, ポーレットh3 967.
- T76 PARK CHO HIEU — 0 dòng quyết (xem PARKED; bằng chứng §T76.2–§T76.4: 2 dòng META ハチロクh1 1393 + 日々姫h1 1465 chứng tỏ "bướm" là từ trẻ con おまんまん; va chạm おちんちん/"chỗ đó" ở lr_日々姫h1).
- T77 MODIFIED by coordinator (khác đề xuất E2): "rộp" cho token SFX れる/るっ ONLY; れろ LOẠI KHỎI T77 — giữ quyết M68 (F1, đã áp dụng ở U12a: ngắn → "liếm", dài ≥3 → romaji "Rero"). Lý do: (1) M68 đã quyết れろ 22/11 ~11:30 trên bằng chứng F1 và U12a đã áp dụng — lật lại là flip-flop; (2) phân biệt âm vị: れる/るっ kết thúc -ru/-ru' (ma sát/dừng, hợp tượng thanh "rộp" có phụ âm cuối -p) vs れろ kết thúc nguyên âm mở -o (giọng rên, hợp "liếm"/romaji); (3) giữ được hệ phân biệt có chủ ý của audit Paulette/Reina (ぺろ→"liếm nhẹ" vs れる→"rộp") cho các token れる/るっ. ぺろ giữ "liếm"; じゅるっ giữ "rột"; るっ trong chuỗi đâm thuộc T78 (phân biệt bằng token kề). Số dòng: worker U13b liệt kê chính xác (≤229 trừ các dòng れろ).
- T78a ずぶ (SFX) → "Phập" — 21 dòng (15 romaji + 5 "Thọc sâu" + 2597 "lún"). Bằng chứng: đa số 104/129; TW nhất quán hướng VÀO (插入/直插到底). 15 dòng chuỗi romaji: đổi theo từng token, giữ các token khác; nếu chuỗi mất mạch thì ghi chú, không đổi cả chuỗi.
- T78b ぬぶ: KHÔNG quy tắc blanket — quyết theo từng dòng; 3 dòng đổi → "Rút" (れいなh2 1730, 真闇h2 1830, lr_ふかみh2 1122 — 1122 độ tin cậy Thấp, worker đọc lại cảnh; nếu là đâm sâu thì giữ "Nubu!" và ghi chú); 7 dòng giữ (gồm ポーレットh4 1609 giữ "Rút" theo audit — TW tự mâu thuẫn trên ぬぶ nên không quyết được dòng này).
- T79 きゃふ → romaji "Kyafu" theo công thức độ dài nguyên âm — 1 dòng (稀咲h3 1988 "kya phu" → "Kyafu"). Bằng chứng: 24/25 đã romaji; họ âm breathy nhất quán (ひゃふ→"Hyafu" 21 dòng, ふにゃ→"Funya" 19 dòng).
- T80 PARKED (in-game font check — đã park từ trước).
- T81 KEEP "Fukutake" — 0 dòng (audit đã sửa đúng từ "Fukuoka" của Gemini).
- Tổng E2 đã quyết: 13 mục (T67–T75, T77–T79, T81) + T76 park + T80 parked; ~370 dòng trừ phần れろ của T77 (worker U13b liệt kê chính xác).
- Mục mới cho U15 (E2 phát hiện, ngoài phạm vi T69): địa danh 帝央 — 3 dạng: "Teio" (đa số ~15 dòng), "Teiou" (共通06 2112, ニイロク03 1570), "Trung tâm Hoàng gia" (仲国05 2032 — dịch mô tả tên riêng, sai chuẩn). Xu hướng: "Teio" (furigana ていおう, romaji ō→o, đa số áp đảo) — chưa quyết, chờ U15.
- Trích dẫn list đã hiệu chỉnh (E2 §0): T69 thực 4 dòng (thiếu グランドリライト08_ふかみ 2155); T72 thực 24 dòng (không phải 23); T73 sai file ハチロク03_冥国式 (dòng thực ハチロク09 1879, ハチロクh6 993, ハチロク09 1508); T74 sai file (dòng thực 凪h2 1766, không phải 日々姫h2); T71 thiếu 3 dòng ngoài H08; T76 nhiều trích dẫn sai (xem E2 §T76.1).

## PARKED for Hieu / in-game (not touched in this pass)

- §5 tag sweep S1–S5, S7 (B19 gate: Paulette 13 key 1596 in-game check).
- §4 G13/G14 (tag sweep items).
- §1 T80 (fa/fu font check in-game).
- §1 T76 (おまんこ register — Hieu's personal preference; evidence in E2 §T76.2–§T76.4; 3 candidates "chỗ đó" / "lồn" / "Cái bướm" + investigator's keep-stratification tendency; coordinator to present to Hieu, do NOT decide in the pass).

## Merged batches

- U2a (22/11 ~11:15, worker decided per delegation, parent spot-verified): 御鉄 = 御一夜鉄道 → "Đường sắt Ohitoyo" (9 rows; ruby [おんてつ,1] + TW 御鐵 + company context). オヒトヨ/おひとよ kana = same as kanji 御一夜 (12 rows; TW writes 御一夜).
- U1c flag (22/11 ~11:15, NOT fixed — for leftovers batch U15): Grand 11 key 2485 — JP/TW have 御一夜 twice, VN renders only the second (first dropped); pre-existing omission the audit passed.
- T1 reconciliation (22/11 ~11:15): project-wide Ohimitera remainder was 311 (not §0's 333 — consolidation map had 9,190 audit pairs vs 9,200 mapped here + moan fixes). U1b 52 + U1c 38 merged; remaining 221 in folders 00–02 (U1a running).
- U9 (22/11 ~11:45, parent-verified from disk): P15 Munakata 俺/オレ/おれ → "tao" 18 dòng / 5 file (28 lần thay tôi→tao; お前 không đụng); O61 "tao" 6 dòng ハチロク16; P7 0 dòng (đã đúng sẵn). F28 không đụng (done in U10).
- U9 flag (NOT fixed — needs a NEW item, candidate for U15): còn **55 dòng Munakata "tôi" project-wide không có 俺 tường minh trong JP** (vd. ハチロク12 1147 dùng 私 trang trọng) — ngoài scope P15/O61; quyết riêng nếu Hieu muốn thống nhất toàn bộ "tao".
- U4 (22/11 ~11:50, parent-verified from disk): §1 set-3, 11 mục / 193 dòng / 56 file — T6 Hinamoto→Hinomoto 34, T7 Yui→Yunoi 107 (111 lần xuất hiện), T15 Obata/Kobata→Okoba 6, T16 Suntetsu→Suntai 1, T41 Kiha→KiHa 18, T45 Meikoku→Minh Quốc 6, T47 →"điều khiển trung tâm" 5, T11 →"thân vận hành" 11, T12 →"thân bảo trì" 3, T19 phi hành đoàn→nhân viên tàu 1, T20 ông nội→ông ngoại (Seki only) 3; T54/T55 0 dòng (đã xong). 3719 đã rebase về giá trị gộp với U2c (không regression).
- U4 flags (NOT fixed — for U15/new items): T20 mục con OPEN (ハチロク09 2027 "bác Seki", 日々姫03 2368/2607, ハチロク07 2588 "các ông của Nagi", 凪ふかみ01 1884, ふかみh1 2368/2607, Grand 08 2010, 日々姫04 2668); 2 "Ohimitera" còn lại được giữ (共通14 1671/1805 — kiểm chứng là cố ý giữ? ghi chú worker: preserved); 2 địa danh Yui giữ theo ngoại lệ (ハチロク09 2118, ハチロク04 1925); P03 1728 gloss 閉塞 "phong tỏa" (giá trị audit) — tips glossary nói "Đóng đường", thuộc batch gloss (không nằm trong scope U5 G1/G2 — đưa vào U15).
- U3 (22/11 ~11:50, parent-verified from disk): §1 set-2, 6 mục / 240 dòng / 69 file (236 dòng mới + 4 dòng ghép với U4) — T3 →Teitetsu 55 (50 trần + 5 gloss T3b), T10 →"Công chúa Tàu điện" 28, T13 宮司→"đền chủ" 38, T14 →"Migita Ichi" 21 (gồm O62 "Migitai" 3 dòng), T17 "Jutsu-sen"→"Jutsusen" 85, T18 →"túi công tác" 16. Second pass bắt 3 lỗi "Migita Ichi Ichi" (1835, 2366, 2444) đã sửa đồng bộ JSON+REVIEW+TOML.
- U13a (22/11 ~12:00, coordinator-verified from disk): §1 OPEN T56–T66 (E1 DECIDED), 8 mục / 171 dòng / 33 file (165 mới + 6 trùng đã gộp) — T56 Trung Quốc 122, T57 Anh Quốc 5, T58 Thị Hiện Lưu 3, T59 Quirquitium 1, T60 Tổng giám đốc 27, T61 công ty holding 7, T63 Đường sắt Đế quốc Hinomoto 4, T66 chín tỉnh 2; T62/T64/T65 giữ nguyên 0 dòng. LỆCH SỐ: T56 thực 122 (không phải 124 như E1 — E1 đếm trùng 2 dòng "tiếng Zhongguo").
- U13a flag (NOT fixed — for U15): F-T56-1 — 仲国08 2823 (JP 日仲, không chứa 仲国; CUR còn "Trọng Quốc" — chờ quyết).
- U5 (22/11 ~12:00, coordinator-verified from disk): §1 misc + G1/G2 gloss sweeps, 8 mục / 336 dòng / 82 file (324 mới + 12 trùng đã gộp) — T8 "chủ tàu" 18, T25+T26 3, T27 "Thẻ bảng (Tablet)" 90, T51 2, T52 20, G1 "đoàn tàu" 121, G2 "lái tàu" 83; T9/T28/T50/T53 0 dòng (đã đúng sẵn). 6 dòng GHÉP với U3/U4 bởi coordinator (2464 G1+T7, 2251 T27+T10, 2326/2328 T27+T11, 2336 T27+T12, 2814 G2+T41).
- U5 flags (NOT fixed — for U15): U5-1 (G8 Common 08 — "Thẻ bảng (Tablet)" hay "thẻ bảng" trần); U5-2 (12 dòng tag %l thiếu `;` đóng — thuộc tag sweep đã park); U5-3 (ニイロク04 — term tag 操作板 ≠ JP タブレット, 10 dòng); U5-4 (audit thêm %l tag ở 7 dòng JP không có tag — G12); U5-5 (真闇h3 3299 "Đại học Hoàng gia" — T5 chưa giao); P07 2311 G1: U5 KHÔNG chứa dòng này (khôi phục sau khi U5 liệt kê) — đưa vào U15.
- U11a (22/11 ~12:05, coordinator-verified from disk): §3 M1/M16/M17 fa/fu, 3 mục / 166 dòng / 47 file — M1 ふぁ/ふあ → "Fa"/"Fua" (H-scene romaji), M16/M17 strict Fa/Fua + split forms; diff chỉ đổi token rên (0 outlier); 11 dòng trùng enumeration U12a đã cờ cho coordinator gộp (chỉ 759 thực trùng).
- U7a (22/11 ~12:05, coordinator-verified from disk): §2 P4 Kisaki "anh Soutetsu"→bare "Soutetsu", 1 mục / 126 dòng / 5 file (124 mới + 2 GHÉP: 1416 P4+T60, 2203 P4+M17); D1 (2 dòng rên tách tên tính là fix), D2 (tiêu chí là NGƯỜI NGHE). Grand 08 1702 KHÔNG phải dòng P4 (đã kiểm chứng).
- U7b (22/11 ~12:10, coordinator-verified from disk): §2 P4 tsuika + lr, 1 mục / 51 dòng / 4 file (48 mới + 3 trùng: 1629 đã đúng = fix U13a, 1470/1513 GHÉP với U11a); F-P4-1: dạng tách "Anh, Soutetsu"/"Anh Sou, tetsu" (8 dòng) ngoài chữ P4 — cần quyết chung (U15).
- U12a (22/11 ~12:10, coordinator-verified from disk): §3 moan dialogue tokens M7/M8/M9/M10/M11/M15/M68/M70, 8 mục / 99 dòng / 43 file (98 mới + 1 GHÉP: 759 M15+M16); M7 còn 59 dòng "Hự" ngoài 4 file quy ước + 5 đã đổi (follow-up); M15 sweep ~154 dòng dạng tách chưa đổi; ふかみh2 989 "Kh" vs M7 (khóa Kh thắng).
- U12b (22/11 ~12:15, coordinator-verified from disk): §3 M14 descriptive-SFX counting + M19 re-checks, 2 mục / 298 dòng / 53 file — M14: 298 dòng (17 M14a + 2 M14b + 279 M14c, 9 SPACED); M19: 0 dòng sửa (3 dòng kiểm lại giữ nguyên); second pass 303 xét / 298 / 5 loại / 43 sửa; HAS-RUN mismatch scan 126 dòng — ứng viên follow-up (U15).
- U11b (22/11 ~12:30, coordinator-verified from disk): §3 M3 Á re-examination, 1 mục / 1 dòng / 1 file — 凪ふかみh1 1218 きゃあっ→"Kyaa" (2 a theo công thức; old_vn = moan fix, vòng rên chỉ đổi phù→Fua mà sót "Á" đầu dòng). Quét toàn dự án: 441 dòng thô → 37 ứng viên → 1 lỗi; 36 dòng GIỮ có lý do (Á diễn あっ 14, やっ theo M8 5, tiểu từ địa phương 11, mora khác 5, tiếng hét giật mình 1). 8 dòng "Á" họ ひゃ cùng file đã romaji sẵn (1214/1216/1219/1221/1222/1223/1224/1226 — kiểm chứng từ moan file). **§3 HOÀN TẤT** (M3 là mục §3 cuối cùng — M1/M3/M7/M8/M9/M10/M11/M14/M15/M16/M17/M19/M68/M70 đều xong).
- U8 (22/11 ~12:40, coordinator-verified from disk): §2 P3/P5/P6/P8 + §6 F17–F24 + §7 O2/O3, 14 mục / 50 dòng (48 mới + 2 GHÉP) / 5 file — HIỆU CHỈNH số học 22/11 ~12:50: chuỗi tổng sau U8 là 86/2.387, không phải 86/2.389 (2 dòng GHÉP đã cộng ở U7b/U13a không cộng lại, theo tiền lệ U3/U7a/U7b/U12a/U5/U13a). — F17 1547 "Em có sao không?" 1, F18 1166 "'To'" 1, F19/P8 Niiroku "Tôi" 3, F20 3 (1116 GHÉP cả F21), F21/P3 17 (tsuika01 9 + tsuika02 8 + 稀咲h2 3, trong JSON 16 F21 + 1 F20 (1116) + 3 P3), F22/P6 4 (1327/1783 GHÉP cả F24), F24/P5 tsuika01 6 (trong JSON 4 F24 + 2 F22), F23 0 dòng mới (U7b đã sửa 1488/1687/1783), O2 0 dòng (XÁC NHẬN phán đoán biên của audit), O3 15 (lr_ニイロクh "em"→"Tôi", gồm 1439 "của mình"→"của tôi"). Second pass 50/50/0/0; JSON 50 = TOML 50 (5 file); old_vn 50/50 vs map đã hiệu chỉnh (csv3 40 / audit 3 / moan 5 / unif 2); 2 dòng GHÉP trên fix đã gộp (1783 U7b, 1077 U13a). **§2 P3/P5 (nhánh tsuika)/P6/P8 HOÀN TẤT** (P5 nhánh Kisaki03 + 稀咲02 và P1 xem dưới — U16).
- U8 — O3 evidence VINDICATED (coordinator re-counted): 自分 trong dòng Niiroku nói = h-file ×8, 01 ×14, 02 ×20 (khớp worker; đếm thô CSV3 11/25/38 gồm cả narration/người khác nói). 7/15 dòng O3 có 自分 tường minh, 8 dòng còn lại không có đại từ tự xưng nào trong JP (chủ ngữ lược — bình thường); 0 dòng có わたし/あたし. Quyết "Tôi" đứng trên: (a) người nghe là Akai (trang trọng, 赤井運転士), (b) quy tắc phẳng 03:32 (31 "Tôi" vs 3 "Em" ở 01/02), (c) không có chuyển register trong JP ở file h.
- U8 — F21/C20 correction (coordinator verified vs CSV3): tsuika02 chỉ 8 dòng, KHÔNG phải 9 — §8 C20 SAI: 1180 JP 「ぁっ」 (gasp của Suika), 1168 JP 「あ――」 (Soutetsu "A——"), 1043 không tồn tại ở cả hai file tsuika. F21 tổng thực tế 17 dòng (9+8), không phải 18. List P3 "tsuika02 9 dòng" đã hiệu chỉnh.
- U8 — P5/tsuika02 0-row claim verified: worker rà 22 dòng Kisaki tự xưng "Tôi"/"tôi" số ít (liệt kê đủ 22 key ở REVIEW §5: 1035/1072/1084/1176/1179/1210/1233/1239/1258/1286/1325/1331/1332/1334/1373/1383/1466/1501/1599/1616/1644/1678 — loại "chúng tôi" số nhiều + "em" gọi Suika); 0 dòng đổi (chuyến khảo sát công việc, chế độ công việc xuyên suốt). List claim "15 dòng → em" không tái tạo được; "1184 là ranh giới như 1744" VOID (1184 ở tsuika02 là gasp của Soutetsu 「っ！！！」; ở tsuika01 key 1184 không tồn tại).
- U8 — tsuika01 1564 DECIDED by coordinator 22/11 ~12:40 (per delegation; closes the last open Kisaki self-pronoun row in tsuika01): KEEP "Em" (0 rows). Evidence: JP ボク; ngữ cảnh tán gẫu bữa tối (không phải nội dung công việc/quyết đoán); Kisaki nói peer-to-peer với Soutetsu ("Nhưng cậu biết không? Em và cô Khương lại không như thế…") — nhánh thân mật/thân tình của quy tắc ngữ cảnh ủng hộ "em"; không có trigger chế độ công việc. Worker đã cố ý không tự mở rộng F24; quyết này chốt dòng đó.
- U10b (22/11 ~12:50, coordinator-verified from disk): §6 F30 moan-beats-audit, 1 mục / 12 dòng / 4 file (11 mới + 1 GHÉP 1716 với U11a) — mikuro 5 (1708/1716/1758/1811/1901 huỷ fix audit, khôi phục CSV3), ポーレットh6 4 (768 "Kyuuuuuuuuuun" 10u, 800/818 "Kua", 869 "Nkyun!"), ポーレットh5 2 (932 "Kua!", 947 "Nkyun!!!!"), ハチロクh8 878 khôi phục "ưm!" (OPEN → QUYẾT trong đợt này: JP んっ là mora hơi thở riêng biệt + TW 嗯; audit mời xem lại). 105 dòng xét, 93 giữ có lý do. Second pass 12/12/0/0; JSON 12 = TOML 12; old_vn 12/12 (audit 11 / unif 1); fix == CSV3 VN 12/12 (khôi phục); 768 đếm 10u đúng công thức (1 base きゅ + 9ぅ). **§6 F30 HOÀN TẤT.**
- U10b — F5 DECIDED by coordinator 22/11 ~12:50 (per delegation): token romaji SFX viết hoa MỌI VỊ TRÍ (đầu dòng và giữa dòng). Bằng chứng: M16 của U11a viết hoa 18/18 dòng mikuro kể cả giữa dòng; vòng moan nghiêng về viết hoa sau ── (10 vs 2); cùng file mikuro không thể vừa "Fua" hoa (U11a) vừa "fue"/"pua" thường (CSV3) cho cùng họ token; chữ thường của CSV3 là thói quen sentence-case của Gemini, không phải quyết định. 3 fix U10b đã sửa theo quyết này trước khi gộp (1716/1758 "fue"→"Fue", 1811 "pua"→"Pua"; 1708 "Fue"/1901 "Pua" đã hoa sẵn). "fu" mảnh ở 1811 giữ nguyên (mảnh hơi thở, không phải token đầy đủ).
- U10b — F9 CONFIRMED by coordinator 22/11 ~12:50: worker ĐÚNG — chuỗi tổng sau U8 là 86/2.387, không phải 86/2.389 như bản gộp U8 ghi. Tiền lệ U3 (+236 không phải +240), U7a (+124 không phải +126), U7b (+48 không phải +51), U12a (+98 không phải +99), U5 (+324 không phải +336), U13a (+165 không phải +171) đều chỉ cộng dòng MỚI; GHÉP không cộng lại. ROUTE + queue đã hiệu chỉnh; báo cáo gộp U8 gửi parent ghi 86/2.389 là sai +2 (sửa trong báo cáo này).
- U10b — F6 NOT REPRODUCIBLE (coordinator checked from disk): file supplement ハチロクh3 chỉ có 4 key (963/1007/1039/1067), không chia sẻ key nào với file main (24 key); các key 1029/1063/1677 chỉ có trong main, không có JP trùng nào trong supplement — không có xung đột main-vs-supplement. Cờ đóng, không đưa vào U15.
- U10b — F1 DONE: nhãn file F30 trong UNIFICATION-LIST.md đã hiệu chỉnh theo bảng §2 của REVIEW (17 chỗ + 1 ghi chú; mục con OPEN 878 cập nhật thành ĐÃ QUYẾT).
- U10b flags (NOT fixed — for U15): (F2) M7 có bao phủ ポーレットh8 2241 (くっ→"Hự" giữ)?; (F3) M10 có bao phủ ポーレットh8 2185 (ふえ độc lập, ứng viên thứ 6) và ranh giới M10 ở mikuro 1708/1758?; (F5-follow) 2 dòng "fua" thường cuối câu ở lr_ニイロクh (1322/1387) chuẩn hoá thành "Fua" theo quyết F5; (F7) 4 dòng audit-only fa/fu mikuro 1703/1707/1925/2322 đã kiểm tra — đều là hơi thở ngắn ふっ/ふぉ ("Phù"/"phu" đúng), không phải ứng viên huỷ; (F8) lr_ポーレットh2 1095 không phải 1095 của F30 (ngoài phạm vi).
- U8 flags (NOT fixed — new batch U16, queued): (F1) P1 chưa có batch nào nhận — Soutetsu tự xưng "Anh" với Kisaki còn ~18 dòng ở 稀咲h2 (915/932/933/1207/1226/1230/1233/1236/1265/1271/1273/1275/1278/1295/1302/1313/1321/1334 — 933/1334 đã sửa địa chỉ ở P3 nhưng tự xưng "Anh" còn nguyên) + tsuika01 1488 câu 2 + tsuika02 1084 (mẫu "Anh" trần chỉ Soutetsu, U7b để lại) — quyết chung P1 ("tôi" với Kisaki) trong U16; (F2) P5 nhánh Kisaki03 + 稀咲02 chưa rà theo quy tắc ngữ cảnh — U16; (F3) tsuika02 1077/1568 xác định người nghe bằng loại trừ (Khương không bao giờ "em"; Suika vắng mặt/không tư vấn) — độ tin cậy trung-cao, có thể đảo ngược, ghi lại để U16/rebuild kiểm chứng; (F4) O2 nhãn file trong list sai (các key thuộc lr稀咲追加03/02, không phải 稀咲h2/h1).
- U11b flag (NOT fixed — needs its own decision, candidate for U15): ranh giới M3 — tiếng hét GIẬT MÌNH きゃっ trong file H (ふかみh1 995, audit fix "…Á!? Oa a a a a a a a!?", giữ "Á!?" theo chuẩn tiếng hét toàn dự án, vd. 共通05 2262, 共通07 1754/1755). Mở rộng M3 sang tiếng hét sẽ implicates cả 175 dòng hét ngoài file H — cần quyết riêng, không tự mở rộng.
- U12a/U12b flags (NOT fixed — for U15): M7 follow-up (59 "Hự" + 5 đã đổi); M15 sweep ~154 dòng dạng tách; ふかみh2 989 "Kh"; M10 cờ trong dòng M11 (ポーレットh2 929/957); ranh giới Ya-vs-Á (1445, 862, 927, 1007, 1070, 1010, 1084); HAS-RUN 126 dòng; F1 sửa số liệu (4 file quy ước 11 dòng Hự; lr_ニイロクh "Fu" ×3; ハチロク02 2170 thuộc ハートブレイク).
- U3 flags (NOT fixed — for U15/new items): 帝央機関区 2 dòng (ハチロク04 1802, 仲国05 2032 — chưa có chuẩn); tên công ty 帝国線路合同会社 8 dòng (稀咲03 ×6, 稀咲h3 ×2 — JP không có 帝鉄, cần quyết tên riêng); các dạng 宮司 "thầy tế" ×14, "Đại tư tế Akai" ×25, "ông Akai" ×11 + "ông" ×1 — có thống nhất về "đền chủ" hay không (chưa quyết); 2 dòng "Denshahime của Mouri" mà JP chỉ nói 毛利の姫 (日々姫11 1774, 日々姫12 2908); trích dẫn list lỗi thời ("Paulette 02 1525" không tồn tại, ハチロク10 [characters] 2791/[character_subs] 2789 không có trong CSV3/TOML-2).


# Snippet — Unification U1b: §1 T1 "Ohimitera" → "Ohitoyo" (folders 03_Paulette / 04_Reina / 05_Mayami / 06_Kisaki)

- Đợt U1b: mục §1 T1 (DECIDED 19/11, Hieu) — dạng cũ "Ohimitera" trong 4 folder 03/04/05/06: **52 dòng sửa, 12 file** (Paulette 11, Reina 11, Mayami 26, Kisaki 4).
- Cả 52 dòng đều đọc JP và xác nhận JP chứa 御一夜 (hoặc 御一夜鉄道): 0 dòng flag misalignment; đợt kiểm tra thứ hai: 52/52 xác nhận, 0 loại bỏ, 0 sửa lại.
- 216 dòng "Ohimitera" khác trong 4 folder đã sửa sẵn trong audit — không đụng. Đếm lại toàn dự án: giá trị hiện tại còn "Ohimitera" là 311 dòng (ước lượng §0: 333); sau đợt này T1 còn 259 dòng ở các folder còn lại.
- Ranh giới: 4 dòng "Đường sắt Ohimitera" (Paulette h3 1255, Mayami 01 1404, lr Kisaki 03 1186/1267) nay đã đúng dạng đích "Đường sắt Ohitoyo" — batch T2 bỏ qua. Mayami h3 2524 còn 1 "Đường sắt Ohito" chờ T2; Paulette 04 1517 còn "Jutsu-sen" chờ T17; Mayami 01 1641 còn "Tuyến Yui" chờ T7.
- File: `unification/unification-t1-ohimitera-03-06-REVIEW.md` + `unification-t1-ohimitera-03-06-wrong.json` (52 mục, kind="terminology", item="T1").

**Tổng cộng sau đợt này: 1 mục / 52 dòng sai (unification)** (cơ sở 0 mục / 0 dòng + đợt U1b 1 mục / 52 dòng — đối chiếu ROUTE-UNIFICATION.md 22/11 ~11:00)

# Snippet — Unification U1c: §1 T1 "Ohimitera" → "Ohitoyo" (folders 07_Nagi_Fukami / 08_Niiroku / 09_Grand / 10_Chikuni / 11_Other)

- Đợt U1c: mục §1 T1 (DECIDED 19/11, Hieu) — dạng cũ "Ohimitera" trong 5 folder 07/08/09/10/11: **38 dòng sửa, 5 file** (Grand 01: 19, Grand 11: 12, 凪ふかみ05: 3, Grand 09: 2, 凪ふかみ02_命の重さ: 2; 40 occurrence — Grand 01 key 3648 và 2869 mỗi dòng ×2). Folders 08/10/11: 0 dòng (08 và 10 đã sửa hết trong audit; 11 không có dòng nào).
- Cả 38 dòng đều đọc JP và xác nhận JP chứa 御一夜 (hoặc 御一夜鉄道): 0 dòng flag misalignment; đợt kiểm tra thứ hai: 38/38 xác nhận, 0 loại bỏ, 0 sửa lại.
- 53 dòng "Ohimitera" khác trong 5 folder đã sửa sẵn trong audit — không đụng (29 sửa trực tiếp → Ohitoyo; 24 dịch mới toàn bộ, JP không có 御一夜). Đếm lại: CSV3 VN có "Ohimitera" trong 5 folder là 91 dòng (07: 15, 08: 5, 09: 56, 10: 15, 11: 0).
- Ranh giới: 0 dòng "Ohimitera" trong gloss %l; 2 dòng "Đường sắt Ohimitera" (Grand 11 key 2485, 3806) nay đã đúng dạng đích "Đường sắt Ohitoyo" — batch T2 bỏ qua. Grand 11 key 3916 còn "Yui"/"tuyến Yui" chờ T7 — không đụng. 1 cờ: Grand 11 key 2485 lược mất 御一夜 đầu trong VN (F-T1-1, xem REVIEW).
- File: `unification/unification-t1-ohimitera-07-11-REVIEW.md` + `unification-t1-ohimitera-07-11-wrong.json` (38 mục, kind="terminology", item="T1").

**Tổng cộng sau đợt này: 1 mục / 90 dòng sai (unification)** (cơ sở 1 mục / 52 dòng + đợt U1c 38 dòng — cùng mục T1 đã tính ở U1b nên không cộng thêm mục; đối chiếu ROUTE-UNIFICATION.md 22/11 ~11:10, đã rebase từ base 0/0 lúc spawn)

# Snippet — Unification U2a: §1 T1 "Ohito" → "Ohitoyo" + T2 "Đường sắt Ohito" → "Đường sắt Ohitoyo" (folders 00–05)

- Đợt U2a: mục §1 T1 (DECIDED 19/11, Hieu) + T2 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền) — dạng cũ "Ohito" (trừ "Ohimitera", thuộc batch U1) trong 6 folder 00/01/02/03/04/05: **136 dòng sửa, 26 file** (Hachiroku 119, Paulette 9, Hibiki 5, Mayami 2, Reina 1, Common 0).
- Phân loại: T2 "Đường sắt Ohito" → "Đường sắt Ohitoyo": 95 dòng; T1 trần "Ohito" → "Ohitoyo": 39 dòng; cả hai dạng trong một dòng (T1+T2): 2 dòng (ハチロク02 3129, ハチロク05 3790). 142 lần xuất hiện dạng trần.
- Cả 136 dòng đều đọc JP (+TW) và xác nhận JP chứa thuật ngữ: 御一夜鉄道 80, 御一夜 35, オヒトヨ 11, 御鉄 (viết tắt của 御一夜鉄道, TW 御鐵 xác nhận) 9, おひとよ 1. 0 dòng flag misalignment; lượt soát 2: 136/136 xác nhận lại, 0 loại bỏ, 0 sửa lại.
- Quyết định trong batch (theo uỷ quyền): 御鉄 → T2; kana オヒトヨ/おひとよ sửa như kanji. TW lược bỏ tên công ty ở 1 dòng (ハチロク04_小畑越え 1902) — JP thắng TW, vẫn sửa.
- Ranh giới: 9 dòng audit-src (old_vn = giá trị audit, 0 dòng moan-src); "tuyến Yui" ở ハチロク08 2828/2868 giữ nguyên chờ T7; 00_Common 0 dòng (đã sửa hết trong audit); không đụng dòng gasp Ư hay dòng "Kh" nào.
- File: `unification/unification-t1-ohito-t2-00-05-REVIEW.md` + `unification-t1-ohito-t2-00-05-wrong.json` (136 mục, kind="terminology", item="T1"/"T2"/"T1+T2").

**Tổng cộng sau đợt này: 2 mục / 226 dòng sai (unification)** (cơ sở 1 mục / 90 dòng + đợt U2a 136 dòng — T2 là mục mới, T1 đã tính ở U1b/U1c nên không cộng thêm mục; đối chiếu ROUTE-UNIFICATION.md 22/11 ~11:15; REBASE bởi parent — snippet gốc ghi cơ sở 0/0 đã cũ vì U1b gộp trong lúc agent chạy)

# Snippet — Unification T1 "Ohimitera" → "Ohitoyo", đợt U1a (00_Common / 01_Hachiroku / 02_Hibiki)

- Đợt U1a, mục T1 (§1): sửa "Ohimitera" → "Ohitoyo" ở 3 folder CSV3 00_Common / 01_Hachiroku / 02_Hibiki.
- Số dòng sửa: **221 dòng** (01_Hachiroku 45 · 02_Hibiki 176 · 00_Common 0), tổng 240 lần xuất hiện; 25 file.
- 00_Common 0 dòng: mọi dòng "Ohimitera" ở folder này đã sửa trong audit (riêng 共通14_負債 30 dòng).
- JP xác nhận 御一夜 ở cả 221/221 dòng; 0 dòng bị flag (không misalignment).
- 90 dòng "Ohimitera" còn lại của T1 thuộc các batch song song (U1b 03–06: 52 dòng, đã gộp; U1c 07–11: 38 dòng, đang chạy); sau cả ba đợt T1-Ohimitera còn 0 dòng.
- Chi tiết: `unification-t1-ohimitera-00-02-REVIEW.md` · fix list: `unification-t1-ohimitera-00-02-wrong.json`.

**Tổng cộng sau đợt này: 2 mục / 447 dòng sai (unification)** (cơ sở 2 mục / 226 dòng + đợt U1a 221 dòng — cùng mục T1 đã tính ở U1b/U1c nên không cộng thêm mục; REBASE bởi parent — snippet gốc ghi cơ sở 1/52 đã cũ vì U1c/U2a gộp trong lúc agent chạy; file `file` trong JSON đã chuẩn hoá từ stem sang basename đầy đủ `.txt.toml`)

# Snippet — Unification U10: §6 file-specific DECIDED (không đại từ)

- F1 ハチロク06_のぞみ 1660: 博太 "Hakuta" → "Hakata" (TW 博多). 1 dòng.
- F2 日々姫10 2464: VN 2 dòng "Vâng!" → đúng 1 dòng (JP 「うんっ！」 1 dòng). 1 dòng.
- F4 仲国05: 1956 + 2254 thêm Ư (っ trên từ âm thanh ああ/はう); 1926 "toa thứ hai từ dưới đếm lên" → "toa thứ hai tính từ cuối đoàn"; 3303 とっ "(Phịch)" → "(Cộp)"; 3280 giữ "(Phịch)". 4 dòng.
- F6 ふかみh2 1513: "Đầu ngón tay em ấy" → "Đầu ngón tay tôi" (ngón tay của Soutetsu). 1 dòng.
- F7 ふかみh2 1096: "Migitaichi" → "Migita Ichi" (ruby みぎたいち). 1 dòng.
- F8 仲国06 1412: "Bảo tồn" → "Nhân giống" (ruby はんしょく = 繁殖). 1 dòng.
- F9 真闇02 2793: SFX "Phụt" → "Kéo" (TW 拉). 1 dòng.
- F10 凪ふかみ01_流れ 1691: "mình" → "tôi" (nói thành tiếng với Hachiroku; dòng này CSV3 thiếu, lấy từ TOML). 1 dòng.
- F11 日々姫02_日々姫の日々 1906/2325: khôi phục "nuôi" (đảo ngược 2 fix audit: "anh trai nuôi", "em gái nuôi"). 2 dòng.
- F12 lr_日々姫真闇h1 2003/2005/2082: "cô em gái" → "cô em gái nuôi". 3 dòng.
- F13 ポーレット14 2402: "Là em gái." → "Là em gái nuôi." 1 dòng.
- F15 日々姫h5 1189: bỏ "đã bao phủ" bịa thêm, diễn cụt theo JP. 1 dòng.
- F26 凪ふかみ07 2209/2212/2213/2215/2218: Fukami tự xưng → "tớ" (2208 đã "tớ"; 2210/2211/2214 không tồn tại). 5 dòng.
- F28 凪ふかみ03 2058: "trưởng tàu thay thế" (audit) → "trưởng tàu đại diện". 1 dòng.
- F29 ふかみh1 979/1043: hủy fix audit, giữ "Kh"/"kh" (quy tắc "Kh" đã khóa). 2 dòng.
- F36 [characters]/[character_subs] 'Olive' → "Olivy": ハチロク15b 1908/2063, グランドリライト09 2180/2466, ハチロク02 2823/3034 (list ghi nhầm 2823/3034 cho Grand 09 — thực tế thuộc ハチロク02). 6 dòng.
- Đã kiểm chứng, giữ nguyên, không dòng: F3 (2595/2715 "chị"), F5 (1654/1850), F14 (3777 đã đúng trong audit), F16 (1145/1234), F25 (1563 "Shiro" vs 1907 "D60 46"), F27 (2201), F31 (1264 "Nukyu", 1154 "Po"), F32 (1493 "em"), F33 (1452/1547/1544), F34 (凪h2 2500 "Nyuuuuuuuuuu" 10u — đếm máy: JP 9 âm う/ぅ + 1 = 10, đúng), F35 (2976 đã đúng trong audit — "Minh Quốc"), F37 (20 dòng ハチロク09_もくもくオリヴィ đã đúng trong audit), F38 (key 1293 không tồn tại — số dòng ROUTE-AUDIT.md bị nhầm thành key; mẫu 2459 "tôi" đúng).
- Lượt soát 2: 32/32 tái kiểm chứng, 0 loại, 0 sửa. Khối TOML 17 file / 32 key parse-verified.

**Tổng cộng sau đợt này: 18 mục / 479 dòng sai (unification)** (cơ sở 2 mục / 447 dòng + 16 mục / 32 dòng đợt U10 — REBASE bởi parent: U1a (221 dòng) gộp trước nên cơ sở tăng từ 2/226 lên 2/447; 0 key trùng với các file U1/U2 đã gộp; F10 1691 đã sửa theo CSV3 — xem ROUTE-UNIFICATION.md)

- U1a (22/11 ~11:20): JSON `file` dùng stem (không `.txt.toml`) — coordinator chuẩn hoá cơ học (stem + `.txt.toml`, mỗi stem khớp đúng 1 basename CSV3 trong 00–02) rồi kiểm chứng lại 0 lỗi. T1-Ohimitera HOÀN TẤT project-wide: 52 + 38 + 221 = 311 dòng (khớp recount, không phải 333 của §0).
- U10 (22/11 ~11:20): F10 1691 — worker ghi nhầm "CSV3 thiếu dòng"; thực tế dòng CÓ trong CSV3 (07_Nagi_Fukami, 1 dòng, không dual-set). Coordinator sửa JSON theo CSV3: TW điền từ CSV3, old_vn/fix giữ nguyên `\n` (không dùng bản TOML-2 đã flatten `\n` thành khoảng trắng); REVIEW sửa theo (mục F10 + block TOML + ghi chú second-pass). F36: 6 dòng [characters]/[character_subs] 'Olive'→"Olivy" đã kiểm chứng trực tiếp từ TOML-2 (Grand 09 có ở cả 07_Nagi_Fukami + 09_Grand — duplicate group, fix phủ cả 2 bản). List errors: F36 ghi "Grand 09 (2823/3034)" sai file — 2823/3034 là của ハチロク02 (Grand 09 thật là 2180/2466); F38 key 1293 KHÔNG tồn tại (số dòng ROUTE-AUDIT.md bị nhầm thành key; nội dung Soutetsu "tôi" với Olivy đã kiểm chứng qua key mẫu 2459, không có dòng).
- QUY TẮC REBUILD (22/11 ~11:20): Grand 01 2181 xuất hiện ở cả U1c (T1) và U6 (P14, đang chạy) — fix của U6 đã BAO GỒM fix U1c (old_vn của U6 = fix của U1c). Rebuild PHẢI áp dụng các fix list unification theo THỨ TỰ GỘP (batch sau ghi đè batch trước trên cùng (file,key)).
- CÒN LẠI (U2c, sắp spawn): các dòng chứa "Đường sắt Ohito" trần còn sót sau U1/U2a ở folders 00–05 — ハチロク01 2467, ハチロク12 1900/2089, 日々姫08 3719 (U1a ghi chú), + Mayami h3 2524 (U1b ghi chú). Các dòng này chứa CẢ "Ohimitera" nên bị loại khỏi U2a; U1 chỉ sửa phần Ohimitera.

# Snippet — Unification batch U6 (§2 Paulette pronouns: P2 + P14 + O1)

- U6 / §2 P2 (quyết 19/11, Hieu): Soutetsu → Paulette "cô" → "em" — **99 dòng** trong 27 file (P09–12: 42; P01–08: 16; P-h7: 3; Common 14: 1; Hachiroku: 13; Hibiki: 9; Grand 04/05: 14; Kisaki 03: 1). Đã đọc kiểm chứng từng dòng kèm 3–5 dòng kề (602 dòng ứng viên "cô" của Soutetsu đã soát; 502 dòng giữ có lý do — xem REVIEW §3).
- U6 / §2 P14 (khóa B4): Paulette → Soutetsu "cậu (Soutetsu)" → "anh Soutetsu" — **6 dòng**: 稀咲03 2138; Grand 01 2756, 2181; P16 2008, 2015, 2016 (tên trần → "anh Soutetsu"). 9 dòng ứng viên khác đã sửa trong audit (kiểm chứng, không sửa trùng); Grand 01 2468/2557 giữ (ngôi ba, xem REVIEW §2); Grand 08 1702 không tồn tại dòng Paulette (list ghi nhầm).
- U6 / §7 O1 (QUYẾT theo ủy quyền Hieu): Paulette 06 key 2047 "Cô thấy sao, Paulette" → **"Em thấy sao, Paulette"** — thống nhất "em" cho MỌI ngữ cảnh, không ngoại lệ công việc (bằng chứng: "cô" xuất hiện cả trong cảnh thân mật P10; cùng mẫu câu 稀咲03 2006 trong họp đã về "em"; P13–16 dùng "em" cả khi làm việc, 0 dòng "cô"). **1 dòng.**
- Lượt soát 2: **106/106 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 30 file / 106 key parse-verified.
- **Tổng cộng đợt U6: 3 mục mới (P2, P14, O1) / 106 dòng.**
- **Tổng cộng sau đợt này: 21 mục / 585 dòng sai (unification)** (cơ sở 18 mục / 479 dòng + đợt U6 3 mục / 106 dòng — REBASE bởi parent: U1a (221) + U10 (32) gộp sau khi agent ghi snippet; 1 key trùng U1c (Grand 01 2181, fix U6 đã bao gồm fix U1c — áp dụng theo thứ tự gộp).
- Trùng lặp: 0 key trùng với các file U1/U2 đã gộp, NGOẠI TRỪ Grand 01 key 2181 — đã nằm trong U1c (sửa "Ohitera"→"Ohitoyo"); đợt này sửa "cậu Soutetsu"→"anh Soutetsu" trên cùng dòng, `old_vn` đã lấy giá trị sau U1c — hai đợt cộng dồn, không đè nhau.
- Nợ coordinator: mục mới cho Soutetsu→Hachiroku "cô" còn lại (27 dòng, xem REVIEW §3a/§5); Grand 01 2756/2181 sửa theo list/task (sau B4) trái với quy ước "giữ cả 4" của audit Grand 01 trước B4 (xem REVIEW §2).
- File: `unification/unification-s2-paulette-pronouns-REVIEW.md`, `unification-s2-paulette-pronouns-wrong.json` (106 dòng).


- E1 DECIDED by coordinator 22/11 ~11:25 (per Hieu's delegation; evidence read from investigation-open-terminology-t56-t66-REPORT.md):
  - T56 仲国 → "Trung Quốc" (124 rows: 72 "Trọng Quốc" + 48 "Zhongguo" + 2 "Nakakuni"/"Chukoku" + 2 "tiếng Zhongguo"→"tiếng Trung"). Evidence: Grand08 1722 audit precedent (changed 冥国→"Minh Quốc" while KEEPING 仲国→"Trung Quốc" in the same line, ×5 lines) + ROUTE-AUDIT convention + JP itself writes 中国 for the same country + majority.
  - T57 詠国 → "Anh Quốc" standalone (5 rows: 1848, 1529, 1833, 2533, 3529); KEEP "Anh" in compounds (8 rows); KEEP exceptions 真闇03 1687 (5-country parallel list) + ハチロク09 2102 (katakana pair with Minh Quốc).
  - T58 次元流 → "Thị Hiện Lưu" (3 rows: 凪ふかみ02 2280/2377/3109). Evidence: TW 示現流 ×3 + real Jigen-ryū (first-strike school, matches 2377's definition) + furigana じげん pun.
  - T59 キルクイティウム → "Quirquitium" (1 row: 日々姫10 2458). 5–1 majority + LOGIC P.13.
  - T60 頭取 → "Tổng giám đốc" (27 rows). Evidence: JP 頭取 = bank president (operating head), TW 行長 ×29; 会長 already "Chủ tịch" and 社長 already "giám đốc" — both would collide if 頭取 took either. Formal intro (Common 11) already uses "tổng giám đốc". Flag: most contestable call — fallback "Chủ tịch" (13 rows) recorded if Hieu prefers it.
  - T61 持株会社 → "công ty holding" (7 rows). "Công ty cổ phần" = 株式会社 (wrong concept); audit ハチロク12 already applied "công ty holding" in 3 rows.
  - T62 民由連 → KEEP "Đảng Dân Do" (0 rows). JP 民由 vs TW 民友 (homophone error); JP wins.
  - T63 帝有鉄道 → "Đường sắt Đế quốc Hinomoto" (4 rows: 1789, 60, 2082, 2248); 鉄道帝有法 (key 60) → "Đạo luật Đường sắt Đế quốc". Evidence: locked 帝鉄 full form + audit precedent Grand10 1134.
  - T64 冥語 → KEEP "tiếng Minh Quốc" (0 rows; already applied in audit ハチロク05 3512).
  - T65 橙汁 → KEEP-VARIANT (0 rows): "Trừng trấp" at 仲国01 1828/2089 (joke rows about the packaging), "nước cam" at 仲国08 2054 (plain request).
  - T66 九国 → "chín tỉnh" (2 rows: グランドリライト07_真闇 2545/2546).
  - E1 total: 173 rows. Cross-item flags for later batches: lr_日々姫ふかみh1 1689 still has old "Ohimitera" (T1 — check U1a/U1c coverage); 仲国03 2082 second half 帝鉄→"Đường sắt Hoàng gia" (banned form — T3 scope, VERIFY U3's T3 enumeration catches it; else U15); 真闇03 1687 five-country list is a future joint decision; ハチロク12 2381 audit fix lost a `\n` (TOML-2 flatten — check at rebuild).
- U6 flags (22/11 ~11:25): Grand 08 key 1702 does NOT exist as a Paulette row (Kisaki speaking — P4 territory; list misattribution). Soutetsu→Hachiroku "cô" rows (27) have NO list item — needs a NEW item (U14/U15), not silently fixed. Common 05 2551/2721/2421/2275 KEPT (Paulette's deliberate くん→さん self-correction). Grand 01 2756/2181 fixed per post-B4 list (audit had kept all four "cậu Soutetsu" as third-person; 2468/2557 kept as third-person — noted in case Hieu wants all four unified).


- F1 DECIDED by coordinator 22/11 ~11:30 (per Hieu's delegation; evidence read from investigation-open-moan-questions-REPORT.md):
  - M7 くっ: H-scene DIALOGUE token → "Ku" (51 deliberate moan-pass changes vs 6; h6 §3c: "Hự" loses the k). KEEP "Hự" in 4 convention files (lr_ふかみh2, 日々姫h1, lrれいな追加h, ハチロクh2 — 12 rows). 5 lone "Hự" rows → "Ku" (凪ふかみh1 1232, lr_ふかみh1 1469, lr_凪h1 1190, ポーレットh6 851, 日々姫h4 1028). Descriptive （ ） くっ → "Ư". Non-H dialogue keeps "Ư". KEEP "kư" (lr_稀咲h1) + verb clusters "Ngoáy"/"Thúc" (incl. ハチロクh3 1815).
  - M8 や/やっ: trigger = FOLLOWING token (words/refusal → "Á"; moan-token chain → "Ya/Yaa"). Drop bare "A" for や (64 rows → "Ya"/"Á"). KEEP 991 "Yaa!" + 1334 "Ya!?". Fix lr_凪h2 1203 last token "áa!" → "Áa!" (capitalization).
  - M9 ふっ: NO project-wide unification — keep per-file. Only unify WITHIN files: 真闇h3 "phù"→"Phư" (3 rows); ハチロクh9/lr_ニイロクh/lr_真闇h1 mixed files per majority. (~3–6 rows)
  - M10 ふぇ/ふえ: moan-chain token → "Fue"; standalone surprise interjection (TW 哎/咦) → "Hể?" (6 rows: 凪h1 1090, ふかみh1 993, れいなh3 1026, れいなh4 1897, lr_稀咲h1 992 — 992 OVERTURNS a moan fix, medium confidence, context = denial sentence like 1091); lengthened → keep "Phuê…"; reina-h3 1133 KEEPS "Hả?" (trailing questioning gasp, TW omits it).
  - M11 ふや: H-scene → romaji "Fuya" (~16 rows, OVERTURNS audit locks — justified: romaji fallback 21/11 + moan-pass practice + 35-vs-14 majority); ふやん→"Fuyan"; non-H keeps "phuya" per locked fa/fu rule.
  - M14 （ ） SFX: keep per-file system (romaji vs VN verb); UNIFY COUNTING: total stretch letters = 1 + JP う/ぅ/ー count. Fix ~20 miscounted rows (listed) + stretch-letter type (lr_日々姫h2 1679/1681: stretch the VOWEL, not t) + add stretch to ~122 lost-length rows (review each — rows using a "long" word instead, e.g. ハチロクh7 1840 "Liếm dài", KEEP). Biggest batch — machine counting per token required.
  - M15 ん+consonant: H-scene → romaji Nkyu/Nku/Na/Nfu/Ne/Nhyu (~11 rows: 日々姫h4 1075 "ưm a!"→"Na!", 真闇h1 1080 "ưm phư"→"Nfu", ハチロクh7/h8 split forms → romaji ×5, lr真闇追加h 1097 "ưm ku"→"Nku", lr_稀咲h1 1162 → "Nu!" (resolves F5), 真闇h3 2323/2328 "ưn"→"ưm"). Bare ん(っ) → "ưm"; んん → "nn"/"mm" (already correct); ポーレットh4 878 ぅんっ→"ưn" KEEP.
  - M19 じゅぶっ: keep per-file; chain rule (thrust→"Phập!", mouth→"Chu mút", romaji-system→"Jubu") only as tie-breaker; ハチロクh3's 6 rows already comply (0 changes); 3 rows to re-check (lr_れいなh1 1896/1867, lr_ハチロクh3 1935).
  - M68 れろ: short → "liếm"; long (≥3) → romaji "Rero…" — Group 1 (4 rows, real loss: ハチロクh8 841, 日々姫h3 1857, れいなh2 1084, れいなh2 1114) + Group 2 (~10 rows, already render length via m-stretch/"dài" — CONVERT to romaji for uniformity, coordinator decision) + lr_日々姫ふかみh1 1461 normalize "rê roooo"→"Reroooo" + 凪h2 2546 "Ngoáyyyyyy"→romaji. "rộp" (14 rows) UNTOUCHED — waits for T77 (Hieu).
  - M70 きゅ: do NOT force long→romaji project-wide; per-file system (romaji-system files: short→meaning, long ≥3→romaji; VN-verb files: keep meaning + fix counts via M14); 1 row to re-check (真闇h2 1842, mixed in one row).
  - F1 list corrections (§0, to fix in UNIFICATION-LIST.md, not followed blindly): 6 wrong-file citations (M7 凪h2 1195→lr_ふかみh2; れいなh1 1225→lr_れいなh1; M8 lr_ふかみh2→lr_凪h2; M15 ハチロクh9 2323/2328→真闇h3; 凪ふかみh1 F5 1061→れいなh3 1061; M10 凪ふかみ01 1547→凪ふかみ01_流れ 1547); moan-h8 2187 precedent DOES exist (ポーレットh8 2187, startled やっ→"Á"); ROUTE-MOANS.md lr_ニイロクh F1 is a copy error (flag belongs to lr_稀咲h1 991/992); ふかみh1 967 "Hyaaann" CORRECT (3a+2n); "33 rows んっ→'ưn'" is a polluted count (real: 8 standalone, 2 bare); audit-obasan-wrong.json (255) has no fixes (already known — excluded from coordinator's maps).

# Snippet — Unification U2c: §1 T1/T2 "Ohito" leftovers (folders 00–05)

- Đợt U2c: mục §1 T1 (DECIDED 19/11, Hieu) + T2 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền) — dạng cũ "Ohito" / "Đường sắt Ohito" còn sót trong 6 folder 00/01/02/03/04/05 sau các đợt U1a/U1b/U1c/U2a: **5 dòng sửa, 4 file** (ハチロク01 2467, ハチロク12 1900/2089, 日々姫08 3719, 真闇h3 2524). Cả 5 đều là T2 ("Đường sắt Ohito" → "Đường sắt Ohitoyo"); 0 dòng T1 trần, 0 dòng T1+T2. Cả 5 dòng đều chứa cả "Ohimitera" lẫn "Ohito" nên U2a đã loại, còn U1 chỉ sửa phần "Ohimitera".
- Cả 5 dòng đều đọc JP (+TW) và xác nhận JP chứa 御一夜鉄道; TW đồng ý 5/5. 0 dòng flag misalignment; lượt soát 2: 5/5 xác nhận lại, 0 loại bỏ, 0 sửa lại. old_vn = fix U1a (4 dòng) / U1b (真闇h3 2524); kiểm chứng chéo TOML-2: 5/5 (sau khi quy đổi Ohimitera→Ohitoyo + dẹp `\\n`).
- Ranh giới: "(Yui)" ở 日々姫08 3719 (JP （湯医）) thuộc mục T7, không đụng; 00_Common / 03_Paulette / 04_Reina: 0 dòng. Không đụng dòng gasp Ư hay dòng "Kh" nào; 0 lần "Ohito" trong gloss %l.
- Quét toàn bộ 00–05: CSV3 VN có "Ohito" trần trong 253 dòng; 248 dòng đã đúng ở giá trị hiện tại (135 qua fix unification, 113 qua fix audit), chỉ 5 dòng còn sót. Lưu ý phương pháp: giá trị hiện tại đúng là unification (đã gộp) > moan > audit > CSV3 theo QUY TẮC REBUILD — thứ tự moan > audit > unification sẽ cho thừa 9 dòng đã sửa xong trong U2a (ハチロク04 1823/2112/1855/1920, ハチロク05 2960, ハチロク15b 1637, 日々姫16 2107, ポーレット03 1750, ハチロク12 2565), đã kiểm chứng từng dòng và không đưa vào đợt này.
- File: `unification/unification-t1-ohito-leftovers-00-05-REVIEW.md` + `unification-t1-ohito-leftovers-00-05-wrong.json` (5 mục, kind="terminology", item="T2").

**Tổng cộng sau đợt này: 21 mục / 590 dòng sai (unification)** (cơ sở 21 mục / 585 dòng + đợt U2c 5 dòng — T1 và T2 đều đã tính nên không cộng thêm mục; đối chiếu ROUTE-UNIFICATION.md 22/11 ~11:25, lúc U6 vừa gộp)


- PRECEDENCE CORRECTION (22/11 ~11:35, U2c worker found, coordinator CONFIRMED): current-value order is **unification (merged, in merge order) > moan > audit > CSV3** — NOT moan > audit > unification as the original brief stated. Proof: U2c's old_vn for 3719 = U1a's merged fix; using the old order yields 14 false candidates vs the correct 5 (9 rows already fixed by U2a). All future verifications must load ONLY merged unification JSONs (in-progress worker files must NOT be in the map — U4's unmerged file briefly polluted a check with its "(Yunoi)" value for 3719).
- OVERLAP WARNING (22/11 ~11:35): 日々姫08 3719 is in BOTH U2c (merged: "Đường sắt Ohito"→"Đường sắt Ohitoyo", keeps "(Yui)") and U4 (running: "(Yui)"→"(Yunoi)", keeps "Đường sắt Ohito"). Neither fix contains the other's change — when U4 completes, its 3719 fix MUST be corrected to the combined value 'Đoạn (Yunoi) - Ohitoyo - Hayato là của Đường sắt Ohitoyo.\n…' before merging, or the merge-order overwrite will regress one change. Same check required for every U4 row overlapping a merged batch.
- U2c side notes: audit-obasan-wrong.json superseded by audit-paulette03-obasan-wrong.json (its 4 Ohito rows already fixed there); 2 audit entries have fix: null (凪ふかみ08a 2426, ポーレット13 1357 — known uncertain rows; treat as no-fix; verification maps must skip fix:null).

# Snippet — Unification U2b: §1 T1 "Ohito" → "Ohitoyo" + T2 "Đường sắt Ohito" → "Đường sắt Ohitoyo" (folders 06–11)

- Đợt U2b: mục §1 T1 (DECIDED 19/11, Hieu) + T2 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền) — dạng cũ "Ohito" (trừ "Ohimitera", thuộc batch U1) trong 6 folder 06/07/08/09/10/11: **72 dòng sửa, 12 file** (Kisaki 38, Nagi-Fukami 19, Grand 15; Niiroku 0, Chikuni 0, Other 0).
- Phân loại: T2 "Đường sắt Ohito" → "Đường sắt Ohitoyo": 29 dòng; T1 trần "Ohito" → "Ohitoyo": 40 dòng; cả hai dạng trong một dòng (T1+T2): 3 dòng (凪ふかみ08c 2199, グランドリライト02 2575/2319). 76 lần xuất hiện dạng cũ.
- Cả 72 dòng đều đọc JP (+TW) và xác nhận JP chứa thuật ngữ: 御一夜鉄道 32, 御一夜 trần 40; TW đồng ý 72/72. 0 dòng flag misalignment; lượt soát 2: 72/72 xác nhận lại, 0 loại bỏ, 0 sửa lại.
- Quyết định trong batch (theo uỷ quyền): "Thành phố Đường sắt Ohito" ở 凪ふかみ08c 2420/2341 xếp T1 (JP là 鉄道の町・御一夜, không phải tên công ty 御一夜鉄道 — chuỗi fix ra giống hệt nhau).
- Ranh giới: 17 dòng audit-src (old_vn = giá trị audit, 0 dòng moan-src); 42 dòng "Ohimitera" trong 06–11 đã loại (thuộc U1b/U1c, 0 dòng chứa thêm "Ohito" trần); "Yui" ở Grand06 2146, "ông nội" Seki ở Grand06 2159 và "hợp đồng Maitetsu" ở 凪h2 1766 giữ nguyên chờ batch khác; 0 dòng "Ohito" trong gloss %l; không đụng dòng gasp Ư hay dòng "Kh" nào. Cờ F-T1T2-1: 5 dòng hai-dạng ("Ohimitera" + "Ohito") ở 01/02/05 còn sót sau U2a+U2b, chờ batch leftovers.
- File: `unification/unification-t1-ohito-t2-06-11-REVIEW.md` + `unification-t1-ohito-t2-06-11-wrong.json` (72 mục, kind="terminology", item="T1"/"T2"/"T1+T2").

**Tổng cộng sau đợt này: 21 mục / 662 dòng sai (unification)** (cơ sở 21 mục / 590 dòng + đợt U2b 72 dòng — T1/T2 đã tính nên không cộng thêm mục; REBASE bởi parent — snippet gốc ghi cơ sở 2/226 đã cũ vì U1a/U10/U6/U2c gộp trong lúc agent chạy; T1+T2 HOÀN TẤT project-wide: U2a 136 + U2b 72 + U2c 5 = 213)

- U2b (22/11 ~11:40): decision D1 — "Thành phố Đường sắt Ohito" (凪ふかみ08c 2420/2341) classified T1, not T2 (JP is 鉄道の町・御一夜, town epithet, not the company 御一夜鉄道; fix string identical either way). Flag F-T1T2-1 (5 leftover rows) RESOLVED by U2c (same 5 rows). Worker used the OLD old_vn order (moan>audit>CSV3) — no errors resulted (0 overlap with merged batches, verified by coordinator with the corrected order).


# Snippet — Unification U9: §2 P15 + P7 + §7 O61 (Munakata "tao" · Kisaki "anh trai của Hibiki")

- Đợt U9 / §2 P15 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền): Munakata (宗方甚六) 俺/オレ → "tao" — **18 dòng sửa, 5 file** (ハチロク04: 3, ハチロク12: 6, ハチロク15a: 3, ハチロク15b: 2, ハチロク16: 4; 28 lần thay "tôi"→"tao"). Nhiều hơn 1 dòng so với list ghi (17): bắt thêm ハチロク16 1884 「おれはマスターではない」 (おれ hiragana = 俺). お前 không đụng ("nhóc"/"cô"/"cậu" giữ nguyên).
- Đợt U9 / §7 O61 (QUYẾT trong đợt này theo uỷ quyền Hieu, không park): Munakata "tôi" 6 dòng không có 俺 tường minh trong **ハチロク16_春** (list ghi nhầm file là ハチロク10_炙り出し — file đó không có các key này) — **"tao" cho cả 6 dòng** (1297/1306/1637/1903/2050/2070). Bằng chứng: cùng file/cảnh với 4 dòng 俺 tường minh (1301/1884/1910/2025) xen kẽ — 1297/1306 kẹp sát 1301, 1903 cách 1910 có 7 key, 2050/2070 cùng mạch trả nợ Olivy với 2025; TW xác nhận ngôi thứ nhất (我) ở cả 6 dòng; Munakata dùng 俺 cả trong câu trang trọng (ハチロク12 1708) nên tính trang trọng không đổi được đại từ.
- Đợt U9 / §2 P7 (DECIDED 22/11 ~04:03, Hieu): Kisaki 日々姫さんのお兄さん → "anh trai của Hibiki" — **0 dòng sửa**: chỉ 2 dòng toàn dự án (共通10 2449/2472) và cả hai đã đúng sẵn trong CSV3 + TOML-2; 3 dòng liên quan (2191/2111/2141) cũng đã đúng; không tồn tại dòng nào dịch お兄さん thành "chị Hibiki".
- Lượt soát 2: **24/24 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 5 file / 24 key parse-verified (trích từ REVIEW, khớp JSON tuyệt đối). old_vn khớp map giá trị hiện tại (unification-đã-gộp > moan > audit > CSV3): 22 dòng csv3, 2 dòng fix U2a (ハチロク16 1884/2070 — giữ nguyên "Đường sắt Ohitoyo").
- Cờ cho điều phối: còn 55 dòng Munakata "tôi" không có 俺 ở các file khác (cần mục riêng nếu muốn thống nhất toàn bộ — trong đó có dòng JP dùng 私 trang trọng, vd. ハチロク12 1147); list cần hiệu chỉnh: P15 thực tế 18 dòng (không phải 17), P15 ×4 + O61 thuộc ハチロク16_春 (không phải ハチロク10_炙り出し).
- File: `unification/unification-s2-munakata-kisaki-REVIEW.md` + `unification/unification-s2-munakata-kisaki-wrong.json` (24 mục, kind="pronoun", item="P15"/"O61").

**Tổng cộng sau đợt này: 24 mục / 686 dòng sai (unification)** (cơ sở 21 mục / 662 dòng + đợt U9 3 mục mới (P15, P7, O61) / 24 dòng — P7 đóng góp 0 dòng; đối chiếu ROUTE-UNIFICATION.md trực tiếp lúc ghi snippet, sau khi U2b gộp: cơ sở 21/590 lúc spawn đã cũ)


# Snippet — Unification batch U4: §1 set-3 terminology (T6, T7, T15, T16, T41, T45, T47, T54, T55, T11, T12, T19, T20)

- Đợt U4: 11 mục thuật ngữ §1 set-3 (tất cả DECIDED — áp trực tiếp): **193 dòng sửa, 56 file**.
  - T6 日ノ本 "Hinamoto" → "Hinomoto": **34 dòng**.
  - T7 湯医 / 湯医線 "Yui" → "Yunoi": **107 dòng** (111 lần xuất hiện; 4 dòng ×2: 日々姫08 3132, グランドリライト04 2205, ポーレット08 2363, グランドリライト11 3916). Gồm 9 dòng JP kana ユノイ線 và 8 dòng "Học viện Yui" (湯医学園) → "Học viện Yunoi".
  - T15 小畑 "Obata"/"Kobata" → "Okoba": **6 dòng** (5 + 1 dòng hai mục ハチロク15a 1842).
  - T16 駿袋鉄道 "Suntetsu" → "Suntai": **1 dòng** (ポーレット02_解放b寝台 1966, ruby すんたい; TW 駿遠 sai theo JP).
  - T41 "Kiha" → "KiHa" (chính tả chính thức của JR): **18 dòng** (17 + 1 dòng hai mục ハチロク08 2840); 7/18 nằm trong gloss %l.
  - T45 冥国 "Meikoku" → "Minh Quốc": **6 dòng**.
  - T47 マスコン / マスターコントローラー → "điều khiển trung tâm": **5 dòng**.
  - T11 運転体 → "thân vận hành": **11 dòng**. T12 整備体 → "thân bảo trì": **3 dòng** (kiểm kê toàn bộ 86 dòng JP 運転体/整備体/ボディ).
  - T19 乗員 "phi hành đoàn" → "nhân viên tàu": **1 dòng** (日々姫03 2834).
  - T20 Seki "ông nội" → "ông ngoại": **3 dòng** (共通12 2182, ハチロク05 1178, グランドリライト06 2159; CHỈ dòng Seki, kiểm kê toàn bộ 25 dòng "ông nội").
  - T54 回数券 → "vé lượt" / 定期券 → "vé định kỳ": **0 dòng** — đã sửa hết trong audit (3 dòng sleeper P02 + 7 dòng 定期券, kể cả P02 1832 JP kana かいすうけん).
  - T55 仲国06 1412 → "Nhân giống": **0 dòng** — đã sửa trong unification đã gộp (U10/s6, F8).
- Cả 193 dòng đều đọc JP (+TW); 182/193 JP chứa trực tiếp thuật ngữ kanji, 9 dòng T7 JP kana ユノイ (cùng thuật ngữ), 2 trường hợp giải thích riêng (D3: ハチロク01 2828 JP dùng レイナナ, referent vẫn KiHa 07; D4: ハチロク06 2139 JP chỉ còn ruby しゅかんせいぎょき, TW 主控 xác nhận). Lượt soát 2: **193/193 tái kiểm chứng, 0 loại bỏ, 0 sửa lại**. Khối TOML 56 file / 193 khóa parse-verified (chạy lại sau rebase 3719).
- Quyết định trong batch (theo uỷ quyền): D1 — T47 bỏ "bộ" trong "bộ điều khiển trung tâm" (4 dòng: P15 1073/1981, ハチロク06 2139/2763; dạng khóa là trần, tiền lệ ハチロク06 2145); D2 — T11/T12 thống nhất cả biến thể chưa liệt kê ("thân điều khiển" ×5, "cơ thể lái tàu", "thân hình lái tàu", "cơ thể bảo dưỡng", "thân chính bảo dưỡng" — tiền lệ audit れいな01 2218 / ニイロク04 2061).
- Giữ lại: T7 địa danh 由衣 ×2 (ハチロク09 2118 — ngoại lệ đã ghi; ハチロク04 1925 — cùng địa danh, áp cùng ngoại lệ); T6 JP 日ノ本 dạng khác ×7 ("Nippon Sharyo" ×5, "Yamato Nadeshiko" ×2 — T73 OPEN); T11/T12 dương tính giả ×2 (仲国06 2327 "kíp lái" = tổ lái, 日々姫09 1942 整備体験); T19 12 dòng "phi hành đoàn" còn lại thuộc T18 (túi); T20 mục con OPEN (ハチロク09 2027 "bác Seki", 日々姫03 2368/2607, ハチロク07 2588 "các ông của Nagi", 凪ふかみ01 1884, ふかみh1 2368/2607, Grand 08 2010, 日々姫04 2668).
- Rebase chồng lấn (cảnh báo coordinator 22/11 ~11:35): 日々姫08 3719 nằm cả ở U2c (đã gộp) và batch này — old_vn đã sửa về giá trị U2c, fix = giá trị gộp "(Yunoi) … Đường sắt Ohitoyo". Hai dòng chồng U2b (Grand06 2146/2159) đã khớp giá trị gộp từ đầu. Thứ tự giá trị hiện tại đã sửa theo coordinator: **unification-đã-gộp > moan > audit > CSV3** (brief gốc viết ngược; chỉ 3719 trong batch này bị ảnh hưởng).
- Chồng lấn với file worker ĐANG CHẠY (chưa gộp — coordinator xử lý thứ tự gộp): set2 — Grand06 3472, P03 1723, ハチロク13 2555, ハチロク12 2508; T56–T66 — ハチロク10 1529.
- File: `unification/unification-t1-set3-REVIEW.md` + `unification-t1-set3-wrong.json` (193 mục, kind="terminology", item="T6"/"T7"/"T15"/"T16"/"T41"/"T45"/"T47"/"T11"/"T12"/"T19"/"T20"/"T7+T15"/"T7+T41").

**Tổng cộng sau đợt này: 35 mục / 879 dòng sai (unification)** (cơ sở 24 mục / 686 dòng + đợt U4 11 mục mới / 193 dòng — REBASE bởi coordinator: U9 (3 mục / 24 dòng) gộp 22/11 ~11:45 sau khi agent ghi snippet; cơ sở 21/662 lúc spawn đã cũ)


# Snippet — Unification batch U3: §1 set-2 terminology (T3, T10, T13, T14, T17, T18)

- Đợt U3: 6 mục thuật ngữ §1 set-2 (tất cả DECIDED — áp trực tiếp): **240 dòng sửa, 69 file**.
  - T3 帝鉄 "Đường sắt Hoàng gia" → "Đường sắt Teitetsu": **55 dòng** (50 dạng trần + 5 gloss %l "Đường sắt Đế quốc" — T3b: れいな02 63, ハチロク09 2792, 日々姫01 2097, 日々姫14 1276, 真闇01 1621; dạng đầy đủ chỉ giữ ở tooltip lần đầu 共通01 1335, thuộc T4).
  - T10 電車姫 → "Công chúa Tàu điện": **28 dòng** (16 "Densha Hime", 10 "Denshahime", 1 "Công chúa Xe điện" Grand01 2724, 1 "công chúa Densha" lrれいな追加03 1170).
  - T13 宮司 → "đền chủ": **38 dòng** (18 "Akai-guji", 7 "Guuji" gồm 2 "Akai Guuji" + 5 "ông Guuji", 8 "thầy cúng", 5 "cha xứ"); 3 dòng trong đó mang cả T18 (グランド06 3242/3472/3540) — tính 1 lần trong tổng 240.
  - T14 Migita (xưởng rượu) → "Migita Ichi": **21 dòng** (gồm 3 dòng "Migitai" đã QUYẾT theo ủy quyền O62: 凪ふかみ03 1071/1429/2525 — "Migitai" là đọc sai của 右田一; cộng 3 dòng JP 右田の蔵/右田の酒蔵 không có 一, cùng thực thể).
  - T17 術仙 "Jutsu-sen" → "Jutsusen": **85 dòng** (71 "Jutsu-sen" gồm 61 fix audit + 2 fix unification đã gộp, 13 "Jussen", 1 dòng khôi phục ポーレット07 2311 — fix audit đã cắt cụt dòng). Bẫy T17 lớn hơn list ước lượng rất nhiều.
  - T18 乗務鞄/運転鞄/運転士鞄 → "túi công tác": **16 dòng** (11 "túi phi hành đoàn", 1 gloss "Túi phi hành đoàn" đầu câu 共通08 1485, 4 "cặp lái tàu" trong gloss %l); 3 dòng mang cả T13 (xem trên).
- Cả 240 dòng đều đọc JP (+TW); 0 dòng flag misalignment. Lượt soát 2: **240/240 đối chiếu lại với JP — 237 đúng ngay, 0 loại bỏ, 3 sửa lại** (đều T14: fix viết nhầm "Migita Ichi Ichi" do cặp thay thế áp dụng chồng — ハチロク15a 1835, 真闇01 2366/2444; đã sửa đồng bộ JSON + REVIEW §4 + khối TOML §7, xem REVIEW §6). Khối TOML 69 file / 240 khóa parse-verified bằng tomllib, khớp JSON 240/240.
- Khôi phục 1 lỗi fix audit: ポーレット07_支線 2311 (audit cắt cụt chỉ còn nửa đầu + mất tag %l; fix = toàn bộ giá trị CSV3 với "Ohimitera"→"Ohitoyo" và "Jutsu-sen"→"Jutsusen").
- 5 dòng old_vn lấy từ unification đã gộp (áp dụng thay đổi của đợt này lên trên): ハチロク12 1525, ポーレット04_ヒヤリング 1517, ポーレット09 2129, 日々姫09_run 1906, 日々姫09_静かなる開戦 1690. Theo tiền lệ U6, batch vẫn cộng đủ 240 dòng vào tổng chain.
- Chồng lấn với batch set3/U4 ĐANG CHẠY (chưa gộp — coordinator xử lý thứ tự gộp): **4 key chung, fix BỔ SUNG nhau, không bên nào bao gồm bên kia** — rebuild PHẢI gộp (compose), không được ghi đè nguyên dòng, nếu không sẽ mất fix của một bên: グランド06 3472 (set2: T13+T18; set3: T11 運転体→"thân vận hành"), ハチロク13 2555 (set2: T18; set3: T11), ポーレット03 1723 (set2: T17; set3: T7 "Yui"→"Yunoi"), ハチロク12_再開発 2508 (set2: T17; set3: T7). Set3 đã ghi cùng 4 key này trong snippet của họ.
- Flag cho coordinator (không tự quyết): 帝央機関区 2 dòng (ハチロク04 1802, 仲国05 2032 — chưa có chuẩn); tên công ty 帝国線路合同会社 8 dòng (稀咲03 ×6, 稀咲h3 ×2 — JP không có 帝鉄); các dạng 宮司 "thầy tế" ×14 (P01/P02), "Đại tư tế Akai" ×25 (P10–P13), "ông Akai" ×11 + "ông" ×1 (グランド06 2269) — có thống nhất về "đền chủ" hay không; 2 dòng "Denshahime của Mouri" mà JP chỉ nói 毛利の姫 (日々姫11 1774, 日々姫12 2908); trích dẫn list lỗi thời: "Paulette 02 1525" không tồn tại, ハチロク10 [characters] 2791 / [character_subs] 2789 không tìm thấy trong CSV3 lẫn TOML-2.
- File: `unification/unification-t1-set2-REVIEW.md` + `unification-t1-set2-wrong.json` (240 mục, kind="terminology", item="T3"/"T10"/"T13"/"T14"/"T17"/"T18"/"T13+T18").

**Tổng cộng sau đợt này: 41 mục / 1.115 dòng sai (unification)** (cơ sở 35 mục / 879 dòng + đợt U3 6 mục mới / 236 dòng mới — 4 dòng trùng U4 (Grand06 3472, ハチロク12_再開発 2508, ハチロク13 2555, ポーレット03 1723) đã tính trong U4, fix đã GHÉP bởi coordinator (xem ghi chú điều phối trong REVIEW U3); REBASE bởi coordinator: U9 + U4 gộp sau khi agent ghi snippet; cơ sở 21/662 lúc spawn đã cũ)


# Snippet — Unification U13a: §1 OPEN T56–T66 (T56, T57, T58, T59, T60, T61, T63, T66)

- Đợt U13a: §1 OPEN T56–T66 theo quyết định của coordinator 22/11 ~11:25 (uỷ quyền Hieu), trên báo cáo điều tra E1: **171 dòng sửa, 33 file, 8 mục mới**.
- T56 仲国 → "Trung Quốc": **122 dòng** (72 "Trọng Quốc" + 46 "Zhongguo" tên nước + 2 "tiếng Zhongguo" → "tiếng Trung" + 1 "Nakakuni" + 1 "nước Chukoku" → "Trung Quốc"/"nước Trung Quốc"). Giữ: 76 dòng đã "Trung Quốc" (gồm 4 "tiếng Trung Quốc"), 5 "tiếng Trung", 仲国06 1796 ("trong nước").
- T57 詠国 → "Anh Quốc" (đứng riêng): **5 dòng** (1848 "Vịnh Quốc", 1529/1833/2533 "Eikoku (...)", 3529 "Anh quốc"). Giữ: 8 dòng dạng ghép "Anh" + 2 dòng đã "Anh Quốc" + ngoại lệ 真闇03 1687 (list 5 nước song song) + ハチロク09 2102 (cặp katakana với Minh Quốc).
- T58 次元流 → "Thị Hiện Lưu": **3 dòng** (凪ふかみ02 2280/2377/3109; TW 示現流 ×3, Jigen-ryū thật).
- T59 キルクイティウム → "Quirquitium": **1 dòng** (日々姫10 2458; 5/5 dòng 共通04 đã đúng).
- T60 頭取 → "Tổng giám đốc": **27 dòng** (16 "Chủ tịch" + 11 "Giám đốc"/"giám đốc ngân hàng"; giữ "ngân hàng"/"Ngân hàng Kumamoto"/"Ngân hàng Kumagin" theo dòng; 2 dòng 共通11 đã đúng). 3 dòng chỉ đổi dạng 頭取, giữ 支店長 "giám đốc chi nhánh" (ハチロク14 1731, ポーレット09 2131, 共通14 1551).
- T61 持株会社 → "công ty holding": **7 dòng** (ハチロク09 ×5, ハチロク15 1953, れいな03 1568; 3 dòng ハチロク12 đã đúng).
- T63 帝有鉄道 → "Đường sắt Đế quốc Hinomoto": **4 dòng** (日々姫01 1789, 日々姫02 60 — kèm tên luật "Đạo luật Đường sắt Đế quốc", 仲国03 2082/2248; 1134 đã đúng).
- T66 九国 → "chín tỉnh": **2 dòng** (グランドリライト07_真闇 2545/2546; 4 dòng còn lại đã đúng).
- T62/T64/T65 GIỮ NGUYÊN, 0 dòng (đã kiểm chứng: "Đảng Dân Do", "tiếng Minh Quốc", "Trừng trấp" 1828/2089 + "nước cam" 2054).
- Lượt soát 2: **171/171 tái kiểm chứng, 0 loại, 0 sửa giá trị fix.** Khối TOML 33 file / 171 key parse-verified. Nguồn `old_vn`: 150 CSV3 + 15 audit + 6 unification đã gộp + 0 moan.
- **LỆCH SỐ — coordinator lưu ý (ghi chi tiết ở REVIEW §0):** (1) T56 thực tế **122 dòng, không phải 124** như báo cáo E1 (E1 đếm trùng 2 dòng "tiếng Zhongguo" — chúng đã nằm trong "Zhongguo 48": 仲国02 27 = 26 + 2897, 仲国03 16 = 15 + 2845); tổng đợt này vì vậy là **171 dòng, không phải 173**. (2) **T66 (2 dòng) có trong quyết định coordinator nhưng không có trong bullet của task** — đã áp dụng và tách riêng theo item để loại được nếu muốn; nếu tính đúng 7 mục trong bullet thì đợt này là 7 mục / 169 dòng.
- **REBASE trên 2 batch gộp song song (§0d):** set2 (T3 帝鉄 → "Teitetsu", 240 dòng) và set3 (日ノ本 "Hinamoto" → "Hinomoto", 193 dòng) gộp trong lúc đợt này đang chạy; 5 dòng trùng (file,key) đã rebase `old_vn` lên giá trị sau set2/set3 (1529, 2175, 2082, 2083, 2251) — nhờ vậy cờ F-T63-1 (2082 nửa sau) và F-T57-1 (1529 "Hinamoto") coi như đã xong. Cờ còn mở duy nhất: **F-T56-1 — 仲国08 2823** (JP 日仲, không chứa 仲国; CUR còn "Trọng Quốc" — chờ quyết ở đợt vét U15).
- File: `unification/unification-t1-open-t56-t66-REVIEW.md` + `unification-t1-open-t56-t66-wrong.json` (171 mục, kind="terminology", item="T56"/"T57"/"T58"/"T59"/"T60"/"T61"/"T63"/"T66").

**Tổng cộng sau đợt này: 49 mục / 1.280 dòng sai (unification)** (cơ sở 41 mục / 1.115 dòng + đợt U13a 8 mục mới / 165 dòng mới — 6 dòng trùng đã gộp (U3/U4) không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 21/662 đã cũ vì U9/U4/U3 gộp trong lúc agent chạy; T56 thực 122 dòng, tổng đợt 171 — xem LỆCH SỐ trong snippet).


# Snippet — Unification U5: §1 misc (T8/T9/T25–T28/T50–T53) + §4 G1/G2 gloss sweeps

- Đợt U5: mục §1 misc DECIDED (T8 まいてつ → "chủ tàu", T9 市電 → "tàu điện thành phố", T25 従輪 → "Bánh xe chịu tải", T26 動輪 → "Bánh xe chủ động", T27 タブレット core → "Thẻ bảng (Tablet)", T28 iPad → "máy tính bảng", T50 流 → "Nagare", T51 隈元 → "Kumamoto", T52 帝都 → "Đế đô", T53 運転台 → "buồng lái") + §4 G1 列車 gloss → "đoàn tàu" và G2 機関士 gloss → "lái tàu": **8 mục / 336 dòng sửa, 82 file** (T8 18, T25+T26 3 dòng riêng biệt, T27 90, T51 2, T52 20, G1 121, G2 83). 4 mục kiểm chứng 0 dòng (T9, T28, T50, T53).
- Phân loại: terminology 123, gloss 213. Nguồn old_vn (quy ước rebuild unification-đã-gộp > moan > audit > CSV3): CSV3 207, audit 116, unification-đã-gộp 12, moan 1 (sau khi coordinator GHÉP 6 dòng trùng U3/U4 — xem dưới).
- Phát hiện lớn nhất — T27: census gloss %lタブレット hiện tại: 75 dòng / 80 tag — "máy tính bảng" 63, "Tablet" 9, "thẻ bảng" 6, "Máy tính bảng" 2; "Thẻ bảng (Tablet)" 0 lần. Audit đã đổi hệ thống gloss core từ "thẻ bảng"/"Tablet" (CSV3) sang "máy tính bảng" theo brief cũ — quyết định của Hieu 22/11 ~04:03 lật lại: core KHÔNG BAO GIỜ là "máy tính bảng". 85 dòng gloss về "Thẻ bảng (Tablet)" (74 tag タブレット + 10 tag 操作板 ở ニイロク04 — term tag giữ nguyên, cờ U5-3) + 5 dòng text trần (4 khôi phục CSV3 + 1 sửa device ハチロク12 1594 "Tablet" → "máy tính bảng", TW 平板電腦 quyết định). P04 2076/2642: đọc "tablet của Hibiki" của audit review là SAI — JP 2076 là たぶれっと, core term (cờ U5-4; audit còn thêm %l tag ở 7 dòng JP không có tag).
- G1: 192 dòng có tag %l列車 (197 tag) — "tàu" 85, "đoàn tàu" 67, "chuyến tàu" 26, "Tàu" 8, "Đoàn tàu" 7, "Chuyến tàu" 4; sửa 121. G2: 230 dòng (235 tag) — "lái tàu"/"Lái tàu" 149 đã đúng, "người lái tàu" 42, "thợ lái đầu máy" 16, "nhân viên cơ vụ" 13, "Người lái tàu" 11, "nữ lái tàu" 1; sửa 83. "nhân viên cơ vụ" → "lái tàu" ở cả 13 lần xuất hiện (đều là 機関士 trần). Giữ: 共通04 2651 gloss "Master" (ruby [マスター,2]機関士, cố ý); gloss 運転士 "nhân viên cơ vụ" ở 3 dòng (khác term); 機関助士 "phụ lái tàu" không đụng.
- T8: chỉ sửa dạng danh từ chung; giữ tên chương trình まいてつラジオ (日々姫03 2056/2678) và "hợp đồng Maitetsu" 凪h2 1766 (T74 OPEN). T51: chỉ 2 dòng JP 隈元銀行 ("Kumagin" → "Ngân hàng Kumamoto"); "Kumagin" ĐÚNG cho JP 隈銀 (20 dòng giữ). T52: 53 dòng đã "Đế đô"; sửa 10 "Đế Đô" giữa câu + 6 "Teito" (toàn グランド06_稀咲) + 4 "thủ đô". T50/T53/T9/T28: 0 dòng — đã đúng sẵn (T50: 5 dòng "ông Ryu" ở ハチロク08_教導, không phải 日々姫03 như list ghi — cờ U5-6).
- Ranh giới / cờ: 12 dòng tag %l thiếu `;` đóng (có từ CSV3) — gloss sửa, phần đóng tag GIỮ NGUYÊN, chờ tag sweep đã park (U5-2). 真闇h3 3299 chỉ sửa "Đế Đô"→"Đế đô", để nguyên "Đại học Hoàng gia" (T5 chưa giao — U5-5). U5-1 (G8): Common 08 ×4 về "Thẻ bảng (Tablet)" — nếu Hieu muốn "thẻ bảng" trần thì lật lại. U5-6: list sai 3 chỗ (ハチロク10_炙り出し ×5 không tồn tại; "ông Ryu" sai file; T51 "仲国02 2434" không tồn tại).
- Trùng batch: U9 gộp TRONG LÚC batch chạy (22/11 ~11:45) — ハチロク15a 2031 đã nạp lại map, old_vn = fix U9, fix đợt này = giá trị kết hợp "Dù tao… + gloss lái tàu" (U5-8, không hồi quy). **6 dòng trùng batch ĐÃ GỘP (U3 T10, U4 T7/T11/T12/T41) ĐÃ GHÉP bởi coordinator 22/11 ~12:00 (U5-7): ハチロク04 2464 (G1+T7), ハチロク11 2251 (T27+T10), ハチロク13 2326/2328 (T27+T11), ハチロク13 2336 (T27+T12), ポーレット03 2814 (G2+T41) — old_vn := fix đã gộp, fix := giá trị kết hợp; 4/6 khớp tuyệt đối cờ U5-7, 2/6 (2326, 2814) khớp trừ dấu `;` đóng tag cờ ghi thiếu. U12a (moan-dialogue, 99 dòng) 0 trùng.**
- Lượt soát 2: 336/336 xác nhận lại với JP/TW, 0 loại bỏ, 0 sửa lại; kiểm cơ học độc lập tag-scoped 0 lỗi (mọi tag giữ term + mã màu; mọi gloss đổi nằm trong tập triple đã chốt; 36 dòng text trần diff đều khớp đổi đã chốt). 6 dòng T27 2-tag ban đầu chỉ sửa tag đầu đã bắt và sửa ở bước kiểm chứng trước khi soát 2 (ニイロク04 1918, ハチロク07 1662/2444/3121, ハチロク10 2190, ハチロク16 2307). TOML: 82 khối, 336 khóa, parse OK. 0 dòng chạm token gasp Ư hay "Kh".
- File: `unification/unification-t1-misc-gloss-REVIEW.md` + `unification/unification-t1-misc-gloss-wrong.json` (336 mục, kind="terminology"/"gloss", item="T8"/"T25"/"T26"/"T27"/"T51"/"T52"/"G1"/"G2"/"T25+T26"/"G2+T27").

**Tổng cộng sau đợt này: 57 mục / 1.604 dòng sai (unification)** (cơ sở 49 mục / 1.280 dòng + đợt U5 8 mục mới / 324 dòng mới — 12 dòng trùng đã gộp (6 khớp sẵn + 6 GHÉP) không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 24/686 đã cũ vì U13a gộp trước (49/1.280).


# Snippet — Unification U11a: §3 M1 / M16 / M17 (fa/fu)

- Đợt U11a / §3 M1 (DECIDED 19/11 Hieu, reaffirmed 20/11 ~15:00): dạng khoá fa/fu trong H-scene moan → romaji — **37 dòng sửa, 10 file** (lr_稀咲ポーレットh1: 6, lr追加_みくろ: 18, れいなh1: 6, lr_ポーレットh2: 1, 日々姫h1: 1, ポーレット03: 1, 日々姫07: 1, 日々姫09: 1, 凪ふかみ03: 1, ポーレットh5: 1). Non-H KEEP dạng khoá; 4 dòng non-H bare "Phù" sửa VỀ dạng khoá (Phùa/Phà/Phàa).
- Đợt U11a / §3 M16 (QUYẾT trong đợt này, theo uỷ quyền): Fa/Fua strict theo mora count (ふぁ→Fa, ふあ→Fua, ふぁん→Fan, ふぇ/ふえ→Fue) — **67 dòng sửa**. Token dài kiểm chứng từng mora (1357: 18 a; 1477: 19 a; 1479: 14 a; 1100: 17 a+n; 962: 8 a+n; 2114: 6 a; 1470/819: 5 a+n; 2458: 5 a); token dán 1358 (a:1, u:14, n:2) chỉ bỏ "u" thừa. 3 dòng ふぇ (lr_れいなh1 1179/1199/1236) loại khỏi M16 — thuộc U12a M10.
- Đợt U11a / §3 M17 (QUYẾT trong đợt này, theo uỷ quyền): split-fa "Fu, a" vs "phù——a" — H-scene → romaji split "Fu"+dấu+"a" (giữ dấu theo JP, giữ case token a), non-H KEEP split VN; loại B nối romaji (H) / dạng khoá VN (non-H) — **62 dòng sửa**. "ah" cho あっ/ぁっ giữ nguyên như moan pass.
- Lượt soát 2: **166/166 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 47 file / 166 key parse-verified (trích từ REVIEW, khớp JSON tuyệt đối). old_vn khớp map giá trị hiện tại (unification-đã-gộp > moan > audit > CSV3): 0 dòng trùng 8 batch đã gộp (656 (file,key)); 11 dòng trùng enumeration U12a đã cờ cho coordinator gộp.
- Cờ cho điều phối: 16 dòng ふや (M11) + các dòng ふぇ/ふえ (M10) + ふっ (M9) để U12a; 3 split ぷ để T79; 凪ふかみh2 1271 (split ふう) chờ quyết có mở rộng M17 sang ふう; list §3: M16 thực tế gồm cả token dán/glued (1358) và token dài tách tại っ (891).
- File: `unification/unification-s3-fa-fu-REVIEW.md` + `unification-s3-fa-fu-wrong.json` (166 mục, kind="moan", item="M1"/"M16"/"M17").

**Tổng cộng sau đợt này: 60 mục / 1.770 dòng sai (unification)** (cơ sở 57 mục / 1.604 dòng + đợt U11a 3 mục mới (M1, M16, M17) / 166 dòng — REBASE bởi coordinator: snippet gốc ghi cơ sở 24/686 đã cũ vì U13a/U5 gộp trước.)


# Snippet — Unification batch U7a (§2 P4 Kisaki address: "anh Soutetsu" → "Soutetsu", folders 03_Paulette + 06_Kisaki)

- U7a / §2 P4 (quyết 21/11 ~19:45, Hieu): Kisaki → Soutetsu "anh Soutetsu" → tên trần "Soutetsu" — **126 dòng, 132 lần xuất hiện** trong 5 file 06_Kisaki (稀咲02_新事業案 15 · 稀咲03_純白のレール 8 · 稀咲h1_性生活 34 · 稀咲h2_プライベートルーム 24, gồm 2 dòng rên tách tên "anh Sou――tetsu" · 稀咲h3_チャイナドレスでおもてなし 45). Folder 03_Paulette (file không lr) **0 dòng**. Đã đọc kiểm chứng từng dòng kèm 3–5 dòng kề: JP đều là 双鉄 trần (124 dòng) hoặc tách tên trong rên (2 dòng); 0 dòng ngôi ba với người khác; giữ 1 dòng đã đúng (h3 2195 "Sou――tetsu"); không đụng 2 dòng người nói khác (稀咲02 2376 Hibiki — đã sửa trong audit; 稀咲03 2137 Reina — "anh Soutetsu" đúng với cô ấy).
- Quyết định trong batch (theo uỷ quyền): (D1) 2 dòng rên tách tên h2 1166/1205 TÍNH là fix — "anh Sou――tetsu" là cùng dạng xưng hô, chỉ bị ngắt bởi dấu rên (JP tách tên tương tự); fix chỉ bỏ "anh ", giữ "Sou――tetsu". (D2) Tiêu chí là NGƯỜI NGHE, không phải vai trò ngữ pháp: sửa cả khi "anh Soutetsu" là chủ ngữ/sở hữu trong lúc Kisaki nói với Soutetsu (vd. h1 1471, h2 1268, h3 2731/2793). (D3) Nguồn `old_vn` (sau khi coordinator GHÉP 2 dòng — xem dưới): CSV3 114 dòng, audit fix 8 dòng, moan fix 2 dòng, unification đã gộp 2 dòng (1416 — fix T60; 2203 — fix M17).
- Lượt soát 2: **126/126 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 5 file / 126 key parse-verified (giá trị khớp fix từng key).
- **Tổng cộng đợt U7a: 1 mục mới (P4) / 126 dòng.**
- **Tổng cộng sau đợt này: 61 mục / 1.894 dòng sai (unification)** (cơ sở 60 mục / 1.770 dòng + đợt U7a 1 mục mới (P4) / 124 dòng mới — 2 dòng trùng đã gộp (1416 U13a, 2203 U11a) GHÉP bởi coordinator, không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 21/662 đã cũ vì U11a gộp trước.)
- Trùng lặp: 2 key trùng với batch đã gộp — **ĐÃ GHÉP bởi coordinator 22/11 ~12:05**: 稀咲h1 1416 (P4+T60, fix T60) và 稀咲h3 2203 (P4+M17, fix M17); old_vn := fix đã gộp, fix := giá trị kết hợp (kiểm chứng 2 chiều, xem ghi chú điều phối trong REVIEW).
- Nợ coordinator: (1) **Va chạm merge-order — XỬ LÝ TRƯỚC KHI GỘP: 稀咲h1_性生活.txt.toml key 1416 trùng với `unification-t1-open-t56-t66-wrong.json` (batch T56–T66, 171 mục, tạo trong lúc đợt này chạy, chưa gộp).** Cả hai `old_vn` giống nhau (giá trị audit); batch kia sửa T60 "giám đốc ngân hàng" → "tổng giám đốc ngân hàng" (giữ "Anh Soutetsu"), đợt này sửa P4 "Anh Soutetsu" → "Soutetsu" (giữ "giám đốc ngân hàng"). Giá trị gộp đúng: 「Không sao, em quen rồi.\nSoutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」 — bên nào gộp sau sẽ ghi đè thay đổi của bên kia nếu không xử lý (chi tiết REVIEW §7). (2) Cờ U6 Grand 08 key 1702 đã kiểm chứng: KHÔNG có gì để sửa cho P4 (Kisaki nói 「キミは、それで――」/「Cậu, như vậy thì――」) — batch 09_Grand không cần đụng dòng này. (3) U7b ĐÃ chạy xong trong lúc đợt này chạy: `unification-s2-kisaki-address-tsuika-lr-wrong.json` (51 mục — ít hơn 62 dòng đếm thô của đợt này; lr_稀咲ポーレットh1 còn 37 dòng Paulette "anh Soutetsu" là ĐÚNG, không được sửa theo P4); 11_Other 0 dòng. (4) Số liệu trong list §2 P4 lệch với thực tế: h1 list 41 → thực 34 (+2 tách tên); h2 list 37 → thực 22 (+2 tách tên; 12 "Anh Sou…" là dạng hoa đầu câu + tách tên, 10 "anh" trần là đại từ ngôi 2, ngoài phạm vi P4); h3 list 33× → thực 45; Kisaki03 key 1793 trong list không phải P4 (chỉ có đại từ "anh", không có "anh Soutetsu").
- File: `unification/unification-s2-kisaki-address-03-06-REVIEW.md`, `unification-s2-kisaki-address-03-06-wrong.json` (126 dòng, kind="pronoun", item="P4").


# Snippet — Unification U7b: §2 P4 Kisaki → Soutetsu bare "Soutetsu" (tsuika + lr files)

- Đợt U7b: mục §2 P4 (DECIDED 21/11 ~19:45, Muse theo uỷ quyền) — Kisaki gọi Soutetsu bằng tên trần "Soutetsu", không bao giờ "anh Soutetsu": **51 dòng sửa (60 lần xuất hiện), 4 file** (lr稀咲追加h 23, lr_稀咲ポーレットh1 21, lr稀咲追加02 4, lr稀咲追加01 3; lr稀咲追加03 và lr_稀咲h1 0 dòng — đã đúng sẵn; 11_Other 0 dòng Kisaki).
- Cả 51 dòng đều đọc JP (+TW, trừ tsuika01 TW đã SHIFT nên chỉ dùng JP + dòng kề) và xác nhận người nghe là Soutetsu (hô gọi, hỏi trực tiếp, sở hữu của người nghe); JP 双鉄 trần ở 59/62 dòng ứng viên (3 dòng dùng そうてつ/てつ tách âm nhưng TW xác nhận đối tượng là Soutetsu). 11 dòng ứng viên Kisaki GIỮ vì ngôi ba (nói về Soutetsu với Paulette/Suika: tsuika02 1233; lr_稀咲ポーレットh1 1389/1632/1722/1772/1792/1802/1804/1844/1845/1879 — 1722/1772/1879 là ranh giới, có thể đảo ngược); 55 dòng "anh Soutetsu" của người nói khác giữ nguyên (Paulette 37, Suika 11, Khương 6, Soutetsu 1).
- Nguồn old_vn (sau khi coordinator GHÉP 2 dòng — xem dưới): CSV3 42 / moan 5 / audit 1 / unification đã gộp 3 (tsuika02 1629 — fix T56; lr_稀咲ポーレットh1 1470 — fix M16; 1513 — fix M1). Lượt soát 2: 51/51 tái kiểm chứng, 0 loại, 0 sửa. Khối TOML 4 file / 51 key parse-verified.
- Cờ: F-P4-1 dạng tách tên "Anh, Soutetsu"/"Anh Sou, tetsu" (8 dòng, vd. lr稀咲追加h 1025/1074/1137/1355, lr_稀咲ポーレットh1 1364) — cần quyết định chung có bỏ "Anh" ở dạng tách tên không; F-P4-2 Grand 08 key 1702 đã kiểm chứng: Kisaki nói nhưng VN "Cậu, như vậy thì――", không phải dòng P4, không cần sửa.
- File: `unification/unification-s2-kisaki-address-tsuika-lr-REVIEW.md` + `unification-s2-kisaki-address-tsuika-lr-wrong.json` (51 mục, kind="pronoun", item="P4").

**Tổng cộng sau đợt này: 61 mục / 1.942 dòng sai (unification)** (cơ sở 61 mục / 1.894 dòng + đợt U7b 0 mục mới (P4 đã tính ở U7a) / 48 dòng mới — 3 dòng trùng đã gộp (1629 U13a, 1470/1513 U11a) trong đó 2 dòng GHÉP bởi coordinator, không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 21/662 đã cũ vì U7a gộp trước — đúng như lưu ý thứ tự gộp của snippet: P4 cộng 0 mục.)


# Snippet — Unification batch U12a (§3 moan/SFX, DIALOGUE tokens: M7, M8, M9, M10, M11, M15, M68, M70)

- U12a / §3 M7 (quyết 22/11 ~11:30, coordinator theo ủy quyền Hieu): くっ đối thoại H-scene → "Ku" — **23 dòng** trong 15 file (Ư/ư → "Ku" 17, "Hự"/"hự" → "Ku" 5, chèn token bị bỏ mất 1: lr_ポーレットh2 1041). Giữ "Hự" 4 file quy ước (lr_ふかみh2, 日々姫h1, lrれいな追加h, ハチロクh2 — 11 dòng, không phải 12 như F1 ghi).
- U12a / §3 M8 (quyết 22/11 ~11:30): や/やっ theo token KỀ SAU — **17 dòng**: "Á" 8 (theo sau là lời nói/từ chối), "Ya" 5 (trong chuỗi rên), "Áa" 2 (やあっ, giữ độ dài), "Yaan" 1 (やぁん, họ やん), hoa đầu token cuối 1 (lr_凪h2 1203 "áa!"→"Áa!"). Số "A" trần thật sự của や chỉ 17, không phải 64 như F1 ghi (phần lớn là あっ→"A").
- U12a / §3 M9 (quyết 22/11 ~11:30): ふっ thống nhất TRONG file — **8 dòng**: 真闇h3 "phù"→"Phư" 3, ハチロクh9 "phù"/"Phù"→"Fu" 3 (file thành "Fu" 6/6), lr_ニイロクh "phù"→"Fu" 1, lr_真闇h1 "phù"→"Fu" 1 (đảo ngược fix moan). F1 ghi lr_ニイロクh "Fu 2" — thực tế "Fu" ×3.
- U12a / §3 M10 (quyết 22/11 ~11:30): ふぇ/ふえ thán từ ngạc nhiên độc lập (TW 哎/咦) → "Hể?" — **5 dòng** (凪h1 1090, ふかみh1 993, れいなh3 1026, れいなh4 1897, lr_稀咲h1 992 — 992 đảo ngược fix moan "Fue!?").
- U12a / §3 M11 (quyết 22/11 ~11:30): ふや H-scene → romaji "Fuya" (giữ độ dài) — **16 dòng** (gồm ふやん→"Fuyan" 2: ふかみh3 2366, 日々姫h2 1081; "fuya" chữ thường giữa chuỗi 1: ハチロクh4 1121). Số a kiểm bằng máy (lr追加_みくろ＆日々姫h 1731: 7a).
- U12a / §3 M15 (quyết 22/11 ~11:30): ん+phụ âm H-scene → romaji — **11 dòng** (Na 1, Nfu 1, Nkyu 2 — gồm 843 tổng 17u kiểm bằng máy, Nku 4, Nu 1, "ưn"→"ưm" 2). ハチロクh8 1561 nằm trong （ ） — chỉ sửa token, cờ ranh giới cho U12b.
- U12a / §3 M68 (quyết 22/11 ~11:30): れろ dài (≥3 mora) → romaji "Rero" + số o theo JP (1 + số お/ぉ) — **18 dòng** (Nhóm 1: 4; Nhóm 2: 10; chuẩn hóa 1461: 1; 2546 "Ngoáyyyyyy": 1; sweep-added 1640 + 1056: 2). Số o kiểm bằng máy 18/18. Dòng "rộp" (14) không động — chờ T77.
- U12a / §3 M70 (quyết 22/11 ~11:30): **1 dòng** — 真闇h2 1842: きゅうっ (ngắn, TW 壓) → "Thắt lại" theo hệ romaji của file; きゅぷっ giữ "kypu" (không có nghĩa VN trong file).
- Lượt soát 2: **99/99 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 43 file / 99 key parse-verified. Nguồn old_vn (sau khi coordinator GHÉP 1 dòng): CSV3 51 / audit 23 / moan 24 / unification đã gộp 1 (ハチロクh8 759 — fix M16, GHÉP bởi coordinator 22/11 ~12:10). Trùng lặp: 1 key trùng với batch đã gộp (759, U11a) — đã GHÉP.
- **Tổng cộng đợt U12a: 8 mục mới (M7, M8, M9, M10, M11, M15, M68, M70) / 99 dòng.**
- **Tổng cộng sau đợt này: 69 mục / 2.040 dòng sai (unification)** (cơ sở 61 mục / 1.942 dòng + đợt U12a 8 mục mới (M7, M8, M9, M10, M11, M15, M68, M70) / 98 dòng mới — 1 dòng trùng đã gộp (759, U11a) GHÉP bởi coordinator, không cộng lại; REBASE bởi coordinator: snippet gốc ghi cơ sở 24/686 đã cũ vì U7a/U7b gộp trước.)
- Cờ cho coordinator: (F1) M7 còn 59 dòng Hự đối thoại ngoài 4 file quy ước + 5 dòng đã đổi — cần quyết follow-up (xem REVIEW §5, bảng theo file); (F2) M15 sweep ~154 dòng dạng tách ("Ưm kyu"/"Ưm ku"/…) không đổi — khoảng trống giữa quy tắc và list đã nêu tên; (F3) ふかみh2 989 くっ→"Kh" (khóa Kh vs M7); (F4) M68 sweep-added 1640 + 1056; (F5) M10 cờ trong dòng M11 (ポーレットh2 929/957, ふえ/ふぇ→"phuê"/"Phuê" trong chuỗi rên); (F6) ranh giới Ya-vs-Á (1445, 862, 927, 1007, 1070, 1010, 1084); (F7) sửa số liệu F1: 4 file quy ước 11 dòng Hự (không phải 12), lr_ニイロクh "Fu" ×3, ハチロク02 2170 thuộc file ハートブレイク (không phải 8620運転台通信); (F8) ranh giới U12b: ハチロクh8 1561 nằm trong （ ）.
- File: `unification/unification-s3-moan-dialogue-REVIEW.md`, `unification-s3-moan-dialogue-wrong.json` (99 dòng).


# Snippet — Unification batch U12b (§3 M14 descriptive-SFX counting + M19 re-checks)

- U12b / §3 M14 (quyết 22/11 ~11:30, coordinator theo ủy quyền Hieu): thống nhất CÁCH ĐẾM chữ kéo trong （ ） SFX, giữ hệ từng file (romaji ở 真闇h2/ハチロクh3/日々姫h4/lr稀咲追加h, động từ VN elsewhere) — **298 dòng** trong 53 file: (a) 17 dòng đếm sai đã liệt kê (kèm 1810 giữ nguyên vì đã đúng); (b) 2 dòng loại chữ kéo (1679 い×1 → "Kéé", 1681 い×6 → "Xoèèèèèèè"); (c) 279 dòng thêm chữ kéo cho các dòng bị mất độ dài (kèm 9 dòng SPACED sửa số chữ cách nhau). Quy tắc đã hòa giải: phụ âm cuối → tổng chữ trong từ = số marks; nguyên âm cuối → tổng = 1 + số marks; size = max(marks, long-vowel run, liquid run); đếm đúng như viết ("Phập" = 1 p, "tuột" = 2 t).
- U12b / §3 M19 (quyết 22/11 ~11:30): kiểm lại 3 dòng じゅぶっ — **0 dòng sửa**: lr_れいなh1 1896/1867 giữ "Chu mút" (file đồng nhất "Chu mút" cho じゅぶっ ở mọi dòng kể cả chuỗi thrust), lr_ハチロクh3 1935 giữ "Phập!" ×4 (chuỗi có ばちゅっ ×2 = thrust; phân loại "mouth" của máy sai).
- Liệt kê bằng máy: LOST 306 token / 298 dòng (khác xa ước tính ~122 của F1 — đã thử hòa giải, không tái tạo được 122); SPACED 21 token / 20 dòng; DASHES 9 dòng và DAI-WORD 6 dòng giữ nguyên theo quy ước file; quét HAS-RUN cờ 134 token / 126 dòng — KHÔNG sửa, ứng viên batch follow-up.
- Lượt soát 2: **303 dòng xét / 298 tái kiểm chứng / 5 loại / 43 sửa** (5 dòng loại: 1532/1539/1836/1986/2039 — "tuột"/"phập" đã đủ tổng; 43 sửa gồm 42 do kiểm chứng máy phát hiện lệch ±1 và 1 ở lượt đọc lại — lr_凪h2 1803). Khối TOML 53 file / 298 key parse-verified. Trùng lặp: 0 key trùng với các file unification đã gộp (kiểm theo thứ tự đúng unification-đã-gộp > moan > audit > CSV3).
- **Tổng cộng đợt U12b: 2 mục mới (M14, M19) / 298 dòng.**
- **Tổng cộng sau đợt này: 71 mục / 2.338 dòng sai (unification)** (cơ sở 69 mục / 2.040 dòng + đợt U12b 2 mục mới (M14, M19) / 298 dòng — REBASE bởi coordinator: snippet gốc ghi cơ sở 32/785 đã cũ vì U12a gộp trước (69/2.040).
- Cờ cho coordinator: (F1) 306-vs-122 — liệt kê máy vs ước tính F1; (F2) HAS-RUN mismatch scan 126 dòng — ứng viên follow-up; (F3) sửa số liệu F1: 1679 い×1, 1681 い×6, 1797 lr_日々姫h1 đích 16 i (máy đếm 15ぅ); (F4) quy ước đếm "Phập" hoa/thường theo ví dụ coordinator (1768 run 14); (F5) ranh giới U12a: lr_ポーレットh2 1178 (chỉ sửa phần （ ）), ハチロクh8 1561 ngoài phạm vi (token đối thoại); (F6) 日々姫h3 1857 chuyển M68; (F7) 真闇h2 1821 giữ hệ VN của dòng; (F8) 1610/1672 thuộc ポーレットh4/h7; (F9) thứ tự old_vn đã hiệu chỉnh — 0 dòng bị ảnh hưởng; (F10) hàng "dàiiiiiiiii" lr真闇追加h trong bucket F2.
- File: `unification/unification-s3-sfx-counting-REVIEW.md`, `unification/unification-s3-sfx-counting-wrong.json` (298 dòng, kind="moan", item="M14").
# Snippet — Unification batch U11b (§3 M3: re-examine already-merged "Á" rows for the ひゃ/ひゅ/ひあ/きゃ family)

- U11b / §3 M3 (quyết 21/11 ~11:55, Muse theo uỷ quyền): rà lại các dòng "Á" đã merge thuộc họ ひゃ/ひゅ/ひあ/きゃ trong dòng rên H-scene → romaji — **1 dòng sửa** (凪ふかみh1 1218: きゃあっ→"Kyaa", 2 a theo công thức; old_vn là moan fix 「Á——ưm——á——nóng quá——Fua——」, vòng rên trước đó chỉ đổi phù→Fua mà sót "Á" đầu dòng). Vòng rên đã làm sạch họ này: 8 dòng "Á" họ ひゃ trong cùng file đều đã thành romaji (1214/1216/1219/1221/1222/1223/1224/1226).
- Liệt kê bằng máy theo thứ tự giá trị hiện tại (unification-đã-gộp > moan > audit > CSV3 good set): 441 dòng thô (Á/á + JP họ này) → 37 ứng viên token "Á" trong 63 file H → 1 lỗi; 36 dòng GIỮ có lý do từng dòng: "Á" diễn あっ (14), やっ theo M8 (5), tiểu từ địa phương ばい/けん/から (11), mora khác んあっ/にっ/こっ/ちゃんっ/もうっ (5), ranh giới tiếng hét giật mình (1: ふかみh1 995). Ngoài 37 ứng viên, quét đối chứng đọc thêm 6 dòng loại trừ (sweep A — くひゅ→"Khíu", lời kể, しなきゃ ngữ pháp, ひゅごっ diễn nghĩa, こぎゃん địa phương). 175 dòng "Á" ngoài file H (tiếng hét giật mình) ngoài phạm vi M3, không đụng. Không đụng dòng gasp-Ư hay "Kh" nào.
- Lượt soát 2: **1/1 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 1 file / 1 key parse-verified. Trùng lặp: 0 key trùng với các file unification đã gộp (không cần ghép).
- **Tổng cộng đợt U11b: 1 mục mới (M3) / 1 dòng.**
- **Tổng cộng sau đợt này: 72 mục / 2.339 dòng sai (unification)** (cơ sở 71 mục / 2.338 dòng + đợt U11b 1 mục mới (M3) / 1 dòng — REBASE: cơ sở lấy từ `unification/ROUTE-UNIFICATION.md` hiện tại, khớp con số spawn-time 71/2.338.)
- Cờ cho coordinator: (F1) ranh giới M3 — tiếng hét giật mình きゃっ trong file H (ふかみh1 995, giữ "Á!?") có tính là dòng rên M3 không; nếu mở rộng thì cả các dòng hét ngoài file H cũng phải quyết riêng.
- File: `unification/unification-s3-hya-a-reexam-REVIEW.md`, `unification/unification-s3-hya-a-reexam-wrong.json` (1 dòng, kind="moan", item="M3").

# Snippet — Unification batch U8 (§2 P3/P5/P6/P8 + §6 F17–F24 + §7 O2/O3, Niiroku + tsuika Kisaki pronoun cluster)

- U8 / §6 F17 (quyết 22/11 ~03:32): Niiroku02 1547 — Shiro hỏi Niiroku-chan có sao không — **1 dòng** ("Chị nghe đây?" → "Em có sao không?").
- U8 / §6 F18 (quyết 22/11 ~03:32): Niiroku02 1166 — quotative と → romaji — **1 dòng** ("'Chứ'" → "'To'").
- U8 / §2 P8 + §6 F19 (quyết 22/11 ~03:32): Niiroku tự xưng với Akai → "Tôi" — **3 dòng** (Niiroku02 1570/1788/1878). Niiroku01 1563/1907 GIỮ cả hai (F25 — JP cố ý đổi "Shiro" vs "D60 46").
- U8 / §6 F20 (quyết 22/11 ~03:32): tsuika01 Soutetsu "Anh" → "Tôi" — **3 dòng** (720/1116/1322; 1116 GHÉP cả F21: "Tôi nghĩ cô đánh giá tôi hơi cao").
- U8 / §2 P3 + §6 F21 (quyết 22/11 ~03:32): Soutetsu → Kisaki "em" → "cô" — **17 dòng** (tsuika01 9: 1025/1116/1187/1246/1249/1290/1371/1534/1538; tsuika02 8: 1089/1118/1188/1216/1761/1910/1077/1568) + **3 dòng** 稀咲h2 (933/1334/1338). Hiệu chỉnh: tsuika02 chỉ 8 dòng, không phải 9 — §8 C20 sai (1180 là gasp của Suika, 1168 là "A——", 1043 không tồn tại); F21 tổng thực tế 17, không phải 18.
- U8 / §2 P6 + §6 F22 (quyết 22/11 ~03:32): tsuika01 Kisaki キミ "anh" → "cậu" — **4 dòng** (1327/1564/1587/1783).
- U8 / §6 F23: tsuika01 "anh Soutetsu" → bare "Soutetsu" — **0 dòng mới** (U7b đã sửa xong cả 3 key 1488/1687/1783).
- U8 / §2 P5 + §6 F24 (quyết 22/11 ~03:32): tsuika01 Kisaki tự xưng → "em" — **6 dòng** (1327/1132/1024/984/1711/1783; 984 tin cậy thấp nhất; 1516 GIỮ "tôi" — trấn an quyết đoán, ranh giới như 1744). P5 ở tsuika02: rà 22 dòng "Tôi" của Kisaki, **0 dòng đổi** (chuyến khảo sát công việc, chế độ công việc xuyên suốt; đoạn kết thân mật chỉ có độc thoại). Nhánh Kisaki03 + 稀咲02 của P5 ngoài phạm vi U8.
- U8 / §7 O2 (quyết 22/11 theo uỷ quyền Hieu — XÁC NHẬN phán đoán biên của audit, 0 dòng đổi): lr稀咲追加03 896/906/1007/1026 giữ "em" (thân mật/dễ tổn thương), 940 giữ "tôi" (quyết đoán); tsuika02 1233 giữ "tôi" (bàn luận công việc với Suika). Nhãn file trong list sai: các key này thuộc tsuika03/tsuika02, không phải 稀咲h2/稀咲h1.
- U8 / §7 O3 (quyết 22/11 theo uỷ quyền Hieu — ÁP "Tôi"): lr_ニイロクh **15 dòng** "em" → "Tôi" (1211/1215/1293/1322/1339/1377/1402/1438/1439/1457/1508/1534/1545/1547/1549; 1439 đổi cả "của mình"→"của tôi"). Bằng chứng: JP 自分 đồng nhất cả 3 file (h-file ×8, 01 ×14, 02 ×20; không có わたし/あたし) — phân bố 15 "em"/0 "Tôi" là lệch của bản dịch, không phải chuyển register trong JP.
- GHÉP với batch đã gộp (2 dòng): tsuika01 1783 (old_vn = fix U7b P4; thêm F22+F24), tsuika02 1077 (old_vn = fix U-t56-t66 "Trung Quốc"; thêm F21). Lượt soát 2: **50/50 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 5 file / 50 key parse-verified. Nguồn old_vn: CSV3 40 / audit 3 / moan 5 / unification đã gộp 2.
- Cờ cho coordinator: (F1) P1 chưa có batch nào nhận — 稀咲h2 còn ~18 dòng Soutetsu "Anh" với Kisaki (915/932/933/1207/1226/1230/1233/1236/1265/1271/1273/1275/1278/1295/1302/1313/1321/1334) chưa đổi thành "Tôi"; cùng mẫu "Anh" trần chỉ Soutetsu ở tsuika01 1488 câu 2 và tsuika02 1084 (U7b để lại) cần quyết chung; (F2) F21 tổng thực tế 17 dòng (C20 sai — xem trên); (F3) tsuika02 1077/1568 xác định người nghe bằng loại trừ (độ tin cậy trung-cao, xem REVIEW §5–§6); (F4) tsuika01 1564 "Em" giữ lại — dòng Kisaki tự xưng duy nhất ở tsuika01 chưa được quyết; (F5) O2 nhãn file sai trong list (tsuika03/tsuika02, không phải h2/h1); (F6) P5 nhánh Kisaki03 + 稀咲02 chưa có batch.
- File: `unification/unification-s2-niiroku-tsuika-cluster-REVIEW.md` + `unification-s2-niiroku-tsuika-cluster-wrong.json` (50 mục, kind="pronoun").

**Tổng cộng sau đợt này: 86 mục / 2.387 dòng sai (unification)** (cơ sở 72 mục / 2.339 dòng (U11b gộp trước trong lúc U8 chạy; snippet gốc ghi cơ sở 71/2.338 đã cũ) + đợt U8 14 mục mới (P3, P5, P6, P8, F17, F18, F19, F20, F21, F22, F23, F24, O2, O3) / 48 dòng mới (50 JSON − 2 GHÉP 1783/1077 đã cộng ở U7b/U13a, không cộng lại) — HIỆU CHỈNH bởi coordinator 22/11 ~12:50 (xem cờ F9 ở mục U10b; snippet gốc ghi 86/2.389 là sai).

# Snippet — Unification batch U10b (§6 F30: moan-beats-audit restorations/cancellations)

- U10b / §6 F30: các dòng vòng moan thắng vòng audit (hoặc fix audit bị HUỶ, khôi phục giá trị trước audit) — **105 dòng xét: 12 dòng sửa, 93 dòng giữ có lý do**.
- 12 dòng sửa (4 file): lr追加_みくろ 5 (1708 "Phuê"→"Fue", 1716 "phuê"→"Fue" GHÉP với U11a, 1758 "phuê"→"Fue", 1811 "pùa"→"Pua", 1901 "Pùa"→"Pua" — đều khôi phục CSV3); ポーレットh6 4 (768 "Kíuuuuuuuuun"→"Kyuuuuuuuuuun" 10u, 800/818 "Ư a"→"Kua", 869 "Ưm!"→"Nkyun!"); ポーレットh5 2 (932 "Ư a!"→"Kua!", 947 "Ưm!!!!"→"Nkyun!!!!"); ハチロクh8 878 (OPEN → QUYẾT khôi phục "ưm!" — JP んっ là mora hơi thở riêng biệt + TW 嗯; audit mời xem lại).
- 93 dòng giữ: ポーレットh8 14 (= moan; 2132 15a đã kiểm chứng), lr_ふかみh1 33 (= moan; 1469 đã GHÉP bởi U12a M7, 1967 audit==moan), lr追加_みくろ 18/23 (romaji đã khôi phục bởi U11a M16 hoặc giống CSV3; 1731 7a, 1857 đúng y moan review §5), ポーレットh4 882/884 + 凪h1 1091 (= moan = CSV3), lr_真闇h1 1433/1598, lr_日々姫真闇h1 1555/1619, ポーレットh2 7 (950 giữ Ư, 952/985/1004/1135 gasp-Ư của audit, 963 10u, 1003 "Kua!"), 日々姫h6 2075/2082, 日々姫h1 970, 凪ふかみh2 1294, lr_稀咲h1 1708 (16u), lr_ふかみh2 1085 (19a), 日々姫h5 1153 (9a), れいなh2 1095, lr_ハチロクh1 1234, lr_日々姫ふかみh1 933/1358/1406/1423/1475 (1358 = U11a M16 "Fafyuuuuuuuuuuuuuunn", 14u/2n).
- Nhãn file trong list F30 sai có hệ thống (key đáng tin, nhãn file không) — bảng hiệu chỉnh đầy đủ ở REVIEW §2 (vd. "ふかみh1 14" thực ra là ポーレットh8; "ハチロクh6/h7" thực ra là ポーレットh6/h5; "日々姫h1 1294" thực ra là 凪ふかみh2).
- Lượt soát 2: **12/12 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 4 file / 12 key parse-verified, khớp JSON.
- **Tổng cộng đợt U10b: 1 mục mới (F30) / 12 dòng (11 dòng mới + 1 dòng GHÉP mikuro 1716 với U11a, không cộng lại).**
- **Tổng cộng sau đợt này: 87 mục / 2.398 dòng sai (unification)** (cơ sở 86 mục / 2.387 dòng — REBASE bởi coordinator: chuỗi tổng sau U8 đã hiệu chỉnh từ 2.389 xuống 2.387 (2 dòng GHÉP 1783/1077 không cộng lại, xem cờ F9) + đợt U10b 1 mục mới (F30) / 11 dòng mới).
- Cờ cho coordinator: (F1) hiệu chỉnh nhãn file F30 trong list (§2 REVIEW); (F2) M7 có bao phủ ポーレットh8 2241 (くっ→"Hự" giữ, M7 "Ku" không áp)?; (F3) M10 có bao phủ ポーレットh8 2185 (ふえ độc lập, ứng viên thứ 6) và ranh giới M10 ở mikuro 1708/1758?; (F4) 1358 đã bị M16 thay thế ở token ふぁ; (F5) ĐÃ QUYẾT bởi coordinator 22/11 ~12:50: token romaji SFX viết hoa MỌI VỊ TRÍ (U11a M16 18/18 mikuro hoa kể cả giữa dòng; vòng moan nghiêng hoa sau ── 10 vs 2; chữ thường CSV3 là thói quen của Gemini) — 3 fix U10b đã sửa (1716/1758 "Fue", 1811 "Pua"); 2 dòng "fua" thường cuối câu ở lr_ニイロクh (1322/1387) đưa vào U15; (F6) KHÔNG TÁI TẠO ĐƯỢC (coordinator kiểm chứng từ disk): file supplement chỉ có 4 key (963/1007/1039/1067), không chia sẻ key nào với file main (24 key); các key 1029/1063/1677 chỉ có trong main, không có JP trùng nào trong supplement — không có xung đột; cờ đóng, không đưa vào U15. (F7) 4 dòng audit-only fa/fu mikuro 1703/1707/1925/2322 đã kiểm tra — đều là hơi thở ngắn ふっ/ふぉ ("Phù"/"phu" đúng), không phải ứng viên huỷ; (F8) lr_ポーレットh2 1095 không phải 1095 của F30 (moan khôi phục `\n`, trái quy ước single-line của file — ngoài phạm vi); (F9) ĐÃ XÁC NHẬN bởi coordinator: worker ĐÚNG — chuỗi tổng sau U8 là 86/2.387 (không phải 86/2.389); tiền lệ U3/U7a/U7b/U12a/U5/U13a đều chỉ cộng dòng MỚI, GHÉP không cộng lại. ROUTE + queue đã hiệu chỉnh; đợt này 87/2.398.
- File: `unification/unification-s6-f30-moan-beats-audit-REVIEW.md`, `unification/unification-s6-f30-moan-beats-audit-wrong.json` (12 dòng, kind="moan", item="F30").


# Snippet — Unification batch U13b (§1 OPEN T67–T81, E2: thuật ngữ mở + SFX chụt/rộp/Phập)

- U13b / T67 (KEEP "buổi bình chọn"): 0 dòng — 日々姫07 2114/1883 đã đúng (JP ひんぴょー会, không có dòng 評議会).
- U13b / T68 ("Showa"): **6 dòng** (ハチロク03 2176 "Chiêu Hòa 11"→"Showa 11", 2550 "Chiêu Hòa 49"→"Showa 49"; ハチロクh9 1410 "Chính Hòa (Showa)"→"Showa"; 仲国02 2617/2492 "Chính Hà 59"→"Showa 59"; lrれいな追加01 1397 "Dầu mỏ Showakai"→"Dầu mỏ Showa Shell" — JP 正和貝石油, chơi chữ 昭和シェル石油). 19/25 dòng phụ lục đã "Showa".
- U13b / T69 (KEEP "Khách sạn Teio"): 0 dòng — グランドリライト08_ふかみ 1628/1858/1895/2155 đã đúng.
- U13b / T70 (KEEP "Niigata"): 0 dòng — 稀咲h3 2648 đã đúng.
- U13b / T71 ("Tàu nhà hàng"): **11 dòng** (10 "Toa ăn Train" + 日々姫09 1753 "nhà ăn trên tàu"); 1358 bỏ gloss "(Toa ăn Tàu hỏa)", 3652 chỉ đổi tên trong ngoặc kép. 13/24 dòng phụ lục đã "Tàu nhà hàng".
- U13b / T72 ("hình quạt", tính từ): **18 dòng** (3052 đổi cả 2 chỗ; 1619 GHÉP với U1a). 6/24 dòng phụ lục đã "hình quạt".
- U13b / T73 ("Hinomoto Nadeshiko"): **3 dòng** (ハチロク09 1879/1508, ハチロクh6 993). 1508 không có gloss cần sửa (E2 CUR cũ; old_vn audit không có gloss).
- U13b / T74 ("hợp đồng chủ tàu"): **1 dòng** (凪h2_おとなの水着 1766, GHÉP với U2b — giữ "Đường sắt Ohitoyo"; list ghi sai file 日々姫h2).
- U13b / T75 (họ "chụt" cho âm hôn trần, theo token, công thức nguyên âm): **71 dòng đổi / 78 phụ lục** — 2 dòng biên GIỮ sau khi đọc cảnh (日々姫h6 3707 ちゅぶっ = tiếng ướt "Nhóp nhép", không phải hôn; ポーレットh3 967 ちゅる―― = trượt liếm "Churu", không phải hôn); 5 dòng chỉ có ちゅず/ちゅく/ちゅりゅ ngoài phạm vi GIỮ (2031/1037/1652/2534/2357).
- U13b / T77 ("rộp" cho token SFX れる/るっ — れろ LOẠI theo quyết coordinator, khác khuyến nghị E2): **188 dòng đổi** (phụ lục 251 dòng: 205 dòng có token れる/るっ — 204 + biến thể lắp れっるっ 1046; 17 dòng có token nhưng không đổi: 16 đã "rộp" + 1 động từ hội thoại 2452; 46 dòng chỉ có れろ/れりゅ). 2 dòng trong phụ lục chỉ đổi T75 (2133, 1068). Quyết biên: 1033 るっ = LICKING (TW toàn âm miệng; kề ぶっ — coordinator xem lại nếu cần); 1475 るっ cuối = THRUST, GIỮ "ru"; 2043 đổi cả るっ + るうううっ trong chuỗi romaji miệng (thành hỗn hợp romaji+VN).
- U13b / T78a (ずぶ SFX → "Phập"): **21 dòng** (15 romaji + 5 "Thọc sâu"/"Thọc"/"Đâm sâu" + 2597 "lún"); chỉ đổi token ずぶ, giữ token khác trong chuỗi. 4 dòng phụ lục GIỮ (1261/881/971 động từ hội thoại, 3140 mô tả ずぶずぶ).
- U13b / T78b (ぬぶ, từng dòng): **2 dòng đổi** (れいなh2 1730 → "Rúttttttttttt——bạch" — 11 t theo JP, hiệu chỉnh M14: CUR audit 10 p và quyết gốc 10 t đều thiếu 1; 真闇h2 1830 → "Rút rút rút rút"); 8 dòng GIỮ, trong đó lr_ふかみh2 1122 GIỮ "Nubu!" (cảnh miệng, hướng không xác định — "Rút" sẽ khẳng định chiều rút không có trong cảnh).
- U13b / T79 (きゃふ → romaji "Kyafu"): **1 dòng** (稀咲h3 1988 "kya phu"→"Kyafu"). 24/25 dòng phụ lục đã romaji.
- U13b / T81 (KEEP "Fukutake"): 0 dòng — ポーレットh8 2462 đã đúng (audit sửa từ "Fukuoka").
- Lượt soát 2: **304/304 tái kiểm chứng, 299 đúng, 5 sửa, 0 loại** — 5 lỗi lệch chỉ số lượt 1 (lr_凪h2 1290, lr真闇追加h 1162/1135, lr_凪ふかみh1 1644, ハチロクh6 934: thay nhầm từ kề chụt/mút/Ưc thay vì token れる/るっ — do `split_pieces` đếm `"` ASCII đầu giá trị thành 1 "từ" và generator lệch trên dòng align=FAIL). Khối TOML 63 file / 304 key parse-verified, khớp JSON. Chuẩn hoá newline: 4 dòng ハチロクh6 (838/884/887/934) có old_vn/fix chứa newline thật do CSV export → chuẩn hoá về literal backslash-n (khớp giá trị parse từ TOML trên disk + tiền lệ U10b).
- **Tổng cộng đợt U13b: 13 mục mới (T67, T68, T69, T70, T71, T72, T73, T74, T75, T77, T78, T79, T81) / 304 dòng (288 dòng mới + 16 dòng GHÉP với batch đã gộp, không cộng lại).**
- **Tổng cộng sau đợt này: 100 mục / 2.686 dòng sai (unification)** (cơ sở 87 mục / 2.398 dòng + đợt U13b 13 mục mới / 288 dòng mới).
- Cờ cho coordinator: (F1) 5 dòng T75 ngoài phạm vi (ちゅず/ちゅく/ちゅりゅ — 2031/1037/1652/2534/2357) — quyết có mở rộng token list không?; (F2) ứng viên sót T75 trong phụ lục T77/T78 (ハチロクh2 1206, lr_日々姫h2 1039/1045, lr_稀咲ポーレットh1 1585/1821/1589, lr_れいなh1 1271, ハチロクh8 825, lr_れいなh1 1266 "Chụt mút"); (F3) 5 ứng viên sót T77 trong phụ lục T75 (lr_日々姫h2 1056, 真闇h3 2332/2336, lr_稀咲h1 1058, lr_凪h1 1220 — 2336 るっ cuối chuỗi trượt nhiều khả năng KHÔNG phải token licking); (F4) mơ hồ るっ ở lr_日々姫h2 1033 (đã xếp LICKING); (F5) chuẩn hoá chữ hoa/thường token romaji còn lại theo quyết F5 (U15) — các token romaji trong dòng đã sửa được GIỮ nguyên; (F6) mục mới U15: địa danh 帝央 — "Teio" (đa số ~15 dòng) vs "Teiou" (共通06 2112, ニイロク03 1570) vs "Trung tâm Hoàng gia" (仲国05 2032); (F7) T73 1508: E2 CUR hiển thị gloss không có trong old_vn audit — không cần sửa gloss, chỉ ghi chú.
- File: `unification/unification-t1-open-t67-t81-REVIEW.md`, `unification/unification-t1-open-t67-t81-wrong.json` (304 dòng, kind="unification").
### U13b — coordinator verification notes 22/11 ~13:00 (batch verified from disk before merge):
- T78b 1730 CORRECTED 10→11 t's: JP ぬぶうううううううううううっ has 11う; M14 rule (1+う) gives 11 t's — worker's correction of the E2/task string (10 t's) is RIGHT; audit CUR (10 p) also short by 1.
- T73 1508: E2's CUR was stale — actual old_vn (audit fix) has NO "(Người phụ nữ Nhật Bản truyền thống)" gloss; fix only changes Yamato→Hinomoto Nadeshiko. No gloss fix needed.
- T77 appendix total CORRECTED: 205 rows contain a れる/るっ SFX token (204 + stutter れっるっ 1046), NOT E2's 229 (229 includes れろ). 188 changed + 17 unchanged (16 already "rộp" + 1 dialogue verb れいなh4 2452) + 46 れろ/れりゅ-only = 251.
- T74 list error: file label says 日々姫h2 — actual file is 凪h2_おとなの水着 1766. List correction for U15.
- F5 (romaji SFX capitalized everywhere, coordinator 22/11 ~12:50) NOT applied to kept romaji tokens inside U13b rows — batch scope predates the decision; swept in U15 instead.


# Snippet — Unification U14a: §7 OPEN O4–O19 (pronoun/addressee, group A)

- Đợt U14a: mục §7 O4–O19 (16 mục OPEN, quyết theo uỷ quyền của Hieu — không park mục nào): **10 dòng sửa mới, 4 file** (0 dòng GHÉP với merged batch — mọi old_vn đều là CSV3).
- O4 (ハチロク15b): 1 dòng — 1566 Soutetsu → Munakata "anh" → "cháu" (tiền lệ ハチロク12 "cháu"/"chú" ×9). 1654 Olivy "chị" GIỮ (tự xưng "chị" nhất quán toàn file 15b); độc thoại "em ấy" ×6 GIỮ (đều chỉ Olivy); 1685 "anh" GIỮ (Soutetsu → Olivy, P24).
- O5 (ハチロク09_もくもくオリヴィ): 0 dòng — GIỮ toàn bộ 14 dòng "anh"/"em" (register vợ chồng bao phủ toàn bộ chuyến đi riêng tư: tàu BBQ + nhà tắm + cảnh đêm).
- O6 ("Anh Migita" vs "ngài Migita"): 5 dòng — Hiyoko 右田氏 → "ngài Migita" (ハチロク10 2092/2197/2198/2201/2277; 2198 sửa cả chủ ngữ + hô ngữ). Hội đồng GIỮ "anh Migita" (1937/2449/1825 — JP 右田さん).
- O7 (Soutetsu ↔ Olivy): 1 dòng — ハチロク10 2304 Soutetsu → Olivy "cậu" → "em" (kề 2302 cùng cảnh). Olivy → Soutetsu GIỮ cả "cậu" (2680) lẫn "anh" (2589/2663) — cung register trước/sau thỏa thuận gọi tên trần (2709); Hachiroku → Olivy "cậu" GIỮ (ハチロク05 2557 — dạng tương hỗ).
- O8 (ハチロク10): 0 dòng — Hachiroku "Tôi" GIỮ (2321/2451/2890, nói với Hiyoko trang trọng).
- O9 (日々姫13): 0 dòng — Kisaki → Hibiki "cô" GIỮ ở cả 4 dòng (1250/1366/1243/1616, register tranh luận công khai); 2515 GIỮ fix audit "tôi".
- O10 (Grand 02): 0 dòng — Hachiroku 1195 "em" + 1785/1589 "Tôi" GIỮ (chuyển register nài nỉ → lễ nghi; JP わたくし ở 2 dòng "Tôi").
- O11 (凪ふかみ03_みかんの旅): 1 dòng — 2684 "Anh đi đây" → "Tôi đi đây" (địa chỉ nhóm Hachiroku + Hibiki; tiền lệ Grand 02 1493).
- O12 (Grand 09): 0 dòng — 1128 "anh" GIỮ (người nghe là Nagi, đã xác định); 2663 GIỮ fix audit (JP cụt).
- O13 (Grand 10): 2 dòng — 1158 "Anh thay đồ đây" → "Tôi thay đồ đây" (địa chỉ nhóm Hachiroku + Hibiki); 2006 "anh, không sao" → "tôi, không sao" (cảnh mơ, bàn tay gia đình không xác định; độ tin cậy Trung bình-cao).
- O14 (Grand 05): 0 dòng — 2025/2032/2035 "Anh" GIỮ (người nghe Reina/Michiko; Akai ở cảnh khác).
- O15 (Grand 07): 0 dòng — 2022 "mình" GIỮ (tự nhủ một mình, thuộc ngoại lệ P19).
- O16 (日々姫04_同乗 2155): 0 dòng mới — đã là "Cảm ơn em." từ U6/P2 (người nghe Paulette; list ghi sai file カフェキッチン).
- O17 (仲国04 1858): 0 dòng — "anh" GIỮ (người nghe Hibiki — file-order: đáp trực tiếp yêu cầu 1798; nghi ngờ cũ dựa trên key-order là sai).
- O18 (仲国02 2356): 0 dòng — "cậu" GIỮ (người nghe Zhihuan; đối chứng 2293 "cô" với Jiang; list ghi sai file 仲国04).
- O19 (仲国02 2182): 0 dòng — GIỮ fix audit "em" (JP gọi thẳng 日々姫; Hachiroku vắng mặt).
- Lượt soát 2: **10/10 tái kiểm chứng, 0 loại bỏ, 0 sửa lại.** JSON 10 mục = khối TOML 10 khóa (4 file); jp/tw khớp CSV3 tuyệt đối (modulo U+3000); old_vn khớp map (csv3 10/10).
- Hiệu chỉnh list: O16 file đúng 日々姫04_同乗; O18 file đúng 仲国02; O7 2557 file đúng ハチロク05; O11 file đúng みかんの旅; O9 thêm key 1616; O4 "em ấy" đếm lại 6 (không phải 8×). Cờ cho U15: Soutetsu → Olivy "cô" công việc (ハチロク14 2427/2986) — xem REVIEW §6.
- File: `unification/unification-s7-open-pronouns-a-REVIEW.md` + `unification-s7-open-pronouns-a-wrong.json` (10 mục, kind="unification", item="O4"/"O6"/"O7"/"O11"/"O13").

**Tổng cộng sau đợt này: 116 mục / 2.696 dòng sai (unification)** (cơ sở 100 mục / 2.686 dòng + đợt U14a 16 mục / 10 dòng mới — 5 mục có dòng sửa + 11 mục GIỮ đã quyết (O5/O8/O9/O10/O12/O14/O15/O16/O17/O18/O19), 0 dòng. HIỆU CHỈNH bởi coordinator: snippet gốc ghi 105 mục (chỉ cộng 5 mục có dòng sửa) — theo tiền lệ U13b/U8, mục đã quyết GIỮ vẫn tính vào chuỗi; xem ROUTE.)
### U14a — coordinator verification notes 22/11 ~13:35 (batch verified from disk before merge):
- CHUỖI HIỆU CHỈNH: worker ghi 105 mục (chỉ cộng 5 mục có dòng sửa). Coordinator sửa thành **116 mục / 2.696 dòng** — 16 mục O4–O19 đều đã quyết (11 mục GIỮ 0 dòng vẫn tính, theo tiền lệ U13b 13 mục gồm 4 mục GIỮ 0 dòng và U8 14 mục gồm O2/F23 0 dòng). Lưu ý: U13a KHÔNG cộng 3 mục GIỮ T62/T64/T65 (chuỗi khi đó 41→49 chỉ +8) — 3 mục đó đã quyết xong nhưng không nằm trong số đếm; chuỗi hiện tại mang thiếu -3 mục này, không sửa ngược.
- O17 PHƯƠNG PHÁP: key KHÔNG phải scene order — kiểm chứng từ CSV3: file 仲国04_z49列車, file-order 1927(84)→1822(85)→1798(86)→1858(87)→2001(88)→2049(89) liên tiếp; 1853/1855/1857 ở vị trí 189/282/341 (cảnh khác). 1858 đáp trực tiếp yêu cầu 1798 của Hibiki — người nghe Hibiki, "anh" đúng. Nghi ngờ cũ dựa trên key-order là sai.
- O10 (Grand 02 1195/1785/1589): GIỮ chuyển register nài nỉ→lễ nghi (JP わたくし ở 2 dòng "Tôi") — quyết gây tranh cãi nhất đợt; đảo ngược được nếu Hieu muốn Hachiroku "em" với Soutetsu mọi ngữ cảnh (cờ F-O10-1 → U15/Hieu).
- O13-2006 (mơ): đổi "anh"→"tôi" (JP 僕), độ tin cậy Trung bình-cao — hoàn lại "anh" nếu bàn tay trong mơ xác nhận là Michiko (cờ F-O13-1).
- O6 2198: 2 token "Anh" trong 1 dòng đều → "Ngài" (chủ ngữ + hô ngữ 右田氏).
- Scratch files của worker còn trong unification/ (`_u14a_*.py`, `_u14a_*.txt`) — không phải deliverable, không ảnh hưởng map gộp (không phải *.json); giữ lại làm vết kiểm chứng.


# Snippet — Unification U14b: §7 OPEN O20–O37 (pronoun/addressee, group B)

- Đợt U14b: mục §7 O20–O37 (18 mục OPEN, quyết theo uỷ quyền của Hieu — không park mục nào): **14 dòng sửa mới, 8 file** (0 dòng GHÉP với merged batch — mọi old_vn đều là CSV3, trừ 1 dòng audit).
- O20 (仲国01 1377): 0 dòng — GIỮ "chị" (Hachiroku → Hibiki "chị Hibiki" ×12 toàn dự án, gọi trực tiếp ≥5 dòng; "cô" chỉ ở cảnh tắm 共通06, P16 khóa giữ).
- O21 (凪ふかみ05): 1 dòng — 2679 Nagi → Hachiroku "cô" → "chị" (JP không đại từ; chuẩn "chị Hachiroku" ×3, 0× "cô Hachiroku"). 1981 "chị Hachiroku" GIỮ.
- O22 (凪ふかみ08c_新しい家族): 1 dòng — 2030 Soutetsu "anh" → "tôi" (đáp lời quở của Hachiroku 2554; P1). Ghi chú: đảo quyết giữ "anh" cũ của parent — cờ F-O22-1.
- O23 (凪ふかみ04): 0 dòng — GIỮ toàn bộ 6 dòng (2294/2296/2407 "em", 2309 "em" = Reina, 2393 "chị", 2174 "Em đợi anh").
- O24 (凪ふかみ01): 1 dòng — 1955 Soutetsu "Anh cảm giác" → "Tôi cảm giác" (người nghe Hachiroku; giữ nguyên fix audit). 1517 "em" GIỮ (người nghe Hachiroku, không phải Fukami). 1884 cờ cho U14c/O64.
- O25 (lr_凪ふかみh1): 3 dòng — 1620 "Chị" → "Tớ", 1672 "Chị" → "Tớ" + "em" → "cậu", 1744 "em" → "cậu" + "chị" → "tớ" (P9; khớp 1746 "tớ"/"cậu"). 1708/1825 "anh" + 1746 GIỮ. Cờ: 1616/1687/1737 cùng lỗi nhưng không có tên trong O25; 2368/2607 thuộc 日々姫03 → U14c/O64.
- O26 (ハチロク08_台枠問題): 3 dòng — 1896 "Anh muốn" → "Tôi muốn", 2398 "Anh đang nghĩ" → "Tôi đang nghĩ" (địa chỉ nhóm, P17); 2023 cắt phần hoàn thiện bịa thêm, giữ đúng điểm cụt 『…8620——』 (phần hoàn thiện là lời nối của Hachiroku 1587).
- O27 (ハチロク10_炙り出し 1825): 0 dòng — "tôi" GIỮ (địa chỉ nhóm có Hachiroku; P17).
- O28 (ハチロク07_ハチロクの目覚め 1507): 0 dòng — "cô" GIỮ (người nghe Navi xác định từ chữ 1666/1523/2305; お前 → "cô" là chuẩn đã khóa, 共通01 ×4).
- O29 (日々姫06_みくろ、来訪 1877): 0 dòng — "tìm tôi" GIỮ (người nghe 職員Ａ; list ghi sai file ハチロク10).
- O30 (ハチロク07_延命 2339): 0 dòng — "chị…em" GIỮ (người nghe Olivy, 2393/2702).
- O31 (ハチロク02_8620運転台通信): 2 dòng — 1952 "anh cũng nghĩ" → "tôi cũng nghĩ" (bàn kế hoạch với Hachiroku); 2049 "Chào em." → "Chào hai người." (おふたり = Reina + Paulette).
- O32 (日々姫h1): 0 dòng — 1352/1423 VOID; 1421/1447 độc thoại Soutetsu "tôi" GIỮ (file không có Paulette); "Kua vs Hự" đã quyết F1/M7: 1010/1052 "Kua!" GIỮ (くあっ), 1062/1041/1043/1044 "Hự" GIỮ (file convention).
- O33 (lrれいな追加02): 0 dòng — 1505 "anh" GIỮ (→ Reina), 1637 "của anh" GIỮ (→ Hibiki). Cờ: 1635 "tôi là chồng của Reina" để nguyên (nhóm hỗn hợp, P17).
- O34 (れいな03): 2 dòng — 1386 "tôi hơi choáng váng" → "em hơi choáng váng", 1644 "tôi sẽ nhận" → "em sẽ nhận" (Paulette → Soutetsu "em").
- O35 (真闇03_ひとしずく 2484): 1 dòng — "hỏi em ấy" → "hỏi chị ấy" (người nghĩ là Hibiki, hỏi Hachiroku; list ghi sai file 真闇01).
- O36 (真闇03): 0 dòng — 2038 VOID; 1999 GIỮ fix audit "anh" (người nghe Hibiki).
- O37 (ハチロク14_冬 + 日々姫05): 0 dòng — 3202/2590 GIỮ fix audit; 日々姫05 1928 "chú" GIỮ (người nghe là trẻ nhỏ) và 2038 "——A" GIỮ (っ―― đã có gạch diễn tiếng ngắt, tiền lệ 1042; list ghi sai file ハチロク14_冬).
- Lượt soát 2: **14/14 tái kiểm chứng, 0 loại bỏ, 0 sửa lại.** JSON 14 mục = khối TOML 14 khóa (8 file); jp/tw khớp CSV3 tuyệt đối (modulo U+3000); old_vn khớp map (csv3 13/14, audit 1/14 — 1955).
- Hiệu chỉnh list: O29 file đúng 日々姫06; O35 file đúng 真闇03; O37 1928/2038 file đúng 日々姫05; O25 2368/2607 file đúng 日々姫03; O32 1352/1423 + O36 2038 là key void. Cờ cho coordinator: F-O22-1 (đảo quyết cũ 2030), F-O24-1 (1884 → U14c/O64, đề xuất GIỮ "ông nội"), F-O25-1 (1616/1687/1737 cùng lỗi P9, chưa sửa), F-O25-2 (2368/2607 → U14c/O64), F-O33-1 (1635 để nguyên).
- File: `unification/unification-s7-open-pronouns-b-REVIEW.md` + `unification/unification-s7-open-pronouns-b-wrong.json` (14 mục, kind="unification", item="O21"/"O22"/"O24"/"O25"/"O26"/"O31"/"O34"/"O35").

**Tổng cộng sau đợt này: 134 mục / 2.710 dòng sai (unification)** (cơ sở 116 mục / 2.696 dòng — U14a ĐÃ gộp trước (22/11 ~13:35, chuỗi hiệu chỉnh 116) + đợt U14b 18 mục / 14 dòng mới — 8 mục có dòng sửa + 10 mục GIỮ đã quyết (O20/O23/O27/O28/O29/O30/O32/O33/O36/O37), 0 dòng. HIỆU CHỈNH bởi coordinator: snippet gốc ghi 108 mục (cơ sở cũ 100 + chỉ 8 mục có dòng sửa) — theo tiền lệ U13b/U8/U14a, mục đã quyết GIỮ vẫn tính vào chuỗi; xem ROUTE.)
### U14b — coordinator verification notes 22/11 ~13:45 (batch verified from disk before merge):
- **F-O22-1 XÁC NHẬN — override ĐÚNG, quyết cũ của parent bị đảo:** 凪ふかみ08c 2030 "anh"→"tôi" STANDS. Parent gỡ fix ngày 20/11 vì cho rằng 2554 thuộc cảnh khác (2550–2559 theo key) và dòng kề là Nagi 2029 — cả hai đều sai theo file-order: CSV3 cho thấy 2554 ở vị trí file-order 439, 2030 ở 440 (LIỀN KỀ, đáp trực tiếp); 2029 ở vị trí 30 (cảnh nước/teamwork đầu file, cách 410 vị trí). 2554 là Hachiroku quở (gọi 双鉄様, "家長としてのつとめ"), 2030 là Soutetsu nhận lỗi, 2376 Fukami bênh, narration 2780 xác nhận Fukami+Nagi bênh vực, Hachiroku cười — người nghe là Hachiroku, P1 → "tôi". Trạng thái "uncertain, chờ Hieu" trong MEMORY.md/ROUTE-AUDIT.md coi như ĐÃ GIẢI QUYẾT bằng bằng chứng, không cần park cho Hieu nữa.
- CHUỖI HIỆU CHỈNH: snippet gốc 108 mục (cơ sở 100 + 8 mục có dòng sửa) → **134 mục / 2.710 dòng** (cơ sở 116 sau U14a + 18 mục O20–O37, kể cả 10 mục GIỮ 0 dòng).
- O26 2023: bản hoàn chỉnh bịa ("không nơi nào là không thấy") đã cắt đúng điểm JP 「8620の――" → "8620——".
- F-O25-1 (lr h1 1616/1687/1737 cùng lỗi P9 như O25 nhưng không có tên trong mục) → U15 follow-up: quyết có sửa cùng dạng "tớ"/"cậu" không.
- F-O24-1: 凪ふかみ01 1884 → U14c/O64 (đề xuất GIỮ "ông nội" — JP じーちゃん chung chung, không định danh Seki).
- Scratch của worker trong unification/_u14b/ (assemble.py, build_review.py, verify_toml.py) — không ảnh hưởng map gộp; giữ làm vết kiểm chứng.


# Snippet U14c — §7 OPEN misc O38–O60 + O63–O65

Chuỗi cơ sở trước batch: 100 mục / 2.686 dòng (U13b đã merge).

| Mục | Dòng mới | Dòng gộp | Ghi chú |
|---|---|---|---|
| O38 | 1 | 0 | 凪ふかみ08a 2426 — làm rõ đối tượng "mong" |
| O39 | 0 | 0 | Giữ "Em——em, làm được rồi!" |
| O40 | 0 | 0 | Giữ "Em nói là…" (Reina) |
| O41 | 0 | 0 | Giữ "Đối với anh" |
| O42 | 0 | 0 | Giữ (gasp sweep, JP bộ tốt đã đúng) |
| O43 | 0 | 0 | Giữ (đã sửa ở audit/moan) |
| O44 | 3 | 0 | ニイロク01 1592 khôi phục + 1593, 2337 mở rộng |
| O45 | 0 | 0 | Giữ 1913 "Tôi", 1826 "Tớ/cậu" |
| O46 | 0 | 0 | Cờ: mục không tái hiện được |
| O47 | 3 | 0 | 日々姫03 "mình"→"em" ×3 |
| O48 | 0 | 0 | Cờ: mục không tái hiện được |
| O49 | 8 | 0 | Olivy độc thoại "mình"→"tôi" ×8 |
| O50 | 1 | 0 | 凪h2 2515 あふゅいっ→"Afyui" |
| O51 | 0 | 0 | Giữ "vàng cam" + câu cụt 1938 |
| O52 | 0 | 0 | Cờ: ô JP hỏng, cần kiểm tra nguồn |
| O53 | 1 | 0 | 凪ふかみ02 1544 "cô"→"em" (người nghe Fukami) |
| O54 | 0 | 0 | Giữ 1562/1566/1947 |
| O55 | 0 | 0 | Giữ "I——a——Nkuu!!!" |
| O56 | 1 | 0 | ハチロクh8 798 れるっ→"rộp" (T77) |
| O57 | 1 | 0 | 凪ふかみh1 1303 れるっ→"rộp" (T77) |
| O58 | 0 | 0 | Giữ 2217/2238/2155 + 2874 (file thật: 稀咲02) |
| O59 | 0 | 0 | Giữ 2916–2918 |
| O60 | 0 | 0 | Giữ "Haa~"/"Hafaa~" (ngáp) |
| O63 | 0 | 0 | Giữ "Chị cứ kỳ vọng đi!" |
| O64 | 2 | 0 | 日々姫03 2368/2607 "ông nội"→"ông ngoại" |
| O65 | 0 | 0 | Giữ "bác Seki" (người lái đò) |
| **Tổng batch** | **21** | **0** | 26 mục đã quyết (9 có sửa, 17 giữ nguyên) |

**Tổng chuỗi sau batch: 160 mục / 2.731 dòng** (134 + 26 mục; 2.710 + 21 dòng mới; 0 dòng gộp. HIỆU CHỈNH bởi coordinator: snippet gốc ghi 126 mục (cơ sở cũ 100 — U14a/U14b đã gộp trước, chuỗi hiện tại là 134/2.710) — theo tiền lệ U13b/U8/U14a/U14b, 17 mục GIỮ 0 dòng vẫn tính vào chuỗi; xem ROUTE.)

Lưu ý: 17 mục giữ nguyên (0 dòng) vẫn tính vào số mục đã quyết vì đã được điều tra và quyết định giữ; nếu điều phối viên chỉ tính mục có dòng sửa vào chuỗi thì tổng mục là 109 mục / 2.707 dòng. Số dòng không đổi theo cách tính nào.
### U14c — coordinator verification notes 22/11 ~13:55 (batch verified from disk before merge):
- **§7 HOÀN TẤT.** O38–O60 + O63–O65 decided (26 items). Uncertain-rows list: 08a 2426 (O38) + Paulette 13 1357 (O39) + 08c 2030 (O22, U14b) ALL RESOLVED by evidence — none need Hieu anymore.
- O38 2426: fix làm rõ "mong như vậy" → "mong anh ấy được hạnh phúc" — KHÔNG phải bịa phần hoàn thiện: nội dung đã có nguyên văn ở dòng kề TRƯỚC 2665 (vị trí file-order 31, ngay trước 2426 ở 32: "わたしは、双鉄おにいさんにしあわせになって欲しい"); old_vn đã có "mong như vậy" — fix chỉ giải nghĩa đại từ theo dòng kề. Khác tiền lệ Hibiki h5 1189 (cắt phần bịa không có căn cứ).
- O39 1357: KEEP "Em——em, làm được rồi!" — file-order: narration 1748 (Paulette lao khỏi phòng họp, ôm Soutetsu) → 1357 → 1309 Soutetsu đáp ("Anh có xem mà. Em làm rất xuất sắc.") — outburst cá nhân với Soutetsu, "em" đúng.
- O44 extensions (1593 + 2337) ACCEPTED — cùng lỗi TW-driven 脈→希望 trong cùng file, ngoài key được trích dẫn nhưng cùng lỗi; worker đã cờ rõ.
- O49: Olivy độc thoại "mình"→"tôi" ×8 theo đếm cơ học (29 "tôi" vs 12 "mình"; 4 "mình" phản thân/thành ngữ giữ lại: 1668/1548/1466/1524).
- O64 2368/2607 "ông nội"→"ông ngoại": おじいちゃんたち = anh em Seki (độc thoại 3579: cụ Hayase Seki + anh em) — KHÁC 凪ふかみ01 1884 (F-O24-1, GIỮ "ông nội" vì じーちゃん chung chung, không định danh Seki). Hai quyết không mâu thuẫn.
- O52 FLAG → U15: JP cell れいな01 2415 bị corrupt (chứa text VN); TW là dòng khác — cần kiểm tra nguồn (TOML-2 `# JP:` comment) trước khi sửa.
- O46/O48 NOT REPRODUCIBLE (không có pattern 'N' trong ハチロク15a; key 2054 không tồn tại, đếm "em 23 vs chị 15" không khớp) — KEEP/FLAG, cần restatement chính xác trước khi xử lý lại (U15).
- CHUỖI HIỆU CHỈNH: snippet gốc 126 mục (cơ sở cũ 100) → **160 mục / 2.731 dòng** (cơ sở 134 sau U14b + 26 mục O38–O60/O63–O65, kể cả 17 mục GIỮ 0 dòng).


# Snippet — Unification batch U16 (§2 P1 + P5, Kisaki-cluster pronoun leftovers)

- U16 / §2 P1 (quyết 22/11): Soutetsu tự xưng với Kisaki "Anh" → "Tôi" toàn dự án — **47 dòng** (稀咲h2 18: 912/915/932/933/1207/1226/1230/1233/1236/1265/1271/1273/1275/1278/1302/1313/1321/1334; lr稀咲追加h 4: 1229/1287/1290/1317; 稀咲01 13: 1499/1503/1514/1515/1559/1611/1753/1796/1810/1828/1863/1945/2002; 稀咲03 4: 1335/1932/1938/1999; 日々姫10 3: 2450/2587/2653; Grand06 3: 2238/2445/2510 — 5 dòng trong số này tìm thêm sau khi sửa lỗi regex liệt kê: h2 912, 稀咲01 1611, Grand06 2238/2445/2510). Trong đó 2 dòng tsuika theo P4, không phải Soutetsu tự xưng: tsuika01 1488 câu 2 + tsuika02 1084 câu 2 ("Anh" trần → "Soutetsu", JP chủ ngữ 双鉄; chỉ đổi câu 2, câu 1 đã có tên). GIỮ có lý do: địa chỉ nhóm/không xác định được (稀咲01 1649/1655, 1799/1800, 1988/1989; 稀咲03 1974, 2135; 日々姫10 2593/2651/2737/2895; 日々姫13 1378), người nghe là Hibiki/Paulette/Reina/Olivy/Nagi/Fukami/Michiko, "anh Urakami" ngôi thứ ba, narration không người nghe (lrれいな追加02 1505/1692).
- U16 / §2 P5 (quyết 22/11): Kisaki tự xưng theo ngữ cảnh (công việc → "tôi", thân mật/dễ tổn thương → "em") — **5 dòng** (稀咲02 1900/2067/2068/2339 → "em"; Kisaki03 906 "Em ấy" → "Em" — sửa hình thức ngôi thứ ba thành ngôi thứ nhất thân mật, hiệu chỉnh xác nhận U8 O2). Các dòng còn lại đã rà đều giữ: "tôi" đúng trong bàn luận công việc, "em" đã đúng ở nhánh thân mật (Kisaki03 896/1007/1026/1189), số nhiều "chúng ta", "em ấy" ngôi thứ ba.
- GHÉP với batch đã gộp (4 dòng): h2 933/1334 (old_vn = fix U8 P3; chỉ đổi "anh"→"tôi"), tsuika01 1488 + tsuika02 1084 (old_vn = fix U7b P4; chỉ đổi câu 2). Lượt soát 2: **52/52 tái kiểm chứng, 0 loại, 0 sửa.** Khối TOML 10 file / 52 key parse-verified. Nguồn old_vn: CSV3 42 / audit 6 / unification đã gộp 4.
- Cờ cho coordinator: (F-U16-1) "anh" trần Kisaki→Soutetsu còn lại — 稀咲01 1822/1992, 稀咲03 2141/2145 + 8 dòng tên tách F-P4-1 (cần quyết chung, ứng viên U15); (F-U16-2) P6 còn sót — Grand06 2507, 稀咲02 2133/2286; (F-U16-3) 稀咲03 2038 ("anh" được cảm ơn, người nghe chưa xác định); (F-U16-4) ranh giới địa chỉ nhóm nếu muốn thống nhất câu họp thành "tôi"; (F-U16-5) giọng narration Soutetsu dùng "anh" (1505/1692); (F-U16-6) h2 1265 JP dùng ボク katakana; (F-U16-7) hiệu chỉnh xác nhận U8 O2 ở Kisaki03 906; (F-U16-8) không trùng (file,key) với U15a/U15b; (F-U16-9) caveat bản đồ ưu tiên (audit 9.242 vs 9.190); (F-U16-10) bài học regex: `\b` bỏ sót đại từ sau `\n` dạng chữ — liệt kê lại tìm thêm 41 dòng P1 + 7 dòng P5.
- File: `unification/unification-s2-kisaki-leftover-p1-p5-REVIEW.md` + `unification-s2-kisaki-leftover-p1-p5-wrong.json` (52 mục, kind="unification").

**Tổng cộng sau đợt này: 162 mục / 2.779 dòng sai (unification)** (cơ sở 160 mục / 2.731 dòng + đợt U16 2 mục mới (P1, P5) / 48 dòng mới — 4 dòng GHÉP trên fix đã gộp (h2 933/1334, tsuika01 1488, tsuika02 1084) chỉ cộng token mới, không cộng lại dòng.)
### U16 — coordinator verification notes 22/11 ~14:05 (batch verified from disk before merge):
- P1 scope EXPANDED by scan: 47 rows (not ~18+2 as estimated) — h2 18 + lr稀咲追加h 4 + 稀咲01 13 + 稀咲03 4 + 日々姫10 3 + Grand06 3 + 2 tsuika (P4). Only fix when addressee is determinably Kisaki; group/mixed/other-addressee rows KEPT with reasons (§4).
- tsuika 1488 s2 + 1084 s2 decided under P4, NOT P1 (per U8 F-P3-1): both are Kisaki speaking, JP subject 双鉄 — "Anh" trần → "Soutetsu". Only sentence 2 changed; sentence 1 already names him (changing it too would repeat the name in the same sentence). Other bare-"anh" Kisaki→Soutetsu rows (稀咲01 1822/1992, 稀咲03 2141/2145 + F-P4-1 split-names) NOT fixed here — joint decision needed (F-U16-1 → U15).
- Kisaki03 906 CORRECTS U8 O2's confirmation: old "Em ấy" was third-person for a first-person JP ボク — fix "Em ấy"→"Em" (form correction, not a pronoun-direction change).
- F-U16-10 enumeration lesson: first `\b`-regex scan missed pronouns following a literal `\n` (2-char); re-running with normalized text found +41 P1 rows (5 fixed) + 7 P5 rows (1 fixed). Later batches: normalize `\n`→space before word-boundary regexes.
- F-U16-2 P6 leftovers (Grand06 2507, 稀咲02 2133/2286) + F-U16-1 → U15 candidates.

**Tổng cộng sau đợt này: 180 mục / 3.215 dòng sai (unification)** (cơ sở 162 mục / 2.779 dòng + đợt U15b 18 mục / 436 dòng mới — 10 mục có dòng sửa (E2-Teio 8, F2 11, F3 7, F5 310, O7 37, O25 3, O46 1, M7 1, M10 1, Munakata 48, F-P4-1 9) + 8 mục 0 dòng đã quyết/ghi chú/park (F1, F4, O10, O13, O33, O52, O48, T74). 21 dòng trùng (file,key) với U15a (đang chạy) là GHÉP, không cộng thêm — U15a gộp sau sẽ chỉ cộng dòng mới của nó.)
### U15b — coordinator verification notes 22/11 ~14:20 (batch verified from disk before merge):
- verify.py PASSED 436/436 (jp/tw CSV3-exact modulo U+3000; old_vn vs merged map: moan 178 / unif 159 / csv3 91 / audit 7 / toml2-characters 1). Independent TOML-block check by coordinator: 79 blocks / 436 values / 0 mismatches, all JSON entries covered. JSON structure: 0 fix==old_vn, 0 real newlines, keys strings, 0 duplicate (file,key). Second pass 436/436 re-verified, 0 removed, 4 values corrected, 25 F5 rows added + 13 amended.
- Decisions (worker per delegation, coordinator verified): E2-Teio → "Teio" (census 12/5/2; furigana ていおう → Teiō → "Teio"; same convention as T69/T68); F1 T75 NOT expanded (ちゅず/ちゅく/ちゅりゅ keep romaji; census correction — "chụt"-family 33 vs romaji 16, U13b's "đa số là romaji" is WRONG); F2 11 real T75-misses (+2 extras); F3 7 real T77-misses (2336 keeps "ru" — terminal mora of one sliding sound); F4 1033 CONFIRMED LICKING (keep U13b "rộp"); F5 310 rows (bounded scope only); O7 37 rows ("cô"→"em" Soutetsu→Olivy 16 + →Hachiroku 20 + Nagi 2510; ハチロク13 1833 kills the work-register-only theory); O25 3 rows (lr_凪ふかみh1 1616/1687/1737 → "tớ"/"cậu"); Munakata 48 rows → "tao" (recount 49, not 55 — U9 overcounted by 6; 2094 kept — Olivy's quoted words); F-P4-1 9 rows (split-names drop "Anh"); M7 2241 "Ku" + M10 2185 "Hể!?"; O46 1 row (ハチロク15a 2345 "Olive"→"Olivy", T46 leftover); O52/O48 PARKED (not reproducible — O52 JP cell corrupt in CSV3 AND TOML-2 `# JP:`; O48 key 2054 is in 共通15, not 共通09); O10/O13/O33/T74 record-only (0 rows).
- Coordinator decisions on worker flags: (a) dialogue "ha" caps KEPT (1598/1887/2449) — はっ is an SFX token, not a VN word; 1887 already capitalizes "ah"→"Ah" for あっ in the same line, so "Ha" is consistent with F5. (b) **1855 conflict DECIDED: M15 wins** — lr追加_みくろ 1855 final value = U15a's "Nhyuuuuuuuuu!" (M15 merges split "Ưm hyu"→"Nhyu"); U15b's "Ưm Hyuuuuuuuuu!" is superseded at U15a merge (F5 explicitly deferred split-forms to the M15 sweep). (c) U15a old_vn at 1513 is STALE (pre-U7b) — U15b's old_vn is correct per merge order; composed value = U15b's fix.
- U15a overlap (21 rows, found after U15a's file landed 07:28): 10 fixes identical, 10 compose at different tokens (proposed composed values in REVIEW Phụ lục), 1 conflict (1855, decided above). At U15a merge: compose, do NOT double-count.
- Loader trap FIXED by worker (recorded for later batches): rank-−1 files must be excluded entirely — `current_unif()` starts `bestrank = -1`, so `r >= bestrank` lets an unmerged file win. Fix: load only ORDER-named files; U16's file added to ORDER.
- Flags carried forward (NOT fixed here): single-letter "a" F5 boundary (745 occurrences, undecided); T46 project-wide "Olive" sweep (~41 rows remain); ~58 remaining "Hự" rows (U12a F1); Munakata→Hachiroku "cô" ×5 (ハチロク15a 2003/2038, ハチロク15b 1520/1727/1734); 共通02 2550 addressee is NAVI; Kisaki bare-"anh" 1355/1513; M68 "rero" question at lr_ハチロクh1 1213 (for U15a); 1589's れろ tokens; 1271's ちゅずず～っ/ずりゅっ.
- GitHub: chunk 18 staged (3 U15b files + ROUTE + queue.json + queue.md), head verified live 5180dea1 before staging; push STILL BLOCKED (combined approval expired — do NOT push until Hieu approves).

**Tổng cộng sau đợt này: 235 mục / 3.610 dòng sai (unification)** (cơ sở 180 mục / 3.215 dòng + đợt U15a 55 mục mới / 395 dòng mới — 60 mục đã quyết, trừ 5 đã tính (M7/M10/M15 U12a, M3 U11b, F5 U15b); 418 dòng giao trừ 23 dòng trùng U15b/U16 (16 bỏ + 7 GHÉP không cộng lại).)
### U15a — coordinator verification notes 22/11 ~14:40 (batch verified from disk before merge):
- Worker delivered 418 entries / 104 files; coordinator re-verified independently: jp/tw CSV3-exact 0 lệch, old_vn vs merged map 4 lệch (xem dưới) — sau hiệu chỉnh: JSON gộp 402 dòng, jp/tw/old_vn 0 lệch, 0 fix==old_vn, 0 newline thật, 0 trùng (file,key). TOML blocks §7: 104 blocks / 402 key = JSON 402/402 (re-parse tomllib). Second pass worker 418/418/0/55. Mechanical checks `_u15a_verify_m.py`: 3 "problem" đều là artifact của script kiểm, không phải lỗi fix (ハチロク06 2322 "Ufu" — JP うふっ = 2 mora, ngoại lệ có chủ ý; ハチロクh7 759 "Nkuuuu~~" đúng — JP んくぅぅぅ～～っ = 4u + ~~, script kiểm đếm thừa 1u; 日々姫h5 1265 tồn tại — file đúng 白濁絵の具の射精会, script kiểm ghi sai tên file; "Nbuuuuuu" = 6u đúng JP).
- Decisions (worker per delegation, coordinator verified): M7 60 rows (recount 60, not 59 — U12a missed lr_日々姫h2 1159, `\n` before くっ); M15 113 rows (ん+consonant → single romaji token; ん contributes no vowel); M24 97 rows (laughter caps per F5; 19 rows keep literal `"…"` quotes — real text, verified in CSV3 AND disk TOML); HAS-RUN 99 rows (M14 count corrections; v2 106 FIX/28 KEEP, 103 unique − 4 hand-overridden = 99); M10 2 rows (929/957 → "Fue"); F5 4 rows; singles M18/M27/M28/M37/M47/M51/M61/M63, M62 ×2; G15 29 rows (drop leaked ruby `[x,n]`); standalones Grand 11 2485 (restore dropped 御一夜), P03 1728 (閉塞 gloss → "Đóng đường"), F-T56-1 仲国08 2823 (→ "Trung Quốc"), P07 2311 (列車 gloss → "đoàn tàu"); 40 items KEEP 0 rows (incl. M3 scream boundary NOT extended to 175 non-H rows; M55/M56 NOT reproducible; G12 all correct; G16 日々姫05 1909 deliberate audit restoration).
- Overlaps (worker missed 2 — coordinator found via old_vn re-verification): 23 rows total (21 U15b + 2 U16). 16 DROPPED (composed == earlier fix): 10 IDENT with U15b + 5 subsumed U15b (1084 "Kuuun", 2241 "Ku", 1616 "Ufufu", 1513 "Fufu", 1092 "Nfufuuuu~") + 1 subsumed U16 (1900 "Fufu"). 7 KEPT as composed (old_vn = earlier fix, fix = composed value — each verified by 2 independent constructions): 1096, 1162, 1857, 1056, 2265 (U15b), 912 (U16, M63 "Ư" + P1 "Tôi"), 1855 (CONFLICT — M15 wins per U15b decision: "Nhyuuuuuuuuu!"). U15a old_vn at 1513 confirmed STALE (pre-U7b); 1513 dropped.
- old_vn correction 1339 (M7, coordinator): worker's old_vn "——Ư, hự——" matches NO layer (CSV3 "——hự——"; no audit/moan/unif entry anywhere — "Ư," was worker-invented). old_vn corrected to CSV3 value; fix kept "Ư, Ku" (correct per JP "――っ、くっ――": っ→"Ư" gasp + くっ→"Ku").
- Item-count correction: 60 decided − 5 already counted (M7/M10/M15 U12a, M3 U11b, F5 U15b) = 55 new items. Worker Kết bài "39 mục giữ nguyên" is a slip (§4 lists 40 keeps).
- Flags carried forward (NOT fixed here): M18 ~25-row "append Kuuun" expansion not taken; M7 scope questions (7 （ ） rows, 15 non-H "hự" rows, lr_ふかみh1 1365 "nhự"); broader F5 sweep; ふかみh2 1000 "chụt u u"; T75/T77/T78 appendix misses + 帝央 (already decided in U15b — Teio); HAS-RUN out-of-scope observations; single-letter "a" F5 boundary (745, from U15b); T46 "Olive" sweep ~41 (U15b); ~58 "Hự" rows (U12a F1, partially addressed by M7 here — 60 done, remainder per §5).
- GitHub: chunk 19 staged (3 U15a files + ROUTE + queue.json + queue.md), head verified live 5180dea1 before staging; push STILL BLOCKED (combined approval expired — do NOT push until Hieu approves).
- **QUEUE EMPTY except parked items** (§5 tag sweep B19, G13/G14, T80, T76) — next: TOML rebuild.

