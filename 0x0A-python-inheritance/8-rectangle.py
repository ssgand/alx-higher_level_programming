#!/usr/bin/python3

'''Defining a class.'''


class BaseGeometry:
    '''Define a class called BaseGeometry.'''

    def area(self):
        '''area method.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validating the value attribute.'''
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


'''Defining a new class.'''


class Rectangle(BaseGeometry):
    '''Rectangle class as a child of BaseGeometry class.'''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator():
        super().integer_validator()
