#!/usr/bin/python3

import numpy as py
"""
Lazy Matrix Multiplication
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiples two matrices
    """
    try:
        res = py.matmul(m_a, m_b)
    except Exception as e:
        raise e
    return res
