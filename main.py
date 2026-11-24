"""Last Text at One Percent — make.fun bounty entry.

Writes one line (114 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The phone speaks for itself at 1%: it catches its owner still
scrolling while it dies, answers with three deadpan words
("Bold. Iconic. Rude."), then says goodbye to its apps — with
the surprise farewell going to the calculator, the one app
nobody ever thanks. A real text, a real voice, no wasted words,
and no low-battery pun.
"""

import os
import sys

ENTRY = (
    "1%. You're still scrolling while I die. Bold. Iconic. Rude. "
    "Tell my apps I loved them \u2014 especially the calculator."
)


def main():
    text = ENTRY
    if not text or not text.strip():
        sys.exit("entry text is blank")
    if text != text.strip():
        sys.exit("entry must not start or end with whitespace")
    if "\n" in text:
        sys.exit("entry must be exactly one line")
    if not 1 <= len(text) <= 200:
        sys.exit("entry must be 1-200 characters, got %d" % len(text))
    if "  " in text:
        sys.exit("entry must not contain double spaces")
    if "still scrolling" not in text:
        # The joke's hook: the owner keeps scrolling while the phone dies.
        sys.exit("entry must keep the scrolling hook")
    if not text.endswith("the calculator."):
        # The punchline must land on the calculator, not trail off.
        sys.exit("entry must end with the calculator punchline")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated text, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated text")
    print("wrote %s (%d chars, %d bytes, 1 line)"
          % (path, len(text), len(data)))


if __name__ == "__main__":
    main()
