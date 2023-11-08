#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = 0
    und = 0
    for av in my_list:
        num += av[0] * av[1]
        und += av[1]
    return (num / und)
