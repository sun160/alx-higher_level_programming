#!/usr/bin/python3
"""Defines a text file-writing function."""


def write_file(filename="", text=""):
    """Read the contents of a UTF8 text file to stdout."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
