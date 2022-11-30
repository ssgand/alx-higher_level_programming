#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print('0{i}'.format(i=i), end=", ")
    else:
        print(i, end=", ")
print(99)
