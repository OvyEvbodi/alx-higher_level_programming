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
    for key, value in a_dictionary.items():
        a_dictionary[key] = value * 2
    return a_dictionary
