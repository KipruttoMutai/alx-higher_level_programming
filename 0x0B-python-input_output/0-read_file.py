#!/usr/bin/python3
"""A function module"""


def read_file(filename=""):
    """opens a file reads and prints it out
    Args:
        filename(str): name of file
    """
    with open(filename, encoding='utf-8') as open_file:
        print(open_file.read(), end="")
