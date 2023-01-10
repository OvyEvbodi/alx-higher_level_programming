#!/usr/bin/python3

"""appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename: the file to be written to
        text: the string to write to filename

    Return:
        The number of characters
    """

    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
