#!/usr/bin/python3
"""
module defining the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    rectangle class, a subclass of Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializes a Rectangle instance.
        """
        super().__init__(id)

        self._check_integer_parameter(width, 'width')
        self._check_integer_parameter(height, 'height')
        self._check_integer_parameter(x, 'x')
        self._check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, param):
        """set the width of the rectangle."""
        self._check_integer_parameter(param, 'width')
        self.__width = param

    @property
    def height(self):
        """get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, param):
        """set the height of the rectangle."""
        self._check_integer_parameter(param, 'height')
        self.__height = param

    @property
    def x(self):
        """get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, param):
        """set the x-coordinate of the rectangle."""
        self._check_integer_parameter(param, 'x')
        self.__x = param

    @property
    def y(self):
        """get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, param):
        """set the y-coordinate of the rectangle."""
        self._check_integer_parameter(param, 'y')
        self.__y = param

    def _check_integer_parameter(self, value, param):
        """
        check if the value is an integer and validate its range.
        """
        if not isinstance(value, int):
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """calculate the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """display the rectangle using '#' characters."""
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.__height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """return a string representation of the rectangle."""
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        update the attributes of the rectangle.
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        convert the rectangle object to a dictionary.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
