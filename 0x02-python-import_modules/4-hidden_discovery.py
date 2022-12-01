#!/usr/bin/python3

# list all the names defined by a compiled module
import hidden_4


def list_names():
    names = dir(hidden_4)
    for name in names:
        if name != "__":
            print("{:s}".format(name))


if __name__ == "__main__":
    list_names()
