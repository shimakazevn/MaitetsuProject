# Audit — 日々姫06_日々姫の決断.txt.toml — 8/462 (1,7%)

- File: `日々姫06_日々姫の決断.txt.toml` — route 02_Hibiki, 462 dòng script.
- Nội dung: Paulette kể về lời đề nghị tài trợ của Ngân hàng Kumamoto (20 năm, 10 triệu yên/năm) kèm điều kiện Thị trưởng từ chức; Hibiki nhận ra chính mình đã vô tình gợi ý cho Kisaki; cả nhóm bàn chiến lược bầu cử (người–tiền–gió); Paulette quyết định từ chức để mở bầu cử, Hibiki quyết định tự ra ứng cử thay vì để Soutetsu làm ứng cử viên kế nhiệm; đêm cuối, Hibiki hôn Soutetsu để lấy dũng khí.
- Nhân vật: monologue 205, 双鉄 83, 日々姫 53, ポーレット 51, ハチロク 34, 真闇 20, れいな 16.
- Cơ sở tổng: 138 file / 6.285 dòng sai (đã tự kiểm chứng lại ROUTE-AUDIT.md — khớp với cơ sở được giao, không cần rebase).

## Kiểm tra cấu trúc

- TOML md5 `84d952a011337e111855c573aae8d311`, BOM + CRLF, 462 dòng script, `[selections]` rỗng. Không có bản sao trùng của file này (md5 duy nhất trong sources/toml2).
- CSV3: 1 set duy nhất (`translation_toml\02_Hibiki`), 462 hàng, 0 trùng khóa, 0 VN trống, 0 TW trống. VN khớp phẳng TOML 462/462. Comment `# JP:` trong TOML khớp CSV3 tuyệt đối 462/462.
- Thẻ `%l`: số lượng thẻ JP = VN trên mọi dòng; không có thẻ VN tự thêm, không có thẻ hỏng, không có thẻ thiếu dấu `;`. Các thẻ giữ nguyên: レイルロオド→Railord (3685, 2042), エアクラ→Aircra (2556, 2643, 2411), 列車→tàu (2398), 8620 (2598), 機関士→người lái tàu/nữ lái tàu (3259, 3394 — xem mục ghi chú).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
  - Nhiễm chéo: đối chiếu VN toàn dự án — 5 va chạm chéo file, tất cả đều là câu ngắn chung chung có JP tương đương (「Ngài Soutetsu.」= 双鉄様; 「Đúng vậy nhỉ, Reina.」= 本当ね、れいな; 「Thì ra là vậy ạ.」= そうだったんですか; 「Cuối cùng, tôi cũng đã hiểu.」= ようやく、僕は理解する) — 0 câu thoại đầy đủ nào bị đặt nhầm file.
  - VN trùng trong file: 3 nhóm, đều là cảm thán ngắn lặp hợp lệ (「…………」2061/2062, 「Hửm?」2501/2534, 「À.」2506/2527).

## Phân loại (8)

- Gasp 2, sai nghĩa 6. Thoại 5/257 (1,9%), độc thoại 3/205 (1,5%).
- Theo nhân vật: 日々姫 4, monologue 3, ポーレット 1.

### §1. Gasp (2 — cả 2 đều là mục sweep, đã kiểm chứng và áp nguyên văn)

Sweep có đúng 2 mục cho file này (`sweep-raw-gasp-wrong.json`); cả 2 đều khớp JP/TW/old_vn với CSV3 tuyệt đối.

- **2942** (日々姫, raw-tsu): JP 「っ！」. Old: 「っ!」 → Fix: 「Ư!」.
- **2489** (ポーレット, raw-tsu): JP 「えっ！？」\n「日々姫？　――っ！！」. Old: 「Ể!?」\n「Hibiki? ——っ!!」 → Fix: 「Ể!?」\n「Hibiki? ——Ư!!」. (Dòng 1 「えっ」→「Ể」 giữ nguyên theo tiền lệ — っ đã được diễn bằng thanh hỏi.)

Quét bổ sung toàn bộ các dòng JP có っ trong file — 0 gasp sót: 2481 ぅわっ (giữa dòng, không phải cuối tuyệt đối), 2479 だってっ / 2518 何故ですかっ / 2623 したらっ / 2675 わたっ・けんっ・おやっ・にぃにっ (っ nhấn mạnh gắn từ nội dung — giữ theo quy tắc đã khóa), 2509 あっ → "A!" (tiền lệ sweep), 2483 はうっ → "Hả!!?" (âm ngắt đã có trong "Hả"), 3749 （ちゅっ！）→"（Chụt!）" (đã diễn), các っ trong từ ở độc thoại (ホっと, くっつける, びっくり…) không phải gasp.

### §2. Đại từ (0 — 1 mục đã bị parent loại khi kiểm chứng gộp)

Quy tắc đã sửa 20/11: Soutetsu "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi, "tôi" với Hachiroku/Mayami/Minokasa/Kisaki; Paulette 双鉄くん → "anh Soutetsu" (khóa B4).

- **2764 — LOẠI (parent, 21/11, tiền lệ file 09 key 2123):** agent đề xuất Soutetsu "anh"→"tôi" với Hachiroku, viện chứng "Soutetsu gọi thẳng tên Hachiroku ở 233 (「ならば、ハチロク」) và Hachiroku đáp ngay ở 237" — nhưng key 233/237 KHÔNG tồn tại trong file này (parent đã kiểm CSV3); câu 「ならば、ハチロク」 cũng không có trong file, câu gần nhất là 2727 「そうだな。ハチロク」 (một trao đổi khác, cách 2764 tới 37 key). Dòng kề thực tế của 2764: 2760 Hibiki gọi Soutetsu "にぃにぃ… 兄さんじゃ、今回の選挙には、勝てない", 2764 Soutetsu đáp, 2766 Soutetsu trấn an Hibiki, 2767 Hibiki đáp "Đúng vậy, anh trai" — người nghe chính là Hibiki → "anh" ĐÚNG theo quy tắc đã sửa, giữ nguyên old VN, không tính sai. Đã gỡ khỏi JSON + khối TOML + tổng số (9 → 8).

### §3. Sai nghĩa (6)

- **2923** (日々姫): JP 「ねぇねぇに――」. Old: 「Anh hai——」 → Fix: 「Chị——」. Đây là lỗi nhầm chị thành anh: ねぇねぇ = chị gái, khác hẳn にぃにぃ (anh hai) mà Hibiki dùng cho Soutetsu; TW 「阿姐……」 xác nhận là chị. Người chị cụ thể (Paulette, khả năng cao nhất) không gọi tên trong JP nên bản sửa giữ dạng trần "Chị——" như JP.
- **2374** (双鉄): JP 「事態は、既に動いていたのだ。」. Old: 「Mọi chuyện vốn đã được định sẵn rồi.」 → Fix: 「Mọi chuyện vốn đã bắt đầu diễn ra từ trước rồi.」. 動いていた = đã bắt đầu chuyển động/diễn ra, không phải "đã được định sẵn" (định mệnh/quyết định trước); TW 「事態早已開始發展了」 xác nhận.
- **3675** (monologue): JP 「ティーカップを前に、ポーレットも日々姫も、厳しい顔で黙りこんでいる。」. Old: 「Đứng trước tách trà,\ncả Paulette và Hibiki đều im lặng với vẻ mặt nghiêm trọng.」 → Fix: 「Trước tách trà,\ncả Paulette và Hibiki đều im lặng với vẻ mặt nghiêm trọng.」. を前に = "trước mặt", không có "đứng" — cả hai đang ngồi uống trà; VN tự thêm tư thế đứng.
- **3567** (monologue): JP 「れいなの話が、呼び水となってくれたのだろう。」. Old: 「Lời kể của Reina có lẽ đã trở thành mồi nhử.」 → Fix: 「Lời kể của Reina có lẽ đã trở thành lời gợi mở.」. 呼び水 = nước mồi/khơi gợi (TW 拋磚引玉 = lời mở đầu dẫn dắt), không mang hàm ý lừa gạt như "mồi nhử".
- **2493** (日々姫): JP 「無理矢理にでも、風を吹かせる。」. Old: 「Dù có phải dùng vũ lực cũng phải tạo ra gió.」 → Fix: 「Dù có phải cưỡng ép cũng phải tạo ra gió.」. 無理矢理 = cưỡng ép/miễn cưỡng; "vũ lực" thêm hàm ý bạo lực thể xác không có trong JP; TW 「哪怕來硬的」 xác nhận nghĩa "dù phải làm căng".
- **2658** (日々姫): JP 「兄さんの手だってひける――大人の女に」. Old: 「Và đôi khi, còn có thể nắm lấy tay anh trai——một người phụ nữ trưởng thành.」 → Fix: 「Và đôi khi, còn có thể dắt tay anh trai bước đi——một người phụ nữ trưởng thành.」. ひける (引ける) = kéo/dắt đi; TW 「牽著哥哥向前走」 (dắt anh trai bước về phía trước) xác nhận sắc thái dẫn dắt mà "nắm lấy tay" làm mất.

## Đã kiểm tra và không tính sai

- **Đại từ:** Paulette 双鉄くん → "anh Soutetsu" đúng mọi chỗ (2514, 2931, 2872, 2524…); Soutetsu gọi Hibiki "em"/tự xưng "anh" đúng mọi chỗ; Soutetsu gọi Hachiroku "em" (2613) đúng; Hachiroku 双鉄様 → "Ngài Soutetsu" đúng; Mayami 双ちゃん → "Sou-chan", ポーちゃん → "Pou-chan", ひーちゃん → "Hii-chan", ウチ → "chị" nhất quán; Hibiki にぃにぃ → "anh hai" đúng mọi chỗ; Hibiki tự xưng "em" đúng; Reina gọi Paulette/Hibiki "chị" đúng; độc thoại Soutetsu dùng "tôi", chỉ 3752 dùng "mình" (（馬鹿か、僕は）→"（Mình bị ngốc à）" — tự vấn cảm xúc, đúng ngoại lệ đã chốt); 3117 "mình" trong mệnh đề "tôi tự hỏi tại sao nãy giờ mình lại…" cũng là tự vấn, giữ nguyên; 2029 "Mình lại ép chị ấy…" là lời nghĩ trích dẫn của Hibiki, giữ nguyên. "Anh" ở 2664 giữ nguyên (kể giả định trước nhóm hỗn hợp, Paulette là người nghe chính).
- **義:** 3676 義理でも兄 → "anh trai nuôi" (TW 義兄 — theo tiền lệ file 14, giữ); 3406 僕の義妹 → "cô em gái nuôi của tôi" (TW 義妹, giữ); 3628 義妹 → "em gái nuôi của tôi" (TW 義妹, giữ).
- **Hoàn thiện câu JP cụt theo TW:** 3748 (TW bổ sung "có đầy" → VN "cũng có đầy", giữ); 2929/2087 Hibiki/Hachiroku nói mớ (TW cùng hoàn thiện 双鉄様/"下定決心", giữ); 2767 (TW 「我一定會找到屬於自己的答案」, giữ).
- **SFX/âm thanh:** 2486 ふぇ？ → "Hể?" (thán từ hỏi, không phải rên — giữ, không áp quy tắc ふぇ→"phuê" vốn dành cho tiếng thở/rên); 2482 ひゃうう → "Hyaa." (tiếng giật mình của Reina, tự phát theo quy tắc ひあ/ひゃ — giữ); 2886 "“ばん”ばっかり" — cả 3 từ đều vần "bàn/bản" trong JP (地盤/看板/鞄), VN chỉ giữ được 2/3 (địa bàn/bảng hiệu, 鞄→"cặp táp" không có vần) — giới hạn dịch không sửa được mà không bóp nghĩa, giữ nguyên và ghi chú; 2035/2038 không có trong file này. Quy tắc romaji fallback cho tiếng rên (duyệt 21/11 ~01:56) không áp dụng cho file này — không có dòng rên fa/fu hay ひあ/ひゃ nào cần chuyển romaji.
- **Thuật ngữ đã đúng:** 宮司 → "Đền chủ" (2914); エアクラ → "Aircra" (3 dòng, thẻ %l nguyên vẹn); Railord (2 dòng); 市長/社長 → "Thị trưởng"/"Giám đốc" nhất quán; 弔い選挙 → "cuộc bầu cử tang tóc" nhất quán; 地盤/看板/鞄 → "địa bàn/bảng hiệu/cặp táp" (giải thích ở 3264 đúng: tổ chức/nổi tiếng/tiền bạc); 2473 "５プラス５０日" → "5 cộng 50 ngày" (giữ nguyên văn JP, TW cũng ghi ５～５５天).

## Chờ đợt thống nhất (không sửa trong audit này)

- **御一夜 → "Ohimitera" (13 dòng, 15 chỗ):** 2926, 3506, 2749, 3326, 2416, 2673, 2582, 3628 (×3 trong 1 dòng), 2589, 2817, 2669, 2696, 3167 — đổi thành "Ohitoyo" theo thuật ngữ đã chốt. Trong đó 3326 là tên công ty 御一夜鉄道株式会社 ("Công ty Cổ phần Đường sắt Ohimitera") — cùng câu hỏi đang chờ Hieu như ハチロク14 2748 (có đổi tên công ty thành "Ohitoyo" không).
- **日ノ本 → "Hinamoto" (2 dòng):** 2709, 2628 — đổi thành "Hinomoto" (khớp đúng danh sách đợt thống nhất đã ghi "日々姫06 ×2").
- **頭取 (2897):** 「頭取の宝生さんとウチとが、互角」 → VN hiện "Giám đốc Houshou và chị cũng ngang ngửa nhau". Toàn dự án đang có 3 cách dịch cho 頭取 của cùng một người Mototada: "chủ tịch" (共通14, đã merge), "tổng giám đốc" (共通11, đã merge), "Giám đốc" (ở đây) — cần chốt 1 dạng trong đợt thống nhất, không tự quyết trong audit này. Ghi chú thêm: "Giám đốc" trùng với cách dịch 支店長 ("Giám đốc chi nhánh", 2416).
- **機関士 gloss (3259, 3394):** thẻ %l ghi "người lái tàu"/"nữ lái tàu" trong khi thuật ngữ đã chốt là "thợ lái đầu máy" (dạng ngắn "lái tàu" trong thoại) — để đợt thống nhất chuẩn hoá gloss.

## Kiểm chứng

- JSON 8 mục dạng chuẩn (list of dicts, khóa chuỗi — parent đã loại mục 2764 khi kiểm chứng gộp, xem §2); khối TOML `[script]` 8 khóa, parse OK, 0 sai lệch giá trị (so sánh chuỗi thô — `\\n` trong khối parse về đúng literal `\n` của CSV3).
- jp/tw/old_vn khớp CSV3 tuyệt đối 8/8 (lấy trực tiếp từ CSV3 khi dựng JSON).
- Diff-sanity: mỗi fix chỉ khác old VN ở đúng chỗ cần sửa, số dòng giữ nguyên 8/8; không có fix viết lại lớn.
- Lượt soát 2: 9/9 tái kiểm chứng, 0 bỏ, 0 sửa (agent); parent loại thêm 1 mục 2764 khi kiểm chứng gộp → còn 8.
- Không còn dòng nào không chắc cần chờ Hieu (trừ các mục đợt thống nhất đã liệt kê + B19 đã park toàn dự án).

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
2374 = "「Mọi chuyện vốn đã bắt đầu diễn ra từ trước rồi.\\nCho dù Hibiki có nói gì, hay có giữ im lặng thì cũng chẳng liên quan đâu.」"
2489 = "「Ể!?」\\n「Hibiki? ——Ư!!」"
2493 = "「Dù có phải cưỡng ép cũng phải tạo ra gió.\\nChị Kisaki đã chuẩn bị sẵn sàng——để có thể làm được điều đó rồi.」"
2658 = "「Em muốn trở thành một người có thể bước đi với cùng một sải bước như anh trai.\\nVà đôi khi, còn có thể dắt tay anh trai bước đi——một người phụ nữ trưởng thành.」"
2923 = "「Chị——」"
2942 = "「Ư!」"
3567 = "Lời kể của Reina có lẽ đã trở thành lời gợi mở.\\nGiọng nói điềm tĩnh của Paulette bắt đầu cất lên."
3675 = "Trước tách trà,\\ncả Paulette và Hibiki đều im lặng với vẻ mặt nghiêm trọng."
```

## Kết bài

File 日々姫06_日々姫の決断.txt.toml: 462 dòng đã đọc hết, **8 dòng sai (1,7%)** — gasp 2 (sweep, 2942 + 2489), sai nghĩa 6 (2923 nhầm ねぇねぇ "chị" thành "anh hai"; 2374 "đã được định sẵn"→"đã bắt đầu diễn ra"; 3675 thêm "đứng"; 3567 呼び水 "mồi nhử"→"lời gợi mở"; 2493 無理矢理 "vũ lực"→"cưỡng ép"; 2658 手だってひける "nắm lấy tay"→"dắt tay… bước đi"). Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Chờ đợt thống nhất: "Ohimitera" 13 dòng → "Ohitoyo", "Hinamoto" 2 dòng → "Hinomoto", 頭取 (2897) chốt 1 dạng, gloss 機関士. Lượt soát 2: 9/9, 0 bỏ, 0 sửa (agent); parent loại 2764 khi kiểm chứng gộp (bằng chứng người nghe không tồn tại trong file; người nghe thực tế là Hibiki) → còn 8. JSON + khối TOML đã kiểm chứng parse, 0 sai lệch.
