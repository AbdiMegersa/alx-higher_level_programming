#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argument = sys.argv
    if len(argument) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argument[2] != '+' or '-' or '*' or '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argument[1])
    b = int(argument[3])
    if argument[2] == '+':
        print("{:d} {} {:d} = {:d}".format(a, argument[2], b, add(a, b)))
    if argument[2] == '-':
        print("{:d} {} {:d} = {:d}".format(a, argument[2], b, sub(a, b)))
    if argument[2] == '*':
        print("{:d} {} {:d} = {:d}".format(a, argument[2], b, mul(a, b)))
    if argument[2] == '/':
        print("{:d} {} {:d} = {:d}".format(a, argument[2], b, div(a, b)))
