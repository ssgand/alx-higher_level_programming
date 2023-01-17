#!/usr/bin/python 3


'''Defining a class named base.'''


import json


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

    def to_json_string(list_dictionaries):
        if list_dictionaries == {} or list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        with 
        if list_objs is None:
            json.dump([])
