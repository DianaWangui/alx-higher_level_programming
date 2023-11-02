#!/usr/bin/python3
if __name__ = '__main__':
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format('0'))
    elif count == 1:
        print("{} argument:".format(count))
    else:
        print("{} argument:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
