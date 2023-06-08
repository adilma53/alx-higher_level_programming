#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

argv.pop(0)
len = len(argv)
sum = 0


for arg in argv:
    print("{}: {}".format(i, arg))
    sum += int(arg)

print(sum)
