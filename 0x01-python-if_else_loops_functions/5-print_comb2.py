#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{:d},".format(i), end=" ")
        continue
    elif i == 99:
        print("{:d}".format(i))
        continue
    else:
        print("{:d},".format(i), end=" ")
