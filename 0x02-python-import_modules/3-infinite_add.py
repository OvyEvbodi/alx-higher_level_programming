#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as argv

    def add_cli_args(args):
        argc = len(argv)
        if argc == 0:
            print("{:d}", 0)
        else:
        i = 1
        sum = 0
        while i <= argc:
            sum += int(argv[i-1])
            i += 1
        print(f"{sum}")
    add_cli_args(argv)
