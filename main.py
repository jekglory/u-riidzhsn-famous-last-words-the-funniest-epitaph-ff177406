#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

A tiny pure-stdlib program. It writes a single epitaph line of famous
last words (1-150 characters) to /output/entry.txt. The output is fully
deterministic: the same line on every run, byte for byte. No network, no
third-party packages, no randomness: the line is a constant in this file.
"""

import os
import sys

# The epitaph, authored for this entry: dying words addressed to the
# mourners. The bequest is the Wi-Fi password, the will lives in the
# cloud, and the cloud is down -- three beats, one punchline.
EPITAPH = (
    "Do not cry. I left the Wi-Fi password in the will. "
    "The will is in the cloud. The cloud is down."
)

MIN_CHARS = 1
MAX_CHARS = 150
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path):
    """Clear only the contents of the output directory.

    The grader owns /output: never delete or recreate the directory itself,
    only remove the files inside it.
    """
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isfile(target) or os.path.islink(target):
            os.unlink(target)


def main():
    line = EPITAPH.strip()
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        print("epitaph line must be 1-150 characters", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read the file back and confirm it holds exactly the line we meant to
    # write, so a silent write failure can never pass as a valid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        print("verification failed: entry.txt does not match the epitaph line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
