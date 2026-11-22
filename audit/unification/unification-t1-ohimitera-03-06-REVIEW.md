# Unification U1b — §1 T1: 御一夜 → "Ohitoyo" — folders 03_Paulette / 04_Reina / 05_Mayami / 06_Kisaki

Batch: **U1b** · Mục: **§1 T1 (DECIDED 19/11, Hieu)** · Phạm vi: chỉ dạng cũ **"Ohimitera"** trong giá trị hiện tại, chỉ 4 folder **03_Paulette, 04_Reina, 05_Mayami, 06_Kisaki**. Dạng "Ohito" trần và "Đường sắt Ohito" thuộc T1-phần-còn-lại / T2 — KHÔNG đụng trong đợt này (trừ 4 dòng "Đường sắt Ohimitera" xem §Ghi chú ranh giới).

## 1. Phạm vi (scope)

- **Mục T1** (UNIFICATION-LIST.md §1, DECIDED 19/11 Hieu): 御一夜 → "Ohitoyo", không bao giờ "Ohimitera"/"Ohito". Tổng CSV3 good-set: "Ohimitera" 824 dòng + "Ohito" 398 dòng = 552 dòng còn lại ước lượng 333 + 219.
- **Đợt này (U1b):** chỉ "Ohimitera" trong 4 folder 03/04/05/06. **52 dòng sửa**, 12 file.
- **Không thuộc đợt này:** "Ohito" trần (T1 phần còn lại), "Đường sắt Ohito" → "Đường sắt Ohitoyo" (T2), "Jutsu-sen" → "Jutsusen" (T17), "Tuyến Yui" → "tuyến Yunoi" (T7) — các dạng này nếu cùng xuất hiện trong một dòng được sửa ở đây thì được GIỮ NGUYÊN để batch của chúng xử lý (xem §5).
- **Không có dòng nào bị loại vì JP thiếu 御一夜:** cả 52 ứng viên đều có 御一夜 (hoặc 御一夜鉄道) trong JP — 0 dòng flag misalignment (xem §5).

## 2. Phương pháp (method)

1. **CSV3 good-set:** đọc toàn bộ 91.731 dòng `sources/csv3/Matetsu Last Run - Trang t#U00ednh3.csv`, bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md` (bộ stale = folder "home" của file) → **87.833 dòng good-set** (khớp §0). Trong 4 folder 03/04/05/06, CSV3 VN chứa "Ohimitera" ở **268 dòng**. File `共通04_キハ07。ポーレットとれいな` có 2 bộ: bộ stale 00_Common đã bỏ, bộ good 03_Paulette được dùng.
2. **Giá trị hiện tại (old_vn):** nạp TOÀN BỘ fix list trước đó — 217 file `audit-*-wrong.json` (9.200 cặp (basename,key) map được) + 66 file `moans/moan-*-wrong.json` (1.516 cặp, map đủ 100%). Map entry → (basename,key) bằng khớp chính xác (key, JP) với CSV3 good-set; entry dạng dict không JP (audit-00common14, 52 mục) map bằng (key, old_vn); entry trùng lặp (key,JP) khớp 2 bản sao TOML (14 mục) áp fix cho cả 2 bản. Giá trị hiện tại = fix moan nếu có, else fix audit, else CSV3 VN (moan > audit > CSV3).
   - Không map được: 47 mục audit, toàn bộ thuộc `audit-lr-nagih2-wrong.json` (dict key→fix, không JP/old_vn, file folder 07_Nagi_Fukami — ngoài phạm vi đợt này, không ảnh hưởng giá trị hiện tại của 4 folder này). Bỏ qua có chủ đích: entry không có fix dạng chuỗi (file rotation `audit-obasan-wrong.json`, dòng uncertain Paulette 13 key 1357 fix null) — chúng không thay đổi giá trị hiện tại.
   - Trong 268 dòng CSV3-VN "Ohimitera" của 4 folder: **216 dòng đã sửa sẵn trong audit** (giá trị hiện tại đã là "Ohitoyo" — phần lớn ở 稀咲03 và 稀咲h3), còn lại **52 ứng viên**. Không có dòng nào do fix list đưa "Ohimitera" vào mới (0 dòng). Không có ứng viên nào có nguồn moan (47 CSV3 + 5 audit, 0 moan).
3. **Kiểm tra từng ứng viên:** đọc JP (+TW) của cả 52 dòng. Điều kiện sửa: JP chứa 御一夜 hoặc 御一夜鉄道. Kết quả: **52/52 đạt** — không có dòng nào JP thiếu 御一夜. Fix = giá trị hiện tại với "Ohimitera" → "Ohitoyo" (toàn bộ lần xuất hiện trong dòng, kể cả trong gloss %l nếu có — kiểm chứng: 0 lần xuất hiện nằm trong thẻ %l; mọi lần xuất hiện đều là display text). JP trong thẻ %l không đụng tới.
4. **Đối chiếu số lượng:** đếm lại toàn dự án bằng cùng phương pháp cho **311 dòng** giá trị hiện tại còn "Ohimitera" (CSV3 VN: 824), so với ước lượng §0 là 333. Chênh 22 dòng: §0 tính remainder bằng map 9.190 cặp audit (slug+md5/key-overlap), còn đợt này map được 9.200 cặp audit + toàn bộ moan — remainder thực tế thấp hơn ước lượng. Theo folder (giá trị hiện tại): 02_Hibiki 176 · 01_Hachiroku 45 · 09_Grand 31 · **05_Mayami 26 · 03_Paulette 11 · 04_Reina 11 · 06_Kisaki 4** · 07_Nagi_Fukami 7 · 00_Common/08_Niiroku/10_Chikuni/11_Other 0. Sau đợt này T1 còn **259 dòng** (311 − 52) ở các folder còn lại. Con số "~110 dòng cho 4 folder" trong task là ước lượng cũ — thực tế chỉ 52 vì 216 dòng đã sửa sẵn trong audit.

## 3. Các dòng sửa (52 dòng — mỗi dòng: file / key / JP / TW / old_vn / fix / lý do)

Lý do chung mọi dòng: JP chứa 御一夜 (hoặc 御一夜鉄道), quy tắc đã chốt 19/11 "Ohitoyo" — "Ohimitera" là dạng sai do Gemini đọc nhầm. Fix chỉ đổi đúng thuật ngữ, không đụng bất kỳ chữ nào khác (kiểm chứng máy: fix khôi phục về old_vn khi đổi ngược "Ohitoyo"→"Ohimitera", 52/52).

### 03_Paulette / `ポーレット03_廃炭鉱.txt.toml` — 3 dòng

**Key 1368** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「……御一夜にずっと暮らしている人たちは、\nこの景色、絶対に知ってる筈なのに――どうして」
- TW: 「……一直生活在御一夜的人們一定知道這幅景象——但為什麼」
- old_vn: 「……Những người luôn sống ở Ohimitera,\nchắc chắn phải biết đến cảnh tượng này chứ——vậy mà tại sao.」
- fix: 「……Những người luôn sống ở Ohitoyo,\nchắc chắn phải biết đến cảnh tượng này chứ——vậy mà tại sao.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2084** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「資源と出来れば何よりだが……出来なかった場合には、\nこの廃鉱山、御一夜にずいぶんな迷惑を」
- TW: 「這座廢礦山要是能成為經營資源自然是最好的……要是不成，那就真是給御一夜添了大麻煩」
- old_vn: 「Nếu có thể biến thành tài nguyên thì không còn gì bằng…… nhưng trong trường hợp không thể,\nthì khu mỏ bỏ hoang này, sẽ mang đến rắc rối lớn cho Ohimitera.」
- fix: 「Nếu có thể biến thành tài nguyên thì không còn gì bằng…… nhưng trong trường hợp không thể,\nthì khu mỏ bỏ hoang này, sẽ mang đến rắc rối lớn cho Ohitoyo.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2892** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: この過去は、この痕跡は。\n御一夜の未来を映す鏡であるとも見れるのだ。
- TW: 這些過去，這些痕跡，彷彿在暗示著御一夜的未來。
- old_vn: Quá khứ này, những dấu tích này.\nCũng có thể coi là tấm gương phản chiếu tương lai của Ohimitera.
- fix: Quá khứ này, những dấu tích này.\nCũng có thể coi là tấm gương phản chiếu tương lai của Ohitoyo.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 03_Paulette / `ポーレット04_ヒヤリング.txt.toml` — 5 dòng

**Key 1517** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「術仙廃炭鉱の再活用を観光振興と繋げたのなら、\n御一夜は必ずや、かつてに勝る輝きを得る」
- TW: 「如果能讓術仙廢煤礦的再利用成為旅遊業復興的一環，御一夜肯定能重新獲得不亞於過去的繁榮」
- old_vn: 「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsu-sen với chấn hưng du lịch,\nthì Ohimitera chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」
- fix: 「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsu-sen với chấn hưng du lịch,\nthì Ohitoyo chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1557** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜市役所の朝イチは、\n午前八時三十分です」
- TW: 「御一夜市政府的一早，是指早上８點３０分」
- old_vn: 「Đầu giờ sáng của tòa thị chính Ohimitera là,\n8 giờ 30 phút sáng ạ.」
- fix: 「Đầu giờ sáng của tòa thị chính Ohitoyo là,\n8 giờ 30 phút sáng ạ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1636** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「そうですか。はじめまして、右田さん。\n御一夜市役所、総務部長の宮本です」
- TW: 「是這樣啊。您好，雙鐵先生。我是御一夜市政府總務部部長宮本」
- old_vn: 「Vậy sao. Chào cậu, cậu Migita.\nTôi là Miyamoto, Trưởng phòng Tổng vụ của Tòa thị chính Ohimitera.」
- fix: 「Vậy sao. Chào cậu, cậu Migita.\nTôi là Miyamoto, Trưởng phòng Tổng vụ của Tòa thị chính Ohitoyo.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2230** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 鉄道がとっくに廃線となり、\nだから安心して暮らせていた、この町、御一夜。
- TW: 御一夜的鐵路早已成為廢線，所以我才能安心生活在這裡。
- old_vn: Đường sắt đã bị bỏ hoang từ lâu,\nnhờ vậy mà tôi mới có thể an tâm sinh sống ở thị trấn Ohimitera này.
- fix: Đường sắt đã bị bỏ hoang từ lâu,\nnhờ vậy mà tôi mới có thể an tâm sinh sống ở thị trấn Ohitoyo này.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2504** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 金の髪が、まだ収まらぬ風に煽られ踊っている。\n瞳は青。御一夜の空より、クマ川よりなお、澄んだ青。
- TW: 還未收住勢頭的勁風，撥弄著她金色的秀髮。她那碧藍的雙眸比御一夜的天空、隈河的河水還要清澈幾分。
- old_vn: Mái tóc vàng tung bay trong cơn gió vẫn chưa dứt.\nĐôi mắt màu xanh thẳm. Một màu xanh trong trẻo hơn cả bầu trời Ohimitera, hơn cả dòng sông Kuma.
- fix: Mái tóc vàng tung bay trong cơn gió vẫn chưa dứt.\nĐôi mắt màu xanh thẳm. Một màu xanh trong trẻo hơn cả bầu trời Ohitoyo, hơn cả dòng sông Kuma.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 03_Paulette / `ポーレット04_鳴呼いきストーブ列車.txt.toml` — 1 dòng

**Key 2809** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 僕とて、御一夜の――
- TW: 雖然只是暫時的工作……
- old_vn: Tôi cũng là một người của Ohimitera——
- fix: Tôi cũng là một người của Ohitoyo——
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 03_Paulette / `ポーレットh3_誘惑アイスコーヒー.txt.toml` — 2 dòng

**Key 1255** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 関連質問の通告を受け、急ぎ探したが、\n市役所内にも御一夜鉄道にも無かったものだ。
- TW: 在接到相關的詢問後，我們趕忙尋找了一下，但是市政府和御一夜鐵道都沒有這個數據。
- old_vn: Nhận được thông báo về các câu hỏi liên quan, chúng tôi đã vội vàng tìm kiếm,\nnhưng cả trong Tòa thị chính lẫn Đường sắt Ohimitera đều không có.
- fix: Nhận được thông báo về các câu hỏi liên quan, chúng tôi đã vội vàng tìm kiếm,\nnhưng cả trong Tòa thị chính lẫn Đường sắt Ohitoyo đều không có.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1347** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 御一夜駅を発着する貨物列車の本数と、\nその総輸送量との統計データ。
- TW: 我們要找的是御一夜站發送的貨運列車班次和運輸總量的統計數據。
- old_vn: Dữ liệu thống kê về số lượng tàu chở hàng đến và đi tại ga Ohimitera,\ncùng với tổng khối lượng vận chuyển của chúng.
- fix: Dữ liệu thống kê về số lượng tàu chở hàng đến và đi tại ga Ohitoyo,\ncùng với tổng khối lượng vận chuyển của chúng.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 04_Reina / `lrれいな追加03_れいなとのレール.txt.toml` — 4 dòng

**Key 675** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「……それゆえ御一夜の観光デートを、\nれいなは好んでくれてたのだなぁ」
- TW: 「……所以玲奈，你才這麼喜歡御一夜旅遊約會啊」
- old_vn: 「……Vì thế nên Reina mới thích\nnhững buổi hẹn hò tham quan quanh Ohimitera đến vậy nhỉ.」
- fix: 「……Vì thế nên Reina mới thích\nnhững buổi hẹn hò tham quan quanh Ohitoyo đến vậy nhỉ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 981** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「けど、御一夜に来て、ポーレットと出会ってそしたら。\nいろんな線路の上にもれいなの世界がひろがって」
- TW: 「但是自從來到御一夜，見到了波萊特後，玲奈的世界在許多條鐵路之上擴展了」
- old_vn: 「Nhưng mà, khi đến Ohimitera, gặp được chị Paulette thì.\nThế giới của Reina đã mở rộng ra trên rất nhiều tuyến đường sắt khác nhau nha~」
- fix: 「Nhưng mà, khi đến Ohitoyo, gặp được chị Paulette thì.\nThế giới của Reina đã mở rộng ra trên rất nhiều tuyến đường sắt khác nhau nha~」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1182** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜きれいでたのしいですし、そうてつさんに\nいろいろ教えてもらえるのもうれしいですからねぇ」
- TW: 「御一夜很漂亮也很有趣，聽雙鐵先生說來歷說故事也很滿足啊」
- old_vn: 「Ohimitera vừa đẹp vừa vui, hơn nữa được anh Soutetsu\nchỉ cho nhiều thứ cũng làm Reina vui lắm nha~」
- fix: 「Ohitoyo vừa đẹp vừa vui, hơn nữa được anh Soutetsu\nchỉ cho nhiều thứ cũng làm Reina vui lắm nha~」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1578** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 御一夜の観光スポット群は、いまとなっては僕の庭だ。\n無論詳しく解説できるし、れいなも大いに喜んでくれる。
- TW: 御一夜的旅遊勝地，現在彷彿已經成了我的庭院。我可以做詳盡的解說，玲奈也會很高興。
- old_vn: Các điểm du lịch ở Ohimitera giờ đây giống như khu vườn nhà tôi vậy.\nTất nhiên tôi có thể giải thích cặn kẽ, và Reina cũng sẽ rất vui.
- fix: Các điểm du lịch ở Ohitoyo giờ đây giống như khu vườn nhà tôi vậy.\nTất nhiên tôi có thể giải thích cặn kẽ, và Reina cũng sẽ rất vui.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 04_Reina / `れいな03_しゅっぱつしんこう.txt.toml` — 7 dòng

**Key 1300** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「ううん、れいな。まだそこまでは無理。\n御一夜からは最優先で、[やつしろ,2]八ツ城までを復線させる」
- TW: 「不，玲奈，現在還連不到那裡。御一夜現在要最優先完成至八代段的廢線恢復工作」
- old_vn: 「Không đâu, Reina. Vẫn chưa thể đến mức đó được.\nTừ Ohimitera, ưu tiên hàng đầu là khôi phục tuyến đường đến Yatsushiro.」
- fix: 「Không đâu, Reina. Vẫn chưa thể đến mức đó được.\nTừ Ohitoyo, ưu tiên hàng đầu là khôi phục tuyến đường đến Yatsushiro.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1337** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「線路、\n御一夜からそこまで繋がることになるんですかぁ？」
- TW: 「到時候線路也會從御一夜連接到那裡嗎？」
- old_vn: 「Đường ray,\nsẽ được nối từ Ohimitera đến tận đó luôn ạ?」
- fix: 「Đường ray,\nsẽ được nối từ Ohitoyo đến tận đó luôn ạ?」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1455** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「はい。今までのように、全ての\x%l列車;#00ffc040;列車%l;#;が御一夜に帰着して\n一日を終えるとは限らなくなりますから」
- TW: 「嗯，因為到時候就不一定能像之前那樣所有的\x%l列車;#00ffc040;列車%l;#;都在一天結束前回到御一夜了」
- old_vn: 「Vâng ạ. Vì sẽ không còn chuyện tất cả các \x%l列車;#00ffc040;tàu%l;#; đều trở về Ohimitera\nđể kết thúc một ngày như trước đây nữa.」
- fix: 「Vâng ạ. Vì sẽ không còn chuyện tất cả các \x%l列車;#00ffc040;tàu%l;#; đều trở về Ohitoyo\nđể kết thúc một ngày như trước đây nữa.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1474** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「うん。わたしは御一夜を離れられる状況じゃないから」
- TW: 「嗯，現在的情況不允許我離開御一夜嘛」
- old_vn: 「Ừ. Chị đang trong tình cảnh không thể rời khỏi Ohimitera được.」
- fix: 「Ừ. Chị đang trong tình cảnh không thể rời khỏi Ohitoyo được.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2160** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 僕は御一夜に縛られて、れいなは矢幡へ送り込まれる。\n共に過ごせる時間が裂かれ、壊れてしまう。
- TW: 我被束縛在御一夜，玲奈則被送到八幡去。共處的時間被撕裂、破壞。
- old_vn: Tôi bị trói buộc ở Ohimitera, còn Reina bị đưa đến Yahata.\nKhoảng thời gian chúng tôi có thể ở bên nhau sẽ bị xé nát, bị phá hủy.
- fix: Tôi bị trói buộc ở Ohitoyo, còn Reina bị đưa đến Yahata.\nKhoảng thời gian chúng tôi có thể ở bên nhau sẽ bị xé nát, bị phá hủy.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2223** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 新しい車輌を迎えるために。\n新しい御一夜を迎えるために。
- TW: 為了去迎接新的車輛，為了去迎接新的御一夜。
- old_vn: Để đón những toa xe mới.\nĐể đón một Ohimitera mới.
- fix: Để đón những toa xe mới.\nĐể đón một Ohitoyo mới.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2431** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: （まさか、れいなが――\nいや、しかし。確かに僕が、御一夜を離れるのは難しい）
- TW: （難道，玲奈——不，可是，我確實也難以離開御一夜）
- old_vn: （Không lẽ, Reina――\nKhông, nhưng mà. Đúng là việc tôi rời khỏi Ohimitera rất khó khăn.）
- fix: （Không lẽ, Reina――\nKhông, nhưng mà. Đúng là việc tôi rời khỏi Ohitoyo rất khó khăn.）
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 05_Mayami / `lr真闇追加02_御一夜新婚旅行.txt.toml` — 3 dòng

**Key 1268** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「あらまぁ、ほんならここも御一夜名所」
- TW: 「哎呀，真是這樣的話，那這裡也是御一夜的知名景點了」
- old_vn: "「Ôi chà, vậy ra đây cũng là một danh lam thắng cảnh của Ohimitera.」"
- fix: "「Ôi chà, vậy ra đây cũng là một danh lam thắng cảnh của Ohitoyo.」"
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1368** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「うふふぅ。れいなが御一夜観光するなら、絶対絶対\nレールショップみてみたいって思ったからでぇす」
- TW: 「嘿嘿。因為如果玲奈要觀光御一夜，絕對會想去看看鐵路商店的」
- old_vn: "「Ufufu~. Vì Reina nghĩ nếu đi tham quan Ohimitera, thì nhất định nhất định\nphải ghé xem cửa hàng đường sắt một lần đó nha~」"
- fix: "「Ufufu~. Vì Reina nghĩ nếu đi tham quan Ohitoyo, thì nhất định nhất định\nphải ghé xem cửa hàng đường sắt một lần đó nha~」"
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1884** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 風呂とご飯とキハ07ｓへの乗車と。\nそれらを残すだけとなった、御一夜観光の締めくくり。
- TW: 洗澡，吃飯，乘坐Ｋｉｈａ０７ｓ。做完這些後，這次御一夜旅行就結束了。
- old_vn: "Tắm rửa, ăn uống và lên chuyến tàu Kiha 07S.\nChuyến tham quan Ohimitera chỉ còn lại những việc đó để khép lại."
- fix: "Tắm rửa, ăn uống và lên chuyến tàu Kiha 07S.\nChuyến tham quan Ohitoyo chỉ còn lại những việc đó để khép lại."
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 05_Mayami / `lr真闇追加03_ブルートレインの夜.txt.toml` — 3 dòng

**Key 1044** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜市の魅力はもちろん、真闇姉の魅力についても」
- TW: 「不只是御一夜市的魅力，也包括真闇姐的魅力」
- old_vn: 「Tất nhiên là sức hấp dẫn của thành phố Ohimitera, và cả sức hấp dẫn của chị Mayami nữa」
- fix: 「Tất nhiên là sức hấp dẫn của thành phố Ohitoyo, và cả sức hấp dẫn của chị Mayami nữa」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1381** (nguồn old_vn: audit; "Ohimitera" ×1)
- JP: 「だな。『れいなにとっての御一夜』は、\nまことひだまりのような場所なのだなぁと、僕も感じた」
- TW: 「沒錯。在我的感受中，“玲奈眼裡的御一夜”簡直就像沐浴在溫暖陽光的地方一樣」
- old_vn: 「Đúng vậy. Tôi cũng cảm nhận được rằng, 『Ohimitera trong mắt Reina』,\nquả thực là một nơi ấm áp như ánh nắng mặt trời」
- fix: 「Đúng vậy. Tôi cũng cảm nhận được rằng, 『Ohitoyo trong mắt Reina』,\nquả thực là một nơi ấm áp như ánh nắng mặt trời」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1768** (nguồn old_vn: audit; "Ohimitera" ×1)
- JP: 日々姫の姉で、僕の義姉で――\nだけでなく、御一夜全体の姉であるような気さえする。
- TW: 既是日日姬的姐姐，也是我的義姐——不僅如此，我甚至覺得她還是御一夜全體人員的姐姐。
- old_vn: Là chị gái của Hibiki, là chị nuôi của tôi——\nKhông chỉ vậy, tôi còn có cảm giác chị ấy như là chị lớn của cả Ohimitera này.
- fix: Là chị gái của Hibiki, là chị nuôi của tôi——\nKhông chỉ vậy, tôi còn có cảm giác chị ấy như là chị lớn của cả Ohitoyo này.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 05_Mayami / `真闇01_再蒸留.txt.toml` — 17 dòng

**Key 1035** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「……良くも悪しくも、古い町だからな、御一夜は」
- TW: 「……不論好壞，御一夜骨子裡還是個老城啊」
- old_vn: 「……Dù tốt hay xấu thì Ohimitera vẫn là một thị trấn cổ mà.」
- fix: 「……Dù tốt hay xấu thì Ohitoyo vẫn là một thị trấn cổ mà.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1335** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「良か案と思うよ。良か案やけどねぇ……今の段階では、\n御一夜が埋もれて、素通りされてしまいかねんね」
- TW: 「倒算是個好方案。雖然好……但目前這個階段弄的話，御一夜可能會被忽略吧」
- old_vn: 「Chị nghĩ đó là một ý tưởng hay. Ý tưởng hay nhưng mà……ở giai đoạn này, \nOhimitera có thể sẽ bị lu mờ và bị bỏ qua mất.」
- fix: 「Chị nghĩ đó là một ý tưởng hay. Ý tưởng hay nhưng mà……ở giai đoạn này, \nOhitoyo có thể sẽ bị lu mờ và bị bỏ qua mất.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1376** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「右田は、クマ焼酎の……\n御一夜に昔からあるもんの、いわば代表格よねぇ」
- TW: 「右田可是隈燒酒的……御一夜自古以來的一員，如今也算是代表了吧」
- old_vn: "「Migita, là đại diện cho rượu shochu Kuma……\nhay nói đúng hơn là đại diện cho những giá trị truyền thống của Ohimitera nhỉ.」"
- fix: "「Migita, là đại diện cho rượu shochu Kuma……\nhay nói đúng hơn là đại diện cho những giá trị truyền thống của Ohitoyo nhỉ.」"
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1404** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「ああ――ならば恐らく、御一夜鉄道にポーレットや、\nひょっとするとれいなも関わり始めた年となるのか」
- TW: 「啊——那恐怕就是波萊特，甚至是玲奈開始參與進御一夜鐵路的那一年吧」
- old_vn: 「A——Nếu vậy thì có lẽ, đây là năm mà Paulette, \nvà biết đâu cả Reina cũng bắt đầu tham gia vào Đường sắt Ohimitera nhỉ.」
- fix: 「A——Nếu vậy thì có lẽ, đây là năm mà Paulette, \nvà biết đâu cả Reina cũng bắt đầu tham gia vào Đường sắt Ohitoyo nhỉ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1545** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜は変化を好まぬ町だ。宝生元忠はそれを知ってる。\n\x%lエアクラ;#00ffc040;エアクラ%l;#;誘致の話も当然、好まれぬものであろうとも」
- TW: 「御一夜是個不喜歡變化的城市。寶生元忠深知這一點。而\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶自然也是被排斥的」
- old_vn: 「Ohimitera là một thành phố không thích sự thay đổi. Houshou Mototada biết điều đó. \nChuyện kêu gọi \x%lエアクラ;#00ffc040;Aircra%l;#; tất nhiên cũng sẽ không được hoan nghênh.」
- fix: 「Ohitoyo là một thành phố không thích sự thay đổi. Houshou Mototada biết điều đó. \nChuyện kêu gọi \x%lエアクラ;#00ffc040;Aircra%l;#; tất nhiên cũng sẽ không được hoan nghênh.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1641** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜まわりだけでもこれほど栄えていたものが……\n四十六年には、湯医線だけしか残らんとは」
- TW: 「當年光是御一夜周圍都這麼興盛……但四十六年卻只剩下湯醫線」
- old_vn: 「Chỉ riêng khu vực quanh Ohimitera đã từng sầm uất đến thế này mà…… \nĐến năm 46, lại chỉ còn mỗi Tuyến Yui thôi sao.」
- fix: 「Chỉ riêng khu vực quanh Ohitoyo đã từng sầm uất đến thế này mà…… \nĐến năm 46, lại chỉ còn mỗi Tuyến Yui thôi sao.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1664** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「確かに御一夜はその面でも不利だ。エアクラを使っても、\nアクセスのよい大都市は八ツ城・隈元くらいしか無い」
- TW: 「確實，御一夜在這方面很不利。就算使用空凝機，方便去的大城市也只有八代和隈元而已」
- old_vn: 「Quả thực Ohimitera cũng bất lợi ở điểm đó. Dù có dùng Aircra, \nnhững thành phố lớn dễ tiếp cận cũng chỉ có Yatsushiro và Kumamoto.」
- fix: 「Quả thực Ohitoyo cũng bất lợi ở điểm đó. Dù có dùng Aircra, \nnhững thành phố lớn dễ tiếp cận cũng chỉ có Yatsushiro và Kumamoto.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1745** (nguồn old_vn: audit; "Ohimitera" ×1)
- JP: 「これ……御一夜は、ターミナル駅としての価値以上の、\n観光地としての価値ば持てんかったゆーことよねぇ」
- TW: 「這……也就是說御一夜除擔負\x%lターミナル駅;#00ffc040;總站%l;#;的價值以外，並沒有作為觀光地的價值咯」
- old_vn: 「Cái này……Có nghĩa là Ohimitera không có giá trị nào khác với tư cách là một địa điểm du lịch, \nngoài giá trị của một ga đầu mối nhỉ.」
- fix: 「Cái này……Có nghĩa là Ohitoyo không có giá trị nào khác với tư cách là một địa điểm du lịch, \nngoài giá trị của một ga đầu mối nhỉ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1754** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜市長に[ひない,1]雛衣さん――\nポーちゃんのお父さんが就いた年よね」
- TW: 「這是雛衣先生——小波父親就任御一夜市長的那一年」
- old_vn: 「Đó là năm mà ông Hinai——\nBố của Pau-chan nhậm chức Thị trưởng Ohimitera nhỉ.」
- fix: 「Đó là năm mà ông Hinai——\nBố của Pau-chan nhậm chức Thị trưởng Ohitoyo nhỉ.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1930** (nguồn old_vn: audit; "Ohimitera" ×1)
- JP: 三十七年の\x%l帝鉄;#00ffc040;帝鉄%l;#;路線は、九洲広くを網羅している。\n御一夜から、北は[やつしろ,2]八ツ城を超え[くまもと,1]隈元-[はかた,1]博太、その先へ。
- TW: 三十七年的\x%l帝鉄;#00ffc040;帝國鐵路%l;#;線路幾乎包羅了整個廣袤的九州。從御一夜向北越過八代、隈元及博多，向更遠處延伸。
- old_vn: Tuyến đường sắt \x%l帝鉄;#00ffc040;Teitetsu%l;#; năm 37 bao phủ rộng khắp Kyushu. \nTừ Ohimitera, hướng Bắc vượt qua Yatsushiro đến Kumamoto - Hakata, và xa hơn nữa.
- fix: Tuyến đường sắt \x%l帝鉄;#00ffc040;Teitetsu%l;#; năm 37 bao phủ rộng khắp Kyushu. \nTừ Ohitoyo, hướng Bắc vượt qua Yatsushiro đến Kumamoto - Hakata, và xa hơn nữa.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2149** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 御一夜の衰退は、鉄道中継点としての価値の喪失と一体だ。\nつまり――
- TW: 御一夜的衰退和作為鐵路中繼點的價值的喪失是一體的。也就是說——
- old_vn: Sự suy thoái của Ohimitera gắn liền với việc mất đi giá trị của một điểm trung chuyển đường sắt. \nNói cách khác——
- fix: Sự suy thoái của Ohitoyo gắn liền với việc mất đi giá trị của một điểm trung chuyển đường sắt. \nNói cách khác——
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2152** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: \x%l8620;#00ffc040;8620%l;#;に乗りたい方は、焼酎無しでも来てくれるだろうし\n……この案、肝心の御一夜への上積みがあまり望めない。
- TW: 想乘\x%l8620;#00ffc040;８６２０%l;#;的人就算沒有燒酒也會來……最重要的御一夜本身的地位卻無法靠這個方案得到提升。
- old_vn: Những người muốn đi \x%l8620;#00ffc040;8620%l;#; thì dù không có shochu họ cũng sẽ đến thôi \n……Kế hoạch này, không thể kỳ vọng nhiều vào việc mang lại lợi ích thiết thực cho Ohimitera.
- fix: Những người muốn đi \x%l8620;#00ffc040;8620%l;#; thì dù không có shochu họ cũng sẽ đến thôi \n……Kế hoạch này, không thể kỳ vọng nhiều vào việc mang lại lợi ích thiết thực cho Ohitoyo.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2227** (nguồn old_vn: csv3; "Ohimitera" ×2)
- JP: 年度別の、御一夜市の宿泊観光客数と、\n御一夜駅の利用者数と。
- TW: 數據的內容是按年度匯總的御一夜市住宿遊客數和御一夜車站的客流量。
- old_vn: Số lượng khách du lịch lưu trú tại thành phố Ohimitera theo từng năm, \nvà số lượng người sử dụng ga Ohimitera.
- fix: Số lượng khách du lịch lưu trú tại thành phố Ohitoyo theo từng năm, \nvà số lượng người sử dụng ga Ohitoyo.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2273** (nguồn old_vn: csv3; "Ohimitera" ×2)
- JP: そんな時代を乗り越えて、御一夜駅利用者数も\n御一夜市への宿泊客数とともに堅調に復活し――
- TW: 熬過那個時代後，御一夜車站乘客數和住宿在御一夜的遊客數都堅挺地復活了——
- old_vn: Vượt qua thời đại đó, số lượng người sử dụng ga Ohimitera \ncùng với số lượng khách lưu trú tại thành phố Ohimitera đã phục hồi vững chắc——
- fix: Vượt qua thời đại đó, số lượng người sử dụng ga Ohitoyo \ncùng với số lượng khách lưu trú tại thành phố Ohitoyo đã phục hồi vững chắc——
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2290** (nguồn old_vn: audit; "Ohimitera" ×1)
- JP: まったく、僕は不明であった。\n御一夜はまさしくそういう町だ。
- TW: 真是的，我簡直笨到家了。御一夜不就是這樣一座城市嗎。
- old_vn: Quả thực, tôi đúng là chẳng hiểu gì cả. \nOhimitera chính xác là một thị trấn như vậy.
- fix: Quả thực, tôi đúng là chẳng hiểu gì cả. \nOhitoyo chính xác là một thị trấn như vậy.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2357** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: そして真闇姉こそは、御一夜とそこにある暮らしとを、\n誰より深く、きっと知っている人なのだ。
- TW: 而真闇姐也正是比任何人都清楚御一夜和這裡的生活的人。
- old_vn: Và chị Mayami, chính là người hiểu rõ về Ohimitera và cuộc sống nơi đây \nsâu sắc hơn bất kỳ ai.
- fix: Và chị Mayami, chính là người hiểu rõ về Ohitoyo và cuộc sống nơi đây \nsâu sắc hơn bất kỳ ai.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2380** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: それで本当に御一夜が変わると思っていたなら、\n宝生元忠――僕が思うよりよほど暗愚なのかもしれぬ。
- TW: 要是他覺得真靠這樣就能改變御一夜的話，寶生元忠——說不定就比我想的還要愚蠢。
- old_vn: Nếu ông ta thực sự nghĩ rằng làm vậy sẽ thay đổi được Ohimitera, \nthì Houshou Mototada——có lẽ còn ngu ngốc hơn tôi tưởng.
- fix: Nếu ông ta thực sự nghĩ rằng làm vậy sẽ thay đổi được Ohitoyo, \nthì Houshou Mototada——có lẽ còn ngu ngốc hơn tôi tưởng.
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 05_Mayami / `真闇03_ひとしずく.txt.toml` — 1 dòng

**Key 1928** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「少しどころか、大いにだ。\x%l機関助士;#00ffc040;機関助士%l;#;としてはもちろん、\n御一夜のことを教えてもくれたし――助かってるさ」
- TW: 「豈止是一些，簡直是幫大忙了啊。\x%l機関助士;#00ffc040;司爐%l;#;的工作自不用說，還幫我了解御一夜——真是幫了我特別多」
- old_vn: 「Không chỉ ít nhiều đâu, mà là rất nhiều đấy. Với tư cách là \x%l機関助士;#00ffc040;phụ lái tàu%l;#; thì đã đành,\nem còn dạy anh biết bao điều về Ohimitera nữa―― anh thực sự rất biết ơn em.」
- fix: 「Không chỉ ít nhiều đâu, mà là rất nhiều đấy. Với tư cách là \x%l機関助士;#00ffc040;phụ lái tàu%l;#; thì đã đành,\nem còn dạy anh biết bao điều về Ohitoyo nữa―― anh thực sự rất biết ơn em.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 05_Mayami / `真闇h3_補習授業の廃校舎.txt.toml` — 2 dòng

**Key 1543** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「――御一夜全体の活気も増し、観光客も増えている。\nこの流れを、より活性化させたいという計画だろうな」
- TW: 「――御一夜整體活力大增，遊客也增加了。而這個計劃，是為了讓這裡變得更有生氣吧」
- old_vn: 「――Sức sống của toàn bộ Ohimitera cũng tăng lên, lượng khách du lịch cũng tăng theo.\nChắc hẳn đây là kế hoạch nhằm thúc đẩy luồng sinh khí này thêm phần sôi động.」
- fix: 「――Sức sống của toàn bộ Ohitoyo cũng tăng lên, lượng khách du lịch cũng tăng theo.\nChắc hẳn đây là kế hoạch nhằm thúc đẩy luồng sinh khí này thêm phần sôi động.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 2524** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「御一夜市と御一夜鉄道とのさらなる発展に繋がる\n可能性のあることだからな。無論、快諾した」
- TW: 「御一夜市和御一夜鐵道都可能因此有進一步的發展，所以我答應了」
- old_vn: 「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohimitera và Đường sắt Ohito mà.\nTất nhiên là tôi đã vui vẻ nhận lời.」
- fix: 「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohitoyo và Đường sắt Ohito mà.\nTất nhiên là tôi đã vui vẻ nhận lời.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

### 06_Kisaki / `lr稀咲追加03_新事業案.txt.toml` — 4 dòng

**Key 1130** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「そっか。加工品も考えたら、10や20、御一夜・クマ\nでも特産品は用意できるかも――うん、なら継続性も」
- TW: 「對啊，算上加工品的話，御一夜和隈元大概能拿得出十幾二十樣特產的——嗯，這樣一來短時間內就不用愁了」
- old_vn: 「Vậy sao. Nếu tính cả các sản phẩm chế biến, thì Ohimitera và Kuma\nchắc cũng chuẩn bị được 10 hay 20 loại đặc sản đấy――Ừm, thế thì tính liên tục cũng」
- fix: 「Vậy sao. Nếu tính cả các sản phẩm chế biến, thì Ohitoyo và Kuma\nchắc cũng chuẩn bị được 10 hay 20 loại đặc sản đấy――Ừm, thế thì tính liên tục cũng」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1186** (nguồn old_vn: csv3; "Ohimitera" ×2)
- JP: 「御一夜鉄道。地域としては御一夜・クマの代表として、\nハチロクがランに、グッズの売上勝負を挑む」
- TW: 「我們御一夜鐵路可以代表御一夜乃至整個隈元，讓八六就相關周邊的銷售額與蘭一決勝負」
- old_vn: 「Đường sắt Ohimitera. Với tư cách là đại diện của khu vực Ohimitera và Kuma,\nHachiroku sẽ thách đấu doanh số bán sản phẩm với Ran.」
- fix: 「Đường sắt Ohitoyo. Với tư cách là đại diện của khu vực Ohitoyo và Kuma,\nHachiroku sẽ thách đấu doanh số bán sản phẩm với Ran.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1267** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「うむ……御一夜鉄道と縁が一番深いとなると、\n現状では肥薩みかん鉄道となるが――どうだろう」
- TW: 「沒錯……目前和我們御一夜鐵路交情最深的，就是肥薩的橙鐵路了——他們會認可嗎？」
- old_vn: 「Ừm……Nếu nói về nơi có mối liên hệ sâu sắc nhất với Đường sắt Ohimitera,\nthì hiện tại là Đường sắt Hisatsu Mikan——nhưng không biết thế nào.」
- fix: 「Ừm……Nếu nói về nơi có mối liên hệ sâu sắc nhất với Đường sắt Ohitoyo,\nthì hiện tại là Đường sắt Hisatsu Mikan——nhưng không biết thế nào.」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

**Key 1412** (nguồn old_vn: csv3; "Ohimitera" ×1)
- JP: 「単純な話。特産品の数。そっち方面は詳しくないけど、例えば御一夜でキャラクターグッズ化できる特産品って」
- TW: 「道理很簡單，就是特產的數量有限，儘管我對這方面並不了解，比如我們御一夜，能有多少可以設計周邊的特產？」
- old_vn: 「Chuyện đơn giản thôi. Số lượng đặc sản. Tôi không rành về mảng đó lắm, nhưng ví dụ ở Ohimitera, những đặc sản có thể làm thành sản phẩm nhân vật là gì?」
- fix: 「Chuyện đơn giản thôi. Số lượng đặc sản. Tôi không rành về mảng đó lắm, nhưng ví dụ ở Ohitoyo, những đặc sản có thể làm thành sản phẩm nhân vật là gì?」
- Lý do: JP có 御一夜 → "Ohimitera" sai, đổi thành "Ohitoyo" (T1, đã chốt 19/11).

## 4. Đã kiểm tra và KHÔNG sửa (kept / flagged)

- **0 dòng flag misalignment:** không có ứng viên nào JP thiếu 御一夜. Mọi dòng "Ohimitera" trong 4 folder đều ứng với 御一夜 thật trong JP — không có dòng nào là lỗi lệch dòng hay nhiễm chéo.
- **216 dòng đã sửa sẵn trong audit (không đụng):** CSV3 VN có "Ohimitera" nhưng giá trị hiện tại đã là "Ohitoyo" — tập trung ở `稀咲03_純白のレール.txt.toml` (1906, 2704, 2903, 1882, 2513, 2891, 1657) và `稀咲h3_チャイナドレスでおもてなし.txt.toml` (2648, 3099, 2740, 2302) cùng các file khác trong 4 folder. Không ghi lại vào JSON (chỉ ghi dòng mình đổi).
- **0 dòng "Ohimitera" trong gloss %l:** kiểm chứng máy — mọi lần xuất hiện đều là display text; không có thẻ gloss nào chứa dạng cũ.

## 5. Ghi chú ranh giới với các mục khác (để batch sau không sửa trùng / không bỏ sót)

- **"Đường sắt Ohimitera" → "Đường sắt Ohitoyo" (4 dòng: ポーレットh3 1255, 真闇01 1404, lr稀咲追加03 1186, 1267):** dạng cũ trong các dòng này là "Đường sắt Ohimitera" (chứa "Ohimitera"), nên phép đổi T1 cho ra đúng dạng đích của T2 ("Đường sắt Ohitoyo"). Sau đợt này 4 dòng này đã ĐÚNG HOÀN TOÀN — **batch T2 phải bỏ qua** (giá trị hiện tại không còn "Đường sắt Ohito" đứng riêng). Lưu ý kỹ thuật: chuỗi con "Đường sắt Ohito" vẫn xuất hiện trong "Đường sắt Ohitoyo" theo nghĩa chuỗi — T2 phải khớp dạng đứng riêng `Đường sắt Ohito(?!yo)`, không đếm chuỗi con.
- **真闇h3 2524 — dòng duy nhất JP có 御一夜 ×2 nhưng fix chỉ 1 "Ohitoyo":** JP 「御一夜市と御一夜鉄道」; old_vn dịch 御一夜市 → "thành phố Ohimitera" (đã sửa → "thành phố Ohitoyo") và 御一夜鉄道 → "Đường sắt Ohito" (dạng T2, GIỮ NGUYÊN chờ batch T2). Đây là hành vi đúng, không phải thiếu sót — đã kiểm chứng trong đợt kiểm tra thứ hai.
- **ポーレット04 1517 — giữ "Jutsu-sen":** fix chỉ đổi "Ohimitera"→"Ohitoyo"; "Jutsu-sen" trong cùng dòng thuộc T17, batch T17 xử lý.
- **真闇01 1641 — giữ "Tuyến Yui":** fix chỉ đổi "Ohimitera"→"Ohitoyo"; "Tuyến Yui" (湯医線) thuộc T7, batch T7 xử lý.
- **ポーレット04 2809 — TW lệch JP:** TW ghi "雖然只是暫時的工作……" (không có 御一夜, có vẻ là dòng khác), nhưng JP rõ ràng 「僕とて、御一夜の――」 và old_vn khớp JP. JP thắng TW — fix vẫn áp dụng. Ghi lại để batch sau không hoang mang vì TW.
- **Dấu ngoặc kép thừa quanh giá trị (4 dòng: lr真闇追加02 1268/1368/1884, 真闇01 1376):** giá trị CSV3 VN của các dòng này có sẵn ký tự `"` bao quanh toàn bộ câu (vd. `"「Ôi chà, …」"`). Đây là trạng thái có sẵn, KHÔNG phải do đợt này thêm — fix chỉ đổi thuật ngữ, giữ nguyên dấu ngoặc. Không sửa trong đợt này (ngoài phạm vi T1).
- **5 dòng old_vn từ audit fix (không phải CSV3):** lr真闇追加03 1381/1768, 真闇01 1745/1930/2290 — old_vn trong JSON là giá trị fix của audit (đã kiểm chứng khớp file audit), fix T1 áp lên trên giá trị đó. Các dòng này có thẻ %l đã đúng (1930: gloss 帝鉄→"Teitetsu") — thẻ không đụng tới.

## 6. Quyết định (decisions)

- Không có mục OPEN trong đợt này: T1 là DECIDED (Hieu, 19/11). Không có phán đoán nào cần quyết thêm — mọi ứng viên đều thỏa điều kiện JP-chứa-御一夜.

## 7. Đợt kiểm tra thứ hai (second pass)

Đọc lại toàn bộ 52 fix đối chiếu JP (đọc lại bằng mắt từng dòng, không chỉ parse-check), cộng kiểm chứng máy:

- **Tổng số fix đọc lại: 52 / 52 xác nhận đúng / 0 loại bỏ / 0 sửa lại.**
- Kiểm chứng máy: fix khác old_vn CHỈ ở phép đổi "Ohimitera"→"Ohitoyo" (52/52); "Ohimitera" không còn trong bất kỳ fix nào (52/52); số lần "Ohitoyo" trong fix = số lần "Ohimitera" trong old_vn (52/52).
- Đối chiếu số lượng JP↔fix: số lần 御一夜 trong JP = số lần "Ohitoyo" trong fix ở 51/52 dòng; dòng duy nhất lệch là 真闇h3 2524 (JP ×2, fix ×1) — đã điều tra: lần 御一夜 thứ hai là 御一夜鉄道, old_vn dịch bằng dạng T2 "Đường sắt Ohito", giữ nguyên đúng quy tắc ranh giới (§5). Không sửa lại dòng này.
- Parse-check KHÔNG thay thế đợt đọc lại này: khối TOML dưới đây parse được bằng tomllib (12 file, 52 key, giá trị khớp JSON từng key), nhưng tính đúng đắn của từng fix đã được xác nhận bằng đợt đọc lại đối chiếu JP ở trên.

## 8. Khối TOML để dán vào file (đã kiểm chứng parse được)

Mỗi khối dán vào section `[script]` của file tương ứng (ghi đè đúng các key liệt kê, giữ nguyên mọi key khác). Fix áp cho CẢ HAI bản sao nếu file thuộc nhóm trùng lặp (rebuild áp theo basename).

### 03_Paulette / `ポーレット03_廃炭鉱.txt.toml` — 3 key

```toml
[script]
1368 = "「……Những người luôn sống ở Ohitoyo,\\nchắc chắn phải biết đến cảnh tượng này chứ——vậy mà tại sao.」"
2084 = "「Nếu có thể biến thành tài nguyên thì không còn gì bằng…… nhưng trong trường hợp không thể,\\nthì khu mỏ bỏ hoang này, sẽ mang đến rắc rối lớn cho Ohitoyo.」"
2892 = "Quá khứ này, những dấu tích này.\\nCũng có thể coi là tấm gương phản chiếu tương lai của Ohitoyo."
```

### 03_Paulette / `ポーレット04_ヒヤリング.txt.toml` — 5 key

```toml
[script]
1517 = "「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsu-sen với chấn hưng du lịch,\\nthì Ohitoyo chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」"
1557 = "「Đầu giờ sáng của tòa thị chính Ohitoyo là,\\n8 giờ 30 phút sáng ạ.」"
1636 = "「Vậy sao. Chào cậu, cậu Migita.\\nTôi là Miyamoto, Trưởng phòng Tổng vụ của Tòa thị chính Ohitoyo.」"
2230 = "Đường sắt đã bị bỏ hoang từ lâu,\\nnhờ vậy mà tôi mới có thể an tâm sinh sống ở thị trấn Ohitoyo này."
2504 = "Mái tóc vàng tung bay trong cơn gió vẫn chưa dứt.\\nĐôi mắt màu xanh thẳm. Một màu xanh trong trẻo hơn cả bầu trời Ohitoyo, hơn cả dòng sông Kuma."
```

### 03_Paulette / `ポーレット04_鳴呼いきストーブ列車.txt.toml` — 1 key

```toml
[script]
2809 = "Tôi cũng là một người của Ohitoyo——"
```

### 03_Paulette / `ポーレットh3_誘惑アイスコーヒー.txt.toml` — 2 key

```toml
[script]
1255 = "Nhận được thông báo về các câu hỏi liên quan, chúng tôi đã vội vàng tìm kiếm,\\nnhưng cả trong Tòa thị chính lẫn Đường sắt Ohitoyo đều không có."
1347 = "Dữ liệu thống kê về số lượng tàu chở hàng đến và đi tại ga Ohitoyo,\\ncùng với tổng khối lượng vận chuyển của chúng."
```

### 04_Reina / `lrれいな追加03_れいなとのレール.txt.toml` — 4 key

```toml
[script]
675 = "「……Vì thế nên Reina mới thích\\nnhững buổi hẹn hò tham quan quanh Ohitoyo đến vậy nhỉ.」"
981 = "「Nhưng mà, khi đến Ohitoyo, gặp được chị Paulette thì.\\nThế giới của Reina đã mở rộng ra trên rất nhiều tuyến đường sắt khác nhau nha~」"
1182 = "「Ohitoyo vừa đẹp vừa vui, hơn nữa được anh Soutetsu\\nchỉ cho nhiều thứ cũng làm Reina vui lắm nha~」"
1578 = "Các điểm du lịch ở Ohitoyo giờ đây giống như khu vườn nhà tôi vậy.\\nTất nhiên tôi có thể giải thích cặn kẽ, và Reina cũng sẽ rất vui."
```

### 04_Reina / `れいな03_しゅっぱつしんこう.txt.toml` — 7 key

```toml
[script]
1300 = "「Không đâu, Reina. Vẫn chưa thể đến mức đó được.\\nTừ Ohitoyo, ưu tiên hàng đầu là khôi phục tuyến đường đến Yatsushiro.」"
1337 = "「Đường ray,\\nsẽ được nối từ Ohitoyo đến tận đó luôn ạ?」"
1455 = "「Vâng ạ. Vì sẽ không còn chuyện tất cả các \\x%l列車;#00ffc040;tàu%l;#; đều trở về Ohitoyo\\nđể kết thúc một ngày như trước đây nữa.」"
1474 = "「Ừ. Chị đang trong tình cảnh không thể rời khỏi Ohitoyo được.」"
2160 = "Tôi bị trói buộc ở Ohitoyo, còn Reina bị đưa đến Yahata.\\nKhoảng thời gian chúng tôi có thể ở bên nhau sẽ bị xé nát, bị phá hủy."
2223 = "Để đón những toa xe mới.\\nĐể đón một Ohitoyo mới."
2431 = "（Không lẽ, Reina――\\nKhông, nhưng mà. Đúng là việc tôi rời khỏi Ohitoyo rất khó khăn.）"
```

### 05_Mayami / `lr真闇追加02_御一夜新婚旅行.txt.toml` — 3 key

```toml
[script]
1268 = "\"「Ôi chà, vậy ra đây cũng là một danh lam thắng cảnh của Ohitoyo.」\""
1368 = "\"「Ufufu~. Vì Reina nghĩ nếu đi tham quan Ohitoyo, thì nhất định nhất định\\nphải ghé xem cửa hàng đường sắt một lần đó nha~」\""
1884 = "\"Tắm rửa, ăn uống và lên chuyến tàu Kiha 07S.\\nChuyến tham quan Ohitoyo chỉ còn lại những việc đó để khép lại.\""
```

### 05_Mayami / `lr真闇追加03_ブルートレインの夜.txt.toml` — 3 key

```toml
[script]
1044 = "「Tất nhiên là sức hấp dẫn của thành phố Ohitoyo, và cả sức hấp dẫn của chị Mayami nữa」"
1381 = "「Đúng vậy. Tôi cũng cảm nhận được rằng, 『Ohitoyo trong mắt Reina』,\\nquả thực là một nơi ấm áp như ánh nắng mặt trời」"
1768 = "Là chị gái của Hibiki, là chị nuôi của tôi——\\nKhông chỉ vậy, tôi còn có cảm giác chị ấy như là chị lớn của cả Ohitoyo này."
```

### 05_Mayami / `真闇01_再蒸留.txt.toml` — 17 key

```toml
[script]
1035 = "「……Dù tốt hay xấu thì Ohitoyo vẫn là một thị trấn cổ mà.」"
1335 = "「Chị nghĩ đó là một ý tưởng hay. Ý tưởng hay nhưng mà……ở giai đoạn này, \\nOhitoyo có thể sẽ bị lu mờ và bị bỏ qua mất.」"
1376 = "\"「Migita, là đại diện cho rượu shochu Kuma……\\nhay nói đúng hơn là đại diện cho những giá trị truyền thống của Ohitoyo nhỉ.」\""
1404 = "「A——Nếu vậy thì có lẽ, đây là năm mà Paulette, \\nvà biết đâu cả Reina cũng bắt đầu tham gia vào Đường sắt Ohitoyo nhỉ.」"
1545 = "「Ohitoyo là một thành phố không thích sự thay đổi. Houshou Mototada biết điều đó. \\nChuyện kêu gọi \\x%lエアクラ;#00ffc040;Aircra%l;#; tất nhiên cũng sẽ không được hoan nghênh.」"
1641 = "「Chỉ riêng khu vực quanh Ohitoyo đã từng sầm uất đến thế này mà…… \\nĐến năm 46, lại chỉ còn mỗi Tuyến Yui thôi sao.」"
1664 = "「Quả thực Ohitoyo cũng bất lợi ở điểm đó. Dù có dùng Aircra, \\nnhững thành phố lớn dễ tiếp cận cũng chỉ có Yatsushiro và Kumamoto.」"
1745 = "「Cái này……Có nghĩa là Ohitoyo không có giá trị nào khác với tư cách là một địa điểm du lịch, \\nngoài giá trị của một ga đầu mối nhỉ.」"
1754 = "「Đó là năm mà ông Hinai——\\nBố của Pau-chan nhậm chức Thị trưởng Ohitoyo nhỉ.」"
1930 = "Tuyến đường sắt \\x%l帝鉄;#00ffc040;Teitetsu%l;#; năm 37 bao phủ rộng khắp Kyushu. \\nTừ Ohitoyo, hướng Bắc vượt qua Yatsushiro đến Kumamoto - Hakata, và xa hơn nữa."
2149 = "Sự suy thoái của Ohitoyo gắn liền với việc mất đi giá trị của một điểm trung chuyển đường sắt. \\nNói cách khác——"
2152 = "Những người muốn đi \\x%l8620;#00ffc040;8620%l;#; thì dù không có shochu họ cũng sẽ đến thôi \\n……Kế hoạch này, không thể kỳ vọng nhiều vào việc mang lại lợi ích thiết thực cho Ohitoyo."
2227 = "Số lượng khách du lịch lưu trú tại thành phố Ohitoyo theo từng năm, \\nvà số lượng người sử dụng ga Ohitoyo."
2273 = "Vượt qua thời đại đó, số lượng người sử dụng ga Ohitoyo \\ncùng với số lượng khách lưu trú tại thành phố Ohitoyo đã phục hồi vững chắc——"
2290 = "Quả thực, tôi đúng là chẳng hiểu gì cả. \\nOhitoyo chính xác là một thị trấn như vậy."
2357 = "Và chị Mayami, chính là người hiểu rõ về Ohitoyo và cuộc sống nơi đây \\nsâu sắc hơn bất kỳ ai."
2380 = "Nếu ông ta thực sự nghĩ rằng làm vậy sẽ thay đổi được Ohitoyo, \\nthì Houshou Mototada——có lẽ còn ngu ngốc hơn tôi tưởng."
```

### 05_Mayami / `真闇03_ひとしずく.txt.toml` — 1 key

```toml
[script]
1928 = "「Không chỉ ít nhiều đâu, mà là rất nhiều đấy. Với tư cách là \\x%l機関助士;#00ffc040;phụ lái tàu%l;#; thì đã đành,\\nem còn dạy anh biết bao điều về Ohitoyo nữa―― anh thực sự rất biết ơn em.」"
```

### 05_Mayami / `真闇h3_補習授業の廃校舎.txt.toml` — 2 key

```toml
[script]
1543 = "「――Sức sống của toàn bộ Ohitoyo cũng tăng lên, lượng khách du lịch cũng tăng theo.\\nChắc hẳn đây là kế hoạch nhằm thúc đẩy luồng sinh khí này thêm phần sôi động.」"
2524 = "「Bởi vì chuyện này có khả năng dẫn đến sự phát triển xa hơn nữa của thành phố Ohitoyo và Đường sắt Ohito mà.\\nTất nhiên là tôi đã vui vẻ nhận lời.」"
```

### 06_Kisaki / `lr稀咲追加03_新事業案.txt.toml` — 4 key

```toml
[script]
1130 = "「Vậy sao. Nếu tính cả các sản phẩm chế biến, thì Ohitoyo và Kuma\\nchắc cũng chuẩn bị được 10 hay 20 loại đặc sản đấy――Ừm, thế thì tính liên tục cũng」"
1186 = "「Đường sắt Ohitoyo. Với tư cách là đại diện của khu vực Ohitoyo và Kuma,\\nHachiroku sẽ thách đấu doanh số bán sản phẩm với Ran.」"
1267 = "「Ừm……Nếu nói về nơi có mối liên hệ sâu sắc nhất với Đường sắt Ohitoyo,\\nthì hiện tại là Đường sắt Hisatsu Mikan——nhưng không biết thế nào.」"
1412 = "「Chuyện đơn giản thôi. Số lượng đặc sản. Tôi không rành về mảng đó lắm, nhưng ví dụ ở Ohitoyo, những đặc sản có thể làm thành sản phẩm nhân vật là gì?」"
```

## Kết bài

Đợt U1b sửa **52 dòng "Ohimitera" → "Ohitoyo"** trong 12 file của 4 folder Paulette/Reina/Mayami/Kisaki (T1, đã chốt 19/11). Cả 52 dòng đều đã đọc JP (+TW) và xác nhận JP chứa 御一夜 — 0 dòng flag misalignment, 0 dòng loại bỏ ở đợt kiểm tra thứ hai. 216 dòng "Ohimitera" khác trong 4 folder đã sửa sẵn từ audit nên không đụng tới. Ranh giới đã ghi rõ cho batch sau: 4 dòng "Đường sắt Ohimitera" nay đã đúng dạng đích nên T2 bỏ qua; 真闇h3 2524 còn 1 "Đường sắt Ohito" chờ T2; ポーレット04 1517 còn "Jutsu-sen" chờ T17; 真闇01 1641 còn "Tuyến Yui" chờ T7. Đếm lại toàn dự án: sau đợt này T1 còn **259 dòng** (từ 311 dòng giá trị hiện tại còn "Ohimitera", thấp hơn ước lượng 333 của §0 — §0 tính từ map audit cũ 9.190 cặp, đợt này map được 9.200 cặp + toàn bộ moan). Khối TOML 12 file / 52 key đã kiểm chứng parse được bằng tomllib, giá trị khớp JSON.
