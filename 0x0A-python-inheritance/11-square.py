#!/usr/bin/python3

""" BaseGeometry class"""


class BaseGeometry:
    """ BaseGeometry class"""

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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """ constructor
        Args:
            width (int): width
            height (int): height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ print rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class """

    def __init__(self, size):
        """contructor """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ over writing (rectangle) with area of square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
