# 🚂 Maitetsu — Steam Version Vietnamese Patch Module

Module đóng gói bản patch Việt hóa dành riêng cho phiên bản **Steam** (Maitetsu / Pure Station).

## 🌟 Đặc Điểm Thiết Kế:
1. **Loại bỏ xung đột Trophy**: Không đè các script danh hiệu / INI của bản *Last Run!!*, bảo toàn 100% tích hợp Steamworks Achievement API của Steam để loại bỏ hoàn toàn lỗi `Invalid character '\x06'`.
2. **Khung thoại & Font tiếng Việt**: Tích hợp cấu hình font scale và ngắt dòng word-wrap tự nhiên.
3. **216 Kịch bản dịch hoàn chỉnh**: Đồng bộ toàn bộ các kịch bản `.scn` tiếng Việt mới nhất.

## 🚀 Cách Build:
* **Đóng gói ra `patch_steam.xp3`**:
  ```bash
  python build_steam_patch.py
  ```
* **Đóng gói và tự động copy vào thư mục Steam Game**:
  ```bash
  python build_steam_patch.py --target "Đường_Dẫn_Thư_Mục_Steam" --name "patch.xp3"
  ```
