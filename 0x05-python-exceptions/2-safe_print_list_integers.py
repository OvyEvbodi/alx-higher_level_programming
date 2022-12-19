#!/usr/bin/python3

'''
safe_print_list_integers - prints the first x elements
of a list and only integers

ARGS:
my_list: the list whose elements are to be printed
x: the number of elements to print from my_list

Return:
The number of elements actually printed out,
if the list contains less than x elements
'''


def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print()
    return num
