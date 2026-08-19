import os
import io
import struct
import zlib
import ctypes
from typing import List

# TVP constants
XP3_SIG = b"XP3\r\n \n\x1a\x8b\x67\x01"
TVP_XP3_FILE_PROTECTED = 0  # 0 = UNPROTECTED / NO CX ENCRYPTION
TVP_XP3_SEGM_ENCODE_RAW = 0 # 0 = RAW DIRECT BYTES

class Xp3Info_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("fsize", ctypes.c_int64),
        ("zsize", ctypes.c_int64),
        ("namelen", ctypes.c_uint16)
    ]

class Xp3Segm_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("flags", ctypes.c_uint32),
        ("offset", ctypes.c_uint64),
        ("fsize", ctypes.c_uint64),
        ("zsize", ctypes.c_uint64)
    ]

class Xp3Adlr_t(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("hash", ctypes.c_uint32)
    ]

class Xp3Entry:
    def __init__(self, name, size, hash_val, offset):
        self.name = name
        self.size = size
        self.hash = hash_val
        self.offset = offset

def update_adler32(data: bytes) -> int:
    return zlib.adler32(data) & 0xFFFFFFFF

def pack_steam_plain_xp3(indir, outpath):
    inpaths = []
    for root, dirs, files in os.walk(indir):
        rel_dir = os.path.relpath(root, indir)
        if rel_dir == "scn" or rel_dir.startswith("scn" + os.sep):
            continue
        for file in files:
            inpath = os.path.relpath(os.path.join(root, file), indir)
            inpath = inpath.replace("\\", "/").strip("/")
            inpaths.append(inpath)

    inpaths.sort()
    print(f"Packing {len(inpaths)} raw unencrypted files to {outpath}...")

    # Write directly to disk stream
    with open(outpath, "wb+") as out_fp:
        # Write V2 Header
        out_fp.write(XP3_SIG)                          # 11 bytes
        out_fp.write(struct.pack("<q", 0x17))          # 8 bytes: 0x17 (offset 23)
        out_fp.write(struct.pack("<i", 1))             # 4 bytes: 1
        out_fp.write(b"\x80")                          # 1 byte: 0x80
        out_fp.write(struct.pack("<q", 0))             # 8 bytes: 0
        
        index_pos_offset = out_fp.tell()
        out_fp.write(struct.pack("<q", 0))             # 8 bytes placeholder for index offset

        entries: List[Xp3Entry] = []
        for inpath in inpaths:
            full_path = os.path.join(indir, inpath)
            with open(full_path, "rb") as fp:
                raw_data = fp.read()
                
            orig_size = len(raw_data)
            adlr_hash = update_adler32(raw_data)

            # Write RAW unencrypted bytes
            offset = out_fp.tell()
            out_fp.write(raw_data)

            entry = Xp3Entry(
                name=inpath,
                size=orig_size,
                hash_val=adlr_hash,
                offset=offset
            )
            entries.append(entry)

        # Build Index Stream: adlr -> segm -> info (flags = 0 for NO CX DECRYPTION)
        index_io = io.BytesIO()
        for entry in entries:
            # 1. adlr chunk
            adlr = Xp3Adlr_t()
            adlr.hash = entry.hash
            adlr_chunk = b"adlr" + struct.pack("<q", ctypes.sizeof(Xp3Adlr_t)) + bytes(adlr)

            # 2. segm chunk (RAW uncompressed)
            segm = Xp3Segm_t()
            segm.flags = TVP_XP3_SEGM_ENCODE_RAW # 0
            segm.offset = entry.offset
            segm.fsize = entry.size
            segm.zsize = entry.size
            segm_chunk = b"segm" + struct.pack("<q", ctypes.sizeof(Xp3Segm_t)) + bytes(segm)

            # 3. info chunk (flags = 0: standard unprotected file, bypasses CX decryption)
            info = Xp3Info_t()
            info.flags = 0 # 0 = UNPROTECTED / BYPASS CX
            info.fsize = entry.size
            info.zsize = entry.size
            info.namelen = len(entry.name)
            
            name_bytes = entry.name.encode("utf-16le")
            info_data_bytes = bytes(info) + name_bytes
            info_chunk = b"info" + struct.pack("<q", len(info_data_bytes)) + info_data_bytes

            # Combine in exact Kirikiri order: adlr -> segm -> info
            sub_chunks_data = adlr_chunk + segm_chunk + info_chunk
            file_chunk = b"File" + struct.pack("<q", len(sub_chunks_data)) + sub_chunks_data
            index_io.write(file_chunk)

        raw_index = index_io.getvalue()
        comp_index = zlib.compress(raw_index, 6)
        index_offset = out_fp.tell()

        # Write compressed index
        # Kirikiri 2 XP3Archive.cpp:
        # byte 0: index_flag (0x01 = TVP_XP3_INDEX_ENCODE_ZLIB)
        # int64: compressed_size (comp_index length)
        # int64: r_index_size (raw_index uncompressed length)
        out_fp.write(b"\x01")  # zlib compressed flag
        out_fp.write(struct.pack("<q", len(comp_index))) # COMPRESSED SIZE FIRST!
        out_fp.write(struct.pack("<q", len(raw_index)))  # RAW SIZE SECOND!
        out_fp.write(comp_index)

        # Patch index offset at byte 32
        out_fp.seek(index_pos_offset)
        out_fp.write(struct.pack("<q", index_offset))

    sz_mb = os.path.getsize(outpath) / (1024*1024)
    print(f"[OK] Steam-compatible unencrypted XP3 created: {outpath} ({sz_mb:.2f} MB)")

if __name__ == "__main__":
    staging = r"E:\MaitetsuProject\steam_version_patch_vn\staging_steam_patch"
    out_xp3 = r"E:\SteamLibrary\steamapps\common\MaitetsuLastRun\patch.xp3"
    pack_steam_plain_xp3(staging, out_xp3)
