#!/usr/bin/python3
"""Say My Name Module"""


def say_my_name(first_name, last_name=""):
    """print My name is <first_name> <last_name>

    Args:
        first_name (str): firstName
        last_name (str, optional): SecondName. Defaults to "".

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
