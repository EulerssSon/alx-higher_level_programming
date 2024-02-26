#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A square class"""
    def __init__(self, size=0, position=(0, 0)) -> None:
        """Init method

        Args:
            size (int): Size of the square default to 0
            position (tuple): Position of the square default to (0, 0)

        Raises:
            ValueError: If size is less than 0
            TypeError: If size is not an integer
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self) -> int:
        """Getter for size

        Returns:
            int: the size of the square private attribute
        """
        return self.__size

    @property
    def position(self) -> tuple:
        """Getter for position

        Returns:
            tuple: the position of the square private attribute
        """
        return self.__position

    @position.setter
    def position(self, value: tuple) -> None:
        """Setter for position

        Args:
            value (tuple): the position of the square

        Raises:
            ValueError: If position is not a tuple of 2 positive integers
            TypeError: If position is not a tuple
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def area(self) -> int:
        """Calculates the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

    def my_print(self) -> None:
        """Prints the square with the character '#'

        X number of lines are printed based on the position of the square
        Y number of spaces are printed based on the position of the square
        The square is printed with '#' characters if size is greater than 0
        else a new line is printed and nothing else

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
