#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

argv.pop(0)
i = 1
len = len(argv)

if len > 0 and len != 1:
    print("{} arguments:".format(len))
elif len == 0:
    print("{} arguments.".format(len))
elif len == 1:
    print("{} argument:".format(len))


for arg in argv:
    print("{}: {}".format(i, arg))
    i += 1
