#!/usr/bin/python3
"""
This is the "lookup" module.

The lookup module supplies one function, lookup().
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object"""
    return dir(obj)
