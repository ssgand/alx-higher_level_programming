#!/usr/bin/python3

'''Defining a class Square with a size attribut having a default value.'''


class Square:
    '''The square class.'''
    def __init__(self, size=0):
        if not int(size) == size:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
