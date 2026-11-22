# Unification §1 set-2 — T3, T10, T13, T14, T17, T18 — đợt U3

**Lưu ý số hiệu mục:** task giao việc gọi Migita là "T18", nhưng theo `UNIFICATION-LIST.md` thì Migita = **T14** và 乗務鞄 = **T18**. Review này dùng số hiệu của LIST (brief quy định `item` = list-item id). Phạm vi đợt U3: T3, T10, T13, T14, T17, T18 — tổng **240 dòng duy nhất** (243 lượt mục trừ 3 dòng 2 mục), **69 file**.

## 1. Phạm vi

| Mục | Thuật ngữ | Dòng sửa | File |
|---|---|---|---|
| T3 | 帝鉄 → "Đường sắt Teitetsu" | **55** | 25 |
| T10 | 電車姫 → "Công chúa Tàu điện" | **28** | 12 |
| T13 | 宮司 → "đền chủ" | **38** | 7 |
| T14 | Migita (xưởng rượu) → "Migita Ichi" | **21** | 15 |
| T17 | 術仙 → "Jutsusen" | **85** | 27 |
| T18 | 乗務鞄 / 運転鞄 / 運転士鞄 → "túi công tác" | **16** | 6 |
| **Tổng** | 6 mục | **240 dòng duy nhất** | **69** |

- 3 dòng mang 2 mục (1 entry duy nhất, fix gộp cả hai thay đổi): グランドリライト06_稀咲 3242 / 3540 (T13+T18); riêng 3472 nay là 3 mục (T13+T18+T11, ghép với fix U4 đã gộp — xem ghi chú điều phối cuối REVIEW).
- Nguồn old_vn: CSV3 VN **151** dòng · audit fix **80** · unification-merged fix **9** (ハチロク12_ムナカタ来訪 1525, ポーレット04_ヒヤリング 1517, ポーレット09_ストーブ客車 2129, 日々姫09_run_with_our_dreams 1906, 日々姫09_静かなる開戦 1690 + 4 dòng ghép với U4 (Grand06 3472, ハチロク12_再開発 2508, ハチロク13 2555, ポーレット03 1723) — old_vn đã lấy giá trị sau đợt đã gộp, fix mới chỉ thay đổi trên nền đó) · moan fix **0**.
- So với ước lượng §0 của list: T3 57 → **thực 55** (50 "Đường sắt Hoàng gia" có JP 帝鉄 + 5 gloss "Đường sắt Đế quốc", xem §3 T3b) · T10 28 → **thực 28** · T13 ~28 → **thực 38** (list đếm thiếu: "Akai-guji" thực tế 18 không phải 19, nhưng cộng thêm "Akai Guuji" 2 + "ông Guuji" 7 — xem §4) · T14 10+2+1=13 → **thực 21** (list đếm thiếu các dạng "xưởng rượu Migita" thiếu "Ichi" và "Migitakazu") · T17 28 → **thực 85** (bẫy T17 lớn hơn list ghi: 61 fix audit đã dùng "Jutsu-sen" trước quyết định 21/11, không phải chỉ 3 dòng đã biết) · T18 18 → **thực 16** (9 dòng đã là "túi công tác", list chỉ ghi 1 dòng đã sửa trong audit).

## 2. Phương pháp liệt kê (enumeration)

1. Đọc CSV3 good-set: **87.833 dòng** (91.731 − 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`). Trước khi kết luận dòng nào vắng mặt, đã tìm trên TOÀN BỘ file CSV3 (mọi folder) — xem §5 mục T10 [characters].
2. Nạp TOÀN BỘ fix list trước đó để tính giá trị hiện tại (current value) của từng dòng: moan fix nếu (file,key) có trong bất kỳ `moans/moan-*-wrong.json` nào, ngược lại audit fix nếu có trong bất kỳ `audit-*-wrong.json` nào, ngược lại unification-merged fix nếu có trong `unification/unification-*-wrong.json` đã gộp, ngược lại CSV3 VN. Map fix→file bằng khớp (key, JP) với CSV3; các file dict-shape không có JP được map riêng: `audit-00common14-wrong.json` (khớp old_vn với CSV3), `audit-lr-nagih2-wrong.json` (dict key→fix, file lr_凪h2_虎さんの交尾), và 1 dòng [selections] (audit-nagifukami07 key 86, JP trống — khớp qua TW). Tổng map được: **audit 9.240 + moan 1.516 + unification-merged 656 cặp (file,key), 0 dòng không map được**.
3. Liệt kê ứng viên theo giá trị hiện tại (không phải chỉ CSV3 VN — vì fix audit/moan/unification có thể đã đưa dạng cũ vào hoặc đã sửa đi): T3 tìm "Hoàng gia"/"Đường sắt Đế quốc" · T10 tìm "Denshahime"/"Densha Hime"/"Công chúa Xe điện"/"Điện Xa Cơ"/"Điện xá Công chúa" + quét JP 電車姫 · T13 tìm "guji"/"thầy cúng"/"cha xứ"/"Thầy Akai"/"Cung tư tế" + quét JP 宮司 · T14 tìm "Migita" không có "Migita Ichi" + quét JP 右田一/酒造/酒蔵 · T17 tìm "Jutsu-sen"/"Jussen" + quét toàn bộ fix audit chứa "Jutsu-sen" (bẫy) + quét JP 術仙 · T18 quét JP 乗務鞄/運転鞄/運転士鞄.
4. Mỗi dòng ứng viên đều được đọc JP (+TW) để xác nhận JP chứa đúng thuật ngữ gốc trước khi sửa. Dòng nào JP không chứa thuật ngữ thì KHÔNG sửa — ghi flag ở §5.
5. Không chạm gasp-Ư, "Kh", đại từ, hay bất kỳ nội dung nào khác của dòng. Không sửa lại dòng đã đúng. Không sửa ROUTE-UNIFICATION.md, MEMORY.md, queue, hay bất kỳ file audit/moan nào.

## 3. Quyết định trong đợt (OPEN / diễn giải, theo ủy quyền của Hieu)

### T3b — 5 gloss "Đường sắt Đế quốc" → "Đường sắt Teitetsu"
List T3 ghi: dạng đầy đủ "Đường sắt Đế quốc" CHỈ dùng trong tooltip %l ở lần xuất hiện đầu (file 01 key 1335 — GIỮ NGUYÊN, và key đó là gloss của 帝鉄貨物, thuộc T4 — không đụng đợt này). 5 gloss %l của 帝鉄 trong thoại ở các file sau (れいな02 63, ハチロク09 2792, 日々姫01 2097, 日々姫14 1276, 真闇01 1621) dùng "Đường sắt Đế quốc" — theo đúng quy tắc T3 thì phải về "Đường sắt Teitetsu". Áp dụng. Riêng グランドリライト10 1134 ("Đường sắt Đế quốc Hinomoto" cho 日ノ本帝有鉄道) KHÔNG sửa — đó là T63 (coordinator đã chốt E1: 帝有鉄道 → "Đường sắt Đế quốc Hinomoto", batch khác).

### T14 — "Migitai" (mục con OPEN O62 của list)
3 dòng 凪ふかみ03 (1071/1429/2525) dùng "Migitai" cho JP 右田一酒造元 / 右田一. QUYẾT: "Migitai" không phải tên riêng khác — đó là cách đọc sai của 右田一 (Migita-ichi bị đọc liền thành "Migitai"); cùng một thực thể xưởng rượu với 20+ dòng "Migita Ichi" khác trong dự án. Sửa về "Migita Ichi". Bằng chứng: JP 1429 「右田一――右田一酒造元さんです」 (ruby みぎたいちしゅぞうもと ở các dòng khác); TW các dòng này cũng là 右田一酒造元.

### T14 — JP 右田の蔵 / 右田の酒蔵 (không có 一)
3 dòng (共通07 2025, 日々姫01 1688, 日々姫08 3067) có JP 右田の酒蔵/右田の蔵 nhưng VN dùng tên thực thể "xưởng rượu Migita" (thiếu "Ichi"). QUYẾT: cùng một xưởng rượu nhà Migita (chỉ có một xưởng rượu Migita trong truyện; 杜氏 của 右田の蔵 chính là Toji của xưởng) — thêm "Ichi". Ngược lại, các dạng sở hữu "nhà Migita" (仲国06 2347 "Nhà Migita là xưởng nấu rượu", 日々姫07 1815, 稀咲h3 3664/2111/3478, 凪ふかみ02 1273) GIỮ NGUYÊN — đó là họ gia đình, không phải tên thực thể.

### T17 — Khôi phục ポーレット07_支線 2311 (audit cắt cụt dòng)
Fix audit của dòng này (audit-paulette07-shisen-wrong.json) đã cắt cụt giá trị chỉ còn nửa đầu và thêm ngoặc 「」 sai: old_vn = "「Sau khi đưa chuyến tàu chiều về đến Ohitoyo,」" trong khi CSV3 VN đầy đủ là "Sau khi đưa chuyến tàu chiều về đến Ohimitera, 8620 sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsu-sen." (JP + TW đều đủ hai vế; JP 術仙洞廃駅). Đây là lỗi fix audit, không phải lỗi dịch gốc. QUYẾT: khôi phục toàn bộ giá trị CSV3 với "Ohimitera"→"Ohitoyo" (T1 đã gộp) và "Jutsu-sen"→"Jutsusen" (T17); old_vn trong JSON là fix audit bị cắt cụt, fix là giá trị đầy đủ đã khôi phục (giữ nguyên tag %l và literal \n).

### T17 — Các trích dẫn bẫy trong list
List T17 nêu 3 dòng audit đã dùng "Jutsu-sen" trước quyết định: Paulette 16 key 2252 ✓ (có, đã lật), Hachiroku 12 key 1525 ✓ (có — current value là fix của đợt unification T1, đã lật), **Paulette 02 key 1525 ✗ (KHÔNG TỒN TẠI — file ポーレット02_古地図 không có key 1525; không có audit entry nào cho key này)** — trích dẫn sai trong list. Thực tế bẫy lớn hơn nhiều: **61 fix audit** chứa "Jutsu-sen" (toàn bộ đã lật trong đợt này) + 2 fix unification đã gộp.

### T18 — Gloss đầu câu 共通08_傷跡 1485
Gloss %l nằm ở đầu câu ("Túi phi hành đoàn giống như giường ngủ...") — giữ chữ hoa đầu câu: "Túi công tác". Các gloss giữa câu khác dùng "túi công tác" thường theo đúng dạng đã chốt.

### T13 — "Thầy Akai" (list ghi ハチロク15b ×5)
Giá trị hiện tại toàn dự án có **0 dòng** "Thầy Akai" — các dòng đó đã về "đền chủ Akai" trong audit. Chỉ còn 1 dòng "Thầy cúng Akai" (ハチロク15a 2414), đã sửa đợt này.

## 4. Các dòng theo mục (JP / TW / old_vn / fix)

old_vn = giá trị hiện tại (moan fix > audit fix > unification-merged fix > CSV3 VN). Ký hiệu `\\n` trong old_vn/fix là literal backslash-n trong giá trị; ký hiệu `↵` là xuống dòng thật trong giá trị (12 dòng, toàn bộ từ fix audit — xem §6). 5 dòng có old_vn = fix unification đã gộp được ghi rõ nguồn.

### T3. 帝鉄 → "Đường sắt Teitetsu" — 55 dòng

#### れいな02_れいなとポーレット.txt.toml (1 dòng)

**Key 63** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T3)
- JP: 帝都における\\x%l帝鉄;#00ffc040;帝鉄%l;#;勤務も、そこまで過酷なものだったのか\\n――思ってすぐさま、ああ、そうだったかと思いだす。
- TW: \\x%l帝鉄;#00ffc040;帝國鐵路%l;#;明明位於帝都，工作殘酷竟然還如此殘酷——我一瞬間閃過這樣的念頭，然後很快想到了答案。
- old_vn: Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao ——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy.
- fix: Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao ——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy.
- Lý do: Gloss %l của 帝鉄 trong thoại, không phải lần xuất hiện đầu — dạng đầy đủ "Đường sắt Đế quốc" CHỈ dùng ở tooltip lần đầu (共通01 1335, thuộc T4, không đụng); các gloss sau dùng "Đường sắt Teitetsu" (T3).

#### れいな03_しゅっぱつしんこう.txt.toml (1 dòng)

**Key 1659** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T3)
- JP: 「お互い同士に、\\x%l帝鉄;#00ffc040;帝鉄%l;#;までが加わった生存競争は、\\nそれこそ、大廃線直前まで熱く燃え盛っていたんです」
- TW: 「直到大廢線到來之前，各大公司之間都在進行著如火如荼的生存競爭，甚至連\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;都參與其中」
- old_vn: 「Cuộc chiến sinh tồn giữa các công ty với nhau, thậm chí có cả sự tham gia của \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;,\\nthực sự đã bùng cháy dữ dội cho đến tận ngay trước Đại bãi bỏ các tuyến.」
- fix: 「Cuộc chiến sinh tồn giữa các công ty với nhau, thậm chí có cả sự tham gia của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;,\\nthực sự đã bùng cháy dữ dội cho đến tận ngay trước Đại bãi bỏ các tuyến.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### グランドリライト01_オール御一夜、成立ならず.txt.toml (1 dòng)

**Key 2467** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T3)
- JP: 「簡単な話だ。旧帝鉄[こくら,1]粉蔵工場が解体された今、\\n九洲の全ての鉄道会社は、検査に苦労している」
- TW: 「很簡單。前帝國鐵路小倉工廠已經廢棄。現在九州所有的鐵路公司都在頭痛如何進行車輛檢查」
- old_vn: 「Chuyện đơn giản thôi. Giờ đây khi nhà máy Kokura của Đường sắt Hoàng gia cũ đã bị tháo dỡ, tất cả các công ty đường sắt ở Kyushu đều đang khổ sở vì việc kiểm tra.」
- fix: 「Chuyện đơn giản thôi. Giờ đây khi nhà máy Kokura của Đường sắt Teitetsu cũ đã bị tháo dỡ, tất cả các công ty đường sắt ở Kyushu đều đang khổ sở vì việc kiểm tra.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### グランドリライト11_ナインスターズ！.txt.toml (1 dòng)

**Key 3393** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 電源車と冷蔵車とをひとまとめにという日々姫の案は、\\n旧帝鉄の技術を引き継ぐ技師たちによって実現された。
- TW: 基於日日姬將發電車與保溫車合二為一的方案，由繼承了前帝國鐵路技術的技工們親手實現的新車。
- old_vn: Ý tưởng gộp chung toa phát điện và toa đông lạnh làm một của Hibiki,\\nđã được các kỹ sư kế thừa kỹ thuật của Đường sắt Hoàng gia cũ hiện thực hóa.
- fix: Ý tưởng gộp chung toa phát điện và toa đông lạnh làm một của Hibiki,\\nđã được các kỹ sư kế thừa kỹ thuật của Đường sắt Teitetsu cũ hiện thực hóa.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### ハチロク09_採決.txt.toml (1 dòng)

**Key 2792** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T3)
- JP: その頬はワインのせいか、かなり赤らみ、\\n手には、\\x%l帝鉄;#00ffc040;帝鉄%l;#;時代のものと思しき路線地図を持っている。
- TW: 可能是因為葡萄酒的原因，她的臉頰紅得厲害，手上則拿著好像屬於\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;時代的線路地圖。
- old_vn: Có lẽ do rượu vang, hai má cô ấy khá ửng đỏ,\\ntrên tay đang cầm một tấm bản đồ tuyến đường, có vẻ như là từ thời \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;.
- fix: Có lẽ do rượu vang, hai má cô ấy khá ửng đỏ,\\ntrên tay đang cầm một tấm bản đồ tuyến đường, có vẻ như là từ thời \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;.
- Lý do: Gloss %l của 帝鉄 trong thoại, không phải lần xuất hiện đầu — xem ghi chú T3b ở §3.

#### ハチロク16_春.txt.toml (1 dòng)

**Key 2338** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 全線電化。かつての帝鉄が掲げた目標。\\nけれど鉄道を\\x%l保線;#00ffc040;保線%l;#;を知るうち、それは叶わぬ夢だと知った。
- TW: 全線電力化，是曾經的帝國鐵路提出的目標。但是，當我知道鐵路需要\\x%l保線;#00ffc040;巡線%l;#;之後，就明白了那是不可能實現的夢想。
- old_vn: Điện khí hóa toàn tuyến. Mục tiêu mà Đường sắt Hoàng gia từng đề ra.\\nNhưng khi tìm hiểu về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, tôi nhận ra đó là một giấc mơ không thể thành hiện thực.
- fix: Điện khí hóa toàn tuyến. Mục tiêu mà Đường sắt Teitetsu từng đề ra.\\nNhưng khi tìm hiểu về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, tôi nhận ra đó là một giấc mơ không thể thành hiện thực.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### ポーレット01_御一夜探し.txt.toml (1 dòng)

**Key 1912** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T3)
- JP: 「それはもう！　だって永山さん、\\n旧\\x%l帝鉄;#00ffc040;帝鉄%l;#;では食堂車勤務してらしたんですから」
- TW: 「那是當然！　永山女士曾經可是前\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的餐車工作人員呢」
- old_vn: 「Đương nhiên rồi! Bởi vì cô Nagayama,\\ntừng làm việc trên toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ mà.」
- fix: 「Đương nhiên rồi! Bởi vì cô Nagayama,\\ntừng làm việc trên toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; cũ mà.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### ポーレット08_未来へのレール.txt.toml (2 dòng)

**Key 2384** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「この仕様の蒸気機関車は、\\n少なくとも旧帝鉄には存在せんな」
- TW: 「至少前帝國鐵路應該並不存在這種型號」
- old_vn: 「Đầu máy hơi nước có cấu hình này,\\nít nhất là ở Đường sắt Hoàng gia cũ không hề tồn tại」
- fix: 「Đầu máy hơi nước có cấu hình này,\\nít nhất là ở Đường sắt Teitetsu cũ không hề tồn tại」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2777** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 旧帝鉄の貨物機は、D51、D52と、\\nそれぞれの改造機であるD61、D62で終わったはずだ。
- TW: 前帝國鐵路的貨運機車有Ｄ５１型、Ｄ５２型，以及各自的改進型號Ｄ６１型、Ｄ６２型，應該再沒有後續型號了。
- old_vn: Đầu máy chở hàng của Đường sắt Hoàng gia cũ đã kết thúc ở D51, D52,\\nvà các mẫu cải tiến tương ứng là D61, D62.
- fix: Đầu máy chở hàng của Đường sắt Teitetsu cũ đã kết thúc ở D51, D52,\\nvà các mẫu cải tiến tương ứng là D61, D62.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### ポーレット11_記憶と記録.txt.toml (1 dòng)

**Key 1340** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T3)
- JP: 「旧\\x%l帝鉄;#00ffc040;帝鉄%l;#;の最後――最新鋭の試験機の、トップナンバー機。\\nスペック的に余裕がある可能性……低くない気がします」
- TW: 「前\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;最後——最新試驗車型的首車。我覺得在性能方面……很可能還有不少發揮空間」
- old_vn: 「Cỗ máy cuối cùng của \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;# cũ――cỗ máy số 1 của dòng máy thử nghiệm tân tiến nhất.\\nKhả năng vẫn còn dư dả về mặt thông số kỹ thuật……tôi nghĩ là không hề thấp đâu.」
- fix: 「Cỗ máy cuối cùng của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;# cũ――cỗ máy số 1 của dòng máy thử nghiệm tân tiến nhất.\\nKhả năng vẫn còn dư dả về mặt thông số kỹ thuật……tôi nghĩ là không hề thấp đâu.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### ポーレット16_明日へのレール.txt.toml (1 dòng)

**Key 3219** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 無理に絞れば、犠牲になるのは安全性か快適性。\\n\\x%l帝鉄;#00ffc040;帝鉄%l;#;が犯した過ちを、僕らも繰り返すことになる。
- TW: 若強行壓縮人數，所犧牲的就是安全性或可玩性。那樣我們就會重蹈\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的覆轍。
- old_vn: Nếu cố ép cắt giảm, thứ bị hy sinh sẽ là sự an toàn hoặc sự thoải mái.\\nChúng ta sẽ lặp lại sai lầm mà \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; đã mắc phải.
- fix: Nếu cố ép cắt giảm, thứ bị hy sinh sẽ là sự an toàn hoặc sự thoải mái.\\nChúng ta sẽ lặp lại sai lầm mà \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; đã mắc phải.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 仲国02_北琴の鉄道.txt.toml (6 dòng)

**Key 2061** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「都度のランニングコストを抑えることで回収していく。\\n旧帝鉄がかつて目指した、全線電化と同じ発想だな」
- TW: 「以降低單次運行成本的方式回收成本，和前帝國鐵路當年的目標，全線電力化可算是異曲同工了」
- old_vn: 「Bằng cách giảm chi phí vận hành cho mỗi chuyến đi để thu hồi vốn.\\nÝ tưởng này cũng giống hệt với mục tiêu điện khí hóa toàn tuyến mà Đường sắt Hoàng gia từng hướng tới.」
- fix: 「Bằng cách giảm chi phí vận hành cho mỗi chuyến đi để thu hồi vốn.\\nÝ tưởng này cũng giống hệt với mục tiêu điện khí hóa toàn tuyến mà Đường sắt Teitetsu từng hướng tới.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2076** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「けれど同じく感じもします。かつて華やかなりし頃の\\n――皆様の暮らしの一部であった、今は懐かしき帝鉄を」
- TW: 「但也有給人感覺相同的部分。追憶起那繁華的年代，帝國鐵路也是融入人們的生活，成為了其中的一部分」
- old_vn: 「Nhưng tôi cũng cảm thấy có nét tương đồng. Giống như Đường sắt Hoàng gia đầy hoài niệm hiện tại,\\n——vốn từng là một phần trong cuộc sống của mọi người vào thời kỳ hoàng kim trước đây.」
- fix: 「Nhưng tôi cũng cảm thấy có nét tương đồng. Giống như Đường sắt Teitetsu đầy hoài niệm hiện tại,\\n——vốn từng là một phần trong cuộc sống của mọi người vào thời kỳ hoàng kim trước đây.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2114** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「旧帝鉄には無いものですね。特別快速――鉄道が順調に\\n発展していれば、発生した列車種別かもしれませんが」
- TW: 「前帝國鐵路就沒有這個分類，特別快速——這是拜鐵路日新月異的發展所賜，才產生的新的列車類型吧」
- old_vn: 「Là loại tàu không có ở Đường sắt Hoàng gia cũ nhỉ. Đặc biệt nhanh——nếu đường sắt phát triển\\nthuận lợi, thì có lẽ đây là loại tàu đã được sinh ra.」
- fix: 「Là loại tàu không có ở Đường sắt Teitetsu cũ nhỉ. Đặc biệt nhanh——nếu đường sắt phát triển\\nthuận lợi, thì có lẽ đây là loại tàu đã được sinh ra.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2175** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「日ノ本と、帝鉄とは――まったく別の選択をして。\\nまったく別の鉄路が――仲国では伸び、生きたのですね」
- TW: 「和帝國鐵路選擇了完全不同的方向。在仲國生龍活虎地延伸著的，已是和日本完全不同的鐵路了」
- old_vn: 「Hinomoto và Đường sắt Hoàng gia——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」
- fix: 「Hinomoto và Đường sắt Teitetsu——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2994** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 20年前まで、もしも帝鉄が新規車輌開発を続けていたら、\\nいったいどんな列車が産まれていたのであろうか――
- TW: 如果帝國鐵路也能繼續新車輛的開發直到２０年前，又會創造出怎樣的新型列車呢——
- old_vn: Nếu như Đường sắt Hoàng gia vẫn tiếp tục phát triển phương tiện mới cho đến tận 20 năm trước,\\nthì không biết những đoàn tàu như thế nào đã được sinh ra đây——
- fix: Nếu như Đường sắt Teitetsu vẫn tiếp tục phát triển phương tiện mới cho đến tận 20 năm trước,\\nthì không biết những đoàn tàu như thế nào đã được sinh ra đây——
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 3185** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 瞬間、胸のモヤが晴れ――自分自身が、今一瞬、\\n『旧帝鉄』に、嫉妬していたのかと気付かされる。
- TW: 而我心中的不快也隨之一掃而空——這時我才意識到，剛才心中竟對“前帝國鐵路”湧起了一絲嫉妒。
- old_vn: Trong khoảnh khắc, đám mây mù trong ngực tôi tan biến——Tôi nhận ra rằng, trong giây lát vừa rồi,\\nchính bản thân mình đã ghen tị với 『Đường sắt Hoàng gia cũ』.
- fix: Trong khoảnh khắc, đám mây mù trong ngực tôi tan biến——Tôi nhận ra rằng, trong giây lát vừa rồi,\\nchính bản thân mình đã ghen tị với 『Đường sắt Teitetsu cũ』.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 仲国03_北琴鉄道歴史館.txt.toml (15 dòng)

**Key 1585** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「……わたくしが現役でしたころの、最晩年の帝鉄にも。\\nそのような考えと行動が、もし定着しておりましたなら」
- TW: 「……在帝國鐵路最末期，我還在服役的那時候，若是這樣的思考與行動方式，能夠成為規定、標准的話」
- old_vn: 「……Ngay cả trong những năm cuối cùng của Đường sắt Hoàng gia, khi tôi vẫn còn đang hoạt động.\\nNếu như lối suy nghĩ và hành động đó được bám rễ vững chắc thì.」
- fix: 「……Ngay cả trong những năm cuối cùng của Đường sắt Teitetsu, khi tôi vẫn còn đang hoạt động.\\nNếu như lối suy nghĩ và hành động đó được bám rễ vững chắc thì.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1867** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T3)
- JP: 「すごかとね！　ほんなら帝鉄は解体されちゃっても。\\nそれでも名前ば、今も世界中で生きておるとね！」
- TW: 「不得了！要說這帝鐵明明都解散了，但是其名卻還在全世界廣為流傳！」
- old_vn: 「Tuyệt thật đấy! Dù Đường sắt Hoàng gia đã bị giải thể.\\nNhưng cái tên đó, hiện tại vẫn đang tồn tại trên toàn thế giới!」
- fix: 「Tuyệt thật đấy! Dù Đường sắt Teitetsu đã bị giải thể.\\nNhưng cái tên đó, hiện tại vẫn đang tồn tại trên toàn thế giới!」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1872** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「最も、ニイロクと赤井運転士とを見れば。旧帝鉄も\\n解体寸前には、ようやく目覚めてくれたとは分かります」
- TW: 「不過，透過二六和赤井駕駛員就能了解，前帝國鐵路到了臨近解體時，總算是幡然醒悟了」
- old_vn: 「Nhưng, nếu nhìn vào Niiroku và người lái tàu Akai. Tôi hiểu rằng Đường sắt Hoàng gia cũ\\ncuối cùng cũng đã thức tỉnh ngay trước bờ vực giải thể.」
- fix: 「Nhưng, nếu nhìn vào Niiroku và người lái tàu Akai. Tôi hiểu rằng Đường sắt Teitetsu cũ\\ncuối cùng cũng đã thức tỉnh ngay trước bờ vực giải thể.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1906** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T3)
- JP: 「その前の帝鉄が悉究しとった、よかとこだって――\\nハチロクから私達、たーくさん受け取っとるでしょ？」
- TW: 「其實之前的帝國鐵路也有悉究和優點啊——我們也從八六身上學到了很多好的東西不是嗎？」
- old_vn: 「Ngay cả những điểm tốt mà Đường sắt Hoàng gia trước đó đã tất cứu——\\nChúng ta cũng đã nhận được rất nhiều từ Hachiroku mà, đúng không?」
- fix: 「Ngay cả những điểm tốt mà Đường sắt Teitetsu trước đó đã tất cứu——\\nChúng ta cũng đã nhận được rất nhiều từ Hachiroku mà, đúng không?」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1992** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T3)
- JP: 「あ～……その頃の帝鉄って、乗客軽視してたんだっけ？\\n一に特急、ニに急行。三四がなくて五に乗客、とか」
- TW: 「啊～那個時候的帝國鐵路，聽說是很不重視乘客的來著？“特快優先，快速其次，其他讓路，最後乘客”之類」
- old_vn: 「A~…… Đường sắt Hoàng gia thời đó, nghe nói là rất coi thường hành khách phải không?\\nMột là tốc hành đặc biệt, hai là tốc hành. Ba bốn không có, năm mới đến hành khách, kiểu vậy.」
- fix: 「A~…… Đường sắt Teitetsu thời đó, nghe nói là rất coi thường hành khách phải không?\\nMột là tốc hành đặc biệt, hai là tốc hành. Ba bốn không có, năm mới đến hành khách, kiểu vậy.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2027** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「目覚めて以降の帝鉄が重ねてくれた悉究は、\\nニイロクの中に残され、僕らはそれを、受け取れた」
- TW: 「在你醒來之後的現在，帝國鐵路所積累下的悉究，仍然在二六身上發光發熱，而我們則要將它傳承下去」
- old_vn: 「Sự tất cứu mà Đường sắt Hoàng gia đã tích lũy được sau khi thức tỉnh,\\nvẫn còn lưu lại trong Niiroku, và chúng ta đã kế thừa được điều đó.」
- fix: 「Sự tất cứu mà Đường sắt Teitetsu đã tích lũy được sau khi thức tỉnh,\\nvẫn còn lưu lại trong Niiroku, và chúng ta đã kế thừa được điều đó.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2029** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「と、帝鉄では申し伝えられておりました」
- TW: 「在帝鐵是這樣流傳的」
- old_vn: 「Ở Đường sắt Hoàng gia, người ta đã truyền tai nhau như vậy ạ.」
- fix: 「Ở Đường sắt Teitetsu, người ta đã truyền tai nhau như vậy ạ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2081** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「確かに帝鉄は解体された。\\nけれどもそれでも――レールを、僕らは継がせて貰った」
- TW: 「帝國鐵路解體確實是無可挽回了。但即便如此，其軌道確實被我們繼承了下來」
- old_vn: 「Đúng là Đường sắt Hoàng gia đã bị giải thể.\\nNhưng dù vậy——chúng ta đã được kế thừa lại những đường ray đó.」
- fix: 「Đúng là Đường sắt Teitetsu đã bị giải thể.\\nNhưng dù vậy——chúng ta đã được kế thừa lại những đường ray đó.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2082** (nhân vật: 西瓜; nguồn old_vn: csv3; mục: T3)
- JP: 「老師の日ノ本帝有鉄道――帝鉄への接し方は、\\n確かに研究でしたけれど、それだけでなく……ん……」
- TW: 「師父對於帝家日本國鐵路——對於帝國鐵路確實是抱以研究的態度，不過不僅如此……嗯……」
- old_vn: 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」
- fix: 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Teitetsu,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」
- Lý do: JP có cả 日ノ本帝有鉄道 và 帝鉄 trong cùng dòng — chỉ sửa nửa sau (帝鉄); nửa đầu "Đường sắt Đế hữu Hinomoto" là T63 (coordinator đã chốt E1, batch khác).

**Key 2083** (nhân vật: 西瓜; nguồn old_vn: csv3; mục: T3)
- JP: 「老師は、帝鉄を大いにライバル視して研究していました。\\n老師だけでなく、私、西瓜も――仲国国鉄全体も」
- TW: 「師父是將帝國鐵路視為一大勁敵而對其加以研究的。而且不僅是師父，我——西瓜，還有仲國國鐵所有人也都是」
- old_vn: 「Sư phụ đã nghiên cứu Đường sắt Hoàng gia với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」
- fix: 「Sư phụ đã nghiên cứu Đường sắt Teitetsu với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2190** (nhân vật: 志寰; nguồn old_vn: csv3; mục: T3)
- JP: 「そうですね……狭軌では速度積載量ともに限界があると\\n帝鉄が示してくれた影響も、あったかもしれません」
- TW: 「是啊……帝國鐵路所展現出的窄軌在速度和承重上的局限性，可能確實是促使我國採用標準軌的原因之一」
- old_vn: 「Đúng vậy nhỉ…… Có lẽ cũng có ảnh hưởng từ việc Đường sắt Hoàng gia\\nđã cho thấy khổ hẹp có giới hạn về cả tốc độ lẫn tải trọng.」
- fix: 「Đúng vậy nhỉ…… Có lẽ cũng có ảnh hưởng từ việc Đường sắt Teitetsu\\nđã cho thấy khổ hẹp có giới hạn về cả tốc độ lẫn tải trọng.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2251** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「かつての帝鉄は――少なくとも仲国国鉄の創設期には、\\nライバル視されるに足る存在であったのか」
- TW: 「當年的帝國鐵路——至少在仲國國鐵創設之初，絕對是一個值得被視為勁敵的存在」
- old_vn: 「Đường sắt Hoàng gia ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」
- fix: 「Đường sắt Teitetsu ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2301** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T3)
- JP: 「ゆーたらナインスターズだって、古きよき帝鉄と、\\n帝鉄が最後に夢見た未来とを、繋ぎあわせたものやけん」
- TW: 「而通過九星這一媒介，帝國鐵路構建的良好傳統，與帝國鐵路最終在夢中所勾勒的未來，也聯繫在了一起」
- old_vn: 「Nói cách khác, ngay cả Nine Stars, cũng là thứ kết nối giữa Đường sắt Hoàng gia tốt đẹp xưa cũ,\\nvà tương lai mà Đường sắt Hoàng gia đã mơ ước vào những giây phút cuối cùng.」
- fix: 「Nói cách khác, ngay cả Nine Stars, cũng là thứ kết nối giữa Đường sắt Teitetsu tốt đẹp xưa cũ,\\nvà tương lai mà Đường sắt Teitetsu đã mơ ước vào những giây phút cuối cùng.」
- Lý do: JP chứa 帝鉄 ×2 — thay cả 2 chỗ.

**Key 2315** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「失礼でなければ、もうひとつ聞かせてほしい。\\n志寰君のご父君は、何故そこまで詳細に帝鉄の分析を」
- TW: 「若不介意，我還想再問一個問題。志寰，不知令尊為何會如此詳細地分析帝國鐵路呢？」
- old_vn: 「Nếu không phiền, tôi muốn hỏi thêm một điều nữa.\\nTại sao cha của Zhihuan lại phân tích chi tiết về Đường sắt Hoàng gia đến vậy?」
- fix: 「Nếu không phiền, tôi muốn hỏi thêm một điều nữa.\\nTại sao cha của Zhihuan lại phân tích chi tiết về Đường sắt Teitetsu đến vậy?」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2860** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 西瓜と志寰君の日ノ本語の上手さ、\\n加え、帝鉄史にまで及ぶ知識の広範さから類推するに――
- TW: 而西瓜與志寰的日語如此流利，知識範圍更是廣到對帝國鐵路的歷史都了如指掌，如此想來——
- old_vn: Từ sự thành thạo tiếng Hinomoto của Suika và Zhihuan,\\ncộng thêm kiến thức sâu rộng bao quát cả lịch sử Đường sắt Hoàng gia, có thể suy ra——
- fix: Từ sự thành thạo tiếng Hinomoto của Suika và Zhihuan,\\ncộng thêm kiến thức sâu rộng bao quát cả lịch sử Đường sắt Teitetsu, có thể suy ra——
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 仲国04_z49列車.txt.toml (1 dòng)

**Key 2007** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「それに、寝台客車は……わたくし、帝鉄時代には、\\n牽引したことさえございませんでしたので」
- TW: 「而且要說臥鋪車的話……至少我在帝國鐵路時代連掛接過的經歷都沒有」
- old_vn: 「Hơn nữa, toa khách giường nằm thì…… vào thời Đường sắt Hoàng gia,\\ntôi thậm chí còn chưa từng kéo chúng bao giờ.」
- fix: 「Hơn nữa, toa khách giường nằm thì…… vào thời Đường sắt Teitetsu,\\ntôi thậm chí còn chưa từng kéo chúng bao giờ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 仲国06_聖都とパンダとハチロクと.txt.toml (2 dòng)

**Key 1821** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「はい。急勾配を持つ難所です。帝鉄全盛期には、\\n\\x%l補機;#00ffc040;補機%l;#;の回送のためだけの迂回線が設けられたほどの」
- TW: 「是的。那裡有著頗難行駛的陡坡。當年帝國鐵路全盛時期，還在那邊鋪設了專門用於\\x%l補機;#00ffc040;補機%l;#;回送的迂迴線路」
- old_vn: 「Vâng. Đó là một khu vực hiểm trở với độ dốc lớn. Thời kỳ hoàng kim của Đường sắt Hoàng gia,\\nhọ thậm chí còn thiết lập cả một tuyến đường vòng chỉ dành riêng cho việc đưa \\x%l補機;#00ffc040;đầu máy phụ%l;#; về.」
- fix: 「Vâng. Đó là một khu vực hiểm trở với độ dốc lớn. Thời kỳ hoàng kim của Đường sắt Teitetsu,\\nhọ thậm chí còn thiết lập cả một tuyến đường vòng chỉ dành riêng cho việc đưa \\x%l補機;#00ffc040;đầu máy phụ%l;#; về.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2347** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 右田は酒造だ。ペットは飼えん。帝鉄時代はそれこそ、\\n動物と接する機会すらなかったろうし……
- TW: 右田家是釀酒廠，當然也沒有養寵物。帝國鐵路時代的話，想來也沒什麼與動物接觸的機會吧……
- old_vn: Nhà Migita là xưởng nấu rượu. Không thể nuôi thú cưng được. Hồi ở Đường sắt Hoàng gia,\\nchắc chắn em ấy cũng chẳng có cơ hội tiếp xúc với động vật……
- fix: Nhà Migita là xưởng nấu rượu. Không thể nuôi thú cưng được. Hồi ở Đường sắt Teitetsu,\\nchắc chắn em ấy cũng chẳng có cơ hội tiếp xúc với động vật……
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫01_双鉄の妹.txt.toml (1 dòng)

**Key 2097** (nhân vật: 永山; nguồn old_vn: audit fix; mục: T3)
- JP: 「いい勘ね。大正解。ハチクマライスは、\\n旧\\x%l帝鉄;#00ffc040;帝鉄%l;#;の食堂車厨房の[まかな]賄い[めし]飯が元祖なの」
- TW: 「你的第六感不錯。完全正確。蜂熊套餐可是起源自前\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;餐車廚房裡的工作餐哦」
- old_vn: 「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; cũ mà.」
- fix: 「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; cũ mà.」
- Lý do: Gloss %l của 帝鉄 trong thoại, không phải lần xuất hiện đầu — xem ghi chú T3b ở §3.

#### 日々姫02_文庫森.txt.toml (6 dòng)

**Key 1242** (nhân vật: 木本; nguồn old_vn: csv3; mục: T3)
- JP: 「……帝鉄の始まりは、私設鉄道の買収からだった。\\nゆー話は、ご存知ですかの」
- TW: 「……要說帝國鐵路當初，其實是從收購私營鐵路起家的。這事你們都知道吧」
- old_vn: 「...Sự khởi đầu của Đường sắt Hoàng gia là từ việc thu mua các tuyến đường sắt tư nhân.\\nChuyện này, hai người có biết không?」
- fix: 「...Sự khởi đầu của Đường sắt Teitetsu là từ việc thu mua các tuyến đường sắt tư nhân.\\nChuyện này, hai người có biết không?」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1570** (nhân vật: 木本; nguồn old_vn: csv3; mục: T3)
- JP: 「全盛期……ゆーのは、昔の……\\n[ていてつ,1]帝鉄以前の来大鉄道についてのことですかの」
- TW: 「你說的……全盛期……是指帝國鐵路之前的久大鐵路嗎？」
- old_vn: 「Thời kỳ hoàng kim... ý cô là, ngày xưa...\\nLà về Đường sắt Kyudai thời trước \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; sao?」
- fix: 「Thời kỳ hoàng kim... ý cô là, ngày xưa...\\nLà về Đường sắt Kyudai thời trước \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; sao?」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1655** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T3)
- JP: 「ほう。帝鉄発足前――\\n私設鉄道の時代からのものだったのですか」
- TW: 「哦。帝國鐵路成立之前，原來是從私營鐵路的時代一路走來的嗎」
- old_vn: 「Chà. Từ trước khi Đường sắt Hoàng gia ra đời——\\nTừ thời đại đường sắt tư nhân sao.」
- fix: 「Chà. Từ trước khi Đường sắt Teitetsu ra đời——\\nTừ thời đại đường sắt tư nhân sao.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1869** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T3)
- JP: 「はい。それも含めて……もしお差し支えなければ、\\n帝鉄時代の思い出とか、廃線後のこととかも」
- TW: 「是的。也包括那個……如果您不介意的話，我也想聽聽有關帝國鐵路時代的回憶，以及廢線之後的事」
- old_vn: 「Vâng. Bao gồm cả khoảng thời gian đó... nếu ông không phiền,\\ncả những kỷ niệm thời Đường sắt Hoàng gia, hay sau khi bãi bỏ tuyến nữa ạ.」
- fix: 「Vâng. Bao gồm cả khoảng thời gian đó... nếu ông không phiền,\\ncả những kỷ niệm thời Đường sắt Teitetsu, hay sau khi bãi bỏ tuyến nữa ạ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1954** (nhân vật: 木本; nguồn old_vn: csv3; mục: T3)
- JP: 「帝鉄に強制買収されて、法に縛られるようになりました。\\n経営の[なん]何もかんも自由にできんようなったとですよ」
- TW: 「被帝國鐵路強制收購後，這裡開始受到法律的束縛。經營在各方各面都遭受了限制」
- old_vn: 「Bị Đường sắt Hoàng gia cưỡng chế thu mua, và bị ràng buộc bởi pháp luật.\\nMọi thứ trong kinh doanh đều không thể tự do làm theo ý mình nữa.」
- fix: 「Bị Đường sắt Teitetsu cưỡng chế thu mua, và bị ràng buộc bởi pháp luật.\\nMọi thứ trong kinh doanh đều không thể tự do làm theo ý mình nữa.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2544** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: れいなの\\x%lキハ07s;#00ffc040;キハ07s%l;#;は、\\x%l硬上鉱山鉄道;#00ffc040;硬上鉱山鉄道%l;#;専用に作られた、\\n帝鉄キハ07の同形機と聞く。
- TW: 聽說玲奈的\\x%lキハ07s;#00ffc040;Ｋｉｈａ０７Ｓ%l;#;是專為\\x%l硬上鉱山鉄道;#00ffc040;片上礦山鐵路%l;#;生產的與帝國鐵路\\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;是同型車。
- old_vn: Nghe nói \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; của Reina là mẫu xe cùng kiểu với KiHa 07 của Đường sắt Hoàng gia,\\nđược chế tạo riêng cho \\x%l硬上鉱山鉄道;#00ffc040;Đường sắt mỏ Katakami%l;#;.
- fix: Nghe nói \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; của Reina là mẫu xe cùng kiểu với KiHa 07 của Đường sắt Teitetsu,\\nđược chế tạo riêng cho \\x%l硬上鉱山鉄道;#00ffc040;Đường sắt mỏ Katakami%l;#;.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫03_湯富院.txt.toml (1 dòng)

**Key 1826** (nhân vật: みくろ; nguồn old_vn: audit fix; mục: T3)
- JP: 「いいえ、みくろは、\\n旧帝鉄[はちろくにいまるけい,4]8620形蒸気機関車、[さんはちろくきゅうろく,4]38696のレイルロオドです」
- TW: 「不，美玖路是前帝國鐵路[八六二零,3]８６２０型蒸汽機車，[三八六九六,4]３８６９６的鐵路人偶」
- old_vn: 「Không phải ạ, Mikuro là,↵Railord của đầu máy hơi nước loại 8620, số hiệu 38696 thuộc Đường sắt Hoàng gia cũ ạ.」
- fix: 「Không phải ạ, Mikuro là,↵Railord của đầu máy hơi nước loại 8620, số hiệu 38696 thuộc Đường sắt Teitetsu cũ ạ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫06_みくろ、来訪.txt.toml (1 dòng)

**Key 3128** (nhân vật: monologue; nguồn old_vn: csv3; mục: T3)
- JP: 旧帝鉄型レイルロオドゆえの世間知らずさも残りはするが、\\n動物園で、よい経験を積ませてもらってきたのだろう。
- TW: 雖然像其他前帝國鐵路鐵路人偶一樣，還有些不諳世事，但她在動物園應該也積累了不少很棒的經驗。
- old_vn: Tuy vẫn còn chút ngây ngô với sự đời của một Railord kiểu Đường sắt Hoàng gia cũ,\\nnhưng chắc hẳn con bé đã tích lũy được nhiều kinh nghiệm quý báu ở sở thú.
- fix: Tuy vẫn còn chút ngây ngô với sự đời của một Railord kiểu Đường sắt Teitetsu cũ,\\nnhưng chắc hẳn con bé đã tích lũy được nhiều kinh nghiệm quý báu ở sở thú.
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫07_たったひとりの宣戦布告.txt.toml (1 dòng)

**Key 1629** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「いいえ？　実際あったのです。\\nわたくしの\\x%l帝鉄;#00ffc040;帝鉄%l;#;時代、帝央\\x%l保線;#00ffc040;保線%l;#;区の\\x%l保線;#00ffc040;保線%l;#;夫さんが」
- TW: 「不哦。實際就有人得過。在\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;時期，帝都中央車站\\x%l保線;#00ffc040;巡線%l;#;區的\\x%l保線;#00ffc040;巡線%l;#;員就得過」
- old_vn: 「Không đâu? Thực tế là có chuyện đó đấy ạ.\\nHồi em còn ở \\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;, một nhân viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#; ở khu \\x%l保線;#00ffc040;bảo trì%l;#; Teio đã bị...」
- fix: 「Không đâu? Thực tế là có chuyện đó đấy ạ.\\nHồi em còn ở \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;, một nhân viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#; ở khu \\x%l保線;#00ffc040;bảo trì%l;#; Teio đã bị...」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫09_run_with_our_dreams.txt.toml (4 dòng)

**Key 1687** (nhân vật: みくろ; nguồn old_vn: csv3; mục: T3)
- JP: 「なんにもない、帝鉄時代の最末期みたいなホームと、\\nわざと古ぼけさせてるホテルと、すごくマッチしてて」
- TW: 「像帝國鐵路時代最末期一樣空空如也的站台，與古樸森然的旅館非常搭調」
- old_vn: 「Một sân ga trống trơn giống hệt như thời kỳ cuối của Đường sắt Hoàng gia,\\nkết hợp với một khách sạn được cố tình làm cho cũ kỹ, thật sự rất ăn khớp với nhau.」
- fix: 「Một sân ga trống trơn giống hệt như thời kỳ cuối của Đường sắt Teitetsu,\\nkết hợp với một khách sạn được cố tình làm cho cũ kỹ, thật sự rất ăn khớp với nhau.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 1906** (nhân vật: ハチロク; nguồn old_vn: unif (đợt unification đã gộp); mục: T3)
- JP: 「旧帝鉄8620形蒸気機関車トップナンバーレイルロオド。\\n現、御一夜鉄道の、ハチロクです」
- TW: 「我是前帝國鐵路８６２０型蒸汽機車首車鐵路人偶。現隸屬於御一夜鐵路，名叫八六」
- old_vn: 「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Hoàng gia cũ.\\nHiện tại thuộc Đường sắt Ohitoyo, Hachiroku ạ.」
- fix: 「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Teitetsu cũ.\\nHiện tại thuộc Đường sắt Ohitoyo, Hachiroku ạ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2046** (nhân vật: みくろ; nguồn old_vn: csv3; mục: T3)
- JP: 「旧帝鉄8620形38696号蒸気機関車レイルロオド、\\nみくろです」
- TW: 「美玖路是前帝國鐵路８６２０型３８６９６號蒸汽機車鐵路人偶，名叫美玖路」
- old_vn: 「Railord của đầu máy hơi nước 38696 thuộc dòng 8620 Đường sắt Hoàng gia cũ,\\nMikuro ạ.」
- fix: 「Railord của đầu máy hơi nước 38696 thuộc dòng 8620 Đường sắt Teitetsu cũ,\\nMikuro ạ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

**Key 2095** (nhân vật: みくろ; nguồn old_vn: csv3; mục: T3)
- JP: 「温泉の湯気越しに見るD51が、蒸気を吐いてるみたいで。\\nまるで、帝鉄時代からずっと走り続けてきたみたいで」
- TW: 「透過溫泉的水氣所看到的Ｄ５１彷彿在噴吐著蒸汽。整輛列車就像從帝國鐵路時代一路行駛到了現在」
- old_vn: 「D51 nhìn qua làn hơi nước của suối nước nóng, trông cứ như đang nhả hơi nước vậy.\\nCứ như thể nó vẫn luôn chạy không ngừng nghỉ từ thời Đường sắt Hoàng gia đến giờ.」
- fix: 「D51 nhìn qua làn hơi nước của suối nước nóng, trông cứ như đang nhả hơi nước vậy.\\nCứ như thể nó vẫn luôn chạy không ngừng nghỉ từ thời Đường sắt Teitetsu đến giờ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml (1 dòng)

**Key 2495** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「模型の中では、\\n\\x%l帝鉄;#00ffc040;帝鉄%l;#;の描いた理想の未来が実現したのですね」
- TW: 「在這座模型裡倒是實現了\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;所描繪的理想未來呢」
- old_vn: 「Bên trong mô hình này,\\\\ntương lai lý tưởng mà \\\\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; vẽ ra đã trở thành hiện thực nhỉ.」
- fix: 「Bên trong mô hình này,\\\\ntương lai lý tưởng mà \\\\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; vẽ ra đã trở thành hiện thực nhỉ.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫11_御一夜モザイク.txt.toml (1 dòng)

**Key 2141** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T3)
- JP: 「もちろんです。\\x%l大詔;#00ffc040;大詔%l;#;時代の\\x%l帝鉄;#00ffc040;帝鉄%l;#;を駆け抜けた、\\n代表的な\\x%l客車;#00ffc040;客車%l;#;ですから」
- TW: 「當然了。它是在大正時代縱橫於\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的代表性\\x%l客車;#00ffc040;客運車廂%l;#;」
- old_vn: 「Tất nhiên rồi ạ. Nó là \\\\x%l客車;#00ffc040;toa hành khách%l;#; tiêu biểu\\\\ntừng rong ruổi trên tuyến \\\\x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; thời \\\\x%l大詔;#00ffc040;Đại Chiếu%l;#; mà.」
- fix: 「Tất nhiên rồi ạ. Nó là \\\\x%l客車;#00ffc040;toa hành khách%l;#; tiêu biểu\\\\ntừng rong ruổi trên tuyến \\\\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; thời \\\\x%l大詔;#00ffc040;Đại Chiếu%l;#; mà.」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

#### 日々姫14_投開票.txt.toml (1 dòng)

**Key 1276** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T3)
- JP: 「\\x%l帝鉄;#00ffc040;帝鉄%l;#;[にまんにせんけいかい,6]22000系改、御一夜\\x%l22形;#00ffc040;[ニイニイ,1]22系%l;#;1号\\x%l客車;#00ffc040;客車%l;#;、\\n\\x%lイロ;#00ffc040;ナイロ[ニイニイイチ,2]221%l;#;改修の全工程は、終了しました」
- TW: 「\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;２２０００型改、御一夜\\x%l22形;#00ffc040;２２型%l;#;１號\\x%l客車;#00ffc040;客運車廂%l;#;、\\x%lナイロ221;#00ffc040;Ｎａｉｒｏ２２１%l;#;的修復工程全部結束了」
- old_vn: 「Toa \\x%l客車;#00ffc040;hành khách%l;#; số 1 Ohitoyo \\x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;,\\ntoàn bộ quá trình cải tạo \\x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」
- fix: 「Toa \\x%l客車;#00ffc040;hành khách%l;#; số 1 Ohitoyo \\x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;,\\ntoàn bộ quá trình cải tạo \\x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」
- Lý do: Gloss %l của 帝鉄 trong thoại, không phải lần xuất hiện đầu — xem ghi chú T3b ở §3.

#### 真闇01_再蒸留.txt.toml (1 dòng)

**Key 1621** (nhân vật: ハチロク; nguồn old_vn: audit fix; mục: T3)
- JP: 「\\x%l正和;#00ffc040;正和%l;#;四十二年は、\\x%l帝鉄;#00ffc040;帝鉄%l;#;解体の年です。ともない、恐らく、\\n隈元でも、大廃線が一気に進んだのでしょう」
- TW: 「正和四十二年是\\x%l帝鉄;#00ffc040;帝國鐵路%l;#;解體的那一年。隨之而來的就是大廢線，恐怕隈元也一口氣廢了很多吧」
- old_vn: 「Năm \\x%l正和;#00ffc040;Showa%l;#; thứ 42 là năm \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#; giải thể. Cùng với đó, có lẽ \\nở Kumamoto, đại bãi bỏ các tuyến đường sắt cũng đã diễn ra đồng loạt.」
- fix: 「Năm \\x%l正和;#00ffc040;Showa%l;#; thứ 42 là năm \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; giải thể. Cùng với đó, có lẽ \\nở Kumamoto, đại bãi bỏ các tuyến đường sắt cũng đã diễn ra đồng loạt.」
- Lý do: Gloss %l của 帝鉄 trong thoại, không phải lần xuất hiện đầu — xem ghi chú T3b ở §3.

#### 稀咲h3_チャイナドレスでおもてなし.txt.toml (2 dòng)

**Key 2547** (nhân vật: 稀咲; nguồn old_vn: csv3; mục: T3)
- JP: 「それだけで、ボクらの会社――\\n帝鉄線路合同会社の評価と信頼は、大きく高まる」
- TW: 「正說明我們的公司――帝國鐵路有限公司受到了多高的評價、多大的信任」
- old_vn: 「Chỉ nội điều đó thôi, đánh giá và sự tin tưởng dành cho công ty của chúng ta――\\nCông ty TNHH Đường sắt Hoàng gia, đã tăng lên đáng kể rồi」
- fix: 「Chỉ nội điều đó thôi, đánh giá và sự tin tưởng dành cho công ty của chúng ta――\\nCông ty TNHH Đường sắt Teitetsu, đã tăng lên đáng kể rồi」
- Lý do: JP 帝鉄線路合同会社 vs TW 帝國鐵路有限公司 — JP thắng TW → "Công ty TNHH Đường sắt Teitetsu".

**Key 2740** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T3)
- JP: 「御一夜とも右田とも宝生とも縁もゆかりもなかった、\\n旧帝鉄総裁を仲人にまで引っ張ってくださったのだ」
- TW: 「連和御一夜、和右田、和寶生都沒有任何來往的舊帝鐵總裁，都肯當我們的媒人了」
- old_vn: 「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Hoàng gia,\\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」
- fix: 「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Teitetsu,\\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」
- Lý do: JP chứa 帝鉄 → "Đường sắt Hoàng gia" sai, "Đường sắt Teitetsu" đúng (T3, quyết 19/11, Hieu).

### T10. 電車姫 → "Công chúa Tàu điện" — 28 dòng

#### lrれいな追加03_れいなとのレール.txt.toml (1 dòng)

**Key 1170** (nhân vật: れいな; nguồn old_vn: csv3; mục: T10)
- JP: 「[さんよう,1]讃陽か[さんいん,1]讃陰。どっちかの線路もつながなくちゃですねぇ。\\nそれで廣島までいけば、電車姫さまの線路があるから」
- TW: 「山陽或者山陰，線路必須連接到這兩地之一才行。然後再能通向廣島的話，那裡就有電車公主的線路了」
- old_vn: 「San'yo hoặc San'in. Phải nối với một trong hai tuyến đó nha~.\\nRồi đi đến Hiroshima, vì ở đó có đường sắt của công chúa Densha mà.」
- fix: 「San'yo hoặc San'in. Phải nối với một trong hai tuyến đó nha~.\\nRồi đi đến Hiroshima, vì ở đó có đường sắt của Công chúa Tàu điện mà.」
- Lý do: JP 電車姫さまの線路 — VN cũ "đường sắt của công chúa Densha" (dạng lai) → "đường sắt của Công chúa Tàu điện".

#### グランドリライト01_オール御一夜、成立ならず.txt.toml (1 dòng)

**Key 2724** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T10)
- JP: 「はい、だから、四年に一度、派遣してもらうんです。\\n電車姫様――[ひろしま,1]廣島毛利電鉄さんのコネで、技師さんを」
- TW: 「是的，所以我們會每四年一次利用人脈，由廣島毛利電鐵電車公主殿下牽頭請技工來這邊」
- old_vn: 「Vâng, vì vậy, cứ bốn năm một lần, chúng tôi lại nhờ họ phái người đến. Công chúa Xe điện——nhờ mối quan hệ của Đường sắt điện Hiroshima Mouri, để mời kỹ sư đến.」
- fix: 「Vâng, vì vậy, cứ bốn năm một lần, chúng tôi lại nhờ họ phái người đến. Công chúa Tàu điện——nhờ mối quan hệ của Đường sắt điện Hiroshima Mouri, để mời kỹ sư đến.」
- Lý do: Dạng cũ là "Công chúa Xe điện" — T10 cấm mọi dạng khác ("Điện xá Công chúa"/"Công chúa Xe điện"/"Điện Xa Cơ"/"Densha Hime").

#### グランドリライト04_ポーレット.txt.toml (1 dòng)

**Key 2117** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T10)
- JP: 「ああ。廣島に電車姫様という方がいらっしゃるのだが、\\nこの方が運転台通信をいたく気に入ってくれてな」
- TW: 「是啊。廣島有一位叫電車公主的人，她特別喜歡駕駛台通信」
- old_vn: 「Ừ. Ở Hiroshima có một người tên là Denshahime,\\ncô ấy rất thích Bản tin buồng lái này.」
- fix: 「Ừ. Ở Hiroshima có một người tên là Công chúa Tàu điện,\\ncô ấy rất thích Bản tin buồng lái này.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### グランドリライト08_ふかみ.txt.toml (1 dòng)

**Key 2086** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T10)
- JP: 「なるほど。それは妙案だな。では、参加各事業者に\\nこころあたりを訪ね、ダメなら電車姫様にも相談しよう」
- TW: 「有道理，這是個好辦法。那就詢問一下參與計劃的相關公司，實在不行就去問問電車公主殿下」
- old_vn: 「Ra vậy. Đúng là một ý kiến hay. Vậy thì, anh sẽ hỏi thử các công ty\\ntham gia xem có biết chỗ nào không, nếu không được thì nhờ ngài Denshahime tư vấn vậy.」
- fix: 「Ra vậy. Đúng là một ý kiến hay. Vậy thì, anh sẽ hỏi thử các công ty\\ntham gia xem có biết chỗ nào không, nếu không được thì nhờ ngài Công chúa Tàu điện tư vấn vậy.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### ハチロク11_御一夜鉄道小畑線.txt.toml (5 dòng)

**Key 1661** (nhân vật: れいな; nguồn old_vn: csv3; mục: T10)
- JP: 「だって、それってぇ、もう電車姫さまから\\n聞いたことがあるお話と、中味はおんなじですよねぇ」
- TW: 「你看哦，剛才這些話，和之前電車公主殿下說的話內在含義其實是一樣的吧」
- old_vn: 「Bởi vì, chuyện đó, giống y hệt như chuyện \\nReina đã từng nghe từ ngài Denshahime mà.」
- fix: 「Bởi vì, chuyện đó, giống y hệt như chuyện \\nReina đã từng nghe từ ngài Công chúa Tàu điện mà.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1919** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T10)
- JP: 「電車姫様がおっしゃっていた、ロオドコアか！\\nロオドコアの再精錬というのが、つまり」
- TW: 「就是電車公主和我們說起過的人偶核啊！而人偶核的二次提取，也就是……」
- old_vn: 「Là Lõi Lord mà ngài Denshahime đã nói đến sao! \\nViệc tinh luyện lại Lõi Lord, tức là」
- fix: 「Là Lõi Lord mà ngài Công chúa Tàu điện đã nói đến sao! \\nViệc tinh luyện lại Lõi Lord, tức là」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1955** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T10)
- JP: 「だと思う。既にたどり着いてるアプローチかとも思うが、\\n不死鳥博士と電車姫様にもお伝えして損はなかろう」
- TW: 「我也這樣覺得。既然大家都對此有了共識，那不妨把這些想法也告知不死鳥博士和電車公主殿下吧」
- old_vn: 「Tôi nghĩ vậy. Dù có thể đây là cách tiếp cận mà họ đã nghĩ đến rồi, \\nnhưng báo cho Tiến sĩ Fushichou và ngài Denshahime biết cũng không thừa.」
- fix: 「Tôi nghĩ vậy. Dù có thể đây là cách tiếp cận mà họ đã nghĩ đến rồi, \\nnhưng báo cho Tiến sĩ Fushichou và ngài Công chúa Tàu điện biết cũng không thừa.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2251** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T10)
- JP: 「電車姫様がおっしゃっていた――\\n『\\x%lタブレット;#00ffc040;タブレット%l;#;からの、ロオドコアの再精錬』」
- TW: 「電車公主殿下所說的——“由\\x%lタブレット;#00ffc040;操作板%l;#;二次提取人偶核”」
- old_vn: 「Ngài Denshahime đã nói—— \\n'Việc tinh luyện lại Lõi Lord từ \\x%lタブレット;#00ffc040;Tablet%l;#;'」
- fix: 「Ngài Công chúa Tàu điện đã nói—— \\n'Việc tinh luyện lại Lõi Lord từ \\x%lタブレット;#00ffc040;Tablet%l;#;'」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2253** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T10)
- JP: 「電車姫様から？」
- TW: 「電車公主殿下？」
- old_vn: 「Từ ngài Denshahime sao?」
- fix: 「Từ ngài Công chúa Tàu điện sao?」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### ハチロク13_実りの秋.txt.toml (1 dòng)

**Key 2472** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: 不死鳥博士・電車姫様・登呂流湯さんの\\n相互協力体制が、ちょうど生まれたあの時期だ。
- TW: 不死鳥博士、電車公主殿下、登呂流浴場老闆三方之間，建立起相互協助的合作體制的時候。
- old_vn: Chính là lúc hệ thống hợp tác tương trợ giữa Tiến sĩ Fushicho,\\nDenshahime và ông chủ nhà tắm Tororyu-yu được hình thành.
- fix: Chính là lúc hệ thống hợp tác tương trợ giữa Tiến sĩ Fushicho,\\nCông chúa Tàu điện và ông chủ nhà tắm Tororyu-yu được hình thành.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### ハチロク16_春.txt.toml (3 dòng)

**Key 2692** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: 小気味よいほどの即答に、電車姫様が笑顔を浮かべる。\\n口元を扇子で隠さぬままに、ニコニコされる。
- TW: 聽到小玉立刻回答，電車公主殿下面露喜色——儘管那笑容仍半掩在她手中的扇子之下。
- old_vn: Trước câu trả lời nhanh gọn và dứt khoát ấy, Densha Hime mỉm cười.\\nCô ấy cười rạng rỡ mà không hề dùng quạt che miệng.
- fix: Trước câu trả lời nhanh gọn và dứt khoát ấy, Công chúa Tàu điện mỉm cười.\\nCô ấy cười rạng rỡ mà không hề dùng quạt che miệng.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2706** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: ディスプレイには、電車姫様。
- TW: 螢幕上現出了電車公主殿下的身影。
- old_vn: Trên màn hình hiển thị là Densha Hime.
- fix: Trên màn hình hiển thị là Công chúa Tàu điện.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2790** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: 電車姫様が扇子を広げる。\\nその口元を覆い隠して、くふふと喉の奥で笑う。
- TW: 電車公主殿下打開扇子，輕掩唇齒，隱撥銀鈴。
- old_vn: Densha Hime mở chiếc quạt giấy ra.\\nChe khuất khóe miệng, cô ấy cười khúc khích trong cổ họng.
- fix: Công chúa Tàu điện mở chiếc quạt giấy ra.\\nChe khuất khóe miệng, cô ấy cười khúc khích trong cổ họng.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### ポーレット09_ストーブ客車.txt.toml (8 dòng)

**Key 1837** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「電車姫様の保存車輌ですから、いい状態だと思います。\\nけど、あの方はＳＬには詳しくないとも思いますから」
- TW: 「因為是電車公主保存的車廂，所以我想狀態應該不會差。不過，我覺得她似乎不太了解蒸汽機車」
- old_vn: 「Vì là xe được Densha Hime bảo quản, nên em nghĩ tình trạng vẫn còn tốt.\\nNhưng mà, em cũng nghĩ cô ấy không am hiểu lắm về SL đâu ạ.」
- fix: 「Vì là xe được Công chúa Tàu điện bảo quản, nên em nghĩ tình trạng vẫn còn tốt.\\nNhưng mà, em cũng nghĩ cô ấy không am hiểu lắm về SL đâu ạ.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1839** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「ちょっと珍しい\\x%l客車;#00ffc040;客車%l;#;だからです。\\n廃棄処分になるところを、電車姫様が買い取って」
- TW: 「因為那節\\x%l客車;#00ffc040;客運車廂%l;#;有些罕見。原本即將被廢棄處理的時候被電車公主買下了」
- old_vn: 「Bởi vì đó là một \\x%l客車;#00ffc040;toa hành khách%l;#; khá hiếm ạ.\\nLúc sắp bị mang đi tiêu hủy thì đã được Densha Hime mua lại.」
- fix: 「Bởi vì đó là một \\x%l客車;#00ffc040;toa hành khách%l;#; khá hiếm ạ.\\nLúc sắp bị mang đi tiêu hủy thì đã được Công chúa Tàu điện mua lại.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1938** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「これを電車姫様にお見せしたら、興味を持って下さって。\\nそれで、マイントレジャー計画についてもお話しして」
- TW: 「我把這張照片給電車公主看了，她表示非常感興趣。於是我把煤探樂園的計劃也跟她說了——」
- old_vn: 「Khi em cho Densha Hime xem bức ảnh này, cô ấy đã rất hứng thú.\\nSau đó, em cũng đã nói chuyện với cô ấy về kế hoạch Mine Treasure.」
- fix: 「Khi em cho Công chúa Tàu điện xem bức ảnh này, cô ấy đã rất hứng thú.\\nSau đó, em cũng đã nói chuyện với cô ấy về kế hoạch Mine Treasure.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2129** (nhân vật: 双鉄; nguồn old_vn: unif (đợt unification đã gộp); mục: T10)
- JP: 「トコロテン方式で不要になった旧\\x%l客車;#00ffc040;客車%l;#;を、\\n電車姫様が引き取って保存していた――ということか」
- TW: 「而淘汰掉的舊\\x%l客車;#00ffc040;客運車廂%l;#;就被電車公主接手並保存起來了嗎」
- old_vn: 「Ý em là, \\x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\\nđã được Densha Hime nhận về và bảo quản――đúng không?」
- fix: 「Ý em là, \\x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\\nđã được Công chúa Tàu điện nhận về và bảo quản――đúng không?」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2137** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「鉄道を好きになってくれる人が増えれば、\\nそれは、電車姫様にも嬉しいことだから、って」
- TW: 「能有更多的人喜歡上鐵路，想必電車公主也會很高興的」
- old_vn: 「Nếu số người yêu thích đường sắt tăng lên,\\nthì điều đó, cũng là niềm vui đối với Densha Hime mà, cô ấy nói vậy.」
- fix: 「Nếu số người yêu thích đường sắt tăng lên,\\nthì điều đó, cũng là niềm vui đối với Công chúa Tàu điện mà, cô ấy nói vậy.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2262** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T10)
- JP: 「電車姫――とは、確か、\\n廣島の毛利電鉄のオーナーのことだったか」
- TW: 「電車公主——我記得是廣島毛利電鐵的所有者吧」
- old_vn: 「Densha Hime――nhớ không nhầm thì, là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」
- fix: 「Công chúa Tàu điện――nhớ không nhầm thì, là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2720** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: \\x%lまいてつ;#00ffc040;まいてつ%l;#;同士、鉄道事業者同士というレベルをさらに超え、\\nポーレットと電車姫様とは、ある種の同士なのだ。
- TW: 波萊特和電車公主不僅同是\\x%lまいてつ;#00ffc040;掌車人%l;#;以及鐵路工作人員，她們還是志同道合的朋友。
- old_vn: Vượt xa hơn cả mức độ giữa những \\x%lまいてつ;#00ffc040;chủ tàu%l;#; với nhau, giữa những nhà kinh doanh đường sắt với nhau,\\nPaulette và Densha Hime, là một kiểu đồng chí.
- fix: Vượt xa hơn cả mức độ giữa những \\x%lまいてつ;#00ffc040;chủ tàu%l;#; với nhau, giữa những nhà kinh doanh đường sắt với nhau,\\nPaulette và Công chúa Tàu điện, là một kiểu đồng chí.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 2723** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: \\x%lストーブ客車;#00ffc040;ストーブ客車%l;#;に、あるいは電車姫様に。\\n強い思い入れがあったからこそ、悩んでいたのか。
- TW: 波萊特是因知道自己對\\x%lストーブ客車;#00ffc040;暖爐客車%l;#;，或是對電車公主有著強烈的情感，所以才不敢自己做決定。
- old_vn: Đối với \\x%lストーブ客車;#00ffc040;toa xe sưởi ấm%l;#;, hay đối với Densha Hime.\\nChính vì có tình cảm sâu sắc, nên cô ấy mới đắn đo sao.
- fix: Đối với \\x%lストーブ客車;#00ffc040;toa xe sưởi ấm%l;#;, hay đối với Công chúa Tàu điện.\\nChính vì có tình cảm sâu sắc, nên cô ấy mới đắn đo sao.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### ポーレット13_再評価.txt.toml (4 dòng)

**Key 1312** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「うん、毛利の電車姫様から」
- TW: 「嗯，是毛利的電車公主」
- old_vn: 「Ừm, từ Densha Hime của nhà Mouri.」
- fix: 「Ừm, từ Công chúa Tàu điện của nhà Mouri.」
- Lý do: JP 毛利の電車姫様 — giữ "của nhà Mouri", chỉ đổi tên gọi.

**Key 1330** (nhân vật: れいな; nguồn old_vn: csv3; mục: T10)
- JP: 「そうでしたぁ。あのですね、電車姫さまからのお電話、\\nどんなお話だったんですかぁ？」
- TW: 「對了。那個呀，電車公主打電話來說什麼了？」
- old_vn: 「À đúng rồi ạ~. Chuyện là, điện thoại từ Densha Hime,\\nđã nói về chuyện gì vậy ạ~?」
- fix: 「À đúng rồi ạ~. Chuyện là, điện thoại từ Công chúa Tàu điện,\\nđã nói về chuyện gì vậy ạ~?」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1482** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T10)
- JP: 「移送も全部、電車姫様がご手配くださったのか」
- TW: 「電車公主連運輸都包辦了嗎」
- old_vn: 「Ngay cả việc vận chuyển, Densha Hime cũng sắp xếp toàn bộ sao.」
- fix: 「Ngay cả việc vận chuyển, Công chúa Tàu điện cũng sắp xếp toàn bộ sao.」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

**Key 1877** (nhân vật: monologue; nguồn old_vn: csv3; mục: T10)
- JP: 電車姫様に引き締められて、それでも顔を見た瞬間、\\nもう全部、双鉄くんにふわふわ引き寄せられそうなのに。
- TW: 與電車公主打完電話，我好不容易變得嚴肅了些。但一看到雙鐵君的臉，就又變得輕飄飄的了。
- old_vn: Dù đã được Densha Hime chấn chỉnh tinh thần, nhưng ngay khoảnh khắc nhìn thấy khuôn mặt anh ấy,\\ntôi lại có cảm giác như mọi thứ lại bị hút về phía anh Soutetsu một cách lâng lâng.
- fix: Dù đã được Công chúa Tàu điện chấn chỉnh tinh thần, nhưng ngay khoảnh khắc nhìn thấy khuôn mặt anh ấy,\\ntôi lại có cảm giác như mọi thứ lại bị hút về phía anh Soutetsu một cách lâng lâng.
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml (1 dòng)

**Key 2708** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T10)
- JP: 「電車姫様の働きかけで、[ひろしま,1]廣島ケーブルテレビ制作で\\nこの四月からはじまって、あっという間に全国ネット！」
- TW: 「通過電車公主殿下的牽線，廣島有線電視台拍攝了這齣節目，從四月開始播送，剛播送就推廣到了全國網路播送！」
- old_vn: 「Nhờ sự vận động của Densha Hime, Đài Truyền hình Cáp Hiroshima đã sản xuất\\nvà bắt đầu phát sóng từ tháng 4 này, chớp mắt đã phủ sóng toàn quốc mạng lưới!」
- fix: 「Nhờ sự vận động của Công chúa Tàu điện, Đài Truyền hình Cáp Hiroshima đã sản xuất\\nvà bắt đầu phát sóng từ tháng 4 này, chớp mắt đã phủ sóng toàn quốc mạng lưới!」
- Lý do: JP chứa 電車姫 → "Công chúa Tàu điện" đúng (T10, quyết 20/11 ~17:50, Muse theo ủy quyền).

#### 日々姫11_御一夜モザイク.txt.toml (1 dòng)

**Key 2018** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T10)
- JP: 「発注と、スポンサードの申し出をいただきました。\\n毛利電鉄の――毛利の、電車姫様から」
- TW: 「我收到了毛利電鐵——毛利的電車公主發來的訂單和贊助申請」
- old_vn: 「Chúng ta đã nhận được đơn đặt hàng và lời đề nghị tài trợ.\\\\nTừ Đường sắt điện Mouri――Denshahime của Mouri.」
- fix: 「Chúng ta đã nhận được đơn đặt hàng và lời đề nghị tài trợ.\\\\nTừ Đường sắt điện Mouri――Công chúa Tàu điện của Mouri.」
- Lý do: JP 毛利の、電車姫様 — giữ "của Mouri", chỉ đổi tên gọi.

#### 日々姫16_夢を乗せて.txt.toml (1 dòng)

**Key 1766** (nhân vật: 稀咲; nguồn old_vn: csv3; mục: T10)
- JP: 「毛利の……電車姫様とか言ったっけ？　あの子が、\\n納品した\\x%l客車;#00ffc040;客車%l;#;の質を大いに気に入ってくれたそうでね」
- TW: 「好像有個叫毛利的……電車公主來著吧？她對我們交付的\\x%l客車;#00ffc040;客運車廂%l;#;的品質非常滿意」
- old_vn: 「Cái người tên là... Denshahime của nhà Mouri ấy nhỉ? Nghe nói cô bé đó rất ưng ý chất lượng của \\x%l客車;#00ffc040;toa hành khách%l;#; mà chúng ta đã giao đấy.」
- fix: 「Cái người tên là... Công chúa Tàu điện của nhà Mouri ấy nhỉ? Nghe nói cô bé đó rất ưng ý chất lượng của \\x%l客車;#00ffc040;toa hành khách%l;#; mà chúng ta đã giao đấy.」
- Lý do: JP 毛利の……電車姫様 — giữ "của nhà Mouri", chỉ đổi tên gọi.

### T13. 宮司 → "đền chủ" — 38 dòng

#### lr真闇追加02_御一夜新婚旅行.txt.toml (2 dòng)

**Key 1456** (nhân vật: 真闇; nguồn old_vn: csv3; mục: T13)
- JP: 「ポーちゃんに宮司さんまで！」
- TW: 「小波還有宮司先生！」
- old_vn: "「Cả Po-chan và thầy cúng nữa cơ á!」"
- fix: "「Cả Po-chan và đền chủ nữa cơ á!」"
- Lý do: JP 宮司さん (không có tên Akai) — "thầy cúng" → "đền chủ" trần.

**Key 1500** (nhân vật: れいな; nguồn old_vn: csv3; mục: T13)
- JP: 「ですねぇ。ポーレットや赤井宮司さんも、\\nときどき撮りにきてますよぉ」
- TW: 「是呀。波萊特和赤井宮司有時候也會過來拍哦」
- old_vn: "「Đúng vậy ạ~. Cả Paulette và thầy cúng Akai\\nthỉnh thoảng cũng đến đây chụp ảnh đó nha~」"
- fix: "「Đúng vậy ạ~. Cả Paulette và đền chủ Akai\\nthỉnh thoảng cũng đến đây chụp ảnh đó nha~」"
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

#### グランドリライト06_稀咲.txt.toml (18 dòng)

**Key 1415** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「……席をたたれたあのときに、\\n赤井宮司が止めてくれると――」
- TW: 「……如果在他起身要走的時候，沒有赤井宮司出聲阻止的話——」
- old_vn: 「……Lúc ông ta đứng dậy rời khỏi chỗ ngồi,\\nviệc Akai-guji sẽ ngăn lại――」
- fix: 「……Lúc ông ta đứng dậy rời khỏi chỗ ngồi,\\nviệc đền chủ Akai sẽ ngăn lại――」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 1877** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T13)
- JP: 「いや、今回は僕というより――\\n赤井宮司だろう」
- TW: 「不，這次的功勞不在我，而在赤井宮司身上吧」
- old_vn: 「Không, lần này người có công lớn nhất không phải là cháu――\\nmà là Akai-guji mới đúng.」
- fix: 「Không, lần này người có công lớn nhất không phải là cháu――\\nmà là đền chủ Akai mới đúng.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2174** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「赤井宮司が止めてくれずに、あのまま退出していたら。\\n赤井宮司の手前もあって、意固地になられたかもしれん」
- TW: 「如果他沒有阻止，讓後東先生離開了。後東先生可能會顧及面子，變得意氣用事」
- old_vn: 「Nếu Akai-guji không cản lại mà để ông ta đi luôn.\\nCó khi vì thể diện với Akai-guji, ông ta sẽ trở nên cố chấp cũng nên.」
- fix: 「Nếu đền chủ Akai không cản lại mà để ông ta đi luôn.\\nCó khi vì thể diện với đền chủ Akai, ông ta sẽ trở nên cố chấp cũng nên.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2371** (nhân vật: 稀咲; nguồn old_vn: csv3; mục: T13)
- JP: 「だね。けど、席を立たれたときには正直焦った。\\nあのとき、赤井宮司が引き止めてくれていなければ――」
- TW: 「是啊。不過他起身要走的時候，我其實很著急。如果赤井宮司那時候沒有攔住他……」
- old_vn: 「Đúng vậy. Nhưng thú thật là lúc ông ta đứng dậy em đã rất hoảng.\\nLúc đó, nếu Akai-guji không cản lại thì――」
- fix: 「Đúng vậy. Nhưng thú thật là lúc ông ta đứng dậy em đã rất hoảng.\\nLúc đó, nếu đền chủ Akai không cản lại thì――」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2415** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T13)
- JP: 「赤井宮司とのご縁のおかげ、でございましょうか？」
- TW: 「是看在赤井宮司的面子上，對吧？」
- old_vn: 「Là nhờ mối quan hệ với Akai-guji phải không ạ?」
- fix: 「Là nhờ mối quan hệ với đền chủ Akai phải không ạ?」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2446** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「それはもちろんだろう。赤井宮司を、\\n恐らく後東氏は、相当に高く評価している」
- TW: 「沒錯。後東先生應該對赤井宮司有著相當高的評價」
- old_vn: 「Tất nhiên rồi. Có lẽ ông Goto\\nđánh giá Akai-guji rất cao.」
- fix: 「Tất nhiên rồi. Có lẽ ông Goto\\nđánh giá đền chủ Akai rất cao.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2571** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「やはり、不安はあるのだろうな。\\n[ごとう,1]後東[かいた,1]槐多氏……赤井宮司の言葉以上の人物ゆえに」
- TW: 「肯定是因為我還是感覺不放心。因為後東慶太……是個比赤井宮司描述中更厲害的人物」
- old_vn: 「Quả nhiên là tôi vẫn cảm thấy bất an.\\nGoto Kaita... Ông ta là một nhân vật vượt xa những gì Akai-guji đã mô tả.」
- fix: 「Quả nhiên là tôi vẫn cảm thấy bất an.\\nGoto Kaita... Ông ta là một nhân vật vượt xa những gì đền chủ Akai đã mô tả.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2916** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: そして、ニイロクと赤井宮司も部屋を出て行く。
- TW: 二六和赤井宮司隨後一起離開了房間。
- old_vn: Sau đó, Niiroku và Akai-guji cũng rời khỏi phòng.
- fix: Sau đó, Niiroku và đền chủ Akai cũng rời khỏi phòng.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3013** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: なるほど、ならば――交渉がいざ危うくなれば、\\n赤井宮司のおっしゃった、怪獣大戦争を見れていたのか。
- TW: 原來如此……如果談判真的瀕臨破裂，就能看到赤井宮司所說的怪獸大戰了啊。
- old_vn: Ra là vậy, thế thì――nếu cuộc đàm phán rơi vào nguy hiểm,\\nchúng ta đã có thể chứng kiến cuộc đại chiến quái thú như lời Akai-guji nói sao.
- fix: Ra là vậy, thế thì――nếu cuộc đàm phán rơi vào nguy hiểm,\\nchúng ta đã có thể chứng kiến cuộc đại chiến quái thú như lời đền chủ Akai nói sao.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3078** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: ほっとしたような笑みを浮かべて、\\n宮司は静かに頭を下げる。
- TW: 宮司露出放心的笑容，靜靜地鞠了一躬
- old_vn: Nở nụ cười nhẹ nhõm,\\nAkai-guji khẽ cúi đầu.
- fix: Nở nụ cười nhẹ nhõm,\\nđền chủ Akai khẽ cúi đầu.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3106** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 興味をいきなり失くしたように、僕との握手もさっと終え。\\n――けれども後東氏は、赤井宮司には手を差し出さない。
- TW: 後東先生一下子鬆開了我的手，彷彿瞬間對我失去了興趣。但他也沒有對赤井宮司伸出手。
- old_vn: Như đột nhiên mất hứng, ông ta nhanh chóng kết thúc cái bắt tay với tôi.\\n――Thế nhưng ông Goto lại không đưa tay ra với Akai-guji.
- fix: Như đột nhiên mất hứng, ông ta nhanh chóng kết thúc cái bắt tay với tôi.\\n――Thế nhưng ông Goto lại không đưa tay ra với đền chủ Akai.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3113** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 言って、後東氏は赤井宮司に背中を向ける。
- TW: 後東先生說完以後就轉過身子，背對赤井宮司。
- old_vn: Nói xong, ông Goto quay lưng lại với Akai-guji.
- fix: Nói xong, ông Goto quay lưng lại với đền chủ Akai.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3184** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 稀咲が動かす視線を追えばその先で、\\n赤井宮司は立ち上がっている。
- TW: 我順著稀咲的視線看過去，赤井宮司已經站起了身。
- old_vn: Nhìn theo hướng mắt của Kisaki,\\nAkai-guji đang đứng dậy.
- fix: Nhìn theo hướng mắt của Kisaki,\\nđền chủ Akai đang đứng dậy.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3242** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13+T18)
- JP: どころか視線も宮司ではなく、\\nその傍らの、運転鞄に向いている。
- TW: 甚至連視線都沒有朝著赤井宮司，而是看向旁邊的駕駛包。
- old_vn: Thậm chí ánh mắt ông ta cũng không hướng về Akai-guji,\\nmà lại nhìn chằm chằm vào chiếc túi phi hành đoàn bên cạnh.
- fix: Thậm chí ánh mắt ông ta cũng không hướng về đền chủ Akai,\\nmà lại nhìn chằm chằm vào chiếc túi công tác bên cạnh.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai).

**Key 3469** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: ほとんど同時に、その何倍も深く、深く、\\n赤井宮司が――
- TW: 赤井宮司也同時深深鞠躬，顯得無比誠懇。
- old_vn: Gần như cùng lúc đó, Akai-guji\\ncũng cúi gập người xuống sâu, sâu hơn gấp nhiều lần――
- fix: Gần như cùng lúc đó, đền chủ Akai\\ncũng cúi gập người xuống sâu, sâu hơn gấp nhiều lần――
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3470** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 部屋すみのソファに静かに座る赤井宮司が、\\n今日、初めての声を出す。
- TW: 赤井宮司安靜地坐在房間角落沙發上，這是他今天第一次開口說話。
- old_vn: Akai-guji đang ngồi lặng lẽ trên ghế sofa ở góc phòng,\\nhôm nay, lần đầu tiên cất tiếng.
- fix: đền chủ Akai đang ngồi lặng lẽ trên ghế sofa ở góc phòng,\\nhôm nay, lần đầu tiên cất tiếng.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3472** (nhân vật: monologue; nguồn old_vn: unification-merged (U4); mục: T13+T18+T11)
- JP: 包帯で顔をぐるぐるにした運転体の\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を、\\n赤井宮司が運転鞄からそっと取り出す。
- TW: 赤井宮司從駕駛包裡小心翼翼地拿出一個駕駛體\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，她的臉上還纏著一圈圈的繃帶。
- old_vn: Akai-guji nhẹ nhàng lấy từ trong chiếc túi phi hành đoàn ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít.
- fix: đền chủ Akai nhẹ nhàng lấy từ trong chiếc túi công tác ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai). "kíp lái" trong cùng dòng là T11 — đã đổi thành "thân vận hành" theo fix U4 đã gộp (ghép bởi điều phối, xem ghi chú cuối REVIEW).

**Key 3540** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13+T18)
- JP: 運転鞄からの突然の声にも、赤井宮司は動じない。\\nニイロクと――鞄に向けて呼びかけて。
- TW: 駕駛包突然發出聲音，赤井宮司卻完全不感到驚訝。而且……他把駕駛包稱作“二六”。
- old_vn: Dù giọng nói bất ngờ phát ra từ chiếc túi phi hành đoàn, Akai-guji vẫn không hề nao núng.\\nÔng gọi Niiroku――hướng về phía chiếc túi.
- fix: Dù giọng nói bất ngờ phát ra từ chiếc túi công tác, đền chủ Akai vẫn không hề nao núng.\\nÔng gọi Niiroku――hướng về phía chiếc túi.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai).

#### ハチロク15a_痛みとの決別.txt.toml (1 dòng)

**Key 2414** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 即座は、日々姫と凪とれいなと。続いて、ポーレット\\n稀咲、ニイロク――　一番最後に、真闇姉と、赤井宮司も。
- TW: 先是日日姬、凪和玲奈，然後是波萊特、稀咲、二六——最後是真闇姐和赤井宮司。
- old_vn: Đầu tiên là Hibiki, Nagi và Reina. Tiếp theo là Paulette\\nKisaki, Niiroku—— Cuối cùng là chị Mayami và cả Thầy cúng Akai.
- fix: Đầu tiên là Hibiki, Nagi và Reina. Tiếp theo là Paulette\\nKisaki, Niiroku—— Cuối cùng là chị Mayami và cả đền chủ Akai.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

#### ポーレット16_明日へのレール.txt.toml (7 dòng)

**Key 1708** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「赤井宮司も本当にありがとうございます」
- TW: 「也非常感謝赤井宮司您的幫助」
- old_vn: 「Thật sự cảm ơn ông Guuji rất nhiều ạ.」
- fix: 「Thật sự cảm ơn đền chủ Akai rất nhiều ạ.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 1715** (nhân vật: れいな; nguồn old_vn: csv3; mục: T13)
- JP: 「ニイロクさんと[ぐうじ,1]宮司さん、お上手ですねぇ」
- TW: 「二六小姐和宮司先生，真是熟練呀」
- old_vn: 「Cô Niiroku và ông Guuji, lái giỏi quá nha~」
- fix: 「Cô Niiroku và đền chủ Akai, lái giỏi quá nha~」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2292** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「神社の視察も良い感触だった。説明役の大役を終え、\\n宮司としても、気分よく乗務されているのだろう」
- TW: 「神社的視察也進展得很順利。完成了介紹神社的艱巨任務，宮司此刻駕駛起來一定也很寬心」
- old_vn: 「Chuyến thị sát đền thờ cũng diễn ra suôn sẻ. Sau khi hoàn thành trọng trách giải thích,\\nông Guuji chắc hẳn cũng đang làm nhiệm vụ với tâm trạng rất tốt.」
- fix: 「Chuyến thị sát đền thờ cũng diễn ra suôn sẻ. Sau khi hoàn thành trọng trách giải thích,\\nđền chủ Akai chắc hẳn cũng đang làm nhiệm vụ với tâm trạng rất tốt.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2933** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T13)
- JP: 御一夜駅のホームに出れば、\\n赤井宮司の言葉の理由が、すぐわかる。
- TW: 我們走出御一夜站月台，馬上理解了赤井宮司的話。
- old_vn: Vừa bước ra sân ga Ohitoyo, tôi lập tức hiểu được lý do cho lời nói của ông Guuji.
- fix: Vừa bước ra sân ga Ohitoyo, tôi lập tức hiểu được lý do cho lời nói của đền chủ Akai.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2969** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 軽く手を振り、赤井宮司に向き直る。
- TW: 我輕輕揮了揮手，轉向赤井宮司。
- old_vn: Tôi khẽ vẫy tay rồi quay sang ông Guuji.
- fix: Tôi khẽ vẫy tay rồi quay sang đền chủ Akai.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3304** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 自分でも露骨にすぎる誤魔化しのように思えるが、\\n赤井宮司もその連れも、全く気にする素振りを見せない。
- TW: 連我自己都覺得這個假動作太過明顯，但赤井宮司與他的同伴都全然沒有在意。
- old_vn: Ngay cả bản thân tôi cũng thấy kiểu lấp liếm này quá lộ liễu,\\nnhưng ông Guuji và người đi cùng hoàn toàn không có vẻ gì là bận tâm.
- fix: Ngay cả bản thân tôi cũng thấy kiểu lấp liếm này quá lộ liễu,\\nnhưng đền chủ Akai và người đi cùng hoàn toàn không có vẻ gì là bận tâm.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3327** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: ガソリン\\x%l気動車;#00ffc040;気動車%l;#;に戻した影響も大きかろうが、\\n宮司たちの腕も、それ以上に寄与してるのだろう。
- TW: 雖說主要是因為Ｋｉｈａ０７復原成了汽油\\x%l気動車;#00ffc040;動車%l;#;，但宮司二人的技術，一定也起到了很大的作用。
- old_vn: Ảnh hưởng từ việc chuyển về dùng xăng cho \\x%l気動車;#00ffc040;toa xe tự hành%l;#; có lẽ là rất lớn,\\nnhưng tay lái của nhóm ông Guuji chắc hẳn còn đóng góp nhiều hơn thế.
- fix: Ảnh hưởng từ việc chuyển về dùng xăng cho \\x%l気動車;#00ffc040;toa xe tự hành%l;#; có lẽ là rất lớn,\\nnhưng tay lái của nhóm đền chủ Akai chắc hẳn còn đóng góp nhiều hơn thế.
- Lý do: JP 宮司たち (= Akai + người đi cùng) — "nhóm ông Guuji" → "nhóm đền chủ Akai" (giữ neo tên Akai như các dòng P16 khác).

#### 日々姫09_run_with_our_dreams.txt.toml (3 dòng)

**Key 2636** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: それを両立させるため、赤井宮司と相談の上、\\n僕らは僕らの結婚式に、人前式を選んだのだ。
- TW: 為了同時實現這兩個願望，我們在跟赤井宮司商量之後，決定用人前式來舉行自己的婚禮。
- old_vn: Để dung hòa cả hai điều đó, sau khi bàn bạc với cha xứ Akai,\\nchúng tôi đã chọn tổ chức lễ cưới trước mặt mọi người.
- fix: Để dung hòa cả hai điều đó, sau khi bàn bạc với đền chủ Akai,\\nchúng tôi đã chọn tổ chức lễ cưới trước mặt mọi người.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2699** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 赤井宮司の落ち着いた声。\\nおかげで、すんなり我に返れる。
- TW: 耳邊傳來赤井宮司平靜的聲音。這讓我一下子回過神來。
- old_vn: Giọng nói điềm tĩnh của cha xứ Akai.\\nNhờ vậy, tôi mới dễ dàng bừng tỉnh.
- fix: Giọng nói điềm tĩnh của đền chủ Akai.\\nNhờ vậy, tôi mới dễ dàng bừng tỉnh.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2751** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 人前式の司会は初めてとのことであったが、\\nさすがは赤井阿蘇神社の宮司なのだと思い知る。
- TW: 雖然是第一次擔任人前式的主持，但我只能說赤井阿蘇神社的宮司還是有實力的。
- old_vn: Dù nghe nói đây là lần đầu tiên ngài ấy chủ trì một lễ cưới trước mặt mọi người,\\nnhưng quả không hổ danh là cha xứ của đền Akai Aso.
- fix: Dù nghe nói đây là lần đầu tiên ngài ấy chủ trì một lễ cưới trước mặt mọi người,\\nnhưng quả không hổ danh là đền chủ của đền Akai Aso.
- Lý do: JP 赤井阿蘇神社の宮司 — "cha xứ của đền Akai Aso" → "đền chủ của đền Akai Aso".

#### 日々姫09_静かなる開戦.txt.toml (5 dòng)

**Key 1790** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T13)
- JP: 「もちろんです。赤井宮司、どうぞ」
- TW: 「當然。赤井宮司先生，請您發言」
- old_vn: 「Tất nhiên rồi ạ. Xin mời thầy cúng Akai.」
- fix: 「Tất nhiên rồi ạ. Xin mời đền chủ Akai.」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2579** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: ポーレットから、少し彷徨い真闇姉へ、僕へ、赤井宮司へ。\\nそしていつしか、たった一人へと集合していく。
- TW: 眾多視線先是有些困惑地飄到真闇姐、我、赤井宮司身上，然後不知不覺間集中到一個人身上。
- old_vn: Từ Paulette, khẽ lướt sang chị Mayami, sang tôi, rồi đến thầy cúng Akai.\\nVà rồi chẳng biết từ lúc nào, tất cả đều dồn về một người duy nhất.
- fix: Từ Paulette, khẽ lướt sang chị Mayami, sang tôi, rồi đến đền chủ Akai.\\nVà rồi chẳng biết từ lúc nào, tất cả đều dồn về một người duy nhất.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2644** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 赤井宮司の静かな挙手に、\\n声を荒らげ腰を浮かせていた男が、口を噤んで引き下がる。
- TW: 赤井宮司一舉手，那個正想起身的粗暴男人立刻閉上嘴坐了回去。
- old_vn: Trước cái giơ tay điềm tĩnh của thầy cúng Akai,\\nngười đàn ông đang lớn tiếng và nhổm dậy liền im bặt và lùi lại.
- fix: Trước cái giơ tay điềm tĩnh của đền chủ Akai,\\nngười đàn ông đang lớn tiếng và nhổm dậy liền im bặt và lùi lại.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2645** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 心底、驚いたような声。\\n赤井宮司は、その目を大きく見開いている。
- TW: 赤井宮司發出恍然大悟的聲音，睜大了眼睛。
- old_vn: Một giọng nói kinh ngạc từ tận đáy lòng.\\nThầy cúng Akai mở to hai mắt.
- fix: Một giọng nói kinh ngạc từ tận đáy lòng.\\nđền chủ Akai mở to hai mắt.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 2660** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: 赤井宮司の声にさえ、緊張に近いものを感じる。
- TW: 連赤井宮司的聲音中都帶有一絲緊張的味道。
- old_vn: Thậm chí trong giọng nói của thầy cúng Akai, tôi cũng cảm nhận được sự căng thẳng.
- fix: Thậm chí trong giọng nói của đền chủ Akai, tôi cũng cảm nhận được sự căng thẳng.
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

#### 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml (2 dòng)

**Key 1415** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T13)
- JP: 「は、な、お――『鼻緒』か！\\n下駄か草履、下駄か草履は――赤井宮司っ！！」
- TW: 「ha、na、o――是木屐帶！木屐或者草屐、木屐或者草屐――去找赤井宮司！！」
- old_vn: 「Ha, na, o――『Hanao (Quai dép)』 sao!\\nGuốc mộc hoặc dép rơm, guốc mộc hoặc dép rơm thì――Cha xứ Akai!!」
- fix: 「Ha, na, o――『Hanao (Quai dép)』 sao!\\nGuốc mộc hoặc dép rơm, guốc mộc hoặc dép rơm thì――đền chủ Akai!!」
- Lý do: JP chứa 宮司 → "đền chủ" đúng (T13, quyết 19/11, Hieu).

**Key 3002** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13)
- JP: なるほど、“智慧を借りる”相手なら、\\nこの社の主、赤井宮司ほどの適任者は無い。
- TW: 原來如此，要借用“智慧”的話，神社的神主赤井宮司無疑是最佳人選。
- old_vn: Ra là vậy, nếu là người để "mượn trí tuệ",\\nthì không ai thích hợp hơn chủ nhân của ngôi đền này, cha xứ Akai.
- fix: Ra là vậy, nếu là người để "mượn trí tuệ",\\nthì không ai thích hợp hơn chủ nhân của ngôi đền này, đền chủ Akai.
- Lý do: JP この社の主、赤井宮司 — giữ "chủ nhân của ngôi đền này", chỉ đổi "cha xứ Akai" → "đền chủ Akai".

### T14. Migita (xưởng rượu) → "Migita Ichi" — 21 dòng

#### lr_ふかみh2_セックスの意味.txt.toml (1 dòng)

**Key 1406** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 右田一でも試飲に使うあのプラカップは、60ml容量だ。\\n三杯呑んでも、普通のコップ一杯にもみたぬ量だが――
- TW: 右田一用的試喝塑膠杯容量是六十毫升。三杯加起來也還不到正常杯子一杯的分量，但是……
- old_vn: Cốc nhựa dùng để uống thử ở Migita System có dung tích 60ml.\\nDù uống ba ly thì cũng chưa đầy một cốc bình thường——
- fix: Cốc nhựa dùng để uống thử ở Migita Ichi có dung tích 60ml.\\nDù uống ba ly thì cũng chưa đầy một cốc bình thường——
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### グランドリライト03_日々姫.txt.toml (1 dòng)

**Key 3017** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 言いたいことをきちんと言葉に直すため、日々姫の仕事を。そうして次に、右田一酒造元の焼酎ラベルを思い浮かべる。
- TW: 為了更好地表達自己想說的意思，我想像了一下日日姬的工作，還有右田一酒廠的燒酒標籤。
- old_vn: Để diễn đạt chính xác những gì muốn nói, tôi nghĩ đến công việc của Hibiki. Tiếp đó, tôi liên tưởng đến nhãn chai shochu của xưởng rượu Migita.
- fix: Để diễn đạt chính xác những gì muốn nói, tôi nghĩ đến công việc của Hibiki. Tiếp đó, tôi liên tưởng đến nhãn chai shochu của xưởng rượu Migita Ichi.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### ハチロク06_のぞみ.txt.toml (1 dòng)

**Key 1577** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: ……夏祭りのとき、右田一酒造元で配布するうちわ。\\n毎年同じ柄なので、記憶もぱたぱた、あおがれる。
- TW: ……扇子是右田一釀酒廠在夏季慶典派發的，因為每年都是相同的圖案，塵封的記憶也在扇子吹拂下漸漸復甦。
- old_vn: ……Chiếc quạt giấy được xưởng rượu Migita phân phát vào dịp lễ hội mùa hè.\\nVì năm nào cũng cùng một họa tiết, nên những ký ức cũng như được quạt tung lên.
- fix: ……Chiếc quạt giấy được xưởng rượu Migita Ichi phân phát vào dịp lễ hội mùa hè.\\nVì năm nào cũng cùng một họa tiết, nên những ký ức cũng như được quạt tung lên.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### ハチロク15a_痛みとの決別.txt.toml (1 dòng)

**Key 1835** (nhân vật: 真闇; nguồn old_vn: csv3; mục: T14)
- JP: 「水なら、右田一酒造元からも提供できるけん。\\n必要あれば、いくらでも」
- TW: 「右田一釀酒廠可以送水過去。要多少有多少」
- old_vn: 「Nếu là nước, thì xưởng rượu Migita System cũng có thể cung cấp.\\nCần bao nhiêu cũng có」
- fix: 「Nếu là nước, thì xưởng rượu Migita Ichi cũng có thể cung cấp.\\nCần bao nhiêu cũng có」
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu). Lượt soát 2 sửa: fix ban đầu viết nhầm "Migita Ichi Ichi" (cặp thay thế "Migita System"/"Migitakazu" → "Migita Ichi" rồi cặp "xưởng rượu Migita" → "xưởng rượu Migita Ichi" áp dụng chồng lên kết quả) → đã sửa thành "Migita Ichi".

#### ハチロク15b_さよなら列車.txt.toml (1 dòng)

**Key 2228** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: クーラーボックスの中には、ぎっしりと、\\n安全のためのペットボトルで、右田一の水が入っている。
- TW: 真闇姐拿來的保溫箱裡裝滿了右田一釀酒廠的瓶裝水，這樣在車裡喝也很安全。
- old_vn: Bên trong thùng giữ nhiệt, chứa đầy ắp\\nnhững chai nhựa nước của Migita System để đảm bảo an toàn.
- fix: Bên trong thùng giữ nhiệt, chứa đầy ắp\\nnhững chai nhựa nước của Migita Ichi để đảm bảo an toàn.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### ポーレット01_御一夜探し.txt.toml (1 dòng)

**Key 1936** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T14)
- JP: 「御一夜[じょうし,1]城址、クマ川下り発船所の他だと、\\n[みぎたいちしゅぞうもと,5]右田一酒造元もそうですよね」
- TW: 「除了御一夜城址、隈河漂流發船點之外，右田一釀酒廠也是其中之一呢」
- old_vn: 「Ngoài Di tích thành Ohitoyo và bến tàu chèo sông Kuma ra, thì Nhà máy rượu Migita System cũng là một điểm tham quan nhỉ.」
- fix: 「Ngoài Di tích thành Ohitoyo và bến tàu chèo sông Kuma ra, thì Nhà máy rượu Migita Ichi cũng là một điểm tham quan nhỉ.」
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 共通07_鍵.txt.toml (2 dòng)

**Key 2025** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T14)
- JP: 「ええと……鉄道にかまけて右田の酒蔵を傾けた……\\nそういう人だから、その……反面教師にするようにって」
- TW: 「爸爸說……他一心只顧著鐵路，差點沒毀了右田一釀酒廠……所以要我……把他當做反面教材」
- old_vn: 「À ừm……bố tôi bảo ông ấy là người vì quá đắm chìm vào đường sắt mà làm khuynh gia bại sản xưởng rượu Migita……\\nlà một người như vậy, nên……hãy lấy đó làm tấm gương xấu.」
- fix: 「À ừm……bố tôi bảo ông ấy là người vì quá đắm chìm vào đường sắt mà làm khuynh gia bại sản xưởng rượu Migita Ichi……\\nlà một người như vậy, nên……hãy lấy đó làm tấm gương xấu.」
- Lý do: JP 右田の酒蔵 (không có 一) nhưng cùng thực thể xưởng rượu nhà Migita — "xưởng rượu Migita" → "xưởng rượu Migita Ichi".

**Key 2547** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 借金問題が発覚したとき、真闇姉は既に右田一酒造の\\x%l杜氏;#00ffc040;杜氏%l;\\n#;――右田家の実質的な当主だった。
- TW: 發現欠款問題的時候，真闇姐已經成了右田一釀酒廠的\\x%l杜氏;#00ffc040;掌窖%l;#;——也就是右田家實際上的當家。
- old_vn: Khi vấn đề nợ nần bị vỡ lở, chị Mayami đã là \\x%l杜氏;#00ffc040;trưởng hầm rượu%l;#; của xưởng rượu Migita\\n——tức là đương gia thực sự của nhà Migita.
- fix: Khi vấn đề nợ nần bị vỡ lở, chị Mayami đã là \\x%l杜氏;#00ffc040;trưởng hầm rượu%l;#; của xưởng rượu Migita Ichi\\n——tức là đương gia thực sự của nhà Migita.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 凪ふかみ03_三人いっしょ.txt.toml (3 dòng)

**Key 1071** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: ……どうにも、なにか、いつもとは違った感じだった。\\n右田一酒造元での真闇姉が。
- TW: ……但就是覺得和以往有些不一樣。是右田一釀酒廠裡的真闇姐嗎。
- old_vn: ...Không hiểu sao, có cảm giác gì đó khác với bình thường.\\nChị Mayami ở cơ sở nấu rượu Migitai ấy.
- fix: ...Không hiểu sao, có cảm giác gì đó khác với bình thường.\\nChị Mayami ở cơ sở nấu rượu Migita Ichi ấy.
- Lý do: QUYẾT theo ủy quyền (mục con OPEN O62 của T14): JP 右田一酒造元 — "Migitai" là cách đọc sai của 右田一, không phải tên riêng khác; cùng thực thể với mọi dòng "Migita Ichi" khác.

**Key 1429** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T14)
- JP: 「右田一――右田一酒造元さんです」
- TW: 「右田一——是右田一釀酒廠」
- old_vn: 「Migitai——Là cơ sở nấu rượu Migitai ạ」
- fix: 「Migita Ichi——Là cơ sở nấu rượu Migita Ichi ạ」
- Lý do: QUYẾT theo ủy quyền (O62): JP 「右田一――右田一酒造元さんです」 — "Migitai——Là cơ sở nấu rượu Migitai" → "Migita Ichi——Là cơ sở nấu rượu Migita Ichi".

**Key 2525** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 僕も倣って、右田一では、一人の修学旅行生として、\\n謙虚に学を修めよう。
- TW: 那我也同樣，以修學旅行的學生身份，前往右田一釀酒廠謙虛地學習吧。
- old_vn: Tôi cũng sẽ bắt chước, ở Migitai, với tư cách là một học sinh đi dã ngoại,\\ntôi sẽ khiêm tốn học hỏi.
- fix: Tôi cũng sẽ bắt chước, ở Migita Ichi, với tư cách là một học sinh đi dã ngoại,\\ntôi sẽ khiêm tốn học hỏi.
- Lý do: QUYẾT theo ủy quyền (O62): JP 右田一では — "ở Migitai" → "ở Migita Ichi".

#### 日々姫01_リゾート食堂列車計画.txt.toml (1 dòng)

**Key 1688** (nhân vật: 日々姫; nguồn old_vn: csv3; mục: T14)
- JP: 「うん。そうしたい。新しい家を作るから。\\n右田の蔵を。うちをあとにするなら、その理由がいい」
- TW: 「就是這樣，我想要組成新的家庭。把這個當成我走出右田酒廠、走出家門的理由正合適」
- old_vn: 「Vâng. Em muốn vậy. Vì chúng ta sẽ tạo nên một gia đình mới.\\nNếu phải rời khỏi xưởng rượu Migita, rời khỏi ngôi nhà này, thì đó là một lý do tuyệt vời.」
- fix: 「Vâng. Em muốn vậy. Vì chúng ta sẽ tạo nên một gia đình mới.\\nNếu phải rời khỏi xưởng rượu Migita Ichi, rời khỏi ngôi nhà này, thì đó là một lý do tuyệt vời.」
- Lý do: JP 右田の蔵 (không có 一) nhưng cùng thực thể xưởng rượu nhà Migita — "xưởng rượu Migita" → "xưởng rượu Migita Ichi".

#### 日々姫02_日々姫の日々.txt.toml (2 dòng)

**Key 2516** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: ああ、しかし。それならばそれで、\\n右田一酒造元が希望を出さなかったということになるのか。
- TW: 不過，這樣也就是說，是右田一釀酒廠沒有提出委託。
- old_vn: A, nhưng mà. Nếu vậy thì,\\nchẳng phải là do nhà nấu rượu Migita System đã không yêu cầu sao.
- fix: A, nhưng mà. Nếu vậy thì,\\nchẳng phải là do nhà nấu rượu Migita Ichi đã không yêu cầu sao.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

**Key 2671** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 蔵人頭――右田一酒蔵元でナンバー２の斎藤さんに、\\n何を意見できるような立場ではない。
- TW: 對於釀酒師總管——右田一釀酒廠的副手齋藤婆婆，我是沒有資格提意見的。
- old_vn: Trước mặt thợ nấu rượu trưởng——nhân vật số 2 ở nhà nấu rượu Migita System là bà Saitou,\\ntôi không có tư cách để đưa ra ý kiến gì cả.
- fix: Trước mặt thợ nấu rượu trưởng——nhân vật số 2 ở nhà nấu rượu Migita Ichi là bà Saitou,\\ntôi không có tư cách để đưa ra ý kiến gì cả.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 日々姫03_湯富院.txt.toml (1 dòng)

**Key 2662** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T14)
- JP: 右田一酒造元での朝の掃除を繰り返すうち、\\n日々姫も僕も、それを事実と学んでいるから。
- TW: 在右田一釀酒廠的無數次晨間打掃的經歷，讓我們學到了這個道理。
- old_vn: 「Nhờ lặp lại việc quét dọn buổi sáng ở nhà máy rượu Migita, Hibiki và tôi đã học được điều đó là sự thật.」
- fix: 「Nhờ lặp lại việc quét dọn buổi sáng ở nhà máy rượu Migita Ichi, Hibiki và tôi đã học được điều đó là sự thật.」
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 日々姫08_とれいん食堂.txt.toml (1 dòng)

**Key 3067** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 職人として――右田の蔵の杜氏と筆頭蔵人が、\\n声を揃えて、形を示して、認めてくれた。
- TW: 右田酒廠的掌窖和首席釀酒師以工匠的身份，一起用話語和實際行動認可了我們。
- old_vn: Với tư cách là những người thợ――Trưởng hầm rượu và Thợ ủ rượu chính của xưởng rượu Migita,\\nđã đồng thanh, thể hiện bằng hành động, và công nhận chúng tôi.
- fix: Với tư cách là những người thợ――Trưởng hầm rượu và Thợ ủ rượu chính của xưởng rượu Migita Ichi,\\nđã đồng thanh, thể hiện bằng hành động, và công nhận chúng tôi.
- Lý do: JP 右田の蔵の杜氏 (không có 一) nhưng cùng thực thể xưởng rượu nhà Migita — "xưởng rượu Migita" → "xưởng rượu Migita Ichi".

#### 日々姫09_run_with_our_dreams.txt.toml (1 dòng)

**Key 1840** (nhân vật: 赤井; nguồn old_vn: csv3; mục: T14)
- JP: 「さて、ここで[みぎたいちしゅぞうもと,5]右田一酒造元。[とうじ,1]杜氏・右田[まくら,1]真闇様。\\n[くらびとがしら,2]蔵人頭・斎藤[ほのか,1]穂香様からのご[しんもつ,1]進物です」
- TW: 「好了，接下來有請來自右田一釀酒廠的掌窖右田真闇小姐，和首席釀酒師齋藤穗香女士獻酒」
- old_vn: 「Vậy thì, tiếp theo đây là món quà chúc mừng từ Xưởng rượu Migita.\\nTrưởng hầm rượu Migita Mayami và Thợ ủ rượu chính Saito Honoka.」
- fix: 「Vậy thì, tiếp theo đây là món quà chúc mừng từ Xưởng rượu Migita Ichi.\\nTrưởng hầm rượu Migita Mayami và Thợ ủ rượu chính Saito Honoka.」
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 日々姫09_静かなる開戦.txt.toml (1 dòng)

**Key 1690** (nhân vật: 日々姫; nguồn old_vn: unif (đợt unification đã gộp); mục: T14)
- JP: 「私、右田日々姫です。右田一酒造元の末娘で、\\n御一夜鉄道株式会社の車輌部長で、見習い\\x%l機関助士;#00ffc040;機関助士%l;#;で」
- TW: 「我叫右田日日姬，是右田一釀酒廠主人的次女，也是御一夜鐵路股份公司的車輛部長，兼任實習\\x%l機関士;#00ffc040;司機%l;#;」
- old_vn: 「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita,\\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohitoyo, và là \\x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」
- fix: 「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita Ichi,\\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohitoyo, và là \\x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu).

#### 真闇01_再蒸留.txt.toml (3 dòng)

**Key 2164** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T14)
- JP: うちの酒蔵の看板酒である“右田一”は、\\n市内からの予約だけで九割が売れる、地元密着の人気酒だ。
- TW: 我們酒窖的招牌酒“右田一”光是靠市內預約的份就能賣掉九成，是與當地密不可分的熱門酒。
- old_vn: Loại rượu trứ danh "Migitakazu" của xưởng rượu nhà tôi,\\nlà một loại rượu rất được ưa chuộng ở địa phương, chỉ riêng lượng đặt trước trong thành phố đã chiếm tới chín mươi phần trăm doanh số.
- fix: Loại rượu trứ danh "Migita Ichi" của xưởng rượu nhà tôi,\\nlà một loại rượu rất được ưa chuộng ở địa phương, chỉ riêng lượng đặt trước trong thành phố đã chiếm tới chín mươi phần trăm doanh số.
- Lý do: JP “右田一” là tên loại rượu trứ danh của xưởng (看板酒) — "Migitakazu" là dạng bịa, đúng là "Migita Ichi".

**Key 2366** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: 二億、万一返済し損ねてしまうなら、\\n真闇姉にも右田一酒蔵にも大きな打撃を与えることは明白だ。
- TW: 萬一沒能還清兩億，那會對真闇姐及右田一釀酒廠造成多大的打擊是顯而易見的。
- old_vn: Hai trăm triệu yên, rủi mà không trả được,\\nthì rõ ràng sẽ giáng một đòn nặng nề lên cả chị Mayami và xưởng rượu Migitakazu.
- fix: Hai trăm triệu yên, rủi mà không trả được,\\nthì rõ ràng sẽ giáng một đòn nặng nề lên cả chị Mayami và xưởng rượu Migita Ichi.
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu). Lượt soát 2 sửa: fix ban đầu viết nhầm "Migita Ichi Ichi" (cặp thay thế "Migita System"/"Migitakazu" → "Migita Ichi" rồi cặp "xưởng rượu Migita" → "xưởng rượu Migita Ichi" áp dụng chồng lên kết quả) → đã sửa thành "Migita Ichi".

**Key 2444** (nhân vật: monologue; nguồn old_vn: csv3; mục: T14)
- JP: （\\x%lエアクラ;#00ffc040;エアクラ%l;#;工場が誘致されてしまえば、いつかは――\\n右田一酒造元にも、致命的な悪影響が及ぶのだから）
- TW: （一旦\\x%lエアクラ;#00ffc040;空凝機%l;#;工廠最終落戶，總有一天——會連右田一釀酒廠都受到致命的影響）
- old_vn: （Nếu nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; được xây dựng, thì một ngày nào đó——\\nNó cũng sẽ gây ra những ảnh hưởng chí mạng đến xưởng rượu Migitakazu.）
- fix: （Nếu nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; được xây dựng, thì một ngày nào đó——\\nNó cũng sẽ gây ra những ảnh hưởng chí mạng đến xưởng rượu Migita Ichi.）
- Lý do: JP chứa 右田一 (xưởng rượu Migita Ichi) → "Migita Ichi" đúng; không tồn tại thực thể "Migita System" (T14, quyết 19/11, Hieu). Lượt soát 2 sửa: fix ban đầu viết nhầm "Migita Ichi Ichi" (cặp thay thế "Migita System"/"Migitakazu" → "Migita Ichi" rồi cặp "xưởng rượu Migita" → "xưởng rượu Migita Ichi" áp dụng chồng lên kết quả) → đã sửa thành "Migita Ichi".

### T17. 術仙 → "Jutsusen" — 85 dòng

#### れいな01_炭鉱探索.txt.toml (1 dòng)

**Key 1742** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「プラスアルファのアイディアを求める意味でも、\\n[じゅつせん,1]術仙廃炭鉱近辺の追加調査を重ねたいのだが――」
- TW: 「我想再次對術仙廢煤礦周邊進行調查。就算是為了尋找額外的賣點，也有這麼做的必要……」
- old_vn: 「Để tìm kiếm những ý tưởng cộng thêm đó,\\nanh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsu-sen――」
- fix: 「Để tìm kiếm những ý tưởng cộng thêm đó,\\nanh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsusen――」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### れいな02_れいなとポーレット.txt.toml (2 dòng)

**Key 1601** (nhân vật: ポーレット; nguồn old_vn: csv3; mục: T17)
- JP: 「今日は、マイントレジャー[じゅつせん,1]術仙炭鉱において産出予定の\\n石炭の用途についてお知恵を頂きたく思っております」
- TW: 「今天請大家來，是希望針對煤探樂園術仙煤礦預定產出的煤炭用途，徵詢大家的寶貴意見」
- old_vn: 「Hôm nay, chúng tôi mong mọi người góp ý về công dụng của lượng than\\ndự kiến khai thác tại Mỏ than Jussen thuộc Mine Treasure.」
- fix: 「Hôm nay, chúng tôi mong mọi người góp ý về công dụng của lượng than\\ndự kiến khai thác tại Mỏ than Jutsusen thuộc Mine Treasure.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1623** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T17)
- JP: 「なくなったというのは――\\n術仙廃炭鉱のように、線路くらいは残っているのか？」
- TW: 「你說“沒有了”——是像術仙廢煤礦那樣，至少還保留著線路嗎？」
- old_vn: 「Không còn nữa tức là——\\nGiống như Mỏ than bỏ hoang Jussen, ít nhất vẫn còn lại đường ray chứ?」
- fix: 「Không còn nữa tức là——\\nGiống như Mỏ than bỏ hoang Jutsusen, ít nhất vẫn còn lại đường ray chứ?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### れいな03_しゅっぱつしんこう.txt.toml (1 dòng)

**Key 1513** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T17)
- JP: 「相互乗り入れとなると、ダイアが複雑化しますからね。\\nまして、マイントレジャー・[じゅつせん,1]術仙炭鉱も稼働しますし」
- TW: 「如果進行互通運行的話，時刻表就會變複雜了。而且煤探樂園·術仙煤礦也會運作起來的」
- old_vn: 「Nếu chạy liên thông thì biểu đồ chạy tàu sẽ phức tạp hơn mà.\\nHuống hồ Mine Treasure và mỏ than Jussen cũng sẽ đi vào hoạt động nữa.」
- fix: 「Nếu chạy liên thông thì biểu đồ chạy tàu sẽ phức tạp hơn mà.\\nHuống hồ Mine Treasure và mỏ than Jutsusen cũng sẽ đi vào hoạt động nữa.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### グランドリライト04_ポーレット.txt.toml (4 dòng)

**Key 1690** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「探検の楽しみだけでなく、工場見学の楽しみも加える。\\n採炭、発電、活用と――術仙を、工業博物館の町とする」
- TW: 「不僅能讓旅客享受探險的樂趣，還能參觀工廠。通過採煤，發電並加以活用，讓術仙成為工業博物館之城」
- old_vn: 「Không chỉ có niềm vui thám hiểm, mà còn thêm cả niềm vui tham quan nhà máy. Khai thác than, phát điện, tận dụng——biến Jutsu-sen thành một thị trấn bảo tàng công nghiệp.」
- fix: 「Không chỉ có niềm vui thám hiểm, mà còn thêm cả niềm vui tham quan nhà máy. Khai thác than, phát điện, tận dụng——biến Jutsusen thành một thị trấn bảo tàng công nghiệp.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2174** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「はい、ここのこと。術仙廃炭鉱のことを、です」
- TW: 「沒錯，就是這裡。術仙廢煤礦」
- old_vn: 「Vâng, chuyện về nơi này. Về Mỏ than bỏ hoang Jutsu-sen ạ.」
- fix: 「Vâng, chuyện về nơi này. Về Mỏ than bỏ hoang Jutsusen ạ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2220** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙の町。傷と思われ、閉じ込められてたこの町が。\\nきっと、わたしたちに未来をくれる」
- TW: 「術仙鎮。這個被視為傷痕，被封鎖的城鎮，一定會為我們帶來未來」
- old_vn: 「Thị trấn Jutsu-sen. Thị trấn từng bị coi là vết thương và bị phong kín này. Chắc chắn sẽ mang đến tương lai cho chúng ta.」
- fix: 「Thị trấn Jutsusen. Thị trấn từng bị coi là vết thương và bị phong kín này. Chắc chắn sẽ mang đến tương lai cho chúng ta.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2923** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 夕方の乗務を終えて、もう一度、\\n回送扱いで折り返しての、術仙炭鉱廃駅。
- TW: 結束傍晚的乘務工作後，我們又一次空車返回了術仙煤礦廢車站。
- old_vn: Kết thúc công việc trên tàu buổi chiều, chúng tôi một lần nữa quay lại Ga bỏ hoang Mỏ than Jutsu-sen bằng chuyến xe chạy không.
- fix: Kết thúc công việc trên tàu buổi chiều, chúng tôi một lần nữa quay lại Ga bỏ hoang Mỏ than Jutsusen bằng chuyến xe chạy không.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### グランドリライト05_れいな.txt.toml (8 dòng)

**Key 1894** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T17)
- JP: 「うむ。術仙炭鉱のテーマパーク化の話なのだが――」
- TW: 「嗯，就是把術仙煤礦改造成主題公園的事情……」
- old_vn: 「Ừm. Chuyện biến mỏ than Jussen thành công viên chủ đề ấy——」
- fix: 「Ừm. Chuyện biến mỏ than Jutsusen thành công viên chủ đề ấy——」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2032** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙という街をテーマパークにしたいのだがな、\\nその街自体が、御一夜に昔から暮らす人々の傷なのだ」
- TW: 「我想把一個叫術仙的小鎮改造成主題公園，但那小鎮對一直住在御一夜的人來說是個傷痕」
- old_vn: 「Anh muốn biến khu phố tên Jussen thành công viên chủ đề,\\nnhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohitoyo từ ngày xưa.」
- fix: 「Anh muốn biến khu phố tên Jutsusen thành công viên chủ đề,\\nnhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohitoyo từ ngày xưa.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2326** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T17)
- JP: 「ならば、れいなの空き時間に僕があわせよう。\\nできるだけ早く、ふたりで術仙廃炭鉱を視察しよう」
- TW: 「那就看你哪天有空吧。我們儘早一起去術仙廢煤礦轉一轉」
- old_vn: 「Vậy thì, anh sẽ sắp xếp theo thời gian rảnh của Reina.\\nCàng sớm càng tốt, hai chúng ta hãy cùng đi khảo sát mỏ than bỏ hoang Jussen.」
- fix: 「Vậy thì, anh sẽ sắp xếp theo thời gian rảnh của Reina.\\nCàng sớm càng tốt, hai chúng ta hãy cùng đi khảo sát mỏ than bỏ hoang Jutsusen.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2364** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T17)
- JP: 「廃坑道の視察のみならず、発電所の位置まで確認できた。\\n術仙廃炭鉱再活用のための素材は、もう十分だ」
- TW: 「除了察看廢棄坑道之外，我們還確認了發電站的位置。重新利用術仙廢煤礦的素材已經收集夠了」
- old_vn: 「Không chỉ khảo sát đường hầm bỏ hoang, mà còn xác nhận được vị trí của nhà máy điện.\\nTài liệu để tái sử dụng mỏ than bỏ hoang Jussen đã đủ rồi.」
- fix: 「Không chỉ khảo sát đường hầm bỏ hoang, mà còn xác nhận được vị trí của nhà máy điện.\\nTài liệu để tái sử dụng mỏ than bỏ hoang Jutsusen đã đủ rồi.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2606** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: 夕方の乗務を終えて、そのまま回送扱いで\\n術仙炭鉱でおろしてもらって、廃坑道を視察して――
- TW: 傍晚的工作結束後，波萊特又專程空車送我們來到術仙煤礦，讓我們在廢棄坑道裡四下察看了一番。
- old_vn: Sau khi kết thúc ca trực buổi chiều tối, Paulette đã đưa chúng tôi đến mỏ than Jussen\\nbằng xe chạy không, rồi chúng tôi đi khảo sát đường hầm bỏ hoang——
- fix: Sau khi kết thúc ca trực buổi chiều tối, Paulette đã đưa chúng tôi đến mỏ than Jutsusen\\nbằng xe chạy không, rồi chúng tôi đi khảo sát đường hầm bỏ hoang——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2667** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: もしも術仙廃炭鉱が、唯一無二なり、それに近い、\\n『採炭を復活できる炭鉱』という存在であるのなら――
- TW: 如果術仙廢煤礦成為獨一無二或者近乎獨一無二的“可以恢復採煤的煤礦”……
- old_vn: Nếu như mỏ than bỏ hoang Jussen, là độc nhất vô nhị, hoặc gần như thế,\\nlà sự tồn tại của một 『mỏ than có thể khôi phục việc khai thác』——
- fix: Nếu như mỏ than bỏ hoang Jutsusen, là độc nhất vô nhị, hoặc gần như thế,\\nlà sự tồn tại của một 『mỏ than có thể khôi phục việc khai thác』——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2786** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: かつては術仙に関わり、あるいは暮らしていた人たちは、\\nれいなと同じく、さみしい思いを痛みと抱え続けて来た。
- TW: 曾經與術仙有過關聯，或者曾經住在過那裡的人，肯定與玲奈一樣，一直很難過很痛苦。
- old_vn: Những người từng gắn bó với Jussen, hay từng sinh sống ở đó,\\ncũng giống như Reina, đã mang theo nỗi buồn như một vết thương lòng.
- fix: Những người từng gắn bó với Jutsusen, hay từng sinh sống ở đó,\\ncũng giống như Reina, đã mang theo nỗi buồn như một vết thương lòng.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 3046** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: （それまでに、術仙廃炭鉱観光地化議案賛成への票固めを、\\nできれば、採決までを済ませておかねばならない）
- TW: （可以的話，最好能在那之前湊夠術仙廢煤礦旅遊開發議案需要的贊成票）
- old_vn: （Trước lúc đó, việc củng cố phiếu bầu tán thành dự luật biến mỏ than bỏ hoang Jussen thành khu du lịch,\\nnếu có thể, phải hoàn tất cho đến lúc biểu quyết.）
- fix: （Trước lúc đó, việc củng cố phiếu bầu tán thành dự luật biến mỏ than bỏ hoang Jutsusen thành khu du lịch,\\nnếu có thể, phải hoàn tất cho đến lúc biểu quyết.）
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### グランドリライト07_真闇.txt.toml (4 dòng)

**Key 2322** (nhân vật: 日々姫; nguồn old_vn: audit fix; mục: T17)
- JP: 「ん。術仙いって、修理で入ってるこ、描いてくる。\\nそしたら何か、アイディア浮かんでくるかもしれないし」
- TW: 「嗯，我要去術仙把正在修理的列車畫下來。或許能從中找到靈感」
- old_vn: 「Vâng. Em định đến Jutsu-sen, vẽ lại chiếc xe đang được đưa vào sửa chữa.\\nBiết đâu lúc đó sẽ nảy ra ý tưởng gì đó.」
- fix: 「Vâng. Em định đến Jutsusen, vẽ lại chiếc xe đang được đưa vào sửa chữa.\\nBiết đâu lúc đó sẽ nảy ra ý tưởng gì đó.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2559** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「日々姫は確か――そうだ、術仙に向かうといっていた」
- TW: 「日日姬好像——對，她去術仙了」
- old_vn: 「Hình như Hibiki——à đúng rồi, em ấy bảo sẽ đến Jutsu-sen.」
- fix: 「Hình như Hibiki——à đúng rồi, em ấy bảo sẽ đến Jutsusen.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2611** (nhân vật: 日々姫; nguồn old_vn: audit fix; mục: T17)
- JP: 「ボロボロだけど、今の術仙でなら改修できるかもな\\nデゴイチと……\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;も、一応、こころあたりは」
- TW: 「有一輛Ｄ５１型……還有\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，雖然都很破舊，但是現在的術仙應該有能力修好」
- old_vn: 「Có một chiếc D51 tơi tả, nhưng nếu là Jutsu-sen hiện tại thì có thể sửa được.\\nVà……về \\x%lレイルロオド;#00ffc040;Railord%l;#;, em cũng có quen biết một người.」
- fix: 「Có một chiếc D51 tơi tả, nhưng nếu là Jutsusen hiện tại thì có thể sửa được.\\nVà……về \\x%lレイルロオド;#00ffc040;Railord%l;#;, em cũng có quen biết một người.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2848** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「ならば、その方向で術仙側ともつめていこう。\\n可能であれば、さらに余裕を大きなものとできようしな」
- TW: 「那麼就按照這個方向，跟術仙也探討一下吧。如果能辦到的話，我們的調整空間又會增加不少」
- old_vn: 「Vậy thì, chúng ta sẽ bàn bạc với phía Jutsu-sen theo hướng đó.\\nNếu có thể, chúng ta sẽ càng có thêm nhiều không gian hơn.」
- fix: 「Vậy thì, chúng ta sẽ bàn bạc với phía Jutsusen theo hướng đó.\\nNếu có thể, chúng ta sẽ càng có thêm nhiều không gian hơn.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### グランドリライト11_ナインスターズ！.txt.toml (1 dòng)

**Key 3313** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: 日ノ本鉄路・術仙車両工場で、\\n果たして対応しきれるものか、些か不安になる程の――
- TW: 其規模恐怕窮盡日本鐵路、術仙車輛工廠之力，都未必能完全應對。
- old_vn: Đến mức khiến tôi hơi lo lắng, không biết\\nNhà máy chế tạo toa xe Jussen - Đường sắt Hinomoto có thể kham nổi không——
- fix: Đến mức khiến tôi hơi lo lắng, không biết\\nNhà máy chế tạo toa xe Jutsusen - Đường sắt Hinomoto có thể kham nổi không——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ハチロク12_ムナカタ来訪.txt.toml (3 dòng)

**Key 1525** (nhân vật: 宗方; nguồn old_vn: unif (đợt unification đã gộp); mục: T17)
- JP: 「術仙車両工場だけにとどまらず、\\x%l保線;#00ffc040;保線%l;#;についても、\\n御一夜回りに集積させ。言うなら“鉄道の御一夜”と？」
- TW: 「不止術仙車輛工廠，也要將\\x%l保線;#00ffc040;巡線%l;#;相關的產業聚集於御一夜周邊，說白了也就是將御一夜打造為“鐵路之都”？」
- old_vn: 「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsu-sen, mà cả về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, \\ncũng sẽ tập trung xung quanh Ohitoyo. Có thể gọi là 'Ohitoyo của đường sắt' sao?」
- fix: 「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsusen, mà cả về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, \\ncũng sẽ tập trung xung quanh Ohitoyo. Có thể gọi là 'Ohitoyo của đường sắt' sao?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2092** (nhân vật: 稀咲; nguồn old_vn: csv3; mục: T17)
- JP: 「最終的な構想としては、粉蔵、鹿兒島の車両工場を復活。\\n術仙を三拠点の中心にしたい、という絵図面になるね」
- TW: 「而終極理想則是重建小倉和鹿兒島的車輛工廠，並且讓術仙成為這個鐵三角的核心」
- old_vn: 「Tầm nhìn cuối cùng là khôi phục các nhà máy chế tạo toa xe ở Kokura và Kagoshima. \\nJutsu-sen sẽ trở thành trung tâm của ba cứ điểm, đó là bản thiết kế của chúng tôi.」
- fix: 「Tầm nhìn cuối cùng là khôi phục các nhà máy chế tạo toa xe ở Kokura và Kagoshima. \\nJutsusen sẽ trở thành trung tâm của ba cứ điểm, đó là bản thiết kế của chúng tôi.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2191** (nhân vật: オリヴィ; nguồn old_vn: csv3; mục: T17)
- JP: 「\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;！　\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;のケンシューとか\\nケンキューするしせつも、オヒトヨとかジュツセンに！」
- TW: 「還有\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;！包括\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;的檢修，以及研究設施，也全部聚集在御一夜或者術仙多好！」
- old_vn: 「\\x%lレイルロオド;#00ffc040;Railord%l;#;! Cơ sở bảo dưỡng hay nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; \\ncũng nên đặt ở Ohitoyo hoặc Jutsu-sen đi!」
- fix: 「\\x%lレイルロオド;#00ffc040;Railord%l;#;! Cơ sở bảo dưỡng hay nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; \\ncũng nên đặt ở Ohitoyo hoặc Jutsusen đi!」
- Lý do: JP katakana ジュツセン (không có kanji 術仙) — cùng thuật ngữ, "Jutsu-sen" → "Jutsusen".

#### ハチロク12_再開発.txt.toml (7 dòng)

**Key 2016** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱廃駅に降ろして欲しいとの希望だが――\\nまず、その理由を教えて欲しい」
- TW: 「你是要我們帶你到術仙煤礦廢車站去——能先告訴我們理由嗎」
- old_vn: 「Cô muốn chúng tôi đưa đến ga bỏ hoang của mỏ than Jutsu-sen—— Nhưng trước tiên, tôi muốn biết lý do.」
- fix: 「Cô muốn chúng tôi đưa đến ga bỏ hoang của mỏ than Jutsusen—— Nhưng trước tiên, tôi muốn biết lý do.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2098** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「ふむ、術仙炭鉱廃駅どまりか」
- TW: 「唔，到術仙煤礦廢車站啊」
- old_vn: 「Hừm, chỉ đến ga bỏ hoang mỏ than Jutsu-sen thôi sao.」
- fix: 「Hừm, chỉ đến ga bỏ hoang mỏ than Jutsusen thôi sao.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2280** (nhân vật: ハチロク; nguồn old_vn: audit fix; mục: T17)
- JP: 「だとすると――当面の試験区間は、\\n術仙炭鉱廃駅までの往復とすることとなりますか？」
- TW: 「既然這樣，目前需要進行測試的路段，就是到術仙煤礦廢車站的往返路程了吧？」
- old_vn: 「Nếu vậy thì——đoạn đường chạy thử trước mắt, sẽ là chặng khứ hồi đến ga bỏ hoang mỏ than Jutsu-sen đúng không ạ?」
- fix: 「Nếu vậy thì——đoạn đường chạy thử trước mắt, sẽ là chặng khứ hồi đến ga bỏ hoang mỏ than Jutsusen đúng không ạ?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2500** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「だったら、術仙炭鉱駅停車時の各部点検が終わったら、\\n駅舎の調査をしてもらえませんか？」
- TW: 「那索性，在術仙煤礦廢車站停車完成各個部位的清查之後，調查一下車站的情況怎麼樣？」
- old_vn: 「Nếu vậy, sau khi dừng tàu tại ga mỏ than Jutsu-sen và kiểm tra xong các bộ phận, mọi người có thể khảo sát luôn nhà ga được không?」
- fix: 「Nếu vậy, sau khi dừng tàu tại ga mỏ than Jutsusen và kiểm tra xong các bộ phận, mọi người có thể khảo sát luôn nhà ga được không?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2508** (nhân vật: ハチロク; nguồn old_vn: unification-merged (U4); mục: T17+T7)
- JP: 「術仙炭鉱廃駅どまりだと、[ゆのい,1]湯医まで行っての折り返しと、\\n後進で御一夜まで戻るのと……いずれがよろしいかと」
- TW: 「開到術仙煤礦廢車站之後，是索性開到湯醫後折返，還是倒車返回御一夜……哪種方法更合適」
- old_vn: 「Nếu chỉ đến ga bỏ hoang mỏ than Jutsu-sen, thì nên chạy tiếp đến Yunoi rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」
- fix: 「Nếu chỉ đến ga bỏ hoang mỏ than Jutsusen, thì nên chạy tiếp đến Yunoi rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2515** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「かつて、術仙炭鉱が栄えていた――\\nということの現れなのであろうがな」
- TW: 「雖然這也是體現了術仙煤礦曾經的繁榮吧」
- old_vn: 「Có lẽ đây là minh chứng cho việc—— mỏ than Jutsu-sen từng một thời hưng thịnh.」
- fix: 「Có lẽ đây là minh chứng cho việc—— mỏ than Jutsusen từng một thời hưng thịnh.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 3070** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 試験区間は徐々に伸ばしていくべきだし、\\n術仙炭鉱廃駅までなら、ちょうど手頃だ。
- TW: 測試路段應該是逐步延長的，到術仙煤礦廢車站的距離正合適。
- old_vn: Đoạn đường chạy thử nên được kéo dài dần dần, đến ga bỏ hoang mỏ than Jutsu-sen là vừa đẹp.
- fix: Đoạn đường chạy thử nên được kéo dài dần dần, đến ga bỏ hoang mỏ than Jutsusen là vừa đẹp.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ハチロク14_橋.txt.toml (1 dòng)

**Key 2258** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: はっきりとしたハチロクの\\x%l喚呼;#00ffc040;喚呼%l;#;が気合を新たにしてくれる。\\n術仙炭鉱廃駅までを安全に乗り切るために――
- TW: 八六吐字清晰的\\x%l喚呼;#00ffc040;復誦%l;#;讓我鼓足了幹勁。為了安全到達術仙煤礦廢車站——
- old_vn: Tiếng \\x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới.\\nĐể vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsu-sen một cách an toàn——
- fix: Tiếng \\x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới.\\nĐể vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsusen một cách an toàn——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット02_古地図.txt.toml (11 dòng)

**Key 1683** (nhân vật: 日々姫; nguồn old_vn: audit fix; mục: T17)
- JP: 「行くんですか？　兄さん。\\n術仙炭鉱跡の調査に」
- TW: 「哥哥，你要去調查那個術仙廢煤礦嗎？」
- old_vn: 「Anh định đi sao? Anh trai.↵Đi điều tra tàn tích Mỏ than Jutsu-sen ấy.」
- fix: 「Anh định đi sao? Anh trai.↵Đi điều tra tàn tích Mỏ than Jutsusen ấy.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1719** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「あ、それは術仙炭鉱の廃駅前からです。\\n遠足のときだけは、臨時停車することになってて」
- TW: 「啊，是從術仙煤礦廢車站那裡。只有去遠足的時候能臨時在那裡停車」
- old_vn: 「A, là từ trước nhà ga Mỏ than Jutsu-sen bị bỏ hoang ạ.↵Chỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」
- fix: 「A, là từ trước nhà ga Mỏ than Jutsusen bị bỏ hoang ạ.↵Chỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1725** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「うむ。術仙炭鉱跡の周辺に、\\nそうした何かが残ってないか、誰かもしも」
- TW: 「嗯。有人知道術仙廢煤礦周圍的鐵路還有留下來嗎」
- old_vn: 「Ừm. Xung quanh tàn tích Mỏ than Jutsu-sen,↵có ai biết liệu còn sót lại thứ gì như vậy không.」
- fix: 「Ừm. Xung quanh tàn tích Mỏ than Jutsusen,↵có ai biết liệu còn sót lại thứ gì như vậy không.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1856** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「近くに無くても奥ならどうだ？\\n術仙炭鉱までにレールは、残ってないのか？」
- TW: 「既然廢車站那裡沒有，那深處呢？現在還有通向術仙煤礦的鐵軌嗎？」
- old_vn: 「Gần đó không có, nhưng ở sâu bên trong thì sao?↵Đường ray đến tận Mỏ than Jutsu-sen, chẳng lẽ không còn sót lại chút nào sao?」
- fix: 「Gần đó không có, nhưng ở sâu bên trong thì sao?↵Đường ray đến tận Mỏ than Jutsusen, chẳng lẽ không còn sót lại chút nào sao?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1858** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「宿舎がいっぱい、というほどの規模なら、\\n術仙炭鉱は産出量に恵まれていたのかな？」
- TW: 「既然有那麼多礦工居住的宿舍，也就是說術仙煤礦曾經產量很高囉？」
- old_vn: 「Nếu quy mô đến mức có nhiều khu nhà ở,↵thì sản lượng của Mỏ than Jutsu-sen chắc phải cao lắm nhỉ?」
- fix: 「Nếu quy mô đến mức có nhiều khu nhà ở,↵thì sản lượng của Mỏ than Jutsusen chắc phải cao lắm nhỉ?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2052** (nhân vật: 真闇; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱のあたりには、宿舎がいっぱい建っとったんよ。\\nさぞや栄えとったんろーねぇ」
- TW: 「術仙煤礦那裡曾經建了好多居住區。當年肯定非常繁榮吧」
- old_vn: 「Quanh Mỏ than Jutsu-sen, người ta xây nhiều khu nhà ở lắm.↵Chắc hẳn ngày xưa sầm uất lắm nhỉ.」
- fix: 「Quanh Mỏ than Jutsusen, người ta xây nhiều khu nhà ở lắm.↵Chắc hẳn ngày xưa sầm uất lắm nhỉ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2136** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「もう、とっくの昔に廃線されてますよ？\\n術仙炭鉱廃駅の近くに、そんな設備は」
- TW: 「那裡可是早就已經廢線了呀？術仙煤礦廢車站那裡已經沒有相應設備了」
- old_vn: 「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?↵Gần nhà ga Mỏ than Jutsu-sen bị bỏ hoang, làm gì còn thiết bị nào...」
- fix: 「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?↵Gần nhà ga Mỏ than Jutsusen bị bỏ hoang, làm gì còn thiết bị nào...」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2394** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 凪の言葉を因数分解すれば、\\n“術仙炭鉱跡＝（遠い+汚い）×２”ということになる。
- TW: 因式分解一下凪的話，就是“術仙廢煤礦＝（遠＋髒）ｘ２”。
- old_vn: Nếu phân tích nhân tử lời của Nagi,↵thì sẽ thành 'Tàn tích Mỏ than Jutsu-sen = (Xa + Bẩn) x 2'.
- fix: Nếu phân tích nhân tử lời của Nagi,↵thì sẽ thành 'Tàn tích Mỏ than Jutsusen = (Xa + Bẩn) x 2'.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2414** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 言われてみれば、術仙炭鉱駅から\\n術仙洞の文字の上、鉱山の地図記号へと、線がある。
- TW: 她這麼一指，我發現從術仙煤礦站到術仙洞幾個字上面的礦山地圖符號之間有一條線連接著。
- old_vn: Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jutsu-sen↵đến ký hiệu bản đồ mỏ phía trên chữ Jutsusendo, có một đường kẻ.
- fix: Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jutsusen↵đến ký hiệu bản đồ mỏ phía trên chữ Jutsusendo, có một đường kẻ.
- Lý do: Chỉ lật "Jutsu-sen" (術仙炭鉱) → "Jutsusen"; "Jutsusendo" (術仙洞) trong cùng dòng GIỮ NGUYÊN.

**Key 2670** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 恐らくは術仙炭鉱跡。\\n老朽化が、急速に進んでしまっているのだ。
- TW: 術仙廢煤礦的老化正在以極快的速度進行著。
- old_vn: Có lẽ là tàn tích Mỏ than Jutsu-sen.↵Sự xuống cấp đang diễn ra với tốc độ chóng mặt.
- fix: Có lẽ là tàn tích Mỏ than Jutsusen.↵Sự xuống cấp đang diễn ra với tốc độ chóng mặt.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2747** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 線路は、上質の鉄材だ。誰かが、恐らくは持ち去っている。\\nが、術仙炭鉱付近は\\x%lエアクラ;#00ffc040;エアクラ%l;#;の作動不能地帯――
- TW: 鐵軌都是用的上等鋼鐵鋪設，一般來說廢線後都會被人拿走。不過術仙煤礦附近是無法使用\\x%lエアクラ;#00ffc040;空凝機%l;#;的——
- old_vn: Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.↵Nhưng khu vực Mỏ than Jutsu-sen là vùng cấm hoạt động của \\x%lエアクラ;#00ffc040;Aircra%l;#;——
- fix: Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.↵Nhưng khu vực Mỏ than Jutsusen là vùng cấm hoạt động của \\x%lエアクラ;#00ffc040;Aircra%l;#;——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット03_廃炭鉱.txt.toml (6 dòng)

**Key 1656** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「つまりその場合、術仙炭鉱廃駅付近での非常停車時には、\\n日々姫が、廃駅まで歩けばいいだけの話になるのか」
- TW: 「也就是說假如真發生了那種情況的話，日日姬只要步行走到廢車站就行了」
- old_vn: 「Nói cách khác, trong trường hợp đó, khi phải dừng khẩn cấp gần ga bỏ hoang mỏ than Jutsu-sen, chỉ cần Hibiki đi bộ đến ga bỏ hoang là xong, phải không?」
- fix: 「Nói cách khác, trong trường hợp đó, khi phải dừng khẩn cấp gần ga bỏ hoang mỏ than Jutsusen, chỉ cần Hibiki đi bộ đến ga bỏ hoang là xong, phải không?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1723** (nhân vật: ポーレット; nguồn old_vn: unification-merged (U4); mục: T17+T7)
- JP: 「よほどの悪天候でも無い限り、湯医線沿線で\\n電波が通じないのは、術仙炭鉱廃駅付近だけです」
- TW: 「只要不是氣象條件特別惡劣，整條湯醫線沒有信號的地方就只有術仙煤礦廢車站附近了」
- old_vn: 「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yunoi, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsu-sen thôi.」
- fix: 「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yunoi, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsusen thôi.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2003** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「ポーレット。できれば日々姫に、術仙炭鉱駅への\\n臨時停車の手本を見せてやってはくれぬか？」
- TW: 「波萊特，不如你給日日姬示範一下怎麼在術仙煤礦站臨時停車可以嗎？」
- old_vn: 「Paulette. Nếu được, em có thể cho Hibiki xem mẫu cách dừng tạm thời ở ga mỏ than Jutsu-sen không?」
- fix: 「Paulette. Nếu được, em có thể cho Hibiki xem mẫu cách dừng tạm thời ở ga mỏ than Jutsusen không?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2052** (nhân vật: 双鉄; nguồn old_vn: csv3; mục: T17)
- JP: 「\\x%l8620;#00ffc040;8620%l;#;でここまで、あるいは術仙炭鉱廃駅まで来て、\\nここで、石炭を体験採掘してもらう」
- TW: 「讓\\x%l8620;#00ffc040;８６２０%l;#;載著乘客到這裡或者是術仙煤礦廢車站，然後讓他們在這裡體驗挖掘煤炭」
- old_vn: 「Đi \\x%l8620;#00ffc040;8620%l;#; đến tận đây, hoặc đến nhà ga bỏ hoang của mỏ than Jutsu-sen,\\nrồi cho mọi người trải nghiệm khai thác than ở đây.」
- fix: 「Đi \\x%l8620;#00ffc040;8620%l;#; đến tận đây, hoặc đến nhà ga bỏ hoang của mỏ than Jutsusen,\\nrồi cho mọi người trải nghiệm khai thác than ở đây.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2083** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「これが、術仙炭鉱廃駅か」
- TW: 「這就是術仙煤礦廢車站啊」
- old_vn: 「Đây là…… ga bỏ hoang mỏ than Jutsu-sen sao.」
- fix: 「Đây là…… ga bỏ hoang mỏ than Jutsusen sao.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2895** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 正\\x%l運転士;#00ffc040;運転士%l;#;を欠いた上、\\n常には行わぬ術仙炭鉱廃駅停車を控えている。
- TW: 這次不光沒有正式\\x%l運転士;#00ffc040;駕駛員%l;#;，還要在平時直接通過的術仙煤礦廢車站停車。
- old_vn: Đã thiếu một \\x%l運転士;#00ffc040;lái tàu%l;#; chính thức, lại còn sắp phải dừng ở ga bỏ hoang mỏ than Jutsu-sen, nơi bình thường vẫn chạy thẳng qua.
- fix: Đã thiếu một \\x%l運転士;#00ffc040;lái tàu%l;#; chính thức, lại còn sắp phải dừng ở ga bỏ hoang mỏ than Jutsusen, nơi bình thường vẫn chạy thẳng qua.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット04_ヒヤリング.txt.toml (2 dòng)

**Key 1517** (nhân vật: 双鉄; nguồn old_vn: unif (đợt unification đã gộp); mục: T17)
- JP: 「術仙廃炭鉱の再活用を観光振興と繋げたのなら、\\n御一夜は必ずや、かつてに勝る輝きを得る」
- TW: 「如果能讓術仙廢煤礦的再利用成為旅遊業復興的一環，御一夜肯定能重新獲得不亞於過去的繁榮」
- old_vn: 「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsu-sen với chấn hưng du lịch,\\nthì Ohitoyo chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」
- fix: 「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsusen với chấn hưng du lịch,\\nthì Ohitoyo chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1616** (nhân vật: 宮本; nguồn old_vn: csv3; mục: T17)
- JP: 「次に、術仙炭鉱の件について。\\n炭鉱の所有権、採掘権は、市が譲渡を受けています」
- TW: 「接下來是術仙煤礦一事。原主已將煤礦的所有權、開採權轉讓給市政府」
- old_vn: 「Tiếp theo, về vấn đề mỏ than Jutsu-sen.\\nThành phố đã nhận chuyển nhượng quyền sở hữu và quyền khai thác mỏ than.」
- fix: 「Tiếp theo, về vấn đề mỏ than Jutsusen.\\nThành phố đã nhận chuyển nhượng quyền sở hữu và quyền khai thác mỏ than.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット04_鳴呼いきストーブ列車.txt.toml (1 dòng)

**Key 2696** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 確かにだ。“いつかは父になりたいか？”\\nあの日、術仙炭鉱でのポーレットからの質問は――
- TW: 的確如此。“將來你想當爸爸嗎？”那天，波萊特在術仙煤礦就問過我這個問題。
- old_vn: Đúng là vậy. “Một ngày nào đó anh có muốn trở thành cha không?” Câu hỏi của Paulette vào ngày hôm đó, tại mỏ than Jutsu-sen——
- fix: Đúng là vậy. “Một ngày nào đó anh có muốn trở thành cha không?” Câu hỏi của Paulette vào ngày hôm đó, tại mỏ than Jutsusen——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット06_おひとよマイントレジャー.txt.toml (6 dòng)

**Key 1464** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「……術仙炭鉱にポジションを取った人が――\\n御一夜には、たくさんいる」
- TW: 「……在術仙煤礦這件事上——御一夜有許多人選定了自己的位置」
- old_vn: 「……Những người đã giữ vị thế đối với mỏ than Jutsu-sen――Ở Ohitoyo có rất nhiều」
- fix: 「……Những người đã giữ vị thế đối với mỏ than Jutsusen――Ở Ohitoyo có rất nhiều」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1765** (nhân vật: 日々姫; nguồn old_vn: audit fix; mục: T17)
- JP: 「つまりこれ、術仙廃炭鉱一帯をまるごと、\\n宝探しテーマパークにするってことですよね」
- TW: 「你們就是想把整個術仙廢煤礦一帶打造成尋寶主題公園對吧」
- old_vn: 「Tóm lại là, sẽ biến toàn bộ khu vực mỏ than bỏ hoang Jutsu-sen, thành một công viên chủ đề tìm kho báu đúng không」
- fix: 「Tóm lại là, sẽ biến toàn bộ khu vực mỏ than bỏ hoang Jutsusen, thành một công viên chủ đề tìm kho báu đúng không」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1974** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙廃炭鉱の再調査。\\nれいなにも同行をしてもらいたい」
- TW: 「我們重新去調查術仙廢煤礦。這次我希望玲奈也同行」
- old_vn: 「Điều tra lại mỏ than bỏ hoang Jutsu-sen. Tôi muốn Reina cũng đi cùng」
- fix: 「Điều tra lại mỏ than bỏ hoang Jutsusen. Tôi muốn Reina cũng đi cùng」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2155** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「そうか――そうだな。\\n術仙廃炭鉱は、市の所有地なのだから」
- TW: 「這樣啊——確實沒錯。因為術仙廢煤礦是市政府的所有地」
- old_vn: 「Ra vậy――đúng rồi nhỉ. Vì mỏ than bỏ hoang Jutsu-sen là đất thuộc sở hữu của thành phố mà」
- fix: 「Ra vậy――đúng rồi nhỉ. Vì mỏ than bỏ hoang Jutsusen là đất thuộc sở hữu của thành phố mà」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2704** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: そして、市内から術仙炭鉱には、\\n送電線が伸びてきてなどいないのだから――
- TW: 而御一夜市內並沒有向術仙煤礦架設電線。所以——
- old_vn: Và từ thành phố đến mỏ than Jutsu-sen, không hề có đường dây điện nào kéo tới cả nên――
- fix: Và từ thành phố đến mỏ than Jutsusen, không hề có đường dây điện nào kéo tới cả nên――
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2753** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 術仙炭鉱にかつてポジションを取っていて、\\nそして今、\\x%lエアクラ;#00ffc040;エアクラ%l;#;誘致賛成派の議員は確実にいる。
- TW: 議員之中一定有人在術仙煤礦這件事上選定了位置，並且還是\\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶支持派的一員。
- old_vn: Những nghị viên từng giữ vị thế đối với mỏ than Jutsu-sen, và hiện tại thuộc phe ủng hộ thu hút \\x%lエアクラ;#00ffc040;Aircra%l;#;, chắc chắn là có.
- fix: Những nghị viên từng giữ vị thế đối với mỏ than Jutsusen, và hiện tại thuộc phe ủng hộ thu hút \\x%lエアクラ;#00ffc040;Aircra%l;#;, chắc chắn là có.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット07_支線.txt.toml (2 dòng)

**Key 2311** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 戻りの\\x%l列車;#00ffc040;列車%l;#;を御一夜にまで運んだあとで、\\n\\x%l8620;#00ffc040;8620%l;#;は転車し、術仙洞廃駅で待っててくれる。
- TW: 回程的\\x%l列車;#00ffc040;列車%l;#;會在御一夜放下客人，然後\\x%l8620;#00ffc040;８６２０%l;#;進行轉車，前往術仙煤礦廢車站等我們。
- old_vn: 「Sau khi đưa chuyến tàu chiều về đến Ohitoyo,」
- fix: Sau khi đưa \\x%l列車;#00ffc040;chuyến tàu%l;#; chiều về đến Ohitoyo,\\n\\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsusen.
- Lý do: KHÔI PHỤC (restoration): fix audit đã cắt cụt dòng này chỉ còn nửa đầu ("「Sau khi đưa chuyến tàu chiều về đến Ohitoyo,」") và làm mất nửa sau + tag %l. fix = toàn bộ giá trị CSV3 với "Ohimitera"→"Ohitoyo" (T1, đã gộp) và "Jutsu-sen"→"Jutsusen" (T17); old_vn = fix audit bị cắt cụt.

**Key 2576** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: 術仙炭鉱廃駅周辺――
- TW: 術仙煤礦廢車站——
- old_vn: Khu vực xung quanh nhà ga bỏ hoang mỏ than Jutsu-sen——
- fix: Khu vực xung quanh nhà ga bỏ hoang mỏ than Jutsusen——
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット08_未来へのレール.txt.toml (2 dòng)

**Key 1891** (nhân vật: ふかみ; nguồn old_vn: csv3; mục: T17)
- JP: 「けど、わたしと凪ちゃん、\\n高等部からは[じゅつせん,1]術仙学園に通ったし！　ですっ！」
- TW: 「但是，我和小凪從高中開始就是去術仙學園上的呀！嗯！」
- old_vn: 「Nhưng mà, em và bé Nagi,\\ntừ cấp 3 đã học ở Học viện Jutsu-sen rồi! Dạ!」
- fix: 「Nhưng mà, em và bé Nagi,\\ntừ cấp 3 đã học ở Học viện Jutsusen rồi! Dạ!」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2881** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: そうだった。\\nマイントレジャーとともに、廃校から復活した術仙学園。
- TW: 對啊。曾經廢校的術仙學園借煤探樂園的東風復活了。
- old_vn: Đúng rồi.\\nCùng với Mine Treasure, Học viện Jutsu-sen đã hồi sinh từ một ngôi trường bị bỏ hoang.
- fix: Đúng rồi.\\nCùng với Mine Treasure, Học viện Jutsusen đã hồi sinh từ một ngôi trường bị bỏ hoang.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット08_線から面へ.txt.toml (1 dòng)

**Key 1744** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱廃駅と鉱山鉄道とを復活させ、\\nまずは、その区間を\\x%lキハ07;#00ffc040;キハ07%l;#;に案内してもらう」
- TW: 「讓術仙煤礦廢車站與礦山鐵路復活，然後先讓\\x%lキハ07;#00ffc040;Ｋｉｈａ０７%l;#;來跑這一路段」
- old_vn: 「Phục sinh nhà ga bỏ hoang mỏ than Jutsu-sen và tuyến đường sắt mỏ, trước tiên, hãy để \\x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」
- fix: 「Phục sinh nhà ga bỏ hoang mỏ than Jutsusen và tuyến đường sắt mỏ, trước tiên, hãy để \\x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット09_ストーブ客車.txt.toml (6 dòng)

**Key 1368** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: ……質問時間を、まるで気にしていないようだ。\\n関原議員は淡々と、術仙炭鉱の歴史を語る。
- TW: ……關原議員彷彿毫不在意提問時間的限制，將術仙煤礦的歷史悠悠道來。
- old_vn: "...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi. Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jutsu-sen."
- fix: "...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi. Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jutsusen."
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1892** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「わしらね、市長。術仙炭鉱で昔働いていたとですよ」
- TW: 「市長啊，我們以前就在術仙煤礦工作」
- old_vn: 「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jutsu-sen đấy.」
- fix: 「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jutsusen đấy.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2048** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「そう。そして旧術仙炭鉱の現所有者は御一夜市であり、\\n補助金制度はまだ生きている」
- TW: 「沒錯。而且現在舊術仙煤礦的所有者是御一夜市，補助金制度還存在著」
- old_vn: 「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jutsu-sen cũ là thành phố Ohitoyo, và chế độ trợ cấp vẫn còn hiệu lực.」
- fix: 「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jutsusen cũ là thành phố Ohitoyo, và chế độ trợ cấp vẫn còn hiệu lực.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2081** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「採炭ば、国の基幹産業の一つと言われておりましてな。\\n[じゅつせん,1]術仙は、その中でも十指に入る、優良炭鉱だったとです」
- TW: 「煤礦在當時是國家的基礎產業之一。術仙煤礦在整個國家的煤礦中也是屈指可數的富礦」
- old_vn: 「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước. Jutsu-sen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」
- fix: 「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước. Jutsusen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2156** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱の会計資料については、\\nわたしも確認させていただいております」
- TW: 「術仙煤礦的帳目資料我也有確認過」
- old_vn: 「Về các tài liệu kế toán của mỏ than Jutsu-sen, tôi cũng đã xác nhận rồi ạ.」
- fix: 「Về các tài liệu kế toán của mỏ than Jutsusen, tôi cũng đã xác nhận rồi ạ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 2782** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 僕らが想像していたよりも、\\n術仙炭鉱は、はるかに豊かな[やま,1]鉱山だったのだ。
- TW: 看來術仙煤礦曾經比我們想像的還要富有。
- old_vn: Hơn cả những gì chúng tôi từng tưởng tượng, Mỏ than Jutsu-sen đã từng là một mỏ quặng trù phú đến nhường nào.
- fix: Hơn cả những gì chúng tôi từng tưởng tượng, Mỏ than Jutsusen đã từng là một mỏ quặng trù phú đến nhường nào.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット13_再評価.txt.toml (9 dòng)

**Key 1319** (nhân vật: 議長; nguồn old_vn: audit fix; mục: T17)
- JP: 「賛成多数と認め、本案を可決いたします。続いて、\\n『旧術仙炭鉱の技術継承炭鉱としての助成申請案』」
- TW: 「多數人贊成，本議案通過。接著是“原術仙煤礦申請技術繼承煤礦補助金草案”」
- old_vn: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, 『Nghị án xin trợ cấp cho mỏ than cũ Jutsu-sen với tư cách là mỏ than kế thừa kỹ thuật』.」
- fix: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, 『Nghị án xin trợ cấp cho mỏ than cũ Jutsusen với tư cách là mỏ than kế thừa kỹ thuật』.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1320** (nhân vật: 議長; nguồn old_vn: audit fix; mục: T17)
- JP: 「賛成多数と認め、本案を可決いたします。続いて、\\n『マイントレジャーによる術仙炭鉱地域再開発』案」
- TW: 「多數人贊成，本議案通過。接著是“通過煤探樂園進行術仙煤礦再開發草案”」
- old_vn: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, Nghị án 『Tái phát triển khu vực mỏ than Jutsu-sen thông qua Mine Treasure』.」
- fix: 「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, Nghị án 『Tái phát triển khu vực mỏ than Jutsusen thông qua Mine Treasure』.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1353** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「御一夜が術仙炭鉱にどれほど多くを注ぎ込んだか……\\nその誤った判断の、あれは、醜か残りカスたい」
- TW: 「御一夜曾經在術仙煤礦上幾乎投入了一切……那個廢煤礦，正是當初的錯誤判斷所留下的醜陋傷疤」
- old_vn: 「Ohitoyo đã đổ bao nhiêu công sức và của cải vào Mỏ than Jutsu-sen…… Đó là, tàn dư xấu xí của một quyết định sai lầm.」
- fix: 「Ohitoyo đã đổ bao nhiêu công sức và của cải vào Mỏ than Jutsusen…… Đó là, tàn dư xấu xí của một quyết định sai lầm.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1366** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱の再検証なしに\\x%lエアクラ;#00ffc040;エアクラ%l;#;工場を誘致して――\\n目ぇ瞑ったまま、手ば引いてもらおうとしておったのか」
- TW: 「我們竟沒有重新審查術仙煤礦的可能性，就決定支持\\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶——簡直就是閉著眼睛，讓人牽著走啊」
- old_vn: 「Mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà không hề kiểm chứng lại Mỏ than Jutsu-sen―― Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」
- fix: 「Mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà không hề kiểm chứng lại Mỏ than Jutsusen―― Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1422** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「石炭需要がのうなったと、そいば打ち切られたとき。\\n術仙炭鉱の命脈もまた、尽きたとです」
- TW: 「當不需要煤礦的時候，國家馬上就收回了援助。術仙煤礦的命運也止步於此」
- old_vn: 「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt. Mệnh mạch của Mỏ than Jutsu-sen cũng theo đó mà cạn kiệt.」
- fix: 「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt. Mệnh mạch của Mỏ than Jutsusen cũng theo đó mà cạn kiệt.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1446** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱にはまだ多くの石炭が眠り。\\nそれだけにとどまらぬ、無数の価値が眠っているのです」
- TW: 「術仙煤礦現在煤礦儲量還很豐富。不僅如此，還有著很多可供開發的地方」
- old_vn: 「Mỏ than Jutsu-sen vẫn còn rất nhiều than đá đang ngủ yên. Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」
- fix: 「Mỏ than Jutsusen vẫn còn rất nhiều than đá đang ngủ yên. Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1447** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱は、廃坑のぎりぎりまで設備投資と\\n技術練磨とを惜しまなかった」
- TW: 「術仙煤礦直到被廢棄的前一刻也在不惜成本進行設備投資和技術培訓」
- old_vn: 「Mỏ than Jutsu-sen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị và mài giũa kỹ thuật.」
- fix: 「Mỏ than Jutsusen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị và mài giũa kỹ thuật.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1448** (nhân vật: ポーレット; nguồn old_vn: audit fix; mục: T17)
- JP: 「術仙炭鉱の再評価は、第三者によって行われるべきです。\\n国により、観光客により、若者により」
- TW: 「術仙煤礦需要由第三者來重新評價。由國家、遊客、還有年輕人們」
- old_vn: 「Việc đánh giá lại Mỏ than Jutsu-sen nên được thực hiện bởi bên thứ ba. Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」
- fix: 「Việc đánh giá lại Mỏ than Jutsusen nên được thực hiện bởi bên thứ ba. Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

**Key 1477** (nhân vật: 老議員; nguồn old_vn: audit fix; mục: T17)
- JP: 「旧術仙炭鉱も、助成金を頼りに運営されていたことを、\\n知っておられますか」
- TW: 「那您知道舊術仙煤礦曾經也是依靠補助金運營的事吧」
- old_vn: 「Thị trưởng có biết rằng Mỏ than Jutsu-sen cũ cũng từng được vận hành dựa vào tiền trợ cấp không?」
- fix: 「Thị trưởng có biết rằng Mỏ than Jutsusen cũ cũng từng được vận hành dựa vào tiền trợ cấp không?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット14_ふたたび走り出すために.txt.toml (1 dòng)

**Key 2462** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T17)
- JP: 術仙炭鉱の技術継承炭鉱の認可。\\n赤井阿蘇神社の文化財指定。
- TW: 術仙煤礦的技術繼承煤礦認定，以及赤井阿蘇神社的文化財產指定。
- old_vn: 「Công nhận mỏ than Jutsu-sen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.」
- fix: 「Công nhận mỏ than Jutsusen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット15_求人難.txt.toml (1 dòng)

**Key 1796** (nhân vật: 双鉄; nguồn old_vn: audit fix; mục: T17)
- JP: 「炭鉱、技術者さんたちの――\\nかつて、術仙炭鉱で働いていた」
- TW: 「曾就職於術仙煤礦的技工名單」
- old_vn: 「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsu-sen.」
- fix: 「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsusen.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレット16_明日へのレール.txt.toml (1 dòng)

**Key 2252** (nhân vật: 経産大臣; nguồn old_vn: audit fix; mục: T17)
- JP: 「もちろん結構ですとも。[じゅつせん,1]術仙技術継承炭鉱には、\\n今後大いに発展してもらわねばなりませんからな」
- TW: 「當然沒有意見。我可是對術仙技術繼承煤礦今後的發展寄予厚望的」
- old_vn: 「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsu-sen, từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」
- fix: 「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsusen, từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### ポーレットh8_気動車の国のアリス.txt.toml (1 dòng)

**Key 3601** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: 術仙炭鉱もそうだった。\\n思い返せば、腑に落ちる。
- TW: 術仙煤礦也是一樣的。想到這個，我就沉著了下來。
- old_vn: Mỏ than Jutsu-sen cũng vậy.\\nNgẫm lại thì, cũng dễ hiểu thôi.
- fix: Mỏ than Jutsusen cũng vậy.\\nNgẫm lại thì, cũng dễ hiểu thôi.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### 共通02_日々姫と真闇と人形と.txt.toml (1 dòng)

**Key 2323** (nhân vật: 日々姫; nguồn old_vn: audit fix; mục: T17)
- JP: 「なか……んっ、無いと思います、兄さん。\\nですが、ひょっとすると[じゅつせんどう,2]術仙洞に」
- TW: 「沒……嗯，應該是沒有，哥哥。但是，說不定在術仙洞有」
- old_vn: 「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jutsu-sendo lại có.」
- fix: 「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jutsusendo lại có.」
- Lý do: JP [じゅつせんどう,2]術仙洞 — "Jutsu-sendo" → "Jutsusendo" (lật phần "Jutsu-sen" theo T17).

#### 共通04_キハ07。ポーレットとれいな.txt.toml (1 dòng)

**Key 3097** (nhân vật: monologue; nguồn old_vn: csv3; mục: T17)
- JP: 僕が\\x%lエアクラ;#00ffc040;エアクラ%l;#;で術仙炭鉱跡へ行こうとしたときに、\\n日々姫の声が、なにやら追いかけていたことを。
- TW: 我準備坐\\x%lエアクラ;#00ffc040;空凝機%l;#;去術仙廢煤礦的時候，日日姬似乎想說什麼。
- old_vn: Khi tôi định đến khu tàn tích mỏ than Jussen bằng \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ntiếng của Hibiki dường như đã đuổi theo tôi để nói gì đó.
- fix: Khi tôi định đến khu tàn tích mỏ than Jutsusen bằng \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ntiếng của Hibiki dường như đã đuổi theo tôi để nói gì đó.
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

#### 共通10_クマ川くだりで見る景色.txt.toml (1 dòng)

**Key 2771** (nhân vật: ハチロク; nguồn old_vn: audit fix; mục: T17)
- JP: 「[じゅつせんはいたんこう,4]術仙廃炭鉱でしたか。あの近く――\\n\\x%lエアクラ;#00ffc040;エアクラ%l;#;が使えなくなる場所を通るのですね？」
- TW: 「那裡有術仙廢煤礦呀。是為了通過那一段\\x%lエアクラ;#00ffc040;空凝機%l;#;無法使用的道路對吧？」
- old_vn: 「Mỏ than bỏ hoang Jutsu-sen phải không ạ. Gần đó――\\nlà đi qua khu vực không thể sử dụng \\x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」
- fix: 「Mỏ than bỏ hoang Jutsusen phải không ạ. Gần đó――\\nlà đi qua khu vực không thể sử dụng \\x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」
- Lý do: JP chứa 術仙 → "Jutsusen" đúng, không gạch nối (T17, quyết 21/11 ~17:30, Muse theo ủy quyền).

### T18. 乗務鞄 / 運転鞄 / 運転士鞄 → "túi công tác" — 16 dòng

#### グランドリライト06_稀咲.txt.toml (5 dòng)

**Key 2935** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: 大切そうに、愛おしそうに、運転鞄を抱きしめて。
- TW: 他抱緊了旁邊的駕駛包，那神情就如懷抱著至寶一般。
- old_vn: Ông đang ôm chặt chiếc túi phi hành đoàn một cách trân trọng và đầy yêu thương.
- fix: Ông đang ôm chặt chiếc túi công tác một cách trân trọng và đầy yêu thương.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

**Key 2937** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: 傍らに置いた運転鞄を優しく撫ぜて、\\nまるで鞄に、言い聞かせてでもいるかのように。
- TW: 他溫柔地撫摸著放在旁邊的駕駛包，簡直就像說給駕駛包聽一樣。
- old_vn: Ông dịu dàng vuốt ve chiếc túi phi hành đoàn đặt bên cạnh,\\nnhư thể đang thì thầm với nó vậy.
- fix: Ông dịu dàng vuốt ve chiếc túi công tác đặt bên cạnh,\\nnhư thể đang thì thầm với nó vậy.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

**Key 3242** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13+T18)
- JP: どころか視線も宮司ではなく、\\nその傍らの、運転鞄に向いている。
- TW: 甚至連視線都沒有朝著赤井宮司，而是看向旁邊的駕駛包。
- old_vn: Thậm chí ánh mắt ông ta cũng không hướng về Akai-guji,\\nmà lại nhìn chằm chằm vào chiếc túi phi hành đoàn bên cạnh.
- fix: Thậm chí ánh mắt ông ta cũng không hướng về đền chủ Akai,\\nmà lại nhìn chằm chằm vào chiếc túi công tác bên cạnh.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai).

**Key 3472** (nhân vật: monologue; nguồn old_vn: unification-merged (U4); mục: T13+T18+T11)
- JP: 包帯で顔をぐるぐるにした運転体の\\x%lレイルロオド;#00ffc040;レイルロオド%l;#;を、\\n赤井宮司が運転鞄からそっと取り出す。
- TW: 赤井宮司從駕駛包裡小心翼翼地拿出一個駕駛體\\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，她的臉上還纏著一圈圈的繃帶。
- old_vn: Akai-guji nhẹ nhàng lấy từ trong chiếc túi phi hành đoàn ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít.
- fix: đền chủ Akai nhẹ nhàng lấy từ trong chiếc túi công tác ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai). "kíp lái" trong cùng dòng là T11 — đã đổi thành "thân vận hành" theo fix U4 đã gộp (ghép bởi điều phối, xem ghi chú cuối REVIEW).

**Key 3540** (nhân vật: monologue; nguồn old_vn: csv3; mục: T13+T18)
- JP: 運転鞄からの突然の声にも、赤井宮司は動じない。\\nニイロクと――鞄に向けて呼びかけて。
- TW: 駕駛包突然發出聲音，赤井宮司卻完全不感到驚訝。而且……他把駕駛包稱作“二六”。
- old_vn: Dù giọng nói bất ngờ phát ra từ chiếc túi phi hành đoàn, Akai-guji vẫn không hề nao núng.\\nÔng gọi Niiroku――hướng về phía chiếc túi.
- fix: Dù giọng nói bất ngờ phát ra từ chiếc túi công tác, đền chủ Akai vẫn không hề nao núng.\\nÔng gọi Niiroku――hướng về phía chiếc túi.
- Lý do: Dòng 2 mục: T13 "Akai-guji" → "đền chủ Akai" + T18 "túi phi hành đoàn" → "túi công tác" (một entry duy nhất, fix gộp cả hai).

#### ハチロク13_夜の嵐.txt.toml (2 dòng)

**Key 2555** (nhân vật: monologue; nguồn old_vn: unification-merged (U4); mục: T18+T11)
- JP: \\x%l運転体;#00ffc040;運転体%l;#;を\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;に大事にしまい、\\nさて――と立っても、まだハチロクは立ち上がらない。
- TW: 我把\\x%l運転体;#00ffc040;駕駛體%l;#;小心翼翼地收入\\x%l乗務鞄;#00ffc040;乘務包%l;#;中。站了起來——但是八六並沒有隨我起身。
- old_vn: Tôi cất cẩn thận \\x%l運転体;#00ffc040;thân vận hành%l;#; vào \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên.
- fix: Tôi cất cẩn thận \\x%l運転体;#00ffc040;thân vận hành%l;#; vào \\x%l乗務鞄;#00ffc040;túi công tác%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

**Key 2559** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: ハチロクをキャブに引っ張り上げる。\\nすぐさま、\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;をあける。
- TW: 我把八六拉進了駕駛室，然後迅速打開了\\x%l乗務鞄;#00ffc040;乘務包%l;#;。
- old_vn: Tôi kéo Hachiroku lên buồng lái.\\nNgay lập tức, mở \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; ra.
- fix: Tôi kéo Hachiroku lên buồng lái.\\nNgay lập tức, mở \\x%l乗務鞄;#00ffc040;túi công tác%l;#; ra.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

#### ポーレット11_記憶と記録.txt.toml (3 dòng)

**Key 2511** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: 元\\x%l運転士;#00ffc040;運転士%l;#;である赤井宮司の居室にいつも、\\n鎮座ましましている\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;。
- TW: 身為前\\x%l運転士;#00ffc040;駕駛員%l;#;的赤井宮司，他的起居室裡一直擺放著一個\\x%l乗務鞄;#00ffc040;乘務包%l;#;。
- old_vn: Chiếc \\x%l乗務鞄;#00ffc040;cặp lái tàu%l;# vẫn luôn chễm chệ\\ntrong phòng khách của cựu \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#, Đại tư tế Akai.
- fix: Chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;# vẫn luôn chễm chệ\\ntrong phòng khách của cựu \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#, Đại tư tế Akai.
- Lý do: "cặp lái tàu" nằm trong gloss %l của 乗務鞄 — đổi gloss, giữ nguyên tag JP và phần còn lại ("Đại tư tế Akai" là dạng khác, không thuộc T13 — xem §5).

**Key 2524** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: 赤井宮司の、\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;のその内側から。
- TW: 這聲音來自於赤井宮司的\\x%l乗務鞄;#00ffc040;乘務包%l;#;之中。
- old_vn: Phát ra từ bên trong,\\nchiếc \\x%l乗務鞄;#00ffc040;cặp lái tàu%l;# của Đại tư tế Akai.
- fix: Phát ra từ bên trong,\\nchiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;# của Đại tư tế Akai.
- Lý do: "cặp lái tàu" nằm trong gloss %l của 乗務鞄 — đổi gloss.

**Key 2615** (nhân vật: monologue; nguồn old_vn: csv3; mục: T18)
- JP: （運転鞄を――よかった、お連れくださっている）
- TW: （駕駛包——太好了，他帶來了）
- old_vn: （Chiếc cặp lái tàu――may quá, ông ấy có mang theo.）
- fix: （Chiếc túi công tác――may quá, ông ấy có mang theo.）
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

#### ポーレット13_再評価.txt.toml (1 dòng)

**Key 1641** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T18)
- JP: ハチロク、日々姫、れいな、ふかみと凪はもちろん、\\n真闇姉に蓑笠老人――赤井宮司に、\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;の姿まである。
- TW: 八六、日日姬、玲奈、深美還有凪自不必說，甚至真闇姐和蓑笠爺爺、赤井宮司，還有他的\\x%l乗務鞄;#00ffc040;乘務包%l;#;也在。
- old_vn: Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói, cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \\x%l乗務鞄;#00ffc040;cặp lái tàu%l;#; cũng có mặt.
- fix: Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói, cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;#; cũng có mặt.
- Lý do: "cặp lái tàu" nằm trong gloss %l của 乗務鞄 — đổi gloss.

#### 共通08_傷跡.txt.toml (4 dòng)

**Key 1485** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T18)
- JP: 「\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;は、わたくしの寝台にして家のようなもの。\\n双鉄様に肌身離さずお持ち頂けましたら嬉しく思います」
- TW: 「\\x%l乗務鞄;#00ffc040;乘務包%l;#;就像是我的床和家一樣。希望雙鐵少爺您能隨身攜帶著它」
- old_vn: 「\\x%l乗務鞄;#00ffc040;Túi phi hành đoàn%l;#; giống như giường ngủ và cũng là ngôi nhà của em vậy.\\nEm sẽ rất vui nếu ngài Soutetsu luôn mang theo nó bên mình ạ.」
- fix: 「\\x%l乗務鞄;#00ffc040;Túi công tác%l;#; giống như giường ngủ và cũng là ngôi nhà của em vậy.\\nEm sẽ rất vui nếu ngài Soutetsu luôn mang theo nó bên mình ạ.」
- Lý do: Gloss %l ở đầu câu — giữ chữ hoa đầu câu: "Túi công tác" (các gloss giữa câu khác dùng "túi công tác" thường).

**Key 1486** (nhân vật: ハチロク; nguồn old_vn: audit fix; mục: T18)
- JP: 「\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;の中には、運転[ボディ]体が収まるようになっています」
- TW: 「\\x%l乗務鞄;#00ffc040;乘務包%l;#;裡面，剛好可以放下駕駛體」
- old_vn: 「Bên trong \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; được thiết kế để vừa vặn chứa thân vận hành ạ.」
- fix: 「Bên trong \\x%l乗務鞄;#00ffc040;túi công tác%l;#; được thiết kế để vừa vặn chứa thân vận hành ạ.」
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

**Key 2088** (nhân vật: ハチロク; nguồn old_vn: csv3; mục: T18)
- JP: 「双鉄様は、これを。\\n\\x%l乗務鞄;#00ffc040;[じょうむかばん,2]乗務鞄%l;#;と呼ばれるものです」
- TW: 「雙鐵少爺，請收下這個。這個東西叫做\\x%l乗務鞄;#00ffc040;乘務包%l;#;」
- old_vn: 「Ngài Soutetsu, xin hãy nhận lấy cái này.\\nNó được gọi là \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; ạ.」
- fix: 「Ngài Soutetsu, xin hãy nhận lấy cái này.\\nNó được gọi là \\x%l乗務鞄;#00ffc040;túi công tác%l;#; ạ.」
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

**Key 2692** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T18)
- JP: \\x%l乗務鞄;#00ffc040;乗務鞄%l;#;のずっしりとした重さに比べ、\\nあまりに軽かった\\x%l運転体;#00ffc040;運転体%l;#;。
- TW: 與\\x%l乗務鞄;#00ffc040;乘務包%l;#;的沉重比起來，\\x%l運転体;#00ffc040;駕駛體%l;#;實在是顯得太輕了。
- old_vn: So với độ nặng trịch của \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#;,\\nthì \\x%l運転体;#00ffc040;thân vận hành%l;#; lại quá đỗi nhẹ nhàng.
- fix: So với độ nặng trịch của \\x%l乗務鞄;#00ffc040;túi công tác%l;#;,\\nthì \\x%l運転体;#00ffc040;thân vận hành%l;#; lại quá đỗi nhẹ nhàng.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

#### 共通10_クマ川くだりで見る景色.txt.toml (1 dòng)

**Key 3005** (nhân vật: monologue; nguồn old_vn: audit fix; mục: T18)
- JP: ハチロクの依頼どおり、\\x%l乗務鞄;#00ffc040;乗務鞄%l;#;は肌身離さず扱っている。\\n中にはもちろん、\\x%l運転体;#00ffc040;運転体%l;#;だ。
- TW: 依照八六的要求，我隨身攜帶著\\x%l乗務鞄;#00ffc040;乘務包%l;#;。裡面裝著的自然是\\x%l運転体;#00ffc040;駕駛體%l;#;。
- old_vn: Theo lời nhờ vả của Hachiroku, tôi luôn giữ \\x%l乗務鞄;#00ffc040;túi phi hành đoàn%l;#; khư khư bên mình.\\nBên trong tất nhiên là \\x%l運転体;#00ffc040;thân vận hành%l;#; rồi.
- fix: Theo lời nhờ vả của Hachiroku, tôi luôn giữ \\x%l乗務鞄;#00ffc040;túi công tác%l;#; khư khư bên mình.\\nBên trong tất nhiên là \\x%l運転体;#00ffc040;thân vận hành%l;#; rồi.
- Lý do: JP chứa 乗務鞄/運転鞄/運転士鞄 → "túi công tác" đúng (T18, quyết 20/11 ~19:15, Hieu).

## 5. Dòng đã xem nhưng GIỮ NGUYÊN / flag (không sửa)

### T3 — giữ / flag
- **4 dòng "Đại học Hoàng gia" (帝大 — T5, không thuộc đợt này):** ハチロク11_幽霊 1814, 凪h2_おとなの水着 1759, 稀咲h3 2302, 真闇h3 3299.
- **2 dòng "Trung tâm Hoàng gia" (帝央機関区 — khác 帝鉄, chưa có chuẩn):** ハチロク04_小畑越え 1802 ("Ở Teitetsu cũ, tại kho đầu máy Trung tâm Hoàng gia..."), 仲国05_真夜中の餐車 2032 ("Ở Khu đầu máy Trung tâm Hoàng gia..."). JP 帝央機関区; TW 帝國中央車站/帝都中央車站機務段. Cần một mục riêng cho 帝央機関区 (đề xuất: "Khu đầu máy Teio" theo chuẩn Teitetsu?) — flag cho coordinator, không tự quyết đợt này.
- **8 dòng "Công ty TNHH Đường sắt Hoàng gia" (帝国線路合同会社 — tên công ty, JP không có 帝鉄):** 稀咲03 1637/1899/2321/2349/2377/2478, 稀咲h3 1571/2594. TW 帝國線路有限公司. Cần quyết tên công ty riêng — flag cho coordinator, không tự đổi thành Teitetsu (JP/TW đều không nói 帝鉄).
- **2 dòng 帝有鉄道 (T63 — coordinator đã chốt E1 ngày 22/11 ~11:30, batch khác áp dụng):** 日々姫01_双鉄の妹 1789 ("Đường sắt Hoàng gia Hinomoto" cho 日ノ本帝有鐵道), 日々姫02_文庫森 60 ("Đạo luật Đường sắt Hoàng gia" cho 鉄道帝有法 + "Đường sắt Hoàng gia Hinomoto" cho 日ノ本帝有鉄道). E1 chốt: 帝有鉄道 → "Đường sắt Đế quốc Hinomoto", 鉄道帝有法 → "Đạo luật Đường sắt Đế quốc".
- **グランドリライト10_ハチロク 1134:** "Đường sắt Đế quốc Hinomoto" cho 日ノ本帝有鉄道 — T63/E1, không đụng.
- **共通01_右田双鉄の帰還 1335:** tooltip %l lần xuất hiện đầu, gloss của 帝鉄貨物 — GIỮ NGUYÊN theo T3 (thuộc T4: 帝鉄貨物 → "Vận tải hàng hóa Teitetsu").

### T10 — giữ / flag
- **日々姫11_御一夜モザイク 1774 và 日々姫12_風 2908:** JP chỉ có 毛利の姫 / 毛利の姫様 (không có 電車姫), VN "Denshahime của Mouri" là cách gọi đồng nhất với nhân vật Điện xa công chúa. GIỮ — theo quy tắc "JP không chứa thuật ngữ thì không sửa"; cách gọi này nhất quán với nội dung truyện (P09 2262 xác nhận 電車姫 = chủ Đường sắt điện Mouri). Đổi thành "công chúa nhà Mouri" sẽ làm mất sự đồng nhất đã thiết lập — cần quyết riêng nếu coordinator muốn đổi. (Lưu ý: list ghi "仲国06 2908" là sai nhãn file — dòng này thuộc 日々姫12.)
- **ハチロク10_炙り出し [characters] 2791 "Densha Hime" / [character_subs] 2789 "電車公主" (mục con OPEN của T10):** KHÔNG TÌM THẤY — không có trong CSV3 good-set (đã tìm toàn bộ file, mọi folder) và không có trong TOML-2: file ハチロク10_炙り出し.txt.toml chỉ có 6 key [characters] (2207/2238/2365/2571/2591/2765) và 6 key [character_subs] (2319/2597/2641/2811/2812/2876), không có key 2789/2791 và không có chuỗi "Densha Hime"/"電車公主" nào. Trích dẫn trong list có vẻ đã lỗi thời — không có gì để sửa.
- **84 dòng JP 電車姫 đã là "Công chúa Tàu điện"** — giữ nguyên.

### T13 — giữ / flag
- **ハチロク07_延命 2821:** JP 「グージはミドルネーム？」 — "Guji" ở đây là TÊN (hỏi có phải tên đệm không), không phải 宮司. VN "Guji là tên đệm à?" đúng — GIỮ.
- **14 dòng "thầy tế (Akai)" (P01 1 + P02 13, JP đều có 宮司):** cách diễn khác của 宮司, audit đã giữ. Không thuộc các dạng cũ T13 liệt kê — GIỮ, không tự thống nhất đợt này.
- **25 dòng "Đại tư tế Akai" (P10–P13, JP đều có 宮司):** cách diễn khác ("đại tư tế" = high priest), audit đã giữ nhất quán cả route. Không thuộc các dạng cũ T13 liệt kê — GIỮ, không tự thống nhất đợt này.
- **11 dòng "ông Akai" + 1 dòng "ông" (グランド06 2269) mà JP nói 赤井宮司/宮司 (ハチロク11 ×10, ハチロク13 2684):** lược bỏ chức danh nhưng là cách xưng hô tự nhiên trong lời dẫn, audit đã giữ. Không thuộc các dạng cũ T13 liệt kê — GIỮ; nếu coordinator muốn bắt buộc "đền chủ Akai" ở mọi chỗ thì đó là một mục mới.
- **89 dòng JP 宮司 đã là "đền chủ"** — giữ nguyên.

### T14 — giữ / flag
- **332 dòng "Migita" là họ gia đình (JP 右田 — "nhà Migita", "Migita Hibiki", "Migita Mayami"...):** không phải thực thể xưởng rượu — GIỮ.
- **6 dòng sở hữu "nhà Migita" chỉ xưởng rượu nhưng ở dạng sở hữu:** 仲国06 2347, 日々姫07 1815, 稀咲h3 3664, 凪ふかみ02 1273, 稀咲h3 2111/3478 — GIỮ (xem §3).
- **ふかみh2_homesweethome 1096:** đã là "Migita Ichi" (quyết định 21/11 ~01:55 đã áp dụng trong audit/moan) — giữ nguyên.

### T17 — giữ / flag
- **25 dòng JP 術仙 đã là "Jutsusen"** — giữ nguyên.
- **ポーレット07_支線 2311:** xem §3 (khôi phục — đã nằm trong danh sách sửa).
- **Trích dẫn "Paulette 02 1525" trong list:** không tồn tại — xem §3.

### T18 — giữ / flag
- **9 dòng đã là "túi công tác":** ハチロク03_客車試験 94 (audit đã sửa), ニイロク04_終端 1639/2024/2603, ハチロク09_採決 2672/2899/2900, グランド05_れいな 2814, 凪ふかみ01_流れ 2287 — giữ nguyên.
- **日々姫03_客車手配 2834:** VN "phi hành đoàn" cho JP 乗員 — thuộc **T19** (乗員 → "nhân viên tàu"), không thuộc đợt này.

## 6. Lượt soát 2 (second pass) — TOÀN BỘ fix đối chiếu lại với JP

Đọc lại toàn bộ 240 dòng §4 (JP / TW / old_vn / fix), đối chiếu từng fix với JP của chính dòng đó; đồng thời quét JSON bằng script chỉ để kiểm tra dư lượng dạng cũ và từ lặp (không sửa bằng script).

- **Tổng số dòng đối chiếu: 240**
- **Đối chiếu đúng ngay, giữ nguyên: 237**
- **Loại bỏ: 0**
- **Sửa lại sau lượt soát 2: 3** — đều ở T14, cùng một lỗi: fix viết nhầm "Migita Ichi Ichi". Nguyên nhân: cặp thay thế dạng riêng ("Migita System" → "Migita Ichi", "Migitakazu" → "Migita Ichi") áp dụng trước, rồi cặp chung ("xưởng rượu Migita" → "xưởng rượu Migita Ichi") áp dụng chồng lên kết quả vừa thay, nhân đôi "Ichi". Ba dòng đã sửa đồng bộ ở JSON, §4 (fix + lý do) và khối TOML §7:
  1. ハチロク15a_痛みとの決別 1835 — old_vn "xưởng rượu Migita System" → fix đúng "xưởng rượu Migita Ichi".
  2. 真闇01_再蒸留 2366 — old_vn "xưởng rượu Migitakazu" → fix đúng "xưởng rượu Migita Ichi".
  3. 真闇01_再蒸留 2444 — old_vn "xưởng rượu Migitakazu" → fix đúng "xưởng rượu Migita Ichi".
- **Quét lại toàn bộ JSON sau khi sửa:** không còn "Ichi Ichi"; không còn dư lượng dạng cũ nào ("Đường sắt Hoàng gia" / "Đường sắt Đế quốc" / "Densha Hime" / "Denshahime" / "Akai-guji" / "ông Guuji" / "thầy cúng" / "cha xứ" / "Migita System" / "Migitai" / "Migitakazu" / "Jutsu-sen" / "Jussen" / "túi phi hành đoàn" / "cặp lái tàu" / "Công chúa Xe điện"); không còn từ lặp sai — các từ láy "chằm chằm" / "sâu, sâu" / "dần dần" / "lâng lâng" / "khư khư" là đúng tiếng Việt, giữ nguyên.
- **Kiểm tra lại khối TOML §7 sau khi sửa:** tách 69 khối theo file, parse bằng tomllib — 69/69 khối parse được, 240/240 giá trị khớp fix trong JSON.
- **Các điểm đã xác nhận trong lượt đọc lại (không sửa):** 仲国03 2082 chỉ sửa nửa sau (帝鉄), nửa đầu "Đường sắt Đế hữu Hinomoto" là T63/E1; 稀咲h3 2547 JP 帝鉄線路合同会社 thắng TW (không phải 8 dòng 帝国線路合同会社 đã loại); ポーレット07 2311 khôi phục đúng giá trị CSV3 (không dấu 「」, đúng monologue JP); ポーレット02 2414 chỉ lật "Jutsu-sen", giữ "Jutsusendo"; các dòng 宮司 trần → "đền chủ Akai" ở P16/グランド06 theo đúng người được chỉ duy nhất là Akai trong file; "Đại tư tế Akai" ở P11/P13 giữ nguyên ngoài phạm vi T13; ハチロク12_再開発 2508 giữ "Yui" chờ mục riêng.

## 7. Khối TOML (parse-verified, theo file)

Mỗi khối có header `[script]`, key dạng chuỗi, giá trị là fix. Trong khối TOML, backslash được escape (`\\` → `\\\\`, `\"` → `\\\"`) nên literal `\\n` trong giá trị viết thành `\\\\n`; xuống dòng thật trong giá trị (12 dòng) viết thành `\\n` (escape TOML) để khối giữ một dòng một key và parse lại ra đúng giá trị. Đã parse-verify bằng tomllib: mọi khối parse được và giá trị parse ra khớp fix từng key (**69 khối / 240 key**). Key trong khối là chuỗi (theo quy ước review trước).

```toml
# lr_ふかみh2_セックスの意味.txt.toml
[script]
"1406" = "Cốc nhựa dùng để uống thử ở Migita Ichi có dung tích 60ml.\\nDù uống ba ly thì cũng chưa đầy một cốc bình thường——"

# lrれいな追加03_れいなとのレール.txt.toml
[script]
"1170" = "「San'yo hoặc San'in. Phải nối với một trong hai tuyến đó nha~.\\nRồi đi đến Hiroshima, vì ở đó có đường sắt của Công chúa Tàu điện mà.」"

# lr真闇追加02_御一夜新婚旅行.txt.toml
[script]
"1456" = "\"「Cả Po-chan và đền chủ nữa cơ á!」\""
"1500" = "\"「Đúng vậy ạ~. Cả Paulette và đền chủ Akai\\nthỉnh thoảng cũng đến đây chụp ảnh đó nha~」\""

# れいな01_炭鉱探索.txt.toml
[script]
"1742" = "「Để tìm kiếm những ý tưởng cộng thêm đó,\\nanh muốn tiến hành thêm các cuộc khảo sát quanh mỏ than bỏ hoang Jutsusen――」"

# れいな02_れいなとポーレット.txt.toml
[script]
"63" = "Công việc ở \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; tại Đế đô cũng khắc nghiệt đến mức đó sao ——Vừa nghĩ đến đó, tôi lập tức nhớ ra, à, đúng là như vậy."
"1601" = "「Hôm nay, chúng tôi mong mọi người góp ý về công dụng của lượng than\\ndự kiến khai thác tại Mỏ than Jutsusen thuộc Mine Treasure.」"
"1623" = "「Không còn nữa tức là——\\nGiống như Mỏ than bỏ hoang Jutsusen, ít nhất vẫn còn lại đường ray chứ?」"

# れいな03_しゅっぱつしんこう.txt.toml
[script]
"1513" = "「Nếu chạy liên thông thì biểu đồ chạy tàu sẽ phức tạp hơn mà.\\nHuống hồ Mine Treasure và mỏ than Jutsusen cũng sẽ đi vào hoạt động nữa.」"
"1659" = "「Cuộc chiến sinh tồn giữa các công ty với nhau, thậm chí có cả sự tham gia của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;,\\nthực sự đã bùng cháy dữ dội cho đến tận ngay trước Đại bãi bỏ các tuyến.」"

# グランドリライト01_オール御一夜、成立ならず.txt.toml
[script]
"2467" = "「Chuyện đơn giản thôi. Giờ đây khi nhà máy Kokura của Đường sắt Teitetsu cũ đã bị tháo dỡ, tất cả các công ty đường sắt ở Kyushu đều đang khổ sở vì việc kiểm tra.」"
"2724" = "「Vâng, vì vậy, cứ bốn năm một lần, chúng tôi lại nhờ họ phái người đến. Công chúa Tàu điện——nhờ mối quan hệ của Đường sắt điện Hiroshima Mouri, để mời kỹ sư đến.」"

# グランドリライト03_日々姫.txt.toml
[script]
"3017" = "Để diễn đạt chính xác những gì muốn nói, tôi nghĩ đến công việc của Hibiki. Tiếp đó, tôi liên tưởng đến nhãn chai shochu của xưởng rượu Migita Ichi."

# グランドリライト04_ポーレット.txt.toml
[script]
"1690" = "「Không chỉ có niềm vui thám hiểm, mà còn thêm cả niềm vui tham quan nhà máy. Khai thác than, phát điện, tận dụng——biến Jutsusen thành một thị trấn bảo tàng công nghiệp.」"
"2117" = "「Ừ. Ở Hiroshima có một người tên là Công chúa Tàu điện,\\ncô ấy rất thích Bản tin buồng lái này.」"
"2174" = "「Vâng, chuyện về nơi này. Về Mỏ than bỏ hoang Jutsusen ạ.」"
"2220" = "「Thị trấn Jutsusen. Thị trấn từng bị coi là vết thương và bị phong kín này. Chắc chắn sẽ mang đến tương lai cho chúng ta.」"
"2923" = "Kết thúc công việc trên tàu buổi chiều, chúng tôi một lần nữa quay lại Ga bỏ hoang Mỏ than Jutsusen bằng chuyến xe chạy không."

# グランドリライト05_れいな.txt.toml
[script]
"1894" = "「Ừm. Chuyện biến mỏ than Jutsusen thành công viên chủ đề ấy——」"
"2032" = "「Anh muốn biến khu phố tên Jutsusen thành công viên chủ đề,\\nnhưng bản thân khu phố đó, lại là vết thương của những người sống ở Ohitoyo từ ngày xưa.」"
"2326" = "「Vậy thì, anh sẽ sắp xếp theo thời gian rảnh của Reina.\\nCàng sớm càng tốt, hai chúng ta hãy cùng đi khảo sát mỏ than bỏ hoang Jutsusen.」"
"2364" = "「Không chỉ khảo sát đường hầm bỏ hoang, mà còn xác nhận được vị trí của nhà máy điện.\\nTài liệu để tái sử dụng mỏ than bỏ hoang Jutsusen đã đủ rồi.」"
"2606" = "Sau khi kết thúc ca trực buổi chiều tối, Paulette đã đưa chúng tôi đến mỏ than Jutsusen\\nbằng xe chạy không, rồi chúng tôi đi khảo sát đường hầm bỏ hoang——"
"2667" = "Nếu như mỏ than bỏ hoang Jutsusen, là độc nhất vô nhị, hoặc gần như thế,\\nlà sự tồn tại của một 『mỏ than có thể khôi phục việc khai thác』——"
"2786" = "Những người từng gắn bó với Jutsusen, hay từng sinh sống ở đó,\\ncũng giống như Reina, đã mang theo nỗi buồn như một vết thương lòng."
"3046" = "（Trước lúc đó, việc củng cố phiếu bầu tán thành dự luật biến mỏ than bỏ hoang Jutsusen thành khu du lịch,\\nnếu có thể, phải hoàn tất cho đến lúc biểu quyết.）"

# グランドリライト06_稀咲.txt.toml
[script]
"1415" = "「……Lúc ông ta đứng dậy rời khỏi chỗ ngồi,\\nviệc đền chủ Akai sẽ ngăn lại――」"
"1877" = "「Không, lần này người có công lớn nhất không phải là cháu――\\nmà là đền chủ Akai mới đúng.」"
"2174" = "「Nếu đền chủ Akai không cản lại mà để ông ta đi luôn.\\nCó khi vì thể diện với đền chủ Akai, ông ta sẽ trở nên cố chấp cũng nên.」"
"2371" = "「Đúng vậy. Nhưng thú thật là lúc ông ta đứng dậy em đã rất hoảng.\\nLúc đó, nếu đền chủ Akai không cản lại thì――」"
"2415" = "「Là nhờ mối quan hệ với đền chủ Akai phải không ạ?」"
"2446" = "「Tất nhiên rồi. Có lẽ ông Goto\\nđánh giá đền chủ Akai rất cao.」"
"2571" = "「Quả nhiên là tôi vẫn cảm thấy bất an.\\nGoto Kaita... Ông ta là một nhân vật vượt xa những gì đền chủ Akai đã mô tả.」"
"2916" = "Sau đó, Niiroku và đền chủ Akai cũng rời khỏi phòng."
"2935" = "Ông đang ôm chặt chiếc túi công tác một cách trân trọng và đầy yêu thương."
"2937" = "Ông dịu dàng vuốt ve chiếc túi công tác đặt bên cạnh,\\nnhư thể đang thì thầm với nó vậy."
"3013" = "Ra là vậy, thế thì――nếu cuộc đàm phán rơi vào nguy hiểm,\\nchúng ta đã có thể chứng kiến cuộc đại chiến quái thú như lời đền chủ Akai nói sao."
"3078" = "Nở nụ cười nhẹ nhõm,\\nđền chủ Akai khẽ cúi đầu."
"3106" = "Như đột nhiên mất hứng, ông ta nhanh chóng kết thúc cái bắt tay với tôi.\\n――Thế nhưng ông Goto lại không đưa tay ra với đền chủ Akai."
"3113" = "Nói xong, ông Goto quay lưng lại với đền chủ Akai."
"3184" = "Nhìn theo hướng mắt của Kisaki,\\nđền chủ Akai đang đứng dậy."
"3242" = "Thậm chí ánh mắt ông ta cũng không hướng về đền chủ Akai,\\nmà lại nhìn chằm chằm vào chiếc túi công tác bên cạnh."
"3469" = "Gần như cùng lúc đó, đền chủ Akai\\ncũng cúi gập người xuống sâu, sâu hơn gấp nhiều lần――"
"3470" = "đền chủ Akai đang ngồi lặng lẽ trên ghế sofa ở góc phòng,\\nhôm nay, lần đầu tiên cất tiếng."
"3472" = "đền chủ Akai nhẹ nhàng lấy từ trong chiếc túi công tác ra\\nmột \\x%lレイルロオド;#00ffc040;Railord%l;#; thân vận hành với khuôn mặt bị quấn băng kín mít."
"3540" = "Dù giọng nói bất ngờ phát ra từ chiếc túi công tác, đền chủ Akai vẫn không hề nao núng.\\nÔng gọi Niiroku――hướng về phía chiếc túi."

# グランドリライト07_真闇.txt.toml
[script]
"2322" = "「Vâng. Em định đến Jutsusen, vẽ lại chiếc xe đang được đưa vào sửa chữa.\\nBiết đâu lúc đó sẽ nảy ra ý tưởng gì đó.」"
"2559" = "「Hình như Hibiki——à đúng rồi, em ấy bảo sẽ đến Jutsusen.」"
"2611" = "「Có một chiếc D51 tơi tả, nhưng nếu là Jutsusen hiện tại thì có thể sửa được.\\nVà……về \\x%lレイルロオド;#00ffc040;Railord%l;#;, em cũng có quen biết một người.」"
"2848" = "「Vậy thì, chúng ta sẽ bàn bạc với phía Jutsusen theo hướng đó.\\nNếu có thể, chúng ta sẽ càng có thêm nhiều không gian hơn.」"

# グランドリライト08_ふかみ.txt.toml
[script]
"2086" = "「Ra vậy. Đúng là một ý kiến hay. Vậy thì, anh sẽ hỏi thử các công ty\\ntham gia xem có biết chỗ nào không, nếu không được thì nhờ ngài Công chúa Tàu điện tư vấn vậy.」"

# グランドリライト11_ナインスターズ！.txt.toml
[script]
"3313" = "Đến mức khiến tôi hơi lo lắng, không biết\\nNhà máy chế tạo toa xe Jutsusen - Đường sắt Hinomoto có thể kham nổi không——"
"3393" = "Ý tưởng gộp chung toa phát điện và toa đông lạnh làm một của Hibiki,\\nđã được các kỹ sư kế thừa kỹ thuật của Đường sắt Teitetsu cũ hiện thực hóa."

# ハチロク06_のぞみ.txt.toml
[script]
"1577" = "……Chiếc quạt giấy được xưởng rượu Migita Ichi phân phát vào dịp lễ hội mùa hè.\\nVì năm nào cũng cùng một họa tiết, nên những ký ức cũng như được quạt tung lên."

# ハチロク09_採決.txt.toml
[script]
"2792" = "Có lẽ do rượu vang, hai má cô ấy khá ửng đỏ,\\ntrên tay đang cầm một tấm bản đồ tuyến đường, có vẻ như là từ thời \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;."

# ハチロク11_御一夜鉄道小畑線.txt.toml
[script]
"1661" = "「Bởi vì, chuyện đó, giống y hệt như chuyện \\nReina đã từng nghe từ ngài Công chúa Tàu điện mà.」"
"1919" = "「Là Lõi Lord mà ngài Công chúa Tàu điện đã nói đến sao! \\nViệc tinh luyện lại Lõi Lord, tức là」"
"1955" = "「Tôi nghĩ vậy. Dù có thể đây là cách tiếp cận mà họ đã nghĩ đến rồi, \\nnhưng báo cho Tiến sĩ Fushichou và ngài Công chúa Tàu điện biết cũng không thừa.」"
"2251" = "「Ngài Công chúa Tàu điện đã nói—— \\n'Việc tinh luyện lại Lõi Lord từ \\x%lタブレット;#00ffc040;Tablet%l;#;'」"
"2253" = "「Từ ngài Công chúa Tàu điện sao?」"

# ハチロク12_ムナカタ来訪.txt.toml
[script]
"1525" = "「Không chỉ dừng lại ở nhà máy chế tạo toa xe Jutsusen, mà cả về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, \\ncũng sẽ tập trung xung quanh Ohitoyo. Có thể gọi là 'Ohitoyo của đường sắt' sao?」"
"2092" = "「Tầm nhìn cuối cùng là khôi phục các nhà máy chế tạo toa xe ở Kokura và Kagoshima. \\nJutsusen sẽ trở thành trung tâm của ba cứ điểm, đó là bản thiết kế của chúng tôi.」"
"2191" = "「\\x%lレイルロオド;#00ffc040;Railord%l;#;! Cơ sở bảo dưỡng hay nghiên cứu \\x%lレイルロオド;#00ffc040;Railord%l;#; \\ncũng nên đặt ở Ohitoyo hoặc Jutsusen đi!」"

# ハチロク12_再開発.txt.toml
[script]
"2016" = "「Cô muốn chúng tôi đưa đến ga bỏ hoang của mỏ than Jutsusen—— Nhưng trước tiên, tôi muốn biết lý do.」"
"2098" = "「Hừm, chỉ đến ga bỏ hoang mỏ than Jutsusen thôi sao.」"
"2280" = "「Nếu vậy thì——đoạn đường chạy thử trước mắt, sẽ là chặng khứ hồi đến ga bỏ hoang mỏ than Jutsusen đúng không ạ?」"
"2500" = "「Nếu vậy, sau khi dừng tàu tại ga mỏ than Jutsusen và kiểm tra xong các bộ phận, mọi người có thể khảo sát luôn nhà ga được không?」"
"2508" = "「Nếu chỉ đến ga bỏ hoang mỏ than Jutsusen, thì nên chạy tiếp đến Yunoi rồi vòng lại, hay là chạy lùi về Ohitoyo…… cách nào sẽ tốt hơn ạ.」"
"2515" = "「Có lẽ đây là minh chứng cho việc—— mỏ than Jutsusen từng một thời hưng thịnh.」"
"3070" = "Đoạn đường chạy thử nên được kéo dài dần dần, đến ga bỏ hoang mỏ than Jutsusen là vừa đẹp."

# ハチロク13_夜の嵐.txt.toml
[script]
"2555" = "Tôi cất cẩn thận \\x%l運転体;#00ffc040;thân vận hành%l;#; vào \\x%l乗務鞄;#00ffc040;túi công tác%l;#;, đứng dậy—— thì Hachiroku vẫn chưa đứng lên."
"2559" = "Tôi kéo Hachiroku lên buồng lái.\\nNgay lập tức, mở \\x%l乗務鞄;#00ffc040;túi công tác%l;#; ra."

# ハチロク13_実りの秋.txt.toml
[script]
"2472" = "Chính là lúc hệ thống hợp tác tương trợ giữa Tiến sĩ Fushicho,\\nCông chúa Tàu điện và ông chủ nhà tắm Tororyu-yu được hình thành."

# ハチロク14_橋.txt.toml
[script]
"2258" = "Tiếng \\x%l喚呼;#00ffc040;hô xác nhận%l;#; rõ ràng của Hachiroku đã tiếp thêm cho tôi sức mạnh mới.\\nĐể vượt qua đoạn đường đến ga mỏ than bỏ hoang Jutsusen một cách an toàn——"

# ハチロク15a_痛みとの決別.txt.toml
[script]
"1835" = "「Nếu là nước, thì xưởng rượu Migita Ichi cũng có thể cung cấp.\\nCần bao nhiêu cũng có」"
"2414" = "Đầu tiên là Hibiki, Nagi và Reina. Tiếp theo là Paulette\\nKisaki, Niiroku—— Cuối cùng là chị Mayami và cả đền chủ Akai."

# ハチロク15b_さよなら列車.txt.toml
[script]
"2228" = "Bên trong thùng giữ nhiệt, chứa đầy ắp\\nnhững chai nhựa nước của Migita Ichi để đảm bảo an toàn."

# ハチロク16_春.txt.toml
[script]
"2338" = "Điện khí hóa toàn tuyến. Mục tiêu mà Đường sắt Teitetsu từng đề ra.\\nNhưng khi tìm hiểu về \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, tôi nhận ra đó là một giấc mơ không thể thành hiện thực."
"2692" = "Trước câu trả lời nhanh gọn và dứt khoát ấy, Công chúa Tàu điện mỉm cười.\\nCô ấy cười rạng rỡ mà không hề dùng quạt che miệng."
"2706" = "Trên màn hình hiển thị là Công chúa Tàu điện."
"2790" = "Công chúa Tàu điện mở chiếc quạt giấy ra.\\nChe khuất khóe miệng, cô ấy cười khúc khích trong cổ họng."

# ポーレット01_御一夜探し.txt.toml
[script]
"1912" = "「Đương nhiên rồi! Bởi vì cô Nagayama,\\ntừng làm việc trên toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; cũ mà.」"
"1936" = "「Ngoài Di tích thành Ohitoyo và bến tàu chèo sông Kuma ra, thì Nhà máy rượu Migita Ichi cũng là một điểm tham quan nhỉ.」"

# ポーレット02_古地図.txt.toml
[script]
"1683" = "「Anh định đi sao? Anh trai.\nĐi điều tra tàn tích Mỏ than Jutsusen ấy.」"
"1719" = "「A, là từ trước nhà ga Mỏ than Jutsusen bị bỏ hoang ạ.\nChỉ những lúc dã ngoại, tàu mới dừng tạm ở đó.」"
"1725" = "「Ừm. Xung quanh tàn tích Mỏ than Jutsusen,\ncó ai biết liệu còn sót lại thứ gì như vậy không.」"
"1856" = "「Gần đó không có, nhưng ở sâu bên trong thì sao?\nĐường ray đến tận Mỏ than Jutsusen, chẳng lẽ không còn sót lại chút nào sao?」"
"1858" = "「Nếu quy mô đến mức có nhiều khu nhà ở,\nthì sản lượng của Mỏ than Jutsusen chắc phải cao lắm nhỉ?」"
"2052" = "「Quanh Mỏ than Jutsusen, người ta xây nhiều khu nhà ở lắm.\nChắc hẳn ngày xưa sầm uất lắm nhỉ.」"
"2136" = "「Tuyến đường đó đã bị bãi bỏ từ lâu lắm rồi mà?\nGần nhà ga Mỏ than Jutsusen bị bỏ hoang, làm gì còn thiết bị nào...」"
"2394" = "Nếu phân tích nhân tử lời của Nagi,\nthì sẽ thành 'Tàn tích Mỏ than Jutsusen = (Xa + Bẩn) x 2'."
"2414" = "Nghe cô ấy nói tôi mới để ý, từ ga Mỏ than Jutsusen\nđến ký hiệu bản đồ mỏ phía trên chữ Jutsusendo, có một đường kẻ."
"2670" = "Có lẽ là tàn tích Mỏ than Jutsusen.\nSự xuống cấp đang diễn ra với tốc độ chóng mặt."
"2747" = "Đường ray là loại thép chất lượng cao. Có lẽ ai đó đã lấy trộm rồi.\nNhưng khu vực Mỏ than Jutsusen là vùng cấm hoạt động của \\x%lエアクラ;#00ffc040;Aircra%l;#;——"

# ポーレット03_廃炭鉱.txt.toml
[script]
"1656" = "「Nói cách khác, trong trường hợp đó, khi phải dừng khẩn cấp gần ga bỏ hoang mỏ than Jutsusen, chỉ cần Hibiki đi bộ đến ga bỏ hoang là xong, phải không?」"
"1723" = "「Trừ khi thời tiết cực kỳ xấu, dọc tuyến Yunoi, chỗ duy nhất không có sóng điện thoại là khu vực quanh ga bỏ hoang mỏ than Jutsusen thôi.」"
"2003" = "「Paulette. Nếu được, em có thể cho Hibiki xem mẫu cách dừng tạm thời ở ga mỏ than Jutsusen không?」"
"2052" = "「Đi \\x%l8620;#00ffc040;8620%l;#; đến tận đây, hoặc đến nhà ga bỏ hoang của mỏ than Jutsusen,\\nrồi cho mọi người trải nghiệm khai thác than ở đây.」"
"2083" = "「Đây là…… ga bỏ hoang mỏ than Jutsusen sao.」"
"2895" = "Đã thiếu một \\x%l運転士;#00ffc040;lái tàu%l;#; chính thức, lại còn sắp phải dừng ở ga bỏ hoang mỏ than Jutsusen, nơi bình thường vẫn chạy thẳng qua."

# ポーレット04_ヒヤリング.txt.toml
[script]
"1517" = "「Nếu có thể kết nối việc tái sử dụng mỏ than bỏ hoang Jutsusen với chấn hưng du lịch,\\nthì Ohitoyo chắc chắn sẽ có được sự huy hoàng vượt xa cả trong quá khứ.」"
"1616" = "「Tiếp theo, về vấn đề mỏ than Jutsusen.\\nThành phố đã nhận chuyển nhượng quyền sở hữu và quyền khai thác mỏ than.」"

# ポーレット04_鳴呼いきストーブ列車.txt.toml
[script]
"2696" = "Đúng là vậy. “Một ngày nào đó anh có muốn trở thành cha không?” Câu hỏi của Paulette vào ngày hôm đó, tại mỏ than Jutsusen——"

# ポーレット06_おひとよマイントレジャー.txt.toml
[script]
"1464" = "「……Những người đã giữ vị thế đối với mỏ than Jutsusen――Ở Ohitoyo có rất nhiều」"
"1765" = "「Tóm lại là, sẽ biến toàn bộ khu vực mỏ than bỏ hoang Jutsusen, thành một công viên chủ đề tìm kho báu đúng không」"
"1974" = "「Điều tra lại mỏ than bỏ hoang Jutsusen. Tôi muốn Reina cũng đi cùng」"
"2155" = "「Ra vậy――đúng rồi nhỉ. Vì mỏ than bỏ hoang Jutsusen là đất thuộc sở hữu của thành phố mà」"
"2704" = "Và từ thành phố đến mỏ than Jutsusen, không hề có đường dây điện nào kéo tới cả nên――"
"2753" = "Những nghị viên từng giữ vị thế đối với mỏ than Jutsusen, và hiện tại thuộc phe ủng hộ thu hút \\x%lエアクラ;#00ffc040;Aircra%l;#;, chắc chắn là có."

# ポーレット07_支線.txt.toml
[script]
"2311" = "Sau khi đưa \\x%l列車;#00ffc040;chuyến tàu%l;#; chiều về đến Ohitoyo,\\n\\x%l8620;#00ffc040;8620%l;#; sẽ quay đầu và đợi chúng tôi ở ga bỏ hoang Jutsusen."
"2576" = "Khu vực xung quanh nhà ga bỏ hoang mỏ than Jutsusen——"

# ポーレット08_未来へのレール.txt.toml
[script]
"1891" = "「Nhưng mà, em và bé Nagi,\\ntừ cấp 3 đã học ở Học viện Jutsusen rồi! Dạ!」"
"2384" = "「Đầu máy hơi nước có cấu hình này,\\nít nhất là ở Đường sắt Teitetsu cũ không hề tồn tại」"
"2777" = "Đầu máy chở hàng của Đường sắt Teitetsu cũ đã kết thúc ở D51, D52,\\nvà các mẫu cải tiến tương ứng là D61, D62."
"2881" = "Đúng rồi.\\nCùng với Mine Treasure, Học viện Jutsusen đã hồi sinh từ một ngôi trường bị bỏ hoang."

# ポーレット08_線から面へ.txt.toml
[script]
"1744" = "「Phục sinh nhà ga bỏ hoang mỏ than Jutsusen và tuyến đường sắt mỏ, trước tiên, hãy để \\x%lキハ07;#00ffc040;KiHa 07%l;#; dẫn đường trong khu vực đó.」"

# ポーレット09_ストーブ客車.txt.toml
[script]
"1368" = "\"...Dường như ông ta hoàn toàn không bận tâm đến thời gian đặt câu hỏi. Nghị viên Sekihara cứ bình thản kể về lịch sử của mỏ than Jutsusen.\""
"1837" = "「Vì là xe được Công chúa Tàu điện bảo quản, nên em nghĩ tình trạng vẫn còn tốt.\\nNhưng mà, em cũng nghĩ cô ấy không am hiểu lắm về SL đâu ạ.」"
"1839" = "「Bởi vì đó là một \\x%l客車;#00ffc040;toa hành khách%l;#; khá hiếm ạ.\\nLúc sắp bị mang đi tiêu hủy thì đã được Công chúa Tàu điện mua lại.」"
"1892" = "「Bọn tôi ấy mà, thưa thị trưởng. Ngày xưa từng làm việc ở mỏ than Jutsusen đấy.」"
"1938" = "「Khi em cho Công chúa Tàu điện xem bức ảnh này, cô ấy đã rất hứng thú.\\nSau đó, em cũng đã nói chuyện với cô ấy về kế hoạch Mine Treasure.」"
"2048" = "「Đúng vậy. Hơn nữa, chủ sở hữu hiện tại của mỏ than Jutsusen cũ là thành phố Ohitoyo, và chế độ trợ cấp vẫn còn hiệu lực.」"
"2081" = "「Khai thác than từng được coi là một trong những ngành công nghiệp mũi nhọn của đất nước. Jutsusen là một mỏ than ưu tú, lọt top mười trong số đó đấy.」"
"2129" = "「Ý em là, \\x%l客車;#00ffc040;toa hành khách%l;#; cũ bị loại bỏ theo kiểu đẩy đùn,\\nđã được Công chúa Tàu điện nhận về và bảo quản――đúng không?」"
"2137" = "「Nếu số người yêu thích đường sắt tăng lên,\\nthì điều đó, cũng là niềm vui đối với Công chúa Tàu điện mà, cô ấy nói vậy.」"
"2156" = "「Về các tài liệu kế toán của mỏ than Jutsusen, tôi cũng đã xác nhận rồi ạ.」"
"2262" = "「Công chúa Tàu điện――nhớ không nhầm thì, là chủ sở hữu của Đường sắt điện Mouri ở Hiroshima nhỉ.」"
"2720" = "Vượt xa hơn cả mức độ giữa những \\x%lまいてつ;#00ffc040;chủ tàu%l;#; với nhau, giữa những nhà kinh doanh đường sắt với nhau,\\nPaulette và Công chúa Tàu điện, là một kiểu đồng chí."
"2723" = "Đối với \\x%lストーブ客車;#00ffc040;toa xe sưởi ấm%l;#;, hay đối với Công chúa Tàu điện.\\nChính vì có tình cảm sâu sắc, nên cô ấy mới đắn đo sao."
"2782" = "Hơn cả những gì chúng tôi từng tưởng tượng, Mỏ than Jutsusen đã từng là một mỏ quặng trù phú đến nhường nào."

# ポーレット11_記憶と記録.txt.toml
[script]
"1340" = "「Cỗ máy cuối cùng của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;# cũ――cỗ máy số 1 của dòng máy thử nghiệm tân tiến nhất.\\nKhả năng vẫn còn dư dả về mặt thông số kỹ thuật……tôi nghĩ là không hề thấp đâu.」"
"2511" = "Chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;# vẫn luôn chễm chệ\\ntrong phòng khách của cựu \\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#, Đại tư tế Akai."
"2524" = "Phát ra từ bên trong,\\nchiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;# của Đại tư tế Akai."
"2615" = "（Chiếc túi công tác――may quá, ông ấy có mang theo.）"

# ポーレット13_再評価.txt.toml
[script]
"1312" = "「Ừm, từ Công chúa Tàu điện của nhà Mouri.」"
"1319" = "「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, 『Nghị án xin trợ cấp cho mỏ than cũ Jutsusen với tư cách là mỏ than kế thừa kỹ thuật』.」"
"1320" = "「Đa số tán thành, nghị án này được thông qua. Tiếp theo là, Nghị án 『Tái phát triển khu vực mỏ than Jutsusen thông qua Mine Treasure』.」"
"1330" = "「À đúng rồi ạ~. Chuyện là, điện thoại từ Công chúa Tàu điện,\\nđã nói về chuyện gì vậy ạ~?」"
"1353" = "「Ohitoyo đã đổ bao nhiêu công sức và của cải vào Mỏ than Jutsusen…… Đó là, tàn dư xấu xí của một quyết định sai lầm.」"
"1366" = "「Mời gọi nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; mà không hề kiểm chứng lại Mỏ than Jutsusen―― Chẳng khác nào nhắm mắt đưa chân để người ta dắt đi sao.」"
"1422" = "「Khi nhu cầu than đá không còn, nguồn trợ cấp đó bị cắt đứt. Mệnh mạch của Mỏ than Jutsusen cũng theo đó mà cạn kiệt.」"
"1446" = "「Mỏ than Jutsusen vẫn còn rất nhiều than đá đang ngủ yên. Không chỉ dừng lại ở đó, còn vô số giá trị khác đang ngủ yên ở đó ạ.」"
"1447" = "「Mỏ than Jutsusen, cho đến tận lúc sắp đóng cửa, vẫn không tiếc công đầu tư thiết bị và mài giũa kỹ thuật.」"
"1448" = "「Việc đánh giá lại Mỏ than Jutsusen nên được thực hiện bởi bên thứ ba. Bởi quốc gia, bởi khách du lịch, bởi những người trẻ tuổi.」"
"1477" = "「Thị trưởng có biết rằng Mỏ than Jutsusen cũ cũng từng được vận hành dựa vào tiền trợ cấp không?」"
"1482" = "「Ngay cả việc vận chuyển, Công chúa Tàu điện cũng sắp xếp toàn bộ sao.」"
"1641" = "Hachiroku, Hibiki, Reina, Fukami và Nagi thì khỏi phải nói, cả chị Mayami, ông lão Minokasa――Đại tư tế Akai, và cả chiếc \\x%l乗務鞄;#00ffc040;túi công tác%l;#; cũng có mặt."
"1877" = "Dù đã được Công chúa Tàu điện chấn chỉnh tinh thần, nhưng ngay khoảnh khắc nhìn thấy khuôn mặt anh ấy,\\ntôi lại có cảm giác như mọi thứ lại bị hút về phía anh Soutetsu một cách lâng lâng."

# ポーレット14_ふたたび走り出すために.txt.toml
[script]
"2462" = "「Công nhận mỏ than Jutsusen là mỏ than kế thừa kỹ thuật. Chỉ định đền Akai Aso là tài sản văn hóa.」"

# ポーレット15_求人難.txt.toml
[script]
"1796" = "「Của các kỹ sư mỏ than—— những người từng làm việc ở mỏ than Jutsusen.」"

# ポーレット16_明日へのレール.txt.toml
[script]
"1708" = "「Thật sự cảm ơn đền chủ Akai rất nhiều ạ.」"
"1715" = "「Cô Niiroku và đền chủ Akai, lái giỏi quá nha~」"
"2252" = "「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsusen, từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」"
"2292" = "「Chuyến thị sát đền thờ cũng diễn ra suôn sẻ. Sau khi hoàn thành trọng trách giải thích,\\nđền chủ Akai chắc hẳn cũng đang làm nhiệm vụ với tâm trạng rất tốt.」"
"2933" = "Vừa bước ra sân ga Ohitoyo, tôi lập tức hiểu được lý do cho lời nói của đền chủ Akai."
"2969" = "Tôi khẽ vẫy tay rồi quay sang đền chủ Akai."
"3219" = "Nếu cố ép cắt giảm, thứ bị hy sinh sẽ là sự an toàn hoặc sự thoải mái.\\nChúng ta sẽ lặp lại sai lầm mà \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; đã mắc phải."
"3304" = "Ngay cả bản thân tôi cũng thấy kiểu lấp liếm này quá lộ liễu,\\nnhưng đền chủ Akai và người đi cùng hoàn toàn không có vẻ gì là bận tâm."
"3327" = "Ảnh hưởng từ việc chuyển về dùng xăng cho \\x%l気動車;#00ffc040;toa xe tự hành%l;#; có lẽ là rất lớn,\\nnhưng tay lái của nhóm đền chủ Akai chắc hẳn còn đóng góp nhiều hơn thế."

# ポーレットh8_気動車の国のアリス.txt.toml
[script]
"3601" = "Mỏ than Jutsusen cũng vậy.\\nNgẫm lại thì, cũng dễ hiểu thôi."

# 仲国02_北琴の鉄道.txt.toml
[script]
"2061" = "「Bằng cách giảm chi phí vận hành cho mỗi chuyến đi để thu hồi vốn.\\nÝ tưởng này cũng giống hệt với mục tiêu điện khí hóa toàn tuyến mà Đường sắt Teitetsu từng hướng tới.」"
"2076" = "「Nhưng tôi cũng cảm thấy có nét tương đồng. Giống như Đường sắt Teitetsu đầy hoài niệm hiện tại,\\n——vốn từng là một phần trong cuộc sống của mọi người vào thời kỳ hoàng kim trước đây.」"
"2114" = "「Là loại tàu không có ở Đường sắt Teitetsu cũ nhỉ. Đặc biệt nhanh——nếu đường sắt phát triển\\nthuận lợi, thì có lẽ đây là loại tàu đã được sinh ra.」"
"2175" = "「Hinomoto và Đường sắt Teitetsu——đã đưa ra những lựa chọn hoàn toàn khác biệt.\\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」"
"2994" = "Nếu như Đường sắt Teitetsu vẫn tiếp tục phát triển phương tiện mới cho đến tận 20 năm trước,\\nthì không biết những đoàn tàu như thế nào đã được sinh ra đây——"
"3185" = "Trong khoảnh khắc, đám mây mù trong ngực tôi tan biến——Tôi nhận ra rằng, trong giây lát vừa rồi,\\nchính bản thân mình đã ghen tị với 『Đường sắt Teitetsu cũ』."

# 仲国03_北琴鉄道歴史館.txt.toml
[script]
"1585" = "「……Ngay cả trong những năm cuối cùng của Đường sắt Teitetsu, khi tôi vẫn còn đang hoạt động.\\nNếu như lối suy nghĩ và hành động đó được bám rễ vững chắc thì.」"
"1867" = "「Tuyệt thật đấy! Dù Đường sắt Teitetsu đã bị giải thể.\\nNhưng cái tên đó, hiện tại vẫn đang tồn tại trên toàn thế giới!」"
"1872" = "「Nhưng, nếu nhìn vào Niiroku và người lái tàu Akai. Tôi hiểu rằng Đường sắt Teitetsu cũ\\ncuối cùng cũng đã thức tỉnh ngay trước bờ vực giải thể.」"
"1906" = "「Ngay cả những điểm tốt mà Đường sắt Teitetsu trước đó đã tất cứu——\\nChúng ta cũng đã nhận được rất nhiều từ Hachiroku mà, đúng không?」"
"1992" = "「A~…… Đường sắt Teitetsu thời đó, nghe nói là rất coi thường hành khách phải không?\\nMột là tốc hành đặc biệt, hai là tốc hành. Ba bốn không có, năm mới đến hành khách, kiểu vậy.」"
"2027" = "「Sự tất cứu mà Đường sắt Teitetsu đã tích lũy được sau khi thức tỉnh,\\nvẫn còn lưu lại trong Niiroku, và chúng ta đã kế thừa được điều đó.」"
"2029" = "「Ở Đường sắt Teitetsu, người ta đã truyền tai nhau như vậy ạ.」"
"2081" = "「Đúng là Đường sắt Teitetsu đã bị giải thể.\\nNhưng dù vậy——chúng ta đã được kế thừa lại những đường ray đó.」"
"2082" = "「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Teitetsu,\\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」"
"2083" = "「Sư phụ đã nghiên cứu Đường sắt Teitetsu với tư cách là một đối thủ lớn.\\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」"
"2190" = "「Đúng vậy nhỉ…… Có lẽ cũng có ảnh hưởng từ việc Đường sắt Teitetsu\\nđã cho thấy khổ hẹp có giới hạn về cả tốc độ lẫn tải trọng.」"
"2251" = "「Đường sắt Teitetsu ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」"
"2301" = "「Nói cách khác, ngay cả Nine Stars, cũng là thứ kết nối giữa Đường sắt Teitetsu tốt đẹp xưa cũ,\\nvà tương lai mà Đường sắt Teitetsu đã mơ ước vào những giây phút cuối cùng.」"
"2315" = "「Nếu không phiền, tôi muốn hỏi thêm một điều nữa.\\nTại sao cha của Zhihuan lại phân tích chi tiết về Đường sắt Teitetsu đến vậy?」"
"2860" = "Từ sự thành thạo tiếng Hinomoto của Suika và Zhihuan,\\ncộng thêm kiến thức sâu rộng bao quát cả lịch sử Đường sắt Teitetsu, có thể suy ra——"

# 仲国04_z49列車.txt.toml
[script]
"2007" = "「Hơn nữa, toa khách giường nằm thì…… vào thời Đường sắt Teitetsu,\\ntôi thậm chí còn chưa từng kéo chúng bao giờ.」"

# 仲国06_聖都とパンダとハチロクと.txt.toml
[script]
"1821" = "「Vâng. Đó là một khu vực hiểm trở với độ dốc lớn. Thời kỳ hoàng kim của Đường sắt Teitetsu,\\nhọ thậm chí còn thiết lập cả một tuyến đường vòng chỉ dành riêng cho việc đưa \\x%l補機;#00ffc040;đầu máy phụ%l;#; về.」"
"2347" = "Nhà Migita là xưởng nấu rượu. Không thể nuôi thú cưng được. Hồi ở Đường sắt Teitetsu,\\nchắc chắn em ấy cũng chẳng có cơ hội tiếp xúc với động vật……"

# 共通02_日々姫と真闇と人形と.txt.toml
[script]
"2323" = "「Khôn……ưm, em nghĩ là không có đâu, anh trai. Nhưng mà, biết đâu ở Jutsusendo lại có.」"

# 共通04_キハ07。ポーレットとれいな.txt.toml
[script]
"3097" = "Khi tôi định đến khu tàn tích mỏ than Jutsusen bằng \\x%lエアクラ;#00ffc040;Aircra%l;#;,\\ntiếng của Hibiki dường như đã đuổi theo tôi để nói gì đó."

# 共通07_鍵.txt.toml
[script]
"2025" = "「À ừm……bố tôi bảo ông ấy là người vì quá đắm chìm vào đường sắt mà làm khuynh gia bại sản xưởng rượu Migita Ichi……\\nlà một người như vậy, nên……hãy lấy đó làm tấm gương xấu.」"
"2547" = "Khi vấn đề nợ nần bị vỡ lở, chị Mayami đã là \\x%l杜氏;#00ffc040;trưởng hầm rượu%l;#; của xưởng rượu Migita Ichi\\n——tức là đương gia thực sự của nhà Migita."

# 共通08_傷跡.txt.toml
[script]
"1485" = "「\\x%l乗務鞄;#00ffc040;Túi công tác%l;#; giống như giường ngủ và cũng là ngôi nhà của em vậy.\\nEm sẽ rất vui nếu ngài Soutetsu luôn mang theo nó bên mình ạ.」"
"1486" = "「Bên trong \\x%l乗務鞄;#00ffc040;túi công tác%l;#; được thiết kế để vừa vặn chứa thân vận hành ạ.」"
"2088" = "「Ngài Soutetsu, xin hãy nhận lấy cái này.\\nNó được gọi là \\x%l乗務鞄;#00ffc040;túi công tác%l;#; ạ.」"
"2692" = "So với độ nặng trịch của \\x%l乗務鞄;#00ffc040;túi công tác%l;#;,\\nthì \\x%l運転体;#00ffc040;thân vận hành%l;#; lại quá đỗi nhẹ nhàng."

# 共通10_クマ川くだりで見る景色.txt.toml
[script]
"2771" = "「Mỏ than bỏ hoang Jutsusen phải không ạ. Gần đó――\\nlà đi qua khu vực không thể sử dụng \\x%lエアクラ;#00ffc040;Aircra%l;#; đúng không ạ?」"
"3005" = "Theo lời nhờ vả của Hachiroku, tôi luôn giữ \\x%l乗務鞄;#00ffc040;túi công tác%l;#; khư khư bên mình.\\nBên trong tất nhiên là \\x%l運転体;#00ffc040;thân vận hành%l;#; rồi."

# 凪ふかみ03_三人いっしょ.txt.toml
[script]
"1071" = "...Không hiểu sao, có cảm giác gì đó khác với bình thường.\\nChị Mayami ở cơ sở nấu rượu Migita Ichi ấy."
"1429" = "「Migita Ichi——Là cơ sở nấu rượu Migita Ichi ạ」"
"2525" = "Tôi cũng sẽ bắt chước, ở Migita Ichi, với tư cách là một học sinh đi dã ngoại,\\ntôi sẽ khiêm tốn học hỏi."

# 凪ふかみ08b_ふかみエピローグ_赤を切る勇気.txt.toml
[script]
"2708" = "「Nhờ sự vận động của Công chúa Tàu điện, Đài Truyền hình Cáp Hiroshima đã sản xuất\\nvà bắt đầu phát sóng từ tháng 4 này, chớp mắt đã phủ sóng toàn quốc mạng lưới!」"

# 日々姫01_リゾート食堂列車計画.txt.toml
[script]
"1688" = "「Vâng. Em muốn vậy. Vì chúng ta sẽ tạo nên một gia đình mới.\\nNếu phải rời khỏi xưởng rượu Migita Ichi, rời khỏi ngôi nhà này, thì đó là một lý do tuyệt vời.」"

# 日々姫01_双鉄の妹.txt.toml
[script]
"2097" = "「Trực giác tốt đấy. Hoàn toàn chính xác. Cơm Hachikuma,\\nvốn có nguồn gốc từ suất ăn cho nhân viên trong nhà bếp toa ăn của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; cũ mà.」"

# 日々姫02_文庫森.txt.toml
[script]
"1242" = "「...Sự khởi đầu của Đường sắt Teitetsu là từ việc thu mua các tuyến đường sắt tư nhân.\\nChuyện này, hai người có biết không?」"
"1570" = "「Thời kỳ hoàng kim... ý cô là, ngày xưa...\\nLà về Đường sắt Kyudai thời trước \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; sao?」"
"1655" = "「Chà. Từ trước khi Đường sắt Teitetsu ra đời——\\nTừ thời đại đường sắt tư nhân sao.」"
"1869" = "「Vâng. Bao gồm cả khoảng thời gian đó... nếu ông không phiền,\\ncả những kỷ niệm thời Đường sắt Teitetsu, hay sau khi bãi bỏ tuyến nữa ạ.」"
"1954" = "「Bị Đường sắt Teitetsu cưỡng chế thu mua, và bị ràng buộc bởi pháp luật.\\nMọi thứ trong kinh doanh đều không thể tự do làm theo ý mình nữa.」"
"2544" = "Nghe nói \\x%lキハ07s;#00ffc040;KiHa 07S%l;#; của Reina là mẫu xe cùng kiểu với KiHa 07 của Đường sắt Teitetsu,\\nđược chế tạo riêng cho \\x%l硬上鉱山鉄道;#00ffc040;Đường sắt mỏ Katakami%l;#;."

# 日々姫02_日々姫の日々.txt.toml
[script]
"2516" = "A, nhưng mà. Nếu vậy thì,\\nchẳng phải là do nhà nấu rượu Migita Ichi đã không yêu cầu sao."
"2671" = "Trước mặt thợ nấu rượu trưởng——nhân vật số 2 ở nhà nấu rượu Migita Ichi là bà Saitou,\\ntôi không có tư cách để đưa ra ý kiến gì cả."

# 日々姫03_湯富院.txt.toml
[script]
"1826" = "「Không phải ạ, Mikuro là,\nRailord của đầu máy hơi nước loại 8620, số hiệu 38696 thuộc Đường sắt Teitetsu cũ ạ.」"
"2662" = "「Nhờ lặp lại việc quét dọn buổi sáng ở nhà máy rượu Migita Ichi, Hibiki và tôi đã học được điều đó là sự thật.」"

# 日々姫06_みくろ、来訪.txt.toml
[script]
"3128" = "Tuy vẫn còn chút ngây ngô với sự đời của một Railord kiểu Đường sắt Teitetsu cũ,\\nnhưng chắc hẳn con bé đã tích lũy được nhiều kinh nghiệm quý báu ở sở thú."

# 日々姫07_たったひとりの宣戦布告.txt.toml
[script]
"1629" = "「Không đâu? Thực tế là có chuyện đó đấy ạ.\\nHồi em còn ở \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;, một nhân viên \\x%l保線;#00ffc040;bảo trì đường ray%l;#; ở khu \\x%l保線;#00ffc040;bảo trì%l;#; Teio đã bị...」"

# 日々姫08_とれいん食堂.txt.toml
[script]
"3067" = "Với tư cách là những người thợ――Trưởng hầm rượu và Thợ ủ rượu chính của xưởng rượu Migita Ichi,\\nđã đồng thanh, thể hiện bằng hành động, và công nhận chúng tôi."

# 日々姫09_run_with_our_dreams.txt.toml
[script]
"1687" = "「Một sân ga trống trơn giống hệt như thời kỳ cuối của Đường sắt Teitetsu,\\nkết hợp với một khách sạn được cố tình làm cho cũ kỹ, thật sự rất ăn khớp với nhau.」"
"1840" = "「Vậy thì, tiếp theo đây là món quà chúc mừng từ Xưởng rượu Migita Ichi.\\nTrưởng hầm rượu Migita Mayami và Thợ ủ rượu chính Saito Honoka.」"
"1906" = "「Railord của đầu máy hơi nước số 1 thuộc dòng 8620 Đường sắt Teitetsu cũ.\\nHiện tại thuộc Đường sắt Ohitoyo, Hachiroku ạ.」"
"2046" = "「Railord của đầu máy hơi nước 38696 thuộc dòng 8620 Đường sắt Teitetsu cũ,\\nMikuro ạ.」"
"2095" = "「D51 nhìn qua làn hơi nước của suối nước nóng, trông cứ như đang nhả hơi nước vậy.\\nCứ như thể nó vẫn luôn chạy không ngừng nghỉ từ thời Đường sắt Teitetsu đến giờ.」"
"2636" = "Để dung hòa cả hai điều đó, sau khi bàn bạc với đền chủ Akai,\\nchúng tôi đã chọn tổ chức lễ cưới trước mặt mọi người."
"2699" = "Giọng nói điềm tĩnh của đền chủ Akai.\\nNhờ vậy, tôi mới dễ dàng bừng tỉnh."
"2751" = "Dù nghe nói đây là lần đầu tiên ngài ấy chủ trì một lễ cưới trước mặt mọi người,\\nnhưng quả không hổ danh là đền chủ của đền Akai Aso."

# 日々姫09_静かなる開戦.txt.toml
[script]
"1690" = "「Cháu là Migita Hibiki. Là con gái út của xưởng rượu Migita Ichi,\\nlà Trưởng phòng Toa xe của Công ty Cổ phần Đường sắt Ohitoyo, và là \\x%l機関助士;#00ffc040;Phụ lái tàu%l;#; tập sự.」"
"1790" = "「Tất nhiên rồi ạ. Xin mời đền chủ Akai.」"
"2579" = "Từ Paulette, khẽ lướt sang chị Mayami, sang tôi, rồi đến đền chủ Akai.\\nVà rồi chẳng biết từ lúc nào, tất cả đều dồn về một người duy nhất."
"2644" = "Trước cái giơ tay điềm tĩnh của đền chủ Akai,\\nngười đàn ông đang lớn tiếng và nhổm dậy liền im bặt và lùi lại."
"2645" = "Một giọng nói kinh ngạc từ tận đáy lòng.\\nđền chủ Akai mở to hai mắt."
"2660" = "Thậm chí trong giọng nói của đền chủ Akai, tôi cũng cảm nhận được sự căng thẳng."

# 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml
[script]
"2495" = "「Bên trong mô hình này,\\\\ntương lai lý tưởng mà \\\\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; vẽ ra đã trở thành hiện thực nhỉ.」"

# 日々姫11_御一夜モザイク.txt.toml
[script]
"2018" = "「Chúng ta đã nhận được đơn đặt hàng và lời đề nghị tài trợ.\\\\nTừ Đường sắt điện Mouri――Công chúa Tàu điện của Mouri.」"
"2141" = "「Tất nhiên rồi ạ. Nó là \\\\x%l客車;#00ffc040;toa hành khách%l;#; tiêu biểu\\\\ntừng rong ruổi trên tuyến \\\\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; thời \\\\x%l大詔;#00ffc040;Đại Chiếu%l;#; mà.」"

# 日々姫14_投開票.txt.toml
[script]
"1276" = "「Toa \\x%l客車;#00ffc040;hành khách%l;#; số 1 Ohitoyo \\x%l22形;#00ffc040;Loại 22%l;#;, cải tạo từ Dòng 22000 của \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#;,\\ntoàn bộ quá trình cải tạo \\x%lイロ;#00ffc040;Nairo 221%l;#; đã hoàn tất.」"

# 日々姫16_夢を乗せて.txt.toml
[script]
"1766" = "「Cái người tên là... Công chúa Tàu điện của nhà Mouri ấy nhỉ? Nghe nói cô bé đó rất ưng ý chất lượng của \\x%l客車;#00ffc040;toa hành khách%l;#; mà chúng ta đã giao đấy.」"

# 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml
[script]
"1415" = "「Ha, na, o――『Hanao (Quai dép)』 sao!\\nGuốc mộc hoặc dép rơm, guốc mộc hoặc dép rơm thì――đền chủ Akai!!」"
"3002" = "Ra là vậy, nếu là người để \"mượn trí tuệ\",\\nthì không ai thích hợp hơn chủ nhân của ngôi đền này, đền chủ Akai."

# 真闇01_再蒸留.txt.toml
[script]
"1621" = "「Năm \\x%l正和;#00ffc040;Showa%l;#; thứ 42 là năm \\x%l帝鉄;#00ffc040;Đường sắt Teitetsu%l;#; giải thể. Cùng với đó, có lẽ \\nở Kumamoto, đại bãi bỏ các tuyến đường sắt cũng đã diễn ra đồng loạt.」"
"2164" = "Loại rượu trứ danh \"Migita Ichi\" của xưởng rượu nhà tôi,\\nlà một loại rượu rất được ưa chuộng ở địa phương, chỉ riêng lượng đặt trước trong thành phố đã chiếm tới chín mươi phần trăm doanh số."
"2366" = "Hai trăm triệu yên, rủi mà không trả được,\\nthì rõ ràng sẽ giáng một đòn nặng nề lên cả chị Mayami và xưởng rượu Migita Ichi."
"2444" = "（Nếu nhà máy \\x%lエアクラ;#00ffc040;Aircra%l;#; được xây dựng, thì một ngày nào đó——\\nNó cũng sẽ gây ra những ảnh hưởng chí mạng đến xưởng rượu Migita Ichi.）"

# 稀咲h3_チャイナドレスでおもてなし.txt.toml
[script]
"2547" = "「Chỉ nội điều đó thôi, đánh giá và sự tin tưởng dành cho công ty của chúng ta――\\nCông ty TNHH Đường sắt Teitetsu, đã tăng lên đáng kể rồi」"
"2740" = "「Bác ấy thậm chí còn mời được cựu Tổng giám đốc Đường sắt Teitetsu,\\nngười vốn không có chút liên hệ nào với Ohitoyo, nhà Migita hay nhà Houshou, làm người mai mối cho chúng ta mà」"
```


### Ghi chú điều phối — 4 dòng trùng với đợt U4 (gộp 22/11 ~11:50, trước khi gộp U3)

4 dòng sau có trong cả U3 và U4 với fix bổ sung nhau (token khác nhau, cùng old_vn). Để tránh merge-order overwrite làm mất một bên, coordinator đã GHÉP fix (combined) vào JSON + REVIEW + TOML block của U3 — old_vn của U3 đổi thành fix U4 (đã gộp), fix = giá trị ghép chứa cả hai thay đổi, đã kiểm chứng lại từng giá trị ghép với JP:
- グランドリライト06_稀咲 3472 (T13+T18+T11): JP có 運転体 + 運転鞄 + 赤井宮司 → "thân vận hành" + "túi công tác" + "đền chủ Akai".
- ハチロク12_再開発 2508 (T17+T7): JP có 術仙 + [ゆのい,1]湯医 → "Jutsusen" + "Yunoi".
- ハチロク13_夜の嵐 2555 (T18+T11): JP có 運転体 + 乗務鞄 → "thân vận hành" + "túi công tác".
- ポーレット03_廃炭鉱 1723 (T17+T7): JP có 湯医線 + 術仙 → "Yunoi" + "Jutsusen".
Vì 4 dòng này đã tính trong U4 (193 dòng), U3 chỉ cộng thêm 240 − 4 = 236 dòng mới vào chuỗi tổng. Số liệu nguồn old_vn trong REVIEW đã cập nhật theo (4 dòng chuyển sang unification-merged).

## Kết bài

Đợt U3 sửa **240 dòng duy nhất / 6 mục (T3, T10, T13, T14, T17, T18)** trên 69 file. Điểm lớn nhất: bẫy T17 thực tế là **85 dòng** (61 fix audit + 2 fix unification đã dùng "Jutsu-sen" trước quyết định 21/11, cộng 13 dòng "Jussen" và 1 dòng khôi phục) chứ không phải 28 như ước lượng list; T3 thực tế 55 dòng (list 57) sau khi loại 10 dòng JP không phải 帝鉄 (8 dòng tên công ty 帝国線路合同会社 + 2 dòng 帝有鉄道 thuộc T63/E1); T13 thực tế 38 dòng; T14 thực tế 21 dòng (gồm 3 dòng "Migitai" đã quyết theo ủy quyền O62). Một lỗi fix audit đã được khôi phục (P07 2311 bị cắt cụt). Các flag còn lại cho coordinator: 帝央機関区 (2 dòng), tên công ty 帝国線路合同会社 (8 dòng), các dạng "thầy tế"/"Đại tư tế"/"ông Akai" của 宮司 (14+25+12 dòng — có thống nhất về "đền chủ" hay không), và 2 dòng "Denshahime của Mouri" mà JP chỉ nói 毛利の姫. Lượt soát 2 đối chiếu lại toàn bộ 240 dòng với JP: 237 dòng đúng ngay, 0 dòng loại bỏ, 3 dòng T14 sửa lại (lỗi "Migita Ichi Ichi" — xem §6). File đính kèm: `unification-t1-set2-wrong.json` (240 dòng), snippet `unification-snippet-t1-set2.md` (tổng cộng rebase theo ROUTE-UNIFICATION.md hiện hành).