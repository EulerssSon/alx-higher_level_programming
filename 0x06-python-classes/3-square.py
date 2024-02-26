#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A square class"""
    def __init__(self, size=0) -> None:
        """Init method

        Args:
            size (int): Size of the square default to 0

        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        '''Caluates the area of the square

        Returns:
            int: Area =  sizeLeng ^2
        '''
        return self.__size ** 2
