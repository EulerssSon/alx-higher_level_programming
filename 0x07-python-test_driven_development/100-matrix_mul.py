#!/usr/bin/python3
"""This module multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): the first matrix
        m_b (list): the second matrix

    Returns:
        list: the product of the two matrices

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        ValueError: If m_a or m_b is empty
        TypeError: If m_a or m_b is not a rectangle
        ValueError: If m_a or m_b can't be multiplied
    """
    if type(m_a) is not list or m_a is None:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list or m_b is None:
        raise TypeError('m_b must be a list')
    if not all(type(row) is list for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(type(row) is list for row in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0:
        raise ValueError('m_a can\'t be empty')
    for row in m_a:
        if len(row) == 0:
            raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0:
        raise ValueError('m_b can\'t be empty')
    for row in m_b:
        if len(row) == 0:
            raise ValueError('m_b can\'t be empty')

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
