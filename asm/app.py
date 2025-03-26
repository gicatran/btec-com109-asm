from asm.views import MainMenuView, AddStudentView, DisplayAllStudentsView
from asm.controllers import StudentController

class App:
    def __init__(self):
        self.__running = True

        self.controller = StudentController()
        self.view = MainMenuView()
    
    def run(self):
        while self.__running:
            self.view.handle_input(self)

    def stop(self):
        self.__running = False

    def set_view(self, view):
        self.reset_view()
        self.view = view()

    def set_main_menu_view(self):
        self.set_view(MainMenuView)

    def set_add_student_view(self):
        self.set_view(AddStudentView)

    def set_display_all_students_view(self):
        self.set_view(DisplayAllStudentsView)

    def reset_view(self):
        self.view.clear()