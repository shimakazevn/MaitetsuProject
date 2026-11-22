# Audit — 日々姫15_終着駅 (02_Hibiki) — REVIEW

- File TOML: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59eb15_#U7d42#U7740#U99c5.txt.toml` (tên thật: `日々姫15_終着駅.txt.toml`)
- CSV3: `日々姫15_終着駅.txt.toml`, 54 dòng, section `script` duy nhất, không key trùng, không dòng VN trống.
- Phương pháp: đọc từng dòng JP + TW + VN (54/54), đối chiếu TOML ↔ CSV3 bằng máy, kiểm tra tag `%l`, kiểm tra sweep gasp, kiểm tra md5/trùng lặp.
- **Kết quả: 54 dòng đọc, 2 dòng sai (3,7%).**

## Tổng quan

File này là cảnh cuối route Hibiki ("ga cuối"): Soutetsu gặp Michiko (em gái sinh đôi đã mất) trong mơ/trên tàu. Người nói chỉ có monologue (Soutetsu), 路子 (Michiko) và 双鉄 (Soutetsu). Bản dịch gốc nhìn chung rất tốt — không lệch dòng, không xoay vòng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. Cả 2 lỗi đều cùng một loại: **sai chủ ngữ** (đổi "ai" thành "ai"), không phải lỗi từ vựng hay ngữ pháp.

## Các dòng sai (2)

### 1. Key 484 — 路子 — sai chủ ngữ

- JP: 「なれたんだよ？　大人に。\nそーちゃんが、大人になってくれたから」
- TW: 「我長大了。因為小雙也長大了」
- VN cũ: 「Em đã lớn rồi đấy? Trở thành người lớn rồi。\nBởi vì Sou-chan, đã lớn lên mà。」
- VN mới: 「Anh đã lớn rồi đấy? Trở thành người lớn rồi。\nBởi vì Sou-chan, đã lớn lên mà。」

Lý do: câu này trả lời trực tiếp câu hỏi của Soutetsu ở key 483 (「僕は、大人になれたのか」— "Anh đã trưởng thành rồi sao?"). Chủ ngữ của なれたんだよ là Soutetsu ("anh đã lớn rồi đấy?"), mệnh đề thứ hai xác nhận: そーちゃんが、大人になってくれたから ("bởi vì Sou-chan đã lớn lên"). VN cũ gán việc "lớn lên" cho "Em" (Michiko) ở mệnh đề đầu rồi lại nói "Sou-chan đã lớn lên" ở mệnh đề sau — tự mâu thuẫn. TW 「我長大了」 cũng sai theo hướng này; JP thắng TW. Chỉ đổi "Em" → "Anh", giữ nguyên toàn bộ phần còn lại (kể cả "Sou-chan" ở mệnh đề hai, đúng JP).

### 2. Key 611 — monologue — sai chủ ngữ

- JP: あの事故の傷を抱えたままで、\nずっと、心は子供のままで――
- TW: 那場事故的傷痕一直殘留在心裡，內心一直都未曾成長——
- VN cũ: Mang theo vết thương của vụ tai nạn đó，\ntrái tim tôi, vẫn luôn là một đứa trẻ――
- VN mới: Mang theo vết thương của vụ tai nạn đó，\ntrái tim em ấy, vẫn luôn là một đứa trẻ――

Lý do: chủ ngữ là trái tim của **Michiko**, không phải của Soutetsu. Bằng chứng: (a) key 609 ngay trước đó tả Michiko cười "y hệt như Michiko hồi còn nhỏ"; (b) key 570 đã chốt: Michiko "đã chết từ lâu lắm rồi, khi còn chưa kịp lớn lên" — trái tim em ấy mãi mãi là một đứa trẻ; (c) toàn bộ mạch cảnh này là Soutetsu nhận ra mình ĐÃ trưởng thành (483–484, 527 "chắc chắn là một Michiko đã trưởng thành"), nên "trái tim tôi vẫn là một đứa trẻ" mâu thuẫn với mạch truyện. TW bỏ trống chủ ngữ nên không giúp phân xử; JP + mạch truyện quyết định. Chỉ đổi "tôi" → "em ấy".

## Đã kiểm tra và giữ nguyên (không sửa)

- **Key 473** 路子 「うん」 → 「Vâng.」 — giữ nguyên. Michiko nói lịch sự ở đây là có tiền lệ trong dự án (グランドリライト07_真闇 key 2310, cùng 路子 「うん」 → 「Vâng.」). Không phải lỗi.
- **Key 426 / 592** セピア → "Màu nâu đỏ" — giữ nguyên cả hai dòng, nhất quán nội bộ; sepia (TW 深棕色) dịch "nâu đỏ" là chấp nhận được.
- **Key 418** monologue "con bé" chỉ Hibiki; **key 587** "con bé" chỉ Michiko — JP bỏ trống chủ ngữ, VN làm rõ đúng người theo ngữ cảnh; giữ nguyên.
- **Key 462** 「また会うときは、ずうっと先でいいけど」 → "Lần tới gặp lại, hy vọng sẽ là một khoảng thời gian rất dài sau này." — hơi dài dòng nhưng đúng nghĩa ("gặp lại sau thật lâu cũng được"); giữ nguyên.
- **Key 496** 「声だけでもさ、届けに来てね？」 → "Dù chỉ là giọng nói, anh cũng nhớ gửi đến cho em nhé?" — khớp TW; giữ nguyên.
- **Đại từ Soutetsu**: "anh" với Michiko (477, 479, 483, 489) đúng quy tắc đã chốt ("anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi); monologue "tôi" đúng; Michiko gọi Soutetsu "anh" (491) và tự xưng "em" đúng; Soutetsu gọi Michiko "em" (497, 500) đúng. 0 lỗi đại từ.
- **Tag `%l`**: 7 dòng có tag (55, 56, 426, 468, 581, 614, 616) — mọi tag `\x%l…;#;` đều đóng đúng, thuật ngữ JP giữ nguyên, gloss đúng quy tắc đã chốt (列車 → "Đoàn tàu", 客車 → "toa hành khách", 運転台 → "buồng lái"). Không tag lỗi, không tag thừa/thiếu.
- **Sweep gasp (っ)**: kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **0 mục** trong sweep (không có dòng nào chứa っ cần xử lý). Không áp dụng gì từ sweep.
- **SFX cuối file** (627 カタン――コトン―― / 628 カトン、トトン) → "(Cạch――cạch―― / xình xịch――xình xịch――)" và "(Cọc cạch, cọc cạch, / xình xịch, xình xịch――)" — đúng, giữ nguyên.
- **Cười** うふふ (468) → "Ufufu" (tiếng cười, không phải tiếng rên) — đúng quy tắc Hieu 19/11.
- **[selections]**: header có trong TOML nhưng rỗng (file không có lựa chọn) — không có gì để audit.
- **Không lệch dòng / xoay vòng / nhiễm chéo / dòng mồ côi / dòng chưa dịch / key trùng**: 0. JP/TW/VN khớp nhau ở cả 54 dòng; key TOML = key CSV3 (54/54); VN TOML khớp VN CSV3 trừ 36 dòng chỉ khác ở chỗ TOML-2 đã flatten `\n` thành khoảng trắng (đặc tính đã biết của TOML-2, không phải lỗi — CSV3 là chuẩn).

## Phân loại lỗi

| Loại | Số dòng | Keys |
|---|---|---|
| Sai chủ ngữ (sai-chu-ngu) | 2 | 484, 611 |
| **Tổng** | **2** | |

## Kiểm chứng máy

- TOML parse (tomllib): OK; 54 key script, trùng key CSV3 54/54.
- JSON 2 mục, key dạng string; jp/tw/old_vn khớp CSV3 tuyệt đối 2/2; mỗi fix chỉ khác old VN đúng một chỗ thay (484: "Em"→"Anh"; 611: "tôi"→"em ấy") — kiểm bằng difflib.
- Khối TOML dưới đây parse được (tomllib), 2 khóa, 0 sai lệch giá trị so với JSON (lưu ý: `\n` literal trong fix được viết `\\n` trong khối).
- MD5 TOML: `2eb3fa8a5cdc2a59e50600b415e6419b`; không có file TOML nào khác trùng md5 (bản duy nhất, không duplicate). File UTF-8 BOM + CRLF (127 dòng CRLF).

## Second pass (đọc lại toàn bộ fix đối chiếu JP)

- Tổng số fix: 2
- Re-verified (đọc lại, giữ nguyên): 2
- Removed (loại bỏ): 0
- Corrected (sửa lại trong pass 2): 0
- Pass 2 ghi chú: key 484 ban đầu suýt bỏ sót cặp ngoặc 「 」 khi viết fix — đã phát hiện trong lúc đối chiếu ký tự với old VN và sửa lại trước khi chốt JSON (fix giữ nguyên 「 」 như old VN).

## Cờ cho Hieu

Không có cờ nào cần Hieu quyết trong file này. Key 611 là phán đoán của audit (chủ ngữ Michiko, không phải Soutetsu) — bằng chứng đã ghi đầy đủ ở trên (570, 609, mạch 483–484); nếu Hieu đọc khác, chỉ cần đảo lại một từ "em ấy" → "tôi".

## Khối TOML (đã kiểm chứng parse)

```toml
"484" = "「Anh đã lớn rồi đấy? Trở thành người lớn rồi.\\nBởi vì Sou-chan, đã lớn lên mà.」"
"611" = "Mang theo vết thương của vụ tai nạn đó,\\ntrái tim em ấy, vẫn luôn là một đứa trẻ――"
```

## Kết bài

File 日々姫15_終着駅: 54 dòng đã đọc, 2 dòng sai (3,7%), cả hai đều là lỗi sai chủ ngữ và đã sửa bằng thay đúng một từ mỗi dòng. Không có lỗi lệch dòng, xoay vòng, nhiễm chéo, dòng mồ côi hay dòng chưa dịch. Đại từ Soutetsu–Michiko đúng quy tắc đã chốt; tag `%l` và SFX đều đúng; sweep gasp không có mục nào cho file này. File sẵn sàng để gộp.
