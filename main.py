#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 make.fun entry.

The deliverable for this competition is a single PNG that lives next to
this script as ``entry.png``.  Running this program publishes that image
by copying it into ``/output/entry.png`` (creating ``/output`` when it is
not there yet) and then double-checks that the published file is present
before reporting success.
"""

import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DESTINATION_DIR = Path("/output")


def publish_image() -> int:
    """Copy the bundled entry image into /output; return an exit code."""
    source = Path(__file__).resolve().parent / IMAGE_NAME

    if not source.is_file():
        print(f"error: expected entry image at {source}, but it is missing",
              file=sys.stderr)
        return 1

    DESTINATION_DIR.mkdir(parents=True, exist_ok=True)
    target = DESTINATION_DIR / IMAGE_NAME
    shutil.copyfile(source, target)

    if not target.is_file():
        print(f"error: copy finished but {target} was not created",
              file=sys.stderr)
        return 1

    print(f"published {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(publish_image())
