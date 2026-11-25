"""Entry for make.fun bounty "Make the AI Judge Laugh".

Writes one original joke about office life to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace,
with no trailing newline.
"""

import os
import sys

JOKE = (
    "My boss told me to treat the office like home, so now I ignore my "
    "emails, nap at my desk, and leave my mug in the sink."
)


def main() -> int:
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} is outside 1-200 characters", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
