#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    biggest = None
    key_big = None
    for i in a_dictionary:
        if biggest is None:
            biggest = a_dictionary[i]
            key_big = i
        elif a_dictionary[i] > biggest:
            biggest = a_dictionary[i]
            key_big = i
    return key_big
