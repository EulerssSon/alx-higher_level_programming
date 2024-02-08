#!/usr/bin/python3
"""Defines a class and a checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a class

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj against

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False
    """
    return type(obj) is a_class
