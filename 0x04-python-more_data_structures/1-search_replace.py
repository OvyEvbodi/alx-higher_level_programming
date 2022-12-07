#!/usr/bin/python3

'''
search_replace - replaces all occurrences
of an element by another in a new list.

ARGUMENTS:
@my_list: the list from which elements are to be replaced
@search: the element to search for
@replace: the new element

RETURN:
The new list.
'''


def search_replace(my_list, search, replace):
    return [i if i != search else replace for i in my_list]
