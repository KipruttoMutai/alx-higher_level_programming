#!/usr/bin/python3
"""
Module:1-my_list
resource:MyList class
"""


class MyList(list):
    """creates mylist"""
    def print_sorted(self):
        """class MyList that inherits from list
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
