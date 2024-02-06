#!/usr/bin/python3

"""
module:2-append_write
resources:append_write()function
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        no_of_characters = file.write(text)
        return no_of_characters
