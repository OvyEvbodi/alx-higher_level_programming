#!/usr/bin/python3
from sys import argv


def print_arg_list():
    argc = len(argv)
    i = 1
    if argc == 1:
        print("{:d} argument.".format(argc))
    elif argc == 2:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    while i <= argc:
        print("{:d}: {:s}".format(i, argv[i]))
        i += 1


if __name__ == "__main__":
    print_arg_list()
