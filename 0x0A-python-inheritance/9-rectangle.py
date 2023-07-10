#!/usr/bin/python3
"""class"""


class BaseGeometry:
    """ BaseGeometry class"""

    def area(self):
        """raises error"""
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


class Rectangle(BaseGeometry):
    """Represents a rectangle class"""

    def __init__(self, width, height):
        """ init values
        Args:
            width (int): The width of the rectangle
            height (int): The height of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ return the area"""
        return self.__width * self.__height

    def __str__(self):
        """print the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
