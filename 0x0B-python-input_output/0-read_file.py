#!/usr/bin/python3


def read_file(filename=""):
    """Opens file and reads it"""
    with open(filename, 'r') as txt:
        txt = txt.read()
        print(txt, end="")
