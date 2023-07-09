#!/usr/bin/python3
"""
This module contains a Square class with a private instance
attribute called size.
"""


class Square:
    """
    The Square class defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square with the given size.

        Args:
            size (int): The size of the new square.

        """
        self.__size = size
