# Audit — 日々姫05_御一夜ステーションカフェ (02_Hibiki) — "Quán cà phê ga Ohitoyo"

- File: `日々姫05_御一夜ステーションカフェ.txt.toml` — route 02_Hibiki, **577 dòng script**, 4 strong candidates, 1 copy (không trùng lặp).
- Nội dung: ngày chạy thử quán cà phê ga Ohitoyo (Gamadas Café đổi tên) — Soutetsu và Hibiki phục vụ khách trong toa ăn: Hachiroku, Reina, Paulette, Kisaki, Fukami, Nagi, phu nhân Nagayama và các gia đình có trẻ con; thực đơn SL curry / dầu diesel / than đá; cuộc thi đặt biệt danh cho quán; chủ đề "mảnh ghép hạnh phúc" và hình ảnh bướm lột xác; sự bảo bọc quá mức của Mayami; chuyện cái chăn đắp cho hai người ngủ quên; kết bằng lời thề của Soutetsu sẽ làm ngọn gió nâng cánh Hibiki.
- Phương pháp: đọc hết 577/577 dòng theo JP + TW (CSV3, 1 set duy nhất — xem §5), đối chiếu TOML-2. Không lấy mẫu. Key không theo thứ tự truyện (độc thoại / đối thoại / cảnh H xen kẽ theo key) — xác định người nói/người nghe theo nội dung và dòng kề.

## §1. Kết quả

**13 dòng sai / 577 (2,3%)** — file khá sạch; lỗi rải rác, không có lỗi hệ thống.

- Lệch vị trí (misaligned) **0**, chuỗi xoay (rotation) **0**, nhiễm chéo file khác **0**, dòng mồ côi (orphan) **0**, chưa dịch **0**, trùng khóa **0**.
- Phân loại (13): xưng hô 4 (1518, 2212, 2407, 2577), gasp 4 (2040, 2069, 2967, 3330 — cả 4 đều từ sweep), SFX 4 (1509, 1909, 2081, 2364), sai nghĩa 1 (3179).
- `[selections]` rỗng (0 mục). Thẻ `%l`: 3 thẻ (2854 ×2, 3041 ×1), đầy đủ mở/đóng, thuật ngữ JP giữ nguyên, gloss dịch đúng (種車→"toa xe nguyên bản", ディーゼル気動車→"toa xe diesel tự hành") — không có thẻ `%l` sai định dạng.
- Không có bản sao file này (md5 duy nhất trong toàn bộ TOML-2; 1 copy, không áp fix 2 nơi).
- 4 strong candidates của queue chỉ là heuristic; lần đọc toàn bộ tìm ra 13 dòng sai (2,3%).

## §2. Chi tiết từng dòng sai

### Xưng hô — Soutetsu tự xưng sai người nghe (4 dòng)

Quy tắc đã chốt: Soutetsu "anh" với Hibiki/Reina/Paulette/Fukami/Nagi, "tôi" với Hachiroku/Mayami/Minokasa/Kisaki; độc thoại "tôi" (ngoại lệ "mình" chỉ cho độc thoại nội tâm tự vấn cảm xúc).

- **1518** (双鉄). JP: 「……だからこそ、応えねばな」. Dòng kề 1515/1516 đều là Hibiki nói với Soutetsu → người nghe là Hibiki → "anh". VN cũ: 「……Chính vì vậy, **tôi** phải đáp lại.」 → **「……Chính vì vậy, anh phải đáp lại.」**
- **2212** (双鉄). JP: 「うむ！　僕は何を手伝えばいい？」. Dòng kề 2210 là Hachiroku hỏi "không cần em giúp đâu nhỉ?" → Soutetsu đáp lại Hachiroku → "tôi". VN cũ: 「Ừm! **Anh** nên giúp gì đây?」 → **「Ừm! Tôi nên giúp gì đây?」**
- **2407** (双鉄). JP: 「毛布、真闇姉がかけてくれたのだよな。ありがとう。おかげで風邪も引かずに済んだ」 — Soutetsu cảm ơn Mayami (người đắp chăn) → "tôi". VN cũ: 「Cái chăn, là chị Mayami đắp cho **em** đúng không. Cảm ơn chị. Nhờ vậy mà **em** không bị cảm.」 → **「Cái chăn, là chị Mayami đắp cho tôi đúng không. Cảm ơn chị. Nhờ vậy mà tôi không bị cảm.」** (sửa cả 2 chỗ "em").
- **2577** (双鉄, độc thoại không có 「」). JP: 「あのころは……\n僕にも理解できてなかったが」. Đây là độc thoại kể chuyện, không phải đối thoại với Hibiki → "tôi" như mọi dòng độc thoại khác trong file (2799, 2808, 2819, 2841, 2943, 3032 đều "tôi"). VN cũ: 「Hồi đó……\n**Anh** cũng không hiểu được, nhưng mà.」 → **「Hồi đó……\nTôi cũng không hiểu được, nhưng mà.」**

### Gasp — mất tiếng thở/っ (4 dòng, cả 4 đều từ sweep)

Sweep có đúng 4 mục cho file này (`sweep-raw-gasp-wrong.json`), cả 4 đều kiểm chứng đúng với JP và được áp dụng nguyên dạng.

- **2040** (ハチロク). JP: 「あらいやだ。わたくしとしたことが、\n何を今さら、未練がましいことなど――っ！」 — sweep `lost-gasp-trailing`. VN cũ: 「……đến nước này rồi còn vương vấn cái gì chứ——!」 → **「……đến nước này rồi còn vương vấn cái gì chứ——Ư!」**
- **2069** (ハチロク). JP: 「っ！」; TW: 「唔！」 — sweep `lost-gasp-whole`, gasp cả dòng. VN cũ: 「!」 → **「Ư!」**
- **2967** (monologue). JP: 「風船のようにまぁるく、丸く、\nまるでお腹がふくらんだような――っ！！？」 — sweep `lost-gasp-trailing`. VN cũ: 「Tròn xoe như quả bóng bay,\ncứ như thể bụng đang to ra vậy——!!?」 → **「Tròn xoe như quả bóng bay,\ncứ như thể bụng đang to ra vậy——Ư!!?」**
- **3330** (monologue). JP: 「そうして僕は、風を吹かそう。\nいつか日々姫が羽ばたくときには――っ！」 — sweep `lost-gasp-trailing`. VN cũ: 「Và rồi tôi, sẽ tạo ra một cơn gió.\nĐể một ngày nào đó khi Hibiki vỗ cánh——!」 → **「Và rồi tôi, sẽ tạo ra một cơn gió.\nĐể một ngày nào đó khi Hibiki vỗ cánh——Ư!」**

### SFX — độ dài nguyên âm / mất tiếng (4 dòng)

- **1509** (ハチロク). JP: 「…………ふぅ」. Công thức độ dài nguyên âm đã chốt (VN = 1 + số う/ぅ trong JP): ふぅ có 1 う → "Phùù" (2 u). Tiền lệ: một audit trước đã sửa ふぅ → "Phùù" với đúng lý do này. VN cũ: 「…………Phù.」 → **「…………Phùù.」**
- **2081** (双鉄). JP: 「ああっ」. VN cũ: 「A.」 — mất 1 nguyên âm (ああ → "A"), lại trùng hệt với 2076 「あ」 → "A." (hai dòng JP khác nhau không được dịch giống hệt — tiền lệ ふぅむ/ふむ). Tiền lệ sweep: ああっ cuối dòng được diễn bằng độ dài nguyên âm, không thêm Ư (vd. あああっ → "Aaa!"). → **「Aa.」**
- **2364** (双鉄). JP: 「ああっ、うむっ！　ならばっ、僕も」. VN cũ: 「A, ừm! Nếu vậy, anh cũng.」 — ああっ → "A" thiếu 1 nguyên âm; うむっ → "ừm!" và ならばっ → "Nếu vậy," giữ nguyên theo tiền lệ (っ cuối âm tiết được dấu "!" hấp thụ). → **「Aa, ừm! Nếu vậy, anh cũng.」**
- **1909** (永山). JP: 「失格よ～？　お客様にぶつかるなんて、\n下の下の下の下。[ゲゲゲ,2]下下下の[ゲ]下だわ」. VN cũ: 「Mất tư cách rồi nha~? Va phải khách hàng thế này,\ntệ của tệ của tệ của tệ. Tệ của tệ của tệ của tệ đấy.」 — vế sau lặp nguyên vế trước, mất hẳn tiếng cười/gag ゲゲゲ ("Gegege" — tiếng cười ma quái kiểu GeGeGe no Kitaro). Khác với các thẻ ruby đọc tên ([れいな,4], [まくら,1] — xem §3) vốn được bỏ theo thông lệ toàn dự án, đây là **âm thanh** (onomatopoeia), không phải cách đọc tên; TW cũng giữ chỗ cho nó bằng ＸＸＸ. → **「Mất tư cách rồi nha~? Va phải khách hàng thế này,\ntệ của tệ của tệ của tệ. [Gegege,2]Tệ tệ tệ của [Ge]tệ đấy.」** (khôi phục thẻ theo đúng mẫu 2143 đã giữ `[đứa bé đó,3]8620`). Điểm này Hieu nên xác nhận lại cách diễn — xem §7.

### Sai nghĩa (1 dòng)

- **3179** (monologue). JP: 「話す間も休めぬこの手を動かす度に、\nくすぐったそうに幸せそうに笑み崩れる――」 — くすぐったそうに = "trông nhột/buồn buồn vì bị cù". VN cũ: 「Mỗi lần bàn tay không ngừng nghỉ này khẽ vuốt ve trong lúc trò chuyện,\ncon bé lại cười rạng rỡ, trông vừa **buồn buồn buồn buồn** vừa hạnh phúc——」 — "buồn" lặp 4 lần đọc như "buồn (sad)" và là lỗi lặp từ; "nhột" mới là từ chuẩn cho cảm giác bị cù. → **「Mỗi lần bàn tay không ngừng nghỉ này khẽ vuốt ve trong lúc trò chuyện,\ncon bé lại cười rạng rỡ, trông vừa nhột vừa hạnh phúc——」**

## §3. Kiểm chứng chéo

- **Sweep:** 4 mục cho file này, cả 4 đúng và đã áp (2040, 2069, 2967, 3330). Không phát hiện thêm gasp nào sweep bỏ sót: các っ cuối âm tiết còn lại (1949 あああっ, 1950 なっ/あっ/違っ, 1968 あっ, 2018/2019 うふふっ/ふふふっ, 2039 ははっ, 2047 ええっ, 2068 うむっ, 2174 うおっ, 2412 んっ, 2529 きゃっ, 2587 ごめんっ) đều đã được diễn bằng dấu "!" hoặc âm tương ứng, đúng tiền lệ sweep (sweep không hề liệt kê dạng này trong 1.399 mục).
- **Rotation / lệch hàng:** 0 — đọc toàn bộ không thấy dòng nào mang nội dung của dòng khác; VN trùng lặp chỉ ở 5 cặp câu ngắn mà JP cũng giống hệt nhau (1932/2520 「おまたせいたしました」, 2087/2604 「！」, 2135/2378, 2208/2346 「かしこまりました」) — hợp lệ.
- **Nhiễm chéo file khác:** 0 — không dòng VN nào thuộc file khác; đã kiểm tra chỉ mục VN toàn dự án cho các dòng khả nghi (không có).
- **Thẻ ruby [x,N]:** file có 10 marker trong JP. 2143 `[あのこ,3]` đã được VN giữ nguyên mẫu ("[đứa bé đó,3]8620") — đúng, giữ. Các marker còn lại được VN bỏ **theo đúng thông lệ toàn dự án** (đã kiểm chứng qua CSV3: `[まくら,1]` bị bỏ trong mọi file khác kể cả file đã audit; `[れいななえす]` bị bỏ trong 共通04, 日々姫09, グランドリライト04/05, ポーレット10): 1936 `[めと]` (cách đọc của 娶 — VN "cưới em làm vợ" đã đủ nghĩa), 2246 `[ひとかけ,1]` ("một mảnh ghép"), 2572 `[みち]` ("con đường"), 3412 `[イムド,1]` ("cà ri Ấn Độ"), 2033 `[れいななえす,2]` và 2495 `[れいな,4]` (cách đọc tên KiHa 07S là "Reina" — VN "KiHa 07S" đã đủ). Chỉ 1909 `[ゲゲゲ,2]` được khôi phục vì đó là âm thanh, không phải cách đọc — xem §2.
- **Thuật ngữ chờ thống nhất (không tính sai):** "Ohimitera" 3 dòng (2560, 3223, 3285) — chờ đợt thống nhất Ohitoyo như các file trước.
- **TW sai / VN theo JP đúng:** 2098 TW bỏ "整理券" trong lời nhờ (VN "Nhờ anh phát vé chờ nhé" theo JP 「整理券お願いしますって」 là đúng); 3112 TW thêm "vừa có một nhóm rời đi" (VN "vừa vặn lúc này" theo JP 「ああ、いま丁度」 là đúng — JP vốn mơ hồ).

## §4. Các dòng đã xem xét nhưng KHÔNG sửa

- **1928** (双鉄). JP: 「いえ、こちらこそ失礼しました」 → VN: 「Không, là chú thất lễ mới đúng.」 — "chú" là Soutetsu tự xưng với khách nhí (cảnh quán có nhiều trẻ con: 児童a/b, ちびっこ, しょうちゃん); người nghe không xác định được chắc chắn từ key kề (1922–1926 đều là Soutetsu), nên giữ nguyên và ghi chú cho Hieu (xem §7).
- **1977** (双鉄). JP: 「少しだけ待っていてくれ。日々姫を部屋で寝かせてくる」 → VN "Đợi tôi một chút nhé. Tôi đưa Hibiki về phòng ngủ đã." — người nghe không phải Hibiki (nói về Hibiki ở ngôi ba) nên "tôi" là dạng trung tính đúng; giữ.
- **2038** (双鉄). JP: 「おわっ！？　っ――あ。すみません」 → VN: 「Oái!? ——A. Xin lỗi.」 — tiếng gasp っ trước あ chưa được diễn ("——ƯA" nghe gượng, ngoài phạm vi sweep); giữ và ghi chú cho Hieu (xem §7).
- **2291** (しょうちゃん). JP: 「のるー！　もどってくるー！」 → VN: 「Đi tàu! Quay lại!」 — TW thêm "ăn" (再回來吃) nhưng JP không có 食べる; VN theo JP là đúng; giữ.
- **1509/2081/2364** đã sửa theo công thức nguyên âm (xem §2); các tiếng cười 2018/2019/2021/2023 (うふふ/ふふふ → "Fufu"/"Fufufu") và ふわぁ 2029 → "Oa." đều đúng quy tắc cười = tiếng cười, không phải tiếng rên.
- **2460** (双鉄): "Chị Mayami, có lẽ đã bảo bọc em quá mức đấy." — "em" ở đây là Hibiki (người nghe), không phải Soutetsu tự xưng; giữ.
- **2338/2377** (双鉄 với Hachiroku): "cô" là cách Soutetsu gọi Hachiroku, nhất quán với 2338; giữ.

## §5. Kiểm chứng kỹ thuật

- CSV3: **1 set duy nhất** cho file này (577 dòng, `translation_toml\02_Hibiki\日々姫05_御一夜ステーションカフェ.txt.toml`), 0 trùng khóa, 0 VN trống, 0 JP trống.
- VN khớp TOML tuyệt đối sau chuẩn hóa `\\n`→khoảng trắng (**326/577 lệch chỉ là TOML-2 làm phẳng literal `\\n` thành khoảng trắng, 0 khác biệt thực chất**); TOML có 577 khóa `[script]`, key 1445–3551.
- TOML md5 `12bc7bb8e26f4336643e8b0b5d04dfc0`, 108.717 byte, UTF-8 BOM + CRLF. Không có bản sao file này trong TOML-2 (1 copy duy nhất).
- JSON 13 mục dạng chuẩn list-of-dicts, khóa chuỗi; khối TOML parse được bằng tomllib, 13 khóa, **0 sai lệch giá trị** so với JSON (so sánh chuỗi thô; `\\n` viết `\\\\n` nên parse ra đúng literal backslash-n của CSV3); jp/tw/old_vn khớp CSV3 tuyệt đối 13/13.
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (1509 thêm 1 chữ "u"; 1518/2212/2407/2577 đổi xưng hô; 2040/2069/2967/3330 thêm "Ư"; 2081/2364 thêm 1 nguyên âm "a"; 3179 "buồn buồn buồn buồn"→"nhột"; 1909 khôi phục thẻ [Gegege,2]/[Ge]).
- Lượt soát 2: **13/13 tái kiểm chứng, 0 bỏ, 0 sửa** — đọc lại toàn bộ 13 fix đối chiếu JP sau khi build JSON (bảng soát 2 in trong quá trình build; mọi fix đều giữ nguyên sau lượt soát).

## §6. Khối TOML (đã kiểm chứng parse)

```toml
"1509" = "「…………Phùù.」"
"1518" = "「……Chính vì vậy, anh phải đáp lại.」"
"1909" = "「Mất tư cách rồi nha~? Va phải khách hàng thế này,\\ntệ của tệ của tệ của tệ. [Gegege,2]Tệ tệ tệ của [Ge]tệ đấy.」"
"2040" = "「Ôi chao. Thật không giống mình chút nào,\\nđến nước này rồi còn vương vấn cái gì chứ——Ư!」"
"2069" = "「Ư!」"
"2081" = "「Aa.」"
"2212" = "「Ừm! Tôi nên giúp gì đây?」"
"2364" = "「Aa, ừm! Nếu vậy, anh cũng.」"
"2407" = "「Cái chăn, là chị Mayami đắp cho tôi đúng không.\\nCảm ơn chị. Nhờ vậy mà tôi không bị cảm.」"
"2577" = "「Hồi đó……\\nTôi cũng không hiểu được, nhưng mà.」"
"2967" = "Tròn xoe như quả bóng bay,\\ncứ như thể bụng đang to ra vậy——Ư!!?"
"3179" = "Mỗi lần bàn tay không ngừng nghỉ này khẽ vuốt ve trong lúc trò chuyện,\\ncon bé lại cười rạng rỡ, trông vừa nhột vừa hạnh phúc——"
"3330" = "Và rồi tôi, sẽ tạo ra một cơn gió.\\nĐể một ngày nào đó khi Hibiki vỗ cánh——Ư!"
```

Kiểm chứng: khối parse được bằng tomllib, 13 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\\n` viết `\\\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\\n` của VN cũ (không thêm `\\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build §5).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohitoyo" (3 dòng: 2560, 3223, 3285 — "quán cà phê ga Ohimitera" / "Ở Ohimitera") — theo tiền lệ các file trước, fix trong đợt thống nhất.
- **1909 khôi phục thẻ [Gegege,2]/[Ge]** — đây là fix duy nhất trong file khôi phục thẻ ruby (các thẻ ruby đọc tên khác đều bỏ theo thông lệ toàn dự án); nếu Hieu thấy "[Gegege,2]Tệ tệ tệ của [Ge]tệ đấy" nghe gượng trong game thì bỏ thẻ và giữ câu lặp cũ.
- **1928 "chú"** — Soutetsu tự xưng "chú" khi xin lỗi; người nghe không xác định chắc chắn từ key kề (có thể là khách nhí, cũng có thể là người lớn). Nếu trong game người nghe là Nagayama thì nên đổi thành "tôi".
- **2038 "——A"** — tiếng gasp っ trước あ chưa được diễn; "——ƯA" nghe gượng nên giữ nguyên, Hieu quyết có cần thêm không.
- **1509 "Phùù."** — theo công thức độ dài nguyên âm (1 う → 2 nguyên âm), đã có tiền lệ sửa ふぅ → "Phùù"; nếu Hieu thấy "Phùù" lạ thì đổi về "Phù.".
- 4 strong candidates của queue chỉ là heuristic; lần đọc toàn bộ tìm ra 13 dòng sai (2,3%) — file sạch, lỗi rải rác không theo hệ thống.

## Kết bài

File 日々姫05_御一夜ステーションカフェ: 577 dòng đã đọc hết, **13 dòng sai (2,3%)** — 4 xưng hô (1518, 2212, 2407, 2577), 4 gasp (2040, 2069, 2967, 3330 — cả 4 từ sweep), 4 SFX (1509, 1909, 2081, 2364), 1 sai nghĩa (3179 "buồn buồn buồn buồn" → "nhột"). Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. CSV3 1 set duy nhất, VN khớp TOML tuyệt đối sau chuẩn hóa `\\n` (326 lệch chỉ là làm phẳng `\\n`, 0 khác biệt thực chất). JSON 13 khóa chuỗi; khối TOML parse OK, 13 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 13/13; lượt soát 2: 13/13, 0 bỏ, 0 sửa.
