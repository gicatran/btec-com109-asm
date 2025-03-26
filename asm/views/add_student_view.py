from asm.views import View

class AddStudentView(View):
    def handle_input(self, app):
        try:
            print("Add Student")
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

            app.controller.create(name, grades)
            print("Student added successfully!")
            app.set_main_menu_view()
        except ValueError as e:
            print(e)
            app.reset_view()
        except Exception as e:
            print(e)
            app.reset_view()