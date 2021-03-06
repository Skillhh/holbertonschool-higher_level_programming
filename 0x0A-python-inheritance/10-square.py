#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """ Override width and height with size
        """
        super().integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size
