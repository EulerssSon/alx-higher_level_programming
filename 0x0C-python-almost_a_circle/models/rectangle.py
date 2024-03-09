#!/usr/bin/python3
"""This module is for the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This is the rectangle class that inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        """This is the constructor for the rectangle class

        Args:
            width (int): This is the width of the rectangle
            height (int): This is the height of the rectangle
            x (int, optional): This is of the rectangle. Defaults to 0.
            y (int, optional): This is tof the rectangle. Defaults to 0.
            id (int, optional): This is the id of. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is the getter for the width attribute

        Returns:
            int: This returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """This is the setter for the width attribute

        Args:
            value (int): This is the value to set the width to

        Raises:
            TypeError: This is raised if the value is not an integer
            ValueError: This is raised if the value is less than or equal to 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is the getter for the height attribute

        Returns:
            int: This returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """This is the setter for the height attribute

        Args:
            value (int): This is the value to set the height to

        Raises:
            TypeError: This is raised if the value is not an integer
            ValueError: This is raised if the value is less than or equal to 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """This is the getter for the x attribute

        Returns:
            int: This returns the x coordinate of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        """This is the setter for the x attribute

        Args:
            value (int): This is the value to set the x coordinate to

        Raises:
            TypeError: This is raised if the value is not an integer
            ValueError: This is raised if the value is less than 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is the getter for the y attribute

        Returns:
            int: This returns the y coordinate of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        """This is the setter for the y attribute

        Args:
            value (int): This is the value to set the y coordinate to

        Raises:
            TypeError: This is raised if the value is not an integer
            ValueError: This is raised if the value is less than 0

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self) -> int:
        """This method returns the area of the rectangle

        Returns:
            int: This returns the area of the rectangle
        """
        return self.width * self.height
