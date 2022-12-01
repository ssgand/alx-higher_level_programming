#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
count = 1
if len(argv) == 1:
    print("0 arguments.")
elif len(argv) == 2:
    print("{} argument:".format(len(argv) - 1))
    print("{}: {}".format(count, argv[count]))
elif len(argv) > 2:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv) - 1):
        print("{}: {}".format(count, argv[count]))
        count += 1
