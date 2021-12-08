#!/usr/bin/python3
def __init__(self, size=0):
        """
            Instantiations with size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if type < 0:
            raise ValueError("size must be >= 0")

        def size(self, value):
            self.__size = value

        def size(self):
            return self.__size

        def area(self):
            """
                Instantiations with size
            """
            return self.__size ** 2


