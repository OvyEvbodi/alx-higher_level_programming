#!/usr/bin/python3

'''
weight_average - returns the weighted average of all integers
tuple (<score>, <weight>)

ARGUMENTS:
@my_list: the list of tuples

RETURN: the resulting weighted average
'''


def weight_average(my_list=[]):
    avg, weight_total = 0, 0
    if my_list:
        for tup in my_list:
            score, weight = tup
            avg += score * weight
            weight_total += weight
    return avg / weight_total
