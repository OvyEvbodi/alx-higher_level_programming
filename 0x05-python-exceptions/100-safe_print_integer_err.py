#!/usr/bin/python3

'''
safe_print_integer - prints an integer with "{:d}".format(),
with an exception message

ARGS:
value: the value to be printed

Return: True if value is an integer,
otherwise, False.
'''


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: ", end="")
        print("{}".format(ve))
        return False
    return True
