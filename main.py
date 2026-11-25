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
    """Write ENTRY as raw UTF-8 bytes, no trailing newline, then verify it.

    Reads the file back and checks the bytes and the 32-character gate, so a
    truncated or mistyped write fails loudly instead of submitting a bad entry.
    """
    os.makedirs(directory, exist_ok=True)
    target = os.path.join(directory, "entry.txt")
    with open(target, "wb") as handle:
        handle.write(ENTRY_BYTES)
    with open(target, "rb") as handle:
        written = handle.read()
    if written != ENTRY_BYTES:
        raise SystemExit("entry.txt does not match the entry")
    if len(written.decode("utf-8")) > 32:
        raise SystemExit("entry exceeds the 32-character limit")


def main():
    sys.stdout.write(ENTRY + "\n")
    output_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
