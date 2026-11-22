# Unification — §1 OPEN T56–T66 (batch U13a: T56, T57, T58, T59, T60, T61, T63, T66)

**Phạm vi:** §1 T56–T66 theo quyết định của coordinator 22/11 ~11:25 (uỷ quyền Hieu), trên báo cáo điều tra E1 (`unification/investigation-open-terminology-t56-t66-REPORT.md`). T62/T64/T65 GIỮ NGUYÊN (0 dòng — đã kiểm chứng, xem §9). T66 được áp dụng theo quyết định đã ghi trong `ROUTE-UNIFICATION.md` (coordinator log E1) dù task giao việc không liệt kê T66 trong danh sách bullet — xem §0 về đối chiếu số liệu.
**Không đụng:** `ROUTE-UNIFICATION.md`, `MEMORY.md`, queue files, bất kỳ file audit/moan nào. Không gửi gì cho Hieu. Không spawn subagent.
**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json` (9.238 mục map được, 0 không map được — xem §0), `moans/moan-*-wrong.json` (1.516 mục), các đợt unification đã gộp (1.060 mục; 6 dòng trong đợt này trùng — xem §0c/§0d), TOML-2 (chỉ đối chiếu 3 dòng nghi vấn — xem §0). Mọi dòng trong đợt này đều có trong CSV3 good-set (0 dòng lấy từ TOML-2).

## 0. Đối chiếu số liệu — HAI lệch số cần coordinator biết

### 0a. T56 thực tế là 122 dòng, không phải 124

Báo cáo E1 ghi T56 = 124 (72 “Trọng Quốc” + 48 “Zhongguo” + 2 “Nakakuni”/“Chukoku” + 2 “tiếng Zhongguo”). Đếm lại trực tiếp từ CSV3 good-set + map giá trị hiện tại: **48 dòng chứa “Zhongguo” trong CUR đã BAO GỒM 2 dòng “tiếng Zhongguo”** (仲国02 2897, 仲国03 2845) — đếm theo file: 仲国02 27 = 26 tên nước + 2897; 仲国03 16 = 15 tên nước + 2845; 仲国04 5. Báo cáo E1 cộng cả “48” lẫn “+2 dòng tiếng” nên đếm trùng 2 dòng ngôn ngữ. Số dòng phân biệt thực tế: **72 + 46 (tên nước “Zhongguo”) + 2 (ngôn ngữ “tiếng Zhongguo”) + 1 (“Nakakuni”) + 1 (“nước Chukoku”) = 122 dòng.** Tổng toàn đợt theo đó là **171 dòng phân biệt** (122+5+3+1+27+7+4+2), không phải 173. Mọi bảng dưới đây cộng lại = 171; snippet đã ghi theo số thực này và nêu rõ cơ sở.

### 0b. T66 (2 dòng) có trong quyết định coordinator nhưng không có trong bullet của task

Task giao việc liệt kê 7 mục (T56, T57, T58, T59, T60, T61, T63) và ghi tổng 173 dòng; log quyết định của coordinator trong `ROUTE-UNIFICATION.md` (mục E1) **có** quyết định T66 → “chín tỉnh” (2 dòng: グランドリライト07_真闇 2545/2546), và tổng 173 của báo cáo E1 cũng bao gồm T66. Đợt này áp dụng cả T66 (8 mục / 171 dòng phân biệt) để khớp với quyết định đã ghi của coordinator; nếu coordinator muốn loại T66 thì chỉ cần bỏ 2 dòng item T66 trong JSON (đã tách riêng theo item). Snippet ghi “8 mục / 171 dòng” và nêu rõ lệch này.

### 0c. Map giá trị hiện tại

Map tự build lại từ đầu (loader của batch U3, có sửa 1 lỗi: các mục `audit-obasan` không có trường `fix` — 2 mục đã map nhầm thành `None`, đã loại; sau sửa: 0 giá trị `None`): CSV3 good-set 87.833 dòng; audit map được 9.238/9.238 (0 không map — loader có fallback khớp TW + khớp `old_vn`, khác với báo cáo E1 dùng khớp `(key, JP)` thuần: 9.144/9.243); moan 1.516/1.516; unification đã gộp **1.060 mục** (656 lúc bắt đầu đợt + 2 file set2/set3 gộp trong lúc đợt này đang chạy — xem §0d). `old_vn` = giá trị sau unification đã gộp nếu có (quy tắc rebuild: áp dụng fix list theo thứ tự gộp), nếu không thì moan > audit > CSV3. Trong đợt này **6 dòng** có nguồn unification: lr_日々姫ふかみh1 1689 (U1a — “Ohitoyo”) + 5 dòng rebase trên set2/set3 (xem §0d); 15 dòng nguồn audit, 150 dòng nguồn CSV3, 0 dòng nguồn moan.

### 0d. Rebase trên 2 batch gộp song song trong lúc đợt này đang chạy (set2/set3)

Trong lúc đợt này đang làm, coordinator đã gộp 2 file unification mới: `unification-t1-set2-wrong.json` (240 dòng, T3 帝鉄 → “Teitetsu”) và `unification-t1-set3-wrong.json` (193 dòng, gồm mục 日ノ本 “Hinamoto” → “Hinomoto”). 5 dòng trong đợt này trùng (file,key) với 2 file đó — theo quy tắc rebuild (áp dụng fix list theo thứ tự gộp, batch sau xây trên giá trị batch trước — tiền lệ U6/Grand 01 2181), `old_vn` của 5 dòng này đã được rebase lên giá trị sau set2/set3, và fix của đợt này chỉ đổi đúng phần thuật ngữ của mình:

- ハチロク10 1529 (T57): set3 đã đổi “Hinamoto” → “Hinomoto”; đợt này chỉ đổi “Eikoku (Anh Quốc)” → “Anh Quốc”, giữ “Hinomoto”. (Nhờ vậy cờ F-T57-1 về “Hinamoto” ở dòng này coi như đã xong qua set3.)
- 仲国02 2175, 仲国03 2083, 仲国03 2251 (T56): set2 đã đổi “Đường sắt Hoàng gia” → “Đường sắt Teitetsu”; đợt này chỉ đổi “Zhongguo” → “Trung Quốc”.
- 仲国03 2082 (T63): set2 đã đổi nửa sau “Đường sắt Hoàng gia” → “Đường sắt Teitetsu”; đợt này chỉ đổi nửa đầu “Đường sắt Đế hữu Hinomoto” → “Đường sắt Đế quốc Hinomoto”. (Nhờ vậy cờ F-T63-1 về nửa sau 2082 coi như đã xong qua set2 — coordinator không cần kiểm tra U3 cho dòng này nữa.)

Ngoài 5 dòng trên, chỉ còn lr_日々姫ふかみh1 1689 trùng đợt đã gộp (U1a, giá trị khớp sẵn). Tổng cộng 6/171 dòng có nguồn unification. Map đã build lại SAU khi set2/set3 xuất hiện (loader loại file output của chính đợt này để khỏi tự ăn giá trị của mình); mọi kiểm chứng cơ học chạy lại trên map mới.

## Phương pháp

- **Liệt kê:** quét toàn bộ CSV3 good-set lấy mọi dòng có JP chứa thuật ngữ gốc (仲国 204 dòng; 詠国 16; 次元流 3; キルクイティウム 6; 頭取 29; 持株会社 10; 帝有 7; 九国 6), phân loại theo dạng trong giá trị hiện tại (CUR). Kiểm chứng chéo số đếm JP-term trong JP so với số lần dạng cũ xuất hiện trong CUR: **T56 0 lệch** (mọi dòng FIX đều có số lần 仲国 trong JP = số lần dạng cũ trong CUR, kể cả các dòng 2 lần: 仲国02 1651/2073, 仲国08 1693/1920/2071/2508); T60 3 dòng có 2 dạng cũ nhưng JP 頭取 chỉ 1 lần — đã đọc JP để xác định đúng lần cần đổi (支店長 giữ nguyên, xem §5); T61 7/7 JP=1/CUR=1; T63 4/4 JP có 帝有鉄道/帝有鐵道 (key 60 có cả 鉄道帝有法).
- **Kiểm tra ngược (misalignment):** quét toàn bộ CUR tìm dạng cũ mà JP KHÔNG chứa thuật ngữ gốc: “Trọng Quốc” 1 dòng (仲国08 2823 — JP 日仲, xem cờ F-T56-1); “Vịnh Quốc” 1 dòng (ハチロク09 2102 — ngoại lệ T57 đã giữ, JP katakana); “công ty cổ phần” 6 dòng — tất cả JP đều là 株式会社/（株） (đúng nghĩa, không phải 持株会社) nên KHÔNG đụng (xem §9); “Đường sắt Đế hữu” 0 dòng ngoài phạm vi (2082/2248 có 帝有鉄道; 1789 có 帝有鐵道 truyền thống).
- **Không sửa bulk bằng script:** mọi giá trị fix đều do đọc JP (+TW) từng dòng rồi quyết cặp thay thế (xem cột Lý do từng dòng; các dòng đặc biệt có ghi chú riêng); script chỉ dùng để tra cứu, lắp khối TOML và kiểm chứng cơ học (kiểm tra ngược: áp dụng cặp thay thế ngược lên fix phải ra đúng `old_vn` — 171/171 đạt; `old_vn` khớp map hiện tại (đã gồm set2/set3) 171/171; JP/TW khớp CSV3 171/171; khối TOML parse-verified 33 file / 171 key).
- **Không đụng dòng gasp Ư hay dòng “Kh”:** chỉ có 仲国03 2845 mang “——Ư!” cuối dòng — phép thay chỉ đổi “tiếng Zhongguo”, giữ nguyên “——Ư!”. Không dòng nào trong đợt này thuộc diện “Kh”.

## 1. T56 — 仲国 → “Trung Quốc” (122 dòng)

### lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1689 | 「まぁ、急な話だったからな。稀咲仲介での、\\n仲国からの要人たちの、団体での御一夜視察」 | 「沒辦法嘛。畢竟在稀咲中介下，來自仲國的重要人物集體來御一夜視察這件事太突然了」 | 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\\nđến thị sát Ohitoyo thông qua sự môi giới của Kisaki.」 | 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Trung Quốc\\nđến thị sát Ohitoyo thông qua sự môi giới của Kisaki.」 | JP 仲国 (không furigana); “Nakakuni” là Gemini đọc sai (仲=naka + 国=kuni) → “Trung Quốc”. old_vn đã qua đợt U1a (“Ohitoyo”). (Dòng này còn “Ohimitera” cũ đã sửa xong trong U1a — không thuộc đợt này.) |

### lr稀咲追加01_仲国視察の誘い.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 996 | 「対人関係のみに絞れば、そうかもね。\\nなにせ仲国国務院鉄道部の副部長秘書だ」 | 「不過，這所謂彈性，在見識過姜小姐的表現以後，真是自慚形穢，差得太遠了」 | 「Nếu chỉ xét riêng về quan hệ đối nhân xử thế, thì có lẽ là vậy.\\nDù sao cô ấy cũng là thư ký của Thứ trưởng Bộ Đường sắt Quốc vụ viện Trọng Quốc mà.」 | 「Nếu chỉ xét riêng về quan hệ đối nhân xử thế, thì có lẽ là vậy.\\nDù sao cô ấy cũng là thư ký của Thứ trưởng Bộ Đường sắt Quốc vụ viện Trung Quốc mà.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1068 | 「ん？　複数の鉄道事業者って……国鉄以外にもあるんだ。\\n仲国にも……いわゆる民鉄、私鉄的なものが」 | 「其實鐵道部也接到了一些對私有線路基金有興趣的鐵路從業人員的諮詢」 | 「Hử? Một số doanh nghiệp đường sắt tức là……ngoài đường sắt quốc gia ra vẫn còn à.\\nỞ Trọng Quốc cũng có……cái gọi là đường sắt dân sự, đường sắt tư nhân sao.」 | 「Hử? Một số doanh nghiệp đường sắt tức là……ngoài đường sắt quốc gia ra vẫn còn à.\\nỞ Trung Quốc cũng có……cái gọi là đường sắt dân sự, đường sắt tư nhân sao.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1091 | 日ノ本車輌の淵さんはじめ、仲国からの声かけを受けた\\n一流どころの技術者ならば、複数の名前を把握している。 | 「原來如此，確實有道理。這方面的情況我也有所耳聞——」 | Từ anh Fuchi của Xe lửa Hinomoto, cho đến những kỹ sư hàng đầu\\nnhận được lời mời từ Trọng Quốc, tôi đều nắm rõ một vài cái tên. | Từ anh Fuchi của Xe lửa Hinomoto, cho đến những kỹ sư hàng đầu\\nnhận được lời mời từ Trung Quốc, tôi đều nắm rõ một vài cái tên. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1161 | 「ふふっ、相変わらず呑むんだねぇ。\\n自分用ってことは――仲国からの持ち込み？」 | 「啊，承蒙邀請，我真是太開心了！哪有拒絕的道理呀！作為回禮，我帶自備的紹興酒過來吧」 | 「Fufu, vẫn thích uống như ngày nào nhỉ.\\nCủa riêng mình nghĩa là――mang từ Trọng Quốc sang sao?」 | 「Fufu, vẫn thích uống như ngày nào nhỉ.\\nCủa riêng mình nghĩa là――mang từ Trung Quốc sang sao?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1182 | よく見れば、茶器と皿ともいつもとは違う、仲国のものだ。\\n細かな気遣いもさすがだなと、改めて感心させられる。 | 「嘻嘻，喜歡的話還有哦，不要客氣。雙鐵也有，給」 | Nhìn kỹ thì, cả bộ ấm chén và đĩa đều khác ngày thường, là đồ của Trọng Quốc.\\nSự chu đáo tỉ mỉ này quả nhiên không hổ danh là cô ấy, khiến tôi một lần nữa phải thán phục. | Nhìn kỹ thì, cả bộ ấm chén và đĩa đều khác ngày thường, là đồ của Trung Quốc.\\nSự chu đáo tỉ mỉ này quả nhiên không hổ danh là cô ấy, khiến tôi một lần nữa phải thán phục. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1511 | 「新事業案の共有。それが仲国でも展開可能なもので\\nあるなら、なんらかの方法での共同展開を検討頂きたい」 | 「能對我們的私有線路基金抱有這樣的興趣，我真的很高興。非常感謝。那第二呢？」 | 「Chia sẻ dự án mới. Nếu đó là dự án có thể triển khai ở Trọng Quốc,\\nchúng tôi mong muốn được xem xét việc cùng triển khai bằng một phương pháp nào đó.」 | 「Chia sẻ dự án mới. Nếu đó là dự án có thể triển khai ở Trung Quốc,\\nchúng tôi mong muốn được xem xét việc cùng triển khai bằng một phương pháp nào đó.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1563 | 仲国は冥国をはっきりとライバル視している国だ。ゆえ、\\n冥国のエアクラ推進への対立軸を立てようとしていると。 | 「這個說法確實多少從稀咲那裡聽說過一點」 | Trọng Quốc là quốc gia coi Minh Quốc là đối thủ rõ rệt. Vì vậy,\\nhọ đang cố gắng thiết lập một trục đối lập với việc thúc đẩy Aircra của Minh Quốc. | Trung Quốc là quốc gia coi Minh Quốc là đối thủ rõ rệt. Vì vậy,\\nhọ đang cố gắng thiết lập một trục đối lập với việc thúc đẩy Aircra của Minh Quốc. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1573 | 稀咲が驚いた顔をする。春節――旧正月は確か、\\n仲国で一番のお祭りの時期と聞き及ぶが…… | 「這！？春節期間還是不太好吧」 | Kisaki lộ vẻ ngạc nhiên. Tết Nguyên Đán――Tết Âm lịch hình như,\\nlà dịp lễ hội lớn nhất ở Trọng Quốc theo như tôi nghe được…… | Kisaki lộ vẻ ngạc nhiên. Tết Nguyên Đán――Tết Âm lịch hình như,\\nlà dịp lễ hội lớn nhất ở Trung Quốc theo như tôi nghe được…… | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1716 | 「というと、仲国国務院の鉄道部内で……ですか。\\n大変恐縮です。――というか、一体全体どういうわけで」 | 她臉上帶著平和的笑容，自然地說出的話語，卻有著與此全然不同的分量，讓我一時沒能完全理解。 | 「Nói vậy tức là, trong nội bộ Bộ Đường sắt của Quốc vụ viện Trọng Quốc……sao.\\nThật vô cùng vinh hạnh. ――Hay đúng hơn là, rốt cuộc thì tại sao lại như vậy.」 | 「Nói vậy tức là, trong nội bộ Bộ Đường sắt của Quốc vụ viện Trung Quốc……sao.\\nThật vô cùng vinh hạnh. ――Hay đúng hơn là, rốt cuộc thì tại sao lại như vậy.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1741 | 「双鉄先生、ご興味がおありでしたらいかがでしょう。\\n弊部がお招きいたしますので、稀咲女士との仲国視察は」 | 姜小姐的態度突然柔和了下來。 | 「Ngài Soutetsu, nếu ngài có hứng thú thì sao ạ.\\nBộ chúng tôi sẽ gửi lời mời, chuyến khảo sát Trọng Quốc cùng cô Kisaki.」 | 「Ngài Soutetsu, nếu ngài có hứng thú thì sao ạ.\\nBộ chúng tôi sẽ gửi lời mời, chuyến khảo sát Trung Quốc cùng cô Kisaki.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1819 | 「父は、それをみかねたんだろうね。\\n仲国からの留学生を、家庭教師につけてくれた」 | 確實，一個新來的小姑娘當支行長，自稱又是[ｂｏｋｕ]我——這樣表現出來的就不是威嚴而是可愛了。 | 「Chắc cha em không thể đứng nhìn mãi được.\\nNên ông đã thuê một du học sinh từ Trọng Quốc về làm gia sư cho em.」 | 「Chắc cha em không thể đứng nhìn mãi được.\\nNên ông đã thuê một du học sinh từ Trung Quốc về làm gia sư cho em.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1860 | 「あなたが双鉄先生ですね。はじめまして。\\n仲国国務院、鉄道部副部長秘書の、[きょうようこう,2]姜叶煌と申します」 | 稀咲的支行長室與往常無二。但今天在座的卻多了一張陌生的面孔。 | 「Ngài là Soutetsu nhỉ. Rất hân hạnh được gặp.\\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc, tên là Khương Diệp Hoàng.」 | 「Ngài là Soutetsu nhỉ. Rất hân hạnh được gặp.\\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trung Quốc, tên là Khương Diệp Hoàng.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### lr稀咲追加02_仲国視察.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1072 | 「仲国で一番たくさんの乗客に乗られている列車。\\nボクらをそれに乗せてほしい」 | 「仲國最多乘客乘坐的列車，我們希望能去乘坐一下」 | 「Chuyến tàu có số lượng hành khách đi nhiều nhất ở Trọng Quốc.\\nTôi muốn chúng tôi được đi chuyến tàu đó.」 | 「Chuyến tàu có số lượng hành khách đi nhiều nhất ở Trung Quốc.\\nTôi muốn chúng tôi được đi chuyến tàu đó.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1073 | 「仲国の若者層の主たるニュースソースはどのあたりだ？\\nネット、新聞、TVなどいろいろあるかとは思うが」 | 「仲國的年輕人主要是通過什麼樣的途徑獲得訊息的？比如網路、報紙和電視，應該是種類繁多」 | 「Nguồn tin tức chính của giới trẻ Trọng Quốc là ở đâu?\\nTôi nghĩ có rất nhiều nguồn như mạng internet, báo chí, TV v.v.」 | 「Nguồn tin tức chính của giới trẻ Trung Quốc là ở đâu?\\nTôi nghĩ có rất nhiều nguồn như mạng internet, báo chí, TV v.v.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1074 | 「仲国では、まだエアクラ自動車の普及率、\\nそこまでではないと理解していたけど？」 | 「仲國的空凝機汽車普及率，應該還沒有那麼高吧？」 | 「Chị hiểu là ở Trọng Quốc, tỷ lệ phổ cập của xe Aircra\\nvẫn chưa đến mức đó mà nhỉ?」 | 「Chị hiểu là ở Trung Quốc, tỷ lệ phổ cập của xe Aircra\\nvẫn chưa đến mức đó mà nhỉ?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1077 | 「かなり強い同意を受けたように思ったが――\\n仲国国鉄の餐車や寝台車も、同じような感じなのか？」 | 「似乎你們也深有同感的樣子——莫非仲國的餐車和臥鋪車也都經歷了類似的過程嗎？ | 「Tôi có cảm giác em rất đồng tình với điều này——\\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trọng Quốc cũng giống như vậy sao?」 | 「Tôi có cảm giác em rất đồng tình với điều này——\\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trung Quốc cũng giống như vậy sao?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1153 | 「ほう。仲国と日ノ本の鉄道両方を知っているのか。\\nそれは大変こころづよいな」 | 「哦，對中日雙方的鐵路知己知彼啊。那可真是相當可靠呢」 | 「Hô. Vậy là em am hiểu cả đường sắt của Trọng Quốc và Hinomoto sao.\\nThế thì thật là đáng tin cậy.」 | 「Hô. Vậy là em am hiểu cả đường sắt của Trung Quốc và Hinomoto sao.\\nThế thì thật là đáng tin cậy.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1294 | 「若者層の主たるニュースソースはニュースサイト、\\nSNS、グループチャット。ステマは仲国でも反感を買う」 | 「年輕人的訊息來源以網站、社交軟體和即時通信軟體為主，仲國人也非常反感秘密行銷」 | 「Nguồn tin tức chính của giới trẻ là các trang tin tức,\\nSNS, trò chuyện nhóm. Stealth marketing ở Trọng Quốc cũng gây phản cảm.」 | 「Nguồn tin tức chính của giới trẻ là các trang tin tức,\\nSNS, trò chuyện nhóm. Stealth marketing ở Trung Quốc cũng gây phản cảm.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1332 | 「ボクもその線がいいと思う。だからまず仲国の若い\\nカップル層の多数が、どのような嗜好かを知りたいな」 | 「我也認為這樣做最為妥當，所以需要先知道你們仲國的年輕情侶大多有著什麼樣的需求」 | 「Tôi cũng nghĩ hướng đó là tốt nhất. Vì vậy, trước tiên tôi muốn biết\\nđại đa số các cặp đôi trẻ ở Trọng Quốc có sở thích như thế nào.」 | 「Tôi cũng nghĩ hướng đó là tốt nhất. Vì vậy, trước tiên tôi muốn biết\\nđại đa số các cặp đôi trẻ ở Trung Quốc có sở thích như thế nào.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1343 | 「西瓜君の印象だけで語って欲しいんだけど――\\n日ノ本の鉄道と仲国の鉄道、一番の違いってなにかな」 | 「我想問一下單以西瓜的第一印象而言的話——日本鐵路和仲國鐵路最大的區別是什麼？」 | 「Chị muốn nghe cảm nhận của riêng Suika thôi nhé——\\nSự khác biệt lớn nhất giữa đường sắt Hinomoto và đường sắt Trọng Quốc là gì vậy?」 | 「Chị muốn nghe cảm nhận của riêng Suika thôi nhé——\\nSự khác biệt lớn nhất giữa đường sắt Hinomoto và đường sắt Trung Quốc là gì vậy?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1346 | 「理解しました。それは確かに悪手ですね。\\n仲国でも、露見すれば反発されることは必至です」 | 「我明白了，這樣做的確不好，就算在仲國，一旦被揭穿也肯定會招來人們的反感」 | 「Tôi hiểu rồi. Đó quả thực là một nước đi tồi.\\nỞ Trọng Quốc cũng vậy, nếu bị lộ chắc chắn sẽ vấp phải sự phản đối gay gắt.」 | 「Tôi hiểu rồi. Đó quả thực là một nước đi tồi.\\nỞ Trung Quốc cũng vậy, nếu bị lộ chắc chắn sẽ vấp phải sự phản đối gay gắt.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1385 | 「仲国の古文にある言葉です。\\n『物事をその成立から遡り突き詰める』的な意味です」 | 「是一句仲國的古文。“事無大小，悉究本末”的意思」 | 「Đó là một từ trong cổ văn của Trọng Quốc.\\nNó mang ý nghĩa 'truy tìm nguồn gốc và đi sâu vào bản chất của sự việc'.」 | 「Đó là một từ trong cổ văn của Trung Quốc.\\nNó mang ý nghĩa 'truy tìm nguồn gốc và đi sâu vào bản chất của sự việc'.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1629 | 「なら僕たちが次に視察するべきは、\\n『仲国国鉄の現状そのもの』かな？　どう思う？　双鉄」 | 「那我們接下來該考察的，就是“仲國國鐵的現狀本身”了吧？你覺得呢，雙鐵？」 | 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trọng Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」 | 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trung Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1634 | 「まさしく、今の仲国国鉄が担っている実需が根こそぎ\\n奪われるでしょう。西瓜はそれを懸念しています」 | 「那無疑會動搖到如今仲國國鐵所肩負的剛需的根基。西瓜擔心的就是這一點」 | 「Chắc chắn, nhu cầu thực tế mà Đường sắt Quốc gia Trọng Quốc đang đảm nhận hiện nay sẽ bị cướp mất tận gốc rễ.\\nSuika đang rất lo ngại về điều đó.」 | 「Chắc chắn, nhu cầu thực tế mà Đường sắt Quốc gia Trung Quốc đang đảm nhận hiện nay sẽ bị cướp mất tận gốc rễ.\\nSuika đang rất lo ngại về điều đó.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1638 | 「なら、西瓜君。仲国国鉄が、鉄道存続のために\\nまっさきに為すべきことは、なんだと思う？」 | 「那西瓜你覺得，仲國國鐵為確保鐵路的存續，該做的最首當其衝的是什麼？」 | 「Vậy thì Suika. Em nghĩ Đường sắt Quốc gia Trọng Quốc,\\nviệc đầu tiên cần làm để duy trì sự tồn tại của đường sắt là gì?」 | 「Vậy thì Suika. Em nghĩ Đường sắt Quốc gia Trung Quốc,\\nviệc đầu tiên cần làm để duy trì sự tồn tại của đường sắt là gì?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1682 | 「ＯＫ。じゃ、もう少しだけ質問させて？　今度は逆に、\\n日ノ本と仲国の鉄道で、同じだと感じるところは？」 | 「ＯＫ。那我再多問一點囉，這次反過來問，日本和仲國的鐵路，有哪些地方感覺是一樣的？」 | 「OK. Vậy cho chị hỏi thêm một chút nữa nhé? Lần này ngược lại,\\nem cảm thấy điểm giống nhau giữa đường sắt Hinomoto và Trọng Quốc là gì?」 | 「OK. Vậy cho chị hỏi thêm một chút nữa nhé? Lần này ngược lại,\\nem cảm thấy điểm giống nhau giữa đường sắt Hinomoto và Trung Quốc là gì?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### lr稀咲追加03_新事業案.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1029 | 「いや本当に豪快だね！　――ああ、けど、うん。\\n食べて供養っていう考えは、多分仲国にもあるのかな」 | 「哎呀，果真是豪爽！哦，不過也對，也許在仲國也有以食表達感激的風俗」 | 「Chà, hào sảng thật đấy! ——À, nhưng mà, ừm.\\nTư tưởng ăn để cúng dường, chắc ở Trọng Quốc cũng có nhỉ.」 | 「Chà, hào sảng thật đấy! ——À, nhưng mà, ừm.\\nTư tưởng ăn để cúng dường, chắc ở Trung Quốc cũng có nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1170 | 「羊料理ひとつとっても、仲国各地で、\\nさぞさまざまなバリエーションがあるのだろうな」 | 「想必在仲國，即便同樣是羊肉，在不同地區也有著截然不同的菜式吧」 | 「Chỉ riêng món thịt cừu thôi, ở các vùng khác nhau của Trọng Quốc,\\nchắc hẳn cũng có vô vàn biến tấu khác nhau nhỉ.」 | 「Chỉ riêng món thịt cừu thôi, ở các vùng khác nhau của Trung Quốc,\\nchắc hẳn cũng có vô vàn biến tấu khác nhau nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1394 | 「さてどうでしょう。少なくとも私は理解できますが、\\nなにせ仲国は広いですから」 | 「這可很難說，雖然我能理解這種文化，但仲國畢竟地大物博」 | 「Chuyện đó thì sao nhỉ. Ít nhất là tôi có thể hiểu được,\\nnhưng dù sao thì Trọng Quốc cũng rộng lớn lắm mà.」 | 「Chuyện đó thì sao nhỉ. Ít nhất là tôi có thể hiểu được,\\nnhưng dù sao thì Trung Quốc cũng rộng lớn lắm mà.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1706 | 西瓜が画面を示してくれる。仲国語が読めずとも、\\n意味するところはアイコンから、何となく伝わってくる。 | 西瓜把手機拿給我們看，即便我看不懂仲文，單看圖示也能大概猜出是什麼意思。 | Suika đưa màn hình cho chúng tôi xem. Dù không đọc được tiếng Trọng Quốc,\\nnhưng tôi vẫn có thể lờ mờ hiểu được ý nghĩa thông qua các biểu tượng. | Suika đưa màn hình cho chúng tôi xem. Dù không đọc được tiếng Trung Quốc,\\nnhưng tôi vẫn có thể lờ mờ hiểu được ý nghĩa thông qua các biểu tượng. | JP 仲国語; “tiếng Trọng Quốc” → “tiếng Trung Quốc” (dạng “tiếng Trung Quốc” đã giữ ở 4 dòng 仲国06). |

### れいな03_しゅっぱつしんこう.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2070 | 言われれば、学園で昔習ったことを思い出す。\\n[ちゅうごく,1]仲国からの鉄鉱石と、築豊炭田の石炭と。 | 她這麼一說，我回想起了過去在學校裡學過的知識。 | Nghe vậy, tôi nhớ lại những gì từng học ở trường.\\nQuặng sắt từ nước Chukoku và than đá từ mỏ than Chikuho. | Nghe vậy, tôi nhớ lại những gì từng học ở trường.\\nQuặng sắt từ nước Trung Quốc và than đá từ mỏ than Chikuho. | JP [ちゅうごく,1]仲国; VN roman hoá furigana “Chukoku” → “nước Trung Quốc” (TW bỏ hẳn tên nước; JP thắng TW). |

### 仲国02_北琴の鉄道.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1651 | 「『仲国視察と、仲国版ナインスターズに関する立案』\\n……その理由を探すこともまた、視察の一部なのですね」 | 「“前往仲國考察，以及草擬仲國版九星的設計方案”……看來找出更深層次的原因也是考察的目的之一啊」 | 「『Khảo sát Zhongguo và lập kế hoạch cho Nine Stars phiên bản Zhongguo』\\n……Việc tìm ra lý do cho yêu cầu đó cũng là một phần của cuộc khảo sát nhỉ.」 | 「『Khảo sát Trung Quốc và lập kế hoạch cho Nine Stars phiên bản Trung Quốc』\\n……Việc tìm ra lý do cho yêu cầu đó cũng là một phần của cuộc khảo sát nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1678 | 「……ああ、さすが仲国は広大なのですね。\\n候補だけでも多すぎて、わたくし、目がまわりそうです」 | 「……噢噢，切身感受到仲國的地大物博了。選擇實在太多，我已經感到眼花撩亂」 | 「……Oa, Zhongguo quả thực rộng lớn quá nhỉ.\\nChỉ nghe danh sách ứng cử viên thôi mà tôi đã thấy chóng mặt rồi.」 | 「……Oa, Trung Quốc quả thực rộng lớn quá nhỉ.\\nChỉ nghe danh sách ứng cử viên thôi mà tôi đã thấy chóng mặt rồi.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1703 | 「その更に三倍、か。しかも仲国は広大だ。\\n同クラスの空港も、恐らく複数箇所あるのだろう」 | 「……這裡直接是日本的三倍嗎。而且仲國幅員遼闊，同樣等級的機場恐怕也不止一處吧」 | 「……Gấp ba lần chỗ đó sao. Hơn nữa Zhongguo lại vô cùng rộng lớn.\\nNhững sân bay cùng đẳng cấp chắc hẳn cũng có không ít đâu nhỉ.」 | 「……Gấp ba lần chỗ đó sao. Hơn nữa Trung Quốc lại vô cùng rộng lớn.\\nNhững sân bay cùng đẳng cấp chắc hẳn cũng có không ít đâu nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2073 | 「仲国は、この緑。車輌更新があってもずっと変わらない、\\nまさしく、仲国国鉄の伝統色です！」 | 「仲國就是這一抹綠色，即便車輛進行了翻新也從不改變。說這是仲國國鐵的傳統顏色毫不為過！」 | 「Zhongguo chính là màu xanh lá này. Dù có đổi mới toa xe thì vẫn luôn không đổi,\\nquả thực, đây chính là màu sắc truyền thống của Đường sắt Quốc gia Zhongguo!」 | 「Trung Quốc chính là màu xanh lá này. Dù có đổi mới toa xe thì vẫn luôn không đổi,\\nquả thực, đây chính là màu sắc truyền thống của Đường sắt Quốc gia Trung Quốc!」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2074 | 「我が仲国は総人口13億強の巨大国家です。\\n北琴空港の年間利用客数も、1億人を優に超えます」 | 「仲國是擁有超過１３億人口的巨大國家。僅以北琴機場為例，每年的旅客吞吐量就輕鬆超過一億人次」 | 「Zhongguo của chúng tôi là một quốc gia khổng lồ với dân số hơn 1,3 tỷ người.\\nChỉ tính riêng lượng hành khách qua sân bay Beiqin hàng năm cũng đã dễ dàng vượt mức 100 triệu người rồi.」 | 「Trung Quốc của chúng tôi là một quốc gia khổng lồ với dân số hơn 1,3 tỷ người.\\nChỉ tính riêng lượng hành khách qua sân bay Beiqin hàng năm cũng đã dễ dàng vượt mức 100 triệu người rồi.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2075 | 「すごかね、仲国の鉄道」 | 「仲國鐵路真厲害呀」 | 「Đường sắt của Zhongguo tuyệt thật đấy.」 | 「Đường sắt của Trung Quốc tuyệt thật đấy.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2175 | 「日ノ本と、帝鉄とは――まったく別の選択をして。\\nまったく別の鉄路が――仲国では伸び、生きたのですね」 | 「和帝國鐵路選擇了完全不同的方向。在仲國生龍活虎地延伸著的，已是和日本完全不同的鐵路了」 | 「Hinomoto và Đường sắt Teitetsu——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」 | 「Hinomoto và Đường sắt Teitetsu——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Trung Quốc nhỉ.」 | Chỉ đổi “Zhongguo”. REBASE (§0d): old_vn đã gồm fix đợt set2 T3 (“Đường sắt Hoàng gia” → “Đường sắt Teitetsu”); đợt này giữ “Teitetsu”, không đụng. |
| 2237 | 「あ、そこ！　そこももちろん見てみたかとよ。\\n仲国の鉄道について、ザラっとでも勉強したかけん」 | 「啊，那裡好！那裡當然也得去！早就想了解一下仲國鐵路的知識咧」 | 「A, chỗ đó! Tất nhiên là em cũng muốn đi xem chỗ đó rồi.\\nEm muốn học hỏi thêm về đường sắt của Zhongguo, dù chỉ là sơ qua.」 | 「A, chỗ đó! Tất nhiên là em cũng muốn đi xem chỗ đó rồi.\\nEm muốn học hỏi thêm về đường sắt của Trung Quốc, dù chỉ là sơ qua.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2259 | 「仲国には、さらに特快の上の列車種別もあります。\\n直達特快――Zhi－da Te－kuai。これが最速のZ列車です」 | 「在仲國，還有一種位居特快之上的列車。直達特快——Ｚｈｉ－ｄａ　Ｔｅ－ｋｕａｉ，就是最快的Ｚ列車了」 | 「Ở Zhongguo, còn có loại tàu cao cấp hơn cả Đặc khoái nữa.\\nĐó là Trực đạt đặc khoái——Zhi-da Te-kuai. Đây là tàu chữ Z nhanh nhất!」 | 「Ở Trung Quốc, còn có loại tàu cao cấp hơn cả Đặc khoái nữa.\\nĐó là Trực đạt đặc khoái——Zhi-da Te-kuai. Đây là tàu chữ Z nhanh nhất!」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2265 | 「仲国では、駅施設は保安の対象となるのです。\\n外国人が写真撮影をすると、身体検査をされかねません」 | 「在我們仲國，車站設施也屬於安保對象，要是外國人在這裡拍照，有可能會被搜身」 | 「Ở Zhongguo, các cơ sở nhà ga là đối tượng được bảo vệ an ninh.\\nNếu người nước ngoài chụp ảnh, rất có thể sẽ bị kiểm tra thân thể đấy.」 | 「Ở Trung Quốc, các cơ sở nhà ga là đối tượng được bảo vệ an ninh.\\nNếu người nước ngoài chụp ảnh, rất có thể sẽ bị kiểm tra thân thể đấy.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2352 | 「西瓜の知る全ての仲国の鉄道駅には、\\n入場券というシステムがありません」 | 「就西瓜所知，全仲國的火車站，都不賣所謂門票的」 | 「Trong tất cả các nhà ga đường sắt ở Zhongguo mà Suika biết,\\nkhông có hệ thống vé vào cửa đâu.」 | 「Trong tất cả các nhà ga đường sắt ở Trung Quốc mà Suika biết,\\nkhông có hệ thống vé vào cửa đâu.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2354 | 「西瓜の知る範囲で、仲国には、日ノ本的な『小さな駅』。\\n改札とホームのみといった構造の駅は存在しません」 | 「就西瓜所知，在仲國並沒有日本那種，只設有檢票口和站台的“小站”」 | 「Trong phạm vi hiểu biết của Suika, ở Zhongguo không tồn tại những 『nhà ga nhỏ』 mang phong cách Hinomoto.\\nTức là những nhà ga chỉ có cấu trúc gồm cổng soát vé và sân ga.」 | 「Trong phạm vi hiểu biết của Suika, ở Trung Quốc không tồn tại những 『nhà ga nhỏ』 mang phong cách Hinomoto.\\nTức là những nhà ga chỉ có cấu trúc gồm cổng soát vé và sân ga.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2401 | 「わたくしは――もしも仲国で蒸気機関車が現役ならば、\\nそのこにあってみたいです」 | 「我……如果仲國還有投入使用的蒸汽機車，我想去見一見」 | 「Tôi——nếu ở Zhongguo vẫn còn đầu máy hơi nước đang hoạt động,\\nthì tôi muốn đi xem đứa bé đó ạ.」 | 「Tôi——nếu ở Trung Quốc vẫn còn đầu máy hơi nước đang hoạt động,\\nthì tôi muốn đi xem đứa bé đó ạ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2462 | 「はい！　西瓜もわかりやすいと思います。\\n仲国でも快速は快速。発音は『Kuai－su』ですから」 | 「是的！西瓜也覺得很直觀。仲國的快速和日文文字相同，讀作“Ｋｕａｉ－ｓｕ”」 | 「Vâng! Suika cũng thấy rất dễ hiểu.\\nỞ Zhongguo, tàu nhanh cũng là tàu nhanh. Phát âm là 『Kuai-su』 mà.」 | 「Vâng! Suika cũng thấy rất dễ hiểu.\\nỞ Trung Quốc, tàu nhanh cũng là tàu nhanh. Phát âm là 『Kuai-su』 mà.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2481 | 「ものがあります。仲国鉄道歴史館という施設が、\\n北琴の郊外に存在しています」 | 「有的，名字叫仲國鐵路博物館，就位於北琴近郊」 | 「Có một nơi như vậy ạ. Có một cơ sở tên là Bảo tàng Lịch sử Đường sắt Zhongguo,\\nnằm ở vùng ngoại ô Beiqin.」 | 「Có một nơi như vậy ạ. Có một cơ sở tên là Bảo tàng Lịch sử Đường sắt Trung Quốc,\\nnằm ở vùng ngoại ô Beiqin.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2582 | 「素敵なデザインと褒めてもらって西瓜は嬉しいです！\\n[ｌｕ－ｂｉ－ｃｈｅ,2]緑比車――[りょくひしゃ,2]緑比車は、仲国の鉄道の象徴です！」 | 「能在外觀上得到讚揚，西瓜好高興！[ｌü－ｐｉ－ｃｈｅ,2]綠比車可是仲國鐵路的象徵呢！」 | 「Được khen là thiết kế tuyệt đẹp, Suika vui lắm!\\nLü-pi-che——Lục Bỉ Xa là biểu tượng của đường sắt Zhongguo đấy!」 | 「Được khen là thiết kế tuyệt đẹp, Suika vui lắm!\\nLü-pi-che——Lục Bỉ Xa là biểu tượng của đường sắt Trung Quốc đấy!」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2611 | 「西瓜の専門は仲国国鉄の線路がつながっている範囲です。\\nその地域外のことは要悉究。少し調べる必要があります」 | 「西瓜對仲國國鐵線路所到之處自然是了如指掌，但除此之外就尚待悉究，需要做一番調查了」 | 「Chuyên môn của Suika là trong phạm vi các tuyến đường sắt quốc gia Zhongguo được kết nối.\\nNhững khu vực ngoài đó thì cần phải tất cứu. Cần phải điều tra một chút ạ.」 | 「Chuyên môn của Suika là trong phạm vi các tuyến đường sắt quốc gia Trung Quốc được kết nối.\\nNhững khu vực ngoài đó thì cần phải tất cứu. Cần phải điều tra một chút ạ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2679 | 「保安員さんは、仲国国鉄のための仕事をしています。\\nだから事情の説明には、制服がとても役にたちました」 | 「這位保全也是在為仲國國鐵盡心盡力。所以在解釋情況的時候，這身制服就具備莫大的份量」 | 「Nhân viên an ninh đang làm việc cho Đường sắt Quốc gia Zhongguo.\\nNên bộ đồng phục này đã giúp ích rất nhiều trong việc giải thích tình hình.」 | 「Nhân viên an ninh đang làm việc cho Đường sắt Quốc gia Trung Quốc.\\nNên bộ đồng phục này đã giúp ích rất nhiều trong việc giải thích tình hình.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2687 | 「仲国の人が、北琴から何泊かの旅行にいく！\\nみたいなとき、メジャーな旅先ってどこですか？」 | 「這樣問好了，在“要從北琴出去玩幾天！”的時候，仲國人大多選擇去哪裡旅行呢？」 | 「Khi người Zhongguo đi du lịch vài ngày từ Beiqin!\\nNhững lúc như thế, điểm đến phổ biến nhất là ở đâu ạ?」 | 「Khi người Trung Quốc đi du lịch vài ngày từ Beiqin!\\nNhững lúc như thế, điểm đến phổ biến nhất là ở đâu ạ?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2715 | 「ならば別方面から考えてみよう。ハチロクは、\\n仲国で乗りたい列車や、見たい列車などはあるか？」 | 「那就換個思路吧。八六你有想在仲國乘坐，或是親眼看一看的列車嗎？」 | 「Vậy thì hãy thử suy nghĩ từ một khía cạnh khác xem sao. Hachiroku,\\ncô có chuyến tàu nào muốn đi, hay muốn xem ở Zhongguo không?」 | 「Vậy thì hãy thử suy nghĩ từ một khía cạnh khác xem sao. Hachiroku,\\ncô có chuyến tàu nào muốn đi, hay muốn xem ở Trung Quốc không?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2731 | 「それでは西瓜はみなさんを、北琴駅――\\n仲国最大のターミナル駅に、ご案内します！」 | 「那西瓜就帶大家去北琴站——仲國最大的總站！」 | 「Vậy thì Suika sẽ dẫn mọi người đến ga Beiqin——\\nga đầu mối lớn nhất của Zhongguo!」 | 「Vậy thì Suika sẽ dẫn mọi người đến ga Beiqin——\\nga đầu mối lớn nhất của Trung Quốc!」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2897 | おっと、仲国語だ。 | 他們的對話突然切換成了仲文。 | Ôi chà, là tiếng Zhongguo. | Ôi chà, là tiếng Trung. | JP 仲国語 → “tiếng Trung” (QĐ T56: chỉ 2 dòng “tiếng Zhongguo” đổi sang “tiếng Trung”). |
| 2920 | たとえ機関車の新規開発が長期に渡り止まっていようと、\\n仲国には、日ノ本における大廃線はなかったと―― | 儘管新型機車的開發工作已經長期停擺，仲國卻並未發生像日本國那樣的大廢線—— | Cho dù việc phát triển đầu máy mới đã bị đình trệ trong một thời gian dài,\\nnhưng ở Zhongguo, không hề có cuộc đại bãi bỏ các tuyến đường sắt như ở Hinomoto—— | Cho dù việc phát triển đầu máy mới đã bị đình trệ trong một thời gian dài,\\nnhưng ở Trung Quốc, không hề có cuộc đại bãi bỏ các tuyến đường sắt như ở Hinomoto—— | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2996 | 仲国版のナインスターズ計画の草案を立案できたなら、\\nその経験は、必ず御一夜鉄道に……も……？ | 如果能成功擬定仲國版九星的設計方案的話，這過程中積累的經驗，想必也能對御一夜鐵路—— | Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……? | Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Trung Quốc,\\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……? | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 3074 | きっぷ売り場で受けた警告を思い出す。\\n“駅施設は、仲国では保安の対象”であるのなら―― | 我想到剛才在售票廳的經歷，如果“車站在仲國屬於安保對象”—— | Tôi chợt nhớ lại lời cảnh báo đã nhận được ở khu vực bán vé.\\nNếu "cơ sở nhà ga là đối tượng được bảo vệ an ninh ở Zhongguo" thì—— | Tôi chợt nhớ lại lời cảnh báo đã nhận được ở khu vực bán vé.\\nNếu "cơ sở nhà ga là đối tượng được bảo vệ an ninh ở Trung Quốc" thì—— | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 3268 | 言って、志寰君は制帽の中央に輝いている、\\n仲国国鉄のマークを指差す。 | 邊說，志寰邊指著制帽正中閃閃發光的仲國國鐵標誌。 | Nói rồi, Zhihuan chỉ vào biểu tượng của Đường sắt Quốc gia Zhongguo\\nđang tỏa sáng ở chính giữa chiếc mũ đồng phục. | Nói rồi, Zhihuan chỉ vào biểu tượng của Đường sắt Quốc gia Trung Quốc\\nđang tỏa sáng ở chính giữa chiếc mũ đồng phục. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 3281 | なにがあったかと顔を向ければ、西瓜の方へ、制服姿\\n――仲国国鉄の制服姿の――青年が小走りに駆けてくる。 | 順著西瓜的目光看去，一位身著制服——身著仲國國鐵制服的青年正朝我們小跑過來。 | Khi tôi quay mặt lại xem có chuyện gì, thì thấy một thanh niên mặc đồng phục\\n——đồng phục của Đường sắt Quốc gia Zhongguo——đang chạy chậm về phía Suika. | Khi tôi quay mặt lại xem có chuyện gì, thì thấy một thanh niên mặc đồng phục\\n——đồng phục của Đường sắt Quốc gia Trung Quốc——đang chạy chậm về phía Suika. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### 仲国03_北琴鉄道歴史館.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1556 | 「『だから』。仲国国鉄は、[せんよんひゃくさんじゅうごみりき,6]1435mm軌――\\n標準軌を選択したのですか？」 | 「“正因如此”，仲國國鐵才選擇了１４３５ｍｍ軌距的標準軌嗎？」 | 「『Vì vậy』. Đường sắt Quốc gia Zhongguo,\\nđã chọn khổ 1435mm——khổ tiêu chuẩn sao?」 | 「『Vì vậy』. Đường sắt Quốc gia Trung Quốc,\\nđã chọn khổ 1435mm——khổ tiêu chuẩn sao?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1878 | 「旧[まんてつ,1]漫鉄で働いた後――\\n仲国国鉄でも活躍をしたのですね、このこは？」 | 「也就是說，她在前南曼鐵路服役之後，還在仲國國鐵大顯身手過囉？」 | 「Sau khi làm việc ở Đường sắt Nam Man cũ——\\nĐứa bé này cũng đã hoạt động tích cực ở Đường sắt Quốc gia Zhongguo nhỉ?」 | 「Sau khi làm việc ở Đường sắt Nam Man cũ——\\nĐứa bé này cũng đã hoạt động tích cực ở Đường sắt Quốc gia Trung Quốc nhỉ?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1882 | 「と、仲国国鉄も見込み、発展を期待していたそうです。\\nけれど、大廃線が全てを大きく狂わせてしまった」 | 「仲國國鐵似乎也意識到了這一點，並靜待其發展成熟。但突如其來的大廢線，徹底打亂了全盤計劃」 | 「Đường sắt Quốc gia Zhongguo cũng đã dự đoán và kỳ vọng vào sự phát triển đó.\\nNhưng cuộc Đại bãi bỏ các tuyến đường sắt đã làm đảo lộn mọi thứ.」 | 「Đường sắt Quốc gia Trung Quốc cũng đã dự đoán và kỳ vọng vào sự phát triển đó.\\nNhưng cuộc Đại bãi bỏ các tuyến đường sắt đã làm đảo lộn mọi thứ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2055 | 「父は、仲国国鉄を支えるべき次期機関車の、\\n開発・選定に深く関わった、試験機関士でした」 | 「家父是與仲國國鐵下一代主力機車開發、選型密切相關的試車員」 | 「Cha tôi là một người lái tàu thử nghiệm,\\nđã tham gia sâu vào việc phát triển và lựa chọn đầu máy thế hệ tiếp theo để hỗ trợ Đường sắt Quốc gia Zhongguo.」 | 「Cha tôi là một người lái tàu thử nghiệm,\\nđã tham gia sâu vào việc phát triển và lựa chọn đầu máy thế hệ tiếp theo để hỗ trợ Đường sắt Quốc gia Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2083 | 「老師は、帝鉄を大いにライバル視して研究していました。\\n老師だけでなく、私、西瓜も――仲国国鉄全体も」 | 「師父是將帝國鐵路視為一大勁敵而對其加以研究的。而且不僅是師父，我——西瓜，還有仲國國鐵所有人也都是」 | 「Sư phụ đã nghiên cứu Đường sắt Teitetsu với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」 | 「Sư phụ đã nghiên cứu Đường sắt Teitetsu với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Trung Quốc cũng vậy.」 | Chỉ đổi “Zhongguo”. REBASE (§0d): old_vn đã gồm fix đợt set2 T3 (“Đường sắt Hoàng gia” → “Đường sắt Teitetsu”); đợt này giữ “Teitetsu”, không đụng. |
| 2132 | 「はじめての、仲国の列車。Z49列車。\\n[こうがしゃ,2]硬臥車……三段寝台をお手配いただけたのですね」 | 「我們即將初次乘坐的仲國的列車，Ｚ４９次列車，硬臥車……應我們的要求安排了三層床鋪車廂的車票啊」 | 「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」 | 「Chuyến tàu đầu tiên ở Trung Quốc. Tàu Z49.\\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2225 | 「そうです。一度は廃棄寸前にまで傷んだものの、\\n仲国建国一周年を記念して修復され、再度活躍しました」 | 「正是如此。該車曾嚴重受損，差點遭到廢棄處理，但趕上仲國建國一周年而得以修復，再次活躍在鐵軌上」 | 「Đúng vậy. Dù từng bị hư hỏng đến mức suýt bị vứt bỏ,\\nnhưng nó đã được phục hồi để kỷ niệm một năm thành lập Zhongguo, và lại tiếp tục hoạt động.」 | 「Đúng vậy. Dù từng bị hư hỏng đến mức suýt bị vứt bỏ,\\nnhưng nó đã được phục hồi để kỷ niệm một năm thành lập Trung Quốc, và lại tiếp tục hoạt động.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2251 | 「かつての帝鉄は――少なくとも仲国国鉄の創設期には、\\nライバル視されるに足る存在であったのか」 | 「當年的帝國鐵路——至少在仲國國鐵創設之初，絕對是一個值得被視為勁敵的存在」 | 「Đường sắt Teitetsu ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」 | 「Đường sắt Teitetsu ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Trung Quốc,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」 | Chỉ đổi “Zhongguo”. REBASE (§0d): old_vn đã gồm fix đợt set2 T3 (“Đường sắt Hoàng gia” → “Đường sắt Teitetsu”); đợt này giữ “Teitetsu”, không đụng. |
| 2331 | 「なぜかを西瓜は説明します。国繋号が繋ぐ二つの国と国。\\nそれは、仲国と日ノ本のことだからです」 | 「西瓜這就為您說明。國系號所聯繫的，是兩個國家——仲國和日本國」 | 「Suika sẽ giải thích lý do tại sao. Hai quốc gia mà Quốc Hệ hiệu kết nối.\\nĐó chính là Zhongguo và Hinomoto.」 | 「Suika sẽ giải thích lý do tại sao. Hai quốc gia mà Quốc Hệ hiệu kết nối.\\nĐó chính là Trung Quốc và Hinomoto.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2384 | 「この歴史館には、[おおさか,1]逢坂で作られた蒸気機関車もいます。\\n仲国と日ノ本のレールは、かつては繋がっていたんです」 | 「這座歷史博物館裡還有大阪生產的蒸汽機車。過去仲國和日本的軌道是有過緊密聯繫的」 | 「Trong bảo tàng lịch sử này, còn có những đầu máy hơi nước được chế tạo ở Osaka nữa.\\nĐường ray của Zhongguo và Hinomoto, trước đây từng được kết nối với nhau đấy.」 | 「Trong bảo tàng lịch sử này, còn có những đầu máy hơi nước được chế tạo ở Osaka nữa.\\nĐường ray của Trung Quốc và Hinomoto, trước đây từng được kết nối với nhau đấy.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2592 | 西瓜がどれほど仲国を、日ノ本を、大事に想って\\nくれているのかが、伝わってくる気さえする。 | 仲國，以及日本國在西瓜心中究竟有著怎樣的分量，在適才的一言一行中，體現得淋漓盡致。 | Tôi thậm chí còn cảm nhận được Suika\\ntrân trọng Zhongguo, trân trọng Hinomoto đến nhường nào. | Tôi thậm chí còn cảm nhận được Suika\\ntrân trọng Trung Quốc, trân trọng Hinomoto đến nhường nào. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2641 | 仲国に来てからのハチロクが、\\nときおりにじませる口惜しさ。 | 到仲國以後，八六話語中不時顯現出絲絲憾意。 | Kể từ khi đến Zhongguo, Hachiroku\\nthỉnh thoảng lại bộc lộ sự tiếc nuối. | Kể từ khi đến Trung Quốc, Hachiroku\\nthỉnh thoảng lại bộc lộ sự tiếc nuối. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2642 | 旧漫州鉄道――というか旧漫州国は、\\n日ノ本と仲国とが相争ったあの\\x%l大戦;#00ffc040;大戦%l;#;の要因のひとつだ。 | 前南曼鐵路——準確說是前曼州國，說來也是當年日本國與仲國之間那場\\x%l大戦;#00ffc040;大戰%l;#;的核心因素之一。 | Đường sắt Nam Man cũ——hay đúng hơn là Manzhouguo cũ,\\nlà một trong những nguyên nhân dẫn đến \\x%l大戦;#00ffc040;Đại chiến%l;#; giữa Hinomoto và Zhongguo. | Đường sắt Nam Man cũ——hay đúng hơn là Manzhouguo cũ,\\nlà một trong những nguyên nhân dẫn đến \\x%l大戦;#00ffc040;Đại chiến%l;#; giữa Hinomoto và Trung Quốc. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2845 | おっと、電話か。\\n姜さんは早口の仲国語でなにやら――っ！ | 真不巧，正趕上有電話進來。姜小姐以很快的語速用仲文和對方交流著。 | Ôi chà, có điện thoại.\\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——Ư! | Ôi chà, có điện thoại.\\nCô Jiang đang nói gì đó bằng tiếng Trung với tốc độ rất nhanh——Ư! | JP 仲国語 → “tiếng Trung”. Chỉ đổi cụm ngôn ngữ; giữ nguyên “——Ư!” cuối dòng (không đụng dòng gasp). |
| 2849 | 西瓜の言葉と、この歴史館に収蔵されている、\\n仲国国鉄ごく初期の、日ノ本製造の\\x%l蒸機;#00ffc040;蒸機%l;#;たち。 | 結合西瓜所講，以及那些藏於這座博物館的仲國國鐵草創期時，曾使用的日本國產\\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;。 | Lời nói của Suika, và những chiếc \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; do Hinomoto sản xuất từ thời kỳ đầu\\ncủa Đường sắt Quốc gia Zhongguo đang được lưu giữ trong bảo tàng lịch sử này. | Lời nói của Suika, và những chiếc \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; do Hinomoto sản xuất từ thời kỳ đầu\\ncủa Đường sắt Quốc gia Trung Quốc đang được lưu giữ trong bảo tàng lịch sử này. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2944 | これでいい。仲国に来てからずうっと、どこかギクシャク不安定だったハチロクに、ようやく一本の芯が通った。 | 這樣就好。出發來中國之後一直不太對勁的八六總算又調整對了狀態。 | Thế này là được rồi. Hachiroku, người luôn có chút gượng gạo và bất ổn kể từ khi đến Zhongguo,\\ncuối cùng cũng đã tìm lại được trục cốt lõi của mình. | Thế này là được rồi. Hachiroku, người luôn có chút gượng gạo và bất ổn kể từ khi đến Trung Quốc,\\ncuối cùng cũng đã tìm lại được trục cốt lõi của mình. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### 仲国04_z49列車.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1392 | 「……よく描けているな。楽しげだ。\\n旅に出る前の空気感は、日ノ本も仲国も変わらんな」 | 「……畫得不錯啊，歡欣雀躍的感覺撲面而來。果然出發旅行前的氣氛，仲日兩國並無二致」 | 「……Vẽ đẹp lắm. Rất có hồn.\\nBầu không khí trước khi khởi hành cho một chuyến đi, dù là Hinomoto hay Zhongguo thì cũng không khác biệt mấy nhỉ.」 | 「……Vẽ đẹp lắm. Rất có hồn.\\nBầu không khí trước khi khởi hành cho một chuyến đi, dù là Hinomoto hay Trung Quốc thì cũng không khác biệt mấy nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1671 | 「ハチロク。車掌さんの業務内容は、\\n仲国も日ノ本も同じではないかと僕は思うぞ？」 | 「八六，要說列車長的工作內容，我覺得仲日兩國應該並無二致吧？」 | 「Hachiroku. Công việc của người trưởng tàu,\\ntôi nghĩ ở Zhongguo và Hinomoto cũng giống nhau thôi, đúng không?」 | 「Hachiroku. Công việc của người trưởng tàu,\\ntôi nghĩ ở Trung Quốc và Hinomoto cũng giống nhau thôi, đúng không?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1829 | 「うふふ、日ノ本と仲国と。\\n両方のサアビスのいいとこどりでございますね」 | 「嘻嘻，這是對仲日兩國的服務各取所長呀」 | 「Ufufu, Hinomoto và Zhongguo.\\nĐây là sự kết hợp những điểm tốt nhất trong dịch vụ của cả hai bên nhỉ.」 | 「Ufufu, Hinomoto và Trung Quốc.\\nĐây là sự kết hợp những điểm tốt nhất trong dịch vụ của cả hai bên nhỉ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1857 | 「早く食べたいな。あの、姜さん。\\n仲国では、食事の開始のときにはどのように」 | 「好想趕快嚐嚐啊。話說，姜小姐，在仲國，開始用餐之前有什麼習慣嗎」 | 「Muốn ăn quá đi. À, cô Jiang này.\\nỞ Zhongguo, khi bắt đầu bữa ăn mọi người thường làm thế nào vậy?」 | 「Muốn ăn quá đi. À, cô Jiang này.\\nỞ Trung Quốc, khi bắt đầu bữa ăn mọi người thường làm thế nào vậy?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2131 | 「食堂車のことを、仲国では[ｃａｎｃｈｅ,1]餐車。[さんしゃ,1]餐車といいます。\\n晩餐の餐という文字を書きますね」 | 「餐車在仲文裡讀作[ｃａｎｃｈｅ,1]餐車。餐就是晚餐的那個餐字」 | 「Ở Zhongguo, toa ăn được gọi là \\x%lｃａｎｃｈｅ;#00ffc040;Can-che%l;#;. \\x%lさんしゃ;#00ffc040;Xan-chơ%l;#;.\\nĐược viết bằng chữ "Xan" trong bữa tối (Vãn xan) đấy ạ.」 | 「Ở Trung Quốc, toa ăn được gọi là \\x%lｃａｎｃｈｅ;#00ffc040;Can-che%l;#;. \\x%lさんしゃ;#00ffc040;Xan-chơ%l;#;.\\nĐược viết bằng chữ "Xan" trong bữa tối (Vãn xan) đấy ạ.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### 仲国08_謝謝再見！.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1086 | 「――日ノ本のナインスターズの“その先”を、\\n仲国では進める必要がありますか」 | 「——你們在日本國為九星所描繪的“將來”，在仲國也同樣有推行的必要啊」 | 「——"Tương lai" của Nine Stars ở Hinomoto,\\ncó cần thiết phải thúc đẩy ở Trọng Quốc không?」 | 「——"Tương lai" của Nine Stars ở Hinomoto,\\ncó cần thiết phải thúc đẩy ở Trung Quốc không?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1149 | 「……この芭岩鉄道の、昔のきっぷを模したメモ帳や、\\n仲国国鉄マークのピンバッチなどが良い参考になるかと」 | 「……芭岩鐵路這個仿造復古車票樣式的筆記本，還有這個仲國國鐵標誌的胸章，感覺都是不錯的樣本」 | 「……Cuốn sổ tay mô phỏng vé tàu ngày xưa của Đường sắt Bayan này,\\nvà huy hiệu cài áo hình logo đường sắt quốc gia Trọng Quốc có lẽ sẽ là tài liệu tham khảo tốt.」 | 「……Cuốn sổ tay mô phỏng vé tàu ngày xưa của Đường sắt Bayan này,\\nvà huy hiệu cài áo hình logo đường sắt quốc gia Trung Quốc có lẽ sẽ là tài liệu tham khảo tốt.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1428 | 「9,597,000[　　　　　２,1]km割ることの、36,750[　　　　　　２,1]km。\\n単純な面積比ですと、仲国は九洲の260倍強となります」 | 「一邊是九百五十九萬七千平方公里的仲國，一邊是三萬六千七百五十平方公里的九州，單就面積便相差兩百六十倍」 | 「9.597.000 km vuông chia cho 36.750 km vuông.\\nTính theo tỷ lệ diện tích đơn thuần, Trọng Quốc lớn hơn Kyushu khoảng 260 lần.」 | 「9.597.000 km vuông chia cho 36.750 km vuông.\\nTính theo tỷ lệ diện tích đơn thuần, Trung Quốc lớn hơn Kyushu khoảng 260 lần.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1473 | 「仲国国鉄が――老師や、志寰や、西瓜たち――\\nみんなが生み出し、守って育てた、西瓜たちの機関車が」 | 「仲國國鐵——老師和志寰，還有西瓜以及無數同志們——由大家創造、守護、培養起來的這型機車——」 | 「Đường sắt quốc gia Trọng Quốc——Lão sư, Zhihuan, và nhóm Suika——\\nĐầu máy của nhóm Suika, được mọi người tạo ra, bảo vệ và nuôi dưỡng.」 | 「Đường sắt quốc gia Trung Quốc——Lão sư, Zhihuan, và nhóm Suika——\\nĐầu máy của nhóm Suika, được mọi người tạo ra, bảo vệ và nuôi dưỡng.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1474 | 「仲国の平均的な大型連休は、7日が二回。\\n春節、つまり旧正月と、国慶節となります。ので――」 | 「仲國大多數人每年擁有兩次七天長假，春節，即舊曆正月，以及國慶節，因此——」 | 「Kỳ nghỉ dài ngày trung bình ở Trọng Quốc gồm hai đợt 7 ngày.\\nĐó là Lễ hội mùa xuân, tức là Tết Nguyên đán, và Quốc khánh. Vì vậy——」 | 「Kỳ nghỉ dài ngày trung bình ở Trung Quốc gồm hai đợt 7 ngày.\\nĐó là Lễ hội mùa xuân, tức là Tết Nguyên đán, và Quốc khánh. Vì vậy——」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1476 | 「しかし、今の仲国の若者にだと――\\nキャンペーンに興味をもってもらうことが難しそうです」 | 「但如今，想要通過活動吸引仲國年輕人的興趣恐怕並不容易」 | 「Nhưng, với giới trẻ Trọng Quốc hiện nay thì——\\ncó vẻ khó để khiến họ hứng thú với chiến dịch này.」 | 「Nhưng, với giới trẻ Trung Quốc hiện nay thì——\\ncó vẻ khó để khiến họ hứng thú với chiến dịch này.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1484 | 「御一夜鉄道だけでは足りない。日ノ本仲国、二つの国の、\\nより多くの知恵と技術の集積が必須となるでしょう」 | 「僅憑御一夜鐵路必然是不夠的，這需要將日本國與仲國兩個國家的眾多智慧與技術匯聚於一處才能實現」 | 「Chỉ Đường sắt Ohitoyo thôi thì không đủ. Sẽ cần phải tập hợp\\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trọng Quốc.」 | 「Chỉ Đường sắt Ohitoyo thôi thì không đủ. Sẽ cần phải tập hợp\\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1674 | 「ゆえ、九洲規模の範囲を切り取って旅しても、\\n『仲国のごく一部』を周遊することにしかなりません」 | 「因而，若是旅行範圍限定在九州規模，這樣的周遊線路，不過是“對仲國管中窺豹”而已」 | 「Vì vậy, dù có khoanh vùng một khu vực có quy mô bằng Kyushu để đi du lịch,\\nthì cũng chỉ là du lịch vòng quanh "một phần rất nhỏ của Trọng Quốc" mà thôi.」 | 「Vì vậy, dù có khoanh vùng một khu vực có quy mô bằng Kyushu để đi du lịch,\\nthì cũng chỉ là du lịch vòng quanh "một phần rất nhỏ của Trung Quốc" mà thôi.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1686 | 「日ノ本では新・幹線――標準軌の専用線を敷かねば\\nいけんばってん、仲国は最初から標準軌やけん」 | 「在日本國，新·幹線必須要鋪設專用的標準軌，但仲國打一開始就是標準軌了」 | 「Ở Hinomoto, Tân Cán Tuyến——phải trải đường ray chuyên dụng khổ tiêu chuẩn,\\nnhưng Trọng Quốc thì ngay từ đầu đã là khổ tiêu chuẩn rồi.」 | 「Ở Hinomoto, Tân Cán Tuyến——phải trải đường ray chuyên dụng khổ tiêu chuẩn,\\nnhưng Trung Quốc thì ngay từ đầu đã là khổ tiêu chuẩn rồi.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1693 | 「仲国の魅力を確かめ直す旅を通じて、仲国鉄路の魅力を。\\nひいては――仲国を旅する自分自身をも、再発見する」 | 「在重新體會仲國魅力的同時，也再次領略仲國鐵路，乃至仲國旅遊自身的魅力」 | 「Thông qua chuyến hành trình khẳng định lại sức hấp dẫn của Trọng Quốc, để cảm nhận sức hấp dẫn của đường sắt Trọng Quốc.\\nXa hơn nữa là——tái khám phá chính bản thân mình khi đi du lịch Trọng Quốc.」 | 「Thông qua chuyến hành trình khẳng định lại sức hấp dẫn của Trung Quốc, để cảm nhận sức hấp dẫn của đường sắt Trung Quốc.\\nXa hơn nữa là——tái khám phá chính bản thân mình khi đi du lịch Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1781 | 「僕らであれば将来的に。6つの地理大区全ての拠点駅\\n――仲国全土を6日間で周遊する列車をご提案できます」 | 「我們想要提出的，是將來最終實現在六天裡周遊六個地理大區全部據點車站的列車方案」 | 「Nếu là chúng tôi thì trong tương lai. Có thể đề xuất một chuyến tàu đi vòng quanh nhà ga cứ điểm của cả 6 đại khu địa lý\\n——toàn bộ Trọng Quốc trong 6 ngày.」 | 「Nếu là chúng tôi thì trong tương lai. Có thể đề xuất một chuyến tàu đi vòng quanh nhà ga cứ điểm của cả 6 đại khu địa lý\\n——toàn bộ Trung Quốc trong 6 ngày.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1782 | 「我々には\\x%l電車;#00ffc040;電車%l;#;特急\\x%lクハ26;#00ffc040;クハ26%l;#;があり。仲国国鉄には東富4Dと\\n標準軌、1435mm軌での列車運用の豊富な蓄積があります」 | 「我們有特快\\x%l電車;#00ffc040;電車%l;#;的\\x%lクハ26;#00ffc040;Ｋｕｈａ２６%l;#;，仲國國鐵有應用東富４Ｄ，以及標準軌１４３５毫米軌距列車的豐富經驗」 | 「Chúng tôi có \\x%lクハ26;#00ffc040;Kuha 26%l;#; tốc hành \\x%l電車;#00ffc040;tàu điện%l;#;. Còn đường sắt quốc gia Trọng Quốc có Dongfeng 4D\\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」 | 「Chúng tôi có \\x%lクハ26;#00ffc040;Kuha 26%l;#; tốc hành \\x%l電車;#00ffc040;tàu điện%l;#;. Còn đường sắt quốc gia Trung Quốc có Dongfeng 4D\\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1784 | 「わたくしたちは、仲国の広さをまず学び、\\n整頓しようと試みました」 | 「我們首先去了解仲國的廣闊，嘗試從中整理思路」 | 「Đầu tiên, chúng tôi tìm hiểu về sự rộng lớn của Trọng Quốc,\\nvà cố gắng sắp xếp lại.」 | 「Đầu tiên, chúng tôi tìm hiểu về sự rộng lớn của Trung Quốc,\\nvà cố gắng sắp xếp lại.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1800 | 「絵と物語を、現実の物と為す。日ノ本では雛衣、稀咲\\n真闇女士たちが果たしたことを、仲国では、きっと私が」 | 「我要將畫作與傳奇化為現實。在日本國經雛衣、稀咲以及真闇女士等實現的，我也一定會在仲國再現」 | 「Biến bức tranh và câu chuyện thành hiện thực. Những gì Hinai, Kisaki\\nvà cô Mayami đã hoàn thành ở Hinomoto, tôi chắc chắn sẽ làm được ở Trọng Quốc.」 | 「Biến bức tranh và câu chuyện thành hiện thực. Những gì Hinai, Kisaki\\nvà cô Mayami đã hoàn thành ở Hinomoto, tôi chắc chắn sẽ làm được ở Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1858 | 「ああ。確かにだ。共感を使い、仲国のレイルロオドと\\n――ハチロクはよく、交流し情報を集めてくれた」 | 「是啊，八六通過共鳴，從仲國的鐵路人偶那裡收集了相當多的訊息」 | 「Ừ. Đúng vậy. Bằng cách sử dụng cộng cảm, Hachiroku đã giao lưu\\nvà thu thập thông tin rất tốt từ các Railord của Trọng Quốc.」 | 「Ừ. Đúng vậy. Bằng cách sử dụng cộng cảm, Hachiroku đã giao lưu\\nvà thu thập thông tin rất tốt từ các Railord của Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1864 | 「ああ。ゆえ、その案は捨て。全く異なる区分を求めた。\\nすると『仲国地理大区』というのものがあると教わった」 | 「是的。所以我們也放棄了這個方案，轉而尋求其他的劃分方法。這時我們了解到了“仲國地理大區”的概念」 | 「Đúng vậy. Do đó, chúng tôi đã từ bỏ phương án đó. Và tìm kiếm một cách phân chia hoàn toàn khác.\\nThế là chúng tôi được biết đến khái niệm "Đại khu địa lý Trọng Quốc".」 | 「Đúng vậy. Do đó, chúng tôi đã từ bỏ phương án đó. Và tìm kiếm một cách phân chia hoàn toàn khác.\\nThế là chúng tôi được biết đến khái niệm "Đại khu địa lý Trung Quốc".」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1898 | 「『将来的な仲国国鉄の復権』にむけ――他にもご提言を\\nいただけそうかと、図々しくも感じてしまいますが」 | 「為了“將來仲國國鐵的復興”——恕我冒昧相問，諸位想必也另有方案吧」 | 「Hướng tới "sự phục hưng của đường sắt quốc gia Trọng Quốc trong tương lai"——tôi có chút trơ trẽn\\nkhi cảm thấy rằng, dường như các vị còn có đề xuất nào khác nữa.」 | 「Hướng tới "sự phục hưng của đường sắt quốc gia Trung Quốc trong tương lai"——tôi có chút trơ trẽn\\nkhi cảm thấy rằng, dường như các vị còn có đề xuất nào khác nữa.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1904 | 「物語に気づいてもらい、読んでもらうための絵を。\\nですので日々姫先生に、仲国でも描いていただきたい」 | 「為讓人能留意到這故事，能夠潛心閱讀，希望日日姬女士能夠揮筆繪下仲國的光明未來」 | 「Bức tranh để mọi người chú ý đến câu chuyện, và đọc nó.\\nVì vậy, tôi muốn cô Hibiki vẽ ở Trọng Quốc nữa.」 | 「Bức tranh để mọi người chú ý đến câu chuyện, và đọc nó.\\nVì vậy, tôi muốn cô Hibiki vẽ ở Trung Quốc nữa.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1908 | 「しかし――実際に来て、乗ってみて。\\n仲国の広大さが、周遊観光を困難にすると理解しました」 | 「然而真正踏上這土地，乘坐列車穿行其中，我才深刻理解了仲國的土地遼闊，導致周遊觀光難度極大」 | 「Nhưng——khi thực sự đến đây và đi thử.\\nTôi mới hiểu ra rằng sự rộng lớn của Trọng Quốc sẽ gây khó khăn cho việc du lịch vòng quanh.」 | 「Nhưng——khi thực sự đến đây và đi thử.\\nTôi mới hiểu ra rằng sự rộng lớn của Trung Quốc sẽ gây khó khăn cho việc du lịch vòng quanh.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1919 | 「数多瞬く星々だ。6つの仲国地理大区――\\nそれぞれに、すくなくとも十以上の星を散りばめたい」 | 「當然是滿天繁星。在六個仲國地理大區，各自散布下至少十顆以上的星星」 | 「Là vô số những vì sao lấp lánh. 6 đại khu địa lý Trọng Quốc——\\nTôi muốn rải ít nhất mười vì sao trở lên vào mỗi khu vực.」 | 「Là vô số những vì sao lấp lánh. 6 đại khu địa lý Trung Quốc——\\nTôi muốn rải ít nhất mười vì sao trở lên vào mỗi khu vực.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1920 | 「仲国を……発見する――\\n仲国の魅力を、再確認する？」 | 「發現……仲國——再一次，體會仲國的魅力？」 | 「Khám phá…… Trọng Quốc——\\nKhẳng định lại sức hấp dẫn của Trọng Quốc?」 | 「Khám phá…… Trung Quốc——\\nKhẳng định lại sức hấp dẫn của Trung Quốc?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 1965 | 「必ず実らせ、茂らせましょう。その根で、枝葉で、\\n仲国と日ノ本とを、それぞれの全土を巡らせましょう」 | 「茁壯成長，其根系枝葉，必將遍布仲日兩國」 | 「Nhất định sẽ đơm hoa kết trái, xum xuê cành lá. Bằng bộ rễ đó, bằng cành lá đó,\\nhãy để chúng lan tỏa khắp toàn bộ lãnh thổ của Trọng Quốc và Hinomoto.」 | 「Nhất định sẽ đơm hoa kết trái, xum xuê cành lá. Bằng bộ rễ đó, bằng cành lá đó,\\nhãy để chúng lan tỏa khắp toàn bộ lãnh thổ của Trung Quốc và Hinomoto.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2012 | 「標準軌完全電化による超高速鉄道を、\\n仲国に走らせるよう――おっしゃっているのですか？」 | 「讓全線電力化的超高速鐵路列車，在仲國的標準軌上馳騁嗎？」 | 「Thầy đang nói——sẽ cho chạy đường sắt siêu tốc\\nbằng cách điện khí hóa hoàn toàn khổ tiêu chuẩn ở Trọng Quốc sao?」 | 「Thầy đang nói——sẽ cho chạy đường sắt siêu tốc\\nbằng cách điện khí hóa hoàn toàn khổ tiêu chuẩn ở Trung Quốc sao?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2042 | 「それが、現時点での仲国国鉄の鉄路復権のために考えた、\\n僕たち、御一夜鉄道による提案の草稿となります」 | 「這就是現階段我們御一夜鐵路，就仲國國鐵復興所提出的方案草案」 | 「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohitoyo,\\nnhằm phục hưng đường sắt quốc gia Trọng Quốc ở thời điểm hiện tại.」 | 「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohitoyo,\\nnhằm phục hưng đường sắt quốc gia Trung Quốc ở thời điểm hiện tại.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2046 | 「環状線ですね。とても小さな。\\nけれど、日ノ本と仲国を繋ぐ、環状線」 | 「這是環線呀，一個小小的環線。但這環線，聯繫起了日本國與仲國」 | 「Là một tuyến đường vòng tròn nhỉ. Rất nhỏ.\\nNhưng, là tuyến đường vòng tròn kết nối Hinomoto và Trọng Quốc.」 | 「Là một tuyến đường vòng tròn nhỉ. Rất nhỏ.\\nNhưng, là tuyến đường vòng tròn kết nối Hinomoto và Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2050 | 「今回の視察で僕がまずまっさきに感じたのは、\\n『仲国の鉄道は生きている』ということでした」 | 「這次考察中，我首先認識到的是，“仲國的鐵路仍有勃勃生機”」 | 「Điều đầu tiên tôi cảm nhận được trong chuyến thị sát lần này,\\nđó là "đường sắt của Trọng Quốc vẫn đang sống".」 | 「Điều đầu tiên tôi cảm nhận được trong chuyến thị sát lần này,\\nđó là "đường sắt của Trung Quốc vẫn đang sống".」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2051 | 「フリーきっぷ……春節中は仲国国鉄乗り放題、的な？\\nそれは――そのきっぷも高価となりそうかと、西瓜は」 | 「通票……比如在春節期間可以自由乘坐仲國國鐵列車嗎？西瓜覺得這通票怕是價格不菲」 | 「Vé trọn gói…… kiểu như đi tàu quốc gia Trọng Quốc thoải mái trong dịp Lễ hội mùa xuân sao?\\nCái đó——Suika nghĩ vé đó có vẻ cũng sẽ rất đắt.」 | 「Vé trọn gói…… kiểu như đi tàu quốc gia Trung Quốc thoải mái trong dịp Lễ hội mùa xuân sao?\\nCái đó——Suika nghĩ vé đó có vẻ cũng sẽ rất đắt.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2071 | 「それでは仲国を代表する観光列車にはなりえませんし\\n仲国の皆さんのこころを繋ぐレールは、伸ばせません」 | 「那樣是無法成為代表仲國的觀光列車的，而聯繫起全仲國人民內心的鐵軌，也會無從鋪就」 | 「Như vậy thì không thể trở thành chuyến tàu du lịch đại diện cho Trọng Quốc được,\\nvà cũng không thể kéo dài tuyến đường ray kết nối trái tim của người dân Trọng Quốc.」 | 「Như vậy thì không thể trở thành chuyến tàu du lịch đại diện cho Trung Quốc được,\\nvà cũng không thể kéo dài tuyến đường ray kết nối trái tim của người dân Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2089 | 「双鉄先生の伸ばすレールは、歌い、物語るレールです。\\n私は仲国の鉄路の上にも、それを紡いで欲しかった」 | 「雙鐵先生所鋪下的鐵軌，織就歌謠，化作傳奇。我也想在仲國的鐵路上，織就同樣的輝煌」 | 「Đường ray mà thầy Soutetsu vươn dài, là đường ray biết hát, biết kể chuyện.\\nTôi cũng muốn dệt nên điều đó trên tuyến đường sắt của Trọng Quốc.」 | 「Đường ray mà thầy Soutetsu vươn dài, là đường ray biết hát, biết kể chuyện.\\nTôi cũng muốn dệt nên điều đó trên tuyến đường sắt của Trung Quốc.」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2422 | 仲国で僕らが学んだことと、みなの意見と、アイディアと。\\nそれらをまとめあげるのに、今までかかってしまったが。 | 在仲國的所見所聞所想，以及大家的意見和建議。我們將這一切進行整理匯總，一直忙到了現在。 | Những gì chúng tôi học được ở Trọng Quốc, cùng với ý kiến và ý tưởng của mọi người.\\nViệc tổng hợp lại tất cả những thứ đó đã tiêu tốn thời gian đến tận bây giờ. | Những gì chúng tôi học được ở Trung Quốc, cùng với ý kiến và ý tưởng của mọi người.\\nViệc tổng hợp lại tất cả những thứ đó đã tiêu tốn thời gian đến tận bây giờ. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2423 | 北琴鉄道博物館で目にした仲国国鉄路線図では、\\n紅港にも、鉄路は当然、繋がっているにもかかわらず。 | 在北琴的鐵路博物館曾看到過仲國國鐵的路線圖，在那上面，箱港自然也有與之相通的線路，但她卻一次都未曾得見。 | Dù trên bản đồ tuyến đường sắt quốc gia Trọng Quốc mà tôi thấy ở Bảo tàng Đường sắt Bắc Cầm,\\nđường sắt hiển nhiên cũng kết nối với Hồng Cảng. | Dù trên bản đồ tuyến đường sắt quốc gia Trung Quốc mà tôi thấy ở Bảo tàng Đường sắt Bắc Cầm,\\nđường sắt hiển nhiên cũng kết nối với Hồng Cảng. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2428 | 仲国を簡易的に描いた地図に、日々姫がさっと線を引く。 | 在簡單畫出的示意地圖上，日日姬橫拉了一條線。 | Trên bản đồ vẽ đơn giản Trọng Quốc, Hibiki nhanh chóng vạch một đường. | Trên bản đồ vẽ đơn giản Trung Quốc, Hibiki nhanh chóng vạch một đường. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2508 | 仲国を繋ぎ、仲国と日ノ本をもまた繋ぐ――\\nそうした列車の草案を、全力で提言するのみだ。 | 將仲國各地聯繫起來，將仲國與日本國聯繫起來——我們要做的就是全力完成這種列車的提案。 | Kết nối Trọng Quốc, và cũng kết nối Trọng Quốc với Hinomoto——\\nChúng tôi chỉ cần dốc toàn lực đề xuất một bản thảo cho chuyến tàu như vậy. | Kết nối Trung Quốc, và cũng kết nối Trung Quốc với Hinomoto——\\nChúng tôi chỉ cần dốc toàn lực đề xuất một bản thảo cho chuyến tàu như vậy. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2741 | 西北・華北・東北と、西南・中南・華東とに――\\n仲国全土が、南北二つに切り分けられる。 | 西北、華北和東北，西南、中南和華東——將仲國全境，以南北為界劃為兩大區域。 | Tây Bắc, Hoa Bắc, Đông Bắc và Tây Nam, Trung Nam, Hoa Đông——\\nToàn bộ Trọng Quốc được chia làm hai nửa Nam Bắc. | Tây Bắc, Hoa Bắc, Đông Bắc và Tây Nam, Trung Nam, Hoa Đông——\\nToàn bộ Trung Quốc được chia làm hai nửa Nam Bắc. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

### 稀咲h3_チャイナドレスでおもてなし.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1983 | 「かかわるというより、融資の主体となるはずだ。\\nもっとも今は仲国も、大廃線の嵐だけれども」 | 「不止是參加那麼簡單，而是融資的主體。現在仲國也掀起了廢線的潮流」 | 「Hơn cả liên quan, họ chắc chắn là chủ thể cấp vốn chính đấy.\\nMặc dù hiện tại Trọng Quốc cũng đang chìm trong cơn bão Đại bãi bỏ các tuyến đường sắt」 | 「Hơn cả liên quan, họ chắc chắn là chủ thể cấp vốn chính đấy.\\nMặc dù hiện tại Trung Quốc cũng đang chìm trong cơn bão Đại bãi bỏ các tuyến đường sắt」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2020 | 「仲国では、銀行も国営なのか」 | 「仲國的銀行也是國營的嗎」 | 「Ở Trọng Quốc, ngân hàng cũng là của nhà nước sao」 | 「Ở Trung Quốc, ngân hàng cũng là của nhà nước sao」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2230 | 「あー……これ、ちゃんと仲国で採寸して仕立てた、\\n本場の、本格的なヤツなんだ」 | 「啊……這是在仲國量身定做的，絕對原汁原味的旗袍」 | 「A…… bộ này, là đồ chính hiệu, được đo may đàng hoàng\\nở Trọng Quốc đấy」 | 「A…… bộ này, là đồ chính hiệu, được đo may đàng hoàng\\nở Trung Quốc đấy」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2455 | 「来客があるんだよ、[ちゅうごく,1]仲国から。父の古い友人の\\n娘さんなんだけどさ、随分気難しい方らしくてね」 | 「我有個來自仲國的客人，是父親老友的女兒，真的很不好相處」 | 「Em sắp có khách đến thăm, từ Trọng Quốc. Là con gái\\ncủa một người bạn cũ của bố em, nhưng có vẻ cô ấy là người khá khó tính」 | 「Em sắp có khách đến thăm, từ Trung Quốc. Là con gái\\ncủa một người bạn cũ của bố em, nhưng có vẻ cô ấy là người khá khó tính」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2489 | 「仲国の方の接待となると、\\nやはり、チャイナドレスを着たりするのか？」 | 「接待來自仲國的客人，肯定要穿旗袍吧？」 | 「Tiếp đón khách từ Trọng Quốc,\\nthì em sẽ mặc sườn xám sao?」 | 「Tiếp đón khách từ Trung Quốc,\\nthì em sẽ mặc sườn xám sao?」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2730 | 「本場の……仲国の一流の工房でお願いしたんだ」 | 「這是在仲國……一流服裝廠訂製的」 | 「Em đã đặt may ở…… một xưởng may hàng đầu tại Trọng Quốc đấy」 | 「Em đã đặt may ở…… một xưởng may hàng đầu tại Trung Quốc đấy」 | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 2972 | 反冥という政府方針もあってだろうか、\\n仲国のエアクラ本格化は日ノ本よりもかなり遅れた。 | 一部分是出於反冥的行政要求，仲國的民航業比日本晚了很久才走上正軌。 | Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\\nmà việc phổ biến Aircra ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều. | Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\\nmà việc phổ biến Aircra ở Trung Quốc diễn ra muộn hơn Hinomoto khá nhiều. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |
| 3324 | 日ノ本文化が、女性の曲線を隠すものなら、\\n仲国文化は、曲線を見せる文化なのだと。 | 日本文化中，女性的身體曲線是要遮掩的。而在仲國，曲線是要表現出來的。 | Nếu văn hóa Hinomoto là che giấu đi những đường cong của người phụ nữ,\\nthì văn hóa Trọng Quốc lại là văn hóa phô bày những đường cong ấy. | Nếu văn hóa Hinomoto là che giấu đi những đường cong của người phụ nữ,\\nthì văn hóa Trung Quốc lại là văn hóa phô bày những đường cong ấy. | JP 仲国 → chuẩn “Trung Quốc” (QĐ T56). |

## 2. T57 — 詠国 → “Anh Quốc” đứng riêng (5 dòng)

### ハチロク09_もくもくオリヴィ.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1848 | 「それもなかなか厳しいようだな。詠国で学んだ者は、\\n日ノ本の\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;技師にも多いそうだが……」 | 「恐怕外國希望也很渺茫。日本的\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;技工有很多都是留學英國的……」 | 「Chuyện đó có vẻ cũng khá khó khăn đấy. Những người từng học ở Vịnh Quốc,\\ntrong số các kỹ sư \\x%lレイルロオド;#00ffc040;Railord%l;#; của Hinomoto cũng có rất nhiều, nhưng mà……」 | 「Chuyện đó có vẻ cũng khá khó khăn đấy. Những người từng học ở Anh Quốc,\\ntrong số các kỹ sư \\x%lレイルロオド;#00ffc040;Railord%l;#; của Hinomoto cũng có rất nhiều, nhưng mà……」 | JP 詠国 đứng riêng → “Anh Quốc” (QĐ T57). |

### ハチロク10_旺宮鉄道歴史館.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1529 | 「……日ノ本の鉄道営業法は、\\n詠国を見本に作られているのですよね？　恐らく」 | 「……想必日本的鐵路運營法，也是仿照英國的法規制定的吧？」 | 「……Luật kinh doanh đường sắt của Hinomoto,\\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」 | 「……Luật kinh doanh đường sắt của Hinomoto,\\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Anh Quốc phải không?」 | Chỉ đổi “Eikoku (Anh Quốc)” → “Anh Quốc”. REBASE (§0d): old_vn đã gồm fix đợt set3 (“Hinamoto” → “Hinomoto”); đợt này giữ “Hinomoto”, không đụng. |

### 真闇03_ひとしずく.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1833 | 「[えいこく,1]詠国の、プレジデンツファインリカーさんて。\\n最低注文は何本からか問い合わせ」 | 「是英國的總統酒行。打來諮詢最少能訂購幾瓶的」 | 「Của hãng President Fine Liquor bên Eikoku (Vương quốc Anh).\\nHọ hỏi xem đơn hàng tối thiểu là từ bao nhiêu chai.」 | 「Của hãng President Fine Liquor bên Anh Quốc.\\nHọ hỏi xem đơn hàng tối thiểu là từ bao nhiêu chai.」 | JP 詠国 đứng riêng → “Anh Quốc” (QĐ T57). |
| 2533 | 時差が九時間だからええっと……\\n詠国は、まだ夜六時ということになる。 | 時差是九個小時……英國的話還只是傍晚六點。 | Chênh lệch múi giờ là chín tiếng, vậy thì……\\nBên Eikoku (Vương quốc Anh) mới chỉ sáu giờ tối thôi. | Chênh lệch múi giờ là chín tiếng, vậy thì……\\nBên Anh Quốc mới chỉ sáu giờ tối thôi. | JP 詠国 đứng riêng → “Anh Quốc” (QĐ T57). |

### 真闇h3_補習授業の廃校舎.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 3529 | 計ったように、蔵から声が響いてくる。\\nF・スコッティ。詠国産まれのレイルロオドだ。 | 正巧此時倉庫傳來了聲音。飛·蘇格闌，是詠國產的鐵路人偶。 | Như đã hẹn trước, từ trong xưởng rượu vang lên một giọng nói.\\nF. Scotty. Một Railord sinh ra ở Anh quốc. | Như đã hẹn trước, từ trong xưởng rượu vang lên một giọng nói.\\nF. Scotty. Một Railord sinh ra ở Anh Quốc. | JP 詠国 đứng riêng → “Anh Quốc” (QĐ T57). |

## 3. T58 — 次元流 → “Thị Hiện Lưu” (3 dòng)

### 凪ふかみ02_凪の大会初挑戦！.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2280 | 「そうばい！　壱刀流からバイ捨流ば産まれて、\\nそのバイ捨流からまた産まれたのが、[じげん,1]次元流ばい！！」 | 「是咧！　體舍流源自一刀流，後續還演變出了示現流咧！！」 | 「Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu,\\nrồi từ Thể Xá Lưu lại sinh ra Thứ Nguyên Lưu đó!!」 | 「Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu,\\nrồi từ Thể Xá Lưu lại sinh ra Thị Hiện Lưu đó!!」 | JP 次元流 [じげん,1]; TW 示現流 cả 3 dòng; 示現流 (Jigen-ryū) thật — lưu phái đặt tất cả vào nhát chém đầu tiên, đúng định nghĩa ở 2377 → “Thị Hiện Lưu”. |
| 2377 | 「一太刀で相手を倒す、っていうのに\\nすべてをかける剣術だよね？　[じげん,1]次元流」 | 「示現流就是在第一招傾盡全力，一擊斃敵的劍術流派，對吧？」 | 「Đó là môn kiếm thuật đặt cược tất cả\\nvào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thứ Nguyên Lưu ấy.」 | 「Đó là môn kiếm thuật đặt cược tất cả\\nvào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thị Hiện Lưu ấy.」 | JP 次元流 [じげん,1]; TW 示現流 cả 3 dòng; 示現流 (Jigen-ryū) thật — lưu phái đặt tất cả vào nhát chém đầu tiên, đúng định nghĩa ở 2377 → “Thị Hiện Lưu”. |
| 3109 | 次元流！　知ってる！！\\nわたし、薄い本で良く勉強してる！！ | 示現流！　這個我知道！！在小本子裡沒少見識！！ | Thứ Nguyên Lưu! Mình biết!!\\nMình hay học hỏi từ mấy cuốn doujinshi lắm!! | Thị Hiện Lưu! Mình biết!!\\nMình hay học hỏi từ mấy cuốn doujinshi lắm!! | JP 次元流 [じげん,1]; TW 示現流 cả 3 dòng; 示現流 (Jigen-ryū) thật — lưu phái đặt tất cả vào nhát chém đầu tiên, đúng định nghĩa ở 2377 → “Thị Hiện Lưu”. |

## 4. T59 — キルクイティウム → “Quirquitium” (1 dòng)

### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2458 | 「ええ。エアロ＝クラフテック機関の心臓部である、\\nキルクイティウムの精製には豊富な真水が必要ですから」 | 「嗯。要精煉空凝機引擎的心臟“鐶”必須要用到大量淡水」 | 「Vâng. Để tinh chế Circuithium, trái tim của động cơ Aero-Craftech,\\nthì cần một lượng lớn nước ngọt.」 | 「Vâng. Để tinh chế Quirquitium, trái tim của động cơ Aero-Craftech,\\nthì cần một lượng lớn nước ngọt.」 | JP キルクイティウム; 5/5 dòng 共通04 đã “Quirquitium” (audit) → thống nhất (QĐ T59). |

## 5. T60 — 頭取 → “Tổng giám đốc” (27 dòng)

### グランドリライト01_オール御一夜、成立ならず.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2523 | 「頭取としては、実現可能性に乏しいと？」 | 「您的意思是，從行長的角度看，認為這件事很難實現？」 | 「Với tư cách là Giám đốc ngân hàng, ngài cho rằng khả năng thực hiện được là rất thấp sao?」 | 「Với tư cách là Tổng giám đốc ngân hàng, ngài cho rằng khả năng thực hiện được là rất thấp sao?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### グランドリライト06_稀咲.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 3319 | 頭取ではなく、父さんと――\\n呼ばわる声に応じたように、一番奥の扉が開く。 | 稀咲喊的不是行長，而是爸爸——最裡面的門隨著話語聲打開了。 | Không phải là Chủ tịch, mà là Bố――\\nNhư để đáp lại tiếng gọi, cánh cửa trong cùng mở ra. | Không phải là Tổng giám đốc, mà là Bố――\\nNhư để đáp lại tiếng gọi, cánh cửa trong cùng mở ra. | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 3338 | 視線での僕の問いに応えて、稀咲が耳打ちしてくれる。\\n頭取ではなく、父さんと。 | 稀咲用目光回答我的疑問，在我耳邊輕聲說道。用的稱呼不是行長，而是爸爸。 | Đáp lại ánh mắt dò hỏi của tôi, Kisaki thì thầm vào tai.\\nKhông phải Chủ tịch, mà là Bố. | Đáp lại ánh mắt dò hỏi của tôi, Kisaki thì thầm vào tai.\\nKhông phải Tổng giám đốc, mà là Bố. | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### グランドリライト08_ふかみ.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2052 | 「ああ。元忠さんに隈銀頭取を追われるようなリスクを、\\n決して負わせてはならん」 | 「是啊，絕不能讓元忠先生承受被撤職的風險」 | 「Ừ. Tuyệt đối không được để ông Mototada\\nphải chịu rủi ro bị mất chức Giám đốc Ngân hàng Kumamoto.」 | 「Ừ. Tuyệt đối không được để ông Mototada\\nphải chịu rủi ro bị mất chức Tổng giám đốc Ngân hàng Kumamoto.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### ハチロク01_こんにちわ赤ちゃん.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1676 | 「……双鉄は頭取の扱いがとても上手いね。\\n当行各支店にも、一人ずつ双鉄を備えたいくらいだ」 | 「……雙鐵，你還真是會應付行長啊。我都想給每個支行配上一個你了」 | 「……Soutetsu đối phó với Giám đốc giỏi thật đấy.\\nĐến mức tôi muốn mỗi chi nhánh của ngân hàng chúng tôi đều có một Soutetsu luôn.」 | 「……Soutetsu đối phó với Tổng giám đốc giỏi thật đấy.\\nĐến mức tôi muốn mỗi chi nhánh của ngân hàng chúng tôi đều có một Soutetsu luôn.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 2138 | 「気がついていなかったのかい？　\\n今日の頭取は機嫌が最悪だった。財務省から」 | 「你難道沒注意到嗎？今天行長的心情可是糟得不行，因為財務省那邊——」 | 「Cậu không nhận ra sao?\\nHôm nay tâm trạng của Giám đốc cực kỳ tồi tệ. Từ lúc ở Bộ Tài chính về.」 | 「Cậu không nhận ra sao?\\nHôm nay tâm trạng của Tổng giám đốc cực kỳ tồi tệ. Từ lúc ở Bộ Tài chính về.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### ハチロク12_再開発.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2364 | 「行員レベルでは、誘致断念の空気が強めかな。\\nけど――頭取はまだ、\\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致を諦めてない」 | 「社員層面上基本都瀰漫著放棄落戶的氛圍。不過，行長本人還沒有放棄\\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶的方案」 | 「Ở cấp độ nhân viên thì bầu không khí từ bỏ việc mời gọi đang khá mạnh.\\nNhưng——Giám đốc vẫn chưa từ bỏ việc mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.」 | 「Ở cấp độ nhân viên thì bầu không khí từ bỏ việc mời gọi đang khá mạnh.\\nNhưng——Tổng giám đốc vẫn chưa từ bỏ việc mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 2874 | 父であり頭取である宝生元忠への対抗心、\\nそれも、恐らく、大いに影響しているのだろうと。 | 她對既是父親又是行長的寶生元忠的對抗心理，恐怕起到了莫大的作用。 | Tâm lý đối kháng với Houshou Mototada, người vừa là cha vừa là Giám đốc ngân hàng,\\ncó lẽ đã ảnh hưởng rất lớn đến cô ấy. | Tâm lý đối kháng với Houshou Mototada, người vừa là cha vừa là Tổng giám đốc ngân hàng,\\ncó lẽ đã ảnh hưởng rất lớn đến cô ấy. | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### ハチロク14_橋.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1731 | 「だからそれは整理して、落ち着いたときに聞いて欲しい。\\n娘ではなく、支店長として。父さんではなく、頭取に」 | 「所以這件事等我整理好思路，情緒穩定下來再來跟你說。以行長和支行行長，而不是父親和女兒的身份」 | 「Thế nên chuyện đó hãy để con sắp xếp lại, lúc nào bình tĩnh rồi con sẽ nói cho bố nghe.\\nKhông phải với tư cách con gái, mà là Giám đốc chi nhánh. Không phải nói với bố, mà là với Chủ tịch.」 | 「Thế nên chuyện đó hãy để con sắp xếp lại, lúc nào bình tĩnh rồi con sẽ nói cho bố nghe.\\nKhông phải với tư cách con gái, mà là Giám đốc chi nhánh. Không phải nói với bố, mà là với Tổng giám đốc.」 | JP có cả 支店長 (con gái) và 頭取 (bố). Chỉ đổi dạng 頭取 “Chủ tịch” → “Tổng giám đốc”; 支店長 “Giám đốc chi nhánh” giữ nguyên. |

### ハチロク15_家族.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1759 | 「[ほうしょうもとただ,3]宝生元忠……\\nやはり、[くまぎん,1]隈銀の頭取たる人物なのですね」 | 「寶生元忠……果然是堪當隈元銀行行長的人物啊」 | 「Houshou Mototada……\\nQuả nhiên là nhân vật xứng tầm Chủ tịch ngân hàng Kumagin nhỉ.」 | 「Houshou Mototada……\\nQuả nhiên là nhân vật xứng tầm Tổng giám đốc ngân hàng Kumagin nhỉ.」 | JP 隈銀の頭取. Đổi “Chủ tịch” → “Tổng giám đốc”; giữ “ngân hàng Kumagin” theo ngữ cảnh dòng (QĐ T60). |
| 2059 | 「[かね]金のことなら、無論、銀行は専門だろうが……\\n頭取ともなると違うな。これほど大きな絵を描けるとは」 | 「雖然知道銀行是金錢方面的專家……不過行長的眼光果然不凡，竟描繪出了如此廣闊的前景」 | 「Nếu nói về tiền bạc, tất nhiên ngân hàng là chuyên gia rồi……\\nNhưng ở tầm Chủ tịch thì đúng là khác biệt. Không ngờ ông ấy có thể vẽ ra một bức tranh lớn đến vậy.」 | 「Nếu nói về tiền bạc, tất nhiên ngân hàng là chuyên gia rồi……\\nNhưng ở tầm Tổng giám đốc thì đúng là khác biệt. Không ngờ ông ấy có thể vẽ ra một bức tranh lớn đến vậy.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### ポーレット09_ストーブ客車.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2131 | 「そして、無能な支店長とは違い。\\n有能な頭取は、国政レベルに働きかけられる」 | 「而與某個無能的支行長不同，優秀的行長，能從國家政策層面進行干涉」 | 「Và, khác với một giám đốc chi nhánh bất tài.\\nMột chủ tịch tài ba, có thể tác động đến cả cấp độ quốc gia.」 | 「Và, khác với một giám đốc chi nhánh bất tài.\\nMột tổng giám đốc tài ba, có thể tác động đến cả cấp độ quốc gia.」 | JP có cả 支店長 và 頭取. Chỉ đổi dạng 頭取 “chủ tịch” → “tổng giám đốc”; “giám đốc chi nhánh” (支店長) giữ nguyên. |
| 2161 | 「隈元銀行頭取――宝生元忠氏によるわけか」 | 「要由隈元銀行行長——寶生元忠先生來判斷嗎」 | 「Do chủ tịch Ngân hàng Kumamoto――ông Houshou Mototada quyết định sao.」 | 「Do tổng giám đốc Ngân hàng Kumamoto――ông Houshou Mototada quyết định sao.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 共通14_負債.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1112 | 「知らない仲でないなら畏まるな――と、\\nそうおっしゃったのは頭取ご自身ですが？」 | 「“既然認識就不要客氣”——這不是行長您自己說的嗎？」 | 「'Nếu không phải người dưng thì đừng có khách sáo'——\\nChẳng phải chính ngài chủ tịch đã nói vậy sao?」 | 「'Nếu không phải người dưng thì đừng có khách sáo'——\\nChẳng phải chính ngài tổng giám đốc đã nói vậy sao?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 1551 | 「おいおい御一夜支店長。\\n頭取に対し、『やめてくれないかな』は無いだろう」 | 「喂喂，御一夜支行長。對行長說話怎麼能用這種口氣呢」 | 「Này này giám đốc chi nhánh Ohitoyo.\\nNói với chủ tịch mà lại dùng từ 'được không' sao.」 | 「Này này giám đốc chi nhánh Ohitoyo.\\nNói với tổng giám đốc mà lại dùng từ 'được không' sao.」 | JP có cả 支店長 (御一夜支店長) và 頭取. Chỉ đổi dạng 頭取 “chủ tịch” → “tổng giám đốc”; “giám đốc chi nhánh Ohitoyo” giữ nguyên. |
| 1882 | 「これは頭取」\\n「仕事の邪魔はやめてくれないかな」 | 「行長您好」\\n「能不能不要妨礙我工作呀」 | 「Kính chào ngài chủ tịch.」\\n「Xin ông đừng làm phiền công việc của tôi được không.」 | 「Kính chào ngài tổng giám đốc.」\\n「Xin ông đừng làm phiền công việc của tôi được không.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 1884 | 「頭取？」 | 「行長？」 | 「Chủ tịch?」 | 「Tổng giám đốc?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 1972 | 「なら――頭取――\\n元忠さんは、汰斗さんの？」 | 「那麼，行長——元忠先生，您跟汰斗老爺是？」 | 「Vậy thì——chủ tịch——\\nÔng Mototada, có quan hệ thế nào với ông Taito?」 | 「Vậy thì——tổng giám đốc——\\nÔng Mototada, có quan hệ thế nào với ông Taito?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 2200 | ざっくばらんに、という頭取指示に、\\nある程度、浦上も寄せるつもりなのだろうか。 | 估計浦上也打算在一定程度上，遵從行長“直言不諱”的命令吧。 | Chỉ thị "cứ thẳng thắn đi" của chủ tịch,\\nphải chăng Urakami cũng định tuân theo ở một mức độ nào đó. | Chỉ thị "cứ thẳng thắn đi" của tổng giám đốc,\\nphải chăng Urakami cũng định tuân theo ở một mức độ nào đó. | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 2708 | 立場で人の何をはかれるわけでもないが――\\nそれにしたって、頭取がこれはあまりにも気さくにすぎる。 | 雖然不能用身份去衡量一個人——但是行長這個樣子，未免有些太平易近人了。 | Dù không thể đánh giá con người qua địa vị——\\nNhưng mà, một chủ tịch như thế này thì lại thân thiện quá mức rồi. | Dù không thể đánh giá con người qua địa vị——\\nNhưng mà, một tổng giám đốc như thế này thì lại thân thiện quá mức rồi. | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 日々姫01_リゾート食堂列車計画.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1805 | 「なるほどなるほど？　双鉄の頼み――じゃないね、\\n頭取の気まぐれが、偶然にも良く機能したわけだ」 | 「明白了。雙鐵的請求……不，行長的心血來潮偶爾也會帶來好處啊」 | 「Ra là vậy, ra là vậy? Lời nhờ vả của Soutetsu——không phải nhỉ,\\nsự bốc đồng của giám đốc ngân hàng tình cờ lại mang đến kết quả tốt đẹp.」 | 「Ra là vậy, ra là vậy? Lời nhờ vả của Soutetsu——không phải nhỉ,\\nsự bốc đồng của tổng giám đốc ngân hàng tình cờ lại mang đến kết quả tốt đẹp.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 1996 | 「それは――そうだね。単なる、頭取の気まぐれさ。\\nあの人が急に、僕のスケジュールを横取りしたから」 | 「那是因為——對了，只是行長心血來潮罷了。是他突然搶走了我原來的行程」 | 「Đó là——đúng rồi. Chỉ đơn giản là sự bốc đồng của giám đốc ngân hàng thôi.\\nVì người đó đột nhiên cướp mất lịch trình của tôi.」 | 「Đó là——đúng rồi. Chỉ đơn giản là sự bốc đồng của tổng giám đốc ngân hàng thôi.\\nVì người đó đột nhiên cướp mất lịch trình của tôi.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 日々姫06_日々姫の決断.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2897 | 「それはそーとね。稀咲ちゃんと双ちゃんが互角として、\\n頭取の宝生さんとウチとが、互角」 | 「那倒有得一拼。現在稀咲妹妹和小雙是不相上下，寶生行長和咱也是不相上下」 | 「Cái đó thì cũng phải xem đã. Cho là bé Kisaki và Sou-chan ngang tài ngang sức đi,\\nthì Giám đốc Houshou và chị cũng ngang ngửa nhau.」 | 「Cái đó thì cũng phải xem đã. Cho là bé Kisaki và Sou-chan ngang tài ngang sức đi,\\nthì Tổng giám đốc Houshou và chị cũng ngang ngửa nhau.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 真闇h3_補習授業の廃校舎.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2469 | 「宝生稀咲も賛同してくれている話らしい。\\n頭取――宝生元忠も巻き込めそうだと」 | 「寶生稀咲好像也贊成了。她還要把行長――寶生元忠也給拉進來呢」 | 「Nghe nói Houshou Kisaki cũng tán thành chuyện này.\\nCó vẻ như sẽ lôi kéo được cả Giám đốc――Houshou Mototada vào nữa.」 | 「Nghe nói Houshou Kisaki cũng tán thành chuyện này.\\nCó vẻ như sẽ lôi kéo được cả Tổng giám đốc――Houshou Mototada vào nữa.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 稀咲01_金と人.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1256 | 「……父と、頭取、どっちの立場で」 | 「……您是以什麼立場來說這句話的？是父親，還是行長？」 | 「……Bố đang nói với tư cách là Bố, hay là Chủ tịch vậy?」 | 「……Bố đang nói với tư cách là Bố, hay là Tổng giám đốc vậy?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |
| 1887 | 「父さ――と、頭取っ！？」 | 「爸——行、行長！？」 | 「Bố――à không, Chủ tịch!?」 | 「Bố――à không, Tổng giám đốc!?」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

### 稀咲h1_性生活.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1416 | 「いや、慣れっこさ。\\n双鉄は巻き込まれただけ。首謀者は父――頭取だ」 | 「沒事，我都習慣了。你只是被捲進來的，罪魁禍首是爸爸――行長」 | 「Không sao, em quen rồi.\\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」 | 「Không sao, em quen rồi.\\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」 | JP 頭取 (TW 行長 cả 29 dòng) = người điều hành ngân hàng → “Tổng giám đốc” (QĐ T60; tránh va chạm 会長→“Chủ tịch”, 社長→“giám đốc”). |

## 6. T61 — 持株会社 → “công ty holding” (7 dòng)

### れいな03_しゅっぱつしんこう.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1568 | 「矢幡製鉄所さんの呼びかけで、\\n持株会社形式で運営されることになるそうですよ」 | 「據說是在八幡煉鐵廠呼籲下建立，並由其作為控股公司主導運營」 | 「Theo lời kêu gọi của nhà máy luyện thép Yahata,\\nhọ sẽ hoạt động dưới hình thức công ty cổ phần đấy.」 | 「Theo lời kêu gọi của nhà máy luyện thép Yahata,\\nhọ sẽ hoạt động dưới hình thức công ty holding đấy.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |

### ハチロク09_採決.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1536 | 「……[だいきゅしゅう,2]大九洲ＳＬ構想を成立、発展させていくため。\\n持株会社は、なるほど、優れた仕組みなのですね」 | 「……我明白了。要想讓大九州蒸汽機車藍圖得以成立並發展壯大，控股公司確實是很合適的結構」 | 「……Để thiết lập và phát triển kế hoạch Đại Kyushu SL.\\nCông ty cổ phần, ra là vậy, đúng là một cơ cấu xuất sắc nhỉ.」 | 「……Để thiết lập và phát triển kế hoạch Đại Kyushu SL.\\nCông ty holding, ra là vậy, đúng là một cơ cấu xuất sắc nhỉ.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |
| 1549 | 「……まずは近県の鉄道会社との、持株会社の設立。か」 | 「……首先與鄰縣的鐵路公司成立控股公司嗎」 | 「……Trước tiên là thành lập một công ty cổ phần, với các công ty đường sắt ở các tỉnh lân cận. Sao.」 | 「……Trước tiên là thành lập một công ty holding, với các công ty đường sắt ở các tỉnh lân cận. Sao.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |
| 2131 | 「持株会社、とはどのようなものなのですか？」 | 「控股公司是指什麼呢？」 | 「Công ty cổ phần, là loại hình như thế nào vậy ạ?」 | 「Công ty holding, là loại hình như thế nào vậy ạ?」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |
| 2143 | 「経営の集約をしつつ独立性も維持できるのが持株会社だ。\\nそれは当然、第三、第四の企業の参入を促しやすくする」 | 「既能匯總經營，又能維持獨立性，這便是控股公司的特徵。當然也容易吸引第三、第四家企業的加入」 | 「Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty cổ phần.\\nĐiều đó đương nhiên, sẽ giúp dễ dàng thúc đẩy sự tham gia của các doanh nghiệp thứ ba, thứ tư.」 | 「Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty holding.\\nĐiều đó đương nhiên, sẽ giúp dễ dàng thúc đẩy sự tham gia của các doanh nghiệp thứ ba, thứ tư.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |
| 2189 | 「そこで、真闇姉を社長とする持株会社を、\\nそれぞれの酒蔵を束ねる、親会社として設立するのだ」 | 「此時，我們要讓真闇姐擔任社長的控股公司成為管理各個酒窖的母公司」 | 「Vì vậy, anh sẽ thành lập một công ty cổ phần do chị Mayami làm giám đốc,\\nvới tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại với nhau.」 | 「Vì vậy, anh sẽ thành lập một công ty holding do chị Mayami làm giám đốc,\\nvới tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại với nhau.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |

### ハチロク15_家族.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1953 | 「\\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の誘致を支援して、\\nかわりに、持株会社への参加を促す」 | 「聲援\\x%lエアクラ;#00ffc040;空凝機%l;#;工廠在當地落戶，作為交換，促進對股份公司的參股」 | 「Sẽ hỗ trợ thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\nđổi lại, thúc đẩy họ tham gia vào công ty cổ phần.」 | 「Sẽ hỗ trợ thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\nđổi lại, thúc đẩy họ tham gia vào công ty holding.」 | JP 持株会社 (TW 控股公司) = holding; “công ty cổ phần” = 株式会社, sai khái niệm → “công ty holding” (QĐ T61; tiền lệ audit ハチロク12). |

## 7. T63 — 帝有鉄道 → “Đường sắt Đế quốc Hinomoto” (4 dòng)

### 仲国03_北琴鉄道歴史館.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2082 | 「老師の日ノ本帝有鉄道――帝鉄への接し方は、\\n確かに研究でしたけれど、それだけでなく……ん……」 | 「師父對於帝家日本國鐵路——對於帝國鐵路確實是抱以研究的態度，不過不僅如此……嗯……」 | 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Teitetsu,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」 | 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế quốc Hinomoto——Đường sắt Teitetsu,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」 | CHỈ đổi nửa đầu: “Đường sắt Đế hữu Hinomoto” → “Đường sắt Đế quốc Hinomoto”. REBASE (§0d): nửa sau đã là “Đường sắt Teitetsu” nhờ fix đợt set2 T3 (không còn “Đường sắt Hoàng gia” nữa) — cờ F-T63-1 coi như đã xong qua set2; đợt này giữ “Teitetsu”. |
| 2248 | 「日ノ本帝有鉄道のオーナー、[ヒノモトノミカド,3]日ノ本帝から、\\nミカドって愛称になったと！？」 | 「由於帝家日本國鐵路的所有人是日本國[米卡多]帝，所以愛稱就叫“帝”了嗎！？」 | 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado),\\nđể đặt biệt danh là Mikado sao!?」 | 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế quốc Hinomoto, Hoàng đế Hinomoto (Mikado),\\nđể đặt biệt danh là Mikado sao!?」 | JP 日ノ本帝有鉄道 → “Đường sắt Đế quốc Hinomoto” (dạng đầy đủ đã chốt của 帝鉄; tiền lệ audit グランド10 1134). |

### 日々姫01_双鉄の妹.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1789 | 「『日ノ本帝有鐵道、蒸気機関車設計図面集』」 | 「《帝家日本國鐵路蒸汽機車設計圖集》」 | 「『Đường sắt Hoàng gia Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』」 | 「『Đường sắt Đế quốc Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』」 | JP 日ノ本帝有鉄道 → “Đường sắt Đế quốc Hinomoto” (dạng đầy đủ đã chốt của 帝鉄; tiền lệ audit グランド10 1134). |

### 日々姫02_文庫森.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 60 | \\x%l明智;#00ffc040;明智%l;#;三十九年。鉄道帝有法制定。布告。\\n日ノ本帝有鉄道発足。 | \\x%l明智;#00ffc040;明治%l;#;三十九年。鐵路國有法制定，頒布。帝家日本國鐵路成立。 | Năm \\x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\\nĐường sắt Hoàng gia Hinomoto chính thức ra đời. | Năm \\x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Đế quốc được ban hành. Công bố.\\nĐường sắt Đế quốc Hinomoto chính thức ra đời. | JP có cả 鉄道帝有法 và 日ノ本帝有鉄道: đổi cả hai — tên luật “Đạo luật Đường sắt Đế quốc” + tên công ty “Đường sắt Đế quốc Hinomoto”. |

## 8. T66 — 九国 → “chín tỉnh” (2 dòng)

### グランドリライト07_真闇.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2545 | 「ナインスターズは、九洲九国を九日間かけ、\\nゆったりと贅沢に周遊していく」 | 「按照我的想法，九星會耗時九天，奢華而悠閒地周遊九州九國」 | "「Nine Stars sẽ dành chín ngày để dạo quanh chín vùng Kyushu,\\nmột chuyến du ngoạn thong thả và xa hoa.」" | "「Nine Stars sẽ dành chín ngày để dạo quanh chín tỉnh Kyushu,\\nmột chuyến du ngoạn thong thả và xa hoa.」" | Giá trị CSV3/TOML có dấu `"` bao ngoài (nguyên văn); chỉ đổi “chín vùng” → “chín tỉnh”, giữ nguyên dấu `"` và `\n`. |
| 2546 | 「リレートレイン・ナインスターズ。\\n九洲九国を、九つの客室で周遊する観光列車」 | 「接力列車·九星。擁有九間客房，周遊九州九國的觀光列車」 | "「Relay Train Nine Stars (Chuyến tàu tiếp sức Chín Ngôi Sao).\\nChuyến tàu du lịch dạo quanh chín vùng Kyushu với chín khoang hành khách.」" | "「Relay Train Nine Stars (Chuyến tàu tiếp sức Chín Ngôi Sao).\\nChuyến tàu du lịch dạo quanh chín tỉnh Kyushu với chín khoang hành khách.」" | Giá trị CSV3/TOML có dấu `"` bao ngoài (nguyên văn); chỉ đổi “chín vùng” → “chín tỉnh”, giữ nguyên dấu `"` và `\n`. |

## 9. Đã kiểm chứng, giữ nguyên (không sửa) + cờ

### 9a. T56 — giữ 82 dòng (JP có 仲国, CUR đã đúng)

- **“Trung Quốc” 76 dòng** (gồm 4 dòng “tiếng Trung Quốc” ở 仲国06: 1008/1732/2237/2397 — nhất quán nội bộ file; và 仲国06 1872 “ngôn ngữ Hinomoto - Trung Quốc - Đức”): lr稀咲追加03 1101; lr稀咲追加h 1033; グランド08 1722 (audit — dòng tiền lệ 6 nước), 1997; グランド11 2173, 2432, 2798, 3797; 仲国01 1330/1365/1366/1385/1790/1847/1863/1885/1900/1938/1942/1943/1944/2035/2049/2072/2076/2079/2112/2143/2153/2185/2186/2203 (24 dòng — toàn file đã “Trung Quốc”); 仲国02 2278 (“Quốc vụ viện Trung Quốc” — cùng chức danh với lr稀咲追加01 1860 đã sửa, nay thống nhất); 仲国05 2183/2595/3089; 仲国06 1066/1068/1107/1575/1580/1611/1739/1764/1940/1994/2007/2032/2081/2434; 仲国07 889/952/1255/1265/1271/1331/1361/1364/1380/1390/1423/1502/1523/1565/1673/1721/1722/1743/1752/1900/2144 (21 dòng).
- **“tiếng Trung” 5 dòng:** 仲国01 1704/2511, 仲国05 2749, 仲国07 1887/1997 (“Tiếng Trung của cô hướng dẫn viên…” — 1997 viết hoa T đầu câu, vẫn là dạng đúng).
- **仲国06 1796:** JP 仲国国内, CUR “trong nước” — không nhắc tên nước, đúng, không đổi.

### 9b. T57 — giữ 11 dòng + 1 dòng ngoài tập JP 詠国

- **Dạng ghép/ngắn “Anh” 8 dòng (giữ theo QĐ):** ハチロク02 2254 “nước Anh”, 2766 “người Anh”; ハチロク03 1580/2437 “kiểu Anh”; ハチロク04 1533 “của Anh”; 凪ふかみ01 1587 “ở Anh”, 1818 “từ Anh”; グランド08 1722 “Anh” (trong list 6 nước — cùng dòng với tiền lệ T56).
- **Đã là “Anh Quốc” 2 dòng:** 真闇03 1662, 1905.
- **Lưu ý:** dòng giữ ハチロク03 1580 (“kiểu Anh”) cũng nằm trong file set2 — giá trị hiện tại của nó nay còn gồm fix T3 ở một chỗ khác trong dòng; phần “kiểu Anh” không bị đụng.
- **Ngoại lệ 1 — giữ nguyên 真闇03 1687:** dòng liệt kê song song 5 nước đều ở dạng hư cấu + gloss (“Eikoku (Vương quốc Anh), Frank (Pháp), Dokkoku (Đức), Rankoku (Hà Lan), Ispania (Tây Ban Nha)”); chỉ đổi một mục sẽ phá cấu trúc song song — cờ cho một quyết định chung về cả list sau này.
- **Ngoại lệ 2 — giữ nguyên ハチロク09 2102:** JP dùng katakana メーコク/エーコク (Olivy phát âm tên nước kiểu ngoại quốc), VN ghép cặp hư cấu + gloss cho CẢ HAI nước (“Minh Quốc (Mỹ) hay Vịnh Quốc (Anh)”); “Minh Quốc” đã chốt nên cặp này phải khớp nhau — đổi một bên sẽ lệch cặp. (Dòng katakana tương tự ハチロク10 2024 “Minh Quốc (Nước Mỹ)” củng cố mẫu này.)

### 9c. T59 — giữ 5 dòng

共通04_キハ07。ポーレットとれいな 2105/2240/2304/2520/2629 — đã “Quirquitium” 5/5 trong audit.

### 9d. T60 — giữ 2 dòng

共通11_経営資源 2696/3448 — đã “tổng giám đốc” (lần giới thiệu chính thức vai trò của Houshou Mototada).

### 9e. T61 — giữ 3 dòng + 6 dòng “công ty cổ phần” đúng nghĩa KHÔNG đụng

- **Đã là “công ty holding” 3 dòng (audit):** ハチロク12_再開発 1699/2258/2381.
- **6 dòng “công ty cổ phần” nhưng JP là 株式会社/（株）, KHÔNG phải 持株会社 — giữ nguyên:** 共通14 1744 (“株式会社化してからの分…”); ポーレット03 2010/2393 (“御一夜鉄道株式会社旅客営業規則” — 2010 đã qua đợt U1/U2, CUR “Đường sắt Ohitoyo”); ポーレット09 1709 (“株式会社形式での第三セクター”); ポーレット15 2457 (“（株）クマ川下り”), 2462 (“（株）御一夜ワークサービス”). Đây là bằng chứng phép quét ngược hoạt động: không phải cứ thấy “công ty cổ phần” là sửa.

### 9f. T63 — giữ 3 dòng

- グランド10 1134 — đã “Đường sắt Đế quốc Hinomoto” trong audit (tiền lệ cho cả mục).
- ハチロク03 2337, 日々姫02 1727 — JP 帝有化 (động từ quốc hữu hoá), CUR “quốc hữu hóa” đúng, không đổi.

### 9g. T66 — giữ 4 dòng

グランドリライト08_ふかみ 2496/2711, グランド11_ナインスターズ！ 2265/3231 — đã “chín tỉnh” 4/6.

### 9h. T62 / T64 / T65 — 0 dòng (đã kiểm chứng, giữ nguyên)

- **T62 民由連:** chỉ 1 dòng JP 民由連 toàn dự án — ハチロク09 2411, CUR “Đảng Dân Do” đã đúng (JP 民由 vs TW 民友 đồng âm; JP thắng TW).
- **T64 冥語:** chỉ 1 dòng — ハチロク05 3512 (list ghi nhầm “凪ふかみ05 3512”), CUR đã là “tiếng Minh Quốc” từ audit.
- **T65 橙汁:** 3 dòng đã đúng dạng theo quy tắc giữ-biến thể — 仲国01 1828/2089 “Trừng trấp” (dòng đùa về bao bì/chữ viết), 仲国08 2054 “nước cam” (yêu cầu thường).

### 9i. Cờ cho coordinator / batch khác

- **F-T56-1 — 仲国08_謝謝再見！ 2823 (KHÔNG sửa ở đây):** JP 「日仲のレールを繋ぐ」 (日仲 = Nhật–Trung, không phải thuật ngữ 仲国 đứng riêng), CUR “…kết nối tuyến đường ray giữa Hinomoto và Trọng Quốc.” Đây là dòng duy nhất còn “Trọng Quốc” sau đợt này mà JP không chứa 仲国. Đề nghị coordinator quyết: sửa nốt → “Trung Quốc” ở đợt vét (U15) cho thống nhất tuyệt đối, hay giữ vì ngoài phạm vi T56 theo nghĩa hẹp. (Không tự sửa vì brief buộc “chỉ sửa dòng có JP chứa thuật ngữ gốc”.)
- **F-T63-1 — ĐÃ XONG qua set2 (không còn là cờ mở):** nửa sau 仲国03 2082 (帝鉄 → “Đường sắt Hoàng gia”) đã được đợt set2 (T3) sửa thành “Đường sắt Teitetsu” trong lúc đợt này đang chạy; đợt này đã rebase lên giá trị đó và chỉ sửa nửa đầu (Đế hữu → Đế quốc) — xem §0d. Coordinator không cần kiểm tra U3 cho dòng này nữa.
- **F-T57-1 — ĐÃ XONG qua set3 (không còn là cờ mở):** “Hinamoto” ở ハチロク10 1529 đã được đợt set3 sửa thành “Hinomoto” trong lúc đợt này đang chạy; đợt này đã rebase lên giá trị đó và chỉ đổi phần Eikoku — xem §0d.
- **Đã biết, không phải cờ mới:** 5 dòng còn “Đường sắt Ohito” (ハチロク01 2467, ハチロク12 1900/2089, 日々姫08 3719, 真闇h3 2524) là phần việc U2c đã ghi trong ROUTE-UNIFICATION.md — không thuộc đợt này. Fix audit ở ハチロク12 2381 làm mất `\n` (TOML-2 flatten) — đã ghi từ E1, xem xét khi ráp TOML (không thuộc T61).

## Lượt soát 2 (second pass)

Đã đọc lại toàn bộ 171 dòng trong bảng (JP / TW / old_vn / fix) và đối chiếu từng khối TOML với JSON: **tổng 171 / tái kiểm chứng 171 / loại bỏ 0 / sửa lại 0 giá trị fix**. 1 hiệu đính duy nhất ở văn bản lý do (không phải giá trị fix): lý do dòng 凪ふかみ02 3109 ghi “[じげん,1]” trong khi JP dòng này không có furigana (chỉ 2280/2377 có) — đã sửa thành “không furigana ở dòng này”. Sau đó, 5 dòng rebase trên set2/set3 (§0d) được đọc lại toàn bộ (JP/TW/old_vn mới/fix mới) và toàn bộ kiểm chứng cơ học chạy lại trên map mới: kiểm tra ngược 171/171 (áp cặp thay thế ngược lên fix ra đúng `old_vn` — chứng minh mọi thay đổi chỉ nằm ở cặp thay thế đã khai); `old_vn` khớp map giá trị hiện tại (đã gồm set2/set3) 171/171; JP/TW khớp CSV3 good-set 171/171; khối TOML parse-verified bằng `tomllib` 33 file / 171 key, 171/171 khớp `fix` trong JSON; 0 trùng lặp (file,key); 6 dòng trùng đợt unification đã gộp (1689 U1a + 5 rebase set2/set3), `old_vn` của cả 6 đều là giá trị sau đợt đã gộp.

## Khối TOML (parse-verified: 33 file / 171 key)

Quy ước: literal backslash-n trong giá trị fix được viết `\\n` trong khối; `\x` trong tag `%l` được viết `\\x`. Đã parse bằng `tomllib` và đối chiếu từng giá trị với `fix` trong JSON — 171/171 khớp.

```toml
# lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml
[script]
"1689" = "「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Trung Quốc\\nđến thị sát Ohitoyo thông qua sự môi giới của Kisaki.」"
```

```toml
# lr稀咲追加01_仲国視察の誘い.txt.toml
[script]
"996" = "「Nếu chỉ xét riêng về quan hệ đối nhân xử thế, thì có lẽ là vậy.\\nDù sao cô ấy cũng là thư ký của Thứ trưởng Bộ Đường sắt Quốc vụ viện Trung Quốc mà.」"
"1068" = "「Hử? Một số doanh nghiệp đường sắt tức là……ngoài đường sắt quốc gia ra vẫn còn à.\\nỞ Trung Quốc cũng có……cái gọi là đường sắt dân sự, đường sắt tư nhân sao.」"
"1091" = "Từ anh Fuchi của Xe lửa Hinomoto, cho đến những kỹ sư hàng đầu\\nnhận được lời mời từ Trung Quốc, tôi đều nắm rõ một vài cái tên."
"1161" = "「Fufu, vẫn thích uống như ngày nào nhỉ.\\nCủa riêng mình nghĩa là――mang từ Trung Quốc sang sao?」"
"1182" = "Nhìn kỹ thì, cả bộ ấm chén và đĩa đều khác ngày thường, là đồ của Trung Quốc.\\nSự chu đáo tỉ mỉ này quả nhiên không hổ danh là cô ấy, khiến tôi một lần nữa phải thán phục."
"1511" = "「Chia sẻ dự án mới. Nếu đó là dự án có thể triển khai ở Trung Quốc,\\nchúng tôi mong muốn được xem xét việc cùng triển khai bằng một phương pháp nào đó.」"
"1563" = "Trung Quốc là quốc gia coi Minh Quốc là đối thủ rõ rệt. Vì vậy,\\nhọ đang cố gắng thiết lập một trục đối lập với việc thúc đẩy Aircra của Minh Quốc."
"1573" = "Kisaki lộ vẻ ngạc nhiên. Tết Nguyên Đán――Tết Âm lịch hình như,\\nlà dịp lễ hội lớn nhất ở Trung Quốc theo như tôi nghe được……"
"1716" = "「Nói vậy tức là, trong nội bộ Bộ Đường sắt của Quốc vụ viện Trung Quốc……sao.\\nThật vô cùng vinh hạnh. ――Hay đúng hơn là, rốt cuộc thì tại sao lại như vậy.」"
"1741" = "「Ngài Soutetsu, nếu ngài có hứng thú thì sao ạ.\\nBộ chúng tôi sẽ gửi lời mời, chuyến khảo sát Trung Quốc cùng cô Kisaki.」"
"1819" = "「Chắc cha em không thể đứng nhìn mãi được.\\nNên ông đã thuê một du học sinh từ Trung Quốc về làm gia sư cho em.」"
"1860" = "「Ngài là Soutetsu nhỉ. Rất hân hạnh được gặp.\\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trung Quốc, tên là Khương Diệp Hoàng.」"
```

```toml
# lr稀咲追加02_仲国視察.txt.toml
[script]
"1072" = "「Chuyến tàu có số lượng hành khách đi nhiều nhất ở Trung Quốc.\\nTôi muốn chúng tôi được đi chuyến tàu đó.」"
"1073" = "「Nguồn tin tức chính của giới trẻ Trung Quốc là ở đâu?\\nTôi nghĩ có rất nhiều nguồn như mạng internet, báo chí, TV v.v.」"
"1074" = "「Chị hiểu là ở Trung Quốc, tỷ lệ phổ cập của xe Aircra\\nvẫn chưa đến mức đó mà nhỉ?」"
"1077" = "「Tôi có cảm giác em rất đồng tình với điều này——\\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trung Quốc cũng giống như vậy sao?」"
"1153" = "「Hô. Vậy là em am hiểu cả đường sắt của Trung Quốc và Hinomoto sao.\\nThế thì thật là đáng tin cậy.」"
"1294" = "「Nguồn tin tức chính của giới trẻ là các trang tin tức,\\nSNS, trò chuyện nhóm. Stealth marketing ở Trung Quốc cũng gây phản cảm.」"
"1332" = "「Tôi cũng nghĩ hướng đó là tốt nhất. Vì vậy, trước tiên tôi muốn biết\\nđại đa số các cặp đôi trẻ ở Trung Quốc có sở thích như thế nào.」"
"1343" = "「Chị muốn nghe cảm nhận của riêng Suika thôi nhé——\\nSự khác biệt lớn nhất giữa đường sắt Hinomoto và đường sắt Trung Quốc là gì vậy?」"
"1346" = "「Tôi hiểu rồi. Đó quả thực là một nước đi tồi.\\nỞ Trung Quốc cũng vậy, nếu bị lộ chắc chắn sẽ vấp phải sự phản đối gay gắt.」"
"1385" = "「Đó là một từ trong cổ văn của Trung Quốc.\\nNó mang ý nghĩa 'truy tìm nguồn gốc và đi sâu vào bản chất của sự việc'.」"
"1629" = "「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trung Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」"
"1634" = "「Chắc chắn, nhu cầu thực tế mà Đường sắt Quốc gia Trung Quốc đang đảm nhận hiện nay sẽ bị cướp mất tận gốc rễ.\\nSuika đang rất lo ngại về điều đó.」"
"1638" = "「Vậy thì Suika. Em nghĩ Đường sắt Quốc gia Trung Quốc,\\nviệc đầu tiên cần làm để duy trì sự tồn tại của đường sắt là gì?」"
"1682" = "「OK. Vậy cho chị hỏi thêm một chút nữa nhé? Lần này ngược lại,\\nem cảm thấy điểm giống nhau giữa đường sắt Hinomoto và Trung Quốc là gì?」"
```

```toml
# lr稀咲追加03_新事業案.txt.toml
[script]
"1029" = "「Chà, hào sảng thật đấy! ——À, nhưng mà, ừm.\\nTư tưởng ăn để cúng dường, chắc ở Trung Quốc cũng có nhỉ.」"
"1170" = "「Chỉ riêng món thịt cừu thôi, ở các vùng khác nhau của Trung Quốc,\\nchắc hẳn cũng có vô vàn biến tấu khác nhau nhỉ.」"
"1394" = "「Chuyện đó thì sao nhỉ. Ít nhất là tôi có thể hiểu được,\\nnhưng dù sao thì Trung Quốc cũng rộng lớn lắm mà.」"
"1706" = "Suika đưa màn hình cho chúng tôi xem. Dù không đọc được tiếng Trung Quốc,\\nnhưng tôi vẫn có thể lờ mờ hiểu được ý nghĩa thông qua các biểu tượng."
```

```toml
# れいな03_しゅっぱつしんこう.txt.toml
[script]
"1568" = "「Theo lời kêu gọi của nhà máy luyện thép Yahata,\\nhọ sẽ hoạt động dưới hình thức công ty holding đấy.」"
"2070" = "Nghe vậy, tôi nhớ lại những gì từng học ở trường.\\nQuặng sắt từ nước Trung Quốc và than đá từ mỏ than Chikuho."
```

```toml
# グランドリライト01_オール御一夜、成立ならず.txt.toml
[script]
"2523" = "「Với tư cách là Tổng giám đốc ngân hàng, ngài cho rằng khả năng thực hiện được là rất thấp sao?」"
```

```toml
# グランドリライト06_稀咲.txt.toml
[script]
"3319" = "Không phải là Tổng giám đốc, mà là Bố――\\nNhư để đáp lại tiếng gọi, cánh cửa trong cùng mở ra."
"3338" = "Đáp lại ánh mắt dò hỏi của tôi, Kisaki thì thầm vào tai.\\nKhông phải Tổng giám đốc, mà là Bố."
```

```toml
# グランドリライト07_真闇.txt.toml
[script]
"2545" = "\"「Nine Stars sẽ dành chín ngày để dạo quanh chín tỉnh Kyushu,\\nmột chuyến du ngoạn thong thả và xa hoa.」\""
"2546" = "\"「Relay Train Nine Stars (Chuyến tàu tiếp sức Chín Ngôi Sao).\\nChuyến tàu du lịch dạo quanh chín tỉnh Kyushu với chín khoang hành khách.」\""
```

```toml
# グランドリライト08_ふかみ.txt.toml
[script]
"2052" = "「Ừ. Tuyệt đối không được để ông Mototada\\nphải chịu rủi ro bị mất chức Tổng giám đốc Ngân hàng Kumamoto.」"
```

```toml
# ハチロク01_こんにちわ赤ちゃん.txt.toml
[script]
"1676" = "「……Soutetsu đối phó với Tổng giám đốc giỏi thật đấy.\\nĐến mức tôi muốn mỗi chi nhánh của ngân hàng chúng tôi đều có một Soutetsu luôn.」"
"2138" = "「Cậu không nhận ra sao?\\nHôm nay tâm trạng của Tổng giám đốc cực kỳ tồi tệ. Từ lúc ở Bộ Tài chính về.」"
```

```toml
# ハチロク09_もくもくオリヴィ.txt.toml
[script]
"1848" = "「Chuyện đó có vẻ cũng khá khó khăn đấy. Những người từng học ở Anh Quốc,\\ntrong số các kỹ sư \\x%lレイルロオド;#00ffc040;Railord%l;#; của Hinomoto cũng có rất nhiều, nhưng mà……」"
```

```toml
# ハチロク09_採決.txt.toml
[script]
"1536" = "「……Để thiết lập và phát triển kế hoạch Đại Kyushu SL.\\nCông ty holding, ra là vậy, đúng là một cơ cấu xuất sắc nhỉ.」"
"1549" = "「……Trước tiên là thành lập một công ty holding, với các công ty đường sắt ở các tỉnh lân cận. Sao.」"
"2131" = "「Công ty holding, là loại hình như thế nào vậy ạ?」"
"2143" = "「Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty holding.\\nĐiều đó đương nhiên, sẽ giúp dễ dàng thúc đẩy sự tham gia của các doanh nghiệp thứ ba, thứ tư.」"
"2189" = "「Vì vậy, anh sẽ thành lập một công ty holding do chị Mayami làm giám đốc,\\nvới tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại với nhau.」"
```

```toml
# ハチロク10_旺宮鉄道歴史館.txt.toml
[script]
"1529" = "「……Luật kinh doanh đường sắt của Hinomoto,\\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Anh Quốc phải không?」"
```

```toml
# ハチロク12_再開発.txt.toml
[script]
"2364" = "「Ở cấp độ nhân viên thì bầu không khí từ bỏ việc mời gọi đang khá mạnh.\\nNhưng——Tổng giám đốc vẫn chưa từ bỏ việc mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;.」"
"2874" = "Tâm lý đối kháng với Houshou Mototada, người vừa là cha vừa là Tổng giám đốc ngân hàng,\\ncó lẽ đã ảnh hưởng rất lớn đến cô ấy."
```

```toml
# ハチロク14_橋.txt.toml
[script]
"1731" = "「Thế nên chuyện đó hãy để con sắp xếp lại, lúc nào bình tĩnh rồi con sẽ nói cho bố nghe.\\nKhông phải với tư cách con gái, mà là Giám đốc chi nhánh. Không phải nói với bố, mà là với Tổng giám đốc.」"
```

```toml
# ハチロク15_家族.txt.toml
[script]
"1759" = "「Houshou Mototada……\\nQuả nhiên là nhân vật xứng tầm Tổng giám đốc ngân hàng Kumagin nhỉ.」"
"1953" = "「Sẽ hỗ trợ thu hút nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\nđổi lại, thúc đẩy họ tham gia vào công ty holding.」"
"2059" = "「Nếu nói về tiền bạc, tất nhiên ngân hàng là chuyên gia rồi……\\nNhưng ở tầm Tổng giám đốc thì đúng là khác biệt. Không ngờ ông ấy có thể vẽ ra một bức tranh lớn đến vậy.」"
```

```toml
# ポーレット09_ストーブ客車.txt.toml
[script]
"2131" = "「Và, khác với một giám đốc chi nhánh bất tài.\\nMột tổng giám đốc tài ba, có thể tác động đến cả cấp độ quốc gia.」"
"2161" = "「Do tổng giám đốc Ngân hàng Kumamoto――ông Houshou Mototada quyết định sao.」"
```

```toml
# 仲国02_北琴の鉄道.txt.toml
[script]
"1651" = "「『Khảo sát Trung Quốc và lập kế hoạch cho Nine Stars phiên bản Trung Quốc』\\n……Việc tìm ra lý do cho yêu cầu đó cũng là một phần của cuộc khảo sát nhỉ.」"
"1678" = "「……Oa, Trung Quốc quả thực rộng lớn quá nhỉ.\\nChỉ nghe danh sách ứng cử viên thôi mà tôi đã thấy chóng mặt rồi.」"
"1703" = "「……Gấp ba lần chỗ đó sao. Hơn nữa Trung Quốc lại vô cùng rộng lớn.\\nNhững sân bay cùng đẳng cấp chắc hẳn cũng có không ít đâu nhỉ.」"
"2073" = "「Trung Quốc chính là màu xanh lá này. Dù có đổi mới toa xe thì vẫn luôn không đổi,\\nquả thực, đây chính là màu sắc truyền thống của Đường sắt Quốc gia Trung Quốc!」"
"2074" = "「Trung Quốc của chúng tôi là một quốc gia khổng lồ với dân số hơn 1,3 tỷ người.\\nChỉ tính riêng lượng hành khách qua sân bay Beiqin hàng năm cũng đã dễ dàng vượt mức 100 triệu người rồi.」"
"2075" = "「Đường sắt của Trung Quốc tuyệt thật đấy.」"
"2175" = "「Hinomoto và Đường sắt Teitetsu——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Trung Quốc nhỉ.」"
"2237" = "「A, chỗ đó! Tất nhiên là em cũng muốn đi xem chỗ đó rồi.\\nEm muốn học hỏi thêm về đường sắt của Trung Quốc, dù chỉ là sơ qua.」"
"2259" = "「Ở Trung Quốc, còn có loại tàu cao cấp hơn cả Đặc khoái nữa.\\nĐó là Trực đạt đặc khoái——Zhi-da Te-kuai. Đây là tàu chữ Z nhanh nhất!」"
"2265" = "「Ở Trung Quốc, các cơ sở nhà ga là đối tượng được bảo vệ an ninh.\\nNếu người nước ngoài chụp ảnh, rất có thể sẽ bị kiểm tra thân thể đấy.」"
"2352" = "「Trong tất cả các nhà ga đường sắt ở Trung Quốc mà Suika biết,\\nkhông có hệ thống vé vào cửa đâu.」"
"2354" = "「Trong phạm vi hiểu biết của Suika, ở Trung Quốc không tồn tại những 『nhà ga nhỏ』 mang phong cách Hinomoto.\\nTức là những nhà ga chỉ có cấu trúc gồm cổng soát vé và sân ga.」"
"2401" = "「Tôi——nếu ở Trung Quốc vẫn còn đầu máy hơi nước đang hoạt động,\\nthì tôi muốn đi xem đứa bé đó ạ.」"
"2462" = "「Vâng! Suika cũng thấy rất dễ hiểu.\\nỞ Trung Quốc, tàu nhanh cũng là tàu nhanh. Phát âm là 『Kuai-su』 mà.」"
"2481" = "「Có một nơi như vậy ạ. Có một cơ sở tên là Bảo tàng Lịch sử Đường sắt Trung Quốc,\\nnằm ở vùng ngoại ô Beiqin.」"
"2582" = "「Được khen là thiết kế tuyệt đẹp, Suika vui lắm!\\nLü-pi-che——Lục Bỉ Xa là biểu tượng của đường sắt Trung Quốc đấy!」"
"2611" = "「Chuyên môn của Suika là trong phạm vi các tuyến đường sắt quốc gia Trung Quốc được kết nối.\\nNhững khu vực ngoài đó thì cần phải tất cứu. Cần phải điều tra một chút ạ.」"
"2679" = "「Nhân viên an ninh đang làm việc cho Đường sắt Quốc gia Trung Quốc.\\nNên bộ đồng phục này đã giúp ích rất nhiều trong việc giải thích tình hình.」"
"2687" = "「Khi người Trung Quốc đi du lịch vài ngày từ Beiqin!\\nNhững lúc như thế, điểm đến phổ biến nhất là ở đâu ạ?」"
"2715" = "「Vậy thì hãy thử suy nghĩ từ một khía cạnh khác xem sao. Hachiroku,\\ncô có chuyến tàu nào muốn đi, hay muốn xem ở Trung Quốc không?」"
"2731" = "「Vậy thì Suika sẽ dẫn mọi người đến ga Beiqin——\\nga đầu mối lớn nhất của Trung Quốc!」"
"2897" = "Ôi chà, là tiếng Trung."
"2920" = "Cho dù việc phát triển đầu máy mới đã bị đình trệ trong một thời gian dài,\\nnhưng ở Trung Quốc, không hề có cuộc đại bãi bỏ các tuyến đường sắt như ở Hinomoto——"
"2996" = "Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Trung Quốc,\\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……?"
"3074" = "Tôi chợt nhớ lại lời cảnh báo đã nhận được ở khu vực bán vé.\\nNếu \"cơ sở nhà ga là đối tượng được bảo vệ an ninh ở Trung Quốc\" thì——"
"3268" = "Nói rồi, Zhihuan chỉ vào biểu tượng của Đường sắt Quốc gia Trung Quốc\\nđang tỏa sáng ở chính giữa chiếc mũ đồng phục."
"3281" = "Khi tôi quay mặt lại xem có chuyện gì, thì thấy một thanh niên mặc đồng phục\\n——đồng phục của Đường sắt Quốc gia Trung Quốc——đang chạy chậm về phía Suika."
```

```toml
# 仲国03_北琴鉄道歴史館.txt.toml
[script]
"1556" = "「『Vì vậy』. Đường sắt Quốc gia Trung Quốc,\\nđã chọn khổ 1435mm——khổ tiêu chuẩn sao?」"
"1878" = "「Sau khi làm việc ở Đường sắt Nam Man cũ——\\nĐứa bé này cũng đã hoạt động tích cực ở Đường sắt Quốc gia Trung Quốc nhỉ?」"
"1882" = "「Đường sắt Quốc gia Trung Quốc cũng đã dự đoán và kỳ vọng vào sự phát triển đó.\\nNhưng cuộc Đại bãi bỏ các tuyến đường sắt đã làm đảo lộn mọi thứ.」"
"2055" = "「Cha tôi là một người lái tàu thử nghiệm,\\nđã tham gia sâu vào việc phát triển và lựa chọn đầu máy thế hệ tiếp theo để hỗ trợ Đường sắt Quốc gia Trung Quốc.」"
"2082" = "「Cách tiếp cận của Sư phụ đối với Đường sắt Đế quốc Hinomoto——Đường sắt Teitetsu,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」"
"2083" = "「Sư phụ đã nghiên cứu Đường sắt Teitetsu với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Trung Quốc cũng vậy.」"
"2132" = "「Chuyến tàu đầu tiên ở Trung Quốc. Tàu Z49.\\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」"
"2225" = "「Đúng vậy. Dù từng bị hư hỏng đến mức suýt bị vứt bỏ,\\nnhưng nó đã được phục hồi để kỷ niệm một năm thành lập Trung Quốc, và lại tiếp tục hoạt động.」"
"2248" = "「Nên lấy từ tên của chủ sở hữu Đường sắt Đế quốc Hinomoto, Hoàng đế Hinomoto (Mikado),\\nđể đặt biệt danh là Mikado sao!?」"
"2251" = "「Đường sắt Teitetsu ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Trung Quốc,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」"
"2331" = "「Suika sẽ giải thích lý do tại sao. Hai quốc gia mà Quốc Hệ hiệu kết nối.\\nĐó chính là Trung Quốc và Hinomoto.」"
"2384" = "「Trong bảo tàng lịch sử này, còn có những đầu máy hơi nước được chế tạo ở Osaka nữa.\\nĐường ray của Trung Quốc và Hinomoto, trước đây từng được kết nối với nhau đấy.」"
"2592" = "Tôi thậm chí còn cảm nhận được Suika\\ntrân trọng Trung Quốc, trân trọng Hinomoto đến nhường nào."
"2641" = "Kể từ khi đến Trung Quốc, Hachiroku\\nthỉnh thoảng lại bộc lộ sự tiếc nuối."
"2642" = "Đường sắt Nam Man cũ——hay đúng hơn là Manzhouguo cũ,\\nlà một trong những nguyên nhân dẫn đến \\x%l大戦;#00ffc040;Đại chiến%l;#; giữa Hinomoto và Trung Quốc."
"2845" = "Ôi chà, có điện thoại.\\nCô Jiang đang nói gì đó bằng tiếng Trung với tốc độ rất nhanh——Ư!"
"2849" = "Lời nói của Suika, và những chiếc \\x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; do Hinomoto sản xuất từ thời kỳ đầu\\ncủa Đường sắt Quốc gia Trung Quốc đang được lưu giữ trong bảo tàng lịch sử này."
"2944" = "Thế này là được rồi. Hachiroku, người luôn có chút gượng gạo và bất ổn kể từ khi đến Trung Quốc,\\ncuối cùng cũng đã tìm lại được trục cốt lõi của mình."
```

```toml
# 仲国04_z49列車.txt.toml
[script]
"1392" = "「……Vẽ đẹp lắm. Rất có hồn.\\nBầu không khí trước khi khởi hành cho một chuyến đi, dù là Hinomoto hay Trung Quốc thì cũng không khác biệt mấy nhỉ.」"
"1671" = "「Hachiroku. Công việc của người trưởng tàu,\\ntôi nghĩ ở Trung Quốc và Hinomoto cũng giống nhau thôi, đúng không?」"
"1829" = "「Ufufu, Hinomoto và Trung Quốc.\\nĐây là sự kết hợp những điểm tốt nhất trong dịch vụ của cả hai bên nhỉ.」"
"1857" = "「Muốn ăn quá đi. À, cô Jiang này.\\nỞ Trung Quốc, khi bắt đầu bữa ăn mọi người thường làm thế nào vậy?」"
"2131" = "「Ở Trung Quốc, toa ăn được gọi là \\x%lｃａｎｃｈｅ;#00ffc040;Can-che%l;#;. \\x%lさんしゃ;#00ffc040;Xan-chơ%l;#;.\\nĐược viết bằng chữ \"Xan\" trong bữa tối (Vãn xan) đấy ạ.」"
```

```toml
# 仲国08_謝謝再見！.txt.toml
[script]
"1086" = "「——\"Tương lai\" của Nine Stars ở Hinomoto,\\ncó cần thiết phải thúc đẩy ở Trung Quốc không?」"
"1149" = "「……Cuốn sổ tay mô phỏng vé tàu ngày xưa của Đường sắt Bayan này,\\nvà huy hiệu cài áo hình logo đường sắt quốc gia Trung Quốc có lẽ sẽ là tài liệu tham khảo tốt.」"
"1428" = "「9.597.000 km vuông chia cho 36.750 km vuông.\\nTính theo tỷ lệ diện tích đơn thuần, Trung Quốc lớn hơn Kyushu khoảng 260 lần.」"
"1473" = "「Đường sắt quốc gia Trung Quốc——Lão sư, Zhihuan, và nhóm Suika——\\nĐầu máy của nhóm Suika, được mọi người tạo ra, bảo vệ và nuôi dưỡng.」"
"1474" = "「Kỳ nghỉ dài ngày trung bình ở Trung Quốc gồm hai đợt 7 ngày.\\nĐó là Lễ hội mùa xuân, tức là Tết Nguyên đán, và Quốc khánh. Vì vậy——」"
"1476" = "「Nhưng, với giới trẻ Trung Quốc hiện nay thì——\\ncó vẻ khó để khiến họ hứng thú với chiến dịch này.」"
"1484" = "「Chỉ Đường sắt Ohitoyo thôi thì không đủ. Sẽ cần phải tập hợp\\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trung Quốc.」"
"1674" = "「Vì vậy, dù có khoanh vùng một khu vực có quy mô bằng Kyushu để đi du lịch,\\nthì cũng chỉ là du lịch vòng quanh \"một phần rất nhỏ của Trung Quốc\" mà thôi.」"
"1686" = "「Ở Hinomoto, Tân Cán Tuyến——phải trải đường ray chuyên dụng khổ tiêu chuẩn,\\nnhưng Trung Quốc thì ngay từ đầu đã là khổ tiêu chuẩn rồi.」"
"1693" = "「Thông qua chuyến hành trình khẳng định lại sức hấp dẫn của Trung Quốc, để cảm nhận sức hấp dẫn của đường sắt Trung Quốc.\\nXa hơn nữa là——tái khám phá chính bản thân mình khi đi du lịch Trung Quốc.」"
"1781" = "「Nếu là chúng tôi thì trong tương lai. Có thể đề xuất một chuyến tàu đi vòng quanh nhà ga cứ điểm của cả 6 đại khu địa lý\\n——toàn bộ Trung Quốc trong 6 ngày.」"
"1782" = "「Chúng tôi có \\x%lクハ26;#00ffc040;Kuha 26%l;#; tốc hành \\x%l電車;#00ffc040;tàu điện%l;#;. Còn đường sắt quốc gia Trung Quốc có Dongfeng 4D\\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」"
"1784" = "「Đầu tiên, chúng tôi tìm hiểu về sự rộng lớn của Trung Quốc,\\nvà cố gắng sắp xếp lại.」"
"1800" = "「Biến bức tranh và câu chuyện thành hiện thực. Những gì Hinai, Kisaki\\nvà cô Mayami đã hoàn thành ở Hinomoto, tôi chắc chắn sẽ làm được ở Trung Quốc.」"
"1858" = "「Ừ. Đúng vậy. Bằng cách sử dụng cộng cảm, Hachiroku đã giao lưu\\nvà thu thập thông tin rất tốt từ các Railord của Trung Quốc.」"
"1864" = "「Đúng vậy. Do đó, chúng tôi đã từ bỏ phương án đó. Và tìm kiếm một cách phân chia hoàn toàn khác.\\nThế là chúng tôi được biết đến khái niệm \"Đại khu địa lý Trung Quốc\".」"
"1898" = "「Hướng tới \"sự phục hưng của đường sắt quốc gia Trung Quốc trong tương lai\"——tôi có chút trơ trẽn\\nkhi cảm thấy rằng, dường như các vị còn có đề xuất nào khác nữa.」"
"1904" = "「Bức tranh để mọi người chú ý đến câu chuyện, và đọc nó.\\nVì vậy, tôi muốn cô Hibiki vẽ ở Trung Quốc nữa.」"
"1908" = "「Nhưng——khi thực sự đến đây và đi thử.\\nTôi mới hiểu ra rằng sự rộng lớn của Trung Quốc sẽ gây khó khăn cho việc du lịch vòng quanh.」"
"1919" = "「Là vô số những vì sao lấp lánh. 6 đại khu địa lý Trung Quốc——\\nTôi muốn rải ít nhất mười vì sao trở lên vào mỗi khu vực.」"
"1920" = "「Khám phá…… Trung Quốc——\\nKhẳng định lại sức hấp dẫn của Trung Quốc?」"
"1965" = "「Nhất định sẽ đơm hoa kết trái, xum xuê cành lá. Bằng bộ rễ đó, bằng cành lá đó,\\nhãy để chúng lan tỏa khắp toàn bộ lãnh thổ của Trung Quốc và Hinomoto.」"
"2012" = "「Thầy đang nói——sẽ cho chạy đường sắt siêu tốc\\nbằng cách điện khí hóa hoàn toàn khổ tiêu chuẩn ở Trung Quốc sao?」"
"2042" = "「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohitoyo,\\nnhằm phục hưng đường sắt quốc gia Trung Quốc ở thời điểm hiện tại.」"
"2046" = "「Là một tuyến đường vòng tròn nhỉ. Rất nhỏ.\\nNhưng, là tuyến đường vòng tròn kết nối Hinomoto và Trung Quốc.」"
"2050" = "「Điều đầu tiên tôi cảm nhận được trong chuyến thị sát lần này,\\nđó là \"đường sắt của Trung Quốc vẫn đang sống\".」"
"2051" = "「Vé trọn gói…… kiểu như đi tàu quốc gia Trung Quốc thoải mái trong dịp Lễ hội mùa xuân sao?\\nCái đó——Suika nghĩ vé đó có vẻ cũng sẽ rất đắt.」"
"2071" = "「Như vậy thì không thể trở thành chuyến tàu du lịch đại diện cho Trung Quốc được,\\nvà cũng không thể kéo dài tuyến đường ray kết nối trái tim của người dân Trung Quốc.」"
"2089" = "「Đường ray mà thầy Soutetsu vươn dài, là đường ray biết hát, biết kể chuyện.\\nTôi cũng muốn dệt nên điều đó trên tuyến đường sắt của Trung Quốc.」"
"2422" = "Những gì chúng tôi học được ở Trung Quốc, cùng với ý kiến và ý tưởng của mọi người.\\nViệc tổng hợp lại tất cả những thứ đó đã tiêu tốn thời gian đến tận bây giờ."
"2423" = "Dù trên bản đồ tuyến đường sắt quốc gia Trung Quốc mà tôi thấy ở Bảo tàng Đường sắt Bắc Cầm,\\nđường sắt hiển nhiên cũng kết nối với Hồng Cảng."
"2428" = "Trên bản đồ vẽ đơn giản Trung Quốc, Hibiki nhanh chóng vạch một đường."
"2508" = "Kết nối Trung Quốc, và cũng kết nối Trung Quốc với Hinomoto——\\nChúng tôi chỉ cần dốc toàn lực đề xuất một bản thảo cho chuyến tàu như vậy."
"2741" = "Tây Bắc, Hoa Bắc, Đông Bắc và Tây Nam, Trung Nam, Hoa Đông——\\nToàn bộ Trung Quốc được chia làm hai nửa Nam Bắc."
```

```toml
# 共通14_負債.txt.toml
[script]
"1112" = "「'Nếu không phải người dưng thì đừng có khách sáo'——\\nChẳng phải chính ngài tổng giám đốc đã nói vậy sao?」"
"1551" = "「Này này giám đốc chi nhánh Ohitoyo.\\nNói với tổng giám đốc mà lại dùng từ 'được không' sao.」"
"1882" = "「Kính chào ngài tổng giám đốc.」\\n「Xin ông đừng làm phiền công việc của tôi được không.」"
"1884" = "「Tổng giám đốc?」"
"1972" = "「Vậy thì——tổng giám đốc——\\nÔng Mototada, có quan hệ thế nào với ông Taito?」"
"2200" = "Chỉ thị \"cứ thẳng thắn đi\" của tổng giám đốc,\\nphải chăng Urakami cũng định tuân theo ở một mức độ nào đó."
"2708" = "Dù không thể đánh giá con người qua địa vị——\\nNhưng mà, một tổng giám đốc như thế này thì lại thân thiện quá mức rồi."
```

```toml
# 凪ふかみ02_凪の大会初挑戦！.txt.toml
[script]
"2280" = "「Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu,\\nrồi từ Thể Xá Lưu lại sinh ra Thị Hiện Lưu đó!!」"
"2377" = "「Đó là môn kiếm thuật đặt cược tất cả\\nvào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thị Hiện Lưu ấy.」"
"3109" = "Thị Hiện Lưu! Mình biết!!\\nMình hay học hỏi từ mấy cuốn doujinshi lắm!!"
```

```toml
# 日々姫01_リゾート食堂列車計画.txt.toml
[script]
"1805" = "「Ra là vậy, ra là vậy? Lời nhờ vả của Soutetsu——không phải nhỉ,\\nsự bốc đồng của tổng giám đốc ngân hàng tình cờ lại mang đến kết quả tốt đẹp.」"
"1996" = "「Đó là——đúng rồi. Chỉ đơn giản là sự bốc đồng của tổng giám đốc ngân hàng thôi.\\nVì người đó đột nhiên cướp mất lịch trình của tôi.」"
```

```toml
# 日々姫01_双鉄の妹.txt.toml
[script]
"1789" = "「『Đường sắt Đế quốc Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』」"
```

```toml
# 日々姫02_文庫森.txt.toml
[script]
"60" = "Năm \\x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Đế quốc được ban hành. Công bố.\\nĐường sắt Đế quốc Hinomoto chính thức ra đời."
```

```toml
# 日々姫06_日々姫の決断.txt.toml
[script]
"2897" = "「Cái đó thì cũng phải xem đã. Cho là bé Kisaki và Sou-chan ngang tài ngang sức đi,\\nthì Tổng giám đốc Houshou và chị cũng ngang ngửa nhau.」"
```

```toml
# 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml
[script]
"2458" = "「Vâng. Để tinh chế Quirquitium, trái tim của động cơ Aero-Craftech,\\nthì cần một lượng lớn nước ngọt.」"
```

```toml
# 真闇03_ひとしずく.txt.toml
[script]
"1833" = "「Của hãng President Fine Liquor bên Anh Quốc.\\nHọ hỏi xem đơn hàng tối thiểu là từ bao nhiêu chai.」"
"2533" = "Chênh lệch múi giờ là chín tiếng, vậy thì……\\nBên Anh Quốc mới chỉ sáu giờ tối thôi."
```

```toml
# 真闇h3_補習授業の廃校舎.txt.toml
[script]
"2469" = "「Nghe nói Houshou Kisaki cũng tán thành chuyện này.\\nCó vẻ như sẽ lôi kéo được cả Tổng giám đốc――Houshou Mototada vào nữa.」"
"3529" = "Như đã hẹn trước, từ trong xưởng rượu vang lên một giọng nói.\\nF. Scotty. Một Railord sinh ra ở Anh Quốc."
```

```toml
# 稀咲01_金と人.txt.toml
[script]
"1256" = "「……Bố đang nói với tư cách là Bố, hay là Tổng giám đốc vậy?」"
"1887" = "「Bố――à không, Tổng giám đốc!?」"
```

```toml
# 稀咲h1_性生活.txt.toml
[script]
"1416" = "「Không sao, em quen rồi.\\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——tổng giám đốc ngân hàng cơ.」"
```

```toml
# 稀咲h3_チャイナドレスでおもてなし.txt.toml
[script]
"1983" = "「Hơn cả liên quan, họ chắc chắn là chủ thể cấp vốn chính đấy.\\nMặc dù hiện tại Trung Quốc cũng đang chìm trong cơn bão Đại bãi bỏ các tuyến đường sắt」"
"2020" = "「Ở Trung Quốc, ngân hàng cũng là của nhà nước sao」"
"2230" = "「A…… bộ này, là đồ chính hiệu, được đo may đàng hoàng\\nở Trung Quốc đấy」"
"2455" = "「Em sắp có khách đến thăm, từ Trung Quốc. Là con gái\\ncủa một người bạn cũ của bố em, nhưng có vẻ cô ấy là người khá khó tính」"
"2489" = "「Tiếp đón khách từ Trung Quốc,\\nthì em sẽ mặc sườn xám sao?」"
"2730" = "「Em đã đặt may ở…… một xưởng may hàng đầu tại Trung Quốc đấy」"
"2972" = "Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\\nmà việc phổ biến Aircra ở Trung Quốc diễn ra muộn hơn Hinomoto khá nhiều."
"3324" = "Nếu văn hóa Hinomoto là che giấu đi những đường cong của người phụ nữ,\\nthì văn hóa Trung Quốc lại là văn hóa phô bày những đường cong ấy."
```

## Kết bài

Đợt U13a sửa **171 dòng phân biệt trong 33 file, 8 mục**: T56 122 (72 “Trọng Quốc” + 46 “Zhongguo” tên nước + 2 “tiếng Zhongguo” → “tiếng Trung” + 1 “Nakakuni” + 1 “nước Chukoku”), T57 5, T58 3, T59 1, T60 27, T61 7, T63 4, T66 2. T62/T64/T65 giữ nguyên (0 dòng, đã kiểm chứng). Nguồn `old_vn`: 150 dòng CSV3, 15 dòng audit, 6 dòng unification đã gộp (1689 U1a + 5 rebase set2/set3), 0 dòng moan. Hai lệch số so với task/báo cáo E1 đã ghi ở §0: (1) T56 thực tế 122 dòng, không phải 124 (báo cáo E1 đếm trùng 2 dòng “tiếng Zhongguo” — chúng đã nằm trong “Zhongguo 48”); (2) T66 (2 dòng) có trong quyết định của coordinator nhưng không có trong bullet của task — đã áp dụng và tách riêng theo item để coordinator loại được nếu muốn. Cờ còn mở duy nhất: F-T56-1 (仲国08 2823, JP 日仲 — dòng “Trọng Quốc” duy nhất còn lại sau đợt này, chờ quyết ở đợt vét U15); F-T63-1 và F-T57-1 đã xong qua set2/set3 trong lúc đợt này đang chạy (xem §0d). Lượt soát 2: 171/171 tái kiểm chứng, 0 loại, 0 sửa giá trị fix. Khối TOML 33 file / 171 key parse-verified.
