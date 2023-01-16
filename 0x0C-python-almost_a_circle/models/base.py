#!/usr/bin/python 3


'''Defining a class named base.'''


class Base:
    '''Class that will be the base of all other
    classes for the models package.'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
