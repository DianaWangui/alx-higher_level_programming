#!/usr/bin/python3
for i in range(100):
    if i < 10:
       formatted_i = "0{:d}".format(i)
    else:
       formatted_i = "{:d}".format(i)
    if i == 99:
        print(formatted_i)
    else:
        print(formatted_i, end=", ")
