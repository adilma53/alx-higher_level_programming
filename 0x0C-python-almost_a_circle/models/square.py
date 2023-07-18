#!/usr/bin/python3
"""
module defining the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class, a subclass of Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes a Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        returns a string representation of the square.
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """
        gets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the size of the square (width and height).
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of the square.
        """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        converts the square object to a dictionary.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
