# REVIEW — Unification batch U9: §2 P15 + P7 + §7 O61 (Munakata "tao" · Kisaki "anh trai của Hibiki")

- Đợt: U9 (§2 P15 + P7, §7 O61).
- Mục: P15 (DECIDED 21/11 ~17:30, Muse theo uỷ quyền), P7 (DECIDED 22/11 ~04:03, Hieu), O61 (OPEN — quyết trong đợt này theo uỷ quyền của Hieu, KHÔNG park).
- File: `unification/unification-s2-munakata-kisaki-REVIEW.md` + `unification/unification-s2-munakata-kisaki-wrong.json` (24 mục, kind="pronoun", item="P15"/"O61"; P7: 0 dòng).
- Kết quả: **P15: 18 dòng · O61: 6 dòng · P7: 0 dòng (đã đúng sẵn) — tổng 24 dòng sửa, 5 file.**

## §1. Phạm vi (scope)

- **P15 — Munakata (宗方甚六) 俺/オレ → "tao" (17 dòng theo list).** Phạm vi áp: mọi dòng Munakata nói, JP chứa 俺/オレ, giá trị hiện tại dùng đại từ khác "tao" cho ngôi tự xưng của ông. お前 KHÔNG đụng (vẫn theo người nghe): các dạng "nhóc" (ハチロク12 2248), "cô" (ハチロク15a 1770/1772/2031), "cậu" (ハチロク04 1814 "giám đốc công ty cậu", ハチロク16 1637 "Cậu nói vậy") giữ nguyên.
- **P7 — Kisaki 日々姫さんのお兄さん → "anh trai của Hibiki" (KHÔNG BAO GIỜ "chị Hibiki").** Phạm vi áp: mọi dòng JP chứa 日々姫さんのお兄さん. Kết quả: **0 dòng sửa** — cả 2 dòng duy nhất toàn dự án đã đúng sẵn (xem §4).
- **O61 — ハチロク10_炙り出し Munakata "tôi" 6 dòng không có 俺 rõ ràng (1297/1306/1637/1903/2050/2070).** Sửa lại tên file trong list: các key này thuộc **ハチロク16_春** (xem §5 — list ghi nhầm file; ROUTE-AUDIT.md mục ハチロク16_春 mới là nguồn đúng). Quyết định trong đợt này: **"tao" cho cả 6 dòng** (xem §5, bằng chứng đầy đủ).

## §2. Phương pháp (method)

1. Đọc `UNIFICATION-BRIEF.md` + `UNIFICATION-LIST.md` §2 P15/P7, §7 O61 + `dual-csv-sets.md`.
2. Xây map giá trị hiện tại theo thứ tự đã hiệu chỉnh (22/11 ~11:35, U2c + coordinator CONFIRMED): **unification-đã-gộp (7 file: U1a/U1b/U1c/U2a/U10/U6/U2c, 584 cặp) > moan (1.516) > audit (9.240) > CSV3 good-set (87.833 dòng)**. Map xây bằng `_u9_map.py` (dựa trên `_u3_map.py`, chỉ khác danh sách unification-đã-gộp). Các file unification chưa gộp (t1-ohito-t2-06-11, t1-set2, t1-set3, t1-open-t56-t66, s2-kisaki-address-*) KHÔNG đưa vào map.
3. Liệt kê ứng viên bằng script (chỉ đếm/liệt kê): P15 = Character `宗方` + JP chứa 俺/オレ (17 dòng) + kiểm tra riêng おれ hiragana (thêm 1 dòng: ハチロク16 1884); P7 = JP chứa 日々姫さんのお兄さん (toàn CSV3, kể cả stale set: 2 dòng); O61 = 6 key trong ハチロク16_春.
4. Đọc từng dòng JP (+TW) + dòng kề để xác nhận người nói / người nghe / ngữ cảnh; mỗi fix chỉ đổi đại từ tự xưng "tôi"/"Tôi" → "tao"/"Tao", không đụng bất cứ token nào khác (kiểm chứng cơ học: chuẩn hoá tôi→tao xong old_vn và fix giống hệt nhau, 24/24).
5. Đối chiếu chéo TOML-2 (decode utf-8-sig, giải mã tên file #U-escaped): 24/24 dòng khớp nội dung CSV3 sau chuẩn hoá `\n` (4 dòng ハチロク12 1552/1708/2143/2212 chỉ khác ở artefact flatten `\n`→khoảng trắng đã biết của TOML-2, nội dung còn lại giống hệt).
6. Đối chiếu trùng lặp với mọi file `unification-*-wrong.json` trên đĩa: chỉ trùng 2 key đã gộp U2a (ハチロク16 1884/2070 — old_vn lấy đúng fix U2a, fix đợt này chỉ đổi đại từ trên nền đó, giữ nguyên "Đường sắt Ohitoyo"); 0 trùng với các batch chưa gộp.

## §3. P15 — Munakata 俺/オレ → "tao" (18 dòng)

Số dòng thực tế là **18, không phải 17 như list ghi**: list đếm 17 dòng 俺/オレ (kanji/katakana) nhưng bỏ sót 1 dòng おれ hiragana — ハチロク16_春 1884 「おれはマスターではない」. おれ = 俺 viết hiragana, cùng một đại từ, cùng người nói (宗方), nên phải sửa như các dòng 俺 khác. 4 dòng "ハチロク10 ×4 (1301/1884/1910/2025)" mà list ghi thực chất thuộc ハチロク16_春 (1301/1910/2025 là 俺, 1884 là おれ) — list ghi nhầm tên file (nguồn ROUTE-AUDIT.md mục ハチロク16_春).

Ghi chú từng nhóm:

- **ハチロク04 (3 dòng):** 1814 俺にも理解できた → "tao cũng hiểu"; 2065 アレもオレも → "cả nó và tao"; 2084 オレ×2 → "tao"×2 ("thì tao cũng bó tay" + "quyền hạn của tao").
- **ハチロク12 (6 dòng):** 1520 俺の頭 → "đầu óc tao"; 1552 少なくとも俺は → "ít nhất là tao"; 1708 俺――自分は宗方甚六 → "tao"×2 (cả 俺 lẫn 自分は đều là tự xưng của Munakata trong câu tự giới thiệu); 2143 俺――/私には → "với tao"×2 (hai lần tự nhắc trong một câu); 2212 俺は → "tao"×2 (chủ ngữ 俺 kéo dài sang câu thứ hai); 2248 俺は → "tao" (giữ "nhóc" cho お前, không đụng).
- **ハチロク15a (3 dòng):** 1770 俺の頼み → "Lời nhờ vả của tao"; 1772 俺がいる → "Thấy tao ở đây"; 2031 今の俺は → "Dù tao bây giờ" (giữ "cô" cho お前).
- **ハチロク15b (2 dòng):** 1683 俺も驚いた → "Tao cũng bất ngờ lắm"; 1846 俺も多少は → "tao cũng hơi nghĩ".
- **ハチロク16 (4 dòng):** 1301 俺は知らん → "Tao không biết"; 1884 おれはマスターではない → "Tao không phải là Master" (old_vn = fix U2a, đã có "Đường sắt Ohitoyo", giữ nguyên); 1910 俺はマスターではない → "Đã bảo tao không phải là Master mà"; 2025 俺は、こだまのマスターじゃない → "Tao không phải là Master của Kodama".

### P15 — 18 dòng (old_vn = giá trị hiện tại: csv3, trừ 1884 là fix U2a)

| File | Key | JP | TW | old_vn (giá trị hiện tại) | fix |
|---|---|---|---|---|---|
| ハチロク04_小畑越え.txt.toml | 1814 | 「いや、御社社長が気にしている点は、俺にも理解できた。\n命令に素直に従っても、アレがみかん鉄道に対して――」 | 「不，我也明白貴公司社長的擔憂，即便奧莉薇會老實服從命令，它對於橙鐵路——」 | 「Không, tôi cũng hiểu được điểm mà giám đốc công ty cậu đang lo ngại.\nCho dù có ngoan ngoãn tuân lệnh, nếu nó vẫn giữ tình cảm với Đường sắt Mikan――」 | 「Không, tao cũng hiểu được điểm mà giám đốc công ty cậu đang lo ngại.\nCho dù có ngoan ngoãn tuân lệnh, nếu nó vẫn giữ tình cảm với Đường sắt Mikan――」 |
| ハチロク04_小畑越え.txt.toml | 2065 | 「譲渡のおかげで、アレもオレも本線に復帰できる。\nいいことばかりだ――使いこなしてもらえるなら、な」 | 「多虧這次轉屬，不論它還是我都能回歸幹線工作，對雙方都是件好事。雖然這還需要貴公司能夠做到物盡其用」 | 「Nhờ có việc chuyển nhượng, cả nó và tôi đều có thể quay lại tuyến chính.\nToàn là chuyện tốt――nếu như các cậu có thể sử dụng nó một cách thành thạo.」 | 「Nhờ có việc chuyển nhượng, cả nó và tao đều có thể quay lại tuyến chính.\nToàn là chuyện tốt――nếu như các cậu có thể sử dụng nó một cách thành thạo.」 |
| ハチロク04_小畑越え.txt.toml | 2084 | 「故障ならオレの手には負えんし、\n拗ねているだけなら、それはもうオレの管轄外だ」 | 「如果是出了故障的話我處理不了，如果只是它在耍性子，如今這也不是我該負責的了」 | 「Nếu hỏng hóc thì tôi cũng bó tay,\ncòn nếu chỉ là đang dỗi, thì đó đã nằm ngoài quyền hạn của tôi rồi.」 | 「Nếu hỏng hóc thì tao cũng bó tay,\ncòn nếu chỉ là đang dỗi, thì đó đã nằm ngoài quyền hạn của tao rồi.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 1520 | 「いや、俺の頭が固く、古いだけのことだろう」 | 「不不，多半是怪我思想陳腐，頭腦愚鈍」 | 「Không, chỉ là do đầu óc tôi cứng nhắc và cổ hủ quá thôi.」 | 「Không, chỉ là do đầu óc tao cứng nhắc và cổ hủ quá thôi.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 1552 | 「追い詰められれば自分のことしか考えられない。\n人間は――少なくとも俺は、そういう程度だ」 | 「人在窮途末路之時，是只顧得上保全自我的，至少我就只有這點本事」 | 「Khi bị dồn vào chân tường, người ta chỉ nghĩ đến bản thân mình thôi. \nCon người——ít nhất là tôi, cũng chỉ ở mức độ đó.」 | 「Khi bị dồn vào chân tường, người ta chỉ nghĩ đến bản thân mình thôi. \nCon người——ít nhất là tao, cũng chỉ ở mức độ đó.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 1708 | 「あ、これは失礼。俺――自分は宗方[じんろく,1]甚六。\nみかん鉄道\x%l機関士;#00ffc040;機関士%l;#;です」 | 「啊，恕我有失問候，我是宗方甚六，是橙鐵路的機車\x%l機関士;#00ffc040;司機%l;#;」 | 「A, tôi mới là người thất lễ. Tôi——tên là Munakata Jinroku. \n\x%l機関士;#00ffc040;Lái tàu%l;#; của Đường sắt Mikan.」 | 「A, tao mới là người thất lễ. Tao——tên là Munakata Jinroku. \n\x%l機関士;#00ffc040;Lái tàu%l;#; của Đường sắt Mikan.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 2143 | 「そこまで大きな話になると、俺――\n私には、どうにも、夢物語にしか聞こえなくなる」 | 「貴公司的計劃如此宏大，在我看來——恕我直言，未免過於異想天開」 | 「Khi câu chuyện trở nên lớn lao đến mức đó, với tôi—— \nvới tôi, nó nghe chẳng khác nào một câu chuyện viển vông.」 | 「Khi câu chuyện trở nên lớn lao đến mức đó, với tao—— \nvới tao, nó nghe chẳng khác nào một câu chuyện viển vông.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 2212 | 「それなら、ネコをかぶっても仕方ない。\n俺は、どこにでもいる\x%l保線;#00ffc040;保線%l;#;上がりの\x%l機関士;#00ffc040;機関士%l;#;です」 | 「那我也無需再向各位客套，我只是一介隨處可見的有幾分\x%l保線;#00ffc040;巡線%l;#;經驗的\x%l機関士;#00ffc040;司機%l;#;」 | 「Nếu vậy thì, tôi cũng không cần phải giả vờ nữa. \nTôi chỉ là một \x%l機関士;#00ffc040;lái tàu%l;#; đi lên từ \x%l保線;#00ffc040;bảo trì đường ray%l;#;, có thể bắt gặp ở bất cứ đâu thôi.」 | 「Nếu vậy thì, tao cũng không cần phải giả vờ nữa. \nTao chỉ là một \x%l機関士;#00ffc040;lái tàu%l;#; đi lên từ \x%l保線;#00ffc040;bảo trì đường ray%l;#;, có thể bắt gặp ở bất cứ đâu thôi.」 |
| ハチロク12_ムナカタ来訪.txt.toml | 2248 | 「俺は今は、お前になにかを頼める立場でもないが」 | 「雖然如今，我也再無任何權利向你提出請求」 | 「Mặc dù hiện tại tôi không ở vị trí có thể nhờ vả nhóc chuyện gì」 | 「Mặc dù hiện tại tao không ở vị trí có thể nhờ vả nhóc chuyện gì」 |
| ハチロク15a_痛みとの決別.txt.toml | 1770 | 「俺の頼みを――よくぞここまで完璧に果たしてくれた」 | 「你圓滿完成了我交給你的任務」 | 「Lời nhờ vả của tôi——Cô đã hoàn thành một cách hoàn hảo đến mức này」 | 「Lời nhờ vả của tao——Cô đã hoàn thành một cách hoàn hảo đến mức này」 |
| ハチロク15a_痛みとの決別.txt.toml | 1772 | 「オウムか、お前は。\n俺がいるのがそんなに不思議か」 | 「你是變成鸚鵡了嗎？看到我在這有這麼不可思議嗎」 | 「Cô là vẹt đấy à.\nThấy tôi ở đây có gì lạ lắm sao」 | 「Cô là vẹt đấy à.\nThấy tao ở đây có gì lạ lắm sao」 |
| ハチロク15a_痛みとの決別.txt.toml | 2031 | 「礼を言う。\n今の俺は、お前にとって、\x%l機関士;#00ffc040;機関士%l;#;でもなんでもないのに」 | 「我要謝謝你。明明我都不是你的\x%l機関士;#00ffc040;司機%l;#;了」 | 「Cảm ơn cô.\nDù tôi bây giờ, đối với cô, chẳng còn là \x%l機関士;#00ffc040;người lái tàu%l;#; hay gì nữa」 | 「Cảm ơn cô.\nDù tao bây giờ, đối với cô, chẳng còn là \x%l機関士;#00ffc040;người lái tàu%l;#; hay gì nữa」 |
| ハチロク15b_さよなら列車.txt.toml | 1683 | 「俺も驚いた。しかも、[やつしろ,2]八ツ城行きの乗務――\n本線を、Ⅸ号で走るとはな」 | 「我也很驚訝。而且這趟車是去八代方向的，沒想到能用九號跑這條幹線」 | 「Tôi cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi [やつしろ,2]Yatsushiro——\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」 | 「Tao cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi [やつしろ,2]Yatsushiro——\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」 |
| ハチロク15b_さよなら列車.txt.toml | 1846 | 「そりゃあ、良かった。\n俺も多少は、こりゃ夢じゃないかと思ったからな」 | 「那就好。其實我也有點覺得自己是不是在做夢」 | 「Vậy thì tốt.\nThực ra tôi cũng hơi nghĩ đây có phải là mơ hay không đấy」 | 「Vậy thì tốt.\nThực ra tao cũng hơi nghĩ đây có phải là mơ hay không đấy」 |
| ハチロク16_春.txt.toml | 1301 | 「……さぁな。俺は知らんし――\n多分、だがな。知らんでいる方がいい代物だろう」 | 「……誰知道呢。我不清楚——不過，可能，你還是不要知道這件事比較好吧」 | 「……Ai mà biết được. Tôi không biết――\nNhưng có lẽ. Tốt nhất là không nên biết về thứ đó đâu.」 | 「……Ai mà biết được. Tao không biết――\nNhưng có lẽ. Tốt nhất là không nên biết về thứ đó đâu.」 |
| ハチロク16_春.txt.toml | 1884 | 「おれはマスターではない。\nで、この人たちは、御一夜鉄道のみなさんだ」 | 「我不是你的主人。他們是御一夜鐵路的人」 | 「Tôi không phải là Master.\nVà, những người này là người của Đường sắt Ohitoyo.」 | 「Tao không phải là Master.\nVà, những người này là người của Đường sắt Ohitoyo.」 |
| ハチロク16_春.txt.toml | 1910 | 「だから、俺はマスターではない。\nで、そいつはいわゆるテレビ電話……みたいなもんだ」 | 「所以說，我不是你的主人。這就是所謂的視訊電話一類的東西」 | 「Đã bảo tôi không phải là Master mà.\nVà, cái đó là điện thoại truyền hình……đại loại thế.」 | 「Đã bảo tao không phải là Master mà.\nVà, cái đó là điện thoại truyền hình……đại loại thế.」 |
| ハチロク16_春.txt.toml | 2025 | 「というか、いい加減に覚えてくれ。\n俺は、こだまのマスターじゃない」 | 「話說，你也該記住了吧。我可不是你的主人」 | 「Nói đúng hơn là, làm ơn nhớ cho kỹ giùm cái.\nTôi không phải là Master của Kodama.」 | 「Nói đúng hơn là, làm ơn nhớ cho kỹ giùm cái.\nTao không phải là Master của Kodama.」 |

## §4. P7 — Kisaki 日々姫さんのお兄さん → "anh trai của Hibiki" (0 dòng sửa — đã đúng sẵn)

Quét toàn bộ CSV3 (91.731 dòng, kể cả stale set): chỉ có **2 dòng** JP chứa 日々姫さんのお兄さん, cả hai đều đã dịch đúng "anh trai của Hibiki" từ bản gốc (src=csv3 — không có fix audit/moan/unification nào chạm vào chúng), và TOML-2 khớp từng ký tự (sau chuẩn hoá `\n`):

| File | Key | Người nói | JP | TW | VN hiện tại (GIỮ) |
|---|---|---|---|---|---|
| 共通10_クマ川くだりで見る景色.txt.toml | 2472 | 稀咲 (Kisaki hỏi Soutetsu) | 「日々姫さんのお兄さん？\nなら、ボクに自己紹介させてください」 | 「您是日日姬同學的哥哥？那麼，請容我自我介紹一下」 | 「Anh là anh trai của Hibiki sao?\nVậy thì, xin cho phép tôi tự giới thiệu.」 |
| 共通10_クマ川くだりで見る景色.txt.toml | 2449 | 稀咲 | 「工場誘致のお話ですか？\nええと……日々姫さんのお兄さんは――」 | 「工廠落戶的事情嗎？呃……日日姬同學的哥哥是——」 | 「Anh đang nói chuyện thu hút nhà máy sao?\nÀ ừm……anh trai của Hibiki là――」 |

Kiểm chứng thêm 3 dòng liên quan (cùng referent — anh trai của Hibiki, tức Soutetsu — nhưng JP dùng dạng khác), tất cả cũng đã đúng, không sửa:

| File | Key | JP | VN hiện tại (GIỮ) |
|---|---|---|---|
| 共通10_クマ川くだりで見る景色.txt.toml | 2191 | 「あのお兄さんが帰ってきてると教えてくれないなんて」 | 「Anh trai em về rồi mà cũng chẳng thèm nói cho tôi biết.」 |
| 日々姫07_たったひとりの宣戦布告.txt.toml | 2111 | 「この人は――日々姫のご家族かな？　お兄さん？」 | 「Người này là——người nhà của Hibiki sao? Anh trai à?」 |
| ポーレット03_廃炭鉱.txt.toml | 2141 | 「ほら、日々姫ちゃんのお兄さん、なんだし」 | 「Thì, anh là anh trai của Hibiki mà.」 |

Không tồn tại dòng nào trong toàn dự án dịch お兄さん (anh trai của Hibiki) thành "chị Hibiki": quét VN chứa "chị Hibiki" cho thấy tất cả đều dịch 日々姫さん/日々姫ちゃん (chính Hibiki), đúng. **P7 = 0 dòng sửa; quyết định của Hieu đã được thoả mãn sẵn trong giá trị hiện tại.** (Nhiều khả năng dạng sai "chị Hibiki" chỉ xuất hiện trong bản nháp/tài liệu tips trước 04:03, không còn trong bản dịch hiện tại.)

## §5. O61 — QUYẾT ĐỊNH: "tao" cho cả 6 dòng (ハチロク16_春)

### 5a. Sửa lại tên file trong list

List (§2 P15, §7 O61) và task ghi "ハチロク10_炙り出し" cho cả P15 ×4 lẫn O61 6 key — **sai file**. Kiểm chứng:

- TOML-2 + CSV3: file ハチロク10_炙り出し **không có** các key 1297/1306/1637/1903/2050/2070 (1297/1306/1903/2050 không tồn tại; 1637 là 双鉄, 2070 là ハチロク). Audit ハチロク10 cũng không nhắc Munakata "tôi" (12 lỗi của file đó là đại từ Soutetsu + gasp + Ohimitera + 乗員).
- Nguồn đúng là **ROUTE-AUDIT.md mục ハチロク16_春**: "Chờ Hieu: (2) Munakata 'tôi' không có 俺 tường minh 6 dòng (1297, 1306, 1637, 1903, 2050, 2070)" và "Munakata 俺/おれ→'tao' ×4 (1301, 1884, 1910, 2025)" — cùng một file, cùng một danh sách key. Tất cả 10 key đều tồn tại trong ハチロク16_春, Character đều là 宗方.

### 5b. Bằng chứng từng dòng (JP + TW + dòng kề)

| Key | JP | TW (xác nhận ngôi thứ nhất) | Dòng kề / ngữ cảnh | "tôi" trong VN |
|---|---|---|---|---|
| 1297 | 「……まさか、\nオリヴィに借りをつくるとは思わなかった」 | 「……沒想到，我還會欠奧莉薇這個人情」 (我 = tôi) | Ngay trước 1301 (俺) 4 key, cùng cảnh trò chuyện với Soutetsu/Hachiroku về Olivy | "tôi lại mang nợ Olivy" |
| 1306 | 「……その節は、大変申し訳無いことを」 | 「……那件事真是麻煩你了」 | Ngay sau 1304 (双鉄 đáp lời), kẹp giữa 1301 (俺) và 1307 (日々姫); cùng một lượt xin lỗi | "tôi thực sự rất xin lỗi" |
| 1637 | 「そう言ってもらえると――\nお世辞でしょうが、なんとも照れくさいもんですな」 | 「你能這麼說——雖然可能是客套話，但是我總覺得有點不好意思」 (我) | Đáp lại 1635 (双鉄 "やはり、幸せな夢だったのか"); gọi Soutetsu là "Cậu" — cùng register thô | "tôi cũng thấy ngại quá" |
| 1903 | 「\x%l保線;#00ffc040;保線%l;#;の専門会社の方も、すぐ参加できずにすみません。\nですが」 | 「我沒能很快加入專業巡線的公司，抱歉。但是——」 (我) | 7 key trước 1910 (俺); cùng cảnh Hachiroku kể chuyện Olivy, Munakata xin lỗi vì chưa tham gia được | "Tôi cũng xin lỗi vì chưa thể tham gia ngay…" |
| 2050 | 「借りですね。だから、返しますよ。\nこいつ――こだまに。オリヴィの遺した、全てのものに」 | 「這是欠你的人情。所以，我要還這個人情。還給小玉。把奧莉薇留下的一切還給她」 (我) | 25 key sau 2025 (俺); cùng mạch "mang nợ Olivy → trả nợ cho Kodama" với 1297 | "tôi sẽ trả lại" |
| 2070 | 「\x%l機関士;#00ffc040;機関士%l;#;の方は、教導を任されることになりました。\n御鉄さんから話をいただいていたおかげです」 | 「那邊的\x%l機関士;#00ffc040;司機%l;#;也交給我來帶了。這都是多虧了御鐵這邊向我提出的邀請」 (我) | 45 key sau 2025 (俺); cùng cảnh, Munakata nhận việc dạy lái tàu từ Ohitoyo | "tôi đã được giao nhiệm vụ chỉ dạy" |

### 5c. Quyết định + lý do

**QUYẾT ĐỊNH (theo uỷ quyền của Hieu, không park): "tao" cho cả 6 dòng.**

1. **Cùng file, cùng cảnh, cùng người nói:** trong ハチロク16_春, Munakata dùng 俺/おれ tường minh ở 4 dòng (1301, 1884, 1910, 2025) xen kẽ với 6 dòng này — 1297/1306 kẹp sát 1301 (cách 4–5 key), 1903 cách 1910 có 7 key, 2050/2070 cùng mạch trả nợ Olivy với 2025. Để "tôi" ở 6 dòng này thì giọng Munakata sẽ lật qua lật lại "tao"/"tôi" trong cùng một buổi sáng, cùng một cuộc trò chuyện — mâu thuẫn trực tiếp với P15 (đại từ tự xưng của Munakata đã chốt là "tao").
2. **TW xác nhận ngôi thứ nhất ở cả 6 dòng** (我 5/6 dòng; 1306 TW lược chủ ngữ nhưng mạch xin lỗi kẹp giữa hai dòng 俺 của cùng người nói).
3. **Tính trang trọng không đổi được đại từ của ông:** các dòng xin lỗi trang trọng (1306, 1903) không phải lý do giữ "tôi" — chính Munakata cũng dùng 俺 trong câu tự giới thiệu trang trọng ở ハチロク12 1708 (「俺――自分は宗方甚六」) và trong câu từ chối làm Master ở 1910/2025. Register thô là bản sắc của ông, không phải trạng thái cảm xúc từng câu.
4. **Phạm vi quyết định chỉ giới hạn ở 6 dòng này + file này:** không mở rộng thành quy tắc toàn dự án cho các dòng Munakata "tôi" không có 俺 ở file khác (xem §6 — 55 dòng, cần một mục riêng nếu Hieu muốn).

### O61 — 6 dòng (old_vn = giá trị hiện tại: csv3, trừ 2070 là fix U2a)

| File | Key | JP | TW | old_vn (giá trị hiện tại) | fix |
|---|---|---|---|---|---|
| ハチロク16_春.txt.toml | 1297 | 「……まさか、\nオリヴィに借りをつくるとは思わなかった」 | 「……沒想到，我還會欠奧莉薇這個人情」 | 「……Không ngờ,\ntôi lại mang nợ Olivy.」 | 「……Không ngờ,\ntao lại mang nợ Olivy.」 |
| ハチロク16_春.txt.toml | 1306 | 「……その節は、大変申し訳無いことを」 | 「……那件事真是麻煩你了」 | 「……Lần đó, tôi thực sự rất xin lỗi.」 | 「……Lần đó, tao thực sự rất xin lỗi.」 |
| ハチロク16_春.txt.toml | 1637 | 「そう言ってもらえると――\nお世辞でしょうが、なんとも照れくさいもんですな」 | 「你能這麼說——雖然可能是客套話，但是我總覺得有點不好意思」 | 「Cậu nói vậy――\nDù chỉ là lời khách sáo, nhưng tôi cũng thấy ngại quá.」 | 「Cậu nói vậy――\nDù chỉ là lời khách sáo, nhưng tao cũng thấy ngại quá.」 |
| ハチロク16_春.txt.toml | 1903 | 「\x%l保線;#00ffc040;保線%l;#;の専門会社の方も、すぐ参加できずにすみません。\nですが」 | 「我沒能很快加入專業巡線的公司，抱歉。但是——」 | 「Tôi cũng xin lỗi vì chưa thể tham gia ngay vào công ty chuyên về \x%l保線;#00ffc040;bảo trì đường ray%l;#;.\nNhưng mà.」 | 「Tao cũng xin lỗi vì chưa thể tham gia ngay vào công ty chuyên về \x%l保線;#00ffc040;bảo trì đường ray%l;#;.\nNhưng mà.」 |
| ハチロク16_春.txt.toml | 2050 | 「借りですね。だから、返しますよ。\nこいつ――こだまに。オリヴィの遺した、全てのものに」 | 「這是欠你的人情。所以，我要還這個人情。還給小玉。把奧莉薇留下的一切還給她」 | 「Là mang nợ đấy. Thế nên, tôi sẽ trả lại.\nCho con bé này――Kodama. Trả lại tất cả những gì Olivy đã để lại.」 | 「Là mang nợ đấy. Thế nên, tao sẽ trả lại.\nCho con bé này――Kodama. Trả lại tất cả những gì Olivy đã để lại.」 |
| ハチロク16_春.txt.toml | 2070 | 「\x%l機関士;#00ffc040;機関士%l;#;の方は、教導を任されることになりました。\n御鉄さんから話をいただいていたおかげです」 | 「那邊的\x%l機関士;#00ffc040;司機%l;#;也交給我來帶了。這都是多虧了御鐵這邊向我提出的邀請」 | 「Về phần \x%l機関士;#00ffc040;lái tàu%l;#;, tôi đã được giao nhiệm vụ chỉ dạy.\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohitoyo các cô cậu đấy.」 | 「Về phần \x%l機関士;#00ffc040;lái tàu%l;#;, tao đã được giao nhiệm vụ chỉ dạy.\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohitoyo các cô cậu đấy.」 |

## §6. Giữ nguyên / cờ (kept / flagged — đã xem nhưng KHÔNG sửa)

- **P7: 5 dòng đã đúng sẵn** (2 dòng 日々姫さんのお兄さん + 3 dòng liên quan, §4) — GIỮ, 0 dòng sửa.
- **お前 — KHÔNG đụng theo P15:** "nhóc" (ハチロク12 2248), "cô" (ハチロク15a 1770/1772/2031 — Munakata gọi Hachiroku), "cậu" (ハチロク04 1814; ハチロク16 1637 — Munakata gọi Soutetsu), "các cậu" (ハチロク04 2065) giữ nguyên toàn bộ.
- **Các dòng 俺/オレ của người khác — KHÔNG phải Munakata, không sửa:** サッカー少年Ｂ/Ｃ (日々姫06 1904/2213/2393, "Cháu"), 後東 (ニイロク03 1802, グランド06 2011, ニイロク04 2029), 雲山 (ハチロク11 2074). "オレンジ" (グランド10 1926, monologue 日々姫05 2840 v.v.) là từ "orange", không phải đại từ — không sửa.
- **CỜ CHO ĐIỀU PHỐI / HIEU (không tự mở rộng phạm vi):** còn **55 dòng** Munakata (宗方) khác toàn dự án mà VN dùng "tôi" nhưng JP không có 俺/おれ/オレ tường minh (vd. ハチロク04 1845/2113/2223, ハチロク12 1147 — JP dùng 私, 1541/1988/2219, ハチロク15b 1520/1686/1787, 凪ふかみ08a 1792/1814/1820). O61 chỉ quyết 6 dòng trong ハチロク16_春 vì có bằng chứng cùng-cảnh với 俺; 55 dòng còn lại — trong đó có những dòng JP dùng 私 trang trọng (ハチロク12 1147 「私が蓄積した経験が」) — cần một mục thống nhất riêng (áp "tao" toàn bộ hay chỉ khi JP có 俺?) trước khi đụng vào. **Không sửa trong đợt này.**
- **CỜ VỀ LIST (đã hiệu chỉnh trong review này, đề nghị sửa list):** (a) P15 "17 dòng" thực tế là 18 (thiếu おれ 1884); (b) P15 ×4 và O61 6 key thuộc **ハチロク16_春**, không phải ハチロク10_炙り出し như list ghi.
- **Không đụng dòng gasp Ư hay dòng "Kh" nào.** Không sửa gloss %l (chỉ giữ nguyên thẻ \x%l…%l;#; trong các fix 1708/1903/2070/2212/2031).

## §7. Lượt soát 2 (second pass — bắt buộc)

Soát lại toàn bộ 24 fix theo từng dòng JP (đọc lại JP + đếm 俺/おれ/オレ + đối chiếu diff old_vn→fix):

- **Tổng: 24 · Tái kiểm chứng: 24 · Loại bỏ: 0 · Sửa lại: 0.**
- Kiểm chứng cơ học: chuẩn hoá "tôi"/"Tôi"→"tao"/"Tao" xong, old_vn và fix giống hệt nhau ở cả 24 dòng (diff duy nhất là họ "ôi"→"ao" trong đại từ tự xưng); 0 "tôi"/"Tôi" còn sót trong fix; tổng 28 lần thay "tôi"→"tao" (P15: 22 lần / 18 dòng; O61: 6 lần / 6 dòng).
- Đối chiếu JP: P15 — JP có 俺/おれ/オレ ở cả 18 dòng (2084 có 2 オレ → fix 2 "tao"; 1708/2143/2212 JP có 1 俺 nhưng VN diễn tự xưng 2 lần — cả hai đều là Munakata tự nhắc, đều → "tao", đã đọc kỹ từng câu); O61 — JP có 0 俺 (đúng như tên mục), quyết "tao" theo bằng chứng cùng-cảnh §5b/§5c.
- old_vn khớp map giá trị hiện tại (unification-đã-gộp > moan > audit > CSV3): 22 dòng src=csv3, 2 dòng src=unif-U2a (ハチロク16 1884/2070 — fix đợt này giữ nguyên phần "Đường sắt Ohitoyo" của U2a).
- P7 soát lại lần 2: quét toàn CSV3 (91.731 dòng, kể cả stale set) vẫn chỉ 2 dòng JP 日々姫さんのお兄さん, cả hai đã đúng — 0 dòng sửa, không thay đổi.

## §8. Khối TOML (parse-verified)

Mỗi file một khối; literal backslash-n trong giá trị fix được viết `\\n` trong raw text của khối. Đã parse-verify bằng tomllib: 5 file / 24 key, giá trị parse ra khớp fix trong JSON tuyệt đối.

#### ハチロク04_小畑越え.txt.toml

```toml
[script]
"1814" = "「Không, tao cũng hiểu được điểm mà giám đốc công ty cậu đang lo ngại.\\nCho dù có ngoan ngoãn tuân lệnh, nếu nó vẫn giữ tình cảm với Đường sắt Mikan――」"
"2065" = "「Nhờ có việc chuyển nhượng, cả nó và tao đều có thể quay lại tuyến chính.\\nToàn là chuyện tốt――nếu như các cậu có thể sử dụng nó một cách thành thạo.」"
"2084" = "「Nếu hỏng hóc thì tao cũng bó tay,\\ncòn nếu chỉ là đang dỗi, thì đó đã nằm ngoài quyền hạn của tao rồi.」"
```

#### ハチロク12_ムナカタ来訪.txt.toml

```toml
[script]
"1520" = "「Không, chỉ là do đầu óc tao cứng nhắc và cổ hủ quá thôi.」"
"1552" = "「Khi bị dồn vào chân tường, người ta chỉ nghĩ đến bản thân mình thôi. \\nCon người——ít nhất là tao, cũng chỉ ở mức độ đó.」"
"1708" = "「A, tao mới là người thất lễ. Tao——tên là Munakata Jinroku. \\n\\x%l機関士;#00ffc040;Lái tàu%l;#; của Đường sắt Mikan.」"
"2143" = "「Khi câu chuyện trở nên lớn lao đến mức đó, với tao—— \\nvới tao, nó nghe chẳng khác nào một câu chuyện viển vông.」"
"2212" = "「Nếu vậy thì, tao cũng không cần phải giả vờ nữa. \\nTao chỉ là một \\x%l機関士;#00ffc040;lái tàu%l;#; đi lên từ \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, có thể bắt gặp ở bất cứ đâu thôi.」"
"2248" = "「Mặc dù hiện tại tao không ở vị trí có thể nhờ vả nhóc chuyện gì」"
```

#### ハチロク15a_痛みとの決別.txt.toml

```toml
[script]
"1770" = "「Lời nhờ vả của tao——Cô đã hoàn thành một cách hoàn hảo đến mức này」"
"1772" = "「Cô là vẹt đấy à.\\nThấy tao ở đây có gì lạ lắm sao」"
"2031" = "「Cảm ơn cô.\\nDù tao bây giờ, đối với cô, chẳng còn là \\x%l機関士;#00ffc040;người lái tàu%l;#; hay gì nữa」"
```

#### ハチロク15b_さよなら列車.txt.toml

```toml
[script]
"1683" = "「Tao cũng bất ngờ lắm. Hơn nữa lại còn là chuyến tàu đi [やつしろ,2]Yatsushiro——\\nKhông ngờ lại được chạy đầu máy số 9 trên tuyến chính đấy」"
"1846" = "「Vậy thì tốt.\\nThực ra tao cũng hơi nghĩ đây có phải là mơ hay không đấy」"
```

#### ハチロク16_春.txt.toml

```toml
[script]
"1297" = "「……Không ngờ,\\ntao lại mang nợ Olivy.」"
"1301" = "「……Ai mà biết được. Tao không biết――\\nNhưng có lẽ. Tốt nhất là không nên biết về thứ đó đâu.」"
"1306" = "「……Lần đó, tao thực sự rất xin lỗi.」"
"1637" = "「Cậu nói vậy――\\nDù chỉ là lời khách sáo, nhưng tao cũng thấy ngại quá.」"
"1884" = "「Tao không phải là Master.\\nVà, những người này là người của Đường sắt Ohitoyo.」"
"1903" = "「Tao cũng xin lỗi vì chưa thể tham gia ngay vào công ty chuyên về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;.\\nNhưng mà.」"
"1910" = "「Đã bảo tao không phải là Master mà.\\nVà, cái đó là điện thoại truyền hình……đại loại thế.」"
"2025" = "「Nói đúng hơn là, làm ơn nhớ cho kỹ giùm cái.\\nTao không phải là Master của Kodama.」"
"2050" = "「Là mang nợ đấy. Thế nên, tao sẽ trả lại.\\nCho con bé này――Kodama. Trả lại tất cả những gì Olivy đã để lại.」"
"2070" = "「Về phần \\x%l機関士;#00ffc040;lái tàu%l;#;, tao đã được giao nhiệm vụ chỉ dạy.\\nCũng nhờ có lời đề nghị từ phía Đường sắt Ohitoyo các cô cậu đấy.」"
```

## Kết bài

Đợt U9 xong: **P15: 18 dòng** (Munakata 俺/おれ/オレ → "tao", 5 file — nhiều hơn 1 dòng so với list vì bắt thêm おれ hiragana 1884), **O61: 6 dòng** (quyết "tao" cho cả 6, theo bằng chứng cùng-cảnh trong ハチロク16_春), **P7: 0 dòng** (2 dòng duy nhất đã đúng sẵn "anh trai của Hibiki"). Tổng **24 dòng / 5 file**, lượt soát 2: **24/24, 0 loại, 0 sửa**. Hai lỗi ghi chép trong list đã hiệu chỉnh trong review này: số dòng P15 (17→18) và tên file của P15 ×4 + O61 (ハチロク10_炙り出し→ハチロク16_春). Nợ lại cho điều phối: 55 dòng Munakata "tôi" không có 俺 ở các file khác (cần mục riêng nếu muốn thống nhất toàn bộ), và P7 không còn việc gì nữa.
