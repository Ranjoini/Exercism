from typing import ClassVar


class Garden:
    STUDENTS_NAMES: ClassVar[list] = [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Fred",
        "Ginny",
        "Harriet",
        "Ileana",
        "Joseph",
        "Kincaid",
        "Larry",
    ]
    PLANT_NAMES: ClassVar[dict] = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets",
    }

    def __init__(self, diagram, students=None):
        if students is None:
            self.students = self.STUDENTS_NAMES
        else:
            self.students = sorted(students)
        self.row1, self.row2 = diagram.splitlines()

    def plants(self, student):
        index = self.students.index(student)
        start = index * 2
        end = start + 2
        student_cups = self.row1[start:end] + self.row2[start:end]
        return [self.PLANT_NAMES[cup] for cup in student_cups]
