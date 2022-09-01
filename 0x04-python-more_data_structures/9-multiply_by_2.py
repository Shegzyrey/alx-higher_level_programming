#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n_dictionary = a_dictionary.copy()
    for i in n_dictionary:
        n_dictionary[i] = n_dictionary[i] * 2
    return (n_dictionary)
