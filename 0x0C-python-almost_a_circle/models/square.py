#!/usr/bin/python3
"""This module is for the square one inherts from rect"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """sq Class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Construct object


        Args:
            size (int): size of square
            x (int, optional): x center
            y (int, optional): y center
            id (int, optional): id of the object
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self) -> int:
        """return size"""
        return self.width

    @size.setter
    def size(self, size: int):
        """set size


        Args:
            size (int): size of square
        """
        self.width = size
        self.height = size

    def __str__(self) -> str:
        """return string representation"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        return f"[Square] ({i}) {x}/{y} - {w}"

    def update(self, *args, **kwargs):
        """update object

        Args:
            *args (tuple): tuple of arguments
            **kwargs (dict): dictionary of arguments
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                # a note doneot use dict is subclasses
                setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """return dictionary representation of square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
