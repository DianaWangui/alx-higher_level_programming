#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        return (0, None)
    else:
        no_empty = (length, first)
        return (no_empty)
