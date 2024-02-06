#!/usr/bin/python3


def read_file(filename=""):
    """Opens file and reads it"""
    with open(filename, 'r', encoding='utf-8') as txt:
        for line in txt:
            print(line, end='')
