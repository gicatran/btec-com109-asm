from asm.utils import Database

class StudentController:
    def __init__(self):
        Database.load()

    def create(self, name, grades):
        return Database.create(name, grades)
    
    def read_all(self):
        return Database.read_all()