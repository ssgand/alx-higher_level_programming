#!/usr/bin/python3

'''Defining a new function.'''


import json
# '''Importing the json module.'''


def to_json_string(my_obj):
    '''Function to make python objects into javascript strings.'''
    return json.dumps(my_obj)
