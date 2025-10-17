class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):

        self.name_plants= {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}
        self.diagram1, self.diagram2 = diagram.split("\n")
        self.students = sorted(students)
        self.dicionario = {}
        self.get_plants()

    def get_plants(self):
        x = 0
        for student in self.students:
            if len(self.diagram1) < x+1: break
            self.dicionario[student] = [self.diagram1[x], self.diagram1[x+1], self.diagram2[x], self.diagram2[x+1],]
            x += 2

    def plants(self, name_student):
        
        return [self.name_plants[initial] for initial in self.dicionario[name_student]]
        
                