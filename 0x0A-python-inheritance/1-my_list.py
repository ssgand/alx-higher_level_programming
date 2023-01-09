#!/usr/bin/python3

'''Defining a class.'''




class MyList(list):
    '''Child class defined.'''

    def __init__(self, object):
        '''Initializing our function.'''
        self.object = object

    def print_sorted(self):
        '''function to return a sorted list.'''
        print(self.object.sort())
        

