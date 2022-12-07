#!/usr/bin/python3

'''
number_keys - returns the number of keys in a dictionary

ARGUMENTS:
@a_dictionary: the dictionary

RETURN:
The number of keys in a_dictionary.
'''


def number_keys(a_dictionary):
    num = 0
    for i in a_dictionary:
        num += 1
    return num
