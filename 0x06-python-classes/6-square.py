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
        else:
            for z in ('#' * self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

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

    @property
    def position(self):
        '''Set the position of the square.'''
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
