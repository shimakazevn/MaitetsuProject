# Moan fix — lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

**File:** `lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml` — route 02_Hibiki (H-scene 3 người Hibiki + Fukami + Soutetsu, "thay cho bé Nagi")
**Đường dẫn TOML:** `sources/toml2/translation_toml/02_Hibiki/lr_#U65e5#U3005#U59eb#U3075#U304b#U307fh1_#U51ea#U3061#U3083#U3093#U306e#U4ee3#U308f#U308a.txt.toml`
**MD5 TOML:** `1975c8fad55084e81cc0031905781f87` — khớp md5 audit, 1 bản duy nhất, không có file trùng.
**CSV3:** 1 bộ duy nhất (485 dòng), 0 khóa trùng, 0 VN trống. Khớp phẳng VN với TOML 485/485 (theo audit).

## Đã đọc

- **Đã đọc: 485/485 dòng script** (độc thoại 210, Soutetsu 85, Hibiki 96, Fukami 94), đọc từng dòng đối chiếu JP + TW.
- Audit của file này đã gộp: 68 sai (14,0%), trong đó 48 dòng gasp っ (39 raw-tsu + 8 lost-gasp + 1 kinship+lost-gasp, gồm 3 dòng sweep bỏ sót 1327/1384/1700) — **không đụng lại bất kỳ dòng gasp Ư nào**; 6 lỗi đếm nguyên âm ở tiếng rên (1357, 1358, 1359, 1447, 1463, 1475) đã kiểm chứng lại bằng máy ở đợt này (xem "Kiểm chứng audit").

## Kho rên (moan inventory)

- Họ はぁ/はあ (thở dốc 2 a): 10 dòng — **sửa cả 10** (933, 1385, 1389, 1422, 1423, 1505, 1740, 1741, 1742, 1743). (1536 có はあれだけ là từ "như thế", không phải rên.)
- Họ ひゃ/ひゅ/ひあ/きゃ: 9 dòng (1319, 1321, 1327, 1328, 1329, 1330, 1331, 1333, 1336) — đã romaji đúng hết, 0 sửa.
- Họ fa/fu (ふぁ/ふあ/ふぇ/ふや): 16 dòng — sửa 1 (1358, đuôi "ưm" trộn).
- Cười (ふふ/うふふ/んふふ/あはは/えへへ): 10 dòng — sửa 1 (1440, "ư fufu" tách).
- Rên ngắn あ/う/ん/く/は/え: sửa 2 (1334 やっ→"Á", 1406 あぁ→"ừm").
- Hôn/mút ちゅ/じゅ/ごく: 42 dòng theo mẫu quét — sửa 1 (1475, audit đếm thiếu 1 u).
- SFX （） độc thoại: 66 dòng — **0 sửa**, theo quyết định của audit (§537): công thức đếm nguyên âm chỉ áp cho tiếng rên có giọng, không áp cho SFX hành động; giữ nguyên onomatopoeia Việt ("Phập", "Trơn tuột", "Tuốt", "Phụt"...).
- Gasp っ: 48 dòng đã có fix trong audit — không đụng. Không có dòng "Kh" khóa nào bị đổi.

## Từng dòng sửa (15)

### Key 933 — 日々姫 — vowel-count

- JP: `「っ――っ――～～～っ！　――ぁ――はぁっ、はぁっ」`
- TW: `「——嗚～～～！　——啊——蛤啊，蛤啊」`
- Cũ (audit): `「Ư――Ư――~~~Ư! ――A――hà, hà」`
- Mới: `「Ư――Ư――~~~Ư! ――A――hàa, hàa」`
- Lý do: はぁっ = は+ぁ = 2 a → "Hàa" (bản cũ "hà" thiếu 1 a; tiền lệ hachiroku-h9: はぁ = 2 a → "haa"). Giữ nguyên phần gasp Ư của audit; giá trị này xây trên fix audit, chỉ đổi đúng token rên.

### Key 1334 — ふかみ — sound-loss

- JP: `「やっ！？　激しっ――ですっ――ふあっ！　あっ！」`
- TW: `「呀！？　太激——烈了——呼啊！啊！」`
- Cũ: `「Á!? Mãnh liệt――quá――fua! A!」`
- Mới: `「Ya!? Mãnh liệt――quá――fua! A!」`
- Lý do: やっ → "Ya" — "Á" mất hẳn phụ âm y (tiền lệ ポーレットh3 "'Á' cho きゃっ/ひゃっ/やっ" là lỗi mất phụ âm; Hibiki h6 2082 やっ→"Ya"). Giữ "fua"/"A" như cũ.

### Key 1358 — ふかみ — mixed-rendering

- JP: `「ふぁふゅぅぅぅぅぅぅぅぅぅぅぅぅぅっんんっ！！」`
- TW: `「呼啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊！！」`
- Cũ (audit): `「Fuafyuuuuuuuuuuuuuuưm!!」`
- Mới: `「Fuafyuuuuuuuuuuuuuunn!!」`
- Lý do: một âm rên dài duy nhất nhưng đuôi んんっ lại diễn bằng tiếng Việt "ưm" chen vào chuỗi romaji — trộn 2 hệ trong một âm (tiền lệ ポーレットh2 sửa 7 dòng "Ưm + romaji"). Sửa đuôi thành romaji "nn" (んん = 2 morae → "nn"; cùng quy ước coda romaji "n" của 1357/1328 trong chính file này). Đếm u giữ nguyên đúng audit: 15 u (ふぁ 1 + ふゅ 1 + ぅ×13), đã đếm máy. Giá trị này xây trên fix audit, chỉ đổi đúng đuôi.

### Key 1385 — 日々姫 — vowel-count

- JP: `「はうっ！　あっ！　はぁっ――はあっ！！！！」`
- TW: `「哈嗚！啊！蛤啊——蛤啊！！！！」`
- Cũ: `「Hau! A! Hà――hà!!!!」`
- Mới: `「Hau! A! Hàa――hàa!!!!」`
- Lý do: はぁっ và はあっ đều = 2 a → "Hàa"/"hàa" (bản cũ 1 a). Giữ "Hau" (はうっ) và "A" như cũ.

### Key 1389 — 日々姫 — vowel-count

- JP: `「えっ！？　あっ！　わっ――――はぁっ……はぁっ。\nおちんちんの、われめ――こんなに――くぱ、くぱっ」`
- TW: `「哎！？　啊！　哇——蛤啊……蛤啊。小雞雞的裂縫——張開得——這麼大」`
- Cũ: `「Hả!? A! Wa――――Hà…… hà.\nRãnh của, chim――đang――mở ra, khép lại thế này.」`
- Mới: `「Hả!? A! Wa――――Hàa…… hàa.\nRãnh của, chim――đang――mở ra, khép lại thế này.」`
- Lý do: はぁっ ×2 = 2 a mỗi âm → "Hàa"/"hàa". Giữ "Hả"/"A"/"Wa" như cũ.

### Key 1406 — 双鉄 — sound-loss

- JP: `「っ！！？　――あ、あぁ」`
- TW: `「唔！！？　——啊，嗯」`
- Cũ (audit): `「Ư!!? ――A, ừm」`
- Mới: `「Ư!!? ――A, aa」`
- Lý do: あぁ là âm "a" dài (2 a), không phải âm mũi — "ừm" diễn sai hẳn âm (JP thắng TW 嗯). Sửa thành "aa". Giữ nguyên Ư đầu dòng của audit; giá trị này xây trên fix audit.

### Key 1422 — 双鉄 — vowel-count

- JP: `「ぁ――あっ――あ……ん――（ごくっ）――\nはぁっ――はあっ――はあっ――はあっ――」`
- TW: `「啊——啊——啊——嗯——（咽口水）——蛤啊——蛤啊——蛤啊——蛤啊——」`
- Cũ: `「A――a――a…… n――（Ực）――\nHà――hà――hà――hà――」`
- Mới: `「A――a――a…… n――（Ực）――\nHàa――hàa――hàa――hàa――」`
- Lý do: はぁっ + はあっ×3 = 2 a mỗi âm → "Hàa"/"hàa" ×4. Giữ "A/a/n/Ực" như cũ.

### Key 1423 — 双鉄 — vowel-count

- JP: `「ぁ――っ――ぁ――はぁっ――んっ」`
- TW: `「啊——啊——蛤啊——嗯」`
- Cũ (audit): `「A――Ư――a――hà――ưm」`
- Mới: `「A――Ư――a――hàa――ưm」`
- Lý do: はぁっ = 2 a → "hàa". Giữ nguyên Ư của audit và "ưm" cho んっ; giá trị này xây trên fix audit, chỉ đổi đúng token rên.

### Key 1440 — ふかみ — mixed-rendering

- JP: `「あっ……うふふっ！\n双鉄おにいさん、おっきくなってきちゃいましたねぇ」`
- TW: `「啊……唔呵呵！雙鐵哥哥，你變大了呀」`
- Cũ: `「A…… ư fufu!\nAnh Soutetsu, nó to lên rồi kìa.」`
- Mới: `「A…… ufufu!\nAnh Soutetsu, nó to lên rồi kìa.」`
- Lý do: うふふっ là một tiếng cười duy nhất — bản cũ tách thành "ư" (Việt) + "fufu" (romaji), trộn 2 hệ trong một âm. Gộp thành "ufufu" (viết thường giữa câu, đúng tiền lệ 1438 "A…… ufufu――" trong chính file này; dạng viết hoa "Ufufu" chỉ dùng ở đầu dòng như 1395/1399).

### Key 1475 — ふかみ — vowel-count (sửa giá trị audit)

- JP: `「ん――ちゅっ――ちゅむっ――ちゅう――れるっ――\nれりゅううっ――じゅるっ――じゅ――ずりゅ――るっ」`
- TW: `「嗯——啾——啾唔——啾嗚——滋溜——滋溜——啾嚕——啾——滋溜——滋溜」`
- Cũ (audit): `「Ưm――chụt――chùn chụt――chụt――rê ru――\nrê ryuu――chùn chụt――chu――zuryu――ru」`
- Mới: `「Ưm――chụt――chùn chụt――chụt――rê ru――\nrê ryuuu――chùn chụt――chu――zuryu――ru」`
- Lý do: token là れりゅううっ = りゅ (1 u) + う×2 = 3 u → "ryuuu". Audit đếm nhầm thành "りゅう = 2 u" (ghi chú trong review audit dòng 523) nên fix audit "ryuu" thiếu 1 u. Cùng công thức với 1461 trong file này: ずりゅうううっ → "zuryuuu" (1+3=4 u ✓). Giá trị này xây trên fix audit, chỉ thêm 1 u đúng chỗ.

### Key 1505 — 双鉄 — vowel-count

- JP: `「ぷぁっ――あっ――はぁっ――はあっ――」`
- TW: `「噗啊——啊——蛤啊——蛤啊——」`
- Cũ: `「Pua――a――hà――hà――」`
- Mới: `「Pua――a――hàa――hàa――」`
- Lý do: はぁっ và はあっ = 2 a mỗi âm → "hàa" ×2. Giữ "Pua"/"a" như cũ.

### Key 1740 — 日々姫 — vowel-count

- JP: `「はあっ――はあっ――はあっ――はあっ――」`
- TW: `「蛤啊——蛤啊——蛤啊——蛤啊——」`
- Cũ: `「Hà――hà――hà――hà――」`
- Mới: `「Hàa――hàa――hàa――hàa――」`
- Lý do: はあっ ×4 = 2 a mỗi âm → "Hàa"/"hàa" ×4.

### Key 1741 — 日々姫 — vowel-count

- JP: `「はぁっ、はぁっ、はぁっ、はぁっ――もう、すぐっ、\nもうすぐっ――にぃにの――射精っ――」`
- TW: `「蛤啊、蛤啊、蛤啊、蛤啊——很快就要、很快就要——阿哥——要射精了——」`
- Cũ: `「Hà, hà, hà, hà――sắp, rồi,\nsắp rồi――anh hai sắp――xuất tinh――」`
- Mới: `「Hàa, hàa, hàa, hàa――sắp, rồi,\nsắp rồi――anh hai sắp――xuất tinh――」`
- Lý do: はぁっ ×4 = 2 a mỗi âm → "Hàa"/"hàa" ×4. Giữ nguyên phần còn lại.

### Key 1742 — 双鉄 — vowel-count

- JP: `「はぁっ！　はぁっ！　はあっ！　はぁっ！！！！」`
- TW: `「蛤啊！　蛤啊！　蛤啊！　蛤啊！！！！」`
- Cũ: `「Hà! Hà! Hà! Hà!!!!」`
- Mới: `「Hàa! Hàa! Hàa! Hàa!!!!」`
- Lý do: はぁっ×3 + はあっ×1 = 2 a mỗi âm → "Hàa" ×4.

### Key 1743 — 双鉄 — vowel-count

- JP: `「はぁっ！　はあっ！　はあっ！　はぁっ！」`
- TW: `「蛤啊！蛤啊！蛤啊！蛤啊！」`
- Cũ: `「Hà! Hà! Hà! Hà!」`
- Mới: `「Hàa! Hàa! Hàa! Hàa!」`
- Lý do: はぁっ×2 + はあっ×2 = 2 a mỗi âm → "Hàa" ×4.

## Kiểm chứng audit (các fix rên của audit đã đúng)

Đếm máy độc lập từ JP, tất cả đều khớp nên giữ nguyên, không sửa lại:

- 1357: JP 18 a — fix audit "Fuaaaaaaaaaaaaaaaaaan!" đúng 18 a (cũ 23 a).
- 1359: JP 9 a (ふや 1 + ぁ×4 + あ×4) — fix audit "Fuyaaaaaaaaa!" đúng 9 a (cũ 8 a).
- 1447: JP ああっ = 2 a — fix audit "Aa!!!!" đúng.
- 1463: JP ぅ 1 + ぁぁ 2 + あ×9 = 11 a — fix audit "Ư a a a a a a a a a a a" đúng 11 a (cũ 10 a).
- 1328: JP ぅ×16 — VN cũ "Hyauuuuuuuuuuuuuuuu~~~n!" đúng 16 u, không cần sửa (audit đã ghi nhận).
- 1371: JP くああああああっ = 6 a — VN "Kuaaaaaa" đúng 6 a.
- 1446: JP ぁぁぁああああああああ = 11 a — VN "A a a a a a a a a a a" đúng 11 a.
- 1461: れろおおおっ = 4 o → "roooo" ✓; ずりゅうううっ = 4 u → "zuryuuu" ✓.
- ひゃ/きゃ: 1319/1321/1328/1329/1330/1331/1336 đã romaji đúng; 1327 "HyauƯ" và 1333 "Hyan" là fix audit đúng (gasp Ư + Hyan cho ひゃん).

## Giữ nguyên có lý do (không sửa)

- **ふっ → "Hư"/"hư" (1350, 1479):** quy ước nhất quán trong file này; các file khác dùng "phù" (mẫu 凪ふかみh1 1227) hoặc "fu" (lr-nagifukami-h1) — để đợt thống nhất chốt một kiểu (xem cờ F1). Không đổi trong đợt moan.
- **くっ/く―― → "ư" (1265, 1432, 1698):** nhất quán trong file; tiền lệ hachiroku-h9 giữ "くっ→'ư'" với đúng lý do này.
- **1931 ああ―― → "A――":** đây là tiếng thở dài/nhận ra trong độc thoại ("A――Hibiki cũng vậy"), không phải rên — giữ theo tiền lệ ポーレットh2/h3 (ああ thở dài giữ "A"/"À"); dạng "Aa" của lr-reinah1 chỉ áp cho ああ―― trong ngữ cảnh rên ("ああ――気持ちいい").
- **1469/1497/1498/1502 ああ → "Ừ":** ああ đồng ý — giữ.
- **1501/1503/1408 hơi thở すー/はー → "hít/thở":** diễn bằng từ nghĩa, quy ước nhất quán trong file — giữ.
- **SFX （） 66 dòng:** giữ nguyên theo quyết định audit §537 (xem cờ F2/F3).
- **Gasp Ư (48 dòng audit) và "Kh":** không đụng dòng nào.
- **ふっ tách fa "phù——a" / "phù, a":** file này không có dạng tách fa; các dòng ふぁ chưa tách đã romaji đúng ("Fua").

## Cờ (để đợt thống nhất / parent, không quyết ở đây)

- **F1 — quy ước hơi thở ふっ:** file này "Hư"/"hư" (1350, 1479); mẫu 凪ふかみh1 giữ "phù"; lr-nagifukami-h1 dùng "fu". Đợt thống nhất cần chốt một kiểu cho ふっ/ふ.
- **F2 — độ dài SFX （）:** 2467 （ずりゅううううううううううっっっっ） → "（Trơn tuột!!!!!!）" ngắn hẳn, trong khi 2468 (JP tương tự) → "（Trơn tuộtttttttt!!!!）" kéo dài bằng t; 2459/2457/2473 （ずぶううううううううう / ぎゅううううううううううう） → "（Phập!…）" ngắn. Audit §537 đã quyết giữ nguyên nhóm này (công thức đếm nguyên âm không áp cho SFX hành động). Nếu đợt thống nhất muốn áp công thức cho cả SFX, xét lại nhóm này cùng cờ 6 của h9.
- **F3 — 2451 （ずっ――くっ） → "（Phập――Ư）":** くっ diễn thành "Ư" trong SFX （） — giữ theo nhóm audit, nhưng lạ (mất phụ âm k); xét cùng F2.
- **F4 — 1475 audit đếm sai:** fix audit "ryuu" thiếu 1 u (đọc れりゅううっ thành れりゅうっ); giá trị moan "ryuuu" thay thế fix audit ở đợt thống nhất.
- **F5 — 5 dòng chồng audit (933, 1358, 1406, 1423, 1475):** giá trị moan xây trên fix audit (giữ nguyên phần gasp Ư và các sửa khác của audit, chỉ đổi đúng token rên) — ở đợt thống nhất áp giá trị moan thay fix audit cho 5 key này. 10 dòng còn lại xây trên VN cũ CSV3.

## Lượt soát 2 (đọc lại toàn bộ fix đối chiếu JP)

- **Tổng: 15 / tái kiểm chứng: 15 / bỏ: 0 / sửa: 0.**
- Kiểm chứng máy: JSON 15 mục, khóa string, jp/tw/old_vn khớp CSV3 15/15; khối TOML 15 khóa parse bằng tomllib, 0 sai lệch giá trị so với JSON; mỗi fix chỉ khác cơ sở (VN cũ hoặc fix audit) đúng chỗ token mục tiêu (đã in diff từng dòng lúc dựng).
- Đếm nguyên âm kiểm chứng độc lập: 1358 = 15 u (1+1+13) ✓; 1475 = 3 u (りゅ 1 + う×2) ✓; はぁっ/はあっ = 2 a mỗi âm, 10 dòng × token đều đủ 2 a sau fix ✓; 1406 あぁ = 2 a ✓; 1334 やっ → "Ya" đủ phụ âm y ✓.

## Khối TOML (đã kiểm parse, 15 khóa, 0 sai lệch)

```toml
933 = "「Ư――Ư――~~~Ư! ――A――hàa, hàa」"
1334 = "「Ya!? Mãnh liệt――quá――fua! A!」"
1358 = "「Fuafyuuuuuuuuuuuuuunn!!」"
1385 = "「Hau! A! Hàa――hàa!!!!」"
1389 = "「Hả!? A! Wa――――Hàa…… hàa.\\nRãnh của, chim――đang――mở ra, khép lại thế này.」"
1406 = "「Ư!!? ――A, aa」"
1422 = "「A――a――a…… n――（Ực）――\\nHàa――hàa――hàa――hàa――」"
1423 = "「A――Ư――a――hàa――ưm」"
1440 = "「A…… ufufu!\\nAnh Soutetsu, nó to lên rồi kìa.」"
1475 = "「Ưm――chụt――chùn chụt――chụt――rê ru――\\nrê ryuuu――chùn chụt――chu――zuryu――ru」"
1505 = "「Pua――a――hàa――hàa――」"
1740 = "「Hàa――hàa――hàa――hàa――」"
1741 = "「Hàa, hàa, hàa, hàa――sắp, rồi,\\nsắp rồi――anh hai sắp――xuất tinh――」"
1742 = "「Hàa! Hàa! Hàa! Hàa!!!!」"
1743 = "「Hàa! Hàa! Hàa! Hàa!」"
```

## Kết bài

File lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml đã đọc hết 485/485 dòng, sửa 15 dòng rên: 11 lỗi đếm nguyên âm (chủ yếu là はぁっ/はあっ thiếu 1 a — 10 dòng — cộng 1475 audit đếm thiếu 1 u), 2 lỗi mất âm (やっ→"Á", あぁ→"ừm"), 2 dòng trộn 2 hệ diễn trong một âm (1358 đuôi "ưm", 1440 "ư fufu"). Không đụng gasp Ư (48 dòng audit), không đụng "Kh", không đụng SFX （） theo quyết định audit §537. 5 giá trị moan xây trên fix audit (933, 1358, 1406, 1423, 1475), 10 giá trị xây trên VN cũ. Lượt soát 2: 15/15 tái kiểm chứng, 0 bỏ, 0 sửa. Khối TOML 15 khóa parse được, 0 sai lệch giá trị.
