#!/usr/bin/python3
"""This module is for the base class"""
from json import dump, dumps, load, loads


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """method returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): This is a list of dictionaries

        Returns:
            str: returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ method writes the JSON string representation of list_objs to a file
        [{dict1}, {dict2}, {dict3}]

        Args:
            list_objs (list): This is a list of objects
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as file:
            if list_objs is None:
                file.write(Base.to_json_string([]))
            elif all(isinstance(obj, cls) for obj in list_objs):
                list_of_obj_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_of_obj_dicts))
