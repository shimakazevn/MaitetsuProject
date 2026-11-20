# Audit — ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml (01_Hachiroku)

- File: `01_Hachiroku/ハチロクh6_ウェディングドレスを脱ぎ捨てて.txt.toml`
- Đọc: **461/461 dòng** (script, key 491–2049), đọc từng dòng đối chiếu JP + TW (CSV3).
- Sai: **16 dòng / 461 = 3,5%** — file sạch nhất nhóm Hachiroku h6 tới nay, sai tập trung ở SFX/gasp.
- Cơ sở rebase: 102 file / 4.846 dòng sai (ROUTE-AUDIT.md, đã tự kiểm chứng 20/11 ~16:00) → sau file này **103 file / 4.862 dòng sai**.
- TOML md5: `9c51863393588f1bb888afa1bdbec48a` (89.719 byte). Không có file trùng lặp (không thuộc 11 nhóm duplicate). CSV3: 1 bộ duy nhất, 461 dòng, 461 key phân biệt, khớp phẳng với TOML (245 "lệch" chỉ là TOML làm phẳng `\n` thành khoảng trắng — CSV3 là chuẩn).
- Nhân vật: monologue 266, ハチロク 118, 双鉄 77. Toàn file là cảnh H (đêm tân hôn, váy cưới + nippless).

## Phân loại sai (16)

| Loại | Số dòng | Key |
|---|---|---|
| lost-gasp (sweep っ, đã kiểm chứng lại từng dòng với JP) | 11 | 519, 775, 873, 1008, 1080, 1081, 1082, 1083, 1085, 1557, 1771 |
| lost-gasp đầu dòng (っ―― đầu câu bị nuốt, không có trong sweep) | 2 | 515, 516 |
| từ bịa thêm (không có trong JP/TW) | 2 | 1050 ("mất"), 1760 ("liếm lấy") |
| đọc sai tên vỡ (broken-name "Soutetsu-san" khi đang mút) | 1 | 511 |

## Chi tiết từng dòng sai

### 1. Key 511 — ハチロク — misread (tên vỡ)
- JP: 「は――むちゅっ――いっ――ちゅむっ――そう――\nれるっ――てつ――ちゅぱっ――さ――んむっ！！？」
- TW: 「——咕啾——咿——啾咕——雙——咻嚕——鐵——啾啪——少爺——唔！！？」
- Cũ: 「Hà——chụm——ư——chụt——ngài——\nmút——Soutetsu——chụt——của——ưm!!?」
- Mới: 「Hà——chụm——ư——chụt——Sou——\nmút——tetsu——chụt——ngài——ưm!!?」
- Lý do: JP là tên "Soutetsu-san" vỡ ra từng mảnh xen tiếng mút: そう (Sou) + てつ (tetsu) + さ (san → "ngài"). Bản cũ đặt "ngài" vào chỗ そう, "Soutetsu" vào chỗ てつ, và dịch んむっ (tiếng mút nghẹn) thành "của" — cả hai đều sai. TW xác nhận thứ tự 雙–鐵–少爺 (Sou–tetsu–ngài).

### 2. Key 515 — ハチロク — lost-gasp-leading
- JP: 「っ――あっ――あっ！　あっ！　あっ！　あっ！！」
- Cũ: 「——A——a! A! A! A!!」 → Mới: 「Ư——A——a! A! A! A!!」
- Lý do: っ đầu dòng bị nuốt mất; cùng file 509 (「っ――」→「Ư——」) và 513 (「っ――くうっ！」→「Ư——hự!」) đều giữ Ư — 515/516 phá vỡ quy ước của chính file.

### 3. Key 516 — 双鉄 — lost-gasp-leading
- JP: 「っ――あっ！」
- Cũ: 「——A!」 → Mới: 「Ư——A!」

### 4. Key 519 — 双鉄 — lost-gasp (sweep)
- JP: 「――っっ！」 (2 っ) → Cũ: 「——!!」 → Mới: 「——ƯƯ!!」

### 5. Key 775 — 双鉄 — lost-gasp (sweep)
- JP: 「が、今はふたりきりだぞ？\n僕にまで、乳首を隠す必要などは――っ！」
- Cũ: 「…ngay cả với tôi chứ——!」 → Mới: 「…ngay cả với tôi chứ——Ư!」

### 6. Key 873 — 双鉄 — lost-gasp (sweep)
- JP: 「っ！！」 → Cũ: 「!!」 → Mới: 「Ư!!」

### 7. Key 1008 — ハチロク — lost-gasp (sweep)
- JP: 「です――から、もっと――双鉄様の……中に、あるもの\n――そこまでもっと――全部――ほし、く、――っ！？」
- Cũ: 「…em muốn, có——!?」 → Mới: 「…em muốn, có——Ư!?」

### 8. Key 1050 — ハチロク — invented-word
- JP: 「そんな、に……した、ら――あっ――わた、くしっ、\nん……ふ――ぁ――おっぱい……おっぱいっ！」
- TW: 「那樣子……做的話——啊——我、我的，嗯……呼——啊——乳房……乳房！」
- Cũ: 「…vú……vú mất!」 → Mới: 「…vú……vú!」
- Lý do: JP và TW đều chỉ là tiếng kêu "vú… vú!"; "mất" là từ bịa thêm, không có căn cứ. (っ cuối câu gắn vào おっぱい là っ nhấn mạnh, không phải gasp — không thêm Ư, theo tiền lệ entry 1474 bị bác.)

### 9–12. Key 1080 / 1081 / 1082 / 1083 — 双鉄 — lost-gasp (sweep)
- JP: 「っ！」/「っ！！」/「っ！！！！！」/「っ！！？」
- Cũ: 「!」/「!!」/「!!!!!」/「!!?」 → Mới: 「Ư!」/「Ư!!」/「Ư!!!!!」/「Ư!!?」

### 13. Key 1085 — ハチロク — lost-gasp (sweep, đa-っ)
- JP: 「～～～～っっ！！！！！！！！！」 (2 っ, 9 dấu !)
- Cũ: 「~~~~!!!!!!!!!」 → Mới: 「~~~~ƯƯ!!!!!!!!!」 (giữ nguyên 9 dấu !)

### 14. Key 1557 — monologue — lost-gasp (sweep)
- JP: 「乳首を勃起の横でコスって、\nドレスと胸との狭隘を、思いっきりに滑らせて――っ！？」
- Cũ: 「…bầu ngực——!?」 → Mới: 「…bầu ngực——Ư!?」

### 15. Key 1760 — monologue — invented-word
- JP: 「すずが――舌を。\n短い舌を懸命に、勃起へと伸ばしてくれている。」
- TW: 「鈴伸出了舌頭。她拚命向肉棒伸出短短的舌頭」
- Cũ: 「…Cố gắng vươn chiếc lưỡi ngắn ngủi liếm lấy cậu bé đang cương cứng.」
- Mới: 「…Cố gắng vươn chiếc lưỡi ngắn ngủi về phía cậu bé đang cương cứng.」
- Lý do: JP chỉ có 伸ばす (vươn ra, hướng tới); "liếm lấy" (liếm) là động tác bịa thêm, TW cũng không có.

### 16. Key 1771 — monologue — lost-gasp (sweep)
- JP: 「すずの喉奥がひゅっと動いて、\n僕の口内の唾液も息も全部が強く吸い取られ――っ！？」
- Cũ: 「…bị hút mạnh đi——!?」 → Mới: 「…bị hút mạnh đi——Ư!?」

## Kiểm chứng sweep っ cho file này
- Sweep có 14 entry cho file: 11 fix đã lấy vào danh sách trên (1008, 1080, 1081, 1082, 1083, 1557, 1771, 775, 873, 1085, 519) — kiểm chứng từng giá trị với JP, tất cả đúng.
- 3 entry "already-rendered" (837, 938, 946) không cần sửa — đồng ý với sweep: gasp đã được diễn bằng SFX khác trong câu (837 "chùn chụt", 938 "Ưm ưm~~~~~", 946 "Ưm ư ư…~").
- っ nhấn mạnh cuối câu gắn vào động từ (1307, 1316, 1542, 1707, 1812) KHÔNG sửa — đúng quy tắc (không phải gasp, tiền lệ entry 1474).

## Các kiểm tra khác — đều sạch
- **Lệch/luân chuyển (rotation):** 0. Không có cặp dòng nào bị tráo key; VN trùng lặp chỉ ở những JP vốn đã lặp (「ああ」868/916, 「っ！！」873/1081, chuỗi SFX 1995/2001/2006) — đều là lặp hợp lệ.
- **Orphan (VN không có nguồn JP):** 0. **Chưa dịch:** 0 (không có VN rỗng, không có VN == TW).
- **Trùng key CSV3:** 0 (461 key phân biệt). **%l tag:** 0 trong file (JP và VN đều không có). **Ký tự Nhật còn sót trong VN:** 0.
- **Ruby [x,n]:** 1 chỗ duy nhất, đúng — key 958: JP `[わたくしの半身,3]8620` → VN `[nửa kia của em,3]8620`.
- **Đại từ Soutetsu:** file toàn cảnh Soutetsu–Hachiroku → "tôi" đúng suốt; không có dòng nào cần đổi "anh"/"tôi". Không có dòng nào Soutetsu xưng với Nagi/Hibiki/Paulette/Reina/Fukami trong file này.
- **Thuật ngữ đã quyết:** Railord (1281), cộng cảm (958), ニップレス → "miếng dán ngực", だんなさま → "phu quân", 市電 không xuất hiện. Không có "Migita System", "Obata", "Yui", "Master Controller" trong file.
- **Tiếng cười:** 823 「うふふっ」→ "Ufufu." đúng (cười ra cười, không thành rên).

## Chờ Hieu (không tính sai — ghi lại, không tự quyết)
- **fa/fu — 14 dòng dùng biến thể "phù a"/"phù" thay vì quy tắc đã quyết ふぁ→"phà", ふあ→"phùa":** 829 (ぷぁ), 830, 831, 832, 852, 863, 881, 884, 915 (ぷぁ+ふぁ), 930, 941, 948 (ぷあっ+ふあああ～), 950, 1020 (ふぁ→"Phù"). Theo tiền lệ lr_ふかみh2 ("phù" flagged cho unification pass, không sửa trong audit), 14 dòng này KHÔNG tính vào 16 dòng sai — để cho đợt thống nhất (unification pass) khi Hieu duyệt phạm vi.
- **Key 491 — JP cụt, không sửa:** JP "――とは、到底いかず。" (câu cụt, nối từ file trước — key đầu file là 491); TW "但實在是沒力氣了" (thực sự hết sức rồi); VN hiện tại "——Nhưng mà, đâu có dễ dàng như vậy." mơ hồ nhưng không rõ sai — giữ nguyên, ghi chú để Hieu soi khi đọc lại cảnh.
- **Key 1813 — JP gốc lạ:** JP ghi "旧悪なレベル" (旧悪 không phải từ chuẩn — gần như chắc là lỗi gõ của 凶悪); TW "動作變得更加兇惡"; VN "một mức độ tàn bạo hơn nữa" theo TW là đúng. Ghi chú, không sửa.
- **Key 1027:** JP 「それ――？」 mơ hồ; VN "Thứ đó——?" theo sát JP (TW diễn giải thành "看什麼" — không theo TW vì JP thắng TW).
- **Key 1522:** VN thêm "giọt mồ hôi" cho "その一滴" — chấp nhận được vì ngữ cảnh (mồ hôi ở 1381); không tính sai.

## Lượt soát 2 (bắt buộc)
- Đọc lại toàn bộ 16 giá trị fix đối chiếu JP (+TW): **16 / 16 re-verified, 0 bỏ, 0 sửa**.
- Lưu ý minh bạch: lúc ráp JSON, bước kiểm chứng ráp đã bắt được 10 giá trị fix viết tay thiếu dấu 「」 (511, 515, 516, 519, 873, 1080–1083, 1085) — đã sửa bằng cách build lại từ old-VN đầy đủ qua thay thế có mục tiêu, rồi mới soát 2. Lượt soát 2 sau đó không phát hiện thêm lỗi nào.
- Kiểm chứng cơ học (script, sau soát 2): JSON 16 mục, key dạng chuỗi; khối TOML parse được, 16 khóa, **0 sai lệch giá trị** so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối **16/16**; mỗi fix chỉ khác old-VN ở đúng chỗ cần sửa (diff-sanity: toàn là insert/delete/replace nhỏ, có mục tiêu).
- Danh sách sửa: `audit-hachiroku-h6-wedding-wrong.json` (16 mục, dạng chuẩn list-of-dicts).

## Khối TOML (đã parse-kiểm chứng)

```toml
[script]
"511" = "「Hà——chụm——ư——chụt——Sou——\\nmút——tetsu——chụt——ngài——ưm!!?」"
"515" = "「Ư——A——a! A! A! A!!」"
"516" = "「Ư——A!」"
"519" = "「——ƯƯ!!」"
"775" = "「Nhưng mà, bây giờ chỉ có hai chúng ta thôi mà?\\nĐâu cần thiết phải giấu núm vú ngay cả với tôi chứ——Ư!」"
"873" = "「Ư!!」"
"1008" = "「Vì——vậy, nhiều hơn nữa——những thứ……bên trong, ngài Soutetsu\\n——vào sâu hơn nữa——tất cả——em muốn, có——Ư!?」"
"1050" = "「Làm, như thế……thì——a——em,\\nưm……phù——a——vú……vú!」"
"1080" = "「Ư!」"
"1081" = "「Ư!!」"
"1082" = "「Ư!!!!!」"
"1083" = "「Ư!!?」"
"1085" = "「~~~~ƯƯ!!!!!!!!!」"
"1557" = "Chà xát núm vú bằng phần hông của cậu bé đang cương cứng,\\ntrượt mạnh qua khe hẹp giữa chiếc váy và bầu ngực——Ư!?"
"1760" = "Suzu——đã dùng lưỡi.\\nCố gắng vươn chiếc lưỡi ngắn ngủi về phía cậu bé đang cương cứng."
"1771" = "Sâu trong cổ họng Suzu khẽ giật,\\ntoàn bộ nước bọt và hơi thở trong miệng tôi bị hút mạnh đi——Ư!?"
```

## Kết bài
File ハチロクh6_ウェディングドレスを脱ぎ捨てて: đọc 461 dòng, sai 16 dòng (3,5%) — 11 gasp っ theo sweep (đã kiểm chứng), 2 gasp đầu dòng sweep bỏ sót, 2 từ bịa thêm, 1 tên vỡ đọc sai. Không lệch, không orphan, không trùng key, không dòng chưa dịch, không lỗi %l; đại từ và thuật ngữ đã quyết đều đúng. Lượt soát 2: 16/16, 0 bỏ, 0 sửa. Chờ Hieu: biến thể fa/fu "phù a" 14 dòng (để unification pass), key 491 (JP cụt), key 1813 (JP "旧悪" lạ).
