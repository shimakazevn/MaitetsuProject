# ✍️ Maitetsu Last Run!! — Hướng Dẫn Quy Chuẩn Dịch Thuật TOML

Tài liệu này hướng dẫn các quy tắc kỹ thuật khi dịch các tệp scenario `.toml` trong thư mục `translation_toml/`.

---

## 1. Cấu Trúc File TOML Kịch Bản
Mỗi tệp kịch bản bao gồm 3 phần chính:
```toml
[characters]
"双鉄" = "Soutetsu"
"ハチロク" = "Hachiroku"

[character_subs]

[scenes]
0001 = "Chào buổi sáng, Hachiroku."
0002 = "Dạ vâng, chào buổi sáng, thiếu gia Soutetsu."
```

---

## 2. Quy Tắc Escape Ký Tự Bắt Buộc

Trình biên dịch SCN Rust (`scn-script-inserter.exe`) yêu cầu xử lý chuỗi nghiêm ngặt:
1. **Dấu gạch chéo ngược (`\`)**: Nếu muốn hiển thị dấu `\`, phải viết `\\`.
2. **Ký tự xuống dòng (`\n`)**:
   * Khi ngắt dòng thủ công trong câu, viết `\n`.
3. **Ký tự nháy kép (`"`)**:
   * Phải escape bằng `\"` (ví dụ: `\"Xin chào!\"`).
4. **Không sử dụng ký tự escape mã byte lạ**: Tránh dùng `\x` hoặc `\u` không hợp lệ trong chuỗi TOML.

---

## 3. Quy Ước Văn Phong & Tên Nhân Vật

* **Danh xưng nhân vật chính**:
  * `双鉄` $\rightarrow$ `Soutetsu`
  * `ハチロク` $\rightarrow$ `Hachiroku`
  * `日々姫` $\rightarrow$ `Hibiki`
  * `ポーレット` $\rightarrow$ `Paulette`
  * `れいな` $\rightarrow$ `Reina`
  * `真闇` $\rightarrow$ `Mayami`
  * `稀咲` $\rightarrow$ `Kisaki`
  * `凪` $\rightarrow$ `Nagi`
  * `ふかみ` $\rightarrow$ `Fukami`
  * `ニイロク` $\rightarrow$ `Niiroku`
  * `オリヴィ` $\rightarrow$ `Olive` / `Olivia`
* **Dấu ngoặc thoại**:
  * Giữ nguyên ngoặc vuông tiếng Nhật `「` và `」` để căn chỉnh lề khung thoại chính xác.
* **Nguyên tắc dịch**:
  * Dịch trực tiếp từ nguyên tác tiếng Nhật trong file đối chiếu hoặc comment để đảm bảo khớp 100% với giọng lồng tiếng (voiceover).

---

## 4. Kiểm Tra & Biên Dịch Sau Khi Dịch
Sau khi chỉnh sửa xong 1 file `.toml`:
```bash
python build_patch.py <tên_file>.txt.toml --restart
```
Game sẽ tự động biên dịch file đó và khởi chạy ngay để bạn duyệt trực tiếp trong game.
