#!/usr/bin/python3
def magic_calculator(a, b):
    if a < b:
        c = add(a, b)
       for i in range(4, 6):
           c = (c, i)
        return (c)
    else:
        return(sub(a, b))
