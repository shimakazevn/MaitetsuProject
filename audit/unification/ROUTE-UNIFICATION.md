# ROUTE-UNIFICATION — Maitetsu: Last Run!! unification pass

Single pass approved 20/11 ~19:15, ordered 22/11 ~10:31 ("Gộp danh sách ngay, chạy khi rên xong") + 22/11 ~11:00 ("Chạy đợt thống nhất luôn đi").
List: `~/workspace/maitetsu-pilot/UNIFICATION-LIST.md` (304 items: DECIDED 142 incl. 8 keep / OPEN 154 / PARKED 8).
Brief: `~/workspace/maitetsu-pilot/unification/UNIFICATION-BRIEF.md`.
Base state at pass start (22/11 ~11:00): audit COMPLETE 216/216, 9,927 wrong; moans COMPLETE 64/64, 1,512 rows; GitHub head 8eae66a5; sync record 93 entries.

## Totals chain

**Tổng cộng sau đợt này: 18 mục / 479 dòng sai (unification)** (cơ sở 2 mục / 226 dòng + đợt U1a T1 Ohimitera 00–02: 221 dòng (cùng mục T1) + đợt U10 §6 file-specific DECIDED: 16 mục / 32 dòng — gộp 22/11 ~11:20, parent kiểm chứng: U1a JSON 221 = TOML block 221, U10 JSON 32 = TOML block 32 (26 script + 6 [characters]/[character_subs]), jp/tw CSV3-exact, old_vn khớp map hiện tại, second pass 221/221 + 32/32)

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
