FG
"""Module to check if an object is an instance of a class that inherited
directly or indirectly from the specified class"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited
    directly or indirectly from the specified class

    Args:
        obj: object to check
        a_class: class to check

    Returns:
        True if the object is an instance of a class that inherited
        directly or indirectly from the specified class; otherwise False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
