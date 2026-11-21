# Audit — グランドリライト07_真闇.txt.toml (05_Mayami / Grand 07)

- **File:** `グランドリライト07_真闇.txt.toml` — route 05_Mayami, Grand 07 (Soutetsu mơ về Michiko trên tàu; ngày nghỉ ở nhà với Hibiki; Mayami nhờ giúp ở xưởng rượu — nếm rượu shochu mới do Railord ủ, gặp Miyako; họp khẩn ở rail shop, Soutetsu đề xuất tàu du lịch "Relay Train Nine Stars" đi vòng 9 vùng Kyushu).
- **Đọc:** 530/530 dòng script (độc thoại 179, thoại 双鉄 145, 真闇 60, ポーレット 27, 稀咲 24, 日々姫 22, 路子 19, ハチロク 16, ふかみ 14, 凪 14, れいな 10) — đọc từng dòng đối chiếu JP + TW.
- **Sai: 131 dòng / 530 (24,7%) — 134 điểm sửa** (3 dòng mang 2 điểm: 1506, 2503, 2664).
- **Phân loại:** đại từ 99 điểm / 99 dòng; thuật ngữ 30 điểm / 29 dòng; sai nghĩa 4; gasp 1.
- **Lỗi hệ thống chính: cụm đại từ Soutetsu** — toàn bộ độc thoại trong file (77 dòng) dùng "em"/"anh" cho Soutetsu thay vì "Tôi" theo quy ước dự án; thoại với Mayami (17 dòng) dùng "em" thay vì "tôi"; Kisaki tự xưng "tôi" 4 dòng khi nói trực tiếp với Soutetsu thay vì "em". File nhất quán nội bộ theo kiểu anh/em, nhưng trái quy tắc đã chốt và trái tiền lệ đã merge (Common 14, Grand 01/06/11, file 09, lr_稀咲h1) — đúng mẫu Grand 11 đã dự báo ("các file chưa audit có cùng mẫu anh/em").

## §1. Kiểm tra cấu trúc — toàn 0

- **Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0.**
- **CSV3: 1 set duy nhất** (530 dòng, thư mục `translation_toml\\05_Mayami`), 0 khóa trùng, 0 VN trống, 0 JP trống. VN khớp phẳng TOML tuyệt đối 530/530 (kiểm chứng bằng tomllib, chuẩn hóa `\n` literal thành khoảng trắng theo cách TOML-2 flatten).
- **TOML:** 2 bản sao, md5 giống nhau `3442909231394adf2facd4c11dece514` — `05_Mayami/...07_真闇.txt.toml` và `09_Grand/...07_真闇.txt.toml`. Fix áp dụng cho CẢ HAI bản. File UTF-8 BOM + CRLF.
- **`[selections]` rỗng (0 mục). `[character_subs]` 7 mục đúng** (3068 "Tất cả", 3071 Hachiroku, 3310 Hibiki, 3347 Paulette, 3353 Fukami, 3355 Reina, 3544 Soutetsu).
- **Thẻ `%l`: 0 lệch.** Số thẻ JP = VN ở mọi dòng; 0 thẻ thiếu dấu `;` đóng. Thẻ JP lỗi phía JP mà VN đã chuẩn hóa thì không tính.
- **VN trùng lặp ở 2 khóa trở lên: 5 nhóm, đều đúng** — 「À——」 (2250/2288), 「Vậy sao.」 (2585/2796), 「Vậy sao?」 (2586/2794), 「A!!」 (2269/2261), 「Ồ!」 (2245/2244) — toàn câu cảm thán ngắn JP giống nhau.
- **Không còn っ thô trong VN.** Quét toàn bộ っ trong JP: toàn là gemination trong từ (れっ車, まったく…), SFX đã diễn (ぴゃうっ→"Pyau" 2218, あむっ→"Amu" 2161, くいっ→"Ực" 3573, がたっ→"Cạch" 3576, にいいっ→diễn thành "mỉm cười" 3391) hoặc gasp ở 2579 (§2).

## §2. Fix ngoài cụm đại từ (32 dòng / 35 điểm)

### 2a. Thuật ngữ đã chốt (27 dòng + 3 điểm kèm trong cụm đại từ = 30 điểm)

| Key | JP (trích) | Cũ → Mới | Ghi chú |
|---|---|---|---|
| 2276 | 赤井宮司 | "thầy cúng Akai" → "đền chủ Akai" | 宮司 = "đền chủ" đã chốt (tiền lệ Grand 06: 38 dòng). Gloss 運転士 "nhân viên cơ vụ" giữ nguyên theo tiền lệ (không tính sai). |
| 2482 | 御一夜 | "Ohimitera" → "Ohitoyo" | Quyết định 19/11. |
| 3426 | 御一夜市民 | "người dân Ohimitera" → "người dân Ohitoyo" | Như trên. |
| 2469 | オール御一夜体制 | "Thể chế toàn Ohimitera" → "Thể chế toàn Ohitoyo" | Như trên. |
| 2664 | オール御一夜 / オール湯医線 | "Ohimitera" + "tuyến Yui" → "Ohitoyo" + "tuyến Yunoi" | 2 điểm cùng dòng. |
| 2314 | 御一夜の木工家具 | "của Ohimitera" → "của Ohitoyo" | Như trên. |
| 2486 | 御一夜温泉駅 | "Ga suối nước nóng Ohimitera" → "Ga suối nước nóng Ohitoyo" | Như trên. |
| 2287 | 御一夜鉄道 | "Đường sắt Ohito" → "Đường sắt Ohitoyo" | Như trên. |
| 3185 | 御一夜鉄道 | "Đường sắt Ohito" → "Đường sắt Ohitoyo" | Như trên. |
| 2671 | 御一夜鉄道 | "Đường sắt Ohito" → "Đường sắt Ohitoyo" | Như trên. |
| 2120 | 御一夜鉄道に？ | "Đường sắt Ohito" → "Đường sắt Ohitoyo" | Như trên. |
| 2259 | 御一夜に | "đến Ohimitera" → "đến Ohitoyo" | Như trên. |
| 2815 | 御一夜よりも | "hơn là Ohimitera" → "hơn là Ohitoyo" | Như trên. |
| 1549 | 『レイル・ロマネスク湯医線』/ 湯医線全線 | "tuyến Yui" ×2 → "tuyến Yunoi" ×2 | 湯医線 = "Yunoi" đã chốt. "Showa" cho 正和 giữ nguyên — xem §6 (chưa chốt). |
| 1548 | 『レイル・ロマネスク湯医線』 | "tuyến Yui" → "tuyến Yunoi" | Như trên. "Ý tôi là" của Kisaki giữ nguyên — xem §6. |
| 1594 | 湯医線しか | "tuyến Yui" → "tuyến Yunoi" | Như trên. |
| 3443 | 帝鉄再興 | "Đường sắt Hoàng gia" → "Teitetsu" | 帝鉄 = "Teitetsu" trong lời thường (dạng đầy đủ "Đường sắt Đế quốc" chỉ trong thẻ %l lần đầu). |
| 3082 | 旧帝鉄9600形 | "Đường sắt Hoàng gia cũ" → "Teitetsu cũ" | Như trên. |
| 2407 | 帝鉄最末期 / 帝鉄が倒れ | "Đường sắt Hoàng gia" ×2 → "Teitetsu" ×2 | Như trên. |
| 2322 | 術仙いって | "đến Jussen" → "đến Jutsu-sen" | 術仙 = "Jutsu-sen" đã chốt. |
| 2559 | 術仙に向かう | "đến Jussen" → "đến Jutsu-sen" | Như trên. |
| 2848 | 術仙側とも | "phía Jussen" → "phía Jutsu-sen" | Như trên. |
| 2611 | 今の術仙でなら | "Jussen hiện tại" → "Jutsu-sen hiện tại" | Như trên. |
| 1605 | "右田一"と同じ酒造 | "Migitakazu" → "Migita Ichi" | Hướng thống nhất đã chốt "Migita Ichi" (ふかみh2 1096); "Migitakazu" (かず) trái dạng này. Còn 15 dòng "Migitakazu" khác toàn dự án — chờ đợt thống nhất. |
| 2728 | 右田一の複雑な深み | "Migitakazu" → "Migita Ichi" | Như trên. |
| 3548 | 電車姫様のコネ | "Denshahime-sama" → "Công chúa Tàu điện" | 電車姫 = "Công chúa Tàu điện" toàn dự án (quyết định 20/11). |
| 1525 | まいてつを迎え入れ | "chào đón Maitetsu" → "chào đón các chủ tàu" | まいてつ = "chủ tàu" đã chốt (tiền lệ Grand 11: 6 dòng). |

Ba điểm thuật ngữ kèm trong cụm đại từ: 1506 右田一酒店 "Migitakazu" → "Migita Ichi"; 2503 御一夜 "Ohimitera" → "Ohitoyo"; 2664 đã tính ở trên (2 điểm).

Sau khi sửa, file không còn dòng nào dùng "Ohimitera"/"Ohito", "Yui", "Jussen", "Migitakazu", "Đường sắt Hoàng gia", "Denshahime-sama", hay "Maitetsu" cho まいてつ.

### 2b. Sai nghĩa (4 dòng)

### 2756 [双鉄] — 余裕 dịch sai hình ảnh
- **JP:** 「赤井さんたちの加入で、全般、大きな余裕が生じた。」
- **TW:** 「赤井先生他們的加入極大地減輕了我們的負擔」
- **Cũ:** 「Sự tham gia của chú Akai đã tạo ra một khoảng trống lớn về mọi mặt.」
- **Mới:** 「Sự tham gia của chú Akai đã mang lại sự dư dả lớn trên mọi mặt.」
- **Lý do:** 余裕 = dư dả/thoải mái (leeway), TW "giảm gánh nặng" xác nhận; "khoảng trống" (empty space) sai hẳn hình ảnh.

### 2164 [双鉄] — sai chủ thể sở hữu
- **JP:** 「自分の機関車を解体されてなお……優しいこで、いつづけていてくれるのか」
- **TW:** 「即便自己的機車被拆解了……她還能保持自己溫柔的性格嗎」
- **Cũ:** 「Dù đầu máy của mình đã bị tháo dỡ…… Em ấy vẫn luôn là một cô bé dịu dàng sao.」
- **Mới:** 「Dù đầu máy của em ấy đã bị tháo dỡ…… Em ấy vẫn luôn là một cô bé dịu dàng sao.」
- **Lý do:** 自分 ở đây là Miyako (người đang được bàn — đầu máy của chính em ấy bị tháo dỡ); "của mình" không chủ ngữ trong tiếng Việt mặc định hiểu là của Soutetsu, sai người.

### 3164 [monologue] — sai chủ ngữ (TW phân biệt)
- **JP:** 強く頷く。――誰からも異論はでてこない。
- **TW:** 她用力地點了點頭。大家對此都全無異議。
- **Cũ:** Em gật đầu mạnh mẽ. ——Không một ai có ý kiến phản đối.
- **Mới:** Em ấy gật đầu mạnh mẽ. ——Không một ai có ý kiến phản đối.
- **Lý do:** TW 她 xác nhận người gật đầu là Fukami (người vừa nói ở 2785), không phải Soutetsu; "Em gật đầu" gán nhầm cho người kể chuyện.

### 2830 [双鉄] — 酒 dịch thành rượu vang
- **JP:** 「大歓迎だ。九洲各地、それぞれ自慢の焼酎や酒を客室で。――か、可能であればビュッフェ等で」
- **TW:** 「將九州各地引以為傲的燒酒和清酒等擺放在客房」
- **Cũ:** 「Hoan nghênh quá đi chứ. Khách hàng có thể thưởng thức những loại rượu shochu, rượu vang hảo hạng của khắp các vùng Kyushu ngay trong khoang hành khách.」
- **Mới:** 「Hoan nghênh quá đi chứ. Khách hàng có thể thưởng thức những loại rượu shochu, rượu sake hảo hạng của khắp các vùng Kyushu ngay trong khoang hành khách.」
- **Lý do:** 酒 ở đây là sake (TW 清酒), không phải rượu vang.

### 2c. Gasp — sweep (1 dòng)

### 2579 [双鉄] — lost-gasp-trailing (sweep)
- **JP:** 「だな。いっそ豪華に、電源車と冷蔵車をともに\x%l編成;#00ffc040;編成%l;#;し――っ！！」
- **TW:** 「是啊，乾脆奢侈點，在\x%l編成;#00ffc040;編組%l;#;裡同時掛發電車和保溫車——！！」
- **Cũ:** 「Đúng vậy. Hay là làm cho hoành tráng luôn, \x%l編成;#00ffc040;ghép%l;#; cả toa phát điện và xe đông lạnh vào——!!」
- **Mới:** 「Đúng vậy. Hay là làm cho hoành tráng luôn, \x%l編成;#00ffc040;ghép%l;#; cả toa phát điện và xe đông lạnh vào——Ư!!」
- **Lý do:** sweep có 1 mục cho file này (key 2579) + 1 mục trùng dưới 09_Grand (cùng dòng, do file có 2 bản TOML) — cùng giá trị; đã kiểm chứng đúng JP (っ cuối sau ―― bị mất hẳn) và áp nguyên.

## §3. Cụm đại từ Soutetsu (99 điểm / 99 dòng)

Quy tắc áp dụng (AUDIT-BRIEF.md + tiền lệ đã merge): độc thoại Soutetsu xưng "Tôi" (không "em"/"anh"/"mình" ở vị trí chủ ngữ); Soutetsu "tôi" với Mayami (chị cả, gọi cậu là 双ちゃん), "anh" với Hibiki/Michiko/Paulette/Reina/Fukami/Nagi; "tôi" với Hachiroku/Minokasa/Kisaki; nhóm "bọn tôi"/"chúng tôi" là dạng trung tính. Kisaki tự xưng "em" với Soutetsu, "tôi" với Paulette.

### 3a. Độc thoại "em"/"anh" → "Tôi" (77 dòng)

| Key | Cũ → Mới (chỗ sửa) |
|---|---|
| 3096 | "báo cho anh" / "anh lại" → "báo cho tôi" / "tôi lại" |
| 3032 | "tiềm thức của anh" / "anh vẫn nghĩ" → "của tôi" / "tôi vẫn nghĩ" |
| 3229 | "Trong mắt anh" → "Trong mắt tôi" |
| 3454 | "anh hoàn toàn" → "tôi hoàn toàn" |
| 3510 | "lúc anh kịp" → "lúc tôi kịp" |
| 3407 | "anh đã hứa" → "tôi đã hứa" |
| 3186 | "Đối với anh" / "Anh cảm thấy" → "Đối với tôi" / "Tôi cảm thấy" |
| 3439 | "Nghe anh nói" → "Nghe tôi nói" |
| 1518 | "em sẽ quên" → "tôi sẽ quên" |
| 3352 | "em tha thiết" → "tôi tha thiết" |
| 3349 | "khuyên em" → "khuyên tôi" |
| 3031 | "em cũng tự kiểm điểm" → "tôi cũng tự kiểm điểm" |
| 3253 | "em hướng ra" → "tôi hướng ra" |
| 3291 | "nên em đi ngang qua" → "nên tôi đi ngang qua" ("em ấy" = Hibiki, giữ nguyên) |
| 3441 | "Nghe em nói" → "Nghe tôi nói" |
| 3266 | "em càng thấy" → "tôi càng thấy" ("em ấy" = Hibiki, giữ nguyên) |
| 3311 | "em bỗng cảm thấy" → "tôi bỗng cảm thấy" |
| 3160 | "yêu cầu em đi cùng" → "yêu cầu tôi đi cùng" ("em ấy" = Hibiki, giữ nguyên) |
| 3273 | "để cho em được nghỉ ngơi" → "để cho tôi được nghỉ ngơi" |
| 3543 | "Em cảm thấy" → "Tôi cảm thấy" |
| 3241 | "lòng em" → "lòng tôi" |
| 3044 | "bọn em vẫn chưa" → "bọn tôi vẫn chưa" |
| 3440 | "em thở phào" → "tôi thở phào" |
| 3450 | "em sẽ lại rơi vào" → "tôi sẽ lại rơi vào" |
| 3134 | "em liền nhận ra" / "bảo vệ em" → "tôi liền nhận ra" / "bảo vệ tôi" |
| 3172 | "tim em đã đập" → "tim tôi đã đập" |
| 3129 | "em đang cảm thấy" → "tôi đang cảm thấy" |
| 3300 | "em vẫn luôn làm" → "tôi vẫn luôn làm" |
| 3265 | "em gần như nghĩ" / "lại cuống cuồng" (chủ ngữ em) → "tôi gần như nghĩ" / "tôi lại cuống cuồng" |
| 3026 | "câu trả lời của em" → "câu trả lời của tôi" |
| 3359 | "nhờ vả em" → "nhờ vả tôi" |
| 3250 | "Em không ngờ" → "Tôi không ngờ" |
| 1463 | "em đã uống cạn" → "tôi đã uống cạn" ("tửu lượng của mình" phản thân, giữ nguyên) |
| 3401 | "em chẳng thốt nên lời" → "tôi chẳng thốt nên lời" |
| 3174 | "em vội vàng uống" → "tôi vội vàng uống" |
| 3246 | "Em đưa ly" → "Tôi đưa ly" |
| 3252 | "của em lại khiến" → "của tôi lại khiến" |
| 3393 | "em đã nói với chị ấy" → "tôi đã nói với chị ấy" ("xưởng nhà mình" của Mayami, giữ nguyên) |
| 3230 | "em uống thêm" → "tôi uống thêm" |
| 3124 | "đến tận tai bọn em" → "đến tận tai bọn tôi" |
| 3138 | "cả em, Hachiroku và Hibiki" → "cả tôi, Hachiroku và Hibiki" |
| 3555 | "bọn em cũng chẳng" → "bọn tôi cũng chẳng" |
| 3281 | "em đang lo lắng" → "tôi đang lo lắng" |
| 1506 | "thân phận của em" → "thân phận của tôi" (+ thuật ngữ Migita Ichi, §2a) |
| 3243 | "em đưa ly" → "tôi đưa ly" |
| 3542 | "chuyên môn của em" / "em đã học được" → "chuyên môn của tôi" / "tôi đã học được" |
| 3272 | "biểu cảm của em" → "biểu cảm của tôi" |
| 3181 | "em vội vàng giải thích" → "tôi vội vàng giải thích" |
| 3402 | "khiến chính em ngạc nhiên" → "khiến chính tôi ngạc nhiên" |
| 1491 | "chúng em đã không" → "chúng tôi đã không" |
| 3235 | "Em chỉ còn biết" → "Tôi chỉ còn biết" |
| 3262 | "em đã từng căm ghét" → "tôi đã từng căm ghét" |
| 1528 | "em vẫn cảm thấy" / "bản thân em ngày xưa" → "tôi vẫn cảm thấy" / "bản thân tôi ngày xưa" |
| 3233 | "em nghĩ về Hibiki" / "chúng em đã thấu hiểu" → "tôi nghĩ về Hibiki" / "chúng tôi đã thấu hiểu" |
| 3176 | "em rất vui" → "tôi rất vui" |
| 3528 | "chúng em đã dày công" → "chúng tôi đã dày công" |
| 3153 | "Em cảm thấy đầu mình" → "Tôi cảm thấy đầu mình" ("đầu mình" phản thân, giữ nguyên) |
| 3041 | "em vẫn không thể" / "em đã hiểu" → "tôi vẫn không thể" / "tôi đã hiểu" ("tại sao mình lại cố chấp" phản thân, giữ nguyên) |
| 3487 | "em vừa thốt lên" → "tôi vừa thốt lên" |
| 3140 | "em vào thẳng kết luận" → "tôi vào thẳng kết luận" |
| 3021 | "cách làm việc của em" / "em phải gật đầu" → "cách làm việc của tôi" / "tôi phải gật đầu" ("em ấy" = Hibiki, giữ nguyên) |
| 3167 | "em chỉ cần làm đường ray" → "tôi chỉ cần làm đường ray" |
| 3236 | "em vạch ra đường ray" → "tôi vạch ra đường ray" |
| 3073 | "em……đã bỏ sót" → "tôi……đã bỏ sót" |
| 3227 | "em đã nghĩ" → "tôi đã nghĩ" |
| 3438 | "với lời em nói" → "với lời tôi nói" |
| 3136 | "em cần phải giải thích" → "tôi cần phải giải thích" |
| 3289 | "dòng suy nghĩ của em" → "dòng suy nghĩ của tôi" |
| 3541 | "em cảm nhận" → "tôi cảm nhận" |
| 3271 | "em tiến lại gần" → "tôi tiến lại gần" |
| 3268 | "Nghe em nói vậy" → "Nghe tôi nói vậy" |
| 3019 | "chạm vào môi em" → "chạm vào môi tôi" |
| 3157 | "những lời em định nói" → "những lời tôi định nói" |
| 3256 | "Em nhìn Hachiroku" → "Tôi nhìn Hachiroku" ("Em ấy" = Hachiroku, giữ nguyên) |
| 3258 | "Em nhìn Paulette" → "Tôi nhìn Paulette" |
| 3260 | "Em nhìn chị Mayami" → "Tôi nhìn chị Mayami" |
| 3154 | "Em đã nhận được điểm đỗ" → "Tôi đã nhận được điểm đỗ" |

Lưu ý: độc thoại trong file KHÔNG có dòng nào dùng "tôi" sẵn (0/179) — toàn bộ 77 dòng trên là lỗi hệ thống, không phải lẫn lộn rải rác. Các "em ấy"/"mình" chỉ người khác hoặc phản thân đã kiểm tra từng dòng và giữ nguyên (3173 "em ấy" = Michiko; 3175/3021/3266/3291 "em ấy" = Hibiki; 3442 lời Miyako + "em ấy" = Miyako; 3571/3158 "em ấy" = Miyako/Fukami; 3144 "trẻ em").

### 3b. Soutetsu thoại với Mayami "em" → "tôi" (17 dòng)

| Key | Cũ → Mới | Người nghe (căn cứ) |
|---|---|---|
| 2324 | "Em được nghỉ" / "em có thể giúp" → "Tôi được nghỉ" / "tôi có thể giúp" | Mayami (2460→2324, gọi "chị") |
| 2641 | "điều em mong muốn" → "điều tôi mong muốn" | Mayami (2340→2641) |
| 2521 | "em rất vui" → "tôi rất vui" | Mayami (2117→2521) |
| 2504 | "Em muốn giúp đỡ" / "em muốn giúp chị Mayami" → "Tôi muốn giúp đỡ" / "tôi muốn giúp chị Mayami" | Mayami |
| 2296 | "em chỉ đơn giản là" → "tôi chỉ đơn giản là" | Mayami (2668→2296) |
| 2073 | "em chỉ đơn giản là" → "tôi chỉ đơn giản là" | Mayami (2180→2073) |
| 2514 | "Như em đã nói" / "điều em hằng mong muốn" → "Như tôi đã nói" / "điều tôi hằng mong muốn" | Mayami |
| 2247 | "em vẫn khó lòng tin được" → "tôi vẫn khó lòng tin được" | Mayami (2239→2247) |
| 1592 | "cảm nhận của em" → "cảm nhận của tôi" | Mayami |
| 2332 | "em đâu có cãi nhau" → "tôi đâu có cãi nhau" | Mayami (2236→2332) |
| 2400 | "cảm nhận của em" → "cảm nhận của tôi" | Mayami ("em ấy" = Miyako, giữ nguyên) |
| 2106 | "kể cho em nghe" → "kể cho tôi nghe" | Mayami |
| 2057 | "em đã luôn trăn trở" → "tôi đã luôn trăn trở" | Mayami (2459→2057) |
| 2757 | "Em cũng sẽ liên lạc" → "Tôi cũng sẽ liên lạc" | Mayami ("em ấy" = Hibiki, giữ nguyên) |
| 2720 | "em vui lắm" / "lòng em vẫn chưa" → "tôi vui lắm" / "lòng tôi vẫn chưa" | Mayami (2033→2720) |
| 2503 | "Em……từ lúc trở về" → "Tôi……từ lúc trở về" (+ Ohitoyo, §2a) | Mayami |
| 2298 | "anh muốn cho" ×2 → "tôi muốn cho" ×2 | Mayami (2721→2298, gọi "chị" trong câu trả lời) |

Căn cứ quy tắc: Mayami gọi Soutetsu là 双ちゃん 366× (chị cả); tiền lệ đã merge "Soutetsu 'em'→'tôi' với Mayami 4 dòng" (file 603 trong ROUTE-AUDIT.md). Mayami gọi Soutetsu là "em" ở 7 dòng trong file này (2466, 2460, 2117, 2815, 2380, 2255, 2805) — chiều ngược lại đúng, không sửa.

### 3c. Các đại từ Soutetsu khác (1 dòng)

| Key | Cũ → Mới | Lý do |
|---|---|---|
| 2859 | "anh dự định sẽ tổ chức kêu gọi ý kiến" → "tôi dự định sẽ tổ chức kêu gọi ý kiến" | Nói với cả cuộc họp (nhóm hỗn hợp) — đại từ số ít "anh" sai đối tượng nhóm; tiền lệ Paulette 14 key 1544 "anh"→"tôi" cho địa chỉ nhóm. |

- Parent kiểm chứng 21/11 ~15:10: LOẠI 2022 ("mình" → "anh", agent cho là thoại với Hibiki). Hàng xóm trong thứ tự truyện (2024 định giá phòng, 2026 Kisaki, 2032 Fukami, 2033 Mayami, 2044 Hachiroku, 2048 Hibiki) cho thấy đây là cuộc họp nhóm, không có căn cứ nào xác định Hibiki là người nghe — khác với 2859 (nhóm → "tôi") cùng cảnh. Theo quy tắc brief ("khi chưa chắc, giữ VN cũ và ghi cờ"), giữ nguyên "mình" và ghi cờ dòng này cho đợt thống nhất; không đổi thành "tôi" vì cũng chưa đủ căn cứ. Fix list 132→131.

Đã kiểm tra và không tính sai: Soutetsu "anh" với Michiko (2052, 2589, 2374, 2370) và với Hibiki (2842) — đúng; "anh" với Paulette (2522, 2519) và với Reina (2663) — đúng; "tôi" với Kisaki (2051) và với nhóm (2351, 2357) — đúng; "em" chỉ Hibiki/Nagi/Reina (2112, 2123, 2105, 2841, 2120, 2663) — đúng người nghe.

### 3d. Kisaki tự xưng "tôi" → "em" khi nói với Soutetsu (4 dòng)

| Key | Cũ → Mới | Người nghe (căn cứ) |
|---|---|---|
| 2706 | "tôi đã cười nhạo" → "em đã cười nhạo" | Soutetsu — phản bác trực tiếp đề xuất của Soutetsu |
| 2102 | "tôi hiểu" → "em hiểu" | Soutetsu — cùng câu gọi thẳng "Soutetsu, cậu đã nghĩ ra…" |
| 2786 | "cứ để tôi" → "cứ để em" | Soutetsu — nhận việc từ Soutetsu (chủ trì họp) |
| 2644 | "Tôi thì lại nghĩ" → "Em thì lại nghĩ" | Soutetsu — đáp trực tiếp 2705 ("Tôi không phản đối tính toán của Kisaki") |

Quy tắc Kisaki (AUDIT-BRIEF.md): tự xưng "em" với Soutetsu, "tôi" với Paulette. Hai dòng "tôi" khác của Kisaki giữ nguyên và ghi ở §6 (địa chỉ nhóm, chưa đủ căn cứ đổi).

## §4. Kiểm tra sweep — 1/1 đúng, 0 bỏ sót

- `sweep-raw-gasp-wrong.json` có **1 mục cho file này (key 2579, lost-gasp-trailing) + 1 mục trùng dưới 09_Grand** (cùng dòng, do file có 2 bản TOML) — cùng giá trị, đã kiểm chứng đúng JP và áp nguyên (§2c).
- Quét độc lập toàn bộ っ trong JP (xem §1): không còn gasp nào bị mất ngoài 2579 — 0 sweep bỏ sót.

## §5. Kiểm chứng

- **Lượt soát 2: 132 tổng / 131 tái xác nhận / 1 loại bỏ / 0 sửa lại.** Đọc lại từng fix đối chiếu JP sau khi viết xong; parent loại 1 fix (2022, xem ghi chú parent ở §3c — người nghe chưa xác định được, giữ VN cũ "mình"). (Lưu ý: trong lúc đọc lần 1 từng suýt giữ nguyên "em" độc thoại vì file dùng nhất quán — đã dừng lại sau khi xác nhận quy ước độc thoại "Tôi" từ tiền lệ Common 14/Grand 01/file 09 và "độc thoại 'Em'→'Tôi'" đã merge.)
- **JSON:** `audit-grand07-mayami-wrong.json` — 131 mục, key dạng string, dạng list-of-dicts chuẩn (key, jp, tw, old_vn, fix, kind, character); jp/tw/old_vn khớp CSV3 tuyệt đối 131/131 (sau khi parent loại 2022).
- **Khối TOML:** 131 khóa, parse bằng tomllib, **0 sai lệch giá trị** so với JSON (sau khi parent loại 2022). (Lưu ý: TOML-2 flatten `\n` thành khoảng trắng nên khối dùng `\\n` cho backslash-n literal; tag `%l` viết `\\x`.)
- **Diff-sanity:** mọi fix chỉ khác VN cũ ở chỗ sửa có chủ đích; 3 dòng tỉ lệ thấp là 2407 (0,81), 2756 (0,84), 3548 (0,83) — thay thuật ngữ/cụm từ theo quyết định đã chốt, không phải viết lại lớn vô căn cứ.

## §6. Ghi nhận chờ đợt thống nhất / chờ Hieu (không tự quyết)

- **正和 (1549):** VN "thời kỳ đầu Showa" — giữ nguyên, CHƯA sửa. 正和 là niên hiệu hư cấu trong game (khác 昭和); toàn dự án đang dùng lẫn "Chiêu Hòa" (ハチロク03: 2176, 2550) và "Showa" (gloss ハチロク12 2015, 日々姫03 2002). Cần Hieu chốt một dạng toàn dự án.
- **Kisaki "tôi" giữ nguyên 2 dòng (địa chỉ nhóm, chưa đủ căn cứ đổi):** 1548 "Ý tôi là" (trình bày ý tưởng trước cả nhóm) và 2257 "tôi sẽ rút lại phương án của mình" (nhượng bộ sau khi Reina/Fukami lên tiếng — người nghe chính là nhóm, không phải riêng Soutetsu). Parent kiểm chứng thêm nếu cần.
- **Giữ nguyên có lý do (không tính sai):** 運転士 gloss "nhân viên cơ vụ" (2276 — tiền lệ 2 file "không tính sai"); 杜氏 gloss "trưởng hầm rượu" (2434 — danh từ chỉ vai trò, khớp TW 掌窖; quy tắc "Toji" đã chốt chỉ áp dụng khi dùng làm cách xưng hô); 2848 余裕 → "không gian" (diễn "room" chấp nhận được, khác 2756); Mayami gọi Hachiroku "Ha-chan" (2290 — biệt danh, giữ nguyên); 2105 lối chơi chữ 餡/案 giữ "(An)" giải thích; 旺宮 → "Omiya" (3458 — theo cách đọc, TW 大宮); 3443/3082 không còn "Đường sắt Hoàng gia" sau khi sửa.
- **"Migitakazu" còn lại toàn dự án:** 15 dòng ở các file khác (vd. lr真闇追加02 ×3) — chờ đợt thống nhất đổi về "Migita Ichi".
- **Sau file này:** 0 "Ohimitera"/"Ohito", 0 "Yui", 0 "Jussen", 0 "Migitakazu", 0 "Đường sắt Hoàng gia", 0 "Denshahime-sama", 0 "Maitetsu" (cho まいてつ) còn trong file này — đợt thống nhất không cần quay lại file này cho các thuật ngữ trên.

## Khối TOML [script] (đã kiểm chứng parse)

```toml
[script]
"1463" = "——Hơn nữa, vì vị ngon hòa quyện ấy, tôi đã uống cạn cả ly.\\nDù tự biết tửu lượng của mình chẳng khá khẩm gì cho cam."
"1491" = "……À không, nhắc mới nhớ, từ nãy đến giờ……\\nCó vẻ như chúng tôi đã không thực sự hiểu ý nhau ở điểm đó——"
"1506" = "……Hoàn toàn không phải là nói dối.\\nVì một phần thân phận của tôi hiện tại vẫn là nhân viên kinh doanh quèn của tiệm rượu Migita Ichi."
"1518" = "……Một điều gì đó, rất quan trọng, đang dần tan biến vào ánh sáng ban mai.\\nChắc chắn, tôi sẽ quên mất giấc mơ này."
"1525" = "……Nếu kế hoạch này tiến triển tốt, các công ty ở Kyushu chắc chắn\\nsẽ đồng loạt chào đón các chủ tàu và đổ xô đi tìm kiếm đầu máy."
"1528" = "……Dù biết chị đang nói về Miyako,\\nnhưng tôi vẫn cảm thấy chút bối rối như thể chị đang nói về chính bản thân tôi ngày xưa vậy."
"1548" = "「『Đường sắt lãng mạn tuyến Yunoi』——\\nÝ tôi là, chỉ cần áp dụng mô hình đó cho tất cả các tuyến đường là được.」"
"1549" = "「『Đường sắt lãng mạn tuyến Yunoi』. Tái hiện lại phong cảnh đường sắt hoài niệm thuở xưa——\\ncủa thời kỳ đầu Showa trên toàn tuyến Yunoi.」"
"1592" = "「……Nếu biết đây là cảm nhận của tôi,\\ncó khi chỉ vì thế mà Miyako sẽ trở nên cố chấp cũng nên.」"
"1594" = "「……Em thì, về các tuyến đường sắt ở Kyushu,\\nhầu như chỉ biết mỗi tuyến Yunoi thôi.」"
"1605" = "「……Hương vị thật trong trẻo làm sao.\\nKhông thể tin được đây lại là loại rượu shochu được sinh ra từ cùng một xưởng với \"Migita Ichi\".」"
"2057" = "「Sự kết nối. Phương tiện để kết nối Kyushu.\\nMột thứ gì đó còn thiếu——tôi đã luôn trăn trở về điều đó.」"
"2073" = "「Tóm lại là, tôi chỉ đơn giản là」"
"2102" = "「Nhưng giờ thì em hiểu. Để biến câu chuyện viển vông đó thành hiện thực——\\nSoutetsu, cậu đã nghĩ ra phương pháp cụ thể rồi đúng không?」"
"2106" = "「Chẳng phải chị đã kể cho tôi nghe sao. Lúc phỏng vấn, Miyako đã nói,\\n『Không bao giờ muốn dính dáng đến đường sắt nữa』.」"
"2120" = "「Người mà em quen biết đó, có muốn đến Đường sắt Ohitoyo không?」"
"2164" = "「Dù đầu máy của em ấy đã bị tháo dỡ……\\nEm ấy vẫn luôn là một cô bé dịu dàng sao.」"
"2247" = "「Dù chị nói vậy nhưng tôi vẫn khó lòng tin được.\\nMột hương vị mang đến cảm giác dịu dàng……thậm chí là ấm áp.」"
"2259" = "「Awa wa wa wa, nếu bé Chikage mà đến Ohitoyo,\\nmà đến đây thì.」"
"2276" = "「À, đền chủ Akai——\\x%l運転士;#00ffc040;nhân viên cơ vụ%l;#; Akai và Niiroku sao.\\nQuả thực, có rất nhiều điều để học hỏi từ bộ đôi đó.」"
"2287" = "「Vâng ạ~. Đây là cửa hàng đường sắt của Đường sắt Ohitoyo nha~」"
"2296" = "「Ừm. Tóm lại là, tôi chỉ đơn giản là——」"
"2298" = "「Ừm. Nếu có thể, ở những đoạn đường đã được điện khí hóa trở lại, tôi muốn cho \\x%l電車;#00ffc040;tàu điện%l;#;\\nkẹp lấy nhóm toa hành khách——tôi muốn cho chạy một \\x%l編成;#00ffc040;đoàn tàu%l;#; như vậy đấy.」"
"2314" = "「Đúng vậy, nếu là Higo thì sẽ dùng đồ gỗ nội thất của Ohitoyo. Chiếu cói của Yatsushiro.\\nGốm sứ của Amakusa. Đèn lồng của Yamaga——chúng ta sẽ trang bị nội thất bằng những thứ đó.」"
"2322" = "「Vâng. Em định đến Jutsu-sen, vẽ lại chiếc xe đang được đưa vào sửa chữa.\\nBiết đâu lúc đó sẽ nảy ra ý tưởng gì đó.」"
"2324" = "「Ừm. Tôi được nghỉ.\\nNếu chị cần gì, tôi có thể giúp cả ngày luôn cũng được.」"
"2332" = "「Hửm? Không, tôi đâu có cãi nhau——」"
"2400" = "「Nếu biết đây là cảm nhận của tôi mà cách đón nhận của em ấy thay đổi.\\nThì mong chị hãy truyền đạt lại đây là cảm nhận của một 『Nhân viên kinh doanh của đại lý rượu』.」"
"2407" = "「Nghe nói nó xuất hiện vào thời kỳ cuối cùng của Teitetsu.\\nĐáng tiếc là Teitetsu đã sụp đổ trước khi nó kịp phát huy tác dụng.」"
"2469" = "「『Thể chế toàn Ohitoyo』 vẫn là chưa đủ——\\nHoàn toàn, chưa đủ.」"
"2482" = "「Cuối cùng thì hiệu quả từ việc Ohitoyo đoàn kết thành một khối cũng đã xuất hiện.\\nĐặc biệt đối với thế hệ trẻ, có lẽ đây là một sự khích lệ rất lớn.」"
"2486" = "「Ga suối nước nóng Ohitoyo cũng cần có một công trình gì đó nhỉ.\\nMột cơ sở vật chất cho thấy đây là ga xuất phát của Nine Stars.」"
"2503" = "「Tôi……từ lúc trở về Ohitoyo đến giờ, chưa một lần nào,\\nthực sự giúp đỡ chị được một việc cho ra hồn cả.」"
"2504" = "「Tôi muốn giúp đỡ trong quá trình, chứ không phải ở kết quả.\\nMột cách trực tiếp hơn, cụ thể hơn. Bằng chính đôi tay này, tôi muốn giúp chị Mayami.」"
"2514" = "「Như tôi đã nói lúc nãy——\\nĐó chính là điều tôi hằng mong muốn.」"
"2521" = "「Nếu được vậy thì tôi rất vui, nhưng——\\nDù sự thật là thế, thì vẫn không phải vậy.」"
"2559" = "「Hình như Hibiki——à đúng rồi, em ấy bảo sẽ đến Jutsu-sen.」"
"2579" = "「Đúng vậy. Hay là làm cho hoành tráng luôn,\\n\\x%l編成;#00ffc040;ghép%l;#; cả toa phát điện và xe đông lạnh vào——Ư!!」"
"2611" = "「Có một chiếc D51 tơi tả, nhưng nếu là Jutsu-sen hiện tại thì có thể sửa được.\\nVà……về \\x%lレイルロオド;#00ffc040;Railord%l;#;, em cũng có quen biết một người.」"
"2641" = "「Đó chính là điều tôi mong muốn.\\n——A.」"
"2644" = "「Tại sao chứ?\\nEm thì lại nghĩ đây chính là giải pháp tối ưu đấy?」"
"2664" = "「Chính là sự đoàn kết của Thể chế toàn Ohitoyo, Thể chế toàn tuyến Yunoi\\nmà hiện tại chúng ta đang cảm nhận rõ sức mạnh của nó. Chúng ta sẽ mở rộng điều đó ra toàn bộ Kyushu.」"
"2671" = "「Là 『Vì mục đích đó』 mà. Ừm. Em nghĩ là có khả năng đấy.\\nChắc chắn cô ấy sẽ muốn làm việc ở Đường sắt Ohitoyo.」"
"2706" = "「Chỉ là lý thuyết suông. Thật nực cười. Nếu làm được thế thì đã chẳng phải khổ.\\n——Nếu là trước khi quen biết Soutetsu, em đã cười nhạo như vậy rồi.」"
"2720" = "「Nghe chị nói vậy tôi vui lắm.\\nNhưng mà, như thế thì lòng tôi vẫn chưa...」"
"2728" = "「Một hương vị hoàn toàn khác biệt so với sự sâu sắc phức tạp của Migita Ichi,\\nmang hơi hướng hiện đại——nhưng lại là một loại rượu thực sự rất ngon.」"
"2756" = "「Sự tham gia của chú Akai đã mang lại sự dư dả lớn trên mọi mặt.\\nTuy nhiên——vẫn còn thiếu nhân lực, tiền bạc, thiếu đủ thứ.」"
"2757" = "「Chị gọi bảo em ấy đến cửa hàng đường sắt hội quân nhé.\\nTôi cũng sẽ liên lạc với mọi người.」"
"2786" = "「Chuyện đó, cứ để em.\\nHay nói đúng hơn là, hãy giao cho Đường sắt Hinomoto.」"
"2815" = "「Đúng vậy thật. Nghe em nói mới thấy, loại rượu không kén người uống và vị sắc sảo này.\\nCó khi lại được ưa chuộng ở những nơi khác hơn là Ohitoyo cũng nên.」"
"2830" = "「Hoan nghênh quá đi chứ. Khách hàng có thể thưởng thức những loại rượu shochu, rượu sake hảo hạng của khắp các vùng Kyushu ngay trong khoang hành khách.——Hoặc, nếu có thể thì phục vụ ở quầy buffet.」"
"2848" = "「Vậy thì, chúng ta sẽ bàn bạc với phía Jutsu-sen theo hướng đó.\\nNếu có thể, chúng ta sẽ càng có thêm nhiều không gian hơn.」"
"2859" = "「Những món đồ muốn đặt trong khoang hành khách, hay ý tưởng thống nhất cho từng khoang,\\ntôi dự định sẽ tổ chức kêu gọi ý kiến từ chính người dân ở các khu vực đó.」"
"3019" = "Chỉ trong một khoảnh khắc, còn nhẹ hơn cả cánh bướm,\\nđầu ngón tay của chị Mayami chạm vào môi tôi, rồi rời ra."
"3021" = "Quả nhiên Hibiki rất hiểu cách làm việc của tôi.\\nChẳng cần tôi phải gật đầu, em ấy đã tự mình suy nghĩ."
"3026" = "Dù là dùng từ giúp đỡ,\\nhay là dùng từ báo đáp, thì câu trả lời của tôi vẫn không hề thay đổi."
"3031" = "Và đồng thời, tôi cũng tự kiểm điểm lại bản thân mình thường ngày."
"3032" = "Hoặc nếu tất cả những điều này chỉ đơn thuần là hoạt động trong tiềm thức của tôi.\\nThì có lẽ ở đâu đó, tôi vẫn nghĩ rằng 『Như vậy vẫn chưa đủ』 chăng——"
"3041" = "Nhưng dù vậy tôi vẫn không thể gật đầu đồng ý——\\nGiờ thì tôi đã hiểu lý do tại sao mình lại cố chấp xin mọi người chờ thêm một chút nữa."
"3044" = "Thế nhưng hình dáng, cái hình dáng lý tưởng ấy,\\nbọn tôi vẫn chưa thể nào phác họa ra được."
"3073" = "Hachiroku cất giọng trầm buồn.\\nNói cách khác là tôi……đã bỏ sót điều gì đó sao."
"3082" = "\\x%lレイルロオド;#00ffc040;Railord%l;#; của \\x%l蒸気機関車;#00ffc040;đầu máy hơi nước%l;#; dòng \\x%l9600;#00ffc040;9600%l;#; Teitetsu cũ, số hiệu 39685,\\n\"Miyako\"."
"3096" = "Chỉ có âm thanh này là luôn chân thực.\\nNó báo cho tôi biết rằng, tôi lại một lần nữa, trở về trong giấc mơ của Michiko."
"3124" = "Mặc dù tiếng kêu gào phản đối tháo dỡ tuyệt vọng của Miyako\\nđã vọng đến tận Kyushu xa xôi, đến tận tai bọn tôi."
"3129" = "À——ra là vậy.\\nNói tóm lại là……tôi đang cảm thấy xấu hổ sao."
"3134" = "Vừa trả lời xong, tôi liền nhận ra điều đó.\\nChị Mayami lúc nào cũng bảo vệ tôi, vậy mà——"
"3136" = "Nên tôi cần phải giải thích cho chị Mayami hiểu từ điểm đó."
"3138" = "Thế nên cả tôi, Hachiroku và Hibiki,\\nhầu như chưa bao giờ tiếp xúc với Miyako."
"3140" = "Thế nên, tôi vào thẳng kết luận mà không cần rào trước đón sau.\\nNhưng phản ứng của mọi người lại không được như mong đợi."
"3153" = "Tôi cảm thấy đầu mình đang nóng lên.\\nKhông phải vì hưng phấn——mà là não bộ đang hoạt động hết công suất."
"3154" = "Tôi đã nhận được điểm đỗ.\\nNếu vậy thì chẳng có lý do gì phải do dự nữa."
"3157" = "Chỉ vậy thôi cũng đủ chặn đứng những lời tôi định nói."
"3160" = "Không hề yêu cầu tôi đi cùng,\\nem ấy khẳng định chắc nịch rằng \"sẽ đi vẽ\"."
"3164" = "Em ấy gật đầu mạnh mẽ.\\n——Không một ai có ý kiến phản đối."
"3167" = "Thật đáng mừng biết bao. Thật vững tâm biết bao.\\nNếu được thế này, à——tôi chỉ cần làm đường ray là đủ rồi."
"3172" = "Chỉ bị hỏi lại thôi mà tim tôi đã đập thình thịch.\\nHai má——rồi cả khuôn mặt nóng bừng lên."
"3174" = "Nghe vậy, tôi vội vàng uống thêm một ngụm nữa.\\n……Nếu đúng là vậy, thì hương vị này cũng dễ hiểu thôi, nhưng——."
"3176" = "Nếu vậy thì, tôi rất vui."
"3181" = "Cảm thấy như đã làm chị Mayami lo lắng,\\ntôi vội vàng giải thích lý do."
"3185" = "Ra là vậy, vì chị ấy ít liên quan đến Đường sắt Ohitoyo——\\nhay nói đúng hơn là ít liên quan đến đường sắt nói chung."
"3186" = "Đối với tôi, việc đó có chút gì đó như là sự áy náy……\\nTôi cảm thấy một sự phản kháng vô hình trong tâm lý——"
"3227" = "Độ bền của đường ray——về tải trọng chịu đựng,\\ntôi đã nghĩ là cần phải xem xét, nhưng——"
"3229" = "Trong mắt tôi chẳng phản chiếu thứ gì cả——\\nNgoài khung cửa sổ kia, dường như chỉ có một màu xám xịt đang chồng chất lên nhau."
"3230" = "Nhẩm lại điều đó một lần nữa, tôi uống thêm một ngụm."
"3233" = "Và rồi, tôi nghĩ về Hibiki thuở nhỏ.\\nRa là vậy, có lẽ chúng tôi đã thấu hiểu nhau ở điểm đó."
"3235" = "Tôi chỉ còn biết gật đầu."
"3236" = "Chỉ cần tôi vạch ra đường ray, thì \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, tín hiệu, vận hành, chỉ huy.\\nMỗi người đều sẽ hoàn thành xuất sắc nhiệm vụ của mình."
"3241" = "Khi cảm nhận được sự tuyệt vời đó,\\nlòng tôi lại càng thêm kiên định và mạnh mẽ."
"3243" = "Được chị Mayami ra hiệu bằng mắt, tôi đưa ly cho chị.\\nChị Mayami cũng một hơi cạn sạch ly shochu đó."
"3246" = "Tôi đưa ly cho chị, nhờ chị rót thêm một ly nữa."
"3250" = "Tôi không ngờ việc báo đáp chị Mayami lại là uống rượu vào buổi sáng.\\nNhưng hôm nay là ngày nghỉ. Có say xỉn đến đâu cũng chẳng sao."
"3252" = "Lời lỡ buột miệng của tôi lại khiến chị Mayami lộ vẻ ngạc nhiên pha chút ngán ngẩm."
"3253" = "Gấp chăn đệm, thay quần áo xong xuôi,\\ntôi hướng ra phòng khách——thì."
"3256" = "Tôi nhìn Hachiroku.\\nEm ấy lộ vẻ ngạc nhiên——rồi từ từ, thận trọng gật đầu đáp lại."
"3258" = "Tôi nhìn Paulette.\\nCô ấy đang làm vẻ mặt có vẻ bối rối."
"3260" = "Tôi nhìn chị Mayami.\\nChị Mayami gật đầu thật mạnh, thật mạnh."
"3262" = "Đúng là tôi đã từng căm ghét đường sắt,\\nvà khao khát được tránh xa nó——từ tận đáy lòng."
"3265" = "Đáng yêu quá——tôi gần như nghĩ vậy theo phản xạ,\\nrồi chẳng hiểu sao lại cuống cuồng cả lên."
"3266" = "Càng nghe em ấy nói, tôi càng thấy đúng là vậy,\\nnên trước mắt cứ dùng bánh nướng dài để khóa miệng Hibiki lại đã."
"3268" = "Nghe tôi nói vậy, chị Mayami bật cười \"Aha\".\\nMột nụ cười nhẹ nhàng, như thể chuyện đó buồn cười lắm vậy."
"3271" = "Trong một góc phòng, tôi tiến lại gần chị Mayami đang đứng lặng lẽ một mình."
"3272" = "Chắc hẳn biểu cảm của tôi đã lộ rõ trên khuôn mặt."
"3273" = "Có lẽ là để cho tôi được nghỉ ngơi——\\nHibiki một mình nhanh chóng chuẩn bị đồ đạc."
"3281" = "Thế nên có lẽ……\\nchỉ là tôi đang lo lắng thái quá thôi."
"3289" = "Tiếp sức.\\nChỉ một từ đó thôi đã tiếp sức cho dòng suy nghĩ của tôi."
"3291" = "Thấy bỏ mặc em ấy thì cũng tội nghiệp,\\nnên tôi đi ngang qua Hibiki đang rên rỉ, tiến vào bếp——"
"3300" = "Một khi đã nhận thức được cảm xúc, thì có thể kiểm soát được nó.\\nTừ trước đến nay tôi vẫn luôn làm như vậy mà."
"3311" = "Từ bao giờ, Hibiki cũng đã trưởng thành như vậy rồi,\\ntôi bỗng cảm thấy có chút chói lọi."
"3349" = "Lòng biết ơn trào dâng\\ntrước việc Paulette đã nhiều lần khuyên tôi nên nghỉ ngơi."
"3352" = "Vì biết như vậy, nên tôi tha thiết cầu nguyện.\\nMong sao những gì đã tan biến, dù chỉ là một mảnh vỡ nhỏ nhoi——"
"3359" = "Dù sao thì cũng là chị Mayami đang nhờ vả tôi mà."
"3393" = "Khi biết điều đó, chị Mayami đã nói 『Nếu vậy thì hãy để xưởng nhà mình tiếp nhận』,\\nvà đó là điều đầu tiên tôi đã nói với chị ấy."
"3401" = "Chị Mayami cười vui vẻ.\\nÁnh mắt chạm nhau——bỗng dưng tôi chẳng thốt nên lời nào nữa."
"3402" = "Chị Mayami tròn xoe mắt ngơ ngác.\\nViệc làm chị ấy ngạc nhiên lại khiến chính tôi ngạc nhiên."
"3407" = "Đúng là tôi đã hứa với Hibiki rằng,\\nlần tới nhất định sẽ đi cùng nhau. Nhưng……"
"3426" = "Việc rút lại quyết định mời gọi nhà máy Aircra đã được xác định, người dân Ohitoyo\\nvà các chính quyền địa phương dọc tuyến đường cũng đang dần đoàn kết lại dưới ý tưởng đó."
"3438" = "Mọi người đều gật đầu đồng tình với lời tôi nói.\\nChỉ có một người duy nhất——ngoại trừ chị Mayami."
"3439" = "Nghe tôi nói vậy,\\nlần này đến lượt Michiko ngẩn tò te, lộ vẻ khó hiểu."
"3440" = "Nghe tiếng gọi, tôi thở phào nhẹ nhõm."
"3441" = "Nghe tôi nói vậy, Hibiki lại bẹp một cái,\\ngục mặt xuống bàn."
"3443" = "Được gửi gắm toàn bộ hy vọng phục hưng Teitetsu,\\n\\x%l電車;#00ffc040;tàu điện%l;#; tốc hành tối tân nhất——nguyên mẫu \\x%lクハ26;#00ffc040;Kuha 26%l;#;, \\x%l編成;#00ffc040;đoàn tàu%l;#; \\x%lクハ26;#00ffc040;Kuha 26%l;#;-000."
"3450" = "Vì nếu cứ để mặc như vậy, chắc chắn tôi sẽ lại rơi vào\\ncái vòng luẩn quẩn không lối thoát như mọi khi."
"3454" = "Ý nghĩa của việc được giao phó chạy thử nghiệm con tàu đó,\\ntôi hoàn toàn——hoàn toàn không hiểu được."
"3487" = "Ngay khi tôi vừa thốt lên, chị Mayami liền gật đầu."
"3510" = "Nhanh hơn một chút so với lúc tôi kịp đưa ra suy luận,\\nMichiko đã nói ra câu trả lời."
"3528" = "Nếu những thành quả mà chúng tôi đã dày công vun đắp,\\ncó thể xoa dịu và mang lại niềm vui cho trái tim của Miyako."
"3541" = "Tất nhiên, việc kiểm tra kỹ lưỡng sẽ được tiến hành sau——\\nNhưng tôi cảm nhận ngày càng rõ rệt rằng: Cách này chắc chắn thành công."
"3542" = "Quảng cáo tuyên truyền không phải chuyên môn của tôi,\\nnhưng trong quá trình kiêm nhiệm công việc kinh doanh cùng Hibiki, tôi đã học được rất nhiều điều."
"3543" = "Tôi cảm thấy có chút cô đơn, nhưng niềm vui thì lại lớn hơn gấp bội."
"3548" = "Liệu mối quan hệ của Công chúa Tàu điện có giúp được gì không nhỉ——\\nHửm?"
"3555" = "Thứ nhất, bọn tôi cũng chẳng có mấy điểm chung."
```

## Kết bài

Audit xong file `グランドリライト07_真闇.txt.toml`: **530 dòng đã đọc, 131 dòng sai (24,7%), 134 điểm sửa**. Lỗi tập trung gần hết vào cụm đại từ Soutetsu (99/134 điểm) — file dùng nhất quán kiểu anh/em trong độc thoại và thoại với Mayami, trái quy tắc dự án đã chốt (độc thoại "Tôi"; Soutetsu "tôi" với Mayami; Kisaki "em" với Soutetsu). Ngoài ra: thuật ngữ 30 điểm (御一夜 13 dòng → Ohitoyo; 湯医 4 → Yunoi; 術仙 4 → Jutsu-sen; 帝鉄 3 → Teitetsu; 右田一 3 → Migita Ichi; 電車姫 1 → Công chúa Tàu điện; まいてつ 1 → chủ tàu; 宮司 1 → đền chủ); sai nghĩa 4 (2756 余裕, 2164 chủ thể, 3164 chủ ngữ theo TW, 2830 sake→rượu vang); gasp 1 (2579, sweep áp nguyên). Không có lệch dòng, chuỗi xoay, nhiễm chéo, mồ côi, chưa dịch hay trùng khóa; CSV3 1 set duy nhất, VN khớp TOML tuyệt đối; 2 bản TOML md5 giống nhau. Cờ chờ Hieu: 正和 "Showa" (1549) chưa chốt toàn dự án; Kisaki "tôi" 2 dòng địa chỉ nhóm (1548, 2257) giữ nguyên chờ kiểm chứng. Lượt soát 2: 132/131, 1 bỏ (2022, parent loại — người nghe chưa xác định), 0 sửa. Khối TOML 131 khóa parse đúng, 0 sai lệch. Deliverables: `audit-grand07-mayami-REVIEW.md` (file này), `audit-grand07-mayami-wrong.json` (131 mục), `route-audit-snippet-grand07-mayami.md`.
