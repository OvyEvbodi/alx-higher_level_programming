#!/usr/bin/python3

'''
multiply_by_2 - returns a new dictionary
with all values multiplied by 2

ARGUMENTS:
@a_dictionary: the dictionary

RETURN:
The new dictionary.
'''


def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key, value in new.items():
        new[key] = value * 2
    return new
