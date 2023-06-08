#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv


argv.pop(0)

i = 1

print("{} argument:".format(len(argv)))

for arg in argv:
    print("{}: {}".format(i, arg))
    i += 1
