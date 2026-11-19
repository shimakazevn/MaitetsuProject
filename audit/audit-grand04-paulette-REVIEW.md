# Audit: Grand Rewrite 04_ポーレット — 19 dòng Việt sai (đã đối chiếu JP + TW)

File: `03_Paulette/グランドリライト04_ポーレット.txt.toml` — 489 dòng script, **19 dòng Việt sai = 3,9%**, 0 dòng chưa chắc chắn.
Ngày audit: 19/11/2026. Nguồn đối chiếu: `Matetsu Last Run - Trang tính3.csv` (cột JP Original + TW Original/Current) và TOML-2. Đây là file thứ 14 audit toàn bộ, sau 廃炭鉱 31%, obasan 56%, Grand 01 45,6%, Hibiki 03 86,2%, Hachiroku 13 夜の嵐 44,9%, 実りの秋 0,4%, Nagi_Fukami 08a 4,3%, Hachiroku 12 ムナカタ来訪 2,3%, 再開発 4,4%, Paulette 04_ヒヤリング 1,8%, stove 22,1%, Paulette 05_whatsentertainment 2,8%, 鳴呼の町 5,0%.
Lưu ý: cùng tên file này còn có một bản sao y hệt trong `09_Grand/` (cùng md5 469b3da460c27dbca329c397cc553e2a, 99.471 byte) — khi áp dụng khối sửa cần áp cho cả hai thư mục hoặc kiểm tra lại cơ chế build dùng bản nào.

## Phương pháp và số liệu kiểm chứng
- Đã đọc **hết 489/489 dòng script** (key 1254–3106, không liên tục), đối chiếu từng dòng với JP + TW theo nghĩa, người nói, thoại/lời dẫn, xưng hô độc thoại theo quy ước của chính file. Không ngoại suy tổng dự án từ file này.
- Phân loại 19 dòng sai: **thuật ngữ 14** (御一夜 → "Ohitoyo" 10 dòng; 術仙 → "Jutsu-sen" 4 dòng), **sai nghĩa 3** (1862, 1864, 2135), **xưng hô độc thoại 2** (2733, 2770 — Soutetsu xưng "mình" thay vì "Tôi"). **Lệch vị trí 0, chưa dịch 0, cụt câu 0, không chắc chắn 0.**
- Thoại sai 13/294 (4,4%); lời dẫn (monologue) sai 6/195 (3,1%). Theo người nói: Paulette 8, monologue 6, Soutetsu 5; Michiko, Reina, Navi 0.
- Phân bố lỗi theo đoạn: key 1254–1856: 2 dòng; 1857–2037: 5 dòng; 2039–2263: 4 dòng; 2264–2733: 4 dòng; 2737–3106: 4 dòng — lỗi rải đều cả file, không tập trung vào một cảnh nào.
- **Heuristic thoại/dẫn báo 0 dòng** — bắt được **0/19 lỗi thật**: toàn bộ lỗi đều cùng loại (thoại→thoại, dẫn→dẫn), thuật ngữ, sai nghĩa và xưng hô — những lỗi heuristic không thể thấy. Đây là minh chứng nữa rằng heuristic chỉ là giới hạn dưới.
- **Không có key-shift sạch:** test shift −5..+5 tốt nhất ở shift 0 (489/489 = 1,000 — do heuristic 0 cờ nên shift 0 là hiển nhiên; không có bằng chứng lệch đều). Mọi kết luận đều từ đọc ngữ nghĩa từng dòng + đối chiếu chỉ mục Việt toàn dự án.
- **TOML và CSV giống hệt nhau về nội dung:** kiểm tra toàn bộ 489 dòng, 0 dòng khác nội dung thực (308 dòng chỉ khác `\n`/khoảng trắng). Không có dòng CSV trống nào trong file này. VN==TW: 0 dòng.
- **Không xét lỗi định dạng `\n`:** theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng, `\n` thủ công không quan trọng. Chỉ báo lỗi nội dung. Các bản sửa trong khối TOML bên dưới viết liền một dòng. Dấu gạch —— trong bản sửa viết không khoảng trắng hai bên, theo quy ước dự án (22.055 dòng); hai dòng 1705, 1919 có sẵn "—— " (khoảng trắng sau gạch, do `\n` cũ chuyển thành khoảng trắng) đã được chuẩn hoá luôn trong bản sửa.
- **[selections]:** file có tiêu đề section `[selections]` nhưng **rỗng (0 mục)** — không có lựa chọn nào để kiểm tra hay sửa.
- **Thẻ `%l`:** không có dòng nào VN thêm/thiếu thẻ so với JP. Các thẻ ở 1779, 1823, 1868, 1887, 1935, 1944, 2097, 2188, 2232, 2316, 2504, 2662, 2709, 2737, 2746 đều khớp JP và giữ nguyên trong bản sửa.
- **Áp dụng phương pháp bổ sung của Hieu ngày 19/11:**
  - **Chuỗi lệch xoay vòng nội bộ:** khi gặp dòng lệch, tra bản Việt đúng trong chính file trước khi dịch mới. File này **không có dòng lệch nào** nên không có chuỗi nào để ghi — đã kiểm chứng bằng 3 cách: (1) đọc ngữ nghĩa từng dòng, mọi VN đều khớp JP/TW của chính key đó; (2) 5 giá trị VN trùng lặp nội bộ đều là câu ngắn thông dụng đúng với JP của chính chúng ("À——" 1852/2269/2111, "Hửm?" 1851/1922/1881, "（Cạch）" 3093/3094/3091, "!" 1850/1860, "Rất đẹp." 2186/2199 — cả hai chỗ đều có JP "とても、綺麗だ"); (3) đối chiếu chỉ mục Việt toàn dự án (81.213 mục): 10 dòng VN trùng file khác đều là câu ngắn thông dụng đúng với JP của chính chúng — không phải copy.
  - **JP và TW mâu thuẫn thì tin JP, không dịch bắc cầu qua TW:** áp dụng ở 2135 (xem mục C) — bản Việt cũ thêm "Navi" theo hướng của TW, nhưng kiểm tra 5 dòng trước/sau và toàn file thì Navi chỉ nói ở 2302/2306, không có mặt ở đoạn 2135; bản sửa lần này dịch sát JP, bỏ cả "Navi" lẫn phần TW thêm vào. Hai trường hợp khác đã kiểm tra và giữ nguyên vì VN đã theo JP: 1693 (JP 足りんな "không đủ" vs TW 不能 "không thể" — VN theo JP), 2643 (JP "nói lớn" vs TW thêm 否定 "phủ định" — VN theo JP).

## Kết luận về cơ chế lỗi
- **File sạch, lỗi chỉ ở mức câu/chữ — không có lỗi hệ thống.** Không lệch vị trí, không tràn chương, không chuỗi xoay vòng, không dòng mồ côi, không dòng chưa dịch. Đây là file thứ tư liên tiếp (sau hearing 1,8%, whatsentertainment 2,8%, 鳴呼の町 5,0%) không có lỗi lệch vị trí — khác hẳn các file nặng trước đó.
- **14/19 lỗi là thuật ngữ theo quyết định mới** (10 dòng 御一夜 = "Ohitoyo", 4 dòng 術仙 = "Jutsu-sen"): toàn bộ đều là những dòng *đúng theo chuẩn cũ* nhưng lệch chuẩn mới sau quyết định 19/11 của Hieu. Nếu không tính nhóm này, file chỉ còn 5 lỗi thực sự về nghĩa/xưng hô (1,0%).
- **5 lỗi còn lại** đều là sai sót lẻ tẻ ở mức câu/chữ: 1 sai người xưng hô (1862), 1 dịch sai từ cảm thán (1864), 1 thêm tác nhân không có trong JP (2135), 2 lần Soutetsu độc thoại xưng "mình" (2733, 2770).
- 470 dòng còn lại đã kiểm tra là đúng, KHÔNG nằm trong danh sách dưới đây.

## Chi tiết 19 dòng sai

### A. Thuật ngữ theo quyết định mới — 御一夜 = "Ohitoyo" (10 dòng)
**Quyết định 19/11 của Hieu: 御一夜 = "Ohitoyo"** (8/8 ở Hachiroku 12 再開発 + furigana おひとよ). Đây là 10 dòng duy nhất trong file có 御一夜 — 8 dòng đang dùng "Ohimitera", 2 dòng dùng "Ohito" (2292, 2662). Sau khi áp dụng, file này không còn "Ohimitera"/"Ohito" nào.
- **1705** (Soutetsu): JP 「つまり、この炭鉱町と炭鉱とは―― / 御一夜市そのものの、乗り越えるべき、過去なわけか」 / TW 「也就是說，這個礦山鎮和煤礦，是御一夜市必須要克服的過去是嗎？」 — VN cũ "thành phố Ohimitera" → "thành phố Ohitoyo". (Đồng thời chuẩn hoá "—— " thành "——" trong dòng này.)
- **1919** (Soutetsu): JP 「ふむ。であれば――温泉と蒸気機関車の町―― / 御一夜のイメージで、湯医線全線を統一すれば」 — VN cũ "dùng hình ảnh của Ohimitera" → "của Ohitoyo". Thẻ `%l` 蒸気機関車 giữ nguyên. (Đồng thời chuẩn hoá "—— " thành "——" trong dòng này. 湯医線 giữ "tuyến Yui" — quyết định Yui/Yunoi vẫn đang chờ Hieu, xem mục Thuật ngữ.)
- **1959** (Paulette): JP 「だって――今回の復線が成功したら、 / 間違いなく、次は御一夜－早戸の復線になりますよね？」 — VN cũ "khôi phục tuyến Ohimitera - Hayato" → "tuyến Ohitoyo - Hayato".
- **1962** (Soutetsu): JP 「八ツ城－御一夜間より先に、まず湯医線だな。」 — VN cũ "Trước đoạn Yatsushiro - Ohimitera" → "đoạn Yatsushiro - Ohitoyo". 湯医線 giữ "tuyến Yui" (chờ quyết định).
- **2055** (Paulette): JP 「あの人が、御一夜の経済復興を真剣に考えている / ことは間違いないと思います」 — VN cũ "sự phục hưng kinh tế của Ohimitera" → "của Ohitoyo".
- **2268** (Paulette): JP 「それなら、御一夜の町並みだとか、 / 湯医の古い駅舎も生きます！！」 — VN cũ "cảnh quan của Ohimitera" → "của Ohitoyo". 湯医 giữ "nhà ga cũ của Yui" (chờ quyết định).
- **2292** (Paulette): JP 「じゃんっ。これで御一夜鉄道特製！ / 8620缶バッジの完成です！」 — VN cũ "Đường sắt Ohito" → "Đường sắt Ohitoyo".
- **2662** (monologue): JP 「結果、御一夜鉄道への一般からの注目も大いに強まった。」 — VN cũ "Đường sắt Ohito" → "Đường sắt Ohitoyo". Thẻ `%l` 客車 giữ nguyên.
- **3063** (monologue): JP 「運転台通信の一号の、御一夜流域イラストマップの――」 — VN cũ "Bản đồ minh họa lưu vực Ohimitera" → "lưu vực Ohitoyo".
- **3103** (monologue): JP 「＜大目標＞御一夜－八ツ城間の復線」 — VN cũ "giữa Ohimitera và Yatsushiro" → "giữa Ohitoyo và Yatsushiro".

### B. Thuật ngữ — 術仙 = "Jutsu-sen" (4 dòng)
術仙 (じゅつせん) viết đúng romaji là "Jutsusen"; chuẩn dự án từ các audit trước là **"Jutsu-sen"** (có gạch nối — audit 廃炭鉱; audit Hachiroku 12 đã sửa 7 chỗ "Jutsusen" → "Jutsu-sen"). File này viết thiếu chữ "t" thành "Jussen" ở cả 4 chỗ có 術仙. Sửa cả 4:
- **1690** (Soutetsu): JP 「採炭、発電、活用と――術仙を、工業博物館の町とする」 — VN cũ "biến Jussen thành một thị trấn bảo tàng công nghiệp" → "biến Jutsu-sen thành…".
- **2174** (Paulette): JP 「はい、ここのこと。術仙廃炭鉱のことを、です」 — VN cũ "Về Mỏ than bỏ hoang Jussen ạ." → "Về Mỏ than bỏ hoang Jutsu-sen ạ."
- **2220** (Paulette): JP 「術仙の町。傷と思われ、閉じ込められてたこの町が。」 — VN cũ "Thị trấn Jussen." → "Thị trấn Jutsu-sen."
- **2923** (monologue): JP 「回送扱いで折り返しての、術仙炭鉱廃駅。」 — VN cũ "quay lại Ga bỏ hoang Mỏ than Jussen" → "Ga bỏ hoang Mỏ than Jutsu-sen".

### C. Sai nghĩa (3 dòng)
- **1862** (Paulette): JP 「あ！　うん。よろしくね」 / TW 「啊！嗯，拜託你了」 — VN cũ "A! Ừ. Nhờ em nhé." **sai người xưng hô:** người nói là Paulette, người nghe là Soutetsu — Paulette gọi Soutetsu là "anh" trong cả file, không gọi "em". Sửa thành "「A! Ừ. Nhờ anh nhé.」".
- **1864** (Paulette): JP 「あ！　よかったぁ！ / 双鉄くんもそう思います？」 / TW 「啊！太好了！你也這麼想？」 — VN cũ "A! Thích quá!" dịch sai よかった ("tốt quá / may quá", TW: 太好了) thành "thích quá" ("rất thích") — khác nghĩa. Sửa thành "「A! Tốt quá! Anh Soutetsu cũng nghĩ vậy sao?」".
- **2135** (Soutetsu): JP 「そうなのか。 / と、いうことなのだが、ポーレット」 / TW 「是嗎。你也聽到了吧，波萊特」 — VN cũ "「Vậy sao. Navi nói vậy đấy, Paulette.」" **thêm tác nhân không có trong JP:** JP không nhắc Navi, chỉ là Soutetsu phản ứng "vậy sao" rồi quay sang Paulette. Kiểm tra ngữ cảnh 5 dòng trước/sau (2125–2142: chỉ có Paulette, Soutetsu, Michiko nói) và toàn file (Navi chỉ nói ở 2302/2306) — Navi không có mặt ở đoạn này, nên "Navi nói" là bịa thêm theo hướng của TW. **Áp dụng quy tắc của Hieu (tin JP, không dịch bắc cầu qua TW):** bản sửa dịch sát JP, bỏ cả "Navi" lẫn phần TW thêm vào ("cũng nghe rồi đấy"): "「Vậy sao. Thế thì, Paulette.」".

### D. Soutetsu độc thoại xưng "mình" thay vì "Tôi" (2 dòng)
Quy ước file + docs (locations §2.1): Soutetsu xưng "Tôi". Đã rà toàn bộ 17 chỗ "mình" trong file: các chỗ còn lại đều không phải lỗi — thành ngữ ("tự mình", "một mình", "chính mình", "khoác lên mình"), sở hữu ("của chính mình"), "giật mình", hoặc Paulette tự xưng "mình" (nói về bản thân, bình thường). Chỉ 2 dòng dưới đây dùng "mình" làm chủ ngữ trong độc thoại của Soutetsu — cùng mẫu lỗi đã thấy ở pilot, hearing, whatsentertainment, Nagi 08a.
- **2733** (monologue): JP 「僕がここまで立ち直れたのも、 / 右田の家の手厚い保護があってこそだとしみじみ思う。」 — VN cũ "Tôi thầm nghĩ, mình có thể vực dậy được đến mức này, cũng là nhờ có sự đùm bọc chu đáo của nhà Migita." → "Tôi thầm nghĩ, tôi có thể vực dậy được đến mức này, …".
- **2770** (monologue): JP 「完成品を手に取った時、『路子にも見せてやりたい』と、 / 僕は確かに、思っていたから。」 — VN cũ "Khi cầm những thành phẩm đó trên tay, tôi thực sự đã nghĩ: 『Mình cũng muốn cho Michiko xem』." → "『Tôi cũng muốn cho Michiko xem』".

## Các cặp trùng lặp / lệch vị trí đã xác nhận
- **0 cặp lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương.** Không dòng Việt nào trong file là bản dịch của một key khác (trong file hay ngoài file) — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (81.213 mục, chỉ khớp 10 câu ngắn thông dụng đúng với JP của chính chúng).
- **5 trùng lặp nội bộ, tất cả đều đúng:** "「À——」" 1852/2269/2111, "「Hửm?」" 1851/1922/1881, "（Cạch）" 3093/3094/3091, "「!」" 1850/1860, "「Rất đẹp.」" 2186/2199 (cả hai chỗ đều có JP "とても、綺麗だ") — không tính lỗi.
- **0 dòng chưa dịch, 0 dòng cụt câu, 0 dòng không chắc chắn.**

## Thuật ngữ đã dùng (theo docs + các dòng đúng sẵn có trong file)
- Soutetsu độc thoại xưng "Tôi" (quy ước file + docs locations §2.1); Soutetsu gọi Paulette "cô" (nhất quán cả file: 1283, 1901, 2012, 2035…); Paulette xưng "Tôi" (với Soutetsu) / "em", gọi Soutetsu "anh Soutetsu"; Michiko gọi Soutetsu "anh Sou" / "Soutetsu", tự xưng "Michi"; Reina gọi Soutetsu "anh Soutetsu"; Navi gọi Soutetsu "Ngài Soutetsu".
- 御一夜 → **"Ohitoyo"** trong các bản sửa (10 dòng, mục A) — **quyết định 19/11 của Hieu**. 御一夜鉄道 = "Đường sắt Ohitoyo" (2292, 2662); 御一夜市 = "thành phố Ohitoyo" (1705).
- 術仙 → **"Jutsu-sen"** (4 dòng, mục B); 術仙炭鉱 = "mỏ than Jutsu-sen" (2174, 2923); 術仙廃炭鉱 = "Mỏ than bỏ hoang Jutsu-sen".
- 湯医 → "Yui" trong cả file (12 chỗ: 1845, 1919, 1962, 2006, 2067, 2127, 2145, 2156, 2172, 2205, 2264, 2268 — "tuyến Yui", "khu vực Yui") — **quyết định Yui/Yunoi vẫn đang chờ Hieu**, nên các bản sửa giữ nguyên "Yui", không đổi sang "Yunoi".
- 閉塞 → "đóng đường" là **đúng theo glossary của team** (translation_guidelines.md:51; context_trans.md:3318 "Hệ thống đóng đường"; ai_translation_prompt.md:60) — các dòng 1823, 1868, 1944, 2188, 2504, 2737 dùng đúng, không tính lỗi. (Lưu ý: đây là thuật ngữ đường sắt, trò đùa "miệng bị đóng đường" của Reina/Paulette là cố ý trong game.)
- 共感 ở 2112/2114 dịch "đồng cảm" là đúng: đây là đồng cảm giữa người với người, không phải năng lực liên kết của Railord ("cộng cảm" trong TIPS glossary, context_trans.md) — giữ nguyên.
- 帝鉄, 冥国, 冥軍, 小畑, 大畑 không xuất hiện trong file này. コン chỉ xuất hiện 1 lần ở 1906 nhưng đó là コンセプト (ý tưởng), không phải cáo コン — không liên quan tới quyết định đang chờ. エアクラ = "Aircra" (1991, đúng sẵn có). 運転台 = "buồng lái" (2117, 3003); 8620 giữ nguyên; キハ07 = "KiHa 07S" (2242, 2287, 2316); 八ツ城 = "Yatsushiro" (1762, 1962, 2016, 3103); 隈元 = "Kumamoto" (1762); 正和 = "Showa" (1910); 帝都 = "Đế đô" (2675); 宝生元忠 = "Houshou Mototada" (1949); 雛衣ポーレット = "Hinai Paulette" (2673).

## Khối TOML để áp dụng (paste vào [script], giữ nguyên key)
Lưu ý khi chép: các bản sửa viết liền một dòng, không chèn `\n` thủ công — theo quyết định của Hieu ngày 19/11, game đã tự xuống dòng. File này KHÔNG tự sửa TOML gốc, Hieu duyệt rồi tự áp dụng — nhớ áp cho cả bản sao trong `09_Grand/` (cùng file, cùng md5). Khối này đã kiểm tra bằng máy: trích khối từ chính file review, parse bằng tomllib — **19/19 key** khớp đúng tập dòng sai, không thừa không thiếu, giá trị sau khi parse khớp đúng bản sửa.

```toml
1690 = "「Không chỉ có niềm vui thám hiểm, mà còn thêm cả niềm vui tham quan nhà máy. Khai thác than, phát điện, tận dụng——biến Jutsu-sen thành một thị trấn bảo tàng công nghiệp.」"
1705 = "「Nói cách khác, thị trấn mỏ than và mỏ than này——chính là quá khứ mà thành phố Ohitoyo cần phải vượt qua sao.」"
1862 = "「A! Ừ. Nhờ anh nhé.」"
1864 = "「A! Tốt quá! Anh Soutetsu cũng nghĩ vậy sao?」"
1919 = "「Ừm. Nếu vậy——thành phố của suối nước nóng và \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#;——chỉ cần dùng hình ảnh của Ohitoyo để thống nhất toàn tuyến Yui thì...」"
1959 = "「Bởi vì——nếu lần khôi phục tuyến này thành công, chắc chắn mục tiêu tiếp theo sẽ là khôi phục tuyến Ohitoyo - Hayato đúng không anh?」"
1962 = "「Trước đoạn Yatsushiro - Ohitoyo, thì phải lo cho tuyến Yui đã. ……Mải mê mơ mộng mà lại bỏ bê nền tảng của chính mình.」"
2055 = "「Em nghĩ không có gì phải nghi ngờ về việc ông ấy đang nghiêm túc suy nghĩ cho sự phục hưng kinh tế của Ohitoyo.」"
2135 = "「Vậy sao. Thế thì, Paulette.」"
2174 = "「Vâng, chuyện về nơi này. Về Mỏ than bỏ hoang Jutsu-sen ạ.」"
2220 = "「Thị trấn Jutsu-sen. Thị trấn từng bị coi là vết thương và bị phong kín này. Chắc chắn sẽ mang đến tương lai cho chúng ta.」"
2268 = "「Nếu vậy, cảnh quan của Ohitoyo, hay nhà ga cũ của Yui cũng sẽ được hồi sinh!!」"
2292 = "「Tèn ten. Vậy là chiếc huy hiệu cài áo 8620 đặc biệt của Đường sắt Ohitoyo đã hoàn thành!」"
2662 = "Việc cô ấy nhượng lại \\x%l客車;#00ffc040;toa hành khách%l;#; đã mở đường cho 8620 bắt đầu vận hành thương mại. Kết quả là sự chú ý của công chúng dành cho Đường sắt Ohitoyo cũng tăng lên đáng kể."
2733 = "Tôi thầm nghĩ, tôi có thể vực dậy được đến mức này, cũng là nhờ có sự đùm bọc chu đáo của nhà Migita."
2770 = "Khi cầm những thành phẩm đó trên tay, tôi thực sự đã nghĩ: 『Tôi cũng muốn cho Michiko xem』."
2923 = "Kết thúc công việc trên tàu buổi chiều, chúng tôi một lần nữa quay lại Ga bỏ hoang Mỏ than Jutsu-sen bằng chuyến xe chạy không."
3063 = "Dù không nhớ, nhưng tôi có thể hiểu được. Khi cầm trên tay Bản tin buồng lái số đầu tiên, hay Bản đồ minh họa lưu vực Ohitoyo——"
3103 = "＜Mục tiêu lớn＞ Khôi phục tuyến đường sắt giữa Ohitoyo và Yatsushiro"
```

## Việc tiếp theo
1. Áp dụng khối TOML trên cho file Grand Rewrite 04_ポーレット (cả `03_Paulette/` và bản sao `09_Grand/`), chơi thử chương rồi báo lại.
2. Xuất lại CSV mới từ TOML (sau khi áp fix) để CSV không còn cũ — với CSV3 thì chỉ còn 2 dòng lẻ chưa dịch (lr真闇追加01/02) là cần dịch mới; 144/146 dòng chưa dịch đã có bản dịch trong các khối audit (Grand 01: 100, Hibiki 03: 44).
3. Audit tiếp các file còn lại theo thứ tự nặng trước — file này sạch (3,9%), nên ưu tiên các file chưa audit trong danh sách heuristic.

## Kết bài
Grand Rewrite 04_ポーレット là file thứ mười bốn được audit toàn bộ, và là một trong những file sạch nhất (3,9% sai, 19/489 dòng): không lệch vị trí, không tràn chương, không chuỗi xoay vòng, không dòng mồ côi, không dòng chưa dịch, không dòng không chắc chắn — mọi lỗi đều ở mức câu/chữ/đơn vị thuật ngữ. Điểm đáng chú ý nhất là 14/19 lỗi chỉ là thuật ngữ theo quyết định mới (Ohitoyo, Jutsu-sen) — tức những dòng này từng đúng theo chuẩn cũ; nếu trừ nhóm đó, file chỉ còn 5 lỗi thực sự (1,0%), cho thấy bản dịch gốc của chương này vốn đã khá tốt, khác hẳn các file nặng như Hibiki 03 (86,2%) hay Grand 01 (45,6%).

Việc còn lại của riêng file này chỉ là áp dụng khối TOML 19 dòng (nhớ cả bản sao `09_Grand/`) và chơi thử chương để nghiệm thu. Còn về tổng thể dự án, mười bốn file đã audit xong đã có 1.473 dòng sai — và việc Grand 04 sạch trong khi cùng tên "Grand Rewrite" với Grand 01 (45,6%) càng chứng minh không thể đoán độ sạch của một file từ tên chương hay file bên cạnh; vẫn phải đọc hết từng dòng.
