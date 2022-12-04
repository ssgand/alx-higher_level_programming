#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'C':
            new_string = my_string.replace('C', '')
            for i in new_string:
                if i == 'c':
                    new_string = new_string.replace('c', '')
        elif i == 'c':
            new_string = my_string.replace('c', '')
            for i in new_string:
                if i == 'C':
                    new_string = new_string.replace('C', '')
    return new_string
