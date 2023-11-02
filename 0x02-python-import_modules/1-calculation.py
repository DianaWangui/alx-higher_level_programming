#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    result_a = add(a, b)
    result_s = sub(a, b)
    result_m = mul(a, b)
    result_d = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, result_a))
    print("{:d} + {:d} = {:d}".format(a, b, result_s))
    print("{:d} + {:d} = {:d}".format(a, b, result_m))
    print("{:d} + {:d} = {:d}".format(a, b, result_d))
