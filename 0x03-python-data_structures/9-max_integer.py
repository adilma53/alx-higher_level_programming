#!/usr/bin/python3


def max_integer(my_list=[]):

    if my_list == []:
        return None

    max = 0

    for i in my_list:
        if i > max or i == None:
            max = i

    return max
