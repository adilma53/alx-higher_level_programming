#!/usr/bin/python3

""" function that show all attribute of an object"""


def lookup(obj):
    """function that show all attribute of an object

    Args:
        obj (class): object to operate on

    Returns:
        list: list of object atributes
    """
    if obj:
        return (dir(obj))
