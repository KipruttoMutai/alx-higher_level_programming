#!/usr/bin/python3

"""
module: 1-write_file
resources: write_file() function
"""


def write_file(filename="", text=""):
    """writes a string to a text file
    returns the number of characters written
     """
    with open(filename, 'w', encoding='utf-8') as file:
        number_of_text = file.write(text)
        return number_of_text
