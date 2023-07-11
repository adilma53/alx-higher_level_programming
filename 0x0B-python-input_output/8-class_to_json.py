#!/usr/bin/python3

""" class to json"""


def class_to_json(obj):
    """ class to json"""
    stored = {}
    if hasattr(obj, "__dict__"):
        stored = obj.__dict__.copy()
    return stored
