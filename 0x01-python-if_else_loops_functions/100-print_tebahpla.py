#!/usr/bin/python3
for a in reversed(range(97, 123)):
    if (a % 2 == 0):
        print("{:c}".format(a), end='')
    else:
        print("{:c}".format(a - 32), end='')
