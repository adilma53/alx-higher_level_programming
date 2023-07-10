#!/usr/bin/python3

"""square inheritance from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


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
