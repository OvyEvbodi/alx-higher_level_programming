#!/usr/bin/python3

# returns a tuple with the length of a string
# and its first character

def multiple_returns(sentence):
    first = ""
    if not len(sentence):
        first = None
    else:
        first = sentence[0]
    return len(sentence), first
