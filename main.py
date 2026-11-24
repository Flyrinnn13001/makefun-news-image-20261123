#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261123 bounty.

The entry is a single picture: entry.png, kept beside this file, sums up
the world news of Monday 23 November 2026 in a dense front page: 52 dated
stories in 7 regions, a 4-story lead strip, a day-in-numbers box and a
ticker of six more stories. The sandbox has no network and reads nothing
but the image this program writes, so the program's whole job is to place
those exact bytes at the output location:

    <output dir>/entry.png

The output dir is $MAKEFUN_OUTPUT_DIR when that variable is set (a local
run) and /output otherwise (the grader's container). Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Python 3.13, standard library only. The copy is byte for byte, so two runs
always write the same file.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
