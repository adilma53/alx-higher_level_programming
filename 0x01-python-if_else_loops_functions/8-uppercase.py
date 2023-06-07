#!/usr/bin/python3

def uppercase(s):
    i = 0
    for c in s:
        i += 1
        if ord(c) >= 97 and ord(c) <= 122:
            up_c = chr(ord(c) - 32)
            print("{}".format(up_c), end="" if i < len(s) else "\n")
        else:
            print("{}".format(c), end="" if i < len(s) else "\n")
