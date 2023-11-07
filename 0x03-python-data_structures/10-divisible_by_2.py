#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            mul[count] = True
        else:
            mul[count] = False
    return(mul)
