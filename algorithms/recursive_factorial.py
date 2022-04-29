"""Module implements factorial function"""


def fact(number):
    """Factorial function.

    Args:
        number (int): integer.

    Returns:
        number * fact(number - 1): if number > 0.
        1: if number == 0.
    """
    if number == 0:
        return 1
    return number * fact(number - 1)
