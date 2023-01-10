#!/usr/bin/python3

'''Defining a new function.'''


def append_write(filename='', text=''):
    '''Function to append new test at the end of an existing file.'''
    with open(filename, 'a+', encoding='UTF8') as fhand:
        f = fhand.write(text)
        return f
