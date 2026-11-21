# Audit — lr稀咲追加01_仲国視察の誘い.txt.toml (route 06_Kisaki)

- File: `lr稀咲追加01_仲国視察の誘い.txt.toml` — route 06_Kisaki, 1 bản duy nhất (không có file trùng).
- Đường dẫn: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/06_Kisaki/lr#U7a00#U54b2#U8ffd#U52a001_#U4ef2#U56fd#U8996#U5bdf#U306e#U8a98#U3044.txt.toml`
- Số dòng script: **330** (Kisaki 109, Soutetsu 86, độc thoại 76, Khương 59). Đọc toàn bộ 330/330 dòng đối chiếu JP + TW từ CSV3.
- Nội dung: Khương Diệp Hoàng (姜叶煌, thư ký Thứ trưởng Bộ Đường sắt Quốc vụ viện Trọng Quốc) tới thăm; bữa tối ở nhà Migita, bàn về Quỹ Đường sắt của tôi (マイレールファンド), lời mời sang Trọng Quốc khảo sát, và chuyện tuần trăng mật dời lại sau chuyến khảo sát. Soutetsu và Kisaki đã kết hôn trong file này (1192: Soutetsu tự nhận "chỉ là chồng của Kisaki"; 1168/1309: tuần trăng mật). Khương từng là gia sư của Kisaki. Không có cảnh H.
- **Kết quả: 19/330 dòng sai (5,8%)** — file dịch khá cẩn thận; lỗi tập trung ở thuật ngữ cũ (Ohimitera/Jiang) và 2 lỗi xưng hô của Khương.
- CSV3: 1 set duy nhất, 0 khóa trùng, 0 dòng VN trống, 0 dòng VN == TW, 0 dòng VN == JP. TOML khớp CSV3 tuyệt đối modulo hiện tượng đã biết: 252 giá trị TOML đã flatten `\n` literal thành khoảng trắng; CSV3 là bản authoritative, fix list lấy theo CSV3.
- TOML md5: `8174ddb1d982df221cd96eb05999ad0e`. Không có bản sao của file này trong 11 nhóm trùng. File có BOM + CRLF (680 dòng CRLF, 0 LF lẻ).
- `[selections]` rỗng. `[character_subs]`: chỉ 1 mục 1961 'Soutetsu' — trỏ tới key không có trong `[script]` (script có 1960 rồi 1962); dư thừa vô hại, không tính lỗi (xem cờ).
- `[characters]`: 1690 Soutetsu, 1718 Khương, 1822 Kisaki.

## Phân loại (19)

| Loại | Số dòng | Keys |
|---|---|---|
| Thuật ngữ (terminology) | 14 | 1025, 1260, 1275, 1300, 1309, 1321, 1564, 1772, 1864, 1866, 1868, 1906, 1920, 1921 |
| Thở gấp (gasp) | 1 | 1400 |
| Sai nghĩa (meaning) | 1 | 1336 |
| Đại từ (pronoun) | 2 | 1572, 1860 |
| SFX | 1 | 1289 |

Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0, cụt câu 0 (các dòng JP cụt được VN giữ cụt theo đúng quy tắc, xem §7).

## §1. Thuật ngữ (terminology) (14)
### 1025 [双鉄] — 姜 → cô Khương
- JP: `「かもしれんな。『そう導ける』と思ったがゆえ、\n元忠さんは姜さんを家庭教師に選んだのかもしれん」`
- TW: `「你這麼一說的話，感覺就像是再我原本道行基礎上，給姜小姐打通了任督二脈的感覺」`
- VN cũ: `「Có thể lắm. Chắc vì nghĩ rằng 'có thể dẫn dắt như vậy',\nnên ông Mototada mới chọn cô Jiang làm gia sư cho em.」`
- Fix: 姜 là Khương ([characters] 1718 'Khương'; file dùng "cô Khương" ở 50+ dòng). "Jiang" là đọc Quan thoại, lẫn vào file.
### 1260 [双鉄] — 姜 → cô Khương
- JP: `「それが姜さんか」`
- TW: `「家父大概也是實在看不下去了。就介紹了一位仲國來的留學生給我做家庭教師」`
- VN cũ: `「Đó là cô Jiang sao?」`
- Fix: Như 1025.
### 1275 [稀咲] — 姜 → cô Khương
- JP: `「うん。姜さんはボクに勉強と――\n勉強そのものの何倍も、多くのことを教えてくれた」`
- TW: `「就是姜小姐嗎」`
- VN cũ: `「Vâng. Cô Jiang không chỉ dạy em học mà——\nCô ấy còn dạy em nhiều điều gấp mấy lần việc học nữa.」`
- Fix: Như 1025.
### 1300 [monologue] — 御一夜鉄道 → Đường sắt Ohitoyo
- JP: `御一夜鉄道をめぐる現況をざっと説明するだけでも、\nかなりの時間が経ってしまった。`
- TW: `「您的問題都是直中要害，我們也不由得興致高漲起來了」`
- VN cũ: `Chỉ mới giải thích sơ qua về tình hình hiện tại xung quanh Đường sắt Ohimitera,\nmà cũng đã tốn khá nhiều thời gian rồi.`
- Fix: Quyết định 19/11 + 21/11 ~17:30: 御一夜鉄道 = "Đường sắt Ohitoyo" (không "Ohimitera"/"Ohito"). Tiền lệ Kisaki 02 sửa trực tiếp trong audit.
### 1309 [双鉄] — My Rail Fund → Quỹ Đường sắt của tôi
- JP: `「いや。新婚旅行は別途でスケジュールを必ず取ろう。\nマイレールファンドの引き継ぎが全て完了次第、すぐ」`
- TW: `「我也贊成。現在應該能有調整行程的空間，說不定可以把一推再推的新婚旅行也安排上」`
- VN cũ: `「Không. Tuần trăng mật nhất định phải sắp xếp lịch trình riêng.\nNgay sau khi hoàn tất việc bàn giao My Rail Fund.」`
- Fix: Thống nhất trong file: 7 dòng khác đều dùng "Quỹ Đường sắt của tôi" (1328, 1367, 1447, 1492, 1743, 1869, 1958); chỉ 1309 giữ tiếng Anh.
### 1321 [稀咲] — 姜 → cô Khương
- JP: `「そういわれると、もともとの素養を、\n姜さんが整頓して道筋を見せてくれた感じなのかな」`
- TW: `「我覺得這個選擇真是無比正確。這就是我所知道的稀咲之所以是稀咲的根源所在啊」`
- VN cũ: `「Anh nói vậy làm em có cảm giác như, những tố chất vốn có của em,\nđã được cô Jiang sắp xếp lại và vạch ra đường đi nước bước cho vậy.」`
- Fix: Như 1025. (Đại từ "Anh"/"em" trong dòng này giữ nguyên — xem cờ thống nhất.)
### 1564 [稀咲] — 姜 → cô Khương
- JP: `「でもね？　ボクや姜さんはそうじゃない。\nポーレットとかもお仲間だよね。閃かないタイプ」`
- TW: `「這太抬舉我了，受之有愧啊……不過若是稀咲這麼評價的話，也說不定真就是這樣」`
- VN cũ: `「Nhưng anh biết không? Em và cô Jiang lại không như thế.\nCả chị Paulette cũng giống tụi em. Đều là tuýp người không có ý tưởng bất chợt.」`
- Fix: Như 1025. (Đại từ "anh"/"Em" trong dòng này giữ nguyên — xem cờ thống nhất.)
### 1772 [姜] — 御一夜鉄道 → Đường sắt Ohitoyo
- JP: `「内諾をいただいた技術者達が一転して続々と辞退を。\n理由を探ればすぐ、双鉄先生と御一夜鉄道に当りました」`
- TW: `想必她對甜食是頗為喜愛吧——每把一塊長饅頭送入口中，在她眼鏡後的雙眸中，就會閃過純粹的喜悅之情。`
- VN cũ: `「Các kỹ sư đã đồng ý ngầm bỗng quay ngoắt lại và liên tiếp từ chối.\nKhi tìm hiểu lý do, chúng tôi ngay lập tức bắt gặp ngài Soutetsu và Đường sắt Ohimitera.」`
- Fix: Như 1300.
### 1864 [稀咲] — 姜 → cô Khương
- JP: `「姜さんが、無言のうちに一番深く教えてくれたのは、\n多分、そこ」`
- TW: `稀咲的話語中充滿了自豪。讓我深感一步一個腳印所積累出的強大。`
- VN cũ: `「Điều mà cô Jiang dạy em sâu sắc nhất trong im lặng,\ncó lẽ chính là điểm đó.」`
- Fix: Như 1025.
### 1866 [双鉄] — Ohimitera → Ohitoyo
- JP: `「姜さん、甘いものが大丈夫でしたら、ぜひご一緒に。\n御一夜名物の長饅頭です。お茶との相性がとても良くて」`
- TW: `稀咲端來了茶盤。在茶盤上——啊。`
- VN cũ: `「Cô Khương, nếu cô dùng được đồ ngọt thì xin mời dùng chung.\nĐây là món bánh trường man thầu đặc sản của Ohimitera. Rất hợp để thưởng thức cùng với trà đấy.」`
- Fix: Như 1300 (御一夜名物).
### 1868 [稀咲] — tuyến Yui + Đường sắt Ohimitera → tuyến Yunoi + Đường sắt Ohitoyo
- JP: `「クマ茶っていって、\n双鉄の勤める御一夜鉄道――湯医線沿線の名産なのさ」`
- TW: `稀咲說完便起身更換了茶具。這次的茶壺和茶碗，是我們平常見慣的日式茶具。`
- VN cũ: `「Đây gọi là trà Kuma,\nđặc sản dọc tuyến Yui――Đường sắt Ohimitera nơi Soutetsu làm việc đấy.」`
- Fix: 湯医線 = "tuyến Yunoi" (quyết định đã khóa); 御一夜鉄道 như 1300.
### 1906 [稀咲] — Ohimitera → Ohitoyo
- JP: `「晩ごはん、一緒にどうかな。御一夜の名店だと、地鶏、\n鰻あたりがおすすめだし――」`
- TW: `見稀咲瞄了我一眼，我便向她點了點頭。不管她在盤算什麼，都由著她去安排便好。`
- VN cũ: `「Ăn tối, cùng nhau thì sao nhỉ. Nhắc đến quán nổi tiếng ở Ohimitera, thì gà thả đồi,\nhay lươn là những món đáng thử đấy――」`
- Fix: Như 1300 (御一夜の名店).
### 1920 [双鉄] — Ohimitera → Ohitoyo
- JP: `「もしも稀咲が力を貸してくれていなければ、\n今の僕も、今の御一夜もありません」`
- TW: `話音未落，稀咲臉上閃過了一絲狼狽的神情。這話也許會讓她有些不好意思，卻是毋庸置疑的事實。`
- VN cũ: `「Nếu không có sự trợ giúp của Kisaki,\nthì đã không có tôi của hiện tại, cũng không có Ohimitera của hiện tại.」`
- Fix: Như 1300.
### 1921 [稀咲] — Ngân hàng Kuma + Đường sắt Ohimitera → Ngân hàng Kumamoto + Đường sắt Ohitoyo
- JP: `「だから隈銀と御一夜鉄道の共同出資で設立した新法人に、\n関連全事業を請け負ってもらうことにしたんだ」`
- TW: `話題又從甜點急轉回了正題。而這樣的節奏，兩人似乎都早已習慣。`
- VN cũ: `「Vì vậy, một pháp nhân mới được thành lập với sự góp vốn chung của Ngân hàng Kuma và Đường sắt Ohimitera,\nsẽ đảm nhận toàn bộ các dự án liên quan.」`
- Fix: 隈銀 là viết tắt của 隈元銀行 = "Ngân hàng Kumamoto" (tiền lệ 00common09 key 3109 giữ gloss; file này 982 đã dùng "Ngân hàng Kumamoto"); 御一夜鉄道 như 1300.
## §2. Thở gấp (gasp) (1)
### 1400 [稀咲] — !!! → Ư!!!
- JP: `「っ！！！」`
- TW: `「是的，這一點我是再清楚不過了」`
- VN cũ: `「!!!」`
- Fix: Sweep lost-gasp-whole đã kiểm chứng: JP 「っ！！！」 cả dòng là tiếng thở gấp; VN cũ chỉ còn dấu chấm than, mất hẳn âm っ.
## §3. Sai nghĩa (meaning) (1)
### 1336 [稀咲] — dự案 → dự án
- JP: `「一時的にそうなっているね。\nとはいえ、新事業を常に模索してもいるよ」`
- TW: `「所以目前稀咲女士和右田先生，都是專注於各自的主業嗎？」`
- VN cũ: `「Tạm thời là như vậy.\nTuy nhiên, chúng tôi cũng luôn tìm tòi các dự案 mới.」`
- Fix: Ký tự CJK 案 lọt vào câu VN ("dự案"); JP là 新事業 = dự án mới.
## §4. Đại từ (pronoun) (2)
### 1572 [姜] — "anh" → "ngài" (Khương → Soutetsu)
- JP: `「お口に合うならなによりです」`
- TW: `「這茶竟是姜小姐所贈啊。十分感謝，讓我也能得嘗此等甘爽」`
- VN cũ: `「Hợp khẩu vị của anh là tốt rồi.」`
- Fix: Khương xưng hô trang trọng "ngài" với Soutetsu trong cả file (1357, 1452, 1464, 1619, 1704, 1717, 1739, 1741, 1745); "anh" ở đây lạc điệu, và Khương lớn tuổi hơn Soutetsu. (Khác tiền lệ tsuika02 dòng 81: ở đó "anh Soutetsu" là dạng thống nhất của file đó; ở đây "ngài" mới là dạng thống nhất.)
### 1860 [姜] — "Anh là ngài Soutetsu" → "Ngài là Soutetsu"
- JP: `「あなたが双鉄先生ですね。はじめまして。\n仲国国務院、鉄道部副部長秘書の、[きょうようこう,2]姜叶煌と申します」`
- TW: `稀咲的支行長室與往常無二。但今天在座的卻多了一張陌生的面孔。`
- VN cũ: `「Anh là ngài Soutetsu nhỉ. Rất hân hạnh được gặp.\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc, tên là Khương Diệp Hoàng.」`
- Fix: Như 1572: Khương dùng "ngài" với Soutetsu trong cả file; "Anh là ngài Soutetsu" trộn hai mức xưng hô trong một câu.
## §5. SFX (1)
### 1289 [双鉄] — ほう → "Ồ."
- JP: `「ほう」`
- TW: `「很遺憾，民營鐵路遠達不到百花齊放的程度。不過，正因其數量不多，而有著各自獨特的魅力」`
- VN cũ: `「Hô.」`
- Fix: ほう là thán từ ngạc nhiên nhẹ; 997 cùng thán từ này đã dịch "Ồ.". "Hô." là phiên âm, không phải tiếng Việt.

## §6. Đại từ đã kiểm chứng — giữ nguyên (không sửa)

- **Soutetsu với Kisaki**: đa số dòng dùng "tôi" đúng quy tắc (1135, 1152, 1174, 1309, 1338, 1382, 1599...). Ba dòng "Anh" (720, 1116, 1322) và các dòng gọi Kisaki "em" — xem cờ thống nhất §8, không tự sửa.
- **Kisaki gọi Soutetsu bằng tên trần "Soutetsu"**: 1016 ("Được Soutetsu khen"), 1341 ("A, Soutetsu"), 1516 ("Không đâu, Soutetsu"), 1521 ("Soutetsu, cậu nghĩ sao?") — đúng quy tắc đã khóa (Kisaki→Soutetsu = tên trần; cô gọi Soutetsu "cậu" theo Common 14).
- **Kisaki tự xưng "em" ở các dòng thân mật**: 1087, 1155, 1275, 1321, 1404, 1564, 1594, 1781, 1785, 1819, 1856, 1864, 1925, 1957 — đúng quy tắc ngữ cảnh (thân mật → "em"); **"tôi" ở các dòng công việc**: 982, 993, 1016, 1034, 1089, 1332, 1345, 1601, 1850, 1924 — đúng quy tắc (công việc/quyết đoán → "tôi"). Các dòng ranh giới — xem cờ §8.
- **Khương với Soutetsu**: "ngài" ở 1357, 1452, 1464, 1619, 1704, 1717, 1739, 1741, 1745 (và "các ngài" 1775) — đúng; chỉ 1572/1860 lạc điệu, đã sửa §4.
- **Khương với Kisaki**: "cô Kisaki" nhất quán. **Soutetsu với Khương**: "cô Khương" nhất quán. **Kisaki với Khương**: "cô Khương" (sau fix 6 dòng "Jiang").
- **Khác**: 1140 義父 → "bố vợ" đúng (Mototada là bố vợ của Soutetsu); 1371 真闇姉 → "chị Mayami" đúng; 1564 "chị Paulette" đúng.

## §7. Giữ nguyên có lý do (không tính lỗi)

- **JP cụt được VN giữ cụt** (không bịa phần tiếp): 1143 ("…là nhờ..."), 1516 ("nếu là cậu thì"), 1606 ("Nội bộ……"), 1152, 1194.
- **Thở/SFX đã render đúng**: 1092 んっ → "Ưm."; 1533/1088 ふふっ → "Fufu"; 1535 ぁぅっ → "Aư."; 1126 っと → "Ái chà." (ngẫu hứng); 1418 こほんっ → "Khụ khụ!"; 1566 ずずっ → "(Nhấp một ngụm)" (diễn tả hành động).
- **Ruby đã strip đúng quy tắc**: 1534 [バンカー,2] → "chủ ngân hàng"; 1860 [きょうようこう,2]姜叶煌 → "Khương Diệp Hoàng"; 1873 [ゆきめきらん,3]雪芽奇蘭 → "Tuyết Nha Kỳ Lan"; 1938 [なごてつ,2]名護鉄 → "Đường sắt Nago".
- **Thuật ngữ đúng sẵn**: 1563 冥国 → "Minh Quốc", エアクラ → "Aircra"; 982 隈元銀行 → "Ngân hàng Kumamoto"; 1021 副丘 → "Fukuoka" (chơi chữ ふくおか); 1938 名護鉄 → "Đường sắt Nago"; 1970 紹興酒 → "rượu Thiệu Hưng"; 1004/1123/1868/1923 長饅頭 → "bánh trường man thầu", クマ茶 → "trà Kuma" (cách gọi thống nhất trong file); 1091 日ノ本車輌 → "Xe lửa Hinomoto" (tên công ty, dạng rút gọn — giữ).
- **720 tục ngữ ghép** (ghi chú, không tính lỗi): VN ghép "cây muốn lặng mà gió chẳng ngừng" trước "tử dục dưỡng mà thân bất đãi đâu"; nửa sau khớp đúng tục ngữ JP (親孝行したいときには親は無し = 子欲養而親不待), nửa đầu là cặp tục ngữ quen thuộc trong tiếng Việt — giữ nguyên.
- **718/1853 "Thầy"/"người thầy" cho cô Khương** (nữ): giữ nguyên — 先生 ở đây là vai trò thầy/mentor; "người thầy" dùng chung được trong tiếng Việt. Ghi chú để đợt thống nhất xem xét nếu muốn đổi thành "cô giáo".
- **Không có thẻ %l nào** trong JP lẫn VN của file này (không lệch thẻ). Không có dòng moan/họ ひゃ — file không có cảnh H.

## §8. Cờ cho Hieu / đợt thống nhất (KHÔNG tự quyết)

1. **Cụm đại từ vợ chồng Soutetsu↔Kisaki** (đã kết hôn trong file này): Soutetsu tự xưng "Anh" 720, 1116, 1322 (vs "tôi" ở đa số dòng khác); Soutetsu gọi Kisaki "em" 1025, 1116, 1187, 1246, 1249, 1290, 1371, 1534 + độc thoại 1538; Kisaki gọi Soutetsu "Anh/anh" 1321, 1327, 1493, 1564, 1587 + "anh Soutetsu" 1488, 1687, 1783. GIỮ NGUYÊN theo quyết định 21/11 ~19:45 (phạm vi "các file Kisaki khác" thuộc đợt thống nhất, sweep) và tiền lệ lr Kisaki tsuika02 (cờ tương tự, không sửa trong audit). Cần một quyết định thống nhất: vợ chồng đã cưới dùng "anh/em" (phong cách của file này) hay "tôi/cô" + tên trần "Soutetsu" (quy tắc đã khóa từ thời Kisaki03)?
2. **Kisaki tự xưng "tôi" hay "em" — các dòng ranh giới theo quy tắc ngữ cảnh**: 1327 (kể chuyện chuẩn bị để khiến Soutetsu yêu mình — thân mật → "em"?), 1132 ("Đừng trêu tôi nữa mà" — trêu đùa với chồng → "em"?), 1024 ("Được Soutetsu khen tôi vui lắm"), 984 (tuần trăng mật/nghỉ phép), 1516 (trấn an), 1711 (hồi tưởng thời trẻ), 1783 ("cô Khương đã dạy tôi" — câu nói về anh là thành quả lớn nhất). Cờ cho đợt thống nhất rà lại theo quy tắc ngữ cảnh (tiền lệ tsuika02 cờ 1233 thay vì sửa).
3. **[character_subs] 1961 'Soutetsu'** trỏ tới key không có trong `[script]` — dư thừa vô hại; để kỹ thuật kiểm tra khi build.
4. **Cột TW lệch vị trí trong file này**: TW 684 ≈ nội dung JP 1145 (Tết Nguyên Đán), TW 700 ≈ JP 1780 (bữa tối nhà Migita), TW 984 ≈ JP 1168/1309 (tuần trăng mật). VN bám JP đúng toàn bộ; TW không dùng làm chứng cứ chính ở file này. (JP vẫn thắng TW khi bất đồng, theo quy tắc.)

## §9. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 19 fix đối chiếu trực tiếp với JP của từng dòng (không chỉ parse-check): **19 tổng / 19 soát lại đạt / 0 bỏ / 0 sửa**. Trong lượt soát 2, kiểm tra thêm: không fix nào thay đổi ngoài phần cần sửa (diff-sanity cơ học: mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa — xem log build); JP/TW/old_vn trong JSON khớp CSV3 tuyệt đối 19/19. Sweep gasp: 1/1 mục của file (1400) đã áp nguyên văn sau khi kiểm chứng JP.

## Khối TOML (đã parse-kiểm chứng: 19 khóa, 0 sai lệch giá trị)

```toml
"1025" = "「Có thể lắm. Chắc vì nghĩ rằng 'có thể dẫn dắt như vậy',\\nnên ông Mototada mới chọn cô Khương làm gia sư cho em.」"
"1260" = "「Đó là cô Khương sao?」"
"1275" = "「Vâng. Cô Khương không chỉ dạy em học mà——\\nCô ấy còn dạy em nhiều điều gấp mấy lần việc học nữa.」"
"1289" = "「Ồ.」"
"1300" = "Chỉ mới giải thích sơ qua về tình hình hiện tại xung quanh Đường sắt Ohitoyo,\\nmà cũng đã tốn khá nhiều thời gian rồi."
"1309" = "「Không. Tuần trăng mật nhất định phải sắp xếp lịch trình riêng.\\nNgay sau khi hoàn tất việc bàn giao Quỹ Đường sắt của tôi.」"
"1321" = "「Anh nói vậy làm em có cảm giác như, những tố chất vốn có của em,\\nđã được cô Khương sắp xếp lại và vạch ra đường đi nước bước cho vậy.」"
"1336" = "「Tạm thời là như vậy.\\nTuy nhiên, chúng tôi cũng luôn tìm tòi các dự án mới.」"
"1400" = "「Ư!!!」"
"1564" = "「Nhưng anh biết không? Em và cô Khương lại không như thế.\\nCả chị Paulette cũng giống tụi em. Đều là tuýp người không có ý tưởng bất chợt.」"
"1572" = "「Hợp khẩu vị của ngài là tốt rồi.」"
"1772" = "「Các kỹ sư đã đồng ý ngầm bỗng quay ngoắt lại và liên tiếp từ chối.\\nKhi tìm hiểu lý do, chúng tôi ngay lập tức bắt gặp ngài Soutetsu và Đường sắt Ohitoyo.」"
"1860" = "「Ngài là Soutetsu nhỉ. Rất hân hạnh được gặp.\\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc, tên là Khương Diệp Hoàng.」"
"1864" = "「Điều mà cô Khương dạy em sâu sắc nhất trong im lặng,\\ncó lẽ chính là điểm đó.」"
"1866" = "「Cô Khương, nếu cô dùng được đồ ngọt thì xin mời dùng chung.\\nĐây là món bánh trường man thầu đặc sản của Ohitoyo. Rất hợp để thưởng thức cùng với trà đấy.」"
"1868" = "「Đây gọi là trà Kuma,\\nđặc sản dọc tuyến Yunoi――Đường sắt Ohitoyo nơi Soutetsu làm việc đấy.」"
"1906" = "「Ăn tối, cùng nhau thì sao nhỉ. Nhắc đến quán nổi tiếng ở Ohitoyo, thì gà thả đồi,\\nhay lươn là những món đáng thử đấy――」"
"1920" = "「Nếu không có sự trợ giúp của Kisaki,\\nthì đã không có tôi của hiện tại, cũng không có Ohitoyo của hiện tại.」"
"1921" = "「Vì vậy, một pháp nhân mới được thành lập với sự góp vốn chung của Ngân hàng Kumamoto và Đường sắt Ohitoyo,\\nsẽ đảm nhận toàn bộ các dự án liên quan.」"```

## Kết bài

File lr稀咲追加01_仲国視察の誘い: đọc 330/330 dòng, sai **19 dòng (5,8%)** — thuật ngữ 14, thở gấp 1 (từ sweep), sai nghĩa 1, đại từ 2, SFX 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Lỗi tập trung ở thuật ngữ cũ (Ohimitera ×7, Jiang ×6, Yui ×1, My Rail Fund ×1, Ngân hàng Kuma ×1) và 2 lỗi xưng hô của Khương. Cụm đại từ vợ chồng Soutetsu↔Kisaki và các dòng ranh giới "tôi"/"em" của Kisaki được giữ nguyên và cờ cho đợt thống nhất (xem §8). Lượt soát 2: 19/19/0/0. Khối TOML 19 khóa parse đạt, 0 sai lệch.
