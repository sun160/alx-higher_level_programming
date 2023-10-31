#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_number = number % 10 if number > 10 else number % -10
if number > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_digit_number), end="")
if number == 0:
    print("Last digit of {} is {} and is 0".format(number, last_digit_number), end="")
if number < 6:
    print("Last digit of {} is {} and is is less than 6 and not 0".format(number, last_digit_number), end="")
