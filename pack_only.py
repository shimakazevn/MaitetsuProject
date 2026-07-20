import os
import sys
import subprocess

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

GAME_DIR       = r"E:\まいてつ Last Run!!"
VN_PATCH_DIR   = os.path.join(GAME_DIR, "vn_patch")
PATCH_FILE     = os.path.join(GAME_DIR, "patch3.xp3")
GAME_EXE       = os.path.join(GAME_DIR, "まいてつ Last Run!!.exe")

def stop_game():
    subprocess.run(
        ["powershell", "Stop-Process -Name 'まいてつ*' -Force -ErrorAction SilentlyContinue"],
        capture_output=True
    )

def pack_xp3():
    print(">>> Packing vn_patch/ into patch3.xp3...")
    sys.path.insert(0, os.path.join(GAME_DIR, "tools"))
    from make_patch3_maitetsu import pack_maitetsu_xp3
    pack_maitetsu_xp3(VN_PATCH_DIR, PATCH_FILE)
    print(">>> Packing complete!")

def restart_game():
    print(">>> Starting game...")
    subprocess.Popen([GAME_EXE], cwd=GAME_DIR)

def main():
    stop_game()
    pack_xp3()
    print("\nDone. If you want to start the game, run: python pack_only.py --restart")
    
    if "--restart" in sys.argv:
        restart_game()

if __name__ == '__main__':
    main()
