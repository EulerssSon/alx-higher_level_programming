#!/usr/bin/python3
"""This Module is to reaf file in utf-8 format"""


def read_file(file_name=""):
    """read file in utf-8 cod3

    Args:
        file_name (str, optional): _description_. file name
    """
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
