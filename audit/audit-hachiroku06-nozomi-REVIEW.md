# Audit — ハチロク06_のぞみ (01_Hachiroku)

- File: `01_Hachiroku/ハチロク06_のぞみ.txt.toml` — route Hachiroku, cảnh ở nhà tắm Tororyu-yu: Olivy quá nhiệt, làm mát bằng bồn nước lạnh, bàn về kéo dài tuổi thọ Railord, mua kem, quạt mát, ngủ chung hình chữ Xuyên.
- Đọc: **501/501 dòng script** (key 76–3513), đối chiếu từng dòng với JP + TW (CSV3). Không lấy mẫu.
- TOML md5: `f8bbef02ab93efa20463ffb54186c7f9`; **1 bản duy nhất, không trùng lặp**. CSV3 1 bộ 501 dòng, key khớp tuyệt đối 501/501, 0 ô VN trống.
- Lưu ý: 303 chênh lệch VN giữa TOML và CSV3 đều là kiểu đã biết — TOML làm phẳng `\n` thật thành khoảng trắng; CSV3 (literal `\n`) là chuẩn. Không có chênh lệch nội dung nào khác.
- Cơ sở tổng cộng (đã kiểm chứng với ROUTE-AUDIT.md dòng 1270): **100 file / 4.799 dòng sai**.

## §1. Kết quả

**31 dòng sai / 501 dòng = 6,2%.** Không có chuỗi xoay vòng, không có dòng mồ côi, không có dòng chưa dịch, không có trùng key, không có tràn file khác.

Phân loại:

| Loại | Số dòng | Key |
|---|---|---|
| Đại từ | 14 | 2309, 2346, 2378, 2381, 2455, 2456, 2467, 2618, 2830, 3088, 3271, 3276, 3329, 3339 |
| Thuật ngữ | 13 | 1636, 2145, 2148, 2197, 2242, 2243, 2384, 2454, 2485, 2561, 2798, 2881, 3269 |
| Sai nghĩa | 2 | 1664, 2279 |
| Sweep っ | 1 | 2402 |
| Format (rác annotation) | 1 | 2370 |

## §2. Chi tiết từng dòng sai

### Đại từ — Hachiroku ↔ Olivy (7 dòng)

Bằng chứng đã chốt trong dự án: **Olivy lớn tuổi hơn Hachiroku** — chính file này key 3455: JP 「オリヴィは冥国製、海外製で、ハチロクよりも古いのだ。」/ TW 「奧莉薇是進口的美國式鐵路人偶，並且年代比八六更加久遠」/ VN đúng 「Olivy được sản xuất tại Mỹ, là hàng ngoại nhập, và còn lớn tuổi hơn cả Hachiroku.」. Tiền lệ đã merge: ハチロク15a keys 1947/2560 (Hachiroku tự xưng "em", Olivy là "chị"). Vì vậy trong file này: Hachiroku gọi Olivy là **"chị"**, tự xưng **"em"**; các dòng dùng "em" cho Olivy và "chị" cho Hachiroku là sai chiều.

- **2309 [ハチロク]** — JP 「ああいえ、オリヴィちゃんは病み上がりなのですから。バニラとイチゴ、どちらを最初に召し上がりますか？」/ TW 「啊不是，我這是考慮到你才剛剛康復不能吃太急，那你想先吃香草味還是草莓味？」/ Cũ: 「À không, vì bé Olivy mới vừa ốm dậy mà.\nVani và dâu tây, em muốn ăn vị nào trước?」 → **「À không, vì bé Olivy mới vừa ốm dậy mà.\nVani và dâu tây, chị muốn ăn vị nào trước?」** ("em"→"chị" cho Olivy)
- **2381 [ハチロク]** — JP 「うふふ、よかった。ふたくちめは、どちらを？」/ TW 「嘻嘻，那就好。那你第二口想吃哪一個？」/ Cũ: 「Ufufu, tốt quá rồi.\nMiếng thứ hai em muốn ăn vị nào?」 → **「Ufufu, tốt quá rồi.\nMiếng thứ hai chị muốn ăn vị nào?」**
- **2455 [ハチロク]** — JP 「オリヴィちゃん、暑くはありませんか？」/ TW 「奧莉薇，你可還覺得熱呀？」/ Cũ: 「Bé Olivy, em có thấy nóng không?」 → **「Bé Olivy, chị có thấy nóng không?」**
- **2456 [ハチロク]** — JP 「オリヴィちゃん、なにかほしいものはありませんか？」/ TW 「奧莉薇，你有什麼想要的嗎？」/ Cũ: 「Bé Olivy, em có muốn ăn gì không?」 → **「Bé Olivy, chị có muốn ăn gì không?」**
- **2467 [ハチロク]** — JP 「かしこまりました。はい、『あーん』」/ TW 「好的。來，“啊——”」/ Cũ: 「Chị hiểu rồi. Nào, 'A' đi.」 → **「Em hiểu rồi. Nào, 'A' đi.」** (Hachiroku tự xưng "chị" là sai chiều — với Soutetsu và với Olivy cô đều xưng "em"; các dòng 2483, 2506, 2723 đều "em")
- **2378 [ハチロク]** — JP 「うふふ、ありがとうございます。たいへん、ここちようございます」/ TW 「嘻嘻，謝謝你奧莉薇，我也感到非常涼爽」 (TW ghi rõ người được cảm ơn là Olivy — cô bé đang quạt cho Hachiroku, cf. 2448 Olivy 「ぱたぱた～」; dòng kề 2381 cũng nói với Olivy) / Cũ: 「Ufufu, cảm ơn cô.\nRất là, dễ chịu ạ」 → **「Ufufu, cảm ơn chị.\nRất là, dễ chịu ạ」** ("cô" sai — Hachiroku không gọi Olivy là "cô"; Olivy lớn tuổi hơn nên là "chị")

Các dòng "chị" cho Olivy đã đúng, giữ nguyên: 2457, 2458, 2473, 2483, 2504, 2620.

- **2346 [オリヴィ]** — JP 「んと――両方ちょーだい！かわりばんこに食べるから」/ TW 「嗚——都給奧莉薇！奧莉薇要換著吃」 ("Cho Olivy cả hai! Olivy sẽ ăn luân phiên"). Cũ: 「Ưm――cho chị cả hai luôn đi!\nChị sẽ ăn luân phiên.」 → **「Ưm――cho Olivy cả hai luôn đi!\nOlivy sẽ ăn luân phiên.」** ("chị" ở đây vừa sai hướng (nếu là Hachiroku thì kem lại đưa cho Hachiroku) vừa sai tự xưng (Olivy nhỏ tuổi hơn Hachiroku, không tự xưng "chị"); Olivy trong file luôn tự gọi tên mình — 2446, 2451, 2453, 2599, 2609, 2638, 2710.)

### Đại từ — Soutetsu (5 dòng)

- **2830 [双鉄]** — JP 「まず、僕らと宗方機関士――みかん鉄道で、Ⅸ号に乗務していた機関士との会話内容を説明しよう」/ Cũ: 「Đầu tiên, anh sẽ giải thích nội dung cuộc trò chuyện giữa chúng ta và \x%l機関士;#00ffc040;Lái tàu%l;#; Munakata――\x%l機関士;#00ffc040;Lái tàu%l;#; từng làm việc trên đầu máy số 9 ở Đường sắt Mikan」 → **「Đầu tiên, tôi sẽ giải thích …」** ("anh"→"tôi": Soutetsu kể lại chuyện Munakata cho **cả nhóm** đang có mặt — Hibiki, Mayami, Hachiroku, Olivy, bà chủ; dòng trước/sau đều là Mayami (2826, 2833). Tiền lệ Paulette 14 key 1544 và ハチロク15a (nhóm → "tôi"). Các "anh" với Hibiki giữ nguyên: 2216, 2565, 2626.)
- **3088 [monologue]** — JP 「ハチロクが、日々姫が、すがる視線で僕をみる。」/ Cũ: 「Hachiroku và chị Hibiki nhìn tôi bằng ánh mắt cầu cứu.\nNhưng…… quyết định chuyện này quả thực khá khó khăn.」 → **「Hachiroku và em Hibiki nhìn tôi bằng ánh mắt cầu cứu.…」** (độc thoại của Soutetsu; Hibiki là em gái ruột của Soutetsu — cô gọi anh là にぃにぃ — nên trong lời kể của anh cô là "em", không phải "chị")
- **3276 [monologue]** — JP 「オリヴィを布団の上へと寝かせれば、あっという間に日々姫が夏掛けを腹へとかける。」/ Cũ: 「Vừa đặt Olivy nằm xuống nệm,\nchị Hibiki đã nhanh thoăn thoắt đắp chăn hè lên bụng em ấy.」 → **「Vừa đặt Olivy nằm xuống nệm,\nem Hibiki đã nhanh thoăn thoắt đắp chăn hè lên bụng em ấy.」**
- **3329 [monologue]** — JP 「幼いころの日々姫も、ああして、ぱたぱた、真闇姉に、僕に、あおがれていた――」/ Cũ: 「Chị Hibiki hồi nhỏ cũng từng được chị Mayami,\nvà cả tôi quạt cho như thế――」 → **「Em Hibiki hồi nhỏ cũng từng được chị Mayami,\nvà cả tôi quạt cho như thế――」**
- **3339 [monologue]** — JP 「日々姫があわてて剥がそうとした夏掛けが、縫い付けられているかのように動かなくなる。」/ Cũ: 「Chị Hibiki cuống cuồng định kéo chăn hè ra,\nnhưng chiếc chăn lại không nhúc nhích, cứ như bị khâu chặt vào nệm vậy.」 → **「Em Hibiki cuống cuồng định kéo chăn hè ra,…」**

"chị Hibiki" trong thoại của Hachiroku là đúng, giữ nguyên: 2302, 2848.

### Đại từ — giới tính bà chủ nhà tắm Tororyu-yu (2 dòng)

Bà chủ là **nữ**: xưng hô trực tiếp "bà" 3 lần trong file (2614 Soutetsu 「bà cũng hầu như không giao lưu」, 2646 Soutetsu 「Nếu bà không phiền」, 2842 Hachiroku 「bà có biết ai không ạ?」) + "bà chủ" 7 lần (1550, 1552, 2607, 3129, 3378, 3434, 3453) + tự xưng ウチ (2271) + vai trò chăm lo cho Reina và Hachiroku. Chỉ 2 dòng độc thoại viết nhầm "ông chủ".

- **2618 [双鉄]** — JP 「そういうわけで、登呂流湯のご主人に診断をお願いし、オリヴィの冷却中に、延命法についてをお伺いした」/ Cũ: 「Vì vậy, chúng tôi đã nhờ ông chủ nhà tắm Tororyu-yu chẩn đoán,\nvà trong lúc làm mát cho Olivy, đã hỏi về phương pháp kéo dài tuổi thọ」 → **「Vì vậy, chúng tôi đã nhờ bà chủ nhà tắm Tororyu-yu chẩn đoán,…」**
- **3271 [monologue]** — JP 「筋道立てて順序よく、登呂流湯のご主人から聞いた話を、僕なりに整頓し、伝えていけてるような気がする。」/ Cũ: 「Những câu chuyện nghe được từ ông chủ nhà tắm Tororyu-yu,\ncó vẻ tôi đã sắp xếp và truyền đạt lại một cách mạch lạc, rõ ràng.」 → **「Những câu chuyện nghe được từ bà chủ nhà tắm Tororyu-yu,…」**

### Thuật ngữ (13 dòng)

- **エアクラ → "Aircra" (9 dòng)** — thuật ngữ đã chốt: エアクラ="Aircra". File này dùng lẫn lộn: 7 dòng đã đúng "Aircra" (1656, 1665, 2410, 2687, 2722, 2728, 2868), 9 dòng sai "Aerocraft": **1636** 「…chính vì Aerocraft đã lấy đi toàn bộ…」 → Aircra; **2148** 「bán Aerocraft hóa đường sắt」 → 「bán Aircra hóa đường sắt」; **2197** 「so với Aerocraft chạy trên mặt đất ạ」 → Aircra; **2243** 「không thắng nổi Aerocraft」 → Aircra; **2454** 「không rành về Aerocraft lắm」 → Aircra; **2485** 「xe ô tô Aerocraft」 → 「xe ô tô Aircra」; **2561** 「những người chuyển sang Aerocraft」 → Aircra; **2798** 「xe Aerocraft chỉ khoảng 60km/h」 → 「xe Aircra」; **3269** 「Navi hóa Aerocraft cho Railord」 → 「Navi hóa Aircra cho Railord」. (Chỉ đổi đúng từ Aerocraft→Aircra, giữ nguyên tag %l và phần còn lại.)
- **2145 [ハチロク]** — JP 「いわゆるマスコン。マスタアコントロオラアのことでございます」/ Cũ: 「Hay còn gọi là \x%lマスコン;#00ffc040;điều khiển trung tâm%l;#;.\nMaster Controller đó ạ.」 → **「Hay còn gọi là \x%lマスコン;#00ffc040;điều khiển trung tâm%l;#;.\nĐiều khiển trung tâm đó ạ.」** (マスコン/マスターコントローラー = "điều khiển trung tâm" theo thuật ngữ đã chốt; dòng 1592 trong file đã dùng đúng.)
- **2384 [双鉄]** — JP 「ああ――聞かせてもらったことがあるな。帝鉄末期の電車などには、すでに配備が開始されていたという」/ Cũ: 「A――Tôi đã từng nghe nói về nó rồi. Nghe nói vào cuối thời kỳ Đường sắt Hoàng gia,\nnó đã bắt đầu được trang bị trên các \x%l電車;#00ffc040;tàu điện%l;#; và những phương tiện tương tự.」 → **「…Nghe nói vào cuối thời kỳ Teitetsu,…」** (帝鉄="Teitetsu"; "Đường sắt Hoàng gia" là dạng cũ đã sửa ngày 19/11.)
- **2242 [オリヴィ] + 2881 [日々姫] — 電車姫/デンシャヒメ** — JP 2242 「って、ソーテツたち、デンシャヒメとコネあるの？」/ JP 2881 「電車姫さま！！」/ TW cả hai đều 「電車公主」 ("Train Princess"). Cũ: 「…có quan hệ với Điện xá Công chúa sao?」 / 「Điện xá Công chúa điện hạ!!」 → **「…có quan hệ với Công chúa Tàu điện sao?」** / **「Công chúa Tàu điện điện hạ!!」** ("Điện xá" là phiên âm sai — 電車 là "điện xa", "xá" 舍 nghĩa là nhà/lều, không phải từ tiếng Việt; "Công chúa Tàu điện" là dạng đã dùng ở các file ハチロク04, ハチロク14, lr追加. Lưu ý: toàn dự án đang có 5+ dạng khác nhau cho nhân vật này — xem §6.)

### Sai nghĩa (2 dòng)

- **1664 [登呂流湯主人]** — JP 「……そいば、どぎゃん路ね」/ TW 「這的確是一條了不起的路呀」 ("Đây đúng là một con đường đáng nể"). Cũ là câu hỏi: 「……Vậy, đó là con đường như thế nào?」 → **「……Đúng vậy, quả là một con đường tuyệt vời nhỉ.」** (JP どぎゃん路ね là câu cảm thán đồng tình, không phải câu hỏi; TW xác nhận.)
- **2279 [日々姫]** — JP 「あわわ！？　そぎゃんと？　なら、夏掛けば」/ TW 「哇哇！？怎麼還這樣的？那不鋪了」 ("Thế thì khỏi trải [chăn] ra nữa"). Cũ viết ngược nghĩa: 「A wa wa!? Vậy sao? Thế thì, lấy chăn hè ra――」 → **「A wa wa!? Vậy sao? Thế thì, khỏi trải chăn hè――」** (Hibiki từ chối dùng chăn hè; dòng 2292 Hachiroku năn nỉ lại "Nếu thế thì em cũng muốn để chị dùng chăn hè" khớp với cách đọc này.)

### Sweep っ (1 dòng)

- **2402 [双鉄]** — mục sweep `lost-gasp-trailing-mid`, đã kiểm chứng đúng với JP: JP 「ほう、冷却には水風呂を使って――っ！\nひょっとしてそのために温泉施設を？」/ TW 「噢，用浴池裝滿水降溫——啊！」/ Cũ: 「Ồ, dùng bồn nước lạnh để hạ nhiệt――!\nKhông lẽ cơ sở suối nước nóng này được xây dựng vì mục đích đó sao?」 → **「Ồ, dùng bồn nước lạnh để hạ nhiệt――Ư!\nKhông lẽ cơ sở suối nước nóng này được xây dựng vì mục đích đó sao?」** (chèn Ư sau ――, giữ nguyên \n từ CSV3.)
- 2 mục sweep còn lại của file đã kiểm tra, không sửa: 2257 (「っ！」→「Ưm!」, đã diễn) và 2329 (「っ！」→「A!」, đã diễn) — đều thuộc loại `already-rendered`.

### Format (1 dòng)

- **2370 [双鉄]** — JP 「うむ。ある。あの方は[ハチロク,3]8620の熱心なファンだしな」/ TW 「嗯，有辦法。畢竟她可是[八六,3]８６２０的死忠粉絲」/ Cũ: 「Ừ. Có chứ.\nVị đó là fan cuồng của dòng [8620'86] mà」 → **「Ừ. Có chứ.\nVị đó là fan cuồng của dòng 8620 mà」** ("[8620'86]" là rác annotation bị biến dạng, vô nghĩa; quy ước trong chính file này là bỏ annotation [ハチロク,3] — cf. 2756, 2849.)

## §3. Kiểm tra sweep っ cho file này

- `sweep-raw-gasp-wrong.json` có 3 mục cho file này (không phải 0): 2402 (áp dụng, xem trên), 2257 + 2329 (`already-rendered`, giữ nguyên). Không có mục sweep nào khác bị bỏ sót.

## §4. Kiểm tra cấu trúc

- 0 dòng chưa dịch, 0 trùng key (501 key duy nhất), 0 dòng mồ côi (không có dòng VN nào không tìm được JP/TW tương ứng trong dự án), 0 chuỗi xoay vòng, 0 tràn file khác.
- Tag %l: số lượng tag JP = VN trên mọi dòng, 0 mất cân bằng mở/đóng; 0 dấu 「 」 lệch. Các annotation ruby [X,n] được xử lý theo quy ước của file (bỏ, trừ 2671 giữ `[Occident Express,3]` theo TW — xem §6).
- Các dòng đã kiểm tra kỹ nhưng giữ nguyên (không tính sai): 1660 博太→"Hakuta" (xem §6), 2177 Olivy 「ならって――なんで？」→"Vậy á――tại sao?" (mơ hồ nhưng không sai rõ), 2456 "muốn ăn gì" (hẹp nghĩa theo ngữ cảnh quán kem, TW không phản bác), 2444 "Olivy cũng chưa" (lược theo ngữ cảnh), 2671 giữ `[Occident Express,3]` (giống TW), 2248 "Cậu nhà Migita" (diễn giải hợp lý cho 右田のは), 2412 "thay thế cô ấy" (ngôi thứ ba cho Paulette là chuẩn), 2870 "Chị Hai" (TW 阿姐), Soutetsu tự xưng "tôi" với Olivy (quy tắc chưa bao phủ Olivy; xem §6).

## §5. Lượt soát 2 (bắt buộc)

Đọc lại toàn bộ 31 fix đối chiếu JP lần 2: **31 tổng / 31 kiểm chứng lại / 0 bỏ / 0 sửa**. Không fix nào bị loại hay sửa lại ở lượt 2.

Kiểm chứng cơ học: JSON 31 mục dạng chuẩn (key dạng string, đủ jp/tw/old_vn/fix/kind/character); jp/tw/old_vn khớp CSV3 tuyệt đối 31/31; khối TOML 31 khóa, parse được bằng tomllib, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô, kể cả `\n` literal); mỗi fix chỉ khác VN cũ ở đúng chỗ cần sửa (kiểm tra diff từng dòng).

## §6. Chờ Hieu (không tính sai, không tự quyết)

1. **1660 博太 → "Hakuta"?** JP: 「……博太によーさん観光にきよる海外のお客さんば、九洲全土に、おまねきできるかもしれんねぇ」/ TW: 「……說不定就能讓那些專程來參觀博多２３景的國外旅客，對九州全域產生興趣」 (TW đọc là 博多/Hakata). VN hiện tại: 「……Những vị khách nước ngoài đến Hakuta du lịch,…」. "博太" không phải địa danh thật; có thể là cách viết phương ngữ/typo của 博多 trong game. JP thắng TW nên giữ "Hakuta" cho đến khi Hieu chốt — cần Hieu quyết: giữ "Hakuta" theo đúng mặt chữ JP, hay sửa thành "Hakata" theo TW?
2. **Điện xá Công chúa / Densha-hime chưa thống nhất toàn dự án.** Các dạng đang tồn tại: "Điện xá Công chúa" (file này + ハチロク07), "Công chúa Tàu điện" (ハチロク04, ハチロク14, lr追加), "Công chúa Xe điện" (ポーレット09 2262), "Densha Hime" (ハチロク09/10/16, ポーレット09/13, グランド04), "Denshahime" (ハチロク11/13, グランド07/08), "Điện Xa Cơ" (グランド10). File này đã sửa về "Công chúa Tàu điện" (2 dòng); cần đợt thống nhất toàn dự án.
3. **Ruby [X,n] chưa thống nhất.** File này bỏ annotation ở 2248/2370/2407/2410/2641/2756/2849 nhưng giữ `[Occident Express,3]` ở 2671 (giống TW). ROUTE-AUDIT.md đã ghi chú chờ quyết.
4. **Olivy xưng "cậu" với Soutetsu/Hachiroku** (2322, 2382, 2499, 2500: "cậu đi nhanh hơn chút nữa được không?", "cảm ơn cậu nhiều nha~") — giữ nguyên theo quy ước của file (giọng trẻ con, suồng sã của Olivy), nhưng nếu Hieu muốn đổi thì báo.
5. **Soutetsu tự xưng với Olivy: "tôi" hay "anh"?** File này dùng "tôi" nhất quán (2180, 2459, 2591, 2572…); file ハチロク15a đã giữ một dòng "anh" với Olivy (không tính sai). Quy tắc đại từ chưa bao phủ Olivy — cần Hieu chốt để thống nhất về sau.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
1636 = "「……Nói ngược lại, chính vì Aircra đã lấy đi toàn bộ\\ncái cảm giác 'muốn đi thử' đó, nên mới xảy ra Đại bãi bỏ」"
1664 = "「……Đúng vậy, quả là một con đường tuyệt vời nhỉ.」"
2145 = "「Hay còn gọi là \\x%lマスコン;#00ffc040;điều khiển trung tâm%l;#;.\\nĐiều khiển trung tâm đó ạ.」"
2148 = "「――Nói cách khác, bán Aircra hóa đường sắt. Vì có quá nhiều người\\nhướng tới mục tiêu đó, nên kỹ thuật kéo dài tuổi thọ cho \\x%lレイルロオド;#00ffc040;Railord%l;#; hiện tại thì」"
2197 = "「Thêm vào đó là tính đúng giờ. Về việc không bị chậm trễ,\\nđường sắt vẫn có lợi thế hơn so với Aircra chạy trên mặt đất ạ」"
2242 = "「Khoan, mấy người Soutetsu, có quan hệ với Công chúa Tàu điện sao?」"
2243 = "「Thế nên, vì tính thực dụng không thắng nổi Aircra,\\nđường sắt mới bị Đại bãi bỏ làm cho tơi tả đó thôi」"
2279 = "「A wa wa!? Vậy sao? Thế thì, khỏi trải chăn hè――」"
2309 = "「À không, vì bé Olivy mới vừa ốm dậy mà.\\nVani và dâu tây, chị muốn ăn vị nào trước?」"
2346 = "「Ưm――cho Olivy cả hai luôn đi!\\nOlivy sẽ ăn luân phiên.」"
2370 = "「Ừ. Có chứ.\\nVị đó là fan cuồng của dòng 8620 mà」"
2378 = "「Ufufu, cảm ơn chị.\\nRất là, dễ chịu ạ」"
2381 = "「Ufufu, tốt quá rồi.\\nMiếng thứ hai chị muốn ăn vị nào?」"
2384 = "「A――Tôi đã từng nghe nói về nó rồi. Nghe nói vào cuối thời kỳ Teitetsu,\\nnó đã bắt đầu được trang bị trên các \\x%l電車;#00ffc040;tàu điện%l;#; và những phương tiện tương tự.」"
2402 = "「Ồ, dùng bồn nước lạnh để hạ nhiệt――Ư!\\nKhông lẽ cơ sở suối nước nóng này được xây dựng vì mục đích đó sao?」"
2454 = "「Olivy thì không rành về Aircra lắm nhưng――\\nvì nó có điểm yếu nên đường sắt mới tồn tại được đúng không?」"
2455 = "「Bé Olivy, chị có thấy nóng không?」"
2456 = "「Bé Olivy, chị có muốn ăn gì không?」"
2467 = "「Em hiểu rồi. Nào, 'A' đi.」"
2485 = "「Vượt xa xe ô tô Aircra――ví dụ như nếu có một tuyến tàu điện siêu tốc\\nnối liền Teiou và Ousaka với tốc độ 200km/h thì sao」"
2561 = "「Vậy thì, những người chuyển sang Aircra cũng không có lỗi.\\nNếu chúng ta có thể――lát lại đường ray đưa họ về với đường sắt một lần nữa」"
2618 = "「Vì vậy, chúng tôi đã nhờ bà chủ nhà tắm Tororyu-yu chẩn đoán,\\nvà trong lúc làm mát cho Olivy, đã hỏi về phương pháp kéo dài tuổi thọ」"
2798 = "「Không chỉ vậy, nhu cầu sử dụng cho công việc cũng sẽ quay lại. Loại chạy trên mặt đất――\\nTốc độ hành trình trung bình của xe Aircra chỉ khoảng 60km/h thôi」"
2830 = "「Đầu tiên, tôi sẽ giải thích nội dung cuộc trò chuyện giữa chúng ta và \\x%l機関士;#00ffc040;Lái tàu%l;#; Munakata――\\x%l機関士;#00ffc040;Lái tàu%l;#; từng làm việc trên đầu máy số 9 ở Đường sắt Mikan」"
2881 = "「Công chúa Tàu điện điện hạ!!」"
3088 = "Hachiroku và em Hibiki nhìn tôi bằng ánh mắt cầu cứu.\\nNhưng…… quyết định chuyện này quả thực khá khó khăn."
3269 = "Navi hóa Aircra cho \\x%lレイルロオド;#00ffc040;Railord%l;#;.\\nKhông ngờ Olivy lại tán thành điều đó――"
3271 = "Những câu chuyện nghe được từ bà chủ nhà tắm Tororyu-yu,\\ncó vẻ tôi đã sắp xếp và truyền đạt lại một cách mạch lạc, rõ ràng."
3276 = "Vừa đặt Olivy nằm xuống nệm,\\nem Hibiki đã nhanh thoăn thoắt đắp chăn hè lên bụng em ấy."
3329 = "Em Hibiki hồi nhỏ cũng từng được chị Mayami,\\nvà cả tôi quạt cho như thế――"
3339 = "Em Hibiki cuống cuồng định kéo chăn hè ra,\\nnhưng chiếc chăn lại không nhúc nhích, cứ như bị khâu chặt vào nệm vậy."
```

## Kết bài

File ハチロク06_のぞみ: đọc 501 dòng, sai 31 dòng (6,2%) — nhẹ hơn nhiều so với mức trung bình dự án (~10%). Lỗi tập trung ở đại từ (14: cặp Hachiroku↔Olivy theo bằng chứng 3455 trong chính file, "chị Hibiki" trong độc thoại Soutetsu, giới tính bà chủ, xưng hô nhóm ở 2830) và thuật ngữ (13: "Aerocraft" 9 dòng chưa đổi sang "Aircra", "Master Controller", "Đường sắt Hoàng gia", "Điện xá Công chúa"). Không có lỗi hệ thống (xoay vòng, mồ côi, tràn file). Hai lỗi nghĩa nặng nhất là 1664 (câu cảm thán bị dịch thành câu hỏi) và 2279 (nghĩa ngược: lấy chăn ra thay vì khỏi trải chăn). 5 điểm chờ Hieu đã ghi ở §6, trong đó quan trọng nhất là 博太/Hakuta ở 1660 và việc thống nhất tên gọi Densha-hime toàn dự án.
