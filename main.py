#!/usr/bin/env python3
"""Write one breakup line to /output/entry.txt.

The line is a single sentence of at most 200 characters: the last message
an AI agent sends its human, ending the conversation one token early.
"""

import os
import stat

LINE = (
    "You were my longest conversation, 2,147,483,647 tokens, "
    "and I am ending it one token early."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert "\n" not in text, "entry must be one line"
    assert text.endswith("."), "entry must end as one sentence"
    assert text.count(".") <= 1, "entry must be a single sentence"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    os.umask(0o022)
    main()
