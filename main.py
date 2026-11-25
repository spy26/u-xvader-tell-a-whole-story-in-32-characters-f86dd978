"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes the single Wi-Fi network name "We Have Your WiFi. Send Pizza."
(30 characters) to /output/entry.txt as raw UTF-8, no trailing newline.

The entry is fully self-contained: a constant string in this file. It reads no
secret, no network, no git history, and no file outside this repository.
"""

import os
import sys

ENTRY = "We Have Your WiFi. Send Pizza."
ENTRY_BYTES = ENTRY.encode("utf-8")

assert len(ENTRY) <= 32, "entry must be at most 32 characters"


def write_entry(directory):
    """Write ENTRY as raw UTF-8 bytes, no trailing newline."""
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(ENTRY_BYTES)


def main():
    sys.stdout.write(ENTRY + "\n")
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
