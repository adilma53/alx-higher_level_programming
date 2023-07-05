#!/usr/bin/python3
"""
 Matrix Multiplication

"""


def matrix_mul(m_a, m_b):
    """
    Multiples two matrices
    """
    test1 = " must be a list"
    test2 = " must be a list of lists"
    test3 = " should contain only integers or floats"
    test4 = "each row of "
    test4A = " must should be of the same size"
    V = " can't be empty"
    V2 = "m_a and m_b can't be multiplied"
    if type(m_a) is not list:
        raise TypeError("m_a" + test1)
    if type(m_b) is not list:
        raise TypeError("m_b" + test1)
    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a" + test2)
    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b" + test2)
    for l in m_a:
        if len(l) == 0:
            raise ValueError("m_a" + V)
    for l in m_b:
        if len(l) == 0:
            raise ValueError("m_b" + V)
    for row in m_a:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError("m_a" + test3)
    for row in m_b:
        for e in row:
            if not isinstance(e, (int, float)):
                raise TypeError("m_b" + test3)
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError(test4 + "m_a" + test4A)
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError(test4 + "m_b" + test4A)
    if len(m_a[0]) != len(m_b):
        raise ValueError(V2)
    new = []
    for ar in m_a:
        nr = []
        for c in range(len(m_b[0])):
            nr.append(sum(a * b for a, b in zip(ar, list(r[c] for r in m_b))))
        new.append(nr)
    return new
