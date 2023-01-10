#!/usr/bin/python3

'''Defining a new function.'''


def read_file(filename=''):
    '''Function to open a file for read_only.'''
    with open(filename, 'r', encoding='utf-8') as fhand:
        fread = fhand.read()
        print(fread)
