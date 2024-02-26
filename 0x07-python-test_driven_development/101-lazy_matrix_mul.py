#!/usr/bin/python3
"""This module is to multiply two matrices together using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies two matrices together
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        the product of the two matrices
    Raises:
        TypeError: if the matrices are not of the correct type
        ValueError: if the matrices are not the correct size
    """
    return np.matmul(m_a, m_b)
