#!/usr/bin/python3

'''Defining a new function.'''


def write_file(filename='', text=''):
    '''Function to open and write to a file.'''
    with open(filename, 'w', encoding='utf-8') as fhand:
        return fhand.write(text)
