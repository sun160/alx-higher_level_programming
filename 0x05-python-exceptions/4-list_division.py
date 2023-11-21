#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for m in range(0, list_length):
        try:
            divide = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            new_list.append(divide)
    return (new_list)
