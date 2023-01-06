#!/usr/bin/python3

'''Using getters and setters to retrieve data and use it.'''


class Square:
    '''The square class.'''
    def __init__(self, size=0):
        '''Initializing the square class.'''
        self.__size = size

    def area(self):
        '''Method to calculate the area of a square.'''
        return self.__size ** 2

    @property
    def size(self):
        '''Set the size of the square.'''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
