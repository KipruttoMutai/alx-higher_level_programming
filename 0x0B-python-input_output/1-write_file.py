#!/usr/bin/python3

""""""


def write_file(filename="", text=""):
    """writes a string to a text file
    returns the number of characters written
     """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return file.tell()
