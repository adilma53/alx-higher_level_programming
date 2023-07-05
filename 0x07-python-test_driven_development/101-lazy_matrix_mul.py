#!/usr/bin/python3
import numpy as np
"""
Lazy Matrix Multiplication
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiples two matrices
    """
    try:
        res = np.matmul(m_a, m_b)
    except:
        raise
    return res
