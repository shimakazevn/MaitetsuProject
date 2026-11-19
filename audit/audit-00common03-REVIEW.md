# Audit — 00_Common file 03 (共通03_ハチロクとナビ)

File: `共通03_ハチロクとナビ.txt.toml` — Common Route chương 3, Hachiroku gặp Navi trên máy bay thử nghiệm EFL-T007.
Audit ngày 19/11/2026. Đọc toàn bộ từng dòng đối chiếu JP + TW, theo brief audit chuẩn (JP thắng TW khi lệch; kiểm tra chuỗi xoay, tràn chương khác, tag %l, quét đại từ Soutetsu, mẫu rên っ).

## ⚠️ Phát hiện về nguồn: CSV có HAI bộ dòng cho file này — chỉ một bộ đúng

CSV "Trang tính 3" liệt kê file này **hai lần**, dưới hai thư mục khác nhau, mỗi bộ 315 dòng, cùng key, cùng JP ở 267 key nhưng **VN khác nhau ở 287/315 key** và **JP khác nhau ở 48 key**:

- Bộ `translation_toml\01_Hachiroku\` — **khớp 100% với TOML**: 104 khớp y hệt + 211 khớp sau khi gỡ `\n` (TOML-2 làm phẳng `\n` thành khoảng trắng) = **315/315, 0 lệch**; JP khớp 100% với `# JP:` comment trong TOML.
- Bộ `translation_toml\00_Common\` — **mồ côi, KHÔNG khớp TOML**: chỉ 24 khớp y hệt, 287 lệch VN, 48 lệch JP (vd. 1385, 2028, 2030). Đây là bản cũ của file, không phải bản đang dùng.

TOML chỉ tồn tại một bản duy nhất dưới `00_Common/` (md5 `5bb90d70f91d54136f8ec4b7b1290c5d`, không có file trùng lặp nào trong toàn dự án). **Audit này dùng bộ `01_Hachiroku` làm nguồn JP/TW/VN** — cùng mẫu như lr_ふかみh2 (bộ `11_Other` mới đúng, bộ `07_` mồ côi). **Số dòng thực của file là 315, không phải 630** như đếm thô từ CSV (630 = 315 dòng thật + 315 dòng mồ côi). Bộ `00_Common` mồ côi phải được loại khỏi CSV trước khi rebuild, nếu không import theo File+Key sẽ ghi đè 287 dòng đúng bằng 287 dòng cũ.

Kiểm tra CSV↔TOML (bộ đúng): 315/315 key khớp, 0 lệch nội dung (ngoài 211 dòng `\n` bị làm phẳng trong TOML — CSV giữ `\n` gốc nên CSV là chuẩn cho fix list). `# JP:` comment đủ 315/315 key script. File giữ BOM + CRLF.

## Tổng kết: 15/315 dòng sai (4,8%)

| Loại | Số dòng | Key |
|---|---|---|
| Thuật ngữ | 5 | 911, 912 (帝鉄→Teitetsu); 1200, 1435, 1506 (御一夜→Ohitoyo) |
| Xưng hô | 3 | 1147 (Navi→Soutetsu "cô"→"anh"); 1430, 2025 (Soutetsu "mình"→"tôi") |
| Rên っ | 4 | 1273, 1274 (sweep), 1309 (sweep-missed), 1323 (sweep) |
| SFX | 1 | 2106 (mất tiếng cười ふふ) |
| Nhỏ/văn phong | 1 | 1358 ("cú giáng trời giáng!") |
| **Tổng** | **14** | |

Lệch dòng (misaligned): **0**. Chuỗi xoay (rotation chain): **0**. Tràn từ chương khác: **0** (không có dòng Việt nào thuộc về key khác trong file hay chương khác — 20 dòng Việt trùng với file khác đều là câu ngắn stock như 「うむ」→"Ừm.", 「ああ」→"À.", 「なるほど」→"Ra là vậy."). Dòng mồ côi (orphan VN): **0**. Dòng chưa dịch: **0**. Trùng key: **0** (VN trùng lặp trong file: 0; JP trùng lặp: 0).

Nhân vật: monologue 115, ハチロク 99, 双鉄 88, ナビ 13. Không có Paulette trong file này nên quy tắc B4 (tên trần "Soutetsu"→"anh Soutetsu") không phát sinh; dòng 1660 「双鉄……様」→"Ngài……Soutetsu" không phải tên trần (có "Ngài" = 様), giữ nguyên.

## 15 dòng sai (chi tiết)

### [911] — Thuật ngữ
- **JP:** 「\x%l帝鉄;#00ffc040;帝鉄%l;#;末期……」
- **Cũ:** 「Cuối thời kỳ \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;……」
- **Mới:** 「Cuối thời kỳ \x%l帝鉄;#00ffc040;Teitetsu%l;#;……」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11 (bỏ "Đường sắt Hoàng gia" — 帝鉄 là 帝国鉄道, không phải 皇室).

### [912] — Thuật ngữ
- **JP:** 「\x%l帝鉄;#00ffc040;帝鉄%l;#;末期には、\x%l保線;#00ffc040;保線%l;#;係の不足も甚だしい物となりました。\nあの時期、鉄道事故が多発した一因は、それです」
- **Cũ:** 「Vào cuối thời kỳ \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, tình trạng thiếu hụt nhân viên \x%l保線;#00ffc040;bảo trì đường ray%l;#; đã trở nên vô cùng nghiêm trọng.\nĐó chính là một trong những nguyên nhân khiến tai nạn đường sắt xảy ra liên tục vào thời điểm đó.」
- **Mới:** 「Vào cuối thời kỳ \x%l帝鉄;#00ffc040;Teitetsu%l;#;, tình trạng thiếu hụt nhân viên \x%l保線;#00ffc040;bảo trì đường ray%l;#; đã trở nên vô cùng nghiêm trọng. Đó chính là một trong những nguyên nhân khiến tai nạn đường sắt xảy ra liên tục vào thời điểm đó.」
- **Lý do:** 帝鉄 → Teitetsu theo quyết định 19/11; gộp `\n` thành một dòng theo quy ước fix (game tự ngắt dòng).

### [1147] — Xưng hô
- **JP:** 「隠れてなどいません。\n本機の姿は、あなたの視界に捉えられています」 (Navi nói với Soutetsu)
- **Cũ:** 「Tôi không hề lẩn trốn.\nHình dáng của hệ thống này vẫn luôn nằm trong tầm nhìn của cô đấy.」
- **Mới:** 「Tôi không hề lẩn trốn. Hình dáng của hệ thống này vẫn luôn nằm trong tầm nhìn của anh đấy.」
- **Lý do:** Navi nói với Soutetsu (nam) mà VN dùng "cô" — sai xưng hô. Kiểm tra toàn dự án: Navi gọi Soutetsu là "anh" (vd. lr真闇追加01 1372); "cô" cho Soutetsu chỉ xuất hiện đúng dòng này trong 148 dòng Navi nói. Sửa thành "anh".

### [1200] — Thuật ngữ
- **JP:** 「人が悪いのも仕方ないのだ。\nなにせ僕は、御一夜市の生まれではない」
- **Cũ:** 「Xấu tính thì cũng đành chịu thôi.\nDù sao thì tôi cũng không sinh ra ở thành phố Ohimitera mà.」
- **Mới:** 「Xấu tính thì cũng đành chịu thôi. Dù sao thì tôi cũng không sinh ra ở thành phố Ohitoyo mà.」
- **Lý do:** 御一夜 → Ohitoyo theo quyết định 19/11 (không dùng Ohimitera). File này có 3 dòng Ohimitera (1200, 1435, 1506) — sửa hết, còn 0 dòng cũ trong file.

### [1273] — Rên っ (sweep)
- **JP:** 「っ！！！」
- **Cũ:** 「!!!」
- **Mới:** 「Ư!!!」
- **Lý do:** Sweep gasp (lost-gasp-whole): JP là tiếng rên っ!!! nguyên dòng, TW 啊!!!, VN chỉ còn "!!!" — mất âm. Fix theo sweep.

### [1274] — Rên っ (sweep)
- **JP:** 「っ！？」 (TW 啊!?)
- **Cũ:** 「!?」
- **Mới:** 「Ư!?」
- **Lý do:** Sweep gasp (lost-gasp-whole): JP っ!? nguyên dòng, VN chỉ còn "!?". Fix theo sweep.

### [1309] — Rên っ (sweep-missed)
- **JP:** 「はい。かしこまりました双鉄様――\nっ！？　なにっ？　\x%l共感;#00ffc040;共感%l;#;っ！？」
- **Cũ:** 「Vâng. Em hiểu rồi thưa ngài Soutetsu——\n!? Cái gì? \x%l共感;#00ffc040;Cộng cảm%l;#;!?」
- **Mới:** 「Vâng. Em hiểu rồi thưa ngài Soutetsu——Ư!? Cái gì? \x%l共感;#00ffc040;Cộng cảm%l;#;!?」
- **Lý do:** Sweep bỏ sót: JP có 3 tiếng っ — っ!? đứng một mình sau ―― là tiếng rên thật (Hachiroku giật mình giữa câu), VN chỉ còn "!?". Hai っ còn lại (なにっ? / 共感っ!?) là っ nhấn mạnh gắn vào từ, theo quy tắc không thêm Ư. Chỉ thêm Ư cho tiếng rên đứng một mình.

### [1323] — Rên っ (sweep)
- **JP:** 「そうであっても！　\x%lエアクラ;#00ffc040;エアクラ%l;#;になぞっ」
- **Cũ:** 「Dù có vậy đi chăng nữa! Em cũng không thèm đi \x%lエアクラ;#00ffc040;Aircra%l;#;っ」
- **Mới:** 「Dù có vậy đi chăng nữa! Em cũng không thèm đi \x%lエアクラ;#00ffc040;Aircra%l;#;Ư」
- **Lý do:** Sweep gasp (raw-tsu): VN còn nguyên ký tự Nhật っ ở cuối câu. Fix theo sweep.

### [1358] — Nhỏ/văn phong
- **JP:** 「ハチロクが想像しているのの、多分数倍は痛い奴だ。\nこつんでもごつんでもなく、ガン！　と来た」
- **Cũ:** 「Chắc chắn là đau gấp mấy lần những gì Hachiroku tưởng tượng đấy.\nKhông phải là cái gõ nhẹ hay cái cốc đầu đâu, mà là một cú giáng trời giáng! luôn.」
- **Mới:** 「Chắc chắn là đau gấp mấy lần những gì Hachiroku tưởng tượng đấy. Không phải là cái gõ nhẹ hay cái cốc đầu đâu, mà là một cú trời giáng! luôn.」
- **Lý do:** "một cú giáng trời giáng!" lặp từ "giáng" hai lần, đọc lủng củng. JP ガン!と来た = một cú trời giáng.

### [1430] — Xưng hô
- **JP:** 「そうだな。僕もそう思った。そして同時に――\nこの人は僕を叱ってくれると、ホっとした」 (Soutetsu độc thoại)
- **Cũ:** 「Đúng vậy. Tôi cũng nghĩ thế. Và đồng thời——\nTôi cảm thấy nhẹ nhõm vì người này đã chịu mắng mình.」
- **Mới:** 「Đúng vậy. Tôi cũng nghĩ thế. Và đồng thời—— Tôi cảm thấy nhẹ nhõm vì người này đã chịu mắng tôi.」
- **Lý do:** Soutetsu độc thoại dùng "mình" làm tân ngữ ("mắng mình" = mắng tôi) — theo tiền lệ pilot 1652 ("đứa em gái đã đẩy mình ra" → "đã đẩy tôi ra"), tân ngữ "mình" của Soutetsu phải về "tôi". ("Mình" ở mệnh đề phụ/quan hệ/sở hữu/phản thân không tính lỗi — tiền lệ hearing 2151/2247/2248.)

### [1435] — Thuật ngữ
- **JP:** 「御一夜[じょうし,1]城址。あそこからも御一夜の町並みを見下ろせる。\n無論、ここからほどに広くは無理だが」
- **Cũ:** 「Đó là tàn tích thành Ohimitera. Từ đó cũng có thể nhìn xuống toàn cảnh thành phố.\nTất nhiên là không thể rộng bằng góc nhìn từ trên này được.」
- **Mới:** 「Đó là tàn tích thành Ohitoyo. Từ đó cũng có thể nhìn xuống toàn cảnh thành phố. Tất nhiên là không thể rộng bằng góc nhìn từ trên này được.」
- **Lý do:** 御一夜城址 → "tàn tích thành Ohitoyo" theo quyết định 19/11.

### [1506] — Thuật ngữ
- **JP:** 「歩いて見る御一夜の町は、また別の顔だ。\n歩くうち、あるいは見覚えに出くわすかもしれん」
- **Cũ:** 「Thành phố Ohimitera khi dạo bước ngắm nhìn sẽ mang một vẻ đẹp khác.\nTrong lúc đi dạo, biết đâu em lại bắt gặp một khung cảnh quen thuộc nào đó.」
- **Mới:** 「Thành phố Ohitoyo khi dạo bước ngắm nhìn sẽ mang một vẻ đẹp khác. Trong lúc đi dạo, biết đâu em lại bắt gặp một khung cảnh quen thuộc nào đó.」
- **Lý do:** 御一夜の町 → "Thành phố Ohitoyo" theo quyết định 19/11.

### [2025] — Xưng hô
- **JP:** ごくまっとうに、ごくごく普通に――\n僕を扱ってくれる人間に、ようやく出会えて。 (Soutetsu độc thoại)
- **Cũ:** 「Một cách rất chính đáng, rất đỗi bình thường——\nCuối cùng tôi cũng gặp được những người đối xử với mình như bao người khác.」
- **Mới:** 「Một cách rất chính đáng, rất đỗi bình thường—— Cuối cùng tôi cũng gặp được những người đối xử với tôi như bao người khác.」
- **Lý do:** Soutetsu độc thoại dùng "mình" làm tân ngữ ("đối xử với mình" = đối xử với tôi) — theo tiền lệ pilot 1652, về "tôi".

### [2106] — SFX
- **JP:** 素朴な疑問を伝えれば、\nハチロクはふふ、と満足そうな笑みを浮かべる。 (monologue)
- **Cũ:** 「Khi tôi nói ra thắc mắc giản đơn đó,\nHachiroku mỉm cười đầy mãn nguyện.」
- **Mới:** 「Khi tôi nói ra thắc mắc giản đơn đó, Hachiroku khẽ bật cười đầy mãn nguyện.」
- **Lý do:** JP có tiếng cười ふふ (Hachiroku "fufu" rồi mỉm cười mãn nguyện) mà VN chỉ còn "mỉm cười" — mất âm cười. Quy tắc "không để mất âm": thêm tiếng cười "khẽ bật cười".

## Đối chiếu sweep rên っ

Sweep có 5 entry cho file này: 3 fix đã nhận nguyên văn (1273, 1274, 1323); 2 entry "needs-file-audit" đã kiểm tra xong, **không cần sửa**: 1547 「左様ですね」→"Đúng vậy nhỉ." (JP/TW/VN đều khớp, không có っ); 2036 「――っ！」→"——A!" (tiếng rên được diễn thành "A!" — giữ âm, hợp quy tắc ngẫu hứng, nhất quán với 1661 「っ！」→"A!"). Ngoài ra audit tìm thêm **1 sweep-missed** (1309, xem trên). Tổng JP có っ: 94 dòng; chỉ 4 dòng mất âm.

## Tag %l

Sạch: 0 tag lỗi trong file. Số lượng tag JP = VN ở mọi dòng (kiểm tra từng dòng). Không có tag thiếu dấu `;` đóng, không có tag thừa/thiếu. Gloss 機関士 "người lái tàu" / 運転士 "nhân viên cơ vụ" (1638, 2108) giữ theo quy ước thiểu số đã chốt, không tính lỗi. Gloss 帝鉄 "Teitetsu" ở 911/912 đã sửa trong fix list (chỉ đổi gloss, giữ nguyên tag).

## Phân tích xưng hô (đã kiểm tra hết, không chỉ heuristic)

- **Soutetsu → Hachiroku "em":** nhất quán toàn file (65 dòng "em", tất cả đều là Hachiroku tự xưng "em" hoặc Soutetsu gọi Hachiroku "em"). 0 dòng "anh" trong VN — Soutetsu không tự xưng "anh" lần nào ở file này.
- **Soutetsu "mình":** 19 lần xuất hiện, chỉ **2 lần sai** (1430, 2025 — tân ngữ "mình" trong độc thoại, xem trên). Các lần còn lại đều đúng theo tiền lệ hearing: sở hữu ("của mình", "sức mình", "trái tim mình"), phản thân ("chính mình", "bản thân mình"), mệnh đề phụ/quan hệ ("những phần mình đã nắm được", "nghĩ mình có thể…", "như mình cũng sắp…"), thành ngữ ("giật mình", "hết sức mình"). **Không có** "mình" làm chủ ngữ mệnh đề chính trong độc thoại Soutetsu ở file này.
- **Hachiroku "mình":** 1523 ("không nhớ mình đã từng…", mệnh đề phụ), 1581 ("bộ dạng khó coi của mình", sở hữu), 1604 ("bản thân mình", phản thân) — đều đúng, không phải lỗi.
- **Navi "cô":** 1680 (Soutetsu gọi Navi "cô"), 2030 + 2050 (monologue "cô ấy" chỉ Navi) — **giữ nguyên**: "cô" cho Navi là cách dùng đã chốt trong dự án (17 lần Soutetsu→Navi "cô" toàn dự án, có cả file 01 pilot đã duyệt 1308; monologue "cô ấy" cho Navi 6 lần vs "em ấy" 2 lần). Chỉ 1147 là sai vì đối tượng là Soutetsu (nam).
- **Navi → Hachiroku "cô"** (1294): đúng, Hachiroku mang hình nữ.
- **"cô Hibiki"** (1661), **"cô gái tóc vàng"** (2066): đúng, cả hai đều là nữ.
- **"chị ấy"** (1427, 1577): đúng — người phụ nữ mắng Soutetsu bằng tiếng Kumamoto là **chị Mayami** (xác nhận ở 1562 「真闇姉に、こっぴどく怒られてげんこつをもらった」→"bị chị Mayami mắng…").
- **"em ấy"** (1633): đúng — chỉ Mayami ("Em ấy ghét chuyện tôi là con nuôi").

## Dòng không chắc chắn: 1

### [1318] — ĐÃ CHỐT theo Hieu (19/11 23:37): hướng 'còn nợ'
- **JP:** 「怒ってないから、むしろです。\n平手打ちを余分にひとつ。わたくしは双鉄様に」 (Hachiroku; câu bị cụt, không có động từ)
- **TW:** 「就是因為不生氣了才這麼說。我還欠雙鐵少爺一件事才算扯平了」 (tôi còn nợ ngài Soutetsu một việc mới hòa)
- **Cũ:** 「Chính vì không giận nên mới thế ạ.\nMột cái tát tay thừa thãi. Em đã dành cho ngài Soutetsu.」
- **Vấn đề:** JP cụt ở 「わたくしは双鉄様に」 (không động từ) nên hướng nghĩa mơ hồ: TW đọc là Hachiroku **còn nợ** Soutetsu một cái tát (để hòa nhau — khớp mạch おあいこ xuyên suốt cảnh này: 1306, 1380 "hòa nhau, sòng phẳng"); VN đọc là cô ấy **đã dành cho** (đã tát) ngài Soutetsu một cái tát thừa. Hai hướng ngược nhau, JP không tự quyết được. Ứng viên sửa (theo TW + mạch truyện): 「Chính vì không giận nên mới thế ạ. Một cái tát thừa. Em còn nợ ngài Soutetsu một cái.」 — **đã áp dụng theo quyết định của Hieu (19/11 23:37)**.

## Cố tình KHÔNG sửa (đã kiểm tra, có lý do)

- **887** 「エアクラそのものが、名前の中に、そもそも悪を内包するような存在です」→"Bản thân Aircra, ngay từ cái tên đã bao hàm ý nghĩa của cái ác rồi." — lược "là một tồn tại" nhưng ý chính (cái tên chứa cái ác) còn nguyên, câu Việt đọc trơn.
- **1247** 「目視でしか？　それでは人間と」→"Chỉ bằng mắt thường sao? Vậy thì có khác gì con người." — JP cụt nhưng hàm ý duy nhất là "thì chẳng khác gì con người"; không phải bịa thêm nội dung mới.
- **1291** うふふ → "Ufufu" — tiếng cười, diễn thành tiếng cười theo quy tắc 22:05.
- **1457** 「何者ですかっ！？」→"Kẻ nào đó!?" — đọc như "Ai đó!?" trong tiếng Việt, chấp nhận được.
- **1546** ふふっ → "fufu" — tiếng cười, giữ nguyên dạng Latin theo quy tắc ngẫu hứng.
- **1631** 「ならば降りますっ！」→"Vậy thì em sẽ xuống!" — っ cuối câu gắn vào động từ là nhấn mạnh, không phải rên, không thêm Ư theo quy tắc.
- **1645** 「レイ"ルロオ"ド」→'Rei-"ruroo"-do' — giữ âm Nhật theo nguyên tắc giữ gần tiếng Nhật; nghĩa chơi chữ (ルロオ = 流浪) được giải ngay câu sau ("chịu cảnh lưu lang").
- **1660** 「双鉄……様」→"Ngài……Soutetsu" — có "Ngài" (= 様), không phải tên trần; vị trí ngập ngừng khác JP nhưng hiệu ứng ngập ngừng khi gọi tên vẫn giữ.
- **1661, 2036** っ！ → "A!" — tiếng rên được diễn thành "A!" (giật mình nhận ra), giữ âm, hợp quy tắc ngẫu hứng.
- **1886** 「エ"アク"ラ」→'E"aku"ra' — giữ chơi chữ âm Nhật (aku = ác).
- **2117** （ぐう～～っ）→（Ọt~~） và **2118** （ピンっ！）→（Búng!） — onomatopoeia Việt tương đương, giữ âm.
- **"Phun cát" / "dồn toa":** file này không có dòng 砂撒き nên câu hỏi pilot (1) không phát sinh ở đây.
- **"RailRoad"** (1374), **"Lord"** (1386): giữ nguyên dạng Latin như TW và bản gốc, có chủ ý.

## Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 14 fix so với JP của từng dòng: **tổng 14 / kiểm tra lại 14 / loại bỏ 0 / sửa 10**. Lần 2 bắt được 1 lỗi hệ thống trong bản thảo fix: 10 fix cho dòng thoại bị thiếu dấu 「」 (911, 912, 1147, 1200, 1309, 1323, 1358, 1430, 1435, 1506) — đã bổ sung lại và kiểm tra chẵn lẻ 「」 giữa JP và fix cho cả 14 dòng. Parse-check riêng là chưa đủ; con số trên là từ lần đọc lại bằng mắt.

Khối TOML dưới đây đã parse-verified bằng tomllib: **15 key, 0 lệch giá trị** so với JSON fix list (`audit-00common03-wrong.json`). Bổ sung 19/11 23:37 (parent): dòng 1318 thêm vào theo quyết định của Hieu (hướng 'còn nợ' theo TW); fix đã kiểm chứng với JP/TW trong CSV3 (bộ 01_Hachiroku) và comment `# JP:` trong TOML.

## Khối TOML (fix)

```toml
[script]
911 = "「Cuối thời kỳ \\x%l帝鉄;#00ffc040;Teitetsu%l;#;……」"
912 = "「Vào cuối thời kỳ \\x%l帝鉄;#00ffc040;Teitetsu%l;#;, tình trạng thiếu hụt nhân viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#; đã trở nên vô cùng nghiêm trọng. Đó chính là một trong những nguyên nhân khiến tai nạn đường sắt xảy ra liên tục vào thời điểm đó.」"
1147 = "「Tôi không hề lẩn trốn. Hình dáng của hệ thống này vẫn luôn nằm trong tầm nhìn của anh đấy.」"
1200 = "「Xấu tính thì cũng đành chịu thôi. Dù sao thì tôi cũng không sinh ra ở thành phố Ohitoyo mà.」"
1273 = "「Ư!!!」"
1274 = "「Ư!?」"
1309 = "「Vâng. Em hiểu rồi thưa ngài Soutetsu——Ư!? Cái gì? \\x%l共感;#00ffc040;Cộng cảm%l;#;!?」"
1318 = "「Chính vì không giận nên mới thế ạ. Một cái tát thừa. Em còn nợ ngài Soutetsu một cái.」"
1323 = "「Dù có vậy đi chăng nữa! Em cũng không thèm đi \\x%lエアクラ;#00ffc040;Aircra%l;#;Ư」"
1358 = "「Chắc chắn là đau gấp mấy lần những gì Hachiroku tưởng tượng đấy. Không phải là cái gõ nhẹ hay cái cốc đầu đâu, mà là một cú trời giáng! luôn.」"
1430 = "「Đúng vậy. Tôi cũng nghĩ thế. Và đồng thời—— Tôi cảm thấy nhẹ nhõm vì người này đã chịu mắng tôi.」"
1435 = "「Đó là tàn tích thành Ohitoyo. Từ đó cũng có thể nhìn xuống toàn cảnh thành phố. Tất nhiên là không thể rộng bằng góc nhìn từ trên này được.」"
1506 = "「Thành phố Ohitoyo khi dạo bước ngắm nhìn sẽ mang một vẻ đẹp khác. Trong lúc đi dạo, biết đâu em lại bắt gặp một khung cảnh quen thuộc nào đó.」"
2025 = "Một cách rất chính đáng, rất đỗi bình thường—— Cuối cùng tôi cũng gặp được những người đối xử với tôi như bao người khác."
2106 = "Khi tôi nói ra thắc mắc giản đơn đó, Hachiroku khẽ bật cười đầy mãn nguyện."
```

## Kết bài

File 03 là file sạch thứ ba của dự án tính đến nay (4,8% sai, sau 実りの秋 0,4% và ヒヤリング 2,0%): **không lệch dòng, không chuỗi xoay, không tràn chương, không dòng mồ côi** — cột Việt đứng đúng chỗ ở cả 315 dòng, khác hẳn Paulette 03 (30,9–56%). 15 lỗi còn lại đều là lỗi lẻ tẻ: 5 thuật ngữ theo quyết định mới (Teitetsu ×2, Ohitoyo ×3), 3 xưng hô (1 Navi→Soutetsu "cô", 2 Soutetsu "mình" tân ngữ), 4 rên っ (3 sweep + 1 sweep-missed), 1 SFX mất tiếng cười, 1 văn phong, 1 nghĩa (1318). Dòng 1318 **đã chốt theo Hieu (19/11 23:37)**: hướng 'còn nợ' theo TW + mạch おあいこ; **0 dòng chưa chắc chắn**.

Phát hiện quan trọng nhất của file này không nằm trong 14 lỗi mà ở **nguồn dữ liệu**: CSV mang hai bộ dòng cho cùng một file, bộ dưới `00_Common\` là bản cũ mồ côi (287 dòng Việt khác + 48 dòng JP khác so với TOML). Ai rebuild từ CSV mà không loại bộ mồ côi sẽ ghi đè 287 dòng đúng bằng bản cũ — cùng kiểu bẫy như lr_ふかみh2. Trước khi rebuild toàn dự án, phải loại 10 bộ mồ côi (đã quét toàn bộ CSV 19/11 — xem dual-csv-sets.md).
