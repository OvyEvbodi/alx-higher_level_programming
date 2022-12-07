#!/usr/bin/python3

'''
uniq_add - adds all unique integers in a
list (only once for each integer)

ARGUMENTS:
@my_list: the list to perform the arithmetic operation on.

RETURN:
The result of the addition of all the elements in my_list.
'''


def uniq_add(my_list=[]):
    new = set(my_list)
    sum = 0
    for i in new:
        sum += i
    return sum
