#!/usr/bin/python3
"""
module:1-my_list
resource:print_sorted
"""


class Mylist(list):
    """creates mylist"""
    def print_sorted(self):
        """class MyList that inherits from list
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
