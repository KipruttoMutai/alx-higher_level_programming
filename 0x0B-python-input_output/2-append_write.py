#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends new text to a file or creates a new one if its non existent
    Args:
    filename: name of file
    text: text to append
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
