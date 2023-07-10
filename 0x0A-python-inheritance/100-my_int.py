#!/usr/bin/python3
""" reverse == and != fucntionality """


class MyInt(int):
    """ reverse == and != fucntionality """

    def __eq__(self, other):
        """ convert == to !=

        Args:
            other (any type): __

        Returns:
            any type: ___
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """ convert != to ==

        Args:
            other (any type): __

        Returns:
            any type: ___
        """
        return super().__eq__(other)
