# Audit — 凪ふかみh1_修学旅行の夜.txt.toml (07_Nagi_Fukami)

- File: `凪ふかみh1_修学旅行の夜.txt.toml` — route 07_Nagi_Fukami, 1 bản duy nhất.
- Disk: `sources/toml2/translation_toml/07_Nagi_Fukami/#U51ea#U3075#U304b#U307fh1_#U4fee#U5b66#U65c5#U884c#U306e#U591c.txt.toml`
- md5: `50c203c62f6e830c5e30413e09083b02` — không có file trùng (chỉ xuất hiện 1 lần trong thư mục 07_Nagi_Fukami; không nằm trong 11 nhóm trùng của dự án).
- Nội dung: đêm tu nghiệp (修学旅行) của ba người — ăn tối ba ba (すっぽん), Soutetsu lần đầu thấy mình "nóng ran" sau khi ăn ba ba, rồi ba người lần đầu làm tình cùng nhau (Nagi trước, Fukami sau), kết bằng thỏa thuận "làm công bằng, lần lượt từng người" cho lần tới.
- Phương pháp: đọc từng dòng 318/318 đối chiếu JP + TW (CSV3), kiểm chứng sweep gasp, kiểm tra %l, kiểm tra trùng khóa / lệch dòng / mồ côi / chưa dịch / nhiễm chéo.

## 1. Tổng quan

- Dòng script: **318** (độc thoại 148, ふかみ 63, 凪 61, 双鉄H 46).
- CSV3: 1 set duy nhất, 318 khóa, 0 trùng khóa, 0 VN trống. TOML parse được, 318 khóa khớp CSV3 tuyệt đối về khóa; VN trong TOML khớp CSV3 tuyệt đối (131 khớp đúng, 185 dạng làm phẳng `\n` → khoảng trắng theo kiểu TOML-2, 2 dòng 1243/1433 chỉ khác vị trí khoảng trắng làm phẳng — không phải lỗi).
- `[selections]`: rỗng `{}`. Thẻ `%l`: không có thẻ nào trong file (cả JP lẫn VN), không có lỗi thẻ.
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**

## 2. Kết quả: 8/318 (2,5%)

Phân loại (8):

- Đại từ: **1** — Fukami tự xưng "tớ" với Nagi (1332; chuẩn dự án là "mình", trong chính file này 1200 cũng dùng "mình" với Nagi).
- Gasp (っ bị mất tiếng): **1** — あんっ → "A" (1280; âm ん mất hẳn, không có dấu câu nào giữ lại tiếng っ).
- SFX: **5** — độ dài hơi thở ふー sai số lượng (1238, 1252); "sột soạt" (tiếng sột soạt khô) dùng sai cho 3 tiếng ướt じゅるんっ/くちゅっ/じゅぶっ (2026, 2027, 2043).
- Lỗi gõ: **1** — dấu nháy đơn thừa sau "nhất" (939).

Soutetsu "anh" với Nagi/Fukami đúng toàn file, không có đại từ nào sai; độc thoại "tôi" đúng; Nagi→Fukami "bé" đúng; Fukami→Nagi "cậu" đúng; Fukami tự xưng "em" với Soutetsu và "mình" với Nagi đúng (trừ 1332).

## 3. Danh sách sửa (8)

### 3.1. Đại từ

**Key 1332 [ふかみ] — pronoun.** JP: `「凪ちゃん、ね？　平気――わたしも、一緒だからっ」` / TW: `「小凪，沒關係，沒事的……有我在一起呢」` — Cũ: `「Bé Nagi, nhé? Không sao đâu——vì tớ cũng, ở cùng cậu mà.」` → Mới: `「Bé Nagi, nhé? Không sao đâu——vì mình cũng, ở cùng cậu mà.」`. (Fukami nói với Nagi; chuẩn dự án: Fukami tự xưng "mình" — trong chính file này 1200 "thì phần của, mình" cũng với Nagi. "Tớ" là lần duy nhất Fukami dùng "tớ" trong file.)

### 3.2. Gasp

**Key 1280 [ふかみ] — gasp.** JP: `「あんっ」` / TW: `「啊」` — Cũ: `「A」` → Mới: `「An」`. (あんっ là tiếng rên mũi + っ cắt ngang; VN "A" làm mất hẳn âm ん và không có dấu câu nào giữ lại tiếng っ — sweep bỏ sót dòng này. "An" khôi phục âm ん; chữ "n" cuối từ vốn đã cắt ngang, đúng quy tắc gasp đã khóa.)

### 3.3. SFX

**Key 1238 [凪] — SFX (độ dài).** JP: `「息ばい？　息ば、にーさんの勃起ビクビクさせるばい？\\n（ふーーーーーーーーーーーーっ！）」` / TW: `「呼吸？呼吸就能讓大哥哥的勃起抖動嗎？（呼！）」` — Cũ: `「Hơi thở á? Hơi thở làm cho của anh hai giật giật được luôn á?\\n（Phùuuuuuuuuuuuuuu!）」` → Mới: `「Hơi thở á? Hơi thở làm cho của anh hai giật giật được luôn á?\\n（Phùuuuuuuuuuuuuu!）」`. (JP ふ + 13 dấu ー = 14 mora; VN cũ 15 nguyên âm — thừa 1; sửa về 14 nguyên âm: ù + 13 u.)

**Key 1252 [ふかみ] — SFX (độ dài).** JP: `「わ。ほんと――双鉄さん、息で、感じちゃうんだ。\\n（ふーーーっ）（ふーーーっ）（ふーーーーーーっ）」` / TW: `「哇，還真是……呼吸就能讓雙鐵先生有感覺啊。（呼……）（呼……）（呼……）」` — Cũ: `「Oa. Thật này——Anh Soutetsu, có cảm giác chỉ với hơi thở thôi sao.\\n（Phùuu）（Phùuu）（Phùuuuuu）」` → Mới: `「Oa. Thật này——Anh Soutetsu, có cảm giác chỉ với hơi thở thôi sao.\\n（Phùuuu）（Phùuuu）（Phùuuuuuu）」`. (JP ふーーーっ = 4 mora ×2, ふーーーーーーっ = 7 mora; VN cũ 3/3/6 nguyên âm — thiếu 1 ở cả ba đoạn; sửa về 4/4/7.)

**Key 2026 [monologue] — SFX.** JP: `（ぬるっ――にゅりゅっ――じゅくっ――じゅるんっ！）` / TW: `（啾……啾……啾……啾！）` — Cũ: `（Trơn tuột——nhóp nhép——rột——sột soạt!）` → Mới: `（Trơn tuột——nhóp nhép——rột——rột!）`. (じゅるんっ là tiếng trượt ướt; "sột soạt" là tiếng sột soạt khô — sai loại tiếng. "Rột" đúng cách diễn tiếng họ じゅる trong file: 1301 じゅるっ→"rột", 2028 じゅんっ→"Rột!".)

**Key 2027 [monologue] — SFX.** JP: `（しにゅっ！　くちゅっ！　ちゅちゅ！　にゅるっ！）` / TW: `（啾！啾！啾！啾！）` — Cũ: `（Nhóp nhép! Sột soạt! Chụt chụt! Trơn tuột!）` → Mới: `（Nhóp nhép! Nhóp nhép! Chụt chụt! Trơn tuột!）`. (くちゅっ là tiếng nhóp nhép ướt; "sột soạt" sai loại tiếng. Chính file này 2025 đã diễn くちゅっ là "nhóp nhép" — sửa cho nhất quán.)

**Key 2043 [monologue] — SFX.** JP: `（ずっ――るっ！　ずりゅ！　じゅぶっ！）` / TW: `（插！插！插！）` — Cũ: `（Phập——rột! Phập! Sột soạt!）` → Mới: `（Phập——rột! Phập! Phập!）`. (じゅぶっ là tiếng thụt vào ướt; "sột soạt" sai loại tiếng. "Phập!" đúng cách diễn trong chính dòng này (ずりゅ!→"Phập!") và 2044 ずりゅっ!→"Phập!".)

### 3.4. Lỗi gõ

**Key 939 [monologue] — typo.** JP: `“一番、恥ずかしいところ”――\\n言葉を、自ら体現しようとするかのように。` / TW: `“最羞人的地方”……就像是用自己的行動表現自己說的這句話一樣。` — Cũ: `Chỗ, đáng xấu hổ, nhất'――\\nNhư thể cô ấy đang tự mình thể hiện câu nói đó vậy.` → Mới: `Chỗ, đáng xấu hổ, nhất――\\nNhư thể cô ấy đang tự mình thể hiện câu nói đó vậy.`. (Dấu nháy đơn thừa sau "nhất" — sót lại từ cặp ngoặc kép “ ” của JP; chỉ bỏ dấu ', không đổi nghĩa.)

## 4. Sweep gasp

- Đã kiểm tra trực tiếp `sweep-raw-gasp-wrong.json`: file này có 5 mục.
- 4 mục already-rendered — kiểm chứng đúng, không sửa: 1235 「っ！」→"Ư!", 1236 「っ！！」→"Ư!!", 1285 「っ！」→"A!" (dấu ! giữ tiếng), 2022 （っ！）→（Ư!）.
- 1 mục needs-file-audit — đã xử lý, KHÔNG sửa: 1736 `目と目。\\nそれだけまた会話して――っ！！？` — VN "Bốn mắt nhìn nhau.\\nChỉ bấy nhiêu thôi mà hai người lại trò chuyện tiếp——ư!!?" đã diễn っ thành "ư" — tiếng đã sống, không nhân đôi theo quy tắc gasp đã khóa.
- Sweep bỏ sót 1 gasp (1280, §3.2) — đã sửa trong audit.

## 5. Đã kiểm tra và giữ nguyên

- **fa/fu "phù" — KHÔNG sửa trong audit, để đợt thống nhất** (tiền lệ ふかみh1, 日々姫h1, lr_ふかみh2): 1166, 1218, 1227, 1237, 1246 (2 lần), 1247, 1336, 1440 — 9 lần ふぁっ/ふあっ diễn thành "phù"/"Phù" (quy tắc đã quyết: ふぁ→"phà", ふあ→"phùa"). Xem §6.
- **1317** れろおおおおおおおおっ → "Liếmmmmmmmm!": 8 dấu お, VN 9 chữ m — giữ nguyên (theo cách đếm 1 + số lượng thì 9 là đúng).
- **1474** dòng 1 `イっ――くぅぅぅぅぅぅぅぅうううううううんっ！` → "R-raaaaaaa mấttttt!": cách diễn sáng tạo của tiếng rên dài, giữ nguyên.
- **1433** おまんこ → "âm đạo" + "chỗ đó": thứ tự từ xáo trộn nhẹ nhưng đủ nghĩa, giữ nguyên.
- **1226** にゃ → "nya": giữ gần tiếng Nhật gốc theo quy tắc Hieu 22:19, giữ nguyên.
- **1285/1231/1314** あっ/ああっ → "A"/"a"/"A!": tiếng っ được giữ bằng dấu ! hoặc dấu ——, không thêm Ư (quy tắc gasp đã khóa).
- **1290** ちゅうっ → "chu": tiếng hôn đã sống, không sửa.
- **2054** （のそっ）→"Sột soạt": のそっ là tiếng sột soạt chậm — dùng đúng, giữ nguyên (khác 3 dòng SFX đã sửa ở §3.3).
- Soutetsu "anh" với Nagi/Fukami đúng toàn file (1170, 1175, 1193, 1241, 1356, 1360, 1406, 1427, 1467); độc thoại "tôi" đúng; "bọn tôi"/"bọn em" nhóm đúng.

## 6. Cờ cho Hieu (không tự quyết)

1. **Nói ngọng khi miệng đang bận (giữ nguyên âm ngọng hay diễn thành lời rõ?) — 2 dòng: 1291, 1303.** JP là tiếng nói ngọng vì miệng đang ngậm/liếm (1291: `ひっはひ――ひほひひょふはっへ――ふっ――ふらはい――へ？`; 1303: `ひょはひょひょ――んっ――ひーはふっ――んっ`), TW diễn thành lời có nghĩa ("沒關係……舒服起來就行了"; "濕漉漉的……沒關係"), VN theo TW ("c-cứ——thấy sướng là được——phù——ạ——nhỉ?"; "kh-không sao đâu——ưm——cứ ra đi——ưm"). Cùng loại với ハチロク07 2916–2918 đã cờ trước — Hieu quyết giữ lời rõ hay trả về âm ngọng.
2. **fa/fu "phù" → đợt thống nhất — 8 key: 1166, 1218, 1227, 1237, 1246, 1247, 1336, 1440** (9 lần ふぁっ/ふあっ). Đã quyết ふぁ→"phà", ふあ→"phùa" — sửa trong đợt thống nhất duy nhất sau khi xong 216 file.
3. **1224 — lỗi nguồn phía JP, không phải lỗi VN:** JP `「ひあ"っ！！？」` có dấu `"` thừa giữa ひあ và っ (cả CSV3 lẫn TOML đều vậy). VN "Á!!?" đúng. Chỉ ghi chú, không sửa VN.

## 7. Lượt soát 2

- Tổng: **8** / kiểm chứng lại: **8** / bỏ: **0** / sửa: **0**.
- Đã đọc lại toàn bộ 8 giá trị fix đối chiếu JP (+TW khi cần): 1 đại từ + 1 gasp + 5 SFX + 1 lỗi gõ — tất cả đúng JP. Kiểm chứng cơ học: JSON 8 mục, khối TOML 8 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 8/8; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa.

## 8. Khối TOML (đã kiểm chứng parse)

```toml
"939" = "Chỗ, đáng xấu hổ, nhất――\\nNhư thể cô ấy đang tự mình thể hiện câu nói đó vậy."
"1238" = "「Hơi thở á? Hơi thở làm cho của anh hai giật giật được luôn á?\\n（Phùuuuuuuuuuuuuu!）」"
"1252" = "「Oa. Thật này——Anh Soutetsu, có cảm giác chỉ với hơi thở thôi sao.\\n（Phùuuu）（Phùuuu）（Phùuuuuuu）」"
"1280" = "「An」"
"1332" = "「Bé Nagi, nhé? Không sao đâu——vì mình cũng, ở cùng cậu mà.」"
"2026" = "（Trơn tuột——nhóp nhép——rột——rột!）"
"2027" = "（Nhóp nhép! Nhóp nhép! Chụt chụt! Trơn tuột!）"
"2043" = "（Phập——rột! Phập! Phập!）"
```

## Kết bài

File 凪ふかみh1_修学旅行の夜.txt.toml: 318 dòng đã đọc hết, **8 dòng sai (2,5%)** — không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch. Lỗi tập trung ở SFX (5/8: 2 độ dài hơi thở + 3 "sột soạt" sai loại tiếng) + 1 đại từ Fukami "tớ"→"mình" + 1 gasp sweep bỏ sót + 1 lỗi gõ. 3 cờ cho Hieu (§6) — nói ngọng 1291/1303, 8 key fa/fu cho đợt thống nhất, và lỗi dấu `"` phía JP ở 1224. Khối TOML 8 khóa đã parse-kiểm chứng, 0 sai lệch giá trị.

Kết bài
