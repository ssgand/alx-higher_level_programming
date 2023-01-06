#!/usr/bin/python3

'''Defining a class.'''


class Square:
    '''The square class.'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initializing the square class.'''
        self.__size = size
        self.__position = position

    def area(self):
        '''Method to calculate the area of a square.'''
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print('')
        elif self.__position[1] > 0:
            for z in ('#' * self.__size):
                print('#' * self.__size)
        else:
            for z in ('#' * self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    @property
    def size(self):
        '''Set the size of the square.'''
        return self.__size

    def position(self):
        '''Set the position of the square.'''
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def position(self, value):
        if not value[0] > 0 and value[1] > 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
