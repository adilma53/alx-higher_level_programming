#!/usr/bin/python3
"""This module defines the Rectangle class"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__height * self.width

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Returns a string representation of the rectangle"""
        empty_string = ""
        if self.__height == 0 or self.__height == 0:
            return empty_string
        for i in range(self.__height):
            empty_string += "#" * self.__width
            if i != self.__height - 1:
                empty_string += '\n'
        return empty_string

    def __repr__(self):
        """Returns a string representation of the rectangle object"""
        empty_string = "Rectangle(" + str(self.__width)
        empty_string += ", " + str(self.__height) + ")"
        return empty_string
