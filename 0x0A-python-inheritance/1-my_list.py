#!/usr/bin/python3
"____________________"


class MyList(list):
    """ inheritance """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
