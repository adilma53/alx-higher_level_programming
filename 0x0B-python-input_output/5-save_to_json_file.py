#!/usr/bin/python3

""" write string to file in jason format"""
import json


def save_to_json_file(my_obj, filename):
    """ write string to file in jason format"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
