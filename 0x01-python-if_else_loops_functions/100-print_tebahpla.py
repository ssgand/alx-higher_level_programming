#!/usr/bin/python3
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{c}".format(chr(c - 1)), end='')
    i = 32 if i == 0 else 0
