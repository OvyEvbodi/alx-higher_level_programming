#!/usr/bin/python3
if __name__ == "main":
    from sys import argv as argv

    def print_arg_list(args):
        argc = len(argv)
        i = 1
        if argc == 0:
            print(f"{argc} argument.")
        elif argc == 1:
            print(f"{argc} argument:")
        else:
            print(f"{argc} arguments:")
        while i < argc:
            print(f"{i}: {argc}")
            i += 1
    print_arg_list(argv)
