#!/usr/bin/python3
"""peak-find function"""

def find_peak(list_of_integers):
    """find the peak of list of integers"""
    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    for num in list_of_integers:
        if num >= peak:
            peak = num

    return peak
