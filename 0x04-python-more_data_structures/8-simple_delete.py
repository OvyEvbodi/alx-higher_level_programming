#!/usr/bin/python3

'''
simple_delete - deletes a key in a dictionary

ARGUMENTS:
@a_dictionary: the dictionary
@key: the key to delete from the dictionary

RETURN:
The updated dictionary.
'''


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        del a_dictionary[key]
    return a_dictionary
