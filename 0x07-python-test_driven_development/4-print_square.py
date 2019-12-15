#!/usr/bin/python3
""" ``print_square`` function
    This function print a # square according to size
    Recive a size variable with length and return
    a square.
"""


def print_square(size):
    """ ``print_square`` function
        print a # square.
    """
    if type(size) is not int or type(size) is float:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        print("{}".format("{}\n".format("#"*size) * size))
