#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    m = 0
    for k in range(x):
        try:
            print(my_list[k], end="")
            m += 1
        except IndexError:
            None
    print()
