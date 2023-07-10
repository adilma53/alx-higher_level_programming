#!/usr/bin/python3


class MyList(list):
    """ inheritance """

    def print_sorted(self):
        """ print sorted list """
        if issubclass(MyList, list):
            print(sorted(self))
