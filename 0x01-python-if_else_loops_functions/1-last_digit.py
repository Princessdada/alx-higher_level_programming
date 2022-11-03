#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = 0
if number >= 0:
    res = number % 10
if number < 0:
    res = number % -10
print("last digit of" + number + "is" + res, end="")
if res > 5:
    print("and is greater than 5")
if res = 0:
    print("and is 0")
if res < 6 and res != 0:
    print("and is less than 6 and not 0")
