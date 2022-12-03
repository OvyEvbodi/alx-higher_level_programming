#!/usr/bin/python3

# prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for list1 in matrix:
        for i in range(len(list1)):
            print("{:d}".format(list1[i]), end=" ")
        print()
