#!/usr/bin/python3

"""
module: 7-add_item
resources: add_arg_to_file() function
"""
import sys
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def add_arg_to_file(filename):
    """
    open the specified file with exclusive creation if file not available
    serialize an empty object to the file specified
    deserialize the contents of the file if file already existed
    loop through the command line arguments
    append the command line arguments to the list
    save the updated list / new list to the specified file
    """
    arg_count = len(sys.argv)
    try:
        with open(filename, "x") as file:
            pass
    except Exception:
        array = load_from_json_file(filename)
    else:
        array = []
    finally:
        for i in range(1, arg_count):
            array.append(sys.argv[i])
        save_to_json_file(array, filename)

    if __name__ == "__main__":
        storage_file = "add_item.json"
        add_arg_to_file(storage_file)
