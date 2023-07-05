#!/usr/bin/python3

"""
Matrix Division

this script divides all elements of a matrix by a given number.

"""


def matrix_divided(matrix, div):
    """
    Divides a matrix by a number.
    """

    matrix_error = 'matrix must be a matrix (list of lists) of integers/floats'
    size_error = 'Each row of the matrix must have the same size'

    if not isinstance(matrix, list) or
    any(not isinstance(row, list) for row in matrix):

        raise TypeError(matrix_error)

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError(size_error)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in row] for row in matrix]
