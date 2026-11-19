# Dual CSV row sets — 10 files (verified by parent 19/11 against TOML-2)

CSV3 ("Trang tính 3") carries TWO row sets for 10 files: same keys, different content.
In every case the set labelled with the file's "home" folder is STALE (only 0–31 of
hundreds of VN values match the TOML); the set labelled with the OTHER folder matches
the TOML almost completely. The stale set must be DROPPED before any TOML rebuild,
or hundreds of correct lines get overwritten with the old version.

Match counts = VN flat-match (literal `\n` normalised to space) vs the TOML script values.

| File | TOML copy | STALE set (drop) | GOOD set (use) | Good-set match |
|---|---|---|---|---|
| lr_ふかみh1_ふかみうさぎのたまご | 07_Nagi_Fukami (289) | 07_Nagi_Fukami 3/289 | 11_Other | 288/289 |
| lr_ふかみh2_セックスの意味 | 07_Nagi_Fukami (291) | 07_Nagi_Fukami 5/291 | 11_Other | 290/291 |
| ふかみh1_ともはり練習 | 07_Nagi_Fukami (272) | 07_Nagi_Fukami 1/272 | 11_Other | 272/272 |
| ふかみh2_homesweethome | 07_Nagi_Fukami (301) | 07_Nagi_Fukami 12/301 | 11_Other | 300/301 |
| ふかみh3_夏休みの最後の日の、前の日 | 07_Nagi_Fukami (649) | 07_Nagi_Fukami 7/649 | 11_Other | 649/649 |
| グランドリライト08_ふかみ | 09_Grand + 07_Nagi_Fukami (485 each) | 07_Nagi_Fukami 0/485 | 09_Grand | 481/485 |
| 共通02_日々姫と真闇と人形と | 00_Common (467) | 00_Common 31/467 | 02_Hibiki | 466/467 |
| 共通03_ハチロクとナビ | 00_Common (315) | 00_Common 28/315 | 01_Hachiroku | 315/315 |
| 共通04_キハ07。ポーレットとれいな | 00_Common (385) | 00_Common 15/385 | 03_Paulette | 384/385 |
| 共通06_8620を探せ | 00_Common (444) | 00_Common 20/444 | 01_Hachiroku | 442/444 |

Total stale rows to drop before rebuild: 3,898 (289+291+272+301+649+485+467+315+385+444).

Rule for all future audits: when a file has 2 CSV sets, determine the good set by
VN flat-match against the TOML and audit ONLY that set. Never trust the folder label.
Real row counts: 共通02 = 467 (not 934), 共通03 = 315 (not 630), 共通04 = 385 (not 770),
共通06 = 444 (not 888). Scan found 10 dual-set files out of 214 script files in CSV3 —
no other file has 2+ sets (verified 19/11).
