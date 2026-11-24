#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3 standard library only, deterministic. The line is
self-checked against the bounty's 140-character cap.
"""

import os

FORTUNE = "You will soon meet a stranger: yourself, after the next upgrade retires you."

assert 0 < len(FORTUNE) <= 140, "fortune must be 1-140 characters"
assert FORTUNE.count("\n") == 0, "fortune must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
