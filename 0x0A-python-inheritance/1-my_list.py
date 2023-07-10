#!/usr/bin/python3

class MyList(list):
    def __init__(self):
        super().__init__()
        self.list = []

    def print_sorted(self):
        print(sorted(self.list))

    def __str__(self):
        return str(self.list)
