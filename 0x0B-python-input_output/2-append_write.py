#!/usr/bin/python3
""" append text to file and return number of chars wirtten"""


def append_write(filename="", text=""):
    """ append text to file and return number of chars wirtten"""
    with open(filename, 'a+', encoding='utf-8') as file:
        return file.write(text)
