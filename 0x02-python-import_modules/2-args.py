#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv


argv.pop(0)

i = 1

len = len(argv)

print("{} argument:".format(len) if len > 0 else "{} argument.".format(len))

for arg in argv:
    print("{}: {}".format(i, arg))
    i += 1
