#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digits = abs(number) % 10
if number < 0:
    l_digits = -l_digits
    print("Last digit of {} is {} and is ".format(number,l_digits), end="")
if l_digits > 5:
    print("greater than 5")
elif l_digits == 0:
    print("0")
else:
    print("less than 6 and not 0")
