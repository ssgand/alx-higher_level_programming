#!/usr/bin/python3

'''Defining a class Square with a size attribute
having a default value and calculating its area with area method.'''


class Square:
    '''The square class.'''
    def __init__(self, size=0):
        '''Initializing a new square.'''
        if not int(size) == size:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Return the area of the square.'''
        return self.__size ** 2
