#!/usr/bin/python3

'''Defining a Node class.'''


class Node:
    '''Node class created.'''
    def __init__(self, data, next_node=None):
        '''Initializing the node class.'''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and value != Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


'''Defining a SinglyLinkedList class.'''


class SinglyLinkedList:
    '''The singlyLinkedList class.'''
    sl_list = []

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        '''Inserts a new Node into the correct sorted position in the list.'''
        SinglyLinkedList.sl_list.append(value)
        SinglyLinkedList.sl_list.sort()

    def __str__(self):
        i = 0
        while i < len(SinglyLinkedList.sl_list):
            print(SinglyLinkedList.sl_list[i])
            i += 1
        return str(SinglyLinkedList.sl_list)
