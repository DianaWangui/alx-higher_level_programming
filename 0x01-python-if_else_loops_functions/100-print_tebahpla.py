#!/usr/bin/python3
for i in range(ord('z'), ord('A') -1, -1):
    if i % 2 == 00:
        print("{:c}".format(i), end="")
    else:
        print("{:c}".format(i -32), end="")
print()
