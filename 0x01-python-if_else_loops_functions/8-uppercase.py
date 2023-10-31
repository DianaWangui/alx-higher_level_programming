#!/usr/bin/python3
def uppercase(str):
    for char in str:
        character = ord(char)
        if character >= 97 and character <= 122:
            character -= 32
        print("{}".format(chr(character)), end="")
    print()
