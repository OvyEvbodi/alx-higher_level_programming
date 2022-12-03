#!/usr/bin/python3

# replaces an element in a list

def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    for item in range(0, len(my_list)):
        if item == idx:
            my_list[item] = element
    return my_list
