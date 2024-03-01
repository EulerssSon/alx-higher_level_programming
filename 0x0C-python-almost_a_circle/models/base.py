#!/usr/bin/python3
"""This the package. It contains the base class for the base class."""


class Base:
    """This is the base class for the base class."""
    __no_objects = 0

    def __init__(self, id=None):
        """construct object

        Args:
            id (int, optional): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json string of list of dictionaries

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: json string
        """
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
