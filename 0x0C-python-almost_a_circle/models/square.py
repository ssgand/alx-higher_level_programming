#!/usr/bin/python3

'''Defining a class called square that inherits from the rectangle class.'''


from models.rectangle import Rectangle

class Square(Rectangle):
    '''Setting the Square class.'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        t = __class__.__name__
        z = self.id
        d = self.x
        j = self.y
        r = self.width
        return '[{}] ({}) {}/{} - {}'.format(t, z, d, j, r)

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        else:
            try:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass

    def to_dictionary(self):
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.setter_validation('width', value)
        self.width = value
