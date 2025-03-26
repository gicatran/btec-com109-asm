from asm.views import View

class DisplayAllStudentsView(View):
    def handle_input(self, app):
        try:
            print("Display All Students")
            students = app.controller.read_all()

            if not students:
                raise Exception("No students found!")

            for student in students:
                print(f"Name: {student.name}")
                for score, credit in student.grades:
                    print(f"Score: {score}, Credit: {credit}")
                print(f"GPA: {student.calculate_gpa()}")
                print()

            app.set_main_menu_view()
        except Exception as e:
            print(e)
            app.reset_view()