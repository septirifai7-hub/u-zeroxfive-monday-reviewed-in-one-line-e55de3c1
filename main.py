#!/usr/bin/env python3
"""Monday, Reviewed in One Line - make.fun bounty entry.

Writes the funniest one-line review of my own Monday, to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "Monday review: one star - the standup ran 47 minutes, the coffee machine quit at 9:03, and my inbox reproduced overnight."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
