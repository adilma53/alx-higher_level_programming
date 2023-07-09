#!/usr/bin/python3
"""
This module contains a Square class with a private instance attribute
called size
and a public instance method called area.
"""


class Square:
    """
    The Square class defines a square with a private size attribute
    and a public area method.
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Computes and returns the area of this square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2
