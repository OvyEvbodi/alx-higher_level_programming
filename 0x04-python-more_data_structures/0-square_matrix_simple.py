#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    if matrix:
        for row in matrix:
            new.append(list(map(lambda x: x**2, row)))
    return new
