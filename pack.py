import zlib
import base64
from pathlib import Path
import json

HERE = Path(__file__).parent

def deflate(data):
    compress = zlib.compressobj(level=9)
    deflated = compress.compress(data)
    deflated += compress.flush()
    return deflated

if __name__ == "__main__":
    for filename in (HERE / "raw blueprints").iterdir():
        if not filename.is_file():
            continue

        with open(filename) as f:
            bp_object = json.load(f)
        name = bp_object["blueprint"]["label"]
        bp_json = json.dumps(bp_object).encode("utf-8")
        deflated = deflate(bp_json)
        encoded_bp = base64.b64encode(deflated).decode("utf-8")
        with open(HERE / "strings" / name, "w") as f:
            f.write("0")
            f.write(encoded_bp)
