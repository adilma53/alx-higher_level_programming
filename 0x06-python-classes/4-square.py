#!/usr/bin/python3
"""
This module contains a Square class with a private instance
attribute called size,
a public instance method called area, and getter and setter
methods for the size attribute.
"""


class Square:
    """
    The Square class defines a square with a private size attribute,
    a public area method, and getter and setter methods for the size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square with the given size.

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size

    def area(self):
        """
        Computes and returns the area of this square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the current size of this square.

        Returns:
            The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Updates the size of this square to the given value.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
