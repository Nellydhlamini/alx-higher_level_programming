#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':

    l_av = len(argv) - 1

    if l_av == 3:
        operator = argv[2]
        num_1 = int(argv[1])
        num_2 = int(argv[3])
        if operator == '+':
            res = add(num_1, num_1)
            print("{:d} + {:d} = {:d}".format(num_1, num_2, res))
            exit(0)
        elif operator == '-':
            res = sub(num_1, num_1)
            print("{:d} - {:d} = {:d}".format(num_1, num_2, res))
            exit(0)
        elif operator == '*':
            res = mul(num_1, num_1)
            print("{:d} * {:d} = {:d}".format(num_1, num_2, res))
            exit(0)
        elif operator == '/':
            res = div(num_1, num_1)
            print("{:d} / {:d} = {:d}".format(num_1, num_2, res))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
