#!/usr/bin/python3
import random
number = random.randit(-10, 10)
if number >= 0:
    if number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is zero")
else:
    print(f"{number} is negative")
