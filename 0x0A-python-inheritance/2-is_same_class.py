#!/usr/bin/python3

""" check if ob is an instance of a specific class"""


def is_same_class(obj, a_class):
    """ check if ob is an instance of a specific class"""
    if type(obj) is a_class:
        return True
    else:
        return False
