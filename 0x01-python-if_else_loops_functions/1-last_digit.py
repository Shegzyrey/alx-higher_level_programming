#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)
l_digit = (number % 10)

if l_digit == 0:
    varStr = "0"
elif l_digit > 5:
    varStr = "greater thn 5"
else:
    varStr = "less than 6 and not 0"

print("Last digit of {} is {} and is {}" .format(number, l_digit, varStr))
