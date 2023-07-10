#!/usr/bin/python3
""" check if obj parrent is inherited from a_class
but but not an instance of a_class"""


def inherits_from(obj, a_class):
    """ check if obj parrent is inherited from a_class
    but but not an instance of a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
