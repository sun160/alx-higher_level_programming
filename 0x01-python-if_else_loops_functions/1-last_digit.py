#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_number = abs(number) % 10
if number > 5:
    print(f"Last digit of {number} is {last_digit_number} and is greater than 5")
if number == 0:
    print(f"Last digit of {number} is {last_digit_number} and is 0")
if number < 6:
     print(f"Last digit of {number} is {last_digit_number} and is less than 6 and not 0")
