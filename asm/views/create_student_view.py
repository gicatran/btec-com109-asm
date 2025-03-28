from asm.views import View


class CreateStudentView(View):
    def show(self):
        try:
            print("Create Student")
            self.print_divider()
            name = input("Enter name: ")
            grades = []

            if not name:
                raise ValueError("Name cannot be empty!")

            while True:
                course_name = input("Enter course name: ")
                score = float(input("Enter score: "))
                credit = float(input("Enter credit: "))

                if not course_name:
                    raise ValueError("Course name cannot be empty!")
                if score < 0 or score > 10:
                    raise ValueError("Grade must be between 0 and 10!")
                if credit <= 0:
                    raise ValueError("Credit must be greater than 0!")

                grades.append((course_name, score, credit))

                if input("Add another course? (y/n): ") == "n":
                    break

            self.print_divider()
            print("Student created successfully!")
            self.print_divider()

            return name, grades
        except ValueError as e:
            print(f"Error: {e}")
            self.clear()
        except Exception:
            print("Error: Invalid input!")
            self.clear()
