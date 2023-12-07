#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """creates a file if it does not exist and overwrites if it does
    Args:
        filename: name of file
        text: text to write"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
