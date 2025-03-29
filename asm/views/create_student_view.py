from asm.views import View


class CreateStudentView(View):
    def show(self, *args):
        try:
            print("Create Student")
            self.print_divider()
            student = args[0]
            student.set_name(input("Enter name: "))

            while True:
                course_name = input("Enter course name: ")
                score = float(input("Enter score: "))
                credit = int(input("Enter credit: "))

                student.add_grade((course_name, score, credit))

                if input("Add another course? (y/n): ") == "n":
                    break

            self.print_divider()
            print("Student created successfully!")
            self.print_divider()

            return student
        except ValueError as e:
            print(f"Error: {e}")
            self.clear()
        except Exception:
            print("Error: Invalid input!")
            self.clear()