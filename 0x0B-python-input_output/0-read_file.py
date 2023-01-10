#!/usr/bin/python3

"""This module reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
    print()
