#!/usr/bin/python3

'''This module divides all elements of a matrix.
It contains 1 function ``matrix_divided``
'''


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix
    Args:
        matrix: the matrix whose elements are the dividends
        div: the divisor

    Returns:
        A new matrix comprised of the corresponding quotients

    Raises:
        TypeError: if matrix is not a list instance;
        if matrix is not comprised of list instance vectors,
            made up fo ints or floats;
        if div is neither an instance of int nor float

        ZeroDivisionError: if div is equal to 0

    Examples:
        >>> matrix_divided([[6,7], [89, 8]], 3)
        [[2.0, 2.33], [29.67, 2.67]]
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    '''

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(len(matrix[i]) == len(matrix[0]) for i in range(len(matrix))):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round((i / div), 2) for i in row]for row in matrix]
    return new_matrix
