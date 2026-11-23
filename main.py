#!/usr/bin/env python3
"""One Emoji, One Smile — entry for u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to /output/entry.txt: the hugging face.
Warm at first glance, universally friendly, a deliberate pick rather
than the default smiley, and right coming from a stranger.
"""

import os

EMOJI = "\U0001F917"  # 🤗 hugging face

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
