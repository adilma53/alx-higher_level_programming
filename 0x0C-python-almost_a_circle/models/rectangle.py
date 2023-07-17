#!/usr/bin/python3

"""rectangle model"""

from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, x=0, y=0, width, height, id=None):
        super().__init__(id)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
