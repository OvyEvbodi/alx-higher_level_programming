#!/usr/bin/python3

# adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2, b1, b2 = 0, 0, 0, 0
    try:
        if tuple_a[0]:
            a1 = tuple_a[0]
    except IndexError:
        a1 = 0
    try:
        if tuple_b[0]:
            b1 = tuple_b[0]
    except IndexError:
        b1 = 0
    try:
        if tuple_a[1]:
            a2 = tuple_a[1]
    except IndexError:
        a2 = 0
    try:
        if tuple_b[1]:
            b2 = tuple_b[1]
    except IndexError:
        b2 = 0

    t1 = a1 + b1
    t2 = a2 + b2
    t = t = (t1, t2)
    return t
