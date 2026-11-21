# Moan-fix REVIEW — 稀咲h3_チャイナドレスでおもてなし.txt.toml

## §1. Xác minh file

- File: `稀咲h3_チャイナドレスでおもてなし.txt.toml` — route 06_Kisaki.
- Đường dẫn đĩa: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/06_Kisaki/#U7a00#U54b2h3_#U30c1#U30e3#U30a4#U30ca#U30c9#U30ec#U30b9#U3067#U304a#U3082#U3066#U306a#U3057.txt.toml`
- TOML md5: `3bccfb4626ff9b0e014a8655d1091f7e` — không có bản trùng (chỉ 1 file h3 trong thư mục 06_Kisaki).
- TOML: UTF-8 BOM + CRLF (1.341 dòng), 662 dòng script; `[info]`, `[characters]`, `[character_subs]`, `[script]`, `[selections]`.
- CSV3: 1 bộ duy nhất, thư mục `translation_toml\\06_Kisaki`, 662 dòng script, 0 khóa trùng. VN TOML-2 khớp CSV3 662/662 sau khi chuẩn hóa `\n` (TOML-2 dẹp `\n` thành khoảng trắng — đã biết, CSV3 là chuẩn cho fix list). Không có bộ CSV thứ hai, không cần chọn bộ tốt.
- Nội dung: Kisaki tham quan xưởng rượu nhà Migita, hẹn hò ăn crepe, thử sườn xám Trọng Quốc may đo, cảnh H (sườn xám xuyên thấu, quan hệ trên sofa). Audit đã merge: 75/662 dòng sai (11,3%).
- Cơ sở tổng moan trước file này (đọc từ `moans/ROUTE-MOANS.md` — snippet cuối đã merge): **6 file / 156 dòng**.

## §2. Kho rên (moan inventory)

- Đã đọc 662/662 dòng (CSV3 + TOML-2).
- 414 dòng ứng viên đã sàng lọc (JP chứa âm rên/SFX hoặc VN có cách diễn rên); 57 dòng còn lại chứa っ/ぁ/ぅ đã kiểm tra tay — toàn từ thường (ちょっと, だった, もっと…) + SFX hành động trong ngoặc （ごとっ）→"（Cạch）", （むにゅっ）→"（Nắm lấy）" v.v. — không phải rên.
- Dòng rên/SFX thực sự (JP chứa âm rên theo danh sách chặt: họ ふぁ/ふあ, ひあ/ひゃ/ひゅ, あ/は/ん/く/ふ, cười ふふ/うふふ, SFX ちゅ/ぴちゃ/ぐちゅ/ずぶ…, SFX trong ngoặc （）): **181 dòng** (97 thoại Kisaki, 14 thoại Soutetsu, 70 độc thoại — trong đó 58 dòng SFX trong ngoặc).
- **Đổi 23 dòng; giữ 158 dòng rên/SFX.**
- Phân loại 23 dòng đổi: romaji 19 (fa/fu → Fua/Pua: 13; họ hia/hya/hyu → romaji: 4; gộp mảnh rời của âm dài: 2), độ dài nguyên âm 2 (2162, 2269), âm sai 2 (2228, 2238).
- Sweep: 13 mục cho file này đã kiểm tra trực tiếp trong `sweep-raw-gasp-wrong.json` — 11 fix Ư đã được audit áp nguyên (1552, 2003, 2161, 2257, 2809, 2810, 2813, 2814, 2824, 2826, 3143), 2 already-rendered (3373, 3483 — không thêm Ư). **Không sửa lại dòng gasp Ư nào.** Riêng 2257 có đổi moan nhưng GIỮ Ư của audit trong fix value (xem §6).

## §3. Các dòng sửa (23 dòng)
### 1538 [稀咲] — romaji

JP: 「っ――ううん。ふあっ――なん、でも――ない……\nんっ――」

TW: 「――不，嗚啊――沒什麼――事……嗯――」

Cũ: 「――Ưm. Phua――không, có――gì……\nưm――」

Mới: 「――Ưm. Fua――không, có――gì……\nưm――」

Lý do: ふあっ → "Phua" là cách diễn Việt của họ fa/fu, nghe ngượng; file này đã dùng "Fua!" ở 2255 cho cùng âm ふあっ — thống nhất sang romaji "Fua".
### 2120 [稀咲] — romaji

JP: 「これっ！　またっ――来てっ！　チカって――\nふあっ――あたま――しろい、の――波っ、きてっ」

TW: 「又！　又――來了！　冒星星――嗚啊――腦袋――白茫茫的――一片」

Cũ: 「Cái này! Lại――đến rồi! Chớp chớp――\nPhua――đầu óc――trắng xóa――cơn sóng, đang đến」

Mới: 「Cái này! Lại――đến rồi! Chớp chớp――\nFua――đầu óc――trắng xóa――cơn sóng, đang đến」

Lý do: ふあっ → "Phua" là cách diễn Việt của họ fa/fu, nghe ngượng — sang romaji "Fua" (nhất quán với "Fua!" ở 2255).
### 2152 [稀咲] — romaji

JP: 「ひゃっ――はっ――かふっ――ふあっ――それ――\nゆっくり――ゆっくり――されたらっ――――」

TW: 「呀――哈――哈呼――嗚啊――那是――慢慢地――慢慢地――來的話――」

Cũ: 「Hya――hà――khaphu――phua――cái đó――\nNếu bị――làm――chậm rãi――chậm rãi――――」

Mới: 「Hya――hà――khaphu――Fua――cái đó――\nNếu bị――làm――chậm rãi――chậm rãi――――」

Lý do: ふあっ → "phua" là cách diễn Việt của họ fa/fu, nghe ngượng — sang romaji "Fua". Giữ "Hya" (ひゃっ) và "khaphu" (かふっ, một cách diễn gộp đúng).
### 2155 [稀咲] — romaji

JP: 「ひゅあ――あっ！　はひゅっ！　しゅごっ！\nそこっ――知らない――これっ――んうううっ！！」

TW: 「呀啊――啊！　嗯！　我喜歡！我――都不知道――這裡――嗯嗚！！」

Cũ: 「Hyua――á! Hahyu! Tuyệt quá!\nChỗ đó――em không biết――cái này――ư ư ư!!」

Mới: 「Hyua――á! Hahyu! Tuyệt quá!\nChỗ đó――em không biết――cái này――Nuuu!!」

Lý do: んうううっ là MỘT âm dài duy nhất, bản cũ tách thành 3 mảnh rời "ư ư ư" — gộp thành một cách diễn romaji "Nuuu" (công thức nguyên âm: 3 u — ん → N, う ×3: âm gốc う + 2 う kéo dài). Tiền lệ ふかみh1: gộp các mảnh rời thành một cách diễn romaji.
### 2162 [稀咲] — vowel-length

JP: 「ひゃうっっ！！？」

TW: 「呀！！？」

Cũ: 「Hya!!?」

Mới: 「Hyau!!?」

Lý do: ひゃうっっ thiếu âm う trong "Hya" — bản cũ làm mất một mora. File này đã diễn ひゃうっ thành "Hyau!" ở 2159; sửa độ dài nguyên âm thành "Hyau!!?" (audit có ghi giữ "Hya!!?" dạng ngẫu hứng, nhưng đó là quyết định trước quy tắc romaji; lỗi ở đây là thiếu âm, không phải chọn dạng).
### 2170 [稀咲] — romaji

JP: 「っっっ～～っ――ふぁっ、あっ――おっぱい――ん、\nふっ――ふあっ――んっ――ふうっ――ふうっ」

TW: 「呃～～――哇、啊――胸部――嗯、呼――嗚啊――嗯――呼――呼」

Cũ: 「~~~――phua, á――vú――ưm,\nphù――phua――ưm――phù――phù」

Mới: 「Ư~~~――Fua, á――vú――ưm,\nphù――Fua――ưm――phù――phù」

Lý do: 2× ふぁっ "phua" → romaji "Fua". GIỮ Ư của audit (っっっ～～っ → "Ư~~~", audit fix đã thêm) — fix value này đã gộp cả Ư của audit, xem §6.
### 2188 [稀咲] — romaji

JP: 「ふうっ――はぁ――んっ――ふぁっ――んっ――\n～～っ！　はっ――ふぁっ――ん……んふ――」

TW: 「呼――哈――嗯――哇――嗯――～～！　哈――哇――嗯……嗯唔――」

Cũ: 「Phù――hà――ưm――phua――ưm――\n~~! Hà――phua――ưm……ưm phu――」

Mới: 「Phù――hà――ưm――Fua――ưm――\n~~Ư! Hà――Fua――ưm……ưm phu――」

Lý do: 2× ふぁっ "phua" → romaji "Fua". GIỮ Ư của audit (～～っ → "~~Ư!", audit fix đã thêm) — fix value này đã gộp cả Ư của audit, xem §6.
### 2195 [稀咲] — romaji

JP: 「ひあっ――あっ――あっ――ふあっ――ああっ――\nそうっ――てつ――すきっ――すき――すきぃ」

TW: 「咿啊――啊――啊――嗚啊――啊啊――雙――鐵――喜歡――喜歡――喜歡你」

Cũ: 「Hia――á――á――phua――á á――\nSou――tetsu――yêu anh――yêu anh――yêu anh」

Mới: 「Hia――á――á――Fua――á á――\nSou――tetsu――yêu anh――yêu anh――yêu anh」

Lý do: ふあっ "phua" → romaji "Fua". Giữ "á á" (ああっ) theo tiền lệ audit đã khóa (hachiroku-h5/fukamih3); giữ "Hia" (ひあっ).
### 2197 [稀咲] — romaji

JP: 「ひあっ――んっ――それっ――あっ！　ちく、びっ\n――そんな、に――くりくり――され、たらぁっ」

TW: 「咿啊――嗯――那是――啊！　乳頭――這樣――捏來捏去――的話」

Cũ: 「I a――ưm――cái đó――á! Núm, vú\n――bị――vê――như thế, thì」

Mới: 「Hia――ưm――cái đó――á! Núm, vú\n――bị――vê――như thế, thì a」

Lý do: ひあっ "I a" tách MỘT âm thành 2 mảnh rời, lại không nhất quán với "Hia" ở 2195 cho cùng âm ひあっ → romaji "Hia". たらぁっ: âm ぁ cuối dòng bị mất hẳn trong "thì" → thêm "a" ("thì a") theo quy tắc không để mất âm. Lưu ý: audit có quy ước っ dính từ nội dung không thêm Ư, nhưng đây là ぁ (một mora nguyên âm), không phải chỉ っ — xem §5.
### 2198 [稀咲] — romaji

JP: 「ひウっ！！！」

TW: 「咿！！！」

Cũ: 「I ư!!!」

Mới: 「Hiu!!!」

Lý do: ひウっ "I ư" tách MỘT âm thành 2 mảnh rời ("I" + "ư") → romaji "Hiu" (ひ + ウ nhấn mạnh bằng katakana).
### 2206 [稀咲] — romaji

JP: 「はっ！？　ひゅっ――ひあ――それっ――なにっ」

TW: 「哈！？　咿――咿啊――那是――什麼」

Cũ: 「Hả!? Hưu――hia――cái đó――là gì vậy」

Mới: 「Hả!? Hyu――hia――cái đó――là gì vậy」

Lý do: ひゅっ "Hưu" — "hưu" là từ Việt có nghĩa thật (nghỉ hưu), đọc lên rất ngượng trong tiếng rên → romaji "Hyu". Giữ "hia" (ひあ, đã romaji).
### 2207 [稀咲] — romaji

JP: 「ぷぁ。んふっ……」

TW: 「哈，嗯唔……」

Cũ: 「Pha. Ưm fu……」

Mới: 「Pua. Ưm fu……」

Lý do: ぷぁ "Pha" — "pha" là từ Việt (pha chế), đọc như một từ có nghĩa → romaji "Pua" (ぷぁ = pu + ぁ). Giữ "Ưm fu" (んふっ).
### 2225 [稀咲] — romaji

JP: 「ぁ――ぁっ――ふあっ――あっ――あつい――の\n――しきゅう――たたいて――ふあっ――あっ」

TW: 「啊――啊――嗚啊――啊――好熱――啊――撞在――子宮上――嗚啊――啊」

Cũ: 「A――á――phua――á――nóng――quá\n――tử cung――đang đập――phua――á」

Mới: 「A――á――Fua――á――nóng――quá\n――tử cung――đang đập――Fua――á」

Lý do: 2× ふあっ "phua" → romaji "Fua". Giữ "A――á――" (ぁ――ぁっ――) và "a……" (あ……).
### 2228 [双鉄] — wrong-sound

JP: 「う……む」

TW: 「啊……嗯」

Cũ: 「Ư…… m」

Mới: 「Ư…… ừm」

Lý do: う……む "Ư…… m" — "m" lẻ loi không phải một âm tiết, đọc như lỗi đánh máy → "Ư…… ừm" (む diễn thành âm tiết đầy đủ).
### 2238 [稀咲] — wrong-sound

JP: 「あむっ――んっ――ふぁ……んっ――ちゅむっ\nほーへふっ――ふっ――しゅき――んっ――ちゅっ」

TW: 「啊嗚――嗯――哇……嗯――啾唔啊嗚――呼――喜歡――嗯――啾」

Cũ: 「A mu――ưm――fua…… ưm――chu mu\nAnh Houhehu――fu――hích anh――ưm――chụt」

Mới: 「A mu――ưm――fua…… ưm――chu mu\nAnh Houhefu――fu――hích anh――ưm――chụt」

Lý do: ほーへふっ "Anh Houhehu" có 2 vấn đề: (1) "Anh" không có cơ sở nào trong JP — TW diễn thành tiếng thở (呼), đây là âm nghẹn khi miệng đang bận hôn, không phải lời xưng hô (kiểu bịa thêm của Gemini); (2) "Houhehu" viết sai ふ thành "hu" — Hepburn đúng là "Houhefu". Bỏ "Anh", sửa thành "Houhefu". Giữ "fua……" (ふぁ……), "hích anh" (しゅき nói ngọng — diễn hay, giữ).
### 2252 [稀咲] — romaji

JP: 「ふあっ――あっ――あ……子宮……これ……\nんっ――卵子……精液で、おぼれちゃう、かも」

TW: 「嗚啊――啊――啊……子宮……這個……嗯――卵子……要給精液從頭泡到腳了」

Cũ: 「Phua――á――a……tử cung……cái này……\nƯm――trứng……chắc sẽ, chết đuối trong tinh dịch mất」

Mới: 「Fua――á――a……tử cung……cái này……\nƯm――trứng……chắc sẽ, chết đuối trong tinh dịch mất」

Lý do: ふあっ "Phua" → romaji "Fua". Giữ "á" (あっ), "a……" (あ……).
### 2253 [稀咲] — romaji

JP: 「ふあっ――んっ――そう、てつ――すご、い――\nっ――びく、びく――してる――あつくて、おっきい」

TW: 「嗚啊――嗯――雙鐵――好厲害――小雞雞――跳個不停――好熱、好粗壯」

Cũ: 「Phua――ưm――anh, Soutetsu――tuyệt, quá――\n――giật, giật――liên hồi――nóng quá, to quá」

Mới: 「Fua――ưm――anh, Soutetsu――tuyệt, quá――\nƯ――giật, giật――liên hồi――nóng quá, to quá」

Lý do: ふあっ "Phua" → romaji "Fua". GIỮ Ư của audit (っ―― → "Ư――", audit fix đã thêm) — fix value này đã gộp cả Ư của audit, xem §6.
### 2254 [稀咲] — romaji

JP: 「ふあっ！　ペニスっ――すごい――双鉄っ――\nこんなに、硬くっ――て――ふ、あっ――熱いっ」

TW: 「嗚啊！　陰莖――好棒――雙鐵――已經這麼硬了――呼、啊――好熱」

Cũ: 「Phua! Dương vật――tuyệt quá――anh Soutetsu――\nCứng――như thế này――phu, á――nóng quá」

Mới: 「Fua! Dương vật――tuyệt quá――anh Soutetsu――\nCứng――như thế này――phu, á――nóng quá」

Lý do: ふあっ！ "Phua!" → romaji "Fua!". Giữ "phu, á" (ふ、あっ — JP tự tách bằng dấu phẩy, VN diễn theo đúng cấu trúc JP).
### 2257 [稀咲] — romaji

JP: 「くふぅんんんん～～～～っ！！！」

TW: 「嗚嗯～～～～！！！」

Cũ: 「Khu phư ưm~~~~!!!」

Mới: 「Kufuunnnn~~~~Ư!!!」

Lý do: くふぅんんんん là MỘT âm dài duy nhất, bản cũ tách thành 3 mảnh rời "Khu phư ưm" — gộp thành romaji "Kufuunnnn" (く→Ku, ふぅ→fuu theo công thức 1+1=2 u, んんんん→nnnn). GIỮ Ư của audit (～～～～っ → "~~~~Ư", audit fix đã thêm) — fix value này đã gộp cả Ư của audit, xem §6.
### 2269 [稀咲] — vowel-length

JP: 「ん……ちゅっ――ふっ――ちゅむっ――ちゅっ、\nちゅるっ――れろっ――れるうっ――ちゅむっ」

TW: 「嗯……啾――呼――啾唔――啾、啾――舔――舔――啾唔」

Cũ: 「Ưm……chụt――phu――chụt――chụt,\nchụt――rero――rero――chụt」

Mới: 「Ưm……chụt――phu――chụt――chụt,\nchụt――rero――Reroo――chụt」

Lý do: れるうっ "rero" — mất độ dài của う: JP phân biệt rõ れろっ (ngắn) vs れるうっ (dài), VN diễn cả hai thành "rero" giống hệt nhau → "Reroo" (giữ "rero" cho れろっ).
### 2277 [稀咲] — romaji

JP: 「んひゅんっ！！！」

TW: 「嗯呀！！！」

Cũ: 「Ưm hưu!!!」

Mới: 「Nhyun!!!」

Lý do: んひゅんっ "Ưm hưu" — "hưu" là từ Việt có nghĩa thật (nghỉ hưu), rất ngượng trong tiếng rên → romaji "Nhyun" (ん→N, ひゅ→hyu, ん→n). Audit có ghi giữ dòng này nhưng lý do giữ là về っ cuối (không thêm Ư) — fix này không thêm Ư, chỉ sửa cách diễn âm.
### 2360 [稀咲] — romaji

JP: 「おまん、こ――いっぱい――ぜんぶ、双鉄っ――\nそうてつ、の、――おちんちん、にぃっ――ふあっ！」

TW: 「小穴――都是――都是雙鐵――雙鐵的――小雞雞――嗚啊！」

Cũ: 「Âm đạo――đầy ắp――tất cả, anh Soutetsu――\ndương vật, của, ――anh Soutetsu――phua!」

Mới: 「Âm đạo――đầy ắp――tất cả, anh Soutetsu――\ndương vật, của, ――anh Soutetsu――Fua!」

Lý do: ふあっ！ "phua!" → romaji "Fua!".
### 3808 [monologue] — romaji

JP: （もみゅっ――もにっ――くにゅつ――ふあっ――）

TW: （揉――揉――夾――嗚啊――）

Cũ: （Xoa――nắn――bóp――phua――）

Mới: （Xoa――nắn――bóp――Fua――）

Lý do: ふあっ trong SFX ngoặc （） "phua" → romaji "Fua". Giữ 3 động từ Xoa/nắn/bóp của các SFX hành động (もみゅっ/もにっ/くにゅつ) — phong cách nhất quán của file.
## §4. Các dòng rên đã giữ (ghi chú đáng kể)

- **11 dòng gasp Ư của sweep đã khóa** (1552, 2003, 2161, 2257, 2809, 2810, 2813, 2814, 2824, 2826, 3143) — audit đã áp nguyên, không sửa lại. 2257 đổi moan nhưng giữ Ư. 2 already-rendered (3373, 3483) giữ nguyên.
- **Audit đã sửa sang romaji, giữ nguyên:** 2158 「きゃああっ！？」→ "Kyaaa!?"; 2218 (chỉ thêm Ư, giữ "Hà"); 2820 (chỉ thêm Ư, giữ "hya! Phu").
- **Audit giữ rõ ràng, tôn trọng không đổi:** 2240 ふゅぁぁあああんんんっ → "Phuaaaaưm!" (audit §§32/36 ghi giữ nguyên 2 lần: một cách diễn gộp duy nhất, っ dính vào từ moan đã diễn thành từ); 2116 きゅううううううううううんんんっ → "Ra――rồiiiiii!!!" (diễn nghĩa, audit giữ); 2278 んきゅっ → "Ưm kyu!?" (audit giữ); 2279 んんんっっ → "Ưm ưm!!!"; 2398 くひゅぅぅぅぅぅんっ → "khưuuuuu!!" (đếm đúng: 1 + 5 ぅ = 6 nguyên âm); 2256 ううっ → "Ư ư"; 2260/2195 ああっ → "a a"/"á á" (tiền lệ audit đã khóa, hachiroku-h5/fukamih3).
- **JP tự tách âm bằng dấu câu — VN diễn theo đúng cấu trúc JP, giữ:** 2189 ふ……ぁっ → "Fu…… a――"; 2203 ふ、ぁ…… → "fu, a……"; 2254 ふ、あっ → "phu, á".
- **ふっ/ふうっ ngắn → "fu"/"phù", giữ** (ghi chú audit: ふっ ngắn giữ nguyên): 2201, 2260, 2266, 2269, 2057, 1988 "kya phu" (きゃふっ 2 mora, diễn đủ cả hai).
- **Cười là cười, không phải rên:** ふふっ → "Fufu" (2183, 2180, 2493, 2179), うふふっ → "ufufu" (2465), うふふっ → "Ufufu" (2185) — giữ.
- **Đã romaji sẵn, giữ:** 2239 はうっ → "Hau"; 2217 くあっ → "Kua!"; 2255 ふあっ → "Fua!"; 2159 ひゃうっ → "Hyau!"; 2157 ひゅあっ → "Hyua!"; 2160 ひゃんっ → "Hyan!"; 2165 ひゃうっ → "hyau"; 2223 ぁ―― → "A――".
- **SFX trong ngoặc （） dịch thành từ Việt — phong cách nhất quán của file, giữ:** （Thúc） (3826), （Nắn nắn――） (3811), （Bóp chặt!!） (3815), （Phập!!!!） (3754/3768/3689…), （Trơn tuột） (3751/3774), （Cọooooo!） (3819/3820), （Chụt） (3787), （Hự!!!） (3780), （Phụt!…） (3782/3794/3790), （Liếm――liếm――liếm） (2816), （Liếm） (3816), （Nắm lấy） (3799), （Nắn） (3804), （Roạt） (3752), （Nhóp nhép） (3753), （Trượt） (3771), （Cạch） (3783).
- **Âm uống/hôn, diễn tự nhiên, giữ:** 2268 (uống rượu: "Ưm…… phu…… ưm――ực――chu zu――ưm――ực――ực――ưm fu"); 2266/2265/2238 (hôn: "chụt/chu mu", "fua……"); 2261 んっっ → "Ưm"; 2283 んっ → "Ưm!!!"; 2258 「っ――」→ "Ưm――" (gasp đã diễn thành tiếng ưm kìm nén, không mất âm).
- **Các âm ngắn đã diễn đúng, giữ:** 2234 あっ → "A"; 2241 あっ → "Á!"; 2242 あっ → "A!?"; 2164 やっ → "Á!?"; 2675 はあ → "Hà"; 2726 ん → "ưm"; 2214 む → "Ưm"; 2515/2276/1539 うん → "Ừm".

## §5. Cờ (flags — ghi lại, không tự quyết hộ Hieu)

- **2238 "Anh Houhehu" → "Anh Houhefu":** parent đã LÙI phần bỏ "Anh" khi merge (là sửa đại từ, không thuộc moan — xem ghi chú parent). Chỉ giữ phần sửa âm ふ "hu"→"fu". Cờ cho đợt thống nhất: "Anh" ở đây có đúng là cách xưng của Kisaki với Soutetsu không (quy tắc đã chốt: Kisaki gọi Soutetsu là "cậu"/tên trần, không phải "anh"), hay là từ bịa thêm của Gemini (TW diễn thành tiếng thở 呼)? Audit không cờ dòng này.
- **2197 "thì a":** đã thêm âm "a" cuối dòng cho たらぁっ theo quy tắc không để mất âm. Audit có quy ước っ dính từ nội dung không thêm Ư, nhưng đây là ぁ (một mora nguyên âm) chứ không phải chỉ っ — ghi lại để parent kiểm chứng khi merge.
- **2162 "Hya" → "Hyau":** audit có ghi giữ "Hya!!?" dạng ngẫu hứng (trước quy tắc romaji); lỗi ở đây là thiếu âm う (JP ひゃうっっ), và file này đã diễn ひゃうっ thành "Hyau!" ở 2159 — sửa vì thiếu âm, không phải vì thống nhất dạng.
- **2206/2277 "Hưu"/"hưu":** audit có ghi giữ 2277 nhưng lý do giữ là về っ cuối (không thêm Ư); fix này không thêm Ư, chỉ sửa cách diễn âm ("hưu" là từ Việt có nghĩa thật).

## §6. Ghi chú áp dụng (cho đợt thống nhất / parent merge)

- **4 dòng có fix value GỘP cả Ư của audit — dùng fix của moan, KHÔNG áp thêm fix audit của cùng key (tránh trùng Ư):** 2170, 2188, 2253, 2257. Ư của audit trong 4 dòng này: 2170 "Ư~~~" (っっっ～～っ), 2188 "~~Ư!" (～～っ), 2253 "Ư――" (っ――), 2257 "~~~~Ư" (～～～～っ).
- **Audit đã khóa, đã tôn trọng không đổi:** "a a"/"á á" (ああっ, 2260/2195), "Phuaaaaưm!" (2240), "rồiiiiii" (2116), "Ưm kyu" (2278), "Ưm ưm" (2279), "khưuuuuu" (2398), "Ư ư" (2256).
- **Fa/fu trong file sau fix này:** tất cả ふあっ/ふぁっ không tách đều thành "Fua" (13 dòng + "Fua!" sẵn ở 2255); chỉ còn "phu"/"phù" cho ふっ/ふうっ ngắn và các dạng JP tự tách ("Fu…… a", "fu, a", "phu, á") — các dạng này giữ nguyên theo cấu trúc JP.
- **Không dòng "Kh" nào bị đổi.** Không dòng Ư gasp nào bị sửa lại (trừ việc giữ Ư của audit trong 4 fix value ở trên).

## §7. Lượt soát 2 (second pass)

Đọc lại từng fix value đối chiếu trực tiếp JP (+TW) sau khi build JSON — 23/23 fix đã tái kiểm chứng, 0 bỏ, 0 sửa.
- Tổng: 23 / tái kiểm chứng: 23 / bỏ: 0 / sửa: 0.
- Lưu ý: bản nháp JSON đầu đã làm mất dấu 「 」 (phát hiện khi in kiểm tra lúc build, đã sửa trước lượt soát 2 — lượt soát 2 chạy trên JSON đã sửa, 23/23 đạt).

## §8. Khối TOML (parse-verified)

Khối dưới đây parse bằng tomllib: 23 khóa, 0 sai lệch giá trị so với JSON. (`\n` trong khối là backslash-n chữ, khớp CSV3.)

```toml
[script]
"1538" = "「――Ưm. Fua――không, có――gì……\\nưm――」"
"2120" = "「Cái này! Lại――đến rồi! Chớp chớp――\\nFua――đầu óc――trắng xóa――cơn sóng, đang đến」"
"2152" = "「Hya――hà――khaphu――Fua――cái đó――\\nNếu bị――làm――chậm rãi――chậm rãi――――」"
"2155" = "「Hyua――á! Hahyu! Tuyệt quá!\\nChỗ đó――em không biết――cái này――Nuuu!!」"
"2162" = "「Hyau!!?」"
"2170" = "「Ư~~~――Fua, á――vú――ưm,\\nphù――Fua――ưm――phù――phù」"
"2188" = "「Phù――hà――ưm――Fua――ưm――\\n~~Ư! Hà――Fua――ưm……ưm phu――」"
"2195" = "「Hia――á――á――Fua――á á――\\nSou――tetsu――yêu anh――yêu anh――yêu anh」"
"2197" = "「Hia――ưm――cái đó――á! Núm, vú\\n――bị――vê――như thế, thì a」"
"2198" = "「Hiu!!!」"
"2206" = "「Hả!? Hyu――hia――cái đó――là gì vậy」"
"2207" = "「Pua. Ưm fu……」"
"2225" = "「A――á――Fua――á――nóng――quá\\n――tử cung――đang đập――Fua――á」"
"2228" = "「Ư…… ừm」"
"2238" = "「A mu――ưm――fua…… ưm――chu mu\\nAnh Houhefu――fu――hích anh――ưm――chụt」"
"2252" = "「Fua――á――a……tử cung……cái này……\\nƯm――trứng……chắc sẽ, chết đuối trong tinh dịch mất」"
"2253" = "「Fua――ưm――anh, Soutetsu――tuyệt, quá――\\nƯ――giật, giật――liên hồi――nóng quá, to quá」"
"2254" = "「Fua! Dương vật――tuyệt quá――anh Soutetsu――\\nCứng――như thế này――phu, á――nóng quá」"
"2257" = "「Kufuunnnn~~~~Ư!!!」"
"2269" = "「Ưm……chụt――phu――chụt――chụt,\\nchụt――rero――Reroo――chụt」"
"2277" = "「Nhyun!!!」"
"2360" = "「Âm đạo――đầy ắp――tất cả, anh Soutetsu――\\ndương vật, của, ――anh Soutetsu――Fua!」"
"3808" = "（Xoa――nắn――bóp――Fua――）"
```

## Ghi chú của parent (kiểm chứng khi gộp, 21/11 ~10:00)

- Kiểm chứng: JSON 23 mục dạng chuẩn, khóa string; khối TOML 23 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 23/23; TOML md5 3bccfb4626ff9b0e014a8655d1091f7e khớp audit; 4 key trùng audit (2170, 2188, 2253, 2257) chỉ khác giá trị audit ở đúng token rên; mọi Ư thêm vào đều là Ư của audit (4/4); không dòng "Kh" nào bị đổi; lượt soát 2: 23/23, 0 bỏ, 0 sửa.
- **SỬA 2155:** fix "Nuuuu" → "Nuuu" (JP んうううっ = 3 u — âm gốc う + 2 う kéo dài; agent áp công thức dạng 1+3=4, đếm trùng âm gốc. Tiền lệ: mikuro 1675 ひゃううううう = 5 u, 1864 んぅ×18 = 18 u).
- **SỬA 2257:** fix "Kufuuunnnn" → "Kufuunnnn" (JP くふぅ = 3 u: く 1 + ふ 1 + ぅ 1; agent đếm thừa 1).
- **LÙI 2238 (phần bỏ "Anh"):** fix "Houhefu" → "Anh Houhefu" — chỉ giữ phần sửa âm ふ "hu"→"fu". Bỏ "Anh" là sửa đại từ, không thuộc phạm vi moan (quy tắc vòng moan: loại mọi fix phi-moan); audit không cờ dòng này. Cờ cho đợt thống nhất: "Anh" ở đây là cách xưng Kisaki→Soutetsu (trái quy tắc đã chốt: Kisaki gọi Soutetsu "cậu"/tên trần) hay từ bịa của Gemini (TW diễn thành tiếng thở 呼)?
- Giữ nguyên (đã ghi cờ): 2197 thêm "a" cho たらぁっ (ぁ là mora nguyên âm, quy tắc không để mất âm); 2162 "Hya"→"Hyau" (JP ひゃうっっ thiếu う, file đã có "Hyau!" ở 2159).

## Kết bài

File 稀咲h3_チャイナドレスでおもてなし.txt.toml (662 dòng) đã sửa moan xong: đổi 23 dòng (romaji 19, độ dài nguyên âm 2, âm sai 2), giữ 158 dòng rên/SFX. Trọng tâm là thống nhất họ fa/fu sang romaji "Fua" (13 dòng, nhất quán với "Fua!" sẵn có ở 2255), sửa 4 dòng họ hia/hya/hyu ("Hia", "Hiu", "Hyu", "Nhyun"), gộp 2 âm dài bị tách mảnh ("Nuuu", "Kufuunnnn"), sửa 2 lỗi độ dài nguyên âm ("Hyau", "Reroo") và 2 âm sai ("Ư…… ừm", "Anh Houhefu"). 11 dòng gasp Ư của sweep và các tiền lệ audit đã khóa được tôn trọng, không sửa lại. JSON 23 mục (khóa string), jp/tw/old_vn khớp CSV3 23/23; khối TOML parse bằng tomllib: 23 khóa, 0 sai lệch giá trị. Lượt soát 2: 23/23 tái kiểm chứng, 0 bỏ, 0 sửa.
