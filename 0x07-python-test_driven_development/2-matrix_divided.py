#!/usr/bin/python3
"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix

    Args:
        matrixlist (list of list(ints or floats)): to be divied by num
        div (num or int): will be the divisor

    Returns:
        list of list: the result of the division

    Raises:
        TypeError: If matrix is not a list of list of integers or floats
        TypeError: If the rows of the matrix are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    size_err = "Each row of the matrix must have the same size"
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(err)
    len_row = len(matrix[0])
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(err)
        if len(row) != len_row:
            raise TypeError(size_err)
        for elem in row:
            if type(elem) not in (int, float) or elem is None:
                raise TypeError(err)
    if type(div) not in (int, float) or div is None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
