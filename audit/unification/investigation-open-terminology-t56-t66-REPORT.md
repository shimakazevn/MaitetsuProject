# Điều tra E1 — §1 Thuật ngữ OPEN T56–T66 (chỉ điều tra, KHÔNG sửa)

**Phạm vi:** chỉ điều tra + đề xuất quyết định cho 11 mục OPEN §1 (T56–T66). Không viết fix JSON, không đổi bất kỳ giá trị nào. Người điều phối (coordinator) quyết định; đợt batch sau mới áp dụng.

**Tài liệu đã đọc trước:** `unification/UNIFICATION-BRIEF.md`, `UNIFICATION-LIST.md` (§0 + §1 T56–T66), `AUDIT-BRIEF.md`, `custom-skills/aligned_translation_audit/SKILL.md` (hai điểm stale trong skill đã được brief supersede: 義→"nuôi" đã chốt đúng; "hỏi user khi JP/TW lệch" đã supersede bởi uỷ quyền quyết định — áp dụng ở đây).

## 0. Phương pháp

- **Nguồn:** CSV3 master (`sources/csv3/Matetsu Last Run - Trang tính 3.csv`), **chỉ good-set 87.833 dòng** — đã bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`. TOML-2 đối chiếu khi cần (vd. 2102, 1134). Các fix list đã merge: `audit-*-wrong.json` (216 file) + `moans/moan-*-wrong.json` (64 file + supplement).
- **Giá trị hiện tại (CUR) của một dòng** = fix moan nếu có, không thì fix audit, không thì VN CSV3 (good-set). Đếm bằng script CHỈ để liệt kê/đếm (đúng luật no-bulk-script); mọi quyết định đọc từng dòng JP + TW + dòng kề.
- **Sửa lỗi loader trong lúc làm:** lần chạy đầu suy file từ tên JSON (sai — mọi `*-wrong.json` đều KHÔNG có trường `file`), nên CUR lần đầu thực chất là VN CSV3. Đã chạy lại, suy file theo khớp `(key, JP)` với CSV3: khớp 9.144/9.243 audit + 1.516/1.535 moan. 4 file không khớp được bằng cách này (`audit-00common14` 52 mục dạng dict keyed-by-key; `audit-lr-nagih2` 46 mục dạng chuỗi trần; `audit-nagifukami07-bunki` 1 mục; `audit-obasan` 255 mục không có trường fix) — đã kiểm tra bằng tay: cả 4 file đều KHÔNG chứa bất kỳ thuật ngữ T56–T66 nào; riêng Common 14 key 1551 đã kiểm tra tay (fix chỉ đổi Ohimitera→Ohitoyo, không đụng 頭取). Mọi số đếm trong báo cáo này đều là CUR sau khi sửa loader, đã kiểm chứng lại.
- **Trích dẫn trong list bị sai (đã hiệu chỉnh khi tra):**
  - T56 "仲国01 1752 vs 1712": 1752 thuộc **仲国07** (không phải 仲国01); key 1712 **không có dòng 仲国 nào**.
  - T56 "仲国08: Trung Quốc 21 vs Trọng Quốc 61 vs Zhongguo 5": sai. Toàn file 仲国08: "Trọng Quốc" 40 lượt, "Trung Quốc" 0, "Zhongguo" 0; trong 34 dòng có JP 仲国, cả 34 đều "Trọng Quốc".
  - T57 "真闇01": thực tế là **真闇03_ひとしずく**; "ハチロク03_冥国式 1848": **không tồn tại dòng này** — chỉ có ハチロク09_もくもくオリヴィ 1848.
  - T63 "仲国04 key 60": **không tồn tại** — các dòng liên quan là 仲国03 2082/2248 + 日々姫02 key 60.
  - T64 "凪ふかみ05 3512": **sai file** — dòng đó là **ハチロク05_レイルロオドたち key 3512**; không có key 3512 nào ở 凪ふかみ05 trong CSV3.

---

## T56. 仲国 → "Trung Quốc" vs "Trọng Quốc" vs "Zhongguo"

**Câu hỏi:** tên nước hư cấu 仲国 (đọc ちゅうごく, chỉ Trung Quốc) dịch thống nhất bằng dạng nào, toàn dự án?

**Dòng đã đọc:** toàn bộ **204 dòng có JP 仲国** (good-set). Đếm theo dòng (CUR, phân loại theo dạng xuất hiện đầu tiên trong dòng):

| Dạng hiện tại | Số dòng | Phân bố theo file |
|---|---|---|
| "Trung Quốc" | **76** | 仲国01 24 · 仲国06 19 · 仲国07 21 · 仲国02 1 · 仲国05 3 · グランド08 2 · グランド11 4 · lr稀咲追加03 1 · lr稀咲追加h 1 |
| "Trọng Quốc" | **72** | lr稀咲追加01 12 · lr稀咲追加02 14 · lr稀咲追加03 4 · 稀咲h3 8 · 仲国08 34 |
| "Zhongguo" | **48** | 仲国02 27 · 仲国03 16 · 仲国04 5 |
| Khác (không phải tên nước) | **8** | xem dưới |

Số lượt nhắc trong CUR: "Trung Quốc" 83 · "Trọng Quốc" 77 · "Zhongguo" 50. 8 dòng "khác": 5 dòng ngôn ngữ "tiếng Trung" (仲国01 1704/2511, 仲国05 2749, 仲国07 1887/1997 — đúng, không đổi); 1 dòng "Nakakuni" (lr_日々姫ふかみh1 1689); 1 dòng "nước Chukoku" (れいな03 2070); 1 dòng không nhắc tên nước (仲国06 1796, JP 仲国国内 dịch "trong nước" — đúng, không đổi).

**Bằng chứng quyết định:**

1. **Tiền lệ audit đã merge — グランド08 1722.** JP liệt kê 6 nước: `[めいこく,1]冥国、[えいこく,1]詠国、[どっこく,1]髑国、フランク、[ちゅうごく,1]仲国、[かんこく,1]汗国`. VN cũ: "Mỹ, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc". Audit fix: "Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc" — auditor **đổi 冥国→"Minh Quốc" nhưng GIỮ NGUYÊN 仲国→"Trung Quốc" và 詠国→"Anh" trong cùng một dòng**. Cùng mẫu lặp lại ở 5 dòng khác có cả 冥国 lẫn 詠国: ハチロク02 2766, ハチロク03 1580/2437, 凪ふかみ01 1587 — audit đổi "Mỹ"→"Minh Quốc" nhưng giữ "Anh"/"kiểu Anh". Đây là bằng chứng mạnh nhất: chính các auditor đã áp dụng "Minh Quốc" cho 冥国 mà vẫn để "Trung Quốc"/"Anh" yên.
2. **Ghi chú quy ước trong ROUTE-AUDIT.md:431** (parent-verified): "quy ước thế giới hư cấu: 冥国=Mỹ, 詠国=Anh, 髑国=Đức, 仲国=Trung Quốc". Nhánh 冥国=Mỹ đã bị supersede bởi quy tắc chốt 冥国="Minh Quốc" + thực hành audit (điểm 1); nhưng ba nhánh còn lại (詠国=Anh, 髑国=Đức, 仲国=Trung Quốc) được chính các audit sau đó xác nhận (điểm 1). 髑国 cũng vậy: 10 dòng JP 髑国, CUR "Đức" 9 dòng, "Dokkoku (Đức)" 1 dòng (chỉ trong list 真闇03 1687).
3. **JP tự viết 中国 cho cùng một nước** — 仲国07 1361: JP 「仲国全土を探したら、中国の鉄道風景の、いろんなとこにちょっとずつ！」 (trong một câu có cả 仲国 lẫn 中国); TW gộp cả hai thành 仲國; VN cả hai đều "Trung Quốc". JP không giữ ranh giới cứng giữa 仲国/中国.
4. **Đa số hẹp nghiêng về "Trung Quốc"** (76 dòng / 83 lượt vs 72 / 77), và các file trục của route dùng nó: 仲国01 (24/24), 仲国06 (19/19), 仲国07 (21/21 sau audit).
5. **Cùng một chức danh, hai dạng** — 仲国02 2278 (Khương tự giới thiệu): "Thư ký Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trung Quốc." vs lr稀咲追加01 1860 (cùng chức danh, cùng người): "thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc". Cùng referent mà hai dạng — bắt buộc phải thống nhất.
6. **Đa số nội bộ từng file đã đi ngược nhau** — audit 仲国04 đổi 1857 "Trung Quốc"→"Zhongguo" "thống nhất theo 4 dòng còn lại trong file"; audit 仲国07 đổi 1255/1523/1743/2144 "Trọng Quốc"→"Trung Quốc" "thống nhất theo đa số nội bộ 17–4". Đa số cấp file không quyết được chuẩn toàn dự án — cần quyết định cấp dự án (chính là mục này).

**Vì sao KHÔNG chọn hai dạng kia:**
- "Trọng Quốc" (Hán-Việt của 仲国, song song với 冥国="Minh Quốc" đã chốt): là lập luận mạnh nhất cho phía đối lập, và cụm 仲国08 (34/34) + tsuika Kisaki (38) dùng nó nhất quán. Nhưng (a) các audit đã giữ "Trung Quốc" ngay trong những dòng họ đổi "Mỹ"→"Minh Quốc" (điểm 1) — dự án KHÔNG áp dụng logic Hán-Việt hư cấu một cách blanket cho tên nước trong thoại; (b) "Trọng Quốc" không có currency trong tiếng Việt (độc giả không hiểu ngay), trong khi "Trung Quốc" hiểu ngay; (c) cụm 仲国08 là dạng Gemini (audit 仲国08 chỉ sửa Ohitoyo, không đụng 仲国), không phải quy tắc đã chốt.
- "Zhongguo" (pinyin): hợp với phong cách pinyin của route Chikuni (北琴=Beiqin, 姜叶煌=Jiang Yehuang, 志寰=Zhihuan, 緑比車=Lü-pi-che, Kuai-su). Nhưng (a) không nước nào khác dùng pinyin (日ノ本=Hinomoto là romaji đã chốt; còn lại đều tên thật); (b) chính 仲国02 phá mẫu ở 2278 ("Quốc vụ viện Trung Quốc" giữa 27 dòng "Zhongguo"); (c) độc giả phải biết pinyin mới đọc được.

**Ngôn ngữ 仲国語 (13 dòng):** "tiếng Trung" 5 · "tiếng Trung Quốc" 4 (đều ở 仲国06, nhất quán với dạng tên nước của file đó) · "tiếng Zhongguo" 2 (仲国02 2897, 仲国03 2845) · dạng khác 2 (仲国06 1872 liệt kê "ngôn ngữ Hinomoto - Trung Quốc - Đức", không dùng chữ "tiếng"). Đề xuất: chỉ đổi 2 dòng "tiếng Zhongguo"→"tiếng Trung" (dạng chuẩn của tiếng Trung trong tiếng Việt, đa số 5+4 đều chứa "tiếng Trung"); giữ nguyên "tiếng Trung Quốc" (đúng tiếng Việt, nhất quán nội bộ file).

**Hai dòng romaji lẻ:**
- lr_日々姫ふかみh1 1689 "Nakakuni": JP không có furigana — "Nakakuni" là Gemini đọc sai (仲=naka + 国=kuni). → "Trung Quốc". (Lưu ý cross-item: dòng này còn "Ohimitera" cũ — thuộc T1, không quyết ở đây.)
- れいな03 2070 "nước Chukoku": JP có furigana [ちゅうごく,1]仲国 — VN roman hoá furigana. → "nước Trung Quốc". (TW bỏ hẳn tên nước ở đây; JP thắng TW.)

**ĐỀ XUẤT — T56: "Trung Quốc" cho tên nước 仲国 ở mọi dòng nhắc tên; 仲国語 → "tiếng Trung" chỉ ở 2 dòng đang là "tiếng Zhongguo".**
**Dòng bị ảnh hưởng: 124** (72 "Trọng Quốc"→"Trung Quốc" + 48 "Zhongguo"→"Trung Quốc" + 2 "Nakakuni"/"Chukoku"→"Trung Quốc" + 2 "tiếng Zhongguo"→"tiếng Trung"). Giữ nguyên: 76 dòng "Trung Quốc", 5 "tiếng Trung", 4 "tiếng Trung Quốc", 仲国06 1796.
**Độ tin cậy: Cao** (tiền lệ audit 1722 + ghi chú quy ước + JP tự dùng 中国 + đa số).

---

## T57. 詠国 → "Anh Quốc" vs "Eikoku" vs "Vịnh Quốc"

**Câu hỏi:** nước hư cấu 詠国 (đọc えいこく, chỉ Anh/UK) dịch thống nhất bằng dạng nào?

**Dòng đã đọc:** toàn bộ **16 dòng có JP 詠国** + 2 dòng katakana liên quan (ハチロク09 2102, ハチロク10 2024). Đếm theo dòng (CUR):

| Dạng hiện tại | Số dòng | Keys |
|---|---|---|
| "Anh" (dạng ngắn/ghép) | **8** | 2254 "nước Anh" · 2766 "người Anh" · 1580/2437 "kiểu Anh" · 1533 "của Anh" · 1587 "ở Anh" · 1818 "từ Anh" · 1722 "Anh" |
| "Eikoku (…)" | **4** | 1529 "Eikoku (Anh Quốc)" · 1687/1833/2533 "Eikoku (Vương quốc Anh)" |
| "Anh Quốc" | **2** | 1662 · 1905 |
| "Anh quốc" (thường q) | **1** | 3529 |
| "Vịnh Quốc" | **1** | 1848 |

**Bằng chứng:**
1. **Cùng tiền lệ audit như T56:** trong 5 dòng audit đổi "Mỹ"→"Minh Quốc" (2766, 1580, 2437, 1587, 1722), 詠国 được giữ nguyên dạng "Anh" ("người Anh", "kiểu Anh", "ở Anh", "Anh"). Auditor áp "Minh Quốc" cho 冥国 nhưng không đụng tới "Anh" — tức chuẩn ngầm của dự án cho 詠国 trong thoại là tên thật "Anh".
2. **Ghi chú ROUTE-AUDIT.md:431:** "詠国=Anh" (xem T56 — nhánh này được audit sau xác nhận).
3. **TW 英國 ở cả 16 dòng** (JP thắng TW khi lệch, nhưng ở đây TW và thực hành dự án đồng thuận).
4. **Audit ハチロク09 (REVIEW dòng 141)** tự đặt câu hỏi: "Key 1848 詠国 → 'Vịnh Quốc': giữ theo lối phiên âm như Minh Quốc; TW là 英國 (nước Anh). Hieu có muốn chuẩn hoá thành 'Anh Quốc' không?" — tức auditor cũng xem "Anh Quốc" là đích chuẩn hoá cho dạng đứng riêng.
5. **髑国 song song:** 10 dòng JP 髑国 → "Đức" 9 dòng; "Dokkoku" chỉ xuất hiện 1 lần, trong list 真闇03 1687. Dạng hư cấu chỉ sống sót trong list đó — cùng logic cho ngoại lệ 1687 dưới đây.

**ĐỀ XUẤT — T57: dạng chuẩn cho tên nước đứng riêng là "Anh Quốc"; giữ "Anh" ở các dạng ghép/ngắn; hai ngoại lệ giữ nguyên.**
- Đổi 5 dòng: 1848 "Vịnh Quốc"→"Anh Quốc" · 1529/1833/2533 "Eikoku (Vương quốc Anh)" / "Eikoku (Anh Quốc)"→"Anh Quốc" · 3529 "Anh quốc"→"Anh Quốc" (chuẩn hoá hoa chữ Q).
- Giữ nguyên 8 dòng dạng "Anh" (kiểu Anh / người Anh / nước Anh / của Anh / từ Anh / ở Anh / "Anh" trong list) — tiếng Việt tự nhiên, không cần đổi.
- **Ngoại lệ 1 — giữ nguyên 真闇03 1687** "Eikoku (Vương quốc Anh)": đây là một dòng liệt kê song song 5 nước đều ở dạng hư cấu + gloss — "Eikoku (Vương quốc Anh), Frank (Pháp), Dokkoku (Đức), Rankoku (Hà Lan), Ispania (Tây Ban Nha)". Chỉ đổi một mục sẽ phá vỡ cấu trúc song song của cả dòng; các mục kia (Frank/Dokkoku/Rankoku/Ispania) ngoài phạm vi T57. Ghi cờ: cả list 1687 là ứng viên cho một quyết định chung sau này.
- **Ngoại lệ 2 — giữ nguyên ハチロク09 2102** "Minh Quốc (Mỹ) hay Vịnh Quốc (Anh)": JP dùng katakana メーコク/エーコク (Olivy phát âm tên nước theo kiểu ngoại quốc) và VN ghép cặp hư cấu + gloss cho CẢ HAI nước. "Minh Quốc" đã chốt — cặp này phải khớp nhau (cùng hư cấu hoặc cùng thật); đổi một bên sẽ lệch cặp. (Dòng katakana tương tự ハチロク10 2024 "Minh Quốc (Nước Mỹ)" củng cố mẫu hư cấu + gloss cho cách đọc katakana.)
- **Dòng bị ảnh hưởng: 5** (1848, 1529, 1833, 2533, 3529).
**Độ tin cậy: Cao.**

---

## T58. 次元流 → "Thứ Nguyên Lưu" vs "Thị Hiện Lưu"

**Câu hỏi:** tên lưu phái kiếm 次元流 (đọc じげん) trong 凪ふかみ02 dịch là "Thứ Nguyên Lưu" (đọc theo chữ Hán 次元 = thứ nguyên/chiều) hay "Thị Hiện Lưu" (Hán-Việt của 示現流)?

**Dòng đã đọc:** toàn bộ **3 dòng có JP 次元流 trong toàn dự án**, đều ở 凪ふかみ02_凪の大会初挑戦！, hiện đều "Thứ Nguyên Lưu":
- 2280 (凪): JP 「そうばい！　壱刀流からバイ捨流ば産まれて、そのバイ捨流からまた産まれたのが、[じげん,1]次元流ばい！！」 — TW 「是咧！　體舍流源自一刀流，後續還演變出了示現流咧！！」 — CUR "Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu, rồi từ Thể Xá Lưu lại sinh ra Thứ Nguyên Lưu đó!!"
- 2377 (ふかみ): JP 「一太刀で相手を倒す、っていうのにすべてをかける剣術だよね？　[じげん,1]次元流」 — TW 「示現流就是在第一招傾盡全力，一擊斃敵的劍術流派，對吧？」 — CUR "Đó là môn kiếm thuật đặt cược tất cả vào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thứ Nguyên Lưu ấy."
- 3109 (monologue, Nagi): JP 「次元流！　知ってる！！」 — TW 「示現流！　這個我知道！！」 — CUR "Thứ Nguyên Lưu! Mình biết!!"

**Bằng chứng:**
1. **TW dùng 示現流 ở cả 3 dòng** — TW không dịch theo chữ Hán 次元 mà dịch theo referent thật.
2. **示現流 (Jigen-ryū) là lưu phái có thật** ở Satsuma (nay là Kagoshima, Kyushu), nổi tiếng vì đặt TẤT CẢ vào nhát chém đầu tiên — "a second strike is not even to be considered" (Wikipedia, "Jigen-ryū"). Đó chính xác là định nghĩa ở 2377 ("一太刀で相手を倒す…すべてをかける" — đặt cược tất cả vào một nhát chém hạ đối thủ). Nagi nói giọng Satsuma; lưu phái của Satsuma là 示現流.
3. **JP đánh furigana [じげん,1]** cho 次元流 ở 2280/2377 — tác giả cố tình đọc nó là "jigen", đồng âm với 示現流. Chữ đùa (pun) chỉ hoạt động khi độc giả nghe ra 示現流; "Thứ Nguyên Lưu" (chiều/thứ nguyên) giết chết chữ đùa và làm chuỗi dòng dõi 一刀流 → バイ捨流 → 次元流 thành vô nghĩa (một "lưu phái thứ nguyên" từ đâu ra?).
4. Chuỗi trong 2280 (Nhất Đao Lưu → Thể Xá Lưu → Thứ Nguyên/Thị Hiện Lưu) là chuỗi các lưu phái kiếm có thật/kiểu thật; TW dịch cả ba theo hướng đó (一刀流 · 體舍流 · 示現流).

**ĐỀ XUẤT — T58: "Thị Hiện Lưu" (Hán-Việt của 示現流) cho cả 3 dòng.**
**Dòng bị ảnh hưởng: 3** (2280, 2377, 3109 — đều ở 凪ふかみ02).
**Độ tin cậy: Cao.**

---

## T59. "Quirquitium" vs "Circuithium"

**Câu hỏi:** chất kết tinh キルクイティウム (trái tim động cơ Aero-Craftech) giữ dạng nào?

**Dòng đã đọc:** toàn bộ **6 dòng có JP キルクイティウム** trong toàn dự án:
- 共通04_キハ07。ポーレットとれいな (good-set 03_Paulette) ×5, đều "Quirquitium": 2520 ("…là một hợp chất dạng đá quý có tên là Quirquitium."), 2105 ("Tuy nhiên, Quirquitium có một điểm yếu."), 2304 ("Nếu để các Quirquitium lại quá gần nhau…"), 2629 ("…việc tập trung Quirquitium lại để sử dụng…"), 2240 ("…chi phí sản xuất Quirquitium…").
- 日々姫10_稀咲の未来図、日々姫の未来図 2458 ×1, "Circuithium": JP 「ええ。エアロ＝クラフテック機関の心臓部である、キルクイティウムの精製には豊富な真水が必要ですから」 — TW 「嗯。要精煉空凝機引擎的心臟"鐶"必須要用到大量淡水」 — CUR "Vâng. Để tinh chế Circuithium, trái tim của động cơ Aero-Craftech, thì cần một lượng lớn nước ngọt."

**Bằng chứng:**
1. **5–1.** File 共通04 đã thống nhất nội bộ 5/5 "Quirquitium" trong audit (ROUTE-AUDIT.md:515: "キルクイティウム thống nhất 'Quirquitium' 5/5 trong file").
2. **LOGIC-DICH-VA-SUA.md P.13** liệt kê "thống nhất 'Quirquitium'" trong các đề xuất chờ chốt — hướng đã định sẵn là Quirquitium.
3. **TW 鐶 không giúp roman hoá** (TW dùng một chữ Hán hiếm làm tên chất, không cho dạng Latinh).
4. **Không có dạng tiếng Anh chính thức nào để đối chiếu:** tìm trên web (Wikipedia/MobyGames/Steam/PlayStation cho Maitetsu / Maitetsu: Pure Station / Last Run!!) không thấy "Quirquitium" hay "Circuithium" ở đâu; bản Anh của Sekai Project dùng các thuật ngữ hư cấu roman hoá (Aircra, Raillord, Hinomoto, Ohitoyo) nhưng không có dạng attested cho từ này.
5. **Cả hai đều không phải Hepburn** (キルクイティウム → Kirukuitiumu). "Kirukuitium" không phải một trong hai phương án và đổi 6 dòng cũng không đem lại lợi ích trong dự án. "Circuithium" trông như ghép "circuit" + "lithium" (chất này là hợp chất dạng đá quý, không liên quan lithium) — khả năng cao là Gemini bịa theo âm.

**ĐỀ XUẤT — T59: "Quirquitium" cho cả 6 dòng.**
**Dòng bị ảnh hưởng: 1** (日々姫10 2458 "Circuithium"→"Quirquitium").
**Độ tin cậy: Cao.**

---

## T60. 頭取 → "Chủ tịch" vs "Tổng giám đốc" vs "Giám đốc"

**Câu hỏi:** chức danh 頭取 của Houshou Mototada (người đứng đầu Ngân hàng Kumamoto 隈元銀行) dịch thống nhất bằng gì?

**Dòng đã đọc:** toàn bộ **29 dòng có JP 頭取**. Đếm theo dòng (CUR):

| Dạng hiện tại | Số dòng | Keys |
|---|---|---|
| "Chủ tịch" | **16** | 共通14 1882/1884/1551/1112/2708/1972/2200 (7) · ハチロク14 1731 · ハチロク15 1759/2059 · ポーレット09 2161/2131 · グランド06 3319/3338 · 稀咲01 1887/1256 (2, audit-fix từ chuỗi lệch dòng) |
| "Giám đốc" / "giám đốc ngân hàng" | **11** | ハチロク01 1676/2138 · ハチロク12 2364/2874 · 日々姫01 1996/1805 · 日々姫06 2897 "Giám đốc Houshou" · 真闇h3 2469 · グランド01 2523 · グランド08 2052 · 稀咲h1 1416 |
| "Tổng giám đốc" | **2** | 共通11 2696/3448 |

**Nhân vật + TW:** tất cả 29 dòng đều chỉ một người — 宝生元忠, 頭取 của 隈元銀行. TW dùng **行長 ở cả 29 dòng** (không bao giờ dùng 董事長 = chủ tịch HĐQT).

**Bằng chứng:**
1. **JP 頭取 = president của ngân hàng** (người điều hành cao nhất; khác với 会長 = chairman). TW 行長 = president/CEO của ngân hàng. Tương đương chức năng trong tiếng Việt là **"Tổng giám đốc"** (người điều hành ngân hàng), không phải "Chủ tịch" (chủ tịch HĐQT).
2. **Va chạm với 会長:** 会長 đã được dịch "Chủ tịch" và đã merge — グランド06 2933: 「頭部と臍部の、両会長だ。」→ "Hai vị chủ tịch của Tobu và Seibu." Nếu 頭取 cũng là "Chủ tịch", hai chức danh JP khác nhau sẽ trùng một dạng VN.
3. **Va chạm với 社長:** 社長 đã được dịch "giám đốc" toàn dự án (vd. Paulette là 社長 của Đường sắt Ohitoyo → "giám đốc"; T61 2189 Mayami làm 社長 của holding → "do chị Mayami làm giám đốc"). Nếu 頭取 cũng là "Giám đốc", người đứng đầu ngân hàng sẽ trùng chức danh với chủ tịch công ty đường sắt — mờ cấp bậc.
4. **Tiền lệ giới thiệu chính thức:** lần đầu giới thiệu vai trò của ông (共通11 2696: 「計画の主導者は多分、隈元銀行頭取で、…宝生元忠さんですけど」) đã dùng "tổng giám đốc Ngân hàng Kumamoto"; 3448 cũng vậy ("tổng giám đốc của một ngân hàng lớn").
5. Các dạng xưng hô/đối lập đều hoạt động tốt với "Tổng giám đốc": 1882 "Kính chào ngài tổng giám đốc." · 1731 "Không phải nói với bố, mà là với Tổng giám đốc." · 3319/3338 "Không phải là Tổng giám đốc, mà là Bố." · 2059 "Nhưng ở tầm Tổng giám đốc thì đúng là khác biệt." · 2052 "…rủi ro bị mất chức Tổng giám đốc Ngân hàng Kumamoto."

**Lập luận đối lập (ghi nhận):** "Chủ tịch" đang là đa số (16/29) và nghe tự nhiên trong tiếng Việt khi gọi người đứng đầu ngân hàng. Nhưng đa số này tập trung ở Common 14 (7 dòng, một auditor) + vài file — là lựa chọn của auditor, không phải quy tắc đã chốt; và nó va chạm trực tiếp với 会長→"Chủ tịch" (điểm 2). Nếu Hieu thích "Chủ tịch" hơn vì tự nhiên, phương án dự phòng là đổi 13 dòng còn lại về "Chủ tịch" — nhưng khuyến nghị chính vẫn là "Tổng giám đốc" vì đúng chức năng + không va chạm.

**ĐỀ XUẤT — T60: "Tổng giám đốc" (kèm "ngân hàng" / "Ngân hàng Kumamoto" / "Ngân hàng Kumagin" theo ngữ cảnh từng dòng như hiện tại).**
**Dòng bị ảnh hưởng: 27** (16 "Chủ tịch" + 11 "Giám đốc"/"giám đốc ngân hàng" → "Tổng giám đốc"; 2 dòng 共通11 đã đúng).
**Độ tin cậy: Cao** (về độ chính xác chức năng; rủi ro chính là Hieu có thể chuộng "Chủ tịch" vì quen tai — xem lập luận đối lập trên).

---

## T61. 持株会社 → "công ty cổ phần" vs "công ty holding"

**Câu hỏi:** 持株会社 (holding company) dịch là gì? Hiện toàn dự án đang dùng "công ty cổ phần" ở 7/10 dòng.

**Dòng đã đọc:** toàn bộ **10 dòng có JP 持株会社**:
- ハチロク09_採決 ×5 (1549, 2131, 2189, 2143, 1536) — đều "công ty cổ phần".
- ハチロク12_再開発 ×3 (2258, 2381, 1699) — đều đã được audit sửa thành **"công ty holding"**.
- ハチロク15_家族 1953, れいな03_しゅっぱつしんこう 1568 — "công ty cổ phần".

**Bằng chứng:**
1. **JP 持株会社 = holding company** (công ty nắm giữ cổ phần của các công ty con). **TW 控股公司 ở 9/10 dòng** (chỉ 1953 TW viết 股份公司 là sai theo JP; JP thắng TW).
2. **"Công ty cổ phần" là sai khái niệm:** đó là 株式会社 (joint-stock company). Các công ty đường sắt trong truyện vốn đã là công ty cổ phần; điểm của 持株会社 là cấu trúc holding — công ty mẹ tập hợp các công ty con mà vẫn giữ tính độc lập của chúng. Chính các dòng trong truyện định nghĩa điều đó: 2143 「経営の集約をしつつ独立性も維持できるのが持株会社だ」("Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty [holding]."); 2189 「真闇姉を社長とする持株会社を、それぞれの酒蔵を束ねる、親会社として設立する」("…công ty [holding] do chị Mayami làm giám đốc, với tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại").
3. **Tiền lệ audit đã merge:** audit ハチロク12 đã sửa cả 3 dòng của file đó sang "công ty holding" — tức hướng này đã được một auditor áp dụng và parent kiểm chứng xong.
4. "Công ty holding" là thuật ngữ kinh doanh chuẩn trong tiếng Việt (luật Doanh nghiệp dùng "công ty mẹ/công ty holding" cho mô hình này).

**ĐỀ XUẤT — T61: "công ty holding" cho cả 10 dòng.**
**Dòng bị ảnh hưởng: 7** (ハチロク09 ×5, ハチロク15 1953, れいな03 1568). 3 dòng ハチロク12 đã đúng.
**Độ tin cậy: Cao.**
*(Ghi chú ngoài phạm vi: fix audit ở ハチロク12 2381 đã làm mất ký tự xuống dòng `\n` trong giá trị (TOML-2 flatten) — không thuộc T61, ghi lại để batch khác xem xét nếu cần.)*

---

## T62. 民由連 → "Đảng Dân Do" vs "Đảng Dân Hữu"

**Câu hỏi:** tên đảng/phái hư cấu 民由連 dịch là gì?

**Dòng đã đọc:** chỉ **1 dòng** có JP 民由連 trong toàn dự án — ハチロク09_採決 2411 (議長, trong phiên họp biểu quyết):
- JP: 「この[さい]際、関連の質疑に入ります。\n[みんゆうれん,2]民由連、斉藤委員」
- TW: 「那麼藉此場合提出對本方案的疑問。請民友連的齋藤委員提問」
- CUR: 「Nhân dịp này, chúng ta sẽ bước vào phần hỏi đáp liên quan.\nỦy viên Saitou của Đảng Dân Do.」
- Dòng kề xác nhận bối cảnh hội đồng biểu quyết (2409 Soutetsu về ngân sách; 2412 Soutetsu về Aircra; 2415 中堅議員 về chức thị trưởng).

**Bằng chứng:**
1. **JP là chuẩn (JP thắng TW):** JP viết 民由連, furigana みんゆうれん. TW viết 民友連 — 由 (yū) và 友 (yū) đồng âm trong tiếng Nhật, TW đọc nhầm hoặc chuẩn hoá nhầm. JP 民由 = "dân do" (民=dân, 由=do); 民友 mới là "dân hữu" (bạn của dân).
2. **Không có dòng JP 民友連 nào** trong toàn CSV3 (grep: 1 lượt "民友連" duy nhất — chính là trường TW của dòng 2411 này).
3. "Đảng" phù hợp bối cảnh: 議長 mời "Ủy viên Saitou của Đảng Dân Do" chất vấn trong phiên họp — một đảng/phái trong hội đồng.

**ĐỀ XUẤT — T62: GIỮ NGUYÊN "Đảng Dân Do".**
**Dòng bị ảnh hưởng: 0.**
**Độ tin cậy: Cao.**

---

## T63. 帝有鉄道 → ?

**Câu hỏi:** tên đầy đủ của đường sắt đế quốc 日ノ本帝有鉄道 (mà 帝鉄 là tên viết tắt) dịch là gì? List ghi "câu hỏi cho Hieu" — nhưng điều tra và đề xuất theo uỷ quyền.

**Dòng đã đọc:** toàn bộ **7 dòng có JP 帝有**:
- Tên đầy đủ 日ノ本帝有鉄道 ×5: グランド10 1134 · 日々姫01 1789 (JP viết 日ノ本帝有鐵道, chữ 鐵 truyền thống) · 日々姫02 60 · 仲国03 2248 · 仲国03 2082.
- Động từ/tính từ 帝有化 (quốc hữu hoá) ×2: ハチロク03 2337, 日々姫02 1727 — đều "quốc hữu hóa", đúng, không đổi.

| Dạng hiện tại (tên đầy đủ) | Số dòng | Keys |
|---|---|---|
| "Đường sắt Đế quốc Hinomoto" | **1** | 1134 (audit-fix) |
| "Đường sắt Đế hữu Hinomoto" | **2** | 2082, 2248 |
| "Đường sắt Hoàng gia Hinomoto" | **2** | 1789, 60 |

Chi tiết từng dòng:
- 1134 (monologue): JP 「……旧帝鉄、日ノ本帝有鉄道の懐中時計。」 — TW 「……這是一隻前帝國鐵路，帝家日本國鐵路的懷表。」 — CSV3 "……Đồng hồ bỏ túi của Đường sắt Hoàng gia cũ, Đường sắt Hoàng gia Hinamoto." → **audit-fix (đã merge): "……Đồng hồ bỏ túi của Teitetsu cũ, Đường sắt Đế quốc Hinomoto."**
- 1789 (双鉄): JP 「『日ノ本帝有鐵道、蒸気機関車設計図面集』」 — TW 「《帝家日本國鐵路蒸汽機車設計圖集》」 — CUR "『Đường sắt Hoàng gia Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』".
- 60 (monologue, 日々姫02): JP 「\x%l明智;#00ffc040;明智%l;#;三十九年。鉄道帝有法制定。布告。\n日ノ本帝有鉄道発足。」 — TW 「…鐵路國有法制定，頒布。帝家日本國鐵路成立。」 — CUR "Năm Meiji thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\nĐường sắt Hoàng gia Hinomoto chính thức ra đời."
- 2248 (日々姫): JP 「日ノ本帝有鉄道のオーナー、[ヒノモトノミカド,3]日ノ本帝から、ミカドって愛称になったと！？」 — TW 「由於帝家日本國鐵路的所有人是日本國[米卡多]帝…」 — CUR "Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado), để đặt biệt danh là Mikado sao!?" (Dòng này cũng là nguồn gốc biệt danh "Mikado" của đầu máy — chủ sở hữu đường sắt là chính Hoàng đế Hinomoto.)
- 2082 (西瓜): JP 「老師の日ノ本帝有鉄道――帝鉄への接し方は、確かに研究でしたけれど…」 — TW 「師父對於帝家日本國鐵路——對於帝國鐵路確實是抱以研究的態度…」 — CUR "Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia, đúng là nghiên cứu, nhưng không chỉ có vậy…"

**Bằng chứng:**
1. **Gloss đã chốt cho 帝鉄 (AUDIT-BRIEF:12):** 帝鉄 = "Teitetsu", dạng đầy đủ là **"Đường sắt Đế quốc"** (chỉ dùng trong tooltip %l ở lần xuất hiện đầu). Vì 帝鉄 chính là viết tắt của 日ノ本帝有鉄道, tên đầy đủ mở rộng nhất quán là "Đường sắt Đế quốc Hinomoto".
2. **Tiền lệ audit đã merge:** fix ở グランド10 1134 đổi cả hai vế về đúng chuẩn này trong cùng một dòng — 旧帝鉄→"Teitetsu cũ" + 日ノ本帝有鉄道→"Đường sắt Đế quốc Hinomoto". Auditor đã nghĩ tới tính nhất quán 帝鉄/帝有鉄道 khi fix.
3. **TW 帝國鐵路** ("Đường sắt Đế quốc") cho 帝鉄/帝有鉄道 ở 1134, 2082 (và 帝家日本國鐵路 cho tên đầy đủ ở 1789/2248/60 — "Đường sắt [nhà] Đế Hinomoto", cùng họ nghĩa với "Đế quốc", không phải "Hoàng gia").
4. **"Đế hữu"** (2 dòng, Gemini): Hán-Việt từng chữ 帝+有 = "của Đế sở hữu" — đúng từng chữ nhưng không có currency trong tiếng Việt, nghe như calque; không có dòng nào khác trong dự án dùng "Đế hữu".
5. **"Hoàng gia"** (2 dòng + nửa sau của 2082): là dạng đã bị cấm cho 帝鉄 ("Đường sắt Hoàng gia" banned 19/11). Dùng nó cho tên đầy đủ của cùng một đường sắt sẽ tái tạo đúng dạng cấm. (Nửa sau của 2082 — 帝鉄 → "Đường sắt Hoàng gia" — là lỗi phạm vi T1/帝鉄, ghi cờ ở dưới, không tính vào T63.)

**Tên đạo luật trong key 60 (鉄道帝有法):** JP 鉄道帝有法; TW 鐵路國有法. Đây là bản tương tự trong thế giới truyện của đạo luật 国有 hoá đường sắt thật của Nhật (鉄道国有法, năm Meiji 39 = 1906 — đúng niên hiệu trong dòng). Đề xuất đi kèm tên công ty: **"Đạo luật Đường sắt Đế quốc"** (chỉ đổi "Hoàng gia"→"Đế quốc", giữ nguyên cấu trúc câu hiện tại). Phương án khác là "Luật Quốc hữu Đường sắt" (sát TW hơn) — nhưng sẽ lệch với tên công ty "Đường sắt Đế quốc"; độ tin cậy cho tên luật này chỉ Trung bình.

**ĐỀ XUẤT — T63: "Đường sắt Đế quốc Hinomoto" cho 日ノ本帝有鉄道; "Đạo luật Đường sắt Đế quốc" cho 鉄道帝有法 (key 60).**
**Dòng bị ảnh hưởng: 4** (1789, 60, 2082, 2248). 1134 đã đúng. 2337/1727 ("quốc hữu hóa" cho 帝有化) giữ nguyên.
**Độ tin cậy: Cao** (tên công ty); Trung bình (tên đạo luật trong key 60).
**Cờ cross-item:** 2082 nửa sau 帝鉄→"Đường sắt Hoàng gia" cần sửa thành "Teitetsu" — thuộc phạm vi T1/帝鉄, không phải T63.

---

## T64. 冥語 → "tiếng Minh Quốc" vs TW 英語

**Câu hỏi:** 冥語 (ngôn ngữ của Minh Quốc = tiếng Anh của người Mỹ) dịch là gì?

**Dòng đã đọc:** chỉ **1 dòng** có JP 冥語 trong toàn dự án — ハチロク05_レイルロオドたち key 3512 (monologue; **list ghi "凪ふかみ05 3512" là sai file — không có key 3512 nào ở 凪ふかみ05**):
- JP: 「冥語の鋭い叫びとともに、差し伸べられたハチロクの手がはねのけられる。」
- TW: 「奧莉薇邊用英語尖叫著，邊推開了八六伸過來的手。」
- CSV3: "（Cùng với tiếng thét chói tai bằng tiếng Mỹ, cô ấy hất văng bàn tay đang chìa ra của Hachiroku.）"
- **CUR (audit-fix đã merge): "（Cùng với tiếng thét chói tai bằng tiếng Minh Quốc, cô ấy hất văng bàn tay đang chìa ra của Hachiroku.）"**
- Dòng kề (3510–3514): Olivy cười rạng rỡ, lùi nửa bước, ôm đầu, rồi thét lên đẩy tay Hachiroku ra — cô là Railord người Mỹ (冥国), tiếng thét bằng tiếng Anh trong thế giới thật.

**Bằng chứng:**
1. **Audit ハチロク05 đã sửa sẵn:** "tiếng Mỹ"→"tiếng Minh Quốc" (merged). Quyết định này trùng khớp hoàn toàn với đề xuất độc lập dưới đây — T64 thực chất đã được quyết + áp trong audit.
2. **Tiền lệ 日ノ本語:** 40 dòng JP 日ノ本語 → CUR "tiếng Hinomoto" 38 dòng, **0 lần "tiếng Nhật"**. Dự án KHÔNG BAO GIỜ bản địa hoá tên ngôn ngữ hư cấu thành tên thật. 冥語 phải theo cùng quy tắc → "tiếng Minh Quốc".
3. **冥国="Minh Quốc" đã chốt** — tên ngôn ngữ đi theo tên nước.
4. **TW 英語 là TW bản địa hoá theo thế giới thật** (JP thắng TW). "Tiếng Anh" sẽ phá mẫu 日ノ本語→"tiếng Hinomoto".
5. **"Tiếng Mỹ" (CSV3 cũ) sai hai mặt:** không có ngôn ngữ nào tên "tiếng Mỹ" (tiếng của người Mỹ là tiếng Anh); và phá mẫu tên hư cấu.

**ĐỀ XUẤT — T64: "tiếng Minh Quốc" — ĐÃ ĐƯỢC ÁP DỤNG TRONG AUDIT, đợt thống nhất chỉ cần GIỮ NGUYÊN.**
**Dòng bị ảnh hưởng: 0** (3512 đã là "tiếng Minh Quốc").
**Độ tin cậy: Cao.**

---

## T65. 橙汁 → "nước cam" vs "Trừng trấp"

**Câu hỏi:** 橙汁 (cách viết kiểu Trung của "nước cam") dịch là "nước cam" hay giữ Hán-Việt "Trừng trấp"?

**Dòng đã đọc:** toàn bộ **3 dòng có JP 橙汁**:
- 仲国01_副丘→北琴 1828 (日々姫): JP 「あ、日ノ本語喋れるアテンダントさん！\nうふふ、嬉しか！　じゃ、私は橙汁！　もう一杯！」 — TW 「啊，是會說日語的空服！太好咧！那我要再來一大杯橙汁！」 — CUR "A, cô tiếp viên nói được tiếng Hinomoto!\nUfufu, vui quá! Vậy, cho tôi một ly Trừng trấp! Một ly nữa!"
- 仲国01 2089 (日々姫): JP 「それに、パッケージとかはもう異国やけん！\nオレンジジュースば『橙汁』って、面白かとよねー」 — TW 「而且這些包裝都是外國版的咧！"橙汁"的這個寫法也很有趣不是嗎」 — CUR "Với lại, bao bì thì đậm chất nước ngoài luôn rồi!\nNước cam mà gọi là 『Trừng trấp』, thú vị ghê nhỉ~"
- 仲国08_謝謝再見！ 2054 (日々姫): JP 「あとね、ご褒美。んっと……橙汁！\n自販機のでいいから、買ってほしかと」 — TW 「還有，我要獎勵！我想想……就橙汁吧！自動販賣機的也可以，幫我買一瓶吧」 — CUR "Với lại, phần thưởng. Ừm…… nước cam!\nMua ở máy bán hàng tự động cũng được, anh mua cho em nha."

**Bằng chứng:**
1. **2089 là dòng đùa (joke) và nó CẦN dạng lạ:** Hibiki bình luận về cách viết 『橙汁』 trên bao bì — cô thấy cách viết đó thú vị. VN hiện tại đã vận hành đúng trò đùa: "Nước cam mà gọi là 『Trừng trấp』, thú vị ghê nhỉ~" — câu này tự giải thích ("Trừng trấp" = nước cam) đồng thời giữ lại cảm giác lạ. Đổi 2089 thành "nước cam" sẽ giết chết trò đùa (câu thành "Nước cam mà gọi là 'nước cam', thú vị ghê" — vô nghĩa).
2. **1828 cùng cảnh, cùng trò đùa:** trên cùng chuyến bay, Hibiki gọi đồ uống bằng đúng từ cô thấy trên bao bì ("cho tôi một ly Trừng trấp!"). Giữ "Trừng trấp" để trò đùa chạy xuyên suốt cảnh.
3. **2054 là yêu cầu thường, không có trò đùa:** dòng kề (2050–2055) là các bài phát biểu chia tay (Soutetsu cảm nhận về đường sắt Trọng Quốc/Trung Quốc, Suika, Khương đáp lời) — Hibiki chỉ xin phần thưởng là nước cam ở máy bán hàng tự động. Không có bao bì, không có chữ viết lạ. "Nước cam" là đúng.
4. **"Trừng trấp" cố tình khó hiểu** — đúng như 橙汁 đối với độc giả Nhật (cách viết kiểu Trung, lạ tai). Tính mờ (opacity) là một phần của trò đùa, và dòng 2089 tự làm rõ nghĩa cho độc giả.

**ĐỀ XUẤT — T65: quy tắc giữ-biến thể (keep-variant), KHÔNG thống nhất một dạng:**
- "Trừng trấp" ở 仲国01 1828 + 2089 (các dòng đùa về bao bì/chữ viết).
- "nước cam" ở các yêu cầu thường (仲国08 2054).
**Dòng bị ảnh hưởng: 0** (cả ba dòng đã đúng dạng theo quy tắc này).
**Độ tin cậy: Cao.**

---

## T66. 九国 → "chín tỉnh" vs "chín vùng"

**Câu hỏi:** 九国 trong 九洲九国 (chín nước/cựu phiên của Kyushu) dịch là "chín tỉnh" hay "chín vùng"?

**Dòng đã đọc:** toàn bộ **6 dòng có JP 九国**, đều trong cụm 九洲九国 (khái niệm tàu Nine Stars: chín phòng, mỗi phòng một cựu quốc của Kyushu):
- グランドリライト07_真闇 2546 (双鉄): JP 「リレートレイン・ナインスターズ。\n九洲九国を、九つの客室で周遊する観光列車」 — TW 「接力列車·九星。擁有九間客房，周遊九州九國的觀光列車」 — CUR "«Relay Train Nine Stars… Chuyến tàu du lịch dạo quanh chín vùng Kyushu với chín khoang hành khách.»"
- グランドリライト07_真闇 2545 (双鉄): JP 「ナインスターズは、九洲九国を九日間かけ、ゆったりと贅沢に周遊していく」 — TW 「按照我的想法，九星會耗時九天，奢華而悠閒地周遊九州九國」 — CUR "«Nine Stars sẽ dành chín ngày để dạo quanh chín vùng Kyushu, một chuyến du ngoạn thong thả và xa hoa.»"
- グランドリライト08_ふかみ 2711 (monologue): JP 「ナインスターズ客車各室が九洲九国であるならば、関門海峡を渡り、それぞれの部屋に向かうべき。」 — CUR "Nếu mỗi phòng trên toa khách Nine Stars là một trong chín tỉnh của Kyushu, thì hành khách nên băng qua Eo biển Kanmon rồi mới tiến vào từng phòng."
- グランドリライト08_ふかみ 2496 (monologue): JP 「――九洲九国。それぞれの国を、それぞれの客室に。\nこのコンセプトは、どの主要都市にも受け入れられた。」 — CUR "――Kyushu chín tỉnh. Mỗi tỉnh một phòng khách.\nÝ tưởng này đã được tất cả các thành phố lớn chấp thuận."
- グランド11_ナインスターズ！ 3231 (monologue): JP 「九洲九国をそれぞれの客室に当てはめた、その名も九洲な、[きゅうじゅう,1]90系客車群。」 — CUR "Nhóm toa hành khách dòng 90 mang đậm chất Kyushu, với mỗi phòng khách tượng trưng cho chín tỉnh của Kyushu."
- グランド11_ナインスターズ！ 2265 (ポーレット): JP 「緊張しました～。[きゅうしゅうきゅうこく,3]九洲九国、[ゆかり]縁の殿様の末裔たちに、九洲[ななけん,1]七県の知事がずらりと勢揃いですから」 — TW 「可緊張死我了。畢竟九州九國各位領主的後裔、九州七縣的知事都齊聚一堂」 — CUR "«Em hồi hộp lắm~. Con cháu của các vị lãnh chúa có liên quan đến chín tỉnh Kyushu, cùng thống đốc của bảy tỉnh Kyushu đều tề tựu đông đủ mà.»"

**Bằng chứng:**
1. **Đa số 4/6 đã là "chín tỉnh"**, gồm cả 2 dòng Grand 11 (phạm vi của mục này trong list).
2. **九国 = chín cựu quốc (kuni) của Kyushu** (Chikuzen, Chikugo, Buzen, Bungo, Hizen, Higo, Hyūga, Ōsumi, Satsuma) — "tỉnh" là cách dịch chuẩn trong tiếng Việt cho một đơn vị hành chính–lãnh thổ cũ kiểu này (bản thân "Kyushu" nghĩa là "chín tỉnh"). "Vùng" (region) mơ hồ hơn và mất nghĩa đơn vị hành chính.
3. **2265 đặt 九国 cạnh 七県 trong cùng một câu** — cả hai đều dịch "tỉnh" vẫn đọc tự nhiên ("chín tỉnh… bảy tỉnh"); sự khác biệt cựu quốc / huyện hiện đại được ngữ cảnh gánh (con cháu lãnh chúa vs thống đốc), không cần đổi từ.
4. 九州 được giữ nguyên "Kyushu" khắp nơi — không thuộc phạm vi mục này.

**ĐỀ XUẤT — T66: "chín tỉnh" cho 九国.**
**Dòng bị ảnh hưởng: 2** (グランドリライト07_真闇 2545, 2546 "chín vùng"→"chín tỉnh").
**Độ tin cậy: Cao.**

---

## Bảng tổng hợp

| Mục | Dạng đề xuất | Độ tin cậy | Dòng bị ảnh hưởng |
|---|---|---|---|
| T56 仲国 | **"Trung Quốc"** (tên nước); 仲国語 → "tiếng Trung" chỉ ở 2 dòng "tiếng Zhongguo" | Cao | **124** (72 Trọng→Trung + 48 Zhongguo→Trung + 2 Nakakuni/Chukoku→Trung + 2 tiếng Zhongguo→tiếng Trung) |
| T57 詠国 | **"Anh Quốc"** (đứng riêng); giữ "Anh" ở dạng ghép; giữ nguyên 1687 + 2102 (ngoại lệ) | Cao | **5** (1848, 1529, 1833, 2533, 3529) |
| T58 次元流 | **"Thị Hiện Lưu"** | Cao | **3** (2280, 2377, 3109) |
| T59 キルクイティウム | **"Quirquitium"** | Cao | **1** (日々姫10 2458) |
| T60 頭取 | **"Tổng giám đốc"** | Cao | **27** (16 "Chủ tịch" + 11 "Giám đốc") |
| T61 持株会社 | **"công ty holding"** | Cao | **7** |
| T62 民由連 | **GIỮ "Đảng Dân Do"** | Cao | **0** |
| T63 帝有鉄道 | **"Đường sắt Đế quốc Hinomoto"** (+ "Đạo luật Đường sắt Đế quốc" ở key 60) | Cao (Trung bình cho tên luật) | **4** (1789, 60, 2082, 2248) |
| T64 冥語 | **"tiếng Minh Quốc" — đã áp trong audit, giữ nguyên** | Cao | **0** |
| T65 橙汁 | **Giữ-biến thể:** "Trừng trấp" (1828/2089) · "nước cam" (2054) | Cao | **0** |
| T66 九国 | **"chín tỉnh"** | Cao | **2** (2545, 2546) |
| **Tổng** | | | **173 dòng** |

## Ghi chú cho người điều phối (coordinator)

1. **Hai mục đã xong một nửa trong audit, chỉ cần xác nhận:** T64 (3512 đã là "tiếng Minh Quốc") và một phần T61 (3/10 dòng đã là "công ty holding"), T63 (1134 đã là "Đường sắt Đế quốc Hinomoto"). Đừng sửa lại những dòng này.
2. **Quyết định gây tranh cãi nhất:** T60 ("Tổng giám đốc" vs "Chủ tịch" 16 dòng). Bằng chứng chức năng + va chạm 会長/社長 ủng hộ "Tổng giám đốc", nhưng nếu Hieu chuộng "Chủ tịch" vì quen tai thì phương án dự phòng tốn 13 dòng. Đáng hỏi Hieu riêng mục này nếu coordinator không chắc.
3. **Cờ cross-item (không thuộc T56–T66, ghi lại để batch khác xử lý):**
   - lr_日々姫ふかみh1 1689 còn "Ohimitera" cũ (T1).
   - 仲国03 2082 nửa sau: 帝鉄 → "Đường sắt Hoàng gia" (dạng cấm; T1 → "Teitetsu").
   - 真闇03 1687: cả list 5 nước hư cấu (Eikoku/Frank/Dokkoku/Rankoku/Ispania) là ứng viên cho một quyết định chung sau này; T57 chỉ giữ nguyên mục Eikoku trong đó.
   - ハチロク12 2381 (T61): fix audit làm mất `\n` trong giá trị (TOML-2 flatten) — xem xét khi ráp TOML block.
4. **Không có mục nào trong 11 mục cần park chờ kiểm tra trong game (B19) hay chờ sở thích cá nhân của Hieu** — mọi mục đều quyết được từ JP + TW + tiền lệ audit đã merge, theo uỷ quyền 21/11. Ngoại trừ lưu ý ở (2) về T60 nếu coordinator muốn Hieu chốt lại.
5. **Không sửa file nào khác.** Không đụng ROUTE-UNIFICATION.md, MEMORY.md, hay bất kỳ file audit/moans nào. Không spawn subagent.

---

## Phụ lục — toàn bộ dòng liên quan (JP / TW / VN CSV3 / CUR)

Các phụ lục dưới đây liệt kê MỌI dòng đã đọc cho từng mục, ở dạng giá trị hiện tại (CUR = moan fix > audit fix > VN CSV3 good-set). `src` = nguồn của CUR (csv3 / audit / moan).

### Phụ lục T56 — 仲国 (204 dòng)

--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1611 | char=ハチロク | src=audit
JP: 「うふふっ。そうしたお気付きもまた、\n仲国にこなければ得られなかったものかもしれませんね」
TW: 「嘻嘻，要不是這次仲國之旅，您或許還未必能注意到這一點呢」
VN(csv3): 「Fufu. Những nhận thức như vậy,\ncó lẽ nếu không đến Trung Quốc thì ngài đã chẳng thể có được nhỉ.」
CUR: 「Ufufu. Những nhận thức như vậy,\ncó lẽ nếu không đến Trung Quốc thì ngài đã chẳng thể có được nhỉ.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2397 | char=monologue | src=csv3
JP: 姜さんが、志寰君と、なにやら仲国語で打ち合わせ始める。\nすぐさま西瓜が、通訳・補足してくれる。
TW: 姜小姐和志寰開始用仲文商量了起來。而一旁的西瓜便把他們的對話翻譯、解釋給我們。
VN(csv3): Cô Khương và Chí Hoàn bắt đầu bàn bạc điều gì đó bằng tiếng Trung Quốc.\nNgay lập tức, Tây Qua đã dịch và giải thích lại cho chúng tôi.
CUR: Cô Khương và Chí Hoàn bắt đầu bàn bạc điều gì đó bằng tiếng Trung Quốc.\nNgay lập tức, Tây Qua đã dịch và giải thích lại cho chúng tôi.
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1994 | char=双鉄 | src=csv3
JP: 「パンダというのは、\n仲国でもやはり人気のある動物なのですか？」
TW: 「要說這熊貓，在仲國果然也是廣受喜愛的動物嗎？」
VN(csv3): 「Gấu trúc,\nở Trung Quốc cũng là một loài động vật rất được yêu thích sao?」
CUR: 「Gấu trúc,\nở Trung Quốc cũng là một loài động vật rất được yêu thích sao?」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2007 | char=西瓜 | src=csv3
JP: 「そうですね。パンダの赤ちゃんを抱っこ出来る施設は、\n仲国全土で。つまり世界中でここ一箇所と聞いています」
TW: 「說得沒錯，能夠抱熊貓寶寶的地方，放眼全仲國，或者說放眼全世界，也僅此一家別無分號」
VN(csv3): 「Đúng vậy ạ. Cơ sở cho phép bế gấu trúc con,\nnghe nói trên toàn Trung Quốc, hay nói cách khác là trên toàn thế giới, chỉ có duy nhất một nơi này thôi.」
CUR: 「Đúng vậy ạ. Cơ sở cho phép bế gấu trúc con,\nnghe nói trên toàn Trung Quốc, hay nói cách khác là trên toàn thế giới, chỉ có duy nhất một nơi này thôi.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2237 | char=monologue | src=csv3
JP: また仲国語での打ち合わせ。\n西瓜は何度でも根気よく、通訳・補足をしてくれる。
TW: 他們又用仲文商量了起來。西瓜則是不厭其煩地給我們進行著翻譯和補充說明。
VN(csv3): Lại là một cuộc thảo luận bằng tiếng Trung Quốc.\nTây Qua vẫn kiên nhẫn phiên dịch và bổ sung cho chúng tôi hết lần này đến lần khác.
CUR: Lại là một cuộc thảo luận bằng tiếng Trung Quốc.\nTây Qua vẫn kiên nhẫn phiên dịch và bổ sung cho chúng tôi hết lần này đến lần khác.
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1008 | char=monologue | src=csv3
JP: ……仲国語のみの放送だけれど、意味は間違いようもない。\n間もなく終点、聖都着――だ。
TW: ……儘管只有仲文，但顯然沒有人會搞錯它所表達的內容——即將抵達終點，盛都了。
VN(csv3): ……Dù thông báo chỉ bằng tiếng Trung Quốc, nhưng ý nghĩa thì không thể nhầm lẫn được.\nSắp đến ga cuối, Thịnh Đô——rồi.
CUR: ……Dù thông báo chỉ bằng tiếng Trung Quốc, nhưng ý nghĩa thì không thể nhầm lẫn được.\nSắp đến ga cuối, Thịnh Đô——rồi.
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1732 | char=西瓜 | src=csv3
JP: 「すまなくないです。けれど双鉄先生とハチロクだけでは、\n仲国語話者とのコミュニケーションが難しいかと」
TW: 「您言重了。只是光靠雙鐵先生和八六的話，遇到說仲文的情況就會有困難了」
VN(csv3): 「Không có gì phải xin lỗi đâu ạ. Nhưng nếu chỉ có thầy Soutetsu và Hachiroku,\nthì việc giao tiếp với người nói tiếng Trung Quốc sẽ rất khó khăn.」
CUR: 「Không có gì phải xin lỗi đâu ạ. Nhưng nếu chỉ có thầy Soutetsu và Hachiroku,\nthì việc giao tiếp với người nói tiếng Trung Quốc sẽ rất khó khăn.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1796 | char=姜 | src=csv3
JP: 「日々姫先生の絵はやはり大人気となりました。\n仲国国内、海外の方。様々な観光客が集まって」
TW: 「日日姬女士的畫果然大受歡迎。聚集過來的不止仲國國內的，還有很多外國遊客」
VN(csv3): 「Tranh của cô Hibiki quả nhiên rất được yêu thích.\nKhách du lịch trong nước, ngoài nước. Đủ mọi du khách xúm lại xem.」
CUR: 「Tranh của cô Hibiki quả nhiên rất được yêu thích.\nKhách du lịch trong nước, ngoài nước. Đủ mọi du khách xúm lại xem.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1872 | char=志寰 | src=csv3
JP: 「日ノ本語・仲国語・髑国語の多重通訳まで発生しました。\n観光客の仲・髑国語話者さんが買ってでてくれて」
TW: 「甚至還出現了日語、仲文、德語交叉翻譯的情況。這要多虧了一位能說仲文和德文的遊客自告奮勇」
VN(csv3): 「Thậm chí còn có cả phiên dịch đa ngôn ngữ Hinomoto - Trung Quốc - Đức nữa.\nMột du khách biết tiếng Trung và tiếng Đức đã tình nguyện làm phiên dịch giúp.」
CUR: 「Thậm chí còn có cả phiên dịch đa ngôn ngữ Hinomoto - Trung Quốc - Đức nữa.\nMột du khách biết tiếng Trung và tiếng Đức đã tình nguyện làm phiên dịch giúp.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2032 | char=日々姫 | src=csv3
JP: 「ほんっとすごかね～　こんお部屋！\n仲国の時代劇とかに出てきそうだもん！！」
TW: 「這房間可真不得了唉～簡直和仲國古裝劇裡的一模一樣！！」
VN(csv3): 「Căn phòng này~ Tuyệt vời thật đấy!\nCứ như bước ra từ phim cổ trang Trung Quốc vậy!!」
CUR: 「Căn phòng này~ Tuyệt vời thật đấy!\nCứ như bước ra từ phim cổ trang Trung Quốc vậy!!」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1739 | char=日々姫 | src=csv3
JP: 「その辺のお話は聞いたと。歴史ば、仲国観光の、\nやっぱりおっきなテーマのひとつみたい」
TW: 「我也記得聽他們說過唉，歷史在中國人的旅行中也是占了很大的比重的」
VN(csv3): 「Em cũng có nghe nói về chuyện đó. Lịch sử,\nquả nhiên là một trong những chủ đề lớn của du lịch Trung Quốc.」
CUR: 「Em cũng có nghe nói về chuyện đó. Lịch sử,\nquả nhiên là một trong những chủ đề lớn của du lịch Trung Quốc.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1580 | char=双鉄 | src=audit
JP: 「ああ、覚えている。というか、[とほ,1]徒甫と添え書きも\nしてあったよな。仲国の、代表的な詩人だろう？」
TW: 「啊，記得記得。而且我看到人像旁還標註了“杜浦”兩字。那應該是仲國代表性的詩人對吧？」
VN(csv3): 「À, anh nhớ rồi. Hình như còn có dòng chữ Đỗ Phủ kèm theo nữa nhỉ.\nLà một nhà thơ tiêu biểu của Trung Quốc đúng không?」
CUR: 「Aa, anh nhớ rồi. Hình như còn có dòng chữ Đỗ Phủ kèm theo nữa nhỉ.\nLà một nhà thơ tiêu biểu của Trung Quốc đúng không?」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1068 | char=双鉄 | src=csv3
JP: 「……なるほど、仲国においての歴史観光は、\n日ノ本のそれの何百倍もの人気をもっているのだな」
TW: 「……原來如此，在仲國，歷史觀光所吸引的人流遠在日本國的數百倍之上啊」
VN(csv3): 「……Ra vậy, du lịch lịch sử ở Trung Quốc,\ncó mức độ phổ biến gấp hàng trăm lần so với ở Hinomoto nhỉ.」
CUR: 「……Ra vậy, du lịch lịch sử ở Trung Quốc,\ncó mức độ phổ biến gấp hàng trăm lần so với ở Hinomoto nhỉ.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1940 | char=日々姫 | src=csv3
JP: 「それに比べて、仲国は本当に歴史観光が盛んみたい。\n春節や国慶節には、史跡めぐりの旅もよく行われるって」
TW: 「與此相比，仲國的歷史觀光真是不得了。春節和國慶的出行行程，也有許多人選擇遊覽歷史古蹟的」
VN(csv3): 「So với điều đó, du lịch lịch sử ở Trung Quốc thực sự rất phát triển.\nVào dịp Lễ hội Mùa xuân hay Quốc khánh, các chuyến đi tham quan di tích lịch sử cũng diễn ra rất thường xuyên.」
CUR: 「So với điều đó, du lịch lịch sử ở Trung Quốc thực sự rất phát triển.\nVào dịp Lễ hội Mùa xuân hay Quốc khánh, các chuyến đi tham quan di tích lịch sử cũng diễn ra rất thường xuyên.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1575 | char=日々姫 | src=audit
JP: 「あ、仲国の大型連休。春節が日ノ本の旧正月で、\n国慶節は仲国の建国記念日。それぞれ一週間のお休み」
TW: 「啊，就是仲國的長假。春節相當於日本國的舊曆正月，國慶是仲國的建國紀念日。都有一週的假期」
VN(csv3): 「À, đó là những kỳ nghỉ lễ lớn ở Trung Quốc. Lễ hội Mùa xuân giống như Tết Nguyên đán của Hinomoto,\ncòn Quốc khánh là ngày kỷ niệm quốc khánh của Trung Quốc. Mỗi dịp đều được nghỉ một tuần.」
CUR: 「À, đó là những kỳ nghỉ lễ lớn ở Trung Quốc. Lễ hội Mùa xuân giống như Tết Nguyên đán của Hinomoto,\ncòn Quốc khánh là ngày kỷ niệm thành lập nước Trung Quốc. Mỗi dịp đều được nghỉ một tuần.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1764 | char=双鉄 | src=csv3
JP: 「ゆえ、移動を単なる移動としないための要素を――\n『仲国版ナインスターズ』で、取り込みたいわけか」
TW: 「所以為了拓展更多要素，讓鐵路不再是單純的出行手段——才想引進“仲國版九星”的概念啊」
VN(csv3): 「Vì vậy, họ muốn đưa những yếu tố giúp việc di chuyển không chỉ đơn thuần là di chuyển——\nvào 'Nine Stars phiên bản Trung Quốc' sao.」
CUR: 「Vì vậy, họ muốn đưa những yếu tố giúp việc di chuyển không chỉ đơn thuần là di chuyển——\nvào 'Nine Stars phiên bản Trung Quốc' sao.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1066 | char=日々姫 | src=csv3
JP: 「……仲国全土の、例えば歴史遺産だけに絞ったとしても、\n周遊ってなると――」
TW: 「……仲國全境，即便只挑選歷史古蹟，想要周遊也——」
VN(csv3): 「……Dù chỉ tập trung vào các di sản lịch sử trên toàn lãnh thổ Trung Quốc,\nnhưng nếu nói đến việc đi vòng quanh thì——」
CUR: 「……Dù chỉ tập trung vào các di sản lịch sử trên toàn lãnh thổ Trung Quốc,\nnhưng nếu nói đến việc đi vòng quanh thì——」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=1107 | char=双鉄 | src=csv3
JP: 「……拠点間の距離を短くとれば、ナインスターズ型も\n可能となるが……それでは、仲国らしさを余りにも欠く」
TW: 「……選擇的據點之間距離較短的話，倒是可以實現九星一樣的形式……但就少了很多仲國特色」
VN(csv3): 「……Nếu rút ngắn khoảng cách giữa các điểm dừng, mô hình Nine Stars\ncũng có thể thực hiện được……Nhưng như vậy, lại quá thiếu đi bản sắc của Trung Quốc.」
CUR: 「……Nếu rút ngắn khoảng cách giữa các điểm dừng, mô hình Nine Stars\ncũng có thể thực hiện được……Nhưng như vậy, lại quá thiếu đi bản sắc của Trung Quốc.」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2081 | char=日々姫 | src=csv3
JP: 「７日間で仲国大陸半周くらいはできそう？\nばってん、乗車と観光の時間のバランスが……」
TW: 「７天大概夠遊覽仲國大陸半圈？而且，搭車與觀光的時間平衡也……」
VN(csv3): 「Trong 7 ngày có thể đi được nửa vòng lục địa Trung Quốc không nhỉ?\nNhưng mà, sự cân bằng giữa thời gian đi tàu và tham quan thì……」
CUR: 「Trong 7 ngày có thể đi được nửa vòng lục địa Trung Quốc không nhỉ?\nNhưng mà, sự cân bằng giữa thời gian đi tàu và tham quan thì……」
--- 01_Hachiroku | 仲国06_聖都とパンダとハチロクと.txt.toml | key=2434 | char=monologue | src=csv3
JP: 僕たちはまだ、仲国の鉄道利用者の。あるいは鉄道を\n利用していない人たちの、声を、ほとんど聞けていない。
TW: 我們所聽到的，在仲國乘坐列車的人的心聲還是太少，而不坐火車的人的意見，更是幾乎沒有。
VN(csv3): Chúng tôi vẫn chưa nghe được nhiều ý kiến của những người sử dụng đường sắt ở Trung Quốc.\nHay thậm chí là của những người không sử dụng đường sắt.
CUR: Chúng tôi vẫn chưa nghe được nhiều ý kiến của những người sử dụng đường sắt ở Trung Quốc.\nHay thậm chí là của những người không sử dụng đường sắt.
--- 02_Hibiki | lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml | key=1689 | char=双鉄 | src=csv3
JP: 「まぁ、急な話だったからな。稀咲仲介での、\n仲国からの要人たちの、団体での御一夜視察」
TW: 「沒辦法嘛。畢竟在稀咲中介下，來自仲國的重要人物集體來御一夜視察這件事太突然了」
VN(csv3): 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\nđến thị sát Ohimitera thông qua sự môi giới của Kisaki.」
CUR: 「Mà, chuyện cũng đột ngột quá mà. Đoàn quan chức cấp cao từ Nakakuni\nđến thị sát Ohimitera thông qua sự môi giới của Kisaki.」
--- 04_Reina | れいな03_しゅっぱつしんこう.txt.toml | key=2070 | char=monologue | src=csv3
JP: 言われれば、学園で昔習ったことを思い出す。\n[ちゅうごく,1]仲国からの鉄鉱石と、築豊炭田の石炭と。
TW: 她這麼一說，我回想起了過去在學校裡學過的知識。
VN(csv3): Nghe vậy, tôi nhớ lại những gì từng học ở trường.\nQuặng sắt từ nước Chukoku và than đá từ mỏ than Chikuho.
CUR: Nghe vậy, tôi nhớ lại những gì từng học ở trường.\nQuặng sắt từ nước Chukoku và than đá từ mỏ than Chikuho.
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1860 | char=姜 | src=audit
JP: 「あなたが双鉄先生ですね。はじめまして。\n仲国国務院、鉄道部副部長秘書の、[きょうようこう,2]姜叶煌と申します」
TW: 稀咲的支行長室與往常無二。但今天在座的卻多了一張陌生的面孔。
VN(csv3): 「Anh là ngài Soutetsu nhỉ. Rất hân hạnh được gặp.\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc, tên là Khương Diệp Hoàng.」
CUR: 「Ngài là Soutetsu nhỉ. Rất hân hạnh được gặp.\nTôi là thư ký của Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trọng Quốc, tên là Khương Diệp Hoàng.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1182 | char=monologue | src=csv3
JP: よく見れば、茶器と皿ともいつもとは違う、仲国のものだ。\n細かな気遣いもさすがだなと、改めて感心させられる。
TW: 「嘻嘻，喜歡的話還有哦，不要客氣。雙鐵也有，給」
VN(csv3): Nhìn kỹ thì, cả bộ ấm chén và đĩa đều khác ngày thường, là đồ của Trọng Quốc.\nSự chu đáo tỉ mỉ này quả nhiên không hổ danh là cô ấy, khiến tôi một lần nữa phải thán phục.
CUR: Nhìn kỹ thì, cả bộ ấm chén và đĩa đều khác ngày thường, là đồ của Trọng Quốc.\nSự chu đáo tỉ mỉ này quả nhiên không hổ danh là cô ấy, khiến tôi một lần nữa phải thán phục.
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1716 | char=双鉄 | src=csv3
JP: 「というと、仲国国務院の鉄道部内で……ですか。\n大変恐縮です。――というか、一体全体どういうわけで」
TW: 她臉上帶著平和的笑容，自然地說出的話語，卻有著與此全然不同的分量，讓我一時沒能完全理解。
VN(csv3): 「Nói vậy tức là, trong nội bộ Bộ Đường sắt của Quốc vụ viện Trọng Quốc……sao.\nThật vô cùng vinh hạnh. ――Hay đúng hơn là, rốt cuộc thì tại sao lại như vậy.」
CUR: 「Nói vậy tức là, trong nội bộ Bộ Đường sắt của Quốc vụ viện Trọng Quốc……sao.\nThật vô cùng vinh hạnh. ――Hay đúng hơn là, rốt cuộc thì tại sao lại như vậy.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1091 | char=monologue | src=csv3
JP: 日ノ本車輌の淵さんはじめ、仲国からの声かけを受けた\n一流どころの技術者ならば、複数の名前を把握している。
TW: 「原來如此，確實有道理。這方面的情況我也有所耳聞——」
VN(csv3): Từ anh Fuchi của Xe lửa Hinomoto, cho đến những kỹ sư hàng đầu\nnhận được lời mời từ Trọng Quốc, tôi đều nắm rõ một vài cái tên.
CUR: Từ anh Fuchi của Xe lửa Hinomoto, cho đến những kỹ sư hàng đầu\nnhận được lời mời từ Trọng Quốc, tôi đều nắm rõ một vài cái tên.
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1563 | char=monologue | src=csv3
JP: 仲国は冥国をはっきりとライバル視している国だ。ゆえ、\n冥国のエアクラ推進への対立軸を立てようとしていると。
TW: 「這個說法確實多少從稀咲那裡聽說過一點」
VN(csv3): Trọng Quốc là quốc gia coi Minh Quốc là đối thủ rõ rệt. Vì vậy,\nhọ đang cố gắng thiết lập một trục đối lập với việc thúc đẩy Aircra của Minh Quốc.
CUR: Trọng Quốc là quốc gia coi Minh Quốc là đối thủ rõ rệt. Vì vậy,\nhọ đang cố gắng thiết lập một trục đối lập với việc thúc đẩy Aircra của Minh Quốc.
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1068 | char=稀咲 | src=csv3
JP: 「ん？　複数の鉄道事業者って……国鉄以外にもあるんだ。\n仲国にも……いわゆる民鉄、私鉄的なものが」
TW: 「其實鐵道部也接到了一些對私有線路基金有興趣的鐵路從業人員的諮詢」
VN(csv3): 「Hử? Một số doanh nghiệp đường sắt tức là……ngoài đường sắt quốc gia ra vẫn còn à.\nỞ Trọng Quốc cũng có……cái gọi là đường sắt dân sự, đường sắt tư nhân sao.」
CUR: 「Hử? Một số doanh nghiệp đường sắt tức là……ngoài đường sắt quốc gia ra vẫn còn à.\nỞ Trọng Quốc cũng có……cái gọi là đường sắt dân sự, đường sắt tư nhân sao.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1741 | char=姜 | src=csv3
JP: 「双鉄先生、ご興味がおありでしたらいかがでしょう。\n弊部がお招きいたしますので、稀咲女士との仲国視察は」
TW: 姜小姐的態度突然柔和了下來。
VN(csv3): 「Ngài Soutetsu, nếu ngài có hứng thú thì sao ạ.\nBộ chúng tôi sẽ gửi lời mời, chuyến khảo sát Trọng Quốc cùng cô Kisaki.」
CUR: 「Ngài Soutetsu, nếu ngài có hứng thú thì sao ạ.\nBộ chúng tôi sẽ gửi lời mời, chuyến khảo sát Trọng Quốc cùng cô Kisaki.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1511 | char=姜 | src=csv3
JP: 「新事業案の共有。それが仲国でも展開可能なもので\nあるなら、なんらかの方法での共同展開を検討頂きたい」
TW: 「能對我們的私有線路基金抱有這樣的興趣，我真的很高興。非常感謝。那第二呢？」
VN(csv3): 「Chia sẻ dự án mới. Nếu đó là dự án có thể triển khai ở Trọng Quốc,\nchúng tôi mong muốn được xem xét việc cùng triển khai bằng một phương pháp nào đó.」
CUR: 「Chia sẻ dự án mới. Nếu đó là dự án có thể triển khai ở Trọng Quốc,\nchúng tôi mong muốn được xem xét việc cùng triển khai bằng một phương pháp nào đó.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1573 | char=monologue | src=csv3
JP: 稀咲が驚いた顔をする。春節――旧正月は確か、\n仲国で一番のお祭りの時期と聞き及ぶが……
TW: 「這！？春節期間還是不太好吧」
VN(csv3): Kisaki lộ vẻ ngạc nhiên. Tết Nguyên Đán――Tết Âm lịch hình như,\nlà dịp lễ hội lớn nhất ở Trọng Quốc theo như tôi nghe được……
CUR: Kisaki lộ vẻ ngạc nhiên. Tết Nguyên Đán――Tết Âm lịch hình như,\nlà dịp lễ hội lớn nhất ở Trọng Quốc theo như tôi nghe được……
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1161 | char=稀咲 | src=csv3
JP: 「ふふっ、相変わらず呑むんだねぇ。\n自分用ってことは――仲国からの持ち込み？」
TW: 「啊，承蒙邀請，我真是太開心了！哪有拒絕的道理呀！作為回禮，我帶自備的紹興酒過來吧」
VN(csv3): 「Fufu, vẫn thích uống như ngày nào nhỉ.\nCủa riêng mình nghĩa là――mang từ Trọng Quốc sang sao?」
CUR: 「Fufu, vẫn thích uống như ngày nào nhỉ.\nCủa riêng mình nghĩa là――mang từ Trọng Quốc sang sao?」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=996 | char=稀咲 | src=csv3
JP: 「対人関係のみに絞れば、そうかもね。\nなにせ仲国国務院鉄道部の副部長秘書だ」
TW: 「不過，這所謂彈性，在見識過姜小姐的表現以後，真是自慚形穢，差得太遠了」
VN(csv3): 「Nếu chỉ xét riêng về quan hệ đối nhân xử thế, thì có lẽ là vậy.\nDù sao cô ấy cũng là thư ký của Thứ trưởng Bộ Đường sắt Quốc vụ viện Trọng Quốc mà.」
CUR: 「Nếu chỉ xét riêng về quan hệ đối nhân xử thế, thì có lẽ là vậy.\nDù sao cô ấy cũng là thư ký của Thứ trưởng Bộ Đường sắt Quốc vụ viện Trọng Quốc mà.」
--- 06_Kisaki | lr稀咲追加01_仲国視察の誘い.txt.toml | key=1819 | char=稀咲 | src=csv3
JP: 「父は、それをみかねたんだろうね。\n仲国からの留学生を、家庭教師につけてくれた」
TW: 確實，一個新來的小姑娘當支行長，自稱又是[ｂｏｋｕ]我——這樣表現出來的就不是威嚴而是可愛了。
VN(csv3): 「Chắc cha em không thể đứng nhìn mãi được.\nNên ông đã thuê một du học sinh từ Trọng Quốc về làm gia sư cho em.」
CUR: 「Chắc cha em không thể đứng nhìn mãi được.\nNên ông đã thuê một du học sinh từ Trọng Quốc về làm gia sư cho em.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1153 | char=双鉄 | src=csv3
JP: 「ほう。仲国と日ノ本の鉄道両方を知っているのか。\nそれは大変こころづよいな」
TW: 「哦，對中日雙方的鐵路知己知彼啊。那可真是相當可靠呢」
VN(csv3): 「Hô. Vậy là em am hiểu cả đường sắt của Trọng Quốc và Hinomoto sao.\nThế thì thật là đáng tin cậy.」
CUR: 「Hô. Vậy là em am hiểu cả đường sắt của Trọng Quốc và Hinomoto sao.\nThế thì thật là đáng tin cậy.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1343 | char=稀咲 | src=csv3
JP: 「西瓜君の印象だけで語って欲しいんだけど――\n日ノ本の鉄道と仲国の鉄道、一番の違いってなにかな」
TW: 「我想問一下單以西瓜的第一印象而言的話——日本鐵路和仲國鐵路最大的區別是什麼？」
VN(csv3): 「Chị muốn nghe cảm nhận của riêng Suika thôi nhé——\nSự khác biệt lớn nhất giữa đường sắt Hinomoto và đường sắt Trọng Quốc là gì vậy?」
CUR: 「Chị muốn nghe cảm nhận của riêng Suika thôi nhé——\nSự khác biệt lớn nhất giữa đường sắt Hinomoto và đường sắt Trọng Quốc là gì vậy?」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1385 | char=姜 | src=csv3
JP: 「仲国の古文にある言葉です。\n『物事をその成立から遡り突き詰める』的な意味です」
TW: 「是一句仲國的古文。“事無大小，悉究本末”的意思」
VN(csv3): 「Đó là một từ trong cổ văn của Trọng Quốc.\nNó mang ý nghĩa 'truy tìm nguồn gốc và đi sâu vào bản chất của sự việc'.」
CUR: 「Đó là một từ trong cổ văn của Trọng Quốc.\nNó mang ý nghĩa 'truy tìm nguồn gốc và đi sâu vào bản chất của sự việc'.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1682 | char=稀咲 | src=csv3
JP: 「ＯＫ。じゃ、もう少しだけ質問させて？　今度は逆に、\n日ノ本と仲国の鉄道で、同じだと感じるところは？」
TW: 「ＯＫ。那我再多問一點囉，這次反過來問，日本和仲國的鐵路，有哪些地方感覺是一樣的？」
VN(csv3): 「OK. Vậy cho chị hỏi thêm một chút nữa nhé? Lần này ngược lại,\nem cảm thấy điểm giống nhau giữa đường sắt Hinomoto và Trọng Quốc là gì?」
CUR: 「OK. Vậy cho chị hỏi thêm một chút nữa nhé? Lần này ngược lại,\nem cảm thấy điểm giống nhau giữa đường sắt Hinomoto và Trọng Quốc là gì?」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1074 | char=稀咲 | src=csv3
JP: 「仲国では、まだエアクラ自動車の普及率、\nそこまでではないと理解していたけど？」
TW: 「仲國的空凝機汽車普及率，應該還沒有那麼高吧？」
VN(csv3): 「Chị hiểu là ở Trọng Quốc, tỷ lệ phổ cập của xe Aircra\nvẫn chưa đến mức đó mà nhỉ?」
CUR: 「Chị hiểu là ở Trọng Quốc, tỷ lệ phổ cập của xe Aircra\nvẫn chưa đến mức đó mà nhỉ?」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1638 | char=稀咲 | src=csv3
JP: 「なら、西瓜君。仲国国鉄が、鉄道存続のために\nまっさきに為すべきことは、なんだと思う？」
TW: 「那西瓜你覺得，仲國國鐵為確保鐵路的存續，該做的最首當其衝的是什麼？」
VN(csv3): 「Vậy thì Suika. Em nghĩ Đường sắt Quốc gia Trọng Quốc,\nviệc đầu tiên cần làm để duy trì sự tồn tại của đường sắt là gì?」
CUR: 「Vậy thì Suika. Em nghĩ Đường sắt Quốc gia Trọng Quốc,\nviệc đầu tiên cần làm để duy trì sự tồn tại của đường sắt là gì?」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1629 | char=稀咲 | src=csv3
JP: 「なら僕たちが次に視察するべきは、\n『仲国国鉄の現状そのもの』かな？　どう思う？　双鉄」
TW: 「那我們接下來該考察的，就是“仲國國鐵的現狀本身”了吧？你覺得呢，雙鐵？」
VN(csv3): 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trọng Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」
CUR: 「Vậy thì thứ tiếp theo chúng ta cần khảo sát,\ncó lẽ là 'chính hiện trạng của Đường sắt Quốc gia Trọng Quốc' nhỉ? Anh thấy sao? Anh Soutetsu.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1072 | char=稀咲 | src=csv3
JP: 「仲国で一番たくさんの乗客に乗られている列車。\nボクらをそれに乗せてほしい」
TW: 「仲國最多乘客乘坐的列車，我們希望能去乘坐一下」
VN(csv3): 「Chuyến tàu có số lượng hành khách đi nhiều nhất ở Trọng Quốc.\nTôi muốn chúng tôi được đi chuyến tàu đó.」
CUR: 「Chuyến tàu có số lượng hành khách đi nhiều nhất ở Trọng Quốc.\nTôi muốn chúng tôi được đi chuyến tàu đó.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1077 | char=双鉄 | src=csv3
JP: 「かなり強い同意を受けたように思ったが――\n仲国国鉄の餐車や寝台車も、同じような感じなのか？」
TW: 「似乎你們也深有同感的樣子——莫非仲國的餐車和臥鋪車也都經歷了類似的過程嗎？
VN(csv3): 「Tôi có cảm giác em rất đồng tình với điều này——\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trọng Quốc cũng giống như vậy sao?」
CUR: 「Tôi có cảm giác em rất đồng tình với điều này——\nToa ăn và toa giường nằm của Đường sắt Quốc gia Trọng Quốc cũng giống như vậy sao?」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1634 | char=西瓜 | src=csv3
JP: 「まさしく、今の仲国国鉄が担っている実需が根こそぎ\n奪われるでしょう。西瓜はそれを懸念しています」
TW: 「那無疑會動搖到如今仲國國鐵所肩負的剛需的根基。西瓜擔心的就是這一點」
VN(csv3): 「Chắc chắn, nhu cầu thực tế mà Đường sắt Quốc gia Trọng Quốc đang đảm nhận hiện nay sẽ bị cướp mất tận gốc rễ.\nSuika đang rất lo ngại về điều đó.」
CUR: 「Chắc chắn, nhu cầu thực tế mà Đường sắt Quốc gia Trọng Quốc đang đảm nhận hiện nay sẽ bị cướp mất tận gốc rễ.\nSuika đang rất lo ngại về điều đó.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1332 | char=稀咲 | src=csv3
JP: 「ボクもその線がいいと思う。だからまず仲国の若い\nカップル層の多数が、どのような嗜好かを知りたいな」
TW: 「我也認為這樣做最為妥當，所以需要先知道你們仲國的年輕情侶大多有著什麼樣的需求」
VN(csv3): 「Tôi cũng nghĩ hướng đó là tốt nhất. Vì vậy, trước tiên tôi muốn biết\nđại đa số các cặp đôi trẻ ở Trọng Quốc có sở thích như thế nào.」
CUR: 「Tôi cũng nghĩ hướng đó là tốt nhất. Vì vậy, trước tiên tôi muốn biết\nđại đa số các cặp đôi trẻ ở Trọng Quốc có sở thích như thế nào.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1073 | char=双鉄 | src=csv3
JP: 「仲国の若者層の主たるニュースソースはどのあたりだ？\nネット、新聞、TVなどいろいろあるかとは思うが」
TW: 「仲國的年輕人主要是通過什麼樣的途徑獲得訊息的？比如網路、報紙和電視，應該是種類繁多」
VN(csv3): 「Nguồn tin tức chính của giới trẻ Trọng Quốc là ở đâu?\nTôi nghĩ có rất nhiều nguồn như mạng internet, báo chí, TV v.v.」
CUR: 「Nguồn tin tức chính của giới trẻ Trọng Quốc là ở đâu?\nTôi nghĩ có rất nhiều nguồn như mạng internet, báo chí, TV v.v.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1346 | char=姜 | src=csv3
JP: 「理解しました。それは確かに悪手ですね。\n仲国でも、露見すれば反発されることは必至です」
TW: 「我明白了，這樣做的確不好，就算在仲國，一旦被揭穿也肯定會招來人們的反感」
VN(csv3): 「Tôi hiểu rồi. Đó quả thực là một nước đi tồi.\nỞ Trọng Quốc cũng vậy, nếu bị lộ chắc chắn sẽ vấp phải sự phản đối gay gắt.」
CUR: 「Tôi hiểu rồi. Đó quả thực là một nước đi tồi.\nỞ Trọng Quốc cũng vậy, nếu bị lộ chắc chắn sẽ vấp phải sự phản đối gay gắt.」
--- 06_Kisaki | lr稀咲追加02_仲国視察.txt.toml | key=1294 | char=稀咲 | src=csv3
JP: 「若者層の主たるニュースソースはニュースサイト、\nSNS、グループチャット。ステマは仲国でも反感を買う」
TW: 「年輕人的訊息來源以網站、社交軟體和即時通信軟體為主，仲國人也非常反感秘密行銷」
VN(csv3): 「Nguồn tin tức chính của giới trẻ là các trang tin tức,\nSNS, trò chuyện nhóm. Stealth marketing ở Trọng Quốc cũng gây phản cảm.」
CUR: 「Nguồn tin tức chính của giới trẻ là các trang tin tức,\nSNS, trò chuyện nhóm. Stealth marketing ở Trọng Quốc cũng gây phản cảm.」
--- 06_Kisaki | lr稀咲追加03_新事業案.txt.toml | key=1029 | char=稀咲 | src=audit
JP: 「いや本当に豪快だね！　――ああ、けど、うん。\n食べて供養っていう考えは、多分仲国にもあるのかな」
TW: 「哎呀，果真是豪爽！哦，不過也對，也許在仲國也有以食表達感激的風俗」
VN(csv3): 「Chà, hào sảng thật đấy! ——A, nhưng mà, ừm.\nTư tưởng ăn để cúng dường, chắc ở Trọng Quốc cũng có nhỉ.」
CUR: 「Chà, hào sảng thật đấy! ——À, nhưng mà, ừm.\nTư tưởng ăn để cúng dường, chắc ở Trọng Quốc cũng có nhỉ.」
--- 06_Kisaki | lr稀咲追加03_新事業案.txt.toml | key=1394 | char=姜 | src=csv3
JP: 「さてどうでしょう。少なくとも私は理解できますが、\nなにせ仲国は広いですから」
TW: 「這可很難說，雖然我能理解這種文化，但仲國畢竟地大物博」
VN(csv3): 「Chuyện đó thì sao nhỉ. Ít nhất là tôi có thể hiểu được,\nnhưng dù sao thì Trọng Quốc cũng rộng lớn lắm mà.」
CUR: 「Chuyện đó thì sao nhỉ. Ít nhất là tôi có thể hiểu được,\nnhưng dù sao thì Trọng Quốc cũng rộng lớn lắm mà.」
--- 06_Kisaki | lr稀咲追加03_新事業案.txt.toml | key=1170 | char=双鉄 | src=csv3
JP: 「羊料理ひとつとっても、仲国各地で、\nさぞさまざまなバリエーションがあるのだろうな」
TW: 「想必在仲國，即便同樣是羊肉，在不同地區也有著截然不同的菜式吧」
VN(csv3): 「Chỉ riêng món thịt cừu thôi, ở các vùng khác nhau của Trọng Quốc,\nchắc hẳn cũng có vô vàn biến tấu khác nhau nhỉ.」
CUR: 「Chỉ riêng món thịt cừu thôi, ở các vùng khác nhau của Trọng Quốc,\nchắc hẳn cũng có vô vàn biến tấu khác nhau nhỉ.」
--- 06_Kisaki | lr稀咲追加03_新事業案.txt.toml | key=1706 | char=monologue | src=csv3
JP: 西瓜が画面を示してくれる。仲国語が読めずとも、\n意味するところはアイコンから、何となく伝わってくる。
TW: 西瓜把手機拿給我們看，即便我看不懂仲文，單看圖示也能大概猜出是什麼意思。
VN(csv3): Suika đưa màn hình cho chúng tôi xem. Dù không đọc được tiếng Trọng Quốc,\nnhưng tôi vẫn có thể lờ mờ hiểu được ý nghĩa thông qua các biểu tượng.
CUR: Suika đưa màn hình cho chúng tôi xem. Dù không đọc được tiếng Trọng Quốc,\nnhưng tôi vẫn có thể lờ mờ hiểu được ý nghĩa thông qua các biểu tượng.
--- 06_Kisaki | lr稀咲追加03_新事業案.txt.toml | key=1101 | char=姜 | src=csv3
JP: 「仲国でも同時にこの企画を走らせることが叶うなら、\n[ヒノチュウ,2]日ノ仲戦も行えるようになりますね」
TW: 「如果能同時在仲國實行這一套方案，我們還可以舉辦仲日對抗賽」
VN(csv3): 「Nếu có thể đồng thời triển khai dự án này ở Trung Quốc,\nthì chúng ta cũng có thể tổ chức trận đấu Nhật-Trung nhỉ.」
CUR: 「Nếu có thể đồng thời triển khai dự án này ở Trung Quốc,\nthì chúng ta cũng có thể tổ chức trận đấu Nhật-Trung nhỉ.」
--- 06_Kisaki | lr稀咲追加h_お風呂は日ノ本式に限るね.txt.toml | key=1033 | char=稀咲 | src=csv3
JP: 「仲国も実に良かったけれど、\nお風呂ばかりは日ノ本式に限るねぇ」
TW: 「仲國之行自然不錯，但說到泡澡還是日本式的好」
VN(csv3): 「Ở Trung Quốc cũng rất tuyệt, nhưng\nnói đến việc tắm rửa thì đúng là phong cách Hinomoto vẫn là nhất nhỉ.」
CUR: 「Ở Trung Quốc cũng rất tuyệt, nhưng\nnói đến việc tắm rửa thì đúng là phong cách Hinomoto vẫn là nhất nhỉ.」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2455 | char=稀咲 | src=csv3
JP: 「来客があるんだよ、[ちゅうごく,1]仲国から。父の古い友人の\n娘さんなんだけどさ、随分気難しい方らしくてね」
TW: 「我有個來自仲國的客人，是父親老友的女兒，真的很不好相處」
VN(csv3): 「Em sắp có khách đến thăm, từ Trọng Quốc. Là con gái\ncủa một người bạn cũ của bố em, nhưng có vẻ cô ấy là người khá khó tính」
CUR: 「Em sắp có khách đến thăm, từ Trọng Quốc. Là con gái\ncủa một người bạn cũ của bố em, nhưng có vẻ cô ấy là người khá khó tính」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2020 | char=双鉄 | src=csv3
JP: 「仲国では、銀行も国営なのか」
TW: 「仲國的銀行也是國營的嗎」
VN(csv3): 「Ở Trọng Quốc, ngân hàng cũng là của nhà nước sao」
CUR: 「Ở Trọng Quốc, ngân hàng cũng là của nhà nước sao」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=1983 | char=稀咲 | src=csv3
JP: 「かかわるというより、融資の主体となるはずだ。\nもっとも今は仲国も、大廃線の嵐だけれども」
TW: 「不止是參加那麼簡單，而是融資的主體。現在仲國也掀起了廢線的潮流」
VN(csv3): 「Hơn cả liên quan, họ chắc chắn là chủ thể cấp vốn chính đấy.\nMặc dù hiện tại Trọng Quốc cũng đang chìm trong cơn bão Đại bãi bỏ các tuyến đường sắt」
CUR: 「Hơn cả liên quan, họ chắc chắn là chủ thể cấp vốn chính đấy.\nMặc dù hiện tại Trọng Quốc cũng đang chìm trong cơn bão Đại bãi bỏ các tuyến đường sắt」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2972 | char=monologue | src=audit
JP: 反冥という政府方針もあってだろうか、\n仲国のエアクラ本格化は日ノ本よりもかなり遅れた。
TW: 一部分是出於反冥的行政要求，仲國的民航業比日本晚了很久才走上正軌。
VN(csv3): Có lẽ cũng một phần do chính sách phản đối Aerocraft của chính phủ,\nmà việc phổ biến Aerocraft ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều.
CUR: Có lẽ cũng một phần do chính sách chống Minh Quốc của chính phủ,\nmà việc phổ biến Aircra ở Trọng Quốc diễn ra muộn hơn Hinomoto khá nhiều.
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2489 | char=双鉄 | src=csv3
JP: 「仲国の方の接待となると、\nやはり、チャイナドレスを着たりするのか？」
TW: 「接待來自仲國的客人，肯定要穿旗袍吧？」
VN(csv3): 「Tiếp đón khách từ Trọng Quốc,\nthì em sẽ mặc sườn xám sao?」
CUR: 「Tiếp đón khách từ Trọng Quốc,\nthì em sẽ mặc sườn xám sao?」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2230 | char=稀咲 | src=csv3
JP: 「あー……これ、ちゃんと仲国で採寸して仕立てた、\n本場の、本格的なヤツなんだ」
TW: 「啊……這是在仲國量身定做的，絕對原汁原味的旗袍」
VN(csv3): 「A…… bộ này, là đồ chính hiệu, được đo may đàng hoàng\nở Trọng Quốc đấy」
CUR: 「A…… bộ này, là đồ chính hiệu, được đo may đàng hoàng\nở Trọng Quốc đấy」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=2730 | char=稀咲 | src=csv3
JP: 「本場の……仲国の一流の工房でお願いしたんだ」
TW: 「這是在仲國……一流服裝廠訂製的」
VN(csv3): 「Em đã đặt may ở…… một xưởng may hàng đầu tại Trọng Quốc đấy」
CUR: 「Em đã đặt may ở…… một xưởng may hàng đầu tại Trọng Quốc đấy」
--- 06_Kisaki | 稀咲h3_チャイナドレスでおもてなし.txt.toml | key=3324 | char=monologue | src=csv3
JP: 日ノ本文化が、女性の曲線を隠すものなら、\n仲国文化は、曲線を見せる文化なのだと。
TW: 日本文化中，女性的身體曲線是要遮掩的。而在仲國，曲線是要表現出來的。
VN(csv3): Nếu văn hóa Hinomoto là che giấu đi những đường cong của người phụ nữ,\nthì văn hóa Trọng Quốc lại là văn hóa phô bày những đường cong ấy.
CUR: Nếu văn hóa Hinomoto là che giấu đi những đường cong của người phụ nữ,\nthì văn hóa Trọng Quốc lại là văn hóa phô bày những đường cong ấy.
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=1722 | char=ふかみ | src=audit
JP: 「もっと高く。衛星軌道にまで飛んで？　どう見える？\n[めいこく,1]冥国、[えいこく,1]詠国、[どっこく,1]髑国、フランク、[ちゅうごく,1]仲国、[かんこく,1]汗国とかの線路は」
TW: 「再飛高點，飛上衛星軌道。美國、英國、德國、法國、仲國、韓國的線路，看起來怎麼樣？」
VN(csv3): 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Mỹ, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」
CUR: 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=1997 | char=双鉄 | src=csv3
JP: 「稀咲と元忠氏の仲国人脈のことならば知っている。\nというか、その他の国に、ツテはないのか？」
TW: 「我知道你和元忠有仲國的人脈。其他的國家你們沒有人脈嗎？」
VN(csv3): 「Về mạng lưới quan hệ ở Trung Quốc của Kisaki và ông Mototada thì tôi biết.\nNói đúng hơn là, không có mối liên hệ nào ở các quốc gia khác sao?」
CUR: 「Về mạng lưới quan hệ ở Trung Quốc của Kisaki và ông Mototada thì tôi biết.\nNói đúng hơn là, không có mối liên hệ nào ở các quốc gia khác sao?」
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=2173 | char=双鉄 | src=audit
JP: 「大陸の――\n[ちゅうごく,1]仲国のご友人の招待なのだろう？」
TW: 「你是指接待大陸的——仲國的朋友嗎？」
VN(csv3): 「Chẳng phải em được mời bởi một người bạn ở Đại lục——\nTrung Quốc sao?」
CUR: 「Chẳng phải cô được mời bởi một người bạn ở Đại lục——\nTrung Quốc sao?」
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=3797 | char=monologue | src=csv3
JP: “元忠さんの旧友”が、\n仲国政府の、交通系の、かなりの要職にあることならば。
TW: 考慮到這位“元忠先生的舊交”，在仲國政府交通相關部門身居要職的話。
VN(csv3): "Bạn cũ của ngài Mototada" là một nhân vật giữ chức vụ\nkhá quan trọng trong hệ thống giao thông của chính phủ Trung Quốc.
CUR: "Bạn cũ của ngài Mototada" là một nhân vật giữ chức vụ\nkhá quan trọng trong hệ thống giao thông của chính phủ Trung Quốc.
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=2432 | char=双鉄 | src=csv3
JP: 「……ナインスターズのような豪華リレートレインを、\nもしも、仲国で走らせられるなら――」
TW: 「如果考慮在仲國開行像九星這樣的豪華接力列車——」
VN(csv3): 「……Một chuyến tàu du lịch chuyển tiếp sang trọng như Nine Stars,\nnếu có thể cho chạy ở Trung Quốc thì——」
CUR: 「……Một chuyến tàu du lịch chuyển tiếp sang trọng như Nine Stars,\nnếu có thể cho chạy ở Trung Quốc thì——」
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=2798 | char=稀咲 | src=csv3
JP: 「さて、忙しくなりそうだ。後東氏にアポを――\nいや、その前に仲国の件の整理が先か」
TW: 「這下可要忙起來了啊。得去約後東先生——不，應該先把仲國那邊的東西理好嗎」
VN(csv3): 「Chà, có vẻ sẽ bận rộn đây. Phải đặt lịch hẹn với ông Goto——\nÀ không, trước đó phải giải quyết vụ Trung Quốc đã.」
CUR: 「Chà, có vẻ sẽ bận rộn đây. Phải đặt lịch hẹn với ông Goto——\nÀ không, trước đó phải giải quyết vụ Trung Quốc đã.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1365 | char=双鉄 | src=csv3
JP: 「……仲国版ナインスターズ、か」
TW: 「……仲國版的九星嗎」
VN(csv3): 「……Nine Stars phiên bản Trung Quốc, sao.」
CUR: 「……Nine Stars phiên bản Trung Quốc, sao.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1944 | char=ハチロク | src=csv3
JP: 「\x%l大戦;#00ffc040;大戦%l;#;前には、仲国に輸出された機関車とレイルロオドも\nいたという記憶はあるのですけれど……」
TW: 「我倒是記得在\x%l大戦;#00ffc040;大戰%l;#;以前，曾經向仲國出口過機車和鐵路人偶，不過……」
VN(csv3): 「Em nhớ là trước \x%l大戦;#00ffc040;Đại chiến%l;#;, cũng từng có đầu máy xe lửa và Railord\nđược xuất khẩu sang Trung Quốc……」
CUR: 「Em nhớ là trước \x%l大戦;#00ffc040;Đại chiến%l;#;, cũng từng có đầu máy xe lửa và Railord\nđược xuất khẩu sang Trung Quốc……」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1885 | char=機内放送 | src=csv3
JP: 「女士們、先生們。\n歓迎乗坐仲国国際航空公司248次副丘前往北琴的航班」
TW: 「女士們，先生們。感謝您乘坐仲國國際航空公司第２４８次，由福岡飛往北琴的航班」
VN(csv3): 「Thưa quý bà, quý ông.\nChào mừng quý khách đã lên chuyến bay số 248 của Hãng hàng không Quốc tế Trung Quốc từ Fukuoka đến Bắc Cầm.」
CUR: 「Thưa quý bà, quý ông.\nChào mừng quý khách đã lên chuyến bay số 248 của Hãng hàng không Quốc tế Trung Quốc từ Fukuoka đến Bắc Cầm.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1704 | char=双鉄 | src=csv3
JP: 「仲国語は全くわからん――。\nあ、いや――」
TW: 「仲文我完全聽不懂啊——啊，慢著——」
VN(csv3): 「Anh hoàn toàn không hiểu tiếng Trung——\nÀ, không——」
CUR: 「Anh hoàn toàn không hiểu tiếng Trung——\nÀ, không——」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1938 | char=双鉄 | src=csv3
JP: 「仲国国際航空248便へのご搭乗ありがとうございます。\nこの飛行機は、[ふくおか,1]副丘発[ぺきん,1]北琴いき――むっ」
TW: 「感謝您乘坐仲國國際航空公司２４８次航班。這架飛機是由福岡飛往北琴——哦」
VN(csv3): 「Cảm ơn quý khách đã lên chuyến bay số 248 của Hãng hàng không Quốc tế Trung Quốc.\nChuyến bay này khởi hành từ Fukuoka đến Bắc Cầm——hửm.」
CUR: 「Cảm ơn quý khách đã lên chuyến bay số 248 của Hãng hàng không Quốc tế Trung Quốc.\nChuyến bay này khởi hành từ Fukuoka đến Bắc Cầm——hửm.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1942 | char=日々姫 | src=csv3
JP: 「ナインスターズの仲国版なんてまるで検討もつかんけん。\n材料、集められるだけ集めとかんと」
TW: 「我們對九星仲國版還完全是一頭霧水的狀況咧。所以當然要儘可能多地收集材料咯」
VN(csv3): 「Phiên bản Trung Quốc của Nine Stars thì em hoàn toàn mù tịt mà.\nNên phải thu thập tư liệu càng nhiều càng tốt thôi.」
CUR: 「Phiên bản Trung Quốc của Nine Stars thì em hoàn toàn mù tịt mà.\nNên phải thu thập tư liệu càng nhiều càng tốt thôi.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1900 | char=日々姫 | src=csv3
JP: 「っていうか、レイルロオドば見慣れんのなら――\nあ！　その前に。ＣＡさんば、仲国の方ですか？」
TW: 「如果不是經常見到鐵路人偶——哦，對了，請問空服小姐，您是仲國人嗎？」
VN(csv3): 「Mà nếu đã không quen nhìn thấy Railord thì——\nA! Trước đó. Cô CA là người Trung Quốc sao?」
CUR: 「Mà nếu đã không quen nhìn thấy Railord thì——\nA! Trước đó. Cô CA là người Trung Quốc sao?」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1366 | char=ハチロク | src=csv3
JP: 「……仲国の鉄道は、\nそこまで廃れてしまっているのでしょうか？」
TW: 「……仲國的鐵路，竟然荒廢到這等地步了嗎？」
VN(csv3): 「……Đường sắt Trung Quốc,\nđã lụi tàn đến mức đó rồi sao?」
CUR: 「……Đường sắt Trung Quốc,\nđã lụi tàn đến mức đó rồi sao?」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2112 | char=双鉄 | src=csv3
JP: 「さぁ、どうだろう。『仲国版ナインスターズを』という\n話がでてくるくらいなら、発展の意思はあるのだろうが」
TW: 「誰知道呢。但會有“仲國版九星”這樣的想法，至少說明還是有意繼續發展的吧」
VN(csv3): 「Chà, ai biết được. Nếu đã có chuyện\n『Nine Stars phiên bản Trung Quốc』 thì chắc là họ có ý định phát triển.」
CUR: 「Chà, ai biết được. Nếu đã có chuyện\n『Nine Stars phiên bản Trung Quốc』 thì chắc là họ có ý định phát triển.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1847 | char=日々姫 | src=csv3
JP: 「うん。八月の一日。年内に仲国視察に来てほしいって。\nにぃにとポーレットさんとわたしがご指名で」
TW: 「嗯，是在八月一日。她說希望在年內能去仲國考察一次，還點名要阿哥、波萊特和我去」
VN(csv3): 「Vâng. Ngày 1 tháng 8. Họ muốn chúng ta đến Trung Quốc khảo sát trong năm nay.\nChỉ đích danh anh hai, chị Paulette và em.」
CUR: 「Vâng. Ngày 1 tháng 8. Họ muốn chúng ta đến Trung Quốc khảo sát trong năm nay.\nChỉ đích danh anh hai, chị Paulette và em.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2079 | char=ハチロク | src=csv3
JP: 「視察の目的は――\n『仲国版ナインスタアズの、コンセプト案の立案』」
TW: 「考察的目的則是——“草擬仲國版九星的設計方案”」
VN(csv3): 「Mục đích của chuyến khảo sát là——\n『Lập dự án ý tưởng cho Nine Stars phiên bản Trung Quốc』.」
CUR: 「Mục đích của chuyến khảo sát là——\n『Lập dự án ý tưởng cho Nine Stars phiên bản Trung Quốc』.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2153 | char=日々姫 | src=csv3
JP: 「『それに、わたし――\n[ちゅうごくてつ,2]仲国鉄もかじっちゃってるんです～～』って！」
TW: 「還說什麼“話說回來，我對仲國鐵也是相當了解啊～～”！」
VN(csv3): 「『Với lại, em——\ncũng có tìm hiểu chút ít về Đường sắt Trung Quốc rồi~~』 nữa!」
CUR: 「『Với lại, em——\ncũng có tìm hiểu chút ít về Đường sắt Trung Quốc rồi~~』 nữa!」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1385 | char=双鉄 | src=csv3
JP: 「……だったな。まさか仲国の鉄道が、日ノ本のマニアの守備範囲に入っているとは、想像だにしていなかったが」
TW: 「……是啊。真想不到，日本鐵路迷竟然連仲國的鐵路都有涉獵」
VN(csv3): 「……Đúng là vậy. Không ngờ đường sắt Trung Quốc lại nằm trong phạm vi hiểu biết của một người đam mê đường sắt ở Hinomoto, thật không thể tưởng tượng nổi.」
CUR: 「……Đúng là vậy. Không ngờ đường sắt Trung Quốc lại nằm trong phạm vi hiểu biết của một người đam mê đường sắt ở Hinomoto, thật không thể tưởng tượng nổi.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1330 | char=monologue | src=csv3
JP: ……ポーレットが市長であることを知った上での、\n仲国側からのアイディアだと、稀咲は密かに教えてくれた。
TW: ……稀咲悄悄跟我說過，仲國方面是在得知波萊特是市長後提出的方案。
VN(csv3): ……Kisaki đã bí mật cho tôi biết, đó là ý tưởng từ phía Trung Quốc\nsau khi họ biết Paulette là thị trưởng.
CUR: ……Kisaki đã bí mật cho tôi biết, đó là ý tưởng từ phía Trung Quốc\nsau khi họ biết Paulette là thị trưởng.
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1863 | char=双鉄 | src=csv3
JP: 「仲国への入国手続に手間取るかもしれないと、\nそこは警告されていたな」
TW: 「在仲國入境可能會花些功夫，對方已經提早通知過我們了」
VN(csv3): 「Họ đã cảnh báo rằng,\nviệc làm thủ tục nhập cảnh vào Trung Quốc có thể sẽ mất thời gian.」
CUR: 「Họ đã cảnh báo rằng,\nviệc làm thủ tục nhập cảnh vào Trung Quốc có thể sẽ mất thời gian.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2076 | char=日々姫 | src=csv3
JP: 「簡単にいうと、仲国でも、私のこのタブレットで、\nインターネットを使えるようにする仕組みのこと」
TW: 「簡單說，就是讓我們在仲國，也能用平板電腦連接網路的東西」
VN(csv3): 「Nói đơn giản thì, đó là một hệ thống giúp em\ncó thể sử dụng Internet bằng chiếc máy tính bảng này ngay cả ở Trung Quốc.」
CUR: 「Nói đơn giản thì, đó là một hệ thống giúp em\ncó thể sử dụng Internet bằng chiếc máy tính bảng này ngay cả ở Trung Quốc.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2203 | char=ハチロク | src=csv3
JP: 「！！？　仲国のいんたあねっとと\n日ノ本のいんたあねっとは別物なのでございますか？」
TW: 「！！？仲國的網路和日本的網路是不一樣的嗎？」
VN(csv3): 「!!? Internet của Trung Quốc\nvà Internet của Hinomoto là hai thứ khác nhau sao ạ?」
CUR: 「!!? Internet của Trung Quốc\nvà Internet của Hinomoto là hai thứ khác nhau sao ạ?」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1790 | char=ハチロク | src=audit
JP: 「ああ、仲国でいんたあねっと線に乗るには、\n仲国の事業者の定期券が必要となるわけですね？」
TW: 「哦，如果要乘仲國網路線路的話，就需要仲國的公司的定期票了，對吧？」
VN(csv3): 「A, vậy là để đi tuyến Internet ở Trung Quốc,\nthì cần phải có vé tháng của nhà cung cấp ở Trung Quốc đúng không ạ?」
CUR: 「A, vậy là để đi tuyến Internet ở Trung Quốc,\nthì cần phải có vé định kỳ của nhà cung cấp ở Trung Quốc đúng không ạ?」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2035 | char=日々姫 | src=audit
JP: 「そそ。で。レンタルwifiがレンタル定期券で――\nVPNば、仲国では使えない車内設備を使えるチケット！」
TW: 「沒錯。所以，隨身Ｗｉ－Ｆｉ就是租借式的定期票，而ＶＰＮ則相當於使用那些在仲國不能使用的車內設施的票啦！」
VN(csv3): 「Đúng đúng. Và wifi thuê chính là vé tháng cho thuê——\nCòn VPN là vé cho phép sử dụng các trang thiết bị trên tàu mà bình thường không dùng được ở Trung Quốc!」
CUR: 「Đúng đúng. Và wifi thuê chính là vé định kỳ cho thuê——\nCòn VPN là vé cho phép sử dụng các trang thiết bị trên tàu mà bình thường không dùng được ở Trung Quốc!」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2511 | char=monologue | src=csv3
JP: 仲国語、詠語、そうして日ノ本語で順次のアナウンス。『あと15分ほどで北琴空港に着陸』だ。
TW: 機內依次以仲文、英語及日語，廣播通知我們“十五分鐘後在北琴機場降落”。
VN(csv3): Thông báo lần lượt bằng tiếng Trung, tiếng Anh, rồi đến tiếng Hinomoto. 『Khoảng 15 phút nữa sẽ hạ cánh xuống sân bay Bắc Cầm』.
CUR: Thông báo lần lượt bằng tiếng Trung, tiếng Anh, rồi đến tiếng Hinomoto. 『Khoảng 15 phút nữa sẽ hạ cánh xuống sân bay Bắc Cầm』.
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2143 | char=日々姫 | src=csv3
JP: 「そんなら！　指紋のことも報告書に書けばよかとね！\n仲国の人たちの安全の役にたつようになるかもしれんし」
TW: 「這樣的話，就把指紋這事也寫進報告裡好了！說不定能為保障仲國人民安全起到一點作用呢」
VN(csv3): 「Vậy thì! Ghi cả chuyện dấu vân tay vào báo cáo là được mà!\nBiết đâu lại giúp ích cho sự an toàn của người dân Trung Quốc thì sao.」
CUR: 「Vậy thì! Ghi cả chuyện dấu vân tay vào báo cáo là được mà!\nBiết đâu lại giúp ích cho sự an toàn của người dân Trung Quốc thì sao.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2049 | char=双鉄 | src=csv3
JP: 「観光地としての――無論、ビジネスの相手としてもの\n――仲国の国際的な評価が、高まっている現れだろうな」
TW: 「畢竟無論是旅遊方面還是商業方面，如今的仲國在國際上的評價都在不斷提高吧」
VN(csv3): 「Với tư cách là một địa điểm du lịch——tất nhiên là cả với tư cách là đối tác kinh doanh\n——đây chắc hẳn là minh chứng cho thấy đánh giá quốc tế về Trung Quốc đang ngày càng tăng cao.」
CUR: 「Với tư cách là một địa điểm du lịch——tất nhiên là cả với tư cách là đối tác kinh doanh\n——đây chắc hẳn là minh chứng cho thấy đánh giá quốc tế về Trung Quốc đang ngày càng tăng cao.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2185 | char=双鉄 | src=csv3
JP: 「言葉の問題は確かにあろうが、共感ならば、\n仲国のレイルロオドと通じあえるものが恐らくあろう」
TW: 「雖然語言方面的問題不可忽視，但通過共鳴的話，應該還是能夠和仲國的鐵路人偶溝通吧」
VN(csv3): 「Vấn đề ngôn ngữ thì chắc chắn là có, nhưng nếu là \x%l共感;#00ffc040;cộng cảm%l;#;,\nthì có lẽ em sẽ giao tiếp được với các Railord của Trung Quốc đấy.」
CUR: 「Vấn đề ngôn ngữ thì chắc chắn là có, nhưng nếu là \x%l共感;#00ffc040;cộng cảm%l;#;,\nthì có lẽ em sẽ giao tiếp được với các Railord của Trung Quốc đấy.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1943 | char=双鉄 | src=audit
JP: 「僕らには捉え得ぬ、『仲国のレイルロオドから見た\n仲国の鉄路』を。ハチロク。お前には捉えてほしい」
TW: 「我們難以了解到的“仲國鐵路人偶眼中的仲國鐵路”，就全部交給你負責了，八六」
VN(csv3): 「Thứ mà chúng ta không thể nắm bắt được, 『Tuyến đường sắt Trung Quốc\nqua góc nhìn của Railord Trung Quốc』. Hachiroku. Anh muốn em nắm bắt điều đó.」
CUR: 「Thứ mà chúng ta không thể nắm bắt được, 『Tuyến đường sắt Trung Quốc\nqua góc nhìn của Railord Trung Quốc』. Hachiroku. Tôi muốn em nắm bắt điều đó.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2072 | char=ハチロク | src=csv3
JP: 「仲国のレイルロオドたちからみた、仲国鉄路の長所や\n短所。改善点や要望などを、わたくしが聞き取り集める」
TW: 「站在仲國鐵路人偶的立場上所看到的仲國鐵路的優點和缺點，以及可以或希望改進之處，就都由我來了解收集」
VN(csv3): 「Ưu điểm và nhược điểm của tuyến đường sắt Trung Quốc qua góc nhìn của các Railord Trung Quốc.\nEm sẽ lắng nghe và thu thập những điểm cần cải thiện, những nguyện vọng của họ.」
CUR: 「Ưu điểm và nhược điểm của tuyến đường sắt Trung Quốc qua góc nhìn của các Railord Trung Quốc.\nEm sẽ lắng nghe và thu thập những điểm cần cải thiện, những nguyện vọng của họ.」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2186 | char=双鉄 | src=csv3
JP: 「視察とはいえ、せっかくのはじめての海外旅行だ。\n楽しもう――仕事自体を。そうして、仲国という国を！」
TW: 「雖說是考察，但也是難得的初次出國旅行。好好享受這次的工作以及仲國的風土人情吧！」
VN(csv3): 「Dù là đi khảo sát, nhưng hiếm khi có dịp ra nước ngoài lần đầu tiên.\nHãy tận hưởng nào——chính công việc này. Và cả đất nước Trung Quốc nữa!」
CUR: 「Dù là đi khảo sát, nhưng hiếm khi có dịp ra nước ngoài lần đầu tiên.\nHãy tận hưởng nào——chính công việc này. Và cả đất nước Trung Quốc nữa!」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2278 | char=姜 | src=csv3
JP: 「はじめまして。[きょう　　ようこう,2]姜叶煌と申します。\n仲国国務院、鉄道部の副部長秘書です」
TW: 「大家好，我叫姜葉煌。在仲國國務院，任交通運輸部副部長秘書一職」
VN(csv3): 「Rất vui được gặp mọi người. Tôi là Jiang Yehuang.\nThư ký Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trung Quốc.」
CUR: 「Rất vui được gặp mọi người. Tôi là Jiang Yehuang.\nThư ký Thứ trưởng Bộ Đường sắt, Quốc vụ viện Trung Quốc.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2074 | char=姜 | src=csv3
JP: 「我が仲国は総人口13億強の巨大国家です。\n北琴空港の年間利用客数も、1億人を優に超えます」
TW: 「仲國是擁有超過１３億人口的巨大國家。僅以北琴機場為例，每年的旅客吞吐量就輕鬆超過一億人次」
VN(csv3): 「Zhongguo của chúng tôi là một quốc gia khổng lồ với dân số hơn 1,3 tỷ người.\nChỉ tính riêng lượng hành khách qua sân bay Beiqin hàng năm cũng đã dễ dàng vượt mức 100 triệu người rồi.」
CUR: 「Zhongguo của chúng tôi là một quốc gia khổng lồ với dân số hơn 1,3 tỷ người.\nChỉ tính riêng lượng hành khách qua sân bay Beiqin hàng năm cũng đã dễ dàng vượt mức 100 triệu người rồi.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=1703 | char=双鉄 | src=csv3
JP: 「その更に三倍、か。しかも仲国は広大だ。\n同クラスの空港も、恐らく複数箇所あるのだろう」
TW: 「……這裡直接是日本的三倍嗎。而且仲國幅員遼闊，同樣等級的機場恐怕也不止一處吧」
VN(csv3): 「……Gấp ba lần chỗ đó sao. Hơn nữa Zhongguo lại vô cùng rộng lớn.\nNhững sân bay cùng đẳng cấp chắc hẳn cũng có không ít đâu nhỉ.」
CUR: 「……Gấp ba lần chỗ đó sao. Hơn nữa Zhongguo lại vô cùng rộng lớn.\nNhững sân bay cùng đẳng cấp chắc hẳn cũng có không ít đâu nhỉ.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=1651 | char=双鉄 | src=csv3
JP: 「『仲国視察と、仲国版ナインスターズに関する立案』\n……その理由を探すこともまた、視察の一部なのですね」
TW: 「“前往仲國考察，以及草擬仲國版九星的設計方案”……看來找出更深層次的原因也是考察的目的之一啊」
VN(csv3): 「『Khảo sát Zhongguo và lập kế hoạch cho Nine Stars phiên bản Zhongguo』\n……Việc tìm ra lý do cho yêu cầu đó cũng là một phần của cuộc khảo sát nhỉ.」
CUR: 「『Khảo sát Zhongguo và lập kế hoạch cho Nine Stars phiên bản Zhongguo』\n……Việc tìm ra lý do cho yêu cầu đó cũng là một phần của cuộc khảo sát nhỉ.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2731 | char=西瓜 | src=csv3
JP: 「それでは西瓜はみなさんを、北琴駅――\n仲国最大のターミナル駅に、ご案内します！」
TW: 「那西瓜就帶大家去北琴站——仲國最大的總站！」
VN(csv3): 「Vậy thì Suika sẽ dẫn mọi người đến ga Beiqin——\nga đầu mối lớn nhất của Zhongguo!」
CUR: 「Vậy thì Suika sẽ dẫn mọi người đến ga Beiqin——\nga đầu mối lớn nhất của Zhongguo!」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2265 | char=姜 | src=csv3
JP: 「仲国では、駅施設は保安の対象となるのです。\n外国人が写真撮影をすると、身体検査をされかねません」
TW: 「在我們仲國，車站設施也屬於安保對象，要是外國人在這裡拍照，有可能會被搜身」
VN(csv3): 「Ở Zhongguo, các cơ sở nhà ga là đối tượng được bảo vệ an ninh.\nNếu người nước ngoài chụp ảnh, rất có thể sẽ bị kiểm tra thân thể đấy.」
CUR: 「Ở Zhongguo, các cơ sở nhà ga là đối tượng được bảo vệ an ninh.\nNếu người nước ngoài chụp ảnh, rất có thể sẽ bị kiểm tra thân thể đấy.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2354 | char=西瓜 | src=csv3
JP: 「西瓜の知る範囲で、仲国には、日ノ本的な『小さな駅』。\n改札とホームのみといった構造の駅は存在しません」
TW: 「就西瓜所知，在仲國並沒有日本那種，只設有檢票口和站台的“小站”」
VN(csv3): 「Trong phạm vi hiểu biết của Suika, ở Zhongguo không tồn tại những 『nhà ga nhỏ』 mang phong cách Hinomoto.\nTức là những nhà ga chỉ có cấu trúc gồm cổng soát vé và sân ga.」
CUR: 「Trong phạm vi hiểu biết của Suika, ở Zhongguo không tồn tại những 『nhà ga nhỏ』 mang phong cách Hinomoto.\nTức là những nhà ga chỉ có cấu trúc gồm cổng soát vé và sân ga.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2352 | char=西瓜 | src=csv3
JP: 「西瓜の知る全ての仲国の鉄道駅には、\n入場券というシステムがありません」
TW: 「就西瓜所知，全仲國的火車站，都不賣所謂門票的」
VN(csv3): 「Trong tất cả các nhà ga đường sắt ở Zhongguo mà Suika biết,\nkhông có hệ thống vé vào cửa đâu.」
CUR: 「Trong tất cả các nhà ga đường sắt ở Zhongguo mà Suika biết,\nkhông có hệ thống vé vào cửa đâu.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2462 | char=西瓜 | src=csv3
JP: 「はい！　西瓜もわかりやすいと思います。\n仲国でも快速は快速。発音は『Kuai－su』ですから」
TW: 「是的！西瓜也覺得很直觀。仲國的快速和日文文字相同，讀作“Ｋｕａｉ－ｓｕ”」
VN(csv3): 「Vâng! Suika cũng thấy rất dễ hiểu.\nỞ Zhongguo, tàu nhanh cũng là tàu nhanh. Phát âm là 『Kuai-su』 mà.」
CUR: 「Vâng! Suika cũng thấy rất dễ hiểu.\nỞ Zhongguo, tàu nhanh cũng là tàu nhanh. Phát âm là 『Kuai-su』 mà.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2259 | char=西瓜 | src=csv3
JP: 「仲国には、さらに特快の上の列車種別もあります。\n直達特快――Zhi－da Te－kuai。これが最速のZ列車です」
TW: 「在仲國，還有一種位居特快之上的列車。直達特快——Ｚｈｉ－ｄａ　Ｔｅ－ｋｕａｉ，就是最快的Ｚ列車了」
VN(csv3): 「Ở Zhongguo, còn có loại tàu cao cấp hơn cả Đặc khoái nữa.\nĐó là Trực đạt đặc khoái——Zhi-da Te-kuai. Đây là tàu chữ Z nhanh nhất!」
CUR: 「Ở Zhongguo, còn có loại tàu cao cấp hơn cả Đặc khoái nữa.\nĐó là Trực đạt đặc khoái——Zhi-da Te-kuai. Đây là tàu chữ Z nhanh nhất!」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2075 | char=日々姫 | src=csv3
JP: 「すごかね、仲国の鉄道」
TW: 「仲國鐵路真厲害呀」
VN(csv3): 「Đường sắt của Zhongguo tuyệt thật đấy.」
CUR: 「Đường sắt của Zhongguo tuyệt thật đấy.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2481 | char=西瓜 | src=csv3
JP: 「ものがあります。仲国鉄道歴史館という施設が、\n北琴の郊外に存在しています」
TW: 「有的，名字叫仲國鐵路博物館，就位於北琴近郊」
VN(csv3): 「Có một nơi như vậy ạ. Có một cơ sở tên là Bảo tàng Lịch sử Đường sắt Zhongguo,\nnằm ở vùng ngoại ô Beiqin.」
CUR: 「Có một nơi như vậy ạ. Có một cơ sở tên là Bảo tàng Lịch sử Đường sắt Zhongguo,\nnằm ở vùng ngoại ô Beiqin.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2237 | char=日々姫 | src=csv3
JP: 「あ、そこ！　そこももちろん見てみたかとよ。\n仲国の鉄道について、ザラっとでも勉強したかけん」
TW: 「啊，那裡好！那裡當然也得去！早就想了解一下仲國鐵路的知識咧」
VN(csv3): 「A, chỗ đó! Tất nhiên là em cũng muốn đi xem chỗ đó rồi.\nEm muốn học hỏi thêm về đường sắt của Zhongguo, dù chỉ là sơ qua.」
CUR: 「A, chỗ đó! Tất nhiên là em cũng muốn đi xem chỗ đó rồi.\nEm muốn học hỏi thêm về đường sắt của Zhongguo, dù chỉ là sơ qua.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2687 | char=日々姫 | src=csv3
JP: 「仲国の人が、北琴から何泊かの旅行にいく！\nみたいなとき、メジャーな旅先ってどこですか？」
TW: 「這樣問好了，在“要從北琴出去玩幾天！”的時候，仲國人大多選擇去哪裡旅行呢？」
VN(csv3): 「Khi người Zhongguo đi du lịch vài ngày từ Beiqin!\nNhững lúc như thế, điểm đến phổ biến nhất là ở đâu ạ?」
CUR: 「Khi người Zhongguo đi du lịch vài ngày từ Beiqin!\nNhững lúc như thế, điểm đến phổ biến nhất là ở đâu ạ?」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=1678 | char=ハチロク | src=csv3
JP: 「……ああ、さすが仲国は広大なのですね。\n候補だけでも多すぎて、わたくし、目がまわりそうです」
TW: 「……噢噢，切身感受到仲國的地大物博了。選擇實在太多，我已經感到眼花撩亂」
VN(csv3): 「……Oa, Zhongguo quả thực rộng lớn quá nhỉ.\nChỉ nghe danh sách ứng cử viên thôi mà tôi đã thấy chóng mặt rồi.」
CUR: 「……Oa, Zhongguo quả thực rộng lớn quá nhỉ.\nChỉ nghe danh sách ứng cử viên thôi mà tôi đã thấy chóng mặt rồi.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2715 | char=双鉄 | src=csv3
JP: 「ならば別方面から考えてみよう。ハチロクは、\n仲国で乗りたい列車や、見たい列車などはあるか？」
TW: 「那就換個思路吧。八六你有想在仲國乘坐，或是親眼看一看的列車嗎？」
VN(csv3): 「Vậy thì hãy thử suy nghĩ từ một khía cạnh khác xem sao. Hachiroku,\ncô có chuyến tàu nào muốn đi, hay muốn xem ở Zhongguo không?」
CUR: 「Vậy thì hãy thử suy nghĩ từ một khía cạnh khác xem sao. Hachiroku,\ncô có chuyến tàu nào muốn đi, hay muốn xem ở Zhongguo không?」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2401 | char=ハチロク | src=csv3
JP: 「わたくしは――もしも仲国で蒸気機関車が現役ならば、\nそのこにあってみたいです」
TW: 「我……如果仲國還有投入使用的蒸汽機車，我想去見一見」
VN(csv3): 「Tôi——nếu ở Zhongguo vẫn còn đầu máy hơi nước đang hoạt động,\nthì tôi muốn đi xem đứa bé đó ạ.」
CUR: 「Tôi——nếu ở Zhongguo vẫn còn đầu máy hơi nước đang hoạt động,\nthì tôi muốn đi xem đứa bé đó ạ.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2611 | char=西瓜 | src=csv3
JP: 「西瓜の専門は仲国国鉄の線路がつながっている範囲です。\nその地域外のことは要悉究。少し調べる必要があります」
TW: 「西瓜對仲國國鐵線路所到之處自然是了如指掌，但除此之外就尚待悉究，需要做一番調查了」
VN(csv3): 「Chuyên môn của Suika là trong phạm vi các tuyến đường sắt quốc gia Zhongguo được kết nối.\nNhững khu vực ngoài đó thì cần phải tất cứu. Cần phải điều tra một chút ạ.」
CUR: 「Chuyên môn của Suika là trong phạm vi các tuyến đường sắt quốc gia Zhongguo được kết nối.\nNhững khu vực ngoài đó thì cần phải tất cứu. Cần phải điều tra một chút ạ.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2920 | char=monologue | src=csv3
JP: たとえ機関車の新規開発が長期に渡り止まっていようと、\n仲国には、日ノ本における大廃線はなかったと――
TW: 儘管新型機車的開發工作已經長期停擺，仲國卻並未發生像日本國那樣的大廢線——
VN(csv3): Cho dù việc phát triển đầu máy mới đã bị đình trệ trong một thời gian dài,\nnhưng ở Zhongguo, không hề có cuộc đại bãi bỏ các tuyến đường sắt như ở Hinomoto——
CUR: Cho dù việc phát triển đầu máy mới đã bị đình trệ trong một thời gian dài,\nnhưng ở Zhongguo, không hề có cuộc đại bãi bỏ các tuyến đường sắt như ở Hinomoto——
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2582 | char=西瓜 | src=csv3
JP: 「素敵なデザインと褒めてもらって西瓜は嬉しいです！\n[ｌｕ－ｂｉ－ｃｈｅ,2]緑比車――[りょくひしゃ,2]緑比車は、仲国の鉄道の象徴です！」
TW: 「能在外觀上得到讚揚，西瓜好高興！[ｌü－ｐｉ－ｃｈｅ,2]綠比車可是仲國鐵路的象徵呢！」
VN(csv3): 「Được khen là thiết kế tuyệt đẹp, Suika vui lắm!\nLü-pi-che——Lục Bỉ Xa là biểu tượng của đường sắt Zhongguo đấy!」
CUR: 「Được khen là thiết kế tuyệt đẹp, Suika vui lắm!\nLü-pi-che——Lục Bỉ Xa là biểu tượng của đường sắt Zhongguo đấy!」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2073 | char=西瓜 | src=csv3
JP: 「仲国は、この緑。車輌更新があってもずっと変わらない、\nまさしく、仲国国鉄の伝統色です！」
TW: 「仲國就是這一抹綠色，即便車輛進行了翻新也從不改變。說這是仲國國鐵的傳統顏色毫不為過！」
VN(csv3): 「Zhongguo chính là màu xanh lá này. Dù có đổi mới toa xe thì vẫn luôn không đổi,\nquả thực, đây chính là màu sắc truyền thống của Đường sắt Quốc gia Zhongguo!」
CUR: 「Zhongguo chính là màu xanh lá này. Dù có đổi mới toa xe thì vẫn luôn không đổi,\nquả thực, đây chính là màu sắc truyền thống của Đường sắt Quốc gia Zhongguo!」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2175 | char=ハチロク | src=csv3
JP: 「日ノ本と、帝鉄とは――まったく別の選択をして。\nまったく別の鉄路が――仲国では伸び、生きたのですね」
TW: 「和帝國鐵路選擇了完全不同的方向。在仲國生龍活虎地延伸著的，已是和日本完全不同的鐵路了」
VN(csv3): 「Hinomoto và Đường sắt Hoàng gia——đã đưa ra những lựa chọn hoàn toàn khác biệt.\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」
CUR: 「Hinomoto và Đường sắt Hoàng gia——đã đưa ra những lựa chọn hoàn toàn khác biệt.\nMột tuyến đường sắt hoàn toàn khác——đã vươn dài và tồn tại ở Zhongguo nhỉ.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2996 | char=monologue | src=audit
JP: 仲国版のナインスターズ計画の草案を立案できたなら、\nその経験は、必ず御一夜鉄道に……も……？
TW: 如果能成功擬定仲國版九星的設計方案的話，這過程中積累的經驗，想必也能對御一夜鐵路——
VN(csv3): Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohito……?
CUR: Nếu có thể lập ra được bản thảo cho kế hoạch Nine Stars phiên bản Zhongguo,\nthì kinh nghiệm đó nhất định cũng sẽ…… mang lại lợi ích cho Đường sắt Ohitoyo……?
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=3074 | char=monologue | src=csv3
JP: きっぷ売り場で受けた警告を思い出す。\n“駅施設は、仲国では保安の対象”であるのなら――
TW: 我想到剛才在售票廳的經歷，如果“車站在仲國屬於安保對象”——
VN(csv3): Tôi chợt nhớ lại lời cảnh báo đã nhận được ở khu vực bán vé.\nNếu "cơ sở nhà ga là đối tượng được bảo vệ an ninh ở Zhongguo" thì——
CUR: Tôi chợt nhớ lại lời cảnh báo đã nhận được ở khu vực bán vé.\nNếu "cơ sở nhà ga là đối tượng được bảo vệ an ninh ở Zhongguo" thì——
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=3281 | char=monologue | src=csv3
JP: なにがあったかと顔を向ければ、西瓜の方へ、制服姿\n――仲国国鉄の制服姿の――青年が小走りに駆けてくる。
TW: 順著西瓜的目光看去，一位身著制服——身著仲國國鐵制服的青年正朝我們小跑過來。
VN(csv3): Khi tôi quay mặt lại xem có chuyện gì, thì thấy một thanh niên mặc đồng phục\n——đồng phục của Đường sắt Quốc gia Zhongguo——đang chạy chậm về phía Suika.
CUR: Khi tôi quay mặt lại xem có chuyện gì, thì thấy một thanh niên mặc đồng phục\n——đồng phục của Đường sắt Quốc gia Zhongguo——đang chạy chậm về phía Suika.
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=3268 | char=monologue | src=csv3
JP: 言って、志寰君は制帽の中央に輝いている、\n仲国国鉄のマークを指差す。
TW: 邊說，志寰邊指著制帽正中閃閃發光的仲國國鐵標誌。
VN(csv3): Nói rồi, Zhihuan chỉ vào biểu tượng của Đường sắt Quốc gia Zhongguo\nđang tỏa sáng ở chính giữa chiếc mũ đồng phục.
CUR: Nói rồi, Zhihuan chỉ vào biểu tượng của Đường sắt Quốc gia Zhongguo\nđang tỏa sáng ở chính giữa chiếc mũ đồng phục.
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2679 | char=志寰 | src=csv3
JP: 「保安員さんは、仲国国鉄のための仕事をしています。\nだから事情の説明には、制服がとても役にたちました」
TW: 「這位保全也是在為仲國國鐵盡心盡力。所以在解釋情況的時候，這身制服就具備莫大的份量」
VN(csv3): 「Nhân viên an ninh đang làm việc cho Đường sắt Quốc gia Zhongguo.\nNên bộ đồng phục này đã giúp ích rất nhiều trong việc giải thích tình hình.」
CUR: 「Nhân viên an ninh đang làm việc cho Đường sắt Quốc gia Zhongguo.\nNên bộ đồng phục này đã giúp ích rất nhiều trong việc giải thích tình hình.」
--- 10_Chikuni | 仲国02_北琴の鉄道.txt.toml | key=2897 | char=monologue | src=csv3
JP: おっと、仲国語だ。
TW: 他們的對話突然切換成了仲文。
VN(csv3): Ôi chà, là tiếng Zhongguo.
CUR: Ôi chà, là tiếng Zhongguo.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2845 | char=monologue | src=audit
JP: おっと、電話か。\n姜さんは早口の仲国語でなにやら――っ！
TW: 真不巧，正趕上有電話進來。姜小姐以很快的語速用仲文和對方交流著。
VN(csv3): Ôi chà, có điện thoại.\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——!
CUR: Ôi chà, có điện thoại.\nCô Jiang đang nói gì đó bằng tiếng Zhongguo với tốc độ rất nhanh——Ư!
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2331 | char=西瓜 | src=csv3
JP: 「なぜかを西瓜は説明します。国繋号が繋ぐ二つの国と国。\nそれは、仲国と日ノ本のことだからです」
TW: 「西瓜這就為您說明。國系號所聯繫的，是兩個國家——仲國和日本國」
VN(csv3): 「Suika sẽ giải thích lý do tại sao. Hai quốc gia mà Quốc Hệ hiệu kết nối.\nĐó chính là Zhongguo và Hinomoto.」
CUR: 「Suika sẽ giải thích lý do tại sao. Hai quốc gia mà Quốc Hệ hiệu kết nối.\nĐó chính là Zhongguo và Hinomoto.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=1878 | char=ハチロク | src=csv3
JP: 「旧[まんてつ,1]漫鉄で働いた後――\n仲国国鉄でも活躍をしたのですね、このこは？」
TW: 「也就是說，她在前南曼鐵路服役之後，還在仲國國鐵大顯身手過囉？」
VN(csv3): 「Sau khi làm việc ở Đường sắt Nam Man cũ——\nĐứa bé này cũng đã hoạt động tích cực ở Đường sắt Quốc gia Zhongguo nhỉ?」
CUR: 「Sau khi làm việc ở Đường sắt Nam Man cũ——\nĐứa bé này cũng đã hoạt động tích cực ở Đường sắt Quốc gia Zhongguo nhỉ?」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2225 | char=志寰 | src=csv3
JP: 「そうです。一度は廃棄寸前にまで傷んだものの、\n仲国建国一周年を記念して修復され、再度活躍しました」
TW: 「正是如此。該車曾嚴重受損，差點遭到廢棄處理，但趕上仲國建國一周年而得以修復，再次活躍在鐵軌上」
VN(csv3): 「Đúng vậy. Dù từng bị hư hỏng đến mức suýt bị vứt bỏ,\nnhưng nó đã được phục hồi để kỷ niệm một năm thành lập Zhongguo, và lại tiếp tục hoạt động.」
CUR: 「Đúng vậy. Dù từng bị hư hỏng đến mức suýt bị vứt bỏ,\nnhưng nó đã được phục hồi để kỷ niệm một năm thành lập Zhongguo, và lại tiếp tục hoạt động.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2642 | char=monologue | src=csv3
JP: 旧漫州鉄道――というか旧漫州国は、\n日ノ本と仲国とが相争ったあの\x%l大戦;#00ffc040;大戦%l;#;の要因のひとつだ。
TW: 前南曼鐵路——準確說是前曼州國，說來也是當年日本國與仲國之間那場\x%l大戦;#00ffc040;大戰%l;#;的核心因素之一。
VN(csv3): Đường sắt Nam Man cũ——hay đúng hơn là Manzhouguo cũ,\nlà một trong những nguyên nhân dẫn đến \x%l大戦;#00ffc040;Đại chiến%l;#; giữa Hinomoto và Zhongguo.
CUR: Đường sắt Nam Man cũ——hay đúng hơn là Manzhouguo cũ,\nlà một trong những nguyên nhân dẫn đến \x%l大戦;#00ffc040;Đại chiến%l;#; giữa Hinomoto và Zhongguo.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2592 | char=monologue | src=csv3
JP: 西瓜がどれほど仲国を、日ノ本を、大事に想って\nくれているのかが、伝わってくる気さえする。
TW: 仲國，以及日本國在西瓜心中究竟有著怎樣的分量，在適才的一言一行中，體現得淋漓盡致。
VN(csv3): Tôi thậm chí còn cảm nhận được Suika\ntrân trọng Zhongguo, trân trọng Hinomoto đến nhường nào.
CUR: Tôi thậm chí còn cảm nhận được Suika\ntrân trọng Zhongguo, trân trọng Hinomoto đến nhường nào.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2384 | char=志寰 | src=csv3
JP: 「この歴史館には、[おおさか,1]逢坂で作られた蒸気機関車もいます。\n仲国と日ノ本のレールは、かつては繋がっていたんです」
TW: 「這座歷史博物館裡還有大阪生產的蒸汽機車。過去仲國和日本的軌道是有過緊密聯繫的」
VN(csv3): 「Trong bảo tàng lịch sử này, còn có những đầu máy hơi nước được chế tạo ở Osaka nữa.\nĐường ray của Zhongguo và Hinomoto, trước đây từng được kết nối với nhau đấy.」
CUR: 「Trong bảo tàng lịch sử này, còn có những đầu máy hơi nước được chế tạo ở Osaka nữa.\nĐường ray của Zhongguo và Hinomoto, trước đây từng được kết nối với nhau đấy.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2083 | char=西瓜 | src=csv3
JP: 「老師は、帝鉄を大いにライバル視して研究していました。\n老師だけでなく、私、西瓜も――仲国国鉄全体も」
TW: 「師父是將帝國鐵路視為一大勁敵而對其加以研究的。而且不僅是師父，我——西瓜，還有仲國國鐵所有人也都是」
VN(csv3): 「Sư phụ đã nghiên cứu Đường sắt Hoàng gia với tư cách là một đối thủ lớn.\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」
CUR: 「Sư phụ đã nghiên cứu Đường sắt Hoàng gia với tư cách là một đối thủ lớn.\nKhông chỉ Sư phụ, mà cả tôi, Suika——và toàn bộ Đường sắt Quốc gia Zhongguo cũng vậy.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2849 | char=monologue | src=csv3
JP: 西瓜の言葉と、この歴史館に収蔵されている、\n仲国国鉄ごく初期の、日ノ本製造の\x%l蒸機;#00ffc040;蒸機%l;#;たち。
TW: 結合西瓜所講，以及那些藏於這座博物館的仲國國鐵草創期時，曾使用的日本國產\x%l蒸気機関車;#00ffc040;蒸汽機車%l;#;。
VN(csv3): Lời nói của Suika, và những chiếc \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; do Hinomoto sản xuất từ thời kỳ đầu\ncủa Đường sắt Quốc gia Zhongguo đang được lưu giữ trong bảo tàng lịch sử này.
CUR: Lời nói của Suika, và những chiếc \x%l蒸機;#00ffc040;đầu máy hơi nước%l;#; do Hinomoto sản xuất từ thời kỳ đầu\ncủa Đường sắt Quốc gia Zhongguo đang được lưu giữ trong bảo tàng lịch sử này.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2251 | char=双鉄 | src=csv3
JP: 「かつての帝鉄は――少なくとも仲国国鉄の創設期には、\nライバル視されるに足る存在であったのか」
TW: 「當年的帝國鐵路——至少在仲國國鐵創設之初，絕對是一個值得被視為勁敵的存在」
VN(csv3): 「Đường sắt Hoàng gia ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」
CUR: 「Đường sắt Hoàng gia ngày xưa——ít nhất là vào thời kỳ đầu thành lập của Đường sắt Quốc gia Zhongguo,\nlà một sự tồn tại xứng đáng được xem như đối thủ sao.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=1556 | char=ハチロク | src=csv3
JP: 「『だから』。仲国国鉄は、[せんよんひゃくさんじゅうごみりき,6]1435mm軌――\n標準軌を選択したのですか？」
TW: 「“正因如此”，仲國國鐵才選擇了１４３５ｍｍ軌距的標準軌嗎？」
VN(csv3): 「『Vì vậy』. Đường sắt Quốc gia Zhongguo,\nđã chọn khổ 1435mm——khổ tiêu chuẩn sao?」
CUR: 「『Vì vậy』. Đường sắt Quốc gia Zhongguo,\nđã chọn khổ 1435mm——khổ tiêu chuẩn sao?」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=1882 | char=志寰 | src=csv3
JP: 「と、仲国国鉄も見込み、発展を期待していたそうです。\nけれど、大廃線が全てを大きく狂わせてしまった」
TW: 「仲國國鐵似乎也意識到了這一點，並靜待其發展成熟。但突如其來的大廢線，徹底打亂了全盤計劃」
VN(csv3): 「Đường sắt Quốc gia Zhongguo cũng đã dự đoán và kỳ vọng vào sự phát triển đó.\nNhưng cuộc Đại bãi bỏ các tuyến đường sắt đã làm đảo lộn mọi thứ.」
CUR: 「Đường sắt Quốc gia Zhongguo cũng đã dự đoán và kỳ vọng vào sự phát triển đó.\nNhưng cuộc Đại bãi bỏ các tuyến đường sắt đã làm đảo lộn mọi thứ.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2055 | char=志寰 | src=csv3
JP: 「父は、仲国国鉄を支えるべき次期機関車の、\n開発・選定に深く関わった、試験機関士でした」
TW: 「家父是與仲國國鐵下一代主力機車開發、選型密切相關的試車員」
VN(csv3): 「Cha tôi là một người lái tàu thử nghiệm,\nđã tham gia sâu vào việc phát triển và lựa chọn đầu máy thế hệ tiếp theo để hỗ trợ Đường sắt Quốc gia Zhongguo.」
CUR: 「Cha tôi là một người lái tàu thử nghiệm,\nđã tham gia sâu vào việc phát triển và lựa chọn đầu máy thế hệ tiếp theo để hỗ trợ Đường sắt Quốc gia Zhongguo.」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2641 | char=monologue | src=csv3
JP: 仲国に来てからのハチロクが、\nときおりにじませる口惜しさ。
TW: 到仲國以後，八六話語中不時顯現出絲絲憾意。
VN(csv3): Kể từ khi đến Zhongguo, Hachiroku\nthỉnh thoảng lại bộc lộ sự tiếc nuối.
CUR: Kể từ khi đến Zhongguo, Hachiroku\nthỉnh thoảng lại bộc lộ sự tiếc nuối.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2944 | char=monologue | src=csv3
JP: これでいい。仲国に来てからずうっと、どこかギクシャク不安定だったハチロクに、ようやく一本の芯が通った。
TW: 這樣就好。出發來中國之後一直不太對勁的八六總算又調整對了狀態。
VN(csv3): Thế này là được rồi. Hachiroku, người luôn có chút gượng gạo và bất ổn kể từ khi đến Zhongguo,\ncuối cùng cũng đã tìm lại được trục cốt lõi của mình.
CUR: Thế này là được rồi. Hachiroku, người luôn có chút gượng gạo và bất ổn kể từ khi đến Zhongguo,\ncuối cùng cũng đã tìm lại được trục cốt lõi của mình.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2132 | char=ハチロク | src=audit
JP: 「はじめての、仲国の列車。Z49列車。\n[こうがしゃ,2]硬臥車……三段寝台をお手配いただけたのですね」
TW: 「我們即將初次乘坐的仲國的列車，Ｚ４９次列車，硬臥車……應我們的要求安排了三層床鋪車廂的車票啊」
VN(csv3): 「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\n\x%lこうがしゃ;#00ffc040;Toa giường cứng%l;#;…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」
CUR: 「Chuyến tàu đầu tiên ở Zhongguo. Tàu Z49.\nToa giường cứng…… Mọi người đã sắp xếp cho chúng ta giường ba tầng nhỉ.」
--- 10_Chikuni | 仲国04_z49列車.txt.toml | key=1392 | char=双鉄 | src=csv3
JP: 「……よく描けているな。楽しげだ。\n旅に出る前の空気感は、日ノ本も仲国も変わらんな」
TW: 「……畫得不錯啊，歡欣雀躍的感覺撲面而來。果然出發旅行前的氣氛，仲日兩國並無二致」
VN(csv3): 「……Vẽ đẹp lắm. Rất có hồn.\nBầu không khí trước khi khởi hành cho một chuyến đi, dù là Hinomoto hay Zhongguo thì cũng không khác biệt mấy nhỉ.」
CUR: 「……Vẽ đẹp lắm. Rất có hồn.\nBầu không khí trước khi khởi hành cho một chuyến đi, dù là Hinomoto hay Zhongguo thì cũng không khác biệt mấy nhỉ.」
--- 10_Chikuni | 仲国04_z49列車.txt.toml | key=1671 | char=双鉄 | src=audit
JP: 「ハチロク。車掌さんの業務内容は、\n仲国も日ノ本も同じではないかと僕は思うぞ？」
TW: 「八六，要說列車長的工作內容，我覺得仲日兩國應該並無二致吧？」
VN(csv3): 「Hachiroku. Công việc của người trưởng tàu,\nanh nghĩ ở Zhongguo và Hinomoto cũng giống nhau thôi, đúng không?」
CUR: 「Hachiroku. Công việc của người trưởng tàu,\ntôi nghĩ ở Zhongguo và Hinomoto cũng giống nhau thôi, đúng không?」
--- 10_Chikuni | 仲国04_z49列車.txt.toml | key=1829 | char=ハチロク | src=csv3
JP: 「うふふ、日ノ本と仲国と。\n両方のサアビスのいいとこどりでございますね」
TW: 「嘻嘻，這是對仲日兩國的服務各取所長呀」
VN(csv3): 「Ufufu, Hinomoto và Zhongguo.\nĐây là sự kết hợp những điểm tốt nhất trong dịch vụ của cả hai bên nhỉ.」
CUR: 「Ufufu, Hinomoto và Zhongguo.\nĐây là sự kết hợp những điểm tốt nhất trong dịch vụ của cả hai bên nhỉ.」
--- 10_Chikuni | 仲国04_z49列車.txt.toml | key=2131 | char=西瓜 | src=csv3
JP: 「食堂車のことを、仲国では[ｃａｎｃｈｅ,1]餐車。[さんしゃ,1]餐車といいます。\n晩餐の餐という文字を書きますね」
TW: 「餐車在仲文裡讀作[ｃａｎｃｈｅ,1]餐車。餐就是晚餐的那個餐字」
VN(csv3): 「Ở Zhongguo, toa ăn được gọi là \x%lｃａｎｃｈｅ;#00ffc040;Can-che%l;#;. \x%lさんしゃ;#00ffc040;Xan-chơ%l;#;.\nĐược viết bằng chữ "Xan" trong bữa tối (Vãn xan) đấy ạ.」
CUR: 「Ở Zhongguo, toa ăn được gọi là \x%lｃａｎｃｈｅ;#00ffc040;Can-che%l;#;. \x%lさんしゃ;#00ffc040;Xan-chơ%l;#;.\nĐược viết bằng chữ "Xan" trong bữa tối (Vãn xan) đấy ạ.」
--- 10_Chikuni | 仲国04_z49列車.txt.toml | key=1857 | char=双鉄 | src=audit
JP: 「早く食べたいな。あの、姜さん。\n仲国では、食事の開始のときにはどのように」
TW: 「好想趕快嚐嚐啊。話說，姜小姐，在仲國，開始用餐之前有什麼習慣嗎」
VN(csv3): 「Muốn ăn quá đi. À, cô Jiang này.\nỞ Trung Quốc, khi bắt đầu bữa ăn mọi người thường làm thế nào vậy?」
CUR: 「Muốn ăn quá đi. À, cô Jiang này.\nỞ Zhongguo, khi bắt đầu bữa ăn mọi người thường làm thế nào vậy?」
--- 10_Chikuni | 仲国05_真夜中の餐車.txt.toml | key=3089 | char=monologue | src=csv3
JP: そうしてお湯は、仲国の寝台列車では、全乗客が。\n自動の給湯器から、いくらでも使えるものなのです。
TW: 至於杯中的熱水，在仲國的臥鋪車上，所有的乘客都可以在自動茶爐機那裡自由取用。
VN(csv3): Hơn nữa, trên tàu giường nằm của Trung Quốc, mọi hành khách\nđều có thể lấy nước nóng từ bình đun tự động bao nhiêu tùy thích.
CUR: Hơn nữa, trên tàu giường nằm của Trung Quốc, mọi hành khách\nđều có thể lấy nước nóng từ bình đun tự động bao nhiêu tùy thích.
--- 10_Chikuni | 仲国05_真夜中の餐車.txt.toml | key=2183 | char=西瓜 | src=csv3
JP: 「けれど、志寰が仲国国鉄の職員に採用された日。制服に、\n志寰の方が着られている姿を始めて目にした、あの日」
TW: 「然而，在志寰成為仲國國鐵職員的那一天，在我第一次見到他身著制服身姿的那一天」
VN(csv3): 「Nhưng, vào ngày Zhihuan được nhận làm nhân viên Đường sắt Quốc gia Trung Quốc. Ngày hôm đó,\nlần đầu tiên Suika nhìn thấy bóng dáng Zhihuan lọt thỏm trong bộ đồng phục.」
CUR: 「Nhưng, vào ngày Zhihuan được nhận làm nhân viên Đường sắt Quốc gia Trung Quốc. Ngày hôm đó,\nlần đầu tiên Suika nhìn thấy bóng dáng Zhihuan lọt thỏm trong bộ đồng phục.」
--- 10_Chikuni | 仲国05_真夜中の餐車.txt.toml | key=2749 | char=monologue | src=csv3
JP: ささやき声です。そのうえおそらく、仲国語。
TW: 她這樣輕聲細語道。而我沒猜錯的話，她說的應該是仲文。
VN(csv3): Một tiếng thì thầm. Hơn nữa có lẽ là tiếng Trung.
CUR: Một tiếng thì thầm. Hơn nữa có lẽ là tiếng Trung.
--- 10_Chikuni | 仲国05_真夜中の餐車.txt.toml | key=2595 | char=monologue | src=csv3
JP: だが仲国では、単純に不足を補充する。――島国と大陸と。\nそれは恐らく、資源そのものの多寡から生じる差異だろう。
TW: 但在仲國就是單純的對不足之處加以補充——這就是島國與大陸資源多寡所造成的差異吧。
VN(csv3): Nhưng ở Trung Quốc, họ đơn giản là bổ sung những gì còn thiếu. ――Quốc đảo và đại lục.\nĐó có lẽ là sự khác biệt nảy sinh từ sự phong phú của chính tài nguyên.
CUR: Nhưng ở Trung Quốc, họ đơn giản là bổ sung những gì còn thiếu. ――Quốc đảo và đại lục.\nĐó có lẽ là sự khác biệt nảy sinh từ sự phong phú của chính tài nguyên.
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=952 | char=日々姫 | src=csv3
JP: 「……仲国だぁ」
TW: 「……仲國啊」
VN(csv3): 「……Đúng là Trung Quốc á.」
CUR: 「……Đúng là Trung Quốc á.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1722 | char=ハチロク | src=csv3
JP: 「まこと……まことに仲国ですね」
TW: 「這還真是……仲國呢」
VN(csv3): 「Quả thật……quả thật là Trung Quốc nhỉ.」
CUR: 「Quả thật……quả thật là Trung Quốc nhỉ.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1364 | char=双鉄 | src=csv3
JP: 「ああ……確かに。\n――絵に描いたような、仲国だな」
TW: 「啊……確實。這真是仲國——簡直再標準不過的形象」
VN(csv3): 「À……đúng vậy.\n――Đúng là Trung Quốc như trong tranh vẽ.」
CUR: 「À……đúng vậy.\n――Đúng là Trung Quốc như trong tranh vẽ.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1331 | char=西瓜 | src=csv3
JP: 「先生たちは、北琴空港からずっと、\n仲国に入国されていますが」
TW: 「各位從抵達北琴機場時，就已經在仲國了啊」
VN(csv3): 「Mọi người đã nhập cảnh vào Trung Quốc\ntừ lúc ở sân bay Bắc Cầm rồi mà.」
CUR: 「Mọi người đã nhập cảnh vào Trung Quốc\ntừ lúc ở sân bay Bắc Cầm rồi mà.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1752 | char=志寰 | src=csv3
JP: 「双鉄先生たちのおっしゃっている仲国は――\nきっと、“日ノ本の皆さんがイメージしている”仲国だ」
TW: 「雙鐵先生他們所說的仲國，肯定是指“日本國的人們印象中的仲國”」
VN(csv3): 「Trung Quốc mà thầy Soutetsu đang nói đến――\nchắc chắn là Trung Quốc "trong trí tưởng tượng của người Hinomoto".」
CUR: 「Trung Quốc mà thầy Soutetsu đang nói đến――\nchắc chắn là Trung Quốc "trong trí tưởng tượng của người Hinomoto".」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1271 | char=姜 | src=csv3
JP: 「健為の景色は、仲国の典型的な地方の光景の一つですね。\n成る程。日ノ本の方の仲国のイメージは、この辺ですか」
TW: 「健為這裡，其實算得上是仲國鄉下典型的樣子了。原來如此，日本國民眾對仲國大致是這樣的印象啊」
VN(csv3): 「Cảnh sắc ở Kiện Vi là một trong những khung cảnh địa phương điển hình của Trung Quốc.\nRa là vậy. Hình ảnh Trung Quốc trong mắt người Hinomoto là như thế này sao.」
CUR: 「Cảnh sắc ở Kiện Vi là một trong những khung cảnh địa phương điển hình của Trung Quốc.\nRa là vậy. Hình ảnh Trung Quốc trong mắt người Hinomoto là như thế này sao.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1380 | char=日々姫 | src=csv3
JP: 「ああ！　そう！　それです！　うん――\nここの景色、“仲国のふるさと”って感じ、する」
TW: 「啊！沒錯！就這意思！嗯——這裡的景色，就是給人“仲國的鄉土”的感覺」
VN(csv3): 「A! Đúng á! Chính là nó! Ưm――\nCảnh sắc ở đây, mang lại cảm giác như "quê hương của Trung Quốc" á.」
CUR: 「A! Đúng á! Chính là nó! Ưm――\nCảnh sắc ở đây, mang lại cảm giác như "quê hương của Trung Quốc" á.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1887 | char=monologue | src=csv3
JP: ハチロクの謝意を微笑で受けて、\n姜さんは、出店のおばさんに仲国語で話しかける。
TW: 以微笑回應了八六的謝意，姜小姐上前與擺攤的大嬸用仲文交談起來。
VN(csv3): Nhận lấy lời cảm ơn của Hachiroku bằng một nụ cười,\ncô Jiang nói chuyện với bà cô bán hàng bằng tiếng Trung.
CUR: Nhận lấy lời cảm ơn của Hachiroku bằng một nụ cười,\ncô Jiang nói chuyện với bà cô bán hàng bằng tiếng Trung.
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1265 | char=双鉄 | src=csv3
JP: 「わからんか、日々姫。この町では――いや、\n仲国という国全体で、会計全てが一瞬で行われるのだ」
TW: 「你還不明白嗎，日日姬。在這小鎮上——不，在整個仲國，付款都可以在眨眼之間完成哦」
VN(csv3): 「Em không hiểu sao, Hibiki. Ở thị trấn này――không,\ntrên toàn đất nước Trung Quốc, mọi việc thanh toán đều diễn ra trong chớp mắt.」
CUR: 「Em không hiểu sao, Hibiki. Ở thị trấn này――không,\ntrên toàn đất nước Trung Quốc, mọi việc thanh toán đều diễn ra trong chớp mắt.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1673 | char=日々姫 | src=audit
JP: 「あの……志寰君？　仲国の鉄道って、\nレイルロオドがスマホいじるの――結構あると？」
TW: 「話說……志寰？在仲國的鐵路線上，鐵路人偶經常會玩手機的嗎？」
VN(csv3): 「Cho chị hỏi……cậu Zhihuan? Ở đường sắt Trung Quốc,\nRailord bấm điện thoại――có thường thấy không á?」
CUR: 「Cho em hỏi……cậu Zhihuan? Ở đường sắt Trung Quốc,\nRailord bấm điện thoại――có thường thấy không á?」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1565 | char=志寰 | src=csv3
JP: 「スマホですか！？　乗務中にはありえません。\n仲国国鉄であれば規則違反。一発で乗務停止です」
TW: 「智慧型手機！？在執行乘務任務中絕無可能。在仲國國鐵的話是嚴重違規，一旦發現直接停職」
VN(csv3): 「Điện thoại sao!? Trong lúc làm nhiệm vụ thì không thể nào.\nNếu là Đường sắt Quốc gia Trung Quốc thì đó là vi phạm nội quy. Sẽ bị đình chỉ công tác ngay lập tức.」
CUR: 「Điện thoại sao!? Trong lúc làm nhiệm vụ thì không thể nào.\nNếu là Đường sắt Quốc gia Trung Quốc thì đó là vi phạm nội quy. Sẽ bị đình chỉ công tác ngay lập tức.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1390 | char=日々姫 | src=csv3
JP: 「あー、[ダイン,3]dineの仲国版って感じ？\nそかそか、これなら」
TW: 「啊，感覺是仲國版的ＤＩＮＥ啊？原來如此，那就懂了」
VN(csv3): 「A, kiểu như phiên bản Trung Quốc của DINE á?\nRa vậy ra vậy, nếu là cái này thì.」
CUR: 「A, kiểu như phiên bản Trung Quốc của DINE á?\nRa vậy ra vậy, nếu là cái này thì.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1423 | char=西瓜 | src=csv3
JP: 「仲国国鉄でもあまりない事例かと思います。\n西瓜も、かなりびっくりしました」
TW: 「在仲國國鐵應該也很少會遇到吧。西瓜也著實嚇了一跳」
VN(csv3): 「Em nghĩ ở Đường sắt Quốc gia Trung Quốc cũng hiếm có trường hợp này.\nSuika cũng khá ngạc nhiên ạ.」
CUR: 「Em nghĩ ở Đường sắt Quốc gia Trung Quốc cũng hiếm có trường hợp này.\nSuika cũng khá ngạc nhiên ạ.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1997 | char=monologue | src=csv3
JP: ガイドさんの仲国語も、かなり楽しげな口調に聞こえる。\n一体何を話しているのか――
TW: 嚮導所說的仲文，語氣也頗為歡快。她們究竟是在……
VN(csv3): Tiếng Trung của cô hướng dẫn viên nghe cũng khá vui vẻ.\nRốt cuộc họ đang nói chuyện gì――
CUR: Tiếng Trung của cô hướng dẫn viên nghe cũng khá vui vẻ.\nRốt cuộc họ đang nói chuyện gì――
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1502 | char=ハチロク | src=csv3
JP: 「見た目の印象ほどには変わらないのかもしれませんね。\n日ノ本と仲国と、ふたつの国の鉄道は」
TW: 「或許，日本國與仲國，兩國鐵路的差別並沒有看起來那麼大」
VN(csv3): 「Có lẽ không khác biệt nhiều như ấn tượng ban đầu nhỉ.\nĐường sắt của hai nước, Hinomoto và Trung Quốc.」
CUR: 「Có lẽ không khác biệt nhiều như ấn tượng ban đầu nhỉ.\nĐường sắt của hai nước, Hinomoto và Trung Quốc.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=889 | char=monologue | src=csv3
JP: ……ポーレットが“仲国鉄も齧っている”と\n言っていた意味が、今なら少しわかる気がする。
TW: ……波萊特所說的“我對仲國鐵路也只是略知一二”，如今我也多少理解了一些其中的含義。
VN(csv3): ……Tôi cảm thấy giờ mình đã hiểu phần nào ý nghĩa câu nói\n"tôi cũng có tìm hiểu về Đường sắt Trung Quốc" của Paulette.
CUR: ……Tôi cảm thấy giờ mình đã hiểu phần nào ý nghĩa câu nói\n"tôi cũng có tìm hiểu về Đường sắt Trung Quốc" của Paulette.
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1361 | char=日々姫 | src=csv3
JP: 「あー、あるのかも！　仲国全土を探したら、\n中国の鉄道風景の、いろんなとこにちょっとずつ！」
TW: 「啊——有可能！走遍全仲國，就能漸漸發現各種不同的仲國鐵路風景！」
VN(csv3): 「A, có khi là vậy á! Nếu tìm kiếm khắp Trung Quốc,\nthì sẽ thấy phong cảnh đường sắt của Trung Quốc, mỗi nơi một chút!」
CUR: 「A, có khi là vậy á! Nếu tìm kiếm khắp Trung Quốc,\nthì sẽ thấy phong cảnh đường sắt của Trung Quốc, mỗi nơi một chút!」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1721 | char=西瓜 | src=csv3
JP: 「その逆もまた真実です。\n日ノ本には、仲国の鉄道に無いものがたくさんあります」
TW: 「這話反過來說也是完全正確的——日本國也有許多仲國鐵路所沒有的東西」
VN(csv3): 「Điều ngược lại cũng là sự thật.\nỞ Hinomoto, có rất nhiều thứ mà đường sắt Trung Quốc không có.」
CUR: 「Điều ngược lại cũng là sự thật.\nỞ Hinomoto, có rất nhiều thứ mà đường sắt Trung Quốc không có.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1900 | char=monologue | src=csv3
JP: 仲国の鉄道にしかない強み。\n日ノ本の鉄道にしかない強み。
TW: 仲國鐵路所獨有的優勢。日本國鐵路所獨有的優勢。
VN(csv3): Điểm mạnh chỉ có ở đường sắt Trung Quốc.\nĐiểm mạnh chỉ có ở đường sắt Hinomoto.
CUR: Điểm mạnh chỉ có ở đường sắt Trung Quốc.\nĐiểm mạnh chỉ có ở đường sắt Hinomoto.
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1255 | char=双鉄 | src=audit
JP: 「だが、仲国では歴史と今は連続している。\n歴史が歴史の重みによって、現在を縛るものではない」
TW: 「但仲國的歷史與現在是相通的。歷史固然有其積澱，但並不會成為對現在的束縛」
VN(csv3): 「Nhưng ở Trọng Quốc, lịch sử và hiện tại là một chuỗi liên tục.\nLịch sử không dùng sức nặng của nó để trói buộc hiện tại.」
CUR: 「Nhưng ở Trung Quốc, lịch sử và hiện tại là một chuỗi liên tục.\nLịch sử không dùng sức nặng của nó để trói buộc hiện tại.」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=2144 | char=monologue | src=audit
JP: 北琴も健為も、歴史館とレールが語る仲国の鉄道も同様だ。\n“今”という時間を、過去の積み重ねの例外としない――
TW: 無論是北琴還是健為，博物館或是線路上的鐵軌，它們描繪出的仲國鐵路的“現在”，無一例外都由過去一步步積累而來。
VN(csv3): Bắc Cầm hay Kiện Vi, cũng như tuyến đường sắt Trọng Quốc mà bảo tàng lịch sử và đường ray kể lại, đều giống nhau.\nKhông coi thời gian "hiện tại" là ngoại lệ của sự tích lũy từ quá khứ——
CUR: Bắc Cầm hay Kiện Vi, cũng như tuyến đường sắt Trung Quốc mà bảo tàng lịch sử và đường ray kể lại, đều giống nhau.\nKhông coi thời gian "hiện tại" là ngoại lệ của sự tích lũy từ quá khứ——
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1523 | char=ハチロク | src=audit
JP: 「でしたら――でしたら双鉄さま。\n仲国版ナインスタアズは」
TW: 「既然這樣——既然這樣，雙鐵少爺，仲國版的九星——」
VN(csv3): 「Nếu vậy——nếu vậy thưa ngài Soutetsu.\nNine Stars phiên bản Trọng Quốc sẽ là」
CUR: 「Nếu vậy——nếu vậy thưa ngài Soutetsu.\nNine Stars phiên bản Trung Quốc sẽ là」
--- 10_Chikuni | 仲国07_芭岩鉄道.txt.toml | key=1743 | char=双鉄 | src=audit
JP: 「仲国版ナインスターズに関する提言の――\n僕らが見出した方向性の、可否を検討してほしいのだ」
TW: 「關於仲國版九星的提案——我們初步找出了方向，希望可以和大家探討一下其可行性」
VN(csv3): 「Về đề xuất liên quan đến Nine Stars phiên bản Trọng Quốc——\nTôi muốn thảo luận xem hướng đi mà chúng ta tìm ra có khả thi hay không.」
CUR: 「Về đề xuất liên quan đến Nine Stars phiên bản Trung Quốc——\nTôi muốn thảo luận xem hướng đi mà chúng ta tìm ra có khả thi hay không.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2422 | char=monologue | src=csv3
JP: 仲国で僕らが学んだことと、みなの意見と、アイディアと。\nそれらをまとめあげるのに、今までかかってしまったが。
TW: 在仲國的所見所聞所想，以及大家的意見和建議。我們將這一切進行整理匯總，一直忙到了現在。
VN(csv3): Những gì chúng tôi học được ở Trọng Quốc, cùng với ý kiến và ý tưởng của mọi người.\nViệc tổng hợp lại tất cả những thứ đó đã tiêu tốn thời gian đến tận bây giờ.
CUR: Những gì chúng tôi học được ở Trọng Quốc, cùng với ý kiến và ý tưởng của mọi người.\nViệc tổng hợp lại tất cả những thứ đó đã tiêu tốn thời gian đến tận bây giờ.
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1858 | char=双鉄 | src=csv3
JP: 「ああ。確かにだ。共感を使い、仲国のレイルロオドと\n――ハチロクはよく、交流し情報を集めてくれた」
TW: 「是啊，八六通過共鳴，從仲國的鐵路人偶那裡收集了相當多的訊息」
VN(csv3): 「Ừ. Đúng vậy. Bằng cách sử dụng cộng cảm, Hachiroku đã giao lưu\nvà thu thập thông tin rất tốt từ các Railord của Trọng Quốc.」
CUR: 「Ừ. Đúng vậy. Bằng cách sử dụng cộng cảm, Hachiroku đã giao lưu\nvà thu thập thông tin rất tốt từ các Railord của Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1086 | char=姜 | src=csv3
JP: 「――日ノ本のナインスターズの“その先”を、\n仲国では進める必要がありますか」
TW: 「——你們在日本國為九星所描繪的“將來”，在仲國也同樣有推行的必要啊」
VN(csv3): 「——"Tương lai" của Nine Stars ở Hinomoto,\ncó cần thiết phải thúc đẩy ở Trọng Quốc không?」
CUR: 「——"Tương lai" của Nine Stars ở Hinomoto,\ncó cần thiết phải thúc đẩy ở Trọng Quốc không?」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2050 | char=双鉄 | src=csv3
JP: 「今回の視察で僕がまずまっさきに感じたのは、\n『仲国の鉄道は生きている』ということでした」
TW: 「這次考察中，我首先認識到的是，“仲國的鐵路仍有勃勃生機”」
VN(csv3): 「Điều đầu tiên tôi cảm nhận được trong chuyến thị sát lần này,\nđó là "đường sắt của Trọng Quốc vẫn đang sống".」
CUR: 「Điều đầu tiên tôi cảm nhận được trong chuyến thị sát lần này,\nđó là "đường sắt của Trọng Quốc vẫn đang sống".」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2423 | char=monologue | src=csv3
JP: 北琴鉄道博物館で目にした仲国国鉄路線図では、\n紅港にも、鉄路は当然、繋がっているにもかかわらず。
TW: 在北琴的鐵路博物館曾看到過仲國國鐵的路線圖，在那上面，箱港自然也有與之相通的線路，但她卻一次都未曾得見。
VN(csv3): Dù trên bản đồ tuyến đường sắt quốc gia Trọng Quốc mà tôi thấy ở Bảo tàng Đường sắt Bắc Cầm,\nđường sắt hiển nhiên cũng kết nối với Hồng Cảng.
CUR: Dù trên bản đồ tuyến đường sắt quốc gia Trọng Quốc mà tôi thấy ở Bảo tàng Đường sắt Bắc Cầm,\nđường sắt hiển nhiên cũng kết nối với Hồng Cảng.
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1908 | char=双鉄 | src=csv3
JP: 「しかし――実際に来て、乗ってみて。\n仲国の広大さが、周遊観光を困難にすると理解しました」
TW: 「然而真正踏上這土地，乘坐列車穿行其中，我才深刻理解了仲國的土地遼闊，導致周遊觀光難度極大」
VN(csv3): 「Nhưng——khi thực sự đến đây và đi thử.\nTôi mới hiểu ra rằng sự rộng lớn của Trọng Quốc sẽ gây khó khăn cho việc du lịch vòng quanh.」
CUR: 「Nhưng——khi thực sự đến đây và đi thử.\nTôi mới hiểu ra rằng sự rộng lớn của Trọng Quốc sẽ gây khó khăn cho việc du lịch vòng quanh.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2508 | char=monologue | src=csv3
JP: 仲国を繋ぎ、仲国と日ノ本をもまた繋ぐ――\nそうした列車の草案を、全力で提言するのみだ。
TW: 將仲國各地聯繫起來，將仲國與日本國聯繫起來——我們要做的就是全力完成這種列車的提案。
VN(csv3): Kết nối Trọng Quốc, và cũng kết nối Trọng Quốc với Hinomoto——\nChúng tôi chỉ cần dốc toàn lực đề xuất một bản thảo cho chuyến tàu như vậy.
CUR: Kết nối Trọng Quốc, và cũng kết nối Trọng Quốc với Hinomoto——\nChúng tôi chỉ cần dốc toàn lực đề xuất một bản thảo cho chuyến tàu như vậy.
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1428 | char=双鉄 | src=csv3
JP: 「9,597,000[　　　　　２,1]km割ることの、36,750[　　　　　　２,1]km。\n単純な面積比ですと、仲国は九洲の260倍強となります」
TW: 「一邊是九百五十九萬七千平方公里的仲國，一邊是三萬六千七百五十平方公里的九州，單就面積便相差兩百六十倍」
VN(csv3): 「9.597.000 km vuông chia cho 36.750 km vuông.\nTính theo tỷ lệ diện tích đơn thuần, Trọng Quốc lớn hơn Kyushu khoảng 260 lần.」
CUR: 「9.597.000 km vuông chia cho 36.750 km vuông.\nTính theo tỷ lệ diện tích đơn thuần, Trọng Quốc lớn hơn Kyushu khoảng 260 lần.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1674 | char=双鉄 | src=csv3
JP: 「ゆえ、九洲規模の範囲を切り取って旅しても、\n『仲国のごく一部』を周遊することにしかなりません」
TW: 「因而，若是旅行範圍限定在九州規模，這樣的周遊線路，不過是“對仲國管中窺豹”而已」
VN(csv3): 「Vì vậy, dù có khoanh vùng một khu vực có quy mô bằng Kyushu để đi du lịch,\nthì cũng chỉ là du lịch vòng quanh "một phần rất nhỏ của Trọng Quốc" mà thôi.」
CUR: 「Vì vậy, dù có khoanh vùng một khu vực có quy mô bằng Kyushu để đi du lịch,\nthì cũng chỉ là du lịch vòng quanh "một phần rất nhỏ của Trọng Quốc" mà thôi.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2071 | char=日々姫 | src=csv3
JP: 「それでは仲国を代表する観光列車にはなりえませんし\n仲国の皆さんのこころを繋ぐレールは、伸ばせません」
TW: 「那樣是無法成為代表仲國的觀光列車的，而聯繫起全仲國人民內心的鐵軌，也會無從鋪就」
VN(csv3): 「Như vậy thì không thể trở thành chuyến tàu du lịch đại diện cho Trọng Quốc được,\nvà cũng không thể kéo dài tuyến đường ray kết nối trái tim của người dân Trọng Quốc.」
CUR: 「Như vậy thì không thể trở thành chuyến tàu du lịch đại diện cho Trọng Quốc được,\nvà cũng không thể kéo dài tuyến đường ray kết nối trái tim của người dân Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1784 | char=ハチロク | src=csv3
JP: 「わたくしたちは、仲国の広さをまず学び、\n整頓しようと試みました」
TW: 「我們首先去了解仲國的廣闊，嘗試從中整理思路」
VN(csv3): 「Đầu tiên, chúng tôi tìm hiểu về sự rộng lớn của Trọng Quốc,\nvà cố gắng sắp xếp lại.」
CUR: 「Đầu tiên, chúng tôi tìm hiểu về sự rộng lớn của Trọng Quốc,\nvà cố gắng sắp xếp lại.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1474 | char=西瓜 | src=csv3
JP: 「仲国の平均的な大型連休は、7日が二回。\n春節、つまり旧正月と、国慶節となります。ので――」
TW: 「仲國大多數人每年擁有兩次七天長假，春節，即舊曆正月，以及國慶節，因此——」
VN(csv3): 「Kỳ nghỉ dài ngày trung bình ở Trọng Quốc gồm hai đợt 7 ngày.\nĐó là Lễ hội mùa xuân, tức là Tết Nguyên đán, và Quốc khánh. Vì vậy——」
CUR: 「Kỳ nghỉ dài ngày trung bình ở Trọng Quốc gồm hai đợt 7 ngày.\nĐó là Lễ hội mùa xuân, tức là Tết Nguyên đán, và Quốc khánh. Vì vậy——」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1864 | char=双鉄 | src=csv3
JP: 「ああ。ゆえ、その案は捨て。全く異なる区分を求めた。\nすると『仲国地理大区』というのものがあると教わった」
TW: 「是的。所以我們也放棄了這個方案，轉而尋求其他的劃分方法。這時我們了解到了“仲國地理大區”的概念」
VN(csv3): 「Đúng vậy. Do đó, chúng tôi đã từ bỏ phương án đó. Và tìm kiếm một cách phân chia hoàn toàn khác.\nThế là chúng tôi được biết đến khái niệm "Đại khu địa lý Trọng Quốc".」
CUR: 「Đúng vậy. Do đó, chúng tôi đã từ bỏ phương án đó. Và tìm kiếm một cách phân chia hoàn toàn khác.\nThế là chúng tôi được biết đến khái niệm "Đại khu địa lý Trọng Quốc".」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2428 | char=monologue | src=csv3
JP: 仲国を簡易的に描いた地図に、日々姫がさっと線を引く。
TW: 在簡單畫出的示意地圖上，日日姬橫拉了一條線。
VN(csv3): Trên bản đồ vẽ đơn giản Trọng Quốc, Hibiki nhanh chóng vạch một đường.
CUR: Trên bản đồ vẽ đơn giản Trọng Quốc, Hibiki nhanh chóng vạch một đường.
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2741 | char=monologue | src=csv3
JP: 西北・華北・東北と、西南・中南・華東とに――\n仲国全土が、南北二つに切り分けられる。
TW: 西北、華北和東北，西南、中南和華東——將仲國全境，以南北為界劃為兩大區域。
VN(csv3): Tây Bắc, Hoa Bắc, Đông Bắc và Tây Nam, Trung Nam, Hoa Đông——\nToàn bộ Trọng Quốc được chia làm hai nửa Nam Bắc.
CUR: Tây Bắc, Hoa Bắc, Đông Bắc và Tây Nam, Trung Nam, Hoa Đông——\nToàn bộ Trọng Quốc được chia làm hai nửa Nam Bắc.
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1919 | char=双鉄 | src=csv3
JP: 「数多瞬く星々だ。6つの仲国地理大区――\nそれぞれに、すくなくとも十以上の星を散りばめたい」
TW: 「當然是滿天繁星。在六個仲國地理大區，各自散布下至少十顆以上的星星」
VN(csv3): 「Là vô số những vì sao lấp lánh. 6 đại khu địa lý Trọng Quốc——\nTôi muốn rải ít nhất mười vì sao trở lên vào mỗi khu vực.」
CUR: 「Là vô số những vì sao lấp lánh. 6 đại khu địa lý Trọng Quốc——\nTôi muốn rải ít nhất mười vì sao trở lên vào mỗi khu vực.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1920 | char=西瓜 | src=csv3
JP: 「仲国を……発見する――\n仲国の魅力を、再確認する？」
TW: 「發現……仲國——再一次，體會仲國的魅力？」
VN(csv3): 「Khám phá…… Trọng Quốc——\nKhẳng định lại sức hấp dẫn của Trọng Quốc?」
CUR: 「Khám phá…… Trọng Quốc——\nKhẳng định lại sức hấp dẫn của Trọng Quốc?」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1693 | char=双鉄 | src=csv3
JP: 「仲国の魅力を確かめ直す旅を通じて、仲国鉄路の魅力を。\nひいては――仲国を旅する自分自身をも、再発見する」
TW: 「在重新體會仲國魅力的同時，也再次領略仲國鐵路，乃至仲國旅遊自身的魅力」
VN(csv3): 「Thông qua chuyến hành trình khẳng định lại sức hấp dẫn của Trọng Quốc, để cảm nhận sức hấp dẫn của đường sắt Trọng Quốc.\nXa hơn nữa là——tái khám phá chính bản thân mình khi đi du lịch Trọng Quốc.」
CUR: 「Thông qua chuyến hành trình khẳng định lại sức hấp dẫn của Trọng Quốc, để cảm nhận sức hấp dẫn của đường sắt Trọng Quốc.\nXa hơn nữa là——tái khám phá chính bản thân mình khi đi du lịch Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1476 | char=志寰 | src=csv3
JP: 「しかし、今の仲国の若者にだと――\nキャンペーンに興味をもってもらうことが難しそうです」
TW: 「但如今，想要通過活動吸引仲國年輕人的興趣恐怕並不容易」
VN(csv3): 「Nhưng, với giới trẻ Trọng Quốc hiện nay thì——\ncó vẻ khó để khiến họ hứng thú với chiến dịch này.」
CUR: 「Nhưng, với giới trẻ Trọng Quốc hiện nay thì——\ncó vẻ khó để khiến họ hứng thú với chiến dịch này.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2051 | char=西瓜 | src=csv3
JP: 「フリーきっぷ……春節中は仲国国鉄乗り放題、的な？\nそれは――そのきっぷも高価となりそうかと、西瓜は」
TW: 「通票……比如在春節期間可以自由乘坐仲國國鐵列車嗎？西瓜覺得這通票怕是價格不菲」
VN(csv3): 「Vé trọn gói…… kiểu như đi tàu quốc gia Trọng Quốc thoải mái trong dịp Lễ hội mùa xuân sao?\nCái đó——Suika nghĩ vé đó có vẻ cũng sẽ rất đắt.」
CUR: 「Vé trọn gói…… kiểu như đi tàu quốc gia Trọng Quốc thoải mái trong dịp Lễ hội mùa xuân sao?\nCái đó——Suika nghĩ vé đó có vẻ cũng sẽ rất đắt.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1149 | char=双鉄 | src=csv3
JP: 「……この芭岩鉄道の、昔のきっぷを模したメモ帳や、\n仲国国鉄マークのピンバッチなどが良い参考になるかと」
TW: 「……芭岩鐵路這個仿造復古車票樣式的筆記本，還有這個仲國國鐵標誌的胸章，感覺都是不錯的樣本」
VN(csv3): 「……Cuốn sổ tay mô phỏng vé tàu ngày xưa của Đường sắt Bayan này,\nvà huy hiệu cài áo hình logo đường sắt quốc gia Trọng Quốc có lẽ sẽ là tài liệu tham khảo tốt.」
CUR: 「……Cuốn sổ tay mô phỏng vé tàu ngày xưa của Đường sắt Bayan này,\nvà huy hiệu cài áo hình logo đường sắt quốc gia Trọng Quốc có lẽ sẽ là tài liệu tham khảo tốt.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2042 | char=双鉄 | src=audit
JP: 「それが、現時点での仲国国鉄の鉄路復権のために考えた、\n僕たち、御一夜鉄道による提案の草稿となります」
TW: 「這就是現階段我們御一夜鐵路，就仲國國鐵復興所提出的方案草案」
VN(csv3): 「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohimitera,\nnhằm phục hưng đường sắt quốc gia Trọng Quốc ở thời điểm hiện tại.」
CUR: 「Đó là bản thảo đề xuất của chúng tôi, Đường sắt Ohitoyo,\nnhằm phục hưng đường sắt quốc gia Trọng Quốc ở thời điểm hiện tại.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1898 | char=姜 | src=csv3
JP: 「『将来的な仲国国鉄の復権』にむけ――他にもご提言を\nいただけそうかと、図々しくも感じてしまいますが」
TW: 「為了“將來仲國國鐵的復興”——恕我冒昧相問，諸位想必也另有方案吧」
VN(csv3): 「Hướng tới "sự phục hưng của đường sắt quốc gia Trọng Quốc trong tương lai"——tôi có chút trơ trẽn\nkhi cảm thấy rằng, dường như các vị còn có đề xuất nào khác nữa.」
CUR: 「Hướng tới "sự phục hưng của đường sắt quốc gia Trọng Quốc trong tương lai"——tôi có chút trơ trẽn\nkhi cảm thấy rằng, dường như các vị còn có đề xuất nào khác nữa.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1781 | char=双鉄 | src=csv3
JP: 「僕らであれば将来的に。6つの地理大区全ての拠点駅\n――仲国全土を6日間で周遊する列車をご提案できます」
TW: 「我們想要提出的，是將來最終實現在六天裡周遊六個地理大區全部據點車站的列車方案」
VN(csv3): 「Nếu là chúng tôi thì trong tương lai. Có thể đề xuất một chuyến tàu đi vòng quanh nhà ga cứ điểm của cả 6 đại khu địa lý\n——toàn bộ Trọng Quốc trong 6 ngày.」
CUR: 「Nếu là chúng tôi thì trong tương lai. Có thể đề xuất một chuyến tàu đi vòng quanh nhà ga cứ điểm của cả 6 đại khu địa lý\n——toàn bộ Trọng Quốc trong 6 ngày.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1782 | char=双鉄 | src=audit
JP: 「我々には\x%l電車;#00ffc040;電車%l;#;特急\x%lクハ26;#00ffc040;クハ26%l;#;があり。仲国国鉄には東富4Dと\n標準軌、1435mm軌での列車運用の豊富な蓄積があります」
TW: 「我們有特快\x%l電車;#00ffc040;電車%l;#;的\x%lクハ26;#00ffc040;Ｋｕｈａ２６%l;#;，仲國國鐵有應用東富４Ｄ，以及標準軌１４３５毫米軌距列車的豐富經驗」
VN(csv3): 「Chúng tôi có Kuha 26 tốc hành tàu điện. Còn đường sắt quốc gia Trọng Quốc có Dongfeng 4D\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」
CUR: 「Chúng tôi có \x%lクハ26;#00ffc040;Kuha 26%l;#; tốc hành \x%l電車;#00ffc040;tàu điện%l;#;. Còn đường sắt quốc gia Trọng Quốc có Dongfeng 4D\nvà sự tích lũy phong phú trong việc vận hành tàu trên khổ tiêu chuẩn 1435mm.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2012 | char=志寰 | src=csv3
JP: 「標準軌完全電化による超高速鉄道を、\n仲国に走らせるよう――おっしゃっているのですか？」
TW: 「讓全線電力化的超高速鐵路列車，在仲國的標準軌上馳騁嗎？」
VN(csv3): 「Thầy đang nói——sẽ cho chạy đường sắt siêu tốc\nbằng cách điện khí hóa hoàn toàn khổ tiêu chuẩn ở Trọng Quốc sao?」
CUR: 「Thầy đang nói——sẽ cho chạy đường sắt siêu tốc\nbằng cách điện khí hóa hoàn toàn khổ tiêu chuẩn ở Trọng Quốc sao?」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1686 | char=日々姫 | src=csv3
JP: 「日ノ本では新・幹線――標準軌の専用線を敷かねば\nいけんばってん、仲国は最初から標準軌やけん」
TW: 「在日本國，新·幹線必須要鋪設專用的標準軌，但仲國打一開始就是標準軌了」
VN(csv3): 「Ở Hinomoto, Tân Cán Tuyến——phải trải đường ray chuyên dụng khổ tiêu chuẩn,\nnhưng Trọng Quốc thì ngay từ đầu đã là khổ tiêu chuẩn rồi.」
CUR: 「Ở Hinomoto, Tân Cán Tuyến——phải trải đường ray chuyên dụng khổ tiêu chuẩn,\nnhưng Trọng Quốc thì ngay từ đầu đã là khổ tiêu chuẩn rồi.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1473 | char=西瓜 | src=csv3
JP: 「仲国国鉄が――老師や、志寰や、西瓜たち――\nみんなが生み出し、守って育てた、西瓜たちの機関車が」
TW: 「仲國國鐵——老師和志寰，還有西瓜以及無數同志們——由大家創造、守護、培養起來的這型機車——」
VN(csv3): 「Đường sắt quốc gia Trọng Quốc——Lão sư, Zhihuan, và nhóm Suika——\nĐầu máy của nhóm Suika, được mọi người tạo ra, bảo vệ và nuôi dưỡng.」
CUR: 「Đường sắt quốc gia Trọng Quốc——Lão sư, Zhihuan, và nhóm Suika——\nĐầu máy của nhóm Suika, được mọi người tạo ra, bảo vệ và nuôi dưỡng.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2089 | char=姜 | src=csv3
JP: 「双鉄先生の伸ばすレールは、歌い、物語るレールです。\n私は仲国の鉄路の上にも、それを紡いで欲しかった」
TW: 「雙鐵先生所鋪下的鐵軌，織就歌謠，化作傳奇。我也想在仲國的鐵路上，織就同樣的輝煌」
VN(csv3): 「Đường ray mà thầy Soutetsu vươn dài, là đường ray biết hát, biết kể chuyện.\nTôi cũng muốn dệt nên điều đó trên tuyến đường sắt của Trọng Quốc.」
CUR: 「Đường ray mà thầy Soutetsu vươn dài, là đường ray biết hát, biết kể chuyện.\nTôi cũng muốn dệt nên điều đó trên tuyến đường sắt của Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1904 | char=姜 | src=csv3
JP: 「物語に気づいてもらい、読んでもらうための絵を。\nですので日々姫先生に、仲国でも描いていただきたい」
TW: 「為讓人能留意到這故事，能夠潛心閱讀，希望日日姬女士能夠揮筆繪下仲國的光明未來」
VN(csv3): 「Bức tranh để mọi người chú ý đến câu chuyện, và đọc nó.\nVì vậy, tôi muốn cô Hibiki vẽ ở Trọng Quốc nữa.」
CUR: 「Bức tranh để mọi người chú ý đến câu chuyện, và đọc nó.\nVì vậy, tôi muốn cô Hibiki vẽ ở Trọng Quốc nữa.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1484 | char=双鉄 | src=audit
JP: 「御一夜鉄道だけでは足りない。日ノ本仲国、二つの国の、\nより多くの知恵と技術の集積が必須となるでしょう」
TW: 「僅憑御一夜鐵路必然是不夠的，這需要將日本國與仲國兩個國家的眾多智慧與技術匯聚於一處才能實現」
VN(csv3): 「Chỉ Đường sắt Ohimitera thôi thì không đủ. Sẽ cần phải tập hợp\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trọng Quốc.」
CUR: 「Chỉ Đường sắt Ohitoyo thôi thì không đủ. Sẽ cần phải tập hợp\nnhiều trí tuệ và công nghệ hơn nữa từ hai nước Hinomoto và Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1800 | char=姜 | src=csv3
JP: 「絵と物語を、現実の物と為す。日ノ本では雛衣、稀咲\n真闇女士たちが果たしたことを、仲国では、きっと私が」
TW: 「我要將畫作與傳奇化為現實。在日本國經雛衣、稀咲以及真闇女士等實現的，我也一定會在仲國再現」
VN(csv3): 「Biến bức tranh và câu chuyện thành hiện thực. Những gì Hinai, Kisaki\nvà cô Mayami đã hoàn thành ở Hinomoto, tôi chắc chắn sẽ làm được ở Trọng Quốc.」
CUR: 「Biến bức tranh và câu chuyện thành hiện thực. Những gì Hinai, Kisaki\nvà cô Mayami đã hoàn thành ở Hinomoto, tôi chắc chắn sẽ làm được ở Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2046 | char=西瓜 | src=csv3
JP: 「環状線ですね。とても小さな。\nけれど、日ノ本と仲国を繋ぐ、環状線」
TW: 「這是環線呀，一個小小的環線。但這環線，聯繫起了日本國與仲國」
VN(csv3): 「Là một tuyến đường vòng tròn nhỉ. Rất nhỏ.\nNhưng, là tuyến đường vòng tròn kết nối Hinomoto và Trọng Quốc.」
CUR: 「Là một tuyến đường vòng tròn nhỉ. Rất nhỏ.\nNhưng, là tuyến đường vòng tròn kết nối Hinomoto và Trọng Quốc.」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=1965 | char=姜 | src=csv3
JP: 「必ず実らせ、茂らせましょう。その根で、枝葉で、\n仲国と日ノ本とを、それぞれの全土を巡らせましょう」
TW: 「茁壯成長，其根系枝葉，必將遍布仲日兩國」
VN(csv3): 「Nhất định sẽ đơm hoa kết trái, xum xuê cành lá. Bằng bộ rễ đó, bằng cành lá đó,\nhãy để chúng lan tỏa khắp toàn bộ lãnh thổ của Trọng Quốc và Hinomoto.」
CUR: 「Nhất định sẽ đơm hoa kết trái, xum xuê cành lá. Bằng bộ rễ đó, bằng cành lá đó,\nhãy để chúng lan tỏa khắp toàn bộ lãnh thổ của Trọng Quốc và Hinomoto.」


### Phụ lục T57 — 詠国 (16 dòng) + 2 dòng katakana liên quan

--- 01_Hachiroku | ハチロク02_8620運転台通信.txt.toml | key=2254 | char=双鉄 | src=csv3
JP: 「それを言うなら[えいこく,1]詠国もだろう。\nあの国の女王こそは、淑女の[かがみ]鑑として知られている」
TW: 「非要這麼說的話英國也是吧。英國的女王還被稱為“淑女典範”呢」
VN(csv3): 「Nói thế thì nước Anh cũng vậy.\nNữ vương của đất nước đó được biết đến như một tấm gương thục nữ mà.」
CUR: 「Nói thế thì nước Anh cũng vậy.\nNữ vương của đất nước đó được biết đến như một tấm gương thục nữ mà.」
--- 01_Hachiroku | ハチロク02_8620運転台通信.txt.toml | key=2766 | char=monologue | src=audit
JP: 冥国なり詠国なりの、しかも老婆が、\n賞賛の意で、よもやチョップをくれるなど――
TW: 美國或者是英國出身的遊客，況且還是老婆婆，居然以贈送小肥肉為表達讚賞的方式――
VN(csv3): Một bà cụ người Mỹ hay người Anh,\nlại đi tặng "cú chặt" để tỏ ý khen ngợi sao——
CUR: Một bà cụ người Minh Quốc hay người Anh,\nlại đi tặng "cú chặt" để tỏ ý khen ngợi sao——
--- 01_Hachiroku | ハチロク03_冥国式レイルロオド.txt.toml | key=1580 | char=ハチロク | src=audit
JP: 「……冥国式\x%lレイルロオド;#00ffc040;レイルロオド%l;#;は、日ノ本や[えいこく,1]詠国、[どっこく,1]髑国式の\n\x%lレイルロオド;#00ffc040;レイルロオド%l;#;と大きく異なり、交代乗務を常とします」
TW: 「……美國式\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;與日本、英國、德國式有著顯著的不同，交替執行乘務任務可以說是家常便飯」
VN(csv3): 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Mỹ khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
CUR: 「……\x%lレイルロオド;#00ffc040;Railord%l;#; kiểu Minh Quốc khác biệt rất lớn so với \x%lレイルロオド;#00ffc040;Railord%l;#;\nkiểu Hinamoto, kiểu Anh hay kiểu Đức, họ thường xuyên thay ca làm nhiệm vụ ạ.」
--- 01_Hachiroku | ハチロク03_冥国式レイルロオド.txt.toml | key=2437 | char=ポーレット | src=audit
JP: 「はい。国は[えいこく,1]詠国式をお手本にしましたし、大手私鉄も\n[どっこく,1]髑国や詠国が主流。[めいこく,1]冥国式は、そもそも少数派でした」
TW: 「是的。國家層面上是借鑑的英國，大型的私營鐵路也是以德國和英國為主流。美國式從一開始就是少數派」
VN(csv3): 「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Mỹ vốn dĩ đã là thiểu số rồi.」
CUR: 「Vâng. Quốc gia đã lấy kiểu Anh làm hình mẫu, các tuyến đường sắt tư nhân lớn\ncũng chủ yếu dùng kiểu Đức và Anh. Kiểu Minh Quốc vốn dĩ đã là thiểu số rồi.」
--- 01_Hachiroku | ハチロク04_煙には煙を.txt.toml | key=1533 | char=ハチロク | src=csv3
JP: 「[ロクセンニヒャクケイ,4]6200形――\x%l6200;#00ffc040;[ネルソン,3]6200%l;#;お姉さま達は、\nニイルセンという[えいこく,1]詠国の会社からの輸入蒸気なのです」
TW: 「[六千二百,3]６２００型——\x%l6200;#00ffc040;[納爾遜,3]６２００%l;#;姐姐她們是從一家叫尼爾森的英國公司進口的蒸汽機車」
VN(csv3): 「Các chị mẫu 6200――\x%l6200;#00ffc040;6200%l;#;,\nlà đầu máy hơi nước nhập khẩu từ một công ty của Anh tên là Neilson ạ.」
CUR: 「Các chị mẫu 6200――\x%l6200;#00ffc040;6200%l;#;,\nlà đầu máy hơi nước nhập khẩu từ một công ty của Anh tên là Neilson ạ.」
--- 01_Hachiroku | ハチロク09_もくもくオリヴィ.txt.toml | key=1848 | char=双鉄 | src=csv3
JP: 「それもなかなか厳しいようだな。詠国で学んだ者は、\n日ノ本の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;技師にも多いそうだが……」
TW: 「恐怕外國希望也很渺茫。日本的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;技工有很多都是留學英國的……」
VN(csv3): 「Chuyện đó có vẻ cũng khá khó khăn đấy. Những người từng học ở Vịnh Quốc,\ntrong số các kỹ sư \x%lレイルロオド;#00ffc040;Railord%l;#; của Hinomoto cũng có rất nhiều, nhưng mà……」
CUR: 「Chuyện đó có vẻ cũng khá khó khăn đấy. Những người từng học ở Vịnh Quốc,\ntrong số các kỹ sư \x%lレイルロオド;#00ffc040;Railord%l;#; của Hinomoto cũng có rất nhiều, nhưng mà……」
--- 01_Hachiroku | ハチロク10_旺宮鉄道歴史館.txt.toml | key=1529 | char=双鉄 | src=csv3
JP: 「……日ノ本の鉄道営業法は、\n詠国を見本に作られているのですよね？　恐らく」
TW: 「……想必日本的鐵路運營法，也是仿照英國的法規制定的吧？」
VN(csv3): 「……Luật kinh doanh đường sắt của Hinamoto,\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」
CUR: 「……Luật kinh doanh đường sắt của Hinamoto,\ncó lẽ được soạn thảo dựa trên khuôn mẫu của Eikoku (Anh Quốc) phải không?」
--- 05_Mayami | 真闇03_ひとしずく.txt.toml | key=1833 | char=真闇 | src=csv3
JP: 「[えいこく,1]詠国の、プレジデンツファインリカーさんて。\n最低注文は何本からか問い合わせ」
TW: 「是英國的總統酒行。打來諮詢最少能訂購幾瓶的」
VN(csv3): 「Của hãng President Fine Liquor bên Eikoku (Vương quốc Anh).\nHọ hỏi xem đơn hàng tối thiểu là từ bao nhiêu chai.」
CUR: 「Của hãng President Fine Liquor bên Eikoku (Vương quốc Anh).\nHọ hỏi xem đơn hàng tối thiểu là từ bao nhiêu chai.」
--- 05_Mayami | 真闇03_ひとしずく.txt.toml | key=1687 | char=ふかみ | src=csv3
JP: 「だって、これ……すごく偏ってるから。\n[えいこく,1]詠国、フランク、[どっこく,1]髑国、[らんこく,1]乱国、イスパニャ――」
TW: 「因為……分布太不平衡了。英國、法國、德國、荷蘭、西班牙——」
VN(csv3): 「Bởi vì, danh sách này…… thiên vị quá.\nEikoku (Vương quốc Anh), Frank (Pháp), Dokkoku (Đức), Rankoku (Hà Lan), Ispania (Tây Ban Nha)――」
CUR: 「Bởi vì, danh sách này…… thiên vị quá.\nEikoku (Vương quốc Anh), Frank (Pháp), Dokkoku (Đức), Rankoku (Hà Lan), Ispania (Tây Ban Nha)――」
--- 05_Mayami | 真闇03_ひとしずく.txt.toml | key=2533 | char=monologue | src=csv3
JP: 時差が九時間だからええっと……\n詠国は、まだ夜六時ということになる。
TW: 時差是九個小時……英國的話還只是傍晚六點。
VN(csv3): Chênh lệch múi giờ là chín tiếng, vậy thì……\nBên Eikoku (Vương quốc Anh) mới chỉ sáu giờ tối thôi.
CUR: Chênh lệch múi giờ là chín tiếng, vậy thì……\nBên Eikoku (Vương quốc Anh) mới chỉ sáu giờ tối thôi.
--- 05_Mayami | 真闇03_ひとしずく.txt.toml | key=1662 | char=双鉄 | src=csv3
JP: 「うむ。研修をさせて欲しいとの希望が殺到している。\n特に、[えいこく,1]詠国の\x%lレイルロオド;#00ffc040;レイルロオド%l;#;が多いそうだぞ」
TW: 「嗯。希望來這邊培訓的請求也蜂擁而至。尤其是英國的\x%lレイルロオド;#00ffc040;鐵路人偶%l;#;，特別多的樣子」
VN(csv3): 「Ừm. Đơn xin đến thực tập đang đổ về nườm nượp.\nĐặc biệt là có rất nhiều \x%lレイルロオド;#00ffc040;Railord%l;#; đến từ Anh Quốc.」
CUR: 「Ừm. Đơn xin đến thực tập đang đổ về nườm nượp.\nĐặc biệt là có rất nhiều \x%lレイルロオド;#00ffc040;Railord%l;#; đến từ Anh Quốc.」
--- 05_Mayami | 真闇03_ひとしずく.txt.toml | key=1905 | char=真闇 | src=csv3
JP: 「[えいこく,1]詠国の」
TW: 「英國」
VN(csv3): 「Anh Quốc á.」
CUR: 「Anh Quốc á.」
--- 05_Mayami | 真闇h3_補習授業の廃校舎.txt.toml | key=3529 | char=monologue | src=csv3
JP: 計ったように、蔵から声が響いてくる。\nF・スコッティ。詠国産まれのレイルロオドだ。
TW: 正巧此時倉庫傳來了聲音。飛·蘇格闌，是詠國產的鐵路人偶。
VN(csv3): Như đã hẹn trước, từ trong xưởng rượu vang lên một giọng nói.\nF. Scotty. Một Railord sinh ra ở Anh quốc.
CUR: Như đã hẹn trước, từ trong xưởng rượu vang lên một giọng nói.\nF. Scotty. Một Railord sinh ra ở Anh quốc.
--- 07_Nagi_Fukami | 凪ふかみ01_凪の成長、ふかみの成長.txt.toml | key=1587 | char=凪 | src=audit
JP: 「確か、蒸気機関車って、日ノ本よりずうっと前から、\n[えいこく,1]詠国やら[めいこく,1]冥国やら[どっこく,1]髑国にはあったんでしょお？」
TW: 「咱記得英國、美國、德國早就有蒸汽機車了，應該比日本還要早得多吧？」
VN(csv3): 「Em nhớ là, đầu máy hơi nước đã có ở Anh, Mỹ và Đức\ntừ rất lâu trước cả Hinomoto rồi phải không?」
CUR: 「Em nhớ là, đầu máy hơi nước đã có ở Anh, Minh Quốc và Đức\ntừ rất lâu trước cả Hinomoto rồi phải không?」
--- 07_Nagi_Fukami | 凪ふかみ01_凪の成長、ふかみの成長.txt.toml | key=1818 | char=双鉄 | src=csv3
JP: 「ああ。蒸気機関車の発祥は[えいこく,1]詠国とされている。\n[えい]詠・[めい]冥・[どく]髑は競い合うように技術を発展させたと」
TW: 「是啊，蒸汽機車發源於英國。英美德三國則是爭先恐後發展了蒸汽機車的技術」
VN(csv3): 「Ừ. Đầu máy hơi nước được cho là bắt nguồn từ Anh.\nAnh, Mỹ, Đức đã phát triển công nghệ như thể đang cạnh tranh với nhau vậy.」
CUR: 「Ừ. Đầu máy hơi nước được cho là bắt nguồn từ Anh.\nAnh, Mỹ, Đức đã phát triển công nghệ như thể đang cạnh tranh với nhau vậy.」
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=1722 | char=ふかみ | src=audit
JP: 「もっと高く。衛星軌道にまで飛んで？　どう見える？\n[めいこく,1]冥国、[えいこく,1]詠国、[どっこく,1]髑国、フランク、[ちゅうごく,1]仲国、[かんこく,1]汗国とかの線路は」
TW: 「再飛高點，飛上衛星軌道。美國、英國、德國、法國、仲國、韓國的線路，看起來怎麼樣？」
VN(csv3): 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Mỹ, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」
CUR: 「Cao hơn nữa. Bay lên tận quỹ đạo vệ tinh xem? Trông như thế nào?\nĐường ray ở các nước như Minh Quốc, Anh, Đức, Pháp, Trung Quốc, Hàn Quốc thì sao?」

--- 01_Hachiroku | ハチロク09_もくもくオリヴィ.txt.toml | key=2102 | src=csv3
JP: 「じゃ、メーコクとかエーコクに聞きにいくしかない？」
TW: 「那只能去美國或者英國打聽了嗎？」
CUR: 「Vậy thì, chỉ còn cách đi hỏi Minh Quốc (Mỹ) hay Vịnh Quốc (Anh) thôi sao?」
--- 01_Hachiroku | ハチロク10_旺宮鉄道歴史館.txt.toml | key=2024 | src=csv3
JP: 「ううん。[メーコク,1]冥国広いから！\nおんなじ州でも、200キロもはなれてる！」
TW: 「不算近，美國地方很大的！即使在同一個州，也隔了有２００公里遠！」
CUR: 「Không đâu. Minh Quốc (Nước Mỹ) rộng lắm!\nDù ở cùng một bang, nhưng cũng cách nhau đến 200 km lận!」


### Phụ lục T58 — 次元流 (3 dòng)

--- 07_Nagi_Fukami | 凪ふかみ02_凪の大会初挑戦！.txt.toml | key=2280 | char=凪 | src=csv3
JP: 「そうばい！　壱刀流からバイ捨流ば産まれて、\nそのバイ捨流からまた産まれたのが、[じげん,1]次元流ばい！！」
TW: 「是咧！　體舍流源自一刀流，後續還演變出了示現流咧！！」
VN(csv3): 「Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu,\nrồi từ Thể Xá Lưu lại sinh ra Thứ Nguyên Lưu đó!!」
CUR: 「Đúng vậy! Thể Xá Lưu bắt nguồn từ Nhất Đao Lưu,\nrồi từ Thể Xá Lưu lại sinh ra Thứ Nguyên Lưu đó!!」
--- 07_Nagi_Fukami | 凪ふかみ02_凪の大会初挑戦！.txt.toml | key=3109 | char=monologue | src=csv3
JP: 次元流！　知ってる！！\nわたし、薄い本で良く勉強してる！！
TW: 示現流！　這個我知道！！在小本子裡沒少見識！！
VN(csv3): Thứ Nguyên Lưu! Mình biết!!\nMình hay học hỏi từ mấy cuốn doujinshi lắm!!
CUR: Thứ Nguyên Lưu! Mình biết!!\nMình hay học hỏi từ mấy cuốn doujinshi lắm!!
--- 07_Nagi_Fukami | 凪ふかみ02_凪の大会初挑戦！.txt.toml | key=2377 | char=ふかみ | src=csv3
JP: 「一太刀で相手を倒す、っていうのに\nすべてをかける剣術だよね？　[じげん,1]次元流」
TW: 「示現流就是在第一招傾盡全力，一擊斃敵的劍術流派，對吧？」
VN(csv3): 「Đó là môn kiếm thuật đặt cược tất cả\nvào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thứ Nguyên Lưu ấy.」
CUR: 「Đó là môn kiếm thuật đặt cược tất cả\nvào việc hạ gục đối thủ bằng một nhát chém duy nhất phải không? Thứ Nguyên Lưu ấy.」


### Phụ lục T59 — キルクイティウム (6 dòng)

--- 02_Hibiki | 日々姫10_稀咲の未来図、日々姫の未来図.txt.toml | key=2458 | src=csv3
JP: 「ええ。エアロ＝クラフテック機関の心臓部である、\nキルクイティウムの精製には豊富な真水が必要ですから」
TW: 「嗯。要精煉空凝機引擎的心臟“鐶”必須要用到大量淡水」
CUR: 「Vâng. Để tinh chế Circuithium, trái tim của động cơ Aero-Craftech,\nthì cần một lượng lớn nước ngọt.」
--- 03_Paulette | 共通04_キハ07。ポーレットとれいな.txt.toml | key=2520 | src=csv3
JP: 「エアロ＝クラフテック機関の心臓部は、\nキルクイティウムという宝石状の化合物だ」
TW: 「空凝機引擎的核心，是一種叫鐶的寶石狀化合物」
CUR: 「Trái tim của động cơ Aero-Craftech\nlà một hợp chất dạng đá quý có tên là Quirquitium.」
--- 03_Paulette | 共通04_キハ07。ポーレットとれいな.txt.toml | key=2105 | src=csv3
JP: 「しかし、キルクイティウムには弱点がある。\nそれは“共振崩壊”という現象だ」
TW: 「不過，鐶有一個缺點。那就是被稱為“共振崩塌”的現象」
CUR: 「Tuy nhiên, Quirquitium có một điểm yếu.\nĐó là hiện tượng mang tên "Cộng hưởng sụp đổ".」
--- 03_Paulette | 共通04_キハ07。ポーレットとれいな.txt.toml | key=2304 | src=csv3
JP: 「ああ。キルクイティウム同士を近づけ過ぎると、\nその双方の回転が制御不能となり、崩壊にいたる」
TW: 「對。鐶互相之間靠得太近的話會導致雙方的旋轉失控，引發崩塌」
CUR: 「Ừ. Nếu để các Quirquitium lại quá gần nhau,\nchuyển động quay của cả hai sẽ mất kiểm soát, dẫn đến sụp đổ.」
--- 03_Paulette | 共通04_キハ07。ポーレットとれいな.txt.toml | key=2629 | src=csv3
JP: 「でしたら……“キルクイティウムを集中しての運用”は、\n不可能ということになりますね？」
TW: 「那麼……“將鐶集中使用”，是不可能實現的嗎？」
CUR: 「Nếu vậy thì…… "việc tập trung Quirquitium lại để sử dụng",\nlà điều không thể đúng không ạ?」
--- 03_Paulette | 共通04_キハ07。ポーレットとれいな.txt.toml | key=2240 | src=csv3
JP: 「だな。そして、キルクイティウムの製造コストは、\n体積が二倍で二乗、三倍で三乗になると言われている」
TW: 「嗯。而且，鐶的製造成本會隨著體積指數增長」
CUR: 「Đúng vậy. Hơn nữa, chi phí sản xuất Quirquitium được cho là\nthể tích tăng gấp đôi thì chi phí bình phương, gấp ba thì lập phương.」


### Phụ lục T60 — 頭取 (29 dòng)

--- 00_Common | 共通11_経営資源.txt.toml | key=2696 | char=ポーレット | src=csv3
JP: 「はい。計画の主導者は多分、隈元銀行頭取で、\n[きさき,1]稀咲さんのお父様である、[ほうしょうもとただ,3]宝生元忠さんですけど」
TW: 「是的。計劃的主導者應該就是隈元銀行總行長，稀咲小姐的父親——寶生元忠」
VN(csv3): 「Vâng. Người chủ đạo kế hoạch có lẽ là tổng giám đốc Ngân hàng Kumamoto,\ncha của cô Kisaki, ông Houshou Mototada.」
CUR: 「Vâng. Người chủ đạo kế hoạch có lẽ là tổng giám đốc Ngân hàng Kumamoto,\ncha của cô Kisaki, ông Houshou Mototada.」
--- 00_Common | 共通11_経営資源.txt.toml | key=3448 | char=monologue | src=csv3
JP: 宝生元忠。あの娘の父にして、大銀行の頭取か。\nどのような人物なのか、一度会いたい気もしてくる。
TW: 寶生元忠。稀咲的父親，大銀行的行長。我不禁想親眼看看對方是個怎樣的人物。
VN(csv3): Houshou Mototada. Cha của cô gái đó, và là tổng giám đốc của một ngân hàng lớn sao.\nTự nhiên tôi cũng muốn gặp một lần xem ông ta là người thế nào.
CUR: Houshou Mototada. Cha của cô gái đó, và là tổng giám đốc của một ngân hàng lớn sao.\nTự nhiên tôi cũng muốn gặp một lần xem ông ta là người thế nào.
--- 00_Common | 共通14_負債.txt.toml | key=1882 | char=浦上 | src=csv3
JP: 「これは頭取」\n「仕事の邪魔はやめてくれないかな」
TW: 「行長您好」\n「能不能不要妨礙我工作呀」
VN(csv3): 「Kính chào ngài chủ tịch.」\n「Xin ông đừng làm phiền công việc của tôi được không.」
CUR: 「Kính chào ngài chủ tịch.」\n「Xin ông đừng làm phiền công việc của tôi được không.」
--- 00_Common | 共通14_負債.txt.toml | key=1884 | char=双鉄 | src=csv3
JP: 「頭取？」
TW: 「行長？」
VN(csv3): 「Chủ tịch?」
CUR: 「Chủ tịch?」
--- 00_Common | 共通14_負債.txt.toml | key=1551 | char=元忠 | src=csv3
JP: 「おいおい御一夜支店長。\n頭取に対し、『やめてくれないかな』は無いだろう」
TW: 「喂喂，御一夜支行長。對行長說話怎麼能用這種口氣呢」
VN(csv3): 「Này này giám đốc chi nhánh Ohimitera.\nNói với chủ tịch mà lại dùng từ 'được không' sao.」
CUR: 「Này này giám đốc chi nhánh Ohimitera.\nNói với chủ tịch mà lại dùng từ 'được không' sao.」
--- 00_Common | 共通14_負債.txt.toml | key=1112 | char=稀咲 | src=csv3
JP: 「知らない仲でないなら畏まるな――と、\nそうおっしゃったのは頭取ご自身ですが？」
TW: 「“既然認識就不要客氣”——這不是行長您自己說的嗎？」
VN(csv3): 「'Nếu không phải người dưng thì đừng có khách sáo'——\nChẳng phải chính ngài chủ tịch đã nói vậy sao?」
CUR: 「'Nếu không phải người dưng thì đừng có khách sáo'——\nChẳng phải chính ngài chủ tịch đã nói vậy sao?」
--- 00_Common | 共通14_負債.txt.toml | key=2708 | char=monologue | src=csv3
JP: 立場で人の何をはかれるわけでもないが――\nそれにしたって、頭取がこれはあまりにも気さくにすぎる。
TW: 雖然不能用身份去衡量一個人——但是行長這個樣子，未免有些太平易近人了。
VN(csv3): Dù không thể đánh giá con người qua địa vị——\nNhưng mà, một chủ tịch như thế này thì lại thân thiện quá mức rồi.
CUR: Dù không thể đánh giá con người qua địa vị——\nNhưng mà, một chủ tịch như thế này thì lại thân thiện quá mức rồi.
--- 00_Common | 共通14_負債.txt.toml | key=1972 | char=双鉄 | src=csv3
JP: 「なら――頭取――\n元忠さんは、汰斗さんの？」
TW: 「那麼，行長——元忠先生，您跟汰斗老爺是？」
VN(csv3): 「Vậy thì——chủ tịch——\nÔng Mototada, có quan hệ thế nào với ông Taito?」
CUR: 「Vậy thì——chủ tịch——\nÔng Mototada, có quan hệ thế nào với ông Taito?」
--- 00_Common | 共通14_負債.txt.toml | key=2200 | char=monologue | src=csv3
JP: ざっくばらんに、という頭取指示に、\nある程度、浦上も寄せるつもりなのだろうか。
TW: 估計浦上也打算在一定程度上，遵從行長“直言不諱”的命令吧。
VN(csv3): Chỉ thị "cứ thẳng thắn đi" của chủ tịch,\nphải chăng Urakami cũng định tuân theo ở một mức độ nào đó.
CUR: Chỉ thị "cứ thẳng thắn đi" của chủ tịch,\nphải chăng Urakami cũng định tuân theo ở một mức độ nào đó.
--- 01_Hachiroku | ハチロク01_こんにちわ赤ちゃん.txt.toml | key=1676 | char=稀咲 | src=csv3
JP: 「……双鉄は頭取の扱いがとても上手いね。\n当行各支店にも、一人ずつ双鉄を備えたいくらいだ」
TW: 「……雙鐵，你還真是會應付行長啊。我都想給每個支行配上一個你了」
VN(csv3): 「……Soutetsu đối phó với Giám đốc giỏi thật đấy.\nĐến mức tôi muốn mỗi chi nhánh của ngân hàng chúng tôi đều có một Soutetsu luôn.」
CUR: 「……Soutetsu đối phó với Giám đốc giỏi thật đấy.\nĐến mức tôi muốn mỗi chi nhánh của ngân hàng chúng tôi đều có một Soutetsu luôn.」
--- 01_Hachiroku | ハチロク01_こんにちわ赤ちゃん.txt.toml | key=2138 | char=稀咲 | src=csv3
JP: 「気がついていなかったのかい？　\n今日の頭取は機嫌が最悪だった。財務省から」
TW: 「你難道沒注意到嗎？今天行長的心情可是糟得不行，因為財務省那邊——」
VN(csv3): 「Cậu không nhận ra sao?\nHôm nay tâm trạng của Giám đốc cực kỳ tồi tệ. Từ lúc ở Bộ Tài chính về.」
CUR: 「Cậu không nhận ra sao?\nHôm nay tâm trạng của Giám đốc cực kỳ tồi tệ. Từ lúc ở Bộ Tài chính về.」
--- 01_Hachiroku | ハチロク12_再開発.txt.toml | key=2364 | char=稀咲 | src=csv3
JP: 「行員レベルでは、誘致断念の空気が強めかな。\nけど――頭取はまだ、\x%lエアクラ;#00ffc040;エアクラ%l;#;工場誘致を諦めてない」
TW: 「社員層面上基本都瀰漫著放棄落戶的氛圍。不過，行長本人還沒有放棄\x%lエアクラ;#00ffc040;空凝機%l;#;工廠落戶的方案」
VN(csv3): 「Ở cấp độ nhân viên thì bầu không khí từ bỏ việc mời gọi đang khá mạnh.\nNhưng——Giám đốc vẫn chưa từ bỏ việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」
CUR: 「Ở cấp độ nhân viên thì bầu không khí từ bỏ việc mời gọi đang khá mạnh.\nNhưng——Giám đốc vẫn chưa từ bỏ việc mời gọi nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;.」
--- 01_Hachiroku | ハチロク12_再開発.txt.toml | key=2874 | char=monologue | src=csv3
JP: 父であり頭取である宝生元忠への対抗心、\nそれも、恐らく、大いに影響しているのだろうと。
TW: 她對既是父親又是行長的寶生元忠的對抗心理，恐怕起到了莫大的作用。
VN(csv3): Tâm lý đối kháng với Houshou Mototada, người vừa là cha vừa là Giám đốc ngân hàng,\ncó lẽ đã ảnh hưởng rất lớn đến cô ấy.
CUR: Tâm lý đối kháng với Houshou Mototada, người vừa là cha vừa là Giám đốc ngân hàng,\ncó lẽ đã ảnh hưởng rất lớn đến cô ấy.
--- 01_Hachiroku | ハチロク14_橋.txt.toml | key=1731 | char=稀咲 | src=csv3
JP: 「だからそれは整理して、落ち着いたときに聞いて欲しい。\n娘ではなく、支店長として。父さんではなく、頭取に」
TW: 「所以這件事等我整理好思路，情緒穩定下來再來跟你說。以行長和支行行長，而不是父親和女兒的身份」
VN(csv3): 「Thế nên chuyện đó hãy để con sắp xếp lại, lúc nào bình tĩnh rồi con sẽ nói cho bố nghe.\nKhông phải với tư cách con gái, mà là Giám đốc chi nhánh. Không phải nói với bố, mà là với Chủ tịch.」
CUR: 「Thế nên chuyện đó hãy để con sắp xếp lại, lúc nào bình tĩnh rồi con sẽ nói cho bố nghe.\nKhông phải với tư cách con gái, mà là Giám đốc chi nhánh. Không phải nói với bố, mà là với Chủ tịch.」
--- 01_Hachiroku | ハチロク15_家族.txt.toml | key=1759 | char=ハチロク | src=csv3
JP: 「[ほうしょうもとただ,3]宝生元忠……\nやはり、[くまぎん,1]隈銀の頭取たる人物なのですね」
TW: 「寶生元忠……果然是堪當隈元銀行行長的人物啊」
VN(csv3): 「Houshou Mototada……\nQuả nhiên là nhân vật xứng tầm Chủ tịch ngân hàng Kumagin nhỉ.」
CUR: 「Houshou Mototada……\nQuả nhiên là nhân vật xứng tầm Chủ tịch ngân hàng Kumagin nhỉ.」
--- 01_Hachiroku | ハチロク15_家族.txt.toml | key=2059 | char=双鉄 | src=csv3
JP: 「[かね]金のことなら、無論、銀行は専門だろうが……\n頭取ともなると違うな。これほど大きな絵を描けるとは」
TW: 「雖然知道銀行是金錢方面的專家……不過行長的眼光果然不凡，竟描繪出了如此廣闊的前景」
VN(csv3): 「Nếu nói về tiền bạc, tất nhiên ngân hàng là chuyên gia rồi……\nNhưng ở tầm Chủ tịch thì đúng là khác biệt. Không ngờ ông ấy có thể vẽ ra một bức tranh lớn đến vậy.」
CUR: 「Nếu nói về tiền bạc, tất nhiên ngân hàng là chuyên gia rồi……\nNhưng ở tầm Chủ tịch thì đúng là khác biệt. Không ngờ ông ấy có thể vẽ ra một bức tranh lớn đến vậy.」
--- 02_Hibiki | 日々姫01_リゾート食堂列車計画.txt.toml | key=1996 | char=稀咲 | src=csv3
JP: 「それは――そうだね。単なる、頭取の気まぐれさ。\nあの人が急に、僕のスケジュールを横取りしたから」
TW: 「那是因為——對了，只是行長心血來潮罷了。是他突然搶走了我原來的行程」
VN(csv3): 「Đó là——đúng rồi. Chỉ đơn giản là sự bốc đồng của giám đốc ngân hàng thôi.\nVì người đó đột nhiên cướp mất lịch trình của tôi.」
CUR: 「Đó là——đúng rồi. Chỉ đơn giản là sự bốc đồng của giám đốc ngân hàng thôi.\nVì người đó đột nhiên cướp mất lịch trình của tôi.」
--- 02_Hibiki | 日々姫01_リゾート食堂列車計画.txt.toml | key=1805 | char=稀咲 | src=csv3
JP: 「なるほどなるほど？　双鉄の頼み――じゃないね、\n頭取の気まぐれが、偶然にも良く機能したわけだ」
TW: 「明白了。雙鐵的請求……不，行長的心血來潮偶爾也會帶來好處啊」
VN(csv3): 「Ra là vậy, ra là vậy? Lời nhờ vả của Soutetsu——không phải nhỉ,\nsự bốc đồng của giám đốc ngân hàng tình cờ lại mang đến kết quả tốt đẹp.」
CUR: 「Ra là vậy, ra là vậy? Lời nhờ vả của Soutetsu——không phải nhỉ,\nsự bốc đồng của giám đốc ngân hàng tình cờ lại mang đến kết quả tốt đẹp.」
--- 02_Hibiki | 日々姫06_日々姫の決断.txt.toml | key=2897 | char=真闇 | src=csv3
JP: 「それはそーとね。稀咲ちゃんと双ちゃんが互角として、\n頭取の宝生さんとウチとが、互角」
TW: 「那倒有得一拼。現在稀咲妹妹和小雙是不相上下，寶生行長和咱也是不相上下」
VN(csv3): 「Cái đó thì cũng phải xem đã. Cho là bé Kisaki và Sou-chan ngang tài ngang sức đi,\nthì Giám đốc Houshou và chị cũng ngang ngửa nhau.」
CUR: 「Cái đó thì cũng phải xem đã. Cho là bé Kisaki và Sou-chan ngang tài ngang sức đi,\nthì Giám đốc Houshou và chị cũng ngang ngửa nhau.」
--- 03_Paulette | ポーレット09_ストーブ客車.txt.toml | key=2161 | char=双鉄 | src=csv3
JP: 「隈元銀行頭取――宝生元忠氏によるわけか」
TW: 「要由隈元銀行行長——寶生元忠先生來判斷嗎」
VN(csv3): 「Do chủ tịch Ngân hàng Kumamoto――ông Houshou Mototada quyết định sao.」
CUR: 「Do chủ tịch Ngân hàng Kumamoto――ông Houshou Mototada quyết định sao.」
--- 03_Paulette | ポーレット09_ストーブ客車.txt.toml | key=2131 | char=稀咲 | src=csv3
JP: 「そして、無能な支店長とは違い。\n有能な頭取は、国政レベルに働きかけられる」
TW: 「而與某個無能的支行長不同，優秀的行長，能從國家政策層面進行干涉」
VN(csv3): 「Và, khác với một giám đốc chi nhánh bất tài.\nMột chủ tịch tài ba, có thể tác động đến cả cấp độ quốc gia.」
CUR: 「Và, khác với một giám đốc chi nhánh bất tài.\nMột chủ tịch tài ba, có thể tác động đến cả cấp độ quốc gia.」
--- 05_Mayami | 真闇h3_補習授業の廃校舎.txt.toml | key=2469 | char=双鉄 | src=csv3
JP: 「宝生稀咲も賛同してくれている話らしい。\n頭取――宝生元忠も巻き込めそうだと」
TW: 「寶生稀咲好像也贊成了。她還要把行長――寶生元忠也給拉進來呢」
VN(csv3): 「Nghe nói Houshou Kisaki cũng tán thành chuyện này.\nCó vẻ như sẽ lôi kéo được cả Giám đốc――Houshou Mototada vào nữa.」
CUR: 「Nghe nói Houshou Kisaki cũng tán thành chuyện này.\nCó vẻ như sẽ lôi kéo được cả Giám đốc――Houshou Mototada vào nữa.」
--- 06_Kisaki | グランドリライト06_稀咲.txt.toml | key=3319 | char=monologue | src=csv3
JP: 頭取ではなく、父さんと――\n呼ばわる声に応じたように、一番奥の扉が開く。
TW: 稀咲喊的不是行長，而是爸爸——最裡面的門隨著話語聲打開了。
VN(csv3): Không phải là Chủ tịch, mà là Bố――\nNhư để đáp lại tiếng gọi, cánh cửa trong cùng mở ra.
CUR: Không phải là Chủ tịch, mà là Bố――\nNhư để đáp lại tiếng gọi, cánh cửa trong cùng mở ra.
--- 06_Kisaki | グランドリライト06_稀咲.txt.toml | key=3338 | char=monologue | src=csv3
JP: 視線での僕の問いに応えて、稀咲が耳打ちしてくれる。\n頭取ではなく、父さんと。
TW: 稀咲用目光回答我的疑問，在我耳邊輕聲說道。用的稱呼不是行長，而是爸爸。
VN(csv3): Đáp lại ánh mắt dò hỏi của tôi, Kisaki thì thầm vào tai.\nKhông phải Chủ tịch, mà là Bố.
CUR: Đáp lại ánh mắt dò hỏi của tôi, Kisaki thì thầm vào tai.\nKhông phải Chủ tịch, mà là Bố.
--- 06_Kisaki | 稀咲01_金と人.txt.toml | key=1887 | char=稀咲 | src=audit
JP: 「父さ――と、頭取っ！？」
TW: 「爸——行、行長！？」
VN(csv3): 「Ta vào được chứ? Có chuyện công việc.」
CUR: 「Bố――à không, Chủ tịch!?」
--- 06_Kisaki | 稀咲01_金と人.txt.toml | key=1256 | char=稀咲 | src=audit
JP: 「……父と、頭取、どっちの立場で」
TW: 「……您是以什麼立場來說這句話的？是父親，還是行長？」
VN(csv3): 「Là mệnh lệnh công việc. Giám đốc chi nhánh.」
CUR: 「……Bố đang nói với tư cách là Bố, hay là Chủ tịch vậy?」
--- 06_Kisaki | 稀咲h1_性生活.txt.toml | key=1416 | char=稀咲 | src=audit
JP: 「いや、慣れっこさ。\n双鉄は巻き込まれただけ。首謀者は父――頭取だ」
TW: 「沒事，我都習慣了。你只是被捲進來的，罪魁禍首是爸爸――行長」
VN(csv3): 「Không sao, tôi quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」
CUR: 「Không sao, em quen rồi.\nAnh Soutetsu chỉ bị cuốn vào thôi. Kẻ chủ mưu là bố——giám đốc ngân hàng cơ.」
--- 09_Grand | グランドリライト01_オール御一夜、成立ならず.txt.toml | key=2523 | char=稀咲 | src=csv3
JP: 「頭取としては、実現可能性に乏しいと？」
TW: 「您的意思是，從行長的角度看，認為這件事很難實現？」
VN(csv3): 「Với tư cách là Giám đốc ngân hàng, ngài cho rằng khả năng thực hiện được là rất thấp sao?」
CUR: 「Với tư cách là Giám đốc ngân hàng, ngài cho rằng khả năng thực hiện được là rất thấp sao?」
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=2052 | char=双鉄 | src=csv3
JP: 「ああ。元忠さんに隈銀頭取を追われるようなリスクを、\n決して負わせてはならん」
TW: 「是啊，絕不能讓元忠先生承受被撤職的風險」
VN(csv3): 「Ừ. Tuyệt đối không được để ông Mototada\nphải chịu rủi ro bị mất chức Giám đốc Ngân hàng Kumamoto.」
CUR: 「Ừ. Tuyệt đối không được để ông Mototada\nphải chịu rủi ro bị mất chức Giám đốc Ngân hàng Kumamoto.」


### Phụ lục T61 — 持株会社 (10 dòng)

--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=1549 | char=双鉄 | src=csv3
JP: 「……まずは近県の鉄道会社との、持株会社の設立。か」
TW: 「……首先與鄰縣的鐵路公司成立控股公司嗎」
VN(csv3): 「……Trước tiên là thành lập một công ty cổ phần, với các công ty đường sắt ở các tỉnh lân cận. Sao.」
CUR: 「……Trước tiên là thành lập một công ty cổ phần, với các công ty đường sắt ở các tỉnh lân cận. Sao.」
--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=2131 | char=ハチロク | src=csv3
JP: 「持株会社、とはどのようなものなのですか？」
TW: 「控股公司是指什麼呢？」
VN(csv3): 「Công ty cổ phần, là loại hình như thế nào vậy ạ?」
CUR: 「Công ty cổ phần, là loại hình như thế nào vậy ạ?」
--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=2189 | char=双鉄 | src=csv3
JP: 「そこで、真闇姉を社長とする持株会社を、\nそれぞれの酒蔵を束ねる、親会社として設立するのだ」
TW: 「此時，我們要讓真闇姐擔任社長的控股公司成為管理各個酒窖的母公司」
VN(csv3): 「Vì vậy, anh sẽ thành lập một công ty cổ phần do chị Mayami làm giám đốc,\nvới tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại với nhau.」
CUR: 「Vì vậy, anh sẽ thành lập một công ty cổ phần do chị Mayami làm giám đốc,\nvới tư cách là công ty mẹ, để tập hợp các nhà xưởng ủ rượu lại với nhau.」
--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=2143 | char=双鉄 | src=csv3
JP: 「経営の集約をしつつ独立性も維持できるのが持株会社だ。\nそれは当然、第三、第四の企業の参入を促しやすくする」
TW: 「既能匯總經營，又能維持獨立性，這便是控股公司的特徵。當然也容易吸引第三、第四家企業的加入」
VN(csv3): 「Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty cổ phần.\nĐiều đó đương nhiên, sẽ giúp dễ dàng thúc đẩy sự tham gia của các doanh nghiệp thứ ba, thứ tư.」
CUR: 「Vừa có thể tập trung kinh doanh, vừa duy trì được tính độc lập, đó chính là công ty cổ phần.\nĐiều đó đương nhiên, sẽ giúp dễ dàng thúc đẩy sự tham gia của các doanh nghiệp thứ ba, thứ tư.」
--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=1536 | char=ハチロク | src=csv3
JP: 「……[だいきゅしゅう,2]大九洲ＳＬ構想を成立、発展させていくため。\n持株会社は、なるほど、優れた仕組みなのですね」
TW: 「……我明白了。要想讓大九州蒸汽機車藍圖得以成立並發展壯大，控股公司確實是很合適的結構」
VN(csv3): 「……Để thiết lập và phát triển kế hoạch Đại Kyushu SL.\nCông ty cổ phần, ra là vậy, đúng là một cơ cấu xuất sắc nhỉ.」
CUR: 「……Để thiết lập và phát triển kế hoạch Đại Kyushu SL.\nCông ty cổ phần, ra là vậy, đúng là một cơ cấu xuất sắc nhỉ.」
--- 01_Hachiroku | ハチロク12_再開発.txt.toml | key=2258 | char=稀咲 | src=audit
JP: 「そのための持株会社設立案だ。もちろん、\n支店レベルで、低利での貸付けも行わせてもらいたい」
TW: 「所以才提出要成立控股公司。當然，能在支行層面拿到低利率的貸款就更好了」
VN(csv3): 「Đó là lý do tôi đề xuất thành lập công ty cổ phần. Tất nhiên,\ntôi cũng muốn chi nhánh có thể cho vay với lãi suất thấp.」
CUR: 「Đó là lý do tôi đề xuất thành lập công ty holding. Tất nhiên, tôi cũng muốn chi nhánh có thể cho vay với lãi suất thấp.」
--- 01_Hachiroku | ハチロク12_再開発.txt.toml | key=2381 | char=双鉄 | src=audit
JP: 「鉄道他社との持株会社を設立すること――\n資金面でも、信用面でも、それが必須となるわけか」
TW: 「與其他鐵路公司聯合成立控股公司……看來不管是從資金角度還是信任角度，都別無選擇了啊」
VN(csv3): 「Thành lập công ty cổ phần cùng các công ty đường sắt khác——\nCả về mặt vốn lẫn uy tín, đó là điều bắt buộc phải không.」
CUR: 「Thành lập công ty holding cùng các công ty đường sắt khác—— Cả về mặt vốn lẫn uy tín, đó là điều bắt buộc phải không.」
--- 01_Hachiroku | ハチロク12_再開発.txt.toml | key=1699 | char=ハチロク | src=audit
JP: 「……持株会社への参加を促す――そのためにも、\n説得力のある資料が必要となるのですね？」
TW: 「……讓別人參加控股公司——想要達成這個目標，也同樣需要拿出具有說服力的資料吧？」
VN(csv3): 「……Thúc đẩy việc tham gia công ty cổ phần——Để làm được điều đó,\ncũng cần phải có những tài liệu mang tính thuyết phục đúng không ạ?」
CUR: 「……Thúc đẩy việc tham gia công ty holding——Để làm được điều đó, cũng cần phải có những tài liệu mang tính thuyết phục đúng không ạ?」
--- 01_Hachiroku | ハチロク15_家族.txt.toml | key=1953 | char=ポーレット | src=csv3
JP: 「\x%lエアクラ;#00ffc040;エアクラ%l;#;工場の誘致を支援して、\nかわりに、持株会社への参加を促す」
TW: 「聲援\x%lエアクラ;#00ffc040;空凝機%l;#;工廠在當地落戶，作為交換，促進對股份公司的參股」
VN(csv3): 「Sẽ hỗ trợ thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\nđổi lại, thúc đẩy họ tham gia vào công ty cổ phần.」
CUR: 「Sẽ hỗ trợ thu hút nhà máy \x%lエアクラ;#00ffc040;Aircra%l;#;,\nđổi lại, thúc đẩy họ tham gia vào công ty cổ phần.」
--- 04_Reina | れいな03_しゅっぱつしんこう.txt.toml | key=1568 | char=ポーレット | src=csv3
JP: 「矢幡製鉄所さんの呼びかけで、\n持株会社形式で運営されることになるそうですよ」
TW: 「據說是在八幡煉鐵廠呼籲下建立，並由其作為控股公司主導運營」
VN(csv3): 「Theo lời kêu gọi của nhà máy luyện thép Yahata,\nhọ sẽ hoạt động dưới hình thức công ty cổ phần đấy.」
CUR: 「Theo lời kêu gọi của nhà máy luyện thép Yahata,\nhọ sẽ hoạt động dưới hình thức công ty cổ phần đấy.」


### Phụ lục T62 — 民由連 (1 dòng)

--- 01_Hachiroku | ハチロク09_採決.txt.toml | key=2411 | char=議長 | src=csv3
JP: 「この[さい]際、関連の質疑に入ります。\n[みんゆうれん,2]民由連、斉藤委員」
TW: 「那麼藉此場合提出對本方案的疑問。請民友連的齋藤委員提問」
VN(csv3): 「Nhân dịp này, chúng ta sẽ bước vào phần hỏi đáp liên quan.\nỦy viên Saitou của Đảng Dân Do.」
CUR: 「Nhân dịp này, chúng ta sẽ bước vào phần hỏi đáp liên quan.\nỦy viên Saitou của Đảng Dân Do.」


### Phụ lục T63 — 帝有鉄道 (4 dòng) + 帝有 (7 dòng)

--- 01_Hachiroku | グランドリライト10_ハチロク.txt.toml | key=1134 | char=monologue | src=audit
JP: ……旧帝鉄、日ノ本帝有鉄道の懐中時計。
TW: ……這是一隻前帝國鐵路，帝家日本國鐵路的懷表。
VN(csv3): ……Đồng hồ bỏ túi của Đường sắt Hoàng gia cũ, Đường sắt Hoàng gia Hinamoto.
CUR: ……Đồng hồ bỏ túi của Teitetsu cũ, Đường sắt Đế quốc Hinomoto.
--- 02_Hibiki | 日々姫02_文庫森.txt.toml | key=60 | char=monologue | src=csv3
JP: \x%l明智;#00ffc040;明智%l;#;三十九年。鉄道帝有法制定。布告。\n日ノ本帝有鉄道発足。
TW: \x%l明智;#00ffc040;明治%l;#;三十九年。鐵路國有法制定，頒布。帝家日本國鐵路成立。
VN(csv3): Năm \x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\nĐường sắt Hoàng gia Hinomoto chính thức ra đời.
CUR: Năm \x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\nĐường sắt Hoàng gia Hinomoto chính thức ra đời.
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2248 | char=日々姫 | src=csv3
JP: 「日ノ本帝有鉄道のオーナー、[ヒノモトノミカド,3]日ノ本帝から、\nミカドって愛称になったと！？」
TW: 「由於帝家日本國鐵路的所有人是日本國[米卡多]帝，所以愛稱就叫“帝”了嗎！？」
VN(csv3): 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado),\nđể đặt biệt danh là Mikado sao!?」
CUR: 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado),\nđể đặt biệt danh là Mikado sao!?」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2082 | char=西瓜 | src=csv3
JP: 「老師の日ノ本帝有鉄道――帝鉄への接し方は、\n確かに研究でしたけれど、それだけでなく……ん……」
TW: 「師父對於帝家日本國鐵路——對於帝國鐵路確實是抱以研究的態度，不過不僅如此……嗯……」
VN(csv3): 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia,\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」
CUR: 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia,\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」

--- 01_Hachiroku | グランドリライト10_ハチロク.txt.toml | key=1134 | char=monologue | src=audit
JP: ……旧帝鉄、日ノ本帝有鉄道の懐中時計。
TW: ……這是一隻前帝國鐵路，帝家日本國鐵路的懷表。
VN(csv3): ……Đồng hồ bỏ túi của Đường sắt Hoàng gia cũ, Đường sắt Hoàng gia Hinamoto.
CUR: ……Đồng hồ bỏ túi của Teitetsu cũ, Đường sắt Đế quốc Hinomoto.
--- 01_Hachiroku | ハチロク03_冥国式レイルロオド.txt.toml | key=2337 | char=ハチロク | src=csv3
JP: 「のちに[ていゆうか,2]帝有化され、[ていてつみのぶせん,4]帝鉄実延線となった路線ですね。\n比較的早期……確か、私鉄時代に電化された筈です」
TW: 「就是後來帝有化，成為帝國鐵路身延線的線路。在相對早期……應該是私營鐵路時代就電力化了」
VN(csv3): 「Là tuyến đường sau này được quốc hữu hóa thành tuyến Minobu của Teitetsu đó ạ.\nNó được điện khí hóa khá sớm…… chắc là từ thời còn là đường sắt tư nhân.」
CUR: 「Là tuyến đường sau này được quốc hữu hóa thành tuyến Minobu của Teitetsu đó ạ.\nNó được điện khí hóa khá sớm…… chắc là từ thời còn là đường sắt tư nhân.」
--- 02_Hibiki | 日々姫01_双鉄の妹.txt.toml | key=1789 | char=双鉄 | src=csv3
JP: 「『日ノ本帝有鐵道、蒸気機関車設計図面集』」
TW: 「《帝家日本國鐵路蒸汽機車設計圖集》」
VN(csv3): 「『Đường sắt Hoàng gia Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』」
CUR: 「『Đường sắt Hoàng gia Hinomoto, Tập bản vẽ thiết kế đầu máy hơi nước』」
--- 02_Hibiki | 日々姫02_文庫森.txt.toml | key=60 | char=monologue | src=csv3
JP: \x%l明智;#00ffc040;明智%l;#;三十九年。鉄道帝有法制定。布告。\n日ノ本帝有鉄道発足。
TW: \x%l明智;#00ffc040;明治%l;#;三十九年。鐵路國有法制定，頒布。帝家日本國鐵路成立。
VN(csv3): Năm \x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\nĐường sắt Hoàng gia Hinomoto chính thức ra đời.
CUR: Năm \x%l明智;#00ffc040;Meiji%l;#; thứ ba mươi chín. Đạo luật Đường sắt Hoàng gia được ban hành. Công bố.\nĐường sắt Hoàng gia Hinomoto chính thức ra đời.
--- 02_Hibiki | 日々姫02_文庫森.txt.toml | key=1727 | char=日々姫 | src=csv3
JP: 「帝有化で……経営の自由度がなくなった、でしたか？」
TW: 「國有化……剝奪了經營的自由嗎？」
VN(csv3): 「Quốc hữu hóa... làm mất đi sự tự do trong kinh doanh sao ạ?」
CUR: 「Quốc hữu hóa... làm mất đi sự tự do trong kinh doanh sao ạ?」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2248 | char=日々姫 | src=csv3
JP: 「日ノ本帝有鉄道のオーナー、[ヒノモトノミカド,3]日ノ本帝から、\nミカドって愛称になったと！？」
TW: 「由於帝家日本國鐵路的所有人是日本國[米卡多]帝，所以愛稱就叫“帝”了嗎！？」
VN(csv3): 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado),\nđể đặt biệt danh là Mikado sao!?」
CUR: 「Nên lấy từ tên của chủ sở hữu Đường sắt Đế hữu Hinomoto, Hoàng đế Hinomoto (Mikado),\nđể đặt biệt danh là Mikado sao!?」
--- 10_Chikuni | 仲国03_北琴鉄道歴史館.txt.toml | key=2082 | char=西瓜 | src=csv3
JP: 「老師の日ノ本帝有鉄道――帝鉄への接し方は、\n確かに研究でしたけれど、それだけでなく……ん……」
TW: 「師父對於帝家日本國鐵路——對於帝國鐵路確實是抱以研究的態度，不過不僅如此……嗯……」
VN(csv3): 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia,\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」
CUR: 「Cách tiếp cận của Sư phụ đối với Đường sắt Đế hữu Hinomoto——Đường sắt Hoàng gia,\nđúng là nghiên cứu, nhưng không chỉ có vậy…… ừm……」


### Phụ lục T64 — 冥語 (1 dòng)

--- 01_Hachiroku | ハチロク05_レイルロオドたち.txt.toml | key=3512 | char=monologue | src=audit
JP: 冥語の鋭い叫びとともに、\n差し伸べられたハチロクの手がはねのけられる。
TW: 奧莉薇邊用英語尖叫著，邊推開了八六伸過來的手。
VN(csv3): （Cùng với tiếng thét chói tai bằng tiếng Mỹ,\ncô ấy hất văng bàn tay đang chìa ra của Hachiroku.）
CUR: （Cùng với tiếng thét chói tai bằng tiếng Minh Quốc,\ncô ấy hất văng bàn tay đang chìa ra của Hachiroku.）


### Phụ lục T65 — 橙汁 (3 dòng)

--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=2089 | char=日々姫 | src=csv3
JP: 「それに、パッケージとかはもう異国やけん！\nオレンジジュースば『橙汁』って、面白かとよねー」
TW: 「而且這些包裝都是外國版的咧！“橙汁”的這個寫法也很有趣不是嗎」
VN(csv3): 「Với lại, bao bì thì đậm chất nước ngoài luôn rồi!\nNước cam mà gọi là 『Trừng trấp』, thú vị ghê nhỉ~」
CUR: 「Với lại, bao bì thì đậm chất nước ngoài luôn rồi!\nNước cam mà gọi là 『Trừng trấp』, thú vị ghê nhỉ~」
--- 10_Chikuni | 仲国01_副丘→北琴.txt.toml | key=1828 | char=日々姫 | src=csv3
JP: 「あ、日ノ本語喋れるアテンダントさん！\nうふふ、嬉しか！　じゃ、私は橙汁！　もう一杯！」
TW: 「啊，是會說日語的空服！太好咧！那我要再來一大杯橙汁！」
VN(csv3): 「A, cô tiếp viên nói được tiếng Hinomoto!\nUfufu, vui quá! Vậy, cho tôi một ly Trừng trấp! Một ly nữa!」
CUR: 「A, cô tiếp viên nói được tiếng Hinomoto!\nUfufu, vui quá! Vậy, cho tôi một ly Trừng trấp! Một ly nữa!」
--- 10_Chikuni | 仲国08_謝謝再見！.txt.toml | key=2054 | char=日々姫 | src=csv3
JP: 「あとね、ご褒美。んっと……橙汁！\n自販機のでいいから、買ってほしかと」
TW: 「還有，我要獎勵！我想想……就橙汁吧！自動販賣機的也可以，幫我買一瓶吧」
VN(csv3): 「Với lại, phần thưởng. Ừm…… nước cam!\nMua ở máy bán hàng tự động cũng được, anh mua cho em nha.」
CUR: 「Với lại, phần thưởng. Ừm…… nước cam!\nMua ở máy bán hàng tự động cũng được, anh mua cho em nha.」


### Phụ lục T66 — 九国 (6 dòng)

--- 05_Mayami | グランドリライト07_真闇.txt.toml | key=2546 | char=双鉄 | src=csv3
JP: 「リレートレイン・ナインスターズ。\n九洲九国を、九つの客室で周遊する観光列車」
TW: 「接力列車·九星。擁有九間客房，周遊九州九國的觀光列車」
VN(csv3): "「Relay Train Nine Stars (Chuyến tàu tiếp sức Chín Ngôi Sao).\nChuyến tàu du lịch dạo quanh chín vùng Kyushu với chín khoang hành khách.」"
CUR: "「Relay Train Nine Stars (Chuyến tàu tiếp sức Chín Ngôi Sao).\nChuyến tàu du lịch dạo quanh chín vùng Kyushu với chín khoang hành khách.」"
--- 05_Mayami | グランドリライト07_真闇.txt.toml | key=2545 | char=双鉄 | src=csv3
JP: 「ナインスターズは、九洲九国を九日間かけ、\nゆったりと贅沢に周遊していく」
TW: 「按照我的想法，九星會耗時九天，奢華而悠閒地周遊九州九國」
VN(csv3): "「Nine Stars sẽ dành chín ngày để dạo quanh chín vùng Kyushu,\nmột chuyến du ngoạn thong thả và xa hoa.」"
CUR: "「Nine Stars sẽ dành chín ngày để dạo quanh chín vùng Kyushu,\nmột chuyến du ngoạn thong thả và xa hoa.」"
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=2711 | char=monologue | src=csv3
JP: ナインスターズ客車各室が九洲九国であるならば、\n関門海峡を渡り、それぞれの部屋に向かうべき。
TW: 既然要將九星的各個客車房間作為九州九國，那就應該渡過關門海峽再前往各自的房間。
VN(csv3): Nếu mỗi phòng trên toa khách Nine Stars là một trong chín tỉnh của Kyushu,\nthì hành khách nên băng qua Eo biển Kanmon rồi mới tiến vào từng phòng.
CUR: Nếu mỗi phòng trên toa khách Nine Stars là một trong chín tỉnh của Kyushu,\nthì hành khách nên băng qua Eo biển Kanmon rồi mới tiến vào từng phòng.
--- 09_Grand | グランドリライト08_ふかみ.txt.toml | key=2496 | char=monologue | src=csv3
JP: ――九洲九国。それぞれの国を、それぞれの客室に。\nこのコンセプトは、どの主要都市にも受け入れられた。
TW: 九州九國，讓每個客房都能展示一國特色。每座主要城市都接納了我們的這個理念。
VN(csv3): ――Kyushu chín tỉnh. Mỗi tỉnh một phòng khách.\nÝ tưởng này đã được tất cả các thành phố lớn chấp thuận.
CUR: ――Kyushu chín tỉnh. Mỗi tỉnh một phòng khách.\nÝ tưởng này đã được tất cả các thành phố lớn chấp thuận.
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=3231 | char=monologue | src=csv3
JP: 九洲九国をそれぞれの客室に当てはめた、\nその名も九洲な、[きゅうじゅう,1]90系客車群。
TW: 九間客房與九州九國一一對應並以其命名，客運車廂的型號“９０系”亦與此呼應。
VN(csv3): Nhóm toa hành khách dòng 90 mang đậm chất Kyushu,\nvới mỗi phòng khách tượng trưng cho chín tỉnh của Kyushu.
CUR: Nhóm toa hành khách dòng 90 mang đậm chất Kyushu,\nvới mỗi phòng khách tượng trưng cho chín tỉnh của Kyushu.
--- 09_Grand | グランドリライト11_ナインスターズ！.txt.toml | key=2265 | char=ポーレット | src=csv3
JP: 「緊張しました～。[きゅうしゅうきゅうこく,3]九洲九国、[ゆかり]縁の殿様の末裔たちに、\n九洲[ななけん,1]七県の知事がずらりと勢揃いですから」
TW: 「可緊張死我了。畢竟九州九國各位領主的後裔、九州七縣的知事都齊聚一堂」
VN(csv3): 「Em hồi hộp lắm~. Con cháu của các vị lãnh chúa có liên quan đến chín tỉnh Kyushu,\ncùng thống đốc của bảy tỉnh Kyushu đều tề tựu đông đủ mà.」
CUR: 「Em hồi hộp lắm~. Con cháu của các vị lãnh chúa có liên quan đến chín tỉnh Kyushu,\ncùng thống đốc của bảy tỉnh Kyushu đều tề tựu đông đủ mà.」
