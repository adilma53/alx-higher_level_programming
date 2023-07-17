#!/usr/bin/python3
"""base class"""


class Base:
    """base class to manage the id attribute for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        constrcutopr for __nb_objects attribute
        """
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = Base.__nb_objects
