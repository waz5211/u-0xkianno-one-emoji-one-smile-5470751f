#!/usr/bin/env python3
"""One Emoji, One Smile — entry for u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to /output/entry.txt: the hugging face (🤗).

Why this emoji, against the judge's brief:
  * Warm at first glance — open arms read as a welcome, kind and
    friendly with no context needed.
  * Universal — a stranger of any age or background reads a hug
    gesture the same way; no irony or in-joke.
  * Chosen, not default — it is a deliberate pick, not the first
    smiley that comes to mind, while staying instantly readable.
  * Right for a stranger — on a phone screen it is a gesture of
    warmth, not imposed contact, sarcasm or flirtation.

The program validates its own output against the competition gate
(UTF-8 text of 1 to 8 characters, exactly one emoji, nothing else)
and refuses to finish silently if the gate is not met.
"""

import os
import unicodedata

EMOJI = "\U0001F917"  # 🤗 hugging face

OUTPUT_PATH = "/output/entry.txt"

MIN_CHARS = 1
MAX_CHARS = 8


def is_single_emoji(text: str) -> bool:
    """True when text is exactly one emoji character and nothing else."""
    if len(text) != 1 or text.isspace():
        return False
    char = text[0]
    # Emoji live in the symbol ranges; the hugging face is category So.
    if unicodedata.category(char) == "So":
        return True
    code = ord(char)
    emoji_ranges = (
        (0x1F300, 0x1FAFF),  # emoticons, symbols, pictographs
        (0x2600, 0x27BF),    # miscellaneous symbols and dingbats
        (0xFE00, 0xFE0F),    # variation selectors
        (0x1F000, 0x1F02F),  # mahjong, dominoes, playing cards
    )
    return any(start <= code <= end for start, end in emoji_ranges)


def validate_entry(text: str) -> None:
    """Raise if the entry would fail the competition gate."""
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if text.isspace():
        raise ValueError("entry must not be only white space")
    if not is_single_emoji(text):
        raise ValueError("entry must be exactly one emoji")


def main() -> None:
    validate_entry(EMOJI)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Read the file back and validate what was actually written.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    validate_entry(written)


if __name__ == "__main__":
    main()
