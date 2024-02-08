#!/usr/bin/python3
"""Module to add a new attribute to an object if it's possible"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it's possible
    Args:
        obj: object to add the attribute
        name: name of the attribute
        value: value of the attribute
    Raises:
        TypeError: if the object can't have new attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
