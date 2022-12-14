#!/usr/bin/python3

'''Defining a new function.'''


import json
'''Importing the json module.'''


def load_from_json_file(filename):
    '''Function to represent python objects form json file.'''
    # f = ''
    with open(filename, 'r', encoding='utf-8') as fhand:
        '''for line in fhand:
            f += line'''
        return json.load(fhand)
