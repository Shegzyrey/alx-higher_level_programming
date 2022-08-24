#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number >= 0:
    if number > 0:
        print(f"{} is positive".format(number))
    else:
        print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
