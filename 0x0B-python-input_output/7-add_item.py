#!/usr/bin/python3
"""Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""

if __name__ == "__main__":
    import sys
    import json
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        item = load_from_json_file("add_item.json")
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save_to_json_file(item, "add_item.json")
