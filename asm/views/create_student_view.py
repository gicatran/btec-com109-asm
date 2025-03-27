from asm.views import View

class CreateStudentView(View):
    def show(self):
        try:
            print("Create Student")
            name = input("Enter name: ")
            grades = []

            if not name:
                raise ValueError("Name cannot be empty!")

            while True:
                score = float(input("Enter score: "))
                credit = float(input("Enter credit: "))

                if score < 0 or score > 10:
                    raise ValueError("Grade must be between 0 and 10!")
                if credit <= 0:
                    raise ValueError("Credit must be greater than 0!")
                
                grades.append((score, credit))

                if input("Add another grade? (y/n): ") == "n":
                    break

            print("Student added successfully!")

            return name, grades
        except ValueError as e:
            print(e)
            self.clear()
        except Exception as e:
            print(e)
            self.clear()