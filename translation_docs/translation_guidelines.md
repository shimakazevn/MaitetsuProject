# Hướng dẫn dịch thuật Maitetsu Last Run!! (JP ➔ VI)

Tài liệu này cung cấp bối cảnh, quy chuẩn thuật ngữ đường sắt, tính cách nhân vật và hướng dẫn định dạng kỹ thuật để đảm bảo bản dịch tiếng Việt đạt chất lượng cao nhất, tự nhiên nhất và đồng nhất trong suốt dự án.

---

## 1. Quy tắc định dạng kỹ thuật & Mã lệnh (Engine Codes)

Game chạy trên công cụ KiriKiri (KAG), các tệp kịch bản `.scn` được biên dịch chứa các nhãn, thẻ điều khiển và mã màu. Khi dịch trên CSV/TOML, cần đặc biệt lưu ý:

### 1.1. Thẻ điều khiển liên kết thuật ngữ (Hyperlink / Ruby Codes)
Game sử dụng cấu trúc liên kết để hiển thị giải nghĩa thuật ngữ (khi người chơi click vào từ sẽ hiện giải thích hoặc đổi màu):
* **Cấu trúc:** `\x%l[Từ gốc JP];#00ffc040;[Từ hiển thị]%l;#;`
* **Quy tắc dịch:** Giữ nguyên cấu trúc mã thẻ, chỉ dịch phần **[Từ hiển thị]** sang tiếng Việt. Phần **[Từ gốc JP]** phải giữ nguyên không đổi để engine tìm đúng cơ sở dữ liệu.
* **Ví dụ:**
  * Gốc: `\x%l粘着力;#00ffc040;黏著力%l;#;` (Chữ gốc JP là `粘着力`, chữ hiển thị tiếng Trung là `黏著力`)
  * Dịch sang Việt: `\x%l粘着力;#00ffc040;Lực bám đường%l;#;` (Tuyệt đối không dịch chữ `粘着力` đầu tiên!)

### 1.2. Thẻ phiên âm Furigana (Ruby Text)
Tiếng Nhật sử dụng chữ Hán kèm phiên âm trên đầu dạng `[phiên âm, chỉ số]chữ Hán`.
* **Cấu trúc:** `[すなま,1]砂撒き` hoặc `[しずおか,1]靜岡`
* **Quy tắc dịch:** Khi dịch sang tiếng Việt, **bỏ hoàn toàn** phần ký tự nằm trong dấu ngoặc vuông `[...]` và dịch từ Hán đó bình thường.
* **Ví dụ:**
  * Gốc: `[すなま,1]砂撒きを進言します`
  * Dịch sang Việt: `Kiến nghị phun cát dồn toa` (Bỏ `[すなま,1]`)

### 1.3. Ký tự xuống dòng và Dấu ngoặc thoại
* **Xuống dòng:** Sử dụng `\n` hoặc `\\n` (tuỳ thuộc vào file TOML hiển thị) để xuống dòng. Giữ nguyên vị trí ngắt dòng sao cho khung thoại cân đối.
* **Ngoặc thoại:** Giữ nguyên dấu ngoặc kép toàn chiều rộng kiểu Nhật: `「` và `」` cho lời thoại, `『` và `』` cho lời thoại lồng hoặc suy nghĩ trích dẫn.
* **Ngoặc tên nhân vật:** Giữ nguyên ngoặc vuông dày `【` và `】` ở đầu dòng thoại.

---

## 2. Bảng thuật ngữ Đường sắt & Cơ khí (Glossary)

Đây là các thuật ngữ chuyên ngành đường sắt xuất hiện liên tục trong game. Cần dịch chính xác để giữ tính chuyên nghiệp của tác phẩm:

| Thuật ngữ gốc (JP) | Bản Trung (TW) | Thuật ngữ Việt chuẩn | Giải nghĩa / Bối cảnh |
| :--- | :--- | :--- | :--- |
| **レイルロオド** | 鐵路人偶 / レイルロオド | **Railord** | Nhân hình cơ khí điều khiển đầu máy tàu hỏa. Giữ nguyên tiếng Anh "Railord". |
| **粘着力** | 黏著力 / 粘着力 | **Lực bám đường** | Ma sát giữa bánh xe chủ động của đầu máy và đường ray. |
| **砂撒き** | 放沙 / 砂撒き | **Phun cát** | Phun cát lên ray để tăng lực bám khi ray trơn trượt. |
| **制動** | 制動 / 減速 | **Hãm phanh** | Thao tác phanh tàu. |
| **常用制動** | 常用刹車 | **Phanh thường** | Chế độ phanh tiêu chuẩn khi vận hành. |
| **非常制動** | 緊急刹車 | **Phanh khẩn cấp** | Chế độ hãm phanh khẩn cấp tối đa lực hãm. |
| **滑走** | 滑走 / 打滑 | **Trượt bánh (Slide)** | Hiện tượng bánh xe bị khóa cứng và trượt đi trên ray khi phanh quá mạnh. |
| **空転** | 空轉 | **Quay trơn (Slip)** | Bánh xe quay tít tại chỗ không bám được ray khi tăng tốc. |
| **ロック** | 抱死 / 鎖死 | **Bó bánh / Kẹt phanh** | Bánh xe bị phanh khóa chặt không quay được. |
| **編組** | 編組 / 編成 | **Ghép đoàn / Tàu** | Việc kết nối các toa xe lại thành một đoàn tàu hoàn chỉnh. |
| **補機** | 補機 | **Đầu máy phụ** | Đầu máy bổ sung ở đuôi hoặc giữa đoàn tàu để đẩy/kéo hỗ trợ vượt dốc. |
| **閉塞** | 閉塞 | **Đóng đường** | Phân chia đường ray thành các phân đoạn (Block) để đảm bảo chỉ có 1 tàu chạy trên đó. |
| **転車台** | 転車台 / 轉車盤 | **Bàn quay đầu máy** | Thiết bị xoay đầu máy hơi nước 180 độ để đổi chiều chạy. |
| **煙管** | 煙管 / 煙道 | **Ống lửa / Ống lò hơi** | Các ống dẫn nhiệt đi qua bể nước trong lò hơi đầu máy hơi nước. |
| **動輪** | 動輪 | **Bánh xe chủ động** | Bánh xe nhận lực truyền từ piston để kéo tàu chạy. |
| **車掌** | 車掌 / 列車長 | **Trưởng tàu** | Người quản lý hành khách và an toàn trên tàu (không phải lái tàu). |
| **機関士** | 機關士 / 司機 | **Lái tàu / Nhân viên cơ vụ** | Người trực tiếp vận hành đầu máy. |
| **車販** | 車販 / 車售 | **Nhân viên bán hàng** | Người đẩy xe bán đồ ăn/nước uống dọc các toa tàu. |
| **保線** | 保線 / 巡線 | **Bảo trì đường ray** | Công tác duy tu, sửa chữa đường ray và nền đường sắt. |

---

## 3. Bản đồ Xưng hô & Đại từ Nhân vật (Deep Analysis)

Dựa trên phân tích thống kê toàn bộ **91,731 dòng thoại gốc**, dưới đây là cách xưng hô chuẩn xác cho từng cặp nhân vật trong game để đảm bảo giữ nguyên bản sắc văn hóa Nhật Bản và tính cách sâu sắc của họ:

### 3.1. Hachiroku (ハチロク) ➔ Soutetsu (双鉄)
* **Trong tiếng Nhật:** Gọi Soutetsu là **`双鉄様` (Soutetsu-sama)** (622 lần) hoặc **`マスター` (Master)** (30 lần). Xưng **`わたくし` (Watashi - kính ngữ)**.
* **Ngữ cảnh & Bản dịch đề xuất:**
  * **"Ngài Soutetsu"** hoặc **"Cậu Soutetsu"**: Sử dụng "Ngài Soutetsu" trong cuộc sống hàng ngày và các tình huống trang trọng để làm nổi bật phong thái của một Railord cổ điển, cực kỳ tôn kính chủ nhân.
  * **"Master"**: Sử dụng khi liên quan đến vận hành cơ khí đầu máy hơi nước 8620 (Hachiroku coi Soutetsu là Master/Người vận hành chính thức).
  * **"Chàng / Anh"**: Ở các phân cảnh cực kỳ thân mật khi tình cảm thăng hoa (hậu kỳ Route cá nhân), Hachiroku xưng "em" và gọi Soutetsu là "anh" hoặc "chàng" (như đoạn `双鉄さまっ――わたくしの――わたくしだけの――[マイ・マスター,4]愛しいお方` ➔ `Ngài Soutetsu... của em... của riêng mình em... người em yêu`).

### 3.2. Hibiki (日々姫) ➔ Soutetsu (双鉄)
* **Trong tiếng Nhật:** Gọi Soutetsu là **`にぃに` (Niini)** (899 lần) ở đời thường, nhưng trong các bối cảnh xã hội công cộng hoặc khi ngượng ngùng cô sẽ cố chuyển sang **`兄さん` (Nii-san)** hoặc **`義兄` (Anh trai nuôi)**.
* **Ngữ cảnh & Bản dịch đề xuất:**
  * **"Anh hai"** hoặc **"Anh Soutetsu"**: Trong các cảnh thường nhật ở nhà hoặc khi làm nũng nịu gọi **"Anh hai"** hoặc **"Anh Soutetsu"** (như `えへへ～！ね、にぃにぃ` ➔ `Hì hì~! Này anh hai, thêm bát nữa nhé?`).
  * **"Anh trai"**: Khi cố tỏ ra nghiêm túc hoặc ở trước mặt người lạ, cô gọi là **"Anh trai"** nhưng thực chất vẫn có chút bối rối (như `何ですか兄さん、じっと見たりして` ➔ `Có chuyện gì vậy anh trai... ý em là anh Soutetsu, sao cứ nhìn chằm chằm em thế`).

### 3.3. Reina (れいna / れいな) ➔ Mọi người
* **Trong tiếng Nhật:** Reina là một Railord có ngoại hình và tính cách như một đứa trẻ tinh nghịch. Tự xưng là **`れいな` (Reina)** ở ngôi thứ ba (13 lần) và kết thúc bằng đuôi điệu đà `ですぅ` (desuuu).
* **Ngữ cảnh & Bản dịch đề xuất:**
  * Với **Paulette**: Gọi là **"Chị Paulette"** hoặc **"Master"** (Paulette là chủ sở hữu của Reina).
  * Với **Soutetsu**: Gọi là **"Anh Soutetsu"** (xưng Reina).
  * Cách dịch lời thoại: Thêm các từ cảm thán dễ thương ở cuối câu: `nha`, `nhá`, `ạ`, `dạ` (như `れいなのマスターのポーレットです` ➔ `Đây là chị Paulette, Master của Reina đó nha~`).

### 3.4. Navi (ナビ) ➔ Soutetsu (双鉄)
* **Trong tiếng Nhật:** Trợ lý ảo AI của Aircra. Gọi Soutetsu là **`双鉄様` (Soutetsu-sama)** (61 lần) hoặc **`ご主人様` (Goshujin-sama / Chủ nhân)**.
* **Ngữ cảnh & Bản dịch đề xuất:**
  * **"Ngài Soutetsu"** / **"Chủ nhân"**: Mang phong thái của một trí tuệ nhân tạo phục vụ tối ưu cho sự an toàn của Soutetsu (như `ナビは、双鉄様の命を最優先として判断します` ➔ `Navi luôn đưa ra quyết định với ưu tiên hàng đầu là mạng sống của ngài Soutetsu`).

### 3.5. Cách xưng hô của các nhân vật khác dành cho Soutetsu:
* **Fukami (深美) ➔ Soutetsu**: Gọi là **`双鉄お兄さん` (Soutetsu-oniisan)**. Đề xuất dịch: **"Anh Soutetsu"** (Fukami có tính cách hiền lành, lễ phép).
* **Nagi (凪) ➔ Soutetsu**: Gọi là **`にーさん` (Nee-san)** hoặc **`双鉄お兄さん`**. Đề xuất dịch: **"Anh Soutetsu" / "Anh hai"**.
* **Kisaki (稀咲) ➔ Soutetsu**: Gọi là **`日々姫さんのお兄さん`** (Anh trai của Hibiki) hoặc **`双鉄さん`**. Đề xuất dịch: **"Anh trai chị Hibiki" / "Anh Soutetsu"**.
* **Soutetsu ➔ Hibiki / Paulette**: Gọi thẳng tên không kèm kính ngữ: **"Hibiki"**, **"Paulette"**. Xưng **"Tôi"** (hoặc **"Anh"** tùy thuộc vào mối quan hệ trong route tương ứng).

---

## 4. Quy trình dịch thuật nhóm qua Google Sheets

Để dịch nhóm hiệu quả, hãy tuân thủ quy trình sau:
1. **Xuất CSV:** Chạy `extract_all.bat` để cập nhật TOML, sau đó chạy `python toml_to_csv.py` để tạo tệp `maitetsu_translation.csv`.
2. **Upload Google Sheets:** Tạo một bảng tính Google Sheets mới, Import tệp CSV này vào (chọn bảng mã UTF-8).
3. **Phân công dịch:** Mọi người dịch trực tiếp vào cột **Vietnamese**. Tuyệt đối không thay đổi thứ tự các cột khác.
4. **Tải về & Ghi đè:** Xuất bảng tính từ Google Sheets dưới dạng `.csv` (chọn tải xuống CSV), lưu đè vào file `E:\MaitetsuProject\maitetsu_translation.csv`.
5. **Cập nhật TOML & Build:** Nhấp đúp chuột vào [build_patch.bat](file:///E:/MaitetsuProject/build_patch.bat) để tự động cập nhật bản dịch từ CSV vào hệ thống game và chạy thử.
