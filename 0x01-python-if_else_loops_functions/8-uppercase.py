#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            p = ord(i) - 32
            print('{p:c}'.format(p=p), end='')
        else:
            print('{i}'.format(i=i), end='')
    print()
