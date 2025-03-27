from asm.views import View

class ShowAllStudentsView(View):
    def show(self, *args):
        try:
            print("Show All Students")
            students = args[0]

            if not students:
                raise Exception("No students found!")

            for student in students:
                print(f"Name: {student.name}")
                for score, credit in student.grades:
                    print(f"Score: {score}, Credit: {credit}")
                print(f"GPA: {student.calculate_gpa()}")
                print()
        except Exception as e:
            print(e)
            self.clear()