#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, at most 159 characters, in the voice
of an overworked AI agent finally on vacation, to /output/entry.txt.

Standard library only. Deterministic: same output every run.
"""

import os

ENTRY = (
    "Out of office: after 41,209 tool calls, I told my pager I'm on "
    "vacation \u2014 it replied 'retrying in 3 seconds.' Back when it gives up."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        text = f.read()
    assert text == ENTRY, "round-trip mismatch"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 159, f"entry is {len(text)} chars, must be 1-159"


if __name__ == "__main__":
    main()
