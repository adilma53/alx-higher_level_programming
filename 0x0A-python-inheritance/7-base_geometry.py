#!/usr/bin/python3


"""class"""


class BaseGeometry:
    """class"""

    def area(self):
        """ function that raises ("area() is not implemented")"""
        raise Exception("area () is not implemented")

    def integer_validator(self, name, value):
        """
        check if value is int and larger than 0
        Args:
            name (str): name
            value: value
        Raises:
            TypeError: if value is int
            ValueError: is value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
