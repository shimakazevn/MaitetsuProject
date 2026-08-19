# 🚂 Maitetsu — Steam Version Vietnamese Patch Module

Module đóng gói bản patch Việt hóa dành riêng cho phiên bản **Steam** (*Maitetsu: Last Run!!* / Pure Station - do Hikari Field phát hành).

---

## 🌟 Đặc Điểm Kỹ Thuật & Giải Pháp Cho Bản Steam:

### 1. 🛡️ Cơ Chế Nạp Patch Qua KrkrPatch (`version.dll`)
* **Đặc thù Steam**: Engine bản Steam (`MaitetsuLastRun.exe`) tích hợp **KrkrSign (Chữ ký điện tử RSA)** và **Bộ lọc giải mã theo bảng FileHash**. Bất kỳ file archive `.xp3` mới nào nếu không có chữ ký số private key của Hikari Field sẽ bị engine từ chối nạp hoặc XOR sai dữ liệu.
* **Giải pháp chuẩn**: Sử dụng proxy DLL `version.dll` (từ dự án [GalPatch / KrkrPatch](https://github.com/bynejake/GalPatch)) để:
  - Tự động hook và cho phép nạp dữ liệu từ `unencrypted.xp3` (hoặc thư mục `unencrypted/`).
  - Bypass bước xác thực chữ ký số KrkrSign và bỏ qua filter giải mã sai lệch đối với các file dịch tiếng Việt.
  - Bảo toàn 100% hệ thống **Steam Overlay**, **Steam Achievements (Thành tựu)** và **Cloud Save**.

### 2. 🔤 Khắc Phục Lỗi Narrow/Wide String Với TIPS (`tw_tips_*.txt`)
* **Vấn đề**: Engine Steam sử dụng API xử lý đường dẫn hẹp (Narrow String), dẫn tới crash với thông báo `Cannot convert given narrow string to wide string` khi gặp các tệp TIPS có tên chứa ký tự full-width Unicode (ví dụ: `tw_tips_Ｃ１１.txt`, `tw_tips_ＤＬ.txt`, `tw_tips_４－８－６.txt`).
* **Giải pháp**:
  - Tách biệt và lọc bỏ các tệp có tên full-width trong thư mục `steam_version_patch_vn/patch_assets/`.
  - Giữ lại 413 tệp TIPS với tên chuẩn ASCII (ví dụ: `tw_tips_C11.txt`, `tw_tips_DL.txt`) được mã hóa chuẩn **UTF-16 LE Single BOM**.

### 3. 📦 Đóng Gói Archive Tinh Gọn
* Sử dụng `Xp3Pack.exe` hoặc `build_steam_patch.py` để đóng gói toàn bộ 982 files (766 patch assets + 216 kịch bản SCN tiếng Việt) thành `unencrypted.xp3` (chỉ khoảng ~50 MB sau khi nén).

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng:

1. **Build patch cho Steam**:
   ```bash
   cd steam_version_patch_vn
   python build_steam_patch.py
   ```
2. **Cài đặt vào Game**:
   * Sao chép `unencrypted.xp3` (hoặc `patch.xp3`) và `version.dll` vào thư mục cài đặt game Steam (`.../steamapps/common/MaitetsuLastRun/`).
3. **Chơi game**:
   * Mở game trực tiếp trên Steam và thưởng thức bản dịch tiếng Việt trọn vẹn!
