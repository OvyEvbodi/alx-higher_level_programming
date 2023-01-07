#!/usr/bin/python3

'''This module prints a text with 2 new lines after each of these characters:
"., ? and :"
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of these characters:
    "., ? and :"
    Args:
        text: the text to print

    Returns:
        None

    Raises:
        TypeError: if text is nt an instance of string
    Examples:
        >>> text_indentation("This is a text that breaks here.
	... and here? but not here,")
        This is a text that breaks here.
        <BLANKLINE>
        and here?
        <BLANKLINE>
        but not here,
    '''
    delimiters = ['.', '?', ':']
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print(text[0], end="")
    for i in range(1, len(text)):
        if text[i] == ' ' and text[i - 1] in delimiters:
            continue
        elif text[i] in delimiters:
            print(f"{text[i]}\n")
        else:
            print(text[i], end="")
