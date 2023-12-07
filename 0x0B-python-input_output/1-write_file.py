#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """"""
    with open(filename, mode='w', encoding='utf-8') as b_file:
        b_file.write(text)
