# Audit — 日々姫01_リゾート食堂列車計画.txt.toml (02_Hibiki)

- File: `日々姫01_リゾート食堂列車計画.txt.toml` — route 02_Hibiki, **339 dòng script**, 1 copy.
- Nội dung: phiên chất vấn của nghị viên Niitsu với thị trưởng Hibiki về dự án tàu ăn uống nghỉ dưỡng (御一夜鉄道) xen kẽ cảnh quán cà phê (Soutetsu + Kisaki) và các đoạn riêng tư Soutetsu–Hibiki; chuẩn bị chuyến khảo sát Yufuin / Bungomori.
- Phương pháp: đọc hết 339/339 dòng theo JP + TW (CSV3, 1 set duy nhất — không trùng khóa, 0 ô VN/JP/TW trống), đối chiếu TOML-2. Không lấy mẫu. Key không theo thứ tự truyện (hội đồng / quán cà phê / độc thoại xen kẽ theo key) — xác định người nói/người nghe theo nội dung và dòng kề.

## §1. Các dòng sai (4 dòng, 1,2%)

### 1.1. 1220 (monologue) — dịch sai: 文字 → "dòng chữ"
- JP: `＜　週明け　→　今週末から　＞\nたったそれだけの文字にすぎない。`
- TW: `“星期一　→　從這週末開始”，就只有這麼幾個字。`
- VN cũ: `＜ Đầu tuần → Từ cuối tuần này ＞\nChỉ vỏn vẹn vài dòng chữ như vậy.`
- Sửa: `＜ Đầu tuần → Từ cuối tuần này ＞\nChỉ vỏn vẹn có vài chữ như vậy mà thôi.`
- Lý do: JP 文字 = chữ cái/ký tự (chỉ đổi "đầu tuần" → "từ cuối tuần này", vài ký tự), TW 幾個字 đồng ý; VN "vài dòng chữ" (vài dòng) dịch sai đơn vị.

### 1.2. 1603 (双鉄) — gasp sweep: mất tiếng っ cả dòng
- JP: `「っ！」`
- TW: `「唔！」`
- VN cũ: `「!」`
- Sửa: `「Ư!」`
- Lý do: mục sweep duy nhất của file này (lost-gasp-whole) — JP là tiếng gasp っ nguyên dòng, VN chỉ còn dấu chấm than; áp nguyên văn giá trị sweep, đã kiểm chứng đúng JP.

### 1.3. 2143 (monologue) — thuật ngữ: 乗務員 → "tổ bay" (hàng không)
- JP: `その上、これほどに長い乗車時間だ。\n乗務員の控室も、絶対に削れない設備になってくる。`
- TW: `另外搭車時間這麼長，乘務員的休息室也是不可或缺的。`
- VN cũ: `Thêm vào đó, thời gian ngồi trên xe lại dài như vậy.\nPhòng nghỉ của tổ bay cũng trở thành thiết bị tuyệt đối không thể cắt giảm.`
- Sửa: `Thêm vào đó, thời gian ngồi trên xe lại dài như vậy.\nPhòng nghỉ của nhân viên tàu cũng trở thành thiết bị tuyệt đối không thể cắt giảm.`
- Lý do: 乗務員 = nhân viên tàu (đường sắt); "tổ bay" là thuật ngữ hàng không — sai lĩnh vực, cùng họ lỗi với 乗員 "phi hành đoàn" đã chốt (tiền lệ sửa trong-audit: ハチロク10_炙り出し 2411). Đây là dòng 乗務員/乗員 duy nhất còn sót dạng hàng không trong file (quét toàn file: "phi hành" 0, "tổ bay" chỉ 1 dòng này).

### 1.4. 2191 (monologue) — đại từ: "chị ấy" cho Hibiki
- JP: `いかにもわざとらしくそう言って、\n肩まで大げさにすくめてみせる。`
- TW: `她邊說邊用力聳了聳肩膀，我看她根本就是故意的。`
- VN cũ: `Nói một cách vô cùng cố ý,\nchị ấy còn cường điệu nhún vai một cái.`
- Sửa: `Nói một cách vô cùng cố ý,\nem ấy còn cường điệu nhún vai một cái.`
- Lý do: khối độc thoại 2175–2194 toàn nói về Hibiki (2175/2177/2179/2181/2185/2190 đều "em ấy"; 2194 nêu đích danh 日々姫) — Soutetsu không bao giờ gọi Hibiki là "chị". Đây là lỗi trượt đại từ của Gemini; "chị ấy" đúng cho Mayami (2429) và "cô ấy" đúng cho Kisaki (2162), chỉ riêng 2191 sai.

## §2. Đã kiểm chứng là ĐÚNG (không sửa)

- **1975 (双鉄) "tôi" — giữ nguyên.** "Chút này cứ để tôi trả" — người nghe là Kisaki, không phải Hibiki: đây là cảnh quán cà phê Soutetsu–Kisaki (1976 Kisaki nói tiếp; 2145 Kisaki uống cà phê; 2162 độc thoại "tay cô ấy định lấy tờ hóa đơn" — Kisaki định trả tiền, Soutetsu ngăn lại). "Tôi" với Kisaki đúng theo quy tắc đã chốt.
- **2491 (độc thoại) "Anh" — giữ nguyên.** Soutetsu nghĩ với Hibiki trong phiên họp ("Anh và Kisaki sẽ hỗ trợ em") — "anh" với Hibiki đúng.
- **Kisaki tự xưng:** "tôi" ở các ngữ cảnh công việc/quyết đoán với Soutetsu (1531 lịch ngân hàng, 1709, 1996) và "chị" với Hibiki (1760, 1884, 1994) — đúng quy tắc Kisaki theo ngữ cảnh; Kisaki gọi Soutetsu bằng tên trần (1709, 1792) đúng quyết định 21/11.
- **1944 千内 → "Sendai" — giữ nguyên.** Furigana JP [せんだい,1]千内 xác nhận Sendai (cùng họ đổi chữ địa danh hư cấu: 隈元=Kumamoto, 来目=Kurume, 大板=Oita); TW 川內 chỉ là đọc theo mặt chữ.
- **1613 「！」 — giữ nguyên.** JP không có âm thanh nào, chỉ dấu "!"; TW thêm 啊 nhưng JP thắng TW.
- **SFX cười/gasp:** 1583 ふふっ → "Fufu" (tiếng cười, đúng); 1661 うれしかっ――（ちゅっ！）→ "Vui quá——（Chụt!）" và 2031 （ちゅっ！）→ "（Chụt!）" đúng quy tắc gasp; 1725 んんっ → "Ưm" đúng; 2008 おまたせっ! (っ gắn từ có nội dung) không thêm Ư, đúng.
- **復線 → "khôi phục tuyến đường" (1702, 2016, 2225, 2433) — giữ nguyên.** TW nhất quán 廢線恢復 ở cả 4 dòng; bối cảnh truyện là khôi phục các tuyến đã bị bãi bỏ (大廃線), không phải lắp đường đôi. Đây là cách dùng 復線 của game, giữ theo TW + mạch truyện.
- **1654 "Đang cười kìa" — giữ nguyên.** JP 笑っている không nêu chủ ngữ; tiếng Việt lược chủ ngữ khi suy ra được từ ngữ cảnh, không phải lỗi.
- **1731/2018 加湿器 → "máy phun sương" — giữ nguyên.** Cách gọi thông dụng trong tiếng Việt cho máy tạo ẩm; nhất quán nội bộ file (2/2).
- **2259 "đáp trả lại" — giữ nguyên.** JP お返しをする mơ hồ đúng mức (ngữ cảnh hôn đáp lại đã rõ từ 2243–2247); VN không sai, chỉ không nói toạc ra như TW.

## §3. Gasp sweep — đã kiểm tra trực tiếp trong sweep-raw-gasp-wrong.json
- File này có **1 mục sweep duy nhất: 1603** (lost-gasp-whole, "「!」" → "「Ư!」") — đã áp nguyên văn (§1.2). Không có mục sweep nào khác cho file này (2 mục còn lại khi tìm "日々姫01" thuộc file 日々姫01_双鉄の妹, không phải file này).

## §4. Thuật ngữ dạng cũ — ghi vào đợt thống nhất (không tính sai trong audit này)
- **"Ohimitera" 13 dòng:** 1224, 1561, 1658, 1680, 1714, 1773, 1895, 1973, 2004, 2225, 2473, 2484, 2506 — trong đó "Đường sắt Ohimitera" 1658/2004/2225, 『Hội Công dân Ohimitera』1773, "Ngân hàng Ohimitera" 2484. Dạng cũ của "Ohitoyo", sửa trong đợt thống nhất theo tiền lệ Hibiki10.
- **"Obata" 1 dòng: 2225** (cùng dòng có cả "Ohimitera" ×2) — thiểu số lệch quy ước "Okoba" (quyết định ở audit ハチロク12: 4 dòng Obata toàn dự án, trong đó có dòng này, thống nhất về "Okoba" khi audit tới).

## §5. Kiểm chứng cơ học
- CSV3: 339 dòng, 1 set duy nhất, 0 trùng key, 0 ô VN/JP/TW trống, 0 dòng chưa dịch.
- TOML-2: 339 khóa `[script]`, md5 `b05f3119505d43486fb8018e0b256598`, không có file trùng nội dung trong toàn bộ TOML-2 (1 copy duy nhất — file `#U65e5...#U59eb01_#U53cc#U9244...` kề bên là 日々姫01_双鉄の妹, file khác). `[selections]` rỗng.
- TOML vs CSV: **227/339 dòng khác nhau CHỈ ở chỗ TOML-2 dẹp literal `\n` thành khoảng trắng** — CSV3 giữ literal `\n` là chuẩn, lấy CSV3 làm căn cứ fix (đúng quy tắc đã chốt). Đây là khác biệt định dạng, không phải lỗi dịch.
- Thẻ `%l`: số lượng JP == VN ở mọi dòng (0 lệch); gloss duy nhất trong file: キハ07s → "KiHa 07S" ×2 (1569, 1989), 種車 → "toa xe nguyên bản" ×1 (1828) — đều đúng.
- Không có っ thô trong VN (0 dòng); không có "Ohito", "Hinamoto", "Migita System", "Yui", "Suntetsu", "Master Controller", "Công chúa Xe điện", "phi hành đoàn" trong file.
- 0 lệch vị trí / 0 chuỗi xoay vòng / 0 nhiễm chéo / 0 dòng mồ côi / 0 dòng chưa dịch / 0 trùng key.
- JSON 4 mục, key chuỗi, dạng list-of-dicts; jp/tw/old_vn khớp CSV3 tuyệt đối 4/4; mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm chứng cơ học).
- **Lượt soát 2 (đọc lại toàn bộ 4 giá trị fix đối chiếu JP): 4/4 tái kiểm chứng, 0 bỏ, 0 sửa.**

## §6. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"1220" = "＜ Đầu tuần → Từ cuối tuần này ＞\\nChỉ vỏn vẹn có vài chữ như vậy mà thôi."
"1603" = "「Ư!」"
"2143" = "Thêm vào đó, thời gian ngồi trên xe lại dài như vậy.\\nPhòng nghỉ của nhân viên tàu cũng trở thành thiết bị tuyệt đối không thể cắt giảm."
"2191" = "Nói một cách vô cùng cố ý,\\nem ấy còn cường điệu nhún vai một cái."
```

Kiểm chứng: khối parse được bằng tomllib, 4 khóa, 0 sai lệch giá trị so với JSON. Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thuật ngữ dạng cũ chờ đợt thống nhất (§4): "Ohimitera" 13 dòng, "Obata" 1 dòng (2225).
- Không có dòng nào cần Hieu quyết trong file này: không có JP cụt cần hoàn thiện, không có người nghe mơ hồ (1975 đã xác minh là Kisaki qua cảnh quán cà phê + 2162), không có B19.

## Kết bài

File 日々姫01_リゾート食堂列車計画: 339 dòng đã đọc hết, **4 dòng sai (1,2%)** — 1 dịch sai (文字→"dòng chữ"), 1 gasp っ mất cả dòng (từ sweep), 1 thuật ngữ hàng không ("tổ bay" cho 乗務員), 1 đại từ ("chị ấy" cho Hibiki). Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. CSV3 1 set duy nhất; TOML-2 dẹp `\n` thành khoảng trắng ở 227 dòng (chỉ là khác biệt định dạng, CSV3 làm chuẩn). JSON 4 khóa chuỗi; khối TOML parse OK, 4 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 4/4; lượt soát 2: 4/4, 0 bỏ, 0 sửa. File sạch hơn nhiều so với mặt bằng chung — lỗi rải rác, không có cụm lỗi hệ thống.
