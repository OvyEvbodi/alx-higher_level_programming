#!/usr/bin/python3
'''
safe_function - executes a function safely

ARGS:
fct: the function
args: its argument(s)

Return: On success, the return value of fct,
otherwise, None
'''


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err))
        return
