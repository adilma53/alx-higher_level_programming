#!/usr/bin/python3
'''
   3-say_my_name
'''


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """


err1 = 'first_name must be a string'
err2 = 'last_name must be a string'
name = 'My name is '


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError(err1)
    if not isinstance(last_name, str):
        raise TypeError(err2)
    else:
        print('My name is {} {}'.format(first_name, last_name))
