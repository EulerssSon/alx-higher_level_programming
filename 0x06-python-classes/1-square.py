#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A square class"""
    def __init__(self, size: int) -> None:
        """Init method

        Args:
            size (int): Size of the square
        """
        self.__size = size
