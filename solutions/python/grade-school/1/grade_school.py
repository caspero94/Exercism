class School:
    def __init__(self):
        self.db = {}
        self.res = []

    def add_student(self, name, grade):
        if name not in self.db:
            self.db[name] = grade
            self.res.append(True)
        else:
            self.res.append(False)

    def roster(self):
        ros = []
        if len(self.db.values()) > 0:
            for x in range(min(self.db.values()), max(self.db.values())+1):
                for y in self.grade(x):
                    ros.append(y)
        return ros

    def grade(self, grade_number):
        gra = []
        for x in self.db.items():
            if x[1] == grade_number:
                gra.append(x[0])
        return sorted(gra)

    def added(self):
        return self.res
