#!/usr/bin/python3

def uppercase(s):
    for c in s:
        print("{}".format(chr(ord(c) - 32)) if ord(c) >= 97 and
              ord(c) <= 122 else "{}".format(c), end="")
    print("")
