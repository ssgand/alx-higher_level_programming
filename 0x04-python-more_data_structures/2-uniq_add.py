#!/usr/bin/python3
def uniq_add(my_list=[]):
    t = set(my_list)
    sum = 0
    for i in t:
        sum += i
    return sum
