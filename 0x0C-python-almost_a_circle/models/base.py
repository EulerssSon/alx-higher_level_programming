#!/usr/bin/python3
"""This module is for the base class"""


class Base:
    """This will be the base class for all other classes
    The goal of it is to manage id for all sub classed"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """This is the constructor for the base class

        Args:
            id (int, optional): This is the id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
