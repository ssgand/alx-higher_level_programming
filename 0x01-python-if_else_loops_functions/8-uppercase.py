#!/usr/bin/python3
def uppercase(c):
    for i in c:
        p = i
        if ord(i) >= 97 and ord(i) <= 122:
            p = chr(ord(i) - 32)
        print('{p}'.format(p=p), end='')
    print()

