#!/usr/bin/python3

'''
safe_print_division - divides 2 integers and prints the result

ARGS:
a: the dividend
b: the divisor

Return:
The quotient, otherwise, None.
'''


def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
