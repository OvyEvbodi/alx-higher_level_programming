#!/usr/bin/python3

#  removes all characters c and C from a string

def no_c(my_string):
    new_string = ""
    for character in my_string:
        if character == 'c' or character == 'C':
            continue
        else:
            new_string += character
    return new_string
