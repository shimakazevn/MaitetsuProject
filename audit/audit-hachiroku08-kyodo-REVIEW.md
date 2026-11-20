# Audit — ハチロク08_教導.txt.toml (01_Hachiroku) — 20/562 (3,6%)

## §1. Tổng quan

- **File:** `01_Hachiroku/ハチロク08_教導.txt.toml` — lớp học bảo trì đường ray (保線教室) của giáo quan Olivy trên tuyến Yunoi: đố vui về cầu, tà vẹt, hiện tượng phụt bùn (噴泥), nước ngầm, sân golf; ba vị trưởng lão (Seki, Nagare, Osamu), Nagi, Fukami, Niiroku và đền chủ Akai tham dự; xen kẽ cảnh cảm ơn nhau.
- **Phương pháp:** đọc toàn bộ 562 dòng, từng dòng đối chiếu JP + TW từ CSV3 (bộ duy nhất, xem §4). Không lấy mẫu.
- **Kết quả: 20 dòng sai / 562 (3,6%)** — đối thoại 14/410 (3,4%), độc thoại 6/152 (3,9%).
- **Phân loại:** terminology 8 (帝鉄 5, 可変パッド 1, Railord 2), name 5 (流→"Ryu" 5), pronoun 3, mistranslation 2, sfx 1, gasp 1.
- **Theo nhân vật:** オリヴィ 6, monologue 6, ニイロク 2, ハチロク 2, ふかみ 2, 凪 1, 赤井 1.
- **0 misaligned / 0 rotation / 0 contamination / 0 orphan / 0 untranslated / 0 duplicate key / 0 uncertain.**
- Nhóm VN trùng 3 cặp đều là cảm thán ngắn lặp hợp lệ: 2086/2206 「Hửm!?」 (cùng JP 「うむっ！？」), 2138/2150 「A——」 (JP 「ああ――」/「あ――」), 2231/2233 「Ồ.」 (JP 「ほー」/「ほう」).

## §2. Danh sách sửa (20 dòng)

| Key | Nhân vật | Loại | JP | TW | VN cũ | VN sửa |
|---|---|---|---|---|---|---|
| 1351 | オリヴィ | mistranslation | 『トンネルがなくて、橋梁がおおいユノイ線。保線する上で、一番』 | 於是巡線上最應當注意的是？ | …Trong việc bảo trì đường ray, thứ nhất』 | …Trong việc bảo trì đường ray, quan trọng nhất』 — 一番 = "quan trọng nhất" (câu hỏi đố dở dang, TW 最應當注意 làm chứng); "thứ nhất" đọc thành "trước hết", sai nghĩa. |
| 1385 | ニイロク | mistranslation | ……必要。ない | ……我不，需要 | ……Không. Cần thiết. | ……Không. Không cần thiết. — JP phủ định ("không cần"), VN cũ khẳng định ngược ("cần thiết"). |
| 1898 | ハチロク | pronoun | いえ――その、わたくしも確かに、おばあちゃんではありますけれども | 不——只是要這麼說，我也的確是老奶奶 | …đúng là em, cũng là một bà lão rồi… | …đúng là tôi, cũng là một bà lão rồi… — tự xưng "em" rồi nhận mình "bà lão", tự mâu thuẫn; Hachiroku dùng "tôi" ở 2063/2611/2838. |
| 1951 | 凪 | terminology | 「ロオド」 | 「人偶」 | 「lord」 | 「Lord」 — nửa sau của レイルロオド = Railord (xem 2833), phải viết hoa như danh từ riêng. |
| 2126 | オリヴィ | terminology | 帝鉄時代の保線台帳、もしかしてなくしちゃったの！？ | 帝國鐵路時代的巡線手冊 | …thời Đường sắt Hoàng gia… | …thời Teitetsu… — 帝鉄 = "Teitetsu" đã chốt; "Đường sắt Hoàng gia" là cách diễn sai (Hoàng gia ≠ Đế quốc), tiền lệ Hibiki08 2342. |
| 2187 | ふかみ | pronoun | あん、待ってよう凪ちゃん | 啊，小凪等一下我啦 | A, đợi em với, Nagi-chan…… | A, đợi mình với, Nagi-chan…… — Fukami nói trực tiếp với Nagi (bằng tuổi, quy tắc đã sửa 20/11: Fukami tự xưng "mình", không "em"/"chị" với Nagi). |
| 2210 | オリヴィ | name | うん。不陸だよねー。ナガレは、ゲンインわかってる？ | 嗯，就是空吊呀。流你知道原因出在哪裡嗎？ | …Ryu, ông có biết nguyên nhân không? | …Nagare, ông có biết nguyên nhân không? — nhân vật 流 tên Nagare (xem §2b). |
| 2476 | オリヴィ | terminology | で、その帝鉄式の保線マニュアルで、三連続のＸは、マンナカのを即交換！ | 按照帝國鐵路的巡線規範 | …kiểu Đường sắt Hoàng gia đó… | …kiểu Teitetsu đó… |
| 2698 | 赤井 | terminology | 退屈などととんでもない。可変パッドには心底感心しましたし―― | 可調撐墊可真是令我大開眼界 | …với đệm lót có thể thay đổi hình dạng đấy… | …với đệm có thể điều chỉnh đấy… — 可変パッド đã có cách diễn thống nhất trong file ("đệm có thể điều chỉnh", 2421/2766); "đệm lót có thể thay đổi hình dạng" là cách diễn khác, gây lệch thuật ngữ. |
| 2753 | ハチロク | terminology | これは、帝鉄式のやり方ですね。 | 這些都是效仿帝國鐵路的做法 | …kiểu Đường sắt Hoàng gia ạ… | …kiểu Teitetsu ạ… |
| 2794 | オリヴィ | terminology | それでもすごいよ！ ユノイせんってだって、帝鉄時代からでしょお！？ | 湯醫線可是從帝國鐵路時代開始就一直存在的吧！？ | …có từ thời Đường sắt Hoàng gia cơ mà!? | …có từ thời Teitetsu cơ mà!? (chỉ sửa phần 帝鉄; "Tuyến Yui" giữ nguyên chờ đợt thống nhất, xem §7). |
| 2823 | オリヴィ | terminology | なら、そのときのためにも！ 帝鉄式のやり方ちゃんと、おぼえておいたほうがいいから！ | 也該掌握帝國鐵路留下的這些制度呀！ | …kiểu của Đường sắt Hoàng gia! | …kiểu của Teitetsu! |
| 2833 | ふかみ | terminology | 「レイル」 | 「鐵路」 | 「Rai」 | 「Rail」 — nửa đầu của レイルロオド = Railord (xem 1951); "Rai" là viết sai chính tả của "Rail". |
| 2855 | ニイロク | sfx | （くすっ） | （嘻嘻） | (Phụt) | (Hì hì) — くすっ là tiếng cười khúc khích nén lại (TW 嘻嘻); "Phụt" là tiếng phụt hơi/nước, sai âm. |
| 3167 | monologue | name | 堰さん――いや、流さんだ。 | 堰先生——不對，是流先生 | Ông Seki—— à không, là ông Ryu. | Ông Seki—— à không, là ông Nagare. |
| 3168 | monologue | name | 堰さん、流さん、治さん。 | 堰先生、流先生和治先生 | Ông Seki, ông Ryu, ông Osamu. | Ông Seki, ông Nagare, ông Osamu. |
| 3171 | monologue | name | 堰さんと治さんが列車見張りをしてくれているゆえ、オリヴィの話し相手は流さんだ。 | 只有流先生回應奧莉薇 | …người nói chuyện với Olivy là ông Ryu. | …người nói chuyện với Olivy là ông Nagare. |
| 3202 | monologue | gasp | 苦しげな声にふりかえる。オリヴィはふらりとよろめいて――っ！！？ | 奧莉薇痛苦的聲音令我回過頭來，只見她身子一晃——！！？ | …Olivy lảo đảo, loạng choạng——!!? | …Olivy lảo đảo, loạng choạng——Ư!!? — áp nguyên mục lost-gasp-trailing của sweep, đã kiểm chứng theo JP (xem §3). |
| 3256 | monologue | pronoun | 僕らの後方を警戒していた治さんを見送って―― | 我們先是目送一直瞭望後方的治先生下橋 | Bọn tôi tiễn anh Osamu… | Bọn tôi tiễn ông Osamu… — 治 (Osamu) là một trong ba vị trưởng lão; trong file này vẫn gọi "ông Osamu" (3168/3171), "anh Osamu" là sai. |
| 3380 | monologue | name | 流さん、治さん、堰さんのお三方が一同に会する壮観は、僕もハチロクも、はじめて目にするものだ。 | 流先生、治先生、堰先生齊聚一堂 | …cả ba ông Ryu, Osamu và Seki… | …cả ba ông Nagare, Osamu và Seki… |

### §2b. Vì sao 流 là "Nagare", không phải "Ryu"

- Toàn dự án: "Nagare" xuất hiện 13 lần ở 4 file (共通12_のぞみ, ハチロク09, ハチロク14, 日々姫04), luôn là tên nhân vật 流 ("ông Nagare" / "anh Nagare"); 共通12 2135: 「Seki? Không, ta là Nagare.」 (早瀬流 tự giới thiệu); 2182: "ông nội của Fukami, ông Seki và ông Nagare".
- "Ryu" trong VN toàn dự án chỉ có 7 lần: 5 lần là tên người — cả 5 đều ở file này; 3 lần còn lại là SFX rên (lr_ふかみh2 1744, lr_凪h1 1219, lr_稀咲ポーレットh1 2507), không phải tên.
- Bản đồ `[characters]` của file này: `'3302': 'Nagare'`.
- Kết luận: file này là file duy nhất gọi nhân vật 流 là "Ryu" — 5 dòng sai tên, sửa hết về "Nagare".

## §3. Kiểm tra sweep っ-gasp

- Sweep có 2 mục cho file này: **3202 lost-gasp-trailing — áp nguyên** (đã kiểm chứng theo JP, xem bảng §2); **2085 already-rendered — giữ nguyên** (「っ！」→「Ực!」, gasp đã được diễn).
- Quét bổ sung **toàn bộ 251 dòng JP có っ**: không còn gasp nào bị sót.
  - っ cuối tiếng reo/hô (đã diễn bằng dấu !/gạch dài, giữ nguyên): 2103 わおわおーーーーーっ/きゃーーーーーーーっ → "Wow wow————!"/"Kya———————!", 2091 あわわっ――, 2108 うわわっ, 2290 はじまりはじまりーっ, 2815 じゃじゃんっ.
  - っ nhấn mạnh cuối câu/từ (tiền lệ 1474, 2428, 2588 — không phải gasp, giữ nguyên): 2076 けどっ/あのっ/そのっ, 2097 はいっ, 2131 えええっ, 2134 うそっ, 2171 ああっ, 2202 あげるっ, 2206 うむっ, 2654 たいへんっ, 1953 赤ちゃんっ.
  - っ trong từ/phương ngữ (ちっちゃ, ばってん, けん, って) — không phải gasp.
  - SFX trong ngoặc đã diễn đúng: 3448 （ふわっ）→"(Nhẹ bẫng)", 3454 （ひょいっ）→"(Bế bổng)", 3455 （がしっ）→"(Chụp lấy)", 3457 （ぎゅっ）→"(Siết chặt)", 3463 （すっ）→"(Soạt)", 3464 （ぺこっ）→"(Cúi đầu)", 3065 ピっ→"tắp!", 3430 とんっ→"bịch!".
  - Tiếng cười うふふ đã diễn đúng thành tiếng cười, không nhét gasp: 2228/2229 「うふふっ」→"Ufufu".

## §4. Kiểm tra cấu trúc

- **CSV bộ duy nhất:** 562 dòng, 0 key trùng, 0 VN trống, 0 JP trống; thư mục `translation_toml\01_Hachiroku` (không có bẫy dual-set ở file này).
- **CSV↔TOML:** 562/562 key khớp; 223 khớp tuyệt đối + 339 gộp `\n` thành khoảng trắng (TOML-2 làm phẳng literal `\n`); **0 khác biệt giá trị thực**. Comment `# JP:` trong `[script]` 562/562 khớp CSV3.
- **TOML md5 `98b197a95b59203975febf766cc038a8`**, BOM + CRLF, `[selections]` rỗng, không bản sao trùng (file ハチロク08 còn lại là 台枠問題, file khác).
- **Thẻ %l:** JP = VN ở mọi dòng (0 sai lệch thuật ngữ trong thẻ); 0 marker ruby còn trong VN.
- **JSON:** 20 mục dạng chuẩn list-of-dicts, key dạng chuỗi; jp/tw/old_vn khớp CSV3 tuyệt đối 20/20; diff-sanity: mọi fix chỉ khác old VN ở đúng chỗ sửa (kiểm tra cơ học).
- **Khối TOML:** parse OK bằng tomllib, 20 khóa, 0 sai lệch giá trị so với JSON.

## §5. Lượt soát 2

- **20/20 tái kiểm chứng, 0 bỏ, 1 sửa:** 1385 — bản nháp đầu của fix gõ nhầm dấu kết câu thành "。" (Nhật) thay vì "." (gốc); đã sửa lại, fix hiện chỉ khác VN cũ ở đúng chỗ thêm "Không ".
- Mọi fix đã đọc lại lần 2 đối chiếu trực tiếp với JP (+TW) của chính dòng đó.

## §6. Đã kiểm tra và giữ nguyên (phán đoán ghi chú)

- **1992 Soutetsu "tôi" — giữ.** Thứ tự truyện trong TOML: 1988 Osamu → 1992 → 1993 Nagare; Soutetsu đang nhận lời cảm ơn thay mặt mọi người và bảo "ngẩng đầu lên" — phía cúi đầu là nhóm các trưởng lão, nên "tôi" đúng với người lớn tuổi. Đối chiếu 2334 "Anh đang cảm ơn" (anh cảm ơn Fukami/Nagi — lúc đó anh là người cảm ơn, không phải người được cảm ơn).
- **2625 "Nghe em nói" — giữ:** "em" = Olivy (dòng kề TOML 2620 là Olivy nói); Soutetsu gọi Olivy (bé gái) là "em" hợp lý.
- **1935 "tôi" — giữ:** xưng hô với cả nhóm (全員), theo quy tắc nhóm ("bọn tôi" trung tính; dạng số ít "tôi" trong ngữ cảnh nhóm được chấp nhận, tiền lệ Paulette 14 1544).
- **Fukami tự xưng em/tớ/cháu/mình lẫn lộn — chỉ sửa 2187.** 2173 "Em sẽ gọi ngay!" (đáp lời Soutetsu nhờ gọi điện ở 2436), 2191 "Em muốn bế!" (nói với nhóm, đối tượng không rõ), 2155/2697/2773 "em" (hướng về Soutetsu/Olivy), 2485/2594 "tớ" (dạng ngang hàng, không phân cấp), 2366 "bọn cháu" / 2408 "cháu" / 2466 "cháu" (tự xưng vai cháu trước các ông/nhóm hỗn hợp) — đều giữ. Việc chuẩn hóa "mình" toàn bộ là mục chờ đợt thống nhất.
- **Olivy tự xưng "em" (2202, 2277) và "cháu" (2203, nói với ông Seki) — giữ:** "cháu" với người lớn tuổi, "em" với nhóm; nhất quán trong file.
- **Hachiroku tự xưng "em" (2487, 2844, 2847 — với Soutetsu) và "tôi" (2063, 2611, 2838 — với Olivy/nhóm) — giữ:** "em" với Soutetsu nhất quán với việc Soutetsu gọi cô ấy là "em" (2402, 2428, 2468); chỉ 1898 sửa vì tự mâu thuẫn "em… bà lão".
- **1976/2070 Hachiroku gọi Olivy là "em" (dạng xưng hô, không phải tự xưng) — giữ. 2817 Hachiroku gọi Fukami là "cô" — giữ** (cách gọi lịch sự của người lớn tuổi trong câu hỏi giả định đặt ra cho nhóm).
- **2518 Niiroku "Mong anh hãy gọi tôi" — giữ:** "anh" = Soutetsu, Railord trẻ gọi anh trai lớn hợp lý.
- **2334 Soutetsu "Anh đang cảm ơn" — giữ:** đúng quy tắc "anh" với Fukami/Nagi.
- **2402/2428/2468 Soutetsu gọi Hachiroku là "em" — giữ** (Railord dáng bé gái).
- **2567/2753 日ノ本 "Hinomoto" — giữ**, nhưng ghi chú: Hibiki08 giữ "Hinamoto" cho cùng từ này — cần chốt một cách viết chung toàn dự án (xem §7).
- **2585/2869 道床 "nền đá dăm" / "đạo sàng" — giữ**, nhất quán trong file; chưa có thuật ngữ chốt cho 道床.
- **1351 "Tuyến Yui" trong fix — giữ nguyên**, chờ đợt thống nhất Yui→Yunoi (xem §7); fix chỉ sửa phần 一番.

## §7. Chờ Hieu / đợt thống nhất (không tính sai)

- **"Yui"→"Yunoi": 12 dòng** — 1351, 1379, 1966, 2302, 2382, 2635, 2794 (đã có fix 帝鉄 ở dòng này; phần Yui giữ lại), 2828, 2840, 2850, 2868, 3335. Toàn file không có dòng nào dùng "Yunoi" (0 lần).
- **"Ohito"→"Ohitoyo": 10 dòng** — 1384, 2031, 2091, 2327, 2328, 2651, 2826, 2828, 2868, 3358.
- **日ノ本: "Hinomoto" (2567, 2753) vs "Hinamoto" (Hibiki08 đã giữ)** — cần Hieu chốt một cách viết chung trước đợt thống nhất.
- Không có câu hỏi nào khác cần Hieu trong file này; không dòng uncertain.

## §8. Khối TOML đã kiểm chứng (parse OK, 20 khóa, 0 sai lệch)

```toml
[script]
1351 = "「『Tuyến Yui không có hầm chui, nhưng lại có rất nhiều cầu đường sắt.\\nTrong việc \\x%l保線;#00ffc040;bảo trì đường ray%l;#;, quan trọng nhất』」"
1385 = "「……Không. Không cần thiết.」"
1898 = "「Dạ không—— ừm, đúng là tôi,\\ncũng là một bà lão rồi nhưng mà.」"
1951 = "「Lord」"
2126 = "「Hảảả!?\\nSổ theo dõi bảo trì đường ray thời Teitetsu, không lẽ bị mất rồi sao!?」"
2187 = "「A, đợi mình với, Nagi-chan……」"
2210 = "「Ừm. Là bị võng xuống nhỉ.\\nNagare, ông có biết nguyên nhân không?」"
2476 = "「Và theo cẩm nang bảo trì đường ray kiểu Teitetsu đó,\\n3 dấu X liên tiếp thì cái ở giữa phải thay ngay lập tức! Là vậy đó.」"
2698 = "「Nhàm chán gì chứ, hoàn toàn không đâu. Tôi thực sự rất ấn tượng\\nvới đệm có thể điều chỉnh đấy——Hơn nữa, cả Niiroku cũng vậy.」"
2753 = "「Đây là cách làm kiểu Teitetsu ạ. Trên khắp Hinomoto,\\nchắc vẫn còn những nơi áp dụng cách làm tương tự.」"
2794 = "「Thế cũng siêu lắm rồi! Tuyến Yui á,\\ncó từ thời Teitetsu cơ mà!?」"
2823 = "「Vậy thì, cũng là để chuẩn bị cho lúc đó! Tốt nhất là\\nnên nhớ kỹ cách làm theo kiểu của Teitetsu!」"
2833 = "「Rail」"
2855 = "「(Hì hì)」"
3167 = "Ông Seki—— à không, là ông Nagare.\\nÔng ấy thốt lên một tiếng đầy vẻ thán phục."
3168 = "Ông Seki, ông Nagare, ông Osamu.\\nCùng với Hachiroku và tôi được tập hợp lại một chỗ."
3171 = "Vì ông Seki và ông Osamu đang làm nhiệm vụ canh gác tàu,\\nnên người nói chuyện với Olivy là ông Nagare."
3202 = "Nghe thấy giọng nói đau đớn, tôi quay lại.\\nOlivy lảo đảo, loạng choạng——Ư!!?"
3256 = "Bọn tôi tiễn ông Osamu, người vẫn luôn cảnh giác phía sau chúng tôi——"
3380 = "Khung cảnh tráng lệ khi cả ba ông Nagare, Osamu và Seki cùng tụ họp,\\nđây là lần đầu tiên tôi và Hachiroku được chứng kiến."
```

## Kết bài

File ハチロク08_教導 là một file sạch vừa phải: **20/562 dòng sai (3,6%)**, không có lỗi hệ thống nào (không lệch dòng, không xoay vòng, không ô nhiễm chéo, không dòng mồ côi). Lỗi tập trung ở hai điểm: tên nhân vật 流 bị gọi sai thành "Ryu" ở cả 5 lần xuất hiện (file duy nhất trong dự án mắc lỗi này — toàn dự án đều gọi "Nagare"), và 帝鉄 bị diễn thành "Đường sắt Hoàng gia" ở cả 5 lần xuất hiện. Còn lại là lỗi rải rác: 1 dòng dịch ngược nghĩa (1385), 1 dòng くすっ dịch sai âm (2855), 2 mảnh từ "Railord" bị viết sai ("lord", "Rai"), 1 gasp của sweep (3202), và 3 lỗi đại từ/xưng hô (1898, 2187, 3256). Đợt thống nhất còn chờ: 12 dòng "Yui"→"Yunoi", 10 dòng "Ohito"→"Ohitoyo", và cách viết 日ノ本 ("Hinomoto" ở file này đối chiếu "Hinamoto" ở Hibiki08). Lượt soát 2: 20/20 tái kiểm chứng, 0 bỏ, 1 sửa (1385).

Kết bài
