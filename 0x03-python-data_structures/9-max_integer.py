#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = None
    num = None
    if my_list == []:
        return None
    else:
        for i in my_list:
            num = i
            if biggest is None:
                biggest = num
            elif num > biggest:
                biggest = num
            else:
                continue
    return biggest
