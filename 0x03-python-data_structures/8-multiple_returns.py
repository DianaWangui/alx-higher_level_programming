#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return (0, None)
    else:
        no_empty = (length, sentence[0])
        return no_empty
