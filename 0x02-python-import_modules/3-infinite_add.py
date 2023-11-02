#!/usr/bin/python3
import sys

def add_arg(*args):
    total = sum(map(int, args))
    return total

if __name__ == '__main__':

    args = sys.argv[1:]
    result = add_arg(*args)
    print(result)
