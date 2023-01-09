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
