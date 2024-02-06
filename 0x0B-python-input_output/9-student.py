#!/usr/bin/python3

"""
module:9-student
resource: student"""


class Student:
    """Initializes a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        Student_dict = {}
        for attr_name in self.__dict__:
            attr_value = getattr(self, attr_name)
            Student_dict[attr_name] = attr_value
        return Student_dict
