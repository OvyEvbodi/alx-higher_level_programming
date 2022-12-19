#!/usr/bin/python3

'''
safe_print_list - prints x elements of a list

ARGS:
my_list: the list whose elements are to be printed
x: the number of elements to print from my_list

Return:
The number of elements actually printed out,
if the list contains less than x elements
'''


def safe_print_list(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            num += 1
        except IndexError:
            break
    print()
    return num
