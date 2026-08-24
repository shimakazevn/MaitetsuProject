#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_steam_patch.py - Maitetsu Last Run!! (Steam): NATIVE encrypted patch.xp3
===============================================================================
Phuong thuc moi (Engine-Oracle Capture, KHONG can version.dll cho end-user):
    chi tiet tai tools/steam_native/README.md

Cach dung:
  python build_steam_patch.py                      # stage -> final -> sync vao game Steam
  python build_steam_patch.py --probe              # chi dong goi probe (chay sau khi doi noi dung)
  python build_steam_patch.py --install-capture    # cai capture dll + probe vao game (che do capture)
  python build_steam_patch.py --verify             # bao cao do phu captures
  python build_steam_patch.py --restore-from FILE  # deploy ban build san co (kiem tra toan ven truoc)
  python build_steam_patch.py --legacy             # (KHONG khuyen nghi) flow unencrypted.xp3 cu

Luu y: sau khi THAY DOI bat ky file nao trong patch_assets/ hay compiled_scn/,
       adler32 se doi => phai chay lai chu ky: --probe -> --install-capture ->
       (mo game ~2-3 phut) -> chay lai script khong tham so.
"""

import os
import sys
import shutil
import struct
import zlib

HERE     = os.path.dirname(os.path.abspath(__file__))
PROJ     = os.path.dirname(HERE)
PIPE_DIR = os.path.join(PROJ, "tools", "steam_native")

sys.path.insert(0, PIPE_DIR)
sys.path.insert(0, os.path.join(PROJ, "tools"))
import steam_native_pipeline as pipe   # noqa: E402

GAME_DIR      = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun"
CAPTURE_DLL   = os.path.join(PIPE_DIR, "capture_version.dll")
OUT_FINAL     = os.path.join(HERE, "patch.xp3")          # ban canonical trong repo
DMM_COPY_PATH = os.path.join(PROJ, "patch3.xp3")         # ban DMM/Mobile (ten patch3)


# ------------------------------------------------------------------ helpers
def xp3_integrity(path):
    """Kiem tra XP3 doc duoc index zlib + so entry protected. Tra (ok, n, prot, msg)."""
    try:
        size = os.path.getsize(path)
        if size < 50 * 1024 * 1024:
            return False, 0, 0, "file qua nho (%d bytes), khong the la patch hoan chinh" % size
        fh = open(path, "rb")
        hdr = fh.read(40)
        if hdr[:11] != b"XP3\r\n \n\x1a\x8b\x67\x01":
            return False, 0, 0, "sai XP3 signature"
        idx_pos = struct.unpack("<q", hdr[32:40])[0]
        fh.seek(idx_pos)
        flag = fh.read(1)[0]
        cs, rs = struct.unpack("<qq", fh.read(16))
        idx = fh.read(cs)
        idx = zlib.decompress(idx) if (flag & 1) else idx
        fh.close()
        n = prot = off = 0
        while off < len(idx):
            if idx[off:off + 4] != b"File":
                break
            csz = struct.unpack("<q", idx[off + 4:off + 12])[0]
            body = idx[off + 12:off + 12 + csz]
            pp = 0
            fl = None
            while pp < len(body):
                ct = body[pp:pp + 4]
                c2 = struct.unpack("<q", body[pp + 4:pp + 12])[0]
                d = body[pp + 12:pp + 12 + c2]
                if ct == b"info":
                    fl = struct.unpack("<I", d[:4])[0]
                pp += 12 + c2
            n += 1
            prot += 1 if (fl and fl & 0x80000000) else 0
            off += 12 + csz
        if n < 500:
            return False, n, prot, "chi %d entry (<500)" % n
        if prot != n:
            return False, n, prot, "%d/%d entry chua protected" % (n - prot, n)
        return True, n, prot, "OK (%d entries, %.1f MB)" % (n, size / 1048576)
    except Exception as e:
        return False, 0, 0, "loi doc file: %s" % e


def sync_to_game(src_path):
    ok, n, prot, msg = xp3_integrity(src_path)
    if not ok:
        print("[!] TU CHOI SYNC - file nguon khong dat chuan:")
        print("    ", msg)
        sys.exit(1)
    dst = os.path.join(GAME_DIR, "patch.xp3")
    shutil.copy2(src_path, dst)
    print("[OK] synced %d entries -> %s" % (n, dst))
    # delivery native khong can bat ky dll nao - don dep neu con sot tu che do capture
    for leftover in ("version.dll", "unencrypted.xp3"):
        p = os.path.join(GAME_DIR, leftover)
        if os.path.exists(p):
            os.remove(p)
            print("[cleanup] da xoa %s khoi thu muc game" % leftover)


def cmd_default():
    st = pipe.assemble_staging()
    if not os.path.isdir(pipe.CAPTURE):
        print("[!] Chua co captures (%s)." % pipe.CAPTURE)
        print("    Chay chu ky capture truoc:  python build_steam_patch.py --install-capture")
        sys.exit(1)
    missing = not pipe.coverage_report(st)
    if missing:
        print("[!] Do phu chua 100%% -> chay:  --probe roi --install-capture roi mo game ~2-3'")
        sys.exit(1)
    pipe.pack_final(st, OUT_FINAL)
    ok, n, prot, msg = xp3_integrity(OUT_FINAL)
    print("[integrity]", msg)
    if not ok:
        sys.exit(1)
    sync_to_game(OUT_FINAL)
    print("[DONE] Game Steam da san sang - khong can version.dll.")


def cmd_probe():
    st = pipe.assemble_staging()
    pipe.pack_plain(st, pipe.OUT_PROBE)


def cmd_install_capture():
    st = pipe.assemble_staging()
    pipe.pack_plain(st, pipe.OUT_PROBE)
    shutil.copy2(CAPTURE_DLL, os.path.join(GAME_DIR, "version.dll"))
    shutil.copy2(pipe.OUT_PROBE, os.path.join(GAME_DIR, "patch.xp3"))
    print("=" * 60)
    print("CHE DO CAPTURE DA BAT. Bay gio:")
    print("  1. Khoi dong game (lap tu Steam hoac exe truc tiep)")
    print("  2. Cho ~2-3 phut o man hinh title (thread tu dump toan bo entry)")
    print("  3. Thoat game")
    print("  4. Chay lai:  python build_steam_patch.py   (se tu dong ra khoi che do capture)")
    print("=" * 60)


def cmd_verify():
    st = pipe.assemble_staging()
    pipe.coverage_report(st)


def cmd_restore_from(src):
    src = os.path.abspath(src)
    if not os.path.exists(src):
        print("[!] Khong ton tai:", src); sys.exit(1)
    ok, n, prot, msg = xp3_integrity(src)
    print("[integrity]", os.path.basename(src), "->", msg)
    if not ok:
        sys.exit(1)
    shutil.copy2(src, OUT_FINAL)
    sync_to_game(OUT_FINAL)
    # cap nhat luon ban DMM/Mobile neu ton tai vi tri chuan
    if os.path.exists(DMM_COPY_PATH):
        shutil.copy2(src, DMM_COPY_PATH)
        print("[OK] cap nhat cung ban DMM/Mobile:", DMM_COPY_PATH)


def cmd_legacy():
    """Flow cu: unencrypted.xp3 + version.dll (chi dung khi bat luc)."""
    from pack_steam_plain_xp3 import pack_steam_plain_xp3
    st = pipe.assemble_staging()
    out = os.path.join(HERE, "unencrypted.xp3")
    pack_steam_plain_xp3(st, out)
    print("[legacy] %s (%.1f MB)" % (out, os.path.getsize(out) / 1048576))
    print("[legacy] CAN DI KEM version.dll (KirikiriUnencryptedArchive) - khuyen nghi khong su dung.")


def main():
    argv = sys.argv[1:]
    if "--probe" in argv:            cmd_probe()
    elif "--install-capture" in argv: cmd_install_capture()
    elif "--verify" in argv:         cmd_verify()
    elif "--restore-from" in argv:
        i = argv.index("--restore-from")
        cmd_restore_from(argv[i + 1] if i + 1 < len(argv) else "")
    elif "--legacy" in argv:         cmd_legacy()
    else:                            cmd_default()


if __name__ == "__main__":
    main()
