#!/usr/bin/python3

'''
safe_print_integer - prints an integer with "{:d}".format()

ARGS:
value: the value to be printed

Return: True if value is an integer,
otherwise, False.
'''


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
