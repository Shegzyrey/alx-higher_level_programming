#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx <= (len(my_list) - 1) and idx >= 0:
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
    return (my_list)
