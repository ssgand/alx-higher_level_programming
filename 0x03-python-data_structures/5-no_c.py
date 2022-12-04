#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if i == 'c':
            new_string += ''
            for i in new_string:
                if i == 'C':
                    new_string += ''
        elif i == 'C':
            new_string += ''
            for i in new_string:
                if i == 'c':
                    new_string += ''
        else:
            new_string += i
    return new_string
