#!/usr/bin/python3

'''Defining a new function.'''


import json
'''Importing loads form json module.'''


def from_json_string(my_str):
    '''Function to represent javascript object to python objects.'''
    f = json.loads(my_str)
    return f
