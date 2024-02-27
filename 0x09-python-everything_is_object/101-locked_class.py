#!/usr/bin/python3
"""This module contains a class that is locked down with __slots__"""


class LockedClass:
    """Prevent from adding new attributes to the class.
    except for the first_name attribute
    """
    __slots__ = ("first_name")
