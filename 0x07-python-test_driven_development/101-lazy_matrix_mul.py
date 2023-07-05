#!/usr/bin/python3

"""
Lazy Matrix Multiplication
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices
    """
    try:
        result = np.matmul(m_a, m_b)
    except Exception as e:
        raise e
    return result
