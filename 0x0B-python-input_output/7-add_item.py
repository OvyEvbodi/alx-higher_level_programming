#!/usr/bin/python3

"""This script adds all arguments to a Python list,
and then saves them to a file"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
from sys import argv
import json


def add_args():
    from sys import argv
    my_list = []
    argc, i = len(argv), 1
    while i < argc:
        my_list.append(argv[i])
        i += 1


if __name__ == "__main__":
    add_args()
