#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.
            or list of strings contains the desired attributes

        Returns:
            dict: of the instance to convert to JSON format
        """
        if type(attrs) is list and all(type(_) is str for _ in attrs):
            my_dict = {}
            for _ in attrs:
                if _ in self.__dict__:
                    my_dict[_] = self.__dict__[_]
        else:
            my_dict = self.__dict__
        return my_dict
