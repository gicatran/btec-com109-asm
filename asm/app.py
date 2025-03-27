from asm.controllers import StudentController

class App:
    def __init__(self):
        self.__running = True
        self.__controller = StudentController(self)
    
    def run(self):
        while self.__running:
            self.__controller.handle_view()

    def stop(self):
        self.__running = False