#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """test """
    i = len(my_list) - 1
    if isinstance(my_list, list):
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
