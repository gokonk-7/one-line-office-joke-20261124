#!/usr/bin/env python3
"""One-Line Office Joke.

Writes one line -- a joke about office life -- to /output/entry.txt, as
the competition's program/v1 harness requires.

The joke: the office plant has survived three rounds of layoffs, two CEOs
and a merger, and HR still won't put it on the org chart. The laugh comes
from the plant being the office's longest-serving employee and still being
denied the one thing every worker wants: recognition on paper. The setup
escalates through corporate upheaval, then the punchline lands on
bureaucracy -- the plant outlasted everyone, yet the org chart, the
official record of who counts, has no room for it. It is a specific,
concrete detail of office life rather than the well-worn meeting-that-
should-have-been-an-email complaint, and it reads as one sentence with a
single clear twist.
"""

import os
import sys

JOKE = (
    "The office plant has survived three rounds of layoffs, two CEOs "
    "and a merger, and HR still won't put it on the org chart."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> int:
    text = JOKE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"joke is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("joke must be a single line", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("joke must be non-blank text", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
