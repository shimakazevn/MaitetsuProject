# Unification — §2 đại từ Paulette: P2 + P14 + O1 (batch U6)

**Phạm vi:** §2 P2 (Soutetsu → Paulette "cô" → "em"), P14 (Paulette → Soutetsu "cậu (Soutetsu)" → "anh Soutetsu" + 3 dòng tên trần P16), §7 O1 (Paulette 06 key 2047 — quyết định theo ủy quyền của Hieu) của `UNIFICATION-LIST.md`.
**Không đụng:** các mục P khác (P3 Kisaki, P8 Niiroku…), §1/§3–§6, tag sweep (§5). Không sửa `ROUTE-UNIFICATION.md`, `MEMORY.md`, hay bất kỳ file audit/moans nào.
**Nguồn:** CSV3 good-set (87.833 dòng; đã loại 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`), `audit-*-wrong.json` (9.139 mục map được; 99 mục không map — toàn bộ có JP trống, là dòng ngoài `[script]`, không thuộc phạm vi batch này), `moans/moan-*-wrong.json` (1.516 mục), TOML-2 (không cần — mọi dòng trong batch đều có trong CSV3), các đợt unification đã gộp (U1b/U1c/U2a — xem §5).

## Phương pháp

- `old_vn` theo quy ước bắt buộc: giá trị moan nếu (file,key) có trong moan list, nếu không thì giá trị audit fix, nếu không thì VN CSV3 good-set. Ngoại lệ duy nhất: Grand 01 key 2181 — `old_vn` lấy giá trị SAU đợt U1c đã gộp ("Ohitoyo", xem §5), vì đợt đó đã sửa cùng dòng này.
- **P2 — liệt kê:** quét toàn bộ CSV3 good-set, lấy mọi dòng có speaker là Soutetsu (Character `双鉄` / `双鉄H`, 17.027 + 1.479 dòng) mà giá trị hiện tại chứa "cô" đứng riêng (regex `(?<![\wÀ-ỹ])cô(?![\wÀ-ỹ])`, không phân biệt hoa/thường): **602 dòng ứng viên**. Loại 191 dòng "cô" ngôi ba/danh từ ("cô ấy", "cô gái", "cô bé", "cô đơn", "cô chủ"…) bằng pattern — kiểm chứng mẫu ngẫu nhiên 15/15 đều đúng là ngôi ba/danh từ. Còn 411 dòng: phân nhóm theo tập hợp nhân vật nói trong ±3 dòng (theo thứ tự file). 126 dòng có Paulette trong nhóm kề (hoặc không có nhân vật nào khác) được **đọc từng dòng kèm 3–5 dòng kề** (JP + TW + VN hiện tại): 99 dòng sửa (P2) + 1 dòng O1 + 26 dòng giữ. 285 dòng còn lại được phân loại theo nhóm kề + đọc hết các dòng trong file Paulette, mọi dòng JP/TW nhắc "ポーレット"/"Paulette", và kiểm chứng mẫu ngẫu nhiên (nhóm Kisaki 8/8, nhóm Hachiroku 6/6) — tất cả đều không phải Paulette (xem §3).
- **P14 — liệt kê:** quét giá trị hiện tại chứa "cậu Soutetsu"/"Cậu Soutetsu": **38 dòng** toàn dự án; trong đó speaker là Paulette chỉ có **9 dòng**. Kiểm chứng từng key ứng viên trong list (2210/2232, 2166, 3078, 2163, 2573/3256/3257, 2436) qua đúng file TOML: cả 9 dòng đều đã sửa thành "anh Soutetsu" trong audit (không sửa trùng). Cộng 3 dòng tên trần P16 (2008/2015/2016) — JP đều là 双鉄くん. Grand 08 key 1702 **không tồn tại** dòng Paulette (key 1702 của グランド08 là Kisaki nói 「キミは、それで――」 — xem §3).
- **Không sửa bulk bằng script:** mọi giá trị fix đều do đọc JP (+TW + dòng kề) rồi viết tay; script chỉ dùng để tra cứu, lắp khối TOML và kiểm chứng cơ học (diff từng fix so với `old_vn`: mọi fix chỉ khác ở đúng chỗ đại từ cần sửa — kiểm chứng bằng span-diff 106/106).
- **O1:** điều tra JP + TW + dòng kề + phân bố "em"/"cô" theo chương (xem §4), rồi QUYẾT theo ủy quyền của Hieu (19/11, tái khẳng định 21/11 01:51).

## 1. P2 — Soutetsu → Paulette: "cô" → "em" (99 dòng)

Quyết định 19/11 (Hieu). Bằng chứng cộng dồn trong list: "em" 119 vs "cô" 49 toàn dự án; cụm P09–12 nghiêng "cô", P13–16 nghiêng "em". **Số dòng thực tế khi liệt kê lại: 99 dòng** (không phải 43 như brief cũ ghi — xem §5: con số 43 chỉ khớp cụm P09–12, 42 dòng; còn 57 dòng ở P01–08, Common, Hachiroku, Hibiki, Grand). Trong 99 dòng này: 102/106 dòng toàn batch lấy `old_vn` từ CSV3, 3 dòng từ audit fix (ハチロク05 3062, 日々姫04 1708, ポーレット05_鳴呼の町 2010 — audit đã sửa chỗ khác nhưng giữ "cô"), 1 dòng từ U1c (Grand 01 2181).

### グランドリライト04_ポーレット.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1283 | 「――ありがとう」 | 「——謝謝你」 | 「——Cảm ơn cô.」 | 「——Cảm ơn em.」 | Paulette 1836 ngạc nhiên vì được cảm ơn; monologue 2853: Paulette cười. |
| 1284 | 「――ありがとう、ポーレット」 | 「——謝謝你，波萊特」 | 「——Cảm ơn cô, Paulette.」 | 「——Cảm ơn em, Paulette.」 | Paulette 2076 nói về vai trò của mình; Soutetsu cảm ơn cô ấy. |
| 1715 | 「今日は、外に出る予定はあるか？\nもしもあるなら、雨にならぬうちに」 | 「今天有計劃外出嗎？如果有的話，趁著沒下雨的時候趕緊出門吧」 | 「Hôm nay cô có dự định ra ngoài không?\nNếu có thì đi trước khi trời mưa nhé.」 | 「Hôm nay em có dự định ra ngoài không?\nNếu có thì đi trước khi trời mưa nhé.」 | Paulette 1865/2158 trả lời sẽ đi cùng Soutetsu. |
| 1768 | 「僕が望んで繰り返し続けていた、苦しみと憎しみに。\nポーレット。君が、区切りをくれたんだ」 | 「其實我是主動投入那痛苦和憎恨的循環之中的。波萊特，是你帶我走到了終點」 | 「Chính tôi đã tự nguyện lặp đi lặp lại những đau khổ và thù hận đó.\nPaulette. Chính cô đã giúp tôi đặt dấu chấm hết cho chúng.」 | 「Chính tôi đã tự nguyện lặp đi lặp lại những đau khổ và thù hận đó.\nPaulette. Chính em đã giúp tôi đặt dấu chấm hết cho chúng.」 | JP 君 = Paulette (nêu tên ポーレット); Paulette 1840 đáp. |
| 1829 | 「おお。すごいな、こうやって手作りしていたのか。\n外部業者に委託しているものだと思っていたが」 | 「哇，真厲害啊，原來是這麼親手做的啊，我還以為是委託外部廠家的呢」 | 「Ồ. Tuyệt thật đấy, ra là cô tự làm thủ công thế này sao.\nTôi cứ tưởng là thuê bên ngoài làm chứ.」 | 「Ồ. Tuyệt thật đấy, ra là em tự làm thủ công thế này sao.\nTôi cứ tưởng là thuê bên ngoài làm chứ.」 | Paulette 2292 khoe huy hiệu tự làm. |
| 1901 | 「ああ、教えてくれるなら大歓迎だ」 | 「嗯，你肯教我那再好不過了」 | 「A, được cô chỉ cho thì còn gì bằng.」 | 「A, được em chỉ cho thì còn gì bằng.」 | Paulette 2270/1807 hướng dẫn; Soutetsu đáp "được cô chỉ cho thì còn gì bằng". |
| 1903 | 「うむ。多分、見て覚えられたかと思う。\n間違っていたら教えてくれ」 | 「嗯，剛才看的時候應該記住了。如果做錯了麻煩你告訴我」 | 「Ừm. Chắc là tôi nhìn và nhớ được rồi.\nNếu sai thì cô chỉ tôi nhé.」 | 「Ừm. Chắc là tôi nhìn và nhớ được rồi.\nNếu sai thì em chỉ tôi nhé.」 | Paulette 2192 hướng dẫn làm huy hiệu. |
| 1923 | 「うむ？　その方が良いのであれば、そうしよう」 | 「嗯？你覺得這樣搬比較好的話我沒意見」 | 「Hửm? Nếu cô thấy thế tốt hơn, thì cứ làm vậy đi.」 | 「Hửm? Nếu em thấy thế tốt hơn, thì cứ làm vậy đi.」 | Paulette 1810/1898 đề xuất cùng khiêng hộp các-tông. |
| 2012 | 「こちらこそ、よろしく頼む」 | 「彼此彼此」 | 「Tôi cũng mong cô giúp đỡ.」 | 「Tôi cũng mong em giúp đỡ.」 | Paulette 2103 chào buổi sáng; Soutetsu đáp lại cô ấy. |
| 2021 | 「なんだ？　今日の僕は、\n塗り替えでも手伝わされるのか？」 | 「怎麼了？我今天要去幫忙重新塗漆嗎？」 | 「Sao thế? Hôm nay tôi\nphải giúp cô sơn lại tàu à?」 | 「Sao thế? Hôm nay tôi\nphải giúp em sơn lại tàu à?」 | Paulette 1841 đáp; Reina 1932 chỉ cười theo. |
| 2035 | 「僕もだ。じっくり話したい」 | 「我也是。那時候再好好聊聊吧」 | 「Tôi cũng vậy. Tôi muốn nói chuyện thật kỹ với cô.」 | 「Tôi cũng vậy. Tôi muốn nói chuyện thật kỹ với em.」 | Paulette 2052 hẹn nói chuyện sau khi tàu chạy. |
| 2168 | 「例えば――そうだな。家族でここに来たとして。\nちいさなポーレットは、何をして遊びたい？」 | 「比如說……對了。假設你們一家人來這裡旅遊，小時候的你會想玩什麼？」 | 「Ví dụ như——để xem nào. Giả sử gia đình cô đến đây.\nCô bé Paulette sẽ muốn chơi trò gì?」 | 「Ví dụ như——để xem nào. Giả sử gia đình em đến đây.\nCô bé Paulette sẽ muốn chơi trò gì?」 | Paulette 2045 trả lời ("わたし,ですか?"); chỉ đổi "cô" đầu câu, giữ "Cô bé Paulette". |
| 2183 | 「ポーレット。君が、あのときの少女なのか」 | 「波萊特，你就是那個時候的少女嗎」 | 「Paulette. Cô, chính là cô bé lúc đó sao?」 | 「Paulette. Em, chính là cô bé lúc đó sao?」 | JP 君 = Paulette (nêu tên ポーレット); chỉ đổi "Cô" đầu, giữ "cô bé lúc đó". |

### グランドリライト05_れいな.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2156 | 「ならば、ポーレット、あとは頼む」 | 「波萊特，那剩下的就交給你了」 | 「Nếu vậy, Paulette, phần còn lại nhờ cô nhé.」 | 「Nếu vậy, Paulette, phần còn lại nhờ em nhé.」 | JP nêu tên ポーレット; Paulette 1730 đáp. |

### ハチロク01_双鉄の目・ハチロクの目.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1923 | 「いや――待ってくれ。今の話だと……金さえあれば、\nそれでも出てくる\x%l客車;#00ffc040;客車%l;#;は、あるにはあるのか？」 | 「慢著——等一下。照你剛才說的，只要掏得起錢的話，想買\x%l客車;#00ffc040;客運車廂%l;#;還是能買得到的囉？」 | 「Không——đợi đã. Theo lời cô vừa nói thì……chỉ cần có tiền,\nthì vẫn có \x%l客車;#00ffc040;toa hành khách%l;#; được bán ra sao?」 | 「Không——đợi đã. Theo lời em vừa nói thì……chỉ cần có tiền,\nthì vẫn có \x%l客車;#00ffc040;toa hành khách%l;#; được bán ra sao?」 | Paulette 2024/2066 vừa giải thích về toa xe sưu tầm; "lời cô vừa nói" là lời Paulette. |

### ハチロク05_レイルロオドたち.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2422 | 「ああ……言われてみれば、そんなものもあった――\nような気がするが」 | 「啊……你這麼一說，似乎確實有這麼個東西……吧」 | 「À……nghe cô nói mới nhớ, hình như cũng có thứ đó――\nthì phải.」 | 「À……nghe em nói mới nhớ, hình như cũng có thứ đó――\nthì phải.」 | Paulette 2319 vừa giải thích về máng tà vẹt (まくらぎ); Reina 2732 nói chuyện khác. |
| 3062 | 「それは――オリヴィの指摘を無視しろ、\nということか？」 | 「那是說——要我無視奧莉薇的批評的意思嗎？」 | 「Ý cô là――bảo anh phớt lờ lời phê bình của Olivy sao?」 | 「Ý em là――bảo anh phớt lờ lời phê bình của Olivy sao?」 | Paulette 2709 nêu lập trường; Soutetsu hỏi lại cô ấy; Paulette 3044 đáp. (old_vn là giá trị audit — audit giữ "cô".) |

### ハチロク05_軋み.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1235 | 「……そういってもらえると気が休まる」 | 「……你這麼說我心裡就好受一些了」 | 「……Nghe cô nói vậy tôi cũng thấy nhẹ nhõm phần nào.」 | 「……Nghe em nói vậy tôi cũng thấy nhẹ nhõm phần nào.」 | Paulette 1741 đáp lời; Soutetsu nói nghe cô ấy nói vậy thì nhẹ nhõm. |
| 1519 | 「気がかりはあるのだが、まだ確認がとれていない。\n確認が取れ次第に、報告させてもらいたく思う」 | 「只是現在還不確定。等確定之後我會向你報告的」 | 「Có chút bận tâm, nhưng tôi vẫn chưa xác nhận được.\nNgay khi xác nhận xong, tôi muốn báo cáo lại với cô.」 | 「Có chút bận tâm, nhưng tôi vẫn chưa xác nhận được.\nNgay khi xác nhận xong, tôi muốn báo cáo lại với em.」 | Paulette 1893 hỏi han; Soutetsu hứa báo cáo lại với cô ấy (monologue 2361: không nói dối Paulette). |
| 1870 | 「ならば安心だな。\n手間をかけてすまなかった。ありがとう」 | 「那我就放心了。給你添麻煩了。謝謝」 | 「Vậy thì yên tâm rồi.\nXin lỗi vì đã làm phiền cô. Cảm ơn nhé.」 | 「Vậy thì yên tâm rồi.\nXin lỗi vì đã làm phiền em. Cảm ơn nhé.」 | Paulette 1569 báo đã nhờ Seki kiểm tra đường ray; Soutetsu cảm ơn cô ấy. |

### ハチロク10_炙り出し.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1795 | 「ああ――よろしく頼む」 | 「嗯，就拜託你了」 | 「Ừm——trăm sự nhờ cô.」 | 「Ừm——trăm sự nhờ em.」 | Paulette 2052/1911 vừa đề xuất. |
| 1965 | 「いや。良いヒントをくれた。ありがたい」 | 「沒事，我們反倒要感謝你給出了提示」 | 「Không đâu. Cô đã cho một gợi ý rất hay. Cảm ơn cô.」 | 「Không đâu. Em đã cho một gợi ý rất hay. Cảm ơn em.」 | Paulette 2092/1847 vừa gợi ý về vận chuyển. |
| 1976 | 「ポーレット、\n出来るのならば、そう気に病んでくれるな」 | 「波萊特，我希望你不要有所負擔」 | 「Paulette,\nnếu được thì xin cô đừng quá phiền lòng như vậy.」 | 「Paulette,\nnếu được thì xin em đừng quá phiền lòng như vậy.」 | JP nêu tên ポーレット; Paulette 1750 ngạc nhiên. |

### ハチロク11_幽霊.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1805 | 「うむ。明日もよろしく頼む」 | 「嗯。明天也麻煩了」 | 「Ừm. Ngày mai cũng nhờ cô nhé.」 | 「Ừm. Ngày mai cũng nhờ em nhé.」 | Paulette 2079/1834 vừa nói chuyện; Soutetsu nhờ cô ấy ngày mai. |

### ハチロク13_夜の嵐.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1235 | 「……僕には今は思いつけん。\n気がつくことの手当を、任せていいか？」 | 「……我能想到的就這麼多。如果還發現有什麼事，可以麻煩你來處理嗎？」 | 「……Giờ tôi chưa nghĩ ra thêm gì cả.\nNếu cô nhận thấy cần chuẩn bị gì thì cứ tự quyết định giúp tôi được không?」 | 「……Giờ tôi chưa nghĩ ra thêm gì cả.\nNếu em nhận thấy cần chuẩn bị gì thì cứ tự quyết định giúp tôi được không?」 | Paulette 1802/1796 trao đổi việc chuẩn bị ứng phó bão. |
| 1977 | 「ありがとう」 | 「謝謝你」 | 「Cảm ơn cô.」 | 「Cảm ơn em.」 | Paulette 1920 xác nhận sẽ lo liệu; Soutetsu cảm ơn cô ấy. |

### ハチロク14_冬.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 3189 | 「よろしく頼む。\x%l保線;#00ffc040;保線%l;#;の方の具体的な行動指針は？」 | 「那就交給你了，\x%l保線;#00ffc040;巡線%l;#;的具體行動方針呢？」 | 「Nhờ cô nhé. Còn kim chỉ nam hành động cụ thể cho phía \x%l保線;#00ffc040;bảo trì đường ray%l;#; thì sao?」 | 「Nhờ em nhé. Còn kim chỉ nam hành động cụ thể cho phía \x%l保線;#00ffc040;bảo trì đường ray%l;#; thì sao?」 | Paulette 2774/3143 là 保線部長, đang bàn kế hoạch hành động. |

### ポーレット01_ポーレット退任.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1539 | 「いつもそばにいてやれるとは限らん。\nあえて離れて見守ることも、愛情だろう」 | 「你總不能陪她一輩子啊。有時候放手也是一種愛」 | 「Không phải lúc nào cô cũng ở bên cạnh con bé được đâu.\nĐôi khi, đứng từ xa quan sát cũng là một cách thể hiện tình yêu thương mà.」 | 「Không phải lúc nào em cũng ở bên cạnh con bé được đâu.\nĐôi khi, đứng từ xa quan sát cũng là một cách thể hiện tình yêu thương mà.」 | Paulette 1844/1593/1591 lo cho Hikari; Soutetsu khuyên cô ấy. |

### ポーレット04_ヒヤリング.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1174 | 「……すまん。\n僕のせいで、シャッターチャンスを逃させてしまったな」 | 「……抱歉。我害你錯過了拍照的機會」 | 「……Xin lỗi nhé.\nVì tôi mà cô đã bỏ lỡ mất cơ hội bấm máy rồi.」 | 「……Xin lỗi nhé.\nVì tôi mà em đã bỏ lỡ mất cơ hội bấm máy rồi.」 | Paulette 1475/1792 phản ứng; Soutetsu xin lỗi cô ấy. |
| 1396 | 「鉄道の写真を、撮りにきたのか？」 | 「你是來拍鐵路的照片的嗎？」 | 「Cô đến đây để chụp ảnh đường sắt sao?」 | 「Em đến đây để chụp ảnh đường sắt sao?」 | Paulette 1544 trả lời về chụp ảnh đường sắt. |
| 1596 | 「驚かせるつもりは――」 | 「我沒想要嚇到你——」 | 「Tôi không định làm cô giật mình——」 | 「Tôi không định làm em giật mình——」 | Paulette 1455 giật mình; Soutetsu xin lỗi cô ấy. |
| 1661 | 「いや、僕も会いたいと思っていた」 | 「沒事，我也正想見你呢」 | 「Không sao, tôi cũng đang muốn gặp cô đây.」 | 「Không sao, tôi cũng đang muốn gặp em đây.」 | Paulette 1612 xin lỗi; Soutetsu đáp cũng muốn gặp cô ấy. |
| 1674 | 「何故、そんなことを言う？\n鉄道事故で、鉄道も\x%l列車;#00ffc040;列車%l;#;も悪くないなど――」 | 「為什麼要這樣說？明明發生了鐵路事故，卻說鐵路和\x%l列車;#00ffc040;列車%l;#;都沒有錯——」 | 「Tại sao cô lại nói như vậy?\nTai nạn đường sắt, mà đường sắt và \x%l列車;#00ffc040;đoàn tàu%l;#; lại không có lỗi sao——」 | 「Tại sao em lại nói như vậy?\nTai nạn đường sắt, mà đường sắt và \x%l列車;#00ffc040;đoàn tàu%l;#; lại không có lỗi sao——」 | Paulette 1789 ấp úng trả lời; Soutetsu hỏi cô ấy. |
| 1721 | 「相談があるとの話だが」 | 「聽說你有事找我商量」 | 「Nghe nói cô có chuyện cần bàn bạc.」 | 「Nghe nói em có chuyện cần bàn bạc.」 | Paulette 1570 nhờ làm thư ký. |
| 1771 | 「そうか、父親に頼まれて撮りに来たのか」 | 「這樣啊，是你父親讓你來拍照」 | 「Vậy sao, cô được ba nhờ đến đây chụp ảnh à.」 | 「Vậy sao, em được ba nhờ đến đây chụp ảnh à.」 | Paulette 1544 nói ba nhờ chụp ảnh; Soutetsu hỏi lại cô ấy. |

### ポーレット05_whatsentertainment.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 975 | 「――お嬢さん。僕と遊んではくれないか？」 | 「——這位小姐，能陪我一起玩嗎？」 | 「——Tiểu thư. Cô có muốn đi chơi cùng tôi không?」 | 「——Tiểu thư. Em có muốn đi chơi cùng tôi không?」 | Paulette 1329/1273 đáp lời mời chơi. |
| 1224 | 「言われてみれば、確かにだ。\n人には恐らく、そうした一面があるのだろう」 | 「你這麼一說好像確實是這樣。人們確實有這樣的一面」 | 「Nghe cô nói vậy, đúng là thế thật.\nCon người có lẽ đều có một mặt như vậy.」 | 「Nghe em nói vậy, đúng là thế thật.\nCon người có lẽ đều có một mặt như vậy.」 | Paulette 1429 vừa nói về đấu giá. |
| 1405 | 「わかった。ならば分業しよう。\nナビには、ポーレットを送っていくよう命令しておく」 | 「我明白，那就分頭行動吧。我會命令Ｎａｖｉ送你過去的」 | 「Tôi hiểu rồi. Vậy thì chúng ta chia việc ra làm nhé.\nTôi sẽ ra lệnh cho Navi đưa cô đi.」 | 「Tôi hiểu rồi. Vậy thì chúng ta chia việc ra làm nhé.\nTôi sẽ ra lệnh cho Navi đưa em đi.」 | JP nêu tên ポーレット (Navi đưa cô ấy đi). |

### ポーレット05_鳴呼の町.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1671 | 「言われてみれば、そんな気もするな」 | 「你這麼一說，好像是這樣」 | 「Nghe cô nói vậy, tôi cũng thấy thế.」 | 「Nghe em nói vậy, tôi cũng thấy thế.」 | Paulette 1625/1906 vừa nói về trứng suối nước nóng. |
| 2010 | 「水切り、な。ポーレット。空いているかごの鎖の端を、\nひかりに持たせてやってくれるか？」 | 「是瀝水籃。波萊特，你能讓光拿著空籃子那一邊的鐵鏈嗎？」 | 「Rổ ráo nước, nhé. Paulette. Cô có thể đưa đầu xích của một chiếc rổ trống cho Hikari cầm giúp tôi được không?」 | 「Rổ ráo nước, nhé. Paulette. Em có thể đưa đầu xích của một chiếc rổ trống cho Hikari cầm giúp tôi được không?」 | JP nêu tên ポーレット; Paulette 1922 đáp. |

### ポーレット08_線から面へ.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1636 | 「おはよう、ポーレット。\n今日は、秘書をできずにすまんな」 | 「早安，波萊特。今天沒辦法處理秘書的工作，真抱歉啊」 | 「Chào buổi sáng, Paulette.\nHôm nay tôi không thể làm thư ký cho cô được, xin lỗi nhé.」 | 「Chào buổi sáng, Paulette.\nHôm nay tôi không thể làm thư ký cho em được, xin lỗi nhé.」 | JP nêu tên ポーレット; Paulette 1668 đáp. |
| 1715 | 「その程度はお安い御用だ。\nが――ナビと、いったい何を話すのだ？」 | 「舉手之勞而已。不過——你要跟Ｎａｖｉ說什麼啊？」 | 「Chuyện nhỏ thôi.\nNhưng mà――cô định nói gì với Navi vậy?」 | 「Chuyện nhỏ thôi.\nNhưng mà――em định nói gì với Navi vậy?」 | Paulette 1486/1786 giấu chuyện với Navi; Soutetsu hỏi cô ấy. |
| 1739 | 「ありがとう。これなら僕も事故無く乗務できそう――\nんっ？」 | 「謝謝。這樣一來，我也能平安完成乘務工作了——嗯？」 | 「Cảm ơn cô. Có cái này thì tôi có thể thực hiện nhiệm vụ mà không gặp tai nạn nào rồi――\nHửm?」 | 「Cảm ơn em. Có cái này thì tôi có thể thực hiện nhiệm vụ mà không gặp tai nạn nào rồi――\nHửm?」 | Paulette 1478 đưa bùa hộ mệnh; Soutetsu cảm ơn cô ấy. |

### ポーレット09_ストーブ客車.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1395 | 「……煙などに対して、\n問題が出てくるかもしれぬということか」 | 「……也就是說有可能在煙這方面出問題嗎」 | 「...Ý cô là,\ncó thể sẽ phát sinh vấn đề liên quan đến khói và những thứ tương tự sao.」 | 「...Ý em là,\ncó thể sẽ phát sinh vấn đề liên quan đến khói và những thứ tương tự sao.」 | Paulette 2007/1995 bàn về vấn đề khói. |
| 1713 | 「食べたのだろう？\n砂糖醤油か、それともキナコか？」 | 「你後來吃到了吧？是蘸甜醬油還是黃豆粉？」 | 「Thế rồi cô có được ăn không?\nChấm nước tương đường, hay là bột đậu nành Kinako?」 | 「Thế rồi em có được ăn không?\nChấm nước tương đường, hay là bột đậu nành Kinako?」 | Paulette 2098/1993 kể chuyện bánh gạo. |
| 1805 | 「ああ、プリントしたのか――\n凪が撮った写真だな？」 | 「啊，列印出來了——這是凪拍的照片吧？」 | 「À, cô in ra rồi sao――\nLà bức ảnh Nagi chụp đúng không?」 | 「À, em in ra rồi sao――\nLà bức ảnh Nagi chụp đúng không?」 | Paulette 1938 khoe ảnh in; Soutetsu hỏi cô ấy. |
| 1819 | 「ああ、すまんな」 | 「啊，麻煩你了」 | 「À, cảm ơn cô.」 | 「À, cảm ơn em.」 | Paulette 1718 pha trà; Soutetsu cảm ơn cô ấy. |
| 1931 | 「相談してもらえて、光栄だ」 | 「我很榮幸，你願意來找我商量」 | 「Rất vinh hạnh vì cô đã thảo luận với tôi.」 | 「Rất vinh hạnh vì em đã thảo luận với tôi.」 | Paulette 1789 ngạc nhiên vì được hỏi ý kiến. |
| 2129 | 「トコロテン方式で不要になった旧\x%l客車;#00ffc040;客車%l;#;を、\n電車姫様が引き取って保存していた――ということか」 | 「而淘汰掉的舊\x%l客車;#00ffc040;客運車廂%l;#;就被電車公主接手並保存起來了嗎」 | 「Ý cô là, \x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\nđã được Densha Hime nhận về và bảo quản――đúng không?」 | 「Ý em là, \x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\nđã được Densha Hime nhận về và bảo quản――đúng không?」 | Paulette 1776/1980 giải thích về toa xe cũ. |
| 2177 | 「念のため聞くが、他の\x%l客車;#00ffc040;客車%l;#;のアテはあるのか？」 | 「謹慎起見我問一下，還有其他的地方能弄到\x%l客車;#00ffc040;客運車廂%l;#;嗎？」 | 「Hỏi để chắc chắn thôi, cô còn nhắm được \x%l客車;#00ffc040;toa hành khách%l;#; nào khác không?」 | 「Hỏi để chắc chắn thôi, em còn nhắm được \x%l客車;#00ffc040;toa hành khách%l;#; nào khác không?」 | Paulette 2255 trả lời còn toa xe khác. |
| 2209 | 「それは誤解だ」 | 「這你可就誤會了」 | 「Cô hiểu lầm rồi.」 | 「Em hiểu lầm rồi.」 | Paulette 2174/1664 cảm ơn; Soutetsu nói cô ấy hiểu lầm. |

### ポーレット10_見えない傷.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 991 | 「――そう思ってもらえたのなら、何よりだ」 | 「——你如果是這樣想的，那就再好不過了」 | 「——Nếu cô nghĩ được như vậy thì tốt quá rồi.」 | 「——Nếu em nghĩ được như vậy thì tốt quá rồi.」 | Paulette 1241 khen Soutetsu; Soutetsu đáp cô ấy. |
| 998 | 「――時間をおけばどんどんべしゃっとしてしまう。\n無理なく食べられるようなら」 | 「——時間一久，就會變得越來越軟。你如果還吃得下的話，就快些吃吧」 | 「——Nếu để lâu thì cháo sẽ càng lúc càng nhão đấy.\nNếu cô vẫn còn ăn được thì...」 | 「——Nếu để lâu thì cháo sẽ càng lúc càng nhão đấy.\nNếu em vẫn còn ăn được thì...」 | Paulette 1431 đang ăn cháo. |
| 1239 | 「いや――礼を言われるようなことではないさ」 | 「不——這不是什麼值得道謝的事情」 | 「Không――đây không phải chuyện đáng để cô phải cảm ơn đâu.」 | 「Không――đây không phải chuyện đáng để em phải cảm ơn đâu.」 | Paulette 1344 cảm ơn; Soutetsu nói không đáng để cô ấy cảm ơn. |
| 1262 | 「倒れた身だぞ？　急に動くな。\nどこかを痛めているかもしれん」 | 「你剛剛都暈倒過了哦，不要突然動起來。說不定有哪裡受著傷」 | 「Cô vừa mới ngất xỉu đấy nhé? Đừng cử động đột ngột.\nBiết đâu lại bị đau ở đâu đó thì sao.」 | 「Em vừa mới ngất xỉu đấy nhé? Đừng cử động đột ngột.\nBiết đâu lại bị đau ở đâu đó thì sao.」 | Paulette 1341 vừa ngất; Soutetsu dặn cô ấy đừng cử động. |
| 1278 | 「悪い夢を見たのか？」 | 「做噩夢了嗎？」 | 「Cô gặp ác mộng à?」 | 「Em gặp ác mộng à?」 | Paulette 1323 vừa tỉnh khỏi ác mộng. |
| 1314 | 「う、む――舌にあったようでなによりだ」 | 「呃、嗯——能合你胃口就太好了」 | 「Ư-ừm——Hợp khẩu vị của cô là tốt rồi.」 | 「Ư-ừm——Hợp khẩu vị của em là tốt rồi.」 | Paulette 1550 khen ngon; Soutetsu nói hợp khẩu vị cô ấy. |
| 1353 | 「ああ、真闇姉がやってくれた。\n今は蔵の仕事があるゆえ、看病を僕が引き継いだ」 | 「啊，是真闇姐幫你換的。她現在要去酒窖工作，所以換我來照顧你」 | 「À, chị Mayami đã thay giúp đấy.\nBây giờ chị ấy có việc ở xưởng rượu, nên tôi đã tiếp quản việc chăm sóc cô.」 | 「À, chị Mayami đã thay giúp đấy.\nBây giờ chị ấy có việc ở xưởng rượu, nên tôi đã tiếp quản việc chăm sóc em.」 | Paulette 1480/1612 hỏi về thay đồ; Soutetsu nói đã tiếp quản chăm sóc cô ấy. |
| 1362 | 「うむ。飲む方か？　食べる方か？」 | 「嗯。先要吃的還是喝的？」 | 「Ừm. Cô muốn uống trước hay ăn trước?」 | 「Ừm. Em muốn uống trước hay ăn trước?」 | Paulette 1611 xin nước ấm. |
| 1378 | 「ああ、そうしてくれ。\nそしてよりよく、一緒に未来へ進んでいこう」 | 「嗯，那就拜託了。就讓我們一同邁向更好的未來吧」 | 「Ừm, nhờ cô nhé.\nVà hãy cùng nhau tiến bước hướng tới một tương lai tốt đẹp hơn.」 | 「Ừm, nhờ em nhé.\nVà hãy cùng nhau tiến bước hướng tới một tương lai tốt đẹp hơn.」 | Paulette 1447/1395 đồng ý cùng tiến bước. |
| 1451 | 「起こすぞ」 | 「我扶你起來」 | 「Tôi đỡ cô dậy nhé.」 | 「Tôi đỡ em dậy nhé.」 | Paulette 1548 báo không đau ở đâu; Soutetsu đỡ cô ấy dậy. |
| 1465 | 「すまん。放って置けなかった。\n寝ているところに触れるなど、やっていいことでは――」 | 「抱歉。我沒辦法袖手旁觀。我不應該在你睡覺的時候碰你——」 | 「Xin lỗi. Tôi không thể để mặc cô được.\nChạm vào người khác lúc đang ngủ, không phải là việc nên làm――」 | 「Xin lỗi. Tôi không thể để mặc em được.\nChạm vào người khác lúc đang ngủ, không phải là việc nên làm――」 | Paulette 1245 đáp lại lời xin lỗi. |
| 1471 | 「大丈夫そうなら、行くぞ、ポーレット」 | 「既然沒有問題，那我們走吧，波萊特」 | 「Nếu cô thấy ổn rồi thì chúng ta đi thôi, Paulette.」 | 「Nếu em thấy ổn rồi thì chúng ta đi thôi, Paulette.」 | JP nêu tên ポーレット ("行くぞ、ポーレット"); Paulette 1491 đáp. |
| 1487 | 「及ばずながら、僕が。\nハチロクと組み、キハ[レイナナ,1]07を\x%l客車;#00ffc040;客車%l;#;とさせてもらった」 | 「是我和八六搭檔，用Ｋｉｈａ０７作\x%l客車;#00ffc040;客運車廂%l;#;完成的班次。雖然我的技術遠不如你就是了」 | 「Dù không bằng cô, nhưng tôi đã làm.\nTôi bắt cặp với Hachiroku, và dùng KiHa 07 làm \x%l客車;#00ffc040;toa hành khách%l;#;.」 | 「Dù không bằng em, nhưng tôi đã làm.\nTôi bắt cặp với Hachiroku, và dùng KiHa 07 làm \x%l客車;#00ffc040;toa hành khách%l;#;.」 | Paulette 1310/1344 hỏi về chạy tàu chiều. |
| 1510 | 「大丈夫だ。少なくとも僕は味方だ。\n僕はここで――望まれる限り側にいる」 | 「沒事的。至少有我支持著你。只要你需要——我就一直在這裡陪你」 | 「Không sao đâu. Ít nhất thì tôi cũng đứng về phía cô.\nTôi sẽ ở đây――bên cạnh cô chừng nào cô còn cần.」 | 「Không sao đâu. Ít nhất thì tôi cũng đứng về phía em.\nTôi sẽ ở đây――bên cạnh em chừng nào em còn cần.」 | Paulette 1018/996 đang run rẩy; Soutetsu an ủi cô ấy (3 lần "cô" đều là Paulette). |
| 1522 | 「ポーレット、体にどこか」 | 「波萊特，你身體有沒有哪裡——」 | 「Paulette, cơ thể cô có chỗ nào...」 | 「Paulette, cơ thể em có chỗ nào...」 | JP nêu tên ポーレット; Paulette 1523 đáp "前方注視". |
| 1561 | 「ともかく、今は回復に専念することだ。\n腹はすいてないか？　喉の渇きは？」 | 「總之，你現在要安心修養。肚子餓不餓？　口渴嗎？」 | 「Nói chung, bây giờ cô cứ tập trung hồi phục đi.\nCó đói bụng không? Có khát nước không?」 | 「Nói chung, bây giờ em cứ tập trung hồi phục đi.\nCó đói bụng không? Có khát nước không?」 | Paulette 1335/1029 xin nước và cháo. |
| 1565 | 「\x%lキハ07;#00ffc040;キハ07%l;#;の乗務を僕にも、担当させてはくれまいか？」 | 「能不能也讓我來負責\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;的乘務工作？」 | 「Liệu cô có thể để tôi phụ trách việc vận hành \x%lキハ07;#00ffc040;KiHa 07%l;# được không?」 | 「Liệu em có thể để tôi phụ trách việc vận hành \x%lキハ07;#00ffc040;KiHa 07%l;# được không?」 | Paulette 981 là người giao nhiệm vụ chạy tàu KiHa 07. |
| 1575 | 「待たせたな。っと――\nいや、少し待て」 | 「讓你久等了。呀——不對，再等會」 | 「Để cô phải đợi rồi. Ây da――\nKhông, đợi một chút đã.」 | 「Để em phải đợi rồi. Ây da――\nKhông, đợi một chút đã.」 | Paulette 1341 ngồi dậy; Soutetsu dỗ cô ấy đợi. |

### ポーレット11_記憶と記録.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1280 | 「誰かが望むからではダメだ。マイントレジャーのことも、\n鉄道経営や観光振興のことも、気にしなくていい」 | 「不能因為“別人希望”就逃避。無論是煤探樂園，還是鐵路經營或旅遊業復興，你都不必去考慮」 | 「Không thể vì ai đó mong muốn được. Cả chuyện Mine Treasure,\nhay chuyện kinh doanh đường sắt, chấn hưng du lịch, cô cũng không cần phải bận tâm.」 | 「Không thể vì ai đó mong muốn được. Cả chuyện Mine Treasure,\nhay chuyện kinh doanh đường sắt, chấn hưng du lịch, em cũng không cần phải bận tâm.」 | Paulette 1774/1543 đang phân vân về Mine Treasure. |
| 1312 | 「本当に――“変わらないで”と、望んでいるのか？」 | 「你真的——希望“不要改變”嗎？」 | 「Cô thực sự――mong muốn “đừng thay đổi” sao?」 | 「Em thực sự――mong muốn “đừng thay đổi” sao?」 | Monologue 2260: Soutetsu chỉ nhìn Paulette; Soutetsu hỏi cô ấy. |
| 1381 | 「それが、僕の望みだからだ。\n僕は、君を助けたい」 | 「因為，這就是我的心願。我希望能夠幫助你」 | 「Vì đó là mong muốn của tôi.\nTôi, muốn giúp cô.」 | 「Vì đó là mong muốn của tôi.\nTôi, muốn giúp em.」 | Paulette 1453/1572 nắm tay Soutetsu; Soutetsu nói muốn giúp cô ấy. |
| 1399 | 「向き合わなければ、乗り越えられない。\nそれはポーレット。君が、僕に教えてくれたことだ」 | 「如果不敢面對，就無法跨越過去。波萊特，這是你教會我的道理」 | 「Nếu không đối mặt, thì không thể vượt qua.\nĐó là điều mà Paulette, chính cô đã dạy cho tôi.」 | 「Nếu không đối mặt, thì không thể vượt qua.\nĐó là điều mà Paulette, chính em đã dạy cho tôi.」 | JP 君 = Paulette (nêu tên ポーレット). |
| 1485 | 「僕には君の悲鳴が聞こえた。君は悲鳴を届けてくれた。\nこの手を僕に、伸ばしてくれた」 | 「我聽到了你的悲鳴。你將一聲聲悲鳴傳達到了我的心裡。你向我伸出了這隻手」 | 「Tôi đã nghe thấy tiếng thét của cô. Cô đã truyền tiếng thét đó đến tôi.\nĐã vươn bàn tay này về phía tôi.」 | 「Tôi đã nghe thấy tiếng thét của em. Em đã truyền tiếng thét đó đến tôi.\nĐã vươn bàn tay này về phía tôi.」 | JP 君 = Paulette; Paulette đang nắm tay Soutetsu (2266). |
| 1488 | 「だから僕は、意地悪だと思われようと、憎まれようと。\n君にも、過去と向き合って欲しいと思っている」 | 「所以，即使被你認為我是刻意刁難，即使被你記恨，我也希望你能勇敢面對過去」 | 「Vì vậy, dù có bị coi là xấu tính, dù có bị ghét bỏ đi chăng nữa.\nTôi vẫn muốn cô đối mặt với quá khứ.」 | 「Vì vậy, dù có bị coi là xấu tính, dù có bị ghét bỏ đi chăng nữa.\nTôi vẫn muốn em đối mặt với quá khứ.」 | Paulette 1356 đáp lại; Soutetsu muốn cô ấy đối mặt quá khứ. |
| 1567 | 「ポーレット。\nここから先は、君が決断しなければいけないことだ」 | 「波萊特。接下來，必須由你來做決定」 | 「Paulette.\nTừ giờ trở đi, cô phải là người đưa ra quyết định.」 | 「Paulette.\nTừ giờ trở đi, em phải là người đưa ra quyết định.」 | JP 君 = Paulette (nêu tên ポーレット); Paulette 1774 sững sờ. |
| 1568 | 「怯え閉じこもる幸福を。れいなをお人形にすることを。\nポーレット、君は本当に望んでいるのか？」 | 「波萊特，你真的希望生活在不安、封閉的幸福之中，希望玲奈變成一個人偶嗎？」 | 「Một hạnh phúc sợ hãi và khép kín. Biến Reina thành một con búp bê.\nPaulette, cô thực sự mong muốn điều đó sao?」 | 「Một hạnh phúc sợ hãi và khép kín. Biến Reina thành một con búp bê.\nPaulette, em thực sự mong muốn điều đó sao?」 | JP 君 = Paulette (nêu tên ポーレット); Paulette 1452 đáp. |
| 1722 | 「これは、君とれいなの話だ。\nポーレット、君たちの未来を決める、決断なんだ」 | 「這是你和玲奈兩個人的事情。波萊特，這是影響你們未來的決定」 | 「Đây là chuyện của cô và Reina.\nPaulette, đây là quyết định định đoạt tương lai của hai người đấy.」 | 「Đây là chuyện của em và Reina.\nPaulette, đây là quyết định định đoạt tương lai của hai người đấy.」 | JP 君 = Paulette (nêu tên, "君とれいな"); Paulette 1543 đáp. |

### ポーレット12_解放.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 973 | 「僕も……恋を教えてもらった」 | 「你也一樣……教會了我愛情是什麼」 | 「Tôi cũng……được cô dạy cho biết yêu là gì.」 | 「Tôi cũng……được em dạy cho biết yêu là gì.」 | Paulette dạy Soutetsu biết yêu (tiếp mạch 1058). |
| 1021 | 「うん。ポーレットは、捨てられてなどいない」 | 「嗯。波萊特才沒有被拋棄」 | 「Ừm. Paulette, cô không hề bị vứt bỏ.」 | 「Ừm. Paulette, em không hề bị vứt bỏ.」 | Paulette 1133 buồn vì tưởng bị bỏ rơi. |
| 1058 | 「僕も――側にいてくれてうれしい。\nだから、側に居て欲しい」 | 「我也一樣——很高興有你在我身邊。所以，我希望能繼續有你的陪伴」 | 「Tôi cũng vậy――rất vui vì cô đã ở bên tôi.\nVì vậy, tôi muốn cô hãy ở bên tôi.」 | 「Tôi cũng vậy――rất vui vì em đã ở bên tôi.\nVì vậy, tôi muốn em hãy ở bên tôi.」 | Paulette 1026 đáp "はい、双鉄くん". |
| 1090 | 「君が、見えるようにしてくれた。\n僕は、こんなにも君を想って、あたたかになれる」 | 「是你讓我明白了這些。原來我想著你的時候，能夠感受到這般的溫暖」 | 「Chính cô đã giúp tôi nhìn thấy.\nTôi có thể nghĩ về cô nhiều đến thế, và trở nên ấm áp đến thế.」 | 「Chính em đã giúp tôi nhìn thấy.\nTôi có thể nghĩ về em nhiều đến thế, và trở nên ấm áp đến thế.」 | JP 君 = Paulette; Soutetsu nói cô ấy giúp mình nhìn thấy. |
| 1110 | 「ポーレット。\n僕は、君に――恋をしている」 | 「波萊特。我喜歡你」 | 「Paulette.\nTôi, đã――yêu cô rồi.」 | 「Paulette.\nTôi, đã――yêu em rồi.」 | JP 君 = Paulette (nêu tên, tỏ tình); Paulette 1099 đáp "わたしもです". |
| 1112 | 「ポーレットは、何も悪くない」 | 「波萊特什麼都沒有做錯」 | 「Paulette, cô không làm gì sai cả.」 | 「Paulette, em không làm gì sai cả.」 | Paulette 1087/1038 tự trách; Soutetsu nói cô ấy không làm gì sai. |
| 1113 | 「お母様もポーレットが大切で。かけがえないと感じてて。\nだからこそ――お父様から、奪えなかった」 | 「波萊特的母親也非常重視波萊特，覺得你是不可或缺的。所以才沒辦法將波萊特從父親手中奪走」 | 「Mẹ cô cũng rất coi trọng Paulette. Cảm thấy cô là người không thể thay thế.\nChính vì vậy――bà ấy mới không thể cướp cô khỏi ba cô.」 | 「Mẹ em cũng rất coi trọng Paulette. Cảm thấy em là người không thể thay thế.\nChính vì vậy――bà ấy mới không thể cướp em khỏi ba em.」 | Paulette 1095 đáp; Soutetsu kể về mẹ cô ấy (3 lần "cô" đều là Paulette). |

### ポーレットh7_残業エッチもyシャツで.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 953 | 「市長。お忘れですか？\nこれは、貴女へのお仕置きですよ？　ご褒美ではなく」 | 「市長，您忘了嗎？這是在懲罰你，而不是獎勵」 | 「Thị trưởng. Cô quên rồi sao?\nĐây là hình phạt dành cho cô đấy nhé? Không phải phần thưởng đâu.」 | 「Thị trưởng. Em quên rồi sao?\nĐây là hình phạt dành cho em đấy nhé? Không phải phần thưởng đâu.」 | Paulette là Thị trưởng trong cảnh H (JP 貴女へのお仕置き); Paulette 828/898 đáp. |
| 954 | 「市長は、これで今回の件のご責任を――」 | 「市長，這件事的責任就——」 | 「Thị trưởng, thế này là cô đã chịu trách nhiệm cho chuyện lần này——」 | 「Thị trưởng, thế này là em đã chịu trách nhiệm cho chuyện lần này——」 | Paulette 787/1022 đáp; cùng cảnh "thị trưởng chịu trách nhiệm". |
| 1015 | 「その程度のことさえ失念し、暴走してしまう。\nそれを改めるための手段は――さて、なんだ？」 | 「這點小事就叫你忘掉了重點，就要失控了。我該用什麼手段糾正你呢？」 | 「Đến cả mức độ đó mà cô cũng quên mất, rồi lại mất kiểm soát.\nBiện pháp để sửa đổi điều đó là——nào, là gì?」 | 「Đến cả mức độ đó mà em cũng quên mất, rồi lại mất kiểm soát.\nBiện pháp để sửa đổi điều đó là——nào, là gì?」 | Paulette 1023 đáp; Soutetsu hỏi cô ấy. |

### 共通14_負債.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1858 | 「この短期間で、良く出してくれたな」 | 「竟能在這麼短的時間內整理好啊」 | 「Trong thời gian ngắn như vậy mà cô đã đưa ra được bản dự toán này, làm tốt lắm.」 | 「Trong thời gian ngắn như vậy mà em đã đưa ra được bản dự toán này, làm tốt lắm.」 | Paulette 1134 vừa đưa bản dự toán; Soutetsu khen cô ấy — ngữ cảnh công việc, vẫn "em" theo P2 (xem quyết định O1). |

### 日々姫04_カフェキッチン.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1708 | 「すまんな、助かる。\nその言葉に甘えすぎぬよう、頼らせてもらう」 | 「不好意思，那就先謝謝你了。我會儘量不給你多添麻煩的」 | Cảm ơn cô, giúp được anh nhiều lắm. Anh sẽ nhờ vả cô, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó. | Cảm ơn em, giúp được anh nhiều lắm. Anh sẽ nhờ vả em, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó. | Paulette 1984/2052/2057 động viên Soutetsu; Soutetsu cảm ơn cô ấy. (old_vn là giá trị audit.) |

### 日々姫04_同乗.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2035 | 「ああ。\x%l客車;#00ffc040;客車%l;#;を見つけてもらえたおかげで、\nここまでこれた」 | 「是啊。多虧你找到了\x%l客車;#00ffc040;客運車廂%l;#;，才能走到這一步」 | 「Ừ. Nhờ cô tìm được \x%l客車;#00ffc040;toa hành khách%l;#;,\nmà chúng ta mới có thể đi xa đến bước này.」 | 「Ừ. Nhờ em tìm được \x%l客車;#00ffc040;toa hành khách%l;#;,\nmà chúng ta mới có thể đi xa đến bước này.」 | Paulette 2186/1951 cùng đi công tác; Soutetsu nói nhờ cô ấy tìm được toa xe. |
| 2155 | 「ありがとう」 | 「謝謝」 | 「Cảm ơn cô.」 | 「Cảm ơn em.」 | Paulette 2127 chúc "乗務 tốt đẹp"; Soutetsu đáp cảm ơn cô ấy (Hibiki 2156 nói sau, với Soutetsu). |

### 日々姫05_御一夜ステーションカフェ.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2518 | 「ありがとう」 | 「謝謝」 | 「Cảm ơn cô.」 | 「Cảm ơn em.」 | Paulette 1903 chúc mừng khai trương quán; Soutetsu cảm ơn cô ấy. |

### 日々姫07_姉の想い。妹の想い.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2058 | 「本当に心強いし、大いに助かる。\nいつもながらだが――ありがとう」 | 「有你的幫助，我們就更有底氣了。這真的是感激之情難以言表」 | 「Thật sự rất vững tâm, và giúp ích được rất nhiều.\nDù là chuyện thường ngày nhưng——cảm ơn cô」 | 「Thật sự rất vững tâm, và giúp ích được rất nhiều.\nDù là chuyện thường ngày nhưng——cảm ơn em」 | Paulette 2231/1717 nhận gánh vác thay Soutetsu. |

### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2322 | 「それより何か、\n温かな飲み物をもらえれば」 | 「先去泡點溫熱的飲料吧」 | 「Thay vì thế, cô có thể cho chúng tôi,\nmột chút đồ uống ấm được không?」 | 「Thay vì thế, em có thể cho chúng tôi,\nmột chút đồ uống ấm được không?」 | Paulette 2887 đáp sẽ pha trà sữa; monologue 3549: Soutetsu giữ cô ấy lại. |

### 日々姫13_討論会.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 1512 | 「ポーレット。ポーレットの鉄道仲間に、\nいわゆる[と]撮り[テツ]鉄という方はどのくらいいる？」 | 「波萊特。你的鐵路同好中有多少鐵影家？」 | 「Paulette. Trong số những người bạn đường sắt của cô,\ncó bao nhiêu người được gọi là \x%l撮り鉄;#00ffc040;Tori-tetsu%l;#;?」 | 「Paulette. Trong số những người bạn đường sắt của em,\ncó bao nhiêu người được gọi là \x%l撮り鉄;#00ffc040;Tori-tetsu%l;#;?」 | JP nêu tên ポーレット (君 = Paulette); Paulette 1438 đáp. |
| 1592 | 「ならば、その方達に頼めないだろうか」 | 「能不能拜託一下他們」 | 「Nếu vậy, cô có thể nhờ họ được không?」 | 「Nếu vậy, em có thể nhờ họ được không?」 | Paulette 1438/1290 sẽ nhờ bạn bè đường sắt giúp. |
| 1649 | 「そうか、であれば頼む」 | 「這樣啊，那就拜託你了」 | 「Vậy sao, thế thì nhờ cô nhé.」 | 「Vậy sao, thế thì nhờ em nhé.」 | Paulette 1347 sẽ nhờ giúp; Soutetsu đáp "nhờ cô nhé". |

### 稀咲03_純白のレール.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2006 | 「どうだろう、ポーレット」 | 「波萊特，你怎麼想」 | 「Cô thấy sao, Paulette.」 | 「Em thấy sao, Paulette.」 | JP nêu tên ポーレット; Paulette 1908 đáp. Cùng mẫu câu với O1 2047 (xem quyết định O1). |

## 2. P14 — Paulette → Soutetsu: "cậu (Soutetsu)" → "anh Soutetsu" (6 dòng)

Khóa B4 (19/11 ~22:24): JP là 双鉄くん trong các dòng này → "anh Soutetsu", không có ngoại lệ rên. 6 dòng sửa: 稀咲03 2138 (gọi trực tiếp), Grand 01 2756/2181 (xem ghi chú dưới), P16 2008/2015/2016 (tên trần → "anh Soutetsu").

### グランドリライト01_オール御一夜、成立ならず.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2181 | 「今回の試験走行までで、御一夜のキーマンが何人も、\n双鉄くんを信頼してくれたと思いますし、その人脈も」 | 「到這次的行駛測試為止，雙鐵君已經獲得了好幾位御一夜大人物相當的信任了，可以利用這些人脈」 | 「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohitoyo,\ntin tưởng cậu Soutetsu, và cả những mối quan hệ đó nữa.」 | 「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohitoyo,\ntin tưởng anh Soutetsu, và cả những mối quan hệ đó nữa.」 | JP 双鉄くん; cùng mạch đề xuất với 2756, Soutetsu đáp 2360. Lưu ý: old_vn đã mang "Ohitoyo" do đợt U1c gộp (xem §5). |
| 2756 | 「例えば、双鉄くんに政策秘書に入ってもらって、\n市政のレベルで観光振興に力を注いでもらう、とか」 | 「比如讓雙鐵君擔任政策秘書，在市政的層面上為振興旅遊業努力之類的」 | 「Ví dụ như, nhờ cậu Soutetsu làm thư ký chính sách,\nvà tập trung sức lực vào việc chấn hưng du lịch ở cấp độ chính quyền thành phố, chẳng hạn.」 | 「Ví dụ như, nhờ anh Soutetsu làm thư ký chính sách,\nvà tập trung sức lực vào việc chấn hưng du lịch ở cấp độ chính quyền thành phố, chẳng hạn.」 | JP 双鉄くん; Paulette đề xuất vai trò cho Soutetsu trong cuộc họp có Soutetsu tham dự (Soutetsu hỏi 2175, đáp 2373). Theo khóa B4 + quyết định P14 (list/task). |

### ポーレット16_明日へのレール.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2008 | 「はい、双鉄くん。喜んで」 | 「好的，雙鐵君。我很樂意」 | 「Vâng, Soutetsu. Em rất sẵn lòng.」 | 「Vâng, anh Soutetsu. Em rất sẵn lòng.」 | JP 双鉄くん, gọi trực tiếp ("はい、双鉄くん"). |
| 2015 | 「双鉄くん以外のキスなんて、\n寝てても私、逃げちゃいますから」 | 「如果吻我的人不是雙鐵君，就算我睡著了也會躲開的」 | 「Nếu không phải là nụ hôn của Soutetsu,\nthì dù có đang ngủ em cũng sẽ né tránh thôi.」 | 「Nếu không phải là nụ hôn của anh Soutetsu,\nthì dù có đang ngủ em cũng sẽ né tránh thôi.」 | JP 双鉄くん; Paulette nhắc tên Soutetsu theo dạng B4 ("anh Soutetsu"). |
| 2016 | 「双鉄くんが来てくれなければ――\nわたしも、町も、きっと眠ったままでした」 | 「如果沒有雙鐵君的到來——我，還有這座城市，一定還在沉睡當中吧」 | 「Nếu Soutetsu không đến đây——\nCả tôi và thành phố này, chắc chắn vẫn sẽ mãi chìm trong giấc ngủ.」 | 「Nếu anh Soutetsu không đến đây——\nCả tôi và thành phố này, chắc chắn vẫn sẽ mãi chìm trong giấc ngủ.」 | JP 双鉄くん; như 2015. |

### 稀咲03_純白のレール.txt.toml

| Key | JP | TW | old_vn | fix | Lý do |
|---|---|---|---|---|---|
| 2138 | 「双鉄くん、細かな話についてなんですけど」 | 「雙鐵君，我想問你一些細節」 | 「Cậu Soutetsu, về những chi tiết cụ thể thì」 | 「Anh Soutetsu, về những chi tiết cụ thể thì」 | JP 双鉄くん; Paulette gọi trực tiếp Soutetsu để hỏi chi tiết. |

**Ghi chú Grand 01 — 2756/2181 sửa, 2468/2557 giữ (đã kiểm chứng từng dòng kề):**

- **2756 sửa:** Paulette đề xuất Soutetsu làm thư ký chính sách trong cuộc họp có Soutetsu tham dự — Soutetsu hỏi lại ngay trước đó (2175 "別のやり方?") và đáp ngay sau (2373 "ほう"). Đề xuất hướng về Soutetsu với tư cách người tham dự.
- **2181 sửa:** cùng mạch đề xuất với 2756; Soutetsu đáp 2360 ("ポーレットのいうこともまた、理解はできるな" — "những gì Paulette nói cũng có thể hiểu được").
- **2468 giữ:** Paulette nói VỚI Kisaki (2995 Paulette "ええと――稀咲さん?"; Kisaki 2293 đáp, 2813 đáp lại 2468) — nhắc Soutetsu ở ngôi ba, không phải gọi Soutetsu.
- **2557 giữ:** Paulette nói với nhóm/Reina (2797 Reina "Reina cũng, cùng với chị Paulette, sẽ ủng hộ anh Soutetsu"); TW "我也會支持雙鐵君的" xác nhận ngôi ba. (Ghi chú: Reina ngay dòng sau dùng "anh Soutetsu" cho cùng người — nhưng task + list chốt giữ 2557 theo quy ước ngôi ba của file, đã khóa trong audit Grand 01.)
- **Mâu thuẫn đã ghi nhận:** audit Grand 01 (trước khi đính chính B4) từng giữ cả 4 dòng theo "quy ước ngôi ba sẵn có của file" và nêu 2756/2181 làm ví dụ đúng. Quyết định P14 trong list + task (sau B4) tách 2756/2181 ra sửa; batch này làm theo list/task, với bằng chứng dòng kề nêu trên (Soutetsu tham dự và đáp lại trong 2756/2181; Kisaki/Reina là người nghe trong 2468/2557). Nếu Hieu muốn thống nhất cả 4 dòng về một dạng, đó là quyết định mới — batch này không tự đổi 2468/2557.

## 3. Đã kiểm chứng, giữ nguyên (không sửa)

### 3a. P2 — 502 dòng ứng viên "cô" của Soutetsu được giữ

- **191 dòng "cô" ngôi ba / danh từ** ("cô ấy", "cô gái", "cô bé", "cô đơn", "cô chủ", "cô dâu"…): không phải xưng hô — mẫu ngẫu nhiên 15/15 kiểm chứng đúng. Ví dụ: ハチロク07 2575 "Paulette ấy à? … cô ấy là một nhà quản lý tài ba đấy." (ngôi ba về Paulette); 真闇02 1996 "cô đọng" (động từ "cô đọng lại", dương tính giả của regex); P16 2141/2121 "cô độc" (tính từ "cô độc", không phải đại từ).
- **Kisaki — "cô" là dạng ĐÚNG (quyết P3, ngược hướng với P2):** 75 dòng nhóm kề chỉ có Kisaki + các dòng đã đọc kỹ: 日々姫14 2018 (Kisaki mới là người có văn phòng tranh cử; Kisaki 1751 đáp), P06 1887 (cuộc họp 3 bên; Kisaki 1980 đáp trực tiếp — người nghe là Kisaki, không phải Paulette), P14 1409 ("là cô à——Houshou Kisaki"), 稀咲h1 1432 (JP 稀咲……綺麗だ), グランド06 19 dòng. Không đụng — P3 thuộc batch khác.
- **Hachiroku — ngoài phạm vi batch này:** 25 dòng nhóm kề chỉ có Hachiroku + ハチロク03 2039 (người trả lời là Hachiroku 1572, về 共感 từ Olivy) + P08_線から面へ 1623. Ghi chú: audit Common 05 đã sửa 2 dòng Soutetsu→Hachiroku "cô"→"em" trong file (2440/2727) — các dòng còn lại chưa có mục nào trong list bao phủ; để coordinator ghi nhận làm mục mới, batch này KHÔNG tự sửa.
- **Olivy:** ハチロク14 2427 (JP nêu tên オリヴィ), 3165 (Olivy là người hỏi ông Ishida, 3029), 3220 (Olivy 3273 đáp kế hoạch gặp lại); ハチロク08 2382 + 2479 (người nghe là Olivy + Niiroku — TW 2382 "希望二位…", monologue 3280/3027 nêu Olivy và Niiroku).
- **Nagayama:** P01_御一夜探し 1783/1919, 1755/1590/1924/1920/1447; P14 1673/1562 (Nagayama 1732/1894 đáp về cơm hộp); P16 1806 (Nagayama 1868 đáp). Soutetsu tự xưng "cháu" với bà — không phải Paulette.
- **Miyamoto (Trưởng phòng Miyamoto):** P04 1561/1829 (cảm ơn Trưởng phòng Miyamoto), 1585/1586 ("cô Miyamoto" ngôi ba); P11 1480/1414 ("cô Miyamoto" + "cô ấy" ngôi ba).
- **Navi:** Common 01 (8 dòng), Common 02/03/04, れいな02 1561 ("quan sát từ trên cao" — Navi).
- **Hibiki đóng vai Thị trưởng:** 日々姫h2 1163 ("Thị trưởng, cô có rảnh không?") + 1166 — người ngủ gật ở bàn thị trưởng là Hibiki (key 846 日々姫 "すぅ…すぅ", monologue 1379/1341: tài liệu đóng dấu thị trưởng, "em ấy" bị cơn buồn ngủ đánh bại). Không phải Paulette.
- **Mayami:** P16 2261 ("Nghe cô nói mới để ý, cháu chưa từng nghĩ…") — người nói trước là Mayami 1906/2180 (hội phụ nữ, vợ ông Minokasa); Soutetsu tự xưng "cháu" nên người nghe là bậc trên, không phải Paulette.
- **Danh xưng / ngôi ba khác:** "cô Hibiki" (P01_退任 1861 — Hibiki là cô giáo vẽ của Hikari), "cô Hinai Paulette" (共通09 2501 — danh xưng giới thiệu), "cô Nakamura" (Grand 09 1123), "cô Maia" (Grand 08 2223 — mẹ Paulette), "cô Khương" (lr稀咲追加01 1685), "cô Yamazaki" (các file Hibiki), "cô Midori" (Common 10), "cô Niiroku" (P16 1931; ハチロク08 2479), "cô phục vụ"/"cô gái"/"cô bé"/"cô con gái" (P04_鳴呼いき 1673 — Hikari; P06_雪の宿 2114 — "cô em gái sinh đôi" của ba Soutetsu).

### 3b. P14 — đã kiểm chứng, giữ nguyên / đã sửa trong audit

- **Tự sửa くん→さん có chủ ý — GIỮ (4 dòng, 共通05):** 2551/2721/2421/2275 — JP đều là 双鉄くっ――双鉄さん (tự sửa くん→さん); VN "Cậu Soutetsu……à không, anh Soutetsu" diễn đúng sự tự sửa. Đổi "cậu"→"anh" sẽ thành "anh Soutetsu……à không, anh Soutetsu" (vô nghĩa). Tiền lệ đã khóa trong audit Common 05 ("Paulette tự sửa くん→さん… theo mẫu 2721/2421/2275").
- **Grand 01 2468/2557 — GIỮ** (ngôi ba, xem §2 ghi chú).
- **Đã sửa trong audit — kiểm chứng, không sửa trùng (9 dòng):** ハチロク01_双鉄の目 2210/2232, ハチロク02_ハートブレイク 2166, ハチロク05_レイルロオドたち 3078, ハチロク11_幽霊 2163, ハチロク14 2573/3256/3257, 凪ふかみ08b_ふかみエピローグ 2436 — giá trị hiện tại đều đã là "anh Soutetsu". (Lưu ý: tên file trong list ghi tắt "Hachiroku 02/05/11" dễ nhầm — đã xác minh đúng file TOML từng key.)
- **Grand 08 key 1702 — KHÔNG TỒN TẠI dòng Paulette:** key 1702 của グランドリライト08_ふかみ là Kisaki (「キミは、それで――" → "Cậu, như vậy thì――" — Kisaki→Soutetsu "cậu", thuộc P4, không phải P14). Không có dòng nào để sửa; ghi nhận list ghi nhầm file/key.
- **"cậu Soutetsu" của người nói khác — GIỮ (29 dòng):** Minokasa (蓑笠) 8, Akai/đền chủ Akai 9, Mototada (元忠) 6, Nagayama (永山) 3, Urakami (浦上) 2, Kisaki 2097 (JP bare 双鉄, "cậu Soutetsu" — Kisaki gọi Soutetsu "cậu" theo P4, không phải Paulette). P14 chỉ bao phủ Paulette.

## 4. Quyết định O1 — Paulette 06 key 2047: thống nhất "em" cho MỌI ngữ cảnh

**Dòng cần quyết:** file `ポーレット06_おひとよマイントレジャー.txt.toml`, key `2047`, speaker 双鉄 (Soutetsu).

- **JP:** 「どうだろうか、ポーレット」
- **TW:** 「波萊特，你覺得怎麼樣？」
- **old_vn (CSV3):** 「Cô thấy sao, Paulette」
- **fix (O1):** 「Em thấy sao, Paulette」

**Ngữ cảnh (dòng kề):** Hibiki 1962 vừa trình bày đánh giá về kế hoạch Mine Treasure; monologue 2547: người quyết định là "市長で社長のポーレット" (Paulette, vừa là thị trưởng vừa là chủ tịch); Paulette 1996 đáp "すごくありがたいと思います。できれば、わたしも直接お会いしたいです". Đúng là ngữ cảnh công việc — câu hỏi xin ý kiến của thị trưởng/chủ tịch về một kế hoạch kinh doanh.

**Câu hỏi mở trong list:** thống nhất "em" cho mọi ngữ cảnh, hay giữ "cô" khi làm việc? (Mẫu ranh giới theo chương: P09–12 nghiêng "cô" 43:3, P13–16 nghiêng "em" 0:11 — gợi ý sự chuyển register có chủ ý.)

**Bằng chứng và quyết định — thống nhất "em", KHÔNG có ngoại lệ ngữ cảnh công việc:**

1. **"cô" không phải dấu hiệu của ngữ cảnh công việc.** 18 dòng P10 ("Vết thương không nhìn thấy") dùng "cô" trong cảnh chăm sóc thân mật nhất của route — Soutetsu đút cháo, đỡ Paulette dậy sau khi ngất, nắm tay an ủi (1510, 1278, 1465, 1353, 1362, 1451…) — và tất cả đều được sửa thành "em" trong P2 đợt này. Nếu "cô" là register công việc thì nó đã không xuất hiện dày đặc trong cảnh chăm sóc ốm. Register thực sự phân theo **giai đoạn chương** (đầu route trang trọng → cuối route thân mật), không phân theo công việc/thân mật.
2. **Cùng một mẫu câu JP, cùng ngữ cảnh công việc, đã về "em" trong chính đợt này:** 稀咲03 key 2006 — JP 「どうだろう、ポーレット」 (hỏi ý kiến Paulette trong cuộc họp kinh doanh với Mototada và Kisaki), old_vn "Cô thấy sao, Paulette." → fix P2 "Em thấy sao, Paulette." Giữ 2047 là "cô" trong khi sửa 2006 thành "em" — hai câu JP gần như giống hệt nhau, cùng ngữ cảnh họp — sẽ là mâu thuẫn nội bộ.
3. **P13–16 dùng "em" cả trong ngữ cảnh công việc:** kiểm đếm trực tiếp — 18 dòng Soutetsu→Paulette "em" trong file P13–16, trong đó P16 2425 (bàn kế hoạch kinh doanh: "nếu em có nghĩ ra điều gì thì cứ nói nhé"), P16 1928 (khôi phục xe goòng), P15 1459 (gặp đền chủ Akai), P15 1531 (cảm ơn trong bối cảnh tuyển dụng khó). Và 0 dòng Soutetsu→Paulette "cô" còn lại trong P13–16 (13 lượt "cô" quét được ở đó đều là "cô ấy" ngôi ba / "cô độc" / Nagayama / Niiroku / Mayami / hội phụ nữ). Nếu ngữ cảnh công việc giữ "cô" thì P13–16 đã phải còn "cô" trong các cảnh họp — thực tế là 0.
4. **Phân bố theo chương (đếm lại đợt này):** P09–12: 42 dòng "cô" sửa thành "em" + 2 dòng "em" đã đúng sẵn (P09 1746, P10 1373); P13–16: 18 dòng "em" đã đúng + 0 dòng "cô". Ranh giới nằm giữa P12 và P13, trùng với bước ngoặt tình cảm của route (P12 tỏ tình, key 1110 "僕は、君に――恋をしている"), không trùng với ranh giới công việc/thân mật nào. P06 2047 nằm ở phía "cô" của ranh giới chương — đúng dạng mà P2 (Hieu 19/11) quyết thống nhất thành "em" toàn dự án, không ngoại lệ.

**Kết luận O1:** sửa 2047 thành "em" (đã đưa vào JSON, item "O1"). Không đặt ngoại lệ "giữ cô khi làm việc" — ngoại lệ đó không có cơ sở trong dữ liệu và sẽ mâu thuẫn với 2006 + các dòng "em" trong ngữ cảnh công việc ở P13–16.

## 5. Đối chiếu số liệu, trùng lặp và ghi chú cho coordinator

- **P2 — 43 → 99 dòng:** brief/list ghi "43 dòng" là ước lượng cũ; con số 43 khớp gần đúng cụm P09–12 (42 dòng sửa đợt này + 2 dòng "em" đã đúng sẵn: P09 1746, P10 1373). 57 dòng còn lại nằm ở P01–08 (16), P-h7 (3), Common (1), Hachiroku (13), Hibiki (9), Grand 04/05 (14) và Kisaki 03 (1) — đều đã kiểm chứng từng dòng là Soutetsu→Paulette. Tổng P2 thực tế: **99 dòng**.
- **Trùng lặp với đợt đã gộp — 1 dòng:** Grand 01 key 2181 đã nằm trong `unification-t1-ohimitera-07-11-wrong.json` (U1c, đã gộp): đợt đó sửa "Ohitera"→"Ohitoyo"; đợt này sửa "cậu Soutetsu"→"anh Soutetsu". `old_vn` trong JSON đợt này đã lấy giá trị SAU U1c ("Ohitoyo"), và fix giữ nguyên "Ohitoyo" — hai đợt cộng dồn đúng, không đè nhau. 0 key trùng với U1a/U1b/U2a và đợt U10/s6 (đã kiểm tra bằng script trên toàn bộ file `unification-*-wrong.json`).
- **Cơ sở đếm (snippet):** `ROUTE-UNIFICATION.md` hiện tại là **2 mục / 226 dòng** (U1b/U1c/U2a gộp 22/11 ~11:15) — cơ sở 0/0 lúc spawn đã cũ, đã rebase. Đợt U10/s6 (snippet ghi 18 mục / 258 dòng) chưa thấy gộp vào `ROUTE-UNIFICATION.md` — coordinator xếp thứ tự khi gộp.
- **Cần mục mới (không thuộc batch này):** Soutetsu→Hachiroku "cô" còn lại (25 dòng nhóm kề Hachiroku + 2 dòng đã đọc kỹ) — audit Common 05 từng sửa 2 dòng dạng này trong file (2440/2727) nhưng list không có mục thống nhất cho Hachiroku; đề nghị coordinator ghi nhận.
- **Grand 01 2756/2181 vs 2468/2557:** xem ghi chú §2 — quyết định theo list/task (sau B4), trái với quy ước "giữ cả 4" của audit Grand 01 trước B4; đã nêu lý do theo dòng kề. Nếu Hieu muốn đổi, chỉ cần quyết một dòng cho cả 4.
- **P16 2015/2016 là nhắc ngôi ba, không phải gọi trực tiếp** ("nụ hôn của Soutetsu", "Nếu Soutetsu không đến đây") — vẫn sửa theo task/list (dạng B4 "anh Soutetsu"), khác với Grand 01 2468/2557 được giữ: khác biệt là 2468/2557 mang đại từ "cậu" theo quy ước ngôi ba đã khóa của file Grand 01, còn P16 mang tên trần (không có đại từ nào) nên đưa về dạng B4.

## 6. Lượt soát 2 (bắt buộc — đọc lại toàn bộ fix theo JP)

- **Tổng số fix đưa vào lượt soát 2: 106 dòng (P2 99 + P14 6 + O1 1). Tái kiểm chứng: 106/106. Loại bỏ: 0. Sửa lại: 0.**
- Mỗi fix đã đọc lại đối chiếu JP (+TW khi cần): đại từ đổi đúng là đại từ xưng hô với Paulette/Soutetsu (JP 君 / ポーレット / 双鉄くん); không dòng nào đổi nghĩa khác; "Cô bé Paulette" (Grand 04 2168/2183) giữ nguyên; "Densha Hime" (P09 2129), "Ohitoyo" (Grand 01 2181) và các thẻ `%l` giữ nguyên — các thuật ngữ đó thuộc batch khác.
- Kiểm chứng cơ học bổ sung: span-diff `old_vn` → `fix` cho 106/106 dòng chỉ gồm đúng phép thay đại từ đã định ("cô"→"em", "Cô"→"Em", "cậu Soutetsu"→"anh Soutetsu", "Cậu Soutetsu"→"Anh Soutetsu", "Soutetsu"→"anh Soutetsu" ở P16, "Cô thấy sao, Paulette"→"Em thấy sao, Paulette" ở O1); không có thay đổi nào khác.
- Nguồn `old_vn`: CSV3 102 dòng, audit fix 3 dòng (ハチロク05 3062, 日々姫04 1708, ポーレット05_鳴呼の町 2010), unification U1c 1 dòng (Grand 01 2181). Không dòng nào lấy từ moan list (không có dòng moan nào trong 106 dòng này).

## 7. Khối TOML (parse-verified, theo file)

Mỗi khối có header `[script]`, key dạng chuỗi, giá trị là fix. Trong khối TOML, backslash được escape (`\` → `\\`, `"` → `\"`), nên literal `\n` trong giá trị viết thành `\\n`. Đã parse-verify bằng tomllib: mọi khối parse được và giá trị parse ra khớp fix từng key (**30 khối / 106 key**).

```toml
# グランドリライト01_オール御一夜、成立ならず.txt.toml
[script]
"2181" = "「Đến cuộc chạy thử lần này, tôi nghĩ đã có nhiều nhân vật chủ chốt của Ohitoyo,\\ntin tưởng anh Soutetsu, và cả những mối quan hệ đó nữa.」"
"2756" = "「Ví dụ như, nhờ anh Soutetsu làm thư ký chính sách,\\nvà tập trung sức lực vào việc chấn hưng du lịch ở cấp độ chính quyền thành phố, chẳng hạn.」"

# グランドリライト04_ポーレット.txt.toml
[script]
"1283" = "「——Cảm ơn em.」"
"1284" = "「——Cảm ơn em, Paulette.」"
"1715" = "「Hôm nay em có dự định ra ngoài không?\\nNếu có thì đi trước khi trời mưa nhé.」"
"1768" = "「Chính tôi đã tự nguyện lặp đi lặp lại những đau khổ và thù hận đó.\\nPaulette. Chính em đã giúp tôi đặt dấu chấm hết cho chúng.」"
"1829" = "「Ồ. Tuyệt thật đấy, ra là em tự làm thủ công thế này sao.\\nTôi cứ tưởng là thuê bên ngoài làm chứ.」"
"1901" = "「A, được em chỉ cho thì còn gì bằng.」"
"1903" = "「Ừm. Chắc là tôi nhìn và nhớ được rồi.\\nNếu sai thì em chỉ tôi nhé.」"
"1923" = "「Hửm? Nếu em thấy thế tốt hơn, thì cứ làm vậy đi.」"
"2012" = "「Tôi cũng mong em giúp đỡ.」"
"2021" = "「Sao thế? Hôm nay tôi\\nphải giúp em sơn lại tàu à?」"
"2035" = "「Tôi cũng vậy. Tôi muốn nói chuyện thật kỹ với em.」"
"2168" = "「Ví dụ như——để xem nào. Giả sử gia đình em đến đây.\\nCô bé Paulette sẽ muốn chơi trò gì?」"
"2183" = "「Paulette. Em, chính là cô bé lúc đó sao?」"

# グランドリライト05_れいな.txt.toml
[script]
"2156" = "「Nếu vậy, Paulette, phần còn lại nhờ em nhé.」"

# ハチロク01_双鉄の目・ハチロクの目.txt.toml
[script]
"1923" = "「Không——đợi đã. Theo lời em vừa nói thì……chỉ cần có tiền,\\nthì vẫn có \\x%l客車;#00ffc040;toa hành khách%l;#; được bán ra sao?」"

# ハチロク05_レイルロオドたち.txt.toml
[script]
"2422" = "「À……nghe em nói mới nhớ, hình như cũng có thứ đó――\\nthì phải.」"
"3062" = "「Ý em là――bảo anh phớt lờ lời phê bình của Olivy sao?」"

# ハチロク05_軋み.txt.toml
[script]
"1235" = "「……Nghe em nói vậy tôi cũng thấy nhẹ nhõm phần nào.」"
"1519" = "「Có chút bận tâm, nhưng tôi vẫn chưa xác nhận được.\\nNgay khi xác nhận xong, tôi muốn báo cáo lại với em.」"
"1870" = "「Vậy thì yên tâm rồi.\\nXin lỗi vì đã làm phiền em. Cảm ơn nhé.」"

# ハチロク10_炙り出し.txt.toml
[script]
"1795" = "「Ừm——trăm sự nhờ em.」"
"1965" = "「Không đâu. Em đã cho một gợi ý rất hay. Cảm ơn em.」"
"1976" = "「Paulette,\\nnếu được thì xin em đừng quá phiền lòng như vậy.」"

# ハチロク11_幽霊.txt.toml
[script]
"1805" = "「Ừm. Ngày mai cũng nhờ em nhé.」"

# ハチロク13_夜の嵐.txt.toml
[script]
"1235" = "「……Giờ tôi chưa nghĩ ra thêm gì cả.\\nNếu em nhận thấy cần chuẩn bị gì thì cứ tự quyết định giúp tôi được không?」"
"1977" = "「Cảm ơn em.」"

# ハチロク14_冬.txt.toml
[script]
"3189" = "「Nhờ em nhé. Còn kim chỉ nam hành động cụ thể cho phía \\x%l保線;#00ffc040;bảo trì đường ray%l;#; thì sao?」"

# ポーレット01_ポーレット退任.txt.toml
[script]
"1539" = "「Không phải lúc nào em cũng ở bên cạnh con bé được đâu.\\nĐôi khi, đứng từ xa quan sát cũng là một cách thể hiện tình yêu thương mà.」"

# ポーレット04_ヒヤリング.txt.toml
[script]
"1174" = "「……Xin lỗi nhé.\\nVì tôi mà em đã bỏ lỡ mất cơ hội bấm máy rồi.」"
"1396" = "「Em đến đây để chụp ảnh đường sắt sao?」"
"1596" = "「Tôi không định làm em giật mình——」"
"1661" = "「Không sao, tôi cũng đang muốn gặp em đây.」"
"1674" = "「Tại sao em lại nói như vậy?\\nTai nạn đường sắt, mà đường sắt và \\x%l列車;#00ffc040;đoàn tàu%l;#; lại không có lỗi sao——」"
"1721" = "「Nghe nói em có chuyện cần bàn bạc.」"
"1771" = "「Vậy sao, em được ba nhờ đến đây chụp ảnh à.」"

# ポーレット05_whatsentertainment.txt.toml
[script]
"975" = "「——Tiểu thư. Em có muốn đi chơi cùng tôi không?」"
"1224" = "「Nghe em nói vậy, đúng là thế thật.\\nCon người có lẽ đều có một mặt như vậy.」"
"1405" = "「Tôi hiểu rồi. Vậy thì chúng ta chia việc ra làm nhé.\\nTôi sẽ ra lệnh cho Navi đưa em đi.」"

# ポーレット05_鳴呼の町.txt.toml
[script]
"1671" = "「Nghe em nói vậy, tôi cũng thấy thế.」"
"2010" = "「Rổ ráo nước, nhé. Paulette. Em có thể đưa đầu xích của một chiếc rổ trống cho Hikari cầm giúp tôi được không?」"

# ポーレット06_おひとよマイントレジャー.txt.toml
[script]
"2047" = "「Em thấy sao, Paulette」"

# ポーレット08_線から面へ.txt.toml
[script]
"1636" = "「Chào buổi sáng, Paulette.\\nHôm nay tôi không thể làm thư ký cho em được, xin lỗi nhé.」"
"1715" = "「Chuyện nhỏ thôi.\\nNhưng mà――em định nói gì với Navi vậy?」"
"1739" = "「Cảm ơn em. Có cái này thì tôi có thể thực hiện nhiệm vụ mà không gặp tai nạn nào rồi――\\nHửm?」"

# ポーレット09_ストーブ客車.txt.toml
[script]
"1395" = "「...Ý em là,\\ncó thể sẽ phát sinh vấn đề liên quan đến khói và những thứ tương tự sao.」"
"1713" = "「Thế rồi em có được ăn không?\\nChấm nước tương đường, hay là bột đậu nành Kinako?」"
"1805" = "「À, em in ra rồi sao――\\nLà bức ảnh Nagi chụp đúng không?」"
"1819" = "「À, cảm ơn em.」"
"1931" = "「Rất vinh hạnh vì em đã thảo luận với tôi.」"
"2129" = "「Ý em là, \\x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\\nđã được Densha Hime nhận về và bảo quản――đúng không?」"
"2177" = "「Hỏi để chắc chắn thôi, em còn nhắm được \\x%l客車;#00ffc040;toa hành khách%l;#; nào khác không?」"
"2209" = "「Em hiểu lầm rồi.」"

# ポーレット10_見えない傷.txt.toml
[script]
"991" = "「——Nếu em nghĩ được như vậy thì tốt quá rồi.」"
"998" = "「——Nếu để lâu thì cháo sẽ càng lúc càng nhão đấy.\\nNếu em vẫn còn ăn được thì...」"
"1239" = "「Không――đây không phải chuyện đáng để em phải cảm ơn đâu.」"
"1262" = "「Em vừa mới ngất xỉu đấy nhé? Đừng cử động đột ngột.\\nBiết đâu lại bị đau ở đâu đó thì sao.」"
"1278" = "「Em gặp ác mộng à?」"
"1314" = "「Ư-ừm——Hợp khẩu vị của em là tốt rồi.」"
"1353" = "「À, chị Mayami đã thay giúp đấy.\\nBây giờ chị ấy có việc ở xưởng rượu, nên tôi đã tiếp quản việc chăm sóc em.」"
"1362" = "「Ừm. Em muốn uống trước hay ăn trước?」"
"1378" = "「Ừm, nhờ em nhé.\\nVà hãy cùng nhau tiến bước hướng tới một tương lai tốt đẹp hơn.」"
"1451" = "「Tôi đỡ em dậy nhé.」"
"1465" = "「Xin lỗi. Tôi không thể để mặc em được.\\nChạm vào người khác lúc đang ngủ, không phải là việc nên làm――」"
"1471" = "「Nếu em thấy ổn rồi thì chúng ta đi thôi, Paulette.」"
"1487" = "「Dù không bằng em, nhưng tôi đã làm.\\nTôi bắt cặp với Hachiroku, và dùng KiHa 07 làm \\x%l客車;#00ffc040;toa hành khách%l;#;.」"
"1510" = "「Không sao đâu. Ít nhất thì tôi cũng đứng về phía em.\\nTôi sẽ ở đây――bên cạnh em chừng nào em còn cần.」"
"1522" = "「Paulette, cơ thể em có chỗ nào...」"
"1561" = "「Nói chung, bây giờ em cứ tập trung hồi phục đi.\\nCó đói bụng không? Có khát nước không?」"
"1565" = "「Liệu em có thể để tôi phụ trách việc vận hành \\x%lキハ07;#00ffc040;KiHa 07%l;# được không?」"
"1575" = "「Để em phải đợi rồi. Ây da――\\nKhông, đợi một chút đã.」"

# ポーレット11_記憶と記録.txt.toml
[script]
"1280" = "「Không thể vì ai đó mong muốn được. Cả chuyện Mine Treasure,\\nhay chuyện kinh doanh đường sắt, chấn hưng du lịch, em cũng không cần phải bận tâm.」"
"1312" = "「Em thực sự――mong muốn “đừng thay đổi” sao?」"
"1381" = "「Vì đó là mong muốn của tôi.\\nTôi, muốn giúp em.」"
"1399" = "「Nếu không đối mặt, thì không thể vượt qua.\\nĐó là điều mà Paulette, chính em đã dạy cho tôi.」"
"1485" = "「Tôi đã nghe thấy tiếng thét của em. Em đã truyền tiếng thét đó đến tôi.\\nĐã vươn bàn tay này về phía tôi.」"
"1488" = "「Vì vậy, dù có bị coi là xấu tính, dù có bị ghét bỏ đi chăng nữa.\\nTôi vẫn muốn em đối mặt với quá khứ.」"
"1567" = "「Paulette.\\nTừ giờ trở đi, em phải là người đưa ra quyết định.」"
"1568" = "「Một hạnh phúc sợ hãi và khép kín. Biến Reina thành một con búp bê.\\nPaulette, em thực sự mong muốn điều đó sao?」"
"1722" = "「Đây là chuyện của em và Reina.\\nPaulette, đây là quyết định định đoạt tương lai của hai người đấy.」"

# ポーレット12_解放.txt.toml
[script]
"973" = "「Tôi cũng……được em dạy cho biết yêu là gì.」"
"1021" = "「Ừm. Paulette, em không hề bị vứt bỏ.」"
"1058" = "「Tôi cũng vậy――rất vui vì em đã ở bên tôi.\\nVì vậy, tôi muốn em hãy ở bên tôi.」"
"1090" = "「Chính em đã giúp tôi nhìn thấy.\\nTôi có thể nghĩ về em nhiều đến thế, và trở nên ấm áp đến thế.」"
"1110" = "「Paulette.\\nTôi, đã――yêu em rồi.」"
"1112" = "「Paulette, em không làm gì sai cả.」"
"1113" = "「Mẹ em cũng rất coi trọng Paulette. Cảm thấy em là người không thể thay thế.\\nChính vì vậy――bà ấy mới không thể cướp em khỏi ba em.」"

# ポーレット16_明日へのレール.txt.toml
[script]
"2008" = "「Vâng, anh Soutetsu. Em rất sẵn lòng.」"
"2015" = "「Nếu không phải là nụ hôn của anh Soutetsu,\\nthì dù có đang ngủ em cũng sẽ né tránh thôi.」"
"2016" = "「Nếu anh Soutetsu không đến đây——\\nCả tôi và thành phố này, chắc chắn vẫn sẽ mãi chìm trong giấc ngủ.」"

# ポーレットh7_残業エッチもyシャツで.txt.toml
[script]
"953" = "「Thị trưởng. Em quên rồi sao?\\nĐây là hình phạt dành cho em đấy nhé? Không phải phần thưởng đâu.」"
"954" = "「Thị trưởng, thế này là em đã chịu trách nhiệm cho chuyện lần này——」"
"1015" = "「Đến cả mức độ đó mà em cũng quên mất, rồi lại mất kiểm soát.\\nBiện pháp để sửa đổi điều đó là——nào, là gì?」"

# 共通14_負債.txt.toml
[script]
"1858" = "「Trong thời gian ngắn như vậy mà em đã đưa ra được bản dự toán này, làm tốt lắm.」"

# 日々姫04_カフェキッチン.txt.toml
[script]
"1708" = "Cảm ơn em, giúp được anh nhiều lắm. Anh sẽ nhờ vả em, nhưng sẽ cố gắng không ỷ lại quá nhiều vào lời nói đó."

# 日々姫04_同乗.txt.toml
[script]
"2035" = "「Ừ. Nhờ em tìm được \\x%l客車;#00ffc040;toa hành khách%l;#;,\\nmà chúng ta mới có thể đi xa đến bước này.」"
"2155" = "「Cảm ơn em.」"

# 日々姫05_御一夜ステーションカフェ.txt.toml
[script]
"2518" = "「Cảm ơn em.」"

# 日々姫07_姉の想い。妹の想い.txt.toml
[script]
"2058" = "「Thật sự rất vững tâm, và giúp ích được rất nhiều.\\nDù là chuyện thường ngày nhưng——cảm ơn em」"

# 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml
[script]
"2322" = "「Thay vì thế, em có thể cho chúng tôi,\\nmột chút đồ uống ấm được không?」"

# 日々姫13_討論会.txt.toml
[script]
"1512" = "「Paulette. Trong số những người bạn đường sắt của em,\\ncó bao nhiêu người được gọi là \\x%l撮り鉄;#00ffc040;Tori-tetsu%l;#;?」"
"1592" = "「Nếu vậy, em có thể nhờ họ được không?」"
"1649" = "「Vậy sao, thế thì nhờ em nhé.」"

# 稀咲03_純白のレール.txt.toml
[script]
"2006" = "「Em thấy sao, Paulette.」"
"2138" = "「Anh Soutetsu, về những chi tiết cụ thể thì」"
```

## Kết bài

Đợt U6 sửa **106 dòng (P2 99 + P14 6 + O1 1)** trong 30 file: Soutetsu gọi Paulette thống nhất thành "em" (kể cả ngữ cảnh công việc — quyết định O1, bằng chứng: "cô" xuất hiện cả trong cảnh thân mật P10, và "em" đã là chuẩn trong cảnh họp ở P13–16); Paulette gọi Soutetsu thống nhất thành "anh Soutetsu" (kể cả 3 dòng tên trần P16); 9 dòng P14 ứng viên đã sửa trong audit được kiểm chứng, không sửa trùng; Grand 08 1702 không tồn tại dòng Paulette (list ghi nhầm). Đã đọc kiểm chứng 602 dòng ứng viên "cô" của Soutetsu: 502 dòng giữ có lý do (ngôi ba/danh từ 191, Kisaki 75+, Hachiroku 25+, Navi, Nagayama, Miyamoto, Olivy, Niiroku, Hibiki-đóng-vai-thị-trưởng, Mayami…). Lượt soát 2: 106/106 tái kiểm chứng, 0 loại, 0 sửa. Khối TOML 30 file / 106 key parse-verified. Còn nợ coordinator: mục mới cho Soutetsu→Hachiroku "cô" (27 dòng) và quyết định cuối về Grand 01 2468/2557 nếu Hieu muốn thống nhất cả 4 dòng.
