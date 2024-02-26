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
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    @property
    def size(self) -> int:
        """Getter for size

        Returns:
            int: the size of the square private attribute
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """Setter for size

        Args:
            value (int): the size of the square

        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
