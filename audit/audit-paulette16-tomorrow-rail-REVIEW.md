# Audit: Paulette 16_明日へのレール — 55 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 55/542 dòng sai (10,1%)** — 0 lệch vị trí, 0 chưa dịch, 0 cụt câu, 0 chưa chắc chắn. Cảnh: ngày thị sát của hai vị bộ trưởng (Kinh tế + Giáo dục) tại Mine Treasure — đoàn đi xe goòng vào hầm lò, xem trình diễn khoan đá, ăn thử cơm hộp bento, nghe Paulette trình bày; cuối chương Soutetsu cầu hôn Paulette.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 542 dòng script** (thoại 324: Paulette 101, Soutetsu 90, Bộ trưởng Kinh tế 35, Bộ trưởng Giáo dục 22, Nagayama 12, Reina 10, Mayami 10, nhân viên A 7, nhân viên B 7, Miyamoto 6, Fukami 6, Niiroku 4, Nagi 3, Hibiki 3, đền chủ Akai 3, Hachiroku 3, bảo vệ 1, nhân viên bãi đỗ xe 1; lời dẫn 218) đối chiếu JP + TW từ CSV "Trang tính 3", target là TOML-2. TW chỉ là nhân chứng thứ hai; chỗ nào JP và TW mâu thuẫn thì theo JP (quy tắc Hieu đặt 19/11).
- Heuristic thoại↔lời dẫn báo **0 dòng** — bắt được 0/55 (1 dòng báo sai là dương tính giả: 1307 — JP mở đầu bằng “ (ngoặc kép cong), VN mở đầu bằng " (ngoặc kép thẳng), cả hai đều là thoại). Toàn bộ lỗi đều là cùng-loại (xưng hô, thuật ngữ, nghĩa, tiếng hít) nên heuristic không thấy được; thêm một bằng chứng nữa rằng heuristic chỉ là cận dưới.
- Không có key-shift sạch (shift 0: 541/542; các shift khác 0,981–0,994 — không có ý nghĩa vì key thưa và lỗi không phải lệch vị trí, không áp dụng).
- TOML và CSV giống hệt nhau về nội dung (327 dòng khác chỉ ở `\n`/khoảng trắng, 0 khác nội dung). Không có dòng CSV trống nào; VN==TW 0 dòng. `[selections]` rỗng (0 mục). Thẻ `%l`: 28 dòng có thẻ trong VN (JP có 28) — **0 thẻ thiếu dấu `;` đóng** (khác Paulette 13: 5 thẻ thiếu `;`).)
- Phân loại lỗi: xưng hô 27 dòng (Soutetsu tự xưng "anh/Anh" 23 dòng trong thoại + 4 dòng trong độc thoại), thuật ngữ 17 dòng (御一夜 16, 術仙 1 "Jutsusen" thiếu gạch nối), sai nghĩa 7 dòng (Paulette gọi Soutetsu là "cậu" 4 dòng, 1707 "kịch kim", 1838 tự bịa kết luận, 2326 theo TW sai "Phu nhân Minokasa"), lỗi nhỏ 4 dòng (mất tiếng hít っ 3 dòng + 3330 còn sót kana っ). Tổng 27 + 17 + 7 + 4 = 55 dòng sai. Theo người nói: Soutetsu 29, Paulette 12, lời dẫn 7, nhân viên B 2, Bộ trưởng Giáo dục 2, Bộ trưởng Kinh tế 2, Fukami 1. **Chưa chắc chắn 0 dòng.**
- Thoại sai 48/324 (14,8%), lời dẫn sai 7/218 (3,2%).
- Về xưng hô Soutetsu trong thoại: quét toàn bộ file bằng máy (đã chuẩn hoá `\n` thành khoảng trắng trước khi chạy regex `\b`, theo bài học Paulette 08) — "tôi/Tôi" 7 dòng (1682, 1702, 1965, 2164, 2249, 2415, 2426 — tất cả đều đúng), "anh/Anh" tự xưng **23 dòng** (tất cả đều sai, xem danh sách dưới), "em/Em" tự xưng **0 dòng**, "cháu" 2 dòng (1806, 2261 — nói với người lớn tuổi, đúng). "Em" ngôi hai 7 lần đều gọi Paulette (1751, 1967, 2117, 2121, 2247, 2412, 2425) — thuộc đề xuất "cô"/"em" đang chờ, giữ nguyên. Các kết quả "em" khác trong quét máy đều là dương tính giả ("trẻ em" 1928/2426, "em gái" 2087, "anh em sinh đôi" 2102).
- Về "mình" trong độc thoại: 11 dòng chứa "mình" — **tất cả đều đúng** (sở hữu cách "của mình"/"của riêng mình" 2714/2917/2943/2999/3118, phản thân "chính mình"/"chính bản thân mình" 2842/2977, thành ngữ "một mình" 2654, "giật nảy mình" 3180, mẫu "Tôi… mình…" 1295). 4 dòng sai về xưng hô trong độc thoại là 1303, 2816, 3015, 3391 (đều là "anh/Anh" tự xưng).
- Về "mình" trong thoại Soutetsu: 4 dòng (1682, 2087, 2141, 2162) — **tất cả đều đúng** (phản thân/sở hữu sau "Tôi", giữ nguyên sau khi sửa "anh" thành "Tôi").
- Không có file trùng lặp: file này chỉ tồn tại ở 03_Paulette/ (đã kiểm tra tên trong cả 227 file TOML-2).

## Kết luận về cơ chế lỗi

Không có lệch vị trí, không có chuỗi xoay vòng, không có tràn chương, không có dòng mồ côi — đã kiểm chứng bằng đọc ngữ nghĩa từng dòng + chỉ mục Việt toàn dự án (84.385 mục): 52/55 dòng sai chỉ xuất hiện đúng 1 lần trong toàn dự án, tại chính key của nó. 3 ngoại lệ đều là chuỗi ngắn chung chung của mẫu lỗi hệ thống mất tiếng hít っ:

- **2448 ("!")**: 206 lần; **2449 ("!!?")**: 85 lần; **2450 ("!?")**: 68 lần trong toàn dự án — đều là cùng một lỗi mất tiếng hít っ lặp lại ở hàng trăm dòng, không phải câu của dòng khác.

Cơ chế lỗi ở đây là **xưng hô hệ thống (27/55) + thuật ngữ chưa thống nhất (17/55)** — Soutetsu tự xưng "anh" trong 23/90 dòng thoại của mình (25,6%) cộng 4 dòng độc thoại, và Paulette gọi Soutetsu là "cậu" trong 4 dòng (trái docs và trái dạng chủ đạo 7 lần "anh" trong chính file này). Nếu trừ 27 dòng xưng hô và 17 dòng thuật ngữ, file chỉ còn 11 lỗi thực chất (2,0%) — ngang nhóm file sạch nhất. Không có lỗi cấu trúc nào: đây là file "sạch nhưng sai xưng hô", giống Paulette 15 (36 lỗi, 23 xưng hô) và Paulette 14 (32 lỗi, 18 xưng hô).

## Chi tiết dòng sai

### Thuật ngữ (17 dòng)

**1313 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 『御一夜の過去は間違ってない』
『過去があっての、今がある』
- TW: “御一夜的過去並不是一個錯誤”“正因有了過去，才會有現在這一刻”
- Cũ: 『Quá khứ của Ohimitera không hề sai』
『Có quá khứ mới có hiện tại』
- Sửa: 『Quá khứ của Ohitoyo không hề sai』 『Có quá khứ mới có hiện tại』
**1699 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「いいですね。それ、いい。借り物じゃない――
御一夜のかつての姿の、テーマパーク」
- TW: 「不錯呀。這真是個好主意。並非借鑑別處——而是還原了御一夜昔日樣貌的主題公園」
- Cũ: 「Hay đấy. Ý tưởng đó rất hay. Không phải vay mượn từ đâu cả——
Mà là một công viên giải trí mang dáng dấp của Ohimitera ngày xưa.」
- Sửa: 「Hay đấy. Ý tưởng đó rất hay. Không phải vay mượn từ đâu cả—— Mà là một công viên giải trí mang dáng dấp của Ohitoyo ngày xưa.」
**1912 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「あ、でしたら、引き換えさせてください。
御一夜の特産品と」
- TW: 「啊，既然如此，請允許我用御一夜的特產與您交換」
- Cũ: 「A, nếu vậy thì, xin hãy để cháu trao đổi.
Bằng đặc sản của Ohimitera ạ.」
- Sửa: 「A, nếu vậy thì, xin hãy để cháu trao đổi. Bằng đặc sản của Ohitoyo ạ.」
**1968 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「だって、そうなったら双鉄くん……
御一夜から、いなくなっちゃう」
- TW: 「因為，如果變成那樣，雙鐵君就要……就要離開御一夜了」
- Cũ: 「Bởi vì, nếu chuyện đó xảy ra, anh Soutetsu……
sẽ rời khỏi Ohimitera mất.」
- Sửa: 「Bởi vì, nếu chuyện đó xảy ra, anh Soutetsu…… sẽ rời khỏi Ohitoyo mất.」
**2032 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera". "Yui" cho 湯医 giữ nguyên — quyết định "Yunoi" vs "Yui" đang chờ chốt.

- JP: 「走っても、すぐに止まります。
御一夜-湯医の24.8キロだけで」
- TW: 「就算跑起來，也很快會停下。它只會跑御一夜到湯醫之間的這短短２４．８公里」
- Cũ: 「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ.
Chỉ trong phạm vi 24,8 km từ Ohimitera đến Yui.」
- Sửa: 「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ. Chỉ trong phạm vi 24,8 km từ Ohitoyo đến Yui.」
**2038 [nhân viên B]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「市長は、御一夜のためにたったひとりでも頑張った。
自分、それを見て感動したから、真似したいんです」
- TW: 「市長您哪怕孤身一人，也一直在為御一夜而奮鬥。我看在眼裡非常感動，也想向您學習」
- Cũ: 「Thị trưởng đã cố gắng hết mình vì Ohimitera dù chỉ có một thân một mình.
Tôi nhìn thấy vậy nên rất cảm động, và cũng muốn bắt chước theo.」
- Sửa: 「Thị trưởng đã cố gắng hết mình vì Ohitoyo dù chỉ có một thân một mình. Tôi nhìn thấy vậy nên rất cảm động, và cũng muốn bắt chước theo.」
**2043 [Bộ trưởng Giáo dục]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「持ち帰り、孫や知り合いに見せますよ。
この御一夜の[じゅうぶん,1]重文や、技術継承炭鉱の話とあわせて、ね」
- TW: 「帶回去，給我的孫子和朋友們看看。同時跟他們講講，御一夜的重要文化財產與技術繼承煤礦」
- Cũ: 「Tôi sẽ mang về cho cháu và người quen xem.
Cùng với câu chuyện về Di sản Văn hóa Trọng điểm của Ohimitera và Mỏ than kế thừa công nghệ.」
- Sửa: 「Tôi sẽ mang về cho cháu và người quen xem. Cùng với câu chuyện về Di sản Văn hóa Trọng điểm của Ohitoyo và Mỏ than kế thừa công nghệ.」
**2075 [nhân viên B]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「諦めなかったじゃないですか。御一夜の水を守るために。
自分たちが様子見してたころにも、たったひとりでも」
- TW: 「您一直都沒有放棄保護御一夜的水源不是嗎。在我們還在觀望情況的時候，您也在一個人努力著」
- Cũ: 「Ngài đã không bỏ cuộc mà. Để bảo vệ nguồn nước của Ohimitera.
Ngay cả lúc chúng tôi còn đang đứng nhìn, dù chỉ có một mình ngài.」
- Sửa: 「Ngài đã không bỏ cuộc mà. Để bảo vệ nguồn nước của Ohitoyo. Ngay cả lúc chúng tôi còn đang đứng nhìn, dù chỉ có một mình ngài.」
**2105 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「テーマパークやキャストという言葉に囚われすぎた。
冷静になれば、御一夜の炭鉱に西洋風の衣装は似合わん」
- TW: 「我們被“主題公園”、“演員”這些舶來的詞彙限制了思路。仔細想想，御一夜的煤礦並不適合西式的服裝」
- Cũ: 「Chúng ta đã quá bị bó buộc vào mấy từ như công viên giải trí hay diễn viên rồi.
Bình tĩnh mà nghĩ thì, mỏ than của Ohimitera đâu có hợp với trang phục kiểu Tây.」
- Sửa: 「Chúng ta đã quá bị bó buộc vào mấy từ như công viên giải trí hay diễn viên rồi. Bình tĩnh mà nghĩ thì, mỏ than của Ohitoyo đâu có hợp với trang phục kiểu Tây.」
**2152 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「みなさん、どうか――
御一夜のために、そのお力を貸してください！！」
- TW: 「拜託各位了——為了御一夜，請助我一臂之力！！」
- Cũ: 「Mọi người, xin hãy——
Vì Ohimitera, hãy cho tôi mượn sức mạnh của mọi người!!」
- Sửa: 「Mọi người, xin hãy—— Vì Ohitoyo, hãy cho tôi mượn sức mạnh của mọi người!!」
**2194 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「はい、御一夜の特産品のひとつです」
- TW: 「是的，是御一夜的特產之一」
- Cũ: 「Vâng, nó là một trong những đặc sản của Ohimitera ạ.」
- Sửa: 「Vâng, nó là một trong những đặc sản của Ohitoyo ạ.」
**2196 [Bộ trưởng Giáo dục]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「鉱山の方――と、と。妖精さんが持たせてくれた。
御一夜木工の宝箱なんだそうだ」
- TW: 「是礦山的工作人員——啊，不。是精靈送給我的。聽說這是御一夜木工製作的寶箱」
- Cũ: 「Người của khu mỏ——à, không. Là Tinh linh đã tặng cho tôi đấy.
Nghe nói đó là rương báu do thợ mộc Ohimitera làm.」
- Sửa: 「Người của khu mỏ——à, không. Là Tinh linh đã tặng cho tôi đấy. Nghe nói đó là rương báu do thợ mộc Ohitoyo làm.」
**2217 [Bộ trưởng Kinh tế]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「帰りは川下りになるとはな。
御一夜の観光を堪能させてもらえるわけか」
- TW: 「沒想到返程是乘坐漂流船呀。是要讓我們好好體驗一回御一夜的觀光景點嗎」
- Cũ: 「Không ngờ lúc về lại đi xuôi dòng sông đấy.
Thế này là định cho chúng tôi tận hưởng trọn vẹn du lịch Ohimitera đây sao.」
- Sửa: 「Không ngờ lúc về lại đi xuôi dòng sông đấy. Thế này là định cho chúng tôi tận hưởng trọn vẹn du lịch Ohitoyo đây sao.」
**2252 [Bộ trưởng Kinh tế]** — 術仙技術継承炭鉱 = "Mỏ than kế thừa công nghệ Jutsu-sen" (thiếu gạch nối: bản cũ "Jutsusen").

- JP: 「もちろん結構ですとも。[じゅつせん,1]術仙技術継承炭鉱には、
今後大いに発展してもらわねばなりませんからな」
- TW: 「當然沒有意見。我可是對術仙技術繼承煤礦今後的發展寄予厚望的」
- Cũ: 「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsusen,
từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」
- Sửa: 「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsu-sen, từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」
**2321 [Paulette]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「御一夜から、北は[ふくおか,1]福丘、[こくら,1]粉蔵、[もじ,1]門次まで。
南は、[かごしま,2]鹿兒島、[まくらざき,1]枕咲へと」
- TW: 「自御一夜出發，北至福岡、小倉、門司。南至鹿兒島、枕崎」
- Cũ: 「Từ Ohimitera, phía Bắc đến Fukuoka, Kokura, Moji.
Phía Nam thì đến Kagoshima, Makurazaki.」
- Sửa: 「Từ Ohitoyo, phía Bắc đến Fukuoka, Kokura, Moji. Phía Nam thì đến Kagoshima, Makurazaki.」
**2338 [Soutetsu]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera".

- JP: 「視察を成功へと導いたのは、御一夜の力にほかならない。
この町が重ねて来たものが、正しく目覚めてくれたから」
- TW: 「視察之所以成功，完全是憑藉御一夜自身的力量。是這座城市一路走來的積累，以正確的方式甦醒了過來」
- Cũ: 「Điều dẫn đến thành công của chuyến thị sát không gì khác ngoài sức mạnh của Ohimitera.
Bởi vì những gì thành phố này tích lũy được đã thức tỉnh một cách đúng đắn.」
- Sửa: 「Điều dẫn đến thành công của chuyến thị sát không gì khác ngoài sức mạnh của Ohitoyo. Bởi vì những gì thành phố này tích lũy được đã thức tỉnh một cách đúng đắn.」
**2933 [lời dẫn]** — 御一夜 = "Ohitoyo" (quyết định 19/11); bản cũ "Ohimitera". "Ông Guuji" cho 宮司 giữ nguyên — đề xuất thống nhất "đền chủ"/"Cung tư tế"/"Guuji" đang chờ chốt.

- JP: 御一夜駅のホームに出れば、
赤井宮司の言葉の理由が、すぐわかる。
- TW: 我們走出御一夜站月台，馬上理解了赤井宮司的話。
- Cũ: Vừa bước ra sân ga Ohimitera,
tôi lập tức hiểu được lý do cho lời nói của ông Guuji.
- Sửa: Vừa bước ra sân ga Ohitoyo, tôi lập tức hiểu được lý do cho lời nói của ông Guuji.
### Xưng hô (27 dòng)

**1303 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "anh" — trái docs (locations §2.1: độc thoại "Tôi"); "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: “君がうれしいと僕もうれしい”――
その単純で利己的で、とても幼稚で、尊い気持ちを。
- TW: “你開心我就也開心”——這一單純而自私、極其幼稚卻無比寶貴的思想。
- Cũ: “Em vui thì anh cũng vui”——
Cái thứ cảm xúc đơn thuần, ích kỷ, vô cùng trẻ con và quý giá đó.
- Sửa: “Em vui thì tôi cũng vui”—— Cái thứ cảm xúc đơn thuần, ích kỷ, vô cùng trẻ con và quý giá đó.
**1703 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「いや、買ってあるのだ。家にある。
どうしよう、今からナビを呼んで」
- TW: 「不，我已經買好了。放在家裡。怎麼辦，我馬上把Ｎａｖｉ叫來——」
- Cũ: 「Không, anh đã mua sẵn rồi. Đang để ở nhà.
Làm sao đây, bây giờ gọi Navi tới nhé.」
- Sửa: 「Không, tôi đã mua sẵn rồi. Đang để ở nhà. Làm sao đây, bây giờ gọi Navi tới nhé.」
**1711 [Soutetsu]** — Soutetsu tự xưng "Anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「他人か。なのかもしれん
あの頃の僕と、今の僕とは、もうすでに」
- TW: 「事不關己嗎。那個時候的我，或許的確和現在的我是兩個人了」
- Cũ: 「Người khác sao. Có lẽ là vậy.
Anh của lúc đó, và anh của bây giờ, đã là.」
- Sửa: 「Người khác sao. Có lẽ là vậy. Tôi của lúc đó, và tôi của bây giờ, đã là.」
**1738 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「が、僕が受けた最大の恩は、それでは決して返せない。
そのことに気づけたがゆえ、変わったのだ」
- TW: 「但是，我所接受的最大的恩情，是無法透過這個方式報答的。當我明白這個道理的時候，我就改變了」
- Cũ: 「Nhưng, ân huệ lớn nhất mà anh nhận được, tuyệt đối không thể đền đáp bằng cách đó.
Vì nhận ra điều đó, nên anh đã thay đổi.」
- Sửa: 「Nhưng, ân huệ lớn nhất mà tôi nhận được, tuyệt đối không thể đền đáp bằng cách đó. Vì nhận ra điều đó, nên tôi đã thay đổi.」
**1743 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「そうするためにまず、
視察を乗り切るのに最小限必要な人数を洗い直したい」
- TW: 「作為第一步，我想再重新計算一次通過視察檢驗所需要的最少人數」
- Cũ: 「Để làm được điều đó, trước tiên,
anh muốn tính toán lại số lượng người tối thiểu cần thiết để vượt qua đợt thị sát.」
- Sửa: 「Để làm được điều đó, trước tiên, tôi muốn tính toán lại số lượng người tối thiểu cần thiết để vượt qua đợt thị sát.」
**1745 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「どんなことでも言ってくれ。
そのため、僕はここにいるんだから」
- TW: 「你什麼事都可以跟我說。我就是為了這個而來到這裡的」
- Cũ: 「Có chuyện gì cứ nói với anh.
Vì điều đó, nên anh mới ở đây mà.」
- Sửa: 「Có chuyện gì cứ nói với tôi. Vì điều đó, nên tôi mới ở đây mà.」
**1947 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「ああ、正午だと聞いている」
- TW: 「嗯，說是中午送來」
- Cũ: 「Ừ, anh nghe nói là giữa trưa.」
- Sửa: 「Ừ, tôi nghe nói là giữa trưa.」
**1967 [Soutetsu]** — Soutetsu tự xưng "Anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「ポーレットのことを好きになり。
君といることが幸せで――だから、わかった」
- TW: 「因為我喜歡上了波萊特，因為和你在一起很幸福——所以我才終於明白了」
- Cũ: 「Anh đã yêu Paulette.
Được ở bên em là niềm hạnh phúc——nên, anh đã hiểu ra.」
- Sửa: 「Tôi đã yêu Paulette. Được ở bên em là niềm hạnh phúc——nên, tôi đã hiểu ra.」
**2087 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Mình" ở vế sau giữ nguyên theo mẫu "Tôi… mình…" (phản thân).

- JP: 「事故のとき――僕はふたごの妹に、
突き放されたと……そう思ってた」
- TW: 「我一直覺得在事故發生的那天——我被我的雙胞胎妹妹推開了」
- Cũ: 「Lúc xảy ra tai nạn——anh đã nghĩ rằng,
mình đã bị em gái sinh đôi……đẩy ra.」
- Sửa: 「Lúc xảy ra tai nạn——tôi đã nghĩ rằng, mình đã bị em gái sinh đôi……đẩy ra.」
**2102 [Soutetsu]** — Soutetsu tự xưng "Anh"/"anh" ×3 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「ふたごだった。何をするのも一緒だった。
ずっと一緒に大人になると……そうとぼんやり思ってた」
- TW: 「我們是雙胞胎。無論做什麼都是兩人一起。我曾經理所當然地以為，我倆會一起長大成人」
- Cũ: 「Bọn anh là anh em sinh đôi. Làm gì cũng có nhau.
Anh đã mơ hồ nghĩ rằng……chúng anh sẽ mãi mãi cùng nhau trưởng thành.」
- Sửa: 「Bọn tôi là anh em sinh đôi. Làm gì cũng có nhau. Tôi đã mơ hồ nghĩ rằng……chúng tôi sẽ mãi mãi cùng nhau trưởng thành.」
**2117 [Soutetsu]** — Soutetsu tự xưng "Anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「僕は、君のことが好きだ」
- TW: 「我喜歡你」
- Cũ: 「Anh yêu em.」
- Sửa: 「Tôi yêu em.」
**2121 [Soutetsu]** — Soutetsu tự xưng "Anh"/"anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「僕は一人じゃなくなった。
――君が幸せに笑ってくれれば、僕も幸せになれるんだ」
- TW: 「我已經不再是孤身一人了。——只要你綻放著幸福的笑容，那麼我也將會是幸福的」
- Cũ: 「Anh không còn cô độc nữa.
——Chỉ cần em mỉm cười hạnh phúc, anh cũng có thể trở nên hạnh phúc.」
- Sửa: 「Tôi không còn cô độc nữa. ——Chỉ cần em mỉm cười hạnh phúc, tôi cũng có thể trở nên hạnh phúc.」
**2141 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Mình" ở vế sau giữ nguyên theo mẫu "Tôi… mình…" (phản thân).

- JP: 「だからこれから、ずっと一人だと思っていた。
一人で、誰かに、尽くすものだと思っていた。が――」
- TW: 「所以我曾經以為，我將一直是孤身一人。以為我會就這樣孤身一人地為他人奉獻我的一生。但是——」
- Cũ: 「Nên từ đó, anh đã nghĩ mình sẽ mãi mãi cô độc.
Nghĩ rằng mình sẽ cống hiến cho một ai đó, trong cô độc. Nhưng——」
- Sửa: 「Nên từ đó, tôi đã nghĩ mình sẽ mãi mãi cô độc. Nghĩ rằng mình sẽ cống hiến cho một ai đó, trong cô độc. Nhưng——」
**2144 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「だから僕は、いなくならない。
誰の意向がどうあれど、僕はポーレットのそばにいる」
- TW: 「所以，我不會離開。無論是誰提出怎樣的意見，我都要和你在一起」
- Cũ: 「Nên anh, sẽ không đi đâu cả.
Dù ý muốn của ai có ra sao, anh vẫn sẽ ở bên cạnh Paulette.」
- Sửa: 「Nên tôi, sẽ không đi đâu cả. Dù ý muốn của ai có ra sao, tôi vẫn sẽ ở bên cạnh Paulette.」
**2162 [Soutetsu]** — Soutetsu tự xưng "anh"/"Anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Mình" sở hữu cách ("cuộc đời mình") giữ nguyên.

- JP: 「ならば僕は、自分の生きたいよう生きる。
自分の生を、精一杯に使い切る」
- TW: 「既然如此，我就要按照自己的想法活下去。我要盡情地享受我全部的人生」
- Cũ: 「Nếu vậy thì anh sẽ sống theo cách anh muốn.
Anh sẽ tận dụng tối đa cuộc đời mình.」
- Sửa: 「Nếu vậy thì tôi sẽ sống theo cách tôi muốn. Tôi sẽ tận dụng tối đa cuộc đời mình.」
**2186 [Soutetsu]** — Soutetsu tự xưng "Anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕が頼んだ。真闇姉を通じてだが」
- TW: 「是我托真闇姐幫忙點的」
- Cũ: 「Anh đã đặt đấy. Dù là thông qua chị Mayami.」
- Sửa: 「Tôi đã đặt đấy. Dù là thông qua chị Mayami.」
**2211 [Soutetsu]** — Soutetsu tự xưng "anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「そうなるために、僕は生かしてもらえたんだ。
僕が生きているそのことが、路子の喜びだったから」
- TW: 「正是為了獲得幸福，我才活了下來。因為看到我活在這個世上，就是路子的喜悅」
- Cũ: 「Để trở nên như vậy, anh mới được sống tiếp.
Vì việc anh sống, chính là niềm vui của Michiko.」
- Sửa: 「Để trở nên như vậy, tôi mới được sống tiếp. Vì việc tôi sống, chính là niềm vui của Michiko.」
**2247 [Soutetsu]** — Soutetsu tự xưng "Anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「この状況だ。気が急くのも解るが――」
- TW: 「現在情況特殊，你會感到焦慮也是情有可原——」
- Cũ: 「Tình hình hiện tại là thế này. Anh hiểu em đang nóng ruột nhưng——」
- Sửa: 「Tình hình hiện tại là thế này. Tôi hiểu em đang nóng ruột nhưng——」
**2253 [Soutetsu]** — Soutetsu tự xưng "anh"/"Anh" ×2 trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「義父が与えてくれた機会を無為にする気も、無論ない。
万が一など起こしはしないし、誰の期待も裏切らない」
- TW: 「當然，我也不打算浪費養父給我的機會。我不會允許意外發生，也不會辜負任何人的期待」
- Cũ: 「Tất nhiên, anh cũng không có ý định lãng phí cơ hội mà cha nuôi đã trao cho.
Anh sẽ không để xảy ra chuyện vạn nhất nào, và cũng sẽ không phản bội kỳ vọng của bất kỳ ai.」
- Sửa: 「Tất nhiên, tôi cũng không có ý định lãng phí cơ hội mà cha nuôi đã trao cho. Tôi sẽ không để xảy ra chuyện vạn nhất nào, và cũng sẽ không phản bội kỳ vọng của bất kỳ ai.」
**2344 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại (cầu hôn) — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「僕と、結婚して欲しい」
- TW: 「請和我結婚吧」
- Cũ: 「Hãy kết hôn với anh nhé.」
- Sửa: 「Hãy kết hôn với tôi nhé.」
**2408 [Soutetsu]** — Soutetsu tự xưng "Anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「あの頃の僕は思いこんでた。人に望まれることをする
――それが唯一の贖罪であり、恩返しする方法なのだと」
- TW: 「那時候的我盲目地以為——去做人們所期望之事，就是我唯一的贖罪，也是唯一的報恩方法」
- Cũ: 「Anh của lúc đó đã đinh ninh rằng. Làm những điều người khác mong muốn
——đó là sự chuộc tội duy nhất, và cũng là cách để đền đáp công ơn.」
- Sửa: 「Tôi của lúc đó đã đinh ninh rằng. Làm những điều người khác mong muốn ——đó là sự chuộc tội duy nhất, và cũng là cách để đền đáp công ơn.」
**2412 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「ならば――よかった。
君を目覚めさせたのが、他の誰でも無い、僕で」
- TW: 「那真是太好了——喚醒你的不是其他任何人，而是我」
- Cũ: 「Nếu vậy thì——thật tốt quá.
Người đánh thức em, không phải ai khác, mà chính là anh.」
- Sửa: 「Nếu vậy thì——thật tốt quá. Người đánh thức em, không phải ai khác, mà chính là tôi.」
**2425 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki). "Em" gọi Paulette giữ nguyên (đề xuất "cô"/"em" đang chờ).

- JP: 「僕の方でもいくつかの手を打ってはいるが、
ポーレットも、思いつくことがあったら言ってくれ」
- TW: 「雖然我也已經做了一些對策，不過波萊特如果有想到什麼好主意，也說給我聽聽吧」
- Cũ: 「Phía anh cũng đã đánh vài nước cờ rồi,
nhưng Paulette, nếu em có nghĩ ra điều gì thì cứ nói nhé.」
- Sửa: 「Phía tôi cũng đã đánh vài nước cờ rồi, nhưng Paulette, nếu em có nghĩ ra điều gì thì cứ nói nhé.」
**2430 [Soutetsu]** — Soutetsu tự xưng "anh" trong thoại — trái docs (locations §2.1: "Tôi", "Anh" chỉ với Hibiki).

- JP: 「いなくなる、か。
そういえば、僕にもそんな話があったな」
- TW: 「離開御一夜嗎。聽你這麼一說，好像的確有這麼一回事啊」
- Cũ: 「Sẽ rời đi, sao.
Nhắc mới nhớ, anh cũng từng nói chuyện đó nhỉ.」
- Sửa: 「Sẽ rời đi, sao. Nhắc mới nhớ, tôi cũng từng nói chuyện đó nhỉ.」
**2816 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "anh" — trái docs (locations §2.1: độc thoại "Tôi").

- JP: 一緒に行くのを、一緒に死ぬのを拒まれたと――
突き放されたことを、心のどこかは、恨んでさえいた。
- TW: 她卻拒絕了我跟她一道同行，拒絕了我跟她一起死去——我對於她那奮力的一推，甚至曾心存怨恨。
- Cũ: Bị từ chối đi cùng nhau, bị từ chối chết cùng nhau——
Bị đẩy ra, ở một góc nào đó trong tim, anh thậm chí đã từng oán hận.
- Sửa: Bị từ chối đi cùng nhau, bị từ chối chết cùng nhau—— Bị đẩy ra, ở một góc nào đó trong tim, tôi thậm chí đã từng oán hận.
**3015 [lời dẫn]** — Độc thoại của Soutetsu tự xưng "Anh" ×2 — trái docs (locations §2.1: độc thoại "Tôi").

- JP: 相手を本当に思いやる。踏み込んで相手のことを考える。
――僕にもそうすることができると、教えてもらえた。
- TW: 是波萊特教會了我——我也能夠真正去關心一個人，我也能夠涉足他人的世界，設身處地為她著想。
- Cũ: Thực sự quan tâm đến đối phương. Bước vào và suy nghĩ cho đối phương.
——Anh đã được dạy rằng, anh cũng có thể làm được như vậy.
- Sửa: Thực sự quan tâm đến đối phương. Bước vào và suy nghĩ cho đối phương. ——Tôi đã được dạy rằng, tôi cũng có thể làm được như vậy.
**3391 [lời dẫn]** — Suy nghĩ trong ngoặc của Soutetsu tự xưng "anh" — trái docs (locations §2.1: "Tôi"). "Em" (người đã cứu anh — Michiko/Paulette, người nghe không xác định được từ 3–5 dòng xung quanh) giữ nguyên vì không ảnh hưởng đến bản sửa.

- JP: （ありがとうな。
助けてくれて――生かしてくれて）
- TW: （謝謝你。救了我——讓我活了下來）
- Cũ: （Cảm ơn em nhé.
Vì đã cứu anh——để anh được sống.）
- Sửa: （Cảm ơn em nhé. Vì đã cứu tôi——để tôi được sống.）
### Sai nghĩa (7 dòng)

**1707 [Soutetsu]** — JP ギリギリ = "chỉ vừa đủ, chật vật lắm mới kịp" — "kịch kim" không phải từ tiếng Việt (chỉ xuất hiện đúng 1 lần trong toàn dự án, chính dòng này), không truyền được nghĩa "vừa đủ/chật vật".

- JP: 「そうか――日程を考えれば、一人が習熟できるのは、
せいぜい一役でギリギリだから」
- TW: 「也對啊——考慮到日程安排，一個人最多只來得及學會扮演一個角色」
- Cũ: 「Cũng phải nhỉ——xét theo lịch trình, một người có thể thành thạo,
cùng lắm cũng chỉ một vai là kịch kim rồi.」
- Sửa: 「Cũng phải nhỉ——xét theo lịch trình, một người có thể thành thạo, cùng lắm cũng chỉ một vai là đã chật vật lắm rồi.」
**1739 [Paulette]** — Paulette gọi Soutetsu là "cậu" — trái docs (locations §2.4: Paulette gọi Soutetsu là "Anh Soutetsu") và trái dạng chủ đạo của chính file này (Paulette gọi Soutetsu là "anh" 7 lần: 1349, 1749, 1759, 1968, 2135, 2385, 2428; toàn dự án 470 lần "anh Soutetsu" vs 13 lần "Cậu Soutetsu" trong lời Paulette).

- JP: 「でも、双鉄くん。
その目覚めをくれたのは――たった一人の、あなたです」
- TW: 「但是，雙鐵君。喚醒這座城市的，只有一個人——那就是你」
- Cũ: 「Nhưng mà, Soutetsu.
Người đã mang đến sự thức tỉnh đó——chỉ có duy nhất một người, là cậu đấy.」
- Sửa: 「Nhưng mà, Soutetsu. Người đã mang đến sự thức tỉnh đó——chỉ có duy nhất một người, là anh đấy.」
**1838 [Fukami]** — JP trailing off với なら (nếu là... thì...) — bản Việt tự bịa thêm kết luận "Thì chắc chắn rồi" không có trong JP (tiền lệ Paulette 13 1510: thêm "đã dừng lại" vào câu dở dang của JP là sai).

- JP: 「わぁ。いいもの。ですね。妖精さんの宝箱。なら」
- TW: 「哇。精靈的寶箱，那一定是好東西呀」
- Cũ: 「Oa. Đồ tốt, nhỉ. Nếu là rương báu của Tinh linh. Thì chắc chắn rồi.」
- Sửa: 「Oa. Đồ tốt, nhỉ. Nếu là rương báu của Tinh linh thì…」
**2269 [Paulette]** — Paulette gọi Soutetsu là "Cậu Soutetsu" — trái docs (locations §2.4: Paulette gọi Soutetsu là "Anh Soutetsu") và trái dạng chủ đạo của chính file này (7 lần "anh" vs 4 lần "cậu"). Thẻ %l 保線 giữ nguyên.

- JP: 「助かります。ね？　双鉄くん。
\x%l保線;#00ffc040;保線%l;#;は、力仕事だけじゃないですし」
- TW: 「真是幫大忙了。對吧，雙鐵君。\x%l保線;#00ffc040;巡線%l;#;也不只是粗活」
- Cũ: 「Giúp được nhiều lắm đấy. Đúng không? Cậu Soutetsu.
\x%l保線;#00ffc040;Bảo trì đường ray%l;#; đâu phải chỉ toàn việc chân tay đâu.」
- Sửa: 「Giúp được nhiều lắm đấy. Đúng không? Anh Soutetsu. \x%l保線;#00ffc040;Bảo trì đường ray%l;#; đâu phải chỉ toàn việc chân tay đâu.」
**2326 [Soutetsu]** — JP 蓑笠さんが = ông Minokasa (người đàn ông) — bản Việt theo TW 蓑笠夫人 ("phu nhân") là sai; quy tắc JP-trên-TW (Hieu 19/11). Bằng chứng trong chính file: 3308 dịch 蓑笠さん là "ông Minokasa", còn vợ ông được gọi riêng là 蓑笠さんの奥さん (2180).

- JP: 「蓑笠さんが」
- TW: 「蓑笠夫人」
- Cũ: 「Phu nhân Minokasa...」
- Sửa: 「Ông Minokasa...」
**2351 [Paulette]** — Paulette gọi Soutetsu là "cậu" ×2 — trái docs (locations §2.4: Paulette gọi Soutetsu là "Anh Soutetsu") và trái dạng chủ đạo của chính file này (7 lần "anh" vs 4 lần "cậu").

- JP: 「ありがとう、ありがとう、双鉄くん。
みんな、双鉄くんのおかげです！」
- TW: 「謝謝你，謝謝你，雙鐵君。這都是你的功勞！」
- Cũ: 「Cảm ơn cậu, cảm ơn cậu nhiều lắm, Soutetsu.
Tất cả đều là nhờ cậu cả đấy!」
- Sửa: 「Cảm ơn anh, cảm ơn anh nhiều lắm, Soutetsu. Tất cả đều là nhờ anh cả đấy!」
**2429 [Paulette]** — Paulette gọi Soutetsu là "Cậu Soutetsu" — trái docs (locations §2.4: Paulette gọi Soutetsu là "Anh Soutetsu") và trái dạng chủ đạo của chính file này (7 lần "anh" vs 4 lần "cậu").

- JP: 「双鉄くん！　やりました！
わたしたち、わたしたちやりましたっ！！」
- TW: 「雙鐵君！　成功了！我們、我們成功了！！」
- Cũ: 「Cậu Soutetsu! Làm được rồi!
Chúng ta, chúng ta làm được rồi!!」
- Sửa: 「Anh Soutetsu! Làm được rồi! Chúng ta, chúng ta làm được rồi!!」
### Lỗi nhỏ (4 dòng)

**2448 [Paulette]** — Mất tiếng hít っ: JP 「っ！」 dịch thành "!" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！」
- TW: 「！」
- Cũ: 「!」
- Sửa: 「Ư!」
**2449 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！！？」 dịch thành "!!?" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「!!?」
- Sửa: 「Ư!!?」
**2450 [Soutetsu]** — Mất tiếng hít っ: JP 「っ！？」 dịch thành "!?" trơ trụi. Tiền lệ Hachiroku 12 2103/2537 và Paulette 09 2274/2275/2277: JP 「っ！」→ "Ư!".

- JP: 「っ！？」
- TW: 「！？」
- Cũ: 「!?」
- Sửa: 「Ư!?」
**3330 [lời dẫn]** — Tiếng hít っ còn sót lại dưới dạng kana Nhật "っ" trong câu Việt ("——っ!") — ký tự Nhật chưa dịch, không khớp quy ước dự án (JP 「っ！」→ "Ư!", tiền lệ Hachiroku 12 2103/2537).

- JP: せっかくあれほど、
古きよき日ノ本の雰囲気をもってらっしゃる――っ！
- TW: 難得那位老人，擁有如此優良古樸的日本氣質——啊！
- Cũ: Hiếm lắm mới có người mang đậm phong thái
Hinomoto cổ kính và tốt đẹp đến nhường ấy——っ!
- Sửa: Hiếm lắm mới có người mang đậm phong thái Hinomoto cổ kính và tốt đẹp đến nhường ấy——Ư!
## Khối TOML để dán vào file (đã kiểm chứng parse được)

```toml
1303 = "“Em vui thì tôi cũng vui”—— Cái thứ cảm xúc đơn thuần, ích kỷ, vô cùng trẻ con và quý giá đó."
1313 = "『Quá khứ của Ohitoyo không hề sai』 『Có quá khứ mới có hiện tại』"
1699 = "「Hay đấy. Ý tưởng đó rất hay. Không phải vay mượn từ đâu cả—— Mà là một công viên giải trí mang dáng dấp của Ohitoyo ngày xưa.」"
1703 = "「Không, tôi đã mua sẵn rồi. Đang để ở nhà. Làm sao đây, bây giờ gọi Navi tới nhé.」"
1707 = "「Cũng phải nhỉ——xét theo lịch trình, một người có thể thành thạo, cùng lắm cũng chỉ một vai là đã chật vật lắm rồi.」"
1711 = "「Người khác sao. Có lẽ là vậy. Tôi của lúc đó, và tôi của bây giờ, đã là.」"
1738 = "「Nhưng, ân huệ lớn nhất mà tôi nhận được, tuyệt đối không thể đền đáp bằng cách đó. Vì nhận ra điều đó, nên tôi đã thay đổi.」"
1739 = "「Nhưng mà, Soutetsu. Người đã mang đến sự thức tỉnh đó——chỉ có duy nhất một người, là anh đấy.」"
1743 = "「Để làm được điều đó, trước tiên, tôi muốn tính toán lại số lượng người tối thiểu cần thiết để vượt qua đợt thị sát.」"
1745 = "「Có chuyện gì cứ nói với tôi. Vì điều đó, nên tôi mới ở đây mà.」"
1838 = "「Oa. Đồ tốt, nhỉ. Nếu là rương báu của Tinh linh thì…」"
1912 = "「A, nếu vậy thì, xin hãy để cháu trao đổi. Bằng đặc sản của Ohitoyo ạ.」"
1947 = "「Ừ, tôi nghe nói là giữa trưa.」"
1967 = "「Tôi đã yêu Paulette. Được ở bên em là niềm hạnh phúc——nên, tôi đã hiểu ra.」"
1968 = "「Bởi vì, nếu chuyện đó xảy ra, anh Soutetsu…… sẽ rời khỏi Ohitoyo mất.」"
2032 = "「Dù có chạy thì cũng sẽ dừng lại ngay thôi ạ. Chỉ trong phạm vi 24,8 km từ Ohitoyo đến Yui.」"
2038 = "「Thị trưởng đã cố gắng hết mình vì Ohitoyo dù chỉ có một thân một mình. Tôi nhìn thấy vậy nên rất cảm động, và cũng muốn bắt chước theo.」"
2043 = "「Tôi sẽ mang về cho cháu và người quen xem. Cùng với câu chuyện về Di sản Văn hóa Trọng điểm của Ohitoyo và Mỏ than kế thừa công nghệ.」"
2075 = "「Ngài đã không bỏ cuộc mà. Để bảo vệ nguồn nước của Ohitoyo. Ngay cả lúc chúng tôi còn đang đứng nhìn, dù chỉ có một mình ngài.」"
2087 = "「Lúc xảy ra tai nạn——tôi đã nghĩ rằng, mình đã bị em gái sinh đôi……đẩy ra.」"
2102 = "「Bọn tôi là anh em sinh đôi. Làm gì cũng có nhau. Tôi đã mơ hồ nghĩ rằng……chúng tôi sẽ mãi mãi cùng nhau trưởng thành.」"
2105 = "「Chúng ta đã quá bị bó buộc vào mấy từ như công viên giải trí hay diễn viên rồi. Bình tĩnh mà nghĩ thì, mỏ than của Ohitoyo đâu có hợp với trang phục kiểu Tây.」"
2117 = "「Tôi yêu em.」"
2121 = "「Tôi không còn cô độc nữa. ——Chỉ cần em mỉm cười hạnh phúc, tôi cũng có thể trở nên hạnh phúc.」"
2141 = "「Nên từ đó, tôi đã nghĩ mình sẽ mãi mãi cô độc. Nghĩ rằng mình sẽ cống hiến cho một ai đó, trong cô độc. Nhưng——」"
2144 = "「Nên tôi, sẽ không đi đâu cả. Dù ý muốn của ai có ra sao, tôi vẫn sẽ ở bên cạnh Paulette.」"
2152 = "「Mọi người, xin hãy—— Vì Ohitoyo, hãy cho tôi mượn sức mạnh của mọi người!!」"
2162 = "「Nếu vậy thì tôi sẽ sống theo cách tôi muốn. Tôi sẽ tận dụng tối đa cuộc đời mình.」"
2186 = "「Tôi đã đặt đấy. Dù là thông qua chị Mayami.」"
2194 = "「Vâng, nó là một trong những đặc sản của Ohitoyo ạ.」"
2196 = "「Người của khu mỏ——à, không. Là Tinh linh đã tặng cho tôi đấy. Nghe nói đó là rương báu do thợ mộc Ohitoyo làm.」"
2211 = "「Để trở nên như vậy, tôi mới được sống tiếp. Vì việc tôi sống, chính là niềm vui của Michiko.」"
2217 = "「Không ngờ lúc về lại đi xuôi dòng sông đấy. Thế này là định cho chúng tôi tận hưởng trọn vẹn du lịch Ohitoyo đây sao.」"
2247 = "「Tình hình hiện tại là thế này. Tôi hiểu em đang nóng ruột nhưng——」"
2252 = "「Tất nhiên là được rồi. Mỏ than kế thừa công nghệ Jutsu-sen, từ nay về sau cần phải phát triển mạnh mẽ hơn nữa mà.」"
2253 = "「Tất nhiên, tôi cũng không có ý định lãng phí cơ hội mà cha nuôi đã trao cho. Tôi sẽ không để xảy ra chuyện vạn nhất nào, và cũng sẽ không phản bội kỳ vọng của bất kỳ ai.」"
2269 = "「Giúp được nhiều lắm đấy. Đúng không? Anh Soutetsu. \\x%l保線;#00ffc040;Bảo trì đường ray%l;#; đâu phải chỉ toàn việc chân tay đâu.」"
2321 = "「Từ Ohitoyo, phía Bắc đến Fukuoka, Kokura, Moji. Phía Nam thì đến Kagoshima, Makurazaki.」"
2326 = "「Ông Minokasa...」"
2338 = "「Điều dẫn đến thành công của chuyến thị sát không gì khác ngoài sức mạnh của Ohitoyo. Bởi vì những gì thành phố này tích lũy được đã thức tỉnh một cách đúng đắn.」"
2344 = "「Hãy kết hôn với tôi nhé.」"
2351 = "「Cảm ơn anh, cảm ơn anh nhiều lắm, Soutetsu. Tất cả đều là nhờ anh cả đấy!」"
2408 = "「Tôi của lúc đó đã đinh ninh rằng. Làm những điều người khác mong muốn ——đó là sự chuộc tội duy nhất, và cũng là cách để đền đáp công ơn.」"
2412 = "「Nếu vậy thì——thật tốt quá. Người đánh thức em, không phải ai khác, mà chính là tôi.」"
2425 = "「Phía tôi cũng đã đánh vài nước cờ rồi, nhưng Paulette, nếu em có nghĩ ra điều gì thì cứ nói nhé.」"
2429 = "「Anh Soutetsu! Làm được rồi! Chúng ta, chúng ta làm được rồi!!」"
2430 = "「Sẽ rời đi, sao. Nhắc mới nhớ, tôi cũng từng nói chuyện đó nhỉ.」"
2448 = "「Ư!」"
2449 = "「Ư!!?」"
2450 = "「Ư!?」"
2816 = "Bị từ chối đi cùng nhau, bị từ chối chết cùng nhau—— Bị đẩy ra, ở một góc nào đó trong tim, tôi thậm chí đã từng oán hận."
2933 = "Vừa bước ra sân ga Ohitoyo, tôi lập tức hiểu được lý do cho lời nói của ông Guuji."
3015 = "Thực sự quan tâm đến đối phương. Bước vào và suy nghĩ cho đối phương. ——Tôi đã được dạy rằng, tôi cũng có thể làm được như vậy."
3330 = "Hiếm lắm mới có người mang đậm phong thái Hinomoto cổ kính và tốt đẹp đến nhường ấy——Ư!"
3391 = "（Cảm ơn em nhé. Vì đã cứu tôi——để tôi được sống.）"
```

Khối trên đã kiểm chứng: parse bằng tomllib được **55/55 keys**, giá trị khớp đúng JSON. Không còn dạng cũ nào trong khối sửa (0 "Ohimitera", 0 "Jussen"/"Jutsusen", 0 "Thẻ bảng"; 16 "Ohitoyo" thay cho "Ohimitera").

## Bằng chứng cho các quyết định đang chờ (ghi nhận, KHÔNG áp dụng)

- **Soutetsu gọi Paulette "cô" vs "em": "em" 7× (1751, 1967, 2117, 2121, 2247, 2412, 2425), "cô" 0× trong thoại.** Đây là file thứ 4 liên tiếp nghiêng về "em" (P13 0:2, P14 0:1, P15 0:1, P16 0:7) — cộng dồn P09–16: "cô" 43 vs "em" 14. **Mẫu mới: ranh giới rạch ròi theo chương** — P09–12 nghiêng hẳn về "cô" (43:3), P13–16 nghiêng hẳn về "em" (0:11). Có thể người dịch đổi tay ở chương 13, hoặc mối quan hệ thân mật hơn ở các chương sau — cần Hieu quyết xem thống nhất theo hướng nào (và có chia theo chương hay không). Suy nghĩ trong ngoặc của Soutetsu ở 3369 dùng "Cô" ("Cô tuyệt lắm đấy, Paulette") — ghi nhận riêng, không cộng vào đếm thoại. Các "cô ấy"/"cô" ngôi ba trong lời dẫn (2710, 2811, 2818, 2831, 2926) là đại từ ngôi ba, không tính. Paulette tự xưng theo người nghe: "tôi" 11 lần, "em" 2 lần (2015, 2385 — với Soutetsu), "cháu" 3 lần (1325, 1912, 2101 — với bộ trưởng/người lớn tuổi) — biến đổi đúng, không tính sai.
- **湯医: "Yui" 1× (2032, "24,8 km từ Ohitoyo đến Yui"), "Yunoi" 0×.** Cán cân toàn dự án vẫn nghiêng "Yunoi" (Grand 01 + 夜の嵐 + Paulette 10 (7×) + Paulette 11 (1×) vs "Yui" lẻ tẻ ở Paulette 14 (1×) và file này (1×)).
- **"KiHa 07": 3 gloss, tất cả đều là "Kiha" (1971, 2835, 3251), "KiHa" 0×.** File này không thêm bằng chứng cho "KiHa" — ngược lại, nó cho thấy dạng "Kiha" vẫn đang được dùng ở các chương cuối.
- **宮司 (đề xuất mới): file này dùng "ông Guuji" 4× (1708, 2292, 2933, 3304).** Kiểm tra toàn dự án: "đền chủ" 46×, "Cung tư tế" 11×, "Guuji" 9×. Ba dạng cùng tồn tại, không có dạng nào được docs quy định — đề xuất thống nhất về "đền chủ" (dạng đa số, đã dùng ở Paulette 15 cho 赤井宮司). Không tính là sai ở file này (docs không quy định).
- **Paulette gọi Soutetsu "cậu" vs "anh": đã sửa 4 dòng ở file này theo docs §2.4 ("Anh Soutetsu")** — nhưng còn 11 dòng "Cậu Soutetsu" trong lời Paulette ở các file chưa audit (ハチロク01 2210/2232, ハチロク02 2166, ハチロク05 3078, ハチロク11 2163, ハチロク14 2573/3256/3257, 稀咲03 2138, グランドリライト08 1702, 凪ふかみ08b 2436) sẽ cần sửa tương tự nếu Hieu xác nhận. Lưu ý: Minokasa gọi Soutetsu là "Cậu Soutetsu" là quy ước riêng đã được ghi nhận (夜の嵐 review) — KHÔNG phải trường hợp này, đừng sửa các dòng của Minokasa.
- **帝鉄: 1× (3219), dùng đúng dạng docs "Đường sắt Hoàng gia"** — không có gì để ghi nhận thêm. マスコン/操作板/タブレット/整備体/運転ボディ/運転体/冥国/冥軍/小畑/大畑/駿袋鉄道/端的/白湯/ぽわっと/廃駅: 0× trong file này. コン (cáo): 0× (3331 là từ khác có chứa コン, 3377 là tiếng gõ cửa （コンコン） → "Cốc cốc", đúng).

## Đề xuất cập nhật context (chưa chốt)

1. **宮司** — thống nhất về "đền chủ" (46×, dạng đa số) thay vì để ba dạng "đền chủ"/"Cung tư tế"/"Guuji" cùng tồn tại. Hieu quyết.
2. **Paulette gọi Soutetsu "cậu" cho 双鉄くん** — file này đã sửa 4 dòng theo docs; 11 dòng còn lại ở các file chưa audit cần xử lý tương tự khi audit tới đó (xem danh sách ở trên).
3. Các đề xuất đang chờ vẫn giữ nguyên: 湯医 "Yunoi" vs "Yui"; "cô" vs "em" (nay có thêm mẫu ranh giới theo chương P09–12 vs P13–16); 整備体/運転ボディ; "KiHa" vs "Kiha"; 帝鉄; コン; 駿袋鉄道; Migita System vs Migita Ichi; マスコン/マスターコントローラー.

## Đã kiểm tra và KHÔNG tính là sai

- **1708/2292/3304 [Soutetsu/lời dẫn]** — 宮司 dịch "ông Guuji": xem đề xuất thống nhất ở trên, không tính sai ở file này.
- **3236 [lời dẫn]** — "anh ta" là ngôi ba chỉ vị quan chức đi cùng (không phải Soutetsu tự xưng) — đúng, giữ nguyên.
- **1307 [lời dẫn]** — dương tính giả của heuristic (JP mở đầu bằng “ cong, VN mở đầu bằng " thẳng — cả hai đều là thoại).
- **1928/2087/2102/2426** — "em" trong "trẻ em"/"em gái"/"anh em sinh đôi" là dương tính giả của quét máy, không phải xưng hô.
- **1696/1723/1749/1852/1869/1898/1903/1943/2012/2013/2260/2400/2429/2453** — っ giữa từ (phụ âm đôi trong thán từ: なっ, えっ, いかんっ, よしっ…) được dịch đúng thành câu cảm thán tiếng Việt — không phải mất tiếng hít.
- **1325/1912/2101 [Paulette]** — tự xưng "cháu" với bộ trưởng/người lớn tuổi: đúng theo vai vế.
- **1806/2261 [Soutetsu]** — tự xưng "cháu" với người lớn tuổi (Nagayama/các quý phu nhân): đúng theo tiền lệ Paulette 05 (Soutetsu "cháu" với cụ Minokasa).
- **2246 [Reina]** — VN theo đúng JP (TW tự thêm 双鉄先生 vào câu của Reina — VN không theo TW, đúng quy tắc JP-trên-TW).
- **2321 [Paulette]** — địa danh viết bằng chữ Hán lạ nhưng đọc theo furigana JP (福丘→Fukuoka, 粉蔵→Kokura, 門次→Moji, 鹿兒島→Kagoshima, 枕咲→Makurazaki) — đúng theo tiền lệ 小畑→Okoba (theo cách đọc trong game, không theo chữ Hán).
- **3219 [lời dẫn]** — 帝鉄 dùng đúng dạng docs "Đường sắt Hoàng gia".
- **3377 [lời dẫn]** — （コンコン） là tiếng gõ cửa, dịch "Cốc cốc" — không phải cáo コン.
- **2931/3118/3185/3305 [lời dẫn]** — "em ấy" chỉ Reina/Michiko/Hibiki (ngôi ba): đúng.
- **3369 [lời dẫn]** — suy nghĩ trong ngoặc dùng "Cô" ("Cô tuyệt lắm đấy, Paulette"): ghi nhận làm bằng chứng "cô"/"em", không tính sai.

## Kết bài

Paulette 16 (55/542, 10,1%) — file sạch về cấu trúc (0 lệch vị trí, 0 chuỗi xoay vòng, 0 tràn chương, 0 dòng chưa dịch, 0 dòng chưa chắc chắn), nhưng là **file có tỉ lệ sai cao thứ hai trong nhóm Paulette 09–16** (10,1%, chỉ sau Paulette 13: 13,9%; trên Paulette 15: 8,8%) — cao vì xưng hô hệ thống: Soutetsu tự xưng "anh" trong 23/90 dòng thoại, 25,6%). Thuật ngữ 17 dòng thì quen thuộc (16 Ohitoyo + 1 Jutsusen). Bốn lỗi mất tiếng hít っ (2448, 2449, 2450, 3330) thuộc mẫu hệ thống đã biết — riêng "!" trơ trụi xuất hiện 206 lần trong toàn dự án, là ứng cử viên số một cho đợt quét thống nhất sau này. Điểm mới của file này: lần đầu tiên Paulette gọi Soutetsu là "cậu" bị tính là sai (4 dòng, theo docs §2.4 và tỉ lệ toàn dự án 470:13), và bằng chứng "cô" vs "em" lần đầu cho thấy ranh giới rạch ròi theo chương (P09–12: "cô"; P13–16: "em").

**Còn lại cho file này:** không còn gì — sau khi áp 55 bản sửa, file coi như xong, trừ các quyết định đang chờ Hieu chốt (đặc biệt "cô" vs "em" — nay có thêm giả thuyết ranh giới theo chương; và 宮司 — đề xuất thống nhất về "đền chủ").

**Tổng cộng: 28 file đã audit, 1.829 dòng sai** (27 file / 1.774 + 55).

**Tiếp theo:** route Paulette chính (chương 03–16 + Grand 04) đã audit xong toàn bộ. Còn lại trong thư mục 03_Paulette: chương mở đầu 01 (2 file) và 02 (2 file), các file h1–h8 (8 file, cảnh người lớn) và lr_h1/lr_h2/lr_稀咲h1/れいな02 (4 file).
