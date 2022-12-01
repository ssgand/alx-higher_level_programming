#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
sum = 0
count = 1
if len(argv) == 1:
    print(0)
else:
    for i in range(len(argv) - 1):
        sum += int(argv[count])
        count += 1
    print(sum)
