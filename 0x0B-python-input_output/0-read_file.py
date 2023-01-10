#!/usr/bin/python3

'''Defining a new function.'''


def read_file(filename=''):
    '''Function to open a file for read_only.'''
    with open(filename, 'r', encoding='UTF8') as fhand:
        for line in fhand:
            # fread = fhand.read()
            print(line, end='')
