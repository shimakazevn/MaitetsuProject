# Audit — ハチロク02_ハートブレイク・レイルロオド.txt.toml — 26/495 (5,3%)

- File: `ハチロク02_ハートブレイク・レイルロオド.txt.toml` — route 01_Hachiroku, 495 dòng script.
- Nội dung: Đầu máy số 9 + Railord Olivy chuyển từ Đường sắt Mikan sang; chuẩn bị tiệc chào mừng; Olivy đến nơi trong nước mắt, Munakata ký xong là rời đi ngay; Soutetsu tạm làm cộng sự hướng dẫn của Olivy.
- Nhân vật: monologue 171, 双鉄 105, ポーレット 56, ハチロク 38, れいな 23, 凪 23, オリヴィ 23, 日々姫 15, ふかみ 14, 真闇 10, 稀咲 9, 宗方 7, 赤井 1.
- Cơ sở tổng: 136 file / 6.200 dòng sai (đã tự kiểm chứng lại ROUTE-AUDIT.md — khớp với cơ sở được giao, không cần rebase).

## Kiểm tra cấu trúc

- TOML md5 `56cbf6691a5d618da886e8bffcf5b681`, BOM + CRLF, 495 dòng script, `[selections]` rỗng. Không có bản sao trùng của file này.
- CSV3: 1 set duy nhất (`translation_toml\01_Hachiroku`), 495 hàng, 0 trùng khóa, 0 VN trống. VN khớp phẳng TOML 494/495 (chỉ 2653 khác ở chỗ TOML-2 gộp `\n` thành khoảng trắng — theo quy ước, CSV3 là chuẩn). Comment `# JP:` trong TOML khớp CSV3 tuyệt đối 495/495.
- Thẻ `%l`: JP 106 lần xuất hiện (53 thẻ), VN 112 lần (56 thẻ) — VN tự thêm 3 thẻ (xem §tag, đã sửa cả 3).
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.
  - Nhiễm chéo: đối chiếu VN toàn dự án — 4 va chạm chéo file, tất cả đều là câu ngắn chung chung có JP tương đương (「Ngài Soutetsu?」= 双鉄様？; 「Cứ giao cho em á!」= まっかせろばーい/頼まれるばい; 「Em hiểu rồi ạ.」= わかりました; 「——Ngài Soutetsu.」= ――双鉄様) — 0 câu thoại đầy đủ nào bị đặt nhầm file.
  - VN trùng trong file: 4 nhóm, đều là cảm thán ngắn lặp hợp lệ (「Ừm.」2178/2241, 「Ưm.」2481/2138, 「A.」2126/2144/2208, 「A——」2140/2207).

## Phân loại (26)

- Đại từ 12, gasp 6, tag 3, thuật ngữ 3, SFX 1, sai nghĩa 1. Thoại 21/324 (6,5%), độc thoại 5/171 (2,9%).
- Theo nhân vật: ポーレット 7, 双鉄 6, monologue 5, オリヴィ 3, れいな 1, 凪 1, 稀咲 1, ハチロク 1, 赤井 1.

### §1. Đại từ (12)

Quy tắc đã sửa 20/11: Soutetsu "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi, "tôi" với Hachiroku/Mayami/Minokasa/Kisaki; Paulette 双鉄くん → "anh Soutetsu" (khóa B4); Soutetsu gọi Kisaki là "cô"; Kisaki gọi Soutetsu là "cậu"/tên trần (Common 14).

**Soutetsu tự xưng "anh" sai đối tượng (2):**

- **2052** (双鉄 → Hachiroku): JP 「蚊がとまっていた。あいにくと逃してしまったが」. Old: 「Có con muỗi đậu vào em. Tiếc là anh đánh trượt mất rồi.」 → Fix: 「Có con muỗi đậu vào em. Tiếc là tôi đánh trượt mất rồi.」. Bằng chứng người nghe: Soutetsu đập muỗi trên người Hachiroku; Hachiroku đáp ngay 2090 「Á!? Ngài Soutetsu?」.
- **2445** (双鉄 → Kisaki): JP 「そういうことか。であらば、預かっておこう」. Old: 「Ra là vậy. Nếu vậy thì anh sẽ giữ nó.」 → Fix: 「Ra là vậy. Nếu vậy thì tôi sẽ giữ nó.」. Bằng chứng: Kisaki vừa giải thích dùi đập đá ở 1967 (và đưa cho Soutetsu ở 2311/3333); TW 「那我就先收著了」.

**Soutetsu gọi Kisaki "em" (1):**

- **2197** (双鉄 → Kisaki): JP 「ああ、すまんが頼む」. Old: 「Ừ, xin lỗi nhưng nhờ em nhé.」 → Fix: 「Ừ, xin lỗi nhưng nhờ cô nhé.」. Bằng chứng: đáp lại Kisaki 2673 (Kisaki đề nghị hủy tiệc chào mừng). Tiền lệ: file khác đã sửa Soutetsu gọi Kisaki "em"→"cô" (key 2173).

**Kisaki gọi Soutetsu "anh" (1):**

- **2311** (稀咲 → Soutetsu): JP 「ポーレットが先方の好みをリサーチしてくれてたから助かったよ。っと――双鉄には、これ」 — JP dùng tên trần 双鉄, không có "anh". Old: 「…À này——cho anh cái này, Soutetsu.」 → Fix: 「…À này——cho cậu cái này, Soutetsu.」. Tiền lệ: file khác đã sửa 3 dòng Kisaki "anh Soutetsu"→"cậu"/tên trần (1664, 2459, 2617). Lưu ý: câu hỏi 33 dòng "anh Soutetsu" toàn tuyến Kisaki vẫn đang chờ Hieu chốt — dòng này trong file Hachiroku, sửa theo khóa Common 14.

**Paulette gọi Soutetsu "cậu" — khóa B4 (6 dòng):**

- **2699**: JP 「その間に双鉄くんには、連絡の手配を頼めますか？」. Old: 「…nhờ cậu Soutetsu liên lạc với mọi người được không?」 → Fix: 「…nhờ anh Soutetsu liên lạc với mọi người được không?」
- **2166**: JP 「双鉄く――右田機関士。そっち、おねがいできますか？」 (tự sửa giữa chừng trước mặt Munakata). Old: 「…Cháu hiểu rồi. Cậu Soutetsu—— / Người lái tàu Migita. Bên đó, nhờ cậu được không?」 → Fix: 「…Cháu hiểu rồi. Anh Soutetsu—— / Người lái tàu Migita. Bên đó, nhờ anh được không?」 (cả hai chỗ "cậu" đều là Soutetsu). Ghi chú: tiền lệ file 07 key 2551 giữ "Cậu Soutetsu……à không, anh Soutetsu" cho kiểu tự sửa くん→さん trên cùng một tên; ở đây Paulette sửa sang chức danh 右田機関士 nên không còn cặp đối lập Cậu→anh để giữ — dạng くん vẫn chịu khóa B4.
- **2440**: JP 「わたしもそうしますし、双鉄くんも」. Old: 「…và cả cậu Soutetsu nữa nhé.」 → Fix: 「…và cả anh Soutetsu nữa nhé.」
- **2384**: JP 「みんなの連絡が終わる頃までにはリストを作りますから」 — "cậu" là Soutetsu (người đi liên lạc; TW 「我會在你聯繫好之前列出清單」). Old: 「Em sẽ lập danh sách xong trước khi cậu liên lạc xong.」 → Fix: 「Em sẽ lập danh sách xong trước khi anh liên lạc xong.」
- **2246**: JP 「わかりました。よろしくおねがいします」 — "cậu" là Soutetsu (TW 「就拜託你處理了」). Old: 「Em hiểu rồi. Trăm sự nhờ cậu nhé.」 → Fix: 「Em hiểu rồi. Trăm sự nhờ anh nhé.」
- **3101** (monologue): JP 「身内以外の前で、僕を双鉄くんと呼びそうになるほど」. Old: 「…suýt nữa thì gọi tôi là cậu Soutetsu trước mặt người ngoài.」 → Fix: 「…suýt nữa thì gọi tôi là anh Soutetsu trước mặt người ngoài.」 (độc thoại tự thuật lại đúng dạng 双鉄くん nên phải đổi theo B4 cho nhất quán với 2166).

**Paulette tự xưng "Tôi" lạc lõng (1):**

- **2390** (ポーレット): JP 「物であっても、人であっても。みんなが気持ちよく働けるのが、安全の源だと思うから」. Old: 「Dù là vật hay là người. Tôi nghĩ việc mọi người có thể làm việc thoải mái chính là cội nguồn của sự an toàn mà.」 → Fix: 「Dù là vật hay là người. Em nghĩ việc mọi người có thể làm việc thoải mái chính là cội nguồn của sự an toàn mà.」. Đây là dòng duy nhất Paulette tự xưng "Tôi" trong file — 30+ chỗ còn lại đều "em" (kể cả câu trang trọng 2366 "Em nghĩ là vậy", 2344 "Em cũng có cảm giác").

**Độc thoại Soutetsu tự xưng "anh" (1):**

- **3176** (monologue): JP 「気持ちは嬉しい。が、明日も始発の乗務がある。そうそう長くは引き止められない。」 — người kể Soutetsu nghĩ về Reina sắp về ngủ. Old: 「Anh rất vui vì tấm lòng của em. Nhưng ngày mai em còn phải làm nhiệm vụ trên chuyến tàu đầu tiên nữa. Không thể giữ em lại lâu được.」 → Fix: 「Tôi rất vui vì tấm lòng của em. Nhưng ngày mai em còn phải làm nhiệm vụ trên chuyến tàu đầu tiên nữa. Không thể giữ em lại lâu được.」. Tiền lệ: ふかみh2 sửa 5 độc thoại "anh"→"tôi".

**Đã kiểm chứng đúng (không sửa):** mọi "anh" còn lại của Soutetsu đều đúng đối tượng — với Paulette (2083, 2680, 2337, 2200), Hibiki (2432, 2670, 2532, 2356, 2569), Nagi (2402), Fukami (2479 — Fukami hỏi ở 2081), Olivy (2317, Railord nhỏ tuổi, "anh" tự nhiên). Soutetsu không dùng "tôi" lần nào trong thoại (độc thoại dùng "tôi" xuyên suốt). "mình" trong độc thoại đều là sở hữu/phản thân ("một mình", "của mình") — đúng.

### §2. Gasp っ (6 — cả 6 từ sweep, áp nguyên văn)

Sweep có 6 mục cho file này, đã kiểm chứng từng mục với JP, nhận cả 6:

- **2103** (双鉄): JP 「っ！！？」 TW 「咦！！？」. Old: 「!!?」 → Fix: 「Ư!!?」
- **2139** (オリヴィ): JP 「っ！！！」 TW 「唔！！！」. Old: 「!!!」 → Fix: 「Ư!!!」
- **2461** (オリヴィ): JP 「みか――っ！？ / ああっ――」. Old: 「Mi——!? / A a——」 → Fix: 「Mi——Ư!? / A a——」 (chỉ thêm Ư ở vế đầu theo đúng sweep; vế sau "A a——" giữ nguyên — sweep cũng giữ).
- **2654** (凪): JP 「…逆に危なかとよ～っ！！」. Old: 「…thì lại càng nguy hiểm hơn á~!!」 → Fix: 「…thì lại càng nguy hiểm hơn á~Ư!!」
- **3261** (monologue): JP 「が、その表情ははっきり暗――っ！！？」. Old: 「…biểu cảm của em ấy lại tối sầm——!?」 → Fix: 「…biểu cảm của em ấy lại tối sầm——Ư!?」
- **78** (monologue): JP 「当然鳴るものと思っていたが――っ！？」. Old: 「…nó sẽ kêu chứ——!?」 → Fix: 「…nó sẽ kêu chứ——Ư!?」

Quét bổ sung: đã rà toàn bộ 203 dòng JP có っ + 24 ứng viên っ cuối dòng không có Ư — không còn gasp sót. Các trường hợp giữ nguyên đều có tiền lệ: あっ trần → "A!"/"A á!"/"A a——" (2146, 2147, 2151 — sweep giữ nguyên dạng này ở các file khác, vd. key 1195/2282/2031: chỉ thêm Ư cho っ cuối chuỗi, còn あっ → "A" được coi là đã diễn đạt); っ nhấn mạnh cuối từ nội dung (2475 よしっ→"Tốt!", 2498 くれっ, 2274 どこっ, 2072 もちろんっ, 2050 したっ) không phải gasp theo quy tắc đã khóa; SFX hành động (3455 ガっ→"Cạch") đã diễn đạt; ひゃっ (2088) thuộc họ ひあ/ひゃ ngẫu hứng.

### §3. Thẻ %l VN tự thêm (3)

Tiền lệ toàn dự án: gỡ thẻ %l do Gemini tự thêm (JP không có thẻ thì VN cũng không được có).

- **2388** (双鉄): JP 「噂に聞く重油[へいねん,1]並燃装置。」 — JP 0 thẻ. VN tự thêm thẻ và gloss sai. Old: 「Là \x%l重油並燃装置;#00ffc040;thiết bị đốt bỏ dầu nặng%l;#; trong lời đồn đó. / Có lẽ họ đã cố tình tạo ra khói đen bằng cái đó đấy.」 → Fix: 「Là thiết bị đốt kèm dầu nặng trong lời đồn đó. / Có lẽ họ đã cố tình tạo ra khói đen bằng cái đó đấy.」
- **2252** (ハチロク): JP chỉ có 1 thẻ (汽笛); VN thêm thẻ thứ 2 cho 重油並燃装置. Old: 「…liệu người ta có gắn \x%l重油並燃装置;#00ffc040;thiết bị đốt bỏ dầu nặng%l;#; cho đầu máy hơi nước thời Meiji không nhỉ?」 → Fix: 「…liệu người ta có gắn thiết bị đốt kèm dầu nặng cho đầu máy hơi nước thời Meiji không nhỉ?」 (thẻ 汽笛 giữ nguyên).
- **2578** (ポーレット): JP chỉ có 1 thẻ (補機 ở dòng 2); VN thêm thẻ ở dòng 1 (JP dòng 1 chỉ có ruby [ほき,1]). Old: 「…có gắn thêm \x%l補機;#00ffc040;đầu máy phụ%l;#; ở đuôi. / Qua khỏi Okoba thì sẽ tháo \x%l補機;#00ffc040;đầu máy phụ%l;#; ra cho quay về.」 → Fix: 「…có gắn thêm đầu máy phụ ở đuôi. / Qua khỏi Okoba thì sẽ tháo \x%l補機;#00ffc040;đầu máy phụ%l;#; ra cho quay về.」 (thẻ dòng 2 giữ nguyên).

Về gloss: 並燃 = đốt kèm/đốt song song (đốt dầu nặng cùng với than để tạo khói đen); TW 旁路燃燒裝置. "Đốt bỏ" (đốt để vứt đi) là sai nghĩa — thiết bị này đốt dầu làm nhiên liệu, không phải để tiêu hủy dầu.

### §4. Thuật ngữ (3)

- **2479** (双鉄): JP 「[めいこく,1]冥国で作られて輸入されてきた蒸機と聞く」 — furigana めいこく (không phải メリケン). TW nói 美國, VN theo TW: "được sản xuất ở Mỹ". JP thắng TW khi mâu thuẫn. Old: 「…nghe nói đó là đầu máy hơi nước được sản xuất ở Mỹ rồi nhập khẩu về.」 → Fix: 「…nghe nói đó là đầu máy hơi nước được sản xuất ở Minh Quốc rồi nhập khẩu về.」. Tiền lệ: file khác đã sửa 冥国 "nước Mỹ"→"Minh Quốc" (1741, 2766).
- **2509** (赤井) + **3428** (monologue): 激Ｖ — tiếng lóng nhiếp ảnh của Akai, JP mờ nghĩa; TW (pivot duy nhất đọc được) dịch 完全順光 ("thuận sáng hoàn toàn"). VN cũ "Góc chụp hoàn hảo" vừa sai nghĩa (góc chụp ≠ thuận sáng) vừa mâu thuẫn logic ở 3428: người kể nói "không hiểu げきぶい là gì" — nếu nó chỉ là cụm từ thuần Việt dễ hiểu thì không có gì để không hiểu; là thuật ngữ chuyên môn thì sự không hiểu mới hợp lý. Quyết theo ủy quyền của Hieu (21/11 01:51 — tự điều tra để quyết, có bằng chứng).
  - 2509: JP 「[ばくえん,1]爆煙！　[げきぶい,1]激Ｖ！　これは素晴らしい！」 TW 「爆煙！完全順光！實在是棒！」. Old: 「Khói mù mịt! Góc chụp hoàn hảo! Tuyệt vời quá!」 → Fix: 「Khói mù mịt! Thuận sáng hoàn toàn! Tuyệt vời quá!」
  - 3428: JP 「げきぶい、が何かはわからんが、なるほど、撮影向けのサービスか。」 TW 「雖然不知道完全順光具體是什麼意思，看來這濃煙是針對攝影安排的。」. Old: 「Dù không hiểu góc chụp hoàn hảo là gì, nhưng ra là vậy, là dịch vụ dành cho chụp ảnh à.」 → Fix: 「Dù không hiểu thuận sáng hoàn toàn là gì, nhưng ra là vậy, là dịch vụ dành cho chụp ảnh à.」

### §6. Sai nghĩa (1)

- **2050** (オリヴィ): JP 「元っ！　みかん鉄道っ――レイル、ロオド――オリヴィ――[きゅうごう,1]Ⅸ号機関車、と――着任、しま、したっ」 — Olivy tự giới thiệu trang trọng sau khi trấn tĩnh (2916 dứt khoát lau nước mắt, đứng dậy). TW 「前！」 đọc 元 như từ hô kiểu quân đội ("phía trước"), không phải tên. VN cũ "Nguyên!" chỉ là phiên âm Hán-Việt của 元 — đọc như tên riêng "Nguyên", gây hiểu lầm (tên cô bé là Olivy). Quyết theo ủy quyền của Hieu (21/11 01:51): đây là tiếng hô mở đầu bản báo cáo nhậm chức → "Nghiêm!" (lệnh "chú ý" trong quân đội, hợp với tư thế đứng nghiêm của Railord). Old: 「Nguyên! Đường sắt Mikan——Rail, lord——Olivy——cùng Đầu máy số 9——đã, đến, nhận nhiệm vụ!」 → Fix: 「Nghiêm! Đường sắt Mikan——Rail, lord——Olivy——cùng Đầu máy số 9——đã, đến, nhận nhiệm vụ!」 (Các っ khác trong dòng: みかん鉄道っ, したっ — nhấn mạnh cuối từ nội dung, không phải gasp.)

### §5. SFX fa/fu (1)

- **2170** (れいな): JP 「ふえぇ……」 (Reina sụt sùi sắp khóc). Old: 「Hu ee……」 → Fix: 「Phuêê……」. Quy tắc đã chốt: ふぇ/ふえ → "phuê" (tiền lệ lr-mikuro 33 dòng fa/fu; file khác ふえっ→"Phuê"); ふえぇ dài 2 mora ê nên "Phuêê". "Hu" làm mất hẳn âm f.

## Giữ nguyên (ghi chú phán đoán)

- **2038** ふぁ～あ → "oáp~": đây là tiếng ngáp (Reina ngáp to, 2028 "Reina vừa nói vừa ngáp to tướng"), không phải tiếng rên — quy tắc fa/fu không áp dụng.
- **2172** ふわぁああああん → "Oaaaaaa": tiếng khóc òa; 6 âm a đúng số lượng JP (わぁああああ); không có quy tắc chốt cho ふわ — giữ.
- **2509/3428** 激Ｖ — ĐÃ SỬA (xem §4): theo TW 完全順光 → "Thuận sáng hoàn toàn" (quyết theo ủy quyền Hieu 21/11 01:51).
- **2271** (ポーレット): JP cụt câu 「正面玄関から出て、エアクラタクシーで」 — VN hoàn thiện thành "đã đi ra cửa trước, rồi lên taxi Aircra". Giữ: nội dung đã hàm ý đầy đủ trong で + ngữ cảnh, chỉ mất dấu ngập ngừng (đã có "ờm——" cho その――).
- **2056** (稀咲): tự sửa オリヴィちゃ―― → オリヴィくん, VN "bé Olivy——à không, cô Olivy" — giữ (diễn đạt được sự chuyển từ thân mật sang trang trọng).
- **2166** "Cháu hiểu rồi" — Paulette tự xưng "cháu" với Munakata, nhất quán với "chú Munakata" trong file — giữ.
- **3221** （そっ） → "（Khẽ）" — giữ (tiếng lại gần khẽ khàng; TW cũng diễn thành lời kể).
- **"Ohito" 29 dòng → đợt thống nhất** (không tính sai ở đây, theo tiền lệ file ふかみh2): 御一夜 27 dòng + 御鉄 2 dòng (2647, 2327) đều dịch "Đường sắt Ohito". Đợt thống nhất sẽ đổi → "Ohitoyo".
- **[characters] 2823/3034 = "Olive"** — khác chính tả đã chốt "Olivy". Đây là mapping tên hiển thị trong TOML, không phải dòng script nên không tính vào 23; **cờ cho Hieu/parent** xem có cần đổi mapping này thành "Olivy" không.
- Các thuật ngữ đã đúng: 小畑→Okoba (3 dòng), まいてつ→"chủ tàu" (3184, 2376), 宮司→"đền chủ" (3313), エアクラ→Aircra (2271), Railord (1 l) xuyên suốt. Không có dòng 帝鉄/帝大/日ノ本/乗務鞄/運転鞄/乗員/湯医 trong file này.

## Kiểm chứng

- JSON 26 mục dạng chuẩn (list of dicts, khóa chuỗi: key, jp, tw, old_vn, fix, kind, character); khối TOML 26 khóa, parse OK, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 26/26; mỗi fix chỉ khác old VN ở đúng chỗ sửa (tỉ lệ diff 0,79–1,00; 2170 là thay toàn bộ SFX ngắn; 2388 là gỡ thẻ + sửa gloss; 2509/3428 là thay thuật ngữ).
- Lượt soát 2 (đọc lại toàn bộ 26 fix đối chiếu JP): **26/26 tái kiểm chứng, 0 bỏ, 0 sửa.**
- Romaji fallback cho tiếng rên (Hieu duyệt 21/11 ~01:56) đã được cân nhắc: "Phuêê" ở 2170 không nghe ngượng nên giữ bản Việt theo đúng điều kiện của quy tắc; các tiếng rên/khóc còn lại trong file (2171–2174, 1544, 2088, 2141) đều là bản Việt tự nhiên, không cần romaji.
- Sweep: 6/6 mục áp nguyên văn sau kiểm chứng; quét bổ sung toàn bộ 203 dòng JP có っ — 0 gasp sót.

## Khối TOML (đã kiểm chứng parse)

```toml
[script]
78 = "\\x%l汽笛;#00ffc040;Còi hơi nước%l;#; không kêu.\\nTôi cứ tưởng đương nhiên là nó sẽ kêu chứ——Ư!?"
2050 = "「Nghiêm! Đường sắt Mikan——Rail, lord——Olivy——cùng Đầu máy số 9——đã, đến, nhận nhiệm vụ!」"
2052 = "「Có con muỗi đậu vào em. Tiếc là tôi đánh trượt mất rồi.」"
2103 = "「Ư!!?」"
2139 = "「Ư!!!」"
2166 = "「Dạ? ——A, vâng. Cháu hiểu rồi. Anh Soutetsu——\\n\\x%l機関士;#00ffc040;Người lái tàu%l;#; Migita. Bên đó, nhờ anh được không?」"
2170 = "「Phuêê……」"
2197 = "「Ừ, xin lỗi nhưng nhờ cô nhé.」"
2246 = "「Em hiểu rồi. Trăm sự nhờ anh nhé.」"
2252 = "「Nếu là phúc lợi cho fan, thì việc không kéo \\x%l汽笛;#00ffc040;còi hơi nước%l;#; là……\\nHơn nữa, liệu người ta có gắn thiết bị đốt kèm dầu nặng cho đầu máy hơi nước thời Meiji không nhỉ?」"
2311 = "「Nhờ Paulette đã tìm hiểu trước sở thích của bên đó\\nnên cũng đỡ lắm. À này——cho cậu cái này, Soutetsu.」"
2384 = "「Em sẽ lập danh sách xong trước khi anh liên lạc xong.\\nNgay khi xác định được ai có thể đến, chúng ta sẽ phân bổ nhân sự.」"
2388 = "Là thiết bị đốt kèm dầu nặng trong lời đồn đó.\\nCó lẽ họ đã cố tình tạo ra khói đen bằng cái đó đấy."
2390 = "「Dù là vật hay là người.\\nEm nghĩ việc mọi người có thể làm việc thoải mái chính là cội nguồn của sự an toàn mà.」"
2440 = "「\"Như những người chuyên nghiệp làm việc cùng nhau\" đúng không. Vâng.\\nVậy là OK rồi. Em cũng sẽ làm như vậy, và cả anh Soutetsu nữa nhé.」"
2445 = "「Ra là vậy.\\nNếu vậy thì tôi sẽ giữ nó.」"
2461 = "「Mi——Ư!?\\nA a——」"
2479 = "「Đúng vậy. Anh nhớ không lầm thì, khoảng cuối thời \\x%l明智;#00ffc040;Meiji%l;#;,\\nnghe nói đó là đầu máy hơi nước được sản xuất ở Minh Quốc rồi nhập khẩu về.」"
2509 = "「Khói mù mịt! Thuận sáng hoàn toàn! Tuyệt vời quá!」"
2578 = "「Em nghe nói là tự chạy, có gắn thêm đầu máy phụ ở đuôi.\\nQua khỏi Okoba thì sẽ tháo \\x%l補機;#00ffc040;đầu máy phụ%l;#; ra cho quay về.」"
2654 = "「Đó! Giờ đâu phải lúc nói chuyện thong thả đâu!\\nCứ vậy rồi lỡ luống cuống thêm thì lại càng nguy hiểm hơn á~Ư!!」"
2699 = "「Bây giờ đây! Em sẽ làm ngay bây giờ.\\nTrong lúc đó, nhờ anh Soutetsu liên lạc với mọi người được không?」"
3101 = "Đang bối rối, ngay cả Paulette cũng vậy.\\nĐến mức suýt nữa thì gọi tôi là anh Soutetsu trước mặt người ngoài."
3176 = "Tôi rất vui vì tấm lòng của em. Nhưng ngày mai em còn phải làm nhiệm vụ trên chuyến tàu đầu tiên nữa.\\nKhông thể giữ em lại lâu được."
3261 = "Paulette chạy chậm lại chỗ tôi.\\nNhưng, biểu cảm của em ấy lại tối sầm——Ư!?"
3428 = "Dù không hiểu thuận sáng hoàn toàn là gì,\\nnhưng ra là vậy, là dịch vụ dành cho chụp ảnh à."
```

## Kết bài

File ハチロク02_ハートブレイク・レイルロオド.txt.toml: 495 dòng đã đọc hết, **26 dòng sai (5,3%)** — đại từ 12 (chủ yếu khóa B4 Paulette "cậu Soutetsu"→"anh Soutetsu" 6 dòng + Soutetsu "anh" sai đối tượng với Hachiroku/Kisaki + "em" với Kisaki), gasp 6 (sweep), tag 3 (VN tự thêm %l), thuật ngữ 3 (冥国→Minh Quốc + 激Ｖ→"Thuận sáng hoàn toàn" 2 dòng), SFX 1 (ふえぇ→"Phuêê"), sai nghĩa 1 (元っ "Nguyên!"→"Nghiêm!"). Không lệch vị trí, không xoay chuỗi, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. 2 quyết định theo ủy quyền của Hieu (21/11 01:51 — tự điều tra để quyết): 2050 元っ và 2509/3428 激Ｖ, đã ghi đầy đủ bằng chứng JP+TW. Không còn dòng nào không chắc cần chờ Hieu (trừ B19 đã park toàn dự án). 29 dòng "Ohito" và các mục fa/fu dạng cũ để đợt thống nhất; mapping [characters] "Olive" vs "Olivy" cần Hieu/parent xem lại. Lượt soát 2: 26/26, 0 bỏ, 0 sửa. JSON + khối TOML đã kiểm chứng parse, 0 sai lệch.
