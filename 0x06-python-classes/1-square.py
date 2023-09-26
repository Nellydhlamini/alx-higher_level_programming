#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 0-square.py)

"""


class Square:
    """
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    """

    def __init__(self, size):
        """__init__

        The __init__ method initializes the size value
        of the square.

        Attributes:
            size (int): The size of the square.

        """
        self.__size = size
