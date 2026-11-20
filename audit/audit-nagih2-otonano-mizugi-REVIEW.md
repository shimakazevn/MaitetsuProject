# Audit — 凪h2_おとなの水着.txt.toml (Nagi h2, "đồ bơi người lớn")

- File: `凪h2_おとなの水着.txt.toml` — route 07_Nagi_Fukami, **673 dòng script**.
- Nội dung: Nagi và Soutetsu mua đồ bơi qua mạng (máy tính, trang thương mại — chọn đồ bơi 'người lớn' chững chạc thay cho đồ bơi quy định của trường, bàn về thương hiệu Channel/Vucci, đồ bơi cũ), rồi Nagi thử đồ bơi trước mặt Soutetsu; cảnh làm tình dài (Nagi mặc đồ bơi, oral, Soutetsu xuất tinh), xen kẽ trò chuyện về bà nội, kiếm thuật, đốt ngải cứu, và kỷ niệm với Fukami; cuối file hai người làm huy hiệu biểu trưng đầu tàu (御一夜鉄道).
- **Kết quả: 89/673 dòng sai (13,2%)** — lỗi hệ thống lớn nhất là đại từ: Soutetsu xưng 'tôi' với Nagi trong 50 dòng (61 lần), còn lại là SFX/gasp/fa-fu và đếm nguyên âm, cộng 3 lỗi nghĩa.
- Phân loại (89): đại từ 50, gasp 7, fa/fu 5, SFX 15, đếm nguyên âm 9, nghĩa 3.
- Theo nhân vật: 双鉄 56 (50 đại từ + gasp 3: 2487, 2536, 2544 + đếm nguyên âm 3: 2514, 2603, 2776), 凪 25 (SFX 15 + fa/fu 5 + đếm nguyên âm 4 + nghĩa 1: 2749), monologue 8 (gasp 4: 3354, 3433, 3610, 3719 + nghĩa 2: 3346, 3717 + đếm nguyên âm 2: 4016, 4023).
- Lệch vị trí **0**, chuỗi xoay **0**, nhiễm chéo **0**, mồ côi **0**, chưa dịch **0**, trùng khóa **0**.

## 1. Xác minh tệp và nguồn

- TOML md5 `a581ef85d1d7aed81fc5303b23f050ea`, BOM + CRLF, `[selections]` rỗng ({}). **Không có bản sao** file này trong 227 tệp TOML-2 (1 copy duy nhất).
- CSV3: **1 set duy nhất** (673 dòng, 0 key trùng, 0 VN rỗng, 0 VN == TW, 0 VN == JP). VN khớp TOML tuyệt đối 673/673 (sau khi gộp `\n` thành khoảng trắng theo hiện tượng đã biết của TOML-2), **0 khác biệt thực chất** — CSV3 là bản chuẩn cho fix list.
- Thẻ `%l`: JP **0** thẻ, VN **0** thẻ, TOML **0** thẻ — không có thẻ sai định dạng nào trong file này.
- Đại từ: Soutetsu tự xưng 'tôi' với Nagi trong **50/164 dòng thoại** của anh (61 lần 'tôi') — lỗi hệ thống, ngược với tiền lệ 凪ふかみ05 ('Soutetsu anh với Nagi/Fukami đúng toàn file'). Soutetsu tự xưng 'anh' đúng: **0 dòng** — toàn bộ đều sai. Nagi gọi Soutetsu 'anh hai' nhất quán; Fukami chỉ được nhắc tên ('bé Fukami' 2912/2952/2964 — đúng quy tắc cùng tuổi, không có 'chị Fukami' nào). Monologue 'tôi' (293 dòng) giữ nguyên — đúng quy tắc độc thoại. 'Chúng tôi'/'bọn tôi' (dạng nhóm, giữ nguyên): **0 dòng** trong file.
- Thuật ngữ đã chốt: 帝都 → 'Đế đô' (2716, 2684, 3639) đúng; 市電 → 'tàu điện thành phố' đúng; 帝鉄 → 'Teitetsu' đúng; 湯医 → 'Yunoi' đúng; まいてつ → 'chủ tàu' đúng (trừ 1 dạng cũ ở 1766, xem §5); 機関士 → 'thợ lái đầu máy' đúng; 'Railord'/'Olivy' đúng chính tả. ちゅ-family thống nhất 'Chụt' toàn file (2548, 2425, 2560, 2561, 2562…).
- Kiểm tra nhiễm chéo: không có cặp VN trùng nào đáng ngờ với JP khác nhau; các SFX lặp (はあっ → 'Hà!' nhiều lần, ちゅっ → 'Chụt') đều là cùng một âm JP lặp lại — lặp hợp lệ, không phải nhiễm chéo.

## 2. Sweep っ (gasp) — kiểm tra trực tiếp

- File này CÓ **8 mục** trong `sweep-raw-gasp-wrong.json`: 7 mục `lost-gasp-trailing` (2487, 2536, 2544, 3354, 3433, 3610, 3719) + 1 mục 'already-rendered' (2489, くっ――ふっ――んひゅっ――んんん～っ！). **Áp nguyên cả 7 mục lost-gasp, đã kiểm chứng từng giá trị với JP.** Mục 2489 tuy sweep ghi 'already-rendered' nhưng kiểm tra lại thấy vẫn sai 2 âm (んひゅっ → 'Ưm' thay vì 'Ưm hứ'; んんん～っ → 'Ưm~' thay vì 'Ưmmm~') nên sửa luôn — xem 2489 ở §3.
- Quét bổ sung **toàn bộ các dòng JP kết bằng っ** (44 dòng): không bắt thêm gasp nào bị sweep bỏ sót — các っ còn lại đều là っ nhấn mạnh gắn với từ (だっ/ぞっ/にっ/ちんっ/とっ/ねっ/さまっ), っ theo sau bởi ――/、/……, hoặc onomatopoeia đã dịch thành từ Việt (ぺろっ → 'Liếm', はむっ → 'Ngoạm', カチっ → 'click') — đều giữ nguyên theo tiền lệ.
- **っ nhấn mạnh gắn với từ — KHÔNG sửa** (tiền lệ h9 §3.4, fukamih2 §4, 1474/2428/2588): 2370 凪っ！→ 'Nagi!', 2752 捕まえたとっ！→ 'Bắt được rồi á!', 2429 ありゃっ！？→ 'Ủa!?', 2576 だっ！→ 'đấy!', 2590 ばいっ→ 'á!!', 2766 ねっ！→ 'á!', 2588 うむっ！？→ 'Hửm!?', 3010 くしゅんっ→ 'Hắt——xì!!'.
- **Đếm consonant kéo dài (±1) — KHÔNG sửa** (chưa có công thức chốt, chỉ là phong cách): 2513, 2533, 2546, 2558, 2561, 2562, 2547, 4065, 4063, 4064, 4040 (chụt/chụt/… kéo dài t).

## 3. Chi tiết từng dòng sai (89 dòng)

### Đại từ — Soutetsu "tôi" → "anh" (50 dòng)

#### 1778 — 双鉄 — pronoun
- **JP:** 「……水着姿の凪を、僕は恐らく舐めたくなる」
- **TW:** 「……但是看見你穿泳裝，我恐怕會想舔你」
- **VN cũ:** 「……Có lẽ tôi sẽ muốn liếm láp Nagi trong bộ đồ bơi đấy」
- **Mới:** 「……Có lẽ anh sẽ muốn liếm láp Nagi trong bộ đồ bơi đấy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 1793 — 双鉄 — pronoun
- **JP:** 「……学園指定の水着。あれは、\n大人っぽいとは正反対にあるものかと思う」
- **TW:** 「……學校泳裝，是與成熟的泳裝恰好相反的泳裝」
- **VN cũ:** 「……Đồ bơi quy định của trường. Bộ đó,\ntôi nghĩ là trái ngược hoàn toàn với sự chững chạc đấy」
- **Mới:** 「……Đồ bơi quy định của trường. Bộ đó,\nanh nghĩ là trái ngược hoàn toàn với sự chững chạc đấy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 1797 — 双鉄 — pronoun
- **JP:** 「……むしろ、濃い色自体の反対を考えるべきでは？\n原色などはどの色であれ、年若い印象が強い気がする」
- **TW:** 「……應該想想濃厚顏色本身的反面吧？三原色不管是哪種看起來都會很年輕」
- **VN cũ:** 「……Đúng hơn là, nên nghĩ ngược lại với bản thân màu đậm thì sao?\nNhững màu cơ bản, dù là màu gì đi nữa, tôi có cảm giác đều mang lại ấn tượng trẻ trung」
- **Mới:** 「……Đúng hơn là, nên nghĩ ngược lại với bản thân màu đậm thì sao?\nNhững màu cơ bản, dù là màu gì đi nữa, anh có cảm giác đều mang lại ấn tượng trẻ trung」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2264 — 双鉄 — pronoun
- **JP:** 「不戦勝ではない。正々堂々の勝負の結果だ。\n凪の魅力――おんなの魅力に、僕は、負けた」
- **TW:** 「不是不戰而勝，這是正式比賽的結果。我輸給了你的魅力――輸給了你作為女人的魅力」
- **VN cũ:** 「Không phải thắng mà không cần đánh. Đây là kết quả của một trận đấu quang minh chính đại.\nTrước sức hấp dẫn của Nagi——sức hấp dẫn của một người phụ nữ, tôi đã thua rồi」
- **Mới:** 「Không phải thắng mà không cần đánh. Đây là kết quả của một trận đấu quang minh chính đại.\nTrước sức hấp dẫn của Nagi——sức hấp dẫn của một người phụ nữ, anh đã thua rồi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2276 — 双鉄 — pronoun
- **JP:** 「しかし……となると、より難しいな。\n古着の水着は、僕としてはできれば避けたいし」
- **TW:** 「不過……這樣就更難了。可以的話，我還是儘量不想買二手」
- **VN cũ:** 「Nhưng mà……nếu vậy thì, lại càng khó khăn hơn nhỉ.\nTôi thì nếu được muốn tránh mua đồ bơi cũ」
- **Mới:** 「Nhưng mà……nếu vậy thì, lại càng khó khăn hơn nhỉ.\nAnh thì nếu được muốn tránh mua đồ bơi cũ」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2277 — 双鉄 — pronoun
- **JP:** 「ところが、これがフリでもないのだ」
- **TW:** 「不過，我並不是假裝的」
- **VN cũ:** 「Nhưng mà, tôi cũng không phải đang tỏ vẻ đâu」
- **Mới:** 「Nhưng mà, anh cũng không phải đang tỏ vẻ đâu」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2282 — 双鉄 — pronoun
- **JP:** 「いや、余裕など、まったくないぞ」
- **TW:** 「不，我可一點都不從容」
- **VN cũ:** 「Không, tôi chẳng ung dung chút nào đâu」
- **Mới:** 「Không, anh chẳng ung dung chút nào đâu」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2306 — 双鉄 — pronoun
- **JP:** 「なんでもなにも、僕は、凪の敗者だからな」
- **TW:** 「什麼為什麼，我可是輸給你了啊」
- **VN cũ:** 「Sao trăng gì, tôi là kẻ bại trận trước Nagi mà」
- **Mới:** 「Sao trăng gì, anh là kẻ bại trận trước Nagi mà」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2310 — 双鉄 — pronoun
- **JP:** 「今日は、凪の命令なしには、\nまったく何もできんのだ」
- **TW:** 「今天沒有你的命令，我什麼都不能做」
- **VN cũ:** 「Hôm nay, nếu không có lệnh của Nagi,\ntôi hoàn toàn không thể làm gì cả」
- **Mới:** 「Hôm nay, nếu không có lệnh của Nagi,\nanh hoàn toàn không thể làm gì cả」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2319 — 双鉄 — pronoun
- **JP:** 「しかし……その恰好で泳ぐのか？\n正直、僕は――今の凪を、僕以外には見せたくない」
- **TW:** 「但是……你要穿成這樣游泳嗎？說實話，我……不想讓除了我之外的人看到現在的你」
- **VN cũ:** 「Nhưng mà……em định mặc thế này đi bơi sao?\nNói thật thì, tôi——không muốn ai khác ngoài tôi nhìn thấy Nagi lúc này đâu」
- **Mới:** 「Nhưng mà……em định mặc thế này đi bơi sao?\nNói thật thì, anh——không muốn ai khác ngoài anh nhìn thấy Nagi lúc này đâu」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2394 — 双鉄 — pronoun
- **JP:** 「いやしかし、僕がプレゼントするのだぞ？」
- **TW:** 「可這是我要送你的啊」
- **VN cũ:** 「Không, nhưng mà, là tôi tặng quà cho em cơ mà?」
- **Mới:** 「Không, nhưng mà, là anh tặng quà cho em cơ mà?」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2467 — 双鉄 — pronoun
- **JP:** 「ああ！　理解した。\n確かに、新鮮味が強い方がうれしいな」
- **TW:** 「哦！我懂了。確實，有驚喜更讓人開心」
- **VN cũ:** 「A! Tôi hiểu rồi.\nĐúng là, cảm giác mới mẻ mãnh liệt thì sẽ vui hơn nhỉ」
- **Mới:** 「A! Anh hiểu rồi.\nĐúng là, cảm giác mới mẻ mãnh liệt thì sẽ vui hơn nhỉ」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2474 — 双鉄 — pronoun
- **JP:** 「一度、じっくりお話してみたくなったな。\n凪の、お祖母様と」
- **TW:** 「哪天有機會，真想和你的奶奶好好聊聊」
- **VN cũ:** 「Tôi muốn được nói chuyện đàng hoàng một lần ghê.\nVới bà nội của Nagi ấy」
- **Mới:** 「Anh muốn được nói chuyện đàng hoàng một lần ghê.\nVới bà nội của Nagi ấy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2504 — 双鉄 — pronoun
- **JP:** 「む、そうか。ならばそこは思い出すまい」
- **TW:** 「唔，是嗎，那我就不回想那裡了」
- **VN cũ:** 「Hừm, vậy sao. Nếu vậy thì tôi sẽ không nhớ lại đoạn đó nữa」
- **Mới:** 「Hừm, vậy sao. Nếu vậy thì anh sẽ không nhớ lại đoạn đó nữa」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2574 — 双鉄 — pronoun
- **JP:** 「うむ。これだ。\n早速着替えて見せてくれ」
- **TW:** 「嗯，就是這個。快點換上給我看看」
- **VN cũ:** 「Ừm. Nó đây.\nMau thay rồi cho tôi xem đi」
- **Mới:** 「Ừm. Nó đây.\nMau thay rồi cho anh xem đi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2576 — 双鉄 — pronoun
- **JP:** 「ああ、好きだとも。大好き――だっ！」
- **TW:** 「嗯，愛你，愛死你了！」
- **VN cũ:** 「Có, tôi thích em. Rất thích——đấy!」
- **Mới:** 「Có, anh thích em. Rất thích——đấy!」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2578 — 双鉄 — pronoun
- **JP:** 「うむ。僕もそうして欲しい」
- **TW:** 「嗯，我也希望你這麼做」
- **VN cũ:** 「Ừm. Tôi cũng muốn em làm vậy」
- **Mới:** 「Ừm. Anh cũng muốn em làm vậy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2579 — 双鉄 — pronoun
- **JP:** 「うむ。実に良い教えだと、僕も思う」
- **TW:** 「嗯，我覺得他們教得很好」
- **VN cũ:** 「Ừm. Quả thực là một lời dạy rất hay, tôi cũng nghĩ vậy」
- **Mới:** 「Ừm. Quả thực là một lời dạy rất hay, anh cũng nghĩ vậy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2610 — 双鉄 — pronoun
- **JP:** 「おおお！　ならば早く見せてくれ」
- **TW:** 「噢！那就快點給我看」
- **VN cũ:** 「Ồ! Vậy thì mau cho tôi xem đi」
- **Mới:** 「Ồ! Vậy thì mau cho anh xem đi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2710 — 双鉄 — pronoun
- **JP:** 「凪……に、触れたい――触れても、いいか」
- **TW:** 「我……想摸你……可以摸嗎」
- **VN cũ:** 「Nagi……tôi muốn chạm vào em——Chạm vào em, được không」
- **Mới:** 「Nagi……anh muốn chạm vào em——Chạm vào em, được không」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2712 — 双鉄 — pronoun
- **JP:** 「僕も詳しくは知らんが――\n代表的なところでは、チャネルとか、ヴッチとか」
- **TW:** 「我也不是很熟悉……代表性的有香奈爾、古弛之類的」
- **VN cũ:** 「Tôi cũng không rành lắm nhưng——\nTiêu biểu thì có Channel, hay là Vucci chẳng hạn」
- **Mới:** 「Anh cũng không rành lắm nhưng——\nTiêu biểu thì có Channel, hay là Vucci chẳng hạn」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2714 — 双鉄 — pronoun
- **JP:** 「そうしたいがな、今は我慢だ。\n凪の水着を、一番鮮やかに焼き付けるため」
- **TW:** 「我也想，但現在我要忍耐。我要將你最漂亮的泳裝模樣刻在眼底」
- **VN cũ:** 「Tôi cũng muốn thế lắm, nhưng bây giờ phải nhịn thôi.\nĐể khắc sâu hình ảnh Nagi mặc đồ bơi một cách sống động nhất」
- **Mới:** 「Anh cũng muốn thế lắm, nhưng bây giờ phải nhịn thôi.\nĐể khắc sâu hình ảnh Nagi mặc đồ bơi một cách sống động nhất」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2716 — 双鉄 — pronoun
- **JP:** 「僕もだ。ううむ……\nこういうときだけは、いささか帝都が恋しくなるな」
- **TW:** 「我也是。唔……唯有這種時候，我會懷念帝都」
- **VN cũ:** 「Tôi cũng vậy. Ừm……\nChỉ những lúc thế này, tôi mới thấy nhớ Đế đô một chút」
- **Mới:** 「Anh cũng vậy. Ừm……\nChỉ những lúc thế này, anh mới thấy nhớ Đế đô một chút」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2717 — 双鉄 — pronoun
- **JP:** 「僕もだ。凪が、大好きだ」
- **TW:** 「我也是，我愛你」
- **VN cũ:** 「Tôi cũng vậy. Rất thích, Nagi」
- **Mới:** 「Anh cũng vậy. Rất thích, Nagi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2720 — 双鉄 — pronoun
- **JP:** 「思いつかんな。\n僕は、学園指定の水着にさほど興味がないらしい」
- **TW:** 「我什麼都想不到。看來我對學校泳裝並沒有什麼興趣」
- **VN cũ:** 「Không nghĩ ra được gì nữa.\nCó vẻ tôi không mấy hứng thú với đồ bơi của trường」
- **Mới:** 「Không nghĩ ra được gì nữa.\nCó vẻ anh không mấy hứng thú với đồ bơi của trường」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2728 — 双鉄 — pronoun
- **JP:** 「大いにほめている。\n普段の理屈をコネない凪も、僕は大好きだからな」
- **TW:** 「我就是在誇。平時不拘小節的你我也非常喜歡」
- **VN cũ:** 「Đang khen ngợi hết lời đấy chứ.\nVì tôi cũng rất thích một Nagi không hay viện cớ như thường ngày mà」
- **Mới:** 「Đang khen ngợi hết lời đấy chứ.\nVì anh cũng rất thích một Nagi không hay viện cớ như thường ngày mà」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2730 — 双鉄 — pronoun
- **JP:** 「凪が一番気に入って、分不相応とも思わぬものを、\n値段のことは気にせずに、好きに選んでもらいたい」
- **TW:** 「我希望你選出你最喜歡的，不覺得不配的，不要在意價格」
- **VN cũ:** 「Tôi muốn em cứ thoải mái chọn thứ mình thích nhất, thứ mà em không cho là không biết lượng sức,\nmà không cần phải bận tâm đến giá cả」
- **Mới:** 「Anh muốn em cứ thoải mái chọn thứ mình thích nhất, thứ mà em không cho là không biết lượng sức,\nmà không cần phải bận tâm đến giá cả」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2733 — 双鉄 — pronoun
- **JP:** 「喜んで――なのだが。その前に、\n水着をなんとか解決したい」
- **TW:** 「我很樂意……但是，在這之前，我們得先買到泳裝」
- **VN cũ:** 「Rất sẵn lòng——nhưng mà. Trước đó,\ntôi muốn giải quyết xong chuyện đồ bơi đã」
- **Mới:** 「Rất sẵn lòng——nhưng mà. Trước đó,\nanh muốn giải quyết xong chuyện đồ bơi đã」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2735 — 双鉄 — pronoun
- **JP:** 「いつもと違う、凪の水着を見てみたい。\nそれ自体、僕の望みであるのだからな」
- **TW:** 「我想看看你和平時不一樣的泳裝。這個本事其實也是我的期待」
- **VN cũ:** 「Tôi muốn được thấy một Nagi trong bộ đồ bơi khác ngày thường.\nBản thân điều đó, đã là mong muốn của tôi rồi」
- **Mới:** 「Anh muốn được thấy một Nagi trong bộ đồ bơi khác ngày thường.\nBản thân điều đó, đã là mong muốn của anh rồi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2736 — 双鉄 — pronoun
- **JP:** 「特に考えたことはない」
- **TW:** 「我沒怎麼想過」
- **VN cũ:** 「Tôi chưa từng nghĩ đến chuyện đó」
- **Mới:** 「Anh chưa từng nghĩ đến chuyện đó」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2738 — 双鉄 — pronoun
- **JP:** 「僕とて凪とそう変わらんぞ。\n仕事で覚えた範囲のこと以外は、まるでこなせん」
- **TW:** 「我跟你也差不多。除了工作需要記住的之外，什麼都不會」
- **VN cũ:** 「Tôi cũng chẳng khác Nagi là mấy đâu.\nNgoài những gì học được trong công việc ra, thì tôi hoàn toàn mù tịt」
- **Mới:** 「Anh cũng chẳng khác Nagi là mấy đâu.\nNgoài những gì học được trong công việc ra, thì anh hoàn toàn mù tịt」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2743 — 双鉄 — pronoun
- **JP:** 「ゆえ、今必死に思い出そうとしてみたのだが、\n思い出せるのはそこから先、凪とふかみの」
- **TW:** 「所以現在我拚命在思索，但每次想起來的都是你和深美的模樣」
- **VN cũ:** 「Do đó, nãy giờ tôi đã cố gắng hết sức để nhớ lại, nhưng\nnhững gì tôi có thể nhớ được từ đó trở đi, là của Nagi và Fukami」
- **Mới:** 「Do đó, nãy giờ anh đã cố gắng hết sức để nhớ lại, nhưng\nnhững gì anh có thể nhớ được từ đó trở đi, là của Nagi và Fukami」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2745 — 双鉄 — pronoun
- **JP:** 「ゆえに、だ。学園指定の水着の逆を考えれば、\n大人っぽさを追求できるのではないかと思う」
- **TW:** 「所以，只要以學校泳裝為反例，就可以明白什麼叫成熟了」
- **VN cũ:** 「Do đó. Nếu nghĩ ngược lại với đồ bơi của trường,\ntôi nghĩ chúng ta có thể tìm ra được sự chững chạc」
- **Mới:** 「Do đó. Nếu nghĩ ngược lại với đồ bơi của trường,\nanh nghĩ chúng ta có thể tìm ra được sự chững chạc」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2754 — 双鉄 — pronoun
- **JP:** 「すまん。いいアイディアを思いついた――\nというか、自分の間抜けさにショックを受けていた」
- **TW:** 「抱歉，我想到一個好主意……其實主要是因為我連這個都忘了，感覺很震驚」
- **VN cũ:** 「Xin lỗi nhé. Tôi vừa nảy ra một ý tưởng hay——\nHay nói đúng hơn là, tôi đang bị sốc trước sự ngốc nghếch của bản thân」
- **Mới:** 「Xin lỗi nhé. Anh vừa nảy ra một ý tưởng hay——\nHay nói đúng hơn là, anh đang bị sốc trước sự ngốc nghếch của bản thân」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2778 — 双鉄 — pronoun
- **JP:** 「そうだな。品物選びまでなら十分だ。\n決済は僕がするので、決めるまでは凪が操作してくれ」
- **TW:** 「是啊，要選商品已經夠了。付款交給我，在這之前你來操作吧」
- **VN cũ:** 「Đúng vậy. Chỉ cần chọn đồ thì thế là đủ rồi.\nViệc thanh toán tôi sẽ lo, nên cho đến lúc quyết định xong thì Nagi cứ thao tác đi」
- **Mới:** 「Đúng vậy. Chỉ cần chọn đồ thì thế là đủ rồi.\nViệc thanh toán anh sẽ lo, nên cho đến lúc quyết định xong thì Nagi cứ thao tác đi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2783 — 双鉄 — pronoun
- **JP:** 「僕の負けだ。完全に捕まえられた。\n凪と、一刻も早く触れ合いたい」
- **TW:** 「是我輸了。我已經徹底被你抓住了。我想趕緊和你相互觸碰」
- **VN cũ:** 「Tôi thua rồi. Hoàn toàn bị em bắt được rồi.\nTôi muốn được chạm vào Nagi, càng sớm càng tốt」
- **Mới:** 「Anh thua rồi. Hoàn toàn bị em bắt được rồi.\nAnh muốn được chạm vào Nagi, càng sớm càng tốt」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2792 — 双鉄 — pronoun
- **JP:** 「凪はときおり、驚かされるほど賢いな」
- **TW:** 「有時候你聰明得很讓人驚訝啊」
- **VN cũ:** 「Nagi đôi khi, thông minh đến mức khiến tôi phải kinh ngạc đấy」
- **Mới:** 「Nagi đôi khi, thông minh đến mức khiến anh phải kinh ngạc đấy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2794 — 双鉄 — pronoun
- **JP:** 「そうしたスポーツブランドの店もあるだろうし、\nもっとこう、いわゆるファッションブランドなども」
- **TW:** 「有這些運動用品品牌店，也有一些流行品牌店」
- **VN cũ:** 「Chắc cũng có những cửa hàng đồ thể thao như vậy,\nnhưng ý tôi là những cửa hàng gọi là thương hiệu thời trang cơ」
- **Mới:** 「Chắc cũng có những cửa hàng đồ thể thao như vậy,\nnhưng ý anh là những cửa hàng gọi là thương hiệu thời trang cơ」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2816 — 双鉄 — pronoun
- **JP:** 「かわいいからこそ、今は、凪の水着を見たい。\n大人な凪を、まずは視線で、楽しみたい」
- **TW:** 「正因為你可愛，我才想看看你穿泳裝。我想先用眼睛觀賞觀賞成熟的你」
- **VN cũ:** 「Chính vì đáng yêu, nên bây giờ, tôi muốn thấy Nagi mặc đồ bơi.\nTrước tiên, tôi muốn dùng ánh mắt để thưởng thức một Nagi chững chạc」
- **Mới:** 「Chính vì đáng yêu, nên bây giờ, anh muốn thấy Nagi mặc đồ bơi.\nTrước tiên, anh muốn dùng ánh mắt để thưởng thức một Nagi chững chạc」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 2862 — 双鉄 — pronoun
- **JP:** 「大真面目だとも。大人っぽい凪がどれほど綺麗か、\n僕は、一刻も早くみたい」
- **TW:** 「當然要認真。我想趕緊看看成熟的你究竟有多漂亮」
- **VN cũ:** 「Rất nghiêm túc là đằng khác. Một Nagi chững chạc sẽ xinh đẹp đến nhường nào,\ntôi muốn được thấy càng sớm càng tốt」
- **Mới:** 「Rất nghiêm túc là đằng khác. Một Nagi chững chạc sẽ xinh đẹp đến nhường nào,\nanh muốn được thấy càng sớm càng tốt」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2879 — 双鉄 — pronoun
- **JP:** 「確かにだ。では、見た目やスペック面のことに\n絞って――ああ、もうひとつ思いついたぞ」
- **TW:** 「確實，那就專精外觀與設計……哦，我又想到一個了」
- **VN cũ:** 「Đúng là vậy. Vậy thì, chỉ tập trung vào\nngoại hình và thông số kỹ thuật thôi——A, tôi nghĩ ra một cái nữa rồi」
- **Mới:** 「Đúng là vậy. Vậy thì, chỉ tập trung vào\nngoại hình và thông số kỹ thuật thôi——A, anh nghĩ ra một cái nữa rồi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2910 — 双鉄 — pronoun
- **JP:** 「脱ごうか？」
- **TW:** 「要我脫嗎？」
- **VN cũ:** 「Để tôi cởi ra nhé?」
- **Mới:** 「Để anh cởi ra nhé?」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2914 — 双鉄 — pronoun
- **JP:** 「撫でられ足りぬなら、あとでいくらでも撫でてやる。\nふたりきりになったとき、凪が、満足しきるまで」
- **TW:** 「要是沒被摸夠的話，回頭你想我怎麼摸我就怎麼摸。到了獨處的時候，我可以摸到你滿意為止」
- **VN cũ:** 「Nếu vuốt ve chưa đủ, lát nữa tôi sẽ vuốt ve em bao nhiêu tùy thích.\nKhi chỉ có hai chúng ta, cho đến khi nào Nagi hoàn toàn thỏa mãn thì thôi」
- **Mới:** 「Nếu vuốt ve chưa đủ, lát nữa anh sẽ vuốt ve em bao nhiêu tùy thích.\nKhi chỉ có hai chúng ta, cho đến khi nào Nagi hoàn toàn thỏa mãn thì thôi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2919 — 双鉄 — pronoun
- **JP:** 「気遣ってくれるのは実に嬉しい。ありがたい。\nが、僕も男だ、多少の見栄というものもある」
- **TW:** 「謝謝你的關照，但我是男人，我得顧著面子」
- **VN cũ:** 「Em lo lắng cho tôi như vậy, tôi thực sự rất vui. Rất biết ơn.\nNhưng, tôi cũng là đàn ông, cũng có chút sĩ diện chứ」
- **Mới:** 「Em lo lắng cho anh như vậy, anh thực sự rất vui. Rất biết ơn.\nNhưng, anh cũng là đàn ông, cũng có chút sĩ diện chứ」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (3 lần trong dòng).

#### 2950 — 双鉄 — pronoun
- **JP:** 「その点はわかるのだが――」
- **TW:** 「這個我也能理解……」
- **VN cũ:** 「Điểm đó thì tôi hiểu, nhưng mà——」
- **Mới:** 「Điểm đó thì anh hiểu, nhưng mà——」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2952 — 双鉄 — pronoun
- **JP:** 「それは単に、凪とふかみとの強い思い出が\n染み付いている品だからだ」
- **TW:** 「這只是因為我對學校泳裝的認識是基於和你還有深美的回憶」
- **VN cũ:** 「Đó đơn giản là vì, nó là món đồ thấm đẫm\nnhững kỷ niệm sâu sắc giữa tôi, Nagi và Fukami thôi」
- **Mới:** 「Đó đơn giản là vì, nó là món đồ thấm đẫm\nnhững kỷ niệm sâu sắc giữa anh, Nagi và Fukami thôi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2957 — 双鉄 — pronoun
- **JP:** 「その点、まったく異論はない」
- **TW:** 「這方面我完全沒有意見」
- **VN cũ:** 「Về điểm đó, tôi hoàn toàn không có ý kiến gì」
- **Mới:** 「Về điểm đó, anh hoàn toàn không có ý kiến gì」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2962 — 双鉄 — pronoun
- **JP:** 「そういうときは『[いろど]彩りの無い色』といえばいい。\n無彩色――これも、日々姫の受け売りだがな」
- **TW:** 「這種時候應該說是不帶色彩的顏色，也就是無彩色。這也是我跟日日姬學的」
- **VN cũ:** 「Những lúc thế này cứ nói là 『Màu không có sắc độ』 là được.\nMàu vô sắc——Cái này, cũng là tôi học mót từ Hibiki thôi」
- **Mới:** 「Những lúc thế này cứ nói là 『Màu không có sắc độ』 là được.\nMàu vô sắc——Cái này, cũng là anh học mót từ Hibiki thôi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

#### 2992 — 双鉄 — pronoun
- **JP:** 「ならば僕はお茶を淹れ。その後は……そうだな、\nヘッドマーク缶バッジでも作っていよう」
- **TW:** 「那我去泡茶。之後嘛……嗯，我做頭像徽章吧」
- **VN cũ:** 「Nếu vậy tôi sẽ đi pha trà. Sau đó thì……để xem nào,\nchắc tôi sẽ làm vài cái huy hiệu biểu trưng đầu tàu vậy」
- **Mới:** 「Nếu vậy anh sẽ đi pha trà. Sau đó thì……để xem nào,\nchắc anh sẽ làm vài cái huy hiệu biểu trưng đầu tàu vậy」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (2 lần trong dòng).

#### 3008 — 双鉄 — pronoun
- **JP:** 「そうはいかん。\n僕とて、多少は水慣れしてきた」
- **TW:** 「開玩笑，我也慢慢會水了啊」
- **VN cũ:** 「Đâu có dễ thế.\nTôi đây cũng đã quen với nước chút đỉnh rồi」
- **Mới:** 「Đâu có dễ thế.\nAnh đây cũng đã quen với nước chút đỉnh rồi」
- **Lý do:** Soutetsu tự xưng 'tôi' với Nagi — sai quy tắc đã chốt (Soutetsu 'anh' với Nagi/Fukami; tiền lệ 凪ふかみ05: 'Soutetsu anh với Nagi/Fukami đúng toàn file'). JP dùng 僕 (hoặc ngôi thứ nhất ngầm định). Đổi 'tôi'→'anh' (1 lần trong dòng).

### Gasp っ — sweep áp nguyên (7 dòng)

#### 2487 — 双鉄 — gasp
- **JP:** 「っ――ぁ――射精……しそう、だ。\nこのまま口に、だしても――いい、のか――」
- **TW:** 「唔……啊……要射了……我可以射你嘴裡嗎……」
- **VN cũ:** 「っ——A——Sắp……xuất tinh, rồi.\nCứ thế này bắn vào miệng, em——có sao, không——」
- **Mới:** 「Ư——A——Sắp……xuất tinh, rồi.\nCứ thế này bắn vào miệng, em——có sao, không——」
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP kết っ――, VN giữ dấu —— nhưng để nguyên ký tự っ (lỗi thô). Thay っ → Ư. (Lưu ý: đây là gasp của Soutetsu — 'sắp xuất tinh' — không phải của Nagi.)

#### 2536 — 双鉄 — gasp
- **JP:** 「っ！」
- **TW:** 「啊！」
- **VN cũ:** 「っ!」
- **Mới:** 「Ư!」
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP chỉ có っ！, VN để nguyên ký tự っ. Thay bằng 'Ư!'.

#### 2544 — 双鉄 — gasp
- **JP:** 「っ！？」
- **TW:** 「啊？！」
- **VN cũ:** 「っ!?」
- **Mới:** 「Ư!?」
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP chỉ có っ！？, VN để nguyên ký tự っ. Thay bằng 'Ư!?'. (Lưu ý: đây là dòng thoại của Soutetsu — gasp của Soutetsu, không phải Nagi.)

#### 3354 — monologue — gasp
- **JP:** ダンボールを抱きしめるようにして、\n凪はくるりと一回転――っ！！？
- **TW:** 凪抱著瓦楞紙箱，原地轉了一個圈……啊？！
- **VN cũ:** Nagi ôm chầm lấy thùng các tông,\nrồi xoay một vòng——!!?
- **Mới:** Nagi ôm chầm lấy thùng các tông,\nrồi xoay một vòng——Ư!!?
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP kết ――っ！！？, VN giữ dấu —— nhưng mất gasp. Thêm Ư.

#### 3433 — monologue — gasp
- **JP:** なのに、これほど濡れている。\nじわじわ、亀頭は食い込むように――っ！
- **TW:** 可是卻已經濕成了這個樣子。我的龜頭就這樣慢慢陷了進去……唔！
- **VN cũ:** Vậy mà, lại ướt đẫm đến thế này.\nTừ từ, quy đầu như đang cắm phập vào——!
- **Mới:** Vậy mà, lại ướt đẫm đến thế này.\nTừ từ, quy đầu như đang cắm phập vào——Ư!
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP kết ――っ！, VN giữ dấu —— nhưng mất gasp. Thêm Ư.

#### 3610 — monologue — gasp
- **JP:** 動かしたのがお気に召したか、\n凪はきゃっきゃと、あどけないような笑顔――っ！？
- **TW:** 我動了動雞巴似乎讓凪很開心，她露出了歡快的稚嫩笑容……啊？！
- **VN cũ:** Có vẻ thích thú khi thấy nó cử động,\nNagi cười khúc khích, một nụ cười ngây thơ——!?
- **Mới:** Có vẻ thích thú khi thấy nó cử động,\nNagi cười khúc khích, một nụ cười ngây thơ——Ư!?
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP kết ――っ！？, VN giữ dấu —— nhưng mất gasp. Thêm Ư.

#### 3719 — monologue — gasp
- **JP:** それから凪はまたキョロキョロして――っ！？
- **TW:** 接著，她的眼珠子又滴溜溜地轉了一圈……嗯？！
- **VN cũ:** Sau đó Nagi lại ngó ngoáy xung quanh——!?
- **Mới:** Sau đó Nagi lại ngó ngoáy xung quanh——Ư!?
- **Lý do:** Sweep lost-gasp-trailing áp nguyên đã kiểm chứng: JP kết ――っ！？, VN giữ dấu —— nhưng mất gasp. Thêm Ư.

### fa/fu (5 dòng)

#### 2405 — 凪 — fa/fu
- **JP:** 「ひぎゅっ！　あ！　すごいっ――すご、かっっ――\nはっ――ふあっ、あっ――おまん、こ、ぐりゅっ、て」
- **TW:** 「呀！啊！好棒……好棒……啊……啊，啊……下面好緊」
- **VN cũ:** 「Higyu! A! Tuyệt quá——Tuyệt, quá——\nHà——Phù, a——Âm, đạo, ngoáy, á」
- **Mới:** 「Higyu! A! Tuyệt quá——Tuyệt, quá——\nHà——Phù a, a——Âm, đạo, ngoáy, á」
- **Lý do:** ふあっ → 'Phù a' (phán quyết parent 20/11: ふあっ → 'Phù a' giữ nguyên dạng tách âm tiết); VN cũ 'Phù, a' tách sai dấu phẩy — 'Phù' + 'a' đọc thành hai âm riêng, trong khi ふあ là một âm tiết 'Phù a' và あっ sau đó mới là 'a'.

#### 2449 — 凪 — fa/fu
- **JP:** 「ふあっ――あっ――んっ――く、うっ――ふあ――\nここ――んっ――ふっ――もう、ちょっと――あうっ」
- **TW:** 「哇……啊……嗯……唔，哇……這裡……嗯，呼……還差一點……啊嗚」
- **VN cũ:** 「Phù——A——Ưm——Ư, ư——Phù——\nChỗ này——Ưm——Phù——Một chút, nữa——A」
- **Mới:** 「Phù a——A——Ưm——Ư, ư——Phù a——\nChỗ này——Ưm——Phù——Một chút, nữa——Au」
- **Lý do:** ふあっ → 'Phù a' và ふあ → 'Phù a' (phán quyết parent 20/11); あうっ → 'Au' (nguyên âm đôi au). VN cũ tách ふあ thành 'Phù' và bỏ mất âm u của あう.

#### 2451 — 凪 — fa/fu
- **JP:** 「ふぁ……ぁ……これ……凄かとばい……\nん……わ……わわ……ええ……どうしよう、ばい」
- **TW:** 「哇……啊……這……太厲害了……唔……哇……哇哇……哎，這可怎麼辦」
- **VN cũ:** 「Phù……A……Cái này……Kinh khủng quá á……\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」
- **Mới:** 「Phà……A……Cái này……Kinh khủng quá á……\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」
- **Lý do:** ふぁ……ぁ → 'Phà……A' — ふぁ → 'Phà' (phán quyết parent: ふぁ → 'phà'); ぁ → 'A'. VN cũ 'Phù' sai âm (ふぁ không phải ふあ).

#### 2462 — 凪 — fa/fu
- **JP:** 「ふぁっ！？」
- **TW:** 「哇？！」
- **VN cũ:** 「Hya!?」
- **Mới:** 「Phà!?」
- **Lý do:** ふぁっ → 'Phà' (phán quyết parent 20/11: ふぁ → 'phà') — VN cũ 'Hya' hoàn toàn sai âm.

#### 2563 — 凪 — fa/fu
- **JP:** 「ん……ちゅううっ――ちゅっ――んっ――ぷっ、\nふぁっ――れろっ――れるっ――ぺろぺろ、ちゅっ」
- **TW:** 「嗯……啾，啾，嗯……噗，哇，啾，啾，啾，啾」
- **VN cũ:** 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nPhù a——Ngoáy——Ngoáy——Liếm liếm, chụt」
- **Mới:** 「Ưm……Chụttt——Chụt——Ưm——Phụt,\nPhà——Ngoáy——Ngoáy——Liếm liếm, chụt」
- **Lý do:** ふぁっ → 'Phà' (phán quyết parent 20/11: ふぁ → 'phà') — VN cũ 'Phù a' sai âm (đây là ふぁ, không phải ふあ).

### SFX — mất âm / sai âm (15 dòng)

#### 2401 — 凪 — sfx
- **JP:** 「ひゅあっ――あっ――そこ、だけ――ん、きゅふっ、\nあっ――なぎ、ウチ――ウチ――らめ、なっちゃうっ」
- **TW:** 「呀……啊，就一個地方……嗯，呀，啊，本……咱，咱……會瘋掉的」
- **VN cũ:** 「Hyua——A——Chỉ, chỗ đó——Ưm, a,\nA——Nagi, em——em——hỏng, mất thôi」
- **Mới:** 「Hyua——A——Chỉ, chỗ đó——Ưm, Kyufu,\nA——Nagi, em——em——hỏng, mất thôi」
- **Lý do:** きゅふっ → 'Kyufu' — VN cũ 'a' mất cả hai âm tiết きゅ+ふ; tiền lệ 'Kyufu' cho きゅふ (xem §1). Chỉ thay 'a' → 'Kyufu'.

#### 2402 — 凪 — sfx
- **JP:** 「ひゃう」
- **TW:** 「呀」
- **VN cũ:** 「Hya」
- **Mới:** 「Hyau」
- **Lý do:** ひゃう → 'Hyau' — VN cũ 'Hya' mất âm u; đa số toàn dự án dùng 'Hyau' cho ひゃう (ふかみh3 1158, ハチロクh5 1080, ハチロク14 2674).

#### 2409 — 凪 — sfx
- **JP:** 「かひゅっ！！！」
- **TW:** 「呀！！！」
- **VN cũ:** 「Hya!!!」
- **Mới:** 「Kahyu!!!」
- **Lý do:** かひゅっ → 'Kahyu' — VN cũ 'Hya' mất cả か+ひゅ; tiền lệ lr稀咲追加h 1089: かひゅっ → 'Kahyu'.

#### 2410 — 凪 — sfx
- **JP:** 「きゃっ、ふうううううううううぅぅぅぅっ！！！」
- **TW:** 「呀，唔！！！」
- **VN cũ:** 「Kya, phuuuuuuuuuuuuuuuuu!!!」
- **Mới:** 「Kya, phuuuuuuuuuuuuuuu!!!」
- **Lý do:** ふうううううううううぅぅぅぅ: đếm nguyên âm — VN cũ 17 chữ u, quy tắc 1 + 10う + 4ぅ = 15 chữ u (đã đếm bằng script). Sửa về 15.

#### 2414 — 凪 — sfx
- **JP:** 「ひあああっ――そこっ――そこ――んひっ、\nいっ、あっ――きもち、よかっ――気持ち、よかぁ」
- **TW:** 「呀，這裡，這裡……嗯，舒服，啊……好舒服，好舒服」
- **VN cũ:** 「Hiaaa——Chỗ đó——Chỗ đó——Ưm,\nA, a——Sướng, quá——Sướng, quá á」
- **Mới:** 「Hiaaa——Chỗ đó——Chỗ đó——Ưm hi,\nA, a——Sướng, quá——Sướng, quá á」
- **Lý do:** んひっ → 'Ưm hi' — VN cũ 'Ưm' mất âm ひ; dạng chuẩn toàn dự án cho んひっ là 'Ưm hi'/'Ưm hí'/'Nhi'.

#### 2416 — 凪 — sfx
- **JP:** 「ひゃあああっ！？」
- **TW:** 「呀？！」
- **VN cũ:** 「Hyaaa!?」
- **Mới:** 「Hyaaaa!?」
- **Lý do:** ひゃあああっ = ひゃ + あ×3 → 4 chữ a; VN cũ 'Hyaaa' chỉ có 3 chữ a. Sửa thành 'Hyaaaa'.

#### 2453 — 凪 — sfx
- **JP:** 「あわわわわっ」
- **TW:** 「哇哇哇」
- **VN cũ:** 「Á á á á」
- **Mới:** 「Awa wa wa wa」
- **Lý do:** あわわわわっ → 'Awa wa wa wa' — VN cũ 'Á á á á' mất âm w; tiền lệ グランドリライト07: あわわ → 'Awa wa'.

#### 2461 — 凪 — sfx
- **JP:** 「わわわ、想像もつかんとばい！」
- **TW:** 「哇哇哇，完全無法想像」
- **VN cũ:** 「Oa oa, không thể tưởng tượng nổi luôn á!」
- **Mới:** 「Oa oa oa, không thể tưởng tượng nổi luôn á!」
- **Lý do:** わわわ (3 lần) → 'Oa oa oa' — VN cũ chỉ có 2 lần 'Oa oa'; cùng file ở 2455/2457/2458 đều dùng 3 lần 'Oa oa oa' cho わわわ.

#### 2483 — 凪 — sfx
- **JP:** 「んんんっ――や――あっ――もっと――おま、んこ、\nよか、とこ――ある――のにっ――んっ――ふっ」
- **TW:** 「唔……不要……啊……再進來點……還有更舒服的地方……嗯……唔」
- **VN cũ:** 「Ưm——A——A——Âm, đạo, vẫn còn——\nchỗ, sướng, hơn——mà——Ưm——Phù」
- **Mới:** 「Ưmmm——Ya——A——Âm, đạo, vẫn còn——\nchỗ, sướng, hơn——mà——Ưm——Phù」
- **Lý do:** んんんっ (3 âm mũi) → 'Ưmmm'; や → 'Ya' — VN cũ 'Ưm' chỉ có 1 m và 'A' mất âm y. Tiền lệ: んんん → 'Ưmmm' (xem §1); や → 'Ya' (như 2555/2917).

#### 2489 — 凪 — sfx
- **JP:** 「くっ――ふっ――んひゅっ――んんん～っ！」
- **TW:** 「唔……嗯……嗯……嗯！」
- **VN cũ:** 「Ư——Phù——Ưm——Ưm~!!」
- **Mới:** 「Ư——Phù——Ưm hứ——Ưmmm~!!」
- **Lý do:** んひゅっ → 'Ưm hứ' (dạng chuẩn toàn dự án); んんん～っ (3 âm mũi) → 'Ưmmm~'. VN cũ 'Ưm' và 'Ưm~' mất âm.

#### 2512 — 凪 — sfx
- **JP:** 「んひゅっ！！！？」
- **TW:** 「唔？！」
- **VN cũ:** 「Hya!!!?」
- **Mới:** 「Ưm hứ!!!?」
- **Lý do:** んひゅっ → 'Ưm hứ' — VN cũ 'Hya' hoàn toàn sai âm; dạng chuẩn toàn dự án cho んひゅっ là 'Ưm hứ'.

#### 2520 — 凪 — sfx
- **JP:** 「かっ――はっ！　あっ！　あぐっ――かふっ！\nはぁっ！　はあっ！　はあっ！　はあっ！」
- **TW:** 「啊……啊！啊！唔……唔！啊！啊！啊！啊」
- **VN cũ:** 「Hà——Hà! A! A——Hà!\nHà! Hà! Hà! Hà!」
- **Mới:** 「Kà——Hà! A! Agù——Kaphù!\nHà! Hà! Hà! Hà!」
- **Lý do:** かっ → 'Kà' (VN cũ 'Hà' sai âm — か không phải は); あぐっ → 'Agù' (PHÁN ĐOÁN, xem §5 — 'A' mất âm ぐ; tiền lệ 'Agu' lr_稀咲h1 998, ngược với 3 file dùng 'A'/'Á' — cần parent chốt); かふっ → 'Kaphù' (tiền lệ paulette-h7 899: きゃふっ → 'Kyaphù'; VN cũ 'Hà' mất cả か+ふ).

#### 2529 — 凪 — sfx
- **JP:** 「あー」
- **TW:** 「啊」
- **VN cũ:** 「Aaa」
- **Mới:** 「Aa」
- **Lý do:** あー → 'Aa' — đếm nguyên âm: あ + ー = 2 chữ a; VN cũ 'Aaa' thừa một a. (Lưu ý tiền lệ mâu thuẫn: 日々姫06 dùng 'Aaa!' cho あー！ — xem §5.)

#### 2555 — 凪 — sfx
- **JP:** 「んっ――やっ――いやっ――動い、ちゃう、とよ、\n――ふっ――あっ――にい、さん、の、おちん、ちん」
- **TW:** 「嗯……不，不要……別動啊，呼……啊……大哥哥的雞巴」
- **VN cũ:** 「Ưm——A——Không——Di chuyển, mất, á,\n——Phù——A——Dương, vật, của, anh, hai」
- **Mới:** 「Ưm——Ya——Không——Di chuyển, mất, á,\n——Phù——A——Dương, vật, của, anh, hai」
- **Lý do:** やっ → 'Ya' — VN cũ 'A' mất âm y; tiền lệ: や → 'Ya' (như 2483/2917).

#### 2917 — 凪 — sfx
- **JP:** 「や――なんで、にいさん」
- **TW:** 「討厭，為什麼，大哥哥」
- **VN cũ:** 「A——Sao vậy, anh hai」
- **Mới:** 「Ya——Sao vậy, anh hai」
- **Lý do:** や―― → 'Ya——' — VN cũ 'A' mất âm y.

### Đếm nguyên âm ああ/おお (9 dòng)

#### 2514 — 双鉄 — vowel-count
- **JP:** 「ああ――」
- **TW:** 「啊……」
- **VN cũ:** 「A——」
- **Mới:** 「Aa——」
- **Lý do:** ああ―― → 'Aa——' — đếm nguyên âm: ああ = 2 chữ a; tiền lệ 1846: ああ―― → 'Aa——'.

#### 2603 — 双鉄 — vowel-count
- **JP:** 「おお――おおっ！！？」
- **TW:** 「噢……噢？！」
- **VN cũ:** 「Oa——Oaaa!!?」
- **Mới:** 「Oo——Oo!!?」
- **Lý do:** おお――おおっ → 'Oo——Oo' — đếm nguyên âm: おお = 2 chữ o; VN cũ 'Oa——Oaaa' sai nguyên âm (a thay vì o).

#### 2607 — 凪 — vowel-count
- **JP:** 「おおお、納得ばい！　なんかにーさんすごかとね！\n日々姫ねーちゃんみたいでカッコよかばい！」
- **TW:** 「噢有道理！大哥哥厲害！就像日日姬一樣帥氣！」
- **VN cũ:** 「Oa, nghe có lý á! Sao anh hai giỏi thế á!\nNgầu như chị Hibiki luôn á!」
- **Mới:** 「Ooo, nghe có lý á! Sao anh hai giỏi thế á!\nNgầu như chị Hibiki luôn á!」
- **Lý do:** おおお (3 chữ o) → 'Ooo' — VN cũ 'Oa' sai nguyên âm (a thay vì o).

#### 2612 — 凪 — vowel-count
- **JP:** 「おおお、にーさんなんだかマジメばい！」
- **TW:** 「噢，大哥哥看起來好認真！」
- **VN cũ:** 「Oa, anh hai trông nghiêm túc ghê á!」
- **Mới:** 「Ooo, anh hai trông nghiêm túc ghê á!」
- **Lý do:** おおお (3 chữ o) → 'Ooo' — VN cũ 'Oa' sai nguyên âm (a thay vì o).

#### 2613 — 凪 — vowel-count
- **JP:** 「おお、日ノ本語、奥のふかかとばーい！」
- **TW:** 「噢，語言真是奧妙無窮！」
- **VN cũ:** 「Oa, tiếng Hinomoto, thâm thúy thật á!」
- **Mới:** 「Oo, tiếng Hinomoto, thâm thúy thật á!」
- **Lý do:** おお (2 chữ o) → 'Oo' — VN cũ 'Oa' sai nguyên âm (a thay vì o).

#### 2751 — 凪 — vowel-count
- **JP:** 「空いたばーい！　じゃじゃんっ！！\nお？　おおお――おおおおおっ！！！？」
- **TW:** 「打開了！鏘鏘！！噢？噢噢噢……噢噢噢？！」
- **VN cũ:** 「Mở được rồi á! Tada!!\nỦa? Oaa——Oaaaaa!!!?」
- **Mới:** 「Mở được rồi á! Tada!!\nỦa? Ooo——Ooooo!!!?」
- **Lý do:** おおお――おおおおおっ → 'Ooo——Ooooo' — đếm nguyên âm: 3 o + 5 o; VN cũ 'Oaa——Oaaaaa' sai nguyên âm (a thay vì o).

#### 2776 — 双鉄 — vowel-count
- **JP:** 「ああ――」
- **TW:** 「是啊」
- **VN cũ:** 「À——」
- **Mới:** 「Aa——」
- **Lý do:** ああ―― → 'Aa——' — đếm nguyên âm: ああ = 2 chữ a; tiền lệ 1846.

#### 4016 — monologue — vowel-count
- **JP:** （ああ……凪は、おんなになったのだな）
- **TW:** （啊……凪已經變成女人了啊）
- **VN cũ:** （A……Nagi, đã trở thành một người phụ nữ rồi nhỉ）
- **Mới:** （Aa……Nagi, đã trở thành một người phụ nữ rồi nhỉ）
- **Lý do:** ああ…… → 'Aa……' — đếm nguyên âm: ああ = 2 chữ a.

#### 4023 — monologue — vowel-count
- **JP:** （ああ――そうだよな）
- **TW:** （嗯，是啊）
- **VN cũ:** （A——Đúng rồi nhỉ）
- **Mới:** （Aa——Đúng rồi nhỉ）
- **Lý do:** ああ―― → 'Aa——' — đếm nguyên âm: ああ = 2 chữ a; tiền lệ 1846.

### Nghĩa / bịa thêm (3 dòng)

#### 2749 — 凪 — meaning
- **JP:** 「あけんと――んと、\nあ！　ここを押せって書いてあるとばい！」
- **TW:** 「打不開……唔，啊！這裡寫了按下去！」
- **VN cũ:** 「Phải mở ra——Ưm,\nA! Ở đây có ghi là ấn vào chỗ này á!」
- **Mới:** 「Mở không ra——Ưm,\nA! Ở đây có ghi là ấn vào chỗ này á!」
- **Lý do:** あけんと = 'không mở được' (あける + phủ định) — VN cũ 'Phải mở ra' nghĩa ngược hoàn toàn ('phải mở' = must open). Sửa thành 'Mở không ra'.

#### 3346 — monologue — meaning
- **JP:** 僕のおでこをぺちりと叩き、\n凪はえへんと無い、胸を……張……る……
- **TW:** 凪彈了一下我的額頭，然後挺了挺她不存在的胸部。
- **VN cũ:** Vỗ nhẹ một cái lên trán tôi,\nNagi hắng giọng một tiếng, rồi ưỡn……ngực……ra……
- **Mới:** Vỗ nhẹ một cái lên trán tôi,\nNagi hắng giọng một tiếng, rồi ưỡn bộ ngực vốn chẳng có……ra……
- **Lý do:** JP có 無い ('không có') — 'bộ ngực không có' — VN cũ bỏ mất, dịch thành 'ưỡn ngực ra' như thể Nagi có ngực. Thêm 'bộ ngực vốn chẳng có'.

#### 3717 — monologue — meaning
- **JP:** ともはりに、剣術修行に日々の投炭。\n――筋肉疲労は、相当だろう。
- **TW:** 掌櫓、劍術修行外加每日的加煤，她的肌肉一定非常疲憊。
- **VN cũ:** Chèo thuyền, luyện kiếm, rồi còn xúc than dồn toa mỗi ngày.\n——Cơ bắp chắc hẳn phải mệt mỏi lắm.
- **Mới:** Chèo thuyền, luyện kiếm, rồi còn xúc than mỗi ngày.\n——Cơ bắp chắc hẳn phải mệt mỏi lắm.
- **Lý do:** 投炭 = 'xúc than' (xúc than vào lò) — VN cũ thêm 'dồn toa' (ghép toa xe) là bịa, không có trong JP hay TW. Bỏ 'dồn toa'. ('Xúc than' đã có tiền lệ ở Common 13; 'ném than' ở Common 05.)
## 4. Lượt soát 2 (second pass)

Đọc lại toàn bộ 89 giá trị fix đối chiếu JP: **89/89 tái kiểm chứng, 0 bỏ, 0 sửa.**
- JSON 89 khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 89/89; mọi fix khác VN cũ đúng ở chỗ sửa nhắm tới (diff-sanity đã kiểm tra từng dòng).
- Khối TOML parse OK (tomllib), 89 khóa, 0 sai lệch giá trị so với JSON.
- Diff-sanity (difflib): mọi fix chỉ khác VN cũ ở đúng chỗ sửa nhắm tới — 0 fix viết lại lớn.
- 0 giá trị fix chứa ký tự xuống dòng thật; `\n` trong fix viết dạng `\\n` trong khối TOML.
- Riêng 2410 đã đếm lại bằng script: VN cũ 17 chữ u, fix 15 chữ u (1 + 10う + 4ぅ).
- Đại từ đã quét lại case-insensitive toàn file: 50 dòng thoại Soutetsu chứa 'tôi' (61 lần), 0 dòng chứa 'chúng tôi'/'bọn tôi', 0 dòng Soutetsu tự xưng 'anh' đúng — toàn bộ 50 dòng đều cần sửa, không sót dòng nào chỉ có 'Tôi' viết hoa đầu câu (2712, 2717 là 2 dòng suýt sót).

## 5. Chờ Hieu / phán đoán cần chốt

- **Phán đoán SFX (đã sửa theo tiền lệ, parent xem lại):** 2520 あぐっ → 'Agù' — 'A' mất âm ぐ; tiền lệ mâu thuẫn: 3 file dùng 'A'/'Á' (共通05 2284, 共通09 2326 — đã audit, giữ nguyên; lr_稀咲h1 1035 — chưa audit) vs 1 file 'Agu' (lr_稀咲h1 998 — chưa audit). Nếu parent chốt 'A' thì hoàn lại 2520 về 'A' (2 sửa còn lại trong dòng — かっ → 'Kà', かふっ → 'Kaphù' — vẫn giữ).
- **2529 あー → 'Aa':** tiền lệ mâu thuẫn — 日々姫06 dùng 'Aaa!' cho あー！ (chưa audit). Nếu parent chốt 'Aaa' cho あー thì hoàn lại.
- **Không chắc chắn (giữ nguyên, không sửa):** 2395 んきゅっ → 'Ưm' (âm きゅ bị nuốt vào âm mũi; chưa có cách render chuẩn cho んきゅっ — 'Ưm kyu' nghe gượng); 2515 câu nói ngọng đã giải mã ('Nóng quá', 'Tinh dịch' — TW đồng ý); 2378 tiếng gọi tên dịch theo ý đồ ('Không cho anh thoát đâu á!!' — TW đồng ý); 2397 ゅっ → 'm' (mảnh rên); 2492 ん～～っっ → 'Ưm~~' (tiền lệ ハチロクh6 1085: ～～～～っっ → '~~~~ƯƯ' — dòng này chỉ có 2 dấu ~ nên 'Ưm~~' giữ nguyên); 2599/2597 えへへー → 'Ehehe' (chuẩn toàn dự án, đã audit ở ハチロク14).
- **Giữ nguyên theo chuẩn dự án (không phải lỗi):** 2469/2471/3017/2979 ああ đầu câu → 'À'/'A' (từ cảm thán ngắn, khác với ああ―― kéo dài đã sửa ở 2776/4023/2514/4016); 2602 おお―― → 'Ồ——' và 2608/2610 おお(お)！ → 'Ồ!' (từ cảm thán 'Ồ' chuẩn toàn dự án — khác với 'Oa' sai nguyên âm đã sửa ở 2603/2607/2612/2613/2751); 2655 わーわー → 'Oa oa' (わ → 'Oa' là quy ước toàn dự án); 2848 カチっ → 'click' (dịch theo nghĩa hành động bấm chuột, không phải âm thanh bị mất); 3853 てっ！ → '——!' (っ ngắt câu, đã render bằng dấu gạch).
- **Đợt thống nhất (không đếm là lỗi, chờ Hieu chốt phạm vi/thời điểm):** 御一夜鉄道 → 'Đường sắt Ohito' (1766, 3568 — dạng cũ, chuẩn là 'Ohitoyo'); 帝大 → 'Đại học Hoàng gia' (1759 — dạng cũ, chuẩn là 'Đại học Đế quốc'); まいてつ契約 → 'hợp đồng Maitetsu' (1766 — dạng cũ, chuẩn là 'hợp đồng chủ tàu'); 'Phù a' giữ nguyên 5 dòng (2452, 2445, 2589, 2428, 2526 — phán quyết parent 20/11, đưa vào đợt thống nhất); 2668 じーちゃん/ばーちゃん → 'ông nội, bà nội' (chờ Hieu chốt 'ông nội' hay 'ông ngoại' — Midori là mẹ Fukami).

## 6. Khối TOML (đã parse-verified, 89 khóa, 0 sai lệch)

```toml
[script]
1778 = "「……Có lẽ anh sẽ muốn liếm láp Nagi trong bộ đồ bơi đấy」"
1793 = "「……Đồ bơi quy định của trường. Bộ đó,\\nanh nghĩ là trái ngược hoàn toàn với sự chững chạc đấy」"
1797 = "「……Đúng hơn là, nên nghĩ ngược lại với bản thân màu đậm thì sao?\\nNhững màu cơ bản, dù là màu gì đi nữa, anh có cảm giác đều mang lại ấn tượng trẻ trung」"
2264 = "「Không phải thắng mà không cần đánh. Đây là kết quả của một trận đấu quang minh chính đại.\\nTrước sức hấp dẫn của Nagi——sức hấp dẫn của một người phụ nữ, anh đã thua rồi」"
2276 = "「Nhưng mà……nếu vậy thì, lại càng khó khăn hơn nhỉ.\\nAnh thì nếu được muốn tránh mua đồ bơi cũ」"
2277 = "「Nhưng mà, anh cũng không phải đang tỏ vẻ đâu」"
2282 = "「Không, anh chẳng ung dung chút nào đâu」"
2306 = "「Sao trăng gì, anh là kẻ bại trận trước Nagi mà」"
2310 = "「Hôm nay, nếu không có lệnh của Nagi,\\nanh hoàn toàn không thể làm gì cả」"
2319 = "「Nhưng mà……em định mặc thế này đi bơi sao?\\nNói thật thì, anh——không muốn ai khác ngoài anh nhìn thấy Nagi lúc này đâu」"
2394 = "「Không, nhưng mà, là anh tặng quà cho em cơ mà?」"
2401 = "「Hyua——A——Chỉ, chỗ đó——Ưm, Kyufu,\\nA——Nagi, em——em——hỏng, mất thôi」"
2402 = "「Hyau」"
2405 = "「Higyu! A! Tuyệt quá——Tuyệt, quá——\\nHà——Phù a, a——Âm, đạo, ngoáy, á」"
2409 = "「Kahyu!!!」"
2410 = "「Kya, phuuuuuuuuuuuuuuu!!!」"
2414 = "「Hiaaa——Chỗ đó——Chỗ đó——Ưm hi,\\nA, a——Sướng, quá——Sướng, quá á」"
2416 = "「Hyaaaa!?」"
2449 = "「Phù a——A——Ưm——Ư, ư——Phù a——\\nChỗ này——Ưm——Phù——Một chút, nữa——Au」"
2451 = "「Phà……A……Cái này……Kinh khủng quá á……\\nƯm……Oa……Oa oa……Ể……Phải làm sao đây, á」"
2453 = "「Awa wa wa wa」"
2461 = "「Oa oa oa, không thể tưởng tượng nổi luôn á!」"
2462 = "「Phà!?」"
2467 = "「A! Anh hiểu rồi.\\nĐúng là, cảm giác mới mẻ mãnh liệt thì sẽ vui hơn nhỉ」"
2474 = "「Anh muốn được nói chuyện đàng hoàng một lần ghê.\\nVới bà nội của Nagi ấy」"
2483 = "「Ưmmm——Ya——A——Âm, đạo, vẫn còn——\\nchỗ, sướng, hơn——mà——Ưm——Phù」"
2487 = "「Ư——A——Sắp……xuất tinh, rồi.\\nCứ thế này bắn vào miệng, em——có sao, không——」"
2489 = "「Ư——Phù——Ưm hứ——Ưmmm~!!」"
2504 = "「Hừm, vậy sao. Nếu vậy thì anh sẽ không nhớ lại đoạn đó nữa」"
2512 = "「Ưm hứ!!!?」"
2514 = "「Aa——」"
2520 = "「Kà——Hà! A! Agù——Kaphù!\\nHà! Hà! Hà! Hà!」"
2529 = "「Aa」"
2536 = "「Ư!」"
2544 = "「Ư!?」"
2555 = "「Ưm——Ya——Không——Di chuyển, mất, á,\\n——Phù——A——Dương, vật, của, anh, hai」"
2563 = "「Ưm……Chụttt——Chụt——Ưm——Phụt,\\nPhà——Ngoáy——Ngoáy——Liếm liếm, chụt」"
2574 = "「Ừm. Nó đây.\\nMau thay rồi cho anh xem đi」"
2576 = "「Có, anh thích em. Rất thích——đấy!」"
2578 = "「Ừm. Anh cũng muốn em làm vậy」"
2579 = "「Ừm. Quả thực là một lời dạy rất hay, anh cũng nghĩ vậy」"
2603 = "「Oo——Oo!!?」"
2607 = "「Ooo, nghe có lý á! Sao anh hai giỏi thế á!\\nNgầu như chị Hibiki luôn á!」"
2610 = "「Ồ! Vậy thì mau cho anh xem đi」"
2612 = "「Ooo, anh hai trông nghiêm túc ghê á!」"
2613 = "「Oo, tiếng Hinomoto, thâm thúy thật á!」"
2710 = "「Nagi……anh muốn chạm vào em——Chạm vào em, được không」"
2712 = "「Anh cũng không rành lắm nhưng——\\nTiêu biểu thì có Channel, hay là Vucci chẳng hạn」"
2714 = "「Anh cũng muốn thế lắm, nhưng bây giờ phải nhịn thôi.\\nĐể khắc sâu hình ảnh Nagi mặc đồ bơi một cách sống động nhất」"
2716 = "「Anh cũng vậy. Ừm……\\nChỉ những lúc thế này, anh mới thấy nhớ Đế đô một chút」"
2717 = "「Anh cũng vậy. Rất thích, Nagi」"
2720 = "「Không nghĩ ra được gì nữa.\\nCó vẻ anh không mấy hứng thú với đồ bơi của trường」"
2728 = "「Đang khen ngợi hết lời đấy chứ.\\nVì anh cũng rất thích một Nagi không hay viện cớ như thường ngày mà」"
2730 = "「Anh muốn em cứ thoải mái chọn thứ mình thích nhất, thứ mà em không cho là không biết lượng sức,\\nmà không cần phải bận tâm đến giá cả」"
2733 = "「Rất sẵn lòng——nhưng mà. Trước đó,\\nanh muốn giải quyết xong chuyện đồ bơi đã」"
2735 = "「Anh muốn được thấy một Nagi trong bộ đồ bơi khác ngày thường.\\nBản thân điều đó, đã là mong muốn của anh rồi」"
2736 = "「Anh chưa từng nghĩ đến chuyện đó」"
2738 = "「Anh cũng chẳng khác Nagi là mấy đâu.\\nNgoài những gì học được trong công việc ra, thì anh hoàn toàn mù tịt」"
2743 = "「Do đó, nãy giờ anh đã cố gắng hết sức để nhớ lại, nhưng\\nnhững gì anh có thể nhớ được từ đó trở đi, là của Nagi và Fukami」"
2745 = "「Do đó. Nếu nghĩ ngược lại với đồ bơi của trường,\\nanh nghĩ chúng ta có thể tìm ra được sự chững chạc」"
2749 = "「Mở không ra——Ưm,\\nA! Ở đây có ghi là ấn vào chỗ này á!」"
2751 = "「Mở được rồi á! Tada!!\\nỦa? Ooo——Ooooo!!!?」"
2754 = "「Xin lỗi nhé. Anh vừa nảy ra một ý tưởng hay——\\nHay nói đúng hơn là, anh đang bị sốc trước sự ngốc nghếch của bản thân」"
2776 = "「Aa——」"
2778 = "「Đúng vậy. Chỉ cần chọn đồ thì thế là đủ rồi.\\nViệc thanh toán anh sẽ lo, nên cho đến lúc quyết định xong thì Nagi cứ thao tác đi」"
2783 = "「Anh thua rồi. Hoàn toàn bị em bắt được rồi.\\nAnh muốn được chạm vào Nagi, càng sớm càng tốt」"
2792 = "「Nagi đôi khi, thông minh đến mức khiến anh phải kinh ngạc đấy」"
2794 = "「Chắc cũng có những cửa hàng đồ thể thao như vậy,\\nnhưng ý anh là những cửa hàng gọi là thương hiệu thời trang cơ」"
2816 = "「Chính vì đáng yêu, nên bây giờ, anh muốn thấy Nagi mặc đồ bơi.\\nTrước tiên, anh muốn dùng ánh mắt để thưởng thức một Nagi chững chạc」"
2862 = "「Rất nghiêm túc là đằng khác. Một Nagi chững chạc sẽ xinh đẹp đến nhường nào,\\nanh muốn được thấy càng sớm càng tốt」"
2879 = "「Đúng là vậy. Vậy thì, chỉ tập trung vào\\nngoại hình và thông số kỹ thuật thôi——A, anh nghĩ ra một cái nữa rồi」"
2910 = "「Để anh cởi ra nhé?」"
2914 = "「Nếu vuốt ve chưa đủ, lát nữa anh sẽ vuốt ve em bao nhiêu tùy thích.\\nKhi chỉ có hai chúng ta, cho đến khi nào Nagi hoàn toàn thỏa mãn thì thôi」"
2917 = "「Ya——Sao vậy, anh hai」"
2919 = "「Em lo lắng cho anh như vậy, anh thực sự rất vui. Rất biết ơn.\\nNhưng, anh cũng là đàn ông, cũng có chút sĩ diện chứ」"
2950 = "「Điểm đó thì anh hiểu, nhưng mà——」"
2952 = "「Đó đơn giản là vì, nó là món đồ thấm đẫm\\nnhững kỷ niệm sâu sắc giữa anh, Nagi và Fukami thôi」"
2957 = "「Về điểm đó, anh hoàn toàn không có ý kiến gì」"
2962 = "「Những lúc thế này cứ nói là 『Màu không có sắc độ』 là được.\\nMàu vô sắc——Cái này, cũng là anh học mót từ Hibiki thôi」"
2992 = "「Nếu vậy anh sẽ đi pha trà. Sau đó thì……để xem nào,\\nchắc anh sẽ làm vài cái huy hiệu biểu trưng đầu tàu vậy」"
3008 = "「Đâu có dễ thế.\\nAnh đây cũng đã quen với nước chút đỉnh rồi」"
3346 = "Vỗ nhẹ một cái lên trán tôi,\\nNagi hắng giọng một tiếng, rồi ưỡn bộ ngực vốn chẳng có……ra……"
3354 = "Nagi ôm chầm lấy thùng các tông,\\nrồi xoay một vòng——Ư!!?"
3433 = "Vậy mà, lại ướt đẫm đến thế này.\\nTừ từ, quy đầu như đang cắm phập vào——Ư!"
3610 = "Có vẻ thích thú khi thấy nó cử động,\\nNagi cười khúc khích, một nụ cười ngây thơ——Ư!?"
3717 = "Chèo thuyền, luyện kiếm, rồi còn xúc than mỗi ngày.\\n——Cơ bắp chắc hẳn phải mệt mỏi lắm."
3719 = "Sau đó Nagi lại ngó ngoáy xung quanh——Ư!?"
4016 = "（Aa……Nagi, đã trở thành một người phụ nữ rồi nhỉ）"
4023 = "（Aa——Đúng rồi nhỉ）"
```

## Kết bài

File 凪h2_おとなの水着 (673 dòng) có 89 dòng sai (13,2%) — lỗi hệ thống lớn nhất là đại từ: Soutetsu xưng 'tôi' với Nagi trong 50 dòng (61 lần), ngược hoàn toàn với tiền lệ 凪ふかみ05; còn lại là SFX/gasp (7 sweep áp nguyên + 15 SFX mất/sai âm + 5 fa/fu), đếm nguyên âm ああ/おお (9 dòng, trong đó 5 dòng 'Oa' sai nguyên âm o→a), và 3 lỗi nghĩa (2749 'Phải mở ra' ngược nghĩa với あけんと; 3346 bỏ mất 無い; 3717 bịa thêm 'dồn toa'). Không lệch dòng, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Khối TOML 89 khóa đã parse-verified, 0 sai lệch; lượt soát 2: 89/89, 0 bỏ, 0 sửa. Một phán đoán cần parent chốt: 2520 あぐっ → 'Agù' (tiền lệ mâu thuẫn 3 'A' vs 1 'Agu'); đợt thống nhất chờ Hieu: 'Đường sắt Ohito' (2), 'Đại học Hoàng gia' (1), 'hợp đồng Maitetsu' (1), 'Phù a' (5), 'ông nội/bà nội' (1).
