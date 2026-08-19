# 🚂 Maitetsu — Steam Version Vietnamese Patch Module

Module đóng gói bản patch Việt hóa dành riêng cho phiên bản **Steam** (Maitetsu: Last Run!! / Pure Station).

---

## 🌟 Đặc Điểm Kỹ Thuật & Khắc Phục Lỗi Steam:

### 1. 📦 Cấu Trúc Đóng Gói Binary XP3 Chuẩn Steam (Unencrypted RAW XP3)
* **Vấn đề**: Bản Steam (`MaitetsuLastRun.exe`) không tích hợp bộ giải mã **Maitetsu CX Encryption** như bản DMM. Nếu dùng packer mã hóa của DMM, game sẽ đọc sai byte PSB và báo lỗi `invalid psb file` hoặc `Read error`.
* **Giải pháp**: Sử dụng công cụ `tools/pack_steam_plain_xp3.py` để đóng gói dữ liệu nguyên bản với cấu trúc nhị phân chuẩn 100% của Steam:
  - Cờ bảo vệ: `info.flags = 0x80000000` (`TVP_XP3_FILE_PROTECTED`).
  - Phân đoạn: `segm.flags = 0` (`TVP_XP3_SEGM_ENCODE_RAW`).
  - Thứ tự sub-chunks chuẩn: `adlr` $\rightarrow$ `segm` $\rightarrow$ `info`.
  - Nén Index luồng bằng Zlib.

### 2. 🛡️ Cách Ly File Hệ Thống (System Script Quarantine)
* **Vấn đề**: Các file script override của bản DMM (`Config.tjs`, `custom.tjs`, `scnlist_*.tjs`, v.v.) gây xung đột với binary Steam, dẫn tới lỗi `"Cannot convert given narrow string to wide string"`.
* **Giải pháp**: Đã di chuyển toàn bộ 14 file script TJS vào thư mục cách ly `quarantined_system_assets/`. Bản patch Steam chỉ đóng gói sạch các tài nguyên:
  - **Giao diện (UI)**: Toàn bộ ảnh texture, khung thoại, nút bấm (`.png`, `.csv`).
  - **TIPS**: Toàn bộ từ điển bách khoa TIPS (`tw_tips_*.txt`, `tipsindex_tw.ini`).
  - **Kịch bản SCN**: Toàn bộ 216 file kịch bản tiếng Việt đã biên dịch (`.scn`).
  - **Font chữ**: Bộ font Signika Negative (`.ttf`).

### 3. 🏆 Tương Thích Hoàn Hảo Steamworks
* Bảo toàn 100% hệ thống thành tựu (Steam Achievements) và giao diện gốc của Steam.

---

## 🚀 Hướng Dẫn Đóng Gói Patch Steam:

* **Đóng gói mặc định và tự động copy vào thư mục game Steam**:
  ```bash
  python build_steam_patch.py
  ```

* **Tùy chỉnh thư mục đích**:
  ```bash
  python build_steam_patch.py --target "E:\SteamLibrary\steamapps\common\MaitetsuLastRun" --name "patch.xp3"
  ```
