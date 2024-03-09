#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None) -> dict:
        """_summary_

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            dict: _description_
        """
        my_dict = {}
        if attrs is None:
            my_dict = self.__dict__
        elif isinstance(attrs, list):
            if all(isinstance(attribute, str) for attribute in attrs):
                for attribute in attrs:
                    if hasattr(self, attribute):
                        my_dict[attribute] = getattr(self, attribute)
        return my_dict
