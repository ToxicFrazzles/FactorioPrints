import zlib
import base64
from pathlib import Path
import json

HERE = Path(__file__).parent

def inflate(data):
    decompress = zlib.decompressobj(0)
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

if __name__ == "__main__":
    for filename in (HERE / "strings").iterdir():
        if not filename.is_file():
            continue

        with open(filename) as f:
            bp_string = f.read().strip()[1:]
        decoded_bp = base64.b64decode(bp_string)
        inflated_bp = inflate(decoded_bp)
        bp_object = json.loads(inflated_bp)
        name = bp_object["blueprint"]["label"]
        with open(HERE / "raw blueprints" / name, "w") as f:
            json.dump(bp_object, f, indent=4)
        # print(inflated_bp)