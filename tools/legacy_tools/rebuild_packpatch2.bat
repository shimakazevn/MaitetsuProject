@echo off
REM Rebuild PackPatch2.exe from PackPatch2.cs
REM Requires .NET Framework 4.8 csc.exe

set NETFW=C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe
set WORKDIR=%~dp0reflect_app\netfw

echo Compiling PackPatch2.exe...
cd /d "%WORKDIR%"

"%NETFW%" /unsafe /r:GameRes.dll /r:ArcFormats.dll /r:System.ComponentModel.Composition.dll /r:System.IO.Compression.dll /out:PackPatch2.exe PackPatch2.cs

if %ERRORLEVEL% EQU 0 (
    echo.
    echo SUCCESS: PackPatch2.exe compiled.
) else (
    echo.
    echo FAILED: Compilation error.
)
pause
