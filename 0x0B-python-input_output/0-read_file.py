#!/usr/bin/python3
"""read from file and print to stdout"""


def read_file(filename=""):
    """read from file and print to stdout

    Args:
        filename (str, optional): file to read from.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
