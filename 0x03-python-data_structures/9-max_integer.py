#!/usr/bin/python3

# finds the biggest integer of a list

def max_integer(my_list=[]):
    max_num = 0
    if not len(my_list):
        return
    for item in my_list:
        if item > max_num:
            max_num = item
    return max_num
