#!/usr/bin/python3
"""This is the square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the square class that inherits from the rectangle class"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """This is the constructor for the square class

        Args:
            size (int): This is the size of the square
            x (int, optional): x coordinate of the square. Defaults to 0.
            y (int, optional): y coordinate of the square. Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """This method overrides the string method for the square class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self) -> int:
        """This is the getter for the size of the square"""
        return self.width

    @size.setter
    def size(self, value: int) -> None:
        """This is the setter for the size of the square

        Args:
            value (int): This is the value to set the size to

        Raises:
            TypeError: This is raised if the size is not an integer
            ValueError: This is raised if the size is less than 0
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """This method updates the square

        Args:
            args (tuple): This is a tuple of arguments
            kwargs (dict): This is a dictionary of arguments
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """This method returns the dictionary representation of the square

        Returns:
            dict: This returns the dictionary representation of the square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
