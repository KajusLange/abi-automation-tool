# data_handler.py

class Student:
    def __init__(self, name, vorname, pb, wdh):
        self.name = name
        self.vorname = vorname
        self.pb = pb
        self.wdh = wdh
        self.kurse = []


class Course:
    def __init__(self, id, title, abi, points):
        self.id = id
        self.title = title
        self.abi = abi
        self.points = points
