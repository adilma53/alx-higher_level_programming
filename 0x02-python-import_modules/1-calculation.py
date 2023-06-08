#!/usr/bin/python3
from calculator_1 import *


if __name__ == "__main__":
    """mini calculator that performs (+,-,*,/)"""


a = 10
b = 5


ops = [
    ('+', add),
    ('-', sub),
    ('*', mul),
    ('/', div)
]


for op, func in ops:
    result = func(a, b)
    print('{} {} {} = {}'.format(a, op, b, result))
