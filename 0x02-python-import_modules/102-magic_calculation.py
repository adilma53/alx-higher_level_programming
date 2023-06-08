#!/usr/bin/python3

from magic_calculation_102 import add, sub


def magic_calculation(a, b):

    if a < b:
        calc = add(a, b)
        for i in range(4, 6):
            calc = add(calc, i)
        return calc
    else:
        return sub(a, b)
