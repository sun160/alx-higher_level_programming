#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit_num = number % -10
elif number >= 0:
    last_digit_num = number % 10
if last_digit_num > 5:
    print(f"Last digit of {number} is {last_digit_num} and is greater than 5")
elif last_digit_num == 0:
    print(f"Last digit of {number} is {last_digit_num} and is 0")
else:
    print(f"Last digit of {number} is {last_digit_num} and is less than 6 and not 0")
