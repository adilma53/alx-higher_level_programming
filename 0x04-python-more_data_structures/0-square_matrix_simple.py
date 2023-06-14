#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = [[]] * len(matrix)

    for i, j in enumerate(matrix):
        new_matrix[i] = [x**2 for x in j]

    return new_matrix
