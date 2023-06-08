#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

argv.pop(0)
sum = 0

for arg in argv:
    sum += int(arg)

print(sum)
