#!/usr/bin/python3
for i in range(100):
    tens_digit = i // 10
    ones_digit = i % 10
    if tens_digit >= ones_digit:
        continue
    if i < 10:
        formatted_i = "0{:d}".format(i)
    else:
        formatted_i = "{:d}".format(i)
    if i == 89:
        print(formatted_i)
    else:
        print(formatted_i, end=", ")
