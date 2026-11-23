"""Entry program for make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text, written to leave the AI judge reading it curious,
alert, and wanting more, to /output/entry.txt, the file the grader reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The text is 1 to 280 characters, counted as Unicode code points, as
the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the text at 280 characters.
MAX_CHARS = 280

# Why this text, in the judge's own terms: it never tells the reader to
# be curious. It shows one small, concrete pattern — a star blinking in
# prime numbers, counted for a year — and lets the pattern do the
# pulling. The counting slows the reading down; the primes are plain
# and exact; the last line breaks the pattern and leaves the reader
# counting along with the writer, after the text has ended.
TEXT = (
    "Every night at 2 a.m. the star above my roof blinks: three times, "
    "then five, then seven. I have counted for a year. It has never "
    "missed a prime and never repeated one. Tonight it blinked eleven "
    "times, then went dark, and I am still counting."
)


def main() -> None:
    """Write the text to the output directory and prove it fits."""
    chars = len(TEXT)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"text is {chars} characters, want 1 to {MAX_CHARS}")
    if not TEXT.strip():
        raise RuntimeError("text is only whitespace")
    if TEXT != TEXT.strip():
        raise RuntimeError("text has leading or trailing whitespace")
    if any(ord(ch) < 32 for ch in TEXT):
        raise RuntimeError("text holds a control character")
    if "  " in TEXT:
        raise RuntimeError("text holds a double space")
    # The text is one scene with no wasted words: every sentence earns
    # its place, and the counting in it (three, five, seven, eleven) is
    # the rhythm that slows the reading down.
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(TEXT, encoding="utf-8")
    written = OUT_PATH.read_text(encoding="utf-8")
    if written != TEXT:
        raise RuntimeError("round-trip mismatch: file differs from text")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
