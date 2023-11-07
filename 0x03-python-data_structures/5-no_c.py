#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for m in my_string:
        if (my_string[m] != 'c' and  my_string[m] != 'C'):
            new += m
    return (new)
