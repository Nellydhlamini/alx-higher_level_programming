#!/usr/bin/python3
def uppercase(str):
    new = ""
    for a in range(len(str)):
        if (ord(str[a]) >= 97 and ord(str[a]) <= 122):
            new += chr(ord(str[a]) - 32)
            continue
        new += str[a]

    print("{0}".format(new))
