# Unification batch U11b — §3 M3: re-examine already-merged "Á" rows for the ひゃ/ひゅ/ひあ/きゃ family

- **Mục:** §3 M3 (DECIDED 21/11 ~11:55, Muse theo uỷ quyền; xem `UNIFICATION-LIST.md` §3 M3 + `moans/MOAN-BRIEF.md` quy tắc 3b).
- **Quy tắc:** trong dòng rên H-scene, ひゃ/ひゅ/ひあ/きゃ → ROMAJI (Hya/Hyu/Hia/Kya; んひゅ→Nhyu, んひゅん→Nhyun; độ dài nguyên âm theo công thức — số nguyên âm romaji = 1 + số mora thêm sau mora gốc). "Á" cho họ này là LỖI MẤT ÂM. "Á" chỉ đúng khi JP không có phụ âm mora (あっ/あぁ). Nói ngọng khi miệng đầy (ひっはひ/ひょはひょひょ) KHÔNG phải dòng rên — không đụng.
- **Kết quả: 1 dòng sửa, 1 file** (凪ふかみh1 1218). 36 dòng ứng viên còn lại đã đọc JP (+TW) từng dòng và GIỮ NGUYÊN, có lý do (xem §3).
- **Trùng lặp với batch đã gộp: 0.** Không dòng nào trong đợt này trùng (file,key) với 18 file unification đã gộp (2.305 cặp duy nhất); không có composition nào cần ghép.
- **Nguồn `old_vn`:** theo thứ tự đã hiệu chỉnh — unification-đã-gộp > moan > audit > CSV3 (good set, 87.833 dòng). Chỉ load 18 file `unification-*-wrong.json` đã gộp; không có file worker đang chạy nào (U8/U10b) trên đĩa lúc làm đợt này, nên không có gì phải loại.

## §1. Phạm vi và phương pháp liệt kê (chỉ đếm bằng script)

1. Dựng map giá trị hiện tại project-wide: CSV3 good set (bỏ 3.898 dòng stale của 10 file dual-set theo `dual-csv-sets.md`) → ghi đè bằng audit fix (9.130 cặp áp được; 257 `fix: null` là dòng uncertain — bỏ qua; 67 không khớp (file,key,JP) — toàn bộ thuộc `audit-00common14`, không liên quan đợt này) → ghi đè bằng moan fix (1.535 cặp, khớp 100%) → ghi đè bằng unification đã gộp (2.305 cặp duy nhất).
2. Liệt kê thô: mọi dòng mà giá trị hiện tại chứa "Á"/"á" VÀ JP chứa mora họ ひゃ/ひゅ/ひあ/きゃ (kể cả きゅ/ひゅ giả — xem bước lọc): **441 dòng** (266 trong 63 file H, 175 ngoài file H).
3. Lọc token: chỉ giữ dòng có token rên "Á"/"á" độc lập (tách theo khoảng trắng, `\n` và dấu gạch ——/――/-): **37 dòng** trong file H. Các token "Á"/"á" còn lại đều nằm trong từ thường ("quá", "cá", "đã", "cái"… — không phải token rên).
4. Quét đối chứng (sweep A): mọi dòng file H mà JP có mora họ này, VN có "Á"/"á", nhưng VN KHÔNG chứa bất kỳ token romaji họ này (Hya/Hyu/Hia/Kya) nào: **8 dòng** — bắt thêm ふかみh1 995 (đã có trong 37) và 6 dòng loại trừ (xem §3.5). Không dòng nào bị sót ngoài 37 + 8 này.
5. Đọc JP (+TW) từng dòng trong 37 dòng, căn token "Á" với từng mora JP theo thứ tự: token "Á" chỉ tính là lỗi M3 khi nó là cách diễn DUY NHẤT của một mora họ ひゃ/ひゅ/ひあ/きゃ. Kết quả: **1 dòng lỗi, 36 dòng giữ**.

Tiền lệ đối chứng: trong cùng file 凪ふかみh1, vòng rên đã chuyển 8 dòng "Á" họ ひゃ sang romaji (1214 ひゃふっ→Hyafu, 1216 ひゅあっ→Hyua, 1219 ひゃっ→Hya, 1221 ひゅふっ→Hyufu, 1222 ひゃうっ→Hyau, 1223 ひゃんっ→Hyan, 1224 ひあっ→Hia, 1226 ひゃぷっ→Hyapu) — chỉ sót 1218, vì fix rên của 1218 chỉ đổi phù→Fua mà để nguyên "Á" đầu dòng.

## §2. Dòng sửa (1 dòng)

### 凪ふかみh1_修学旅行の夜 — key 1218 (Fukami)

- **JP:** 「きゃあっ――んっ――やっ――熱っ――ふあっ――」
- **TW:** 「呀……嗯……哎呀……好熱……呼……」
- **old_vn** (moan fix): 「Á——ưm——á——nóng quá——Fua——」
- **fix:** 「Kyaa——ưm——á——nóng quá——Fua——」
- **Lý do:** きゃあっ là rên H-scene (chuỗi rên liên tục: きゃあっ――んっ――やっ――熱っ――ふあっ), "Á" làm mất hoàn toàn phụ âm ky- — đúng lỗi M3. Romaji theo công thức: きゃ + あ = "Kyaa" (2 nguyên âm a; tiền lệ: ひゃああ→"Hyaaa" 3 a, ひゃあっ→"Hyaa" 2 a). Dấu っ cuối ngầm hiểu, JP không có !/? ở token này nên không thêm. Các token còn lại giữ nguyên đúng fix rên: んっ→"ưm", やっ→"á" (không thuộc họ này; xem §3.1), 熱っ→"nóng quá", ふあっ→"Fua". Một dòng = một cách diễn cho mỗi token rên (không trộn VN/romaji trong cùng một token).
- **Nguồn old_vn:** moan fix (`moan-nagifukamih1-shuugaku-ryokou-no-yoru-wrong.json`: old CSV3 「Á——ưm——á——nóng quá——phù——」 → fix rên 「Á——ưm——á——nóng quá——Fua——」). CSV3/TOML-2 vẫn giữ giá trị cũ 「…phù——」 (TOML key 1218 bare, đã kiểm chứng trực tiếp trong file `07_Nagi_Fukami/#U51ea#U3075#U304b#U307fh1_#U4fee#U5b66#U65c5#U884c#U306e#U591c.txt.toml`).

## §3. Dòng đã đọc nhưng GIỮ NGUYÊN (36 dòng)

Nguyên tắc căn token: trong mọi dòng dưới đây, mora họ ひゃ/ひゅ/ひあ/きゃ ĐÃ được diễn bằng romaji (Hya/Hyu/Hia/Kya…), còn token "Á"/"á" căn đúng với một mora KHÁC (あっ, やっ, tiểu từ địa phương ばい/けん/から, ぁっ, にっ/こっ/ちゃんっ…). Không dòng nào trong số này có "Á" là cách diễn duy nhất của mora họ ひゃ.

### §3.1 "Á" diễn やっ — giữ theo M8 (U12a đã quyết: や theo sau là lời nói/từ chối → "Á") — 5 dòng

- ハチロクh8_桜色のひめごと 706: ひゃぎゅっ→Hyagyu; やっ、ちくびっ→"Á, núm vú".
- lr_凪h2_虎さんの交尾 1187: ひゃうううっ→Hyauuu; やっ!→"Á! Không chịu!" (từ chối).
- ポーレットh5_裸エプロンのレモンドレッシング和え 933: ひゃうっ→Hyau; やっ→"Á——tuột ra!?".
- ポーレットh8_気動車の国のアリス 2187: やっ→"Á——vừa rồi"; んひゃうっ→Hyau.
- (Cùng nhóm, căn やっ trong chuỗi rên:) ハチロクh1_契り 1222: ひあっ→Hia; やっ→"á——cái này".

### §3.2 "Á"/"á" diễn あっ/ああっ (JP không có phụ âm mora — "Á" đúng theo quy tắc) — 14 dòng

- ポーレットh1_ファーストセックス 976: ひゃっ→Hya; あっ→"á——tử cung".
- ポーレットh2_制服変更？ 1019: んひゅっ→Nhyu; あっ→"Á——Nfuuuuu".
- ポーレットh2_制服変更？ 991: あ……ひあ……あっ――ふぁ――あっ――あっ――あ → "A... hia... á——Fa——á——á——a." (căn 1:1, 7 âm → 7 token; "á" ×3 đều là あっ).
- ポーレットh2_制服変更？ 942: きゃふっ→Kyafu; あっ→"Á——to".
- ポーレットh2_制服変更？ 964: ぁっ→"á"; ひゅあっ→"hyua".
- ポーレットh2_制服変更？ 955: ひゃっ→"hya"; あっ→"á".
- ポーレットh2_制服変更？ 929: ひゃっ→Hya; あっ→"á!".
- 稀咲h3_チャイナドレスでおもてなし 2197: ひあっ→Hia; あっ→"á!".
- 稀咲h3_チャイナドレスでおもてなし 2155: ひゅあ→Hyua; あっ→"á!".
- 稀咲h3_チャイナドレスでおもてなし 2165: ヒャっ→Hya; あっ→"Á".
- 稀咲h3_チャイナドレスでおもてなし 2160: ひゃんっ→Hyan; あっ→"Á".
- 稀咲h3_チャイナドレスでおもてなし 2195: ひあっ→Hia; あっ→"á" ×2; ああっ→"á á" (2 a).
- 真闇h3_補習授業の廃校舎 2216: ひあっ→"hia"; あっ→"á".
- れいなh4_ふたりっきりのハロウィン 2013: ひゃうんっ→Hyaun; あっ→"Á" và "á".

### §3.3 "á" là tiểu từ địa phương / tiểu từ câu (phương ngữ Nagi ばい/けん/から, よかぁ…) — 11 dòng

- 凪h1_ふたりっきりのデート 1051: ひゃ→Hya; "á" diễn ば ("Mồ hôi, á").
- 凪h1_ふたりっきりのデート 1062: ひあっ→Hia; "á!?" là tiểu từ cuối câu.
- 凪h1_ふたりっきりのデート 1108: ひあっ→Hia; "á" diễn ばいっ.
- 凪h2_おとなの水着 2419 / 2420 / 2414 / 2398 / 2412 / 2418 / 2531: ひゃああ/ひあああ/ひーひゃん đều đã romaji (Hyaaa/Hiaaa/Hiihyan); "á" cuối câu diễn ばい/けん/からあっ/よかぁ.
- 凪h2_おとなの水着 2620: ひゃっ→Hya; "á" diễn ばい ("bắt đầu lại trò chơi á——Hya!?").

### §3.4 "á" diễn mora khác (んあっ, にっ/こっ/ちゃんっ, もうっ) — 5 dòng

- lr_稀咲h1_おしおきとごほうび 997: きゃっっ→"Kya!!!?"; "á!?" diễn んあっ ("Ưn á!?").
- れいなh1_おかあさんのレッスン 1343: ひゃっ→Hya; "á" diễn にっ ("ở chỗ kín, á").
- 真闇h2_無濾過 1094: ひあっ→"hia"; "á" diễn こっ ("bướm, á").
- 真闇h3_補習授業の廃校舎 2184: ひゃあああん→Hyaaaan; "á" diễn ちゃんっ ("chị, á").
- 稀咲h3_チャイナドレスでおもてなし 2159: ひゃうっ→Hyau; "á!" cuối diễn もうっ.

### §3.5 Trường hợp ranh giới — GIỮ, cờ cho điều phối

- **ふかみh1_ともはり練習 995 — GIỮ, cờ ranh giới M3:** JP 「えっ！？ あっ！ 双鉄さん、今こっちに来ちゃっ―― / きゃっ！？ わあああああっ！？」 (TW 「哎！？啊！雙鐵先生，現在千萬別過來……呀！？哇！？」), old_vn (audit fix) 「Hả!? A! Anh Soutetsu, khoan hẵng qua đây—— / Á!? Oa a a a a a a a!?」. Đây là tiếng hét GIẬT MÌNH (Soutetsu sắp bước vào lúc Fukami đang tập tomohari), không phải tiếng rên khoái cảm: chuỗi えっ/あっ/きゃっ/わあああ toàn là thốt lên vì bất ngờ. "Á!?" là cách diễn tiếng hét đã chuẩn toàn dự án cho きゃっ giật mình (hàng chục dòng ngoài file H, vd. 共通05 2262, 共通07 1754/1755 — xem §4). Đổi thành "Kya!?" ở đây sẽ vừa lệch chuẩn tiếng hét toàn dự án, vừa đổi nghĩa (giật mình → rên). Vòng rên cũng đã để nguyên dòng này (không có trong moan fix list của file). **Nếu điều phối muốn mở rộng M3 sang cả tiếng hét giật mình trong file H, dòng này (cùng các dòng hét ngoài file H) cần một quyết định riêng — không tự mở rộng trong đợt này.**

### §3.6 Sweep A — các dòng loại trừ (không phải token "Á" diễn mora họ này)

- lr_ポーレットh2 1025: くひゅっ→"Khíu!" (giữ k- của く + híu; "á" chỉ nằm trong "quá").
- lr_稀咲ポーレットh1 2086: ひゅーひゅー là lời kể (tiếng rít trong cổ họng), không phải dòng rên.
- れいなh4 2925: きゃらきゃら là lời kể (cười khúc khích), không phải dòng rên.
- ポーレットh2 997: きゃ trong しなきゃ là ngữ pháp ("phải dọn dẹp"), không phải âm rên; "á" nằm trong "các".
- ポーレットh4 969: ひゅごっ được diễn theo NGHĨA ("Tuyệt——quá"), ひうっ→"Hiu" — không có token "Á" nào diễn mora họ này; ngoài phạm vi M3 (dòng rên theo nghĩa của vòng rên, không đụng).
- 日々姫h6 2359: こぎゃん là từ địa phương (こんな), không phải âm rên.

## §4. Ngoài phạm vi (ghi nhận, không đụng)

- **175 dòng ngoài file H** có "Á"/"á" + JP chứa mora họ này (vd. きゃっ giật mình → "Á!?" ở 共通05/07/08/09, ハチロク02/03/04/06…). Toàn bộ là tiếng hét giật mình/ngạc nhiên trong thoại thường, không phải dòng rên H-scene — ngoài phạm vi M3 ("dòng rên H-scene"). Không đổi dòng nào; nếu điều phối muốn thống nhất cả tiếng hét, đó là quyết định riêng (và sẽ phải đổi cả trăm dòng).
- Không đụng dòng gasp-Ư nào, không đụng dòng "Kh" nào.

## §5. Quyết định trong đợt (theo uỷ quyền)

- (D1) "Á" chỉ tính là lỗi M3 khi nó là cách diễn DUY NHẤT của một mora họ ひゃ/ひゅ/ひあ/きゃ trong dòng rên — căn token theo thứ tự JP. "Á" diễn あっ/やっ/tiểu từ địa phương/mora khác thì giữ (bằng chứng: 36/37 dòng ứng viên giữ theo đúng tiêu chí này).
- (D2) Tiếng hét giật mình きゃっ trong file H (ふかみh1 995) KHÔNG tính là dòng rên M3 — giữ "Á!?" theo chuẩn tiếng hét toàn dự án; cờ lại cho điều phối thay vì tự mở rộng phạm vi.
- (D3) Độ dài "Kyaa" cho きゃあっ: 2 a (きゃ + あ), theo công thức đếm mora; っ cuối ngầm hiểu, không thêm !/? vì JP không có.

## §6. Lượt soát 2 (second pass)

Đọc lại toàn bộ fix (1 dòng) đối chiếu JP + TW, kiểm tra từng token theo thứ tự, đếm lại số a, kiểm tra dấu gạch và old_vn khớp map giá trị hiện tại (moan fix), kiểm tra trùng lặp với 18 file unification đã gộp, parse-verify khối TOML.

- **Tổng số: 1 / Tái kiểm chứng: 1 / Loại bỏ: 0 / Sửa lại: 0.**

## §7. Khối TOML (parse-verified)

File: `translation_toml/07_Nagi_Fukami/凪ふかみh1_修学旅行の夜.txt.toml` (trên đĩa: `#U51ea#U3075#U304b#U307fh1_#U4fee#U5b66#U65c5#U884c#U306e#U591c.txt.toml`). TOML-2 hiện giữ giá trị CSV3 cũ 「Á——ưm——á——nóng quá——phù——」 ở key 1218 (bare key, đã kiểm chứng trực tiếp); khối dưới đây thay bằng giá trị fix (giá trị rebuild lấy từ JSON, old_vn trong JSON là moan fix).

```toml
[script]
"1218" = "「Kyaa——ưm——á——nóng quá——Fua——」"
```

Khối TOML 1 file / 1 key parse-verified (giá trị khớp fix từng key). Không có ký tự `\n` literal trong fix nên không cần escape.

## Kết bài

Đợt U11b rà toàn bộ dự án theo thứ tự giá trị hiện tại (unification-đã-gộp > moan > audit > CSV3): 441 dòng thô → 37 ứng viên token "Á" trong file H → **1 dòng sửa duy nhất (凪ふかみh1 1218, きゃあっ→"Kyaa")**, 36 dòng giữ có lý do từng dòng (Á diễn あっ/やっ/tiểu từ địa phương/mora khác, mora họ này đã romaji). Vòng rên trước đó đã làm gần như sạch họ này: 8 dòng "Á" họ ひゃ trong cùng file 凪ふかみh1 đều đã thành romaji, chỉ sót đúng 1218 vì fix rên chỉ đổi token ふあ. Cờ duy nhất cho điều phối: ranh giới tiếng hét giật mình きゃっ trong file H (ふかみh1 995) — giữ "Á!?" theo chuẩn toàn dự án, chờ quyết riêng nếu muốn mở rộng M3 sang tiếng hét (cả trong và ngoài file H).
