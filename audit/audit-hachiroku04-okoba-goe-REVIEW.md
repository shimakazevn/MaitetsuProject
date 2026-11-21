# Audit — ハチロク04_小畑越え.txt.toml

- File: `ハチロク04_小畑越え.txt.toml` — route 01_Hachiroku, 448 dòng script (168 độc thoại, 126 thoại Soutetsu, 103 thoại Hachiroku, 39 thoại Munakata, 12 thoại Mima).
- Nội dung: lần đầu vượt đèo Okoba cùng Hachiroku — Hachiroku từ bỏ ước mơ vượt đèo trong buồng lái 8620 để lo việc Olivy; leo đèo bằng đường vòng zigzag (switchback) + đường vòng tròn (loop line); hồi tưởng chuyến phà thời thơ ấu với Mayami (hải âu cướp bánh phồng tôm Shibaten, lời hứa đưa Hibiki đi phà); đến ga Yatsushiro, gặp Mima (Trưởng phòng Vận tải Đường sắt Mikan) và Munakata (lái tàu cũ của Olivy); biết Olivy đóng kín cộng cảm vì tưởng mình bị Mikan vứt bỏ, kiểm tra cho thấy lão hóa nặng nên khuyến cáo kiểm tra toàn diện hàng năm; Olivy muốn sang Ohitoyo làm việc càng sớm càng tốt.
- **Kết quả: 27/448 dòng sai (6,0%)** — đọc đủ từng dòng đối chiếu JP + TW.

## §1. Kiểm tra cấu trúc


- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
- CSV3 1 set duy nhất (448 dòng, 0 khóa trùng, 0 ô VN trống, 0 VN==TW thật — dòng 1443 「……」 giống nhau ở cả 3 ngôn ngữ, chỉ là dấu ba chấm); TOML 448 khóa script, khớp CSV3 tuyệt đối 448/448 sau khi chuẩn hóa \n (306 dòng chỉ khác ở chỗ TOML-2 làm phẳng dấu \n thành khoảng trắng, đã biết, không phải lỗi). `[selections]` rỗng, `[info]` rỗng.
- TOML md5 `bbf7d882e646cde74ace8b5fe1541e47`; 1 bản duy nhất (không thuộc 11 nhóm trùng — đã kiểm tra: file ハチロク04 còn lại trong thư mục là 歯車の調べ, file khác). UTF-8 BOM + CRLF giữ nguyên.
- Không có thẻ `%l` nào sai định dạng trong VN (kiểm tra máy: số thẻ khớp JP từng dòng — chỉ 1 dòng VN tự thêm thẻ: 1951, gloss "chúng em" cho レイルロオド theo đúng ruby JP [わたくしたち,5], nội dung đúng, chỉ ghi nhận — xem §5).
- Nhiễm chéo kiểm tra máy: 0 dòng VN đặc trưng (≥25 ký tự) trong file này trùng với dòng VN ở file khác mà JP khác; trong file chỉ có VN trùng lặp hợp lệ: 「Đúng vậy.」 ×2 (2370, 2285 — đều là JP 「だな」), 「Vậy sao.」 ×3 (1860, 2022, 2497 — đều là JP 「そうか」), 「Vâng.」 ×2 (2016, 1889 — đều là JP 「はい」).
- Soutetsu: tự xưng "tôi" 38 lần, 0 lần "anh"/"em" trong thoại (đúng với Hachiroku — quy tắc đã sửa: "tôi" với Hachiroku); gọi Hachiroku "em" (2023 "em định nói thế"), 0 lần "cô" với Hachiroku (các "cô ấy" trong thoại Soutetsu đều là Olivy, ngôi thứ ba); gọi Mayami "chị Mayami" nhất quán (2214, 1801, 2490, 1809, 2380, 2466); gọi Hibiki "anh" đúng vai anh trai (2212 "anh sẽ cho Hibiki đi phà"); độc thoại 0 lần "mình" làm chủ ngữ. Hachiroku tự xưng "em" 22 lần, gọi Soutetsu "ngài Soutetsu" 10 lần — nhất quán toàn file.
- Thuật ngữ: file này đã có sẵn "Teitetsu" đúng 1 dòng (3201 "thời Teitetsu"); "Hinamoto" 0 dòng; "Ohimitera" 0 dòng; sau khi sửa không còn "Ohito" trần / "Yui" (湯医) / "Đường sắt Hoàng gia" nào — chỉ còn "Đường sắt Ohito" là tên công ty (11 dòng, GIỮ — xem §6).

## §2. Danh sách sửa (27 dòng)


Phân loại: thuật ngữ 27 (御一夜→Ohitoyo 16, 帝鉄→Teitetsu 7, 湯医線→Yunoi 3, 宮司→đền chủ 1). Toàn bộ là thuật ngữ đã chốt, không có sai nghĩa / đại từ / gasp / SFX nào khác.

### 1432 — 双鉄 — thuật ngữ
- JP: “「――ＳＬ御一夜」”
- TW: “「——御一夜蒸機」”
- VN cũ: "「——SL Ohito.」"
- Sửa: "「——SL Ohitoyo.」"
- Lý do: JP ＳＬ御一夜 — tên tàu, bare 御一夜 → 'Ohitoyo'.

### 1802 — 双鉄 — thuật ngữ
- JP: “「旧帝鉄、[ていおう,1]帝央\x%l機関区;#00ffc040;機関区%l;#;では、8620[けい]形\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、\nトップナンバー以外、ハロ１、ハロ２の連番だったと」”
- TW: “「不是說在前帝國鐵路，帝國中央車站\x%l機関区;#00ffc040;機務段%l;#;，８６２０型\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;除首車人偶都依次稱為Haro1號、Haro2號的嘛」”
- VN cũ: "「Ở Đường sắt Hoàng gia cũ, tại \x%l機関区;#00ffc040;kho đầu máy%l;#; Trung tâm Hoàng gia, các \x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」"
- Sửa: "「Ở Teitetsu cũ, tại \x%l機関区;#00ffc040;kho đầu máy%l;#; Trung tâm Hoàng gia, các \x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」"
- Lý do: JP 旧帝鉄 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11. ('Trung tâm Hoàng gia' cho 帝央機関区 giữ nguyên — chưa có thuật ngữ đã chốt cho 帝央.)

### 1807 — 双鉄 — thuật ngữ
- JP: “「[ひさつ,1]肥薩線の、そして[やつしろ,2]八ツ城－隈元間の復線が叶ったら、\n隈元－御一夜の直通列車を走らせてもおもしろかろうな」”
- TW: “「不止是肥薩線，要能再讓八代至隈元的廢線恢復通車的話，就可以考慮開行隈元至御一夜的直通列車了」”
- VN cũ: "「Nếu tuyến Hisatsu, và đoạn giữa Yatsushiro - Kumamoto được khôi phục,\nthì việc chạy chuyến tàu thẳng từ Kumamoto đến Ohito chắc sẽ thú vị lắm.」"
- Sửa: "「Nếu tuyến Hisatsu, và đoạn giữa Yatsushiro - Kumamoto được khôi phục,\nthì việc chạy chuyến tàu thẳng từ Kumamoto đến Ohitoyo chắc sẽ thú vị lắm.」"
- Lý do: JP 隈元－御一夜の直通列車 — bare 御一夜 → 'Ohitoyo'.

### 1823 — 双鉄 — thuật ngữ
- JP: “「御一夜では、お世話になりました。\n御一夜鉄道[ハチロクニイマル,3]8620号\x%l機関士;#00ffc040;機関士%l;#;。右田双鉄です」”
- TW: “「之前在御一夜勞煩您了，我是御一夜鐵路８６２０號\x%l機関士;#00ffc040;司機%l;#;，名叫右田雙鐵」”
- VN cũ: "「Ở Ohito đã làm phiền anh rồi.\nTôi là \x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohito. Migita Soutetsu.」"
- Sửa: "「Ở Ohitoyo đã làm phiền anh rồi.\nTôi là \x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohito. Migita Soutetsu.」"
- Lý do: JP 御一夜では、お世話になりました — bare 御一夜 → 'Ohitoyo'. ('Đường sắt Ohito' trong cùng dòng là tên công ty, GIỮ theo tiền lệ ROUTE-AUDIT — xem §6.)

### 1844 — 宗方 — thuật ngữ
- JP: “「御一夜では、[きゅうごう,1]Ⅸ号とオリヴィを――」”
- TW: “「你們御一夜是要讓九號和奧莉薇——」”
- VN cũ: "「Ở Ohito, các người định để Đầu máy số 9 và Olivy――」"
- Sửa: "「Ở Ohitoyo, các người định để Đầu máy số 9 và Olivy――」"
- Lý do: JP 御一夜では — bare 御一夜 → 'Ohitoyo'.

### 1859 — 双鉄 — thuật ngữ
- JP: “「旧帝鉄の文化では――ああ、いや、\nハチロクにも聞かされたことがあったか」”
- TW: “「依照前帝國鐵路的文化——啊，等等，這些其實也都聽你說起過的」”
- VN cũ: "「Trong văn hóa của Đường sắt Hoàng gia cũ——à không,\nHachiroku cũng từng kể cho tôi nghe rồi nhỉ.」"
- Sửa: "「Trong văn hóa của Teitetsu cũ——à không,\nHachiroku cũng từng kể cho tôi nghe rồi nhỉ.」"
- Lý do: JP 旧帝鉄の文化 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11.

### 1897 — 双鉄 — thuật ngữ
- JP: “「旧帝鉄――」”
- TW: “「前帝國鐵路——」”
- VN cũ: "「Đường sắt Hoàng gia cũ——」"
- Sửa: "「Teitetsu cũ——」"
- Lý do: JP 旧帝鉄 — thuật ngữ đã chốt: 帝鉄='Teitetsu'; guideline cấm 'Đường sắt Hoàng gia' (translation_guidelines.md:73, quyết định 19/11: 帝鉄 là viết tắt của 帝国鉄道 = Đường sắt Đế quốc, không phải Hoàng gia).

### 1922 — 双鉄 — thuật ngữ
- JP: “「同時に、Ⅸ号機関車の湯医線本線試運転のために、\nいくつかの点も確認してくる」”
- TW: “「另外讓九號機車進行湯醫線幹線試運營前，也需要先向對方明確幾個問題」”
- VN cũ: "「Đồng thời, cũng để xác nhận một số điểm\ncho việc chạy thử nghiệm đầu máy số 9 trên đường chính tuyến Yui.」"
- Sửa: "「Đồng thời, cũng để xác nhận một số điểm\ncho việc chạy thử nghiệm đầu máy số 9 trên đường chính tuyến Yunoi.」"
- Lý do: JP 湯医線本線 — thuật ngữ đã chốt: 湯医/湯医線='Yunoi' (AUDIT-BRIEF). VN cũ 'Yui'.

### 2048 — ハチロク — thuật ngữ
- JP: “「うふふ。御一夜急行でございますね。\nそれとも、御一夜特急、でございましょうか？」”
- TW: “「嘻嘻，那就是御一夜快列了。還是說稱之為御一夜特快更好？」”
- VN cũ: "「Ufufu. Là Tàu tốc hành Ohito nhỉ.\nHay là, Tàu siêu tốc Ohito ạ?」"
- Sửa: "「Ufufu. Là Tàu tốc hành Ohitoyo nhỉ.\nHay là, Tàu siêu tốc Ohitoyo ạ?」"
- Lý do: JP 御一夜急行 / 御一夜特急 — tên tàu, bare 御一夜 → 'Ohitoyo' (2 lần trong 1 dòng).

### 2061 — 双鉄 — thuật ngữ
- JP: “「長年\x%l入換;#00ffc040;入換%l;#;でしか走――いや、動いていなかったⅨ号が、\n御一夜までの長旅を経験したのだ」”
- TW: “「多年以來只為\x%l入換;#00ffc040;調車%l;#;而行駛——不，應該說是只被用於\x%l入換;#00ffc040;調車%l;#;的九號，剛剛又經歷了來到御一夜的長途旅程」”
- VN cũ: "「Nhiều năm qua, đầu máy số 9 chỉ chạy——à không, chỉ hoạt động \x%l入換;#00ffc040;dồn toa%l;#;,\nnay lại vừa trải qua một chuyến đi dài đến Ohito.」"
- Sửa: "「Nhiều năm qua, đầu máy số 9 chỉ chạy——à không, chỉ hoạt động \x%l入換;#00ffc040;dồn toa%l;#;,\nnay lại vừa trải qua một chuyến đi dài đến Ohitoyo.」"
- Lý do: JP 御一夜 (bare) — thuật ngữ đã chốt: 御一夜='Ohitoyo' (AUDIT-BRIEF, quyết định 19/11). VN cũ 'Ohito'.

### 2081 — ハチロク — thuật ngữ
- JP: “「残すは、北側――御一夜－八ツ城間のみ。\n叶いますね、ほんの数年後には、[ひさつ,1]肥颯線の全線復旧が」”
- TW: “「如今就只剩北邊——御一夜至八代路段尚未恢復。不出幾年，肥薩線就能實現全線恢復通車」”
- VN cũ: "「Chỉ còn lại phía Bắc——đoạn giữa Ohito và Yatsushiro thôi ạ.\nSẽ thành hiện thực thôi, chỉ vài năm nữa, tuyến Hisatsu sẽ được khôi phục toàn tuyến.」"
- Sửa: "「Chỉ còn lại phía Bắc——đoạn giữa Ohitoyo và Yatsushiro thôi ạ.\nSẽ thành hiện thực thôi, chỉ vài năm nữa, tuyến Hisatsu sẽ được khôi phục toàn tuyến.」"
- Lý do: JP 御一夜－八ツ城間 — bare 御一夜 → 'Ohitoyo'.

### 2083 — 宗方 — thuật ngữ
- JP: “「みかん鉄道への復職を希望するようなことがあっては、\n御一夜でフルパフォーマンスを発揮できない危険がある」”
- TW: “「如果奧莉薇依然心存返回橙鐵路工作的念頭，有可能會導致其在御一夜無法全力以赴」”
- VN cũ: "「Nếu nó có ý định muốn quay lại làm việc cho Đường sắt Mikan,\nthì có nguy cơ sẽ không thể phát huy hết khả năng ở Ohito.」"
- Sửa: "「Nếu nó có ý định muốn quay lại làm việc cho Đường sắt Mikan,\nthì có nguy cơ sẽ không thể phát huy hết khả năng ở Ohitoyo.」"
- Lý do: JP 御一夜でフルパフォーマンス — bare 御一夜 → 'Ohitoyo'.

### 2094 — 宗方 — thuật ngữ
- JP: “「『それなら、一日でも早く御一夜で仕事をしたい』\nと――」”
- TW: “「它便提出，希望儘早去御一夜工作——」”
- VN cũ: "「'Nếu vậy, tôi muốn làm việc ở Ohito sớm ngày nào hay ngày đó'\nnó bảo thế――」"
- Sửa: "「'Nếu vậy, tôi muốn làm việc ở Ohitoyo sớm ngày nào hay ngày đó'\nnó bảo thế――」"
- Lý do: JP 御一夜で仕事をしたい — bare 御一夜 → 'Ohitoyo'.

### 2112 — 双鉄 — thuật ngữ
- JP: “「そうか。ポーレットには帝鉄勤務の経験が無い。\nゆえ、御一夜鉄道はその文化圏の外にあるのか」”
- TW: “「對啊，波萊特沒有在帝國鐵路工作的經驗，所以御一夜鐵路就沒有受到其文化的薰陶」”
- VN cũ: "「Ra vậy. Paulette không có kinh nghiệm làm việc ở Đường sắt Hoàng gia.\nDo đó, Đường sắt Ohito nằm ngoài vòng văn hóa đó sao.」"
- Sửa: "「Ra vậy. Paulette không có kinh nghiệm làm việc ở Teitetsu.\nDo đó, Đường sắt Ohito nằm ngoài vòng văn hóa đó sao.」"
- Lý do: JP 帝鉄勤務 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11. ('Đường sắt Ohito' trong cùng dòng là tên công ty, GIỮ — xem §6.)

### 2125 — 双鉄 — thuật ngữ
- JP: “「それほど特別に扱われたのか。\nかつての帝鉄の、\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は物とする文化の中でも」”
- TW: “「就是在曾經帝國鐵路將\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;視為物品的文化環境之中，她都有如此特殊的待遇」”
- VN cũ: "「Được đối xử đặc biệt đến thế sao.\nNgay cả trong nền văn hóa coi \x%lレイルロオド;#00ffc040;Railord%l;#; là đồ vật của Đường sắt Hoàng gia trước đây.」"
- Sửa: "「Được đối xử đặc biệt đến thế sao.\nNgay cả trong nền văn hóa coi \x%lレイルロオド;#00ffc040;Railord%l;#; là đồ vật của Teitetsu trước đây.」"
- Lý do: JP かつての帝鉄 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11.

### 2175 — ハチロク — thuật ngữ
- JP: “「ＳＬ御一夜――シンプルで力強く、蒸気の香りが漂う。\nとても素敵な名前です」”
- TW: “「御一夜蒸機——簡短而有力，蘊含著蒸汽的芬芳，實在是再好不過的一個名字」”
- VN cũ: "「SL Ohito——Đơn giản, mạnh mẽ, và thoang thoảng hương thơm của hơi nước.\nMột cái tên rất tuyệt vời ạ.」"
- Sửa: "「SL Ohitoyo——Đơn giản, mạnh mẽ, và thoang thoảng hương thơm của hơi nước.\nMột cái tên rất tuyệt vời ạ.」"
- Lý do: JP ＳＬ御一夜 — tên tàu, bare 御一夜 → 'Ohitoyo'.

### 2340 — ハチロク — thuật ngữ
- JP: “「左様でございます。\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、基本、物。\nそこは、旧帝鉄の取扱の基本でございました」”
- TW: “「正是如此，一般\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;都只被定義為物品，這也是過去前帝國鐵路的基本認識」”
- VN cũ: "「Đúng là như vậy ạ. \x%lレイルロオド;#00ffc040;Railord%l;#; về cơ bản chỉ là đồ vật.\nĐó là quy tắc ứng xử cơ bản của Đường sắt Hoàng gia cũ ạ.」"
- Sửa: "「Đúng là như vậy ạ. \x%lレイルロオド;#00ffc040;Railord%l;#; về cơ bản chỉ là đồ vật.\nĐó là quy tắc ứng xử cơ bản của Teitetsu cũ ạ.」"
- Lý do: JP 旧帝鉄の取扱の基本 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11.

### 2460 — ハチロク — thuật ngữ
- JP: “「左様ですね。そして、みかん鉄道様は、見たところ、\n旧帝鉄の文化をそのまま引き継いでらっしゃるかと」”
- TW: “「誠如您所言。而依我所見，橙鐵路這裡應當是繼承了前帝國鐵路的文化氛圍」”
- VN cũ: "「Đúng vậy ạ. Và theo như em thấy, Đường sắt Mikan\ncó vẻ như vẫn kế thừa nguyên vẹn văn hóa của Đường sắt Hoàng gia cũ ạ.」"
- Sửa: "「Đúng vậy ạ. Và theo như em thấy, Đường sắt Mikan\ncó vẻ như vẫn kế thừa nguyên vẹn văn hóa của Teitetsu cũ ạ.」"
- Lý do: JP 旧帝鉄の文化 — 帝鉄='Teitetsu'; 'Đường sắt Hoàng gia' bị cấm theo quyết định 19/11.

### 2466 — 双鉄 — thuật ngữ
- JP: “「真闇姉の都合のつく日を作ってもらって――\n乗務の方は、赤井宮司か、み[てつ]鉄さんかにヘルプを頼んで」”
- TW: “「讓真闇姐空出幾天時間——乘務那邊就拜託赤井宮司或者橙鐵的人幫忙頂個班——」”
- VN cũ: "「Để chị Mayami sắp xếp một ngày rảnh rỗi——\nCòn việc làm nhiệm vụ thì nhờ ông Akai hoặc Đường sắt Mikan giúp đỡ.」"
- Sửa: "「Để chị Mayami sắp xếp một ngày rảnh rỗi——\nCòn việc làm nhiệm vụ thì nhờ đền chủ Akai hoặc Đường sắt Mikan giúp đỡ.」"
- Lý do: JP 赤井宮司 — 宮司='đền chủ' (AUDIT-BRIEF, đã chốt); VN cũ bỏ hẳn chức danh 宮司, chỉ còn 'ông Akai'.

### 2495 — 宗方 — thuật ngữ
- JP: “「御一夜には[とろ,1]登呂[もとぎかん,2]元技官もいるのだろう？\nなら、Ⅸ号にもアレにも、そちらの方が好環境だ」”
- TW: “「那位曾任高級技工的登呂不是也在御一夜嗎？那麼不論對於九號還是奧莉薇，也都是那邊的環境更加適合」”
- VN cũ: "「Ở Ohito cũng có cựu kỹ quan Toro phải không?\nVậy thì, môi trường bên đó tốt hơn cho cả Đầu máy số 9 và nó đấy.」"
- Sửa: "「Ở Ohitoyo cũng có cựu kỹ quan Toro phải không?\nVậy thì, môi trường bên đó tốt hơn cho cả Đầu máy số 9 và nó đấy.」"
- Lý do: JP 御一夜には登呂元技官もいる — bare 御一夜 → 'Ohitoyo'.

### 2512 — 双鉄 — thuật ngữ
- JP: “「ならば、ＳＬ御一夜を走らせるためにも頑張ろう。\n御一夜－[はやと,1]早戸間の営業運転を、何としても成功させよう」”
- TW: “「那麼為了讓御一夜蒸機得以實現，我們也要努力。無論如何都要讓御一夜至隼人的運營獲得成功」”
- VN cũ: "「Vậy thì, hãy cùng cố gắng để SL Ohito được chạy nào.\nDù thế nào cũng phải đưa tuyến Ohito - Hayato vào vận hành thương mại thành công.」"
- Sửa: "「Vậy thì, hãy cùng cố gắng để SL Ohitoyo được chạy nào.\nDù thế nào cũng phải đưa tuyến Ohitoyo - Hayato vào vận hành thương mại thành công.」"
- Lý do: JP ＳＬ御一夜 / 御一夜－早戸間 — bare 御一夜 → 'Ohitoyo' (2 lần trong 1 dòng).

### 2524 — 双鉄 — thuật ngữ
- JP: “「ゆえ――気の早い話にも程があるが、いつかはそちらを\n山の得意な機関車に任せ、僕らは御一夜－隈元間を」”
- TW: “「雖然這麼想實在為時過早，但我還是盼望有一天能將這邊交給擅長翻山越嶺的機車，我們負責御一夜至隈元的運營」”
- VN cũ: "「Cho nên——dù nói chuyện này hơi sớm, nhưng một ngày nào đó,\nchúng ta sẽ giao khu vực đó cho những đầu máy giỏi leo núi, còn chúng ta sẽ phụ trách đoạn Ohito - Kumamoto.」"
- Sửa: "「Cho nên——dù nói chuyện này hơi sớm, nhưng một ngày nào đó,\nchúng ta sẽ giao khu vực đó cho những đầu máy giỏi leo núi, còn chúng ta sẽ phụ trách đoạn Ohitoyo - Kumamoto.」"
- Lý do: JP 御一夜－隈元間 — bare 御一夜 → 'Ohitoyo'.

### 2750 — monologue — thuật ngữ
- JP: “可及的速やかに、Ⅸ号には湯医線を走ってもらい、\n僕らと8620は、この線路の上を走りたいものだ。”
- TW: “他希望九號能儘快在湯醫線投入運營，這樣才能騰出我們和８２６０去負責目前身處的這條線路。”
- VN cũ: "Chúng tôi muốn đầu máy số 9 chạy trên tuyến Yui càng sớm càng tốt,\nđể tôi và 8620 có thể chạy trên tuyến đường này."
- Sửa: "Chúng tôi muốn đầu máy số 9 chạy trên tuyến Yunoi càng sớm càng tốt,\nđể tôi và 8620 có thể chạy trên tuyến đường này."
- Lý do: JP 湯医線を走って — 湯医線='Yunoi'. VN cũ 'Yui'.

### 2837 — monologue — thuật ngữ
- JP: “九洲在住とはいえど、\nハチロクはあまり、湯医線の外に出ることはない。”
- TW: “八六雖然是住在九州，卻很少到湯醫線之外的區域走動。”
- VN cũ: "Dù sống ở Kyushu,\nnhưng Hachiroku rất hiếm khi ra khỏi tuyến Yui."
- Sửa: "Dù sống ở Kyushu,\nnhưng Hachiroku rất hiếm khi ra khỏi tuyến Yunoi."
- Lý do: JP 湯医線の外 — 湯医線='Yunoi'. VN cũ 'Yui'.

### 2959 — monologue — thuật ngữ
- JP: “隈元からの観光客を御一夜へと直通で運ぶ。\n御一夜急行。確かにわかりやすくて、素敵な名前だ。”
- TW: “將隈元的遊客直接送往御一夜，稱之為御一夜快列的確是通俗易懂，是個不錯的名字。”
- VN cũ: "Chở thẳng khách du lịch từ Kumamoto đến Ohito.\nTàu tốc hành Ohito. Quả thực là một cái tên dễ hiểu và tuyệt vời."
- Sửa: "Chở thẳng khách du lịch từ Kumamoto đến Ohitoyo.\nTàu tốc hành Ohitoyo. Quả thực là một cái tên dễ hiểu và tuyệt vời."
- Lý do: JP 御一夜へ / 御一夜急行 — bare 御一夜 → 'Ohitoyo' (2 lần trong 1 dòng).

### 3082 — monologue — thuật ngữ
- JP: “が、ポーレットが時間を設けての準備を依頼したのは、\n御一夜での性能低下を心配してのことではないだろう。”
- TW: “然而波萊特之所以拜託對方留出足夠的準備時間，肯定不會是因為擔心奧莉薇來到御一夜會出現性能低下的問題。”
- VN cũ: "Nhưng, lý do Paulette yêu cầu dành thời gian chuẩn bị,\nchắc chắn không phải vì lo lắng hiệu suất ở Ohito sẽ giảm sút."
- Sửa: "Nhưng, lý do Paulette yêu cầu dành thời gian chuẩn bị,\nchắc chắn không phải vì lo lắng hiệu suất ở Ohitoyo sẽ giảm sút."
- Lý do: JP 御一夜での性能低下 — bare 御一夜 → 'Ohitoyo'.

### 3226 — monologue — thuật ngữ
- JP: “ロングシートも、帝都を思い出して嫌いではない。\nが、御一夜から小畑を越えて早戸へと――”
- TW: “雖然對於豎排座位，抑或由此勾起的在帝都時的回憶，我都並不牴觸，但是從御一夜出發越過大畑前往隼人——”
- VN cũ: "Ghế dài dọc theo xe gợi nhớ đến Đế Đô nên tôi cũng không ghét.\nNhưng đi từ Ohito qua đèo Okoba đến Hayato——"
- Sửa: "Ghế dài dọc theo xe gợi nhớ đến Đế Đô nên tôi cũng không ghét.\nNhưng đi từ Ohitoyo qua đèo Okoba đến Hayato——"
- Lý do: JP 御一夜から小畑を越えて — bare 御一夜 → 'Ohitoyo'.

## §3. Sweep っ — kiểm tra trực tiếp sweep-raw-gasp-wrong.json


- File này có **0 mục** trong sweep (2 mục "ハチロク04" tìm thấy đều thuộc file khác ハチロク04_煙には煙を: 2455, 3088 — không phải file này). Không có gasp nào sweep bỏ sót.
- Quét bổ sung toàn bộ dòng JP chứa っ: các っ còn lại đều đã được diễn đúng hoặc không phải gasp theo quy tắc đã khóa 20/11 — 1947 きゃっ→"Á!?" (tiền lệ hachiroku09/15a: っ gắn liền với tiếng kêu, giữ "Á"); 1998 あっ→"A." (tiền lệ 00common12 2058); 2001 ああああああっ！→"Aaaaa!" (tiền lệ ハチロク03: っ đi sau có dấu !/? nên không thuộc trường hợp "mất hẳn"); 1958 ははっ→"Haha" (tiền lệ あははっ→"A haha"); 2044/2046 うふふっ→"Ufufu" (tiếng cười, đã diễn); 3251 （ぐんっ）→（Vù） (SFX đã diễn); 2525 そ、双鉄さまっ→"Ng, ngài Soutetsu!?" (lắp bắp, đã diễn — xem §5); các っ trong từ (しっかり, ぽぽっと, なって, ホっと→"thở phào") đã dịch đúng nghĩa.

## §4. Đã kiểm tra và không tính sai


- **"Đường sắt Ohito" (tên công ty) — 11 dòng GIỮ, không sửa:** 1477, 1973, 2298, 2217, 1902, 2121, 2181, 2112 (vế 2), 1823 (vế 2), 2234, 2182 — đều là 御一夜鉄道. Tiền lệ ROUTE-AUDIT: "Đường sắt Ohito" GIỮ (215 lần toàn dự án vs "Đường sắt Ohitoyo" 5 lần), chờ Hieu/unification quyết có đổi tên công ty đường sắt không. Chỉ sửa dạng trần 御一夜 (địa danh/tên tàu) trong cùng các dòng (2112, 1823 đã sửa vế trần).
- **1925 由衣 "khu vực Yui" — GIỮ:** JP [ゆい,1]由衣 là địa danh Yui (Shizuoka), KHÔNG phải 湯医 — không đổi sang Yunoi. TW 由比 xác nhận.
- **1951 VN tự thêm thẻ %l — chỉ ghi nhận:** JP không có thẻ %l nhưng có ruby [わたくしたち,5] trên レイルロオド; VN chuyển ruby thành gloss thẻ "chúng em" — nội dung đúng theo JP, theo tiền lệ 00common 2090 (thẻ thêm, nội dung đúng, chỉ ghi nhận).
- **2459 "con cũng sẽ ở lại" — GIỮ:** Soutetsu thuật lại lời mình nói hồi nhỏ với ông Taito (người nhận nuôi) — xưng "con" là tự nhiên với trẻ con nói với người lớn trong nhà, không phải lỗi đại từ.
- **2212 "anh sẽ cho Hibiki đi phà" — GIỮ:** Soutetsu là anh trai của Hibiki — "anh" đúng.
- **2458 "Nhà máy chế tạo toa xe Jutsusen" — GIỮ (ghi chú thống nhất):** 術仙 không gạch nối. Toàn dự án "Jutsusen" 34 lần vs "Jutsu-sen" 13 lần — dạng không gạch nối đang là đa số, brief chưa chốt dạng nào cho 術仙 (khác với "Jussen" thiếu chữ "t" đã sửa ở Paulette 02). Đề xuất thống nhất chốt một dạng cho toàn dự án sau.
- **1827/1440 "Lò trúng thưởng" cho 当り[がま]罐 — GIỮ:** 2 lần trong file, nhất quán; TW 大獎 (giải thưởng lớn) ủng hộ nghĩa "trúng thưởng". Chỉ có 2 lần toàn dự án, đều ở file này.
- **1814/2262 câu JP dở dang, VN hoàn thiện phần đuôi — GIỮ:** 1814 「アレがみかん鉄道に対して――」 VN thêm "giữ tình cảm"; 2262 「時間を」 VN thêm "đã xin thêm thời gian" — cả hai đều được dòng ngay sau (2083: Olivy muốn quay lại Mikan; 3082: Paulette yêu cầu dành thời gian chuẩn bị) xác nhận, không phải bịa thêm.
- **2242 Munakata xưng "mày" (お前) nhưng "tôi" (オレ) ở các dòng khác — GIỮ, ghi chú:** Munakata nói giọng thô (オレ/お前); VN dùng "mày" cho お前 ở 2242 nhưng "tôi" cho オレ ở 2084/2113/2268/2271/2475. "Tôi" cho オレ không sai nghĩa, chỉ mất độ thô; đổi toàn bộ sang "tao" là quyết định văn phong lớn, chưa có tiền lệ dự án — để Hieu quyết nếu muốn thống nhất.
- **2525 "Ng, ngài Soutetsu!?" — GIỮ:** lắp bắp "そ、" của Hachiroku, VN diễn bằng mảnh "Ng," — hiểu được là lắp bắp, không sai nghĩa.
- **3215 "Suzu vui vẻ" — GIỮ:** JP うれしげにすず — すず là tên Suzu của Hachiroku (TW 鈴 xác nhận), không phải lỗi.
- **2307/2322 スイッチバック→"đường vòng zigzag", ループ線→"đường ray vòng tròn" — GIỮ:** dịch nghĩa hợp lý, TW 折返線/展線 tương ứng; không có thuật ngữ đã chốt cho hai từ này.
- **69 ポイント→"Ghi đường sắt" — GIỮ:** theo tiền lệ Paulette 02 (ポイント "công tắc"→"ghi").
- **2055 "Teitetsu cũ" — đã đúng sẵn:** JP 『旧帝鉄』, VN đã dùng "Teitetsu" — không cần sửa. 3201 "thời Teitetsu" cũng đã đúng sẵn.
- **1802 帝央機関区→"kho đầu máy Trung tâm Hoàng gia" — GIỮ phần này:** chỉ sửa 帝鉄→Teitetsu; 帝央 chưa có thuật ngữ đã chốt, bản dịch nghĩa "Trung tâm Hoàng gia" giữ nguyên.

## §5. Khối TOML (đã parse-kiểm chứng: 27 khóa, 0 sai lệch)


```toml
[script]
1432 = "「——SL Ohitoyo.」"
1802 = "「Ở Teitetsu cũ, tại \\x%l機関区;#00ffc040;kho đầu máy%l;#; Trung tâm Hoàng gia, các \\x%lレイルロオド;#00ffc040;Railord%l;#; mẫu 8620,\\nngoại trừ chiếc đầu tiên thì đều được gọi theo số thứ tự Haro 1, Haro 2.」"
1807 = "「Nếu tuyến Hisatsu, và đoạn giữa Yatsushiro - Kumamoto được khôi phục,\\nthì việc chạy chuyến tàu thẳng từ Kumamoto đến Ohitoyo chắc sẽ thú vị lắm.」"
1823 = "「Ở Ohitoyo đã làm phiền anh rồi.\\nTôi là \\x%l機関士;#00ffc040;lái tàu%l;#; đầu máy 8620 của Đường sắt Ohito. Migita Soutetsu.」"
1844 = "「Ở Ohitoyo, các người định để Đầu máy số 9 và Olivy――」"
1859 = "「Trong văn hóa của Teitetsu cũ——à không,\\nHachiroku cũng từng kể cho tôi nghe rồi nhỉ.」"
1897 = "「Teitetsu cũ——」"
1922 = "「Đồng thời, cũng để xác nhận một số điểm\\ncho việc chạy thử nghiệm đầu máy số 9 trên đường chính tuyến Yunoi.」"
2048 = "「Ufufu. Là Tàu tốc hành Ohitoyo nhỉ.\\nHay là, Tàu siêu tốc Ohitoyo ạ?」"
2061 = "「Nhiều năm qua, đầu máy số 9 chỉ chạy——à không, chỉ hoạt động \\x%l入換;#00ffc040;dồn toa%l;#;,\\nnay lại vừa trải qua một chuyến đi dài đến Ohitoyo.」"
2081 = "「Chỉ còn lại phía Bắc——đoạn giữa Ohitoyo và Yatsushiro thôi ạ.\\nSẽ thành hiện thực thôi, chỉ vài năm nữa, tuyến Hisatsu sẽ được khôi phục toàn tuyến.」"
2083 = "「Nếu nó có ý định muốn quay lại làm việc cho Đường sắt Mikan,\\nthì có nguy cơ sẽ không thể phát huy hết khả năng ở Ohitoyo.」"
2094 = "「'Nếu vậy, tôi muốn làm việc ở Ohitoyo sớm ngày nào hay ngày đó'\\nnó bảo thế――」"
2112 = "「Ra vậy. Paulette không có kinh nghiệm làm việc ở Teitetsu.\\nDo đó, Đường sắt Ohito nằm ngoài vòng văn hóa đó sao.」"
2125 = "「Được đối xử đặc biệt đến thế sao.\\nNgay cả trong nền văn hóa coi \\x%lレイルロオド;#00ffc040;Railord%l;#; là đồ vật của Teitetsu trước đây.」"
2175 = "「SL Ohitoyo——Đơn giản, mạnh mẽ, và thoang thoảng hương thơm của hơi nước.\\nMột cái tên rất tuyệt vời ạ.」"
2340 = "「Đúng là như vậy ạ. \\x%lレイルロオド;#00ffc040;Railord%l;#; về cơ bản chỉ là đồ vật.\\nĐó là quy tắc ứng xử cơ bản của Teitetsu cũ ạ.」"
2460 = "「Đúng vậy ạ. Và theo như em thấy, Đường sắt Mikan\\ncó vẻ như vẫn kế thừa nguyên vẹn văn hóa của Teitetsu cũ ạ.」"
2466 = "「Để chị Mayami sắp xếp một ngày rảnh rỗi——\\nCòn việc làm nhiệm vụ thì nhờ đền chủ Akai hoặc Đường sắt Mikan giúp đỡ.」"
2495 = "「Ở Ohitoyo cũng có cựu kỹ quan Toro phải không?\\nVậy thì, môi trường bên đó tốt hơn cho cả Đầu máy số 9 và nó đấy.」"
2512 = "「Vậy thì, hãy cùng cố gắng để SL Ohitoyo được chạy nào.\\nDù thế nào cũng phải đưa tuyến Ohitoyo - Hayato vào vận hành thương mại thành công.」"
2524 = "「Cho nên——dù nói chuyện này hơi sớm, nhưng một ngày nào đó,\\nchúng ta sẽ giao khu vực đó cho những đầu máy giỏi leo núi, còn chúng ta sẽ phụ trách đoạn Ohitoyo - Kumamoto.」"
2750 = "Chúng tôi muốn đầu máy số 9 chạy trên tuyến Yunoi càng sớm càng tốt,\\nđể tôi và 8620 có thể chạy trên tuyến đường này."
2837 = "Dù sống ở Kyushu,\\nnhưng Hachiroku rất hiếm khi ra khỏi tuyến Yunoi."
2959 = "Chở thẳng khách du lịch từ Kumamoto đến Ohitoyo.\\nTàu tốc hành Ohitoyo. Quả thực là một cái tên dễ hiểu và tuyệt vời."
3082 = "Nhưng, lý do Paulette yêu cầu dành thời gian chuẩn bị,\\nchắc chắn không phải vì lo lắng hiệu suất ở Ohitoyo sẽ giảm sút."
3226 = "Ghế dài dọc theo xe gợi nhớ đến Đế Đô nên tôi cũng không ghét.\\nNhưng đi từ Ohitoyo qua đèo Okoba đến Hayato——"
```

### Lượt soát 2

- 27 tổng / 27 kiểm tra lại đối chiếu JP / 0 loại bỏ / 0 sửa giá trị. Mọi fix chỉ đổi đúng phần thuật ngữ mục tiêu (kiểm tra máy: diff từng cặp old_vn→fix chỉ chứa đoạn thay thế đã định — "Ohito"→"Ohitoyo" (chèn "yo"), "Yui"→"Yunoi" (chèn "no"), "Đường sắt Hoàng gia"→"Teitetsu", "ông Akai"→"đền chủ Akai").
- Khối TOML 27 khóa đã parse-kiểm chứng bằng tomllib: 27/27 khóa, 0 sai lệch giá trị so với JSON (lưu ý: giá trị chứa \n literal được viết \\n trong khối để parse đúng). JSON 27 mục, khóa là chuỗi, jp/tw/old_vn khớp CSV3 tuyệt đối 27/27.

## §6. Chờ Hieu (không tự quyết)


- **"Đường sắt Ohito" (tên công ty) 11 dòng — KHÔNG thêm lại vào hàng đợi thống nhất dưới dạng lỗi audit:** 1477, 1973, 2298, 2217, 1902, 2112, 2181, 1823, 2234, 2182 + 2121. Đây là quyết định tên công ty đang chờ Hieu (tiền lệ ROUTE-AUDIT: 215 lần "Đường sắt Ohito" vs 5 lần "Đường sắt Ohitoyo" toàn dự án). Nếu đợt thống nhất quyết đổi tên công ty, quét toàn dự án, không chỉ file này.
- **Ohito trần→Ohitoyo (16 dòng) + Yui→Yunoi (3 dòng) + Teitetsu (7 dòng) + đền chủ Akai (1 dòng) đã sửa trong audit này — KHÔNG thêm lại các key này vào hàng đợi thống nhất:** 2061, 3226, 2081, 1807, 2524, 2048, 2959, 1432, 2175, 2512, 1823, 1844, 2083, 3082, 2094, 2495 (Ohitoyo); 1922, 2750, 2837 (Yunoi); 1897, 2112, 2460, 1859, 1802, 2340, 2125 (Teitetsu); 2466 (đền chủ). (Lưu ý: một audit trước — ハチロク04_煙には煙を — chọn để "Ohito"/"Yui" lại chờ thống nhất; các file đã audit vẫn còn "Ohito"/"Yui" ở dạng chờ — đợt thống nhất cần quét toàn dự án.)
- **"Jutsusen" vs "Jutsu-sen" (2458) — đề xuất thống nhất chốt một dạng toàn dự án** (hiện 34 vs 13, dạng không gạch nối đang nhiều hơn).
- **Đăng ký giọng Munakata オレ→"tao" hay giữ "tôi" — hỏi Hieu nếu muốn thống nhất** (xem §5).
- Không có câu hỏi thuật ngữ mới khác, không còn đại từ mơ hồ nào chưa quyết, không có dòng JP dở dang nào cần Hieu hoàn thiện.

## Kết bài


File ハチロク04_小畑越え đã audit xong toàn bộ 448 dòng: 27 dòng sai (6,0%) — toàn bộ thuật ngữ (御一夜→Ohitoyo 16, 帝鉄→Teitetsu 7, 湯医線→Yunoi 3, 宮司→đền chủ 1). Không lệch dòng, không xoay chuỗi, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch, không trùng khóa. Khối TOML 27 khóa đã parse-kiểm chứng, 0 sai lệch. Lượt soát 2: 27/27 giá trị fix đã đọc lại đối chiếu JP, 0 bỏ, 0 sửa giá trị. Chờ Hieu: tên công ty "Đường sắt Ohito" (11 dòng, chờ quyết), "Jutsusen" vs "Jutsu-sen", giọng Munakata オレ.

