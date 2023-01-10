#!/usr/bin/python3

'''Collecting command line arguments and saving them in json file.'''


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

n = len(sys.argv)
try:
    c = load_from_json_file('add_item.json')
    for i in range(1, n):
        c.append(sys.argv[i])
    save_to_json_file(c, 'add_item.json')
except FileNotFoundError:
    j = []
    for i in range(1, n):
        j.append(sys.argv[i])
    save_to_json_file(j, 'add_item.json')
