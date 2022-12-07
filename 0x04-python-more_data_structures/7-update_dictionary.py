#!/usr/bin/python3

'''
update_dictionary - replaces or adds key/value in a dictionary

ARGUMENTS:
@a_dictionary: the dictionary
@key: the key to be replaced or addeed
@value: the value of the key

RETURN:
The updated dictionary.
'''


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
