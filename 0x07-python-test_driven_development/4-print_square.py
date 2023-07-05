#!/usr/bin/python3

'''
   print_square function
'''


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and is less than 0.

    """
    # Check that size is an int
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    # Check if size is less than zero
    if size < 0:
        raise ValueError('size must be >= 0')

    # Check if size is float and is less than zero
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    # print a square with '#' by size
    for rows in range(size):
        for cols in range(size):
            print('#', end='')
        print()
