#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    col = 0
    for row in matrix:
        items = len(row) - 1
        for number in row:
            if col < items:
                print("{:d}".format(number), end=" ")
            else:
                print("{:d}".format(number), end="")
            col += 1
        print()
