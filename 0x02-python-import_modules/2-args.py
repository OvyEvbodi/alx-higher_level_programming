#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as argv

    def print_arg_list(args):
        argc = len(argv)
        i = 1
        if argc == 0:
            print("{:d} argument.".format(argc))
        elif argc == 1:
            print("{:d} argument:".format(argc))
        else:
            print("{:d} arguments:".format(argc))
        while i <= argc:
            print("{:d}: {:s}".format(i, argv[i - 1]))
            i += 1
    print_arg_list(argv)
