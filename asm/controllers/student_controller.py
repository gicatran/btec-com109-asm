from asm.controllers import Controller
from asm.models import StudentModel
from asm.views import MainMenuView, CreateStudentView, ShowAllStudentsView


class StudentController(Controller):
    def __init__(self, app):
        super().__init__(app, StudentModel(), MainMenuView())

    def handle_view(self):
        if isinstance(self.view, MainMenuView):
            response = self.view.show()

            if not response:
                return

            match response:
                case 1:
                    self.set_view(CreateStudentView())
                case 2:
                    self.set_view(ShowAllStudentsView())
                case 3:
                    self.app.stop()
        elif isinstance(self.view, CreateStudentView):
            response = self.view.show()

            if not response:
                return

            name, grades = response

            student = StudentModel(name, grades)
            self.create(student)

            self.set_view(MainMenuView())
        elif isinstance(self.view, ShowAllStudentsView):
            students = self.read_all()
            self.view.show(students)

            self.set_view(MainMenuView())
