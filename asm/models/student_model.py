from asm.models import Model


class StudentModel(Model):
    def __init__(self, name="temp", grades=[]):
        super().__init__("students")

        self.set_name(name)
        self.set_grades(grades)

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if not name:
            raise ValueError("Name cannot be empty!")

        self.__name = name

    def get_grades(self):
        return self.__grades
    
    def set_grades(self, grades):
        if not isinstance(grades, list):
            raise ValueError("Grades must be a list")
        
        for grade in grades:
            if not isinstance(grade, tuple) or len(grade) != 3:
                raise ValueError("Each grade must be a tuple with three elements")
            course_name, score, credit = grade
            if not course_name or score < 0 or score > 10 or credit <= 0:
                raise ValueError("Invalid grade data")
            
        self.__grades = grades
    
    def add_grade(self, grade):
        course_name, score, credit = grade

        if not course_name:
            raise ValueError("Course name cannot be empty!")
        if score < 0 or score > 10:
            raise ValueError("Grade must be between 0 and 10!")
        if credit <= 0:
            raise ValueError("Credit must be greater than 0!")
        
        self.__grades.append(grade)

    def __str__(self):
        text = self.__name

        for course_name, score, credit in self.__grades:
            text += f',{course_name}-{score}-{credit}'

        return text

    @classmethod
    def parse_from_string(cls, string: str):
        parts = string.split(",")
        name = parts[0]
        grades = []

        for part in parts[1:]:
            course_name, score, credit = part.split("-")
            grades.append((course_name, float(score), int(credit)))

        return StudentModel(name, grades)

    def calculate_gpa(self):
        if not self.__grades:
            return 0

        total_grades = 0
        total_credits = 0

        for course_name, score, credit in self.__grades:
            total_grades += score * credit
            total_credits += credit

        return round(total_grades / total_credits, 2)
