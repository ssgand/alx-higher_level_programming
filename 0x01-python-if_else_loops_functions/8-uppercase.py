#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            i=chr(ord(i) - 32)
            print('{i}'.format(i=i), end='')
        print()