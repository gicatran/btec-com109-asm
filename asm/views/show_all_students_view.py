from asm.views import View


class ShowAllStudentsView(View):
    def show(self, *args):
        try:
            print("Show All Students")
            self.print_divider()
            students = args[0]

            if not students:
                raise Exception("No students found!")

            for student in students:
                print(f"Name: {student.name}\n")
                for course_name, score, credit in student.grades:
                    print(
                        f"Course: {course_name}\n Score: {score}\n Credit: {credit}\n")
                print(f"Final GPA: {student.calculate_gpa()}")
                self.print_divider()
        except Exception as e:
            print(f"Error: {e}")
            self.clear()
