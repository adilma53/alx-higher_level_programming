
# !/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)

    if a_len == 0:
        new_tuple_a = (0, 0)
    elif a_len == 1:
        new_tuple_a = (tuple_a[0], 0)
    else:
        new_tuple_a = tuple_a

    if b_len == 0:
        new_tuple_b = (0, 0)
    elif b_len == 1:
        new_tuple_b = (tuple_b[0], 0)
    else:
        new_tuple_b = tuple_b

    return (new_tuple_a[0] + new_tuple_b[0], new_tuple_a[1] + new_tuple_b[1])
