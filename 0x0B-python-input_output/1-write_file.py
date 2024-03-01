#!/usr/bin/python3
"""This Module is to write file in utf-8 format"""


def write_file(filename="", text=""):
    """function to write in

    Args:
        filename (str, optional):the name of the file
        text (str, optional): the text to be written in the file

    Returns:
        int: the number of characters written in the file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
