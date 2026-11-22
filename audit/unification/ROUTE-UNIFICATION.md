# ROUTE-UNIFICATION — Maitetsu: Last Run!! unification pass

Single pass approved 20/11 ~19:15, ordered 22/11 ~10:31 ("Gộp danh sách ngay, chạy khi rên xong") + 22/11 ~11:00 ("Chạy đợt thống nhất luôn đi").
List: `~/workspace/maitetsu-pilot/UNIFICATION-LIST.md` (304 items: DECIDED 142 incl. 8 keep / OPEN 154 / PARKED 8).
Brief: `~/workspace/maitetsu-pilot/unification/UNIFICATION-BRIEF.md`.
Base state at pass start (22/11 ~11:00): audit COMPLETE 216/216, 9,927 wrong; moans COMPLETE 64/64, 1,512 rows; GitHub head 8eae66a5; sync record 93 entries.

## Totals chain

**Tổng cộng sau đợt này: 21 mục / 585 dòng sai (unification)** (cơ sở 18 mục / 479 dòng + đợt U6 §2 P2/P14/O1: 3 mục / 106 dòng — gộp 22/11 ~11:25, parent kiểm chứng: U6 JSON 106 = TOML block 106 (30 file, 1 fence 30 [script]), jp/tw CSV3-exact, old_vn khớp map hiện tại (102 CSV3 + 3 audit + 1 U1c), diff chỉ đổi đại từ (giữ 'Cô bé'/'công' nguyên — kiểm chứng từng dòng), second pass 106/106; Grand 01 2181 fix U6 đã bao gồm fix U1c)

## Decisions log (coordinator decisions on OPEN items — evidence in batch reviews)

### U1b — T1 Ohimitera (folders 03–06): 52 dòng / 12 file (Paulette 11, Reina 11, Mayami 26, Kisaki 4). GitHub: xem sync record.

## PARKED for Hieu / in-game (not touched in this pass)

- §5 tag sweep S1–S5, S7 (B19 gate: Paulette 13 key 1596 in-game check).
- §4 G13/G14 (tag sweep items).
- §1 T80 (fa/fu font check in-game).

## Merged batches

- U2a (22/11 ~11:15, worker decided per delegation, parent spot-verified): 御鉄 = 御一夜鉄道 → "Đường sắt Ohitoyo" (9 rows; ruby [おんてつ,1] + TW 御鐵 + company context). オヒトヨ/おひとよ kana = same as kanji 御一夜 (12 rows; TW writes 御一夜).
- U1c flag (22/11 ~11:15, NOT fixed — for leftovers batch U15): Grand 11 key 2485 — JP/TW have 御一夜 twice, VN renders only the second (first dropped); pre-existing omission the audit passed.
- T1 reconciliation (22/11 ~11:15): project-wide Ohimitera remainder was 311 (not §0's 333 — consolidation map had 9,190 audit pairs vs 9,200 mapped here + moan fixes). U1b 52 + U1c 38 merged; remaining 221 in folders 00–02 (U1a running).


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
