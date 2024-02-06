#!/usr/bin/python3
"""100-append_after.py"""


def append_after(filename="", search_string="", new_string=""):
    """t inserts a line of text to a file
    after each line containing a specific string"""
    data = []

    with open(filename, mode="r", encoding="utf-8") as file_obj:
        data = file_obj.readlines()
        idx = 0
        while idx < len(data):
            if search_string in data[idx]:
                data[idx:idx + 1] = [data[idx], new_string]
                idx += 1
            idx += 1

    with open(filename, mode="w", encoding="utf-8") as file_obj:
        file_obj.writelines(data)
