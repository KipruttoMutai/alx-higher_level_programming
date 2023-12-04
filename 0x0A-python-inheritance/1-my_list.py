#!/usr/bin/python3
"""MyList class that prints sorted int object attributes."""


class MyList(list):
    """My list class inheriting from the built-in list class"""

    def print_sorted(self):
        """Prints sorted attributes specific to int objects."""

        print(sorted(self))
