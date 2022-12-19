#!/usr/bin/python3
import sys


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
    except Exception as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False
    return True
