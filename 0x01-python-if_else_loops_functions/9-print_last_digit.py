#!/usr/bin/python3
def print_last_digit(n):
    i = abs(n) % 10
    print("{:d}".format(i), end="")
    return (i)
