# Audit — ハチロク09_採決.txt.toml (01_Hachiroku)

- File: `ハチロク09_採決.txt.toml` — route 01_Hachiroku, 1 bản duy nhất.
- Disk: `sources/toml2/translation_toml/01_Hachiroku/#U30cf#U30c1#U30ed#U30af09_#U63a1#U6c7a.txt.toml`
- md5: `df8fdf27838f6b6d01625020164b4e28` — không có file trùng (đã quét md5 toàn bộ 227 file TOML: 216 md5 riêng biệt, 11 nhóm trùng — file này không nằm trong nhóm trùng nào).
- Nội dung: ngày bỏ phiếu quyết định ở hội đồng thành phố Ohitoyo — buổi sáng Soutetsu và Hachiroku thức dậy, Hibiki mang bảng lật (flip) do Mayami chuẩn bị; phiên chất vấn: Paulette giải trình dự toán ngân sách bổ sung và tuyên bố từ chức thị trưởng, Soutetsu làm nhân chứng về tàu BBQ 8620, Kisaki (giám đốc ngân hàng Kumamoto) chất vấn về tính tái hiện của việc thay khung gầm 8620, Hachiroku lên tiếng về các tuyến đường sắt còn lại ở Kyushu; dự toán được thông qua; tiệc mừng; cuối file Soutetsu ra ngoài gặp Reina, Kon và bầy chim sẻ ở nhà xe đầu máy.
- Phương pháp: đọc từng dòng 471/471 đối chiếu JP + TW (CSV3), kiểm chứng sweep gasp, kiểm tra %l, kiểm tra trùng khóa / lệch dòng / mồ côi / chưa dịch.

## 1. Tổng quan

- Dòng script: **471** (độc thoại 207, Soutetsu 110, Hachiroku 40, Hibiki 22, Paulette 22, Kisaki 18, Reina 17, chủ tọa 11, nữ nghị sĩ 8, nghị sĩ trung kiên 7, Urakami 3, Kon 2, chim sẻ 2, Nagi 1, Fukami 1).
- CSV3: 1 set duy nhất, 471 khóa, 0 trùng khóa, 0 VN trống. TOML parse được, 471 khóa khớp CSV3 tuyệt đối về khóa.
- TOML vs CSV3: 297 dòng VN chỉ khác ở chỗ TOML-2 làm phẳng `\n` (literal) thành khoảng trắng — đã biết, CSV3 là chuẩn (đã kiểm chứng cơ học: 297/297 đều đúng dạng này, 0 lệch khác).
- `[selections]`: rỗng `{}`. Không có thẻ `%l` sai định dạng (không thiếu dấu `;` đóng). Có 1 thẻ `%l` do VN tự thêm (key 2288 — đã sửa, xem §3.6).
- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**

## 2. Kết quả: 39/471 (8,3%)

Phân loại (39):

- Thuật ngữ (đã quyết trong dự án): **29** — Ohimitera→Ohitoyo 24 dòng / 25 lần (2164, 3021, 3062, 2107, 3196, 2804, 3063, 2128, 1855, 2017, 2112, 2923, 2282, 1818, 2284, 1868, 2220, 1912, 2323, 2296, 3070, 2105 [×2], 2190, 2066); 湯医線→Tuyến Yunoi 1 (1818 — cùng dòng với Ohimitera); 運転鞄/鞄→"túi công tác" 4 (2900, 2899, 2672, 2952); gloss 帝鉄 "Đường sắt Hoàng gia"→"Đường sắt Đế quốc" 1 (2792).
- Gasp (sweep, đã kiểm chứng): **4** — 2452, 2453, 2454, 2649.
- SFX: **3** — 3334, 1473 (vỗ tay パチパチ "Lộp bộp"→"Bốp"), 1530 (すぅ "Su"→"Suu" theo công thức độ dài nguyên âm).
- Đại từ: **1** — 2064 Hachiroku gọi Fukami "cô"→"em".
- Dịch sai nghĩa: **1** — 2097 Kisaki bịa thêm "đùa à".
- Thẻ %l: **1** — 2288 gỡ thẻ VN tự thêm trên 静態保存.

29 dòng thuật ngữ sửa trực tiếp trong audit (theo tiền lệ ハチロク03/ハチロク07/ハチロク09_もくもくオリヴィ) — KHÔNG thêm lại các key này vào hàng đợi thống nhất.

## 3. Danh sách sửa (39)

### 3.1. Thuật ngữ

**Key 1818 [ハチロク] — thuật ngữ.** JP: `「九洲に残る鉄道路線は、 / 御一夜鉄道、[ゆのい,1]湯医線だけではございません」` / TW: `「九州剩下的鐵路線路不僅僅只有御一夜鐵路的湯醫線」` — Cũ: `Kyushu, / không chỉ có Tuyến Yui của Đường sắt Ohimitera đâu  […] có Tuyến Yui của Đường sắt Ohimitera đâu ạ.」 […] Tuyến Yui của Đường sắt Ohimitera đâu ạ.」` → Mới: `Kyushu, / không chỉ có Tuyến Yunoi của Đường sắt Ohitoyo đâu ạ. […]  Tuyến Yunoi của Đường sắt Ohitoyo đâu ạ.」 […] Tuyến Yunoi của Đường sắt Ohitoyo đâu ạ.」`. (湯医線 = "Tuyến Yunoi" (đã quyết); 御一夜鉄道 = "Đường sắt Ohitoyo". Một dòng mang cả hai lỗi.)

**Key 1855 [ポーレット] — thuật ngữ.** JP: `「しかし、人材の問題がありました。政界を見れば、 / 御一夜には優れた人材が数多くいらっしゃいますが――」` / TW: `「但是在人才方面存在問題。縱觀政治界，雖然御一夜擁有眾多優秀的人才——」` — Cũ: ` Nhìn vào giới chính trị, / Ohimitera có rất nhiều nhân tài xuấ […] ìn vào giới chính trị, / Ohimitera có rất nhiều nhân tài xuất ch` → Mới: ` Nhìn vào giới chính trị, / Ohitoyo có rất nhiều nhân tài xuấ […] Nhìn vào giới chính trị, / Ohitoyo có rất nhiều nhân tài xuất ch`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 1868 [双鉄] — thuật ngữ.** JP: `「近隣にある――そう、例えばみかん鉄道とでしたら、 / 御一夜-[やつしろ,2]八ツ城間を復線させれば、繋がれます」` / TW: `「位於近鄰的——比如說橙鐵路。若是讓御一夜到八代的廢線恢復，就能與之互通」` — Cũ: ` phục lại tuyến đường giữa Ohimitera và Yatsushiro, thì có thể […] ục lại tuyến đường giữa Ohimitera và Yatsushiro, thì có thể kết` → Mới: ` phục lại tuyến đường giữa Ohitoyo và Yatsushiro, thì có thể […] phục lại tuyến đường giữa Ohitoyo và Yatsushiro, thì có thể kết`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 1912 [ポーレット] — thuật ngữ.** JP: `「そっか……車輌は各地に――そして、ＳＬに特化した、 / 保全・改修のための設備や人材を、御一夜に集中させて」` / TW: `「原來如此……派出車輛前往各地——並且讓跟蒸汽機車配套的維護及修理設備還有人才聚集在御一夜」` — Cũ: `ệc bảo trì, sửa chữa SL về Ohimitera.」 […] bảo trì, sửa chữa SL về Ohimitera.」` → Mới: `ệc bảo trì, sửa chữa SL về Ohitoyo.」 […] c bảo trì, sửa chữa SL về Ohitoyo.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2017 [ポーレット] — thuật ngữ.** JP: `「ですので、御一夜の政・財のよりよき発展のために、 / 市長辞任の方がベターと、判断させていただきました」` / TW: `「因此，為了讓御一夜的財政得到更好的發展，我認為辭去市長一職是更好的方法」` — Cũ: `ủa cả chính trị và kinh tế Ohimitera, / tôi đã quyết định rằng  […] cả chính trị và kinh tế Ohimitera, / tôi đã quyết định rằng việc` → Mới: `ủa cả chính trị và kinh tế Ohitoyo, / tôi đã quyết định rằng  […] a cả chính trị và kinh tế Ohitoyo, / tôi đã quyết định rằng việc`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2066 [ハチロク] — thuật ngữ.** JP: `「すぐ南……御一夜と、これほど近くにあったのですね」` / TW: `「就在南邊不遠……原來離御一夜這麼近」` — Cũ: `Nam……Hóa ra nó lại nằm gần Ohimitera đến thế này sao.」 […] ……Hóa ra nó lại nằm gần Ohimitera đến thế này sao.」` → Mới: `Nam……Hóa ra nó lại nằm gần Ohitoyo đến thế này sao.」 […] am……Hóa ra nó lại nằm gần Ohitoyo đến thế này sao.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2105 [双鉄] — thuật ngữ.** JP: `「蒸気のふるさと御一夜として、全ての資源を連携させる。 / それは、御一夜にしか、鉄道でしか出来ないことだ」` / TW: `「我們要打著蒸汽之鄉的名號，讓御一夜協調運用所有的資源。這是只有御一夜，只有鐵路才能辦到的事」` — Cũ: ` là Quê hương của hơi nước Ohimitera, chúng ta sẽ liên kết tất […]  Quê hương của hơi nước Ohimitera, chúng ta sẽ liên kết tất cả  […] i nhau. / Đó là điều mà chỉ Ohimitera, chỉ đường sắt mới có thể […] hau. / Đó là điều mà chỉ Ohimitera, chỉ đường sắt mới có thể làm` → Mới: ` là Quê hương của hơi nước Ohitoyo, chúng ta sẽ liên kết tất […] là Quê hương của hơi nước Ohitoyo, chúng ta sẽ liên kết tất cả  […] i nhau. / Đó là điều mà chỉ Ohitoyo, chỉ đường sắt mới có thể […]  nhau. / Đó là điều mà chỉ Ohitoyo, chỉ đường sắt mới có thể làm`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2107 [日々姫] — thuật ngữ.** JP: `「御一夜に一番良かかと思うことば手伝ーとるだけ」` / TW: `「我只是覺得這樣做對御一夜最有益處，所以才會幫忙」` — Cũ: `mà em nghĩ là tốt nhất cho Ohimitera thôi.」 […] em nghĩ là tốt nhất cho Ohimitera thôi.」` → Mới: `mà em nghĩ là tốt nhất cho Ohitoyo thôi.」 […] à em nghĩ là tốt nhất cho Ohitoyo thôi.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2112 [稀咲] — thuật ngữ.** JP: `「隈元銀行御一夜支店長、宝生稀咲です」` / TW: `「我是隈元銀行御一夜支行行長寶生稀咲」` — Cũ: `Kisaki, Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto.」 […] aki, Giám đốc chi nhánh Ohimitera của Ngân hàng Kumamoto.」` → Mới: `Kisaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」 […] isaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2128 [議長] — thuật ngữ.** JP: `「この際、関連の質疑を続けます。 / 御一夜の未来を考える会。[にいつ,1]新津議員」` / TW: `「接下來繼續提出對本方案的質疑。有請御一夜未來規劃會的新津議員發言」` — Cũ: ` liên quan. / Hội Tương lai Ohimitera. Nghị sĩ Niitsu.」 […] ên quan. / Hội Tương lai Ohimitera. Nghị sĩ Niitsu.」` → Mới: ` liên quan. / Hội Tương lai Ohitoyo. Nghị sĩ Niitsu.」 […] liên quan. / Hội Tương lai Ohitoyo. Nghị sĩ Niitsu.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2164 [ハチロク] — thuật ngữ.** JP: `「左様ですね。今日の議会で、[あの子,3]8620の―― / いえ、御一夜そのものの未来が決定される」` / TW: `「是的。今天議會將會決定[那孩子,3]８６２０——不，是整個御一夜的未來」` — Cũ: `ng, là tương lai của chính Ohimitera sẽ được định đoạt.」 […]  là tương lai của chính Ohimitera sẽ được định đoạt.」` → Mới: `ng, là tương lai của chính Ohitoyo sẽ được định đoạt.」 […] g, là tương lai của chính Ohitoyo sẽ được định đoạt.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2190 [双鉄] — thuật ngữ.** JP: `「例えば……そうだな、真闇姉に、 / 御一夜市内のクマ焼酎の全体を見てもらおうと考える」` / TW: `「比如說……對了，假設讓真闇姐來管理御一夜市內整個隈燒酒行業」` — Cũ: `hochu Kuma trong thành phố Ohimitera.」 […] hu Kuma trong thành phố Ohimitera.」` → Mới: `hochu Kuma trong thành phố Ohitoyo.」 […] ochu Kuma trong thành phố Ohitoyo.」`. (Chỉ sửa thuật ngữ Ohimitera→Ohitoyo; "anh" của Soutetsu với Hachiroku GIỮ NGUYÊN — xem cờ §6.1.)

**Key 2220 [双鉄] — thuật ngữ.** JP: `「故に、御一夜を中心とした鉄道路線を復活させ、 / そこでのＳＬの集中運用というモデルを作る」` / TW: `「為此，我們需要讓以御一夜為中心的鐵路線路復活，創造集中運用蒸汽機車的模式」` — Cũ: `nh các tuyến đường sắt lấy Ohimitera làm trung tâm, / và tạo ra […] các tuyến đường sắt lấy Ohimitera làm trung tâm, / và tạo ra một` → Mới: `nh các tuyến đường sắt lấy Ohitoyo làm trung tâm, / và tạo ra […] h các tuyến đường sắt lấy Ohitoyo làm trung tâm, / và tạo ra một`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2282 [稀咲] — thuật ngữ.** JP: `「交換頂く\x%l台枠;#00ffc040;台枠%l;#;も、老朽部品には変わりない。 / 検査整備する御一夜鉄道側は、\x%l台枠;#00ffc040;台枠%l;#;損傷を見過ごした」` / TW: `「而交換來的\x%l台枠;#00ffc040;車架%l;#;也同樣是舊部件。負責檢查整備的御一夜鐵路方忽視了\x%l台枠;#00ffc040;車架%l;#;損傷」` — Cũ: `hận cũ kỹ. / Phía Đường sắt Ohimitera phụ trách kiểm tra bảo dưỡng,` → Mới: `hận cũ kỹ. / Phía Đường sắt Ohitoyo phụ trách kiểm tra bảo dưỡng,`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2284 [双鉄] — thuật ngữ.** JP: `「その中心に……御一夜が」` / TW: `「而御一夜……就是其中心」` — Cũ: `ủa sự kết nối đó……chính là Ohimitera.」 […] sự kết nối đó……chính là Ohimitera.」` → Mới: `ủa sự kết nối đó……chính là Ohitoyo.」 […] a sự kết nối đó……chính là Ohitoyo.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2296 [日々姫] — thuật ngữ.** JP: `「ＳＬの……蒸気の町―― / ううん、そう――蒸気のふるさと、御一夜」` / TW: `「蒸汽機車的……蒸汽之城——不，是蒸汽之鄉——御一夜」` — Cũ: `i——Quê hương của hơi nước, Ohimitera.」 […] Quê hương của hơi nước, Ohimitera.」` → Mới: `i——Quê hương của hơi nước, Ohitoyo.」 […] ——Quê hương của hơi nước, Ohitoyo.」`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2323 [双鉄] — thuật ngữ.** JP: `「御一夜をＳＬ観光の起点駅とする。\x%l8620;#00ffc040;8620%l;#;から乗り換えて、 / ＳＬで、九洲各地を観光できる。そんな未来を作るのだ」` / TW: `「讓御一夜成為蒸汽機車旅遊的起點站。從\x%l8620;#00ffc040;８６２０%l;#;換乘，然後搭乘蒸汽機車在九州各地觀光。我們要創造這樣的未來」` — Cũ: `「Biến Ohimitera thành ga xuất phát cho du […] 「Biến Ohimitera thành ga xuất phát cho du lịc` → Mới: `「Biến Ohitoyo thành ga xuất phát cho du […] 「Biến Ohitoyo thành ga xuất phát cho du lịc`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2672 [monologue] — thuật ngữ.** JP: `運転鞄からの、声。` / TW: `乘務包裡傳出了八六的聲音。` — Cũ: `t giọng nói, phát ra từ chiếc cặp lái tàu. […] nói, phát ra từ chiếc cặp lái tàu. […] ói, phát ra từ chiếc cặp lái tàu.` → Mới: `t giọng nói, phát ra từ chiếc túi công tác. […] ọng nói, phát ra từ chiếc túi công tác. […] i, phát ra từ chiếc túi công tác.`. (運転鞄/鞄 = "túi công tác" (quyết 20/11).)

**Key 2792 [monologue] — thuật ngữ.** JP: `その頬はワインのせいか、かなり赤らみ、 / 手には、\x%l帝鉄;#00ffc040;帝鉄%l;#;時代のものと思しき路線地図を持っている。` / TW: `可能是因為葡萄酒的原因，她的臉頰紅得厲害，手上則拿著好像屬於\x%l帝鉄;#00ffc040;帝國鐵路%l;#;時代的線路地圖。` — Cũ: `ời \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;. […] l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#;.` → Mới: `ời \x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;. […] \x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;.`. (帝鉄 = Teitetsu; gloss trong thẻ %l phải là "Đường sắt Đế quốc" (TW 帝國鐵路), không phải "Đường sắt Hoàng gia". Đây là lần duy nhất 帝鉄 xuất hiện trong file, đúng vị trí tooltip đầu tiên.)

**Key 2804 [monologue] — thuật ngữ.** JP: `それが、御一夜のよりよい未来を作ると信じ…… / そうしてそこでハチロクに、暮らして欲しいと願うから。` / TW: `因為我相信我們能夠創造對御一夜而言更好的未來……並希望八六能幸福地生活在這裡。` — Cũ: ` tương lai tốt đẹp hơn cho Ohimitera…… / Và vì tôi mong muốn, H […] ơng lai tốt đẹp hơn cho Ohimitera…… / Và vì tôi mong muốn, Hachi` → Mới: ` tương lai tốt đẹp hơn cho Ohitoyo…… / Và vì tôi mong muốn, H […] tương lai tốt đẹp hơn cho Ohitoyo…… / Và vì tôi mong muốn, Hachi`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2899 [monologue] — thuật ngữ.** JP: `運転鞄の中から、詰まった声。` / TW: `從乘務包中傳來倒吸一口涼氣的聲音。` — Cũ: `Từ trong chiếc cặp lái tàu, phát ra một giọng nói n […] Từ trong chiếc cặp lái tàu, phát ra một giọng nói ngh […] Từ trong chiếc cặp lái tàu, phát ra một giọng nói nghẹn ` → Mới: `Từ trong chiếc túi công tác, phát ra một giọng  […] Từ trong chiếc túi công tác, phát ra một giọng nói ngh […] Từ trong chiếc túi công tác, phát ra một giọng nói nghẹn `. (運転鞄/鞄 = "túi công tác" (quyết 20/11).)

**Key 2900 [monologue] — thuật ngữ.** JP: `運転鞄の中からは、低く抑えた―― / そして嬉しげで誇らしげなハチロクの声。` / TW: `從乘務包中傳出八六的聲音——她把聲音壓得很低，但聽起來充滿了喜悅和自豪。` — Cũ: `Từ trong chiếc cặp lái tàu, truyền ra một giọng nói […] Từ trong chiếc cặp lái tàu, truyền ra một giọng nói t […] Từ trong chiếc cặp lái tàu, truyền ra một giọng nói trầm` → Mới: `Từ trong chiếc túi công tác, truyền ra một giọn […] Từ trong chiếc túi công tác, truyền ra một giọng nói t […] Từ trong chiếc túi công tác, truyền ra một giọng nói trầm`. (運転鞄/鞄 = "túi công tác" (quyết 20/11).)

**Key 2923 [monologue] — thuật ngữ.** JP: `現在の御一夜鉄道の財政状況に補助金がくわわったとして、 / それに対応するのは正直……極めて厳しい。` / TW: `憑目前御一夜鐵路的財政狀況，就算有補助金補貼，要承受這樣的費用……老實說是非常困難的。` — Cũ: `ính hiện tại của Đường sắt Ohimitera, / thì nói thật, việc đáp  […]  hiện tại của Đường sắt Ohimitera, / thì nói thật, việc đáp ứng ` → Mới: `ính hiện tại của Đường sắt Ohitoyo, / thì nói thật, việc đáp  […] nh hiện tại của Đường sắt Ohitoyo, / thì nói thật, việc đáp ứng `. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 2952 [monologue] — thuật ngữ.** JP: `鞄を開けて抱き上げたなら、 / ハチロクは、その体勢のまま大音声を張り上げる。` / TW: `我打開包把她抱起，八六保持著原來的姿勢大聲說道。` — Cũ: `Khi tôi mở cặp và ôm cô ấy lên, / Hachirok […] Khi tôi mở cặp và ôm cô ấy lên, / Hachiroku v` → Mới: `Khi tôi mở túi công tác và ôm cô ấy lên, / Hac […] Khi tôi mở túi công tác và ôm cô ấy lên, / Hachiroku v`. (運転鞄/鞄 = "túi công tác" (quyết 20/11).)

**Key 3021 [monologue] — thuật ngữ.** JP: `御一夜市議会、予算委員会の補正予算審議。 / その採決が行われるのだから。` / TW: `會議中將會對御一夜市議會、預算委員會的預算修正案審議進行表決。` — Cũ: `uộc họp hội đồng thành phố Ohimitera, thẩm định ngân sách bổ s […]  họp hội đồng thành phố Ohimitera, thẩm định ngân sách bổ sung ` → Mới: `uộc họp hội đồng thành phố Ohitoyo, thẩm định ngân sách bổ s […] ộc họp hội đồng thành phố Ohitoyo, thẩm định ngân sách bổ sung `. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 3062 [monologue] — thuật ngữ.** JP: `御一夜の未来を見誤らぬよう、議論を活性化させるため、 / その程度の逸脱を良しとするとて、不思議もあるまい。` / TW: `為了不耽誤御一夜的未來，為了讓議論更加具備靈活性，他對這種程度的意外睜隻眼閉隻眼也是不足為奇的。` — Cũ: `n sai lầm về tương lai của Ohimitera, nhằm thúc đẩy các cuộc t […] ai lầm về tương lai của Ohimitera, nhằm thúc đẩy các cuộc tranh` → Mới: `n sai lầm về tương lai của Ohitoyo, nhằm thúc đẩy các cuộc t […]  sai lầm về tương lai của Ohitoyo, nhằm thúc đẩy các cuộc tranh`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 3063 [monologue] — thuật ngữ.** JP: `御一夜のよりよい未来を築くため―― / その一点を目的とした、無私の行動。` / TW: `為了創造御一夜更好的未來——她所採取的行動全都圍繞著這一中心，沒有一點私心。` — Cũ: ` tương lai tốt đẹp hơn cho Ohimitera—— / Một hành động vô tư, c […] ơng lai tốt đẹp hơn cho Ohimitera—— / Một hành động vô tư, chỉ n` → Mới: ` tương lai tốt đẹp hơn cho Ohitoyo—— / Một hành động vô tư, c […] tương lai tốt đẹp hơn cho Ohitoyo—— / Một hành động vô tư, chỉ n`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 3070 [monologue] — thuật ngữ.** JP: `焼酎、温泉、\x%l蒸気機関車;#00ffc040;蒸気機関車%l;#;――御一夜は、今の時点でも、 / “蒸気のふるさと”と呼ばれてしかるべき町だ。` / TW: `燒酒、溫泉、\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;——哪怕是現在，御一夜也一樣稱得上是“蒸汽之鄉”。` — Cũ: `040;Đầu máy hơi nước%l;#;——Ohimitera, ngay tại thời điểm này,\ […] ;Đầu máy hơi nước%l;#;——Ohimitera, ngay tại thời điểm này, / cũn` → Mới: `040;Đầu máy hơi nước%l;#;——Ohitoyo, ngay tại thời điểm này,\ […] 40;Đầu máy hơi nước%l;#;——Ohitoyo, ngay tại thời điểm này, / cũn`. (御一夜 = "Ohitoyo" (đã quyết).)

**Key 3196 [monologue] — thuật ngữ.** JP: `よりよい御一夜を作るための最適解を探し求める、 / いわば、ひとつのコンペなのだと。` / TW: `而是一場尋求建設御一夜的最佳方案的競爭。` — Cũ: `ưu nhất / nhằm xây dựng một Ohimitera tốt đẹp hơn. […] nhất / nhằm xây dựng một Ohimitera tốt đẹp hơn.` → Mới: `ưu nhất / nhằm xây dựng một Ohitoyo tốt đẹp hơn. […] u nhất / nhằm xây dựng một Ohitoyo tốt đẹp hơn.`. (御一夜 = "Ohitoyo" (đã quyết).)

### 3.2. Gasp (sweep)

**Key 2452 [双鉄] — gasp.** JP: `「っ！」` / TW: `「！」` — Cũ: `「!」` → Mới: `「Ư!」`. (JP là cả dòng chỉ có tiếng nấc っ + dấu câu; VN chỉ còn dấu câu — thêm Ư (sweep lost-gasp-whole, đã kiểm chứng).)

**Key 2453 [ポーレット] — gasp.** JP: `「っ！！？」` / TW: `「！！？」` — Cũ: `「!!?」` → Mới: `「Ư!!?」`. (Như 2452 (sweep lost-gasp-whole, đã kiểm chứng).)

**Key 2454 [ハチロク] — gasp.** JP: `「っ！？」` / TW: `「！？」` — Cũ: `「!?」` → Mới: `「Ư!?」`. (Như 2452 (sweep lost-gasp-whole, đã kiểm chứng).)

**Key 2649 [monologue] — gasp.** JP: `粉蔵の技術者達もそうだし、閉鎖されてしまったという、 / 日ノ本車輌蒸気部門の技師たちも――っ！` / TW: `不僅是小倉的技術人員，還有據說已經被關閉的日本車輛蒸汽部門的技工——啊！` — Cũ: `ợc cho là đã bị đóng cửa nữa——!` → Mới: `ợc cho là đã bị đóng cửa nữa——Ư!`. (JP kết bằng ――っ！, TW kết ——啊！; VN giữ dấu gạch nhưng làm mất tiếng nấc — thêm Ư sau dấu gạch (sweep lost-gasp-trailing, đã kiểm chứng).)

### 3.3. SFX

**Key 1473 [monologue] — SFX.** JP: `パチ、パチと。最初の拍手は、稀咲から。 / ほどなくそれは、議場のすべて、全ての手から、鳴り響く。` / TW: `“啪、啪”。第一個鼓掌的人是稀咲。不久後，會場的所有人都送來了掌聲。` — Cũ: `Lộp bộp, lộp bộp. Tiếng vỗ tay đầu t […] Lộp bộp, lộp bộp. Tiếng vỗ tay đầu tiên, là […] Lộp bộp, lộp bộp. Tiếng vỗ tay đầu tiên, là t` → Mới: `Bốp, bốp. Tiếng vỗ tay đầu tiên, […] Bốp, bốp. Tiếng vỗ tay đầu tiên, là […] Bốp, bốp. Tiếng vỗ tay đầu tiên, là t`. (Như 3334: パチ、パチ là tiếng vỗ tay đầu tiên của Kisaki.)

**Key 1530 [ハチロク] — SFX.** JP: `「……すぅ……すぅ」` / TW: `「……呼……呼」` — Cũ: `「……Su……su.」 […] 「……Su……su.」` → Mới: `「……Suu……suu.」 […] 「……Suu……suu.」`. (すぅ = す + ぅ → công thức độ dài nguyên âm: VN 2 nguyên âm (tiền lệ ふうむ→"Hừừm").)

**Key 3334 [monologue] — SFX.** JP: `（パチパチパチパチ）` / TW: `（啪啪啪啪）` — Cũ: `（Lộp bộp lộp bộp） […] （Lộp bộp lộp bộp） […] （Lộp bộp lộp bộp）` → Mới: `（Bốp bốp bốp bốp） […] （Bốp bốp bốp bốp） […] （Bốp bốp bốp bốp）`. (パチパチ là tiếng vỗ tay (TW 啪啪); "Lộp bộp" là tiếng lộp bộp (mưa/rơi), sai âm. Toàn dự án dùng "Bốp" cho vỗ tay (3 dòng khác đã đúng).)

### 3.4. Đại từ

**Key 2064 [ハチロク] — đại từ.** JP: `「ど、どう――と聞かれましても……」` / TW: `「就、就算——你這麼問……」` — Cũ: `「Th, thế nào——cô hỏi vậy thì……」` → Mới: `「Th, thế nào——em hỏi vậy thì……」`. (Người nghe là Fukami (hỏi ở 2390, Hachiroku trả lời ở đây). Fukami gọi Hachiroku là "Chị Hachiroku" (tiền lệ ROUTE-AUDIT 590: Hachiroku tự xưng "chị" với Fukami) → Hachiroku gọi Fukami là "em", không phải "cô".)

### 3.5. Dịch sai nghĩa

**Key 2097 [稀咲] — dịch sai nghĩa.** JP: `「復線って、君、双鉄。 / そんな簡単に言うけれど」` / TW: `「恢復廢線……雙鐵你啊，話說得倒是簡單」` — Cũ: `「Khôi phục tuyến đường, cậu đùa à, Soutetsu. / Nói thì nghe dễ dà` → Mới: `「Khôi phục tuyến đường, cậu Soutetsu. / Nói thì nghe dễ dà`. (JP: 「復線って、君、双鉄。そんな簡単に言うけれど」— Kisaki chỉ nói "chuyện khôi phục tuyến đường ấy, cậu Soutetsu"; VN cũ bịa thêm "đùa à" (cáo buộc đùa giỡn) không có trong JP.)

### 3.6. Thẻ %l

**Key 2288 [ポーレット] — thẻ %l.** JP: `「[せいたい,1]静態保存のものを含めれば、 / [きゅうしゅう,1]九洲内だけで、さらに数倍はあると思います」` / TW: `「若是算上靜態保存的車輛，光是九州範圍內的數目就比這多出好幾倍」` — Cũ: `tính cả những chiếc đang được \x%l静態保存;#00ffc040;lưu tĩnh%l;#;, / thì chỉ tính r […] ợc \x%l静態保存;#00ffc040;lưu tĩnh%l;#;, / thì chỉ tính riêng trong Ky` → Mới: `tính cả những chiếc đang được lưu tĩnh, / thì chỉ tính riêng  […] những chiếc đang được lưu tĩnh, / thì chỉ tính riêng trong Ky`. (JP chỉ có ruby [せいたい,1] trên 静態, không có thẻ %l; VN tự thêm thẻ gloss — mẫu bịa thêm của Gemini (xem skill). Gỡ thẻ, giữ chữ "lưu tĩnh" trong câu.)

## 4. Kiểm tra sweep gasp

- Sweep có **4 mục** cho file này (2452, 2453, 2454, 2649) — nhận cả 4, đã kiểm chứng từng giá trị với JP/TW (2452–2454 là cả dòng chỉ có っ + dấu câu; 2649 TW kết bằng 啊 xác nhận tiếng nấc).
- Quét máy bổ sung: **không còn gasp nào sweep bỏ sót.** Các っ còn lại đã được diễn đạt sẵn: 1945/1946 ケンっ → "Keng!" (tiếng sủa của Kon, không phải nấc người); 1989 ひゃっ → "hya" (họ ひあ/ひゃ ngẫu hứng theo Hieu 20/11); 1990 ちゅんくっ → "Chiếp chiếp!"; 1993 ちょっ → "Chờ chút!?"; 1999 むっ → "hử?"; 2004 うんっ / 2179 はいっ → "Vâng!"; 1503 む → "Ưm", 1994 んっ―― → "Ưm——", 1995 ん → "Ưm". Không có dòng cười ふふ/うふふ nào bị dịch thành tiếng rên; không có dòng ふぁ/ふあ nào.

## 5. Các dòng giữ nguyên (đã kiểm tra, không sai)

- **2240** Soutetsu "bọn anh" với Hibiki — dạng nhóm, không chịu quy tắc số ít (tiền lệ ROUTE-AUDIT dòng 774: "bọn anh" của Soutetsu GIỮ 3 dòng theo quy tắc dạng nhóm).
- **2115** Kisaki tự xưng "Tôi" — phát biểu trước nhóm (Soutetsu + Paulette + Hibiki), "Tôi" là dạng trung tính khi xưng hô với nhóm (tiền lệ Paulette 14: "anh"→"tôi" khi xưng hô nhóm).
- **2421/2773** 再現性 → "tính khả thi để tái hiện lại" — giữ: diễn đạt tương đương "tính tái hiện được" trong ngữ cảnh (Kisaki hỏi liệu cơ duyên có lặp lại được không).
- **3333** （トンっ） → "（Cạch）" — giữ: SFX ngẫu hứng theo ngữ cảnh; toàn dự án có dòng khác dùng "（Cạch）" cho トンっ.
- **2405/2381** フランク産 → "Frank (Pháp)" / "Frank" — giữ: Frank là tên trong truyện của Pháp, ghi chú "(Pháp)" là gloss giải thích hợp lệ, không bịa nghĩa.
- **2404/2062** 加東雀/加東隼戦闘隊 → "Kato Suzume (Chim sẻ Kato)" / "Đội chiến đấu Kato Hayabusa (Chim ưng Kato)" — giữ: tên riêng + gloss nghĩa trong ngoặc, đúng trò đùa gốc (雀 = chim sẻ, 隼 = chim ưng).
- **2062** "Hồi nhỏ anh từng đọc" — JP 読んでな (đọc); TW nói 電影 (xem phim) là sai, JP thắng TW.
- **1988** Reina gọi Soutetsu 双鉄さん → "anh Soutetsu"; **2390** Fukami gọi Soutetsu 双鉄さん → "anh Soutetsu"; **2416/2382/2023** Soutetsu "anh" với Reina — đều đúng quy tắc đã sửa ("anh" với Reina). **1983/2095/2211/2240/2286** Soutetsu "anh" với Hibiki — đúng.
- **2844** TW bịa thêm tiếng gõ "哐、哐" — JP chỉ có ぽつ、ぽつ (lác đác); VN theo JP, đúng.

## 6. Cờ cho Hieu (không tự quyết)

1. **Phạm vi "anh" của Soutetsu với Hachiroku — 5 dòng: 1870, 2002, 2189, 2190, 2230.** Cùng câu hỏi đã cờ ở ハチロク09_もくもくオリヴィ (1073, 1724, 1883, 1578, 1734, 1861, 1545, 1891, 2116 — cảnh tắm/đêm): Soutetsu tự xưng "anh" với Hachiroku trong những khoảnh khắc riêng tư (1870 động viên Hachiroku trước phiên chất vấn: "Giọng nói của em là giọng nói của anh"; 2002/2189/2190/2230 ở tiệc mừng sau khi dự toán thông qua). Quy tắc hiện hành nói "tôi" với Hachiroku, nhưng các file trước đã sửa "anh"→"tôi" với Hachiroku ở ngữ cảnh khác (vd. ハチロク10 2475/2479/2656) — còn ở đây là ngữ cảnh thân mật. Giữ nguyên cả 5 dòng, chờ Hieu chốt: giữ toàn bộ "anh" trong cảnh riêng tư, hay sửa thành "tôi" theo quy tắc chung?
2. **"Anh Migita" với Soutetsu — 3 dòng: 1937, 1825 (nữ nghị sĩ Saitou với Soutetsu trong phiên chất vấn), 2449 (Urakami với Soutetsu).** Cùng câu hỏi đã cờ ở ハチロク10 (Dr. Phoenix→Soutetsu "Anh Migita" vs "ngài Migita"): trong bối cảnh hội đồng trang trọng, gọi Soutetsu là "anh Migita" có đúng không, hay nên là "ngài Migita"? Giữ nguyên, chờ Hieu.
3. **2411 民由連 → "Đảng Dân Do".** JP viết 民由連 (ruby みんゆうれん), TW viết 民友連. VN theo JP (由 → "Do"). "Đảng Dân Do" hay "Đảng Dân Hữu" (theo TW)? Giữ nguyên, chờ Hieu.
4. **持株会社 → "công ty cổ phần" — câu hỏi thuật ngữ toàn dự án, KHÔNG sửa trong audit này.** "Công ty cổ phần" (joint-stock) khác khái niệm "công ty holding" (持株会社), nhưng cách dịch này dùng nhất quán toàn dự án: 10 dòng / 4 file (file này 5: 1549, 2131, 2189, 2143, 1536; ハチロク12 3; ハチロク15 1; れいな03 1). Sửa riêng file này sẽ phá vỡ nhất quán — hỏi Hieu có đổi thành "công ty holding" / "công ty mẹ nắm giữ cổ phần" trong đợt thống nhất không.

## 7. Lượt soát 2

- Tổng: **39** / kiểm chứng lại: **39** / bỏ: **0** / sửa: **0**.
- Đã đọc lại toàn bộ 39 giá trị fix đối chiếu JP (+TW khi cần): 24 dòng Ohimitera→Ohitoyo (25 lần) + 1 dòng Yui→Yunoi, 4 dòng túi công tác, 1 gloss Đế quốc, 4 gasp sweep, 3 SFX, 1 đại từ, 1 nghĩa, 1 thẻ — tất cả đều đúng JP, không dòng nào phải loại hay sửa lại. Kiểm chứng cơ học: JSON 39 mục, khối TOML 39 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 39/39; mỗi fix chỉ khác VN cũ ở đúng chỗ sửa (đã kiểm tra diff từng dòng).

## 8. Khối TOML (đã kiểm chứng parse)

```toml
"1473" = "Bốp, bốp. Tiếng vỗ tay đầu tiên, là từ Kisaki.\\nChẳng mấy chốc, nó đã vang lên từ khắp hội trường, từ tất cả những đôi bàn tay."
"1530" = "「……Suu……suu.」"
"1818" = "「Những tuyến đường sắt còn sót lại ở Kyushu,\\nkhông chỉ có Tuyến Yunoi của Đường sắt Ohitoyo đâu ạ.」"
"1855" = "「Tuy nhiên, lại có vấn đề về nhân sự. Nhìn vào giới chính trị,\\nOhitoyo có rất nhiều nhân tài xuất chúng, nhưng mà——」"
"1868" = "「Nằm ở khu vực lân cận——đúng rồi, ví dụ như Đường sắt Mikan,\\nnếu chúng ta khôi phục lại tuyến đường giữa Ohitoyo và Yatsushiro, thì có thể kết nối được với họ.」"
"1912" = "「Ra là vậy……phân bổ phương tiện đến các nơi——và rồi, tập trung những trang thiết bị, nhân lực\\nchuyên môn hóa cho việc bảo trì, sửa chữa SL về Ohitoyo.」"
"2017" = "「Vì vậy, vì sự phát triển tốt đẹp hơn của cả chính trị và kinh tế Ohitoyo,\\ntôi đã quyết định rằng việc từ chức thị trưởng sẽ là lựa chọn tốt hơn.」"
"2064" = "「Th, thế nào——em hỏi vậy thì……」"
"2066" = "「Ngay phía Nam……Hóa ra nó lại nằm gần Ohitoyo đến thế này sao.」"
"2097" = "「Khôi phục tuyến đường, cậu Soutetsu.\\nNói thì nghe dễ dàng thế thôi.」"
"2105" = "「Với tư cách là Quê hương của hơi nước Ohitoyo, chúng ta sẽ liên kết tất cả các nguồn tài nguyên lại với nhau.\\nĐó là điều mà chỉ Ohitoyo, chỉ đường sắt mới có thể làm được.」"
"2107" = "「Em chỉ đang giúp đỡ những việc mà em nghĩ là tốt nhất cho Ohitoyo thôi.」"
"2112" = "「Tôi là Houshou Kisaki, Giám đốc chi nhánh Ohitoyo của Ngân hàng Kumamoto.」"
"2128" = "「Nhân dịp này, chúng ta sẽ tiếp tục phần hỏi đáp liên quan.\\nHội Tương lai Ohitoyo. Nghị sĩ Niitsu.」"
"2164" = "「Đúng vậy nhỉ. Trong cuộc họp hội đồng hôm nay, tương lai của đứa bé đó, 8620——\\nKhông, là tương lai của chính Ohitoyo sẽ được định đoạt.」"
"2190" = "「Ví dụ như……đúng rồi, giả sử anh muốn nhờ chị Mayami,\\nquản lý toàn bộ mảng rượu shochu Kuma trong thành phố Ohitoyo.」"
"2220" = "「Do đó, chúng ta sẽ hồi sinh các tuyến đường sắt lấy Ohitoyo làm trung tâm,\\nvà tạo ra một mô hình tập trung vận hành SL tại đó.」"
"2282" = "「\\x%l台枠;#00ffc040;Khung gầm%l;#; được thay thế, cũng vẫn chỉ là những bộ phận cũ kỹ.\\nPhía Đường sắt Ohitoyo phụ trách kiểm tra bảo dưỡng, đã bỏ sót những hư hỏng của \\x%l台枠;#00ffc040;khung gầm%l;#;.」"
"2284" = "「Và trung tâm của sự kết nối đó……chính là Ohitoyo.」"
"2288" = "「Nếu tính cả những chiếc đang được lưu tĩnh,\\nthì chỉ tính riêng trong Kyushu, tôi nghĩ số lượng còn gấp vài lần như thế.」"
"2296" = "「Thành phố của SL……của hơi nước——\\nKhông, đúng rồi——Quê hương của hơi nước, Ohitoyo.」"
"2323" = "「Biến Ohitoyo thành ga xuất phát cho du lịch SL. Từ \\x%l8620;#00ffc040;8620%l;#; đổi chuyến,\\nđể có thể đi du lịch khắp Kyushu bằng SL. Chúng ta sẽ tạo ra một tương lai như vậy.」"
"2452" = "「Ư!」"
"2453" = "「Ư!!?」"
"2454" = "「Ư!?」"
"2649" = "Các kỹ thuật viên ở Kokura cũng vậy, và cả những kỹ sư\\ncủa bộ phận hơi nước thuộc Công ty Xe lửa Hinomoto, nơi được cho là đã bị đóng cửa nữa——Ư!"
"2672" = "Một giọng nói, phát ra từ chiếc túi công tác."
"2792" = "Có lẽ do rượu vang, hai má cô ấy khá ửng đỏ,\\ntrên tay đang cầm một tấm bản đồ tuyến đường, có vẻ như là từ thời \\x%l帝鉄;#00ffc040;Đường sắt Đế quốc%l;#;."
"2804" = "Vì tôi tin rằng, điều đó sẽ tạo ra một tương lai tốt đẹp hơn cho Ohitoyo……\\nVà vì tôi mong muốn, Hachiroku sẽ sống ở đó."
"2899" = "Từ trong chiếc túi công tác, phát ra một giọng nói nghẹn lại."
"2900" = "Từ trong chiếc túi công tác, truyền ra một giọng nói trầm thấp——\\nNhưng lại chứa đựng sự vui sướng và tự hào của Hachiroku."
"2923" = "Dù có thêm tiền trợ cấp vào tình hình tài chính hiện tại của Đường sắt Ohitoyo,\\nthì nói thật, việc đáp ứng được chi phí đó……là cực kỳ khó khăn."
"2952" = "Khi tôi mở túi công tác và ôm cô ấy lên,\\nHachiroku vẫn giữ nguyên tư thế đó, lớn tiếng nói."
"3021" = "Cuộc họp hội đồng thành phố Ohitoyo, thẩm định ngân sách bổ sung của ủy ban ngân sách.\\nBởi vì cuộc bỏ phiếu sẽ được diễn ra."
"3062" = "Để không nhìn nhận sai lầm về tương lai của Ohitoyo, nhằm thúc đẩy các cuộc tranh luận sôi nổi hơn,\\nviệc ông ấy chấp nhận mức độ sai lệch đó, cũng không có gì lạ."
"3063" = "Để xây dựng một tương lai tốt đẹp hơn cho Ohitoyo——\\nMột hành động vô tư, chỉ nhắm vào một mục đích duy nhất đó."
"3070" = "Rượu shochu, suối nước nóng, \\x%l蒸気機関車;#00ffc040;Đầu máy hơi nước%l;#;——Ohitoyo, ngay tại thời điểm này,\\ncũng đã là một thành phố xứng đáng được gọi là \"Quê hương của hơi nước\" rồi."
"3196" = "Mà là một cuộc thi, để tìm ra giải pháp tối ưu nhất\\nnhằm xây dựng một Ohitoyo tốt đẹp hơn."
"3334" = "（Bốp bốp bốp bốp）"
```

## Kết bài

File ハチロク09_採決.txt.toml: 471 dòng đã đọc hết, **39 dòng sai (8,3%)** — không lệch dòng, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch. Lỗi tập trung ở thuật ngữ đã quyết (29/39: Ohimitera 24 dòng, túi công tác 4, gloss Đế quốc 1) + 4 gasp sweep + 3 SFX + 1 đại từ + 1 nghĩa + 1 thẻ. 4 cờ cho Hieu (§6) — phạm vi "anh" Soutetsu–Hachiroku (5 dòng), "Anh Migita" (3 dòng), 民由連 "Đảng Dân Do", và 持株会社 "công ty cổ phần" toàn dự án. Khối TOML 39 khóa đã parse-kiểm chứng, 0 sai lệch giá trị.

Kết bài