#!/usr/bin/python3
# Finds a peak in a list of unsorted integers


def find_peak(list_of_integers):
    if not list_of_integers:
        return
    peak = list_of_integers[0] - 1
    changed = False
    for i in range(1, len(list_of_integers)):
        val = list_of_integers[i]
        if val >= peak:
            peak = val
            changed = True
        # else:
        #     break
    # return peak, changed
    return peak if changed else peak + 1
