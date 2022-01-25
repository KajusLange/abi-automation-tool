# data_handler.py

class Student:
    def __init__(self, name, vorname, pb, wdh):
        self.name = name
        self.vorname = vorname
        self.pb = pb
        self.wdh = wdh
        self.kurse = []


class Course:
    def __init__(self, id, title, aufgabenfeld, abi, points):
        self.id = id
        self.title = title
        self.agf = aufgabenfeld
        self.abi = abi
        self.points = points


class Leistungskurs(Course):
    def __init__(self, id, title, aufgabenfeld, abi, points):
        super(Leistungskurs, self).__init__(id, title, aufgabenfeld, abi, points)
