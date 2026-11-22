# Unification REVIEW — T1 "Ohimitera" → "Ohitoyo", folders 07–11 (batch U1c)

Mục T1 (§1 UNIFICATION-LIST.md): 御一夜 → "Ohitoyo" — DECIDED 19/11, Hieu. Phạm vi đợt này: **chỉ các thư mục CSV3 07_Nagi_Fukami, 08_Niiroku, 09_Grand, 10_Chikuni, 11_Other**. Các thư mục còn lại của T1 thuộc batch khác.

## Phạm vi

- Item: **T1** (1 mục, làm một phần — folders 07–11; T1 toàn dự án: §0 ước lượng remainder 333, đợt U1b đếm lại giá trị hiện tại còn "Ohimitera" là 311 toàn dự án và đã gộp 52 dòng folders 03–06 vào 22/11 ~11:10 — xem ROUTE-UNIFICATION.md. Cơ sở tổng lúc viết snippet: **1 mục / 52 dòng** (đã rebase, xem file snippet).)
- **Lưu ý rebase:** lúc bắt đầu đợt này (22/11 ~11:04) ROUTE-UNIFICATION.md đang ở 0 mục / 0 dòng; trong lúc làm, đợt U1b (T1, folders 03–06, 52 dòng) đã được gộp (~11:10). Mọi con số tổng trong file này đã đối chiếu lại với ROUTE-UNIFICATION.md hiện tại, không dùng base lúc spawn.
- Files có fix trong đợt này (5 file, 38 dòng):
  - `グランドリライト01_オール御一夜、成立ならず.txt.toml` — 19 dòng: 1612, 2181, 2244, 2277, 2349, 2366, 2408, 2418, 2434, 2524, 2582, 2762, 2869, 3034, 3278, 3481, 3577, 3648, 3936
  - `グランドリライト09_凪.txt.toml` — 2 dòng: 2507, 2738
  - `グランドリライト11_ナインスターズ！.txt.toml` — 12 dòng: 1598, 2157, 2485, 2570, 2578, 2700, 2845, 3414, 3524, 3806, 3915, 3916
  - `凪ふかみ02_命の重さ.txt.toml` — 2 dòng: 960, 2168
  - `凪ふかみ05_凪の開眼！？.txt.toml` — 3 dòng: 2266, 2367, 3222
- Folders 08_Niiroku, 10_Chikuni, 11_Other: **0 dòng** còn lại trong đợt này (mọi occurrence đã sửa hết trong audit — xem đối chiếu bên dưới).

## Phương pháp

1. **Nguồn:** CSV3 good-set 87.833 dòng (91.731 dòng − 3.898 dòng stale của 10 file dual-set, theo `dual-csv-sets.md`; đã kiểm chứng lại bằng script: tổng good-set đúng 87.833). Trong đó 18.246 dòng thuộc 5 folders 07–11 (07: 9.134; 08: 1.801; 09: 2.178; 10: 2.890; 11: 2.243).
2. **Current value** theo đúng quy ước brief: moan fix > audit fix > CSV3 VN. Đã load TOÀN BỘ fix lists: 217 file `audit-*-wrong.json` (9.245 entries) + 66 file `moans/moan-*-wrong.json` (1.535 entries, gồm supplement ハチロクh3). Hai lưu ý khi load:
   - `audit-obasan-wrong.json` bị LOẠI khỏi fix-map: trường `vn` của nó là giá trị SAI (bản dịch lệch vị trí), không phải fix; fix thật nằm ở `audit-paulette03-obasan-wrong.json` (file này thuộc folder 03, ngoài phạm vi đợt này nên việc loại không ảnh hưởng kết quả).
   - `audit-lr-nagih2-wrong.json` dạng dict key→fix (không có JP): resolve basename qua dòng `File:` trong REVIEW kèm theo.
   - 3 collisions còn lại giữa 2 file moan ハチロクh3 (orphan 23 entries vs merged 24 entries, keys 1029/1063/1677) đều thuộc folder 01, ngoài phạm vi — không ảnh hưởng; file merged được ưu tiên.
3. **Liệt kê:** trong 5 folders, CSV3 VN chứa "Ohimitera" ở **91 dòng**. Đối chiếu current value: **53 dòng đã sửa trong audit** (không còn Ohimitera) → còn lại **38 dòng ứng viên**, tất cả đều có current value = CSV3 VN (0 fix value nào còn chứa Ohimitera).
4. **Kiểm từng dòng:** đọc JP (+TW) của cả 38 ứng viên. JP chứa 御一夜 ở **38/38** → sửa tất cả. Không có dòng nào JP thiếu 御一夜 (0 flag loại này). Không có "Ohimitera" nào nằm trong gloss %l (0 dòng); các tag %l giữ nguyên, JP trong tag không đụng.
5. **Đối chiếu với ước lượng §0:** parent ước ~110 dòng cho 5 folders này; thực tế **38 dòng**. Chênh lệch vì phần lớn đã sửa trong audit (53/91). Theo đếm lại của đợt U1b: giá trị hiện tại toàn dự án còn "Ohimitera" là 311 dòng (so với ước lượng §0 là 333); sau U1b còn 259, sau đợt này còn **221 dòng** ở các folder còn lại của T1 (00–02).

### Đối chiếu theo folder (CSV3 VN có "Ohimitera" → đã sửa trong audit → còn lại đợt này)

| Folder | CSV3 VN có Ohimitera | Đã sửa trong audit | Còn lại (đợt này) |
|---|---|---|---|
| 07_Nagi_Fukami | 15 | 8 | **7** |
| 08_Niiroku | 5 | 5 | **0** |
| 09_Grand | 56 | 25 | **31** |
| 10_Chikuni | 15 | 15 | **0** |
| 11_Other | 0 | 0 | **0** |
| **Tổng** | **91** | **53** | **38** |

53 dòng "đã sửa trong audit" chia làm 2 loại (đã kiểm chứng từng dòng): 29 dòng sửa trực tiếp Ohimitera→Ohitoyo (JP có 御一夜, current value có Ohitoyo); 24 dòng được audit dịch mới toàn bộ từ JP mà JP KHÔNG có 御一夜 (CSV3 VN lệch hàng — bản dịch của dòng khác — nên current value đúng là không có dạng Ohitoyo nào). 0 dòng trong nhóm này có JP chứa 御一夜 mà current value thiếu Ohitoyo.

## Các dòng sửa (38 dòng — fix = old_vn chỉ đổi "Ohimitera" → "Ohitoyo")

Lý do chung mọi dòng: JP chứa 御一夜 (hoặc 御一夜鉄道); 御一夜 = "Ohitoyo" theo quyết định 19/11 của Hieu; dạng cũ "Ohimitera" sai. Ghi chú riêng từng dòng (nếu có) nằm ngay dưới bảng của file đó.

### グランドリライト01_オール御一夜、成立ならず.txt.toml (19 dòng)

| Key | JP | TW | old_vn | fix |
|---|---|---|---|---|
| 1612 | 「……御一夜銀行も、\nこの復線買収をすでに検討していたのですか？」 | 「……難道說御一夜銀行已經研究過了收購廢線的可行性嗎？」 | 「……Ngân hàng Ohimitera cũng,\nđã xem xét việc mua lại để phục hồi tuyến đường này rồi sao?」 | 「……Ngân hàng Ohitoyo cũng,\nđã xem xét việc mua lại để phục hồi tuyến đường này rồi sao?」 |
| 2181 | 「今回の試験走行までで、御一夜のキーマンが何人も、\n双鉄くんを信頼してくれたと思いますし、その人脈も」 | 「到這次的行駛測試為止，雙鐵君已經獲得了好幾位御一夜大人物相當的信任了，可以利用這些人脈」 | 「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohimitera,\ntin tưởng cậu Soutetsu, và cả những mối quan hệ đó nữa.」 | 「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohitoyo,\ntin tưởng cậu Soutetsu, và cả những mối quan hệ đó nữa.」 |
| 2244 | 「繋げるための初めの一歩。\n御一夜－八ツ城間復線のハードルが、あまりに高い」 | 「可是恢復廢線的第一步——也就是御一夜和八代之間的線路恢復難度太高了」 | 「Bước đầu tiên để kết nối lại.\nRào cản cho việc phục hồi tuyến đường giữa Ohimitera - Yatsushiro, là quá cao.」 | 「Bước đầu tiên để kết nối lại.\nRào cản cho việc phục hồi tuyến đường giữa Ohitoyo - Yatsushiro, là quá cao.」 |
| 2277 | 「御一夜の郷土史関係の本とか、\nここに置いておくんでよかと？」 | 「和御一夜當地歷史有關的書就都擱這裡了」 | 「Sách liên quan đến lịch sử địa phương của Ohimitera,\nđể ở đây là được đúng không?」 | 「Sách liên quan đến lịch sử địa phương của Ohitoyo,\nđể ở đây là được đúng không?」 |
| 2349 | 「うん。僕が作りたいのは、各々の利害を超えた、\nいわば、オール御一夜の体制だ」 | 「嗯。我想創造的是能超越各方利害關係、讓御一夜團結一致的體制」 | 「Ừm. Thứ tôi muốn tạo ra là một thể chế vượt qua lợi ích của từng cá nhân,\ncó thể gọi là thể chế All Ohimitera.」 | 「Ừm. Thứ tôi muốn tạo ra là một thể chế vượt qua lợi ích của từng cá nhân,\ncó thể gọi là thể chế All Ohitoyo.」 |
| 2366 | 「うむ。オール御一夜体制を築くための、土台。\nその素案は、誰の色を交えてもきっと、成り立たぬ」 | 「嗯，這是構建全御一夜體制的基石。我認為，這基石一定得是純色的，不能混進其他人的顏色」 | 「Ừm. Nền tảng để xây dựng thể chế All Ohimitera.\nBản nháp đó, nếu pha trộn màu sắc của bất kỳ ai thì chắc chắn, sẽ không thành lập được.」 | 「Ừm. Nền tảng để xây dựng thể chế All Ohitoyo.\nBản nháp đó, nếu pha trộn màu sắc của bất kỳ ai thì chắc chắn, sẽ không thành lập được.」 |
| 2408 | 「よかろう、御一夜支店長。業務命令だ。\n右田双鉄氏をサポートし、本件提案の可否を見極めろ」 | 「好吧。那御一夜支行行長，你就協助右田雙鐵，徹底查清這次提案的可行性。這是公司命令」 | 「Được thôi, Giám đốc chi nhánh Ohimitera. Đây là mệnh lệnh công việc.\nHãy hỗ trợ cậu Migita Soutetsu, và xem xét tính khả thi của đề xuất này.」 | 「Được thôi, Giám đốc chi nhánh Ohitoyo. Đây là mệnh lệnh công việc.\nHãy hỗ trợ cậu Migita Soutetsu, và xem xét tính khả thi của đề xuất này.」 |
| 2418 | 「御一夜のことをもっと知ったほうがいいと思うの。\n兄さんが、この町を本当に復興させたいんなら」 | 「如果哥哥真的想讓御一夜復興，我覺得需要更加了解這座城鎮」 | 「Em nghĩ anh nên tìm hiểu thêm về Ohimitera.\nNếu anh thực sự muốn phục hưng thị trấn này.」 | 「Em nghĩ anh nên tìm hiểu thêm về Ohitoyo.\nNếu anh thực sự muốn phục hưng thị trấn này.」 |
| 2434 | 「実際、僕らは、\nそして御一夜は、厳しい状況に置かれていますが」 | 「實際上，我們——御一夜現在就是處於危險的狀態」 | 「Thực tế thì, chúng tôi,\nvà cả Ohimitera, đang bị đặt vào một tình thế nghiêm trọng mà.」 | 「Thực tế thì, chúng tôi,\nvà cả Ohitoyo, đang bị đặt vào một tình thế nghiêm trọng mà.」 |
| 2524 | 「御一夜支店長として“も”の、他に――\nいったい、どのようなお立場で」 | 「您說作為御一夜支行行長倒是“也”很想參與這個計劃，那除此之外您還有別的身份想要參加嗎」 | 「Ngoài việc “cũng” với tư cách là Giám đốc chi nhánh Ohimitera ra——\nrốt cuộc, cô đứng ở lập trường nào」 | 「Ngoài việc “cũng” với tư cách là Giám đốc chi nhánh Ohitoyo ra——\nrốt cuộc, cô đứng ở lập trường nào」 |
| 2582 | 「御一夜支店長としても、計画に噛んでおきたくは思う。\n放置するには、惜しい――と同時に、危険な案だから」 | 「我作為御一夜支行行長倒是也很想參與這個計劃。如果就這麼擱置的話太可惜了——雖然這是個危險的賭博」 | 「Ngay cả với tư cách là Giám đốc chi nhánh Ohimitera, cháu cũng muốn tham gia vào kế hoạch này.\nVì nếu bỏ mặc thì thật đáng tiếc——đồng thời, đây cũng là một phương án nguy hiểm.」 | 「Ngay cả với tư cách là Giám đốc chi nhánh Ohitoyo, cháu cũng muốn tham gia vào kế hoạch này.\nVì nếu bỏ mặc thì thật đáng tiếc——đồng thời, đây cũng là một phương án nguy hiểm.」 |
| 2762 | 「そのとおりだ。ゆえ、オール御一夜を描くためには、\n土台が真っ白であることが必須となるかと思うのだ」 | 「沒錯。所以我認為全御一夜體制的基石必須是純白的」 | 「Đúng là vậy. Do đó, để vẽ nên bức tranh All Ohimitera,\ntôi nghĩ việc nền tảng phải hoàn toàn trắng tinh là điều bắt buộc.」 | 「Đúng là vậy. Do đó, để vẽ nên bức tranh All Ohitoyo,\ntôi nghĩ việc nền tảng phải hoàn toàn trắng tinh là điều bắt buộc.」 |
| 2869 | 「三点目。“御一夜市民”に与えるメリット。\n君の案では、御一夜市民の生活不安は解消されない」 | 「第三點是“帶給御一夜市民的利益”。你現在的方案無法解決御一夜市民的生活問題」 | 「Điểm thứ ba. Lợi ích mang lại cho “người dân Ohimitera”.\nPhương án của cậu, không giải quyết được nỗi bất an trong cuộc sống của người dân Ohimitera.」 | 「Điểm thứ ba. Lợi ích mang lại cho “người dân Ohitoyo”.\nPhương án của cậu, không giải quyết được nỗi bất an trong cuộc sống của người dân Ohitoyo.」 |
| 3034 | 「酒蔵のことも、私の看板描きやなにかも、\n御一夜の人と密着するお仕事でしょ？　だから――」 | 「釀酒廠那邊，還有我畫招牌都是與御一夜的人密切相關的工作吧？所以——」 | 「Chuyện xưởng rượu, hay việc vẽ biển hiệu của em cũng vậy,\nđều là những công việc gắn bó mật thiết với người dân Ohimitera đúng không? Vì vậy——」 | 「Chuyện xưởng rượu, hay việc vẽ biển hiệu của em cũng vậy,\nđều là những công việc gắn bó mật thiết với người dân Ohitoyo đúng không? Vì vậy——」 |
| 3278 | いや、違う。それさえもやはり一つの過程――\n御一夜を立て直すためのステップであるにすぎない。 | 不，不對。這不過也是過程之一是令御一夜復興過程中的一個步驟。 | Không, không phải. Ngay cả điều đó cũng chỉ là một quá trình——\nchỉ là một bước đệm để vực dậy Ohimitera mà thôi. | Không, không phải. Ngay cả điều đó cũng chỉ là một quá trình——\nchỉ là một bước đệm để vực dậy Ohitoyo mà thôi. |
| 3481 | エアクラ誘致、その一点で白と黒とを分け合うことない、\nオール御一夜で協力し合える、その体制を作るには。 | 工廠落戶也只是復興御一夜的方法之一。我們如今要創造的是復興御一夜的體制，無論黑貓白貓，能捉到耗子就是好貓。 | Để tạo ra một thể chế mà tất cả Ohimitera có thể hợp tác với nhau,\nchứ không phân biệt trắng đen chỉ vì vấn đề thu hút nhà máy Aircra. | Để tạo ra một thể chế mà tất cả Ohitoyo có thể hợp tác với nhau,\nchứ không phân biệt trắng đen chỉ vì vấn đề thu hút nhà máy Aircra. |
| 3577 | 御一夜が積み重ねてきた歴史を、失敗を整頓し、\n僕が見てきた、教えてもらった現状を加味して―― | 我要重新回顧參考御一夜悠久的歷史和經歷的挫折，以及我回到這裡的所見所學。 | Sắp xếp lại lịch sử mà Ohimitera đã tích lũy, những thất bại đã trải qua,\nthêm vào đó là hiện trạng mà tôi đã nhìn thấy, đã được chỉ dạy—— | Sắp xếp lại lịch sử mà Ohitoyo đã tích lũy, những thất bại đã trải qua,\nthêm vào đó là hiện trạng mà tôi đã nhìn thấy, đã được chỉ dạy—— |
| 3648 | 御一夜復興のために一丸となる。\nオール御一夜――その体制の、[いしづえ]礎を。 | 構建能夠團結起整個御一夜，朝著產業復興前進的體制基礎。 | Đoàn kết thành một khối vì sự phục hưng của Ohimitera.\nAll Ohimitera——nền tảng của thể chế đó. | Đoàn kết thành một khối vì sự phục hưng của Ohitoyo.\nAll Ohitoyo——nền tảng của thể chế đó. |
| 3936 | 同じく観光振興、御一夜再生を目的として、\nしかし手段は百八十度異なっている。 | 雖然目的同樣是振興旅遊業、讓御一夜復興，但手段卻截然不同。 | Cùng với mục đích chấn hưng du lịch, tái thiết Ohimitera,\nnhưng phương tiện lại khác nhau 180 độ. | Cùng với mục đích chấn hưng du lịch, tái thiết Ohitoyo,\nnhưng phương tiện lại khác nhau 180 độ. |

- Key 3648: JP có 御一夜 ×2 (御一夜復興 / オール御一夜) — VN có "Ohimitera" ×2, sửa cả 2.
- Key 2869: JP có 御一夜市民 ×2 — VN có "người dân Ohimitera" ×2, sửa cả 2.

### グランドリライト09_凪.txt.toml (2 dòng)

| Key | JP | TW | old_vn | fix |
|---|---|---|---|---|
| 2507 | 8620の復活が、オール御一夜の象徴ならば\nD51 1031の復活は、オール九洲の象徴だ。 | 如果說８６２０的復活是全御一夜體制的象徵，那麼Ｄ５１　１０３１的復活，就是全九州體制的象徵。 | Nếu sự hồi sinh của 8620 là biểu tượng của toàn Ohimitera,\nthì sự hồi sinh của D51 1031 là biểu tượng của toàn Kyushu. | Nếu sự hồi sinh của 8620 là biểu tượng của toàn Ohitoyo,\nthì sự hồi sinh của D51 1031 là biểu tượng của toàn Kyushu. |
| 2738 | その一角を、数年前までは御一夜の町の、\nごく普通のボイラー屋さんだった、秦さんが担ってくれた。 | 秦先生直到幾年前，還只是御一夜普普通通的鍋爐店老闆，但這次也在其中作出了貢獻。 | Đóng góp một phần trong đó, là bác Hata,\nngười mà vài năm trước chỉ là một chủ tiệm lò hơi bình thường ở Ohimitera. | Đóng góp một phần trong đó, là bác Hata,\nngười mà vài năm trước chỉ là một chủ tiệm lò hơi bình thường ở Ohitoyo. |

### グランドリライト11_ナインスターズ！.txt.toml (12 dòng)

| Key | JP | TW | old_vn | fix |
|---|---|---|---|---|
| 1598 | ――みんなで揃って、御一夜に。 | ——大家一同回到了御一夜。 | ——Tất cả cùng nhau, quay về Ohimitera. | ——Tất cả cùng nhau, quay về Ohitoyo. |
| 2157 | 「『ナインスターズ一号列車の運行開始おめでとう。\n御一夜に戻ったら、九つ星で一杯やろう』って」 | 「他說“恭喜九星一號列車開始運營。等回御一夜一起乾上一杯九星吧”」 | 「『Chúc mừng chuyến tàu Nine Stars số 1 bắt đầu vận hành.\nKhi nào về Ohimitera, hai bố con mình cùng cạn ly Ngôi sao thứ chín nhé』.」 | 「『Chúc mừng chuyến tàu Nine Stars số 1 bắt đầu vận hành.\nKhi nào về Ohitoyo, hai bố con mình cùng cạn ly Ngôi sao thứ chín nhé』.」 |
| 2485 | 「御一夜の……御一夜鉄道を支えてくれたみんなは。\n嬉しかとよね。こん晴れの舞台での、そん並び」 | 「御一夜的……支撐著御一夜鐵路的各位，要是能並肩站在這盛大的舞台上的話，肯定都老高興了吧」 | 「Mọi người... những người đã ủng hộ Đường sắt Ohimitera.\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」 | 「Mọi người... những người đã ủng hộ Đường sắt Ohitoyo.\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」 |
| 2570 | 「ああ。御一夜－八ツ城間、今日の一号列車のみは、\n記念編成で走らせるからな」 | 「是啊。從御一夜至八代段，今天的一號列車將以紀念編組前往」 | 「Ừ. Giữa Ohimitera và Yatsushiro, chỉ riêng chuyến tàu số 1 hôm nay,\nsẽ chạy bằng đội hình kỷ niệm mà.」 | 「Ừ. Giữa Ohitoyo và Yatsushiro, chỉ riêng chuyến tàu số 1 hôm nay,\nsẽ chạy bằng đội hình kỷ niệm mà.」 |
| 2578 | 「はい。御一夜-[やつしろ,2]八ツ城の一区間。その区間だけの\nキャンセル待ちをいれてたのは、双鉄くん一人です」 | 「是的。只有從御一夜到八代之間的這一站。申請這一站退票候補的，也只有你一個人而已」 | 「Vâng. Một chặng từ Ohimitera đến Yatsushiro. Người đăng ký chờ hủy\ncho riêng chặng đó, chỉ có mỗi anh Soutetsu thôi ạ.」 | 「Vâng. Một chặng từ Ohitoyo đến Yatsushiro. Người đăng ký chờ hủy\ncho riêng chặng đó, chỉ có mỗi anh Soutetsu thôi ạ.」 |
| 2700 | 「記念セレモニーなどは？\n御一夜駅でもあるのだろう？」 | 「紀念典禮呢？御一夜站也要舉行的吧？」 | 「Còn lễ kỷ niệm thì sao?\nỞ ga Ohimitera cũng có đúng không?」 | 「Còn lễ kỷ niệm thì sao?\nỞ ga Ohitoyo cũng có đúng không?」 |
| 2845 | 「まずは、折り返して御一夜に」 | 「那我們就先調頭回御一夜吧」 | 「Trước tiên, chúng ta phải quay về Ohimitera đã.」 | 「Trước tiên, chúng ta phải quay về Ohitoyo đã.」 |
| 3414 | 御一夜駅の――彼女のホームを、\nいとおしそうに、そっと眺める。 | 她用充滿憐愛的眼神眺望的，正是御一夜站的站台——屬於她的站台。 | Cô ấy âu yếm, lặng lẽ ngắm nhìn sân ga Ohimitera——\nsân ga của cô ấy. | Cô ấy âu yếm, lặng lẽ ngắm nhìn sân ga Ohitoyo——\nsân ga của cô ấy. |
| 3524 | 御一夜駅のホームに戻れば、\n真闇姉とコンとが僕らを迎えてくれる。 | 我們剛停靠在御一夜站的站台，就受到了真闇姐和空的熱烈歡迎。 | Khi trở lại sân ga Ohimitera,\nchị Mayami và Kon ra đón chúng tôi. | Khi trở lại sân ga Ohitoyo,\nchị Mayami và Kon ra đón chúng tôi. |
| 3806 | この細腕で、ずっと御一夜鉄道を――\n思いは、そのまま言葉に変わる。 | 而她以這纖弱的身軀，一直以來肩負著御一夜鐵路——想到這裡，我心中的想法不禁脫口而出。 | Với cánh tay nhỏ bé này, cô ấy đã luôn bảo vệ Đường sắt Ohimitera——\nSuy nghĩ ấy cứ thế biến thành lời nói. | Với cánh tay nhỏ bé này, cô ấy đã luôn bảo vệ Đường sắt Ohitoyo——\nSuy nghĩ ấy cứ thế biến thành lời nói. |
| 3915 | 瞬間、ふっと思い出す。御一夜に戻ってきて、\nハチロクを目覚めさせた――あの日も丁度こうだった。 | 這一瞬間，我突然想起剛回到御一夜、喚醒八六的時候——那天也是這樣的。 | Trong khoảnh khắc, tôi chợt nhớ lại. Ngày tôi trở về Ohimitera,\nvà đánh thức Hachiroku——ngày hôm đó cũng giống hệt thế này. | Trong khoảnh khắc, tôi chợt nhớ lại. Ngày tôi trở về Ohitoyo,\nvà đánh thức Hachiroku——ngày hôm đó cũng giống hệt thế này. |
| 3916 | 御一夜を出てしばらくは、\n湯医線、湯医に向かうⅨ号機関車と併走だ。 | 這使得我們在剛剛駛出御一夜站的一小段路上，可以和在湯醫線上駛向湯醫的九號齊頭並進。 | Sau khi rời Ohimitera một đoạn,\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yui trên tuyến Yui. | Sau khi rời Ohitoyo một đoạn,\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yui trên tuyến Yui. |

- Key 2485: JP có 御一夜 ×2 (御一夜の…… / 御一夜鉄道) nhưng VN chỉ diễn dòng thứ hai ("Đường sắt Ohimitera"); dòng đầu bị lược trong VN ("Mọi người..."). T1 chỉ sửa chỗ đã diễn → "Đường sắt Ohitoyo"; phần lược xem cờ F-T1-1 bên dưới, KHÔNG sửa trong đợt này.
- Key 3806: "Đường sắt Ohimitera" → "Đường sắt Ohitoyo" — thuộc T1 (dạng nguồn là Ohimitera); trùng đích với T2 nhưng không phải dòng T2.
- Key 3916: "Yui" / "tuyến Yui" trong cùng dòng GIỮ NGUYÊN — thuộc T7, batch khác, không đụng.

### 凪ふかみ02_命の重さ.txt.toml (2 dòng)

| Key | JP | TW | old_vn | fix |
|---|---|---|---|---|
| 960 | 「――と、いうわけで僕は右田の養子となった。\nそして、御一夜にやってきたのだ」 | 「——就是這樣，我就成了右田家的養子。而後就來了御一夜」 | 「——Chính vì thế, anh đã trở thành con nuôi nhà Migita.\nVà rồi, anh chuyển đến Ohimitera.」 | 「——Chính vì thế, anh đã trở thành con nuôi nhà Migita.\nVà rồi, anh chuyển đến Ohitoyo.」 |
| 2168 | \x%l8620;#00ffc040;8620%l;#;の\x%lブラスト;#00ffc040;ブラスト%l;#;音をかき消すほどの激しい風雨が、\n御一夜駅のホームを叩き、洗ってる。 | 激烈到連\x%l8620;#00ffc040;８６２０%l;#;的\x%lブラスト;#00ffc040;汽缸排汽%l;#;聲都被壓過的狂風暴雨正猛烈沖刷著御一夜站的站台。 | Trận cuồng phong bão táp dữ dội lấn át cả tiếng \x%lブラスト;#00ffc040;khí thải xi lanh%l;#; của \x%l8620;#00ffc040;8620%l;#;,\nđang trút xuống và gột rửa sân ga Ohimitera. | Trận cuồng phong bão táp dữ dội lấn át cả tiếng \x%lブラスト;#00ffc040;khí thải xi lanh%l;#; của \x%l8620;#00ffc040;8620%l;#;,\nđang trút xuống và gột rửa sân ga Ohitoyo. |

- Key 2168: các tag %l của 8620 / ブラスト giữ nguyên, chỉ đổi display text "sân ga Ohimitera" → "sân ga Ohitoyo".

### 凪ふかみ05_凪の開眼！？.txt.toml (3 dòng)

| Key | JP | TW | old_vn | fix |
|---|---|---|---|---|
| 2266 | 「なるばい！　凪さま！\nめざせ！　御一夜一のよかおんな！　ばい！！！」 | 「好嘞！　本小姐！要成為御一夜最好的女人！！！」 | 「Tớ sẽ làm được! Nagi ta đây!\nMục tiêu! Người phụ nữ tuyệt vời nhất Ohimitera!!!」 | 「Tớ sẽ làm được! Nagi ta đây!\nMục tiêu! Người phụ nữ tuyệt vời nhất Ohitoyo!!!」 |
| 2367 | 「大納得ばい！　御一夜戻ったら稽古の前に銀行よって、\n教えてもらえるか聞いてくるばい！」 | 「懂咧！　回到御一夜以後，咱在練劍前先去一趟銀行，問問她能不能教咱！」 | 「Quá hợp lý! Về tới Ohimitera tớ sẽ ghé ngân hàng trước giờ tập,\nđể hỏi xem chị ấy có chịu dạy tớ không!」 | 「Quá hợp lý! Về tới Ohitoyo tớ sẽ ghé ngân hàng trước giờ tập,\nđể hỏi xem chị ấy có chịu dạy tớ không!」 |
| 3222 | そーいえばそーだったとばい！\n御一夜の駅で、車椅子のおばちゃんにも言われたと！ | 還真是嘞！在御一夜站的時候，坐輪椅的老婆婆也是這麼說的！ | Nhắc mới nhớ đúng là vậy ha!\nLúc ở ga Ohimitera, tớ cũng bị bà lão ngồi xe lăn nhắc nhở mà! | Nhắc mới nhớ đúng là vậy ha!\nLúc ở ga Ohitoyo, tớ cũng bị bà lão ngồi xe lăn nhắc nhở mà! |

## Giữ nguyên / cờ (không sửa trong đợt này)

- **0 dòng ứng viên bị loại vì JP thiếu 御一夜.** Mọi dòng CSV3 VN còn "Ohimitera" trong 5 folders đều có JP chứa 御一夜 và đều đã sửa.
- **F-T1-1 — グランドリライト11_ナインスターズ！ key 2485 (cờ, không sửa):** JP "御一夜の……御一夜鉄道を支えてくれたみんなは" có 御一夜 ×2, TW cũng có 御一夜 ×2 ("御一夜的……支撐著御一夜鐵路"), nhưng VN chỉ diễn dòng thứ hai ("những người đã ủng hộ Đường sắt Ohimitera"), dòng đầu bị lược thành "Mọi người...". Đây là lược dịch có từ trước (audit đã duyệt dòng này, không nằm trong fix list), không phải lệch hàng. T1 chỉ đổi "Đường sắt Ohimitera" → "Đường sắt Ohitoyo". Việc có bổ sung "của Ohitoyo" cho "Mọi người..." hay không để coordinator quyết ở pass sau — không tự ý thêm nghĩa trong đợt thuật ngữ này.
- **53 dòng đã sửa trong audit** (liệt kê ở § Phương pháp) không nằm trong JSON này — không sửa lại, không đếm trùng.
- **Folders 08 / 10 / 11 không có dòng nào:** 08_Niiroku (5 dòng CSV3) và 10_Chikuni (15 dòng CSV3) đã sửa hết trong audit; 11_Other không có dòng CSV3 nào chứa "Ohimitera".

## Lượt soát thứ hai (second pass)

- **Tổng: 38 / soát lại: 38 / loại bỏ: 0 / sửa lại: 0** (giá trị fix). Đọc lại từng fix đối chiếu JP: mọi fix diễn đúng 御一夜 trong JP thành "Ohitoyo", không đổi gì khác.
- Kiểm chứng cơ học (script chỉ kiểm, không sửa): jp/tw/old_vn trong JSON khớp nguồn liệt kê 38/38 — trong lúc kiểm phát hiện 1 lỗi chép TW ở グランドリライト11 key 2157 (thiếu dấu 」 cuối), đã sửa TRƯỚC lượt soát thứ hai; mọi fix == old_vn chỉ đổi "Ohimitera"→"Ohitoyo" (40/40 occurrence: 36 dòng ×1 + 2 dòng ×2); 0 fix còn chứa "Ohimitera"; keys là string, không trùng (file,key).
- Đối chiếu TOML-2: old_vn của cả 38 dòng khớp giá trị script trong TOML-2 (chuẩn hoá literal `\n` → khoảng trắng, vì TOML-2 có chỗ flatten `\n` thành space) — **38/38**.
- Khối TOML: 5 khối (mỗi file 1 khối), 38 keys, parse bằng tomllib OK, giá trị parse ra == fix trong JSON **38/38**.

## Khối TOML (đã parse-verified)

### グランドリライト01_オール御一夜、成立ならず.txt.toml (19 dòng)

```toml
[script]
1612 = "「……Ngân hàng Ohitoyo cũng,\\nđã xem xét việc mua lại để phục hồi tuyến đường này rồi sao?」"
2181 = "「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohitoyo,\\ntin tưởng cậu Soutetsu, và cả những mối quan hệ đó nữa.」"
2244 = "「Bước đầu tiên để kết nối lại.\\nRào cản cho việc phục hồi tuyến đường giữa Ohitoyo - Yatsushiro, là quá cao.」"
2277 = "「Sách liên quan đến lịch sử địa phương của Ohitoyo,\\nđể ở đây là được đúng không?」"
2349 = "「Ừm. Thứ tôi muốn tạo ra là một thể chế vượt qua lợi ích của từng cá nhân,\\ncó thể gọi là thể chế All Ohitoyo.」"
2366 = "「Ừm. Nền tảng để xây dựng thể chế All Ohitoyo.\\nBản nháp đó, nếu pha trộn màu sắc của bất kỳ ai thì chắc chắn, sẽ không thành lập được.」"
2408 = "「Được thôi, Giám đốc chi nhánh Ohitoyo. Đây là mệnh lệnh công việc.\\nHãy hỗ trợ cậu Migita Soutetsu, và xem xét tính khả thi của đề xuất này.」"
2418 = "「Em nghĩ anh nên tìm hiểu thêm về Ohitoyo.\\nNếu anh thực sự muốn phục hưng thị trấn này.」"
2434 = "「Thực tế thì, chúng tôi,\\nvà cả Ohitoyo, đang bị đặt vào một tình thế nghiêm trọng mà.」"
2524 = "「Ngoài việc “cũng” với tư cách là Giám đốc chi nhánh Ohitoyo ra——\\nrốt cuộc, cô đứng ở lập trường nào」"
2582 = "「Ngay cả với tư cách là Giám đốc chi nhánh Ohitoyo, cháu cũng muốn tham gia vào kế hoạch này.\\nVì nếu bỏ mặc thì thật đáng tiếc——đồng thời, đây cũng là một phương án nguy hiểm.」"
2762 = "「Đúng là vậy. Do đó, để vẽ nên bức tranh All Ohitoyo,\\ntôi nghĩ việc nền tảng phải hoàn toàn trắng tinh là điều bắt buộc.」"
2869 = "「Điểm thứ ba. Lợi ích mang lại cho “người dân Ohitoyo”.\\nPhương án của cậu, không giải quyết được nỗi bất an trong cuộc sống của người dân Ohitoyo.」"
3034 = "「Chuyện xưởng rượu, hay việc vẽ biển hiệu của em cũng vậy,\\nđều là những công việc gắn bó mật thiết với người dân Ohitoyo đúng không? Vì vậy——」"
3278 = "Không, không phải. Ngay cả điều đó cũng chỉ là một quá trình——\\nchỉ là một bước đệm để vực dậy Ohitoyo mà thôi."
3481 = "Để tạo ra một thể chế mà tất cả Ohitoyo có thể hợp tác với nhau,\\nchứ không phân biệt trắng đen chỉ vì vấn đề thu hút nhà máy Aircra."
3577 = "Sắp xếp lại lịch sử mà Ohitoyo đã tích lũy, những thất bại đã trải qua,\\nthêm vào đó là hiện trạng mà tôi đã nhìn thấy, đã được chỉ dạy——"
3648 = "Đoàn kết thành một khối vì sự phục hưng của Ohitoyo.\\nAll Ohitoyo——nền tảng của thể chế đó."
3936 = "Cùng với mục đích chấn hưng du lịch, tái thiết Ohitoyo,\\nnhưng phương tiện lại khác nhau 180 độ."
```

### グランドリライト09_凪.txt.toml (2 dòng)

```toml
[script]
2507 = "Nếu sự hồi sinh của 8620 là biểu tượng của toàn Ohitoyo,\\nthì sự hồi sinh của D51 1031 là biểu tượng của toàn Kyushu."
2738 = "Đóng góp một phần trong đó, là bác Hata,\\nngười mà vài năm trước chỉ là một chủ tiệm lò hơi bình thường ở Ohitoyo."
```

### グランドリライト11_ナインスターズ！.txt.toml (12 dòng)

```toml
[script]
1598 = "——Tất cả cùng nhau, quay về Ohitoyo."
2157 = "「『Chúc mừng chuyến tàu Nine Stars số 1 bắt đầu vận hành.\\nKhi nào về Ohitoyo, hai bố con mình cùng cạn ly Ngôi sao thứ chín nhé』.」"
2485 = "「Mọi người... những người đã ủng hộ Đường sắt Ohitoyo.\\nChắc hẳn sẽ rất vui nhỉ. Khi thấy đội hình đó trên sân khấu rực rỡ này.」"
2570 = "「Ừ. Giữa Ohitoyo và Yatsushiro, chỉ riêng chuyến tàu số 1 hôm nay,\\nsẽ chạy bằng đội hình kỷ niệm mà.」"
2578 = "「Vâng. Một chặng từ Ohitoyo đến Yatsushiro. Người đăng ký chờ hủy\\ncho riêng chặng đó, chỉ có mỗi anh Soutetsu thôi ạ.」"
2700 = "「Còn lễ kỷ niệm thì sao?\\nỞ ga Ohitoyo cũng có đúng không?」"
2845 = "「Trước tiên, chúng ta phải quay về Ohitoyo đã.」"
3414 = "Cô ấy âu yếm, lặng lẽ ngắm nhìn sân ga Ohitoyo——\\nsân ga của cô ấy."
3524 = "Khi trở lại sân ga Ohitoyo,\\nchị Mayami và Kon ra đón chúng tôi."
3806 = "Với cánh tay nhỏ bé này, cô ấy đã luôn bảo vệ Đường sắt Ohitoyo——\\nSuy nghĩ ấy cứ thế biến thành lời nói."
3915 = "Trong khoảnh khắc, tôi chợt nhớ lại. Ngày tôi trở về Ohitoyo,\\nvà đánh thức Hachiroku——ngày hôm đó cũng giống hệt thế này."
3916 = "Sau khi rời Ohitoyo một đoạn,\\nchúng tôi sẽ chạy song song với đầu máy số 9 hướng về Yui trên tuyến Yui."
```

### 凪ふかみ02_命の重さ.txt.toml (2 dòng)

```toml
[script]
960 = "「——Chính vì thế, anh đã trở thành con nuôi nhà Migita.\\nVà rồi, anh chuyển đến Ohitoyo.」"
2168 = "Trận cuồng phong bão táp dữ dội lấn át cả tiếng \\x%lブラスト;#00ffc040;khí thải xi lanh%l;#; của \\x%l8620;#00ffc040;8620%l;#;,\\nđang trút xuống và gột rửa sân ga Ohitoyo."
```

### 凪ふかみ05_凪の開眼！？.txt.toml (3 dòng)

```toml
[script]
2266 = "「Tớ sẽ làm được! Nagi ta đây!\\nMục tiêu! Người phụ nữ tuyệt vời nhất Ohitoyo!!!」"
2367 = "「Quá hợp lý! Về tới Ohitoyo tớ sẽ ghé ngân hàng trước giờ tập,\\nđể hỏi xem chị ấy có chịu dạy tớ không!」"
3222 = "Nhắc mới nhớ đúng là vậy ha!\\nLúc ở ga Ohitoyo, tớ cũng bị bà lão ngồi xe lăn nhắc nhở mà!"
```

## Kết bài

Đợt U1c xong: **T1 (phần folders 07–11) — 38 dòng**, tất cả đều có JP chứa 御一夜 và đã đổi "Ohimitera" → "Ohitoyo" (40 occurrence). Không có dòng nào JP thiếu 御一夜, không có dòng nào còn "Ohimitera" trong gloss %l, không đụng "Yui" (T7) hay bất kỳ thuật ngữ nào khác. Phần còn lại của T1 (folders 00–02) thuộc batch khác; theo đếm lại của U1b, sau đợt này T1 còn **221 dòng** (259 − 38). Một cờ duy nhất để lại cho coordinator: Grand 11 key 2485 lược mất 御一夜 đầu trong VN (F-T1-1).
