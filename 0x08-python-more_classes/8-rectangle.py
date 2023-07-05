#!/usr/bin/python3
"""This module defines the Rectangle class"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join([str(self.print_symbol)
                for _ in range(self.__width)]) for _ in range(self.__height)]))

    def __repr__(self):
        """Returns a string representation of the rectangle object"""
        empty_string = "Rectangle(" + str(self.__width)
        empty_string += ", " + str(self.__height) + ")"
        return empty_string

    def __del__(self):
        """Deletes the rectangle object and prints a message"""
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
