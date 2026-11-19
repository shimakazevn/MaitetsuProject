# Audit: Paulette 05_鳴呼の町 — 23 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/ポーレット05_鳴呼の町.txt.toml` — 458 dòng script, **23 dòng Việt sai = 5,0%**, 0 dòng chưa chắc chắn (cập nhật 19/11: 1992 đã chốt từ ngữ cảnh; 1726 đã rút khỏi danh sách sai — xem các mục dưới).
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 13 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8%, stove 22,1%, Paulette 05_whatsentertainment 2,8%.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 458/458 dòng script** (key 27 và 1240–2811, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 23 dòng sai: **lệch vị trí 11** (1245, 1264, 1969, 2187, 2375, 2518, 2558, 2568, 2697, 2699, 2784 — xem 3 chuỗi chuyển chỗ ở mục dưới), **sai nghĩa 4** (1700, 2010, 2136, 2177), **thuật ngữ 5** (1625, 2112, 2140, 2512, 2640 — "Ohimitera" theo quyết định mới phải đổi thành "Ohitoyo"), **xưng hô 2** (1660, 2593 — Soutetsu xưng "mình"). Chưa dịch 0, cụt câu 0, không chắc chắn 0 (1992 đã chốt sau khi Hieu yêu cầu trích ngữ cảnh — xem dưới; 1726 đã rút khỏi danh sách sai vì audit nhận định nhầm — xem dưới).
- Thoại sai 12/303 (4,0%); lời dẫn (monologue) sai 11/155 (7,1%). Theo người nói: monologue 11, Soutetsu 6, Paulette 3, Hikari 3; Reina, bà cụ, nhân viên cửa hàng 0.
- Phân bố lỗi theo đoạn: key 27–1726: 5 dòng; 1969–2187: 5 dòng; 2375–2593: 9 dòng; 2640–2784: 4 dòng — lỗi tập trung ở cảnh trượt chân xuống hố tuyết (key 1245–2784, xem chuỗi chuyển chỗ), phần còn lại rải rác.
- **Heuristic thoại/dẫn báo 5 dòng** (1264, 2187, 2518, 2558, 2699) — cả 5 đều là lỗi thật, nhưng chỉ bắt được **5/23 dòng sai (21,7%)**: 18 dòng còn lại là lệch cùng loại (thoại→thoại, dẫn→dẫn), sai nghĩa, xưng hô và thuật ngữ — những lỗi heuristic không thể thấy. Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** test shift −5..+5 tốt nhất ở shift 0 (453/458 = 0,989). Không có bằng chứng lệch đều; lỗi xác nhận bằng đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 458 dòng, 0 dòng khác nội dung thực (217 dòng chỉ khác `\n`/khoảng trắng). Không có dòng CSV trống nào trong file này. VN==TW: 0 dòng.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có dòng nào VN thêm/thiếu thẻ so với JP. (Lưu ý: thẻ `%l` ở 2413 nằm trong cột TW, không phải JP gốc — VN không có thẻ là đúng.) Dấu gạch —— trong bản sửa viết không khoảng trắng hai bên, theo quy ước dự án (22.055 dòng).

## Kết luận về cơ chế lỗi
- **Lệch vị trí nội bộ theo 3 chuỗi xoay vòng — không phải tràn chương.** Khác với 夜の嵐 (tràn từ Hachiroku 12) và stove (tràn từ hearing), file này không có dòng Việt nào copy từ file khác: toàn bộ 11 dòng lệch đều là bản dịch đúng của một key khác **trong cùng file**, xoay vòng thành 3 chuỗi (xem mục A). Cơ chế vẫn là dán nhầm cột Việt theo từng dòng rời rạc trong Sheets, nhưng lần này các dòng bị dán nhầm chỉ loanh quanh trong cùng một cảnh (cảnh trượt chân xuống hố tuyết) thay vì tràn từ chương khác.
- **9/11 bản sửa lệch vị trí khôi phục được từ trong file** (chỉ cần chuyển bản dịch đúng đang nằm ở key khác về đúng chỗ); 2 dòng phải dịch mới (1245, 2187 — bản dịch đúng của chúng không còn ở đâu trong dự án).
- **2 trùng lặp nội bộ:** "A!!" 1854/1969 (chỉ 1854 đúng) và "Đợi đã! Đừng động đậy, đừng lại gần đây!!" 2091/2558 (chỉ 2091 đúng) — cả hai đều nằm trong 11 dòng lệch trên, không tính thêm.
- Ngoài chuỗi lệch, lỗi còn lại chỉ ở mức câu/chữ: 5 sai nghĩa, 5 thuật ngữ theo quyết định mới, 2 xưng hô.
- 435 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 23 dòng sai

### A. Lệch vị trí — 3 chuỗi xoay vòng nội bộ (11 dòng)
Mỗi chuỗi dưới đây: bản Việt cũ ở key này là bản dịch đúng của key ghi sau mũi tên — đã xác minh bằng cách đối chiếu từng câu với JP + TW ở cả hai đầu (JP và TW khớp nhau ở mọi dòng). Chi tiết đầy đủ từng dòng (JP/TW/VN cũ/bản sửa) ở file JSON `audit-paulette05-narukonotown-wrong.json`.

**Chuỗi 1 — cảnh hố tuyết, 4 dòng (1264 → 2518 → 2375 → 2187):**
- **1264** (Soutetsu): JP 「……雪の下が空洞になっている部分があったのだな。そこを踏み抜き、右足がすっぽり落ちてしまった」 ("Dưới tuyết có chỗ rỗng, tôi dẫm phải, chân phải lọt thỏm xuống.") — VN cũ "Tiếp theo, dùng lời nói để xác nhận tình trạng hiện tại." (đó là bản dịch đúng của 2568, xem chuỗi 2). Bản sửa lấy từ 2518: "「……Có một khoảng trống dưới lớp tuyết nhỉ. Tôi đã dẫm phải chỗ đó, và chân phải bị lọt thỏm xuống.」"
- **2518** (monologue): JP 「雪の下。どれだけの範囲に空洞があるのかわからない。広ければ、残ってる左足ごと――全身が下に落ちかねない。」 — VN cũ là bản dịch đúng của 1264 (câu trên). Bản sửa lấy từ 2375: "Dưới lớp tuyết. Không biết khoảng trống đó rộng bao nhiêu. Nếu nó rộng, có thể cả chân trái còn lại——toàn thân tôi sẽ rơi xuống dưới mất."
- **2375** (monologue): JP 「しかし、山の下に地面があるかもわからない。深い溝にでもなっていたなら、冗談ではなく命の危機だ。」 — VN cũ là bản dịch đúng của 2518 (câu trên). Bản sửa lấy từ 2187: "Nhưng, cũng không biết dưới ngọn núi này có phải là mặt đất hay không. Nếu nó là một cái rãnh sâu, thì không phải chuyện đùa đâu, sẽ nguy hiểm đến tính mạng đấy."
- **2187** (Paulette): JP 「双鉄くん、足、抜ける？」 ("Anh Soutetsu, chân rút ra được không?") — VN cũ là bản dịch đúng của 2375 (câu trên). Bản dịch đúng của dòng này không còn ở đâu trong dự án — dịch mới: "「Anh Soutetsu, chân rút ra được không?」"

**Chuỗi 2 — ngăn ngừa tai nạn thứ cấp, 3 dòng (2558 → 2568 → 1264):**
- **2558** (monologue): JP 「状況が上手く把握できない。ならば最優先すべきは、二次災害の防止。」 — VN cũ "「Đợi đã! Đừng động đậy, đừng lại gần đây!!」" trùng y hệt 2091 (chỉ 2091 đúng). Bản sửa lấy từ 2568: "Tôi chưa nắm rõ được tình hình. Vậy thì ưu tiên hàng đầu là ngăn ngừa tai nạn thứ cấp."
- **2568** (monologue): JP 「次いで、言葉に直して現状確認。」 ("Tiếp theo, dùng lời nói để xác nhận tình trạng hiện tại.") — VN cũ là bản dịch đúng của 2558 (câu trên). Bản sửa lấy từ 1264: "Tiếp theo, dùng lời nói để xác nhận tình trạng hiện tại."
- **1264**: xem chuỗi 1 — VN cũ của 1264 chính là bản dịch đúng của 2568, khép kín chuỗi 2.

**Chuỗi 3 — lời nói làm bình tĩnh lại, 4 dòng (1969 → 2699 → 2697 → 2784 → 1245):**
- **1969** (Soutetsu): JP 「僕は大丈夫。痛みはない、おそらく、怪我もしていない」 ("Tôi không sao. Không thấy đau, có lẽ cũng không bị thương.") — VN cũ "A!!" trùng y hệt 1854 (chỉ 1854 đúng). Bản sửa lấy từ 2699: "「Tôi không sao. Không thấy đau, có lẽ cũng không bị thương.」"
- **2699** (monologue): JP 「言葉が気持ちを落ち着けて、せばまっていた視野が広がる。」 — VN cũ là bản dịch đúng của 1969 (câu trên). Bản sửa lấy từ 2697: "Lời nói giúp tôi bình tĩnh lại, và tầm nhìn đang bị thu hẹp dần mở rộng ra."
- **2697** (monologue): JP 「言えば、危険を理解する。」 ("Nói ra thì mới hiểu được sự nguy hiểm.") — VN cũ là bản dịch đúng của 2699 (câu trên). Bản sửa lấy từ 2784: "Nói ra thì mới hiểu được sự nguy hiểm."
- **2784** (monologue, ngoặc suy nghĩ): JP 「（１メートルほどの高さの山だ。例え落ちても、大けがをするようなことは無かろうが――）」 — VN cũ là bản dịch đúng của 2697 (câu trên). Bản sửa lấy từ 1245: "（Đây là một ngọn núi cao khoảng 1 mét. Cho dù có rơi xuống, chắc cũng không đến mức bị thương nặng——）"
- **1245** (monologue): JP 「……慎重にいきたいところだが、このままとどまっているのも怖い。」 ("Tôi muốn thật cẩn thận, nhưng cứ đứng yên ở đây thế này cũng đáng sợ.") — VN cũ là bản dịch đúng của 2784 (câu trên). Bản dịch đúng của dòng này không còn ở đâu trong dự án (đã tìm trong chỉ mục Việt toàn dự án: không dòng nào chứa "cẩn thận" + "sợ" khớp nghĩa này) — dịch mới: "……Tôi muốn thật cẩn thận, nhưng cứ đứng yên ở đây thế này cũng đáng sợ."

### B. Sai nghĩa (5 dòng)
- **1700** (Hikari): JP 「あのね、ひかりね。きゅっきゅってなるこがいいのー」 — VN cũ "Mẹ ơi, Hikari nhé. Muốn làm cái kêu cót két cơ~" thêm "Mẹ ơi" không có trong JP (あのね chỉ là "này nhé") — mà lúc này Hikari đang nói với papa (Soutetsu, xem 1693 "Hikari, là cô giáo của papa"), không phải với mẹ: sai cả người nghe. Sửa thành "「Này nhé~! Hikari muốn làm cái kêu cót két cơ~」".
- **1726** (Hikari): ~~ĐÃ RÚT KHỎI DANH SÁCH SAI (audit nhận định nhầm, sửa ngày 19/11 theo góp ý của Hieu)~~ — JP gốc thực sự viết **かまくま**, không phải かまくら: 「ふゆのたのしみー！　ゆきだるま！　ゆきがっせん！　かまくま！」. Đây là Hikari nói ngọng có chủ đích (chơi chữ かまくら + くま gấu), không phải lỗi gõ: Soutetsu đã sửa cô bé ở 1633 (「かまくまではなく、かまくらだ」 — "Không phải gấu tuyết, mà là lều tuyết"), và tới 1945 cô bé tự nói đúng (「そうだったのー！　かまくらー」 — "Thì ra là vậy~! Lều tuyết~"). Bản Việt hiện tại "Gấu tuyết!" là **ĐÚNG** — giữ nguyên nhịp thoại đùa. Bản sửa cũ ("Lều tuyết!") đã bị gỡ khỏi khối TOML. Bài học: khi JP và TW mâu thuẫn nhau, tin JP; bản TW bắc cầu (住雪洞) đã xóa mất trò đùa chữ.
- **2010** (Soutetsu): JP 「水切り、な。ポーレット。空いているかごの鎖の端を、ひかりに持たせてやってくれるか？」 / TW 「是瀝水籃。」 — 水切り (rổ để ráo nước) bị dịch thành "Vớt nước". Sửa thành "Rổ ráo nước, nhé."
- **2136** (Soutetsu): JP 「ひもではなく鎖。鎖が、水切りかごに結びつけられ、水切りかごは、温泉の湯の中に沈んでいる」 / TW 「鐵鏈上掛著瀝水籃」 — 水切りかご = rổ để ráo nước (TW: 瀝水籃), không phải "rổ vớt nước" (2 lần trong dòng). Sửa cả hai chỗ thành "rổ ráo nước".
- **2177** (Hikari): JP 「くさりと、みずきいかごーと、おんせんのゆー」 / TW 「鐵鏈掛著瀝水籃，放進溫泉」 — cùng lỗi: "rổ vớt nước" → "rổ ráo nước".

### C. Soutetsu xưng "mình" thay vì "Tôi" (2 dòng)
Quy ước file + docs (locations §2.1): Soutetsu xưng "Tôi". Các "mình" khác trong file đều không phải lỗi: thành ngữ ("một mình", "tự mình"), hoặc Soutetsu xưng "cháu" khi nói với người lớn tuổi (không tính). Chỉ 2 dòng dưới đây dùng "mình" làm chủ ngữ mệnh đề — cùng mẫu lỗi đã thấy ở pilot, hearing và file whatsentertainment.
- **1660** (Soutetsu): JP 「まかせておけ。ハチロクとは長いつきあいだ。あれのこけしなら、僕は相当うまくつくれる気がする」 — VN cũ "Cứ giao cho tôi. Tôi đã quen biết Hachiroku từ lâu rồi. Nếu là Kokeshi của em ấy, tôi có cảm giác mình sẽ làm khá tốt đấy." → "tôi có cảm giác sẽ làm khá tốt đấy."
- **2593** (monologue): JP 「暖まってみて初めて自分が、かなり冷えていたことに気づかされる。」 — VN cũ "Chỉ khi ấm lên rồi tôi mới nhận ra rằng, mình đã bị lạnh đến nhường nào." → "tôi đã bị lạnh đến nhường nào."

### D. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (5 dòng)
**Quyết định 19/11 của Hieu: 御一夜 = "Ohitoyo"** (8/8 ở Hachiroku 12 再開発 + furigana おひとよ). Đây là 5 dòng duy nhất trong file có 御一夜 — cả 5 đều đang dùng "Ohimitera" theo docs cũ, cần đổi để thống nhất. Sau khi áp dụng, file này không còn "Ohimitera" nào.
- **1625** (Paulette): "Không chỉ riêng Ohimitera đâu ạ?" → "Không chỉ riêng Ohitoyo đâu ạ?"
- **2112** (Soutetsu): "Nhắc mới nhớ, ở Ohimitera không làm trứng luộc suối nước nóng nhỉ." → "ở Ohitoyo không làm…"
- **2140** (Paulette): "nếu chỉ thuê phòng nghỉ ở Ohimitera thì sẽ rất khó tìm quán ăn sáng." → "ở Ohitoyo thì…"
- **2512** (monologue): "Hikari hầu như chưa bao giờ rời khỏi Ohimitera. Và nếu ở Ohimitera, chỉ cần những người thân thiết là đủ cho mọi thứ." → cả hai chỗ thành "Ohitoyo".
- **2640** (monologue): "công việc ở Đường sắt Ohimitera sẽ……" → "công việc ở Đường sắt Ohitoyo sẽ……"

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **Chuỗi 1 (4 dòng):** 1264←2518, 2518←2375, 2375←2187, 2187 dịch mới (mục A).
- **Chuỗi 2 (3 dòng):** 2558←2568, 2568←1264, 1264 xem chuỗi 1 (mục A).
- **Chuỗi 3 (4 dòng):** 1969←2699, 2699←2697, 2697←2784, 2784←1245, 1245 dịch mới (mục A).
- **2 trùng lặp nội bộ:** "A!!" 1854/1969 (chỉ 1854 đúng); "Đợi đã! Đừng động đậy, đừng lại gần đây!!" 2091/2558 (chỉ 2091 đúng) — cả hai đều nằm trong các chuỗi trên.
- **0 tràn chương:** không dòng Việt nào trong file khớp với key của file khác trong dự án (đã kiểm tra qua chỉ mục Việt 84.381 mục); 26 dòng Việt trùng với file khác đều là câu ngắn thông dụng (tiếng kêu, "Ồ.", "Ừm.") đúng với JP của chính chúng — không phải copy.
- **9/11 bản sửa lệch vị trí khôi phục được từ trong file** (chuyển bản dịch đúng đang nằm ở key khác về); 2 dòng phải dịch mới (1245, 2187).

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (quy ước file + docs locations §2.1); Paulette xưng "Tôi", gọi Soutetsu "anh Soutetsu"; Hikari (4 tuổi) gọi Soutetsu "papa", gọi Paulette "mama", tự xưng tên mình "Hikari"; Reina gọi Soutetsu "Anh Soutetsu"; bà cụ làm Kokeshi xưng "tôi", gọi Soutetsu "người cha" (お父さん — đúng theo ngữ cảnh gia đình trong chương này, giữ nguyên).
- 御一夜 → **"Ohitoyo"** trong các bản sửa (1625, 2112, 2140, 2512, 2640) — **quyết định 19/11 của Hieu**. 御一夜鉄道 = "Đường sắt Ohitoyo" (2640).
- 鳴呼 = "Naruko" (hẻm núi Naruko, Kokeshi Naruko, tàu sưởi ấm Naruko); 鳴呼峡 = "hẻm núi Naruko" (1269, 1667); こけし = "Kokeshi" (búp bê Kokeshi); 温泉卵 = "trứng luộc suối nước nóng" (nhất quán cả file); 水切りかご = "rổ ráo nước" (sửa 2010/2136/2177, theo TW 瀝水籃); かまくら = "lều tuyết" (1633, 1945, 2064); かまくま = "gấu tuyết" — Hikari nói ngọng có chủ đích (かまくら + くま), Soutetsu sửa ở 1633, Hikari tự sửa ở 1945; 1726 "Gấu tuyết!" là đúng, KHÔNG sửa (xem mục 1726 đã rút); 日ノ本 = "Hinomoto" (2743); エアクラ không xuất hiện trong file này.
- 湯医, 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện trong file này. コン chỉ xuất hiện 1 lần ở 2540 nhưng đó là コンビニ (túi nilon cửa hàng tiện lợi), không phải cáo コン — không liên quan tới quyết định đang chờ.

## Đề xuất context mới
- Không có đề xuất mới cần Hieu quyết từ file này. Ghi nhận một thuật ngữ đã chọn trong bản sửa để dùng thống nhất về sau: **水切りかご = "rổ ráo nước"** (theo TW 瀝水籃; 3 dòng 2010/2136/2177).

## Dòng 1992 — ĐÃ CHỐT (19/11, theo ngữ cảnh Hieu yêu cầu trích — nằm trong khối TOML)
- **1992** (Hikari): JP 「いただくのー！」 / TW 「教我們吧！」 — VN cũ "Xin được chỉ giáo~!" đi theo TW ("dạy chúng tôi") là sai nghĩa: いただく không bao giờ có nghĩa "dạy". Ngữ cảnh trích được (1987 Hikari đang xoa bóp "Quý khách ơi~, có chỗ nào bị ngứa không ạ~"; 1990 "Buông em ra~, em muốn leo lên cơ~"; 1995 "Cháu hiểu rồi ạ~. Xoa xoa, xoa xoa"): cô bé đang được cho leo lên để xoa bóp, câu này là "Em xin nhận đây~!" — đúng gợi ý của Hieu, không cần chơi game tới đoạn đó. Bản sửa trong khối TOML: `1992 = "「Em xin nhận đây~!」"` (xưng "em" theo dòng 1990 ngay trước đó; dòng 1995 dùng "cháu" — nếu Hieu muốn thống nhất "cháu" cho Hikari thì đổi một chữ).

## Khối TOML sửa (23 dòng — đã kiểm tra parse bằng tomllib, đúng 23/23 key, giá trị khớp JSON)
```toml
1245 = "……Tôi muốn thật cẩn thận, nhưng cứ đứng yên ở đây thế này cũng đáng sợ."
1264 = "「……Có một khoảng trống dưới lớp tuyết nhỉ. Tôi đã dẫm phải chỗ đó, và chân phải bị lọt thỏm xuống.」"
1625 = "「Không chỉ riêng Ohitoyo đâu ạ? Ở Kyushu, suối nước nóng có làm món trứng này hiếm lắm.」"
1660 = "「Cứ giao cho tôi. Tôi đã quen biết Hachiroku từ lâu rồi. Nếu là Kokeshi của em ấy, tôi có cảm giác sẽ làm khá tốt đấy.」"
1700 = "「Này nhé~! Hikari muốn làm cái kêu cót két cơ~」"
1969 = "「Tôi không sao. Không thấy đau, có lẽ cũng không bị thương.」"
1992 = "「Em xin nhận đây~!」"
2010 = "「Rổ ráo nước, nhé. Paulette. Cô có thể đưa đầu xích của một chiếc rổ trống cho Hikari cầm giúp tôi được không?」"
2112 = "「Nhắc mới nhớ, ở Ohitoyo không làm trứng luộc suối nước nóng nhỉ.」"
2136 = "「Không phải dây mà là xích. Xích được buộc vào rổ ráo nước, và rổ ráo nước đang chìm trong nước suối nóng.」"
2140 = "「Chúng ta phải tham khảo thôi. Từ hồi tôi còn làm thị trưởng, đã có ý kiến cho rằng nếu chỉ thuê phòng nghỉ ở Ohitoyo thì sẽ rất khó tìm quán ăn sáng.」"
2177 = "「Xích, và rổ ráo nước, và nước suối nóng~」"
2187 = "「Anh Soutetsu, chân rút ra được không?」"
2375 = "Nhưng, cũng không biết dưới ngọn núi này có phải là mặt đất hay không. Nếu nó là một cái rãnh sâu, thì không phải chuyện đùa đâu, sẽ nguy hiểm đến tính mạng đấy."
2512 = "Từ khi sinh ra đến nay, Hikari hầu như chưa bao giờ rời khỏi Ohitoyo. Và nếu ở Ohitoyo, chỉ cần những người thân thiết là đủ cho mọi thứ."
2518 = "Dưới lớp tuyết. Không biết khoảng trống đó rộng bao nhiêu. Nếu nó rộng, có thể cả chân trái còn lại——toàn thân tôi sẽ rơi xuống dưới mất."
2558 = "Tôi chưa nắm rõ được tình hình. Vậy thì ưu tiên hàng đầu là ngăn ngừa tai nạn thứ cấp."
2568 = "Tiếp theo, dùng lời nói để xác nhận tình trạng hiện tại."
2593 = "Chỉ khi ấm lên rồi tôi mới nhận ra rằng, tôi đã bị lạnh đến nhường nào."
2640 = "Tất nhiên, nếu Hachiroku cũng đi thì công việc ở Đường sắt Ohitoyo sẽ…… cũng có lý do đó, nhưng——"
2697 = "Nói ra thì mới hiểu được sự nguy hiểm."
2699 = "Lời nói giúp tôi bình tĩnh lại, và tầm nhìn đang bị thu hẹp dần mở rộng ra."
2784 = "（Đây là một ngọn núi cao khoảng 1 mét. Cho dù có rơi xuống, chắc cũng không đến mức bị thương nặng——）"
```

## Kết bài
Paulette 05_鳴呼の町 là file thứ mười ba được audit toàn bộ (23/458 = 5,0% sai): nặng hơn hẳn file cùng chương whatsentertainment (2,8%) — và là file đầu tiên có lệch vị trí theo chuỗi xoay vòng nội bộ thay vì tràn từ chương khác. 11 dòng lệch tập trung ở cảnh trượt chân xuống hố tuyết, xoay vòng thành 3 chuỗi; 9/11 bản sửa khôi phục được từ trong file, chỉ 2 dòng phải dịch mới. Ngoài chuỗi lệch, lỗi còn lại chỉ ở mức câu/chữ (4 sai nghĩa, 5 thuật ngữ Ohitoyo, 2 xưng hô), 0 dòng chưa chắc chắn (1992 đã chốt từ ngữ cảnh ngày 19/11; 1726 đã rút vì audit nhận định nhầm về かまくま).

Việc còn lại của riêng file này là áp dụng khối TOML 23 dòng và chơi thử chương để nghiệm thu. Tổng 13 file đã audit: 1.454 dòng sai — và việc hai file cùng một chương 05 mà một file sạch (2,8%) một file lệch chuỗi (5,0%) cho thấy không thể đoán độ sạch từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng. File gợi ý tiếp theo theo thứ tự nặng trước: Grand Rewrite 04_ポーレット (489 dòng, chưa audit).
