import subprocess

cmd = r'"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars32.bat" && cl /LD /EHsc version_hijack.cpp /link /OUT:version.dll user32.lib kernel32.lib'

res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print(res.stdout)
if res.returncode != 0:
    print(res.stderr)
