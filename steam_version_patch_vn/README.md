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

### 3. 🎭 Bảo Toàn Nhân Vật & Mã Lệnh E-mote SCN (Phôi Steam SCN Riêng Biệt)
* **Vấn đề cốt lõi**: File kịch bản `.scn` của bản DMM có bảng opcode và ánh xạ actor ID khác với bản Steam. Tuyệt đối không dùng trực tiếp file nhị phân SCN nguyên bản của DMM nạp vào Steam vì sẽ gây lỗi **Fatal Crash** và làm nhân vật biến mất.
* **Giải pháp chuẩn & Nguồn dữ liệu SCN**:
  - Toàn bộ 216 phôi SCN nguyên bản của Steam đã được trích xuất và biên dịch cùng kịch bản Việt hoá thành công.
  - **Từ nay về sau**, chúng ta sẽ thống nhất sử dụng toàn bộ các file SCN đã dịch tại thư mục gốc `E:\MaitetsuProject\compiled_scn\` làm nguồn chuẩn để build patch cho Steam. Không cần phải tự biên dịch lại từ đầu trừ khi có thay đổi text việt hoá.

### 4. 📦 Hai Phương Thức Đóng Gói Patch Cho Steam

* **Cách 1: Gói `unencrypted.xp3` (Qua proxy KrkrPatch `version.dll` - Tối ưu cho Test/Dev)**:
  - Chạy `python steam_version_patch_vn/build_steam_patch.py`.
  - Tự động nén toàn bộ tài nguyên patch thành `unencrypted.xp3` (~50 MB).
  - Tự động sync sang thư mục game Steam `E:\SteamLibrary\steamapps\common\MaitetsuLastRun\`.
* **Cách 2: Gói Patch Mã Hóa Native (Qua KrkrExtract GUI - Chuẩn phát hành chính thức)**:
  - Mở KrkrExtract GUI gắn vào game đang chạy.
  - Tại khung **Pack Setting**:
    - **Base Dir**: Chọn thư mục chứa asset Việt hóa (`steam_version_patch_vn/patch_assets/` + SCN đã compile).
    - **Original Archive**: Chọn `others.xp3` hoặc `data.xp3` của Steam.
    - **Output Archive**: Đặt tên file xuất ra (ví dụ: `patch.xp3`).
    - Nhấn **Make Archive** (hoặc **Make Universal Patch**) để sinh patch mã hóa chuẩn Steam.

### 5. 🗄️ Bộ Dữ Liệu Gốc Backup Toàn Diện (`KrkrExtract_Output/`)
* Thư mục `steam_version_patch_vn/KrkrExtract_Output/` chứa đầy đủ 23 phân hệ archive gốc của Steam (gồm `data`, `data2`, `others`, `bgimage`, `bgm`, `voice`, toàn bộ 11 gói DLC `patch_append*`).
* Đây là nguồn dữ liệu chuẩn 100% (Baseline Truth) để trích xuất phôi SCN, đối soát bảng mã, và lấy layer hình ảnh giao diện gốc của Steam.

---

## 🚀 Hướng Dẫn Cài Đặt & Sử Dụng:

1. **Build patch cho Steam**:
   ```bash
   cd steam_version_patch_vn
   python build_steam_patch.py
   ```
2. **Cài đặt vào Game**:
   * Sao chép `unencrypted.xp3` và `version.dll` vào thư mục cài đặt game Steam (`.../steamapps/common/MaitetsuLastRun/`).
3. **Chơi game**:
   * Mở game trực tiếp trên Steam và thưởng thức bản dịch tiếng Việt trọn vẹn!

