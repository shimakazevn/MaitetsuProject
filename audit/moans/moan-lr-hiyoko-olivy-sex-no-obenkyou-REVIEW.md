# Moan-fix REVIEW — lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml

## 1. Xác minh file

- File: `lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml` — route 11_Other (lr追加, Olivy học về sex với Hiyoko + Momiji), 441 dòng script.
- Disk: `~/workspace/maitetsu-pilot/sources/toml2/translation_toml/11_Other/lr#U8ffd#U52a0_#U3072#U3088#U3053#U96fb#U8eca#U59eb#U30aa#U30ea#U30f4#U30a3#U300c#U30bb#U30c3#U30af#U30b9#U306e#U304a#U52c9#U5f37#U300d.txt.toml`
- TOML md5: `bdb02933933db615a0380eb3839cd6de`. Không có bản trùng TOML.
- CSV3: **1 bộ duy nhất** (`translation_toml\\11_Other\\lr追加_ひよこ電車姫オリヴィ「セックスのお勉強」.txt.toml`), 441 dòng, 0 trùng khóa. TOML vs CSV3: 441/441 khóa có mặt; các dòng nhiều đoạn chỉ khác ở chỗ TOML-2 làm phẳng `\\n` literal thành khoảng trắng (mẫu đã biết — CSV3 là chuẩn cho danh sách sửa).
- Audit: file này đã audit xong, 22 dòng sai (`audit-lr-olivy-hiyoko-wrong.json`). Trùng với moan-fix: **2 khóa** (2331, 2426). 2331: audit sửa token cuối "phụt"→"phù ah" (ぷあっ) — moan sửa tiếp thành "Pua" theo quy tắc romaji fallback (ghi đè audit, xem key 2331). 2426: audit thêm "Ư" cho っっ và sửa đếm chuỗi きゅ thành 13u đúng — moan GIỮ cả hai, chỉ đổi token いっ "Ư"→"I" (xem key 2426). Không có key nào moan-fix hủy toàn bộ fix audit.
- Sweep gasp: 6 mục cho file này — 1301/1554/1591/1925/2099 (lost-gasp, đã sửa bằng sweep/audit) và 2166 (needs-file-audit, audit đã xử lý: thêm Ư) — tất cả đã do audit sửa, moan KHÔNG đụng. 2146 (っっ――→"ư——") và 2426 (っっ) sweep không bao phủ riêng, nhưng giá trị Ư đã có sẵn/khớp audit nên giữ nguyên.
- Không có dòng "Kh" cho っ nào bị đổi: 1887/2449 か……→"Ka" và 2238/1804 くっ→"Ku" là âm か/く đầy đủ (có nguyên âm), không phải っ trần — khác với 5 dòng "Kh" khóa của ふかみh2 (989/997/1017/1731/1739).

## 2. Kiểm kê rên (moan inventory)

- Đã đọc **441/441 dòng** (CSV3 bộ tốt + đối chiếu TOML). Xét **~160 dòng rên/SFX** (đếm tay từ lần đọc đầy đủ).
- **Sửa 55 dòng, giữ ~105 dòng.**
- Phân loại 55 dòng sửa (một dòng có thể mang 2 token):
  - Họ fa/fu → romaji (Fua/Fuaa/Fuaaa/Fuaaaaaa/Pua): 19 dòng (875, 899, 1359, 1368, 1527, 1556, 1697, 2094, 2145, 2146, 2159, 2238, 2279, 2331, 2334, 2346, 2422, 2457, 2458).
  - Họ ひゃ/ひゅ/ひあ/きゃ/や → romaji (Hya/Hyu/Hia/Kya/Nhyu/Ya/Yaa/Hyagu/Hyai): 9 dòng (1368, 1428, 1542, 1655, 1802, 2422, 2428, 2435, 2438).
  - Họ ん+phụ âm / ん+nguyên âm dài → romaji gộp (Nku/Nchu/Nkyu/Nkyun/Nuu/Nuuuu/Nfuuuuuu/Fuuuuun): 9 dòng (1354, 1426, 1433, 1481, 1519, 2247, 2434, 2452, 2460).
  - Họ ちゅ/れる/じゅ/ごちゅ (âm miệng/lưỡi trong thoại) → romaji (Chumu/Chuu/Chubu/Reru/Rero/Jubu/Jururuu/Zuji/Buchu/Gochu/Pechu): 7 dòng (1370, 1527, 2146, 2184, 2247, 2331, 2098).
  - くっ → "Ku" (mất phụ âm k / mất nguyên âm u): 7 dòng (1710, 1804, 2168, 2220, 2234, 2238, 2428).
  - か…… → "Ka" (mất nguyên âm a): 2 dòng (1887, 2449); いっ → "I" (mất nguyên âm i): 1 dòng (2426).
  - Đếm nguyên âm (sửa số lượng theo công thức, giữ dạng VN): 4 dòng (1409: 1→4a; 1424: 3→2a; 1773: phù 1→2u + Ahhh 3→2a; 2343: tách mảnh + 3a).
  - Dài ふうう → "Fuuu" (3u): 2 dòng (2084, 2342) — đã tính trong nhóm romaji/đếm.
- Kiểu lỗi chính: bản cũ tách MỘT âm rên thành nhiều mảnh ("phù ah", "Ư hiu", "Ưm ư ư ư ư", "chụt ưm"), mất phụ âm mora (くっ→"ư", やっ→"Ư", いっ→"Ư", か→"Kh"), và sai đếm nguyên âm ("Ahhh" cho 2a, "Cứuu…" cho 13u).

## 3. Từng dòng sửa (55 dòng)

### Key 875 (ひよこ)
- JP: `「ふあっ――ん……あ。オリヴィ、氏」`
- TW: `——這是在電視中能看到的成年人的接吻。她們就跟情侶一樣，吻得十分投入。`
- VN cũ: `「Phù ah——ưm……a. Cô Olivy」`
- Sửa: `「Fua——ưm……a. Cô Olivy」`
- Lý do: ふあっ→"Phù ah" tách một âm thành hai mảnh, ngượng → "Fua" (romaji fallback, Hieu duyệt 21/11).

### Key 899 (monologue)
- JP: `「わ――すごい……伸びてる……ふ、ぁ――電車姫さま\\n――もうひとつ、穴――オリヴィには無い穴があるんだ」`
- TW: `「……唔——呼——」`
- VN cũ: `「Oa——tuyệt quá……nó giãn ra kìa……phù, ah——Công chúa Tàu điện\\n——còn một lỗ nữa——có một cái lỗ mà Olivy không có.」`
- Sửa: `「Oa——tuyệt quá……nó giãn ra kìa……Fua——Công chúa Tàu điện\\n——còn một lỗ nữa——có một cái lỗ mà Olivy không có.」`
- Lý do: ふ、ぁ→"phù, ah" tách một âm thành hai mảnh → "Fua".

### Key 1354 (ひよこ)
- JP: `「んふうううううっ！！！」`
- TW: `「你可愛的陰蒂也變得硬邦邦的——陰蒂和陰蒂在互相摩擦——」`
- VN cũ: `「Ưm phù ư ư ư ư ư!!!」`
- Sửa: `「Nfuuuuuu!!!」`
- Lý do: んふうううううっ→"Ưm phù ư ư ư ư ư" tách một âm dài thành 6 mảnh → gộp romaji "Nfuuuuuu" (6u theo công thức).

### Key 1359 (電車姫)
- JP: `「わらわ！　わらわもっ！　いっしょがいい――けど！\\nきちゃって、凄いのっ――イキそっ――んっ――ふあっ」`
- TW: `「你忍一下，再稍微忍一會！嗯！待會我們一起高潮！」`
- VN cũ: `「Ta! Ta cũng! Muốn cùng nhau——nhưng!\\nNó đến rồi, kinh khủng lắm——sắp lên đỉnh——ưm——phù ah」`
- Sửa: `「Ta! Ta cũng! Muốn cùng nhau——nhưng!\\nNó đến rồi, kinh khủng lắm——sắp lên đỉnh——ưm——Fua」`
- Lý do: ふあっ→"phù ah" tách mảnh → "Fua".

### Key 1368 (電車姫)
- JP: `「ひゃぐっ！　んっ――あっ！　がまんっ！　がまんっ！\\nふあっ！？　むりっ――これっ、むりっ――げんかいっ」`
- TW: `「來了！馬上來了！真的要來了！求你了！我們一起！一起高潮！！」`
- VN cũ: `「Hya gu! Ưm——ah! Nhịn! Cố nhịn!\\nPhù ah!? Không được——cái này, không được——đến giới hạn rồi」`
- Sửa: `「Hyagu! Ưm——ah! Nhịn! Cố nhịn!\\nFua!? Không được——cái này, không được——đến giới hạn rồi」`
- Lý do: ひゃぐっ→"Hya gu" tách một âm thành hai mảnh → "Hyagu"; ふあっ→"phù ah" tách mảnh → "Fua".

### Key 1370 (電車姫)
- JP: `「ん……あ――ん――ぷっ――ちゅっ――ちゅむっっ――\\nぺろっ――ぺちゅっ――ちゅうっ――べろおおおおっっ」`
- TW: `「來吧，紅葉。這東西比想像中大得多。麻煩你和我一起把它舔濕」`
- VN cũ: `「Ưm……a——ưm——phụt——chụt——chụt ưm——\\nLiếm——chụt——chụt——liếm liếm liếm liếm」`
- Sửa: `「Ưm……a——ưm——phụt——chụt——Chumu——\\nLiếm——Pechu——Chuu——Berooooo」`
- Lý do: ちゅむっっ→"chụt ưm" tách mảnh → "Chumu"; ぺちゅっ→"chụt" mất phụ âm ぺ → "Pechu"; ちゅうっ→"chụt" mất độ dài → "Chuu"; べろおおおおっっ→"liếm liếm liếm liếm" diễn 1 âm dài thành 4 động tác → "Berooooo" (5 o, xem cờ F4).

### Key 1409 (ひよこ)
- JP: `「ああああっ！！！」`
- TW: `「呀啊！撐不住了！余已經！啊！好想丟又不能丟，快要壞掉了」`
- VN cũ: `「Ahhhh!!!」`
- Sửa: `「Aaaa!!!」`
- Lý do: ああああっ (4a)→"Ahhhh" chỉ có 1 nguyên âm a → "Aaaa".

### Key 1424 (ひよこ)
- JP: `「ああっ――んっ――ふっっ――\\nしあわせっ――しあわせっ」`
- TW: `「呼啊——啊——啊——啊」`
- VN cũ: `「Ahhh——ưm——phù——\\nHạnh phúc——hạnh phúc quá」`
- Sửa: `「Aah——ưm——phù——\\nHạnh phúc——hạnh phúc quá」`
- Lý do: ああっ (2a)→"Ahhh" 3a → "Aah".

### Key 1426 (電車姫)
- JP: `「んううううっ！！　あっ――ああっ――そこっ！\\nクリトリスすきっ！　なかっ、もっ――きもち、いっ！」`
- TW: `「呼啊——啊——好棒——好舒服！呼——啊，拜託了——就這樣一直繼續——一直這樣」`
- VN cũ: `「Ưm ư ư ư ư!! Ah——ahhh——chỗ đó!\\nThích âm vật quá! Bên trong, cũng——sướng, quá!」`
- Sửa: `「Nuuuu!! Ah——Aah——chỗ đó!\\nThích âm vật quá! Bên trong, cũng——sướng, quá!」`
- Lý do: んううううっ→"Ưm ư ư ư ư" tách một âm thành 5 mảnh → "Nuuuu" (4u); ああっ→"ahhh" 3a → "Aah".

### Key 1428 (monologue)
- JP: `「ひゃいっ！？」`
- TW: `「呼啊——嗯……啊。奧莉薇女士」`
- VN cũ: `「Hya i!?」`
- Sửa: `「Hyai!?」`
- Lý do: ひゃいっ→"Hya i" tách một âm thành hai mảnh → "Hyai" (quy tắc 3b).

### Key 1433 (ひよこ)
- JP: `「んきゅっ！！？　ふっ――あっ――もみじっ！！\\nうごくっ――っっと――あっ――ふうううんっ！！！」`
- TW: `「呼啊啊！啊！啊啊？！！這太棒了！嗯，唔——太酸爽了——插得好深！！」`
- VN cũ: `「Ưm kyu!!? Phù——ah——Momiji!!\\nĐang chuyển động——kìa——ah——phù ư ư ư ư!!!」`
- Sửa: `「Nkyu!!? Phù——ah——Momiji!!\\nĐang chuyển động——kìa——ah——Fuuuuun!!!」`
- Lý do: んきゅっ→"Ưm kyu" tách mảnh → "Nkyu"; ふうううんっ→"phù ư ư ư ư" tách 5 mảnh → "Fuuuuun" (5u+n).

### Key 1481 (電車姫)
- JP: `「んふふっ！　よいっ！　よいぞっ！　ぞんぶんにっ――かわいいっ、声を――たくさん――たくさんっ！！」`
- TW: `「唔唔？！！！！！」`
- VN cũ: `「Ưm fufu! Tốt! Tốt lắm! Cứ thỏa thích——phát ra, những âm thanh——đáng yêu——thật nhiều——thật nhiều vào!!」`
- Sửa: `「Nfufu! Tốt! Tốt lắm! Cứ thỏa thích——phát ra, những âm thanh——đáng yêu——thật nhiều——thật nhiều vào!!」`
- Lý do: んふふっ→"Ưm fufu" tách một tiếng cười thành hai mảnh → "Nfufu" (cười khúc khích, giữ nguyên âm cười).

### Key 1515 (ひよこ)
- JP: `「クリトリス――完全に勃起、してます、なっ――んっ、\\n相変わらず……エッチで――大きっ――！　ふきゅ！？」`
- TW: `「嗯——呼——呼啊——雛——雛——再用力點——就是那裡——摩擦起來好舒服」`
- VN cũ: `「Âm vật——cương cứng, hoàn toàn, rồi, nhỉ——ưm,\\nVẫn……dâm đãng——và to——như mọi khi——! Phù kyu!?」`
- Sửa: `「Âm vật——cương cứng, hoàn toàn, rồi, nhỉ——ưm,\\nVẫn……dâm đãng——và to——như mọi khi——! Fukyu!?」`
- Lý do: ふきゅ→"Phù kyu" tách một âm thành hai mảnh → "Fukyu".

### Key 1519 (電車姫)
- JP: `「はあっ――はあっ――んくっ――ンッ――（ごくっ）\\nふふっ――ひよこ――お主はいつも――かわいい、の！」`
- TW: `「嗯——哈——蛤啊——這東西——真的是，唔，太粗了」`
- VN cũ: `「Haa——haa——ưm kh——Ưm——(ực)\\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」`
- Sửa: `「Haa——haa——Nku——Ưm——(ực)\\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」`
- Lý do: んくっ→"ưm kh" tách mảnh, mất âm → "Nku".

### Key 1527 (ひよこ)
- JP: `「ちゅぶっ――ちゅうっ――れるっ――れりゅうっ――\\nちゅうっ――ちゅっ――ちゅむむぅっ――ぷあっ」`
- TW: `「嗯……啾——咧溜——滋溜——嗯啾——啾——啾——啾嚕嚕」`
- VN cũ: `「Chụt bụp——chụt——rột——rột——\\nChụt——chụt——chụt——phù ah」`
- Sửa: `「Chubu——Chuu——Reru——Reryuu——\\nChuu——chụt——Chumumuu——Pua」`
- Lý do: ちゅぶっ→"Chụt bụp" tách mảnh → "Chubu"; ちゅうっ→"chụt" mất độ dài → "Chuu" (×2); れるっ→"rột" mất âm → "Reru"; れりゅうっ→"rột" mất âm → "Reryuu"; ちゅむむぅっ→"chụt" mất âm + độ dài → "Chumumuu" (4u); ぷあっ→"phù ah" tách mảnh → "Pua".

### Key 1542 (ひよこ)
- JP: `「ひゅあぁぁぁぁぁぁぁぁぁぁぁぁんんんっっっ！！！」`
- TW: `「嗯唔唔唔嗯嗯嗯嗯！！！！！」`
- VN cũ: `「Hyu ahhhhhhhhhhh ưm ưm!!!」`
- Sửa: `「Hyuaaaaaaaaaaaaannn!!!」`
- Lý do: ひゅあぁ…(13a)んんん→"Hyu ahhh… ưm ưm" sai đếm (1a) + tách mảnh → "Hyuaaaaaaaaaaaaannn" (13a+3n).

### Key 1556 (ひよこ)
- JP: `「ふっ――んっ――はっ――あ……ふあっ――（ごくっ）、\\n紅葉も――余裕、あるよう、には――見えません、が！」`
- TW: `「嗯，呼呼？剛才那副從容的表情哪裡去了？剛剛是不是丟了？」`
- VN cũ: `「Phù——ưm——ha——a……phù ah——(ực),\\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」`
- Sửa: `「Phù——ưm——ha——a……Fua——(ực),\\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」`
- Lý do: ふあっ→"phù ah" tách mảnh → "Fua".

### Key 1655 (電車姫)
- JP: `「ひあっ！　あっ！！　ひよこ！　ひよこぉ！！\\nおねがいじゃ！　もっと！　もっと！　もっとぉ！！」`
- TW: `「我明白。我說到就一定會做到」`
- VN cũ: `「Hi ah! Ah!! Hiyoko! Hiyoko!!\\nXin cô đấy! Nữa! Nữa! Nữa đi!!」`
- Sửa: `「Hia! Ah!! Hiyoko! Hiyoko!!\\nXin cô đấy! Nữa! Nữa! Nữa đi!!」`
- Lý do: ひあっ→"Hi ah" tách mảnh → "Hia" (quy tắc 3b: "Á" cho họ ひあ là lỗi mất phụ âm).

### Key 1697 (電車姫)
- JP: `「ふあっ――フッ――指っ――その、ように――\\nひっきり、なし、にっ――んっ――ううぅっ！！！」`
- TW: `「有聽到剛剛的問題吧？現在你的這個聽過去有些難受的喘息聲是什麼」`
- VN cũ: `「Phù ah——Phù——Ngón tay——như, thế——\\nKhông, ngừng, nghỉ——ưm——ư ư!!!」`
- Sửa: `「Fua——Phù——Ngón tay——như, thế——\\nKhông, ngừng, nghỉ——ưm——Ưưư!!!」`
- Lý do: ふあっ→"Phù ah" tách mảnh → "Fua"; ううぅっ→"ư ư" tách mảnh + sai đếm (3u) → "Ưưư".

### Key 1710 (電車姫)
- JP: `「ん……くっ――はぁっ――はあ――（ごくっ）――\\nわらわの、[ほと,1]女陰、から、溢れ出しておる――液体、は」`
- TW: `「比平時箍得還要緊……真是未免讓人有些嫉妒。被奧莉薇女士盯著看竟然會讓你如此亢奮」`
- VN cũ: `「Ưm……ư——haa——haa——(ực)——\\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」`
- Sửa: `「Ưm……Ku——haa——haa——(ực)——\\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」`
- Lý do: くっ→"ư" mất phụ âm k → "Ku".

### Key 1773 (電車姫)
- JP: `「はっ、あっ――んっ――ふうっ――\\nンッ――フッ――ああっ」`
- TW: `「紅葉？奧莉薇女士又發問了」`
- VN cũ: `「Ha, ah——ưm——phù——\\nƯm——Phù——Ahhh」`
- Sửa: `「Ha, ah——ưm——Phùù——\\nƯm——Phù——Aah」`
- Lý do: ふうっ (2u)→"phù" chỉ 1u → "Phùù"; ああっ (2a)→"Ahhh" 3a → "Aah".

### Key 1802 (電車姫)
- JP: `「やあっ！　むりいっっ！　もうっ！　わらわっ！　あ！\\nイキたっ――すぎ、てっ――むりっ！　こわれるうっ！」`
- TW: `「蛤啊！啊！呼！啊啊——馬上丟了！嗯——再一小會就來了——嗯！呼呼！」`
- VN cũ: `「Ya ah! Không được rồi! Không được nữa! Ta! A!\\nMuốn lên đỉnh——quá, rồi——không được! Hỏng mất!」`
- Sửa: `「Yaa! Không được rồi! Không được nữa! Ta! A!\\nMuốn lên đỉnh——quá, rồi——không được! Hỏng mất!」`
- Lý do: やあっ→"Ya ah" tách một âm thành hai mảnh → "Yaa".

### Key 1804 (ひよこ)
- JP: `「んうっっ――くっ――んっ――ああっ――あっ」`
- TW: `「蛤啊，蛤啊，蛤啊，蛤啊」`
- VN cũ: `「Ưm——kh——ưm——ahhh——ah」`
- Sửa: `「Ưm——Ku——ưm——aah——ah」`
- Lý do: くっ→"kh" mất nguyên âm u → "Ku"; ああっ→"ahhh" 3a → "aah".

### Key 1887 (電車姫)
- JP: `「か……はっ――あっ！　待てと、申すに……んうっ！\\nなにも――そこ、まで――男の、ように――ひぎっ！？」`
- TW: `「那麼粗的東西……Ａｍａｚｉｎｇ……真的插進去了……陰道口整個被撐大了，好厲害」`
- VN cũ: `「Kh……ha——ah! Ta bảo đợi đã, mà……ưm ư!\\nĐâu cần——đến, mức đó——như đàn ông, vậy——hi gi!?」`
- Sửa: `「Ka……ha——ah! Ta bảo đợi đã, mà……Ưm!\\nĐâu cần——đến, mức đó——như đàn ông, vậy——Higi!?」`
- Lý do: か……→"Kh" mất nguyên âm a → "Ka"; んうっ→"ưm ư" tách mảnh → "Ưm" (âm ngắn, giữ VN "Ưm" theo tiền lệ fukamih2); ひぎっ→"hi gi" tách mảnh → "Higi".

### Key 2084 (電車姫)
- JP: `「はっ！　あっ！　ああっ！　じらされ、てた、からっ！\\nんっ！　ふううっ！　わらわっ――わらわ！　もうっ！」`
- TW: `三根手指在劇烈地一進一出，大拇指也同時不斷地來回摩挲陰蒂。`
- VN cũ: `「Ha! Ah! Ahhh! Bị bắt, nhịn, nãy giờ!\\nƯm! Phù ư ư! Ta——ta! Sắp!」`
- Sửa: `「Ha! Ah! Aah! Bị bắt, nhịn, nãy giờ!\\nƯm! Fuuu! Ta——ta! Sắp!」`
- Lý do: ああっ→"Ahhh" 3a → "Aah"; ふううっ→"Phù ư ư" tách mảnh → "Fuuu" (3u).

### Key 2094 (電車姫)
- JP: `「ふ……ぁっ――」`
- TW: `不死鳥博士彷彿在向我展示一般，輕輕地撫摸著陰道口的周邊。`
- VN cũ: `「Phù……ah——」`
- Sửa: `「Fua——」`
- Lý do: ふ……ぁっ→"Phù……ah" tách mảnh → "Fua".

### Key 2098 (電車姫)
- JP: `「はあっ――はあっ――はあっ――はあっ――んっ―――\\nわらわっっ――こんなっ――あさましい――ひっ、ぐっ」`
- TW: `不死鳥博士撐開陰道口，內部一覽無餘。陰道口就好像痙攣一般不斷地在顫抖。`
- VN cũ: `「Haa——Haa——Haa——Haa——Ưm——\\nTa——Bộ dạng——đáng xấu hổ, này——Hức, hức」`
- Sửa: `「Haa——Haa——Haa——Haa——Ưm——\\nTa——Bộ dạng——đáng xấu hổ, này——Hi, gu」`
- Lý do: ひっ、ぐっ→"Hức, hức" gộp hai âm khác nhau thành một kiểu nấc → "Hi, gu" (xem cờ F5).

### Key 2145 (電車姫)
- JP: `「ンッ――ふっ――ふあっ――ひよこっ――ひよこっ――もっと、つよ、く――そこっ――こすれてっ――いいっ」`
- TW: `兩人的下體緊緊貼在一起扭動起了腰肢。隨之而來的是水聲以及濺出的水花。`
- VN cũ: `「Ưm——phù——phù ah——Hiyoko——Hiyoko——mạnh, hơn nữa——chỗ đó——cọ xát——thích quá」`
- Sửa: `「Ưm——phù——Fua——Hiyoko——Hiyoko——mạnh, hơn nữa——chỗ đó——cọ xát——thích quá」`
- Lý do: ふあっ→"phù ah" tách mảnh → "Fua".

### Key 2146 (ひよこ)
- JP: `「はあっ――っっ――ふっ――ふあっ――きもち、いっ！\\nん――おくっ、にっ――ごちゅ、ごちゅ――あた、って」`
- TW: `兩人的動作漸漸開始同化為一體。就好像彼此合二為一了一般——`
- VN cũ: `「Haa——ư——phù——phù ah——sướng, quá!\\nƯm——ở sâu, bên trong——nhóp nhép, nhóp nhép——chạm, vào rồi」`
- Sửa: `「Haa——ư——phù——Fua——sướng, quá!\\nƯm——ở sâu, bên trong——Gochu, gochu——chạm, vào rồi」`
- Lý do: ふあっ→"phù ah" tách mảnh → "Fua"; ごちゅ→"nhóp nhép" sai âm (âm đẩy ướt, không phải nhai) → "Gochu" (xem cờ F3).

### Key 2159 (電車姫)
- JP: `「ふあああっ！　しゅきっ！　クリトリスぅっ――\\nちゅんって！　ちゅんって！　タッチ、されるの！！」`
- TW: `只見三根手指同時沒根插入陰道口，並且大拇指也沒有停止對陰蒂的愛撫。`
- VN cũ: `「Phù ahhh! Sướng quá! Âm vật——\\nBị búng! Bị búng! Bị chạm, vào rồi!!」`
- Sửa: `「Fuaaa! Sướng quá! Âm vật——\\nBị búng! Bị búng! Bị chạm, vào rồi!!」`
- Lý do: ふあああっ (3a)→"Phù ahhh" tách mảnh + sai đếm → "Fuaaa".

### Key 2168 (ひよこ)
- JP: `「ん――はっ――はあっ――これっ――はっ――やはり、\\nくっ――ふと、すぎ――るっ――かもっ――」`
- TW: `太壯觀了，愛液和汗水弄得身體都黏糊糊的。兩個人的臉還紅通通的，連乳頭都立起來了——`
- VN cũ: `「Ưm——ha——haa——cái này——ha——quả nhiên,\\nư——to, quá——mất, rồi——」`
- Sửa: `「Ưm——ha——haa——cái này——ha——quả nhiên,\\nKu——to, quá——mất, rồi——」`
- Lý do: くっ→"ư" mất phụ âm k → "Ku".

### Key 2184 (電車姫)
- JP: `「ん……ちゅっ――れるっ――れろっ――んっ――\\nちゅむっ――ちゅうっ――ちゅっ――じゅるるうっ」`
- TW: `她們深情地吻在了一起，激烈程度與剛才的簡直有著天壤之別——`
- VN cũ: `「Ưm……chụt——rột——rột——ưm——\\nChụt——chụt——chụt——rột rột」`
- Sửa: `「Ưm……chụt——Reru——Rero——ưm——\\nChumu——Chuu——chụt——Jururuu」`
- Lý do: れるっ→"rột" mất âm → "Reru"; れろっ→"rột" mất âm → "Rero"; ちゅむっ→"Chụt" mất âm → "Chumu"; ちゅうっ→"chụt" mất độ dài → "Chuu"; じゅるるうっ→"rột rột" mất âm → "Jururuu" (4u).

### Key 2220 (電車姫)
- JP: `「はぁっ――んっ――感じる――いつも、より――くっ\\nこのような――異常な――状況――んっ……は、あっ」`
- TW: `手指的每一次輕撫，電車公主的皮膚都會隨之慢慢染上紅暈。看起來就和真的“紅葉”一樣，非常漂亮。`
- VN cũ: `「Haa——ưm——cảm nhận được——hơn, mọi khi——ư\\nTình trạng——bất thường——thế này——ưm……ha, ah」`
- Sửa: `「Haa——ưm——cảm nhận được——hơn, mọi khi——Ku\\nTình trạng——bất thường——thế này——ưm……ha, ah」`
- Lý do: くっ→"ư" mất phụ âm k → "Ku".

### Key 2234 (ひよこ)
- JP: `「ん……くっ――これっ――くっ――ふっ！　あっっ！　いれ、たら――挿れ、たらっ――ふ、太、すぎっ――！」`
- TW: `是什麼來著？對了，是雙頭假陽具！只見其中一頭緩緩進入到不死鳥博士的下體裡。`
- VN cũ: `「Ưm……ư——Cái này——ư——phù! Ah! Đút, vào——nhét, vào rồi——phù, to, quá——!」`
- Sửa: `「Ưm……Ku——Cái này——Ku——phù! Ah! Đút, vào——nhét, vào rồi——phù, to, quá——!」`
- Lý do: くっ ×2→"ư" mất phụ âm k → "Ku" ×2.

### Key 2238 (電車姫)
- JP: `「ふああっ！　あ！　ああっ！！？　これっ、しゅごっ！\\nんっ、くっ――すご、いっ――おくっ――おくっ！！」`
- TW: `最粗的部分穿進去之後，剩下的部分輕而易舉地完全進去了。`
- VN cũ: `「Phù ahhh! A! Ahhh!!? Cái này, sướng quá!\\nƯm, kh——sướng, quá——sâu——sâu quá!!」`
- Sửa: `「Fuaa! A! Aah!!? Cái này, sướng quá!\\nƯm, Ku——sướng, quá——sâu——sâu quá!!」`
- Lý do: ふああっ (2a)→"Phù ahhh" tách mảnh + sai đếm → "Fuaa"; ああっ→"Ahhh" 3a → "Aah"; くっ→"kh" mất nguyên âm u → "Ku".

### Key 2247 (電車姫)
- JP: `「んくっ――んっ――むぶっ――んちゅっ――ちゅっ――\\nちゅむ――ぶちゅっ――ずぢっ――ちゅっ、ちゅぶうっ」`
- TW: `為了讓假陽具塗滿唾液，電車公主直接一口含住了假陽具。`
- VN cũ: `「Ưm——ưm——ưm——ưm chụt——chụt——\\nChụt ưm——phụt——rột——chụt, chụt bụp」`
- Sửa: `「Nku——ưm——Mubu——Nchu——chụt——\\nChumu——Buchu——Zuji——chụt, Chubuu」`
- Lý do: んくっ→"Ưm" mất âm k → "Nku"; むぶっ→"ưm" mất cả âm → "Mubu"; んちゅっ→"ưm chụt" tách mảnh → "Nchu"; ちゅむ→"Chụt ưm" tách mảnh → "Chumu"; ぶちゅっ→"phụt" sai âm → "Buchu"; ずぢっ→"rột" sai âm → "Zuji"; ちゅぶうっ→"chụt bụp" tách mảnh + mất độ dài → "Chubuu" (3u).

### Key 2279 (電車姫)
- JP: `「あ……ふっ――んっ――ふあっ、あっ」`
- TW: `眼看著假陽具就要插進電車公主的陰道口，不會斷掉嗎？！剛想到這，沒想到它一點點進去——`
- VN cũ: `「A……phù——ưm——phù ah, ah」`
- Sửa: `「A……phù——ưm——Fua, ah」`
- Lý do: ふあっ→"phù ah" tách mảnh → "Fua".

### Key 2331 (電車姫)
- JP: `「ちゅっ――れるっ――じゅぶっ――ちゅぼおおおっ――\\nちゅるっ――れるっ――くぷうううううっ――ぷあっ」`
- TW: `電車公主含著假陽具的同時前後搖頭……表情看過去似乎有點痛苦——但不知為何這幅場景卻美如畫。`
- VN cũ: `「Chụt——rột——nhóp nhép——chụt bụp——\\nChụt rột——rột——chụt rột——phụt」`
- Sửa: `「Chụt——Reru——Jubu——Chuboooo——\\nChuru——Reru——Kupuuuuuu——Pua」`
- Lý do: れるっ→"rột" mất âm → "Reru" (×2); じゅぶっ→"nhóp nhép" sai âm → "Jubu"; ちゅぼおおおっ→"chụt bụp" tách mảnh + mất độ dài → "Chuboooo" (4o); ちゅるっ→"Chụt rột" tách mảnh → "Churu"; くぷうううううっ→"chụt rột" sai âm hoàn toàn → "Kupuuuuuu" (7u); ぷあっ→"Pua" (ghi đè "phù ah" của audit — audit đã sửa "phụt"→"phù ah"; xem §1).

### Key 2334 (電車姫)
- JP: `「んっ――いきなり、挿入――ディルド、使うのか、と、\\nあっ――思うて、おった、が――くっ――ふ、あっ」`
- TW: `電車公主和不死鳥博士的胯部……呃，是大陰唇！大陰唇和大陰唇親在了一起。`
- VN cũ: `「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\\nah——cứ nghĩ, là vậy, nhưng——ư——phù, ah」`
- Sửa: `「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\\nah——cứ nghĩ, là vậy, nhưng——Ku——Fua」`
- Lý do: くっ→"ư" mất phụ âm k → "Ku"; ふ、あっ→"phù, ah" tách mảnh → "Fua".

### Key 2342 (ひよこ)
- JP: `「はあっ！　あっ！　ふっ！　ああっ――もう、すぐっ！\\nん――これっ――もう、すこしっ――んっ！　ふうう！」`
- TW: `電車公主的眼角滲出了淚花。但即便淚眼汪汪，卻依然享受著至高的快感——以及忍耐高潮的焦躁感。`
- VN cũ: `「Haa! Ah! Phù! Ahhh——sắp, rồi!\\nƯm——cái này——một chút, nữa thôi——ưm! Phù ư ư!」`
- Sửa: `「Haa! Ah! Phù! Aah——sắp, rồi!\\nƯm——cái này——một chút, nữa thôi——ưm! Fuuu!」`
- Lý do: ああっ→"Ahhh" 3a → "Aah"; ふうう！→"Phù ư ư" tách mảnh → "Fuuu" (3u).

### Key 2343 (電車姫)
- JP: `「はああっ！　わらわっ！　わらわっ！　んっ！　ふっっ！　見られて――見られてっ！」`
- TW: `電車公主的胯部如雨注一般嘩啦啦地漫出大量汁液。`
- VN cũ: `「Haa ah! Ta! Ta! Ưm! Phù! Bị nhìn thấy——bị nhìn thấy rồi!」`
- Sửa: `「Haaa! Ta! Ta! Ưm! Phù! Bị nhìn thấy——bị nhìn thấy rồi!」`
- Lý do: はああっ (3a)→"Haa ah" tách một âm thành hai mảnh → "Haaa".

### Key 2346 (電車姫)
- JP: `「ふぁっ――あっ――あっ――あっ」`
- TW: `電車公主的身體高高翹起，不死鳥博士則是蜷縮起身子。`
- VN cũ: `「Phù ah——ah——ah——ah」`
- Sửa: `「Fua——ah——ah——ah」`
- Lý do: ふぁっ→"Phù ah" tách mảnh → "Fua".

### Key 2352 (ひよこ)
- JP: `「はふっ――んっ――きゅっ！　ふあっ！　ああっ！\\nなかっ！　[なか,1]膣内っっ！　ずりゅって！　みちみちっ！」`
- TW: `電車公主開始轉動腰肢。不死鳥博士也跟著節奏扭腰。`
- VN cũ: `「Hap——ưm——kyu! Phù ah! Ahhh!\\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」`
- Sửa: `「Hafu——ưm——kyu! Fua! Aah!\\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」`
- Lý do: はふっ→"Hap" sai âm (はふ≠hap) → "Hafu"; ふあっ→"Phù ah" tách mảnh → "Fua"; ああっ→"Ahhh" 3a → "Aah".

### Key 2422 (電車姫)
- JP: `「ふあっ！　あっ！　あっ！　あっ！　きもち、いいっ、\\nやっ！　あっ！　それ――もっと――ひよこ、もっと！」`
- TW: `（來回抽插）`
- VN cũ: `「Phù ah! Ah! Ah! Ah! Sướng, quá,\\nƯ! Ah! Nữa——nữa đi——Hiyoko, nữa đi!」`
- Sửa: `「Fua! Ah! Ah! Ah! Sướng, quá,\\nYa! Ah! Nữa——nữa đi——Hiyoko, nữa đi!」`
- Lý do: ふあっ→"Phù ah" tách mảnh → "Fua"; やっ→"Ư" mất phụ âm y → "Ya" (tiền lệ ポーレットh3).

### Key 2426 (電車姫)
- JP: `「っっ！！！？\\nいっ！　きゅぅぅぅぅぅぅぅぅぅぅぅぅっっっっっ！！」`
- TW: `（劇烈收縮）`
- VN cũ: `「!!!?\\nƯ! Cứuuuuuuuuuuuuuuu!!」`
- Sửa: `「Ư!!!?\\nI! Kyuuuuuuuuuuuuu!!」`
- Lý do: っっ→audit đã thêm "Ư" (giữ); いっ→"Ư" mất nguyên âm i → "I"; きゅぅ…(13u)→audit đã sửa "Cứuu…" (sai đếm) thành "Kyuuuuuuuuuuuuu" đúng 13u (giữ). Giá trị moan = giá trị audit, chỉ đổi token いっ (xem §1).

### Key 2428 (電車姫)
- JP: `「んヒュッ――ふっ……くっ――荒、く……なって――\\nしまって――おる、がっ――んうっ！！」`
- TW: `（反覆摩擦）`
- VN cũ: `「Ư hiu——phù……ư——Trở nên, gấp……gáp——\\nMất rồi——nhưng——ư ư!!」`
- Sửa: `「Nhyu——phù……Ku——Trở nên, gấp……gáp——\\nMất rồi——nhưng——Ưm!!」`
- Lý do: んヒュッ→"Ư hiu" tách mảnh, trái quy tắc 3b → "Nhyu"; くっ→"ư" mất phụ âm k → "Ku"; んうっ→"ư ư" tách mảnh → "Ưm" (âm ngắn, giữ VN "Ưm").

### Key 2434 (電車姫)
- JP: `「んっきゅううううううんんんんんっっっっ！！！！！」`
- TW: `（急雨如注）`
- VN cũ: `「Ưm kyuuuuuuuuưưưưm!!!!!」`
- Sửa: `「Nkyuuuuuuunnnnn!!!!!」`
- Lý do: んっきゅううううううんんんんんっっっっ→"Ưm kyuuuuuuuuưưưưm" tách mảnh + sai đếm → "Nkyuuuuuuunnnnn" (7u+5n).

### Key 2435 (電車姫)
- JP: `「ひあっ！？　あっ、やっ――みられてっ！　わらわっ！\\nイッってる――性器っ――ひらかれ、てっ――んうっ！」`
- TW: `（抽出）`
- VN cũ: `「Hi ah!? Ah, ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ư ư!」`
- Sửa: `「Hia!? Ah, ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ưm!」`
- Lý do: ひあっ→"Hi ah" tách mảnh → "Hia"; んうっ→"Ư ư" tách mảnh → "Ưm".

### Key 2437 (ひよこ)
- JP: `「ふきゅうううううううっ！！！！！？」`
- TW: `（抽動）`
- VN cũ: `「Phù kyu ư ư ư ư ư ư ư!!!!!?」`
- Sửa: `「Fukyuuuuuuuu!!!!!?」`
- Lý do: ふきゅうううううううっ (9u)→"Phù kyu ư ư ư ư ư ư ư" tách 8 mảnh → "Fukyuuuuuuuu" (9u — lượt soát 2 sửa từ 8u lên 9u).

### Key 2438 (電車姫)
- JP: `「んひゅっ！」`
- TW: `（插入）`
- VN cũ: `「Ư hiu!」`
- Sửa: `「Nhyu!」`
- Lý do: んひゅっ→"Ư hiu" tách mảnh → "Nhyu" (quy tắc 3b).

### Key 2449 (電車姫)
- JP: `「か……はっ――！！！！？」`
- TW: `（直搗黃龍）`
- VN cũ: `「Kh……ha——!!!!?」`
- Sửa: `「Ka……ha——!!!!?」`
- Lý do: か……→"Kh" mất nguyên âm a → "Ka".

### Key 2452 (電車姫)
- JP: `「んきゅんっ！！！！！」`
- TW: `（緊貼）`
- VN cũ: `「Ưm kyu!!!!!」`
- Sửa: `「Nkyun!!!!!」`
- Lý do: んきゅんっ→"Ưm kyu" tách mảnh → "Nkyun".

### Key 2457 (電車姫)
- JP: `「ふぁっ――あっ――いいっ――イイっ！　ふっ――あ、\\nおねがいっ――このまま――このまま――このままあっ」`
- TW: `（進進出出）`
- VN cũ: `「Phù ah——ah——sướng——sướng quá! Phù——ah,\\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」`
- Sửa: `「Fua——ah——sướng——sướng quá! Phù——ah,\\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」`
- Lý do: ふぁっ→"Phù ah" tách mảnh → "Fua".

### Key 2458 (電車姫)
- JP: `「ふあああああっっ！！！！」`
- TW: `（長驅直入）`
- VN cũ: `「Phù ahhhh!!!!」`
- Sửa: `「Fuaaaaaa!!!!」`
- Lý do: ふあああああっっ (6a)→"Phù ahhhh" tách mảnh + sai đếm → "Fuaaaaaa".

### Key 2460 (電車姫)
- JP: `「んううっ！！　あっ！？　はげしっ――はげしいっ！　\\nそんなっ――そんなっ――はげしくっ――されたらぁ！」`
- TW: `（開開合合）`
- VN cũ: `「Ưm ư ư!! Ah!? Mãnh liệt——mãnh liệt quá!\\nBị làm——bị làm——mãnh liệt——thế này, thì!」`
- Sửa: `「Nuu!! Ah!? Mãnh liệt——mãnh liệt quá!\\nBị làm——bị làm——mãnh liệt——thế này, thì!」`
- Lý do: んううっ (2u)→"Ưm ư ư" tách 3 mảnh → "Nuu".

## 4. Dòng rên giữ nguyên (ghi chú)

- ふむ/ふぅん/ふぅむ → "Hừm/Hửm" (14 dòng: 53, 1308, 1388, 1478, 1507, 1627, 1759, 1782, 1868, 1870, 1876, 2107, 2276, 1511) — tiếng ậm ừ suy nghĩ, diễn VN tự nhiên, giữ.
- んっ → "Ưm/ưm" (1 âm ngắn, đúng) — giữ. んうっ ngắn → "Ưm" giữ (1437, 1804, 2147); 2339 "ưm, ư" giữ vì JP có dấu 、tách thành 2 nhịp.
- あっ/はっ → "Ah/Ha" (っ đã diễn bằng ——/dấu câu theo tiền lệ あっ――→"A——") — giữ. ああっ→"Aah" chỉ sửa ở 4 dòng sai đếm (1424, 1426, 1804, 2084, 2238, 2342 — đã sửa).
- ふっ → "Phù/phù" — giữ (nhất quán cả file; tiền lệ h7 F3 "phù vs Fu" vẫn mở ở đợt thống nhất).
- SFX trong ngoặc （ ） diễn thành động từ/từ tượng thanh VN ("Tách ra" 1590, "Nắn bóp" 1406, "Chạm nhẹ" 1891/1676, "Phập" 1589/1902/2087/1390/1886/1536/1543/1419/1715/1408, "Nhóp nhép" 1867/2087/1393/1419/1715/1543/1496/1431/1408/1886, "Trượt vào" 1488/2328/1408, "Ngoạm" 1618, "Ực" 2187/1710/1519/1556, "Áp sát" 1386/1418 đã audit sửa thành "Nhóp nhép") — giữ theo tiền lệ paulette-h4 (SFX ngoặc diễn thành động từ VN là chấp nhận được).
- Cười ふふっ → "Fufu" (1908, 2323, 2347, 2350, 1519) — giữ, đúng quy tắc cười là cười, không phải rên. んふふっ → "Nfufu" là 1 trong 55 dòng sửa (1481).
- ふえっ → "Hể!?" (1557) — giữ (thán từ ngạc nhiên tiếng Việt tự nhiên, không phải rên).
- 1369 じゅぶじゅぶっ/ちゅんちゅん → "Bị đút vào nhóp nhép, bị búng liên tục" — giữ (diễn nghĩa đúng cho SFX hành động trong câu thoại; xem cờ F7).
- くっ trong từ nội dung (くっつく, しゅごっ, にくっ, ぽいっ, びくびく, がくっ…) — không phải âm rên, giữ nguyên.
- Gasp Ư: 1822 「っ///」→"Ư///" giữ. Sweep 6 mục đã do audit sửa (xem §1), không đụng.
- 1655 ひよこぉ → "Hiyoko" và もっとぉ → "Nữa đi" — độ dài ぉ bị mất nhưng là tên gọi/từ hô, không phải rên — không sửa (xem cờ F6).

## 5. Cờ cho đợt thống nhất

- **F1 — んうっ:** "Ưm" (âm ngắn 1u) vs romaji "Nu/Nuu" (âm dài): file này dùng "Ưm" cho んうっ 1u (2428/2435/1887 sửa từ tách mảnh về 1 token; 1437/1804/2147 giữ nguyên) và romaji "Nuu"/"Nuuuu" cho んううっ/んううううっ (2460/1426). Cần quyết một quy tắc cho toàn dự án (fukamih2 F4 "ưm vs ưm ư" vẫn mở).
- **F2 — ふっ "phù" vs "Fu":** file này giữ "phù" nhất quán; tiền lệ h7 F3 vẫn mở.
- **F3 — SFX miệng/lưỡi trong thoại → romaji vs động từ VN:** file này romaji hoá dòng toàn âm thanh (2331/2247/2184/1527/2146: Jubu/Zuji/Gochu/Reru…) nhưng SFX ngoặc （ ） vẫn giữ động từ VN ("Phập"/"Nhóp nhép"). Cần quyết ranh giới thống nhất.
- **F4 — べろおおおおっっ → "Berooooo" (1370):** 1 âm dài diễn thành romaji thay vì "liếm liếm liếm liếm" (4 động tác); cần xác nhận (paulette-h4 932 giữ "liếm" cho ぺろぺろ).
- **F5 — ひっ、ぐっ → "Hi, gu" (2098):** "Hức, hức" cũ diễn thành tiếng nấc; romaji giữ đúng 2 âm. Cần xác nhận.
- **F6 — 1655:** ひよこぉ → "Hiyoko", もっとぉ → "Nữa đi" (độ dài ぉ mất — tên gọi/từ hô, không sửa).
- **F7 — 1369:** じゅぶじゅぶっ/ちゅんちゅん giữ diễn nghĩa ("Bị đút vào nhóp nhép, bị búng liên tục") — SFX hành động trong câu thoại, khác dòng toàn âm thanh (2331) đã romaji hoá. Cần quyết.
- **F8 — Trùng audit (2331, 2426):** 2331 "Pua" ghi đè "phù ah" của audit (audit sửa "phụt"→"phù ah"); 2426 giữ "Ư" + đếm 13u của audit, chỉ đổi いっ "Ư"→"I". Parent đối chiếu `audit-lr-olivy-hiyoko-wrong.json`.
- **F9 — あっ "Ah" vs "A"/"Á":** file này: あっ→"Ah", あ→"A", ああっ→"Aah" — chưa nhất quán toàn dự án.
- **F10 — 2146 っっ―― → "ư——":** giữ (gasp đã diễn bằng Ư, không đụng); sweep không bao phủ key này — cần xác nhận ở đợt thống nhất.

## 6. Lượt soát 2 (second pass)

- Đọc lại toàn bộ 55 giá trị fix đối chiếu JP (+TW) sau khi viết xong: **tổng 55 / tái kiểm chứng 54 / bỏ 0 / sửa 1.**
- Dòng sửa ở lượt 2: **2437** — "Fukyuuuuuuu" (8u) → "Fukyuuuuuuuu" (9u): đếm lại JP ふきゅうううううううっ = ふ(1u)+きゅ(1u)+う×7(7u) = 9u.
- Đếm nguyên âm kiểm chứng độc lập bằng script (sau lượt soát 2): 2458 "Fua"+6a; 2159 3a; 2238 2a; 1542 "Hyu"+13a+3n; 1354 "Nf"+6u; 1433 "F"+5u+"n"; 2437 "Fukyu"+9u; 2434 "Nky"+7u+5n; 2426 "Ky"+13u (khớp audit); 1426 "N"+4u; 2460 "N"+2u; 2331 "Chub"+4o / "Kup"+7u; 1370 "Ber"+5o; 1527 "Chumumu"+4u; 2184 "Jururu"+4u; 2247 "Chub"+3u; 2084/2342 "F"+3u — tất cả khớp JP.
- JSON 55 mục, khóa string, jp/tw/old_vn khớp CSV3 55/55 (1 bộ duy nhất, 441 dòng).
- Khối TOML parse bằng tomllib: 55 khóa, 0 sai lệch giá trị.

## 7. Khối TOML (parse-verified)

```toml
[script]
"875" = "「Fua——ưm……a. Cô Olivy」"
"899" = "「Oa——tuyệt quá……nó giãn ra kìa……Fua——Công chúa Tàu điện\\n——còn một lỗ nữa——có một cái lỗ mà Olivy không có.」"
"1354" = "「Nfuuuuuu!!!」"
"1359" = "「Ta! Ta cũng! Muốn cùng nhau——nhưng!\\nNó đến rồi, kinh khủng lắm——sắp lên đỉnh——ưm——Fua」"
"1368" = "「Hyagu! Ưm——ah! Nhịn! Cố nhịn!\\nFua!? Không được——cái này, không được——đến giới hạn rồi」"
"1370" = "「Ưm……a——ưm——phụt——chụt——Chumu——\\nLiếm——Pechu——Chuu——Berooooo」"
"1409" = "「Aaaa!!!」"
"1424" = "「Aah——ưm——phù——\\nHạnh phúc——hạnh phúc quá」"
"1426" = "「Nuuuu!! Ah——Aah——chỗ đó!\\nThích âm vật quá! Bên trong, cũng——sướng, quá!」"
"1428" = "「Hyai!?」"
"1433" = "「Nkyu!!? Phù——ah——Momiji!!\\nĐang chuyển động——kìa——ah——Fuuuuun!!!」"
"1481" = "「Nfufu! Tốt! Tốt lắm! Cứ thỏa thích——phát ra, những âm thanh——đáng yêu——thật nhiều——thật nhiều vào!!」"
"1515" = "「Âm vật——cương cứng, hoàn toàn, rồi, nhỉ——ưm,\\nVẫn……dâm đãng——và to——như mọi khi——! Fukyu!?」"
"1519" = "「Haa——haa——Nku——Ưm——(ực)\\nFufu——Hiyoko——cô lúc nào cũng——đáng yêu, thật đấy!」"
"1527" = "「Chubu——Chuu——Reru——Reryuu——\\nChuu——chụt——Chumumuu——Pua」"
"1542" = "「Hyuaaaaaaaaaaaaannn!!!」"
"1556" = "「Phù——ưm——ha——a……Fua——(ực),\\nMomiji cũng——đâu có vẻ gì, là——thong dong, đâu!」"
"1655" = "「Hia! Ah!! Hiyoko! Hiyoko!!\\nXin cô đấy! Nữa! Nữa! Nữa đi!!」"
"1697" = "「Fua——Phù——Ngón tay——như, thế——\\nKhông, ngừng, nghỉ——ưm——Ưưư!!!」"
"1710" = "「Ưm……Ku——haa——haa——(ực)——\\nChất lỏng, tràn ra từ——âm hộ, của ta, là——」"
"1773" = "「Ha, ah——ưm——Phùù——\\nƯm——Phù——Aah」"
"1802" = "「Yaa! Không được rồi! Không được nữa! Ta! A!\\nMuốn lên đỉnh——quá, rồi——không được! Hỏng mất!」"
"1804" = "「Ưm——Ku——ưm——aah——ah」"
"1887" = "「Ka……ha——ah! Ta bảo đợi đã, mà……Ưm!\\nĐâu cần——đến, mức đó——như đàn ông, vậy——Higi!?」"
"2084" = "「Ha! Ah! Aah! Bị bắt, nhịn, nãy giờ!\\nƯm! Fuuu! Ta——ta! Sắp!」"
"2094" = "「Fua——」"
"2098" = "「Haa——Haa——Haa——Haa——Ưm——\\nTa——Bộ dạng——đáng xấu hổ, này——Hi, gu」"
"2145" = "「Ưm——phù——Fua——Hiyoko——Hiyoko——mạnh, hơn nữa——chỗ đó——cọ xát——thích quá」"
"2146" = "「Haa——ư——phù——Fua——sướng, quá!\\nƯm——ở sâu, bên trong——Gochu, gochu——chạm, vào rồi」"
"2159" = "「Fuaaa! Sướng quá! Âm vật——\\nBị búng! Bị búng! Bị chạm, vào rồi!!」"
"2168" = "「Ưm——ha——haa——cái này——ha——quả nhiên,\\nKu——to, quá——mất, rồi——」"
"2184" = "「Ưm……chụt——Reru——Rero——ưm——\\nChumu——Chuu——chụt——Jururuu」"
"2220" = "「Haa——ưm——cảm nhận được——hơn, mọi khi——Ku\\nTình trạng——bất thường——thế này——ưm……ha, ah」"
"2234" = "「Ưm……Ku——Cái này——Ku——phù! Ah! Đút, vào——nhét, vào rồi——phù, to, quá——!」"
"2238" = "「Fuaa! A! Aah!!? Cái này, sướng quá!\\nƯm, Ku——sướng, quá——sâu——sâu quá!!」"
"2247" = "「Nku——ưm——Mubu——Nchu——chụt——\\nChumu——Buchu——Zuji——chụt, Chubuu」"
"2279" = "「A……phù——ưm——Fua, ah」"
"2331" = "「Chụt——Reru——Jubu——Chuboooo——\\nChuru——Reru——Kupuuuuuu——Pua」"
"2334" = "「Ưm——đột nhiên, đút vào——tưởng là, sẽ dùng, dildo,\\nah——cứ nghĩ, là vậy, nhưng——Ku——Fua」"
"2342" = "「Haa! Ah! Phù! Aah——sắp, rồi!\\nƯm——cái này——một chút, nữa thôi——ưm! Fuuu!」"
"2343" = "「Haaa! Ta! Ta! Ưm! Phù! Bị nhìn thấy——bị nhìn thấy rồi!」"
"2346" = "「Fua——ah——ah——ah」"
"2352" = "「Hafu——ưm——kyu! Fua! Aah!\\nBên trong! Bên trong âm đạo! Cứ trượt đi trượt lại! Chật ních rồi!」"
"2422" = "「Fua! Ah! Ah! Ah! Sướng, quá,\\nYa! Ah! Nữa——nữa đi——Hiyoko, nữa đi!」"
"2426" = "「Ư!!!?\\nI! Kyuuuuuuuuuuuuu!!」"
"2428" = "「Nhyu——phù……Ku——Trở nên, gấp……gáp——\\nMất rồi——nhưng——Ưm!!」"
"2434" = "「Nkyuuuuuuunnnnn!!!!!」"
"2435" = "「Hia!? Ah, ya——Bị nhìn, thấy rồi! Ta! Đang lên đỉnh——Cơ quan sinh dục——Bị banh, ra——Ưm!」"
"2437" = "「Fukyuuuuuuuu!!!!!?」"
"2438" = "「Nhyu!」"
"2449" = "「Ka……ha——!!!!?」"
"2452" = "「Nkyun!!!!!」"
"2457" = "「Fua——ah——sướng——sướng quá! Phù——ah,\\nXin cô đấy——cứ thế này——cứ thế này——cứ thế này đi」"
"2458" = "「Fuaaaaaa!!!!」"
"2460" = "「Nuu!! Ah!? Mãnh liệt——mãnh liệt quá!\\nBị làm——bị làm——mãnh liệt——thế này, thì!」"
```

Kết bài