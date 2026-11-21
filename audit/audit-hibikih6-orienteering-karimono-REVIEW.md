# Audit: 日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml — 50/667 (7,5%)

## 0. Xác minh file

- File: `日々姫h6_オリエンテーリング借り物競走（ペア）.txt.toml` — route 02_Hibiki.
- TOML-2: `sources/toml2/translation_toml/02_Hibiki/#U65e5#U3005#U59ebh6_#U30aa#U30ea#U30a8#U30f3#U30c6#U30fc#U30ea#U30f3#U30b0#U501f#U308a#U7269#U7af6#U8d70#Uff08#U30da#U30a2#Uff09.txt.toml`, md5 `77423bec9e1cb3f3bfbb14002019ad44`, UTF-8 BOM + CRLF, 667 key script. 1 bản TOML duy nhất (không có file trùng).
- CSV3: 1 set duy nhất, 667/667 key khớp TOML; VN khớp TOML 661/667 — 6 lệch còn lại chỉ là TOML-2 làm phẳng `\n` thành khoảng trắng (2166, 2270, 2348, 2550, 2657, 2731); CSV3 là chuẩn. Không có set stale.
- `[selections]` rỗng. 0 lệch tag `%l` (file không có tag `%l`; 5 tag ruby `[x,N]` phía JP được VN chuẩn hoá đúng: 2348, 2476, 2494, 2526, 2701).
- Nội dung: cuộc thi chạy định hướng + mượn đồ theo cặp (Hibiki × Soutetsu) trong Đại hội thao khu phố thương mại; xen kẽ giải đố cờ vua/bản đồ (〒=123→132, ￥, b1/b8/g1/g8) và H-scene. Nhân vật: monologue 257, 日々姫 241, 双鉄 169.
- Lệch vị trí 0, chuỗi xoay 0, nhiễm chéo 0, mồ côi 0, chưa dịch 0, trùng khóa 0. (VN==JP duy nhất là key 2768 `〒=123→132` — dòng chỉ có ký hiệu, không phải chưa dịch. 4 VN trùng nhau đều là cùng JP lặp lại: 「À――」×2, 「!!!」×2 — 2201 là sweep fix nên khác, 「Đúng vậy」×2, 「Aaaaa!」×2 — 2202/2203 khác JP nên đã sửa đếm nguyên âm.)
- Đại từ Soutetsu kiểm chứng bằng máy: 0 "tôi" trong thoại 双鉄 (toàn "anh" với Hibiki — đúng); monologue toàn "tôi" (1 "anh" ở 3470 là lời trích trong ngoặc, không phải tự xưng); Hibiki không có "tôi"/"chị" tự xưng (4 "chị" đều là "chị cả"/"chị Paulette" ngôi thứ ba).

## 1. Phân loại (50)

- gasp 13 (9 từ sweep áp nguyên + 4 audit tự tìm: 1427, 2185, 2282, 2764)
- moan 25 (họ fa/fu → romaji 22, ぷ → P 2, mất âm 2, nguyên âm trong dòng moan 3 gộp)
- nguyên âm 8 (đếm nguyên âm romaji/chuỗi "A" sai: 2080, 2109, 2190, 2196, 2199, 2202, 2203, 2713)
- sai nghĩa 3 (2015, 2362: うける→"đỉnh"; 2457: đảo せいり/うんどう)
- thuật ngữ 1 (1985: 整備体→"Thân bảo trì")

## 2. Từng dòng sửa

### 2a. Gasp — sweep áp nguyên (9)

- **1418** [双鉄] JP: 「――っ」 / TW: 「――」 / Cũ: 「――」 / Mới: 「――Ư」 — gasp cuối dòng mất hoàn toàn, thêm Ư.
- **2201** [双鉄] JP: 「っっっ」 / TW: 「啊啊啊」 / Cũ: 「!!!」 / Mới: 「ƯƯƯ!!!」 — 3 っ → 3 Ư, giữ "!!!".
- **2241** [日々姫] JP: 「あんっ――ううう～～っ」 / TW: 「嗯――唔唔唔～～」 / Cũ: 「A――ư ư ư~~」 / Mới: 「A――ư ư ư~~Ư」 — っ cuối sau ～～ mất, thêm Ư.
- **2759** [双鉄] JP: 「っ！」 / TW: 「！」 / Cũ: 「!」 / Mới: 「Ư!」.
- **2761** [双鉄] JP: 「っ！！？」 / TW: 「！！？」 / Cũ: 「!!?」 / Mới: 「Ư!!?」.
- **2767** [日々姫] JP: 「～～～～～～～～～～～～っっ！！！！」 / TW: 「～～～～～～～～～～～～！！！！」 / Cũ: 「~~~~~~~~~~~~!!!!」 / Mới: 「~~~~~~~~~~~~ƯƯ!!!!」 — 12 ~ giữ nguyên, っっ → ƯƯ.
- **2982** [monologue] JP: `…封筒を取っては広げ――っ！！？` / TW: `…打開了――！！？` / Cũ: `…mở ra――!!?` / Mới: `…mở ra――Ư!!?`.
- **3414** [monologue] JP: `…丸見えになり――っ！` / TW: `…――` / Cũ: `…toàn bộ――!` / Mới: `…toàn bộ――Ư!`.
- **3421** [monologue] JP: `日々姫がズイと身を乗り出――っ！！？` / TW: `日日姬探出身子來――` / Cũ: `Hibiki rướn người tới trước――!!?` / Mới: `Hibiki rướn người tới trước――Ư!!?`.

### 2b. Gasp — audit tự tìm, sweep bỏ sót (4)

- **1427** [双鉄] JP: 「っ――！」 / TW: 「――！」 / Cũ: 「――!」 / Mới: 「Ư――!」 — gasp đầu dòng mất hoàn toàn; sweep không liệt kê (mẫu sweep chỉ bắt っ cuối dòng).
- **2764** [日々姫] JP: 「～～～～～っっ！　くあっ！　ああああっ！　んっ、そこ、おちんちん、だけの、とこ――しゅきっ」 / TW: 「～～～～～！啊！啊啊啊！嗯、那裡是，雞雞才能碰到的地方――我好喜歡」 / Cũ: 「~~~~~!! Kua! Aaaaa! Ưm, Chỗ đó, chỗ chỉ dành, cho chim――thích lắm」 / Mới: 「~~~~~ƯƯ!! Kua! Aaaaa! Ưm, Chỗ đó, chỗ chỉ dành, cho chim――thích lắm」 — っっ giữa dòng sau ～～～～～, cùng lớp với sweep 2767 nhưng sweep bỏ sót (chỉ bắt っ cuối dòng).
- **2185** [日々姫] JP: 「あ――はっ――んっ！　んんん～～っ！　は、ひゅ、そ、こっ――こしゅって――腰、らめ、ふわって！！」 / TW: 「啊――呼――嗯！嗯嗯嗯～～！呼、呀、那裡――噗哧一聲――腰、不行了、腰軟了！！」 / Cũ: 「A――hà――ưm! Ưm ưm~~! Hà, hyu, Chỗ, đó――bị ngoáy――Hông, không được, nhũn ra mất!!」 / Mới: 「A――hà――ưm! Ưm ưm ưm~~Ư! Hà, hyu, Chỗ, đó――bị ngoáy――Hông, không được, nhũn ra mất!!」 — sweep gắn nhãn "already-rendered" là SAI cho đoạn này: んんん có 3 nhịp mà VN chỉ có 2 "Ưm", và っ sau ～～ mất hoàn toàn (cùng mẫu với sweep 2241/2767). Nhãn sweep đúng cho んっ→Ưm ở đầu dòng, sai cho đoạn cuối.
- **2282** [日々姫] JP: 「うん、ゴールの時にふたり一緒にいれば良か――って！　違っ――違わなっ！　んっ――う～～っ」 / TW: 「嗯，兩個人一起到終點就可以了――啊！沒――沒錯！嗯――唔～～」 / Cũ: 「Vâng, chỉ cần lúc về đích hai người ở cùng nhau là được―― Á! Không――không phải! Ưm――ư~~」 / Mới: 「Vâng, chỉ cần lúc về đích hai người ở cùng nhau là được―― Á! Không――không phải! Ưm――ư~~Ư」 — sweep gắn nhãn "already-rendered" là SAI cho っ cuối dòng sau う～～: んっ→Ưm đã diễn đúng, nhưng う～～っ cuối dòng mất hoàn toàn (cùng mẫu sweep 2241).

### 2c. Moan — họ fa/fu → romaji (tiền lệ moan 凪h2 + MOAN-BRIEF quy tắc 5)

"Phù"/"Phù a" cho ふあ/ふぁ là sai nguyên âm (fua/fa ≠ fu) và tách một âm thành hai; "Phà" nghe ngượng trong dòng moan (đọc như từ "phà") nên dùng romaji. Phân biệt ふあ (2 kana → "Fua") với ふぁ (1 kana → "Fa").

- **1426** [日々姫] JP: 「――っ――か、はっ――ンッ――ふあ！　あっ！ / にぃに！　らめっ――こわれるっ――わた、ひっ」 / TW: 「――嗯――呃、啊――嗯――呼！啊！阿哥！不行――我要――壞掉了」 / Cũ: 「――ưm――hà――ưm――phù! A! / Anh hai! Không được――hỏng mất――em, mất」 / Mới: 「――ưm――hà――ưm――Fua! A! / Anh hai! Không được――hỏng mất――em, hi」 — (1) ふあ→"Fua"; (2) わた、ひっ: わた = "em" (cắt ngang từ わたし), ひっ là tiếng nấc "hi" (tiền lệ 2243 ひぃ、ひっ→"Hii, hi") — "mất" là sai, "mất" đã dùng cho こわれる rồi.
- **2075** [日々姫] JP: 「きゃふうううううんっ！　あっ！　おな、かっ―― / ぎゅうんって――おちん、ちん――ひろげっ――ふあ」 / TW: 「呀嗯！啊！肚子裡――有感覺――雞雞――撐開了――呼」 / Cũ: 「Kyafuuuuun! A! Trong, bụng―― / Bị nhồi nhét――chim――mở rộng ra――phù」 / Mới: 「Kyafuuuuun! A! Trong, bụng―― / Bị nhồi nhét――chim――mở rộng ra――Fua」 — (1) きゃふうううううん: 6 u (ふ 1u + う×5), cũ 5 u → thêm 1 u [PARENT SỬA: agent đếm nhầm う×6 và cũ 6 u]; (2) ふあ→"Fua".
- **2077** [日々姫] JP: 「ひゅあんっ！？　にっ、にぃ――ちょっ、待っ！ / はっ――ふあっ――あっ！　あっ！　ああああっ」 / TW: 「呀嗯！？阿哥――等、等等！呼――呼啊――啊！　啊！　啊啊啊！」 / Cũ: 「Hyuan!? A, anh hai――khoan, đợi đã! / Hà――phù――a! A! Aaaaa」 / Mới: 「Hyuan!? A, anh hai――khoan, đợi đã! / Hà――Fua――a! A! Aaaa」 — (1) ふあっ→"Fua"; (2) ああああっ 4 a, cũ 5 a → "Aaaa".
- **2084** [日々姫] JP: 「やああっ！　ンッ――これ――わたし――ふあっ！ / からだ――ちから、が――ぬけ、て――ふわっ、て」 / TW: 「呀！嗯――這個――我的――呼啊！身上――沒力氣了――軟綿綿的」 / Cũ: 「Yaaa! Ưm――Thế này――em――phù! / Cơ thể――sức lực――bị rút cạn――nhũn ra, mất」 / Mới: 「Yaaa! Ưm――Thế này――em――Fua! / Cơ thể――sức lực――bị rút cạn――nhũn ra, mất」.
- **2102** [日々姫] JP: 「はっ――ふあ、あっ――みちって、ひろがる――ん / ふっ――あっ、おなか、おまんこ、いっぱい、でっ」 / TW: 「呼――呼、啊――填滿了，撐開了――嗯、呼――啊、肚子裡、小穴裡、滿滿的」 / Cũ: 「Hà――phù, a――Căng đầy, mở rộng ra――ưm / Phù――a, bụng em, âm đạo em, đầy ắp, rồi」 / Mới: 「Hà――Fua, a――Căng đầy, mở rộng ra――ưm / Phù――a, bụng em, âm đạo em, đầy ắp, rồi」 — ふあっ、あっ → "Fua, a" (tiền lệ moan 凪h2); んふっ→"ưm Phù" giữ nguyên (ふ = hơi thở, đúng).
- **2111** [日々姫] JP: 「ふあっ――あっ、あつい、あついよぉ」 / TW: 「呼啊――好、好燙，好燙啊」 / Cũ: 「Phù――a, nóng quá, nóng quá đi」 / Mới: 「Fua――a, nóng quá, nóng quá đi」.
- **2112** [日々姫] JP: 「ふあっ」 / TW: 「呼啊」 / Cũ: 「Phù a」 / Mới: 「Fua」 — một âm, không tách thành hai (tiền lệ moan 凪h2).
- **2114** [日々姫] JP: 「ふぁぁぁぁぁあっ――ああっ――そこ、すき、なの / んっ――もっと、そこ、より――だけどっ、もっとぉ」 / TW: 「呼啊啊啊――啊啊――我喜歡那裡，嗯――比那裡，要更――更――」 / Cũ: 「Fuaaaaaa――aa――Chỗ đó, em thích, lắm / Ưm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」 / Mới: 「Faaaaaaa――aa――Chỗ đó, em thích, lắm / Ưm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」 — ふぁ = "Fa" (1 kana, 7 a: ふぁ 1 + ぁ×5 + あ 1), không phải "Fua" (thừa 'u', thiếu 1 'a').
- **2116** [日々姫] JP: 「ふあっ！？　あっ！　にぃに、ね？　そこ、ね？ / おちんちん――もっと――こしゅっ、こしゅっ、って」 / TW: 「呼啊！？啊！阿哥、那個、哪裡，用雞雞――再多――蹭蹭」 / Cũ: 「Phù!? A! Anh hai, nè? Chỗ đó, ấy? / Chim――nhiều hơn nữa――cọ xát, cọ xát, đi anh」 / Mới: 「Fua!? A! Anh hai, nè? Chỗ đó, ấy? / Chim――nhiều hơn nữa――cọ xát, cọ xát, đi anh」.
- **2117** [日々姫] JP: 「ふぁんっ！！！」 / TW: 「呼嗯！！！」 / Cũ: 「Fuan!!!」 / Mới: 「Fan!!!」 — ふぁん = "fan" (Hepburn), "Fuan" thêm 'u' không có trong JP.
- **2122** [日々姫] JP: 「ふぁっ！　あっ！　きもちい、きもちいいっ―― / んっ！　そこ、しゅき、おまん、こ、とけ、るうっ」 / TW: 「呼！啊！好舒服、好舒服啊――嗯！我喜歡、那裡、小穴、要化了」 / Cũ: 「Phù! A! Sướng quá, sướng quá đi―― / Ưm! Chỗ đó, em thích, âm đạo, sắp tan chảy, ra rồi」 / Mới: 「Fa! A! Sướng quá, sướng quá đi―― / Ưm! Chỗ đó, em thích, âm đạo, sắp tan chảy, ra rồi」.
- **2124** [日々姫] JP: 「ふあっ！　あっ！　びゅっびゅ！　あつい、のっ！ / どろって、しきゅう――あたってっ――たまって！」 / TW: 「呼！啊！射進來了！熱熱的！黏黏的――進到――子宮裡――積了起來！」 / Cũ: 「Phù! A! Bắn rồi! Nóng, quá! / Nhơm nhớp, tử cung――bị chạm vào――đọng lại rồi!」 / Mới: 「Fua! A! Bắn rồi! Nóng, quá! / Nhơm nhớp, tử cung――bị chạm vào――đọng lại rồi!」.
- **2138** [日々姫] JP: 「ぇえっ――ゆっくり――ん……くっ―― / は、あっ――ん――ふあっ！」 / TW: 「哎――慢慢的――嗯……唔――呼、啊――嗯――呼啊！」 / Cũ: 「Ể――từ từ――ưm……hự―― / Hà, a――ưm――phù a!」 / Mới: 「Ể――từ từ――ưm……hự―― / Hà, a――ưm――Fua!」.
- **2182** [日々姫] JP: 「あ――ふあっ――あっ――キス――ちゅうっ、 / ちゅうっ、するのっ――ちゅうううぅ」 / TW: 「啊――呼――啊――要接吻――要親親――親親」 / Cũ: 「A――phù――a――Hôn――chụt, / hôn em, đi――chụt」 / Mới: 「A――Fua――a――Hôn――chụt, / hôn em, đi――chụt」.
- **2184** [日々姫] JP: 「あ――ふっ――んっッ――ふあっ―― / ふとい――あつい、の――いつも、よりっ」 / TW: 「啊――呼――嗯――呼――比平時――好粗――好燙」 / Cũ: 「A――phù――ưm――phù―― / To quá――nóng, quá――hơn, mọi khi」 / Mới: 「A――phù――ưm――Fua―― / To quá――nóng, quá――hơn, mọi khi」 — "phù" đầu = ふっ (hơi thở, giữ); chỉ sửa ふあっ.
- **2210** [日々姫] JP: 「はっ！　きゅっ――うっ――ふっ――はっ―― / いきっ――いきっ――くるしっ――ふあっ、あっ！」 / TW: 「啊！呀――唔――呼――啊――喘――喘不過氣――呼、啊！」 / Cũ: 「Hà! Kyu――ư――phù――hà―― / Thở――khó――thở quá――phù, a!」 / Mới: 「Hà! Kyu――ư――phù――hà―― / Thở――thở――khó thở quá――Fua, a!」 — (1) いきっ、いきっ、くるしっ bị xáo: いき=thở, くるしい=khó thở — cũ gán "khó" cho いき thứ hai và "thở quá" cho くるしっ, ngược nhau; (2) ふあっ→"Fua".
- **2297** [日々姫] JP: 「ぷあっ！　あっ！　あっ――ふ、あっ――ああ―― / は――ああ……ふあ――あっ――」 / TW: 「噗哈！啊！啊――呼、啊――啊啊――呼――啊……呼――啊――」 / Cũ: 「Phù! A! A――phù, a――a―― / Hà――a……phù――a――」 / Mới: 「Pua! A! A――phù, a――a―― / Hà――a……Fua――a――」 — (1) ぷあっ = "pua" (ぷ=P, không phải Ph — MOAN-BRIEF); (2) ふあ→"Fua"; giữ "phù, a" cho ふ、あっ tách dấu phẩy.
- **2298** [日々姫] JP: 「ぷはっ！　ごちそーさま！　補給完了！」 / TW: 「噗哈！喝飽了！補充完畢！」 / Cũ: 「Phù! Cảm ơn anh! Tiếp nước hoàn tất!」 / Mới: 「Puha! Cảm ơn anh! Tiếp nước hoàn tất!」 — ぷはっ = "puha", "Phù" mất mora は.
- **2364** [日々姫] JP: 「おまんこ――おまん、この、おなか、の、方の―― / ん――ふあっ！　あ――ゆび、にいに、の、ゆび、の」 / TW: 「小穴――小穴的，靠肚子的一面――嗯――呼！啊――手指、阿哥的、手指」 / Cũ: 「Âm đạo――âm, đạo, ở phía, bụng―― / Ưm――phù! A――Ngón tay, của anh hai, ngón tay」 / Mới: 「Âm đạo――âm, đạo, ở phía, bụng―― / Ưm――Fua! A――Ngón tay, của anh hai, ngón tay」.
- **2709** [日々姫] JP: 「に――にぃにの――ンッ――くい、こんで―― / きて――ふあっ――あっ……くっ――ふぅっ」 / TW: 「阿――阿哥――嗯――陷進來了――呼啊――啊……唔――呼」 / Cũ: 「A――Của anh hai――ưm――lún sâu, vào―― / rồi――phù――a……hự――phù」 / Mới: 「A――Của anh hai――ưm――lún sâu, vào―― / rồi――Fua――a……hự――phù」 — giữ "phù" cuối = ふぅっ (hơi thở dài, đúng).
- **2711** [日々姫] JP: 「にぃ――に――こ、れっ……んっ――フッ―― / ふあっ――あっ――んくっ！」 / TW: 「阿――阿哥――這樣……嗯――呼――呼啊――啊――嗯！」 / Cũ: 「A――anh――Thế, này……ưm――Phù―― / Phù a――a――ưm hự!」 / Mới: 「A――anh――Thế, này……ưm――Phù―― / Fua――a――ưm hự!」 — giữ "Phù" = フッ (hơi thở, đúng).
- **2751** [日々姫] JP: 「おちん、ちんっ――ふあっ――だめ――つきあげ、 / らて、てっ――おなかっ、おさ、れてっ――は、あっ」 / TW: 「雞雞――呼――不行――被頂到――肚子裡、被壓到――呼、啊」 / Cũ: 「Chim――phù――không được――bị thúc lên, / thế này――bụng, bị ép, vào――hà, a」 / Mới: 「Chim――Fua――không được――bị thúc lên, / thế này――bụng, bị ép, vào――hà, a」.
- **2266** [日々姫] JP: 「ふきゅっ！？　ンッ――くぅんんんんんっっっっ！」 / TW: 「嗯呀！？　嗯――唔嗯嗯嗯！」 / Cũ: 「Fukyu!? Ưm――Kuuunnnn!」 / Mới: 「Fukyu!? Ưm――KuunnnnnƯƯƯƯ!」 — くぅ = 2 u (cũ 3 u, thừa 1); ん×5 (cũ 4 n, thiếu 1); っ×4 cuối dòng → Ư×4 theo quy tắc đa-っ (tiền lệ 2201 っっっ→ƯƯƯ, 2767 っっ→ƯƯ).
- **2085** [日々姫] JP: 「やぁっ！　おちんちん！　にげちゃ、やぁなのっ」 / TW: 「呀！雞雞！不要跑！」 / Cũ: 「A! Chim kìa! Đừng có, chạy đi mà」 / Mới: 「Yaa! Chim kìa! Đừng có, chạy đi mà」 — やぁっ = "yaa" (2 a); "A" mất phụ âm y — tiền lệ ポーレットh3: "Á" cho やっ là lỗi mất phụ âm. やぁなのっ → "Đừng có" (diễn nghĩa từ chối, giữ).
- **2028** [日々姫] JP: 「もっと、奥ぅっ――おまんこ、の、おくっ―― / 指じゃ、ぜったい、とどかない――とこっ――にぃ」 / TW: 「再深一點――小穴的、深處――手指――搆不到的地方――」 / Cũ: 「Sâu, hơn nữa――sâu bên trong, âm đạo―― / Chỗ mà, ngón tay, tuyệt đối không chạm tới được――ấy」 / Mới: 「Sâu, hơn nữa――sâu bên trong, âm đạo―― / Chỗ mà, ngón tay, tuyệt đối không chạm tới được――anh…」 — にぃ cuối dòng là gọi "anh hai" bị cắt ngang (tiền lệ 2248 にぃ、に→"Anh, hai"); "ấy" là từ đệm, mất tiếng gọi.

### 2d. Nguyên âm (9)

Đếm cơ học từ CSV3 (không đếm bằng mắt): số nguyên âm VN phải bằng số âm tiết nguyên âm JP.

- **2078 — PARENT LOẠI (không sai, đã xóa khỏi fix list):** JP 「きゅっ！　ふぅぅぅぅぅぅぅぅぅぅぅぅぅんっ！」 / TW 「呀！呼嗯！」 / Cũ: 「Kyu! Fuuuuuuuuuuuuuun!」 (14 u) — ĐÚNG theo công thức (ふ 1u + ぅ×13 = 14 u). Agent đếm nhầm ぅ×12 → sửa thành 13 u (sai). Fix list còn 50 mục.
- **2109** [日々姫] JP: 「はあぁっ――はっ――ふううううううっ！！！」 / TW: 「呼啊――哈――呼唔唔！！！」 / Cũ: 「Haaa――hà――fuuuuuu!!!」 (6 u) / Mới: 「Haaa――hà――fuuuuuuu!!!」 (7 u) — JP: ふ 1u + う×6 = 7 u. はあぁっ→"Haaa" (3 a) đã đúng.
- **2196** [日々姫] JP: 「ふやぁぁぁぁぁぁぁぁぁぁんっ！！！！」 / TW: 「啊呀嗯！！！！」 / Cũ: 「Fuyaaaaaaaaaan!!!!」 (10 a) / Mới: 「Fuyaaaaaaaaaaan!!!!」 (11 a) — JP: や 1a + ぁ×10 = 11 a.
- **2199** [日々姫] JP: 「ああああ――あっ！　きたっ――きてるっ、 / にぃにの、ちんちん――あっ――わたし、おまんこ」 / TW: 「啊啊啊――啊！來了――插進來了。阿哥的、雞雞――啊――插進了、我的小穴」 / Cũ: 「Aaaaa――a! Đến rồi――đang vào rồi, / Chim của, anh hai――a――âm đạo, của em」 (5 a) / Mới: 「Aaaa――a! Đến rồi――đang vào rồi, / Chim của, anh hai――a――âm đạo, của em」 (4 a).
- **2202** [日々姫] JP: 「ああああああっ！」 / TW: 「啊啊啊啊啊！」 / Cũ: 「Aaaaa!」 (5 a) / Mới: 「Aaaaaa!」 (6 a) — JP 6 a.
- **2203** [日々姫] JP: 「ああああ！」 / TW: 「啊啊啊！」 / Cũ: 「Aaaaa!」 (5 a) / Mới: 「Aaaa!」 (4 a) — JP 4 a. (2202/2203 cùng VN cũ "Aaaaa!" dù JP khác nhau — bằng chứng đếm sai.)
- **2190** [日々姫] JP: 「ああっ――ンッ――こ、れ――おっっぱい―― / おっぱい、も――足、に、こすれ、てッ――あっ」 / TW: 「啊――嗯――這樣――胸部――胸部也――跟腿摩擦――啊」 / Cũ: 「A――ưm――Thế, này――Ngực―― / Ngực, cũng――cọ xát, vào chân――a」 / Mới: 「Aa――ưm――Thế, này――Ngực―― / Ngực, cũng――cọ xát, vào chân――a」 — ああっ 2 a, cũ 1 a.
- **2080** [日々姫] JP: 「ひゃっ！　あっ！　あ、あ、あ、あっ！　また、 / ねっ！　にぃに、また、わたし、また、またぁ」 / TW: 「呀！啊！啊、啊、啊、啊！又要、那個！阿哥、我、又要、又要」 / Cũ: 「Hyaa! A! A, a, a, a! Lại, / nữa! Anh hai, lại nữa, em, lại, lại nữa rồi」 / Mới: 「Hya! A! A, a, a, a! Lại, / nữa! Anh hai, lại nữa, em, lại, lại nữa rồi」 — ひゃっ 1 a; っ cuối moan ngắn là ẩn (MOAN-BRIEF 3b), không thêm 'a'.
- **2713** [日々姫] JP: 「にぃ、に――んっ――くううう～～ん――ふ、あっ / すと……レッチ、も――いい、けど――よか、けどっ」 / TW: 「阿哥――嗯――唔唔唔～～嗯――呼、啊，伸……伸展運動――做的差不多了吧」 / Cũ: 「Anh, hai――ưm――kuuu~~n――phù, a / Khởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」 / Mới: 「Anh, hai――ưm――kuuuu~~n――phù, a / Khởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」 — くううう 4 u, cũ 3 u.

### 2e. Sai nghĩa (3)

- **2015** [双鉄] JP: 「うけるかどうかはともかく、ありえんはわかるな。 / 僕の産まれた町でも、帝都でも、これはなかった」 / TW: 「先不說是不是有趣，我知道他們為什麼不相信。不管是我出生的地方，還是在帝都，都沒有這種事情」 / Cũ: 「Chưa bàn đến chuyện đỉnh hay không, nhưng không thể tin được thì anh hiểu. / Ngay cả ở thị trấn nơi anh sinh ra, hay ở Đế đô, cũng không có chuyện này」 / Mới: 「Chưa bàn đến chuyện buồn cười hay không, nhưng không thể tin được thì anh hiểu. / Ngay cả ở thị trấn nơi anh sinh ra, hay ở Đế đô, cũng không có chuyện này」 — うける = buồn cười/thú vị (TW 有趣), "đỉnh" (tuyệt vời) sai nghĩa.
- **2362** [日々姫] JP: 「そ！　『うける～！　ありえ～～ん！』って」 / TW: 「對啊！他們都說“好有意思，不可能吧”」 / Cũ: 「Đúng rồi! Tụi nó bảo là 『Đỉnh thật! Không thể tin được!』」 / Mới: 「Đúng rồi! Tụi nó bảo là 『Buồn cười thật! Không thể tin được!』」 — cùng lỗi うける→"đỉnh".
- **2457** [日々姫] JP: 「せいり……うんどう」 / TW: 「整理……運動」 / Cũ: 「Vận động……thả lỏng」 / Mới: 「Thả lỏng……vận động」 — hai nửa bị đảo: せいり (整理 = thả lỏng/cool-down) → "Thả lỏng", うんどう (運動 = vận động) → "vận động". TW giữ đúng thứ tự.

### 2f. Thuật ngữ (1)

- **1985** [双鉄] JP: 「速く走る、というタイプではないだろう。 / 整備体のハチロク、れいなも同様だな」 / TW: 「但她不是跑得很快的那種。八六跟玲奈的整備體也差不多」 / Cũ: 「Nhưng không phải tuýp người chạy nhanh đúng không. / Cơ thể bảo trì của Hachiroku và Reina cũng vậy」 / Mới: 「Nhưng không phải tuýp người chạy nhanh đúng không. / Thân bảo trì của Hachiroku và Reina cũng vậy」 — 整備体 = "thân bảo trì" (đã quyết); "Cơ thể bảo trì" sai thuật ngữ. Viết hoa "Thân" vì đầu câu.

## 3. Sweep kiểm chứng

- Sweep có 10 mục cho file: nhận 9 fix (1418, 2201, 2241, 2759, 2761, 2767, 2982, 3414, 3421 — JP/TW/old_vn khớp CSV3, giá trị áp nguyên; 2767 đã đếm 12 ~ khớp).
- 1 mục sweep nhãn "already-rendered" là SAI, audit tự sửa: 2282 (xem §2b — っ cuối dòng う～～っ mất hoàn toàn).
- Sweep bỏ sót 3 gasp, audit tự tìm: 1427, 2185, 2764 (xem §2b). Quét máy bổ sung toàn bộ dòng JP chứa っ — không còn gasp nào sót ngoài 4 dòng trên.
- Họ ひゃ/ひゅ/ひあ/きゃ: 0 dòng dùng "Á" — toàn bộ đã romaji đúng (Hyaaaaan, Kyafuuuuun, Hyuan, Hyaa→Hya sau sửa, Kyafu, Hyan, Hyaaa, Kya, hyu). 2226 ひゃくにじゅうさん là từ số (123), không phải moan.
- Họ fa/fu "phù" tách âm (ふ、あっ / ふ……ぁ → "phù, a" / "Phù……a": 1944, 2106, 2194, 2713) giữ nguyên — hai âm tách dấu câu, không phải một âm ふあ; để vòng moan phán xét.
- "Hà" cho はぁっ (2035, 2098, 2118) giữ nguyên theo tiền lệ đã gộp (1565, 2152: "Hà" là cách diễn hơi thở đã chốt, không đếm lại).
- Tiếng cười えへへ (2143, 2144, 2145, 2146) giữ nguyên "Ehehe" — cười là ngẫu hứng theo nhân vật, không đếm số へ.
- SFX miệng bằng tiếng Việt (ちゅっ→"chụt", ちゅむっ→"chùn chụt", びゅっ→"Phụt", ぐっ→"Thúc/Đâm") giữ nguyên — quy ước nhất quán trong file, TW cũng diễn nghĩa.

## 4. Giữ nguyên, ghi nhận đợt thống nhất (12 dòng)

- 御一夜 "Ohimitera" → "Ohitoyo" — 6 dòng: 2258, 2309, 2442, 2589, 3039, 3698.
- 宮司 "cha xứ/Cha xứ Akai" → "đền chủ" — 2 dòng: 1415 (「赤井宮司っ！！」), 3002.
- 遅刻温泉 "Chikoku" — 2 dòng (2348, 3605) đã nhất quán, không đổi.
- Không có 日ノ本, 電車姫, まいてつ, Migita trong file.

## 5. Đã kiểm tra, không sai (ghi chú đáng kể)

- 2511: JP gốc chứa `\\マーク` (2 dấu backslash — do ￥/0x5C Shift-JIS chuyển mã); VN "ký hiệu ￥" là ĐÚNG (câu đố xác nhận: 1950/1953, 3012 hộp 『￥』, 3045 ￥マーク ở checkpoint 1). Không sửa.
- 1932 「足りたか？　不足ならもう一本」→ "anh mua thêm chai nữa": "mua" là suy ra từ ngữ cảnh (quầy đồ uống ở hội thao), không phải bịa ý mới — giữ.
- 2744 ちらっ → "Hé mở!": đang mở phong bì (ngữ cảnh + TW 「我拉」) — giữ.
- 2746 thứ tự từ đảo trong lời nói ngắt quãng (「仕切ると。今年も。ねぇねぇが」→"Năm nay. Chị cả cũng. Đứng ra tổ chức") — nghĩa giữ nguyên, giữ.
- 3109 隈銀 + gloss "(Ngân hàng Kumamoto)": giải thích đúng chữ viết tắt — giữ. 1415 『Hanao (Quai dép)』, 2214 "Okashi (Bánh kẹo)", 2231 "Ema (Tấm gỗ cầu nguyện)", 2222 "Knight (Hiệp sĩ)": gloss đúng — giữ.
- 1980/2222 "Bác ấy" (người chỉ cờ vua / cho xem quân Knight): TW xác nhận "他" (người đàn ông lớn tuổi) — giữ.
- 38 (ぐいっ！）→ "(Kéo ra!)": SFX hành động diễn bằng nghĩa — giữ.
- 2070 がっ → "sẽ": theo TW 「就」 — giữ. 2082 てっっ → "này", 2074 けどぉっ → "nhưng mà": っ nhấn mạnh trên từ nội dung, không phải gasp — giữ.
- 2296 うふふふっ → "Ufufufu" (cười, không phải rên) — giữ. 2405 ひ、あ → "Hi, a" (tách âm, đúng).
- 2182 ちゅうううだ → "chụt": quy ước "chụt" đã chốt cho họ ちゅう — giữ (vòng moan phán xét nếu cần).
- 3712/3714 びゅううううっ → "Phụt": SFX tiếng Việt đã chốt cho họ びゅ — giữ.
- 1435, 1968, 2019, 2024, 2037, 2048, 2058, 2066, 2234, 2255, 2292, 2329, 2344, 2363, 2411, 2439, 2471, 2476, 2500, 2511, 2526, 2544, 2557, 2623, 2666, 2697, 2714, 2717, 2719, 2725, 3205 (TW sai, JP thắng: tay Hibiki siết lại), 3237, 3386, 3425, 3445, 3470, 3528, 3605, 3625 — đã đọc kỹ, không sai.

## 6. Lượt soát 2

- Tổng 51 / tái kiểm chứng 50 / bỏ 0 / sửa 1 (1985: "thân bảo trì" → "Thân bảo trì" — viết hoa đầu câu, phát hiện ở lượt 2, đã sửa và chạy lại toàn bộ kiểm chứng máy).
- **Parent kiểm chứng 21/11 ~14:40 (đếm nguyên âm độc lập từ JP): 2075 sửa 7u→6u (ふ 1u + う×5); 2078 LOẠI khỏi fix list (VN cũ 14 u đã đúng: ふ 1u + ぅ×13; agent đếm nhầm ぅ×12). Sau sửa parent: 50 mục. Kiểm chứng máy chạy lại: JSON 50 mục, khối TOML 50 khóa, 0 sai lệch; jp/tw/old_vn khớp CSV3 tuyệt đối 50/50.**
- Kiểm chứng máy (sau sửa): JSON 50 mục (key string, dạng list-of-dicts chuẩn); khối TOML 50 khóa, 0 sai lệch giá trị; jp/tw/old_vn khớp CSV3 tuyệt đối 50/50; old_vn khớp TOML-2 (trừ làm phẳng `\n`) 50/50; mỗi fix chỉ khác old_vn ở đúng chỗ thay đổi mục tiêu.

## 7. Khối TOML (đã kiểm chứng parse)

```toml
[script]
1418 = "「――Ư」"
1426 = "「――ưm――hà――ưm――Fua! A!\\nAnh hai! Không được――hỏng mất――em, hi」"
1427 = "「Ư――!」"
1985 = "「Nhưng không phải tuýp người chạy nhanh đúng không.\\nThân bảo trì của Hachiroku và Reina cũng vậy」"
2015 = "「Chưa bàn đến chuyện buồn cười hay không, nhưng không thể tin được thì anh hiểu.\\nNgay cả ở thị trấn nơi anh sinh ra, hay ở Đế đô, cũng không có chuyện này」"
2028 = "「Sâu, hơn nữa――sâu bên trong, âm đạo――\\nChỗ mà, ngón tay, tuyệt đối không chạm tới được――anh…」"
2075 = "「Kyafuuuuun! A! Trong, bụng――\\nBị nhồi nhét――chim――mở rộng ra――Fua」"
2077 = "「Hyuan!? A, anh hai――khoan, đợi đã!\\nHà――Fua――a! A! Aaaa」"
2080 = "「Hya! A! A, a, a, a! Lại,\\nnữa! Anh hai, lại nữa, em, lại, lại nữa rồi」"
2084 = "「Yaaa! Ưm――Thế này――em――Fua!\\nCơ thể――sức lực――bị rút cạn――nhũn ra, mất」"
2085 = "「Yaa! Chim kìa! Đừng có, chạy đi mà」"
2102 = "「Hà――Fua, a――Căng đầy, mở rộng ra――ưm\\nPhù――a, bụng em, âm đạo em, đầy ắp, rồi」"
2109 = "「Haaa――hà――fuuuuuuu!!!」"
2111 = "「Fua――a, nóng quá, nóng quá đi」"
2112 = "「Fua」"
2114 = "「Faaaaaaa――aa――Chỗ đó, em thích, lắm\\nƯm――Hơn cả, chỗ đó, nữa cơ――nhưng mà, hơn nữa cơ」"
2116 = "「Fua!? A! Anh hai, nè? Chỗ đó, ấy?\\nChim――nhiều hơn nữa――cọ xát, cọ xát, đi anh」"
2117 = "「Fan!!!」"
2122 = "「Fa! A! Sướng quá, sướng quá đi――\\nƯm! Chỗ đó, em thích, âm đạo, sắp tan chảy, ra rồi」"
2124 = "「Fua! A! Bắn rồi! Nóng, quá!\\nNhơm nhớp, tử cung――bị chạm vào――đọng lại rồi!」"
2138 = "「Ể――từ từ――ưm……hự――\\nHà, a――ưm――Fua!」"
2182 = "「A――Fua――a――Hôn――chụt,\\nhôn em, đi――chụt」"
2184 = "「A――phù――ưm――Fua――\\nTo quá――nóng, quá――hơn, mọi khi」"
2185 = "「A――hà――ưm! Ưm ưm ưm~~Ư! Hà, hyu,\\nChỗ, đó――bị ngoáy――Hông, không được, nhũn ra mất!!」"
2190 = "「Aa――ưm――Thế, này――Ngực――\\nNgực, cũng――cọ xát, vào chân――a」"
2196 = "「Fuyaaaaaaaaaaan!!!!」"
2199 = "「Aaaa――a! Đến rồi――đang vào rồi,\\nChim của, anh hai――a――âm đạo, của em」"
2201 = "「ƯƯƯ!!!」"
2202 = "「Aaaaaa!」"
2203 = "「Aaaa!」"
2210 = "「Hà! Kyu――ư――phù――hà――\\nThở――thở――khó thở quá――Fua, a!」"
2241 = "「A――ư ư ư~~Ư」"
2266 = "「Fukyu!? Ưm――KuunnnnnƯƯƯƯ!」"
2282 = "「Vâng, chỉ cần lúc về đích hai người ở cùng nhau là được――\\nÁ! Không――không phải! Ưm――ư~~Ư」"
2297 = "「Pua! A! A――phù, a――a――\\nHà――a……Fua――a――」"
2298 = "「Puha! Cảm ơn anh! Tiếp nước hoàn tất!」"
2362 = "「Đúng rồi! Tụi nó bảo là 『Buồn cười thật! Không thể tin được!』」"
2364 = "「Âm đạo――âm, đạo, ở phía, bụng――\\nƯm――Fua! A――Ngón tay, của anh hai, ngón tay」"
2457 = "「Thả lỏng……vận động」"
2709 = "「A――Của anh hai――ưm――lún sâu, vào――\\nrồi――Fua――a……hự――phù」"
2711 = "「A――anh――Thế, này……ưm――Phù――\\nFua――a――ưm hự!」"
2713 = "「Anh, hai――ưm――kuuuu~~n――phù, a\\nKhởi……động, thì――cũng tốt, thôi――tốt, thôi nhưng」"
2751 = "「Chim――Fua――không được――bị thúc lên,\\nthế này――bụng, bị ép, vào――hà, a」"
2759 = "「Ư!」"
2761 = "「Ư!!?」"
2764 = "「~~~~~ƯƯ!! Kua! Aaaaa! Ưm,\\nChỗ đó, chỗ chỉ dành, cho chim――thích lắm」"
2767 = "「~~~~~~~~~~~~ƯƯ!!!!」"
2982 = "Trong lúc đó, những người tham gia khác,\\nđã lần lượt lấy phong bì và mở ra――Ư!!?"
3414 = "Hibiki móc ngón tay vào cổ áo, kéo nhẹ xuống một chút.\\nKhe ngực mỏng manh và độ phồng của bầu ngực liền phơi bày ra toàn bộ――Ư!"
3421 = "Hibiki rướn người tới trước――Ư!!?"
```

- Lưu ý cơ sở tổng: task giao cơ sở 158 file / 7.033 dòng sai, nhưng trong lúc audit, loop đã gộp グランドリライト06_稀咲 (+70) — ROUTE-AUDIT.md hiện tại là **159 file / 7.103 dòng sai**. Snippet dùng cơ sở mới này (tổng sau file này: 160 file / 7.154 dòng sai).

## Kết bài

File 日々姫h6 (667 dòng) đọc hết từng dòng với JP + TW: **50 dòng sai (7,5%)** — gasp 13, moan 25, nguyên âm 8, sai nghĩa 3, thuật ngữ 1. Không lệch vị trí, không chuỗi xoay, không nhiễm chéo, không mồ côi, không chưa dịch, không trùng khóa. Sweep áp nguyên 9/10 mục; 1 nhãn "already-rendered" của sweep là sai (2282) và sweep bỏ sót 3 gasp (1427, 2185, 2764) — cả 4 đã sửa trong audit. Lỗi nặng nhất tập trung ở H-scene: họ fa/fu diễn "phù" mất nguyên âm 'a' (22 dòng) và đếm nguyên âm sai ở chuỗi "A"/romaji dài (8 dòng, trong đó 2202/2203 cùng VN cũ "Aaaaa!" dù JP 6a/4a). Đại từ Soutetsu đúng toàn file ("anh" với Hibiki, "tôi" trong độc thoại). Ghi nhận đợt thống nhất 12 dòng: 御一夜 "Ohimitera" 6, 宮司 "cha xứ" 2, còn lại đã nhất quán. Chi tiết đầy đủ: `audit-hibikih6-orienteering-karimono-wrong.json` (50 mục sau khi parent loại 2078, khối TOML 50 khóa, 0 sai lệch, jp/tw/old_vn khớp CSV3 tuyệt đối 50/50; lượt soát 2: 51/50/0/1; parent sửa 2075 + loại 2078).
