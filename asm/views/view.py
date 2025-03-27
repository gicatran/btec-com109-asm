import os
from abc import abstractmethod

class View:
    def show(self, *args):
        raise NotImplementedError
    
    def clear(self):
        input("\nPress any key to continue...")
        os.system("cls")