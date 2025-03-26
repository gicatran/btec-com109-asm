from asm.views import View

class MainMenuView(View):
    def handle_input(self, app):
        try:
            print("Main Menu")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                app.set_add_student_view()
            elif choice == "2":
                app.set_display_all_students_view()
            elif choice == "3":
                app.stop()
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(e)
            app.reset_view()
        except Exception as e:
            print("Invalid input!")
            app.reset_view()