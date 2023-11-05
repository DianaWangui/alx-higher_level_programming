#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)

    for row in matrix:
        items = len(row)
        column = 0
        for number in row:
            if column < items - 1
                print("{:d}".format(number), end=" ")
            else:
                print("{:d}".format(number), end="")
            column += 1
        print()
