from asm.controllers import Controller
from asm.models import StudentModel
from asm.views import MainMenuView, CreateStudentView, ShowAllStudentsView


class StudentController(Controller):
    def __init__(self, app):
        super().__init__(app, StudentModel(), MainMenuView())

    def handle_view(self):
        if isinstance(self.view, MainMenuView):
            choice = self.view.show()

            if not choice:
                return

            match choice:
                case 1:
                    self.set_view(CreateStudentView())
                case 2:
                    self.set_view(ShowAllStudentsView())
                case 3:
                    self.app.stop()
        elif isinstance(self.view, CreateStudentView):
            student = StudentModel()
            created_student = self.view.show(student)

            if not created_student:
                return

            self.create(created_student)

            self.set_view(MainMenuView())
        elif isinstance(self.view, ShowAllStudentsView):
            students = self.read_all()
            self.view.show(students)

            self.set_view(MainMenuView())
