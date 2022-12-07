#!/usr/bin/python3

'''
best_score - returns a key with the biggest integer value

ARGUMENTS:
@a_dictionary: the dictionary

RETURN:
The key with the biggest integer value
'''


def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return
    for key, value in a_dictionary.items():
        if value > max:
            max = value
    for key, value in a_dictionary.items():
        if value == max:
            return key
