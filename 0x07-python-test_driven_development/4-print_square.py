#!/usr/bin/python3
"""This module prints a square with the character '#'"""


def print_square(size):
    """Prints a square with the character '#'

    Args:
        size (int): the size of the square

    Returns:
        None

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
