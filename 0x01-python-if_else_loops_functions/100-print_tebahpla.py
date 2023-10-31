#!/usr/bin/python3
for i in range(ord('z'), ord('A') - 1, - 1):
    if ord('a') <= i <= ord('z'):
        print("{:c}".format(i), end="")
    elif ord('A') <= i <= ord('Z'):
        print(("{:c}".format(i), end="")
print()
