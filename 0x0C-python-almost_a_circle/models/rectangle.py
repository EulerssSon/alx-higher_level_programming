#!/usr/bin/python3
"""This module for rectangle inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): rect wid
            height (_type_): rect height
            x (int, optional): center x
            y (int, optional): center y
            id (_type_, optional): id of the shape
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        """return width"""
        return self.__width

    @width.setter
    def width(self, width: int):
        """_summary_

        Args:
            width (int): Width of rect
        """
        self.__width = width

    @property
    def height(self) -> int:
        """return height"""
        return self.__height

    @height.setter
    def height(self, height: int):
        """_summary_

        Args:
            height (int): Height of rect
        """
        self.__height = height

    @property
    def x(self) -> int:
        """return x"""
        return self.__x

    @x.setter
    def x(self, x: int):
        """_summary_

        Args:
            x (int): x center of rect
        """
        self.__x = x

    @property
    def y(self) -> int:
        """return y"""
        return self.__y

    @y.setter
    def y(self, y: int):
        """_summary_

        Args:
            y (int): y center of rect
        """
        self.__y = y
