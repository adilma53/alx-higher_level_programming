#!/usr/bin/python3
" inheriting list class"


class MyList(list):
    """ inheritance """

    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))
