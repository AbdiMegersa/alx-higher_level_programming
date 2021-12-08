#!/usr/bin/python3
""" This creates a class called Square
"""


class Square:
    """ Instantiation"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
    def area(self):
        return size * size
