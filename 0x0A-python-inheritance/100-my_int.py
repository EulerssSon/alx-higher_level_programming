#!/usr/bin/python3
"""Module for MyInt class."""


class MyInt(int):
    """Class MyInt."""
    def __eq__(self, other):
        """Override equality operator."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Override inequality operator."""
        return int(self) == int(other)
