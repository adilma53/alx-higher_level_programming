#!/usr/bin/python3
""" a function that convert jason to string"""

import json


def from_json_string(my_str):
    """ a function that convert jason to string"""
    return json.loads(my_str)
