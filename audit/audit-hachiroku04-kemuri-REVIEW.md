# Audit — ハチロク04_煙には煙を (01_Hachiroku) — "Lấy khói trị khói"

- File: `ハチロク04_煙には煙を.txt.toml` — route 01_Hachiroku, **389 dòng script**, 5 strong candidates.
- Nội dung: thử nghiệm khói lò sưởi trong toa hành khách (buzzer, Nagi thèm bấm còi); nảy ra ý "lấy khói trị khói" — chạy chuyến tàu BBQ thịt nướng để khói thịt chặn khói lò; chụp ảnh kỷ niệm chuyến số 1; Paulette báo đặt vé quá tải, bàn tăng chuyến + đào tạo Hibiki/Nagi, nhắc tin đồn đầu máy 6200 "Nelson".
- Phương pháp: đọc hết 389/389 dòng theo JP + TW (CSV3), đối chiếu TOML-2. Không lấy mẫu.

## §1. Kết quả

**10 dòng sai / 389 (2,6%)** — file khá sạch; lỗi tập trung ở đại từ xưng hô của Soutetsu (4) + Hibiki (2).

- Lệch vị trí (misaligned) **0**, chuỗi xoay (rotation) **0**, nhiễm chéo file khác **0**, dòng mồ côi (orphan) **0**, chưa dịch **0**, trùng khóa **0**.
- Phân loại (10): xưng hô 6 (1848, 2415, 2058, 2425, 2392, 1920), sai nghĩa 2 (1855, 2383), cụt câu/mảnh vỡ 1 (2062), gasp 1 (2455, từ sweep).
- `[selections]` rỗng (0 mục). Không có thẻ `%l` sai định dạng nào trong file (0/389; đếm `\x%l` vs `%l;#;` khớp tuyệt đối).
- Không có bản sao file này (md5 duy nhất trong toàn bộ TOML-2; 1 copy, không áp fix 2 nơi).

## §2. Chi tiết từng dòng sai

### Xưng hô — Soutetsu "anh" → "tôi" với Hachiroku (4 dòng, quy tắc đã chốt 20/11)

- **2058** (双鉄). JP: 「土日祝を一日二便に増発するくらいであれば、僕の体力的にはまったく問題ない」. Đối tượng là Hachiroku (monologue 2673 ngay trước: ánh mắt Hachiroku hướng về Soutetsu; cô vừa nói 1929 về huấn luyện song song). VN cũ: "…thì thể lực của **anh** hoàn toàn không có vấn đề gì." → **"thì thể lực của tôi hoàn toàn không có vấn đề gì."**
- **2425** (双鉄). JP: 「ならばハチロク、除煙板の図面を起こしてくれ」 — gọi thẳng tên Hachiroku. VN cũ: "…em phác thảo bản vẽ tấm chắn khói giúp **anh** nhé." → **"…giúp tôi nhé."**
- **2392** (双鉄). JP: 「その間僕は、整備清掃をしておこう」 — "その間" là lúc Hachiroku bàn ca trực với Paulette (2328/2136). VN cũ: "Trong lúc đó, **anh** sẽ đi dọn dẹp bảo dưỡng." → **"Trong lúc đó, tôi sẽ đi dọn dẹp bảo dưỡng."**
- **1920** (双鉄). JP: 「頑張らねばと――僕も思っていただけだ。まずは、観光振興のため、そして御一夜を守るため」 — trả lời Hachiroku 2442 (「双鉄様？ひょっとしてお疲れなのですか？」), Hachiroku đáp lại 2195. VN cũ: "**Anh** cũng chỉ đang nghĩ――mình phải cố gắng thôi." → **"Tôi cũng chỉ đang nghĩ――mình phải cố gắng thôi."**

Các dòng "anh" khác của Soutetsu đã kiểm chứng và GIỮ (đối tượng đúng nhóm "anh"): 2126 (Hibiki), 1842 (Nagi/Hibiki), 1922 (Fukami — "anh" với Fukami đúng quy tắc), 2266 (Hibiki), 1557 (Hibiki), 2124 (Hibiki), 2003 (trả lời Nagi), 2133 "Tôi muốn thảo luận" (đúng, với Hachiroku). Dòng 2389 "anh" nói với cả đội (Hibiki + Hachiroku) — giữ, ghi chú §4.

### Xưng hô — Hibiki (2 dòng)

- **1848** (日々姫). JP: 「今日はねぇね――姉さんがおでかけだから、私たち、何もなくても外食の予定だったし」 — người nói là Hibiki (nữ), "私たち" là Hibiki (+ Soutetsu). VN cũ: "…nên dù không có chuyện này thì **bọn anh** cũng định đi ăn ngoài mà." → **"…thì bọn em cũng định đi ăn ngoài mà."**
- **2415** (日々姫). JP: 「決まりね！　じゃ、ちょっとだけ待ってて、着替えてくるから」 — chính Hibiki đi thay đồ. VN cũ: "Quyết định vậy nhé! Vậy chờ **anh chị** một chút, **anh chị** đi thay đồ đã." → **"Quyết định vậy nhé! Vậy chờ bọn em một chút, bọn em đi thay đồ đã."**

### Sai nghĩa (2 dòng)

- **1855** (日々姫). JP: 「煙で煙って――にぃに――兄さん、正気ですか？夏の御一夜の、しかもこの広さの室内ですよ？」 — "この広さの室内" là phòng toa tàu chật hẹp; TW xác nhận: "車廂很狹窄啊". VN cũ: "…Mùa hè ở Ohito, mà phòng lại **rộng** chừng này cơ mà?" (đảo nghĩa: rộng ↔ chật). → **"…Mùa hè ở Ohito, mà lại trong căn phòng chật hẹp thế này cơ mà?"** ("Ohito" giữ nguyên chờ đợt thống nhất, §3.)
- **2383** (ポーレット). JP: 「6200が出るかもしれないって噂、前から聞いてるんです」 — 出る = đầu máy cũ ra khỏi kho/tái xuất; TW: "或許會再出山的傳聞". VN cũ: "…tin đồn 6200 có thể sẽ **xuất xưởng**." ("xuất xưởng" = mới sản xuất xong, sai sắc thái). → **"…tin đồn 6200 có thể sẽ xuất hiện trở lại."**

### Cụt câu / mảnh vỡ (1 dòng)

- **2062** (ふかみ). JP: 「焼肉列車……っていうことにするなら、エプロン――服が汚れないようつけて貰っておかしくない。です、し」. VN cũ kết bằng mảnh vỡ: "…để quần áo không bị bẩn cũng không có gì lạ. **Cả,**" (dịch vụn đuôi "し" thành "Cả," treo lơ lửng; các dòng Fukami khác diễn đuôi し bằng "ạ"/"…"). → **"…để quần áo không bị bẩn cũng không có gì lạ đâu ạ."** Thẻ `%l` giữ nguyên.

### Gasp — sweep (1 dòng)

- **2455** (双鉄). JP: 「っ！」 — gasp cả dòng. Sweep `lost-gasp-whole` đã liệt kê đúng. VN cũ: 「!」 → **「Ư!」**.
- Sweep còn 1 mục cho file: 3088 （ぐ～っ） → VN （Rột~） — đã diễn bằng SFX khác, **không sửa** (đúng loại "already-rendered").

## §3. Thuật ngữ dạng cũ — chờ đợt thống nhất, KHÔNG tính sai

- "Ohito" (御一夜 → "Ohitoyo" đã chốt): **6 dòng** — 2073, 1855, 2393, 2105, 2464, 1920. Hai dòng trong số đó nằm trong fix của audit này (1855, 1920) nhưng chỉ sửa phần sai nghĩa/xưng hô, giữ nguyên "Ohito" để đợt thống nhất đổi một lượt.
- "Tuyến Yui" / "bến tàu Yui" (湯医/湯医線 → "Yunoi" đã chốt): **2 dòng** — 2947, 2464.
- "ông nội" cho 爺ちゃん (2420, 2203): giữ theo toàn dự án; câu hỏi "ông nội" hay "ông ngoại" vẫn chờ Hieu chốt (§6).

## §4. Các dòng đã kiểm tra kỹ và GIỮ NGUYÊN (không sửa)

- **Nagi → Fukami dùng "cậu" (1894, 2076, 2078) — GIỮ.** Đếm lại toàn dự án: Nagi nói với Fukami dùng "bé" 55× vs "cậu" 25× (trong đó file này 3× "cậu") — "cậu" là biến thể đã có sẵn, không phải lỗi. Quy tắc "bé" chỉ cấm dùng "chị" (tiền lệ file 08b). Không đổi.
- **Paulette tự xưng "tôi" (2189, 2192) vs "em" (1988, 2383, 2011, 2101) — GIỮ, ghi chú.** Không có quy tắc dự án nào cấm Paulette dùng "tôi"; hai dòng "tôi" đều ở ngữ cảnh quản lý/kinh doanh trang trọng (bàn tăng chuyến, tuyển phụ lái). Nếu Hieu muốn thống nhất "em" thì đổi trong đợt thống nhất.
- **Soutetsu "anh" với cả đội 2389 — GIỮ, ghi chú.** Monologue 2861 nói rõ anh nói với cả đội (Hibiki + Hachiroku), Hibiki đáp lại 1864; đối tượng chính là Hibiki. Trường hợp ranh giới, giữ theo nguyên tắc "nghi ngờ thì giữ".
- **Ruby [ハチロク,3] trên 8620 bị bỏ (1544, 1531, 2459) và [ネルソン,3] trên 6200 (1533) — GIỮ, ghi chú.** Số hiệu hiển thị (8620/6200) vẫn đúng; ruby chỉ là cách đọc. Nhưng không nhất quán với các dòng khác trong file (2683 "Rokunii", 2212 "Gyusha", 2048 "chùa Yurei", 1983 "Ngài Aki", 1898 "Tobu" đều diễn ruby thành tên). Cần Hieu/parent quyết có bổ sung ruby đọc thành tên trong đợt thống nhất hay không — không tự đổi trong audit này.
- **2072** — chơi chữ 間違いなか/町だけに của Nagi ("Chắc chắn rồi nha! Chỉ là thị trấn thôi mà.") — chơi chữ không chuyển được sang Việt, bản dịch giữ được nghĩa "chắc chắn"; giữ.
- **2201** "Là như vậy…….sao ạ?" — dấu "……." thừa một chấm, lỗi chính tả nhỏ (cosmetic), không tính sai.
- **1958** 「う――む」 → "Ư――m." — giữ (diễn âm trầm ngâm; khác với 1991 ううむ → "Hừm……" nhưng cả hai đều chấp nhận được).
- **1927** Kon kêu 『ケン？』 → "Keng?" — giữ (phiên âm Việt hoá tiếng kêu của Kon; "Ken?" sát JP hơn nhưng "Keng?" không sai nghĩa).
- **1519** ――たかと思うと、思い切り押す → "――Rồi con bé nhấn mạnh một cái." — giữ (bỏ sắc thái "vừa nghĩ đã…" nhưng không sai nghĩa).
- **2944** "Dạo gần đây tôi thấy cảnh này hơi bị thường xuyên đấy." — giữ (diễn しばしば bằng "hơi bị thường xuyên", hơi vụng nhưng đúng nghĩa).
- **2073** "thợ mộc ở Ohito" cho 職人 — giữ ("thợ mộc" trong ngữ cảnh sửa chữa quán; "Ohito" chờ thống nhất).
- **1935** むぎゅっ → "Úi!", **3094** ぐいっ → "Giật!", **3091** ブーーーーーーーーっ → "Biiiiiiiiiiiiiiiiiiiip!", **2776** クスクス → "khúc khích" — giữ (SFX diễn ngẫu hứng theo quy tắc Hieu 22:05; cười là cười, không thành tiếng rên).
- **1544/1531** tên chuyến 『バーベキュートレイン　もくもく8620』 → "Chuyến tàu Thịt nướng Mokumoku 8620" — giữ (xem ghi chú ruby trên).
- **2212** [ぎゅうしゃ,1]牛炙 → quán "Gyusha" — giữ (diễn ruby thành tên, đúng mẫu 2048/1983).
- **2391** [くまもとあかおう,3]隈元赤王 → "Kumamoto Akaou" — giữ, đúng JP (TW viết nhầm "隈元和王"; JP thắng TW).
- **2166** [マイ・マスター,2]双鉄様 → "Thưa ngài Soutetsu, [マイ・マスター,2]Master của em." — giữ (giữ thẻ như TW giữ [我的主人,3]).
- **1539** 共感 → "cộng cảm" (Reina truyền qua Railord-link) vs 2758 "đồng cảm" (giữa người với người) — giữ, đúng phân biệt đã chốt.
- **2947** 湯医線 → "Tuyến Yui" (chờ thống nhất, §3); キハ07 → "KiHa 07", エアクラ → "Aircra", ナビ → "Navi" — giữ, đúng thuật ngữ.
- **2474/2476** hai dòng lặp 『「出発！　進行！！」』 — giữ (JP cũng lặp nguyên văn hai lần; CSV3 và TOML khớp tuyệt đối).
- **21 VN ngắn trùng chéo file** (「A.」, 「Hử?」, 「Ừ.」, 「Ngài Soutetsu?」…) — đều là câu cảm thán/câu gọi mẫu, JP tương ứng khớp nghĩa; không phải nhiễm chéo.
- **0 VN trùng nhau trong file** (không có chuỗi xoay); **0 khóa trùng** trong CSV3 và TOML (389 khóa duy nhất); CSV3 VN khớp TOML tuyệt đối 389/389 (chênh lệch \n ở lần đếm đầu chỉ là cách hiển thị khi so sánh, đã kiểm chứng trực tiếp: chuỗi bằng nhau hoàn toàn).

## §5. Kiểm chứng cơ học

- CSV3: 389 dòng, 1 set duy nhất (không có dual-set), 0 khóa trùng, 0 VN trống, 0 JP trống.
- TOML-2: 389 khóa `[script]`, md5 `f775ff2196ac509ba3cc7832046b3770`, không có file trùng nội dung trong toàn bộ TOML-2 (1 copy duy nhất). `[selections]` rỗng.
- JSON: 10 mục, khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 10/10.
- Khối TOML: parse được bằng tomllib, 10 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3).
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (log build: 1848 anh→em; 1855 rộng→chật hẹp; 1920 Anh→Tôi; 2058 anh→tôi; 2062 bỏ "Cả," thêm "đâu ạ"; 2383 xuất xưởng→xuất hiện trở lại; 2392 anh→tôi; 2415 anh chị→bọn em ×2; 2425 anh→tôi; 2455 thêm Ư).
- Sweep: 2 mục cho file — 2455 áp nguyên (đã kiểm chứng đúng JP), 3088 không sửa (đã diễn).
- Lượt soát 2: **10/10 tái kiểm chứng, 0 bỏ, 9 sửa** — bản nháp đầu làm rơi cặp 「」 ở 9 dòng thoại (1848, 1855, 1920, 2058, 2062, 2383, 2392, 2415, 2425); đã khôi phục bằng cách áp thay đổi lên đúng chuỗi VN cũ và kiểm chứng lại diff từng dòng.

## §6. Khối TOML (đã kiểm chứng parse)

```toml
"1848" = "「Hôm nay chị hai――chị Mayami đi vắng,\\nnên dù không có chuyện này thì bọn em cũng định đi ăn ngoài mà.」"
"1855" = "「Khói trị khói á――anh hai――anh Soutetsu, anh tỉnh táo không đấy?\\nMùa hè ở Ohito, mà lại trong căn phòng chật hẹp thế này cơ mà?」"
"1920" = "「Tôi cũng chỉ đang nghĩ――mình phải cố gắng thôi.\\nTrước hết là vì chấn hưng du lịch, và vì bảo vệ Ohito.」"
"2058" = "「Nếu chỉ tăng cường thêm 2 chuyến một ngày vào cuối tuần và ngày lễ,\\nthì thể lực của tôi hoàn toàn không có vấn đề gì.」"
"2062" = "「Nếu gọi là \\x%l列車;#00ffc040;Chuyến tàu%l;#; Thịt nướng……thì việc phát tạp dề――\\nđể quần áo không bị bẩn cũng không có gì lạ đâu ạ.」"
"2383" = "「Tất nhiên là em đang cân nhắc cho tương lai rồi.\\nTừ trước em đã nghe tin đồn \\x%l6200;#00ffc040;6200%l;#; có thể sẽ xuất hiện trở lại.」"
"2392" = "「Trong lúc đó, tôi sẽ đi dọn dẹp bảo dưỡng.」"
"2415" = "「Quyết định vậy nhé! Vậy chờ bọn em một chút,\\nbọn em đi thay đồ đã.」"
"2425" = "「Nếu vậy Hachiroku,\\nem phác thảo bản vẽ \\x%l除煙板;#00ffc040;tấm chắn khói%l;#; giúp tôi nhé.」"
"2455" = "「Ư!」"
```

Kiểm chứng: khối parse được bằng tomllib, 10 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build §5).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohito" → "Ohitoyo" (6 dòng: 2073, 1855, 2393, 2105, 2464, 1920) + "Yui" → "Yunoi" (2 dòng: 2947, 2464) — theo tiền lệ các file trước, fix trong đợt thống nhất.
- "ông nội" cho 爺ちゃん (2420, 2203) — câu hỏi "ông nội" hay "ông ngoại" vẫn chờ Hieu chốt (theo toàn dự án hiện dùng "ông nội").
- Paulette tự xưng "tôi" (2189, 2192) vs "em" — ngữ cảnh quản lý trang trọng; nếu Hieu muốn thống nhất "em" thì đổi trong đợt thống nhất.
- Ruby đọc [ハチロク,3] trên 8620 (1544, 1531, 2459) và [ネルソン,3] trên 6200 (1533) bị bỏ, trong khi các ruby tên khác trong file đều được diễn thành tên — cần quyết có bổ sung trong đợt thống nhất hay không.
- SFX 1958 "Ư――m" và 1927 "Keng?" là diễn ngẫu hứng theo quy tắc Hieu 22:05 — nếu Hieu muốn cách diễn khác thì đổi.

## Kết bài

File ハチロク04_煙には煙を: 389 dòng đã đọc hết, **10 dòng sai (2,6%)** — 6 xưng hô (Soutetsu "anh"→"tôi" với Hachiroku 4, Hibiki "bọn anh"/"anh chị"→"bọn em" 2), 2 sai nghĩa, 1 cụt câu, 1 gasp (sweep). Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. JSON 10 khóa chuỗi; khối TOML parse OK, 10 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 10/10; lượt soát 2: 10/10, 0 bỏ, 9 sửa (khôi phục 「」).
