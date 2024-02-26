#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A square class"""
    def __init__(self, size=0) -> None:
        """Init method

        Args:
            size (int): Size of the square default to 0
        """
        self.size = size

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
            TypeError: If size is not an integer or not a float
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        self.__size = value

    def area(self) -> int:
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def __eq__(self, __value: object) -> bool:
        """Equal comparison magic method for Square class to
        compare two objects with the size

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the two objects are equal
        """
        if self.__size == __value.size:
            return True

    def __ne__(self, __value: object) -> bool:
        """Not equal comparison magic method for Square class to

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the two objects are not equal
        """
        return not (self == __value)

    def __le__(self, __value: object) -> bool:
        """Less than or equal comparison magic method for Square class to

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the object is less than or equal to the value
        """
        if self.__size <= __value.size:
            return True

    def __lt__(self, __value: object) -> bool:
        """Less than comparison magic method for Square class to

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the object is less than the value
        """
        return self <= __value and self != __value

    def __ge__(self, __value: object) -> bool:
        """Greater than or equal comparison magic method for Square class to

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the object is greater than or equal to the value
        """

        if self.__size >= __value.size:
            return True

    def __gt__(self, __value: object) -> bool:
        """Greater than comparison magic method for Square class to

        Args:
            __value (object): the value to compare with

        Returns:
            bool: if the object is greater than the value
        """
        return self >= __value and self != __value
