#!/usr/bin/python3
"""
Matrix Multiplication
"""


def matrix_multiply(matrix_a, matrix_b):
    """Multiplies two matrices
    """
    error_msg1 = " must be a list"
    error_msg2 = " must be a list of lists"
    error_msg3 = " should contain only integers or floats"
    error_msg4a = "each row of "
    error_msg4b = " must be of the same size"
    error_msg5 = " can't be empty"
    error_msg6 = "matrix_a and matrix_b can't be multiplied"

    if type(matrix_a) is not list:
        raise TypeError("matrix_a" + error_msg1)
    if type(matrix_b) is not list:
        raise TypeError("matrix_b" + error_msg1)
    if not any(isinstance(row, list) for row in matrix_a):
        raise TypeError("matrix_a" + error_msg2)
    if not any(isinstance(row, list) for row in matrix_b):
        raise TypeError("matrix_b" + error_msg2)
    for row in matrix_a:
        if len(row) == 0:
            raise ValueError("matrix_a" + error_msg5)
    for row in matrix_b:
        if len(row) == 0:
            raise ValueError("matrix_b" + error_msg5)
    for row in matrix_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix_a" + error_msg3)
    for row in matrix_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix_b" + error_msg3)
    if len(set(len(row) for row in matrix_a)) != 1:
        raise TypeError(error_msg4a + "matrix_a" + error_msg4b)
    if len(set(len(row) for row in matrix_b)) != 1:
        raise TypeError(error_msg4a + "matrix_b" + error_msg4b)
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError(error_msg6)

    new_matrix = []
    for row in matrix_a:
        new_row = []
        for c in range(len(matrix_b[0])):
            new_row.append(
                sum(a * b for a, b in zip(row, list(r[c] for r in matrix_b))))
        new_matrix.append(new_row)
    return new_matrix
