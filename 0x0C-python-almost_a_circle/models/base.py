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
        """Serializes list_objs in CSV format and writes to a file"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = f"{class_name}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if class_name == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif class_name == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes data from a CSV file and returns a list of instances"""
        class_name = cls.__name__
        filename = f"{class_name}.csv"
        instances = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if class_name == "Rectangle":
                    instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]))
                elif class_name == "Square":
                    instance = cls(int(row[0]), int(row[1]), int(row[2]), int(row[3]))
                instances.append(instance)
        return instances
