def add_integer(a, b=98):
    """
    Returns the addition of a and b. Both a and b must be integers or floats.
    If they are floats, they will be casted to integers before addition.
    If b is not provided, it defaults to 98.

    Args:
        a (int/float): The first number to be added.
        b (int/float): The second number to be added. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
