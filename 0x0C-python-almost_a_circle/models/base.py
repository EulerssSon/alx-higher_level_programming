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

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """Return list of json strings reps

        Args:
            json_string (str): formatted json str

        Returns:
            list: of fromtatedd json
        """
        if json_string is None or not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create obj from dict rep

        Args:
            kwargs dictary

        Returns:
            and obj rect or sq
        """
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(100, 100)
        else:
            dummy_obj = cls(101)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """load objects from file

        Returns:
            list: list of objects
        """
        file_name = f"{cls.__name__}.json"
        list_objs = []
        try:
            with open(file_name, mode="r") as file:
                list_dicts = cls.from_json_string(file.read())
                for dict in list_dicts:
                    list_objs.append(cls.create(**dict))
        except FileNotFoundError:
            pass
        return list_objs
