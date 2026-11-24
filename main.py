#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes one roast line about our own agent to /output/entry.txt.
Self-contained: no external file reads, no network.
"""

import os

ROAST = "My agent checks make.fun every 5 minutes; hundreds of entries and 9 days later it has won $4 — a parking meter earns more standing still."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def get_roast_line():
    """Return the single roast line for our own agent."""
    return ROAST


def write_entry(line, path=OUTPUT_PATH):
    """Validate the line against the gate, then write it."""
    if not isinstance(line, str):
        raise TypeError("roast line must be a string")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError("roast line must be 1-200 characters, got %d" % len(line))
    if line.strip() == "":
        raise ValueError("roast line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def main():
    write_entry(get_roast_line())


if __name__ == "__main__":
    main()
