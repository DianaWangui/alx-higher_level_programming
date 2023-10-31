#!/usr/bin/python3
for i in range(ord('z'), ord('A') -1, -1):
    if ord('z') - i % 2 == 0:
        print("{:c}".format(i), end="")
print()
