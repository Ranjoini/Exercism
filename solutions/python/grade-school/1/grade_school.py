class School:
    def __init__(self) -> None:
        # dict[str, int] means the keys are strings (names) and values are integers (grades)
        self.directory: dict[str, int] = {}
        # list[bool] means this array will only ever contain True or False
        self.add_log: list[bool] = []

    def add_student(self, name: str, grade: int) -> None:
        if name in self.directory:
            self.add_log.append(False)
        else:
            self.directory[name] = grade
            self.add_log.append(True)

    def added(self) -> list[bool]:
        return self.add_log

    def grade(self, grade_number: int) -> list[str]:
        students_in_grade: list[str] = [
            name for name, g in self.directory.items() if g == grade_number
        ]
        return sorted(students_in_grade)

    def roster(self) -> list[str]:
        all_students = self.directory.items()
        sorted_students = sorted(all_students, key=lambda item: (item[1], item[0]))
        return [name for name, grade in sorted_students]
