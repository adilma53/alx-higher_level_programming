#!/usr/bin/python3

def uppercase(s):
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            up_c = chr(ord(c) - 32)
            print({}.format(up_c), end="")
        else:
            print({}.format(c), end="")
    print()
