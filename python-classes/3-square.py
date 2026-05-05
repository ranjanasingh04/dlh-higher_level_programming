#!usr/bin/python3
""" Module that calculate area of square"""


class Square:
    """ Square Class """
    def __init__(self, _size=0):
        """ Initiale Square to calculare area"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self._size = size
        
        def area(self):
            """ Calculare area of square"""
            return self.__size ** 2

