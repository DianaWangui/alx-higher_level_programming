#!/usr/bin/python3
if __name__ = '__main__':
    import sys

    arg_count = len(sys.argv) - 1  # Minus the file name argument
    if arg_count == 0:
        print("{:d} aggument.".format(arg_count))
    elif arg_count == 1:
        print("{:d} argument:".format(arg_count))
    else:
        print("{:d} arguments:".format(arg_count))
    for i in range(arg_count):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
