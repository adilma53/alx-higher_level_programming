#!/usr/bin/python3

def best_score(a_dictionary):

    if not a_dictionary:
        return None

    for key in a_dictionary:
        max_n = a_dictionary[key]
        break

    key = ""

    for i, j in a_dictionary.items():
        if j > max_n:
            max_n = j
            key = i

    return key
