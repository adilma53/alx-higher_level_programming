#!/usr/bin/python3

"""function to add attributes to instances"""


def add_attribute(obj, attribute, value):
    """Afunction to add attributes to instances

    Args:
        obj (any): instance to add to
        attribute (string): name
        value (any): value
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
