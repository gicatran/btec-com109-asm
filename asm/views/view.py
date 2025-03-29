import os
from abc import abstractmethod


class View:
    def show(self, *args):
        """
            Show the view. This method should be overridden in subclasses.

            Args:
                *args: The arguments to show in the view (optional).

            Returns:
                data: The data to be shown in the view.
        """
        raise NotImplementedError

    def print_divider(self):
        print("--------------------------------------------------")

    def clear(self):
        input("Press any key to continue...")
        os.system("cls")
