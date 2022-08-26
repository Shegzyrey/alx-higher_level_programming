#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 2:
        var_arg = "argument"
    else:
        var_arg = "arguments"
    if length > 1:
        print("{} {}:".format(length-1, var_arg))
        n = 1
        while n < length:
            print("{}: {}".format(n, argv[n]))
            n += 1
    else:
        print("0 {}.".format(var_arg))
