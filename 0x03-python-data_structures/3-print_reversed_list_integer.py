#!/usr/bin/python3
def print_reserved_list_integer(my_list=[]):
    if len(my_list) >= 1:
        for i in my_list.reverse():
            print("{:d}".format(i))
