from asm.models import StudentModel

class Database:
    __data = []

    @classmethod
    def load(self):
        try:
            with open("database.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    name = parts[0]
                    grades = []

                    for entry in parts[1:]:
                        grade = entry.split("-")
                        score = float(grade[0])
                        credit = int(grade[1])
                        grades.append((score, credit))

                    student = StudentModel(name, grades)
                    self.__data.append(student)
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def save(self):
        try:
            with open("database.txt", "w") as file:
                for student in self.__data:
                    file.write(f"{student.name}")
                    for score, credit in student.grades:
                        file.write(",")
                        file.write(f"{score}-{credit}")
                    file.write("\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def create(self, name, grades):
        student = StudentModel(name, grades)

        self.__data.append(student)
        self.save()

    @classmethod
    def read_all(self):
        return self.__data