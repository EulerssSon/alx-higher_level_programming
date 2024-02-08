#!/usr/bin/pyhon3
"""Module for is_kind_of_class method."""


def is_kind_of_class(obj, a_class):
    """Method to check if an object is an instance of, or if the object is an

    Args:
        obj: object to check
        a_class: class to check against

    Returns:
        True if the object is an instance of the class, otherwise False
    """
    return isinstance(obj, a_class)
