#!/usr/bin/python3
import sys

args = sys.argv
args.pop(0)

i = 1

print(f"{len(args)} argument:")

for arg in args:
    print("{}: {}".format(i, arg))
    i += 1
