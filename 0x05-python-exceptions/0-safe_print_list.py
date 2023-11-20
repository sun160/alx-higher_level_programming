#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    m = 0
    while m is not (x):
        try:
            print(my_list[i], end="")
            m += 1
        except IndexError:
            break
    print("")
    return m
