"""ai-happy-01 entry: emit one happy image (corgi puddle-leap iteration).

Stdlib only, no network, deterministic: the program copies the exact bytes
of entry.png beside it to $MAKEFUN_OUTPUT_DIR/entry.png on every run.

Gate constraints (verified): the image is a whole PNG of 974,777 bytes
(at most 1 MiB) and 784 by 784 pixels (at most 1024 by 1024). The picture
is one specific joyful moment: a corgi mid-leap through a puddle, ears
flying, in golden light — instant happiness, one mood, reads small.
"""

import os
import shutil

IMAGE_NAME = "entry.png"


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), IMAGE_NAME)
    shutil.copyfile(src, os.path.join(outdir, IMAGE_NAME))


if __name__ == "__main__":
    main()
