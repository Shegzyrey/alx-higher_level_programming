#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = 1
    sum_arg = 0
    while n < len(argv):
        sum_arg += int(argv[n])
        n += 1
    print("{}".format(sum_arg))
