#!/usr/bin/python3
"""Module with a funciton"""


def find_peak(list_of_integers):
    """Function that prints a peak of a list"""
    left, right = 0, len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
