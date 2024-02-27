#!/usr/bin/python3
"""This module To Represent a Rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        """Constructor for rect with width and height

        Args:
            width (int, optional): Rect width. Defaults to 0.
            height (int, optional): Rect height. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __del__(self) -> None:
        """Destructor for rect"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2) -> "Rectangle":
        """function to compare two rectangles

        Args:
            rect_1 (Rectangle): First rect
            rect_2 (Rectangle): Second rect

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle

        Returns:
            Rectangle: The bigger rect or the first rect if they are equal
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """Make a square form a rectangle using same length and width

        Args:
            size (int, optional = 0): size of the new square. Defaults to 0.
        """

        return cls(size, size)
