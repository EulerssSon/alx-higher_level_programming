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

    @classmethod
    def save_to_file(cls, list_objs):
        """save list of objects to file

        Args:
            list_objs (list): list of objects
        """
        file_name = f"{cls.__name__}.json"
        list_dicts = []
        with open(file_name, mode="w") as file:
            if list_objs is not None:
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
            file_str = cls.to_json_string(list_dicts)
            file.write(file_str)
