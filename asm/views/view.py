import os
from abc import abstractmethod


class View:
    def show(self, *args):
        raise NotImplementedError

    def print_divider(self):
        print("--------------------------------------------------")

    def clear(self):
        input("Press any key to continue...")
        os.system("cls")
