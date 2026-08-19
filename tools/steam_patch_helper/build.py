import subprocess
import os

bat_path = r"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars32.bat"
src_dir = r"E:\MaitetsuProject\tools\steam_patch_helper"
cmd = f'call "{bat_path}" && cd /d "{src_dir}" && cl /O2 /LD steam_patch_helper.cpp /Fe:steam_patch_helper.dll user32.lib'

res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)

dll_out = os.path.join(src_dir, "steam_patch_helper.dll")
print("DLL created successfully:", os.path.exists(dll_out))
if os.path.exists(dll_out):
    print("DLL size:", os.path.getsize(dll_out), "bytes")
