#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
count = 0 
if len(argv) == 1:
    print("0 arguments.")
elif len(argv) > 1:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv) - 1):
        count += 1
        print("{}: {}".format(count, argv[count]))
