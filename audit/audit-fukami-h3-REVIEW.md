# Audit — ふかみh3_夏休みの最後の日の、前の日 (07_Nagi_Fukami) — "Ngày trước ngày cuối cùng của kỳ nghỉ hè"

- File: `ふかみh3_夏休みの最後の日の、前の日.txt.toml` — route 07_Nagi_Fukami, **649 dòng script** (queue ghi 1298 dòng vì CSV3 có 2 set × 649 — xem §5; số dòng thật là 649), 4 strong candidates.
- Nội dung: buổi hẹn hò của Soutetsu–Fukami dọc tuyến đường sắt vào ngày trước ngày cuối kỳ nghỉ hè: bài học về đá ba-lát/nhổ cỏ/bảo trì đường ray, nhà ga bỏ hoang với bức vẽ ô chung tình của cặp đôi bí mật (Kenji & Manami), cơn mưa rào bất chợt và trú mưa, gốc cây mang kỷ niệm của Nagi, cảnh H, và chủ đề "tô điểm thêm kỷ niệm" (重ねる). Kết thúc hẹn về ga Ohitoyo Onsen trước 17:10.
- Phương pháp: đọc hết 649/649 dòng theo JP + TW (CSV3, set tốt 11_Other — set 07_Nagi_Fukami là stale, xem §5), đối chiếu TOML-2. Không lấy mẫu. Key không theo thứ tự truyện (cảnh hẹn hò / cảnh H / độc thoại xen kẽ theo key) — xác định người nói/người nghe theo nội dung và dòng kề.

## §1. Kết quả

**28 dòng sai / 649 (4,3%)** — file khá sạch; lỗi tập trung ở SFX fa/fu hệ thống (20 dòng: dịch giả dùng "phù" cho mọi ふぁ/ふあ/ぷあ, trái quy tắc đã chốt 19/11).

- Lệch vị trí (misaligned) **0**, chuỗi xoay (rotation) **0**, nhiễm chéo file khác **0**, dòng mồ côi (orphan) **0**, chưa dịch **0**, trùng khóa **0**.
- Phân loại (28): gasp 4 (1664, 1677, 2449, 2728), fa/fu 20 (2278, 2287, 2301, 2302, 2338, 2345, 2346, 2351, 2352, 2358, 2359, 2362, 2371, 2385, 2388, 2394, 2402, 2430, 2577, 2767), sai nghĩa 3 (2130, 3300, 3887), bịa thêm nghĩa (fabrication) 1 (2292).
- `[selections]` rỗng (0 mục). Không có thẻ `%l` sai định dạng nào (25 mở / 25 đóng, mọi thuật ngữ %l đều có trong dòng JP tương ứng).
- Không có bản sao file này (md5 duy nhất trong toàn bộ TOML-2; 1 copy, không áp fix 2 nơi).

## §2. Chi tiết từng dòng sai

### Gasp — mất tiếng thở/っ (4 dòng)

- **1664** (ふかみ). JP: 「…………っ」 — gasp cả dòng. Sweep `lost-gasp-trailing` đã liệt kê đúng. VN cũ: 「…………」 → **「…………Ư」**.
- **1677** (双鉄). JP: 「……っ」; TW: 「……啊」 (có tiếng "a"). Sweep BỎ SÓT dòng này (không có trong 14 mục sweep của file). VN cũ: 「……」 → **「……Ư」**.
- **2449** (双鉄). JP: 「っ！！？」 — gasp cả dòng; TW: 「嗯？！」 (có tiếng "ừm"). Sweep BỎ SÓT. VN cũ: 「!!?」 (không còn âm thanh nào) → **「Ư!!?」**.
- **2728** (双鉄). JP: 「なるほど、道理だ。\nしかし、しあわせと言われても――っ！」; TW: 「……啊！」 (có tiếng "a"). Sweep `lost-gasp-trailing` đã liệt kê đúng. VN cũ: 「Ra vậy, có lý.\nNhưng, nói là hạnh phúc thì——!」 → **「Ra vậy, có lý.\nNhưng, nói là hạnh phúc thì——Ư!」** (giữ nguyên ngắt dòng literal `\n` của VN cũ; fix của sweep dẹp `\n` thành khoảng trắng nên không áp nguyên dạng đó).

### SFX fa/fu — ふぁ/ふあ/ぷあ → "phù" thay vì "phà"/"phùa" (20 dòng, quy tắc đã chốt 19/11)

Dịch giả dùng "phù" một cách hệ thống cho mọi ふぁ/ふあ/ぷあ trong file. Theo quy tắc đã chốt: ふぁ → "phà", ふあ/ぷあ → "phùa". Mỗi fix chỉ đổi đúng âm đó; các "phù" đúng (cho ふっ/ふ) được giữ nguyên (2301, 2359, 2402, 2767 mỗi dòng có cả hai loại — chỉ sửa đúng chỗ ふぁ/ふあ).

- **2278** (ふかみ). JP: 「ひゅあっ！　あっ――ふあっ！　これ――しゅご、…」. VN cũ: 「Hya! A—— **phù!** Cái này—— tuyệt,…」 → **「Hya! A—— phùa! Cái này—— tuyệt,…」**
- **2287** (ふかみ). JP: 「ふきゅうううんんっ！！　ふあっ――おく――…」. VN cũ: 「Fukyuuuuun!! **Phù**—— bên trong——…」 → **「Fukyuuuuun!! Phùa—— bên trong——…」**
- **2301** (ふかみ). JP: 「ふっ――んっ――じんじん、ってして――ふぁ――…」. VN cũ: 「Phù—— ưm—— tê tê, rần rần—— **phù**—— Hà—— phù, ư——…」 → **「Phù—— ưm—— tê tê, rần rần—— phà—— Hà—— phù, ư——…」** (chỉ đổi "phù" thứ hai = ふぁ; "Phù" đầu = ふっ và "phù" sau "Hà" = ふ đều giữ).
- **2302** (ふかみ). JP: 「んくッ――んくっ――んくっ――ぷあぁ」. VN cũ: 「Ực—— ực—— ực—— **phù**」 → **「Ực—— ực—— ực—— phùa」**
- **2338** (ふかみ). JP: 「ぁっ……ふあっ――んっ――ちゅっ――…」. VN cũ: 「A…… **phù**—— ưm—— chụt——…」 → **「A…… phùa—— ưm—— chụt——…」**
- **2345** (ふかみ). JP: 「ふぁ……は……ぁっ――」. VN cũ: 「**Phù**…… hà…… a——」 → **「Phà…… hà…… a——」**
- **2346** (ふかみ). JP: 「ふあっ――あっ――はっ――はあっ――…」. VN cũ: 「**Phù**—— a—— hà—— hà——…」 → **「Phùa—— a—— hà—— hà——…」**
- **2351** (ふかみ). JP: 「ふあっ――あっ――んっ――ちゅ――ぷあっ！…」. VN cũ: 「**Phù**—— a—— ưm—— chụt—— **phù!**…」 → **「Phùa—— a—— ưm—— chụt—— phùa!…」** (cả hai âm).
- **2352** (ふかみ). JP: 「ふあっ――あっ――おっき――…」. VN cũ: 「**Phù**—— a—— to—— to, quá——…」 → **「Phùa—— a—— to—— to, quá——…」** (っ cuối dòng 「とこっ――っ」 là ngắt câu nhấn mạnh, không thêm Ư — xem §4).
- **2358** (ふかみ). JP: 「ふぁっ――あ――おっぱい、ちく、びっ――んっ、もっと――もっと、つよくても、へい、き――ふぁっ」. VN cũ: 「**Phù**—— a—— ngực, núm, vú—— ưm, Mạnh—— mạnh hơn, chút nữa, cũng không, sao—— **phù**」 → **「Phà—— a—— ngực, núm, vú—— ưm, Mạnh—— mạnh hơn, chút nữa, cũng không, sao—— phà」** (cả hai âm).
- **2359** (ふかみ). JP: 「はっ――あっ――中ッ――っっ――あっ、ふあっ、指っ――ん、っ――うっ――こすって――ふ、あ」. VN cũ: 「Hà—— a—— bên trong—— a, **phù**, Ngón tay—— ưm, ư—— ư—— cọ xát—— **phù, a**」 → **「Hà—— a—— bên trong—— a, phùa, Ngón tay—— ưm, ư—— ư—— cọ xát—— phà, a」** (cả hai âm).
- **2362** (ふかみ). JP: 「ふあっ――あっ――ひ、ぅっ――おまんこ、の――…」. VN cũ: 「**Phù**—— a—— hi, ư—— phần trên——…」 → **「Phùa—— a—— hi, ư—— phần trên——…」**
- **2371** (ふかみ). JP: 「あ……ここ、です――ふ……ァッ――…」. VN cũ: 「A…… chỗ này, ạ—— **phù**…… a——…」 → **「A…… chỗ này, ạ—— phà…… a——…」**
- **2385** (ふかみ). JP: 「っ！　――ぷあっ」. VN cũ: 「Ư! ——**Phù**」 → **「Ư! ——Phùa」** ("Ư!" cho っ！ đã đúng, giữ nguyên).
- **2388** (ふかみ). JP: 「ふあっ！　あっ――あついの――…」. VN cũ: 「**Phù!** A—— nóng quá——…」 → **「Phùa! A—— nóng quá——…」**
- **2394** (ふかみ). JP: 「はっ！　しゅきっ――うれしっ――いっ――ふあっ、…」. VN cũ: 「Hà! Thích—— sướng—— quá—— **phù**,…」 → **「Hà! Thích—— sướng—— quá—— phùa,…」**
- **2402** (ふかみ). JP: 「はぁあああっっ、ふっ！　あっ！　しきゅうっ！　ほしっいっ――ふあっ――…」. VN cũ: 「Hà a a a, phù! A! Tử cung! Muốn—— **phù**—— bị cộc—— gõ cửa」 → **「Hà a a a, phù! A! Tử cung! Muốn—— phùa—— bị cộc—— gõ cửa」** (chỉ đổi "phù" thứ hai = ふあっ; "phù!" đầu = ふっ, giữ).
- **2430** (ふかみ). JP: 「んっ――ふあっ――」. VN cũ: 「Ưm—— **phù**——」 → **「Ưm—— phùa——」**
- **2577** (ふかみ). JP: 「わかる、です。――んっ――双鉄、おにいさん、の――かた、ち――ふあっ――…」. VN cũ: 「…Của, anh, Soutetsu—— **phù**—— của, chim——」 → **「…Của, anh, Soutetsu—— phùa—— của, chim——」**
- **2767** (ふかみ). JP: 「ふく――とか――そんなの――どうでも、いい――ふあっ――んっ――ふっ――はうっ」. VN cũ: 「Quần áo—— hay gì đó—— sao cũng, được—— **phù**—— ưm—— phù—— a ư」 → **「Quần áo—— hay gì đó—— sao cũng, được—— phùa—— ưm—— phù—— a ư」** (chỉ đổi "phù" đầu = ふあっ; "phù" sau "ưm" = ふっ, giữ).

### Sai nghĩa (3 dòng)

- **2130** (双鉄). JP: 「今日は、なんだ？」 ("Hôm nay là cái gì thế?"); TW: 「一定要什麼？」 (TW cũng lệch). VN cũ: 「Hôm nay **phải làm sao?**」 (thêm "phải làm sao" không có trong JP) → **「Hôm nay là sao?」**
- **3300** (monologue). JP: 「健気だ、かわいい、キスしたい――」 — 健気 = can đảm, đáng khâm phục, kiên cường (không phải "đáng yêu"); TW cũng diễn lỏng thành 青春/可愛 nhưng JP thắng TW. VN cũ: 「**Đáng yêu** quá, dễ thương quá, muốn hôn quá——…」 → **「Can đảm quá, dễ thương quá, muốn hôn quá——…」** (xem §7 — Hieu có thể chọn cách diễn khác cho 健気).
- **3887** (monologue). JP: 「（白い……な、本当にすらりとしている）」; TW: 「（好白啊……而且很苗條）」 — cả JP lẫn TW đều KHÔNG nói đến chân. VN cũ thêm danh từ không có căn cứ: 「（Trắng quá…… mà, **chân em** thon thả thật đấy）」 → **「（Trắng quá…… mà, thon thả thật đấy）」**

### Bịa thêm nghĩa — fabrication (1 dòng)

- **2292** (ふかみ). JP: 「やっ、なにこれっ！？　こんなにひどいとかっ」 — KHÔNG có chữ 雨 nào; TW: 「呀，怎麼回事？居然這麼大」 (TW xác nhận đang nói về độ lớn, trong cảnh H — các key kề 2290/2293/2295 đều là tiếng rên). VN cũ bịa ra mưa từ bối cảnh (trong file có cảnh mưa rào): 「Á, gì thế này!? **Sao lại mưa to thế này chứ**」 → **「Á, gì thế này!? Sao lại to thế này chứ」**. Đây KHÔNG phải dòng lệch vị trí: JP này chỉ xuất hiện 1 lần trong set tốt; bản VN mưa không thuộc về bất kỳ dòng JP nào khác trong toàn dự án (tìm toàn CSV3: chỉ 2 dòng JP có ひどい+雨 là ハチロク05 2090 và ニイロク02 1551, cả hai đều đã có VN đúng riêng); set stale cũng ghép đúng JP này với đúng VN mưa đó ở key khác — chứng tỏ lỗi nằm trong bản dịch gốc (Gemini đọc 「こんなにひどいと」 trong bối cảnh mưa mà suy ra "mưa to"), không phải do xáo hàng.

## §3. Thuật ngữ dạng cũ — chờ đợt thống nhất, KHÔNG tính sai

- "Đường sắt Ohitera" (御一夜 → "Ohitoyo" đã chốt): **4 dòng** — 2442, 2506, 2638 ("ga Ohitera Onsen"), 2867 ("quay về Ohitera").
- 日ノ本 "Hinomoto" (3178): **1 dòng** — chờ Hieu chốt "Hinomoto" vs "Hinamoto" (theo toàn dự án).

## §4. Các dòng đã kiểm tra kỹ và GIỮ NGUYÊN (không sửa)

- **っ cuối câu nhấn mạnh — KHÔNG phải gasp (tiền lệ 1474): 2202, 2596, 3208, 3435, 3476.** 2202 「それほど慌てて飲まずとも――っ」 (không có ！, TW không có tiếng thở) — giữ. 2596 「そしたらきっと、いつか――っ！」 (TW không có tiếng thở, sweep không liệt kê) — giữ. 3208 monologue 「ふかみの膣の、最奥のその向こうまでをも――っ！」 (độc thoại, TW không có tiếng thở) — giữ. 3435 monologue 「…もっとじっくり――っ！？」 — giữ. 3476 「食い込ませっ――」 (ngắt câu) — giữ. Phân biệt với 2728 (đã sửa): 2728 có TW 「……啊！」 và sweep liệt kê; các dòng trên không có bằng chứng TW nào.
- **Sweep 10 mục `needs-file-audit` đã xử lý:** 2292 → sửa (xem §2, không phải lệch dòng); 2519, 2531, 2629, 2829, 2869, 3127, 3390, 3619, 3805 → GIỮ (VN khớp JP/TW; sweep chỉ gắn cờ do lệch số đoạn, không phải lỗi dịch). Riêng 2519 「一雨くるな」 → "Sắp mưa to rồi": 一雨 là cơn mưa rào, "to" chỉ là nhấn mạnh trong bối cảnh mưa rào buổi chiều — giữ.
- **Sweep 2 mục `already-rendered`:** 2281, 3645 — VN đã diễn gasp bằng cách khác (Ưm/Ư) — giữ.
- **SFX phiên âm giữ nguyên (giữ sát tiếng Nhật, theo Hieu 22:19):** 2286 「きゃうっ！！」 → "Kyau!!", 2289 「きゅふああああああああああああああんんっ！！！」 → "Kyufuaaaaaaaaaaaaaaan!!!", 2332 「んきゅううっっ！！！」 → "Nkyuuu!!!". Quy tắc "never romanisation" áp cho việc diễn ふぁ thành "fa", không áp cho cả một tiếng kêu nguyên vẹn; sửa thành "Kyuphùa…" còn tệ hơn.
- **1662** 「…………」 VN==TW — KHÔNG phải chưa dịch, chỉ là dấu lặng; đúng.
- **2632** 「そうだな。いくなら、一緒がいいな」 → "Nếu lên đỉnh, thì cùng nhau sẽ tốt hơn" — TW xác nhận cách đọc tình dục (要舒服還是一起舒服好); giữ.
- **2792** 「どうしょう？」 = 道床 (đường nền) đọc hiragana — TW 「路基？」 xác nhận; VN "Mặt nền đường sắt?" đúng; giữ.
- **3514** 「…なお、かたい。」 → "nhưng vẫn còn rất khít" — chủ ngữ mơ hồ trong JP (TW 僵硬 cũng mơ hồ tương tự); cách đọc "khít" hợp ngữ cảnh; giữ.
- **3879/3880** （びゅううっ） và （ひゅううっ） cùng → （Vù vù） — cả hai đều là tiếng gió, một onomatopoeia Việt chung là chấp nhận được; giữ.
- **3917/3921** （きゅうっ！） và （きゅううううううっ） cùng → （Siết chặt） — chênh lệch độ dài không diễn được bằng tiếng Việt; giữ.
- **3135** 「やだもう」 → "thật tình" — tiếng lẩm bẩm bực dọc, chấp nhận được; giữ.
- **2426** 「はぅ……」 → "Hưm……" vs 2427 「はぅぅ」 → "A ư" — hai cách diễn tiếng thở dài không nhất quán nhưng đều hợp lý; giữ.
- **2139** 「ワン、ピース、を――よご、さぬっ――よう」 → "Để—— không làm, bẩn—— váy, liền" — giữ đúng kiểu ngắt quãng của JP (よごさぬよう = để khỏi làm bẩn); giữ.
- **2144** chơi chữ 水色→青→碧 — bản dịch thơ ("Màu nước biển hòa vào màu xanh lam…") giữ được ý; giữ.
- **Ruby bỏ theo quy tắc strip-ruby:** [みずみち,1]水路 (2271, 2773), [いのち,1]生命 (2572) — VN diễn nghĩa, bỏ ruby; giữ.
- **Xưng hô — kiểm chứng toàn file, 0 lỗi:** Soutetsu đối thoại 0× "tôi" (toàn "anh" với Fukami — đúng quy tắc); độc thoại Soutetsu 0× "anh" (toàn "tôi" — đúng); Fukami tự xưng "em" với Soutetsu; "chị Hibiki" (2417) đúng (Hibiki lớn tuổi hơn); Nagi không có lời thoại trong file này (chỉ được nhắc đến), nên cặp Nagi→Fukami "bé"/Fukami→Nagi "cậu" không có dòng nào để kiểm tra ở đây.
- **VN trùng nhau trong file (7 cặp):** [1662, 1664] 「…………」 (1664 đã sửa thành 「…………Ư」 nên cặp này hết trùng); [2321, 2451] 「À」; [2333, 2443] 「Hửm?」; [2383, 2427] 「A ư」; [2473, 2608] 「V, vâng」; [3879, 3880] （Vù vù）; [3917, 3921] （Siết chặt） — đều là câu cảm thán/SFX lặp lại hợp lệ, JP tương ứng cũng lặp/khớp nghĩa; không phải chuỗi xoay.
- **2248** 「おじいちゃんたち」 → "các ông" — giữ (chỉ chung "các ông", không phải câu hỏi ông nội/ông ngoại về Seki).

## §5. Kiểm chứng cơ học

- CSV3: 1298 dòng cho file này = **2 set × 649**. Set tốt `translation_toml\11_Other\...` khớp TOML tuyệt đối sau chuẩn hóa `\n`→khoảng trắng (**0/649 lệch**); set `translation_toml\07_Nagi_Fukami\...` (thư mục "home") là STALE — **642/649 VN lệch** với TOML và JP bị xoay so với key (vd. JP của stale-2695 = JP của good-3631; JP của stale-3631 = JP của good-2695). Audit này chỉ dùng set tốt. Đây là file dual-set thứ 11+ của dự án (quy tắc "home-folder set là stale" đã đúng ở đây).
- Set tốt: 649 khóa duy nhất, 0 khóa trùng, 0 VN trống, 0 JP trống, 0 TW trống.
- TOML-2: 649 khóa `[script]`, md5 `468ff9287da913deb380278b68d048f8`, không có file trùng nội dung trong toàn bộ TOML-2 (1 copy duy nhất). `[selections]` rỗng.
- JSON: 28 mục, khóa chuỗi, dạng chuẩn list-of-dicts (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 (set tốt) tuyệt đối 28/28.
- Khối TOML: parse được bằng tomllib, 28 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3).
- Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (log build: 1664/1677/2449/2728 thêm Ư; 2130 bỏ "phải làm sao"→"là sao"; 2292 bỏ "mưa "; 3300 "Đáng yêu"→"Can đảm"; 3887 bỏ " chân em"; 20 dòng fa/fu chỉ đổi ù→à hoặc thêm 'a' — phù→phà/phùa).
- Sweep: 14 mục cho file — 2 áp nguyên đã kiểm chứng (1664, 2728), 2 already-rendered giữ (2281, 3645), 10 needs-file-audit đã xử lý (1 sửa 2292, 9 giữ). Sweep BỎ SÓT 2 gasp (1677, 2449) — đã bắt được trong lần đọc toàn bộ.
- Lượt soát 2: **28/28 tái kiểm chứng, 0 bỏ, 0 sửa** — đọc lại toàn bộ 28 fix đối chiếu JP (bảng soát 2 in trong quá trình build; mọi fix đều giữ nguyên sau lượt soát).

## §6. Khối TOML (đã kiểm chứng parse)

```toml
"1664" = "「…………Ư」"
"1677" = "「……Ư」"
"2130" = "「Hôm nay là sao?」"
"2278" = "「Hya! A—— phùa! Cái này—— tuyệt,\\nƯm ư ư—— bên trong—— từ từ—— bị, đẩy, vào」"
"2287" = "「Fukyuuuuun!! Phùa—— bên trong——\\nSâu, nhất—— tử cung—— bị, chạm vào, rồi——」"
"2292" = "「Á, gì thế này!? Sao lại to thế này chứ」"
"2301" = "「Phù—— ưm—— tê tê, rần rần—— phà——\\nHà—— phù, ư—— ưm…… bứt, rứt, quá」"
"2302" = "「Ực—— ực—— ực—— phùa」"
"2338" = "「A…… phùa—— ưm—— chụt—— chụt,\\nchụt—— chụt—— chụt—— chụt」"
"2345" = "「Phà…… hà…… a——」"
"2346" = "「Phùa—— a—— hà—— hà—— ngập tràn,\\nBụng—— ngập tràn—— óc ách—— óc ách」"
"2351" = "「Phùa—— a—— ưm—— chụt—— phùa!\\nA—— em muốn, ạ—— toàn bộ, anh, Soutetsu」"
"2352" = "「Phùa—— a—— to—— to, quá——\\nChim—— chỗ đó—— chỗ, thô to——」"
"2358" = "「Phà—— a—— ngực, núm, vú—— ưm,\\nMạnh—— mạnh hơn, chút nữa, cũng không, sao—— phà」"
"2359" = "「Hà—— a—— bên trong—— a, phùa,\\nNgón tay—— ưm, ư—— ư—— cọ xát—— phà, a」"
"2362" = "「Phùa—— a—— hi, ư—— phần trên——\\nCủa, cô bé—— ưm—— giống như, đang cào—— vậy——」"
"2371" = "「A…… chỗ này, ạ—— phà…… a——\\nChim, của—— anh, Soutetsu」"
"2385" = "「Ư! ——Phùa」"
"2388" = "「Phùa! A—— nóng quá—— bên trong—— bên trong!\\nBên trong—— cô bé—— phụt ra, đánh vào」"
"2394" = "「Hà! Thích—— sướng—— quá—— phùa,\\nCứ thế này—— cứ, thế này—— em—— cứ thế này」"
"2402" = "「Hà a a a, phù! A! Tử cung!\\nMuốn—— phùa—— bị cộc—— gõ cửa」"
"2430" = "「Ưm—— phùa——」"
"2449" = "「Ư!!?」"
"2577" = "「Em biết, ạ. ——Ưm—— hình, dáng——\\nCủa, anh, Soutetsu—— phùa—— của, chim——」"
"2728" = "「Ra vậy, có lý.\\nNhưng, nói là hạnh phúc thì——Ư!」"
"2767" = "「Quần áo—— hay gì đó—— sao cũng,\\nđược—— phùa—— ưm—— phù—— a ư」"
"3300" = "Can đảm quá, dễ thương quá, muốn hôn quá——\\nTôi phản xạ nghĩ vậy, nhưng bây giờ, đôi môi này còn có việc quan trọng khác phải làm."
"3887" = "（Trắng quá…… mà, thon thả thật đấy）"
```

Kiểm chứng: khối parse được bằng tomllib, 28 khóa, 0 sai lệch giá trị so với JSON (so sánh chuỗi thô; `\n` viết `\\n` nên parse ra đúng literal backslash-n của CSV3). Tất cả fix đều giữ nguyên ngắt dòng literal `\n` của VN cũ (không thêm `\n` thủ công mới). Diff-sanity: mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (xem log build §5).

## §7. Ghi chú cho Hieu (cần quyết / chờ thống nhất — không tính sai trong audit này)

- Thống nhất "Ohitoyo" (4 dòng: 2442, 2506, 2638, 2867) + 日ノ本 "Hinomoto" vs "Hinamoto" (1 dòng: 3178) — theo tiền lệ các file trước, fix trong đợt thống nhất.
- **3300 "Can đảm quá" cho 健気だ** — là từ đơn gần nhất cho 健気 (can đảm / đáng khâm phục / kiên cường); nếu Hieu muốn "Ngoan quá" hay cách diễn khác thì đổi.
- **3887 bỏ "chân em"** — danh từ thêm vào không có căn cứ JP/TW; nếu trong game cảnh đó rõ ràng đang nhìn chân em thì Hieu có thể khôi phục.
- **2292 không phải lệch dòng** — là lỗi dịch gốc của Gemini (đọc 「こんなにひどいと」 trong bối cảnh mưa mà suy ra "mưa to"); đã sửa theo TW. Không cần tìm dòng bị xáo.
- 20 fix fa/fu theo quy tắc đã chốt 19/11; "phù" đã bị dùng hệ thống cho mọi ふぁ/ふあ/ぷあ trong file này — các file khác có thể cũng mắc cùng kiểu, đáng kiểm tra khi audit tới.
- 4 strong candidates của queue chỉ là heuristic; lần đọc toàn bộ tìm ra 28 dòng sai (4,3%) — file sạch hơn các file Paulette nhưng lỗi fa/fu hệ thống chiếm đa số.

## Kết bài

File ふかみh3_夏休みの最後の日の、前の日: 649 dòng đã đọc hết, **28 dòng sai (4,3%)** — 20 SFX fa/fu (phù→phà/phùa theo quy tắc đã chốt), 4 gasp (2 từ sweep, 2 sweep bỏ sót), 3 sai nghĩa, 1 bịa thêm nghĩa (2292 "mưa to"). Không có chuỗi xoay, không lệch hàng, không nhiễm chéo, không dòng mồ côi, không dòng chưa dịch. CSV3 có 2 set — chỉ audit set tốt (11_Other), set home-folder là stale và JP bị xoay. JSON 28 khóa chuỗi; khối TOML parse OK, 28 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 28/28; lượt soát 2: 28/28, 0 bỏ, 0 sửa.
