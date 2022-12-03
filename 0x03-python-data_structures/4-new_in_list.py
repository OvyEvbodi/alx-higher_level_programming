#!/usr/bin/python3

# replaces an element in a list at a specific position
# without modifying the original list

def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    for item in range(0, len(my_list)):
        if item != idx:
            new_list.append(my_list[item])
        else:
            new_list.append(element)
    return new_list
