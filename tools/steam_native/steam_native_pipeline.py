#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
steam_native_pipeline.py - Engine-Oracle Capture pipeline cho Maitetsu Steam
=============================================================================
Sinh ra ban patch.xp3 MA HOA NATIVE (engine tu giai ma, khong can version.dll).

Nguyen ly: bo loc CX cua engine ap dung len MOI entry va la XOR involutive.
  1. (probe)   Dong goi plaintext vao probe patch.xp3 (flags=0, adler32 that)
  2. (capture) capture_version.dll hook CreateStreamByIndex -> engine "decrypt"
               plaintext, DLL ghi output (= ciphertext) vao steam_capture/
               dong thoi tra stream tho cho game de boot van chay binh thuong;
               sau 60 giay tu dong dump toan bo entry con lai
  3. (final)   Dong goi ciphertext voi info.flags |= 0x80000000 + adlr =
               adler32(plaintext) -> engine doc nhu DLC chinh chu

Cac lenh: dung build_steam_patch.py (wrapper chinh thuc) hoac import module nay.
"""

import os
import sys
import struct
import shutil
import zlib

HERE         = os.path.dirname(os.path.abspath(__file__))
PROJ         = os.path.dirname(os.path.dirname(HERE))            # E:\MaitetsuProject
SV_DIR       = os.path.join(PROJ, "steam_version_patch_vn")
PATCH_ASSETS = os.path.join(SV_DIR, "patch_assets")
COMPILED_SCN = os.path.join(PROJ, "compiled_scn")
WORK         = os.path.join(SV_DIR, "native_work")
STAGING      = os.path.join(WORK, "staging")
CAPTURE      = os.path.join(PROJ, "steam_capture")               # thu muc DLL ghi ciphertext
OUT_PROBE    = os.path.join(WORK, "probe_patch.xp3")
OUT_FINAL    = os.path.join(SV_DIR, "patch.xp3")

sys.path.insert(0, os.path.join(PROJ, "tools"))
sys.path.insert(0, PROJ)

XP3_SIG = b"XP3\r\n \n\x1a\x8b\x67\x01"
TVP_XP3_FILE_PROTECTED = 1 << 31


# ---------------------------------------------------------------- staging
def assemble_staging():
    if os.path.exists(STAGING):
        shutil.rmtree(STAGING)
    os.makedirs(STAGING, exist_ok=True)
    n = 0
    for f in os.listdir(PATCH_ASSETS):
        src = os.path.join(PATCH_ASSETS, f)
        if os.path.isfile(src):
            shutil.copy2(src, os.path.join(STAGING, f)); n += 1
    if os.path.isdir(COMPILED_SCN):
        for f in os.listdir(COMPILED_SCN):
            if f.endswith(".scn"):
                shutil.copy2(os.path.join(COMPILED_SCN, f), os.path.join(STAGING, f)); n += 1
    print("[stage] %d files -> %s" % (n, STAGING))
    return STAGING


def list_staging(staging):
    out = []
    for root, dirs, files in os.walk(staging):
        rel = os.path.relpath(root, staging)
        if rel == "scn" or rel.startswith("scn" + os.sep):
            continue
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), staging).replace("\\", "/"))
    return sorted(out)


# ---------------------------------------------------------------- pack plain (probe)
def pack_plain(staging, outpath):
    from pack_steam_plain_xp3 import pack_steam_plain_xp3
    if os.path.exists(outpath):
        os.remove(outpath)
    pack_steam_plain_xp3(staging, outpath)
    print("[probe] %s (%.1f MB)" % (outpath, os.path.getsize(outpath) / 1048576))


# ---------------------------------------------------------------- coverage
def coverage_report(staging):
    want = {}
    for name in list_staging(staging):
        data = open(os.path.join(staging, name), "rb").read()
        h = zlib.adler32(data) & 0xFFFFFFFF
        want.setdefault(h, name)
    have = set()
    for f in os.listdir(CAPTURE):
        try:
            have.add(int(f[:-4], 16))
        except ValueError:
            pass
    missing = [(h, n) for h, n in want.items() if h not in have]
    print("[verify] unique=%d captured=%d missing=%d" % (len(want), len(want) - len(missing), len(missing)))
    for h, n in missing[:15]:
        print("   MISSING %08X %s" % (h, n))
    return len(missing) == 0


# ---------------------------------------------------------------- structs
def _structs():
    import ctypes

    class Xp3Info_t(ctypes.Structure):
        _pack_ = 1
        _fields_ = [("flags", ctypes.c_uint32), ("fsize", ctypes.c_int64),
                    ("zsize", ctypes.c_int64), ("namelen", ctypes.c_uint16)]

    class Xp3Segm_t(ctypes.Structure):
        _pack_ = 1
        _fields_ = [("flags", ctypes.c_uint32), ("offset", ctypes.c_uint64),
                    ("fsize", ctypes.c_uint64), ("zsize", ctypes.c_uint64)]

    class Xp3Adlr_t(ctypes.Structure):
        _pack_ = 1
        _fields_ = [("hash", ctypes.c_uint32)]
    return Xp3Info_t, Xp3Segm_t, Xp3Adlr_t


# ---------------------------------------------------------------- pack final (native)
def pack_final(staging, outpath):
    Xp3Info_t, Xp3Segm_t, Xp3Adlr_t = _structs()
    if not coverage_report(staging):
        print("[final] ABORT: thieu captures!")
        sys.exit(1)

    entries = []
    outio = bytearray()
    outio += XP3_SIG
    outio += struct.pack("<q", 0x17)
    outio += struct.pack("<i", 1)
    outio += b"\x80"
    outio += struct.pack("<q", 0)
    idx_off_pos = len(outio)
    outio += struct.pack("<q", 0)

    for name in list_staging(staging):
        plain = open(os.path.join(staging, name), "rb").read()
        h = zlib.adler32(plain) & 0xFFFFFFFF
        cipher = open(os.path.join(CAPTURE, "%08X.bin" % h), "rb").read()
        assert len(cipher) == len(plain), "len mismatch: %s" % name
        offset = len(outio)
        outio += cipher
        entries.append((name, len(plain), h, offset))

    index_io = bytearray()
    for name, size, h, offset in entries:
        info = Xp3Info_t(); info.flags = TVP_XP3_FILE_PROTECTED
        info.fsize = size; info.zsize = size; info.namelen = len(name)
        nb = name.encode("utf-16le")
        info_data = bytes(info) + nb
        info_chunk = b"info" + struct.pack("<q", len(info_data)) + info_data

        segm = Xp3Segm_t(); segm.flags = 0
        segm.offset = offset; segm.fsize = size; segm.zsize = size
        segm_chunk = b"segm" + struct.pack("<q", 28) + bytes(segm)

        adlr = Xp3Adlr_t(); adlr.hash = h
        adlr_chunk = b"adlr" + struct.pack("<q", 4) + bytes(adlr)

        sub = adlr_chunk + segm_chunk + info_chunk
        index_io += b"File" + struct.pack("<q", len(sub)) + sub

    idx_pos = len(outio)
    comp = zlib.compress(bytes(index_io), 9)
    outio += b"\x01"
    outio += struct.pack("<Q", len(comp))
    outio += struct.pack("<Q", len(index_io))
    outio += comp
    struct.pack_into("<q", outio, idx_off_pos, idx_pos)

    open(outpath, "wb").write(bytes(outio))
    print("[final] %d entries -> %s (%.1f MB)" % (len(entries), outpath, os.path.getsize(outpath) / 1048576))
