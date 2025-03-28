from asm.models import Model


class StudentModel(Model):
    def __init__(self, name="", grades=[]):
        super().__init__("students")
        self.name = name
        self.grades = grades

    def __str__(self):
        text = self.name

        for course_name, score, credit in self.grades:
            text += f',{course_name}-{score}-{credit}'

        return text

    def parse_from_string(self, string):
        parts = string.split(",")
        self.name = parts[0]
        self.grades = []

        for part in parts[1:]:
            course_name, score, credit = part.split("-")
            self.grades.append((course_name, float(score), int(credit)))

        return StudentModel(self.name, self.grades)

    def calculate_gpa(self):
        if not self.grades:
            return 0

        total_grades = 0
        total_credits = 0

        for course_name, score, credit in self.grades:
            total_grades += score * credit
            total_credits += credit

        return round(total_grades / total_credits, 2)
