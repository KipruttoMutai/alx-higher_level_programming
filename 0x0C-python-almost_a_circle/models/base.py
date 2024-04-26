#!/usr/bin/python3
"""
modules:base.py
resources:class base
"""
import json
import csv


class Base:
    """creates a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
         assigns the public instance attribute id with this argument value
         if id is not none otherwise  assigns the new value to
         the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the json string representation of a dictionary"""
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list_objs = []
        if type(list_objs) is list:
            for item in list_objs:
                new_list_objs.append(item.to_dictionary())
        class_name = cls.__name__
        filename = f"{class_name}.json"
        json_string = Base.to_json_string(new_list_objs)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a new object"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_of_instances = []
        filename = f"{cls.__name__}.json"
        try:
            with open(filename) as file:
                str_list_of_dict = file.read()
        except FileNotFoundError:
            return []
        else:
            list_output = cls.from_json_string(str_list_of_dict)
            for dictionary in list_output:
                list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the CSV serialization of a list of objects to a file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    filednames = ["id", "width", "height", "x", "y"]
                else:
                    filednames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=filednames)

                new_list_dict = []

                converted_dict = {}

                for d in list_dicts:
                    for key, value in d.items():
                        converted_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict

                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))

                return list_of_instances
        except FileNotFoundError:
            return []
