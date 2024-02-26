#!/usr/bin/python3


def add_integer(a, b=98) -> int:
    """Funciton to add 2 ints

    Args:
        a (int: float): fisrt number
        b (int, optional): second operand. Defaults to 98.

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: If a or b is not an integer
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
