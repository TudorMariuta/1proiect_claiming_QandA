from pathlib import Path
import sys

PNG_SIGNATURE = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
ROOT = Path(__file__).parent

png_file_path = Path(sys.argv[1])

def is_png(_content: bytes):
    signature = _content[:8]
    return PNG_SIGNATURE == signature

def get_resolution(_content: bytes):
    # 16-24
    wide = _content[16:20]
    hight = _content[20:24]
    # print(int(wide.hex(), base=16), int(hight.hex(), base=16))
    return int.from_bytes(wide), int.from_bytes(hight) # tuple

if not png_file_path.is_file():
    print("File not found")
    sys.exit(1)

try:
    with open(png_file_path, "rb") as fin:
        content = fin.read(24)
        if is_png(content):
            print("This is a PNG file.")
            resolution = get_resolution(content)
            print(f"Resolution {resolution[0]}x{resolution[1]}")
except OSError as err:
    print(err)
    sys.exit(1)