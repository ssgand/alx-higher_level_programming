#!/usr/bin/python3

from models.base import Base

'''Defining a rectangle class.'''


class Rectangle(Base):
    '''Rectangle class to inherit from the base class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        z = 0
        while z < self.__y:
            print('')
            z += 1
        i = 0
        while i < self.__height:
            j = 0
            print(' ' * self.__x, end='')
            while j < self.__width:
                print('#', end='')
                j += 1
            print()
            i += 1

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        dic = {}
        r = self.__height
        e = self.__width
        d = self.__x
        z = self.__y
        dic = {'id': self.id, 'width': e, 'height': r, 'x': d, 'y': z}
        return dic

    def __str__(self):
        t = __class__.__name__
        r = self.__height
        e = self.__width
        d = self.__x
        z = self.__y
        return '[{}] ({}) {}/{} - {}/{}'.format(t, self.id, d, z, e, r)

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
        if not type(value) == int:
            raise TypeError('{} must be an integer'.format(attribute))
        elif attribute == 'x' or attribute == 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attribute))
        else:
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attribute))
