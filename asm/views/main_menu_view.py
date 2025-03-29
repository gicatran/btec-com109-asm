from asm.views import View


class MainMenuView(View):
    def show(self):
        try:
            print("Main Menu")
            self.print_divider()
            print("1. Create Student")
            print("2. Show All Students")
            print("3. Exit")
            self.print_divider()
            choice = int(input("Enter choice: "))

            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice")
            
            return choice
        except ValueError as e:
            print(f"Error: {e}")
            self.clear()
        except Exception:
            print("Error: Invalid input!")
            self.clear()
