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
        self.points.sort(reversed=True)


class Leistungskurs(Course):
    def __init__(self, id, title, aufgabenfeld, abi, points):
        super(Leistungskurs, self).__init__(id, title, aufgabenfeld, abi, points)

    def sum_points(self):
        return sum(self.points * 2)

    def avg_points(self):
        return round(sum(self.points) / 4, 2)

    def n_defizite(self):
        return sum(1 for x in self.points if x < 5)


class Grundkurs(Course):
    def __init__(self, id, title, aufgabenfeld, abi, points):
        super(Grundkurs, self).__init__(id, title, aufgabenfeld, abi, points)
        self.pflicht_n = 0
        self.extra_n = 0

    def sum_points(self):
        return sum(self.points)

    def avg_points(self):
        return round(self.sum_points() / 4, 2)
