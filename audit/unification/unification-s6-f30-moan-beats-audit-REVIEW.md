# Unification U10b — §6 F30: moan-beats-audit restorations/cancellations — REVIEW

Đợt U10b / §6 F30 (mục mở 22/11, quyết theo uỷ quyền Hieu khi cần): các dòng mà vòng **moan thắng vòng audit** (hoặc fix audit bị **HUỶ**, khôi phục giá trị trước audit). **105 dòng đã xét: 12 dòng SỬA, 93 dòng GIỮ có lý do.** 4 file / 12 key trong JSON. 1 mục mới (F30), 11 dòng mới + 1 dòng GHÉP (mikuro 1716 với U11a).

## 1. Phạm vi

F30 liệt kê: fukamih1 14, lr-fukamih1 22+9+2, lr-mikuro 23, lr-fukamih1 fa/fu (trùng 21 dòng trong 22 — đếm 1 lần), hachirokuh6 4, hachirokuh7 2, hachirokuh4 882/884, nagih1 1091, hachirokuh2 1433/1598, hachirokuh5 1555/1619, hachirokuh9 963, nagifukamih1 2075/2082, hachirokuh1 1003, hibikih1 1294, gasp-Ư 5, hibikih5 1153, lr-reina 1085, 1967, 1708, 1196, 1095, 970, lr-hachirokuh1 1234, 5 dòng 933/1358/1406/1423/1475, và 1 dòng OPEN ハチロクh8 878 (quyết trong đợt này, xem §6).

## 2. Nhãn file trong list SAI — bảng hiệu chỉnh (key đáng tin, nhãn file không)

Nhãn file của F30 sai có hệ thống. File thật xác định bằng khớp giá trị với audit/moan/CSV3 + `moans/ROUTE-MOANS.md`:

| Nhãn trong list F30 | File thật (basename đầy đủ) |
|---|---|
| ふかみh1 14 | ポーレットh8_気動車の国のアリス.txt.toml (2132, 2137, 2139, 2142, 2185, 2187, 2241, 2279, 2286, 2304, 2340, 2365, 2376, 2413) |
| ハチロクh6 HUỶ 4 (768/800/818/869) | ポーレットh6_あなたとふたりの学園エッチ.txt.toml |
| ハチロクh7 HUỶ 2 (932/947) | ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml |
| ハチロクh4 882/884 | ポーレットh4_クリーム＆クリーム.txt.toml |
| ハチロクh2 1433/1598 | lr_真闇h1_僕のおねえちゃん.txt.toml |
| ハチロクh5 1555/1619 | lr_日々姫真闇h1_三人家族.txt.toml |
| ハチロクh9 963 | ポーレットh2_制服変更？.txt.toml |
| 凪ふかみh1 2075/2082 | 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml |
| ハチロクh1 1003 "Khà"→"Kua" | ポーレットh2_制服変更？.txt.toml (ハチロクh1 không có key 1003) |
| 日々姫h1 1294 | 凪ふかみh2_みずあそび.txt.toml (日々姫h1 không có key 1294) |
| lrれいな追加h 1085 19a | lr_ふかみh2_セックスの意味.txt.toml |
| 1095 | れいなh2_おもらし防止大作戦.txt.toml (JP 「うむ」, CSV3 "Ừm.", không có fix nào) |
| gasp-Ư 5 (952/985/1004/1135/950) | đều ở ポーレットh2 |
| 5 dòng 933/1358/1406/1423/1475 | đều ở lr_日々姫ふかみh1_凪ちゃんの代わり.txt.toml |
| 1708 (16u) | lr_稀咲h1 (khác với 1708 của lr追加_みくろ trong danh sách 23) |
| 1967 | lr_ふかみh1 1967 (audit == moan) |

**Cờ F1 cho coordinator:** list F30 cần hiệu chỉnh nhãn file theo bảng trên để các đợt sau không đuổi nhầm file.

## 3. Phương pháp

- Map xây từ: CSV3 good set 87.833 dòng (bỏ 3.898 dòng stale của 10 file dual-set), audit 9.140 mục, moan 1.516 mục, unification đã gộp **20 file** (18 file lúc spawn + U11b §3 M3 và U8 §2/§6 gộp trong lúc chạy — xem §6), **2.354 key duy nhất**.
- Thứ tự ưu tiên giá trị hiện tại (old_vn): unification đã gộp (theo thứ tự gộp) > moan > audit > CSV3 VN.
- Mọi fix đều đọc tay từng dòng JP (+TW); JP thắng TW; không bịa phần hoàn thiện cho JP cụt; không đụng dòng gasp-Ư hay "Kh" trừ khi F30 nói rõ.
- Đếm nguyên âm kiểm chứng bằng máy từ JP thật của CSV3 (không gõ tay): 768: 10u; 2132: 15a; 1433: 2u; 1555: 4u (theo token); 1619: 7a tổng; 963: 10u; 2075: 6u (theo token); 1708 (lr_稀咲h1): 16u; 1085: 19a; 1153: 9a; 1358: 14u/2n; 1731: 7a. Lưu ý: đếm theo token — đếm cả chuỗi sẽ lẫn 'u'/'a' trong token khác (vd. "Fua" có 'u').
- Kiểm tra đầy đủ: audit fa/fu ở lr_ふかみh1: 14 dòng, tất cả đều có mục moan (không còn dòng audit-only). ポーレットh8: 12 dòng audit fa/fu; audit-only 2161/2224 đã trong unification, 2505/2817 là false positive ("pha trà", không phải token rên). lr追加_みくろ: 35 dòng audit fa/fu; 4 dòng ngoài danh sách 23 đã kiểm tra — 1703/1707/1925/2322 đều là hơi thở ngắn ふっ/ふぅ ("Phù"/"phu" đúng quy ước file, không phải ふぁ/ふあ/ふぇ/ぷあ) — không phải ứng viên huỷ, chỉ ghi chú.

## 4. 12 dòng SỬA (kind="moan", item="F30")

### 4.1. lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml — 5 dòng (huỷ fix audit, khôi phục CSV3)

**1708** — JP 「ふえっ！？　またっ──みくろっ！　またっ！\nだって！　ぼっきっ！　だってっ！　だってぇっ！！」; TW 「呼哎？！又來了——美玖路又要洩了！因為！肉棒！真的！非常舒服！！」; old_vn (audit) 「Phuê!? Lại nữa── Mikuro! Lại nữa!\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」; **fix = CSV3 「Fue!? Lại nữa── Mikuro! Lại nữa!\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」**. Lý do: ふえ là token rên, moan review §5 xác nhận huỷ "phuê" → romaji; CSV3 đã đúng "Fue" (đầu dòng, viết hoa).

**1716 — GHÉP với U11a** — JP 「ふあっ──あっ──すごっ──ふえっ！！？\nや、みくろ──ごめんっ、制服──私、汚してっっ」; TW 「呼啊——啊——天啊——哎？！！呀，美玖路，對不起，你的制服被我弄髒了」; old_vn = fix U11a 「Fua── a── tuyệt quá── phuê!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」; **fix = CSV3 toàn dòng, token romaji viết hoa theo quyết F5 (coordinator) 「Fua── a── tuyệt quá── Fue!!?\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」**. Chỉ token ふえ khác nhau; U11a đã khôi phục token ふあ ("Fua") nhưng để sót "phuê". Dòng này đã tính ở U11a nên **không cộng lại vào tổng** (xem snippet).

**1758** — JP 「ひゅあっ！？　あ──あ……ふえっ！？」; TW 「咿呀？！啊——啊……呼哎？！」; old_vn (audit) 「Hyua!? A── a…… phuê!?」; **fix = CSV3, viết hoa token romaji theo quyết F5 (coordinator) 「Hyua!? A── a…… Fue!?」**. Lý do: ふえ cuối dòng sau khoảng lặng → romaji "fue" (CSV3 viết thường vì không phải đầu dòng).

**1811** — JP 「あ……ん──ちゅっ──ちゅむっ──ちゅっ──ふ\n……ん……れるっ──れりゅっ──れろおおっ──ぷあ」; TW 「啊……嗯——啾——啾唔——啾——呼……嗯……咧溜——滋溜溜——噗啊」; old_vn (audit) 「A……ưm──chụt──chụt──chụt──fu\n……ưm……liếm──liếm──liếmmm──pùa」; **fix = CSV3, viết hoa token romaji theo quyết F5 (coordinator) 「A……ưm──chụt──chụt──chụt──fu\n……ưm……liếm──liếm──liếmmm──Pua」** (chỉ token cuối ぷあ đổi "pùa" → "pua").

**1901** — JP 「ぷあっ──ふふっ、だって。みくろ」; TW 「噗啊——呵呵，阿哥是這麼說的哦。美玖路」; old_vn (audit) 「Pùa──fufu, anh ấy bảo thế kìa. Mikuro.」; **fix = CSV3 「Pua──fufu, anh ấy bảo thế kìa. Mikuro.」**. Lý do: ぷあ đầu dòng → romaji "Pua".

Lưu ý chữ hoa/thường (cờ F5): CSV3 viết "fue"/"pua" thường ở giữa/cuối dòng (1716/1758/1811), trong khi M16 của U11a viết hoa token romaji ("Fue"/"Pua") ở cùng file. 1708/1901 đã viết hoa trong CSV3 (đầu dòng) nên không có vấn đề. QUYẾT bởi coordinator 22/11 ~12:50 (F5): CHUẨN HOÁ — token romaji SFX viết hoa MỌI VỊ TRÍ (đầu dòng và giữa dòng). Bằng chứng: M16 của U11a viết hoa 18/18 dòng mikuro kể cả giữa dòng; vòng moan nghiêng về viết hoa sau ── (10 vs 2); cùng file mikuro không thể vừa "Fua" hoa (U11a) vừa "fue"/"pua" thường (CSV3) cho cùng họ token; chữ thường của CSV3 là thói quen sentence-case của Gemini, không phải quyết định. 3 fix U10b đã sửa theo quyết này (1716/1758 "Fue", 1811 "Pua"); 2 dòng "fua" thường cuối câu ở lr_ニイロクh (1322/1387) đưa vào U15 để chuẩn hoá cùng.

### 4.2. ポーレットh6_あなたとふたりの学園エッチ.txt.toml — 4 dòng (huỷ fix audit, khôi phục CSV3)

**768** — JP 「きゅぅぅぅぅぅぅぅぅぅん！！！」 (9ぅ → 10u, kiểm chứng bằng máy); TW 「呀啊啊啊！！！」; old_vn (audit) 「Kíuuuuuuuuun!!!」; **fix = CSV3 「Kyuuuuuuuuuun!!!」**. Lý do: audit sai vần ("Kíu" thay vì "Kyu"); moan review xác nhận huỷ.

**800** — JP 「くぁ――あっ――」; TW 「唔——啊——」; old_vn (audit) 「Ư a——a——」; **fix = CSV3 「Kua——a——」**. Lý do: くぁ là "Kua" (romaji), audit diễn thành "Ư a" làm mất âm.

**818** — JP 「くあっ！！！」; TW 「啊！！！」; old_vn (audit) 「Ư a!!!」; **fix = CSV3 「Kua!!!」**. Lý do như 800.

**869** — JP 「んきゅんっ！」; TW 「嗯啊！」; old_vn (audit) 「Ưm!」; **fix = CSV3 「Nkyun!」**. Lý do: んきゅん là "Nkyun" (romaji), audit rút gọn thành "Ưm!" làm mất âm.

### 4.3. ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml — 2 dòng (huỷ fix audit, khôi phục CSV3)

**932** — JP 「くあっ！」; TW 「啊！」; old_vn (audit) 「Ư a!」; **fix = CSV3 「Kua!」**. Lý do như 818 (moan review: "2 fix audit bị HUỶ... 932 ('Kua!'), 947 ('Nkyun!!!!')").

**947** — JP 「んきゅんっ！！！！」; TW 「嗯呀！！！！」; old_vn (audit) 「Ưm!!!!」; **fix = CSV3 「Nkyun!!!!」**. Lý do như 869.

### 4.4. ハチロクh8_桜色のひめごと.txt.toml — 1 dòng (OPEN, quyết trong đợt này)

**878 — QUYẾT: khôi phục "ưm!"** (per delegation Hieu). JP 「すずは、全部を――双鉄、さま――にっ――んっ！\n染めて――作り変えて――いただき、たい――ですっ！」 (người nói ハチロク/Suzu, giữa H-scene; dòng trước 876 là câu nói rõ ràng của Soutetsu); TW 「我，的全部——都是您的——嗯——！讓我——染上您的色彩——變成您的模樣吧——！」; old_vn (audit) 「Suzu muốn, tất cả——Ngài Soutetsu——!\nNhuốm màu——tạo hình lại——cho em——!」; **fix = CSV3 「Suzu muốn, tất cả——Ngài Soutetsu——ưm!\nNhuốm màu——tạo hình lại——cho em——!」**. Bằng chứng: んっ là mora hơi thở riêng biệt (không thuộc にっ), TW 嗯 xác nhận "ưm"; audit tự ghi lý do bỏ "ưm" theo tiền lệ "tiểu từ + っ thì bỏ, không diễn thành tiếng rên" nhưng mời xem lại ("nếu muốn giữ tiếng rên ngắt câu thì nói lại" — audit-hachirokuh8 REVIEW dòng 549). Bỏ nó là mất âm. Quyết: giữ "ưm!".

## 5. 93 dòng GIỮ (giá trị hiện tại đã bằng đích F30)

- **ポーレットh8 — 14 dòng GIỮ** (giá trị hiện tại = moan). 2132 đếm 15a đã kiểm chứng (JP ひゅあ+14ぁ; audit cũng 15a, moan chỉ đổi Híu→Hyu). Cờ: **2241** — くっ → "Hự" trong moan, M7 của U12a ("Ku") không áp vào dòng này (cờ F2: M7 có bao phủ không?); **2185** — cả dòng chỉ là ふえっ！？ độc lập + TW 哎, các dòng kề 2183/2184/2187 đều là Paulette ngạc nhiên — ứng viên M10 thứ 6, M10 đã gộp không đụng tới (cờ F3; theo quy tắc đợt này: moan đúng thì GIỮ + cắm cờ, không tự mở rộng M10).
- **lr_ふかみh1 — 33 dòng GIỮ** (22 diff + 9 apply-audit + 2 mới; giá trị hiện tại = moan). 1469 đã GHÉP bởi U12a M7 (moan "hự"→"Ku", "Fa" giữ). 1432 "aa!!" đã kiểm chứng (JP ぁあっ). 1967 audit==moan '(Gichuchu! Kyuu! Kyuun!!)' (CSV3 'Kyu!' sai số lượng, audit sửa, moan đồng ý). Nhóm "HUỶ fa/fu lr_ふかみh1" trong list trùng với 21 dòng trong 22 — đếm 1 lần.
- **lr追加_みくろ — 18/23 dòng GIỮ**: romaji đã khôi phục bởi U11a M16 dạng strict (vd. 1678 "Fua" vs CSV3 thường "fua" — M16 quyết chữ hoa) hoặc giống hệt CSV3. 1731 đếm 7a đã kiểm chứng (CSV3 == unif "Fuyaaaaaaan"). 1857 đúng y như moan review §5 (Fua + giữ "vào hết" của audit — chỉ huỷ một phần "Phùa").
- **ポーレットh4 882/884 GIỮ**: giá trị hiện tại = moan = CSV3 ("Kyafua!?" / "Nkyu!!" — khôi phục no-op).
- **凪h1 1091 GIỮ**: giá trị hiện tại = moan = CSV3 "Hể? ——A! A, em hiểu rồi á" (cũng khớp M10 đã gộp).
- **lr_真闇h1 1433/1598 GIỮ**: 1433 "Fuu" (2u đã kiểm chứng; CSV3 4u sai, audit "Foo" sai vần); 1598 "ha——" khôi phục từ JP はっ (moan giữ "Tôi"/"Ư" của audit).
- **lr_日々姫真闇h1 1555/1619 GIỮ**: 1555 token 4u đã kiểm chứng (JP んウゥゥぅ; cả chuỗi đếm 5u vì "Fua" có 'u'); 1619 tổng 7a đã kiểm chứng từ JP thật CSV3 『あーーーーーーん』 = あ+6ー (MOA A+6a+n = 7 tổng, AUD A+7a+n = 8).
- **ポーレットh2 — 7 dòng GIỮ**: 950 (moan giữ Ư của audit, gộp "Hyaun"), 952/985/1004/1135 (giá trị hiện tại = gasp-Ư của audit: 「Ư!」, 「Á——Ư!」, 「ƯƯ!!?」, 「~~~~~~~~Ư!!!」), 963 (10u đã kiểm chứng: JP あふ+9う; CSV3 11u, audit 9u), 1003 (giá trị hiện tại = moan "Kua!", CSV3 "Khà!" — くあ diễn sai, không phải "Kh" khoá cho っ).
- **日々姫h6 2075/2082 GIỮ**: 2075 token 6u đã kiểm chứng (JP きゃふ+5う); 2082 "Ya" cho やっ giữa chuỗi (moan-only, không có mục audit).
- **日々姫h1 970 GIỮ**: moan "Au" cho あうっ + giữ nghĩa audit "Vào trong tử cung".
- **凪ふかみh2 1294 GIỮ**: moan giữ Ư của audit + đếm số: "Hàà... hàà... hàà——hà——aa~Ư".
- **lr_稀咲h1 1708 GIỮ**: 16u đã kiểm chứng (mora u 9 trong âm tiết + 7 trong chuỗi う/ぅ; AUD 15, CSV3 14).
- **lr_ふかみh2 1085 GIỮ**: 19a đã kiểm chứng (quyết của parent; AUD 18a).
- **日々姫h5 1153 GIỮ**: 9a đã kiểm chứng (JP あ×9; moan JSON đã là giá trị parent hiệu chỉnh).
- **れいなh2 1095 GIỮ**: JP 「うむ」, CSV3 "Ừm.", không có fix ở đâu — GIỮ theo audit §7.
- **lr_ハチロクh1 1234 GIỮ**: moan "chumu" cho ちゅむっ (audit "chum" làm mất u).
- **lr_日々姫ふかみh1 933/1406/1423/1475 GIỮ** (giá trị hiện tại = moan đã gộp với audit) + **1358 GIỮ**: giá trị hiện tại = U11a M16 "Fafyuuuuuuuuuuuuuunn" (u=14, n=2 đã kiểm chứng vs JP ふぁふゅ+13ぅ+んん); "Fuafyu..." của F30 đã bị M16 thay thế ở token ふぁ (ghi chú U11a: "Token dán 1358 (a:1, u:14, n:2) chỉ bỏ 'u' thừa").

## 6. Quyết định trong đợt này

1. **ハチロクh8 878 (OPEN → QUYẾT)**: khôi phục "ưm!" — xem §4.4 (bằng chứng JP んっ riêng biệt + TW 嗯; audit mời xem lại).
2. **Hiệu chỉnh nhãn file F30** (bảng §2) — key đáng tin, nhãn file sai có hệ thống.
3. **Rebase cơ sở tổng**: header `ROUTE-UNIFICATION.md` ghi 71 mục / 2.338 dòng (22/11 ~12:15) đã cũ — U11b (72/2.339) và U8 (86/2.389) gộp trong lúc đợt này chạy. Map unification đã nạp lại với đủ 20 file đã gộp (2.354 key duy nhất). Không có dòng F30 nào trùng U8/U11b (file U8: lr_ニイロクh, lr稀咲追加01/02, ニイロク02, 稀咲h2; U11b: 凪ふかみh1 1218) — old_vn của 12 dòng sửa không đổi.
4. **Mikuro 1716 GHÉP với U11a** (không cộng lại dòng) — xem §4.1.
5. **Không mở rộng M10/M7**: 2185 (M10) và 2241 (M7) chỉ cắm cờ, không tự sửa.

## 7. Lượt soát 2 (second pass)

Đọc lại toàn bộ 12 fix so với JP (+TW) sau khi viết JSON, kèm kiểm chứng bằng máy (token romaji khớp mora JP; đếm 768 = 10u; 1716 giữ "Fua" + đổi "phuê"→"Fue"; 878 "ưm" khớp んっ + TW 嗯).

- **Tổng số: 12 / Tái kiểm chứng: 12 / Loại bỏ: 0 / Sửa: 0.**

## 8. Khối TOML (parse-verified, theo file)

4 file / 12 key parse-verified bằng tomllib; giá trị parse ra khớp JSON từng key. Giá trị `\n` chữ trong fix được viết `\\n` trong khối.

# lr追加_みくろ＆日々姫h「みくろのマスター」.txt.toml
```toml
[script]
"1708" = "「Fue!? Lại nữa── Mikuro! Lại nữa!\\nBởi vì! Cương cứng! Bởi vì! Bởi vì!!」"
"1716" = "「Fua── a── tuyệt quá── Fue!!?\\nA, Mikuro── xin lỗi, đồng phục── chị, làm bẩn mất rồi」"
"1758" = "「Hyua!? A── a…… Fue!?」"
"1811" = "「A……ưm──chụt──chụt──chụt──fu\\n……ưm……liếm──liếm──liếmmm──Pua」"
"1901" = "「Pua──fufu, anh ấy bảo thế kìa. Mikuro.」"
```

# ポーレットh6_あなたとふたりの学園エッチ.txt.toml
```toml
[script]
"768" = "「Kyuuuuuuuuuun!!!」"
"800" = "「Kua——a——」"
"818" = "「Kua!!!」"
"869" = "「Nkyun!」"
```

# ポーレットh5_裸エプロンのレモンドレッシング和え.txt.toml
```toml
[script]
"932" = "「Kua!」"
"947" = "「Nkyun!!!!」"
```

# ハチロクh8_桜色のひめごと.txt.toml
```toml
[script]
"878" = "「Suzu muốn, tất cả——Ngài Soutetsu——ưm!\\nNhuốm màu——tạo hình lại——cho em——!」"
```

## Kết bài

Đợt U10b xét 105 dòng F30: **12 dòng sửa** (5 mikuro huỷ "phuê"/"pùa" → romaji CSV3, 4 ポーレットh6 + 2 ポーレットh5 huỷ fix audit khôi phục "Kua"/"Nkyun"/"Kyuuuuuuuuuun", 1 ハチロクh8 878 khôi phục "ưm!" theo quyết mới) và **93 dòng giữ** có lý do từng nhóm. Trùng lặp: 1 dòng GHÉP (mikuro 1716 với U11a, không cộng lại). Còn nợ coordinator: hiệu chỉnh nhãn file F30 trong list (§2, cờ F1); ranh giới M7/M10 ở ポーレットh8 2241/2185 (cờ F2/F3); chuẩn hoá chữ hoa/thường romaji mikuro (cờ F5); xung đột main-vs-supplement moan ハチロクh3 1029/1063/1677 (cờ F6); và xác nhận số học chuỗi tổng sau U8 (cờ F9 — xem snippet).
