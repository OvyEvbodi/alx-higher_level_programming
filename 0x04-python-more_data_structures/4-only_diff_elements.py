#!/usr/bin/python3

'''
only_diff_elements -returns a set of all
elements present in only one set

ARGUMENTS:
@set_1: the first set
@set_2: the second set

RETURN:
A set of uncommon elements in set_1 and set_2.
'''


def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
