#!/usr/bin/python3


def print_arg_list(args):
    argc = len(argv)
    i = 1
    if argc == 1:
        print("{:d} argument.".format(argc))
    elif argc == 2:
        print("{:d} argument:".format(argc))
    else:
        print("{:d} arguments:".format(argc))
    while i <= argc:
        print("{:d}: {:s}".format(i, argv[i - 1]))
        i += 1

if __name__ == "__main__":
    from sys import argv as argv
    print_arg_list(argv)
