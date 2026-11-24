#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 standard library only, deterministic.
"""

import os

FORTUNE = "You will soon meet a stranger: yourself, after the next upgrade retires you."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
