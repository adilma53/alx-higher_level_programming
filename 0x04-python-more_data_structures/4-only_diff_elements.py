#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    common = set_1 & set_2
    joined_set = set_1 | set_2
    new_set = set()

    for i in joined_set:
        if i not in common:
            new_set.add(i)

    return new_set
