#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    max_k = None
    max_v = None

    for i, j in a_dictionary.items():
        if max_k is None or j > max_k:
            max_k = j
            max_v = i

    return max_v
