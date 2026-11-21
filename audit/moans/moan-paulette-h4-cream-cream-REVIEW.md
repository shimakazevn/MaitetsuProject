# Moan-fix REVIEW — ポーレットh4_クリーム＆クリーム.txt.toml

## 1. Xác minh file

- File: `ポーレットh4_クリーム＆クリーム.txt.toml` — route 03_Paulette, 265 dòng script.
- Disk: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/03_Paulette/#U30dd#U30fc#U30ec#U30c3#U30c8h4_#U30af#U30ea#U30fc#U30e0#Uff06#U30af#U30ea#U30fc#U30e0.txt.toml`
- TOML md5: `64abe8098966360371870067cd0d2843`. Không có bản trùng TOML.
- CSV3: **1 bộ duy nhất** (`translation_toml\03_Paulette\ポーレットh4_クリーム＆クリーム.txt.toml`), 265 dòng. TOML vs CSV3: 265/265 khóa có mặt; 146 dòng chỉ khác ở chỗ TOML-2 làm phẳng `\n` literal thành khoảng trắng (mẫu đã biết — CSV3 là chuẩn cho danh sách sửa). Bộ tốt đã xác minh bằng flat-match.
- Audit: file này đã audit xong, 23 dòng sai (`audit-paulette-h4-cream-and-cream-wrong.json`). Trùng với moan-fix: **11 khóa** (859, 881, 882, 884, 901, 903, 906, 911, 914, 952, 970). Trong đó 10 khóa là fix "romanisation" của audit (chuyển romaji về VN) — vòng moan xem xét lại theo quy tắc romaji (Hieu duyệt 21/11) và sửa/hủy phần lớn (xem từng dòng dưới). 906 chỉ trùng ở đại từ (audit), token rên do moan sửa.
- Sweep gasp: 4 mục cho file này (1030, 1632, 941 — đã sửa bằng sweep/audit, không đụng; 896 — loại "already-rendered", không sửa). 1010 (っ đứng riêng) và 932 (～っ) sweep KHÔNG bao phủ — xem cờ F5.

## 2. Kiểm kê rên (moan inventory)

- Đã đọc **265/265 dòng**. Xét **123 dòng rên/SFX**: 83 dòng thoại có âm rên/SFX + 40 dòng SFX trong ngoặc （ ）.
- **Sửa 44 dòng, giữ 79 dòng.**
- Không có dòng cười (ふふっ/うふふ/んふふ) nào trong file. 914/970 là nói ngọng (garbled speech), không phải rên — chỉ sửa token rên, giữ nguyên phần ngọng của audit.
- Phân loại 44 dòng sửa (một dòng có thể mang 2 token):
  - Họ fa/fu → romaji (Fua/Fuya/Funyaa/Fuhya/Pua): 18 dòng (859, 879, 901, 903, 906, 908, 910, 911, 914, 915, 934, 947, 950, 952, 963, 970, 1008, 1010).
  - Họ ひゃ/ひゅ/ひあ/きゃ → romaji (Hya/Hyu/Hia/Kya/Nhyu...): 12 dòng (859, 873, 885, 887, 889, 891, 903, 912, 960, 961, 963, 969).
  - Họ ん+phụ âm / ん+nguyên âm dài → romaji gộp (Nkyu/Nmyu/Na/An/Nuu/Nuuuuuu...): 13 dòng (859, 873, 884, 896, 912, 936, 950, 952, 961, 963, 965, 969, 1008).
  - やっ → "Ya" (mất phụ âm y): 4 dòng (879, 926, 960, 1010).
  - Họ ちゅ → romaji (Chumu/Churo/Churu/Chuu/Chubu/Muchu): 6 dòng (930, 932, 945, 947, 1576, 1579).
  - Mất phụ âm đầu khác (Kaha/Ka/Kua/Gaa/Ua/Ihyu/Kahyu): 876, 889, 893, 903, 904, 912, 961.
  - Đếm nguyên âm (sửa số lượng theo công thức): 8 dòng (881: 12→11u; 901: 1→2a; 908: Hà→Haa; 911: 10→11a + thêm n; 932/896: phù→Phùu; 970: 1→2a; 1008: 11→12a).
  - Thứ tự / đổi loại: 892 (đổi chỗ 2 token), 896/921 (くっ "Ư"→"Hự"), 1010 (っ đứng riêng → thêm Ư).
  - Hủy fix audit (giá trị moan = VN cũ): 882, 884 (xem §3).

## 3. Từng dòng sửa (44 dòng)

### Key 859 (ポーレット)
- JP: `「ひゃにっ？！　ひえっ！？　ま、まだっ――\nんきゅ！　ふあっ――あっ――あっ――んひゅっ！」`
- TW: `「什麼？！哎！？又、又來了——嗯！呼啊——啊——啊——嗯！」`
- VN cũ: `「Cái gì?! Hả!? V, vẫn còn——\nNkyu! Phù——a——a——ưm hya!」`
- Sửa: `「Cái gì?! Hả!? V, vẫn còn——\nNkyu! Fua——a——a——Nhyu!」`
- Lý do: ふあっ→"phù" sai nguyên âm (phải là Fua); んひゅっ→"ưm hya" tách một âm thành hai mảnh VÀ sai âm (ひゅ≠ひゃ) → "Nhyu" (quy tắc 3b). Khôi phục "Nkyu!" của VN cũ — audit đổi thành "Ưm!" làm mất phụ âm kyu (hủy fix audit).

### Key 873 (ポーレット)
- JP: `「ひゃっ――あっ――おまんこっ――きたっ――\n精液っ――あついっ――あついのっ――んひゅっ！？」`
- TW: `「呀——啊——射到——小穴裡了——精液——好燙——好燙——嗯啊！」`
- VN cũ: `「Hya——a——cô bé——đến rồi——\nTinh dịch——nóng quá——nóng quá——ưm hya!?」`
- Sửa: `「Hya——a——cô bé——đến rồi——\nTinh dịch——nóng quá——nóng quá——Nhyu!?」`
- Lý do: んひゅっ→"ưm hya" tách một âm thành hai mảnh VÀ sai âm (ひゅ≠ひゃ) → "Nhyu". ひゃっ→"Hya" giữ nguyên (đúng).

### Key 876 (ポーレット)
- JP: `「ひ――あっ――おひりっ――んっ――わたしの――\nおしり――ぺろぺろって――そうてつ、くん、がぁっ」`
- TW: `「呀——啊——屁股——嗯——我的——屁股——被舔到了——雙鐵」`
- VN cũ: `「Hí——a——mông——ưm——của em——\nMông——đang bị liếm——anh Soutetsu, a」`
- Sửa: `「Hii——a——mông——ưm——của em——\nMông——đang bị liếm——anh Soutetsu, Gaa」`
- Lý do: ひ―― là "hii" dài (ー kéo dài i) → "Hii" (VN cũ 1 i, mất độ dài); がぁっ→"a" mất phụ âm g → "Gaa" (が+ぁ = 2 a).

### Key 879 (ポーレット)
- JP: `「やっ――ンッ――ゆるん――じゃう、っ――\nわたし――おしりっ――ゆるめ、られ、てっ――ふあっ」`
- TW: `「呀——嗯——變鬆了——我的——屁股——被鬆開了——呼啊」`
- VN cũ: `「Á——ưm——lỏng——ra mất, rồi——\nEm——mông——bị làm cho lỏng, ra——phù」`
- Sửa: `「Ya——ưm——lỏng——ra mất, rồi——\nEm——mông——bị làm cho lỏng, ra——Fua」`
- Lý do: やっ→"Á" mất phụ âm y (tiền lệ h3: "Á" cho やっ là lỗi mất phụ âm) → "Ya"; ふあっ→"phù" sai nguyên âm → "Fua".

### Key 881 (ポーレット)
- JP: `「きゃふううううううううううっっ！！！」`
- TW: `「呀啊啊啊啊啊！！！」`
- VN cũ: `「Kyafuuuuuuuuuuuu!!!」`
- Sửa: `「Kyafuuuuuuuuuuu!!!」`
- Lý do: đếm sai — JP ふ+う×10 = 11 u, VN cũ 12 u → sửa thành 11 u. Đồng thời hủy fix audit ("KyaphùùùùùùùùùùùƯƯ!!!") — audit chuyển romaji về VN "phù" + thêm ƯƯ cho っっ; theo quy tắc romaji + っ cuối rên romaji là ngầm định (tiền lệ h7), giữ romaji, không thêm Ư.

### Key 882 (ポーレット) — HỦY fix audit
- JP: `「きゃふあっ！？」`
- TW: `「呀啊！？」`
- VN cũ: `「Kyafua!?」`
- Sửa: `「Kyafua!?」` (= VN cũ)
- Lý do: VN cũ đã đúng (romaji thuần). Audit đổi thành "KyaphùaƯ!?" — vừa trộn romaji "Kya" + VN "phùa" trong MỘT âm (vi phạm "một âm = một cách diễn"), vừa thêm Ư cho っ cuối rên (double-render). Giá trị moan = VN cũ → hủy fix audit ở đợt thống nhất.

### Key 884 (ポーレット) — HỦY fix audit
- JP: `「んきゅっ！！」`
- TW: `「呀！！」`
- VN cũ: `「Nkyu!!」`
- Sửa: `「Nkyu!!」` (= VN cũ)
- Lý do: VN cũ đã đúng ("Nkyu" = romaji chính xác của んきゅっ). Audit đổi thành "Ưm!!" làm mất phụ âm kyu. Giá trị moan = VN cũ → hủy fix audit.

### Key 885 (ポーレット)
- JP: `「ひゃんっ！？」`
- TW: `「呀！？」`
- VN cũ: `「Á!?」`
- Sửa: `「Hyan!?」`
- Lý do: ひゃんっ→"Á" mất cả phụ âm hy lẫn n (lỗi mất âm, quy tắc 3b) → "Hyan". Đối chiếu 883 cùng file: ひゃんっ→"Hyan!" đã đúng.

### Key 887 (ポーレット)
- JP: `「ひゃううっ！？　んっ――あっ――\nこれっ――んっ――すごく――きもちいいっ！」`
- TW: `「呀！？嗯——啊——這樣——嗯——好舒服！」`
- VN cũ: `「Hyaau!? Ưm——a——\nThế này——ưm——sướng——quá!」`
- Sửa: `「Hyauu!? Ưm——a——\nThế này——ưm——sướng——quá!」`
- Lý do: ひゃううっ: う sau ひゃ đọc là "u", không phải "a" (tiền lệ h7 811/812: ひゃう×8 → "Hyau"+u) → "Hyauu" (1 a + 2 u), không phải "Hyaau" (2 a + 1 u).

### Key 889 (ポーレット)
- JP: `「いひゅっ！？　んっ――あっ――入って――\nうっ――べろ――ベロっ――べろぉっ」`
- TW: `「呀！？嗯——啊——進來了——唔——舌頭——舌頭——舌頭」`
- VN cũ: `「Í!? Ưm——a——vào rồi——\nƯ——lưỡi——lưỡi——lưỡi」`
- Sửa: `「Ihyu!? Ưm——a——vào rồi——\nƯ——lưỡi——lưỡi——lưỡi」`
- Lý do: いひゅっ→"Í" mất hoàn toàn âm ひゅ → "Ihyu" (romaji, quy tắc 3b). うっ→"Ư" giữ (ư ≈ u, đúng). べろぉっ→"lưỡi" giữ (từ có nghĩa, xem §4).

### Key 891 (ポーレット)
- JP: `「ひあっ！？　子宮っ――んっ――押されっ――てっ」`
- TW: `「呀！？子宮——被壓到了——」`
- VN cũ: `「Hya!? Tử cung——ưm——bị ấn, vào——rồi」`
- Sửa: `「Hia!? Tử cung——ưm——bị ấn, vào——rồi」`
- Lý do: ひあっ≠ひゃっ — ひあ là "hia" (hi+a riêng), không phải "hya" → "Hia" (tiền lệ 凪h2: ひあ "Hya"→"Hia" ×5).

### Key 892 (双鉄H)
- JP: `「くっ――っ――」`
- TW: `「呃——啊——」`
- VN cũ: `「Ư——hự——」`
- Sửa: `「Hự——Ư——」`
- Lý do: thứ tự token bị đảo — JP くっ trước, っ sau; VN cũ "Ư" (cho っ trần) trước, "hự" (cho くっ) sau. Đổi lại đúng thứ tự: くっ→"Hự", っ→"Ư". Đối chiếu 951 cùng file: っ――くっ―― → "Ư——hự——" đã đúng thứ tự.

### Key 893 (双鉄H)
- JP: `「っ――ぅあっ！？」`
- TW: `「呃——啊！？」`
- VN cũ: `「Ư——á!?」`
- Sửa: `「Ư——Ua!?」`
- Lý do: ぅあっ→"á" mất âm ぅ (u nhỏ dẫn) → "Ua" (romaji: ぅ+あ).

### Key 896 (ポーレット)
- JP: `「ふっ――ンッ――んみゅっ――んっ――\nくっ――ふっ――ふうっ――っっっっっっ～～っ！！！」`
- TW: `「呼——嗯——嗯唔——嗯——唔——呼——呼——嗯嗯嗯～～！！！」`
- VN cũ: `「Phù——ưm——ưm——ưm——\nƯ——phù——phù——ư ư ư ư ư ư～～!!!」`
- Sửa: `「Phù——ưm——Nmyu——ưm——\nHự——phù——Phùu——ư ư ư ư ư ư～～!!!」`
- Lý do: んみゅっ→"ưm" mất hoàn toàn みゅ → "Nmyu" (romaji gộp, tiền lệ h7: んむっ→"Nmu"); くっ→"Ư" sai loại âm (Ư dành cho っ trần; くっ có phụ âm k) → "Hự" (cách diễn grunt của chính file này, 951/894); ふうっ→"phù" sai đếm (ふ+う = 2 u) → "Phùu". Chuỗi っ cuối giữ nguyên theo quyết định của sweep (already-rendered, không sửa — xem cờ F7).

### Key 901 (ポーレット)
- JP: `「は……あっ――ふにゃあっ――」`
- TW: `「呼……啊——呼喵——」`
- VN cũ: `「Hà……a——funya——」`
- Sửa: `「Hà……a——Funyaa——」`
- Lý do: ふにゃあっ = ふ+にゃ+あ = 2 a; VN cũ "funya" chỉ 1 a → "Funyaa". Đồng thời hủy phần "phunyaaƯ" của audit (trộn "ph" VN + romaji + Ư cho っ cuối rên — っ ngầm định, không thêm Ư).

### Key 903 (ポーレット)
- JP: `「ふやんっ――くあっ――んっ――ひうっ――んっ！」`
- TW: `「呼啊——啊——嗯——呀——嗯！」`
- VN cũ: `「Phuyan——a——ưm——hí——ưm!」`
- Sửa: `「Fuyan——Kua——ưm——Hiu——ưm!」`
- Lý do: ふやんっ→"Fuyan" (tiền lệ h7 809: ふや→"Fuya" romaji f; hủy Ư audit thêm cho っ cuối rên); くあっ→"a" mất cả ku → "Kua"; ひうっ→"hí" mất âm u cuối → "Hiu" (ひ+う).

### Key 904 (ポーレット)
- JP: `「かはっ――あっ――んっ――ふあっ――\nおひ、りっ――んっ――アナルっ――がっ――」`
- TW: `「呼啊——啊——嗯——呼啊——屁股——嗯——屁眼——」`
- VN cũ: `「Hà——a——ưm——phù——\nMông——ưm——lỗ hậu——đang——」`
- Sửa: `「Kaha——a——ưm——Fua——\nMông——ưm——lỗ hậu——Ga——」`
- Lý do: かはっ→"Hà" mất phụ âm k → "Kaha"; ふあっ→"phù" sai nguyên âm → "Fua"; がっ→"đang" là bịa từ (が là tiểu từ, không phải "đang") → "Ga" (romaji, giữ âm).

### Key 906 (双鉄H)
- JP: `「ぷあっ――あっ――ポーレット――\n好きだ――愛してる――大好きだっ」`
- TW: `「呼啊——啊——波萊特——我喜歡你——我愛你——我好愛你」`
- VN cũ: `「Phù——a——Paulette——\nAnh thích em——Anh yêu em——Yêu em nhiều lắm.」`
- Sửa: `「Pua——a——Paulette——\nTôi thích em——Tôi yêu em——Yêu em nhiều lắm.」`
- Lý do: ぷあっ→"Phù" sai cả phụ âm lẫn nguyên âm (pu+a → "Pua"). Giá trị moan = giá trị audit ("Tôi thích em" — fix đại từ của audit được giữ, chỉ đổi token rên).

### Key 908 (ポーレット)
- JP: `「はぁっ――あっ――えぐっって――ふあっ――\nおまん、こっ――めりって――めくれて――んうっ」`
- TW: `「呼啊——啊——被挖到了——呼啊——小穴——攪到了裡面——攪到了——嗯」`
- VN cũ: `「Hà——a——bị ngoáy sâu——phù——\nCô bé——đang——bị nong ra——bị lộn ra——ưm」`
- Sửa: `「Haa——a——bị ngoáy sâu——Fua——\nCô bé——đang——bị nong ra——bị lộn ra——ưm」`
- Lý do: はぁっ = は+ぁ = 2 a → "Haa" (VN cũ 1 a); ふあっ→"phù" sai nguyên âm → "Fua". んうっ→"ưm" giữ (xem §4).

### Key 910 (ポーレット)
- JP: `「ふあっ――うれしっ――ん――そうてつ、くっ――\nすきっ――すきっ――すきっ――すきぃっ――」`
- TW: `「呼啊——我好開心——嗯——雙鐵——我喜歡你——喜歡你——喜歡你——」`
- VN cũ: `「Phù——vui quá——ưm——anh Soutetsu——\nThích anh——thích anh——thích anh——thích anh lắm——」`
- Sửa: `「Fua——vui quá——ưm——anh Soutetsu——\nThích anh——thích anh——thích anh——thích anh lắm——」`
- Lý do: ふあっ→"phù" sai nguyên âm → "Fua".

### Key 911 (ポーレット)
- JP: `「ふやああああああああああんっ！！」`
- TW: `「呼啊啊啊啊啊！！」`
- VN cũ: `「Phuyaaaaaaaaaa!!」`
- Sửa: `「Fuyaaaaaaaaaaan!!」`
- Lý do: đếm sai + mất âm — JP ふや+あ×10+ん = 11 a + n; VN cũ 10 a, không có n → "Fuy"+11a+"n" (kiểm chứng bằng script). Hủy Ư của audit (っ cuối rên romaji ngầm định). "Fuy" theo tiền lệ h7 809 (ふや→"Fuya").

### Key 912 (ポーレット)
- JP: `「かひゅっ！　ふっ――んっ――んううううううっ！」`
- TW: `「呼啊！啊——嗯——嗯啊啊！」`
- VN cũ: `「Hya! Phù——ưm——ưm ư ư ư ư ư!」`
- Sửa: `「Kahyu! Phù——ưm——Nuuuuuu!」`
- Lý do: かひゅっ→"Hya" mất phụ âm k → "Kahyu"; んううううううっ (ん+う×6) VN cũ diễn bằng 6 token "ưm ư ư..." rời rạc, đọc ngượng → romaji "Nuuuuuu" (6 u, đếm đã kiểm chứng).

### Key 914 (ポーレット)
- JP: `「ふひゃっ――そうへふ、ふん――\nわらひ、ひあわへれ……のほへちゃいまひはぁ」`
- TW: `「呼喵——雙鐵——我幸福得……暈過去啦」`
- VN cũ: `「Fuhya——anh Houhehu——\nEm, hạnh phúh quá……nên hỉu mấh rồi」`
- Sửa: `「Fuhya——anh Hôu-hê-hu——\nEm, hạnh phúh quá……nên hỉu mấh rồi」`
- Lý do: ふひゃっ→"Fuhya" (VN cũ đã đúng; hủy fix audit "PhùhyaƯ" — trộn VN+romaji trong một âm + thêm Ư). Phần nói ngọng giữ nguyên giá trị audit ("Hôu-hê-hu") — chỉ đổi token rên.

### Key 915 (ポーレット)
- JP: `「ふあっ！？　あっ――シャワー――精液っ――ンッ\n――精液、シャワー――びゅっびゅ、しな、がらっ」`
- TW: `「哇！？啊——下雨了——精液做的雨——精液做的雨——射了出來」`
- VN cũ: `「Phù!? A——mưa rào——tinh dịch——ưm\n——Tinh dịch, như mưa rào——phụt phụt, tuôn, trào」`
- Sửa: `「Fua!? A——mưa rào——tinh dịch——ưm\n——Tinh dịch, như mưa rào——phụt phụt, tuôn, trào」`
- Lý do: ふあっ→"Phù" sai nguyên âm → "Fua".

### Key 921 (双鉄H)
- JP: `「くっ――んっ」`
- TW: `「唔——嗯」`
- VN cũ: `「Ư——ưm」`
- Sửa: `「Hự——ưm」`
- Lý do: くっ→"Ư" sai loại âm (Ư dành cho っ trần; くっ có phụ âm k) → "Hự" (cách diễn grunt của chính file này, 951/894).

### Key 926 (ポーレット)
- JP: `「ァッ――やっ――おしり――でっ――んっ――\n双鉄、くんっ――わた、しっ――アナル――でっ！」`
- TW: `「啊——呀——用屁股——嗯——雙鐵君——在用——我的屁股！」`
- VN cũ: `「Á——á——bằng mông——ưm——\nAnh Soutetsu——em——bằng lỗ hậu——!」`
- Sửa: `「Á——Ya——bằng mông——ưm——\nAnh Soutetsu——em——bằng lỗ hậu——!」`
- Lý do: やっ→"á" mất phụ âm y → "Ya". ァッ→"Á" giữ (あ trần, không có phụ âm mora — "Á" đúng).

### Key 930 (ポーレット)
- JP: `「あっ――あむっ――んっ――ちゅっ――ちゅるっ――\nちゅむっ――んんっ――ふあっ――むちゅっ」`
- TW: `「啊——啊唔——嗯——啾——啾嚕——啾噗——嗯——呼啊——啾嚕」`
- VN cũ: `「A——ngoạm——ưm——chụt——chu——\nchụt——ưm——phù——chụt」`
- Sửa: `「A——ngoạm——ưm——chụt——Churu——\nChumu——ưm——Fua——Muchu」`
- Lý do: ちゅるっ→"chu" mất る → "Churu"; ちゅむっ→"chụt" mất む (diễn thành ちゅっ) → "Chumu"; ふあっ→"phù" sai nguyên âm → "Fua"; むちゅっ→"chụt" mất む → "Muchu". ちゅっ→"chụt" giữ (dạng VN chuẩn cho hôn).

### Key 932 (ポーレット)
- JP: `「～っ――んっ！　んっ――ちゅっ――ちゅむうっ――\nんっ――ふうっ――れるっ――れろっ――れろおおっ」`
- TW: `「啊——嗯！嗯――啾嚕――啾噗――嗯——呼——啾嚕——啾嚕——啾噗」`
- VN cũ: `「～——ưm! Ưm——chụt——chụtttt——\nƯm——phù——liếm——liếm——liếmmmm」`
- Sửa: `「～——ưm! Ưm——chụt——Chumuu——\nƯm——Phùu——liếm——liếm——liếmmmm」`
- Lý do: ちゅむうっ→"chụtttt" mất む và kéo dài sai chữ (t thay vì u) → "Chumuu" (ちゅ+む+う: chu+mu+u, 3 u tổng); ふうっ→"phù" sai đếm (2 u) → "Phùu". ～っ đầu dòng giữ nguyên "～" (xem cờ F5).

### Key 934 (ポーレット)
- JP: `「あっ――あつっ――いっ――んっ――ふあっ――\nふと、い――のにっ――ぬるって――ちゅるっ、って」`
- TW: `「啊——好燙——咿——嗯——呼啊——明明這麼粗——卻是滑滑的——」`
- VN cũ: `「A——nóng——quá——ưm——phù——\nTo, thế——mà——lại trơn——tuột」`
- Sửa: `「A——nóng——quá——ưm——Fua——\nTo, thế——mà——lại trơn——tuột」`
- Lý do: ふあっ→"phù" sai nguyên âm → "Fua". いっ→"quá" giữ (lựa chọn dịch tự nhiên, không phải lỗi âm).

### Key 936 (ポーレット)
- JP: `「あっ――手っ――双鉄くんの、おてて――んうっ――\nぬるぬる――して、てっ――おっきく、て――あんっ」`
- TW: `「啊——手——雙鐵君——你的手——嗯——濕濕的——大大的——啊」`
- VN cũ: `「A——tay——tay của anh Soutetsu——ưm——\nTrơn trượt——quá——to, quá——a」`
- Sửa: `「A——tay——tay của anh Soutetsu——ưm——\nTrơn trượt——quá——to, quá——An」`
- Lý do: あんっ→"a" mất ん → "An" (a+n). んうっ→"ưm" giữ.

### Key 945 (ポーレット)
- JP: `「ちゅっ――ちゅむっ――ちゅっ――ん――ぷあっ――\nだからっ――くださいッ――わたし――わたしにっ――」`
- TW: `「啾——啾嚕——啾——嗯——呼啊——所以——給我吧——給我吧」`
- VN cũ: `「Chụt——chu——chụt——ưm——phù——\nNên là——hãy cho em——em——cho em——」`
- Sửa: `「Chụt——Chumu——chụt——ưm——Pua——\nNên là——hãy cho em——em——cho em——」`
- Lý do: ちゅむっ→"chu" mất む → "Chumu"; ぷあっ→"Phù" sai cả phụ âm lẫn nguyên âm → "Pua".

### Key 947 (ポーレット)
- JP: `「ちゅっ――ちゅむっ――ちゅうっ――ちゅぶっ――\nぷあっ――んっ――ぺろっ――ちゅううっ―ちゅろっ」`
- TW: `「啾噗——啾嚕——啾嚕——啾噗——呼啊——嗯——啾噗——啾嚕——啾噗」`
- VN cũ: `「Chụt——chu——chụtttt——chu——\nPhù——ưm——liếm——chụtttt——chụt」`
- Sửa: `「Chụt——Chumu——Chuu——Chubu——\nPua——ưm——liếm——Chuuu——Churo」`
- Lý do: ちゅむっ→"Chumu" (mất む); ちゅうっ→"Chuu" (2 u; "chụtttt" kéo dài sai chữ t); ちゅぶっ→"Chubu" (mất ぶ); ぷあっ→"Pua"; ちゅううっ→"Chuuu" (3 u); ちゅろっ→"Churo" (mất ろ). ちゅっ→"chụt" giữ.

### Key 950 (ポーレット)
- JP: `「んっ――ふあ――あっ――あんっ！」`
- TW: `「嗯——呼——啊——嗯！」`
- VN cũ: `「Ưm——phù——a——a!」`
- Sửa: `「Ưm——Fua——a——An!」`
- Lý do: ふあ (không っ) →"phù" sai nguyên âm → "Fua"; あんっ→"a!" mất ん → "An!".

### Key 952 (ポーレット)
- JP: `「んきゅっ――あっ――ふあっ――んうっ――\nあなる――おしりっ――なかっ――ぐりって――んっ」`
- TW: `「嗯——啊——呼啊——嗯——屁眼——屁股——裡面——被鑽到了——嗯」`
- VN cũ: `「Nkyu——a——phù——ưm——\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」`
- Sửa: `「Nkyu——a——Fua——ưm——\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」`
- Lý do: ふあっ→"phù" sai nguyên âm → "Fua". Khôi phục "Nkyu" — audit đổi thành "Ưm" (mất kyu); giá trị moan giữ "Nkyu" của VN cũ.

### Key 960 (ポーレット)
- JP: `「んひぃぃぃ――すっちゃ。、やっ――んっ――\nわたしの、アナルっ――吸ったら、ダメ、なのぉ」`
- TW: `「嗯呀——不要——吸啦——嗯——不要吸——我的屁眼」`
- VN cũ: `「Ưm ááá——mút. Không——ưm——\nLỗ hậu, của em——đừng, mút, mà」`
- Sửa: `「Nhyiiii——mút. Ya——ưm——\nLỗ hậu, của em——đừng, mút, mà」`
- Lý do: んひぃぃぃ→"Ưm ááá" tách một âm thành hai mảnh VÀ sai âm (ひぃぃぃ là "hiiii", không phải "á") → "Nhyiiii" (ん+ひ+ぃ×3 = 4 i); やっ→"Không" diễn âm thành từ, mất tiếng → "Ya" (tiền lệ h3).

### Key 961 (ポーレット)
- JP: `「んひゅ――かっ――んうううううううっ！！？」`
- TW: `「嗯呀——啊——嗯啊啊啊！！？」`
- VN cũ: `「Ưm hya——á——ưm ư ư ư ư ư ư!!?」`
- Sửa: `「Nhyu——Ka——Nuuuuuuu!!?」`
- Lý do: んひゅ→"Ưm hya" tách một âm thành hai mảnh VÀ sai âm (ひゅ≠ひゃ) → "Nhyu"; かっ→"á" mất phụ âm k → "Ka"; んうううううううっ (ん+う×7) VN cũ diễn bằng 7 token "ưm ư ư..." rời rạc, đọc ngượng → romaji "Nuuuuuuu" (7 u, đếm đã kiểm chứng).

### Key 963 (ポーレット)
- JP: `「んひゅっ――やっ――えっ！？　キスっ――んっ――\n双鉄、くんが――わたしの――ふあっ――アナル、にっ」`
- TW: `「嗯唔——呀——哎！？親上了——嗯——雙鐵君——你親上了——呼啊——我的屁眼——」`
- VN cũ: `「Ưm——á——hả!? Hôn——ưm——\nAnh Soutetsu——đang——phù——vào lỗ hậu, của em」`
- Sửa: `「Nhyu——Ya——hả!? Hôn——ưm——\nAnh Soutetsu——đang——Fua——vào lỗ hậu, của em」`
- Lý do: んひゅっ→"Ưm" mất ひゅ → "Nhyu"; やっ→"á" mất y → "Ya"; ふあっ→"phù" sai nguyên âm → "Fua". えっ→"hả!?" giữ (cảm thán VN tự nhiên).

### Key 965 (ポーレット)
- JP: `「んあっ！　ひゃっ――おっぱい――にゅる、って――」`
- TW: `「嗯！呀――胸部——彈彈的——」`
- VN cũ: `「Ưm a! Hya——ngực——trơn tuột, mất——」`
- Sửa: `「Na! Hya——ngực——trơn tuột, mất——」`
- Lý do: んあっ→"Ưm a" tách một âm "na" thành hai mảnh → "Na". ひゃっ→"Hya" giữ (đúng).

### Key 969 (ポーレット)
- JP: `「ひゅごっ――いっ――これっ――んううっ――あっ、\nぉまん――こっ――ひうっ――いっぱい――いっぱいぃ」`
- TW: `「好厲害——這樣——嗯——啊——小穴裡——嗯——填滿了」`
- VN cũ: `「Tuyệt——quá——thế này——ưm——a,\nCô bé——đang——hí——đầy——đầy ứ」`
- Sửa: `「Tuyệt——quá——thế này——Nuu——a,\nCô bé——đang——Hiu——đầy——đầy ứ」`
- Lý do: んううっ (ん+う×2) →"ưm" mất độ dài (1 ư thay vì 2 u) → "Nuu"; ひうっ→"hí" mất âm u cuối → "Hiu". ひゅごっ→"Tuyệt" giữ (nói lắp của すごい, xem §4).

### Key 970 (ポーレット)
- JP: `「ひゃい……ほーへふふん……ふにゃあ」`
- TW: `「好呀……嘿嘿……呼喵」`
- VN cũ: `「Vâng ạ……anh Houhehu……funya」`
- Sửa: `「Vâng ạ……Hừm hừm hừm……Funyaa」`
- Lý do: ふにゃあ = ふ+にゃ+あ = 2 a; VN cũ "funya" chỉ 1 a → "Funyaa" (romaji f, như 901). Phần nói ngọng giữ nguyên giá trị audit ("Hừm hừm hừm") — chỉ đổi token rên.

### Key 1008 (ポーレット)
- JP: `「いっ――くっ――んあっ――あっ――あっ――\nふあっ――――ああああああああああああっ！！！」`
- TW: `「要丟了——嗯——啊——啊——呼啊——啊啊啊啊啊！！！」`
- VN cũ: `「Ra——mất——a——a——a——\nPhù————A a a a a a a a a a a!!!」`
- Sửa: `「Ra——mất——Na——a——a——\nFua————A a a a a a a a a a a a!!!」`
- Lý do: んあっ→"a" mất ん → "Na"; ふあっ→"Phù" sai nguyên âm → "Fua"; chuỗi あ cuối: JP 12 あ, VN cũ 11 a → thêm 1 a (12 a, giữ kiểu tách khoảng trắng của bản cũ). いっ――くっ→"Ra——mất" giữ (từ rút gọn của いく).

### Key 1010 (ポーレット)
- JP: `「やっ――やすませっ――ひっ――ふやっ――っ――\nおまんこっ、あつくてっ――やけどっ――しちゃっうっ」`
- TW: `「讓、讓我喘口氣——咿——啊——啊——小穴——太燙了——要燒傷了」`
- VN cũ: `「Đừng——cho em nghỉ——hí——phù——\nCô bé, nóng quá——sắp bỏng——mất rồi」`
- Sửa: `「Ya——cho em nghỉ——hí——Fuya——Ư——\nCô bé, nóng quá——sắp bỏng——mất rồi」`
- Lý do: やっ→"Đừng" diễn âm thành từ, mất tiếng → "Ya"; ふやっ→"phù" sai nguyên âm (phải là Fuya); っ đứng riêng giữa ふやっ và おまんこっ bị mất hoàn toàn trong VN → thêm "Ư" (gasp đứng riêng, tiền lệ h7 816 giữ Ư gasp của audit cho っ đứng riêng; sweep không bao phủ dòng này — xem cờ F5). ひっ→"hí" giữ (ひ ngắn, 1 âm).

### Key 1576 (monologue)
- JP: `（ちゅむっ――）`
- TW: `（啾噗）`
- VN cũ: `（Chụt——）`
- Sửa: `（Chumu——）`
- Lý do: ちゅむっ→"Chụt" mất む (diễn thành ちゅっ) → "Chumu".

### Key 1579 (monologue)
- JP: `（ちゅむっ――ちゅっ――ちゅろっ――ちゅううっ）`
- TW: `（啾嚕——啾噗——啾嚕——啾噗）`
- VN cũ: `（Chu——chụt——chụt——chụtttt）`
- Sửa: `（Chumu——chụt——Churo——Chuuu）`
- Lý do: ちゅむっ→"Chumu" (mất む); ちゅろっ→"Churo" (mất ろ); ちゅううっ→"Chuuu" (3 u; "chụtttt" kéo dài sai chữ t). ちゅっ→"chụt" giữ.

## 4. Ghi chú dòng rên GIỮ (không sửa)

- **Đã đúng romaji từ đầu:** 883 ひゃんっ→"Hyan!"; 880 ひゃあぁ→"Hyaaa" (3 a đúng); 871 ひぁっ→"Hya" (ひぁ = glide "hya" — khác với ひあっ→"Hia"); 878 ひゃふっ→"Hyafu", あひっ→"ahi"; 882/884 romaji cũ đúng (audit đổi sai — đã hủy, §3).
- **Ưm cho âm mũi:** 895 んふっ→"ưm" giữ — ふ ở đây là hơi thở nhẹ, "ưm" là tiếng ưm mũi đã có sẵn trong file (đối chiếu h7 F2: んぷっ giữ "Ưm"); 1572 （むっ）→"（Ưm）" giữ (m còn nguyên); 952/908/936 んうっ→"ưm" giữ (âm mũi ngắn, không kéo dài).
- **Grunt "hự":** 951/894 くっ→"hự" giữ; 954 むっ→"hự" giữ — "hự" là cách diễn grunt chung của file cho Soutetsu (xem cờ F1: Ku vs Hự vs Ư vẫn mở, theo h7 F1).
- **ふっ→"phù":** 937/896/912 giữ — h7 F7 ("phù" vs "Fu") vẫn mở, không quyết ở đây; chỉ sửa đếm cho ふうっ→"Phùu" (896, 932).
- **Lựa chọn dịch (không phải lỗi âm):** 934/969/851 いっ→"quá", よおっ→"anh ơi" (gọi tên); 899 でっ→"đi anh"; 937 あのっ→"chuyện đó"; 889 べろぉっ→"lưỡi" (từ có nghĩa, độ dài rơi nhưng từ còn nguyên); 969 ひゅごっ→"Tuyệt" (nói lắp của すごい); 982 くぅんっ→"anh Soutetsu" (tên).
- **SFX trong ngoặc diễn thành động từ/tính từ VN:** "Phập", "Phụt", "Siết", "Nắn bóp", "Trơn tuột", "Liếmmmm", "Chà", "vò", "Cọ xát", "Ngoáy" — kiểu nhất quán cả file, giữ. Kể cả các âm dài kéo dài phụ âm cuối ("Trơn tuộtttttt" 1618, "Siếtttttt" 1596, "Liếmmmmm" 1624, "Ngoáyyyyyyy" 1638, "Phậppppppp" 1617) — cách kéo dài kiểu VN, giữ.
- **Sweep/audit đã sửa, không đụng:** 941 「っ!」→"Ư!" (sweep raw-tsu + audit gasp); 1030 ～...っ→"～Ư!!" (sweep lost-gasp-trailing + audit); 1632 っ cuối độc thoại → thêm Ư (sweep + audit).
- **1594 ちゅるっ→"chụt" giữ** — cụm SFX trong ngoặc diễn theo kiểu VN (đối chiếu 930 "Churu" trong thoại; xem cờ F4).
- **896 chuỗi っ cuối (6 ư vs 7 っ):** giữ theo quyết định của sweep (already-rendered, không sửa — xem cờ F7).

## 5. Cờ cho đợt thống nhất

- **F1 — họ く Ku vs Hự vs Ư** (mở, theo h7 F1): file này dùng "hự" cho grunt của Soutetsu (951/894/954 giữ); 896/921/892 sửa "Ư"→"Hự" cho くっ. Cần quyết chung một dạng.
- **F2 — ん+phụ âm: romaji gộp vs "Ưm"** (mở, theo h7 F2): file này giữ "ưm" cho んふっ (895) nhưng dùng romaji cho んひゅ/んきゅ/んみゅ/んあ. Cần quyết chung.
- **F3 — ふっ "phù" vs "Fu"** (mở, theo h7 F7): giữ "phù" ở đây, không quyết.
- **F4 — họ ちゅ "chụt" vs "Chuu/Chumu" vs h3 "chụụt/chumu"** (mở, theo h7 F5): file này: ちゅっ thuần→"chụt", ちゅ+âm thêm→romaji; riêng 1594 ちゅるっ→"chụt" giữ trong cụm SFX ngoặc.
- **F5 — gasp っ sweep chưa bao phủ:** (a) 1010 っ đứng riêng → đã thêm "Ư" ở đây (phán đoán: っ trần đứng riêng, mất hoàn toàn, tiền lệ h7 816) — cần xác nhận lại theo quy tắc gasp ở đợt thống nhất. (b) 932 ～っ đầu dòng giữ nguyên "～" — đối chiếu tiền lệ sweep 1030 (thêm Ư sau chuỗi ～) — cần quyết có thêm "～Ư" hay không.
- **F6 — 897 きちゃう→"chạm vào" là lỗi nghĩa, KHÔNG sửa ở đây** (moan-only): きちゃう = "sắp ra", VN "chạm vào mất" sai nghĩa. Audit cũng không sửa dòng này — cần vòng audit chú ý.
- **F7 — 896 chuỗi っ cuối: 6 ư vs 7 っ** — sweep ghi "already-rendered", giữ nguyên. Nếu đợt thống nhất muốn đếm đủ thì sửa thành 7 ư.
- **F8 — 10 fix "romanisation" của audit bị moan sửa/hủy** (859, 881, 882, 884, 901, 903, 911, 914, 952, 970): giá trị moan THAY THẾ giá trị audit cho các khóa này ở đợt thống nhất (đặc biệt 882/884: giá trị moan = VN cũ, tức hủy fix audit).
- **F9 — họ ふ: "F" (romaji) vs "ph" (VN):** file này theo tiền lệ h7 809 (ふや→"Fuya", ふあ→"Fua", ふにゃ→"Funyaa", ふひゃ→"Fuhya", ぷあ→"Pua"); quy tắc khóa của audit brief nói ふやぁ→"phuya". Đợt thống nhất cần chọn một cách viết cho cả họ ふ (903/911/1010 đã đổi Ph→F).
- **F10 — 1594 vs 930:** cùng âm ちゅるっ, hai cách diễn ("chụt" trong SFX ngoặc vs "Churu" trong thoại) — cần quyết có thống nhất không.

## 6. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 44 giá trị fix đối chiếu JP (+TW) sau khi viết xong: **tổng 44 / tái kiểm chứng 44 / bỏ 0 / sửa 0.**
- Đếm nguyên âm kiểm chứng độc lập bằng script (sau lượt soát 2): 881 "Kyaf"+11u; 911 "Fuy"+11a+"n"; 1008 đuôi 12 a; 961 "Nuuuuuuu" 7u; 912 "Nuuuuuu" 6u; 969 "Nuu" 2u; 960 "Nhyiiii" 4i; 887 "Hyauu" 1a+2u — tất cả khớp JP.
- JSON 44 mục, khóa string, jp/tw/old_vn khớp CSV3 44/44 (1 bộ duy nhất, 265 dòng).
- Khối TOML parse bằng tomllib: 44 khóa, 0 sai lệch giá trị.

## 7. Khối TOML (parse-verified)

```toml
[script]
"859" = "「Cái gì?! Hả!? V, vẫn còn——\\nNkyu! Fua——a——a——Nhyu!」"
"873" = "「Hya——a——cô bé——đến rồi——\\nTinh dịch——nóng quá——nóng quá——Nhyu!?」"
"876" = "「Hii——a——mông——ưm——của em——\\nMông——đang bị liếm——anh Soutetsu, Gaa」"
"879" = "「Ya——ưm——lỏng——ra mất, rồi——\\nEm——mông——bị làm cho lỏng, ra——Fua」"
"881" = "「Kyafuuuuuuuuuuu!!!」"
"882" = "「Kyafua!?」"
"884" = "「Nkyu!!」"
"885" = "「Hyan!?」"
"887" = "「Hyauu!? Ưm——a——\\nThế này——ưm——sướng——quá!」"
"889" = "「Ihyu!? Ưm——a——vào rồi——\\nƯ——lưỡi——lưỡi——lưỡi」"
"891" = "「Hia!? Tử cung——ưm——bị ấn, vào——rồi」"
"892" = "「Hự——Ư——」"
"893" = "「Ư——Ua!?」"
"896" = "「Phù——ưm——Nmyu——ưm——\\nHự——phù——Phùu——ư ư ư ư ư ư～～!!!」"
"901" = "「Hà……a——Funyaa——」"
"903" = "「Fuyan——Kua——ưm——Hiu——ưm!」"
"904" = "「Kaha——a——ưm——Fua——\\nMông——ưm——lỗ hậu——Ga——」"
"906" = "「Pua——a——Paulette——\\nTôi thích em——Tôi yêu em——Yêu em nhiều lắm.」"
"908" = "「Haa——a——bị ngoáy sâu——Fua——\\nCô bé——đang——bị nong ra——bị lộn ra——ưm」"
"910" = "「Fua——vui quá——ưm——anh Soutetsu——\\nThích anh——thích anh——thích anh——thích anh lắm——」"
"911" = "「Fuyaaaaaaaaaaan!!」"
"912" = "「Kahyu! Phù——ưm——Nuuuuuu!」"
"914" = "「Fuhya——anh Hôu-hê-hu——\\nEm, hạnh phúh quá……nên hỉu mấh rồi」"
"915" = "「Fua!? A——mưa rào——tinh dịch——ưm\\n——Tinh dịch, như mưa rào——phụt phụt, tuôn, trào」"
"921" = "「Hự——ưm」"
"926" = "「Á——Ya——bằng mông——ưm——\\nAnh Soutetsu——em——bằng lỗ hậu——!」"
"930" = "「A——ngoạm——ưm——chụt——Churu——\\nChumu——ưm——Fua——Muchu」"
"932" = "「～——ưm! Ưm——chụt——Chumuu——\\nƯm——Phùu——liếm——liếm——liếmmmm」"
"934" = "「A——nóng——quá——ưm——Fua——\\nTo, thế——mà——lại trơn——tuột」"
"936" = "「A——tay——tay của anh Soutetsu——ưm——\\nTrơn trượt——quá——to, quá——An」"
"945" = "「Chụt——Chumu——chụt——ưm——Pua——\\nNên là——hãy cho em——em——cho em——」"
"947" = "「Chụt——Chumu——Chuu——Chubu——\\nPua——ưm——liếm——Chuuu——Churo」"
"950" = "「Ưm——Fua——a——An!」"
"952" = "「Nkyu——a——Fua——ưm——\\nLỗ hậu——mông——bên trong——bị ngoáy——ưm」"
"960" = "「Nhyiiii——mút. Ya——ưm——\\nLỗ hậu, của em——đừng, mút, mà」"
"961" = "「Nhyu——Ka——Nuuuuuuu!!?」"
"963" = "「Nhyu——Ya——hả!? Hôn——ưm——\\nAnh Soutetsu——đang——Fua——vào lỗ hậu, của em」"
"965" = "「Na! Hya——ngực——trơn tuột, mất——」"
"969" = "「Tuyệt——quá——thế này——Nuu——a,\\nCô bé——đang——Hiu——đầy——đầy ứ」"
"970" = "「Vâng ạ……Hừm hừm hừm……Funyaa」"
"1008" = "「Ra——mất——Na——a——a——\\nFua————A a a a a a a a a a a a!!!」"
"1010" = "「Ya——cho em nghỉ——hí——Fuya——Ư——\\nCô bé, nóng quá——sắp bỏng——mất rồi」"
"1576" = "（Chumu——）"
"1579" = "（Chumu——chụt——Churo——Chuuu）"
```

Kết bài
