# Audit 00_Common file 15 — 共通15_回り始める動輪.txt.toml

**Ngày kiểm toán:** 20/11/2026
**Tệp TOML:** `00_Common/共通15_回り始める動輪.txt.toml` — md5 `3e8962a81d4d874c12d33ca89c7a201c`, 106.839 byte, BOM, CRLF (1.045 CRLF, 0 LF-only), `[selections]` rỗng, **không có bản sao trùng** (kiểm tra md5 toàn bộ 227 tệp TOML).
**Nguồn CSV:** "Trang tính 3" — bộ hàng duy nhất `00_Common` (không có bẫy dual-set ở file này), 492 hàng `[script]`.
**Kết quả: 27/492 dòng sai (5,5%), 0 dòng chưa chắc chắn, 0 dòng lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo file.**

## 1. Tổng quan

| Phân loại | Số dòng sai |
|---|---|
| Thuật ngữ (terminology) | 18 |
| Đại từ xưng hô (pronoun) | 5 |
| Sai nghĩa (meaning) | 2 |
| Tiếng thở/gasp (gasp) | 1 |
| SFX (tiếng thở/cảm thán) | 1 |
| **Tổng** | **27** |

Key 2308 tính vào nhóm đại từ nhưng đồng thời sửa 1 lỗi thuật ngữ (Ohimitera→Ohitoyo); tổng số dòng chạm vào thuật ngữ là 19.

**Theo loại dòng:** thoại 17/251 sai (6,8%), độc thoại 10/241 sai (4,1%).
**Theo nhân vật:** 双鉄 (Soutetsu) 6, 日々姫 (Hibiki) 4, ハチロク (Hachiroku) 4, monologue 10, 蓑笠 (Minokasa) 1, ポーレット (Paulette) 1, 凪 (Nagi) 1.

Nhóm thuật ngữ (19 dòng chạm, 18 tính riêng): 御一夜→Ohitoyo 14 dòng / 15 lần (1544, 1795, 2064 [×2], 2173, 2307, 2308, 2312, 2339, 2673, 2895, 2903, 2942, 3307, 3358 — toàn bộ "Ohimitera" trong file); 運転体→"thân vận hành" 3 dòng (1516, 2619, 2938 — "cơ thể lái tàu"/"thân chính"); 整備体→"thân bảo trì" 1 dòng (3140); タブレット→"máy tính bảng" 1 dòng (2619, cùng dòng với 運転体 — cùng lỗi "thẻ bảng" như Paulette 04 stove); 帝鉄→"Teitetsu" 1 dòng (3108); 湯医線→"tuyến Yunoi" 1 dòng (2903, cùng dòng với Ohimitera — dòng "Yui" thứ 8 toàn dự án (sau P14 83, P16 2032, file 12 3391, file 14 1435/1571/1671/1805)). Nhóm đại từ (5): Hibiki tự xưng "chị"→"em" với Soutetsu 2 dòng (1843 [×2], 2132 [×3]); Soutetsu gọi "cô"→"em" 1 dòng (1943); Soutetsu tự xưng "anh"→"tôi" với Hachiroku 2 dòng (2063, 2308 — 2308 kèm Ohimitera). Sai nghĩa (2): 1541 (bịa "Dù" + làm mất 確かだ), 1951 ("rất biết ơn" bịa thêm). Gasp (1): 1906 từ sweep, đã kiểm chứng. SFX (1): 2378 nghiến răng → "Ken két".

File này sạch về cấu trúc — 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 key trùng. Tỷ lệ sai 5,5% thấp thứ ba trong nhóm 00_Common (sau file 03: 4,8% và file 04: 4,9%) — lỗi tập trung ở thuật ngữ chưa cập nhật theo các quyết định 19–20/11 (đặc biệt Ohimitera 15 lần) và vài đại từ, không phải lỗi cấu trúc. Toàn bộ 27 lỗi đều sửa được tại chỗ, không cần dịch lại.

## 2. Phương pháp và độ tin cậy của nguồn

- **Xác minh tệp:** đối chiếu theo tên tệp + nội dung, không theo đường dẫn thư mục. TOML md5 `3e8962a81d4d874c12d33ca89c7a201c`, BOM + CRLF, `[selections]` rỗng, không có bản sao trùng trong 227 tệp.
- **CSV vs TOML:** VN khớp tuyệt đối 194 hàng; khớp sau khi gộp ký tự xuống dòng thành khoảng trắng 294 hàng; **4 khác biệt — đều là hiện tượng gộp `\n` thành khoảng trắng trong TOML (biến thể double-backslash), KHÔNG phải lỗi dịch**. CSV3 là bản chuẩn cho fix list.
- **Sweep っ (gasp):** sweep CÓ liệt kê file này — 2 mục trong sweep-raw-gasp-wrong.json: 1906 (lost-gasp-whole, đã kiểm chứng đúng, áp nguyên) và 1474 (**BÁC — giá trị sweep sai, audit thắng sweep**, xem §4). Quét っ hệ thống trên toàn bộ 174 dòng JP chứa っ: không có gasp っ trần nào khác bị mất.
- **Thẻ %l:** JP 284 thẻ, VN 284 thẻ — khớp tuyệt đối. Không có thẻ %l đóng sai định dạng nào trong VN (kiểm tra `%l;#` không có `;` cuối: 0 dòng). JP có 4 thẻ đóng sai ở phía nguồn (1501, 2594, 2858, 2927 — cùng mẫu file 07/09/10) nhưng VN đã chuẩn hoá, KHÔNG phải lỗi VN, không sửa.
- **Kiểm tra toàn vẹn:** không có hàng nào chưa dịch (VN rỗng: 0), không có VN mồ côi (orphan: 0), không có key trùng. Chỉ 1 hàng VN == TW là key 1517 (JP/TW/VN đều là 「…………」 — dấu lặng, hợp lệ, không phải chưa dịch).
- **Kiểm tra nhiễm chéo:** đối chiếu 27 giá trị VN cũ trong fix list qua chỉ mục VN toàn dự án — 155 lần trùng đều là câu ngắn thông dụng (「Ừm.」, 「Đúng vậy.」…) dịch độc lập giống nhau; 0 lần trùng VN trong file với JP khác nhau. Toàn bộ 492 VN đều khớp đúng JP của chính dòng mình.
- **Thứ tự dòng:** key số trong file này KHÔNG phải thứ tự truyện — các cảnh xen kẽ nhau theo key (như file 11/13). Vì vậy địa chỉ người nghe được xác định từ nội dung dòng + mạch hội thoại (ai nói trước/sau về cùng chủ đề, TW dùng đại từ số nhiều/số ít), KHÔNG dùng key kề nhau theo thứ tự số. Bằng chứng: 1943 (người nghe suy từ lời mời song song 1956→1958), 2063/2308 (trả lời Hachiroku ở 2060/2307).

## 3. Các lỗi đã sửa (27 dòng)

### 1516 — 双鉄 — terminology

**JP:** 「『運転試験　ハチロク』か。単純であるがかわいらしい。⏎このマンガは、運転[ボディ]体のハチロクだな？」

**TW:** 「“走行測試八六”。很簡單，不過很可愛。這漫畫畫的，是八六的駕駛體吧？」

**VN cũ:** 「『Chạy thử nghiệm Hachiroku』 à. Đơn giản nhưng đáng yêu thật.⏎Hình vẽ manga này là cơ thể lái tàu của Hachiroku nhỉ?」

**Fix:** 「『Chạy thử nghiệm Hachiroku』 à. Đơn giản nhưng đáng yêu thật.⏎Hình vẽ manga này là thân vận hành của Hachiroku nhỉ?」

運転体 = "thân vận hành" (quyết chốt; "cơ thể lái tàu" không thống nhất với file 08/10/13).

### 1541 — 双鉄 — meaning

**JP:** 「……正直、わからん。⏎そのために整備修復してきたことは、確かだが」

**TW:** 「……說實話，我不知道。但我們整備和修復為的就是讓它跑起來」

**VN cũ:** 「……Thành thật mà nói, anh không biết.⏎Dù mục đích của việc bảo dưỡng và phục hồi là để nó chạy được.」

**Fix:** 「……Thành thật mà nói, anh không biết.⏎Nhưng chắc chắn là chúng ta đã bảo dưỡng và phục hồi nó để nó chạy được.」

JP 「そのために整備修復してきたことは、確かだが」: khẳng định CHẮC CHẮN đã bảo dưỡng/phục hồi vì mục đích đó (TW: 為的就是讓它跑起來). Bản cũ bịa "Dù" (nhượng bộ không có trong JP) và làm mất 確かだ.

### 1544 — 蓑笠 — terminology

**JP:** 「……御一夜の職人たちの、誇りば感じる仕事ですな。⏎新旧部品すり合わせ良し、ぴたりハマっておりますばい」

**TW:** 「……這工作真讓御一夜的匠人們感到驕傲啊。新舊零件磨合得非常完美」

**VN cũ:** 「……Quả là một công việc mang đầy niềm tự hào của những người thợ thủ công Ohimitera nhỉ.⏎Việc mài khớp các bộ phận cũ và mới rất tốt, vừa khít luôn.」

**Fix:** 「……Quả là một công việc mang đầy niềm tự hào của những người thợ thủ công Ohitoyo nhỉ.⏎Việc mài khớp các bộ phận cũ và mới rất tốt, vừa khít luôn.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 1795 — 双鉄 — terminology

**JP:** 「つながりの力で、御一夜の力で。⏎――みんなで、8620の傷を、直したんだ」

**TW:** 「依靠人與人的情誼，依靠御一夜的力量——我們一起修好了８６２０」

**VN cũ:** 「Bằng sức mạnh của sự kết nối, bằng sức mạnh của Ohimitera.⏎——Tất cả mọi người, đã cùng nhau sửa chữa vết thương của 8620.」

**Fix:** 「Bằng sức mạnh của sự kết nối, bằng sức mạnh của Ohitoyo.⏎——Tất cả mọi người, đã cùng nhau sửa chữa vết thương của 8620.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 1843 — 日々姫 — pronoun

**JP:** 「見学会のチラシのときに、資料、いろいろ調べて。⏎それで、記念の時にはあった方がいいかと思ったの」

**TW:** 「參觀會做傳單的時候，我查了不少資料。所以，我覺得在這個值得紀念的時刻有會它更好」

**VN cũ:** 「Lúc làm tờ rơi cho buổi tham quan, chị đã tìm hiểu rất nhiều tài liệu.⏎Nên chị nghĩ, vào những dịp kỷ niệm thì có cái này sẽ tốt hơn.」

**Fix:** 「Lúc làm tờ rơi cho buổi tham quan, em đã tìm hiểu rất nhiều tài liệu.⏎Nên em nghĩ, vào những dịp kỷ niệm thì có cái này sẽ tốt hơn.」

Hibiki tự xưng "em" với Soutetsu (1536, 2332, 2344 trong file này; "em" 1157 vs "chị" 352 toàn dự án). Dòng này giải thích banner với Soutetsu/nhóm.

### 1906 — ハチロク — gasp

**JP:** 「まぁ」⏎「っ！」

**TW:** 「哎呀」⏎「！」

**VN cũ:** 「Chà.」⏎「!」

**Fix:** 「Chà.」⏎「Ư!」

Sweep lost-gasp-whole, kiểm chứng đúng vs JP: 「まぁ」\n「っ！」 — っ trần ở đầu dòng = tiếng hít (tiền lệ file 09 key 2802).

### 1943 — 双鉄 — pronoun

**JP:** 「うん。言ってみてくれ」

**TW:** 「嗯，你說吧」

**VN cũ:** 「Ừm. Cô cứ nói đi.」

**Fix:** 「Ừm. Em cứ nói đi.」

Soutetsu gọi người nghe là "em" — mọi đối tượng khả dĩ (Nagi/Hibiki/Paulette/Hachiroku) đều lấy "em"; "cô" sai với tất cả. Người nghe suy từ lời mời song song 1956→1958 (Nagi).

### 1951 — ハチロク — meaning

**JP:** 「ええ、本当に」

**TW:** 「嗯，是啊」

**VN cũ:** 「Vâng, thật sự rất biết ơn.」

**Fix:** 「Vâng, đúng vậy.」

JP 「ええ、本当に」= "Vâng, đúng vậy." — "rất biết ơn" bịa thêm, JP không có biết ơn (kiểu bịa của Gemini).

### 2063 — 双鉄 — pronoun

**JP:** 「わかっている。ゆっくり、少しずつ、まんべんなくだ」

**TW:** 「我知道。我會慢慢地、一點點地、均衡地來」

**VN cũ:** 「Anh biết rồi. Phải từ từ, từng chút một, và trải đều ra.」

**Fix:** 「Tôi biết rồi. Phải từ từ, từng chút một, và trải đều ra.」

Soutetsu tự xưng "tôi" với Hachiroku (quy tắc đã sửa 20/11) — trả lời Hachiroku ở 2060 về vận hành đầu máy.

### 2064 — 日々姫 — terminology

**JP:** 「もっと御一夜のことを良く知ったほうがいいと思うの。⏎兄さんが、御一夜を本当に復興させたいんなら」

**TW:** 「我覺得如果哥哥真的想振興御一夜的話，應該去更加深入地了解御一夜」

**VN cũ:** 「Em nghĩ anh nên tìm hiểu thêm về Ohimitera.⏎Nếu anh thực sự muốn phục hưng Ohimitera.」

**Fix:** 「Em nghĩ anh nên tìm hiểu thêm về Ohitoyo.⏎Nếu anh thực sự muốn phục hưng Ohitoyo.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai). (2 lần trong dòng).

### 2132 — 日々姫 — pronoun

**JP:** 「決まりとかあるなら違っちゃってるかもしれないし、⏎プラバンに油絵の具だから、強度も正直わかんないけど」

**TW:** 「有可能和傳統當中的不一樣，材質是塑膠板，上色用的油畫顏料，到底耐不耐用我也不清楚」

**VN cũ:** 「Nếu có quy định gì đó thì có thể chị đã làm sai,⏎và vì chị vẽ bằng sơn dầu trên tấm nhựa dẻo nên thú thật chị cũng không rõ độ bền của nó đâu.」

**Fix:** 「Nếu có quy định gì đó thì có thể em đã làm sai,⏎và vì em vẽ bằng sơn dầu trên tấm nhựa dẻo nên thú thật em cũng không rõ độ bền của nó đâu.」

Hibiki tự xưng "em" với Soutetsu — trả lời câu hỏi của Soutetsu ở 2130, Soutetsu đồng tình ở 2133.

### 2173 — ハチロク — terminology

**JP:** 「御一夜温泉駅入線。一番ホーム。停止準備を」

**TW:** 「準備進入御一夜溫泉站，一號站台。準備停車」

**VN cũ:** 「Tiến vào ga suối nước nóng Ohimitera. Sân ga số 1. Chuẩn bị dừng lại.」

**Fix:** 「Tiến vào ga suối nước nóng Ohitoyo. Sân ga số 1. Chuẩn bị dừng lại.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2307 — ハチロク — terminology

**JP:** 「これが、御一夜――⏎双鉄様が守ろうとしている、町と人たちなのですね」

**TW:** 「這就是御一夜——這就是雙鐵少爺想要守護的城市和人嗎」

**VN cũ:** 「Đây là, Ohimitera——⏎Là thị trấn và những con người mà ngài Soutetsu đang cố gắng bảo vệ đúng không ạ.」

**Fix:** 「Đây là, Ohitoyo——⏎Là thị trấn và những con người mà ngài Soutetsu đang cố gắng bảo vệ đúng không ạ.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2308 — 双鉄 — pronoun

**JP:** 「これが御一夜、僕を育ててくれた町だ。⏎守ろうなどとはおこがましいが――」

**TW:** 「這就是御一夜。哺育我長大的城市。守護這個詞用起來太自大了——」

**VN cũ:** 「Đây là Ohimitera, thị trấn đã nuôi dưỡng anh khôn lớn.⏎Nói là bảo vệ thì có vẻ hơi kiêu ngạo nhưng——」

**Fix:** 「Đây là Ohitoyo, thị trấn đã nuôi dưỡng tôi khôn lớn.⏎Nói là bảo vệ thì có vẻ hơi kiêu ngạo nhưng——」

御一夜 = "Ohitoyo"; Soutetsu tự xưng "tôi" với Hachiroku — trả lời Hachiroku ở 2307.

### 2312 — ポーレット — terminology

**JP:** 「今回の試験走行までで、御一夜のキーマンが何人も、⏎双鉄くんを信頼してくれたと思いますし、その人脈も」

**TW:** 「通過這次的走行測試，御一夜有幾個大人物應該已經開始信任你了，他們的熟人也會同樣信任你」

**VN cũ:** 「Cho đến cuộc chạy thử nghiệm lần này, tôi nghĩ đã có rất nhiều nhân vật chủ chốt của Ohimitera⏎tin tưởng anh Soutetsu, và cả những mối quan hệ đó nữa.」

**Fix:** 「Cho đến cuộc chạy thử nghiệm lần này, tôi nghĩ đã có rất nhiều nhân vật chủ chốt của Ohitoyo⏎tin tưởng anh Soutetsu, và cả những mối quan hệ đó nữa.」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2339 — 日々姫 — terminology

**JP:** 「酒蔵のことも、私の看板描きやなにもかも、⏎御一夜の人と密接するお仕事でしょ？　だから――」

**TW:** 「酒窖裡的工作，還有我畫招牌畫的工作，都是與御一夜的人息息相關的工作。所以——」

**VN cũ:** 「Chuyện xưởng rượu, chuyện vẽ biển hiệu của em và mọi thứ khác,⏎đều là những công việc gắn liền với người dân Ohimitera đúng không? Vì vậy——」

**Fix:** 「Chuyện xưởng rượu, chuyện vẽ biển hiệu của em và mọi thứ khác,⏎đều là những công việc gắn liền với người dân Ohitoyo đúng không? Vì vậy——」

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2378 — 凪 — sfx

**JP:** 「ぐぎぎぎぎぎぎ」

**TW:** 「（咬牙切齒）」

**VN cũ:** 「Gừ gừ gừ gừ gừ」

**Fix:** 「Ken két ken két ken két」

ぐぎぎぎ = nghiến răng (TW: 咬牙切齒). "Gừ" là tiếng gầm — sai loại âm. "Ken két" là tiếng nghiến răng tiếng Việt.

### 2619 — monologue — terminology

**JP:** かちり、\x%lタブレット;#00ffc040;タブレット%l;#;が交換される。⏎ぱちり、\x%l運転体;#00ffc040;運転体%l;#;のハチロクの目が開く。

**TW:** 交換完\x%lタブレット;#00ffc040;操作板%l;#;，八六的\x%l運転体;#00ffc040;駕駛體%l;#;睜開了眼。

**VN cũ:** Cạch, \x%lタブレット;#00ffc040;thẻ bảng%l;#; được hoán đổi.⏎Chớp chớp, đôi mắt của Hachiroku \x%l運転体;#00ffc040;thân chính%l;#; mở ra.

**Fix:** Cạch, \x%lタブレット;#00ffc040;máy tính bảng%l;#; được hoán đổi.⏎Chớp chớp, đôi mắt của Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; mở ra.

タブレット = "máy tính bảng" (entry 38 docs; "thẻ bảng" sai); 運転体 = "thân vận hành".

### 2673 — monologue — terminology

**JP:** 同じく観光振興、御一夜再生を目的として、⏎しかし手段は１８０度異なっている。

**TW:** 儘管目的同樣是振興旅遊業、振興御一夜，但手段卻完全不同。

**VN cũ:** Cùng có chung mục đích là chấn hưng du lịch, tái thiết Ohimitera,⏎nhưng phương tiện lại khác nhau 180 độ.

**Fix:** Cùng có chung mục đích là chấn hưng du lịch, tái thiết Ohitoyo,⏎nhưng phương tiện lại khác nhau 180 độ.

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2895 — monologue — terminology

**JP:** \x%l石造機関庫;#00ffc040;石造機関庫%l;#;から御一夜駅ホームまで。⏎全行程で１キロも無い、新生\x%l8620;#00ffc040;8620%l;#;、初めての旅。

**TW:** 從\x%l石造機関庫;#00ffc040;石製機車庫%l;#;到御一夜站站台，全程不到一公里。新\x%l8620;#00ffc040;８６２０%l;#;第一次踏上了旅途。

**VN cũ:** Từ \x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; đến sân ga Ohimitera.⏎Toàn bộ hành trình chưa đến 1 km, chuyến đi đầu tiên của \x%l8620;#00ffc040;8620%l;#; mới sinh.

**Fix:** Từ \x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; đến sân ga Ohitoyo.⏎Toàn bộ hành trình chưa đến 1 km, chuyến đi đầu tiên của \x%l8620;#00ffc040;8620%l;#; mới sinh.

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 2903 — monologue — terminology

**JP:** 御一夜周辺――湯医線沿線やクマ川流域の広くからも、⏎数えきれぬほどの応援と励ましと手とを、いただいた。

**TW:** 御一夜附近——包括湯醫線沿線還有隈河流域的居民們，都給予了我們無數的鼓勵與幫助。

**VN cũ:** Xung quanh Ohimitera——dọc theo tuyến Yui và trên một khu vực rộng lớn của lưu vực sông Kuma,⏎chúng tôi đã nhận được vô số sự ủng hộ, động viên và giúp đỡ.

**Fix:** Xung quanh Ohitoyo——dọc theo tuyến Yunoi và trên một khu vực rộng lớn của lưu vực sông Kuma,⏎chúng tôi đã nhận được vô số sự ủng hộ, động viên và giúp đỡ.

御一夜 = "Ohitoyo"; 湯医線 = "tuyến Yunoi" (quyết chốt; "Yui" sai — dòng Yui thứ 8 toàn dự án).

### 2938 — monologue — terminology

**JP:** \x%l機関士;#00ffc040;機関士%l;#;鞄を大きく開き、⏎中から\x%l運転体;#00ffc040;運転体%l;#;のハチロクを取り出す。

**TW:** 我打開\x%l機関士;#00ffc040;司機%l;#;專用包，從中取出八六的\x%l運転体;#00ffc040;駕駛體%l;#;。

**VN cũ:** Tôi mở rộng chiếc cặp \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;,⏎lấy Hachiroku \x%l運転体;#00ffc040;thân chính%l;#; từ bên trong ra.

**Fix:** Tôi mở rộng chiếc cặp \x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;,⏎lấy Hachiroku \x%l運転体;#00ffc040;thân vận hành%l;#; từ bên trong ra.

運転体 = "thân vận hành" (quyết chốt; "thân chính" sai).

### 2942 — monologue — terminology

**JP:** \x%l汽笛;#00ffc040;汽笛%l;#;を鳴らす。⏎ホームの、御一夜の人たちに、心の限りの感謝を込めて。

**TW:** 我拉響了\x%l汽笛;#00ffc040;汽笛%l;#;。向站台上的、御一夜的人們表達最真誠的謝意。

**VN cũ:** Tôi kéo \x%l汽笛;#00ffc040;còi hơi nước%l;#;.⏎Gửi gắm vào đó tất cả lòng biết ơn chân thành nhất đến những người dân Ohimitera trên sân ga.

**Fix:** Tôi kéo \x%l汽笛;#00ffc040;còi hơi nước%l;#;.⏎Gửi gắm vào đó tất cả lòng biết ơn chân thành nhất đến những người dân Ohitoyo trên sân ga.

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 3108 — monologue — terminology

**JP:** ポーレットの\x%lまいてつ;#00ffc040;まいてつ%l;#;仲間や、赤井宮司の人脈から⏎集まってくれた旧\x%l帝鉄;#00ffc040;帝鉄%l;#;の技師さんや職員さんたち。

**TW:** 波萊特的\x%lまいてつ;#00ffc040;掌車人%l;#;伙伴，以及赤井宮司認識的那些前\x%l帝鉄;#00ffc040;帝國鐵路%l;#;的技師與員工們——

**VN cũ:** Những người bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của Paulette, cùng với các kỹ sư và nhân viên của \x%l帝鉄;#00ffc040;Đường sắt Hoàng gia%l;#; cũ⏎được tập hợp lại thông qua mạng lưới quan hệ của đền chủ Akai.

**Fix:** Những người bạn \x%lまいてつ;#00ffc040;chủ tàu%l;#; của Paulette, cùng với các kỹ sư và nhân viên của \x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ⏎được tập hợp lại thông qua mạng lưới quan hệ của đền chủ Akai.

帝鉄 = "Teitetsu" (quyết chốt 21:20; "Đường sắt Hoàng gia" là dịch sai 帝→皇). まいてつ "chủ tàu" và 宮司 "đền chủ Akai" trong cùng dòng đã đúng, giữ nguyên.

### 3140 — monologue — terminology

**JP:** そのまま崩れる\x%l整備体;#00ffc040;整備体%l;#;のハチロクを、⏎機関庫内にしつらえた、専用席へと座らせる。

**TW:** 然後將八六癱倒在地上的\x%l整備体;#00ffc040;整備體%l;#;扶坐在機車庫裡設置的專用座位上。

**VN cũ:** Tôi đỡ lấy Hachiroku \x%l整備体;#00ffc040;thân chính%l;#; đang đổ gục xuống,⏎và đặt em ấy ngồi vào chiếc ghế chuyên dụng được chuẩn bị sẵn trong xưởng đầu máy.

**Fix:** Tôi đỡ lấy Hachiroku \x%l整備体;#00ffc040;thân bảo trì%l;#; đang đổ gục xuống,⏎và đặt em ấy ngồi vào chiếc ghế chuyên dụng được chuẩn bị sẵn trong xưởng đầu máy.

整備体 = "thân bảo trì" (quyết chốt; "thân chính" sai).

### 3307 — monologue — terminology

**JP:** 赤井宮司が招いてくれた粉蔵時代の技師さんは、⏎さらに仲間の技師たちに、御一夜へ来るよう誘ってくれた。

**TW:** 赤井宮司請來了他在小倉時認識的技師，而他又邀請了更多的技師同伴們來到了御一夜。

**VN cũ:** Kỹ sư thời ở nhà máy bột mà đền chủ Akai mời đến,⏎lại tiếp tục rủ thêm các kỹ sư đồng nghiệp đến Ohimitera.

**Fix:** Kỹ sư thời ở nhà máy bột mà đền chủ Akai mời đến,⏎lại tiếp tục rủ thêm các kỹ sư đồng nghiệp đến Ohitoyo.

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

### 3358 — monologue — terminology

**JP:** 点火材として使うにはもったいないほどのそれは、⏎御一夜森林組合の皆様からの寄付品だ。

**TW:** 這是御一夜森林行會送給我們的。不得不說拿這個做引火物很浪費。

**VN cũ:** Dùng chúng làm mồi lửa thì thật lãng phí,⏎đây là món đồ được quyên góp từ mọi người trong Hiệp hội Lâm nghiệp Ohimitera.

**Fix:** Dùng chúng làm mồi lửa thì thật lãng phí,⏎đây là món đồ được quyên góp từ mọi người trong Hiệp hội Lâm nghiệp Ohitoyo.

御一夜 = "Ohitoyo" (quyết chốt; "Ohimitera" sai).

## 4. Kiểm tra chéo

- **Sweep っ-gasp:** 2 mục cho file này (1474, 1906). 1906 áp nguyên, đã kiểm chứng đúng với JP. **1474 BÁC — audit thắng sweep** (cùng lớp với các lần supersession ở h6): JP 「ブロワーっ！！」 là っ nhấn mạnh cuối câu gắn với thuật ngữ kỹ thuật được hô to; giá trị sweep thêm "Ư!!" nhưng VN "Thiết bị thổi gió!!" đã diễn độ nhấn bằng "!!". Mẫu giống hệt trong file này chưa từng bị sweep gắn cờ và chưa từng diễn thành Ư: 進行っ！ (1835), 良しっ！ (1973), よしっ！ (2000), ならばっ！ (2113). 1942 bare っ!? đã diễn ("Hả!?") — đúng nên không bị gắn cờ. Quét bổ sung toàn bộ 174 dòng JP chứa っ: còn lại đều là っ nhấn mạnh, っ trong từ, hoặc âm đã render đúng — không có gasp nào sweep bỏ sót.
- **Thẻ %l:** JP 284 = VN 284, khớp tuyệt đối (trước và sau fix — không có fix nào chạm thẻ). Không có thẻ đóng sai định dạng trong VN.
- **Nhiễm chéo:** 0 (xem §2).
- **Lệch dòng / chuỗi xoay:** 0. Không có dòng nào cần dịch lại từ đầu; không có chuỗi xoay; không có VN mồ côi.
- **Kiểm tra cơ học:** 27/27 fix khác VN cũ; 27/27 key dạng chuỗi, không trùng; 27/27 fix một dòng (không chứa ký tự xuống dòng thật — chỉ backslash-n dạng 2 ký tự); ngoặc 「 」 cân bằng 27/27; thẻ %l không đổi 27/27; 0 fix trùng VN của dòng khác trong file; 4 nhóm VN trùng trong file đều là câu ngắn lặp hợp lệ (「Ừm.」 ×3, 「Chuẩn bị đánh lửa tốt!」 ×2, 「Đánh lửa tốt!」 ×3, 「Đúng vậy.」 ×2).

## 5. Kiểm tra lần 2 (second pass)

Đọc lại toàn bộ 27 giá trị fix đối chiếu từng cái với JP gốc (đợt đọc thứ hai, độc lập với đợt đọc đầu): **tổng 27 / kiểm tra lại 27 / loại bỏ 0 / sửa lại 0**. Kiểm tra cơ học kèm theo: với mỗi fix, dùng difflib kiểm tra fix khác VN cũ CHỈ ở chỗ sửa có chủ đích (27/27) — ví dụ 2064 chỉ đổi "Ohimitera"→"Ohitoyo" ×2, 2308 chỉ đổi Ohimitera→Ohitoyo + "anh"→"tôi", 1541 là viết lại câu thứ hai theo đúng nghĩa JP (khẳng định chắc chắn, bỏ "Dù" bịa). Một chi tiết hiển thị đã được xác minh là artifact, không phải lỗi dữ liệu: dòng 3140 trong bản in làm việc hiện "整備���" nhưng byte JSON sạch — kiểm chứng bằng repr và bằng phép thử `fix.replace('thân bảo trì','thân chính') == old_vn`.

## 6. Các dòng cố tình KHÔNG sửa (ghi chú phán đoán)

- **Câu hỏi quy tắc Nagi — CẦN QUYẾT (flag cho parent/Hieu):** Nagi gọi Soutetsu にーさん ("anh hai") **326 lần toàn dự án** (so với "anh Soutetsu" 64 lần). Theo nguyên tắc xưng hô tương hỗ (đã chốt ở B4), Soutetsu là "anh" với Nagi. Điều này MÂU THUẪN với nhánh "tôi với Nagi" của quy tắc đại từ đã sửa 20/11. Bằng chứng trong file này: "anh" nhất quán ở 1461 và 2078; file 13 key 1907 giữ "anh" với Nagi; Nagi gọi "anh hai" ở 1958, 1988, 2091 trong file này. **KHÔNG sửa 1461/2078 thành "tôi".** Parent quyết xem có sửa quy tắc thành "anh với Nagi" không.
- **1461 + 2078 Soutetsu "anh" với Nagi:** xem trên — giữ nguyên theo nguyên tắc tương hỗ, chờ quyết.
- **1914 + 1938 Soutetsu "tôi" trong suy ngẫm nhóm:** giữ. Ghi chú: 1938 không nhất quán với 1936 ("anh" với Fukami) trong cùng mạch trao đổi — phán đoán giữ nguyên vì 1938 là suy ngẫm chung, không xưng hô trực tiếp với Fukami.
- **1775 + 2157 Hachiroku→Hibiki "chị Hibiki":** giữ. Đa số toàn dự án là "chị" (8 vs "cô" 1) — các dòng "cô" ở file 06 là ngoại lệ, không phải chuẩn.
- **2158 Minokasa→Soutetsu bare "Soutetsu!":** giữ. Đa số toàn dự án là bare (6 vs "Cậu Soutetsu" 2).
- **1775 + 2171 "Thị trưởng Paulette":** giữ — dùng 100+ lần toàn dự án.
- **2054 Michiko tự xưng "em":** giữ. Đa số toàn dự án "em" 23 vs "chị" 15 vs "tôi" 4 — chờ đợt thống nhất (unification pass).
- **2366 凪様→"Nagi":** giữ — cách gọi trực tiếp (vocative), bỏ kính ngữ là chấp nhận được.
- **3119 "của anh" trong tường thuật:** giữ — lời kể từ góc nhìn Hibiki (cô nói sẽ làm trợ lý của "anh trai" ở 2332).
- **31, 2774, 2792 しゅ/しゅん → "xình, xịch":** giữ — lựa chọn phong cách nhất quán cho tiếng hơi nước, không phải lỗi.
- **3437/3438 số nguyên âm tiếng còi:** giữ — phong cách, không sửa.
- **1474 sweep BÁC:** xem §4 — っ nhấn mạnh cuối câu, không phải gasp.
- **1501, 2594, 2858, 2927 thẻ %l JP đóng sai:** VN đã chuẩn hoá — không phải lỗi VN, không sửa.
- **1517 「…………」:** JP/TW/VN giống hệt nhau — dấu lặng, hợp lệ.

## Kết bài

File 15 là file 00_Common sạch về cấu trúc (27/492 = 5,5%): 0 lệch dòng, 0 chuỗi xoay, 0 nhiễm chéo, 0 dòng chưa dịch, 0 dòng chưa chắc chắn. Lỗi tập trung ở thuật ngữ chưa cập nhật theo các quyết định 19–20/11 (19 dòng chạm, đặc biệt toàn bộ 15 lần "Ohimitera" trong file đã được sửa hết) và vài đại từ/sai nghĩa do Gemini bịa. Toàn bộ 27 fix đều sửa tại chỗ, không cần dịch lại.

Sau file này, "Ohimitera" trong 00_Common chỉ còn **8 lần** (toàn bộ ở file 01 pilot, chưa chốt). Câu hỏi mở duy nhất cần quyết: nhánh "tôi với Nagi" của quy tắc đại từ Soutetsu có mâu thuẫn với 326 lần Nagi gọi "anh hai" không (xem §6) — 1461/2078 được giữ nguyên chờ quyết, không tự sửa.

Khối TOML dưới đây parse được bằng tomllib, **27 key, 0 sai lệch giá trị so với JSON**. Quy tắc ký tự xuống dòng: giá trị fix nào chứa ký tự xuống dòng dạng backslash-n (2 ký tự, như trong JSON và trong TOML gốc) thì trong khối này được ghi bằng 2 dấu backslash + n để tomllib parse lại thành đúng backslash-n — đã kiểm chứng bằng so sánh giá trị đã parse với JSON. (22 lần backslash-n trong 27 fix.)

```toml
[script]
"1516" = "「『Chạy thử nghiệm Hachiroku』 à. Đơn giản nhưng đáng yêu thật.\\nHình vẽ manga này là thân vận hành của Hachiroku nhỉ?」"
"1541" = "「……Thành thật mà nói, anh không biết.\\nNhưng chắc chắn là chúng ta đã bảo dưỡng và phục hồi nó để nó chạy được.」"
"1544" = "「……Quả là một công việc mang đầy niềm tự hào của những người thợ thủ công Ohitoyo nhỉ.\\nViệc mài khớp các bộ phận cũ và mới rất tốt, vừa khít luôn.」"
"1795" = "「Bằng sức mạnh của sự kết nối, bằng sức mạnh của Ohitoyo.\\n——Tất cả mọi người, đã cùng nhau sửa chữa vết thương của 8620.」"
"1843" = "「Lúc làm tờ rơi cho buổi tham quan, em đã tìm hiểu rất nhiều tài liệu.\\nNên em nghĩ, vào những dịp kỷ niệm thì có cái này sẽ tốt hơn.」"
"1906" = "「Chà.」\\n「Ư!」"
"1943" = "「Ừm. Em cứ nói đi.」"
"1951" = "「Vâng, đúng vậy.」"
"2063" = "「Tôi biết rồi. Phải từ từ, từng chút một, và trải đều ra.」"
"2064" = "「Em nghĩ anh nên tìm hiểu thêm về Ohitoyo.\\nNếu anh thực sự muốn phục hưng Ohitoyo.」"
"2132" = "「Nếu có quy định gì đó thì có thể em đã làm sai,\\nvà vì em vẽ bằng sơn dầu trên tấm nhựa dẻo nên thú thật em cũng không rõ độ bền của nó đâu.」"
"2173" = "「Tiến vào ga suối nước nóng Ohitoyo. Sân ga số 1. Chuẩn bị dừng lại.」"
"2307" = "「Đây là, Ohitoyo——\\nLà thị trấn và những con người mà ngài Soutetsu đang cố gắng bảo vệ đúng không ạ.」"
"2308" = "「Đây là Ohitoyo, thị trấn đã nuôi dưỡng tôi khôn lớn.\\nNói là bảo vệ thì có vẻ hơi kiêu ngạo nhưng——」"
"2312" = "「Cho đến cuộc chạy thử nghiệm lần này, tôi nghĩ đã có rất nhiều nhân vật chủ chốt của Ohitoyo\\ntin tưởng anh Soutetsu, và cả những mối quan hệ đó nữa.」"
"2339" = "「Chuyện xưởng rượu, chuyện vẽ biển hiệu của em và mọi thứ khác,\\nđều là những công việc gắn liền với người dân Ohitoyo đúng không? Vì vậy——」"
"2378" = "「Ken két ken két ken két」"
"2619" = "Cạch, \\x%lタブレット;#00ffc040;máy tính bảng%l;#; được hoán đổi.\\nChớp chớp, đôi mắt của Hachiroku \\x%l運転体;#00ffc040;thân vận hành%l;#; mở ra."
"2673" = "Cùng có chung mục đích là chấn hưng du lịch, tái thiết Ohitoyo,\\nnhưng phương tiện lại khác nhau 180 độ."
"2895" = "Từ \\x%l石造機関庫;#00ffc040;xưởng đầu máy bằng đá%l;#; đến sân ga Ohitoyo.\\nToàn bộ hành trình chưa đến 1 km, chuyến đi đầu tiên của \\x%l8620;#00ffc040;8620%l;#; mới sinh."
"2903" = "Xung quanh Ohitoyo——dọc theo tuyến Yunoi và trên một khu vực rộng lớn của lưu vực sông Kuma,\\nchúng tôi đã nhận được vô số sự ủng hộ, động viên và giúp đỡ."
"2938" = "Tôi mở rộng chiếc cặp \\x%l機関士;#00ffc040;nhân viên cơ vụ%l;#;,\\nlấy Hachiroku \\x%l運転体;#00ffc040;thân vận hành%l;#; từ bên trong ra."
"2942" = "Tôi kéo \\x%l汽笛;#00ffc040;còi hơi nước%l;#;.\\nGửi gắm vào đó tất cả lòng biết ơn chân thành nhất đến những người dân Ohitoyo trên sân ga."
"3108" = "Những người bạn \\x%lまいてつ;#00ffc040;chủ tàu%l;#; của Paulette, cùng với các kỹ sư và nhân viên của \\x%l帝鉄;#00ffc040;Teitetsu%l;#; cũ\\nđược tập hợp lại thông qua mạng lưới quan hệ của đền chủ Akai."
"3140" = "Tôi đỡ lấy Hachiroku \\x%l整備体;#00ffc040;thân bảo trì%l;#; đang đổ gục xuống,\\nvà đặt em ấy ngồi vào chiếc ghế chuyên dụng được chuẩn bị sẵn trong xưởng đầu máy."
"3307" = "Kỹ sư thời ở nhà máy bột mà đền chủ Akai mời đến,\\nlại tiếp tục rủ thêm các kỹ sư đồng nghiệp đến Ohitoyo."
"3358" = "Dùng chúng làm mồi lửa thì thật lãng phí,\\nđây là món đồ được quyên góp từ mọi người trong Hiệp hội Lâm nghiệp Ohitoyo."
```
