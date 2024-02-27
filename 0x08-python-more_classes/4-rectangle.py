#!/usr/bin/python3
"""This module To Represent a Rectangle"""


class Rectangle:
    """Class Rectangle"""
    def __init__(self, width=0, height=0) -> None:
        """Constructor for rect with width and height

        Args:
            width (int, optional): Rect width. Defaults to 0.
            height (int, optional): Rect height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Getter for width

        Returns:
            int: Width of rect
        """
        return self.__width

    @property
    def height(self) -> int:
        """Getter for height

        Returns:
            int: Height of rect
        """
        return self.__height

    @width.setter
    def width(self, value: int) -> None:
        """Setter for width

        Args:
            value (int): Width of rect

        Raises:
            TypeError: If width is not an int
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value: int) -> None:
        """Setter for height

        Args:
            value (int): Height of rect

        Raises:
            TypeError: If height is not an int
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self) -> int:
        """Calculate area of rect

        Returns:
            int: Area of rect
        """
        return (self.width * self.height) if self.width and self.height else 0

    def perimeter(self) -> int:
        """Calculate perimeter of rect

        Returns:
            int: Perimeter of rect
        """
        per = 0
        if self.width and self.height:
            per = (self.width + self.height) * 2
        return per

    def __str__(self) -> str:
        """String representation of rect

        Returns:
            str: String representation of rect
        """
        rect_str = ""
        if self.width and self.height:
            for _ in range(self.height):
                if _ == self.height - 1:
                    rect_str += "#" * self.width
                else:
                    rect_str += "#" * self.width + "\n"
        return rect_str

    def __repr__(self) -> str:
        """String representation of rect

        Returns:
            str: String representation of rect
        """
        return f'Rectangle({self.width}, {self.height})'
