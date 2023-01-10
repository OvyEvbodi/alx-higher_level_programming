#!/usr/bin/python3

"""This module writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: the file to be written to
        text: the string to write to filename

    Return:
        The number of characters
    """

    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
