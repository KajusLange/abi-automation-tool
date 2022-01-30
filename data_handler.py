# data_handler.py

class Student:
    def __init__(self, name, vorname, pb, wdh):
        self.name = name
        self.vorname = vorname
        self.pb = pb
        self.wdh = wdh
        self.kurse = []


class Course:
    def __init__(self, id, title, aufgabenfeld, abi, points, diffkurs):
        self.id = id
        self.title = title
        self.agf = aufgabenfeld
        self.abi = abi
        self.points = points
        self.diffkurs = diffkurs
        #self.points.sort(reverse=True)


class Leistungskurs(Course):
    def __init__(self, id, title, aufgabenfeld, abi, points, diffkurs):
        super().__init__(id, title, aufgabenfeld, abi, points, diffkurs)

    def sum_points(self):
        return sum(self.points * 2)

    def avg_points(self):
        return round(sum(self.points) / 4, 2)

    def n_defizite(self):
        return sum(1 for x in self.points if x < 5)


class Grundkurs(Course):
    def __init__(self, id, title, aufgabenfeld, abi, points, diffkurs):
        super().__init__(id, title, aufgabenfeld, abi, points, diffkurs)
        self.pflicht_n = 0
        self.extra_n = 0

    def sum_points(self):
        return sum(self.points)

    def avg_points(self):
        return round(self.sum_points() / 4, 2)

    def pflicht_points(self):
        return sum(self.points[0:self.pflicht_n])

    def extra_points(self):
        p, e = self.pflicht_n, self.extra_n
        return sum(self.points[p:p+e])

    def pflicht_defizite(self):
        return 0 if self.pflicht_n == 0 else sum(1 for x in self.points[0:self.pflicht_n] if x < 5)

    def extra_defizite(self):
        p, e = self.pflicht_n, self.extra_n
        return 0 if e == 0 else sum(1 for x in self.points[p:p+e] if x < 5)
