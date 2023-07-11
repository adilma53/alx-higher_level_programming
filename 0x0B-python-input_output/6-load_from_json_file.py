#!/usr/bin/python3

""" create string from file that is of json type"""

import json


def load_from_json_file(filename):
    """ create string from file that is of json type"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
