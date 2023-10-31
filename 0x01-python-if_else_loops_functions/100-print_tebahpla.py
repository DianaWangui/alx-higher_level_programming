#!/usr/bin/python3
for i in range(0, 26):
    c = ord('z') - i
    if i % 2 == 1:
        c = (chr(c - ord('a') + ord('A')))
    else:
        c = chr(c)
    print("{}".format(c), end='')
