class StudentModel():
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def calculate_gpa(self):
        if not self.grades:
            return 0
        
        total_grades = 0
        total_credits = 0

        for score, credit in self.grades:
            total_grades += score * credit
            total_credits += credit

        return round(total_grades / total_credits, 2)