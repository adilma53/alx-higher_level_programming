#!/usr/bin/python3
""" write to file and return number chars written"""


def write_file(filename="", text=""):
    """ write to file and return number chars written"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
