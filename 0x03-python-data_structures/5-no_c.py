#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for m in my_string:
        if (m != 'c') and (m != 'C'):
            new += m
    return (new)
