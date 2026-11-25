#!/usr/bin/env python3
"""Write the funniest famous last words epitaph to /output/entry.txt.

The line is built from its two beats so the joke's construction is explicit:

  * the setup  - "I see the light", the canonical dying-words image, and
  * the twist  - "it's the fridge", which reframes that light as the
    fridge light: the afterlife turns out to be the kitchen.

The assembled line is then checked against the competition gate before it
is written: UTF-8 text, 1 to 150 characters, not only whitespace, a single
line, no stage directions, no explanation. Deterministic, stdlib only.
"""
import os

SETUP = "I see the light"          # the dying-words image
TWIST = "it's the fridge"          # the surprise: the light is the fridge
DASH = "\u2014"                     # em dash, one breath of dying speech

MAX_CHARS = 150


def build_entry() -> str:
    """Assemble the epitaph from its setup and its twist."""
    return f"{SETUP} {DASH} {TWIST}."


def validate(entry: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not isinstance(entry, str):
        raise ValueError("entry must be text")
    if not (1 <= len(entry) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    entry.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    entry = build_entry()
    validate(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
