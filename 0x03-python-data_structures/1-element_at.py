#!/usr/bin/python3

# retrieves an item from a specific index of a list

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
