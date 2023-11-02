#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for m, s in enumerate(str):
        if m != n:
            new += s
    return new
