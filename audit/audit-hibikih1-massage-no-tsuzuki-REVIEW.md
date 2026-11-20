# Audit: 日々姫h1_マッサージの続き.txt.toml — route 02_Hibiki

- File: `日々姫h1_マッサージの続き.txt.toml` — route 02_Hibiki, 329 dòng script (độc thoại 183, 日々姫 81, 双鉄H 65).
- Nội dung: cảnh H tiếp nối buổi mát xa — đêm sau tiệc mừng chiến thắng, Hibiki sang phòng Soutetsu mát xa cho anh (mát xa đứng, rồi bằng miệng), cả hai thừa nhận muốn làm tình, Soutetsu đề nghị làm tình "đàng hoàng" thay vì thuận đà, Hibiki đồng ý và xin anh lấy đi lần đầu của mình, quan hệ lần đầu, kết bằng những nụ hôn và cả hai chìm vào giấc ngủ.
- Nguồn: TOML-2 `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh1_#U30de#U30c3#U30b5#U30fc#U30b8#U306e#U7d9a#U304d.txt.toml`, md5 `c8169ed72a3a329d6f677624531c75cf` (UTF-8 BOM + CRLF). CSV3: 329 dòng, 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN==TW. VN khớp TOML tuyệt đối 329/329 (0 sai lệch). `[selections]` rỗng. Không có bản sao file này (md5 duy nhất trong cây toml2). Không có thẻ `%l` nào trong file.
- Phương pháp: đọc từng dòng 329/329 đối chiếu JP + TW (JP thắng khi khác nhau); kiểm tra trực tiếp 6 mục sweep cho file này trong `sweep-raw-gasp-wrong.json`, thẻ `%l`, lệch vị trí/chuỗi xoay/nhiễm chéo/mồ côi/chưa dịch/trùng khóa; quét máy đại từ Soutetsu và ký tự JP thô trong VN; lượt soát 2 toàn bộ fix.

## Kết quả tổng quan

**12/329 dòng sai (3,6%)** — gasp 10, dịch sai nghĩa 2.

**Tổng cộng sau file này: 131 file / 6.001 dòng sai** (cơ sở 130/5.989 + 12 file này — cơ sở đã tự kiểm chứng lại với ROUTE-AUDIT.md dòng 2674).

## §1. Gasp っ bị mất (10 dòng)

Sweep có 6 mục cho file này (1011, 1230, 1231, 1232, 1237, 1670) — cả 6 đều đúng, đã nhận nguyên. Ngoài ra tìm thêm 4 gasp sweep bỏ sót (792, 1051, 1056, 1222). Phân biệt áp dụng theo quy tắc gasp đã khóa 20/11: chỉ thêm Ư khi âm っ mất hẳn; っ đứng TRƯỚC gạch ngang (っ――) thì gạch đã diễn tả tiếng ngắt — giữ nguyên (vd. 1042 「うあっ――あっ――気持ち、いいっ――」→「Ua——a——sướng, quá——」, 3 đoạn JP = 3 đoạn VN, không sửa).

### key 792 — 双鉄H
- JP: 「っ――」
- TW: 「――」
- VN cũ: 「——」
- VN sửa: 「——Ư」
- Lý do: っ ở đầu dòng bị mất hoàn toàn — VN chỉ còn gạch ngang. Sweep bỏ sót. Thêm Ư sau gạch theo mẫu sweep.

### key 1011 — 双鉄H (sweep: lost-gasp-trailing)
- JP: 「む、すまん――っ！？」
- TW: 「呃，抱歉！？」
- VN cũ: 「Ơ, xin lỗi——!?」
- VN sửa: 「Ơ, xin lỗi——Ư!?」
- Lý do: nhận nguyên mục sweep — っ đứng sau gạch ngang, VN giữ gạch nhưng mất gasp.

### key 1051 — 双鉄H
- JP: 「っ！　あっ――」
- TW: 「啊！　啊――」
- VN cũ: 「! A——」
- VN sửa: 「Ư! A——」
- Lý do: っ ở đầu dòng bị mất hoàn toàn (chỉ còn "!"). Sweep bỏ sót. Đoạn sau あっ―― đã diễn thành "A——" nên chỉ thêm Ư ở đầu.

### key 1056 — 日々姫
- JP: 「あむっ――っ――れるっ――れろっ――むちゅうっ」
- TW: 「啾――啾嚕――啾嚕――啾噗」
- VN cũ: 「Ngoạm——Liếm——Liếm——Mút.」
- VN sửa: 「Ngoạm——Ư——Liếm——Liếm——Mút.」
- Lý do: JP có 5 đoạn, VN chỉ còn 4 — đoạn っ―― đứng một mình giữa dòng không có diễn tả nào. Sweep bỏ sót. Thêm Ư làm đoạn riêng, khớp lại 5 đoạn = 5 đoạn.

### key 1222 — 日々姫
- JP: 「にぃ――に――わた、しっ――っ――\nはっ――あっ――平気――だか、らっ――」
- TW: 「阿哥――我――呼――啊――沒事――的――」
- VN cũ: 「Anh——hai——em——Hơ——A——Không sao——đâu——」
- VN sửa: 「Anh——hai——em——Ư——Hơ——A——Không sao——đâu——」
- Lý do: như 1056 — JP có 8 đoạn, VN chỉ còn 7, đoạn っ―― đứng một mình bị mất. Sweep bỏ sót. Thêm Ư làm đoạn riêng, khớp lại 8 đoạn = 8 đoạn.

### key 1230 — 双鉄H (sweep: lost-gasp-whole)
- JP: 「っ！」
- TW: 「！」
- VN cũ: 「!」
- VN sửa: 「Ư!」
- Lý do: nhận nguyên mục sweep — cả dòng chỉ là gasp っ+punct, VN chỉ còn dấu câu.

### key 1231 — 双鉄H (sweep: lost-gasp-whole)
- JP: 「っ！！！」
- TW: 「！！！」
- VN cũ: 「!!!」
- VN sửa: 「Ư!!!」
- Lý do: nhận nguyên mục sweep — như 1230.

### key 1232 — 日々姫 (sweep: lost-gasp-whole)
- JP: 「っ！！？」
- TW: 「！！？」
- VN cũ: 「!!?」
- VN sửa: 「Ư!!?」
- Lý do: nhận nguyên mục sweep — như 1230.

### key 1237 — 双鉄H (sweep: lost-gasp-trailing)
- JP: 「～～～～～～っ！！」
- TW: 「～～～～～～！！」
- VN cũ: 「~~~~~~!!」
- VN sửa: 「~~~~~~Ư!!」
- Lý do: nhận nguyên mục sweep — っ đứng sau chuỗi ~, VN giữ ~ nhưng mất gasp.

### key 1670 — monologue (sweep: lost-gasp-trailing)
- JP: 嬉しげに、日々姫の目がアーチを描――っ！？
- TW: 日日姬高興得眉毛彎成了一條弧線――
- VN cũ: Đôi mắt Hibiki cong lên thành hình vòng cung đầy vẻ vui sướng——!?
- VN sửa: Đôi mắt Hibiki cong lên thành hình vòng cung đầy vẻ vui sướng——Ư!?
- Lý do: nhận nguyên mục sweep — dòng độc thoại, っ sau gạch ngang bị mất.

## §2. Dịch sai nghĩa (2 dòng)

### key 970 — 日々姫
- JP: 「来たっ！　きてるっ――あうっ――んっ――\nあつい、の――精液――おなか――子宮、にっ――」
- TW: 「來了！進來了――啊――嗯――熱熱的――精液――進到肚子――子宮的裡面――」
- VN cũ: 「Đến rồi! Đến rồi——A——Ưm——Nóng quá——Tinh dịch——Bụng——Tử cung, đang——」
- VN sửa: 「Đến rồi! Đến rồi——A——Ưm——Nóng quá——Tinh dịch——Bụng——Vào trong tử cung——」
- Lý do: 子宮に = "vào trong tử cung" (hướng vào trong — TW xác nhận: 子宮的裡面); "đang" trong VN cũ không có cơ sở nào ở JP lẫn TW (に là giới từ chỉ hướng, không phải thì tiếp diễn). Đổi "Tử cung, đang——" → "Vào trong tử cung——".

### key 1046 — 日々姫
- JP: 「あっ――おっぱいっ！　んっ――私――にぃににっ――\nんっ、おっぱい――ちゅうちゅう――して、もらってっ」
- TW: 「啊――胸部！嗯――阿哥――嗯，舔著――我的胸部――」
- VN cũ: 「A——Ngực! Ưm——Em——Bị anh hai——Ưm, ngực——Mút mát——Cho.」
- VN sửa: 「A——Ngực! Ưm——Em——Bị anh hai——Ưm, ngực——Mút mát——Cho em.」
- Lý do: してもらって = được [anh] làm cho — em là người hưởng lợi; "Cho." trơ trụi không tân ngữ, đọc như mệnh lệnh ngược hướng ("cho đi"). Thêm "em" để rõ người hưởng: "Mút mát——Cho em."

## §3. Không sai — đã kiểm tra

- **Lệch vị trí / chuỗi xoay: 0.** Không có dòng VN nào thuộc về key khác; không có cặp hoán đổi.
- **Nhiễm chéo / mồ côi: 0.** Mọi dòng VN đều có JP tương ứng trong file; không có dòng VN lạ.
- **Chưa dịch: 0.** 0 dòng VN trống, 0 dòng VN==TW.
- **Trùng khóa: 0.** 329 khóa duy nhất ở cả CSV3 lẫn TOML.
- **Đại từ Soutetsu: 0 sai.** Quét máy toàn bộ 65 dòng 双鉄H: không có dòng thoại nào dùng "tôi"; tất cả tự xưng "anh" với Hibiki đều đúng (vd. 989, 1099, 1115, 1116, 1142, 1156, 1208). Độc thoại Soutetsu dùng "tôi" xuyên suốt.
- **Thuật ngữ đã quyết: 0 sai.** Không có Ohimitera/Hinamoto/nuôi/Điện xá/tuyến Yui/Migita System nào trong file.
- **Thẻ `%l`: 0.** Không có thẻ `%l` trong VN; 2 ruby phía JP ([こわば,1] key 962, [ちつこう,1] key 1214) là furigana trong comment `# JP:`, VN đã chuẩn hóa đúng — không phải lỗi.
- **Ký tự JP thô trong VN: 0.**
- **SFX / tiếng rên giữ nguyên có lý do:** các chuỗi SFX trong ngoặc đơn (1862–1915) đều đã diễn thành tiếng Việt (Chụt/Ngoạm/Phụt/Bạch...); các っ gắn với từ SFX đã diễn (ぺろっ→"Liếm.", くちっ→"Nhóp nhép", ちゅっ→"Chụt") không thêm Ư theo quy tắc gasp; 1049 「っ」→"A." (âm đã diễn); 1050 ふああ…んっ→"Fuaaaaaaaaaaan!!!" (âm kéo dài đã diễn, ngắt cuối truyền qua "n" + !!!).

## §4. Cờ chờ Hieu (không tự quyết)

1. **fa/fu "Phù" → unification (4 dòng):** 1013, 1017, 1018, 1059 — JP ふあっ/ふぁ đều đang là "Phù", trong khi dạng đã quyết là ふあ→"phùa", ふぁ→"phà". Theo tiền lệ (ハチロクh6, ふかみh1) để vào đợt unification, không sửa trong file này. (1050 ふああ…んっ→"Fuaaaaaaaaaaan" là phiên âm đúng, giữ nguyên.)
2. **key 1383 (monologue) — Soutetsu tự xưng lẫn "Anh" và "tôi" trong cùng một dòng:** 「僕もわからん。そんなことは。だけれど不安を与えぬように、ともかく頷く。」→ "Anh cũng có biết đâu. Mấy chuyện này ấy. Nhưng để em ấy không thấy bất an, tôi cứ gật đầu cái đã." Quy ước độc thoại là "tôi"; đây là suy nghĩ đáp lại câu hỏi của Hibiki nên "Anh" có thể là giọng hướng về em. Giữ nguyên, chờ Hieu quyết có chuẩn hóa về "tôi" hay không. Đây là dòng monologue duy nhất trong file dùng "Anh" (quét máy xác nhận).
3. **key 1059 — しゅごっ → "Sướng quá":** JP+TW đều là "amazing" (TW 好厲害), VN diễn thành "Sướng quá" (cảm giác sướng). Giữ nguyên theo quy tắc SFX ngẫu hứng theo nhân vật + ngữ cảnh; cờ để Hieu quyết có muốn nghĩa đen "Tuyệt quá" hay không.
4. **key 1025 — ふぇ？ → "Hả?":** không theo dạng bảng mặc định ("phuê") mà diễn thành thán từ Việt tự nhiên. Giữ nguyên theo quy tắc ngẫu hứng; ghi chú để Hieu biết.
5. **key 1015 — lời nói ngọng khi thè lưỡi:** ろふろふ→"Lêu lêu", ほれッ→"Kìa", ひへっ→"Hihe" — giữ nguyên theo quy tắc ngẫu hứng (diễn chơi theo tiếng Việt, không phiên âm 1:1).

## §5. Lượt soát 2 + kiểm chứng máy

- Lượt soát 2 (đọc lại toàn bộ 12 fix đối chiếu JP): **12 / 12 / 0 / 0** (tổng / xác minh lại / loại bỏ / sửa đổi).
- Kiểm chứng máy: JSON 12 mục, khóa là chuỗi; khối TOML parse được (tomllib), 12 khóa, **0 sai lệch giá trị** so với JSON; jp/tw/old_vn khớp CSV3 tuyệt đối **12/12**; mỗi fix chỉ khác VN cũ ở đúng vùng thay đổi mục tiêu (kiểm tra bằng diff — 11 fix là 1 lần chèn duy nhất, 970 là 1 vùng thay thế duy nhất).
- Ghi chú kiểm chứng: lúc ráp JSON, kiểm tra diff phát hiện 11 giá trị fix nháp bị thiếu ngoặc 「」 (lỗi chép tay khi ráp, không phải lỗi dịch) — đã sửa lại cho khớp VN cũ trước khi chốt; các giá trị cuối cùng trong JSON + khối TOML đều đã khớp máy 12/12.

## Khối TOML (đã kiểm chứng parse)

```toml
"792" = "「——Ư」"
"970" = "「Đến rồi! Đến rồi——A——Ưm——Nóng quá——Tinh dịch——Bụng——Vào trong tử cung——」"
"1011" = "「Ơ, xin lỗi——Ư!?」"
"1046" = "「A——Ngực! Ưm——Em——Bị anh hai——Ưm, ngực——Mút mát——Cho em.」"
"1051" = "「Ư! A——」"
"1056" = "「Ngoạm——Ư——Liếm——Liếm——Mút.」"
"1222" = "「Anh——hai——em——Ư——Hơ——A——Không sao——đâu——」"
"1230" = "「Ư!」"
"1231" = "「Ư!!!」"
"1232" = "「Ư!!?」"
"1237" = "「~~~~~~Ư!!」"
"1670" = "Đôi mắt Hibiki cong lên thành hình vòng cung đầy vẻ vui sướng——Ư!?"
```

## Kết bài

File 日々姫h1_マッサージの続き: đọc 329/329 dòng, **12 dòng sai (3,6%)** — gasp 10 (6 mục sweep nhận nguyên + 4 sweep bỏ sót), dịch sai nghĩa 2. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo/mồ côi, không chưa dịch, không trùng khóa. Đại từ Soutetsu sạch (anh với Hibiki toàn bộ). Cờ chờ Hieu: 4 dòng fa/fu "Phù" → unification; 1383 monologue lẫn "Anh"/"tôi"; 1059 しゅごっ→"Sướng quá"; 1025 ふぇ？→"Hả?"; 1015 lời ngọng thè lưỡi. Lượt soát 2: 12/12/0/0. Khối TOML 12 khóa parse OK, 0 sai lệch.
