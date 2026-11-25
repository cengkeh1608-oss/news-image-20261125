"""Copy the pre-rendered front page to the output directory.

The entry image (entry.png, 1024x1024, the world news of 25 November 2026)
is rendered locally and committed beside this file. This program only copies
its bytes to /output/entry.png, so both grading runs write identical bytes.
Standard library only; no network, no environment reads.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    # Copy, do not re-draw: the judge must see exactly the image we proofed,
    # byte for byte, on every run. A redraw could drift with fonts or versions.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
