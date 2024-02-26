#!/usr/bin/python3
"""Module for A Magic  class"""


import math


class MagicClass:
    """A class representing a magic circle class."""
    def __init__(self, radius=0) -> None:
        """Initinze the object

        Args:
            radius (int, optional): The radius of the magic circle def 0
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
