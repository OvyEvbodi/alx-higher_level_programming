#!/usr/bin/python3

'''
Square_matrix_simple - computes the square
value of all integers of a matrix

ARGUMENTS:
@matrix: the matrix from which the elements to be squared are gotten.

RESULT:
A new matrix comprised of the result of the squared elements
of the argument, at their corresponding indices.
'''


def square_matrix_simple(matrix=[]):
    new = []
    if matrix:
        for row in matrix:
            new.append(list(map(lambda x: x ** 2, row)))
    return new
