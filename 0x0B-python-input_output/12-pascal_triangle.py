#!/usr/bin/python3

"""This module creates a Pascal's triangle of a height specified by the user
It contains 1 function ``pascal_triangle``
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n

    Args:
        n(int): the height(number of lists) of the triangle

    Return:
        a list of lists of integers
        representing the Pascal’s triangle of n
    """

    pascal_s_matrix = []
    row_list = [1]
    prev_list = []
    i, num_of_add, j, k = 2, 0, 0, 1

    if n == 1:
        pascal_s_matrix.append(row_list)
    if n > 1:
        pascal_s_matrix.append(row_list[:])
    while i <= n:
        num_of_add = i - 2
        j, k = 0, 1
        prev_list = row_list[:]
        row_list[:] = [1]
        while num_of_add:
            row_list.append(prev_list[j] + prev_list[k])
            j += 1
            k += 1
            num_of_add -= 1
        row_list.append(1)
        pascal_s_matrix.append(row_list[:])
        i += 1
    return pascal_s_matrix
