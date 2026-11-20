# Audit — 日々姫10_稀咲の未来図、日々姫の未来図 (02_Hibiki) — "Bản đồ tương lai của Kisaki, bản đồ tương lai của Hibiki"

- File: `日々姫10_稀咲の未来図、日々姫の未来図.txt.toml` — route 02_Hibiki, **489 dòng script**, 3 strong candidates (queue).
- Nội dung: buổi phỏng vấn của phóng viên Ichikawa (Kumamoto Shimpo) với Kisaki tại chi nhánh ngân hàng; màn trình diễn sa bàn N-gauge (KiHa 07 + 8620); Hibiki vật lộn vẽ "bản đồ tương lai" của Ohitoyo, bị Kisaki sao chép toàn bộ kế hoạch phục hồi toa xe; Hibiki quỳ rạp xin lỗi cả nhóm; Soutetsu thuyết phục phe Paulette cũ và chốt phương án "mời mọi người cùng vẽ".
- Phương pháp: đọc hết 489/489 dòng theo JP + TW (CSV3, 1 set duy nhất — không trùng khóa, 0 ô VN/JP/TW trống), đối chiếu TOML-2. Không lấy mẫu. Key không theo thứ tự truyện (phỏng vấn / trình diễn mô hình / độc thoại xen kẽ theo key) — xác định người nói/người nghe theo nội dung và dòng kề.

## §1. Kết quả

**16 dòng sai / 489 (3,3%)** — file khá sạch; lỗi rải rác, không có cụm hệ thống. Không có dòng lệch vị trí nào — bản dịch gốc ở file này nhìn chung giữ đúng hàng.

- Lệch vị trí (misaligned) **0**, chuỗi xoay (rotation) **0**, nhiễm chéo file khác **0**, dòng mồ côi (orphan) **0**, chưa dịch **0**, trùng khóa **0**.
- Phân loại (16): gasp 2 (2940, 3390 — cả 2 từ sweep, đều nhận), đại từ 3 (2691, 2847, 2925), sai nghĩa 4 (2647, 2888, 3620, 3666), phong cách 3 (2581, 2602, 2920 — です đứng một mình thành "Ạ."), bịa thêm nghĩa 1 (2437), bỏ sót danh từ 1 (2720), thẻ %l 1 (2781), phiên âm 1 (2943).
- `[selections]` rỗng (0 mục). Thẻ `%l`: số lượng JP == VN ở mọi dòng; chỉ 1 thẻ sai định dạng (2781, đã sửa).
- Không có bản sao file này (md5 `45ecfdf18d22d323e120874ecafc3a6c`, duy nhất trong toàn bộ TOML-2; 1 copy, không áp fix 2 nơi).

## §2. Chi tiết từng dòng sai

### Gasp — mất tiếng thở/っ (2 dòng, cả 2 từ sweep)

- **2940** (双鉄). JP: 「っ！」; TW: 「！」. Sweep `lost-gasp-whole` liệt kê đúng, fix nhận nguyên: VN cũ: 「!」 → **「Ư!」**.
- **3390** (monologue). JP: 「その姿勢のまま――\nなにか手段がないかどうかを考え、探し求め――っ！！？」; TW: 「……啊！！？」 (có tiếng "a"). Sweep `lost-gasp-trailing` liệt kê đúng. VN cũ: 「Vẫn giữ nguyên tư thế đó——\nTôi cố gắng suy nghĩ, tìm kiếm xem có cách nào không——!!?」 → **「……không——Ư!!?」** (fix dựng từ VN cũ của CSV3; old_vn của sweep khác VN hiện tại chỉ ở cách viết `\n`).

### Đại từ — xưng hô (3 dòng)

- **2691** (双鉄). JP: 「ポーレット、すまんが、電話を借りてもいいか？」 — Soutetsu gọi thẳng tên Paulette, người nghe rõ ràng là Paulette. Theo quy tắc đã sửa (Soutetsu là "anh" với Paulette), VN cũ "tôi" sai: 「Paulette, xin lỗi nhé, **tôi** mượn điện thoại được không?」 → **「Paulette, xin lỗi nhé, anh mượn điện thoại được không?」**.
- **2847** (ふかみ). JP: 「そんなこともちろんわかってるよ？　けど……\nあれ、凪ちゃんは綺麗って思わなかった？」 — Fukami hỏi Nagi. Theo quy tắc đã sửa (Fukami–Nagi cùng tuổi, "bạn bè"; Fukami tự xưng "mình", không "chị"): VN cũ 「Chuyện đó tất nhiên là **chị** biết rồi?」 → **「Chuyện đó tất nhiên là mình biết rồi?」**.
- **2925** (ハチロク). JP: 「まだ家を出てないのでしょうか？\n電話をしてみてはいかがですか？」 — Hachiroku nói với Soutetsu. Cô gọi anh là 双鉄様 → "ngài Soutetsu" (ngay dòng 2922 trong file này: 「Ngài Soutetsu?」), nên VN cũ "Anh thử gọi điện xem sao?" mâu thuẫn: → **「Ngài thử gọi điện xem sao?」**.

### Sai nghĩa (4 dòng)

- **2647** (双鉄). JP: 「そう……だな」 — Soutetsu đồng tình ("Ừ… đúng vậy"); TW: 「是啊……」. VN cũ 「Chắc…… vậy thôi.」 biến câu đồng tình thành phỏng đoán ("chắc"): → **「Ừ…… đúng vậy.」**.
- **2888** (双鉄). JP: 「ならば、そのやり方を試してみよう。\nれいな、いいか」 — 「いいか」 = "được chứ / nghe rõ chứ", không phải "lại đây". VN cũ 「Vậy thì, thử cách đó xem sao.\nReina, **lại đây nào.**」 → **「Reina, được chứ?」** (TW cũng dịch lệch thành "過來一下" — JP thắng TW).
- **3620** (monologue). JP: 「破顔一笑。」 — "nở nụ cười rạng rỡ" (cười bằng mặt, không phải cười thành tiếng); TW: 「破顏一笑」 xác nhận. VN cũ 「Chị Mayami **phá lên cười.**」 → **「Chị Mayami nhoẻn miệng cười.」**.
- **3666** (monologue). JP: 「もはや様付けを放棄して、\nしかしハチロクは、稀咲のことを称賛する。」 — 「様付け」 = cách gọi kèm -sama (Hachiroku thôi gọi Kisaki là "Kisaki-sama"); TW: 「連“小姐”都不叫了」 xác nhận. VN cũ 「Hachiroku thậm chí đã từ bỏ việc dùng kính ngữ **"cô"**,」 diễn sai (chữ "cô" không phải là hậu tố kính ngữ): → **「Hachiroku thậm chí đã thôi gọi Kisaki bằng kính ngữ,」**.

### Phong cách — です đứng một mình thành "Ạ." (3 dòng)

Dịch giả tách câu lịch sự です cuối dòng thành một câu "Ạ."/"Ạ!" riêng — không phải câu tiếng Việt. Cả 3 dòng đều gộp "ạ" vào câu trước:

- **2581** (ふかみ). JP: 「わたしももちろん。ええと……究極賛成。です」. VN cũ: 「Em cũng vậy. Ừm……tán thành tuyệt đối. **Ạ.**」 → **「Em cũng vậy. Ừm…… tán thành tuyệt đối ạ.」**
- **2602** (ふかみ). JP: 「あ、お手伝いします。です！」. VN cũ: 「A, em sẽ phụ một tay. **Ạ!**」 → **「A, em sẽ phụ một tay ạ!」**
- **2920** (ふかみ). JP: 「この都市モデルも綺麗。です。けど！\n御一夜の自然とクマ川の水の方が、もっと綺麗。です！」. VN cũ: 「Mô hình đô thị này cũng đẹp. **Thật ạ.** Nhưng!\nThiên nhiên Ohimitera và nước sông Kuma còn đẹp hơn nhiều. **Lắm ạ!**」 → **「Mô hình đô thị này cũng đẹp thật ạ. Nhưng!\nThiên nhiên Ohimitera và nước sông Kuma còn đẹp hơn nhiều ạ!」** (giữ nguyên "Ohimitera" — chờ đợt thống nhất, xem §3).

### Bịa thêm nghĩa — fabrication (1 dòng)

- **2437** (記者Ａ). JP: 「いやいや、どうもどうも」 ("không, không, cảm ơn nhiều"); TW: 「啊，客氣了客氣了」 xác nhận. VN cũ thêm "Chắc chắn rồi" không có căn cứ JP/TW: 「**Chắc chắn rồi**, cảm ơn cô rất nhiều.」 → **「Không, không, cảm ơn cô rất nhiều.」**.

### Bỏ sót danh từ — omission (1 dòng)

- **2720** (ポーレット). JP: 「あのね？　こっちがブレーキハンドルで、\nこっちが[マスコンハンドル,5]集合運転装置」 — Paulette chỉ hai bộ phận: cần phanh và **thiết bị lái tích hợp** (集合運転装置); TW: 「這裡是整合駕駛裝置，上面有中控把手」 xác nhận. VN cũ chỉ dịch [マスコンハンドル,5] mà bỏ mất danh từ chính: 「Này nhé? Đây là cần phanh,\ncòn đây là **bộ điều khiển trung tâm.**」 → **「còn đây là thiết bị lái tích hợp.」**.

### Thẻ %l sai định dạng (1 dòng)

- **2781** (真闇). JP: 「…ポーちゃんの\x%lまいてつ;#00ffc040;まいてつ%l;\n#;人脈だけが頼りやけんね。…」 — dấu ngắt dòng `\n` nằm **bên trong** thẻ %l (giữa `%l;` và `#;`), khiến thẻ không đóng trên cùng một dòng hiển thị. VN cũ giữ nguyên lỗi này. Fix chỉ dời dấu ngắt dòng ra sau `#;` (vị trí ngắt hiển thị không đổi): 「…mạng lưới quan hệ \x%lまいてつ;#00ffc040;chủ tàu%l;\n#; của Pau-chan thôi…」 → **「…chủ tàu%l;#;\n của Pau-chan thôi…」** (giữ đúng số backslash của CSV3 cho dòng này).

### Phiên âm (1 dòng)

- **2943** (双鉄). JP: 「えぬのれいあうと？」 — えぬ là cách đọc chữ cái "N"; TW: 「Ｎ場景模型？」. VN cũ phiên âm kana thành tên riêng: 「Sa bàn **En-nu?**」 → **「Sa bàn N?」**.

## §3. Thuật ngữ dạng cũ — chờ đợt thống nhất, KHÔNG tính sai

- **"Ohimitera"** 24 dòng (2258, 2385, 2519, 2523, 2585, 2592, 2613, 2623, 2641, 2695, 2703, 2704, 2753, 2770, 2852, 2854, 2856, 2920, 2938, 3112, 3135, 3287, 3496, 3774) — dạng cũ của "Ohitoyo", sửa trong đợt thống nhất.
- **"Đường sắt Hoàng gia"** 1 dòng (2495) — dạng cũ của "Teitetsu" (帝鉄), chờ thống nhất.
- **"tuyến Yui"** 1 dòng (2613) — dạng cũ của "tuyến Yunoi" (湯医線), chờ thống nhất.
- **"Circuithium"** 1 dòng (2458) — キルクイティウム; đang chờ chốt "Quirquitium variants" trong đợt thống nhất, không tự đổi.

## §4. Sweep っ-gasp — kiểm tra trực tiếp

- Sweep có **2 mục** cho file này (2940 `lost-gasp-whole`, 3390 `lost-gasp-trailing`) — cả 2 đều đúng, đã nhận vào fix (xem §2).
- Quét toàn bộ っ trong file: các っ còn lại đều là nhấn mạnh trong từ (〜っ！, 〜けんっ, 〜ばいっ), SFX đã diễn (2451 「Ưm——khụ khụ」, 2453, 2411 「Ư ư!」), hoặc đã có âm tương đương (2403 「Hả!?」, 2432 「A!」) — **không có gasp nào sweep bỏ sót**. VN không còn っ thô (0 dòng chứa っ/ッ).
- 2 dòng 「Vâng.」 trùng nhau ở 2395/2461 (JP khác nhau: 「はぁ」 vs 「ええ」) — cùng là lời đáp "vâng" hợp lệ, không phải lệch dòng.

## §5. Kiểm chứng

- CSV3: 489 dòng cho file này, 1 set duy nhất, 0 trùng khóa (File,Section,Key), 0 ô VN/JP/TW trống. Không có set stale (khác 10 file dual-set đã biết).
- TOML-2: 489 khóa `[script]`, md5 `45ecfdf18d22d323e120874ecafc3a6c`, không có file trùng nội dung trong toàn bộ TOML-2 (1 copy duy nhất). `[selections]` rỗng.
- TOML vs CSV: **317/489 dòng khác nhau CHỈ ở chỗ TOML-2 dẹp literal `\n` thành khoảng trắng** (vd. 76, 2720) — CSV3 giữ literal `\n` là chuẩn, lấy CSV3 làm căn cứ fix (đúng quy tắc đã chốt). 3 dòng khớp tuyệt đối (2404, 2464, 2633). Đây là khác biệt định dạng, không phải lỗi dịch.
- JSON: 16 khóa (chuỗi); jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (log build).
- Khối TOML: parse được bằng tomllib, 16 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` literal viết `\\n` nên parse ra đúng dạng của CSV3). Mọi fix đều giữ nguyên quy ước ngắt dòng của từng dòng trong CSV3 (có dòng dùng `\n` đơn, có dòng dùng `\\n` kép — không chuẩn hóa).
- Lượt soát 2: **16/16 tái kiểm chứng, 0 bỏ, 0 sửa** — đọc lại toàn bộ 16 fix đối chiếu JP. (Lúc build, khâu kiểm tra diff cơ học bắt được 1 lỗi lắp ráp ở 2781 — dấu `;` thừa do cắt chuỗi sai vị trí — đã sửa trước khi viết review; nội dung fix không đổi.)
- Không có CJK ngoài thẻ %l (sau khi lột thẻ đúng cách; điểm duy nhất bắt được chính là thẻ rách 2781). Số lượng `%l` JP == VN ở mọi dòng.

## §6. Khối TOML (đã kiểm chứng parse)

```toml
[script]
"2437" = "「Không, không, cảm ơn cô rất nhiều.」"
"2581" = "「Em cũng vậy. Ừm…… tán thành tuyệt đối ạ.」"
"2602" = "「A, em sẽ phụ một tay ạ!」"
"2647" = "「Ừ…… đúng vậy.」"
"2691" = "「Paulette, xin lỗi nhé, anh mượn điện thoại được không?」"
"2720" = "「Này nhé? Đây là cần phanh,\\\\ncòn đây là thiết bị lái tích hợp.」"
"2781" = "「Để việc phục hồi \\\\x%l客車;#00ffc040;toa hành khách%l;#; đi vào quỹ đạo, chỉ có thể trông cậy vào mạng lưới quan hệ \\\\x%lまいてつ;#00ffc040;chủ tàu%l;#;\\\\n của Pau-chan thôi. Trăm sự nhờ em đấy.」"
"2847" = "「Chuyện đó tất nhiên là mình biết rồi? Nhưng mà……\\nNày, Nagi-chan không thấy nó đẹp sao?」"
"2888" = "「Vậy thì, thử cách đó xem sao.\\\\nReina, được chứ?」"
"2920" = "「Mô hình đô thị này cũng đẹp thật ạ. Nhưng!\\\\nThiên nhiên Ohimitera và nước sông Kuma còn đẹp hơn nhiều ạ!」"
"2925" = "「Chưa ra khỏi nhà sao ạ?\\nNgài thử gọi điện xem sao?」"
"2940" = "「Ư!」"
"2943" = "「Sa bàn N?」"
"3390" = "Vẫn giữ nguyên tư thế đó——\\\\nTôi cố gắng suy nghĩ, tìm kiếm xem có cách nào không——Ư!!?"
"3620" = "Chị Mayami nhoẻn miệng cười."
"3666" = "Hachiroku thậm chí đã thôi gọi Kisaki bằng kính ngữ,\\nnhưng vẫn dành lời khen ngợi cho Kisaki."
```

Kiểm chứng: khối parse được bằng tomllib, 16 khóa, 0 sai lệch giá trị so với JSON. Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- **2464 (凪) — KHÔNG sửa, chờ Hieu quyết.** JP chỉ có 1 dòng 「うんっ！」 nhưng TW và VN đều có 2 dòng 「Vâng!」×2. Có thể là lỗi nhân đôi của dịch giả (JP thắng TW → chỉ giữ 1 dòng), nhưng cũng có thể trong game câu này thực sự lặp 2 lần (2 đoạn giọng nói) mà cột JP đã gộp. Để nguyên 2 dòng, chờ Hieu kiểm tra trong game hoặc quyết theo JP.
- **2595 + 2715 (日々姫) — KHÔNG sửa, chờ Hieu quyết.** Hibiki tự xưng "chị" ở 2 dòng này ("Họa cụ của chị——…", "chị sẽ đơn giản hóa nó…") trong cảnh đông người (cả Soutetsu lẫn Nagi/Reina đều có mặt). Nếu nói với Soutetsu thì phải là "em", nếu nói với Nagi/Reina thì "chị" đúng. Người nghe không xác định được từ dòng kề nên giữ nguyên, chờ Hieu.
- **2624 (日々姫) — giữ nguyên, ghi chú biên.** VN thêm "mọi người" ("Em, em phải, phải xin lỗi mọi người!") trong khi JP 「謝らなくっちゃいけんけんっ！」 không có tân ngữ. Ngữ cảnh (Hibiki xin lỗi cả nhóm) ủng hộ cách thêm này nên không sửa; nếu Hieu muốn sát JP hơn thì bỏ "mọi người".
- Thuật ngữ dạng cũ chờ đợt thống nhất (§3): "Ohimitera" 24 dòng, "Đường sắt Hoàng gia" 1, "tuyến Yui" 1, "Circuithium" 1.
- 3 strong candidates của queue chỉ là heuristic; lần đọc toàn bộ tìm ra 16 dòng sai (3,3%) — file sạch hơn mặt bằng chung (4.799/100 file ≈ 48 dòng/file), lỗi tập trung ở đại từ/xưng hô và các lỗi nhỏ lẻ.

## Kết bài

File 日々姫10_稀咲の未来図、日々姫の未来図: 489 dòng đã đọc hết, **16 dòng sai (3,3%)** — 2 gasp (cả 2 từ sweep), 3 đại từ (Soutetsu "tôi"→"anh" với Paulette; Fukami "chị"→"mình" với Nagi; Hachiroku "Anh"→"Ngài" với Soutetsu), 4 sai nghĩa, 3 lỗi "Ạ." đứng một mình, 1 bịa thêm nghĩa, 1 bỏ sót danh từ, 1 thẻ %l rách, 1 phiên âm. Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. CSV3 1 set duy nhất; TOML-2 dẹp `\n` thành khoảng trắng ở 317 dòng (chỉ là khác biệt định dạng, CSV3 làm chuẩn). JSON 16 khóa chuỗi; khối TOML parse OK, 16 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 16/16; lượt soát 2: 16/16, 0 bỏ, 0 sửa.
