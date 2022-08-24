#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
last_digit = (number % 10)

if last_digit is 0:
    conditionalStr = "0"
elif last_digit > 5:
    conditionalStr = "greater thn 5"
else:
    conditionalStr = "less than 6 and not 0"

print("Last digit of {} is {} and is {}" .format(number, last_digit, conditionalStr))
