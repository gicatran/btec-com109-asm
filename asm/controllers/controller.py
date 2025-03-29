from typing import Generic
from asm.utils import Database
from asm.views import View
from asm.models import Model

class Controller():
    def __init__(self, app, model: Model, view: View):
        self.app = app
        self.model = model
        self.view = view
        
        Database.load()

    def create(self, value):
        Database.create(self.model.table_name, value)

    def read_all(self):
        data = Database.read_all(self.model.table_name)
        parsed_data = []

        for line in data:
            parsed_data.append(self.model.__class__.parse_from_string(line))

        return parsed_data

    def set_view(self, view: View):
        self.view = view
        self.view.clear()

    def handle_view(self):
        """
            Handle the view logic. This method should be overridden in subclasses.
        """

        raise NotImplementedError