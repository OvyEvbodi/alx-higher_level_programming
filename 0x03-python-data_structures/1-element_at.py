#!/usr/bin/python3

# retrieve an item from a specific index of a list

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    for i in range(0, len(my_list)):
        if i == idx:
            return my_list[i]