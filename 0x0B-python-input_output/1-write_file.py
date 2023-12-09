#!/usr/bin/python3

"""Defines a file writing function"""


def write_file(filename="", text=""):
    """Writes a str to utf text file
    Args:
        filename(str): The name of fime to write
        text(str): The text to write to the file
    Return:
        number of char written
        """
    with open(filename, "w", encoding="utf-8") as f:
       write = f.write(text)
       return write
