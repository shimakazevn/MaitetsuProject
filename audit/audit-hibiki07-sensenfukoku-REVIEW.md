# Audit: 日々姫07_たったひとりの宣戦布告 — 20 dòng Việt sai (đã đối chiếu JP + TW)

**Kết quả: 20/400 dòng sai (5,0%)** — sweep 4, sfx 8, đại từ 5, nghĩa 3. 0 lệch dòng, 0 chuỗi xoay, 0 tràn file khác, 0 dòng chưa dịch, 0 trùng key. Cảnh: buổi sáng ở nhà Migita — Hibiki ngủ nướng, Soutetsu và Hachiroku lo lắng; Kisaki đến xem sổ phác thảo, rủ Hibiki lập hội đồng hào và tuyên chiến với những kẻ cười nhạo tranh của em; xen kẽ độc thoại của Hibiki về giấc mơ, về Kuma Kuma và về việc trở thành người lớn.

## Phương pháp và số liệu kiểm chứng

- Đọc ngữ nghĩa **từng dòng trong 400 dòng script** (lời dẫn/monologue 160, 日々姫 133, 双鉄 64, ハチロク 24, 稀咲 19) đối chiếu JP + TW từ CSV3 "Trang tính 3", target là TOML-2. Key trong TOML xếp theo thứ tự số, trùng thứ tự trong file.
- CSV3 chỉ có **1 bộ 400 dòng** cho file này (không có dual-set); 0 key trùng, 0 dòng VN trống, 0 dòng VN == TW (1324 「…………」 trùng nhau chỉ vì toàn dấu chấm lửng, không phải chưa dịch).
- TOML khớp CSV3 về nội dung tuyệt đối: 249 dòng khác nhau chỉ ở chỗ TOML-2 làm phẳng `\n` thành khoảng trắng — 0 khác biệt nội dung thực sự. CSV3 (literal `\n`) là chuẩn cho danh sách sửa. `[selections]` có mặt nhưng rỗng ({}).
- TOML md5 `97ca6eb7d92b39522d73c2d45245eb4f` (UTF-8 BOM + CRLF); **không có file TOML trùng nội dung** (đã kiểm tra cả 227 file trong toml2/ — file này chỉ có 1 bản).
- **Sweep っ:** kiểm tra trực tiếp `sweep-raw-gasp-wrong.json` — file này có **4 mục** (1949, 2166, 2168, 2169, đều raw-tsu). Cả 4 giá trị đã kiểm chứng đúng với JP và được áp nguyên văn.
- **Quét っ hệ thống** trên toàn bộ dòng JP chứa っ (không chỉ dựa vào sweep): các dòng còn lại đều là っ trong từ (ほっと, まったく…), っ nhấn mạnh cuối câu (けどっ, でっ, そっか… — không phải gasp, không thêm Ư), hoặc âm đã được render (んっ→"ưm", えっ→"Hả", あっ→"A", うきゃあっっ→"U kyaaaaaaa!"). Chỉ còn 2 gasp sweep bỏ sót bắt được khi quét bổ sung: 1333 (ぁぅっ) và 1728 (ぇぅっ) — cả hai đều mất âm ぅ, VN chỉ còn "A.".
- **Quét fa/fu hệ thống** trên toàn bộ JP chứa ふぁ/ふあ/ふぇ/ふえ/ふや: 1720, 1727, 1742, 1759 đều sai theo quy tắc đã chốt (xem chi tiết); 2430 (はうぅ) sai theo tiền lệ はう→"Hau". Không còn dòng fa/fu nào khác trong file.
- **Chuỗi xoay:** không có VN trùng lặp trong file (ngoài 「…………」); không dòng nào có VN đúng nằm ở key khác. **Tràn file khác:** đối chiếu từng VN của file này với chỉ mục VN toàn dự án (CSV3) — 19 VN trùng ở file khác đều là câu ngắn chung chung ("Tất nhiên rồi.", "Cảm ơn vì bữa ăn.", "Ra là vậy, ra là vậy.", "Quả nhiên là vậy.", "Được vậy thì tốt quá.") vốn lặp lại hợp lệ; **0 dòng tràn file khác**.
- **Quét đại từ:** Soutetsu tự xưng "anh" đúng trong mọi dòng có đại từ (30/64 dòng; các dòng còn lại không có đại từ — 0 dòng "tôi" tự xưng sai); Hachiroku gọi Hibiki "chị" nhất quán (1637, 1828, 2156, 1928); Hibiki gọi Hachiroku "chị"/"em" nhất quán theo cặp; Hibiki chỉ dùng "tớ" ở đúng 2 dòng (1883, 1981 — cả hai đều sai, xem chi tiết).
- Phân loại lỗi: sweep 4, sfx 8, đại từ 5, nghĩa 3. Theo người nói: 日々姫 11, 双鉄 3 (1797, 1849, 1949 — 1949 tính theo người nói), monologue 5, 稀咲 0, ハチロク 0. **Chưa chắc chắn 0 dòng.**
- 2033 義兄→"anh trai nuôi": **giữ nguyên, không tính sai** — TW nói 義兄, đúng ngoại lệ đã chốt (file 14 keys 2206/2317).
- Độc thoại Hibiki xưng "tôi"/"mình" lẫn lộn (vd. 2351, 2405, 2428 "tôi" vs 2344, 2362 "mình"): **giữ nguyên, không tính sai** — theo tiền lệ pilot, "tôi" là dạng mặc định an toàn, "mình" chỉ là ngoại lệ cho phép trong độc thoại tự vấn cảm xúc, không bắt buộc.

## Kết luận về cơ chế lỗi

Không có lỗi hệ thống (lệch dòng / xoay vòng / nhiễm chéo) trong file này — toàn bộ 20 lỗi đều là lỗi dịch tại chỗ, rải rác. Nhóm lớn nhất là SFX/tiếng thở (12 dòng kể cả sweep): Gemini dịch các tiếng thở ふぁ/ふあ/ふぇ/ふえ thành "Hả?"/"Oa." (mất phụ âm đầu "ph"), và bỏ sót các gasp っ đứng một mình hoặc dính sau nguyên âm nhỏ (ぁぅっ, ぇぅっ). Nhóm đại từ (5 dòng) đều là lỗi xưng hô theo người nghe: Hibiki dùng "tớ" với senpai/anh trai, Hibiki dùng "chị" với Kisaki, và hai lần Soutetsu tự sửa 真闇さん→真闇姉 bị viết trùng thành "chị Mayami——chị Mayami" (mất hẳn ý tự sửa).

## Chi tiết dòng sai

### Sweep っ (4 dòng — áp nguyên giá trị sweep đã kiểm chứng)

**1949 [日々姫]** — sweep raw-tsu. JP gasp っ đứng một mình sau "あむっ", VN còn để nguyên chữ Nhật.

- JP: 「いただきます――あむっ――っ！！！」
- TW: 「我開動了——啊嗚——嗯！！！」
- Cũ: 「Chị ăn đây——Amu——っ!!!」
- Sửa: 「Chị ăn đây——Amu——Ư!!!」

**2166 [双鉄]** — sweep raw-tsu. Hai dòng toàn gasp っ, VN còn để nguyên chữ Nhật.

- JP: 「っ」\n「っ！」
- TW: 「！」\n「！」
- Cũ: 「っ」\n「っ!」
- Sửa: 「Ư」\n「Ư!」

**2168 [双鉄]** — sweep raw-tsu.

- JP: 「っ！！」
- TW: 「！！」
- Cũ: 「っ!!」
- Sửa: 「Ư!!」

**2169 [日々姫]** — sweep raw-tsu.

- JP: 「っ！！？」
- TW: 「！！？」
- Cũ: 「っ!!?」
- Sửa: 「Ư!!?」

### SFX (8 dòng)

**1333 [日々姫]** — sweep BỎ SÓT: JP ぁぅっ (a-u + ngắt giọng), VN chỉ còn "A." — mất hẳn âm ぅ và dấu ngắt. Theo công thức độ dài nguyên âm (ぁぅ có 1 ぅ → 2 nguyên âm), sửa thành "A ư."; っ cuối là ngắt giọng nhấn mạnh trên SFX đã diễn, không phải gasp riêng (tiền lệ ふぇぇぇええっ) nên không thêm Ư.

- JP: 「……ぁぅっ」
- TW: 「……啊嗚」
- Cũ: 「……A.」
- Sửa: 「……A ư.」

**1728 [日々姫]** — sweep BỎ SÓT, cùng mẫu với 1333: JP ぇぅっ (e-u + ngắt giọng), VN chỉ còn "A." — mất cả hai âm. ぇぅ có 1 ぅ → 2 nguyên âm: "E ư.".

- JP: 「ぇぅっ」
- TW: 「哎」
- Cũ: 「A.」
- Sửa: 「E ư.」

**1720 [日々姫]** — ふぇっ dịch thành "Hả?" — sai âm: ふぇ là tiếng thở, không phải "hả?" (tiền lệ: ふぇ→"phuê"; ふぇ→"Hể" đã bị sửa ở file khác vì cùng lý do). っ nhấn mạnh, giữ dấu "?".

- JP: 「ふぇっ？」
- TW: 「呼哎？」
- Cũ: 「Hả?」
- Sửa: 「Phuê?」

**1727 [日々姫]** — ふあっ dịch thành "Hả!?" — sai âm: quy tắc đã chốt ふあっ→"phù" (tiền lệ lr_凪h2, 19 dòng).

- JP: 「ふあっ！？」
- TW: 「哇啊！？」
- Cũ: 「Hả!?」
- Sửa: 「Phù!?」

**1742 [日々姫]** — ふえっ dịch thành "Hả!?" — sai âm: tiền lệ ふえっ→"phuê" (đối chiếu 929 trong file h1/h2).

- JP: 「ふえっ！？　なにそれっ」
- TW: 「哎！？什麼意思」
- Cũ: 「Hả!? Gì vậy chứ.」
- Sửa: 「Phuê!? Gì vậy chứ.」

**1759 [日々姫]** — ふぁっ dịch thành "Oa." — mất âm "ph": tiền lệ 08b 2174/2176 (ふぁっ→"Phà") và lr_凪h2 (ふぁ→"phà", 38 dòng).

- JP: 「ふぁっ」
- TW: 「啊……」
- Cũ: 「Oa.」
- Sửa: 「Phà.」

**1785 [日々姫]** — tiếng hét dài thiếu 1 âm a: JP あ×7 sau きゃ, VN chỉ có a×6.

- JP: 「うきゃあああああああっっ！」
- TW: 「嗚哇啊啊啊啊啊啊！」
- Cũ: 「U kyaaaaaa!」
- Sửa: 「U kyaaaaaaa!」

**2430 [monologue]** — はうぅ dịch thành "Hya!" — sai âm: tiền lệ はうっ→"Hau" (giữ âm Nhật, không diễn thành lời khác). Công thức độ dài nguyên âm: はうぅ có 2 âm う/ぅ → 3 nguyên âm "Hauu".

- JP: はうぅ！　これ、ダメっっ！\nうずうずぞわぞわ、恥ずかしすぎてムズムズするけんっ！
- TW: 哇啊！這可不行啊！\n我開始心神不寧、坐立不安了，太羞恥了，心跳個不停！
- Cũ: Hya! Thế này, không được đâu!\nCứ bồn chồn râm ran, xấu hổ đến mức ngứa ngáy hết cả người rồi!
- Sửa: Hauu! Thế này, không được đâu!\nCứ bồn chồn râm ran, xấu hổ đến mức ngứa ngáy hết cả người rồi!

### Đại từ (5 dòng)

**1870 [日々姫]** — Hibiki tự xưng "chị" với Kisaki — sai: Hibiki là hậu bối khóa dưới của Kisaki, tự xưng phải là "em". Người nghe xác nhận từ thứ tự trong file: dòng trước (1869) là Kisaki đang nhặt sổ phác thảo rơi, Hibiki nói "để phụ cho" với chính Kisaki.

- JP: 「ごめんっ！　手伝う」
- TW: 「對不起！我來幫忙吧」
- Cũ: 「Xin lỗi nha! Để chị phụ cho.」
- Sửa: 「Xin lỗi nha! Để em phụ cho.」

**1883 [日々姫]** — Hibiki tự xưng "tớ" với Kisaki — sai: với senpai phải là "em". (Trong toàn dự án, Hibiki chỉ dùng "tớ" với bạn ngang hàng như Paulette; với Kisaki/Soutetsu thì không.)

- JP: 「すごかとよねー。ばってん、ひんぴょー会のことと、\nわたしのテストの点とは関係なかよねぇ」
- TW: 「很厲害對吧。不過，評議會和我考試的分數沒什麼關係啊」
- Cũ: 「Tuyệt thật đó nha. Nhưng mà, chuyện buổi bình chọn\nthì có liên quan gì đến điểm kiểm tra của tớ đâu chứ.」
- Sửa: 「Tuyệt thật đó nha. Nhưng mà, chuyện buổi bình chọn\nthì có liên quan gì đến điểm kiểm tra của em đâu chứ.」

**1981 [日々姫]** — Hibiki tự xưng "tớ" (2 chỗ) — sai: người nghe là Soutetsu (cảnh buổi sáng, hai dòng kề 1972 và 1982 đều là Soutetsu), tự xưng phải là "em".

- JP: 「だよねぇ。なのに、なんでそぎゃんと言うてくれっと、\nくまくまだけなんか、私、さっぱりわからんばい」
- TW: 「是吧。可我真不明白，為什麼只有熊熊一個人肯這麼說」
- Cũ: 「Đúng không. Vậy mà, tại sao chỉ có mỗi Kuma Kuma\nlà nói với tớ như vậy, tớ chả hiểu gì sất.」
- Sửa: 「Đúng không. Vậy mà, tại sao chỉ có mỗi Kuma Kuma\nlà nói với em như vậy, em chả hiểu gì sất.」

**1797 [双鉄]** — Soutetsu tự sửa 真闇さ→真闇姉, nhưng VN viết trùng thành "chị Mayami——chị Mayami" — mất hẳn ý tự sửa (từ cách gọi trang trọng -san sang cách gọi gia đình -nee). Theo tiền lệ Paulette file 07 (sửa "anh Soutetsu……à không, anh Soutetsu" thành "Cậu Soutetsu……à không, anh Soutetsu" theo đúng mẫu くん→"cậu"/さん→"anh"): giữ "Mayami-san" cho dạng -san để phép tự sửa hiện ra. Câu trích dẫn sau đó ("đừng thêm chữ "san" vào nữa") càng khớp với cách sửa này.

- JP: 「ああ、それは真闇さ――真闇姉に指示された。\n『これからは家族なのだから、さん付けはよせ』と」
- TW: 「嗯。這是真闇小——真闇姐指示的。她說“從今以後我們就是家人了，別再加‘小姐’了”」
- Cũ: 「À, đó là do chị Mayami——chị Mayami đã chỉ thị cho anh.\n『Từ giờ chúng ta là gia đình rồi, nên đừng thêm chữ "san" vào nữa』.」
- Sửa: 「À, đó là do Mayami-san——à không, chị Mayami đã chỉ thị cho anh.\n『Từ giờ chúng ta là gia đình rồi, nên đừng thêm chữ "san" vào nữa』.」

**1849 [双鉄]** — cùng mẫu với 1797: Soutetsu tự sửa 真闇さん→真闇姉, VN viết trùng thành "chị Mayami——à không, chị Mayami". Sửa theo cùng mẫu.

- JP: 「それが指示なら努力したいが、今はまだ見習えるほど、\n真闇さん――いや、真闇姉のことを知らんので少し困る」
- TW: 「如果這是指示的話我倒是願意努力，不過我現在還沒對真闇小姐——不，對真闇姐了解到能學習的程度，有點傷腦筋」
- Cũ: 「Nếu đó là chỉ thị thì anh cũng muốn cố gắng, nhưng hiện tại,\nanh vẫn chưa hiểu rõ về chị Mayami——à không, chị Mayami đủ để học theo, nên hơi khó xử một chút.」
- Sửa: 「Nếu đó là chỉ thị thì anh cũng muốn cố gắng, nhưng hiện tại,\nanh vẫn chưa hiểu rõ về Mayami-san——à không, chị Mayami đủ để học theo, nên hơi khó xử một chút.」

### Nghĩa (3 dòng)

**2128 [日々姫]** — ね？ (gọi để gây chú ý: "này, nghe này") bị dịch thành "Dạ?" (từ đáp lời, không phải từ gọi). TW dịch đúng ý này: 「聽我說」 (nghe tôi nói).

- JP: 「あの！　ね？　そうてつさん」
- TW: 「那個！聽我說！雙鐵哥哥」
- Cũ: 「Nè! Dạ? Anh Soutetsu.」
- Sửa: 「Nè! Nghe em nói này, anh Soutetsu.」

**2596 [monologue]** — JP/TW đều là 人 số ít ("người đã nói"), VN viết số nhiều "những người". Độc thoại này đang liệt kê từng người một (xem 2711 "Người thứ ba").

- JP: “絵をもっと人に見せろ”って、\n私に、言ってくれた人。
- TW: 會對我說“要把畫帶給更多的人看”的人。
- Cũ: Là những người đã nói với mình rằng,\n"Hãy cho mọi người xem tranh của em nhiều hơn nữa đi".
- Sửa: Là người đã nói với mình rằng,\n"Hãy cho mọi người xem tranh của em nhiều hơn nữa đi".

**2718 [monologue]** — Hibiki tự sửa trong độc thoại にぃに→兄さん (từ cách gọi trẻ con/dialect sang cách gọi chuẩn), nhưng VN viết thành "anh hai——anh Soutetsu" — đổi thành tên người, mất ý sửa cách gọi. Sửa theo đúng bản chất phép sửa: "anh hai" (dạng thân mật) → "anh trai" (dạng chuẩn).

- JP: 言ってまっすぐ、にぃに――兄さんが、\n私の瞳をじっと見つめる。
- TW: 阿哥——哥哥邊這麼說著，邊堅定地看著我的眼睛。
- Cũ: Vừa nói, anh hai――anh Soutetsu\nnhìn thẳng vào mắt tôi.
- Sửa: Vừa nói, anh hai——anh trai\nnhìn thẳng vào mắt tôi.

## Lượt soát 2

Đọc lại toàn bộ 20 fix đối chiếu từng JP lần thứ hai: **20 tổng / 20 tái kiểm chứng / 0 loại bỏ / 0 sửa lại.** Đặc biệt kiểm tra lại: 4 mục sweep áp nguyên khớp JP từng dấu; 2 gasp sweep bỏ sót (1333, 1728) khớp công thức độ dài nguyên âm; 5 dòng fa/fu khớp quy tắc đã chốt và tiền lệ (ふぇ→"phuê", ふあっ→"phù", ふえっ→"phuê", ふぁっ→"Phà", はうぅ→"Hauu"); 1785 khớp đủ 7 âm a; 5 dòng đại từ đã xác nhận người nghe từ các dòng kề trong file; 1797/1849 khớp tiền lệ Paulette file 07; 2128 khớp TW; 2596 khớp JP/TW số ít; 2718 giữ đúng bản chất phép tự sửa cách gọi.

## Ghi chú / chờ Hieu (không tính sai, không tự quyết)

- **ぴゃ/あわわ — giữ nguyên, chờ quyết chung.** 1725 ぴゃうっ→"Hya!!?", 1763 ぴゃわわわわわっ→"Oa oa oa oa oa!?" (đủ 5 âm "oa" theo 5 âm わ), 2438 あわわ→"Awa wa" (để nguyên dạng Latin). Chưa có quy tắc đã chốt cho họ âm ぴゃ/あわわ; theo luật ngẫu hứng 22:05 và tiền lệ h6 giữ nguyên SFX Latin ("Hyau!"/"Kua!") nên giữ nguyên. Nếu Hieu muốn thống nhất một thể (vd. ぴゃ→"Pya") thì làm trong đợt thống nhất sau.
- **評議会/ひんぴょー会 → "buổi bình chọn" — giữ nguyên, cần Hieu xác nhận.** Chỉ xuất hiện ở 2 dòng trong file này (1883, 2114), không có ở đâu khác trong dự án. TW nói 評議會 (hội đồng); VN hiện dịch theo nghĩa sự kiện (buổi bình chọn/chấm giải rượu). Nếu muốn dùng "Hội đồng bình xét" thì đổi trong đợt thống nhất.
- **帝鉄 gloss "Đường sắt Hoàng gia" (1629) — KHÔNG sửa ở đây.** Đây là dạng cũ của thuật ngữ đã chốt (帝鉄="Teitetsu"), thuộc diện unification pass; ghi chú để đợt thống nhất xử lý chung.
- **1902 "cậu" trong lời trích dẫn — giữ nguyên.** JP trong dấu trích không có đại từ nhân xưng; TW nói "他們" (họ) — người trích dẫn không rõ danh tính nên "cậu" là phỏng đoán hợp lý của người dịch cũ, không đủ căn cứ sửa.
- **1629 câu JP cụt + VN "đã bị..." — giữ nguyên.** JP cụt giữa chừng (không có động từ); TW hoàn thiện câu ("巡線員就得過"); VN giữ dấu "..." để giữ dạng câu cụt, không bịa trọn vẹn. Không tính sai.
- **2554 "Răng lại rứa" — giữ nguyên.** Dịch phương ngữ Hakata (どぎゃんして) bằng phương ngữ Việt (miền Trung) — lựa chọn dịch có chủ ý, hợp lý.
- **1871/1956/2033 thẻ [x,1] (furigana) bị lược trong VN — không tính sai.** Đây là thẻ hiển thị phía JP (くらびと/ばんくま/あに); bản Việt không cần furigana.
- **2424 "ca cao pha sữa nóng" — giữ nguyên.** JP không nói "nóng" nhưng TW nói 熱可可 (ca cao nóng); không mâu thuẫn JP nên theo TW.
- File sạch về thuật ngữ đã chốt khác: không có "Ohimitera", "Yui", "Migita System", "Obata", "Suntetsu", "Master Controller"; "Migita" đã đúng dạng ở 1646; Soutetsu xưng "anh" với Hibiki đúng toàn bộ; không có lỗi thẻ `%l` (số lượng `%l` JP==VN ở mọi dòng).

## Khối TOML (đã kiểm chứng parse)



```toml
[script]
1333 = "「……A ư.」"
1720 = "「Phuê?」"
1727 = "「Phù!?」"
1728 = "「E ư.」"
1742 = "「Phuê!? Gì vậy chứ.」"
1759 = "「Phà.」"
1785 = "「U kyaaaaaaa!」"
1797 = "「À, đó là do Mayami-san——à không, chị Mayami đã chỉ thị cho anh.\\n『Từ giờ chúng ta là gia đình rồi, nên đừng thêm chữ \"san\" vào nữa』.」"
1849 = "「Nếu đó là chỉ thị thì anh cũng muốn cố gắng, nhưng hiện tại,\\nanh vẫn chưa hiểu rõ về Mayami-san——à không, chị Mayami đủ để học theo, nên hơi khó xử một chút.」"
1870 = "「Xin lỗi nha! Để em phụ cho.」"
1883 = "「Tuyệt thật đó nha. Nhưng mà, chuyện buổi bình chọn\\nthì có liên quan gì đến điểm kiểm tra của em đâu chứ.」"
1949 = "「Chị ăn đây——Amu——Ư!!!」"
1981 = "「Đúng không. Vậy mà, tại sao chỉ có mỗi Kuma Kuma\\nlà nói với em như vậy, em chả hiểu gì sất.」"
2128 = "「Nè! Nghe em nói này, anh Soutetsu.」"
2166 = "「Ư」\\n「Ư!」"
2168 = "「Ư!!」"
2169 = "「Ư!!?」"
2430 = "Hauu! Thế này, không được đâu!\\nCứ bồn chồn râm ran, xấu hổ đến mức ngứa ngáy hết cả người rồi!"
2596 = "Là người đã nói với mình rằng,\\n\"Hãy cho mọi người xem tranh của em nhiều hơn nữa đi\"."
2718 = "Vừa nói, anh hai――anh trai\\nnhìn thẳng vào mắt tôi."
```

## Kết bài

File 日々姫07_たったひとりの宣戦布告 đã đọc xong toàn bộ 400 dòng: **20 dòng sai (5,0%)**, gồm 4 lỗi sweep っ, 8 lỗi SFX, 5 lỗi đại từ và 3 lỗi nghĩa. Lượt soát 2: 20/20/0/0. Không có lệch dòng, chuỗi xoay, tràn file khác, dòng chưa dịch hay trùng key; không có lỗi thuật ngữ đã chốt; Soutetsu xưng "anh" đúng toàn bộ. Còn chờ Hieu: quy tắc chung cho ぴゃ/あわわ, thuật ngữ 評議会 ("buổi bình chọn" hay "Hội đồng bình xét"), và gloss 帝鉄 "Đường sắt Hoàng gia" trong đợt thống nhất.
