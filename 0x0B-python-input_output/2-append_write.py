#!/usr/bin/python3

""" A function that appends a string to a utf file"""


def append_write(filename="", text=""):
    """Writes a str to utf text file
    Args:
        filename(str): The name of fime to append
        text(str): The text to append to the file
    Return:
        number of char appended
    """

    with open(filename, "a", encoding="utf-8") as f:
        append = f.write(text)
        return append
