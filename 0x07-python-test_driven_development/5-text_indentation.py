#!/usr/bin/python3
"""This Moudle is to print /n/n after .?:"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and:

    Args:
        text (str): the text to print

    Returns:
        None

    Raises:
        TypeError: If text is not a string
    """
    if type(text) is not str or text is None:
        raise TypeError('text must be a string')
    for char in '.:?':
        text = (char + '\n\n').join(
            [line.strip(' ') for line in text.split(char)])
    print(text, end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
