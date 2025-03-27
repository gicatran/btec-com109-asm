from asm.views import View

class MainMenuView(View):
    def show(self):
        try:
            print("Main Menu")
            print("1. Create Student")
            print("2. Show All Students")
            print("3. Exit")
            choice = int(input("Enter choice: "))

            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice")
            
            return choice
        except ValueError as e:
            print(e)
            self.clear()
        except Exception as e:
            print("Invalid input!")
            self.clear()