#!/usr/bin/python3

'''
print_sorted_dictionary - prints a dictionary by ordered keys

ARGUMENTS:
@a_dictionary: the dictionary

RETURN:
void
'''


def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")
