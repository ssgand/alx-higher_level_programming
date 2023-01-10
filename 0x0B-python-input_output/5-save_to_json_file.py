#!/usr/bin/python3

'''Defining a new class.'''


import json
'''Importing the json module.'''


def save_to_json_file(my_obj, filename):
    '''function to save python objects into a json file.'''
    with open(filename, 'w+', encoding='utf-8') as fhand:
        json.dump(my_obj, fhand)
