"""news-image-20261125 entry program (stdlib only).

Copies the pre-rendered entry.png (1024x1024, <= 1 MiB) to the output
directory and verifies its sha256, so both graded runs write identical
bytes. Deterministic: the PNG is fixed in this repo; no network, no clock.
"""
import hashlib
import os
import shutil
import sys

EXPECTED_SHA256 = "8103345c5ea3f989deafa299f960ee77bb43adf69ff73cef640a1e07ca81d928"
# entry.png: 1024x1024, 94492 bytes. Rendered twice from gen/draw_entry.py
# (PIL + system DejaVu fonts) with byte-identical sha256; main.py copies
# those exact bytes, so both graded runs write identical output.

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        sys.exit("entry.png sha256 mismatch")
    with open(dst, "wb") as f:
        f.write(data)
    print(f"wrote {dst} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
