#!/usr/bin/python3

from models.base import Base

'''Defining a rectangle class.'''


class Rectangle(Base):
    '''Rectangle class to inherit from the base class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setter_validation('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setter_validation('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setter_validation('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setter_validation('y', value)
        self.__y = value


    @staticmethod
    def setter_validation(attribute, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(attribute))
        elif attribute == 'width' or attribute == 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attribute))
        else:
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attribute))
