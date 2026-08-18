@echo off
chcp 65001 >nul

:: Tắt delayed expansion để giữ nguyên dấu !! trong tên thư mục
setlocal disabledelayedexpansion

:: Tự động lấy thư mục hiện tại (nơi đang chứa file .bat này)
set "TARGET_DIR=%~dp0"
if "%TARGET_DIR:~-1%"=="\" set "TARGET_DIR=%TARGET_DIR:~0,-1%"

:: Thiết lập các đường dẫn
set "COMPILER=E:\MaitetsuProject\tjs2Compiler.exe"
set "DEST_DIR=E:\まいてつ Last Run!!\vn_patch"
set "BAK_DIR=%DEST_DIR%\bak"

:: Tạo thư mục đích và thư mục backup nếu chưa có
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"
if not exist "%BAK_DIR%" mkdir "%BAK_DIR%"

echo ==========================================
echo 1. BAT DAU BIEN DICH TAT CA FILE .TJS
echo Thu muc: %TARGET_DIR%
echo ==========================================
echo.

:: Lặp qua từng file .tjs trong thư mục và truyền vào tool
for %%F in ("%TARGET_DIR%\*.tjs") do (
    echo [*] Dang xu ly: %%~nxF
    "%COMPILER%" "%%~F" "%%~F.comp"
)

echo.
echo ==========================================
echo 2. CHUYEN FILE VA BACKUP
echo ==========================================
echo.

:: Lặp qua các file .comp vừa được tạo ra
for %%F in ("%TARGET_DIR%\*.comp") do (
    :: %%~nF sẽ lấy tên file bỏ đuôi cuối cùng (.comp) - vd: MessageLayer.tjs
    echo [*] Xu ly file: %%~nF
    
    :: Kiểm tra xem file cũ có tồn tại ở vn_patch không
    if exist "%DEST_DIR%\%%~nF" (
        echo     - Phat hien file cu, dang backup vao thu muc \bak...
        move /Y "%DEST_DIR%\%%~nF" "%BAK_DIR%\" >nul
    )
    
    :: Chuyển file .comp sang vn_patch và đổi tên (mất đuôi .comp)
    echo     - Dang di chuyen file moi sang vn_patch...
    move /Y "%%~F" "%DEST_DIR%\%%~nF" >nul
)

echo.
echo ==========================================
echo HOAN TAT TOAN BO QUA TRINH!
pause